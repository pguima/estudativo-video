"""Visual — Estudativo · MAT-EQU-011: isolar uma letra numa fórmula.
Na tela, as letras são v, d e t (a voz diz "vê", "dê", "tê"); o ponto do meio é o sinal de vezes, explicado em s09.
As equações ficam alinhadas pelo igual (peça eq) e a operação dos dois lados entra em pílulas embaixo de cada lado.
O carro na estrada mostra a velocidade; o triângulo do atalho é desenhado aqui (triangulo) e a mão que cobre é um cartão.
Instantes: cues C[...] e, dentro da frase, a palavra falada (PW)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-011_isolar_letra_formula.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("letras", "isolar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AP = E.APERTO["g"]

assert 180 / 2 == 90 and 90 * 2 == 180 and 10 / 2 == 5 and 5 * 2 == 10
assert 80 * 3 == 240 and 240 / 3 == 80 and 180 / 90 == 2 and 90 / 2 == 45 != 180
assert 300 / 75 == 4 and 75 * 4 == 300

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
    return [(w, est, size, cor) for w in txt.split()]


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def gap(size):
    return size * 0.55


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, a=0)


def eq(c, t, t0, esq, dir_, y, size, cor=None, cx=W / 2, cor_e=None, cor_d=None):
    """equação alinhada pelo igual em cx"""
    g = gap(size)
    E.foco(c, t, t0, 0.5, lambda a: (E.formula(c, esq, cx - g, y, size, cor=cor_e or cor or TINTA, a=a, align="right"),
                                      centro(c, "=", cx, y, size, "g", cor or TINTA, a),
                                      E.formula(c, dir_, cx + g, y, size, cor=cor_d or cor or TINTA, a=a)))


def lados(esq, dir_, size, cx=W / 2):
    g = gap(size)
    return cx - g - larg_f(esq, size) / 2, cx + g + larg_f(dir_, size) / 2


def x_esq(esq, size, cx=W / 2):
    return cx - gap(size) - larg_f(esq, size)


def x_dir(size, cx=W / 2):
    return cx + gap(size)


def trecho(s, sub, x0, size, n=1):
    i = -1
    for _ in range(n):
        i = s.find(sub, i + 1)
    assert i >= 0, (s, sub)
    ate = lambda u: E.larg(u, "g", size) + (AP * size if u else 0)
    return x0 + ate(s[:i]), E.larg(sub, "g", size)


def caixa(c, t, t0, x0, w, y, size, cor=None, alto=None):
    q = ep(t, t0, 0.45)
    h = alto or size * 1.18
    E.caixa_pontilhada(c, x0 - size * 0.18, y - size * 0.92, w + size * 0.36, h, q, cor or COR, prog_=q)


def ops(c, t, t0, esq, dir_, y, size, txt, cor=None, dy=None):
    ce, cd = lados(esq, dir_, size)
    yy = y + (dy or size * 0.78)
    E.foco(c, t, t0, 0.4, lambda a: (E.pilula(c, txt, ce, yy, 46, estilo="b", fundo=cor or E.COR, a=a),
                                      E.pilula(c, txt, cd, yy, 46, estilo="b", fundo=cor or E.COR, a=a)), sobe=6)


def selo_eq(c, t, t0, dir_, y, size, ok=True):
    r = size * 0.4
    x = x_dir(size) + larg_f(dir_, size) + r + size * 0.3
    E.foco(c, t, t0, 0.45, lambda q: E.selo(c, x, y - size * 0.36, r, ok, q))
    return x + r


def selo_dep(c, t, t0, s, x, y, size, ok=True, align="center"):
    """selo logo depois de uma fórmula escrita em x (centro ou borda esquerda)"""
    w = larg_f(s, size)
    x1 = x + w / 2 if align == "center" else x + w
    r = size * 0.4
    E.foco(c, t, t0, 0.45, lambda q: E.selo(c, x1 + r + size * 0.3, y - size * 0.36, r, ok, q))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None, est="g"):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, est, tinta or E.SOBRE, a)


def carro(c, x, y, a, cor=None):
    """carrinho visto de lado: (x, y) = ponto no chão, no meio do carro"""
    if a <= 0:
        return
    cor = cor or E.COR
    M.rrect(c, x - 80, y - 74, 160, 50, 14, cor, a)
    M.rrect(c, x - 44, y - 110, 92, 44, 14, cor, a)
    M.rrect(c, x - 30, y - 100, 30, 26, 6, BR, a * 0.85)
    M.rrect(c, x + 8, y - 100, 30, 26, 6, BR, a * 0.85)
    for dx in (-46, 46):
        c.drawCircle(x + dx, y - 20, 20, M.paint(TINTA, a))
        c.drawCircle(x + dx, y - 20, 8, M.paint(BR, a))


def triangulo(c, cx, topo, meia, base, a, tinta, cor, letras=(1, 1, 1), size=150):
    """o triângulo do atalho: d em cima, v e t embaixo; letras = alfa de cada letra (d, v, t)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, topo); p.lineTo(cx + meia, base); p.lineTo(cx - meia, base); p.close()
    pt = M.paint(tinta, a, stroke=8)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    ym = topo + (base - topo) * 0.6
    hw = meia * 0.6
    M.line(c, cx - hw, ym, cx + hw, ym, tinta, a, 8)
    M.line(c, cx, ym, cx, base, tinta, a, 8)
    d_, v_, t_ = letras
    k = size / 150
    centro(c, "d", cx, ym - 40 * k, size, "g", cor, a * d_)
    centro(c, "v", cx - meia * 0.36, base - 50 * k, size * 0.86, "g", cor, a * v_)
    centro(c, "t", cx + meia * 0.36, base - 50 * k, size * 0.86, "g", cor, a * t_)
    return ym


