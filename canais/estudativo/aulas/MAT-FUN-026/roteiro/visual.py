"""Visual — Estudativo · MAT-FUN-026: custo médio e outras funções racionais.

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita, texto à esquerda; erro em vermelho. Como na MAT-FUN-014: custo em preto (CUS), dinheiro com ponto
de milhar ("2.000"). Como na MAT-FUN-005: domínio na reta numérica de sempre (RX0 a RX1), trecho índigo de E.intervalo com o furo
aberto, e a resposta "]−∞, 2[ ou ]2, +∞[" em índigo. Como na MAT-FUN-025: a hipérbole y = k/x.
Nesta aula: a curva do custo médio é preta; a assíntota é a reta tracejada y = 30 com a pílula "assíntota"; o pedaço do aluguel
(2.000/x) é a faixa índigo entre a curva e a assíntota, e a barra empilhada mostra 50 = 30 de material + 20 de aluguel.
Tempos: sem voz gravada, tudo sai dos marcadores {a}, {b}... Dentro de uma frase longa, quando() acha a palavra no texto do
cenas.py e interpola entre os dois marcadores vizinhos (vale para a voz provisória e para a voz real).
Peças locais: quando(), eixos(), fsub(), caixa_f(), caixa_par(), plano_cm(), assintota(), barra_peca(), dominio()."""
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
CUS = TINTA  # custo
ARQUIVO_FINAL = "estudativo_MAT-FUN-026_custo_medio_e_funcoes_racionais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("medio", "limite", "dominio", "atalho", "questao", "fim"))
BR = "#FFFFFF"
VERT = "#F2B705"
PAPEL = "#F4F3EF"
AMARELO = "#FFD500"

custo = lambda x: 2000 + 30 * x
cm = lambda x: 30 + 2000 / x
assert custo(100) == 5000 and 5000 / 100 == 50 and (10 + 6) / 2 == 8 == 10 / 2 + 6 / 2
assert cm(1) == 2030 and cm(100) == 50 and cm(1000) == 32 and abs(cm(10000) - 30.2) < 1e-9
assert 2000 / (40 - 30) == 200 and cm(200) == 40 and (-1 + 1) / (-1 - 2) == 0
assert 600 / 300 + 2 == 4 and 600 / (3 - 2) == 600 and (5 - 5) / (5 + 3) == 0

PL = (1080, 190, 700, 700)
PC = E.Plano(*PL, -50, 1080, -8, 108)
MC = ([200, 400, 600, 800, 1000], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
RX0, RX1 = 300, 1620  # a reta de sempre (MAT-FUN-005)


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
    partes = (("(", TINTA if not cores else cx_), (xv, cx_), (", ", TINTA if not cores else cx_), (yv, cy_), (")", TINTA if not cores else cy_))
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
def plano_cm(c, t, t0, P=PC, marcas=MC, size=32):
    eixos(c, t, P, t0, tg=t0, marcas=marcas, size=size, fmt=mil)


def assintota(c, t, t0, P, yv, rot=True, cor=TINTA2, x0=None):
    """reta tracejada y = yv que cresce da esquerda para a direita, com a pílula "assíntota" na ponta"""
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    x, y, w, h = P.caixa
    X0 = P.x(0) if x0 is None else x0
    M.line(c, X0, P.y(yv), lerp(X0, x + w, p), P.y(yv), cor, 1.0, 5, dash=[18, 12])
    if rot:
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: E.pilula(c, "assíntota", x + w - 110, P.y(yv) + 48, 38, "g", fundo=cor, a=a))


