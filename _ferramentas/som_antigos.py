"""Som do canal Nós, os Antigos: trilha de museu com sintetizador analógico (alegre, em Ré maior) + efeitos.
Tudo SINTETIZADO aqui (livre de direitos).

Trilha (trilha(dur, revela, fim)): até `revela` só pad quente com filtro fechado e notas soltas de glockenspiel
(curiosidade); em `revela` uma subida leva à parte cheia: arpejo pluck com eco, baixo redondo, shaker e bumbo macio;
em `fim` um acorde de sino fecha e a trilha some. Abaixa sozinha sob a voz (ducking pela narração).
Efeitos (fx(nome)): holofote, faisca, scan, bateria, fantasma, falha, whoosh, luz, pulo, pouso, brilho, pop, vinheta.
Uso: from som_antigos import mixar; mixar(video_mudo, voz_wav, saida, dur, revela, fim, eventos=[(t, "nome"), ...])
"""
import subprocess
import wave
import numpy as np

SR = 48000
RNG = np.random.default_rng(11)
BPM = 92
BEAT = 60 / BPM
# Dmaj9 · Bm7(11) · Gmaj7(#11) · A(sus4→3): progressão luminosa, sem drama
PROG = [[38, 50, 54, 57, 61, 64], [35, 50, 54, 57, 59, 64], [31, 50, 54, 57, 59, 61], [33, 49, 52, 57, 59, 64]]


def note(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def tt(d):
    return np.arange(int(d * SR)) / SR


def nrm(x, p=1.0):
    return x / (np.max(np.abs(x)) + 1e-9) * p


def lp(x, fc, order=2):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    return np.fft.irfft(X / np.sqrt(1 + (f / fc) ** (2 * order)), len(x))


def hp(x, fc, order=2):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR) + 1e-9
    return np.fft.irfft(X / np.sqrt(1 + (fc / f) ** (2 * order)), len(x))


def bp(x, f1, f2):
    return lp(hp(x, f1), f2)


def saw(f, t):
    return 2 * ((f * t) % 1.0) - 1


def reverb(x, seg=2.6, mix=0.3, seed=3):
    """sala grande: convolução com ruído decaindo (estéreo) → (n, 2)"""
    r = np.random.default_rng(seed)
    n = int(seg * SR)
    t = np.arange(n) / SR
    out = []
    for ch in range(2):
        ir = r.normal(0, 1, n) * np.exp(-t * 6.9 / seg)
        ir = lp(ir, 5000)
        ir[: int(0.012 * SR)] = 0
        L = len(x) + n
        F = 1 << (L - 1).bit_length()
        y = np.fft.irfft(np.fft.rfft(x, F) * np.fft.rfft(ir, F), F)[: len(x)]
        out.append(y / (np.max(np.abs(y)) + 1e-9) * np.max(np.abs(x)))
    w = np.stack(out, 1)
    return np.stack([x, x], 1) * (1 - mix) + w * mix


def put(buf, t, sig, g=1.0):
    i0 = int(t * SR)
    if i0 < 0:
        sig, i0 = sig[-i0:], 0
    n = min(len(sig), len(buf) - i0)
    if n > 0:
        buf[i0:i0 + n] += sig[:n] * g


