"""Photo pack: Etsy's "10+ images and a short video" for any Printify listing (owner, Nov 25).

Etsy emails ask for "a short video and 10+ images from different angles or in use".
Printify only pushes 3-4 mockups for most of our shirts, so this builds 10 square
2000x2000 photos plus a 10 s video from REAL Printify renders of the exact product
(never AI people, never invented mockups), framed in the shop's design system.

Usage:
  python3 design/photo-pack/build.py <printify_product_id> <config.json> <out_dir>
config (see design/photo-pack/configs/):
  name, kicker, feel:[line1,line2], moment (gift/use line), back_line, audience,
  palette {ink, accent, bg}, cams {front, back, model?, size?, extra:[...]} (camera ids for the blueprint),
  colours: optional list of colour names to show (defaults to all enabled colours, max 4)
Output: 01..10 jpgs + <slug>-video.mp4 (rendered with social/motion/render.js). Mac agent uploads them
from listings/etsy-upload-queue.md.
"""
import json, os, subprocess, sys, base64, tempfile

pid, cfg_path, out = sys.argv[1:4]
cfg = json.load(open(cfg_path))
os.makedirs(out, exist_ok=True)
tmp = tempfile.mkdtemp(prefix="pp_")
H = ["-H", "Authorization: Bearer proxy-injected"]
p = json.loads(subprocess.run(["curl", "-sS", *H, f"https://api.printify.com/v1/shops/29591075/products/{pid}.json"],
                              capture_output=True, text=True).stdout)
# first enabled variant per colour
by_colour = {}
copt = next((o for o in p.get("options", []) if o.get("type") == "color"), None)
cname = {val["id"]: val["title"] for val in (copt["values"] if copt else [])}
for v in p["variants"]:
    if v["is_enabled"]:
        cid = next((o for o in v.get("options", []) if o in cname), None)
        by_colour.setdefault(cname.get(cid, v["title"].split(" / ")[0].strip()), v["id"])
colours = cfg.get("colours") or list(by_colour)[:4]
colours = [c for c in colours if c in by_colour][:4] or list(by_colour)[:1]
first = by_colour[colours[0]]
B = f"https://images.printify.com/mockup/{pid}"


def get(var, cam, name):
    path = os.path.join(tmp, name)
    subprocess.run(["curl", "-sS", "-o", path, f"{B}/{var}/{cam}/x.jpg?s=2048"])
    ok = os.path.exists(path) and os.path.getsize(path) > 5000
    return path if ok else None


C = cfg["cams"]
img = {"front": get(first, C["front"], "front.jpg"), "back": get(first, C["back"], "back.jpg")}
if C.get("model"): img["model"] = get(first, C["model"], "model.jpg")
if C.get("size"): img["size"] = get(first, C["size"], "size.jpg")
for i, cam in enumerate(C.get("extra", [])):
    img[f"extra{i}"] = get(first, cam, f"extra{i}.jpg")
img["colours"] = [(c, get(by_colour[c], C["front"], f"col{i}.jpg")) for i, c in enumerate(colours)]
img = {k: v for k, v in img.items() if v}


def A(path):
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()


