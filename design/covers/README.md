# Cover sources

Editable HTML sources for the site's post covers. These files are excluded
from the Jekyll build (`design` in `_config.yml`); only the rendered PNGs in
`assets/images/` are published.

## Render a cover

```bash
chromium --headless=new --no-sandbox --disable-gpu --disable-dev-shm-usage \
  --hide-scrollbars --force-device-scale-factor=1 --window-size=1200,630 \
  --screenshot=assets/images/playing-with-ai-pentest-tools-cover.png \
  file://"$PWD"/design/covers/playing-with-ai-pentest-tools-cover.html
```

The output path must match the post's `cover:` and `image:` front matter.
Covers are 1200×630 and use the dark palette tokens from
`assets/css/style.css`: background `#0e1216`, body text `#e6edf3`, muted
`#93a1ae`, accent `#79c0ff`.

## Existing covers

| Source | Rendered to |
|---|---|
| `playing-with-ai-pentest-tools-cover.html` | `assets/images/playing-with-ai-pentest-tools-cover.png` |

The two earlier covers (`skilltriage-cover.png`, `semgrep-cover.png`) were
produced before this directory existed and have no source here.
