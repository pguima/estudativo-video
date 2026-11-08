"""Visual — Estudativo · MAT-FUN-003: notação f(x), calcular e fazer o caminho de volta.

Linguagem visual da trilha Funções (MAT-FUN-001 e 002): entrada (x, o número nos parênteses) em índigo, saída (f(x), o número
depois do igual) em preto; máquina escura com o nome "f" no canto, entrada em esfera índigo pela esquerda e saída em esfera preta
pela direita. Ida = setas para a direita; volta (desfazer) = setas para a esquerda, com a conta inversa.
Peças locais: mista() (texto com uma cor por parte), maquina(), passa(), caixa_em() (destaque pontilhado de um trecho)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-003_notacao_f_de_x.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("notacao", "calcular", "volta", "atalho", "questao", "fim"))
BR = "#FFFFFF"
f = lambda x: 2 * x + 3
assert f(5) == 13 and f(-2) == -1 and f(13.5) == 30 and f(30) == 63 and (30 - 3) / 2 == 13.5
P = lambda d: 5 + 2.5 * d
assert P(8) == 25 and P(14) == 40 and 350 / 25 == 14


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def mista(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """texto numa linha com uma cor por parte: partes = [(texto, cor)]; devolve (centro x, largura) de cada parte"""
    ws = [E.larg(s, est, size) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x
    cs = []
    for (s, cor), w in zip(partes, ws):
        E.escreve(c, s, xx, y, size, est, cor, a)
        cs.append((xx + w / 2, w))
        xx += w
    return cs


def mista_em(c, t, t0, partes, x, y, size, align="left", est="g"):
    E.foco(c, t, t0, 0.5, lambda a: mista(c, partes, x, y, size, a, align, est))
    return mista(c, partes, x, y, size, 0, align, est)


def caixa_em(c, t, t0, cx, w, y, size, cor, d=0.5):
    """caixa pontilhada em volta de um trecho já escrito (cx, w = centro e largura do trecho; y = linha de base)"""
    p = ep(t, t0, d)
    if p > 0:
        E.caixa_pontilhada(c, cx - w / 2 - 16, y - size * 0.86, w + 32, size * 1.12, p, cor, p)


def bolinha(c, X, Y, s, cor, a=1.0, r=62, size=None):
    if a <= 0:
        return
    size = size or (r * 0.95 if len(s) < 3 else r * 0.62 if len(s) < 5 else r * 0.5)
    E.bola(c, X, Y, r, cor, a)
    centro(c, s, X, Y + size * 0.36, size, "g", BR, a)


def maquina(c, cx, cy, regra, a=1.0, w=520, h=280, size=72, rotulos=True, nome="f"):
    """a máquina da função: caixa escura com a regra e o nome no canto; boca de entrada (índigo) à esquerda, de saída à direita"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 10, cy - h / 2 + 18, w, h), 40, 40), s)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 40, TINTA, a)
    M.rrect(c, cx - w / 2 - 22, cy - 66, 44, 132, 14, ENT, a)
    M.rrect(c, cx + w / 2 - 22, cy - 66, 44, 132, 14, TINTA2, a)
    if nome:
        E.escreve(c, nome, cx - w / 2 + 36, cy - h / 2 + 74, 64, "i", CLARO, a)
    if regra:
        E.formula(c, regra, cx, cy + size * 0.36 + 14, size, "g", BR, a, "center")
    if rotulos:
        centro(c, "entrada", cx - w / 2 - 150, cy + 120, 44, "i", ENT, a)
        centro(c, "saída", cx + w / 2 + 150, cy + 120, 44, "i", SAI, a)


def passa(c, t, cx, cy, ent, sai, t_in, t_out, w=520, some=None, r=58, dist=260):
    """a entrada rola até a boca e some; a saída nasce na outra boca e anda para fora. some = instante em que tudo vai embora"""
    fim = 1.0 if some is None else 1 - ep(t, some, 0.4)
    if fim <= 0:
        return
    p = ease_io(prog(t, t_in, 0.8))
    if ent is not None:
        if 0 < p < 1:
            bolinha(c, lerp(cx - w / 2 - dist, cx - w / 2 - 10, p), cy, ent, ENT, (1 - ep(t, t_in + 0.55, 0.25)) * fim, r)
        elif p <= 0 and t >= t_in - 0.6:
            bolinha(c, cx - w / 2 - dist, cy, ent, ENT, ep(t, t_in - 0.6, 0.4) * fim, r)
    if sai is not None:
        q = ease_out(prog(t, t_out, 0.8))
        if q > 0:
            bolinha(c, lerp(cx + w / 2, cx + w / 2 + dist, q), cy, sai, SAI, min(1, q * 3) * fim, r)


