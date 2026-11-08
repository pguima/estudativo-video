"""Visual — Estudativo · MAT-FUN-028: sistema de inequações.

Linguagem visual da trilha Funções (MAT-FUN-001): entrada / x em índigo (eixo x índigo), saída / y em preto; plano à direita e
texto à esquerda; erro em vermelho. Como na MAT-FUN-022: parábola de a > 0 índigo, região abaixo do eixo pintada de vermelho;
a solução vai na reta na cor da matéria (bolinha cheia = a ponta entra, aberta = fica de fora, seta = segue para sempre).
Trilho dos passos no alto (o da MAT-FUN-020 e 022).
Nesta aula: a chave do sistema (E.sistema) no alto, à esquerda; as respostas empilhadas em retas com a mesma escala (E.reta) e as
guias tracejadas em pé nos números que importam; a parte comum ganha uma faixa em pé da cor da matéria, que desce até a
reta-resposta; a união errada fica em vermelho. Os símbolos ∪ e ∩ são desenhados à mão (a fonte não tem).
Peças locais: trilho(), retas(), faixa(), guias(), solucao(), formula_u(), simbolo_conj(), pal() e as da trilha."""
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
CA, CB, CC = COR, TINTA2, TINTA
POS, NEG = CERTO, ERRADO
ARQUIVO_FINAL = "estudativo_MAT-FUN-028_sistema_de_inequacoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sistema", "metodo", "outro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERT = "#F2B705"
ESCURO = "#0B0B16"

f = lambda x: x * x - 5 * x + 6
g = lambda x: x * x - 6 * x + 5
q = lambda x: x * x - x - 6
assert f(2) == 0 and f(3) == 0 and all(f(x / 10) < 0 for x in range(21, 30)) and all(x / 10 - 1 > 0 for x in range(21, 30))
assert 36 - 20 == 16 and g(1) == 0 and g(5) == 0 and (6 - 4) / 2 == 1 and (6 + 4) / 2 == 5 and 6 / 2 == 3
assert 10 - 1 == 9 and 100 - 50 + 6 == 56 and f(10) == 56
assert 1 + 24 == 25 and (1 + 5) / 2 == 3 and (1 - 5) / 2 == -2 and q(3) == 0 and q(-2) == 0 and 3 - (-1) == 4
assert [n for n in range(-5, 6) if q(n) <= 0 and 3 - n < 4] == [0, 1, 2, 3]

RX0, RX1 = 600, 1680
RY = (640, 790, 950)  # reta 1, reta 2, reta-resposta
PL = (1330, 150, 420, 330)
PF = E.Plano(*PL, -0.5, 4.5, -0.8, 3)

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




# ---------------- peças da aula ----------------
PASSOS = ("cada uma", "empilhe", "o pintado em todas")


def trilho(c, t, t0, ativos, a=1.0):
    """os passos no alto (o da MAT-FUN-020 e 022); ativos = instantes em que cada passo vira o da vez"""
    a = ep(t, t0, 0.5) * a
    if a <= 0:
        return
    x0, dx, y = XE + 30, 380, 100
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
        E.bola(c, X, y, 28 * kk, cor, a)
        centro(c, str(i + 1), X, y + 14, 40, "g", BR, a)
        E.escreve(c, nome, X + 44, y + 13, 38, "g" if on else "i", cor, a)


def retas(c, t, ts, vmin, vmax, marcas, rotulos=None, x0=RX0, x1=RX1, ys=RY, escuro=False):
    """as retas empilhadas, com a mesma escala; ts[i] = instante de cada reta (None = não mostra); rotulos = texto à esquerda de cada uma"""
    vx = None
    for i, (ti, y) in enumerate(zip(ts, ys)):
        if ti is None:
            continue
        vx = E.reta(c, t, ti, x0, x1, y, vmin, vmax, marcas, E._num, escuro=escuro, size=40)
        if rotulos and rotulos[i]:
            E.foco(c, t, ti + 0.2, 0.4, lambda a, i=i, y=y: formula_u(c, rotulos[i], XE, y + 14, 46, "g", BR if escuro else TINTA2, a))
    return lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)


