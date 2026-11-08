"""Visual — Estudativo · MAT-EQU-012: praticando equações do 1º grau.
Aula de prática: cinco equações, uma de cada tipo, cada uma com selo de progresso, relógio de pausa e a resolução em
linhas alinhadas pelo igual (peça eq), com a operação da vez numa pílula à esquerda. Conferência em duas colunas.
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
ARQUIVO_FINAL = "estudativo_MAT-EQU-012_praticando_equacoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao3", "questao5", "fim"))
BR = "#FFFFFF"
AP = E.APERTO["g"]

x = 7
assert x + 13 == 4 * x - 8 == 20 and 3 * x - 8 == 13 and 3 * x == 21 and 4 * 7 == 28
assert -3 * 7 + 13 == -8  # tirando 4x: −3x + 13 = −8
x = 3
assert 2 * (x + 4) == 5 * x - 1 == 14 and 3 * x - 1 == 8 and 3 * x == 9
x = 15
assert x / 3 - 2 == x / 5 == 3 and 5 * x - 30 == 3 * x and 2 * x == 30 and 15 % 3 == 0 and 15 % 5 == 0
assert 1 / 3 - 2 < 0 < 1 / 5 and 5 * 1 - 2 == 3 * 1  # quem esquece o 2: 5x − 2 = 3x dá x = 1
x = 10
assert abs(0.2 * x + 3 - 0.5 * x) < 1e-9 and 2 * x + 30 == 5 * x and 3 * x == 30
assert 18 / 12 == 1.5 and 12 * 1.5 == 18

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


def caixa(c, t, t0, x0, w, y, size, cor=None):
    q = ep(t, t0, 0.45)
    E.caixa_pontilhada(c, x0 - size * 0.18, y - size * 0.92, w + size * 0.36, size * 1.18, q, cor or COR, prog_=q)


def ops(c, t, t0, esq, dir_, y, size, txt, cor=None, dy=None):
    ce, cd = lados(esq, dir_, size)
    yy = y + (dy or size * 0.78)
    E.foco(c, t, t0, 0.4, lambda a: (E.pilula(c, txt, ce, yy, 46, estilo="b", fundo=cor or E.COR, a=a),
                                      E.pilula(c, txt, cd, yy, 46, estilo="b", fundo=cor or E.COR, a=a)), sobe=6)


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


def marca(c, t, t0, n):
    """equação n de 5, com cinco pontos de progresso"""
    s = f"equação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, C, sid, n, esq, dir_, rel):
    """tela da questão: selo de progresso, a equação, a pergunta e o relógio"""
    a, b_, c_ = C[f"{sid}.a"], C[f"{sid}.b"], C[f"{sid}.c"]
    marca(c, t, a, n)
    E.frase(c, t, a, ps(f"equação {n}", "i", 80, COR), XE, 300)
    E.formula_em(c, t, b_, f"{esq} = {dir_}", XE, 520, 130, "g", TINTA)
    E.frase(c, t, c_, ps("quanto vale", "i", 110) + ps("x?", "g", 110, COR), XE, 800, passo=0.15)
    E.relogio(c, t, rel, 1530, 440, 190)


def conferir(c, t, t0, esq, dir_, tb, y0=220, x_=None):
    """conferência em duas colunas: esq e dir_ = [(instante, fórmula), ...]; tb = instante do 'bateu'"""
    E.frase(c, t, t0, ps("conferindo", "i", 84, COR) + ([("x = " + x_, "g", 80, COR)] if x_ else []), W / 2, y0, "center")
    cl, cr = 560, 1360
    for cx, lista, nome in ((cl, esq, "lado esquerdo"), (cr, dir_, "lado direito")):
        E.foco(c, t, lista[0][0], 0.4, lambda q, cx=cx, nome=nome: centro(c, nome, cx, y0 + 140, 52, "i", TINTA2, q))
        for i, (ti, s) in enumerate(lista):
            fcen(c, t, ti, s, cx, y0 + 270 + i * 140, 92)
    return tb


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("equações", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, PW("s01", "criadas"), ps("criadas para esta aula", "i", 80), XE, 480, passo=0.15)
    E.frase(c, t, PW("s01", "uma"), ps("uma de cada tipo", "i", 80) + ps("que você viu", "i", 80, TINTA2), XE, 590, passo=0.15)
    for i, (s, cx, ti) in enumerate((("pause", 440, b_), ("resolva", 960, PW("s01", "resolva")), ("confira", 1480, c_))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 800, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 825, 92, "g", TINTA, p)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    a, b_, c_ = C["s02.a"], C["s02.b"], C["s02.c"]
    E.frase(c, t, C["s02"] + 0.1, ps("a ferramenta é uma só", "i", 84, COR), XE, 220, passo=0.12)
    E.frase(c, t, a, ps("faça o mesmo", "g", 96, COR), XE, 360)
    E.frase(c, t, a + 0.6, ps("nos dois lados", "g", 96), XE, 470)
    E.foco(c, t, a, 0.5, lambda q: E.balanca(c, 1420, 470, "x + 7", "12", 0, q, 84, larg_braco=500))
    E.frase(c, t, b_ - 0.6, ps("antes, às vezes:", "i", 70, TINTA2), XE, 620)
    E.frase(c, t, b_, ps("abrir parênteses", "g", 72), XE, 720)
    E.frase(c, t, c_, ps("sumir com frações e vírgulas", "g", 72), XE, 820)
    E.frase(c, t, PW("s02", "procure"), ps("travou? procure a aula no canal", "i", 62), XE, 960, passo=0.11)


# ---------------- equação 1 ----------------
def b_questao1(c, t, C, b):
    pergunta(c, t, C, "s03", 1, "x + 13", "4x − 8", C["s04.a"])


def b_resposta1(c, t, C, b):
    t5, t6 = C["s05"], C["s06"]
    marca(c, t, t5 - 0.5, 1)

    def s05():
        a, b_, c_, d, e = (C[f"s05.{k}"] for k in "abcde")
        s = 104
        eq(c, t, t5 + 0.1, "x + 13", "4x − 8", 250, s, TINTA2)
        x0, w = trecho("4x − 8", "4x", x_dir(s), s)
        caixa(c, t, a, x0, w, 250, s)
        E.foco(c, t, a + 0.2, 0.4, lambda q: E.pilula(c, "mais x", x0 + w / 2, 115, 48, estilo="b", a=q))
        rot(c, t, b_, "− x", 410, s)
        eq(c, t, b_ + 0.3, "13", "3x − 8", 410, s)
        rot(c, t, c_, "+ 8", 570, s)
        eq(c, t, c_ + 0.3, "21", "3x", 570, s)
        rot(c, t, d, "÷ 3", 730, s)
        eq(c, t, d + 0.3, "7", "x", 730, s)
        eq(c, t, e, "x", "7", 920, 140, COR)
        selo_eq(c, t, e + 0.4, "7", 920, 140)

    def s06():
        a, b_ = C["s06.a"], C["s06.b"]
        conferir(c, t, t6 + 0.1, [(a, "7 + 13 = 20")], [(b_, "4 × 7 = 28"), (PW("s06", "Menos"), "28 − 8 = 20")], 0, x_="7")
        tb = PW("s06", "Bateu")
        eq(c, t, tb - 0.2, "20", "20", 860, 130, CERTO)
        selo_eq(c, t, tb, "20", 860, 130)

    fase(c, t, t5, t6 - 0.1, s05)
    fase(c, t, t6, 1e9, s06)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a, b_, c_, d = (C[f"s07.{k}"] for k in "abcd")
    E.frase(c, t, C["s07"] + 0.1, ps("aqui vale o atalho", "i", 84, CLARO), W / 2, 160, "center")

    def um():
        E.frase(c, t, a, ps("deixe o x no lado com", "i", 76, CLARO) + ps("mais x", "g", 72, BR), W / 2, 290, "center", passo=0.1)
        E.frase(c, t, a + 1.4, ps("mesmo que seja o direito", "i", 72, CLARO), W / 2, 380, "center", passo=0.1)
        s = 104
        eq(c, t, a + 0.3, "x + 13", "4x − 8", 540, s, BR)
        x0, w = trecho("4x − 8", "4x", x_dir(s), s)
        caixa(c, t, a + 0.8, x0, w, 540, s, CLARO)
        E.foco(c, t, b_, 0.45, lambda q: (centro(c, "tirando x", 560, 690, 56, "i", CLARO, q),
                                           E.formula(c, "13 = 3x − 8", 560, 800, 92, cor=BR, a=q, align="center"),
                                           centro(c, "positivo", 560, 900, 64, "g", "#7EE2B0", q)))
        E.foco(c, t, c_, 0.45, lambda q: (centro(c, "tirando 4x", 1360, 690, 56, "i", CLARO, q),
                                           E.formula(c, "−3x + 13 = −8", 1360, 800, 92, cor=BR, a=q, align="center"),
                                           centro(c, "um sinal a mais", 1360, 900, 64, "g", "#FF8A8D", q)))
    E.saida(c, t, d - 0.1, um)
    E.frase(c, t, d, ps("x num lado só?", "g", 96, BR), W / 2, 480, "center", passo=0.12)
    E.frase(c, t, d + 1.0, ps("aí não faz diferença", "i", 100, CLARO), W / 2, 640, "center", passo=0.12)
    E.formula_em(c, t, d + 1.6, "2x + 3 = 11", W / 2, 840, 100, "g", CLARO, "center")


# ---------------- equação 2 ----------------
def b_questao2(c, t, C, b):
    pergunta(c, t, C, "s08", 2, "2(x + 4)", "5x − 1", C["s09.a"])


def b_resposta2(c, t, C, b):
    t10, t11 = C["s10"], C["s11"]
    marca(c, t, t10 - 0.5, 2)

    def s10():
        a, b_, c_, d, e = (C[f"s10.{k}"] for k in "abcde")
        s = 104
        eq(c, t, t10 + 0.1, "2(x + 4)", "5x − 1", 230, s, TINTA2)
        rot(c, t, a, "abra", 390, s)
        eq(c, t, a + 0.3, "2x + 8", "5x − 1", 390, s)
        rot(c, t, b_, "− 2x", 550, s)
        eq(c, t, c_, "8", "3x − 1", 550, s)
        rot(c, t, d, "+ 1", 710, s)
        eq(c, t, d + 0.3, "9", "3x", 710, s)
        rot(c, t, e - 0.3, "÷ 3", 910, 140)
        eq(c, t, e, "x", "3", 910, 140, COR)
        selo_eq(c, t, e + 0.4, "3", 910, 140)

    def s11a():
        a, b_ = C["s11.a"], C["s11.b"]
        conferir(c, t, t11 + 0.1, [(a, "3 + 4 = 7"), (PW("s11", "Vezes"), "7 × 2 = 14")],
                 [(b_, "5 × 3 = 15"), (PW("s11", "Menos"), "15 − 1 = 14")], 0, x_="3")
        tb = PW("s11", "Bateu")
        eq(c, t, tb - 0.2, "14", "14", 860, 130, CERTO)
        selo_eq(c, t, tb, "14", 860, 130)

    def s11b():
        c_, d = C["s11.c"], C["s11.d"]
        E.frase(c, t, c_ - 0.8, ps("e se o lado direito fosse", "i", 80), W / 2, 250, "center", passo=0.11)
        s = 112
        eq(c, t, c_, "2(x + 4)", "2x + 5", 440, s)
        caixa(c, t, c_ + 0.3, x_dir(s), larg_f("2x + 5", s), 440, s)
        eq(c, t, PW("s11", "sumiria"), "2x + 8", "2x + 5", 620, s)
        eq(c, t, d, "8", "5", 820, 140, ERRADO)
        xs = selo_eq(c, t, d + 0.3, "5", 820, 140, False)
        E.frase(c, t, PW("s11", "nenhum"), ps("nenhum número serve", "g", 72, ERRADO), W / 2, 980, "center", passo=0.1)

    fase(c, t, t10, t11 - 0.1, s10)
    fase(c, t, t11, C["s11.c"] - 0.9, s11a)
    fase(c, t, C["s11.c"] - 0.8, 1e9, s11b)


# ---------------- equação 3 ----------------
def b_questao3(c, t, C, b):
    pergunta(c, t, C, "s12", 3, "f{x}{3} − 2", "f{x}{5}", C["s13.a"])


def b_resposta3(c, t, C, b):
    t14, t15 = C["s14"], C["s15"]
    marca(c, t, t14 - 0.5, 3)

    def s14():
        a, b_, c_, d = (C[f"s14.{k}"] for k in "abcd")
        eq(c, t, t14 + 0.1, "f{x}{3} − 2", "f{x}{5}", 300, 120, TINTA2)
        E.foco(c, t, a, 0.45, lambda q: E.pilula(c, "MMC(3, 5) = 15", 1560, 260, 52, estilo="b", a=q))
        E.frase(c, t, PW("s14", "Multiplique"), ps("× 15 em cada termo,", "g", 64, COR) + ps("até no número sem fração", "i", 66),
                W / 2, 460, "center", passo=0.1)
        for ti, s, y in ((b_, "f{x}{3} × 15 = 5x", 620), (c_, "−2 × 15 = −30", 780), (d, "f{x}{5} × 15 = 3x", 950)):
            fcen(c, t, ti, s, W / 2, y, 88)

    def s15a():
        a, b_, c_, d = (C[f"s15.{k}"] for k in "abcd")
        s = 108
        eq(c, t, a, "5x − 30", "3x", 260, s)
        rot(c, t, b_, "− 3x", 440, s)
        eq(c, t, b_ + 0.3, "2x − 30", "0", 440, s)
        rot(c, t, c_, "+ 30", 620, s)
        eq(c, t, c_ + 0.3, "2x", "30", 620, s)
        rot(c, t, d - 0.3, "÷ 2", 840, 140)
        eq(c, t, d, "x", "15", 840, 140, COR)
        selo_eq(c, t, d + 0.4, "15", 840, 140)

    def s15b():
        e, f, g, h = (C[f"s15.{k}"] for k in "efgh")
        conferir(c, t, e - 0.3, [(e, "f{15}{3} = 5"), (PW("s15", "Menos", e), "5 − 2 = 3")], [(f, "f{15}{5} = 3")], 0, x_="15")
        tb = PW("s15", "Bateu")
        eq(c, t, tb - 0.2, "3", "3", 790, 100, CERTO)
        selo_eq(c, t, tb, "3", 790, 100)
        E.frase(c, t, PW("s15", "Quem"), ps("quem esquece de multiplicar o 2:", "i", 64), XE + 60, 910, passo=0.1)
        E.formula_em(c, t, g, "x = 1", 1250, 915, 92, "g", ERRADO)
        E.foco(c, t, g + 0.3, 0.45, lambda q: E.selo(c, 1580, 880, 42, False, q))
        E.foco(c, t, h, 0.45, lambda q: (E.formula(c, "f{1}{3} − 2 < 0", XE + 60, 1030, 60, cor=ERRADO, a=q),
                                          E.formula(c, "f{1}{5} > 0", 1000, 1030, 60, cor=TINTA, a=q)))

    fase(c, t, t14, t15 - 0.1, s14)
    fase(c, t, t15, C["s15.e"] - 0.4, s15a)
    fase(c, t, C["s15.e"] - 0.3, 1e9, s15b)


# ---------------- equação 4 ----------------
def b_questao4(c, t, C, b):
    pergunta(c, t, C, "s16", 4, "0,2x + 3", "0,5x", C["s17.a"])


def b_resposta4(c, t, C, b):
    t18 = C["s18"]
    a, b_, c_, d, e, f = (C[f"s18.{k}"] for k in "abcdef")
    marca(c, t, t18 - 0.5, 4)

    def resolve():
        s = 104
        eq(c, t, t18 + 0.1, "0,2x + 3", "0,5x", 250, s, TINTA2)
        E.frase(c, t, PW("s18", "Nenhum"), ps("só uma casa depois da vírgula", "i", 56, TINTA2), W / 2, 340, "center", passo=0.08)
        rot(c, t, a, "× 10", 450, s)
        eq(c, t, b_, "2x + 30", "5x", 450, s)
        rot(c, t, c_, "− 2x", 630, s)
        eq(c, t, c_ + 0.3, "30", "3x", 630, s)
        rot(c, t, d - 0.3, "÷ 3", 850, 140)
        eq(c, t, d, "x", "10", 850, 140, COR)
        selo_eq(c, t, d + 0.4, "10", 850, 140)

    def confere():
        conferir(c, t, e - 0.3, [(e, "0,2 × 10 = 2"), (PW("s18", "Mais", e), "2 + 3 = 5")], [(f, "0,5 × 10 = 5")], 0, x_="10")
        tb = PW("s18", "Bateu")
        eq(c, t, tb - 0.2, "5", "5", 860, 130, CERTO)
        selo_eq(c, t, tb, "5", 860, 130)

    fase(c, t, t18, e - 0.4, resolve)
    fase(c, t, e - 0.3, 1e9, confere)


# ---------------- equação 5 ----------------
def b_questao5(c, t, C, b):
    a, b_, c_, d = (C[f"s19.{k}"] for k in "abcd")
    marca(c, t, a, 5)
    E.frase(c, t, a, ps("a última,", "i", 80, COR) + ps("com fórmula", "g", 74, COR), XE, 280, passo=0.12)
    E.frase(c, t, PW("s19", "ciclista"), ps("um ciclista pedala a", "i", 80), XE, 420, passo=0.12)
    E.formula_em(c, t, b_, "12 km/h", 880, 420, 100, "g", COR)
    E.frase(c, t, c_, ps("quanto tempo para", "i", 96), XE, 600, passo=0.13)
    E.formula_em(c, t, PW("s19", "dezoito"), "18 km?", 900, 600, 110, "g", COR)
    p = ep(t, d, 0.45)
    E.caixa_pontilhada(c, XE - 10, 730, 560, 150, p, prog_=p)
    E.formula_em(c, t, d + 0.4, "d = v · t", XE + 30, 840, 110, "g", TINTA)
    E.relogio(c, t, C["s20.a"], 1530, 440, 190)


def b_resposta5(c, t, C, b):
    t21, t22 = C["s21"], C["s22"]
    marca(c, t, t21 - 0.5, 5)

    def s21():
        a, b_, c_, d = (C[f"s21.{k}"] for k in "abcd")
        s = 112
        eq(c, t, t21 + 0.1, "d", "v · t", 220, 96, TINTA2)
        eq(c, t, a, "18", "12 · t", 420, s)
        ops(c, t, b_, "18", "12 · t", 420, s, "÷ 12")
        eq(c, t, c_, "t", "18 ÷ 12 = 1,5", 660, s, COR)
        E.frase(c, t, d - 0.1, ps("conferindo:", "i", 72, TINTA2), XE, 880)
        E.formula_em(c, t, d, "12 × 1,5 = 18", 720, 885, 100, "g", TINTA)
        selo_dep(c, t, PW("s21", "Bateu"), "12 × 1,5 = 18", 720, 885, 100, align="left")

    def s22():
        a, b_, c_ = C["s22.a"], C["s22.b"], C["s22.c"]
        E.frase(c, t, t22 + 0.1, ps("cuidado na resposta", "g", 84, ERRADO), W / 2, 230, "center")
        fcen(c, t, a, "1,5 h = 1 hora e meia", W / 2, 400, 110, COR)
        tm = PW("s22", "sessenta")
        E.foco(c, t, tm, 0.45, lambda q: E.formula(c, "1 h = 60 min", 560, 560, 92, cor=TINTA, a=q, align="center"))
        E.foco(c, t, PW("s22", "cem"), 0.45, lambda q: (E.formula(c, "não 100", 1340, 560, 92, cor=ERRADO, a=q, align="center")))
        E.foco(c, t, PW("s22", "meia", tm), 0.45, lambda q: E.formula(c, "meia hora = 30 min", W / 2, 700, 84, cor=TINTA2, a=q, align="center"))
        E.foco(c, t, b_, 0.45, lambda q: (E.formula(c, "1 h 30 min", 560, 900, 110, cor=CERTO, a=q, align="center"),
                                           E.selo(c, 900, 860, 44, True, q)))
        E.foco(c, t, c_, 0.45, lambda q: (E.formula(c, "1 h 50 min", 1360, 900, 110, cor=ERRADO, a=q, align="center"),
                                           E.selo(c, 1700, 860, 44, False, q)))
        if t >= c_ + 0.3:
            E.risco(c, 1150, 910, 1570, 830, t, c_ + 0.3, largura=12)

    fase(c, t, t21, t22 - 0.1, s21)
    fase(c, t, t22, 1e9, s22)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s23.a", ps("arrume", "i", 84) + ps("a equação", "g", 80, COR)),
                 (590, "s23.b", ps("faça o mesmo", "i", 84) + ps("nos dois lados", "g", 80, COR)),
                 (780, "s23.c", ps("confira", "i", 84) + ps("substituindo", "g", 80, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), 430, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 530, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a_, b_, c_ = C["s24.a"], C["s24.b"], C["s24.c"]
    E.frase(c, t, C["s24"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, PW("s24", "pronta"), ps("a equação não vem pronta", "i", 76, TINTA2), XE, 350, passo=0.11)
    E.frase(c, t, a_, ps("montar", "g", 130, COR), XE, 500)
    E.frase(c, t, a_ + 0.4, ps("a equação", "g", 130, COR), XE, 640)
    E.frase(c, t, PW("s24", "problema"), ps("a partir de um problema escrito", "i", 70), XE, 760, passo=0.11)
    E.foco(c, t, b_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, b_ + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1650, p), lerp(650, 405, p), ep(t, b_ + 0.2, 0.4), TINTA)
    E.frase(c, t, c_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3,
              questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
