"""Visual — Estudativo · MAT-FUN-024: praticando função quadrática (quatro situações).

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()); erro em vermelho.
Como na MAT-FUN-016 a 018: parábola de a > 0 índigo, de a < 0 preta; raízes como círculos índigo no eixo x; o vértice é a esfera
amarela (VERT) com anel; eixo de simetria tracejado em pé; a imagem é a faixa preta sobre o eixo y (faixa_imagem()).
Como na MAT-FUN-014 e 015: lucro verde e prejuízo vermelho, pintados com E.area; cada situação abre com a esfera numerada.
Nesta aula: "quando?" (o x) em pílula índigo no eixo x e "quanto?" (o y) em pílula preta no eixo y; ]2, 10[ como faixa verde
sobre o eixo x com as bolinhas abertas.
Tempos: sem voz gravada, tudo sai dos marcadores {a}, {b}... Dentro de uma frase longa, quando() acha a palavra no texto do
cenas.py e interpola entre os dois marcadores vizinhos (vale para a voz provisória e para a voz real).
Peças locais: quando(), eixos(), par(), anel(), marca_ponto(), fsub(), caixa_f(), raiz(), vertice(), eixo_sim(), faixa_imagem(),
faixa_x(), num_situacao(), pergunta(), marmita()."""
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
ARQUIVO_FINAL = "estudativo_MAT-FUN-024_praticando_funcao_quadratica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
VERT = "#F2B705"
PAPEL = "#F4F3EF"

f1 = lambda x: x * x - 8 * x + 12
h2 = lambda x: -5 * x * x + 30 * x
r3 = lambda x: (20 + x) * (200 - 5 * x)
l4 = lambda x: -x * x + 12 * x - 20
assert 8 ** 2 == 64 and 4 * 1 * 12 == 48 and 64 - 48 == 16 and (8 + 4) / 2 == 6 and (8 - 4) / 2 == 2 and f1(2) == f1(6) == 0
assert (2 + 6) / 2 == 4 and 16 - 32 + 12 == -4 and f1(4) == -4
assert h2(0) == h2(6) == 0 and -30 / -5 == 6 and 6 / 2 == 3 and -5 * 9 == -45 and -45 + 90 == 45 and h2(3) == 45
assert r3(-20) == r3(40) == 0 and (-20 + 40) / 2 == 10 and 20 + 10 == 30 and 200 - 5 * 10 == 150 and 30 * 150 == 4500 and r3(0) == 4000
assert 12 ** 2 == 144 and 4 * -1 * -20 == 80 and 144 - 80 == 64 and (-12 + 8) / -2 == 2 and (-12 - 8) / -2 == 10
assert l4(2) == l4(10) == 0 and (2 + 10) / 2 == 6 and -36 + 72 - 20 == 16 and l4(6) == 16 and l4(5) > 0 and l4(1) < 0 and l4(11) < 0

PL = (1080, 190, 700, 700)
P1 = E.Plano(*PL, -0.8, 8.6, -6, 7.5)
M1 = ([1, 2, 3, 4, 5, 6, 7, 8], [-6, -4, -2, 2, 4, 6])
P2 = E.Plano(*PL, -0.7, 7.2, -7, 56)
M2 = ([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50])
P3 = E.Plano(*PL, -26, 47, -700, 5600)
M3 = ([-20, -10, 10, 20, 30, 40], [1000, 2000, 3000, 4000, 5000])
P4 = E.Plano(*PL, -0.8, 13.2, -24, 21)
M4 = ([2, 4, 6, 8, 10, 12], [-20, -10, 10, 20])


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


