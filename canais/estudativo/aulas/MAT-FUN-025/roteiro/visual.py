"""Visual — Estudativo · MAT-FUN-025: função y = k/x, a hipérbole.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita, texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Nesta aula: a hipérbole é índigo; o produto x · y aparece como o retângulo da origem até o ponto (ret_xy()), pintado de leve:
mesma área = mesmo produto. Na tabela, o plano começa de 0 a 13 e se afasta (zoom) até 0 a 25 para caber (0,5; 24) e (24; 0,5).
O ramo negativo aparece num plano de quatro quadrantes, na mesma caixa. No atalho, palco escuro.
Tempos: sem voz gravada, tudo sai dos marcadores {a}, {b}... Dentro de uma frase longa, quando() acha a palavra no texto do
cenas.py e interpola entre os dois marcadores vizinhos (vale para a voz provisória e para a voz real).
Peças locais: quando(), par(), anel(), marca_ponto(), fsub(), caixa_f(), caixa_par(), plano_z() (plano com zoom), ret_xy(), tabela_xy()."""
import functools
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
ARQUIVO_FINAL = "estudativo_MAT-FUN-025_funcao_k_sobre_x_hiperbole.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "curva", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
VERT = "#F2B705"
PAPEL = "#F4F3EF"
AMARELO = "#FFD500"

h12 = lambda x: 12 / x
h20 = lambda x: 20 / x
reta = lambda x: 12 - x
TAB = ((1, 12), (2, 6), (3, 4), (4, 3), (6, 2), (12, 1))
assert all(x * y == 12 for x, y in TAB) and 12 / 0.5 == 24 and 12 / 24 == 0.5 and 12 / -2 == -6
assert reta(2) == 10 and reta(6) == 6 and 2 * 10 == 20 and 6 * 6 == 36 and reta(12) == 0
assert 3 * 4 == 12 and 4 * 5 == 20 and 20 / 10 == 2 and 2 * 10 == 20

PL = (1080, 190, 700, 700)


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
                rot and (rx is None or v in rx) and centro(c, E._num(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
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



def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


# ---------------- peças desta aula ----------------
def faz_P(z):
    m = lerp(13.5, 25.5, ease_io(z))
    return E.Plano(*PL, -m * 0.06, m, -m * 0.06, m)


def plano_z(c, t, t0, z, nx="x", ny="y", size=34):
    """plano de x, y ≥ 0 com zoom: z = 0 vai até 13 (marcas de 1 em 1, números de 2 em 2), z = 1 vai até 25 (marcas de 2 em 2,
    números de 4 em 4); a troca das marcas é um esmaecer cruzado"""
    P = faz_P(z)
    if t < t0:
        return P
    x, y, w, h = P.caixa
    q = ep(t, t0, 0.8)
    for passo, rot, alfa in ((1, 2, 1 - z), (2, 4, z)):
        if alfa <= 0.01:
            continue
        for v in range(passo, int(P.xmax) + 1, passo):
            X, Y = P.x(v), P.y(v)
            M.line(c, X, y, X, y + h, FIO, q * alfa, 2)
            M.line(c, x, Y, x + w, Y, FIO, q * alfa, 2)
            M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, q * alfa, 4)
            M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, q * alfa, 4)
            if v % rot == 0:
                centro(c, str(v), X, P.oy + 14 + size, size, "b", TINTA2, q * alfa)
                E.escreve(c, str(v), P.ox - 20 - E.larg(str(v), "b", size), Y + size * 0.36, size, "b", TINTA2, q * alfa)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, t0, 0.7))
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (E.escreve(c, nx, x + w + 20, P.oy + 66, 62, "i", ENT, a),
                                          E.escreve(c, ny, P.ox + 22, y - 18, 62, "i", SAI, a)))
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, "0", P.ox - 16 - E.larg("0", "b", size), P.oy + 14 + size, size, "b", TINTA2, a))
    return P


