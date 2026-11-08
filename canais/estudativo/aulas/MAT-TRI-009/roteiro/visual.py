"""Visual — Estudativo · MAT-TRI-009: redução ao primeiro quadrante (sen 150° = sen 30° = 1/2; cos 240° = −cos 60° = −1/2;
sen 330° = −1/2; sen 225° = −√2/2; cos 300° = 1/2).
Linguagem da trigonometria (MAT-TRI-001, 007 e 008): seno = altura em âmbar (OPO), cosseno = horizontal em petróleo (ADJ; ADJ_ESC no
palco escuro), raio em índigo; o ângulo original é o ponto P na cor da matéria e o PARCEIRO do 1º quadrante é um ponto vazado
(contorno), ligado a P por uma linha tracejada que mostra o espelho: horizontal no 2º quadrante (espelho no eixo y), pelo centro
no 3º, vertical no 4º (espelho no eixo x). A distância até 180° ou 360° é um arco cinza com o valor. "+" verde, "−" vermelho.
A figura não mente: os pontos estão nos ângulos ditos, e as alturas e larguras dos pares são iguais de verdade.
Peças locais: ciclo(), ponto() (P cheio ou parceiro vazado), barra_sen(), barra_cos(), espelho() (linha entre o par), arco_dist()
(o pedaço até 180° ou 360°), resp(), lista(), pilula().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-009_reducao_ao_primeiro_quadrante.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("segundo", "terceiro", "metodo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"      # cor fixa de cada lado da trigonometria
ADJ_ESC = "#3CC7D3"
S = lambda g: math.sin(math.radians(g))
Cs = lambda g: math.cos(math.radians(g))
assert abs(S(150) - 0.5) < 1e-12 and abs(S(150) - S(30)) < 1e-12 and abs(Cs(150) + math.sqrt(3) / 2) < 1e-12 and 180 - 150 == 30
assert 240 - 180 == 60 and abs(Cs(240) + 0.5) < 1e-12 and 360 - 330 == 30 and abs(S(330) + 0.5) < 1e-12
assert 225 - 180 == 45 and abs(S(225) + math.sqrt(2) / 2) < 1e-12 and 360 - 300 == 60 and abs(Cs(300) - 0.5) < 1e-12 and 360 - 315 == 45


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def resp(c, t, t0, s, cx, cy, size=76, alto=1.75, cor=None):
    def f(a):
        w = E.formula(c, s, 0, 0, size, a=0) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")
    E.foco(c, t, t0, 0.5, f)


def pilula(c, t, t0, s, cx, cy, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", a=a, cor=E.SOBRE))


def lista(c, t, itens, x, y0, dy=150, size=64):
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - size * 0.36, 40, a=a),
                                                   centro(c, str(i + 1), x + 40, y - size * 0.36 + 18, 50, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 110, y, "left", 0.1)


def pt(cx, cy, r, ang):
    return cx + r * Cs(ang), cy - r * S(ang)


def ciclo(c, t, t0, cx, cy, r, escuro=False, tq=None, marcas=True):
    if t < t0:
        return
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.6)
    M.arrow(c, cx - r - 70, cy, cx + r + 90, cy, tinta, q, 4, 20, q)
    M.arrow(c, cx, cy + r + 70, cx, cy - r - 90, tinta, q, 4, 20, q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, t0 + 0.2, 0.9)), False, M.paint(tinta, 1.0, stroke=5))
    sec = CLARO if escuro else TINTA2
    E.foco(c, t, t0 + 0.6, 0.4, lambda a: (E.escreve(c, "x", cx + r + 70, cy + 56, 50, "i", sec, a),
                                           E.escreve(c, "y", cx + 22, cy - r - 66, 50, "i", sec, a)))
    if tq is not None:
        for i, ang in enumerate((45, 135, 225, 315)):
            X, Y = pt(cx, cy, r * 0.62, ang)
            E.foco(c, t, tq + 0.12 * i, 0.4, lambda a, i=i, X=X, Y=Y: centro(c, f"{i + 1}º", X, Y + 20, 50, "g", CINZA if not escuro else CLARO, a))


def ponto(c, t, t0, cx, cy, r, ang, rot=None, parceiro=False, escuro=False, fora=72, size=50, arco=True):
    """P (cheio) ou o parceiro (vazado), com o arco desde 0 e o rótulo do ângulo por fora"""
    k = ease_back(prog(t, t0, 0.4))
    if k <= 0:
        return
    cor = E.COR if not escuro else CLARO
    if arco and not parceiro:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -ang * ease_io(prog(t, t0, 0.7)), False, M.paint(cor, 0.85, stroke=8, cap_round=True))
    X, Y = pt(cx, cy, r, ang)
    if parceiro:
        c.drawCircle(X, Y, 15 * k, M.paint(BR if not escuro else "#07070F"))
        c.drawCircle(X, Y, 15 * k, M.paint(cor, 1.0, stroke=6))
    else:
        c.drawCircle(X, Y, 16 * k, M.paint(cor))
        c.drawCircle(X, Y, 16 * k, M.paint(BR if not escuro else "#07070F", 1.0, stroke=3))
    if rot:
        Xr, Yr = pt(cx, cy, r + fora, ang)
        E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.formula(c, rot, Xr, Yr + size * 0.36, size, "g", cor if not parceiro else (TINTA2 if not escuro else CLARO), a, "center"))


def barra_sen(c, t, t0, cx, cy, r, ang, cor=None, a=1.0):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    X, Y = pt(cx, cy, r, ang)
    M.line(c, X, cy, X, lerp(cy, Y, q), cor or OPO, a, 12, cap_round=False)


def barra_cos(c, t, t0, cx, cy, r, ang, cor=None, a=1.0, dy=0):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    X, Y = pt(cx, cy, r, ang)
    M.line(c, cx, cy + dy, lerp(cx, X, q), cy + dy, cor or ADJ, a, 12, cap_round=False)


def espelho(c, t, t0, cx, cy, r, a1, a2, cor=TINTA2, a=1.0):
    q = ep(t, t0, 0.7) * a
    if q <= 0:
        return
    P1, P2 = pt(cx, cy, r, a1), pt(cx, cy, r, a2)
    M.line(c, *P1, *P2, cor, a, 4, dash=E.TRACO, progress=ease_io(prog(t, t0, 0.7)))


def arco_dist(c, t, t0, cx, cy, r, de, ate, rot, cor=CINZA, size=46, a=1.0, fora=46):
    fora = max(fora, 78)
    """arco de `de` até `ate` (graus) um pouco por fora, com o valor"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    rr = r + 24
    ini, varre = min(de, ate), abs(ate - de)
    c.drawArc(skia.Rect.MakeXYWH(cx - rr, cy - rr, 2 * rr, 2 * rr), -ini, -varre * ease_io(prog(t, t0, 0.6)), False, M.paint(cor, a, stroke=10, cap_round=True))
    meio = (de + ate) / 2
    X, Y = pt(cx, cy, rr + fora, meio)
    E.foco(c, t, t0 + 0.4, 0.4, lambda b: E.formula(c, rot, X, Y + size * 0.36, size, "g", cor, b * a, "center"))


