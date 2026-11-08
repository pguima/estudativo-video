"""Visual — Estudativo · MAT-FUN-020: montar a função para otimizar.

Linguagem visual da trilha Funções (MAT-FUN-001): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Como na MAT-FUN-016 a 019: na lei, o a em índigo, o b em cinza e o c em preto; parábola de a < 0 preta; o vértice é a esfera
amarela (VERT); régua tracejada em pé no x do vértice; raízes como anéis no eixo x (amarelos no palco escuro); o valor lido ganha
pílula no eixo (índigo no x, preta no y).
Nesta aula: trilho dos 4 passos no alto (passo da vez em índigo); quadro "desconto × preço × vendidos" com a linha do x em destaque;
chuveirinho com setas em arco (o da MAT-EQU-005); o x anotado numa etiqueta índigo ("x = reais de desconto"); ingresso desenhado
(ingresso()); canteiro com muro (canteiro()): tela índigo tracejada nos três lados, lados x em índigo e a frente em preto.
Peças locais: as da trilha (eixos(), par(), lei(), fsub(), vertice(), regua(), guia(), marca_eixo()) + trilho(), quadro(), flecha(),
chuveiro(), ingresso(), canteiro(), raiz(), etiqueta(), pal()."""
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
ARQUIVO_FINAL = "estudativo_MAT-FUN-020_montar_a_funcao_para_otimizar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "show", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERT = "#F2B705"
ESCURO = "#0B0B16"

R = lambda x: (40 - x) * (300 + 10 * x)
Rk = lambda x: R(x) / 1000
A_ = lambda x: x * (40 - 2 * x)
assert all(R(x) == -10 * x * x + 100 * x + 12000 for x in range(-40, 50))
assert 40 * 300 == 12000 and 40 * 10 == 400 and -100 / -20 == 5 and 40 - 5 == 35 and 300 + 50 == 350 and 35 * 350 == 12250 and R(0) == 12000
assert R(40) == 0 and R(-30) == 0 and (40 - 30) / 2 == 5 and 12250 - 12000 == 250
assert A_(0) == 0 and A_(20) == 0 and A_(10) == 200 and 40 - 20 == 20 and 10 * 20 == 200

PL = (1080, 250, 700, 640)
PR = E.Plano(*PL, -36, 58, -2.5, 14.5)
MR = ([-30, -20, -10, 10, 20, 30, 40], [4, 8, 12])
PA = E.Plano(*PL, -2.5, 23, -30, 235)
MA = ([5, 10, 15, 20], [100, 200])
LEI_R = "R(x) = (40 − x)(300 + 10x)"
LEI_RA = [("R(x) = ", TINTA), ("−10x^2", CA), (" + 100x", CB), (" + 12.000", CC)]

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


