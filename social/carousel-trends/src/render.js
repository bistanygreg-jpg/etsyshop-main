// Renders every carousel in this folder into 1080x1350 PNG slides (Instagram 4:5).
// Usage: node social/carousel-trends/src/render.js [name ...]
//
// Two layouts are supported:
//  - a wide #canvas with data-slides="N" (or 4 by default): clipped into N slides so
//    lines and trails continue across swipes;
//  - one <section class="slide"> per slide.
// Output goes to social/carousel-trends/<name>/slide-<n>.png.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const W = 1080, H = 1350;
const only = process.argv.slice(2);

(async () => {
  const names = fs.readdirSync(__dirname)
    .filter(f => f.endsWith('.html'))
    .map(f => f.replace(/\.html$/, ''))
    .filter(n => !only.length || only.includes(n));

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W * 6, height: H }, deviceScaleFactor: 1 });

  for (const name of names) {
    const outDir = path.join(root, name);
    fs.mkdirSync(outDir, { recursive: true });
    for (const f of fs.readdirSync(outDir)) if (/^slide-\d+\.png$/.test(f)) fs.unlinkSync(path.join(outDir, f));

    await page.setViewportSize({ width: W * 6, height: H });
    await page.goto('file://' + path.join(__dirname, name + '.html'), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);

    const canvas = await page.$('#canvas');
    let count;
    if (canvas) {
      count = +(await canvas.getAttribute('data-slides') || 4);
      for (let i = 0; i < count; i++) {
        await page.screenshot({ path: path.join(outDir, `slide-${i + 1}.png`), clip: { x: i * W, y: 0, width: W, height: H } });
      }
    } else {
      await page.setViewportSize({ width: W, height: H });
      const slides = await page.$$('section.slide');
      count = slides.length;
      for (let i = 0; i < count; i++) {
        await slides[i].screenshot({ path: path.join(outDir, `slide-${i + 1}.png`) });
      }
    }
    console.log(`${name}: ${count} slides`);
  }
  await browser.close();
})();
