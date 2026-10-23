"""Trilha investigativa + efeitos sonoros, tudo SINTETIZADO aqui (livre de direitos). Variante de _ferramentas/musica.py.

Uso: python3 som/gerar_som.py   (depois de audio/tempos.json existir)
Gera som/trilha.wav (música, estéreo) e som/sfx.wav (efeitos, estéreo), ambos com a duração do vídeo.
Os tempos dos efeitos vêm dos cues do roteiro (audio/tempos.json), então acompanham a narração.

Trilha (v3, 22/10): plantão de notícias — 126 BPM, cordas em staccato, metais, tímpano, bateria marcada e relógio de redação.
(bumbo macio). Some antes do "O QUE ACONTECEU?" (silêncio + impacto) e, no encerramento, perde o pulso e
vira um pad maior e reflexivo com uma nota suave no texto final; fade-out nos créditos.
"""
import json
from pathlib import Path
import numpy as np

SR = 48000
EP = Path(__file__).resolve().parents[1]
rng = np.random.default_rng(9)


def note(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def cues():
    d = json.loads((EP / "audio" / "tempos.json").read_text(encoding="utf-8"))
    C = {}
    for s in d["scenes"]:
        C[s["id"]] = s["start"]
        C[s["id"] + ".end"] = s["start"] + s["dur"]
        for k, v in s["cues"].items():
            C[f"{s['id']}.{k}"] = s["start"] + v
    return C, d["total"] + 0.3


C, DUR = cues()
N = int(DUR * SR)
T = np.arange(N) / SR


def env_ramp(points):
    """envelope por pontos (t, valor) com interpolação linear"""
    ts, vs = zip(*points)
    return np.interp(T, ts, vs)


def lp_fft(x, fc, order=4):
    """passa-baixa no domínio da frequência (rápido para sinais longos)"""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (f / fc) ** (2 * order))
    return np.fft.irfft(X, len(x))


def hp_fft(x, fc, order=2):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    with np.errstate(divide="ignore"):
        X *= 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** (2 * order))
    return np.fft.irfft(X, len(x))


# ------------------------------------------------------------------ trilha
# ------------------------------------------------------------------ trilha (v3: plantão de notícias)
# 126 BPM em lá menor, marcado e urgente. Camadas: ostinato de "cordas" em staccato (semicolcheias), metais sintéticos
# em golpes (stabs) sincopados, tímpano nas cabeças de frase, bumbo nos 4 tempos, caixa no 2 e 4, chimbal em
# semicolcheias, baixo em colcheias com oitava e o relógio de redação. Arranjo pelos cues: abertura com relógio +
# ostinato + tímpanos crescendo; silêncio antes do "O QUE ACONTECEU?"; batida completa do congestionamento às
# perguntas (sem caixa/metais no "houve fraude?"); encerramento sem bateria, acordes maiores, arpejo lento.
DARK = [[45, 52, 57, 60, 64], [45, 52, 57, 60, 64], [41, 48, 53, 57, 60], [40, 47, 52, 56, 59]]   # Am Am F E
LIGHT = [[48, 55, 60, 64, 67], [43, 50, 55, 59, 62], [45, 52, 57, 60, 64], [41, 48, 53, 57, 64]]  # C G Am Fmaj7
BPM = 126
BEAT = 60 / BPM
S16 = BEAT / 4
BAR = 4 * BEAT                  # acorde troca a cada 2 compassos
T_FIM = C["08"]
T_Q = C["01.q"]


