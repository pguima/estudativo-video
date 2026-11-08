"""Visual — Estudativo · MAT-FUN-027: praticando função racional simples (quatro situações). Fecha a trilha Funções.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita, texto à esquerda; par (x, y) com o x índigo e o y preto (par(); com decimal, "(180; 0,1)").
Como na MAT-FUN-015 e 024: cada situação abre com a esfera numerada, e o relógio de pausa fica à direita.
Como na MAT-FUN-025: hipérbole índigo e o produto x · y como retângulo da origem até o ponto (ret_xy()). Como na MAT-FUN-026:
custo em preto, assíntota tracejada com a pílula "assíntota", dinheiro com ponto de milhar.
Nesta aula: tabelas x | y com a coluna "x · y" que aparece na resposta (tabela_xy()): produto igual em verde, diferente em vermelho.
Na situação 3, o eixo x se afasta (zoom só no x) até 190 para caber (180; 0,1), colado no eixo.
Tempos: sem voz gravada, tudo sai dos marcadores {a}, {b}... Dentro de uma frase longa, quando() acha a palavra no texto do
cenas.py e interpola entre os dois marcadores vizinhos (vale para a voz provisória e para a voz real).
Peças locais: quando(), eixos(), par(), fsub(), caixa_f(), caixa_par(), num_situacao(), pergunta(), tabela_xy(), ret_xy(), plano_x(),
assintota(), relogio_3h()."""
import functools
import math
import re
import runpy
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada · y / saída
CUS = TINTA  # custo
ARQUIVO_FINAL = "estudativo_MAT-FUN-027_praticando_funcao_racional_simples.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"
VERT = "#F2B705"
PAPEL = "#F4F3EF"
AMARELO = "#FFD500"

T1 = ((2, 180), (3, 120), (4, 90), (5, 72))
TA = ((2, 30), (3, 20), (5, 12), (6, 10))
TB = ((1, 30), (2, 15), (3, 10), (4, 6))
P3 = ((2, 9), (3, 6), (6, 3))
h18 = lambda x: 18 / x
cm = lambda x: 10 + 4000 / x
assert all(x * y == 360 for x, y in T1) and 360 / 6 == 60
assert all(x * y == 60 for x, y in TA) and [x * y for x, y in TB] == [30, 30, 30, 24]
assert all(x * y == 18 for x, y in P3) and 18 / 9 == 2 and abs(18 / 180 - 0.1) < 1e-12
assert 4000 / 200 == 20 and cm(200) == 30 and 4000 / (15 - 10) == 800 and cm(800) == 15

PL = (1080, 190, 700, 700)
P4 = E.Plano(*PL, -50, 1080, -5, 65)
M4 = ([200, 400, 600, 800, 1000], [10, 20, 30, 40, 50, 60])


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- tempo de uma palavra pelos marcadores ----------------
_TXT = {s["id"]: s["text"] for s in runpy.run_path(str(Path(__file__).with_name("cenas.py")))["SCENES"]}


def _norm(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


@functools.lru_cache(None)
def _sint(sid):
    """posição provisória (0,36 s por palavra + pausas) de cada palavra e de cada marcador da cena"""
    lt, ws, cues = 0.3, [], {}
    for piece in re.findall(r"\{[^}]+\}|\[p=[\d.]+\]|\S+", _TXT[sid]):
        if piece.startswith("{"):
            cues[piece[1:-1]] = lt
        elif piece.startswith("[p="):
            lt += float(piece[3:-1])
        else:
            ws.append((_norm(piece), lt))
            lt += 0.36
    return tuple(ws), tuple(sorted(cues.items())), lt + 0.4


@functools.lru_cache(None)
def _pos(sid, frase, n):
    ws, _, _ = _sint(sid)
    alvo = [_norm(w) for w in frase.split()]
    k = 0
    for i in range(len(ws)):
        if [w for w, _ in ws[i:i + len(alvo)]] == alvo:
            k += 1
            if k == n:
                return ws[i][1]
    raise KeyError((sid, frase, n))


def quando(C, sid, frase, n=1):
    """instante da n-ésima vez que `frase` é dita na cena: interpolado entre os marcadores vizinhos"""
    ts = _pos(sid, frase, n)
    _, cues, fim = _sint(sid)
    anc = sorted([(0.0, C[sid])] + [(v, C[f"{sid}.{k}"]) for k, v in cues] + [(fim, C[sid + ".end"])])
    for (s0, r0), (s1, r1) in zip(anc, anc[1:]):
        if s0 <= ts <= s1:
            return r0 if s1 <= s0 else lerp(r0, r1, (ts - s0) / (s1 - s0))
    return anc[-1][1]


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, "g", a=0)


def mil(v):
    s = f"{abs(int(round(v))):,}".replace(",", ".")
    return ("−" if v < 0 else "") + s