def tampa(c, x, y, w, h, a, cor):
    """o cartão que cobre a letra escolhida"""
    if a <= 0:
        return
    M.rrect(c, x - w / 2, y - h / 2, w, h, 18, cor, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, C["s01"] + 0.1, ps("uma fórmula que cai muito em prova", "i", 72, COR), W / 2, 190, "center", passo=0.1)
        eq(c, t, a_, "v", "f{d}{t}", 450, 170)
        E.foco(c, t, a_ + 0.6, 0.45, lambda q: (centro(c, "velocidade", 520, 610, 54, "i", TINTA2, q),
                                                 centro(c, "distância ÷ tempo", 1280, 610, 54, "i", TINTA2, q)))
        E.frase(c, t, b_, ps("mas a pergunta quer", "i", 80) + ps("a distância", "g", 76, COR), W / 2, 760, "center", passo=0.12)
        E.saida(c, t, c_ - 0.1, lambda: E.frase(c, t, PW("s01", "decorar"), ps("decorar outra fórmula?", "i", 80), W / 2, 900, "center", passo=0.12))
        E.frase(c, t, c_, ps("não:", "g", 80, CERTO) + ps("a balança vira a fórmula", "i", 84), W / 2, 900, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, PW("s02", "qualquer"), [("qualquer", "i", 110), ("letra", "g", 126, COR)], XE, 450)
        E.frase(c, t, PW("s02", "sozinha"), [("sozinha", "g", 126, COR)], XE, 590)
        E.frase(c, t, PW("s02", "fórmula"), ps("numa fórmula simples", "i", 84), XE, 720, passo=0.13)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 505, 80, "g", E.SOBRE, a),
                                                centro(c, "de prova", 1480, 590, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você só precisa de", "i", 84), XE, 410, passo=0.13)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 190, 700, 120, "i", TINTA, a))
    x, y, w = 900, 220, 860
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("Fazer o mesmo", "i", 62), ("nos dois lados", "g", 62, COR)], x + 44, y + 90)
    E.formula_em(c, t, C["s03.b"] + 0.8, "2x + 3 = 11", x + 44, y + 220, 76, "g", TINTA2)
    E.formula_em(c, t, C["s03.b"] + 1.2, "→ x = 4", x + 520, y + 220, 76, "g", TINTA2)
    E.frase(c, t, PW("s03", "física"), ps("nada de física", "g", 72, COR), x + 44, 680)
    E.frase(c, t, PW("s03", "procure"), ps("faltou? procure no canal", "i", 62), x + 44, 860, passo=0.11)