def fx(arg, resto="", cor_arg=None, cor_resto=TINTA):
    """partes de "f(arg)resto" com o argumento na cor da entrada"""
    out = [("f(", TINTA), (arg, cor_arg or ENT), (")", TINTA)]
    return out + ([(resto, cor_resto)] if resto else [])


FX = [("f(", TINTA), ("x", ENT), (") = 2", TINTA), ("x", ENT), (" + 3", TINTA)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: mista(c, FX, W / 2, 250, 130, a, "center"))
        for x0, k, partes, pede, cor in ((260, "s01.b", fx("5", " = ?"), "pede a saída", SAI),
                                         (1010, "s01.c", [("f(", TINTA), ("x", ENT), (") = 30", TINTA)], "pede a entrada", ENT)):
            p = ep(t, C[k], 0.5)
            if p > 0:
                M.rrect(c, x0, 380, 650, 380, 28, BR, 0.85 * p)
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, 380, 650, 380), 28, 28), M.paint(cor, p, stroke=4))
            E.foco(c, t, C[k], 0.5, lambda a, x0=x0, partes=partes: mista(c, partes, x0 + 325, 560, 120, a, "center"))
            E.foco(c, t, C["s01.d"] + (0 if k == "s01.b" else 0.8), 0.5,
                   lambda a, x0=x0, pede=pede, cor=cor: E.pilula(c, pede, x0 + 325, 680, 52, "g", fundo=cor, a=a))
        E.foco(c, t, C["s01.c"] + 0.4, 0.4, lambda a: centro(c, "x = ?", 1335, 450, 56, "b", ENT, a))
        E.foco(c, t, C["s01.e"], 0.4, lambda a: centro(c, "63", 1335, 900, 130, "g", ERRADO, a))
        if t >= C["s01.e"] + 0.5:
            E.risco(c, 1240, 920, 1430, 790, t, C["s01.e"] + 0.5, largura=14)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 1.2, [("as", "i", 110), ("duas", "g", 120, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 2.0, [("sem", "i", 110), ("trocar", "g", 120)], XE, 630)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "função:", "cada entrada, uma saída"), ("s03.c", "resolver equação:", "2x = 27 → x = 13,5"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 68)], x + 44, y + 96)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 190)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.b"], 0.4))


# ---------------- notação ----------------
FXN = [("f", TINTA), ("(", TINTA), ("x", ENT), (")", TINTA), (" = 2", TINTA), ("x", ENT), (" + 3", TINTA)]


def b_notacao(c, t, C, b):
    sobe = ease_io(prog(t, C["s05"] - 0.2, 0.8))
    y, size = lerp(430, 230, sobe), lerp(180, 120, sobe)
    E.foco(c, t, C["s04.a"], 0.6, lambda a: mista(c, FXN, W / 2, y, size, a, "center"))
    cs = mista(c, FXN, W / 2, y, size, 0, "center")

    def rotulos():
        (xf, wf), (xx, wx) = cs[0], cs[2]
        caixa_em(c, t, C["s04.b"], xf, wf, y, size, TINTA)
        E.frase(c, t, C["s04.b"] + 0.2, [("nome", "g", 56)], xf - 50, 600, "center")
        E.frase(c, t, C["s04.b"] + 1.4, ps("(da máquina)", "i", 46, TINTA2), xf - 50, 660, "center")
        caixa_em(c, t, C["s04.c"], xx, wx, y, size, ENT)
        E.frase(c, t, C["s04.c"] + 0.2, [("entrada", "g", 56, ENT)], xx + 60, 600, "center")
        x0 = cs[0][0] - cs[0][1] / 2
        x1 = cs[3][0] + cs[3][1] / 2
        p = ep(t, C["s04.d"], 0.6)
        if p > 0:
            E.chave(c, x0, x1, y - size * 0.95, SAI, p, -24, 6)
            E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: (centro(c, "saída", (x0 + x1) / 2, y - size * 0.95 - 110, 64, "g", SAI, a),
                                                            centro(c, "o que a máquina devolve", (x0 + x1) / 2 + 420, y - size * 0.95 - 112, 46, "i", TINTA2, a)))
    E.saida(c, t, C["s05"] - 0.3, rotulos)
    if t < C["s05"]:
        return

    def maq():
        E.foco(c, t, C["s05"], 0.5, lambda a: maquina(c, W / 2, 600, None, a, w=620, h=300))
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.pilula(c, "× 2", W / 2 - 110, 615, 72, "g", fundo=COR, a=a))
        E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "+ 3", W / 2 + 110, 615, 72, "g", fundo=COR, a=a))
        if t >= C["s05.b"]:
            p = ep(t, C["s05.b"], 0.4)
            M.arrow(c, W / 2 - 30, 615, W / 2 + 30, 615, CLARO, p, 5, 16, p)
    E.saida(c, t, C["s05.c"] - 0.1, maq)
    if t < C["s05.c"]:
        return
    E.foco(c, t, C["s05.c"], 0.5, lambda a: mista(c, [("f(", TINTA), ("x", ENT), (")", TINTA)], 640, 640, 150, a, "center"))
    E.foco(c, t, C["s05.c"] + 0.4, 0.5, lambda a: centro(c, "≠", W / 2, 630, 150, "g", ERRADO, a))
    E.foco(c, t, C["s05.c"] + 0.8, 0.5, lambda a: mista(c, [("f × ", TINTA2), ("x", ENT)], 1280, 640, 150, a, "center"))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "o parêntese mostra o que entra", W / 2, 850, 60, "g", fundo=ENT, a=a))