def flecha(c, t, t0, x0, y0, x1, y1, alto, cor, d=0.6, largura=6):
    """arco de (x0, y0) a (x1, y1) com ponta de seta; alto > 0 sobe, alto < 0 desce (MAT-EQU-005)"""
    p = ep(t, t0, d)
    if p <= 0:
        return
    cx = (x0 + x1) / 2
    cy = (min(y0, y1) - alto) if alto > 0 else (max(y0, y1) - alto)
    pt = lambda u: ((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x1, (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y1)
    n = max(2, int(30 * p))
    path = skia.Path()
    path.moveTo(*pt(0))
    for i in range(1, n + 1):
        path.lineTo(*pt(p * i / n))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.97:
        ang = math.atan2(y1 - cy, x1 - cx)
        for da in (2.6, -2.6):
            M.line(c, x1, y1, x1 + 24 * math.cos(ang + da), y1 + 24 * math.sin(ang + da), cor, 1.0, largura)


def chuveiro(c, t, ts, s, termos, x, y, size, cor, align="left", alto=70):
    """as quatro setas do chuveirinho em ts = (a·c, a·d, b·c, b·d); termos = (a, b, c, d) como aparecem em s"""
    a1, b1, a2, b2 = termos
    pos = lambda tr, n=0: trecho_x(s, tr, x, size, align, n)
    (xa1, wa1), (xb1, wb1), (xa2, wa2), (xb2, wb2) = pos(a1), pos(b1), pos(a2), pos(b2)
    topo, base = y - size * 0.95, y + size * 0.2
    flecha(c, t, ts[0], xa1 + wa1 / 2, topo, xa2 + wa2 / 2, topo, alto * 1.3, cor)
    flecha(c, t, ts[1], xa1 + wa1 / 2, topo, xb2 + wb2 / 2, topo, alto * 2.1, cor)
    flecha(c, t, ts[2], xb1 + wb1 / 2, base, xa2 + wa2 / 2, base, -alto * 1.3, cor)
    flecha(c, t, ts[3], xb1 + wb1 / 2, base, xb2 + wb2 / 2, base, -alto * 2.1, cor)


def plano_r(c, t, t0, escuro=False):
    eixos(c, t, PR, t0, tg=t0, marcas=MR, nx="x (R$)", ny="R (mil R$)", size=32, escuro=escuro)


def plano_a(c, t, t0):
    eixos(c, t, PA, t0, tg=t0, marcas=MA, nx="x (m)", ny="área")


def raiz(c, t, t0, P_, xv, cor=AMARELO, rot=None, size=40):
    """raiz como anel no eixo x, com o valor numa pílula embaixo"""
    if t < t0:
        return
    q = ease_back(prog(t, t0, 0.5))
    c.drawCircle(P_.x(xv), P_.oy, 22 * q, M.paint(cor, 1.0, stroke=7))
    anel(c, t, t0, P_.x(xv), P_.oy, cor)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.pilula(c, rot, P_.x(xv), P_.oy + 56, size, "g", fundo=cor, cor=ESCURO if cor == AMARELO else BR, a=a))


def etiqueta(c, s, x, y, size, a=1.0, cor=ENT):
    """a anotação do x: etiqueta índigo com o furo do barbante"""
    if a <= 0:
        return
    w, h_ = E.larg(s, "g", size) + size * 1.6, size * 1.6
    pth = skia.Path()
    pth.moveTo(x, y)
    pth.lineTo(x + h_ * 0.45, y - h_ / 2)
    pth.lineTo(x + w, y - h_ / 2)
    pth.lineTo(x + w, y + h_ / 2)
    pth.lineTo(x + h_ * 0.45, y + h_ / 2)
    pth.close()
    c.drawPath(pth, M.paint(cor, a))
    c.drawCircle(x + h_ * 0.42, y, size * 0.14, M.paint(BR, a))
    E.escreve(c, s, x + h_ * 0.75, y + size * 0.35, size, "g", BR, a)


# ---------------- ingresso e trilho ----------------
def ingresso(c, cx, cy, preco, a=1.0, cor=COR, w=540, h_=200, risca=0.0):
    """ingresso com picote e o preço no meio"""
    if a <= 0:
        return
    p = skia.Path()
    p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h_ / 2, w, h_), 24, 24))
    for sx in (-1, 1):
        f = skia.Path()
        f.addCircle(cx + sx * w / 2, cy, 30)
        p = skia.Op(p, f, skia.PathOp.kDifference_PathOp)
    c.drawPath(p, M.paint(cor, a))
    xp = cx - w / 2 + 110
    M.line(c, xp, cy - h_ / 2 + 22, xp, cy + h_ / 2 - 22, BR, 0.6 * a, 4, dash=[10, 10])
    centro(c, "show", cx - w / 2 + 56, cy + 12, 34, "i", BR, 0.85 * a)
    centro(c, preco, cx + 55, cy + 30, 84, "g", BR, a)
    if risca > 0:
        M.line(c, cx - w / 2 + 120, cy + 50, lerp(cx - w / 2 + 120, cx + w / 2 - 20, risca), lerp(cy + 50, cy - 50, risca), ERRADO, a, 12)


PASSOS = ("o que varia", "cada parte", "a função", "o vértice")


