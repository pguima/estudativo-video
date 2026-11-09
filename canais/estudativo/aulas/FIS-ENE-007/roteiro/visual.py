"""Visual — Estudativo · FIS-ENE-007: quantidade de movimento e impulso. Abre o módulo Impulso e colisões.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001): quantidade de movimento Q = seta petróleo grossa, no sentido de v; impulso I = seta laranja,
como a força; sentido positivo com a peça sentido_mais. No airbag, o impulso é a área de um retângulo força × tempo:
alto e estreito sem airbag, baixo e largo com airbag (mesma área).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-007_quantidade_de_movimento_e_impulso.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quantidade", "impulso", "airbag", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
QC = F.VEL  # quantidade de movimento

# todas as contas da aula
ok = lambda a, b: abs(a - b) < 1e-9
assert 0.5 * 20 == 10 and 1000 * 20 == 20000 and 20000 / 10 == 2000 and ok(500 * 0.02, 10) and 10 / 0.5 == 20 and ok(72 / 3.6, 20)
assert 70 * 20 == 1400 and ok(1400 / 0.01, 140000) and ok(1400 / 0.1, 14000) and 0.5 * (-10 - 10) == -10
assert ok(0.4 * (-10 - 15), -10) and ok(10 / 0.05, 200) and ok(0.4 * (15 - 10) / 0.05, 40)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "250 J" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def sinal_tau(c, t, t0, tipo, cx, cy, size=48):
    """pílula do sinal do trabalho: + ajuda (laranja), − atrapalha (azul), 0 perpendicular (cinza)"""
    txt, fundo = {"+": ("τ > 0", E.COR), "-": ("τ < 0", F.NEG), "0": ("τ = 0", TINTA2)}[tipo]
    pilula_em(c, t, t0, txt, cx, cy, size, fundo)


def milhar(v):
    """número com ponto de milhar: 200000 vira 200.000"""
    return f"{int(v):,}".replace(",", ".") if float(v).is_integer() else E._num(v)


def barras_energia(c, t, x, yb, h, vmax, itens, larg_=150, gap=60, size=44, total=None, t_total=None, fmt=None):
    """barras verticais de energia na base yb: itens = [(rótulo, valor, cor, instante)]; h = altura de vmax.
    total = valor da linha tracejada do total (aparece em t_total). O valor (fmt) vai em cima de cada barra"""
    fmt = fmt or (lambda v: milhar(v) + " J")
    for i, (rot, v, cor, ti) in enumerate(itens):
        bx = x + i * (larg_ + gap)
        q = ep(t, ti, 0.4)
        if q <= 0:
            continue
        hh = h * v / vmax * ease_io(prog(t, ti, 0.7))
        if hh > 0.5:
            M.rrect(c, bx, yb - hh, larg_, hh, 10, cor, q)
        E.foco(c, t, ti + 0.4, 0.4, lambda a, bx=bx, v=v, hh=hh: F.medida(c, *(fmt(v).split(" ", 1) + [""])[:2], bx + larg_ / 2, yb - h * v / vmax - 18, size, TINTA, a, "center"))
        E.foco(c, t, ti, 0.4, lambda a, bx=bx, rot=rot, cor=cor: centro(c, rot, bx + larg_ / 2, yb + size + 14, size, "g", cor, a))
    if total is not None and t_total is not None and t >= t_total:
        n = len(itens)
        yt = yb - h * total / vmax
        M.line(c, x - 30, yt, x + n * larg_ + (n - 1) * gap + 30, yt, TINTA, ep(t, t_total, 0.4), 4, dash=E.TRACO)
    if t >= min(it[3] for it in itens):
        n = len(itens)
        M.line(c, x - 30, yb, x + n * larg_ + (n - 1) * gap + 30, yb, TINTA, ep(t, min(it[3] for it in itens), 0.4), 5)


def sentido_mais(c, t, t0, x, y, escuro=False):
    """convenção de sinal: seta curta para a direita com "+" (sentido positivo)"""
    tinta = BR if escuro else TINTA
    E.foco(c, t, t0, 0.4, lambda a: (F.seta(c, x, y, x + 150, y, tinta, a, 7), E.escreve(c, "+", x + 165, y + 18, 56, "g", tinta, a),
                                      E.escreve(c, "sentido positivo", x, y + 56, 36, "i", tinta, a)))


def lembrete(c, t, C, cena, itens, desenhos=()):
    """lembrete de 2 ou 3 coisas: itens = [(cue, linha fina, linha forte, linha de fórmula ou None)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hs = [200 + (70 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, x + 44, y + 160, 56, "g", COR, a))
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: E.formula(c, l3, x + 44, y + 240, 46, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


# ---------------- desenhos desta aula ----------------
def bola_futebol(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR, a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=max(3, r * 0.08)))
    for k in range(5):
        g = math.radians(90 + 72 * k)
        c.drawCircle(cx + math.cos(g) * r * 0.62, cy - math.sin(g) * r * 0.62, r * 0.17, M.paint(TINTA, a))
    c.drawCircle(cx, cy, r * 0.22, M.paint(TINTA, a))


def parede_bola(c, t, t0, xp, y, r, v_ida, v_volta, t_ida, t_volta, rot_ida, rot_volta, t_bola=None):
    """parede à direita em xp; vetores de velocidade chegando e voltando acima e abaixo da bola"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    F.parede(c, xp, y - 260, y + 260, 1, q)
    F.chao(c, xp - 700, xp, y + 260, q)
    E.foco(c, t, t_bola if t_bola is not None else t0, 0.4, lambda a: bola_futebol(c, xp - r - 6, y, r, a))
    F.vetor(c, t, t_ida, (xp - r - 40 - v_ida, y - 150), (xp - r - 40, y - 150), "v", rot_ida, QC, 9, lado=1, size=46)
    if t_volta is not None:
        F.vetor(c, t, t_volta, (xp - r - 40, y + 150), (xp - r - 40 - v_volta, y + 150), "v", rot_volta, QC, 9, lado=-1, size=46)


def retangulo_ft(c, t, t0, x, yb, w, h, cor, rot_f, rot_t, a=1.0, acima=False):
    """impulso como área: retângulo força × tempo crescendo de baixo para cima"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    hh = h * ease_io(prog(t, t0, 0.7))
    M.rrect(c, x, yb - hh, w, hh, 6, cor, 0.85 * q)
    fx, fy = (x, yb - h - 24) if acima else (x + w + 20, yb - h + 30)
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: (E.formula(c, rot_f, fx, fy, 46, "g", TINTA, a),
                                            centro(c, rot_t, x + w / 2, yb + 56, 44, "g", TINTA2, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 760
        if t >= C["s01.a"]:
            F.chao(c, 170, 1750, y, ep(t, C["s01.a"], 0.4))
            F.parede(c, 1500, y - 380, y, 1, ep(t, C["s01.a"], 0.4))
        p = ease_out(prog(t, C["s01.a"] + 0.3, 1.6))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: F.carrinho(c, lerp(500, 1290, p), y, 360, a=a))
        E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: F.medida(c, 72, "km/h", 260, 360, 80, TINTA, a))
        E.frase(c, t, C["s01.a"] + 1.8, ps("vai parar de qualquer jeito", "i", 62, TINTA2), 260, 470, passo=0.1)
        if t >= C["s01.b"]:
            E.foco(c, t, C["s01.b"], 0.5, lambda a: E.bola(c, 1250, y - 230, 120 * ease_back(prog(t, C["s01.b"], 0.5)), BR, a))
            E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: centro(c, "airbag", 1250, y - 216, 46, "g", COR, a))
        E.frase(c, t, C["s01.c"], [("duas", "i", 80), ("grandezas", "g", 76), ("novas", "g", 76, COR)], 260, 980, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 320 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
        itens = (("s02.a", "Q e impulso", 1.4), ("s02.b", "ligar um ao outro", 0), ("s02.c", "o airbag numa conta", 0))
        for i, (k, s, dt) in enumerate(itens):
            y = 450 + i * 160
            E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a segunda lei de Newton:", "F = m · a", "F = força resultante"),
                              ("s03.c", "a aceleração:", "a = f{Δv}{Δt}", None)))


