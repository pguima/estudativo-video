"""Visual — Estudativo · MAT-EQU-009: equação com parênteses.
As equações ficam alinhadas pelo sinal de igual (peça eq), como no caderno: cada passo desce uma linha e a operação dos
dois lados entra numa pílula embaixo de cada lado. O "três vezes tudo" vira três pacotes e arcos do 3 até cada termo.
O x que some vira balança com caixas e pesos. Instantes: cues C[...] e, dentro da frase, a palavra falada (PW)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-009_equacao_com_parenteses.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("parenteses", "some", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AP = E.APERTO["g"]

x = 10
assert 3 * (x - 2) == 2 * x + 4 == 24 and 3 * x - 6 == 2 * x + 4 and x - 6 == 4
assert 3 * (6 - 2) == 12 and 2 * 6 + 4 == 16 and 3 * 6 - 2 == 2 * 6 + 4  # o erro: 3x − 2 = 2x + 4 dá x = 6
assert all(2 * (v + 1) == 2 * v + 2 for v in range(-5, 20)) and 2 * (10 + 1) == 22
x = 5
assert 4 * (x + 1) == x + 19 == 24 and 3 * x + 4 == 19 and 3 * x == 15
assert 4 * 6 + 1 == 6 + 19  # quem multiplica só o x: 4x + 1 = x + 19 dá x = 6

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


def fase(c, t, t0, t1, fn):
    """uma tela do bloco: de t0 até sumir em t1"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def gap(size):
    return size * 0.55


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, a=0)


def eq(c, t, t0, esq, dir_, y, size, cor=None, cx=W / 2, cor_e=None, cor_d=None):
    """equação alinhada pelo igual em cx: o lado esquerdo termina antes do igual, o direito começa depois"""
    g = gap(size)
    E.foco(c, t, t0, 0.5, lambda a: (E.formula(c, esq, cx - g, y, size, cor=cor_e or cor or TINTA, a=a, align="right"),
                                      centro(c, "=", cx, y, size, "g", cor or TINTA, a),
                                      E.formula(c, dir_, cx + g, y, size, cor=cor_d or cor or TINTA, a=a)))


def lados(esq, dir_, size, cx=W / 2):
    """centro de cada lado da equação de eq()"""
    g = gap(size)
    return cx - g - larg_f(esq, size) / 2, cx + g + larg_f(dir_, size) / 2


def trecho(s, sub, x0, size, n=1):
    """x inicial e largura do n-ésimo `sub` dentro de s escrito a partir de x0 (texto simples)"""
    i = -1
    for _ in range(n):
        i = s.find(sub, i + 1)
    assert i >= 0, (s, sub)
    ate = lambda u: E.larg(u, "g", size) + (AP * size if u else 0)
    return x0 + ate(s[:i]), E.larg(sub, "g", size)


def x_esq(esq, size, cx=W / 2):
    return cx - gap(size) - larg_f(esq, size)


def x_dir(size, cx=W / 2):
    return cx + gap(size)


def caixa(c, t, t0, x0, w, y, size, cor=None):
    """caixa pontilhada em volta de um trecho de altura `size` com linha de base y"""
    q = ep(t, t0, 0.45)
    E.caixa_pontilhada(c, x0 - size * 0.18, y - size * 0.92, w + size * 0.36, size * 1.18, q, cor or COR, prog_=q)


def ops(c, t, t0, esq, dir_, y, size, txt, cor=None, dy=None):
    """a mesma operação numa pílula embaixo de cada lado"""
    ce, cd = lados(esq, dir_, size)
    yy = y + (dy or size * 0.78)
    E.foco(c, t, t0, 0.4, lambda a: (E.pilula(c, txt, ce, yy, 46, estilo="b", fundo=cor or E.COR, a=a),
                                      E.pilula(c, txt, cd, yy, 46, estilo="b", fundo=cor or E.COR, a=a)), sobe=6)


