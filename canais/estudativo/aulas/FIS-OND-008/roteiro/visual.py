"""Visual — Estudativo · FIS-OND-008: efeito Doppler.

Segue a linguagem visual da trilha Ondas e Som (docstring do visual.py da FIS-OND-001) e a da Física (FIS-CIN-001).
Nesta aula: a sirene é a fonte laranja; as frentes de onda são círculos laranja que saem de onde a fonte estava no instante
de cada crista (frentes()), e por isso se apertam na frente e se abrem atrás. Agudo em laranja, grave em azul (F.NEG).
A fórmula geral precisa de índice (v com o e v com f): formula_sub() desenha a fração com subscrito.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
from fractions import Fraction

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-008_efeito_doppler.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("porque", "formula", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
GRAVE = F.NEG

# todas as contas da aula
assert 720 * 340 / (340 - 20) == 765 and Fraction(720, 320) == Fraction(9, 4) and Fraction(9, 4) * 340 == 765
assert 720 * 340 / (340 + 20) == 680 and 720 / 360 == 2 and 2 * 340 == 680 and 680 < 720 < 765
assert Fraction(680, 600) == Fraction(17, 15) and 340 == 20 * 17 and 20 * 15 == 300 and 340 - 300 == 40
assert 600 * 340 / (340 - 40) == 680 and 40 * 3.6 == 144


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais (copiadas da FIS-OND-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete2(c, t, C, cena, itens, desenhos):
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


# ---------------- peças desta aula ----------------
def linha_sub(c, partes, x, y, size, cor, a=1.0):
    """texto com índice: partes = "v ± v_o" (o caractere depois de _ vira índice pequeno). Devolve a largura"""
    xx = x
    i = 0
    while i < len(partes):
        if partes[i] == "_" and i + 1 < len(partes):
            s, sz, dy = partes[i + 1], size * 0.58, size * 0.22
            if c is not None and a > 0:
                E.escreve(c, s, xx, y + dy, sz, "b", cor, a)
            xx += E.larg(s, "b", sz) + size * 0.04
            i += 2
            continue
        if partes[i] == "∓":  # a grotesca não tem ∓: é o ± de cabeça para baixo
            if c is not None and a > 0:
                cy = y - size * 0.36
                c.save(); c.translate(0, 2 * cy); c.scale(1, -1)
                E.escreve(c, "±", xx, y, size, "g", cor, a)
                c.restore()
            xx += E.larg("±", "g", size)
            i += 1
            continue
        j = i
        while j < len(partes) and partes[j] not in "_∓":
            j += 1
        s = partes[i:j]
        if c is not None and a > 0:
            E.escreve(c, s, xx, y, size, "g", cor, a)
        xx += E.larg(s, "g", size)
        i = j
    return xx - x


def formula_sub(c, pre, cima, baixo, x, y, size, cor=None, a=1.0, pos="", cor_f=None):
    """pre + fração (cima/baixo com índice) + pos; y = linha de base do texto. Devolve a largura"""
    cor = cor or TINTA
    cor_f = cor_f or cor
    wp = E.formula(c, pre, x, y, size, "g", cor, a) + size * 0.2 if pre else 0
    s2 = size * 0.82
    wc, wb = linha_sub(None, cima, 0, 0, s2, cor), linha_sub(None, baixo, 0, 0, s2, cor)
    wf = max(wc, wb) + size * 0.3
    xf = x + wp
    yb = y - size * 0.33
    if a > 0:
        M.line(c, xf, yb, xf + wf, yb, cor_f, a, max(4, size * 0.07), cap_round=False)
        linha_sub(c, cima, xf + (wf - wc) / 2, yb - size * 0.2, s2, cor_f, a)
        linha_sub(c, baixo, xf + (wf - wb) / 2, yb + size * 0.82, s2, cor_f, a)
    wpos = E.formula(c, pos, xf + wf + size * 0.2, y, size, "g", cor, a) + size * 0.2 if pos else 0
    return wp + wf + wpos


def formula_sub_em(c, t, t0, *args, **kw):
    E.foco(c, t, t0, 0.5, lambda a: formula_sub(c, *args, a=a, **kw))


def ambulancia(c, x, y, w=240, a=1.0, sentido=1):
    """ambulância de lado, rodas tocando y, centro em x; sirene laranja no teto"""
    if a <= 0:
        return
    h = w * 0.42
    c.save(); c.translate(x, 0)
    if sentido < 0:
        c.scale(-1, 1)
    M.rrect(c, -w / 2, y - h - w * 0.08, w * 0.72, h, 10, "#FFFFFF", a, stroke=5, stroke_color=TINTA)
    M.rrect(c, -w / 2 + w * 0.7, y - h * 0.72 - w * 0.08, w * 0.3, h * 0.72, 10, "#FFFFFF", a, stroke=5, stroke_color=TINTA)
    M.rrect(c, w * 0.26, y - h * 0.62 - w * 0.08, w * 0.17, h * 0.3, 4, "#9FD3E6", a)
    cx_, cy_ = -w * 0.16, y - h * 0.55 - w * 0.08
    M.line(c, cx_ - h * 0.22, cy_, cx_ + h * 0.22, cy_, ERRADO, a, h * 0.12)
    M.line(c, cx_, cy_ - h * 0.22, cx_, cy_ + h * 0.22, ERRADO, a, h * 0.12)
    M.rrect(c, -w * 0.2, y - h - w * 0.08 - h * 0.18, w * 0.12, h * 0.18, 4, E.COR, a)
    for rx in (-w * 0.3, w * 0.3):
        c.drawCircle(rx, y - w * 0.07, w * 0.08, M.paint(TINTA, a))
        c.drawCircle(rx, y - w * 0.07, w * 0.035, M.paint("#BBBBBB", a))
    c.restore()


def pessoa(c, x, y, s=1.0, a=1.0, cor=None):
    """bonequinho de pé com os pés em y"""
    if a <= 0:
        return
    cor = cor or TINTA
    c.drawCircle(x, y - 150 * s, 24 * s, M.paint(cor, a))
    M.line(c, x, y - 124 * s, x, y - 60 * s, cor, a, 12 * s)
    M.line(c, x, y - 60 * s, x - 20 * s, y, cor, a, 10 * s)
    M.line(c, x, y - 60 * s, x + 20 * s, y, cor, a, 10 * s)
    M.line(c, x - 30 * s, y - 105 * s, x + 30 * s, y - 105 * s, cor, a, 9 * s)


def frentes(c, t, t0, pos, vs=260, dt=0.42, rmax=900, cor=None, a=1.0, t1=None):
    """frentes de onda: a cada dt a fonte solta um círculo do ponto onde está (pos(te) → (x, y)), que cresce a vs px/s"""
    if t < t0 or a <= 0:
        return
    cor = cor or E.COR
    k = 0
    while True:
        te = t0 + k * dt
        if te > t or (t1 is not None and te > t1):
            break
        r = (t - te) * vs
        if 4 < r < rmax:
            cx, cy = pos(te)
            c.drawCircle(cx, cy, r, M.paint(cor, a * 0.85 * (1 - r / rmax), stroke=5))
        k += 1


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 860
        t0, t1 = C["s01.a"], C["s01.d"] + 1.0
        x = lambda tt: lerp(260, 1760, ease_io(prog(tt, t0, t1 - t0)))
        F.chao(c, 100, 1820, y, ep(t, t0, 0.4)) if t >= t0 else None
        frentes(c, t, t0 + 0.2, lambda te: (x(te), y - 120), vs=300, dt=0.32, rmax=700, a=ep(t, t0, 0.4))
        E.foco(c, t, t0, 0.5, lambda a: ambulancia(c, x(t), y, 240, a))
        E.foco(c, t, t0 + 0.3, 0.5, lambda a: pessoa(c, 1060, y, 1.0, a))
        E.frase(c, t, C["s01.a"] + 0.2, ps("chegando:", "i", 76), XE, 230, passo=0.1)
        E.frase(c, t, C["s01.b"], [("aguda", "g", 96, COR)], XE + 380, 230)
        E.frase(c, t, C["s01.c"], ps("passou:", "i", 76), XE, 370, passo=0.1)
        E.frase(c, t, C["s01.d"], [("grave", "g", 96, GRAVE)], XE + 380, 370)
        pilula(c, t, C["s01.e"], "mas a sirene não mudou nada", W / 2, 520, 60, TINTA)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.a", "explicar a mudança", 1.2), ("s02.b", "a frequência ouvida", 0), ("s02.c", "o atalho dos sinais", 0))
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 2 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def ondas(a, x, y):
        F.onda(c, 99, 0, x - 190, x - 30, y - 50, 22, 40, eixo=False) if a > 0.99 else None
        F.onda(c, 99, 0, x - 190, x - 30, y + 30, 22, 110, cor=GRAVE, eixo=False) if a > 0.99 else None

    def equa(a, x, y):
        E.formula(c, "f{x}{2} = 5", x - 60, y + 30, 66, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "frequência alta: agudo,", "baixa = grave"), ("s03.c", "resolver uma equação", "com fração")), (ondas, equa))


# ---------------- por quê ----------------
def b_porque(c, t, C, b):
    y = 560
    if t < C["s05"]:
        def s04():
            cx = 960
            frentes(c, t, C["s04.a"], lambda te: (cx, y), vs=200, dt=0.6, rmax=760)
            E.foco(c, t, C["s04"], 0.5, lambda a: (E.bola(c, cx, y, 34, a=a)))
            E.frase(c, t, C["s04"], ps("a sirene solta", "i", 70) + [("cristas", "g", 70, COR)], W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s04.b"], [("parada:", "g", 64)] + ps("espaço igual dos dois lados", "i", 64), W / 2, 980, "center", 0.1)
            for x_, s in ((260, "f"), (1660, "f")):
                E.foco(c, t, C["s04.b"] + 0.8, 0.5, lambda a, x_=x_: (pessoa(c, x_, y + 160, 0.9, a), E.pilula(c, "mesma f", x_, y - 60, 44, "g", fundo=TINTA, a=a)))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        t0 = C["s05.a"]
        x = lambda tt: 380 + 115 * ((max(tt, t0) - t0) % 11.0)  # atravessa a tela em 11 s e recomeça
        frentes(c, t, t0, lambda te: (x(te), y), vs=210, dt=0.55, rmax=820)
        E.bola(c, x(t), y, 34, a=ep(t, t0, 0.4))
        F.vetor(c, t, t0 + 0.4, (x(t) + 50, y), (x(t) + 200, y), None, None, TINTA, 7) if t > t0 + 0.4 else None
        E.frase(c, t, C["s05.a"], ps("andando: cada crista sai", "i", 64) + [("mais à frente", "g", 64)], W / 2, 140, "center", 0.1)
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "λ menor", 1640, 300, 60, "g", fundo=E.COR, a=a, cor=BR))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "mais agudo", 1640, 410, 60, "g", fundo=E.COR, a=a, cor=BR))
        E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "λ maior", 280, 300, 60, "g", fundo=GRAVE, a=a, cor=BR))
        E.foco(c, t, C["s05.e"], 0.5, lambda a: E.pilula(c, "mais grave", 280, 410, 60, "g", fundo=GRAVE, a=a, cor=BR))
        E.foco(c, t, C["s05.f"], 0.5, lambda a: E.pilula(c, "efeito Doppler", W / 2, 980, 76, "g", fundo=TINTA, a=a, cor=BR))
        return
    # s06: você se mexendo
    E.frase(c, t, C["s06.a"], ps("e com", "i", 76) + [("você", "g", 76, COR)] + ps("se mexendo", "i", 76), W / 2, 170, "center", 0.12)
    cx = 960
    frentes(c, t, C["s06"], lambda te: (cx, y), vs=200, dt=0.6, rmax=760)
    E.bola(c, cx, y, 34, a=ep(t, C["s06"], 0.4))
    yp = y + 300
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (pessoa(c, 1500, yp, 0.8, a), F.seta(c, 1440, yp - 190, 1290, yp - 190, TINTA, a, 8)))
    E.foco(c, t, C["s06.b"] + 0.6, 0.5, lambda a: E.pilula(c, "vai na direção: mais agudo", 1520, 400, 44, "g", fundo=E.COR, a=a, cor=BR))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: (pessoa(c, 420, yp, 0.8, a), F.seta(c, 400, yp - 190, 250, yp - 190, TINTA, a, 8)))
    E.foco(c, t, C["s06.c"] + 0.4, 0.5, lambda a: E.pilula(c, "foge: mais grave", 400, 400, 44, "g", fundo=GRAVE, a=a, cor=BR))
    E.frase(c, t, C["s06.d"], [("distância", "i", 60), ("diminui", "g", 58, COR), ("↑", "g", 58, COR), ("·", "g", 58, TINTA2), ("aumenta", "g", 58, GRAVE),
                               ("↓", "g", 58, GRAVE)], W / 2, 1010, "center", 0.12)


# ---------------- fórmula ----------------
def b_formula(c, t, C, b):
    if t < C["s08"]:
        def s07():
            x, y, sz = XE, 330, 120
            E.foco(c, t, C["s07.a"], 0.5, lambda a: E.formula(c, "f' = f ·", x, y, sz, "g", TINTA, a))
            wp = E.formula(None, "f' = f ·", 0, 0, sz, a=0) + sz * 0.2
            E.foco(c, t, C["s07.b"], 0.5, lambda a: formula_sub(c, "", "v ± v_o", "", x + wp, y, sz, TINTA, a))
            E.foco(c, t, C["s07.c"], 0.5, lambda a: formula_sub(c, "", "", "v ∓ v_f", x + wp, y, sz, TINTA, a))
            E.foco(c, t, C["s07.b"] + 0.4, 0.5, lambda a: E.pilula(c, "quem ouve: observador", 1460, 230, 46, "g", fundo=TINTA, a=a, cor=BR))
            E.foco(c, t, C["s07.c"] + 0.4, 0.5, lambda a: E.pilula(c, "quem emite: fonte", 1460, 420, 46, "g", fundo=E.COR, a=a, cor=BR))
            leg = (("s07.d", "f", "da sirene", "(Hz)"), ("s07.e", "f'", "a que você ouve", "(Hz)"), ("s07.f", "v", "do som: 340", "(m/s)"))
            for i, (k, l, s, u) in enumerate(leg):
                yy = 640 + i * 110
                E.foco(c, t, C[k], 0.5, lambda a, l=l, s=s, u=u, yy=yy: (E.escreve(c, l, XE, yy, 70, "g", COR, a), E.escreve(c, s, XE + 130, yy, 60, "i", TINTA, a),
                                                                          E.escreve(c, u, XE + 140 + E.larg(s, "i", 60) + 20, yy, 52, "b", TINTA2, a)))
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    # s08: os sinais
    formula_sub_em(c, t, C["s08"], "f' = f ·", "v ± v_o", "v ∓ v_f", XE, 230, 90, TINTA)
    E.frase(c, t, C["s08.a"], [("em", "i", 60), ("direção", "i", 60), ("ao", "i", 60), ("outro:", "i", 60), ("f'", "g", 60, COR), ("sobe", "g", 60, COR)], 1000, 210, "left", 0.1)
    E.frase(c, t, C["s08.b"], ps("escolha o sinal que deixa a fração", "i", 56) + [("maior", "g", 56, COR)], 1000, 300, "left", 0.08)
    linhas = (("s08.c", "+ em cima", "você vai em direção à fonte", E.COR), ("s08.d", "− embaixo", "a fonte vem em sua direção", E.COR),
              ("s08.e", "− em cima, + embaixo", "quem se afasta: f' cai", GRAVE), ("s08.f", "parado: 0", "o termo some", TINTA))
    for i, (k, p, s, cor) in enumerate(linhas):
        yy = 520 + i * 135
        E.foco(c, t, C[k], 0.5, lambda a, p=p, cor=cor, yy=yy: E.pilula(c, p, XE + 20 + (E.larg(p, "g", 54) + 48) / 2, yy - 18, 54, "g", fundo=cor, a=a, cor=BR))
        E.frase(c, t, C[k] + 0.4, ps(s, "i", 58), XE + 700, yy, "left", 0.08)


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    if t < C["s10"]:
        y = 470
        t0 = C["s09"]
        x = lambda tt: lerp(300, 900, ease_io(prog(tt, t0, 12)))
        F.chao(c, 120, 1820, y, ep(t, t0, 0.4)) if t >= t0 else None
        frentes(c, t, t0, lambda te: (x(te), y - 100), vs=260, dt=0.4, rmax=600, a=0.6)
        E.foco(c, t, t0, 0.5, lambda a: ambulancia(c, x(t), y, 220, a))
        E.foco(c, t, t0 + 0.3, 0.5, lambda a: pessoa(c, 1600, y, 0.9, a))
        E.foco(c, t, C["s09.a"], 0.5, lambda a: (E.escreve(c, "f =", XE, 180, 72, "g", TINTA, a), F.medida(c, 720, "Hz", XE + 140, 180, 72, COR, a)))
        E.foco(c, t, C["s09.b"], 0.5, lambda a: (linha_sub(c, "v_f =", XE + 600, 180, 72, TINTA, a),
                                                 F.medida(c, 20, "m/s", XE + 800, 180, 72, COR, a)))
        E.foco(c, t, C["s09.c"] - 0.6, 0.5, lambda a: E.pilula(c, "você parado", 1600, 540, 44, "g", fundo=TINTA, a=a, cor=BR))
        E.saida(c, t, C["s09.d"] - 0.05, lambda: E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "f' = 720 · f{340}{    }", XE, 760, 110, "g", TINTA, a)), d=0.1)
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "f' = 720 · f{340}{340 − 20}", XE, 760, 110, "g", TINTA, a))
        E.foco(c, t, C["s09.d"] + 0.8, 0.5, lambda a: E.formula(c, "= 720 · f{340}{320}", XE + 960, 760, 110, "g", COR, a))
        E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: centro(c, "fonte se aproxima: − embaixo", XE + 470, 960, 50, "i", TINTA2, a))
        return
    E.frase(c, t, C["s10"], [("chegando", "g", 70, COR)], XE, 170)
    conta(c, t, [(C["s10.a"], "f{720}{320} = f{9}{4}"), (C["s10.b"], "f{9}{4} · 340")], XE, 340, 210, 100)
    bola_txt(c, t, C["s10.c"], "765 Hz", 860, 440, 130, 66)
    if t >= C["s10.d"]:
        M.line(c, 1080, 150, 1080, 960, FIO, ep(t, C["s10.d"], 0.4), 3)
    E.frase(c, t, C["s10.d"], [("saindo", "g", 70, GRAVE)], 1160, 170)
    E.foco(c, t, C["s10.d"] + 0.6, 0.5, lambda a: E.formula(c, "720 · f{340}{340 + 20}", 1160, 360, 84, "g", TINTA, a))
    E.foco(c, t, lerp(C["s10.d"], C["s10.e"], 0.6), 0.5, lambda a: E.formula(c, "f{720}{360} = 2", 1160, 560, 84, "g", TINTA, a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "2 · 340", 1160, 730, 84, "g", TINTA, a))
    bola_txt(c, t, C["s10.e"] + 0.6, "680 Hz", 1640, 700, 130, 66, GRAVE)
    E.frase(c, t, lerp(C["s10.e"], C["s10.end"], 0.55), [("765", "g", 64, COR), ("na", "i", 64), ("chegada,", "i", 64), ("680", "g", 64, GRAVE), ("na", "i", 64), ("saída", "i", 64)],
            W / 2, 1000, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("trocar os sinais", "i", 76), XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s11.b"] - 0.6, 0.5, lambda a: E.pilula(c, "ambulância chegando", XE + 270, 330, 50, "g", fundo=E.COR, a=a, cor=BR))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "720 · f{340}{340 + 20}", XE, 560, 110, "g", ERRADO, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "= 680 Hz", XE + 760, 560, 110, "g", ERRADO, a))
    E.frase(c, t, C["s11.c"] + 1.2, [("680", "g", 64, ERRADO), ("<", "g", 64, TINTA2), ("720:", "g", 64), ("mais", "i", 66), ("grave?", "g", 64, GRAVE)], XE, 760, passo=0.12)
    if t >= C["s11.d"]:
        E.risco(c, XE - 20, 600, XE + 1220, 450, t, C["s11.d"], largura=12)
    E.frase(c, t, C["s11.d"] + 0.4, ps("quem se aproxima soa", "i", 64) + [("mais agudo", "g", 64, COR)], XE, 880, passo=0.1)
    E.frase(c, t, C["s11.e"], ps("deu o contrário?", "i", 60) + [("sinal trocado", "g", 58, ERRADO)], XE, 990, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
    E.frase(c, t, C["s12.a"], ps("antes da conta:", "i", 70, CLARO) + [("maior", "g", 70, BR), ("ou", "i", 70, CLARO), ("menor?", "g", 70, BR)], W / 2, 300, "center", 0.12)
    for i, (k, s1, s2, cor) in enumerate((("s12.b", "aproximou ↑", "f' maior que f", E.COR), ("s12.c", "afastou ↓", "f' menor que f", GRAVE))):
        x = 560 + i * 800
        E.foco(c, t, C[k], 0.5, lambda a, x=x, s1=s1, cor=cor: E.pilula(c, s1, x, 480, 76, "g", fundo=cor, a=a, cor=BR))
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, x=x, s2=s2: centro(c, s2, x, 610, 60, "b", BR, a))
    E.frase(c, t, C["s12.d"], ps("corta", "i", 64, CLARO) + [("metade", "g", 64, BR)] + ps("das alternativas e escolhe os sinais", "i", 64, CLARO), W / 2, 780, "center", 0.1)
    E.frase(c, t, C["s12.e"], [("não", "g", 56, ERRADO), ("basta:", "i", 58, CLARO)] + ps("um vem e o outro foge —", "i", 58, CLARO) + [("monte a fórmula", "g", 56, BR)],
            W / 2, 950, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s13.a"], [("sirene", "i", 76)], XE, 350)
    E.foco(c, t, C["s13.a"] + 0.3, 0.5, lambda a: F.medida(c, 600, "Hz", XE + 290, 350, 90, COR, a))
    E.frase(c, t, C["s13.a"] + 1.2, ps("se aproxima; você parado", "i", 56, TINTA2), XE, 440, passo=0.08)
    E.frase(c, t, C["s13.b"], [("ouve", "i", 76)], XE, 570)
    E.foco(c, t, C["s13.b"] + 0.3, 0.5, lambda a: F.medida(c, 680, "Hz", XE + 290, 570, 90, COR, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.escreve(c, "v =", XE, 700, 72, "g", TINTA, a), F.medida(c, 340, "m/s", XE + 150, 700, 72, TINTA, a)))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: (linha_sub(c, "v_f = ?", XE, 860, 100, COR, a)))
    if t < C["s14"]:
        y = 760
        tt0 = C["s13.a"]
        x = lambda tt: lerp(980, 1520, ease_io(prog(tt, tt0, 9)))
        F.chao(c, 950, 1840, y, ep(t, tt0, 0.4)) if t >= tt0 else None
        frentes(c, t, tt0, lambda te: (x(te), y - 100), vs=240, dt=0.45, rmax=420, a=0.6)
        E.foco(c, t, tt0, 0.5, lambda a: ambulancia(c, x(t), y, 200, a))
        E.foco(c, t, tt0 + 0.3, 0.5, lambda a: pessoa(c, 1760, y, 0.8, a))
    else:
        E.relogio(c, t, C["s14.a"], cx=1460, cy=400, r=190)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: E.pilula(c, "dica: compare 680 com 600", 1460, 880, 50, "g", fundo=TINTA, a=a, cor=BR))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s15():
        E.foco(c, t, C["s15.a"], 0.5, lambda a: E.pilula(c, "se aproxima: − embaixo", XE + 300, 200, 54, "g", fundo=E.COR, a=a, cor=BR))
        formula_sub_em(c, t, C["s15.b"], "680 = 600 ·", "340", "340 − v_f", XE, 450, 110, TINTA)
        E.foco(c, t, C["s15.c"], 0.5, lambda a: centro(c, "÷ 600 nos dois lados", W / 2, 640, 56, "i", TINTA2, a))
        E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "f{680}{600} = f{17}{15}", XE, 860, 110, "g", COR, a))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    formula_sub_em(c, t, C["s16.a"], "", "340", "340 − v_f", XE, 260, 100, TINTA, pos="= f{17}{15}")
    E.foco(c, t, C["s16.a"] + 1.6, 0.5, lambda a: E.formula(c, "340 = 20 · 17", XE, 460, 84, "g", TINTA2, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.escreve(c, "de baixo:", XE, 600, 70, "i", TINTA, a), E.formula(c, "20 · 15 = 300", XE + 330, 600, 84, "g", COR, a)))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: (linha_sub(c, "340 − v_f = 300", XE, 760, 84, TINTA, a)))
    bola_txt(c, t, C["s16.d"], "40 m/s", 1450, 560, 160, 74)
    pilula(c, t, C["s16.e"], "= 144 km/h", 1450, 820, 60, TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s17.a", [("aproximou:", "g", 66), ("agudo", "g", 66, COR), ("·", "g", 66, TINTA2), ("afastou:", "g", 66), ("grave", "g", 66, GRAVE)]),
                 ("s17.b", [("a", "i", 66), ("sirene", "i", 66), ("não", "g", 62), ("muda:", "g", 62), ("muda", "i", 66), ("o", "i", 66), ("que", "i", 66), ("chega", "i", 66)]),
                 ("s17.c", [("o", "i", 66), ("sinal", "g", 62), ("leva", "i", 66), ("a", "i", 66), ("resposta", "i", 66), ("para", "i", 66), ("o", "i", 66), ("lado", "i", 66), ("certo", "g", 62, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("praticando:", "i", 100), ("som", "g", 110, COR)], XE, 400, passo=0.15)
    for i, s in enumerate(("decibéis", "instrumentos", "ressonância", "Doppler")):
        ti = C["s18.b"] + 0.4 * i
        E.foco(c, t, ti, 0.4, lambda a, s=s, i=i: E.pilula(c, s, XE + 160 + (i % 2) * 420, 560 + (i // 2) * 120, 52, "g", fundo=TINTA if i < 3 else E.COR, a=a, cor=BR))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, porque=b_porque, formula=b_formula, exemplo=b_exemplo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
