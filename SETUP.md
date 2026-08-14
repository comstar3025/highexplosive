# Getting highexplosive.net live

Four things happen here: the folder becomes a git repository, the repository
goes to GitHub, GitHub starts publishing it, and Gandi points the domain at
GitHub. About 30 minutes of work, then a wait for DNS.

Everything below assumes your GitHub username is **`comstar3025`**. If you use
a different account, substitute it everywhere.

---

## 0. Before anything: get this folder out of Dropbox

**Do this first.** Dropbox and git corrupt each other. Dropbox syncs files the
instant they change; git rewrites dozens of small files inside `.git` in bursts.
Dropbox catches them half-written, syncs the broken state, and eventually the
repository stops opening. It is a well-known failure and it is not recoverable
from Dropbox's version history in any pleasant way.

Two ways out. Pick one.

**Move it (simplest, recommended).** GitHub becomes your backup and your
history, which is a strictly better backup than Dropbox for this:

```sh
mkdir -p ~/Projects
mv ~/Library/CloudStorage/Dropbox/Games/BattleTech/Projects/highexplosive ~/Projects/
cd ~/Projects/highexplosive
```

**Or keep it in Dropbox and hide `.git` from it.** Dropbox honours an
extended attribute that tells it to leave a folder alone:

```sh
cd "$HOME/Library/CloudStorage/Dropbox/Games/BattleTech/Projects/highexplosive"
git init                                   # creates .git — do this first
xattr -w com.dropbox.ignored 1 .git
```

The rest of this guide assumes you are in the site folder, wherever it ended up.

---

## 1. Check the tools you need

```sh
git --version
python3 --version
```

If git is missing, macOS offers to install the Command Line Tools when you run
it — accept. Both are already on any recent macOS.

Install the one Python package the build needs:

```sh
python3 -m pip install --user markdown PyYAML
```

## 2. See it working locally first

Before involving GitHub at all, confirm the site builds on your machine:

```sh
python3 scripts/build.py --serve
```

Open <http://localhost:8080>. Sigil, one link, and the comparator behind it.
Ctrl-C to stop.

If that works, everything else is plumbing.

## 3. Make it a git repository

```sh
git init -b main
git add .
git commit -m "Initial site"
```

`.gitignore` already keeps out `_site/`, any `Sources/` folder, all PDFs, and
the usual macOS clutter. Check that nothing you want private slipped in:

```sh
git ls-files | grep -i -E 'source|\.pdf' || echo "clean"
```

## 4. Create the GitHub repository and push

**With the GitHub CLI** — it handles login properly, which is the part that
usually goes wrong:

```sh
brew install gh          # skip if you already have it
gh auth login            # choose GitHub.com, HTTPS, login with a browser
gh repo create highexplosive --public --source=. --remote=origin --push
```

**Without the CLI:** create the repository at
<https://github.com/new> — name it `highexplosive`, set it **Public**, and add
no README, no .gitignore, no licence. Then:

```sh
git remote add origin https://github.com/comstar3025/highexplosive.git
git push -u origin main
```

