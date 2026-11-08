"""Visual — Estudativo · MAT-RAZ-005: direta, inversa ou nenhuma, o teste do dobro.
Peças locais: a tabela de duas grandezas da trilha (cabeca com nome em itálico e fio; valores grandes), salto() é a seta entre
duas linhas com a operação numa pílula (× 2 subindo junto, ÷ 2 caindo pela metade), tipo() é a pílula da resposta (direta,
inversa, nenhuma); corrida() é a barra do preço do táxi: a bandeirada fixa em preto e um pedaço de R$ 3 por quilômetro na cor
da matéria; vela() é a vela que queima. Instantes: cues C[...] e a palavra falada (PW, lida de audio/tempos.json)."""
import json
import unicodedata
from pathlib import Path

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-005_teste_do_dobro.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("teste", "taxi", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CHAMA = "#FFB21F"
# as contas da aula, conferidas
assert 5 + 3 * 2 == 11 and 5 + 3 * 4 == 17 and 2 * 11 == 22 != 17
assert 2 * 8 == 16 and 30 * 4 == 60 * 2 == 120
assert 20 - 2 * 2 == 16 and 20 - 2 * 4 == 12 and 16 // 2 == 8 and 2 * 16 == 32 and 4 * 12 == 48
assert 120 // 2 == 60 and 120 // 4 == 30 and 50 + 80 == 130 and 50 + 160 == 210 and 2 * 130 == 260
assert 18 // 3 == 6

_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))


def _n(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower()) if ch.isalnum())


def PW(sid, palavra, n=1):
    """instante em que a voz diz a n-ésima `palavra` da cena sid"""
    for s in _TEMPOS["scenes"]:
        if s["id"] == sid:
            k = 0
            for tk in s["tokens"]:
                if _n(tk["disp"]) == _n(palavra):
                    k += 1
                    if k == n:
                        return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, n))


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


# --- tabela (mesma linguagem de MAT-RAZ-004 e 007) ---
Y0, DY = 300, 150


def ylin(i):
    return Y0 + DY * (i + 1)


def cabeca(c, t, t0, nome, cx, y=Y0, size=54, cor=None, larg=300):
    E.foco(c, t, t0, 0.5, lambda a: (centro(c, nome, cx, y, size, "i", cor or TINTA2, a),
                                      M.line(c, cx - larg / 2, y + 30, cx + larg / 2, y + 30, FIO, a, 3)))


def valor(c, t, t0, s, cx, i, size=96, cor=TINTA):
    E.formula_em(c, t, t0, s, cx, ylin(i) + size * 0.36, size, "g", cor, "center")


def salto(c, t, t0, x, rot, desce=True, cor=None, escuro=False):
    """seta da linha 0 para a 1 ao lado da coluna, com a operação numa pílula ao lado"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    cor = cor or E.COR
    ya, yb = ylin(0) - 30, ylin(1) + 30
    M.arrow(c, x, ya, x, yb, cor, p, 7, 26, ease_io(prog(t, t0, 0.6)))
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.pilula(c, rot, x + 90, (ya + yb) / 2, 44, "g", fundo=cor, cor=M.on(cor) if not escuro else BR, a=a))


def tipo(c, t, t0, s, cx, cy, cor=None, size=60):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor or E.COR, cor=E.SOBRE, a=a))


def saida_n(c, t, t0, n, txt, y=170):
    """número da saída numa esfera e o texto ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 46, y - 26, 46, a=a), centro(c, str(n), XE + 46, y - 4, 56, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.1, ps(txt, "i", 72), XE + 120, y, passo=0.1)


