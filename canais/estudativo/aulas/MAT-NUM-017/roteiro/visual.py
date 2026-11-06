"""Visual — Estudativo · MAT-NUM-017: multiplicar e dividir inteiros, regra de sinais.
Identidade em _ferramentas/editorial.py. A imagem central é tirar uma dívida é como ganhar (E.divida, com cancela).
Peças locais: nota (cédula), pessoa e fila_dividas (fileira de cartões que podem ser cancelados)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-017_regra_de_sinais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("casos", "dividir", "atalho", "questao", "fim"))
BR = "#FFFFFF"
sn = lambda v: str(v).replace("-", "−")  # o menos da tela


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def pal(s, estilo="i", size=84, cor=TINTA):
    """frase em palavras, para entrar uma a uma"""
    return [(p, estilo, size, cor) for p in s.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def xpos(s, i, size):
    """x do caractere i dentro de s, escrito na grotesca pesada"""
    return E.larg(s[:i], "g", size) + (E.APERTO["g"] * size if i else 0)


def nota(c, x, y, w, h, s, a=1.0):
    """cédula na cor da matéria (peça local, a mesma de MAT-FRA-015)"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 22, E.COR, a)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 16, y + 16, w - 32, h - 32), 12, 12)
    c.drawRRect(r, M.paint(E.SOBRE, 0.55 * a, stroke=4))
    E.centro(c, s, x + w / 2, y + h / 2 + h * 0.13, h * 0.38, "g", E.SOBRE, a)


def pessoa(c, cx, cy, r, a=1.0):
    """pessoa simples: cabeça e ombros (peça local)"""
    if a <= 0:
        return
    E.bola(c, cx, cy - r * 0.9, r * 0.62, a=a)
    M.rrect(c, cx - r, cy - r * 0.1, 2 * r, r * 1.1, r * 0.6, E.COR, a)


def fila_dividas(c, t, ts, cx0, dx, y, w, h, v, canc=None):
    """fileira de dívidas: ts = instante de cada cartão; canc = {índice: instante do cancelamento} (peça local)"""
    for i, ti in enumerate(ts):
        k = ease_io(prog(t, canc[i], 0.5)) if canc and i in canc else 0.0
        E.foco(c, t, ti, 0.45, lambda a, i=i, k=k: E.divida(c, cx0 + i * dx, y, w, h, v, a, k))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
        fim = C["s01.end"]
        y, s = 360, 150
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "(−4) × (−3)", XE, y, s, "g", TINTA, a))
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "= +12", 1120, y, s, "g", CERTO, a))
        E.frase(c, t, lerp(kb, kc, 0.3), pal("duas coisas negativas viram", size=84) + pal("dinheiro", "g", 84, COR) + pal("no bolso?", size=84), W / 2, 580, "center", passo=0.1)
        E.frase(c, t, lerp(kb, kc, 0.78), pal("decorar", size=100) + [("não", "g", 100, ERRADO), ("ajuda", "g", 100, ERRADO)], 500, 790, "center", passo=0.1)
        E.frase(c, t, kc, [("entender,", "g", 110, CERTO), ("sim", "g", 110, CERTO)], 1370, 790, "center", passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 520, 280 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, pal("até o fim desta aula", size=90), XE, 330)
        E.frase(c, t, lerp(ta, tb, 0.4), [("multiplica", "g", 124)], XE, 480)
        E.frase(c, t, lerp(ta, tb, 0.5), pal("e", size=110) + [("divide", "g", 124)] + pal("com", size=110) + [("sinal", "g", 124, COR)], XE, 630, passo=0.1)
        E.frase(c, t, lerp(ta, tb, 0.75), pal("sabendo o", size=100) + [("motivo", "g", 110, COR)], XE, 780, passo=0.1)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1490, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1490, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ka = C["s03.a"]
    E.frase(c, t, C["s03"] + 0.1, pal("você só precisa de"), XE, 410)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ka + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w, y0, dy = 960, 780, 190, 240
    itens = (("s03.b", "saber", "a tabuada"), ("s03.c", "a prova real:", "multiplicar de volta"), ("s03.d", "tirar uma dívida", "é como ganhar"))
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))


