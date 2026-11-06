"""Visual — Estudativo · MAT-DIV-006: problemas de MDC.
A peça central é a fita em escala real: 120 cm é sempre a mesma largura, e o corte mostra na hora se sobra ou não.
Depois o mesmo problema volta como bandejas, com as 15 bandejas enchendo na fala.
Todo instante vem de C[...]: o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, barra
import motor as M
import skia

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-006_problemas_de_mdc.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fitas", "bandejas", "atalho", "questao", "fim"))
BR = "#FFFFFF"

ESC = 1300 / 120  # px por cm: as duas fitas na mesma escala
assert 72 % 24 == 0 and 120 % 24 == 0 and 72 // 24 + 120 // 24 == 8
assert 2 * 2 * 2 * 3 == 24 and 3 * 5 == 15 and 30 // 15 == 2 and 45 // 15 == 3
assert 3 * 7 == 21 and 63 // 21 == 3 and 84 // 21 == 4


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


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def bola_duas(c, l1, l2, cx, cy, r, s1, s2, a=1.0, cor=None):
    """esfera com o número e a unidade embaixo"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, l1, cx, cy + s1 * 0.2, s1, "g", E.SOBRE, a)
    centro(c, l2, cx, cy + s1 * 0.2 + s2 * 1.05, s2, "i", E.SOBRE, a)


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.2):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


def relogio(c, t, t0, cx=1490, cy=340, r0=190):
    """relógio de pausa: enche em 3 segundos"""
    r = r0 * ease_back(prog(t, t0, 0.6))
    if r <= 0:
        return
    E.bola(c, cx, cy, r)
    f = M.clamp(prog(t, t0 + 0.8, 3.0))
    if f > 0:
        E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
    for dx in (-40, 40):
        M.rrect(c, cx + dx - 20, cy - 72, 40, 144, 11, E.SOBRE, ep(t, t0 + 0.2, 0.4))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + r0 + 104, 60, "i", TINTA, a))


def fita(c, y, cm, h, a=1.0, pedaco=None, pc=1.0, enche=1.0, x=XE):
    """fita em escala: pedaco = tamanho do corte em cm, pc = 0..1 desce as lâminas uma a uma, a sobra fica em vermelho"""
    if a <= 0:
        return
    w = cm * ESC
    cortes = []
    n = cm // pedaco if pedaco else 0
    if pedaco:
        for i in range(1, n + 1):
            if i * pedaco < cm:
                cortes.append((i * pedaco / cm, ease_io(M.clamp(pc * n - (i - 1)))))
    barra(c, x, y, w, h, 1.0, cortes, a, enche=enche, largura=6)
    if pedaco and cm % pedaco:  # o resto não vira pedaço
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
        c.save(); c.clipRRect(rr, True)
        c.drawRect(skia.Rect.MakeXYWH(x + n * pedaco * ESC, y, (cm % pedaco) * ESC, h), M.paint(ERRADO, a * M.clamp(pc * 2 - 1)))
        c.restore()
        c.drawRRect(rr, M.paint(TINTA, a, stroke=3))


