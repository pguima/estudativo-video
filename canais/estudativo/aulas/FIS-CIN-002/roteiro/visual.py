"""Visual — Estudativo · FIS-CIN-002: vetores, somar e subtrair.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: as parcelas (velocidades) em petróleo (F.VEL) e a RESULTANTE, a grandeza da vez, em laranja (E.COR), sempre com a
letra R. "Ponta com começo": o segundo vetor desliza até encostar o começo na ponta do primeiro (peca desliza()).
Rio = faixa azul-clara com as margens em azul; barco e drone desenhados aqui (barco(), drone()).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-002_vetores_somar_e_subtrair.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("resultante", "fila", "reto", "subtrair", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AGUA, MARGEM = "#7FC8E8", "#3B8DB5"

# todas as contas da aula
assert math.isqrt(3 ** 2 + 4 ** 2) == 5 and 3 ** 2 + 4 ** 2 == 25 and 9 + 16 == 25 and 4 + 3 == 7 and 4 - 3 == 1
assert 2 + 1 == 3 and 2 - 1 == 1 and (+2) + (-1) == +1 and (-5) + (-5) == -10 and (-5) - (+5) == -10
assert 1 <= 5 <= 7 and 6 ** 2 + 8 ** 2 == 100 and math.isqrt(100) == 10 and 1 ** 2 + 2 ** 2 == 5
assert 5 ** 2 + 12 ** 2 == 169 and 25 + 144 == 169 and math.isqrt(169) == 13 and 12 - 5 == 7


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais (copiadas entre as aulas FIS-CIN) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete(c, t, C, cena, itens, desenhos=None):
    """'você precisa de N coisas': itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita de cada caixa"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    h, gap, s1 = (230, 290, 58) if n == 2 else (196, 236, 52)
    y0 = 520 - (h + gap * (n - 1)) / 2
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s1, COR)], x + 44, y + h * 0.74)
        if desenhos:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 150, y + h / 2))
    ult = itens[-1][0]
    E.frase(c, t, lerp(C[ult], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 990, "left", 0.12)


def promessa(c, t, C, cena, itens, titulo="até o fim da aula"):
    """gancho: a órbita à direita e a lista numerada; itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps(titulo, "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a),
                                                        centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def fim_inscreva(c, t, C, cena, k_insc, k_bons):
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def resumo(c, t, C, cena, itens):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 190
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


# ---------------- peças desta aula ----------------
def rio(c, x0, x1, y0, y1, a=1.0):
    """faixa de água com as duas margens e ondinhas"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x0, y0, x1, y1), M.paint(AGUA, 0.32 * a))
    for yy in (y0, y1):
        M.line(c, x0, yy, x1, yy, MARGEM, a, 6)
    for k in range(4):
        yy = y0 + (y1 - y0) * (k + 0.5) / 4
        for j in range(5):
            xx = x0 + 60 + j * (x1 - x0 - 120) / 4
            M.line(c, xx, yy, xx + 40, yy, MARGEM, 0.35 * a, 4)


def barco(c, x, y, s=60, a=1.0):
    """barquinho visto de cima, apontando para cima; (x, y) = centro"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y - s); p.quadTo(x + s * 0.55, y - s * 0.2, x + s * 0.42, y + s * 0.7)
    p.lineTo(x - s * 0.42, y + s * 0.7); p.quadTo(x - s * 0.55, y - s * 0.2, x, y - s); p.close()
    c.drawPath(p, M.paint("#8B5E3C", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))
    M.line(c, x - s * 0.3, y + s * 0.2, x + s * 0.3, y + s * 0.2, "#6E4A2F", a, 5)


def drone(c, x, y, s=50, a=1.0):
    """drone visto de cima: corpo e quatro hélices"""
    if a <= 0:
        return
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        M.line(c, x, y, x + dx * s, y + dy * s, TINTA, a, 7)
        c.drawCircle(x + dx * s, y + dy * s, s * 0.42, M.paint(TINTA2, 0.25 * a))
        c.drawCircle(x + dx * s, y + dy * s, s * 0.42, M.paint(TINTA, a, stroke=4))
    M.rrect(c, x - s * 0.38, y - s * 0.38, s * 0.76, s * 0.76, 10, E.COR, a)


def desliza(t, t0, A, B, d=0.8):
    """posição de um ponto que vai de A até B a partir de t0"""
    q = ease_io(prog(t, t0, d))
    return (lerp(A[0], B[0], q), lerp(A[1], B[1], q))


def seta_em(c, t, t0, A, B, cor, largura=11, a=1.0):
    """seta já crescida (para vetores que deslizam); entra com foco em t0"""
    E.foco(c, t, t0, 0.4, lambda q: F.seta(c, *A, *B, cor, q * a, largura), blur=0)


def rot(c, s, x, y, size=52, cor=TINTA2, est="i", a=1.0, align="center"):
    if a <= 0:
        return
    if align == "center":
        centro(c, s, x, y, size, est, cor, a)
    else:
        E.escreve(c, s, x, y, size, est, cor, a)


def angulo_reto(c, P, ux, uy, vx, vy, k=34, a=1.0, cor=TINTA):
    """quadradinho de ângulo reto no vértice P, entre as direções u e v"""
    pts = [(P[0] + ux * k, P[1] + uy * k), (P[0] + ux * k + vx * k, P[1] + uy * k + vy * k), (P[0] + vx * k, P[1] + vy * k)]
    F.poli(c, pts, 1.0, cor, a, 4)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        X0, X1, Y0, Y1 = 980, 1800, 300, 860
        u = 120
        O = (1170, 820)
        E.foco(c, t, C["s01.a"], 0.6, lambda a: rio(c, X0, X1, Y0, Y1, a), blur=0)
        E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: rot(c, "outra margem", 1600, Y0 - 24, 40, MARGEM, a=a))
        # o barco anda pela diagonal depois da resposta
        q = ease_io(prog(t, C["s01.e"] + 0.6, 2.4))
        bx, by = lerp(O[0], O[0] + 3 * u, q), lerp(O[1], O[1] - 4 * u, q)
        E.foco(c, t, C["s01.a"] + 0.2, 0.5, lambda a: barco(c, bx, by, 52, a))
        F.vetor(c, t, C["s01.a"] + 0.6, O, (O[0], O[1] - 4 * u), None, "4 m/s", F.VEL, 11, size=56)
        F.vetor(c, t, C["s01.b"] + 0.3, O, (O[0] + 3 * u, O[1]), None, "3 m/s", F.VEL, 11, lado=-1, size=56)
        if t >= C["s01.e"]:
            M.line(c, *O, O[0] + 3 * u, O[1] - 4 * u, E.COR, 1.0, 9, dash=E.TRACO, progress=ease_io(prog(t, C["s01.e"], 0.6)))
        E.frase(c, t, C["s01.a"], [("barco", "i", 80)], XE, 300)
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: F.medida(c, 4, "m/s", XE + 250, 300, 96, TINTA, a))
        E.frase(c, t, C["s01.b"], [("correnteza", "i", 80)], XE, 430)
        E.foco(c, t, C["s01.b"] + 0.4, 0.5, lambda a: F.medida(c, 3, "m/s", XE + 400, 430, 96, TINTA, a))
        E.foco(c, t, C["s01.c"], 0.4, lambda a: E.escreve(c, "7?", XE, 680, 150, "g", ERRADO, a))
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.escreve(c, "1?", XE + 260, 680, 150, "g", ERRADO, a))
        if t >= C["s01.e"]:
            E.risco(c, XE - 10, 690, XE + 190, 560, t, C["s01.e"], largura=11)
            E.risco(c, XE + 250, 690, XE + 440, 560, t, C["s01.e"] + 0.15, largura=11)
        bola_txt(c, t, C["s01.e"] + 0.3, "5 m/s", XE + 240, 860, 125, 66)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.b", "mesmo sentido", 0), ("s02.c", "sentidos opostos", 0), ("s02.d", "ângulo reto", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def seta_p(a, x, y):
        F.seta(c, x - 90, y + 40, x + 70, y - 40, F.VEL, a, 9)

    def tri(a, x, y):
        A, B, D = (x - 80, y + 55), (x + 80, y + 55), (x - 80, y - 65)
        F.poli(c, [A, B, D, A], 1.0, TINTA, a, 5)
        E.escreve(c, "3", x - 30, y + 105, 40, "b", TINTA2, a); E.escreve(c, "4", x - 130, y + 10, 40, "b", TINTA2, a)
        E.escreve(c, "5", x + 10, y - 10, 40, "b", COR, a)
    lembrete(c, t, C, "s03", (("s03.b", "o vetor:", "módulo, direção, sentido"), ("s03.c", "Pitágoras,", "como o 3, 4, 5")), (seta_p, tri))


# ---------------- resultante ----------------
def b_resultante(c, t, C, b):
    E.frase(c, t, C["s04"], ps("dois vetores juntos", "i", 76), XE, 250, passo=0.12)
    E.frase(c, t, C["s04.a"], [("=", "g", 80, TINTA2), ("um", "g", 80), ("só", "g", 80)], XE, 360)
    E.frase(c, t, C["s04.b"], [("resultante", "g", 120, COR)], XE, 520)
    E.foco(c, t, C["s04.b"] + 0.3, 0.4, lambda a: E.escreve(c, "R", XE + 680, 520, 120, "g", COR, a))
    E.frase(c, t, C["s04.c"], [("ponta", "g", 64), ("com", "i", 68), ("começo", "g", 64)], XE, 700, passo=0.14)
    E.frase(c, t, C["s04.d"], ps("R vai do começo do 1º", "i", 54, TINTA2), XE, 820, passo=0.08)
    E.frase(c, t, C["s04.d"] + 0.6, ps("até a ponta do 2º", "i", 54, TINTA2), XE, 895, passo=0.08)
    A0, A1 = (1000, 760), (1380, 500)
    vb = (330, 170)
    B0 = (1240, 900)
    F.vetor(c, t, C["s04"] + 0.4, A0, A1, "a", None, F.VEL, 11, size=60)
    S = desliza(t, C["s04.c"] + 0.3, B0, A1, 1.0)
    seta_em(c, t, C["s04"] + 1.2, S, (S[0] + vb[0], S[1] + vb[1]), F.VEL)
    E.foco(c, t, C["s04"] + 1.2, 0.4, lambda a: F.letra_vetor(c, "b", S[0] + vb[0] / 2 + 40, S[1] + vb[1] / 2 + 80, 60, F.VEL, a))
    if t >= C["s04.c"] + 0.3:  # brilho na emenda
        q = ep(t, C["s04.c"] + 1.2, 0.3) * (1 - ep(t, C["s04.d"], 0.4))
        if q > 0:
            c.drawCircle(*A1, 34, M.paint(E.COR, q, stroke=5))
    F.vetor(c, t, C["s04.d"] + 0.2, A0, (A1[0] + vb[0], A1[1] + vb[1]), "R", None, E.COR, 12, 0.8, lado=-1, size=64)


# ---------------- mesmo sentido e opostos ----------------
U = 230  # pixels por m/s


def b_fila(c, t, C, b):
    x0 = 360

    def s05():
        E.frase(c, t, C["s05"], [("1.", "g", 76, COR), ("mesmo", "g", 76), ("sentido", "g", 76)], XE, 200)
        y = 470
        F.vetor(c, t, C["s05.b"], (x0, y), (x0 + 2 * U, y), None, "2 m/s", F.VEL, 12, size=56)
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: rot(c, "balsa", x0 + U, y + 80, 48, a=a))
        S = desliza(t, C["s05.d"], (x0, y + 200), (x0 + 2 * U, y), 0.8)
        seta_em(c, t, C["s05.c"], S, (S[0] + U, S[1]), F.VEL)
        E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: rot(c, "você 1 m/s", S[0] + U / 2, S[1] - 34, 46, a=a))
        F.vetor(c, t, C["s05.e"], (x0, y + 250), (x0 + 3 * U, y + 250), "R", "3 m/s", E.COR, 13, lado=-1, size=60)
        E.foco(c, t, C["s05.e"] + 0.6, 0.5, lambda a: E.formula(c, "2 + 1 = 3", 1500, 620, 110, "g", TINTA, a, "center"))
        pilula_em(c, t, C["s05.e"] + 1.0, "soma", 1500, 760, 52, E.COR)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06"], [("2.", "g", 76, COR), ("sentidos", "g", 76), ("opostos", "g", 76)], XE, 200)
            y = 520
            F.vetor(c, t, C["s06"] + 0.5, (x0, y), (x0 + 2 * U, y), None, "2 m/s", F.VEL, 12, lado=-1, size=56)
            E.foco(c, t, C["s06"] + 0.8, 0.4, lambda a: rot(c, "balsa", x0 + U, y + 130, 48, a=a))
            F.vetor(c, t, C["s06.c"], (x0 + 2 * U, y - 70), (x0 + U, y - 70), None, None, F.VEL, 12)
            E.foco(c, t, C["s06.b"], 0.4, lambda a: rot(c, "você, para trás, 1 m/s", x0 + 1.5 * U, y - 140, 46, a=a))
            F.vetor(c, t, C["s06.d"], (x0, y + 220), (x0 + U, y + 220), "R", "1 m/s", E.COR, 13, lado=-1, size=60)
            E.foco(c, t, C["s06.d"] + 0.4, 0.5, lambda a: E.formula(c, "2 − 1 = 1", 1500, 560, 110, "g", TINTA, a, "center"))
            pilula_em(c, t, C["s06.e"], "sentido do maior", 1500, 720, 52, E.COR)
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], ps("com", "i", 84) + [("sinais", "g", 84, COR)], W / 2, 220, "center")
    y = 470
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (F.seta(c, 1060, y, 1460, y, F.VEL, a, 11), E.escreve(c, "+", 1500, y + 30, 110, "g", F.VEL, a)))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: (F.seta(c, 860, y, 460, y, F.VEL, a, 11), E.escreve(c, "−", 360, y + 30, 110, "g", F.VEL, a)))
    E.foco(c, t, C["s07.b"] + 0.4, 0.4, lambda a: rot(c, "direita", 1260, y + 80, 48, a=a))
    E.foco(c, t, C["s07.c"] + 0.4, 0.4, lambda a: rot(c, "esquerda", 660, y + 80, 48, a=a))
    if t >= C["s07.b"]:
        c.drawCircle(960, y, 14, M.paint(TINTA, ep(t, C["s07.b"], 0.4)))
    E.formula_em(c, t, C["s07.d"], "(+2) + (−1) = ", W / 2 - 60, 760, 110, "g", TINTA, "right")
    E.formula_em(c, t, C["s07.d"] + 1.2, "+1", W / 2 - 40, 760, 120, "g", COR, "left")
    E.frase(c, t, lerp(C["s07.d"], C["s07.end"], 0.55), ps("o sinal diz o sentido", "i", 64, TINTA2), W / 2, 920, "center", 0.12)


# ---------------- ângulo reto ----------------
def b_reto(c, t, C, b):
    X0, X1, Y0, Y1 = 1000, 1820, 230, 920
    u = 140
    O = (1150, 860)
    Q = (O[0], O[1] - 4 * u)
    Pf = (Q[0] + 3 * u, Q[1])
    E.foco(c, t, C["s08"], 0.6, lambda a: rio(c, X0, X1, Y0, Y1, a), blur=0)
    q = ease_io(prog(t, C["s09.f"], 2.2))
    E.foco(c, t, C["s08"] + 0.3, 0.5, lambda a: barco(c, lerp(O[0], Pf[0], q), lerp(O[1], Pf[1], q), 46, a))
    F.vetor(c, t, C["s08.b"], O, Q, None, "4 m/s", F.VEL, 12, size=56)
    S = desliza(t, C["s08.d"], (O[0], O[1] - 90), Q, 0.8)
    seta_em(c, t, C["s08.c"], S, (S[0] + 3 * u, S[1]), F.VEL)
    E.foco(c, t, C["s08.c"] + 0.4, 0.4, lambda a: F.medida(c, 3, "m/s", S[0] + 1.5 * u, S[1] - 26, 50, TINTA, a, "center"))
    E.foco(c, t, C["s08.c"] + 0.4, 0.4, lambda a: rot(c, "correnteza", 1690, Y1 - 30, 40, MARGEM, a=a))
    if t >= C["s08.d"] + 0.8:
        angulo_reto(c, Q, 0, 1, 1, 0, 34, ep(t, C["s08.d"] + 0.8, 0.4))
    F.vetor(c, t, C["s08.e"], O, Pf, "R", None, E.COR, 13, 0.8, lado=-1, size=64)
    pilula_em(c, t, C["s08.e"] + 0.8, "hipotenusa", 1580, 700, 46, E.COR)
    E.frase(c, t, C["s08.a"], [("3.", "g", 76, COR), ("ângulo", "g", 76), ("reto", "g", 76)], XE, 200)
    if t < C["s09"]:
        E.frase(c, t, C["s08.b"], [("barco", "i", 70), ("4 m/s", "g", 64)], XE, 380, passo=0.14)
        E.frase(c, t, C["s08.c"], [("correnteza", "i", 70), ("3 m/s", "g", 64)], XE, 480, passo=0.14)
        E.frase(c, t, C["s08.d"], ps("as setas formam um", "i", 60, TINTA2), XE, 640, passo=0.1)
        E.frase(c, t, C["s08.d"] + 0.9, [("triângulo", "g", 64), ("retângulo", "g", 64)], XE, 730, passo=0.14)
        E.frase(c, t, C["s08.e"], [("R", "g", 70, COR), ("=", "g", 70, TINTA2), ("hipotenusa", "i", 72)], XE, 870, passo=0.14)
        return
    E.formula_em(c, t, C["s09.a"], "R^2 = 3^2 + 4^2", XE, 380, 96, "g", TINTA)
    E.formula_em(c, t, C["s09.b"], "= 9 + 16", XE + 140, 520, 96, "g", TINTA)
    E.formula_em(c, t, C["s09.d"], "= 25", XE + 140, 650, 96, "g", TINTA)
    E.formula_em(c, t, C["s09.e"], "R = r{25}", XE, 790, 96, "g", COR)
    bola_txt(c, t, C["s09.e"] + 1.0, "5 m/s", 780, 760, 110, 60)
    E.frase(c, t, C["s09.f"] + 0.4, ps("na diagonal", "i", 60, TINTA2), XE, 960, passo=0.12)


# ---------------- subtrair ----------------
def b_subtrair(c, t, C, b):
    E.frase(c, t, C["s10"], [("subtrair", "g", 84)], XE, 220)
    E.frase(c, t, C["s10.a"], [("=", "g", 80, TINTA2), ("somar", "i", 84), ("o", "i", 84), ("oposto", "g", 80, COR)], XE + 420, 220, passo=0.12)
    F.vetor(c, t, C["s10.a"] + 0.4, (1150, 330), (1500, 330), "b", None, F.VEL, 11, size=56)
    F.vetor(c, t, C["s10.b"], (1500, 430), (1150, 430), "−b", None, F.VEL, 11, lado=1, size=56)
    if t >= C["s10.b"]:
        M.line(c, 1050, 500, 1800, 500, FIO, ep(t, C["s10.b"], 0.4), 3)
    # bola e parede
    yb, xp = 640, 1760
    E.foco(c, t, C["s10.c"], 0.5, lambda a: F.parede(c, xp, 540, 900, lado=1, a=a))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.bola(c, xp - 46, 720, 40, a=a))
    F.vetor(c, t, C["s10.c"] + 0.3, (1120, yb), (1620, yb), None, "+5 m/s", F.VEL, 11, size=52)
    F.vetor(c, t, C["s10.d"], (1620, yb + 180), (1120, yb + 180), None, "−5 m/s", F.VEL, 11, lado=-1, size=52)
    E.foco(c, t, C["s10.c"] + 0.4, 0.4, lambda a: E.escreve(c, "inicial", 930, yb + 16, 44, "i", TINTA2, a))
    E.foco(c, t, C["s10.d"] + 0.4, 0.4, lambda a: E.escreve(c, "final", 960, yb + 196, 44, "i", TINTA2, a))
    E.frase(c, t, C["s10.e"], ps("final − inicial", "i", 64), XE, 600, passo=0.12)
    E.formula_em(c, t, C["s10.e"] + 1.6, "(−5) + (−5)", XE, 730, 90, "g", TINTA)
    E.formula_em(c, t, C["s10.f"], "= −10 m/s", XE, 860, 90, "g", COR)
    E.frase(c, t, C["s10.g"], [("mudou", "i", 60), ("10", "g", 60, COR), ("m/s,", "b", 50, F.UNID), ("não", "i", 60), ("0", "g", 60, ERRADO)], XE, 980, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("somar os módulos sempre", "i", 72), XE + 480, 200, passo=0.12)

    def s11a():
        E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "4 + 3 = 7 ?", W / 2, 420, 130, "g", ERRADO, a, "center"))
        if t >= C["s11.b"] + 0.9:
            E.risco(c, W / 2 - 330, 440, W / 2 + 330, 320, t, C["s11.b"] + 0.9, largura=12)
        E.frase(c, t, C["s11.c"], ps("7 só com as setas em fila", "i", 64, TINTA2), W / 2, 560, "center", 0.1)
    E.saida(c, t, C["s11.d"] - 0.1, s11a)
    if t < C["s11.d"]:
        return
    vx = E.reta(c, t, C["s11.d"], 300, 1620, 560, 0, 8, list(range(9)), size=50)
    q = ease_io(prog(t, C["s11.e"], 0.7))
    if q > 0:
        M.rrect(c, vx(1), 530, (vx(7) - vx(1)) * q, 60, 30, E.COR, 0.28)
    E.foco(c, t, C["s11.e"] + 0.2, 0.5, lambda a: (centro(c, "diferença", vx(1), 460, 50, "i", TINTA2, a), centro(c, "4 − 3", vx(1), 400, 50, "b", TINTA, a)))
    E.foco(c, t, C["s11.e"] + 0.7, 0.5, lambda a: (centro(c, "soma", vx(7), 460, 50, "i", TINTA2, a), centro(c, "4 + 3", vx(7), 400, 50, "b", TINTA, a)))
    E.frase(c, t, C["s11.d"], ps("R fica sempre entre", "i", 66, TINTA), W / 2, 760, "center", 0.12)
    E.foco(c, t, C["s11.f"], 0.5, lambda a: (E.bola(c, vx(5), 560, 44, a=a), centro(c, "5", vx(5), 580, 54, "g", BR, a)))
    E.frase(c, t, C["s11.f"] + 0.3, [("ângulo", "i", 70), ("reto:", "i", 70), ("Pitágoras", "g", 70, COR)], W / 2, 900, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s12.a"], ps("decore os", "i", 76, CLARO) + [("ternos", "g", 76, BR)], W / 2, 290, "center", 0.12)
        for i, (k, s) in enumerate((("s12.b", "3 · 4 · 5"), ("s12.c", "6 · 8 · 10"), ("s12.d", "5 · 12 · 13"))):
            x = 440 + i * 520
            E.foco(c, t, C[k], 0.5, lambda a, x=x, s=s: (M.rrect(c, x - 220, 380, 440, 170, 30, E.COR, 0.9 * a),
                                                       centro(c, s, x, 495, 84, "g", BR, a)))
        E.frase(c, t, C["s12.e"] - 2.2, [("6", "g", 76, BR), ("e", "i", 76, CLARO), ("8", "g", 76, BR)] + ps("em ângulo reto?", "i", 76, CLARO), W / 2, 720, "center", 0.12)
        E.foco(c, t, C["s12.e"], 0.5, lambda a: (E.bola(c, W / 2, 880, 100, a=a), centro(c, "10", W / 2, 908, 80, "g", BR, a)))
        E.frase(c, t, C["s12.e"] + 0.5, ps("sem conta", "i", 64, CLARO), W / 2 + 180, 900, "left", 0.12)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("terno", "g", 76, BR), ("=", "g", 76, CLARO)] + ps("Pitágoras já feito", "i", 76, CLARO), W / 2, 220, "center", 0.12)
    E.formula_em(c, t, C["s13.a"] + 1.4, "6^2 + 8^2 = 100  →  r{100} = 10", W / 2, 400, 90, "g", BR, "center")
    E.frase(c, t, C["s13.b"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("1 e 2 não formam terno", "i", 70, CLARO), W / 2, 640, "center", 0.1)
    E.formula_em(c, t, C["s13.c"], "R = r{1^2 + 2^2} = r{5}", W / 2, 820, 96, "g", CLARO, "center")


# ---------------- questão ----------------
def rosa(c, cx, cy, r, a=1.0):
    """rosa dos ventos simples: N, L, S, O"""
    if a <= 0:
        return
    M.line(c, cx - r, cy, cx + r, cy, FIO, a, 3)
    M.line(c, cx, cy - r, cx, cy + r, FIO, a, 3)
    for s, dx, dy in (("N", 0, -1), ("S", 0, 1), ("L", 1, 0), ("O", -1, 0)):
        centro(c, s, cx + dx * (r + 40), cy + dy * (r + 40) + 18, 48, "g", TINTA2, a)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], [("drone:", "i", 72), ("norte", "g", 68), ("12 m/s", "g", 68, COR)], XE, 350, passo=0.14)
    E.frase(c, t, C["s14.b"], [("vento:", "i", 72), ("leste", "g", 68), ("5 m/s", "g", 68, COR)], XE, 470, passo=0.14)
    E.frase(c, t, C["s14.c"], [("resultante?", "g", 76)], XE, 630)
    E.frase(c, t, C["s14.d"], ps("e se o vento fosse", "i", 64) + [("para o sul?", "g", 64, COR)], XE, 780, passo=0.12)
    O = (1460, 640)
    if t < C["s15"]:
        E.foco(c, t, C["s14.a"], 0.5, lambda a: rosa(c, *O, 300, a))
        E.foco(c, t, C["s14.a"] + 0.2, 0.5, lambda a: drone(c, *O, 46, a))
        F.vetor(c, t, C["s14.a"] + 0.6, (O[0], O[1] - 70), (O[0], O[1] - 300), None, "12 m/s", F.VEL, 11, size=50)
        F.vetor(c, t, C["s14.b"] + 0.4, (O[0] + 70, O[1]), (O[0] + 200, O[1]), None, None, F.VEL, 11)
        E.foco(c, t, C["s14.b"] + 0.8, 0.4, lambda a: F.medida(c, 5, "m/s", O[0] + 140, O[1] + 70, 50, TINTA, a, "center"))
    else:
        E.relogio(c, t, C["s15.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    u = 52
    O = (1250, 940)

    def s16():
        Q = (O[0], O[1] - 12 * u)
        Pf = (Q[0] + 5 * u, Q[1])
        F.vetor(c, t, C["s16"] + 0.3, O, Q, None, "12 m/s", F.VEL, 11, size=52)
        F.vetor(c, t, C["s16"] + 0.8, Q, Pf, None, "5 m/s", F.VEL, 11, size=52)
        if t >= C["s16.a"]:
            angulo_reto(c, Q, 0, 1, 1, 0, 30, ep(t, C["s16.a"], 0.4))
        F.vetor(c, t, C["s16.c"], O, Pf, "R", None, E.COR, 12, lado=-1, size=60)
        E.frase(c, t, C["s16.a"], ps("norte e leste:", "i", 70) + [("ângulo", "g", 66), ("reto", "g", 66)], XE, 230, passo=0.12)
        E.foco(c, t, C["s16.b"], 0.5, lambda a: (M.rrect(c, XE, 300, 500, 140, 30, E.COR, 0.9 * a), centro(c, "5 · 12 · 13", XE + 250, 395, 76, "g", BR, a)))
        bola_txt(c, t, C["s16.c"], "13 m/s", XE + 760, 370, 120, 60)
        E.formula_em(c, t, C["s16.d"], "5^2 + 12^2 = 25 + 144 = 169", XE, 640, 74, "g", TINTA)
        E.formula_em(c, t, C["s16.e"], "R = r{169} = 13", XE, 790, 84, "g", COR)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], ps("vento para o sul:", "i", 70) + [("opostos", "g", 66, COR)], XE, 230, passo=0.12)
    x = 1400
    F.vetor(c, t, C["s17.a"], (x, 900), (x, 900 - 12 * u), None, "12 m/s", F.VEL, 11, size=52)
    F.vetor(c, t, C["s17.a"] + 0.6, (x + 70, 900 - 12 * u), (x + 70, 900 - 7 * u), None, "5 m/s", F.VEL, 11, lado=1, size=52)
    F.vetor(c, t, C["s17.c"], (x + 330, 900), (x + 330, 900 - 7 * u), "R", "7 m/s", E.COR, 12, lado=1, size=60)
    E.formula_em(c, t, C["s17.b"], "12 − 5 = 7", XE, 460, 110, "g", TINTA)
    bola_txt(c, t, C["s17.c"], "7 m/s", XE + 220, 700, 120, 64)
    E.frase(c, t, C["s17.c"] + 0.8, ps("para o norte, o do maior", "i", 60, TINTA2), XE, 900, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s18():
        resumo(c, t, C, "s18", (("s18.a", [("mesmo", "i", 70), ("sentido:", "i", 70), ("soma", "g", 70, COR)]),
                                ("s18.b", [("opostos:", "i", 70), ("subtrai,", "g", 70, COR), ("sentido", "i", 70), ("do", "i", 70), ("maior", "i", 70)]),
                                ("s18.c", [("ângulo", "i", 70), ("reto:", "i", 70), ("Pitágoras", "g", 70, COR)])))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("parado", "g", 110, COR), ("ou", "i", 100)], XE, 400)
    E.frase(c, t, C["s19.a"] + 0.5, [("em movimento?", "g", 110, COR)], XE, 530)
    E.frase(c, t, C["s19.b"], [("distância", "g", 70), ("×", "g", 70, TINTA2), ("deslocamento", "g", 70)], XE, 680, passo=0.14)
    E.foco(c, t, C["s19.a"] + 0.6, 0.5, lambda a: F.carrinho(c, 600, 900, 300, a=a))
    if t >= C["s19.a"] + 0.6:
        F.chao(c, 300, 1000, 900, ep(t, C["s19.a"] + 0.6, 0.4))
    fim_inscreva(c, t, C, "s19", "s19.c", "s19.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, resultante=b_resultante, fila=b_fila, reto=b_reto, subtrair=b_subtrair,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
