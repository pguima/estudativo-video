"""Visual — Estudativo · FIS-OND-005: praticando ondas e seus fenômenos (cinco questões inéditas).
Linguagem visual da trilha Ondas e Som: docstring do visual.py da FIS-OND-001 (onda laranja sobre eixo tracejado, λ na
grotesca, segunda onda em azul F.NEG, conta em pilha com o resultado na esfera). Prática no modelo da FIS-CIN-010:
cada questão com o enunciado à esquerda, o desenho à direita e o relógio de pausa; a resposta numa tela própria.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-005_praticando_ondas_e_fenomenos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 12 / 2 == 6 and 1 / 2 == 0.5 and 6 * 0.5 == 3 and 6 / 2 == 3          # q2: 3 cristas = 2 λ; f = 1/T; v = λf = λ/T
assert abs(0.4 * 2 - 0.8) < 1e-12 and abs(0.4 * 10 - 4) < 1e-12 and abs(0.8 * 10 - 8) < 1e-12 and 8 == 2 * 4   # q3
assert 26 - 20 == 6 and 4 / 2 == 2 and 6 / 2 == 3 and 3 % 2 == 1              # q5: ímpar → destrutiva
assert abs(math.sqrt(1 / 4) - 1 / 2) < 1e-12                                  # q1: L/4 → T/2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças (copiadas da FIS-OND-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def cota(c, t, t0, xa, xb, y, rot, size=56, cor=TINTA):
    """cota horizontal de xa a xb com o rótulo em cima"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    xm = (xa + xb) / 2
    for xx in (xa, xb):
        M.line(c, xx, y - 26, xx, y + 26, cor, q, 4)
    F.seta(c, xm, y, lerp(xm, xa, q), y, cor, 1.0, 5, 20)
    F.seta(c, xm, y, lerp(xm, xb, q), y, cor, 1.0, 5, 20)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, rot, xm, y - 30, size, "g", cor, a))


