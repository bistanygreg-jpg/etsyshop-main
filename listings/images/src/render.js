// Renders the lifestyle listing photos: node listings/images/src/render.js
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 2000, height: 1600}});
  await p.goto('file://' + path.join(__dirname, 'lifestyle.html'), {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  const out = {nicelist: 'nice-list-kit_lifestyle.jpg', megabundle: 'christmas-eve-mega-bundle_lifestyle.jpg'};
  for (const [id, name] of Object.entries(out)) {
    await (await p.$('#' + id)).screenshot({path: path.join(__dirname, '..', name), type: 'jpeg', quality: 88});
  }
  await b.close();
})();
