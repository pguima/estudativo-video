"""Visual — Estudativo · MAT-RAZ-002: proporção, achar o termo desconhecido.
Peças locais: prop() desenha a proporção a/b = c/d (o x na cor da matéria); cruz() traça as duas diagonais do produto cruzado,
cada uma no seu instante, com um vão no meio para o "=" (diagonal na cor da matéria = a primeira multiplicação falada, preta =
a segunda); reto() é o erro de multiplicar na horizontal, em vermelho; copo() são os copos da receita (açúcar na cor da matéria,
farinha em preto). Instantes: cues C[...] e, dentro da frase, a palavra falada (PW, lida de audio/tempos.json)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-002_proporcao_termo_desconhecido.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("proporcao", "achar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 2 * 3 == 6 and 3 * 3 == 9 and 2 * 9 == 18 == 3 * 6
assert 3 * 8 == 6 * 4 == 24 and 24 // 3 == 8 and 8 / 6 == 4 / 3
assert 10 * 7 == 5 * 14 == 70 and 70 // 10 == 7
assert 2 * 12 == 3 * 8 == 24
assert 4 * 4.5 == 6 * 3 == 18
assert 6 * 15 == 4 * 15 * 1.5 and 6 * 10 == 4 * 15 == 60 and 10 / 4 == 5 / 2 == 15 / 6 and 5 * 2 == 10

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def _n(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


def PW(sid, palavra, n=1):
    """instante em que a voz diz a n-ésima `palavra` da cena sid"""
    for s in _TEMPOS["scenes"]:
        if s["id"] == sid:
            k = 0
            for tk in s["tokens"]:
                if _n(tk["disp"]) == _n(palavra):
                    k += 1
                    if k == n:
                        return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, n))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def troca(c, t, estados, cx, y, size):
    """equação que evolui no lugar: estados = [(t0, fórmula, cor)]; cada uma sai quando a próxima entra"""
    for i, (t0, s, cor) in enumerate(estados):
        if t < t0:
            break
        t1 = estados[i + 1][0] if i + 1 < len(estados) else 1e9
        E.saida(c, t, t1 - 0.15, lambda t0=t0, s=s, cor=cor: fcen(c, t, t0, s, cx, y, size, cor), d=0.3)


def _cor(v, cor):
    return COR if str(v) == "x" else cor


def termo(c, v, cx, cy, s, cima, cor=TINTA, a=1.0):
    """um termo da fração (em cima ou embaixo), com a mesma geometria de E.fracao"""
    v = str(v)
    y = cy - s * 0.2 if cima else cy + s * 0.9
    E.escreve(c, v, cx - E.larg(v, "g", s) / 2, y, s, "g", _cor(v, cor), a)


def frac(c, n, d, cx, cy, s, cor=TINTA, a=1.0):
    """fração com o x na cor da matéria"""
    if a <= 0:
        return
    termo(c, n, cx, cy, s, True, cor, a)
    termo(c, d, cx, cy, s, False, cor, a)
    lw = max(E.larg(str(n), "g", s), E.larg(str(d), "g", s)) + s * 0.2
    b = s * 0.085
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + s * 0.03, lw, b), b / 2, b / 2), M.paint(cor, a))


def prop(c, t, t0, n1, d1, n2, d2, xa, xb, cy, s, cor=TINTA, passo=0.35):
    """proporção n1/d1 = n2/d2: a primeira fração, o igual e a segunda entram em fila"""
    E.foco(c, t, t0, 0.5, lambda a: frac(c, n1, d1, xa, cy, s, cor, a))
    E.foco(c, t, t0 + passo, 0.45, lambda a: centro(c, "=", (xa + xb) / 2, cy + s * 0.3, s * 0.8, "g", cor, a))
    E.foco(c, t, t0 + 2 * passo, 0.5, lambda a: frac(c, n2, d2, xb, cy, s, cor, a))


def _linha_vao(c, x0, y0, x1, y1, cor, p, w, a=1.0):
    """linha com um vão no meio (onde fica o =); p = 0..1 desenha do começo ao fim"""
    if p <= 0:
        return
    for u0, u1 in ((0.0, 0.34), (0.66, 1.0)):
        if p <= u0:
            break
        u = min(p, u1)
        M.line(c, lerp(x0, x1, u0), lerp(y0, y1, u0), lerp(x0, x1, u), lerp(y0, y1, u), cor, a, w)


def diagonal(c, t, t0, xa, xb, cy, s, desce=True, cor=None, a=1.0):
    """desce=True: de cima da 1ª até embaixo da 2ª; desce=False: de baixo da 1ª até em cima da 2ª"""
    if t < t0 or a <= 0:
        return
    p = ease_io(prog(t, t0, 0.6))
    y0, y1 = (cy - s * 0.5, cy + s * 0.5) if desce else (cy + s * 0.5, cy - s * 0.5)
    _linha_vao(c, xa + s * 0.45, y0, xb - s * 0.45, y1, cor or E.COR, p, max(6, s * 0.05), a)


def reto(c, t, t0, xa, xb, cy, s, a=1.0):
    """o erro: os dois traços na horizontal (de cima com de cima, de baixo com de baixo)"""
    if t < t0 or a <= 0:
        return
    p = ease_io(prog(t, t0, 0.6))
    for y in (cy - s * 0.56, cy + s * 0.54):
        M.line(c, xa + s * 0.45, y, lerp(xa + s * 0.45, xb - s * 0.45, p), y, ERRADO, a, max(6, s * 0.05))


def copo(c, cx, base, w, h, cor, a=1.0):
    """copo: trapézio mais largo em cima, cheio da cor"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - w / 2, base - h)
    p.lineTo(cx + w / 2, base - h)
    p.lineTo(cx + w * 0.36, base)
    p.lineTo(cx - w * 0.36, base)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    M.line(c, cx - w / 2 + 6, base - h + 10, cx + w / 2 - 6, base - h + 10, BR, a * 0.45, 3)


