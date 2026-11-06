"""Visual — Estudativo · MAT-NUM-007: multiplicar por 10, por 100 e por um algarismo.
Identidade em _ferramentas/editorial.py. O quadro de casas mostra o algarismo subindo de casa, os envelopes mostram o número
quebrado em notas e moedas, e E.conta_mult refaz a conta armada. Painel à direita: o passo que a voz está dizendo.
Peças locais: envelope e nota (retângulo simples, nunca cópia de cédula real)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-007_multiplicar_por_10_100_e_um_algarismo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("zeros", "quebrar", "conta", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def lin(c, t, t0, s, x, y, size=64, estilo="b", cor=None):
    """uma linha do painel ao lado da conta"""
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, estilo, cor or TINTA, a))


def igual(c, t, t0, t1, s1, s2, x, y, size=66, estilo="b", cor=None, cor2=None):
    """conta em duas partes: a pergunta em t0 e o resultado só em t1, quando a voz chega nele"""
    lin(c, t, t0, s1, x, y, size, estilo, cor)
    lin(c, t, t1, s2, x + E.larg(s1 + " ", estilo, size), y, size, estilo, cor2 or cor or COR)


def lista(c, t, C, ini, ta, n, itens):
    E.frase(c, t, C[ini] + 0.7, [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
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


def envelope(c, x, y, w, h, a):
    """envelope aberto: retângulo com a aba em V, onde a nota e as moedas ficam"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 12, E.VAZIO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 12, 12), M.paint(TINTA, a, stroke=3))
    M.line(c, x + 6, y + 4, x + w / 2, y + 54, TINTA2, a, 3)
    M.line(c, x + w - 6, y + 4, x + w / 2, y + 54, TINTA2, a, 3)