def conta_pedacos(c, t, t0, y, h, cm, pedaco, size=64, passo=0.14, x=XE):
    """numera os pedaços, um a um, dentro da fita"""
    for i in range(cm // pedaco):
        s, cx = str(i + 1), x + (i + 0.5) * pedaco * ESC
        E.foco(c, t, t0 + i * passo, 0.3, lambda a, s=s, cx=cx: centro(c, s, cx, y + h / 2 + size * 0.36, size, "g", E.SOBRE, a), sobe=8, blur=8)


def fatores(c, t, n, fs, y, t0, t1, tc=None, comuns=(), s=100, xn=440, x0=630, dx=165):
    """n = a × b × c, fator a fator entre t0 e t1; em tc os fatores comuns ganham esfera e os outros ficam cinza"""
    E.foco(c, t, t0, 0.45, lambda a: (E.escreve(c, str(n), xn - E.larg(str(n), "g", s), y, s, "g", TINTA, a),
                                      centro(c, "=", xn + 75, y, round(s * 0.8), "g", TINTA2, a)))
    marcado = tc is not None and t >= tc
    for i, f in enumerate(fs):
        ti, cx = lerp(t0, t1, (i + 1) / len(fs)), x0 + i * dx
        if i:
            E.foco(c, t, ti - 0.1, 0.35, lambda a: centro(c, "×", cx - dx / 2, y, round(s * 0.6), "b", TINTA2, a), sobe=8)
        if tc is not None and i in comuns:
            r = s * 0.56 * ease_back(prog(t, tc + i * 0.1, 0.45))
            if r > 1:
                E.bola(c, cx, y - s * 0.36, r)
        na_bola = marcado and i in comuns
        cor, sz = (E.SOBRE, round(s * 0.8)) if na_bola else (CINZA if marcado else TINTA, s)
        E.foco(c, t, ti, 0.4, lambda a: centro(c, str(f), cx, y - s * 0.36 + sz * 0.36, sz, "g", cor, a), sobe=8)


def conta_comum(c, t, t0, fs, y, x=XE, s=92):
    """em comum: a × b"""
    partes = [("em", "i", 80, TINTA, t0 - 0.3), ("comum:", "i", 80, TINTA, t0 - 0.15)]
    for i, f in enumerate(fs):
        if i:
            partes.append(("×", "b", 64, TINTA2, t0 + i * 0.25 - 0.1))
        partes.append((str(f), "g", s, COR, t0 + i * 0.25))
    linha(c, t, partes, x, y)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def fitas():
        y1, y2, h = 280, 460, 130
        E.frase(c, t, C["s01"] + 0.3, ps("duas", "i", 90) + ps("fitas", "g", 84, COR), XE, 200)
        fita(c, y1, 72, h, ep(t, a_, 0.3), enche=ep(t, a_, 0.9))
        fita(c, y2, 120, h, ep(t, b_, 0.3), enche=ep(t, b_, 0.9))
        E.foco(c, t, a_ + 0.5, 0.45, lambda a: E.escreve(c, "72 cm", XE + 72 * ESC + 40, y1 + h / 2 + 28, 84, "g", TINTA, a))
        E.foco(c, t, b_ + 0.5, 0.45, lambda a: E.escreve(c, "120 cm", XE + 1300 + 30, y2 + h / 2 + 26, 72, "g", TINTA, a))
        E.frase(c, t, lerp(b_, c_, 0.3), ps("pedaços iguais,", "g", 62, COR) + ps("os maiores possíveis,", "i", 72) + ps("sem sobrar nada", "g", 62, COR), W / 2, 720, "center", 0.32)
        E.frase(c, t, c_, ps("quantos pedaços", "i", 130) + ps("saem?", "g", 120, COR), W / 2, 900, "center", 0.3)
    E.saida(c, t, C["s02"] - 0.1, fitas)

    if t >= C["s02"]:
        s0 = C["s02"]
        q = ease_back(prog(t, C["s02.b"] - 0.2, 0.7))
        if q > 0:
            E.bola(c, 1480, 540, 290 * q)
        E.frase(c, t, s0 + 0.35, ps("até o fim da aula", "i", 90), XE, 370)
        E.frase(c, t, s0 + 1.5, ps("você", "i", 124) + ps("resolve", "g", 124), XE, 530)
        E.frase(c, t, C["s02.a"], ps("sem", "i", 110) + ps("tentativa", "g", 100, COR), XE, 680, passo=0.3)
        E.frase(c, t, C["s02.a"] + 0.8, ps("e", "i", 110) + ps("erro", "g", 100, COR), XE, 810, passo=0.25)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 500, 84, "g", E.SOBRE, a),
                                                      centro(c, "de prova", 1480, 585, 84, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.35, ps("para acompanhar,"), XE, 310)
    E.frase(c, t, C["s03"] + 1.4, ps("você só precisa de"), XE, 420)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 730, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 710, 120, "i", TINTA, a))
    x, y, w = 900, 330, 840
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 236, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("Calcular o MDC", "g", 76, COR)], x + 44, y + 100)
    E.frase(c, t, C["s03.b"] + 0.3, [("de dois números", "i", 70)], x + 44, y + 184)
    E.cursor(c, x + w - 40, y + 190, ep(t, C["s03.b"] + 0.2, 0.4))
    E.frase(c, t, lerp(C["s03.b"], C["s03.end"], 0.6), ps("procure a aula no canal", "i", 62), x, 680, passo=0.14)


