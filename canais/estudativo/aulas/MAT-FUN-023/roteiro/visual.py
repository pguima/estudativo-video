"""Visual — Estudativo · MAT-FUN-023: inequações produto e quociente (quadro de sinais).

Linguagem visual da trilha Funções (MAT-FUN-001): entrada / x em índigo, saída / y em preto; texto à esquerda; erro em vermelho.
Como na MAT-FUN-011 e 022: positivo = bolinha "+" verde, negativo = bolinha "−" vermelha, com o trecho da reta na mesma cor;
a solução vai na reta na cor da matéria (bolinha cheia = a ponta entra, aberta = fica de fora, seta = segue para sempre).
Nesta aula, o quadro de sinais (peça local, não existe no kit): reta-guia no alto com os zeros −2, 1 e 3 alinhados e em ordem
(o quadro não é em escala: os zeros ficam igualmente espaçados); guias tracejadas descendo de cada zero; uma linha por fator
(rótulo à esquerda, bolinha "0" preta no zero dele, um sinal em cada pedaço); a linha do resultado numa faixa da cor da matéria;
no resultado, bolinha cheia onde o de cima zera e bolinha aberta vermelha onde o de baixo zera ("÷ 0").
A coluna da vez (o pedaço que se multiplica) ganha uma faixa em pé.
Peças locais: quadro(), linha_fator(), sinal_bola(), coluna(), resultado(), reta_q(), solucao(), sinais(), pal()."""
import json
import math
import re
from pathlib import Path
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
POS, NEG = CERTO, ERRADO
ARQUIVO_FINAL = "estudativo_MAT-FUN-023_inequacoes_produto_e_quociente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "quadro", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD500"
ESCURO = "#0B0B16"
VERT = "#F2B705"
CA, CB, CC = COR, TINTA2, TINTA

F = lambda x: (x - 1) * (x + 2) / (x - 3)
G = lambda x: (x + 3) * (x - 2) / (x - 5)
sg = lambda v: "+" if v > 0 else "−"
assert [sg(F(x)) for x in (-3, 0, 2, 4)] == ["−", "+", "−", "+"] and F(1) == 0 and F(-2) == 0
assert [sg(x + 2) for x in (-3, 0, 2, 4)] == ["−", "+", "+", "+"] and [sg(x - 1) for x in (-3, 0, 2, 4)] == ["−", "−", "+", "+"]
assert [sg(x - 3) for x in (-3, 0, 2, 4)] == ["−", "−", "−", "+"] and (2 - 1) * (2 + 2) / (2 - 3) == -4
assert [sg(G(x)) for x in (-4, 0, 3, 6)] == ["−", "+", "−", "+"] and G(-3) == 0 and G(2) == 0

INEQ = "f{(x − 1)(x + 2)}{x − 3} ≥ 0"
QX0, QX1, QY = 560, 1740, 300
LY = (430, 540, 650)
RYQ = 790
AY = 950  # reta da resposta
ZEROS = (-2, 1, 3)
LINHAS = (("x + 2", 0), ("x − 1", 1), ("x − 3", 2))


def zx(i):
    return QX0 + (i + 1) * (QX1 - QX0) / 4


def cx(j):
    b = [QX0] + [zx(i) for i in range(3)] + [QX1]
    return (b[j] + b[j + 1]) / 2


def sinal_fator(zi, j):
    return "−" if j <= zi else "+"


RES = tuple(sg(F(x)) for x in (-3, 0, 2, 4))

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def pal(sid, palavra, n=0, padrao=None):
    """instante em que a palavra é dita na cena (n-ésima ocorrência); sem achar, usa padrao"""
    for s in _TEMPOS["scenes"]:
        if s["id"] != sid:
            continue
        k = 0
        for tk in s["tokens"]:
            if re.sub(r"[^\wçãõáéíóúâêô]", "", tk["disp"].lower()) == palavra:
                if k == n:
                    return s["start"] + tk["t0"]
                k += 1
    return padrao


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, "g", a=0)


def eixos(c, t, P, tx, ty=None, tg=None, marcas=None, nx="x", ny="y", size=36, escuro=False):
    """plano em etapas (o da MAT-FUN-001): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty, com o nome da grandeza"""
    ty = tx if ty is None else ty
    x, y, w, h_ = P.caixa
    mx, my = marcas
    ce, cs, ct = (CLARO, BR, CLARO) if escuro else (ENT, SAI, TINTA2)
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8) * (0.18 if escuro else 1)
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h_, CLARO if escuro else FIO, q, 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), CLARO if escuro else FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ce, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, nx, x + w + 30 - E.larg(nx, "i", 46), P.oy - 24, 46, "i", ce, a))
        for i, v in enumerate(mx):
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ce, a, 4),
                centro(c, E._num(v), X, P.oy + 14 + size, size, "b", ct, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h_ + 10, P.ox, y - 44, cs, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, ny, P.ox + 22, y - 16, 46, "i", cs, a))
        for i, v in enumerate(my):
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, cs, a, 4),
                E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", ct, a)), sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto"""
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", TINTA if not cores else cx_), (xv, cx_), (", ", TINTA if not cores else cx_), (yv, cy_), (")", TINTA if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    if c is None or a <= 0:
        return w
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def anel(c, t, t0, X, Y, cor=None, d=0.9):
    p = prog(t, t0, d)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def lei(c, partes, x, y, size, a=1.0, align="left"):
    """lei escrita por partes [(texto, cor)]; devolve [(x0, x1)] de cada parte"""
    w = sum(larg_f(s, size) for s, _ in partes)
    xx = x - w / 2 if align == "center" else x
    pos = []
    for s, cor in partes:
        lw = larg_f(s, size)
        if a > 0 and c is not None:
            E.formula(c, s, xx, y, size, "g", cor, a)
        pos.append((xx, xx + lw))
        xx += lw
    return pos