# ---------------- casos ----------------
def b_casos(c, t, C, b):
    def caso1():
        ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
        E.frase(c, t, C["s04"] + 0.1, pal("multiplicar é", size=88) + [("repetir", "g", 88, COR)], W / 2, 170, "center", passo=0.1)
        y, s = 370, 140
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "(−4) × 3", 360, y, s, "g", TINTA, a))
        E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "= −12", 1030, y, s, "g", ERRADO, a))
        fila_dividas(c, t, (kb, kb + 0.5, kb + 1.0), 520, 440, 610, 360, 200, "R$ 4")
        for x, ti in ((740, kb + 0.5), (1180, kb + 1.0)):
            E.foco(c, t, ti, 0.4, lambda a, x=x: E.centro(c, "+", x, 640, 90, "g", ERRADO, a))
        E.frase(c, t, kd, [("3 × (−4)", "g", 96)] + pal("também dá", size=80) + [("−12", "g", 96, ERRADO)], W / 2, 900, "center", passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, caso1)

    def caso2():
        ka, kb, kc = C["s05.a"], C["s05.b"], C["s05.c"]
        E.frase(c, t, C["s05"] + 0.1, pal("e se o", size=84) + [("quantas", "g", 84, COR), ("vezes", "g", 84, COR)] + pal("for negativo?", size=84), W / 2, 170, "center", passo=0.1)
        E.frase(c, t, ka, pal("o menos", size=92) + [("inverte", "g", 92, COR), ("a", "g", 92, COR), ("ação:", "g", 92, COR)] + pal("em vez de pôr, você tira", size=84), W / 2, 310, "center", passo=0.09)
        y, s = 530, 140
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "4 × (−3)", 360, y, s, "g", TINTA, a))
        E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "= −12", 1030, y, s, "g", ERRADO, a))
        for i in range(3):
            xn = 470 + i * 360
            ti = lerp(kb, kc, 0.3 + i * 0.2)
            E.foco(c, t, ti, 0.45, lambda a, xn=xn: (nota(c, xn, 690, 260, 140, "R$ 4", a), E.centro(c, "tirou", xn + 130, 900, 62, "i", ERRADO, a)))
            E.risco(c, xn - 20, 840, xn + 280, 680, t, ti + 0.3, largura=10)
    if C["s05"] - 0.1 <= t:
        E.saida(c, t, C["s06"] - 0.1, caso2)

    def caso3():
        ka, kb, kc, kd = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        E.frase(c, t, C["s06"] + 0.1, pal("e se o que você tira é", size=88) + [("dívida?", "g", 88, ERRADO)], W / 2, 170, "center", passo=0.1)
        ts = tuple(ka + i * 0.16 for i in range(5))
        canc = {i: kc + 0.3 * (i - 2) for i in (2, 3, 4)}
        fila_dividas(c, t, ts, 400, 280, 420, 260, 190, "R$ 4", canc)
        E.frase(c, t, ka + 0.5, [("5", "g", 76)] + pal("dívidas de", size=72) + [("4", "g", 76)] + pal("reais", size=72), W / 2, 630, "center", passo=0.1)
        E.frase(c, t, kb, pal("saldo:", size=88) + [("−20", "g", 110, ERRADO)], 620, 820, "center", passo=0.1)
        E.frase(c, t, kc, pal("a loja", size=76) + [("cancela", "g", 80, COR), ("3", "g", 80, COR)], 1340, 790, "center", passo=0.1)
        E.frase(c, t, kd, pal("sobram 2, saldo:", size=76) + [("−8", "g", 96, ERRADO)], 1340, 910, "center", passo=0.1)
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, caso3)

    def caso4():
        ka, kb, kc, kd = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
        fim = C["s07.end"]
        y = 320
        vx = E.reta(c, t, C["s07"], 300, 1620, y, -22, -6, (-20, -16, -12, -8), fmt=sn, size=52)
        E.bola(c, vx(-20), y, 24 * ease_back(prog(t, C["s07"], 0.5)), ERRADO)
        E.bola(c, vx(-8), y, 24 * ease_back(prog(t, C["s07"] + 0.2, 0.5)), CERTO)
        E.salto(c, t, ka, vx(-20), vx(-8), y, 110, CERTO, "o saldo subiu 12", size=70)
        E.frase(c, t, kb, [("−20 + 12 = −8", "g", 100)], W / 2, 560, "center")
        E.foco(c, t, kb + 0.8, 0.5, lambda a: E.selo(c, 1380, 525, 56, True, a))
        yy = 770
        E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "(−4) × (−3)", XE, yy, 120, "g", TINTA, a))
        E.foco(c, t, kd, 0.5, lambda a: E.escreve(c, "= +12", 1000, yy, 120, "g", CERTO, a))
        E.frase(c, t, lerp(kc, kd, 0.3), [("−4:", "g", 64, COR)] + pal("a dívida", size=64), 1400, 700, passo=0.08)
        E.frase(c, t, lerp(kc, kd, 0.6), [("× (−3):", "g", 64, COR)] + pal("tirar 3", size=64), 1400, 790, passo=0.08)
        E.frase(c, t, lerp(kd, fim, 0.4), [("tirar", "g", 84, COR), ("uma", "g", 84, COR), ("dívida", "g", 84, COR)] + pal("é como", size=84) + [("ganhar", "g", 84, CERTO)], W / 2, 950, "center", passo=0.1)
    if C["s07"] - 0.1 <= t:
        E.saida(c, t, C["s08"] - 0.1, caso4)

    def tabela():
        ka, kb, kc, kd, ke = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"]
        E.frase(c, t, C["s08"] + 0.1, pal("juntando", size=88) + [("tudo", "g", 88, COR)], W / 2, 170, "center", passo=0.1)
        for k, s, cor, x, y in ((ka, "+ × + = ", CERTO, 300, 340), (kb, "− × − = ", CERTO, 300, 510), (kc, "+ × − = ", ERRADO, 1040, 340), (kd, "− × + = ", ERRADO, 1040, 510)):
            r = "+" if cor == CERTO else "−"
            E.foco(c, t, k, 0.5, lambda a, s=s, x=x, y=y, r=r, cor=cor: (E.escreve(c, s, x, y, 130, "g", TINTA, a), E.escreve(c, r, x + E.larg(s, "g", 130) + 24, y, 130, "g", cor, a)))
        E.frase(c, t, ke, pal("multiplicando ou dividindo,", size=76), W / 2, 660, "center", passo=0.1)
        E.frase(c, t, ke + 0.9, pal("sinais iguais dão", size=92) + [("mais", "g", 92, CERTO)], W / 2, 790, "center", passo=0.1)
        E.frase(c, t, ke + 1.8, pal("sinais diferentes dão", size=92) + [("menos", "g", 92, ERRADO)], W / 2, 920, "center", passo=0.1)
    if C["s08"] - 0.1 <= t:
        E.saida(c, t, C["s09"] - 0.1, tabela)

    if t >= C["s09"]:
        ka, kb, kc, kd, ke = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
        E.frase(c, t, ka, [("dois", "g", 88, COR), ("passos:", "g", 88, COR)] + pal("primeiro o sinal, depois a conta", size=84), W / 2, 190, "center", passo=0.09)
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "(−6) × 7", W / 2, 430, 160, "g", TINTA, a))
        x = 300
        E.foco(c, t, kc, 0.5, lambda a: E.bola(c, x + 56, 590, 56, a=a))
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "1", x + 56, 613, 64, "g", E.SOBRE, a))
        E.frase(c, t, kc, pal("sinais diferentes:", size=80) + [("negativo", "g", 80, ERRADO)], x + 140, 615, passo=0.1)
        E.foco(c, t, kd, 0.5, lambda a: E.bola(c, x + 56, 760, 56, a=a))
        E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "2", x + 56, 783, 64, "g", E.SOBRE, a))
        E.frase(c, t, kd, [("6 × 7 = 42", "g", 96)], x + 140, 790)
        bola_txt(c, t, ke, "−42", 1500, 750, 130, 96, ERRADO)


