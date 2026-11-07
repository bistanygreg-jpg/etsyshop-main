// Renders the carousel HTML files into 1080x1350 PNG slides (Instagram 4:5).
// Usage: node social/carousel-trends/src/render.js
const path = require('path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const W = 1080, H = 1350;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W * 4, height: H }, deviceScaleFactor: 1 });

  // Follow the Line: one wide canvas clipped into 4 slides so lines continue across swipes.
  await page.goto('file://' + path.join(__dirname, 'follow-the-line.html'));
  await page.evaluate(() => document.fonts.ready);
  for (let i = 0; i < 4; i++) {
    await page.screenshot({
      path: path.join(root, 'follow-the-line', `slide-${i + 1}.png`),
      clip: { x: i * W, y: 0, width: W, height: H },
    });
  }

  // Santa Didn't Pay Us: one <section> per slide.
  await page.setViewportSize({ width: W, height: H });
  await page.goto('file://' + path.join(__dirname, 'santa-didnt-pay.html'));
  await page.evaluate(() => document.fonts.ready);
  const slides = await page.$$('section.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(root, 'santa-didnt-pay', `slide-${i + 1}.png`) });
  }

  await browser.close();
})();
