"""Visual — Estudativo · MAT-FUN-019: máximo e mínimo em problemas.

Linguagem visual da trilha Funções (MAT-FUN-001): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Como na MAT-FUN-016 a 018: na lei, o a em índigo, o b em cinza e o c em preto; parábola de a > 0 índigo, de a < 0 preta;
o vértice é a esfera amarela (VERT) com anel; régua tracejada em pé no x do vértice. Como na MAT-FUN-007: trecho que sobe repintado
de verde e o que desce de vermelho; o valor lido ganha pílula no eixo (índigo no x, preta no y).
Nesta aula: "quando? / quanto usar?" = guia índigo do vértice até o eixo x; "o valor máximo / mínimo" = guia preta até o eixo y.
Os eixos têm o nome da grandeza (t em segundos, h em metros; caixas e lucro em reais; horas e graus).
Peças locais: eixos(), par(), anel(), lei(), sob_parte(), fsub(), vertice(), regua(), guia(), marca_eixo(), trecho(), bola_voo(), pal()."""
import json
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
ARQUIVO_FINAL = "estudativo_MAT-FUN-019_maximo_e_minimo_em_problemas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "bola", "lucro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERT = "#F2B705"
ESCURO = "#0B0B16"

h = lambda x: -5 * x * x + 20 * x
L = lambda x: -x * x + 40 * x - 300
T = lambda x: x * x - 6 * x + 5
assert -20 / (2 * -5) == 2 and h(2) == 20 and -5 * 4 == -20 and 20 * 2 == 40 and h(0) == 0 and h(4) == 0 and -20 / -5 == 4
assert -40 / -2 == 20 and L(20) == 100 and -400 + 800 - 300 == 100 and L(10) == 0 and L(30) == 0
assert 6 / 2 == 3 and T(3) == -4 and 9 - 18 + 5 == -4 and T(1) == 0 and T(5) == 0

PL = (1080, 200, 700, 680)
PB = E.Plano(*PL, -0.7, 4.8, -3.5, 24)
MB = ([1, 2, 3, 4], [5, 10, 15, 20])
PLU = E.Plano(*PL, -4, 44, -25, 125)
MLU = ([10, 20, 30, 40], [50, 100])
PQ = E.Plano(*PL, -0.8, 6.8, -5.5, 6.5)
MQ = ([1, 2, 3, 4, 5, 6], [-4, -2, 2, 4])
PI = E.Plano(*PL, -0.5, 4.5, -2.5, 4.5)
LEI_H = [("h(t) = ", TINTA), ("−5t^2", CA), (" + 20t", CB)]
LEI_L = [("L(x) = ", TINTA), ("−x^2", CA), (" + 40x", CB), (" − 300", CC)]
LEI_T = [("T(t) = ", TINTA), ("t^2", CA), (" − 6t", CB), (" + 5", CC)]
g_max = lambda x: -(x - 2) ** 2 + 3.2
g_min = lambda x: (x - 2) ** 2 - 1.5

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


def bola_voo(c, t, t0, P_, fn, a_, b_, d, cor=TINTA, r=20, escuro=False, some=False):
    """a bola andando sobre a curva enquanto ela se desenha (mesmo passo de E.curva); some = apaga depois de pousar"""
    if t < t0:
        return
    p = ease_io(prog(t, t0, d))
    a = 1 - ep(t, t0 + d + 0.4, 0.5) if some else 1.0
    if a <= 0:
        return
    xv = a_ + (b_ - a_) * p
    X, Y = P_(xv, fn(xv))
    E.bola(c, X, Y - r, r, cor, a) if not escuro else c.drawCircle(X, Y - r, r, M.paint(cor, a))


def plano_bola(c, t, t0, grade=True):
    eixos(c, t, PB, t0, tg=t0 if grade else None, marcas=MB, nx="t (s)", ny="h (m)")


def plano_lucro(c, t, t0):
    eixos(c, t, PLU, t0, tg=t0, marcas=MLU, nx="caixas", ny="lucro (R$)")


