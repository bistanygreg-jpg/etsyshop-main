# Mixtape Mercantile video tools (for Riff, the Mixtape agent)

- `v-*.html` + `base.css`: 8 product video concepts (cassette deck, 1999 CD burn, flashlight, camcorder skate video, dial-up, pixel game, roller rink, arcade) and the "take me back" brand intro (`v-takemeback*.html`). Render them with `node social/motion/render.js <file.html> <out.mp4>`.
- They expect the product's on-model images next to the HTML, named `<printify_id>_<view>.jpg`. Fetch them from `https://images.printify.com/mockup/<printify_id>/<variant_id>/<camera>/x.jpg?s=1600` (Printify store 29843816). Gildan 5000 cameras: hero 101994, turn 101995, backguy 101990, backcurly 101992, duo 101996, pair 101997, side 101991, design 102002, fold 102001, hanger 102003, chair 102004, flat 127735.
- `scenes/tmb*.jpg`: the AI-generated 90s scenes (no products, no brands): 1 cul-de-sac, 2 VHS, 3 phone cord, 4 dial-up, 5 boombox, 6 roller rink, 7 sleepover.
- Voiceover: `vo.py` and `vo_slow.py` use Kokoro TTS (Apache-2.0; `pip install kokoro-onnx soundfile`; model files from github.com/thewh1teagle/kokoro-onnx releases, `model-files-v1.0`). **Mixtape voice: af_nicole** (soft), at natural pace with pauses (`vo_slow.py`).
- Rules: real Printify renders for shirts only; AI scenes are moods only; no real brands, logos or copyrighted characters; add TikTok's AI label when posting.
