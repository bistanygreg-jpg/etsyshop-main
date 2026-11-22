// Frame-accurate renderer for animated social videos (Reels / TikTok / Shorts, 1080x1920).
// Usage: node social/motion/render.js <file.html> <out.mp4> [fps=30]
// The page must set <body data-duration="ms">. Every CSS animation is paused and seeked
// to the exact frame time, screenshotted, then encoded with ffmpeg (H.264, yuv420p).
const {chromium} = require('playwright');
const path = require('path'), fs = require('fs'), os = require('os');
const {execFileSync} = require('child_process');
(async () => {
  const [file, out, fpsArg] = process.argv.slice(2);
  const fps = Number(fpsArg || 30);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1920}});
  await p.goto('file://' + path.resolve(__dirname, file), {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const dur = await p.evaluate(() => Number(document.body.dataset.duration));
  const frames = Math.round(dur / 1000 * fps);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'mm-frames-'));
  await p.evaluate(() => document.getAnimations().forEach(a => a.pause()));
  for (let i = 0; i < frames; i++) {
    const t = i * 1000 / fps;
    await p.evaluate(t => document.getAnimations().forEach(a => { a.currentTime = t; }), t);
    await p.screenshot({path: path.join(dir, `f${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92});
  }
  await b.close();
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(dir, 'f%05d.jpg'),
    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out]);
  fs.rmSync(dir, {recursive: true, force: true});
  console.log('wrote', out, frames, 'frames');
})();
