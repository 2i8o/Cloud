---
name: abbas-carousel-identity
description: The approved visual identity, design system and production pipeline for every Instagram/social carousel and motion Reel made for Abbas Abdulmunem (عباس عبدالمنعم). Use whenever creating, revising, critiquing or exporting a carousel, slide set, cover, or single 4:5 post for Abbas, on any topic, so new carousels match the approved 20-20-20 carousel. Covers brand tokens (verified vs provisional), IBM Plex Sans Arabic typography and its required ligature fix, composition rules (no box/card layouts), color rhythm, curiosity-driven cover method, scientific-accuracy rules, the HTML/SVG → PNG render pipeline with pixel-level QA, 3x high-resolution export, and the review/approval workflow.
---

# Abbas Abdulmunem — Carousel Identity System

This skill fixes the carousel identity Abbas approved on the 20-20-20 carousel (cover «عيونك دزّتلك رسالة») and its motion Reel. Apply it to **every** carousel and Reel for Abbas, whatever the topic. Change the content per topic. Keep the system the same.

Pair it with `abbas-personal-operating-system` (or `abbas-work-profile`) for voice, evidence standards and brand strategy. If the user supplies `brand.ts`, `theme.ts`, `STANDARDS.md` or an official brand-lock file, those **override** the provisional values here. Update the tokens in one place (see §2) and say so.

---

## 1. Non-negotiables

1. **Canvas:** 1080 × 1350 px (4:5), RGB/sRGB, PNG. One file per slide, named `NN-slug.png`.
2. **Palette:** only the four brand colors (§2). No gradients, purple, new hues, or transparency used as a colour.
3. **Typeface:** IBM Plex Sans Arabic only, with the scoped ligature fix (§4). Never disable `rlig` globally.
4. **Copy:** natural Iraqi Arabic, rendered as real text, never drawn by an image model. Never rewrite correct wording to dodge a rendering problem; fix the rendering instead.
5. **No box-based layouts:**
   - No repeated rectangular cards, icon-and-paragraph rows, or generic infographic panels.
   - A rectangle is allowed only when it is a real object, such as a phone or a lock-screen notification.
   - Do not swap boxes for random circles or blobs. Every shape needs a purpose.
6. **Science:**
   - Wording must be no stronger than the evidence.
   - No fearmongering, no cure or guarantee claims.
   - Keep claim-to-source traceability, and carry qualifications into the slides themselves.
7. **Approval workflow:**
   - Work in a separate review copy.
   - Never commit, push or overwrite a repository until Abbas explicitly approves the visuals.
   - When asked for a review, deliver the PNGs, a contact sheet and the editable source.

## 2. Brand tokens — single source of truth

All colours live in `template/src/base.css` → `:root`. No hex values may appear in any slide file. `render.mjs` flags `HARDCODED COLOR`. SVG shapes use `style="fill:var(--navy)"`. The yellow brush reads `--yellow` through a CSS mask.

