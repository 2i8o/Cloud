// Pixel-level QA on the rendered slides.
//  1. Glyph collisions: real ink overlap between two text elements (not line-box intersection).
//  2. Contrast: WCAG ratio measured per glyph pixel against the actual rendered background,
//     with the large-text threshold judged at phone display size (1080 px canvas ≈ 390 css px).
// Usage: node qa.mjs [slide-prefix ...]
import { createRequire } from 'module';
import { readdirSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const require = createRequire(import.meta.url);
let playwright;
try { playwright = require('playwright'); } catch { playwright = require('/opt/node-tools/node_modules/playwright'); }

const root = dirname(fileURLToPath(import.meta.url));
const src = resolve(root, 'src');
const only = process.argv.slice(2);
const slides = readdirSync(src).filter(f => /^\d\d-.*\.html$/.test(f)).sort()
  .filter(f => !only.length || only.some(p => f.startsWith(p)));
const PHONE = 390 / 1080;

const browser = await playwright.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });

for (const f of slides) {
  await page.goto('file://' + resolve(src, f));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForLoadState('networkidle');

  // tag every element that directly owns visible text
  const items = await page.evaluate(() => {
    const els = new Set();
    const w = document.createTreeWalker(document.querySelector('.slide'), NodeFilter.SHOW_TEXT);
    while (w.nextNode()) if (w.currentNode.nodeValue.trim()) els.add(w.currentNode.parentElement);
    // contrast is judged per direct text owner (its own size/weight/colour);
    // collisions per block (spans of one line touching each other are not a defect)
    const owners = [...els];
    const blocks = [...new Set(owners.map(e => e.closest('.abs, .sig, .pager, text') || e))];
    let i = 0; const out = [];
    for (const e of owners) { e.setAttribute('data-qa', i); const r = e.getBoundingClientRect();
      out.push({ i: i++, kind: 'owner', text: [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.nodeValue).join(' ').trim().replace(/\s+/g, ' ').slice(0, 26), r: [r.left, r.top, r.right, r.bottom] }); }
    for (const e of blocks) { e.setAttribute('data-qb', i); const r = e.getBoundingClientRect();
      out.push({ i: i++, kind: 'block', text: e.textContent.trim().replace(/\s+/g, ' ').slice(0, 26), r: [r.left, r.top, r.right, r.bottom] }); }
    return out;
  });

  // background with all text removed (brush shapes stay, they are background)
  await page.addStyleTag({ content: '.qa-notext, .qa-notext * { color: transparent !important; fill-opacity: 1; } .qa-notext text, .qa-notext tspan { fill: transparent !important; }' });
  await page.evaluate(() => document.body.classList.add('qa-notext'));
  const bg = (await page.screenshot()).toString('base64');
  await page.evaluate(() => document.body.classList.remove('qa-notext'));

  // per element: ink mask (only this element's glyphs, transparent page)
  await page.addStyleTag({ content: `
    body.qa-iso, body.qa-iso .slide { background: transparent !important; }
    body.qa-iso .slide * { visibility: hidden !important; }
    body.qa-iso .slide svg.layer { display: none; }
    body.qa-iso .qa-show, body.qa-iso .qa-show * { visibility: visible !important; }
    body.qa-iso .qa-show .brush::before, body.qa-iso .qa-show.brush::before, body.qa-iso .qa-show .strike::after, body.qa-iso .qa-show.strike::after { display: none !important; }
    body.qa-iso svg:has(.qa-show) { display: block !important; visibility: visible !important; }` });
  const masks = {};
  for (const it of items) {
    await page.evaluate(i => { document.body.classList.add('qa-iso'); document.querySelector(`[data-qa="${i}"],[data-qb="${i}"]`).classList.add('qa-show'); }, it.i);
    masks[it.i] = (await page.screenshot({ omitBackground: true })).toString('base64');
    await page.evaluate(i => { document.body.classList.remove('qa-iso'); document.querySelector(`[data-qa="${i}"],[data-qb="${i}"]`).classList.remove('qa-show'); }, it.i);
  }
  // full render (to read the real glyph color)
  const full = (await page.screenshot()).toString('base64');

  const report = await page.evaluate(async ({ bg, full, masks, items, PHONE }) => {
    const decode = async b64 => {
      const img = new Image(); img.src = 'data:image/png;base64,' + b64; await img.decode();
      const c = document.createElement('canvas'); c.width = img.width; c.height = img.height;
      const x = c.getContext('2d'); x.drawImage(img, 0, 0); return x.getImageData(0, 0, c.width, c.height).data;
    };
    const lum = (r, g, b) => { const f = v => (v /= 255) <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
    const B = await decode(bg), F = await decode(full);
    const M = {}; for (const k in masks) M[k] = await decode(masks[k]);
    const W = 1080, out = { contrast: [], collisions: [] };
    for (const it of items.filter(x => x.kind === 'owner')) {
      const m = M[it.i], el = document.querySelector(`[data-qa="${it.i}"]`);
      const cs = getComputedStyle(el.closest('text') ? el : el);
      const ratios = [];
      // glyph color = the most saturated-alpha mask pixels' color in the full render
      for (let p = 0; p < m.length; p += 4) {
        if (m[p + 3] < 250) continue;               // solid glyph core only
        const tl = lum(F[p], F[p + 1], F[p + 2]), bl = lum(B[p], B[p + 1], B[p + 2]);
        ratios.push((Math.max(tl, bl) + 0.05) / (Math.min(tl, bl) + 0.05));
      }
      if (!ratios.length) continue;
      ratios.sort((a, b) => a - b);
      const p10 = ratios[Math.floor(ratios.length * 0.10)];
      const size = parseFloat(cs.fontSize), weight = parseInt(cs.fontWeight);
      const shown = size * PHONE;
      const large = shown >= 24 || (shown >= 18.66 && weight >= 700);
      const need = large ? 3 : 4.5;
      out.contrast.push({ text: it.text, size, shown: +shown.toFixed(1), weight, ratio: +p10.toFixed(2), need, pass: p10 >= need });
    }
    const blocks = items.filter(x => x.kind === 'block');
    for (let a = 0; a < blocks.length; a++) for (let b = a + 1; b < blocks.length; b++) {
      const A = blocks[a].r, Bx = blocks[b].r;
      const x0 = Math.max(0, Math.floor(Math.max(A[0], Bx[0]))), x1 = Math.min(W, Math.ceil(Math.min(A[2], Bx[2])));
      const y0 = Math.max(0, Math.floor(Math.max(A[1], Bx[1]))), y1 = Math.min(1350, Math.ceil(Math.min(A[3], Bx[3])));
      if (x0 >= x1 || y0 >= y1) continue;
      const ma = M[blocks[a].i], mb = M[blocks[b].i]; let hit = 0, near = 0;
      for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) {
        const p = (y * W + x) * 4;
        if (ma[p + 3] > 60 && mb[p + 3] > 60) hit++;
      }
      // proximity: ink of a within 6 px of ink of b
      if (!hit) {
        outer: for (let y = y0; y < y1; y += 2) for (let x = x0; x < x1; x += 2) {
          const p = (y * W + x) * 4; if (ma[p + 3] <= 60) continue;
          for (let dy = -6; dy <= 6; dy += 3) for (let dx = -6; dx <= 6; dx += 3) {
            const yy = y + dy, xx = x + dx; if (yy < 0 || yy >= 1350 || xx < 0 || xx >= W) continue;
            if (mb[(yy * W + xx) * 4 + 3] > 60) { near++; break outer; }
          }
        }
      }
      out.collisions.push({ a: blocks[a].text, b: blocks[b].text, inkOverlapPx: hit, within6px: !!near });
    }
    return out;
  }, { bg, full, masks, items, PHONE });

  const fails = report.contrast.filter(c => !c.pass);
  const real = report.collisions.filter(c => c.inkOverlapPx || c.within6px);
  console.log(`\n${f}`);
  console.log(`  contrast: ${report.contrast.length} text blocks, min ratio ${Math.min(...report.contrast.map(c => c.ratio)).toFixed(2)}, smallest on phone ${Math.min(...report.contrast.map(c => c.shown))}px`);
  for (const c of report.contrast) console.log(`    ${c.pass ? 'ok  ' : 'FAIL'} ${c.ratio.toFixed(2)} (need ${c.need}) ${c.size}px→${c.shown}px w${c.weight}  ${c.text}`);
  console.log(`  line-box intersections: ${report.collisions.length}, real glyph overlap/near-touch: ${real.length}`);
  for (const c of real) console.log(`    GLYPH ${c.inkOverlapPx ? 'OVERLAP ' + c.inkOverlapPx + 'px' : 'within 6px'}: ${c.a} × ${c.b}`);
}
await browser.close();