def lei_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: lei(c, partes, x, y, size, a, align))
    return lei(None, partes, x, y, size, 0, align)


def sob_parte(c, t, t0, pos, i, y, rot, cor, size=50, apara=0):
    """chave sob a parte i da lei (pos = o que lei() devolveu) com o rótulo embaixo; apara corta o sinal da esquerda"""
    x0, x1 = pos[i]
    x0 += apara
    p = ep(t, t0, 0.5)
    if p > 0:
        E.chave(c, x0 + 6, x1 - 2, y + 28, cor, p, 22, 5)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.formula(c, rot, (x0 + x1) / 2, y + 28 + 22 + size + 6, size, "g", cor, a, "center"))


def fsub(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """E.formula com índice no começo: "t_v = f{−b}{2a}" escreve t com o v pequeno embaixo"""
    if len(s) < 3 or s[1] != "_":
        if c is None:
            return larg_f(s, size)
        return E.formula(c, s, x, y, size, estilo, cor, a, align)
    le, sub, rest = s[0], s[2], s[3:]
    wx, ws, wr = E.larg(le, estilo, size), E.larg(sub, estilo, size * 0.55), larg_f(rest, size)
    w = wx + ws + size * 0.06 + wr
    if a <= 0 or c is None:
        return w
    x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
    E.escreve(c, le, x0, y, size, estilo, cor or TINTA, a)
    E.escreve(c, sub, x0 + wx + size * 0.02, y + size * 0.2, size * 0.55, estilo, cor or TINTA, a)
    E.formula(c, rest, x0 + wx + ws + size * 0.06, y, size, estilo, cor or TINTA, a)
    return w


def fml(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fsub(c, s, x, y, size, "g", cor, a, align))


def vertice(c, t, t0, P_, xv, yv, rot=None, size=44, abaixo=True):
    """o vértice: esfera amarela com anel, e o par embaixo (ou em cima)"""
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        X, Y = P_(xv, yv)
        c.drawCircle(X, Y, 19 * k, M.paint(VERT))
        c.drawCircle(X, Y, 19 * k, M.paint(TINTA, 1.0, stroke=4))
        anel(c, t, t0, X, Y, VERT)
        if rot:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, rot[0], rot[1], X, Y + (78 if abaixo else -40), size, a, "center"))


def caixa_par(c, xv, yv, X, Y, size, a, align="left"):
    """par com fundo de papel (legível sobre a grade e a curva)"""
    w = par(None, xv, yv, 0, 0, size, 0)
    x0 = X - w / 2 if align == "center" else X - w if align == "right" else X
    M.rrect(c, x0 - 10, Y - size * 0.95, w + 20, size * 1.3, 12, "#F4F3EF", 0.92 * a)
    par(c, xv, yv, x0, Y, size, a)


def regua(c, t, t0, P_, xv, cor=ENT, a=1.0):
    """régua tracejada em pé no x do vértice (a da MAT-FUN-006 e 018)"""
    p = ep(t, t0, 0.8)
    if p > 0 and a > 0:
        x, y, w, h_ = P_.caixa
        X = P_.x(xv)
        M.line(c, X, y + h_ + 10, X, lerp(y + h_ + 10, y - 20, p), cor, a * 0.8, 5, dash=[18, 12])


def guia(c, t, t0, P_, xv, yv, eixo, cor=None, d=0.6, largura=6, a=1.0):
    """tracejado do ponto até o eixo: "x" = até o eixo x (índigo, o quando), "y" = até o eixo y (preto, o valor)"""
    q = ease_io(prog(t, t0, d))
    if q <= 0 or a <= 0:
        return
    X, Y = P_(xv, yv)
    if eixo == "x":
        M.line(c, X, Y, X, P_.oy, cor or ENT, a, largura, dash=E.TRACO, progress=q)
    else:
        M.line(c, X, Y, P_.ox, Y, cor or SAI, a, largura, dash=E.TRACO, progress=q)


