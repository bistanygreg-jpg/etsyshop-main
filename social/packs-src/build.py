"""Builds Shout's hand-post packs (Nov 9-15 and Nov 16-22, 2026).

Usage: python3 social/packs-src/build.py && node social/packs-src/render.js
Each post becomes social/packs-src/html/<pack>__<post>.html; render.js writes
social/<pack>/<post>/slide-N.png (1080x1350 for Instagram/Facebook, 1080x1920 for TikTok).

Images are real: Printify mockups (shirts, golf prints), crops of the shop's own
listing graphics (printables). Copy follows CLAUDE.md house rules: real prices,
AI disclosure, "link in bio", golf "Not affiliated with any club or tour".
"""
from pathlib import Path
import html

SRC = Path(__file__).parent
OUT = SRC / "html"

AI_PRINT = "Designs made with AI design tools."
AI_GOLF = "Art created with AI tools. Not affiliated with any club or tour."
SALE = "25% off through Wed, Nov 18"

# A slide is a dict: kicker, title, sub, img, fit ("cover"|"contain"), pill, note, count.
# Layout "cta" centers text without an image.
def S(title, sub="", img=None, kicker="", pill="", note="", fit="cover", layout="hero", pill_red=False):
    return dict(title=title, sub=sub, img=img, kicker=kicker, pill=pill, note=note, fit=fit, layout=layout, pill_red=pill_red)

