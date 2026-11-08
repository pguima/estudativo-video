"""Visual — Estudativo · MAT-EQU-018: sistema de equações, método da substituição.
Teste: x + y = 5 e 2x + y = 7 → (2, 3) serve, (1, 4) não. Problema: x + y = 30 e 4x + 2y = 100 → 20 carros e 10 motos.
Erro: 2(30 − x) virar 60 − x → 3x = 40. Questão: x + y = 12 e 3x + y = 20 → x = 4, y = 8.
Instantes: cues C[...] e, para números ditos no meio da frase, pal(cena, palavra) lê o instante da palavra na voz real."""
import json
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, passo, palco, centro
import motor as M
import skia

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-018_sistema_substituicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sistema", "problema", "metodo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula
assert 2 + 3 == 5 and 2 * 2 + 3 == 7 and 1 + 4 == 5 and 2 * 1 + 4 == 6 != 7
x, y = 20, 10
assert x + y == 30 and 4 * x + 2 * y == 100 and 4 * x + 2 * (30 - x) == 100 and 2 * 30 == 60 and (100 - 60) / 2 == 20
assert 4 * 20 == 80 and 2 * 10 == 20 and 100 - 60 == 40 and 40 % 3 != 0
assert 4 + 8 == 12 and 3 * 4 + 8 == 20 and (20 - 12) / 2 == 4 and 12 - 4 == 8


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


def relacao(c, a, esq, sig, dir_, y, size, cor=None, xm=W / 2):
    g = size * 0.5
    E.formula(c, esq, xm - g, y, size, "g", cor, a, "right")
    centro(c, sig, xm, y, size, "g", cor, a)
    E.formula(c, dir_, xm + g, y, size, "g", cor, a)


def pilha(c, t, linhas, ops, xm, y0, dy, size):
    """resolução em linhas alinhadas pelo igual: linhas = [(t0, esq, dir)], ops = {k: (t0, op)} escrita sob os dois lados da linha k.
    A linha antiga fica cinza quando a nova chega; a última fica na cor da matéria."""
    g = size * 0.5
    for k, (t0, esq, dir_) in enumerate(linhas):
        y = y0 + k * dy
        ult = k == len(linhas) - 1
        velha = not ult and t >= linhas[k + 1][0]
        cor = COR if ult else (CINZA if velha else TINTA)
        E.foco(c, t, t0, 0.5, lambda a, esq=esq, dir_=dir_, y=y, cor=cor: relacao(c, a, esq, "=", dir_, y, size, cor, xm))
        if k in ops:
            to, op = ops[k]
            we = E.formula(c, esq, 0, 0, size, a=0)
            wd = E.formula(c, dir_, 0, 0, size, a=0)
            cop = CINZA if velha else COR
            for cx in (xm - g - we / 2, xm + g + wd / 2):
                E.foco(c, t, to, 0.45, lambda a, cx=cx, cop=cop: E.formula(c, op, cx, y + size * 0.72, size * 0.52, "b", cop, a, "center"), sobe=8)


def selo_em(c, t, t0, cx, cy, r, ok):
    E.foco(c, t, t0, 0.5, lambda a: E.selo(c, cx, cy, r, ok, a))