# ---------------- gancho ----------------
GX, GY_, GR = 1400, 580, 270


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.foco(c, t, a1, 0.5, lambda a: E.formula(c, "sen 150°", XE, 420, 170, "g", TINTA, a))
        E.frase(c, t, a1 + 1.4, ps("não está na tabela", "i", 60, TINTA2), XE, 540, "left", 0.08)
        E.foco(c, t, b1, 0.5, lambda a: E.formula(c, "= f{1}{2} = sen 30°", XE, 740, 110, "g", OPO, a))
        E.frase(c, t, c1, ps("todo arco tem um", "i", 60) + [("parceiro", "g", 66, COR)], XE, 920, "left", 0.1)
        E.frase(c, t, c1 + 1.4, ps("no 1º quadrante", "i", 60), XE, 1000, "left", 0.1)
        ciclo(c, t, a1 + 0.3, GX, GY_, GR, marcas=False)
        ponto(c, t, a1 + 0.8, GX, GY_, GR, 150, "150°")
        ponto(c, t, b1, GX, GY_, GR, 30, "30°", parceiro=True)
        espelho(c, t, b1 + 0.3, GX, GY_, GR, 150, 30)
        barra_sen(c, t, b1 + 0.6, GX, GY_, GR, 150)
        barra_sen(c, t, b1 + 0.6, GX, GY_, GR, 30)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 280, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("sen", "g", 100, OPO)] + ps("e", "i", 90) + [("cos", "g", 100, ADJ)], XE, 440, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("fora do 1º quadrante", "i", 80), XE, 570, passo=0.12)
        E.frase(c, t, tb, ps("com a", "i", 80) + [("tabela", "g", 90, COR)] + ps("que você já conhece", "i", 70), XE, 720, passo=0.12)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 545, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 630, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "a tabela de", [("30°, 45° e 60°", "g", 64, COR)]),
             ("s03.c", "no ciclo:", [("sen", "g", 64, OPO), ("altura,", "i", 58), ("cos", "g", 64, ADJ), ("horizontal", "i", 58)]),
             ("s03.d", "os sinais:", [("to, se, ta, co", "g", 64, COR)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, l2, x + 44, y + 164, "left", 0.08)
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 580, q1), 820, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- segundo quadrante ----------------
CX, CY, CR = 590, 560, 320


