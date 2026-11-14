"""Build and verify the arXiv source bundle of the paper.

arXiv publishes the sources, so the bundle holds them without comments. Shipping
the compiled bibliography pins it to the local build. The builder compiles with
pdfLaTeX alone and fails unless its text matches main.pdf, then writes the form's
fields to metadata.txt.
"""

import argparse
import difflib
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "arxiv"
REFERENCE = ROOT / "main"
VERBATIM = re.compile(r"\\(begin|end)\{(lstlisting|verbatim)\*?\}")
UNRESOLVED = re.compile(r"undefined references|Citation `[^']*' .*undefined|Reference `[^']*' .*undefined|Rerun to get")
ABSTRACT_LIMIT = 1920
LICENSE = "CC BY 4.0"
CATEGORY = "cs.SE"


class BuildError(Exception):
    pass


def comment_start(line: str) -> int | None:
    """Index of the first % that an even number of backslashes precedes."""
    position = line.find("%")
    while position >= 0:
        backslashes = len(line[:position]) - len(line[:position].rstrip("\\"))
        if backslashes % 2 == 0:
            return position
        position = line.find("%", position + 1)
    return None


def strip_comments(text: str) -> str:
    """Drop comment-only lines and comment text, keeping each % that ends a line of code."""
    lines = []
    verbatim = False
    for line in text.splitlines():
        if verbatim:
            lines.append(line)
            verbatim = not any(match.group(1) == "end" for match in VERBATIM.finditer(line))
            continue
        start = comment_start(line)
        code = line if start is None else line[:start + 1]
        if start is not None and not line[:start].strip():
            continue
        lines.append(code)
        verbatim = any(match.group(1) == "begin" for match in VERBATIM.finditer(code))
    return "\n".join(lines) + "\n"


def run(command: list[str], cwd: Path) -> None:
    result = subprocess.run(command, cwd=cwd, capture_output=True, check=False, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode:
        tail = "\n".join((result.stdout + result.stderr).splitlines()[-30:])
        raise BuildError(f"{' '.join(command)} failed in {cwd}:\n{tail}")


def pdf_text(pdf: Path) -> str:
    result = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, check=True,
                            text=True, encoding="utf-8", errors="replace")
    return result.stdout


def stage(target: Path) -> None:
    pending = [ROOT / "main.tex"]
    staged = set()
    while pending:
        path = pending.pop()
        if path in staged:
            continue
        staged.add(path)
        relative = path.relative_to(ROOT)
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix != ".tex":
            shutil.copyfile(path, destination)
            continue
        text = strip_comments(path.read_text(encoding="utf-8"))
        for command, name in re.findall(
                r"\\(input|include|includegraphics|lstinputlisting)\s*(?:\[[^\]]*\])?\s*\{([^{}]+)\}", text):
            dependency = ROOT / name
            extensions = (".tex",) if command in ("input", "include") else (
                ".pdf", ".png", ".jpg", ".jpeg") if command == "includegraphics" else ()
            if command == "includegraphics" or not dependency.is_file():
                dependency = next((Path(str(dependency) + extension) for extension in extensions
                                   if Path(str(dependency) + extension).is_file()), dependency)
            if not dependency.is_file():
                raise BuildError(f"Missing input: {name}")
            pending.append(dependency)
        destination.write_text(text, encoding="utf-8", newline="\n")
    bibliography = strip_comments(REFERENCE.with_suffix(".bbl").read_text(encoding="utf-8"))
    (target / "main.bbl").write_text(bibliography, encoding="utf-8", newline="\n")


def compile_bundle(source: Path, work: Path) -> Path:
    """Compile a copy of the bundle as arXiv does: pdfLaTeX only, from the shipped bibliography."""
    shutil.copytree(source, work)
    for _ in range(3):
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], work)
    log = (work / "main.log").read_text(encoding="utf-8", errors="replace")
    if problems := sorted(set(UNRESOLVED.findall(log))):
        raise BuildError(f"The bundle leaves unresolved references: {problems}")
    return work / "main.pdf"


def compare(reference: Path, bundle: Path) -> int:
    expected, actual = pdf_text(reference), pdf_text(bundle)
    if expected != actual:
        diff = difflib.unified_diff(expected.splitlines(), actual.splitlines(), "paper", "bundle", lineterm="", n=1)
        raise BuildError("The bundle's text differs from main.pdf:\n" + "\n".join(list(diff)[:40]))
    return expected.count("\f")


