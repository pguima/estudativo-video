"""Visual — Estudativo · MAT-POT-004: potência de potência e de um produto.
Identidade em _ferramentas/editorial.py. Peças desta aula: turnos em blocos de horas, tabela de fatoração do kit em uma coluna
e os pares de 2 e 5 no palco. Expoente sempre com E.formula."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, sinal, palco, centro, montar, tabela, seta_primo
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-004_potencia_de_potencia_e_de_produto.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("potpot", "fatorar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
T64 = montar((64,), (2, 2, 2, 2, 2, 2))
T216 = montar((216,), (2, 2, 2, 3, 3, 3))
G = dict(xs=(330,), xb=490, xp=590, y0=190, dy=118, s=92)
assert (2 ** 3) ** 4 == 2 ** 12 == 8 ** 4 == 4096 and 2 ** 7 == 128 and (2 * 5) ** 3 == 1000 == 8 * 125 and 2 ** 6 == 64
assert 2 ** 3 * 3 ** 2 * 5 == 360 and 8 * 9 == 72 and 72 * 5 == 360 and (2 + 3) ** 2 == 25 and 2 ** 2 + 3 ** 2 == 13
assert 2 ** 4 * 5 ** 3 == 2000 == 16 * 125 and 2 ** 3 * 3 ** 3 == 216 == 6 ** 3


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
    """número ou fórmula dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    E.formula(c, s, cx, cy + size * 0.36, size, cor=tinta or E.SOBRE, a=a, align="center")


def fm(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, cor=cor, align=align)


def fl(c, t, partes, x, y, size, align="left", gap=None):
    """linha de fórmulas em que cada parte entra no seu instante: partes = [(escrita, cor, t0), ...]; devolve o x e a largura de cada uma"""
    gap = size * 0.2 if gap is None else gap
    ws = [E.formula(None, p[0], 0, 0, size, a=0) for p in partes]
    tot = sum(ws) + gap * (len(ws) - 1)
    xx = x - tot / 2 if align == "center" else x
    xs = []
    for p, w in zip(partes, ws):
        fm(c, t, p[2], p[0], xx, y, size, p[1])
        xs.append(xx)
        xx += w + gap
    return xs, ws


def turno(c, t, ti, x, y, w, h, cor=None):
    """um turno: caixa com três horas dobrando dentro"""
    def fn(a):
        M.rrect(c, x, y, w, h, 16, E.VAZIO, a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16), M.paint(cor or E.COR, a, stroke=4))
        for i in range(3):
            num_bola(c, "×2", x + w * (i + 0.5) / 3, y + h / 2, 48, 40, a)
    E.foco(c, t, ti, 0.45, fn)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s01.{k}"] for k in "abcd")

    def conta():
        y = 460
        fm(c, t, a_, "(2^3)^4", 230, y, 240)
        sinal(c, t, lerp(b_, c_, 0.55), "=", 960, y - 80, 170)
        E.foco(c, t, lerp(b_, c_, 0.6), 0.5, lambda q: E.formula(c, "2^7", 1110, y, 240, cor=ERRADO, a=q))
        if t >= c_:
            E.risco(c, 1090, y + 30, 1430, y - 200, t, c_, largura=18)
        E.frase(c, t, c_, ps("errou", "g", 100, ERRADO), 1110, y + 150)
        E.foco(c, t, d_, 0.5, lambda q: num_bola(c, "2^{12}", 1520, 790, 170, 140, q, CERTO, BR))
        E.frase(c, t, b_, ps("somou os expoentes?", "i", 84), XE, 700, passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, conta)

    if t >= C["s02"]:
        a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
        E.frase(c, t, a2, ps("até o fim desta aula", "i", 92), XE, 240)
        E.frase(c, t, lerp(a2, b2, 0.4), ps("quando", "i", 92) + ps("somar", "g", 92, COR), XE, 380)
        E.frase(c, t, lerp(a2, b2, 0.65), ps("quando", "i", 92) + ps("multiplicar expoentes", "g", 84, COR), XE, 500)
        fm(c, t, b2, "360 = 2^3 · 3^2 · 5", XE, 690, 120, COR)
        E.frase(c, t, b2 + 0.9, ps("números grandes como", "i", 72) + ps("potências de primos", "g", 66, COR), XE, 800, passo=0.14)
        E.foco(c, t, c2 - 0.1, 0.6, lambda a: E.bola(c, 1560, 300, 190 * ease_back(prog(t, c2 - 0.1, 0.6))), blur=0)
        E.foco(c, t, c2 + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1560, 295, 70, "g", E.SOBRE, a), centro(c, "de prova", 1560, 370, 70, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.1, ps("lembre de", "i", 96), XE, 410)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, p))
    x, w = 830, 920
    for i, (k, l1, l2) in enumerate(((b_, "multiplicando potências de mesma base,", "soma os expoentes"), (c_, "fatorar é escrever como", "multiplicação só de primos"))):
        y = 240 + i * 290
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 58)], x + 44, y + 96)
        E.frase(c, t, k + 0.3, [(l2, "g", 60, COR)], x + 44, y + 186)
    E.frase(c, t, lerp(c_, C["s03.end"], 0.6), ps("faltou alguma?", "i", 66, COR) + ps("procure no canal", "i", 66), W / 2, 960, "center", 0.15)