def titulo_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 46, 168, 46, a=a), centro(c, str(n), XE + 46, 190, 60, "g", BR, a)))
    E.frase(c, t, t0 + 0.1, [("questão", "i", 72, COR)], XE + 120, 192)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01"], ps("questão de ondas pede", "i", 80), XE, 230, passo=0.12)
    E.frase(c, t, C["s01.a"], [("uma", "i", 80), ("de", "i", 80), ("duas", "g", 80, COR), ("coisas", "i", 80)], XE, 340, passo=0.12)
    for i, (k, s) in enumerate((("s01.b", "conta: v = λ · f"), ("s01.c", "nome do fenômeno"))):
        y = 520 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, XE + 110, y, 80, "g", TINTA, a))
    F.onda(c, t, C["s01.b"] + 0.3, 1180, 1760, 470, 60, 190, d=1.0, velocidade=90)
    tb = C["s01.d"]
    E.foco(c, t, tb, 0.6, lambda a: E.simbolo(c, 1470, 760, 170 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s01.d"], [("5", "g", 110, COR), ("questões", "g", 90)], XE, 920, passo=0.15)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 84), XE, 230, passo=0.14)
    itens = (("s02.a", "pêndulo e mola"), ("s02.b", "v = λ · f"), ("s02.c", "reflexão, refração, difração"), ("s02.d", "interferência e polarização"))
    for i, (k, s) in enumerate(itens):
        y = 400 + i * 140
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 36, a=a), centro(c, str(i + 1), XE + 40, y - 6, 46, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y, i=i: E.formula(c, s, XE + 110, y, 68, "g", COR if i == 1 else TINTA, a))
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.5), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), XE, 990, passo=0.12)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    E.frase(c, t, C["s03"], ps("o que a onda", "i", 84) + [("fez?", "g", 84, COR)], XE, 200, passo=0.12)
    linhas = (("s03.b", "voltou?", "reflexão"), ("s03.c", "trocou de meio?", "refração"), ("s03.d", "contornou?", "difração"),
              ("s03.e", "encontrou outra?", "interferência"))
    for i, (k, p_, r_) in enumerate(linhas):
        y = 350 + i * 130
        E.frase(c, t, C[k], ps(p_, "i", 70), XE, y, passo=0.1)
        E.foco(c, t, C[k] + 0.5, 0.4, lambda a, y=y: F.seta(c, 820, y - 22, 960, y - 22, TINTA2, a, 6))
        E.frase(c, t, C[k] + 0.6, [(r_, "g", 70, COR)], 1000, y)
    pilula(c, t, C["s03.c"] + 1.6, "f fica", 1560, 465, 46, CERTO)
    E.frase(c, t, C["s03.f"], [("conta:", "i", 60, TINTA2), ("f", "g", 60, COR), ("é", "i", 60), ("da", "i", 60), ("fonte;", "g", 60), ("v", "g", 60, COR),
                               ("é", "i", 60), ("do", "i", 60), ("meio", "g", 60)], XE, 960, passo=0.12)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    if t < C["s05"]:
        titulo_q(c, t, C["s04"], 1)
        E.frase(c, t, C["s04.a"], ps("relógio de pêndulo", "i", 70) + [("atrasando", "g", 70, ERRADO)], XE, 330, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("cada ida e volta", "i", 64) + [("demora mais", "g", 64)], XE, 440, passo=0.1)
        for i, s in enumerate(("bola mais pesada", "alongar o fio", "encurtar o fio")):
            y = 600 + i * 120
            E.foco(c, t, C["s04.c"] + 0.9 * i, 0.4, lambda a, s=s, y=y, i=i: (E.pilula(c, "ABC"[i], XE + 30, y - 22, 44, "g", fundo=E.COR, a=a, cor=BR),
                                                                             E.escreve(c, s, XE + 100, y, 60, "g", TINTA, a)))
        if t < C["s04.d"]:
            F.pendulo(c, t, C["s04"], 1420, 160, 560, F.oscila(t, C["s04"] + 0.6, 18, 3.2), r=50)
        else:
            E.relogio(c, t, C["s04.d"], cx=1460, cy=440, r=200)
        return
    E.frase(c, t, C["s05"], [("resposta", "i", 70, COR)], XE, 190)
    E.formula_em(c, t, C["s05.a"], "T = 2π · r{f{L}{g}}", XE, 400, 120, "g", TINTA)
    E.foco(c, t, C["s05.a"] + 0.8, 0.5, lambda a: E.escreve(c, "massa", XE + 760, 380, 80, "g", ERRADO, a))
    if t >= C["s05.a"] + 1.3:
        E.risco(c, XE + 740, 390, XE + 1000, 320, t, C["s05.a"] + 1.3, largura=10)
    E.frase(c, t, C["s05.b"], [("L", "g", 80, COR), ("maior", "i", 80), ("→", "g", 80, TINTA2), ("T", "g", 80), ("maior", "i", 80)], XE, 590, passo=0.12)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: (E.pilula(c, "C", XE + 30, 718, 50, "g", fundo=CERTO, a=a, cor=BR),
                                             E.escreve(c, "encurtar o fio", XE + 110, 740, 80, "g", CERTO, a)))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.formula(c, "f{L}{4} → f{T}{2}", XE, 940, 90, "g", TINTA, a))
    E.foco(c, t, C["s05.d"] + 0.6, 0.4, lambda a: E.escreve(c, "(raiz de 4 é 2)", XE + 480, 930, 52, "b", TINTA2, a))
    E.foco(c, t, C["s05.c"], 0.6, lambda a: F.pendulo(c, 99, 0, 1500, 220, 380, F.oscila(t, C["s05.c"], 18, 1.6), r=46))


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    x0, x1, y, lam = 980, 1820, 520, 300
    if t < C["s07"]:
        titulo_q(c, t, C["s06"], 2)
        E.frase(c, t, C["s06.a"], [("3", "g", 70, COR), ("cristas", "i", 70), ("em", "i", 70), ("12", "g", 70), ("m", "b", 52, F.UNID)], XE, 330, passo=0.12)
        E.frase(c, t, C["s06.b"], ps("boia:", "i", 70) + [("T", "g", 70, COR), ("=", "g", 70, TINTA2), ("2", "g", 70), ("s", "b", 52, F.UNID)], XE, 450, passo=0.12)
        E.frase(c, t, C["s06.c"], [("v?", "g", 100, COR)], XE, 620)
        if t < C["s06.d"]:
            cr = F.onda(c, t, C["s06.a"], x0, x1, y, 70, lam, d=1.0)
            if len(cr) >= 3:
                cota(c, t, C["s06.a"] + 1.2, cr[0], cr[2], y - 140, "12 m")
            if t >= C["s06.b"]:
                xb = cr[1] if len(cr) > 1 else (x0 + x1) / 2
                yb = y - 70 * math.cos(2 * math.pi * (t - C["s06.b"]) / 2.0)
                E.foco(c, t, C["s06.b"], 0.4, lambda a: E.bola(c, xb, yb - 26, 30, "#F2C200", a))
        else:
            E.relogio(c, t, C["s06.d"], cx=1460, cy=440, r=200)
        return
    E.frase(c, t, C["s07"], [("resposta", "i", 70, COR)], XE, 190)
    cr = F.onda(c, t, C["s07"], x0, x1, 380, 60, lam, d=0.8)
    if len(cr) >= 3:
        cota(c, t, C["s07.a"], cr[0], cr[1], 230, "λ", 60, COR)
        cota(c, t, C["s07.a"] + 0.5, cr[1], cr[2], 230, "λ", 60, COR)
    conta(c, t, [(C["s07.a"], "2λ = 12"), (C["s07.b"], "λ = 6 m"), (C["s07.c"], "f = f{1}{2} = 0,5 Hz"), (C["s07.d"], "v = 6 · 0,5")], XE, 380, 165, 90)
    E.foco(c, t, C["s07.e"], 0.5, lambda a: E.formula(c, "ou: v = f{λ}{T} = f{6}{2}", 1000, 640, 80, "g", TINTA2, a))
    bola_txt(c, t, C["s07.d"] + 0.8, "3 m/s", 1560, 870, 120, 64)