# ---------------- calcular ----------------
MX, MY = 1300, 470


def b_calcular(c, t, C, b):
    E.foco(c, t, C["s06"] - 0.3, 0.5, lambda a: maquina(c, MX, MY, "2x + 3", a, w=440, h=250, size=64))
    passa(c, t, MX, MY, "5", "13", C["s06.e"] - 0.4, C["s06.e"] + 0.5, w=440, some=C["s07"])
    passa(c, t, MX, MY, "−2", "−1", C["s07.d"] - 0.4, C["s07.d"] + 0.5, w=440)

    def s06():
        cs = mista_em(c, t, C["s06.a"], fx("5"), XE, 300, 130)
        caixa_em(c, t, C["s06.b"], cs[1][0], cs[1][1], 300, 130, ENT)
        E.frase(c, t, C["s06.b"] + 0.3, ps("dentro dos parênteses: entrada", "i", 50, ENT), XE, 400, passo=0.08)
        mista_em(c, t, C["s06.c"], [("2 · (", TINTA), ("5", ENT), (") + 3", TINTA)], XE, 540, 96)
        mista_em(c, t, C["s06.d"], [("10 + 3 = ", TINTA), ("13", SAI)], XE, 670, 96)
        E.foco(c, t, C["s06.e"], 0.5, lambda a: (M.rrect(c, XE - 20, 760, 560, 130, 65, COR, a),
                                                 mista(c, [("f(5) = 13", BR)], XE + 260, 852, 90, a, "center")))
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    mista_em(c, t, C["s07.a"], fx("−2"), XE, 300, 130)
    mista_em(c, t, C["s07.b"], [("2 · (", TINTA), ("−2", ENT), (") + 3", TINTA)], XE, 470, 96)
    mista_em(c, t, C["s07.c"], [("−4 + 3 = ", TINTA), ("−1", SAI)], XE, 610, 96)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: (M.rrect(c, XE - 20, 720, 600, 130, 65, COR, a),
                                             mista(c, [("f(−2) = −1", BR)], XE + 280, 812, 90, a, "center")))