def selo_eq(c, t, t0, dir_, y, size, ok=True, x_extra=None):
    """selo logo depois do lado direito da equação de eq()"""
    r = size * 0.4
    x = x_dir(size) + larg_f(dir_, size) + r + size * 0.3
    E.foco(c, t, t0, 0.45, lambda q: E.selo(c, x, y - size * 0.36, r, ok, q))
    return x + r


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def pacote(c, cx, cy, w, h, s, a):
    """um pacote fechado com o que vai dentro"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 18, M.mix(E.COR, BR, 0.84), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18), M.paint(E.COR, a, stroke=5))
    M.line(c, cx - w / 2 + 20, cy - h / 2 + 30, cx + w / 2 - 20, cy - h / 2 + 30, E.COR, a * 0.5, 3)
    E.formula(c, s, cx, cy + 40, 76, cor=COR, a=a, align="center")


def caixas_pesos(t, n_cx, peso, ta, tb):
    """o que vai em cada prato: n caixas com x (entram em ta) e um peso de `peso` kg (entra em tb)"""
    def fn(c, px, py):
        a1, a2 = ep(t, ta, 0.4), ep(t, tb, 0.4)
        s, gp = 92, 14
        wp = 120
        total = n_cx * s + (n_cx) * gp + wp
        x0 = px - total / 2
        for i in range(n_cx):
            xx = x0 + i * (s + gp)
            if a1 > 0:
                M.rrect(c, xx, py - s, s, s, 10, E.COR, a1)
                centro(c, "x", xx + s / 2, py - s * 0.3, 62, "g", BR, a1)
        xp = x0 + n_cx * (s + gp)
        if a2 > 0:
            p = skia.Path()
            p.moveTo(xp + 18, py - 86); p.lineTo(xp + wp - 18, py - 86); p.lineTo(xp + wp, py); p.lineTo(xp, py); p.close()
            c.drawPath(p, M.paint(TINTA, a2))
            c.drawCircle(xp + wp / 2, py - 98, 14, M.paint(TINTA, a2, stroke=6))
            centro(c, f"{peso} kg", xp + wp / 2, py - 26, 40, "b", BR, a2)
    return fn


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        y, s = 400, 150
        eq(c, t, a_, "2x + 1", "2x + 3", y, s)
        for k, (x0, w) in enumerate((trecho("2x + 1", "2x", x_esq("2x + 1", s), s), trecho("2x + 3", "2x", x_dir(s), s))):
            if t >= b_ + k * 0.2:
                E.risco(c, x0 - 14, y + 16, x0 + w + 14, y - 110, t, b_ + k * 0.2, largura=14)
        E.frase(c, t, b_, ps("o", "i", 84) + ps("x", "g", 80, ERRADO) + ps("some", "i", 84), W / 2, 560, "center")
        eq(c, t, b_ + 0.9, "1", "3", 720, 130, COR)
        E.saida(c, t, c_ - 0.1, lambda: E.frase(c, t, PW("s01", "Errou"), ps("errou alguma coisa?", "i", 84), W / 2, 920, "center", passo=0.12))
        E.frase(c, t, c_, ps("não:", "g", 80, CERTO) + ps("a equação está dando", "i", 84) + ps("um recado", "g", 80, COR),
                W / 2, 920, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, conta)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, PW("s02", "equações"), [("equações", "g", 126, COR)], XE, 450)
        E.frase(c, t, PW("s02", "parênteses"), [("com", "i", 116), ("parênteses", "g", 126, COR)], XE, 590)
        E.frase(c, t, PW("s02", "entende"), ps("e quando o x desaparece", "i", 80), XE, 740, passo=0.13)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 505, 80, "g", E.SOBRE, a),
                                                centro(c, "de prova", 1480, 590, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você só precisa de", "i", 84), XE, 410, passo=0.13)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "Abrir", "parênteses", "3(x − 2) = 3x − 6"), ("s03.c", "Resolver com", "x dos dois lados", "2x + 3 = x + 8"))
    for i, (k, l1, l2, ex) in enumerate(itens):
        y = 200 + i * 320
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 270, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62), (l2, "g", 62, COR)], x + 44, y + 90)
        E.formula_em(c, t, C[k] + 0.8, ex, x + 44, y + 210, 70, "g", TINTA2)
    E.frase(c, t, PW("s03", "procure"), ps("faltou? procure no canal", "i", 62), x + 44, 900, passo=0.11)


# ---------------- exemplo com parênteses ----------------
EX = ("3(x − 2)", "2x + 4")


def b_parenteses(c, t, C, b):
    s4, s5, s6, s7, s8 = (C[f"s0{i}"] for i in range(4, 9))
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    yt, st = 300, 130

    def topo():
        eq(c, t, a4, *EX, yt, st)
        xe = x_esq(EX[0], st)
        x0, w = trecho(EX[0], "(x − 2)", xe, st)
        if t < s5:
            E.saida(c, t, s5 - 0.1, lambda: caixa(c, t, b4, x0, w, yt, st))
        # d: o 3 multiplica cada termo de dentro
        x3, w3 = trecho(EX[0], "3", xe, st)
        xx, wx = trecho(EX[0], "x", xe, st)
        x2, w2 = trecho(EX[0], "2", xe, st)
        E.salto(c, t, d5, x3 + w3 / 2, xx + wx / 2, yt - st * 0.85, 70, COR, d=0.6)
        E.salto(c, t, d5 + 0.6, x3 + w3 / 2, x2 + w2 / 2, yt - st * 0.85, 120, COR, d=0.7)

    E.saida(c, t, s7 - 0.1, topo)

    def s04():
        E.frase(c, t, b4, ps("o", "i", 84) + ps("x", "g", 80, COR) + ps("está preso nos parênteses", "i", 84), W / 2, 560, "center", passo=0.12)
        E.frase(c, t, c4, ps("antes da balança,", "i", 96) + ps("solte o x", "g", 92, COR), W / 2, 760, "center", passo=0.14)

    def s05():
        E.frase(c, t, a5, ps("passo 1:", "i", 84) + ps("abra os parênteses", "g", 80, COR), W / 2, 500, "center", passo=0.13)
        fcen(c, t, b5, "3 × (tudo o que está dentro)", W / 2, 650, 76, TINTA2)
        for i, cx in enumerate((520, 960, 1400)):
            E.foco(c, t, c5 + i * 0.35, 0.45, lambda a, cx=cx: pacote(c, cx, 860, 330, 150, "x − 2", a))

    def s06():
        fcen(c, t, a6, "3 × x = 3x", W / 2, 530, 104)
        fcen(c, t, b6, "3 × (−2) = −6", W / 2, 690, 104)
        eq(c, t, c6, "3x − 6", "2x + 4", 900, 124, COR)

    fase(c, t, s4, s5 - 0.1, s04)
    fase(c, t, s5, s6 - 0.1, s05)
    fase(c, t, s6, s7 - 0.1, s06)

    def s07():
        a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
        E.frase(c, t, a7, ps("passo 2:", "i", 80) + ps("como na aula passada", "g", 72, COR), W / 2, 170, "center", passo=0.12)
        s = 112
        eq(c, t, s7 + 0.2, "3x − 6", "2x + 4", 340, s)
        ops(c, t, b7, "3x − 6", "2x + 4", 340, s, "− 2x")
        eq(c, t, c7, "x − 6", "4", 570, s)
        ops(c, t, d7, "x − 6", "4", 570, s, "+ 6")
        eq(c, t, e7, "x", "10", 830, 140, COR)
        selo_eq(c, t, e7 + 0.3, "10", 830, 140)

    def s08():
        a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
        E.frase(c, t, s8 + 0.1, ps("conferindo no começo", "i", 84, COR), W / 2, 170, "center", passo=0.12)
        esq, dir_, s = "3(10 − 2)", "2 × 10 + 4", 112
        eq(c, t, a8, esq, dir_, 330, s)
        ce, cd = lados(esq, dir_, s)
        fcen(c, t, b8, "10 − 2 = 8", ce, 520, 84)
        fcen(c, t, PW("s08", "Vezes"), "8 × 3 = 24", ce, 650, 84)
        fcen(c, t, c8, "2 × 10 = 20", cd, 520, 84)
        fcen(c, t, PW("s08", "Mais"), "20 + 4 = 24", cd, 650, 84)
        tb = PW("s08", "Bateu")
        eq(c, t, tb - 0.2, "24", "24", 880, 130, CERTO)
        selo_eq(c, t, tb, "24", 880, 130)

    fase(c, t, s7, s8 - 0.1, s07)
    fase(c, t, s8, 1e9, s08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    t9, t10 = C["s09"], C["s10"]

    def s09():
        a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
        E.frase(c, t, t9 + 0.1, ps("o erro", "g", 100, ERRADO) + ps("mais comum", "i", 104), W / 2, 190, "center")
        s = 112
        eq(c, t, t9 + 0.6, *EX, 400, s)
        xe = x_esq(EX[0], s)
        x3, w3 = trecho(EX[0], "3", xe, s)
        xx, wx = trecho(EX[0], "x", xe, s)
        E.salto(c, t, a9, x3 + w3 / 2, xx + wx / 2, 400 - s * 0.85, 70, ERRADO, d=0.6)
        eq(c, t, b9, "3x − 2", "2x + 4", 620, s, cor_e=ERRADO)
        x2, w2 = trecho("3x − 2", "2", x_esq("3x − 2", s), s)
        caixa(c, t, PW("s09", "esquecendo"), x2, w2, 620, s, ERRADO)
        eq(c, t, c9, "x", "6", 850, 130, ERRADO)

    def s10():
        a, b_, c_, d = (C[f"s10.{k}"] for k in "abcd")
        E.frase(c, t, t10 + 0.1, ps("confira com", "i", 84) + ps("x = 6", "g", 80, ERRADO), W / 2, 190, "center")
        cl, cr = 560, 1360
        E.foco(c, t, a, 0.4, lambda q: centro(c, "lado esquerdo", cl, 330, 52, "i", TINTA2, q))
        fcen(c, t, a, "6 − 2 = 4", cl, 450, 92)
        fcen(c, t, PW("s10", "Vezes"), "4 × 3 = 12", cl, 580, 92)
        E.foco(c, t, b_, 0.4, lambda q: centro(c, "lado direito", cr, 330, 52, "i", TINTA2, q))
        fcen(c, t, b_, "2 × 6 + 4 = 16", cr, 515, 92)
        fcen(c, t, c_, "12 ≠ 16", W / 2, 770, 130, ERRADO)
        E.foco(c, t, c_ + 0.2, 0.45, lambda q: E.selo(c, W / 2 + larg_f("12 ≠ 16", 130) / 2 + 90, 725, 54, False, q))
        E.frase(c, t, d, ps("o de fora multiplica", "i", 80) + ps("todo mundo lá dentro", "g", 74, COR), W / 2, 950, "center", passo=0.12)

    fase(c, t, t9, t10 - 0.1, s09)
    fase(c, t, t10, 1e9, s10)


# ---------------- quando o x some ----------------
def b_some(c, t, C, b):
    s11, s12, s13, s14 = C["s11"], C["s12"], C["s13"], C["s14"]

    def s11_12():
        a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
        a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
        E.frase(c, t, s11 + 0.1, ps("o caso do começo", "i", 80, COR), W / 2, 150, "center")
        s = 112
        eq(c, t, a1, "2x + 1", "2x + 3", 300, s)
        ops(c, t, b1, "2x + 1", "2x + 3", 300, s, "− 2x")
        eq(c, t, c1, "1", "3", 580, 140)
        xs = selo_eq(c, t, a2, "3", 580, 140, False)
        E.frase(c, t, a2, ps("falso", "g", 84, ERRADO), xs + 30, 560)
        E.frase(c, t, b2, ps("não depende do x:", "i", 76) + ps("ele sumiu", "g", 72, COR), W / 2, 730, "center", passo=0.12)
        E.frase(c, t, c2, ps("nenhum número resolve", "i", 80), W / 2, 840, "center", passo=0.12)
        E.foco(c, t, d2, 0.5, lambda q: E.pilula(c, "não tem solução", W / 2, 940, 80, estilo="g", fundo=ERRADO, a=q))

    def s13_():
        a, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
        tn = PW("s13", "Nunca")
        E.saida(c, t, tn - 0.1, lambda: E.frase(c, t, s13 + 0.1, ps("na", "i", 84) + ps("balança", "g", 80, COR), W / 2, 150, "center"))
        E.frase(c, t, tn, ps("nunca", "g", 84, ERRADO) + ps("equilibra", "i", 88), W / 2, 150, "center")
        inc = 0.75 * ease_io(prog(t, c_ - 0.3, 1.2))
        E.foco(c, t, s13 + 0.2, 0.5, lambda q: E.balanca(c, W / 2, 560, caixas_pesos(t, 2, 1, a, b_), caixas_pesos(t, 2, 3, a, b_ + 0.5),
                                                       inc, q, larg_braco=880))
        E.frase(c, t, c_, ps("direita:", "i", 76) + ps("sempre 2 kg a mais", "g", 72, COR), W / 2, 960, "center", passo=0.12)

    def s14_():
        a, b_, c_, d = (C[f"s14.{k}"] for k in "abcd")
        E.frase(c, t, s14 + 0.1, ps("e se sobrar uma conta", "i", 80) + ps("verdadeira?", "g", 76, CERTO), W / 2, 150, "center", passo=0.12)
        s = 112
        eq(c, t, a, "2(x + 1)", "2x + 2", 310, s)
        eq(c, t, PW("s14", "Abrindo"), "2x + 2", "2x + 2", 520, s)
        if t >= b_:
            for x0, w in ((x_esq("2x + 2", s), larg_f("2x + 2", s)), (x_dir(s), larg_f("2x + 2", s))):
                caixa(c, t, b_, x0, w, 520, s, COR)
        ops(c, t, PW("s14", "Tirando"), "2x + 2", "2x + 2", 520, s, "− 2x", dy=s * 0.85)
        eq(c, t, c_, "2", "2", 760, 130, CERTO)
        xs = selo_eq(c, t, c_ + 0.3, "2", 760, 130)
        E.frase(c, t, c_ + 0.3, ps("verdadeiro", "g", 76, CERTO), xs + 30, 740)
        tt = PW("s14", "Teste")
        E.saida(c, t, tt - 0.1, lambda: E.foco(c, t, d, 0.5, lambda q: E.pilula(c, "todo número serve", W / 2, 940, 80, estilo="g", fundo=CERTO, a=q)))
        E.frase(c, t, tt, ps("teste com", "i", 76) + ps("x = 10:", "g", 72, COR), 360, 960, passo=0.12)
        E.formula_em(c, t, PW("s14", "vinte"), "22 = 22", 1160, 960, 96, "g", CERTO)

    fase(c, t, s11, s13 - 0.1, s11_12)
    fase(c, t, s13, s14 - 0.1, s13_)
    fase(c, t, s14, 1e9, s14_)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s15, s16 = C["s15"], C["s16"]

    def s15_():
        a, b_, c_, d = (C[f"s15.{k}"] for k in "abcd")
        E.frase(c, t, s15 + 0.1, ps("o atalho", "g", 110, BR), W / 2, 170, "center")
        E.frase(c, t, a, ps("abra os parênteses, junte os termos e", "i", 64, CLARO), W / 2, 290, "center", passo=0.08)
        to = PW("s15", "olhe")
        E.frase(c, t, to, ps("olhe o número que multiplica o", "i", 64, CLARO) + ps("x", "g", 64, BR), W / 2, 370, "center", passo=0.08)
        s, y = 130, 560
        esq, dir_ = "2x + 1", "2x + 3"
        eq(c, t, to, esq, dir_, y, s, BR)
        xe = x_esq(esq, s)
        for x0, w in (trecho(esq, "2", xe, s), trecho(dir_, "2", x_dir(s), s)):
            caixa(c, t, b_, x0, w, y, s, CLARO)
        E.frase(c, t, b_, ps("o mesmo:", "i", 76, CLARO) + ps("o x vai sumir", "g", 72, BR), W / 2, 720, "center", passo=0.12)
        for k, (x0, w) in enumerate((trecho(esq, "1", xe, s), trecho(dir_, "3", x_dir(s), s))):
            caixa(c, t, c_ - 0.6 + k * 0.2, x0, w, y, s, ERRADO)
        E.frase(c, t, PW("s15", "Basta"), ps("compare os números sem letra", "i", 60, CLARO), W / 2, 815, "center", passo=0.08)
        E.foco(c, t, c_, 0.45, lambda q: (centro(c, "diferentes:", 560, 905, 60, "i", CLARO, q),
                                           centro(c, "nenhuma solução", 560, 990, 72, "g", BR, q)))
        E.foco(c, t, d, 0.45, lambda q: (centro(c, "iguais:", 1360, 905, 60, "i", CLARO, q),
                                          centro(c, "todo número serve", 1360, 990, 72, "g", BR, q)))

    def s16_():
        a, b_, c_ = C["s16.a"], C["s16.b"], C["s16.c"]
        E.frase(c, t, s16 + 0.1, ps("funciona porque", "i", 84, CLARO), W / 2, 200, "center")
        E.frase(c, t, a, ps("tirar as mesmas caixas de cada prato", "i", 80, BR), W / 2, 330, "center", passo=0.1)
        E.frase(c, t, a + 1.4, ps("deixa só os pesos", "g", 80, BR), W / 2, 440, "center", passo=0.12)
        E.frase(c, t, b_, ps("não vale olhar", "g", 72, "#FF8A8D") + ps("antes de abrir os parênteses", "i", 76, CLARO), W / 2, 620, "center", passo=0.1)
        s, y = 120, 840
        fcen(c, t, c_, "3(x − 2) = 3x − 6", W / 2, y, s, BR)
        w = larg_f("3(x − 2) = 3x − 6", s)
        x0, w3 = trecho("3(x − 2) = 3x − 6", "3x", W / 2 - w / 2, s)
        caixa(c, t, c_ + 0.6, x0, w3, y, s, CLARO)

    fase(c, t, s15, s16 - 0.1, s15_)
    fase(c, t, s16, 1e9, s16_)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"] - 0.3, ps("resolva", "i", 84), XE, 340)
    E.formula_em(c, t, C["s17.a"], "4(x + 1) = x + 19", XE, 520, 120, "g", TINTA)
    E.frase(c, t, C["s17.b"], ps("quanto vale", "i", 110) + ps("x?", "g", 110, COR), XE, 790, passo=0.15)
    E.relogio(c, t, C["s18.a"], 1530, 440, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s19, s20 = C["s19"], C["s20"]

    def s19_():
        a, b_, c_, d, e = (C[f"s19.{k}"] for k in "abcde")
        s = 100
        rot = lambda t0, txt, y: E.foco(c, t, t0, 0.4, lambda q: E.pilula(c, txt, 230, y - s * 0.32, 44, estilo="b", fundo=E.COR, a=q))
        eq(c, t, s19 + 0.2, "4(x + 1)", "x + 19", 190, s, TINTA2)
        rot(a, "abra", 350)
        eq(c, t, a, "4x + 4", "x + 19", 350, s)
        xe = x_esq("4x + 4", s)
        for x0, w in (trecho("4x + 4", "4", xe, s), trecho("x + 19", "x", x_dir(s), s)):
            caixa(c, t, b_, x0, w, 350, s, COR)
        E.foco(c, t, b_ + 0.3, 0.45, lambda q: (centro(c, "4 e 1", 1590, 320, 64, "b", TINTA, q),
                                                 centro(c, "diferentes", 1590, 400, 64, "g", CERTO, q)))
        rot(c_, "− x", 510)
        eq(c, t, c_ + 0.3, "3x + 4", "19", 510, s)
        rot(d, "− 4", 670)
        eq(c, t, d + 0.3, "3x", "15", 670, s)
        rot(e, "÷ 3", 860)
        eq(c, t, e + 0.3, "x", "5", 860, 140, COR)
        selo_eq(c, t, e + 0.7, "5", 860, 140)

    def s20_():
        a, b_, c_ = C["s20.a"], C["s20.b"], C["s20.c"]
        E.frase(c, t, s20 + 0.1, ps("conferindo com", "i", 84) + ps("x = 5", "g", 80, COR), W / 2, 180, "center")
        cl, cr = 560, 1360
        E.foco(c, t, a, 0.4, lambda q: centro(c, "lado esquerdo", cl, 320, 52, "i", TINTA2, q))
        fcen(c, t, a, "5 + 1 = 6", cl, 440, 92)
        fcen(c, t, PW("s20", "Vezes"), "6 × 4 = 24", cl, 570, 92)
        E.foco(c, t, b_, 0.4, lambda q: centro(c, "lado direito", cr, 320, 52, "i", TINTA2, q))
        fcen(c, t, b_, "5 + 19 = 24", cr, 505, 92)
        tb = PW("s20", "Bateu")
        eq(c, t, tb - 0.2, "24", "24", 740, 120, CERTO)
        selo_eq(c, t, tb, "24", 740, 120)
        E.frase(c, t, PW("s20", "Quem"), ps("quem multiplicou só o x:", "i", 72), 330, 940, passo=0.1)
        E.formula_em(c, t, c_, "x = 6", 1180, 945, 96, "g", ERRADO)
        E.foco(c, t, c_ + 0.3, 0.45, lambda q: E.selo(c, 1520, 910, 46, False, q))

    fase(c, t, s19, s20 - 0.1, s19_)
    fase(c, t, s20, 1e9, s20_)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s21.a", ps("abra os", "i", 84) + ps("parênteses primeiro", "g", 80, COR)),
                 (590, "s21.b", ps("resolva", "i", 84) + ps("como antes", "g", 80, COR)),
                 (780, "s21.c", ps("o x sumiu?", "i", 84) + ps("leia o que sobrou", "g", 80, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), 330, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 430, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a_, b_, c_, d_ = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("equação com", "i", 100), XE, 380)
    E.frase(c, t, a_ + 0.4, ps("frações e vírgula", "g", 112, COR), XE, 520, passo=0.15)
    E.frase(c, t, b_, ps("e as frações", "i", 80) + ps("somem", "g", 80, COR), XE, 660, passo=0.13)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1650, p), lerp(650, 405, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, parenteses=b_parenteses, erro=b_erro, some=b_some, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
