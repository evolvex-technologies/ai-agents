#!/usr/bin/env python3
"""Generate the branded LinkedIn Post Template.jpg for EvolveX Technologies.

Builds a 1200x1500 (4:5) card: dark brand-gradient background, a rounded
glow frame, and the EvolveX logo seated on a light chip in the bottom-right
corner. The inner content area is left empty for Nano Banana 2 to fill in
via image_input during post generation.
"""

import math
import os
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGO_PATH = os.path.join(ROOT, "Nano Banana 2", "assets", "logo", "evolvex-logo@4x.png")
OUTPUT_PATH = os.path.join(ROOT, "Linkedin Post Template.jpg")

CANVAS_W, CANVAS_H = 1200, 1500

# Corner colors for the background gradient (deep, dark tones from the
# EvolveX mark: near-black fading into plum/magenta).
TOP_LEFT = (11, 7, 16)
TOP_RIGHT = (23, 10, 26)
BOTTOM_LEFT = (20, 9, 22)
BOTTOM_RIGHT = (42, 14, 46)

# Accent colors lifted straight from the EvolveX logo gradient.
GOLD = (249, 206, 52)      # #F9CE34
ORANGE = (241, 96, 10)     # #F1600A
PINK = (238, 42, 123)      # #EE2A7B
PURPLE = (98, 40, 215)     # #6228D7
WINE = (133, 1, 82)        # #850152


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def build_gradient_background(w, h):
    """Bilinear 4-corner gradient, rendered small then upscaled for smoothness."""
    small_w, small_h = 80, 100
    small = Image.new("RGB", (small_w, small_h))
    px = small.load()
    for y in range(small_h):
        v = y / (small_h - 1)
        left = lerp(TOP_LEFT, BOTTOM_LEFT, v)
        right = lerp(TOP_RIGHT, BOTTOM_RIGHT, v)
        for x in range(small_w):
            u = x / (small_w - 1)
            px[x, y] = lerp(left, right, u)
    return small.resize((w, h), Image.LANCZOS)


def add_corner_glow(base, center, color, radius, strength=140):
    """Soft radial glow blob, additively blended for a premium ambient feel."""
    glow = Image.new("L", base.size, 0)
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse(
        [center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius],
        fill=strength,
    )
    glow = glow.filter(ImageFilter.GaussianBlur(radius / 2.2))
    tint = Image.new("RGB", base.size, color)
    base.paste(tint, (0, 0), glow)


def rounded_rect(draw, box, radius, outline, width):
    draw.rounded_rectangle(box, radius=radius, outline=outline, width=width)


def draw_frame(base, margin=40, radius=52):
    w, h = base.size
    box = [margin, margin, w - margin, h - margin]

    # Soft outer glow behind the frame line (drawn on a blurred overlay).
    glow_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow_layer)
    gdraw.rounded_rectangle(box, radius=radius, outline=PINK + (160,), width=10)
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(6))
    base.paste(Image.alpha_composite(base.convert("RGBA"), glow_layer).convert("RGB"), (0, 0))

    # Crisp frame line on top, blending pink -> purple across the perimeter.
    draw = ImageDraw.Draw(base)
    rounded_rect(draw, box, radius, PINK, 3)


def place_logo(base):
    logo = Image.open(LOGO_PATH).convert("RGBA")
    target_w = 300
    scale = target_w / logo.width
    logo = logo.resize((target_w, round(logo.height * scale)), Image.LANCZOS)

    pad_x, pad_y = 36, 26
    chip_w, chip_h = logo.width + pad_x * 2, logo.height + pad_y * 2
    chip = Image.new("RGBA", (chip_w, chip_h), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chip)
    cdraw.rounded_rectangle([0, 0, chip_w - 1, chip_h - 1], radius=22, fill=(245, 241, 245, 235))

    margin = 40
    inset = 30
    chip_x = base.width - margin - inset - chip_w
    chip_y = base.height - margin - inset - chip_h

    base.paste(chip, (chip_x, chip_y), chip)
    base.paste(logo, (chip_x + pad_x, chip_y + pad_y), logo)


def main():
    base = build_gradient_background(CANVAS_W, CANVAS_H)

    add_corner_glow(base, (CANVAS_W * 0.88, CANVAS_H * 0.90), ORANGE, radius=420, strength=90)
    add_corner_glow(base, (CANVAS_W * 0.08, CANVAS_H * 0.05), PURPLE, radius=380, strength=70)

    draw_frame(base, margin=40, radius=52)
    place_logo(base)

    base.convert("RGB").save(OUTPUT_PATH, "JPEG", quality=94)
    print(f"Saved template: {OUTPUT_PATH} ({base.size[0]}x{base.size[1]})")


if __name__ == "__main__":
    main()