def copos(c, t, t0, n, x, base, cor, w=56, h=78, gap=16, passo=0.07):
    for i in range(n):
        E.foco(c, t, t0 + i * passo, 0.4, lambda a, i=i: copo(c, x + i * (w + gap) + w / 2, base, w, h, cor, a))
    return n * (w + gap) - gap


def _xleft(s, i, x, size, est="g"):
    """centro x do caractere i de s escrito a partir de x"""
    pre = E.larg(s[:i], est, size) + E.APERTO[est] * size if i > 0 else 0
    return x + pre + E.larg(s[i], est, size) / 2


# ---------------- gancho ----------------
XA, XB, CY, S = 700, 1220, 470, 150  # a proporção grande no meio da tela


def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]

    def cena():
        prop(c, t, a1, "x", 6, 4, 3, XA, XB, 380, 170, passo=0.6)
        E.frase(c, t, PW("s01", "Quanto"), ps("quanto vale", "i", 84) + [("x?", "g", 84, COR)], W / 2, 700, "center", 0.12)
        E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "1 multiplicação", 660, 880, 64, "g", a=a))
        E.foco(c, t, PW("s01", "divisao") - 0.2, 0.5, lambda a: E.pilula(c, "1 divisão", 1300, 880, 64, "g", fundo=TINTA, a=a))
        E.foco(c, t, PW("s01", "divisao") - 0.4, 0.45, lambda a: centro(c, "+", 990, 902, 70, "g", TINTA2, a))
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, PW("s02", "descobre"), ps("o número", "i", 84) + [("que falta", "g", 96, COR)], XE, 490, passo=0.12)
        E.frase(c, t, PW("s02", "qualquer"), ps("em qualquer", "i", 84) + [("proporção", "g", 84, COR)], XE, 640, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "o que é", "razão"), ("s03.c", "o teste da cruz", "das frações"), ("s03.d", "equação:", "o mesmo nos dois lados"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    alvo = [x + w - 30, 360, 600, 840]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0], lerp(lerp(alvo[1], alvo[2], q1), alvo[3], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "faltar"), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52), 960, 1010, "left", 0.12)