def eixos(c, t, P, tx, ty=None, tg=None, marcas=None, size=38, rot=True, rx=None, ry=None, fmt=E._num, nx="x", ny="y"):
    """plano em etapas (o da MAT-FUN-001): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty; nx, ny = nomes dos eixos"""
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    mx, my = marcas
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, nx, x + w + 20, P.oy + 66, 62, "i", ENT, a))
        for i, v in enumerate(mx):
            if v == 0:
                continue
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                rot and (rx is None or v in rx) and centro(c, fmt(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, ny, P.ox + 22, y - 18, 62, "i", SAI, a))
        for i, v in enumerate(my):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                rot and (ry is None or v in ry) and E.escreve(c, fmt(v), P.ox - 20 - E.larg(fmt(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)),
                sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto"""
    cx_, cy_ = cores or (ENT, SAI)
    sep = "; " if "," in str(xv) + str(yv) else ", "  # com decimal, o par separa com ponto e vírgula: (0,5; 24)
    partes = (("(", TINTA if not cores else cx_), (xv, cx_), (sep, TINTA if not cores else cx_), (yv, cy_), (")", TINTA if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    if c is None or a <= 0:
        return w
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align))


def anel(c, t, t0, X, Y, cor=None, d=0.9):
    p = prog(t, t0, d)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def marca_ponto(c, t, t0, X, Y, cor, r=26):
    q = ease_back(prog(t, t0, 0.5))
    if q > 0:
        c.drawCircle(X, Y, r * q, M.paint(cor, 0.22))
        c.drawCircle(X, Y, r * q, M.paint(cor, 1.0, stroke=6))
    anel(c, t, t0, X, Y, cor)


def fsub(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """E.formula com índice no começo: "x_v = f{−b}{2a}" escreve x com o v pequeno embaixo"""
    if not s.startswith("x_"):
        return E.formula(c, s, x, y, size, estilo, cor, a, align)
    sub, rest = s[2], s[3:]
    wx, ws, wr = E.larg("x", estilo, size), E.larg(sub, estilo, size * 0.55), larg_f(rest, size)
    w = wx + ws + size * 0.06 + wr
    if a <= 0 or c is None:
        return w
    x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
    E.escreve(c, "x", x0, y, size, estilo, cor or TINTA, a)
    E.escreve(c, sub, x0 + wx + size * 0.02, y + size * 0.2, size * 0.55, estilo, cor or TINTA, a)
    E.formula(c, rest, x0 + wx + ws + size * 0.06, y, size, estilo, cor or TINTA, a)
    return w


def fml(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fsub(c, s, x, y, size, "g", cor, a, align))


def caixa_f(c, s, x, y, size, fundo, a, align="left"):
    """fórmula branca numa caixa cheia (resultado)"""
    w = fsub(None, s, 0, 0, size, a=0)
    x0 = x - w / 2 if align == "center" else x
    M.rrect(c, x0 - 40, y - size * 1.0, w + 80, size * 1.45, 40, fundo, a)
    fsub(c, s, x0, y, size, "g", BR, a)


def caixa_par(c, xv, yv, X, Y, size, a, align="left"):
    """par com fundo de papel (legível sobre a grade e a curva)"""
    w = par(None, xv, yv, 0, 0, size, 0)
    x0 = X - w / 2 if align == "center" else X - w if align == "right" else X
    M.rrect(c, x0 - 10, Y - size * 0.95, w + 20, size * 1.3, 12, PAPEL, 0.92 * a)
    par(c, xv, yv, x0, Y, size, a)


def raiz(c, t, t0, P_, xv, rot=None, size=40, lado=1, off=40):
    """raiz: círculo índigo no eixo x, com o par (x, 0) acima do eixo"""
    if t < t0:
        return
    marca_ponto(c, t, t0, P_.x(xv), P_.oy, ENT, 20)
    if rot:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, rot, "0", P_.x(xv) + (off if lado > 0 else -off), P_.oy - 32, size, a,
                                                          "left" if lado > 0 else "right"))


def vertice(c, t, t0, P_, xv, yv, rot=None, size=42, abaixo=True, dx=0):
    """o vértice: esfera amarela com anel, e o par embaixo (ou em cima)"""
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        X, Y = P_(xv, yv)
        c.drawCircle(X, Y, 19 * k, M.paint(VERT))
        c.drawCircle(X, Y, 19 * k, M.paint(TINTA, 1.0, stroke=4))
        anel(c, t, t0, X, Y, VERT)
        if rot:
            E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, rot[0], rot[1], X + dx, Y + (78 if abaixo else -36), size, a, "center"))


def eixo_sim(c, t, t0, P_, xv, cor=TINTA, a=1.0):
    p = ep(t, t0, 0.8)
    if p > 0 and a > 0:
        x, y, w, h_ = P_.caixa
        X = P_.x(xv)
        M.line(c, X, y + h_ + 10, X, lerp(y + h_ + 10, y - 20, p), cor, a, 5, dash=[18, 12])


def faixa_imagem(c, t, t0, P_, y0, para_cima=True, cor=SAI, a=1.0):
    """imagem como faixa sobre o eixo y: fechada em y0 (bolinha cheia) e indo até a borda com seta"""
    p = ease_io(prog(t, t0, 0.9))
    if p <= 0 or a <= 0:
        return
    x, y, w, h_ = P_.caixa
    Y0 = P_.y(y0)
    Yf = y - 30 if para_cima else y + h_ + 30
    Y1 = lerp(Y0, Yf, p)
    M.line(c, P_.ox, Y0, P_.ox, Y1, cor, 0.3 * a, 16)
    M.arrow(c, P_.ox + 28, Y0, P_.ox + 28, Y1, cor, a, 7, 22, 1.0)
    c.drawCircle(P_.ox + 28, Y0, 13, M.paint(cor, a))


def faixa_x(c, t, t0, P_, x0, x1, cor=CERTO):
    """intervalo aberto ]x0, x1[ sobre o eixo x: faixa que cresce e bolinhas abertas nas pontas"""
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    X0, X1 = P_.x(x0), P_.x(x1)
    M.line(c, X0, P_.oy, lerp(X0, X1, p), P_.oy, cor, 0.85, 14)
    for X in (X0, X1):
        c.drawCircle(X, P_.oy, 15, M.paint(BR, p))
        c.drawCircle(X, P_.oy, 15, M.paint(cor, p, stroke=6))


def guia_h(c, t, t0, P_, xv, yv, a=1.0):
    """tracejado do ponto até o eixo y"""
    p = ep(t, t0, 0.5)
    if p > 0 and a > 0:
        M.line(c, P_.x(xv), P_.y(yv), P_.ox, P_.y(yv), TINTA, a, 4, dash=E.TRACO, progress=p)



def num_situacao(c, t, t0, n, x=XE, y=200, titulo=None):
    """esfera com o número da situação e o título ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 46, y - 26, 46, a=a), centro(c, str(n), x + 46, y - 4, 56, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, titulo or [("situação", "i", 72), (str(n), "g", 72, COR)], x + 120, y)


