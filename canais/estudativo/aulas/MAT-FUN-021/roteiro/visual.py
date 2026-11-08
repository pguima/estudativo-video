"""Visual — Estudativo · MAT-FUN-021: achar a lei da parábola.

Linguagem visual da trilha Funções (MAT-FUN-001): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Como na MAT-FUN-016 a 020: parábola de a > 0 índigo; raízes como anéis no eixo x (amarelos no palco escuro); o vértice é a esfera
amarela (VERT); régua tracejada em pé no x do vértice; o trecho da lei de que se fala ganha realce (realce(), MAT-EQU-005).
Nesta aula: o palpite (x − 1)(x − 5) é a curva tracejada cinza; a família y = a(x − 1)(x − 5) é uma curva que respira (o a muda
com o tempo) presa nas duas raízes; o ponto que decide o a pulsa em preto no eixo y; as três formas da lei empilhadas com
etiqueta (fatorada, com a, b e c, do vértice); h em índigo (é x) e k em preto (é y).
Peças locais: as da trilha (eixos(), par(), lei(), fsub(), vertice(), regua(), guia(), marca_eixo(), raiz(), realce()) + forma(), pal()."""
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
CA, CB, CC = COR, TINTA2, TINTA  # cores de a, b e c
SOBE, DESCE = CERTO, ERRADO
ARQUIVO_FINAL = "estudativo_MAT-FUN-021_achar_a_lei_da_parabola.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fatorada", "vertice", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERT = "#F2B705"
ESCURO = "#0B0B16"

f = lambda x: 2 * (x - 1) * (x - 5)
g = lambda x: (x - 1) * (x - 5)
q = lambda x: 2 * (x + 2) * (x - 4)
assert f(0) == 10 and g(0) == 5 and 10 / 5 == 2 and all(f(x) == 2 * x * x - 12 * x + 10 == 2 * (x - 3) ** 2 - 8 for x in range(-9, 9))
assert all(g(x) == x * x - 6 * x + 5 for x in range(-9, 9)) and (1 + 5) / 2 == 3 and f(3) == -8
assert (-3 - 3) ** 2 == 36 and 2 * 36 - 8 == 64 and 1 * 5 == 5 and 2 * 5 * 1 == 10
assert q(0) == -16 and -2 * 4 == -8 and -16 / -8 == 2 and all(q(x) == 2 * x * x - 4 * x - 16 == 2 * (x - 1) ** 2 - 18 for x in range(-9, 9))
assert (-2 + 4) / 2 == 1

PL = (1080, 200, 700, 680)
PF = E.Plano(*PL, -1.5, 7, -10.5, 13.5)
MF = ([1, 2, 3, 4, 5, 6], [-8, 5, 10])
PQ = E.Plano(*PL, -3.5, 5.5, -21, 9)
MQ = ([-2, -1, 1, 2, 3, 4], [-16, -8])
FAT = "y = 2(x − 1)(x − 5)"
DES = "y = 2x^2 − 12x + 10"
VER = "y = 2(x − 3)^2 − 8"

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




def fw(s, size):
    return larg_f(s, size) if s else 0.0


def trecho_x(s, tr, x, size, align="left", n=0):
    """(x inicial, largura) de um trecho da fórmula s (o da MAT-EQU-005)"""
    xi = x - fw(s, size) / 2 if align == "center" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(tr, i0 + 1)
    return xi + fw(s[:i0], size), fw(tr, size) - size * 0.02


def realce(c, t, t0, s, tr, x, y, size, cor=None, align="left", n=0, t1=None):
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    x0, w = trecho_x(s, tr, x, size, align, n)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.18 * a)


def raiz(c, t, t0, P_, xv, cor=AMARELO, rot=None, size=40):
    """raiz como anel no eixo x, com o valor numa pílula embaixo"""
    if t < t0:
        return
    q = ease_back(prog(t, t0, 0.5))
    c.drawCircle(P_.x(xv), P_.oy, 22 * q, M.paint(cor, 1.0, stroke=7))
    anel(c, t, t0, P_.x(xv), P_.oy, cor)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, rot, P_.x(xv), P_.oy + 56, size, "g", fundo=cor, cor=ESCURO if cor == AMARELO else BR, a=a))




def plano_f(c, t, t0, escuro=False):
    eixos(c, t, PF, t0, tg=t0, marcas=MF, escuro=escuro)