def guias(c, t, t0, vx, vals, y0=RY[0] - 50, y1=RY[2] + 30, cor=TINTA2, alfa=0.45):
    for i, v in enumerate(vals):
        p = ep(t, t0 + 0.12 * i, 0.6)
        if p > 0:
            M.line(c, vx(v), y0, vx(v), lerp(y0, y1, p), cor, alfa, 3, dash=[10, 10])


def faixa(c, t, t0, vx, a_, b_, y0=RY[0] - 50, y1=RY[1] + 40, cor=None, alfa=0.14, t1=None, desce=None):
    """a parte comum: faixa em pé de a_ até b_ (valores) cobrindo as retas; desce = instante em que ela se estende até a reta-resposta"""
    q_ = ep(t, t0, 0.5) * (1 - ep(t, t1, 0.4) if t1 is not None else 1)
    if q_ <= 0:
        return
    yb = y1 if desce is None else lerp(y1, RY[2] + 40, ease_io(prog(t, desce, 0.6)))
    M.rrect(c, vx(a_) - 6, y0, vx(b_) - vx(a_) + 12, yb - y0, 16, cor or COR, alfa * q_)


def solucao(c, t, t0, vx, y, ini, fim, fi=False, ff=False, cor=None, x0=RX0, x1=RX1, d=0.6, fundo=None):
    """trecho da solução na reta, com seta quando segue para sempre (a mesma da MAT-FUN-022); trechos finitos usam E.intervalo"""
    if ini is not None and fim is not None:
        E.intervalo(c, t, t0, vx, y, ini, fim, fi, ff, cor=cor, d=d)
        return
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


def simbolo_conj(c, x, y, size, cor, a, cap=False):
    """∪ (ou ∩ com cap=True) desenhado à mão, com a base em y"""
    wu = size * 0.62
    l, r_, top, bot = x + size * 0.1, x + wu - size * 0.1, y - size * 0.62, y - size * 0.02
    u = skia.Path()
    if not cap:
        u.moveTo(l, top); u.lineTo(l, bot - (r_ - l) / 2)
        u.arcTo(skia.Rect.MakeLTRB(l, bot - (r_ - l), r_, bot), 180, -180, False)
        u.lineTo(r_, top)
    else:
        u.moveTo(l, bot); u.lineTo(l, top + (r_ - l) / 2)
        u.arcTo(skia.Rect.MakeLTRB(l, top, r_, top + (r_ - l)), 180, 180, False)
        u.lineTo(r_, bot)
    c.drawPath(u, M.paint(cor or TINTA, a, stroke=size * 0.11, cap_round=True))
    return wu


