#!/usr/bin/env python3
"""
High Explosive — static site builder.

Turns the Markdown under content/ into a plain HTML site in _site/. There is
no framework here and nothing to keep up to date: one dependency (markdown),
one template, one pass. If this file ever stops working you can read the whole
thing in ten minutes and fix it.

    python3 scripts/build.py            build into _site/
    python3 scripts/build.py --serve    build, then serve at localhost:8080
    python3 scripts/build.py --drafts   include pages marked draft: true

How content is organised
------------------------
content/
    index.md                  the homepage
    about.md                  a standalone page          -> /about/
    tools/
        _section.md           the section itself         -> /tools/
        comparator.md         an entry in that section   -> /tools/comparator/
    battle-reports/
        _section.md
        2026-08-10-first.md                              -> /battle-reports/first/

A new section is a new folder with a _section.md in it. A new page is a new
.md file. Nothing else needs editing — the navigation, the section indexes,
the homepage list and the feed all follow from what is on disk.

Front matter keys
-----------------
Every .md file may start with a YAML block between --- lines.

  title:      required. Shown as the heading and in listings.
  summary:    one or two sentences, used on cards and in the feed.
  date:       YYYY-MM-DD. Entries with a date sort newest first.
  updated:    YYYY-MM-DD, if it has been revised since.
  draft:      true to keep it out of the build until it is ready.
  link:       publish this as a listing card that points somewhere else
              instead of generating a page (used for the comparator, which
              is a whole app rather than a page of prose).
  hidden:     true to build the page but keep it out of listings.
  toc:        true to insert a table of contents where [TOC] appears.

And in a _section.md, additionally:

  nav_order:  position in the site navigation. Lower is further left.
  nav:        false to build the section but keep it out of the navigation.
  layout:     "cards" (default) or "list" for a dated, blog-style index.
  empty:      the message shown while the section has no entries yet.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit(
        "This build needs the 'markdown' package.\n"
        "Install it with:  python3 -m pip install --user markdown\n"
    )

try:
    import yaml
except ImportError:
    yaml = None  # front matter falls back to a minimal parser


ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"
TEMPLATES = ROOT / "templates"
OUT = ROOT / "_site"

MD_EXTENSIONS = [
    "extra",        # tables, fenced code, footnotes, attribute lists, def lists
    "sane_lists",
    "smarty",       # curly quotes and proper dashes
    "toc",
    "admonition",
]
MD_CONFIG = {"toc": {"permalink": False}}


# --------------------------------------------------------------------------
# configuration
# --------------------------------------------------------------------------

DEFAULT_SITE = {
    "name": "High Explosive",
    "tagline": "",
    "base_url": "",
    "description": "",
    "legal": "",
}


def load_site_config() -> dict:
    cfg = dict(DEFAULT_SITE)
    path = ROOT / "site.yaml"
    if path.exists():
        raw = path.read_text(encoding="utf-8")
        parsed = yaml.safe_load(raw) if yaml else parse_simple_yaml(raw)
        if parsed:
            cfg.update(parsed)
    cfg["base_url"] = str(cfg.get("base_url", "")).rstrip("/")
    return cfg


def parse_simple_yaml(text: str) -> dict:
    """A very small YAML subset, used only if PyYAML is not installed.

    Handles `key: value`, quoted values, true/false, and `key: |` blocks.
    That covers everything this site's front matter actually uses.
    """
    out: dict = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value in ("|", ">", "|-", ">-"):
            block = []
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                block.append(lines[i].strip() if value.startswith(">") else lines[i].lstrip())
                i += 1
            joined = (" " if value.startswith(">") else "\n").join(block).strip()
            out[key] = joined
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        low = value.lower()
        if low in ("true", "yes"):
            out[key] = True
        elif low in ("false", "no"):
            out[key] = False
        elif low in ("", "null", "~"):
            out[key] = ""
        elif re.fullmatch(r"-?\d+", value):
            out[key] = int(value)
        else:
            out[key] = value
    return out


# --------------------------------------------------------------------------
# front matter
# --------------------------------------------------------------------------

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)


def split_front_matter(text: str) -> tuple[dict, str]:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}, text
    raw = match.group(1)
    data = (yaml.safe_load(raw) if yaml else parse_simple_yaml(raw)) or {}
    if not isinstance(data, dict):
        data = {}
    return data, text[match.end():]


def as_date(value) -> dt.date | None:
    if value is None or value == "":
        return None
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return dt.datetime.strptime(str(value).strip(), fmt).date()
        except ValueError:
            continue
    return None


def fmt_date(date: dt.date | None) -> str:
    return date.strftime("%d %B %Y").lstrip("0") if date else ""


def slugify(text: str) -> str:
    """Filenames become URLs, so make them safe ones regardless of how the
    file was named — lower case, no spaces, no accents, no surprises."""
    import unicodedata
    text = unicodedata.normalize("NFKD", str(text))
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "page"


# --------------------------------------------------------------------------
# model
# --------------------------------------------------------------------------

class Page:
    def __init__(self, source: Path, meta: dict, body: str, section: "Section | None"):
        self.source = source
        self.meta = meta
        self.body = body
        self.section = section
        self.slug = slugify(re.sub(r"^\d{4}-\d{2}-\d{2}-", "", source.stem))

        self.title = str(meta.get("title") or self.slug.replace("-", " ").title())
        self.summary = str(meta.get("summary") or "").strip()
        self.date = as_date(meta.get("date"))
        self.updated = as_date(meta.get("updated"))
        self.draft = bool(meta.get("draft"))
        self.hidden = bool(meta.get("hidden"))
        self.link = str(meta.get("link") or "").strip()
        self.external = self.link.startswith(("http://", "https://"))

    @property
    def url(self) -> str:
        if self.link:
            return self.link
        if self.section:
            return f"/{self.section.slug}/{self.slug}/"
        return f"/{self.slug}/"

    @property
    def output_path(self) -> Path:
        if self.section:
            return OUT / self.section.slug / self.slug / "index.html"
        return OUT / self.slug / "index.html"


class Section:
    def __init__(self, directory: Path, meta: dict, body: str):
        self.directory = directory
        self.slug = slugify(directory.name)
        self.meta = meta
        self.body = body

        self.title = str(meta.get("title") or self.slug.replace("-", " ").title())
        self.summary = str(meta.get("summary") or "").strip()
        self.nav_order = int(meta.get("nav_order", 100))
        self.in_nav = meta.get("nav", True) is not False
        self.layout = str(meta.get("layout") or "cards").lower()
        self.empty_text = str(
            meta.get("empty") or "Nothing here yet — this section is waiting on its first entry."
        )
        self.pages: list[Page] = []

    @property
    def url(self) -> str:
        return f"/{self.slug}/"

    @property
    def listed(self) -> list[Page]:
        visible = [p for p in self.pages if not p.hidden]
        if self.layout == "list":
            return sorted(visible, key=lambda p: (p.date or dt.date.min, p.title), reverse=True)
        return sorted(
            visible,
            key=lambda p: (int(p.meta.get("order", 50)), -(p.date or dt.date.min).toordinal(), p.title),
        )


# --------------------------------------------------------------------------
# rendering helpers
# --------------------------------------------------------------------------

TOKEN = re.compile(r"\{\{\s*(\w+)\s*\}\}")


def render_template(template: str, context: dict) -> str:
    """One pass, so page content containing {{ }} can never be re-substituted."""
    return TOKEN.sub(lambda m: str(context.get(m.group(1), "")), template)


def md_to_html(text: str, use_toc: bool = False) -> str:
    converter = markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG)
    out = converter.convert(text)
    # Let wide tables scroll instead of breaking the layout on a phone.
    out = re.sub(r"<table>", '<div class="table-wrap"><table>', out)
    out = re.sub(r"</table>", "</table></div>", out)
    return out


def strip_tags(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


def card(url: str, kicker: str, title: str, summary: str, foot: str = "",
         foot_class: str = "card-date", external: bool = False) -> str:
    attrs = ' target="_blank" rel="noopener"' if external else ""
    arrow = " ↗" if external else ""
    return f"""      <a class="card" href="{esc(url)}"{attrs}>
        {f'<span class="card-kicker">{esc(kicker)}</span>' if kicker else ''}
        <span class="card-title">{esc(title)}{arrow}</span>
        <span class="card-summary">{esc(summary)}</span>
        {f'<span class="{foot_class}">{esc(foot)}</span>' if foot else ''}
      </a>"""


# --------------------------------------------------------------------------
# collection
# --------------------------------------------------------------------------

def collect(include_drafts: bool) -> tuple[list[Section], list[Page], Page | None]:
    sections: list[Section] = []
    loose: list[Page] = []
    home: Page | None = None

    for entry in sorted(CONTENT.iterdir()):
        if entry.name.startswith((".", "_")):
            continue

        if entry.is_dir():
            marker = entry / "_section.md"
            if not marker.exists():
                print(f"  ! skipping {entry.name}/ — no _section.md", file=sys.stderr)
                continue
            meta, body = split_front_matter(marker.read_text(encoding="utf-8"))
            section = Section(entry, meta, body)
            for md_file in sorted(entry.glob("*.md")):
                if md_file.name == "_section.md":
                    continue
                p_meta, p_body = split_front_matter(md_file.read_text(encoding="utf-8"))
                page = Page(md_file, p_meta, p_body, section)
                if page.draft and not include_drafts:
                    continue
                section.pages.append(page)
            sections.append(section)

        elif entry.suffix == ".md":
            meta, body = split_front_matter(entry.read_text(encoding="utf-8"))
            page = Page(entry, meta, body, None)
            if page.draft and not include_drafts:
                continue
            if entry.stem == "index":
                home = page
            else:
                loose.append(page)

    sections.sort(key=lambda s: (s.nav_order, s.title))
    return sections, loose, home


# --------------------------------------------------------------------------
# page writers
# --------------------------------------------------------------------------

class Builder:
    def __init__(self, site: dict, sections: list[Section],
                 nav_items: list[tuple[int, str, str]], cachebust: str):
        self.site = site
        self.sections = sections
        self.nav_items = sorted(nav_items)
        self.cachebust = cachebust
        self._templates: dict[str, str] = {}
        self.legal_html = md_to_html(str(site.get("legal", "")).strip())
        self.written: list[tuple[str, dt.date | None, str, str]] = []  # url, date, title, summary

    def load_template(self, name: str) -> str:
        if name not in self._templates:
            self._templates[name] = (TEMPLATES / name).read_text(encoding="utf-8")
        return self._templates[name]

    def nav_html(self, current: str) -> str:
        items = []
        for _order, title, url in self.nav_items:
            mark = ' aria-current="page"' if current.startswith(url) else ""
            items.append(f'      <a href="{url}"{mark}>{esc(title)}</a>')
        return "\n".join(items)

    def write(self, out_path: Path, *, url: str, title: str, description: str,
              content: str, og_type: str = "website", template: str = "base.html",
              extra: dict | None = None) -> None:
        base = self.site["base_url"]
        # A page may name its own browser/search title. Useful where the h1 is
        # the in-fiction name and the title has to be what people search for.
        page_title = (extra or {}).get("page_title") or (
            title if url == "/" else f"{title} — {self.site['name']}")
        theme = str(self.site.get("theme", "dark")).lower()
        page = render_template(self.load_template(template), {
            **(extra or {}),
            "theme": theme,
            "theme_color": "#ffffff" if theme == "light" else "#0f1216",
            "legal_short": esc(self.site.get("legal_short", "")),
            "page_title": esc(page_title),
            "title": esc(title),
            "description": esc(description or self.site.get("description", "")),
            "canonical": esc(base + url),
            "base_url": esc(base),
            "site_name": esc(self.site["name"]),
            "tagline": esc(self.site.get("tagline", "")),
            "og_type": og_type,
            "nav": self.nav_html(url),
            "content": content,
            "legal": self.legal_html,
            "cachebust": self.cachebust,
        })
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page, encoding="utf-8")

    # ---- schedule of issued material -------------------------------------

    def schedule_html(self, page: Page) -> str:
        """One card per series, each listing that series' files.

        Everything here comes from `series:` and `releases:` in the page's front
        matter. Adding a download is one entry in that list and nothing else —
        no markup, no prose. Grouping follows the `series` key; order within a
        group follows the list; group order follows first appearance.

        An entry with `status` instead of `href` renders unlinked and italic,
        which is the "in preparation" state.
        """
        series = page.meta.get("series") or {}
        releases = page.meta.get("releases") or []

        groups: dict[str, list[dict]] = {}
        for item in releases:
            groups.setdefault(str(item.get("series", "")), []).append(item)

        cards = []
        for name, items in groups.items():
            info = series.get(name) or {}
            head = ""
            if info.get("mark"):
                fallback = info.get("mark_fallback")
                img = (f'<img class="mark" src="{esc(info["mark"])}" '
                       f'alt="{esc(name)}" loading="lazy">')
                if fallback:
                    img = (f'<picture><source srcset="{esc(info["mark"])}" '
                           f'type="image/webp">'
                           f'<img class="mark" src="{esc(fallback)}" '
                           f'alt="{esc(name)}" loading="lazy"></picture>')
                head = img
            else:
                head = f'<p class="name">{esc(name)}</p>'

            blurb = (f'<div class="blurb">{md_to_html(str(info["blurb"]))}</div>'
                     if info.get("blurb") else "")

            rows = []
            for item in items:
                label, meta = str(item.get("label", "")), str(item.get("meta", ""))
                if item.get("href"):
                    title = f'<a href="{esc(item["href"])}">{esc(label)}</a>'
                else:
                    title = (f'<span class="pending">{esc(label)}'
                             f'{" — " + esc(item["status"]) if item.get("status") else ""}'
                             "</span>")
                # Thumbnails sit on the RIGHT. On the left, an entry without one
                # leaves a gap and the titles stop aligning.
                thumb = ""
                if item.get("thumb"):
                    srcset = (f' srcset="{esc(item["thumb"])} 1x, '
                              f'{esc(item["thumb2x"])} 2x"' if item.get("thumb2x") else "")
                    thumb = (f'<span class="thumb"><img src="{esc(item["thumb"])}"'
                             f'{srcset} alt="" loading="lazy"></span>')
                rows.append(f"""        <div class="item">
          <span class="txt">{title}
            <span class="meta">{esc(meta)}</span></span>
{thumb and "          " + thumb}
        </div>""")

            cards.append(f"""    <section class="card">
      {head}
      {blurb}
      <div class="files">
{chr(10).join(rows)}
      </div>
    </section>""")
        return "\n".join(cards)

    # ---- a page that brings its own template ------------------------------

    def write_templated_page(self, page: Page) -> None:
        """Front matter names a template; the front matter fills it in."""
        m = page.meta
        hero = ""
        if m.get("hero"):
            srcset = (f' srcset="{esc(m["hero"])} 1x, {esc(m["hero2x"])} 2x"'
                      if m.get("hero2x") else "")
            hero = (f'<img class="hero" src="{esc(m.get("hero_fallback") or m["hero"])}"'
                    f'{srcset} alt="{esc(m.get("hero_alt", ""))}">')

        memo_head = "\n".join(
            f'      <span><b>{esc(k)}</b> {esc(v)}</span>'
            for row in (m.get("memo_head") or []) for k, v in row.items())

        sign = m.get("signoff") or {}
        signoff = ""
        if sign:
            lines = "".join(f'<span class="role">{esc(l)}</span>'
                            for l in (sign.get("lines") or []))
            signoff = (f'<p class="signoff"><span class="name">'
                       f'{esc(sign.get("name", ""))}</span><br>{lines}</p>')

        # Social preview. A page that gets linked into a forum thread is judged
        # on the card the forum draws, so the image and the wording of that card
        # are worth setting apart from the page's own heading.
        base = self.site["base_url"]
        og_image = str(m.get("og_image") or "")
        if og_image and not og_image.startswith("http"):
            og_image = base + og_image
        og = []
        if og_image:
            og.append(f'<meta property="og:image" content="{esc(og_image)}">')
            for k in ("og_image_width", "og_image_height", "og_image_alt"):
                if m.get(k):
                    og.append(f'<meta property="og:image:{k[9:]}" '
                              f'content="{esc(m[k])}">')
        else:
            og.append(f'<meta property="og:image" content="{esc(base)}'
                      '/img/favicon-180.png">')
        og.append('<meta name="twitter:card" content="'
                  f'{"summary_large_image" if og_image else "summary"}">')

        caption = esc(m.get("caption", ""))
        self.write(page.output_path, url=page.url, title=page.title,
                   description=page.summary or str(m.get("standfirst", "")),
                   content=md_to_html(page.body), template=str(m["template"]),
                   extra={
                       "page_title": str(m.get("page_title") or "").strip(),
                       "og_title": esc(str(m.get("og_title")
                                             or page.title).strip()),
                       "og_description": esc(str(m.get("og_description")
                                                 or page.summary
                                                 or m.get("standfirst", "")).strip()),
                       "og_extra": "\n".join(og),
                       "standfirst": esc(m.get("standfirst", "")),
                       "hero": hero,
                       # Optional: an empty caption emits no element at all
                       # rather than an empty one that still takes margin.
                       "caption": (f'<p class="caption">{caption}</p>'
                                   if caption else ""),
                       "memo_head": memo_head,
                       "signoff": signoff,
                       "schedule_heading": esc(m.get("schedule_heading", "")),
                       "preamble": esc(str(m.get("preamble", "")).strip()),
                       "schedule": self.schedule_html(page),
                       "back_label": esc(m.get("back_label", self.site["name"])),
                   })

    # ---- individual content page ----------------------------------------

    def write_page(self, page: Page) -> None:
        if page.meta.get("template"):
            return self.write_templated_page(page)
        body_html = md_to_html(page.body, use_toc=bool(page.meta.get("toc")))
        bits = []
        if page.section:
            bits.append(f'<p class="kicker">{esc(page.section.title)}</p>')
        bits.append(f"<h1>{esc(page.title)}</h1>")

        meta_line = []
        if page.date:
            meta_line.append(
                f'<time datetime="{page.date.isoformat()}">{fmt_date(page.date)}</time>')
        if page.updated and page.updated != page.date:
            meta_line.append(f"updated {fmt_date(page.updated)}")
        if meta_line:
            bits.append(f'<p class="meta">{" &middot; ".join(meta_line)}</p>')

        if page.summary:
            bits.append(f'<p class="lede">{esc(page.summary)}</p>')

        bits.append(f'<div class="prose">\n{body_html}\n</div>')

        if page.section:
            bits.append(
                f'<div class="btn-row"><a class="btn" href="{page.section.url}">'
                f"&larr; All {esc(page.section.title.lower())}</a></div>")

        description = page.summary or strip_tags(body_html)[:180]
        self.write(page.output_path, url=page.url, title=page.title,
                   description=description, content="\n".join(bits), og_type="article")

        if not page.hidden:
            self.written.append((page.url, page.date, page.title, description))

    # ---- section index ---------------------------------------------------

    def write_section(self, section: Section) -> None:
        bits = [f"<h1>{esc(section.title)}</h1>"]
        if section.summary:
            bits.append(f'<p class="lede">{esc(section.summary)}</p>')
        if section.body.strip():
            bits.append(f'<div class="prose">\n{md_to_html(section.body)}\n</div>')

        entries = section.listed
        if not entries:
            bits.append(f'<p class="empty">{esc(section.empty_text)}</p>')
        elif section.layout == "list":
            rows = []
            for page in entries:
                meta = fmt_date(page.date) if page.date else ""
                rows.append(f"""    <li class="entry">
      {f'<p class="entry-meta">{esc(meta)}</p>' if meta else ''}
      <h2 class="entry-title"><a href="{esc(page.url)}">{esc(page.title)}</a></h2>
      {f'<p class="entry-summary">{esc(page.summary)}</p>' if page.summary else ''}
    </li>""")
            bits.append('<ul class="entries">\n' + "\n".join(rows) + "\n</ul>")
        else:
            cards = [card(p.url, "", p.title, p.summary,
                          fmt_date(p.date) if p.date else "", external=p.external)
                     for p in entries]
            bits.append('<div class="cards">\n' + "\n".join(cards) + "\n</div>")

        self.write(OUT / section.slug / "index.html", url=section.url,
                   title=section.title,
                   description=section.summary or f"{section.title} — {self.site['name']}",
                   content="\n".join(bits))

    # ---- homepage --------------------------------------------------------

    def write_home(self, home: Page | None) -> None:
        if home and home.meta.get("bare"):
            return self.write_bare_home(home)

        title = home.title if home else self.site["name"]
        summary = home.summary if home else self.site.get("description", "")
        body = md_to_html(home.body) if home and home.body.strip() else ""

        bits = [f"""<div class="hero">
  <h1>{esc(title)}</h1>
  {f'<p class="lede">{esc(summary)}</p>' if summary else ''}