def plano_q(c, t, t0):
    eixos(c, t, PQ, t0, tg=t0, marcas=MQ)


def ponto_y(c, t, t0, P_, yv, cor=SAI, pulsa=None, rot=None):
    """o ponto que sobra, no eixo y; pulsa = instante em que ele chama a atenção"""
    E.ponto(c, t, t0, P_, 0, yv, cor=cor, r=15)
    if pulsa is not None and t >= pulsa:
        anel(c, t, pulsa, P_.ox, P_.y(yv), cor)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, "0", rot, P_.ox + 30, P_.y(yv) - 22, 40, a))


def forma(c, t, t0, nome, s, y, size=70, cor=TINTA, x=XE, etq=TINTA2):
    """uma das três formas da lei: etiqueta pequena acima e a lei"""
    E.foco(c, t, t0, 0.5, lambda a: (E.escreve(c, nome, x, y - size - 18, 40, "i", etq, a),
                                    E.formula(c, s, x, y, size, "g", cor, a)))


def caixa_lei(c, t, t0, s, x, y, size, cor=COR, w=None):
    """a lei pronta numa caixa da cor da matéria"""
    w = w or fw(s, size) + 80
    E.foco(c, t, t0, 0.6, lambda a: (M.rrect(c, x - 20, y - size * 1.2, w, size * 1.75, 44, cor, a),
                                     E.formula(c, s, x + 20, y, size, "g", BR, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano_f(c, t, C["s01"])
        raiz(c, t, C["s01.a"] + 0.4, PF, 1, ENT, "1")
        raiz(c, t, C["s01.a"] + 0.8, PF, 5, ENT, "5")
        ponto_y(c, t, C["s01.b"] + 0.3, PF, 10, rot="10")
        E.curva(c, t, C["s01.c"] + 0.6, PF, f, -0.15, 6.15, d=1.4, cor=COR)
        E.frase(c, t, C["s01.a"], [("corta", "i", 70), ("o", "i", 70), ("x", "g", 80, ENT), ("no", "i", 70), ("1", "g", 84, ENT), ("e", "i", 70), ("no", "i", 70), ("5", "g", 84, ENT)],
                XE, 300)
        E.frase(c, t, C["s01.b"], [("corta", "i", 70), ("o", "i", 70), ("y", "g", 80), ("no", "i", 70), ("10", "g", 84)], XE, 430)
        E.frase(c, t, C["s01.c"], [("a", "i", 96), ("lei?", "g", 120, COR)], XE, 640)
        E.foco(c, t, C["s01.c"] + 1.4, 0.5, lambda a: E.formula(c, "y = ?", XE, 800, 110, "g", TINTA, a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 260)
        E.frase(c, t, C["s02.a"] + 1.2, [("a", "i", 90), ("lei", "g", 110, COR), ("pelas", "i", 90), ("raízes", "g", 100)], XE, 410)
        E.frase(c, t, pal("s02", "passa", 0, C["s02.a"] + 4.0), [("com", "i", 76), ("a,", "g", 80, CA), ("b", "g", 80, CB), ("e", "i", 76), ("c", "g", 80, CC)], XE, 550)
        E.frase(c, t, C["s02.b"], [("o", "i", 76), ("ponto", "g", 80), ("de", "i", 76), ("virada", "g", 80, VERT)], XE, 690)
        E.frase(c, t, C["s02.b"] + 1.2, ps("direto na lei", "i", 64, TINTA2), XE, 790)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 76), ("precisa", "i", 76), ("de", "i", 76)], XE, 360)
    E.frase(c, t, C["s03.a"], [("2", "g", 220, COR), ("coisas", "i", 100)], XE, 600)
    x, w = 820, 960
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 170, w, 260, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("raiz:", "g", 60, ENT), ("onde", "i", 56), ("corta", "i", 56), ("o", "i", 56), ("eixo", "i", 56), ("x", "g", 64, ENT)], x + 44, 270)
    E.foco(c, t, C["s03.b"] + 0.8, 0.5, lambda a: (M.arrow(c, x + 60, 370, x + 860, 370, ENT, a, 5, 20),
                                                  c.drawCircle(x + 300, 370, 18, M.paint(ENT, a, stroke=6)),
                                                  c.drawCircle(x + 620, 370, 18, M.paint(ENT, a, stroke=6))))
    p = ep(t, C["s03.c"], 0.5)
    E.caixa_pontilhada(c, x, 490, w, 450, p, prog_=p)
    E.frase(c, t, C["s03.c"] + 0.1, [("cada", "i", 56), ("raiz", "g", 60, ENT), ("vira", "i", 56), ("um", "i", 56), ("parêntese", "g", 60)], x + 44, 590)
    E.foco(c, t, C["s03.c"] + 1.6, 0.5, lambda a: E.formula(c, "(x − raiz)", x + 44, 700, 70, "g", COR, a))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.formula(c, "x^2 + 5x + 6 = (x + 2)(x + 3)", x + 44, 860, 62, "g", TINTA, a))
    q_ = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(400, 900, q_), ep(t, C["s03.b"], 0.4))


