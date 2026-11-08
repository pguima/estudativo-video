"""Visual — Estudativo · MAT-RAZ-017: densidade.
Peças locais: tanque() é o aquário de água em que os objetos caem e boiam (na linha d'água) ou afundam (no fundo), no
tempo da fala; cubinhos() mostra o volume em cubinhos de 1 cm³. Mesma tipografia das aulas vizinhas da trilha
(índigo = o que boia e o que está sendo calculado, preto = o que afunda, vermelho = erro, verde = conferido).
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-017_densidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "exemplos", "agua", "material", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AGUA = E.mix(E.COR, "#FFFFFF", 0.78)
# as contas da aula, conferidas
assert D(600) / 1000 == D("0.6") and D(150) / 60 == D("2.5") and D("2.5") * 200 == 500 and D(1000) / 1000 == 1
assert D(1200) / 2000 == D("0.6") and D(300) / 500 == D("0.6") and 600 < 1000
assert D(450) / 500 == D("0.9") and D(270) / 100 == D("2.7") and 450 < 500 and 270 > 100


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


def tanque(c, t, x, y, w, h, objs, a=1.0, nivel=0.35):
    """aquário com água a partir de y + h*nivel. objs = [(cx, ow, oh, cor, rotulo, t0, boia)]: o objeto cai no t0 e
    para na linha d'água (boia, 60% para dentro) ou no fundo (afunda)"""
    if a <= 0:
        return
    yw = y + h * nivel
    M.rrect(c, x, yw, w, y + h - yw, 0, AGUA, a)
    for i in range(3):  # ondinhas
        yy = yw + 4
        M.line(c, x + 40 + i * w / 3, yy, x + 40 + i * w / 3 + 80, yy, BR, 0.8 * a, 4)
    for cx, ow, oh, cor, rot, t0, boia in objs:
        p = prog(t, t0, 1.0)
        if p <= 0:
            continue
        fim = yw - oh * 0.4 if boia else y + h - oh - 6
        if boia:  # cai, mergulha um pouco e volta
            yo = lerp(y - oh - 40, fim, ease_io(min(1, p / 0.5))) + (18 * M.math.sin((p - 0.5) * 9) * (1 - p) if p > 0.5 else 0)
        else:
            yo = lerp(y - oh - 40, fim, ease_io(p))
        q = min(1.0, p * 3) * a
        M.rrect(c, cx - ow / 2, yo, ow, oh, 12, cor, q)
        if rot:
            centro(c, rot, cx, yo + oh / 2 + 18, 46, "g", M.on(cor), q)
    # paredes por cima
    path = skia.Path(); path.moveTo(x, y); path.lineTo(x, y + h); path.lineTo(x + w, y + h); path.lineTo(x + w, y)
    c.drawPath(path, M.paint(TINTA, a, stroke=6, cap_round=True))


