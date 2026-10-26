"""Original score + sound design, synthesised from scratch (no samples, no generative-AI audio).

Music: calm D-major bed, 80 BPM, pad + felt-piano arpeggio + sub, light synthetic room.
SFX: tuned to the same key and placed from cues.json (the motion timeline), so picture and sound are frame-locked.
Mix: music is ducked a few dB under each effect; master is loudness-normalised later by ffmpeg.
Output: mix.wav (48 kHz, stereo, float32).
"""
import json, pathlib
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

ROOT = pathlib.Path(__file__).parent
SR = 48000
import os
CUES = os.environ.get('CUES', 'cues.json'); OUTP = os.environ.get('OUT', '')
LOOP = os.environ.get('LOOP') == '1'
TL = json.loads((ROOT / CUES).read_text())
DUR = TL['END']
N_OUT = int(DUR * SR)
TAIL = int(3.0 * SR) if LOOP else 0
N = N_OUT + TAIL                       # render a tail; for a loop it is folded back onto the start
rng = np.random.default_rng(20)          # fixed seed → reproducible render
t_all = np.arange(N) / SR

def hz(m): return 440.0 * 2 ** ((m - 69) / 12)   # MIDI → Hz
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x)

def place(buf, sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= buf.shape[0]: return
    sig = sig[: buf.shape[0] - i]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[i:i + len(sig), 0] += sig * gain * l * 1.414
    buf[i:i + len(sig), 1] += sig * gain * r * 1.414

def env_adsr(n, a, d, s, r_len):
    e = np.ones(n) * s
    na, nd, nr = int(a * SR), int(d * SR), int(r_len * SR)
    e[:na] = np.linspace(0, 1, na)
    e[na:na + nd] = np.linspace(1, s, nd)
    if nr: e[-nr:] *= np.linspace(1, 0, nr) ** 1.5
    return e

def room(n_sec=2.4, decay=3.2, seed=1):
    r = np.random.default_rng(seed)
    n = int(n_sec * SR); tt = np.arange(n) / SR
    ir = r.standard_normal((n, 2)) * np.exp(-decay * tt)[:, None]
    ir[:, 0] = lp(ir[:, 0], 5000); ir[:, 1] = lp(ir[:, 1], 5000)
    return ir / np.abs(ir).sum(axis=0).max() * 6

IR = room()

def reverb(x, wet):
    y = np.stack([fftconvolve(x[:, c], IR[:, c])[: len(x)] for c in range(2)], axis=1)
    return x * (1 - wet) + y * wet

# ───────────────────────── music ─────────────────────────
BPM = float(os.environ.get('BPM', 80)); BEAT = 60 / BPM; BAR = 4 * BEAT
# two bars per chord: Dmaj9 · Bm9 · Gmaj9 · A(add9)/sus → resolves on D
CHORDS = [
    [50, 57, 61, 64, 66],   # D  A  C# E  F#
    [47, 54, 57, 61, 62],   # B  F# A  C# D
    [43, 50, 54, 57, 59],   # G  D  F# A  B
    [45, 52, 57, 59, 61],   # A  E  A  B  C#
]
music = np.zeros((N, 2))

def pad_voice(f, n):
    tt = np.arange(n) / SR
    vib = 1 + 0.0025 * np.sin(2 * np.pi * 4.6 * tt)
    s = 0
    for det, g in ((-0.12, .5), (0.0, 1), (0.12, .5)):
        ff = f * 2 ** (det / 12)
        ph = 2 * np.pi * ff * np.cumsum(vib) / SR
        s = s + g * (np.sin(ph) + .28 * np.sin(2 * ph) + .12 * np.sin(3 * ph))
    return s / 2

def felt_key(f, dur=1.6):
    n = int(dur * SR); tt = np.arange(n) / SR
    s = sum(a * np.sin(2 * np.pi * f * k * tt) * np.exp(-tt * (2.6 + k * 1.6)) for k, a in ((1, 1), (2, .38), (3, .14), (4, .06)))
    hammer = rng.standard_normal(n) * np.exp(-tt * 120) * .05
    s = lp(s + hammer, 2600)
    a = int(.006 * SR); s[:a] *= np.linspace(0, 1, a)
    return s

nbars = int(np.ceil(DUR / BAR)) + 1
for b in range(nbars):
    t0 = b * BAR
    if t0 >= DUR - 1e-6: break
    ch = CHORDS[(b // 2) % 4] if (LOOP or t0 < DUR - 4.2) else CHORDS[0]
    if LOOP and t0 >= DUR - 2 * BAR - 1e-6: ch = CHORDS[3]       # loop: last two bars sit on A, which resolves to D at the restart
    # pad: one swell per bar
    n = int((BAR + 1.6) * SR)
    pad = sum(pad_voice(hz(m + 12), n) for m in ch[1:]) * env_adsr(n, 1.1, .8, .8, 1.6)
    pad = lp(pad, 1500)
    build = 0.85 if LOOP else (0.55 if t0 < 4 else (0.8 if t0 < 19 else 1.0))
    place(music, pad * .055 * build, t0, pan=0)
    # sub bass
    nb = int((BAR + .8) * SR); tb = np.arange(nb) / SR
    sub = np.sin(2 * np.pi * hz(ch[0] - 12) * tb) * env_adsr(nb, .25, .6, .7, .8)
    place(music, sub * .11 * (1 if LOOP or t0 >= 4 else 0.6), t0)
    # felt-piano arpeggio (sparser in the intro, fuller in the middle, still at the end)
    pattern = [0, 2, 4, 3, 1, 4, 2, 3] if (LOOP or 4 <= t0 < DUR - 4.2) else [0, 4, 2, 3]
    step = BAR / len(pattern)
    for k, idx in enumerate(pattern):
        note = ch[1:][idx % 4] + 12
        place(music, felt_key(hz(note)) * .07 * (0.75 + .25 * (k % 2 == 0)), t0 + k * step, pan=(-.35 if k % 2 else .35))

music = reverb(music, .32)
if not LOOP:
    fade_in, fade_out = int(.6 * SR), int(1.4 * SR)
    music[:fade_in] *= np.linspace(0, 1, fade_in)[:, None]
    music[N_OUT - fade_out:N_OUT] *= np.linspace(1, 0, fade_out)[:, None] ** 1.6
    music[N_OUT:] = 0

# ───────────────────────── sound design ─────────────────────────
def tone(f, dur, decay, partials=((1, 1),)):
    n = int(dur * SR); tt = np.arange(n) / SR
    return sum(a * np.sin(2 * np.pi * f * k * tt) for k, a in partials) * np.exp(-decay * tt)

def sfx_ping():                    # two-note notification (E6 → B6), soft bell
    a = tone(hz(88), .9, 7, ((1, 1), (2.01, .18), (3.0, .05)))
    b = tone(hz(95), 1.1, 6, ((1, 1), (2.01, .15)))
    out = np.zeros(int(1.3 * SR)); out[:len(a)] += a; i = int(.09 * SR); out[i:i + len(b)] += b * .9
    return lp(out, 7000) * .5

def sfx_whoosh(d=.7):
    n = int(d * SR); tt = np.arange(n) / SR
    s = bp(rng.standard_normal(n), 350, 3200)
    e = np.sin(np.pi * np.clip(tt / d, 0, 1)) ** 2
    return s * e * .22

def sfx_swipe():                   # pen stroke for the strike line
    n = int(.32 * SR); tt = np.arange(n) / SR
    s = bp(rng.standard_normal(n), 1800, 7000) * (np.exp(-tt * 9) * (1 - np.exp(-tt * 140)))
    return s * .35

def sfx_tick():                    # clock escapement, tiny
    n = int(.05 * SR); tt = np.arange(n) / SR
    s = bp(rng.standard_normal(n), 2500, 6500) * np.exp(-tt * 260) + .4 * np.sin(2 * np.pi * 3100 * tt) * np.exp(-tt * 180)
    return s * .5

def sfx_click():                   # seconds marker, woody
    return lp(tone(hz(81), .09, 45, ((1, 1), (2.7, .3))), 4500) * .5

def sfx_accent():                  # the yellow "now" mark (A6)
    return tone(hz(93), 1.0, 5, ((1, 1), (2.0, .2), (3.01, .06))) * .42

def sfx_pop():
    n = int(.12 * SR); tt = np.arange(n) / SR
    f = 520 + 380 * np.exp(-tt * 40)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 28) * .5

def sfx_lid():                     # soft, low close of the eyelid
    n = int(.6 * SR); tt = np.arange(n) / SR
    body = np.sin(2 * np.pi * 92 * tt) * np.exp(-tt * 9)
    air = lp(rng.standard_normal(n), 420) * np.exp(-tt * 7) * .6
    return (body + air) * (1 - np.exp(-tt * 60)) * .55

def sfx_chime():                   # closing D-major arpeggio (D6 F#6 A6 D7)
    out = np.zeros(int(2.4 * SR))
    for k, m in enumerate((86, 90, 93, 98)):
        s = tone(hz(m), 2.0, 2.8, ((1, 1), (2.0, .12), (3.0, .04)))
        i = int(k * .085 * SR); out[i:i + len(s)] += s * (.55 - k * .07)
    return lp(out, 8000) * .45

BANK = dict(ping=sfx_ping, whoosh=sfx_whoosh, swipe=sfx_swipe, tick=sfx_tick, click=sfx_click,
            accent=sfx_accent, pop=sfx_pop, lid=sfx_lid, chime=sfx_chime)
PAN = dict(ping=-.15, tick=.2, click=.1, accent=-.2, pop=0, swipe=.15)

# per-effect trims from measured level above the music at each hit (target ≈ +2…+8 dB; ticks/whoosh sit under)
TRIM = dict(ping=.26, accent=.62, chime=1.0, lid=1.0, swipe=1.0, click=.88, pop=1.57, tick=1.76, whoosh=2.0)
if LOOP:                                # full-level music from the first beat: re-trim against the measured balance
    TRIM.update(ping=.46, swipe=1.5, click=1.15, pop=2.0, tick=2.4, accent=.57, lid=1.2, chime=1.05, whoosh=2.6)
fx = np.zeros((N, 2))
for c in TL['cues']:
    place(fx, BANK[c['name']](), c['t'], c['gain'] * TRIM[c['name']], PAN.get(c['name'], 0))
fx = reverb(fx, .18)

# duck the music under the effects (≈ −4 dB max), smooth attack/release so it never pumps
lvl = np.abs(fx).max(axis=1)
k_att, k_rel = np.exp(-1 / (.03 * SR)), np.exp(-1 / (.35 * SR))
envl = np.zeros(N); e = 0.0
for i in range(0, N, 48):                      # 1 ms resolution
    x = lvl[i:i + 48].max()
    e = x + (e - x) * (k_att ** 48 if x > e else k_rel ** 48)
    envl[i:i + 48] = e
duck = 1 - np.clip(envl / (envl.max() + 1e-9), 0, 1) * (1 - 10 ** (-4 / 20))

mix = music * duck[:, None] + fx
def fold(x):
    x = x.copy()
    if LOOP: x[:TAIL] += x[N_OUT:N_OUT + TAIL]   # tails ring into the restart → no seam
    return x[:N_OUT]
music_d, fx_o = fold(music * duck[:, None]), fold(fx)
mix = fold(mix)
norm = np.abs(mix).max() / 0.7
mix /= norm                              # headroom; final loudness set by ffmpeg loudnorm
pre = OUTP and OUTP + '_' or ''
wavfile.write(ROOT / f'{pre}stem_music_in_mix.wav', SR, (music_d / norm).astype(np.float32))
wavfile.write(ROOT / f'{pre}stem_fx_in_mix.wav', SR, (fx_o / norm).astype(np.float32))
wavfile.write(ROOT / f'{pre}mix.wav', SR, mix.astype(np.float32))
print('mix.wav', DUR, 's,', len(TL['cues']), 'cues')