# ---------------- proporção ----------------
def b_proporcao(c, t, C, b):
    def receita():
        a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
        E.frase(c, t, C["s04"] + 0.3, ps("duas receitas", "i", 80), W / 2, 160, "center", 0.12)
        xa, xf = 430, 430 + 6 * 72 + 70
        for k, (y, na, nf, t0, nome) in enumerate(((410, 2, 3, a4, "receita 1"), (680, 6, 9, b4, "receita 2"))):
            E.foco(c, t, t0, 0.5, lambda a, y=y, nome=nome: E.escreve(c, nome, XE, y - 20, 50, "i", TINTA2, a))
            copos(c, t, t0, na, xa, y, E.COR)
            copos(c, t, t0 + 0.6 if k == 0 else PW("s04", "nove"), nf, xf, y, TINTA)
        E.foco(c, t, a4 + 0.3, 0.5, lambda a: (E.escreve(c, "açúcar", xa, 270, 48, "g", COR, a), E.escreve(c, "farinha", xf, 270, 48, "g", TINTA, a)))
        # × 3 descendo da receita 1 para a 2
        if t >= c4:
            p = ep(t, c4, 0.6)
            M.arrow(c, 1680, 400, 1680, 600, E.COR, p, 6, 22, p)
        E.foco(c, t, c4 + 0.2, 0.5, lambda a: E.pilula(c, "× 3", 1680, 500, 64, "g", a=a))
        E.frase(c, t, PW("s04", "sabor"), ps("o sabor é", "i", 76) + [("o mesmo", "g", 76, COR)], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s05"] - 0.1, receita)

    if t < C["s05"]:
        return
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]

    def fracs():
        prop(c, t, a5, 2, 3, 6, 9, XA, XB, 420, S)
        diagonal(c, t, b6, XA, XB, 420, S, True, E.COR)
        diagonal(c, t, c6, XA, XB, 420, S, False, TINTA)
        fcen(c, t, b6 + 0.4, "2 · 9 = 18", 480, 760, 84, COR)
        fcen(c, t, c6 + 0.4, "3 · 6 = 18", 1440, 760, 84, TINTA)
        E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "deu igual: é proporção", W / 2, 910, 64, "g", fundo=CERTO, a=a))
    E.saida(c, t, e6 - 0.1, fracs)

    def nome():
        E.foco(c, t, b5, 0.5, lambda a: E.pilula(c, "proporção", W / 2, 140, 76, "g", a=a))
        E.linha(c, t, [("2", "g", 70, COR, c5), ("está para", "i", 70, TINTA, PW("s05", "esta")), ("3,", "g", 70, COR, PW("s05", "tres")),
                       ("assim como", "i", 70, TINTA, PW("s05", "assim")), ("6", "g", 70, COR, PW("s05", "seis", 2)),
                       ("está para", "i", 70, TINTA, PW("s05", "esta", 2)), ("9", "g", 70, COR, PW("s05", "nove"))], W / 2, 830, "center")
    E.saida(c, t, a6 - 0.1, nome)
    E.frase(c, t, a6, ps("produto", "g", 76, COR) + ps("cruzado", "g", 76, COR) + ps("= o teste da cruz", "i", 72), W / 2, 150, "center", 0.12)

    if t >= e6:  # meios e extremos
        s, y = 170, 560
        txt = "2 : 3 = 6 : 9"
        x0 = W / 2 - E.larg(txt, "g", s) / 2
        E.foco(c, t, e6, 0.5, lambda a: E.escreve(c, txt, x0, y, s, "g", TINTA, a))
        xs = {k: _xleft(txt, i, x0, s) for k, i in (("2", 0), ("3", 4), ("6", 8), ("9", 12))}
        te, tm = PW("s06", "extremos", 2), PW("s06", "meios", 2)

        def arco(xa, xb, ycur, alto, t0, cor):
            p = ep(t, t0, 0.7)
            if p <= 0:
                return
            mx, my = (xa + xb) / 2, ycur + alto
            pts = [(lerp(lerp(xa, mx, u), lerp(mx, xb, u), u), lerp(lerp(ycur, my, u), lerp(my, ycur, u), u)) for u in [p * j / 30 for j in range(31)]]
            path = skia.Path(); path.moveTo(*pts[0])
            for px, py in pts[1:]:
                path.lineTo(px, py)
            c.drawPath(path, M.paint(cor, 1.0, stroke=7, cap_round=True))
        arco(xs["2"], xs["9"], y - s * 0.85, -170, te, E.COR)
        E.foco(c, t, te + 0.4, 0.5, lambda a: E.pilula(c, "extremos", W / 2, y - s * 0.85 - 90, 56, "g", a=a))
        arco(xs["3"], xs["6"], y + 40, 150, tm, TINTA)
        E.foco(c, t, tm + 0.4, 0.5, lambda a: E.pilula(c, "meios", W / 2, y + 40 + 80, 56, "g", fundo=TINTA, a=a))
        E.foco(c, t, PW("s06", "produto", 2) - 0.2, 0.5, lambda a: centro(c, "produto dos meios = produto dos extremos", W / 2, 940, 54, "i", TINTA2, a))