def trilho(c, t, t0, ativos):
    """os 4 passos no alto; ativos = instantes em que cada passo vira o da vez"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    x0, dx, y = XE + 30, 430, 120
    M.line(c, x0, y, x0 + dx * 3, y, FIO, a, 5)
    da_vez = -1
    for i, ti in enumerate(ativos):
        if ti is not None and t >= ti:
            da_vez = i
    for i, nome in enumerate(PASSOS):
        X = x0 + dx * i
        on = i == da_vez
        feito = i < da_vez
        cor = COR if on else (TINTA2 if feito else CINZA)
        k = 1 + 0.25 * ease_back(prog(t, ativos[i], 0.5)) if (on and ativos[i] is not None) else 1
        E.bola(c, X, y, 30 * k, cor, a)
        centro(c, str(i + 1), X, y + 15, 42, "g", BR, a)
        E.escreve(c, nome, X + 46, y + 14, 40, "g" if on else "i", cor, a)


# ---------------- quadro desconto × preço × vendidos ----------------
QX, QY, QW, QH = 1000, 330, 260, 96
QCAB = (("desconto", ENT), ("preço", TINTA), ("vendidos", TINTA))
QLIN = (("0", "40", "300"), ("1", "39", "310"), ("2", "38", "320"), ("x", "40 − x", "300 + 10x"))


def quadro(c, t, tc, tcols, a=1.0, mult=None):
    """quadro em pé; tcols[j] = instante da coluna j (as linhas entram uma a uma); a última linha (a do x) fica em destaque"""
    q = ep(t, tc, 0.5) * a
    if q <= 0:
        return
    for j, (nome, cor) in enumerate(QCAB):
        centro(c, nome, QX + QW * j + QW / 2, QY - 26, 44, "b", cor, q)
    M.line(c, QX, QY, QX + 3 * QW, QY, TINTA, q, 4)
    for j in (1, 2):
        M.line(c, QX + QW * j, QY, QX + QW * j, QY + QH * 4 + 10, TINTA, q, 4)
    ry = QY + 10 + QH * 3
    k = ep(t, tcols[0] + 1.0, 0.5) * a
    if k > 0:
        M.rrect(c, QX - 10, ry + 4, 3 * QW + 20, QH - 8, 16, COR, 0.13 * k)
    for j in range(3):
        if tcols[j] is None:
            continue
        for i, row in enumerate(QLIN):
            v = row[j]
            yy = QY + 10 + QH * i + QH / 2 + 22
            cor = ENT if j == 0 else TINTA
            E.foco(c, t, tcols[j] + 0.25 * i, 0.4, lambda z, v=v, j=j, yy=yy, cor=cor, i=i: E.formula(
                c, v, QX + QW * j + QW / 2, yy, 58 if i < 3 else 44, "g", cor, z * a, "center"), sobe=6)
    if mult is not None:
        E.foco(c, t, mult, 0.4, lambda z: E.pilula(c, "×", QX + QW * 2, ry + 6, 30, "g", fundo=COR, a=z * a), sobe=0)


# ---------------- canteiro ----------------
def canteiro(c, t, t0, x0, y0, w, h_, tm=None, ta=None, rl=None, rf=None, tr=None, a=1.0, area=None):
    """muro em cima (cinza, hachurado); tela índigo tracejada nos três lados; rl / rf = rótulos dos lados e da frente em tr"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    # muro
    mq = q * (1 if tm is None else 0.6 + 0.4 * ep(t, tm, 0.4))
    M.rrect(c, x0 - 60, y0 - 46, w + 120, 46, 6, CINZA, mq)
    for i in range(int((w + 120) / 40)):
        xx = x0 - 60 + 20 + i * 40
        M.line(c, xx, y0 - 6, xx + 24, y0 - 40, PAPEL_ESC, mq, 3)
    E.foco(c, t, t0 + 0.2, 0.4, lambda z: centro(c, "muro", x0 + w / 2, y0 - 62, 40, "i", TINTA2, z * a))
    # área
    if ta is not None:
        k = ep(t, ta, 0.6) * a
        if k > 0:
            c.drawRect(skia.Rect.MakeXYWH(x0, y0, w, h_), M.paint(CERTO, 0.16 * k))
            if area:
                centro(c, area, x0 + w / 2, y0 + h_ / 2 + 20, 56, "g", CERTO, k)
    # tela nos três lados
    p = ease_io(prog(t, t0 + 0.3, 1.0))
    pts = [(x0, y0), (x0, y0 + h_), (x0 + w, y0 + h_), (x0 + w, y0)]
    tot = 2 * h_ + w
    feito = p * tot
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        L_ = math.hypot(xb - xa, yb - ya)
        u = max(0.0, min(1.0, feito / L_))
        feito -= L_
        if u > 0:
            M.line(c, xa, ya, lerp(xa, xb, u), lerp(ya, yb, u), COR, q, 9, dash=[22, 12])
    if rl and tr is not None:
        E.foco(c, t, tr[0], 0.4, lambda z: (E.escreve(c, rl, x0 - 30 - E.larg(rl, "g", 60), y0 + h_ / 2 + 20, 60, "g", ENT, z * a),
                                            E.escreve(c, rl, x0 + w + 30, y0 + h_ / 2 + 20, 60, "g", ENT, z * a)))
    if rf and tr is not None and len(tr) > 1:
        E.foco(c, t, tr[1], 0.4, lambda z: E.formula(c, rf, x0 + w / 2, y0 + h_ + 76, 56, "g", TINTA, z * a, "center"))