# ---------------- potência de potência ----------------
def b_potpot(c, t, C, b):
    def s04():
        a, b_, c_, d = (C[f"s04.{k}"] for k in "abcd")
        E.frase(c, t, C["s04"] + 0.1, ps("uma colônia de bactérias", "i", 84), XE, 170, passo=0.13)
        E.frase(c, t, a, ps("dobra", "g", 80, COR) + ps("a cada hora", "i", 84), XE, 280)
        x0, w, gap, y, h = 190, 365, 30, 370, 170
        turno(c, t, b_, x0, y, w, h)
        fm(c, t, lerp(b_, c_, 0.55), "× 2^3", x0 + w / 2, y + h + 110, 96, COR, "center")
        for i in (1, 2, 3):
            turno(c, t, c_ + (i - 1) * 0.2, x0 + i * (w + gap), y, w, h)
            fm(c, t, c_ + (i - 1) * 0.2, "× 2^3", x0 + i * (w + gap) + w / 2, y + h + 110, 96, COR, "center")
        E.frase(c, t, lerp(b_, c_, 0.2), ps("um turno:", "i", 72) + ps("3 horas", "g", 68, COR), XE, 790, passo=0.14)
        E.frase(c, t, c_ + 0.1, ps("4 turnos", "g", 72, COR), 940, 790)
        fm(c, t, d, "(2^3)^4", W / 2, 985, 150, align="center")
    E.saida(c, t, C["s05"] - 0.1, s04)

    if C["s05"] <= t < C["s06"] + 0.4:
        a, b_, c_, d, e = (C[f"s05.{k}"] for k in "abcde")

        def s05():
            E.frase(c, t, C["s05"] + 0.1, ps("quantas horas?", "i", 84), XE, 200)
            fm(c, t, a, "4 × 3 = 12", 780, 205, 110, COR)
            x0, w, gap, y, h = 190, 365, 30, 330, 190
            for i in range(4):
                x = x0 + i * (w + gap)

                def caixa(q, x=x):
                    M.rrect(c, x, y, w, h, 16, E.VAZIO, q)
                    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16), M.paint(E.COR, q, stroke=4))
                E.foco(c, t, b_ + i * 0.2, 0.45, caixa)
                if t < c_ + 0.3:
                    E.saida(c, t, c_, lambda x=x, i=i: fm(c, t, b_ + i * 0.2, "2^3", x + w / 2, y + 128, 120, COR, "center"), d=0.3)
                fm(c, t, c_ + i * 0.15, "2 × 2 × 2", x + w / 2, y + 120, 66, COR, "center")
            q = ep(t, d, 0.45)
            E.chave(c, x0, x0 + 4 * w + 3 * gap, y + h + 18, COR, q, 24, 6, abre=False)
            E.frase(c, t, d, ps("4 blocos de 3", "g", 92, COR), W / 2, 720, "center")
            fl(c, t, [("(2^3)^4", None, e - 0.2), ("=", None, e - 0.1)], 620, 930, 140)
            E.foco(c, t, e, 0.5, lambda p: num_bola(c, "2^{12}", 1230, 880, 130, 110, p, CERTO, BR))
        E.saida(c, t, C["s06"] - 0.1, s05)

    if t >= C["s06"]:
        a, b_, c_, d = (C[f"s06.{k}"] for k in "abcd")
        E.frase(c, t, a, ps("potência de potência:", "i", 88), W / 2, 180, "center", 0.15)
        E.frase(c, t, b_, ps("repete a base", "g", 96, COR) + ps("e", "i", 96) + ps("multiplica os expoentes", "g", 80, COR), W / 2, 310, "center", 0.17)
        M.line(c, XE, 390, W - XE, 390, FIO, ep(t, lerp(b_, c_, 0.8), 0.5), 3)
        y1, y2 = 540, 830
        fm(c, t, c_, "2^3 · 2^4 = 2^7", XE, y1, 130)
        E.frase(c, t, c_ + 0.7, ps("um vezes entre as potências", "i", 60, TINTA2), XE, y1 + 86, passo=0.11)
        E.foco(c, t, c_ + 1.6, 0.45, lambda q: E.pilula(c, "soma", 1230, y1 - 40, 84, estilo="g", a=q, cor=E.SOBRE))
        fm(c, t, d, "(2^3)^4 = 2^{12}", XE, y2, 130)
        E.frase(c, t, d + 0.7, ps("um expoente dentro, outro fora", "i", 60, TINTA2), XE, y2 + 90, passo=0.11)
        E.foco(c, t, d + 1.6, 0.45, lambda q: E.pilula(c, "multiplica", 1320, y2 - 40, 84, estilo="g", a=q, cor=E.SOBRE))