# =====================================================================
# TRILHA
# =====================================================================
def _acorde(t):
    return PROG[int(t // (4 * BEAT * 2)) % 4]  # 2 compassos por acorde


def _pad(N):
    out = np.zeros(N)
    seg = 8 * BEAT
    for k in range(int(N / SR / seg) + 1):
        ch = _acorde(k * seg + 0.01)
        t = tt(seg + 1.5)
        s = sum(saw(note(m) * 2 ** (d / 12), t + RNG.uniform(0, 1)) * (0.6 if m < 45 else 1)
                for m in ch[1:] for d in (-0.09, 0.0, 0.1))
        a = np.minimum(1, t / 1.2) * np.minimum(1, np.maximum(0, seg + 1.5 - t) / 1.5)
        put(out, k * seg, s * a)
    return out


def _arp(N):
    out = np.zeros(N)
    ordem = [1, 3, 2, 4, 3, 5, 4, 2]
    t = tt(0.5)
    for i in range(int(N / SR / (BEAT / 2)) + 1):
        t0 = i * BEAT / 2
        f = note(_acorde(t0)[ordem[i % 8]] + 12)
        # pluck analógico: dente de serra com filtro que fecha rápido (aprox.: mistura saw + seno)
        w = 0.45 * saw(f, t) * np.exp(-t * 22) + np.sin(2 * np.pi * f * t) * np.exp(-t * 7)
        put(out, t0, w * np.minimum(1, t / 0.003) * (1.0 if i % 2 == 0 else 0.75))
    return lp(out, 3200)


def _glock(N, t0, t1, every=2.6):
    """notas soltas de glockenspiel (sininho de museu) entre t0 e t1"""
    out = np.zeros(N)
    escala = [74, 76, 78, 81, 83, 86]
    t = tt(1.6)
    tc = t0
    k = 0
    while tc < t1:
        f = note(escala[(k * 3 + 1) % len(escala)])
        s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 9)
        put(out, tc, s * np.exp(-t * 2.6) * np.minimum(1, t / 0.002))
        tc += every * (0.8 + 0.4 * ((k * 7) % 5) / 4)
        k += 1
    return out


def _baixo(N):
    out = np.zeros(N)
    t = tt(BEAT * 0.95)
    for i in range(int(N / SR / BEAT) + 1):
        t0 = i * BEAT
        f = note(_acorde(t0)[0])
        put(out, t0, (np.sin(2 * np.pi * f * t) + 0.25 * saw(f, t)) * np.minimum(1, t / 0.01) * np.exp(-t * 2.2))
    return lp(out, 500)


def _ritmo(N):
    kick, shk = np.zeros(N), np.zeros(N)
    t = tt(0.3)
    k = np.sin(2 * np.pi * np.cumsum(48 + 90 * np.exp(-t * 40)) / SR) * np.exp(-t * 14)
    th = tt(0.06)
    for b in range(int(N / SR / BEAT) + 1):
        if b % 2 == 0:
            put(kick, b * BEAT, k)
        for q, g in ((0, 0.5), (0.5, 1.0)):
            put(shk, (b + q) * BEAT, RNG.normal(0, 1, len(th)) * np.exp(-th * 70) * g)
    return kick, hp(shk, 6000)


def _sino(dur=4.0):
    """acorde de sino do logo"""
    t = tt(dur)
    s = sum(np.sin(2 * np.pi * note(m) * t) * np.exp(-t * (1.2 + i * 0.3)) +
            0.3 * np.sin(2 * np.pi * note(m) * 3.01 * t) * np.exp(-t * 5) for i, m in enumerate([74, 78, 81, 86, 90]))
    return s * np.minimum(1, t / 0.003)


def _subida(d=2.0):
    """ruído + tom subindo antes da revelação"""
    t = tt(d)
    ns = bp(RNG.normal(0, 1, len(t)), 800, 6000) * (t / d) ** 2.2
    tom = np.sin(2 * np.pi * np.cumsum(220 + 660 * (t / d) ** 2) / SR) * (t / d) ** 2 * 0.4
    return ns + tom


def env(N, pts):
    ts, vs = zip(*pts)
    return np.interp(np.arange(N) / SR, ts, vs)


def trilha(dur, revela, fim):
    N = int(dur * SR)
    pad, arp, baixo = _pad(N), _arp(N), _baixo(N)
    kick, shk = _ritmo(N)
    glock = _glock(N, 1.2, revela - 0.5)
    # pad: filtro fechado (mistério) e depois aberto (salão aceso)
    pad = lp(pad, 700) * env(N, [(0, 1), (revela, 1), (revela + 1.5, 0.5), (dur, 0.5)]) + \
        lp(pad, 2600) * env(N, [(0, 0), (revela - 0.5, 0), (revela + 1.5, 0.6), (dur, 0.6)])
    D = dur
    g = dict(pad=env(N, [(0, 0), (1.5, 0.9), (D - 1.5, 0.9), (D, 0)]),
             arp=env(N, [(0, 0), (revela, 0), (revela + 0.4, 1), (fim, 1), (fim + 1, 0.4), (D, 0)]),
             baixo=env(N, [(0, 0), (revela, 0), (revela + 0.3, 1), (fim, 1), (fim + 1, 0.3), (D, 0)]),
             kick=env(N, [(0, 0), (revela + 1.2, 0), (revela + 1.3, 1), (fim, 1), (fim + 0.1, 0), (D, 0)]),
             shk=env(N, [(0, 0), (revela, 0), (revela + 0.5, 1), (fim, 1), (fim + 0.5, 0), (D, 0)]))
    mono = (0.30 * nrm(pad) * g["pad"] + 0.26 * nrm(arp) * g["arp"] + 0.34 * nrm(baixo) * g["baixo"] +
            0.30 * nrm(kick) * g["kick"] + 0.07 * nrm(shk) * g["shk"] + 0.16 * nrm(glock))
    put(mono, revela - 2.0, nrm(_subida(2.0)), 0.16)
    put(mono, fim, nrm(_sino()), 0.30)
    st = reverb(mono, 2.8, 0.32)
    # eco do arpejo abrindo o estéreo (pingue-pongue)
    d = int(BEAT * 0.75 * SR)
    eco = np.concatenate([np.zeros(d), (0.26 * nrm(arp) * g["arp"])[:-d]])
    st[:, 0] += 0.35 * eco
    st[:, 1] += 0.35 * np.concatenate([np.zeros(d), eco[:-d]])
    return nrm(st, 0.9)


# =====================================================================
# EFEITOS
# =====================================================================
def fx(nome):
    if nome == "holofote":  # relé grande ligando: estalo grave + zumbido elétrico
        t = tt(0.9)
        thump = np.sin(2 * np.pi * np.cumsum(70 + 80 * np.exp(-t * 30)) / SR) * np.exp(-t * 10)
        clk = hp(RNG.normal(0, 1, len(t)), 2500) * np.exp(-t * 120)
        hum = (np.sin(2 * np.pi * 120 * t) + 0.5 * np.sin(2 * np.pi * 240 * t)) * np.exp(-t * 3) * 0.25
        return nrm(thump + 0.6 * clk + hum)
    if nome == "faisca":  # piscada da lâmpada
        t = tt(0.12)
        return nrm(bp(RNG.normal(0, 1, len(t)), 1500, 7000) * np.exp(-t * 40)) * 0.5
    if nome == "luz":  # luzes do salão acendendo (mais leve)
        t = tt(0.5)
        thump = np.sin(2 * np.pi * np.cumsum(90 + 60 * np.exp(-t * 30)) / SR) * np.exp(-t * 14)
        return nrm(thump + 0.4 * hp(RNG.normal(0, 1, len(t)), 3000) * np.exp(-t * 150)) * 0.7
    if nome == "scan":  # raio-x: varredura subindo + bipe
        t = tt(1.1)
        sw = np.sin(2 * np.pi * np.cumsum(400 + 1400 * (t / 1.1)) / SR) * np.sin(np.pi * t / 1.1) ** 2
        ns = bp(RNG.normal(0, 1, len(t)), 2000, 8000) * np.sin(np.pi * t / 1.1) ** 2 * 0.3
        bip = np.zeros(len(t))
        tb = tt(0.08)
        put(bip, 0.95, np.sin(2 * np.pi * 1760 * tb) * np.exp(-tb * 30))
        return nrm(0.5 * sw + ns + 0.7 * bip) * 0.6
    if nome == "bateria":  # bateria fraca: dois bipes descendo
        out = np.zeros(int(0.7 * SR))
        t = tt(0.16)
        for i, f in enumerate((660, 440)):
            sq = np.sign(np.sin(2 * np.pi * f * t)) * 0.4 + np.sin(2 * np.pi * f * t)
            put(out, i * 0.24, lp(sq, 3000) * np.exp(-t * 12) * np.minimum(1, t / 0.004))
        return nrm(out) * 0.6
    if nome == "fantasma":  # a tela antiga acendendo: brilho de vidro subindo
        out = np.zeros(int(1.6 * SR))
        t = tt(1.0)
        for i, m in enumerate([81, 85, 88, 93, 97]):
            put(out, i * 0.06, np.sin(2 * np.pi * note(m) * t) * np.exp(-t * 4))
        g = bp(RNG.normal(0, 1, len(out)), 3000, 9000) * np.exp(-np.arange(len(out)) / SR * 6) * 0.25
        return nrm(out + g) * 0.55
    if nome == "falha":  # glitch digital apagando
        out = np.zeros(int(0.5 * SR))
        for k in range(7):
            t = tt(RNG.uniform(0.015, 0.04))
            f = RNG.choice([180, 360, 720, 1400])
            put(out, k * 0.055, np.sign(np.sin(2 * np.pi * f * t)) * RNG.uniform(0.4, 1))
        t = tt(0.3)
        put(out, 0.38, np.sin(2 * np.pi * np.cumsum(900 * np.exp(-t * 12) + 60) / SR) * np.exp(-t * 10))
        return nrm(lp(out, 6000)) * 0.45
    if nome == "whoosh":  # câmera recuando
        d = 2.4
        t = tt(d)
        env_ = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 1.5
        x = RNG.normal(0, 1, len(t))
        lo, hi = lp(x, 500), lp(x, 2500)
        k = t / d
        return nrm((lo * (1 - k) + hi * k) * env_) * 0.6
    if nome == "pulo":  # Lume pulando: "boing" curto subindo
        t = tt(0.22)
        f = 260 + 520 * (t / 0.22) ** 0.6
        return nrm(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * np.minimum(1, t / 0.004)) * 0.45
    if nome == "pouso":  # pouso fofo
        t = tt(0.25)
        th = np.sin(2 * np.pi * np.cumsum(140 * np.exp(-t * 12) + 60) / SR) * np.exp(-t * 18)
        return nrm(th + 0.15 * lp(RNG.normal(0, 1, len(t)), 1200) * np.exp(-t * 30)) * 0.55
    if nome == "brilho":  # aceno: cintilado
        out = np.zeros(int(1.0 * SR))
        t = tt(0.5)
        for i, m in enumerate([86, 90, 93, 98, 93, 98]):
            put(out, i * 0.07, np.sin(2 * np.pi * note(m) * t) * np.exp(-t * 10))
        return nrm(out) * 0.4
    if nome == "pop":
        t = tt(0.14)
        return nrm(np.sin(2 * np.pi * note(81) * t * (1 + 0.2 * np.exp(-t * 60))) * np.exp(-t * 30)) * 0.45
    if nome == "transicao":  # whoosh curto entre partes
        d = 0.7
        t = tt(d)
        x = RNG.normal(0, 1, len(t))
        k = t / d
        return nrm((lp(x, 700) * (1 - k) + lp(x, 3000) * k) * np.sin(np.pi * k) ** 2) * 0.35
    if nome == "tique":  # relógio acelerando
        out = np.zeros(int(2.2 * SR))
        tc, k = 0.0, 0
        while tc < 2.0:
            tb = tt(0.03)
            put(out, tc, hp(RNG.normal(0, 1, len(tb)), 3000) * np.exp(-tb * 200) * (1.0 if k % 2 == 0 else 0.6))
            tc += max(0.05, 0.28 * (1 - tc / 2.2))
            k += 1
        return nrm(out) * 0.5
    if nome == "rachar":  # rachadura no concreto
        out = np.zeros(int(0.6 * SR))
        for k in range(9):
            tb = tt(0.02)
            put(out, k * 0.05 + RNG.uniform(0, 0.02), hp(RNG.normal(0, 1, len(tb)), 1500) * np.exp(-tb * 150) * RNG.uniform(0.4, 1))
        tb = tt(0.4)
        put(out, 0.0, np.sin(2 * np.pi * np.cumsum(120 * np.exp(-tb * 8) + 40) / SR) * np.exp(-tb * 12) * 0.6)
        return nrm(out) * 0.55
    if nome == "desabar":  # estrondo de prédio caindo (abafado, sem violência)
        t = tt(1.6)
        x = lp(RNG.normal(0, 1, len(t)), 300) * np.exp(-t * 2.2) * np.minimum(1, t / 0.05)
        th = np.sin(2 * np.pi * np.cumsum(60 * np.exp(-t * 3) + 30) / SR) * np.exp(-t * 4)
        return nrm(x + th) * 0.6
    if nome == "agua":  # água correndo / pingando
        t = tt(2.5)
        x = bp(RNG.normal(0, 1, len(t)), 400, 2500) * (0.5 + 0.5 * np.sin(2 * np.pi * 1.3 * t)) * np.sin(np.pi * t / 2.5)
        out = x * 0.4
        for k in range(10):
            tb = tt(0.12)
            f0 = RNG.uniform(600, 1400)
            put(out, RNG.uniform(0, 2.3), np.sin(2 * np.pi * np.cumsum(f0 + 900 * tb / 0.12) / SR) * np.exp(-tb * 30) * 0.5)
        return nrm(out) * 0.45
    if nome == "carimbo":  # carimbo batendo
        t = tt(0.5)
        th = np.sin(2 * np.pi * np.cumsum(90 * np.exp(-t * 20) + 50) / SR) * np.exp(-t * 16)
        clk = bp(RNG.normal(0, 1, len(t)), 800, 4000) * np.exp(-t * 60)
        return nrm(th + 0.7 * clk) * 0.7
    if nome == "maquina":  # máquina de escrever (~1,2 s de teclas)
        out = np.zeros(int(1.4 * SR))
        tc = 0.0
        while tc < 1.2:
            tb = tt(0.04)
            put(out, tc, bp(RNG.normal(0, 1, len(tb)), 1200, 6000) * np.exp(-tb * 120) * RNG.uniform(0.5, 1))
            put(out, tc + 0.005, np.sin(2 * np.pi * 180 * tb) * np.exp(-tb * 80) * 0.4)
            tc += RNG.uniform(0.07, 0.13)
        return nrm(out) * 0.45
    if nome == "fogo":  # fogueira estalando
        t = tt(3.0)
        out = lp(RNG.normal(0, 1, len(t)), 900) * 0.25 * np.sin(np.pi * t / 3.0)
        for k in range(30):
            tb = tt(0.015)
            put(out, RNG.uniform(0, 2.9), hp(RNG.normal(0, 1, len(tb)), 2000) * np.exp(-tb * 300) * RNG.uniform(0.3, 1))
        return nrm(out) * 0.45
    if nome == "cogumelo":  # explosão distante e abafada
        t = tt(1.8)
        x = lp(RNG.normal(0, 1, len(t)), 220) * np.exp(-t * 2.5) * np.minimum(1, t / 0.02)
        return nrm(x) * 0.5
    if nome == "radio":  # chiado de rádio varrendo estações
        t = tt(2.0)
        ns = bp(RNG.normal(0, 1, len(t)), 1500, 5000) * 0.4
        tom = np.sin(2 * np.pi * np.cumsum(500 + 400 * np.sin(2 * np.pi * 0.7 * t)) / SR) * 0.3 * (np.sin(2 * np.pi * 3 * t) > 0.3)
        return nrm((ns + tom) * np.sin(np.pi * t / 2.0)) * 0.4
    if nome == "broca":  # sonda perfurando
        t = tt(2.0)
        x = (saw(95, t) + 0.5 * saw(190.5, t)) * (0.7 + 0.3 * np.sin(2 * np.pi * 7 * t))
        return nrm(lp(x, 1500) * np.minimum(1, t / 0.1) * np.minimum(1, (2.0 - t) / 0.3)) * 0.35
    # ---- vídeo 02 (celulares)
    if nome == "vibra":  # celular vibrando: dois zumbidos graves
        out = np.zeros(int(1.0 * SR))
        t = tt(0.32)
        z = (saw(150, t) * (0.6 + 0.4 * np.sin(2 * np.pi * 30 * t))) * np.minimum(1, t / 0.01) * np.minimum(1, (0.32 - t) / 0.03)
        put(out, 0.0, lp(z, 900))
        put(out, 0.5, lp(z, 900))
        return nrm(out) * 0.5
    if nome == "ding":  # notificação: dois tons claros
        out = np.zeros(int(0.9 * SR))
        t = tt(0.6)
        for i, m in enumerate([88, 93]):
            put(out, i * 0.11, (np.sin(2 * np.pi * note(m) * t) + 0.3 * np.sin(4 * np.pi * note(m) * t)) * np.exp(-t * 7))
        return nrm(out) * 0.45
    if nome == "rolos":  # máquina de apostas: rolos girando e parando
        out = np.zeros(int(1.6 * SR))
        tc, k = 0.0, 0
        while tc < 1.3:
            tb = tt(0.02)
            put(out, tc, bp(RNG.normal(0, 1, len(tb)), 1500, 5000) * np.exp(-tb * 200))
            tc += 0.04 + 0.1 * (tc / 1.3) ** 2
            k += 1
        tb = tt(0.4)
        put(out, 1.35, np.sin(2 * np.pi * note(84) * tb) * np.exp(-tb * 8))
        return nrm(out) * 0.45
    if nome == "moeda":  # moedinha caindo
        out = np.zeros(int(0.5 * SR))
        t = tt(0.35)
        for i, m in enumerate([96, 100]):
            put(out, i * 0.06, np.sin(2 * np.pi * note(m) * t) * np.exp(-t * 14))
        return nrm(out) * 0.35
    raise ValueError(nome)


def ler_wav(path, dur):
    with wave.open(str(path)) as w:
        sr, ch = w.getframerate(), w.getnchannels()
        x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    if ch > 1:
        x = x.reshape(-1, ch).mean(1)
    if sr != SR:
        x = np.interp(np.arange(int(len(x) * SR / sr)) / SR, np.arange(len(x)) / sr, x)
    n = int(dur * SR)
    return np.pad(x[:n], (0, max(0, n - len(x))))


def ducking(voz, prof=0.6):
    """ganho da trilha: abaixa quando a voz fala (ataque rápido, soltura lenta)"""
    hop = SR // 100
    r = np.sqrt(np.convolve(voz ** 2, np.ones(hop) / hop, mode="same"))
    r = np.clip(r / (np.percentile(r, 90) + 1e-9), 0, 1)
    g = np.empty_like(r)
    a, rel, v = 1 - np.exp(-1 / (0.03 * SR)), 1 - np.exp(-1 / (0.45 * SR)), 0.0
    for i, x in enumerate(r[::hop]):  # passo de 10 ms
        v += (x - v) * (a * hop if x > v else rel * hop)
        g[i * hop:(i + 1) * hop] = v
    return 1 - prof * np.clip(g, 0, 1)


def mixar(video_mudo, voz_wav, saida, dur, revela, fim, eventos, g_trilha=0.26, g_fx=0.42, salvar_stems=None):
    voz = ler_wav(voz_wav, dur)
    fade = np.minimum(1, np.maximum(0, dur - np.arange(len(voz)) / SR) / 0.6)
    voz *= fade
    mus = trilha(dur, revela, fim) * ducking(voz)[:, None]
    fxb = np.zeros(len(voz))
    for t, nome in eventos:
        put(fxb, t, fx(nome))
    fxs = reverb(fxb, 1.6, 0.22, seed=5)
    mix = np.stack([voz, voz], 1) + g_trilha * mus + g_fx * fxs
    mix = nrm(mix, 0.95) if np.max(np.abs(mix)) > 0.95 else mix
    if salvar_stems:
        for nome, x in (("trilha", mus), ("efeitos", fxs)):
            _grava(f"{salvar_stems}/{nome}.wav", x)
    tmp = str(saida) + ".mix.wav"
    _grava(tmp, mix)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video_mudo), "-i", tmp, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", str(saida)], check=True)
    import os
    os.remove(tmp)


