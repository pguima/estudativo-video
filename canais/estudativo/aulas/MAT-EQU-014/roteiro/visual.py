"""Visual — Estudativo · MAT-EQU-014: comparar dois planos.
Plano A = 40 + 0,5x, plano B = 20 + x; empate em 40 minutos (R$ 60). Questão: táxi 5 + 3x = 11 + 2,5x, x = 12 (R$ 41).
Instantes: cues C[...] e, para números ditos no meio da frase, pal(cena, palavra) lê o instante da palavra na voz real."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, passo, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-014_comparar_dois_planos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conta", "equacao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula
A_, B_ = (lambda m: 40 + 0.5 * m), (lambda m: 20 + m)
assert (A_(0), B_(0), A_(20), B_(20), A_(60), B_(60)) == (40, 20, 50, 40, 70, 80)
assert A_(40) == B_(40) == 60 and (40 - 20) / (1 - 0.5) == 40
assert 5 + 3 * 12 == 11 + 2.5 * 12 == 41 and (11 - 5) / (3 - 2.5) == 12


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- instante de uma palavra na voz ----------------
_T = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_TOK = {s["id"]: (s["start"], s["tokens"]) for s in _T["scenes"]}


def pal(sid, palavra, n=1):
    """instante em que a n-ésima ocorrência de `palavra` começa na cena sid"""
    st, toks = _TOK[sid]
    k = 0
    for tk in toks:
        if tk["disp"].lower().strip(".,:;!?") == palavra:
            k += 1
            if k == n:
                return st + tk["t0"]
    raise KeyError((sid, palavra, n))


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def cartao(c, x, y, w, h, a, cor=FIO):
    if a > 0:
        M.rrect(c, x, y, w, h, 30, E.VAZIO, a, stroke=4, stroke_color=cor)


def letra(c, t, t0, s, cx, cy, r, cor=None):
    """letra do plano numa esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + r * 0.36, r * 1.0, "g", E.SOBRE, a)))


def igualdade(c, a, esq, dir_, y, size, cor=None, xm=W / 2):
    """equação alinhada pelo sinal de igual em xm"""
    g = size * 0.45
    E.formula(c, esq, xm - g, y, size, "g", cor, a, "right")
    centro(c, "=", xm, y, size, "g", cor, a)
    E.formula(c, dir_, xm + g, y, size, "g", cor, a)


