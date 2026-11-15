// Renders social/packs-src/new/new-this-week.html to slide-N.png and slide-N.jpg (1080x1350).
// Usage: node social/packs-src/new/render.js <out-dir>
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const out = path.resolve(process.argv[2]);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'new-this-week.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const s = await p.$$('section.slide');
  for (let i = 0; i < s.length; i++) {
    await s[i].screenshot({ path: `${out}/slide-${i + 1}.png` });
    await s[i].screenshot({ path: `${out}/slide-${i + 1}.jpg`, type: 'jpeg', quality: 90 });
  }
  console.log(s.length, 'slides');
  await b.close();
})();
