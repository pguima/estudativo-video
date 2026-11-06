"""Visual — Estudativo · MAT-FRA-004: frações maiores que 1 e número misto.
Identidade em _ferramentas/editorial.py. Sete pedaços soltos voam para três barras iguais: duas se completam e sobra um
terço. A conta armada entrega cada número para o seu lugar no número misto. Todos os instantes vêm dos cues da voz.
Peças só desta aula: P, fica, relogio, conta, misto, armada, voa, xicara, pizza, reta_mini."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, chocolate, chave, centro
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-004_fracoes_maiores_que_1_numero_misto.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barras", "ida", "volta", "atalho", "questao"))
BR = E.SOBRE


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def P(s, est="i", size=84, cor=None):
    """palavras de uma frase, todas no mesmo estilo"""
    return [(w, est, size, cor or TINTA) for w in s.split()]


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.15):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


def relogio(c, t, t0, cx, cy):
    """relógio de pausa: enche nos 3 segundos da pausa"""
    r = 190 * ease_back(prog(t, t0, 0.6))
    if r <= 0:
        return
    E.bola(c, cx, cy, r)
    f = M.clamp(prog(t, t0 + 0.8, 3.0))
    if f > 0:
        E.arco(c, cx, cy, r + 30, -90, 360 * f, TINTA, 10)
    for dx in (-40, 40):
        M.rrect(c, cx + dx - 20, cy - 72, 40, 144, 11, BR, ep(t, t0 + 0.2, 0.4))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + 300, 60, "i", TINTA, a))


def conta(c, t, esq, t0, dir_, t1, x, y, size, cor=None, cor2=None):
    """conta em que o resultado só aparece quando é falado"""
    E.foco(c, t, t0, 0.5, lambda a: E.escreve(c, esq, x, y, size, "g", cor or TINTA, a))
    E.foco(c, t, t1, 0.4, lambda a: E.escreve(c, dir_, x + E.larg(esq, "g", size) + size * 0.28, y, size, "g", cor2 or cor or TINTA, a))


def misto_xy(i, n, d, cx, s):
    """x do inteiro e da fração de um número misto centrado em cx; o inteiro é 1,7 vez maior que a fração"""
    n, d = str(n), str(d)
    wi = E.larg(str(i), "g", s * 1.7)
    wf = max(E.larg(n, "g", s), E.larg(d, "g", s)) + s * 0.2
    x0 = cx - (wi + s * 0.16 + wf) / 2
    return x0, x0 + wi + s * 0.16 + wf / 2


def misto(c, i, n, d, cx, cy, s, cor=None, a=1.0):
    """número misto: o inteiro grande e a fração ao lado"""
    if a <= 0:
        return
    xi, xf = misto_xy(i, n, d, cx, s)
    E.escreve(c, str(i), xi, cy + s * 0.6, s * 1.7, "g", cor or TINTA, a)
    E.fracao(c, n, d, xf, cy, s, cor or TINTA, a)


def armada(c, t, n, d, x, y, s, t0, tq, tr, q, r):
    """conta de dividir armada: dividendo, chave, divisor, resultado (em tq) e resto (em tr); x = onde a chave fica"""
    def base(a):
        E.escreve(c, str(n), x - E.larg(str(n), "g", s) - 34, y, s, "g", TINTA, a)
        M.line(c, x, y - s * 0.86, x, y + s * 0.3, TINTA, a, 7)
        M.line(c, x, y + s * 0.3, x + s * 1.1, y + s * 0.3, TINTA, a, 7)
        E.escreve(c, str(d), x + 36, y, s, "g", TINTA, a)
    E.foco(c, t, t0, 0.5, base)
    E.foco(c, t, tq, 0.4, lambda a: E.escreve(c, str(q), x + 36, y + s * 1.25, s, "g", COR, a))
    E.foco(c, t, tr, 0.4, lambda a: E.escreve(c, str(r), x - E.larg(str(n), "g", s) - 34, y + s * 1.25, s, "g", COR, a))


def voa(c, s_, x0, y0, s0, x1, y1, s1, q, cor):
    """número que sai de um lugar e pousa em outro; q = 0..1"""
    if q > 0:
        s = round(lerp(s0, s1, q))
        E.escreve(c, s_, lerp(x0, x1, q), lerp(y0, y1, q), s, "g", cor, 1.0)


def xicara(c, cx, y, w, h, f, a=1.0):
    """xícara com alça; y = topo; f = quanto está cheia"""
    if a <= 0:
        return
    x = cx - w / 2
    E.arco(c, x + w, y + h * 0.45, h * 0.24, -90, 180, TINTA, 9, a)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24)
    c.drawRRect(rr, M.paint(E.VAZIO, a))
    c.save(); c.clipRRect(rr, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * (1 - f), w, h * f), M.paint(COR, a))
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=4))


def pizza(c, cx, cy, r, n, cheias, cor=None, a=1.0):
    """pizza cortada em n fatias, com `cheias` pintadas"""
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    c.drawCircle(cx, cy, r, M.paint(E.VAZIO, a))
    for i in range(cheias):
        c.drawArc(ret, -90 + i * 360 / n, 360 / n, True, M.paint(cor or COR, a))
    for i in range(n):
        ang = M.math.radians(-90 + i * 360 / n)
        M.line(c, cx, cy, cx + r * M.math.cos(ang), cy + r * M.math.sin(ang), BR if i <= cheias and cheias else FIO, a, 4)
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=4))


def reta_mini(c, x0, x1, y, n, a=1.0):
    """trecho de reta numérica de 0 a n"""
    M.line(c, x0, y, x1, y, TINTA, a, 5)
    for i in range(n + 1):
        px = lerp(x0, x1, i / n)
        M.line(c, px, y - 16, px, y + 16, TINTA, a, 5)
        centro(c, str(i), px, y + 74, 54, "b", TINTA2, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    s2, ta, tb, tc = C["s02"], C["s01.a"], C["s01.b"], C["s01.c"]

    def duvida():
        x, w = 460, 1000
        E.foco(c, t, ta, 0.5, lambda q: chocolate(c, x, 170, w, 170, 3, (), q))
        E.foco(c, t, ta + 0.2, 0.4, lambda q: centro(c, "3 pedaços", W / 2, 420, 72, "g", COR, q))
        fr(c, t, tb, 7, 3, W / 2, 660, 210, COR)
        sinal(c, t, tb + 0.4, "?", W / 2 + 200, 650, 200, ERRADO)
        E.frase(c, t, tb + 1.2, P("parece erro de digitação"), W / 2, 950, "center", passo=0.17)
    E.saida(c, t, tc - 0.1, duvida)
    if t >= tc - 0.1:
        def maisde():
            E.foco(c, t, tc, 0.5, lambda a: E.fracao(c, 7, 3, 340, 450, 230, COR, a))
            for i in range(3):
                ped = [(j, COR, prog(t, tc + 0.2 + (i * 3 + j) * 0.12, 0.3)) for j in range(3) if i * 3 + j < 7]
                E.foco(c, t, tc + i * 0.1, 0.4, lambda a, i=i, ped=ped: chocolate(c, 680, 230 + i * 180, 1000, 140, 3, ped, a))
            E.frase(c, t, tc + 0.3, P("um jeito de contar") + P("mais de uma barra", "g", 76, COR), W / 2, 880, "center", passo=0.15)
        E.saida(c, t, s2 - 0.1, maisde)
    if t < s2:
        return

    E.frase(c, t, s2 + 0.2, P("até o fim desta aula, você vai", size=80, cor=COR), XE, 180, passo=0.13)
    ta2, tb2, tc2 = C["s02.a"], C["s02.b"], C["s02.c"]
    # ida
    y = 330
    fr(c, t, ta2, 7, 3, 300, y, 104, COR)
    p = ep(t, ta2 + 0.3, 0.6)
    if p > 0:
        M.arrow(c, 400, y, 610, y, TINTA, p, 5, 18, p)
    E.foco(c, t, ta2 + 0.6, 0.5, lambda a: misto(c, 2, 1, 3, 780, y, 100, COR, a))
    E.frase(c, t, ta2 + 0.8, [("transformar", "g", 92)], 1040, y + 30)
    # volta
    y = 590
    E.foco(c, t, tb2, 0.5, lambda a: misto(c, 2, 1, 3, 780, y, 100, COR, a))
    p = ep(t, tb2 + 0.2, 0.6)
    if p > 0:
        M.arrow(c, 610, y, 400, y, TINTA, p, 5, 18, p)
    fr(c, t, tb2 + 0.4, 7, 3, 300, y, 104, COR)
    E.frase(c, t, tb2 + 0.6, [("voltar", "g", 92)], 1040, y + 30)
    # atalho
    p = ease_back(prog(t, tc2 - 0.1, 0.5))
    if p > 0:
        E.mais(c, 300, 830, 62 * p, giro=(1 - p) * 90)
    E.frase(c, t, tc2, P("atalho", "g", 92) + P("de prova", "i", 100), 1040, 860, passo=0.15)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ta, tb, tc = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.3, P("para acompanhar,"), XE, 310)
    E.frase(c, t, ta - 0.8, P("você precisa de"), XE, 410, passo=0.14)
    E.foco(c, t, ta, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ta + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 235, 700, 120, "i", TINTA, a))
    x, w = 900, 840
    p = ep(t, tb, 0.5)
    E.caixa_pontilhada(c, x, 190, w, 220, p, prog_=p)
    E.frase(c, t, tb + 0.1, [("Saber o que é", "i", 72)], x + 44, 285)
    E.frase(c, t, tb + 0.3, [("uma fração", "g", 76, COR)], x + 44, 370)
    p = ep(t, tc, 0.5)
    E.caixa_pontilhada(c, x, 450, w, 300, p, prog_=p)
    E.frase(c, t, tc + 0.1, [("Dividir", "i", 72), ("com resto", "g", 76, COR)], x + 44, 550, passo=0.2)
    E.foco(c, t, tc + 1.3, 0.4, lambda a: E.escreve(c, "17 ÷ 5 = 3", x + 44, 660, 76, "g", TINTA, a))
    E.foco(c, t, tc + 2.1, 0.4, lambda a: E.escreve(c, "sobram 2", x + 480, 660, 66, "b", COR, a))
    q = ease_io(prog(t, tc - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(380, 720, q), ep(t, tb, 0.4))
    E.frase(c, t, C["s04"] - 1.6, P("procure a aula", size=60) + P("no canal", "g", 54, COR), XE, 860, passo=0.14)


# ---------------- três barras, sete pedaços ----------------
BX, BW, BH = 560, 1060, 125
BYS = (170, 320, 470)


def b_barras(c, t, C, b):
    lp = BW / 3
    ta, tb, tc = C["s04.a"], C["s04.b"], C["s04.c"]
    xa, xb, xc, xd = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    ya, yb, yc = C["s06.a"], C["s06.b"], C["s06.c"]

    # títulos
    fica(c, t, C["s04"] + 0.2, xa - 0.15, P("três barras iguais, cada uma em", size=72) + P("três pedaços", "g", 66, COR), W / 2, 110, "center", passo=0.13)
    fica(c, t, xa, ya - 0.1, P("sete terços são", size=72) + P("sete pedaços", "g", 66, COR), W / 2, 110, "center", passo=0.13)
    E.frase(c, t, ya, P("duas barras inteiras", "g", 66, COR) + P("e mais um terço", size=72), W / 2, 110, "center", passo=0.13)

    # as barras
    for i, y in enumerate(BYS):
        E.foco(c, t, ta + i * 0.25, 0.5, lambda a, y=y: chocolate(c, BX, y, BW, BH, 3, (), a, ep(t, tb, 0.8)))

    # os 7 pedaços nascem soltos e voam para as barras
    for k in range(7):
        tk = xb + k * 0.1 if k < 3 else xc + (k - 3) * 0.1 if k < 6 else xd
        q = ease_io(prog(t, tk, 0.6))
        p = prog(t, xa + k * 0.12, 0.35)
        x = lerp(960 - 7 * 150 / 2 + k * 150 + 8, BX + (k % 3) * lp, q)
        y = lerp(650, BYS[k // 3], q)
        w, h = lerp(134, lp, q), lerp(125, BH, q)
        if p > 0:
            E.tablete(c, x, y, w, h, COR, M.clamp(p * 1.6), lerp(0.55, 1.0, ease_back(p)))
            centro(c, str(k + 1), x + w / 2, y + h / 2 + 27, 76, "g", BR, M.clamp(p * 1.6))

    # cada pedaço é um terço
    def terco():
        E.foco(c, t, tc, 0.4, lambda a: E.caixa_pontilhada(c, BX + 6, BYS[0] + 6, lp - 12, BH - 12, a, COR))
        E.foco(c, t, tc, 0.5, lambda a: E.fracao(c, 1, 3, 330, BYS[0] + BH / 2 - 4, 76, COR, a))
    E.saida(c, t, xa - 0.15, terco)

    # à esquerda, o que cada barra virou
    def rotulos():
        for t0, s, i in ((xb + 0.4, "1 barra", 0), (xc + 0.4, "mais 1", 1), (xd + 0.3, "sobra 1", 2)):
            E.foco(c, t, t0, 0.4, lambda a, s=s, i=i: E.escreve(c, s, BX - 40 - E.larg(s, "g", 70), BYS[i] + BH / 2 + 24, 70, "g", COR, a))
    E.saida(c, t, ya - 0.1, rotulos, d=0.3)
    p = ep(t, ya, 0.5)
    if p > 0:
        M.line(c, BX - 30, BYS[0] + 6, BX - 30, lerp(BYS[0] + 6, BYS[1] + BH - 6, p), TINTA, p, 6)
    E.foco(c, t, ya + 0.1, 0.4, lambda a: (centro(c, "2", 230, 345, 150, "g", COR, a), E.escreve(c, "inteiros", 300, 335, 62, "b", COR, a)))
    E.foco(c, t, ya + 0.9, 0.4, lambda a: E.fracao(c, 1, 3, 400, BYS[2] + BH / 2 - 4, 76, COR, a))

    # a mesma quantidade
    y = 790
    E.frase(c, t, yb - 2.4, P("a mesma quantidade,", size=72) + P("dois jeitos", "g", 66, COR), W / 2, 985, "center", passo=0.14)
    fr(c, t, yb, 7, 3, 620, y, 120)
    sinal(c, t, yc - 0.2, "=", 820, y, 110)
    E.foco(c, t, yc, 0.5, lambda a: misto(c, 2, 1, 3, 1090, y, 120, COR, a))


# ---------------- nomes ----------------
def b_nomes(c, t, C, b):
    ta, tb = C["s07.a"], C["s07.b"]
    s8, xa, xb, xc = C["s08"], C["s08.a"], C["s08.b"], C["s08.c"]

    def duas():
        E.frase(c, t, C["s07"] + 0.2, P("esses jeitos têm") + P("nome", "g", 76, COR), W / 2, 160, "center")
        M.line(c, W / 2, 240, W / 2, 960, FIO, ep(t, C["s07"] + 0.4, 0.5), 3)
        # imprópria
        x = XE
        E.frase(c, t, ta - 2.8, P("de cima", "g", 62) + P("maior ou igual", size=68), x, 300, passo=0.13)
        E.frase(c, t, ta, P("fração", size=96) + P("imprópria", "g", 88, COR), x, 440, passo=0.2)
        E.foco(c, t, ta + 0.2, 0.5, lambda a: E.fracao(c, 7, 3, x + 90, 620, 130, COR, a))
        for i in range(3):
            E.foco(c, t, ta + 0.3 + i * 0.12, 0.4, lambda a, i=i: chocolate(c, x + 230, 515 + i * 92, 480, 76, 3, [(j, COR, 1) for j in range(3) if i * 3 + j < 7], a))
        E.frase(c, t, ta + 1.0, P("vale", size=72) + P("1 inteiro ou mais", "g", 66, COR), x, 880, passo=0.13)
        # própria
        x = 1010
        E.frase(c, t, tb - 1.4, P("de cima", "g", 62) + P("menor", size=68), x, 300, passo=0.13)
        E.frase(c, t, tb, P("fração", size=96) + P("própria", "g", 88, COR), x, 440, passo=0.2)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: E.fracao(c, 2, 3, x + 90, 620, 130, COR, a))
        E.foco(c, t, tb + 0.3, 0.4, lambda a: chocolate(c, x + 230, 607, 480, 76, 3, [(j, COR, 1) for j in range(2)], a))
        E.frase(c, t, tb + 1.0, P("vale", size=72) + P("menos que 1 inteiro", "g", 66, COR), x, 880, passo=0.13)
    E.saida(c, t, s8 - 0.1, duas)
    if t < s8 - 0.1:
        return

    E.frase(c, t, xa - 1.2, P("um inteiro junto com uma fração", size=76), W / 2, 170, "center", passo=0.13)
    E.frase(c, t, xa, P("número misto", "g", 130, COR), W / 2, 330, "center", passo=0.2)
    cx, cy, s = 520, 590, 170
    E.foco(c, t, xa + 0.3, 0.5, lambda a: misto(c, 2, 1, 3, cx, cy, s, None, a))
    xi, xf = misto_xy(2, 1, 3, cx, s)
    E.frase(c, t, xb, P("dois inteiros e um terço", size=92), cx, 860, "center", passo=0.17)
    # receita: 2 xícaras e meia
    y = 470
    for i, f in enumerate((1.0, 1.0, 0.5)):
        E.foco(c, t, xc + 0.2 + i * 0.25, 0.5, lambda a, i=i, f=f: xicara(c, 1150 + i * 230, y, 170, 200, f, a))
    E.frase(c, t, xc, P("duas xícaras", "g", 66, COR) + P("e meia", size=72), 1370, 760, "center", passo=0.15)
    E.foco(c, t, xc + 0.8, 0.5, lambda a: misto(c, 2, 1, 2, 1370, 900, 66, COR, a))


# ---------------- da fração para o número misto ----------------
def b_ida(c, t, C, b):
    s10, s11, s12 = C["s10"], C["s11"], C["s12"]
    ta, tb, tc_, td = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    xa, xb, xc = C["s10.a"], C["s10.b"], C["s10.c"]

    def tela():
        fica(c, t, C["s09"] + 0.2, s10 - 0.1, P("o traço é uma") + P("divisão", "g", 76, COR), W / 2, 170, "center")
        fica(c, t, s10 + 0.1, s11, P("cada número tem") + P("seu lugar", "g", 76, COR), W / 2, 170, "center")
        lb = E.mix(TINTA, COR, ep(t, ta, 0.4))
        cy, s = 480, 200
        E.foco(c, t, C["s09"] + 0.3, 0.5, lambda a: E.fracao(c, 7, 3, 290, cy, s, TINTA, a, barra=lb))
        sinal(c, t, tb - 0.1, "=", 490, cy, 130)
        # a conta armada
        xc0, yc0, z = 780, cy - 30, 150
        armada(c, t, 7, 3, xc0, yc0, z, tb, tc_, td, 2, 1)
        E.foco(c, t, td + 0.1, 0.4, lambda a: E.escreve(c, "sobra 1", xc0 - 300, yc0 + z * 1.25 + 90, 60, "b", COR, a))
        # o número misto, com os lugares marcados
        cx, s2 = 1500, 170
        xi, xf = misto_xy(2, 1, 3, cx, s2)
        p = ep(t, s10 + 0.1, 0.5)
        lw = E.larg("3", "g", s2) + s2 * 0.2
        wi = E.larg("2", "g", s2 * 1.7)
        ain = 1 - prog(t, xa + 0.5, 0.2)
        E.caixa_pontilhada(c, xi - 16, cy - s2 * 0.9, wi + 32, s2 * 1.8, p * ain, COR, prog_=p)
        E.caixa_pontilhada(c, xf - lw / 2 - 10, cy - s2 * 0.95, lw + 20, s2 * 0.86, p * (1 - prog(t, xb + 0.5, 0.2)), COR, prog_=p)
        E.caixa_pontilhada(c, xf - lw / 2 - 10, cy + s2 * 0.13, lw + 20, s2 * 0.86, p * (1 - prog(t, xc + 0.5, 0.2)), COR, prog_=p)
        M.rrect(c, xf - lw / 2, cy - 7, lw, 15, 7, TINTA, p)
        # cada número voa para o seu lugar
        voa(c, "2", xc0 + 36, yc0 + z * 1.25, z, xi, cy + s2 * 0.6, s2 * 1.7, ease_io(prog(t, xa, 0.6)), COR)
        voa(c, "1", xc0 - E.larg("7", "g", z) - 34, yc0 + z * 1.25, z, xf - E.larg("1", "g", s2) / 2, cy - s2 * 0.2, s2, ease_io(prog(t, xb, 0.6)), COR)
        voa(c, "3", xc0 + 36, yc0, z, xf - E.larg("3", "g", s2) / 2, cy + s2 * 0.9, s2, ease_io(prog(t, xc, 0.6)), COR)
        fica(c, t, xa, xb - 0.1, P("o resultado vira o") + P("inteiro", "g", 76, COR), W / 2, 880, "center")
        fica(c, t, xb, xc - 0.1, P("o resto vira o") + P("de cima", "g", 76, COR), W / 2, 880, "center")
        E.frase(c, t, xc, P("o de baixo") + P("continua igual:", "g", 76, COR) + P("o pedaço não mudou"), W / 2, 880, "center", passo=0.13)
    E.saida(c, t, s11 - 0.1, tela)
    if t < s11 - 0.1:
        return

    ya, yb, yc = C["s11.a"], C["s11.b"], C["s11.c"]
    za, zb = C["s12.a"], C["s12.b"]
    # com resto
    y = 270
    fr(c, t, ya, 11, 4, 280, y, 130, COR)
    conta(c, t, "11 ÷ 4 =", ya + 0.8, "2", yb + 0.1, 460, y - 26, 84)
    E.foco(c, t, yb + 0.7, 0.4, lambda a: E.escreve(c, "sobram 3", 860, y - 26, 70, "b", COR, a))
    for i in range(3):
        E.foco(c, t, yb + 0.1 + i * 0.2, 0.4, lambda a, i=i: chocolate(c, 460 + i * 290, y + 34, 270, 84, 4, [(j, COR, 1) for j in range(4 if i < 2 else 3)], a))
    E.foco(c, t, yc, 0.5, lambda a: misto(c, 2, 3, 4, 1560, y, 120, COR, a))
    # sem resto
    M.line(c, XE, 500, W - XE, 500, FIO, ep(t, C["s12"], 0.5), 3)
    y = 700
    E.frase(c, t, C["s12"] + 0.2, P("e sem resto?", size=72, cor=COR), W / 2, 590, "center")
    fr(c, t, za, 12, 4, 280, y, 130)
    conta(c, t, "12 ÷ 4 =", za + 0.7, "3", za + 1.8, 460, y - 26, 84)
    E.foco(c, t, za + 2.2, 0.4, lambda a: E.escreve(c, "sem sobra", 860, y - 26, 70, "b", COR, a))
    for i in range(3):
        E.foco(c, t, za + 1.8 + i * 0.2, 0.4, lambda a, i=i: chocolate(c, 460 + i * 290, y + 34, 270, 84, 4, [(j, COR, 1) for j in range(4)], a))
    E.foco(c, t, zb, 0.5, lambda a: (E.bola(c, 1560, y + 3, 120, a=a), centro(c, "3", 1560, y + 52, 150, "g", BR, a)))
    E.frase(c, t, zb + 0.4, P("número inteiro,") + P("sem fração nenhuma", "g", 76, COR), W / 2, 950, "center", passo=0.14)


# ---------------- a volta ----------------
def b_volta(c, t, C, b):
    s14, s15 = C["s14"], C["s15"]
    ta, tb, tc_, td = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]

    def pedacos():
        E.frase(c, t, C["s13"] + 0.2, P("para voltar,") + P("pense nos pedaços", "g", 76, COR), XE, 150, passo=0.14)
        E.foco(c, t, C["s13"] + 0.3, 0.5, lambda a: misto(c, 2, 1, 3, 340, 370, 120, None, a))
        bx, bw, bh = 700, 1000, 120
        lp = bw / 3
        ys = (210, 350, 490)
        for k, y in enumerate(ys):
            E.foco(c, t, C["s13"] + 0.4 + k * 0.15, 0.4, lambda a, y=y: chocolate(c, bx, y, bw, bh, 3, (), a))
        for k in range(7):
            tk = ta + k * 0.12 if k < 6 else tb
            p = prog(t, tk, 0.35)
            if p > 0:
                x, y = bx + (k % 3) * lp, ys[k // 3]
                E.tablete(c, x, y, lp, bh, COR, M.clamp(p * 1.6), lerp(0.55, 1.0, ease_back(p)))
                centro(c, str(k + 1), x + lp / 2, y + bh / 2 + 27, 76, "g", BR, M.clamp(p * 1.6))
        conta(c, t, "2 × 3 =", ta, "6", ta + 1.2, XE, 760, 104)
        E.foco(c, t, ta + 1.4, 0.4, lambda a: E.escreve(c, "pedaços", 640, 760, 72, "i", TINTA, a))
        conta(c, t, "6 + 1 =", tc_, "7", tc_ + 0.8, XE, 910, 104, COR)
        E.resultado(c, t, td, 7, 3, 1400, 790, 124, 165)
    E.saida(c, t, s14 - 0.1, pedacos)
    if t < s14 - 0.1:
        return

    def regra():
        xa, xb, xc, xd = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
        E.frase(c, t, s14 + 0.2, P("a regra", cor=COR), XE, 170)
        E.foco(c, t, s14 + 0.3, 0.5, lambda a: misto(c, 2, 1, 3, 400, 490, 210, None, a))
        x = 800
        for i, (t0, l1, l2) in enumerate(((xa, "inteiro × de baixo", "2 × 3 = 6"), (xb, "mais o de cima", "6 + 1 = 7"), (xc, "de baixo igual", "7/3"))):
            y = 290 + i * 190
            E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 52, y - 26, 52, a=a), centro(c, str(i + 1), x + 52, y - 3, 60, "g", BR, a)))
            E.frase(c, t, t0 + 0.1, [(l1, "g", 76)], x + 140, y)
            if i < 2:
                E.frase(c, t, t0 + 0.4, [(l2, "b", 66, COR)], x + 140, y + 80)
            else:
                E.foco(c, t, t0 + 0.4, 0.5, lambda a, y=y: E.fracao(c, 7, 3, x + 740, y - 26, 72, COR, a))
        E.foco(c, t, xd, 0.4, lambda a: E.pilula(c, "prova real", 480, 925, 62, estilo="g", fundo=TINTA, cor=BR, a=a))
        E.frase(c, t, xd + 0.5, P("resultado × divisor + resto", "b", 62, TINTA2), 760, 947, passo=0.12)
    E.saida(c, t, s15 - 0.1, regra)
    if t < s15 - 0.1:
        return

    ya, yb, yc, yd = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, s15 + 0.2, P("treine", cor=COR), XE, 190)
    E.foco(c, t, ya, 0.5, lambda a: misto(c, 3, 2, 5, 380, 540, 170, None, a))
    conta(c, t, "3 × 5 =", ya + 1.0, "15", yb, 720, 470, 110)
    conta(c, t, "15 + 2 =", yb + 0.5, "17", yc, 720, 660, 110, COR)
    E.resultado(c, t, yd, 17, 5, 1520, 540, 118, 170)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ta, tb = C["s16.a"], C["s16.b"]
    xa, xb, xc, xd = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, C["s16"] + 0.2, P("cuidado", "g", 92, ERRADO) + P("com o erro mais comum", size=88), W / 2, 160, "center")
    y = 320
    E.foco(c, t, C["s16"] + 0.6, 0.5, lambda a: misto(c, 2, 1, 3, 380, y, 120, None, a))
    E.foco(c, t, ta, 0.5, lambda a: E.escreve(c, "2 + 1", 650, y + 30, 84, "g", ERRADO, a))
    sinal(c, t, tb - 0.2, "=", 960, y, 100)
    fr(c, t, tb, 3, 3, 1110, y, 120, ERRADO)
    if t >= xa:
        E.risco(c, 1040, y + 120, 1180, y - 120, t, xa, largura=12)
    fica(c, t, ta, xa - 0.1, P("soma o inteiro com o de cima", size=76, cor=ERRADO), W / 2, 590, "center", passo=0.13)
    # uma barra só contra mais de duas
    E.foco(c, t, xa, 0.5, lambda a: (E.fracao(c, 3, 3, 300, 575, 76, ERRADO, a), chocolate(c, 450, 520, 340, 100, 3, [(j, ERRADO, 1) for j in range(3)], a)))
    E.foco(c, t, xa + 0.3, 0.4, lambda a: E.escreve(c, "uma barra só", 830, 590, 72, "g", ERRADO, a))
    E.foco(c, t, xb, 0.5, lambda a: misto(c, 2, 1, 3, 300, 755, 60, COR, a))
    for i in range(3):
        E.foco(c, t, xb + i * 0.15, 0.4, lambda a, i=i: chocolate(c, 450 + i * 355, 700, 340, 100, 3, [(j, COR, 1) for j in range(3 if i < 2 else 1)], a))
    E.frase(c, t, xc, P("cada inteiro vale", size=72) + P("3 pedaços,", "g", 66, COR) + P("não 1", size=72), XE, 900, passo=0.13)
    E.frase(c, t, xd, P("o inteiro", size=72) + P("multiplica antes de somar", "g", 66, COR), XE, 985, passo=0.13)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s19, s20 = C["s19"], C["s20"]
    ta, tb, tc_ = C["s18.a"], C["s18.b"], C["s18.c"]

    def tabuada():
        E.frase(c, t, C["s18"] + 0.3, P("e o atalho prometido", cor=CLARO), W / 2, 150, "center")
        E.frase(c, t, ta, P("a tabuada", "i", 120, CLARO) + P("do de baixo", "g", 110, BR), W / 2, 300, "center")
        fr(c, t, tb, 23, 4, 300, 610, 170, BR)
        y, px, x0 = 620, 190, 610
        for i, v in enumerate((4, 8, 12, 16, 20, 24)):
            x = x0 + i * px
            tv = tb + 1.6 + i * 0.2
            if v == 20:
                E.foco(c, t, tc_, 0.4, lambda a, x=x: E.bola(c, x, y - 33, 78, CERTO, a))
            cor = BR if v == 20 and t >= tc_ else CLARO
            E.foco(c, t, tv, 0.35, lambda a, x=x, v=v, cor=cor: centro(c, str(v), x, y, 92, "g", cor, a))
        if t >= tc_:
            E.risco(c, x0 + 5 * px - 70, y + 30, x0 + 5 * px + 70, y - 90, t, tc_, largura=9)
        E.frase(c, t, tb + 1.9, P("o maior que não passa de 23", "i", 70, CLARO), x0 - 80, 780, passo=0.13)
        E.foco(c, t, tc_, 0.5, lambda a: E.escreve(c, "4 × 5 = 20", 800, 920, 110, "g", BR, a))
    E.saida(c, t, s19 - 0.1, tabuada)
    if t < s19 - 0.1:
        return

    def acha():
        xa, xb, xc = C["s19.a"], C["s19.b"], C["s19.c"]
        fr(c, t, s19, 23, 4, 300, 480, 170, BR)
        E.foco(c, t, s19 + 0.1, 0.4, lambda a: E.escreve(c, "4 ×", 540, 370, 110, "g", CLARO, a))
        E.foco(c, t, xa, 0.4, lambda a: (E.bola(c, 820, 332, 80, a=a), centro(c, "5", 820, 372, 112, "g", BR, a)))
        E.foco(c, t, s19 + 0.1, 0.4, lambda a: E.escreve(c, "= 20", 925, 370, 110, "g", CLARO, a))
        E.frase(c, t, xa + 0.2, P("o cinco é o inteiro", "i", 72, CLARO), 540, 460, passo=0.13)
        conta(c, t, "23 − 20 =", xb - 0.9, "3", xb, 540, 660, 110, CLARO, BR)
        E.frase(c, t, xb + 0.2, P("faltam três: é o de cima", "i", 72, CLARO), 540, 750, passo=0.13)
        E.foco(c, t, xc, 0.5, lambda a: (E.bola(c, 1520, 520, 240, CERTO, a), misto(c, 5, 3, 4, 1520, 520, 104, BR, a)))
    E.saida(c, t, s20 - 0.1, acha)
    if t < s20 - 0.1:
        return

    xa, xb, xc = C["s20.a"], C["s20.b"], C["s20.c"]
    E.frase(c, t, xa - 1.1, P("funciona porque", "i", 80, CLARO), W / 2, 190, "center")
    E.frase(c, t, xa, P("quantas vezes", "i", 100, CLARO) + P("o de baixo cabe", "g", 92, BR), W / 2, 330, "center", passo=0.15)
    E.frase(c, t, xa + 1.0, P("no de cima", "g", 92, BR), W / 2, 450, "center")
    E.frase(c, t, xb - 1.4, P("não compensa", "g", 76, BR) + P("fora da tabuada", "i", 84, CLARO), W / 2, 610, "center", passo=0.14)
    fr(c, t, xb, 307, 7, 560, 800, 130, BR)
    E.foco(c, t, xc, 0.5, lambda a: (E.escreve(c, "307", 1000, 835, 130, "g", BR, a), M.line(c, 1270, 725, 1270, 865, CLARO, a, 7),
                                     M.line(c, 1270, 865, 1440, 865, CLARO, a, 7), E.escreve(c, "7", 1310, 835, 130, "g", BR, a)))
    E.foco(c, t, xc + 0.3, 0.4, lambda a: E.pilula(c, "arme a conta", 1230, 960, 56, estilo="g", fundo=E.COR, cor=BR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ta, tb, tc_ = C["s21.a"], C["s21.b"], C["s21.c"]
    E.frase(c, t, C["s21"] + 0.3, P("hora de testar", size=72, cor=COR), XE, 170)
    E.frase(c, t, ta - 0.9, P("uma pizzaria corta cada pizza em", size=62), XE, 310, passo=0.13)
    E.frase(c, t, ta, P("8 fatias", "g", 100, COR), XE, 420)
    E.frase(c, t, tb - 0.8, P("em uma noite, vendeu", size=68), XE, 560, passo=0.13)
    E.frase(c, t, tb, P("19 fatias", "g", 100, COR), XE, 670)
    E.foco(c, t, ta + 0.1, 0.5, lambda a: pizza(c, 1125, 450, 155, 8, 8, a=a))
    E.frase(c, t, tc_, P("quantas pizzas,", size=100) + P("em número misto?", "g", 90, COR), XE, 880, passo=0.15)
    relogio(c, t, C["s22.a"], 1555, 340)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ta, tb, tc_, td = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    s24, xa, xb = C["s24"], C["s24.a"], C["s24.b"]
    E.frase(c, t, ta - 1.2, P("cada fatia é um oitavo", size=72, cor=COR), XE, 150, passo=0.13)
    fr(c, t, ta, 19, 8, 280, 350, 150, COR)
    conta(c, t, "8 × 2 =", tb, "16", tb + 1.0, 520, 310, 92)
    conta(c, t, "19 − 16 =", tc_ - 0.9, "3", tc_, 520, 450, 92, COR)
    E.foco(c, t, td, 0.5, lambda a: (M.rrect(c, 1090, 230, 640, 240, 120, CERTO, a), misto(c, 2, 3, 8, 1410, 345, 84, BR, a)))
    # as pizzas vendidas
    y, r = 750, 165
    E.foco(c, t, tb + 0.2, 0.5, lambda a: pizza(c, 310, y, r, 8, 8, a=a))
    E.foco(c, t, tb + 0.4, 0.5, lambda a: pizza(c, 680, y, r, 8, 8, a=a))
    E.foco(c, t, tc_, 0.5, lambda a: pizza(c, 1050, y, r, 8, 3, a=a))
    conta(c, t, "2 × 8 =", xa, "16", xa + 0.8, 1300, 690, 76)
    conta(c, t, "+ 3 =", xb, "19", xb + 0.6, 1300, 800, 76, COR)
    E.foco(c, t, xb + 1.0, 0.4, lambda a: E.pilula(c, "bateu!", 1500, 900, 60, estilo="g", fundo=CERTO, cor=BR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    s26 = C["s26"]

    def resumo():
        E.frase(c, t, C["s25"] + 0.3, P("resumindo", size=92, cor=COR), W / 2, 170, "center")
        ta, tb = C["s25.a"], C["s25.b"]
        for i, (t0, l1, l2) in enumerate(((ta, "para ir:", "divide, e o resto vira o de cima"), (tb, "para voltar:", "inteiro × de baixo + de cima"))):
            y = 400 + i * 300
            E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, 250, y + 20, 62, a=a), centro(c, str(i + 1), 250, y + 45, 72, "g", BR, a)))
            E.frase(c, t, t0 + 0.1, [(l1, "i", 100)], 350, y)
            E.frase(c, t, t0 + 0.3, [(l2, "g", 76, COR)], 350, y + 110)
    E.saida(c, t, s26 - 0.1, resumo)
    if t < s26 - 0.1:
        return

    ta, tb, tc_, td = C["s26.a"], C["s26.b"], C["s26.c"], C["s26.d"]
    E.frase(c, t, s26 + 0.2, P("próxima aula"), XE, 190)
    E.frase(c, t, s26 + 0.8, P("Comparar frações", "g", 112, COR), XE, 320, passo=0.15)
    E.frase(c, t, ta + 0.8, P("e marcar na reta", "g", 112, COR), XE, 440, passo=0.15)
    E.foco(c, t, ta + 0.8, 0.5, lambda a: reta_mini(c, 260, 1040, 700, 3, a))
    px = lerp(260, 1040, 2.5 / 3)
    p = ease_back(prog(t, tb, 0.5))
    if p > 0:
        E.bola(c, px, 700, 26 * p)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: E.fracao(c, 5, 2, px, 570, 76, COR, a))
    E.foco(c, t, tc_, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 620, 84, estilo="g", cor=BR, a=a))
    p = ease_io(prog(t, tc_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1630, p), lerp(860, 660, p), ep(t, tc_ + 0.2, 0.4), cor=TINTA)
    E.frase(c, t, td, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barras=b_barras, nomes=b_nomes, ida=b_ida, volta=b_volta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
