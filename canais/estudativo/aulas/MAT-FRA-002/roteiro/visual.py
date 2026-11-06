"""Visual — Estudativo · MAT-FRA-002: fração de uma quantidade, a parte e o total.
Identidade em _ferramentas/editorial.py. A barra de 20 quadradinhos abre em 4 partes de 5; depois a barra do salário faz o
caminho de volta. Azul = a parte, vermelho = erro, verde = certo. Todos os instantes vêm dos cues da voz.
Peças só desta aula: P, fica, relogio, vinte, tamanhos, tanque."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, chocolate, chave, centro
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-002_fracao_de_uma_quantidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barra", "volta", "escolha", "atalho", "questao"))
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


W5, GAP = 320, 40  # largura de uma parte da barra de 20 e o vão quando ela abre


def x_parte(i, abre):
    """x da parte i da barra de 20, com as partes abrindo a partir do meio"""
    g = GAP * abre
    return W / 2 - (4 * W5 + 3 * g) / 2 + i * (W5 + g)


def vinte(c, y, h, abre, pinta, a=1.0, cortes=1.0, escuro=False):
    """barra de 20 quadradinhos. abre = 0 é a barra inteira; abre > 0 são 4 partes de 5. pinta[i] = (cor, p) da parte i"""
    if abre <= 0:
        ped = [(i * 5 + j, *pinta[i]) for i in range(4) if pinta[i] for j in range(5)]
        chocolate(c, x_parte(0, 0), y, 4 * W5, h, 20, ped, a, cortes, escuro)
        return
    for i in range(4):
        ped = [(j, *pinta[i]) for j in range(5)] if pinta[i] else []
        chocolate(c, x_parte(i, abre), y, W5, h, 5, ped, a, 1.0, escuro)


def tamanhos(c, t, x, y, h, itens):
    """barras de mesma escala, para comparar a olho: itens = [(valor, rótulo, cor, t0)]; R$ 1.500 ocupa 1500 px menos a folga"""
    for i, (v, rot, cor, t0) in enumerate(itens):
        yy = y + i * (h + 66)
        w = v * 0.8
        q = ep(t, t0, 0.6)
        if q > 0:
            M.rrect(c, x, yy, w * q, h, 12, cor, 1.0)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a, rot=rot, cor=cor, yy=yy, w=w: E.escreve(c, rot, x + w + 26, yy + h / 2 + 22, 62, "b", cor, a))


def tanque(c, x, y, w, h, n, cheio, a=1.0, cor=None):
    """tanque em pé, com n partes iguais e `cheio` partes de combustível"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 26, 26)
    c.drawRRect(rr, M.paint(E.VAZIO, a))
    c.save(); c.clipRRect(rr, True)
    al = h * cheio / n
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - al, w, al), M.paint(cor or COR, a))
    for i in range(1, n):
        ly = y + h * i / n
        M.line(c, x, ly, x + w, ly, BR if ly > y + h - al + 1 else TINTA2, a, 4, cap_round=False)
    c.restore()
    c.drawRRect(rr, M.paint(TINTA, a, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    s2, ta, tb, tc = C["s02"], C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        y = 300
        fr(c, t, ta, 2, 5, 330, y, 190, COR)
        E.frase(c, t, ta + 0.3, P("do seu salário", size=108), 500, y + 36, passo=0.15)
        sinal(c, t, tb - 0.15, "=", 1200, y + 2, 130)
        E.frase(c, t, tb, [("R$ 600", "g", 150, COR)], 1290, y + 52)
        E.frase(c, t, tb + 1.2, P("qual é o salário?", "g", 84), W / 2, 560, "center", passo=0.17)

        def errado():
            E.foco(c, t, tc, 0.5, lambda a: centro(c, "R$ 240 ?", W / 2, 720, 130, "g", ERRADO, a))
        E.saida(c, t, lerp(tc, s2, 0.45), errado, d=0.3)
        E.saida(c, t, lerp(tc, s2, 0.45), lambda: E.frase(c, t, lerp(tc, s2, 0.25), P("tem algo") + P("muito errado", "g", 76, ERRADO), W / 2, 870, "center"), d=0.3)
        tq = lerp(tc, s2, 0.5)
        tamanhos(c, t, 400, 640, 96, ((600, "a parte: R$ 600", COR, tq), (240, "o salário: R$ 240 ?", ERRADO, tq + 0.5)))
    E.saida(c, t, s2 - 0.1, conta)
    if t < s2:
        return

    E.frase(c, t, s2 + 0.2, P("até o fim desta aula, você vai", size=80, cor=COR), XE, 200, passo=0.13)
    x = 620
    # 1: fração de qualquer quantidade
    E.foco(c, t, C["s02.a"], 0.5, lambda a: (E.fracao(c, 3, 4, XE + 90, 380, 92, COR, a), E.escreve(c, "de 20", XE + 170, 412, 80, "i", TINTA, a)))
    E.frase(c, t, C["s02.a"] + 0.1, P("calcular", "g", 88) + P("a fração", "i", 96), x, 390, passo=0.15)
    E.frase(c, t, C["s02.a"] + 0.5, P("de qualquer quantidade", "i", 76, TINTA2), x, 470, passo=0.13)
    # 2: da parte para o total
    y = 640

    def seta(a):
        E.escreve(c, "parte", XE, y + 18, 70, "g", COR, a)
    E.foco(c, t, C["s02.b"], 0.5, seta)
    p = ep(t, C["s02.b"] + 0.2, 0.5)
    if p > 0:
        M.arrow(c, XE + 195, y - 4, XE + 270, y - 4, TINTA, p, 5, 16, p)
    E.foco(c, t, C["s02.b"] + 0.4, 0.5, lambda a: centro(c, "total", XE + 350, y + 18, 66, "g", TINTA, a))
    E.frase(c, t, C["s02.b"] + 0.1, P("fazer", "i", 96) + P("o caminho de volta", "g", 84), x, y + 20, passo=0.15)
    # 3: atalho
    p = ease_back(prog(t, C["s02.c"] - 0.1, 0.5))
    if p > 0:
        E.mais(c, XE + 130, 850, 62 * p, giro=(1 - p) * 90)
    E.frase(c, t, C["s02.c"], P("atalho", "g", 88) + P("de prova", "i", 96), x, 880, passo=0.15)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, P("para acompanhar,"), XE, 310)
    E.frase(c, t, C["s03.a"] - 0.8, P("você precisa de"), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 235, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    itens = ((C["s03.b"], "Saber o que é", "uma fração"), (C["s03.c"], "Multiplicar por", "um algarismo"))
    for i, (t0, l1, l2) in enumerate(itens):
        y = 260 + i * 270
        p = ep(t, t0, 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, t0 + 0.1, [(l1, "i", 66)], x + 44, y + 92)
        E.frase(c, t, t0 + 0.3, [(l2, "g", 70, COR)], x + 44, y + 176)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 720, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.c"] + 1.6, P("procure a aula", size=60) + P("no canal", "g", 54, COR), XE, 850, passo=0.14)


# ---------------- a barra de 20 ----------------
def b_barra(c, t, C, b):
    ta, tb, tc = C["s04.a"], C["s04.b"], C["s04.c"]
    t5a, t5b, t6a, t6b, t6c = C["s05.a"], C["s05.b"], C["s06.a"], C["s06.b"], C["s06.c"]
    y, h = 370, 150
    abre = ease_io(prog(t, t5a, 0.8))

    # a pergunta fica no alto
    E.saida(c, t, t6c - 0.15, lambda: E.frase(c, t, tc - 0.5, P("quanto é", size=96), 700, 240, "right"), d=0.3)
    E.foco(c, t, tc, 0.5, lambda a: E.fracao(c, 3, 4, 800, 210, 104, COR, a))
    E.frase(c, t, tc + 0.3, P("de 20", size=96), 900, 240)
    E.foco(c, t, t6c, 0.5, lambda a: E.escreve(c, "é 15", 1130, 240, 104, "g", COR, a))
    fica(c, t, ta, tc - 0.5, P("uma barra de") + P("chocolate", "g", 76, COR), W / 2, 200, "center")

    # a barra
    pinta = [(COR, prog(t, t6a + i * 0.25, 0.4)) if t >= t6a else None for i in range(3)] + [None]
    vinte(c, y, h, abre if t >= t5a else 0, pinta, ep(t, ta, 0.5), ep(t, tb - 0.1, 0.8))

    def total():
        chave(c, x_parte(0, 0), x_parte(0, 0) + 4 * W5, y + h + 14, TINTA2, ep(t, tb, 0.5))
        E.foco(c, t, tb + 0.1, 0.4, lambda a: centro(c, "20 quadradinhos", W / 2, y + h + 104, 72, "g", TINTA, a))
    E.saida(c, t, t5a - 0.15, total)

    # cada parte tem 5
    for i in range(4):
        x0 = x_parte(i, 1)
        chave(c, x0 + 6, x0 + W5 - 6, y + h + 14, COR if i < 3 and t >= t6a else TINTA2, ep(t, t5b + i * 0.1, 0.4))
        E.foco(c, t, t5b + 0.1 + i * 0.1, 0.4, lambda a, i=i, x0=x0: centro(c, "5", x0 + W5 / 2, y + h + 110, 84, "g", COR if i < 3 and t >= t6a else TINTA2, a))

    # as contas
    yc = 860
    fica(c, t, t5a, t5b - 1.3, P("o de baixo é 4:", size=72) + P("4 partes", "g", 66, COR), XE, yc, passo=0.14)
    conta(c, t, "20 ÷ 4 =", t5b - 1.2, "5", t5b + 0.5, XE, yc, 84)
    E.foco(c, t, t6a, 0.4, lambda a: E.escreve(c, "3 partes", 720, yc - 100, 60, "b", COR, a))
    conta(c, t, "3 × 5 =", t6b - 1.0, "15", t6b, 720, yc, 84, COR)
    E.foco(c, t, t6c, 0.5, lambda a: (E.bola(c, 1520, yc - 30, 118, a=a), centro(c, "15", 1520, yc + 18, 130, "g", BR, a)))


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    s8 = C["s08"]
    ta, tb, tc, td = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]

    def regra():
        E.frase(c, t, C["s07"] + 0.3, P("toda fração de uma quantidade", size=80, cor=COR), XE, 170, passo=0.13)
        for i, (t0, v, r, y) in enumerate(((ta, "divide", "pelo de baixo", 380), (tb, "multiplica", "pelo de cima", 660))):
            E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 56, y - 36, 56, a=a), centro(c, str(i + 1), XE + 56, y - 12, 66, "g", BR, a)))
            E.frase(c, t, t0 + 0.1, [(v, "g", 112, COR), (r, "i", 112)], XE + 150, y, passo=0.25)
        E.frase(c, t, tc - 0.9, P("acha o tamanho de", size=72) + P("uma parte", "g", 66, COR), XE + 150, 480, passo=0.13)
        E.frase(c, t, td - 0.9, P("junta", size=72) + P("as partes que você quer", "g", 66, COR), XE + 150, 760, passo=0.13)
        cx, cy, s = 1560, 480, 240
        cn, cd = E.mix(TINTA, COR, ep(t, tb, 0.4)), E.mix(TINTA, COR, ep(t, ta, 0.4) * (1 - ep(t, tb, 0.4)))

        def frac(a):
            E.fracao(c, 3, 4, cx, cy, s, TINTA, a)
            centro(c, "3", cx, cy - s * 0.2, s, "g", cn, a)
            centro(c, "4", cx, cy + s * 0.9, s, "g", cd, a)
        E.foco(c, t, ta, 0.5, frac)
    E.saida(c, t, s8 - 0.1, regra)
    if t < s8 - 0.1:
        return

    # com dinheiro: uma conta de R$ 300
    a_, b_, c_, d_ = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    x, y, w, h = 260, 340, 1400, 190
    lp = w / 5
    E.frase(c, t, s8 + 0.2, P("com") + P("dinheiro", "g", 76, COR) + P("é igual"), XE, 160)
    E.frase(c, t, a_, P("uma conta de") + P("R$ 300", "g", 84, COR), XE, 270, passo=0.14)
    E.frase(c, t, b_, P("você pagou"), 1040, 270)
    E.foco(c, t, b_ + 0.2, 0.5, lambda a: E.fracao(c, 2, 5, 1470, 230, 96, COR, a))
    ped = [(i, COR, prog(t, d_ - 0.2 + i * 0.2, 0.4)) for i in range(2)]
    chocolate(c, x, y, w, h, 5, ped, ep(t, a_, 0.5), ep(t, b_ + 0.6, 0.8))
    for i in range(5):
        E.foco(c, t, c_ + i * 0.1, 0.3, lambda a, i=i: centro(c, "60", x + lp * (i + 0.5), y + 126, 84, "g", BR if i < 2 and t >= d_ else TINTA2, a), sobe=0, blur=6)
    yc = 760
    conta(c, t, "300 ÷ 5 =", c_ - 1.2, "60", c_, XE, yc, 84)
    conta(c, t, "60 × 2 =", d_ - 1.0, "120", d_, XE, yc + 130, 84, COR)
    E.foco(c, t, d_, 0.5, lambda a: (M.rrect(c, 980, 730, 680, 180, 90, COR, a), centro(c, "R$ 120", 1320, 862, 120, "g", BR, a)))