# ---------------- forma fatorada ----------------
PALPITE = "y = (x − 1)(x − 5)"
FAMILIA = "y = a(x − 1)(x − 5)"


def b_fatorada(c, t, C, b):
    plano_f(c, t, C["s04"])
    raiz(c, t, C["s04"] + 0.3, PF, 1, ENT, "1")
    raiz(c, t, C["s04"] + 0.5, PF, 5, ENT, "5")
    ponto_y(c, t, C["s04"] + 0.7, PF, 10, pulsa=C["s05.c"] if t < C["s06"] else C["s07.c"])
    # o palpite, tracejado
    if t < C["s06"]:
        E.curva(c, t, C["s04.a"] + 0.3, PF, g, -0.4, 6.4, d=1.0, cor=TINTA2, largura=6, tracejada=True)
        E.ponto(c, t, C["s05.b"] + 0.6, PF, 0, 5, cor=ERRADO, r=14)
        E.foco(c, t, C["s05.b"] + 0.9, 0.4, lambda a: caixa_par(c, "0", "5", PF.ox + 30, PF.y(5) + 20, 40, a, "left"))
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], [("raízes", "i", 66), ("1", "g", 76, ENT), ("e", "i", 66), ("5", "g", 76, ENT)], XE, 230)
            E.frase(c, t, C["s04"] + 1.0, ps("primeiro palpite", "i", 56, TINTA2), XE, 340)
            E.foco(c, t, C["s04.a"], 0.5, lambda a: E.formula(c, PALPITE, XE, 470, 84, "g", TINTA, a))
            realce(c, t, C["s04.b"], PALPITE, "(x − 1)", XE, 470, 84, ENT)
            fml(c, t, C["s04.b"] + 0.4, "x = 1:  (1 − 1) = 0", XE, 620, 60, ENT)
            realce(c, t, C["s04.c"], PALPITE, "(x − 5)", XE, 470, 84, ENT)
            fml(c, t, C["s04.c"] + 0.4, "x = 5:  (5 − 5) = 0", XE, 730, 60, ENT)
            E.foco(c, t, pal("s04", "batem", 0, C["s04.c"] + 2.4), 0.4, lambda a: E.pilula(c, "as raízes batem", XE + 250, 850, 50, "g", fundo=CERTO, a=a))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.foco(c, t, C["s05"], 0.5, lambda a: E.formula(c, PALPITE, XE, 230, 70, "g", TINTA, a))
            E.frase(c, t, C["s05.a"], [("corte", "i", 60), ("no", "i", 60), ("y:", "g", 66), ("x", "g", 70, ENT), ("=", "g", 70, ENT), ("0", "g", 70, ENT)], XE, 370)
            fml(c, t, C["s05.b"], "(0 − 1)(0 − 5) = (−1)(−5) = 5", XE, 500, 58, TINTA)
            E.frase(c, t, C["s05.c"], [("o", "i", 62), ("desenho", "i", 62), ("pede", "i", 62), ("10", "g", 80)], XE, 640)
            E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "não passa pelo ponto", XE + 300, 780, 50, "g", fundo=ERRADO, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        # a família: o a respira entre 2 e −1, presa nas raízes
        k0 = C["s06.a"]
        if t >= k0:
            for kk in (-1, -0.5, 0.5, 2):
                E.curva(c, t, k0, PF, lambda x, kk=kk: kk * g(x), -0.4, 6.4, d=0.8, cor=FIO, largura=4)
            fase = (t - k0) * 0.9
            a_ = 0.6 + 1.4 * math.sin(fase) if t < C["s06.c"] else lerp(0.6 + 1.4 * math.sin((C["s06.c"] - k0) * 0.9), 1.0, ep(t, C["s06.c"], 0.6))
            E.curva(c, t, k0 + 0.2, PF, lambda x: a_ * g(x), -0.4, 6.4, d=0.6, cor=COR, largura=7)
            E.foco(c, t, k0 + 0.6, 0.4, lambda a: E.pilula(c, f"a = {a_:.1f}".replace(".", ",").replace("-", "−"), PF.x(5.4), PF.y(12), 36, "g", fundo=COR, a=a))
        E.frase(c, t, C["s06.a"], [("infinitas", "g", 76, COR), ("parábolas", "i", 72)], XE, 260)
        E.frase(c, t, C["s06.a"] + 1.2, ps("com raízes 1 e 5", "i", 60, TINTA2), XE, 350)
        E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, FAMILIA, XE, 520, 84, "g", TINTA, a))
        realce(c, t, C["s06.b"] + 0.8, FAMILIA, "a", XE, 520, 84, COR)
        E.frase(c, t, pal("s06", "boca", 0, C["s06.b"] + 4.0), ps("vira a boca, fecha ou abre", "i", 52, TINTA2), XE, 640, passo=0.1)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "a · 0 = 0: as raízes ficam", XE + 330, 790, 46, "g", fundo=CERTO, a=a))
        return
    if t < C["s08"]:
        y0, size = 330, 84
        E.frase(c, t, C["s07.a"], [("forma", "i", 66), ("fatorada", "g", 72, COR)], XE, 200)
        E.foco(c, t, C["s07"], 0.4, lambda a: E.formula(c, FAMILIA, XE, y0, size, "g", TINTA, a))
        pos_a = trecho_x(FAMILIA, "a", XE, size)
        p = ep(t, C["s07.b"], 0.5)
        if p > 0:
            xa, wa = pos_a
            E.chave(c, xa, xa + wa, y0 + 30, COR, p, 20, 5)
            x1, w1 = trecho_x(FAMILIA, "(x − 1)(x − 5)", XE, size)
            E.chave(c, x1, x1 + w1, y0 + 30, ENT, p, 20, 5)
            E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: (centro(c, "a", xa + wa / 2, y0 + 110, 46, "g", COR, a),
                                                          centro(c, "um parêntese por raiz", x1 + w1 / 2, y0 + 110, 42, "i", ENT, a)))
        E.frase(c, t, C["s07.c"], [("quem", "i", 54), ("escolhe", "i", 54), ("o", "i", 54), ("a:", "g", 60, COR), ("o", "i", 54), ("ponto", "g", 58), ("que", "i", 54),
                                   ("sobrou", "g", 58)], XE, 540)
        E.foco(c, t, C["s07.d"], 0.4, lambda a: par(c, "0", "10", XE, 650, 70, a))
        fml(c, t, C["s07.e"], "10 = a(−1)(−5)", XE + 300, 650, 66, TINTA)
        fml(c, t, C["s07.f"], "10 = 5a  →  a = 2", XE, 790, 72, COR)
        return
    E.curva(c, t, C["s08"] + 0.2, PF, f, -0.15, 6.15, d=1.2, cor=COR)
    E.frase(c, t, C["s08"], [("forma", "i", 66), ("fatorada", "g", 72, COR)], XE, 300)
    caixa_lei(c, t, C["s08.a"], FAT, XE, 500, 86)
    E.foco(c, t, C["s08.a"] + 1.2, 0.4, lambda a: E.pilula(c, "passa por (0, 10)", XE + 280, 690, 48, "g", fundo=CERTO, a=a))


