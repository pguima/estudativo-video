"""Som do episódio: voz + trilha + efeitos + ambiente, tudo sintetizado aqui (livre de direitos).

    py video/som.py ep01-ai-bubble            gera os stems, mixa e monta <ep>.mp4 e <ep>.srt
    py video/som.py ep01-ai-bubble --so-som   só os stems e a mixagem (sem o vídeo)

Entradas: output/planos.json (render.py), audio/tempos.json (alinhar.py), audio/*.wav (voz.py) e
episodes/<ep>/trilha.json (o que toca em cada parte da história e efeitos pontuais).
Saídas: som/voz.wav, som/trilha.wav, som/efeitos.wav, som/mix.wav, output/<ep>.mp4, output/<ep>.srt

Efeitos automáticos, pelos eventos dos planos: transição (whoosh), impacto/carimbo (hits), cartão de dia,
mudança do painel, gráfico entrando, batimento (mesmo pulso da imagem quando stress > 75) e ambiente por cenário.
"""
import argparse
import json
import math
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / '_ferramentas'))
from scipy.signal import butter, sosfilt  # noqa: E402
from som_antigos import SR, bp, ducking, hp, lp, note, nrm, put, reverb, saw, tt  # noqa: E402

RNG = np.random.default_rng(2026)
BEAT = 60 / 112
BAR = BEAT * 4
LEAD, LEAD_FALA = 0.12, 0.15
TRANS_EARLY = 0.14
AMB = {'trading_floor': 'pregao', 'street': 'rua', 'house_exterior': 'rua', 'datacenter_site': 'vento', 'datacenter_closed': 'vento',
       'kitchen': 'casa', 'living_room': 'casa', 'bedroom_kids': 'casa', 'bedroom_parents': 'casa', 'garage': 'casa',
       'hospital': 'hospital', 'school': 'murmurio', 'office': 'escritorio', 'supermarket': 'murmurio'}
GAMB = {'pregao': 0.34, 'rua': 0.13, 'vento': 0.15, 'casa': 0.05, 'hospital': 0.06, 'murmurio': 0.14, 'escritorio': 0.07}


def st(x, pan=0.0):
    """mono → estéreo (n, 2)"""
    a = (pan + 1) * math.pi / 4
    return np.stack([x * math.cos(a), x * math.sin(a)], 1) * 1.414


def env_ar(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    e[:na] = np.linspace(0, 1, na) ** 2
    e[-nr:] *= np.linspace(1, 0, nr) ** 2
    return e


# ------------------------------------------------------------------ instrumentos
# Tema original do canal, em linguagem de trailer: ostinato de cordas, metais, coro, tambores. Ré menor, 112 BPM.
HEROI = [[38, 57, 62, 65], [34, 58, 62, 65], [41, 57, 60, 65], [36, 55, 60, 64]]   # Dm Bb F C
LUZ = [[41, 57, 60, 65], [36, 55, 60, 64], [38, 57, 62, 65], [34, 58, 62, 65]]     # F C Dm Bb (mesma grade, abre para a esperança)
TEMA = [(62, 3), (69, 1), (69, 2), (67, 1), (69, 1),  (70, 3), (69, 1), (67, 2), (65, 2),
        (65, 3), (69, 1), (72, 2), (70, 1), (69, 1),  (67, 3), (72, 1), (72, 4)]   # (nota, tempos); 32 tempos = 8 compassos


def g_metal(notas, d=None):
    d = d or BAR * 2 + 1.3
    t = tt(d)
    x = np.zeros(len(t))
    for n in notas + [notas[0] + 12]:
        for det in (0.996, 1.0, 1.005):
            x += saw(note(n) * det, t + RNG.random())
    brilho = np.clip(t / 0.22, 0, 1) * (0.5 + 0.5 * np.exp(-t * 1.5))
    x = lp(x, 520, 2) * (1 - brilho) + lp(x, 2600, 2) * brilho
    x = np.tanh(x / np.max(np.abs(x)) * 2.2) * env_ar(len(t), 0.07, 0.7)
    return np.float32(reverb(nrm(x, 0.7), 2.4, 0.3))


def g_trompa(m, d):
    t = tt(d + 0.9)
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.1 * t) * np.clip((t - 0.25) / 0.3, 0, 1)
    fase = np.cumsum(note(m) * vib) / SR
    x = saw(1, fase) + 0.5 * (2 * np.abs(saw(1, fase * 0.5)) - 1) + 0.55 * saw(1, fase * 0.5 + 0.13)
    x = lp(x, 1900, 2) * env_ar(len(t), 0.05, 0.75)
    return np.float32(reverb(nrm(x, 0.8), 2.4, 0.34))