def bnum(c, t, t0, s, cx, cy, r, cor=None, size=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + (size or r) * 0.36, size or r, "g", E.SOBRE, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]

    def muitas():
        fcen(c, t, ka, "x + y = 5", W / 2, 250, 150, COR)
        E.frase(c, t, pal("s01", "são"), ps("duas letras, cada uma no lugar de", "i", 64, TINTA2) + [("um número", "g", 66, TINTA2)], W / 2, 380, "center", 0.09)
        E.frase(c, t, pal("s01", "quanto"), ps("quanto vale", "i", 80) + [("x?", "g", 84, COR)], W / 2, 500, "center", 0.12)
        pares = ((kb, "x = 1, y = 4", 500, 650, TINTA), (kc, "x = 2, y = 3", 1420, 650, TINTA),
                 (kd, "x = 3, y = 2", 500, 780, CINZA), (kd + 0.15, "x = 0, y = 5", 960, 780, CINZA), (kd + 0.3, "x = 4, y = 1", 1420, 780, CINZA),
                 (kd + 0.45, "x = 5, y = 0", 960, 650, CINZA))
        for k, s, cx, cy, cor in pares:
            fcen(c, t, k, s, cx, cy, 72, cor)

        def sobra():
            E.frase(c, t, pal("s01", "com"), ps("com uma equação só,", "i", 72) + [("sobra resposta demais", "g", 76, ERRADO)], W / 2, 950, "center", 0.1)
        if t < a2 + 0.4:
            E.saida(c, t, a2 - 0.1, sobra)
        E.frase(c, t, a2 + 0.1, ps("chega", "i", 72) + [("uma segunda informação:", "g", 72)] + ps("a resposta vira", "i", 72) + [("uma só", "g", 76, CERTO)], W / 2, 950, "center", 0.1)
    E.saida(c, t, b2 - 0.1, muitas)
    if t < b2:
        return
    E.foco(c, t, c2 - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 220 * ease_back(prog(t, c2 - 0.2, 0.7))), blur=0)
    E.frase(c, t, b2, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, pal("s02", "resolve"), ps("resolver", "i", 90) + [("duas equações", "g", 96, COR)], XE, 450, passo=0.14)
    E.frase(c, t, pal("s02", "juntas"), [("juntas", "g", 96, COR)], XE, 590)
    E.foco(c, t, c2 + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 76, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 630, 76, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 940, 820
    itens = (("s03.b", "resolver equação fazendo", "o mesmo dos dois lados"), ("s03.c", "abrir parênteses:", "o de fora vezes cada termo"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 160)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, pal("s03", "se"), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 940, 800, "left", 0.12)


# ---------------- o que é sistema e solução ----------------
def b_sistema(c, t, C, b):
    ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    E.frase(c, t, pal("s04", "duas"), ps("duas equações valendo", "i", 70) + [("ao mesmo tempo", "g", 72)], XE, 170, "left", 0.11)
    E.frase(c, t, kb - 0.4, ps("formam um", "i", 84) + [("sistema", "g", 120, COR)], XE, 320, "left", 0.12)
    E.sistema(c, t, kc - 0.2, ["x + y = 5", "2x + y = 7"], XE + 40, 540, 110, tl=(kc, kd))
    xr = 1300

    def teste1():
        a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
        E.foco(c, t, a5, 0.5, lambda a: E.pilula(c, "x = 2 e y = 3?", xr, 380, 64, "g", a=a, cor=E.SOBRE))
        fcen(c, t, b5, "2 + 3 = 5", xr, 560, 96)
        selo_em(c, t, c5, xr + 330, 525, 46, True)
        fcen(c, t, d5, "2 × 2 + 3 = 7", xr, 720, 96)
        selo_em(c, t, e5, xr + 400, 685, 46, True)
        E.frase(c, t, C["s06.a"] - 0.4, ps("valeu nas duas:", "i", 76) + [("é a solução do sistema", "g", 80, CERTO)], W / 2, 930, "center", 0.11)
    if t < C["s06.b"] + 0.4:
        E.saida(c, t, C["s06.b"] - 0.1, teste1)
    if t < C["s06.b"]:
        return
    b6, c6, d6, e6 = C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "x = 1 e y = 4?", xr, 380, 64, "g", a=a, cor=E.SOBRE))
    fcen(c, t, c6, "1 + 4 = 5", xr, 560, 96)
    selo_em(c, t, c6 + 0.6, xr + 330, 525, 46, True)
    fcen(c, t, d6, "2 × 1 + 4 = 6", xr, 720, 96)
    E.frase(c, t, pal("s06", "não"), ps("e não 7", "i", 56, ERRADO), xr, 800, "center", 0.1)
    selo_em(c, t, pal("s06", "não"), xr + 400, 685, 46, False)
    E.frase(c, t, e6, ps("falhou em uma:", "i", 76) + [("não serve", "g", 80, ERRADO)], W / 2, 950, "center", 0.11)