def pilha(c, t, linhas, ops, xm, y0, dy, size, fim=None):
    """resolução em linhas: linhas = [(t0, esq, dir)], ops = [(t0, op)] escrita sob os dois lados, entre a linha k e a k+1.
    A linha antiga fica cinza quando a nova chega; a última fica na cor da matéria."""
    g = size * 0.45
    for k, (t0, esq, dir_) in enumerate(linhas):
        y = y0 + k * dy
        ult = k == len(linhas) - 1
        velha = not ult and t >= linhas[k + 1][0]
        cor = COR if ult else (CINZA if velha else TINTA)
        E.foco(c, t, t0, 0.5, lambda a, esq=esq, dir_=dir_, y=y, cor=cor: igualdade(c, a, esq, dir_, y, size, cor, xm))
        if ult and fim is not None:
            pass
        if k < len(ops):
            to, op = ops[k]
            we = E.formula(c, esq, 0, 0, size, a=0)
            wd = E.formula(c, dir_, 0, 0, size, a=0)
            cop = CINZA if velha else COR
            yo = y + size * 0.72
            for cx in (xm - g - we / 2, xm + g + wd / 2):
                E.foco(c, t, to, 0.45, lambda a, cx=cx, cop=cop: E.formula(c, op, cx, yo, size * 0.52, "b", cop, a, "center"), sobe=8)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]

    def planos():
        for x, k, nome, fixo, minuto, tf, tm in ((150, ka, "A", "R$ 40", "+ R$ 0,50", pal("s01", "quarenta"), pal("s01", "cinquenta")),
                                                 (990, kb, "B", "R$ 20", "+ R$ 1", pal("s01", "vinte"), pal("s01", "um"))):
            y, w, h = 150, 780, 420
            E.foco(c, t, k, 0.5, lambda a, x=x: cartao(c, x, y, w, h, a), blur=4)
            letra(c, t, k + 0.1, nome, x + 90, y + 95, 52)
            E.frase(c, t, k + 0.2, ps("plano", "i", 72), x + 165, y + 120)
            E.frase(c, t, tf, [(fixo, "g", 130, TINTA)] + ps("por mês", "i", 64), x + 60, y + 270, passo=0.15)
            E.frase(c, t, tm, [(minuto, "g", 88, COR)] + ps("por minuto", "i", 60, COR), x + 60, y + 375, passo=0.15)
        E.frase(c, t, kc, ps("qual é", "i", 100) + [("mais barato?", "g", 100, COR)], W / 2, 760, "center", 0.14)

        def duvida():
            E.frase(c, t, a2 - 1.2, ps("responder", "i", 72) + [("B", "g", 80)] + ps("na hora pode", "i", 72) + [("pagar mais caro", "g", 80, ERRADO)], W / 2, 880, "center", 0.1)
        if t < b2 + 0.4:
            E.saida(c, t, b2 - 0.1, duvida)
        E.frase(c, t, b2 + 0.2, ps("a resposta", "i", 72) + [("depende de quanto você fala", "g", 80, COR)], W / 2, 880, "center", 0.12)
        E.frase(c, t, c2, ps("valores inventados para a aula", "i", 48, TINTA2), W / 2, 990, "center", 0.08)

    E.saida(c, t, C["s03"] - 0.1, planos)
    if t >= C["s03"]:
        ta, tb = C["s03.a"], C["s03.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 540, 230 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, pal("s03", "quantos"), ps("com", "i", 90) + [("quantos minutos", "g", 100, COR)], XE, 460, passo=0.14)
        E.frase(c, t, pal("s03", "dois"), ps("dois planos", "i", 84) + [("custam o mesmo", "g", 84)], XE, 600, passo=0.14)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1560, 525, 76, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 610, 76, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s04"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s04.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s04.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s04.b", "montar a equação", "de um problema"), ("s04.c", "resolver equação com", "x dos dois lados"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    py = lerp(410, 670, ease_io(prog(t, C["s04.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s04.b"], 0.4))
    E.frase(c, t, pal("s04", "se"), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 960, 800, "left", 0.12)


# ---------------- a conta de cada plano ----------------
def b_conta(c, t, C, b):
    def incognita():
        E.frase(c, t, C["s05"] + 0.2, ps("o que você não sabe:", "i", 84), W / 2, 330, "center", 0.12)
        E.frase(c, t, C["s05.a"], [("quantos minutos", "g", 110, COR)] + ps("vai falar", "i", 100), W / 2, 500, "center", 0.14)
        kb = C["s05.b"]
        E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "minutos", 760, 730, 80, "i", a=a, cor=E.SOBRE))
        E.foco(c, t, kb + 0.3, 0.5, lambda a: M.arrow(c, 960, 732, 1110, 732, TINTA, a, 6, 20))
        E.foco(c, t, pal("s05", "xis"), 0.5, lambda a: (E.bola(c, 1240, 730, 90, a=a), centro(c, "x", 1240, 768, 120, "g", E.SOBRE, a)))
    E.saida(c, t, C["s06"] - 0.1, incognita)
    if t < C["s06"]:
        return
    # plano A
    x0 = XE + 150
    letra(c, t, pal("s06", "plano"), "A", XE + 40, 270, 56)
    E.linha(c, t, [("R$ 40", "g", 72, TINTA, pal("s06", "quarenta")), ("fixos", "i", 68, TINTA, pal("s06", "fixos")),
                   ("+ R$ 0,50", "g", 72, TINTA, pal("s06", "cinquenta")), ("a cada minuto", "i", 68, TINTA, pal("s06", "cada"))], x0, 295)
    E.formula_em(c, t, C["s06.a"], "40 + 0,5x", x0, 470, 140, "g", COR)
    # plano B
    kb, kc = C["s06.b"], C["s06.c"]
    letra(c, t, pal("s06", "plano", 2), "B", XE + 40, 700, 56)
    um = lambda: E.formula(c, "20 + 1x", x0, 900, 140, "g", COR)
    if t < kc + 0.4:
        E.foco(c, t, kb, 0.5, lambda a: E.saida(c, t, kc, um))
    E.formula_em(c, t, kc + 0.3, "20 + x", x0, 900, 140, "g", COR)
    E.frase(c, t, kc + 0.4, [("1x", "g", 72, TINTA2)] + ps("é o mesmo que", "i", 68, TINTA2) + [("x", "g", 72, TINTA2)], 1010, 880, "left", 0.1)