def marca_eixo(c, t, t0, P_, s, v, eixo, cor, size=40, a=1.0):
    """o valor lido ganha pílula no eixo: no x (embaixo) ou no y (à esquerda)"""
    if eixo == "x":
        cx, cy = P_.x(v), P_.oy + 52
    else:
        cx, cy = P_.ox - 22 - E.larg(s, "g", size) / 2 - size * 0.55, P_.y(v)
    E.foco(c, t, t0, 0.4, lambda q: E.pilula(c, s, cx, cy, size, "g", fundo=cor, a=q * a), sobe=0)


def trecho(c, t, t0, P_, fn, a_, b_, cor, d=0.9, largura=13):
    """repinta um pedaço da curva (sobe = verde, desce = vermelho), da esquerda para a direita (MAT-FUN-007)"""
    E.curva(c, t, t0, P_, fn, a_, b_, d=d, cor=cor, largura=largura)




# ---------------- peças da aula: sinais e solução (as da MAT-FUN-022) ----------------
def sinal_bola(c, X, Y, s, k=1.0, r=30, a=1.0):
    """bolinha do sinal: "+" verde, "−" vermelha"""
    if k <= 0 or a <= 0:
        return
    E.bola(c, X, Y, r * k, POS if s == "+" else NEG, a)
    centro(c, s, X, Y + r * 0.6 * k, r * 1.7 * k, "g", BR, a)


def sinal_em(c, t, t0, X, Y, s, r=30, a=1.0):
    k = ease_back(prog(t, t0, 0.4))
    sinal_bola(c, X, Y, s, k, r, a)


