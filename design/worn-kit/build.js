// Worn kit: builds an Etsy photo set (2000x2000) and a feel-first 9:16 video page
// for one Printify product from its real on-model mockups.
// Usage: node design/worn-kit/build.js <config.json> <asset_dir> <out_dir>
// config: { name, kicker, feel:[line1,line2], back_line, close, palette:{ink,accent,bg}, colours:[{key,label}] }
// asset_dir holds model_<key>.jpg, back_<first>.jpg, front_<first>.jpg, size.jpg (downloaded by fetch.py).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [cfgPath, assetDir, outDir] = process.argv.slice(2);
const cfg = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });
const A = f => 'data:image/jpeg;base64,' + fs.readFileSync(path.join(assetDir, f)).toString('base64');
const P = cfg.palette, first = cfg.colours[0].key;
const FONTS = `<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,800;0,9..144,900;1,9..144,500;1,9..144,600&family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">`;
const base = `*{box-sizing:border-box;margin:0}body{width:2000px;height:2000px;overflow:hidden;background:${P.bg};font-family:'Barlow Condensed'}
.k{font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:${P.accent}}
.h{font-family:'Fraunces';font-weight:900;color:${P.ink};line-height:.95}
.i{font-family:'Fraunces';font-style:italic;font-weight:600;color:${P.accent}}`;

const photos = {
  // 1. Hero: the person wearing it + the feeling
  '01-worn-hero': `<style>${base}body{background:#fff}.img{position:absolute;left:560px;top:0;width:2000px;height:2000px;object-fit:cover;object-position:50% 40%}
   .txt{position:absolute;left:90px;top:0;bottom:0;width:820px;display:flex;flex-direction:column;justify-content:center}</style>
   <img class="img" src="${A('model_' + first + '.jpg')}">
   <div class="txt"><div class="i" style="font-size:118px;line-height:1.05">${cfg.feel[0]}</div><div class="h" style="font-size:132px;margin-top:24px">${cfg.feel[1]}</div>
    <div style="width:160px;height:8px;background:${P.accent};margin:70px 0"></div>
    <div class="k" style="font-size:54px;color:${P.ink};letter-spacing:.12em;line-height:1.3">${cfg.name}</div>
    <div class="k" style="font-size:40px;color:${P.accent};margin-top:16px;letter-spacing:.12em">Comfort Colors tee · front + back</div></div>`,
  // 2. Back statement
  '02-back': `<style>${base}.img{position:absolute;inset:0;width:2000px;height:2000px;object-fit:cover;transform:scale(1.35);transform-origin:50% 36%}</style>
   <img class="img" src="${A('back_' + first + '.jpg')}">
   <div style="position:absolute;left:0;right:0;bottom:80px;text-align:center"><span class="k" style="font-size:56px;background:${P.bg};padding:14px 40px;border-radius:60px">${cfg.back_line}</span></div>`,
  // 3. Every colour, worn
  '03-colours': `<style>${base}.g{position:absolute;left:40px;right:40px;top:200px;display:grid;grid-template-columns:repeat(${cfg.colours.length},1fr);gap:20px}
   .g div{height:1600px;overflow:hidden;border-radius:24px;background:#fff;position:relative}.g img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;transform:scale(1.6);transform-origin:50% 30%}
   .g span{position:absolute;left:0;right:0;bottom:30px;text-align:center;font-weight:700;font-size:52px;letter-spacing:.15em;color:${P.ink};text-transform:uppercase}</style>
   <div style="position:absolute;left:0;right:0;top:70px;text-align:center" class="h"><span style="font-size:90px">${cfg.colours.length} soft, garment-dyed colours</span></div>
   <div class="g">${cfg.colours.map(c => `<div><img src="${A('model_' + c.key + '.jpg')}"><span>${c.label}</span></div>`).join('')}</div>`,
  // 4. Detail + fit
  '04-detail': `<style>${base}.img{position:absolute;left:0;top:0;width:1250px;height:2000px;object-fit:cover;object-position:60% 40%;transform:scale(1.55);transform-origin:62% 45%}
   .side{position:absolute;left:1300px;right:70px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:56px}</style>
   <div style="position:absolute;left:0;top:0;width:1250px;height:2000px;overflow:hidden"><img class="img" src="${A('model_' + first + '.jpg')}"></div>
   <div class="side"><div class="h" style="font-size:96px">Made to<br><span class="i">live in</span></div>
    ${['Small chest emblem, statement back', 'Garment-dyed Comfort Colors cotton', 'Relaxed unisex fit', 'Size down for a fitted look', 'Made to order for you'].map(t => `<div class="k" style="font-size:50px;color:${P.ink};letter-spacing:.08em">— ${t}</div>`).join('')}</div>`,
  // 5. Size chart (Printify's own)
  '05-size': `<style>${base}img{position:absolute;inset:0;width:2000px;height:2000px;object-fit:contain;background:#fff}</style><img src="${A('size.jpg')}">`,
};