def g_coro(notas):
    d = BAR * 2 + 2.0
    t = tt(d)
    x = np.zeros(len(t))
    for n in notas[1:] + [notas[1] + 12]:
        for det in (0.997, 1.004):
            f = note(n) * det * (1 + 0.003 * np.sin(2 * np.pi * (4.6 + det) * t))
            x += saw(1, np.cumsum(f) / SR + RNG.random())
    x = bp(x, 520, 900) + 0.6 * bp(x, 1050, 1450) + 0.22 * bp(x, 2300, 2950)   # formantes de "ah"
    return np.float32(reverb(nrm(x * env_ar(len(t), 0.7, 1.4), 0.6), 3.4, 0.5))


def g_spic(m):
    t = tt(0.17)
    f = note(m)
    x = saw(f, t) + saw(f * 1.006, t + 0.1) * 0.7 + saw(f * 0.995, t + 0.2) * 0.5
    return np.float32(st(lp(x, 3000) * np.exp(-t * 13) * env_ar(len(t), 0.002, 0.02)))


def g_baixo(m):
    t = tt(0.26)
    f = note(m)
    x = lp(saw(f, t), 300) + np.sin(2 * np.pi * f * t) * 0.9
    return np.float32(st(x * np.exp(-t * 6) * env_ar(len(t), 0.003, 0.03)))


def g_piano(n):
    t = tt(2.8)
    f = note(n)
    x = sum(np.sin(2 * np.pi * f * k * (1 + 0.0004 * k * k) * t) * np.exp(-t * (1.0 + 0.6 * k)) / k ** 1.1 for k in range(1, 9))
    x += lp(RNG.normal(0, 1, len(t)), 3000) * np.exp(-t * 90) * 0.12
    return np.float32(reverb(nrm(x * env_ar(len(t), 0.002, 0.2), 0.8), 2.2, 0.26))


def g_tick(alto):
    t = tt(0.05)
    r = np.sin(2 * np.pi * (2700 if alto else 2050) * t) * np.exp(-t * 300)
    x = r * 0.7 + bp(RNG.normal(0, 1, len(t)), 1800, 7000) * np.exp(-t * 500) * 0.9
    return np.float32(st(nrm(x, 0.8), 0.18 if alto else -0.18))


def g_taiko(f0=56):
    t = tt(1.3)
    f = f0 + 110 * np.exp(-t * 26)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 4.6)
    x += lp(RNG.normal(0, 1, len(t)), 1100) * np.exp(-t * 34) * 0.6
    return np.float32(reverb(nrm(x, 0.9), 2.0, 0.28))


def g_caixa():
    t = tt(0.32)
    x = bp(RNG.normal(0, 1, len(t)), 1400, 7500) * np.exp(-t * 20) + np.sin(2 * np.pi * 196 * t) * np.exp(-t * 34) * 0.7
    return np.float32(reverb(nrm(x, 0.8), 0.9, 0.2))


def g_prato(d=3.6):
    t = tt(d)
    x = hp(RNG.normal(0, 1, len(t)), 3800) * np.exp(-t * 1.5) * env_ar(len(t), 0.002, 0.4)
    return np.float32(np.stack([x, np.roll(x, 211)], 1) * 0.7)