def plano_camara(c, t, t0):
    eixos(c, t, PQ, t0, tg=t0, marcas=MQ, nx="t (h)", ny="T (°C)")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano_bola(c, t, C["s01"])
        E.curva(c, t, C["s01"] + 0.6, PB, h, 0, 4, d=2.4, cor=TINTA)
        bola_voo(c, t, C["s01"] + 0.6, PB, h, 0, 4, 2.4, TINTA2)
        E.frase(c, t, C["s01"], ps("uma bola chutada para cima", "i", 60, TINTA2), XE, 230, passo=0.12)
        lei_em(c, t, C["s01.a"], LEI_H, XE, 380, 96)
        E.frase(c, t, C["s01.b"], [("altura", "g", 96), ("máxima?", "g", 96, COR)], XE, 560)
        vertice(c, t, C["s01.b"] + 0.4, PB, 2, 20)
        # a resposta errada: o 2 é o quando
        E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "2?", XE, 760, 150, "g", ERRADO, a))
        if t >= C["s01.c"] + 0.7:
            E.risco(c, XE - 10, 770, XE + 210, 650, t, C["s01.c"] + 0.7, largura=10)
        guia(c, t, C["s01.c"], PB, 2, 20, "x", ERRADO)
        marca_eixo(c, t, C["s01.c"] + 0.5, PB, "2", 2, "x", ERRADO)
        tq = pal("s01", "quando", 0, C["s01.c"] + 1.4)
        E.frase(c, t, tq, [("é", "i", 60), ("o", "i", 60), ("quando", "g", 64, ENT)], XE + 280, 700)
        ta = pal("s01", "altura", 2, C["s01.c"] + 3.0)
        E.frase(c, t, ta, [("não", "i", 60), ("a", "i", 60), ("altura", "g", 64)], XE + 280, 790)
        guia(c, t, ta, PB, 2, 20, "y", SAI)
        marca_eixo(c, t, ta + 0.5, PB, "?", 20, "y", SAI)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 280)
        E.frase(c, t, C["s02.a"] + 1.0, [("o", "i", 90), ("maior", "g", 110, COR), ("e", "i", 90), ("o", "i", 90), ("menor", "g", 110, COR)], XE, 430)
        E.frase(c, t, C["s02.a"] + 2.0, ps("valor num problema", "i", 80), XE, 550)
        E.frase(c, t, C["s02.b"], [("responda", "i", 76), ("o", "i", 76), ("que", "i", 76), ("foi", "i", 76), ("pedido", "g", 80)], XE, 720)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 76), ("precisa", "i", 76), ("de", "i", 76)], XE, 300)
    E.frase(c, t, C["s03.a"], [("1", "g", 200, COR), ("coisa", "i", 96)], XE, 520)
    E.frase(c, t, C["s03.a"] + 0.6, [("o", "i", 96), ("vértice", "g", 110, VERT)], XE, 680)
    x, w = 900, 880
    itens = (("s03.b", "x do vértice:", ENT, lambda a, y: (fsub(c, "x_v = f{−b}{2a}", x + 44, y + 10, 76, "g", ENT, a),
                                                          E.escreve(c, "ou a média das raízes", x + 370, y - 6, 48, "i", TINTA2, a))),
             ("s03.c", "y do vértice:", SAI, lambda a, y: (E.escreve(c, "troque esse x na função", x + 44, y - 6, 58, "i", TINTA, a))))
    for i, (k, l1, cor, fn) in enumerate(itens):
        y = 200 + i * 340
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 270, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 60, cor)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, fn=fn, y=y: fn(a, y + 200))
    q_ = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(440, 780, q_), ep(t, C["s03.b"], 0.4))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    eixos(c, t, PI, C["s04"], tg=None, marcas=([], []))

    def maximo():
        E.curva(c, t, C["s04.a"], PI, g_max, 0.1, 3.9, d=1.0, cor=TINTA)
        ts = pal("s04", "sobe", 0, C["s04.a"] + 2.0)
        td = pal("s04", "desce", 0, ts + 1.4)
        trecho(c, t, ts, PI, g_max, 0.1, 2, SOBE, d=0.7)
        trecho(c, t, td, PI, g_max, 2, 3.9, DESCE, d=0.7)
        vertice(c, t, C["s04.b"], PI, 2, 3.2)
        guia(c, t, C["s04.c"], PI, 2, 3.2, "y", SAI)
        E.foco(c, t, C["s04.c"] + 0.4, 0.4, lambda a: E.pilula(c, "máximo", PI.x(2) + 150, PI.y(3.2) - 50, 40, "g", fundo=SAI, a=a))
        E.frase(c, t, C["s04"], [("por", "i", 76), ("que", "i", 76), ("o", "i", 76), ("vértice?", "g", 80, VERT)], XE, 230)
        E.frase(c, t, C["s04.a"], [("a", "g", 96, CA), ("<", "g", 96, CA), ("0:", "g", 96, CA), ("abre", "i", 72), ("para", "i", 72), ("baixo", "g", 76)], XE, 400)
        E.frase(c, t, ts, [("sobe,", "g", 66, SOBE)], XE, 520)
        E.frase(c, t, ts + 0.6, [("faz", "i", 66), ("a", "i", 66), ("curva", "i", 66)], XE + 210, 520)
        E.frase(c, t, td, [("e", "i", 66), ("desce", "g", 66, DESCE)], XE + 530, 520)
        E.frase(c, t, C["s04.b"], [("o", "i", 72), ("ponto", "i", 72), ("mais", "i", 72), ("alto", "g", 80)], XE, 680)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "o máximo da função", XE + 300, 820, 58, "g", fundo=SAI, a=a))
    E.saida(c, t, C["s05"] - 0.1, maximo)
    if t < C["s05"]:
        return
    E.curva(c, t, C["s05.a"], PI, g_min, 0.15, 3.85, d=1.0, cor=COR)
    vertice(c, t, C["s05.b"], PI, 2, -1.5)
    guia(c, t, C["s05.c"], PI, 2, -1.5, "y", SAI)
    E.foco(c, t, C["s05.c"] + 0.4, 0.4, lambda a: E.pilula(c, "mínimo", PI.x(2) + 150, PI.y(-1.5) + 50, 40, "g", fundo=COR, a=a))
    E.frase(c, t, C["s05.a"], [("a", "g", 96, CA), (">", "g", 96, CA), ("0:", "g", 96, CA), ("abre", "i", 72), ("para", "i", 72), ("cima", "g", 76)], XE, 260)
    E.frase(c, t, C["s05.a"] + 1.6, ps("como um sorriso", "i", 60, TINTA2), XE, 360)
    E.frase(c, t, C["s05.b"], [("o", "i", 72), ("ponto", "i", 72), ("mais", "i", 72), ("baixo:", "g", 80)], XE, 480)
    E.frase(c, t, C["s05.c"], [("o", "i", 80), ("mínimo", "g", 90, COR)], XE, 590)
    E.foco(c, t, C["s05.d"], 0.6, lambda a: (M.rrect(c, XE - 20, 670, 720, 310, 46, COR, a),
                                             E.escreve(c, "antes da conta:", XE + 30, 750, 52, "i", BR, a),
                                             E.escreve(c, "a < 0  máximo", XE + 30, 850, 66, "g", BR, a),
                                             E.escreve(c, "a > 0  mínimo", XE + 30, 940, 66, "g", BR, a)))


