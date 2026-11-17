# Teralizer paper

LaTeX sources of the paper "Teralizer: Semantics-Based Test Generalization from Conventional Unit Tests to Property-Based Tests" by Johann Glock, Clemens Bauer and Martin Pinzger. The preprint is [arXiv:2512.14475](https://arxiv.org/abs/2512.14475).

Teralizer, its documentation and its analysis scripts are in [glockyco/Teralizer](https://github.com/glockyco/Teralizer). The replication package with the data behind the evaluation is on Zenodo as [10.5281/zenodo.17950380](https://doi.org/10.5281/zenodo.17950380).

## Build the paper

Build with a TeX Live installation that includes `latexmk`:

```sh
latexmk -pdf main.tex
```

## Cite

```bibtex
@misc{glock_2025_teralizer,
  title         = {Teralizer: Semantics-Based Test Generalization from Conventional Unit Tests to Property-Based Tests},
  author        = {Glock, Johann and Bauer, Clemens and Pinzger, Martin},
  year          = {2025},
  eprint        = {2512.14475},
  archivePrefix = {arXiv},
  primaryClass  = {cs.SE},
  url           = {https://arxiv.org/abs/2512.14475}
}
```

## License

The text, figures and tables of the paper are licensed under [CC BY 4.0](LICENSE-CC-BY-4.0). `elsarticle-harv.bst` keeps its own license.

`AGENTS.md` describes how the paper is written and built.