# ---------------- o problema ----------------
def b_problema(c, t, C, b):
    def enunciado():
        ka, kb, kc = C["s07.a"], C["s07.b"], C["s07.c"]
        E.frase(c, t, pal("s07", "mas"), ps("como achar a solução", "i", 72, TINTA2) + [("do zero?", "g", 76, TINTA2)], W / 2, 170, "center", 0.11)
        E.frase(c, t, pal("s07", "num"), ps("num estacionamento:", "i", 72), XE, 320)
        E.frase(c, t, ka, [("30", "g", 150, COR)] + ps("veículos,", "i", 80), XE, 500, passo=0.14)
        E.frase(c, t, pal("s07", "entre"), ps("entre", "i", 64, TINTA2) + [("carros e motos", "g", 66, TINTA2)], XE + 560, 500, passo=0.1)
        E.frase(c, t, kb, [("100", "g", 150, COR)] + ps("rodas no total", "i", 80), XE, 690, passo=0.14)
        E.frase(c, t, kc, ps("quantos são os", "i", 80) + [("carros", "g", 84, COR)] + ps("e quantas são as", "i", 80) + [("motos?", "g", 84, COR)], W / 2, 900, "center", 0.1)
    E.saida(c, t, C["s08"] - 0.1, enunciado)
    if t < C["s08"]:
        return
    ka, kb, kc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    E.frase(c, t, ka, [("x", "g", 96, COR)] + ps("= número de carros", "i", 72), 280, 210, "left", 0.12)
    E.frase(c, t, kb, [("y", "g", 96, COR)] + ps("= número de motos", "i", 72), 1060, 210, "left", 0.12)
    E.sistema(c, t, kc - 0.2, ["x + y = 30", "4x + 2y = 100"], 520, 480, 120, tl=(kc, kd))
    E.frase(c, t, kc + 0.8, ps("veículos", "i", 60, TINTA2), 1400, 480)
    E.frase(c, t, kd + 1.0, ps("rodas", "i", 60, TINTA2), 1400, 654)
    E.frase(c, t, pal("s08", "cada"), ps("cada carro tem", "i", 64) + [("4 rodas,", "g", 68, COR)] + ps("cada moto tem", "i", 64) + [("2", "g", 68, COR)], W / 2, 900, "center", 0.1)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    def passo1():
        ka, kb, kc = C["s09.a"], C["s09.b"], C["s09.c"]
        E.sistema(c, t, C["s09"], ["x + y = 30", "4x + 2y = 100"], XE + 20, 170, 70)
        E.frase(c, t, ka - 0.2, ps("substituição:", "i", 64, TINTA2) + [("3 passos", "g", 70, COR)], 1000, 170, "left", 0.12)
        passo(c, t, kb, 1, "passo 1:", "deixe uma letra sozinha", 460)
        linhas = ((pal("s09", "primeira"), "x + y", "30"), (kc, "y", "30 − x"))
        pilha(c, t, linhas, {0: (pal("s09", "tire"), "− x")}, 1380, 420, 210, 110)
        E.frase(c, t, pal("s09", "motos"), ps("motos = 30 − carros", "i", 60, TINTA2), 1380, 800, "center", 0.1)
    E.saida(c, t, C["s10"] - 0.1, passo1)

    def passo2():
        ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
        a1, b1, c1, d1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        passo(c, t, ka, 2, "passo 2:", "troque essa letra na outra equação", 160)
        E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "y → (30 − x)", 1560, 370, 56, "g", a=a, cor=E.SOBRE))
        linhas = ((pal("s10", "outra"), "4x + 2y", "100"), (kc, "4x + 2(30 − x)", "100"), (b1 + 0.6, "4x + 60 − 2x", "100"), (d1, "2x + 60", "100"))
        pilha(c, t, linhas, {}, 950, 380, 165, 96)
        fcen(c, t, a1, "2 × 30 = 60", 1560, 560, 64, TINTA2)
        fcen(c, t, b1, "2 × (−x) = −2x", 1560, 680, 64, TINTA2)
        fcen(c, t, c1, "4x − 2x = 2x", 1560, 800, 64, TINTA2)
    if C["s10"] - 0.1 <= t:
        E.saida(c, t, C["s12"] - 0.1, passo2)

    def balanca():
        ka, kb, kc, kd = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
        E.frase(c, t, C["s12"] + 0.2, ps("daqui em diante,", "i", 64, TINTA2) + [("é a balança", "g", 66, TINTA2)], W / 2, 140, "center", 0.11)
        linhas = ((C["s12"] + 0.1, "2x + 60", "100"), (kb, "2x", "40"), (kd, "x", "20"))
        pilha(c, t, linhas, {0: (ka, "− 60"), 1: (kc, "÷ 2")}, W / 2, 320, 240, 120)
        E.foco(c, t, pal("s12", "são"), 0.5, lambda a: E.pilula(c, "20 carros", 1450, 770, 70, "g", a=a, cor=E.SOBRE))
    if C["s12"] - 0.1 <= t:
        E.saida(c, t, C["s13"] - 0.1, balanca)
    if t < C["s13"]:
        return
    ka, kb, kc = C["s13.a"], C["s13.b"], C["s13.c"]
    passo(c, t, ka, 3, "passo 3:", "volte e ache a outra letra", 200)
    fcen(c, t, pal("s13", "ípsilon"), "y = 30 − x", W / 2, 440, 110)
    fcen(c, t, kb, "y = 30 − 20 = 10", W / 2, 610, 110, COR)
    bnum(c, t, kc, "20", 620, 830, 90, None, 96)
    E.frase(c, t, kc + 0.2, [("carros", "g", 84)], 740, 860)
    bnum(c, t, pal("s13", "dez", 2), "10", 1160, 830, 90, None, 96)
    E.frase(c, t, pal("s13", "dez", 2) + 0.2, [("motos", "g", 84)], 1280, 860)