def chord_at(t):
    k = int(t // (2 * BAR))
    return (LIGHT if t >= T_FIM - 1 else DARK)[k % 4]


def add(out, t, sig):
    i0 = int(t * SR)
    if 0 <= i0 < N:
        n = min(len(sig), N - i0)
        out[i0:i0 + n] += sig[:n]


def saw(f, tt):
    return 2 * ((f * tt) % 1.0) - 1


def nrm(x):
    return x / (np.max(np.abs(x)) + 1e-9)


def tick_layer():
    out = np.zeros(N)
    L = int(0.025 * SR); tt = np.arange(L) / SR
    for i in range(int(DUR / BEAT) + 1):
        f = 2800 if i % 2 == 0 else 2000
        s = np.sin(2 * np.pi * f * tt) * np.exp(-tt * 300) + rng.normal(0, 0.3, L) * np.exp(-tt * 600)
        add(out, i * BEAT, s)
    return nrm(out)


def ostinato_layer():
    """cordas em staccato: semicolcheias insistentes (raiz, quinta, oitava), ensemble de serras"""
    out = np.zeros(N)
    L = int(S16 * 0.8 * SR); tt = np.arange(L) / SR
    pat = [0, 0, 7, 0, 12, 0, 7, 0, 0, 0, 7, 0, 12, 7, 3, 7]
    env = np.exp(-tt * 18) * np.minimum(1, tt / 0.004)
    for i in range(int(DUR / S16) + 1):
        t = i * S16
        f = note(chord_at(t)[1] + pat[i % 16])
        s = sum(saw(f * 2 ** (d / 12), tt + o) for d, o in ((-0.1, 0.1), (0, 0.4), (0.1, 0.7)))
        add(out, t, s * env * (1.0 if i % 4 == 0 else 0.75))
    out = hp_fft(lp_fft(out, 2800, 2), 180)
    return nrm(out)


def bass_layer():
    """baixo em colcheias, raiz e oitava, serra filtrada e seca"""
    out = np.zeros(N)
    L = int(BEAT / 2 * 0.9 * SR); tt = np.arange(L) / SR
    for i in range(int(DUR / (BEAT / 2)) + 1):
        t = i * BEAT / 2
        f = note(chord_at(t)[0] - 12 + (12 if i % 2 else 0))
        s = (saw(f, tt) + 0.6 * np.sin(2 * np.pi * f / 2 * tt)) * np.exp(-tt * 7) * np.minimum(1, tt / 0.003)
        add(out, t, s)
    return nrm(lp_fft(out, 650, 3))


def brass_layer():
    """metais sintéticos em golpes: cabeça de cada frase + síncopes (1, 2e, 4 do compasso ímpar)"""
    out = np.zeros(N)
    L = int(0.5 * SR); tt = np.arange(L) / SR
    for k in range(int(DUR / (2 * BAR)) + 1):
        t0 = k * 2 * BAR
        for off, dur, g in ((0, 0.45, 1.0), (1.5 * BEAT, 0.22, 0.7), (3 * BEAT, 0.22, 0.75), (4 * BEAT + 2.5 * BEAT, 0.3, 0.85)):
            ch = chord_at(t0 + 0.01)
            n = int(dur * SR); x = tt[:n]
            s = sum(saw(note(m), x + rng.uniform(0, 1)) for m in ch[1:])
            # "brilho" de metal: filtro abre e fecha (aprox. com mistura de versão filtrada)
            bright = np.exp(-x * 10)
            sig = s * (np.minimum(1, x / 0.012)) * np.exp(-x * 3) * (0.35 + 0.65 * bright)
            sig[-int(0.02 * SR):] *= np.linspace(1, 0, int(0.02 * SR))
            add(out, t0 + off, sig * g)
    return nrm(lp_fft(out, 3500, 2))


def timpani_layer():
    """tímpano: golpe grave afinado na raiz, nas cabeças de frase; rufo curto antes de cada 4ª frase"""
    out = np.zeros(N)
    L = int(1.6 * SR); tt = np.arange(L) / SR
    for k in range(int(DUR / (2 * BAR)) + 1):
        t0 = k * 2 * BAR
        f0 = note(chord_at(t0 + 0.01)[0] - 12)
        f = f0 * (1 + 0.08 * np.exp(-tt * 25))
        hit = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 3.0) + lp_fft(rng.normal(0, 1, L), 500) * np.exp(-tt * 30) * 0.5
        add(out, t0, hit)
        if k % 4 == 3:  # rufo na última semínima da frase
            for j in range(8):
                add(out, t0 + 2 * BAR - BEAT + j * BEAT / 8, hit[:int(0.3 * SR)] * (0.25 + 0.08 * j))
    return nrm(out)


