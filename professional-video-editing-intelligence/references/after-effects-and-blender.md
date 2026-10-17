# After Effects, Blender, and Tool Integration

Tags: **[BM-vid]** Ben Marriott transcripts (60-minute AE basics read; 10-minute excerpt read). **[CF]** Casey Faris Resolve course (transcript read, selected sections). **[Web]** third-party web material (Blender Stack Exchange, rendering guides); verify against your installed version. **[Known]** widely documented behaviour of the tool; not from the listed videos - verify on the installed version. **[Synth]** this skill's reasoning.

## 1. Capability probe (do first; never assume control)

Claude cannot operate After Effects, Blender, or Resolve's GUI unless a verified integration exists. Probe instead:

```
# Windows PowerShell
Get-Command ffmpeg, ffprobe, blender, python -ErrorAction SilentlyContinue
Get-ChildItem "C:\Program Files\Adobe" -Directory          # look for "Adobe After Effects <year>"
Get-ChildItem "C:\Program Files\Adobe\Adobe After Effects*\Support Files\aerender.exe"
Get-ChildItem "C:\Program Files\Blackmagic Design\DaVinci Resolve"
# macOS/Linux
which ffmpeg ffprobe blender python3
```

Report what is found. Then pick a *supported* method:

| Goal | Supported method | Needs |
|---|---|---|
| Blender scene creation / batch render | `blender -b scene.blend --python script.py` and CLI flags [Known] | Blender installed |
| After Effects automation | ExtendScript `.jsx` run from AE (File > Scripts) or `afterfx -r script.jsx`; `aerender` for headless render [Known] | AE installed; user runs it unless a verified tool is present |
| Resolve automation | Resolve's scripting API (Python/Lua) in Studio / scripting-enabled builds [Known, verify] | Resolve + scripting enabled |
| Encode/convert/measure | `ffmpeg`, `ffprobe`, `scripts/*.py` | ffmpeg on PATH |
| Anything else | Write an exact click-path plan the user can follow | - |

If any MCP/plugin for these apps appears in the session, inspect its tool list and test with a harmless read-only call before relying on it.

## 2. Which tool for which job

| Need | Use | Why |
|---|---|---|
| Typography, shapes, UI/infographic motion, masks, transitions | **After Effects** (or equivalent 2D) | Fast iteration on 2D animation; precomps; expressions |
| Physically-accurate objects, refraction, glass, real 3D camera moves, parallax | **Blender** (Cycles for accuracy; EEVEE for speed) | Real geometry and physically-based light (set IOR for glass: ~1.33 water, ~1.5 common glass) |
| Cutting, rhythm, audio, color on footage | NLE (Resolve / Premiere / etc.) | Timeline workflow |
| Batch conversions, loudness/shot analysis | ffmpeg + scripts | Reproducible |
| Both fast 2D and one 3D hero object | Blender render -> AE comp | Don't build full 3D if one rendered element suffices |

**Faux-3D rule** [Synth]: use AE 2.5D (layers in 3D space with a camera) for parallax and simple depth; go to Blender only when you need correct reflection/refraction, real object rotation with accurate perspective, or modeling that must stay consistent from many angles.

## 3. After Effects practice

From the 60-minute fundamentals transcript and the 10-minute excerpt [BM-vid]:
- **Organize first:** rename layers, color-label them, put assets in folders. "Having a clear and organized project... you'll be everyone's favorite person to work with."
- **Animate with keyframes, then ease them** (select -> F9 Easy Ease), then **retime** (a pop that is too slow feels floaty).
- **Offset** related layers by a few frames for flow.
- **Precomp** to reuse animations across compositions (changes in the precomp propagate to every instance).
- Animate multiple transform properties together (position, scale, rotation) for a more interesting entrance; reveal only keyframed properties with `U`.
- Texture "looping" via a few short frames of different texture crops (the demo uses 4-frame instances) gives a hand-made feel; unify with blending modes and adjustment layers.
- Render: AE render queue -> a high-quality intermediate (ProRes 422 HQ in the demo) -> compress to H.264 via Media Encoder for web; the high-quality file is much larger (the demo: 10 s = ~200 MB vs ~12 MB). [BM-vid]

Principles layer on top of this (see `motion-design.md`): purpose test, easing, timing, hierarchy, restraint. The *videos themselves* teach tool operation; the principle content comes from the syllabus and the other cited sources.

