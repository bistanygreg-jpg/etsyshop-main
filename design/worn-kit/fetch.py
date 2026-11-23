"""Download a Printify product's real on-model and flat mockups for the worn kit.
Usage: python3 design/worn-kit/fetch.py <printify_product_id> <config.json> <asset_dir>
Comfort Colors 1717 cameras: 98448 = woman wearing it (front), 98445 front flat, 98446 back flat, 110132 size chart.
(Gildan 5000 adds 101994 man front, 101995 back worn, 101996/101997 groups, 127735 lifestyle.)"""
import json, os, subprocess, sys
pid, cfg_path, out = sys.argv[1:4]
cfg = json.load(open(cfg_path)); os.makedirs(out, exist_ok=True)
H = ["-H", "Authorization: Bearer proxy-injected"]
p = json.loads(subprocess.run(["curl", "-sS", *H, f"https://api.printify.com/v1/shops/29591075/products/{pid}.json"], capture_output=True, text=True).stdout)
var = {}  # colour label -> first enabled variant id
for v in p["variants"]:
    if v["is_enabled"]:
        var.setdefault(v["title"].split(" / ")[-1].strip().lower(), v["id"])
B = f"https://images.printify.com/mockup/{pid}"
def get(url, name): subprocess.run(["curl", "-sS", "-o", os.path.join(out, name), url + "?s=2048"])
for c in cfg["colours"]:
    get(f"{B}/{var[c['key']]}/98448/x.jpg", f"model_{c['key']}.jpg")
first = var[cfg["colours"][0]["key"]]
get(f"{B}/{first}/98446/x.jpg", f"back_{cfg['colours'][0]['key']}.jpg")
get(f"{B}/{first}/98445/x.jpg", f"front_{cfg['colours'][0]['key']}.jpg")
get(f"{B}/{first}/110132/x.jpg", "size.jpg")
print("fetched", len(cfg["colours"]) + 3, "images for", p["title"][:50])
