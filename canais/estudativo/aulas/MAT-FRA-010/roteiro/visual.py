"""Visual — Estudativo · MAT-FRA-010: fração do restante.
A alma da aula é a barra de doze quadradinhos (E.chocolate): cada gasto cai da barra e fica à vista, embaixo, com o valor.
O que sobra continua no lugar, então "fração de quê?" se responde olhando. O atalho das sobras fica no palco escuro."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, frac_q, centro
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-010_fracao_do_restante.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barra", "fracoes", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NY, DY = -0.565, 0.535  # centro do número de cima e do de baixo, em relação ao centro de uma fração de tamanho s

assert 1200 // 12 == 100 and 12 // 3 == 4 and 4 * 100 == 400 and 12 - 4 == 8 and 8 // 4 == 2 and 2 * 100 == 200
assert 12 - 4 - 2 == 6 and 6 * 100 == 600 and 400 + 200 == 600 and 1200 // 6 == 200
assert 1200 // 4 == 300 and 400 + 300 == 700 and 1200 - 700 == 500 and 1200 - 400 == 800
assert 90 // 5 == 18 and 90 * 2 // 5 == 36 and 90 - 36 == 54 and 54 * 2 // 3 == 36 and 54 - 36 == 18


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


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.2):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


def conta(c, t, ti, s, x, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def conta_c(c, t, ti, s, cx, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def corte(c, t, t0, cx, cy, s, novo, tn, baixo=False, risco=None, tinta=None):
    """corte em cruz no número centrado em (cx, cy): embaixo da fração, o valor novo desce para não bater no traço"""
    E.corta(c, t, t0, cx, cy, s, None, risco or COR)
    yb = cy + s * 0.8 if baixo else cy - s * 0.5
    E.foco(c, t, tn, 0.4, lambda a: E.escreve(c, str(novo), cx + s * 0.38, yb, s * 0.56, "g", tinta or COR, a), sobe=8)


def rotulo_sobre(c, t, t0, x0, x1, y, s, cor=TINTA2, size=56, sai=None):
    """colchete acima de um trecho da barra, com rótulo"""
    def fn():
        E.chave(c, x0, x1, y, cor, ep(t, t0, 0.4), -16, 4)
        conta_c(c, t, t0, s, (x0 + x1) / 2, y - 34, size, cor)
    E.saida(c, t, sai, fn) if sai is not None else fn()


def tanque(c, x, y, w, h, nivel, a=1.0):
    """caixa de água no palco: cinco partes e a água no nível 0..1"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22)
    c.drawRRect(rr, M.paint(BR, 0.07 * a))
    c.save(); c.clipRRect(rr, True)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * (1 - nivel), w, h * nivel), M.paint(CLARO, a))
    c.restore()
    for i in range(1, 5):
        yy = y + h * i / 5
        M.line(c, x, yy, x + w, yy, BR, 0.45 * a, 3, cap_round=False)
    c.drawRRect(rr, M.paint(BR, a, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def cena1():
        E.frase(c, t, a1, ps("salário de", "i", 96) + ps("R$ 1.200", "g", 110, COR), XE, 250)
        E.frase(c, t, b1 - 0.4, ps("gasta", "i", 96), XE, 450)
        fr(c, t, b1, 1, 3, 480, 420, 120, COR)
        E.frase(c, t, c1 - 0.5, ps("depois, gasta", "i", 96), XE, 650)
        fr(c, t, c1, 1, 4, 780, 620, 120, COR)
        E.frase(c, t, c1 + 0.5, ps("do que sobrou", "g", 96), 880, 650)
        E.frase(c, t, d1, ps("quanto", "i", 150) + ps("restou?", "g", 140, COR), XE, 900)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if C["s02"] <= t < C["s03"] + 0.3:
        a2, b2 = C["s02.a"], C["s02.b"]

        def cena2():
            E.frase(c, t, C["s02"] + 0.1, ps("se a sua resposta foi", "i", 84), W / 2, 200, "center", 0.26)
            E.foco(c, t, a2, 0.5, lambda a: centro(c, "R$ 500", W / 2, 400, 180, "g", ERRADO, a))
            E.frase(c, t, lerp(a2, b2, 0.3), ps("você caiu na armadilha mais comum", "i", 80), W / 2, 540, "center", 0.26)
            E.frase(c, t, b2, ps("do que sobrou", "g", 170, COR), W / 2, 830, "center")
            q = ep(t, b2 + 0.4, 0.5)
            E.caixa_pontilhada(c, 300, 680, 1320, 210, q, prog_=q)
            E.cursor(c, 1610, 880, q)
        E.saida(c, t, C["s03"] - 0.1, cena2)

    if t >= C["s03"]:
        a3, b3 = C["s03.a"], C["s03.b"]
        E.foco(c, t, b3 - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, b3 - 0.2, 0.7))), blur=0)
        E.frase(c, t, a3, ps("até o fim da aula", "i", 96), XE, 340)
        E.frase(c, t, lerp(a3, b3, 0.3), ps("fração", "g", 132), XE, 490)
        E.frase(c, t, lerp(a3, b3, 0.33), ps("do restante", "g", 118, COR), XE, 630)
        E.frase(c, t, lerp(a3, b3, 0.6), ps("com ou sem o valor em reais", "i", 70), XE, 760, passo=0.26)
        E.foco(c, t, b3 + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", E.SOBRE, a), E.escreve(c, "de prova", 1310, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, f_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.end"]
    E.frase(c, t, lerp(C["s04"], a_, 0.4), ps("você precisa de", "i", 84), XE, 410)
    E.foco(c, t, a_, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, a_ + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, a))
    x, w = 900, 830
    p = ep(t, b_, 0.5)
    E.caixa_pontilhada(c, x, 150, w, 290, p, prog_=p)
    E.frase(c, t, b_ + 0.1, ps("quanto falta", "g", 74, COR), x + 44, 245)
    E.frase(c, t, b_ + 0.4, ps("para um inteiro", "i", 70), x + 44, 325)
    conta(c, t, lerp(b_, c_, 0.3), "3/3 − 1/3 = 2/3", x + 44, 410, 62)
    p = ep(t, c_, 0.5)
    E.caixa_pontilhada(c, x, 490, w, 240, p, prog_=p)
    E.frase(c, t, c_ + 0.1, ps("multiplicar frações", "g", 74, COR), x + 44, 585)
    E.frase(c, t, lerp(c_, f_, 0.25), ps("de", "g", 66) + ps("vira", "i", 72) + ps("vezes", "g", 66), x + 44, 680)
    E.frase(c, t, lerp(c_, f_, 0.6), ps("faltou?", "g", 60, COR) + ps("procure a aula no canal", "i", 66), W / 2, 880, "center", 0.26)