def formula_u(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """E.formula que desenha o ∪ e o ∩ à mão; devolve a largura"""
    partes = re.split(r"([∪∩])", s)
    wu = size * 0.62
    w = sum(wu if p in "∪∩" and p else larg_f(p, size) for p in partes if p)
    if c is None or a <= 0:
        return w
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p in partes:
        if not p:
            continue
        if p in ("∪", "∩"):
            simbolo_conj(c, xx, y, size, cor, a, p == "∩")
            xx += wu
        else:
            E.formula(c, p, xx, y, size, estilo, cor, a)
            xx += larg_f(p, size)
    return w


def conta(c, t, t0, s, y, size=60, cor=TINTA, x=XE):
    E.foco(c, t, t0, 0.5, lambda a: formula_u(c, s, x, y, size, "g", cor, a))


def sistema_em(c, t, t0, linhas, x=XE + 20, y=230, size=60, tl=None, realces=()):
    """a chave do sistema; realces = [(linha, t_ini, t_fim)] pinta a linha da vez"""
    for i, t1, t2 in realces:
        a_ = ep(t, t1, 0.3) * (1 - ep(t, t2, 0.3))
        if a_ > 0:
            w = larg_f(linhas[i], size)
            M.rrect(c, x + size * 0.3 - 14, y + i * size * 1.45 - size * 0.95, w + 28, size * 1.25, 14, COR, 0.15 * a_)
    E.sistema(c, t, t0, linhas, x, y, size, tl=tl)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01.a"], [("duas", "g", 80, COR), ("condições", "i", 74), ("ao", "i", 74), ("mesmo", "i", 74), ("tempo", "g", 80)], XE, 240)
        sistema_em(c, t, C["s01.b"], ["x − 1 > 0", "x^2 − 5x + 6 < 0"], XE + 30, 420, 92, tl=[C["s01.b"], C["s01.c"]])
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.pilula(c, "resolver e juntar tudo: erra", XE + 420, 760, 50, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s01.e"] - 0.8, ps("quem manda é a palavra", "i", 60, TINTA2), XE, 900, passo=0.08)
        k = ease_back(prog(t, C["s01.e"], 0.6))
        if k > 0:
            E.bola(c, 1480, 520, 230 * k)
            centro(c, "e", 1480, 520 + 110 * k, 320 * k, "i", BR)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("sistema", "g", 100, COR), ("de", "i", 90)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.8, [("inequações", "g", 100, COR)], XE, 580)
        E.frase(c, t, pal("s02", "empilhando", 0, C["s02.a"] + 4.0), [("empilhando", "g", 76), ("as", "i", 72), ("respostas", "i", 72)], XE, 740)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 76), ("precisa", "i", 76), ("de", "i", 76)], XE, 360)
    E.frase(c, t, C["s03.a"], [("3", "g", 220, COR), ("coisas", "i", 100)], XE, 600)
    x, w = 780, 1000
    for t0, y, h_ in ((C["s03.b"], 140, 250), (C["s03.c"], 420, 220), (C["s03.d"], 670, 330)):
        p = ep(t, t0, 0.5)
        E.caixa_pontilhada(c, x, y, w, h_, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("1º", "g", 58, COR), ("grau:", "g", 58), ("o", "i", 52), ("mesmo", "i", 52), ("nos", "i", 52), ("dois", "i", 52), ("lados", "i", 52)], x + 40, 220)
    E.foco(c, t, pal("s03", "vire", 0, C["s03.b"] + 3.0), 0.4, lambda a: (E.formula(c, "÷ (−1):", x + 40, 330, 54, "g", TINTA, a),
                                                                         E.escreve(c, "vira o sinal", x + 280, 328, 52, "g", ERRADO, a)))
    E.frase(c, t, C["s03.c"] + 0.1, [("2º", "g", 58, COR), ("grau:", "g", 58), ("raízes,", "i", 52), ("boca", "i", 52), ("e", "i", 52), ("o", "i", 52), ("pedaço", "g", 56)], x + 40, 500)
    E.foco(c, t, C["s03.c"] + 0.8, 0.4, lambda a: E.formula(c, "x^2 − 5x + 6 < 0  →  ]2, 3[", x + 40, 590, 52, "g", TINTA2, a))
    E.frase(c, t, C["s03.d"] + 0.1, [("interseção:", "g", 58), ("o", "i", 52), ("pintado", "g", 56, COR), ("em", "i", 52), ("todas", "i", 52)], x + 40, 750)
    if t >= C["s03.d"] + 0.6:
        vx = lambda v: x + 120 + (v - 0) / 7 * (w - 260)
        for i, (yy, a_, b_) in enumerate(((830, 1, 5), (900, 3, 7))):
            E.reta(c, t, C["s03.d"] + 0.6 + 0.2 * i, x + 120, x + w - 140, yy, 0, 7, [], size=30)
            E.intervalo(c, t, C["s03.d"] + 0.8 + 0.2 * i, vx, yy, a_, b_, True, True)
        faixa(c, t, C["s03.d"] + 1.6, vx, 3, 5, 800, 930)
    q_ = ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(360, 960, q_), ep(t, C["s03.b"], 0.4))


# ---------------- o que é ----------------
def b_sistema(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("sistema", "g", 96, COR), ("de", "i", 86), ("inequações", "g", 96, COR)], XE, 240)
    sistema_em(c, t, C["s04.a"] + 1.0, ["x − 1 > 0", "x^2 − 5x + 6 < 0"], XE + 30, 430, 80)
    E.frase(c, t, C["s04.b"], [("valem", "i", 66), ("ao", "i", 66), ("mesmo", "i", 66), ("tempo", "g", 72)], XE, 720)
    E.frase(c, t, pal("s04", "chave", 0, C["s04.b"] + 2.6), ps("unidas pela chave", "i", 54, TINTA2), XE, 810)
    k = ease_back(prog(t, C["s04.c"], 0.6))
    if k > 0:
        E.bola(c, 1450, 430, 190 * k)
        centro(c, "e", 1450, 430 + 90 * k, 260 * k, "i", BR)
    E.foco(c, t, C["s04.d"], 0.5, lambda a: (E.escreve(c, "=", 1300, 820, 90, "g", TINTA, a), simbolo_conj(c, 1390, 830, 120, COR, a, True),
                                             E.escreve(c, "interseção", 1480, 815, 64, "g", COR, a)))


