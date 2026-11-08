"""Visual — Estudativo · MAT-EQU-013: montar uma equação a partir do problema.
Os quatro passos do método ficam numa pílula no alto ("passo n") enquanto os problemas andam. Os consecutivos viram três
cartões (x, x + 1, x + 2); o dinheiro da carteira vira uma barra dividida em almoço (1/3), passagem (1/4) e sobra (R$ 10).
Equações alinhadas pelo igual (peça eq), com a operação da vez numa pílula à esquerda.
Instantes: cues C[...] e, dentro da frase, a palavra falada (PW, com `apos` para pegar a ocorrência certa)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-013_montar_equacao_problema.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "carteira", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AP = E.APERTO["g"]

x = 27
assert x + (x + 1) + (x + 2) == 84 and 3 * x + 3 == 84 and 3 * x == 81 and 84 // 3 == 28 and 84 % 3 == 0
x = 24
assert x / 3 + x / 4 + 10 == x and 4 * x + 3 * x + 120 == 12 * x and 7 * x + 120 == 12 * x and 5 * x == 120
assert 24 // 3 == 8 and 24 // 4 == 6 and 8 + 6 + 10 == 24
x = 12
assert x + 3 * x == 48 and 4 * x == 48 and 3 * x == 36 and 12 + 36 == 48

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def _n(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


def PW(sid, palavra, apos=None):
    """instante em que a voz diz `palavra` na cena sid (a primeira depois do instante `apos`, se dado)"""
    for s in _TEMPOS["scenes"]:
        if s["id"] == sid:
            for tk in s["tokens"]:
                ti = s["start"] + tk["t0"]
                if _n(tk["disp"]) == _n(palavra) and (apos is None or ti >= apos - 0.05):
                    return ti
    raise KeyError((sid, palavra, apos))


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


def x_dir(size, cx=W / 2):
    return cx + gap(size)


def rot(c, t, t0, txt, y, size):
    """a operação da linha, numa pílula à esquerda"""
    E.foco(c, t, t0, 0.4, lambda q: E.pilula(c, txt, 300, y - size * 0.32, 48, estilo="b", fundo=E.COR, a=q))


def selo_eq(c, t, t0, dir_, y, size, ok=True):
    r = size * 0.4
    x = x_dir(size) + larg_f(dir_, size) + r + size * 0.3
    E.foco(c, t, t0, 0.45, lambda q: E.selo(c, x, y - size * 0.36, r, ok, q))
    return x + r


def selo_dep(c, t, t0, s, x, y, size, ok=True, align="center"):
    w = larg_f(s, size)
    x1 = x + w / 2 if align == "center" else x + w
    r = size * 0.4
    E.foco(c, t, t0, 0.45, lambda q: E.selo(c, x1 + r + size * 0.3, y - size * 0.36, r, ok, q))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def etiqueta(c, t, t0, t1, n):
    """pílula "passo n" no alto, enquanto o problema anda"""
    fase(c, t, t0, t1, lambda: E.foco(c, t, t0, 0.4, lambda q: E.pilula(c, f"passo {n}", XE + 110, 110, 48, estilo="b", a=q), sobe=6))


def cartao(c, cx, cy, w, h, s, a, cor=None, tinta=None, size=92):
    """cartão com uma fórmula dentro"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, cor or M.mix(E.COR, BR, 0.86), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22), M.paint(E.COR, a, stroke=5))
    E.formula(c, s, cx, cy + size * 0.36, size, cor=tinta or COR, a=a, align="center")


def interrogacao(c, cx, cy, s, a):
    p = a
    E.caixa_pontilhada(c, cx - s / 2, cy - s / 2, s, s, p, COR, prog_=p)
    centro(c, "?", cx, cy + s * 0.22, s * 0.6, "g", COR, a)


BX, BW, BY, BH = 260, 1400, 520, 150  # a barra do dinheiro
PARTES = ((0, 1 / 3, E.COR), (1 / 3, 1 / 4, TINTA), (7 / 12, 5 / 12, CERTO))