PAPEL_ESC = "#6E6E74"


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        n = int(min(3, 4 * prog(t, C["s01.b"] + 1.0, 3.0))) if t >= C["s01.b"] + 1.0 else 0
        E.foco(c, t, C["s01.a"], 0.5, lambda a: ingresso(c, 1440, 330, f"R$ {40 - n}", a))
        E.foco(c, t, C["s01.a"] + 1.4, 0.5, lambda a: (centro(c, f"{300 + 10 * n}", 1440, 600, 120, "g", TINTA, a),
                                                      centro(c, "ingressos vendidos", 1440, 670, 46, "i", TINTA2, a)))
        if t >= C["s01.b"] + 1.0 and n > 0:
            E.foco(c, t, C["s01.b"] + 1.0, 0.3, lambda a: (E.pilula(c, f"−R$ {n}", 1720, 250, 40, "g", fundo=ERRADO, a=a),
                                                          E.pilula(c, f"+{10 * n}", 1660, 530, 40, "g", fundo=CERTO, a=a)), sobe=0)
        E.frase(c, t, C["s01"], ps("um show", "i", 66, TINTA2), XE, 230)
        E.frase(c, t, C["s01.a"], [("R$", "g", 90), ("40", "g", 90), ("o", "i", 66), ("ingresso", "i", 66)], XE, 350)
        E.frase(c, t, C["s01.a"] + 1.4, [("300", "g", 90), ("ingressos", "i", 66)], XE, 460)
        E.frase(c, t, C["s01.b"], [("cada", "i", 60), ("R$", "g", 66, ERRADO), ("1", "g", 66, ERRADO), ("de", "i", 60), ("desconto", "i", 60)], XE, 600)
        E.frase(c, t, C["s01.b"] + 1.4, [("vende", "i", 60), ("+10", "g", 70, CERTO), ("ingressos", "i", 60)], XE + 60, 690)
        E.frase(c, t, C["s01.c"], [("baixar", "i", 70), ("o", "i", 70), ("preço", "g", 70), ("enche", "i", 70), ("o", "i", 70), ("caixa?", "g", 76, COR)], XE, 830)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: E.pilula(c, "só até certo ponto", 1440, 860, 54, "g", fundo=COR, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 280)
        E.frase(c, t, C["s02.a"] + 1.0, [("história", "g", 104), ("→", "g", 96, COR)], XE, 430)
        E.frase(c, t, C["s02.a"] + 2.2, [("função", "g", 110, COR)], XE, 570)
        E.frase(c, t, C["s02.b"], [("o", "i", 84), ("melhor", "g", 90), ("valor", "i", 84)], XE, 740)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