# ---------------- a bola ----------------
def b_bola(c, t, C, b):
    plano_bola(c, t, C["s06"])
    E.curva(c, t, C["s06.c"], PB, h, 0, 4, d=1.2, cor=TINTA)
    # rótulo da lei fica no alto durante o bloco
    pos = lei_em(c, t, C["s06"], LEI_H, XE, 200, 80)
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], [("t", "g", 72, ENT), ("=", "g", 72, ENT), ("tempo", "i", 64), ("(segundos)", "i", 52, TINTA2)], XE, 420)
            E.frase(c, t, pal("s06", "agá", 0, C["s06.a"] + 2.0), [("h", "g", 72, SAI), ("=", "g", 72, SAI), ("altura", "i", 64), ("(metros)", "i", 52, TINTA2)], XE, 520)
            sob_parte(c, t, C["s06.b"], pos, 1, 200, "a = −5", CA, 44)
            sob_parte(c, t, pal("s06", "bê", 0, C["s06.b"] + 1.4), pos, 2, 200, "b = 20", CB, 44, apara=larg_f(" + ", 80))
            E.foco(c, t, pal("s06", "cê", 0, C["s06.b"] + 2.6), 0.4, lambda a: E.formula(c, "c = 0", XE + 640, 300, 44, "g", CC, a))
            E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "a < 0: tem ponto mais alto", XE + 330, 680, 46, "g", fundo=SAI, a=a))
        E.saida(c, t, C["s07"] - 0.1, s06)
    regua(c, t, C["s07.d"] + 0.3, PB, 2)
    marca_eixo(c, t, C["s07.d"] + 0.6, PB, "2", 2, "x", ENT)

    def s07():
        fml(c, t, C["s07.a"], "t_v = f{−b}{2a}", XE, 400, 84, ENT)
        fml(c, t, C["s07.b"], "−b = −20", XE, 560, 68, CB)
        fml(c, t, C["s07.c"], "2a = 2 · (−5) = −10", XE, 670, 68, CA)
        fml(c, t, C["s07.d"], "t_v = f{−20}{−10} = 2", XE, 850, 84, ENT)
        E.foco(c, t, C["s07.d"] + 0.8, 0.4, lambda a: E.pilula(c, "2 segundos", XE + 620, 820, 46, "g", fundo=ENT, a=a))
    if C["s07"] <= t < C["s08"]:
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    # a partir daqui o t do vértice fica no alto
    E.foco(c, t, C["s08"] - 0.1, 0.4, lambda a: fsub(c, "t_v = 2", 830, 200, 64, "g", ENT, a))

    def s08():
        fml(c, t, C["s08.a"], "h(2) = −5 · 2^2 + 20 · 2", XE, 380, 72, TINTA)
        fml(c, t, C["s08.b"], "−5 · 4 = −20", XE + 40, 510, 64, TINTA2)
        fml(c, t, C["s08.c"], "20 · 2 = 40", XE + 40, 610, 64, TINTA2)
        fml(c, t, C["s08.d"], "h(2) = −20 + 40 = 20", XE, 770, 76, SAI)
        E.foco(c, t, C["s08.d"] + 0.8, 0.4, lambda a: E.pilula(c, "20 metros", XE + 300, 880, 46, "g", fundo=SAI, a=a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    vertice(c, t, C["s08.d"] + 0.3, PB, 2, 20, ("2", "20"), abaixo=False)
    guia(c, t, C["s08.d"] + 0.3, PB, 2, 20, "y", SAI, a=1 - ep(t, C["s09"], 0.4))
    if t < C["s09"]:
        return
    # o segredo: x = quando (ou quanto usar), y = o valor
    guia(c, t, C["s09.a"], PB, 2, 20, "x", ENT, d=0.8, largura=8)
    guia(c, t, C["s09.b"], PB, 2, 20, "y", SAI, d=0.8, largura=8)
    marca_eixo(c, t, C["s09.b"] + 0.6, PB, "20", 20, "y", SAI)
    E.frase(c, t, C["s09"], ps("o segredo dos problemas", "i", 64, TINTA2), XE, 330, passo=0.12)
    E.frase(c, t, C["s09.a"], [("x", "g", 80, ENT), ("do", "i", 64), ("vértice:", "i", 64), ("quando?", "g", 70, ENT)], XE, 460)
    E.frase(c, t, pal("s09", "quanto", 0, C["s09.a"] + 2.0), [("ou", "i", 56, TINTA2), ("quanto", "g", 60, ENT), ("usar?", "g", 60, ENT)], XE + 120, 550)
    E.frase(c, t, C["s09.b"], [("y", "g", 80, SAI), ("do", "i", 64), ("vértice:", "i", 64), ("o", "i", 64), ("valor", "g", 70)], XE, 680)
    E.frase(c, t, C["s09.b"] + 1.6, ps("máximo ou mínimo", "i", 56, TINTA2), XE + 120, 770)
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "altura máxima: 20 m", XE + 280, 880, 50, "g", fundo=SAI, a=a))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "aos 2 s", XE + 700, 880, 50, "g", fundo=ENT, a=a))