# ---------------- caminho de volta ----------------
def b_volta(c, t, C, b):
    def maq():
        E.foco(c, t, C["s08"] - 0.3, 0.5, lambda a: maquina(c, MX, MY, "2x + 3", a, w=440, h=250, size=64))
        E.foco(c, t, C["s08.b"] + 0.4, 0.5, lambda a: bolinha(c, MX + 220 + 240, MY, "30", SAI, a, 58))
        if t < C["s09.b"]:
            E.foco(c, t, C["s08.c"], 0.5, lambda a: bolinha(c, MX - 220 - 240, MY, "?", ENT, a, 58))
        else:
            E.foco(c, t, C["s09.b"], 0.5, lambda a: bolinha(c, MX - 220 - 240, MY, "13,5", ENT, a, 58))
    E.saida(c, t, C["s10"] - 0.1, maq)

    def s08():
        cs = mista_em(c, t, C["s08.a"], [("f(", TINTA), ("x", ENT), (") = ", TINTA), ("30", SAI)], XE, 300, 130)
        caixa_em(c, t, C["s08.b"], cs[3][0], cs[3][1], 300, 130, SAI)
        E.frase(c, t, C["s08.b"] + 0.3, ps("depois do igual: saída", "i", 50), XE, 400, passo=0.08)
        E.frase(c, t, C["s08.c"], [("falta", "i", 64), ("a", "i", 64), ("entrada", "g", 62, ENT)], XE, 540)
        E.frase(c, t, C["s08.d"], [("uma", "i", 64), ("equação:", "g", 62)], XE, 680)
        mista_em(c, t, C["s08.d"] + 0.8, [("2", TINTA), ("x", ENT), (" + 3 = 30", TINTA)], XE, 820, 110)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"] + 0.3:
        def s09():
            mista_em(c, t, C["s09"], [("2", TINTA), ("x", ENT), (" + 3 = 30", TINTA)], XE, 260, 96)
            mista_em(c, t, C["s09.a"], [("2", TINTA), ("x", ENT), (" = 27", TINTA)], XE, 400, 96)
            E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "− 3", XE + 520, 368, 46, "g", fundo=TINTA2, a=a))
            mista_em(c, t, C["s09.b"], [("x", ENT), (" = ", TINTA), ("13,5", ENT)], XE, 540, 96)
            E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "÷ 2", XE + 520, 508, 46, "g", fundo=TINTA2, a=a))
            mista_em(c, t, C["s09.c"], [("2 · ", TINTA), ("13,5", ENT), (" = 27", TINTA)], XE, 680, 70)
            mista_em(c, t, C["s09.d"], [("27 + 3 = ", TINTA), ("30", SAI)], XE, 780, 70)
            E.foco(c, t, C["s09.d"] + 0.6, 0.4, lambda a: E.selo(c, XE + 560, 755, 36, True, a))
            E.foco(c, t, C["s09.e"], 0.5, lambda a: (M.rrect(c, XE - 20, 850, 620, 130, 65, COR, a),
                                                     mista(c, [("f(13,5) = 30", BR)], XE + 290, 942, 84, a, "center")))
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("quem", "i", 84), ("decide", "i", 84), ("é", "i", 84), ("o", "i", 84), ("lugar", "g", 80, COR), ("do", "i", 84),
                               ("número", "i", 84)], W / 2, 230, "center")
    cs = mista_em(c, t, C["s10.b"], fx("5"), 300, 470, 120)
    caixa_em(c, t, C["s10.b"] + 0.3, cs[1][0], cs[1][1], 470, 120, ENT)
    E.frase(c, t, C["s10.b"] + 0.6, [("dentro:", "i", 64), ("entrada", "g", 64, ENT), ("→", "g", 64, TINTA2), ("calcule", "g", 64)], 880, 450)
    cs = mista_em(c, t, C["s10.c"], [("f(", TINTA), ("x", ENT), (") = ", TINTA), ("30", SAI)], 300, 720, 120)
    caixa_em(c, t, C["s10.c"] + 0.3, cs[3][0], cs[3][1], 720, 120, SAI)
    E.frase(c, t, C["s10.c"] + 0.6, [("depois", "i", 58), ("do", "i", 58), ("igual:", "i", 58), ("saída", "g", 58), ("→", "g", 58, TINTA2),
                                     ("resolva", "g", 58)], 880, 700)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    cs = mista_em(c, t, C["s11"], [("f(", TINTA), ("x", ENT), (") = ", TINTA), ("30", SAI)], W / 2, 230, 120, "center")
    if t >= C["s11.a"]:  # o 30 pula para dentro do parêntese: o erro
        p = ease_io(prog(t, C["s11.a"] + 0.3, 0.9))
        x0, x1 = cs[3][0], cs[1][0]
        X = lerp(x0, x1, p)
        Y = 230 - 60 - 120 * (4 * p * (1 - p))
        if p < 1:
            centro(c, "30", X, Y + 30, 70, "g", ERRADO, ep(t, C["s11.a"], 0.3))
        else:
            centro(c, "30", x1, 120, 70, "g", ERRADO, 1)
            M.arrow(c, x1, 135, x1, 160, ERRADO, 1, 4, 12)
    mista_em(c, t, C["s11.b"], [("2 · (30) + 3 = 63", ERRADO)], W / 2, 450, 110, "center")
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "isso é f(30)", W / 2, 570, 56, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s11.d"], [("o", "i", 70), ("30", "g", 70), ("era", "i", 70), ("a", "i", 70), ("saída,", "g", 70), ("não", "i", 70), ("a", "i", 70),
                               ("entrada", "g", 70, ENT)], W / 2, 730, "center")
    E.frase(c, t, C["s11.e"], [("confira:", "i", 70, CERTO), ("f(resposta)", "g", 70), ("tem", "i", 70), ("que", "i", 70), ("dar", "i", 70),
                               ("30", "g", 70, CERTO)], W / 2, 900, "center")