# ---------------- tabela ----------------
def b_tabela(c, t, C, b):
    ka, kb, kc = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    xs = (420, 960, 1440)
    E.foco(c, t, ka, 0.5, lambda a: (centro(c, "minutos", xs[0], 290, 64, "i", TINTA, a),
                                     E.formula(c, "40 + 0,5x", xs[1], 290, 72, "g", COR, a, "center"),
                                     E.formula(c, "20 + x", xs[2], 290, 72, "g", COR, a, "center")))
    E.foco(c, t, ka, 0.5, lambda a: (centro(c, "plano A", xs[1], 190, 56, "i", TINTA2, a), centro(c, "plano B", xs[2], 190, 56, "i", TINTA2, a)))
    if t >= ka:
        M.line(c, 220, 340, 1700, 340, TINTA, 1.0, 4, progress=ep(t, ka, 0.6))
    linhas = ((450, "0", kb, "40", pal("s07", "quarenta"), "20", pal("s07", "vinte"), 2, pal("s07", "ganha")),
              (600, "20", kc, "50", pal("s07", "cinquenta"), "40", pal("s07", "quarenta", 2), 2, pal("s07", "ganha", 2)),
              (900, "60", a8, "70", pal("s08", "setenta"), "80", pal("s08", "oitenta"), 1, b8))
    for y, m, tm, va, ta, vb, tb, ganha, tg in linhas:
        cen(c, t, tm, m, xs[0], y, 92, TINTA)
        if t >= tg:
            xg = xs[ganha]
            E.foco(c, t, tg, 0.4, lambda a, xg=xg, y=y: M.rrect(c, xg - 150, y - 92, 300, 120, 24, CERTO, 0.16 * a), blur=4)
        cen(c, t, ta, va, xs[1], y, 92, CERTO if (ganha == 1 and t >= tg) else TINTA)
        cen(c, t, tb, vb, xs[2], y, 92, CERTO if (ganha == 2 and t >= tg) else TINTA)
        E.frase(c, t, tg, ps(("B ganha" if ganha == 2 else "virou!"), "i", 56, CERTO), 1620, y - 20)
    E.frase(c, t, pal("s08", "agora"), ps("A ganha", "i", 56, CERTO), 1620, 960, passo=0.1)
    # a linha do meio: o empate ainda sem número
    p = ep(t, c8, 0.5)
    if p > 0:
        E.caixa_pontilhada(c, 240, 680, 1440, 130, p, prog_=p)
        E.frase(c, t, c8 + 0.2, [("?", "g", 92, COR)], xs[0] - 20, 778)
        E.frase(c, t, c8 + 0.5, ps("custam", "i", 68, COR) + [("o mesmo", "g", 72, COR)], (xs[1] + xs[2]) / 2, 770, "center", 0.12)