CH = "(a + b)(c + d)"


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 76), ("precisa", "i", 76), ("de", "i", 76)], XE, 360)
    E.frase(c, t, C["s03.a"], [("2", "g", 220, COR), ("coisas", "i", 100)], XE, 600)
    x, w = 860, 920
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 170, w, 330, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("o", "i", 60), ("vértice:", "g", 60, VERT), ("máximo", "i", 56), ("ou", "i", 56), ("mínimo", "i", 56)], x + 44, 260)
    tx_ = pal("s03", "xis", 0, C["s03.b"] + 2.4)
    E.frase(c, t, tx_, [("x", "g", 64, ENT), ("→", "g", 56, TINTA2), ("quanto", "g", 56, ENT), ("usar", "g", 56, ENT)], x + 44, 360)
    E.frase(c, t, pal("s03", "ípsilon", 0, tx_ + 1.6), [("y", "g", 64, SAI), ("→", "g", 56, TINTA2), ("o", "i", 56), ("valor", "g", 56)], x + 44, 450)
    p = ep(t, C["s03.c"], 0.5)
    E.caixa_pontilhada(c, x, 560, w, 380, p, prog_=p)
    E.frase(c, t, C["s03.c"] + 0.1, [("o", "i", 60), ("chuveirinho", "g", 60, COR)], x + 44, 650)
    tc = pal("s03", "cada", 0, C["s03.c"] + 3.0)
    E.foco(c, t, C["s03.c"] + 0.6, 0.5, lambda a: E.formula(c, CH, x + w / 2, 840, 84, "g", TINTA, a, "center"))
    chuveiro(c, t, (tc, tc + 0.5, tc + 1.0, tc + 1.5), CH, ("a", "b", "c", "d"), x + w / 2, 840, 84, COR, "center", alto=34)
    q_ = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(470, 900, q_), ep(t, C["s03.b"], 0.4))


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    trilho(c, t, C["s04.a"], (C["s04.b"], C["s05.a"], C["s06.a"], C["s08.a"]))
    # o quadro, do passo 1 ao 3
    if t < C["s07"]:
        E.saida(c, t, C["s07"] - 0.1, lambda: quadro(c, t, C["s04.c"] + 0.4, (C["s04.c"] + 0.8, C["s05.b"], C["s05.c"]), mult=C["s06.b"] + 0.8))
    # etiqueta do x: fica até o fim do bloco
    tl = C["s04.c"]
    E.foco(c, t, tl + 0.4, 0.5, lambda a: etiqueta(c, "x = reais de desconto", XE, 960, 44, a), sobe=0)

    def s04():
        E.frase(c, t, C["s04.a"], [("4", "g", 200, COR), ("passos", "i", 100)], XE, 420)
        E.frase(c, t, C["s04.b"], [("1.", "g", 72, COR), ("escolha", "i", 66), ("o", "i", 66), ("que", "i", 66), ("varia", "g", 72)], XE, 580)
        E.frase(c, t, C["s04.b"] + 1.6, [("e", "i", 66), ("chame", "i", 66), ("de", "i", 66), ("x", "g", 84, ENT)], XE + 60, 680)
    E.saida(c, t, C["s05"] - 0.1, s04)

    def s05():
        E.frase(c, t, C["s05.a"], [("2.", "g", 72, COR), ("cada", "i", 66), ("parte", "g", 70), ("com", "i", 66), ("x", "g", 80, ENT)], XE, 330)
        fml(c, t, C["s05.b"], "preço = 40 − x", XE, 520, 84, TINTA)
        fml(c, t, C["s05.c"], "vendidos = 300 + 10x", XE, 680, 68, TINTA)
        E.frase(c, t, C["s05.c"] + 2.0, ps("10 a mais por real de desconto", "i", 46, TINTA2), XE, 770, passo=0.08)
    E.saida(c, t, C["s06"] - 0.1, s05)

    def s06():
        E.frase(c, t, C["s06.a"], [("3.", "g", 72, COR), ("monte", "i", 66), ("a", "i", 66), ("função", "g", 70)], XE, 330)
        E.frase(c, t, C["s06.b"], [("receita", "g", 76, COR), ("=", "g", 70), ("dinheiro", "i", 62), ("que", "i", 62), ("entra", "i", 62)], XE, 470)
        E.frase(c, t, C["s06.b"] + 1.4, [("=", "g", 70), ("preço", "g", 70), ("×", "g", 70, COR), ("quantidade", "g", 70)], XE, 570)
        E.foco(c, t, C["s06.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 650, 800, 170, 44, COR, a),
                                                 E.formula(c, LEI_R, XE + 380, 760, 62, "g", BR, a, "center")))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            y0, size = 360, 92
            E.foco(c, t, C["s07"], 0.5, lambda a: E.formula(c, LEI_R, W / 2, y0, size, "g", TINTA, a, "center"))
            ts = (C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"])
            chuveiro(c, t, ts, LEI_R, ("40", "− x", "300", "+ 10x"), W / 2, y0, size, COR, "center", alto=60)
            itens = (("40 · 300 = 12.000", ts[0]), ("40 · 10x = 400x", ts[1]), ("−x · 300 = −300x", ts[2]), ("−x · 10x = −10x^2", ts[3]))
            for i, (s, ti) in enumerate(itens):
                X = W / 2 - 430 + (i % 2) * 860
                Y = 580 + (i // 2) * 100
                fml(c, t, ti + 0.4, s, X, Y, 64, TINTA2 if i else TINTA, "center")
            E.foco(c, t, C["s07.e"], 0.6, lambda a: (M.rrect(c, W / 2 - 560, 730, 1120, 160, 44, COR, a),
                                                     lei(c, [("R(x) = ", BR), ("−10x^2", BR), (" + 100x", BR), (" + 12.000", BR)], W / 2, 835, 76, a, "center")))
            # 400x − 300x = 100x
            E.foco(c, t, C["s07.e"] + 0.6, 0.4, lambda a: E.pilula(c, "400x − 300x = 100x", W / 2 + 430, 950, 36, "g", fundo=TINTA2, a=a))
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s08"]:
        return
    plano_r(c, t, C["s08.a"])
    E.curva(c, t, C["s08.a"] + 0.4, PR, Rk, -30, 40, d=1.2, cor=TINTA)
    tdiv = pal("s08", "dividido", 0, C["s08.c"] + 2.0)
    regua(c, t, tdiv + 0.8, PR, 5)
    marca_eixo(c, t, C["s08.d"], PR, "5", 5, "x", ENT)
    vertice(c, t, C["s08.d"] + 0.3, PR, 5, 12.25)
    pos = lei_em(c, t, C["s08.a"], LEI_RA, XE, 330, 54)
    E.frase(c, t, C["s08.a"], [("4.", "g", 60, COR), ("o", "i", 56), ("vértice", "g", 60, VERT)], XE, 230)
    sob_parte(c, t, C["s08.a"] + 1.4, pos, 1, 330, "a = −10", CA, 40)
    sob_parte(c, t, C["s08.c"], pos, 2, 330, "b = 100", CB, 40, apara=larg_f(" + ", 54))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "tem máximo", XE + 150, 480, 40, "g", fundo=SAI, a=a))
    fml(c, t, tdiv, "x_v = f{−100}{−20} = 5", XE, 660, 80, ENT)
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.pilula(c, "desconto de R$ 5", XE + 300, 810, 54, "g", fundo=ENT, a=a))