def _grava(path, st):
    x = np.clip(st, -1, 1)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


TRACKS = ("pad", "escuro", "arp", "baixo", "kick", "shk", "glock")


def trilha_secoes(dur, pontos, sinos=(), subidas=()):
    """trilha longa: pontos = [(t, dict(pad=, escuro=, arp=, baixo=, kick=, shk=, glock=)), ...] (interpolados);
    sinos = tempos do acorde de sino; subidas = tempos em que uma subida termina (2 s antes)"""
    N = int(dur * SR)
    pad, arp, baixo = _pad(N), _arp(N), _baixo(N)
    kick, shk = _ritmo(N)
    glock = _glock(N, 0.5, dur, every=2.4)
    ts = [p[0] for p in pontos]
    g = {k: env(N, [(t, d.get(k, 0.0)) for t, d in pontos]) for k in TRACKS}
    pad = lp(pad, 700) * g["escuro"] + lp(pad, 2600) * (1 - g["escuro"]) * 0.6
    mono = (0.30 * nrm(pad) * g["pad"] + 0.26 * nrm(arp) * g["arp"] + 0.34 * nrm(baixo) * g["baixo"] +
            0.30 * nrm(kick) * g["kick"] + 0.07 * nrm(shk) * g["shk"] + 0.16 * nrm(glock) * g["glock"])
    for t in subidas:
        put(mono, t - 2.0, nrm(_subida(2.0)), 0.16)
    for t in sinos:
        put(mono, t, nrm(_sino()), 0.30)
    st = reverb(mono, 2.8, 0.32)
    d = int(BEAT * 0.75 * SR)
    eco = np.concatenate([np.zeros(d), (0.26 * nrm(arp) * g["arp"])[:-d]])
    st[:, 0] += 0.35 * eco
    st[:, 1] += 0.35 * np.concatenate([np.zeros(d), eco[:-d]])
    return nrm(st, 0.9)


def mixar_trilha(video_mudo, voz_wav, saida, dur, mus, eventos, g_trilha=0.26, g_fx=0.42, salvar_stems=None):
    """como mixar(), mas com a trilha já pronta (trilha_secoes)"""
    voz = ler_wav(voz_wav, dur)
    mus = mus[:len(voz)] * ducking(voz)[:, None]
    fxb = np.zeros(len(voz))
    for t, nome in eventos:
        put(fxb, t, fx(nome))
    fxs = reverb(fxb, 1.6, 0.22, seed=5)
    mix = np.stack([voz, voz], 1) + g_trilha * mus + g_fx * fxs
    mix = nrm(mix, 0.95) if np.max(np.abs(mix)) > 0.95 else mix
    if salvar_stems:
        for nome, x in (("trilha", mus), ("efeitos", fxs)):
            _grava(f"{salvar_stems}/{nome}.wav", x)
    tmp = str(saida) + ".mix.wav"
    _grava(tmp, mix)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video_mudo), "-i", tmp, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", str(saida)], check=True)
    import os
    os.remove(tmp)
