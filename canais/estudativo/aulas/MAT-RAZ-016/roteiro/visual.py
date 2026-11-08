"""Visual — Estudativo · MAT-RAZ-016: converter km/h em m/s.
Peças locais: estrada() e carro() (a mesma pista escura da MAT-RAZ-015); caixas() desenha as duas unidades lado a lado com
a seta de ida (÷ 3,6) e a de volta (× 3,6); placa() é a placa de limite de velocidade. Índigo = o que está sendo calculado,
vermelho = erro, verde = conferido. Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f)."""
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-016_converter_km_h_em_m_s.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("unidades", "deducao", "fator", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ASFALTO = "#26262B"
# as contas da aula, conferidas
assert 72000 / 3600 == 20 and 720 / 36 == 20 and 60 * 60 == 3600 and D(3600) / 1000 == D("3.6") and D(72) / D("3.6") == 20
assert D(54) / D("3.6") == 15 and 540 / 36 == 15 and 15 * 3 == 45 and 15 * D("0.6") == 9 and 45 + 9 == 54
assert D(72) * D("3.6") == D("259.2") and [D(n) / D("3.6") for n in (36, 72, 108)] == [10, 20, 30]
assert 90 == 72 + 18 and D(18) / D("3.6") == 5 and 20 + 5 == 25 and D(90) / D("3.6") == 25
assert str(D(100) / D("3.6"))[:5] == "27.77" and 30 * D("3.6") == 108 and 108 > 90 and 30 > 25


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


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=130, size=70, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def carro(c, cx, base, a, cor=None):
    """carro de lado, com a base em (cx, base)"""
    if a <= 0:
        return
    cor = cor or E.COR
    M.rrect(c, cx - 50, base - 92, 110, 50, 18, cor, a)
    M.rrect(c, cx - 36, base - 82, 38, 28, 6, BR, 0.9 * a)
    M.rrect(c, cx + 10, base - 82, 38, 28, 6, BR, 0.9 * a)
    M.rrect(c, cx - 100, base - 58, 200, 46, 18, cor, a)
    for dx in (-58, 58):
        c.drawCircle(cx + dx, base - 12, 17, M.paint(TINTA, a))
        c.drawCircle(cx + dx, base - 12, 6, M.paint(BR, a))


def estrada(c, x0, x1, y, a, pos=None):
    """pista escura de x0 a x1 (y = meio); pos = 0..1 põe o carro em cima"""
    if a <= 0:
        return
    M.rrect(c, x0, y - 30, x1 - x0, 60, 30, ASFALTO, a)
    xx = x0 + 40
    while xx < x1 - 60:
        M.line(c, xx, y, xx + 34, y, BR, 0.75 * a, 4)
        xx += 70
    if pos is not None:
        carro(c, lerp(x0 + 110, x1 - 110, M.clamp(pos)), y - 26, a)


def caixa_unid(c, cx, cy, s, a, cor=None, escuro=False):
    """caixa com a unidade (km/h ou m/s)"""
    if a <= 0:
        return
    w, h = 360, 170
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 26, cor or (BR if not escuro else "#FFFFFF"), a * (1 if not escuro else 0.08))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26), M.paint(BR if escuro else TINTA, a, stroke=4))
    centro(c, s, cx, cy + 34, 96, "g", (BR if escuro else TINTA) if cor is None else M.on(cor), a)


def caixas(c, t, t0, ti, tv, y, xa=520, xb=1400, escuro=False):
    """km/h à esquerda, m/s à direita; ti = seta de ida (÷ 3,6), tv = seta de volta (× 3,6)"""
    E.foco(c, t, t0, 0.5, lambda a: caixa_unid(c, xa, y, "km/h", a, escuro=escuro))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: caixa_unid(c, xb, y, "m/s", a, escuro=escuro))
    if ti is not None:
        E.ponte(c, t, ti, xa + 200, xb - 200, y - 50, "÷ 3,6", None, 48)
    if tv is not None:
        E.ponte(c, t, tv, xb - 200, xa + 200, y + 50, "× 3,6", TINTA if not escuro else E.mix(E.COR, BR, 0.3), 48)


