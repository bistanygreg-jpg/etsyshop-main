// Render kit designs to transparent PNGs, cropped later.
// Usage: node design/apparel-kit/render.js <html file in this folder> <outdir> [id ...]
// Full-size outputs are print files: write them to the scratchpad, never commit them.
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const [file, outdir, ...ids] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 3200, height: 3600}});
  await p.goto('file://' + path.join(__dirname, file), {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  const all = ids.length ? ids : await p.$$eval('.wrap[id]', els => els.map(e => e.id));
  for (const id of all) {
    const el = await p.$('#' + id + ' svg');
    await el.screenshot({path: path.join(outdir, id + '.png'), omitBackground: true});
    console.log('rendered', id);
  }
  await b.close();
})();