# ---------------- achar o x ----------------
def b_achar(c, t, C, b):
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8, c8, d8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"]
    a9, b9 = C["s09.a"], C["s09.b"]

    def parte1():
        cy = 400
        x8 = t >= a9  # o x vira 8 na conferência
        E.foco(c, t, a7, 0.5, lambda a: frac(c, 8 if x8 else "x", 6, XA, cy, S, TINTA, a))
        E.foco(c, t, a7 + 0.4, 0.45, lambda a: centro(c, "=", (XA + XB) / 2, cy + S * 0.3, S * 0.8, "g", TINTA, a))
        E.foco(c, t, a7 + 0.8, 0.5, lambda a: frac(c, 4, 3, XB, cy, S, TINTA, a))
        E.saida(c, t, a8 - 0.1, lambda: E.frase(c, t, b7, ps("a cruz tem que", "i", 72) + [("dar igual", "g", 72, COR)], W / 2, 780, "center", 0.12))

        def cruz_contas():
            diagonal(c, t, a8, XA, XB, cy, S, True, E.COR)
            diagonal(c, t, b8, XA, XB, cy, S, False, TINTA)
            fcen(c, t, a8 + 0.3, "3 · x", 470, 720, 90, COR)
            fcen(c, t, b8 + 0.3, "6 · 4", 1450, 720, 90, TINTA)
            troca(c, t, [(c8, "3x = 24", TINTA)], 760, 900, 100)
            E.foco(c, t, d8, 0.5, lambda a: E.pilula(c, "÷ 3 nos dois lados", 1200, 868, 46, "g", fundo=TINTA, a=a))
            bola_res(c, t, e8, "x = 8", 1640, 860, 110, 72)
        E.saida(c, t, a9 - 0.1, cruz_contas)
        # conferência: 8/6 = 4/3
        E.foco(c, t, a9, 0.5, lambda a: frac(c, 8, 6, 720, 790, 110, TINTA, a))
        E.pontes(c, t, 820, 1020, 790, 110, "÷ 2", PW("s09", "dividindo"), PW("s09", "dividindo") + 0.4, size=42)
        E.foco(c, t, b9, 0.5, lambda a: frac(c, 4, 3, 1120, 790, 110, CERTO, a))
        E.foco(c, t, PW("s09", "Bateu"), 0.5, lambda a: E.selo(c, 1380, 780, 60, True, a))
    E.saida(c, t, C["s10"] - 0.1, parte1)

    if C["s10"] <= t < C["s11"] + 0.5:
        E.saida(c, t, C["s11"] - 0.1, lambda: balanca(c, t, C))

    if t >= C["s11"]:
        a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
        E.frase(c, t, C["s11"] + 0.3, ps("o", "i", 76) + [("x", "g", 76, COR)] + ps("pode estar", "i", 76) + [("embaixo", "g", 76, COR)], W / 2, 160, "center", 0.12)
        prop(c, t, a11, 5, "x", 10, 14, XA, XB, 420, S)
        diagonal(c, t, b11, XA, XB, 420, S, False, E.COR)
        diagonal(c, t, PW("s11", "cinco", 2), XA, XB, 420, S, True, TINTA)
        troca(c, t, [(b11, "10x = 5 · 14", TINTA), (PW("s11", "setenta"), "10x = 70", TINTA), (c11, "x = 70 ÷ 10", TINTA)], 800, 820, 100)
        bola_res(c, t, PW("s11", "sete"), "x = 7", 1500, 790, 110, 72)