def drums():
    kick = np.zeros(N); snare = np.zeros(N); hat = np.zeros(N)
    L = int(0.3 * SR); tt = np.arange(L) / SR
    f = 48 + 110 * np.exp(-tt * 40)
    k = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 11)
    Ls = int(0.22 * SR); ts = np.arange(Ls) / SR
    sn = hp_fft(rng.normal(0, 1, Ls), 1200) * np.exp(-ts * 22) + 0.6 * np.sin(2 * np.pi * 190 * ts) * np.exp(-ts * 30)
    Lh = int(0.04 * SR); th = np.arange(Lh) / SR
    for b in range(int(DUR / BEAT) + 1):
        t = b * BEAT
        add(kick, t, k)
        if b % 4 in (1, 3):
            add(snare, t, sn)
        if b % 8 == 7:
            add(snare, t + 0.5 * BEAT, sn * 0.5); add(snare, t + 0.75 * BEAT, sn * 0.7)   # virada curta
        for j in range(4):
            add(hat, t + j * S16, rng.normal(0, 1, Lh) * np.exp(-th * 140) * (1.0 if j % 2 else 0.55))
    return nrm(kick), nrm(snare), nrm(hp_fft(hat, 7500))


def arp_slow():
    """encerramento: arpejo lento com eco"""
    out = np.zeros(N)
    step = S16 * 2
    L = int(0.4 * SR); tt = np.arange(L) / SR
    order = [0, 2, 3, 4, 3, 2, 1, 2]
    for i in range(int(DUR / step) + 1):
        t = i * step
        if t < T_FIM - 2:
            continue
        f = note(chord_at(t)[1 + order[i % 8] % 4] + 12)
        w = np.tanh(3 * np.sin(2 * np.pi * f * tt)) * 0.6 + 0.4 * np.sin(2 * np.pi * 2 * f * tt)
        add(out, t, w * np.exp(-tt * 7) * np.minimum(1, tt / 0.002))
    out = lp_fft(out, 3200, 2)
    d = int(3 * S16 * SR)
    echo = 0.45 * np.concatenate([np.zeros(d), out[:-d]]) + 0.2 * np.concatenate([np.zeros(2 * d), out[:-2 * d]])
    m = np.max(np.abs(out)) + 1e-9
    return out / m, echo / m


def pad_layer():
    out = np.zeros(N)
    seg = 2 * BAR
    for k in range(int(DUR / seg) + 1):
        t0 = k * seg
        ch = chord_at(t0 + 0.01)
        n = int((seg + 1.5) * SR); tt = np.arange(n) / SR
        s = sum(saw(note(m) * 2 ** (d / 12), tt + rng.uniform(0, 1)) for m in ch[1:] for d in (-0.07, 0.07))
        a = np.minimum(1, tt / 1.2) * np.minimum(1, np.maximum(0, seg + 1.5 - tt) / 1.5)
        add(out, t0, s * a)
    return nrm(lp_fft(out, 900, 3))