If it asks for a password, that is not your GitHub password — GitHub stopped
accepting those. Either use `gh auth login` above, or install
[GitHub Desktop](https://desktop.github.com/), which handles it for you.

## 5. Turn on Pages

On GitHub: **your repository → Settings → Pages**.

Under **Build and deployment → Source**, choose **GitHub Actions**. Not
"Deploy from a branch" — the workflow in `.github/workflows/deploy.yml`
handles the build.

That is the only setting. Go to the **Actions** tab and watch the run. It takes
under a minute. Green tick means the site is live at
`https://comstar3025.github.io/highexplosive/` — visit it and confirm.

> The logo and links will look broken on that temporary address — the site is
> built for the root of a domain, not a subfolder. It fixes itself the moment
> the custom domain is attached. Don't chase it.

If the run fails, click into it — the failing step's log says why. The most
likely cause is a typo in a `_section.md`.

## 6. Attach the domain on GitHub

**Settings → Pages → Custom domain**. Enter:

```
www.highexplosive.net
```

Save. GitHub will report a DNS check failure — correct, you haven't done the
DNS yet. Leave it and continue.

## 7. Point the domain at GitHub, at Gandi

Log in at <https://admin.gandi.net>, open **highexplosive.net**, then the
**DNS Records** tab.

### First, delete what Gandi put there

Gandi ships a default zone that will fight you. Delete these if present:

- the `A` record on `@` (points at a Gandi parking page)
- the `AAAA` record on `@`
- the `CNAME` on `www` (points at `webredir.vip.gandi.net`)

Leave `MX` records alone if you use email on this domain. Leave the `NS` and
`SOA` records alone regardless.

### Then add these nine records

Gandi's DNS Records tab has an **"Edit the zone file"** / text mode. That is far
faster than the form. Paste:

```zone
@     10800  IN  A      185.199.108.153
@     10800  IN  A      185.199.109.153
@     10800  IN  A      185.199.110.153
@     10800  IN  A      185.199.111.153
@     10800  IN  AAAA   2606:50c0:8000::153
@     10800  IN  AAAA   2606:50c0:8001::153
@     10800  IN  AAAA   2606:50c0:8002::153
@     10800  IN  AAAA   2606:50c0:8003::153
www   10800  IN  CNAME  comstar3025.github.io.
```

Using the form instead? Same thing, one row at a time:

| Type  | Name  | Value                    |
|-------|-------|--------------------------|
| A     | `@`   | `185.199.108.153`        |
| A     | `@`   | `185.199.109.153`        |
| A     | `@`   | `185.199.110.153`        |
| A     | `@`   | `185.199.111.153`        |
| AAAA  | `@`   | `2606:50c0:8000::153`    |
| AAAA  | `@`   | `2606:50c0:8001::153`    |
| AAAA  | `@`   | `2606:50c0:8002::153`    |
| AAAA  | `@`   | `2606:50c0:8003::153`    |
| CNAME | `www` | `comstar3025.github.io.` |

Two details that cause most of the failures here:

- The trailing dot on `comstar3025.github.io.` matters. Without it some panels
  append the domain and you end up pointing at
  `comstar3025.github.io.highexplosive.net`.
- The CNAME target has **no repository name** in it. `comstar3025.github.io`,
  not `comstar3025.github.io/highexplosive`.

The four A records are not alternatives — add all four. Same for the AAAA
records. They are what makes the bare `highexplosive.net` redirect to `www`.

## 8. Wait, then turn on HTTPS

DNS changes take anywhere from a few minutes to a few hours. Check progress:

```sh
dig +short www.highexplosive.net
dig +short highexplosive.net
```

You want `comstar3025.github.io` from the first and the four `185.199.*`
addresses from the second.

Once that resolves, go back to **Settings → Pages**. The red DNS warning should
be gone. Then tick **Enforce HTTPS**. If the box is greyed out, GitHub is still
issuing the certificate — it can take up to 24 hours, though it is usually
under an hour. Nothing to do but wait.

Done. `https://www.highexplosive.net` is your site, and `highexplosive.net`
redirects to it.

---

## Day to day

```sh
git add . && git commit -m "..." && git push
```

The push triggers the build. Live about 40 seconds later.

**Another link on the front page** — add a line to `content/index.md`:

```yaml
links:
  - title: Weapon Package Comparator
    url: /tools/comparator/
  - title: Something Else
    url: /whatever/
```

**A different theme** — `theme: light` or `theme: dark` in `site.yaml`.

**A new comparator version:**

```sh
cp "path/to/Weapon Comparator/comparator.html" static/tools/comparator/index.html
```

**Full pages, when you want them.** The section machinery is built and parked
in `content/_later/` — folders prefixed with `_` are skipped by the build. Move
one back up to `content/` and it comes alive, with its own index page and
navigation. `content/_later/house-rules/EXAMPLE-copy-me.md` documents every
front matter option.

---

## When something is wrong

**The Action failed.** Actions tab → click the red run → click the failed step.
The error names the file. Usually a front matter typo: a missing `---`, or a
value containing a colon that needs quoting.

**A page didn't appear.** It is probably still `draft: true`. Build with
`python3 scripts/build.py --drafts --serve` to see drafts locally.

**The site is live but stale.** Check the Actions tab actually ran. Then
hard-reload — Cmd-Shift-R.

**The domain shows a GitHub 404.** The custom domain in Settings → Pages got
cleared, which GitHub sometimes does when a DNS check fails. Re-enter it.

**Everything looks unstyled.** The CSS 404'd. Almost always the custom domain
is not attached yet and you are on the `github.io/highexplosive/` address —
see the note in step 5.