# ---------------- a barra de doze quadradinhos ----------------
BX, BY, BW, BH = 216, 420, 1488, 150
LP = BW / 12
CAI = 190  # quanto um gasto desce


def trecho(i, j):
    """x de início e fim dos quadradinhos i..j-1"""
    return BX + i * LP, BX + j * LP


def b_barra(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"]
    # títulos, um por cena
    fica(c, t, a5, C["s06"] - 0.1, ps("fração de", "i", 128) + ps("quê?", "g", 124, COR), W / 2, 240, "center")
    E.saida(c, t, C["s07"] - 0.1, lambda: E.linha(c, t, [("primeiro gasto:", "i", 84, TINTA, C["s06"] + 0.1), ("1/3", "g", 80, COR, lerp(C["s06"], a6, 0.6)), ("do salário", "g", 80, TINTA, a6)], W / 2, 170, "center"))
    E.saida(c, t, C["s08"] - 0.1, lambda: E.linha(c, t, [("segundo gasto:", "i", 84, TINTA, C["s07"] + 0.1), ("1/4", "g", 80, COR, lerp(C["s07"], a7, 0.6)), ("do que sobrou", "g", 80, COR, a7)], W / 2, 170, "center"))
    E.frase(c, t, a8, ps("restaram", "i", 84) + ps("6 quadradinhos", "g", 80, CERTO), W / 2, 170, "center")
    # a barra: nasce inteira, em doze; cada gasto ganha a sua cor e cai
    tb = b5
    ped = []
    for i in range(12):
        q1 = ep(t, tb + 0.5 + i * 0.04, 0.3)
        if i < 4:
            q, dy = ep(t, b6 + i * 0.1, 0.4), CAI * ease_io(prog(t, c6, 0.7))
            cor = M.mix(CLARO, E.COR, q)
        elif i < 6:
            q, dy = ep(t, b7 + (i - 4) * 0.12, 0.4), CAI * ease_io(prog(t, c7, 0.7))
            cor = M.mix(CLARO, TINTA, q)
        else:
            q, dy = ep(t, a8 + (i - 6) * 0.06, 0.4), 0
            cor = M.mix(CLARO, CERTO, q)
        ped.append((i, cor, q1, dy, q > 0.5))
    E.foco(c, t, tb, 0.5, lambda a: E.chocolate(c, BX, BY, BW, BH, 12, [p[:4] for p in ped], a, ep(t, tb + 0.1, 0.7)))
    for i, cor, q1, dy, forte in ped:
        E.foco(c, t, c5 + i * 0.05, 0.3, lambda a, i=i, dy=dy, forte=forte: centro(c, "100", BX + (i + 0.5) * LP, BY + dy + BH / 2 + 17, 48, "g", BR if forte else TINTA, a), sobe=6)
    # s05: por que doze, e quanto vale cada um
    E.saida(c, t, C["s06"] - 0.1, lambda: conta_c(c, t, tb, "R$ 1.200", W / 2, 385, 62, TINTA2))

    def por_que():
        E.frase(c, t, lerp(b5, c5, 0.2), ps("doze porque é", "i", 72) + ps("3 × 4", "g", 68, COR), W / 2, 680, "center", 0.26)
        E.frase(c, t, lerp(b5, c5, 0.42), ps("tira terços e, depois, quartos sem quebrar", "i", 62), W / 2, 780, "center", 0.26)
        conta_c(c, t, c5, "1.200 ÷ 12 = 100", W / 2, 920, 84, COR)
    E.saida(c, t, C["s06"] - 0.1, por_que)
    # s06
    E.saida(c, t, C["s07"] - 0.1, lambda: conta_c(c, t, b6, "12 ÷ 3 = 4 quadradinhos", W / 2, 300, 72))
    conta_c(c, t, c6, "R$ 400", trecho(0, 4)[0] + 2 * LP, BY + CAI + BH + 90, 84, COR, "g")
    x0, x1 = trecho(4, 12)
    rotulo_sobre(c, t, d6, x0, x1, BY - 12, "sobraram 8 quadradinhos", COR, sai=C["s08"] - 0.1)
    # s07
    if t < C["s08"]:
        E.saida(c, t, b7 - 0.1, lambda: E.frase(c, t, lerp(a7, b7, 0.2), ps("a conta usa os 8 que sobraram,", "i", 66) + ps("não os 12", "g", 62, ERRADO), W / 2, 285, "center", 0.26))
        E.saida(c, t, C["s08"] - 0.1, lambda: conta_c(c, t, b7, "8 ÷ 4 = 2 quadradinhos", W / 2, 285, 72))
    conta_c(c, t, c7, "R$ 200", trecho(4, 6)[0] + LP, BY + CAI + BH + 90, 84, TINTA, "g")
    # s08
    x0, x1 = trecho(6, 12)
    xc = (x0 + x1) / 2
    rotulo_sobre(c, t, a8, x0, x1, BY - 12, "6 de 12", CERTO)
    conta_c(c, t, b8, "R$ 600", xc, 730, 110, CERTO, "g")
    E.frase(c, t, c8, ps("metade", "g", 76, CERTO) + ps("do salário", "i", 80), xc, 840, "center")
    xg = (BX + x0) / 2
    E.frase(c, t, d8, ps("gastou", "i", 66) + ps("a outra metade", "g", 62), xg, 940, "center")
    conta_c(c, t, e8, "400 + 200 = 600", xg, 1020, 60, TINTA)


# ---------------- só com frações ----------------
def b_fracoes(c, t, C, b):
    def parte9():
        a_, b_ = C["s09.a"], C["s09.b"]
        E.frase(c, t, C["s09"] + 0.1, ps("e se o enunciado", "i", 86) + ps("não disser o salário?", "g", 78, COR), W / 2, 190, "center", 0.26)
        E.frase(c, t, lerp(C["s09"], a_, 0.6), ps("só com frações", "g", 110), W / 2, 340, "center")
        E.frase(c, t, a_ - 0.3, ps("sobraram", "i", 92), XE, 560)
        fr(c, t, a_, 2, 3, 590, 530, 120, COR)
        E.frase(c, t, a_ + 0.4, ps("do salário", "g", 80), 680, 560)
        ped = [(i, E.COR, ep(t, a_ + 0.3 + i * 0.2, 0.4)) for i in range(2)]
        E.foco(c, t, a_ + 0.2, 0.5, lambda p: E.chocolate(c, 1150, 460, 600, 150, 3, ped, p))
        fr(c, t, b_, 1, 4, 700, 800, 140, COR)
        E.foco(c, t, b_ + 0.2, 0.45, lambda a: E.escreve(c, "de", 800, 836, 110, "i", TINTA, a))
        fr(c, t, b_ + 0.4, 2, 3, 980, 800, 140, COR)
    E.saida(c, t, C["s10"] - 0.1, parte9)

    if C["s10"] <= t < C["s11"] + 0.3:
        a_, b_, c_, d_, f_ = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.end"]

        def parte10():
            E.frase(c, t, C["s10"] + 0.1, ps("a palavra", "i", 72) + ps("de", "g", 68, COR) + ps("vira", "i", 72) + ps("vezes", "g", 68, COR), XE, 150)
            s, xa, xb, y = 180, 310, 700, 430
            fr(c, t, C["s10"], 1, 4, xa, y, s)
            fr(c, t, C["s10"] + 0.2, 2, 3, xb, y, s)
            ny, dy = y + s * NY, y + s * DY
            if t >= a_:
                M.line(c, xb - 72, ny + 10, xa + 72, dy - 10, CLARO, 1.0, 6, progress=ep(t, a_, 0.5))
            c.drawCircle((xa + xb) / 2, y, 56, M.paint(E.PAPEL))
            sinal(c, t, C["s10"] + 0.3, "×", (xa + xb) / 2, y - 15, 130, COR)
            corte(c, t, lerp(a_, b_, 0.45), xa, dy, s, 2, lerp(a_, b_, 0.75), True)
            corte(c, t, lerp(a_, b_, 0.45), xb, ny, s, 1, lerp(a_, b_, 0.75), False)
            sinal(c, t, b_ - 0.2, "=", 960, y - 15, 110)
            E.foco(c, t, b_, 0.45, lambda a: centro(c, "1 × 1", 1170, y - 42, 96, "g", TINTA, a))
            E.foco(c, t, b_, 0.4, lambda a: c.drawRect(skia.Rect.MakeXYWH(1050, y - 3, 240, 7), M.paint(TINTA, a)))
            E.foco(c, t, c_, 0.45, lambda a: centro(c, "2 × 3", 1170, y + 102, 96, "g", TINTA, a))
            sinal(c, t, lerp(c_, d_, 0.5), "=", 1360, y - 15, 110)
            E.resultado(c, t, lerp(c_, d_, 0.55), 1, 6, 1590, y, 130, 150)
            E.frase(c, t, lerp(c_, d_, 0.65), ps("do salário", "i", 66), 1590, 660, "center")
            E.frase(c, t, d_, ps("não", "g", 74, ERRADO) + ps("1/4", "g", 74, ERRADO), 1590, 755, "center")
            E.frase(c, t, lerp(d_, f_, 0.28), ps("o que sobrou é menor que o salário", "i", 70), XE, 850, passo=0.26)
            E.frase(c, t, lerp(d_, f_, 0.6), ps("1/4", "g", 62, COR) + ps("do que sobrou é menor que", "i", 70) + ps("1/4", "g", 62, COR) + ps("do salário", "i", 70), XE, 960, passo=0.26)
        E.saida(c, t, C["s11"] - 0.1, parte10)

    if t >= C["s11"]:
        a_, b_ = C["s11.a"], C["s11.b"]
        y = 320
        tr = lerp(a_, b_, 0.75)
        fr(c, t, a_, 1, 6, 480, y, 130, COR)
        E.foco(c, t, a_ + 0.2, 0.45, lambda p: E.escreve(c, "de", 570, y + 34, 110, "i", TINTA, p))
        E.foco(c, t, a_ + 0.5, 0.45, lambda p: E.escreve(c, "1.200", 700, y + 44, 124, "g", TINTA, p))
        sinal(c, t, lerp(a_, b_, 0.7), "=", 1125, y - 15, 110)
        E.foco(c, t, tr, 0.5, lambda p: E.escreve(c, "R$ 200", 1200, y + 44, 124, "g", COR, p))
        x, yb, w, h = 216, 540, 1488, 170
        ped = [(0, E.COR, ep(t, tr, 0.4))]
        E.foco(c, t, a_ + 0.4, 0.5, lambda p: E.chocolate(c, x, yb, w, h, 6, ped, p))
        for i in range(6):
            E.foco(c, t, a_ + 0.6 + i * 0.07, 0.35, lambda p, i=i: centro(c, "200", x + w * (i + 0.5) / 6, yb + h / 2 + 24, 66, "g", BR if i == 0 and t >= tr else TINTA, p), sobe=6)
        E.foco(c, t, b_, 0.5, lambda p: E.selo(c, 500, 860, 62, True, p))
        E.frase(c, t, b_ + 0.1, ps("bateu com", "i", 110) + ps("a barra", "g", 100, CERTO), 590, 900)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]

    def parte12():
        E.frase(c, t, C["s12"] + 0.1, ps("e os", "i", 84) + ps("R$ 500", "g", 80, ERRADO) + ps("do começo?", "i", 84), W / 2, 170, "center")
        E.frase(c, t, lerp(C["s12"], a2, 0.8), ps("1/4", "g", 76, ERRADO) + ps("do salário inteiro:", "i", 84), XE, 340)
        conta(c, t, b2, "R$ 300", 1030, 340, 84, ERRADO, "g")
        x, y, w, h = 216, 420, 1488, 140
        lp = w / 12
        ped = [(i, CLARO, ep(t, a2 + i * 0.04, 0.3)) for i in range(4)] + [(i, ERRADO, ep(t, b2 + (i - 4) * 0.12, 0.35)) for i in range(4, 7)]
        E.foco(c, t, a2, 0.5, lambda p: E.chocolate(c, x, y, w, h, 12, ped, p))
        E.chave(c, x, x + 4 * lp, y + h + 12, CINZA, ep(t, c2, 0.4), 16, 4)
        conta_c(c, t, c2, "R$ 400", x + 2 * lp, y + h + 90, 62, TINTA2)
        E.chave(c, x + 4 * lp, x + 7 * lp, y + h + 12, ERRADO, ep(t, b2, 0.4), 16, 4)
        conta_c(c, t, b2, "R$ 300", x + 5.5 * lp, y + h + 90, 62, ERRADO)
        ft = lerp(c2, C["s12.end"], 0.55)
        E.chave(c, x + 7 * lp, x + 12 * lp, y + h + 12, CINZA, ep(t, ft, 0.4), 16, 4)
        conta_c(c, t, ft, "sobram R$ 500", x + 9.5 * lp, y + h + 90, 62, TINTA2)
        conta_c(c, t, c2, "400 + 300 = 700 gastos", W / 2, 820, 76, TINTA)
    E.saida(c, t, C["s13"] - 0.1, parte12)

    if t >= C["s13"]:
        a3, b3, c3, d3, e3, f3 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"], C["s13.end"]
        E.frase(c, t, C["s13"] + 0.1, ps("no segundo gasto, só tinha", "i", 88) + ps("R$ 800", "g", 92, COR), W / 2, 190, "center", 0.26)
        E.frase(c, t, lerp(a3, b3, 0.45), ps("fique de olho", "i", 70), W / 2, 310, "center")
        tsub = lerp(d3, e3, 0.55)
        for s, x, ti in (("do que sobrou", 470, b3), ("do restante", 1000, c3), ("do resto", 1460, d3)):
            w = E.larg(s, "g", 70)
            E.frase(c, t, ti, [(s, "g", 70, COR)], x, 450, "center")
            q = ep(t, ti, 0.5)
            E.caixa_pontilhada(c, x - w / 2 - 28, 380, w + 56, 100, q, prog_=q)
            if t >= tsub:
                M.line(c, x - w / 2, 468, x + w / 2, 468, COR, 1.0, 7, progress=ep(t, tsub, 0.4))
        E.frase(c, t, lerp(d3, e3, 0.1), ps("apontam para", "i", 84) + ps("o que ficou,", "g", 80, CERTO) + ps("não para o começo", "i", 84), W / 2, 630, "center", 0.26)
        E.frase(c, t, tsub, ps("sublinhe no enunciado", "i", 76), W / 2, 760, "center", 0.26)
        E.frase(c, t, e3, ps("fração de", "i", 130) + ps("quê?", "g", 124, COR), W / 2, 930, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte14():
        a_, b_, c_, d_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
        E.frase(c, t, C["s14"] + 0.1, ps("agora, o atalho", "i", 78, CLARO), W / 2, 150, "center")
        E.frase(c, t, a_, ps("multiplique", "g", 116, BR) + ps("só as sobras", "i", 126, BR), W / 2, 290, "center")
        for y, ti, tf, n, d, l1, nf, df in ((480, lerp(a_, b_, 0.5), b_, 1, 3, "gastou", 2, 3), (680, lerp(b_, c_, 0.25), c_, 1, 4, "do resto, gastou", 3, 4)):
            E.foco(c, t, ti, 0.45, lambda a, l1=l1, y=y: E.escreve(c, l1, 300, y + 26, 76, "i", BR, a))
            xf = 300 + E.larg(l1, "i", 76) + 90
            fr(c, t, ti + 0.2, n, d, xf, y, 96, BR)
            if t >= tf:
                p = ep(t, tf, 0.5)
                M.arrow(c, xf + 80, y, xf + 200, y, CLARO, p, 5, 16, p)
            E.foco(c, t, tf, 0.45, lambda a, xf=xf, y=y: E.escreve(c, "sobram", xf + 240, y + 26, 76, "g", CLARO, a))
            fr(c, t, tf + 0.1, nf, df, xf + 590, y, 110, CLARO)
        fr(c, t, d_, 3, 4, 790, 880, 96, BR)
        E.foco(c, t, d_ + 0.2, 0.45, lambda a: E.escreve(c, "de", 880, 910, 86, "i", CLARO, a))
        fr(c, t, d_ + 0.4, 2, 3, 1040, 880, 96, BR)
    E.saida(c, t, C["s15"] - 0.1, parte14)

    if C["s15"] <= t < C["s16"] + 0.3:
        a_, b_, c_, f_ = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.end"]

        def parte15():
            s, xa, xb, y = 210, 340, 800, 450
            fr(c, t, C["s15"], 3, 4, xa, y, s, BR)
            fr(c, t, C["s15"] + 0.2, 2, 3, xb, y, s, BR)
            ny, dy = y + s * NY, y + s * DY
            if t >= a_:
                M.line(c, xa + 80, ny + 10, xb - 80, dy - 10, CLARO, 1.0, 7, progress=ep(t, a_, 0.5))
            if t >= b_:
                M.line(c, xb - 80, ny + 10, xa + 80, dy - 10, CLARO, 1.0, 7, progress=ep(t, b_, 0.5))
            c.drawCircle((xa + xb) / 2, y, 60, M.paint("#0F0B38"))
            sinal(c, t, C["s15"] + 0.3, "×", (xa + xb) / 2, y - 6, 120, BR)
            corte(c, t, a_ + 0.3, xa, ny, s, 1, a_ + 0.7, False, CLARO, CLARO)
            corte(c, t, a_ + 0.3, xb, dy, s, 1, a_ + 0.7, True, CLARO, CLARO)
            corte(c, t, b_ + 0.3, xa, dy, s, 2, b_ + 0.7, True, CLARO, CLARO)
            corte(c, t, b_ + 0.3, xb, ny, s, 1, b_ + 0.7, False, CLARO, CLARO)
            sinal(c, t, c_ - 0.2, "=", 1110, y - 15, 130, BR)
            E.foco(c, t, c_, 0.5, lambda a: E.fracao(c, 1, 2, 1330, y, 230, CLARO, a))
            E.frase(c, t, lerp(c_, f_, 0.25), ps("metade do salário,", "g", 86, BR) + ps("em uma linha só", "i", 92, CLARO), W / 2, 900, "center")
        E.saida(c, t, C["s16"] - 0.1, parte15)

    if C["s16"] <= t < C["s17"] + 0.3:
        a_, b_, c_, d_, e_, f_ = (C[f"s16.{k}"] for k in "abcdef")

        def parte16():
            E.frase(c, t, C["s16"] + 0.1, ps("mais um,", "i", 80, CLARO) + ps("sem nenhum valor", "g", 74, BR), XE, 160)
            nivel = 1 - 0.2 * ease_io(prog(t, a_ + 0.2, 0.8)) - 0.4 * ease_io(prog(t, b_ + 0.2, 0.8))
            E.foco(c, t, lerp(C["s16"], a_, 0.5), 0.5, lambda p: tanque(c, 1330, 200, 340, 680, nivel, p))
            E.foco(c, t, lerp(C["s16"], a_, 0.5), 0.45, lambda p: centro(c, "caixa de água", 1500, 950, 60, "i", CLARO, p))
            E.frase(c, t, a_ - 0.5, ps("de manhã, saiu", "i", 76, BR), XE, 310)
            fr(c, t, a_, 1, 5, 760, 285, 88, CLARO)
            E.frase(c, t, b_ - 0.4, ps("à tarde,", "i", 76, BR) + ps("metade do restante", "g", 68, CLARO), XE, 450)
            conta(c, t, c_, "sobram 4/5", XE, 600, 76, BR, "g")
            E.frase(c, t, d_, ps("e depois", "i", 76, BR) + ps("1/2", "g", 70, CLARO) + ps("deles", "i", 76, BR), 640, 600)
            y = 800
            fr(c, t, e_, 1, 2, 270, y, 124, BR)
            sinal(c, t, e_ + 0.2, "×", 400, y - 15, 90, BR)
            fr(c, t, e_ + 0.4, 4, 5, 530, y, 124, BR)
            sinal(c, t, f_ - 0.2, "=", 665, y - 15, 90, BR)
            fr(c, t, f_, 2, 5, 790, y, 124, CLARO)
            E.frase(c, t, f_ + 0.2, ps("da caixa", "g", 70, BR), 890, y + 26)
        E.saida(c, t, C["s17"] - 0.1, parte16)

    if t >= C["s17"]:
        a_, b_, c_ = C["s17.a"], C["s17.b"], C["s17.c"]
        E.frase(c, t, C["s17"] + 0.1, ps("funciona porque", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, a_, ps("cada sobra é uma fração", "g", 84, BR), W / 2, 300, "center", 0.26)
        E.frase(c, t, a_ + 1.2, ps("da sobra anterior", "i", 92, BR), W / 2, 410, "center", 0.26)
        E.frase(c, t, lerp(a_, b_, 0.5), ps("fração de fração é vezes", "i", 74, CLARO), W / 2, 520, "center", 0.26)
        E.frase(c, t, b_ - 0.8, ps("não compensa quando a pergunta é", "i", 66, CLARO), W / 2, 680, "center", 0.26)
        E.frase(c, t, b_, ps("quanto saiu em uma etapa", "g", 84, BR), W / 2, 790, "center", 0.26)
        E.frase(c, t, c_, ps("o segundo gasto:", "i", 80, CLARO) + ps("1/6 do salário", "g", 74, BR), W / 2, 940, "center", 0.26)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_, d_ = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, a_, ps("90", "g", 110, COR) + ps("camisetas", "g", 92), XE, 340)
    E.frase(c, t, b_ - 0.4, ps("de manhã, vendeu", "i", 84), XE, 495)
    fr(c, t, b_, 2, 5, 810, 465, 96, COR)
    E.frase(c, t, c_ - 0.4, ps("à tarde, vendeu", "i", 84), XE, 685)
    fr(c, t, c_, 2, 3, 760, 655, 96, COR)
    E.frase(c, t, c_ + 0.4, ps("do restante", "g", 72), 850, 685)
    E.frase(c, t, d_, ps("quantas", "i", 120) + ps("sobraram?", "g", 112, COR), XE, 900)
    E.relogio(c, t, C["s19.a"], 1530, 350, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0, d0 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]

    def sobras():
        E.frase(c, t, C["s20"] + 0.1, ps("vamos lá,", "i", 72, COR) + ps("pelas sobras", "g", 66, COR), XE, 170)
        for y, ti, l1, nf, df in ((295, a0, "vendeu 2/5:", 3, 5), (465, b0, "vendeu 2/3 do restante:", 1, 3)):
            E.frase(c, t, ti - 0.9, [(l1, "i", 80)], XE, y + 26)
            xs = XE + E.larg(l1, "i", 80) + 50
            E.foco(c, t, ti, 0.45, lambda a, xs=xs, y=y: E.escreve(c, "sobra", xs, y + 26, 76, "g", COR, a))
            fr(c, t, ti + 0.1, nf, df, xs + 310, y, 110, COR)
        s, xa, xb, y = 170, 500, 900, 790
        fr(c, t, c0, 1, 3, xa, y, s)
        E.saida(c, t, c0 + 1.3, lambda: E.foco(c, t, c0 + 0.2, 0.4, lambda a: centro(c, "de", (xa + xb) / 2, y + 34, 120, "i", TINTA, a)))
        sinal(c, t, c0 + 1.3, "×", (xa + xb) / 2, y - 15, 120, COR)
        fr(c, t, c0 + 0.4, 3, 5, xb, y, s)
        ny, dy = y + s * NY, y + s * DY
        corte(c, t, lerp(c0, d0, 0.7), xa, dy, s, 1, lerp(c0, d0, 0.9), True)
        corte(c, t, lerp(c0, d0, 0.7), xb, ny, s, 1, lerp(c0, d0, 0.9), False)
        sinal(c, t, d0 - 0.2, "=", 1160, y - 15, 110)
        E.resultado(c, t, d0, 1, 5, 1380, y, 130, 150)
    E.saida(c, t, C["s21"] - 0.1, sobras)

    if t >= C["s21"]:
        a_, b_, c_, d_, e_, f_ = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"], C["s21.e"], C["s21.end"]
        x, y, w, h, cai = 216, 370, 1488, 170, 200
        lp = w / 5
        E.frase(c, t, C["s21"] + 0.1, ps("1/5", "g", 96, COR) + ps("de 90:", "i", 104), XE, 190)
        E.frase(c, t, a_, ps("18 camisetas", "g", 96, CERTO), 620, 190)
        ped = []
        for i in range(5):
            tq = b_ if i < 2 else d_ if i < 4 else None
            q = ease_io(prog(t, tq, 0.7)) if tq else 0
            ped.append((i, E.COR if i < 4 else CERTO, ep(t, a_ + i * 0.1, 0.35), cai * q))
        E.foco(c, t, a_, 0.5, lambda p: E.chocolate(c, x, y, w, h, 5, ped, p))
        for i, _, _, dy in ped:
            E.foco(c, t, a_ + 0.2 + i * 0.1, 0.35, lambda p, i=i, dy=dy: centro(c, "18", x + (i + 0.5) * lp, y + dy + h / 2 + 30, 84, "g", BR, p), sobe=6)
        conta_c(c, t, b_, "manhã: 36", x + lp, y + cai + h + 80, 70, COR)
        conta_c(c, t, d_, "tarde: 36", x + 3 * lp, y + cai + h + 80, 70, COR)
        E.saida(c, t, d_, lambda: (E.chave(c, x + 2 * lp, x + 5 * lp, y - 12, TINTA2, ep(t, c_, 0.4), -16, 4), conta_c(c, t, c_, "ficam 54", x + 3.5 * lp, y - 44, 60, TINTA2)))
        E.chave(c, x + 4 * lp, x + 5 * lp, y - 12, CERTO, ep(t, e_, 0.4), -16, 4)
        conta_c(c, t, e_, "ficam 18", x + 4.5 * lp, y - 44, 60, CERTO)
        tb = lerp(e_, f_, 0.5)
        E.foco(c, t, tb, 0.5, lambda p: E.selo(c, 1480, 800, 66, True, p))
        E.frase(c, t, tb, ps("bateu", "g", 84, CERTO), 1570, 830)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 200, "center")
        E.frase(c, t, C["s22.a"] - 0.5, ps("antes de cada conta,", "i", 88), W / 2, 380, "center")
        E.frase(c, t, C["s22.a"], ps("fração de", "i", 120) + ps("quê?", "g", 116, COR), W / 2, 520, "center")
        E.frase(c, t, C["s22.b"] - 0.8, ps("quando for do restante,", "i", 88), W / 2, 720, "center")
        E.frase(c, t, C["s22.b"], ps("multiplique", "g", 116, COR) + ps("as sobras", "i", 120), W / 2, 860, "center")
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a_, b_, c_, d_ = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 84), XE, 260)
    E.frase(c, t, a_, ps("dividir frações", "g", 130, COR), XE, 410, passo=0.25)
    E.frase(c, t, b_, ps("quantos copos de", "i", 80) + ps("1/4 de litro", "g", 76, COR), XE, 550, passo=0.26)
    E.frase(c, t, b_ + 1.1, ps("cabem em", "i", 80) + ps("3 litros?", "g", 76, COR), XE, 650, passo=0.26)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 240, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1640, p), lerp(650, 285, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barra=b_barra, fracoes=b_fracoes, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