def balanca(c, t, C):
    """por que a cruz vale: x/6 · 6 · 3 = 4/3 · 6 · 3; o 6 de baixo some de um lado, o 3 do outro"""
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    E.frase(c, t, C["s10"] + 0.2, ps("por que a cruz vale?", "i", 76) + [("a balança", "g", 76, COR)], W / 2, 170, "center", 0.12)
    s, cy = 120, 440
    tm = PW("s10", "multiplique")
    yb = cy + s * 0.36
    E.foco(c, t, a10 - 0.2, 0.5, lambda a: frac(c, "x", 6, 380, cy, s, TINTA, a))
    E.foco(c, t, a10 - 0.2, 0.5, lambda a: centro(c, "=", 900, cy + s * 0.3, s * 0.8, "g", TINTA, a))
    E.foco(c, t, a10 - 0.2, 0.5, lambda a: frac(c, 4, 3, 1110, cy, s, TINTA, a))
    mult = "· 6 · 3"
    xl, xr = 470, 1200
    E.foco(c, t, tm + 0.6, 0.5, lambda a: (E.escreve(c, mult, xl, yb, s, "g", COR, a), E.escreve(c, mult, xr, yb, s, "g", COR, a)))
    # lado do x: o 6 de baixo e o · 6 somem
    E.risco(c, 380 - s * 0.32, cy + s * 0.95, 380 + s * 0.32, cy + s * 0.1, t, b10, ERRADO, 10)
    x6 = _xleft(mult, 2, xl, s)
    E.risco(c, x6 - s * 0.3, yb + 10, x6 + s * 0.3, yb - s * 0.8, t, b10 + 0.15, ERRADO, 10)
    fcen(c, t, PW("s10", "fica") + 0.2, "3 · x", 600, 740, 100, COR)
    # outro lado: o 3 de baixo e o · 3 somem
    t3 = PW("s10", "tres", 3)
    E.risco(c, 1110 - s * 0.32, cy + s * 0.95, 1110 + s * 0.32, cy + s * 0.1, t, t3, ERRADO, 10)
    x3 = _xleft(mult, 6, xr, s)
    E.risco(c, x3 - s * 0.3, yb + 10, x3 + s * 0.3, yb - s * 0.8, t, t3 + 0.15, ERRADO, 10)
    fcen(c, t, PW("s10", "fica", 2) + 0.2, "6 · 4", 1330, 740, 100, TINTA)
    E.foco(c, t, c10, 0.5, lambda a: E.pilula(c, "sobra a cruz: 3 · x = 6 · 4", W / 2, 920, 64, "g", a=a))