# ---------------- questão 3 ----------------
def cordas(c, t, t0, y, lam1, lam2, xm=1380, x0=960, x1=1820):
    """corda grossa (à esquerda) emendada na fina; λ maior na fina"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return []
    M.line(c, x0, y, xm, y, TINTA, 0.25 * q, 22)
    M.line(c, xm, y, x1, y, TINTA, 0.25 * q, 6)
    M.line(c, xm, y - 110, xm, y + 110, TINTA2, 0.6 * q, 3, dash=E.TRACO)
    F.onda(c, t, t0, x0, xm, y, 60, lam1, d=0.8, eixo=False, largura=11)
    F.onda(c, t, t0 + 0.6, xm, x1, y, 60, lam2, d=0.8, eixo=False, largura=5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (centro(c, "grossa", (x0 + xm) / 2, y + 140, 48, "i", TINTA2, a),
                                           centro(c, "fina", (xm + x1) / 2, y + 140, 48, "i", TINTA2, a)))


def b_q3(c, t, C, b):
    if t < C["s09"]:
        titulo_q(c, t, C["s08"], 3)
        E.frase(c, t, C["s08.a"], [("grossa", "i", 66), ("→", "g", 66, TINTA2), ("fina:", "i", 66), ("v", "g", 66, COR), ("×2", "g", 66, COR)], XE, 330, passo=0.12)
        E.frase(c, t, C["s08.b"], [("f", "g", 66, COR), ("=", "g", 66, TINTA2), ("10", "g", 66), ("Hz", "b", 48, F.UNID)], XE, 450, passo=0.12)
        E.frase(c, t, C["s08.b"] + 1.4, [("λ", "g", 66, COR), ("=", "g", 66, TINTA2), ("40", "g", 66), ("cm", "b", 48, F.UNID)], XE, 560, passo=0.12)
        E.frase(c, t, C["s08.c"], ps("e na", "i", 76) + [("fina?", "g", 76, COR)], XE, 720, passo=0.12)
        if t < C["s08.d"]:
            cordas(c, t, C["s08.a"], 520, 120, 240)
        else:
            E.relogio(c, t, C["s08.d"], cx=1460, cy=440, r=200)
        return
    E.frase(c, t, C["s09"], [("resposta", "i", 70, COR)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("trocou de meio:", "i", 66) + [("refração", "g", 66, COR)], XE, 320, passo=0.12)
    E.frase(c, t, C["s09.b"], [("f", "g", 80, COR), ("=", "g", 80, TINTA2), ("10", "g", 80), ("Hz", "b", 58, F.UNID)], XE, 470, passo=0.12)
    pilula(c, t, C["s09.b"] + 0.6, "fica", XE + 560, 445, 46, CERTO)
    E.frase(c, t, C["s09.c"], [("v", "g", 80, COR), ("×2", "g", 80), ("→", "g", 80, TINTA2), ("λ", "g", 80, COR), ("×2", "g", 80), ("=", "g", 80, TINTA2), ("80", "g", 80, CERTO),
                               ("cm", "b", 58, F.UNID)], XE, 620, passo=0.12)
    conta(c, t, [(C["s09.d"], "0,4 · 10 = 4 m/s", TINTA), (C["s09.d"] + 2.2, "0,8 · 10 = 8 m/s", TINTA)], XE, 820, 120, 72)
    E.foco(c, t, C["s09.d"] + 3.4, 0.4, lambda a: E.pilula(c, "o dobro", XE + 820, 920, 52, "g", fundo=CERTO, a=a, cor=BR))
    cordas(c, t, C["s09"], 470, 120, 240, xm=1450, x0=1100, x1=1820)


# ---------------- questão 4 ----------------
SIT = (("morcego e o eco", "reflexão"), ("rádio atrás do morro", "difração"), ("onda na parte rasa", "refração"))


def b_q4(c, t, C, b):
    if t < C["s11"]:
        titulo_q(c, t, C["s10"], 4)
        E.frase(c, t, C["s10"] + 0.8, ps("diga o fenômeno", "i", 64, TINTA2), XE + 480, 192, passo=0.1)
        for i, (k, (s, _)) in enumerate(zip(("s10.a", "s10.b", "s10.c"), SIT)):
            y = 380 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 70)], XE + 110, y)
        if t >= C["s10.d"]:
            E.relogio(c, t, C["s10.d"], cx=1460, cy=440, r=200)
        return
    E.frase(c, t, C["s11"], [("resposta", "i", 70, COR)], XE, 190)
    for i, (k, (s, r_)) in enumerate(zip(("s11.a", "s11.b", "s11.c"), SIT)):
        y = 380 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "i", 64)], XE + 110, y)
        E.foco(c, t, C[k] + 0.5, 0.4, lambda a, y=y: F.seta(c, 1000, y - 20, 1140, y - 20, TINTA2, a, 6))
        E.frase(c, t, C[k] + 0.6, [(r_, "g", 76, COR)], 1180, y)
    E.foco(c, t, C["s11.b"] + 1.4, 0.4, lambda a: E.escreve(c, "λ de metros a centenas de metros", XE + 110, 640, 44, "b", TINTA2, a))


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    S1, S2, P = (1080, 380), (1000, 900), (1680, 520)
    def tanque(t0):
        for k, (S, cor) in enumerate(((S1, E.COR), (S2, F.NEG))):
            E.foco(c, t, t0 + 0.2 * k, 0.4, lambda a, S=S, cor=cor: E.bola(c, *S, 22, cor, a))
            for j in range(4):
                r = ((t - t0) * 60 + j * 70) % 280 + 30
                if t >= t0:
                    c.drawCircle(*S, r, M.paint(cor, 0.5 * (1 - r / 310) * ep(t, t0, 0.5), stroke=4))
    if t < C["s13"]:
        titulo_q(c, t, C["s12"], 5)
        E.frase(c, t, C["s12.a"], ps("duas fontes juntas,", "i", 64) + [("λ", "g", 64, COR), ("=", "g", 64, TINTA2), ("4", "g", 64), ("cm", "b", 46, F.UNID)], XE, 330, passo=0.1)
        E.frase(c, t, C["s12.b"], [("P:", "g", 66), ("20", "g", 66, E.COR), ("e", "i", 66), ("26", "g", 66, F.NEG), ("cm", "b", 48, F.UNID)], XE, 460, passo=0.12)
        E.frase(c, t, C["s12.c"], ps("balança muito ou", "i", 66) + [("fica parada?", "g", 66, COR)], XE, 620, passo=0.1)
        if t < C["s12.d"]:
            tanque(C["s12.a"])
            if t >= C["s12.b"]:
                q = ep(t, C["s12.b"], 0.6)
                M.line(c, *S1, *P, E.COR, q, 4, dash=E.TRACO)
                M.line(c, *S2, *P, F.NEG, q, 4, dash=E.TRACO)
                E.foco(c, t, C["s12.b"], 0.4, lambda a: (E.bola(c, *P, 20, TINTA, a), E.escreve(c, "P", P[0] + 30, P[1] + 18, 56, "g", TINTA, a),
                                                         E.escreve(c, "20", 1360, 410, 52, "g", E.COR, a), E.escreve(c, "26", 1300, 770, 52, "g", F.NEG, a)))
        else:
            E.relogio(c, t, C["s12.d"], cx=1460, cy=440, r=200)
        return
    E.frase(c, t, C["s13"], [("resposta", "i", 70, COR)], XE, 190)
    conta(c, t, [(C["s13.a"], "26 − 20 = 6 cm"), (C["s13.b"], "f{λ}{2} = 2 cm"), (C["s13.c"], "6 ÷ 2 = 3")], XE, 360, 170, 96)
    pilula(c, t, C["s13.c"] + 1.0, "ímpar", XE + 640, 680, 60, ERRADO)
    E.frase(c, t, C["s13.d"], [("destrutiva:", "g", 76, COR), ("quase", "i", 76), ("parada", "i", 76)], XE, 900, passo=0.12)
    # crista + vale em P: soma quase zero
    yb = 470
    senoide(c, t, C["s13.a"], 1180, 1800, yb - 130, 50, 200, 0.0, E.COR)
    senoide(c, t, C["s13.a"] + 0.4, 1180, 1800, yb, 50, 200, math.pi, F.NEG)
    E.foco(c, t, C["s13.a"] + 0.2, 0.4, lambda a: (E.escreve(c, "crista", 1060, yb - 160, 40, "i", TINTA2, a), E.escreve(c, "vale", 1080, yb + 30, 40, "i", TINTA2, a)))
    if t >= C["s13.d"]:
        q = ep(t, C["s13.d"], 0.6)
        M.line(c, 1180, yb + 160, lerp(1180, 1800, q), yb + 160, TINTA, 1.0, 7)
        E.foco(c, t, C["s13.d"] + 0.4, 0.4, lambda a: centro(c, "soma ≈ 0", 1490, yb + 250, 56, "g", TINTA, a))


def senoide(c, t, t0, x0, x1, y, A, lam, fase, cor, d=0.8, largura=6):
    """senoide parada com fase escolhida (π = começa invertida: vale onde a outra tem crista)"""
    if t < t0:
        return
    n = 120
    pts = [(x0 + (x1 - x0) * i / n, y - A * math.cos(2 * math.pi * (x1 - x0) * i / n / lam + fase)) for i in range(n + 1)]
    F.poli(c, pts, ease_io(prog(t, t0, d)), cor, 1.0, largura)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s14"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s1, s2) in enumerate((("s14.a", "conta:", "v = λ · f, com f da fonte"), ("s14.b", "fenômeno:", "o que a onda fez"))):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 76)], 400, y)
            E.formula_em(c, t, C[k] + 0.5, s2, 900, y, 72, "g", COR)
    E.saida(c, t, C["s15"] - 0.1, resumo)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s15.c"], [("o", "i", 110), ("som", "g", 130, COR)], XE, 420)
    for i, (s, lam, A) in enumerate((("grave", 260, 50), ("agudo", 110, 50), ("forte", 180, 90), ("fraco", 180, 30))):
        y = 560 + i * 120
        E.foco(c, t, C["s15.d"] + 0.4 * i, 0.4, lambda a, s=s, y=y: E.escreve(c, s, XE, y + 18, 54, "g", TINTA, a))
        F.onda(c, t, C["s15.d"] + 0.4 * i, XE + 230, 1150, y, A * 0.55, lam, d=0.6, eixo=False, largura=5)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s15.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s15.e"] + 0.2, 0.4))
    E.frase(c, t, C["s15.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