def cubinhos(c, x, y, n_lado, lado, a, cor=None):
    """n_lado x n_lado cubinhos (vista de frente) a partir de (x, y)"""
    if a <= 0:
        return
    for i in range(n_lado):
        for j in range(n_lado):
            M.rrect(c, x + i * lado, y + j * lado, lado - 4, lado - 4, 4, cor or E.COR, a * 0.85)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def cena():
        objs = [(640, 420, 110, E.mix("#8A5A2B", E.COR, 0.0), "300 kg", a1 + 0.3, True), (1300, 90, 30, TINTA, "", b1 + 0.6, False)]
        tanque(c, t, 300, 300, 1320, 560, objs, ep(t, C["s01"], 0.5))
        E.frase(c, t, a1, ps("tronco de", "i", 64) + [("300 kg:", "g", 68)] + [("boia", "g", 68, COR)], 640, 220, "center", 0.1)
        E.frase(c, t, b1 + 0.2, ps("clipe:", "i", 64) + [("afunda", "g", 68)], 1300, 220, "center", 0.1)
        E.frase(c, t, lerp(b1, c1, 0.6), ps("não é o", "i", 70) + [("peso", "g", 74, ERRADO)] + ps("que decide", "i", 70), W / 2, 960, "center", 0.1)
        E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "é a densidade", W / 2, 1040, 50, "g", a=a))
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), [("densidade", "g", 120, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("boia ou", "i", 90) + [("afunda?", "g", 96, COR)], XE, 610, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a3, b3, c3, d3, e3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"], C["s03.end"]
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, a3, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, a3 + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    for i, (k, l1, l2) in enumerate(((b3, "ler uma taxa:", "“por” = dividido"), (c3, "o volume:", "1 L = 1.000 cm³"))):
        y = 150 + i * 240
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, (k + 0.3) if i == 0 else d3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q = ease_io(prog(t, c3 - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(320, 560, q), ep(t, b3, 0.4))
    # o cubinho de 1 cm
    tc = lerp(c3, d3, 0.3)
    E.foco(c, t, tc, 0.5, lambda a: (M.rrect(c, x + 60, 690, 120, 120, 10, E.COR, a), E.escreve(c, "1 cm", x + 80, 860, 44, "g", TINTA, a),
                                     E.escreve(c, "= 1 cm³", x + 220, 770, 60, "g", COR, a)))
    E.foco(c, t, d3, 0.5, lambda a: cubinhos(c, x + 500, 650, 6, 34, a))
    E.foco(c, t, d3 + 0.3, 0.5, lambda a: E.escreve(c, "mil cubinhos = 1 L", x + 440, 900, 44, "i", TINTA, a))
    E.frase(c, t, lerp(d3, e3, 0.6), ps("faltou alguma?", "i", 50, COR) + ps("procure no canal", "i", 50, TINTA2), x, 1010, "left", 0.1)


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, C["s04"] + 0.1, [("densidade", "g", 110, COR)], W / 2, 210, "center")
    E.frase(c, t, a4, ps("quanta massa cabe em", "i", 70) + [("cada pedacinho de volume", "g", 70)], W / 2, 330, "center", 0.1)
    # balança e caixa
    E.foco(c, t, b4, 0.5, lambda a: (M.rrect(c, 400, 640, 400, 40, 12, TINTA, a), M.rrect(c, 560, 680, 80, 120, 10, TINTA, a),
                                     M.rrect(c, 380, 800, 440, 40, 12, TINTA, a), M.rrect(c, 520, 520, 160, 120, 14, E.COR, a)))
    E.foco(c, t, b4 + 0.3, 0.5, lambda a: (centro(c, "massa", 600, 920, 80, "g", TINTA, a), centro(c, "o que a balança marca: g ou kg", 600, 990, 44, "i", TINTA2, a)))
    E.foco(c, t, c4, 0.5, lambda a: cubinhos(c, 1200, 520, 7, 40, a))
    E.foco(c, t, c4 + 0.3, 0.5, lambda a: (centro(c, "volume", 1340, 920, 80, "g", COR, a), centro(c, "o espaço que ocupa", 1340, 990, 44, "i", TINTA2, a)))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    fcen(c, t, a5, "d = f{m}{V}", W / 2, 400, 220, COR)
    for i, (l, pal, cor) in enumerate((("d", "densidade", COR), ("m", "massa", TINTA), ("V", "volume", TINTA))):
        E.foco(c, t, b5 + i * 0.5, 0.5, lambda a, i=i, l=l, pal=pal, cor=cor: (centro(c, l, 520 + i * 440, 650, 96, "g", cor, a),
                                                                               centro(c, pal, 520 + i * 440, 730, 54, "i", TINTA, a)))
    E.frase(c, t, c5 - 0.6, [("g e cm³", "g", 60, TINTA2)] + ps("dão", "i", 64, TINTA2), W / 2 - 230, 900, "center", 0.1)
    E.foco(c, t, c5, 0.5, lambda a: E.pilula(c, "g/cm³", W / 2 + 220, 880, 72, "g", a=a))


# ---------------- exemplos ----------------
def b_exemplos(c, t, C, b):
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]

    def madeira():
        E.frase(c, t, C["s06"] + 0.2, ps("bloco de", "i", 76) + [("madeira", "g", 80, COR)], W / 2, 200, "center", 0.12)
        fcen(c, t, a6, "m = 600 g", 620, 400, 96)
        fcen(c, t, b6, "V = 1.000 cm³", 1300, 400, 96)
        fcen(c, t, c6, "d = f{600}{1.000} = 0,6 g/cm³", W / 2, 680, 110, COR)
    E.saida(c, t, C["s07"] - 0.1, madeira)
    if t < C["s07"]:
        return
    a7, b7, c7, d7, e7 = (C[f"s07.{k}"] for k in "abcde")
    E.frase(c, t, C["s07"] + 0.2, ps("uma", "i", 76) + [("pedra", "g", 80)], W / 2, 170, "center", 0.12)
    fcen(c, t, a7, "m = 150 g", 620, 320, 90)
    fcen(c, t, b7, "V = 60 cm³", 1300, 320, 90)
    fcen(c, t, c7, "d = f{150}{60} = 2,5 g/cm³", W / 2, 540, 100, TINTA)
    E.frase(c, t, d7 - 1.2, ps("isolando a massa:", "i", 60, TINTA2), W / 2, 720, "center", 0.1)
    fcen(c, t, d7, "m = d × V", W / 2, 830, 96, COR)
    fcen(c, t, e7, "2,5 × 200 = 500 g", W / 2, 990, 96, COR)


# ---------------- a água ----------------
def b_agua(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    E.frase(c, t, C["s08"] + 0.2, ps("e a", "i", 80) + [("água?", "g", 84, COR)], W / 2, 180, "center", 0.12)
    E.foco(c, t, a8, 0.5, lambda a: (M.rrect(c, 300, 340, 360, 460, 30, AGUA, a), c.drawRRect(
        skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(300, 340, 360, 460), 30, 30), M.paint(TINTA, a, stroke=5)), centro(c, "1 L", 480, 600, 96, "g", COR, a)))
    fcen(c, t, a8 + 0.4, "1 kg = 1.000 g", 1180, 420, 90)
    fcen(c, t, b8, "em 1.000 cm³", 1180, 560, 90)
    fcen(c, t, c8, "d = 1 g/cm³", 1180, 760, 120, COR)


# ---------------- boia ou afunda ----------------
def b_boia(c, t, C, b):
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    E.linha(c, t, [("menor que 1:", "i", 72, TINTA, a9), ("boia", "g", 80, COR, a9 + 0.5)], 560, 200, "center")
    E.linha(c, t, [("maior que 1:", "i", 72, TINTA, b9), ("afunda", "g", 80, TINTA, b9 + 0.4)], 1360, 200, "center")
    objs = [(700, 300, 120, E.COR, "0,6", c9 - 0.3, True), (1260, 220, 120, TINTA, "2,5", d9 - 0.6, False)]
    tanque(c, t, 340, 300, 1240, 640, objs, ep(t, C["s09"], 0.5))
    E.foco(c, t, c9 + 0.6, 0.5, lambda a: centro(c, "madeira", 700, 410 - 20, 50, "i", COR, a))
    E.foco(c, t, d9 + 0.3, 0.4, lambda a: centro(c, "pedra", 1260, 790, 50, "i", TINTA, a))


# ---------------- do material ----------------
def b_material(c, t, C, b):
    a0, b0, c0, e0 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.end"]
    E.frase(c, t, a0, ps("a densidade é", "i", 72) + [("do material,", "g", 76, COR)] + ps("não do tamanho", "i", 72), W / 2, 200, "center", 0.1)
    E.foco(c, t, lerp(a0, b0, 0.5), 0.5, lambda a: M.rrect(c, 360, 380, 180, 180, 14, E.COR, a))
    E.foco(c, t, lerp(a0, b0, 0.6), 0.5, lambda a: M.rrect(c, 640, 380, 360, 180, 14, E.COR, a))
    E.foco(c, t, lerp(a0, b0, 0.7), 0.5, lambda a: (centro(c, "1×", 450, 620, 52, "i", TINTA, a), centro(c, "2× o tamanho", 820, 620, 52, "i", TINTA, a)))
    fcen(c, t, b0, "f{1.200 g}{2.000 cm³}", 1400, 470, 80)
    fcen(c, t, c0, "= 0,6 g/cm³ de novo", W / 2, 800, 100, COR)
    E.frase(c, t, lerp(c0, e0, 0.4), ps("grande ou pequeno,", "i", 66, TINTA2) + [("boia", "g", 70, COR)], W / 2, 950, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1, e1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.end"]

    def tronco():
        E.frase(c, t, C["s11"] + 0.2, ps("o erro:", "i", 80) + [("o mais pesado afunda", "g", 84, ERRADO)], W / 2, 180, "center", 0.12)
        E.foco(c, t, a1 + 0.6, 0.5, lambda a: E.selo(c, 1680, 150, 44, False, a))
        fcen(c, t, b1 - 0.6, "tronco: 300 kg em 500 L", W / 2, 360, 90)
        fcen(c, t, c1, "f{300}{500} = 0,6 kg/L", W / 2, 560, 110, COR)
        fcen(c, t, d1, "água: 1 kg/L", W / 2, 760, 96)
        E.frase(c, t, lerp(d1, e1, 0.4), ps("0,6 < 1:", "g", 72) + ps("boia, mesmo pesado", "i", 72, COR), W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s12"] - 0.1, tronco)
    if t < C["s12"]:
        return
    a2, b2 = C["s12.a"], C["s12.b"]
    E.frase(c, t, C["s12"] + 0.2, ps("o clipe é leve, mas é de", "i", 76) + [("aço", "g", 80)], W / 2, 260, "center", 0.12)
    E.frase(c, t, a2, [("bem mais denso", "g", 84)] + ps("que a água: afunda", "i", 76), W / 2, 450, "center", 0.12)
    E.foco(c, t, b2, 0.5, lambda a: E.selo(c, 360, 690, 50, False, a))
    E.frase(c, t, b2 + 0.1, ps("não compare", "i", 80) + [("pesos", "g", 84, ERRADO)], 450, 715, "left", 0.1)
    E.foco(c, t, b2 + 0.8, 0.5, lambda a: E.selo(c, 360, 870, 50, True, a))
    E.frase(c, t, b2 + 0.9, ps("compare", "i", 80) + [("densidades", "g", 84, CERTO)], 450, 895, "left", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3, e3, f3 = (C[f"s13.{k}"] for k in "abcdef")

    def compara():
        E.frase(c, t, C["s13"] + 0.1, ps("agora, o atalho:", "i", 66, CLARO) + [("g e cm³", "g", 70, BR)], W / 2, 160, "center", 0.12)
        E.frase(c, t, b3, [("compare os números", "g", 92, BR)], W / 2, 300, "center")
        E.linha(c, t, [("massa", "g", 76, BR, c3), ("<", "g", 76, CLARO, c3 + 0.2), ("volume:", "g", 76, BR, c3 + 0.3), ("boia", "g", 80, CLARO, c3 + 0.6)],
               W / 2, 460, "center")
        E.linha(c, t, [("massa", "g", 76, BR, d3), (">", "g", 76, CLARO, d3 + 0.2), ("volume:", "g", 76, BR, d3 + 0.3), ("afunda", "g", 80, CLARO, d3 + 0.6)],
               W / 2, 590, "center")
        fcen(c, t, e3 - 0.8, "600 g em 1.000 cm³", W / 2, 760, 90, BR)
        E.frase(c, t, e3, [("600 < 1.000:", "g", 72, BR)] + ps("boia", "i", 76, CLARO), W / 2, 870, "center", 0.12)
        E.frase(c, t, f3, ps("vale também com", "i", 64, CLARO) + [("kg e L", "g", 68, BR)], W / 2, 1000, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, compara)
    if t < C["s14"]:
        return
    a4, b4, c4, d4 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, a4, ps("a água tem", "i", 72, CLARO) + [("densidade 1", "g", 76, BR)], W / 2, 190, "center", 0.12)
    fcen(c, t, b4 - 0.6, "f{m}{V} > 1  quando  m > V", W / 2, 360, 96, BR)
    E.foco(c, t, c4, 0.5, lambda a: E.selo(c, 330, 590, 50, False, a))
    E.frase(c, t, c4 + 0.1, ps("outro líquido, como o", "i", 66, CLARO) + [("óleo", "g", 70, BR)], 420, 615, "left", 0.1)
    E.frase(c, t, lerp(c4, d4, 0.5), ps("unidades misturadas:", "i", 66, CLARO) + [("kg e cm³", "g", 70, BR)], 420, 740, "left", 0.1)
    E.frase(c, t, d4, ps("converta antes:", "i", 70, CLARO) + [("g e cm³, ou kg e L", "g", 74, BR)], W / 2, 920, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a5, b5, c5, d5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a5, ps("bola:", "i", 80) + [("450 g", "g", 88, COR)] + ps("em", "i", 80) + [("500 cm³", "g", 88, COR)], XE, 360, passo=0.12)
    E.frase(c, t, b5, ps("metal:", "i", 80) + [("270 g", "g", 88)] + ps("em", "i", 80) + [("100 cm³", "g", 88)], XE, 500, passo=0.12)
    E.frase(c, t, c5, ps("a densidade de", "i", 80) + [("cada uma?", "g", 84, COR)], XE, 680, passo=0.12)
    E.frase(c, t, d5, [("quem boia?", "g", 100, COR)], XE, 840, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1590, 430, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    a8, b8 = C["s18.a"], C["s18.b"]
    objs = [(1460, 200, 110, E.COR, "bola", b7, True), (1680, 180, 100, TINTA, "metal", b8, False)]
    tanque(c, t, 1300, 330, 520, 560, objs, ep(t, C["s17"], 0.5))
    fcen(c, t, a7, "bola: f{450}{500} = 0,9 g/cm³", 640, 330, 76, COR)
    E.frase(c, t, b7, ps("menor que 1:", "i", 66) + [("boia", "g", 70, COR)], 640, 450, "center", 0.1)
    E.frase(c, t, c7, ps("atalho:", "i", 56, TINTA2) + [("450 < 500", "g", 60)], 640, 540, "center", 0.1)
    fcen(c, t, a8, "metal: f{270}{100} = 2,7 g/cm³", 640, 720, 76)
    E.frase(c, t, b8, ps("maior que 1:", "i", 66) + [("afunda", "g", 70)], 640, 840, "center", 0.1)
    E.frase(c, t, lerp(b8, C["s18.end"], 0.5), ps("só a", "i", 70) + [("bola boia", "g", 76, CERTO)], 640, 970, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s19.a", "densidade =", "massa ÷ volume"), ("s19.b", "é do material,", "não do tamanho"), ("s19.c", "menor que a da água:", "boia"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72) + [(l2, "g", 74, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 84), XE, 220, passo=0.14)
    E.frase(c, t, a0, [("vazão", "g", 140, COR)], XE, 380, passo=0.12)
    E.frase(c, t, lerp(a0, b0, 0.4), ps("litros por minuto", "i", 70), XE, 490, passo=0.1)
    E.frase(c, t, b0, ps("o tempo para", "i", 70) + [("encher uma caixa", "g", 70)], XE, 590, passo=0.1)
    E.frase(c, t, c0, [("duas torneiras", "g", 70, COR)] + ps("juntas", "i", 70), XE, 690, passo=0.1)
    E.foco(c, t, d0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d0 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1020, 815, p), ep(t, d0 + 0.2, 0.4))
    E.frase(c, t, e0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, formula=b_formula, exemplos=b_exemplos, agua=b_agua, boia=b_boia,
              material=b_material, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
