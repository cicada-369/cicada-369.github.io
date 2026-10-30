# cicada-369.github.io

Personal blog: **https://cicada-369.github.io**

Built with Jekyll and served by GitHub Pages. No build workflow is needed —
GitHub Pages builds the `main` branch directly.

## Writing a post

Create a file in `_posts/` named `YYYY-MM-DD-slug.md`:

```yaml
---
title: "Post title"
description: "One sentence used on cards, in search results, and in the feed."
date: 2026-10-30
tags:
  - security
  - ai
cover: /assets/images/example-cover.png
image: /assets/images/example-cover.png
---
```

The permalink is `/blog/<slug>/`. Put images in `assets/images/` and reference
them as `/assets/images/name.png`.

## Local preview

With Docker (no Ruby install needed):

```bash
docker run --rm -it \
  -v "$PWD:/srv/jekyll" \
  -p 4000:4000 \
  jekyll/jekyll:pages \
  jekyll serve --host 0.0.0.0
```

Then open <http://localhost:4000>.

With Ruby installed:

```bash
bundle install
bundle exec jekyll serve
```

## Publishing

```bash
git add -A
git commit -m "Post: ..."
git push
```

GitHub Pages rebuilds automatically in about a minute. Check the build at
`https://github.com/cicada-369/cicada-369.github.io/actions` or the Pages
settings.

## Layout

| Path | Purpose |
|---|---|
| `_posts/` | Blog posts |
| `_layouts/` | Page templates |
| `_includes/` | Header, footer, cards, SEO head |
| `assets/css/style.css` | The whole design system, light and dark |
| `blog/`, `about/` | Section index pages |

Projects are intentionally not part of the site yet. When you want them, add a
`projects/index.html`, a `_data/projects.yml`, and a `_includes/project-card.html`
— the stylesheet already has the card layout. The Atlas page and project drafts
remain in `/home/ra/projects/blog/`, unpublished.