def b_segundo(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5 = (C[f"s05.{k}"] for k in "abc")
    a6 = C["s06.a"]
    X = 1420
    ciclo(c, t, C["s04"] - 0.3, CX, CY, CR, tq=C["s04"])
    ponto(c, t, a4, CX, CY, CR, 150, "150°")
    arco_dist(c, t, b4, CX, CY, CR, 150, 180, "30°", fora=40)
    ponto(c, t, c4, CX, CY, CR, 30, "30°", parceiro=True)
    if t >= d4:  # o espelho: o eixo vertical acende
        q = ep(t, d4, 0.5)
        M.line(c, CX, CY - CR - 40, CX, CY + CR + 40, COR, q, 7, dash=[22, 12])
    espelho(c, t, d4 + 0.4, CX, CY, CR, 150, 30)
    barra_sen(c, t, a5, CX, CY, CR, 150)
    barra_sen(c, t, a5 + 0.3, CX, CY, CR, 30)
    barra_cos(c, t, b5, CX, CY, CR, 30)
    barra_cos(c, t, b5 + 0.4, CX, CY, CR, 150)

    def quatro():
        E.frase(c, t, a4, [("150°:", "g", 66, COR)] + ps("2º quadrante", "i", 60), X, 220, "center", 0.1)
        E.frase(c, t, b4, ps("faltam", "i", 60) + [("30°", "g", 66, CINZA)] + ps("para 180°", "i", 60), X, 360, "center", 0.1)
        E.frase(c, t, c4, ps("marque", "i", 60) + [("30°", "g", 66, TINTA2)] + ps("no 1º", "i", 60), X, 500, "center", 0.1)
        E.frase(c, t, d4, [("frente a frente", "g", 66, COR)], X, 660, "center", 0.1)
        E.frase(c, t, d4 + 1.2, ps("o eixo vertical é o espelho", "i", 54, TINTA2), X, 750, "center", 0.08)
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t < C["s05"] - 0.1:
        return

    def cinco():
        E.frase(c, t, a5, ps("a mesma", "i", 60) + [("altura", "g", 66, OPO)], X, 220, "center", 0.1)
        fcen(c, t, a5 + 1.0, "sen 150° = sen 30° = f{1}{2}", X, 380, 74, OPO)
        E.frase(c, t, b5, ps("a mesma", "i", 60) + [("horizontal,", "g", 64, ADJ)] + ps("à esquerda", "i", 60), X, 560, "center", 0.1)
        fcen(c, t, c5, "cos 150° = −f{r{3}}{2}", X, 720, 84, ADJ)
    E.saida(c, t, a6 - 0.1, cinco)
    if t >= a6 - 0.1:
        E.frase(c, t, a6, ps("regra do", "i", 64) + [("2º quadrante", "g", 68, COR)], X, 340, "center", 0.1)
        resp(c, t, a6 + 0.8, "parceiro = 180° − ângulo", X, 520, 64)
        fcen(c, t, a6 + 1.8, "180° − 150° = 30°", X, 720, 72, TINTA2)


# ---------------- terceiro quadrante ----------------
def b_terceiro(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = (C[f"s08.{k}"] for k in "abc")
    X = 1420
    ciclo(c, t, C["s07"] - 0.3, CX, CY, CR, tq=C["s07"])
    ponto(c, t, b7, CX, CY, CR, 240, "240°")
    arco_dist(c, t, c7, CX, CY, CR, 180, 240, "60°", fora=44)
    ponto(c, t, d7, CX, CY, CR, 60, "60°", parceiro=True)
    espelho(c, t, d7 + 0.3, CX, CY, CR, 240, 60)
    barra_cos(c, t, a8, CX, CY, CR, 60, dy=0)
    barra_cos(c, t, b8, CX, CY, CR, 240, dy=0)
    E.foco(c, t, a8 + 0.4, 0.4, lambda a: E.formula(c, "f{1}{2}", CX + CR / 4, CY + 90, 50, "g", ADJ, a, "center"))
    E.foco(c, t, b8 + 0.4, 0.4, lambda a: E.formula(c, "−f{1}{2}", CX - CR / 4, CY - 50, 50, "g", ADJ, a, "center"))
    fcen(c, t, a7, "cos 240°", X, 230, 110)

    def sete():
        E.frase(c, t, b7, ps("passou de 180°:", "i", 58) + [("3º quadrante", "g", 62, COR)], X, 380, "center", 0.1)
        fcen(c, t, c7, "240 − 180 = 60", X, 530, 84)
        E.frase(c, t, d7, ps("parceiro", "i", 58) + [("60°,", "g", 64, TINTA2)] + ps("do lado oposto", "i", 58), X, 680, "center", 0.1)
        E.frase(c, t, d7 + 1.4, ps("passando pelo centro", "i", 52, TINTA2), X, 770, "center", 0.08)
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t < C["s08"] - 0.1:
        return
    fcen(c, t, a8, "cos 60° = f{1}{2}", X, 430, 80, ADJ)
    E.frase(c, t, b8, ps("no 3º,", "i", 60) + [("cos", "g", 64, ADJ), ("−", "g", 76, ERRADO)], X, 600, "center", 0.1)
    resp(c, t, c8, "cos 240° = −f{1}{2}", X, 790, 70, 2.4, cor=ADJ)


# ---------------- quarto quadrante ----------------
def b_quarto(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    X = 1420
    ciclo(c, t, C["s09"] - 0.3, CX, CY, CR, tq=C["s09"])
    ponto(c, t, c9, CX, CY, CR, 330, "330°")
    arco_dist(c, t, c9 + 0.6, CX, CY, CR, 330, 360, "30°", fora=40)
    ponto(c, t, c9 + 1.2, CX, CY, CR, 30, "30°", parceiro=True)
    espelho(c, t, c9 + 1.5, CX, CY, CR, 330, 30)
    barra_sen(c, t, d9, CX, CY, CR, 30)
    barra_sen(c, t, d9 + 0.3, CX, CY, CR, 330)
    E.frase(c, t, a9, [("3º:", "g", 62, COR)] + ps("parceiro =", "i", 58) + [("ângulo − 180°", "g", 62)], X, 220, "center", 0.1)
    E.frase(c, t, b9, [("4º:", "g", 62, COR)] + ps("parceiro =", "i", 58) + [("360° − ângulo", "g", 62)], X, 340, "center", 0.1)
    fcen(c, t, c9, "360 − 330 = 30", X, 520, 84)
    E.frase(c, t, d9, ps("no 4º,", "i", 60) + [("sen", "g", 64, OPO), ("−", "g", 76, ERRADO)], X, 680, "center", 0.1)
    resp(c, t, d9 + 1.4, "sen 330° = −f{1}{2}", X, 860, 70, 2.4, cor=OPO)


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    E.frase(c, t, a0 - 0.6, ps("o método em", "i", 80) + [("2 passos", "g", 90, COR)], XE, 230, "left", 0.12)
    E.foco(c, t, b0, 0.5, lambda a: (E.bola(c, XE + 70, 420, 70, a=a), centro(c, "1", XE + 70, 448, 84, "g", BR, a)))
    E.frase(c, t, b0 + 0.1, [("o número:", "g", 80)], XE + 180, 450, "left", 0.1)
    E.frase(c, t, b0 + 0.8, ps("o valor do parceiro na tabela", "i", 62, TINTA2), XE + 180, 540, "left", 0.08)
    E.foco(c, t, c0, 0.5, lambda a: (E.bola(c, XE + 70, 700, 70, a=a), centro(c, "2", XE + 70, 728, 84, "g", BR, a)))
    E.frase(c, t, c0 + 0.1, [("o sinal:", "g", 80)], XE + 180, 730, "left", 0.1)
    E.frase(c, t, c0 + 0.8, ps("o quadrante do ângulo", "i", 62, TINTA2) + [("original", "g", 64, COR)], XE + 180, 820, "left", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    X = 1420
    ciclo(c, t, C["s11"] - 0.3, CX, CY, CR, tq=C["s11"])
    ponto(c, t, C["s11"], CX, CY, CR, 240, "240°")
    ponto(c, t, C["s11"] + 0.3, CX, CY, CR, 60, "60°", parceiro=True)
    espelho(c, t, C["s11"] + 0.5, CX, CY, CR, 240, 60)
    if t >= b1:  # o sinal copiado: o cosseno desenhado à direita, errado
        k = ep(t, b1, 0.5) * (1 - ep(t, c1, 0.4))
        M.line(c, CX, CY + 40, CX + CR / 2, CY + 40, ERRADO, k, 12, cap_round=False)
    if t >= c1:
        q = ep(t, c1, 0.5)
        M.line(c, CX, CY - CR - 40, CX, CY + CR + 40, COR, q, 7, dash=[22, 12])
        barra_cos(c, t, c1 + 0.3, CX, CY, CR, 240)
        E.foco(c, t, c1 + 0.6, 0.4, lambda a: E.escreve(c, "à esquerda", CX - CR + 10, CY - 30, 48, "g", ADJ, a))
    E.frase(c, t, a1, ps("o erro:", "i", 60) + [("copiar o sinal do parceiro", "g", 58, ERRADO)], X, 220, "center", 0.1)
    fcen(c, t, b1, "cos 240° = f{1}{2}", X - 40, 390, 80, ERRADO)
    E.foco(c, t, b1 + 0.5, 0.5, lambda a: E.selo(c, X + 270, 365, 40, False, a))
    fcen(c, t, c1, "cos 240° = −f{1}{2}", X - 40, 580, 80, CERTO)
    E.foco(c, t, c1 + 0.8, 0.5, lambda a: E.selo(c, X + 290, 555, 40, True, a))
    E.foco(c, t, d1, 0.5, lambda a: E.caixa_pontilhada(c, X - 380, 700, 760, 250, a, COR, prog_=ep(t, d1, 0.6)))
    E.frase(c, t, d1 + 0.1, [("parceiro", "g", 64, COR), ("→", "b", 56)] + ps("o número", "i", 60), X, 800, "center", 0.1)
    E.frase(c, t, e1, [("quadrante", "g", 64, COR), ("→", "b", 56)] + ps("o sinal", "i", 60), X, 900, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    cx, cy, r = 560, 580, 300
    X = 1420

    def doze():
        ciclo(c, t, C["s12"] - 0.3, cx, cy, r, escuro=True)
        if t >= a2:  # o eixo horizontal acende
            q = ep(t, a2, 0.5)
            M.line(c, cx - r - 50, cy, cx + r + 50, cy, AMBAR, q, 8)
        for ang, rot in ((180, "180°"), (360, "360°")):
            X0, Y0 = pt(cx, cy, r, ang)
            k = ease_back(prog(t, b2, 0.4))
            if k > 0:
                c.drawCircle(X0, Y0, 14 * k, M.paint(AMBAR))
                E.escreve(c, rot, X0 - 150 if ang == 180 else X0 + 10, Y0 + (70 if ang == 180 else -30), 46, "g", AMBAR, ep(t, b2, 0.4))
        for ang, de, ate, rot, tk in ((150, 150, 180, "30°", c2), (240, 180, 240, "60°", d2), (315, 315, 360, "45°", e2)):
            ponto(c, t, tk, cx, cy, r, ang, f"{ang}°", escuro=True, arco=False, fora=80)
            arco_dist(c, t, tk + 0.3, cx, cy, r, de, ate, rot, CLARO, 46, fora=40)

        def txt():
            E.frase(c, t, C["s12"] + 0.2, ps("agora o atalho", "i", 60, CLARO), X, 200, "center", 0.1)
            E.frase(c, t, a2, ps("parceiro =", "i", 62, CLARO) + [("distância até", "g", 64, BR)], X, 320, "center", 0.1)
            E.frase(c, t, a2 + 1.0, [("o eixo horizontal", "g", 64, AMBAR)], X, 410, "center", 0.1)
            E.frase(c, t, b2, ps("olhe", "i", 58, CLARO) + [("180°", "g", 62, AMBAR)] + ps("ou", "i", 58, CLARO) + [("360°", "g", 62, AMBAR)], X, 540, "center", 0.1)
            E.frase(c, t, c2, [("150°", "g", 60, BR)] + ps("está a", "i", 56, CLARO) + [("30°", "g", 60, CLARO)] + ps("de 180°", "i", 56, CLARO), X, 680, "center", 0.1)
            E.frase(c, t, d2, [("240°", "g", 60, BR)] + ps("está a", "i", 56, CLARO) + [("60°", "g", 60, CLARO)] + ps("de 180°", "i", 56, CLARO), X, 780, "center", 0.1)
            E.frase(c, t, e2, [("315°", "g", 60, BR)] + ps("está a", "i", 56, CLARO) + [("45°", "g", 60, CLARO)] + ps("de 360°", "i", 56, CLARO), X, 880, "center", 0.1)
        txt()
    E.saida(c, t, C["s13"] - 0.1, doze)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, a3, ps("funciona porque o ciclo é", "i", 66, CLARO) + [("simétrico", "g", 74, BR)], W / 2, 230, "center", 0.12)
    E.frase(c, t, b3, ps("mesma distância do eixo horizontal:", "i", 56, CLARO), W / 2, 360, "center", 0.1)
    E.frase(c, t, b3 + 1.0, [("mesma altura,", "g", 64, OPO), ("mesma horizontal", "g", 64, ADJ_ESC)], W / 2, 450, "center", 0.1)
    E.frase(c, t, b3 + 2.0, ps("só muda o", "i", 60, CLARO) + [("sinal", "g", 66, BR)], W / 2, 550, "center", 0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.selo(c, 480, 690, 42, False, a))
    E.frase(c, t, c3, [("90°, 270°:", "g", 64, BR)] + ps("em cima dos eixos,", "i", 56, CLARO) + [("leia no ciclo", "g", 60, BR)], 560, 715, "left", 0.1)
    E.frase(c, t, d3, ps("maior que uma volta?", "i", 60, CLARO) + [("tire 360° primeiro", "g", 66, BR)], W / 2, 900, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4 = C["s14.a"], C["s14.b"]
    E.frase(c, t, C["s14"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 220, passo=0.12)
    E.frase(c, t, a4 - 0.6, ps("calcule", "i", 80), XE, 380, passo=0.1)
    E.foco(c, t, a4, 0.5, lambda a: E.formula(c, "sen 225°", XE, 560, 130, "g", OPO, a))
    E.foco(c, t, b4, 0.5, lambda a: E.formula(c, "cos 300°", XE, 760, 130, "g", ADJ, a))
    E.relogio(c, t, C["s15.a"], 1520, 440, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    X = 1420
    ciclo(c, t, C["s16"] - 0.3, CX, CY, CR, tq=C["s16"])

    def dezesseis():
        ponto(c, t, a6, CX, CY, CR, 225, "225°")
        arco_dist(c, t, b6, CX, CY, CR, 180, 225, "45°", fora=44)
        ponto(c, t, b6 + 0.5, CX, CY, CR, 45, "45°", parceiro=True)
        espelho(c, t, b6 + 0.8, CX, CY, CR, 225, 45)
        barra_sen(c, t, c6, CX, CY, CR, 45)
        barra_sen(c, t, d6, CX, CY, CR, 225)
        E.frase(c, t, a6, [("225°:", "g", 66, COR)] + ps("3º quadrante", "i", 60), X, 200, "center", 0.1)
        fcen(c, t, b6, "225 − 180 = 45", X, 350, 84)
        fcen(c, t, c6, "sen 45° = f{r{2}}{2}", X, 520, 80, OPO)
        E.frase(c, t, d6, ps("no 3º,", "i", 58) + [("sen", "g", 62, OPO), ("−", "g", 72, ERRADO)], X, 680, "center", 0.1)
        resp(c, t, d6 + 1.4, "sen 225° = −f{r{2}}{2}", X, 860, 66, 2.6, cor=OPO)
    E.saida(c, t, C["s17"] - 0.1, dezesseis)
    if t < C["s17"] - 0.1:
        return
    ponto(c, t, a7, CX, CY, CR, 300, "300°")
    arco_dist(c, t, b7, CX, CY, CR, 300, 360, "60°", fora=44)
    ponto(c, t, b7 + 0.5, CX, CY, CR, 60, "60°", parceiro=True)
    espelho(c, t, b7 + 0.8, CX, CY, CR, 300, 60)
    barra_cos(c, t, c7, CX, CY, CR, 60)
    E.frase(c, t, a7, [("300°:", "g", 66, COR)] + ps("4º quadrante", "i", 60), X, 200, "center", 0.1)
    fcen(c, t, b7, "360 − 300 = 60", X, 350, 84)
    fcen(c, t, c7, "cos 60° = f{1}{2}", X, 520, 80, ADJ)
    E.frase(c, t, d7, ps("no 4º,", "i", 58) + [("cos", "g", 62, ADJ), ("+", "g", 72, CERTO)], X, 680, "center", 0.1)
    resp(c, t, d7 + 1.4, "cos 300° = f{1}{2}", X, 860, 66, 2.6, cor=ADJ)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s18.a", "ache o", "parceiro no 1º quadrante"), ("s18.b", "pegue o valor", "na tabela"), ("s18.c", "o sinal vem do", "quadrante original"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 68) + [(l2, "g", 70, COR)], 320, y, "left", 0.1)
    t_fim = min(C["s19"] + 1.4, C["s19.a"] - 0.4)
    E.saida(c, t, t_fim, resumo)
    if t < t_fim:
        return
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, t_fim + 0.1, ps("na próxima aula, seno e cosseno numa conta só", "i", 64), XE, 200, passo=0.08)
    E.foco(c, t, a9, 0.5, lambda a: E.formula(c, "sen^2 + cos^2 = 1", XE, 350, 96, "g", COR, a))
    E.foco(c, t, b9, 0.5, lambda a: E.formula(c, "sen = f{3}{5}", XE, 540, 76, "g", OPO, a))
    E.foco(c, t, c9, 0.5, lambda a: E.formula(c, "→  cos = f{4}{5}", XE + 330, 540, 76, "g", ADJ, a))
    E.foco(c, t, d9, 0.5, lambda a: E.formula(c, "tg = f{sen}{cos}", XE, 700, 70, "g", TINTA, a))
    E.foco(c, t, C["s19.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s19.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s19.e"] + 0.2, 0.4))
    E.frase(c, t, C["s19.f"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, segundo=b_segundo, terceiro=b_terceiro, quarto=b_quarto, metodo=b_metodo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