def placa(c, cx, cy, r, s, a, cor=None):
    """placa redonda de limite de velocidade"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR, a))
    c.drawCircle(cx, cy, r * 0.86, M.paint(ERRADO, a, stroke=r * 0.16))
    centro(c, s, cx, cy + r * 0.24, r * 0.7, "g", cor or TINTA, a)


# ---------------- gancho ----------------
X0, X1 = 260, 1660


def b_gancho(c, t, C, b):
    a1, b1, c1, e1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.end"]

    def cena():
        fcen(c, t, a1, "72 km/h", W / 2, 230, 140, COR)
        E.foco(c, t, C["s01"], 0.5, lambda a: estrada(c, X0, X1, 540, a, ease_io(prog(t, a1, max(1.0, e1 - a1)))))
        E.frase(c, t, b1, ps("quantos metros em", "i", 80) + [("1 segundo?", "g", 84, COR)], W / 2, 720, "center", 0.12)
        if t >= c1:
            E.chave(c, 860, 1060, 430, COR, ep(t, c1, 0.5), -22)
        E.foco(c, t, c1 + 0.2, 0.5, lambda a: centro(c, "20 m", 960, 386, 64, "g", COR, a))
        E.frase(c, t, c1, [("= 20 m/s", "g", 100, COR)], W / 2, 880, "center")
        E.frase(c, t, lerp(c1, e1, 0.45), ps("com uma conta só", "i", 66, TINTA2), W / 2, 990, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), [("converter", "g", 120, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("km/h", "g", 100), ("e", "i", 90), ("m/s", "g", 100)], XE, 600, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("sem errar a", "i", 84) + [("direção", "g", 88, COR)], XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "ler uma taxa:", "“por” = dividido"), ("s03.c", "a escada do metro:", "1 km = 1.000 m"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 690, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56, TINTA2), x, 900, "left", 0.1)


# ---------------- as duas unidades ----------------
def b_unidades(c, t, C, b):
    a4, b4, c4, d4, e4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.end"]
    fcen(c, t, a4, "m/s", 560, 330, 170, COR)
    E.frase(c, t, b4 - 0.6, ps("metros em", "i", 64) + [("cada segundo", "g", 64, COR)], 560, 450, "center", 0.1)
    E.frase(c, t, lerp(b4, c4, 0.55), ps("aparece na física", "i", 54, TINTA2), 560, 540, "center", 0.08)
    fcen(c, t, c4, "km/h", 1360, 330, 170)
    E.frase(c, t, c4 + 0.6, ps("o do", "i", 64) + [("velocímetro", "g", 64)], 1360, 450, "center", 0.1)
    E.frase(c, t, d4, ps("as", "i", 72) + [("duas", "g", 76, COR)] + ps("unidades mudam juntas", "i", 72), W / 2, 710, "center", 0.1)
    E.foco(c, t, lerp(d4, e4, 0.45), 0.5, lambda a: E.pilula(c, "km → m", 700, 870, 66, "g", a=a))
    E.foco(c, t, lerp(d4, e4, 0.7), 0.5, lambda a: E.pilula(c, "h → s", 1220, 870, 66, "g", a=a))


# ---------------- na raça ----------------
def b_deducao(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]

    def raca():
        E.frase(c, t, C["s05"] + 0.2, ps("primeiro,", "i", 72) + [("sem atalho", "g", 76, COR)], W / 2, 170, "center", 0.12)
        fcen(c, t, a5, "72 km = 72.000 m", W / 2, 360, 104)
        fcen(c, t, b5, "1 h = 60 min", W / 2, 530, 96)
        fcen(c, t, lerp(b5, c5, 0.5), "1 min = 60 s", W / 2, 670, 96)
        fcen(c, t, c5, "1 h = 60 × 60 = 3.600 s", W / 2, 860, 104, COR)
    E.saida(c, t, C["s06"] - 0.1, raca)
    if t < C["s06"]:
        return
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    fcen(c, t, a6, "72.000 m em 3.600 s", W / 2, 230, 96)
    E.frase(c, t, b6 - 0.5, ps("por segundo:", "i", 66, TINTA2), W / 2, 360, "center", 0.1)
    fcen(c, t, b6, "f{72.000}{3.600}", 520, 560, 130)
    if t >= c6 - 0.6:
        E.foco(c, t, c6 - 0.6, 0.5, lambda a: E.pilula(c, "corte 2 zeros em cada um", W / 2, 860, 56, "g", a=a))
    fcen(c, t, c6, "= f{720}{36}", 960, 560, 130)
    fcen(c, t, d6, "= 20 m/s", 1440, 600, 120, COR)
    E.foco(c, t, d6 + 1.0, 0.5, lambda a: E.selo(c, 1440, 720, 44, True, a))


# ---------------- o fator 3,6 ----------------
def b_fator(c, t, C, b):
    a7, b7, c7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.end"]

    def junta():
        E.frase(c, t, C["s07"] + 0.2, ps("repare no que você fez", "i", 72, TINTA2), W / 2, 160, "center", 0.12)
        E.linha(c, t, [("72", "g", 110, TINTA, a7 - 0.3), ("× 1.000", "g", 110, COR, a7), ("÷ 3.600", "g", 110, COR, a7 + 0.8)], W / 2, 330, "center")
        fcen(c, t, b7, "3.600 ÷ 1.000 = 3,6", W / 2, 500, 90)
        E.frase(c, t, b7 + 0.6, ps("o mil cabe", "i", 60, TINTA2) + [("3,6 vezes", "g", 60)] + ps("no 3.600", "i", 60, TINTA2), W / 2, 590, "center", 0.08)
        E.frase(c, t, c7 - 0.8, ps("as duas contas =", "i", 70), 760, 760, "center", 0.1)
        E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "÷ 3,6", 1360, 738, 84, "g", a=a))
        fcen(c, t, lerp(c7, e7, 0.45), "72 ÷ 3,6 = 20", W / 2 - 40, 960, 96, CERTO)
        E.foco(c, t, lerp(c7, e7, 0.6), 0.5, lambda a: E.selo(c, W / 2 + 360, 926, 46, True, a))
    E.saida(c, t, C["s08"] - 0.1, junta)
    if t < C["s08"]:
        return
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    caixas(c, t, C["s08"], a8, b8, 330)
    E.foco(c, t, a8 + 0.4, 0.5, lambda a: centro(c, "ida: divida", 960, 200, 54, "i", COR, a))
    E.foco(c, t, b8 + 0.4, 0.5, lambda a: centro(c, "volta: multiplique", 960, 490, 54, "i", TINTA, a))
    E.frase(c, t, c8 - 0.5, ps("teste:", "i", 66, TINTA2), 360, 720, "left")
    fcen(c, t, c8, "54 ÷ 3,6", 760, 720, 100)
    E.foco(c, t, d8 - 0.8, 0.5, lambda a: E.pilula(c, "× 10 nos dois", 760, 830, 48, "g", fundo=TINTA, a=a))
    fcen(c, t, d8, "540 ÷ 36 = 15 m/s", 760, 980, 100, COR)
    bola_res(c, t, d8 + 1.0, "15 m/s", 1500, 860, 150, 64)


# ---------------- a volta ----------------
def b_volta(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    E.frase(c, t, C["s09"] + 0.2, ps("o caminho de", "i", 72) + [("volta", "g", 76, COR)], W / 2, 170, "center", 0.12)
    fcen(c, t, a9, "15 m/s", 520, 360, 120, COR)
    E.ponte(c, t, a9 + 0.4, 800, 1120, 320, "× 3,6", TINTA, 48)
    fcen(c, t, b9, "15 × 3,6", 1400, 360, 110)
    fcen(c, t, lerp(b9, c9, 0.25), "15 × 3 = 45", 960, 560, 90)
    fcen(c, t, lerp(b9, c9, 0.6), "15 × 0,6 = 9", 960, 700, 90)
    fcen(c, t, c9, "45 + 9 = 54 km/h", 760, 900, 110, COR)
    bola_res(c, t, c9 + 1.0, "54 km/h", 1560, 860, 150, 62)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0, e0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.end"]

    def errado():
        E.frase(c, t, C["s10"] + 0.2, ps("o erro:", "i", 80) + [("errar a direção", "g", 84, ERRADO)], W / 2, 180, "center", 0.12)
        fcen(c, t, lerp(a0, b0, 0.45), "72 × 3,6", W / 2, 400, 110)
        fcen(c, t, b0, "= 259,2 m/s", W / 2, 560, 110, ERRADO)
        E.foco(c, t, b0 + 0.6, 0.5, lambda a: E.selo(c, 1520, 520, 50, False, a))
        E.frase(c, t, c0, ps("mais de", "i", 72) + [("250 metros", "g", 76, ERRADO)] + ps("a cada segundo", "i", 72), W / 2, 760, "center", 0.1)
        E.frase(c, t, lerp(c0, e0, 0.5), ps("coisa de avião,", "i", 70, TINTA2) + [("não de carro", "g", 72)], W / 2, 900, "center", 0.1)
    E.saida(c, t, C["s11"] - 0.1, errado)
    if t < C["s11"]:
        return
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    E.frase(c, t, C["s11"] + 0.2, ps("para nunca errar", "i", 72, COR), W / 2, 160, "center", 0.12)
    fcen(c, t, lerp(C["s11"], a1, 0.3), "1 m/s = 3,6 km/h", W / 2, 320, 110)
    E.frase(c, t, a1, ps("mesma velocidade:", "i", 66) + [("número maior em km/h", "g", 68, COR)], W / 2, 470, "center", 0.1)
    E.linha(c, t, [("indo para km/h:", "i", 72, TINTA, b1), ("cresce,", "g", 76, TINTA, b1 + 0.4), ("multiplica", "g", 76, COR, b1 + 0.8)], W / 2, 680, "center")
    E.linha(c, t, [("indo para m/s:", "i", 72, TINTA, c1), ("diminui,", "g", 76, TINTA, c1 + 0.4), ("divide", "g", 76, COR, c1 + 0.8)], W / 2, 850, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]

    def pares():
        E.frase(c, t, C["s12"] + 0.1, ps("agora, o atalho:", "i", 70, CLARO) + [("guarde 3 pares", "g", 76, BR)], W / 2, 170, "center", 0.12)
        E.foco(c, t, a2, 0.5, lambda a: (centro(c, "km/h", 700, 320, 60, "i", CLARO, a), centro(c, "m/s", 1220, 320, 60, "i", CLARO, a)))
        for k, kmh, ms, y in ((b2, "36", "10", 480), (c2, "72", "20", 650), (d2, "108", "30", 820)):
            fcen(c, t, k, kmh, 700, y, 130, BR)
            E.foco(c, t, k + 0.2, 0.4, lambda a, y=y: centro(c, "=", 960, y - 10, 100, "g", CLARO, a))
            fcen(c, t, k + 0.4, ms, 1220, y, 130, CLARO)
    E.saida(c, t, C["s13"] - 0.1, pares)

    a3, b3 = C["s13.a"], C["s13.b"]
    if C["s13"] <= t:
        def porque():
            fcen(c, t, a3, "36 ÷ 3,6 = 10", W / 2, 230, 100, BR)
            E.frase(c, t, a3 + 1.0, ps("exato", "i", 60, CLARO), W / 2, 320, "center")
            E.frase(c, t, lerp(a3, b3, 0.18), ps("os outros:", "i", 64, CLARO) + [("o dobro e o triplo", "g", 66, BR)], W / 2, 430, "center", 0.1)
            E.frase(c, t, lerp(a3, b3, 0.32), ps("e", "i", 90, CLARO) + [("90?", "g", 100, BR)], W / 2, 580, "center", 0.12)
            fcen(c, t, lerp(a3, b3, 0.48), "90 = 72 + 18", W / 2, 720, 96, BR)
            k18 = lerp(a3, b3, 0.7)
            E.linha(c, t, [("18", "g", 72, BR, k18), ("é a metade de 36:", "i", 66, CLARO, k18 + 0.2), ("5 m/s", "g", 72, BR, b3 - 0.2)], W / 2, 830, "center")
            fcen(c, t, b3, "20 + 5 = 25 m/s", W / 2, 980, 104, CLARO)
        E.saida(c, t, C["s14"] - 0.1, porque)

    if t < C["s14"]:
        return
    a4, b4 = C["s14.a"], C["s14.b"]
    E.foco(c, t, a4, 0.5, lambda a: E.selo(c, 330, 300, 50, False, a))
    E.frase(c, t, a4 + 0.1, ps("não compensa com", "i", 76, CLARO) + [("100 km/h", "g", 84, BR)], 420, 325, "left", 0.1)
    fcen(c, t, lerp(a4, b4, 0.45), "100 ÷ 3,6 = 27,77...", W / 2, 560, 110, BR)
    E.frase(c, t, lerp(a4, b4, 0.7), ps("os setes não acabam", "i", 64, CLARO), W / 2, 670, "center", 0.1)
    E.frase(c, t, b4, ps("aí,", "i", 80, CLARO) + [("divida por 3,6 direto", "g", 84, BR)], W / 2, 880, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.foco(c, t, a5 - 0.2, 0.5, lambda a: placa(c, XE + 110, 380, 110, "90", a))
    E.frase(c, t, a5, ps("limite:", "i", 80) + [("90 km/h", "g", 88, COR)], XE + 260, 410, passo=0.12)
    E.frase(c, t, b5, ps("o radar mede", "i", 80) + [("30 m/s", "g", 88, COR)], XE, 620, passo=0.12)
    E.frase(c, t, c5, ps("está", "i", 96) + [("acima do limite?", "g", 100, COR)], XE, 820, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1590, 430, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]

    def conta():
        E.frase(c, t, C["s17"] + 0.3, ps("passe para", "i", 76) + [("km/h", "g", 80, COR)], W / 2, 180, "center", 0.12)
        E.foco(c, t, a7, 0.5, lambda a: E.pilula(c, "× 3,6", W / 2, 320, 70, "g", a=a))
        fcen(c, t, b7, "30 × 3,6 = 108 km/h", 760, 540, 110)
        E.foco(c, t, c7 - 0.3, 0.5, lambda a: placa(c, 1540, 500, 130, "90", a))
        E.linha(c, t, [("108 > 90:", "g", 96, TINTA, c7), ("acima do limite", "g", 96, ERRADO, c7 + 0.6)], W / 2, 820, "center")
    E.saida(c, t, C["s18"] - 0.1, conta)
    if t < C["s18"]:
        return
    a8, b8 = C["s18.a"], C["s18.b"]
    E.frase(c, t, C["s18"] + 0.2, ps("pelo atalho,", "i", 76) + [("sem conta", "g", 80, COR)], W / 2, 180, "center", 0.12)
    fcen(c, t, a8, "30 m/s = 108 km/h", W / 2, 360, 110, COR)
    E.frase(c, t, a8 + 1.0, ps("é um dos 3 pares", "i", 60, TINTA2), W / 2, 450, "center", 0.1)
    E.frase(c, t, b8 - 0.6, ps("ou pelo", "i", 66, TINTA2) + [("outro lado:", "g", 66)], W / 2, 610, "center", 0.1)
    fcen(c, t, b8, "90 km/h = 25 m/s", W / 2, 760, 104)
    fcen(c, t, lerp(b8, C["s18.end"], 0.5), "30 > 25", W / 2, 920, 110, ERRADO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s19.a", "para m/s:", "÷ 3,6"), ("s19.b", "para km/h:", "× 3,6"), ("s19.c", "km/h tem sempre", "o número maior"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 76) + [(l2, "g", 80, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, a0, ps("ida a", "i", 80) + [("40 km/h,", "g", 88, COR)] + ps("volta a", "i", 80) + [("60", "g", 88, COR)], XE, 400, passo=0.12)
    E.frase(c, t, b0, ps("a média", "i", 84) + [("não é 50", "g", 96, ERRADO)], XE, 540, passo=0.12)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1020, 815, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, unidades=b_unidades, deducao=b_deducao, fator=b_fator, volta=b_volta,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
