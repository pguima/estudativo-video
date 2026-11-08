"""Visual — Estudativo · MAT-FUN-022: estudo do sinal e inequação do 2º grau.

Linguagem visual da trilha Funções (MAT-FUN-001): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; erro em vermelho.
Como na MAT-FUN-011 (sinal da função afim): positiva = região entre a curva e o eixo pintada de verde (E.area), negativa = de
vermelho; o sinal na reta é uma bolinha "+" verde ou "−" vermelha sobre cada trecho, com o trecho da mesma cor.
Como na MAT-FUN-016 a 021: parábola de a > 0 índigo, de a < 0 preta; raízes como anéis índigo no eixo x; trilho dos passos no alto
(o da MAT-FUN-020). A solução da inequação vai na reta numérica embaixo, na cor da matéria (solucao()): bolinha cheia = a ponta entra,
aberta = fica de fora, seta = segue para sempre.
Peças locais: as da trilha (eixos(), par(), fsub(), regua(), marca_eixo(), raiz(), realce(), trilho()) + sinais(), solucao(), mini(), pal()."""
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
POS, NEG = CERTO, ERRADO
SOBE, DESCE = CERTO, ERRADO
ARQUIVO_FINAL = "estudativo_MAT-FUN-022_estudo_do_sinal_e_inequacao_do_2o_grau.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sinal", "metodo", "casos", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERT = "#F2B705"
ESCURO = "#0B0B16"

f = lambda x: x * x - 5 * x + 6
h = lambda x: -x * x + 2 * x + 3
k = lambda x: x * x + 2 * x + 5
q1 = lambda x: -x * x + 6 * x - 8
q2 = lambda x: x * x - 9
gs = lambda x: 0.6 * (x - 1) * (x - 4)
assert 25 - 24 == 1 and f(2) == 0 and f(3) == 0 and abs(f(2.5) + 0.25) < 1e-12 and 2.5 ** 2 == 6.25 and 5 * 2.5 == 12.5
assert h(-1) == 0 and h(3) == 0 and h(1) == 4 and 4 - 20 == -16 and all(k(x / 10) > 0 for x in range(-100, 100)) and f(0) == 6
assert 36 - 32 == 4 and q1(2) == 0 and q1(4) == 0 and q1(3) == 1 and q2(3) == 0 and q2(-3) == 0

PL = (1080, 220, 700, 640)
PF = E.Plano(*PL, -0.4, 5.2, -0.9, 3.4)
MF = ([1, 2, 3, 4, 5], [1, 2, 3])
PS = E.Plano(*PL, -0.5, 5.5, -2.5, 4)
PH = E.Plano(*PL, -2.2, 4.6, -3, 5.2)
MH = ([-1, 1, 2, 3, 4], [-2, 2, 4])
PK = E.Plano(*PL, -4.2, 2.4, -1, 10)
MK = ([-3, -2, -1, 1, 2], [2, 4, 6, 8])
PE = E.Plano(*PL, -0.6, 5.2, -1, 7)
ME = ([1, 2, 3, 4, 5], [2, 4, 6])
PQ1 = E.Plano(*PL, -0.5, 5.5, -3, 2.2)
MQ1 = ([1, 2, 3, 4, 5], [-2, -1, 1])
PQ2 = E.Plano(*PL, -5, 5, -10, 8.5)
MQ2 = ([-4, -3, -2, -1, 1, 2, 3, 4], [-8, -4, 4, 8])
RY = 900  # reta numérica embaixo, à esquerda
RX0, RX1 = XE + 40, XE + 720

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




PASSOS = ("as raízes", "a boca", "o desenho")


