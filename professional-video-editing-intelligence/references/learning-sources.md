# Learning Sources: What Was Actually Accessed

Research date: 2026-10-17, from a cloud sandbox. Direct web fetch was blocked (DNS) for most sites; content was read through a search/fetch connector (Exa) that returned page text and YouTube transcripts. **No video was watched or heard.** "Read" below means a text transcript or page text was read. Where only part was read, it says so.

Evidence tiers used across the package: **A** primary text/transcript read in this research; **B** secondary summary/commentary of a primary source; **C** practitioner heuristic or vendor/blog guidance; **D** the author's synthesis (this skill) - plausible, untested outside worked examples. Study evidence: **Obs** observational; **Weak** small/unreviewed.

## 1. The five starting resources: verification and verdict

| # | Resource (as given) | What it actually is | Accessed | Verdict |
|---|---|---|---|---|
| 1 | Every Frame a Painting (YouTube search URL) | A search page, not a video. Resolved to the series' editing essay **"How Does an Editor Think and Feel?"** https://www.youtube.com/watch?v=3Q3eITC01Fg (2016, Tony Zhou & Taylor Ramos; ~9 min) | **Full English transcript read** (community subtitles). Other EFAP episodes: not read. | **Keep.** Highest value per minute for rhythm, emotion timing, invisible vs jarring cuts. Limit: film-editing focus; one episode only. |
| 2 | StudioBinder - Murch / *In the Blink of an Eye* https://www.youtube.com/watch?v=PKYeClvvlTw | "The Book Every Editor Has to Read - Walter Murch and In the Blink of an Eye" by StudioBinder | **Full transcript read.** Murch's own text for the Rule of Six read via excerpts (Berkeley course blog; New School excerpt PDF; Video&Filmmaker). Book not read in full. | **Keep.** Foundational: blink theory, Rule of Six, dragnet cutting, 30°/180° rules, test-audience insight. Limit: feature-film context; weights are Murch's tongue-in-cheek numbers. |
| 3 | Ben Marriott - Master Motion Design (first prompt: https://www.youtube.com/watch?v=EyHO1liVCpo; second prompt: https://www.benmarriott.com/mastermotiondesign) | The YouTube video is a **1-minute promo** (transcript read: no teaching content). The course page (paid, 8 weeks, 10+ hours) lists weekly syllabus text. | Promo transcript read; **course page syllabus text read**; **no lesson content accessed (paywalled).** | **Keep only as syllabus-level evidence** (12 principles with focus on anticipation/overlap, blocking, arcs, file organization, transitions, morphing, effects-driven systems). Do not claim lesson-level knowledge. Motion principles were supplemented from sources in section 2. |
| 4 | Casey Faris - DaVinci Resolve full course (YouTube search URL; first prompt: https://www.youtube.com/watch?v=MCDVcQIA3UM) | "Introduction to DaVinci Resolve - [Full Course] for Beginners (2026)" | **Entire transcript retrieved (about 330k characters); only selected sections read** (intro, Edit/anchor-technique tail, Fusion color-management setup, color primaries, Fairlight bus/EQ/compressor, delivery/codecs). | **Demote to implementation reference.** It teaches software operation, not editing judgement. Used for audio-bus structure, color-management reminders, and codec trade-offs only (tagged [CF]). |
| 5 | Ben Marriott - After Effects fundamentals (YouTube search URL; first prompt: "Teach You After Effects in 60 Minutes") | "I'll Teach You After Effects in 60 Minutes..." https://www.youtube.com/watch?v=jFbRZZmMW7c (2023), a preview of his paid *Motion Foundation* course; plus "Learn After Effects in 10 Minutes" https://www.youtube.com/watch?v=hb2bbfiNBXA | 60-min transcript read (retrieved ~65k characters); 10-min video excerpt read. | **Keep as the AE workflow source** (organization habits, easing, offset, precomps, render intermediate -> H.264). Beginner level; principles come from other sources. |

**Net judgement:** Sources 1 and 2 carry the editing intelligence. Sources 3-5 carry tool workflow. Motion-design and sound principles needed more depth than 3-5 offered, so section 2 sources were added.

## 2. Additional sources added (gaps filled)

| Topic | Source | Access | Tier |
|---|---|---|---|
| Sound layering | Walter Murch, "Dense Clarity - Clear Density" and "Womb Tone" (Transom Review) https://transom.org/2005/walter-murch/ | Text read (large excerpts) | A |
| Rule of Six primary text | Murch, *In the Blink of an Eye* excerpts (Berkeley blog: https://blogs.ischool.berkeley.edu/i290-viznarr-s12/the-rule-of-six-walter-murch/ ; New School PDF excerpt) | Excerpts read | A/B |
| Animation principles for screen | Adobe Blog, "Redesigning the 12 Principles of Animation for Motion Design" https://blog.adobe.com/en/publish/2016/11/08/redesigning-the-12-principles-of-animation-for-motion-design ; Adobe principles page | Text read | B/C |
| Motion-design principles | Envato Tuts+ "The Principles of Motion Design" https://design.tutsplus.com/the-principles-of-motion-design--ytc-79c ; School of Motion Animation Bootcamp description | Text read (description/summary) | C |
| Motion craft numbers | "showtime" motion-craft doc https://faviovazquez.github.io/showtime/docs/motion-craft.html | Text read | C (one project's taste) |
| Montage / Kuleshov | Wikipedia "Kuleshov effect"; Kuleshov's essay excerpt; Dancyger's textbook table of contents | Excerpts | B (note: original experiment not documented) |
| Blender/AE pipeline | Blender Stack Exchange (transparent PNG vs EXR; AE export formats); MediaScaleUp rendering guide; third-party Blender automation notes | Excerpts | C (version-dependent) |
| Short-form retention | Postdom 1,272-video study (2026-10-05); jump-cut conference paper (N=242); ACM RecSys 2025 peak-end retention paper | Excerpts / abstracts | Obs / Weak / Indirect |
| Claude Code skills | code.claude.com/docs/en/skills | Page text read (first part) | A |

**Rejected as evidence:** "Hook Analytics: Optimizing the First 3 Seconds" (JAAFR) - its abstract states a *synthetic* 13-video dataset. Not used.

## 3. Verified vs. interpreted, by principle

| Principle | Verified in a source | Interpretation added by this package |
|---|---|---|
| Cut = punctuation of a completed thought | SB, Murch text | Applying it to voice-over phrasing and presenter-edit cut points |
| Rule of Six ordering and weights | Murch text | Adding Accuracy for explainers; using ladder as tie-break procedure |
| Emotions take time; release longer than build | EFAP transcript (Empire example, 30 s vs 30 frames) | Hold-after-payoff rule and shot-length curve procedure |
| Editing ~70% rhythm | EFAP (Murch quote) | "Rhythm is not cut count" corollary |
| Invisible vs deliberate cuts | EFAP | Decision rule: name the reaction first |
| Test audiences detect problems, not causes | SB | "Check comprehension first" |
| Dense clarity: <= ~5 layers, 2.5 within one color | Murch-sound text | Counting procedure per 5-second window |
| Easing is universal | Adobe interview; Marriott 10-min | Easing-by-event table (heuristic numbers from C sources) |
| Organize layers, offset, precomp, intermediate -> H.264 | Marriott transcripts | Handoff checklists |
| Dialogue bus + EQ + light compression; codec tradeoffs | Faris transcript | Generic mix chain |
| Hook text/ending effects on views | Postdom (observational) | Used only as "what to test" |
| 30°, 180° rules | SB | Applied to optics-diagram direction rule |

## 4. Limits and unverified items

- No video or audio was watched or heard; transcripts are text.
- EFAP: one episode only. Other episodes (e.g., on action scenes, comedy, cinematography) were not read.
- Marriott's paid course lessons were not accessed; syllabus text only.
- Faris: transcript retrieved fully but read selectively.
- Murch's book was read via excerpts, not cover to cover.
- Numeric rules tagged [Heur]/[Guess] (reading budgets, safe-area pixel margins, loudness targets, stagger times) are starting points to verify with current platform documentation and by testing.
- Behaviour of After Effects, Blender, and Resolve was **not tested** here (none installed in the research sandbox). Commands are marked [Known]/[Web] and must be validated on the installed versions.
- Claude Code discovery was verified against the official documentation text, not by running Claude Code on the user's machine.

## 5. Suggested further study (not done)

Other Every Frame a Painting editing/comedy/action episodes; Murch's full book and *Dense Clarity* audio clips; a motion-design course's lesson content (if the user can share a transcript legitimately); Blender's official manual for the installed version; current platform safe-zone and loudness documentation.