def pt(c, t, t0, P, xv, yv, cor=COR, r=14):
    """ponto que entra com um salto (sem rótulo)"""
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        X, Y = P(xv, yv)
        c.drawCircle(X, Y, r * k, M.paint(cor))
        c.drawCircle(X, Y, r * k, M.paint(BR, 1.0, stroke=3))


def ret_xy(c, t, t0, P, xv, yv, cor=COR, rot=None, a=1.0, size=40):
    """retângulo da origem até (xv, yv): a área é x · y"""
    p = ease_io(prog(t, t0, 0.6))
    if p <= 0 or a <= 0:
        return
    X, Y = P(xv, yv)
    r = skia.Rect.MakeLTRB(P.ox, lerp(P.oy, Y, p), X, P.oy)
    c.drawRect(r, M.paint(cor, 0.16 * a))
    c.drawRect(r, M.paint(cor, 0.8 * a, stroke=4))
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda q: E.formula(c, rot, (P.ox + X) / 2, Y + 20 + size, size, "g", cor, q * a, "center"))


def rot_par(c, t, t0, P, xv, yv, sx, sy, size=40, dx=24, dy=-24, align="left"):
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: caixa_par(c, sx, sy, P.x(xv) + dx, P.y(yv) + dy, size, a, align))


def tabela_xy(c, t, x0, y0, cab, linhas, tc, wc=200, hl=76, size=52):
    """tabela em pé x | y; linhas = [(sx, sy, t0)]"""
    a = ep(t, tc, 0.5)
    if a > 0:
        for j, (s, cor) in enumerate(cab):
            centro(c, s, x0 + wc * j + wc / 2, y0 - 26, 52, "g", cor, a)
        M.line(c, x0, y0, x0 + 2 * wc, y0, TINTA, a, 4)
        M.line(c, x0 + wc, y0, x0 + wc, y0 + hl * len(linhas) + 10, TINTA, a, 4)
    for i, (sx, sy, t0) in enumerate(linhas):
        ry = y0 + 10 + hl * i
        E.foco(c, t, t0, 0.4, lambda q, sx=sx, sy=sy, ry=ry: (centro(c, sx, x0 + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ENT, q),
                                                             centro(c, sy, x0 + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", SAI, q)), sobe=6)


def torneira(c, cx, cy, s, cor, a):
    """torneira simples: cano, bico e uma gota"""
    if a <= 0:
        return
    M.rrect(c, cx - 50 * s, cy - 14 * s, 90 * s, 28 * s, 10 * s, cor, a)
    M.rrect(c, cx + 22 * s, cy - 14 * s, 26 * s, 50 * s, 8 * s, cor, a)
    M.rrect(c, cx - 14 * s, cy - 40 * s, 28 * s, 26 * s, 6 * s, cor, a)
    c.drawCircle(cx + 35 * s, cy + 58 * s, 9 * s, M.paint(E.mix(cor, BR, 0.4), a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ts = quando(C, "s01", "Sai uma curva")

    def cena1():
        E.frase(c, t, C["s01"], [("mais", "i", 84), ("torneiras,", "g", 84, COR)], XE, 300)
        for i in range(3):
            E.foco(c, t, C["s01"] + 0.4 + 0.25 * i, 0.4, lambda a, i=i: torneira(c, 1240 + 180 * i, 300, 1.3, COR, a))
        E.frase(c, t, C["s01.a"], [("menos", "i", 84), ("tempo", "g", 84)], XE, 420)
        E.frase(c, t, C["s01.b"], [("não", "g", 76, ERRADO), ("é", "i", 76), ("uma", "i", 76), ("reta", "g", 76)], XE, 600)
        E.frase(c, t, ts, [("é", "i", 76), ("uma", "i", 76), ("curva", "g", 76, COR)], XE, 710)
        E.frase(c, t, C["s01.c"], [("que", "i", 70), ("nunca", "g", 70, COR), ("encosta", "i", 70), ("no", "i", 70), ("eixo", "g", 70)], XE, 850)
        Q = E.plano(c, t, C["s01.b"], 1220, 480, 520, 420, 0, 13, 0, 13, passo=13, grade=False, rotulos=False, size=30, d=0.5)
        E.saida(c, t, ts, lambda: E.curva(c, t, C["s01.b"] + 0.2, Q, reta, 0, 12, d=0.6, cor=ERRADO, largura=7, tracejada=True))
        E.curva(c, t, ts + 0.2, Q, h12, 0.93, 13, d=2.0, cor=COR, largura=9)
        p = ep(t, C["s01.c"] + 0.3, 0.5)
        if p > 0:
            M.arrow(c, Q.x(0.45), Q.y(5), Q.x(0.45), Q.y(12.5), TINTA2, p, 5, 18, p)
            M.arrow(c, Q.x(5.5), Q.y(0.5), Q.x(12.5), Q.y(0.5), TINTA2, p, 5, 18, p)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        tn = quando(C, "s02", "descobre o número")
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.2, [("desenhar", "g", 110), ("a", "i", 100), ("curva", "g", 110, COR)], XE, 460)
        E.frase(c, t, tn, [("e", "i", 90), ("o", "i", 90), ("número", "g", 100), ("que", "i", 90)], XE, 610)
        E.frase(c, t, tn + 0.8, [("nunca", "i", 90), ("muda", "g", 100, COR)], XE, 730)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"] - 0.6, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] - 0.45, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.a", "inversamente proporcionais:", lambda a, y: E.escreve(c, "o produto não muda", x + 44, y, 66, "g", COR, a)),
             ("s03.b", "o gráfico pela tabela:", lambda a, y: (E.escreve(c, "x", x + 44, y, 66, "g", ENT, a),
                                                              E.escreve(c, "→  y  →  ponto", x + 100, y, 66, "g", SAI, a))))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q_ = ease_io(prog(t, C["s03.b"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q_), ep(t, C["s03.a"], 0.4))
    E.foco(c, t, quando(C, "s03", "Se faltar"), 0.5, lambda a: E.pilula(c, "faltou? procure no canal", W / 2, 960, 46, "g", fundo=TINTA2, a=a))


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("torneiras iguais, uma caixa", "i", 66), XE, 200, passo=0.12)
        tabela_xy(c, t, XE + 40, 360, (("torneiras", ENT), ("horas", SAI)),
                  (("1", "12", C["s04.a"]), ("2", "6", C["s04.b"]), ("3", "4", C["s04.c"])), C["s04"] + 0.6, wc=280, hl=96, size=64)
        for i, k in enumerate(("s04.a", "s04.b", "s04.c")):
            for j in range(i + 1):
                E.foco(c, t, C[k] + 0.15 * j, 0.4, lambda a, i=i, j=j: torneira(c, 1150 + 150 * j, 420 + 96 * i, 0.75, COR, a))
        E.foco(c, t, C["s04.d"], 0.6, lambda a: caixa_f(c, "horas = 12 ÷ torneiras", XE + 20, 800, 70, TINTA, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("x", "g", 66, ENT), ("=", "g", 66, ENT), ("torneiras", "i", 62), ("·", "g", 62, TINTA2), ("y", "g", 66, SAI), ("=", "g", 66, SAI),
                             ("horas", "i", 62)], XE, 220)
    E.foco(c, t, C["s05.a"], 0.6, lambda a: (M.rrect(c, XE - 20, 290, 560, 260, 50, COR, a),
                                             E.formula(c, "y = f{12}{x}", XE + 260, 460, 120, "g", BR, a, "center")))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "x · y = 12", XE + 700, 460, 100, "g", COR, a))
    for i, (xv, yv) in enumerate(TAB[:3]):
        E.foco(c, t, C["s05.b"] + 0.6 + 0.4 * i, 0.4, lambda a, xv=xv, yv=yv, i=i: E.formula(c, f"{xv} · {yv} = 12", XE + 700, 580 + 80 * i, 56, "g", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.pilula(c, "inversamente proporcional", W / 2, 900, 60, "g", fundo=COR, a=a))


# ---------------- tabela ----------------
def b_tabela(c, t, C, b):
    z = ease_io(prog(t, C["s07.a"] + 0.6, 1.4))
    P = plano_z(c, t, C["s06"], z)
    linhas = [(E._num(x_), E._num(y_), C[f"s06.{k}"]) for (x_, y_), k in zip(TAB, "abcdef")]
    linhas += [("0,5", "24", C["s07.a"]), ("24", "0,5", C["s07.b"])]
    tabela_xy(c, t, XE + 60, 250, (("x", ENT), ("y", SAI)), linhas, C["s06"], wc=220, hl=78, size=54)
    E.foco(c, t, C["s06"], 0.4, lambda a: E.escreve(c, "y = 12 ÷ x", XE + 560, 330, 56, "g", COR, a))
    E.foco(c, t, C["s06"] + 0.4, 0.4, lambda a: E.escreve(c, "x > 0", XE + 560, 420, 56, "g", ENT, a))
    for (xv, yv), k in zip(TAB, "abcdef"):
        pt(c, t, C[f"s06.{k}"] + 0.2, P, xv, yv)
    E.foco(c, t, C["s07"], 0.4, lambda a: E.escreve(c, "x quebrado:", XE + 560, 560, 50, "i", TINTA2, a))
    E.foco(c, t, C["s07.a"] + 0.6, 0.4, lambda a: E.formula(c, "12 ÷ 0,5 = 24", XE + 560, 650, 50, "g", TINTA, a))
    E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.formula(c, "12 ÷ 24 = 0,5", XE + 560, 740, 50, "g", TINTA, a))
    pt(c, t, C["s07.a"] + 2.0, P, 0.5, 24)
    pt(c, t, C["s07.b"] + 0.4, P, 24, 0.5)
    if t >= C["s07.a"] + 2.0:
        rot_par(c, t, C["s07.a"] + 2.0, P, 0.5, 24, "0,5", "24", 38, dx=26, dy=14)
    if t >= C["s07.b"] + 0.4:
        rot_par(c, t, C["s07.b"] + 0.4, P, 24, 0.5, "24", "0,5", 38, dx=0, dy=-30, align="right")