# ---------------- método ----------------
SIS1 = ["x − 1 > 0", "x^2 − 5x + 6 < 0"]


def b_metodo(c, t, C, b):
    trilho(c, t, C["s05.a"], (C["s05.b"], C["s07.a"], C["s07.d"]))
    sistema_em(c, t, C["s05"] - 0.2, SIS1, XE + 20, 230, 56,
               realces=((0, C["s05.c"], C["s06"]), (1, C["s06.a"], C["s07"])))
    vx = retas(c, t, (C["s05.e"], C["s06.c"], C["s08.c"] - 0.3), -1, 5, [-1, 0, 1, 2, 3, 4, 5], ("x > 1", "]2, 3[", None))
    # linha de conta da vez
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("3", "g", 90, COR), ("passos", "i", 66)], XE + 760, 260)
            conta(c, t, C["s05.c"], "x − 1 > 0", 470, 64)
            conta(c, t, C["s05.d"], "→  x > 1", 470, 64, COR, XE + 360)
            E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: E.escreve(c, "+1 dos dois lados", XE + 700, 465, 42, "i", TINTA2, a))
            conta(c, t, C["s05.e"], "]1, +∞[", 550, 56, COR)
        E.saida(c, t, C["s06"] - 0.1, s05)
    solucao(c, t, C["s05.e"] + 0.4, vx, RY[0], 1, None)
    if C["s06"] <= t < C["s07"]:
        def s06():
            conta(c, t, C["s06.a"], "x^2 − 5x + 6 < 0", 470, 60)
            E.frase(c, t, C["s06.b"], [("raízes", "i", 52), ("2", "g", 60, ENT), ("e", "i", 52), ("3,", "g", 60, ENT), ("boca", "i", 52), ("para", "i", 52), ("cima", "g", 56)], XE, 550)
        E.saida(c, t, C["s07"] - 0.1, s06)
    # a parábola, ao lado
    def graf():
        eixos(c, t, PF, C["s06.b"], tg=None, marcas=([1, 2, 3, 4], []), size=30)
        E.curva(c, t, C["s06.b"] + 0.3, PF, f, 0.5, 4.2, d=0.8, cor=COR, largura=6)
        E.area(c, t, C["s06.c"], PF, f, 2, 3, cor=NEG, alfa=0.45, d=0.5)
    E.saida(c, t, C["s07"] - 0.1, graf)
    solucao(c, t, C["s06.c"] + 0.4, vx, RY[1], 2, 3)
    if t < C["s07"]:
        return
    guias(c, t, C["s07.a"] + 0.3, vx, (1, 2, 3))
    for i, k in enumerate(("s07.b", "s07.c")):
        p = ep(t, C[k], 0.3) * (1 - ep(t, C[k] + 1.6, 0.4))
        if p > 0:
            M.rrect(c, RX0 - 60, RY[i] - 50, RX1 - RX0 + 120, 110, 30, COR, 0.1 * p)
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("2.", "g", 62, COR), ("empilhe,", "g", 62), ("números", "i", 56), ("alinhados", "i", 56)], XE, 480)
        E.frase(c, t, C["s07.d"], [("3.", "g", 62, COR), ("o", "i", 56), ("pintado", "g", 62, COR), ("em", "i", 56), ("ambas", "g", 62)], XE, 560)
        return
    faixa(c, t, C["s08.a"], vx, 2, 3, desce=C["s08.c"] - 0.3)
    for v in (2, 3):
        if t >= C["s08.b"]:
            anel(c, t, C["s08.b"], vx(v), RY[1], ERRADO)
    if t < C["s09"]:
        E.frase(c, t, C["s08.b"], [("2", "g", 60, ERRADO), ("e", "i", 56), ("3:", "g", 60, ERRADO), ("abertas", "g", 60, ERRADO), ("embaixo,", "i", 56), ("ficam", "i", 56), ("de", "i", 56),
                                   ("fora", "g", 60)], XE, 560)
    solucao(c, t, C["s08.c"], vx, RY[2], 2, 3)
    E.foco(c, t, C["s08.c"] + 0.4, 0.5, lambda a: (M.rrect(c, XE - 20, RY[2] - 56, 300, 90, 30, COR, a),
                                                   E.formula(c, "]2, 3[", XE + 130, RY[2] + 10, 50, "g", BR, a, "center")))
    if t < C["s09"]:
        E.frase(c, t, C["s08"], [("3.", "g", 62, COR), ("o", "i", 56), ("pintado", "g", 62, COR), ("em", "i", 56), ("ambas", "g", 62)], XE, 480)
        return
    E.frase(c, t, C["s09.a"], [("a", "i", 60), ("1ª", "g", 64), ("não", "g", 64, COR), ("tirou", "i", 60), ("nada", "g", 64)], XE, 480)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "entre 2 e 3: já é > 1", XE + 300, 545, 40, "g", fundo=CERTO, a=a))