# ---------------- o que cada letra é ----------------
def b_letras(c, t, C, b):
    s4, s5 = C["s04"], C["s05"]

    def s04():
        E.frase(c, t, s4 + 0.1, ps("o que cada letra é", "i", 84, COR), XE, 180, passo=0.12)
        E.frase(c, t, PW("s04", "primeira"), ps("a primeira letra de uma palavra", "i", 60, TINTA2), XE, 270, passo=0.1)
        itens = (("s04.a", "v", "velocidade", "km que anda em 1 hora"), ("s04.b", "d", "distância", "o caminho percorrido"),
                 ("s04.c", "t", "tempo", "quanto dura a viagem"))
        for i, (k, l, nome, ex) in enumerate(itens):
            y = 430 + i * 200
            E.foco(c, t, C[k], 0.5, lambda q, y=y, l=l: num_bola(c, l, 330, y - 40, 76, 100, q))
            E.frase(c, t, C[k] + 0.15, [(nome, "g", 92, COR)], 460, y)
            E.frase(c, t, C[k] + 0.6, ps(ex, "i", 64, TINTA2), 1060, y, passo=0.1)

    def s05():
        a, b_, c_, d, e = (C[f"s05.{k}"] for k in "abcde")
        x0, x1, y = 300, 1620, 400
        q = ep(t, a, 0.6)
        if q > 0:
            M.line(c, x0, y, lerp(x0, x1, q), y, TINTA, 1.0, 8)
        E.chave(c, x0, x1, y + 30, COR, ep(t, a + 0.2, 0.5), 22, 5)
        E.foco(c, t, a + 0.3, 0.45, lambda q: centro(c, "180 km", 840, y + 130, 72, "g", COR, q))
        pos = ease_io(prog(t, b_, max(0.6, c_ - b_)))
        E.foco(c, t, s5 + 0.1, 0.4, lambda q: carro(c, lerp(x0, x1, pos), y - 6, q))
        E.foco(c, t, b_, 0.45, lambda q: E.escreve(c, "em 2 horas", 1000, y + 130, 72, "i", TINTA, q))
        xm = (x0 + x1) / 2
        E.foco(c, t, c_, 0.45, lambda q: (M.line(c, xm, y - 26, xm, y + 26, TINTA, q, 6),
                                           centro(c, "90 km em 1 h", (x0 + xm) / 2, y - 150, 54, "b", TINTA2, q),
                                           centro(c, "90 km em 1 h", (xm + x1) / 2, y - 150, 54, "b", TINTA2, q)))
        fcen(c, t, d, "v = 90 km/h", W / 2, 680, 110, COR)
        fcen(c, t, e, "v = f{d}{t} = f{180}{2} = 90", W / 2, 910, 104)

    fase(c, t, s4, s5 - 0.1, s04)
    fase(c, t, s5, 1e9, s05)


