"""Visual — Estudativo · MAT-TOP-019: combinação com repetição, bolinhas e barras.

Linguagem: cada escolha é uma fila de símbolos. Bolinha = esfera na cor da matéria (um objeto); barra = traço alto em tinta
(separa os tipos). Embaixo de cada espaço entre barras, o nome do tipo (sabor ou letra) em cinza. Os lugares numerados (1, 2, 3...)
aparecem como casinhas tracejadas quando a conta vira "escolher lugares". A conta da combinação segue a das aulas de
Contagem: arranjo em cima, fatorial embaixo. Erro em vermelho, certo em verde, atalho no palco escuro.
Peças locais: fila() (bolinhas e barras numa linha, cada símbolo com o seu instante), lugares() (casinhas numeradas)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-019_combinacao_com_repeticao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("bolinhas", "regra", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
C_ESC = "#3CC7D3"
SABORES = ("chocolate", "morango", "coco", "limão")


def comb(n, p):
    return math.comb(n, p)


assert comb(6, 3) == 20 == 6 * 5 * 4 // 6 and comb(4, 3) == 4 and 4 ** 3 == 64 and comb(12, 2) == 66 == comb(12, 10) == 12 * 11 // 2
assert comb(9, 2) == 36 and comb(6, 2) == 15 == 5 + comb(5, 2) and comb(8, 2) == 28
# conferência por força bruta
assert len({tuple(sorted(s)) for s in __import__("itertools").product(range(4), repeat=3)}) == 20
assert sum(1 for x in range(11) for y in range(11) if 10 - x - y >= 0) == 66
assert sum(1 for x in range(1, 11) for y in range(1, 11) if 10 - x - y >= 1) == 36
assert sum(1 for x in range(7) for y in range(7) if 6 - x - y >= 0) == 28


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return w


def conta_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: conta(c, partes, x, y, size, a, align))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def fila(c, t, simbolos, t0, x, y, passo=110, r=34, dt=0.12, nomes=None, tn=None, escuro=False, cor_b=None):
    """simbolos: string com 'o' (bolinha) e '|' (barra). nomes: um rótulo por espaço entre barras (sabores ou letras)"""
    tinta = BR if escuro else TINTA
    for i, s in enumerate(simbolos):
        cx = x + i * passo
        k = ease_back(prog(t, t0 + dt * i, 0.4))
        if k <= 0:
            continue
        if s == "o":
            E.bola(c, cx, y, r * k, cor_b)
        else:
            M.line(c, cx, y - 70 * k, cx, y + 70 * k, tinta, 1.0, 10)
    if nomes and tn is not None:
        # posição de cada espaço: entre barras
        bars = [i for i, s in enumerate(simbolos) if s == "|"]
        limites = [-1] + bars + [len(simbolos)]
        for j, nome in enumerate(nomes):
            a_, b_ = limites[j], limites[j + 1]
            cx = x + (a_ + b_) / 2 * passo
            qtd = b_ - a_ - 1
            E.foco(c, t, tn + 0.15 * j, 0.4, lambda a, cx=cx, nome=nome, qtd=qtd: (
                E.centro(c, str(qtd), cx, y + 150, 54, "g", COR if not escuro else C_ESC, a),
                E.centro(c, nome, cx, y + 205, 36, "b", CINZA if not escuro else CLARO, a)))


def lugares(c, t, t0, n, x, y, passo=110, escuro=False):
    for i in range(n):
        cx = x + i * passo
        E.foco(c, t, t0 + 0.05 * i, 0.3, lambda a, cx=cx, i=i: (E.caixa_pontilhada(c, cx - 48, y - 90, 96, 180, a, CLARO if escuro else CINZA),
                                                               E.centro(c, str(i + 1), cx, y - 110, 34, "b", CLARO if escuro else TINTA2, a)))


SAB_COR = ("#6B3E26", "#E0508A", "#D9CBB0", "#6BB33A")


def docinho(c, cx, cy, r, i, a=1.0):
    E.bola(c, cx, cy, r, SAB_COR[i], a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        E.frase(c, t, C["s01.a"], [("4", "g", 90, COR), ("sabores", "i", 84)], XE, 260)
        for i, s in enumerate(SABORES):
            cx = 330 + i * 230
            E.foco(c, t, C["s01.a"] + 0.2 + 0.15 * i, 0.4, lambda a, i=i, cx=cx, s=s: (docinho(c, cx, 420, 62, i, a),
                                                                                     E.centro(c, s, cx, 530, 40, "b", TINTA2, a)))
        E.frase(c, t, C["s01.b"], [("levar", "i", 84), ("3", "g", 90, COR), ("doces,", "i", 84), ("pode", "i", 84), ("repetir", "g", 80, COR)], XE, 700)
        for k, s, x in (("s01.c", "4?", 300), ("s01.d", "64?", 620)):
            E.foco(c, t, C[k], 0.4, lambda a, s=s, x=x: E.escreve(c, s, x, 900, 130, "g", ERRADO, a))
            if t >= C[k] + 0.4:
                E.risco(c, x - 10, 920, x + E.larg(s, "g", 130) + 10, 800, t, C[k] + 0.4, largura=12)
        bola_txt(c, t, C["s01.e"], "20", 1500, 750, 140, 130, CERTO)
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("escolher", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.4, [("podendo", "i", 100), ("repetir", "g", 120, COR)], XE, 590)
        E.foco(c, t, C["s02.a"] + 3.2, 0.5, lambda a: E.formula(c, "x + y + z = 10", XE, 730, 80, "g", TINTA2, a))
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 190, "center")
    x, w = 200, 1520
    for k, y in (("s03.b", 280), ("s03.c", 610)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 290, p, prog_=p)
    k = C["s03.b"]
    E.frase(c, t, k, [("combinação:", "g", 62, COR), ("a", "i", 64), ("ordem", "i", 64), ("não", "g", 62), ("importa", "i", 64)], 260, 380)
    conta_em(c, t, k + 2.0, [("8 entre 3:  f{8 · 7 · 6}{3!} = 56", TINTA)], 260, 500, 64)
    k = C["s03.c"]
    E.frase(c, t, k, [("quem", "i", 64), ("entra", "g", 62, COR), ("=", "i", 64), ("quem", "i", 64), ("fica", "i", 64), ("de", "i", 64), ("fora", "g", 62, COR)], 260, 710)
    conta_em(c, t, k + 1.8, [("8 entre 10 = 2 entre 10 = f{10 · 9}{2} = 45", TINTA)], 260, 830, 60)
    E.frase(c, t, C["s04"] - 2.4, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 980, "center", passo=0.1)


# ---------------- por que não é 4 ----------------
def b_problema(c, t, C, b):
    E.frase(c, t, C["s04"], [("por", "i", 80), ("que", "i", 80), ("não", "i", 80), ("é", "i", 80), ("4?", "g", 86, ERRADO)], XE, 230)
    conta_em(c, t, C["s04.a"], [("4 sabores, 3 a 3: f{4 · 3 · 2}{3!} = 4", TINTA)], XE, 380, 62)
    E.frase(c, t, C["s04.b"], ps("só com 3 sabores diferentes", "i", 58, TINTA2), XE, 480, passo=0.1)
    E.frase(c, t, C["s04.b"] + 2.2, [("mas", "i", 70), ("pode", "i", 70), ("repetir:", "g", 66, COR)], XE, 640)
    for i in range(3):
        E.foco(c, t, C["s04.c"] + 0.12 * i, 0.4, lambda a, i=i: docinho(c, 400 + i * 150, 800, 56, 0, a))
    E.foco(c, t, C["s04.c"] + 0.4, 0.4, lambda a: E.centro(c, "3 de chocolate", 550, 910, 40, "b", TINTA2, a))
    for i, s in enumerate((2, 2, 3)):
        E.foco(c, t, C["s04.d"] + 0.12 * i, 0.4, lambda a, i=i, s=s: docinho(c, 1150 + i * 150, 800, 56, s, a))
    E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: E.centro(c, "2 de coco e 1 de limão", 1300, 910, 40, "b", TINTA2, a))


# ---------------- bolinhas e barras ----------------
FX, FP = 520, 150   # início da fila e passo entre símbolos (6 símbolos)


def b_bolinhas(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("bolinhas", "g", 80, COR), ("e", "i", 80), ("barras", "g", 80)], W / 2, 190, "center")

    def s05_06():
        # a fila de exemplo 1: oo|o||
        E.foco(c, t, C["s05.b"], 0.4, lambda a: (E.bola(c, 600, 330, 30, a=a), E.escreve(c, "= 1 doce", 660, 345, 50, "i", TINTA, a)))
        E.foco(c, t, C["s05.c"], 0.4, lambda a: (M.line(c, 1150, 290, 1150, 370, TINTA, a, 10), E.escreve(c, "= separa os sabores", 1190, 345, 50, "i", TINTA, a)))
        E.frase(c, t, C["s05.d"], [("4", "g", 60, COR), ("sabores", "i", 62), ("→", "g", 60), ("3", "g", 60, COR), ("barras", "i", 62)], W / 2, 470, "center")
        fila(c, t, "oo|o||", C["s06.a"], FX, 680, FP, 40, 0.15, SABORES, C["s06.a"] + 1.2)
    E.saida(c, t, C["s06.b"] - 0.1, s05_06)

    def s06b():
        fila(c, t, "|||ooo", C["s06.b"], FX, 600, FP, 40, 0.15, SABORES, C["s06.b"] + 1.0)
    if C["s06.b"] <= t:
        E.saida(c, t, C["s07"] - 0.1, s06b)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("6", "g", 70, COR), ("símbolos:", "i", 66), ("3", "g", 70, COR), ("bolinhas", "i", 66), ("e", "i", 66), ("3", "g", 70),
                               ("barras", "i", 66)], W / 2, 320, "center")
    lugares(c, t, C["s07.b"], 6, FX, 590, FP)
    # bolinhas escolhendo lugares: 2, 3 e 5 (oo|o|| → ocupa 1, 2 e 4)
    for j, pos in enumerate((0, 1, 3)):
        k = ease_back(prog(t, C["s07.b"] + 1.2 + 0.25 * j, 0.4))
        if k > 0:
            E.bola(c, FX + pos * FP, 590, 40 * k)
    for j, pos in enumerate((2, 4, 5)):
        q = ep(t, C["s07.b"] + 2.2 + 0.15 * j, 0.3)
        if q > 0:
            M.line(c, FX + pos * FP, 520, FX + pos * FP, 660, TINTA, q, 10)
    E.frase(c, t, C["s07.b"], ps("escolher 3 lugares entre 6", "i", 62, COR), W / 2, 820, "center", passo=0.1)
    if t >= C["s08"]:
        conta_em(c, t, C["s08.a"], [("f{6 · 5 · 4}{3!} = f{120}{6} = ", TINTA)], 620, 990, 70)
        bola_txt(c, t, C["s08.c"], "20", 1280, 960, 70, 72, CERTO)


# ---------------- a regra e a equação ----------------
def b_regra(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], [("a", "i", 84), ("regra", "g", 84, COR)], XE, 260)
        E.frase(c, t, C["s09.a"], [("n", "g", 72, COR), ("tipos,", "i", 72), ("p", "g", 72, COR), ("objetos", "i", 72)], XE, 420)
        E.frase(c, t, C["s09.b"], [("p", "g", 66, COR), ("bolinhas", "i", 66), ("e", "i", 66), ("n − 1", "g", 66), ("barras", "i", 66)], XE, 560)
        conta_em(c, t, C["s09.c"], [("lugares: p + n − 1", COR)], XE, 720, 76)
        E.frase(c, t, C["s09.c"] + 2.0, ps("escolha os p das bolinhas", "i", 60, TINTA2), XE, 840, passo=0.1)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.formula_em(c, t, C["s10.a"], "x + y + z = 10", W / 2, 260, 100, align="center")
    E.frase(c, t, C["s10.b"], ps("inteiros, sem negativos: 0, 1, 2...", "i", 54, TINTA2), W / 2, 350, "center", passo=0.08)
    sim = "ooo|ooooo|oo"
    x0, p0 = 300, 120
    fila(c, t, sim, C["s10.c"], x0, 560, p0, 30, 0.08, ("x", "y", "z"), C["s10.c"] + 1.6)
    E.frase(c, t, C["s10.d"], [("10", "g", 66, COR), ("bolinhas", "i", 66), ("+", "g", 66), ("2", "g", 66), ("barras", "i", 66), ("=", "g", 66),
                               ("12", "g", 66, COR), ("lugares", "i", 66)], W / 2, 880, "center")
    if t >= C["s11"]:
        def s11():
            conta_em(c, t, C["s11.a"], [("10 entre 12 = 2 entre 12", TINTA2)], 330, 1010, 54)
            conta_em(c, t, C["s11.b"], [("f{12 · 11}{2} = ", TINTA)], 1000, 1010, 60)
            bola_txt(c, t, C["s11.c"], "66", 1330, 985, 62, 60, CERTO)
        s11()


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 230)
    conta_em(c, t, C["s12.a"], [("4 · 4 · 4 = 64", ERRADO)], XE, 400, 96)
    if t >= C["s12.c"]:
        E.risco(c, XE - 10, 420, XE + 640, 320, t, C["s12.c"], largura=12)
    for row, (ordem, y, k) in enumerate((((0, 2), 600, "s12.b"), ((2, 0), 760, "s12.b"))):
        for j, s in enumerate(ordem):
            E.foco(c, t, C[k] + 0.6 * row + 0.15 * j, 0.4, lambda a, s=s, j=j, y=y: docinho(c, 360 + j * 150, y, 50, s, a))
        E.foco(c, t, C[k] + 0.6 * row + 0.3, 0.4, lambda a, y=y, ordem=ordem: E.escreve(c, f"{SABORES[ordem[0]]}, depois {SABORES[ordem[1]]}", 620, y + 18, 56, "i", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "na sacola: a mesma escolha", 760, 910, 54, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s13.a"], [("pelo", "i", 80, CLARO), ("menos", "i", 80, CLARO), ("um", "g", 80, BR), ("para", "i", 80, CLARO), ("cada?", "i", 80, CLARO)],
                W / 2, 290, "center")
        E.frase(c, t, C["s13.b"], [("dê", "g", 70, C_ESC), ("um", "g", 70, C_ESC), ("para", "i", 72, CLARO), ("cada", "i", 72, CLARO), ("antes", "i", 72, CLARO)],
                W / 2, 400, "center")
        # x, y, z recebem uma bolinha cada; sobram 7
        for i, l in enumerate(("x", "y", "z")):
            cx = 560 + i * 400
            E.foco(c, t, C["s13.c"] + 0.2 * i, 0.4, lambda a, cx=cx, l=l: (E.bola(c, cx, 560, 36, a=a), E.centro(c, l, cx, 660, 52, "g", BR, a)))
        E.frase(c, t, C["s13.c"] + 1.0, [("10", "g", 66, BR), ("−", "g", 66, BR), ("3", "g", 66, BR), ("=", "g", 66, CLARO), ("7", "g", 66, C_ESC),
                                         ("sobram", "i", 66, CLARO)], W / 2, 790, "center")
        conta_em(c, t, C["s13.d"], [("7 + 2 = 9 lugares", CLARO)], 520, 940, 64)
        conta_em(c, t, C["s13.e"], [("f{9 · 8}{2} = ", BR), ("36", C_ESC)], 1180, 940, 72)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 260, "center")
    E.frase(c, t, C["s14.a"], ps("garantido o um de cada, o resto é livre", "i", 62, CLARO), W / 2, 420, "center", passo=0.08)
    E.frase(c, t, C["s14.b"], [("não", "g", 72, ERRADO), ("compensa:", "i", 76, CLARO), ("zero", "g", 72, BR), ("permitido", "i", 76, CLARO)], W / 2, 660, "center")
    E.frase(c, t, C["s14.b"] + 2.0, ps("aí, conte direto", "i", 64, CLARO), W / 2, 780, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("1)", "g", 64, COR), ("5", "g", 70), ("sabores,", "i", 70)], XE, 360)
    E.frase(c, t, C["s15.b"], [("2", "g", 70), ("bolas,", "i", 70), ("pode", "i", 70), ("repetir", "g", 66, COR)], XE + 80, 460)
    E.frase(c, t, C["s15.b"] + 1.8, [("quantas", "i", 66), ("casquinhas?", "g", 64, COR)], XE + 80, 560)
    E.frase(c, t, C["s15.c"], [("2)", "g", 64, COR)], XE, 740)
    E.foco(c, t, C["s15.c"] + 0.3, 0.4, lambda a: E.formula(c, "x + y + z = 6", XE + 90, 740, 80, "g", TINTA, a))
    E.frase(c, t, C["s15.c"] + 2.0, ps("inteiros, sem negativos", "i", 56, TINTA2), XE + 90, 840, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1480, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        fila(c, t, "o||o||", C["s17.a"], 560, 360, 140, 38, 0.12)
        E.frase(c, t, C["s17.a"] + 1.0, [("2", "g", 60, COR), ("bolinhas", "i", 62), ("+", "g", 60), ("4", "g", 60), ("barras", "i", 62), ("=", "g", 60),
                                         ("6", "g", 60, COR), ("lugares", "i", 62)], W / 2, 560, "center")
        conta_em(c, t, C["s17.b"], [("f{6 · 5}{2} = ", TINTA)], 640, 720, 80)
        bola_txt(c, t, C["s17.b"] + 0.6, "15", 1030, 690, 70, 70, CERTO)
        conta_em(c, t, C["s17.c"], [("5 de um sabor", TINTA2)], 300, 920, 56)
        conta_em(c, t, C["s17.d"], [("+  10 de dois sabores  =  15", TINTA2)], 720, 920, 56)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.formula_em(c, t, C["s18"], "x + y + z = 6", W / 2, 270, 96, align="center")
    fila(c, t, "oo|ooo|o", C["s18.a"], 520, 520, 125, 34, 0.08, ("x", "y", "z"), C["s18.a"] + 0.9)
    conta_em(c, t, C["s18.a"] + 1.4, [("6 + 2 = 8 lugares", TINTA2)], 330, 900, 60)
    conta_em(c, t, C["s18.b"], [("f{8 · 7}{2} = ", TINTA)], 1000, 900, 74)
    bola_txt(c, t, C["s18.b"] + 0.6, "28", 1360, 875, 70, 70, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", [("repete", "i", 70), ("e", "i", 70), ("sem", "i", 70), ("ordem?", "i", 70), ("bolinhas", "g", 68, COR), ("e", "i", 70), ("barras", "g", 68)]),
                 ("s19.b", [("n", "g", 68, COR), ("tipos", "i", 70), ("→", "g", 68), ("n − 1", "g", 68), ("barras", "i", 70)]),
                 ("s19.c", [("escolha", "i", 70), ("os", "i", 70), ("lugares", "g", 68, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s20"] + 0.8, [("Praticando", "g", 150, COR)], XE, 460)
    E.frase(c, t, C["s20.a"], ps("binômio e acertos exatos", "i", 58, TINTA2), XE, 580, passo=0.08)
    E.frase(c, t, C["s20.b"], ps("casa dos pombos, inclusão e exclusão, bolinhas", "i", 58, TINTA2), XE, 670, passo=0.08)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(620, 325, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, problema=b_problema, bolinhas=b_bolinhas, regra=b_regra, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