# ---------------- a resposta do show ----------------
def b_show(c, t, C, b):
    plano_r(c, t, C["s09"])
    E.curva(c, t, C["s09"] + 0.2, PR, Rk, -30, 40, d=0.6, cor=TINTA)
    vertice(c, t, C["s09"] + 0.6, PR, 5, 12.25, ("5", "12.250"), abaixo=False)
    regua(c, t, C["s09"] + 0.6, PR, 5, a=0.6)
    guia(c, t, C["s09.d"] + 0.6, PR, 5, 12.25, "y", SAI)
    E.ponto(c, t, C["s09.e"], PR, 0, 12, cor=TINTA2, r=13)
    E.foco(c, t, C["s09"], 0.5, lambda a: etiqueta(c, "x = reais de desconto", XE, 200, 40, a), sobe=0)
    E.frase(c, t, C["s09.a"], [("pedido:", "i", 66), ("o", "i", 66), ("preço", "g", 76, COR)], XE, 340)
    fml(c, t, C["s09.b"], "40 − 5 = 35", XE, 470, 80, TINTA)
    E.foco(c, t, C["s09.b"] + 1.0, 0.4, lambda a: E.pilula(c, "R$ 35", XE + 620, 445, 50, "g", fundo=CERTO, a=a))
    fml(c, t, C["s09.c"], "300 + 10 · 5 = 350", XE, 590, 64, TINTA2)
    E.foco(c, t, C["s09.c"] + 0.6, 0.4, lambda a: E.escreve(c, "ingressos", XE + 610, 590, 50, "i", TINTA2, a))
    fml(c, t, C["s09.d"], "R = 35 · 350 = 12.250", XE, 730, 76, SAI)
    E.frase(c, t, C["s09.e"], [("antes:", "i", 58, TINTA2), ("12.000", "g", 62, TINTA2)], XE, 850)
    E.foco(c, t, pal("s09", "rendeu", 0, C["s09.e"] + 1.6), 0.5, lambda a: E.pilula(c, "+ R$ 250", XE + 560, 830, 50, "g", fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], ps("o erro mais comum", "i", 70), XE, 230)

    def errado():
        E.foco(c, t, C["s10.a"], 0.5, lambda a: ingresso(c, 1430, 380, "R$ 5", a, ERRADO, risca=ep(t, C["s10.b"], 0.5)))
    E.saida(c, t, C["s10.c"], errado)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: ingresso(c, 1430, 380, "R$ 35", a, CERTO))
    E.frase(c, t, C["s10.a"], [("responder", "i", 70), ("R$", "g", 80, ERRADO), ("5", "g", 80, ERRADO)], XE, 360)
    E.frase(c, t, C["s10.b"], [("5", "g", 80, ENT), ("=", "g", 76, ENT), ("o", "i", 66), ("desconto", "g", 70, ENT), ("(o", "i", 62, TINTA2), ("x)", "g", 66, ENT)], XE, 490)
    E.frase(c, t, C["s10.c"], [("a", "i", 66), ("pergunta:", "i", 66), ("o", "i", 66), ("preço", "g", 70), ("→", "g", 66), ("R$", "g", 80, CERTO), ("35", "g", 80, CERTO)],
            XE, 620)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: etiqueta(c, "x = reais de desconto", XE, 800, 58, a), sobe=0)
    E.frase(c, t, pal("s10", "volte", 0, C["s10.d"] + 2.4), ps("volte aqui antes de responder", "i", 52, TINTA2), XE, 920, passo=0.1)
    if t >= C["s10.d"]:
        p = ease_io(prog(t, C["s10.d"] + 0.3, 0.8))
        E.cursor(c, lerp(1100, 900, p), lerp(950, 815, p), ep(t, C["s10.d"] + 0.2, 0.4))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    QR = E.Plano(*PL, -36, 58, -2.5, 14.5, escuro=True)
    eixos(c, t, QR, C["s11"], tg=C["s11"], marcas=MR, nx="x (R$)", ny="R (mil R$)", size=32, escuro=True)
    E.curva(c, t, C["s11"] + 0.3, QR, Rk, -30, 40, d=1.0, cor=CLARO, largura=8)
    raiz(c, t, C["s11.c"] + 1.0, QR, 40, rot="40")
    raiz(c, t, C["s11.d"] + 1.0, QR, -30, rot="−30")
    if t < C["s12"]:
        def s11():
            y0, size = 330, 76
            E.frase(c, t, C["s11"], ps("agora, o atalho", "i", 62, CLARO), XE, 190)
            E.foco(c, t, C["s11"] + 0.4, 0.5, lambda a: E.formula(c, LEI_R, XE, y0, size, "g", BR, a))
            E.frase(c, t, C["s11.a"], [("não", "g", 64, AMARELO), ("abra", "i", 60, CLARO), ("os", "i", 60, CLARO), ("parênteses", "i", 60, CLARO)], XE, 450)
            E.frase(c, t, C["s11.b"], [("R", "g", 62, BR), ("=", "g", 62, BR), ("0:", "g", 62, BR), ("um", "i", 58, CLARO), ("parêntese", "i", 58, CLARO), ("vale", "i", 58, CLARO),
                                       ("0", "g", 62, AMARELO)], XE, 560)
            realce(c, t, C["s11.c"], LEI_R, "(40 − x)", XE, y0, size, AMARELO)
            fml(c, t, C["s11.c"] + 0.6, "40 − x = 0  →  x = 40", XE, 690, 58, BR)
            E.frase(c, t, pal("s11", "ingresso", 0, C["s11.c"] + 2.6), ps("ingresso de graça", "i", 46, CLARO), XE + 60, 770, passo=0.1)
            realce(c, t, C["s11.d"], LEI_R, "(300 + 10x)", XE, y0, size, AMARELO)
            fml(c, t, C["s11.d"] + 0.6, "300 + 10x = 0  →  x = −30", XE, 890, 58, BR)
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    p = ep(t, C["s12.a"], 0.6)
    if p > 0:
        E.chave(c, QR.x(-30), QR.x(40), QR.oy + 110, AMARELO, p, 22, 5)
        regua(c, t, C["s12.c"], QR, 5, CLARO)
        E.foco(c, t, C["s12.c"] + 0.3, 0.4, lambda a: E.pilula(c, "meio: 5", QR.x(5), QR.oy + 190, 40, "g", fundo=AMARELO, cor=ESCURO, a=a))
        vertice(c, t, C["s12.c"] + 0.6, QR, 5, 12.25)
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12.a"], [("vértice", "g", 70, BR), ("no", "i", 64, CLARO), ("meio", "g", 70, AMARELO), ("das", "i", 64, CLARO), ("raízes", "i", 64, CLARO)], XE, 280)
            fml(c, t, C["s12.b"], "40 + (−30) = 10", XE, 450, 76, BR)
            fml(c, t, C["s12.c"], "10 ÷ 2 = 5", XE, 590, 76, AMARELO)
            E.frase(c, t, C["s12.c"] + 1.4, [("o", "i", 58, CLARO), ("mesmo", "i", 58, CLARO), ("desconto,", "i", 58, CLARO)], XE, 740)
            E.frase(c, t, C["s12.c"] + 2.0, [("sem", "g", 62, BR), ("chuveirinho", "g", 62, AMARELO)], XE, 830)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], [("a", "i", 62, CLARO), ("parábola", "g", 64, BR), ("é", "i", 62, CLARO), ("simétrica", "g", 64, AMARELO)], XE, 250)
    E.frase(c, t, C["s13.b"], [("−30:", "g", 64, AMARELO), ("só", "i", 58, CLARO), ("um", "i", 58, CLARO), ("número", "i", 58, CLARO), ("da", "i", 58, CLARO), ("conta", "g", 60, BR)],
            XE, 380)
    E.frase(c, t, C["s13.c"], [("não", "g", 62, ERRADO), ("compensa:", "i", 58, CLARO), ("sem", "i", 58, CLARO), ("produto", "g", 62, BR)], XE, 530)
    E.foco(c, t, pal("s13", "lucro", 0, C["s13.c"] + 4.0), 0.4, lambda a: E.formula(c, "L(x) = −x^2 + 40x − 300", XE, 630, 56, "g", CLARO, a))
    E.foco(c, t, C["s13.d"], 0.6, lambda a: (M.rrect(c, XE - 20, 720, 560, 200, 46, CERTO, a),
                                             fsub(c, "x_v = f{−b}{2a}", XE + 30, 845, 84, "g", BR, a)))


