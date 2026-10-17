# Sound Design and Audio Editing

Tags: **[Murch-sound]** Walter Murch, "Dense Clarity - Clear Density" / "Womb Tone" (Transom Review text read). **[CF]** Casey Faris Resolve course (transcript read; Fairlight section). **[Heur]** practitioner rule. **[Synth]** this skill's reasoning. **[Verify]** commonly cited number - confirm against current platform documentation before delivery.

## 1. Sound's job

Sound sets emotion, location, tempo, and attention before the picture does. Murch notes that hearing is the first sense to develop, and that sound's synchronization with picture is a deep expectation. [Murch-sound] Decide each sound's **job** exactly as you do for shots: emotion, information, rhythm, or attention. A sound with no job is clutter.

## 2. The layer budget (Dense Clarity)

Murch's framework [Murch-sound]:
- **Encoded sound** (speech/language) at one end; **Embodied sound** (music) at the other; sound effects sit in between.
- **Law of two-and-a-half:** layers of the *same "color"* (same part of the spectrum) congeal into one mass at three. Three robots' footsteps: if one or two, sync matters; at three, "any sync point is as good as any other."
- Layers spread across the spectrum (dialogue + music + two kinds of effects + ambience) can reach **about five** distinct layers per "moment" (he suggests ~5 seconds) while staying clear. Six equals sixteen equals sixty: density without clarity.
- Mix density like loudness: "A monotonously dense soundtrack is just as wearing as a monotonously loud film." Add something new -> remove something else.
- He removed music under key dialogue because the story required the words, even when "realism" said otherwise.

**Operational rules** [Synth from Murch]
1. For any 5-second window, count distinct layers: voice, music, hard FX, soft/ambient FX, ambience. Over 5 -> remove. Over 2-3 *within one category* -> remove or merge.
2. Voice-over leads: when it speaks, music ducks and effects thin out to accents.
3. Choose which single element is the **hero** per beat; others support in volume and complexity.
4. The audience is "primarily involved in following the story"; if a rule hurts the story, the story wins. [Murch-sound]

## 3. Silence

"In film... silence can be a glowing and powerful force if, like any potentially dangerous substance, it is handled correctly." [Murch-sound] Use: just before a reveal, immediately after a surprising number, after a hit to let it ring out. Do not leave dead gaps: keep room tone/ambience unless true silence is the point. [Synth]

## 4. Sync

- Hard-sync what the viewer can *see* make a sound (object impacts, clicks, UI lands), because mismatch reads as error.
- Don't over-sync crowds/repeats (three or more similar sources: loosely placed beats feel more natural). [Murch-sound, footsteps]
- Sync graphics to a **sound beat**, not just to a visual: a text slam, a hit, and a visible frame change should coincide within about 1-2 frames at 30 fps. [Heur]

## 5. Audio transitions

| Device | What it does | Use |
|---|---|---|
| **J-cut** | Next scene's audio begins before its picture | Anticipation; smooth topic changes |
| **L-cut** | Previous audio continues over next picture | Reaction/continuity; let a sentence finish over new image |
| **Pre-lap ambience** | New room tone fades in 6-12 frames early | Location change that feels natural |
| **Cut to silence** | Everything drops at the cut | Shock/focus; payoff isolation |
| **Riser -> hit** | Build then impact on cut | Strong reveal, use rarely |
| **Whoosh** | Tied to *visible* fast motion | Only when something visibly moves fast; never on a static fade |

Matching a transition's audio to its visual character is part of whether the transition is justified: if you cannot find a sound that makes sense for it, the transition may not be motivated. [Synth]

## 6. Sound for motion graphics (starting points, adjust by ear) [Heur]

| Visual event | Sound approach |
|---|---|
| Text/element lands | Short, dry hit or soft tick, 1-2 frames before/at the settle; shaped by the easing (soft ease-out -> soft sound) |
| Line draws / wipe reveals | Soft airy sweep matching duration |
| Number counts up | Ticks that follow the number rate; end with a distinct final tone |
| Object morph / transform | One continuous tone shift, not many hits |
| Camera push | Low swell scaled to distance |
| Emphasis | One accent per beat, not per element |
| Glitch/flash | Very sparing; photosensitivity limits apply (`motion-design.md`) |

Rule: each *rhythmic unit* gets one primary sound; stagger secondary sounds a few frames apart rather than stacking at one frame.

## 7. Music

- Decide the music last: it is the easiest layer to over-supply.
- Cut to the music's phrase boundaries, but never let the grid override a thought boundary (storytelling section 1). If conflict -> story wins.
- Instrumental under voice; leave spectral room (reduce competing midrange).
- Duck 3-6 dB under voice with smooth attack/release rather than an abrupt level jump. [Heur]
- Licensing/provenance recorded for every track; unknown source -> do not ship. [Synth]

## 8. Mix structure (tool-agnostic, example from Resolve/Fairlight)

[CF] Fairlight shares the same timeline as the Edit page, so audio can be adjusted back and forth. "Tracks are your best friend"; use many tracks, route groups to **buses** (submixes) so one EQ/dynamics setting can apply to all. A dialogue bus with a compressor with only "a little bit of gain reduction" levels speech; to make a sound seem to come from another room, cut its high frequencies with EQ. Loudness meter is available for perceived loudness.

Generic chain: clean (noise/hum) -> level (clip gain) -> tone (EQ) -> control (light compression) -> place (reverb/pan) -> balance (bus faders) -> loudness check.

## 9. Delivery loudness [Verify]

Commonly cited target for online video is about -14 LUFS integrated with true peak at or below about -1 dBTP, but platforms differ and change. Measure with:

```
python scripts/video_qc.py your.mp4        # includes EBU R128 loudness via ffmpeg
```

Compare against the destination's current documentation; keep the dialogue intelligible on a phone speaker.

## 10. Verification routine

1. Listen once with picture off: is the story still followable?
2. Listen at low volume: dialogue still intelligible?
3. Check mono compatibility (phase issues vanish content).
4. Phone-speaker check (most viewers).
5. Run `scripts/video_qc.py` for loudness, silence gaps, clipping flags.
6. Count layers in the busiest 5 seconds.

## 11. Common mistakes -> corrections

| Mistake | Fix |
|---|---|
| Whoosh on every transition | Reserve for visible fast motion; use ambience/J-cut elsewhere |
| Music loud under VO | Duck; thin midrange; shorten music edit points |
| Each animated element has its own sound | One sound per rhythmic unit; stagger secondaries |
| Silence from dropped room tone | Keep a quiet bed; reserve true silence for the beat that needs it |
| Unmotivated bass hits | Only when something visible lands with weight |
| Clipping / inconsistent levels | Clip gain first, then compression; verify with meters |