def num_situacao(c, t, t0, n, x=XE, y=200, titulo=None):
    """esfera com o número da situação e o título ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x + 46, y - 26, 46, a=a), centro(c, str(n), x + 46, y - 4, 56, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, titulo or [("situação", "i", 72), (str(n), "g", 72, COR)], x + 120, y)


def pergunta(c, t, t0, n, partes, y, x=XE, size=62):
    E.frase(c, t, t0, [(f"{n})", "g", size, COR)] + [(w, e, size, *k) for w, e, *k in partes], x, y)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 220, COR), ("situações", "i", 110)], XE, 400)
    E.frase(c, t, C["s01.a"] + 1.4, ps("com o principal da parábola", "i", 70, TINTA2), XE, 520, passo=0.12)
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
    itens = (("s02.a", "as raízes", lambda a, x, y: E.formula(c, "Δ e Bhaskara", x, y, 66, "g", ENT, a)),
             ("s02.b", "o vértice", lambda a, x, y: (E.escreve(c, "média ou", x, y, 58, "i", TINTA, a),
                                                     E.formula(c, "f{−b}{2a}", x + E.larg("média ou", "i", 58) + 24, y, 66, "g", COR, a))),
             ("s02.c", "o sinal do a", lambda a, x, y: E.escreve(c, "diz a boca", x, y, 66, "g", TINTA, a)),
             ("s02.d", "o estudo", lambda a, x, y: E.escreve(c, "do sinal", x, y, 66, "g", TINTA, a)))
    for i, (k, rot, fn) in enumerate(itens):
        col, lin = i % 2, i // 2
        x, y = XE + col * 820, 400 + lin * 270
        E.foco(c, t, C[k], 0.5, lambda a, i=i, x=x, y=y: (E.bola(c, x + 40, y - 20, 40, a=a),
                                                          centro(c, str(i + 1), x + 40, y, 48, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, rot=rot, x=x, y=y: E.escreve(c, rot, x + 110, y, 56, "i", TINTA2, a))
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, fn=fn, x=x, y=y: fn(a, x + 110, y + 100))
    E.foco(c, t, quando(C, "s02", "Se alguma"), 0.5,
           lambda a: E.pilula(c, "travou? procure a aula no canal", W / 2, 960, 46, "g", fundo=TINTA2, a=a))


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    num_situacao(c, t, C["s03.a"], 1)
    fml(c, t, C["s03.b"], "f(x) = x^2 − 8x + 12", XE, 400, 100, TINTA)
    pergunta(c, t, C["s03.c"], 1, [("as", "i"), ("raízes", "g"), ("e", "i"), ("o", "i"), ("vértice?", "g", COR)], 580)
    pergunta(c, t, quando(C, "s03", "O vértice é"), 2, [("máximo", "g"), ("ou", "i"), ("mínimo?", "g")], 690)
    pergunta(c, t, quando(C, "s03", "E qual é"), 3, [("a", "i"), ("imagem?", "g", COR)], 800)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=1500, cy=460, r=180)


def b_resposta1(c, t, C, b):
    eixos(c, t, P1, C["s05"], tg=C["s05"], marcas=M1, size=36)
    E.curva(c, t, C["s05.b"] + 0.3, P1, f1, 0.8, 7.2, d=1.2, cor=COR)
    raiz(c, t, C["s05.b"], P1, 6, "6", lado=-1, size=34, off=22)
    raiz(c, t, C["s05.b"] + 0.3, P1, 2, "2", size=34, off=22)
    Q = lambda fr_, n=1: quando(C, "s05", fr_, n)

    def s05():
        fml(c, t, C["s05"] + 0.4, "Δ = b^2 − 4ac", XE, 240, 72, TINTA)
        fml(c, t, C["s05.a"], "b^2 = 64", XE, 370, 64, TINTA)
        fml(c, t, Q("quatro vezes á"), "4ac = 48", XE + 380, 370, 64, TINTA)
        fml(c, t, Q("Sessenta e quatro menos"), "Δ = 64 − 48 = 16", XE, 490, 64, TINTA)
        fml(c, t, Q("A raiz de"), "r{16} = 4", XE, 620, 64, TINTA)
        fml(c, t, Q("Xis é igual"), "x = f{8 ± 4}{2}", XE, 790, 76, ENT)
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.escreve(c, "= 6 ou 2", XE + larg_f("x = f{8 ± 4}{2}", 76) + 30, 790, 76, "g", ENT, a))
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    Q = lambda fr_, n=1: quando(C, "s06", fr_, n)
    eixo_sim(c, t, C["s06.a"] + 0.6, P1, 4, ENT, 0.7)
    vertice(c, t, C["s06.c"], P1, 4, -4, ("4", "−4"), dx=90)
    E.frase(c, t, C["s06"], [("raízes:", "i", 56, TINTA2), ("2", "g", 60, ENT), ("e", "i", 56, TINTA2), ("6", "g", 60, ENT)], XE, 220)
    fml(c, t, C["s06.a"], "x_v = f{2 + 6}{2} = f{8}{2} = 4", XE, 360, 70, ENT)
    fml(c, t, C["s06.b"], "f(4) = 16 − 32 + 12 = −4", XE, 490, 64, SAI)
    E.frase(c, t, C["s06.c"], [("vértice:", "i", 64)], XE, 600)
    par_em(c, t, C["s06.c"] + 0.3, "4", "−4", XE + 225, 600, 70)
    E.foco(c, t, C["s06.d"], 0.5, lambda a: E.pilula(c, "a > 0: boca para cima → mínimo", XE + 360, 710, 46, "g", fundo=COR, a=a))
    guia_h(c, t, C["s06.e"], P1, 4, -4)
    faixa_imagem(c, t, C["s06.e"] + 0.3, P1, -4, True)
    E.foco(c, t, C["s06.e"] + 0.3, 0.6, lambda a: caixa_f(c, "Im = [−4, +∞[", XE + 20, 870, 76, SAI, a))


# ---------------- situação 2 ----------------
def bola_jogada(c, t, t0, a):
    """bola que sobe do chão e volta, sem parar"""
    if a <= 0:
        return
    x0, chao = 1500, 860
    M.line(c, 1300, chao, 1700, chao, TINTA, a, 6)
    u = ((t - t0) / 2.4) % 1
    alt = 4 * u * (1 - u)
    M.line(c, x0, chao - 30, x0, chao - 30 - 440 * alt, FIO, a, 4, dash=E.TRACO)
    E.bola(c, x0, chao - 40 - 440 * alt, 40, a=a)
    E.foco(c, t, t0 + 0.4, 0.4, lambda q: E.escreve(c, "chão", 1310, chao + 56, 44, "i", TINTA2, q * a))


def b_questao2(c, t, C, b):
    num_situacao(c, t, C["s07.a"], 2)
    E.frase(c, t, C["s07.a"] + 1.0, ps("uma bola sai do chão", "i", 62, TINTA2), XE, 310, passo=0.12)
    fml(c, t, C["s07.b"], "h(t) = −5t^2 + 30t", XE, 460, 96, TINTA)
    E.frase(c, t, quando(C, "s07", "com tê em"), [("h", "g", 50, SAI), ("em", "i", 50, TINTA2), ("metros,", "i", 50, TINTA2),
                                                    ("t", "g", 50, ENT), ("em", "i", 50, TINTA2), ("segundos", "i", 50, TINTA2)], XE, 560)
    pergunta(c, t, C["s07.c"], 1, [("a", "i"), ("altura", "g"), ("máxima?", "g", COR)], 700)
    pergunta(c, t, C["s07.d"], 2, [("quanto", "i"), ("tempo", "g"), ("no", "i"), ("ar?", "g", COR)], 810)
    E.saida(c, t, C["s08.a"] - 0.2, lambda: bola_jogada(c, t, C["s07.a"], ep(t, C["s07.a"] + 0.6, 0.5)))
    if t >= C["s08"]:
        E.relogio(c, t, C["s08.a"], cx=1500, cy=460, r=180)


def b_resposta2(c, t, C, b):
    eixos(c, t, P2, C["s09"], tg=C["s09"], marcas=M2, size=36, nx="t", ny="h")
    E.curva(c, t, C["s09.a"] + 0.3, P2, h2, 0, 6, d=1.4, cor=TINTA)
    raiz(c, t, C["s09.a"], P2, 0, "0")
    raiz(c, t, C["s09.c"], P2, 6, "6", lado=-1)
    fml(c, t, C["s09"], "h(t) = −5t^2 + 30t", XE, 230, 66, TINTA)
    Q = lambda fr_, n=1: quando(C, "s09", fr_, n)

    def s09():
        E.foco(c, t, Q("Sem cê"), 0.5, lambda a: E.pilula(c, "sem c", XE + 90, 340, 46, "g", fundo=TINTA2, a=a))
        fml(c, t, C["s09.a"], "uma raiz: t = 0", XE, 470, 66, ENT)
        fml(c, t, C["s09.b"], "a outra: f{−b}{a} = f{−30}{−5} = 6", XE, 620, 66, ENT)
        E.foco(c, t, C["s09.c"], 0.5, lambda a: caixa_f(c, "no ar: 6 segundos", XE + 20, 820, 72, CERTO, a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    Q = lambda fr_, n=1: quando(C, "s10", fr_, n)
    eixo_sim(c, t, C["s10.a"], P2, 3, ENT, 0.7)
    vertice(c, t, C["s10.d"], P2, 3, 45, ("3", "45"), abaixo=True)
    fml(c, t, C["s10.a"], "topo no meio: t = 3", XE, 360, 62, ENT)
    fml(c, t, C["s10.b"], "h(3) = −5 · 3^2 + 30 · 3", XE, 480, 62, TINTA)
    fml(c, t, C["s10.c"], "−5 · 9 = −45", XE, 590, 62, TINTA)
    fml(c, t, C["s10.d"], "−45 + 90 = 45 m", XE, 700, 72, SAI)
    # o erro: o 3 diz quando, o 45 diz quanto
    tq, tn = Q("respondeu quando"), Q("não quanto")
    E.foco(c, t, tq, 0.4, lambda a: E.pilula(c, "quando? 3 s", P2.x(3), P2.oy + 110, 40, "g", fundo=ENT, a=a))
    guia_h(c, t, tn - 0.3, P2, 3, 45, 0.8)
    E.foco(c, t, tn, 0.4, lambda a: E.pilula(c, "quanto? 45 m", P2.ox - 160, P2.y(45), 40, "g", fundo=SAI, a=a))
    E.frase(c, t, C["s10.e"], [("respondeu", "i", 58), ("3?", "g", 62, ERRADO), ("parou", "i", 58), ("no", "i", 58), ("x", "g", 62, ERRADO)], XE, 860)


# ---------------- situação 3 ----------------
def marmita(c, cx, cy, s, a):
    """marmita de alumínio com tampa"""
    if a <= 0:
        return
    w, h = 300 * s, 150 * s
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 26 * s, "#D9D9DE", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26 * s, 26 * s), M.paint(TINTA, a, stroke=6))
    M.rrect(c, cx - w / 2 - 14 * s, cy - h / 2 - 34 * s, w + 28 * s, 40 * s, 16 * s, COR, a)
    M.line(c, cx - w / 2 + 30 * s, cy, cx + w / 2 - 30 * s, cy, "#BDBDC4", a, 5)


def b_questao3(c, t, C, b):
    num_situacao(c, t, C["s11.a"], 3)
    E.frase(c, t, C["s11.b"], [("vende", "i", 62), ("200", "g", 68, SAI), ("marmitas", "i", 62), ("por", "i", 62), ("dia", "i", 62)], XE, 330)
    E.frase(c, t, quando(C, "s11", "a vinte"), [("a", "i", 62), ("R$", "g", 68, COR), ("20", "g", 68, COR), ("cada", "i", 62)], XE, 430)
    E.frase(c, t, C["s11.c"], [("cada", "i", 62), ("+", "g", 68, COR), ("R$", "g", 68, COR), ("1", "g", 68, COR), ("de", "i", 62), ("aumento:", "i", 62),
                               ("−5", "g", 68, ERRADO), ("marmitas", "i", 62)], XE, 560)
    pergunta(c, t, C["s11.d"], 1, [("qual", "i"), ("preço", "g", COR), ("dá", "i"), ("a", "i"), ("maior", "i"), ("receita?", "g")], 730)
    pergunta(c, t, quando(C, "s11", "E de quanto"), 2, [("de", "i"), ("quanto", "i"), ("é", "i"), ("essa", "i"), ("receita?", "g")], 840)

    def desenho():
        marmita(c, 1640, 300, 0.75, ep(t, C["s11.b"], 0.5))
        E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: E.pilula(c, "R$ 20", 1640, 430, 46, "g", fundo=COR, a=a))
    E.saida(c, t, C["s12.a"] - 0.2, desenho)
    if t >= C["s12"]:
        E.relogio(c, t, C["s12.a"], cx=1500, cy=460, r=180)


def tabela3(c, t, ta, tb, tc, tl):
    """quadro aumento x | preço | marmitas, com a linha do x no fim"""
    x0, y0, wc, hl = 1100, 330, 230, 110
    cab = (("aumento x", ENT), ("preço", COR), ("marmitas", SAI))
    a = ep(t, ta, 0.5)
    if a > 0:
        for j, (s, cor) in enumerate(cab):
            centro(c, s, x0 + wc * j + wc / 2, y0 - 30, 44, "i" if j else "g", cor, a)
        M.line(c, x0, y0, x0 + 3 * wc, y0, TINTA, a, 4)
        for j in (1, 2):
            M.line(c, x0 + wc * j, y0, x0 + wc * j, y0 + hl * 3 + 10, TINTA, a, 4)
    linhas = ((("0", ta + 0.3), ("20", ta + 0.4), ("200", ta + 0.5)),
              (("1", tl), ("21", tl + 0.2), ("195", tl + 0.4)),
              (("x", ta + 0.6), ("20 + x", tb), ("200 − 5x", tc)))
    for i, row in enumerate(linhas):
        ry = y0 + 10 + hl * i
        if i == 2 and t >= ta + 0.6:
            M.rrect(c, x0 - 8, ry + 6, 3 * wc + 16, hl - 12, 14, COR, 0.12 * ep(t, ta + 0.6, 0.4))
        for j, (v, t0) in enumerate(row):
            E.foco(c, t, t0, 0.4, lambda q, v=v, j=j, ry=ry: centro(c, v, x0 + wc * j + wc / 2, ry + hl / 2 + 20, 56 if len(v) < 6 else 46, "g",
                                                                    cab[j][1], q), sobe=6)


def b_resposta3(c, t, C, b):
    Q = lambda fr_, n=1: quando(C, "s13", fr_, n)

    def s13():
        E.foco(c, t, C["s13.a"], 0.5, lambda a: (E.caixa_pontilhada(c, XE - 20, 170, 760, 100, a, prog_=a),
                                                 E.escreve(c, "x = reais de aumento", XE + 10, 240, 56, "g", ENT, a)))
        E.cursor(c, XE + 720, 250, ep(t, Q("Anote isso"), 0.4))
        fml(c, t, C["s13.b"], "preço = 20 + x", XE, 400, 64, COR)
        fml(c, t, C["s13.c"], "marmitas = 200 − 5x", XE, 520, 64, SAI)
        E.frase(c, t, Q("Receita é preço"), [("receita", "g", 56), ("=", "g", 56), ("preço", "i", 56, COR), ("×", "g", 56), ("quantidade", "i", 56, SAI)],
                XE, 650)
        tabela3(c, t, C["s13.a"], C["s13.b"], C["s13.c"], C["s13.a"] + 1.0)
    E.saida(c, t, C["s14"] - 0.1, s13)
    # a lei fica no alto até o fim
    y_lei = lerp(820, 230, ease_io(prog(t, C["s14"], 0.6)))
    E.foco(c, t, C["s13.d"], 0.6, lambda a: caixa_f(c, "R(x) = (20 + x)(200 − 5x)", XE + 20, y_lei, 64 if t < C["s14"] else 56, TINTA, a))
    if t < C["s14"]:
        return
    eixos(c, t, P3, C["s14"], tg=C["s14"], marcas=M3, size=32, fmt=mil, ry=[1000, 2000, 4000, 5000])
    E.curva(c, t, C["s14"] + 0.3, P3, r3, -20, 40, d=1.4, cor=TINTA)
    raiz(c, t, C["s14.a"], P3, -20, "−20")
    raiz(c, t, C["s14.b"], P3, 40, "40", lado=-1)
    eixo_sim(c, t, C["s14.c"] + 0.8, P3, 10, ENT, 0.7)
    Q = lambda fr_, n=1: quando(C, "s14", fr_, n)

    def s14():
        E.foco(c, t, C["s14"], 0.5, lambda a: E.pilula(c, "atalho: não abra os parênteses", XE + 330, 350, 42, "g", fundo=COR, a=a))
        fml(c, t, C["s14.a"], "20 + x = 0  →  x = −20", XE, 480, 60, ENT)
        fml(c, t, C["s14.b"], "200 − 5x = 0  →  x = 40", XE, 590, 60, ENT)
        fml(c, t, C["s14.c"], "x_v = f{−20 + 40}{2} = f{20}{2} = 10", XE, 740, 64, ENT)
        E.foco(c, t, Q("O melhor aumento"), 0.5, lambda a: E.pilula(c, "melhor aumento: R$ 10", XE + 270, 880, 48, "g", fundo=ENT, a=a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    Q = lambda fr_, n=1: quando(C, "s15", fr_, n)
    ta = Q("Antes, eram")
    E.ponto(c, t, ta, P3, 0, 4000, cor=TINTA2, r=14)
    E.foco(c, t, ta + 0.3, 0.4, lambda a: E.pilula(c, "antes: 4.000", P3.ox + 120, P3.y(3300), 34, "g", fundo=TINTA2, a=a))
    vertice(c, t, C["s15.d"], P3, 10, 4500, ("10", "4.500"), abaixo=False, dx=30)
    E.frase(c, t, C["s15.a"], [("a", "i", 64), ("pergunta", "i", 64), ("pede", "i", 64), ("o", "i", 64), ("preço", "g", 68, COR)], XE, 360)
    fml(c, t, C["s15.b"], "20 + 10 = R$ 30", XE, 480, 70, COR)
    E.frase(c, t, C["s15.c"], [("vende", "i", 62), ("150", "g", 68, SAI), ("marmitas", "i", 62)], XE, 590)
    E.foco(c, t, C["s15.d"], 0.6, lambda a: caixa_f(c, "30 · 150 = R$ 4.500", XE + 20, 730, 66, CERTO, a))
    E.frase(c, t, C["s15.e"], [("R$", "g", 58, ERRADO), ("10", "g", 58, ERRADO), ("é", "i", 56), ("o", "i", 56), ("aumento,", "i", 56), ("não", "g", 56, ERRADO),
                               ("o", "i", 56), ("preço", "g", 56)], XE, 880)


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    num_situacao(c, t, C["s16.a"], 4, titulo=[("máximo", "g", 72, COR), ("e", "i", 72), ("sinal", "g", 72, COR)])
    E.frase(c, t, quando(C, "s16", "Uma fábrica"), [("x", "g", 60, ENT), ("=", "g", 60, ENT), ("toneladas", "i", 58), ("por", "i", 58), ("mês", "i", 58)],
            XE, 320)
    fml(c, t, C["s16.b"], "L(x) = −x^2 + 12x − 20", XE, 470, 92, TINTA)
    E.frase(c, t, C["s16.b"] + 0.6, ps("lucro em mil reais", "i", 50, TINTA2), XE, 560, passo=0.1)
    pergunta(c, t, C["s16.c"], 1, [("para", "i"), ("quais", "i"), ("x", "g", ENT), ("há", "i"), ("lucro?", "g", CERTO)], 710)
    pergunta(c, t, C["s16.d"], 2, [("qual", "i"), ("x", "g", ENT), ("dá", "i"), ("o", "i"), ("maior", "i"), ("lucro?", "g", COR)], 820)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=460, r=180)


def b_resposta4(c, t, C, b):
    eixos(c, t, P4, C["s18"], tg=C["s18"], marcas=M4, size=34)
    E.curva(c, t, C["s18.c"] + 0.3, P4, l4, 0, 12, d=1.2, cor=TINTA)
    raiz(c, t, C["s18.c"], P4, 2, "2", lado=-1)
    raiz(c, t, C["s18.c"] + 0.3, P4, 10, "10")
    fml(c, t, C["s18"], "L(x) = −x^2 + 12x − 20", XE, 230, 64, TINTA)
    Q = lambda fr_, n=1: quando(C, "s18", fr_, n)

    def s18():
        E.frase(c, t, C["s18.a"], [("lucro:", "i", 60), ("L(x)", "g", 64), (">", "g", 64, CERTO), ("0", "g", 64, CERTO)], XE, 340)
        E.foco(c, t, Q("é estudo"), 0.4, lambda a: E.pilula(c, "estudo do sinal", XE + 640, 320, 40, "g", fundo=TINTA2, a=a))
        fml(c, t, Q("Delta: bê"), "b^2 = 144", XE, 460, 60, TINTA)
        fml(c, t, Q("E quatro vezes"), "4ac = 4 · (−1) · (−20)", XE, 570, 60, TINTA)
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.escreve(c, "= 80", XE + larg_f("4ac = 4 · (−1) · (−20)", 60) + 20, 570, 60, "g", CERTO, a))
        E.foco(c, t, Q("porque menos com"), 0.4, lambda a: E.pilula(c, "− com − dá +", XE + 220, 650, 38, "g", fundo=CERTO, a=a))
        fml(c, t, Q("Cento e quarenta e quatro menos"), "Δ = 144 − 80 = 64", XE, 770, 60, TINTA)
        fml(c, t, Q("A raiz é"), "r{64} = 8", XE + 600, 770, 60, TINTA)
        fml(c, t, Q("Xis é igual"), "x = f{−12 ± 8}{−2}", XE, 920, 66, ENT)
        E.foco(c, t, C["s18.c"], 0.5, lambda a: E.escreve(c, "= 2 ou 10", XE + larg_f("x = f{−12 ± 8}{−2}", 66) + 30, 920, 66, "g", ENT, a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    # sinal: lucro (verde) entre as raízes, prejuízo (vermelho) fora
    E.area(c, t, C["s19.a"], P4, l4, 2, 10, cor=CERTO, alfa=0.3, d=1.0)
    E.area(c, t, C["s19.a"] + 1.0, P4, l4, 0, 2, cor=ERRADO, alfa=0.22, d=0.5)
    E.area(c, t, C["s19.a"] + 1.0, P4, l4, 10, 12, cor=ERRADO, alfa=0.22, d=0.5)
    faixa_x(c, t, C["s19.c"], P4, 2, 10)
    Q = lambda fr_, n=1: quando(C, "s19", fr_, n)

    def s19():
        E.frase(c, t, C["s19"], [("a", "g", 64), ("<", "g", 64), ("0:", "g", 64), ("boca", "i", 60), ("para", "i", 60), ("baixo", "g", 60)], XE, 350)
        E.frase(c, t, C["s19.a"], [("entre", "i", 60), ("as", "i", 60), ("raízes:", "i", 60), ("o", "i", 60), ("contrário", "g", 60), ("do", "i", 60), ("a", "g", 60)],
                XE, 470)
        E.foco(c, t, C["s19.a"] + 1.4, 0.4, lambda a: E.pilula(c, "positivo: lucro", XE + 200, 560, 44, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s19.b"], [("entre", "i", 60), ("2", "g", 64, ENT), ("e", "i", 60), ("10", "g", 64, ENT), ("toneladas,", "i", 60)], XE, 690)
        E.frase(c, t, Q("sem as pontas"), [("sem", "i", 60), ("as", "i", 60), ("pontas", "g", 60, ERRADO)], XE, 780)
        E.foco(c, t, Q("porque nelas"), 0.4, lambda a: E.formula(c, "L(2) = L(10) = 0", XE + 470, 780, 50, "g", TINTA2, a))
        E.foco(c, t, C["s19.c"], 0.6, lambda a: caixa_f(c, "lucro: ]2, 10[", XE + 20, 920, 72, CERTO, a))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    eixo_sim(c, t, C["s20.a"], P4, 6, ENT, 0.7)
    vertice(c, t, C["s20.c"], P4, 6, 16, ("6", "16"), abaixo=False)
    guia_h(c, t, C["s20.c"] + 0.3, P4, 6, 16, 0.8)
    fml(c, t, C["s20.a"], "x_v = f{2 + 10}{2} = 6", XE, 370, 66, ENT)
    fml(c, t, C["s20.b"], "L(6) = −36 + 72 − 20", XE, 500, 64, TINTA)
    fml(c, t, C["s20.c"], "= 16", XE + larg_f("L(6) = −36 + 72 − 20", 64) + 24, 500, 64, SAI)
    E.foco(c, t, C["s20.c"] + 0.5, 0.4, lambda a: E.escreve(c, "maior lucro: 16 mil reais", XE, 610, 54, "i", TINTA, a))
    E.foco(c, t, C["s20.d"], 0.6, lambda a: caixa_f(c, "produção: 6 toneladas", XE + 20, 780, 70, ENT, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s21.a", [("o", "i", 70), ("sinal", "i", 70), ("do", "i", 70), ("a", "g", 74, COR), ("decide", "i", 70), ("a", "i", 70), ("boca", "g", 74)]),
                 ("s21.b", [("o", "i", 70), ("vértice", "g", 74, COR), ("dá", "i", 70), ("o", "i", 70), ("máximo", "g", 74), ("ou", "i", 70), ("o", "i", 70),
                            ("mínimo", "g", 74)]),
                 ("s21.c", [("as", "i", 70), ("raízes", "g", 74, COR), ("separam", "i", 70), ("os", "i", 70), ("sinais", "g", 74)]),
                 ("s21.d", [("releia", "g", 74, COR), ("o", "i", 70), ("que", "i", 70), ("a", "i", 70), ("pergunta", "i", 70), ("pede", "g", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 50, a=a),
                                                         centro(c, str(i + 1), 240, y - 5, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 330, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s22.a"], [("a", "i", 120), ("hipérbole", "g", 130, COR)], XE, 440)
    E.foco(c, t, C["s22.a"] + 0.8, 0.5, lambda a: E.formula(c, "y = f{12}{x}", XE, 610, 100, "g", TINTA, a))
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.formula(c, "x · y = 12", XE + 440, 610, 80, "g", COR, a))
    E.frase(c, t, C["s22.c"], ps("grandezas inversamente proporcionais", "i", 54, TINTA2), XE, 760, passo=0.1)
    Q = E.plano(c, t, C["s22.a"] + 0.4, 1300, 560, 400, 280, 0, 13, 0, 13, passo=13, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, C["s22.a"] + 0.7, Q, lambda x: 12 / x, 0.95, 13, d=1.0, cor=COR, largura=9)
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