# ---------------- curva ----------------
def b_curva(c, t, C, b):
    if t < C["s10"]:
        def pos():
            P = plano_z(c, t, C["s08"] - 3, 1.0)
            for xv, yv in TAB + ((0.5, 24), (24, 0.5)):
                pt(c, t, C["s08"] - 3, P, xv, yv)
            E.curva(c, t, quando(C, "s08", "ligue com"), P, h12, 0.47, 25.5, d=1.8, cor=COR)
            p = ep(t, C["s08.a"], 0.5)
            if p > 0:
                M.arrow(c, P.x(1.6), P.y(10), P.x(1.6), P.y(22), TINTA2, p, 5, 20, p)
            p = ep(t, C["s08.b"], 0.5)
            if p > 0:
                M.arrow(c, P.x(8), P.y(3.6), P.x(20), P.y(3.6), TINTA2, p, 5, 20, p)
            E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "hipérbole", P.x(13), P.y(9), 56, "g", fundo=COR, a=a))
            # os eixos acendem: a curva chega perto e não encosta
            q = pulso(t, C["s09.c"], 3.0)
            if q > 0:
                x, y, w, h = P.caixa
                M.line(c, x, P.oy, x + w + 30, P.oy, COR, 0.25 * q, 22)
                M.line(c, P.ox, y + h, P.ox, y - 30, TINTA, 0.25 * q, 22)
        E.saida(c, t, C["s10"] - 0.1, pos)

    def s08():
        E.frase(c, t, C["s08"], ps("ligue os pontos", "i", 70), XE, 240)
        E.frase(c, t, C["s08.a"], [("perto", "i", 64), ("do", "i", 64), ("eixo", "i", 64), ("y:", "g", 66, SAI), ("dispara", "g", 66)], XE, 400)
        E.frase(c, t, C["s08.b"], [("longe", "i", 64), ("dele:", "i", 64), ("quase", "i", 64), ("deitada", "g", 66)], XE, 520)
        E.frase(c, t, C["s08.c"], [("a", "i", 100), ("hipérbole", "g", 110, COR)], XE, 720)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t:
        def s09():
            E.frase(c, t, C["s09"], [("por", "i", 66), ("que", "i", 66), ("nunca", "g", 66, COR), ("toca", "i", 66), ("os", "i", 66), ("eixos?", "g", 66)], XE, 230)
            fml(c, t, C["s09.a"], "y = 0:  x · 0 = 0 ≠ 12", XE, 380, 60, TINTA)
            fml(c, t, quando(C, "s09", "Se o xis fosse"), "x = 0:  0 · y = 0 ≠ 12", XE, 490, 60, TINTA)
            E.foco(c, t, C["s09.b"], 0.5, lambda a: (E.formula(c, "f{12}{0}", XE, 650, 70, "g", ERRADO, a),
                                                     E.escreve(c, "não existe", XE + 130, 650, 62, "g", ERRADO, a)))
            E.foco(c, t, quando(C, "s09", "porque nenhum"), 0.4, lambda a: E.escreve(c, "nenhum número vezes 0 dá 12", XE, 760, 48, "i", TINTA2, a))
            E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "chega perto, mas não encosta", XE + 360, 890, 50, "g", fundo=COR, a=a))
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    # o ramo negativo, num plano de quatro quadrantes
    Q = E.plano(c, t, C["s10"], *PL, -13, 13, -13, 13, passo=2, marcas_x=[-12, -8, -4, 4, 8, 12], marcas_y=[-12, -8, -4, 4, 8, 12], size=32)
    pos_ = ep(t, C["s10.b"], 0.5)
    E.curva(c, t, C["s10"] + 0.3, Q, h12, 0.93, 13, d=0.8, cor=COR, largura=7 + 5 * pos_)
    c.saveLayerAlpha(None, int(255 * (1 - 0.65 * pos_)))
    E.curva(c, t, C["s10.a"], Q, h12, -13, -0.93, d=1.0, cor=TINTA)
    if t >= C["s10.a"] + 0.8:
        E.ponto(c, t, C["s10.a"] + 0.8, Q, -2, -6, cor=TINTA, r=14)
        rot_par(c, t, C["s10.a"] + 0.8, Q, -2, -6, "−2", "−6", 40, dx=-30, dy=14, align="right")
    c.restore()
    E.frase(c, t, C["s10"], [("com", "i", 66), ("x", "g", 70, ENT), ("negativo:", "i", 66)], XE, 260)
    E.frase(c, t, C["s10.a"], [("uma", "i", 62), ("segunda", "g", 64), ("parte,", "i", 62)], XE, 370)
    E.frase(c, t, C["s10.a"] + 1.0, [("embaixo", "i", 62), ("à", "i", 62), ("esquerda", "g", 64)], XE, 460)
    fml(c, t, quando(C, "s10", "doze dividido por menos"), "f{12}{−2} = −6", XE, 620, 76, TINTA)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.pilula(c, "problemas reais: só a parte positiva", XE + 400, 800, 44, "g", fundo=COR, a=a))


