---
# ---------------------------------------------------------------------------
# A worked example of every front matter key. It has draft: true, so it does
# not appear on the site — copy it, rename it, delete this comment block and
# set draft to false when you are ready to publish.
#
# The same file works in any section. Only _section.md files are special.
# ---------------------------------------------------------------------------

title: Ammunition Explosions Are Survivable
summary: >
  One or two sentences. This is what appears on the section index card, in
  the feed, and as the grey standfirst under the title.
date: 2026-08-13
updated: 2026-08-20        # optional — omit if it has never been revised
draft: true                # set to false to publish
order: 50                  # cards layout only; lower sorts first
# hidden: true             # build the page but keep it out of all listings
# link: https://elsewhere  # publish as a card pointing somewhere else, no page
---

The body is ordinary Markdown. Everything below is here to show what the
stylesheet does with each kind of thing, so you can see what is available
before you need it.

## A second-level heading

Paragraphs, **bold**, *italic*, `inline code`, and
[a link](/tools/). Ellipses, dashes -- and "quotes" are typeset properly on
the way out.

### A third-level heading

- A bullet list
- With a second item
    - And a nested one
- Numbers work the same way with `1.`

> A blockquote, for pulling a line out of the rulebook or out of a game.

## Tables

Tables get a horizontal scroll on narrow screens rather than breaking the
layout, so a wide one is safe.

| Roll (2d6) | Result                      | Notes                     |
|-----------:|-----------------------------|---------------------------|
|        2–5 | No effect                   | Crew hold it together     |
|        6–8 | Ammunition cooks off         | Standard critical applies |
|       9–12 | Catastrophic                | As written                |

## Code and data

    Indented four spaces gives you a code block

```
Or fence it with three backticks
for record-sheet extracts and log output.
```

## Images

Put the file in `static/img/` and reference it from the site root:

![Alt text describing the image](/img/comstar.png)

## Footnotes

A claim that needs a source can carry one.[^1]

[^1]: *BattleMech Manual*, 6th printing, p. 42.

## Rules of thumb for this section

1. Say what went wrong in play before saying what the rule does.
2. State the cost. Every rule breaks something in exchange.
3. Note the date you last played with it.