# ---------------- atalho (palco escuro) ----------------
def caixinha(c, X, Y, s, a, cor):
    w = E.larg(s, "g", 64) + 60
    M.rrect(c, X - w / 2, Y - 50, w, 100, 24, cor, a)
    centro(c, s, X, Y + 23, 64, "g", BR, a)


def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 72, CLARO), W / 2, 150, "center")
        E.frase(c, t, C["s12.a"], [("desfaça", "g", 92, BR), ("de", "i", 92, CLARO), ("trás", "i", 92, CLARO), ("para", "i", 92, CLARO),
                                   ("a", "i", 92, CLARO), ("frente", "i", 92, CLARO)], W / 2, 290, "center")
        xs = (330, 700, 1030, 1360, 1680)
        yi, yv = 480, 780
        # ida
        a = ep(t, C["s12.b"], 0.5)
        if a > 0:
            bolinha(c, xs[0], yi, "x", COR, a, 58)
            caixinha(c, xs[1], yi, "× 2", a, COR)
            caixinha(c, xs[3], yi, "+ 3", a, COR)
            bolinha(c, xs[4], yi, "30", "#3C3C46", a, 58)
            bolinha(c, xs[2], yi, "2x", "#3C3C46", a, 58)
            for i in range(4):
                M.arrow(c, xs[i] + 75, yi, xs[i + 1] - 80, yi, CLARO, a, 5, 18)
            centro(c, "ida", 180, yi + 18, 48, "i", CLARO, a)
        # volta
        a = ep(t, C["s12.c"], 0.5)
        if a > 0:
            bolinha(c, xs[4], yv, "30", "#3C3C46", a, 58)
            caixinha(c, xs[3], yv, "− 3", a, "#E0A000")
            M.arrow(c, xs[4] - 75, yv, xs[3] - (-90), yv, CLARO, a, 5, 18)
            M.arrow(c, xs[3] - 90, yv, xs[2] + 75, yv, CLARO, a, 5, 18)
            bolinha(c, xs[2], yv, "27", "#3C3C46", a, 58)
            centro(c, "volta", 180, yv + 18, 48, "i", CLARO, a)
        a = ep(t, C["s12.d"], 0.5)
        if a > 0:
            caixinha(c, xs[1], yv, "÷ 2", a, "#E0A000")
            M.arrow(c, xs[2] - 75, yv, xs[1] + 80, yv, CLARO, a, 5, 18)
            M.arrow(c, xs[1] - 80, yv, xs[0] + 75, yv, CLARO, a, 5, 18)
            bolinha(c, xs[0], yv, "13,5", COR, a, 58)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("tirar", "i", 84, CLARO), ("o", "i", 84, CLARO), ("sapato", "g", 84, BR), ("antes", "i", 84, CLARO), ("da", "i", 84, CLARO),
                               ("meia", "g", 84, BR)], W / 2, 260, "center")
    E.frase(c, t, C["s13.a"] + 1.4, ps("o último a ser feito é o primeiro a ser desfeito", "i", 56, CLARO), W / 2, 370, "center", 0.08)
    E.frase(c, t, C["s13.b"], [("não", "g", 72, ERRADO), ("compensa:", "i", 72, CLARO), ("x", "g", 80, CLARO), ("em", "i", 72, CLARO), ("mais", "i", 72, CLARO),
                               ("de", "i", 72, CLARO), ("um", "i", 72, CLARO), ("lugar", "g", 72, BR)], W / 2, 620, "center")
    E.frase(c, t, C["s13.c"], [("aí,", "i", 72, CLARO), ("monte", "g", 72, BR), ("a", "i", 72, CLARO), ("equação", "g", 72, BR), ("e", "i", 72, CLARO),
                               ("resolva", "i", 72, CLARO), ("pela", "i", 72, CLARO), ("balança", "g", 72, BR)], W / 2, 820, "center")