# ---------------- isolar o d ----------------
def b_isolar(c, t, C, b):
    t6, t7, t8, t9, t10 = (C[f"s{i:02d}"] for i in range(6, 11))

    def s06():
        a, b_, c_ = C["s06.a"], C["s06.b"], C["s06.c"]
        E.frase(c, t, t6 + 0.1, ps("isolar uma letra:", "g", 80, COR), W / 2, 180, "center")
        E.frase(c, t, a, ps("deixar ela sozinha de um lado do igual", "i", 76), W / 2, 280, "center", passo=0.1)
        s = 140
        eq(c, t, a + 0.6, "v", "f{d}{t}", 500, s)
        E.foco(c, t, b_, 0.45, lambda q: E.pilula(c, "d dividida por t", 1380, 470, 50, estilo="b", a=q))
        tl = PW("s06", "Lembra")
        E.frase(c, t, tl, ps("lembra?", "i", 72, TINTA2), XE, 720)
        eq(c, t, tl + 0.3, "f{x}{4}", "5", 760, 110)
        ops(c, t, c_, "f{x}{4}", "5", 760, 110, "× 4", dy=125)

    def s07():
        a, b_, c_, d = (C[f"s07.{k}"] for k in "abcd")
        s = 130
        eq(c, t, t7 + 0.1, "v", "f{d}{t}", 260, s)
        ops(c, t, a, "v", "f{d}{t}", 260, s, "× t", dy=150)
        eq(c, t, a + 0.9, "v · t", "f{d · t}{t}", 610, s)
        # os dois t da direita se anulam
        xf = x_dir(s)
        s_ = s * 0.78
        wc, wb = larg_f("d · t", s_), larg_f("t", s_)
        wf = max(wc, wb) + s * 0.12
        xt, wt = trecho("d · t", "t", xf + (wf - wc) / 2, s_)
        xb = xf + (wf - wb) / 2
        for k, (x0, yb) in enumerate(((xt, 610 - s * 0.46), (xb, 610 + s * 0.46))):
            if t >= b_ + k * 0.3:
                E.risco(c, x0 - 10, yb + 10, x0 + wt + 10, yb - s_ * 0.8, t, b_ + k * 0.3, largura=10)
        E.frase(c, t, b_ + 0.4, [("÷ t", "g", 60, ERRADO), ("e", "i", 64), ("× t", "g", 60, ERRADO)] + ps("se anulam", "i", 64), 1290, 590, passo=0.1)
        eq(c, t, c_, "v · t", "d", 870, 150, cor_d=COR)
        xe = x_esq("v · t", 150)
        caixa(c, t, d, xe, larg_f("v · t", 150), 870, 150)

    def s08():
        a, b_, c_ = C["s08.a"], C["s08.b"], C["s08.c"]
        E.frase(c, t, t8 + 0.1, ps("por que se", "i", 84) + ps("anulam?", "g", 80, COR), W / 2, 180, "center")
        E.frase(c, t, PW("s08", "números"), ps("pense em números", "i", 72, TINTA2), W / 2, 290, "center", passo=0.1)
        fcen(c, t, a, "10 ÷ 2 = 5", W / 2, 450, 120)
        fcen(c, t, b_, "5 × 2 = 10", W / 2, 620, 120, COR)
        E.foco(c, t, b_ + 0.4, 0.4, lambda q: E.pilula(c, "volta", 1420, 580, 50, estilo="b", a=q))
        E.frase(c, t, c_, ps("seja qual for o número", "i", 80), W / 2, 790, "center", passo=0.12)
        fcen(c, t, PW("s08", "letra"), "f{d · t}{t} = d", W / 2, 960, 100, COR)

    def s09():
        a, b_, c_ = C["s09.a"], C["s09.b"], C["s09.c"]
        s = 170
        eq(c, t, a, "d", "v · t", 360, s, COR)
        E.frase(c, t, PW("s09", "trocaram"), ps("os lados trocaram de lugar:", "i", 70), W / 2, 540, "center", passo=0.1)
        E.frase(c, t, PW("s09", "Pode"), ps("pode,", "g", 66, CERTO) + ps("a balança segue em equilíbrio", "i", 70), W / 2, 640, "center", passo=0.1)
        xd, wd = trecho("v · t", "·", x_dir(s), s)
        caixa(c, t, b_, xd, wd, 360, s, ERRADO)
        E.foco(c, t, b_ + 0.3, 0.45, lambda q: E.pilula(c, "· é vezes", 1580, 300, 56, estilo="b", fundo=ERRADO, a=q))
        fcen(c, t, c_, "90 · 2 = 180 km", W / 2, 870, 110)
        selo_dep(c, t, PW("s09", "Bateu"), "90 · 2 = 180 km", W / 2, 870, 110)

    def s10():
        a, b_, c_, d = (C[f"s10.{k}"] for k in "abcd")
        E.frase(c, t, t10 + 0.1, ps("agora use", "i", 84, COR), W / 2, 180, "center")
        E.formula_em(c, t, a, "v = 80 km/h", 330, 340, 96, "g", TINTA)
        E.formula_em(c, t, b_, "t = 3 h", 1150, 340, 96, "g", TINTA)
        fcen(c, t, c_, "d = 80 · 3 = 240 km", W / 2, 560, 120, COR)
        E.frase(c, t, PW("s10", "Conferindo"), ps("conferindo na fórmula do começo", "i", 64, TINTA2), W / 2, 720, "center", passo=0.1)
        fcen(c, t, d, "v = f{240}{3} = 80 km/h", W / 2, 900, 104)
        selo_dep(c, t, PW("s10", "Bateu"), "v = f{240}{3} = 80 km/h", W / 2, 900, 104)

    fase(c, t, t6, t7 - 0.1, s06)
    fase(c, t, t7, t8 - 0.1, s07)
    fase(c, t, t8, t9 - 0.1, s08)
    fase(c, t, t9, t10 - 0.1, s09)
    fase(c, t, t10, 1e9, s10)