def nota(c, x, y, w, h, s, a):
    """nota simples na cor da matéria: retângulo com o valor, nunca cópia de cédula real"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 8, E.COR, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 7, y + 7, w - 14, h - 14), 4, 4), M.paint(E.SOBRE, 0.5 * a, stroke=2))
    E.centro(c, s, x + w / 2, y + h / 2 + 18, 50, "g", E.SOBRE, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def tudo():
        ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
        E.linha(c, t, [("6 parcelas", "g", 120, COR, ka), ("de", "i", 110, TINTA, kb - 0.3), ("R$ 47", "g", 120, TINTA, kb)], W / 2, 260, "center")
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "R$ 242", W / 2, 530, 220, "g", ERRADO, a))
        E.frase(c, t, kd, [("faltaram", "i", 120), ("R$ 40", "g", 120, ERRADO)], W / 2, 720, "center", passo=0.3)
        E.frase(c, t, lerp(kd, C["s01.end"], 0.48), [("um", "i", 92), ("número", "i", 92), ("pequeno", "g", 84, COR), ("que", "i", 92), ("muita", "i", 92), ("gente", "i", 92), ("esquece", "i", 92)], W / 2, 900, "center", passo=0.3)
    E.saida(c, t, C["s02"] - 0.1, tudo)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 520, 270 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("desta", "i", 90), ("aula", "i", 90)], XE, 340)
        E.frase(c, t, lerp(ta, tb, 0.27), [("multiplicar", "g", 110)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.33), [("por", "i", 100), ("10", "g", 110, COR), ("e", "i", 100), ("por", "i", 100), ("100", "g", 110, COR)], XE, 620, passo=0.25)
        E.frase(c, t, lerp(ta, tb, 0.6), [("armar", "g", 84), ("a", "i", 84), ("conta", "g", 84)], XE, 790, passo=0.25)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1500, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1500, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lista(c, t, C, "s03", "s03.a", 3, (("s03.b", "saber o valor", "de cada algarismo"), ("s03.c", "somar", "com vai um"), ("s03.d", "a", "tabuada")))


# ---------------- vezes dez e vezes cem ----------------
QX, QW, QY, QS, QH = 170, 190, 300, 104, 150


def cel(i):
    return QX + (i + 0.5) * QW


def lin_y(j):
    return QY + QH * j + QS * 1.02


def b_zeros(c, t, C, b):
    def quadro():
        ka, kb, kc, kd, ke = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]
        z5, h6, z6 = C["s05.b"], C["s06.a"], C["s06.b"]
        E.quadro_casas(c, t, ("milhar", "centena", "dezena", "unidade"), (h6, ke, kc, kb),
                       [[("", 0), ("", 0), ("3", ka), ("7", ka)],
                        [("", 0), ("3", ke + 0.3), ("7", kc + 0.3), ("0", z5, COR)],
                        [("3", h6), ("7", h6), ("0", z6, COR), ("0", z6 + 0.25, COR)]], QX, QY, QW, QS, QH, grossa=None)
        # cada algarismo sobe para a casa da esquerda
        for i, tk in ((3, kc), (2, ke)):
            p = ep(t, tk, 0.4)
            if p > 0:
                M.arrow(c, cel(i) - 24, lin_y(0) + 16, cel(i - 1) + 34, lin_y(1) - 84, COR, p, 5, 18, p)
        E.saida(c, t, C["s06"] - 0.1, lambda: E.frase(c, t, C["s04.a"], [("quanto", "i", 84), ("é", "i", 84), ("37", "g", 84, COR), ("×", "g", 84), ("10?", "g", 84, COR)], W / 2, 170, "center", passo=0.16))
        if t >= C["s06"]:
            E.frase(c, t, C["s06"] + 0.1, [("vezes", "i", 84), ("100", "g", 84, COR)], W / 2, 170, "center")
        xp = 1000
        lin(c, t, ka, "37", xp, lin_y(0), 80)
        lin(c, t, C["s05.c"], "37 × 10 = 370", xp, lin_y(1), 80, "b", COR)
        igual(c, t, C["s06.c"], C["s06.d"], "37 × 100 =", "3.700", xp, lin_y(2), 80)

        def fala5():
            E.frase(c, t, C["s05.a"], [("subiu", "g", 80, COR), ("uma", "i", 84), ("casa", "i", 84)], XE, 900, passo=0.16)
            E.frase(c, t, lerp(C["s05.a"], C["s05.b"], 0.5), [("casa", "i", 84), ("vazia:", "i", 84)], xp, 900, passo=0.16)
            E.frase(c, t, C["s05.b"], [("zero", "g", 80, COR)], xp + 350, 900)
        E.saida(c, t, C["s06"] - 0.1, fala5)
        if t >= C["s06"]:
            E.frase(c, t, C["s06.a"] - 0.3, [("sobe", "i", 84), ("duas", "g", 80, COR), ("casas", "i", 84)], XE, 900, passo=0.16)
            E.frase(c, t, C["s06.b"], [("dois", "g", 80, COR), ("zeros", "i", 84)], xp, 900, passo=0.16)
    E.saida(c, t, C["s07"] - 0.1, quadro)
    if t >= C["s07"]:
        ka, kb, kc = C["s07.a"], C["s07.b"], C["s07.c"]
        E.frase(c, t, C["s07"] + 0.1, [("a", "i", 88), ("regra,", "i", 88, COR), ("para", "i", 88), ("números", "i", 88), ("inteiros", "g", 80)], W / 2, 180, "center", passo=0.2)
        E.foco(c, t, ka, 0.5, lambda a: E.pilula(c, "× 10", 340, 345, 76, estilo="g", cor=E.SOBRE, a=a))
        E.frase(c, t, ka + 0.3, [("acrescente", "i", 84), ("um", "g", 76), ("zero", "g", 76, COR), ("no", "i", 84), ("fim", "i", 84)], 560, 372, passo=0.22)
        E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "× 100", 340, 530, 76, estilo="g", cor=E.SOBRE, a=a))
        E.frase(c, t, kb + 0.3, [("acrescente", "i", 84), ("dois", "g", 76), ("zeros", "g", 76, COR)], 560, 557, passo=0.22)
        E.frase(c, t, lerp(kb, kc, 0.3), [("vale", "i", 76), ("também", "i", 76), ("para", "i", 76), ("quem", "i", 76), ("já", "i", 76), ("termina", "i", 76), ("em", "i", 76), ("zero", "g", 68)], W / 2, 730, "center", passo=0.25)
        fim = lerp(kc, C["s07.end"], 0.3)
        xc = 620
        E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "40 × 10 =", xc, 880, 110, "g", TINTA, a))
        E.foco(c, t, fim, 0.5, lambda a: E.escreve(c, "400", xc + E.larg("40 × 10 = ", "g", 110), 880, 110, "g", COR, a))


# ---------------- quebrar o número ----------------
EX, EY, EW, EH, EP = 172, 236, 240, 300, 267


def b_quebrar(c, t, C, b):
    E.frase(c, t, C["s08"] + 0.1, [("e", "i", 84), ("quando", "i", 84), ("o", "i", 84), ("número", "i", 84), ("não", "g", 76), ("é", "i", 84), ("redondo?", "g", 76, COR)], XE, 170, passo=0.2) if t < C["s08.a"] else None
    if t >= C["s08.a"]:
        E.frase(c, t, C["s08.a"], [("6", "g", 110, COR), ("×", "g", 110), ("23", "g", 110, COR)], W / 2, 180, "center", passo=0.16)
    ka_m = 1 - 0.75 * ep(t, C["s09.a"], 0.4) + 0.75 * ep(t, C["s10.a"], 0.4)
    ka_n = 1 - 0.75 * ep(t, C["s10.a"], 0.4) + 0.75 * ep(t, C["s10.b"], 0.4)
    for i in range(6):
        x = EX + i * EP
        E.foco(c, t, C["s08.b"] + i * 0.12, 0.45, lambda a, x=x: envelope(c, x, EY, EW, EH, a))
        E.foco(c, t, C["s08.c"] + i * 0.1, 0.4, lambda a, x=x: nota(c, x + 24, EY + 72, EW - 48, 104, "R$ 20", a * ka_n))
        E.foco(c, t, C["s08.d"] + i * 0.1, 0.4, lambda a, x=x: [E.moeda(c, x + 48 + j * 72, EY + 234, 34, "1", a * ka_m) for j in range(3)])

    def rotulos():
        lin(c, t, C["s08.c"], "uma nota de R$ 20", XE, 680, 66, "b", COR)
        lin(c, t, C["s08.d"], "3 moedas de R$ 1", 1000, 680, 66, "b", COR)
    E.saida(c, t, C["s09"] - 0.1, rotulos)
    if t >= C["s09"]:
        ka, kb, kc = C["s09.a"], C["s09.b"], C["s09.c"]
        E.frase(c, t, C["s09"] + 0.1, [("junte", "i", 70), ("as", "i", 70), ("notas", "i", 70, COR)], XE, 660, passo=0.16)
        lin(c, t, ka, "6 × 20", XE + 390, 660, 70)
        igual(c, t, kb, lerp(kb, kc, 0.6), "6 × 2 =", "12", XE, 780, 70)
        igual(c, t, kc, lerp(kc, C["s09.end"], 0.45), "com o zero:", "120", XE, 900, 70)
    if t >= C["s10"]:
        ka, kb, kc, kd = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
        xp = 1000
        E.frase(c, t, C["s10"] + 0.1, [("junte", "i", 70), ("as", "i", 70), ("moedas", "i", 70, COR)], xp, 660, passo=0.16)
        igual(c, t, ka, lerp(ka, kb, 0.6), "6 × 3 =", "18", xp + 430, 660, 70)
        lin(c, t, kb, "120 + 18 =", xp, 780, 70)
        bola_txt(c, t, kc, "138", 1600, 830, 112, 84)
        lin(c, t, kd, "23 = 20 + 3", xp, 900, 70, "b", COR)


# ---------------- conta armada ----------------
XV, Y0, SZ, XP = 720, 400, 130, 1000


def b_conta(c, t, C, b):
    a2, a3 = C["s12.b"], C["s13.c"]
    E.frase(c, t, C["s11"] + 0.1, [("a", "i", 80), ("conta", "i", 80), ("armada", "g", 72, COR)], W / 2, 170, "center")
    E.conta_mult(c, t, 47, 6, (C["s11.a"], C["s11.b"]), [[a2, a3, a3 + 0.3]], XV, Y0, SZ, vai=[(1, "4", C["s12.c"], a3)])

    def fala11():
        lin(c, t, lerp(C["s11"], C["s11.a"], 0.55), "começando pelas unidades", XP, 320, 62, "i", COR)
        lin(c, t, C["s11.a"], "47 × 6", XP, 430, 72)
        lin(c, t, C["s11.b"], "o 6 embaixo do 7", XP, 540, 66)
        lin(c, t, lerp(C["s11.b"], C["s11.end"], 0.27), "a ordem não muda", XP, 680, 66, "i")
        lin(c, t, lerp(C["s11.b"], C["s11.end"], 0.6), "3 × 4 = 4 × 3", XP, 790, 72, "b", COR)
    E.saida(c, t, C["s12"] - 0.1, fala11)

    def fala12():
        igual(c, t, C["s12.a"], lerp(C["s12.a"], C["s12.b"], 0.55), "6 × 7 =", "42", XP, 340, 80)
        lin(c, t, C["s12.b"], "escreva o 2", XP, 470, 72)
        lin(c, t, C["s12.c"], "o 4 sobe", XP, 590, 72, "g", COR)
        E.frase(c, t, lerp(C["s12.c"], C["s12.end"], 0.45), [("vai um", "g", 66, COR), ("mesmo", "i", 72), ("quando", "i", 72), ("vão", "i", 72), ("4", "g", 72)], XP, 730, passo=0.18)
    if t >= C["s12"]:
        E.saida(c, t, C["s13"] - 0.1, fala12)

    def fala13():
        igual(c, t, C["s13.a"], lerp(C["s13.a"], C["s13.b"], 0.6), "6 × 4 =", "24", XP, 340, 80)
        igual(c, t, C["s13.b"], lerp(C["s13.b"], C["s13.c"], 0.25), "com o 4 que subiu:", "28", XP, 460, 66)
        lin(c, t, lerp(C["s13.b"], C["s13.c"], 0.42), "ninguém precisa subir", XP, 580, 66, "i")
        lin(c, t, C["s13.c"], "escreva o 28 inteiro", XP, 690, 66, "g", COR)
        bola_txt(c, t, lerp(C["s13.d"], C["s13.end"], 0.2), "282", 1300, 855, 112, 84)
    if t >= C["s13"]:
        E.saida(c, t, C["s14"] - 0.1, fala13)

    if t >= C["s14"]:
        lin(c, t, C["s14"] + 0.1, "confira quebrando", XP, 330, 72, "i", COR)
        igual(c, t, C["s14.a"], lerp(C["s14.a"], C["s14.b"], 0.5), "6 × 40 =", "240", XP, 470, 76)
        igual(c, t, C["s14.b"], lerp(C["s14.b"], C["s14.c"], 0.5), "6 × 7 =", "42", XP, 590, 76)
        igual(c, t, C["s14.c"], lerp(C["s14.c"], C["s14.end"], 0.3), "240 + 42 =", "282", XP, 710, 76)
        E.foco(c, t, lerp(C["s14.c"], C["s14.end"], 0.75), 0.5, lambda a: E.selo(c, XP + 110, 860, 76, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kcc, kd, ke, kf = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"], C["s15.f"]
    xv, y, s = 620, 400, 120
    xp = 880
    E.frase(c, t, ka, [("esquecer", "g", 80, ERRADO), ("de", "i", 88), ("somar", "i", 88), ("o", "i", 88), ("que", "i", 88), ("subiu", "g", 80, ERRADO)], W / 2, 170, "center", passo=0.16)

    def monta(a):
        E.numero(c, "47", xv, y, s, "g", TINTA, a)
        E.numero(c, "6", xv, y + 140, s, "g", TINTA, a)
        E.escreve(c, "×", xv - 3 * s * 0.72, y + 140, s, "g", TINTA, a)
    E.foco(c, t, ka, 0.5, monta)
    if t >= ka:
        M.line(c, xv - 3.2 * s * 0.72, y + 172, xv + 10, y + 172, TINTA, 1.0, 6, progress=ep(t, ka + 0.2, 0.5))
    x4 = E._centros("47", xv, s)[0]
    E.foco(c, t, ka + 0.4, 0.4, lambda a: E.centro(c, "4", x4, y - 112, 62, "g", CERTO, a), sobe=-12)
    E.foco(c, t, kcc, 0.5, lambda a: E.numero(c, "242", xv, y + 310, s, "g", ERRADO, a))
    if t >= kd:
        q = ep(t, kd, 0.3)
        E.caixa_pontilhada(c, x4 - 44, y - 170, 88, 76, q, ERRADO, prog_=q)

    def fase1():
        igual(c, t, kb - 0.7, kb, "6 × 4 =", "24", xp, 340, 80)
        E.frase(c, t, lerp(kb, kcc, 0.4), [("ignora", "i", 76), ("o", "i", 76), ("vai um", "g", 68, ERRADO)], xp, 470, passo=0.16)
        lin(c, t, kd, "aquele 4 são 4 dezenas:", xp, 600, 64)
        lin(c, t, lerp(kd, ke, 0.4), "R$ 40", xp, 700, 80, "g", ERRADO)
        E.frase(c, t, ke - 0.8, [("o", "i", 66), ("que", "i", 66), ("subiu", "i", 66), ("sempre", "g", 60, COR), ("entra", "g", 60, COR), ("na", "i", 66), ("conta", "i", 66)], xp, 840, passo=0.2)
    E.saida(c, t, lerp(ke, kf, 0.3) - 0.1, fase1)
    if t >= lerp(ke, kf, 0.3):
        E.frase(c, t, lerp(ke, kf, 0.32), [("dava", "i", 84), ("para", "i", 84), ("desconfiar", "g", 76, COR)], xp, 360, passo=0.16)
        lin(c, t, lerp(ke, kf, 0.56), "47 é quase 50", xp, 500, 76)
        igual(c, t, kf, lerp(kf, C["s15.end"], 0.3), "6 × 50 =", "300", xp, 630, 76)
        E.frase(c, t, lerp(kf, C["s15.end"], 0.42), [("242", "g", 76, ERRADO), ("ficou", "i", 84), ("longe", "i", 84), ("demais", "i", 84)], xp, 790, passo=0.25)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def cem():
        ka, kb, kc, kd, ke = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
        E.frase(c, t, C["s16"] + 0.1, [("agora,", "i", 76, CLARO), ("o", "i", 76, CLARO), ("atalho:", "i", 76, CLARO)], W / 2, 170, "center", passo=0.1)
        E.frase(c, t, ka, [("vezes", "i", 150, CLARO), ("99", "g", 170, BR)], W / 2, 360, "center", passo=0.2)
        E.frase(c, t, kb, [("99", "g", 92, BR), ("parcelas", "i", 100, CLARO), ("de", "i", 100, CLARO), ("R$ 6", "g", 92, BR)], W / 2, 530, "center", passo=0.2)
        y = 760
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "100 × 6", 340, y + 30, 100, "g", BR, a))
        E.foco(c, t, lerp(kc, kd, 0.6), 0.5, lambda a: E.centro(c, "= 600", 700, y + 30, 100, "g", BR, a))
        E.ponte(c, t, kd, 920, 1230, y, "− 6", CLARO, 60)
        E.foco(c, t, ke, 0.5, lambda a: E.centro(c, "594", 1470, y + 50, 150, "g", CLARO, a))
    E.saida(c, t, C["s17"] - 0.1, cem)
    if t >= C["s17"]:
        ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
        E.frase(c, t, ka, [("99", "g", 150, CLARO), ("=", "g", 130, BR), ("100", "g", 150, BR), ("−", "g", 130, BR), ("1", "g", 150, BR)], W / 2, 290, "center", passo=0.2)
        E.frase(c, t, lerp(ka, kb, 0.38), [("contou", "i", 80, CLARO), ("uma", "i", 80, CLARO), ("a", "i", 80, CLARO), ("mais,", "i", 80, CLARO), ("devolve", "g", 72, BR)], W / 2, 440, "center", passo=0.22)
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 300, 620, 72, True, a))
        E.frase(c, t, kb + 0.1, [("número", "i", 84, CLARO), ("colado", "g", 76, BR), ("em", "i", 84, CLARO), ("um", "i", 84, CLARO), ("redondo", "g", 76, BR)], 410, 648, passo=0.25)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 300, 800, 72, False, a))
        E.frase(c, t, kc + 0.1, [("longe", "i", 84, CLARO), ("disso,", "i", 84, CLARO), ("como", "i", 84, CLARO), ("35", "g", 80, BR)], 410, 828, passo=0.25)
        E.frase(c, t, lerp(kc, C["s17.end"], 0.72), [("arme", "g", 76, BR), ("a", "g", 76, BR), ("conta", "g", 76, BR)], 410, 940, passo=0.2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    E.frase(c, t, lerp(C["s18"], C["s18.a"], 0.5), [("compra", "i", 92), ("parcelada", "i", 92)], XE, 400, passo=0.3)
    E.frase(c, t, C["s18.a"], [("em", "i", 92), ("8", "g", 104, COR), ("vezes", "g", 92)], XE, 530, passo=0.2)
    E.frase(c, t, C["s18.b"], [("de", "i", 92), ("R$ 57", "g", 104, COR)], XE, 660, passo=0.2)
    E.frase(c, t, C["s18.c"], [("qual", "i", 110), ("é", "i", 110), ("o", "i", 110), ("total", "g", 100, COR), ("pago?", "g", 100, COR)], XE, 850, passo=0.22)
    E.relogio(c, t, C["s19.a"], 1490, 400, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kcc, kd, ke, kf = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"], C["s20.f"]
    t45 = lerp(ke, kf, 0.7)
    E.frase(c, t, C["s20"] + 0.1, [("vamos", "i", 80), ("lá", "i", 80, COR)], W / 2, 170, "center")
    E.conta_mult(c, t, 57, 8, (ka, ka + 0.3), [[kcc, t45, t45 + 0.25]], XV, Y0, SZ, vai=[(1, "5", kcc + 0.5, t45)])
    igual(c, t, kb, lerp(kb, kcc, 0.6), "8 × 7 =", "56", XP, 340, 80)
    lin(c, t, kcc, "escreva o 6, e o 5 sobe", XP, 450, 62, "b", COR)
    igual(c, t, kd, lerp(kd, ke, 0.6), "8 × 5 =", "40", XP, 580, 80)
    igual(c, t, ke, t45, "com o 5 que subiu:", "45", XP, 690, 66)
    bola_txt(c, t, kf + 0.5, "R$ 456", 1300, 860, 134, 62)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s21.a", "× 10 e × 100: acrescente zeros"), ("s21.b", "difícil: quebre em pedaços"), ("s21.c", "conta armada: some o que subiu"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 1, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 70)], 350, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s22.a"], [("dois", "g", 130, COR), ("algarismos", "g", 130, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s22.a"] + 0.5, [("também", "i", 80), ("no", "i", 80), ("número", "i", 80), ("de", "i", 80), ("baixo", "i", 80)], XE, 570, passo=0.12)
    E.frase(c, t, C["s22.b"], [("uma", "i", 80), ("segunda", "g", 72), ("linha", "g", 72, COR)], XE, 690, passo=0.2)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 710, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(960, 735, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, zeros=b_zeros, quebrar=b_quebrar, conta=b_conta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
