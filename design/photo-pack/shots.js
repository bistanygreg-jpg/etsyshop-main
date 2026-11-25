// Screenshot every <name>.html in a folder to <out>/<name>.jpg at 2000x2000.
// Usage: node design/photo-pack/shots.js <html_dir> <out_dir>
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [dir, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const pg = await b.newPage({viewport: {width: 2000, height: 2000}});
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort()) {
    await pg.goto('file://' + path.resolve(dir, f), {waitUntil: 'networkidle'});
    await pg.evaluate(() => document.fonts.ready);
    await pg.screenshot({path: path.join(out, f.replace('.html', '.jpg')), type: 'jpeg', quality: 88});
  }
  await b.close();
})();
