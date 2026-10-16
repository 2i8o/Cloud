// Renders src/*.html → export/*.png at 1080×1350 and builds a contact sheet.
// Usage: node render.mjs [slide-prefix ...]
import { createRequire } from 'module';
import { readdirSync, mkdirSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const require = createRequire(import.meta.url);
let playwright;
try { playwright = require('playwright'); } catch { playwright = require('/opt/node-tools/node_modules/playwright'); }

const root = dirname(fileURLToPath(import.meta.url));
const src = resolve(root, 'src');
const out = resolve(root, 'export');
mkdirSync(out, { recursive: true });

const only = process.argv.slice(2);
const slides = readdirSync(src).filter(f => /^\d\d-.*\.html$/.test(f)).sort()
  .filter(f => !only.length || only.some(p => f.startsWith(p)));

const browser = await playwright.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
for (const f of slides) {
  await page.goto('file://' + resolve(src, f));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForLoadState('networkidle');
  // QA: flag any text element that leaves the canvas
  const overflow = await page.evaluate(() => [...document.querySelectorAll('.slide *')]
    .filter(e => e.childNodes.length && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
    .map(e => ({ t: e.textContent.trim().slice(0, 24), r: e.getBoundingClientRect() }))
    .filter(({ r }) => r.left < 0 || r.top < 0 || r.right > 1080 || r.bottom > 1350)
    .map(({ t, r }) => `${t} [${Math.round(r.left)},${Math.round(r.top)},${Math.round(r.right)},${Math.round(r.bottom)}]`));
  const fontsOk = await page.evaluate(() => document.fonts.check('700 40px "Plex Ar"', 'ع'));
  await page.screenshot({ path: resolve(out, f.replace('.html', '.png')) });
  console.log(f, fontsOk ? 'font ok' : 'FONT MISSING', overflow.length ? 'OVERFLOW: ' + overflow.join(' | ') : '');
}

if (!only.length) {
  const imgs = slides.map(f => `<img src="file://${resolve(out, f.replace('.html', '.png'))}">`).join('');
  await page.setViewportSize({ width: 2240, height: 1460 });
  await page.setContent(`<style>body{margin:0;background:#e9edf2;display:grid;grid-template-columns:repeat(4,1fr);gap:24px;padding:24px}img{width:100%;display:block}</style>${imgs}`);
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: resolve(out, 'contact-sheet.png'), fullPage: true });
  console.log('contact-sheet.png');
}
await browser.close();