# ---------------- o caminho de volta ----------------
def b_volta(c, t, C, b):
    s9, s10, s11, s12 = C["s09"], C["s10"], C["s11"], C["s12"]
    x, y, w, h = 260, 290, 1400, 180
    lp = w / 5

    def pergunta():
        E.frase(c, t, s9 + 0.3, P("voltando à pergunta do começo", size=84, cor=COR), W / 2, 190, "center", passo=0.14)
        E.frase(c, t, C["s09.a"], P("aqui você", size=110) + P("não tem o total", "g", 100, ERRADO), W / 2, 450, "center", passo=0.18)
        E.frase(c, t, C["s09.b"], P("você tem", size=110) + P("a parte", "g", 100, COR), W / 2, 620, "center", passo=0.18)
        yy = 800
        fr(c, t, C["s09.b"] + 0.6, 2, 5, 560, yy, 120, COR)
        E.frase(c, t, C["s09.b"] + 0.9, P("do salário", size=92) + P("=", "g", 84) + P("R$ 600", "g", 104, COR), 680, yy + 30, passo=0.15)
    E.saida(c, t, s10 - 0.1, pergunta)
    if t < s10 - 0.1:
        return

    def salario():
        ta, tb, tc, td = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        t1a, t1b = C["s11.a"], C["s11.b"]
        E.saida(c, t, s11 - 0.1, lambda: E.frase(c, t, s10 + 0.2, P("desenhe o") + P("salário", "g", 76, COR), W / 2, 170, "center"), d=0.3)
        ped = [(i, COR, prog(t, tb + i * 0.2, 0.4)) for i in range(2)] + [(i, TINTA2, prog(t, t1a + (i - 2) * 0.2, 0.4)) for i in (2, 3, 4)]
        chocolate(c, x, y, w, h, 5, ped, ep(t, ta, 0.5), ep(t, ta + 0.2, 0.9))
        yc = y + h + 14

        def duas():
            chave(c, x + 8, x + lp * 2 - 8, yc, COR, ep(t, tb, 0.4))
            E.foco(c, t, tb + 0.1, 0.4, lambda a: centro(c, "duas partes: R$ 600", x + lp, yc + 88, 62, "b", COR, a))
        E.saida(c, t, s11 - 0.1, duas)
        for i in range(5):
            t0 = td + i * 0.1 if i < 2 else t1a + (i - 2) * 0.2
            E.foco(c, t, t0, 0.3, lambda a, i=i: centro(c, "300", x + lp * (i + 0.5), y + 120, 88, "g", BR, a), sobe=0, blur=6)
        yy = 740
        E.foco(c, t, tc, 0.5, lambda a: E.escreve(c, "600 ÷ 2 =", XE, yy, 96, "g", TINTA, a))
        E.foco(c, t, td, 0.5, lambda a: E.escreve(c, "R$ 300", XE + 470, yy, 96, "g", COR, a))
        E.foco(c, t, td + 0.2, 0.4, lambda a: E.escreve(c, "uma parte", XE + 840, yy, 76, "i", TINTA, a))
        # o inteiro são cinco partes
        chave(c, x, x + w, y - 14, TINTA, ep(t, t1a, 0.5), h=-20)
        E.foco(c, t, t1a + 0.1, 0.4, lambda a: centro(c, "o salário inteiro: 5 partes", W / 2, y - 54, 66, "b", TINTA, a))
        E.foco(c, t, t1b - 1.0, 0.5, lambda a: E.escreve(c, "5 × 300 =", XE, yy + 170, 96, "g", TINTA, a))
        E.foco(c, t, t1b, 0.5, lambda a: (M.rrect(c, 680, yy + 60, 640, 170, 85, CERTO, a), centro(c, "R$ 1.500", 1000, yy + 186, 110, "g", BR, a)))
    E.saida(c, t, s12 - 0.1, salario)
    if t < s12 - 0.1:
        return

    # virou do avesso, e a conferência
    ta, tb, tc, td = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    E.frase(c, t, s12 + 0.2, P("a conta virou") + P("do avesso", "g", 76, COR), XE, 170)
    E.foco(c, t, s12 + 0.3, 0.5, lambda a: E.fracao(c, 2, 5, 1560, 170, 96, COR, a))
    E.frase(c, t, ta, [("divide", "g", 96, COR), ("pelo de cima", "i", 104)], XE, 340, passo=0.2)
    E.frase(c, t, tb, [("multiplica", "g", 96, COR), ("pelo de baixo", "i", 104)], XE, 480, passo=0.2)
    p = ep(t, tc - 1.1, 0.5)
    E.caixa_pontilhada(c, XE, 570, 1580, 360, p, prog_=p)
    E.frase(c, t, tc - 1.0, P("confira", size=72, cor=COR), XE + 50, 650)
    conta(c, t, "1.500 ÷ 5 =", tc, "300", lerp(tc, td, 0.75), XE + 50, 760, 84)
    conta(c, t, "300 × 2 =", td, "600", td + 0.7, XE + 50, 880, 84)
    E.foco(c, t, td + 1.2, 0.5, lambda a: (E.bola(c, 1490, 750, 130, CERTO, a), centro(c, "bateu!", 1490, 772, 66, "g", BR, a)))