# ---------------- outro sistema ----------------
SIS2 = ["x^2 − 6x + 5 ≤ 0", "2x − 6 > 0"]


def b_outro(c, t, C, b):
    sistema_em(c, t, C["s10.a"], SIS2, XE + 20, 200, 56, tl=[C["s10.a"], C["s10.b"]],
               realces=((0, C["s10.c"] - 0.4, C["s11"]), (1, C["s11"], C["s11.c"])))
    vx = retas(c, t, (C["s10.d"], C["s11.b"], C["s11.c"]), 0, 6, [0, 1, 2, 3, 4, 5, 6], ("[1, 5]", "x > 3", None))
    if t < C["s11"]:
        conta(c, t, C["s10.c"], "Δ = 36 − 20 = 16", 420, 58, TINTA2)
        E.foco(c, t, pal("s10", "raízes", 0, C["s10.c"] + 2.0), 0.4, lambda a: E.formula(c, "x = 1  e  x = 5", XE, 510, 58, "g", ENT, a))
        E.foco(c, t, pal("s10", "boca", 0, C["s10.d"] - 1.6), 0.4, lambda a: E.escreve(c, "boca para cima, pedaço de baixo, com tracinho", XE + 560, 505, 40, "i", TINTA2, a))
    else:
        def s11():
            conta(c, t, C["s11.a"], "2x > 6", 420, 60)
            conta(c, t, C["s11.b"], "→  x > 3", 420, 60, COR, XE + 260)
        E.saida(c, t, C["s11.c"] - 0.1, s11)
    solucao(c, t, C["s10.d"] + 0.3, vx, RY[0], 1, 5, True, True)
    solucao(c, t, C["s11.b"] + 0.3, vx, RY[1], 3, None)
    if t < C["s11.c"]:
        return
    guias(c, t, C["s11.c"], vx, (3, 5))
    faixa(c, t, C["s11.c"] + 0.2, vx, 3, 5, desce=C["s11.f"] - 0.3)
    E.frase(c, t, C["s11.c"], [("pintado", "g", 60, COR), ("em", "i", 56), ("ambas:", "i", 56), ("do", "i", 56), ("3", "g", 62), ("ao", "i", 56), ("5", "g", 62)], XE, 420)
    if t >= C["s11.d"]:
        anel(c, t, C["s11.d"], vx(3), RY[1], ERRADO)
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "3: a 2ª não pega", XE, 510, 46, "g", ERRADO, a))
    if t >= C["s11.e"]:
        anel(c, t, C["s11.e"], vx(5), RY[0], CERTO)
    E.foco(c, t, C["s11.e"], 0.4, lambda a: E.escreve(c, "5: está em ambas", XE + 420, 510, 46, "g", CERTO, a))
    solucao(c, t, C["s11.f"], vx, RY[2], 3, 5, False, True)
    E.foco(c, t, C["s11.f"] + 0.4, 0.5, lambda a: (M.rrect(c, XE - 20, RY[2] - 56, 300, 90, 30, COR, a),
                                                   E.formula(c, "]3, 5]", XE + 130, RY[2] + 10, 50, "g", BR, a, "center")))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    sistema_em(c, t, C["s12"] - 0.2, SIS1, XE + 20, 200, 56)
    E.frase(c, t, C["s12.a"], [("o", "i", 60), ("erro:", "i", 60), ("juntar", "g", 66, ERRADO), ("em", "i", 60), ("vez", "i", 60), ("de", "i", 60), ("cruzar", "g", 66)], XE, 420)
    ys = (640, 760, 900)
    vx = retas(c, t, (C["s12"] - 0.2, C["s12"] - 0.2, C["s12.b"]), -1, 11, [0, 1, 2, 3, 5, 10], ("x > 1", "]2, 3[", None), ys=ys)
    solucao(c, t, C["s12"], vx, ys[0], 1, None)
    solucao(c, t, C["s12"] + 0.2, vx, ys[1], 2, 3)
    solucao(c, t, C["s12.b"] + 0.3, vx, ys[2], 1, None, cor=ERRADO)
    E.foco(c, t, C["s12.b"] + 0.6, 0.4, lambda a: (M.rrect(c, XE - 20, ys[2] - 50, 300, 84, 30, ERRADO, a),
                                                   formula_u(c, "]1, +∞[", XE + 130, ys[2] + 12, 46, "g", BR, a, "center")))
    kk = ease_back(prog(t, C["s12.c"], 0.5))
    if kk > 0:
        M.line(c, vx(10), ys[0] - 40, vx(10), ys[2] + 30, TINTA, 0.5 * min(1, kk), 3, dash=[10, 10])
        c.drawCircle(vx(10), ys[2], 22 * kk, M.paint(TINTA))
        E.pilula(c, "x = 10", vx(10), ys[0] - 80, 36, "g", fundo=TINTA, a=min(1, kk))
    E.foco(c, t, pal("s12", "nove", 0, C["s12.c"] + 1.4), 0.4, lambda a: E.formula(c, "10 − 1 = 9 > 0", 1240, 420, 46, "g", CERTO, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.formula(c, "100 − 50 + 6 = 56", 1240, 510, 46, "g", ERRADO, a))
    if t >= C["s12.e"]:
        c.drawCircle(vx(10), ys[1], 22, M.paint(ERRADO, ep(t, C["s12.e"], 0.3), stroke=7))
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.pilula(c, "o 10 falha na 2ª", vx(10) - 200, ys[1] - 60, 34, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s12.f"], 0.6, lambda a: (M.rrect(c, XE - 20, 470, 1030, 90, 40, CERTO, a),
                                             E.escreve(c, "sistema é e: interseção, nunca união", XE + 20, 530, 50, "g", BR, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 62, CLARO), XE, 190)
        E.frase(c, t, C["s13.a"], ps("cada uma dá um pedaço só?", "i", 56, CLARO), XE, 290, passo=0.08)
        E.frase(c, t, C["s13.b"], [("do", "i", 66, CLARO), ("maior", "g", 74, AMARELO), ("dos", "i", 66, CLARO), ("começos", "g", 72, BR), ("ao", "i", 66, CLARO), ("menor", "g", 74, AMARELO),
                                   ("dos", "i", 66, CLARO), ("fins", "g", 72, BR)], XE, 410)
        E.foco(c, t, C["s13.b"] + 1.6, 0.4, lambda a: (formula_u(c, "[1, 5]", XE, 590, 64, "g", BR, a), formula_u(c, "]3, +∞[", XE, 710, 64, "g", BR, a)))
        cols = ((1100, "começos", ("1", "3"), C["s13.c"], 1), (1500, "fins", ("5", "+∞"), C["s13.d"], 0))
        for x, nome, vals, tk, idx in cols:
            E.foco(c, t, C["s13.b"] + 1.8, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 480, 50, "i", CLARO, a))
            for i, v in enumerate(vals):
                y = 590 + i * 120
                E.foco(c, t, C["s13.b"] + 2.0 + 0.2 * i, 0.4, lambda a, x=x, y=y, v=v: E.formula(c, v, x, y, 64, "g", BR, a, "center"))
            kk = ease_back(prog(t, tk, 0.5))
            if kk > 0:
                y = 590 + idx * 120 - 22
                c.drawCircle(x, y, 62 * kk, M.paint(AMARELO, 1.0, stroke=7))
        E.foco(c, t, C["s13.d"] + 1.2, 0.6, lambda a: (M.rrect(c, XE - 20, 800, 760, 140, 44, AMARELO, a),
                                                       E.formula(c, "do 3 ao 5: ]3, 5]", XE + 360, 895, 64, "g", ESCURO, a, "center")))
        return
    E.frase(c, t, C["s14.a"], [("passou", "i", 60, CLARO), ("de", "i", 60, CLARO), ("cada", "i", 60, CLARO), ("começo", "g", 66, AMARELO)], XE, 220)
    E.frase(c, t, C["s14.b"], [("e", "i", 60, CLARO), ("não", "i", 60, CLARO), ("chegou", "i", 60, CLARO), ("a", "i", 60, CLARO), ("nenhum", "i", 60, CLARO), ("fim", "g", 66, AMARELO)], XE, 320)
    E.frase(c, t, C["s14.c"], [("não", "g", 64, ERRADO), ("compensa:", "i", 60, CLARO), ("dois", "g", 66, BR), ("pedaços", "g", 66, BR)], XE, 480)
    E.foco(c, t, C["s14.d"], 0.4, lambda a: E.formula(c, "x^2 − 9 > 0", XE, 590, 64, "g", BR, a))
    vx = retas(c, t, (None, None, C["s14.d"] + 0.4), -5, 5, [-3, 0, 3], x0=600, x1=1640, ys=(0, 0, 760), escuro=True)
    solucao(c, t, C["s14.d"] + 0.8, vx, 760, None, -3, x0=600, x1=1640, fundo="#07070F", cor=AMARELO)
    solucao(c, t, C["s14.d"] + 1.1, vx, 760, 3, None, x0=600, x1=1640, fundo="#07070F", cor=AMARELO)
    E.foco(c, t, C["s14.e"], 0.5, lambda a: E.pilula(c, "empilhe as retas", W / 2, 920, 52, "g", fundo=CERTO, a=a))


