// Renders each src/<name>.html (one <section class="slide"> per slide) into
// social/tiktok/<name>/slide-N.png at 1080x1920 for TikTok photo mode.
// Usage: node social/tiktok/src/render.js [name ...]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const only = process.argv.slice(2);

(async () => {
  const names = fs.readdirSync(__dirname).filter(f => f.endsWith('.html')).map(f => f.slice(0, -5))
    .filter(n => !only.length || only.includes(n));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const name of names) {
    const out = path.join(root, name);
    fs.mkdirSync(out, { recursive: true });
    for (const f of fs.readdirSync(out)) if (/^slide-\d+\.png$/.test(f)) fs.unlinkSync(path.join(out, f));
    await page.goto('file://' + path.join(__dirname, name + '.html'), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const slides = await page.$$('section.slide');
    for (let i = 0; i < slides.length; i++) await slides[i].screenshot({ path: path.join(out, `slide-${i + 1}.png`) });
    console.log(`${name}: ${slides.length} slides`);
  }
  await browser.close();
})();