# ---------------- qual caminho ----------------
def b_escolha(c, t, C, b):
    s14 = C["s14"]
    ta, tb, tc = C["s13.a"], C["s13.b"], C["s13.c"]

    def pergunta():
        E.frase(c, t, C["s13"] + 0.3, P("qual caminho usar?", size=96, cor=COR), W / 2, 180, "center", passo=0.16)
        E.frase(c, t, ta - 0.3, P("pergunte:", size=76), W / 2, 310, "center")
        E.frase(c, t, ta, P("o número que eu tenho é o", size=96) + P("total", "g", 88, COR) + P("ou a", size=96) + P("parte?", "g", 88, COR), W / 2, 430, "center", passo=0.15)
        for x, t0, l1, l2, l3 in ((170, tb, "tem o total", "divide pelo", "de baixo"), (990, tc, "tem a parte", "divide pelo", "de cima")):
            p = ep(t, t0, 0.5)
            E.caixa_pontilhada(c, x, 520, 760, 400, p, prog_=p)
            E.frase(c, t, t0 + 0.1, [(l1, "g", 92, COR)], x + 50, 640)
            E.frase(c, t, t0 + 0.3, [(l2, "i", 88)], x + 50, 760)
            E.frase(c, t, t0 + 0.4, [(l3, "g", 84)], x + 50, 860)
    E.saida(c, t, s14 - 0.1, pergunta)
    if t < s14 - 0.1:
        return

    # frases parecidas, contas opostas
    a_, b_, c_, d_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, s14 + 0.2, P("frases parecidas,") + P("caminhos diferentes", "g", 76, COR), W / 2, 160, "center", passo=0.14)
    M.line(c, W / 2, 240, W / 2, 960, FIO, ep(t, a_, 0.5), 3)
    colunas = ((XE - 20, a_, b_, "de 80 balas", "80 é o total", "80 ÷ 4 = 20", "20 × 3 =", "60", TINTA), (1000, c_, d_, "são 60 balas", "60 é a parte", "60 ÷ 3 = 20", "20 × 4 =", "80", COR))
    for x, t0, t1, frase, tipo, l1, l2, res, cor in colunas:
        E.foco(c, t, t0, 0.5, lambda a, x=x: E.fracao(c, 3, 4, x + 64, 330, 96, COR, a))
        E.frase(c, t, t0 + 0.2, [(frase, "i", 84)], x + 150, 362)
        E.frase(c, t, lerp(t0, t1, 0.3), [(tipo, "g", 76, COR)], x, 520)
        E.foco(c, t, lerp(t0, t1, 0.55), 0.5, lambda a, l1=l1, x=x: E.escreve(c, l1, x, 660, 76, "g", TINTA2, a))
        E.foco(c, t, lerp(t0, t1, 0.8), 0.5, lambda a, l2=l2, x=x: E.escreve(c, l2, x, 790, 76, "g", TINTA2, a))
        E.foco(c, t, t1, 0.5, lambda a, x=x, res=res: (E.bola(c, x + 540, 760, 104, a=a), centro(c, res, x + 540, 800, 110, "g", BR, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    s16, ta, tb, tc = C["s16"], C["s15.a"], C["s15.b"], C["s15.c"]

    def conta():
        E.frase(c, t, C["s15"] + 0.2, P("o") + P("erro", "g", 76, ERRADO) + P("do começo é pular essa pergunta"), W / 2, 180, "center", passo=0.14)
        E.frase(c, t, ta - 1.5, P("usa o caminho do total", size=80), W / 2, 340, "center", passo=0.14)
        y = 620
        E.foco(c, t, ta, 0.5, lambda a: E.escreve(c, "600 ÷ 5", 240, y, 130, "g", TINTA, a))
        E.foco(c, t, tb, 0.5, lambda a: E.escreve(c, "× 2", 800, y, 130, "g", TINTA, a))
        E.foco(c, t, tc, 0.5, lambda a: E.escreve(c, "= R$ 240", 1080, y, 130, "g", ERRADO, a))
    E.saida(c, t, s16 - 0.1, conta)
    if t < s16 - 0.1:
        return

    xa, xb, xc = C["s16.a"], C["s16.b"], C["s16.c"]
    E.saida(c, t, xc - 0.2, lambda: E.frase(c, t, s16 + 0.1, P("mas 600 é só") + P("uma parte", "g", 76, COR) + P("do salário"), W / 2, 180, "center"), d=0.3)
    E.frase(c, t, xc, P("o total é") + P("maior", "g", 76, CERTO) + P("que a parte"), W / 2, 180, "center")
    itens = [(600, "a parte: R$ 600", COR, xa), (240, "R$ 240 ?", ERRADO, xb)]
    tamanhos(c, t, XE, 320, 110, itens[:1])
    x, y, h = XE, 496, 110
    E.saida(c, t, xc + 0.5, lambda: tamanhos(c, t, x, y, h, itens[1:]), d=0.3)
    fica(c, t, xb + 0.5, xc - 0.1, P("o salário não pode ser") + P("menor", "g", 76, ERRADO) + P("que a parte"), W / 2, 780, "center")
    tamanhos(c, t, x, y, h, ((1500, "", CERTO, xc + 0.6),))
    E.foco(c, t, xc + 1.0, 0.5, lambda a: centro(c, "o salário inteiro: R$ 1.500", W / 2, 720, 72, "g", CERTO, a))
    E.frase(c, t, xc + 1.5, P("olhe sempre o tamanho da resposta", size=76, cor=COR), W / 2, 880, "center", passo=0.13)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s18, s19 = C["s18"], C["s19"]

    def titulo():
        E.frase(c, t, C["s17"] + 0.3, P("e o atalho prometido", cor=CLARO), W / 2, 240, "center")
        E.frase(c, t, C["s17.a"], P("tire o pedaço", "i", 130, BR) + P("que falta", "g", 120, BR), W / 2, 430, "center", passo=0.16)
        E.frase(c, t, C["s17.b"] - 1.8, P("quando a fração é", "i", 76, CLARO) + P("quase o inteiro", "g", 70, BR), W / 2, 600, "center", passo=0.14)
        y = 790
        fr(c, t, C["s17.b"], 4, 5, 700, y, 130, BR)
        E.frase(c, t, C["s17.b"] + 0.4, P("de", "i", 100, CLARO) + P("400", "g", 100, BR), 810, y + 34, passo=0.2)
    E.saida(c, t, s18 - 0.1, titulo)
    if t < s18 - 0.1:
        return

    def barra_400():
        ta, tb, tc, td = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
        x, y, w, h = 260, 220, 1400, 170
        lp = w / 5
        E.frase(c, t, s18 + 0.2, P("ache só", "i", 84, CLARO) + P("um quinto", "g", 76, BR), W / 2, 150, "center")
        sai = ep(t, tb, 0.6)
        ped = [(i, CLARO, prog(t, tb - 1.7 + i * 0.1, 0.3)) for i in range(4)] + [(4, "#FFFFFF", prog(t, ta, 0.4) * (1 - sai), 140 * sai)]
        chocolate(c, x, y, w, h, 5, ped, ep(t, s18 + 0.2, 0.5), 1.0, escuro=True)
        E.saida(c, t, tb + 0.2, lambda: E.foco(c, t, ta, 0.4, lambda a: centro(c, "80", x + lp * 4.5, y + 112, 92, "g", E.COR, a), sobe=0, blur=6), d=0.25)
        chave(c, x + 8, x + lp * 4 - 8, y + h + 14, CLARO, ep(t, tb - 1.7, 0.4))
        E.foco(c, t, tb - 1.6, 0.4, lambda a: centro(c, "tudo, menos um quinto", x + lp * 2, y + h + 96, 62, "i", BR, a))
        yy = 660
        E.foco(c, t, tb, 0.5, lambda a: E.escreve(c, "400 − 80 =", 330, yy, 130, "g", BR, a))
        E.foco(c, t, tc, 0.5, lambda a: (E.bola(c, 1270, yy - 42, 135, CERTO, a), centro(c, "320", 1270, yy - 2, 120, "g", BR, a)))
        E.frase(c, t, td - 1.8, P("nos 20 quadradinhos:", "i", 76, CLARO), 330, 880, passo=0.13)
        conta(c, t, "20 − 5 =", td, "15", td + 1.0, 1000, 880, 92, BR, CERTO)
    E.saida(c, t, s19 - 0.1, barra_400)
    if t < s19 - 0.1:
        return

    ta, tb, tc = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, ta - 0.6, P("funciona porque", "i", 80, CLARO), W / 2, 190, "center")
    E.frase(c, t, ta, P("falta só", "i", 104, CLARO) + P("uma parte", "g", 96, BR), W / 2, 330, "center", passo=0.16)
    E.frase(c, t, ta + 2.0, P("e subtrair é", "i", 76, CLARO) + P("mais rápido", "g", 70, BR), W / 2, 450, "center", passo=0.14)
    E.frase(c, t, tb - 1.2, P("não compensa quando", "i", 76, CLARO) + P("falta muito", "g", 70, BR), W / 2, 620, "center", passo=0.14)
    fr(c, t, tb, 2, 9, 330, 800, 130, BR)
    E.frase(c, t, tc, P("divida e multiplique", "g", 84, BR) + P("normalmente", "i", 92, CLARO), 480, 830, passo=0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ta, tb, tc = C["s20.a"], C["s20.b"], C["s20.c"]
    E.frase(c, t, C["s20"] + 0.3, P("hora de testar", size=72, cor=COR), XE, 170)
    E.frase(c, t, ta - 0.9, P("um tanque de combustível", size=76), XE, 300, passo=0.14)
    E.frase(c, t, ta - 0.5, P("está com", size=84), XE, 470, passo=0.14)
    E.foco(c, t, ta, 0.5, lambda a: E.fracao(c, 3, 4, 500, 435, 110, COR, a))
    E.frase(c, t, ta + 0.4, P("da capacidade", size=84), 590, 470, passo=0.14)
    E.frase(c, t, tb - 0.2, P("o que dá", size=84) + P("36 litros", "g", 100, COR), XE, 630, passo=0.14)
    E.foco(c, t, ta, 0.6, lambda a: tanque(c, 1095, 230, 190, 480, 4, 3, a))
    E.frase(c, t, tc, P("quantos litros cabem no", size=100) + P("tanque cheio?", "g", 90, COR), XE, 860, passo=0.15)
    relogio(c, t, C["s21.a"], 1555, 340)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ta, tb, tc, td = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]
    x, y, w, h = 300, 200, 1320, 170
    lp = w / 4
    ped = [(i, COR, prog(t, ta + i * 0.15, 0.35)) for i in range(3)] + [(3, CERTO, prog(t, td, 0.4))]
    chocolate(c, x, y, w, h, 4, ped, ep(t, C["s22"] + 0.2, 0.5), 1.0)
    yc = y + h + 14

    def parte():
        chave(c, x + 8, x + lp * 3 - 8, yc, COR, ep(t, ta, 0.4))
        E.foco(c, t, ta + 0.1, 0.4, lambda a: centro(c, "36 litros: a parte", x + lp * 1.5, yc + 88, 66, "g", COR, a))
    E.saida(c, t, td - 0.15, parte, d=0.3)
    for i in range(4):
        t0 = tb + 1.6 + i * 0.1 if i < 3 else td
        E.foco(c, t, t0, 0.3, lambda a, i=i: centro(c, "12", x + lp * (i + 0.5), y + 118, 96, "g", BR, a), sobe=0, blur=6)
    chave(c, x, x + w, y - 14, TINTA, ep(t, tc, 0.5), h=-20)
    E.foco(c, t, tc + 0.1, 0.4, lambda a: centro(c, "o tanque: 4 partes", W / 2, y - 54, 62, "b", TINTA, a))
    conta(c, t, "36 ÷ 3 =", tb, "12", tb + 1.6, XE, 680, 96)
    E.foco(c, t, tb + 1.8, 0.4, lambda a: E.escreve(c, "cada parte", 790, 680, 72, "i", TINTA, a))
    conta(c, t, "12 × 4 =", tc, "48", td, XE, 830, 96, COR)
    E.foco(c, t, td, 0.5, lambda a: (M.rrect(c, 1100, 630, 560, 210, 105, CERTO, a), centro(c, "48 litros", 1380, 765, 106, "g", BR, a)))
    E.frase(c, t, td + 1.0, P("maior que a parte:") + P("faz sentido", "g", 76, CERTO), W / 2, 970, "center", passo=0.14)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    s24 = C["s24"]

    def resumo():
        E.frase(c, t, C["s23"] + 0.3, P("resumindo", size=92, cor=COR), W / 2, 170, "center")
        for i, (t0, l1, l2, l3) in enumerate(((C["s23.a"], "tem o total", "÷ pelo de baixo", "× pelo de cima"), (C["s23.b"], "tem a parte", "÷ pelo de cima", "× pelo de baixo"))):
            x = 170 + i * 820
            p = ep(t, t0, 0.5)
            E.caixa_pontilhada(c, x, 280, 760, 520, p, prog_=p)
            E.frase(c, t, t0 + 0.1, [(l1, "g", 96, COR)], x + 50, 420)
            E.frase(c, t, t0 + 0.3, [(l2, "b", 76, TINTA)], x + 50, 570)
            E.frase(c, t, t0 + 0.5, [(l3, "b", 76, TINTA)], x + 50, 690)
    E.saida(c, t, s24 - 0.1, resumo)
    if t < s24 - 0.1:
        return

    ta, tb, tc, td = C["s24.a"], C["s24.b"], C["s24.c"], C["s24.d"]
    E.frase(c, t, s24 + 0.2, P("próxima aula"), XE, 190)
    E.frase(c, t, s24 + 0.8, P("Frações", "g", 112, COR), XE, 320)
    E.frase(c, t, s24 + 1.1, P("equivalentes", "g", 112, COR), XE, 440)
    y = 640
    for i, (n, d) in enumerate(((1, 2), (2, 4), (3, 6))):
        fr(c, t, ta + i * 0.5, n, d, 250 + i * 240, y, 104, COR if i == 0 else None)
        if i:
            sinal(c, t, ta + i * 0.5 - 0.1, "=", 130 + i * 240, y, 84)
    E.frase(c, t, tb, P("e como", size=88) + P("simplificar", "g", 84, COR), 860, y + 30, passo=0.15)
    E.foco(c, t, tc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 300, 84, estilo="g", cor=BR, a=a))
    p = ease_io(prog(t, tc + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1620, p), lerp(560, 340, p), ep(t, tc + 0.2, 0.4), cor=TINTA)
    E.frase(c, t, td, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barra=b_barra, regra=b_regra, volta=b_volta, escolha=b_escolha, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
