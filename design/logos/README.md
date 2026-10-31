# Logos

The cicada mark, traced from `source/cicada-drawing.png` (the line drawing
supplied for the logo). One drawing, rendered at three levels of detail.

## Canonical files

| File | Use |
|---|---|
| `cicada-lineart.svg` | Full mark: teal line art + white `369` on a dark tile. Source for the favicon and avatar. |
| `cicada-avatar.svg` | Same mark with a full-bleed background. |
| `cicada-avatar.png` | 460×460 export for the GitHub profile avatar. |
| `../../assets/favicon.svg` | Copy of `cicada-lineart.svg`, served as the site favicon. |
| `../../assets/cicada-mark.svg` | Line art only, no tile and no numerals. Used as a CSS mask for the site header. |

## Size behaviour

- **64px and up:** the line work and `369` both read.
- **32px:** the cicada outline reads as a sketch; `369` is no longer legible.
- **16–32px (favicon):** a delicate sketch; the shape carries it.
- **Header (26px):** the numerals are omitted and the glyph is a `currentColor`
  mask, so it follows the light/dark accent.

This is inherent to the chosen line-art style. The thicker cuts in `traced/`
(`thick-13.svg`, `thick-21.svg`, `thick-31.svg`) remain available if a
small-size variant is ever wanted.

## Regenerating

The mark is traced from the source drawing with
[potracer](https://pypi.org/project/potracer/). From the repository root:

```bash
python3 -m venv /tmp/logotrace-venv
/tmp/logotrace-venv/bin/pip install potracer
/tmp/logotrace-venv/bin/python design/logos/tools/finalize.py \
  design/logos/source/cicada-drawing.png "$PWD"
```

`finalize.py` writes `design/logos/cicada-lineart.svg`, `assets/favicon.svg`,
and `assets/cicada-mark.svg`. The numerals are outlined paths, so the mark has
no font dependency. Render the avatar from `avatar.html` at 460×460.

## Working files

- `traced/` — the trace comparisons, stroke-weight tests, and size tests.
- `options/` — the first silhouette concepts, kept for reference. Superseded.
- `source/` — the original drawing.