| Token | Value | Status |
|---|---|---|
| `--blue` | `#5599D9` | **Verified** (Abbas's reference, sampled from an approved cover) |
| `--navy` | `#0E2A47` | **Provisional**: approved in use, not yet checked against an official token file |
| `--yellow` | `#FFC83D` | **Provisional**: approved in use, not yet checked against an official token file |
| `--white` | `#FFFFFF` | Standard white |
| `--skin`, `--skin-shade` | `#E3AE88`, `#CB9370` | Illustration material only (e.g. a figure seen from behind), not brand colours |

Never present the provisional values as official. If official values arrive, change them in `:root` only. Tested: changing `:root` alone recolours every pixel of every slide.

### Measured contrast (WCAG, from rendered pixels)
| Pair | Ratio | Use |
|---|---|---|
| navy / white | 14.6 | any size |
| navy / yellow | 9.4 | text on the brush |
| navy ↔ blue | 4.8 | normal text OK |
| white ↔ blue | **3.0** | **large text only** |

**Mobile rule:** a 1080 px slide shows at about 390 px on a phone (×0.36). "Large" means at least 24 px displayed (≈ 67 px on canvas), or at least 18.66 px displayed and bold 700 (≈ 52 px on canvas).
- White-on-blue is for big headlines and numerals only.
- Small text on blue is navy.

## 3. Typography system

| Role | Canvas size | Weight |
|---|---|---|
| Cover headline | 128–136 | 700 |
| Slide headline | 88–112 | 700 |
| Display numerals | 160–330 | 600 (white on blue, or navy) |
| Units / sub-heads | 52–80 | 600 |
| Tip headings | 54 | 600 |
| Body / supporting | 40–48 | 500 |
| Labels (kicker, «الخطوة الأولى») | 40 | 500 |
| Sources | 26 (minimum) | 500 |
| Signature «عباس عبدالمنعم» | 30 | 600 (bottom-right, with a yellow/blue dot) |
| Pager «01 / 08» | 26 | 600 (top-left) |

- **Weights:** 700 only for headlines. Avoid bold paragraphs.
- **Line height:** body 1.5–1.6.
- **Line breaks:** break lines by meaning, using explicit `<br>`. No orphans.
- **Overcrowding:** never shrink text to fit. Cut genuinely redundant words, or recompose the slide.
- **RTL reading order:** text read first must sit right or above. Do not put an explanatory line («يعني…») to the right of the number it explains.
- **Numbers:** wrap them in `<span class="num">`, which applies LTR isolation and tabular figures.
- **Yellow brush:**
  - `.brush` marks the key word, usually once or twice per slide.
  - `.brush.full` is for text whose colour equals the background, so the glyph tops do not vanish.
  - The brush is a solid shape. Never add a translucent underline.

## 4. Required Arabic shaping fix (IBM Plex Sans Arabic 1.101)

The font's `rlig` feature contains tooth + alef-maksura ligatures:
- `تى` → glyph `uniFC74`, which reads as **ق** («حتى» → «حق»).
- `نى` → `uniFC8E`, which reads as **ف** («معنى» → «معفى»).

`rlig` also builds lam-alef (لا), so it must **not** be turned off globally.

`template/src/shaping.js` (include it in every slide: `<script src="shaping.js"></script>`) wraps only the affected words (a tooth letter ب ت ث ن ي ئ پ followed by ى) in `.rlig-off`. `render.mjs` verifies that no affected word is left unwrapped and that no lam-alef is wrapped.

## 5. Colour rhythm & composition

- **Backgrounds:**
  - Blue is the primary background on most slides.
  - White gives quiet "breathing" slides.
  - Navy is for structure: layered planes, an iris, an eyelid, text.
  - Avoid fully dark slides. At most one, and only with a reason.
- **Rhythm:** alternate dense and quiet slides, e.g. quiet → dense → medium → medium → quiet → dense → medium → quiet.
- **Depth:**
  - Use layered **solid** planes, such as a navy offset disc behind a clock, a sloped navy "night" plane, or a white curved "landing".
  - No translucency, halos, or gradients.
- **Composition:**
  - Free-standing typography, expressive numerals, purposeful asymmetry, generous negative space.
  - One dominant focal point per slide.
- **Visual thread:** carry one meaningful motif through the series. In 20-20-20 it is eye → time → distance → rest: an eye icon in the cover notification, a closed eye on the tips slide, an eyelid closing over the final question. Do not overuse the motif.
- **Objects must be physically coherent:**
  - Clock hands at real times (10:20, not impossible angles).
  - Perspective with one vanishing point.
  - Lashes that start exactly on the lid curve.
  - Phones with a notch and correct proportions.
- **Signature and pager:** on every slide, in the same positions.

## 6. The cover: curiosity first, clarity second, decoration last

Do not make a cover that only announces the topic, such as a giant literal icon plus "your eyes need rest". Method:
1. **Develop three genuinely different concepts**, e.g. a familiar phone moment interrupted, an oversized typographic riddle, a visual contradiction. For each, document: the psychological hook, the visual metaphor, the headline, why the viewer would swipe, and the scientific/interpretive risk.
2. **Score them** on self-relevance, curiosity, instant comprehension, brand fit, phone/thumbnail readability, and link to the inner slides. These are designer judgements, never "proven to go viral".
3. **Review each concept** at full size, at phone size (≈390 px), and at grid-thumbnail size (≈124 px).
4. **Write the final cover from these parts:**
   - Kicker: an audience line, e.g. «طلاب السادس وجماعة الموبايل».
   - One headline with a brush on the key word.
   - A **quiet secondary label naming the topic**, e.g. «قاعدة 20-20-20» at 46 px, navy, 500. It must not compete with the headline.
   - One focal visual that withholds the answer.
5. **Avoid on the cover:** fear, urgency, judgemental cues (e.g. a 2:47 a.m. timestamp), and app/brand look-alikes. Late-night jokes belong inside the story, not on the cover.

**Approved example:** «عيونك دزّتلك رسالة». The phone's lock screen shows a neutral 5:40 and one white notification:
- «عيونك · هسه»
- «صارلك 20 دقيقة تباوع للشاشة»
- «عندي طلب صغير… ياخذ 20 ثانية بس»

See `references/example-20-20-20/`.

## 7. Content & science rules for slides

- One core idea per slide. Number the steps («الخطوة الأولى»).
- **Every claim must be traceable to a source you have actually read.** If a claim is not in the sources (e.g. "screens reduce blinking" when only "blink frequently" is sourced), rephrase or drop it.
- **Put qualifications on the slide,** integrated into the composition. For example, 06 says «للأمانة العلمية: … تذكير عملي … مو علاج مثبت … والأدلة … محدودة».
- **Put a short source line on the slide** («AOA · Johnson & Rosenfield, Optom Vis Sci 2023»), and the full reference in the documentation.
- **Mark draft copy as draft** until Abbas approves it.

## 8. Production pipeline

```
template/
  src/base.css        # tokens, @font-face, brush, .rlig-off, signature/pager
  src/shaping.js      # scoped ligature fix
  src/NN-slug.html    # one editable HTML/SVG file per slide
  fonts/              # IBM Plex Sans Arabic woff2 + OFL licence
  render.mjs          # → export/NN-slug.png + contact-sheet.png + basic checks
  qa.mjs              # pixel-level QA
scripts/export-hires.cjs   # 3× export (3240 × 4050) for archiving/print
```

1. Copy `template/` to a new working folder. Write each slide as `src/NN-slug.html`, linking `base.css` and ending with `<script src="shaping.js"></script>`. The 8 files in `references/example-20-20-20/src/` are the reference implementation; to render them, copy them into `template/src/`.
2. Run `node render.mjs` to render all slides plus the contact sheet, or `node render.mjs 03` for one slide. It checks: font loaded, text clipping, unwrapped ligature words, lam-alef inside a wrapper, hard-coded colours, and line-box intersections (a hint only).
3. Run `node qa.mjs`. It isolates each text's ink and reports **real glyph overlap/near-touch (<6 px)**, plus **WCAG contrast measured per glyph pixel** against the actual rendered background, judged at phone size. Fix every FAIL, except a deliberate effect (e.g. a strike line), which must be named.
4. Inspect every slide at full resolution **and** the contact sheet. A render that succeeds is not proof of quality.
5. For a high-resolution export, run `node scripts/export-hires.cjs <src-dir> <out-dir> [scale=3]`. This re-renders from source (not an upscale). Note for Abbas: Instagram downsizes carousels to 1080 px wide, so high resolution is for archiving and print.

Playwright/Chromium is required. `render.mjs` falls back to `/opt/node-tools/node_modules/playwright`. On Windows use `npx.cmd playwright` if PowerShell blocks scripts.

## 9. Motion / Reels (approved on the 20-20-20 Reel)

Reference implementation: `references/example-20-20-20/reel/` (`reel.html`, `reel.js`, `audio.py`, `render_reel.cjs`, `encode.sh`). Reproduction commands are in `references/example-20-20-20/ART-DIRECTION.md` §6.

1. **Native 9:16 (1080×1920, 30 fps).** Never stretch 4:5 slides. Recompose every scene; real objects keep real proportions (phone width:height ≈ 0.48) and are cropped by the frame edge.
2. **Reels safe zone for text:**
   - Top ≥ 250 px.
   - Bottom ≤ 1500 px.
   - Right edge ≤ 940 px below y ≈ 1080, to stay clear of the action column.
   - Art may bleed to every edge.
3. **Signature:** in one fixed place for the whole Reel (top-left: top 250, left 88).
4. **Text never scales or pulses.** Scaling re-rasterises glyphs every frame, so the text visibly shimmers.
   - Camera zoom (about 6%, smootherstep) applies to SVG art and background dots only, with the origin on each scene's focal graphic.
   - Text appears word by word, in reading order. Never letter by letter, because that breaks Arabic joining.
5. **Render** at 2× (2160×3840), then downscale with lanczos. Verify stillness: the mean per-pixel change of resting text between consecutive frames should be ≈ 0.
6. **Floating dots:**
   - Solid brand colours, no glow or gradients.
   - Periodic motion, so the loop is seamless.
   - **Kept clear of all text**, including their drift range, because a dot near Arabic letters reads as a letter dot.
7. **Algorithm-aware structure.** Per Instagram's head, the top signals are watch time, likes per reach and sends per reach; sends matter most for non-followers.
   - The first frame already carries the hook.
   - Pace for a quick read: entrance times and word stagger ×1.2, 0.9 s scene wipes, every scene holds its full text ≥ 1.7 s (measured: `ends` in the cue file), so about 34 s; the trade-off is a lower completion rate. Seamless loop: the last frame equals the first, and the music is an integer number of bars (14 @ 100 BPM) ending on V→I.
   - "Send it to a friend" (دزّه لصديقك) is the lead CTA.
   - On-screen text throughout, since much viewing is muted.
   - Never trade scientific accuracy for reach. Keep the qualification slide.
8. **Sound:** original synthesis or properly licensed tracks only, with no generative-AI audio. SFX are tuned to the music key and placed from the timeline cue list.
   - Mix: each SFX +2…+7 dB above the music at its hit; the music ducks about 4 dB under SFX.
   - Master: −16.5 LUFS, true peak ≤ −1.5 dBTP. Measure the balance; the author cannot listen.
9. **Delivery:** H.264 High, BT.709, AAC 48 kHz. `encode.sh` strips metadata, SEI and the encoder name. Verify the box tree: no XMP/C2PA. Report honestly that platform labelling cannot be guaranteed.

## 10. Acceptance checklist (every slide)

- [ ] Exactly 1080 × 1350, sRGB PNG; editable source kept.
- [ ] Only brand tokens; provisional values documented as provisional.
- [ ] `qa.mjs`: 0 glyph overlaps; every text passes its contrast threshold (or a named deliberate exception).
- [ ] Arabic shaping correct, ligature fix active, RTL reading order logical, no orphans, no clipping.
- [ ] No box/card layout; one focal point; every shape has a purpose.
- [ ] Every claim sourced and no stronger than the evidence; qualifications visible.
- [ ] Series reviewed together on the contact sheet: colour rhythm, density rhythm, motif continuity.
- [ ] Nothing merged, committed or pushed without Abbas's explicit approval.