def sequencia(dur, inicio_ciclo):
    """faixas soltas, cada uma com a duração do episódio. Tudo cai na mesma grade, e um ciclo de 8 compassos começa
    exatamente em inicio_ciclo (o cartão final), para o tema entrar na cabeça do compasso."""
    n = int(dur * SR) + SR * 8
    ciclo = BAR * 8
    zero = inicio_ciclo % ciclo - ciclo
    passos = lambda p: [(k, zero + k * p) for k in range(int((dur - zero) / p) + 1)]
    vazio = lambda: np.zeros((n, 2), np.float32)
    rng = np.random.default_rng(7)
    acorde = lambda t, prog: prog[int(((t - zero) / (BAR * 2)) % 4)]
    PAT = [0, 12, 0, 7, 12, 0, 7, 0, 0, 12, 0, 7, 12, 19, 12, 7]

    def cordas(prog, oit):
        cache = {}
        b = vazio()
        for k, t in passos(BEAT / 4):
            m = acorde(t + 0.001, prog)[0] + oit + PAT[k % 16]
            cache.setdefault(m, g_spic(m))
            put(b, t, cache[m], 1.0 if k % 4 == 0 else 0.62 + 0.14 * (k % 2))
        return b

    def baixo():
        cache = {}
        b = vazio()
        for k, t in passos(BEAT / 2):
            m = acorde(t + 0.001, HEROI)[0] + (12 if k % 4 == 3 else 0)
            cache.setdefault(m, g_baixo(m))
            put(b, t, cache[m], 1.0 if k % 2 == 0 else 0.7)
        return b

    def blocos(prog, grao):
        gs = [grao(c) for c in prog]
        b = vazio()
        for k, t in passos(BAR * 2):
            put(b, t, gs[k % 4])
        return b

    def tema(oit):
        cache = {}
        b = vazio()
        for c in range(int((dur - zero) / ciclo) + 1):
            t = zero + c * ciclo
            for m, q in TEMA:
                d = q * BEAT
                chave = (m + oit, q)
                cache.setdefault(chave, g_trompa(m + oit, d))
                put(b, t, cache[chave])
                t += d
        return b

    def piano():
        cache = {}
        b = vazio()
        ARP = [0, 1, 2, 3, 2, 1, 3, 2]
        for k, t in passos(BEAT / 2):
            c = acorde(t + 0.001, LUZ)
            m = c[1 + ARP[k % 8] % 3] + 12 * (1 + (ARP[k % 8] == 3))
            cache.setdefault(m, g_piano(m))
            put(b, t + rng.normal(0, 0.005), cache[m], 0.5 + 0.3 * (k % 4 == 0) + rng.random() * 0.15)
        return b

    def tambores():
        b = vazio()
        g, g2 = g_taiko(), g_taiko(92)
        PAD = [1, 0, 0, .6, 0, 0, .8, 0, 1, 0, .55, 0, .8, 0, .55, .6]
        for k, t in passos(BEAT / 4):
            compasso = (k // 16) % 8
            if compasso == 7 and k % 16 >= 8:                 # virada para o próximo ciclo
                put(b, t, g2, 0.45 + 0.55 * (k % 16 - 8) / 8)
            elif PAD[k % 16]:
                put(b, t, g, PAD[k % 16])
        return b

    def caixa():
        b = vazio()
        g = g_caixa()
        for k, t in passos(BEAT / 4):
            compasso = (k // 16) % 8
            if compasso == 7:
                put(b, t, g, 0.3 + 0.7 * (k % 16) / 16)       # rufo que sobe
            elif k % 8 == 4 or k % 16 in (14, 15):
                put(b, t, g, 0.8 if k % 8 == 4 else 0.45)
        return b

    def pratos():
        b = vazio()
        g = g_prato()
        sobe = g_prato(BAR)[::-1].copy()
        for k, t in passos(BAR * 4):
            put(b, t, g)
            put(b, t - BAR, sobe, 0.55)
        return b

    def tick():
        b = vazio()
        g0, g1 = g_tick(True), g_tick(False)
        for k, t in passos(BEAT):
            put(b, t, g0 if k % 2 == 0 else g1)
        return b

    yield 'cordas', 0.15, lambda: cordas(HEROI, 12)
    yield 'luz', 0.13, lambda: cordas(LUZ, 12)
    yield 'baixo', 0.20, baixo
    yield 'metal', 0.20, lambda: blocos(HEROI, g_metal)
    yield 'tema', 0.27, lambda: tema(0)
    yield 'alto', 0.22, lambda: tema(12)
    yield 'coro', 0.17, lambda: blocos(HEROI, g_coro)
    yield 'piano', 0.30, piano
    yield 'taiko', 0.36, tambores
    yield 'caixa', 0.10, caixa
    yield 'prato', 0.12, pratos
    yield 'tick', 0.09, tick


def trilha(dur, pontos, inicio_ciclo):
    n = int(dur * SR)
    pontos = sorted(pontos, key=lambda p: p[0])
    mus = np.zeros((n, 2), np.float32)
    ctl = np.arange(0, dur + 1, 0.05)
    for nome, ganho, faz in sequencia(dur, inicio_ciclo):
        alvo = np.zeros(len(ctl))
        for (t0, v), t1 in zip(pontos, [p[0] for p in pontos[1:]] + [dur + 1]):
            alvo[(ctl >= t0) & (ctl < t1)] = v.get(nome, 0)
        k = 2
        alvo = np.convolve(np.pad(alvo, k, mode='edge'), np.ones(2 * k + 1) / (2 * k + 1), mode='valid')[:len(ctl)]  # troca em ~0,25 s
        if alvo.max() == 0:
            continue
        faixa = faz()[:n]
        e = np.float32(np.interp(np.arange(n) / SR, ctl, alvo))
        mus += faixa * e[:, None] * ganho
        del faixa
        print('  trilha', nome, flush=True)
    return mus


# ------------------------------------------------------------------ efeitos
def fx_whoosh(d=0.42, baixo=False):
    t = tt(d)
    e = np.sin(np.pi * t / d) ** 2.4
    a, b = (lp(RNG.normal(0, 1, len(t)), 700), lp(RNG.normal(0, 1, len(t)), 2600))
    x = (a * (1 - t / d) + b * (t / d) * (0.35 if baixo else 1)) * e
    if baixo:
        x = x + np.sin(2 * np.pi * np.cumsum(60 + 110 * t / d) / SR) * e * 0.5
    p = np.stack([x * (1 - t / d), x * (t / d)], 1) * 1.4
    return nrm(p, 0.8)


def fx_impacto():
    t = tt(1.9)
    f = 34 + 75 * np.exp(-t * 9)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.6) + lp(RNG.normal(0, 1, len(t)), 3200) * np.exp(-t * 26) * 0.6
    return reverb(nrm(x, 0.9), 2.2, 0.32)


def fx_baque():
    t = tt(0.7)
    f = 44 + 70 * np.exp(-t * 18)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7.5) + lp(RNG.normal(0, 1, len(t)), 1200) * np.exp(-t * 60) * 0.3
    return st(nrm(x, 0.9))