# ---------------- potência de um produto ----------------
def b_produto(c, t, C, b):
    a, b_, c_ = (C[f"s07.{k}"] for k in "abc")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def tela():
        E.frase(c, t, C["s07"] + 0.1, ps("e quando a base é uma multiplicação?", "i", 72), XE, 130, passo=0.12)
        y = 300
        fm(c, t, a, "(2 · 5)^3", XE, y, 140)
        fm(c, t, b_, "= 10^3", 790, y, 130)
        E.frase(c, t, b_ + 0.1, ps("primeiro o parêntese", "i", 58, TINTA2), 790, y + 76, passo=0.11)
        fm(c, t, c_, "= 1.000", 1240, y, 130, COR)
        M.line(c, XE, 410, W - XE, 410, FIO, ep(t, a8 - 0.5, 0.5), 3)
        fm(c, t, a8, "(2 · 5) · (2 · 5) · (2 · 5)", XE, 530, 104)
        E.frase(c, t, b8 - 0.2, ps("junte quem é igual", "g", 62, COR), 1200, 510, passo=0.12)
        fm(c, t, b8 + 0.2, "2 · 2 · 2 · 5 · 5 · 5", XE, 680, 104)
        fm(c, t, c8, "= 2^3 · 5^3", 1080, 680, 110, COR)
        fl(c, t, [("8 × 125", None, d8), ("=", None, d8 + 0.5)], XE, 880, 130)
        E.foco(c, t, d8 + 0.7, 0.5, lambda q: num_bola(c, "1.000", 1050, 835, 130, 76, q, CERTO, BR))
        E.frase(c, t, d8 + 0.9, ps("mil de novo", "i", 80), 1230, 860)
    E.saida(c, t, C["s09"] - 0.1, tela)

    if t >= C["s09"]:
        a, b_, c_ = (C[f"s09.{k}"] for k in "abc")
        E.frase(c, t, a, ps("o expoente de fora vai para", "i", 80) + ps("cada número", "g", 74, COR), W / 2, 200, "center", 0.14)
        fm(c, t, a + 1.2, "(2 · 5)^3 = 2^3 · 5^3", W / 2, 350, 130, align="center")
        E.frase(c, t, b_ - 0.5, ps("e ao contrário:", "i", 80, COR), W / 2, 500, "center")
        E.frase(c, t, b_, ps("expoentes iguais,", "i", 84) + ps("junte as bases", "g", 80, COR), W / 2, 610, "center", 0.15)
        fm(c, t, b_ + 1.2, "2^3 · 5^3 = 10^3", W / 2, 760, 130, align="center")
        E.frase(c, t, lerp(b_, c_, 0.55), ps("base diferente não soma expoente:", "i", 72), XE, 930, passo=0.12)
        E.frase(c, t, c_, ps("ele fica como está", "g", 70, COR), 1110, 930, passo=0.13)


