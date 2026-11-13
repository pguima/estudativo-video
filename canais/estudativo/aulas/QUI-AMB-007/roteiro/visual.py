"""Visual — Estudativo · QUI-AMB-007: praticando química e ambiente (aula de prática, última de Química do Zero).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a LINGUAGEM VISUAL DA QUÍMICA AMBIENTAL
(cabeçalho de QUI-AMB-001/roteiro/visual.py). Nesta aula, cada questão abre com o TEXTO da prova num cartão (anuncio):
o trecho que a questão põe à prova fica sublinhado; na resolução, a afirmação errada ganha risco e selo vermelho, e a
versão certa entra embaixo, na cor da matéria.
Peças candidatas ao kit: anuncio (cartão de texto de prova com trecho marcado), barra_massa (já em QUI-AMB-006).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Química e Ambiente")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-AMB-007_praticando_quimica_ambiente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q2", "q3", "q4", "fim"))
BR = "#FFFFFF"
MASSA = {"H": 1, "C": 12, "O": 16}


def mm(f):
    return sum(MASSA[k] * n for k, n in Q.contar(f).items())


ROTA_A, ROTA_B = "C2H4 + H2O -> C2H6O", "C6H12O6 -> 2 C2H6O + 2 CO2"
for e in (ROTA_A, ROTA_B, "C2H6O + 3 O2 -> 2 CO2 + 3 H2O", "SO3 + H2O -> H2SO4"):
    r, p = Q.lados(e)
    assert r == p, e
assert mm("C2H4") == 28 and mm("H2O") == 18 and mm("C2H6O") == 46 and mm("C6H12O6") == 180
assert mm("C2H4") + mm("H2O") == mm("C2H6O")            # rota A: 100%
assert 2 * 46 == 92 and round(92 / 180 * 100) == 51      # rota B: cerca de 51%


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def riscado(c, t, t0, s, x, y, size=56, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, est, ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, est, size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def titulo_q(c, t, t0, n):
    E.frase(c, t, t0, [("questão", "i", 70, TINTA2), (str(n), "g", 80, COR)], XE, 170, passo=0.12)


def anuncio(c, t, t0, linhas, x, y, w, size=58, tl=None, marca=None, tm=None):
    """cartão com o texto da prova; linhas entram em tl[k]; marca = índices sublinhados em tm"""
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    h = 80 + len(linhas) * size * 1.5
    M.rrect(c, x, y, w, h, 30, BR, q, stroke=3, stroke_color=FIO)
    M.rrect(c, x, y, 18, h, 9, E.COR, q)
    for k, s in enumerate(linhas):
        ti = tl[k] if tl else t0
        yy = y + 60 + size * 0.9 + k * size * 1.5
        E.foco(c, t, ti, 0.4, lambda a, s=s, yy=yy: E.escreve(c, s, x + 60, yy, size, "b", TINTA, a))
        if marca and k in marca and tm is not None and t >= tm:
            p = ease_io(prog(t, tm, 0.6))
            M.line(c, x + 60, yy + 14, x + 60 + E.larg(s, "b", size) * p, yy + 14, ERRADO, 1, 6)
    return h


def pausa(c, t, t0, texto):
    E.frase(c, t, t0, ps(texto, "i", 56, TINTA2), XE, 290, passo=0.08)
    E.relogio(c, t, t0 + 0.05, cx=W / 2, cy=620, r=200)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, (s, x, y, g) in enumerate((("anúncio", 330, 520, -6), ("notícia", 960, 470, 4), ("laudo de rio", 1590, 540, -3))):
            E.foco(c, t, C["s01.a"] + 0.3 * k, 0.5, lambda a, s=s, x=x, y=y, g=g: (c.save(), c.rotate(0),
                                                                                  M.rrect(c, x - 230, y - 160, 460, 320, 26, BR, a, stroke=3, stroke_color=FIO),
                                                                                  [M.rrect(c, x - 180, y - 60 + 50 * j, 360 - 60 * (j % 2), 18, 9, "#E3E5E8", a) for j in range(4)],
                                                                                  centro(c, s, x, y - 90, 48, "g", COR, a), c.restore()))
        E.frase(c, t, C["s01.b"], ps("a prova traz um texto e pergunta o que está certo", "i", 56), W / 2, 820, "center", 0.08)
        E.frase(c, t, C["s01.c"], [("4", "g", 80, COR), ("textos,", "i", 70), ("cada", "i", 70), ("um", "i", 70), ("com", "i", 70), ("uma", "i", 70), ("armadilha", "g", 70, ERRADO)], W / 2, 960, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 80, TINTA2), XE, 240, passo=0.12)
    for k, (key, s) in enumerate((("s02.a", "combustíveis"), ("s02.b", "chuva ácida"), ("s02.c", "efeito estufa"), ("s02.d", "oxigênio dissolvido"), ("s02.e", "economia atômica"))):
        y = 380 + 120 * k
        E.foco(c, t, C[key], 0.4, lambda a, y=y: E.bola(c, XE + 30, y - 24, 22, a=a))
        E.frase(c, t, C[key] + 0.1, [(s, "g", 64)], XE + 90, y)
    pilula_em(c, t, C["s02.e"] + 1.2, "faltou alguma? procure no canal", 1400, 1000, 44, TINTA)


# ---------------- Q1 ----------------
def b_q1(c, t, C, b):
    titulo_q(c, t, C["s03.a"], 1)
    linhas = ["Carro a etanol:", "emissão zero de gás carbônico", "e ainda protege a camada de ozônio!"]
    if t < C["s04"]:
        anuncio(c, t, C["s03.a"], linhas, XE, 280, 1300, 64, tl=[C["s03.a"] + 0.4, C["s03.b"], C["s03.c"]], marca=(1, 2), tm=C["s03.d"])
        E.frase(c, t, C["s03.d"], ps("o que está errado nas duas promessas?", "i", 60), XE, 860, passo=0.08)
        return
    if t < C["s05"]:
        pausa(c, t, C["s04"], "o que está errado nas duas promessas?")
        return
    anuncio(c, t, C["s05"], linhas, XE, 220, 1100, 48, marca=(1, 2), tm=C["s05"])
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.selo(c, XE + 1160, 385, 36, False, a))
    if t < C["s06"]:
        Q.equacao(c, t, C["s05.b"], "C2H6O + 3 O2 -> 2 CO2 + 3 H2O", W / 2, 620, 84, tl=[C["s05.b"] + 0.2 * k for k in range(8)], cores={"CO2": E.COR})
        E.frase(c, t, C["s05.c"], ps("a cana retirou esse carbono do ar ao crescer:", "i", 52), XE, 790, passo=0.06)
        E.frase(c, t, C["s05.d"], [("o", "i", 56), ("ciclo", "g", 56, COR), ("fecha", "i", 56), ("em", "i", 56), ("parte", "g", 56, COR)], XE, 880, passo=0.1)
        E.foco(c, t, C["s05.e"], 0.4, lambda a: E.escreve(c, "plantar e transportar também emitem", XE, 970, 48, "b", TINTA2, a))
        return
    E.foco(c, t, C["s06.a"], 0.4, lambda a: E.selo(c, XE + 1160, 457, 36, False, a))
    E.frase(c, t, C["s06.a"], ps("a segunda mistura os assuntos:", "i", 56, TINTA2), XE, 560, passo=0.08)
    E.frase(c, t, C["s06.b"], [("CO₂", "g", 60), ("é", "i", 60), ("gás", "g", 60, COR), ("estufa:", "g", 60, COR), ("segura", "i", 60), ("calor", "i", 60)], XE, 680, passo=0.1)
    E.frase(c, t, C["s06.c"], [("o", "i", 60), ("ozônio", "g", 60), ("é", "i", 60), ("atacado", "i", 60), ("pelo", "i", 60), ("cloro", "g", 60, COR), ("do", "i", 60), ("CFC", "g", 60, COR)], XE, 790, passo=0.1)
    pilula_em(c, t, C["s06.d"], "trocar gasolina por etanol não protege a camada de ozônio", W / 2, 950, 44, E.COR)


# ---------------- Q2 ----------------
def b_q2(c, t, C, b):
    titulo_q(c, t, C["s07.a"], 2)
    linhas = ["A cidade troca o diesel dos ônibus", "por um com muito menos enxofre."]
    if t < C["s08"]:
        anuncio(c, t, C["s07.b"], linhas, XE, 280, 1300, 60, tl=[C["s07.b"], C["s07.b"] + 1.0])
        E.frase(c, t, C["s07.c"], [("1", "g", 60, COR)] + ps("qual poluente cai?", "i", 62), XE, 680, passo=0.1)
        E.frase(c, t, C["s07.d"], [("2", "g", 60, COR)] + ps("que estrago ele fazia no mármore da praça?", "i", 62), XE, 800, passo=0.08)
        return
    if t < C["s09"]:
        pausa(c, t, C["s08"], "qual poluente cai? que estrago fazia?")
        return
    Q.formula_em(c, t, C["s09.a"], "SO2", XE, 300, 110, cores={"SO2": E.COR})
    E.foco(c, t, C["s09.a"] + 0.4, 0.4, lambda a: E.escreve(c, "cai: menos enxofre, menos SO₂", XE + 300, 290, 56, "g", TINTA, a))
    Q.formula_em(c, t, C["s09.b"], "SO2 -> SO3", XE, 470, 90)
    Q.formula_em(c, t, C["s09.c"], "SO3 + H2O -> H2SO4", XE + 640, 470, 90, cores={"H2SO4": E.COR})
    E.frase(c, t, C["s09.d"], ps("chuva ácida: corrói o carbonato de cálcio do mármore", "i", 54), XE, 620, passo=0.06)
    Q.formula_em(c, t, C["s09.d"] + 1.6, "CaCO3", XE + 1360, 625, 60)
    riscado(c, t, C["s10.a"], "a pegadinha: dizer que cai o CO₂", XE, 820, 56, "b")
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "o CO₂ vem do carbono do diesel, e isso não mudou", XE, 920, 48, "b", TINTA2, a))


# ---------------- Q3 ----------------
def b_q3(c, t, C, b):
    titulo_q(c, t, C["s11.a"], 3)
    linhas = ["Usina devolve ao rio a água de resfriamento,", "limpa, 8 °C mais quente.", "Fiscal: a DBO não mudou, não há poluição."]
    if t < C["s12"]:
        anuncio(c, t, C["s11.b"], linhas, XE, 280, 1500, 56, tl=[C["s11.b"], C["s11.b"] + 1.2, C["s11.c"]], marca=(2,), tm=C["s11.d"])
        E.frase(c, t, C["s11.d"], ps("ele está certo?", "i", 70, COR), XE, 840, passo=0.12)
        return
    if t < C["s13"]:
        pausa(c, t, C["s12"], "o fiscal está certo?")
        return
    anuncio(c, t, C["s13"], linhas[2:], XE, 220, 1300, 50, marca=(0,), tm=C["s13"])
    E.foco(c, t, C["s13.a"], 0.4, lambda a: E.selo(c, XE + 1380, 290, 40, False, a))
    E.frase(c, t, C["s13.b"], ps("água mais quente dissolve menos oxigênio", "i", 58), XE, 470, passo=0.08)
    E.foco(c, t, C["s13.b"] + 1.2, 0.4, lambda a: E.escreve(c, "como o refrigerante quente que perde gás", XE, 540, 44, "b", TINTA2, a))
    E.frase(c, t, C["s13.c"], [("o", "i", 60), ("OD", "g", 60, ERRADO), ("cai,", "i", 60), ("sem", "i", 60), ("esgoto", "g", 60), ("nenhum", "i", 60)], XE, 660, passo=0.1)
    E.frase(c, t, C["s13.d"], ps("e no calor o peixe precisa de mais oxigênio", "i", 54), XE, 770, passo=0.08)
    pilula_em(c, t, C["s13.e"], "poluição térmica: a DBO não mede isso", W / 2, 920, 50, ERRADO)


# ---------------- Q4 ----------------
def b_q4(c, t, C, b):
    titulo_q(c, t, C["s14.a"], 4)
    if t < C["s15.b"]:
        E.frase(c, t, C["s14.a"] + 0.6, ps("dois caminhos para o etanol", "i", 60, TINTA2), XE, 280, passo=0.1)
        E.foco(c, t, C["s14.b"], 0.4, lambda a: E.escreve(c, "rota A (eteno, do petróleo)", XE, 400, 48, "g", TINTA, a))
        Q.formula_em(c, t, C["s14.b"] + 0.4, ROTA_A, XE, 490, 76)
        E.foco(c, t, C["s14.c"], 0.4, lambda a: E.escreve(c, "rota B (glicose, da cana)", XE, 620, 48, "g", COR, a))
        Q.formula_em(c, t, C["s14.c"] + 0.4, ROTA_B, XE, 710, 76)
        E.frase(c, t, C["s14.d"], [("1", "g", 56, COR)] + ps("maior economia atômica?", "i", 58), XE, 850, passo=0.08)
        E.frase(c, t, C["s14.e"], [("2", "g", 56, COR)] + ps("que princípio a rota B cumpre melhor?", "i", 58), XE, 950, passo=0.08)
        E.foco(c, t, C["s15.a"], 0.4, lambda a: (M.rrect(c, 1180, 380, 640, 360, 30, BR, a, stroke=3, stroke_color=FIO),
                                                [E.escreve(c, s, 1230, 460 + 80 * k, 52, "b", TINTA, a) for k, s in enumerate(("eteno = 28", "água = 18", "etanol = 46", "glicose = 180"))]))
        return
    if t < C["s16"]:
        pausa(c, t, C["s15.b"] - 0.3, "economia atômica de cada rota? e o princípio da B?")
        return
    E.foco(c, t, C["s16"], 0.4, lambda a: E.escreve(c, "rota A", XE, 300, 60, "g", TINTA, a))
    Q.formula_em(c, t, C["s16"], ROTA_A, XE + 260, 300, 66)
    pilula_em(c, t, C["s16.a"], "um produto só", XE + 190, 400, 44, TINTA)
    bola_txt(c, t, C["s16.b"], "100%", 1720, 280, 80, 52, CERTO)
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.escreve(c, "rota B", XE, 560, 60, "g", COR, a))
    Q.formula_em(c, t, C["s16.c"], ROTA_B, XE + 260, 560, 66)
    E.formula_em(c, t, C["s16.c"] + 0.6, "2 × 46 = 92", XE + 260, 660, 60, "g", TINTA2)
    E.formula_em(c, t, C["s16.d"], "92 ÷ 180 × 100 ≈", XE + 1000, 660, 60, "g", TINTA)
    bola_txt(c, t, C["s16.d"] + 0.8, "51%", 1720, 560, 80, 60)
    E.frase(c, t, C["s17.a"], ps("na economia atômica, a rota A vence", "i", 54), XE, 800, passo=0.08)
    pilula_em(c, t, C["s17.b"], "a rota B usa matéria-prima renovável: a cana", 1080, 890, 44, E.COR)
    E.frase(c, t, C["s17.c"], ps("doze princípios: um número só não decide", "i", 52, TINTA2), XE, 1000, passo=0.06)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("as", "i", 80, TINTA2), ("quatro", "i", 80, TINTA2), ("lições", "g", 80, COR)], W / 2, 180, "center", 0.12)
        itens = (("s18.a", [("renovável", "g", 62), ("≠", "g", 62, ERRADO), ("emissão", "i", 66), ("zero", "i", 66)]),
                 ("s18.b", [("enxofre", "g", 62), ("vira", "i", 66), ("chuva", "g", 62, COR), ("ácida", "g", 62, COR)]),
                 ("s18.c", [("água", "g", 62), ("quente", "g", 62, ERRADO), ("também", "i", 66), ("asfixia", "i", 66)]),
                 ("s18.d", [("economia", "g", 62), ("atômica:", "g", 62), ("um", "i", 66), ("princípio,", "i", 66), ("não", "i", 66), ("o", "i", 66), ("único", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], ps("a última aula de", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, C["s19"] + 1.0, [("Química", "g", 110, COR), ("do", "i", 110), ("Zero", "g", 110, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s19.a"], ps("do átomo até o planeta", "i", 76), XE, 540, passo=0.12)
    E.foco(c, t, C["s19.a"] + 0.4, 0.5, lambda a: (Q.atomo(c, 300, 760, 60, "C", a), M.arrow(c, 400, 760, 640, 760, TINTA2, a, 6, 22), E.bola(c, 800, 760, 120, "#3E7FC1", a)))
    pilula_em(c, t, C["s19.b"], "revise na playlist completa", 1100, 930, 46, TINTA)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, fim=b_fim)