def pergunta(c, t, t0, n, partes, y, x=XE, size=60):
    E.frase(c, t, t0, [(f"{n})", "g", size, COR)] + [(w, e, size, *k) for w, e, *k in partes], x, y)


def tabela_xy(c, t, x0, y0, cab, linhas, tc, wc=190, hl=88, size=56, prod=False, tp=None):
    """tabela em pé x | y (| x · y): linhas = [(sx, sy, t0, sp, tp, cor_p)]; a terceira coluna entra em tp (traço) e em cada tp da linha"""
    nc = 3 if prod else 2
    a = ep(t, tc, 0.5)
    cores = (ENT, SAI, COR)
    if a > 0:
        for j, s in enumerate(cab[:2]):
            centro(c, s, x0 + wc * j + wc / 2, y0 - 26, 50, "g", cores[j], a)
        M.line(c, x0, y0, x0 + 2 * wc, y0, TINTA, a, 4)
        M.line(c, x0 + wc, y0, x0 + wc, y0 + hl * len(linhas) + 10, TINTA, a, 4)
    if prod and tp is not None:
        q = ep(t, tp, 0.5)
        if q > 0:
            centro(c, "x · y", x0 + wc * 2.5, y0 - 26, 50, "g", COR, q)
            M.line(c, x0 + 2 * wc, y0, x0 + 3 * wc, y0, TINTA, q, 4)
            M.line(c, x0 + 2 * wc, y0, x0 + 2 * wc, y0 + hl * len(linhas) + 10, TINTA, q, 4)
    for i, ln in enumerate(linhas):
        sx, sy, t0 = ln[:3]
        ry = y0 + 10 + hl * i
        E.foco(c, t, t0, 0.4, lambda q, sx=sx, sy=sy, ry=ry: (centro(c, sx, x0 + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ENT, q),
                                                             centro(c, sy, x0 + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", SAI, q)), sobe=6)
        if prod and len(ln) > 3:
            sp, tq, cor = ln[3:]
            E.foco(c, t, tq, 0.4, lambda q, sp=sp, ry=ry, cor=cor: centro(c, sp, x0 + wc * 2.5, ry + hl / 2 + size * 0.36, size, "g", cor, q), sobe=6)


def ret_xy(c, t, t0, P, xv, yv, cor=COR, rot=None, a=1.0, size=40):
    """retângulo da origem até (xv, yv): a área é x · y"""
    p = ease_io(prog(t, t0, 0.6))
    if p <= 0 or a <= 0:
        return
    X, Y = P(xv, yv)
    r = skia.Rect.MakeLTRB(P.ox, lerp(P.oy, Y, p), X, P.oy)
    c.drawRect(r, M.paint(cor, 0.14 * a))
    c.drawRect(r, M.paint(cor, 0.8 * a, stroke=4))
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda q: E.formula(c, rot, (P.ox + X) / 2, Y + 20 + size, size, "g", cor, q * a, "center"))


def pt(c, t, t0, P, xv, yv, cor=COR, r=14):
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        X, Y = P(xv, yv)
        c.drawCircle(X, Y, r * k, M.paint(cor))
        c.drawCircle(X, Y, r * k, M.paint(BR, 1.0, stroke=3))


def rot_par(c, t, t0, P, xv, yv, sx, sy, size=40, dx=24, dy=-24, align="left"):
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, sx, sy, P.x(xv) + dx, P.y(yv) + dy, size, a, align))


