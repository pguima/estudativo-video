"""Visual — Estudativo · MAT-FRA-016: multiplicar decimais e andar com a vírgula.
Identidade em _ferramentas/editorial.py. A vírgula salta com E.anda: os algarismos ficam parados e o zero entra sozinho."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, passo, palco
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-016_multiplicar_decimais_andar_virgula.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("andar", "multiplicar", "sinal", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def num(c, t, t0, s, xv, y, size, cor=None, cores=None):
    """decimal alinhado pela vírgula, com entrada de foco"""
    E.foco(c, t, t0, 0.5, lambda a: E.numero(c, s, xv, y, size, "g", cor, a, cores))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def fita(c, x, y, w, h, cor, a=1.0):
    """pedaço de fita: faixa com costura pontilhada (peça local)"""
    if a <= 0 or w <= 0:
        return
    M.rrect(c, x, y, w, h, 8, cor, a)
    p = M.paint(M.on(cor), 0.6 * a, stroke=3)
    p.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    for yy in (y + 14, y + h - 14):
        path = skia.Path(); path.moveTo(x + 6, yy); path.lineTo(x + w - 6, yy)
        c.drawPath(path, p)


def seta(c, t, t0, x0, x1, y, cor=None):
    if t >= t0:
        p = ep(t, t0, 0.5)
        M.arrow(c, x0, y, x1, y, cor or COR, p, 6, 20, p)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    x, y, h, u = 300, 300, 120, 900  # u = largura de um metro de fita
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def tudo():
        E.foco(c, t, ka, 0.5, lambda a: fita(c, x, y, u, h, E.COR, a))
        E.foco(c, t, kb, 0.5, lambda a: fita(c, x + u + 6, y, u * 0.2, h, TINTA, a))
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "30 centavos o metro", x + u / 2, y - 40, 72, "b", COR, a))
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "1 metro e 20", x + u * 0.6, y + h + 90, 72, "i", TINTA, a))
        ym = 760
        E.frase(c, t, kc, [("1,2", "g", 140), ("×", "g", 110), ("0,3", "g", 140, COR)], 640, ym, "center", passo=0.3)
        E.sinal(c, t, kd - 0.1, "=", 1000, ym - 45, 120)
        num(c, t, kd, "3,6", 1220, ym, 140, ERRADO)
        E.frase(c, t, lerp(kd, C["s01.end"], 0.35), [("R$ 3,60", "g", 80, ERRADO), ("em", "i", 88), ("pouco", "i", 88), ("mais", "i", 88), ("de", "i", 88), ("um", "i", 88), ("metro?", "i", 88)], W / 2, 930, "center", passo=0.13)
    E.saida(c, t, C["s02"] - 0.1, tudo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.3), [("multiplicar", "g", 124)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.32), [("decimais", "g", 124)], XE, 620)
        E.frase(c, t, lerp(ta, tb, 0.42), [("até", "i", 84), ("com", "i", 84), ("sinal", "i", 84), ("negativo", "i", 84, COR)], XE, 740)
        E.frase(c, t, lerp(ta, tb, 0.62), [("andar", "g", 84), ("com", "i", 90), ("a", "i", 90), ("vírgula", "g", 84, COR)], XE, 860)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1500, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1500, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini], [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C[ta], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[ta] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    y0, dy = (280, 260) if len(itens) == 2 else (190, 240)
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * dy
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    px = x + w - 30
    py = y0 + 170
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, y0 + i * dy + 170, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, px, py, ep(t, C[itens[0][0]], 0.4))


def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", "s03.a", 3, (("s03.b", "saber o que é", "casa decimal"), ("s03.c", "multiplicar por", "dois algarismos"), ("s03.d", "a regra", "de sinais")))


# ---------------- andar com a vírgula ----------------
def b_andar(c, t, C, b):
    def vezes():
        E.frase(c, t, C["s04.a"], [("100", "g", 84, COR), ("pessoas", "i", 92), ("pagam", "i", 92), ("R$ 3,70", "g", 84), ("cada", "i", 92)], W / 2, 180, "center", passo=0.14)
        E.frase(c, t, C["s04.b"], [("3,7", "g", 120), ("×", "g", 100), ("100", "g", 120, COR)], W / 2, 335, "center")
        E.frase(c, t, C["s05.a"], [("100", "g", 72, COR), ("tem", "i", 80), ("2", "g", 72, COR), ("zeros", "g", 72, COR)], W / 2, 470, "center", passo=0.12)
        E.frase(c, t, C["s05.b"] + 0.2, [("a", "i", 72), ("vírgula", "i", 72), ("anda", "i", 72), ("2", "g", 64, COR), ("casas", "g", 64, COR), ("para", "i", 72), ("a", "i", 72), ("direita", "g", 64, COR)], W / 2, 570, "center", passo=0.1)
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.anda(c, t, "37", 1, [(C["s05.c"], 2), (C["s05.d"], 3)], 440, 830, 210, some=True))
        for t0, t1, s in ((C["s05.c"], C["s05.d"], "uma casa"), (C["s05.d"], C["s05.e"], "duas casas")):
            if t0 <= t:
                E.saida(c, t, t1 - 0.1, lambda s=s, t0=t0: E.foco(c, t, t0, 0.4, lambda a: E.centro(c, s, 1320, 790, 80, "i", COR, a)))
        bola_txt(c, t, C["s05.e"], "R$ 370", 1370, 760, 150, 76)
    E.saida(c, t, C["s06"] - 0.1, vezes)

    def porque():
        ka, kb, kc = C["s06.a"], C["s06.b"], C["s06.c"]
        y = 250
        for i in range(7):
            E.foco(c, t, ka + i * 0.12, 0.35, lambda a, i=i: E.moeda(c, 210 + i * 96, y, 46, "10¢", a))
        E.foco(c, t, lerp(ka, kb, 0.6), 0.45, lambda a: E.pilula(c, "× 10", 960, y, 66, "g", a=a, cor=E.SOBRE))
        seta(c, t, kb, 1080, 1200, y)
        E.frase(c, t, kb, [("7", "g", 120, COR), ("reais", "g", 120, COR)], 1240, y + 42)
        ts = lerp(kb, kc, 0.3)
        E.frase(c, t, ts, [("cada", "i", 80), ("algarismo", "g", 72), ("sobe", "i", 80), ("uma", "i", 80), ("casa", "i", 80)], W / 2, 430, "center", passo=0.12)
        size, xv, yn = 170, 520, 700

        def desliza(a):
            cl = E.larg("0", "g", size) * 1.1
            f = size * 0.17
            q = ease_io(prog(t, ts + 0.8, 0.8))
            E._digito(c, "3", lerp(xv - f - 0.5 * cl, xv - f - 1.5 * cl, q), yn, size, "g", TINTA, a)
            E._digito(c, "7", lerp(xv + f + 0.5 * cl, xv - f - 0.5 * cl, q), yn, size, "g", TINTA, a)
            E._virgula(c, xv, yn, size, COR, a)
            if q >= 1:
                E.foco(c, t, ts + 1.6, 0.4, lambda a2: E._digito(c, "0", xv + f + 0.5 * cl, yn, size, "g", COR, a2))
        E.foco(c, t, ts, 0.5, desliza)
        E.foco(c, t, kc, 0.5, lambda a: E.anda(c, t, "37", 1, [(kc + 0.5, 2)], 1180, yn, size))
        E.foco(c, t, kc + 1.3, 0.4, lambda a: E._digito(c, "0", 1180 + 2.5 * E.casa(size), yn, size, "g", COR, a))
        E.frase(c, t, kc, [("na", "i", 80), ("tela,", "i", 80), ("parece", "i", 80), ("que", "i", 80), ("foi", "i", 80), ("a", "i", 80), ("vírgula", "g", 72, COR), ("que", "i", 80), ("andou", "i", 80)], W / 2, 900, "center", passo=0.12)
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, porque)

    def dividir():
        E.frase(c, t, C["s07.a"], [("45", "g", 120), ("÷", "g", 100), ("1.000", "g", 120, COR)], W / 2, 210, "center")
        y, size, x = 590, 200, 960
        ka, kb, kc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
        tb7, tc7 = C["s07.b"], C["s07.c"]
        cap = ((tb7, tc7, [("uma", "i", 80), ("vírgula", "g", 72, COR), ("escondida", "i", 80), ("no", "i", 80), ("fim", "i", 80)]),
               (tc7, ka, [("1.000", "g", 72, COR), ("tem", "i", 80), ("3", "g", 72, COR), ("zeros:", "g", 72, COR), ("anda", "i", 80), ("3", "g", 72, COR), ("casas", "g", 72, COR), ("para", "i", 80), ("a", "i", 80), ("esquerda", "g", 72, COR)]))
        for t0, t1, partes in cap:
            if t0 <= t:
                E.saida(c, t, t1 - 0.1, lambda partes=partes, t0=t0: E.frase(c, t, t0, partes, W / 2, 350, "center", passo=0.1))
        px = lambda i: x + (i + 0.5) * E.casa(size)
        E.foco(c, t, C["s07.a"], 0.5, lambda a: E.anda(c, t, "45", 2, [(ka, 1), (kb, 0), (kc, -1)], x, y, size, tv=tb7))
        # 45 = 45,0: o zero aparece só enquanto a fala mostra a vírgula escondida
        if tb7 <= t:
            E.saida(c, t, tc7 - 0.1, lambda: E.foco(c, t, lerp(tb7, tc7, 0.45), 0.4, lambda a: E._digito(c, "0", px(2), y, size, "g", COR, a)))
        for t0, t1, s in ((ka, kb, "uma: 4,5"), (kb, kc, "duas: 0,45"), (kc, kd, "três: 0,045")):
            if t0 <= t:
                E.saida(c, t, t1 - 0.1, lambda s=s, t0=t0: E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.centro(c, s, W / 2, 800, 80, "i", COR, a)))
        E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "45 milésimos", W / 2, 830, 88, "g", a=a, cor=E.SOBRE))
    if C["s07"] - 0.1 <= t:
        E.saida(c, t, C["s09"] - 0.1, dividir)

    if t >= C["s09"]:
        E.frase(c, t, C["s09"] + 0.1, [("a", "i", 84, COR), ("regra,", "i", 84, COR), ("só", "i", 84), ("para", "i", 84), ("10,", "g", 76), ("100", "g", 76), ("e", "i", 84), ("1.000", "g", 76)], W / 2, 170, "center", passo=0.1)
        E.frase(c, t, C["s09.a"], [("multiplicar", "g", 88, COR), ("anda", "i", 92), ("para", "i", 92), ("a", "i", 92), ("direita", "g", 88)], XE, 360, passo=0.1)
        E.frase(c, t, C["s09.a"] + 1.2, [("e", "i", 92), ("o", "i", 92), ("número", "i", 92), ("cresce", "g", 88, COR)], XE, 470, passo=0.1)
        E.frase(c, t, C["s09.b"], [("dividir", "g", 88, COR), ("anda", "i", 92), ("para", "i", 92), ("a", "i", 92), ("esquerda", "g", 88)], XE, 630, passo=0.1)
        E.frase(c, t, C["s09.b"] + 1.2, [("e", "i", 92), ("o", "i", 92), ("número", "i", 92), ("diminui", "g", 88, COR)], XE, 740, passo=0.1)
        E.foco(c, t, C["s09.c"], 0.5, lambda a: E.pilula(c, "quantos zeros, tantas casas", W / 2, 910, 76, "g", a=a, cor=E.SOBRE))


# ---------------- multiplicar ----------------
def b_multiplicar(c, t, C, b):
    def metodo():
        ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
        xp = 860
        passo(c, t, kb, 1, "ignore", "as vírgulas", 210)
        y1 = 240
        E.saida(c, t, kb + 0.2, lambda: E.frase(c, t, ka, [("1,2", "g", 110), ("×", "g", 92), ("0,3", "g", 110)], xp, y1, passo=0.3))
        E.frase(c, t, kb + 0.5, [("12", "g", 110), ("×", "g", 92), ("3", "g", 110)], xp, y1, passo=0.05)
        E.frase(c, t, kc, [("=", "g", 92), ("36", "g", 120, COR)], 1240, y1)

        ka2, kb2, kc2, kd2 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        passo(c, t, ka2, 2, "conte as casas", "depois da vírgula", 500)
        y2, sz = 540, 110
        for xv, s, k, nome in ((960, "1,2", kb2, "1,2"), (1270, "0,3", kc2, "0,3")):
            xs = E._centros(s, xv, sz)
            num(c, t, k, s, xv, y2, sz, None, {2: COR})
            q = ep(t, k, 0.4)
            if q > 0:
                E.caixa_pontilhada(c, xs[2] - 58, y2 - 96, 116, 118, q, COR, prog_=q)
            E.foco(c, t, k + 0.1, 0.4, lambda a, xv=xv: E.centro(c, "uma", xv + 30, y2 + 80, 50, "i", COR, a))
        E.foco(c, t, kd2, 0.5, lambda a: E.pilula(c, "2 casas", 1610, y2 - 34, 62, "g", a=a, cor=E.SOBRE))

        ka3, kb3, kc3 = C["s12.a"], C["s12.b"], C["s12.c"]
        passo(c, t, ka3, 3, "o resultado fica", "com essas casas", 820)
        bola_txt(c, t, kb3, "0,36", 1010, 830, 118, 84)
        E.frase(c, t, kc3, [("36", "g", 88), ("centavos", "i", 96)], 1170, 860)
    E.saida(c, t, C["s13"] - 0.1, metodo)

    def porque():
        ka, kb, kc, kd = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
        E.frase(c, t, C["s13"] + 0.1, [("por", "i", 80), ("que", "i", 80), ("funciona?", "g", 72, COR)], W / 2, 150, "center")
        for y, a_, b_, k in ((310, "1,2", "12", ka), (470, "0,3", "3", kb)):
            num(c, t, k, a_, 560, y, 120)
            seta(c, t, k + 0.2, 700, 820, y - 40)
            E.foco(c, t, k + 0.3, 0.4, lambda a, b_=b_, y=y: E.centro(c, b_, 930, y, 120, "g", TINTA, a))
            E.frase(c, t, k + 0.5, [("10", "g", 72, COR), ("vezes", "i", 80), ("maior", "i", 80)], 1080, y - 8, passo=0.1)
        E.frase(c, t, kc, [("10", "g", 96), ("×", "g", 84), ("10", "g", 96), ("=", "g", 84), ("100", "g", 96, COR), ("vezes", "i", 96), ("maior", "i", 96)], W / 2, 660, "center", passo=0.12)
        E.frase(c, t, kd, [("desfaz:", "i", 84), ("duas", "g", 76, COR), ("casas", "g", 76, COR), ("para", "i", 84), ("a", "i", 84), ("esquerda", "g", 76, COR)], W / 2, 830, "center", passo=0.12)
    if C["s13"] - 0.1 <= t:
        E.saida(c, t, C["s14"] - 0.1, porque)

    if t >= C["s14"]:
        ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
        x, y, h, u = 300, 340, 130, 1000
        E.frase(c, t, C["s14"] + 0.1, [("confira", "i", 90), ("na", "i", 90), ("fita", "g", 82, COR)], W / 2, 180, "center")
        E.foco(c, t, ka, 0.5, lambda a: (fita(c, x, y, u, h, E.COR, a), E.centro(c, "1 metro", x + u / 2, y - 30, 66, "i", TINTA, a),
                                         E.centro(c, "30 centavos", x + u / 2, y + h + 80, 72, "g", COR, a)))
        E.foco(c, t, kb, 0.5, lambda a: (fita(c, x + u + 8, y, u * 0.2, h, TINTA, a), E.centro(c, "20 cm", x + u * 1.1, y - 30, 66, "i", TINTA, a),
                                         E.centro(c, "6 centavos", x + u * 1.1 + 80, y + h + 80, 72, "g", TINTA, a)))
        E.frase(c, t, kb + 0.4, [("a", "i", 72), ("quinta", "i", 72), ("parte", "i", 72), ("do", "i", 72), ("metro", "i", 72)], x + u + 210, y + h + 190, "right", passo=0.1)
        E.frase(c, t, kc - 0.3, [("total:", "i", 110)], 300, 830)
        bola_txt(c, t, kc, "36¢", 680, 795, 130, 88)


# ---------------- sinal ----------------
def b_sinal(c, t, C, b):
    def fiado():
        ka, kb, kc, kd = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, ka, [("resolva", "i", 92), ("o", "i", 92), ("sinal", "g", 84, COR), ("no", "i", 92), ("fim", "i", 92)], W / 2, 180, "center", passo=0.12)
        E.frase(c, t, kb, [("cada", "i", 84), ("metro", "i", 84), ("é", "i", 84), ("uma", "i", 84), ("dívida:", "i", 84), ("−0,3", "g", 96, COR)], W / 2, 340, "center", passo=0.1)
        E.frase(c, t, kc, [("−0,3", "g", 140, COR), ("×", "g", 110), ("1,2", "g", 140)], 660, 620, "center", passo=0.2)
        E.sinal(c, t, kd - 0.1, "=", 1100, 575, 120)
        bola_txt(c, t, kd, "−0,36", 1370, 590, 150, 84)
        E.frase(c, t, lerp(kc, kd, 0.65), [("sinais", "i", 84), ("diferentes,", "i", 84), ("negativo", "g", 76, COR)], W / 2, 860, "center", passo=0.1)
    E.saida(c, t, C["s16"] - 0.1, fiado)
    if t >= C["s16"]:
        ka, kb = C["s16.a"], C["s16.b"]
        E.frase(c, t, C["s16"] + 0.2, [("a", "i", 84), ("loja", "i", 84), ("cancela", "g", 76, COR), ("a", "i", 84), ("dívida", "i", 84)], W / 2, 180, "center", passo=0.12)
        E.frase(c, t, ka, [("−0,3", "g", 130, COR), ("×", "g", 104), ("(−1,2)", "g", 130, COR)], 620, 450, "center", passo=0.2)
        E.frase(c, t, lerp(ka, kb, 0.55), [("menos", "i", 84), ("vezes", "i", 84), ("menos", "i", 84), ("dá", "i", 84), ("mais", "g", 76, CERTO)], W / 2, 690, "center", passo=0.1)
        E.sinal(c, t, kb - 0.1, "=", 1080, 405, 120)
        bola_txt(c, t, kb, "+0,36", 1340, 400, 170, 92, CERTO)
        E.frase(c, t, lerp(kb, C["s16.end"], 0.4), [("tirar", "i", 84), ("uma", "i", 84), ("dívida", "g", 76, COR), ("é", "i", 84), ("como", "i", 84), ("ganhar", "g", 76, CERTO)], W / 2, 860, "center", passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, ka, [("contar", "i", 92), ("as", "i", 92), ("casas", "i", 92), ("de", "i", 92), ("um", "i", 92), ("número", "g", 84, ERRADO), ("só", "g", 84, ERRADO)], W / 2, 180, "center", passo=0.12)
    x, u, h = 370, 370, 110
    y1, y2 = 330, 560
    E.foco(c, t, kb, 0.5, lambda a: (E.centro(c, "3,6", 240, y1 + 82, 92, "g", ERRADO, a), E.barra_fatias(c, x, y1, u * 3.6, h, 1, 1, ERRADO, a)))
    E.foco(c, t, kc, 0.5, lambda a: (E.centro(c, "1,2", 240, y2 + 82, 92, "g", TINTA, a), E.barra(c, x, y2, u * 1.2, h, 0.3, [(0.3, 1.0)], a)))
    E.frase(c, t, kc + 0.4, [("pegar", "i", 84), ("só", "i", 84), ("um", "i", 84), ("pedaço", "g", 76, COR)], x + u * 1.2 + 70, y2 + 80, passo=0.12)
    E.frase(c, t, kd, [("menor", "g", 110, CERTO), ("que", "i", 120), ("1,2", "g", 120)], W / 2, 870, "center")
    E.foco(c, t, kb + 0.3, 0.5, lambda a: E.selo(c, x + u * 3.6 + 72, y1 + h / 2, 50, False, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def cinco():
        ka, kb, kc, kd, ke, kf = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"], C["s18.f"]
        E.frase(c, t, C["s18"] + 0.1, [("agora,", "i", 80, CLARO), ("o", "i", 80, CLARO), ("atalho:", "i", 80, CLARO)], W / 2, 170, "center", passo=0.1)
        E.frase(c, t, ka, [("vezes", "g", 150, BR), ("cinco", "g", 150, BR)], W / 2, 340, "center")
        E.frase(c, t, kb, [("multiplique", "i", 72, CLARO), ("por", "i", 72, CLARO), ("10", "g", 66, BR)], 300, 490, passo=0.08)
        E.frase(c, t, kc, [("tire", "i", 72, CLARO), ("a", "i", 72, CLARO), ("metade", "g", 66, BR)], 1100, 490, passo=0.08)
        y = 760
        E.frase(c, t, kd, [("2,4", "g", 130, BR), ("×", "g", 104, CLARO), ("5", "g", 130, BR)], 390, y, "center", passo=0.15)
        E.ponte(c, t, ke - 0.3, 640, 880, y - 44, "× 10", CLARO, 54)
        E.foco(c, t, ke, 0.5, lambda a: E.centro(c, "24", 1010, y, 140, "g", BR, a))
        E.ponte(c, t, kf - 0.3, 1140, 1380, y - 44, "÷ 2", CLARO, 54)
        E.foco(c, t, kf, 0.5, lambda a: E.centro(c, "12", 1530, y, 170, "g", CLARO, a))
    E.saida(c, t, C["s19"] - 0.1, cinco)
    if t >= C["s19"]:
        ka, kb = C["s19.a"], C["s19.b"]
        E.frase(c, t, ka, [("5", "g", 170, CLARO), ("é", "i", 130, BR), ("a", "i", 130, BR), ("metade", "g", 120, BR), ("de", "i", 130, BR), ("10", "g", 170, CLARO)], W / 2, 400, "center", passo=0.14)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 690, 72, False, a))
        E.frase(c, t, kb + 0.1, [("não", "i", 80, CLARO), ("compensa", "i", 80, CLARO), ("se", "i", 80, CLARO), ("a", "i", 80, CLARO), ("metade", "g", 72, BR), ("não", "i", 80, CLARO), ("sai", "i", 80, CLARO), ("de", "i", 80, CLARO), ("cabeça", "g", 72, BR)], 410, 715, passo=0.1)
        E.frase(c, t, kb + 2.2, [("aí,", "i", 84, CLARO), ("arme", "g", 76, BR), ("a", "g", 76, BR), ("conta", "g", 76, BR)], 410, 840, passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s20"], [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 190)
    E.frase(c, t, C["s20.a"], [("levou", "i", 84), ("fiado", "i", 84), ("1", "g", 76, COR), ("metro", "g", 76, COR), ("e", "g", 76, COR), ("50", "g", 76, COR)], XE, 370, passo=0.1)
    E.frase(c, t, C["s20.b"], [("cada", "i", 84), ("metro:", "i", 84), ("dívida", "i", 84), ("de", "i", 84), ("R$ 3,20", "g", 76, COR)], XE, 520, passo=0.1)
    E.frase(c, t, lerp(C["s20.b"], C["s20.c"], 0.55), [("saldo", "i", 84), ("estava", "i", 84), ("em", "i", 84), ("zero", "g", 76)], XE, 670, passo=0.1)
    E.frase(c, t, C["s20.c"], [("qual", "i", 110), ("é", "i", 110), ("o", "i", 110), ("saldo", "g", 100, COR), ("agora?", "g", 100, COR)], XE, 860)
    E.relogio(c, t, C["s21.a"], 1520, 370, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc = C["s22.a"], C["s22.b"], C["s22.c"]
    E.frase(c, t, ka, [("−3,2", "g", 120, COR), ("×", "g", 96), ("1,5", "g", 120)], W / 2, 200, "center", passo=0.25)
    E.frase(c, t, kb, [("32", "g", 110), ("×", "g", 92), ("15", "g", 110)], 780, 370, "center", passo=0.2)
    E.frase(c, t, kc, [("=", "g", 92), ("480", "g", 120, COR)], 1190, 370, "center", passo=0.1)
    ka2, kb2, kc2 = C["s23.a"], C["s23.b"], C["s23.c"]
    E.frase(c, t, C["s23"] + 0.1, [("uma", "i", 76), ("casa", "i", 76), ("mais", "i", 76), ("uma", "i", 76), ("casa:", "i", 76), ("2", "g", 70, COR), ("casas", "g", 70, COR)], W / 2, 520, "center", passo=0.1)
    num(c, t, kb2, "4,80", 640, 740, 150, TINTA)
    seta(c, t, lerp(kb2, kc2, 0.8), 960, 1060, 690)
    bola_txt(c, t, kc2, "−4,8", 1210, 690, 130, 90)
    E.frase(c, t, kc2 + 0.3, [("reais", "i", 110)], 1365, 725)
    E.frase(c, t, lerp(kb2, kc2, 0.45), [("sinais", "i", 84), ("diferentes,", "i", 84), ("negativo", "g", 76, COR)], W / 2, 920, "center", passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s24.a", "quantos zeros, tantas casas"), ("s24.b", "na multiplicação, some as casas"), ("s24.c", "o sinal se decide primeiro"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 400, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s25.a"], [("Dividir", "g", 140, COR), ("quando", "i", 130), ("sobra", "i", 130), ("resto", "g", 140, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s25.b"], [("a", "i", 80), ("conta", "i", 80), ("continua", "g", 72), ("depois", "i", 80), ("da", "i", 80), ("vírgula", "g", 72, COR)], XE, 590, passo=0.1)
    E.foco(c, t, C["s25.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 710, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s25.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 735, p), ep(t, C["s25.c"] + 0.2, 0.4))
    E.frase(c, t, C["s25.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, andar=b_andar, multiplicar=b_multiplicar, sinal=b_sinal, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
