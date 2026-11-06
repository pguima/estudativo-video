"""Visual — Estudativo · MAT-NUM-004: subtrair de cabeça e com a conta armada.
Identidade em _ferramentas/editorial.py. Toda conta armada certa passa por E.armada (marcas = empréstimo: 0 → 10 → 9 na mesma casa).
A conta errada de 475 é desenhada à mão, porque E.armada não aceita resultado errado."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-004_subtrair_cabeca_conta_armada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cabeca", "emprestar", "zero", "atalho", "questao", "fim"))
BR = "#FFFFFF"
XV, Y0, ST = 750, 370, 150
XP = 1360  # centro do painel da direita


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def entre(a, b, f):
    """instante proporcional entre dois cues: sobrevive à troca do tempo provisório pela voz real"""
    return a + (b - a) * f


# ---------------- peças locais ----------------
def nota(c, cx, cy, w, s, a=1.0, cor=None, giro=0.0):
    """nota de dinheiro didática: retângulo com o valor, sem imitar cédula real"""
    if a <= 0:
        return
    cor = cor or E.COR
    h = w * 0.5
    c.save(); c.translate(cx, cy); c.rotate(giro)
    sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.22 * a))
    sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, max(3, w * 0.03)))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + 3, -h / 2 + 7, w, h), w * 0.04, w * 0.04), sombra)
    M.rrect(c, -w / 2, -h / 2, w, h, w * 0.04, cor, a)
    m = w * 0.045
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 + m, -h / 2 + m, w - 2 * m, h - 2 * m), w * 0.025, w * 0.025), M.paint(E.SOBRE, 0.45 * a, stroke=max(2, w * 0.008)))
    size = h * 0.5
    E.centro(c, "R$ " + s, 0, size * 0.36, size, "g", E.SOBRE, a)
    c.restore()


def conta(c, t, s, x, y, t0, cor=TINTA, size=92, align="center"):
    """uma linha de conta que entra de uma vez, com a cor pedida"""
    w = E.larg(s, "g", size)
    xx = x - w / 2 if align == "center" else x
    E.foco(c, t, t0, 0.45, lambda a: E.escreve(c, s, xx, y, size, "g", cor, a))


def faixa(c, x, y, w, h, a):
    M.rrect(c, x, y, w, h, 18, E.COR, 0.08 * a)


def banda(c, t, x, t0, t1, nome=""):
    """a coluna da vez, com o nome da casa em cima"""
    q = ep(t, t0, 0.3) * (1 - ep(t, t1 - 0.25, 0.25))
    if q > 0:
        faixa(c, x - 74, 90, 148, 690, q)
        E.centro(c, nome, x, 140, 46, "i", COR, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta_errada():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.centro(c, "503 − 178", W / 2, 400, 210, "g", TINTA, a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.centro(c, "= 475", W / 2, 640, 210, "g", ERRADO, a))
        E.frase(c, t, C["s01.c"], [("o", "i", 100), ("erro", "g", 96, ERRADO), ("mais", "g", 96, ERRADO), ("comum", "g", 96, ERRADO), ("da", "i", 100), ("subtração", "i", 100)], W / 2, 880, "center", passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, conta_errada)

    if t >= C["s02"]:
        a_, b_, c_ = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, c_ - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, c_ - 0.2, 0.7))), blur=0)
        E.frase(c, t, a_, [("até", "i", 92), ("o", "i", 92), ("fim", "i", 92), ("desta", "i", 92), ("aula", "i", 92)], XE, 330)
        E.frase(c, t, entre(a_, b_, 0.3), [("você", "i", 92), ("subtrai", "g", 116, COR)], XE, 490)
        E.frase(c, t, entre(a_, b_, 0.55), [("até", "i", 92), ("com", "i", 92), ("zero", "g", 92), ("no", "i", 92), ("caminho", "i", 92)], XE, 610, passo=0.12)
        E.frase(c, t, b_ - 0.3, [("confere", "g", 92, COR), ("com", "i", 92), ("uma", "i", 92), ("soma", "g", 92, COR)], XE, 750, passo=0.12)
        E.foco(c, t, c_ + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1270, 505, 88, "g", E.SOBRE, a),
                                               E.escreve(c, "de prova", 1300, 595, 88, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, fim = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.end"]
    E.frase(c, t, a_, [("você", "i", 88), ("só", "i", 88), ("precisa", "i", 88), ("de", "i", 88), ("uma", "g", 84, COR), ("coisa", "g", 84, COR)], W / 2, 170, "center", passo=0.1)
    E.frase(c, t, b_, [("somar", "i", 96), ("com", "i", 96), ("a", "i", 96), ("conta", "g", 92), ("armada", "g", 92)], W / 2, 300, "center", passo=0.12)
    ti = entre(b_, c_, 0.45)
    for i in range(10):
        k = ease_back(prog(t, ti + i * 0.05, 0.4))
        if k > 0:
            E.moeda(c, 380 + (i % 5) * 112, 480 + (i // 5) * 112, 50 * k, "1", M.clamp(k * 2))
    E.foco(c, t, ti + 0.7, 0.5, lambda a: nota(c, 1450, 535, 380, "10", a))
    # a seta da troca: primeiro para a nota; depois vira ao contrário
    p = ep(t, ti + 0.4, 0.4)
    vira = ease_io(prog(t, c_, 0.6))
    if p > 0:
        x0, x1 = lerp(1000, 1210, vira), lerp(1210, 1000, vira)
        M.arrow(c, x0, 535, x1, 535, E.COR if vira > 0.5 else TINTA, p, 8, 28, p)
    E.frase(c, t, c_, [("hoje,", "i", 96), ("a", "i", 96), ("troca", "i", 96), ("é", "i", 96), ("ao", "g", 92, COR), ("contrário", "g", 92, COR)], W / 2, 790, "center", passo=0.12)
    E.frase(c, t, entre(c_, fim, 0.55), [("se", "i", 66, TINTA2), ("faltar,", "i", 66, TINTA2), ("procure", "i", 66, TINTA2), ("a", "i", 66, TINTA2), ("aula", "i", 66, TINTA2), ("no", "i", 66, TINTA2), ("canal", "i", 66, TINTA2)], W / 2, 920, "center", passo=0.08)


# ---------------- de cabeça ----------------
def moedas_treze(c, t, ta, te, tf):
    """treze moedas: dez no quadro, três fora. As três saem em te; duas do quadro saem em tf"""
    passo_, r, x0, y0 = 124, 54, 300, 330
    pos = [(x0 + (i % 5) * passo_, y0 + (i // 5) * passo_) for i in range(10)] + [(1040 + i * passo_, y0) for i in range(3)]
    M.rrect(c, x0 - 72, y0 - 72, 5 * passo_ + 20, 2 * passo_ + 20, 22, E.VAZIO, ep(t, ta, 0.4))
    for i, (x, y) in enumerate(pos):
        k = ease_back(prog(t, ta + 0.04 * i, 0.4))
        if k <= 0:
            continue
        sai = 0.0
        if i >= 10:
            sai = ease_io(prog(t, te + (i - 10) * 0.14, 0.6))
        elif i >= 8:
            sai = ease_io(prog(t, tf + (i - 8) * 0.14, 0.6))
        if sai < 1:
            E.moeda(c, x + sai * 130, y - sai * 190, r * k * (1 - 0.35 * sai), "1", M.clamp(k * 2) * (1 - sai), cor=ERRADO if sai > 0 else None)


def b_cabeca(c, t, C, b):
    def tirar():
        a_, b_, c_, d_, e_, f_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"], C["s04.f"]
        E.frase(c, t, a_, [("subtrair", "i", 112), ("é", "i", 112), ("tirar", "g", 108, COR)], W / 2, 160, "center", passo=0.12)
        moedas_treze(c, t, b_, e_ - 0.2, f_ - 0.2)
        conta(c, t, "13 − 5", 560, 720, c_, TINTA, 104)
        conta(c, t, "5 = 3 + 2", 1300, 720, d_, TINTA, 104)
        conta(c, t, "13 − 3 = 10", 560, 880, e_, TINTA, 104)
        conta(c, t, "10 − 2 = 8", 1300, 880, f_, COR, 120)
    E.saida(c, t, C["s05"] - 0.1, tirar)
    if t < C["s05"]:
        return
    a_, b_, c_, fim = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.end"]
    E.frase(c, t, C["s05"] + 0.1, [("como", "i", 88), ("saber", "i", 88), ("se", "i", 88), ("está", "i", 88), ("certo?", "i", 88)], W / 2, 170, "center", passo=0.1)
    E.frase(c, t, a_, [("some", "i", 96), ("o", "i", 96), ("que", "i", 96), ("sobrou", "g", 92, COR), ("com", "i", 96), ("o", "i", 96), ("que", "i", 96), ("tirou", "g", 92, COR)], W / 2, 310, "center", passo=0.1)
    E.foco(c, t, b_, 0.5, lambda a: E.centro(c, "8 + 5 = 13", 880, 580, 190, "g", TINTA, a))
    k = ease_back(prog(t, c_, 0.5))
    E.selo(c, 1500, 515, 92 * k, True)
    E.frase(c, t, entre(c_, fim, 0.3), [("o", "i", 80), ("que", "i", 80), ("sobrou", "g", 76), ("+", "g", 76), ("o", "i", 80), ("que", "i", 80), ("saiu", "g", 76), ("=", "g", 76), ("tudo", "g", 76, COR), ("o", "i", 80), ("que", "i", 80), ("você", "i", 80), ("tinha", "i", 80)], W / 2, 830, "center", passo=0.08)


# ---------------- pedir emprestado ----------------
def b_emprestar(c, t, C, b):
    xs = E._centros("52", XV, ST)
    banda(c, t, xs[1], C["s06.d"], C["s08.b"], "unidade")
    banda(c, t, xs[0], C["s08.b"], C["s08.c"], "dezena")
    E.armada(c, t, ["52", "27"], "−", "25", (C["s06.c"], C["s06.c"] + 0.4), (C["s08.a"], C["s08.b"]), XV, Y0, ST,
             marcas=[(0, 0, "4", C["s07.c"]), (0, 1, "12", C["s07.d"])])

    def inicio():
        a_, b_, d_ = C["s06.a"], C["s06.b"], C["s06.d"]
        E.frase(c, t, a_, [("casa", "i", 84), ("embaixo", "i", 84), ("de", "i", 84), ("casa", "i", 84)], XP, 230, "center", passo=0.1)
        E.frase(c, t, b_, [("da", "i", 84), ("direita", "g", 80, COR), ("para", "i", 84), ("a", "i", 84), ("esquerda", "g", 80, COR)], XP, 350, "center", passo=0.1)
        p = ep(t, b_ + 0.3, 0.6)
        if p > 0:
            M.arrow(c, 1660, 410, 1060, 410, E.COR, p, 6, 22, p)
        conta(c, t, "2 − 7", XP, 620, d_, ERRADO, 150)
        E.frase(c, t, entre(d_, C["s06.end"], 0.3), [("não", "g", 80, ERRADO), ("dá", "g", 80, ERRADO), ("para", "i", 84), ("tirar", "i", 84)], XP, 780, "center", passo=0.1)
    E.saida(c, t, C["s07"] - 0.1, inicio)

    def emprestimo():
        a_, b_, c_, d_, fim = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.end"]
        E.frase(c, t, a_, [("pede", "g", 88, COR), ("emprestado", "g", 88, COR)], XP, 210, "center", passo=0.1)
        E.frase(c, t, a_ + 0.5, [("ao", "i", 84), ("vizinho", "i", 84)], XP, 300, "center")
        E.foco(c, t, b_, 0.45, lambda q: nota(c, 1120, 450, 280, "10", q))
        p = ep(t, entre(b_, c_, 0.45), 0.4)
        if p > 0:
            M.arrow(c, 1280, 450, 1370, 450, TINTA, p, 6, 20, p)
        for i in range(10):
            k = ease_back(prog(t, entre(b_, c_, 0.5) + i * 0.04, 0.35))
            if k > 0:
                E.moeda(c, 1420 + (i % 5) * 72, 415 + (i // 5) * 72, 33 * k, "1", M.clamp(k * 2))
        conta(c, t, "5 vira 4", 1160, 640, c_, TINTA, 76)
        conta(c, t, "2 vira 12", 1570, 640, d_, COR, 76)
        E.frase(c, t, entre(d_, fim, 0.2), [("o", "i", 76), ("dinheiro", "i", 76), ("é", "i", 76), ("o", "i", 76), ("mesmo", "g", 72, CERTO)], XP, 770, "center", passo=0.1)
        E.frase(c, t, entre(d_, fim, 0.55), [("passa", "i", 62), ("de", "i", 62), ("nove", "i", 62), ("só", "g", 58), ("por", "g", 58), ("um", "g", 58), ("instante", "g", 58)], XP, 880, "center", passo=0.08)
    if C["s07"] <= t:
        E.saida(c, t, C["s08"] - 0.1, emprestimo)
    if t >= C["s08"]:
        conta(c, t, "12 − 7 = 5", XP, 300, C["s08.a"], TINTA, 110)
        conta(c, t, "4 − 2 = 2", XP, 450, C["s08.b"], TINTA, 110)
        E.foco(c, t, C["s08.c"], 0.5, lambda q: E.pilula(c, "25", XP, 660, 150, estilo="g", cor=E.SOBRE, a=q))


# ---------------- por cima do zero ----------------
def b_zero(c, t, C, b):
    xs = E._centros("503", XV, ST)
    banda(c, t, xs[2], C["s09.b"], C["s09.c"], "unidade")
    banda(c, t, xs[2], C["s12.a"], C["s12.b"], "unidade"); banda(c, t, xs[1], C["s12.b"], C["s12.c"], "dezena"); banda(c, t, xs[0], C["s12.c"], C["s12.d"], "centena")
    q = ep(t, C["s09.c"], 0.4) * (1 - ep(t, C["s10.a"], 0.4))
    if q > 0:
        E.caixa_pontilhada(c, xs[1] - 66, Y0 - 122, 132, 150, q, ERRADO, prog_=q)
    if t >= C["s10.a"]:
        E.saida(c, t, C["s11"], lambda: E.salto(c, t, C["s10.a"], xs[0], xs[2], 165, 62, cor=E.COR))
    E.armada(c, t, ["503", "178"], "−", "325", (C["s09.a"], C["s09.a"] + 0.5), (C["s12.a"], C["s12.b"], C["s12.c"]), XV, Y0, ST,
             marcas=[(0, 0, "4", C["s10.b"]), (0, 1, "10", C["s10.c"]), (0, 1, "9", C["s10.d"]), (0, 2, "13", C["s10.e"])])

    def inicio():
        E.frase(c, t, C["s09"] + 0.1, [("e", "i", 88), ("quando", "i", 88), ("o", "i", 88), ("vizinho", "i", 88)], XP, 220, "center", passo=0.1)
        E.frase(c, t, C["s09"] + 0.6, [("não", "g", 88, COR), ("tem", "g", 88, COR), ("nada?", "g", 88, COR)], XP, 320, "center", passo=0.1)
        conta(c, t, "3 − 8", XP, 560, C["s09.b"], ERRADO, 150)
        E.frase(c, t, C["s09.b"] + 0.4, [("não", "g", 76, ERRADO), ("dá", "g", 76, ERRADO)], XP, 680, "center")
        E.frase(c, t, C["s09.c"], [("e", "i", 88), ("o", "i", 88), ("vizinho", "i", 88), ("é", "i", 88), ("zero", "g", 84, ERRADO)], XP, 830, "center", passo=0.1)
    E.saida(c, t, C["s10"] - 0.1, inicio)

    def caminho():
        a_, b_, c_, d_, e_ = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
        E.frase(c, t, a_, [("o", "i", 76), ("empréstimo", "i", 76), ("vem", "i", 76), ("do", "i", 76), ("5,", "g", 76, COR)], XP, 190, "center", passo=0.1)
        E.frase(c, t, a_ + 0.6, [("por", "i", 76), ("cima", "i", 76), ("do", "i", 76), ("zero", "g", 72, COR)], XP, 280, "center", passo=0.1)
        ti = entre(a_, b_, 0.5)
        E.foco(c, t, ti, 0.45, lambda q: nota(c, 1120, 410, 240, "100", q, TINTA))
        E.foco(c, t, ti + 0.3, 0.45, lambda q: E.escreve(c, "dez notas de 10", 1270, 430, 64, "i", TINTA2, q))
        for s, y, ti, cor in (("5 vira 4", 570, b_, TINTA), ("0 vira 10", 680, c_, TINTA), ("10 vira 9", 790, d_, TINTA), ("3 vira 13", 900, e_, COR)):
            conta(c, t, s, XP, y, ti, cor, 88)
    if C["s10"] <= t:
        E.saida(c, t, C["s11"] - 0.1, caminho)

    def dinheiro():
        a_, b_, c_ = C["s11.a"], C["s11.b"], C["s11.c"]
        E.frase(c, t, C["s11"] + 0.1, [("confira", "i", 80), ("o", "i", 80), ("dinheiro", "g", 76, COR)], XP, 150, "center", passo=0.1)
        for i in range(4):
            E.foco(c, t, a_ + i * 0.09, 0.35, lambda q, i=i: nota(c, 1080 + i * 36, 290, 240, "100", q, TINTA), sobe=-10)
        E.foco(c, t, a_ + 0.4, 0.4, lambda q: E.escreve(c, "R$ 400", 1410, 322, 96, "g", TINTA, q))
        for i in range(9):
            E.foco(c, t, b_ + i * 0.07, 0.35, lambda q, i=i: nota(c, 1040 + i * 26, 490, 240, "10", q), sobe=-10)
        E.foco(c, t, b_ + 0.5, 0.4, lambda q: E.escreve(c, "R$ 90", 1410, 522, 96, "g", TINTA, q))
        for i in range(13):
            k = ease_back(prog(t, c_ + i * 0.05, 0.35))
            if k > 0:
                E.moeda(c, 950 + (i % 7) * 62, 660 + (i // 7) * 62, 29 * k, "1", M.clamp(k * 2))
        E.foco(c, t, c_ + 0.5, 0.4, lambda q: E.escreve(c, "R$ 13", 1410, 702, 96, "g", TINTA, q))
        E.frase(c, t, entre(c_, C["s11.end"], 0.5), [("continua", "i", 84), ("sendo", "i", 84), ("503", "g", 88, CERTO)], XP, 890, "center", passo=0.1)
    if C["s11"] <= t:
        E.saida(c, t, C["s12"] - 0.1, dinheiro)

    def conta_final():
        conta(c, t, "13 − 8 = 5", XP, 270, C["s12.a"], TINTA, 104)
        conta(c, t, "9 − 7 = 2", XP, 410, C["s12.b"], TINTA, 104)
        conta(c, t, "4 − 1 = 3", XP, 550, C["s12.c"], TINTA, 104)
        E.foco(c, t, C["s12.d"], 0.5, lambda q: E.pilula(c, "325", XP, 750, 130, estilo="g", cor=E.SOBRE, a=q))
    if C["s12"] <= t:
        E.saida(c, t, C["s13"] - 0.1, conta_final)
    if t >= C["s13"]:
        a_, b_ = C["s13.a"], C["s13.b"]
        E.frase(c, t, C["s13"] + 0.1, [("confira", "i", 84), ("com", "i", 84), ("uma", "i", 84), ("soma", "g", 80, COR)], XP, 170, "center", passo=0.1)
        E.armada(c, t, ["325", "178"], "+", "503", (a_, a_ + 0.5), (b_, b_ + 0.15, b_ + 0.3), 1560, 340, 110,
                 vai=[(1, "1", entre(a_, b_, 0.65)), (2, "1", entre(a_, b_, 0.85))])
        k = ease_back(prog(t, b_ + 0.7, 0.5))
        E.selo(c, XP, 860, 74 * k, True)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    s, xv, y0, dy = 140, 640, 370, 170
    t0 = C["s14"] + 0.1
    xs = E._centros("503", xv, s)
    E.frase(c, t, a_, [("a", "i", 96), ("pessoa", "i", 96), ("inverte", "g", 96, ERRADO)], W / 2, 150, "center", passo=0.1)
    E.foco(c, t, t0, 0.45, lambda q: E.numero(c, "503", xv, y0, s, "g", TINTA, q))
    E.foco(c, t, t0 + 0.2, 0.45, lambda q: (E.numero(c, "178", xv, y0 + dy, s, "g", TINTA, q), E.centro(c, "−", xs[0] - 150, y0 + dy, s, "g", TINTA, q)))
    if t >= t0 + 0.3:
        M.line(c, xs[0] - 200, y0 + dy + 44, xv + 40, y0 + dy + 44, TINTA, 1.0, 6, progress=ep(t, t0 + 0.3, 0.5))
    E.foco(c, t, t0 + 0.5, 0.45, lambda q: E.numero(c, "475", xv, y0 + 2 * dy + 20, s, "g", ERRADO, q))
    # a seta sobe: é a conta feita de baixo para cima
    p = ep(t, b_, 0.5)
    if p > 0:
        M.arrow(c, xs[2] + 66, y0 + dy - 40, xs[2] + 66, y0 - 60, ERRADO, p, 6, 20, p)

    def contas():
        conta(c, t, "8 − 3", 1340, 330, b_, ERRADO, 130)
        conta(c, t, "7 − 0", 1340, 480, entre(b_, c_, 0.3), ERRADO, 130)
        E.frase(c, t, entre(b_, c_, 0.6), [("o", "i", 84), ("que", "i", 84), ("sai", "i", 84), ("é", "i", 84), ("sempre", "i", 84), ("o", "i", 84), ("de", "g", 80, COR), ("baixo", "g", 80, COR)], 1340, 660, "center", passo=0.09)
    E.saida(c, t, c_ - 0.1, contas)
    if t >= c_:
        E.armada(c, t, ["475", "178"], "+", "653", (c_, c_ + 0.3), (d_, d_ + 0.15, d_ + 0.3), 1500, 370, 120,
                 vai=[(1, "1", d_ - 0.3), (2, "1", d_ - 0.1)], cor_res=ERRADO)
        E.frase(c, t, e_, [("não", "g", 88, ERRADO), ("voltou", "g", 88, ERRADO), ("ao", "i", 92), ("começo", "i", 92)], 1340, 880, "center", passo=0.12)
        k = ease_back(prog(t, e_ + 0.5, 0.5))
        E.selo(c, 1710, 660, 70 * k, False)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def redondo():
        a_, b_, c_, d_, e_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]
        E.frase(c, t, a_, [("deixe", "g", 88, BR), ("redondo", "g", 88, CLARO), ("o", "i", 92, CLARO), ("número", "i", 92, CLARO), ("de", "i", 92, CLARO), ("baixo", "i", 92, CLARO)], W / 2, 150, "center", passo=0.12)
        E.expressao(c, t, [("403 − 198", "198", c_), ("405 − 200", None), ("205", None)], (d_, e_), 580, 400, 150, empilha=210, escuro=True, t0=b_)
        E.foco(c, t, c_, 0.45, lambda q: E.centro(c, "o mesmo tanto", 1370, 350, 84, "i", CLARO, q))
        E.foco(c, t, c_ + 0.5, 0.45, lambda q: E.centro(c, "+ 2 em cima", 1370, 480, 92, "g", BR, q))
        E.foco(c, t, c_ + 0.8, 0.45, lambda q: E.centro(c, "+ 2 embaixo", 1370, 600, 92, "g", BR, q))
        k = ease_back(prog(t, e_, 0.5))
        E.selo(c, 860, 775, 66 * k, True)
    E.saida(c, t, C["s16"] - 0.1, redondo)
    if t < C["s16"]:
        return

    a_, b_, c_, d_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, a_, [("a", "i", 92, CLARO), ("distância", "g", 88, BR), ("entre", "i", 92, CLARO), ("os", "i", 92, CLARO), ("números", "i", 92, CLARO), ("não", "g", 88, BR), ("muda", "g", 88, BR)], W / 2, 170, "center", passo=0.1)
    # duas idades andando juntas: a régua entre elas não muda
    y = 480
    if t >= b_:
        p = ep(t, b_, 0.5)
        M.line(c, 280, y, 1640, y, CLARO, p * 0.6, 4)
        q = ease_io(prog(t, entre(b_, c_, 0.45), 1.2))
        x1, x2 = 560 + 240 * q, 1060 + 240 * q
        for x in (x1, x2):
            k = ease_back(prog(t, b_ + 0.2, 0.5))
            if k > 0:
                E.bola(c, x, y, 46 * k)
        E.chave(c, x1, x2, y - 66, CLARO, ep(t, b_ + 0.4, 0.4), h=-30, largura=6)
        E.foco(c, t, b_ + 0.5, 0.4, lambda a: E.centro(c, "a diferença", (x1 + x2) / 2, y - 120, 72, "g", BR, a))
        E.foco(c, t, b_ + 0.3, 0.4, lambda a: E.centro(c, "hoje", 560 + 250, y + 110, 72, "i", CLARO, a * (1 - q)))
        E.foco(c, t, entre(b_, c_, 0.55), 0.4, lambda a: E.centro(c, "daqui a 2 anos", 1050, y + 110, 72, "i", CLARO, a))
    E.frase(c, t, c_, [("não", "g", 80, ERRADO), ("compensa", "g", 80, ERRADO), ("longe", "i", 88, BR), ("de", "i", 88, BR), ("um", "i", 88, BR), ("redondo", "i", 88, BR)], W / 2, 790, "center", passo=0.1)
    E.frase(c, t, d_, [("arme", "g", 100, CLARO), ("a", "g", 100, CLARO), ("conta", "g", 100, CLARO)], W / 2, 920, "center", passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.linha(c, t, [("na", "i", 100, TINTA2, C["s17.a"] - 0.5), ("conta:", "i", 100, TINTA2, C["s17.a"] - 0.4), ("R$ 705", "g", 116, TINTA, C["s17.a"])], XE, 370)
    E.linha(c, t, [("boleto:", "i", 100, TINTA2, C["s17.b"] - 0.4), ("R$ 268", "g", 116, TINTA, C["s17.b"])], XE, 530)
    E.frase(c, t, C["s17.c"], [("quanto", "i", 110), ("sobrou?", "g", 110, COR)], XE, 760)
    E.relogio(c, t, C["s18.a"], 1490, 400)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs = E._centros("705", XV, ST)
    t0 = C["s19"] + 0.1
    banda(c, t, xs[2], C["s19.a"], C["s19.b"], "unidade")
    banda(c, t, xs[2], C["s20.a"], C["s20.b"], "unidade"); banda(c, t, xs[1], C["s20.b"], C["s20.c"], "dezena"); banda(c, t, xs[0], C["s20.c"], C["s20.d"], "centena")
    E.armada(c, t, ["705", "268"], "−", "437", (t0, t0 + 0.2), (C["s20.a"], C["s20.b"], C["s20.c"]), XV, Y0, ST,
             marcas=[(0, 0, "6", C["s19.b"]), (0, 1, "10", C["s19.c"]), (0, 1, "9", C["s19.d"]), (0, 2, "15", C["s19.e"])])

    def troca():
        a_ = C["s19.a"]
        conta(c, t, "5 − 8", XP, 300, a_, ERRADO, 130)
        E.frase(c, t, a_ + 0.4, [("não", "g", 76, ERRADO), ("dá,", "g", 76, ERRADO), ("e", "i", 80), ("o", "i", 80), ("vizinho", "i", 80), ("é", "i", 80), ("zero", "g", 76)], XP, 420, "center", passo=0.09)
        for s, x, y, k, cor in (("7 vira 6", 1160, 600, "s19.b", TINTA), ("0 vira 10", 1560, 600, "s19.c", TINTA), ("10 vira 9", 1160, 760, "s19.d", TINTA), ("5 vira 15", 1560, 760, "s19.e", COR)):
            conta(c, t, s, x, y, C[k], cor, 80)
    E.saida(c, t, C["s20"] - 0.1, troca)
    if t >= C["s20"]:
        conta(c, t, "15 − 8 = 7", XP, 240, C["s20.a"], TINTA, 96)
        conta(c, t, "9 − 6 = 3", XP, 360, C["s20.b"], TINTA, 96)
        conta(c, t, "6 − 2 = 4", XP, 480, C["s20.c"], TINTA, 96)
        E.foco(c, t, C["s20.d"], 0.5, lambda q: E.pilula(c, "R$ 437", XP, 640, 100, estilo="g", fundo=CERTO, a=q))
        conta(c, t, "437 + 268", XP - 130, 870, C["s20.e"], TINTA, 96)
        conta(c, t, "= 705", XP + 270, 870, C["s20.f"], CERTO, 96)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21.a"], [("faltou,", "i", 110), ("peça", "g", 104, COR), ("ao", "g", 104, COR), ("vizinho", "g", 104, COR)], W / 2, 280, "center", passo=0.12)
        E.frase(c, t, C["s21.b"], [("vizinho", "i", 104), ("zero,", "i", 104), ("vem", "g", 96, COR), ("de", "g", 96, COR), ("mais", "g", 96, COR), ("longe", "g", 96, COR)], W / 2, 520, "center", passo=0.12)
        E.frase(c, t, C["s21.c"], [("no", "i", 110), ("fim,", "i", 110), ("confira", "g", 104, COR), ("com", "g", 104, COR), ("uma", "g", 104, COR), ("soma", "g", 104, COR)], W / 2, 760, "center", passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22.a"] - 1.2, [("próxima", "i", 84), ("aula:", "i", 84), ("multiplicação", "i", 84, COR)], XE, 270, passo=0.12)
    E.frase(c, t, C["s22.a"], [("vezes", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s22.a"] + 0.5, [("como", "i", 84), ("soma", "i", 84), ("repetida", "i", 84)], XE, 510, passo=0.1)
    E.frase(c, t, C["s22.b"], [("macetes", "g", 76)], XE, 630)
    E.frase(c, t, C["s22.b"] + 0.4, [("tabuadas", "i", 76), ("do", "i", 76), ("2,", "g", 72), ("5,", "g", 72), ("9", "g", 72), ("e", "i", 76), ("10", "g", 72)], XE, 720, passo=0.14)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1400, 400, 76, estilo="g", cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1530, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cabeca=b_cabeca, emprestar=b_emprestar, zero=b_zero, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