# ---------------- questão ----------------
PD = [("P(", TINTA), ("d", ENT), (") = 5 + 2,5", TINTA), ("d", ENT)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 190)
    mista_em(c, t, C["s14.a"], PD, XE, 360, 120)
    E.frase(c, t, C["s14.a"] + 1.8, ps("o preço de uma corrida de d km", "i", 54, TINTA2), XE, 450, passo=0.08)
    mista_em(c, t, C["s14.b"], [("P(", TINTA), ("8", ENT), (") = ?", TINTA)], XE, 620, 100)
    mista_em(c, t, C["s14.c"], [("custou ", TINTA), ("R$ 40", SAI), (": ", TINTA), ("d", ENT), (" = ?", TINTA)], XE, 780, 90)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1500, cy=480, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x1, x2 = XE, 1040
    cs = mista_em(c, t, C["s16"], [("P(", TINTA), ("8", ENT), (")", TINTA)], x1, 260, 110)
    caixa_em(c, t, C["s16.a"], cs[1][0], cs[1][1], 260, 110, ENT)
    E.frase(c, t, C["s16.a"] + 0.2, [("entrada", "g", 56, ENT)], x1 + 280, 245)
    mista_em(c, t, C["s16.b"], [("2,5 · ", TINTA), ("8", ENT), (" = 20", TINTA)], x1, 430, 84)
    mista_em(c, t, C["s16.c"], [("5 + 20 = ", TINTA), ("25", SAI)], x1, 560, 84)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: (M.rrect(c, x1 - 20, 640, 520, 120, 60, COR, a),
                                             mista(c, [("P(8) = 25", BR)], x1 + 240, 724, 80, a, "center")))
    p = ep(t, C["s17"], 0.4)
    if p > 0:
        M.line(c, 960, 200, 960, 960, FIO, p, 3)
    cs = mista_em(c, t, C["s17"], [("P(", TINTA), ("d", ENT), (") = ", TINTA), ("40", SAI)], x2, 260, 110)
    caixa_em(c, t, C["s17.a"], cs[3][0], cs[3][1], 260, 110, SAI)
    E.frase(c, t, C["s17.a"] + 0.2, [("saída", "g", 56)], x2 + 520, 245)
    mista_em(c, t, C["s17.b"], [("40 − 5 = 35", TINTA)], x2, 400, 76)
    mista_em(c, t, C["s17.c"], [("35 ÷ 2,5", TINTA)], x2, 510, 76)
    mista_em(c, t, C["s17.c"] + 2.4, [("= 350 ÷ 25", TINTA2)], x2 + 330, 510, 64)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: (M.rrect(c, x2 - 20, 560, 480, 120, 60, COR, a),
                                             mista(c, [("d = 14 km", BR)], x2 + 220, 644, 80, a, "center")))
    mista_em(c, t, C["s17.e"], [("2,5 · ", TINTA), ("14", ENT), (" = 35", TINTA)], x2, 790, 64)
    mista_em(c, t, C["s17.e"] + 2.0, [("35 + 5 = ", TINTA), ("40", SAI)], x2, 880, 64)
    E.foco(c, t, C["s17.e"] + 2.6, 0.4, lambda a: E.selo(c, x2 + 420, 858, 34, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s18.a", [("número", "i", 80), ("nos", "i", 80), ("parênteses:", "i", 80), ("calcule", "g", 80, ENT)]),
                 ("s18.b", [("número", "i", 80), ("depois", "i", 80), ("do", "i", 80), ("igual:", "i", 80), ("resolva", "g", 80)]),
                 ("s18.c", [("confira", "g", 80, CERTO), ("devolvendo", "i", 80), ("à", "i", 80), ("função", "i", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s19.a"], ps("o que entra e o que sai", "i", 70, TINTA2), XE, 410)
    E.frase(c, t, C["s19.b"], [("domínio,", "g", 104, COR)], XE, 540)
    E.frase(c, t, C["s19.b"] + 0.5, [("contradomínio", "g", 104, COR)], XE, 650)
    E.frase(c, t, C["s19.b"] + 1.0, [("e", "i", 100), ("imagem", "g", 104, COR)], XE, 760)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, notacao=b_notacao, calcular=b_calcular, volta=b_volta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