# ---------------- questão ----------------
SIS3 = ["x^2 − x − 6 ≤ 0", "3 − x < 4"]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 70, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("quantos", "i", 70), ("inteiros", "g", 76, COR), ("valem", "i", 70), ("as", "i", 70), ("duas?", "g", 76)], XE, 350)
    sistema_em(c, t, C["s15.b"], SIS3, XE + 30, 540, 96, tl=[C["s15.b"], C["s15.c"]])
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=460, r=180)


def b_resposta(c, t, C, b):
    sistema_em(c, t, C["s17"] - 0.2, SIS3, XE + 20, 200, 56, realces=((0, C["s17"], C["s18"]), (1, C["s18"], C["s18.c"])))
    vx = retas(c, t, (C["s17.d"], C["s18.b"], C["s18.c"]), -3, 4, [-3, -2, -1, 0, 1, 2, 3, 4], ("[−2, 3]", "x > −1", None))
    if t < C["s18"]:
        for i, s_ in enumerate(("a = 1", "b = −1", "c = −6")):
            E.foco(c, t, C["s17"] + 0.8 + 0.3 * i, 0.4, lambda a, s_=s_, i=i: E.formula(c, s_, XE + 620 + i * 220, 230, 44, "g", TINTA2, a))
        E.foco(c, t, pal("s17", "menos", 2, C["s17.a"] + 2.4), 0.4, lambda a: E.formula(c, "−b = 1", XE + 620, 400, 52, "g", TINTA2, a))
        conta(c, t, C["s17.a"], "Δ = 1 + 24 = 25", 400, 52, TINTA2)
        conta(c, t, C["s17.b"], "x = f{1 + 5}{2} = 3", 520, 52, ENT)
        conta(c, t, C["s17.c"], "x = f{1 − 5}{2} = −2", 520, 52, ENT, XE + 470)
    elif t < C["s18.c"]:
        def s18():
            conta(c, t, C["s18.a"], "−x < 1", 430, 60)
            conta(c, t, C["s18.b"], "x > −1", 430, 60, COR, XE + 300)
            E.foco(c, t, C["s18.b"] + 0.4, 0.4, lambda a: E.escreve(c, "× (−1): vira o sinal", XE + 620, 425, 44, "g", ERRADO, a))
        E.saida(c, t, C["s18.c"] - 0.1, s18)
    solucao(c, t, C["s17.d"] + 0.3, vx, RY[0], -2, 3, True, True)
    solucao(c, t, C["s18.b"] + 0.4, vx, RY[1], -1, None)
    if t < C["s18.c"]:
        return
    guias(c, t, C["s18.c"], vx, (-1, 3))
    faixa(c, t, C["s18.c"], vx, -1, 3, desce=C["s18.d"])
    E.frase(c, t, C["s18.c"], [("maior", "g", 58, COR), ("dos", "i", 54), ("começos:", "i", 54), ("−1", "g", 62)], XE, 420)
    E.frase(c, t, C["s18.d"], [("menor", "g", 58, COR), ("dos", "i", 54), ("fins:", "i", 54), ("3", "g", 62)], XE + 600, 420)
    solucao(c, t, C["s18.d"] + 0.4, vx, RY[2], -1, 3, False, True)
    # os inteiros
    tn = (C["s19.a"], pal("s19", "um", 0, C["s19.a"] + 0.8), pal("s19", "dois", 0, C["s19.a"] + 1.6), pal("s19", "três", 0, C["s19.a"] + 2.4))
    for n, tk in zip((0, 1, 2, 3), tn):
        kk = ease_back(prog(t, tk, 0.4))
        if kk > 0:
            c.drawCircle(vx(n), RY[2] + 66, 28 * kk, M.paint(CERTO))
            centro(c, str(n), vx(n), RY[2] + 66 + 15 * kk, 42 * kk, "g", BR)
    E.foco(c, t, C["s19.b"], 0.6, lambda a: (M.rrect(c, XE - 20, 470, 560, 110, 40, CERTO, a),
                                             E.escreve(c, "4 inteiros", XE + 30, 545, 70, "g", BR, a)))
    if t >= C["s19.c"]:
        anel(c, t, C["s19.c"], vx(-1), RY[2], ERRADO)
    E.foco(c, t, C["s19.c"], 0.4, lambda a: E.pilula(c, "−1: ponta aberta", XE + 170, RY[2], 34, "g", fundo=ERRADO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("resolva", "g", 78), ("cada", "i", 72), ("inequação", "i", 72)]),
                 ("s20.b", [("empilhe", "g", 78, COR), ("as", "i", 72), ("retas", "g", 78)]),
                 ("s20.c", [("fique", "i", 72), ("com", "i", 72), ("o", "i", 72), ("pintado", "g", 78, COR), ("em", "i", 72), ("todas", "g", 78)]))
        for i, (kk, partes) in enumerate(itens):
            y = 420 + i * 200
            E.foco(c, t, C[kk], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                          E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[kk] + 0.1, partes, 340, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s21"] + 1.0, [("praticando", "g", 96, COR)], XE, 400)
    E.frase(c, t, C["s21.a"], [("a", "i", 70), ("função", "g", 76), ("quadrática", "g", 76), ("inteira", "i", 70)], XE, 510)
    E.frase(c, t, C["s21.b"], [("raízes", "g", 60, ENT), ("e", "i", 56), ("vértice", "g", 60, VERT)], XE, 630)
    E.frase(c, t, C["s21.c"], [("máximo", "g", 60), ("e", "i", 56), ("mínimo", "g", 60), ("em", "i", 56), ("problemas", "i", 56)], XE, 730)
    E.frase(c, t, C["s21.d"], [("o", "i", 56), ("sinal", "g", 60, COR), ("da", "i", 56), ("parábola", "i", 56)], XE, 830)
    E.foco(c, t, C["s21.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.e"] + 0.2, 0.4))
    E.frase(c, t, C["s21.f"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sistema=b_sistema, metodo=b_metodo, outro=b_outro, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