# ---------------- o lucro ----------------
def b_lucro(c, t, C, b):
    plano_lucro(c, t, C["s10"])
    E.curva(c, t, C["s10.a"] + 0.4, PLU, L, 10, 30, d=1.2, cor=TINTA)
    pos = lei_em(c, t, C["s10.a"], LEI_L, XE, 220, 74)
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], ps("segundo problema", "i", 60, TINTA2), XE, 360)
            E.frase(c, t, C["s10"] + 1.2, [("x", "g", 72, ENT), ("=", "g", 72, ENT), ("caixas", "i", 64), ("por", "i", 64), ("dia", "i", 64)], XE, 460)
            E.frase(c, t, C["s10.b"], [("1)", "g", 64, COR), ("quantas", "i", 64), ("caixas", "g", 64, ENT), ("dão", "i", 64)], XE, 640)
            E.frase(c, t, C["s10.b"] + 1.0, ps("o maior lucro?", "i", 64), XE + 60, 730)
            E.frase(c, t, C["s10.c"], [("2)", "g", 64, COR), ("qual", "i", 64), ("é", "i", 64), ("esse", "i", 64), ("lucro?", "g", 64)], XE, 870)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    tdiv = pal("s11", "dividido", 0, C["s11.b"] + 4.0)
    regua(c, t, tdiv + 0.8, PLU, 20)
    marca_eixo(c, t, tdiv + 1.0, PLU, "20", 20, "x", ENT)
    vertice(c, t, C["s11.d"] + 0.3, PLU, 20, 100, ("20", "100"), abaixo=False)
    if t < C["s12"]:
        def s11():
            sob_parte(c, t, C["s11.a"], pos, 1, 220, "a = −1", CA, 40)
            E.foco(c, t, C["s11.a"] + 0.8, 0.4, lambda a: E.pilula(c, "tem máximo", XE + 520, 300, 40, "g", fundo=SAI, a=a))
            fml(c, t, C["s11.b"], "−b = −40", XE, 430, 60, CB)
            fml(c, t, pal("s11", "dois", 0, C["s11.b"] + 2.4), "2a = −2", XE + 420, 430, 60, CA)
            fml(c, t, tdiv, "x_v = f{−40}{−2} = 20", XE, 560, 72, ENT)
            fml(c, t, C["s11.c"], "L(20) = −20^2 + 40 · 20 − 300", XE, 720, 60, TINTA)
            fml(c, t, pal("s11", "mais", 0, C["s11.c"] + 4.0), "= −400 + 800 − 300", XE + 170, 820, 60, TINTA)
            fml(c, t, C["s11.d"], "= 100", XE + 170, 930, 72, SAI)
            E.foco(c, t, C["s11.d"] + 0.4, 0.4, lambda a: E.pilula(c, "R$ 100", XE + 520, 905, 46, "g", fundo=SAI, a=a))
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    # as respostas
    E.frase(c, t, C["s12"], ps("respostas", "i", 64, TINTA2), XE, 360)
    E.frase(c, t, C["s12.a"], [("20", "g", 90, ENT), ("caixas", "g", 70, ENT), ("por", "i", 60), ("dia", "i", 60)], XE, 480)
    E.frase(c, t, C["s12.b"], [("lucro", "i", 64), ("máximo:", "i", 64), ("R$", "g", 90, SAI), ("100", "g", 90, SAI)], XE, 600)
    E.frase(c, t, C["s12.c"], [("quantas", "i", 56), ("caixas?", "g", 56)], XE, 770)
    E.foco(c, t, C["s12.c"] + 0.8, 0.4, lambda a: E.pilula(c, "o x", XE + 560, 752, 46, "g", fundo=ENT, a=a))
    E.frase(c, t, C["s12.d"], [("qual", "i", 56), ("é", "i", 56), ("o", "i", 56), ("lucro?", "g", 56)], XE, 880)
    E.foco(c, t, C["s12.d"] + 0.8, 0.4, lambda a: E.pilula(c, "o y", XE + 560, 862, 46, "g", fundo=SAI, a=a))
    guia(c, t, C["s12.c"], PLU, 20, 100, "x", ENT, largura=8)
    guia(c, t, C["s12.d"], PLU, 20, 100, "y", SAI, largura=8)
    marca_eixo(c, t, C["s12.d"] + 0.5, PLU, "100", 100, "y", SAI)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano_lucro(c, t, C["s13"] - 3)
    E.curva(c, t, C["s13"] - 3, PLU, L, 10, 30, d=0.05, cor=TINTA)
    vertice(c, t, C["s13"] - 3, PLU, 20, 100, ("20", "100"), abaixo=False)
    lei_em(c, t, C["s13"] - 3, LEI_L, XE, 200, 64)
    E.frase(c, t, C["s13.a"], [("o", "i", 70), ("erro:", "i", 70), ("parar", "g", 76, ERRADO), ("no", "i", 70), ("x", "g", 80, ERRADO)], XE, 340)

    def errado():
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.escreve(c, "lucro máximo = R$ 20", XE, 470, 66, "g", ERRADO, a))
        if t >= C["s13.b"] + 1.6:
            E.risco(c, XE - 10, 480, XE + 700, 420, t, C["s13.b"] + 1.6, largura=10)
        q = ep(t, C["s13.b"] + 0.4, 0.5)
        if q > 0:
            M.line(c, PLU.ox, PLU.y(20), PLU.x(40), PLU.y(20), ERRADO, 0.9 * q, 6, dash=E.TRACO, progress=q)
            marca_eixo(c, t, C["s13.b"] + 0.6, PLU, "20?", 20, "y", ERRADO)
    E.saida(c, t, C["s13.d"], errado)
    guia(c, t, C["s13.c"], PLU, 20, 100, "x", ENT, largura=8)
    marca_eixo(c, t, C["s13.c"] + 0.5, PLU, "20", 20, "x", ENT)
    E.frase(c, t, C["s13.c"], [("20", "g", 76, ENT), ("=", "g", 76, ENT), ("quantidade", "i", 64), ("de", "i", 64), ("caixas", "g", 66, ENT)], XE, 590)
    guia(c, t, C["s13.d"], PLU, 20, 100, "y", CERTO, largura=8)
    marca_eixo(c, t, C["s13.d"] + 0.5, PLU, "100", 100, "y", CERTO)
    E.frase(c, t, C["s13.d"], [("lucro", "g", 66), ("=", "g", 70), ("L(20)", "g", 70), ("=", "g", 70), ("R$", "g", 76, CERTO), ("100", "g", 76, CERTO)], XE, 710)
    E.foco(c, t, C["s13.e"], 0.6, lambda a: (M.rrect(c, XE - 20, 790, 110 + E.larg("releia: quer o", "i", 58) + E.larg("x ou o y?", "g", 64), 170, 44, COR, a),
                                             E.escreve(c, "releia: quer o", XE + 30, 895, 58, "i", BR, a),
                                             E.escreve(c, "x ou o y?", XE + 50 + E.larg("releia: quer o", "i", 58), 895, 64, "g", BR, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    QB = E.Plano(*PL, -0.7, 4.8, -3.5, 24, escuro=True)
    eixos(c, t, QB, C["s14"], tg=C["s14"], marcas=MB, nx="t (s)", ny="h (m)", escuro=True)
    E.curva(c, t, C["s14"] + 0.3, QB, h, 0, 4, d=1.0, cor=CLARO, largura=8)
    tz = pal("s14", "zero", 0, C["s14.a"] + 4.0)
    for k, (xv, t0) in enumerate(((0, tz), (4, C["s14.b"] + 1.6))):
        if t >= t0:
            q = ease_back(prog(t, t0, 0.5))
            c.drawCircle(QB.x(xv), QB.oy, 22 * q, M.paint(AMARELO, 1.0, stroke=7))
            anel(c, t, t0, QB.x(xv), QB.oy, AMARELO)
    bola_voo(c, t, C["s14.c"], QB, h, 0, 4, 2.4, BR, escuro=True, some=True)
    p = ep(t, C["s14.d"], 0.6)
    if p > 0:
        E.chave(c, QB.x(0), QB.x(4), QB.oy + 64, AMARELO, p, 22, 5)
        E.foco(c, t, C["s14.d"] + 0.3, 0.4, lambda a: E.pilula(c, "meio: 2", QB.x(2), QB.oy + 140, 40, "g", fundo=AMARELO, cor=ESCURO, a=a))
        regua(c, t, C["s14.d"] + 0.4, QB, 2, CLARO)
        vertice(c, t, C["s14.d"] + 0.9, QB, 2, 20)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 66, CLARO), XE, 200)
        E.frase(c, t, C["s14.a"], [("o", "i", 66, CLARO), ("topo", "g", 76, BR), ("fica", "i", 66, CLARO), ("no", "i", 66, CLARO), ("meio", "g", 76, AMARELO)], XE, 320)
        E.frase(c, t, C["s14.a"] + 1.4, ps("do voo", "i", 66, CLARO), XE, 410)
        E.frase(c, t, pal("s14", "sem", 0, tz - 1.8), [("sem", "i", 60, CLARO), ("c:", "g", 66, BR), ("uma", "i", 60, CLARO), ("raiz", "i", 60, CLARO), ("é", "i", 60, CLARO), ("0", "g", 70, AMARELO)], XE, 540)
        fml(c, t, C["s14.b"], "a outra:  f{−b}{a} = f{−20}{−5} = 4", XE, 680, 64, BR)
        E.frase(c, t, C["s14.c"], [("sai", "i", 60, CLARO), ("no", "i", 60, CLARO), ("0,", "g", 66, AMARELO), ("volta", "i", 60, CLARO), ("no", "i", 60, CLARO), ("4", "g", 66, AMARELO)], XE, 820)
        E.frase(c, t, C["s14.d"], [("topo:", "i", 70, CLARO), ("2", "g", 86, AMARELO), ("segundos", "g", 70, BR)], XE, 940)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("a", "i", 64, CLARO), ("parábola", "g", 66, BR), ("é", "i", 64, CLARO), ("simétrica", "g", 66, AMARELO)], XE, 260)
    E.frase(c, t, C["s15.a"] + 1.6, ps("vértice no meio das raízes", "i", 56, CLARO), XE, 350, passo=0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 64, ERRADO), ("compensa", "i", 60, CLARO), ("com", "i", 60, CLARO), ("c", "g", 70, BR)], XE, 500)
    E.foco(c, t, C["s15.b"] + 1.0, 0.4, lambda a: E.formula(c, "−x^2 + 40x − 300", XE, 600, 60, "g", CLARO, a))
    E.frase(c, t, pal("s15", "bhaskara", 0, C["s15.b"] + 3.0), [("raízes:", "i", 56, CLARO), ("Bhaskara", "g", 60, ERRADO)], XE, 690)
    E.foco(c, t, C["s15.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 760, 780, 200, 46, CERTO, a),
                                             fsub(c, "x_v = f{−b}{2a}", XE + 30, 885, 84, "g", BR, a),
                                             E.escreve(c, "numa conta só", XE + 70 + fsub(None, "x_v = f{−b}{2a}", 0, 0, 84), 875, 52, "i", BR, a)))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 70, COR), XE, 200)
    E.frase(c, t, C["s16"] + 1.2, [("câmara", "g", 76), ("fria", "g", 76, COR)], XE, 320)
    E.frase(c, t, C["s16.a"], [("t", "g", 70, ENT), ("=", "g", 70, ENT), ("horas", "i", 62), ("depois;", "i", 62), ("T", "g", 70, SAI), ("=", "g", 70, SAI),
                               ("graus", "i", 62)], XE, 440)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: lei(c, LEI_T, XE, 590, 96, a))
    E.frase(c, t, C["s16.c"], [("1)", "g", 64, COR), ("a", "i", 64), ("menor", "g", 64), ("temperatura?", "i", 64)], XE, 750)
    E.frase(c, t, C["s16.d"], [("2)", "g", 64, COR), ("depois", "i", 64), ("de", "i", 64), ("quantas", "i", 64), ("horas?", "g", 64, ENT)], XE, 860)
    E.saida(c, t, C["s17"] - 0.1, lambda: termometro(c, t, C["s16"] + 0.6, C["s16.a"], C["s16.c"]))
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=460, r=180)