def barra_peca(c, t, t0, t1, x, y, w, a=1.0):
    """barra em pé do custo de uma peça: 30 de material (preto) + 20 de aluguel (índigo) = 50"""
    k = 9.0  # pixels por real
    p = ease_io(prog(t, t0, 0.6)) * a
    if p <= 0:
        return
    hm = 30 * k * p
    c.drawRect(skia.Rect.MakeXYWH(x, y - hm, w, hm), M.paint(CUS, a))
    E.foco(c, t, t0 + 0.4, 0.4, lambda q: (centro(c, "30", x + w / 2, y - 30 * k / 2 + 18, 50, "g", BR, q * a),
                                          E.escreve(c, "material", x + w + 24, y - 30 * k / 2 + 16, 44, "i", CUS, q * a)))
    q = ease_io(prog(t, t1, 0.6)) * a
    if q > 0:
        ha = 20 * k * q
        c.drawRect(skia.Rect.MakeXYWH(x, y - 30 * k - ha, w, ha), M.paint(COR, a))
        E.foco(c, t, t1 + 0.4, 0.4, lambda r: (centro(c, "20", x + w / 2, y - 30 * k - 10 * k + 18, 50, "g", BR, r * a),
                                              E.escreve(c, "aluguel", x + w + 24, y - 40 * k + 16, 44, "i", COR, r * a)))
        E.foco(c, t, t1 + 0.8, 0.4, lambda r: centro(c, "R$ 50", x + w / 2, y - 50 * k - 24, 54, "g", TINTA, r * a))