# ---------------- dividir ----------------
def b_dividir(c, t, C, b):
    def d1():
        ka, kb, kc, kd = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        fim = C["s10.end"]
        y, s = 280, 130
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "(−20) ÷ 4", 420, y, s, "g", TINTA, a))
        E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "= −5", 1100, y, s, "g", ERRADO, a))
        for i, x in enumerate((420, 780, 1140, 1500)):
            ti = kb + i * 0.2
            E.foco(c, t, ti, 0.45, lambda a, x=x: pessoa(c, x, 430, 62, a))
            E.foco(c, t, ti + 0.1, 0.45, lambda a, x=x: E.divida(c, x, 620, 280, 170, "R$ 5", a, topo="deve"))
        E.frase(c, t, kd, pal("prova real:", size=76) + [("4 × (−5) = −20", "g", 92)], W / 2, 830, "center", passo=0.1)
        E.foco(c, t, lerp(kd, fim, 0.42), 0.5, lambda a: E.selo(c, 1540, 800, 54, True, a))
        E.frase(c, t, lerp(kd, fim, 0.55), pal("com +5 não fecharia:", size=72) + [("4 × 5 = 20", "g", 76, ERRADO)], W / 2, 960, "center", passo=0.1)
    E.saida(c, t, C["s11"] - 0.1, d1)

    def d2():
        ka, kb, kc, kd = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "(−20) ÷ (−4)", W / 2, 230, 130, "g", TINTA, a))
        E.frase(c, t, kb, pal("quantas dívidas de", size=84) + [("4", "g", 88, ERRADO)] + pal("cabem em uma de", size=84) + [("20?", "g", 88, ERRADO)], W / 2, 370, "center", passo=0.09)
        fila_dividas(c, t, tuple(lerp(kb, kc, 0.55 + i * 0.07) for i in range(5)), 400, 280, 560, 250, 170, "R$ 4")
        E.frase(c, t, kc, pal("cabem 5, sinais iguais:", size=84) + [("+5", "g", 104, CERTO)], W / 2, 790, "center", passo=0.1)
        E.frase(c, t, kd, pal("prova real:", size=76) + [("5 × (−4) = −20", "g", 92)], W / 2, 930, "center", passo=0.1)
        E.foco(c, t, kd + 1.4, 0.5, lambda a: E.selo(c, 1540, 900, 54, True, a))
    if C["s11"] - 0.1 <= t:
        E.saida(c, t, C["s12"] - 0.1, d2)

    if t >= C["s12"]:
        ka, kb, kc = C["s12.a"], C["s12.b"], C["s12.c"]
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "20 ÷ (−4)", W / 2, 340, 170, "g", TINTA, a))
        E.frase(c, t, kb, pal("sinais diferentes:", size=92) + [("−5", "g", 120, ERRADO)], W / 2, 590, "center", passo=0.1)
        E.frase(c, t, kc, pal("prova real:", size=84) + [("(−4) × (−5) = 20", "g", 100)], W / 2, 790, "center", passo=0.1)
        E.foco(c, t, kc + 1.4, 0.5, lambda a: E.selo(c, W / 2, 900, 60, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    fim = C["s13.end"]
    E.frase(c, t, ka, [("cuidado:", "g", 88, ERRADO)] + pal("a regra é só para", size=88) + [("×", "g", 88, COR), ("e", "i", 88), ("÷", "g", 88, COR)], W / 2, 180, "center", passo=0.1)
    y, s = 400, 140
    E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "−4 − 3", 240, y, s, "g", TINTA, a))
    E.foco(c, t, kd, 0.5, lambda a: E.escreve(c, "= −7", 720, y, s, "g", ERRADO, a))
    E.frase(c, t, lerp(kb, kc, 0.5), pal("aqui não tem vezes", size=70), 240, 510, passo=0.08)
    E.foco(c, t, kc - 0.3, 0.5, lambda a: E.divida(c, 1320, 360, 280, 170, "R$ 4", a))
    E.foco(c, t, kc, 0.5, lambda a: E.divida(c, 1620, 360, 280, 170, "R$ 3", a))
    E.linha(c, t, [("3 − (−5)", "g", 110, TINTA, ke), ("vira mais por", "i", 80, TINTA, ke + 0.8), ("outro", "g", 80, COR, ke + 1.1), ("motivo", "g", 80, COR, ke + 1.3)], W / 2, 740, "center")
    E.frase(c, t, lerp(ke, fim, 0.72), pal("ali você", size=84) + [("tira", "g", 84, COR), ("uma", "g", 84, COR), ("dívida", "g", 84, COR)], W / 2, 890, "center", passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s = "(−2) × (−5) × (−1)"

    def conta():
        ka, kb, kc, kd, ke, kf = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"], C["s14.f"]
        fim = C["s14.end"]
        E.frase(c, t, ka, pal("o atalho:", size=84, cor=CLARO) + pal("conte os", size=84, cor=CLARO) + [("sinais", "g", 84, BR), ("de", "g", 84, BR), ("menos", "g", 84, BR)], W / 2, 170, "center", passo=0.09)
        cx, y, size = W / 2, 370, 120
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, s, cx, y, size, "g", BR, a))
        x0 = cx - E.larg(s, "g", size) / 2
        n = 0
        for i, ch in enumerate(s):
            if ch == "−":
                n += 1
                xm = x0 + xpos(s, i, size) + E.larg("−", "g", size) / 2
                E.foco(c, t, kc + (n - 1) * 0.15, 0.4, lambda a, xm=xm, n=n: (E.bola(c, xm, y + 80, 36, E.COR, a), E.centro(c, str(n), xm, y + 100, 56, "g", E.SOBRE, a)))
        E.frase(c, t, kc + 0.5, [("3", "g", 80, BR)] + pal("sinais", size=80, cor=CLARO), W / 2, 590, "center", passo=0.1)
        E.frase(c, t, kd, pal("ímpar:", size=76, cor=CLARO) + [("negativo", "g", 76, BR)], 560, 710, "center", passo=0.1)
        E.frase(c, t, lerp(kd, ke, 0.25), pal("par:", size=76, cor=CLARO) + [("positivo", "g", 76, BR)], 1360, 710, "center", passo=0.1)
        E.foco(c, t, ke, 0.5, lambda a: E.centro(c, "sem os sinais: 10", 720, 900, 84, "g", BR, a))
        bola_txt(c, t, kf, "−10", 1270, 870, 110, 88, ERRADO)
    E.saida(c, t, C["s15"] - 0.1, conta)

    if t >= C["s15"]:
        ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
        fim = C["s15.end"]
        E.frase(c, t, C["s15"] + 0.1, pal("funciona porque", size=84, cor=CLARO), W / 2, 170, "center")
        E.frase(c, t, ka, pal("cada", size=92, cor=CLARO) + [("dupla", "g", 92, BR)] + pal("de menos vira", size=92, cor=CLARO) + [("mais", "g", 92, BR)], W / 2, 320, "center", passo=0.1)
        E.frase(c, t, kb, pal("na contagem ímpar,", size=84, cor=CLARO) + pal("sobra", "g", 84, BR) + pal("um menos sem dupla", size=84, cor=CLARO), W / 2, 480, "center", passo=0.09)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 290, 680, 72, False, a))
        E.frase(c, t, kc, pal("só vale se a conta inteira for", size=76, cor=CLARO) + [("×", "g", 76, BR), ("e", "i", 76, CLARO), ("÷", "g", 76, BR)], 400, 700, passo=0.09)
        E.foco(c, t, lerp(kc, fim, 0.62), 0.5, lambda a: E.selo(c, 290, 860, 72, False, a))
        E.frase(c, t, lerp(kc, fim, 0.62), pal("com dois números, não compensa", size=76, cor=CLARO), 400, 880, passo=0.09)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s16"], pal("hora de testar", size=72, cor=COR), XE, 170)
    E.frase(c, t, ka - 0.2, pal("saldo:", size=92) + [("−42", "g", 100, ERRADO)] + pal("reais", size=92), XE, 310, passo=0.1)
    fila_dividas(c, t, tuple(kb + i * 0.14 for i in range(6)), 260, 186, 490, 172, 160, "R$ ?")
    E.frase(c, t, kb + 0.6, [("6", "g", 76)] + pal("parcelas iguais", size=76), XE, 660, passo=0.1)
    E.frase(c, t, kc, pal("a loja", size=88) + [("cancela", "g", 88, COR), ("2", "g", 88, COR)] + pal("parcelas", size=88), XE, 790, passo=0.1)
    E.frase(c, t, kd, pal("qual é o", size=104) + [("novo", "g", 104, COR), ("saldo?", "g", 104, COR)], XE, 930, passo=0.1)
    E.relogio(c, t, C["s17.a"], 1540, 380, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
    da, db, dc = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, ka - 0.4, pal("cada parcela:", size=72), XE, 220, passo=0.08)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "(−42) ÷ 6 = −7", 640, 225, 92, "g", TINTA, a))
    E.frase(c, t, kb - 0.4, pal("cancelar duas:", size=72), XE, 350, passo=0.08)
    E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "(−7) × (−2)", 640, 355, 92, "g", TINTA, a))
    E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "= +14", 1190, 355, 92, "g", CERTO, a))
    fila_dividas(c, t, tuple(ka + 0.3 + i * 0.12 for i in range(6)), 300, 264, 530, 240, 170, "R$ 7", {4: kb + 0.3, 5: kb + 0.6})
    y = 790
    E.frase(c, t, da - 0.4, pal("novo saldo:", size=76), XE, y - 10, passo=0.08)
    tb_ = db
    E.expressao(c, t, [("−42 + 14", "−42 + 14", da), ("−28", "−28", tb_)], [tb_], 860, y, 110, t0=da)
    E.frase(c, t, dc, pal("sobraram 4 parcelas de 7 reais:", size=72) + [("28", "g", 76, ERRADO)] + pal("reais de dívida", size=72), W / 2, 940, "center", passo=0.09)
    E.foco(c, t, dc + 1.6, 0.5, lambda a: E.selo(c, 1710, 905, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (k, s) in enumerate((("s20.a", "sinais iguais: mais"), ("s20.b", "sinais diferentes: menos"), ("s20.c", "a regra é de × e ÷"))):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 92)], 400, y)
        E.frase(c, t, lerp(C["s20.c"], C["s20.end"], 0.55), pal("com + e −, pense em", size=84) + [("dívida", "g", 84, COR)], W / 2, 900, "center", passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, pal("próxima aula"), XE, 270)
    E.frase(c, t, C["s21.a"], pal("junta", size=100) + [("tudo", "g", 110, COR)] + pal("em uma conta só", size=100), XE, 410, passo=0.12)
    E.frase(c, t, C["s21.b"], [("negativos", "g", 110)] + pal("e", size=100) + [("parênteses", "g", 110)], XE, 550, passo=0.12)
    E.frase(c, t, C["s21.c"], pal("na", size=96) + [("ordem", "g", 96, COR), ("certa", "g", 96, COR)] + pal("das operações", size=96), XE, 680, passo=0.12)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(990, 815, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], 700, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, casos=b_casos, dividir=b_dividir, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
