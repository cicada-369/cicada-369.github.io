import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import potrace

SRC = sys.argv[1]
REPO = sys.argv[2]

TILE = "#0e1216"
TEAL = "#5eead4"
WHITE = "#e6edf3"
FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def curve_d(c):
    p = c.start_point
    d = f"M{p.x:.2f},{p.y:.2f}"
    for seg in c.segments:
        if seg.is_corner:
            d += f"L{seg.c.x:.2f},{seg.c.y:.2f}L{seg.end_point.x:.2f},{seg.end_point.y:.2f}"
        else:
            d += f"C{seg.c1.x:.2f},{seg.c1.y:.2f} {seg.c2.x:.2f},{seg.c2.y:.2f} {seg.end_point.x:.2f},{seg.end_point.y:.2f}"
    return d + "Z"


# --- trace the cicada drawing ---
img = Image.open(SRC).convert("RGBA")
bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
bg.alpha_composite(img)
gray = np.array(bg.convert("L"))
data = gray >= 160  # potracer treats False as foreground
path = potrace.Bitmap(data).trace(turdsize=10, alphamax=1.0, opticurve=True, opttolerance=0.2)
curves = list(path)

all_d = " ".join(curve_d(c) for c in curves)
xs, ys = [], []
for c in curves:
    for p in c.decomposition_points:
        xs.append(p.x); ys.append(p.y)
x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
W, pad = 512, 36
s = min((W - 2 * pad) / (x1 - x0), (W - 2 * pad) / (y1 - y0))
tx = (W - (x1 - x0) * s) / 2 - x0 * s
ty = (W - (y1 - y0) * s) / 2 - y0 * s
transform = f"translate({tx:.2f},{ty:.2f}) scale({s:.4f})"

# --- outline "369" at the same position and size as the approved text ---
canvas = Image.new("L", (512, 512), 255)
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype(FONT_PATH, 62)
spacing = -1.0
widths = [draw.textlength(ch, font=font) for ch in "369"]
total = sum(widths) + spacing * 2
x = 256 - total / 2
for ch, w in zip("369", widths):
    draw.text((x, 318), ch, font=font, fill=0, anchor="ls")
    x += w + spacing

digits_data = np.array(canvas) >= 128
digits_path = potrace.Bitmap(digits_data).trace(turdsize=2, alphamax=1.0, opticurve=True, opttolerance=0.2)
digits_d = " ".join(curve_d(c) for c in digits_path)

mark = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512" '
    f'role="img" aria-label="Cicada 369">\n'
    f'  <rect width="512" height="512" rx="112" fill="{TILE}"/>\n'
    f'  <g transform="{transform}"><path d="{all_d}" fill="{TEAL}" fill-rule="evenodd"/></g>\n'
    f'  <path d="{digits_d}" fill="{WHITE}" fill-rule="evenodd"/>\n'
    f'</svg>\n'
)

glyph = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">\n'
    f'  <g transform="{transform}"><path d="{all_d}" fill="#000000" fill-rule="evenodd"/></g>\n'
    f'</svg>\n'
)

os.makedirs(os.path.join(REPO, "design/logos"), exist_ok=True)
os.makedirs(os.path.join(REPO, "assets"), exist_ok=True)
open(os.path.join(REPO, "design/logos/cicada-lineart.svg"), "w").write(mark)
open(os.path.join(REPO, "assets/favicon.svg"), "w").write(mark)
open(os.path.join(REPO, "assets/cicada-mark.svg"), "w").write(glyph)
print("wrote design/logos/cicada-lineart.svg, assets/favicon.svg, assets/cicada-mark.svg")
print("digits path length:", len(digits_d))