def trilho(c, t, t0, ativos):
    """os passos no alto (o da MAT-FUN-020); ativos = instantes em que cada passo vira o da vez"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    x0, dx, y = XE + 30, 330, 120
    M.line(c, x0, y, x0 + dx * (len(PASSOS) - 1), y, FIO, a, 5)
    da_vez = -1
    for i, ti in enumerate(ativos):
        if ti is not None and t >= ti:
            da_vez = i
    for i, nome in enumerate(PASSOS):
        X = x0 + dx * i
        on, feito = i == da_vez, i < da_vez
        cor = COR if on else (TINTA2 if feito else CINZA)
        kk = 1 + 0.25 * ease_back(prog(t, ativos[i], 0.5)) if on else 1
        E.bola(c, X, y, 30 * kk, cor, a)
        centro(c, str(i + 1), X, y + 15, 42, "g", BR, a)
        E.escreve(c, nome, X + 46, y + 14, 40, "g" if on else "i", cor, a)


def reta_s(c, t, t0, vmin, vmax, marcas, y=RY, x0=RX0, x1=RX1, escuro=False, tm=None):
    return E.reta(c, t, t0, x0, x1, y, vmin, vmax, marcas, E._num, escuro=escuro, size=44, tm=tm)


def sinais(c, t, vx, y, cortes, sgs, ts, x0=RX0, x1=RX1, escuro=False):
    """sinal de cada trecho: faixa colorida logo acima da reta e bolinha "+" verde / "−" vermelha; cortes = raízes (valores)"""
    pts = [x0 - 30] + [vx(v) for v in cortes] + [x1 + 40]
    for i, (sg, ti) in enumerate(zip(sgs, ts)):
        if ti is None or t < ti:
            continue
        cor = POS if sg == "+" else NEG if sg == "−" else CINZA
        xa, xb = pts[i], pts[i + 1]
        p = ease_io(prog(t, ti, 0.5))
        M.line(c, xa + 8, y - 34, lerp(xa + 8, xb - 8, p), y - 34, cor, 0.9, 10)
        kk = ease_back(prog(t, ti + 0.15, 0.4))
        if kk > 0:
            cx = (xa + xb) / 2
            E.bola(c, cx, y - 92, 34 * kk, cor)
            centro(c, sg, cx, y - 92 + 20 * kk, 58 * kk, "g", BR, 1.0)


def solucao(c, t, t0, vx, y, ini, fim, fi=False, ff=False, cor=None, x0=RX0, x1=RX1, d=0.6, fundo=None):
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


def mini(c, t, t0, x, y, w, h_, fn, cor=None, d=0.7, escuro=False, ymin=-3, ymax=3, area=None):
    Q = E.plano(c, t, t0, x, y, w, h_, -3, 3, ymin, ymax, grade=False, rotulos=False, size=30, d=0.5, escuro=escuro, nomes=("", ""))
    if area:
        for a_, b_, cor_ in area:
            E.area(c, t, t0 + 0.3, Q, fn, a_, b_, cor=cor_, alfa=0.3, d=d)
    E.curva(c, t, t0 + 0.3, Q, fn, -3, 3, d=d, largura=7, cor=cor)
    return Q


def pinta(c, t, t0, P_, fn, a_, b_, pos, d=0.7, alfa=0.22):
    E.area(c, t, t0, P_, fn, a_, b_, cor=POS if pos else NEG, alfa=alfa, d=d)


def ineq(c, t, t0, s, x, y, size, cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        ineq(c, t, C["s01.a"], "x^2 − 5x + 6 < 0", W / 2, 330, 120, TINTA, "center")
        vx = reta_s(c, t, C["s01.a"] + 0.6, 0, 5, [0, 1, 2, 3, 4, 5], y=720, x0=420, x1=1500)
        for i, v in enumerate((2, 3)):
            kk = ease_back(prog(t, C["s01.b"] + 0.3 * i, 0.4))
            if kk > 0:
                c.drawCircle(vx(v), 720, 22 * kk, M.paint(ERRADO))
        E.frase(c, t, C["s01.b"], [("acha", "i", 66), ("2", "g", 76, ERRADO), ("e", "i", 66), ("3", "g", 76, ERRADO), ("e", "i", 66), ("para?", "g", 70, ERRADO)], W / 2, 520, "center")
        solucao(c, t, C["s01.c"], vx, 720, 2, 3, x0=420, x1=1500, d=0.8)
        E.frase(c, t, C["s01.c"] + 0.4, [("um", "i", 70), ("pedaço", "g", 76, COR), ("inteiro", "g", 76, COR), ("da", "i", 70), ("reta", "i", 70)], W / 2, 920, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("inequação", "g", 100, COR)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.8, [("do", "i", 90), ("2º", "g", 100), ("grau", "i", 90)], XE, 580)
        E.frase(c, t, pal("s02", "olhando", 0, C["s02.a"] + 4.0), [("só", "i", 76), ("olhando", "i", 76), ("a", "i", 76), ("parábola", "g", 80)], XE, 740)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 76), ("precisa", "i", 76), ("de", "i", 76)], XE, 360)
    E.frase(c, t, C["s03.a"], [("3", "g", 220, COR), ("coisas", "i", 100)], XE, 600)
    x, w = 820, 960
    caixas = ((C["s03.b"], 160), (C["s03.c"], 430), (C["s03.d"], 700))
    for t0, y in caixas:
        p = ep(t, t0, 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("raízes:", "g", 60, ENT), ("delta", "i", 56), ("e", "i", 56), ("Bhaskara", "g", 58)], x + 44, 250)
    E.foco(c, t, C["s03.b"] + 0.6, 0.5, lambda a: fsub(c, "x = f{−b ± r{Δ}}{2a}", x + 44, 350, 52, "g", TINTA2, a))
    E.frase(c, t, C["s03.c"] + 0.1, [("sinal", "i", 56), ("do", "i", 56), ("a:", "g", 62, CA), ("para", "i", 56), ("onde", "i", 56), ("abre", "g", 60)], x + 44, 520)
    E.foco(c, t, C["s03.c"] + 0.6, 0.5, lambda a: (E.formula(c, "a > 0", x + 44, 615, 52, "g", COR, a), E.formula(c, "a < 0", x + 420, 615, 52, "g", TINTA, a)))
    for i, (sg, cor) in enumerate(((1, COR), (-1, TINTA))):
        X0 = x + 250 + i * 380
        E.foco(c, t, C["s03.c"] + 0.8, 0.4, lambda a, X0=X0, sg=sg, cor=cor: desenha_boca(c, X0, 600, sg, cor, a))
    E.frase(c, t, C["s03.d"] + 0.1, [("intervalo:", "g", 60), ("o", "i", 56), ("colchete", "i", 56), ("abraça", "g", 60, COR)], x + 44, 790)
    E.foco(c, t, C["s03.d"] + 0.6, 0.5, lambda a: (E.formula(c, "]2, 5]", x + 44, 890, 62, "g", COR, a),
                                                  E.escreve(c, "o 5 entra, o 2 não", x + 260, 885, 48, "i", TINTA2, a)))
    q_ = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(400, 930, q_), ep(t, C["s03.b"], 0.4))


def desenha_boca(c, X0, Y0, sg, cor, a, w=90, h_=60):
    """parábola pequena: sg > 0 sorriso, sg < 0 de cabeça para baixo"""
    pa = skia.Path()
    for i in range(41):
        u = -1 + 2 * i / 40
        (pa.lineTo if i else pa.moveTo)(X0 + u * w / 2, Y0 - sg * (u * u - 0.5) * h_)
    c.drawPath(pa, M.paint(cor, a, stroke=6, cap_round=True))


# ---------------- o sinal ----------------
def b_sinal(c, t, C, b):
    eixos(c, t, PS, C["s04"], tg=None, marcas=([], []))
    E.curva(c, t, C["s04"] + 0.4, PS, gs, 0.2, 5.2, d=1.0, cor=COR)
    pinta(c, t, C["s04.b"], PS, gs, 0.2, 1, True)
    pinta(c, t, C["s04.b"] + 0.3, PS, gs, 4, 5.2, True)
    for xv in (1, 4):
        if t >= C["s04.c"]:
            q_ = ease_back(prog(t, C["s04.c"], 0.5))
            c.drawCircle(PS.x(xv), PS.oy, 22 * q_, M.paint(ENT, 1.0, stroke=7))
            anel(c, t, C["s04.c"], PS.x(xv), PS.oy, ENT)
    pinta(c, t, C["s04.d"], PS, gs, 1, 4, False)
    E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.pilula(c, "+", PS.x(0.5), PS.y(2.6), 56, "g", fundo=POS, a=a))
    E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.pilula(c, "+", PS.x(4.9), PS.y(2.6), 56, "g", fundo=POS, a=a))
    E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: E.pilula(c, "−", PS.x(2.5), PS.y(-0.6), 56, "g", fundo=NEG, a=a))
    E.frase(c, t, C["s04"], ps("estudar o sinal", "i", 66, TINTA2), XE, 230)
    E.frase(c, t, C["s04.a"], [("onde", "i", 70), ("é", "i", 70), ("+,", "g", 84, POS), ("0", "g", 84, ENT), ("ou", "i", 70), ("−", "g", 84, NEG), ("?", "g", 84)], XE, 350)
    E.frase(c, t, C["s04.b"], [("acima", "g", 70), ("do", "i", 64), ("eixo:", "i", 64), ("positiva", "g", 70, POS)], XE, 530)
    E.frase(c, t, C["s04.c"], [("no", "i", 64), ("eixo:", "i", 64), ("zero", "g", 70, ENT)], XE, 650)
    E.frase(c, t, C["s04.d"], [("abaixo", "g", 70), ("do", "i", 64), ("eixo:", "i", 64), ("negativa", "g", 70, NEG)], XE, 770)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    trilho(c, t, C["s05.a"], (C["s05.b"], C["s06.a"], C["s06.c"]))
    eixos(c, t, PF, C["s05.b"], tg=C["s05.b"], marcas=MF)
    raiz(c, t, C["s05.c"] + 0.6, PF, 2, ENT)
    raiz(c, t, C["s05.c"] + 0.9, PF, 3, ENT)
    E.curva(c, t, C["s06.d"], PF, f, 0.6, 4.4, d=1.2, cor=COR)
    pinta(c, t, C["s07.a"], PF, f, 2, 3, False, alfa=0.35)
    pinta(c, t, C["s07.b"], PF, f, 0.6, 2, True)
    pinta(c, t, C["s07.b"] + 0.3, PF, f, 3, 4.4, True)
    lado = ep(t, C["s06.e"], 0.5) * (1 - ep(t, C["s07"], 0.4))
    if lado > 0:
        E.pilula(c, "acima", PF.x(0.9), PF.y(2.3), 40, "g", fundo=POS, a=lado)
        E.pilula(c, "abaixo", PF.x(2.5), PF.oy + 110, 40, "g", fundo=NEG, a=lado)
    if t < C["s07"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("3", "g", 160, COR), ("passos", "i", 90)], XE, 400)
            E.frase(c, t, C["s05.b"], [("1.", "g", 70, COR), ("as", "i", 64), ("raízes", "g", 70)], XE, 560)
            E.foco(c, t, C["s05.b"] + 1.0, 0.5, lambda a: E.formula(c, "x^2 − 5x + 6", XE, 680, 76, "g", TINTA, a))
            fml(c, t, C["s05.c"], "Δ = 1  →  x = 2  e  x = 3", XE, 800, 62, ENT)
        E.saida(c, t, C["s06"] - 0.1, s05)

        def s06():
            E.frase(c, t, C["s06.a"], [("2.", "g", 70, COR), ("a", "i", 64), ("boca", "g", 70)], XE, 300)
            E.frase(c, t, C["s06.b"], [("a", "g", 70, CA), ("=", "g", 70, CA), ("1", "g", 70, CA), ("> 0:", "g", 70, CA), ("abre", "i", 64), ("para", "i", 64), ("cima", "g", 70)], XE, 410)
            E.foco(c, t, C["s06.b"] + 0.5, 0.4, lambda a: desenha_boca(c, XE + 820, 395, 1, COR, a))
            E.frase(c, t, C["s06.c"], [("3.", "g", 70, COR), ("um", "i", 64), ("desenho", "g", 70), ("rápido", "i", 64)], XE, 580)
            E.frase(c, t, C["s06.d"], ps("um sorriso cortando o 2 e o 3", "i", 56, TINTA2), XE, 680, passo=0.1)
            E.frase(c, t, C["s06.e"], [("só", "i", 60), ("importa", "i", 60), ("o", "i", 60), ("lado", "g", 66, COR), ("do", "i", 60), ("eixo", "i", 60)], XE, 820)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    vx = reta_s(c, t, C["s07.a"], 0, 5, [2, 3])
    sinais(c, t, vx, RY, (2, 3), ("+", "−", "+"), (C["s07.b"], C["s07.a"] + 0.3, C["s07.b"] + 0.2))
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], [("entre", "i", 62), ("2", "g", 70, ENT), ("e", "i", 62), ("3:", "g", 70, ENT), ("negativa", "g", 66, NEG)], XE, 270)
            E.frase(c, t, C["s07.b"], [("fora:", "i", 62), ("positiva", "g", 66, POS)], XE, 370)
            E.frase(c, t, C["s07.c"], [("confira", "i", 58), ("com", "i", 58), ("2,5", "g", 66, ENT)], XE, 480)
            tq = pal("s07", "quadrado", 0, C["s07.c"] + 1.4)
            fml(c, t, tq, "2,5^2 = 6,25", XE, 570, 54, TINTA2)
            fml(c, t, pal("s07", "tire", 0, tq + 2.5), "5 · 2,5 = 12,5", XE + 380, 570, 54, TINTA2)
            fml(c, t, pal("s07", "some", 0, tq + 6.0), "6,25 − 12,5 + 6", XE, 660, 60, TINTA)
            fml(c, t, C["s07.d"], "= −0,25", XE + 470, 660, 66, NEG)
            E.foco(c, t, C["s07.d"] + 0.8, 0.4, lambda a: E.pilula(c, "negativo: bateu", XE + 560, 735, 40, "g", fundo=CERTO, a=a))
            E.ponto(c, t, C["s07.d"], PF, 2.5, -0.25, cor=NEG, r=13)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    # respostas: < 0, ≤ 0, > 0
    E.foco(c, t, C["s08"] - 0.2, 0.5, lambda a: E.formula(c, "x^2 − 5x + 6", XE, 270, 70, "g", TINTA, a))
    linhas = ((C["s08.a"], "< 0", "]2, 3[", C["s09.a"]), (C["s09.a"], "≤ 0", "[2, 3]", C["s09.c"]), (C["s09.c"], "> 0", "x < 2  ou  x > 3", None))
    for i, (t0, sg, resp, t1) in enumerate(linhas):
        y = 400 + i * 110
        tr = C["s08.c"] if i == 0 else (C["s09.b"] if i == 1 else C["s09.d"])
        apaga = 1 - 0.55 * (ep(t, t1, 0.4) if t1 else 0)
        E.foco(c, t, t0, 0.5, lambda a, sg=sg, y=y, apaga=apaga: E.formula(c, sg, XE, y, 66, "g", COR, a * apaga))
        E.foco(c, t, tr, 0.5, lambda a, resp=resp, y=y, apaga=apaga: (E.escreve(c, "→", XE + 160, y - 4, 60, "g", TINTA2, a * apaga),
                                                                      E.formula(c, resp, XE + 250, y, 66, "g", TINTA, a * apaga)))
    if t < C["s09"]:
        E.foco(c, t, C["s08.a"] + 0.6, 0.4, lambda a: E.escreve(c, "o pedaço de baixo", XE + 250, 405, 50, "i", NEG, a * (1 - ep(t, C["s08.c"], 0.3))))
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.escreve(c, "sem tracinho: as pontas ficam de fora (valem 0)", XE, 720, 40, "i", TINTA2, a))
    # na reta, a resposta da vez
    E.saida(c, t, C["s09.a"], lambda: solucao(c, t, C["s08.c"], vx, RY, 2, 3))
    E.saida(c, t, C["s09.c"], lambda: solucao(c, t, C["s09.b"], vx, RY, 2, 3, True, True))
    solucao(c, t, C["s09.d"], vx, RY, None, 2)
    solucao(c, t, C["s09.d"] + 0.3, vx, RY, 3, None)
    # no gráfico: as pontas em zero
    if C["s08.b"] <= t < C["s09"]:
        for xv in (2, 3):
            anel(c, t, C["s08.b"], PF.x(xv), PF.oy, NEG)


# ---------------- outros casos ----------------
def b_casos(c, t, C, b):
    if t < C["s11"]:
        eixos(c, t, PH, C["s10"], tg=C["s10"], marcas=MH)
        ineq(c, t, C["s10.a"], "−x^2 + 2x + 3 ≥ 0", XE, 260, 80)
        E.frase(c, t, C["s10"], [("a", "g", 66, CA), ("<", "g", 66, CA), ("0:", "g", 66, CA), ("a", "i", 60), ("boca", "g", 64), ("vira", "i", 60)], XE + 0, 380)
        raiz(c, t, C["s10.b"], PH, -1, ENT, "−1")
        raiz(c, t, C["s10.b"] + 0.3, PH, 3, ENT, "3")
        E.frase(c, t, C["s10.b"], [("raízes", "i", 60), ("−1", "g", 70, ENT), ("e", "i", 60), ("3", "g", 70, ENT)], XE, 490)
        E.curva(c, t, C["s10.c"] - 0.6, PH, h, -1.7, 3.7, d=1.0, cor=TINTA)
        pinta(c, t, C["s10.c"], PH, h, -1, 3, True, alfa=0.3)
        E.frase(c, t, C["s10.c"], [("entre", "i", 60), ("as", "i", 60), ("raízes:", "i", 60), ("acima", "g", 66, POS)], XE, 600)
        vx = reta_s(c, t, C["s10.c"], -2, 4, [-1, 3])
        sinais(c, t, vx, RY, (-1, 3), ("−", "+", "−"), (C["s10.c"] + 0.6, C["s10.c"] + 0.3, C["s10.c"] + 0.8))
        solucao(c, t, C["s10.d"], vx, RY, -1, 3, True, True)
        E.foco(c, t, C["s10.d"] + 0.3, 0.5, lambda a: (E.escreve(c, "tracinho:", XE, 720, 50, "i", TINTA2, a),
                                                      E.formula(c, "[−1, 3]", XE + 260, 725, 76, "g", COR, a)))
        return
    eixos(c, t, PK, C["s11"], tg=C["s11"], marcas=MK)
    E.frase(c, t, C["s11"], ps("e sem raízes?", "i", 64, TINTA2), XE, 240)
    ineq(c, t, C["s11.a"], "x^2 + 2x + 5", XE, 370, 76)
    fml(c, t, C["s11.a"] + 1.6, "Δ = 4 − 20 = −16", XE, 480, 60, TINTA2)
    E.curva(c, t, C["s11.b"] - 0.4, PK, k, -3.8, 1.8, d=1.0, cor=COR)
    pinta(c, t, C["s11.b"] + 0.4, PK, k, -3.8, 1.8, True, alfa=0.2)
    E.frase(c, t, C["s11.b"], [("nunca", "i", 60), ("toca", "i", 60), ("o", "i", 60), ("eixo", "i", 60)], XE, 590)
    vx = reta_s(c, t, C["s11.b"], -4, 2, [-3, -2, -1, 0, 1])
    sinais(c, t, vx, RY, (), ("+",), (C["s11.b"] + 0.6,))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: (E.formula(c, "> 0:", XE, 700, 64, "g", POS, a), E.escreve(c, "todo x real", XE + 190, 700, 60, "g", TINTA, a)))
    q_ = ep(t, C["s11.c"] + 0.3, 0.6)
    if q_ > 0:
        M.line(c, lerp((RX0 + RX1) / 2, RX0 - 30, q_), RY, lerp((RX0 + RX1) / 2, RX1 + 40, q_), RY, COR, 1.0, 12)
        if q_ > 0.95:
            for xa, s_ in ((RX0 - 30, 1), (RX1 + 40, -1)):
                M.line(c, xa, RY, xa + 26 * s_, RY - 18, COR, 1.0, 8); M.line(c, xa, RY, xa + 26 * s_, RY + 18, COR, 1.0, 8)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: (E.formula(c, "< 0:", XE + 560, 700, 64, "g", NEG, a), E.escreve(c, "nenhum", XE + 750, 700, 60, "g", TINTA, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    eixos(c, t, PE, C["s12"] - 3, tg=C["s12"] - 3, marcas=ME)
    E.curva(c, t, C["s12"] - 3, PE, f, -0.1, 4.6, d=0.05, cor=COR)
    ineq(c, t, C["s12"] - 0.2, "x^2 − 5x + 6 < 0", XE, 240, 76)
    E.frase(c, t, C["s12.a"], [("o", "i", 62), ("erro:", "i", 62), ("copiar", "g", 66, ERRADO), ("o", "i", 62), ("sinal", "g", 66, ERRADO)], XE, 370)
    vx = reta_s(c, t, C["s12"] - 3, 0, 5, [0, 2, 3])

    def errado():
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "x < 2  ou  x < 3", XE, 490, 70, "g", ERRADO, a))
        solucao(c, t, C["s12.b"] + 0.6, vx, RY, None, 3, cor=ERRADO)
        q_ = ease_back(prog(t, pal("s12", "teste", 0, C["s12.b"] + 3.0), 0.5))
        if q_ > 0:
            c.drawCircle(vx(0), RY, 20 * q_, M.paint(TINTA))
            E.pilula(c, "o 0 está aí", vx(0) + 40, RY - 70, 36, "g", fundo=TINTA, a=min(1, q_))
    E.saida(c, t, C["s12.e"], errado)
    fml(c, t, C["s12.c"], "f(0) = 0 − 0 + 6 = 6", XE, 640, 64, TINTA)
    E.ponto(c, t, C["s12.c"] + 0.4, PE, 0, 6, cor=POS, r=15)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "positivo: o 0 não serve", XE + 330, 750, 44, "g", fundo=POS, a=a))
    solucao(c, t, C["s12.e"] + 0.4, vx, RY, 2, 3, cor=CERTO)
    E.foco(c, t, C["s12.e"], 0.6, lambda a: (M.rrect(c, XE - 20, 430, 760, 84, 40, CERTO, a),
                                             E.escreve(c, "quem decide o lado é o desenho", XE + 20, 487, 46, "g", BR, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def quadro_atalho():
        y, x0, x1 = 760, 300, 1620
        vx = E.reta(c, t, C["s13"], x0, x1, y, 0, 6, [2, 4], lambda v: "x'" if v == 2 else "x''", escuro=True, size=50)
        zonas = ((x0 - 30, vx(2)), (vx(2), vx(4)), (vx(4), x1 + 40))
        rot = (("mesmo sinal do a", C["s13.a"]), ("contrário", C["s13.b"]), ("mesmo sinal do a", C["s13.a"] + 0.4))
        for (xa, xb), (s, t0) in zip(zonas, rot):
            E.foco(c, t, t0, 0.5, lambda a, xa=xa, xb=xb, s=s: centro(c, s, (xa + xb) / 2, y - 190, 46, "g", AMARELO if s == "contrário" else BR, a))
        sinais(c, t, vx, y, (2, 4), ("+", "−", "+"), (C["s13.c"] + 0.4, C["s13.d"], C["s13.c"] + 0.6), x0=x0, x1=x1, escuro=True)
    E.saida(c, t, C["s14"] - 0.1, quadro_atalho)

    def topo():
        E.frase(c, t, C["s13"], ps("agora, o atalho, sem desenho", "i", 66, CLARO), W / 2, 220, "center")
        E.frase(c, t, C["s13.c"], [("x²", "g", 70, BR), ("−", "g", 70, BR), ("5x", "g", 70, BR), ("+", "g", 70, BR), ("6:", "g", 70, BR), ("a", "g", 70, AMARELO), (">", "g", 70, AMARELO),
                                   ("0", "g", 70, AMARELO)], W / 2, 380, "center")
        E.foco(c, t, C["s13.d"] + 0.4, 0.4, lambda a: E.pilula(c, "entre 2 e 3: negativo", W / 2, 470, 44, "g", fundo=NEG, a=a))
    E.saida(c, t, C["s14"] - 0.1, topo)
    if t < C["s14"]:
        return
    E.foco(c, t, C["s14.a"], 0.5, lambda a: (M.line(c, 1180, 400, 1720, 400, CLARO, a, 4), desenha_boca(c, 1450, 360, 1, CLARO, a, 400, 240)))
    if t >= C["s14.a"] + 0.6:
        p = ep(t, C["s14.a"] + 0.6, 0.5)
        for s_ in (-1, 1):
            M.arrow(c, 1450 + s_ * 230, 260, 1450 + s_ * 230, 170, POS, p, 7, 22, p)
        E.foco(c, t, C["s14.a"] + 0.9, 0.4, lambda a: E.pilula(c, "−", 1450, 500, 44, "g", fundo=NEG, a=a))
    E.frase(c, t, C["s14.a"], [("as", "i", 62, CLARO), ("pontas", "g", 66, BR), ("seguem", "i", 62, CLARO), ("o", "i", 62, CLARO), ("a", "g", 70, AMARELO)], XE, 260)
    E.frase(c, t, C["s14.a"] + 1.6, ps("o miolo afunda", "i", 56, CLARO), XE, 360)
    E.frase(c, t, C["s14.b"], [("não", "g", 64, ERRADO), ("vale:", "i", 60, CLARO), ("Δ", "g", 68, BR), ("≤", "g", 68, BR), ("0", "g", 68, BR)], XE, 600)
    for i, (fn, rot_) in enumerate(((lambda x: 0.3 * x * x, "Δ = 0"), (lambda x: 0.3 * x * x + 0.8, "Δ < 0"))):
        X = 1130 + i * 360
        E.foco(c, t, C["s14.c"] + 0.3 * i, 0.4, lambda a, X=X, rot_=rot_: E.pilula(c, rot_, X + 140, 640, 38, "g", fundo=AMARELO, cor=ESCURO, a=a))
        mini(c, t, C["s14.c"] + 0.3 * i, X, 700, 280, 220, fn, CLARO, escuro=True, ymin=-1, ymax=3, area=((-3, 3, POS),))
    E.frase(c, t, C["s14.c"], ps("um lado só, com o sinal do a", "i", 54, CLARO), XE, 720, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 70, COR), XE, 220)
    E.frase(c, t, C["s15.a"], [("1)", "g", 64, COR)], XE, 420)
    ineq(c, t, C["s15.a"], "−x^2 + 6x − 8 > 0", XE + 110, 420, 92)
    E.frase(c, t, C["s15.b"], [("2)", "g", 64, COR)], XE, 620)
    ineq(c, t, C["s15.b"], "x^2 − 9 ≥ 0", XE + 110, 620, 92)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=460, r=180)


def b_resposta(c, t, C, b):
    if t < C["s18"]:
        eixos(c, t, PQ1, C["s17"], tg=C["s17"], marcas=MQ1)
        ineq(c, t, C["s17"], "−x^2 + 6x − 8 > 0", XE, 240, 76)
        fml(c, t, C["s17.a"], "Δ = 36 − 32 = 4", XE, 370, 62, TINTA2)
        fml(c, t, C["s17.b"], "x = 2  e  x = 4", XE, 480, 66, ENT)
        raiz(c, t, C["s17.b"] + 0.3, PQ1, 2, ENT, "2")
        raiz(c, t, C["s17.b"] + 0.5, PQ1, 4, ENT, "4")
        E.curva(c, t, C["s17.b"] + 0.8, PQ1, q1, 1.1, 4.9, d=1.0, cor=TINTA)
        E.frase(c, t, C["s17.c"], [("a", "g", 62, CA), ("<", "g", 62, CA), ("0:", "g", 62, CA), ("entre", "i", 58), ("→", "g", 58), ("positivo", "g", 62, POS)], XE, 590)
        pinta(c, t, C["s17.c"] + 0.3, PQ1, q1, 2, 4, True, alfa=0.3)
        vx = reta_s(c, t, C["s17.c"], 0, 6, [2, 4])
        sinais(c, t, vx, RY, (2, 4), ("−", "+", "−"), (C["s17.c"] + 0.6, C["s17.c"] + 0.3, C["s17.c"] + 0.8))
        solucao(c, t, C["s17.d"], vx, RY, 2, 4)
        E.foco(c, t, C["s17.d"] + 0.3, 0.5, lambda a: E.formula(c, "]2, 4[", XE + 450, 700, 80, "g", COR, a))
        return
    eixos(c, t, PQ2, C["s18"], tg=C["s18"], marcas=MQ2, size=32)
    ineq(c, t, C["s18"], "x^2 − 9 ≥ 0", XE, 240, 76)
    fml(c, t, C["s18.a"], "x^2 = 9  →  x = −3  e  x = 3", XE, 370, 58, ENT)
    raiz(c, t, C["s18.a"] + 0.6, PQ2, -3, ENT, "−3")
    raiz(c, t, C["s18.a"] + 0.8, PQ2, 3, ENT, "3")
    E.curva(c, t, C["s18.a"] + 1.0, PQ2, q2, -4.2, 4.2, d=1.0, cor=COR)
    E.frase(c, t, C["s18.b"], [("a", "g", 62, CA), (">", "g", 62, CA), ("0:", "g", 62, CA), ("fora", "i", 58), ("→", "g", 58), ("positivo", "g", 62, POS)], XE, 490)
    pinta(c, t, C["s18.b"] + 0.3, PQ2, q2, -4.2, -3, True, alfa=0.3)
    pinta(c, t, C["s18.b"] + 0.5, PQ2, q2, 3, 4.2, True, alfa=0.3)
    vx = reta_s(c, t, C["s18.b"], -5, 5, [-3, 3])
    sinais(c, t, vx, RY, (-3, 3), ("+", "−", "+"), (C["s18.b"] + 0.3, C["s18.b"] + 0.6, C["s18.b"] + 0.5))
    solucao(c, t, C["s18.c"], vx, RY, None, -3, ff=True)
    solucao(c, t, C["s18.c"] + 0.3, vx, RY, 3, None, fi=True)
    E.foco(c, t, C["s18.c"] + 0.4, 0.5, lambda a: E.formula(c, "x ≤ −3  ou  x ≥ 3", XE, 640, 70, "g", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("ache", "i", 72), ("as", "i", 72), ("raízes", "g", 78, ENT)]),
                 ("s19.b", [("veja", "i", 72), ("a", "i", 72), ("boca", "g", 78)]),
                 ("s19.c", [("pegue", "i", 72), ("o", "i", 72), ("pedaço", "g", 78, COR), ("que", "i", 72), ("a", "i", 72), ("pergunta", "i", 72), ("pede", "g", 78)]))
        for i, (kk, partes) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[kk], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                          E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[kk] + 0.1, partes, 340, y, passo=0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "f{(x − 1)(x + 2)}{x − 3} ≥ 0", XE, 460, 80, "g", TINTA, a))
    E.frase(c, t, C["s20.b"], [("o", "i", 90), ("quadro", "g", 100, COR), ("de", "i", 90), ("sinais", "g", 100, COR)], XE, 700)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sinal=b_sinal, metodo=b_metodo, casos=b_casos, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