def fx_carimbo():
    t = tt(0.5)
    x = bp(RNG.normal(0, 1, len(t)), 280, 2200) * np.exp(-t * 62) + np.sin(2 * np.pi * 130 * t) * np.exp(-t * 26) * 0.9
    return reverb(nrm(x, 0.9), 0.6, 0.18)


def fx_tom(notas, d=0.085, tipo='sen'):
    x = np.zeros(0)
    for f in notas:
        t = tt(d)
        w = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t)
        x = np.concatenate([x, w * env_ar(len(t), 0.004, 0.035)])
    return st(nrm(x, 0.7))


def fx_sino():
    """sino de abertura do pregão: martelo elétrico"""
    t = tt(2.6)
    x = sum(np.sin(2 * np.pi * f * t) * g * np.exp(-t * q) for f, g, q in ((1330, 1, 1.3), (2210, 0.6, 1.8), (3550, 0.4, 2.6), (5120, 0.2, 4)))
    x *= 0.55 + 0.45 * np.sign(np.sin(2 * np.pi * 19 * t)) * (t < 2.1) + (t >= 2.1) * 0.45
    return reverb(nrm(x * env_ar(len(t), 0.003, 0.3), 0.7), 1.6, 0.3)


def fx_vibra(vezes=2):
    x = np.zeros(int(SR * (vezes * 0.62)))
    t = tt(0.42)
    z = (np.sign(np.sin(2 * np.pi * 172 * t)) * 0.7 + np.sin(2 * np.pi * 344 * t) * 0.4) * env_ar(len(t), 0.01, 0.02)
    for k in range(vezes):
        put(x, k * 0.62, z)
    return st(nrm(lp(x, 1000), 0.7))