def corrida(c, t, t0, km, x, y, h=110, px=40, tk=None, a=1.0, realce_km=0.0, realce_fixa=0.0):
    """barra do preço do táxi: bandeirada de R$ 5 (preto) + R$ 3 por km (pedaços na cor da matéria). tk = instante dos km"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return x
    w5 = 5 * px
    M.rrect(c, x, y, w5 - 6, h, 14, TINTA, q)
    centro(c, "5", x + w5 / 2, y + h / 2 + 22, 60, "g", BR, q)
    xx = x + w5
    for i in range(km):
        qi = ep(t, (tk if tk is not None else t0) + 0.12 * i, 0.35) * a
        if qi > 0:
            M.rrect(c, xx + i * 3 * px, y, 3 * px - 6, h, 14, E.COR, qi)
            centro(c, "3", xx + i * 3 * px + 1.5 * px, y + h / 2 + 22, 54, "g", BR, qi)
    if realce_km > 0:
        E.caixa_pontilhada(c, xx - 10, y - 12, km * 3 * px + 8, h + 24, realce_km * a, E.COR, prog_=realce_km)
    if realce_fixa > 0:
        E.caixa_pontilhada(c, x - 10, y - 12, w5 + 8, h + 24, realce_fixa * a, TINTA, prog_=realce_fixa)
    return xx + km * 3 * px


def vela(c, cx, base, cm, a=1.0, tracejada=False, px=18):
    """vela de cm centímetros (px por cm), com chama"""
    if a <= 0:
        return
    h, w = cm * px, 92
    if tracejada:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, base - h, w, h), 12, 12)
        p = M.paint(ERRADO, a, stroke=5)
        p.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
        c.drawRRect(r, p)
        return
    M.rrect(c, cx - w / 2, base - h, w, h, 12, E.COR, a)
    M.line(c, cx, base - h, cx, base - h - 18, TINTA, a, 4)
    pt = skia.Path()
    top = base - h - 18
    pt.moveTo(cx, top - 62)
    pt.quadTo(cx + 30, top - 20, cx, top)
    pt.quadTo(cx - 30, top - 20, cx, top - 62)
    c.drawPath(pt, M.paint(CHAMA, a))


# ---------------- gancho ----------------
XQ, XP = 560, 1100


def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def cena():
        E.frase(c, t, C["s01"] + 0.2, ps("uma corrida de", "i", 72) + [("táxi", "g", 72, COR)], W / 2, 170, "center", 0.12)
        cabeca(c, t, a1 - 0.3, "distância", XQ)
        cabeca(c, t, a1 - 0.1, "preço", XP)
        valor(c, t, a1, "2 km", XQ, 0)
        valor(c, t, PW("s01", "onze"), "R$ 11", XP, 0)
        valor(c, t, PW("s01", "quatro"), "4 km", XQ, 1)
        tn = PW("s01", "Nao")

        def vinte_dois():
            valor(c, t, b1, "R$ 22?", XP, 1, cor=CINZA)
            if t >= tn:
                E.risco(c, XP - 170, ylin(1) + 40, XP + 170, ylin(1) - 40, t, tn, ERRADO, 10)
        E.saida(c, t, c1 - 0.1, vinte_dois)
        valor(c, t, c1 + 0.2, "R$ 17", XP, 1, cor=COR)
        salto(c, t, PW("s01", "dobrou"), XQ + 200, "× 2")
        E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "não dobrou", XP + 330, (ylin(0) + ylin(1)) / 2, 50, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, PW("s02", "decide"), ps("decidir", "i", 84) + [("em segundos", "g", 96, COR)], XE, 490, passo=0.12)
        E.frase(c, t, PW("s02", "grandezas"), ps("se são", "i", 84) + [("proporcionais", "g", 84, COR)], XE, 640, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "na direta,", "a divisão não muda"), ("s03.c", "na inversa,", "o produto não muda"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 710, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, PW("s03", "faltar"), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- o teste do dobro ----------------
def b_teste(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]

    def intro():
        E.frase(c, t, C["s04"] + 0.3, ps("o teste do", "i", 110) + [("dobro", "g", 120, COR)], W / 2, 300, "center", 0.12)
        E.frase(c, t, a4, [("dobre", "g", 76, COR)] + ps("uma grandeza,", "i", 72) + [("olhe", "g", 76, COR)] + ps("a outra", "i", 72), W / 2, 450, "center", 0.12)
        E.foco(c, t, b4, 0.5, lambda a: centro(c, "3 saídas", W / 2, 620, 80, "g", TINTA, a))
        for i, (s, cor) in enumerate((("dobra", E.COR), ("cai pela metade", TINTA), ("nem um, nem outro", CINZA))):
            E.foco(c, t, b4 + 0.4 + 0.3 * i, 0.5, lambda a, s=s, cor=cor, i=i: E.pilula(c, s, (380, 900, 1480)[i], 780, 52, "g", fundo=cor, a=a))
    E.saida(c, t, C["s05"] - 0.1, intro)

    # 1ª saída: direta
    def direta():
        a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
        saida_n(c, t, a5, 1, "a outra também dobra")
        tipo(c, t, b5, "direta", 1620, 150)
        cabeca(c, t, PW("s05", "Um"), "quilos", XQ)
        cabeca(c, t, PW("s05", "Um") + 0.2, "preço (R$)", XP)
        valor(c, t, PW("s05", "Um"), "1", XQ, 0)
        valor(c, t, PW("s05", "oito"), "8", XP, 0)
        valor(c, t, PW("s05", "Dois"), "2", XQ, 1)
        valor(c, t, c5, "16", XP, 1)
        salto(c, t, PW("s05", "Dois") + 0.2, XQ + 160, "× 2")
        salto(c, t, c5 + 0.2, XP + 160, "× 2")
        E.frase(c, t, PW("s05", "Se"), ps("preço do quilo", "i", 66) + [("não muda", "g", 66, COR)], W / 2, 860, "center", 0.12)
        E.frase(c, t, d5, ps("o dobro de quilos custa", "i", 66) + [("o dobro", "g", 66, COR)], W / 2, 970, "center", 0.12)
    if C["s05"] <= t:
        E.saida(c, t, C["s06"] - 0.1, direta)

    # 2ª saída: inversa
    def inversa():
        a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        saida_n(c, t, a6, 2, "a outra cai pela metade")
        tipo(c, t, b6, "inversa", 1620, 150, TINTA)
        tv = PW("s06", "Na")
        E.foco(c, t, tv, 0.5, lambda a: centro(c, "viagem de 120 km", 1620, 250, 50, "i", TINTA2, a))
        cabeca(c, t, tv + 0.3, "velocidade (km/h)", XQ, larg=380)
        cabeca(c, t, tv + 0.5, "tempo (h)", XP)
        valor(c, t, PW("s06", "trinta"), "30", XQ, 0)
        valor(c, t, PW("s06", "quatro"), "4", XP, 0)
        valor(c, t, PW("s06", "sessenta"), "60", XQ, 1)
        valor(c, t, c6, "2", XP, 1)
        salto(c, t, PW("s06", "sessenta") + 0.2, XQ + 180, "× 2")
        salto(c, t, c6 + 0.2, XP + 160, "÷ 2", cor=TINTA)
        fcen(c, t, PW("s06", "produto"), "30 · 4 = 60 · 2 = 120", W / 2, 870, 76, TINTA)
        E.frase(c, t, d6, ps("um dobra,", "i", 62) + [("o outro cai pela metade", "g", 62, COR)], W / 2, 980, "center", 0.12)
    if C["s06"] <= t:
        E.saida(c, t, C["s07"] - 0.1, inversa)

    # 3ª saída: nenhuma
    if t >= C["s07"]:
        a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
        saida_n(c, t, a7, 3, "nem dobra, nem cai pela metade")
        E.foco(c, t, b7, 0.5, lambda a: E.pilula(c, "nem direta, nem inversa", W / 2, 360, 70, "g", fundo=CINZA, a=a))
        E.frase(c, t, PW("s07", "dobro"), ps("o dobro é só o mais fácil:", "i", 66), W / 2, 540, "center", 0.12)
        E.frase(c, t, c7, ps("com o", "i", 66) + [("triplo (× 3)", "g", 70, COR)] + ps("funciona igual", "i", 66), W / 2, 640, "center", 0.12)
        E.foco(c, t, d7, 0.5, lambda a: E.pilula(c, "mude só uma grandeza", W / 2, 810, 60, "g", a=a))
        E.frase(c, t, PW("s07", "Na"), ps("na viagem, a distância", "i", 58) + [("continua 120 km", "g", 58, COR)], W / 2, 950, "center", 0.1)


# ---------------- o táxi ----------------
TX = 560


def b_taxi(c, t, C, b):
    a8, b8 = C["s08.a"], C["s08.b"]
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]

    def regra():
        E.frase(c, t, C["s08"] + 0.3, ps("o", "i", 84) + [("táxi", "g", 84, COR)], W / 2, 190, "center")
        E.foco(c, t, a8, 0.5, lambda a: (M.rrect(c, 560, 330, 200, 130, 16, TINTA, a), centro(c, "R$ 5", 660, 418, 64, "g", BR, a)))
        E.frase(c, t, a8 + 0.3, [("bandeirada", "g", 76, TINTA)], 820, 420)
        E.frase(c, t, PW("s08", "valor"), ps("valor fixo, pago ao entrar,", "i", 56, TINTA2), 820, 500, passo=0.1)
        E.frase(c, t, PW("s08", "mesmo"), ps("mesmo sem andar nada", "i", 56, TINTA2), 820, 570, passo=0.1)
        E.frase(c, t, PW("s08", "Ela"), ps("não depende da distância", "g", 56, COR), 820, 640, passo=0.1)
        E.foco(c, t, b8, 0.5, lambda a: (M.rrect(c, 560, 740, 120, 130, 16, E.COR, a), centro(c, "R$ 3", 620, 828, 46, "g", BR, a)))
        E.frase(c, t, b8 + 0.3, [("por quilômetro", "g", 76, COR)], 820, 830)
    E.saida(c, t, C["s09"] - 0.1, regra)
    if t < C["s09"]:
        return

    def barras():
        y1, y2 = 240, 470
        E.foco(c, t, C["s09"] + 0.3, 0.5, lambda a: E.escreve(c, "2 km", XE, y1 + 80, 70, "g", TINTA, a))
        xe = corrida(c, t, C["s09"] + 0.3, 2, TX, y1, tk=PW("s09", "seis"), realce_km=ep(t, c9, 0.5), realce_fixa=ep(t, d9, 0.5))
        E.formula_em(c, t, a9, "5 + 6 = 11", xe + 50, y1 + 80, 70, "g", TINTA)
        E.foco(c, t, PW("s09", "Quatro"), 0.5, lambda a: E.escreve(c, "4 km", XE, y2 + 80, 70, "g", TINTA, a))
        xe = corrida(c, t, PW("s09", "Quatro"), 4, TX, y2, tk=PW("s09", "doze"), realce_km=ep(t, c9 + 0.3, 0.5), realce_fixa=ep(t, d9, 0.5))
        E.formula_em(c, t, b9, "5 + 12 = 17", xe + 50, y2 + 80, 70, "g", TINTA)
        E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "6 → 12: dobrou", 1200, 680, 50, "g", a=a))
        E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "5 → 5: ficou", 660, 680, 50, "g", fundo=TINTA, a=a))
    barras()
    E.saida(c, t, c10 - 0.1, lambda: (E.frase(c, t, a10, [("não é proporcional", "g", 70, ERRADO)] + ps("à distância", "i", 66), W / 2, 830, "center", 0.12),
                                      E.frase(c, t, b10, ps("um pedaço do preço", "i", 62) + [("não acompanha os km", "g", 62, COR)], W / 2, 950, "center", 0.1)))
    if t >= c10:
        for i, (s, tw) in enumerate((("taxa fixa", c10), ("matrícula", PW("s10", "matricula")), ("bandeirada", PW("s10", "bandeirada")))):
            E.foco(c, t, tw, 0.45, lambda a, s=s, i=i: E.pilula(c, s, 560 + i * 400, 830, 56, "g", fundo=TINTA, a=a))
        E.frase(c, t, PW("s10", "desconfie"), [("desconfie!", "g", 84, ERRADO)], W / 2, 990, "center")


# ---------------- erro ----------------
VX = (400, 700, 1000)  # as três velas
VB = 840


def b_erro(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    E.frase(c, t, C["s11"] + 0.3, ps("o erro:", "i", 72) + [("um sobe, o outro desce,", "g", 72, ERRADO)] + ps("é inversa?", "i", 72), W / 2, 150, "center", 0.1)
    for cx, cm, h, t0 in ((VX[0], 20, "0 h", b11), (VX[1], 16, "2 h", c11), (VX[2], 12, "4 h", d11)):
        E.foco(c, t, t0, 0.5, lambda a, cx=cx, cm=cm: vela(c, cx, VB, cm, a))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a, cx=cx, cm=cm, h=h: (centro(c, h, cx, VB + 70, 52, "i", TINTA2, a), centro(c, f"{cm} cm", cx, VB + 150, 60, "g", COR, a)))
    E.foco(c, t, PW("s11", "queima"), 0.5, lambda a: E.pilula(c, "− 2 cm por hora", 1500, 330, 50, "g", fundo=TINTA, a=a))
    # se fosse inversa: 8 cm
    E.saida(c, t, b12 - 0.1, lambda: E.foco(c, t, a12, 0.5, lambda a: (vela(c, VX[2] + 160, VB, 8, a, tracejada=True),
                                                                     centro(c, "8?", VX[2] + 160, VB - 8 * 18 - 30, 60, "g", ERRADO, a))))
    E.foco(c, t, a12 - 0.5, 0.5, lambda a: E.escreve(c, "se fosse inversa: 8 cm", 1260, 470, 50, "i", ERRADO, a * (1 - ep(t, b12, 0.3))))
    E.foco(c, t, b12, 0.5, lambda a: E.pilula(c, "nem inversa, nem direta", 1540, 470, 44, "g", fundo=ERRADO, a=a))
    E.frase(c, t, c12, ps("só descer", "i", 60) + [("não basta", "g", 60, ERRADO)], 1560, 590, "center", 0.12)
    fcen(c, t, d12, "2 · 16 = 32", 1560, 740, 76, TINTA)
    fcen(c, t, e12, "4 · 12 = 48", 1560, 860, 76, TINTA)
    E.foco(c, t, PW("s12", "Mudou"), 0.5, lambda a: E.pilula(c, "mudou", 1560, 960, 56, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]

    def zero():
        E.frase(c, t, C["s13"] + 0.3, ps("o atalho:", "i", 72, CLARO), W / 2, 150, "center")
        E.frase(c, t, a13, ps("o teste do", "i", 110, CLARO) + [("zero", "g", 120, BR)], W / 2, 290, "center", 0.12)
        linhas = ((b13, "direta:", "0 kg → R$ 0", None), (c13, "táxi:", "0 km → R$ 5", d13), (e13, "vela:", "0 h → 20 cm", e13 + 1.2))
        for i, (t0, rot, s, tn) in enumerate(linhas):
            y = 470 + i * 170
            E.foco(c, t, t0, 0.5, lambda a, rot=rot, y=y: E.escreve(c, rot, 300, y, 60, "i", CLARO, a))
            E.formula_em(c, t, t0 + 0.2, s, 560, y, 84, "g", BR)
            if tn is None:
                E.foco(c, t, PW("s13", "zero", 3), 0.5, lambda a, y=y: E.selo(c, 1300, y - 28, 40, True, a))
            else:
                E.foco(c, t, tn, 0.5, lambda a, y=y: E.pilula(c, "não é direta", 1400, y - 28, 50, "g", fundo=ERRADO, cor=BR, a=a))
    E.saida(c, t, C["s14"] - 0.1, zero)

    if t >= C["s14"]:
        a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
        E.frase(c, t, a14, ps("na direta:", "i", 66, CLARO) + ps("uma = outra × número fixo", "g", 66, BR), W / 2, 230, "center", 0.1)
        fcen(c, t, PW("s14", "zero"), "0 · 8 = 0", W / 2, 360, 90, CLARO)
        E.frase(c, t, b14, ps("não descobre se é", "i", 66, CLARO) + ps("inversa", "g", 66, BR), W / 2, 540, "center", 0.12)
        E.frase(c, t, PW("s14", "zero", 3), ps("o zero só", "i", 66, CLARO) + ps("descarta a direta", "g", 66, BR), W / 2, 640, "center", 0.12)
        E.frase(c, t, c14 - 0.9, ps("para o resto,", "i", 100, CLARO) + ps("dobre", "g", 120, BR), W / 2, 870, "center", 0.12)


# ---------------- questão ----------------
def item_q(c, t, t0, n, l1, l2, y, size=50):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 36, y - 20, 36, a=a), centro(c, str(n), XE + 36, y - 2, 44, "g", E.SOBRE, a)))
    E.frase(c, t, t0 + 0.1, [(l1, "g", size)], XE + 100, y)
    E.frase(c, t, t0 + 0.4, [(l2, "i", size - 4, TINTA2)], XE + 100, y + 64)


def b_questao(c, t, C, b):
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 64, COR), XE, 150)
    E.frase(c, t, PW("s15", "Diga"), [("direta,", "g", 64, COR)] + [("inversa", "g", 64, COR)] + ps("ou", "i", 64) + [("nenhuma?", "g", 64, COR)], XE, 260, passo=0.12)
    item_q(c, t, a15, 1, "ingressos iguais comprados", "e o valor total pago", 420)
    item_q(c, t, b15, 2, "pessoas que dividem uma conta de R$ 120", "e quanto cada uma paga", 610)
    item_q(c, t, c15, 3, "academia: matrícula R$ 50 + R$ 80 por mês", "e o total pago em cada número de meses", 800)
    E.relogio(c, t, C["s16.a"], 1640, 470, 160)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]

    def doze():
        E.frase(c, t, C["s17"] + 0.3, ps("dobrando", "i", 72, COR), W / 2, 150, "center")
        item_q(c, t, a17, 1, "ingressos", "o preço de cada um não muda", 310, 60)
        E.foco(c, t, PW("s17", "dobro"), 0.5, lambda a: E.pilula(c, "× 2 → × 2", 1100, 300, 54, "g", fundo=TINTA, a=a))
        tipo(c, t, PW("s17", "direta"), "direta", 1500, 300)
        item_q(c, t, b17, 2, "conta de R$ 120", "", 560, 60)
        fcen(c, t, PW("s17", "duas"), "2 pessoas: R$ 60 cada", 760, 720, 70, TINTA)
        fcen(c, t, PW("s17", "Quatro"), "4 pessoas: R$ 30 cada", 760, 840, 70, TINTA)
        E.foco(c, t, PW("s17", "Caiu"), 0.5, lambda a: E.pilula(c, "÷ 2", 1250, 780, 54, "g", fundo=TINTA, a=a))
        tipo(c, t, c17, "inversa", 1500, 780, TINTA)
    E.saida(c, t, C["s18"] - 0.1, doze)
    if t < C["s18"]:
        return
    item_q(c, t, a18, 3, "academia", "matrícula R$ 50 + R$ 80 por mês", 220, 60)
    fcen(c, t, PW("s18", "um"), "1 mês: 50 + 80 = 130", 760, 450, 76, TINTA)
    fcen(c, t, b18, "2 meses: 50 + 160 = 210", 760, 580, 76, TINTA)
    fcen(c, t, PW("s18", "dobro"), "o dobro de 130 seria 260", 760, 720, 66, ERRADO)
    E.foco(c, t, PW("s18", "dobro") + 1.6, 0.5, lambda a: centro(c, "≠ 210", 1300, 720, 66, "g", ERRADO, a))
    tipo(c, t, c18, "nenhuma", 1550, 500, CINZA, 70)
    E.frase(c, t, PW("s18", "matricula"), [("matrícula", "g", 70, COR)] + ps("faz o papel da", "i", 66) + [("bandeirada", "g", 70, COR)], W / 2, 900, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", "dobrou junto: direta"), ("s19.b", "caiu pela metade: inversa"), ("s19.c", "nenhum dos dois: nenhuma"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, a20, [("regra de três", "g", 130, COR)], XE, 460)
    E.frase(c, t, a20 + 0.4, [("direta", "g", 130, COR)], XE, 600)
    E.frase(c, t, b20, ps("3 kg custam R$ 18;", "i", 64) + [("7 kg?", "g", 64, COR)], XE, 730, passo=0.12)
    E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, c20 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, c20 + 0.2, 0.4))
    E.frase(c, t, d20, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, teste=b_teste, taxi=b_taxi, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