</div>"""]

        if body:
            bits.append(f'<div class="prose">\n{body}\n</div>')

        # Most recent dated entries across every section.
        limit = int(home.meta.get("latest", 4)) if home else 4
        recent = sorted(
            [p for s in self.sections for p in s.pages
             if p.date and not p.hidden and not p.link],
            key=lambda p: (p.date, p.title), reverse=True)[:limit]
        if recent:
            bits.append("<h2>Latest</h2>")
            bits.append('<div class="cards">\n' + "\n".join(
                card(p.url, p.section.title if p.section else "", p.title,
                     p.summary, fmt_date(p.date)) for p in recent) + "\n</div>")

        if not home or home.meta.get("show_sections", True) is not False:
            bits.append("<h2>Sections</h2>")
            cards = []
            for section in self.sections:
                if not section.in_nav:
                    continue
                n = len([p for p in section.pages if not p.hidden])
                foot = ("1 entry" if n == 1 else f"{n} entries") if n else "Coming soon"
                cards.append(card(section.url, "", section.title, section.summary,
                                  foot, foot_class="card-count"))
            bits.append('<div class="cards">\n' + "\n".join(cards) + "\n</div>")

        self.write(OUT / "index.html", url="/", title=self.site["name"],
                   description=summary or self.site.get("description", ""),
                   content="\n".join(bits))

    # ---- bare homepage ---------------------------------------------------

    def write_bare_home(self, home: Page) -> None:
        """The sigil and a list of links. Nothing else on the page.

        Links come from the front matter of content/index.md:

            links:
              - title: Weapon Package Comparator
                url: /tools/comparator/
        """
        rows = []
        for item in (home.meta.get("links") or []):
            if isinstance(item, str):
                item = {"title": item, "url": item}
            url = str(item.get("url", "")).strip()
            external = url.startswith(("http://", "https://"))
            attrs = ' target="_blank" rel="noopener"' if external else ""
            rows.append(f'  <a href="{esc(url)}"{attrs}>{esc(item.get("title", url))}</a>')

        self.write(OUT / "index.html", url="/", title=self.site["name"],
                   description=self.site.get("description", ""),
                   content="\n".join(rows), template="bare.html")

    # ---- feed, sitemap, 404 ---------------------------------------------

    def write_feed(self) -> None:
        base = self.site["base_url"]
        dated = sorted([w for w in self.written if w[1]], key=lambda w: w[1], reverse=True)[:20]
        stamp = (max(w[1] for w in dated) if dated else dt.date.today()).isoformat()
        items = []
        for url, date, title, summary in dated:
            items.append(f"""  <entry>
    <title>{esc(title)}</title>
    <link href="{esc(base + url)}"/>
    <id>{esc(base + url)}</id>
    <updated>{date.isoformat()}T00:00:00Z</updated>
    <summary>{esc(summary)}</summary>
  </entry>""")
        feed = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>{esc(self.site['name'])}</title>
  <subtitle>{esc(self.site.get('description', ''))}</subtitle>
  <link href="{esc(base)}/feed.xml" rel="self"/>
  <link href="{esc(base)}/"/>
  <id>{esc(base)}/</id>
  <updated>{stamp}T00:00:00Z</updated>
{chr(10).join(items)}
</feed>
"""
        (OUT / "feed.xml").write_text(feed, encoding="utf-8")

    def write_sitemap(self, urls: list[str]) -> None:
        base = self.site["base_url"]
        entries = "\n".join(f"  <url><loc>{esc(base + u)}</loc></url>" for u in sorted(set(urls)))
        (OUT / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{entries}\n</urlset>\n", encoding="utf-8")
        (OUT / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n", encoding="utf-8")

    def write_404(self, bare: bool) -> None:
        if bare:
            self.write(OUT / "404.html", url="/404.html", title="Not found",
                       description="Not found.", template="bare.html",
                       content='  <a href="/">Not found</a>')
            return
        content = """<div class="hero">
  <h1>No contact</h1>
  <p class="lede">That page is not on this map. It may have moved, or it may
  never have existed.</p>
</div>
<div class="btn-row">
  <a class="btn btn-primary" href="/">Back to the front page</a>
</div>"""
        self.write(OUT / "404.html", url="/404.html", title="Page not found",
                   description="Page not found.", content=content)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def copy_static() -> None:
    if not STATIC.exists():
        return
    for item in STATIC.iterdir():
        target = OUT / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


def check_links(urls: set[str]) -> list[str]:
    """Warn about internal hrefs that no built page answers to."""
    problems = []
    for html_file in OUT.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8", errors="replace")
        for href in re.findall(r'href="(/[^"#?]*)"', text):
            if href in urls:
                continue
            candidate = OUT / href.lstrip("/")
            if candidate.exists() or (candidate / "index.html").exists():
                continue
            problems.append(f"{html_file.relative_to(OUT)} -> {href}")
    return sorted(set(problems))


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the High Explosive site.")
    parser.add_argument("--serve", action="store_true", help="serve the result on :8080")
    parser.add_argument("--drafts", action="store_true", help="include draft pages")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    site = load_site_config()
    sections, loose, home = collect(args.drafts)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    copy_static()

    # Sections make up the navigation; a loose page joins it by declaring a
    # nav_order of its own.
    nav_items = [(s.nav_order, s.title, s.url) for s in sections if s.in_nav]
    nav_items += [(int(p.meta["nav_order"]), p.title, p.url)
                  for p in loose if p.meta.get("nav_order") is not None]

    cachebust = dt.datetime.now().strftime("%Y%m%d%H%M")
    builder = Builder(site, sections, nav_items, cachebust)

    urls = {"/"}
    for section in sections:
        builder.write_section(section)
        urls.add(section.url)
        for page in section.pages:
            if page.link:
                continue           # a card only; the target is somewhere else
            builder.write_page(page)
            urls.add(page.url)
    for page in loose:
        builder.write_page(page)
        urls.add(page.url)

    builder.write_home(home)
    builder.write_feed()
    builder.write_sitemap(sorted(urls))
    builder.write_404(bare=bool(home and home.meta.get("bare")))

    pages = len(list(OUT.rglob("*.html")))
    entries = sum(len(s.pages) for s in sections)
    print(f"Built {pages} pages — {len(sections)} sections, {entries} entries -> {OUT}")

    for problem in check_links(urls):
        print(f"  ! dead internal link: {problem}", file=sys.stderr)

    if args.serve:
        import functools
        import http.server
        import socketserver
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", args.port), handler) as httpd:
            print(f"Serving http://localhost:{args.port}/  (Ctrl-C to stop)")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