def solucao(c, t, t0, vx, y, ini, fim, fi=False, ff=False, cor=None, x0=QX0, x1=QX1, d=0.6, fundo=None):
    """trecho da solução na reta: None = segue até a ponta com seta; fi/ff = bolinha cheia (a ponta entra)"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or COR
    fundo = fundo or E.PAPEL
    xa = vx(ini) if ini is not None else x0 - 30
    xb = vx(fim) if fim is not None else x1 + 40
    if ini is None:
        xm = lerp(xb, xa, p); M.line(c, xm, y, xb, y, cor, 1.0, 12)
    else:
        xm = lerp(xa, xb, p); M.line(c, xa, y, xm, y, cor, 1.0, 12)
    if p > 0.95:
        if ini is None:
            M.line(c, xa, y, xa + 26, y - 18, cor, 1.0, 8); M.line(c, xa, y, xa + 26, y + 18, cor, 1.0, 8)
        if fim is None:
            M.line(c, xb, y, xb - 26, y - 18, cor, 1.0, 8); M.line(c, xb, y, xb - 26, y + 18, cor, 1.0, 8)
    q_ = ep(t, t0, 0.3)
    for v, fe in ((ini, fi), (fim, ff)):
        if v is None:
            continue
        X = vx(v)
        c.drawCircle(X, y, 17, M.paint(cor if fe else fundo, q_))
        c.drawCircle(X, y, 17, M.paint(cor, q_, stroke=6))


def reta_q(c, t, t0, zeros, y, x0=QX0, x1=QX1, tz=None, escuro=False, acima=False, size=46):
    """reta fora de escala com os zeros igualmente espaçados; devolve valor → x (só para os zeros)"""
    tinta = BR if escuro else TINTA
    pos = {v: x0 + (i + 1) * (x1 - x0) / (len(zeros) + 1) for i, v in enumerate(zeros)}
    if t >= t0:
        p = ep(t, t0, 0.6)
        M.arrow(c, x0 - 40, y, x1 + 60, y, tinta, p, 5, 18, p)
    for i, v in enumerate(zeros):
        ti = tz[i] if tz else t0 + 0.2 + 0.1 * i
        X = pos[v]
        E.foco(c, t, ti, 0.4, lambda a, X=X, v=v: (M.line(c, X, y - 20, X, y + 20, tinta, a, 5),
                                                  centro(c, E._num(v), X, y - 40 if acima else y + 80, size, "g", tinta, a)), sobe=6)
    return lambda v: pos[v]


def sinais_q(c, t, vx, y, zeros, sgs, ts, x0=QX0, x1=QX1, r=30):
    """sinal de cada pedaço da reta: faixa colorida logo acima e bolinha (como na MAT-FUN-022)"""
    pts = [x0 - 30] + [vx(v) for v in zeros] + [x1 + 40]
    for i, (s, ti) in enumerate(zip(sgs, ts)):
        if ti is None or t < ti:
            continue
        cor = POS if s == "+" else NEG
        xa, xb = pts[i], pts[i + 1]
        p = ease_io(prog(t, ti, 0.5))
        M.line(c, xa + 8, y - 34, lerp(xa + 8, xb - 8, p), y - 34, cor, 0.9, 10)
        sinal_em(c, t, ti + 0.15, (xa + xb) / 2, y - 92, s, r)


# ---------------- o quadro de sinais ----------------
def guia_q(c, t, t0, tz):
    """reta-guia no alto com os zeros em ordem (acima dela) e as guias tracejadas descendo"""
    vx = reta_q(c, t, t0, ZEROS, QY, tz=tz, acima=True)
    for i in range(3):
        p = ep(t, tz[i] + 0.2, 0.6)
        if p > 0:
            M.line(c, zx(i), QY + 20, zx(i), lerp(QY + 20, RYQ + 50, p), TINTA2, 0.45, 3, dash=[10, 10])
    return vx


def linha_fator(c, t, y, rot, zi, tl, tz, tmenos, tmais, a=1.0):
    """uma linha do quadro: rótulo, bolinha 0 no zero do fator, sinais nos pedaços"""
    E.foco(c, t, tl, 0.5, lambda q: E.formula(c, rot, XE, y + 22, 62, "g", TINTA, q * a))
    q_ = ep(t, tl, 0.5) * a
    if q_ > 0:
        M.line(c, QX0 - 30, y + 46, QX1 + 40, y + 46, FIO, q_, 2)
    kk = ease_back(prog(t, tz, 0.4))
    if kk > 0:
        c.drawCircle(zx(zi), y, 24 * kk, M.paint(TINTA, a))
        centro(c, "0", zx(zi), y + 14 * kk, 38 * kk, "g", BR, a)
    for j in range(4):
        s = sinal_fator(zi, j)
        t0 = (tmenos + 0.15 * j) if s == "−" else (tmais + 0.15 * (j - zi - 1))
        if t0 is not None and t >= t0:
            sinal_bola(c, cx(j), y, s, ease_back(prog(t, t0, 0.4)), 28, a)


def coluna(c, t, j, t0, t1=None, cor=None, alfa=0.12):
    a_ = ep(t, t0, 0.3) * (1 - ep(t, t1, 0.3) if t1 is not None else 1)
    if a_ > 0:
        b = [QX0 - 30] + [zx(i) for i in range(3)] + [QX1 + 40]
        M.rrect(c, b[j] + 10, QY + 60, b[j + 1] - b[j] - 20, RYQ + 50 - QY - 60, 18, cor or COR, alfa * a_)


def faixa_res(c, t, t0, a=1.0):
    q_ = ep(t, t0, 0.5) * a
    if q_ <= 0:
        return
    M.rrect(c, XE - 20, RYQ - 60, QX1 + 60 - XE, 120, 30, COR, 0.12 * q_)
    E.formula(c, "f{(x − 1)(x + 2)}{x − 3}", XE, RYQ + 18, 40, "g", COR, q_)


def quadro(c, t, C, a=1.0):
    """o quadro inteiro, com os instantes do roteiro"""
    tz = (C["s05.c"], C["s05.b"], C["s05.d"])
    guia_q(c, t, C["s05"] - 0.2, tz)
    tl = (C["s05.c"], C["s05.b"], C["s05.d"])
    for (rot, zi), y, tli in zip(LINHAS, LY, tl):
        linha_fator(c, t, y, rot, zi, tli, tli + 0.6, C["s06.c"], C["s06.d"], a)
    faixa_res(c, t, C["s07.a"], a)
    tc = (C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"])
    for j in range(4):
        coluna(c, t, j, tc[j], tc[j + 1] if j < 3 else C["s08"])
        if t >= tc[j] + 1.2:
            sinal_bola(c, cx(j), RYQ, RES[j], ease_back(prog(t, tc[j] + 1.2, 0.4)), 34, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.formula(c, INEQ, W / 2, 360, 120, "g", TINTA, a, "center"))
        E.frase(c, t, C["s01.b"], [("o", "i", 66), ("reflexo:", "i", 66), ("passar", "g", 70), ("multiplicando", "g", 70, COR)], W / 2, 560, "center")
        tb = C["s01.b"] + 1.6
        E.foco(c, t, tb, 0.5, lambda a: (E.formula(c, "(x − 1)(x + 2)", 600, 730, 92, "g", TINTA, a, "center"),
                                         E.formula(c, "0 · (x − 3)", 1340, 730, 92, "g", TINTA, a, "center")))
        # o ≥ que vira ≤
        vira = ease_io(prog(t, C["s01.c"] + 1.4, 0.8))
        if t >= tb:
            sim = "≥" if vira < 0.5 else "≤"
            cor = TINTA if vira < 0.5 else ERRADO
            sy = abs(1 - 2 * vira)
            c.save(); c.translate(970, 700); c.scale(1, max(0.05, sy)); c.translate(-970, -700)
            centro(c, sim, 970, 730, 110, "g", cor, ep(t, tb, 0.5))
            c.restore()
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "e se x − 3 for negativo?", W / 2, 880, 54, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("produtos", "g", 100, COR), ("e", "i", 90)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.8, [("divisões", "g", 100, COR)], XE, 580)
        E.frase(c, t, pal("s02", "quadro", 0, C["s02.a"] + 4.0), [("com", "i", 76), ("o", "i", 76), ("quadro", "g", 80), ("de", "i", 76), ("sinais", "g", 80)], XE, 740)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 76), ("precisa", "i", 76), ("de", "i", 76)], XE, 360)
    E.frase(c, t, C["s03.a"], [("3", "g", 220, COR), ("coisas", "i", 100)], XE, 600)
    x, w = 780, 1000
    for t0, y in ((C["s03.b"], 150), (C["s03.c"], 470), (C["s03.d"], 740)):
        p = ep(t, t0, 0.5)
        E.caixa_pontilhada(c, x, y, w, 300 if y == 150 else 240, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("sinal", "i", 50), ("da", "i", 50), ("afim:", "g", 54), ("à", "i", 50), ("direita", "g", 54), ("da", "i", 50), ("raiz,", "i", 50),
                                     ("sinal", "i", 50), ("do", "i", 50), ("a", "g", 56, COR)], x + 40, 225)
    if t >= C["s03.b"] + 1.0:
        vx = reta_q(c, t, C["s03.b"] + 1.0, (1,), 360, x0=x + 120, x1=x + w - 160, size=40)
        sinais_q(c, t, vx, 360, (1,), ("−", "+"), (pal("s03", "esquerda", 0, C["s03.b"] + 4.0), C["s03.b"] + 1.6), x0=x + 120, x1=x + w - 160, r=26)
        E.foco(c, t, C["s03.b"] + 1.2, 0.4, lambda a: E.formula(c, "a > 0", x + w - 110, 300, 44, "g", COR, a, "center"))
    E.frase(c, t, C["s03.c"] + 0.1, [("regra", "g", 60), ("de", "i", 56), ("sinais:", "g", 60)], x + 40, 560)
    E.foco(c, t, C["s03.c"] + 0.8, 0.5, lambda a: (E.escreve(c, "iguais", x + 40, 650, 52, "i", TINTA, a), sinal_bola(c, x + 260, 632, "+", 1, 26, a),
                                                  E.escreve(c, "diferentes", x + 360, 650, 52, "i", TINTA, a), sinal_bola(c, x + 650, 632, "−", 1, 26, a)))
    E.frase(c, t, C["s03.d"] + 0.1, [("união", "g", 60), ("de", "i", 56), ("intervalos:", "i", 56)], x + 40, 830)
    E.foco(c, t, C["s03.d"] + 0.6, 0.5, lambda a: formula_u(c, "[1, 2] ∪ [4, 5]", x + 40, 920, 60, "g", COR, a))
    q_ = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 960, q_), ep(t, C["s03.b"], 0.4))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    E.frase(c, t, C["s04"], ps("a ideia é simples", "i", 66, TINTA2), XE, 220)
    E.frase(c, t, C["s04.a"], [("o", "i", 62), ("sinal", "g", 66, COR), ("do", "i", 62), ("produto", "g", 66)], XE, 360)
    E.frase(c, t, C["s04.a"] + 1.4, ps("só depende do sinal de cada fator", "i", 54), XE, 450, passo=0.1)
    E.frase(c, t, C["s04.b"], [("÷", "g", 70, COR), ("segue", "i", 60), ("a", "i", 60), ("mesma", "i", 60), ("regra", "g", 66)], XE, 600)
    E.foco(c, t, C["s04.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 700, 780, 200, 44, COR, a),
                                             E.escreve(c, "não abra nada:", XE + 30, 785, 52, "i", BR, a),
                                             E.escreve(c, "onde cada fator é + ou −", XE + 30, 865, 52, "g", BR, a)))
    # à direita, as contas de sinal
    linhas = (((("−", "×", "−"), "+"), C["s04.a"] + 1.0), ((("+", "×", "−"), "−"), C["s04.a"] + 2.2),
              ((("−", "÷", "−"), "+"), C["s04.b"] + 0.6), ((("+", "÷", "−"), "−"), C["s04.b"] + 1.6))
    for i, ((ops, res), t0) in enumerate(linhas):
        y = 300 + i * 160
        E.foco(c, t, t0, 0.5, lambda a, ops=ops, res=res, y=y: (
            sinal_bola(c, 1180, y, ops[0], 1, 40, a), centro(c, ops[1], 1290, y + 26, 70, "g", TINTA, a),
            sinal_bola(c, 1400, y, ops[2], 1, 40, a), centro(c, "=", 1510, y + 26, 70, "g", TINTA, a),
            sinal_bola(c, 1630, y, res, 1, 40, a)))


# ---------------- quadro ----------------
def b_quadro(c, t, C, b):
    E.foco(c, t, C["s05"] - 0.2, 0.5, lambda a: E.formula(c, INEQ, QX1 + 40, 140, 50, "g", TINTA, a, "right"))
    quadro(c, t, C)
    # cabeçalho do passo
    passos = ((C["s05.a"], C["s06.a"], [("1.", "g", 56, COR), ("o", "i", 52), ("zero", "g", 56), ("de", "i", 52), ("cada", "i", 52), ("fator", "i", 52)]),
              (C["s06.a"], C["s07.a"], [("2.", "g", 56, COR), ("o", "i", 52), ("quadro:", "g", 56), ("−", "g", 60, NEG), ("antes,", "i", 52), ("+", "g", 60, POS), ("depois", "i", 52)]),
              (C["s07.a"], C["s08.a"], [("3.", "g", 56, COR), ("multiplique", "g", 56), ("de", "i", 52), ("cima", "i", 52), ("para", "i", 52), ("baixo", "i", 52)]),
              (C["s08.a"], None, [("4.", "g", 56, COR), ("escolha", "g", 56), ("os", "i", 52), ("pedaços", "i", 52), ("com", "i", 52), ("+", "g", 60, POS)]))
    for t0, t1, partes in passos:
        if t1 is None:
            E.saida(c, t, C["s09.e"] + 0.5, lambda partes=partes, t0=t0: E.frase(c, t, t0, partes, XE, 150, passo=0.08))
        else:
            E.saida(c, t, t1 - 0.1, lambda partes=partes, t0=t0: E.frase(c, t, t0, partes, XE, 150, passo=0.08))
    # os zeros, um por fator (na ordem da fala), com a pílula "zera em"
    for (rot, zi), y, tk in zip(LINHAS, LY, (C["s05.c"], C["s05.b"], C["s05.d"])):
        E.saida(c, t, C["s06"] - 0.1, lambda y=y, tk=tk, zi=zi: E.foco(c, t, tk + 0.3, 0.4, lambda a: E.pilula(c, f"zera em {E._num(ZEROS[zi])}", XE + 400, y + 2, 34, "g",
                                                                                                         fundo=TINTA, a=a)))
    # os 4 pedaços
    q_ = ep(t, C["s05.e"], 0.4) * (1 - ep(t, C["s06.a"], 0.4))
    if q_ > 0:
        for j in range(4):
            E.pilula(c, f"{j + 1}º", cx(j), QY + 50, 32, "g", fundo=COR, a=q_)
    # os zeros em ordem: um pulso em cada um
    for i, tk in enumerate((C["s06.b"], pal("s06", "um", 0, C["s06.b"] + 1.0), pal("s06", "três", 0, C["s06.b"] + 2.0))):
        if t >= tk:
            anel(c, t, tk, zx(i), QY, COR)
    if t < C["s08"]:
        return
    # passo 4: os pedaços com + e as pontas
    for j in (1, 3):
        coluna(c, t, j, C["s08.b"], None, POS, 0.14)
    for i in (0, 1):
        kk = ease_back(prog(t, C["s08.c"] + 0.3 * i, 0.4))
        if kk > 0:
            c.drawCircle(zx(i), RYQ, 22 * kk, M.paint(COR))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "0 serve: fechada", (zx(0) + zx(1)) / 2, RYQ + 90, 34, "g", fundo=COR, a=a))
    if t < C["s09"]:
        return
    kk = ease_back(prog(t, C["s09.a"], 0.4))
    if kk > 0:
        c.drawCircle(zx(2), RYQ, 22 * kk, M.paint(E.PAPEL))
        c.drawCircle(zx(2), RYQ, 22 * kk, M.paint(ERRADO, 1, stroke=7))
    E.saida(c, t, C["s09.c"], lambda: E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "÷ 0: não existe", zx(2), RYQ + 90, 34, "g", fundo=ERRADO, a=a)))
    E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: E.pilula(c, "÷ 0: sempre aberta", zx(2), RYQ + 90, 34, "g", fundo=ERRADO, a=a))
    vx = reta_q(c, t, C["s09.d"] - 0.4, ZEROS, AY, size=40)
    solucao(c, t, C["s09.d"], vx, AY, -2, 1, True, True)
    solucao(c, t, C["s09.e"], vx, AY, 3, None)
    E.foco(c, t, C["s09.e"] + 0.6, 0.5, lambda a: (M.rrect(c, XE - 20, 80, 560, 110, 34, COR, a),
                                                   formula_u(c, "[−2, 1] ∪ ]3, +∞[", XE + 260, 156, 56, "g", BR, a, "center")))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], ps("voltando ao erro do começo", "i", 60, TINTA2), XE, 200)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "(x − 1)(x + 2) ≥ 0", XE, 330, 76, "g", ERRADO, a))
    E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: E.escreve(c, "sem o x − 3", XE + 760, 325, 46, "i", TINTA2, a))
    fml(c, t, C["s10.b"], "x ≤ −2  ou  x ≥ 1", XE, 460, 72, ERRADO)
    vx = E.reta(c, t, C["s10.b"], XE + 60, W - 200, AY - 60, -4, 5, [-2, 1, 2, 3], E._num, size=46)
    solucao(c, t, C["s10.b"] + 0.4, vx, AY - 60, None, -2, ff=True, cor=ERRADO, x0=XE + 60, x1=W - 200)
    solucao(c, t, C["s10.b"] + 0.7, vx, AY - 60, 1, None, fi=True, cor=ERRADO, x0=XE + 60, x1=W - 200)
    kk = ease_back(prog(t, C["s10.c"], 0.5))
    if kk > 0:
        c.drawCircle(vx(2), AY - 60, 24 * kk, M.paint(TINTA))
        E.pilula(c, "x = 2", vx(2), AY - 125, 36, "g", fundo=TINTA, a=min(1, kk))
    fml(c, t, C["s10.d"], "f{1 · 4}{−1} = −4", XE, 640, 72, TINTA)
    E.foco(c, t, C["s10.e"], 0.4, lambda a: E.pilula(c, "negativo: o 2 não serve", XE + 820, 615, 44, "g", fundo=NEG, a=a))
    E.foco(c, t, C["s10.f"], 0.6, lambda a: (M.rrect(c, XE - 20, 680, 1340, 96, 40, CERTO, a),
                                             E.escreve(c, "nunca passe multiplicando o que tem x: monte o quadro", XE + 20, 745, 46, "g", BR, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    y = 800
    vx = reta_q(c, t, C["s11"], ZEROS, y, x0=360, x1=1640, escuro=True, size=52)
    if t < C["s12"]:
        tr = (pal("s11", "antes", 0, C["s11.c"] + 5.0), pal("s11", "entre", 1, C["s11.c"] + 3.6), pal("s11", "entre", 0, C["s11.c"] + 1.8), C["s11.c"])
        sinais_q(c, t, vx, y, ZEROS, ("−", "+", "−", "+"), tr, x0=360, x1=1640, r=34)
        # o salto da troca, da direita para a esquerda
        cxs = [(a_ + b_) / 2 for a_, b_ in zip([330] + [vx(v) for v in ZEROS], [vx(v) for v in ZEROS] + [1680])]
        for j, tk in ((3, tr[1]), (2, tr[2]), (1, tr[0])):
            p = ep(t, tk - 0.4, 0.5)
            if p > 0:
                E.arco(c, (cxs[j] + cxs[j - 1]) / 2, y - 140, (cxs[j] - cxs[j - 1]) / 2 * 0.8, 0, -180 * p, AMARELO, 5)
        E.frase(c, t, C["s11"], ps("agora, o atalho, sem quadro", "i", 62, CLARO), W / 2, 200, "center")
        E.frase(c, t, C["s11.a"], [("depois", "i", 66, CLARO), ("da", "i", 66, CLARO), ("maior", "g", 70, BR), ("raiz:", "i", 66, CLARO), ("tudo", "g", 70, BR), ("+", "g", 80, POS)],
                W / 2, 310, "center")
        E.frase(c, t, C["s11.b"], [("para", "i", 62, CLARO), ("a", "i", 62, CLARO), ("esquerda,", "i", 62, CLARO), ("troca", "g", 70, AMARELO), ("a", "i", 62, CLARO), ("cada", "i", 62, CLARO),
                                   ("raiz", "g", 66, BR)], W / 2, 410, "center")
        return
    sinais_q(c, t, vx, y, ZEROS, ("−", "+", "−", "+"), (C["s12"] - 1,) * 4, x0=360, x1=1640, r=34)
    E.frase(c, t, C["s12.a"], [("à", "i", 58, CLARO), ("direita", "g", 62, BR), ("de", "i", 58, CLARO), ("tudo:", "i", 58, CLARO), ("cada", "i", 58, CLARO), ("fator", "i", 58, CLARO),
                               ("é", "i", 58, CLARO), ("+", "g", 70, POS)], XE, 200)
    E.frase(c, t, C["s12.b"], [("passou", "i", 58, CLARO), ("uma", "i", 58, CLARO), ("raiz:", "i", 58, CLARO), ("só", "g", 62, AMARELO), ("1", "g", 62, AMARELO), ("fator", "i", 58, CLARO),
                               ("muda", "g", 62, BR)], XE, 300)
    E.frase(c, t, C["s12.c"], [("não", "g", 62, ERRADO), ("vale:", "i", 58, CLARO)], XE, 430)
    E.foco(c, t, C["s12.c"] + 0.8, 0.4, lambda a: E.formula(c, "3 − x", XE + 330, 430, 64, "g", BR, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: (E.escreve(c, "ou", XE + 600, 430, 56, "i", CLARO, a), E.formula(c, "(x − 1)^2", XE + 700, 430, 64, "g", BR, a)))
    E.foco(c, t, C["s12.d"] + 1.0, 0.4, lambda a: E.escreve(c, "o quadrado não troca de sinal", XE + 700, 510, 40, "i", CLARO, a))
    E.foco(c, t, C["s12.e"], 0.5, lambda a: E.pilula(c, "faça o quadro", 1500, 430, 50, "g", fundo=CERTO, a=a))


# ---------------- questão ----------------
INEQ_Q = "f{(x + 3)(x − 2)}{x − 5} ≤ 0"


def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 70, COR), XE, 220)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, INEQ_Q, XE, 520, 120, "g", TINTA, a))
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1500, cy=460, r=180)


def b_resposta(c, t, C, b):
    E.foco(c, t, C["s15"], 0.5, lambda a: E.formula(c, INEQ_Q, XE, 230, 76, "g", TINTA, a))
    y = 640
    zs = (-3, 2, 5)
    tz = (C["s15.a"], pal("s15", "dois", 0, C["s15.a"] + 1.0), pal("s15", "cinco", 0, C["s15.a"] + 2.0))
    vx = reta_q(c, t, C["s15.a"] - 0.3, zs, y, tz=tz)
    E.frase(c, t, pal("s15", "todo", 0, C["s15.a"] + 3.0), ps("todo fator com +x: vale o atalho", "i", 50, TINTA2), XE, 380, passo=0.08)
    tr = (pal("s15", "antes", 0, C["s15.b"] + 5.0), pal("s15", "entre", 1, C["s15.b"] + 3.6), pal("s15", "entre", 0, C["s15.b"] + 1.8), C["s15.b"])
    sinais_q(c, t, vx, y, zs, ("−", "+", "−", "+"), tr)
    if t < C["s16"]:
        return
    for j_, (xa, xb) in enumerate(((QX0 - 30, vx(-3)), (vx(2), vx(5)))):
        a_ = ep(t, C["s16.a"], 0.4)
        if a_ > 0:
            M.rrect(c, xa + 6, y - 150, xb - xa - 12, 190, 20, NEG, 0.12 * a_)
    E.frase(c, t, C["s16.a"], [("≤", "g", 66, COR), ("0:", "g", 66, COR), ("os", "i", 58), ("pedaços", "i", 58), ("com", "i", 58), ("−", "g", 70, NEG)], XE, 470)
    solucao(c, t, C["s16.d"], vx, y + 160, None, -3, ff=True)
    solucao(c, t, C["s16.e"], vx, y + 160, 2, 5, True, False)
    if t >= C["s16.d"] - 0.3:
        p = ep(t, C["s16.d"] - 0.3, 0.5)
        M.arrow(c, QX0 - 40, y + 160, QX1 + 60, y + 160, TINTA, p, 5, 18, p)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "−3 e 2: fechadas (em cima)", 760, y + 260, 36, "g", fundo=COR, a=a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "5: aberta (embaixo)", 1420, y + 260, 36, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s16.e"] + 0.6, 0.5, lambda a: (M.rrect(c, XE - 20, y + 310, 560, 110, 34, COR, a),
                                                   formula_u(c, "]−∞, −3] ∪ [2, 5[", XE + 260, y + 386, 56, "g", BR, a, "center")))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s17.a", [("ache", "i", 72), ("o", "i", 72), ("zero", "g", 78), ("de", "i", 72), ("cada", "i", 72), ("fator", "g", 78)]),
                 ("s17.b", [("multiplique", "g", 78, COR), ("os", "i", 72), ("sinais", "i", 72), ("no", "i", 72), ("quadro", "g", 78)]),
                 ("s17.c", [("o", "i", 72), ("zero", "g", 78), ("de", "i", 72), ("baixo:", "i", 72), ("sempre", "i", 72), ("aberto", "g", 78, ERRADO)]))
        for i, (kk, partes) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[kk], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                          E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[kk] + 0.1, partes, 340, y, passo=0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s18.a"], [("sistema", "g", 82, COR), ("de", "i", 76), ("inequações", "g", 82, COR)], XE, 410)
    E.sistema(c, t, C["s18.b"], ["x − 1 > 0", "x^2 − 5x + 6 < 0"], XE + 20, 570, 70)
    E.frase(c, t, C["s18.c"], [("empilhe", "g", 66), ("as", "i", 62), ("retas", "g", 66, COR)], XE, 820)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s18.d"] + 0.2, 0.4))
    E.frase(c, t, C["s18.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, quadro=b_quadro, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)


def formula_u(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """E.formula que desenha o ∪ à mão (a fonte não tem o símbolo); devolve a largura"""
    partes = s.split("∪")
    wu = size * 0.62
    ws = [larg_f(p, size) for p in partes]
    w = sum(ws) + wu * (len(partes) - 1)
    if c is None or a <= 0:
        return w
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for i, (p, wp) in enumerate(zip(partes, ws)):
        E.formula(c, p, xx, y, size, estilo, cor, a)
        xx += wp
        if i < len(partes) - 1:
            u = skia.Path()
            l, r_, top, bot = xx + size * 0.1, xx + wu - size * 0.1, y - size * 0.62, y - size * 0.02
            u.moveTo(l, top); u.lineTo(l, bot - (r_ - l) / 2)
            u.arcTo(skia.Rect.MakeLTRB(l, bot - (r_ - l), r_, bot), 180, -180, False)
            u.lineTo(r_, top)
            c.drawPath(u, M.paint(cor or TINTA, a, stroke=size * 0.11, cap_round=True))
            xx += wu
    return w
