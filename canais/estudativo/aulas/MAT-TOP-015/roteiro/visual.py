"""Visual — Estudativo · MAT-TOP-015: algarismos significativos e arredondamento.

Linguagem: o número é escrito algarismo a algarismo (digitos()), e cada algarismo ganha a cor do seu papel:
    índigo = significativo certo · âmbar = o primeiro estimado (o último significativo da medida) · cinza = zero que só marca
    a vírgula (não conta) · vermelho = algarismo inventado, que sai no arredondamento.
Embaixo de cada medida, uma pílula com quantos significativos ela tem. A régua de centímetros mostra de onde vem o "certo" e o
"estimado". Atalho (notação científica) no palco escuro. Erro em vermelho, certo em verde."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-015_algarismos_significativos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regua", "regras", "contas", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EST = "#D98A00"   # o algarismo estimado
C_ESC = "#3CC7D3"
assert round(2.5 * 3.14, 2) == 7.85 and round(6.0 * 1.25, 3) == 7.5 and abs(4.20e-2 - 0.0420) < 1e-12 and abs(3.05e-3 - 0.00305) < 1e-12


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


def larg_digitos(s, size):
    return sum(E.larg(ch, "g", size) for ch in s) + size * 0.03 * (len(s) - 1)


def digitos(c, s, x, y, size, cores=None, a=1.0, align="left", padrao=TINTA):
    """número algarismo a algarismo; cores = {índice: cor}. Devolve a lista de centros x de cada caractere"""
    w = larg_digitos(s, size)
    xx = x - w / 2 if align == "center" else x
    xs = []
    for i, ch in enumerate(s):
        wc = E.larg(ch, "g", size)
        if a > 0:
            E.escreve(c, ch, xx, y, size, "g", (cores or {}).get(i, padrao), a)
        xs.append(xx + wc / 2)
        xx += wc + size * 0.03
    return xs


def digitos_em(c, t, t0, s, x, y, size, cores=None, align="left", padrao=TINTA):
    E.foco(c, t, t0, 0.5, lambda a: digitos(c, s, x, y, size, cores, a, align, padrao))


def sig(c, t, t0, n, cx, y, size=40, cor=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"{n} signif.", cx, y, size, "g", fundo=cor or COR, a=a))


# cores de 0,0420: zeros da esquerda em cinza, 4 e 2 certos, o zero do fim estimado
C0420 = {0: CINZA, 1: CINZA, 2: CINZA, 3: COR, 4: COR, 5: EST}


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        # o fio
        x0, x1, y = 260, 1660, 300
        p = ease_io(prog(t, C["s01.a"], 0.9))
        if p > 0:
            pts = [(lerp(x0, x1, i / 60), y + 10 * math.sin(i / 60 * math.pi * 3)) for i in range(int(60 * p) + 1)]
            path = skia.Path(); path.moveTo(*pts[0])
            for q in pts[1:]:
                path.lineTo(*q)
            c.drawPath(path, M.paint(COR, 1, stroke=10, cap_round=True))
        E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: E.pilula(c, "2,5 m", (x0 + x1) / 2, y - 80, 56, "g", a=a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "3,14 g por metro", (x0 + x1) / 2, y + 90, 46, "g", fundo=TINTA, a=a))
        # a calculadora
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (M.rrect(c, 560, 470, 800, 250, 30, TINTA, a),
                                                M.rrect(c, 600, 510, 720, 170, 18, "#C9D8C5", a)))
        E.foco(c, t, C["s01.c"] + 0.2, 0.4, lambda a: digitos(c, "7,85", 1290 - larg_digitos("7,85", 140), 640, 140,
                                                               {3: ERRADO if t >= C["s01.d"] else TINTA}, a))
        if t >= C["s01.d"] + 0.3:
            xs = digitos(None, "7,85", 1290 - larg_digitos("7,85", 140), 640, 140, a=0)
            E.risco(c, xs[3] - 50, 660, xs[3] + 50, 530, t, C["s01.d"] + 0.3, largura=12)
        E.frase(c, t, C["s01.d"], [("inventado", "g", 64, ERRADO)], 1440, 800)
        E.frase(c, t, C["s01.e"], [("honesto:", "i", 80)], 560, 900)
        bola_txt(c, t, C["s01.e"] + 0.3, "7,9 g", 1000, 870, 100, 72, CERTO)
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("algarismos", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.4, [("significativos", "g", 120, COR)], XE, 580)
        E.frase(c, t, C["s02.a"] + 3.0, ps("e o arredondamento certo", "i", 70, TINTA2), XE, 710, passo=0.1)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 190, "center")
    x, w = 200, 1520
    for k, y in (("s03.b", 290), ("s03.c", 610)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 270, p, prog_=p)
    k = C["s03.b"]
    E.frase(c, t, k, [("arredondar", "g", 66, COR)], 260, 380)
    E.frase(c, t, k + 1.0, ps("olhe o algarismo seguinte: 5 ou mais, sobe", "i", 54), 260, 470, passo=0.08)
    E.foco(c, t, k + 3.0, 0.5, lambda a: (digitos(c, "3,146", 1180, 420, 90, {4: EST}, a), E.escreve(c, "→  3,15", 1460, 420, 90, "g", COR, a)))
    k = C["s03.c"]
    E.frase(c, t, k, [("notação", "g", 66, COR), ("científica", "g", 66, COR)], 260, 700)
    E.frase(c, t, k + 1.4, ps("frente de 1 até menos de 10", "i", 54), 260, 790, passo=0.08)
    E.cientifica(c, t, k + 2.6, "4,5", 7, 1200, 760, 100)
    E.frase(c, t, C["s04"] - 2.4, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 980, "center", passo=0.1)


# ---------------- a régua ----------------
RX0, RU = 230, 112  # zero da régua e pixels por centímetro


def regua(c, t, t0, y):
    a = ep(t, t0, 0.5)
    if a <= 0:
        return
    M.rrect(c, RX0 - 40, y, 14 * RU + 80, 130, 14, "#F7E7B5", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(RX0 - 40, y, 14 * RU + 80, 130), 14, 14), M.paint(TINTA, a, stroke=3))
    for i in range(15):
        q = ep(t, t0 + 0.02 * i, 0.3)
        M.line(c, RX0 + i * RU, y, RX0 + i * RU, y + 46, TINTA, q, 4)
        E.centro(c, str(i), RX0 + i * RU, y + 100, 40, "b", TINTA, q)


def lapis(c, t, t0, y, comp=12.3):
    p = ease_io(prog(t, t0, 0.8))
    if p <= 0:
        return
    L = comp * RU * p
    M.rrect(c, RX0, y, max(1, L - 50), 60, 8, COR, 1)
    if p > 0.95:
        path = skia.Path(); path.addPoly([(RX0 + L - 50, y), (RX0 + L, y + 30), (RX0 + L - 50, y + 60)], True)
        c.drawPath(path, M.paint("#E8C48A"))
        c.drawCircle(RX0 + L - 6, y + 30, 6, M.paint(TINTA))


def b_regua(c, t, C, b):
    yr, yl = 420, 330
    regua(c, t, C["s04.a"], yr)
    lapis(c, t, C["s04.b"] - 0.6, yl)
    if t >= C["s04.d"]:
        q = ep(t, C["s04.d"], 0.4)
        xl = RX0 + 12.3 * RU
        M.line(c, xl, yl - 10, xl, yr + 60, EST, q, 4, dash=E.TRACO)
        c.drawRect(skia.Rect.MakeLTRB(RX0 + 12 * RU, yr + 2, RX0 + 13 * RU, yr + 48), M.paint(EST, 0.25 * q))
    E.frase(c, t, C["s04"], [("toda", "i", 72), ("medida", "i", 72), ("tem", "i", 72), ("um", "i", 72), ("limite", "g", 72, COR)], XE, 200)

    def s04():
        digitos_em(c, t, C["s04.b"], "12,3", XE + 120, 800, 170, {0: COR if t >= C["s04.c"] else TINTA, 1: COR if t >= C["s04.c"] else TINTA,
                                                                    3: EST if t >= C["s04.d"] else TINTA})
        E.escreve(c, "cm", XE + 520, 800, 70, "i", TINTA2, ep(t, C["s04.b"] + 0.3, 0.4))
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.pilula(c, "certos", XE + 230, 880, 44, "g", fundo=COR, a=a))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "estimado", XE + 450, 880, 44, "g", fundo=EST, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("certos", "g", 64, COR), ("+", "g", 64), ("o", "i", 66), ("1º", "g", 64, EST), ("estimado", "g", 64, EST)], XE, 700)
    E.frase(c, t, C["s05.a"], [("=", "i", 70), ("algarismos", "g", 70), ("significativos", "g", 70, COR)], XE, 800)
    E.foco(c, t, C["s05.b"], 0.4, lambda a: (digitos(c, "12,3", XE, 960, 100, {0: COR, 1: COR, 3: EST}, a), E.pilula(c, "3 signif.", XE + 380, 930, 44, "g", a=a)))
    E.foco(c, t, C["s05.c"], 0.4, lambda a: digitos(c, "12,345", 1150, 960, 100, {0: COR, 1: COR, 3: EST, 4: ERRADO, 5: ERRADO}, a))
    E.foco(c, t, C["s05.c"] + 0.5, 0.4, lambda a: E.pilula(c, "inventado", 1450, 1015, 40, "g", fundo=ERRADO, a=a))


# ---------------- as regras ----------------
def b_regras(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("três", "g", 80, COR), ("regras", "i", 84)], XE, 200)

    def s06():
        E.frase(c, t, C["s06.b"], [("1", "g", 70, COR), ("diferente", "i", 66), ("de", "i", 66), ("zero:", "i", 66), ("conta", "g", 66, CERTO)], XE, 360)
        digitos_em(c, t, C["s06.b"] + 1.2, "3,14", 1250, 360, 110, {0: COR, 2: COR, 3: EST})
        E.frase(c, t, C["s06.c"], [("2", "g", 70, COR), ("zero", "i", 66), ("no", "i", 66), ("meio:", "i", 66), ("conta", "g", 66, CERTO)], XE, 560)
        digitos_em(c, t, C["s06.d"], "205", 1250, 560, 110, {0: COR, 1: COR, 2: EST})
        sig(c, t, C["s06.d"] + 0.4, 3, 1660, 525)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("3", "g", 70, COR), ("zero", "i", 66), ("à", "i", 66), ("esquerda:", "i", 66), ("não", "g", 66, ERRADO), ("conta", "g", 66, ERRADO)],
            XE, 340)
    s = "0,0420"
    x0 = W / 2 - larg_digitos(s, 200) / 2
    cc = {}
    if t >= C["s07.c"]:
        cc.update({0: CINZA, 1: CINZA, 2: CINZA})
    if t >= C["s07.d"]:
        cc.update({5: EST})
    if t >= C["s08.b"]:
        cc.update({3: COR, 4: COR})
    xs = digitos(None, s, x0, 640, 200, a=0)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: digitos(c, s, x0, 640, 200, cc, a))
    E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: E.pilula(c, "só o lugar da vírgula", (xs[0] + xs[2]) / 2, 720, 40, "g", fundo=CINZA, a=a))
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "medido até aqui: conta", xs[5] + 40, 430, 40, "g", fundo=EST, a=a))
    E.frase(c, t, C["s08.a"], [("3", "g", 96, COR), ("significativos", "g", 80, COR)], W / 2, 900, "center")


# ---------------- nas contas ----------------
def b_contas(c, t, C, b):
    y = 420

    def s09_10():
        E.frase(c, t, C["s09.a"], [("multiplicar", "g", 66), ("ou", "i", 66), ("dividir:", "g", 66)], XE, 200)
        E.frase(c, t, C["s09.b"], ps("manda a medida com menos significativos", "i", 56, TINTA2), XE, 290, passo=0.08)
        x = 300
        digitos_em(c, t, C["s09.c"] - 0.6, "2,5", x, y, 130, {0: COR, 2: EST})
        E.foco(c, t, C["s09.c"] - 0.4, 0.4, lambda a: E.escreve(c, "×", x + 270, y, 110, "g", TINTA, a))
        digitos_em(c, t, C["s09.c"] - 0.2, "3,14", x + 430, y, 130, {0: COR, 2: COR, 3: EST})
        E.foco(c, t, C["s09.c"] + 0.4, 0.4, lambda a: E.escreve(c, "=", x + 790, y, 110, "g", TINTA, a))
        cores_r = {}
        if t >= C["s10.b"]:
            cores_r = {0: COR, 2: EST, 3: ERRADO}
        digitos_em(c, t, C["s09.c"] + 0.6, "7,85", x + 940, y, 130, cores_r)
        sig(c, t, C["s09.c"], 2, x + 110, y + 90)
        sig(c, t, C["s09.d"], 3, x + 560, y + 90)
        sig(c, t, C["s09.e"], 2, x + 1060, y + 90, cor=CERTO)
        if t >= C["s10.c"] + 0.4:
            xs = digitos(None, "7,85", x + 940, y, 130, a=0)
            E.risco(c, xs[3] - 45, y + 20, xs[3] + 45, y - 100, t, C["s10.c"] + 0.4, largura=11)
        E.frase(c, t, C["s10.c"], ps("o seguinte é 5: o 8 sobe", "i", 60), XE, 720, passo=0.1)
        bola_txt(c, t, C["s10.d"], "7,9 g", 1000, 880, 110, 76, CERTO)
    E.saida(c, t, C["s11"] - 0.1, s09_10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], [("por", "i", 90), ("quê?", "g", 90, COR)], XE, 260)
    digitos_em(c, t, C["s11.a"], "2,5", XE, 480, 150, {0: COR, 2: EST})
    E.foco(c, t, C["s11.a"] + 0.4, 0.4, lambda a: E.pilula(c, "dúvida nos décimos", XE + 520, 440, 46, "g", fundo=EST, a=a))
    E.frase(c, t, C["s11.b"], ps("a conta não fica mais precisa", "i", 66), XE, 680, passo=0.1)
    E.frase(c, t, C["s11.b"] + 1.6, ps("que a medida mais pobre", "i", 66), XE, 780, passo=0.1)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "regra de × e ÷", XE + 300, 920, 50, "g", a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 220)
    E.frase(c, t, C["s12.a"], ps("contar os zeros da esquerda", "i", 70), XE, 350, passo=0.1)
    s = "0,0420"
    x0 = W / 2 - larg_digitos(s, 180) / 2
    xs = digitos(None, s, x0, 600, 180, a=0)
    cores = C0420 if t >= C["s12.d"] else {}
    E.foco(c, t, C["s12.a"] + 0.6, 0.5, lambda a: digitos(c, s, x0, 600, 180, cores, a))
    if C["s12.b"] <= t < C["s12.d"]:
        for k_, j in enumerate((0, 2, 3, 4, 5)):
            E.foco(c, t, C["s12.b"] + 0.12 * k_, 0.3, lambda a, j=j, k_=k_: E.centro(c, str(k_ + 1), xs[j], 690, 46, "g", ERRADO, a))
        E.foco(c, t, C["s12.b"] + 0.8, 0.4, lambda a: E.escreve(c, "5?", x0 + larg_digitos(s, 180) + 60, 600, 120, "g", ERRADO, a))
        if t >= C["s12.b"] + 1.4:
            E.risco(c, x0 + larg_digitos(s, 180) + 40, 620, x0 + larg_digitos(s, 180) + 200, 500, t, C["s12.b"] + 1.4, largura=12)
    E.frase(c, t, C["s12.c"], ps("número pequeno não é mais preciso", "i", 60, TINTA2), W / 2, 830, "center", passo=0.08)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "zeros da esquerda = lugar da vírgula", W / 2, 940, 50, "g", fundo=CINZA, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 200, "center")
        E.frase(c, t, C["s13.a"], [("notação", "g", 100, BR), ("científica", "g", 100, BR)], W / 2, 340, "center")
        s = "0,0420"
        E.foco(c, t, C["s13.b"], 0.5, lambda a: digitos(c, s, 500 - larg_digitos(s, 130) / 2, 580, 130, {0: "#77778A", 1: "#77778A", 2: "#77778A"}, a, padrao=BR))
        E.foco(c, t, C["s13.b"] + 0.6, 0.4, lambda a: E.escreve(c, "=", 840, 580, 110, "g", CLARO, a))
        E.cientifica(c, t, C["s13.b"] + 1.0, "4,20", -2, 960, 580, 130, BR, C_ESC)
        E.frase(c, t, C["s13.c"], ps("os zeros da esquerda somem", "i", 64, CLARO), W / 2, 760, "center", passo=0.1)
        E.frase(c, t, C["s13.d"], [("4,20:", "g", 76, C_ESC), ("3", "g", 76, BR), ("significativos", "g", 76, BR)], W / 2, 900, "center")
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("potência:", "g", 64, C_ESC), ("lugar", "i", 66, CLARO), ("da", "i", 66, CLARO), ("vírgula", "i", 66, CLARO)], W / 2, 220, "center")
    E.frase(c, t, C["s14.b"], [("frente:", "g", 64, BR), ("a", "i", 66, CLARO), ("medida", "g", 66, BR)], W / 2, 320, "center")
    E.frase(c, t, C["s14.c"], [("4", "g", 90, BR), ("200", "g", 90, BR), ("com", "i", 76, CLARO), ("3", "g", 90, BR), ("significativos?", "i", 76, CLARO)],
            W / 2, 500, "center")
    E.cientifica(c, t, C["s14.d"], "4,20", 3, W / 2, 660, 110, BR, C_ESC, align="center")
    E.frase(c, t, C["s14.e"], [("não", "g", 66, ERRADO), ("compensa", "i", 70, CLARO), ("em", "i", 70, CLARO), ("3,14:", "g", 66, BR), ("conte", "i", 70, CLARO),
                               ("direto", "g", 66, BR)], W / 2, 880, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("1)", "g", 64, COR), ("significativos", "i", 70), ("de", "i", 70)], XE, 380)
    digitos_em(c, t, C["s15.a"] + 0.6, "0,00305", XE + 80, 520, 120)
    E.frase(c, t, C["s15.b"], [("2)", "g", 64, COR)], XE, 720)
    E.foco(c, t, C["s15.b"] + 0.2, 0.4, lambda a: E.escreve(c, "6,0 × 1,25 = ?", XE + 100, 720, 100, "g", TINTA, a))
    E.frase(c, t, C["s15.b"] + 2.0, ps("com os significativos certos", "i", 56, TINTA2), XE + 100, 820, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1480, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        s = "0,00305"
        x0 = 330
        cc = {}
        if t >= C["s17.a"]:
            cc.update({0: CINZA, 1: CINZA, 2: CINZA, 3: CINZA})
        if t >= C["s17.b"]:
            cc.update({4: COR, 5: COR, 6: EST})
        digitos(c, s, x0, 400, 170, cc, ep(t, C["s17"], 0.4))
        sig(c, t, C["s17.c"], 3, x0 + larg_digitos(s, 170) + 200, 350, 56, CERTO)
        E.cientifica(c, t, C["s17.d"], "3,05", -3, W / 2, 700, 120, TINTA, COR, align="center")
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    cores6 = {0: COR, 2: EST} if t >= C["s18.b"] else {}
    E.foco(c, t, C["s18.a"], 0.5, lambda a: (digitos(c, "6,0", 300, 400, 120, cores6, a),
                                            E.escreve(c, " × 1,25 = 7,5", 300 + larg_digitos("6,0", 120) + 10, 400, 120, "g", TINTA, a)))
    sig(c, t, C["s18.b"] + 0.4, 2, 390, 490)
    sig(c, t, C["s18.c"], 3, 680, 490, cor=TINTA)
    E.frase(c, t, C["s18.b"] + 1.2, ps("o zero do fim conta", "i", 56, TINTA2), 300, 620, passo=0.1)
    bola_txt(c, t, C["s18.d"], "7,5", 1300, 760, 120, 90, CERTO)
    sig(c, t, C["s18.d"] + 0.4, 2, 1300, 940, cor=CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", [("certos", "g", 70, COR), ("+", "g", 70), ("o", "i", 72), ("1º", "g", 70, EST), ("estimado", "g", 70, EST)]),
                 ("s19.b", [("zero", "i", 72), ("à", "i", 72), ("esquerda", "i", 72), ("não", "g", 70, ERRADO), ("conta", "g", 70)]),
                 ("s19.c", [("×", "g", 70, COR), ("e", "i", 72), ("÷:", "g", 70, COR), ("manda", "i", 72), ("a", "i", 72), ("medida", "i", 72), ("mais", "i", 72),
                            ("pobre", "g", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s20.a"], [("Troncos", "g", 150, COR)], XE, 460)
    E.frase(c, t, C["s20.b"], [("de", "i", 110), ("cone", "g", 130, COR), ("e", "i", 110), ("pirâmide", "g", 130, COR)], XE, 610)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(620, 325, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regua=b_regua, regras=b_regras, contas=b_contas, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