# ---------------- reconhecer ----------------
def b_reconhecer(c, t, C, b):
    P = plano_z(c, t, C["s11"], 0.0)
    E.curva(c, t, C["s11"] + 0.3, P, h12, 0.9, 13.5, d=0.9, cor=COR)
    ret_xy(c, t, C["s11.b"], P, 2, 6, COR, "12", a=1 - 0.6 * ep(t, C["s11.c"], 0.4))
    pt(c, t, C["s11.b"], P, 2, 6)
    rot_par(c, t, C["s11.b"], P, 2, 6, "2", "6", 40)
    ret_xy(c, t, C["s11.c"], P, 3, 4, TINTA, "12")
    pt(c, t, C["s11.c"], P, 3, 4, TINTA)
    rot_par(c, t, C["s11.c"], P, 3, 4, "3", "4", 40)
    E.frase(c, t, C["s11.a"], [("multiplique", "g", 64, COR), ("as", "i", 62), ("coordenadas", "i", 62)], XE, 230)
    fml(c, t, C["s11.b"] + 0.3, "2 · 6 = 12", XE, 360, 72, TINTA)
    fml(c, t, C["s11.c"] + 0.3, "3 · 4 = 12", XE + 420, 360, 72, TINTA)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "produto igual: inversa", XE + 300, 490, 52, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s11.e"], [("o", "i", 62), ("número", "i", 62), ("fixo:", "i", 62), ("k", "g", 76, COR)], XE, 640)
    E.foco(c, t, C["s11.f"], 0.6, lambda a: (M.rrect(c, XE - 20, 700, 460, 230, 46, COR, a),
                                             E.formula(c, "y = f{k}{x}", XE + 210, 850, 100, "g", BR, a, "center")))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    th = quando(C, "s13", "A hipérbole nunca")
    P = plano_z(c, t, C["s12"], 0.0)
    E.curva(c, t, C["s12.b"], P, reta, 0, 12, d=1.0, cor=TINTA)
    pt(c, t, C["s12.c"], P, 2, 10, TINTA)
    rot_par(c, t, C["s12.c"], P, 2, 10, "2", "10", 40)
    pt(c, t, C["s12.d"], P, 6, 6, TINTA)
    rot_par(c, t, C["s12.d"], P, 6, 6, "6", "6", 40)
    if t >= C["s13"]:
        ret_xy(c, t, C["s13.a"], P, 2, 10, ERRADO, "20", a=1 - 0.6 * ep(t, C["s13.b"], 0.4))
        ret_xy(c, t, C["s13.b"], P, 6, 6, ERRADO, "36")
        if t >= C["s13.d"]:
            marca_ponto(c, t, C["s13.d"], P.x(12), P.oy, ERRADO, 24)
        c.saveLayerAlpha(None, 120)
        E.curva(c, t, th, P, h12, 0.9, 13.5, d=0.9, cor=COR, tracejada=True)
        c.restore()

    def s12():
        E.frase(c, t, C["s12.a"], [("todo", "i", 64), ("gráfico", "i", 64), ("que", "i", 64), ("desce", "g", 66)], XE, 230)
        E.frase(c, t, C["s12.a"] + 1.4, [("é", "i", 64), ("inversa?", "g", 66, ERRADO)], XE, 330)
        fml(c, t, C["s12.b"], "y = 12 − x", XE, 500, 90, TINTA)
        E.frase(c, t, C["s12.c"], [("ela", "i", 60), ("desce", "g", 62)], XE, 640)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13"], 0.4, lambda a: E.formula(c, "y = 12 − x", XE, 230, 66, "g", TINTA, a))
    fml(c, t, C["s13.a"], "2 · 10 = 20", XE, 380, 72, ERRADO)
    fml(c, t, C["s13.b"], "6 · 6 = 36", XE + 450, 380, 72, ERRADO)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.pilula(c, "produtos diferentes: não é inversa", XE + 380, 510, 48, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s13.d"], [("corta", "i", 62), ("o", "i", 62), ("eixo", "i", 62), ("x", "g", 66, ENT), ("no", "i", 62), ("12", "g", 66, ERRADO)], XE, 680)
    E.frase(c, t, th, [("a", "i", 62), ("hipérbole", "g", 64, COR), ("nunca", "g", 64), ("faz", "i", 62), ("isso", "i", 62)], XE, 790)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    Q = E.plano(c, t, C["s14"], 1120, 220, 640, 640, 0, 13, 0, 13, passo=1, marcas_x=[2, 4, 6, 8, 10, 12], marcas_y=[2, 4, 6, 8, 10, 12], escuro=True)
    if t >= C["s14.b"]:
        q = ease_io(prog(t, C["s14.c"], 0.6))
        if q > 0:
            X, Y = Q(3, 4)
            r = skia.Rect.MakeLTRB(Q.ox, lerp(Q.oy, Y, q), X, Q.oy)
            c.drawRect(r, M.paint(AMARELO, 0.18))
            c.drawRect(r, M.paint(AMARELO, 0.9, stroke=4))
            E.foco(c, t, C["s14.c"] + 0.4, 0.4, lambda a: centro(c, "12", (Q.ox + X) / 2, (Q.oy + Y) / 2 + 16, 44, "g", AMARELO, a))
        E.ponto(c, t, C["s14.b"], Q, 3, 4, cor=AMARELO, r=16)
    E.curva(c, t, C["s14.d"] + 0.3, Q, h12, 0.93, 13, d=1.2, cor=CLARO)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 70, CLARO), XE, 200)
        E.frase(c, t, C["s14.a"], [("um", "g", 80, BR), ("ponto", "g", 80, AMARELO), ("basta", "i", 76, CLARO)], XE, 330)
        E.frase(c, t, C["s14.b"], [("passa", "i", 64, CLARO), ("por", "i", 64, CLARO)], XE, 470)
        E.foco(c, t, C["s14.b"] + 0.3, 0.4, lambda a: par(c, "3", "4", XE + 270, 470, 72, a, cores=(CLARO, BR)))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "k = 3 · 4 = 12", XE, 610, 80, "g", AMARELO, a))
        E.foco(c, t, C["s14.d"], 0.6, lambda a: (M.rrect(c, XE - 20, 680, 460, 230, 46, COR, a),
                                                 E.formula(c, "y = f{12}{x}", XE + 210, 830, 100, "g", BR, a, "center")))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("x", "g", 76, BR), ("·", "g", 76, BR), ("y", "g", 76, BR), ("=", "g", 76, BR), ("k", "g", 76, AMARELO), ("sempre", "i", 70, CLARO)],
            XE, 260)
    E.frase(c, t, C["s15.b"], [("não", "g", 66, ERRADO), ("compensa:", "i", 64, CLARO)], XE, 440)
    E.frase(c, t, C["s15.b"] + 0.8, ps("não sabe se é hipérbole", "i", 60, CLARO), XE, 530, passo=0.12)
    E.frase(c, t, C["s15.c"], [("multiplique", "g", 62, BR), ("vários", "i", 60, CLARO), ("pontos", "i", 60, CLARO), ("antes", "g", 62, AMARELO)], XE, 690)
    E.frase(c, t, quando(C, "s15", "Se algum produto"), ps("um produto diferente: a lei é outra", "i", 54, CLARO), XE, 800, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 70, COR), XE, 200)
    fml(c, t, C["s16.a"], "y = f{k}{x}", XE, 380, 100, TINTA)
    E.frase(c, t, C["s16.b"], [("passa", "i", 66), ("por", "i", 66)], XE + 420, 370)
    par_em(c, t, C["s16.b"] + 0.3, "4", "5", XE + 690, 370, 80)
    E.frase(c, t, C["s16.c"], [("1)", "g", 62, COR), ("a", "i", 62), ("lei?", "g", 62)], XE, 560)
    E.foco(c, t, C["s16.d"], 0.4, lambda a: (E.escreve(c, "2)", XE, 670, 62, "g", COR, a),
                                             E.escreve(c, "y em x = 10?", XE + 90, 670, 62, "g", TINTA, a)))
    E.foco(c, t, C["s16.e"], 0.4, lambda a: (E.escreve(c, "3)", XE, 780, 62, "g", COR, a), par(c, "2", "10", XE + 90, 780, 62, a),
                                             E.escreve(c, "está na curva?", XE + 90 + par(None, "2", "10", 0, 0, 62) + 24, 780, 62, "i", TINTA, a)))
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=460, r=180)