# ---------------- conferir ----------------
def b_conferir(c, t, C, b):
    ka, kb, kc, kd, ke, kf = (C[f"s14.{k}"] for k in "abcdef")
    E.frase(c, t, C["s14"] + 0.3, ps("confira", "i", 84) + [("nas duas equações", "g", 84, COR)], W / 2, 160, "center", 0.12)
    E.sistema(c, t, ka, ["x + y = 30", "4x + 2y = 100"], XE + 20, 380, 100, dy=250)
    fcen(c, t, kb, "20 + 10 = 30", 1220, 380, 96)
    selo_em(c, t, kb + 1.2, 1610, 345, 44, True)
    fcen(c, t, kc, "4 × 20 = 80", 1220, 580, 80, TINTA2)
    fcen(c, t, kd, "2 × 10 = 20", 1220, 690, 80, TINTA2)
    fcen(c, t, ke, "80 + 20 = 100", 1220, 820, 96)
    selo_em(c, t, kf, 1640, 785, 44, True)
    E.frase(c, t, kf + 0.1, [("bateu!", "g", 100, CERTO)], W / 2, 990, "center")


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s15"] + 0.4, ps("cuidado: o erro", "i", 72) + [("mora no parêntese", "g", 76, ERRADO)], W / 2, 150, "center", 0.11)
    fcen(c, t, pal("s15", "parêntese"), "2(30 − x)", W / 2, 320, 130)
    E.frase(c, t, a5, ps("multiplicou", "i", 56, ERRADO) + [("só o 30", "g", 58, ERRADO)], 560, 440, "center", 0.1)
    fcen(c, t, b5, "60 − x", 500, 570, 110, ERRADO)
    selo_em(c, t, b5 + 0.5, 760, 535, 44, False)
    E.frase(c, t, c5 - 0.4, ps("em vez de", "i", 56, CERTO), 1360, 440, "center", 0.1)
    fcen(c, t, c5, "60 − 2x", 1300, 570, 110, CERTO)
    selo_em(c, t, c5 + 0.5, 1590, 535, 44, True)
    fcen(c, t, a6, "3x = 40", 500, 740, 100, ERRADO)
    E.frase(c, t, pal("s16", "quarenta", 2), ps("40 ÷ 3", "g", 72) + ps("não dá", "i", 66) + [("número inteiro", "g", 70, ERRADO)], 1300, 740, "center", 0.1)
    E.frase(c, t, pal("s16", "ninguém"), ps("ninguém estaciona um pedaço de carro", "i", 60, TINTA2), W / 2, 850, "center", 0.08)
    E.frase(c, t, c6 - 0.6, ps("o número de fora", "i", 72) + [("multiplica tudo o que está dentro", "g", 72, COR)], W / 2, 980, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        ka, kb = C["s17.a"], C["s17.b"]
        E.frase(c, t, C["s17"] + 0.3, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("deixe sozinha a letra", "i", 80, CLARO) + [("sem número na frente", "g", 84, BR)], W / 2, 290, "center", 0.11)
        E.frase(c, t, pal("s17", "a", 2), ps("a que tem o", "i", 72, CLARO) + [("1 escondido:", "g", 76, BR)], 760, 440, "center", 0.11)
        fcen(c, t, pal("s17", "um"), "1x = x", 1360, 440, 90, CLARO)
        fcen(c, t, pal("s17", "em"), "x + y = 30", W / 2, 650, 130, BR)
        E.frase(c, t, pal("s17", "nenhuma"), ps("nenhuma letra tem número na frente", "i", 64, CLARO), W / 2, 770, "center", 0.08)
        E.frase(c, t, kb - 0.3, ps("tire uma delas:", "i", 72, CLARO), 640, 940, "center", 0.1)
        fcen(c, t, kb + 0.6, "y = 30 − x", 1240, 940, 110, BR)
    E.saida(c, t, C["s18"] - 0.1, regra)
    if t < C["s18"]:
        return
    ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, ka - 0.4, ps("assim,", "i", 84, CLARO) + [("você não divide nada", "g", 90, BR)], W / 2, 200, "center", 0.12)
    E.frase(c, t, pal("s18", "se"), ps("isolar o x na segunda?", "i", 70, CLARO), W / 2, 350, "center", 0.1)
    fcen(c, t, pal("s18", "segunda"), "4x + 2y = 100", 560, 540, 100, BR)
    E.foco(c, t, kb, 0.5, lambda a: M.arrow(c, 920, 510, 1080, 510, CLARO, a, 6, 20))
    fcen(c, t, kb + 0.2, "x = f{100 − 2y}{4}", 1400, 540, 100, CLARO)
    E.frase(c, t, pal("s18", "apareceria"), ps("apareceria", "i", 60, CLARO) + [("fração", "g", 64, BR)], 1400, 700, "center", 0.1)
    selo_em(c, t, kc, 300, 840, 46, False)
    E.frase(c, t, kc + 0.1, ps("todas as letras com número na frente?", "i", 66, CLARO), 380, 865, "left", 0.08)
    E.frase(c, t, pal("s18", "outro"), [("outro método compensa mais", "g", 76, BR)], 380, 975)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, C["s19"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    E.frase(c, t, pal("s19", "resolva"), ps("resolva por", "i", 76) + [("substituição", "g", 80)], XE, 300, passo=0.12)
    E.sistema(c, t, ka - 0.2, ["x + y = 12", "3x + y = 20"], XE + 30, 500, 120, tl=(ka, kb))
    E.frase(c, t, kc, ps("quanto valem", "i", 80) + [("x", "g", 84, COR)] + ps("e", "i", 80) + [("y?", "g", 84, COR)], XE, 900, passo=0.12)
    E.relogio(c, t, C["s20.a"], 1520, 360, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def resolve():
        ka, kb, kc = C["s21.a"], C["s21.b"], C["s21.c"]
        a2, b2, c2, d2 = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]
        fcen(c, t, ka, "y = 12 − x", 900, 150, 90, COR)
        linhas = ((kb, "3x + (12 − x)", "20"), (pal("s21", "frente"), "3x + 12 − x", "20"), (kc, "2x + 12", "20"), (b2, "2x", "8"), (c2, "x", "4"))
        pilha(c, t, linhas, {2: (a2, "− 12"), 3: (pal("s22", "dividindo"), "÷ 2")}, 900, 320, 152, 96)
        E.foco(c, t, pal("s21", "com"), 0.5, lambda a: E.pilula(c, "com + na frente, o parêntese some", 1480, 240, 42, "g", a=a, cor=E.SOBRE))
        fcen(c, t, pal("s22", "e"), "y = 12 − 4", 1550, 760, 84)
        fcen(c, t, d2, "y = 8", 1550, 900, 110, COR)
    E.saida(c, t, C["s23"] - 0.1, resolve)
    if t < C["s23"]:
        return
    ka, kb, kc = C["s23.a"], C["s23.b"], C["s23.c"]
    fcen(c, t, C["s23"], "x = 4  e  y = 8", W / 2, 200, 120, COR)
    fcen(c, t, ka, "4 + 8 = 12", 860, 430, 100)
    selo_em(c, t, ka + 1.1, 1220, 395, 46, True)
    fcen(c, t, kb, "3 × 4 + 8 = 20", 860, 620, 100)
    selo_em(c, t, kb + 3.2, 1300, 585, 46, True)
    E.frase(c, t, kc, [("bateu nas duas!", "g", 100, CERTO)], W / 2, 860, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.3, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s24.a", "deixe uma letra sozinha"), ("s24.b", "troque na outra equação"), ("s24.c", "confira nas duas"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 350, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    ka, kb, kc = C["s25.a"], C["s25.b"], C["s25.c"]
    E.frase(c, t, C["s25"] + 0.3, ps("e quando nenhuma letra está sozinha?", "i", 72, TINTA2), XE, 200, passo=0.09)
    E.frase(c, t, pal("s25", "na"), ps("na próxima aula", "i", 84), XE, 340, passo=0.14)
    E.frase(c, t, ka - 0.3, ps("some", "i", 110) + [("as equações", "g", 120, COR)], XE, 500, passo=0.14)
    E.frase(c, t, pal("s25", "para"), ps("para uma letra", "i", 80) + [("sumir", "g", 84, COR)], XE, 630, passo=0.12)
    E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 770, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kb + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1000, 795, p), ep(t, kb + 0.2, 0.4))
    E.frase(c, t, kc, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sistema=b_sistema, problema=b_problema, metodo=b_metodo, conferir=b_conferir,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