# ---------------- isolar o t ----------------
def b_tempo(c, t, C, b):
    a, b_, c_, d = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, C["s11"] + 0.1, ps("e se a pergunta for", "i", 80) + ps("o tempo?", "g", 76, COR), W / 2, 170, "center", passo=0.12)
    s = 130
    eq(c, t, a, "d", "v · t", 360, s)
    ops(c, t, b_, "d", "v · t", 360, s, "÷ v")
    eq(c, t, c_, "f{d}{v}", "t", 690, 140, COR)
    E.foco(c, t, c_ + 0.5, 0.45, lambda q: E.pilula(c, "t = d ÷ v", 1500, 650, 52, estilo="b", a=q))
    fcen(c, t, d, "t = f{180}{90} = 2 h", W / 2, 950, 110)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s12"] + 0.1, ps("o erro", "g", 100, ERRADO) + ps("mais comum", "i", 104), W / 2, 180, "center")
    s = 140
    eq(c, t, a, "d", "f{v}{t}", 400, s, ERRADO)
    E.frase(c, t, PW("s12", "lembra"), ps("o t muda de lugar... mas como?", "i", 64, TINTA2), W / 2, 560, "center", passo=0.1)
    fcen(c, t, b_, "f{90}{2} = 45", 700, 760, 110)
    E.foco(c, t, c_, 0.45, lambda q: (E.formula(c, "≠ 180 km", 1080, 760, 110, cor=ERRADO, a=q),
                                       E.selo(c, 1660, 720, 46, False, q)))
    E.frase(c, t, d, ps("na dúvida,", "i", 80) + ps("teste com números", "g", 76, COR), W / 2, 950, "center", passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s13, s14, s15 = C["s13"], C["s14"], C["s15"]
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    cx, topo, meia, base = 560, 260, 380, 860

    def tri():
        letras = (ep(t, b3, 0.45), ep(t, c3, 0.45), ep(t, c3 + 0.4, 0.45))
        ym = triangulo(c, cx, topo, meia, base, ep(t, a3, 0.6), BR, CLARO, letras)
        # o cartão que cobre: d, depois v, depois t
        for t0, t1, (x, y) in ((a4, b4 - 0.2, (cx, ym - 90)), (b4, c4 - 0.2, (cx - meia * 0.36, base - 100)),
                               (c4, d4 - 0.2, (cx + meia * 0.36, base - 100))):
            q = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.35))
            tampa(c, x, y, 170, 150, q, E.COR)
        if t >= d4:
            q = ep(t, d4 + 0.4, 0.45)
            E.chave(c, cx - meia * 0.6, cx + meia * 0.6, base + 30, CLARO, q, 22, 5)
    E.saida(c, t, s15 - 0.1, tri)

    def s13_():
        E.frase(c, t, s13 + 0.1, ps("o atalho:", "i", 84, CLARO) + ps("o triângulo", "g", 84, BR), W / 2, 150, "center")
        E.frase(c, t, b3, ps("d em cima", "g", 76, BR), 1060, 330, passo=0.1)
        E.frase(c, t, b3 + 0.6, ps("como na fórmula do começo", "i", 62, CLARO), 1060, 410, passo=0.1)
        E.frase(c, t, c3, ps("v e t embaixo", "g", 76, BR), 1060, 530, passo=0.1)
        E.frase(c, t, c3 + 0.6, ps("lado a lado", "i", 62, CLARO), 1060, 610, passo=0.1)
        E.frase(c, t, d3, ps("cubra a letra que quer:", "i", 72, CLARO), 1060, 760, passo=0.1)
        E.frase(c, t, d3 + 1.2, ps("o que sobra é a conta", "g", 72, BR), 1060, 860, passo=0.1)

    def s14_():
        xr = 1100
        for t0, s in ((a4, "d = v · t"), (b4, "v = f{d}{t}"), (c4, "t = f{d}{v}")):
            y = {a4: 280, b4: 480, c4: 700}[t0]
            E.formula_em(c, t, t0 + 0.3, s, xr, y, 120, "g", BR)
        E.frase(c, t, d4, ps("a fórmula desenhada:", "i", 64, CLARO), xr, 830, passo=0.1)
        E.frase(c, t, PW("s14", "lado"), ps("lado a lado = vezes", "g", 60, BR), xr, 920, passo=0.08)
        E.frase(c, t, PW("s14", "uma"), ps("em cima = dividido", "g", 60, BR), xr, 1000, passo=0.08)

    def s15_():
        a, b_ = C["s15.a"], C["s15.b"]
        E.frase(c, t, a, ps("não compensa com", "i", 84, CLARO) + ps("soma ou subtração", "g", 80, BR), W / 2, 380, "center", passo=0.12)
        E.frase(c, t, PW("s15", "mais"), ps("ou com", "i", 84, CLARO) + ps("mais de 3 letras", "g", 80, BR), W / 2, 500, "center", passo=0.12)
        E.frase(c, t, b_, ps("volte para a", "i", 110, CLARO) + ps("balança", "g", 110, BR), W / 2, 760, "center", passo=0.14)

    fase(c, t, s13, s14 - 0.1, s13_)
    fase(c, t, s14, s15 - 0.1, s14_)
    fase(c, t, s15, 1e9, s15_)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, PW("s16", "caminhão"), ps("um caminhão viajou", "i", 84), XE, 360, passo=0.12)
    E.formula_em(c, t, a, "300 km", XE, 510, 120, "g", COR)
    E.frase(c, t, b_ - 0.1, ps("a", "i", 100), 680, 510)
    E.formula_em(c, t, b_, "75 km/h", 760, 510, 120, "g", COR)
    E.frase(c, t, c_, ps("quantas horas", "g", 110, COR), XE, 750, passo=0.15)
    E.frase(c, t, c_ + 0.6, ps("durou a viagem?", "i", 110), XE, 880, passo=0.15)
    E.relogio(c, t, C["s17.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s18, s19 = C["s18"], C["s19"]

    def s18_():
        a, b_, c_, d, e = (C[f"s18.{k}"] for k in "abcde")
        s = 110
        eq(c, t, a, "d", "v · t", 200, s, TINTA2)
        eq(c, t, b_, "300", "75 · t", 400, s)
        ops(c, t, c_, "300", "75 · t", 400, s, "÷ 75")
        eq(c, t, d, "f{300}{75}", "t", 680, s)
        E.foco(c, t, d + 0.6, 0.45, lambda q: E.formula(c, "300 ÷ 75 = 4", 1300, 680, 70, cor=TINTA2, a=q))
        eq(c, t, e, "t", "4 h", 900, 140, COR)
        selo_eq(c, t, e + 0.4, "4 h", 900, 140)

    def s19_():
        a, b_ = C["s19.a"], C["s19.b"]
        E.frase(c, t, s19 + 0.1, ps("conferindo", "i", 84, COR), W / 2, 180, "center")
        fcen(c, t, a, "75 · 4 = 300", W / 2, 380, 130)
        selo_dep(c, t, PW("s19", "Bateu"), "75 · 4 = 300", W / 2, 380, 130)
        cx, topo, meia, base = 560, 520, 260, 930
        q = ep(t, b_, 0.5)
        if q > 0:
            ym = triangulo(c, cx, topo, meia, base, q, TINTA, COR, size=110)
            tampa(c, cx + meia * 0.36, base - 75, 120, 110, ep(t, b_ + 0.5, 0.35), E.COR)
        E.frase(c, t, b_ + 0.3, ps("cobrindo o t:", "i", 76), 950, 680, passo=0.1)
        E.formula_em(c, t, b_ + 1.2, "t = f{d}{v} = f{300}{75}", 950, 850, 100, "g", COR)

    fase(c, t, s18, s19 - 0.1, s18_)
    fase(c, t, s19, 1e9, s19_)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s20.a", ps("isolar é deixar", "i", 84) + ps("a letra sozinha", "g", 80, COR)),
                 (590, "s20.b", ps("com a", "i", 84) + ps("mesma balança", "g", 80, COR)),
                 (780, "s20.c", ps("teste a fórmula", "i", 84) + ps("com números", "g", 80, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), 330, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 430, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a_, b_, c_, d_ = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("praticando", "g", 120, COR), XE, 390)
    E.frase(c, t, a_ + 0.4, ps("equações", "g", 120, COR), XE, 520)
    E.frase(c, t, b_, ps("conferindo cada resposta", "i", 80), XE, 660, passo=0.13)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1650, p), lerp(650, 405, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, letras=b_letras, isolar=b_isolar, tempo=b_tempo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