def barra_dinheiro(c, t, tp, a=1.0):
    """o dinheiro todo como uma barra: tp = instante de cada parte (almoço, passagem, sobra)"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX, BY, BW, BH), 16, 16)
    c.drawRRect(r, M.paint(E.VAZIO, a))
    c.save(); c.clipRRect(r, True)
    for (ini, w, cor), ti in zip(PARTES, tp):
        q = ep(t, ti, 0.5)
        if q > 0:
            c.drawRect(skia.Rect.MakeXYWH(BX + BW * ini, BY, BW * w * q, BH), M.paint(cor, a))
    c.restore()
    for ini in (1 / 3, 7 / 12):
        if t >= tp[1 if ini < 0.5 else 2]:
            M.line(c, BX + BW * ini, BY, BX + BW * ini, BY + BH, BR, a, 5)
    c.drawRRect(r, M.paint(TINTA, a, stroke=4))


def meio_parte(i):
    ini, w, _ = PARTES[i]
    return BX + BW * (ini + w / 2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, a_ + 0.1, ps("três números seguidos", "i", 84) + ps("somam 84", "g", 80, COR), W / 2, 230, "center", passo=0.13)
        for i, cx in enumerate((540, 860, 1180)):
            E.foco(c, t, a_ + 0.8 + i * 0.25, 0.45, lambda q, cx=cx: interrogacao(c, cx, 480, 200, q))
        for i, cx in enumerate((700, 1020)):
            E.foco(c, t, a_ + 1.0 + i * 0.25, 0.4, lambda q, cx=cx: centro(c, "+", cx, 515, 110, "g", TINTA, q))
        E.foco(c, t, a_ + 1.6, 0.4, lambda q: E.formula(c, "= 84", 1320, 520, 120, cor=COR, a=q))
        E.frase(c, t, b_, ps("quais são?", "g", 96, COR), W / 2, 720, "center")
        E.saida(c, t, c_ - 0.1, lambda: E.frase(c, t, PW("s01", "chutando"), ps("dá para chutar...", "i", 84, TINTA2), W / 2, 900, "center", passo=0.12))
        E.frase(c, t, c_, ps("mas existe um jeito que", "i", 80) + ps("nunca falha", "g", 80, COR), W / 2, 900, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, PW("s02", "problema"), [("problema", "g", 120, COR)], XE, 450)
        E.frase(c, t, PW("s02", "problema") + 0.4, [("de texto", "i", 110)], XE, 570)
        E.frase(c, t, PW("s02", "equação"), ps("vira", "i", 110) + ps("equação", "g", 120, COR), XE, 720, passo=0.15)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 505, 80, "g", E.SOBRE, a),
                                                centro(c, "de prova", 1480, 590, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, ps("você só precisa de", "i", 84), XE, 410, passo=0.13)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "Escrever frase", "com letra", "o dobro de um número mais 3", "2x + 3"),
             ("s03.c", "Equação", "com fração", "multiplicar tudo pelo MMC", "f{x}{2} + f{x}{3} = 5"))
    for i, (k, l1, l2, ex_t, ex) in enumerate(itens):
        y = 170 + i * 330
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 290, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62), (l2, "g", 62, COR)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.7, ps(ex_t, "i", 48, TINTA2), x + 44, y + 160, passo=0.06)
        E.formula_em(c, t, C[k] + 1.2, ex, x + 44, y + 250, 70, "g", TINTA2)
    E.frase(c, t, PW("s03", "procure"), ps("faltou? procure no canal", "i", 62), x + 44, 900, passo=0.11)


# ---------------- método ----------------
PASSOS = ((ps("o que você não sabe", "i", 70) + ps("vira x", "g", 70, COR)),
          (ps("escreva cada informação", "i", 70) + ps("com x", "g", 70, COR)),
          (ps("o que é igual a quê?", "i", 70) + ps("monte a equação", "g", 70, COR)),
          (ps("resolva, responda", "g", 70, COR) + ps("e confira no texto", "i", 70)))


def b_metodo(c, t, C, b):
    def quatro():
        E.frase(c, t, C["s04"] + 0.2, ps("o jeito que nunca falha", "i", 90), W / 2, 420, "center", passo=0.13)
        E.frase(c, t, C["s04.a"], [("4", "g", 220, COR), ("passos", "g", 200, COR)], W / 2, 700, "center")
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t < C["s05"]:
        return
    for i, k in enumerate("abcd"):
        y = 250 + i * 210
        ti = C[f"s05.{k}"]
        E.foco(c, t, ti, 0.5, lambda q, i=i, y=y: num_bola(c, str(i + 1), XE + 80, y - 26, 62, 72, q))
        E.frase(c, t, ti + 0.15, PASSOS[i], XE + 200, y, passo=0.1)


# ---------------- consecutivos ----------------
CX3 = (480, 960, 1440)


def b_consecutivos(c, t, C, b):
    t6, t7, t8, t9, t10 = (C[f"s{i:02d}"] for i in range(6, 11))

    def s06():
        a, b_, c_ = C["s06.a"], C["s06.b"], C["s06.c"]
        E.frase(c, t, t6 + 0.2, ps("primeiro problema", "i", 72, TINTA2), W / 2, 170, "center")
        E.frase(c, t, a, ps("números", "i", 100) + ps("consecutivos", "g", 100, COR), W / 2, 310, "center", passo=0.13)
        E.frase(c, t, a + 1.1, ps("seguidos: um logo depois do outro", "i", 72), W / 2, 420, "center", passo=0.1)
        for i, (s, cx) in enumerate(zip(("7", "8", "9"), (660, 960, 1260))):
            ti = PW("s06", ("sete", "oito", "nove")[i])
            E.foco(c, t, ti, 0.45, lambda q, s=s, cx=cx: num_bola(c, s, cx, 750, 100, 120, q))
        for i in range(2):
            E.salto(c, t, c_ + i * 0.4, (660, 960)[i], (960, 1260)[i], 640, 80, COR, "+1", size=60)
        E.frase(c, t, c_ + 0.8, ps("cada um:", "i", 72) + ps("1 a mais que o anterior", "g", 66, COR), W / 2, 980, "center", passo=0.1)

    def s07_08():
        a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
        a8, b8 = C["s08.a"], C["s08.b"]
        etiqueta(c, t, a7, b7 - 0.1, 1)
        etiqueta(c, t, b7, a8 - 0.1, 2)
        etiqueta(c, t, a8, t9 - 0.1, 3)
        for i, (nome, s, ti) in enumerate((("primeiro", "x", a7 + 0.6), ("segundo", "x + 1", c7), ("terceiro", "x + 2", d7))):
            E.foco(c, t, ti - 0.2, 0.4, lambda q, i=i, nome=nome: centro(c, nome, CX3[i], 260, 56, "i", TINTA2, q))
            E.foco(c, t, ti, 0.45, lambda q, i=i, s=s: cartao(c, CX3[i], 400, 360, 170, s, q))
        E.frase(c, t, b7, ps("o seguinte:", "i", 66) + ps("1 a mais", "g", 62, COR), W / 2, 580, "center", passo=0.1)
        E.frase(c, t, a8, ps("a soma é igual a", "i", 80) + ps("84", "g", 80, COR), W / 2, 700, "center", passo=0.12)
        s, y = 100, 880
        pecas = (("x", b8), (" + (x + 1)", PW("s08", "um", b8)), (" + (x + 2)", PW("s08", "dois", b8)), (" = 84", PW("s08", "igual", b8)))
        total = larg_f("x + (x + 1) + (x + 2) = 84", s)
        xx = W / 2 - total / 2
        for p_, ti in pecas:
            E.formula_em(c, t, ti, p_.strip() if p_ == "x" else p_, xx, y, s, "g", COR if "84" in p_ else TINTA)
            xx += larg_f(p_, s)

    def s09():
        a, b_, c_, d, e, f = (C[f"s09.{k}"] for k in "abcdef")
        etiqueta(c, t, a, t10 - 0.1, 4)
        s = 100
        eq(c, t, t9 + 0.1, "x + (x + 1) + (x + 2)", "84", 270, 92, TINTA2)
        rot(c, t, b_ - 0.4, "junte", 450, s)
        eq(c, t, b_, "3x + 3", "84", 450, s)
        rot(c, t, c_, "− 3", 630, s)
        eq(c, t, d, "3x", "81", 630, s)
        rot(c, t, e, "÷ 3", 850, 140)
        eq(c, t, f, "x", "27", 850, 140, COR)

    def s10():
        a, b_, c_, d = (C[f"s10.{k}"] for k in "abcd")
        E.frase(c, t, a, ps("a pergunta pede", "i", 84) + ps("os 3 números", "g", 80, COR), W / 2, 220, "center", passo=0.12)
        for i, (s, w) in enumerate((("27", "sete"), ("28", "oito"), ("29", "nove"))):
            ti = PW("s10", w, b_)
            E.foco(c, t, ti, 0.45, lambda q, i=i, s=s: num_bola(c, s, (660, 960, 1260)[i], 480, 110, 110, q))
        fcen(c, t, c_, "27 + 28 + 29 = 84", W / 2, 800, 120, CERTO)
        selo_dep(c, t, d, "27 + 28 + 29 = 84", W / 2, 800, 120)

    fase(c, t, t6, t7 - 0.1, s06)
    fase(c, t, t7, t9 - 0.1, s07_08)
    fase(c, t, t9, t10 - 0.1, s09)
    fase(c, t, t10, 1e9, s10)


# ---------------- carteira ----------------
def b_carteira(c, t, C, b):
    t11, t12, t13, t14, t15 = (C[f"s{i}"] for i in range(11, 16))

    def s11_12():
        a, b_, c_, d = (C[f"s11.{k}"] for k in "abcd")
        a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
        E.frase(c, t, t11 + 0.2, ps("segundo problema:", "i", 66, TINTA2) + ps("com fração", "g", 62, COR), XE, 150, passo=0.1)
        E.frase(c, t, PW("s11", "carteira"), ps("saiu de casa com um dinheiro na carteira", "i", 70), XE, 250, passo=0.09)
        E.foco(c, t, PW("s11", "carteira"), 0.5, lambda q: barra_dinheiro(c, t, (a, b_, c_), q))
        for i, (nome, ti, f1, f2, t2) in enumerate((("almoço", a, "f{1}{3}", "f{x}{3}", b2), ("passagem", b_, "f{1}{4}", "f{x}{4}", c2),
                                                     ("sobrou", c_, "R$ 10", "10", 1e9))):
            cx = meio_parte(i)
            E.foco(c, t, ti + 0.2, 0.4, lambda q, cx=cx, nome=nome: centro(c, nome, cx, BY + BH + 70, 56, "i", TINTA2, q))
            if t < t2 + 0.3:
                E.saida(c, t, t2, lambda cx=cx, f1=f1, ti=ti: E.foco(c, t, ti + 0.3, 0.4, lambda q: E.formula(c, f1, cx, BY + BH + 190, 84, cor=PARTES[i][2] if i != 1 else TINTA, a=q, align="center")))
            E.foco(c, t, t2 + 0.2, 0.4, lambda q, cx=cx, f2=f2: E.formula(c, f2, cx, BY + BH + 190, 84, cor=COR, a=q, align="center"))
        q = ep(t, d, 0.5)
        E.chave(c, BX, BX + BW, BY - 24, COR, q, -22, 5)
        if t < a2 + 0.3:
            E.saida(c, t, a2, lambda: E.foco(c, t, d, 0.45, lambda q: centro(c, "com quanto saiu?", W / 2, BY - 70, 66, "g", COR, q)))
        E.foco(c, t, a2 + 0.2, 0.45, lambda q: centro(c, "x", W / 2, BY - 64, 96, "g", COR, q))
        E.frase(c, t, d2, ps("almoço + passagem + sobra", "g", 58), XE, 1010, passo=0.12)
        E.frase(c, t, e2, ps("= o dinheiro todo", "g", 58, COR), 1000, 1010, passo=0.12)

    def s13():
        a, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
        s = 110
        eq(c, t, a, "f{x}{3} + f{x}{4} + 10", "x", 330, s)
        E.foco(c, t, PW("s13", "MMC"), 0.45, lambda q: E.pilula(c, "MMC(3, 4) = 12", 1560, 160, 52, estilo="b", a=q))
        E.frase(c, t, b_, ps("× 12 em cada termo,", "g", 70, COR) + ps("até o 10", "i", 76), W / 2, 560, "center", passo=0.11)
        eq(c, t, c_, "4x + 3x + 120", "12x", 800, s)

    def s14():
        a, b_, c_, d, e = (C[f"s14.{k}"] for k in "abcde")
        s = 104
        eq(c, t, t14 + 0.1, "4x + 3x + 120", "12x", 250, s, TINTA2)
        rot(c, t, PW("s14", "Junte"), "junte", 430, s)
        eq(c, t, a, "7x + 120", "12x", 430, s)
        rot(c, t, b_, "− 7x", 610, s)
        eq(c, t, c_, "120", "5x", 610, s)
        rot(c, t, d, "÷ 5", 830, 140)
        eq(c, t, e, "x", "24", 830, 140, COR)

    def s15():
        a, b_, c_, d = (C[f"s15.{k}"] for k in "abcd")
        E.frase(c, t, a, ps("ela saiu com", "i", 84) + ps("R$ 24", "g", 84, COR), W / 2, 200, "center", passo=0.12)
        E.foco(c, t, PW("s15", "Confira"), 0.5, lambda q: barra_dinheiro(c, t, (b_, c_, d), q))
        E.chave(c, BX, BX + BW, BY - 24, COR, ep(t, a, 0.5), -22, 5)
        E.foco(c, t, a + 0.2, 0.45, lambda q: centro(c, "R$ 24", W / 2, BY - 64, 80, "g", COR, q))
        for i, (ti, s, val) in enumerate(((b_, "f{1}{3} de 24 = 8", "8"), (c_, "f{1}{4} de 24 = 6", "6"), (d, "", "10"))):
            cx = meio_parte(i)
            E.foco(c, t, ti + 0.3, 0.4, lambda q, cx=cx, val=val: centro(c, val, cx, BY + BH / 2 + 30, 84, "g", BR, q))
            if s:
                E.foco(c, t, ti, 0.4, lambda q, cx=cx, s=s: E.formula(c, s, cx, BY + BH + 130, 60, cor=TINTA2, a=q, align="center"))
        fcen(c, t, d, "8 + 6 + 10 = 24", W / 2, 970, 110, CERTO)
        selo_dep(c, t, d + 0.6, "8 + 6 + 10 = 24", W / 2, 970, 110)

    fase(c, t, t11, t13 - 0.1, s11_12)
    fase(c, t, t13, t14 - 0.1, s13)
    fase(c, t, t14, t15 - 0.1, s14)
    fase(c, t, t15, 1e9, s15)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d = (C[f"s16.{k}"] for k in "abcd")
    E.frase(c, t, C["s16"] + 0.1, ps("cuidado:", "g", 90, ERRADO) + ps("um erro muito comum", "i", 96), W / 2, 190, "center", passo=0.12)
    E.frase(c, t, a, ps("achar o x e", "i", 84) + ps("parar ali", "g", 80, ERRADO), W / 2, 330, "center", passo=0.12)
    E.frase(c, t, b_ - 0.3, ps("resposta:", "i", 84), 560, 500)
    E.formula_em(c, t, b_, "só 27", 900, 505, 110, "g", ERRADO)
    E.foco(c, t, c_, 0.45, lambda q: E.selo(c, 1300, 465, 50, False, q))
    E.frase(c, t, c_, ps("27 sozinho não soma 84", "i", 72), W / 2, 640, "center", passo=0.1)
    for i, s in enumerate(("27", "28", "29")):
        E.foco(c, t, d + i * 0.2, 0.45, lambda q, i=i, s=s: num_bola(c, s, (760, 960, 1160)[i], 770, 70, 76, q, COR if i == 0 else CINZA))
    E.foco(c, t, d + 0.3, 0.4, lambda q: centro(c, "x", 760, 890, 60, "g", COR, q))
    E.frase(c, t, PW("s16", "Sempre"), ps("sempre volte à", "i", 76) + ps("pergunta", "g", 72, COR), W / 2, 1010, "center", passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    t17, t18 = C["s17"], C["s18"]

    def s17():
        a, b_, c_, d = (C[f"s17.{k}"] for k in "abcd")
        E.frase(c, t, t17 + 0.1, ps("o atalho prometido", "i", 84, CLARO), W / 2, 170, "center")
        E.frase(c, t, a, ps("3 números seguidos:", "i", 80, CLARO) + ps("soma ÷ 3", "g", 80, BR), W / 2, 310, "center", passo=0.12)
        E.frase(c, t, b_, ps("=", "g", 80, BR) + ps("o do meio", "g", 80, BR), W / 2, 420, "center", passo=0.12)
        fcen(c, t, c_, "84 ÷ 3 = 28", W / 2, 600, 130, BR)
        E.foco(c, t, d - 0.6, 0.45, lambda q: num_bola(c, "28", 960, 820, 90, 96, q))
        E.foco(c, t, d, 0.45, lambda q: num_bola(c, "27", 700, 820, 80, 84, q, E.mix(E.COR, "#000000", 0.2), CLARO))
        E.foco(c, t, d + 0.5, 0.45, lambda q: num_bola(c, "29", 1220, 820, 80, 84, q, E.mix(E.COR, "#000000", 0.2), CLARO))

    def s18():
        a, b_, c_ = C["s18.a"], C["s18.b"], C["s18.c"]
        E.frase(c, t, t18 + 0.1, ps("funciona porque", "i", 84, CLARO), W / 2, 170, "center")
        for i, s in enumerate(("27", "28", "29")):
            E.foco(c, t, t18 + 0.2, 0.45, lambda q, i=i, s=s: num_bola(c, s, (660, 960, 1260)[i], 470, 80, 84, q))
        E.salto(c, t, a, 960, 660, 380, 70, CLARO, "−1", size=60)
        E.salto(c, t, a + 1.0, 960, 1260, 380, 70, CLARO, "+1", size=60)
        E.frase(c, t, PW("s18", "compensa"), ps("um compensa o outro", "g", 76, BR), W / 2, 670, "center", passo=0.12)
        E.frase(c, t, b_, ps("4 números seguidos?", "g", 72, "#FF8A8D") + ps("não tem o do meio", "i", 76, CLARO), W / 2, 830, "center", passo=0.11)
        E.frase(c, t, c_, ps("aí, a", "i", 84, CLARO) + ps("equação resolve", "g", 84, BR), W / 2, 970, "center", passo=0.12)

    fase(c, t, t17, t18 - 0.1, s17)
    fase(c, t, t18, 1e9, s18)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_ = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s19"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, a, ps("o pai tem o", "i", 84) + ps("triplo", "g", 80, COR), XE, 350, passo=0.12)
    E.frase(c, t, a + 0.9, ps("da idade do filho", "i", 84), XE, 450, passo=0.12)
    E.frase(c, t, PW("s19", "ou"), ps("(3 vezes a idade dele)", "i", 62, TINTA2), XE, 540, passo=0.08)
    E.frase(c, t, b_, ps("somadas:", "i", 84) + ps("48 anos", "g", 80, COR), XE, 680, passo=0.12)
    E.frase(c, t, c_, ps("qual é a idade", "i", 100) + ps("do pai?", "g", 96, COR), XE, 860, passo=0.13)
    E.relogio(c, t, C["s20.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t21, t22 = C["s21"], C["s22"]

    def s21():
        a, b_, c_, d, e = (C[f"s21.{k}"] for k in "abcde")
        E.foco(c, t, a, 0.45, lambda q: cartao(c, 640, 230, 420, 150, "filho: x", q, size=80))
        E.foco(c, t, b_, 0.45, lambda q: cartao(c, 1280, 230, 420, 150, "pai: 3x", q, size=80))
        s = 110
        eq(c, t, c_, "x + 3x", "48", 470, s)
        rot(c, t, d - 0.3, "junte", 650, s)
        eq(c, t, d, "4x", "48", 650, s)
        rot(c, t, PW("s21", "Dividindo"), "÷ 4", 860, 140)
        eq(c, t, e, "x", "12", 860, 140, COR)

    def s22():
        a, b_, c_, d = (C[f"s22.{k}"] for k in "abcd")
        E.frase(c, t, t22 + 0.1, ps("cuidado:", "g", 84, ERRADO) + ps("12 é a idade", "i", 88) + ps("do filho", "g", 84, COR), W / 2, 220, "center", passo=0.12)
        fcen(c, t, b_, "pai = 3 × 12 = 36 anos", W / 2, 480, 120, COR)
        E.frase(c, t, c_ - 0.3, ps("conferindo:", "i", 72, TINTA2), W / 2, 680, "center")
        fcen(c, t, c_, "12 + 36 = 48", W / 2, 840, 120, CERTO)
        selo_dep(c, t, d, "12 + 36 = 48", W / 2, 840, 120)

    fase(c, t, t21, t22 - 0.1, s21)
    fase(c, t, t22, 1e9, s22)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s23.a", ps("o desconhecido", "i", 84) + ps("vira x", "g", 80, COR)),
                 (590, "s23.b", ps("cada informação", "i", 84) + ps("vira conta", "g", 80, COR)),
                 (780, "s23.c", ps("responda", "i", 84) + ps("o que a pergunta pede", "g", 80, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), 330, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 430, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a_, b_, c_, d_ = (C[f"s24.{k}"] for k in "abcd")
    E.frase(c, t, C["s24"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("comparar", "g", 120, COR), XE, 390)
    E.frase(c, t, a_ + 0.4, ps("dois planos", "g", 120, COR), XE, 520)
    E.frase(c, t, PW("s24", "celular"), ps("de celular", "i", 84), XE, 630)
    E.frase(c, t, b_, ps("com quantos minutos custam o mesmo", "i", 66), XE, 750, passo=0.1)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1650, p), lerp(650, 405, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, consecutivos=b_consecutivos, carteira=b_carteira,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
