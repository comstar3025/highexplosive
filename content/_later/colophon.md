---
title: Colophon
summary: How this site is built, and what it is made of.
---

## Build

The site is a folder of Markdown files turned into plain HTML by a single
Python script, `scripts/build.py`. There is no framework, no JavaScript on
the content pages and no database. The only dependency is
[Python-Markdown](https://python-markdown.github.io/).

Pushing to the `main` branch on GitHub triggers a build and publishes the
result to GitHub Pages, which is where you are reading it.

## Type

Headings are set in **Anta** by Sergej Lebedev, used under the
[SIL Open Font License 1.1](/fonts/Anta-OFL.txt). It is the same face the
Weapon Package Comparator uses, which is where the rest of the palette comes
from too. Body text uses whatever sans-serif your system provides — that is a
deliberate choice, not an omission. It loads instantly and looks native
wherever you are.

## Credit

The starburst is the ComStar sigil. Rules data underlying the tools is derived
from the published BattleTech rulebooks and from
[MegaMek](https://megamek.org/), which is open source and much better at this
than any one person could be.