def termometro(c, t, t0, t1, t2):
    """termômetro da câmara fria: a coluna desce em t1 e fica com um "?" no ponto mais baixo em t2; sai no relógio"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    cx, y0, y1, w = 1500, 260, 760, 70
    M.rrect(c, cx - w / 2, y0, w, y1 - y0, w / 2, BR, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y0, w, y1 - y0), w / 2, w / 2), M.paint(TINTA, a, stroke=6))
    c.drawCircle(cx, y1 + 40, 70, M.paint(COR, a))
    c.drawCircle(cx, y1 + 40, 70, M.paint(TINTA, a, stroke=6))
    nivel = lerp(0.8, 0.3, ease_io(prog(t, t1, 2.5)))
    M.rrect(c, cx - 18, lerp(y1, y0 + 30, nivel), 36, y1 + 20 - lerp(y1, y0 + 30, nivel), 18, COR, a)
    for i in range(6):
        yy = y0 + 60 + i * 75
        M.line(c, cx + w / 2 + 10, yy, cx + w / 2 + 40, yy, TINTA2, a, 4)
    E.foco(c, t, t2, 0.5, lambda q: E.pilula(c, "menor?", cx + 190, lerp(y1, y0 + 30, 0.3), 46, "g", fundo=COR, a=q * a))


def b_resposta(c, t, C, b):
    plano_camara(c, t, C["s18"])
    E.curva(c, t, C["s18"] + 0.3, PQ, T, 0, 6, d=1.0, cor=COR)
    lei_em(c, t, C["s18"], LEI_T, XE, 200, 70)
    regua(c, t, C["s18.b"] + 0.6, PQ, 3)
    marca_eixo(c, t, C["s18.b"] + 0.9, PQ, "3", 3, "x", ENT)
    vertice(c, t, C["s18.d"] + 0.3, PQ, 3, -4, ("3", "−4"))

    def s18():
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.pilula(c, "a = 1 > 0: ponto mais baixo", XE + 340, 330, 44, "g", fundo=COR, a=a))
        fml(c, t, C["s18.b"], "t_v = f{6}{2} = 3", XE, 500, 80, ENT)
        E.foco(c, t, C["s18.b"] + 1.2, 0.4, lambda a: E.pilula(c, "3 horas", XE + 640, 470, 44, "g", fundo=ENT, a=a))
        fml(c, t, C["s18.c"], "T(3) = 9 − 18 + 5", XE, 680, 76, TINTA)
        fml(c, t, C["s18.d"], "= −4", XE + 180, 820, 84, SAI)
        E.foco(c, t, C["s18.d"] + 0.5, 0.4, lambda a: E.pilula(c, "−4 graus", XE + 560, 795, 46, "g", fundo=SAI, a=a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    guia(c, t, C["s19.a"], PQ, 3, -4, "y", SAI, largura=8)
    marca_eixo(c, t, C["s19.a"] + 0.5, PQ, "−4", -4, "y", SAI)
    guia(c, t, C["s19.b"], PQ, 3, -4, "x", ENT, largura=8)
    E.frase(c, t, C["s19.a"], [("menor", "i", 64), ("temperatura:", "i", 64)], XE, 370)
    E.frase(c, t, C["s19.a"] + 0.8, [("−4", "g", 110, SAI), ("graus", "g", 80)], XE, 500)
    E.frase(c, t, C["s19.b"], [("quando?", "i", 64), ("3", "g", 90, ENT), ("horas", "g", 70, ENT), ("depois", "i", 64)], XE, 640)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.escreve(c, "3 graus?", XE, 820, 80, "g", ERRADO, a))
    if t >= C["s19.c"] + 0.6:
        E.risco(c, XE - 10, 830, XE + 330, 760, t, C["s19.c"] + 0.6, largura=10)
    E.frase(c, t, C["s19.c"] + 0.9, [("parou", "i", 56), ("no", "i", 56), ("x", "g", 64, ERRADO)], XE + 380, 820)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("sinal", "i", 72), ("do", "i", 72), ("a:", "g", 76, CA), ("máximo", "g", 72), ("ou", "i", 72), ("mínimo", "g", 72, COR)]),
                 ("s20.b", [("x", "g", 80, ENT), ("do", "i", 72), ("vértice:", "i", 72), ("quando,", "g", 72, ENT), ("quanto", "g", 72, ENT), ("usar", "i", 72)]),
                 ("s20.c", [("y", "g", 80, SAI), ("do", "i", 72), ("vértice:", "i", 72), ("o", "i", 72), ("valor", "g", 72), ("máximo", "i", 72),
                            ("ou", "i", 72), ("mínimo", "i", 72)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s21.a"], [("monte", "g", 110, COR), ("a", "i", 100), ("função", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s21.b"], [("R$", "g", 64), ("1", "g", 64), ("de", "i", 60), ("desconto", "i", 60)], XE, 570)
    E.frase(c, t, C["s21.b"] + 1.6, [("+10", "g", 70, COR), ("ingressos", "i", 60)], XE, 660)
    E.frase(c, t, C["s21.c"], [("qual", "i", 60, TINTA2), ("preço", "g", 64), ("dá", "i", 60, TINTA2), ("o", "i", 60, TINTA2), ("maior", "i", 60, TINTA2),
                               ("caixa?", "g", 64, COR)], XE, 780)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, bola=b_bola, lucro=b_lucro, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