P = cfg["palette"]
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,800;0,9..144,900;1,9..144,500;1,9..144,600&family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">'
base = f"""*{{box-sizing:border-box;margin:0}}body{{width:2000px;height:2000px;overflow:hidden;background:{P['bg']};font-family:'Barlow Condensed';position:relative}}
.k{{font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{P['accent']}}}
.h{{font-family:'Fraunces';font-weight:900;color:{P['ink']};line-height:.98}}
.i{{font-family:'Fraunces';font-style:italic;font-weight:600;color:{P['accent']}}}
.card{{position:absolute;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.08)}}
.card img{{width:100%;height:100%;object-fit:cover}}"""
hero = img.get("model", img["front"])
slides = {}
# 01 hero: the feeling + the product
slides["01-hero"] = f"""<div class="card" style="left:760px;top:120px;width:1140px;height:1760px"><img src="{A(hero)}" style="object-position:50% 35%"></div>
<div style="position:absolute;left:100px;top:0;bottom:0;width:620px;display:flex;flex-direction:column;justify-content:center">
<div class="i" style="font-size:96px;line-height:1.05">{cfg['feel'][0]}</div><div class="h" style="font-size:112px;margin-top:20px">{cfg['feel'][1]}</div>
<div style="width:140px;height:8px;background:{P['accent']};margin:60px 0"></div>
<div class="k" style="font-size:48px;color:{P['ink']};letter-spacing:.1em;line-height:1.25">{cfg['name']}</div></div>"""
# 02 front, big
slides["02-front"] = f"""<img src="{A(img['front'])}" style="position:absolute;inset:0;width:2000px;height:2000px;object-fit:cover;background:#fff">
<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center"><span class="k" style="font-size:52px;background:{P['bg']};padding:14px 40px;border-radius:60px">The front</span></div>"""
# 03 back
slides["03-back"] = f"""<img src="{A(img['back'])}" style="position:absolute;inset:0;width:2000px;height:2000px;object-fit:cover;background:#fff">
<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center"><span class="k" style="font-size:52px;background:{P['bg']};padding:14px 40px;border-radius:60px">{cfg['back_line']}</span></div>"""
# 04 front + back together
slides["04-both"] = f"""<div class="h" style="position:absolute;left:0;right:0;top:90px;text-align:center;font-size:110px">Printed front <span class="i">&amp;</span> back</div>
<div class="card" style="left:80px;top:330px;width:900px;height:1500px"><img src="{A(img['front'])}"></div>
<div class="card" style="left:1020px;top:330px;width:900px;height:1500px"><img src="{A(img['back'])}"></div>"""
# 05 detail close-up
slides["05-detail"] = f"""<div style="position:absolute;inset:0;overflow:hidden"><img src="{A(img['front'])}" style="width:2000px;height:2000px;object-fit:cover;transform:scale(2.1);transform-origin:50% 38%"></div>
<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center"><span class="k" style="font-size:52px;background:{P['bg']};padding:14px 40px;border-radius:60px">Up close: crisp, soft-hand print</span></div>"""
# 06 colours
n = len(img["colours"])
slides["06-colours"] = f"""<div class="h" style="position:absolute;left:0;right:0;top:90px;text-align:center;font-size:100px">{n} colour{'s' if n > 1 else ''} to choose from</div>
<div style="position:absolute;left:60px;right:60px;top:300px;display:grid;grid-template-columns:repeat({max(n,1)},1fr);gap:24px">""" + "".join(
    f"""<div class="card" style="position:relative;height:1560px"><img src="{A(path)}" style="object-position:50% 40%;transform:scale(1.25)"><div class="k" style="position:absolute;left:0;right:0;bottom:36px;text-align:center;font-size:46px;color:{P['ink']}">{c}</div></div>"""
    for c, path in img["colours"]) + "</div>"
# 07 the moment (gift / in use)
slides["07-moment"] = f"""<div style="position:absolute;inset:0;background:{P['ink']}"></div>
<div class="card" style="left:1060px;top:200px;width:820px;height:1600px"><img src="{A(img.get('extra0', hero))}" style="object-position:50% 35%"></div>
<div style="position:absolute;left:110px;top:0;bottom:0;width:860px;display:flex;flex-direction:column;justify-content:center">
<div class="k" style="font-size:46px;color:#FFD27A">{cfg['kicker']}</div>
<div style="font-family:Fraunces;font-weight:900;color:#fff;font-size:118px;line-height:1.02;margin-top:40px">{cfg['moment']}</div></div>"""
# 08 who it's for + details
slides["08-details"] = f"""<div class="card" style="left:80px;top:200px;width:900px;height:1600px"><img src="{A(img.get('extra1', img['front']))}" style="object-position:50% 40%"></div>
<div style="position:absolute;left:1060px;right:90px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:50px">
<div class="h" style="font-size:100px">Made for<br><span class="i">{cfg['audience']}</span></div>""" + "".join(
    f'<div class="k" style="font-size:48px;color:{P["ink"]};letter-spacing:.06em">— {t}</div>' for t in cfg["details"]) + "</div>"