# ---------------- desenvolvida ----------------
def b_desenvolvida(c, t, C, b):
    plano_f(c, t, C["s09"] - 3)
    E.curva(c, t, C["s09"] - 3, PF, f, -0.15, 6.15, d=0.05, cor=COR)
    ponto_y(c, t, C["s09"] - 3, PF, 10, pulsa=C["s09.d"] + 0.3)
    forma(c, t, C["s09"], "fatorada", FAT, 270, 62, TINTA, etq=TINTA2)
    E.frase(c, t, C["s09.a"], [("abra", "i", 62), ("os", "i", 62), ("parênteses", "g", 66)], XE, 400)
    fml(c, t, C["s09.b"], "(x − 1)(x − 5) = x^2 − 6x + 5", XE, 530, 60, TINTA2)
    fml(c, t, C["s09.c"], "2(x^2 − 6x + 5)", XE, 650, 60, TINTA2)
    forma(c, t, C["s09.c"] + 1.4, "com a, b e c", DES, 830, 72, TINTA)
    realce(c, t, C["s09.d"], DES, "10", XE, 830, 72, CERTO)
    E.foco(c, t, C["s09.d"] + 0.4, 0.4, lambda a: E.pilula(c, "c = 10: bateu", XE + 250, 930, 44, "g", fundo=CERTO, a=a))


