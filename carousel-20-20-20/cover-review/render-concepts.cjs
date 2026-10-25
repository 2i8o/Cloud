// Renders the cover concepts plus mobile-size and thumbnail-size review sheets.
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path = require('path'), fs = require('fs');
const root = path.resolve(__dirname, '..');
const items = [
  ['A — رسالة من عيونك (المختار)', 'src/01-cover.html', 'cover-review/A-selected.png'],
  ['B — ثلاث عشرينات', 'concepts/B-three-twenties.html', 'cover-review/B-three-twenties.png'],
  ['C — أبعد شي باوعتله', 'concepts/C-farthest-view.html', 'cover-review/C-farthest-view.png'],
  ['الغلاف الحالي (rev3)', null, 'cover-review/current-rev3.png'],
];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const [, src, out] of items) {
    if (!src) continue;
    await p.goto('file://' + path.join(root, src)); await p.evaluate(() => document.fonts.ready); await p.waitForLoadState('networkidle');
    await p.screenshot({ path: path.join(root, out) });
  }
  // review sheet: each concept at full-ish, phone feed (390 px), and grid thumbnail (124 px)
  const font = 'file://' + path.join(root, 'fonts/ibm-plex-sans-arabic-arabic-600-normal.woff2');
  const rows = items.map(([l, , out]) => `<div class=r><div class=l>${l}</div><img class=f src="file://${path.join(root, out)}"><img class=m src="file://${path.join(root, out)}"><img class=t src="file://${path.join(root, out)}"></div>`).join('');
  const html = `<!doctype html><meta charset=utf-8><style>@font-face{font-family:P;src:url(${font})}body{margin:0;background:#e9edf2;padding:24px;font:600 24px P;color:#222;direction:rtl}.r{display:flex;align-items:flex-end;gap:28px;margin-bottom:28px}.l{width:220px}.f{width:520px}.m{width:390px}.t{width:124px}.h{display:flex;gap:28px;margin:0 0 12px 248px;font-size:20px;color:#555}.h span:nth-child(1){width:520px}.h span:nth-child(2){width:390px}</style><div class=h><span>كامل (مصغّر)</span><span>حجم الهاتف ≈ 390</span><span>مصغّرة الشبكة ≈ 124</span></div>${rows}`;
  fs.writeFileSync(path.join(root, 'cover-review/sheet.html'), html);
  await p.setViewportSize({ width: 1440, height: 900 });
  await p.goto('file://' + path.join(root, 'cover-review/sheet.html')); await p.waitForLoadState('networkidle');
  await p.screenshot({ path: path.join(root, 'cover-review/review-sheet.png'), fullPage: true });
  fs.unlinkSync(path.join(root, 'cover-review/sheet.html'));
  await b.close();
})();