# 09 size chart (Printify's) or sizing note
if img.get("size"):
    slides["09-size"] = f"""<img src="{A(img['size'])}" style="position:absolute;inset:0;width:2000px;height:2000px;object-fit:contain;background:#fff">"""
else:
    slides["09-size"] = f"""<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:60px;text-align:center;padding:0 160px">
<div class="h" style="font-size:120px">Finding the right size</div>
<div class="k" style="font-size:54px;color:{P['ink']};line-height:1.5;letter-spacing:.06em">{cfg['size_note']}</div>
<div class="i" style="font-size:72px">Not sure? Message us your child's height and we'll help you pick.</div></div>"""
# 10 order note (honest dates only)
slides["10-order"] = f"""<div style="position:absolute;inset:0;background:{P['ink']}"></div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:70px;text-align:center;padding:0 160px">
<div class="i" style="font-size:110px;color:#FFD27A">Made to order, just for you</div>
<div style="font-family:Fraunces;font-weight:900;color:#fff;font-size:120px;line-height:1.05">{cfg['order_line']}</div>
<div class="k" style="font-size:50px;color:rgba(255,255,255,.8)">Milestone &amp; Meaning</div></div>"""

here = os.path.dirname(os.path.abspath(__file__))
hdir = os.path.join(tmp, "html"); os.makedirs(hdir, exist_ok=True)
for name, body in slides.items():
    open(os.path.join(hdir, name + ".html"), "w").write(
        f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{base}</style></head><body>{body}</body></html>')
subprocess.run(["node", os.path.join(here, "shots.js"), hdir, out], check=True)

# 10 s square video for the Etsy listing (Etsy plays it muted): slow push-ins across the strongest frames
order = ["01-hero", "03-back", "05-detail", "06-colours", "07-moment", "10-order"]
dur = 10000; step = dur // len(order)
frames = "".join(
    f'<img src="{A(os.path.join(out, n + ".jpg"))}" style="position:absolute;inset:0;width:1080px;height:1080px;opacity:0;animation:show {step + 300}ms {i * step}ms forwards">'
    for i, n in enumerate(order))
vid = f"""<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0}}body{{width:1080px;height:1920px;background:{P['bg']};overflow:hidden;position:relative}}
.wrap{{position:absolute;left:0;top:420px;width:1080px;height:1080px;overflow:hidden}}
@keyframes show{{0%{{opacity:0;transform:scale(1.06)}}8%{{opacity:1}}100%{{opacity:1;transform:scale(1)}}}}</style></head>
<body data-duration="{dur}"><div class="wrap">{frames}</div></body></html>"""
vp = os.path.join(tmp, "video.html")
open(vp, "w").write(vid)
slug = os.path.basename(os.path.normpath(out))
subprocess.run(["node", os.path.join(here, "..", "..", "social", "motion", "render.js"), vp, os.path.join(out, slug + "-video.mp4")], check=True)
# crop the 9:16 render to a square 1080x1080 for Etsy (keeps file small, fills the listing frame)
sq = os.path.join(out, slug + "-video.mp4")
tmpv = os.path.join(tmp, "sq.mp4")
subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", sq, "-vf", "crop=1080:1080:0:420", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "24", tmpv], check=True)
os.replace(tmpv, sq)
print("built", len(slides), "photos +", slug + "-video.mp4", "| colours:", [c for c, _ in img["colours"]], "| missing:", [k for k in ("model", "size") if C.get(k) and k not in img])