def trilha():
    tick, ost, bass, brass, timp, pad = tick_layer(), ostinato_layer(), bass_layer(), brass_layer(), timpani_layer(), pad_layer()
    kick, snare, hat = drums()
    arps, arps_echo = arp_slow()
    e2, e5, e6, e7 = C["02"], C["05"], C["06"], C["07"]
    cut = lambda a, b: [(T_Q - 0.3, a), (T_Q - 0.02, 0.0), (e2 - 0.3, 0.0), (e2 + 0.2, b)]
    end = lambda v: [(T_FIM - 0.8, v), (T_FIM + 1.0, 0.0)]
    g_tick = env_ramp([(0, 0), (0.5, 1.0)] + cut(1.0, 0.8) + [(e7, 0.8)] + end(0.8))
    g_ost = env_ramp([(0, 0), (0.5, 0.35), (T_Q - 3, 0.7)] + cut(0.75, 0.8) + [(e5, 0.8), (e5 + 1, 0.55), (e6, 0.7), (e7, 0.9)] + end(0.9))
    g_timp = env_ramp([(0, 0), (0.5, 0.5), (T_Q - 3, 0.9)] + cut(0.9, 0.8) + [(e7, 0.9)] + end(0.9))
    g_bass = env_ramp([(0, 0), (C["01.b"], 0), (C["01.b"] + 1, 0.6)] + cut(0.7, 1.0) + [(e7, 1.0)] + end(1.0))
    g_kick = env_ramp([(0, 0), (C["01.b"], 0), (C["01.b"] + 0.2, 0.55)] + cut(0.55, 1.0) + [(e5, 1.0), (e5 + 1, 0.85), (e6, 1.0)] + end(1.0))
    g_snare = env_ramp([(0, 0), (C["02.a"], 0), (C["02.a"] + 0.2, 0.9), (e5, 0.9), (e5 + 0.4, 0.0), (e6, 0.0), (e6 + 0.3, 0.9)] + end(0.9))
    g_hat = env_ramp([(0, 0), (e2, 0), (e2 + 1, 0.8), (e7, 1.0)] + end(1.0))
    g_brass = env_ramp([(0, 0), (C["01.b"], 0), (C["01.b"] + 0.3, 0.7)] + cut(0.7, 0.9) + [(e5, 0.9), (e5 + 0.4, 0.0), (e6, 0.0),
                       (e6 + 0.3, 0.8), (e7, 1.0)] + end(1.0))
    g_pad = env_ramp([(0, 0), (T_FIM - 2, 0), (T_FIM + 2, 0.9), (DUR - 8, 0.8), (DUR, 0.0)])
    g_arps = env_ramp([(0, 0), (T_FIM - 1, 0), (T_FIM + 2, 0.7), (DUR - 8, 0.6), (DUR, 0.0)])
    mono = (0.22 * tick * g_tick + 0.30 * ost * g_ost + 0.45 * bass * g_bass + 0.28 * brass * g_brass + 0.45 * timp * g_timp
            + 0.75 * kick * g_kick + 0.38 * snare * g_snare + 0.09 * hat * g_hat + 0.30 * pad * g_pad + 0.26 * arps * g_arps)
    d = int(0.011 * SR)
    wide = 0.30 * ost * g_ost + 0.28 * brass * g_brass   # abre cordas e metais no estéreo
    wide_d = np.concatenate([np.zeros(d), wide[:-d]])
    left = mono + 0.35 * (wide_d - wide) + 0.26 * arps_echo * g_arps
    right = mono + 0.35 * (wide - wide_d) + 0.26 * arps_echo * g_arps * 0.5
    st = np.stack([left, right], 1)
    return st / (np.max(np.abs(st)) + 1e-9) * 0.9


# ------------------------------------------------------------------ efeitos
def place(buf, t, sig, gain=1.0, pan=0.0):
    i0 = int(t * SR)
    if i0 >= N or i0 < 0:
        return
    n = min(len(sig), N - i0)
    buf[i0:i0 + n, 0] += sig[:n] * gain * (1 - max(0, pan))
    buf[i0:i0 + n, 1] += sig[:n] * gain * (1 + min(0, pan))


def s_typing(dur=1.2, rate=14):
    L = int(dur * SR)
    out = np.zeros(L)
    t = 0.0
    while t < dur - 0.05:
        i0 = int(t * SR)
        n = int(0.018 * SR)
        click = rng.normal(0, 1, n) * np.exp(-np.arange(n) / SR * 400)
        out[i0:i0 + n] += click * rng.uniform(0.5, 1.0)
        t += 1 / rate * rng.uniform(0.6, 1.4)
    return hp_fft(out, 2500) * 0.6


def s_notif():
    L = int(0.6 * SR)
    tt = np.arange(L) / SR
    a = np.sin(2 * np.pi * note(83) * tt) * np.exp(-tt * 9) * (tt < 0.3)
    b = np.sin(2 * np.pi * note(88) * (tt - 0.11)) * np.exp(-(tt - 0.11).clip(0) * 7) * (tt >= 0.11)
    return (a + b) * 0.5


def s_impact():
    L = int(2.8 * SR)
    tt = np.arange(L) / SR
    f = 32 + 70 * np.exp(-tt * 12)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.6)
    thump = lp_fft(rng.normal(0, 1, L), 300) * np.exp(-tt * 14) * 2.0
    tail = lp_fft(rng.normal(0, 1, L), 900) * np.exp(-tt * 2.2) * 0.25
    s = boom + thump + tail
    return s / np.max(np.abs(s))


