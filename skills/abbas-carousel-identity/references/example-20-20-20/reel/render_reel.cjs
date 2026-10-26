// Captures reel.html frame by frame (deterministic: render(t) per frame, no real-time playback).
// node render_frames.cjs [--preview t1,t2,...]   → stills for review
// node render_frames.cjs                          → frames/00000.png … + cues.json
const fs = require('fs'), path = require('path');
let chromium; try { ({ chromium } = require('playwright')); } catch { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }
const root = __dirname;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: Number(process.env.SS || 1) });
  const warnings = [];
  p.on('console', m => { if (m.type() === 'warning' || m.type() === 'error') warnings.push(m.text()); });
  await p.goto('file://' + path.join(root, 'reel.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForLoadState('networkidle');
  const TL = await p.evaluate(() => { window.render(0); const T = window.TIMELINE; return { ...T, ends: T.ends, cues: T.cues }; });
  fs.writeFileSync(path.join(root, 'cues-reel.json'), JSON.stringify(TL, null, 1));
  const prev = process.argv.indexOf('--preview');
  if (prev > 0) {
    const out = path.join(root, 'preview-reel'); fs.mkdirSync(out, { recursive: true });
    for (const t of process.argv[prev + 1].split(',').map(Number)) {
      await p.evaluate(t => window.render(t), t);
      await p.screenshot({ path: path.join(out, `t${t.toFixed(2).padStart(6, '0')}.png`) });
    }
  } else {
    const out = path.join(root, 'frames-reel'); fs.rmSync(out, { recursive: true, force: true }); fs.mkdirSync(out);
    const n = Math.round(TL.END * TL.FPS);
    for (let f = 0; f < n; f++) {
      await p.evaluate(t => window.render(t), f / TL.FPS);
      await p.screenshot({ path: path.join(out, String(f).padStart(5, '0') + '.png') });
      if (f % 150 === 0) console.log('frame', f, '/', n);
    }
    console.log('frames-reel', n);
  }
  if (warnings.length) console.log('WARN', [...new Set(warnings)].join(' | '));
  await b.close();
})();