# ---------------- quantidade de movimento ----------------
def b_quantidade(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("para parar: pesa a massa ou a velocidade?", "i", 62), XE, 200, passo=0.1)
        y1, y2 = 520, 880
        if t >= C["s04.a"]:
            F.chao(c, 170, 1100, y1, ep(t, C["s04.a"], 0.4))
            F.chao(c, 170, 1100, y2, ep(t, C["s04.b"], 0.4)) if t >= C["s04.b"] else None
        E.foco(c, t, C["s04.a"], 0.5, lambda a: bola_futebol(c, 500, y1 - 50, 50, a))
        F.vetor(c, t, C["s04.a"] + 0.3, (580, y1 - 50), (840, y1 - 50), "v", "20 m/s", QC, 8, size=44)
        E.foco(c, t, C["s04.a"] + 0.6, 0.4, lambda a: E.selo(c, 1000, y1 - 120, 50, True, a))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: F.carrinho(c, 500, y2, 300, a=a))
        F.vetor(c, t, C["s04.b"] + 0.3, (680, y2 - 100), (940, y2 - 100), "v", "20 m/s", QC, 8, size=44)
        E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.selo(c, 1000, y2 - 190, 50, False, a))
        E.frase(c, t, C["s04.c"], [("quantidade", "g", 70, QC), ("de", "i", 74)], 1180, 560, passo=0.12)
        E.frase(c, t, C["s04.c"] + 0.4, [("movimento", "g", 70, QC)], 1180, 650)
        E.frase(c, t, C["s04.c"] + 0.9, ps("massa e velocidade juntas", "i", 54, TINTA2), 1180, 750, passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("massa", "i", 70), ("×", "g", 70), ("velocidade", "i", 70)], XE, 220, passo=0.12)
            F.formula_legenda(c, t, C["s05.b"], "Q = m · v", [("Q", "quantidade de movimento", "kg · m/s"), ("m", "massa", "kg"), ("v", "velocidade", "m/s")],
                              XE, 470, 140, tl=[C["s05.c"], C["s05.c"] + 0.4, C["s05.c"] + 0.8])
            y = 520
            E.foco(c, t, C["s05.d"], 0.4, lambda a: F.bloco(c, 1250, y, 160, 130, "m", E.COR, a))
            F.vetor(c, t, C["s05.d"] + 0.3, (1250, y - 120), (1550, y - 120), "v", None, F.VEL, 8, size=46)
            F.vetor(c, t, C["s05.d"] + 0.8, (1250, y + 130), (1650, y + 130), "Q", None, QC, 16, lado=-1, size=54)
            E.foco(c, t, C["s05.d"] + 1.2, 0.4, lambda a: E.pilula(c, "VETORIAL", 1450, 880, 56, "g", fundo=E.COR, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    for i, (k, kr, txt, conta, res, y) in enumerate((("s06.a", "s06.b", "bola 0,5 kg · 20 m/s", "Q = 0,5 · 20", "10", 330),
                                                    ("s06.c", "s06.d", "carro 1.000 kg · 20 m/s", "Q = 1.000 · 20", "20.000", 680))):
        E.foco(c, t, C[k], 0.5, lambda a, txt=txt, y=y: E.formula(c, txt, XE, y - 90, 54, "b", TINTA2, a))
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, conta=conta, y=y: E.formula(c, conta, XE, y + 40, 90, "g", TINTA, a))
        E.foco(c, t, C[kr], 0.5, lambda a, res=res, y=y: F.medida(c, res, "kg · m/s", 1050, y + 40, 90, QC, a))
        L = 60 if i == 0 else 700
        F.vetor(c, t, C[kr] + 0.3, (1050, y + 110), (1050 + L, y + 110), None, None, QC, 14)
    pilula_em(c, t, C["s06.d"] + 1.0, "2.000 vezes mais", 1450, 960, 50, TINTA)


# ---------------- impulso ----------------
def b_impulso(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07"], ps("para mudar Q: força durante um tempo", "i", 62), XE, 200, passo=0.1)
        F.formula_legenda(c, t, C["s07.b"], "I = F · Δt", [("I", "impulso", "N · s"), ("F", "força", "N"), ("Δt", "intervalo de tempo", "s")],
                          XE, 450, 140, tl=[C["s07.c"], C["s07.c"] + 0.4, C["s07.c"] + 0.8])
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.formula(c, "impulso = força × tempo", 1050, 450, 56, "b", TINTA2, a))
        F.vetor(c, t, C["s07.d"], (1100, 700), (1500, 700), "I", None, E.COR, 14, size=54)
        E.foco(c, t, C["s07.d"] + 0.4, 0.4, lambda a: E.escreve(c, "sentido da força", 1100, 800, 50, "i", TINTA2, a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if C["s08"] <= t < C["s10"]:
        def s08_09():
            linhas = [(C["s08.a"], "F = m · a"), (C["s08.b"], "F = m · f{Δv}{Δt}"), (C["s08.d"], "F · Δt = m · Δv")]
            for i, (ti, s) in enumerate(linhas):
                E.foco(c, t, ti, 0.5, lambda a, s=s, i=i: E.formula(c, s, XE + 40, 260 + i * 190, 96, "g", TINTA if i < 2 else E.COR_TEXTO, a))
            E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "Δt passa multiplicando", 1300, 450, 46, "b", fundo=TINTA2, a=a))
            if t >= C["s09"]:
                E.foco(c, t, C["s09.a"], 0.4, lambda a: centro(c, "impulso I", XE + 200, 760, 56, "g", E.COR_TEXTO, a))
                E.foco(c, t, C["s09.b"], 0.4, lambda a: centro(c, "variação de Q", XE + 560, 760, 56, "g", QC, a))
                E.foco(c, t, C["s09.c"], 0.6, lambda a: (E.bola(c, 1420, 760, 170 * ease_back(prog(t, C["s09.c"], 0.6)), a=a),
                                                         E.formula(c, "I = ΔQ", 1420, 790, 80, "g", BR, a, "center")))
                E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "ΔQ = Q fim − Q começo", W / 2, 1010, 64, "g", QC, a, "center"))
        E.saida(c, t, C["s10"] - 0.1, s08_09)
    if t < C["s10"]:
        return
    y = 520
    if t >= C["s10"]:
        F.chao(c, 170, 1100, y + 60, ep(t, C["s10"], 0.4))
    E.foco(c, t, C["s10"], 0.4, lambda a: bola_futebol(c, 600, y, 60, a))
    F.forca(c, t, C["s10.a"], (330, y), 0, 200, "F", None, "500 N", size=48)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.formula(c, "Δt = 0,02 s", 330, 760, 60, "g", TINTA2, a))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "I = 500 · 0,02 = 10 N · s", 1080, 320, 70, "g", E.COR_TEXTO, a))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "Q = 0 + 10 = 10 kg · m/s", 1080, 500, 70, "g", QC, a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "v = f{10}{0,5}", 1080, 720, 80, "g", TINTA, a))
    bola_txt(c, t, C["s10.e"] + 0.8, "20 m/s", 1600, 700, 120, 58, QC)