def plain(tex: str) -> str:
    """Text without the manuscript's markup, as arXiv's form fields require."""
    text = strip_comments(tex)
    definitions = strip_comments((ROOT / "main.tex").read_text(encoding="utf-8"))
    definitions += strip_comments((ROOT / "tables/generated/macros.tex").read_text(encoding="utf-8"))
    macros = dict(re.findall(r"\\newcommand\{\\(\w+)\}\{(.*)\}\s*$", definitions, re.MULTILINE))
    for _ in range(10):
        expanded = re.sub(r"\\(\w+)\{\}", lambda match: macros.get(match.group(1), match.group(0)), text)
        if expanded == text:
            break
        text = expanded
    text = re.sub(r"\\textbf\{([^{}]*)\}\s*", r"\1 ", text)
    text = re.sub(r"\\url\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:emph|textit|textsc)\{([^{}]*)\}", r"\1", text)
    text = text.replace("\\,", " ").replace("\\%", "%").replace("~", " ").replace("--", "-")
    text = re.sub(r"\s+", " ", text).strip()
    if leftover := sorted(set(re.findall(r"\\[A-Za-z]+|[{}$]", text))):
        raise BuildError(f"The text keeps markup that arXiv would show literally: {leftover}")
    return text


def metadata(pages: int, figures: int) -> str:
    tex = strip_comments((ROOT / "main.tex").read_text(encoding="utf-8"))
    title_match = re.search(r"^\\title(?:\[[^\]]*\])?\{(.+)\}\s*$", tex, re.MULTILINE)
    abstract_match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.DOTALL)
    keywords_match = re.search(r"\\keywords\{([^{}]*)\}", tex)
    if not title_match or not abstract_match or not keywords_match:
        raise BuildError("main.tex lacks a one-line \\title, an abstract or \\keywords.")
    title = plain(title_match.group(1).replace("\\\\", " "))
    authors = ", ".join(plain(author) for author in re.findall(r"\\author\{([^}]*)\}", tex))
    abstract = plain(abstract_match.group(1))
    if len(abstract) > ABSTRACT_LIMIT:
        raise BuildError(f"The abstract has {len(abstract)} characters, more than arXiv's {ABSTRACT_LIMIT}.")
    return (f"Title: {title}\nAuthors: {authors}\nComments: {pages} pages, {figures} figures\n"
            f"Category: {CATEGORY}\nLicense: {LICENSE}\nKeywords: {plain(keywords_match.group(1))}\n"
            f"Abstract ({len(abstract)} of {ABSTRACT_LIMIT} characters):\n{abstract}\n")


def archive(source: Path, target: Path) -> None:
    def anonymous_owner(info: tarfile.TarInfo) -> tarfile.TarInfo:
        info.uid = info.gid = 0
        info.uname = info.gname = ""
        return info

    with tarfile.open(target, "w:gz") as tar:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                tar.add(path, arcname=path.relative_to(source).as_posix(), filter=anonymous_owner)


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    try:
        run(["latexmk", "-pdf", "-interaction=nonstopmode", "-file-line-error", "-halt-on-error", "main.tex"], ROOT)
        if OUT.exists():
            shutil.rmtree(OUT)
        source = OUT / "source"
        stage(source)
        with tempfile.TemporaryDirectory(prefix="arxiv-") as directory:
            bundle_pdf = compile_bundle(source, Path(directory) / "bundle")
            pages = compare(REFERENCE.with_suffix(".pdf"), bundle_pdf)
            shutil.copyfile(bundle_pdf, OUT / "main.pdf")
        figures = sum(len(re.findall(r"\\begin\{figure\*?\}", path.read_text(encoding="utf-8")))
                      for path in source.rglob("*.tex"))
        archive(source, OUT / "arxiv-source.tar.gz")
        (OUT / "metadata.txt").write_text(metadata(pages, figures), encoding="utf-8", newline="\n")
    except (BuildError, OSError, subprocess.CalledProcessError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"Wrote {OUT / 'arxiv-source.tar.gz'}, {OUT / 'main.pdf'} and {OUT / 'metadata.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
