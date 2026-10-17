# Color, Compositing, Finishing, and Delivery

Tags: **[CF]** Casey Faris Resolve course transcript (selected sections read: color management, primary wheels, export). **[Web]** rendering/output guide (MediaScaleUp) - secondary. **[Known]** standard practice, verify on your tools. **[Synth]** this skill's reasoning.

## 1. Order of operations

1. Lock picture (cuts) and timing first; color and polish never fix a structure problem.
2. Technical normalize: input color space / color management set correctly. [CF: "color managed" timelines transform log footage with the right input color space; mismatched interpretation is the common mistake]
3. Primary balance: exposure, contrast, white balance, so skin/neutral objects read correctly.
4. Look: one deliberate look applied consistently.
5. Secondary fixes: isolate skin, sky, or a brand color only if needed.
6. Unify: grain/blur/contrast over composited elements.
7. Brand/readability check of graphics after the grade.

## 2. Primary corrections (what each control does)

[CF] **Lift / Gamma / Gain** act mostly on shadows / midtones / highlights; **Offset** shifts the whole image. Push a color into one range (e.g. warm only the highlights with Gain) to tint without flooding the whole frame. Master slider = brightness of that range. [Known]: judge on scopes (waveform / vectorscope), not only the eye; calibrated displays matter.

Decision rule [Synth]: grade toward the **story's emotion and the subject's clarity**, not a trendy preset. For educational content the first job is to make the subject legible and color-true (objects look like what they are).

## 3. Matching shots and graphics

- Match exposure and white balance across shots in a sequence before any "look."
- Composited CG/graphics: match black level, shadow color, sharpness, and grain; otherwise they float. [Known]
- Do not over-sharpen: halos read as cheap and compress poorly.
- Gradients and banding: gradients can band after compression; prefer flat fills, subtle noise, or grain when brand rules restrict gradients.

## 4. Delivery planning

Derive in this order [Web, CF]:
1. **Mastering file**: high-quality intermediate (ProRes / DNxHR, or lossless image sequence). Keep it.
2. **Delivery files** derived from the master: platform codec/container (often H.264 MP4, sometimes H.265), the platform's resolution and frame rate.
3. Set resolution, fps, color space from the **spec**, not application defaults. Short vertical form default: 1080x1920 at the project's fps (commonly 30; confirm per project).
4. Transparent renders need a codec/channel that includes alpha (ProRes 4444, PNG/TIFF/EXR sequences); H.264/most HEVC/ProRes 422 carry none. [Web]
5. Test-render a short range at final settings before the full render. [Web]
6. Never overwrite originals or earlier finals; use versioned file names (`name_v03.mp4`).

Codec tradeoff [CF]: you can have small, great-looking, or easy-to-edit - rarely all three. ProRes = quality + easy playback, large; H.265 = small + good, harder to play/edit; H.264 = small + easy playback, less quality at the same size.

## 5. Captions and on-screen text at delivery

- Captions/hard-coded text inside safe areas of the target platform.
- Verify sync to speech; check that the reading time suffices (`pacing-and-continuity.md` section 3).
- Burned-in captions are part of picture: check against compression artifacts on a phone.
- Arabic: check right-to-left order, joined letters, numerals, and punctuation in the final export.

## 6. Final checks

Run `python scripts/video_qc.py final.mp4 --expect-width 1080 --expect-height 1920 --expect-fps 30` for resolution, fps, duration, loudness, silence/black/freeze detection. Then do the human pass in `quality-control.md`.