def dominio(c, t, y, t0, raiz, tc, td, vmin, vmax, txt1, txt2, ty, tok=None, vok=None, tf=None):
    """reta numérica com o furo em `raiz`: os dois trechos em tc e td e a resposta "]..[ ou ]..[" embaixo"""
    vx = E.reta(c, t, t0, RX0, RX1, y, vmin, vmax, list(range(vmin, vmax + 1)), E._num, size=46)
    E.intervalo(c, t, tc, vx, y, None, raiz)
    E.intervalo(c, t, td, vx, y, raiz, None)
    if tf is not None:
        anel(c, t, tf, vx(raiz), y, ERRADO)
        E.foco(c, t, tf, 0.4, lambda a: centro(c, "furo", vx(raiz), y - 50, 46, "b", ERRADO, a))
    E.foco(c, t, tc, 0.5, lambda a: centro(c, txt1, 640, ty, 90, "g", ENT, a))
    E.foco(c, t, td - 0.4, 0.4, lambda a: centro(c, "ou", W / 2, ty, 70, "i", TINTA, a))
    E.foco(c, t, td, 0.5, lambda a: centro(c, txt2, 1280, ty, 90, "g", ENT, a))
    if tok is not None and t >= tok:
        k = ease_back(prog(t, tok, 0.5))
        c.drawCircle(vx(vok), y, 19 * k, M.paint(CERTO))
        c.drawCircle(vx(vok), y, 19 * k, M.paint(BR, 1.0, stroke=4))
        anel(c, t, tok, vx(vok), y, CERTO)
    return vx


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01.a"], [("1", "g", 80, ENT), ("peça:", "i", 72), ("R$", "g", 80, CUS), ("2.030", "g", 80, CUS)], XE, 300)
        E.frase(c, t, C["s01.b"], [("1.000", "g", 80, ENT), ("peças:", "i", 72), ("R$", "g", 80, CUS), ("32", "g", 80, CUS), ("cada", "i", 72)], XE, 430)
        E.frase(c, t, quando(C, "s01", "Quanto mais peças"), ps("mais peças, mais barata cada uma", "i", 60, TINTA2), XE, 560, passo=0.1)
        E.frase(c, t, C["s01.c"], [("um", "i", 76), ("preço", "g", 80, COR), ("que", "i", 76), ("ela", "i", 76)], XE, 740)
        E.frase(c, t, C["s01.c"] + 0.8, [("nunca", "g", 80, COR), ("alcança", "i", 76)], XE, 850)
        Q = E.plano(c, t, C["s01.a"], 1220, 300, 560, 560, 0, 1050, 0, 105, passo=2000, grade=False, rotulos=False, size=30, d=0.5)
        E.curva(c, t, C["s01.a"] + 0.3, Q, cm, 25, 1050, d=3.0, cor=CUS, largura=9)
        assintota(c, t, C["s01.c"], Q, 30, rot=False, cor=COR)
        E.foco(c, t, C["s01.c"] + 0.5, 0.4, lambda a: E.pilula(c, "?", Q.x(1000), Q.y(30) + 60, 50, "g", fundo=COR, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 280)
        E.frase(c, t, C["s02.a"] + 1.2, [("o", "i", 100), ("custo", "g", 120), ("médio", "g", 120, COR)], XE, 440)
        E.frase(c, t, quando(C, "s02", "descobre esse"), [("e", "i", 90), ("o", "i", 90), ("limite", "g", 100)], XE, 580)
        E.frase(c, t, quando(C, "s02", "acha o domínio"), [("+", "g", 90, COR), ("o", "i", 90), ("domínio", "g", 100)], XE, 720)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"] - 0.6, 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] - 0.45, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.a", "o custo da fábrica", lambda a, y: E.formula(c, "C(x) = 2.000 + 30x", x + 44, y, 64, "g", CUS, a)),
             ("s03.b", "a hipérbole", lambda a, y: (E.formula(c, "f{k}{x}", x + 44, y, 64, "g", COR, a),
                                                    E.escreve(c, "nunca toca o eixo", x + 150, y, 58, "g", TINTA, a))),
             ("s03.c", "o domínio pela fórmula", lambda a, y: E.escreve(c, "embaixo da divisão ≠ 0", x + 44, y, 58, "g", ERRADO, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 170 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 44, y + 76)
        E.foco(c, t, C[k] + 0.5, 0.5, lambda a, fn=fn, y=y: fn(a, y + 170))
    py = lerp(lerp(350, 600, ease_io(prog(t, C["s03.b"] - 0.35, 0.5))), 850, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.a"], 0.4))
    E.foco(c, t, quando(C, "s03", "Se faltar"), 0.5, lambda a: E.pilula(c, "faltou? procure no canal", W / 2, 1000, 44, "g", fundo=TINTA2, a=a))


# ---------------- custo médio ----------------
def b_medio(c, t, C, b):
    Q = lambda fr_, n=1: quando(C, "s04", fr_, n)

    def s04():
        F, s = "C(x) = 2.000 + 30x", 110
        x0 = W / 2 - larg_f(F, s) / 2
        E.foco(c, t, C["s04"], 0.5, lambda a: E.formula(c, F, x0, 300, s, "g", CUS, a))
        E.foco(c, t, C["s04.a"], 0.4, lambda a: E.pilula(c, "custo total do mês", W / 2, 150, 46, "g", fundo=CUS, a=a))
        xa = x0 + larg_f("C(x) = ", s)
        xb = xa + larg_f("2.000", s)
        xc = xb + larg_f(" + ", s)
        xd = xc + larg_f("30x", s)
        ta, tb = Q("Dois mil de"), Q("e trinta reais")
        E.chave(c, xa + 4, xb - 4, 340, TINTA2, ep(t, ta, 0.5), 22, 5)
        E.foco(c, t, ta + 0.2, 0.4, lambda a: centro(c, "aluguel e máquinas", (xa + xb) / 2, 430, 44, "i", TINTA2, a))
        E.chave(c, xc + 4, xd - 4, 340, ENT, ep(t, tb, 0.5), 22, 5)
        E.foco(c, t, tb + 0.2, 0.4, lambda a: centro(c, "R$ 30 por peça", (xc + xd) / 2, 430, 44, "i", ENT, a))
        E.frase(c, t, C["s04.b"], [("custo", "g", 76), ("médio:", "g", 76, COR), ("quanto", "i", 72), ("sai", "i", 72), ("cada", "i", 72), ("peça", "g", 76)],
                W / 2, 620, "center")
        E.foco(c, t, C["s04.c"], 0.6, lambda a: (M.rrect(c, W / 2 - 440, 690, 880, 230, 50, COR, a),
                                                 E.formula(c, "médio = f{C(x)}{x}", W / 2, 840, 96, "g", BR, a, "center")))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("com", "i", 72), ("100", "g", 80, ENT), ("peças:", "i", 72)], XE, 230)
    fml(c, t, C["s05.a"], "C(100) = 2.000 + 3.000 = 5.000", XE, 380, 66, CUS)
    fml(c, t, C["s05.b"], "f{5.000}{100} = R$ 50 por peça", XE, 560, 72, COR)
    E.frase(c, t, quando(C, "s05", "Repare que"), [("mais", "i", 60), ("que", "i", 60), ("os", "i", 60), ("R$", "g", 64, CUS), ("30", "g", 64, CUS), ("de", "i", 60),
                                                    ("material", "i", 60)], XE, 720)
    E.frase(c, t, C["s05.c"], [("cada", "i", 60), ("peça", "i", 60), ("carrega", "i", 60), ("um", "i", 60), ("pedaço", "g", 64, COR), ("do", "i", 60),
                               ("aluguel", "g", 64, COR)], XE, 840)
    barra_peca(c, t, quando(C, "s05", "Repare que"), C["s05.c"], 1380, 900, 160)