PACKS = {
  "wk-nov9-pack": {
    "01-mon-nov09-ig-golf": ("ig", [
        S("The golfer who has everything doesn't have this ⛳", "His favorite kind of view, on the wall", "golf-pano-golden-xmas.jpg", kicker="Gift idea for dad"),
        S("Golden hour on the fairway", "Realistic art print, printed to order", "golf-print-golden-shelf.jpg"),
        S("Or sunrise over the water", "Looks right over the mantel", "golf-print-sunrise-fireplace.jpg"),
        S("Classic poster or wide panorama", "Free shipping", layout="cta", pill="Find us on Etsy: MilestoneAndMeaning", note=AI_GOLF),
    ]),
    "02-wed-nov11-ig-fb-wishlist": ("ig", [
        S("Dear Santa…", "A wish list they'll actually want to fill in", "wishlist-page.jpg", kicker="Kids' Christmas Wish List", fit="contain"),
        S("What's inside", "Wish lists to type, write or draw · a sibling page · \"Received!\" cards from Santa's mail room", "wishlist-spread.jpg", fit="contain"),
        S("How it works", "1. Type their name (or let them write it)\n2. Print at home, US Letter or A4\n3. Mail it to the North Pole (the fridge counts)", layout="cta"),
        S("$3.99 · instant download", SALE, layout="cta", pill="Link in bio · Etsy: MilestoneAndMeaning", note=AI_PRINT),
    ]),
    "03-thu-nov12-tiktok-wishlist": ("tt", [
        S("Their Christmas list, but make it official ✉️", "", "wishlist-page.jpg", fit="contain"),
        S("Type it, write it or draw it", "plus a page for siblings", "wishlist-spread.jpg", fit="contain"),
        S("Then Santa's mail room sends a \"Received!\" card 📬", "so they know it arrived", layout="cta"),
        S("Kids' Christmas Wish List", "$3.99 · " + SALE, layout="cta", pill="link in bio", note=AI_PRINT),
    ]),
    "04-fri-nov13-ig-fb-shirts": ("ig", [
        S("Telling them about the baby on Christmas morning? 🎄", "Let Santa make the announcement", "shirt-toddler-bro-white.jpg", kicker="Big sibling reveal"),
        S("Santa promoted me to Big Sister", "Toddler tee · Baby arriving 2027", "shirt-toddler-sis-pink.jpg"),
        S("Santa promoted me to Big Brother", "Toddler and kids sizes", "shirt-kids-bro-white.jpg"),
        S("Big Brother & Big Sister shirts", "Toddler $21.99 · Kids $19.99", layout="cta", pill="Find us on Etsy: MilestoneAndMeaning", note=AI_PRINT),
    ]),
    "05-sat-nov14-ig-fb-sale": ("ig", [
        S("25% off ends Wednesday", "Nice List Kit · Christmas Eve Mega Bundle · Kids' Wish List · Scavenger Hunt", "three-kits.jpg", kicker="Launch sale", fit="contain"),
        S("Type their name, print at home, cut", "About five minutes. Nothing ships: instant download, fillable PDF, US Letter + A4.", "mega-bundle.jpg"),
        S("Regular prices", "Nice List Kit $6.99\nChristmas Eve Mega Bundle $12.99\nKids' Christmas Wish List $3.99", layout="cta", pill=SALE, pill_red=True, note=AI_PRINT),
    ]),
    "06-sun-nov15-tiktok-sale": ("tt", [
        S("Christmas Eve, sorted in 5 minutes 🎄", "type their name · print · cut", "mega-bundle.jpg"),
        S("Letter from Santa, Nice List certificate, reindeer food tags…", "", "nice-list-kit.jpg"),
        S("25% off ends Wed, Nov 18", "Nice List Kit · Christmas Eve Mega Bundle · Wish List", "three-kits.jpg", fit="contain"),
        S("Instant download", "MilestoneAndMeaning on Etsy", layout="cta", pill="link in bio", note=AI_PRINT),
    ]),
  },
  "wk-nov16-pack": {
    "01-mon-nov16-ig-bundle-sale": ("ig", [
        S("The whole Christmas Eve box, printed at home", "25% off until Wednesday", "mega-bundle.jpg", kicker="Christmas Eve Mega Bundle"),
        S("13 pages", "Box labels, magic key tags, boarding passes, door hangers, reindeer food tags and more", "everything.jpg"),
        S("Thanks for the cookies, Santa 🍪", "2 notes per page, with a spot for their name and a P.S.", "cookie-note.jpg"),
        S("Cocoa night menu", "for a cozy Christmas Eve", "cocoa.jpg"),
        S("$12.99 · includes the whole Nice List Kit", SALE, layout="cta", pill="Link in bio · Etsy: MilestoneAndMeaning", note=AI_PRINT),
    ]),
    "02-tue-nov17-fb-nicelist-sale": ("ig", [
        S("A letter from Santa, made at home", "The Nice List Kit · 25% off until tomorrow", "nice-list-kit.jpg", kicker="Nice List Kit"),
        S("24 Days of Kindness", "A December countdown with easy ideas", "kindness.jpg"),
        S("Magic reindeer food tags", "6 per page, plus the Nice List certificate", "reindeer-food.jpg"),
        S("$6.99 · 5 pages", SALE, layout="cta", pill="Find us on Etsy: MilestoneAndMeaning", note=AI_PRINT),
    ]),
    "03-wed-nov18-ig-last-day": ("ig", [
        S("Last day: 25% off", "Nice List Kit · Christmas Eve Mega Bundle · Kids' Wish List · Scavenger Hunt", "three-kits.jpg", kicker="Ends tonight", fit="contain",
          pill="Link in bio", note=AI_PRINT),
    ]),
    "04-thu-nov19-tiktok-shirts": ("tt", [
        S("The present they open last 🎁", "big sibling reveal, Christmas morning", "shirt-toddler-bro-blue.jpg"),
        S("Santa promoted me to Big Sister", "", "shirt-toddler-sis-natural.jpg"),
        S("Santa promoted me to Big Brother", "kids sizes too", "shirt-kids-bro-seated.jpg"),
        S("Big Brother & Big Sister shirts", "toddler $21.99 · kids $19.99", layout="cta", pill="link in bio", note=AI_PRINT),
    ]),
    "05-fri-nov20-ig-fb-shirts": ("ig", [
        S("Which promotion did Santa hand out at your house? ⭐", "", "shirt-toddler-bro-blue.jpg", kicker="Big sibling shirts"),
        S("Big Sister", "Toddler tee · Baby arriving 2027", "shirt-toddler-sis-natural.jpg"),
        S("Big Brother", "Toddler and kids sizes", "shirt-kids-bro-white.jpg"),
        S("Shirts for the big announcement", "Toddler $21.99 · Kids $19.99", layout="cta", pill="Find us on Etsy: MilestoneAndMeaning", note=AI_PRINT),
    ]),
    "06-sat-nov21-tiktok-golf": ("tt", [
        S("Rate these golf course views 1–10 ⛳", "", "golf-pano-sunrise-front.jpg", fit="contain"),
        S("Golden hour on the fairway", "", "golf-print-golden-front.jpg", fit="contain"),
        S("Sunrise over the water", "", "golf-print-sunrise-front.jpg", fit="contain"),
        S("Now picture it on dad's wall", "realistic golf prints · free shipping", "golf-pano-golden-fireplace.jpg"),
        S("Golf course prints", "free shipping", layout="cta", pill="link in bio", note=AI_GOLF),
    ]),
    "07-sun-nov22-ig-fb-golf": ("ig", [
        S("Sunrise or golden hour? ⛳", "Pick one for the golfer on your list", "golf-print-sunrise-front.jpg", kicker="Gift idea for dad", fit="contain"),
        S("Sunrise", "Over the mantel", "golf-print-sunrise-fireplace.jpg"),
        S("Golden hour", "Next to the bookshelf", "golf-print-golden-shelf.jpg"),
        S("Or go wide", "Panorama size for over the couch", "golf-pano-sunrise-shelf.jpg"),
        S("Realistic golf course prints", "Free shipping", layout="cta", pill="Find us on Etsy: MilestoneAndMeaning", note=AI_GOLF),
    ]),
    # Only post once Bob has published the Big Cousin tee on Etsy (HQ card ap-pf-big-cousin).
    "optional-big-cousin-slide": ("ig", [
        S("And for the cousins: Big Cousin", "Kids tee · $19.99", "shirt-kids-cousin-white.jpg", kicker="New"),
    ]),
    "optional-big-cousin-slide-tiktok": ("tt", [
        S("And for the cousins 👀", "Santa promoted me to Big Cousin · kids tee $19.99", "shirt-kids-cousin-blue.jpg"),
    ]),
  },
}

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&display=swap');
:root { --cream:#EBE2D1; --paper:#FBF6EC; --red:#8D1B1B; --green:#204D39; --gold:#C9A24A; --ink:#3B2A26; --muted:#6E5A52; }
html,body { margin:0; padding:0; background:#bbb; }
.slide { position:relative; width:1080px; background:var(--cream); color:var(--ink); font-family:Poppins, 'Noto Color Emoji', sans-serif;
  overflow:hidden; box-sizing:border-box; display:flex; flex-direction:column; align-items:center; text-align:center; padding:96px 80px 0; }
.slide.ig { height:1350px; } .slide.tt { height:1920px; padding-top:250px; }
.slide + .slide { margin-top:20px; }
.bar { position:absolute; left:0; right:0; height:22px; } .bar.top { top:0; background:var(--red); } .bar.bottom { bottom:0; background:var(--green); }
.kicker { font-weight:700; letter-spacing:5px; text-transform:uppercase; font-size:26px; color:var(--green); margin-bottom:18px; }
.title { font-weight:800; color:var(--red); font-size:68px; line-height:1.08; letter-spacing:-1px; margin:0; }
.tt .title { font-size:84px; }
.sub { font-weight:500; color:var(--green); font-size:34px; line-height:1.35; margin:20px 0 0; white-space:pre-line; }
.tt .sub { font-size:44px; }
.card { margin-top:44px; width:920px; flex:1; max-height:760px; background:var(--paper); border-radius:22px; box-shadow:0 18px 40px rgba(60,30,20,.18); overflow:hidden; }
.tt .card { max-height:1000px; }
.card.short { max-height:640px; }
.card img { display:block; width:100%; height:100%; }
.card.contain { padding:24px; box-sizing:border-box; } .card.contain img { object-fit:contain; } .card.cover img { object-fit:cover; }
.cta { justify-content:center; padding-top:0; }
.cta .title { font-size:80px; } .tt.cta .title { font-size:96px; }
.cta .sub { font-size:42px; margin-top:30px; } .tt.cta .sub { font-size:52px; }
.pill { display:inline-block; margin-top:48px; background:var(--green); color:#fff; border-radius:60px; padding:24px 52px; font-weight:700; font-size:32px; }
.pill.red { background:var(--red); }
.hero .pill { margin-top:36px; }
.note { position:absolute; bottom:96px; left:80px; right:80px; font-size:22px; color:var(--muted); font-weight:500; }
.tt .note { bottom:330px; font-size:28px; }
.handle { position:absolute; bottom:48px; left:0; right:0; font-size:24px; color:var(--muted); font-weight:600; }
.tt .handle { bottom:260px; font-size:32px; }
.spacer { height:120px; flex:none; }
"""

def slide_html(kind, s):
    e = html.escape
    cls = f"slide {kind} {s['layout']}"
    parts = [f'<section class="{cls}"><div class="bar top"></div><div class="bar bottom"></div>']
    if s["kicker"]: parts.append(f'<div class="kicker">{e(s["kicker"])}</div>')
    parts.append(f'<p class="title">{e(s["title"])}</p>')
    if s["sub"]: parts.append(f'<p class="sub">{e(s["sub"])}</p>')
    if s["img"]:
        short = " short" if s["pill"] else ""
        parts.append(f'<div class="card {s["fit"]}{short}"><img src="../img/{s["img"]}"></div>')
    if s["pill"]: parts.append(f'<span class="pill{" red" if s["pill_red"] else ""}">{e(s["pill"])}</span>')
    if s["img"]: parts.append('<div class="spacer"></div>')
    if s["note"]: parts.append(f'<div class="note">{e(s["note"])}</div>')
    handle = "@milestone.and.mea" if kind == "tt" else "@milestoneandmeaning"
    parts.append(f'<div class="handle">{handle}</div></section>')
    return "".join(parts)

def main():
    OUT.mkdir(exist_ok=True)
    for f in OUT.glob("*.html"): f.unlink()
    n = 0
    for pack, posts in PACKS.items():
        for post, (kind, slides) in posts.items():
            body = "\n".join(slide_html(kind, s) for s in slides)
            (OUT / f"{pack}__{post}.html").write_text(
                f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>\n{body}\n</body></html>\n')
            n += 1
    print(f"{n} posts written to {OUT}")

if __name__ == "__main__":
    main()