# ---------------- de volta à receita ----------------
def b_receita(c, t, C, b):
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    E.frase(c, t, C["s12"] + 0.3, ps("de volta à", "i", 76) + [("receita", "g", 76, COR)], W / 2, 150, "center", 0.12)
    copos(c, t, a12, 8, 300, 360, E.COR)
    E.foco(c, t, a12 + 0.5, 0.5, lambda a: E.escreve(c, "8 de açúcar", 300, 450, 54, "g", COR, a))
    E.foco(c, t, PW("s12", "quantos"), 0.5, lambda a: (E.escreve(c, "? de farinha", 1050, 450, 54, "g", TINTA, a),
                                                       centro(c, "?", 1200, 350, 120, "g", CINZA, a)))
    cy = 640
    E.foco(c, t, b12 - 0.2, 0.5, lambda a: (E.escreve(c, "açúcar", 380, cy - 40, 44, "i", COR, a), E.escreve(c, "farinha", 380, cy + 100, 44, "i", TINTA, a)))
    prop(c, t, b12, 2, 3, 8, "x", 680, 1080, cy, 130, passo=0.6)
    diagonal(c, t, c12, 680, 1080, cy, 130, True, E.COR)
    diagonal(c, t, PW("s12", "tres", 2), 680, 1080, cy, 130, False, TINTA)
    troca(c, t, [(c12, "2x = 3 · 8", TINTA), (PW("s12", "vinte"), "2x = 24", TINTA)], 1460, 680, 96)
    bola_res(c, t, d12, "x = 12", 1460, 880, 120, 70)
    E.foco(c, t, PW("s12", "copos", 3), 0.5, lambda a: E.escreve(c, "copos de farinha", 1600, 1010, 44, "i", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.saida(c, t, C["s14"] - 0.1, lambda: E.frase(c, t, C["s13"] + 0.3, ps("o erro:", "i", 84) + [("multiplicar reto", "g", 84, ERRADO)], W / 2, 170, "center", 0.12))
    E.frase(c, t, C["s14"] + 0.2, ps("dá para ver", "i", 84) + [("sem conta", "g", 84, COR)], W / 2, 170, "center", 0.12)
    cy = 420
    prop(c, t, PW("s13", "xis"), "x", 6, 4, 3, XA, XB, cy, S)
    reto(c, t, b13, XA, XB, cy, S, 1 - ep(t, c14, 0.4))

    def contas():
        fcen(c, t, b13 + 0.2, "x · 4 = 6 · 3", 700, 760, 90, ERRADO)
        fcen(c, t, c13, "4x = 18", 700, 900, 90, ERRADO)
        E.foco(c, t, d13, 0.5, lambda a: E.pilula(c, "x = 4,5", 1350, 870, 76, "g", fundo=ERRADO, a=a))
    E.saida(c, t, a14 - 0.1, contas)
    E.foco(c, t, a14, 0.5, lambda a: E.pilula(c, "x < 6: menor que 1", XA - 40, 730, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, b14, 0.5, lambda a: E.pilula(c, "maior que 1", XB + 60, 730, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, b14 + 0.6, 0.45, lambda a: centro(c, "≠", (XA + XB) / 2 + 10, 755, 90, "g", ERRADO, a))
    diagonal(c, t, c14 + 0.2, XA, XB, cy, S, True, E.COR)
    diagonal(c, t, c14 + 0.5, XA, XB, cy, S, False, E.COR)
    E.frase(c, t, PW("s14", "liga"), ps("a cruz liga", "i", 64) + [("o de cima", "g", 64, COR)] + ps("de uma com", "i", 64) + [("o de baixo", "g", 64, COR)] + ps("da outra", "i", 64),
            W / 2, 920, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def fator():
        a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, C["s15"] + 0.3, ps("o atalho:", "i", 80, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, a15, ps("procure o", "i", 96, CLARO) + [("fator", "g", 96, BR)], W / 2, 300, "center", 0.12)
        xa, xb, cy, s = 700, 1220, 590, 150
        xx = t >= c15 + 0.3
        E.foco(c, t, PW("s15", "xis"), 0.5, lambda a: ((termo(c, "x", xa, cy, s, True, BR, a) if not xx else None), termo(c, 6, xa, cy, s, False, BR, a),
                                                       c.drawRect(skia.Rect.MakeXYWH(xa - 70, cy - 6, 140, 13), M.paint(BR, a))))
        if xx:
            E.foco(c, t, c15 + 0.3, 0.5, lambda a: termo(c, 8, xa, cy, s, True, CLARO, a))
        E.foco(c, t, PW("s15", "xis") + 0.3, 0.45, lambda a: centro(c, "=", (xa + xb) / 2, cy + s * 0.3, s * 0.7, "g", BR, a))
        E.foco(c, t, PW("s15", "xis") + 0.6, 0.5, lambda a: E.fracao(c, 4, 3, xb, cy, s, BR, a))
        E.ponte(c, t, b15, xb - 110, xa + 110, cy + s * 0.535, "× 2", CLARO, 40)
        E.ponte(c, t, c15 - 0.2, xb - 110, xa + 110, cy - s * 0.565, "× 2", CLARO, 40)
        E.foco(c, t, PW("s15", "Sem"), 0.5, lambda a: E.pilula(c, "sem equação", W / 2, 920, 64, "g", a=a))
    E.saida(c, t, C["s16"] - 0.1, fator)

    if t >= C["s16"]:
        a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
        E.frase(c, t, a16, ps("proporção =", "i", 84, CLARO) + ps("fração equivalente", "g", 84, BR), W / 2, 250, "center", 0.12)
        E.frase(c, t, PW("s16", "o"), ps("o que multiplica embaixo,", "i", 60, CLARO) + ps("multiplica em cima", "g", 60, BR), W / 2, 360, "center", 0.1)
        E.foco(c, t, b16, 0.5, lambda a: E.pilula(c, "fator não inteiro", 560, 600, 60, "g", fundo=ERRADO, cor=BR, a=a))
        tq = PW("s16", "quatro")
        E.foco(c, t, tq, 0.5, lambda a: centro(c, "4", 1100, 640, 120, "g", BR, a))
        if t >= tq + 0.3:
            p = ep(t, tq + 0.3, 0.5)
            M.arrow(c, 1170, 600, 1390, 600, CLARO, p, 5, 18, p)
        E.foco(c, t, tq + 0.3, 0.4, lambda a: centro(c, "× ?", 1280, 560, 50, "g", CLARO, a))
        E.foco(c, t, PW("s16", "seis"), 0.5, lambda a: centro(c, "6", 1460, 640, 120, "g", BR, a))
        E.frase(c, t, c16, ps("aí,", "i", 110, CLARO) + ps("vá de cruz", "g", 120, BR), W / 2, 880, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, PW("s17", "Ache"), ps("ache o", "i", 84) + [("x", "g", 84, COR)], XE, 340, passo=0.12)
    prop(c, t, C["s17.a"], "x", 4, 15, 6, 400, 800, 600, 170, passo=0.5)
    E.relogio(c, t, C["s18.a"], 1450, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]

    def cruz19():
        cy = 400
        prop(c, t, C["s19"] + 0.2, "x", 4, 15, 6, XA, XB, cy, S, passo=0.2)
        E.foco(c, t, PW("s19", "quatro"), 0.5, lambda a: E.pilula(c, "4 → 6: fator não inteiro", W / 2, 170, 50, "g", fundo=TINTA, a=a))
        diagonal(c, t, a19 - 0.1, XA, XB, cy, S, True, E.COR)
        diagonal(c, t, PW("s19", "quatro", 2), XA, XB, cy, S, False, TINTA)
        troca(c, t, [(b19, "6x = 4 · 15", TINTA), (PW("s19", "sessenta"), "6x = 60", TINTA), (c19, "x = 60 ÷ 6", TINTA)], 800, 820, 100)
        bola_res(c, t, PW("s19", "dez"), "x = 10", 1500, 790, 120, 72, CERTO)
    E.saida(c, t, C["s20"] - 0.1, cruz19)

    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"] + 0.3, ps("conferindo", "i", 72, COR), W / 2, 150, "center")

    def conf():
        s = 110
        E.foco(c, t, a20, 0.5, lambda a: frac(c, 10, 4, 400, 330, s, TINTA, a))
        E.pontes(c, t, 500, 680, 330, s, "÷ 2", PW("s20", "dividindo"), PW("s20", "dividindo") + 0.3, size=40)
        E.foco(c, t, PW("s20", "cinco"), 0.5, lambda a: frac(c, 5, 2, 770, 330, s, CERTO, a))
        E.foco(c, t, b20, 0.5, lambda a: frac(c, 15, 6, 400, 640, s, TINTA, a))
        E.pontes(c, t, 500, 680, 640, s, "÷ 3", PW("s20", "dividindo", 2), PW("s20", "dividindo", 2) + 0.3, size=40)
        E.foco(c, t, PW("s20", "mesmo"), 0.5, lambda a: frac(c, 5, 2, 770, 640, s, CERTO, a))
    conf()
    # o fator: 5/2 = x/4, de 2 para 4 é × 2
    xa, xb, cy, s = 1180, 1700, 480, 130
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "achou o fator", 1435, 230, 50, "g", a=a))
    ok = t >= d20
    E.foco(c, t, c20 + 0.2, 0.5, lambda a: (frac(c, 5, 2, xa, cy, s, TINTA, a), centro(c, "=", (xa + xb) / 2, cy + s * 0.3, s * 0.7, "g", TINTA, a),
                                            termo(c, 4, xb, cy, s, False, TINTA, a),
                                            c.drawRect(skia.Rect.MakeXYWH(xb - 50, cy - 5, 100, 11), M.paint(TINTA, a))))
    if not ok:
        E.foco(c, t, c20 + 0.2, 0.5, lambda a: termo(c, "x", xb, cy, s, True, TINTA, a))
    E.ponte(c, t, PW("s20", "dois", 3), xa + 70, xb - 100, cy + s * 0.535, "× 2", None, 36)
    E.ponte(c, t, PW("s20", "Cinco", 2), xa + 70, xb - 100, cy - s * 0.565, "× 2", None, 36)
    E.foco(c, t, d20, 0.5, lambda a: (E.bola(c, xb, cy - s * 0.47, 78, CERTO, a), centro(c, "10", xb, cy - s * 0.2, s * 0.8, "g", BR, a)))
    E.foco(c, t, d20 + 0.3, 0.5, lambda a: centro(c, "o mesmo 10", 1435, 860, 60, "g", CERTO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s21.a", "proporção = razão igual a razão"), ("s21.b", "com a cruz, vira equação"))
        for i, (k, s) in enumerate(itens):
            y = 470 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 360, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a22, b22, c22, d22 = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, a22, ps("o truque do", "i", 110) + [("k", "g", 150, COR)], XE, 480, passo=0.15)
    E.frase(c, t, b22, ps("razão", "i", 70) + [("3 para 5,", "g", 70, COR)] + ps("soma", "i", 70) + [("64", "g", 70, COR)], XE, 640, passo=0.12)
    E.foco(c, t, c22, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, c22 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, c22 + 0.2, 0.4))
    E.frase(c, t, d22, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, proporcao=b_proporcao, achar=b_achar, receita=b_receita, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