# ---------------- forma do vértice ----------------
def b_vertice(c, t, C, b):
    plano_f(c, t, C["s10"])
    E.curva(c, t, C["s10"] + 0.2, PF, f, -0.15, 6.15, d=0.8, cor=COR)
    raiz(c, t, C["s10"] + 0.4, PF, 1, ENT)
    raiz(c, t, C["s10"] + 0.4, PF, 5, ENT)
    vertice(c, t, C["s10.a"] + 0.3, PF, 3, -8, ("3", "−8") if t >= C["s12.d"] else None)
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("uma terceira forma", "i", 60, TINTA2), XE, 230)
        E.frase(c, t, C["s10.a"], [("o", "i", 70), ("vértice:", "g", 76, VERT)], XE, 360)
        E.frase(c, t, C["s10.a"] + 1.0, ps("onde a parábola faz a curva", "i", 54), XE, 450, passo=0.1)
        forma(c, t, C["s10.b"], "do vértice", VER, 680, 92, TINTA)
        return
    if t < C["s12"]:
        forma(c, t, C["s11"] - 0.2, "do vértice", VER, 250, 70, TINTA)
        E.frase(c, t, C["s11"], ps("confira abrindo", "i", 54, TINTA2), XE, 360)
        fml(c, t, C["s11.a"], "(x − 3)^2 = x^2 − 6x + 9", XE, 480, 60, TINTA2)
        fml(c, t, C["s11.b"], "2(x^2 − 6x + 9) = 2x^2 − 12x + 18", XE, 590, 52, TINTA2)
        fml(c, t, C["s11.c"], "2x^2 − 12x + 18 − 8", XE, 730, 60, TINTA)
        fml(c, t, C["s11.c"] + 1.0, "= 2x^2 − 12x + 10", XE + 80, 830, 66, COR)
        E.foco(c, t, pal("s11", "mesma", 0, C["s11.c"] + 2.4), 0.4, lambda a: E.pilula(c, "a mesma lei", XE + 650, 805, 44, "g", fundo=CERTO, a=a))
        return
    if t < C["s13"]:
        size = 92
        forma(c, t, C["s12"] - 0.2, "do vértice", VER, 260, size, TINTA)
        realce(c, t, C["s12.a"], VER, "(x − 3)^2", XE, 260, size, VERT)
        E.frase(c, t, C["s12.a"], [("nunca", "i", 60), ("é", "i", 60), ("negativo:", "i", 60), ("≥", "g", 70, VERT), ("0", "g", 70, VERT)], XE, 420)
        E.frase(c, t, C["s12.b"], [("menor", "i", 58), ("valor:", "i", 58), ("0,", "g", 64), ("com", "i", 58), ("x", "g", 64, ENT), ("=", "g", 64, ENT), ("3", "g", 64, ENT)], XE, 530)
        fml(c, t, C["s12.c"], "y = 2 · 0 − 8 = −8", XE, 640, 64, SAI)
        regua(c, t, C["s12.b"] + 0.4, PF, 3)
        M.line(c, PF.x(-1.5), PF.y(-8), PF.x(7), PF.y(-8), SAI, 0.7 * ep(t, C["s12.c"], 0.5), 4, dash=E.TRACO, progress=ep(t, C["s12.c"], 0.8))
        tq = pal("s12", "qualquer", 0, C["s12.c"] + 2.0)
        E.frase(c, t, tq, [("outro", "i", 54), ("x:", "g", 60, ENT), ("y", "g", 60), ("acima", "g", 58), ("de", "i", 54), ("−8", "g", 60)], XE, 750)
        # um ponto que passeia pela curva, sempre acima de −8
        a_ = ep(t, tq, 0.4) * (1 - ep(t, C["s12.d"] - 0.3, 0.4))
        if a_ > 0:
            xv = 3 + 2.6 * math.sin((t - tq) * 1.1)
            X, Y = PF(xv, f(xv))
            M.line(c, X, Y, X, PF.y(-8), SOBE, a_, 5, dash=[10, 8])
            c.drawCircle(X, Y, 15, M.paint(SAI, a_))
        E.foco(c, t, C["s12.d"], 0.4, lambda a: (E.escreve(c, "o mais baixo:", XE, 860, 54, "i", TINTA, a),
                                                par(c, "3", "−8", XE + 360, 860, 70, a)))
        p = ep(t, C["s12.e"], 0.6)
        if p > 0:
            E.chave(c, PF.x(1), PF.x(5), PF.oy - 50, ENT, p, -22, 5)
            E.foco(c, t, C["s12.e"] + 0.3, 0.4, lambda a: E.pilula(c, "meio: 3", PF.x(3), PF.oy - 120, 40, "g", fundo=ENT, a=a))
        return
    GER = "y = a(x − h)^2 + k"
    forma(c, t, C["s13"], "do vértice", VER, 250, 70, TINTA)
    E.frase(c, t, C["s13.a"], [("forma", "i", 62), ("do", "i", 62), ("vértice", "g", 68, VERT)], XE, 380)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: lei(c, [("y = a(x − ", TINTA), ("h", ENT), (")^2 + ", TINTA), ("k", SAI)], XE, 530, 92, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (E.escreve(c, "vértice:", XE, 680, 60, "i", TINTA, a), par(c, "h", "k", XE + 250, 680, 80, a)))
    te_ = pal("s13", "exemplo", 0, C["s13.c"] + 2.0)
    E.frase(c, t, te_, [("h", "g", 66, ENT), ("=", "g", 66, ENT), ("3", "g", 66, ENT)], XE, 800)
    E.frase(c, t, te_ + 0.6, [("k", "g", 66), ("=", "g", 66), ("−8", "g", 66)], XE + 300, 800)
    E.foco(c, t, pal("s13", "negativo", 0, C["s13.c"] + 5.0), 0.4, lambda a: E.pilula(c, "a < 0: o ponto mais alto", XE + 300, 900, 44, "g", fundo=SAI, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano_f(c, t, C["s14"] - 3)
    E.curva(c, t, C["s14"] - 3, PF, f, -0.15, 6.15, d=0.05, cor=COR)
    vertice(c, t, C["s14"] - 3, PF, 3, -8, ("3", "−8"))
    size = 84
    E.foco(c, t, C["s14"] - 0.2, 0.5, lambda a: E.formula(c, VER, XE, 240, size, "g", TINTA, a))
    realce(c, t, C["s14.a"], VER, "− 3", XE, 240, size, ERRADO, t1=C["s14.e"])
    E.frase(c, t, C["s14.a"], [("o", "i", 62), ("erro:", "i", 62), ("copiar", "g", 66, ERRADO), ("o", "i", 62), ("sinal", "g", 66, ERRADO)], XE, 380)

    def errado():
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.formula(c, "x = −3 ?", XE, 500, 72, "g", ERRADO, a))
        fml(c, t, C["s14.c"], "(−3 − 3)^2 = (−6)^2 = 36", XE, 610, 56, TINTA2)
        fml(c, t, C["s14.d"], "2 · 36 − 8 = 64", XE, 710, 66, ERRADO)
        q_ = ep(t, C["s14.d"] + 0.6, 0.5)
        if q_ > 0:
            M.arrow(c, PF.x(-1.2), PF.y(2), PF.x(-1.2), PF.caixa[1] - 30, ERRADO, q_, 8, 26, q_)
            E.pilula(c, "y = 64: lá em cima", PF.x(3.6), PF.caixa[1] + 10, 38, "g", fundo=ERRADO, a=q_)
    E.saida(c, t, C["s14.e"], errado)
    regua(c, t, C["s14.e"] + 0.3, PF, 3, CERTO)
    fml(c, t, C["s14.e"], "x − 3 = 0  →  x = 3", XE, 560, 72, CERTO)
    E.frase(c, t, C["s14.e"] + 1.0, [("o", "i", 56), ("número", "i", 56), ("que", "i", 56), ("zera", "g", 60, CERTO), ("o", "i", 56), ("parêntese", "i", 56)], XE, 680)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    QF = E.Plano(*PL, -1.5, 7, -10.5, 13.5, escuro=True)
    eixos(c, t, QF, C["s15"], tg=C["s15"], marcas=MF, escuro=True)
    raiz(c, t, C["s15.b"], QF, 1, rot="1")
    raiz(c, t, C["s15.b"] + 0.3, QF, 5, rot="5")
    E.ponto(c, t, C["s15"] + 0.4, QF, 0, 10, cor=BR, r=15)
    E.curva(c, t, C["s15.c"] + 0.6, QF, f, -0.15, 6.15, d=1.0, cor=CLARO, largura=8)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 62, CLARO), XE, 200)
        E.foco(c, t, C["s15.a"], 0.6, lambda a: (E.escreve(c, "a =", XE, 400, 96, "g", BR, a),
                                                 E.formula(c, "f{c}{produto das raízes}", XE + 190, 400, 70, "g", AMARELO, a)))
        fml(c, t, C["s15.b"], "1 · 5 = 5", XE, 600, 76, BR)
        fml(c, t, C["s15.c"], "a = 10 ÷ 5 = 2", XE, 750, 86, AMARELO)
        return
    E.frase(c, t, C["s16"], ps("por que funciona", "i", 56, CLARO), XE, 200)
    fml(c, t, C["s16.a"], "x = 0:  (0 − 1)(0 − 5) = (−1)(−5)", XE, 320, 52, BR)
    E.frase(c, t, C["s16.a"] + 1.6, ps("as raízes com o sinal trocado", "i", 48, CLARO), XE, 400, passo=0.08)
    E.frase(c, t, pal("s16", "trocar", 0, C["s16.a"] + 4.0), [("−", "g", 60, AMARELO), ("×", "g", 60, BR), ("−", "g", 60, AMARELO), ("=", "g", 60, BR), ("+", "g", 60, AMARELO)], XE, 490)
    fml(c, t, C["s16.b"], "c = a · 1 · 5", XE, 610, 70, BR)
    E.frase(c, t, C["s16.c"], [("não", "g", 60, ERRADO), ("vale:", "i", 56, CLARO), ("ponto", "i", 56, CLARO), ("fora", "g", 60, BR), ("do", "i", 56, CLARO), ("eixo", "i", 56, CLARO),
                               ("y", "g", 60, BR)], XE, 740)
    E.ponto(c, t, C["s16.c"] + 0.5, QF, 6, 10, cor=ERRADO, r=15)
    E.foco(c, t, C["s16.c"] + 0.8, 0.4, lambda a: caixa_par_esc(c, "6", "10", QF.x(6) - 20, QF.y(10) - 34, 40, a))
    fml(c, t, C["s16.d"], "10 = a(6 − 1)(6 − 5)", XE, 870, 60, AMARELO)