(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 2000, height: 2000 } });
  for (const [n, body] of Object.entries(photos)) {
    await pg.setContent(`<!doctype html><html><head><meta charset="utf-8">${FONTS}</head><body>${body}</body></html>`, { waitUntil: 'networkidle' });
    await pg.screenshot({ path: path.join(outDir, n + '.jpg'), type: 'jpeg', quality: 90 });
  }
  await b.close();
  // video page for social/motion/render.js (1080x1920)
  const cuts = cfg.colours.map((c, i) => `<img class="full cut" src="${A('model_' + c.key + '.jpg')}" style="animation:cut ${i === cfg.colours.length - 1 ? 1400 : 600}ms ${6600 + i * 600}ms forwards">`).join('');
  const vid = `<!doctype html><html><head><meta charset="utf-8">${FONTS}<style>
*{box-sizing:border-box;margin:0}body{width:1080px;height:1920px;overflow:hidden;background:#fff;position:relative;font-family:'Barlow Condensed'}
.s{position:absolute;inset:0;opacity:0;overflow:hidden}.full{position:absolute;top:240px;left:-310px;width:1700px;height:1700px;object-fit:cover}
.k{font-weight:700;letter-spacing:.2em;text-transform:uppercase}.h{font-family:'Fraunces';font-weight:900;line-height:.95}.i{font-family:'Fraunces';font-style:italic;font-weight:600}
@keyframes on{0%{opacity:0}5%{opacity:1}95%{opacity:1}100%{opacity:0}}@keyframes in{from{opacity:0}to{opacity:1}}
@keyframes up{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}@keyframes push{from{transform:scale(1.08)}to{transform:scale(1)}}
@keyframes cut{0%{opacity:1}97%{opacity:1}100%{opacity:1}}.cut{opacity:0}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.06)}}
</style></head><body data-duration="11000">
<div class="s" style="opacity:1;background:${P.ink};animation:on 2600ms forwards">
 <div style="position:absolute;left:0;right:0;top:640px;text-align:center"><div class="i" style="font-size:120px;color:#fff;animation:up 600ms 150ms both">${cfg.feel[0]}</div>
 <div class="h" style="font-size:130px;color:${P.accentLight || '#FFD27A'};margin-top:30px;animation:up 600ms 1100ms both">${cfg.feel[1]}</div></div>
 <div class="k" style="position:absolute;left:0;right:0;top:1300px;text-align:center;font-size:44px;color:rgba(255,255,255,.7);animation:in 400ms 1500ms both">${cfg.kicker}</div></div>
<div class="s" style="animation:on 2300ms 2500ms forwards"><img class="full" src="${A('model_' + first + '.jpg')}" style="animation:push 2300ms 2500ms both">
 <div style="position:absolute;left:0;right:0;top:90px;text-align:center"><div class="h" style="font-size:96px;color:${P.ink};animation:up 500ms 2700ms both">${cfg.name}</div></div></div>
<div class="s" style="animation:on 1900ms 4700ms forwards;background:#fff"><img src="${A('back_' + first + '.jpg')}" style="position:absolute;left:-460px;top:160px;width:2000px;height:2000px;object-fit:cover;animation:push 1900ms 4700ms both">
 <div style="position:absolute;left:0;right:0;top:90px;text-align:center" class="k"><span style="font-size:54px;color:${P.accent};animation:in 400ms 4900ms both;display:inline-block">${cfg.back_line}</span></div></div>
<div class="s" style="animation:in 1ms 6600ms forwards">${cuts}
 <div style="position:absolute;left:0;right:0;top:90px;text-align:center" class="k"><span style="font-size:52px;color:${P.ink}">${cfg.colours.length} colours · relaxed fit</span></div></div>
<div class="s" style="animation:in 400ms 9000ms both;background:${P.ink}">
 <div style="position:absolute;left:80px;right:80px;top:720px;text-align:center"><div class="i" style="font-size:96px;color:#fff;line-height:1.15">${cfg.close}</div>
 <div class="k" style="font-size:48px;color:${P.accentLight || '#FFD27A'};margin-top:70px;display:inline-block;animation:pulse 800ms 9400ms infinite">Shop on Etsy · link in bio</div></div></div>
</body></html>`;
  fs.writeFileSync(path.join(outDir, 'video.html'), vid);
  console.log('built', Object.keys(photos).length, 'photos + video.html');
})();