# ---------------- fatoração com potências ----------------
def rampa(ks, ini, dt=0.25):
    """instantes da tabela a partir das cues: números, primos e traço; ks = instante de cada número novo"""
    tn = [[ini]] + [[k] for k in ks]
    tp = [k - dt for k in ks]
    tb = [ini] + list(ks)
    return tn, tp, tb


def b_fatorar(c, t, C, b):
    def s10():
        a, b_ = C["s10.a"], C["s10.b"]
        ks = [C[f"s10.{k}"] for k in "cdefgh"]
        i_, j = C["s10.i"], C["s10.j"]
        E.frase(c, t, a, ps("potência", "i", 84) + ps("encurta a fatoração", "g", 78, COR), 800, 190, passo=0.15)
        tn, tp, tb = rampa(ks, b_)
        tabela(c, t, T64, tn, tp, tb, G, cor_fim=CERTO if t >= ks[5] + 0.4 else None)
        for k in range(6):
            seta_primo(c, t, tp[k], tp[k + 1] if k < 5 else i_, k, G)
        E.frase(c, t, lerp(b_, ks[0], 0.3), ps("divisões sucessivas pelo menor primo", "i", 64), 800, 300, passo=0.1)
        q = ep(t, i_, 0.5)
        E.caixa_pontilhada(c, G["xp"] - 66, G["y0"] - G["s"] * 0.95, 132, G["dy"] * 5 + G["s"] * 1.2, q, COR, prog_=q)
        E.frase(c, t, i_, ps("6 divisões por 2", "g", 92, COR), 800, 560)
        E.foco(c, t, j, 0.5, lambda p: E.formula(c, "64 = 2^6", 800, 800, 190, cor=CERTO, a=p))
    E.saida(c, t, C["s11"] - 0.1, s10)

    if t >= C["s11"]:
        a, b_, c_, d, e, f = (C[f"s11.{k}"] for k in "abcdef")
        E.frase(c, t, C["s11"] + 0.1, ps("com primos diferentes,", "i", 80) + ps("junte os iguais", "g", 74, COR), XE, 190, passo=0.14)
        y, s = 400, 110
        xn, wn = fl(c, t, [("360", None, a), ("=", None, b_ - 0.05)], XE, y, s)
        x = xn[-1] + wn[-1] + 34
        tb = [lerp(b_, c_, 0.8 * i / 6) for i in range(6)]
        partes = []
        for i, ch in enumerate("222335"):
            if i:
                partes.append(("·", None, tb[i] - 0.03))
            partes.append((ch, None, tb[i]))
        xs, ws = fl(c, t, partes, x, y, s, gap=22)
        grupos = ((0, 4, c_, COR, "o 2 aparece 3 vezes", "2^3"), (6, 8, d, TINTA, "o 3, 2 vezes", "3^2"), (10, 10, e, CERTO, "o 5, 1 vez", "5"))
        for i0, i1, k, cor, txt, fr_ in grupos:
            x0, x1 = xs[i0], xs[i1] + ws[i1]
            E.chave(c, x0 - 4, x1 + 4, y + 34, cor, ep(t, k, 0.45), 24, 5, abre=False)
            fm(c, t, k + 0.2, fr_, (x0 + x1) / 2, y + 170, 110, cor, "center")
        E.frase(c, t, e + 0.4, ps("o expoente 1 não se escreve", "i", 62), XE, 720, passo=0.11)
        E.foco(c, t, f, 0.5, lambda p: E.formula(c, "360 = 2^3 · 3^2 · 5", W / 2, 910, 140, cor=CERTO, a=p, align="center"))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_ = (C[f"s12.{k}"] for k in "abc")
    a3, b3, c3 = (C[f"s13.{k}"] for k in "abc")
    E.frase(c, t, a, ps("o erro comum:", "i", 80, ERRADO) + ps("levar o expoente para dentro", "g", 62, ERRADO), XE, 170, passo=0.14)
    y1 = 390
    fm(c, t, b_, "(2 + 3)^2", XE, y1, 150)
    fm(c, t, c_, "= 2^2 + 3^2", 800, y1, 110, ERRADO)
    fm(c, t, c_ + 1.2, "4 + 9 = 13", 800, y1 + 120, 100, ERRADO)
    if t >= a3 - 0.2:
        E.risco(c, 790, y1 + 134, 1390, y1 - 90, t, a3 - 0.2, largura=12)
    M.line(c, XE, 590, W - XE, 590, FIO, ep(t, a3 - 0.3, 0.5), 3)
    E.frase(c, t, C["s13"] + 0.1, ps("o parêntese vem primeiro", "i", 72), XE, 690, passo=0.13)
    y2 = 830
    fm(c, t, a3, "2 + 3 = 5", XE, y2, 120, COR)
    fm(c, t, b3 - 0.1, "5^2 =", 800, y2, 120, COR)
    E.foco(c, t, b3 + 0.1, 0.5, lambda q: num_bola(c, "25", 1150, y2 - 42, 100, 88, q, CERTO, BR))
    E.frase(c, t, c3, ps("multiplicação,", "g", 80, COR) + ps("nunca soma", "g", 80, ERRADO), W / 2, 990, "center", 0.15)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def tela():
        a, b_, c_, d, e = (C[f"s14.{k}"] for k in "abcde")
        a5, b5 = C["s15.a"], C["s15.b"]
        E.frase(c, t, C["s14"] + 0.1, ps("agora, o atalho", "i", 72, CLARO), W / 2, 110, "center")
        E.frase(c, t, a, ps("procure pares de", "i", 88, CLARO) + ps("2 e 5", "g", 84, BR), W / 2, 215, "center", 0.15)
        fl(c, t, [("2 × 5 = 10", BR, b_)], XE, 370, 96)
        E.frase(c, t, b_ + 0.7, ps("vezes 10:", "i", 66, CLARO) + ps("só acrescentar zero", "g", 60, BR), 780, 355, passo=0.13)
        fm(c, t, c_, "2^4 · 5^3", XE, 620, 140, BR)
        x0, dx, y1, y2, r = 870, 200, 520, 720, 66
        for i in range(4):
            x = x0 + i * dx
            cor = CERTO if i == 3 and t >= e else E.COR
            E.foco(c, t, c_ + 0.2 + i * 0.1, 0.4, lambda q, x=x, cor=cor: num_bola(c, "2", x, y1, r, 72, q, cor, BR))
        for i in range(3):
            x = x0 + i * dx
            E.foco(c, t, c_ + 0.7 + i * 0.1, 0.4, lambda q, x=x: num_bola(c, "5", x, y2, r, 72, q, TINTA2, BR))
            q = ep(t, d + i * 0.15, 0.4)
            if q > 0:
                M.line(c, x, y1 + r + 4, x, y2 - r - 4, CLARO, q, 7)
                centro(c, "10", x + 62, (y1 + y2) / 2 + 16, 44, "g", BR, q)
        E.frase(c, t, d + 0.5, ps("3 pares", "g", 76, BR), XE, 760)
        E.frase(c, t, e, ps("sobra um 2", "g", 66, CERTO), x0 + 3 * dx - 120, y2 + 16)
        fl(c, t, [("10^3 = 1.000", BR, a5)], XE, 930, 104)
        fl(c, t, [("1.000 × 2 =", BR, b5)], 840, 930, 100)
        E.foco(c, t, b5 + 0.3, 0.5, lambda q: num_bola(c, "2.000", 1600, 890, 120, 68, q, CERTO, BR))
    E.saida(c, t, lerp(C["s15.b"], C["s15.end"], 0.45), tela)

    te = lerp(C["s15.b"], C["s15.end"], 0.45)
    if te <= t < C["s16"] + 0.4:
        def sem():
            E.frase(c, t, te + 0.2, ps("sem o atalho", "i", 110, CLARO), W / 2, 420, "center")
            fm(c, t, te + 0.5, "16 × 125", W / 2, 640, 190, BR, "center")
        E.saida(c, t, C["s16"] - 0.1, sem)

    if t >= C["s16"]:
        a, b_, c_ = (C[f"s16.{k}"] for k in "abc")
        E.frase(c, t, a - 0.2, ps("funciona porque", "i", 84, CLARO), W / 2, 210, "center")
        E.frase(c, t, a, ps("a ordem da multiplicação", "g", 84, BR), W / 2, 330, "center", 0.14)
        E.frase(c, t, a + 1.0, ps("não muda o resultado", "i", 84, CLARO), W / 2, 440, "center", 0.14)
        E.frase(c, t, b_, ps("não compensa", "g", 84, ERRADO) + ps("quando falta o 2 ou o 5", "i", 84, CLARO), W / 2, 620, "center", 0.14)
        fm(c, t, c_, "3^2 · 7^2", 430, 860, 150, BR)
        E.frase(c, t, c_ + 0.9, ps("nenhum dez", "g", 100, ERRADO), 1040, 830)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_ = C["s17.a"], C["s17.b"]
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 76, COR), XE, 200)
    E.frase(c, t, a, ps("fatore", "i", 110) + ps("216", "g", 130, COR), XE, 410)
    E.frase(c, t, a + 0.7, ps("usando potências", "i", 84), XE, 530)
    E.frase(c, t, b_, ps("escreva o resultado", "i", 84), XE, 720, passo=0.14)
    E.frase(c, t, b_ + 0.8, ps("como", "i", 92) + ps("uma potência só", "g", 88, COR), XE, 840)
    E.relogio(c, t, C["s18.a"], 1520, 400, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ks = [C[f"s19.{k}"] for k in "abc"] + [C[f"s19.{k}"] for k in "efg"]
    d, h = C["s19.d"], C["s19.h"]
    a2, b2, c2 = (C[f"s20.{k}"] for k in "abc")
    tn, tp, tb = rampa(ks, C["s19"] + 0.1)
    tabela(c, t, T216, tn, tp, tb, G, cor_fim=CERTO if t >= ks[5] + 0.4 else None)
    for k in range(6):
        seta_primo(c, t, tp[k], tp[k + 1] if k < 5 else h, k, G)
    X = 800
    q = ep(t, d, 0.45)
    E.caixa_pontilhada(c, G["xp"] - 66, G["y0"] - G["s"] * 0.95, 132, G["dy"] * 2 + G["s"] * 1.2, q, COR, prog_=q)
    q = ep(t, h, 0.45)
    E.caixa_pontilhada(c, G["xp"] - 66, G["y0"] + G["dy"] * 3 - G["s"] * 0.95, 132, G["dy"] * 2 + G["s"] * 1.2, q, COR, prog_=q)
    fl(c, t, [("216 =", None, d - 0.1), ("2^3", COR, d), ("·", None, h - 0.1), ("3^3", COR, h)], X, 300, 130)
    E.frase(c, t, C["s20"] + 0.1, ps("expoentes iguais,", "i", 72) + ps("junte as bases", "g", 68, COR), X, 460, passo=0.14)
    fm(c, t, a2, "= (2 · 3)^3", X, 610, 130)
    E.foco(c, t, b2, 0.5, lambda p: num_bola(c, "6^3", 1570, 620, 120, 112, p, CERTO, BR))
    fm(c, t, c2, "6 × 6 × 6 = 216", X, 830, 110, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a, b_, c_ = (C[f"s21.{k}"] for k in "abc")

    def resumo():
        E.frase(c, t, C["s21"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 170, "center")
        for k, y, s1, f1 in ((a, 370, "vezes entre potências: soma", "2^3 · 2^4 = 2^7"), (b_, 610, "dentro e fora: multiplica", "(2^3)^4 = 2^{12}"), (c_, 850, "vai para cada número", "(2 · 5)^3 = 2^3 · 5^3")):
            E.frase(c, t, k, ps(s1, "g", 58, COR), XE, y - 80, passo=0.1)
            fm(c, t, k + 0.5, f1, XE, y + 40, 110)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 220)
    E.frase(c, t, a2, ps("o expoente", "i", 110) + ps("fica negativo", "g", 104, COR), XE, 370)
    fl(c, t, [("10^{−3}", COR, b2), ("=", None, b2 + 0.8), ("0,001", COR, b2 + 0.9)], XE, 570, 130)
    E.frase(c, t, b2 + 1.3, ps("contando as casas", "i", 72), XE, 680, passo=0.14)
    E.foco(c, t, c2, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1450, 560, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1590, p), lerp(800, 600, p), ep(t, c2 + 0.2, 0.4), TINTA)
    E.frase(c, t, d2, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, potpot=b_potpot, produto=b_produto, fatorar=b_fatorar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
