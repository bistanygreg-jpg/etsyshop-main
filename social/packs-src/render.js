// Renders social/packs-src/html/<pack>__<post>.html into social/<pack>/<post>/slide-N.png.
// Usage: node social/packs-src/render.js [filter ...]   (filter matches part of the file name)
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const htmlDir = path.join(__dirname, 'html');
const socialDir = path.resolve(__dirname, '..');
const only = process.argv.slice(2);

(async () => {
  const files = fs.readdirSync(htmlDir).filter(f => f.endsWith('.html'))
    .filter(f => !only.length || only.some(o => f.includes(o)));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const f of files) {
    const [pack, post] = f.slice(0, -5).split('__');
    const out = path.join(socialDir, pack, post);
    fs.mkdirSync(out, { recursive: true });
    for (const g of fs.readdirSync(out)) if (/^slide-\d+\.png$/.test(g)) fs.unlinkSync(path.join(out, g));
    await page.goto('file://' + path.join(htmlDir, f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const slides = await page.$$('section.slide');
    for (let i = 0; i < slides.length; i++) await slides[i].screenshot({ path: path.join(out, `slide-${i + 1}.png`) });
    console.log(`${pack}/${post}: ${slides.length} slides`);
  }
  await browser.close();
})();