def plano_x(c, t, t0, z, size=34):
    """plano de x, y ≥ 0 com zoom só no x: z = 0 vai até 13 (números de 2 em 2), z = 1 vai até 195 (números de 40 em 40);
    o y fica de 0 a 13. A troca das marcas do x é um esmaecer cruzado"""
    m = lerp(13.5, 195, ease_io(z))
    P = E.Plano(*PL, -m * 0.06, m, -0.8, 13.5)
    if t < t0:
        return P
    x, y, w, h = P.caixa
    q = ep(t, t0, 0.8)
    for v in range(1, 14):
        Y = P.y(v)
        M.line(c, x, Y, x + w, Y, FIO, q, 2)
        M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, q, 4)
        if v % 2 == 0:
            E.escreve(c, str(v), P.ox - 20 - E.larg(str(v), "b", size), Y + size * 0.36, size, "b", TINTA2, q)
    for passo, rot, alfa in ((1, 2, 1 - z), (20, 40, z)):
        if alfa <= 0.01:
            continue
        for v in range(passo, int(P.xmax) + 1, passo):
            X = P.x(v)
            M.line(c, X, y, X, y + h, FIO, q * alfa, 2)
            M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, q * alfa, 4)
            if v % rot == 0:
                centro(c, str(v), X, P.oy + 14 + size, size, "b", TINTA2, q * alfa)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, t0, 0.7))
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (E.escreve(c, "x", x + w + 20, P.oy + 66, 62, "i", ENT, a),
                                          E.escreve(c, "y", P.ox + 22, y - 18, 62, "i", SAI, a)))
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, "0", P.ox - 16 - E.larg("0", "b", size), P.oy + 14 + size, size, "b", TINTA2, a))
    return P


def assintota(c, t, t0, P, yv, rot=True, cor=TINTA2):
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    x, y, w, h = P.caixa
    X0 = P.x(0)
    M.line(c, X0, P.y(yv), lerp(X0, x + w, p), P.y(yv), cor, 1.0, 5, dash=[18, 12])
    if rot:
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: E.pilula(c, "assíntota", x + w - 110, P.y(yv) + 48, 38, "g", fundo=cor, a=a))


