"""Render the front page of THE WORLD TODAY for Friday 20 November 2026.

Pure Pillow drawing. No network, no randomness, no clock: the same input
always produces the same bytes. All copy lives in STORIES below so the
text can be checked against NEWS.md.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

PAPER = (247, 243, 234, 255)
INK = (24, 24, 22, 255)
MUTED = (90, 86, 78, 255)
RULE = (24, 24, 22, 255)
ACCENT = (158, 32, 26, 255)
NAVY = (18, 38, 66, 255)
CARD_BG = (255, 255, 255, 255)
CARD_EDGE = (198, 192, 180, 255)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)  # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit within width."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            trial = cur + " " + word
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill=INK):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)


def hline(draw, x0, x1, y, width=1, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


LEAD_HEADLINE = "Trump, Xi and Putin issue joint \u2018peace declaration\u2019"
LEAD_DECK = (
    "After 90 minutes of first-ever three-way talks in Shenzhen, the leaders "
    "of the United States, China and Russia say a nuclear war \u201ccannot be won "
    "and must never be fought\u201d \u2014 but the declaration says nothing about "
    "Ukraine or Iran."
)
LEAD_FACTS = "Four-point text  \u2022  Dialogue on nuclear risks  \u2022  More oil supply  \u2022  UN reform  \u2022  No timelines"

CARDS = [
    (
        "JUSTICE",
        "World court: Myanmar committed genocide",
        "The ICJ rules 9\u20136 that Myanmar committed genocide against the "
        "Rohingya in 2017 \u2014 the first time the court has found a state "
        "guilty of genocide \u2014 and orders return and reparations.",
    ),
    (
        "IRAN",
        "Trump puts Iran decision off to next year",
        "\u201cWe\u2019ll see what happens after January 1,\u201d the US president "
        "says of renewed strikes on Iran, telling Reuters and Fox News he is "
        "\u201cnot rushing into any decision.\u201d",
    ),
    (
        "MARKETS",
        "Anthropic\u2019s record debut jumps 17%",
        "The AI firm behind Claude closes its first Nasdaq day at $97.17, up "
        "17% on its $83 IPO price, after raising a record $81.3bn.",
    ),
    (
        "WEATHER",
        "Cyclone Akvan nears Odisha; 300,000 moved",
        "The storm is due to make landfall near Gopalpur on Friday with winds "
        "of 90\u2013100 km/h, as Odisha evacuates about 300,000 people to shelters.",
    ),
    (
        "RIYADH",
        "Houthi strike hits Riyadh\u2019s tallest tower",
        "A Houthi attack damages several floors of the PIF Tower, HQ of Saudi "
        "Arabia\u2019s wealth fund, Saudi civil defence says. No injuries reported.",
    ),
    (
        "CULTURE",
        "GTA VI takes an estimated $1.84bn on day one",
        "Sensor Tower estimates 19m copies sold by launch day \u2014 passing the "
        "entire $1.805bn box-office run of Nolan\u2019s \u201cThe Odyssey\u201d.",
    ),
]

ALSO = [
    "COP31 enters its closing day in Antalya with no deal yet; a slimmed draft drops fossil-fuel language and the $120bn adaptation figure.",
    "NASA confirms Voyager 1 is one light-day from Earth \u2014 the first human-made object to get that far.",
    "Russia strikes Kyiv with ballistic missiles overnight; fires reported across several districts.",
    "Drones halt Genoa airport flights for about two hours.",
    "JAXA drops Hayabusa2\u2019s 2031 asteroid landing after engine trouble; new target is a 2028 flyby.",
]

FOOTER = (
    "Sources: Reuters, AP, BBC, NASA, JAXA, IMD, Sensor Tower via Forbes. "
    "Stories first reported 19\u201320 November 2026."
)


def draw_globe(draw, cx, cy, r):
    """Simple line globe: circle with meridians and parallels."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=NAVY, width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=NAVY, width=2)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 180, fill=NAVY, width=2)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 180, 360, fill=NAVY, width=2)