def caixa_par_esc(c, xv, yv, X, Y, size, a):
    w = par(None, xv, yv, 0, 0, size, 0)
    M.rrect(c, X - w - 10, Y - size * 0.95, w + 20, size * 1.3, 12, ESCURO, 0.9 * a)
    par(c, xv, yv, X - w, Y, size, a, cores=(CLARO, BR))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 70, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("raízes", "i", 64), ("−2", "g", 76, ENT), ("e", "i", 64), ("4", "g", 76, ENT)], XE, 330)
    E.frase(c, t, C["s17.b"], [("passa", "i", 64), ("por", "i", 64)], XE, 450)
    E.foco(c, t, C["s17.b"] + 0.4, 0.4, lambda a: par(c, "0", "−16", XE + 290, 450, 76, a))
    E.frase(c, t, C["s17.c"], [("1)", "g", 58, COR), ("a", "i", 56), ("lei", "g", 60), ("fatorada", "i", 56), ("e", "i", 56), ("com", "i", 56), ("a,", "g", 60, CA), ("b", "g", 60, CB),
                               ("e", "i", 56), ("c", "g", 60)], XE, 600)
    E.frase(c, t, C["s17.d"], [("2)", "g", 58, COR), ("o", "i", 56), ("vértice", "g", 60, VERT), ("de", "i", 56)], XE, 730)
    E.foco(c, t, C["s17.d"] + 1.0, 0.5, lambda a: E.formula(c, "y = 2(x − 1)^2 − 18", XE + 60, 850, 72, "g", TINTA, a))

    def graf():
        plano_q(c, t, C["s17.a"])
        raiz(c, t, C["s17.a"] + 0.4, PQ, -2, ENT, "−2")
        raiz(c, t, C["s17.a"] + 0.7, PQ, 4, ENT, "4")
        ponto_y(c, t, C["s17.b"] + 0.4, PQ, -16)
    E.saida(c, t, C["s18"] - 0.1, graf)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1440, cy=460, r=180)


