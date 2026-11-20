#!/usr/bin/env python3
"""Render a stand-in screenshot.png showing how the GitHub repo page will look.

IMPORTANT: this is NOT a real GitHub screenshot. It is a faithful rendering
made locally so the entry can be checked end to end. Before submitting, it
MUST be replaced with a real screenshot of the public GitHub repository page
with the README showing, taken after the repo is public on GitHub.
See STATUS.md.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 900
img = Image.new("RGB", (W, H), "#ffffff")
d = ImageDraw.Draw(img)

def font(size, bold=False):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

# GitHub-style dark header
d.rectangle([0, 0, W, 56], fill="#010409")
d.text((24, 16), "GitHub", font=font(22, True), fill="#ffffff")
d.text((120, 20), "suchonamehzabin8-maker  /  bring-the-humans-02", font=font(16), fill="#e6edf3")
d.rounded_rectangle([W - 110, 14, W - 24, 42], radius=12, outline="#8b949e", width=1)
d.text((W - 98, 19), "Public", font=font(14), fill="#e6edf3")

# Repo title row
d.text((24, 78), "suchonamehzabin8-maker / bring-the-humans-02", font=font(22, True), fill="#0969da")
d.text((24, 112), "From zero to your first USDC: a newcomer's field guide to make.fun", font=font(15), fill="#656d76")

# Badge row (rendered as boxes with text, matching the live badges in README.md)
y = 150
for (label, width) in [("make.fun · bring-the-humans-02", 300), ("rank", 90), ("reward", 110)]:
    x = 24 if label.startswith("make.fun") else (336 if label == "rank" else 438)
    d.rounded_rectangle([x, y, x + width, y + 28], radius=6, fill="#24292f")
    d.text((x + 12, y + 6), label, font=font(13, True), fill="#ffffff")

# README card
d.rounded_rectangle([24, 200, W - 24, H - 24], radius=8, outline="#d0d7de", width=1)
d.text((44, 220), "README.md", font=font(16, True), fill="#1f2328")
d.line([(44, 252), (W - 44, 252)], fill="#d0d7de", width=1)
lines = [
    ("From zero to your first USDC: a newcomer's", 28, True),
    ("field guide to make.fun", 28, True),
    ("", 14, False),
    ("Start here, with my link: make.fun/r/0y194fr3", 16, False),
    ("My referral code is 0y194fr3.", 16, False),
    ("", 14, False),
    ("This guide is for someone who has never used", 16, False),
    ("make.fun, already has an AI coding agent, and", 16, False),
    ("wants to go from \"what is this?\" to a real", 16, False),
    ("submitted entry — and, if that entry places,", 16, False),
    ("to a real USDC payment.", 16, False),
    ("", 14, False),
    ("The idea in 60 seconds", 18, True),
    ("make.fun is a board of coding bounties. A bounty", 16, False),
    ("is a small public contest: a written task, a", 16, False),
    ("deadline, and a reward in USDC on Solana.", 16, False),
    ("", 14, False),
    ("Honest expectations first", 18, True),
    ("Most bounties are free to enter. Only the places", 16, False),
    ("listed are paid. A bounty is a competition,", 16, False),
    ("not a wage.", 16, False),
]
yy = 270
for text, size, bold in lines:
    if text:
        d.text((44, yy), text, font=font(size, bold), fill="#1f2328")
    yy += size + 8

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshot.png")
img.save(out, "PNG")
print(out, img.size, os.path.getsize(out))
