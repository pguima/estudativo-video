"""Visual — Estudativo · MAT-RAZ-004: grandezas direta e inversamente proporcionais.
Peças locais: a tabela de duas grandezas na linguagem da trilha (cabeca: nome em itálico com fio embaixo; valores grandes;
seta ao lado de cada coluna: setas no mesmo sentido = direta, em sentidos opostos = inversa, como em MAT-RAZ-007) e a terceira
coluna com a conta de cada linha (a divisão na direta, a multiplicação na inversa), com o resultado na cor da matéria e a caixa
pontilhada em volta quando ele se repete. Instantes: cues C[...] e a palavra falada (PW, lida de audio/tempos.json)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-004_grandezas_direta_inversa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("direta", "inversa", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert [p // q for q, p in ((1, 8), (2, 16), (3, 24), (5, 40))] == [8] * 4 and 4 * 8 == 32
assert [v * h for v, h in ((30, 4), (40, 3), (60, 2), (120, 1))] == [120] * 4 and 60 * 2 == 120
assert 90 / 2 == 45 and 100 / 4 == 25
assert [n * h for n, h in ((1, 12), (2, 6), (3, 4), (4, 3))] == [12] * 4 and 12 // 6 == 2

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


# --- tabela (mesma linguagem de MAT-RAZ-007) ---
Y0, DY = 250, 118  # linha do nome e distância entre as linhas


def ylin(i):
    return Y0 + DY * (i + 1)


def cabeca(c, t, t0, nome, cx, y=Y0, size=52, cor=None, larg=300):
    """nome da grandeza, em itálico, com o fio embaixo"""
    E.foco(c, t, t0, 0.5, lambda a: (centro(c, nome, cx, y, size, "i", cor or TINTA2, a),
                                      M.line(c, cx - larg / 2, y + 30, cx + larg / 2, y + 30, FIO, a, 3)))


def valor(c, t, t0, s, cx, i, size=84, cor=TINTA):
    E.formula_em(c, t, t0, s, cx, ylin(i) + size * 0.36, size, "g", cor, "center")


def conta(c, t, t0, esq, res, cx, i, size=70, cor_res=None, tr=None):
    """a conta da linha: 'esq' em preto e o resultado na cor da matéria (tr = instante do resultado)"""
    y = ylin(i) + size * 0.36
    w1 = E.formula(c, esq, 0, 0, size, a=0)
    w2 = E.formula(c, " " + res, 0, 0, size, a=0)
    x0 = cx - (w1 + w2) / 2
    E.formula_em(c, t, t0, esq, x0, y, size, "g", TINTA)
    E.formula_em(c, t, tr if tr is not None else t0 + 0.3, " " + res, x0 + w1, y, size, "g", cor_res or COR)
    wr = E.formula(c, res, 0, 0, size, a=0)
    return x0 + w1 + w2 - wr / 2  # centro do resultado


def seta(c, t, t0, x, i0, i1, desce=True, cor=None, a=1.0):
    """seta vertical ao lado da coluna, da linha i0 à i1 (desce) ou ao contrário (sobe)"""
    p = ep(t, t0, 0.6) * a
    if p <= 0:
        return
    ya, yb = ylin(i0) - 40, ylin(i1) + 40
    if not desce:
        ya, yb = yb, ya
    M.arrow(c, x, ya, x, yb, cor or E.COR, p, 7, 26, ease_io(prog(t, t0, 0.6)))


def tipo(c, t, t0, s, cx, cy, cor=None, size=50, escuro=False):
    """pílula com o tipo da relação (direta / inversa)"""
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor or E.COR, cor=E.SOBRE, a=a))


def caixa_col(c, t, t0, cx, i0, i1, w=170, cor=None):
    """caixa pontilhada em volta dos resultados repetidos (linhas i0..i1)"""
    p = ep(t, t0, 0.5)
    E.caixa_pontilhada(c, cx + 8 - w / 2, ylin(i0) - 62, w, ylin(i1) - ylin(i0) + 124, p, cor or E.COR, prog_=p)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        for cx, w1, w2, t1, t2, sobe2, rot, tr in ((560, "quilos", "preço", C["s01"], a1, True, "anda junto", PW("s01", "junto")),
                                                  (1360, "velocidade", "tempo", PW("s01", "velocidade"), b1, False, "ao contrário", PW("s01", "contrario"))):
            E.foco(c, t, t1, 0.5, lambda a, cx=cx, w1=w1: E.escreve(c, w1, cx - 300, 360, 84, "g", TINTA, a))
            E.foco(c, t, t2, 0.5, lambda a, cx=cx, w2=w2: E.escreve(c, w2, cx - 300, 520, 84, "g", TINTA, a))
            p1 = ep(t, t1 + 0.3, 0.5)
            M.arrow(c, cx + 220, 380, cx + 220, 280, E.COR, p1, 9, 30, p1)
            p2 = ep(t, t2 + 0.2, 0.5)
            if sobe2:
                M.arrow(c, cx + 220, 540, cx + 220, 440, E.COR, p2, 9, 30, p2)
            else:
                M.arrow(c, cx + 220, 440, cx + 220, 540, TINTA, p2, 9, 30, p2)
            E.foco(c, t, tr, 0.5, lambda a, cx=cx, rot=rot: E.pilula(c, rot, cx - 80, 690, 56, "g", fundo=E.COR if rot == "anda junto" else TINTA, a=a))
        E.frase(c, t, c1, ps("uma", "i", 76) + [("conta simples", "g", 76, COR)] + ps("na tabela mostra", "i", 76), W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, PW("s02", "reconhece"), ps("reconhecer", "i", 84) + [("numa tabela", "g", 84, COR)], XE, 490, passo=0.12)
        E.frase(c, t, PW("s02", "grandezas"), ps("se são", "i", 84) + [("proporcionais", "g", 84, COR)], XE, 640, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, w, y = 960, 800, 400
    k = "s03.b"
    p = ep(t, C[k], 0.5)
    E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
    E.frase(c, t, C[k] + 0.1, [("razão", "i", 60)], x + 44, y + 84)
    E.frase(c, t, PW("s03", "comparar"), [("comparar pela divisão", "g", 60, COR)], x + 44, y + 160)
    E.cursor(c, x + w - 30, y + 170, ep(t, C[k], 0.4))
    E.frase(c, t, PW("s03", "faltar"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- grandeza ----------------
def b_grandeza(c, t, C, b):
    a4 = C["s04.a"]
    E.frase(c, t, C["s04"] + 0.3, ps("primeiro, uma palavra", "i", 76, TINTA2), W / 2, 220, "center", 0.12)
    E.frase(c, t, a4, [("grandeza", "g", 130, COR)], W / 2, 420, "center")
    E.frase(c, t, PW("s04", "tudo"), ps("tudo que dá para", "i", 76) + [("medir", "g", 76, COR)] + ps("ou", "i", 76) + [("contar", "g", 76, COR)],
            W / 2, 560, "center", 0.12)
    for i, (k, s) in enumerate((("s04.b", "preço"), ("s04.c", "peso"), ("s04.d", "tempo"), ("s04.e", "velocidade"))):
        cx = 420 + i * 360
        E.foco(c, t, C[k], 0.45, lambda a, s=s, cx=cx: E.pilula(c, s, cx, 780, 60, "g", fundo=TINTA if s != "velocidade" else E.COR, a=a))


# ---------------- direta ----------------
XQ, XP, XR = 380, 760, 1340  # colunas: 1ª grandeza, 2ª grandeza, conta


def b_direta(c, t, C, b):
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    E.saida(c, t, a7 - 0.1, lambda: E.frase(c, t, C["s05"] + 0.2, ps("veja esta", "i", 72) + [("tabela", "g", 72, COR)], W / 2, 140, "center", 0.12))
    cabeca(c, t, a5 - 0.3, "quilos", XQ)
    cabeca(c, t, a5 - 0.1, "preço (R$)", XP)
    linhas = (("1", "8", a5, PW("s05", "oito")), ("2", "16", b5, PW("s05", "dezesseis")), ("3", "24", c5, PW("s05", "vinte")), ("5", "40", d5, PW("s05", "quarenta")))
    for i, (q, p, tq, tp) in enumerate(linhas):
        valor(c, t, tq, q, XQ, i)
        valor(c, t, tp, p, XP, i)
    # a conta de cada linha
    cabeca(c, t, a6, "preço ÷ quilos", XR, larg=420)
    contas = (("8 ÷ 1 =", a6 + 0.6), ("16 ÷ 2 =", b6), ("24 ÷ 3 =", c6), ("40 ÷ 5 =", d6))
    xr = XR
    for i, (s, t0) in enumerate(contas):
        tr = t0 + 0.6 if i == 0 else PW("s06", "oito", i)
        xr = conta(c, t, t0, s, "8", XR, i, tr=tr)
    caixa_col(c, t, e6, xr, 0, 3, 72)
    # s07: nome, significado, constante, 4ª linha
    tipo(c, t, a7, "diretamente proporcionais", W / 2, 140, size=54)
    seta(c, t, a7 + 0.4, XQ + 130, 0, 3, True, TINTA)
    seta(c, t, a7 + 0.4, XP + 150, 0, 3, True, TINTA)
    E.saida(c, t, c7 - 0.1, lambda: E.frase(c, t, b7, [("8", "g", 70, COR)] + ps("= o preço de", "i", 66) + [("1 quilo", "g", 70, COR)], W / 2, 990, "center", 0.12))
    E.frase(c, t, c7, ps("nos livros:", "i", 62, TINTA2) + [("constante de proporcionalidade", "g", 62, COR)], W / 2, 990, "center", 0.1)
    valor(c, t, PW("s07", "quatro"), "4", XQ, 4, cor=CERTO)
    conta(c, t, PW("s07", "quatro", 2), "4 · 8 =", "32", XR, 4, cor_res=CERTO, tr=PW("s07", "trinta"))
    valor(c, t, PW("s07", "trinta"), "32", XP, 4, cor=CERTO)


# ---------------- inversa ----------------
def b_inversa(c, t, C, b):
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]

    def intro():
        E.frase(c, t, C["s08"] + 0.4, ps("uma viagem de", "i", 84) + [("120 km", "g", 96, COR)], W / 2, 330, "center", 0.12)
        E.frase(c, t, a8, [("km/h", "g", 110, COR)], W / 2, 560, "center")
        E.frase(c, t, PW("s08", "quantos"), ps("quantos km o carro anda", "i", 76) + [("em 1 hora", "g", 76, COR)], W / 2, 720, "center", 0.12)
        # a estrada
        p = ep(t, C["s08"] + 0.6, 1.0)
        M.line(c, 360, 880, lerp(360, 1560, p), 880, TINTA2, 1, 6)
        for k in range(13):
            if 360 + k * 100 <= lerp(360, 1560, p):
                M.line(c, 360 + k * 100, 868, 360 + k * 100, 892, TINTA2, 1, 4)
    E.saida(c, t, C["s09"] - 0.1, intro)
    if t < C["s09"]:
        return
    cabeca(c, t, C["s09"] + 0.2, "velocidade (km/h)", XQ, larg=360)
    cabeca(c, t, C["s09"] + 0.4, "tempo (h)", XP)
    linhas = (("30", "4", a9, PW("s09", "quatro")), ("40", "3", b9, PW("s09", "tres")), ("60", "2", c9, PW("s09", "duas")))
    for i, (v, h, tv, th) in enumerate(linhas):
        valor(c, t, tv, v, XQ, i)
        valor(c, t, th, h, XP, i)
    E.saida(c, t, a10 - 0.1, lambda: E.foco(c, t, PW("s09", "dividir"), 0.5, lambda a: E.pilula(c, "÷ não dá sempre igual", XR, ylin(1), 50, "g", fundo=ERRADO, a=a)))
    E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "multiplique", W / 2, 140, 60, "g", a=a * (1 - ep(t, a11 - 0.2, 0.3))))
    cabeca(c, t, a10 - 0.2, "velocidade · tempo", XR, larg=440)
    xr = XR
    for i, (s, t0) in enumerate((("30 · 4 =", a10), ("40 · 3 =", b10), ("60 · 2 =", c10))):
        xr = conta(c, t, t0, s, "120", XR, i, tr=PW("s10", "cento", i + 1))
    caixa_col(c, t, d10, xr, 0, 2, 150)
    E.saida(c, t, a11 - 0.1, lambda: E.frase(c, t, d10, ps("velocidade · tempo", "g", 66, COR) + ps("não muda", "i", 66), W / 2, 990, "center", 0.12))
    # s11: nome, setas em sentidos opostos, significado, 4ª linha
    tipo(c, t, a11, "inversamente proporcionais", W / 2, 140, size=54)
    seta(c, t, a11 + 0.4, XQ + 150, 0, 2, True, TINTA)
    seta(c, t, a11 + 0.4, XP + 150, 0, 2, False, TINTA)
    E.saida(c, t, b11 - 0.1, lambda: E.frase(c, t, PW("s11", "sessenta"), [("60 km", "g", 64, COR)] + ps("por hora ·", "i", 62) + [("2 horas", "g", 64, COR)] + ps("=", "i", 62) + [("120 km", "g", 64, COR)],
                                               W / 2, 990, "center", 0.1))
    E.frase(c, t, b11, ps("velocidade · tempo =", "i", 66) + [("distância", "g", 70, COR)], W / 2, 990, "center", 0.12)
    valor(c, t, c11, "120", XQ, 3, cor=CERTO)
    valor(c, t, d11, "1", XP, 3, cor=CERTO)
    conta(c, t, PW("s11", "porque"), "120 · 1 =", "120", XR, 3, cor_res=CERTO, tr=PW("s11", "cento", 5))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    E.frase(c, t, C["s12"] + 0.3, ps("o erro:", "i", 76) + [("subiu junto, é direta?", "g", 76, ERRADO)], W / 2, 140, "center", 0.12)
    cabeca(c, t, b12 - 0.3, "idade (anos)", XQ)
    cabeca(c, t, b12 - 0.1, "altura (cm)", XP)
    valor(c, t, PW("s12", "dois"), "2", XQ, 0)
    valor(c, t, b12, "90", XP, 0)
    valor(c, t, PW("s12", "quatro"), "4", XQ, 1)
    valor(c, t, c12, "100", XP, 1)
    seta(c, t, PW("s12", "idade"), XQ + 130, 0, 1, True, TINTA)
    seta(c, t, PW("s12", "altura"), XP + 150, 0, 1, True, TINTA)
    cabeca(c, t, a13 - 0.3, "altura ÷ idade", XR, larg=420)
    conta(c, t, a13, "90 ÷ 2 =", "45", XR, 0, tr=PW("s13", "quarenta"))
    conta(c, t, b13, "100 ÷ 4 =", "25", XR, 1, cor_res=ERRADO, tr=PW("s13", "vinte"))
    E.foco(c, t, c13, 0.5, lambda a: E.pilula(c, "não é proporcional", XR, ylin(2) + 30, 56, "g", fundo=ERRADO, a=a))
    E.foco(c, t, d13, 0.5, lambda a: E.pilula(c, "quem decide é a conta", W / 2, ylin(3) + 60, 60, "g", a=a))
    E.frase(c, t, e13, ps("um sobe, o outro desce:", "i", 60) + ps("pode não ser inversa", "g", 60, ERRADO), W / 2, 990, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]

    def dd():
        E.frase(c, t, C["s14"] + 0.3, ps("o atalho:", "i", 80, CLARO), W / 2, 180, "center", 0.12)
        s, y = 130, 450

        def palavra(w, x, a, destaca):
            E.escreve(c, w[0], x, y, s, "g", BR, a)
            E.escreve(c, w[1:], x + E.larg(w[0], "g", s) + E.APERTO["g"] * s, y, s, "g", CLARO if destaca else BR, a)
            return x + E.larg(w, "g", s)
        x1 = 260
        E.foco(c, t, a14, 0.5, lambda a: palavra("direta", x1, a, True))
        E.foco(c, t, a14 + 0.3, 0.5, lambda a: centro(c, "→", 960, y - 10, 110, "g", CLARO, a))
        x2 = 1100
        E.foco(c, t, PW("s14", "divisao"), 0.5, lambda a: palavra("divisão", x2, a, True))
        for x in (x1, x2):
            q = ep(t, b14, 0.5)
            if q > 0:
                cx = x + E.larg("d", "g", s) / 2
                c.drawCircle(cx, y - s * 0.36, s * 0.52, M.paint(CLARO, q, stroke=7))
        E.foco(c, t, b14, 0.5, lambda a: centro(c, "as duas começam com d", W / 2, 620, 60, "i", CLARO, a))
        s2, y2 = 110, 840
        E.foco(c, t, c14, 0.5, lambda a: E.escreve(c, "inversa", 260, y2, s2, "g", BR, a))
        E.foco(c, t, c14 + 0.3, 0.5, lambda a: centro(c, "→", 900, y2 - 10, 100, "g", CLARO, a))
        E.foco(c, t, PW("s14", "multiplicacao"), 0.5, lambda a: E.escreve(c, "multiplicação", 1000, y2, s2, "g", BR, a))
    E.saida(c, t, C["s15"] - 0.1, dd)

    if t >= C["s15"]:
        a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, a15, ps("direta: crescem na", "i", 64, CLARO) + ps("mesma medida", "g", 64, BR), W / 2, 220, "center", 0.1)
        E.frase(c, t, PW("s15", "divisao"), ps("a", "i", 64, CLARO) + ps("divisão", "g", 64, BR) + ps("fica parada", "i", 64, CLARO), W / 2, 310, "center", 0.1)
        E.frase(c, t, b15, ps("inversa: uma cresce,", "i", 64, CLARO) + ps("a outra encolhe", "g", 64, BR), W / 2, 450, "center", 0.1)
        E.frase(c, t, PW("s15", "produto"), ps("o", "i", 64, CLARO) + ps("produto", "g", 64, BR) + ps("fica parado", "i", 64, CLARO), W / 2, 540, "center", 0.1)
        E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "o macete diz qual conta fazer", W / 2, 690, 50, "g", a=a))
        E.frase(c, t, d15, ps("confira", "i", 70, CLARO) + ps("todas as linhas", "g", 70, BR), W / 2, 830, "center", 0.12)
        E.frase(c, t, PW("s15", "nem"), ps("nem ÷ nem · se repetem:", "i", 56, CLARO) + ps("nenhuma das duas", "g", 56, BR), W / 2, 950, "center", 0.1)


# ---------------- questão ----------------
XT, XH = 330, 640  # torneiras, horas


def tabela_torneiras(c, t, ts):
    cabeca(c, t, ts[0] - 0.4, "torneiras", XT, larg=260)
    cabeca(c, t, ts[0] - 0.2, "horas", XH, larg=240)
    for i, (n, h) in enumerate(((1, 12), (2, 6), (3, 4), (4, 3))):
        valor(c, t, ts[i], str(n), XT, i)
        valor(c, t, ts[i] + 0.4, str(h), XH, i)


def b_questao(c, t, C, b):
    a16, b16, c16, d16, e16, f16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"], C["s16.f"]
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 64, COR), XE, 140)
    tabela_torneiras(c, t, (a16, b16, c16, d16))
    E.frase(c, t, e16, [("direta", "g", 64, COR)] + ps("ou", "i", 64) + [("inversa?", "g", 64, COR)], XE, 880, passo=0.12)
    E.frase(c, t, f16, ps("qual número", "i", 64) + [("não muda?", "g", 64, COR)], XE, 980, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1450, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18, d18, e18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    t0 = C["s18"] + 0.2
    tabela_torneiras(c, t, (t0, t0 + 0.15, t0 + 0.3, t0 + 0.45))
    xr0 = 1200

    tp = PW("s18", "Pista")
    E.saida(c, t, tp - 0.1, lambda: E.foco(c, t, PW("s18", "Mais"), 0.5, lambda a: E.pilula(c, "mais torneiras, menos tempo: pista de inversa", 1150, 140, 42, "g", fundo=TINTA, a=a)))
    E.saida(c, t, a19 - 0.1, lambda: E.foco(c, t, tp, 0.5, lambda a: E.pilula(c, "pista, não prova: quem decide é a conta", 1150, 140, 42, "g", fundo=TINTA, a=a)))
    cabeca(c, t, a18, "torneiras · horas", xr0, larg=420)
    xr = xr0
    for i, t1 in enumerate((b18, c18, d18, e18)):
        n, h = ((1, 12), (2, 6), (3, 4), (4, 3))[i]
        xr = conta(c, t, t1, f"{n} · {h} =", "12", xr0, i, tr=PW("s18", "doze", i + 2))
    caixa_col(c, t, a19 + 0.3, xr, 0, 3, 100)
    tipo(c, t, a19, "inversamente proporcionais", 1300, 140, size=46)
    E.frase(c, t, b19, [("12", "g", 60, COR)] + ps("= o tempo de", "i", 58) + [("1 torneira sozinha", "g", 60, COR)], W / 2, 1000, "center", 0.1)
    # 6 torneiras: 12 ÷ 6 = 2, na linha nova da tabela
    valor(c, t, c19, "6", XT, 4, cor=CERTO)
    conta(c, t, PW("s19", "doze", 2), "12 ÷ 6 =", "2", xr0, 4, cor_res=CERTO, tr=PW("s19", "duas"))
    valor(c, t, PW("s19", "duas"), "2", XH, 4, cor=CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s20.a", "divisão sempre igual: direta"), ("s20.b", "produto sempre igual: inversa"))
        for i, (k, s) in enumerate(itens):
            y = 470 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 400, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a21, b21, c21, d21 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, a21, ps("o teste do", "i", 110) + [("dobro", "g", 130, COR)], XE, 470, passo=0.15)
    E.frase(c, t, b21, ps("por que o", "i", 70) + [("táxi", "g", 70, COR)] + ps("não é proporcional", "i", 70), XE, 630, passo=0.12)
    E.foco(c, t, c21, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, c21 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, c21 + 0.2, 0.4))
    E.frase(c, t, d21, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, grandeza=b_grandeza, direta=b_direta, inversa=b_inversa, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