## 4. Blender -> After Effects pipeline

**Rules** [Web, Known]
1. After Effects does not import Blender meshes natively; render from Blender and import the images/video. Render a **transparent image sequence** (RGBA) or a multilayer **OpenEXR** sequence.
2. Render **image sequences, not video**, so a crash resumes from the last good frame. Encode afterwards.
3. Use `film_transparent = True` and RGBA when you need an alpha channel.
4. **Glow/light effects and PNG alpha:** PNG stores unassociated alpha; glow pixels with near-zero alpha lose color. Options: use OpenEXR (associated alpha, linear), or render the glow on black and composite with an **Add** blend mode. [Web]
5. Linear EXR needs correct color management in AE (set project color space; interpret footage consistently). Mismatched interpretation is the usual cause of "washed out" or "too dark" renders. [Web]
6. Match **frame rate, resolution, and aspect ratio** to the destination *before* rendering; render a 2-second test range at full settings before committing hours. [Web]
7. Passes for control (diffuse, shadow, AO, depth/mist, cryptomatte) let you grade and blur in AE without re-rendering. [Web]
8. Blender's Python API changes by version (e.g. render-output media-type setting and compositor node-group APIs changed in 5.0 per one source); check `blender --version` and the API before running scripts. [Web]

**Minimal CLI examples** [Known; adjust paths]

```
blender -b scene.blend -E CYCLES -s 1 -e 120 -o //renders/lens_#### -F PNG -a
blender -b --factory-startup --python make_lens.py --python-exit-code 1
ffmpeg -framerate 30 -i renders/lens_%04d.png -c:v prores_ks -profile:v 4 -pix_fmt yuva444p10le lens_alpha.mov
```
(ProRes 4444 with alpha; `-profile:v 4` = 4444. Confirm the build supports it with `ffmpeg -encoders | grep prores`.)

**Handoff checklist (Blender -> AE)**
- [ ] Frame range, fps, resolution, aspect ratio match the AE comp
- [ ] Alpha present and verified over a bright and a dark background
- [ ] Color management consistent (Blender view transform not baked in twice)
- [ ] Frame count complete, no gaps
- [ ] Camera/object scale and orientation match the 2D layout
- [ ] Motion blur decision made in one place only (Blender or AE, not both)

## 5. Compositing 3D with 2D graphics

- Contact shadows and a subtle shared grain/blur unify CG with graphics.
- Keep one light direction across 2D drop shadows and 3D lighting.
- Keep depth cues (focus, atmosphere) consistent with the story: what should be sharp?
- Apply a final, unified grade over everything.

## 6. Resolve notes

Facts taken from the Casey Faris course transcript [CF] (software operation, not editing philosophy): Resolve's Edit and Fairlight pages share one timeline; Fusion is the compositing page; the color page is for grading; deliver with a codec/container choice (QuickTime container with ProRes for a high-quality master or when more editing follows; H.265 for small files that look good but play back harder; H.264 for compatibility with some softness). He suggests starting from the preset, matching timeline resolution and frame rate, and naming files clearly. His "anchor technique" builds a scene around shots already on the timeline, adding coverage over an anchor track. For color management: set color science and input color space for log footage. `color-and-finishing.md` has the finishing steps.

## 7. Branching: choose the pipeline

| Project | Pipeline |
|---|---|
| Talking head + B-roll | NLE rough cut -> rhythm pass -> sound -> light motion overlays (AE or NLE) -> grade -> QC |
| 2D motion piece | Storyboard -> animatic (rough timing + temp sound) -> AE build -> sound -> grade/finish |
| One 3D hero + graphics | Style frames -> Blender hero render (RGBA/EXR) -> AE composite -> sound -> finish |
| Photoreal 3D scene | Blender full render with passes -> AE/Resolve comp -> grade -> sound |
| AI-generated imagery assets | Generate -> object QC (geometry, physics, identity) -> edit; do not ship assets that fail QC |

## 8. Scripting guidance

- Generate scripts (`.jsx`, `bpy`) only after the animatic or storyboard exists; the script implements a decided design.
- Scripts must be reproducible: parameters at the top, no hard-coded absolute paths, a log, and non-destructive output (new files, never overwrite originals).
- Tell the user clearly which steps they must run and what output to expect; do not claim the script ran.
