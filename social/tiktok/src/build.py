"""Builds the TikTok photo-mode slideshows (1080x1920) for the shirts and golf posters.

Usage: python3 social/tiktok/src/build.py && node social/tiktok/src/render.js
Each post becomes src/<name>.html; render.js writes <name>/slide-N.png.
Slide copy lives in POSTS below. Keep claims factual (see CLAUDE.md house rules).
"""
from pathlib import Path
import html

SRC = Path(__file__).parent

THEMES = {
    # Matches the existing "Big brother era: unlocked" graphic.
    "shirt": dict(bg="#FBDBB4", ink="#1E1A17", accent="#E0A526", font="'Itim', cursive", icon="img/star.png"),
    # Matches the existing "Gift for the golfer who has everything" graphic.
    "golf": dict(bg="#FEE4C1", ink="#151515", accent="#3F7D3A", font="'Poppins', sans-serif", icon="img/flag.png"),
}

# Each slide: (big text, small text, show_icon). The last slide is the call to action.
POSTS = {
    "golf-has-everything": ("golf", [
        ("Buying for the golfer who has everything? 😩", "", False),
        ("Clubs ✔️\nRangefinder ✔️\n400 golf balls ✔️", "", False),
        ("The one thing he doesn't have…", "", False),
        ("His favorite course on the wall.", "Realistic golf course posters\nfree shipping · link in bio", True),
    ]),
    "golf-gifts-ranked": ("golf", [
        ("Golf gifts, ranked by how much he'll actually use them ⛳", "", False),
        ("5. Novelty golf socks", "worn once", False),
        ("4. Another sleeve of balls", "lost by spring", False),
        ("3. A swing gadget", "lives in the garage", False),
        ("2. A tee time together", "10/10, do this too", False),
        ("1. A print of the course he loves", "he sees it every single day\nfree shipping · link in bio", True),
    ]),
    "golf-dad-translated": ("golf", [
        ("What dad says vs. what he means 🎁", "", False),
        ("\"I don't need anything.\"", "= get him golf stuff", False),
        ("\"Just get me socks.\"", "= please do not get him socks", False),
        ("\"I'll play when it warms up.\"", "= he's counting the days", False),
        ("So give him the course for the wall.", "Realistic golf course posters\nfree shipping · link in bio", True),
    ]),
    "bigbro-announcement-ideas": ("shirt", [
        ("Christmas pregnancy announcement ideas that make grandma cry 🎄", "", False),
        ("1. A baby's-first-Christmas ornament with the due date", "", False),
        ("2. One extra stocking on the mantel, no name yet", "", False),
        ("3. Santa's letter says: \"one more nice kid next year\"", "", False),
        ("4. The big sibling opens their shirt last", "Big Brother & Big Sister shirts\nlink in bio", True),
    ]),
    "bigbro-job-posting": ("shirt", [
        ("🚨 NOW HIRING:\nBig Brother", "", False),
        ("Start date:\nthe baby's due date", "Experience: none required", False),
        ("Duties:", "sharing (ugh)\ngentle hugs\nteaching baby everything you know", False),
        ("Benefits:", "a lifelong best friend\nuniform provided", False),
        ("Uniform available ⭐", "Big Brother & Big Sister shirts\nlink in bio", True),
    ]),
    "bigbro-filming-tips": ("shirt", [
        ("How to film the big sibling reveal on Christmas morning 🎥", "", False),
        ("Hide the shirt in the LAST present", "save the best for last", False),
        ("Ask them to read the shirt out loud", "that's the moment", False),
        ("Keep filming after", "the grandparents' reaction is the best part", False),
        ("Ready for the big reveal?", "Big Brother & Big Sister shirts\nlink in bio", True),
    ]),
}

PAGE = """<!doctype html>
<html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Itim&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
<style>
  html,body {{ margin:0; background:#999; }}
  .slide {{ position:relative; width:1080px; height:1920px; background:{bg}; color:{ink}; font-family:{font};
    box-sizing:border-box; padding:0 100px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; overflow:hidden; }}
  .slide + .slide {{ margin-top:20px; }}
  .big {{ font-size:104px; line-height:1.12; font-weight:800; white-space:pre-line; letter-spacing:-1px; }}
  .big.long {{ font-size:86px; }}
  .small {{ font-size:56px; line-height:1.35; margin-top:48px; white-space:pre-line; color:{ink}; opacity:.8; font-weight:600; }}
  .cta .small {{ background:{accent}; color:#fff; opacity:1; border-radius:40px; padding:30px 50px; font-size:50px; }}
  .icon {{ width:520px; margin-top:70px; -webkit-mask-image: radial-gradient(ellipse at center, #000 58%, transparent 72%); }}
  .count {{ position:absolute; top:230px; font-size:40px; opacity:.45; }}
  .handle {{ position:absolute; bottom:300px; font-size:38px; opacity:.65; font-family:'Poppins', sans-serif; font-weight:600; }}
</style></head><body>
{slides}
</body></html>"""


def slide(i, n, big, small, icon, theme):
    cls = "slide cta" if icon else "slide"
    long = " long" if len(big) > 48 else ""
    parts = [f'<section class="{cls}">', f'<div class="count">{i}/{n}</div>' if n > 1 else ""]
    parts.append(f'<div class="big{long}">{html.escape(big)}</div>')
    if small:
        parts.append(f'<div class="small">{html.escape(small)}</div>')
    if icon:
        parts.append(f'<img class="icon" src="{theme["icon"]}">')
    parts.append('<div class="handle">@milestone.and.mea</div></section>')
    return "\n".join(parts)


for name, (theme_name, slides) in POSTS.items():
    t = THEMES[theme_name]
    body = "\n".join(slide(i + 1, len(slides), *s, t) for i, s in enumerate(slides))
    (SRC / f"{name}.html").write_text(PAGE.format(slides=body, **t))
    print("wrote", name)