def s_data(dur=1.6):
    """transmissão de dados: bipes curtos em frequências aleatórias, bem baixo"""
    L = int(dur * SR)
    out = np.zeros(L)
    t = 0.0
    while t < dur - 0.06:
        n = int(rng.uniform(0.02, 0.05) * SR)
        f = rng.choice([1200, 1500, 1800, 2400, 3000])
        tt = np.arange(n) / SR
        i0 = int(t * SR)
        out[i0:i0 + n] += np.sign(np.sin(2 * np.pi * f * tt)) * np.hanning(n) * 0.5
        t += rng.uniform(0.04, 0.12)
    return lp_fft(out, 5000) * np.linspace(1, 0.3, L)


def s_glitch(dur=0.9):
    """leve distorção digital: ruído recortado (bitcrush) em rajadas"""
    L = int(dur * SR)
    out = np.zeros(L)
    t = 0.0
    while t < dur - 0.08:
        n = int(rng.uniform(0.03, 0.09) * SR)
        i0 = int(t * SR)
        hold = rng.integers(20, 80)
        x = np.repeat(rng.normal(0, 1, n // hold + 1), hold)[:n]
        x = np.round(x * 3) / 3
        out[i0:i0 + n] += x * np.hanning(n)
        t += rng.uniform(0.08, 0.2)
    return lp_fft(out, 4000) * 0.6


def s_whoosh(dur=0.9):
    L = int(dur * SR)
    tt = np.arange(L) / SR
    x = rng.normal(0, 1, L) * np.sin(np.pi * tt / dur) ** 2
    return lp_fft(hp_fft(x, 400), 2500) * 0.5


def s_bell():
    L = int(5.0 * SR)
    tt = np.arange(L) / SR
    s = np.zeros(L)
    for m, a, d in ((72, 1.0, 1.2), (79, 0.5, 1.6), (84, 0.35, 2.2), (88, 0.15, 3.0)):
        s += a * np.sin(2 * np.pi * note(m) * tt) * np.exp(-tt * d)
    return s / np.max(np.abs(s)) * np.minimum(1, tt / 0.01)


def sfx():
    buf = np.zeros((N, 2))
    place(buf, C["01.a"] + 0.05, s_typing(1.4), 0.10, -0.3)
    place(buf, C["01.c"] + 0.2, s_glitch(1.0), 0.12, 0.2)
    place(buf, T_Q, s_impact(), 0.55)
    place(buf, C["02.d"] + 0.05, s_typing(1.0), 0.09, 0.3)
    place(buf, C["02.a"] + 0.2, s_data(2.2), 0.06, -0.4)
    place(buf, C["02.c"] + 0.1, s_glitch(0.8), 0.11, 0.3)
    place(buf, C["03.a"], s_whoosh(), 0.12)
    place(buf, C["03.b"], s_notif(), 0.09, 0.3)
    place(buf, C["03.d"], s_notif(), 0.10)
    for cue in ("04.a", "04.b", "04.c"):
        place(buf, C[cue], s_data(0.6), 0.05, (-0.4, 0, 0.4)[("04.a", "04.b", "04.c").index(cue)])
    place(buf, C["05.b"], s_notif(), 0.09)
    place(buf, C["06.b"], s_whoosh(), 0.10)
    place(buf, C["06.e"], s_notif(), 0.09)
    place(buf, C["06.e"] + 1.6, s_notif(), 0.08)
    place(buf, C["07.z"] + 0.1, s_typing(1.0), 0.09)
    for i, cue in enumerate(("07.a", "07.b", "07.c", "07.d")):
        place(buf, C[cue], s_notif(), 0.07, (-0.3, 0.3)[i % 2])
    place(buf, C["08.x"], s_bell(), 0.16)
    return buf


def save(path, st):
    import subprocess
    raw = path.with_suffix(".f32")
    st.astype(np.float32).tofile(raw)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", str(raw), str(path)],
                   check=True)
    raw.unlink()


if __name__ == "__main__":
    out = EP / "som"
    save(out / "trilha.wav", trilha())
    save(out / "sfx.wav", np.clip(sfx(), -1, 1))
    print("ok", round(DUR, 2), "s")
