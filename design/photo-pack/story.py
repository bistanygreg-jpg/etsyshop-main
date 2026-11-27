"""Story photos for family-reveal listings (owner, Nov 27: "get creative").

Printify's on-model photos only show young adults, so for Grandma/Grandpa (and any reveal role)
we tell the reveal story AROUND the real shirt instead of faking a person wearing it:
  11-gift-box    the real folded shirt in a kraft gift box with ribbon and a to/from tag
  12-group-chat  the moment the news lands: a family group chat with the real shirt photo
  13-family-set  the matching reveal set: this shirt plus our other live reveal shirts (real renders)
Every shirt image is a real Printify render of the exact product. No AI people, no invented mockups.

Usage: python3 design/photo-pack/story.py <config.json> <out_dir>
config: { role, tag_to, tag_from, chat:[[side,text],...], palette{ink,accent,bg},
          shirt:{pid, folded, flat, front}, set:[{pid, cam, label}, ...] }
"""
import base64, json, os, subprocess, sys, tempfile

cfg_path, out = sys.argv[1:3]
cfg = json.load(open(cfg_path))
os.makedirs(out, exist_ok=True)
tmp = tempfile.mkdtemp(prefix="story_")
H = ["-H", "Authorization: Bearer proxy-injected"]


def first_variant(pid):
    p = json.loads(subprocess.run(["curl", "-sS", *H, f"https://api.printify.com/v1/shops/29591075/products/{pid}.json"],
                                  capture_output=True, text=True).stdout)
    want = cfg.get("colour")
    copt = next((o for o in p.get("options", []) if o.get("type") == "color"), None)
    names = {v["id"]: v["title"] for v in (copt["values"] if copt else [])}
    for v in p["variants"]:
        if v["is_enabled"] and (not want or any(names.get(o) == want for o in v["options"])):
            return v["id"]
    return next(v["id"] for v in p["variants"] if v["is_enabled"])


def get(pid, cam, name):
    path = os.path.join(tmp, name)
    subprocess.run(["curl", "-sS", "-m", "90", "-o", path,
                    f"https://images.printify.com/mockup/{pid}/{first_variant(pid)}/{cam}/x.jpg?s=1600"])
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()


S = cfg["shirt"]
folded = get(S["pid"], S["folded"], "folded.jpg")
flat = get(S["pid"], S["flat"], "flat.jpg")
sets = [(s["label"], get(s["pid"], s["cam"], f"set{i}.jpg")) for i, s in enumerate(cfg["set"])]
P = cfg["palette"]
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,800;0,9..144,900;1,9..144,500;1,9..144,600&family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;600&display=swap" rel="stylesheet">'
base = f"""*{{box-sizing:border-box;margin:0}}body{{width:2000px;height:2000px;overflow:hidden;background:{P['bg']};position:relative;font-family:'Barlow Condensed'}}
.k{{font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{P['accent']}}}
.h{{font-family:'Fraunces';font-weight:900;color:{P['ink']};line-height:1}}
.i{{font-family:'Fraunces';font-style:italic;font-weight:600;color:{P['accent']}}}"""

slides = {}
# 11 gift box: kraft box (CSS), tissue, the real folded shirt inside, ribbon, hand-lettered tag
slides["11-gift-box"] = f"""
<div class="h" style="position:absolute;left:0;right:0;top:110px;text-align:center;font-size:104px">The box {cfg.get("they","she")} opens <span class="i">last</span></div>
<div style="position:absolute;left:330px;top:420px;width:1340px;height:1280px;background:linear-gradient(160deg,#C9A27A,#B08458);border-radius:18px;box-shadow:0 40px 90px rgba(60,35,10,.28)"></div>
<div style="position:absolute;left:380px;top:470px;width:1240px;height:1180px;background:#F7F1E6;border-radius:10px;overflow:hidden">
  <div style="position:absolute;inset:0;background:repeating-linear-gradient(115deg,rgba(255,255,255,.0) 0 60px,rgba(230,220,205,.55) 60px 64px)"></div>
  <img src="{folded}" style="position:absolute;left:60px;top:50px;width:1120px;height:1080px;object-fit:cover;border-radius:6px;mix-blend-mode:multiply">
</div>
<div style="position:absolute;left:330px;top:1010px;width:1340px;height:70px;background:{P['accent']};opacity:.92"></div>
<div style="position:absolute;left:1240px;top:900px;width:420px;height:300px;transform:rotate(-8deg);background:#FBF6EC;border-radius:14px;box-shadow:0 18px 40px rgba(0,0,0,.18);padding:46px 50px">
  <div class="k" style="font-size:34px">{cfg['tag_kicker']}</div>
  <div class="i" style="font-size:64px;color:{P['ink']};margin-top:18px;line-height:1.05">To {cfg['tag_to']},</div>
  <div class="i" style="font-size:44px;margin-top:14px">{cfg['tag_from']}</div>
</div>
<div class="k" style="position:absolute;left:0;right:0;bottom:90px;text-align:center;font-size:48px;color:{P['ink']}">Wrap it. Watch {cfg.get("them","her")} read it. That's the whole plan.</div>"""