FAT_Q = "y = a(x + 2)(x − 4)"


def b_resposta(c, t, C, b):
    plano_q(c, t, C["s19"])
    raiz(c, t, C["s19"] + 0.2, PQ, -2, ENT, "−2")
    raiz(c, t, C["s19"] + 0.4, PQ, 4, ENT, "4")
    ponto_y(c, t, C["s19"] + 0.6, PQ, -16)
    E.curva(c, t, C["s19.d"] + 0.4, PQ, q, -2.6, 4.6, d=1.0, cor=COR)
    if t < C["s20"]:
        E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, FAT_Q, XE, 250, 76, "g", TINTA, a))
        fml(c, t, C["s19.b"], "produto: −2 · 4 = −8", XE, 400, 62, TINTA2)
        fml(c, t, C["s19.c"], "a = −16 ÷ (−8) = 2", XE, 530, 70, COR)
        caixa_lei(c, t, C["s19.d"], "y = 2(x + 2)(x − 4)", XE, 720, 72)
        return
    forma(c, t, C["s20"] - 0.2, "fatorada", "y = 2(x + 2)(x − 4)", 230, 58, TINTA, etq=TINTA2)
    fml(c, t, C["s20.a"], "(x + 2)(x − 4) = x^2 − 2x − 8", XE, 340, 56, TINTA2)
    forma(c, t, C["s20.b"], "com a, b e c", "y = 2x^2 − 4x − 16", 510, 66, TINTA)
    VQ = "y = 2(x − 1)^2 − 18"
    forma(c, t, C["s20.c"] - 0.4, "do vértice", VQ, 680, 66, TINTA)
    realce(c, t, C["s20.c"], VQ, "(x − 1)", XE, 680, 66, VERT)
    regua(c, t, C["s20.c"] + 0.4, PQ, 1)
    vertice(c, t, C["s20.d"], PQ, 1, -18, ("1", "−18"))
    E.foco(c, t, C["s20.d"], 0.4, lambda a: (E.escreve(c, "vértice:", XE, 830, 56, "i", TINTA, a), par(c, "1", "−18", XE + 230, 830, 66, a)))
    p = ep(t, C["s20.e"], 0.6)
    if p > 0:
        E.chave(c, PQ.x(-2), PQ.x(4), PQ.oy - 60, ENT, p, -22, 5)
        E.foco(c, t, C["s20.e"] + 0.3, 0.4, lambda a: E.pilula(c, "meio: 1", PQ.x(1), PQ.oy - 130, 40, "g", fundo=ENT, a=a))
    E.foco(c, t, C["s20.e"] + 1.2, 0.4, lambda a: E.pilula(c, "bateu", XE + 640, 810, 46, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", [("cada", "i", 72), ("raiz", "g", 76, ENT), ("vira", "i", 72), ("um", "i", 72), ("parêntese", "g", 76)]),
                 ("s21.b", [("o", "i", 72), ("ponto", "g", 76), ("que", "i", 72), ("sobra", "i", 72), ("decide", "i", 72), ("o", "i", 72), ("a", "g", 80, COR)]),
                 ("s21.c", [("a", "i", 72), ("forma", "i", 72), ("do", "i", 72), ("vértice", "g", 76, VERT), ("mostra", "i", 72), ("o", "i", 72), ("vértice", "g", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s22"] + 1.0, [("estudo", "g", 110, COR), ("do", "i", 100), ("sinal", "g", 110, COR)], XE, 430)
    E.foco(c, t, C["s22.a"], 0.5, lambda a: E.formula(c, "x^2 − 5x + 6 < 0 ?", XE, 590, 80, "g", TINTA, a))
    E.frase(c, t, C["s22.b"], [("onde", "i", 62), ("a", "i", 62), ("curva", "i", 62), ("passa", "i", 62), ("abaixo", "g", 66, ERRADO), ("do", "i", 62), ("eixo", "i", 62), ("x", "g", 70, ENT)],
            XE, 720)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fatorada=b_fatorada, desenvolvida=b_desenvolvida, vertice=b_vertice, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