# ---------------- separar a soma ----------------
def b_separar(c, t, C, b):
    fml(c, t, C["s06.a"], "f{2.000 + 30x}{x}", XE, 300, 100, CUS)
    E.frase(c, t, C["s06"], [("custo", "g", 64), ("médio", "g", 64, COR)], XE, 150)

    def s06():
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.pilula(c, "divida cada parcela", XE + 860, 270, 50, "g", fundo=COR, a=a))
        E.frase(c, t, C["s06.c"], [("teste:", "i", 60, TINTA2)], XE, 560)
        fml(c, t, C["s06.c"] + 0.3, "f{10 + 6}{2} = f{16}{2} = 8", XE + 230, 560, 72, TINTA)
        fml(c, t, C["s06.d"], "f{10}{2} + f{6}{2} = 5 + 3 = 8", XE + 230, 760, 72, TINTA)
        E.foco(c, t, C["s06.d"] + 1.6, 0.4, lambda a: E.pilula(c, "igual", XE + 1300, 740, 50, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    x1 = XE + larg_f("f{2.000 + 30x}{x}", 100) + 30
    E.foco(c, t, C["s07"], 0.4, lambda a: E.escreve(c, "=", x1, 300, 100, "g", TINTA, a))
    fml(c, t, C["s07.a"], "f{2.000}{x}", x1 + 90, 300, 100, COR)
    x2 = x1 + 90 + larg_f("f{2.000}{x}", 100) + 20
    fml(c, t, C["s07.b"], "+ f{30x}{x}", x2, 300, 100, CUS)
    fml(c, t, C["s07.c"], "f{30x}{x} = 30", XE, 560, 80, CUS)
    E.foco(c, t, C["s07.c"] + 0.5, 0.4, lambda a: E.escreve(c, "o x de cima cancela com o de baixo", XE + 560, 545, 46, "i", TINTA2, a))
    E.foco(c, t, C["s07.d"], 0.6, lambda a: (M.rrect(c, XE - 20, 670, 1100, 250, 50, COR, a),
                                             E.formula(c, "médio = 30 + f{2.000}{x}", XE + 530, 840, 100, "g", BR, a, "center")))


# ---------------- tabela ----------------
def b_tabela(c, t, C, b):
    E.frase(c, t, C["s08"], [("médio", "g", 66, COR), ("=", "g", 66), ("30", "g", 70, CUS), ("+", "g", 66), ("2.000", "g", 70, COR), ("÷", "g", 66),
                             ("x", "g", 70, ENT)], XE, 190)
    x0, y0, hl = 260, 330, 150
    cols = ((360, "peças", ENT), (960, "2.000 ÷ x  +  30", TINTA2), (1560, "custo médio", SAI))
    a = ep(t, C["s08"] + 0.4, 0.5)
    if a > 0:
        for cx, s, cor in cols:
            centro(c, s, cx, y0 - 30, 50, "g" if cor != TINTA2 else "b", cor, a)
        M.line(c, x0, y0, W - x0 + 80, y0, TINTA, a, 4)
    linhas = (("1", "2.000 + 30", "R$ 2.030", "s08.a"), ("100", "20 + 30", "R$ 50", "s08.b"), ("1.000", "2 + 30", "R$ 32", "s08.c"),
              ("10.000", "0,2 + 30", "R$ 30,20", "s08.d"))
    for i, (xv, conta, res, k) in enumerate(linhas):
        ry = y0 + 100 + hl * i
        E.foco(c, t, C[k], 0.4, lambda q, xv=xv, ry=ry: centro(c, xv, cols[0][0], ry, 70, "g", ENT, q), sobe=6)
        E.foco(c, t, C[k] + 0.4, 0.4, lambda q, conta=conta, ry=ry: centro(c, conta, cols[1][0], ry, 62, "g", TINTA2, q), sobe=6)
        E.foco(c, t, C[k] + 0.9, 0.4, lambda q, res=res, ry=ry: centro(c, res, cols[2][0], ry, 70, "g", SAI, q), sobe=6)


# ---------------- limite ----------------
def b_limite(c, t, C, b):
    lift = ease_io(prog(t, C["s10.a"] + 0.3, 1.6))
    plano_cm(c, t, C["s09"])
    E.curva(c, t, C["s09.a"] + 0.4, PC, lambda x: 2000 / x + 30 * lift, 19, 1080, d=1.6, cor=CUS if lift > 0.5 else COR)
    if t < C["s10"]:
        q = pulso(t, C["s09.b"], 3.0)
        if q > 0:
            x, y, w, h = PC.caixa
            M.line(c, PC.ox, PC.oy, x + w + 30, PC.oy, COR, 0.25 * q, 22)
    assintota(c, t, C["s10.b"], PC, 30, cor=TINTA2)
    if t >= C["s10.d"]:
        E.area(c, t, C["s10.d"], PC, cm, 30, 1060, lambda x: 30, cor=COR, alfa=0.22, d=1.2)
    for xv, yv, sx, sy in ((100, 50, "100", "50"), (1000, 32, "1.000", "32")):
        pt_t = C["s10.a"] + 2.2
        if t >= pt_t:
            E.ponto(c, t, pt_t, PC, xv, yv, cor=CUS, r=13)
            E.foco(c, t, pt_t + 0.3, 0.4, lambda a, xv=xv, yv=yv, sx=sx, sy=sy: caixa_par(c, sx, sy, PC.x(xv) + (20 if xv < 500 else -10),
                                                                                         PC.y(yv) - 30, 38, a, "left" if xv < 500 else "right"))

    def s09():
        E.frase(c, t, C["s09"], [("chega", "i", 70), ("a", "i", 70), ("30?", "g", 76, CUS)], XE, 240)
        fml(c, t, C["s09.a"], "f{2.000}{x} = 0 ?", XE, 420, 84, COR)
        E.frase(c, t, C["s09.b"], [("a", "i", 60), ("hipérbole", "g", 64, COR), ("chega", "i", 60), ("perto", "i", 60), ("do", "i", 60), ("zero,", "g", 64)],
                XE, 580)
        E.frase(c, t, C["s09.b"] + 1.4, [("mas", "i", 60), ("nunca", "g", 64, ERRADO), ("encosta", "i", 60)], XE, 670)
        E.foco(c, t, C["s09.c"], 0.6, lambda a: caixa_f(c, "perto de 30, sem chegar", XE + 20, 850, 62, CUS, a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("a", "i", 64), ("mesma", "i", 64), ("hipérbole,", "g", 66, COR)], XE, 240)
    E.frase(c, t, C["s10.a"] + 1.0, [("levantada", "i", 64), ("+30", "g", 70, CUS)], XE, 330)
    E.frase(c, t, C["s10.b"], [("reta", "i", 62), ("tracejada:", "i", 62), ("y", "g", 66, SAI), ("=", "g", 66), ("30", "g", 66, SAI)], XE, 470)
    E.frase(c, t, C["s10.c"], [("a", "i", 100), ("assíntota", "g", 110, COR)], XE, 640)
    E.frase(c, t, C["s10.d"], [("o", "i", 56), ("aluguel", "g", 60, COR), ("se", "i", 56), ("espalha", "i", 56), ("e", "i", 56), ("quase", "i", 56), ("some", "g", 60)],
            XE, 820)


# ---------------- domínio ----------------
def b_dominio(c, t, C, b):
    def s11():
        E.frase(c, t, C["s11"], ps("x embaixo da divisão:", "i", 70), W / 2, 260, "center")
        E.frase(c, t, C["s11.a"], [("funções", "g", 120, COR), ("racionais", "g", 120, COR)], W / 2, 420, "center")
        E.frase(c, t, quando(C, "s11", "pelo vilão"), [("o", "i", 60), ("vilão:", "i", 60), ("÷", "g", 66, ERRADO), ("0", "g", 66, ERRADO)], W / 2, 540, "center")
        fml(c, t, C["s11.b"], "f(x) = f{(x + 1)}{(x − 2)}", W / 2, 820, 110, TINTA, "center")
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    if t < C["s13"]:
        def s12():
            fml(c, t, C["s12"], "f{(x + 1)}{(x − 2)}", XE, 260, 80, TINTA)
            fml(c, t, C["s12.a"], "x − 2 ≠ 0", XE + 500, 230, 76, ERRADO)
            fml(c, t, C["s12.b"], "x ≠ 2", XE + 1050, 230, 90, ENT)
            dominio(c, t, 560, C["s12.b"], 2, C["s12.c"], C["s12.d"], -2, 6, "]−∞, 2[", "]2, +∞[", 800, tf=C["s12.b"] + 0.6)
            E.foco(c, t, quando(C, "s12", "sempre aberto"), 0.4, lambda a: centro(c, "aberto no 2", W / 2, 920, 50, "b", TINTA2, a))
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    fml(c, t, C["s13"], "f{(x + 1)}{(x − 2)}", XE, 260, 80, TINTA)
    E.frase(c, t, C["s13"], [("o", "i", 62), ("de", "i", 62), ("cima", "g", 66), ("pode", "i", 62), ("ser", "i", 62), ("0", "g", 66, CERTO)], XE + 520, 230)
    fml(c, t, C["s13.a"], "x = −1:  f{−1 + 1}{−1 − 2} = f{0}{−3}", XE, 470, 70, TINTA)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.pilula(c, "= 0: um número normal", XE + 1290, 450, 48, "g", fundo=CERTO, a=a))
    dominio(c, t, 680, C["s13"], 2, C["s13"], C["s13"] + 0.2, -2, 6, "", "", -100, tok=C["s13.b"], vok=-1)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.pilula(c, "na fábrica: x = 1, 2, 3, …", W / 2, 900, 52, "g", fundo=CUS, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14.a"], [("o", "i", 70), ("erro:", "i", 70), ("cortar", "g", 76, ERRADO), ("o", "i", 70), ("x", "g", 76, ERRADO), ("só", "i", 70), ("de", "i", 70),
                               ("um", "i", 70), ("lado", "i", 70)], XE, 220)
    fml(c, t, quando(C, "s14", "A pessoa risca"), "f{2.000 + 30x}{x}", XE, 420, 90, TINTA)
    xe = XE + larg_f("f{2.000 + 30x}{x}", 90) + 30
    fml(c, t, C["s14.b"], "= 2.000 + 30 = 2.030", xe, 420, 76, ERRADO)
    E.foco(c, t, C["s14.b"] + 1.0, 0.4, lambda a: E.escreve(c, "para qualquer quantidade?", xe, 500, 46, "i", ERRADO, a))
    if t >= C["s14.c"]:
        E.risco(c, xe - 10, 440, xe + larg_f("= 2.000 + 30 = 2.030", 76) + 10, 360, t, C["s14.c"], largura=12)
    E.frase(c, t, C["s14.c"], [("100", "g", 70, ENT), ("peças:", "i", 64)], XE, 680)
    fml(c, t, C["s14.c"] + 0.6, "f{5.000}{100} = 50", XE + 330, 680, 80, CERTO)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "a divisão vale para as duas parcelas", W / 2, 900, 56, "g", fundo=COR, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    Q = E.plano(c, t, C["s15"], 1120, 220, 640, 640, -50, 1080, -8, 108, passo=200, passo_y=10, marcas_x=[200, 400, 600, 800, 1000], marcas_y=[30, 40, 60, 80, 100],
                fmt=mil, escuro=True, size=30)
    E.curva(c, t, C["s15"] + 0.3, Q, cm, 19, 1080, d=1.2, cor=CLARO)
    assintota(c, t, C["s15"] + 0.6, Q, 30, rot=False, cor=CLARO)
    p = ep(t, C["s15.a"] + 0.6, 0.6)
    if p > 0:
        M.line(c, Q.x(0), Q.y(40), lerp(Q.x(0), Q.x(1060), p), Q.y(40), AMARELO, 1.0, 4, dash=[12, 10])
    if t >= C["s15.c"]:
        M.line(c, Q.x(200), Q.y(40), Q.x(200), Q.oy, AMARELO, ep(t, C["s15.c"], 0.4), 4, dash=E.TRACO)
        E.ponto(c, t, C["s15.c"], Q, 200, 40, cor=AMARELO, r=16)
        E.foco(c, t, C["s15.c"] + 0.3, 0.4, lambda a: E.pilula(c, "200 peças", Q.x(200) + 130, Q.y(40) - 60, 38, "g", fundo=COR, a=a))
    if t >= C["s16.c"]:
        q = ep(t, C["s16.c"], 0.5)
        M.line(c, Q.x(0), Q.y(22), Q.x(1060), Q.y(22), ERRADO, q, 4, dash=[12, 10])
        E.foco(c, t, C["s16.c"] + 0.3, 0.4, lambda a: E.pilula(c, "sem resposta", Q.x(700), Q.y(22) + 46, 34, "g", fundo=ERRADO, a=a))

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho do alvo", "i", 66, CLARO), XE, 200, passo=0.12)
        E.frase(c, t, C["s15.a"], [("médio", "g", 66, BR), ("=", "g", 66, BR), ("R$", "g", 70, AMARELO), ("40:", "g", 70, AMARELO)], XE, 310)
        E.frase(c, t, C["s15.a"] + 1.0, [("quantas", "i", 62, CLARO), ("peças?", "g", 66, BR)], XE, 400)
        E.foco(c, t, C["s15.b"] - 0.6, 0.4, lambda a: E.escreve(c, "tire o custo por peça", XE, 500, 46, "i", CLARO, a))
        fml(c, t, C["s15.b"], "40 − 30 = 10", XE, 600, 80, BR)
        E.foco(c, t, C["s15.c"] - 0.6, 0.4, lambda a: E.escreve(c, "divida o fixo pelo resto", XE, 700, 46, "i", CLARO, a))
        fml(c, t, C["s15.c"], "f{2.000}{10} = 200 peças", XE, 850, 84, AMARELO)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    fml(c, t, C["s16.a"], "f{2.000}{x} = 10", XE, 280, 84, BR)
    E.foco(c, t, C["s16.a"] + 0.8, 0.4, lambda a: E.escreve(c, "o pedaço do aluguel", XE + 520, 270, 48, "i", CLARO, a))
    fml(c, t, C["s16.b"], "f{2.000}{200} = 10", XE, 480, 76, BR)
    fml(c, t, quando(C, "s16", "Mais trinta dá"), "10 + 30 = 40", XE + 430, 480, 64, AMARELO)
    E.frase(c, t, C["s16.c"], [("não", "g", 66, ERRADO), ("compensa:", "i", 62, CLARO), ("alvo", "i", 62, CLARO), ("≤", "g", 66, BR), ("30", "g", 66, BR)], XE, 680)
    E.frase(c, t, quando(C, "s16", "aí não existe"), ps("o custo médio nunca chega lá", "i", 56, CLARO), XE, 790, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], [("hora", "i", 70, COR), ("de", "i", 70, COR), ("testar", "i", 70, COR)], XE, 200)
    E.foco(c, t, C["s17"] + 1.0, 0.4, lambda a: E.pilula(c, "valores inventados", XE + 730, 180, 40, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s17.a"], [("gráfica:", "i", 64)], XE, 350)
    fml(c, t, C["s17.a"] + 0.4, "C(x) = 600 + 2x", XE + 280, 350, 84, CUS)
    E.frase(c, t, C["s17.b"], [("1)", "g", 60, COR), ("custo", "i", 60), ("médio", "g", 60), ("de", "i", 60), ("300", "g", 64, ENT), ("convites?", "i", 60)], XE, 520)
    E.frase(c, t, C["s17.c"], [("2)", "g", 60, COR), ("quantos", "i", 60), ("convites", "i", 60), ("para", "i", 60), ("R$", "g", 64, CUS), ("3?", "g", 64, CUS)], XE, 630)
    E.foco(c, t, C["s17.d"], 0.4, lambda a: (E.escreve(c, "3)", XE, 780, 60, "g", COR, a), E.escreve(c, "domínio de", XE + 90, 780, 60, "i", TINTA, a),
                                             E.formula(c, "f{x − 5}{x + 3}?", XE + 90 + E.larg("domínio de", "i", 60) + 24, 780, 64, "g", TINTA, a)))
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1500, cy=520, r=170)


def b_resposta(c, t, C, b):
    Q = lambda fr_, n=1: quando(C, "s19", fr_, n)

    def s19():
        E.foco(c, t, C["s19.a"], 0.6, lambda a: (M.rrect(c, XE - 20, 150, 760, 210, 46, COR, a),
                                                 E.formula(c, "médio = 2 + f{600}{x}", XE + 360, 290, 84, "g", BR, a, "center")))
        E.frase(c, t, C["s19.b"], [("300", "g", 64, ENT), ("convites:", "i", 60)], XE, 500)
        fml(c, t, C["s19.b"] + 0.5, "f{600}{300} = 2", XE + 360, 500, 72, COR)
        fml(c, t, Q("Mais dois dá"), "2 + 2 = R$ 4", XE + 780, 500, 72, CERTO)
        E.frase(c, t, Q("Para três reais"), [("alvo", "i", 60), ("R$", "g", 64, CUS), ("3:", "g", 64, CUS)], XE, 720)
        fml(c, t, C["s19.c"], "3 − 2 = 1", XE + 300, 720, 72, TINTA)
        fml(c, t, C["s19.d"], "f{600}{1} = 600 convites", XE + 700, 720, 72, CERTO)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    fml(c, t, C["s20"], "f{x − 5}{x + 3}", XE, 260, 80, TINTA)
    fml(c, t, C["s20.a"], "x + 3 ≠ 0", XE + 400, 230, 76, ERRADO)
    fml(c, t, C["s20.b"], "x ≠ −3", XE + 960, 230, 90, ENT)
    dominio(c, t, 560, C["s20.b"], -3, C["s20.c"], C["s20.d"], -5, 6, "]−∞, −3[", "]−3, +∞[", 800, tok=C["s20.e"], vok=5, tf=C["s20.b"] + 0.6)
    E.foco(c, t, C["s20.e"], 0.5, lambda a: E.pilula(c, "x = 5: f(5) = 0, entra", W / 2, 940, 48, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", lambda a, y: (E.escreve(c, "custo médio =", 340, y, 70, "i", TINTA, a),
                                         E.formula(c, "30 + f{2.000}{x}", 340 + E.larg("custo médio =", "i", 70) + 30, y, 80, "g", COR, a))),
                 ("s21.b", lambda a, y: (E.escreve(c, "chega perto de 30,", 340, y, 72, "g", CUS, a),
                                         E.escreve(c, "sem nunca chegar", 340 + E.larg("chega perto de 30,", "g", 72) + 26, y, 72, "i", TINTA, a))))
        for i, (k, fn) in enumerate(itens):
            y = 450 + i * 240
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, fn=fn, y=y: fn(a, y))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s22"] + 0.8, [("praticando", "g", 130, COR)], XE, 460)
    E.frase(c, t, C["s22.a"], [("k/x", "g", 62, COR), ("em", "i", 58), ("tabelas", "i", 58), ("e", "i", 58), ("gráficos", "i", 58)], XE, 590)
    E.frase(c, t, C["s22.b"], [("e", "i", 58), ("quando", "i", 58), ("o", "i", 58), ("x", "g", 62, ENT), ("cresce?", "g", 62)], XE, 690)
    Q = E.plano(c, t, C["s22"] + 0.4, 1300, 560, 400, 280, 0, 13, 0, 13, passo=13, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, C["s22"] + 0.7, Q, lambda x: 12 / x, 0.95, 13, d=1.0, cor=COR, largura=9)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, medio=b_medio, separar=b_separar, tabela=b_tabela, limite=b_limite, dominio=b_dominio,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