def relogio_3h(c, cx, cy, r, a, ang=1.0):
    """relógio às três horas: ponteiro grande no 12, pequeno no 3 e o quarto de volta entre eles"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR, a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=8))
    for i in range(12):
        th = math.radians(i * 30)
        M.line(c, cx + (r - 26) * math.sin(th), cy - (r - 26) * math.cos(th), cx + (r - 10) * math.sin(th), cy - (r - 10) * math.cos(th), TINTA, a, 5)
    if ang > 0:
        E.arco(c, cx, cy, r * 0.42, -90, 90 * ang, COR, 9)
    M.line(c, cx, cy, cx, cy - r * 0.78, TINTA, a, 10)
    M.line(c, cx, cy, cx + r * 0.55, cy, TINTA, a, 14)
    c.drawCircle(cx, cy, 14, M.paint(COR, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 220, COR), ("situações", "i", 110)], XE, 400)
    E.frase(c, t, C["s01.a"] + 1.4, ps("para fechar a trilha de funções", "i", 66, TINTA2), XE, 520, passo=0.12)
    for i in range(4):
        E.foco(c, t, C["s01.a"] + 0.5 + 0.2 * i, 0.4, lambda a, i=i: (E.bola(c, 1150 + 170 * i, 340, 62, a=a),
                                                                      centro(c, str(i + 1), 1150 + 170 * i, 366, 72, "g", BR, a)), blur=0)
    E.relogio(c, t, C["s01.b"], cx=1400, cy=640, r=110)
    E.frase(c, t, C["s01.b"] + 0.4, [("pause", "g", 80, COR), ("e", "i", 80), ("resolva", "g", 80)], XE, 700)
    E.frase(c, t, C["s01.b"] + 1.2, ps("antes de ver a resposta", "i", 70), XE, 800, passo=0.12)
    E.frase(c, t, quando(C, "s01", "Errar"), [("errar", "i", 64, TINTA2), ("aqui", "i", 64, TINTA2), ("ensina", "g", 64, CERTO)], XE, 940)


# ---------------- o que vai usar ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], [("você", "i", 80), ("vai", "i", 80), ("usar", "g", 80, COR)], XE, 200)
    itens = (("s02.a", lambda a, x, y: (E.formula(c, "y = f{k}{x}:", x, y, 66, "g", COR, a),
                                        E.escreve(c, "x · y = k sempre", x + larg_f("y = f{k}{x}:", 66) + 30, y, 62, "g", TINTA, a))),
             ("s02.b", lambda a, x, y: (E.escreve(c, "um ponto dá o k:", x, y, 62, "i", TINTA, a),
                                        E.escreve(c, "k = x · y", x + E.larg("um ponto dá o k:", "i", 62) + 30, y, 66, "g", COR, a))),
             ("s02.c", lambda a, x, y: (E.escreve(c, "custo médio:", x, y, 62, "i", TINTA, a),
                                        E.escreve(c, "perto do custo por peça, sem chegar", x + E.larg("custo médio:", "i", 62) + 30, y, 58, "g", CUS, a))))
    for i, (k, fn) in enumerate(itens):
        y = 400 + i * 190
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 20, 40, a=a), centro(c, str(i + 1), XE + 40, y, 48, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, XE + 110, y))
    E.foco(c, t, quando(C, "s02", "Se alguma"), 0.5, lambda a: E.pilula(c, "travou? procure a aula no canal", W / 2, 960, 46, "g", fundo=TINTA2, a=a))


# ---------------- situação 1: o churrasco ----------------
def linhas_t1(C, prod=False):
    ks = ("s03.b", "s03.c", "s03.d", "s03.e")
    tq = ("s05.a", "s05.b", "s05.c", "s05.d")
    if not prod:
        return [(str(x), str(y), C[k]) for (x, y), k in zip(T1, ks)]
    return [(str(x), str(y), C["s05"] - 3, "360", C[q], CERTO) for (x, y), q in zip(T1, tq)]


def b_questao1(c, t, C, b):
    num_situacao(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.a"] + 1.0, ps("a conta do churrasco, dividida igual", "i", 60, TINTA2), XE, 320, passo=0.1)
    tabela_xy(c, t, 1150, 330, ("pessoas", "R$ cada"), linhas_t1(C), C["s03.b"] - 0.3, wc=260, hl=100, size=62)
    pergunta(c, t, C["s03.f"], 1, [("qual", "i"), ("é", "i"), ("a", "i"), ("lei?", "g", COR)], 560)
    pergunta(c, t, quando(C, "s03", "E quanto cada"), 2, [("com", "i"), ("6", "g", ENT), ("pessoas,", "i"), ("quanto", "i"), ("cada?", "g")], 670)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=640, cy=820, r=68)


def b_resposta1(c, t, C, b):
    tabela_xy(c, t, XE, 330, ("pessoas", "R$ cada"), linhas_t1(C, True), C["s05"] - 3, wc=220, hl=100, size=62, prod=True, tp=C["s05"] + 0.6)
    E.frase(c, t, C["s05"] + 0.3, [("multiplique", "g", 60, COR), ("cada", "i", 58), ("linha", "i", 58)], XE, 190)
    E.foco(c, t, C["s05.e"], 0.6, lambda a: caixa_f(c, "k = 360", 1180, 380, 80, COR, a))
    E.frase(c, t, C["s05.e"] + 0.4, [("é", "i", 56), ("a", "i", 56), ("conta", "g", 60), ("inteira", "g", 60)], 1180, 500)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"], 0.6, lambda a: (M.rrect(c, 1140, 570, 560, 220, 46, COR, a),
                                             E.formula(c, "y = f{360}{x}", 1420, 715, 96, "g", BR, a, "center")))
    fml(c, t, C["s06.b"], "f{360}{6} = R$ 60", 1160, 920, 72, CERTO)


# ---------------- situação 2: qual tabela ----------------
TXA, TXB = XE, 1060


def linhas_ab(C, tab, frases, sid, prod=None):
    out = []
    for i, ((x, y), fr_) in enumerate(zip(tab, frases)):
        t0 = quando(C, sid, fr_)
        if prod is None:
            out.append((str(x), str(y), t0))
        else:
            tq, cor = prod[i]
            out.append((str(x), str(y), t0, str(x * y), tq, cor))
    return out


FA = ("xis dois, ípsilon trinta", "xis três, ípsilon vinte", "xis cinco, ípsilon doze", "xis seis, ípsilon dez")
FB = ("xis um, ípsilon trinta", "xis dois, ípsilon quinze", "xis três, ípsilon dez", "xis quatro, ípsilon seis")


def tabelas_ab(c, t, C, resp=False):
    t0 = C["s09"] - 3 if resp else None
    la = linhas_ab(C, TA, FA, "s07")
    lb = linhas_ab(C, TB, FB, "s07")
    if resp:
        pa = [(C["s09.a"], CERTO), (quando(C, "s09", "Três vezes vinte"), CERTO), (quando(C, "s09", "Cinco vezes doze"), CERTO),
              (quando(C, "s09", "Seis vezes dez"), CERTO)]
        pb = [(C["s10.a"], CERTO), (quando(C, "s10", "dois vezes quinze"), CERTO), (quando(C, "s10", "e três vezes dez"), CERTO), (C["s10.c"], ERRADO)]
        la = [(a_, b_, t0, str(x * y), tq, cor) for (a_, b_, _), (x, y), (tq, cor) in zip(la, TA, pa)]
        lb = [(a_, b_, t0, str(x * y), tq, cor) for (a_, b_, _), (x, y), (tq, cor) in zip(lb, TB, pb)]
    ta = t0 if resp else C["s07.b"]
    tb = t0 if resp else C["s07.c"]
    E.foco(c, t, ta, 0.4, lambda a: E.escreve(c, "tabela A", TXA, 300, 60, "g", TINTA, a))
    E.foco(c, t, tb, 0.4, lambda a: E.escreve(c, "tabela B", TXB, 300, 60, "g", TINTA, a))
    tabela_xy(c, t, TXA, 420, ("x", "y"), la, ta, wc=180, hl=88, size=56, prod=resp, tp=C["s09.a"] - 0.4 if resp else None)
    tabela_xy(c, t, TXB, 420, ("x", "y"), lb, tb, wc=180, hl=88, size=56, prod=resp, tp=C["s10.a"] - 0.4 if resp else None)


def b_questao2(c, t, C, b):
    num_situacao(c, t, C["s07.a"], 2)
    E.frase(c, t, C["s07.a"] + 1.0, [("nas", "i", 56, TINTA2), ("duas,", "i", 56, TINTA2), ("o", "i", 56, TINTA2), ("y", "g", 60, SAI), ("desce", "g", 60)],
            XE + 560, 200)
    tabelas_ab(c, t, C)
    E.frase(c, t, C["s07.d"], [("qual", "i", 60), ("é", "i", 60), ("do", "i", 60), ("tipo", "i", 60)], XE, 900)
    E.foco(c, t, C["s07.d"] + 0.8, 0.4, lambda a: E.formula(c, "f{k}{x}?", XE + 470, 900, 66, "g", COR, a))
    if t >= C["s08"]:
        E.relogio(c, t, C["s08.a"], cx=1000, cy=830, r=64)


def b_resposta2(c, t, C, b):
    tabelas_ab(c, t, C, True)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "A: k = 60", TXA + 270, 840, 52, "g", fundo=CERTO, a=a))
    if t >= C["s10.c"]:
        anel(c, t, C["s10.c"], TXB + 180 * 2.5, 420 + 10 + 88 * 3 + 44, ERRADO)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "B: não é", TXB + 270, 840, 52, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.pilula(c, "o erro: conferir só 2 ou 3 linhas. confira todas", W / 2, 960, 46, "g", fundo=TINTA, a=a))


# ---------------- situação 3: o gráfico ----------------
def b_questao3(c, t, C, b):
    P = plano_x(c, t, C["s11"], 0.0)
    for (xv, yv), k in zip(P3, "bcd"):
        pt(c, t, C[f"s11.{k}"], P, xv, yv)
        rot_par(c, t, C[f"s11.{k}"], P, xv, yv, str(xv), str(yv), 40)
    E.curva(c, t, C["s11.a"] + 0.4, P, h18, 1.4, 13.5, d=1.4, cor=COR, largura=6)
    num_situacao(c, t, C["s11.a"], 3)
    E.frase(c, t, C["s11.a"] + 1.0, ps("uma hipérbole passa por", "i", 58, TINTA2), XE, 320, passo=0.1)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: par(c, "2", "9", XE, 420, 62, a))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: par(c, "3", "6", XE + 230, 420, 62, a))
    E.foco(c, t, C["s11.d"], 0.4, lambda a: par(c, "6", "3", XE + 460, 420, 62, a))
    E.foco(c, t, C["s11.e"], 0.4, lambda a: (E.escreve(c, "1)", XE, 580, 60, "g", COR, a), E.escreve(c, "é do tipo", XE + 90, 580, 60, "i", TINTA, a),
                                             E.formula(c, "f{k}{x}?", XE + 90 + E.larg("é do tipo", "i", 60) + 24, 580, 62, "g", COR, a)))
    E.foco(c, t, C["s11.f"], 0.4, lambda a: (E.escreve(c, "2)", XE, 700, 60, "g", COR, a), E.escreve(c, "y em x = 9?", XE + 90, 700, 60, "g", TINTA, a)))
    E.frase(c, t, C["s11.g"], [("3)", "g", 60, COR), ("x", "g", 64, ENT), ("cresce", "g", 60), ("sem", "i", 60), ("parar:", "i", 60), ("e", "i", 60), ("o", "i", 60),
                               ("y?", "g", 64, SAI)], XE, 810)
    if t >= C["s12"]:
        E.relogio(c, t, C["s12.a"], cx=1600, cy=330, r=100)


def b_resposta3(c, t, C, b):
    z = ease_io(prog(t, C["s14.b"] - 0.2, 1.6))
    P = plano_x(c, t, C["s13"] - 3, z)
    E.curva(c, t, C["s13"] - 3, P, h18, 1.4, P.xmax, d=0.05, cor=COR, largura=6)
    for (xv, yv), k in zip(P3, "abc"):
        ret_xy(c, t, C[f"s13.{k}"], P, xv, yv, COR, "18" if z < 0.05 else None, a=(1 - ep(t, C["s13.d"], 0.5)) * (1 - z))
        pt(c, t, C["s13"] - 3, P, xv, yv)
        if z < 0.05:
            rot_par(c, t, C["s13"] - 3, P, xv, yv, str(xv), str(yv), 38)
    pt(c, t, C["s13.e"] + 0.3, P, 9, 2, CERTO)
    if z < 0.05:
        rot_par(c, t, C["s13.e"] + 0.3, P, 9, 2, "9", "2", 38)
    if t >= C["s14.b"] + 1.4:
        pt(c, t, C["s14.b"] + 1.4, P, 180, 0.1, CERTO)
        rot_par(c, t, C["s14.b"] + 1.4, P, 180, 0.1, "180", "0,1", 38, dx=0, dy=-40, align="right")
    p = ep(t, C["s14.a"], 0.6) * (1 - z)
    if p > 0:
        M.arrow(c, P.x(4.5), P.y(4.0) - 40, P.x(12), P.y(1.5) - 40, TINTA2, p, 6, 22, p)
    q = pulso(t, C["s14.c"], 3.0)
    if q > 0:
        x, y, w, h = P.caixa
        M.line(c, P.ox, P.oy, x + w + 30, P.oy, COR, 0.25 * q, 22)

    def s13():
        fml(c, t, C["s13.a"], "2 · 9 = 18", XE, 260, 70, TINTA)
        fml(c, t, C["s13.b"], "3 · 6 = 18", XE + 400, 260, 70, TINTA)
        fml(c, t, C["s13.c"], "6 · 3 = 18", XE, 380, 70, TINTA)
        E.foco(c, t, quando(C, "s13", "Todos os produtos"), 0.4, lambda a: E.pilula(c, "todos batem", XE + 560, 360, 46, "g", fundo=CERTO, a=a))
        E.foco(c, t, C["s13.d"], 0.6, lambda a: (M.rrect(c, XE - 20, 450, 460, 220, 46, COR, a),
                                                 E.formula(c, "y = f{18}{x}", XE + 210, 600, 96, "g", BR, a, "center")))
        fml(c, t, C["s13.e"], "x = 9:  f{18}{9} = 2", XE, 820, 72, CERTO)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.foco(c, t, C["s14"], 0.4, lambda a: E.formula(c, "y = f{18}{x}", XE, 270, 76, "g", COR, a))
    E.frase(c, t, C["s14.a"], [("x", "g", 66, ENT), ("cresce:", "i", 62), ("y", "g", 66, SAI), ("cada", "i", 62), ("vez", "i", 62), ("menor", "g", 66)], XE, 430)
    fml(c, t, C["s14.b"], "x = 180:  f{18}{180} = 0,1", XE, 570, 66, TINTA)
    E.frase(c, t, C["s14.c"], [("vai", "i", 62), ("colando", "g", 66), ("no", "i", 62), ("eixo", "i", 62), ("x", "g", 66, ENT)], XE, 720)
    E.frase(c, t, C["s14.d"], [("nunca", "g", 64, ERRADO), ("chega", "i", 60), ("a", "i", 60), ("zero:", "i", 60), ("x · y", "g", 64, COR), ("=", "g", 64),
                               ("18", "g", 64, COR)], XE, 840)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], ps("atalho para eliminar alternativas", "i", 62, CLARO), XE, 200, passo=0.1)
    E.frase(c, t, C["s15.a"], [("a", "i", 72, CLARO), ("hipérbole", "g", 76, BR), ("nunca", "g", 76, AMARELO), ("toca", "i", 72, CLARO), ("os", "i", 72, CLARO),
                               ("eixos", "g", 76, BR)], XE, 330)
    # dois gráficos de alternativa: o que corta os eixos sai sem conta
    Q1 = E.plano(c, t, C["s15.b"] - 0.4, 300, 480, 420, 320, 0, 13, 0, 13, passo=13, grade=False, rotulos=False, escuro=True, size=30, d=0.5)
    E.curva(c, t, C["s15.b"], Q1, lambda x: 11 - 0.04 * x * x - 0.3 * x, 0, 13, d=0.8, cor=CLARO, largura=7)
    if t >= C["s15.b"] + 0.9:
        for xv, yv in ((0, 11), (12.66, 0)):
            c.drawCircle(Q1.x(xv), Q1.y(yv), 18, M.paint(ERRADO, 1.0, stroke=6))
    E.foco(c, t, C["s15.b"] + 1.2, 0.4, lambda a: E.pilula(c, "corta o eixo: não é", 510, 880, 40, "g", fundo=ERRADO, a=a))
    Q2 = E.plano(c, t, C["s15.c"] - 0.4, 1200, 480, 420, 320, 0, 13, 0, 13, passo=13, grade=False, rotulos=False, escuro=True, size=30, d=0.5)
    E.curva(c, t, C["s15.c"], Q2, h18, 1.4, 13, d=0.8, cor=CLARO, largura=7)
    E.foco(c, t, C["s15.d"], 0.4, lambda a: E.pilula(c, "não toca: multiplique", 1410, 880, 40, "g", fundo=COR, a=a))
    E.foco(c, t, quando(C, "s15", "Funciona porque"), 0.4, lambda a: E.formula(c, "no eixo: 0 · y = 0 ≠ k", W / 2, 1000, 50, "g", AMARELO, a, "center"))


# ---------------- situação 4: o curso online ----------------
def b_questao4(c, t, C, b):
    num_situacao(c, t, C["s16.a"], 4, titulo=[("última", "i", 72), ("situação", "g", 72, COR)])
    E.frase(c, t, C["s16.a"] + 1.0, ps("um curso online", "i", 60, TINTA2), XE, 310, passo=0.1)
    E.frase(c, t, C["s16.b"], [("R$", "g", 68, CUS), ("4.000", "g", 68, CUS), ("por", "i", 62), ("mês", "i", 62), ("(plataforma)", "i", 52, TINTA2)], XE, 420)
    E.frase(c, t, C["s16.c"], [("+", "g", 68, COR), ("R$", "g", 68, CUS), ("10", "g", 68, CUS), ("por", "i", 62), ("aluno", "i", 62)], XE, 520)
    pergunta(c, t, C["s16.d"], 1, [("custo", "i"), ("médio", "g"), ("com", "i"), ("200", "g", ENT), ("alunos?", "i")], 680)
    pergunta(c, t, quando(C, "s16", "Com quantos alunos"), 2, [("quantos", "i"), ("alunos", "i"), ("para", "i"), ("R$", "g", CUS), ("15?", "g", CUS)], 790)
    pergunta(c, t, quando(C, "s16", "E ele pode"), 3, [("pode", "i"), ("chegar", "i"), ("a", "i"), ("R$", "g", CUS), ("10?", "g", CUS)], 900)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=460, r=180)


def b_resposta4(c, t, C, b):
    eixos(c, t, P4, C["s18"], tg=C["s18"], marcas=M4, size=32, fmt=mil)
    E.curva(c, t, C["s18.a"] + 0.4, P4, cm, 70, 1080, d=1.4, cor=CUS)
    E.ponto(c, t, C["s18.c"], P4, 200, 30, cor=CUS, r=14)
    E.foco(c, t, C["s18.c"] + 0.3, 0.4, lambda a: caixa_par(c, "200", "30", P4.x(200) + 22, P4.y(30) - 26, 38, a))
    p = ep(t, C["s19.a"], 0.6)
    if p > 0:
        M.line(c, P4.x(0), P4.y(15), lerp(P4.x(0), P4.x(1060), p), P4.y(15), COR, 1.0, 4, dash=[12, 10])
    E.ponto(c, t, C["s19.b"], P4, 800, 15, cor=CERTO, r=15)
    E.foco(c, t, C["s19.b"] + 0.3, 0.4, lambda a: caixa_par(c, "800", "15", P4.x(800), P4.y(15) - 34, 38, a, "center"))
    assintota(c, t, C["s19.e"], P4, 10, cor=TINTA2)

    def s18():
        E.foco(c, t, C["s18.a"], 0.6, lambda a: (M.rrect(c, XE - 20, 160, 780, 220, 46, COR, a),
                                                 E.formula(c, "médio = 10 + f{4.000}{x}", XE + 370, 310, 84, "g", BR, a, "center")))
        fml(c, t, C["s18.b"], "200 alunos:  f{4.000}{200} = 20", XE, 540, 66, TINTA)
        fml(c, t, C["s18.c"], "20 + 10 = R$ 30 por aluno", XE, 720, 70, CERTO)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19"], 0.4, lambda a: E.formula(c, "médio = 10 + f{4.000}{x}", XE, 260, 66, "g", COR, a))
    E.frase(c, t, C["s19"] + 0.4, [("alvo", "i", 60), ("R$", "g", 64, CUS), ("15:", "g", 64, CUS)], XE, 400)
    fml(c, t, C["s19.a"], "15 − 10 = 5", XE + 300, 400, 66, TINTA)
    fml(c, t, C["s19.b"], "f{4.000}{5} = 800 alunos", XE, 540, 70, CERTO)
    E.frase(c, t, C["s19.c"], [("R$", "g", 66, CUS), ("10:", "g", 66, CUS), ("nunca", "g", 70, ERRADO)], XE, 690)
    fml(c, t, C["s19.d"], "f{4.000}{x} ≠ 0", XE + 480, 690, 60, ERRADO)
    E.frase(c, t, C["s19.e"], [("só", "i", 60), ("se", "i", 60), ("aproxima", "g", 64), ("de", "i", 60), ("R$", "g", 64, CUS), ("10", "g", 64, CUS)], XE, 840)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("multiplique", "g", 76, COR), ("as", "i", 72), ("coordenadas,", "i", 72), ("todas", "g", 76)]),
                 ("s20.b", [("x", "g", 76, ENT), ("cresce:", "i", 72), ("k/x", "g", 76, COR), ("encolhe", "g", 76), ("sem", "i", 72), ("chegar", "i", 72), ("a", "i", 72),
                            ("0", "g", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 450 + i * 240
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"], [("trilha", "i", 60, TINTA2), ("de", "i", 60, TINTA2), ("funções:", "i", 60, TINTA2), ("completa", "g", 64, CERTO)], XE, 200)
    E.frase(c, t, C["s21.b"] - 0.8, [("próxima", "i", 84), ("aula", "i", 84)], XE, 330)
    E.frase(c, t, C["s21.b"], [("ângulos", "g", 150, COR)], XE, 490)
    E.frase(c, t, C["s21.c"], [("3", "g", 64), ("horas:", "i", 60), ("um", "i", 60), ("quarto", "g", 64), ("de", "i", 60), ("volta,", "i", 60), ("90°", "g", 64, COR)],
            XE, 630)
    E.frase(c, t, C["s21.d"], ps("agudo, reto, obtuso ou raso", "i", 56, TINTA2), XE, 740, passo=0.12)
    a = ep(t, C["s21.b"] + 0.3, 0.5)
    relogio_3h(c, 1450, 700, 150, a, ease_io(prog(t, C["s21.c"], 0.8)))
    E.foco(c, t, C["s21.c"] + 0.6, 0.4, lambda q: E.escreve(c, "90°", 1492, 628, 40, "g", COR, q))
    E.foco(c, t, C["s21.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.e"] + 0.2, 0.4))
    E.frase(c, t, C["s21.f"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