def fx_toque(vezes=2):
    x = np.zeros(int(SR * vezes * 1.5))
    t = tt(0.95)
    z = (np.sin(2 * np.pi * 440 * t) + np.sin(2 * np.pi * 480 * t)) * (0.6 + 0.4 * np.sin(2 * np.pi * 20 * t)) * env_ar(len(t), 0.01, 0.05)
    for k in range(vezes):
        put(x, k * 1.5, z)
    return st(nrm(bp(x, 350, 2200), 0.6))


def fx_coracao():
    x = np.zeros(int(SR * 0.6))
    for t0, f, g, q in ((0, 58, 1, 16), (0.24, 46, 0.72, 12)):
        t = tt(0.3)
        put(x, t0, np.sin(2 * np.pi * f * t) * np.exp(-t * q) * np.sin(np.minimum(t * 90, np.pi / 2)), g)
    return st(nrm(x, 0.9))


def fx_tique_dia():
    a, b = np.array(g_tick(True), float), np.array(g_tick(False), float)
    x = np.zeros((int(SR * 1.3), 2))
    put(x, 0.0, b * 0.9)
    put(x, 0.0, fx_baque() * 0.8)
    put(x, 0.5, a * 0.8)
    put(x, 1.0, b * 0.7)
    return x


def fx_sting():
    t = tt(4.2)
    x = sum(saw(note(n) * d, t) for n, d in ((26, 1), (26, 1.008), (38, 0.996), (45, 1.004), (50, 1.0)))
    x = lp(np.tanh(x * 0.8), 620, 3) * np.exp(-t * 1.0) * env_ar(len(t), 0.02, 1)
    return reverb(nrm(x, 0.9), 3, 0.35)


def fx_final():
    """acorde de dominante (Lá) que não resolve: o episódio termina em suspenso"""
    x = np.array(g_metal([33, 57, 61, 64], 1.1), float)
    x = np.pad(x, ((0, SR), (0, 0)))
    t = np.array(g_taiko(), float)
    x[:len(t)] += t
    return x


def fx_subida(d=2.4):
    t = tt(d)
    x = np.zeros(len(t))
    r = RNG.normal(0, 1, len(t))
    for k in range(6):                                   # filtro abrindo em blocos que se cruzam
        a, b = k / 6 * d, (k + 2) / 6 * d
        j = (t >= a) & (t < b)
        x[j] += lp(r[j], 300 * 1.9 ** k) * np.sin(np.pi * (t[j] - a) / (b - a))
    return st(nrm(x * (t / d) ** 2, 0.7))