# ---------------- questão ----------------
CX, CY, CW, CHh = 1180, 300, 520, 360


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 70, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("40", "g", 84, COR), ("m", "g", 70, COR), ("de", "i", 62), ("tela", "g", 66)], XE, 330)
    E.frase(c, t, C["s14.b"], [("muro:", "g", 58, TINTA2), ("1", "g", 62), ("lado;", "i", 58), ("tela:", "g", 58, COR), ("os", "i", 58), ("outros", "i", 58), ("3", "g", 62, COR)], XE, 450)
    E.frase(c, t, C["s14.c"], [("área", "g", 62), ("=", "g", 62), ("comprimento", "i", 58), ("×", "g", 62), ("largura", "i", 58)], XE, 570)
    E.frase(c, t, C["s14.d"], [("1)", "g", 60, COR), ("medidas", "i", 60), ("da", "i", 60), ("maior", "g", 62), ("área?", "g", 62)], XE, 740)
    E.frase(c, t, C["s14.e"], [("2)", "g", 60, COR), ("qual", "i", 60), ("é", "i", 60), ("essa", "i", 60), ("área?", "g", 62)], XE, 850)
    E.saida(c, t, C["s15"] - 0.1, lambda: (canteiro(c, t, C["s14.a"], CX, CY, CW, CHh, tm=C["s14.b"], ta=C["s14.c"], area="?"),
                                           E.foco(c, t, C["s14.a"] + 0.8, 0.4, lambda a: centro(c, "40 m de tela", CX + CW / 2, CY + CHh + 90, 46, "i", COR, a))))
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1440, cy=460, r=180)


