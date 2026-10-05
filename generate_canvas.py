import math
import os
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONTS_DIR = r"C:\Users\USER\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\8b63dbb4-2d55-4c47-a364-211601f4610b\108fe625-bf80-4b47-9e51-792bac831982\skills\canvas-design\canvas-fonts"
OUTPUT = r"C:\Users\USER\Storyforge\portfolio\meridian-noir.pdf"

W, H = 800, 1100

font_map = {
    "IBMPlexSerif-Bold": "IBMPlexSerif-Bold.ttf",
    "IBMPlexSerif-Regular": "IBMPlexSerif-Regular.ttf",
    "IBMPlexSerif-Italic": "IBMPlexSerif-Italic.ttf",
    "IBMPlexMono-Regular": "IBMPlexMono-Regular.ttf",
    "GeistMono-Regular": "GeistMono-Regular.ttf",
    "GeistMono-Bold": "GeistMono-Bold.ttf",
    "InstrumentSans-Regular": "InstrumentSans-Regular.ttf",
    "InstrumentSerif-Italic": "InstrumentSerif-Italic.ttf",
    "DMMono-Regular": "DMMono-Regular.ttf",
    "InstrumentSans-Italic": "InstrumentSans-Italic.ttf",
}

for name, fname in font_map.items():
    path = os.path.join(FONTS_DIR, fname)
    if os.path.exists(path):
        try:
            pdfmetrics.registerFont(TTFont(name, path))
        except Exception as e:
            print(f"Font skip: {name} — {e}")

import random
random.seed(42)

c = pdf_canvas.Canvas(OUTPUT, pagesize=(W, H))

def hex_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))

BG     = hex_rgb("060610")
FG     = hex_rgb("EDEBE6")
ACCENT = hex_rgb("3B6EEF")
DIM    = hex_rgb("1A1A30")

def sf(col, a=1.0):
    c.setFillColorRGB(*col)
    c.setFillAlpha(a)

def ss(col, a=1.0):
    c.setStrokeColorRGB(*col)
    c.setStrokeAlpha(a)

# ── BACKGROUND ───────────────────────────────────────────────────────────────
sf(BG, 1.0)
ss(BG, 1.0)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Subtle inner vignette (lighter center strip) — painted as stacked rect fills
for i in range(12):
    shade = i / 12
    sf(FG, 0.008 * (1 - shade))
    margin = 60 + i * 28
    c.rect(margin, margin, W - 2*margin, H - 2*margin, fill=1, stroke=0)

# Micro star-field: very faint scattered dots suggesting depth / data
for _ in range(180):
    px = random.uniform(0, W)
    py = random.uniform(0, H)
    size = random.choice([0.5, 0.5, 0.5, 1.0, 1.0, 1.5])
    alpha = random.uniform(0.02, 0.07)
    sf(FG, alpha)
    c.circle(px, py, size, fill=1, stroke=0)

# ── STRUCTURAL GRID ──────────────────────────────────────────────────────────
ss(FG, 0.035)
c.setLineWidth(0.25)
step_h = 110
for y in range(0, H + step_h, step_h):
    c.line(0, y, W, y)