def b_resposta(c, t, C, b):
    P = plano_z(c, t, C["s18"], 0.0)
    pt(c, t, C["s18"] + 0.4, P, 4, 5)
    rot_par(c, t, C["s18"] + 0.4, P, 4, 5, "4", "5", 40)
    E.curva(c, t, C["s18.b"] + 0.3, P, h20, 1.5, 13.5, d=1.2, cor=COR)
    pt(c, t, C["s18.c"] + 0.4, P, 10, 2)
    rot_par(c, t, C["s18.c"] + 0.4, P, 10, 2, "10", "2", 40, dy=-28)
    pt(c, t, C["s18.d"], P, 2, 10, CERTO)
    rot_par(c, t, C["s18.d"], P, 2, 10, "2", "10", 40)
    fml(c, t, C["s18.a"], "k = 4 · 5 = 20", XE, 240, 76, COR)
    E.foco(c, t, C["s18.b"], 0.6, lambda a: (M.rrect(c, XE - 20, 290, 420, 210, 46, COR, a),
                                             E.formula(c, "y = f{20}{x}", XE + 190, 430, 90, "g", BR, a, "center")))
    fml(c, t, C["s18.c"], "x = 10:  f{20}{10} = 2", XE, 655, 70, TINTA)
    fml(c, t, C["s18.d"], "2 · 10 = 20", XE, 800, 72, TINTA)
    E.foco(c, t, C["s18.e"], 0.5, lambda a: E.pilula(c, "bate: está na curva", XE + 260, 920, 52, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", lambda a, y: (E.formula(c, "y = f{k}{x}:", 340, y, 80, "g", COR, a),
                                         E.escreve(c, "x · y = k sempre", 340 + larg_f("y = f{k}{x}:", 80) + 30, y, 72, "g", TINTA, a))),
                 ("s19.b", lambda a, y: (E.escreve(c, "hipérbole:", 340, y, 76, "g", COR, a),
                                         E.escreve(c, "nunca toca os eixos", 340 + E.larg("hipérbole:", "g", 76) + 30, y, 72, "i", TINTA, a))))
        for i, (k, fn) in enumerate(itens):
            y = 450 + i * 240
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, fn=fn, y=y: fn(a, y))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s20.a"], [("custo", "g", 130, COR), ("médio", "g", 130, COR)], XE, 470)
    E.frase(c, t, quando(C, "s20", "Quanto mais"), ps("mais peças, mais barata cada uma", "i", 56, TINTA2), XE, 590, passo=0.1)
    E.frase(c, t, C["s20.b"], [("e", "i", 62), ("um", "i", 62), ("valor", "g", 64), ("que", "i", 62), ("nunca", "g", 64, COR), ("alcança", "i", 62)], XE, 700)
    Q = E.plano(c, t, C["s20.a"] + 0.4, 1300, 560, 400, 280, 0, 13, 0, 13, passo=13, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, C["s20.a"] + 0.7, Q, lambda x: 3 + 12 / x, 1.2, 13, d=1.0, cor=COR, largura=9)
    E.curva(c, t, C["s20.b"], Q, lambda x: 3, 0, 13, d=0.6, cor=TINTA2, largura=4, tracejada=True)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, tabela=b_tabela, curva=b_curva, reconhecer=b_reconhecer, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