# 12 group chat: generic phone, our own simple chat UI (no app branding), real flat-lay photo bubble
bubbles = ""
for side, text in cfg["chat"]:
    if side == "photo":
        bubbles += f'<div style="align-self:flex-end;width:560px;border-radius:34px;overflow:hidden;margin:10px 0"><img src="{flat}" style="width:100%;display:block"></div>'
    else:
        me = side == "me"
        bubbles += (f'<div style="align-self:{"flex-end" if me else "flex-start"};max-width:640px;background:{"#2F6B4F" if me else "#ECE7DF"};'
                    f'color:{"#fff" if me else "#222"};font-family:Inter;font-size:40px;line-height:1.3;padding:24px 34px;border-radius:40px;margin:8px 0">{text}</div>')
slides["12-group-chat"] = f"""
<div style="position:absolute;left:110px;top:0;bottom:0;width:640px;display:flex;flex-direction:column;justify-content:center">
  <div class="k" style="font-size:44px">{cfg['chat_kicker']}</div>
  <div class="h" style="font-size:118px;margin-top:30px">{cfg['chat_headline']}</div>
  <div class="i" style="font-size:64px;margin-top:40px">{cfg['chat_sub']}</div></div>
<div style="position:absolute;left:880px;top:110px;width:960px;height:1780px;background:#111;border-radius:110px;padding:36px;box-shadow:0 40px 100px rgba(0,0,0,.25)">
  <div style="width:100%;height:100%;background:#fff;border-radius:80px;overflow:hidden;display:flex;flex-direction:column">
    <div style="height:170px;border-bottom:2px solid #eee;display:flex;align-items:center;justify-content:center;font-family:Inter;font-weight:600;font-size:42px;color:#222">{cfg['chat_title']}</div>
    <div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding:40px 44px 60px">{bubbles}</div>
  </div></div>"""

# 13 family set: real renders of the matching reveal shirts
n = len(sets)
slides["13-family-set"] = f"""
<div class="h" style="position:absolute;left:0;right:0;top:100px;text-align:center;font-size:104px">The whole family, <span class="i">promoted</span></div>
<div style="position:absolute;left:70px;right:70px;top:330px;display:grid;grid-template-columns:repeat({n},1fr);gap:30px">""" + "".join(
    f'<div style="background:#fff;border-radius:28px;overflow:hidden;height:1380px;position:relative;box-shadow:0 20px 60px rgba(0,0,0,.08)"><img src="{img}" style="width:100%;height:100%;object-fit:cover;object-position:50% 40%"><div class="k" style="position:absolute;left:0;right:0;bottom:40px;text-align:center;font-size:44px;color:{P["ink"]}">{label}</div></div>'
    for label, img in sets) + f"""</div>
<div class="k" style="position:absolute;left:0;right:0;bottom:80px;text-align:center;font-size:46px;color:{P['ink']}">Each sold separately in our shop · matching "Promoted by Santa" design</div>"""

hdir = os.path.join(tmp, "html"); os.makedirs(hdir)
for name, body in slides.items():
    open(os.path.join(hdir, name + ".html"), "w").write(
        f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{base}</style></head><body>{body}</body></html>')
here = os.path.dirname(os.path.abspath(__file__))
subprocess.run(["node", os.path.join(here, "shots.js"), hdir, out], check=True, stdin=subprocess.DEVNULL)
print("built", list(slides))