# ---------------- airbag ----------------
def b_airbag(c, t, C, b):
    E.frase(c, t, C["s11"], [("o", "i", 76), ("airbag", "g", 76, COR)], XE, 190)
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.formula(c, "70 kg · 20 m/s → 0", XE, 330, 66, "g", TINTA, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "ΔQ = 0 − 1.400 = −1.400", XE, 470, 66, "g", QC, a))
    E.frase(c, t, C["s11.b"] + 1.5, ps("com ou sem airbag", "i", 56, TINTA2), XE, 560, passo=0.1)
    yb = 960
    x1, x2 = 1050, 1400
    if t >= C["s11.c"]:
        M.line(c, 1000, yb, 1860, yb, TINTA, ep(t, C["s11.c"], 0.4), 5)
    retangulo_ft(c, t, C["s11.c"], x1, yb, 40, 600, ERRADO, "140.000 N", "0,01 s")
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "volante", x1 - 30, yb - 640, 44, "i", ERRADO, a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "F = f{1.400}{0,01} = 140.000 N", XE, 760, 60, "g", ERRADO, a))
    if t >= C["s12"]:
        retangulo_ft(c, t, C["s12.a"], x2, yb, 400, 60, CERTO, "14.000 N", "0,1 s", acima=True)
        E.foco(c, t, C["s12.a"], 0.4, lambda a: E.escreve(c, "airbag", x2, yb - 160, 44, "i", CERTO, a))
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "F = f{1.400}{0,1} = 14.000 N", XE, 900, 60, "g", CERTO, a))
        pilula_em(c, t, C["s12.c"], "mesmo impulso = mesma área", 1480, 600, 46, E.COR)
        E.frase(c, t, C["s12.d"], ps("por isso você dobra os joelhos", "i", 52, TINTA2), XE, 1030, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("esquecer o sentido", "i", 76), XE + 480, 200, passo=0.12)
    sentido_mais(c, t, C["s13.b"], 1500, 150)
    parede_bola(c, t, C["s13.b"], 1750, 560, 50, 280, 280, C["s13.b"] + 0.3, C["s13.b"] + 1.6, "10 m/s", "10 m/s")

    def errado():
        E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "10 − 10 = 0", XE, 480, 90, "g", ERRADO, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "sem impulso?", XE, 640, 80, "g", ERRADO, a))
        if t >= C["s14"]:
            E.risco(c, XE - 10, 500, XE + 520, 400, t, C["s14"], largura=12)
    E.saida(c, t, C["s14.b"] - 0.1, errado)
    if t < C["s14.b"]:
        return
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "ida +10, volta −10", XE, 400, 70, "g", TINTA, a))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "Δv = −10 − 10 = −20", XE, 560, 70, "g", TINTA, a))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "ΔQ = 0,5 · (−20) = −10", XE, 720, 70, "g", QC, a))
    F.vetor(c, t, C["s14.e"], (1640, 930), (1340, 930), "I", "10 N · s", E.COR, 12, lado=1, size=48)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s15.a"], ps("bater e voltar igual =", "i", 64, CLARO) + [("2×", "g", 64, BR)] + ps("o impulso de bater e parar", "i", 64, CLARO),
                W / 2, 290, "center", 0.1)
        for i, (k, txt, L) in enumerate((("s15.b", "parar: 10 → 0", 300), ("s15.c", "voltar: 10 → −10", 600))):
            y = 470 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, txt=txt, y=y: E.formula(c, txt, 260, y + 20, 64, "g", BR, a))
            F.vetor(c, t, C[k] + 0.4, (1500, y), (1500 - L, y), None, None, CLARO, 14, escuro=True)
        E.frase(c, t, C["s15.d"], ps("mesmo impulso:", "i", 60, CLARO) + [("tempo × 10", "g", 60, BR), ("→", "g", 60, CLARO), ("força ÷ 10", "g", 60, BR)], W / 2, 900, "center", 0.1)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("F · Δt", "g", 76, BR), ("fixo:", "i", 76, CLARO)] + ps("inversamente proporcionais", "i", 70, CLARO), W / 2, 330, "center", 0.12)
    E.frase(c, t, C["s16.b"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("volta com outra velocidade", "i", 64, CLARO), W / 2, 620, "center", 0.1)
    E.frase(c, t, lerp(C["s16.b"], C["s16.end"], 0.6), ps("aí, faça a conta com os sinais", "i", 60, CLARO), W / 2, 740, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("bola", "i", 70), ("0,4 kg", "g", 66)], XE, 350, passo=0.12)
    E.frase(c, t, C["s17.b"], [("chega", "i", 70), ("a", "i", 70), ("15 m/s", "g", 66, QC)], XE, 460, passo=0.12)
    E.frase(c, t, C["s17.c"], [("volta", "i", 70), ("a", "i", 70), ("10 m/s", "g", 66, QC)], XE, 570, passo=0.12)
    E.frase(c, t, C["s17.d"], [("contato:", "i", 70), ("0,05 s", "g", 66)], XE, 680, passo=0.12)
    E.frase(c, t, C["s17.e"], [("impulso?", "g", 66, COR), ("força", "i", 70), ("média?", "g", 66, COR)], XE, 860, passo=0.12)
    if t < C["s18"]:
        parede_bola(c, t, C["s17.a"], 1750, 560, 50, 380, 250, C["s17.b"], C["s17.c"], "15 m/s", "10 m/s")
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        sentido_mais(c, t, C["s19.a"], 1500, 150)
        E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "ida +15, volta −10", XE, 300, 70, "g", TINTA, a))
        E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "Δv = −10 − 15 = −25", XE, 480, 76, "g", TINTA, a))
        E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "ΔQ = 0,4 · (−25) = −10", XE, 660, 76, "g", QC, a))
        bola_txt(c, t, C["s19.d"], "10 N·s", 1450, 640, 140, 60)
        E.foco(c, t, C["s19.d"] + 0.5, 0.4, lambda a: centro(c, "para fora da parede", 1450, 860, 50, "i", TINTA2, a))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"], [("força", "i", 70), ("média", "g", 66, COR)] + ps("= a constante que dá o mesmo impulso", "i", 62), XE, 260, passo=0.1)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "F = f{10}{0,05}", W / 2 - 300, 560, 120, "g", TINTA, a, "center"))
    bola_txt(c, t, C["s20.c"], "200 N", W / 2 + 350, 520, 140, 70, CERTO)
    E.frase(c, t, C["s20.d"] - 1.4, ps("sem o sinal: 15 − 10", "i", 60, TINTA2) + [("→", "g", 60, TINTA2), ("40 N", "g", 60, ERRADO)], W / 2, 900, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s21.a", "Q = m · v"), ("s21.b", "I = F · Δt"), ("s21.c", "I = ΔQ"), ("s21.d", "mais tempo de parada, menos força"))
        for i, (k, s) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 72, "g", TINTA, a))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], ps("nada de fora empurra:", "i", 70, TINTA2), XE, 400, passo=0.1)
    E.frase(c, t, C["s22.b"], [("Q", "g", 110, QC), ("total", "g", 110), ("não", "i", 100), ("muda", "g", 110, COR)], XE, 560, passo=0.14)
    E.frase(c, t, C["s22.b"] + 1.4, ps("o coice da espingarda", "i", 64, TINTA2), XE, 690, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quantidade=b_quantidade, impulso=b_impulso, airbag=b_airbag, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