def b_resposta(c, t, C, b):
    if t < C["s17"]:
        canteiro(c, t, C["s16"], CX, CY, CW, CHh, rl="x", rf="40 − 2x", tr=(C["s16.a"], C["s16.b"]))
        E.frase(c, t, C["s16.a"], [("x", "g", 84, ENT), ("=", "g", 76, ENT), ("cada", "i", 62), ("lado", "g", 66), ("que", "i", 62), ("sai", "i", 62), ("do", "i", 62),
                                   ("muro", "i", 62)], XE, 300)
        E.foco(c, t, C["s16.a"] + 0.3, 0.5, lambda a: etiqueta(c, "x = lado que sai do muro", XE, 420, 40, a), sobe=0)
        E.frase(c, t, C["s16.b"], [("frente:", "i", 62), ("sobra", "i", 62)], XE, 580)
        fml(c, t, C["s16.b"] + 0.6, "40 − 2x", XE + 400, 580, 76, TINTA)
        E.foco(c, t, C["s16.c"], 0.6, lambda a: (M.rrect(c, XE - 20, 680, 640, 170, 44, COR, a),
                                                 E.formula(c, "A(x) = x(40 − 2x)", XE + 300, 790, 70, "g", BR, a, "center")))
        return
    plano_a(c, t, C["s17"])
    E.curva(c, t, C["s17"] + 0.3, PA, A_, 0, 20, d=1.0, cor=TINTA)
    raiz(c, t, C["s17.a"], PA, 0, COR, None)
    raiz(c, t, C["s17.b"], PA, 20, COR, None)
    p = ep(t, C["s17.c"], 0.6)
    if p > 0:
        E.chave(c, PA.x(0), PA.x(20), PA.oy + 70, ENT, p, 22, 5)
        E.foco(c, t, C["s17.c"] + 0.3, 0.4, lambda a: E.pilula(c, "meio: 10", PA.x(10), PA.oy + 150, 40, "g", fundo=ENT, a=a))
    regua(c, t, C["s17.c"] + 0.3, PA, 10)
    vertice(c, t, C["s17.f"], PA, 10, 200, ("10", "200"), abaixo=False)
    guia(c, t, C["s17.f"] + 0.3, PA, 10, 200, "y", SAI)
    E.foco(c, t, C["s17"], 0.5, lambda a: E.formula(c, "A(x) = x(40 − 2x)", XE, 200, 66, "g", TINTA, a))
    fml(c, t, C["s17.a"], "x = 0", XE, 310, 60, ENT)
    fml(c, t, C["s17.b"], "40 − 2x = 0  →  x = 20", XE, 410, 60, ENT)
    fml(c, t, C["s17.c"], "meio: f{0 + 20}{2} = 10", XE, 530, 60, ENT)
    E.frase(c, t, C["s17.d"], [("lados:", "i", 58), ("10", "g", 70, ENT), ("m", "g", 62, ENT)], XE, 660)
    E.frase(c, t, C["s17.e"], [("frente:", "i", 58), ("40", "g", 62), ("−", "g", 62), ("20", "g", 62), ("=", "g", 62), ("20", "g", 70), ("m", "g", 62)], XE, 760)
    E.foco(c, t, C["s17.f"], 0.6, lambda a: (M.rrect(c, XE - 20, 810, 700, 150, 44, CERTO, a),
                                             E.formula(c, "A = 10 · 20 = 200 m^2", XE + 330, 910, 66, "g", BR, a, "center")))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s18.a", [("chame", "i", 70), ("de", "i", 70), ("x", "g", 80, ENT), ("o", "i", 70), ("que", "i", 70), ("varia", "g", 72)]),
                 ("s18.b", [("monte", "g", 72), ("a", "i", 70), ("função", "g", 72, COR), ("com", "i", 70), ("a", "i", 70), ("história", "i", 70)]),
                 ("s18.c", [("ache", "i", 70), ("o", "i", 70), ("vértice", "g", 72, VERT)]),
                 ("s18.d", [("responda", "g", 72), ("o", "i", 70), ("que", "i", 70), ("foi", "i", 70), ("perguntado", "g", 72, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 390 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 52, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 60) / 2, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s19"] + 1.0, [("o", "i", 90), ("caminho", "g", 100, COR), ("de", "i", 90), ("volta", "g", 100, COR)], XE, 420)
    E.frase(c, t, C["s19.a"], [("raízes", "g", 64), ("+", "g", 64, COR), ("1", "g", 64), ("ponto", "i", 60)], XE, 570)
    E.frase(c, t, C["s19.b"], [("→", "g", 64, COR), ("a", "i", 60), ("lei", "g", 64), ("da", "i", 60), ("parábola", "i", 60)], XE, 670)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, show=b_show, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
