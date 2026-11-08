"""Visual — Estudativo · MAT-TOP-007: distância de ponto a reta. Abre o módulo "Distância de ponto a reta e área por determinante".

Herda a linguagem da Geometria Analítica (MAT-ANA-001): plano na metade direita, texto na esquerda, eixo x em índigo,
pontos em tinta com nome, escala igual nos dois eixos (a figura não mente), resposta na esfera.
Cores desta aula: a reta em tinta; a distância (o segmento perpendicular) em índigo; o caminho "descendo reto" e os outros
caminhos, mais longos, em âmbar tracejado. Na fórmula, o número de cima (o ponto trocado na reta) em índigo e o de baixo
(a raiz de a² + b²) em petróleo.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-007_distancia_de_ponto_a_reta.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("caminho", "formula", "sentido", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMB, PET = "#D98A00", "#0E9AA7"
d_ = lambda a, b, c, x, y: abs(a * x + b * y + c) / math.hypot(a, b)
assert d_(3, 4, -1, 1, 2) == 2 and 3 * 1 + 4 * 2 - 1 == 10 and math.hypot(3, 4) == 5
assert abs(3 * -0.2 + 4 * 0.4 - 1) < 1e-12 and 2 - (1 - 3 * 1) / 4 == 2.5          # pé da perpendicular e "descer reto"
assert math.hypot(1 - (-1), 2 - 1) > 2 and 3 * -1 + 4 * 1 - 1 == 0                    # outro caminho (até (−1, 1)) é mais longo
assert d_(0, 1, -3, 1, 7) == 4
assert abs(-1 - 9) / 5 == 2 and d_(3, 4, 9, -1, 1) == 2                               # paralelas: (−1, 1) está na primeira
assert 2 * 0 + 3 == 3 and abs(2 * 0 + 1 * 3 + 3) == 6 and 2 * 0 - 3 + 3 == 0
assert d_(5, 12, 15, 2, -1) == 1 and 10 - 12 + 15 == 13 and 25 + 144 == 169 == 13 ** 2

PG = E.Plano(1040, 150, 770, 660, -3, 4, -2, 4)   # gancho: P(1, 2) e 3x + 4y − 1 = 0
PH = E.Plano(1150, 120, 560, 800, -1, 6, -1, 9)   # reta deitada y = 3 e o ponto (1, 7)
P0, F0, V0, Q0 = (1, 2), (-0.2, 0.4), (1, -0.5), (-1, 1)
RA, RB = (-1, 1), (3, -2)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da geometria analítica (como na MAT-ANA-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def plano(c, t, t0, P, size=38, escuro=False):
    E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, size=size, nomes=("", "y"), escuro=escuro)
    if t >= t0:
        x, y, w, h = P.caixa
        p = ep(t, t0, 0.6)
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, COR if not escuro else CLARO, 1.0, 6, 24, p)
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 26, P.oy + 62, 58, "i", COR if not escuro else CLARO, a))


def nome(c, t, t0, P, x, y, s, lado=(1, -1), size=46, r=15, cor=TINTA):
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=r)
    if s:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, s, *P(x, y), lado[0], lado[1], r + 8, size, "b", cor, a))


def seg(c, t, t0, P, A, B, cor, largura=8, tracejado=False, d=0.7, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor, a, largura, dash=E.TRACO if tracejado else None, progress=p)


def canto(c, t, t0, P, V, A, B, cor=TINTA):
    E.angulo(c, t, t0, P(*V), P(*A), P(*B), r=40, cor=cor, preenche=0.12)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, str(s), cx, cy + size * 0.36, size, "g", BR, a, "center")))


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


def txt_em(c, t, t0, s, x, y, size, cor=TINTA, est="g", align="left"):
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, s, x, y, size, est, cor, a, align))


def formula_d(c, x, y, size, a=1.0, cor_c=None, cor_b=None, escuro=False):
    """d = |a·xP + b·yP + c| / raiz(a² + b²), com o de cima em índigo e o de baixo em petróleo"""
    tinta = BR if escuro else TINTA
    E.formula(c, "d =", x, y, size, "g", tinta, a)
    x1 = x + E.formula(None, "d =", 0, 0, size, "g", a=0) + size * 0.2
    cima, baixo = "|a·xₚ + b·yₚ + c|", "r{a^2 + b^2}"
    wc = E.formula(None, cima, 0, 0, size * 0.8, "g", a=0)
    wb = E.formula(None, baixo, 0, 0, size * 0.8, "g", a=0)
    w = max(wc, wb) + size * 0.2
    E.formula(c, cima, x1 + (w - wc) / 2, y - size * 0.42, size * 0.8, "g", cor_c or (CLARO if escuro else COR), a)
    E.formula(c, baixo, x1 + (w - wb) / 2, y + size * 0.62, size * 0.8, "g", cor_b or PET, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x1, y - size * 0.3 - 3, w, 7), 3, 3), M.paint(tinta, a))


def figura(c, t, tp, tr, tv=None, tf=None, tq=None, a_v=1.0):
    """o plano do gancho: ponto P, reta, descer reto (tv) e a perpendicular (tf); tq = outro caminho"""
    plano(c, t, tp, PG)
    E.reta_pontos(c, t, tr, PG, RA, RB, cor=TINTA, largura=6, pontos=False)
    E.foco(c, t, tr + 0.5, 0.4, lambda a: E.escreve(c, "estrada", PG.x(2.2), PG.y(-1.6) + 50, 40, "i", TINTA2, a))
    nome(c, t, tp + 0.3, PG, *P0, "casa", (1, -1))
    if tv is not None and a_v > 0:
        seg(c, t, tv, PG, P0, V0, AMB, 6, True, a=a_v)
        E.foco(c, t, tv + 0.6, 0.4, lambda a: E.escreve(c, "2,5", PG.x(1) + 18, PG.y(0.6), 46, "g", AMB, a * a_v))
    if tf is not None:
        seg(c, t, tf, PG, P0, F0, COR, 9)
        canto(c, t, tf + 0.6, PG, F0, P0, RA)
        E.foco(c, t, tf + 0.6, 0.4, lambda a: E.escreve(c, "2", PG.x(0.1) - 70, PG.y(1.3), 54, "g", COR, a))
    if tq is not None:
        seg(c, t, tq, PG, P0, Q0, AMB, 6, True)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        figura(c, t, C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"])
        E.foco(c, t, C["s01.a"], 0.4, lambda a: E.formula(c, "casa (1, 2)", XE, 300, 76, "g", TINTA, a))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.formula(c, "3x + 4y − 1 = 0", XE, 440, 76, "g", TINTA, a))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "na vertical: 2,5", XE, 600, 64, "i", AMB, a))
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "mais curto: 2", XE, 720, 76, "g", COR, a))
        E.foco(c, t, C["s01.e"], 0.4, lambda a: E.pilula(c, "uma fórmula", 420, 880, 60, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 560, 270 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 0.9, [("distância", "g", 120, COR)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.4, [("de", "i", 110), ("ponto", "g", 120)], XE, 630)
        E.frase(c, t, C["s02.a"] + 1.9, [("a", "i", 110), ("reta", "g", 120, COR)], XE, 780)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1300, 545, 80, "g", BR, a),
                                                      E.escreve(c, "de prova", 1320, 630, 80, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 84), XE, 190)
    E.frase(c, t, C["s03.a"], [("3", "g", 110, COR), ("coisas", "i", 100)], XE + 640, 190)
    itens = (("s03.b", "equação geral", "ax + by + c = 0"), ("s03.c", "perpendiculares", "cruzam em ângulo reto"), ("s03.d", "módulo", "|−7| = 7"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 245
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, XE, y, 1580, 200, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 64, COR)], XE + 50, y + 125)
        txt_em(c, t, C[k] + 0.5, l2, XE + 700, y + 125, 64, TINTA, "g" if "=" in l2 else "i")


# ---------------- o menor caminho ----------------
def b_caminho(c, t, C, b):
    figura(c, t, C["s04"], C["s04"] + 0.2, None, C["s04.b"], C["s04.c"])
    E.frase(c, t, C["s04.a"], [("o", "i", 70), ("menor", "g", 70, COR), ("caminho", "i", 70)], XE, 300)
    E.frase(c, t, C["s04.b"], [("chega", "i", 64), ("em", "i", 64), ("ângulo", "g", 62), ("reto", "g", 62)], XE, 440)
    if t >= C["s04.c"]:
        q = ep(t, C["s04.c"] + 0.6, 0.5)
        path = skia.Path()
        path.addPoly([PG(*P0), PG(*F0), PG(*Q0)], True)
        c.drawPath(path, M.paint(AMB, 0.12 * q))
        E.foco(c, t, C["s04.c"] + 0.6, 0.4, lambda a: E.escreve(c, "hipotenusa", PG.x(-1.6) - 120, PG.y(1.9), 40, "b", AMB, a))
    E.frase(c, t, C["s04.c"], ps("outro caminho: hipotenusa", "i", 60, AMB), XE, 620)
    E.frase(c, t, C["s04.d"], [("hipotenusa", "i", 60), (">", "g", 60), ("cateto", "g", 60, COR)], XE, 760)


# ---------------- fórmula ----------------
def b_formula(c, t, C, b):
    def parte1():
        E.foco(c, t, C["s05.a"], 0.5, lambda a: E.formula(c, "reta: ax + by + c = 0", XE, 230, 76, "g", TINTA, a))
        E.foco(c, t, C["s05.a"] + 0.8, 0.4, lambda a: E.formula(c, "ponto: P = (xₚ, yₚ)", 1050, 230, 64, "g", TINTA2, a))
        E.foco(c, t, C["s05.b"], 0.5, lambda a: formula_d(c, 300, 560, 130, a))
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: E.escreve(c, "o ponto na reta", 1330, 500, 56, "i", COR, a))
        E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "| | tira o sinal: distância nunca é negativa", 860, 900, 52, "g", fundo=COR, a=a))
        E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "a escala", 1330, 720, 56, "i", PET, a))
    E.saida(c, t, C["s06"] - 0.1, parte1)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06"], 0.4, lambda a: E.formula(c, "3x + 4y − 1 = 0   e   (1, 2)", XE, 200, 70, "g", TINTA, a))
    E.foco(c, t, C["s06.a"], 0.4, lambda a: E.escreve(c, "a = 3   b = 4   c = −1", XE, 310, 60, "b", TINTA2, a))
    conta_em(c, t, C["s06.b"], [("|3·1 + 4·2 − 1|", COR)], XE, 470, 80)
    conta_em(c, t, C["s06.c"], [("= |3 + 8 − 1| = 10", COR)], XE + 580, 470, 80)
    conta_em(c, t, C["s06.d"], [("r{3^2 + 4^2} = r{25} = 5", PET)], XE, 680, 80)
    conta_em(c, t, C["s06.e"], [("d = ", TINTA), ("f{10}{5}", TINTA), (" = 2", CERTO)], XE, 900, 100)
    bola_txt(c, t, C["s06.e"] + 0.5, "2", 1300, 860, 100, 120, CERTO)


# ---------------- sentido da fórmula ----------------
def b_sentido(c, t, C, b):
    def parte1():
        E.frase(c, t, C["s07"], ps("teste:", "i", 70), XE, 200)
        E.foco(c, t, C["s07.a"], 0.4, lambda a: E.escreve(c, "ponto na reta (−1, 1):", XE, 340, 58, "i", TINTA, a))
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.formula(c, "|3·(−1) + 4·1 − 1| = 0", XE, 450, 72, "g", COR, a))
        E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.escreve(c, "d = 0", XE + 920, 450, 72, "g", CERTO, a))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: E.escreve(c, "mais longe da reta: número de cima maior", XE, 650, 58, "i", TINTA, a))
        E.foco(c, t, C["s07.d"], 0.4, lambda a: E.escreve(c, "o de baixo acerta a escala", XE, 820, 58, "g", PET, a))
    E.saida(c, t, C["s08"] - 0.1, parte1)
    if t < C["s08"]:
        return
    plano(c, t, C["s08"], PH)
    E.reta_pontos(c, t, C["s08.a"], PH, (-1, 3), (6, 3), cor=TINTA, largura=6, pontos=False)
    E.foco(c, t, C["s08.a"], 0.4, lambda a: E.formula(c, "y = 3", XE, 220, 80, "g", TINTA, a))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.formula(c, "0x + 1y − 3 = 0", XE, 340, 72, "g", TINTA, a))
    E.foco(c, t, C["s08.b"] + 0.6, 0.4, lambda a: E.escreve(c, "a = 0   b = 1   c = −3", XE, 430, 52, "b", TINTA2, a))
    nome(c, t, C["s08.c"], PH, 1, 7, "(1, 7)", (1, -1))
    conta_em(c, t, C["s08.c"] + 0.5, [("|7 − 3| = 4", COR)], XE, 580, 76)
    conta_em(c, t, C["s08.d"], [("r{0 + 1} = 1", PET)], XE, 720, 76)
    seg(c, t, C["s08.e"], PH, (1, 7), (1, 3), COR, 9)
    for k in range(4):
        E.foco(c, t, C["s08.e"] + 0.3 + k * 0.2, 0.3, lambda a, k=k: E.escreve(c, str(k + 1), PH.x(1) + 20, PH.y(6.5 - k) + 16, 40, "g", COR, a))
    bola_txt(c, t, C["s08.e"], "4", 520, 900, 80, 100, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], XE, 200)
    E.frase(c, t, C["s09.a"], ps("fora da equação geral", "i", 70, ERRADO), 1000, 200)
    txt_em(c, t, C["s09.b"], "y = 2x + 3", XE, 400, 110)
    E.foco(c, t, C["s09.b"] + 1.0, 0.4, lambda a: E.escreve(c, "a = 2?  b = 1?  c = 3?", 900, 400, 70, "g", ERRADO, a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.formula(c, "(0, 3): |2·0 + 1·3 + 3| = 6 ≠ 0", XE, 540, 64, "g", ERRADO, a))
    if t >= C["s09.d"]:
        E.risco(c, 890, 420, 1650, 330, t, C["s09.d"] - 0.3, largura=10)
        q = ep(t, C["s09.d"] - 0.3, 0.4)
        c.drawCircle(XE + 28, 362, 62, M.paint(ERRADO, q, stroke=6))
    txt_em(c, t, C["s09.d"], "2x − y + 3 = 0", XE, 700, 100, CERTO)
    E.foco(c, t, C["s09.e"], 0.4, lambda a: E.escreve(c, "a = 2   b = −1   c = 3", XE, 840, 70, "g", CERTO, a))
    E.foco(c, t, C["s09.e"] + 1.6, 0.4, lambda a: E.formula(c, "(0, 3): |2·0 − 3 + 3| = 0", XE, 970, 64, "g", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parte1():
        E.frase(c, t, C["s10.a"], [("atalho:", "i", 76, CLARO), ("retas", "g", 72, BR), ("paralelas", "g", 72, BR)], W / 2, 180, "center")
        txt_em(c, t, C["s10.b"], "3x + 4y − 1 = 0", XE, 360, 84, BR)
        txt_em(c, t, C["s10.c"], "3x + 4y + 9 = 0", XE, 490, 84, BR)
        E.foco(c, t, C["s10.b"] + 0.5, 0.4, lambda a: E.escreve(c, "c = −1", 1000, 360, 70, "g", CLARO, a))
        E.foco(c, t, C["s10.c"] + 0.5, 0.4, lambda a: E.escreve(c, "c = 9", 1000, 490, 70, "g", CLARO, a))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "d = f{|c₁ − c₂|}{r{a^2 + b^2}}", 1200, 470, 110, "g", BR, a))
        txt_em(c, t, C["s10.e"], "|−1 − 9| = 10", XE, 720, 90, CLARO)
        E.foco(c, t, C["s10.f"], 0.5, lambda a: E.pilula(c, "10 ÷ 5 = 2", 1300, 690, 76, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s11"] - 0.1, parte1)
    if t < C["s11"]:
        return
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.formula(c, "na 1ª reta: 3x + 4y = 1", XE, 280, 80, "g", BR, a))
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.formula(c, "na conta da 2ª: 1 + 9 = 10", XE, 420, 80, "g", CLARO, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "só com a e b iguais nas duas", W / 2, 620, 60, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "6x + 8y + ...  →  ÷ 2  →  3x + 4y + ...", W / 2, 840, 70, "g", BR, a, "center"))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s12.a"], [("ponto", "i", 84)], XE, 420)
    txt_em(c, t, C["s12.a"] + 0.3, "(2, −1)", XE + 260, 420, 100, COR)
    E.frase(c, t, C["s12.b"], [("reta", "i", 84)], XE, 620)
    txt_em(c, t, C["s12.b"] + 0.3, "5x + 12y + 15 = 0", XE + 220, 620, 90, TINTA)
    E.frase(c, t, C["s12.b"] + 1.4, [("distância", "i", 84), ("=", "g", 84), ("?", "g", 84, COR)], XE, 820)
    E.relogio(c, t, C["s13.a"], 1560, 360, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    conta_em(c, t, C["s14.a"], [("|5·2 + 12·(−1) + 15|", COR)], XE, 260, 84)
    conta_em(c, t, C["s14.b"], [("= |10 − 12 + 15| = 13", COR)], XE, 400, 84)
    conta_em(c, t, C["s14.c"], [("r{25 + 144} = r{169} = 13", PET)], XE, 600, 84)
    conta_em(c, t, C["s14.d"], [("d = ", TINTA), ("f{13}{13}", TINTA), (" = 1", CERTO)], XE, 840, 100)
    bola_txt(c, t, C["s14.d"] + 0.5, "1", 1350, 800, 110, 130, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s15"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        for i, (k, s, cor) in enumerate((("s15.a", "reta na equação geral", TINTA), ("s15.b", "em cima: o ponto, em módulo", COR),
                                         ("s15.c", "embaixo: raiz de a² + b²", PET))):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 86, cor)], 400, y)
    E.saida(c, t, C["s16"] - 0.1, resumo)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s16.a"], [("3", "g", 130, COR), ("pontos", "g", 130)], XE, 470)
    E.frase(c, t, C["s16.a"] + 0.4, [("alinhados?", "g", 130, COR)], XE, 620)
    E.frase(c, t, C["s16.b"], ps("pelo determinante", "i", 70), XE, 770)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s16.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s16.c"] + 0.2, 0.4))
    E.frase(c, t, C["s16.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, caminho=b_caminho, formula=b_formula, sentido=b_sentido, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
