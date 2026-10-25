// High-resolution export: node export-hires.cjs <src-dir> <out-dir> [scale=3] -> re-renders every NN-*.html at scale x (3 -> 3240x4050).
let chromium; try { ({ chromium } = require("playwright")); } catch { ({ chromium } = require("/opt/node-tools/node_modules/playwright")); }
const fs = require('fs'), path = require('path');
const [,, src, out] = process.argv;
fs.mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: Number(process.argv[4] || 3) });
  for (const f of fs.readdirSync(src).filter(f => /^\d\d-.*\.html$/.test(f)).sort()) {
    await p.goto('file://' + path.join(src, f));
    await p.evaluate(() => document.fonts.ready); await p.waitForLoadState('networkidle');
    await p.screenshot({ path: path.join(out, f.replace('.html', '.png')) });
  }
  await b.close();
})();