# ---------------- por que é MDC ----------------
def b_fitas(c, t, C, b):
    Y1, Y2, H_ = 300, 500, 120
    s4, s5 = C["s04"], C["s05"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    t12 = lerp(b5, c5, 0.5)  # "pedaços de doze?"

    def historia():
        fica(c, t, s4 + 0.35, C["s04.a"] - 0.3, ps("antes da conta,", "i", 96) + ps("entenda a história", "g", 88, COR), W / 2, 190, "center", 0.18)
        fica(c, t, C["s04.a"] - 0.1, s5 - 0.1, ps("o pedaço precisa", "i", 88) + ps("caber certinho", "g", 80, COR), W / 2, 190, "center", 0.2)
        # as fitas ficam: primeiro o teste com 30, depois com 12
        if t < t12:
            pc, ped = ep(t, a5, 0.7) * (1 - ep(t, t12 - 0.4, 0.35)), 30
        else:
            pc, ped = ep(t, t12, 0.9), 12
        fita(c, Y1, 72, H_, ep(t, s4 + 0.4, 0.5), ped, pc)
        fita(c, Y2, 120, H_, ep(t, s4 + 0.4, 0.5), 12 if t >= t12 else None, ep(t, t12, 0.9))
        E.foco(c, t, s4 + 0.5, 0.45, lambda a: (E.escreve(c, "72 cm", XE + 72 * ESC + 40, Y1 + H_ / 2 + 26, 76, "g", TINTA, a),
                                                E.escreve(c, "120 cm", XE + 1300 + 30, Y2 + H_ / 2 + 24, 70, "g", TINTA, a)))
        for k, y, wf in (("s04.a", Y1, 72), ("s04.b", Y2, 120)):  # "caber em 72", "e também em 120"
            q = ep(t, C[k], 0.5) * (1 - ep(t, s5 - 0.4, 0.3))
            E.caixa_pontilhada(c, XE - 14, y - 14, wf * ESC + 28, H_ + 28, q, prog_=q)
        if t >= t12:
            conta_pedacos(c, t, c5 - 0.1, Y1, H_, 72, 12, 52, 0.07)
            conta_pedacos(c, t, c5 + 0.2, Y2, H_, 120, 12, 52, 0.07)
        # caber certinho = divisor
        fica(c, t, C["s04.c"] - 0.5, s5 - 0.1, ps("caber certinho", "i", 104) + [("=", "g", 96, TINTA2)] + ps("ser", "i", 104) + ps("divisor", "g", 110, COR), W / 2, 830, "center", 0.2)
        # teste com 30
        E.saida(c, t, t12 - 0.2, lambda: (
            E.foco(c, t, s5 + 0.3, 0.45, lambda a: E.pilula(c, "pedaços de 30 cm?", W / 2, 170, 72, estilo="g", a=a)),
            E.foco(c, t, a5, 0.45, lambda a: E.escreve(c, "72 ÷ 30 = 2 e sobram 12", XE, 800, 76, "b", TINTA, a)),
            E.frase(c, t, b5, ps("não serve", "g", 112, ERRADO), XE, 930)), 0.3)
        # teste com 12
        if t >= t12:
            E.foco(c, t, t12, 0.45, lambda a: E.pilula(c, "pedaços de 12 cm?", W / 2, 170, 72, estilo="g", a=a))
            E.foco(c, t, c5, 0.45, lambda a: (E.escreve(c, "72 ÷ 12 = 6", XE, 790, 72, "b", CERTO, a),
                                              E.escreve(c, "120 ÷ 12 = 10", 640, 790, 72, "b", CERTO, a)))
            E.frase(c, t, c5 + 0.5, ps("serve nas duas", "g", 80, CERTO), 1190, 790, passo=0.2)
            E.frase(c, t, d5, ps("mas será que é", "i", 112) + ps("o maior?", "g", 104, COR), W / 2, 950, "center", 0.2)
    E.saida(c, t, C["s06"] - 0.1, historia)

    if t < C["s06"]:
        return
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    tam, X = 140, 870
    lin = ((400, "M", "áximo", b6), (620, "D", "ivisor", a6), (840, "C", "omum", a6 + 0.5))
    for y, l, resto, ti in lin:
        E.foco(c, t, ti, 0.5, lambda a: (E.escreve(c, l, XE, y, tam, "g", COR, a), E.escreve(c, resto, XE + E.larg(l, "g", tam) + 2, y, tam, "g", TINTA, a)))
    E.frase(c, t, a6 + 0.2, ps("cabe certinho", "i", 84), X, 600, passo=0.2)
    E.frase(c, t, a6 + 0.7, ps("nas duas medidas", "i", 84), X, 820, passo=0.2)
    E.frase(c, t, b6 + 0.2, ps("o maior possível", "i", 84), X, 380, passo=0.2)
    E.frase(c, t, c6, ps("isso é o", "i", 96) + ps("MDC", "g", 130, COR), W / 2, 200, "center", 0.2)


# ---------------- conta ----------------
def b_conta(c, t, C, b):
    a_, b_, c_, d_ = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]

    def contas():
        fatores(c, t, 72, (2, 2, 2, 3, 3), 310, a_, lerp(a_, b_, 0.85), c_, (0, 1, 2, 3))
        fatores(c, t, 120, (2, 2, 2, 3, 5), 490, b_, lerp(b_, c_, 0.85), c_, (0, 1, 2, 3))
        conta_comum(c, t, c_ + 0.3, (2, 2, 2, 3), 760)
        E.foco(c, t, d_, 0.5, lambda a: bola_duas(c, "24", "cm", 1540, 650, 200, 170, 76, a))
    E.saida(c, t, C["s08"] - 0.1, contas)

    if t < C["s08"]:
        return
    s0 = C["s08"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    linha(c, t, [(w, "i", 82, TINTA, s0 + 0.3 + i * 0.16) for i, w in enumerate("a pergunta não é o tamanho:".split())]
          + [("é", "i", 82, TINTA, a8 - 0.1), ("quantos", "g", 76, COR, a8), ("pedaços", "g", 76, COR, a8 + 0.3)], W / 2, 170, "center")
    y1, y2, h = 250, 520, 120
    fita(c, y1, 72, h, ep(t, s0 + 0.4, 0.5), 24, ep(t, b8, 0.7))
    fita(c, y2, 120, h, ep(t, s0 + 0.4, 0.5), 24, ep(t, c8, 0.7))
    conta_pedacos(c, t, b8 + 0.4, y1, h, 72, 24, 76, 0.25)
    conta_pedacos(c, t, c8 + 0.4, y2, h, 120, 24, 76, 0.2)
    E.foco(c, t, s0 + 0.6, 0.45, lambda a: E.escreve(c, "cada pedaço: 24 cm", XE + 72 * ESC + 50, y1 + h / 2 + 22, 62, "b", TINTA2, a))
    E.foco(c, t, b8 + 0.1, 0.45, lambda a: E.escreve(c, "72 ÷ 24 = 3 pedaços", XE, y1 + h + 92, 72, "b", TINTA, a))
    E.foco(c, t, c8 + 0.1, 0.45, lambda a: E.escreve(c, "120 ÷ 24 = 5 pedaços", XE, y2 + h + 92, 72, "b", TINTA, a))
    E.foco(c, t, d8, 0.5, lambda a: E.escreve(c, "3 + 5 =", 820, 945, 120, "g", TINTA, a))
    E.foco(c, t, d8 + 0.4, 0.5, lambda a: (num_bola(c, "8", 1320, 905, 110, 130, a), E.escreve(c, "pedaços", 1450, 945, 104, "i", COR, a)))


# ---------------- bandejas ----------------
def pao(c, x, y, r, a=1.0, k=1.0):
    """pão de queijo"""
    E.bola(c, x, y, r * k, a=a)


def coxinha(c, x, y, r, a=1.0, k=1.0):
    """coxinha: a gota de sempre"""
    if a <= 0 or k <= 0:
        return
    r *= k
    p = skia.Path()
    p.moveTo(x, y - 1.3 * r)
    p.cubicTo(x + 0.35 * r, y - 0.6 * r, x + 1.1 * r, y - 0.1 * r, x + r, y + 0.45 * r)
    p.cubicTo(x + 0.9 * r, y + 1.05 * r, x - 0.9 * r, y + 1.05 * r, x - r, y + 0.45 * r)
    p.cubicTo(x - 1.1 * r, y - 0.1 * r, x - 0.35 * r, y - 0.6 * r, x, y - 1.3 * r)
    c.drawPath(p, M.paint(TINTA, a))


def b_bandejas(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def mesa():
        E.frase(c, t, C["s09"] + 0.35, ps("o mesmo problema,", "i", 88) + ps("outra roupa", "g", 80, COR), W / 2, 170, "center", 0.18)
        E.frase(c, t, a9, ps("30", "g", 72, COR) + ps("pães de queijo", "i", 76), 210, 300, passo=0.2)
        E.frase(c, t, b9, ps("45", "g", 72) + ps("coxinhas", "i", 76), 860, 300, passo=0.2)
        for i in range(30):
            q = ease_back(prog(t, a9 + i * 0.03, 0.4))
            pao(c, 240 + (i % 6) * 76, 370 + (i // 6) * 66, 26, min(1.0, q * 2), q)
        for i in range(45):
            q = ease_back(prog(t, b9 + i * 0.022, 0.4))
            coxinha(c, 880 + (i % 9) * 76, 370 + (i // 9) * 66, 23, min(1.0, q * 2), q)
        E.frase(c, t, c9, ps("o maior número possível de", "i", 74) + ps("bandejas iguais", "g", 68, COR), W / 2, 800, "center", 0.15)
        E.frase(c, t, c9 + 1.2, ps("sem sobrar nada", "i", 84), W / 2, 910, "center", 0.2)
    E.saida(c, t, C["s10"] - 0.1, mesa)

    if C["s10"] <= t < C["s11"]:
        a_, b_, c_, d_ = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]

        def conta():
            s0 = C["s10"]
            linha(c, t, [(w, "i", 80, TINTA, s0 + 0.3 + i * 0.14) for i, w in enumerate("o número de bandejas precisa dividir".split())]
                  + [("30", "g", 84, COR, a_), ("e", "i", 80, TINTA, a_ + 0.2), ("45", "g", 84, COR, b_)], W / 2, 170, "center")
            E.frase(c, t, lerp(b_, c_, 0.25), ps("é divisor comum, e o maior:", "i", 76), XE, 300, passo=0.13)
            E.foco(c, t, c_, 0.45, lambda a: E.pilula(c, "MDC", 1150, 275, 76, estilo="g", a=a))
            tc = lerp(c_, d_, 0.72)
            fatores(c, t, 30, (2, 3, 5), 490, lerp(c_, d_, 0.08), lerp(c_, d_, 0.32), tc, (1, 2))
            fatores(c, t, 45, (3, 3, 5), 650, lerp(c_, d_, 0.36), lerp(c_, d_, 0.64), tc, (1, 2))
            conta_comum(c, t, lerp(c_, d_, 0.78), (3, 5), 860)
            E.foco(c, t, d_, 0.5, lambda a: bola_duas(c, "15", "bandejas", 1450, 570, 220, 170, 76, a))
        E.saida(c, t, C["s11"] - 0.1, conta)

    if C["s11"] <= t < C["s12"]:
        a_, b_ = C["s11.a"], C["s11.b"]

        def bandejas():
            E.frase(c, t, C["s11"] + 0.2, ps("em cada", "i", 88) + ps("bandeja", "g", 80, COR), W / 2, 170, "center")
            for k in range(15):
                x, y = 190 + (k % 5) * 310, 240 + (k // 5) * 158
                q = ep(t, C["s11"] + 0.2 + k * 0.03, 0.4)
                M.rrect(c, x, y, 280, 132, 18, "#FFFFFF", q, shadow=True)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 280, 132), 18, 18), M.paint(TINTA, q, stroke=3))
                for j in range(2):
                    z = ease_back(prog(t, a_ + 0.5 + k * 0.05, 0.35))
                    pao(c, x + 42 + j * 48, y + 66, 19, min(1.0, z * 2), z)
                for j in range(3):
                    z = ease_back(prog(t, b_ + 0.5 + k * 0.05, 0.35))
                    coxinha(c, x + 142 + j * 46, y + 68, 18, min(1.0, z * 2), z)
            E.foco(c, t, a_, 0.45, lambda a: E.escreve(c, "30 ÷ 15 = 2 pães", XE, 880, 72, "b", COR, a))
            E.foco(c, t, b_, 0.45, lambda a: E.escreve(c, "45 ÷ 15 = 3 coxinhas", 900, 880, 72, "b", TINTA, a))
        E.saida(c, t, C["s12"] - 0.1, bandejas)

    if t >= C["s12"]:
        s0 = C["s12"]
        E.frase(c, t, s0 + 0.35, ps("repare na", "i", 88) + ps("diferença", "g", 80, COR), W / 2, 180, "center")
        M.line(c, W / 2, 250, W / 2, 790, FIO, ep(t, C["s12.a"] - 0.2, 0.4), 3)

        def lado(cx, nome, n, l1, l2, t0):
            E.foco(c, t, t0, 0.5, lambda a: centro(c, nome, cx, 340, 96, "g", TINTA, a))
            E.foco(c, t, t0 + 0.2, 0.5, lambda a: num_bola(c, n, cx, 510, 110, 110, a))
            E.frase(c, t, t0 + 0.5, ps(l1, "i", 76), cx, 690, "center", 0.15)
            E.frase(c, t, t0 + 0.9, ps(l2, "g", 62, COR), cx, 780, "center", 0.15)
        lado(500, "Fitas", "24", "o MDC foi o", "tamanho do pedaço", C["s12.a"])
        lado(1420, "Bandejas", "15", "o MDC foi a", "quantidade de bandejas", C["s12.b"])
        E.frase(c, t, C["s12.c"], ps("o que esse número", "i", 96) + ps("significa", "g", 88, COR) + ps("na história?", "i", 96), W / 2, 930, "center", 0.17)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    linha(c, t, [("o", "i", 84, TINTA, C["s13"] + 0.35), ("erro", "g", 78, ERRADO, C["s13"] + 0.5), ("mais", "i", 84, TINTA, C["s13"] + 0.7),
                 ("comum", "i", 84, TINTA, C["s13"] + 0.9), ("é", "i", 84, TINTA, a_ - 0.1), ("parar", "g", 78, ERRADO, a_), ("no", "g", 78, ERRADO, a_ + 0.2),
                 ("MDC", "g", 78, ERRADO, a_ + 0.4)], W / 2, 180, "center")
    E.foco(c, t, b_, 0.5, lambda a: centro(c, "24", 480, 560, 300, "g", ERRADO, a))
    E.frase(c, t, b_ + 0.3, ps("a pessoa responde", "i", 66), 480, 300, "center", 0.15)
    tam = lerp(c_, d_, 0.55)  # "vinte e quatro é o tamanho"
    if t >= tam:
        E.risco(c, 280, 590, 680, 370, t, tam, largura=14)
    E.frase(c, t, tam, ps("24", "g", 76, ERRADO) + ps("é o tamanho", "i", 84), 480, 700, "center", 0.2)
    x, w = 900, 830
    p = ep(t, c_, 0.5)
    E.caixa_pontilhada(c, x, 280, w, 200, p, prog_=p)
    E.frase(c, t, c_ + 0.1, ps("a pergunta era", "i", 66), x + 44, 355, passo=0.14)
    E.frase(c, t, c_ + 0.4, ps("quantos pedaços?", "g", 78, COR), x + 44, 445, passo=0.2)
    E.frase(c, t, d_, ps("a resposta é", "i", 92), x + 20, 660, passo=0.16)
    E.foco(c, t, d_ + 0.4, 0.5, lambda a: num_bola(c, "8", 1540, 630, 120, 150, a, CERTO, BR))
    E.frase(c, t, e_, ps("antes de terminar,", "i", 88) + ps("releia", "g", 84, COR) + ps("o que foi pedido", "i", 88), W / 2, 900, "center", 0.17)
    E.cursor(c, 1640, 930, ep(t, e_ + 0.5, 0.4), TINTA)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def pista():
        s0 = C["s14"]
        E.frase(c, t, s0 + 0.35, ps("agora, o atalho", "i", 90, CLARO), W / 2, 200, "center")
        E.frase(c, t, s0 + 1.3, ps("uma", "i", 104, BR) + ps("pista", "g", 104, BR) + ps("no texto", "i", 104, BR), W / 2, 330, "center", 0.2)
        E.frase(c, t, C["s14.a"], ps("procure", "i", 88, CLARO) + ps("3 ideias", "g", 84, BR) + ps("juntas", "i", 88, CLARO), W / 2, 490, "center", 0.2)
        rot = (("partes iguais", "s14.b"), ("sem sobra", "s14.c"), ("o maior possível", "s14.d"))
        size, gap = 60, 44
        ws = [E.larg(s, "g", size) + size * 1.1 for s, _ in rot]
        x = W / 2 - (sum(ws) + 2 * gap) / 2
        for (s, k), w_ in zip(rot, ws):
            E.foco(c, t, C[k], 0.45, lambda a: E.pilula(c, s, x + w_ / 2, 650, size, estilo="g", fundo=E.COR, cor=BR, a=a))
            x += w_ + gap
        E.frase(c, t, C["s14.e"], ps("apareceu isso,", "i", 104, CLARO) + ps("é MDC", "g", 130, BR), W / 2, 870, "center", 0.25)
    E.saida(c, t, C["s15"] - 0.1, pista)

    def nome():
        s0 = C["s15"]
        E.frase(c, t, s0 + 0.35, ps("cada ideia é", "i", 90, CLARO) + ps("um pedaço do nome", "g", 84, BR), W / 2, 200, "center", 0.17)
        for y, k, l1, l2 in ((390, "s15.a", "sem sobra", "divisor"), (590, "s15.b", "igual para todos", "comum"), (790, "s15.c", "o maior possível", "máximo")):
            E.foco(c, t, C[k], 0.45, lambda a: E.escreve(c, l1, 960 - 130 - E.larg(l1, "i", 92), y, 92, "i", CLARO, a))
            if t >= C[k] + 0.3:
                p = ep(t, C[k] + 0.3, 0.45)
                M.arrow(c, 860, y - 30, 1040, y - 30, CLARO, p, 5, 16, p)
            E.foco(c, t, C[k] + 0.5, 0.45, lambda a: E.pilula(c, l2, 1340, y - 28, 84, estilo="g", fundo=E.COR, cor=BR, a=a))
    if t >= C["s15"]:
        E.saida(c, t, C["s16"] - 0.1, nome)

    if t >= C["s16"]:
        s0 = C["s16"]
        a_, b_, c_, d_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
        E.frase(c, t, s0 + 0.3, ps("quando", "i", 96, CLARO) + ps("não compensa?", "g", 90, BR), W / 2, 170, "center", 0.2)
        E.frase(c, t, a_, ps("o texto", "i", 80, CLARO) + ps("já dá o tamanho", "g", 72, BR) + ps("do pedaço?", "i", 80, CLARO), XE, 320, passo=0.17)
        E.frase(c, t, lerp(a_, b_, 0.6), ps("não tem MDC:", "i", 80, CLARO), XE, 425, passo=0.17)
        E.frase(c, t, b_, ps("é só dividir", "g", 78, BR), 660, 425, passo=0.18)
        M.line(c, XE, 500, 1750, 500, CLARO, 0.25 * ep(t, c_ - 0.3, 0.4), 2)
        E.frase(c, t, c_, ps("a palavra", "i", 80, CLARO) + ps("maior,", "g", 76, BR) + ps("sozinha, não prova nada", "i", 80, CLARO), XE, 600, passo=0.16)
        E.frase(c, t, d_, ps("confira se a história é de", "i", 72, CLARO) + ps("repartir em partes iguais", "g", 66, BR), XE, 705, passo=0.13)
        E.frase(c, t, lerp(d_, C["s16.end"], 0.45), ps("coisas que se", "i", 76, CLARO) + ps("repetem no tempo", "g", 70, BR) + ps("pedem outra conta:", "i", 76, CLARO), XE, 860, passo=0.15)
        E.frase(c, t, lerp(d_, C["s16.end"], 0.75), ps("assunto da próxima aula", "i", 76, CLARO), XE, 960, passo=0.15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    s0 = C["s17"]
    E.frase(c, t, s0 + 0.3, ps("hora de testar", "i", 76, COR), XE, 190)
    linha(c, t, [("63", "g", 110, COR, C["s17.a"]), ("sabonetes", "i", 96, TINTA, C["s17.a"] + 0.3)], XE, 340)
    linha(c, t, [("84", "g", 110, COR, C["s17.b"]), ("cremes", "i", 96, TINTA, C["s17.b"] + 0.3)], XE, 470)
    E.frase(c, t, C["s17.c"], ps("o maior número possível", "i", 76), XE, 610, passo=0.16)
    E.frase(c, t, C["s17.c"] + 1.1, ps("de", "i", 76) + ps("kits iguais,", "g", 70, COR) + ps("sem sobrar nada", "i", 76), XE, 710, passo=0.16)
    E.frase(c, t, C["s17.d"], ps("quantos", "i", 110) + ps("kits?", "g", 100, COR), XE, 860, passo=0.2)
    E.frase(c, t, C["s17.d"] + 0.8, ps("e o que vai em", "i", 88) + ps("cada um?", "g", 80, COR), XE, 970, passo=0.17)
    relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def kit(c, t, x, y, ts, tc):
    """o kit aberto: 3 sabonetes e 4 cremes"""
    q = ep(t, ts - 0.3, 0.4)
    M.rrect(c, x, y, 460, 180, 20, "#FFFFFF", q, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 460, 180), 20, 20), M.paint(TINTA, q, stroke=3))
    for i in range(3):
        z = ease_back(prog(t, ts + 0.3 + i * 0.15, 0.4))
        E.bola(c, x + 70 + i * 80, y + 58, 32 * z, a=min(1.0, z * 2))
    for i in range(4):
        z = ease_back(prog(t, tc + 0.3 + i * 0.15, 0.4))
        if z > 0:
            E.tablete(c, x + 44 + i * 76, y + 102, 66, 60, TINTA, min(1.0, z * 2), z)


def b_resposta(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"], C["s19.e"]
    s0 = C["s19"]
    E.frase(c, t, s0 + 0.3, ps("kits iguais, sem sobra, o maior número:", "i", 76), XE, 180, passo=0.11)
    E.foco(c, t, a_, 0.45, lambda a: E.pilula(c, "MDC", 1500, 155, 76, estilo="g", a=a))
    fatores(c, t, 63, (3, 3, 7), 340, b_, lerp(b_, c_, 0.8), d_, (1, 2), 92, dx=150)
    fatores(c, t, 84, (2, 2, 3, 7), 490, c_, lerp(c_, d_, 0.8), d_, (2, 3), 92, dx=150)
    conta_comum(c, t, d_ + 0.3, (3, 7), 660, s=88)
    E.foco(c, t, e_, 0.5, lambda a: bola_duas(c, "21", "kits", 1500, 430, 190, 150, 76, a, CERTO))
    a2, b2 = C["s20.a"], C["s20.b"]
    E.frase(c, t, C["s20"] + 0.2, ps("em cada kit", "i", 72, COR), XE, 780, passo=0.2)
    E.foco(c, t, a2, 0.45, lambda a: E.escreve(c, "63 ÷ 21 = 3 sabonetes", XE, 880, 66, "b", TINTA, a))
    E.foco(c, t, b2, 0.45, lambda a: E.escreve(c, "84 ÷ 21 = 4 cremes", XE, 970, 66, "b", TINTA, a))
    kit(c, t, 1230, 760, a2, b2)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.35, ps("resumindo", "i", 96, COR), W / 2, 210, "center")
        a_, b_ = C["s21.a"], C["s21.b"]
        E.foco(c, t, a_, 0.5, lambda a: num_bola(c, "1", 220, 400, 56, 64, a))
        E.frase(c, t, a_ + 0.1, ps("partes iguais, sem sobra,", "i", 84), 310, 430, passo=0.16)
        E.frase(c, t, a_ + 1.2, ps("as maiores possíveis:", "i", 84) + ps("é MDC", "g", 88, COR), 310, 540, passo=0.16)
        E.foco(c, t, b_, 0.5, lambda a: num_bola(c, "2", 220, 690, 56, 64, a))
        E.frase(c, t, b_ + 0.1, ps("confira o que", "i", 84) + ps("a pergunta quer", "g", 80, COR), 310, 720, passo=0.16)
        E.frase(c, t, b_ + 0.9, ps("de verdade", "i", 84), 310, 830, passo=0.16)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    s0 = C["s22"]
    E.frase(c, t, s0 + 0.5, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s22.a"], ps("Ônibus", "g", 130, COR) + ps("que", "i", 120), XE, 430)
    E.frase(c, t, C["s22.a"] + 0.7, ps("se", "i", 120) + ps("encontram", "g", 130, COR), XE, 570)
    E.frase(c, t, lerp(C["s22.a"], C["s22.b"], 0.5), ps("o problema de MMC", "i", 76), XE, 700, passo=0.2)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 380, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1740, 1590, p), lerp(690, 425, p), ep(t, C["s22.b"] + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s22.c"], ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fitas=b_fitas, conta=b_conta, bandejas=b_bandejas, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