# ---------------- a equação ----------------
def b_equacao(c, t, C, b):
    def nome():
        a9, b9 = C["s09.a"], C["s09.b"]
        E.frase(c, t, a9, [("ponto de equilíbrio", "g", 130, COR)], W / 2, 360, "center")
        E.frase(c, t, pal("s09", "onde"), ps("onde os preços ficam", "i", 84) + [("iguais", "g", 90)], W / 2, 500, "center", 0.12)
        E.frase(c, t, b9 - 0.1, ps("conta de A", "g", 90) + [("=", "g", 110, COR)] + ps("conta de B", "g", 90), W / 2, 760, "center", 0.16)
    E.saida(c, t, C["s10"] - 0.1, nome)

    def resolve():
        E.frase(c, t, pal("s10", "vamos"), ps("x de um lado só", "i", 64, TINTA2), W / 2, 120, "center", 0.12)
        linhas = ((C["s10.a"], "40 + 0,5x", "20 + x"), (C["s10.c"], "40", "20 + 0,5x"), (C["s11.b"], "20", "0,5x"), (C["s11.e"], "x", "40"))
        ops = ((C["s10.b"], "− 0,5x"), (C["s11.a"], "− 20"), (C["s11.c"], "÷ 0,5"))
        pilha(c, t, linhas, ops, W / 2, 260, 190, 104)
        E.frase(c, t, C["s11.d"] - 1.0, [("÷ 0,5", "g", 80, COR)] + ps("é o mesmo que", "i", 72) + [("× 2", "g", 80, COR)], W / 2, 1010, "center", 0.14)
        E.foco(c, t, C["s11.e"] + 0.3, 0.5, lambda a: M.rrect(c, W / 2 - 230, 830 - 120, 460, 160, 30, COR, 0.12 * a), blur=4)
    if C["s10"] - 0.1 <= t:
        E.saida(c, t, C["s12"] - 0.1, resolve)

    def confere():
        a2, b2, c2, d2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
        E.foco(c, t, a2, 0.5, lambda a: (E.bola(c, 640, 250, 120, a=a), centro(c, "40", 640, 292, 120, "g", E.SOBRE, a)))
        E.frase(c, t, a2 + 0.3, [("minutos", "i", 110)], 800, 285)
        letra(c, t, b2 - 0.5, "A", XE + 40, 500, 50)
        E.linha(c, t, [("40 + 0,5 × 40", "g", 90, TINTA, b2 - 0.3), ("= 40 + 20", "g", 90, TINTA, pal("s12", "quarenta", 2)),
                       ("= R$ 60", "g", 90, COR, pal("s12", "sessenta"))], XE + 120, 532)
        letra(c, t, c2 - 0.5, "B", XE + 40, 690, 50)
        E.linha(c, t, [("20 + 40", "g", 90, TINTA, pal("s12", "vinte", 2)), ("= R$ 60", "g", 90, COR, pal("s12", "sessenta", 2))], XE + 120, 722)
        E.foco(c, t, d2, 0.5, lambda a: E.selo(c, 820, 890, 64, True, a))
        E.frase(c, t, d2 + 0.1, [("bateu!", "g", 100, CERTO)], 910, 925)
    if C["s12"] - 0.1 <= t:
        E.saida(c, t, C["s13"] - 0.1, confere)
    if t < C["s13"]:
        return
    a3, b3 = C["s13.a"], C["s13.b"]
    E.frase(c, t, C["s13"] + 0.2, ps("a tabela conta o", "i", 84) + [("resto da história", "g", 84, COR)], W / 2, 190, "center", 0.12)
    x0, x1, y = 260, 1660, 600
    vx = lambda v: x0 + v / 80 * (x1 - x0)
    E.foco(c, t, a3, 0.5, lambda a: M.rrect(c, vx(0), y - 50, vx(40) - vx(0), 100, 14, COR, 0.16 * a), blur=4)
    E.foco(c, t, b3, 0.5, lambda a: M.rrect(c, vx(40), y - 50, vx(80) - vx(40), 100, 14, CERTO, 0.16 * a), blur=4)
    E.reta(c, t, C["s13"] + 0.2, x0, x1, y, 0, 80, (0, 20, 40, 60, 80), lambda v: f"{v} min", size=56)
    E.foco(c, t, C["s13"] + 0.6, 0.5, lambda a: E.pilula(c, "empate: R$ 60", vx(40), 440, 56, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, a3, ps("antes:", "i", 62) + [("B mais barato", "g", 66, COR)], vx(20), 800, "center", 0.12)
    E.frase(c, t, b3, ps("depois:", "i", 62) + [("A mais barato", "g", 66, CERTO)], vx(60), 800, "center", 0.12)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, C["s14"] + 0.3, ps("cuidado com o", "i", 80) + [("erro mais comum", "g", 80, ERRADO)], W / 2, 160, "center", 0.12)
    E.frase(c, t, ka, ps("olhar só", "i", 96) + [("a mensalidade", "g", 100, ERRADO)], W / 2, 320, "center", 0.14)
    E.frase(c, t, pal("s14", "vinte"), [("R$ 20", "g", 90)] + ps("é menos que", "i", 76) + [("R$ 40", "g", 90)], W / 2, 480, "center", 0.14)
    E.frase(c, t, pal("s14", "escolhe") - 0.2, ps("então escolhe", "i", 76) + [("B", "g", 90, ERRADO)], W / 2, 590, "center", 0.12)
    E.frase(c, t, pal("s14", "com"), ps("com", "i", 76) + [("60 minutos", "g", 80)], W / 2, 720, "center", 0.12)
    E.frase(c, t, kb - 0.3, ps("paga", "i", 80) + [("R$ 80", "g", 110, ERRADO)], 640, 860, "center", 0.12)
    E.frase(c, t, kc - 0.3, ps("poderia pagar", "i", 80) + [("R$ 70", "g", 110, CERTO)], 1300, 860, "center", 0.12)
    E.frase(c, t, kd, ps("quem fala muito sente o peso do", "i", 60) + [("minuto mais caro", "g", 64, COR)], W / 2, 990, "center", 0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        ka, kb, kc, kd = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, C["s15"] + 0.3, ps("agora, o atalho", "i", 76, CLARO), W / 2, 130, "center", 0.11)
        E.foco(c, t, ka, 0.5, lambda a: centro(c, "diferença das mensalidades", W / 2, 290, 76, "g", BR, a))
        E.foco(c, t, pal("s15", "dividida"), 0.5, lambda a: M.rrect(c, W / 2 - 520, 322, 1040, 9, 4, CLARO, a))
        E.foco(c, t, pal("s15", "diferença", 2), 0.5, lambda a: centro(c, "diferença do minuto", W / 2, 415, 76, "g", BR, a))
        E.linha(c, t, [("mensalidades:", "i", 68, CLARO, kb - 0.2), ("40 − 20 =", "g", 84, BR, kb), ("R$ 20", "g", 84, CLARO, pal("s15", "vinte", 2))], 330, 600)
        E.linha(c, t, [("minuto:", "i", 68, CLARO, kc - 0.2), ("1 − 0,50 =", "g", 84, BR, kc), ("R$ 0,50", "g", 84, CLARO, pal("s15", "cinquenta", 2))], 330, 740)
        E.linha(c, t, [("20 ÷ 0,5 =", "g", 110, BR, kd), ("40", "g", 140, CLARO, pal("s15", "quarenta", 2)), ("minutos", "i", 96, CLARO, pal("s15", "minutos"))], W / 2, 940, "center")
    E.saida(c, t, C["s16"] - 0.1, regra)
    if t < C["s16"]:
        return
    ka, kb, kc, kd, ke = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
    E.frase(c, t, ka - 0.4, ps("B começa", "i", 76, CLARO) + [("R$ 20 mais barato", "g", 80, BR)], XE, 190, "left", 0.12)
    # a vantagem de B encolhendo minuto a minuto, até zero em 40 minutos
    m = 40 * ease_io(prog(t, kb + 0.6, (kc - 0.1) - (kb + 0.6)))
    v = 20 - 0.5 * m
    x0, x1, yb = XE, 1750, 260
    E.foco(c, t, ka + 0.3, 0.5, lambda a: (M.rrect(c, x0, yb, x1 - x0, 90, 20, BR, 0.08 * a),
                                           M.rrect(c, x0, yb, max(1, (x1 - x0) * v / 20), 90, 20, CLARO, a) if v > 0.01 else None), blur=4)
    E.foco(c, t, ka + 0.5, 0.5, lambda a: E.escreve(c, ("vantagem de B: R$ " + f"{v:.2f}".replace(".", ",")), x0, yb + 170, 64, "g", BR, a))
    E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, f"minuto {round(m)}", 1400, yb + 170, 64, "g", CLARO, a))
    E.frase(c, t, kb, ps("a cada minuto, a vantagem", "i", 72, CLARO) + [("cai R$ 0,50", "g", 76, BR)], XE, 560, "left", 0.1)
    E.frase(c, t, kc - 0.9, ps("em", "i", 80, CLARO) + [("40 minutos,", "g", 84, BR)] + ps("a vantagem", "i", 80, CLARO) + [("acaba", "g", 84, CLARO)], XE, 680, "left", 0.12)
    E.foco(c, t, kd, 0.5, lambda a: E.selo(c, XE + 50, 815, 50, False, a))
    E.linha(c, t, [("não compensa com", "i", 66, CLARO, kd + 0.1), ("taxa extra", "g", 70, BR, pal("s16", "taxa")),
                   ("ou", "i", 66, CLARO, pal("s16", "ou")), ("franquia", "g", 70, BR, pal("s16", "franquia"))], XE + 130, 838)
    E.frase(c, t, ke - 0.4, ps("aí,", "i", 84, CLARO) + [("monte a equação", "g", 90, BR)], XE + 130, 975, "left", 0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 150, passo=0.12)
    ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
    for y, k, n, sai, km, ts, tk in ((300, ka, "A", "R$ 5", "+ R$ 3", pal("s17", "cinco"), pal("s17", "três")),
                                     (560, kb, "B", "R$ 11", "+ R$ 2,50", pal("s17", "onze"), pal("s17", "dois"))):
        letra(c, t, k, n, XE + 40, y - 30, 48)
        E.frase(c, t, k + 0.1, ps("táxi", "i", 72), XE + 110, y)
        E.frase(c, t, ts, [(sai, "g", 100, COR)] + ps("de saída", "i", 68), XE + 290, y, passo=0.14)
        E.frase(c, t, tk, [(km, "g", 90, TINTA)] + ps("por km", "i", 68), XE + 110, y + 120, passo=0.14)
    E.frase(c, t, kc, ps("com quantos", "i", 80) + [("km", "g", 84, COR)] + ps("as corridas", "i", 80) + [("custam o mesmo?", "g", 84, COR)], W / 2, 900, "center", 0.1)
    E.relogio(c, t, C["s18.a"], 1520, 330, 170)
    E.frase(c, t, ka - 1.0, ps("valores inventados", "i", 44, TINTA2), 1750, 1010, "right", 0.08)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    a0, b0, c0, d0, e0, f0 = (C[f"s20.{k}"] for k in "abcdef")

    def resolve():
        E.foco(c, t, a9, 0.5, lambda a: E.pilula(c, "km", 760, 130, 60, "i", a=a, cor=E.SOBRE))
        E.foco(c, t, a9 + 0.3, 0.5, lambda a: M.arrow(c, 860, 132, 980, 132, TINTA, a, 5, 18))
        E.foco(c, t, pal("s19", "xis"), 0.5, lambda a: (E.bola(c, 1070, 128, 62, a=a), centro(c, "x", 1070, 156, 84, "g", E.SOBRE, a)))
        linhas = ((b9, "5 + 3x", "11 + 2,5x"), (d9, "5 + 0,5x", "11"), (b0, "0,5x", "6"), (c0, "x", "12"))
        ops = ((c9, "− 2,5x"), (a0, "− 5"), (pal("s20", "dobrando"), "× 2"))
        pilha(c, t, linhas, ops, 900, 320, 190, 100)
        E.frase(c, t, c0 + 0.5, [("km", "g", 90, COR)], 1110, 890)
    E.saida(c, t, d0 - 0.4, resolve)
    if t < d0 - 0.4:
        return
    E.foco(c, t, d0 - 0.3, 0.5, lambda a: (E.bola(c, 760, 230, 110, a=a), centro(c, "12", 760, 270, 110, "g", E.SOBRE, a)))
    E.frase(c, t, d0 - 0.2, [("km", "g", 110)], 900, 268)
    letra(c, t, d0, "A", XE + 40, 470, 50)
    E.linha(c, t, [("5 + 3 × 12", "g", 96, TINTA, d0 + 0.1), ("= R$ 41", "g", 96, COR, pal("s20", "quarenta"))], XE + 120, 505)
    letra(c, t, e0, "B", XE + 40, 680, 50)
    E.linha(c, t, [("11 + 2,5 × 12", "g", 96, TINTA, e0 + 0.1), ("= R$ 41", "g", 96, COR, pal("s20", "quarenta", 2))], XE + 120, 715)
    E.foco(c, t, f0, 0.5, lambda a: E.selo(c, 820, 890, 64, True, a))
    E.frase(c, t, f0 + 0.1, [("bateu!", "g", 100, CERTO)], 910, 925)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 250, "center")
        for i, (k, s) in enumerate((("s21.a", "escreva a conta de cada plano"), ("s21.b", "iguale as contas: é o empate"))):
            y = 470 + i * 210
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 350, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    ka, kb, kc, kd, ke, kf = (C[f"s22.{k}"] for k in "abcdef")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 84), XE, 200, passo=0.14)
    E.linha(c, t, [("de", "i", 72, TINTA, ka - 0.2), ("quando fica igual", "g", 76, TINTA2, ka), ("para", "i", 72, TINTA, kb - 0.3), ("quando fica menor", "g", 76, COR, kb)], XE, 330)
    E.frase(c, t, kc - 0.2, ps("é a", "i", 100) + [("inequação", "g", 130, COR)], XE, 490, passo=0.14)
    E.frase(c, t, kd - 1.0, ps("e por que, às vezes,", "i", 72) + [("o sinal vira", "g", 80, COR)], XE, 610, passo=0.1)
    E.foco(c, t, ke, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, ke + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, ke + 0.2, 0.4))
    E.frase(c, t, kf, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conta=b_conta, tabela=b_tabela, equacao=b_equacao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
