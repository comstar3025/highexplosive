# HighExplosive.net

Source for [www.highexplosive.net](https://www.highexplosive.net).

First-time setup: **[SETUP.md](SETUP.md)**.

```sh
python3 -m pip install --user markdown PyYAML
python3 scripts/build.py --serve        # http://localhost:8080
```

`--drafts` includes pages marked `draft: true`. `--port N` to change the port.

## Layout

```
content/index.md    the front page — front matter only: theme, links
content/_later/     sections, parked. A leading _ is skipped by the build.
static/             copied to the site root verbatim
  tools/comparator/index.html    the comparator, as built
templates/          bare.html (front page) and base.html (full pages)
scripts/build.py    the build
site.yaml           name, domain, theme, footer line
```

Pushing to `main` builds and publishes via GitHub Actions.

## Licence

Original content: use it, adapt it, no attribution needed. Anta under the SIL
Open Font License (`static/fonts/Anta-OFL.txt`). BattleTech is a trademark of
The Topps Company, Inc.; unofficial fan work.
