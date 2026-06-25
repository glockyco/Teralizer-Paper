---
name: acmart-conventions
description: ACM acmart/TOSEM formatting conventions. Use when setting document class options, toggling review vs camera-ready, adding CCS concepts, the ACM Reference Format, or the copyright block.
---

# acmart / TOSEM conventions

- Document class: `\documentclass[manuscript,screen,review]{acmart}` for submission/review.
  For camera-ready, drop `review` and set the journal/volume/copyright per ACM instructions.
- Anonymous review: `acmart` `[anonymous,review]` strips author/affiliation; keep author macros
  intact and let the option control visibility — do not delete author blocks manually.
- CCS concepts: include `\begin{CCSXML}...\end{CCSXML}` + `\ccsdesc` blocks generated from the
  ACM CCS tool.
- ACM Reference Format and copyright block are emitted by the class — do not hand-format them.
- Use numbered citation style (ACM default).