def render(path):
    img = Image.new("RGB", (W, H), PAPER[:3])
    d = ImageDraw.Draw(img)
    mx = 36  # side margin
    right = W - mx

    # ---- Masthead -------------------------------------------------------
    draw_centered(d, W // 2, 22, "THE WORLD TODAY", SERIF_B(60))
    hline(d, mx, right, 100, width=3)
    hline(d, mx, right, 106, width=1)
    draw_centered(d, W // 2, 116, "FRIDAY 20 NOVEMBER 2026", SANS_B(27), fill=ACCENT)
    draw_centered(
        d, W // 2, 152, "The day\u2019s world news \u2014 in one page",
        SANS(16), fill=MUTED,
    )
    hline(d, mx, right, 182, width=2)

    # ---- Lead story -----------------------------------------------------
    y = 196
    d.text((mx, y), "LEAD  \u2014  SHENZHEN SUMMIT", font=SANS_B(16), fill=ACCENT)
    y += 26
    head_lines = wrap(d, LEAD_HEADLINE, SERIF_B(37), right - mx - 150)
    for line in head_lines:
        d.text((mx, y), line, font=SERIF_B(37), fill=INK)
        y += 46
    # Globe at the right of the headline block.
    draw_globe(d, right - 62, 196 + 26 + 46, 52)
    y += 4
    for line in wrap(d, LEAD_DECK, SANS(19), right - mx):
        d.text((mx, y), line, font=SANS(19), fill=INK)
        y += 26
    y += 6
    d.text((mx, y), LEAD_FACTS, font=SANS_B(14), fill=MUTED)
    y += 30
    hline(d, mx, right, y, width=2)

    # ---- Story cards: 2 rows x 3 columns -------------------------------
    gap = 14
    cw = (right - mx - 2 * gap) // 3
    ch = 196
    top = y + 14
    for i, (kicker, head, body) in enumerate(CARDS):
        row, col = divmod(i, 3)
        x0 = mx + col * (cw + gap)
        y0 = top + row * (ch + gap)
        d.rectangle([x0, y0, x0 + cw, y0 + ch], fill=CARD_BG, outline=CARD_EDGE, width=1)
        d.rectangle([x0, y0, x0 + cw, y0 + 4], fill=ACCENT)
        tx = x0 + 12
        ty = y0 + 14
        d.text((tx, ty), kicker, font=SANS_B(13), fill=ACCENT)
        ty += 22
        for line in wrap(d, head, SANS_B(19), cw - 24):
            d.text((tx, ty), line, font=SANS_B(19), fill=INK)
            ty += 24
        ty += 4
        for line in wrap(d, body, SANS(14), cw - 24):
            d.text((tx, ty), line, font=SANS(14), fill=INK)
            ty += 19

    # ---- "Also today" strip ---------------------------------------------
    sy = top + 2 * ch + gap + 14
    sh = 118
    d.rectangle([mx, sy, right, sy + sh], fill=NAVY)
    d.text((mx + 14, sy + 10), "ALSO TODAY", font=SANS_B(15), fill=(255, 214, 90, 255))
    ay = sy + 34
    col_w = (right - mx - 28 - 4 * 18) // 5
    for i, item in enumerate(ALSO):
        x0 = mx + 14 + i * (col_w + 18)
        for line in wrap(d, item, SANS(12), col_w):
            d.text((x0, ay), line, font=SANS(12), fill=(255, 255, 255, 255))
            ay += 16
        ay = sy + 34
        if i < 4:
            d.line(
                [(x0 + col_w + 9, sy + 36), (x0 + col_w + 9, sy + sh - 10)],
                fill=(120, 140, 170, 255), width=1,
            )

    # ---- Footer -----------------------------------------------------------
    fy = sy + sh + 12
    draw_centered(d, W // 2, fy, FOOTER, SANS(12), fill=MUTED)

    img.save(path, format="PNG", optimize=True)
    return path


if __name__ == "__main__":
    import sys

    render(sys.argv[1] if len(sys.argv) > 1 else "entry.png")
