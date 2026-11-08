"""Visual — Estudativo · MAT-RAZ-006: regra de três direta.
Peças locais (as mesmas de MAT-RAZ-007, para a trilha ter uma linguagem só): a tabela da regra de três (coluna com nome em
itálico e fio embaixo, valores grandes, x na cor da matéria, seta ao lado de cada coluna: setas no mesmo sentido = direta),
cruz() é o produto cruzado entre as duas frações das colunas, tipo() é a pílula da relação. desce() é a seta entre duas linhas
com a operação numa pílula (o caminho do valor de um). Instantes: cues C[...] e a palavra falada (PW, de audio/tempos.json)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-006_regra_de_tres_direta.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("montar", "unidade", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 3 * 42 == 7 * 18 == 126 and 126 // 3 == 42 and 18 // 3 == 6 and 7 * 6 == 42
assert 4 * 45 == 6 * 30 == 180 and 30 % 4 != 0
assert 3 * 300 == 50 * 18 == 900 and 300 * 3 == 50 * 18 and 3 * 100 == 300
assert 7 * 20 % 3 != 0
assert 3 * 120 == 8 * 45 == 360 and 45 // 3 == 15 and 8 * 15 == 120

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


# --- tabela da regra de três (mesma linguagem de MAT-RAZ-007) ---
DY3 = 150


def cabeca(c, t, t0, nome, cx, y, size=56, cor=None, larg=300):
    """nome da grandeza, em itálico, com o fio embaixo"""
    E.foco(c, t, t0, 0.5, lambda a: (centro(c, nome, cx, y, size, "i", cor or TINTA2, a),
                                      M.line(c, cx - larg / 2, y + 34, cx + larg / 2, y + 34, FIO, a, 3)))


def coluna(c, t, cx, y, vals, size=110):
    """valores de uma coluna: vals = [(texto, cor, t0), ...], linha i na altura y + DY3*(i+1)"""
    for i, (s, cor, t0) in enumerate(vals):
        fcen(c, t, t0, s, cx, y + DY3 * (i + 1) + size * 0.36, size, cor)


def seta(c, t, t0, x, y, desce=True, cor=None, a=1.0, n=2):
    """seta vertical ao lado da coluna, da 1ª à última linha (desce) ou ao contrário (sobe)"""
    p = ep(t, t0, 0.6) * a
    if p <= 0:
        return
    ya, yb = y + DY3 - 40, y + DY3 * n + 40
    if not desce:
        ya, yb = yb, ya
    M.arrow(c, x, ya, x, yb, cor or COR, p, 7, 26, ease_io(prog(t, t0, 0.6)))


def cruz(c, t, t0, xa, xb, y, cor=None, fundo=None):
    """produto cruzado entre duas frações em xa e xb (barra em y): duas diagonais, com o = limpo no meio"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.line(c, xa + 60, y - 90, xb - 60, y + 110, cor or E.COR, 1.0, 7, progress=p)
    M.line(c, xa + 60, y + 110, xb - 60, y - 90, cor or E.COR, 1.0, 7, progress=p)
    c.drawCircle((xa + xb) / 2, y + 8, 46, M.paint(fundo or E.PAPEL))


def tipo(c, t, t0, s, cx, cy, cor=None, size=48):
    """pílula com o tipo da relação (direta / inversa)"""
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor or E.COR, cor=E.SOBRE, a=a))


def proporcao(c, t, t0, n1, d1, n2, d2, xa, xb, y, size=120, cor=TINTA, tcruz=None):
    """as duas frações das colunas, com o = no meio e a cruz em tcruz"""
    E.foco(c, t, t0, 0.5, lambda a: E.fracao(c, n1, d1, xa, y, size, cor, a))
    E.foco(c, t, t0 + 0.5, 0.5, lambda a: E.fracao(c, n2, d2, xb, y, size, cor, a))
    if tcruz is not None:
        cruz(c, t, tcruz, xa, xb, y)
    E.foco(c, t, t0 + 0.3, 0.5, lambda a: centro(c, "=", (xa + xb) / 2, y + 40, 110, "g", cor, a))


def desce(c, t, t0, x, y0, y1, rot, cor=None):
    """seta entre duas linhas com a operação numa pílula ao lado (o caminho do valor de um)"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    M.arrow(c, x, y0, x, y1, cor or E.COR, p, 6, 22, ease_io(prog(t, t0, 0.5)))
    E.foco(c, t, t0 + 0.15, 0.4, lambda a: E.pilula(c, rot, x + 80, (y0 + y1) / 2, 40, "g", fundo=cor or E.COR, a=a))


def passo_n(c, t, t0, n, txt, y=170):
    """passo do método: número na esfera e o texto ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 46, y - 26, 46, a=a), centro(c, str(n), XE + 46, y - 4, 56, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.1, ps(txt, "i", 72), XE + 120, y, passo=0.1)