def loops():
    """ambientes de 12 s; o filtro é circular, então emendam sem clique"""
    n = 12 * SR
    t = np.arange(n) / SR
    per = lambda f, fase=0.0: 0.5 + 0.5 * np.sin(2 * np.pi * round(f * 12) / 12 * t + fase)
    r = lambda: RNG.normal(0, 1, n)
    out = {}

    def fala(nvozes):
        x = np.zeros(n)
        for k in range(nvozes):
            f0, f1 = 300 + k * 90, 900 + k * 170
            x += bp(r(), f0, f1) * per(2.3 + k * 0.37, k) * per(0.61 + k * 0.13, 2 * k)
        return nrm(x, 0.5)
    for nome, faz in {
        'pregao': lambda: fala(9) + lp(r(), 240) * 0.2,
        'murmurio': lambda: fala(5) * 0.7 + lp(r(), 200) * 0.12,
        'rua': lambda: nrm(bp(r(), 120, 900) * (0.5 + 0.5 * per(0.083)), 0.5),
        'vento': lambda: nrm(bp(r(), 160, 1300) * (0.25 + 0.75 * per(0.17)), 0.55),
        'casa': lambda: nrm(lp(r(), 260) + np.sin(2 * np.pi * 60 * t) * 0.8 * np.std(lp(r(), 260)), 0.5),
        'hospital': lambda: nrm(lp(r(), 420), 0.45),
        'escritorio': lambda: nrm(bp(r(), 150, 1500), 0.4),
    }.items():
        out[nome] = np.float32(np.stack([faz(), np.roll(faz(), SR // 3)], 1))
    return out


def efeitos(pl, dur, voz_js, cfg):
    n = int(dur * SR)
    b = np.zeros((n, 2), np.float32)
    lista = dict(whoosh=fx_whoosh(), zoom=fx_whoosh(0.55, True), impacto=fx_impacto(), baque=fx_baque(), carimbo=fx_carimbo(),
                 desce=fx_tom([620, 415]), sobe=fx_tom([523, 784]), dados=fx_tom([1760, 2093, 1760], 0.05), caixa=fx_tom([2350], 0.09),
                 sino=fx_sino(), vibra=fx_vibra(), toque=fx_toque(), coracao=fx_coracao(), dia=fx_tique_dia(), sting=fx_sting(), subida=fx_subida(), final=fx_final(), crash=np.array(g_prato(), float),
                 tique=np.array(g_tick(True), float), tambor=np.array(g_taiko(), float))
    amb = loops()
    GG = dict(whoosh=0.30, zoom=0.34, impacto=0.75, baque=0.46, carimbo=0.62, desce=0.13, sobe=0.13, dados=0.05, caixa=0.12,
              sino=0.28, vibra=0.30, toque=0.2, coracao=0.42, dia=0.5, sting=0.8, subida=0.34, final=0.9, crash=0.3, tique=0.34, tambor=0.8)
    bip = 0
    painel = {}
    for s in pl:
        t0, d = s['start'], s['dur']
        if s['tin'] in ('whip', 'zoom'):
            put(b, t0 - TRANS_EARLY, lista['whoosh' if s['tin'] == 'whip' else 'zoom'], GG['whoosh' if s['tin'] == 'whip' else 'zoom'])
        if s['card']:
            put(b, t0, lista['dia'], GG['dia'])
        if s['gfx'] and not s['bg']:
            put(b, t0 + 0.28, lista['dados'], GG['dados'])
        for h in s['hits']:
            t = t0 + h['t']
            if h['stamp']:
                put(b, t, lista['carimbo'], GG['carimbo'])
            if h['flash'] and h['shake']:
                put(b, t, lista['impacto'], GG['impacto'])
            elif h['shake'] or h['punch']:
                put(b, t, lista['baque'], GG['baque'] * (1 if h['shake'] else 0.6))
        if s['hud']:
            cai = any(k == 'cash' and v < painel.get('cash', v) for k, v in s['hud'].items() if isinstance(v, (int, float))) or s['hud'].get('stress', 0) > painel.get('stress', 100)
            painel.update(s['hud'])
            put(b, t0 + s['hudAt'], lista['desce' if cai else 'sobe'], GG['desce'])
        if s['stress'] > 75 and not s['card']:                    # mesmo pulso de camera.js: sin(t * 5.2) ^ 12
            forca = min(1, (s['stress'] - 75) / 25)
            k = 0
            while True:
                t = (math.pi / 2 + 2 * math.pi * k) / 5.2
                if t > d - 0.3:
                    break
                put(b, t0 + t - 0.05, lista['coracao'], GG['coracao'] * (0.4 + 0.6 * forca))
                k += 1
        nome = AMB.get(s['bg'])
        if nome:
            bip += 1
            a = int(t0 * SR)
            m = min(int(d * SR), n - a)
            of = (bip * 31337) % (amb[nome].shape[0] - 1)
            trecho = np.take(amb[nome], np.arange(of, of + m) % amb[nome].shape[0], axis=0)
            e = np.float32(env_ar(m, min(0.25, d / 3), min(0.25, d / 3)))
            b[a:a + m] += trecho * e[:, None] * GAMB[nome]
            if nome == 'hospital':
                for k in range(int(d / 1.15)):
                    put(b, t0 + 0.3 + k * 1.15, lista['caixa'], 0.05)
    ini = {s['id']: s for s in pl}
    for ev in cfg['eventos']:
        s = ini[ev['plano']]
        t = s['start'] + ev.get('t', 0)
        if 'palavra' in ev:
            ws = voz_js[s['id']]['wt']
            t = s['start'] + next(x[1] for x in ws if x[0].startswith(ev['palavra']))
        put(b, t, lista[ev['fx']], GG[ev['fx']] * ev.get('g', 1))
    return b


# ------------------------------------------------------------------ voz
def wav48(src, dst):
    if not dst.exists():
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(src), '-ar', str(SR), '-ac', '1', str(dst)], check=True)
    with wave.open(str(dst)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768


def montar_voz(pl, tempos, aud, dur):
    tmp = aud / '48k'
    tmp.mkdir(exist_ok=True)
    partes = {n: wav48(aud / f'parte_{n}.wav', tmp / f'parte_{n}.wav') for n in (1, 2)}
    ref = math.sqrt(np.mean(partes[1] ** 2))
    alvo = 0.075
    v = np.zeros(int(dur * SR), np.float32)
    fade = int(0.006 * SR)
    for s in pl:
        c = tempos.get(str(s['i']))
        if c:
            x = partes[c['parte']][int(c['a'] * SR):int(c['b'] * SR)].copy() * (alvo / ref)
            # aproxima os planos do mesmo nível, sem igualar: sussurro continua mais baixo que grito
            x *= float(np.clip((alvo / (math.sqrt(np.mean(x ** 2)) + 1e-9)) ** 0.6, 0.6, 1.9))
            at = s['start'] + LEAD
        elif s['who']:
            x = wav48(aud / f"{s['id']}.wav", tmp / f"{s['id']}.wav").copy()
            fala = x[np.abs(x) > 0.01]
            x *= alvo * 1.1 / (math.sqrt(np.mean(fala ** 2)) + 1e-9)
            at = s['start'] + LEAD_FALA
        else:
            continue
        x[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)
        x[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
        put(v, at, x)
    return v


def srt(pl, tempos, voz_js, dst):
    fmt = lambda t: f'{int(t // 3600):02d}:{int(t // 60 % 60):02d}:{int(t % 60):02d},{int(t * 1000 % 1000):03d}'
    linhas = []
    for s in pl:
        if not s['n']:
            continue
        ws = s['n'].split()
        wt = voz_js[s['id']].get('wt') or [[w, 0.15 + (s['dur'] - 0.4) * k / len(ws)] for k, w in enumerate(ws)]
        fim_plano = s['start'] + s['dur'] - 0.05
        k = 0
        while k < len(ws):
            j = k
            while j < len(ws) - 1 and j - k < 9 and not (j - k >= 2 and re.search(r'[.?!:]$', ws[j])):
                j += 1
            a = s['start'] + wt[k][1]
            b = s['start'] + wt[j + 1][1] - 0.02 if j + 1 < len(ws) else fim_plano
            linhas.append((a, b, ' '.join(ws[k:j + 1])))
            k = j + 1
    dst.write_text(''.join(f'{i}\n{fmt(a)} --> {fmt(b)}\n{t}\n\n' for i, (a, b, t) in enumerate(linhas, 1)), encoding='utf8')
    return len(linhas)


def grava(path, x):
    y = np.clip(x, -1, 1)
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(2 if y.ndim == 2 else 1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((y * 32767).astype(np.int16).tobytes())


def ler(path):
    with wave.open(str(path)) as w:
        return (np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768).reshape(-1, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ep')
    ap.add_argument('--so-som', action='store_true')
    ap.add_argument('--efeitos', action='store_true', help='refaz os efeitos e mantém a trilha')
    ap.add_argument('--remix', action='store_true', help='refaz só a mixagem com os stems existentes (trilha e efeitos levam ~13 min)')
    a = ap.parse_args()
    base = ROOT / 'episodes' / a.ep
    out, aud = base / 'output', base / 'audio'
    som = base / 'som'
    som.mkdir(exist_ok=True)
    pl = json.loads((out / 'planos.json').read_text(encoding='utf8'))
    tempos = json.loads((aud / 'tempos.json').read_text(encoding='utf8'))
    voz_js = json.loads(re.sub(r'^self\.EP_VOZ = |;\s*$', '', (base / 'voz.js').read_text(encoding='utf8')))
    cfg = json.loads((base / 'trilha.json').read_text(encoding='utf8'))
    dur = pl[-1]['start'] + pl[-1]['dur']
    inicio = {s['id']: s['start'] for s in pl}
    print(f'{dur:.1f} s', flush=True)

    v = montar_voz(pl, tempos, aud, dur)
    grava(som / 'voz.wav', v)
    print('voz ok', flush=True)
    print('legendas', srt(pl, tempos, voz_js, out / f'{a.ep}.srt'), flush=True)
    if a.remix or a.efeitos:
        mus = ler(som / 'trilha.wav')
    else:
        mus = trilha(dur, [(inicio[s['de']] + s.get('t', 0), s['faixas']) for s in cfg['secoes']], inicio[cfg['ciclo']])
        grava(som / 'trilha.wav', mus)
    if a.remix:
        fx = ler(som / 'efeitos.wav')
    else:
        fx = efeitos(pl, dur, voz_js, cfg)
        grava(som / 'efeitos.wav', fx)
    print('efeitos ok', flush=True)

    g = np.float32(ducking(v.astype(np.float64), cfg.get('duck', 0.62)))
    # planos em que a trilha divide a faixa com a voz: "abaixa": {"plano": ganho}
    ctl = np.arange(0, dur + 1, 0.05)
    ab = np.ones(len(ctl))
    for s in pl:
        if s['id'] in cfg.get('abaixa', {}):
            ab[(ctl >= s['start'] - 0.2) & (ctl < s['start'] + s['dur'] + 0.2)] = cfg['abaixa'][s['id']]
    ab = np.convolve(np.pad(ab, 8, mode='edge'), np.ones(17) / 17, mode='valid')[:len(ctl)]
    mus = mus * np.float32(np.interp(np.arange(len(mus)) / SR, ctl, ab))[:, None] * cfg.get('g_trilha', 1.0)
    # sob a voz os agudos da trilha cedem mais que os graves: ela continua grande sem encobrir a fala
    lo = sosfilt(butter(2, 280, 'lp', fs=SR, output='sos'), mus, axis=0).astype(np.float32)
    fala = (1 - g) / cfg.get('duck', 0.62)
    fundo = lo * (1 - cfg.get('duck_grave', 0.4) * fala)[:, None] + (mus - lo) * (1 - cfg.get('duck_agudo', 0.8) * fala)[:, None]
    del lo
    fundo += fx * cfg.get('g_efeitos', 1.0) * (0.45 + 0.55 * g)[:, None]
    fundo = np.tanh(fundo * 1.1) / 1.1                         # segura os picos dos tambores sem baixar a voz
    mix = np.stack([v, v], 1) + fundo
    pico = float(np.max(np.abs(mix)))
    print(f'pico antes do ajuste: {pico:.2f}', flush=True)
    mix /= max(pico, 1.0) * 1.02
    grava(som / 'mix.wav', mix)
    print('mix ok', flush=True)

    # volume do YouTube: -14 LUFS em duas passagens (a segunda só desloca o nível, sem comprimir)
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(som / 'mix.wav'), '-af', 'loudnorm=I=-14:TP=-1.5:LRA=14:print_format=json', '-f', 'null', '-'], capture_output=True, text=True)
    m = json.loads(re.findall(r'\{[^{}]*"input_i"[^{}]*\}', r.stderr)[-1])
    print({k: m[k] for k in ('input_i', 'input_tp', 'input_lra')}, flush=True)
    filtro = f"loudnorm=I=-14:TP=-1.5:LRA=14:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,alimiter=limit=0.84:level=false"
    if a.so_som:
        return
    final = out / f'{a.ep}.mp4'
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(out / f'{a.ep}_sem_audio.mp4'), '-i', str(som / 'mix.wav'), '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                    '-af', filtro + f',aresample={SR}', '-c:a', 'aac', '-b:a', '256k', '-shortest', '-movflags', '+faststart', str(final)], check=True)
    print('PRONTO', final, flush=True)


main()
