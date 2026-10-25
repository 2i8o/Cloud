// Reel timeline (1080×1920, 30 fps, seamless loop). window.render(t) draws the exact state at time t.
// Picture, floating dots, camera and every sound cue come from this one file.
(() => {
  const FPS = 30, END = 21.6, WIPE = 0.55, LOOP_AT = 21.0;
  const START = [0, 3.3, 6.3, 8.6, 10.9, 13.2, 17.8];
  // art-zoom origin per scene; null = no art zoom (S1/S2 phones carry text, S6 is text-led)
  const ZOOM = [null, null, '676px 984px', '300px 1000px', '540px 960px', null, '540px 420px'];

  const ease = {
    out: p => 1 - Math.pow(1 - p, 3),
    out5: p => 1 - Math.pow(1 - p, 5),
    inOut: p => p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2,
    soft: p => { const c = 1.06, k = c + 1; return 1 + k * Math.pow(p - 1, 3) + c * Math.pow(p - 1, 2); },
    lin: p => p,
  };
  const clamp = p => Math.max(0, Math.min(1, p));
  const $$ = s => [...document.querySelectorAll(s)];
  const NS = 'http://www.w3.org/2000/svg';

  // ── build: timer marks for S5 (20 marks = 20 seconds) ──
  const ticks = document.querySelector('#s5 .a-ticks');
  for (let i = 0; i < 20; i++) {
    const a = i * 18 * Math.PI / 180, cx = 540, cy = 960, r1 = 300, r2 = 346;
    const l = document.createElementNS(NS, 'line');
    l.setAttribute('x1', (cx + r1 * Math.sin(a)).toFixed(1)); l.setAttribute('y1', (cy - r1 * Math.cos(a)).toFixed(1));
    l.setAttribute('x2', (cx + r2 * Math.sin(a)).toFixed(1)); l.setAttribute('y2', (cy - r2 * Math.cos(a)).toFixed(1));
    l.setAttribute('stroke-width', 12); l.setAttribute('stroke-linecap', 'round');
    l.setAttribute('class', `tk tk${i}`); l.style.stroke = 'var(--blue)';
    ticks.append(l);
  }

  // ── build: floating dots (solid brand colours, no glow); motion is periodic over END so the loop is seamless ──
  const SCHEME = { blue: ['var(--white)', 'var(--white)', 'var(--white)', 'var(--yellow)'],
                   sky: ['var(--white)', 'var(--white)', 'var(--yellow)'],
                   white: ['var(--blue)', 'var(--blue)', 'var(--blue)', 'var(--yellow)'] };
  const dots = [];
  for (const layer of $$('.dots')) {
    let s = +layer.dataset.seed * 9301 + 49297;
    const rnd = () => (s = (s * 9301 + 49297) % 233280) / 233280;
    const cols = SCHEME[layer.dataset.scheme];
    const yMax = layer.dataset.scheme === 'sky' ? 990 : 1880;
    for (let i = 0; i < 16; i++) {
      const d = document.createElement('i');
      const r = 4 + rnd() * 7;
      d.style.width = d.style.height = (r * 2) + 'px';
      d.style.background = cols[Math.floor(rnd() * cols.length)];
      layer.append(d);
      dots.push({ el: d, layer, rnd, yMax, x: 30 + rnd() * 1020, y: 120 + rnd() * (yMax - 120), r,
                  ax: 10 + rnd() * 18, ay: 18 + rnd() * 30, k: 1 + Math.floor(rnd() * 3), ph: rnd() * 6.283, ph2: rnd() * 6.283 });
    }
  }

  // ── timeline ──
  const tracks = [], cues = [];
  const add = (scene, sel, at, dur, fx, o = {}) => {
    const T = START[scene - 1] + at;
    tracks.push({ scene, sel: `#s${scene} ${sel}`, at: T, dur, fx, o, els: null });
    if (o.sfx) cues.push({ t: +(T + (o.sfxAt || 0)).toFixed(3), name: o.sfx, gain: o.gain ?? 1 });
  };
  const cue = (t, name, gain = 1) => cues.push({ t: +t.toFixed(3), name, gain });

  const splitWords = el => {
    if (el.dataset.split) return; el.dataset.split = 1;
    for (const node of [...el.childNodes]) {
      if (node.nodeType === 3) {
        const frag = document.createDocumentFragment();
        for (const p of node.nodeValue.split(/(\s+)/)) {
          if (!p) continue;
          if (/^\s+$/.test(p)) frag.append(p);
          else { const w = document.createElement('span'); w.className = 'ww'; w.textContent = p; frag.append(w); }
        }
        node.replaceWith(frag);
      } else if (node.nodeType === 1 && node.tagName !== 'BR') node.classList.add('ww');
    }
  };
  const FX = {
    rise: (el, e, o) => { el.style.opacity = e; el.style.transform = `translateY(${(1 - e) * (o.dy ?? 34)}px)`; },
    fade: (el, e) => { el.style.opacity = e; },
    slideY: (el, e, o) => { el.style.transform = `translateY(${(1 - e) * o.dy}px)`; },
    scale: (el, e, o) => { el.style.transformOrigin = o.origin || 'center'; el.style.transform = `scale(${(o.from ?? .85) + (1 - (o.from ?? .85)) * e})`; if (o.fade !== false) el.style.opacity = Math.min(1, e * 1.6); },
    pulse: (el, e, o) => { el.style.transformOrigin = 'center'; el.style.transform = `scale(${1 + (o.amp ?? .05) * Math.sin(Math.PI * e)})`; },
    brush: (el, e) => el.style.setProperty('--b', e),
    strike: (el, e) => el.style.setProperty('--s', e),
    count: (el, e, o) => { el.textContent = String(Math.round(e * o.to)); },
    fn: (el, e, o) => o.fn(el, e),
  };

  // S1 hook — headline + phone are already on frame 0; the message arrives at 0.35 s
  add(1, '.a-note', 0.35, .5, 'rise', { dy: -46, ease: 'soft', sfx: 'ping', gain: .9 });
  add(1, '.note', 0.35, .5, 'rise', { dy: -46, ease: 'soft' });
  add(1, '.note .d .brush', 0.95, .45, 'brush');

  // S2 problem
  add(2, '.a-night', 0.0, .8, 'slideY', { dy: 820, ease: 'out5', sfx: 'whoosh', gain: .5 });
  add(2, '.a-phone', 0.2, .9, 'slideY', { dy: 900, ease: 'out5' });
  add(2, '.was', 0.15, .45, 'rise');
  add(2, '.was .strike', 0.55, .4, 'strike', { ease: 'inOut', sfx: 'swipe', gain: .55 });
  add(2, '.now', 0.8, .5, 'words', { stagger: .15 });
  add(2, '.now .brush', 0.95, .45, 'brush');
  add(2, '.why', 1.25, .45, 'words', { stagger: .05 });
  add(2, '.tag', 1.7, .45, 'rise');
  add(2, '.sym', 1.9, .45, 'words', { stagger: .07 });

  // S3 twenty minutes
  add(3, '.lbl', 0.05, .45, 'rise');
  add(3, '.head', 0.1, .5, 'words', { stagger: .1 });
  add(3, '.two', 0.15, .7, 'rise', { dy: 60 });
  add(3, '.a-clock', 0.2, .7, 'scale', { from: .75, origin: '676px 984px', ease: 'out5' });
  add(3, '.a-sector', 0.6, 1.0, 'fn', { ease: 'inOut', fn: (el, e) => {
    const a = e * 120 * Math.PI / 180, r = 256;
    el.setAttribute('d', e <= 0 ? 'M0 0 Z' : `M0 0 L0 ${-r} A${r} ${r} 0 0 1 ${(r * Math.sin(a)).toFixed(2)} ${(-r * Math.cos(a)).toFixed(2)} Z`);
  } });
  add(3, '.a-min', 0.6, 1.0, 'fn', { ease: 'inOut', fn: (el, e) => { el.style.transformOrigin = '0px 0px'; el.style.transform = `rotate(${e * 120 - 120}deg)`; } });
  for (let i = 0; i < 20; i++) cue(START[2] + 0.6 + 1.0 * (i + .5) / 20, 'tick', .45);
  add(3, '.note', 1.3, .45, 'words', { stagger: .04 });
  add(3, '.note .brush', 1.75, .4, 'brush');

  // S4 twenty feet
  add(4, '.a-horizon', 0.05, .6, 'scale', { from: 0, fade: false, origin: '540px 1000px', ease: 'inOut' });
  add(4, '.a-road', 0.15, .7, 'fn', { ease: 'out5', fn: (el, e) => { el.style.transformOrigin = '300px 1000px'; el.style.transform = `scale(${.02 + .98 * e})`; } });
  add(4, '.a-dash path', 0.45, .5, 'fade');
  add(4, '.a-person', 0.1, .8, 'slideY', { dy: 640, ease: 'out5' });
  add(4, '.a-tree', 0.6, .5, 'scale', { from: 0, origin: '220px 1000px', ease: 'soft', sfx: 'pop', gain: .5 });
  add(4, '.a-sight', 0.85, .7, 'fn', { ease: 'inOut', fn: (el, e) => {
    el.setAttribute('d', `M700 1236 L${(700 - 438 * e).toFixed(1)} ${(1236 - 308 * e).toFixed(1)}`); el.style.opacity = e > 0 ? 1 : 0;
  } });
  add(4, '.a-sightend', 1.55, .3, 'scale', { from: 0, origin: '262px 928px', sfx: 'pop', gain: .4 });
  add(4, '.lbl', 0.05, .45, 'rise');
  add(4, '.head', 0.1, .5, 'words', { stagger: .09 });
  add(4, '.big', 0.45, .45, 'rise');
  add(4, '.big .n', 0.45, .7, 'count', { to: 20 });
  add(4, '.eq', 1.0, .45, 'words', { stagger: .06 });
  add(4, '.eq .brush', 1.3, .4, 'brush');
  add(4, '.ex', 1.4, .45, 'words', { stagger: .04 });

  // S5 twenty seconds (quiet white scene)
  add(5, '.lbl', 0.05, .45, 'rise');
  add(5, '.head', 0.1, .5, 'words', { stagger: .12 });
  add(5, '.tk', 0.05, .4, 'fade');
  for (let i = 0; i < 20; i++) {
    const at = 0.45 + i * 0.075;
    if (i < 13) { add(5, `.tk${i}`, at, .1, 'fn', { fn: (el, e) => { el.style.stroke = e >= .5 ? 'var(--navy)' : 'var(--blue)'; } }); cue(START[4] + at + .05, 'click', .5); }
    else if (i === 13) { add(5, `.tk${i}`, at, .2, 'fn', { fn: (el, e) => { el.style.stroke = e >= .3 ? 'var(--yellow)' : 'var(--blue)'; el.style.strokeWidth = e >= .3 ? 16 : 12; } }); cue(START[4] + at + .06, 'accent', .7); }
  }
  add(5, '.center .n', 0.2, .6, 'scale', { from: .8 });
  add(5, '.center .u', 0.4, .45, 'rise', { dy: 16 });
  add(5, '.center .least', 1.5, .35, 'rise', { dy: 12 });
  add(5, '.center .least .brush', 1.6, .4, 'brush');
  add(5, '.note', 1.6, .45, 'words', { stagger: .04 });

  // S6 the full rule (longest hold: the save-worthy frame)
  add(6, '.head', 0.05, .5, 'words', { stagger: .1 });
  add(6, '.head .brush', 0.5, .4, 'brush');
  add(6, '.r1', 0.6, .5, 'rise', { dy: 40, sfx: 'pop', gain: .35 });
  add(6, '.r2', 0.85, .5, 'rise', { dy: 40, sfx: 'pop', gain: .35 });
  add(6, '.r3', 1.1, .5, 'rise', { dy: 40, sfx: 'pop', gain: .35 });
  add(6, '.a-land', 1.4, .7, 'slideY', { dy: 820, ease: 'out5', sfx: 'whoosh', gain: .4 });
  add(6, '.caveat', 1.7, .45, 'words', { stagger: .035 });
  add(6, '.src', 2.6, .45, 'fade');

  // S7 call to action — the eyelid closes over the question; "send it" leads
  add(7, '.a-lid', 0.0, .9, 'slideY', { dy: -1250, ease: 'inOut', sfx: 'lid', sfxAt: .5, gain: .6 });
  add(7, '.a-lashes', 0.8, .4, 'scale', { from: 0, origin: '540px 1000px' });
  add(7, '.kick', 0.85, .45, 'rise');
  add(7, '.q', 0.95, .55, 'words', { stagger: .09 });
  add(7, '.cta', 1.6, .5, 'words', { stagger: .15 });
  add(7, '.cta .brush', 1.75, .45, 'brush', { sfx: 'chime', gain: .6 });
  add(7, '.cta2', 2.0, .45, 'words', { stagger: .05 });

  // scene wipe whooshes (soft) + the eye re-opening into frame 0
  for (const s of [3, 4, 5]) cue(START[s - 1] + .03, 'whoosh', .28);
  cue(LOOP_AT + .05, 'whoosh', .3);

  // ── engine ──
  let ready = false;
  // Arabic: a stray dot near letters reads as a letter dot (نقطة) — keep every dot clear of all text,
  // including its full drift range and the camera push-in.
  const placeDots = () => {
    for (const d of dots) {
      const scene = d.layer.closest('.scene');
      scene.style.display = 'block';
      const zones = [...scene.querySelectorAll('.abs, .mast')].map(e => e.getBoundingClientRect());
      const pad = 44 + d.r + Math.max(d.ax, d.ay);
      const clear = (x, y) => zones.every(z => x < z.left - pad || x > z.right + pad || y < z.top - pad || y > z.bottom + pad);
      let ok = clear(d.x, d.y);
      for (let k = 0; k < 400 && !ok; k++) { d.x = 30 + d.rnd() * 1020; d.y = 120 + d.rnd() * (d.yMax - 120); ok = clear(d.x, d.y); }
      if (!ok) d.el.style.display = 'none';
      scene.style.display = '';
    }
  };
  const init = () => { placeDots(); for (const tr of tracks) { tr.els = $$(tr.sel); if (!tr.els.length) console.warn('no match', tr.sel); if (tr.fx === 'words') tr.els.forEach(splitWords); } ready = true; };

  window.render = t => {
    if (!ready) init();
    const loop = t >= LOOP_AT;
    $$('.scene').forEach((sc, i) => {
      const s0 = START[i], next = START[i + 1];
      let visible = t >= s0 && !(next !== undefined && t >= next + WIPE);
      let clip = 'none', ty = 0;
      if (i > 0 && t < s0 + WIPE) { const p = ease.inOut(clamp((t - s0) / WIPE)); clip = `inset(${((1 - p) * 100).toFixed(3)}% 0 0 0)`; }
      if (i === 0 && loop) visible = true;                                   // frame-0 state waits underneath
      if (i === START.length - 1 && loop) ty = -1920 * ease.inOut(clamp((t - LOOP_AT) / (END - LOOP_AT)));  // eye opens upward
      sc.style.display = visible ? 'block' : 'none';
      sc.style.zIndex = i + 1;
      sc.style.clipPath = clip;
      sc.style.transform = ty ? `translateY(${ty.toFixed(2)}px)` : '';
      // slow camera push-in across the scene's life; scene 1 restarts at 1.0 for the loop
      const life = (next !== undefined ? next + WIPE : END) - s0;
      const lt = (i === 0 && loop) ? 0 : clamp((t - s0) / life);
      // Camera: the ART zooms, the TEXT never does (scaling text re-rasterises glyphs every frame → shimmer).
      // Smootherstep so the push starts and settles without a jolt; origin = each scene's focal graphic.
      const sm = lt * lt * lt * (lt * (6 * lt - 15) + 10);
      const art = sc.querySelector('.cam > svg.layer');
      if (ZOOM[i]) { art.style.transformOrigin = ZOOM[i]; art.style.transform = `scale(${(1 + .06 * sm).toFixed(5)})`; }
      sc.querySelector('.dots').style.transform = `scale(${(1 + .08 * sm).toFixed(5)})`;
    });
    // dots: periodic in END → identical at t=0 and t=END
    const tl = loop ? 0 : t;
    for (const d of dots) {
      const w = 2 * Math.PI * d.k / END;
      const tt = d.layer.closest('#s1') ? tl : t;
      const x = d.x + d.ax * Math.sin(w * tt + d.ph), y = d.y + d.ay * Math.sin(w * tt * .5 * 2 + d.ph2);
      const s = 1 + .18 * Math.sin(w * tt + d.ph2);
      d.el.style.transform = `translate(${(x - d.r).toFixed(2)}px, ${(y - d.r).toFixed(2)}px) scale(${s.toFixed(3)})`;
    }
    for (const tr of tracks) {
      const tt = (tr.scene === 1 && loop) ? 0 : t;                          // scene 1 returns to its frame-0 state
      const ez = ease[tr.o.ease || 'out'];
      if (tr.fx === 'words') {
        for (const el of tr.els) [...el.querySelectorAll(':scope > .ww')].forEach((w, k) => {
          const e = ez(clamp((tt - tr.at - k * (tr.o.stagger ?? .08)) / tr.dur));
          w.style.opacity = e; w.style.transform = `translateY(${(1 - e) * (tr.o.dy ?? 30)}px)`;
        });
        continue;
      }
      // a second track on the same element (pulse after brush) only acts once it has started
      if (tr.fx === 'pulse' && tt < tr.at) continue;
      const e = ez(clamp((tt - tr.at) / tr.dur));
      for (const el of tr.els) FX[tr.fx](el, e, tr.o);
    }
  };
  window.TIMELINE = { FPS, END, START, WIPE, LOOP_AT, cues: cues.sort((a, b) => a.t - b.t) };
})();