for x in [80, W // 2, W - 80]:
    ss(FG, 0.035)
    c.setLineWidth(0.25)
    c.line(x, 0, x, H)

# ── GHOST DISPLAY TEXT: "MERIDIAN" ──────────────────────────────────────────
sf(FG, 0.055)
c.setFont("IBMPlexSerif-Bold", 116)
c.drawString(-8, H - 148, "MERIDIAN")

# ── NAVIGATIONAL CIRCLE SYSTEM ───────────────────────────────────────────────
cx, cy = W / 2, H / 2 - 20
r_outer = 242
r_inner = 158
r_tiny  = 60

# Outermost faint ring
ss(FG, 0.06)
c.setLineWidth(0.4)
c.circle(cx, cy, r_outer + 28, stroke=1, fill=0)

# Main outer circle
ss(FG, 0.22)
c.setLineWidth(1.2)
c.circle(cx, cy, r_outer, stroke=1, fill=0)

# Inner circle
ss(FG, 0.09)
c.setLineWidth(0.5)
c.circle(cx, cy, r_inner, stroke=1, fill=0)

# Tiny inner ring
ss(FG, 0.06)
c.setLineWidth(0.4)
c.circle(cx, cy, r_tiny, stroke=1, fill=0)

# Compass cross (full bleed through circle)
ss(FG, 0.10)
c.setLineWidth(0.4)
c.line(cx, cy - r_outer - 30, cx, cy + r_outer + 30)
c.line(cx - r_outer - 30, cy, cx + r_outer + 30, cy)

# 22.5° tick marks all around
for deg in range(0, 360, 22):
    rad = math.radians(deg)
    is_cardinal = (deg % 90 == 0)
    is_major    = (deg % 45 == 0)
    inner_r = r_outer - (14 if is_cardinal else 8 if is_major else 5)
    outer_r = r_outer + (14 if is_cardinal else 8 if is_major else 5)
    ix = cx + inner_r * math.cos(rad)
    iy = cy + inner_r * math.sin(rad)
    ox = cx + outer_r * math.cos(rad)
    oy = cy + outer_r * math.sin(rad)
    alpha = 0.22 if is_cardinal else 0.14 if is_major else 0.07
    ss(FG, alpha)
    c.setLineWidth(0.5 if is_cardinal else 0.35)
    c.line(ix, iy, ox, oy)

# Cardinal labels
c.setFont("DMMono-Regular", 8)
pad = 26
for label, angle in [("N", 90), ("E", 0), ("S", 270), ("W", 180)]:
    rad = math.radians(angle)
    lx = cx + (r_outer + pad) * math.cos(rad)
    ly = cy + (r_outer + pad) * math.sin(rad) - 3
    sf(FG, 0.35)
    c.drawCentredString(lx, ly, label)

# ── CENTER CROSSHAIR ─────────────────────────────────────────────────────────
ss(FG, 0.30)
c.setLineWidth(0.8)
ch = 22
c.line(cx - ch, cy, cx + ch, cy)
c.line(cx, cy - ch, cx, cy + ch)

sf(FG, 0.55)
c.circle(cx, cy, 2.8, fill=1, stroke=0)

# Small concentric center rings
for r_c, a_c in [(8, 0.12), (16, 0.07)]:
    ss(FG, a_c)
    c.setLineWidth(0.4)
    c.circle(cx, cy, r_c, stroke=1, fill=0)

# ── FEATURE ARC (the "product arc") ─────────────────────────────────────────
# C-shape opening right: from 110° to 250° (CCW in reportlab)
arc_start = 108
arc_extent = 144  # ends at 252°

ss(FG, 0.65)
c.setLineWidth(2.2)
c.arc(cx - r_outer, cy - r_outer,
      cx + r_outer, cy + r_outer,
      startAng=arc_start, extent=arc_extent)

# Endpoints
s_rad = math.radians(arc_start)
sx, sy = cx + r_outer * math.cos(s_rad), cy + r_outer * math.sin(s_rad)

e_rad = math.radians(arc_start + arc_extent)
ex, ey = cx + r_outer * math.cos(e_rad), cy + r_outer * math.sin(e_rad)

# Blue accent dot at arc start (the "north star")
sf(ACCENT, 1.0)
c.circle(sx, sy, 6, fill=1, stroke=0)

# Outer accent ring around north star dot
ss(ACCENT, 0.30)
c.setLineWidth(0.5)
c.circle(sx, sy, 14, stroke=1, fill=0)

# Blue radial spoke from center toward end point
ss(ACCENT, 0.35)
c.setLineWidth(0.9)
spoke_len = 55
lx2 = cx + spoke_len * math.cos(e_rad)
ly2 = cy + spoke_len * math.sin(e_rad)
c.line(cx, cy, lx2, ly2)

# Tangent bearing line from the north-star blue dot — extends to canvas edge
# Tangent at arc_start is perpendicular to the radius at that point
tang_rad = s_rad + math.pi / 2  # 90 degrees CCW from radius = tangent direction
tang_len = 320
tx1 = sx + tang_len * math.cos(tang_rad)
ty1 = sy + tang_len * math.sin(tang_rad)
tx2 = sx - tang_len * math.cos(tang_rad)
ty2 = sy - tang_len * math.sin(tang_rad)
ss(ACCENT, 0.10)
c.setLineWidth(0.6)
c.line(tx1, ty1, tx2, ty2)

# Small square marker at blue dot — precision cross
ss(ACCENT, 0.45)
c.setLineWidth(0.6)
sq = 10
c.line(sx - sq, sy, sx + sq, sy)
c.line(sx, sy - sq, sx, sy + sq)

# ── ARC DEGREE MARKERS ───────────────────────────────────────────────────────
marker_angles = [120, 150, 180, 210, 240]
for i, deg in enumerate(marker_angles):
    rad = math.radians(deg)
    tick_i = cx + (r_outer - 11) * math.cos(rad), cy + (r_outer - 11) * math.sin(rad)
    tick_o = cx + (r_outer + 11) * math.cos(rad), cy + (r_outer + 11) * math.sin(rad)
    lbl_pos = cx + (r_outer + 24) * math.cos(rad), cy + (r_outer + 24) * math.sin(rad)

    ss(FG, 0.22)
    c.setLineWidth(0.5)
    c.line(*tick_i, *tick_o)

    c.setFont("DMMono-Regular", 6)
    sf(FG, 0.32)
    actual_deg = [120, 150, 180, 210, 240][i]
    c.drawCentredString(lbl_pos[0], lbl_pos[1] - 3, f"{actual_deg}")

# ── INNER FLOATING LABELS ────────────────────────────────────────────────────
inner_labels = [
    (cx - 72, cy + 55,  "signal"),
    (cx + 22, cy - 18,  "clarity"),
    (cx - 88, cy - 72,  "depth"),
]
c.setFont("DMMono-Regular", 8)
for lx, ly, text in inner_labels:
    sf(FG, 0.22)
    c.drawString(lx, ly, text)
    tw = c.stringWidth(text, "DMMono-Regular", 8)
    ss(FG, 0.09)
    c.setLineWidth(0.3)
    c.line(lx, ly - 2, lx + tw, ly - 2)

# ── ZONE DIVIDER LINES ───────────────────────────────────────────────────────
# Golden-section horizontals with slight accent
for y_pos, a in [(H - 196, 0.10), (220, 0.07)]:
    ss(FG, a)
    c.setLineWidth(0.4)
    c.line(40, y_pos, W - 40, y_pos)

# ── VERTICAL SIDE TEXT ───────────────────────────────────────────────────────
c.saveState()
c.setFont("InstrumentSans-Regular", 7)
sf(FG, 0.18)
c.translate(16, H / 2)
c.rotate(90)
c.drawCentredString(0, 0, "PORTFOLIO  ·  DESIGN  SYSTEM  ·  2026")
c.restoreState()

# Right-side vertical label
c.saveState()
c.setFont("DMMono-Regular", 7)
sf(FG, 0.15)
c.translate(W - 16, H / 2)
c.rotate(-90)
c.drawCentredString(0, 0, "MERIDIAN  NOIR  ·  REV 01")
c.restoreState()

# ── TOP-RIGHT "NOIR" LABEL ───────────────────────────────────────────────────
c.setFont("GeistMono-Regular", 12)
sf(FG, 0.80)
c.drawRightString(W - 40, H - 54, "NOIR")

noir_w = c.stringWidth("NOIR", "GeistMono-Regular", 12)
ss(FG, 0.18)
c.setLineWidth(0.4)
c.line(W - 40 - noir_w, H - 58, W - 40, H - 58)

# ── DEGREE NOTATION (top-left system coords) ─────────────────────────────────
c.setFont("DMMono-Regular", 7)
sf(FG, 0.25)
c.drawString(40, H - 54, f"dia {int(r_outer * 2)} pt")

ss(FG, 0.12)
c.setLineWidth(0.3)
c.line(40, H - 60, 140, H - 60)

sf(FG, 0.15)
c.setFont("DMMono-Regular", 6)
c.drawString(40, H - 70, f"cx {int(cx)}  cy {int(H - cy)}")

# ── BOTTOM SECTION ────────────────────────────────────────────────────────────
bot = 72
ss(FG, 0.08)
c.setLineWidth(0.4)
c.line(40, bot + 38, W - 40, bot + 38)

# Name — italic serif, warm
c.setFont("InstrumentSerif-Italic", 14)
sf(FG, 0.72)
c.drawString(40, bot + 14, "Muhammad Adi Putra")

# Role — thin sans
c.setFont("InstrumentSans-Regular", 8)
sf(FG, 0.26)
c.drawString(40, bot - 2, "Product Manager")

# Bottom-right: accent color swatch + hex
sf(ACCENT, 1.0)
c.rect(W - 52, bot + 2, 14, 14, fill=1, stroke=0)

c.setFont("DMMono-Regular", 7)
sf(ACCENT, 0.65)
c.drawRightString(W - 60, bot + 7, "#3B6EEF")

# ── FINE DETAIL: small dots at grid intersections (selective) ────────────────
dot_positions = [(80, H - 196), (W//2, H - 196), (W-80, H - 196),
                 (80, 220),      (W//2, 220),      (W-80, 220)]
for dx, dy in dot_positions:
    sf(FG, 0.18)
    c.circle(dx, dy, 2, fill=1, stroke=0)

# ── THIN ACCENT HEADER BAND ──────────────────────────────────────────────────
# A 2pt accent blue line at the very top, spanning full width
sf(ACCENT, 0.55)
c.rect(0, H - 3, W, 3, fill=1, stroke=0)

# Matching micro-line at very bottom
sf(ACCENT, 0.18)
c.rect(0, 0, W, 1.5, fill=1, stroke=0)

# ── FINAL FLOURISH: thin border ──────────────────────────────────────────────
ss(FG, 0.06)
c.setLineWidth(0.5)
c.rect(24, 24, W - 48, H - 48, stroke=1, fill=0)

ss(FG, 0.03)
c.setLineWidth(0.3)
c.rect(30, 30, W - 60, H - 60, stroke=1, fill=0)

c.save()
print(f"OK  Saved -> {OUTPUT}")