XP, XD, YT = 430, 830, 300  # colunas e linha do nome


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        cabeca(c, t, a1, "quilos", XP + 100, 300)
        cabeca(c, t, a1 + 0.2, "reais", XD + 200, 300)
        coluna(c, t, XP + 100, 300, [("3", TINTA, a1 + 0.2), ("7", TINTA, PW("s01", "sete"))], 140)
        coluna(c, t, XD + 200, 300, [("18", TINTA, PW("s01", "dezoito")), ("?", COR, b1 + 0.4)], 140)
        E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "cai muito em prova", 1500, 450, 56, "g", a=a))
        E.foco(c, t, PW("s01", "dois"), 0.5, lambda a: E.pilula(c, "2 caminhos", 1500, 600, 56, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, PW("s02", "qualquer"), ps("qualquer", "i", 84), XE, 480, passo=0.12)
        E.frase(c, t, PW("s02", "regra"), [("regra de três", "g", 104, COR)], XE, 610)
        E.frase(c, t, PW("s02", "direta"), [("direta", "g", 104, COR)], XE, 740)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "achar o x numa proporção", "produto cruzado"), ("s03.c", "grandezas diretas", "a divisão não muda"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 710, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "faltar"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- montar ----------------
def b_montar(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5 = C["s05.a"], C["s05.b"]
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]

    def nome():
        E.frase(c, t, a4, [("regra de três", "g", 120, COR)], W / 2, 300, "center")
        E.frase(c, t, PW("s04", "acha"), ps("acha", "i", 76) + [("1 número", "g", 76, COR)] + ps("a partir de", "i", 76) + [("outros 3", "g", 76, COR)],
                W / 2, 440, "center", 0.12)
        for i, (s, tw) in enumerate((("3", b4), ("18", PW("s04", "dezoito")), ("7", PW("s04", "sete")))):
            E.foco(c, t, tw, 0.45, lambda a, s=s, i=i: (M.rrect(c, 520 + i * 260 - 100, 580, 200, 180, 24, TINTA, a), centro(c, s, 520 + i * 260, 708, 110, "g", BR, a)))
        E.foco(c, t, c4, 0.5, lambda a: (M.rrect(c, 1300 - 100, 580, 200, 180, 24, E.COR, a), centro(c, "x", 1300, 708, 120, "g", BR, a)))
        E.foco(c, t, c4 + 0.3, 0.5, lambda a: centro(c, "o que falta", 1300, 830, 50, "i", COR, a))
    E.saida(c, t, C["s05"] - 0.1, nome)

    def tipo1():
        passo_n(c, t, a5, 1, "confira o tipo")
        tipo(c, t, b5, "diretamente proporcionais", W / 2, 420, size=70)
        E.frase(c, t, PW("s05", "preco", 2), ps("o preço de", "i", 66) + [("1 quilo", "g", 66, COR)] + ps("não muda", "i", 66), W / 2, 620, "center", 0.12)
        E.frase(c, t, PW("s05", "Mais"), ps("mais quilos, mais reais,", "i", 66) + [("na mesma medida", "g", 66, COR)], W / 2, 760, "center", 0.12)
    if t >= C["s05"]:
        E.saida(c, t, C["s06"] - 0.1, tipo1)
    if t < C["s06"]:
        return

    # passo 2: a tabela
    E.saida(c, t, a7 - 0.1, lambda: passo_n(c, t, a6, 2, "monte a tabela"))
    cabeca(c, t, b6, "quilos", XP, YT)
    cabeca(c, t, PW("s06", "reais"), "reais", XD, YT)
    coluna(c, t, XP, YT, [("3", TINTA, c6), ("7", TINTA, d6)])
    coluna(c, t, XD, YT, [("18", TINTA, PW("s06", "dezoito")), ("x", COR, PW("s06", "xis"))])
    E.saida(c, t, a7 - 0.1, lambda: (E.foco(c, t, e6, 0.5, lambda a: E.caixa_pontilhada(c, XD - 150, YT + 70, 300, 330, a, E.COR)),
                                     E.foco(c, t, e6 + 0.3, 0.5, lambda a: centro(c, "o x vai na coluna do que você quer", 960, 920, 54, "i", COR, a))))
    # passo 3: proporção e cruz
    if t >= a7:
        passo_n(c, t, a7, 3, "direta: as colunas formam uma proporção")
        seta(c, t, a7 + 0.5, XP + 130, YT)
        seta(c, t, a7 + 0.5, XD + 130, YT)
        tipo(c, t, a7 + 0.8, "direta", 630, 830)
        xa, xb, y = 1300, 1600, 470
        proporcao(c, t, b7, 3, 7, 18, "x", xa, xb, y, tcruz=c7 - 0.4)
        fcen(c, t, c7, "3x = 7 · 18 = 126", 1450, 730, 84, TINTA)
        fcen(c, t, d7, "x = 126 ÷ 3", 1310, 880, 76, TINTA)
        bola_res(c, t, PW("s07", "quarenta"), "R$ 42", 1720, 860, 110, 62)


# ---------------- o caminho do valor de um ----------------
def b_unidade(c, t, C, b):
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10, d10, e10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]

    def unidade():
        E.frase(c, t, C["s08"] + 0.3, ps("o 2º caminho:", "i", 72) + [("o preço de 1 quilo", "g", 72, COR)], W / 2, 150, "center", 0.12)
        y = YT
        cabeca(c, t, C["s08"] + 0.5, "quilos", XP, y)
        cabeca(c, t, C["s08"] + 0.6, "reais", XD, y)
        rows = ((y + DY3, "3", "18", C["s08"] + 0.6), (y + 2 * DY3, "1", "6", PW("s08", "seis")), (y + 3 * DY3, "7", "42", PW("s08", "quarenta")))
        for yy, q, r, t0 in rows:
            fcen(c, t, t0 if q != "1" else b8, q, XP, yy + 40, 110, TINTA if q != "1" else COR)
            fcen(c, t, t0, r, XD, yy + 40, 110, TINTA if r != "6" else COR)
        desce(c, t, b8, XP + 110, y + DY3 + 10, y + 2 * DY3 - 40, "÷ 3")
        desce(c, t, b8 + 0.2, XD + 120, y + DY3 + 10, y + 2 * DY3 - 40, "÷ 3")
        desce(c, t, c8, XP + 110, y + 2 * DY3 + 10, y + 3 * DY3 - 40, "× 7")
        desce(c, t, c8 + 0.2, XD + 120, y + 2 * DY3 + 10, y + 3 * DY3 - 40, "× 7")

        def contas():
            fcen(c, t, b8, "18 ÷ 3 = 6", 1500, 470, 84, TINTA)
            E.foco(c, t, PW("s08", "reais") + 0.1, 0.5, lambda a: centro(c, "R$ 6 o quilo", 1500, 560, 54, "i", COR, a))
            fcen(c, t, c8 + 0.6, "7 · 6 = 42", 1500, 720, 84, TINTA)
            E.foco(c, t, PW("s08", "mesmo"), 0.5, lambda a: E.pilula(c, "o mesmo resultado", 1500, 820, 46, "g", fundo=CERTO, a=a))
            E.frase(c, t, d8, ps("7 kg > 3 kg:", "i", 58) + [("mais que R$ 18", "g", 58, COR)], W / 2, 1010, "center", 0.12)
        E.saida(c, t, C["s09"] - 0.1, contas)
        if t >= C["s09"]:
            E.frase(c, t, a9, [("6", "g", 64, COR)] + ps("= o número que", "i", 56) + [("não muda", "g", 60, COR)], 1450, 470, "center", 0.1)
            E.frase(c, t, b9, ps("preço ÷ quilos", "g", 70, TINTA), 1450, 600, "center", 0.12)
            E.foco(c, t, PW("s09", "feijao"), 0.5, lambda a: centro(c, "(o quilo do feijão da aula das grandezas)", 1450, 680, 40, "i", TINTA2, a))
            E.frase(c, t, PW("s09", "Quando"), ps("divisão exata:", "i", 62), 1450, 830, "center", 0.1)
            E.frase(c, t, c9, ps("o mais rápido", "g", 66, COR) + ps("de cabeça", "i", 62), 1450, 930, "center", 0.1)
    E.saida(c, t, C["s10"] - 0.1, unidade)

    if t >= C["s10"]:
        E.frase(c, t, C["s10"] + 0.3, ps("nem sempre o valor de 1", "i", 70) + [("sai inteiro", "g", 70, ERRADO)], W / 2, 150, "center", 0.12)
        cabeca(c, t, a10, "metros", XP, YT)
        cabeca(c, t, a10 + 0.2, "reais", XD, YT)
        coluna(c, t, XP, YT, [("4", TINTA, a10 + 0.3), ("6", TINTA, PW("s10", "seis"))])
        coluna(c, t, XD, YT, [("30", TINTA, PW("s10", "trinta")), ("x", COR, b10 + 0.6)])
        E.saida(c, t, c10 - 0.2, lambda: E.foco(c, t, PW("s10", "Trinta", 2), 0.5, lambda a: E.pilula(c, "30 ÷ 4: não é exato", 1450, 470, 54, "g", fundo=ERRADO, a=a)))
        seta(c, t, c10 - 0.6, XP + 130, YT)
        seta(c, t, c10 - 0.6, XD + 130, YT)
        xa, xb, y = 1300, 1600, 470
        if t >= c10 - 0.2:
            proporcao(c, t, c10 - 0.2, 4, 6, 30, "x", xa, xb, y, tcruz=c10)
        fcen(c, t, c10 + 0.6, "4x = 6 · 30 = 180", 1450, 730, 84, TINTA)
        bola_res(c, t, d10, "R$ 45", 1450, 880, 110, 66)
        E.foco(c, t, e10, 0.5, lambda a: (E.pilula(c, "mais metros, mais reais", 630, 900, 50, "g", a=a), E.selo(c, 960, 900, 40, True, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    E.frase(c, t, C["s11"] + 0.3, ps("o erro:", "i", 70) + [("unidades diferentes", "g", 70, ERRADO)] + ps("na mesma coluna", "i", 70), W / 2, 150, "center", 0.1)
    cabeca(c, t, b11, "tecido", XP, YT)
    cabeca(c, t, b11 + 0.2, "reais", XD, YT)
    # 3 m vira 300 cm
    y0 = YT + DY3 + 40
    E.saida(c, t, c12 + 0.3, lambda: fcen(c, t, b11 + 0.3, "3 m", XP, y0, 100, TINTA))
    fcen(c, t, c12 + 0.4, "300 cm", XP, y0, 90, CERTO)
    fcen(c, t, c11, "50 cm", XP, YT + 2 * DY3 + 40, 90, TINTA)
    coluna(c, t, XD, YT, [("18", TINTA, PW("s11", "dezoito")), ("x", COR, c11 + 0.4)])
    # caixa da coluna: vermelha com 3 e 50, verde com 300 e 50
    E.saida(c, t, d12 - 0.1, lambda: E.foco(c, t, a12, 0.5, lambda a: E.caixa_pontilhada(c, XP - 170, YT + 70, 340, 330, a, ERRADO)))
    E.foco(c, t, d12, 0.5, lambda a: E.caixa_pontilhada(c, XP - 170, YT + 70, 340, 330, a, CERTO))

    def errado():
        E.foco(c, t, b12, 0.5, lambda a: E.pilula(c, "R$ 300", 1450, 470, 80, "g", fundo=ERRADO, a=a))
        if t >= b12 + 0.6:
            E.risco(c, 1300, 510, 1600, 430, t, PW("s12", "Mais"), BR, 10)
        E.frase(c, t, PW("s12", "Mais"), ps("mais caro que", "i", 58) + [("3 m inteiros!", "g", 58, ERRADO)], 1450, 600, "center", 0.1)
    E.saida(c, t, d12 - 0.1, errado)
    E.foco(c, t, c12, 0.5, lambda a: E.pilula(c, "escada do metro: 3 m = 300 cm", 960, 900, 48, "g", fundo=TINTA, a=a * (1 - ep(t, e12, 0.4))))
    bola_res(c, t, e12, "R$ 3", 1450, 520, 120, 72, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]

    def divide():
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho:", "i", 76, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, a13, ps("divida", "g", 100, BR) + ps("antes de multiplicar", "i", 96, CLARO), W / 2, 310, "center", 0.12)
        fcen(c, t, b13, "3x = 7 · 18", W / 2, 500, 110, BR)
        tn = PW("s13", "Nao")
        E.saida(c, t, c13 - 0.1, lambda: (E.foco(c, t, tn, 0.5, lambda a: E.pilula(c, "126", 1450, 465, 60, "g", fundo=CINZA, a=a)),
                                          E.risco(c, 1360, 500, 1540, 430, t, tn + 0.4, ERRADO, 10) if t >= tn + 0.4 else None))
        fcen(c, t, c13, "x = 7 · (18 ÷ 3)", W / 2, 690, 100, CLARO)
        E.foco(c, t, PW("s13", "seis", 2), 0.5, lambda a: E.pilula(c, "18 ÷ 3 = 6", 1500, 655, 50, "g", fundo=CLARO, cor="#07070F", a=a))
        fcen(c, t, d13, "x = 7 · 6", 760, 880, 100, BR)
        E.foco(c, t, PW("s13", "quarenta"), 0.5, lambda a: (E.bola(c, 1250, 850, 100, a=a), E.formula(c, "42", 1250, 880, 84, "g", BR, a, "center")))
    E.saida(c, t, C["s14"] - 0.1, divide)

    if t >= C["s14"]:
        a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
        E.frase(c, t, a14, ps("× e ÷: a ordem", "i", 72, CLARO) + ps("não muda o resultado", "g", 72, BR), W / 2, 260, "center", 0.12)
        E.frase(c, t, b14, ps("dividir primeiro deixa os", "i", 66, CLARO) + ps("números pequenos", "g", 66, BR), W / 2, 380, "center", 0.12)
        E.frase(c, t, c14, ps("não compensa se", "i", 66, CLARO) + ps("nenhuma divisão é exata", "g", 66, BR), W / 2, 580, "center", 0.12)
        E.foco(c, t, PW("s14", "sete"), 0.5, lambda a: E.pilula(c, "7 · 20 ÷ 3", W / 2, 680, 56, "g", fundo=ERRADO, cor=BR, a=a))
        E.frase(c, t, d14, ps("aí,", "i", 80, CLARO) + ps("multiplique primeiro", "g", 80, BR), W / 2, 860, "center", 0.12)
        E.frase(c, t, PW("s14", "divida"), ps("e divida no fim", "i", 70, CLARO), W / 2, 960, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a15, b15 = C["s15.a"], C["s15.b"]
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, PW("s15", "Uma"), ps("uma impressora", "i", 70), XE, 320, passo=0.12)
    cabeca(c, t, a15, "minutos", XP, 440)
    cabeca(c, t, a15 + 0.2, "páginas", XD, 440)
    coluna(c, t, XP, 440, [("3", TINTA, PW("s15", "tres")), ("8", TINTA, PW("s15", "oito"))])
    coluna(c, t, XD, 440, [("45", TINTA, a15), ("?", CINZA, b15)])
    E.frase(c, t, PW("s15", "mesmo"), ps("no mesmo", "i", 64) + [("ritmo", "g", 64, COR)], XE, 1000, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1450, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17, d17, e17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"], C["s17.e"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, PW("s17", "Mais"), ps("mais minutos, mais páginas:", "i", 64), XE, 170, passo=0.1)
    tipo(c, t, a17, "direta", 1100, 150, size=52)
    cabeca(c, t, b17 - 0.4, "minutos", XP, YT)
    cabeca(c, t, b17 - 0.2, "páginas", XD, YT)
    coluna(c, t, XP, YT, [("3", TINTA, b17), ("8", TINTA, c17)])
    coluna(c, t, XD, YT, [("45", TINTA, PW("s17", "quarenta")), ("x", COR, PW("s17", "xis"))])
    seta(c, t, c17 + 0.6, XP + 130, YT)
    seta(c, t, c17 + 0.6, XD + 130, YT)
    xa, xb, y = 1300, 1600, 470

    def cruzada():
        if t >= d17 - 0.6:
            proporcao(c, t, d17 - 0.6, 3, 8, 45, "x", xa, xb, y, tcruz=d17)
        fcen(c, t, d17 + 0.6, "3x = 8 · 45 = 360", 1450, 730, 80, TINTA)
        fcen(c, t, e17, "x = 360 ÷ 3", 1320, 880, 76, TINTA)
    E.saida(c, t, C["s18"] - 0.1, cruzada)
    bola_res(c, t, PW("s17", "cento"), "120", 1690, 860, 100, 76, CERTO)
    if t >= C["s18"]:
        E.frase(c, t, C["s18"] + 0.3, ps("com o atalho:", "i", 66, COR), 1400, 400, "center")
        fcen(c, t, a18, "45 ÷ 3 = 15", 1400, 530, 90, TINTA)
        fcen(c, t, b18, "8 · 15 = 120", 1400, 680, 90, TINTA)
        E.foco(c, t, c18, 0.5, lambda a: E.pilula(c, "15 páginas por minuto", 760, 990, 54, "g", a=a))
        E.foco(c, t, PW("s18", "unidade"), 0.5, lambda a: E.escreve(c, "= o caminho do valor de 1", 1100, 1008, 46, "i", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", "confira se é direta"), ("s19.b", "tabela com unidades iguais"), ("s19.c", "cruz ou valor de 1"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, a20, [("regra de três", "g", 130, COR)], XE, 460)
    E.frase(c, t, a20 + 0.4, [("inversa", "g", 130, COR)], XE, 600)
    E.frase(c, t, b20, ps("4 pintores: 9 dias;", "i", 64) + [("6 pintores?", "g", 64, COR)], XE, 730, passo=0.12)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, montar=b_montar, unidade=b_unidade, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
