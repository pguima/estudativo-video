"""Visual — Estudativo · MAT-POT-011: praticando raízes.
Aula de prática: quatro problemas de medida, cada um com selo de progresso, relógio de pausa e um desenho próprio:
sala com rodapé, jardim visto de cima com a tábua, canteiros na calçada e reservatório em cubo com o fundo marcado.
Todo instante vem de C[...]: o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, montar, tabela
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-011_praticando_raizes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"

T1225 = montar((1225,), (5, 5, 7, 7))
T1225_TELA = dict(T1225, linhas=[("1.225",)] + T1225["linhas"][1:])  # a tabela escreve str(v): assim sai com o ponto
G = dict(xs=(380,), xb=540, xp=640, y0=320, dy=140, s=104)  # coluna de 5 linhas
assert 5 * 7 == 35 and 35 ** 2 == 1225 and 4 * 35 == 140  # 3,5 × 4 = 14
assert 55 * 55 == 3025 and 25 < 30 < 36  # 5,5² = 30,25
assert 16 * 2 == 32 and 25 * 2 == 50 and 4 + 5 == 9 and 9 * 14 == 126 and 32 + 50 == 82  # 9 × 1,4 = 12,6
assert 3 ** 6 == 729 and 9 ** 3 == 729 and 9 * 9 == 81 and 3 * 3 == 9


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
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def fase(c, t, t0, t1, fn):
    """uma tela do bloco: de t0 até sumir em t1"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def par(c, t, ta, tb, esq, dir_, x, y, s, cor=None, cor_d=None):
    """fórmula em ta e a continuação em tb, logo depois dela"""
    w = E.formula(c, esq, 0, 0, s, a=0)
    form(c, t, ta, esq, x, y, s, cor)
    form(c, t, tb, dir_, x + w + s * 0.2, y, s, cor_d or cor)


def troca(c, t, itens, fim, x, y, size, cor=None, est="b"):
    """texto da vez: itens = [(instante, texto)], cada um some quando o seguinte chega"""
    for i, (ti, s) in enumerate(itens):
        t1 = itens[i + 1][0] - 0.15 if i + 1 < len(itens) else fim
        if ti - 0.1 <= t < t1 + 0.3:
            E.saida(c, t, t1, lambda: E.foco(c, t, ti, 0.4, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a)), d=0.2)


def marca(c, t, t0, n):
    """problema n de 4, com quatro pontos de progresso"""
    s = f"problema {n} de 4"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(4):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def perimetro(c, x, y, w, h, p, cor, largura=12):
    """contorno que se desenha lado a lado (p = 0..1)"""
    pts = ((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y))
    k = p * 4
    for i in range(4):
        q = M.clamp(k - i)
        if q > 0:
            M.line(c, pts[i][0], pts[i][1], lerp(pts[i][0], pts[i + 1][0], q), lerp(pts[i][1], pts[i + 1][1], q), cor, 1.0, largura)


def piso_sala(c, x, y, l, a, n=6):
    """a sala vista de cima: piso claro com juntas"""
    M.rrect(c, x, y, l, l, 6, E.VAZIO, a)
    for i in range(1, n):
        M.line(c, x + l * i / n, y, x + l * i / n, y + l, FIO, a, 2.5)
        M.line(c, x, y + l * i / n, x + l, y + l * i / n, FIO, a, 2.5)


def gramado(c, x, y, w, h, a, cor=None):
    """canteiro ou jardim visto de cima: a cor da matéria com tufos"""
    M.rrect(c, x, y, w, h, 10, cor or M.mix(E.COR, BR, 0.34), a)
    for i in range(int(w // 46)):
        for j in range(int(h // 46)):
            px, py = x + 24 + i * 46 + (j % 2) * 16, y + 26 + j * 46
            if px < x + w - 18:
                M.line(c, px - 7, py + 7, px, py - 6, BR, a * 0.6, 3)
                M.line(c, px + 7, py + 7, px, py - 6, BR, a * 0.6, 3)


def tabua(c, x, y, w, h, a):
    """a tábua: uma peça comprida, com veios"""
    M.rrect(c, x, y, w, h, 6, TINTA2, a)
    for f in (0.3, 0.68):
        M.line(c, x + 14, y + h * f, x + w - 14, y + h * f, BR, a * 0.3, 2.5)


def iso(cx, cy, u, i, j, k):
    """ponto do cubo em perspectiva: (cx, cy) é o canto da frente do chão. Eixos desiguais, para o canto de trás não cair em cima do da frente"""
    return cx + (i * 0.9 - j * 0.55) * u, cy - (i * 0.3 + j * 0.34 + k) * u


def face(c, pts, cor, a, tom=TINTA, stroke=4):
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    c.drawPath(p, M.paint(tom, 1.0 if a > 0.9 else a + 0.5, stroke=stroke))


def reservatorio(c, cx, cy, u, a, f=0.0):
    """cubo aberto em cima: as paredes de trás, o fundo (f = 0..1 pinta) e as duas da frente, transparentes"""
    if a <= 0:
        return
    P = lambda x, y, z: iso(cx, cy, u, x, y, z)
    fundo = [P(0, 0, 0), P(1, 0, 0), P(1, 1, 0), P(0, 1, 0)]
    face(c, [P(1, 1, 0), P(0, 1, 0), P(0, 1, 1), P(1, 1, 1)], M.mix(E.COR, BR, 0.82), a * 0.9, E.COR, 3)
    face(c, [P(1, 1, 0), P(1, 0, 0), P(1, 0, 1), P(1, 1, 1)], M.mix(E.COR, BR, 0.7), a * 0.9, E.COR, 3)
    face(c, fundo, M.mix(M.mix(E.COR, BR, 0.75), CERTO, f), a, E.COR, 3)
    face(c, [P(0, 0, 0), P(1, 0, 0), P(1, 0, 1), P(0, 0, 1)], E.COR, a * 0.32, E.COR, 5)
    face(c, [P(0, 0, 0), P(0, 1, 0), P(0, 1, 1), P(0, 0, 1)], E.COR, a * 0.22, E.COR, 5)


def dupla(c, t, ti, i, cor=None, g=G):
    """caixa em volta de dois primos seguidos da coluna: i = linha do primeiro"""
    q = ep(t, ti, 0.45)
    s, y = g["s"], g["y0"] + i * g["dy"]
    E.caixa_pontilhada(c, g["xp"] - s * 0.6, y - s * 0.88, s * 1.2, g["dy"] + s * 1.02, q, cor or COR, prog_=q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("4", "g", 240, COR) + ps("problemas", "g", 170, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 0.7, ps("de medida", "i", 120), XE, 490, passo=0.2)
    E.frase(c, t, lerp(a_, b_, 0.55), ps("criados para esta aula", "i", 72), XE, 590, passo=0.15)
    for i, (s, cx) in enumerate((("pause", 440), ("resolva", 960), ("confira", 1480))):
        ti = b_ + i * 0.5
        E.foco(c, t, ti, 0.5, lambda p: (num_bola(c, str(i + 1), cx - 190, 780, 56, 64, p), E.escreve(c, s, cx - 110, 805, 92, "g", TINTA, p)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s02.{k}"] for k in "abcd")
    fim = C["s02.end"]
    E.frase(c, t, C["s02"] + 0.1, ps("uma ideia volta sempre", "i", 88, COR), XE, 180, passo=0.13)
    x, y, l = XE + 10, 290, 460
    E.foco(c, t, a_, 0.5, lambda p: (M.rrect(c, x, y, l, l, 12, E.COR, p), centro(c, "área", x + l / 2, y + l / 2 + 34, 104, "g", E.SOBRE, p)))
    E.foco(c, t, b_, 0.45, lambda p: (E.chave(c, x, x + l, y + l + 12, COR, p, 16, 5, abre=False), centro(c, "lado", x + l / 2, y + l + 86, 62, "b", COR, p)))
    xt = 770
    E.frase(c, t, a_ + 0.3, ps("área:", "g", 76, COR) + ps("o tamanho de uma superfície", "i", 70), xt, 340, passo=0.1)
    form(c, t, b_, "área = lado × lado", xt, 500, 90)
    E.foco(c, t, c_, 0.45, lambda p: E.formula(c, "em metros quadrados: m^2", xt, 620, 70, cor=TINTA2, a=p, estilo="b"))
    form(c, t, d_, "lado = r{área}", xt, 810, 110, COR)
    E.frase(c, t, lerp(d_, fim, 0.6), ps("travou? procure a aula no canal", "i", 62), xt, 950, passo=0.11)


# ---------------- problema 1 ----------------
def b_questao1(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s03.{k}"] for k in "abcd")
    marca(c, t, a_, 1)
    x, y, l = 1290, 280, 420
    form(c, t, b_, "sala quadrada: 12,25 m^2", XE, 330, 92, COR)
    E.frase(c, t, c_, ps("rodapé nas", "i", 88) + ps("quatro paredes", "g", 80), XE, 490, passo=0.14)
    E.frase(c, t, c_ + 1.0, ps("inteiras, sem descontar porta", "i", 76), XE, 590, passo=0.11)
    E.frase(c, t, d_, ps("quantos metros", "i", 104), XE, 790, passo=0.15)
    E.frase(c, t, d_ + 0.6, ps("de rodapé?", "g", 104, COR), XE, 910, passo=0.15)

    def sala():
        E.foco(c, t, b_, 0.5, lambda p: piso_sala(c, x, y, l, p))
        if t >= c_:
            perimetro(c, x, y, l, l, ep(t, c_, 1.2), COR)
    E.saida(c, t, C["s04"] - 0.1, sala)
    E.relogio(c, t, C["s04.a"], 1490, 440, 200)


def b_resposta1(c, t, C, b):
    marca(c, t, C["s05"] - 0.5, 1)
    a_, b_, c_, d_, e_, f_ = (C[f"s05.{k}"] for k in "abcdef")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    s6 = C["s06"]
    d = [b_, c_, d_, e_, f_]
    tabela(c, t, T1225_TELA, [(x,) for x in d], d[1:], d[:4], G, cor_fim=CERTO if t >= f_ + 0.5 else None)
    dupla(c, t, lerp(s6, a6, 0.15), 0)
    dupla(c, t, lerp(s6, a6, 0.55), 2)
    x = 880

    def conta():
        form(c, t, a_, "lado = r{12,25}", x, 300, 104, COR)
        E.frase(c, t, lerp(a_, b_, 0.3), ps("esqueça a vírgula e fatore", "i", 72), x, 430, passo=0.11)
    E.saida(c, t, s6 - 0.1, conta)
    troca(c, t, [(c_, "1.225 ÷ 5 = 245"), (d_, "245 ÷ 5 = 49"), (e_, "49 ÷ 7 = 7"), (f_, "7 ÷ 7 = 1")], s6 - 0.1, x, 640, 88)
    if t >= s6:
        form(c, t, a6, "5 × 7 = 35", x, 300, 104)
        E.frase(c, t, lerp(a6, b6, 0.3), ps("duas casas: a raiz tem uma", "i", 70), x, 420, passo=0.11)
        form(c, t, b6, "r{12,25} = 3,5 m", x, 590, 110, COR)
        form(c, t, c6, "4 × 3,5 =", x, 840, 110)
        E.foco(c, t, d6, 0.5, lambda p: num_bola(c, "14 m", 1530, 800, 150, 96, p, CERTO, BR))


# ---------------- problema 2 ----------------
def b_questao2(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s07.{k}"] for k in "abcd")
    marca(c, t, a_, 2)
    x, y, l = 1260, 340, 440
    form(c, t, b_, "jardim quadrado: 30 m^2", XE, 330, 92, COR)
    form(c, t, c_, "tábua de 5,5 m", XE, 500, 92)
    E.frase(c, t, c_ + 0.8, ps("ao longo de um lado do jardim", "i", 72), XE, 610, passo=0.11)
    E.frase(c, t, d_, ps("a tábua cabe nesse lado,", "i", 96), XE, 790, passo=0.13)
    E.frase(c, t, d_ + 0.8, ps("sem sobrar para fora?", "g", 84, COR), XE, 910, passo=0.13)

    def desenho():
        E.foco(c, t, b_, 0.5, lambda p: gramado(c, x, y, l, l, p))
        E.foco(c, t, c_, 0.5, lambda p: tabua(c, x, y - 60, l, 42, p))
    E.saida(c, t, C["s08"] - 0.1, desenho)
    E.relogio(c, t, C["s08.a"], 1490, 440, 200)


def b_resposta2(c, t, C, b):
    marca(c, t, C["s09"] - 0.5, 2)
    a_, b_, c_, d_ = (C[f"s09.{k}"] for k in "abcd")
    form(c, t, a_, "lado = r{30}", XE, 340, 130, COR)
    form(c, t, b_, "5^2 = 25", XE, 560, 120)
    form(c, t, c_, "6^2 = 36", 900, 560, 120)
    form(c, t, d_, "5 < lado < 6", XE, 790, 130, COR)
    E.frase(c, t, lerp(d_, C["s09.end"], 0.68), ps("chega a", "i", 96), 1090, 780, passo=0.13)
    form(c, t, lerp(d_, C["s09.end"], 0.76), "5,5?", 1420, 785, 110, COR)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s10():
        a, b_, c_, d = (C[f"s10.{k}"] for k in "abcd")
        E.frase(c, t, C["s10"] + 0.1, ps("aqui entra o atalho", "i", 84, CLARO), W / 2, 170, "center")
        E.frase(c, t, a, ps("não calcule a raiz:", "i", 92, CLARO), W / 2, 290, "center", 0.12)
        E.frase(c, t, a + 0.8, ps("eleve a medida da tábua ao quadrado", "g", 72, BR), W / 2, 400, "center", 0.1)
        form(c, t, b_, "5,5 × 5,5 = 30,25", W / 2, 590, 130, BR, "center")
        form(c, t, c_ - 0.5, "30,25 > 30", 330, 760, 110, CLARO)
        E.frase(c, t, c_, ps("a tábua é maior que o lado", "i", 80, CLARO), 950, 755, passo=0.12)
        E.foco(c, t, d, 0.45, lambda p: E.selo(c, 640, 910, 66, False, p))
        E.frase(c, t, d, ps("não cabe,", "g", 100, BR) + ps("por pouco", "i", 110, CLARO), 740, 945, passo=0.15)

    def s11():
        a, b_ = C["s11.a"], C["s11.b"]
        fim = C["s11.end"]
        E.frase(c, t, C["s11"] + 0.1, ps("funciona porque", "i", 92, CLARO), W / 2, 240, "center")
        E.frase(c, t, a, ps("quanto maior a medida,", "i", 100, BR), W / 2, 380, "center", 0.13)
        E.frase(c, t, a + 0.8, ps("maior o quadrado dela", "g", 96, BR), W / 2, 510, "center", 0.13)
        E.frase(c, t, b_ - 0.5, ps("não compensa se pedir", "i", 92, CLARO), W / 2, 700, "center", 0.12)
        E.frase(c, t, b_, ps("o valor do lado", "g", 96, BR), W / 2, 820, "center", 0.13)
        E.frase(c, t, lerp(b_, fim, 0.55), ps("aí, cerque e confira", "i", 96, CLARO), W / 2, 950, "center", 0.13)

    fase(c, t, C["s10"], C["s11"] - 0.1, s10)
    fase(c, t, C["s11"], 1e9, s11)


# ---------------- problema 3 ----------------
def b_questao3(c, t, C, b):
    a_, b_, c_, d_, e_ = (C[f"s12.{k}"] for k in "abcde")
    fim = C["s12.end"]
    marca(c, t, a_, 3)
    u = 38
    l1, l2 = u * math.sqrt(32), u * math.sqrt(50)
    xc, yc = 1120, 700  # o canto esquerdo na calçada
    E.frase(c, t, b_ - 0.5, ps("dois canteiros quadrados", "i", 84), XE, 280, passo=0.12)
    form(c, t, b_, "32 m^2", XE, 410, 96, COR)
    form(c, t, c_, "e 50 m^2", 520, 410, 96, COR)
    E.frase(c, t, d_, ps("lado a lado, com um lado", "i", 76), XE, 540, passo=0.11)
    E.frase(c, t, d_ + 0.9, ps("inteiro na calçada", "i", 76), XE, 630, passo=0.11)
    E.frase(c, t, e_, ps("quantos metros de calçada", "i", 84), XE, 770, passo=0.11)
    E.frase(c, t, e_ + 0.9, ps("ocupam juntos?", "g", 80, COR), XE, 870, passo=0.11)
    E.frase(c, t, lerp(e_, fim, 0.72), ps("forma simplificada e valor aproximado", "i", 62), XE, 970, passo=0.09)

    def desenho():
        E.foco(c, t, b_, 0.5, lambda p: gramado(c, xc, yc - l1, l1, l1, p))
        E.foco(c, t, c_, 0.5, lambda p: gramado(c, xc + l1 + 6, yc - l2, l2, l2, p))
        E.foco(c, t, b_ + 0.3, 0.4, lambda p: centro(c, "32", xc + l1 / 2, yc - l1 / 2 + 24, 66, "g", TINTA, p))
        E.foco(c, t, c_ + 0.3, 0.4, lambda p: centro(c, "50", xc + l1 + 6 + l2 / 2, yc - l2 / 2 + 24, 66, "g", TINTA, p))
        E.foco(c, t, d_, 0.5, lambda p: (M.rrect(c, xc - 50, yc + 12, l1 + l2 + 106, 48, 6, CINZA, p), centro(c, "calçada", xc + (l1 + l2) / 2, yc + 130, 62, "i", TINTA2, p)))
    E.saida(c, t, C["s13"] - 0.1, desenho)
    E.relogio(c, t, C["s13.a"], 1490, 440, 200)


def b_resposta3(c, t, C, b):
    marca(c, t, C["s14"] - 0.5, 3)
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")

    def s14():
        s = 110
        form(c, t, a4, "medida = r{32} + r{50}", XE, 330, 120, COR)
        form(c, t, b4, "32 = 16 × 2", XE, 590, s)
        form(c, t, c4, "r{32} = 4r{2}", 980, 590, s, COR)
        form(c, t, d4, "50 = 25 × 2", XE, 800, s)
        form(c, t, e4, "r{50} = 5r{2}", 980, 800, s, COR)

    def s15():
        form(c, t, a5, "4r{2} + 5r{2} = 9r{2} m", XE, 320, 110, CERTO)
        form(c, t, b5, "r{2} ≈ 1,4", XE, 510, 100)
        form(c, t, c5, "9 × 1,4 = 12,6", 760, 510, 100)
        E.frase(c, t, d5, ps("um pouco mais de", "i", 84), XE, 680, passo=0.12)
        form(c, t, d5 + 0.6, "12,5 m", 860, 685, 110, CERTO)
        form(c, t, e5, "r{82} ≈ 9", XE, 900, 110, ERRADO)
        E.foco(c, t, e5 + 0.1, 0.45, lambda p: E.selo(c, 720, 860, 54, False, p))
        E.frase(c, t, e5 + 0.4, ps("quem soma direto", "i", 80), 830, 890, passo=0.12)

    fase(c, t, C["s14"], C["s15"] - 0.1, s14)
    fase(c, t, C["s15"], 1e9, s15)


# ---------------- problema 4 ----------------
def b_questao4(c, t, C, b):
    a_, b_, c_, d_, e_, f_ = (C[f"s16.{k}"] for k in "abcdef")
    marca(c, t, a_, 4)
    E.frase(c, t, a_, ps("o último, e ele junta tudo", "i", 76, COR), XE, 240, passo=0.11)
    E.frase(c, t, b_, ps("reservatório em forma de", "i", 80) + ps("cubo", "g", 80, COR), XE, 350, passo=0.11)
    E.frase(c, t, b_ + 0.7, ps("comprimento, largura e altura iguais", "i", 60), XE, 430, passo=0.08)
    form(c, t, c_, "729 m^3", XE, 570, 110, COR)
    E.frase(c, t, c_ + 0.8, ps("o volume:", "i", 60), 620, 545, passo=0.1)
    E.frase(c, t, c_ + 1.4, ps("comprimento × largura × altura", "i", 52), 620, 615, passo=0.07)
    E.frase(c, t, d_, ps("forrar", "i", 88) + ps("só o fundo,", "g", 80, CERTO), XE, 750, passo=0.13)
    E.frase(c, t, e_, ps("um quadrado", "i", 84), 850, 750, passo=0.13)
    E.frase(c, t, f_, ps("quantos", "i", 92), XE, 900, passo=0.13)
    form(c, t, f_ + 0.3, "m^2", 450, 900, 92, COR)
    E.frase(c, t, f_ + 0.5, ps("de lona?", "i", 92), 610, 900, passo=0.13)

    def desenho():
        E.foco(c, t, b_, 0.5, lambda p: reservatorio(c, 1480, 900, 290, p, ep(t, d_, 0.6)))
        E.foco(c, t, e_, 0.45, lambda p: centro(c, "fundo", 1530, 835, 62, "g", BR, p))
    E.saida(c, t, C["s17"] - 0.1, desenho)
    E.relogio(c, t, C["s17.a"], 1490, 440, 200)


def b_resposta4(c, t, C, b):
    marca(c, t, C["s18"] - 0.5, 4)
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")

    def s18():
        form(c, t, a8, "volume = lado × lado × lado", XE, 260, 84)
        form(c, t, lerp(a8, b8, 0.55), "lado = r3{729}", XE, 390, 90, COR)
        s, x, y = 100, XE, 550
        txt = "729 = 3 × 3 × 3 × 3 × 3 × 3"
        form(c, t, b8, txt, x, y, s)
        cx = lambda i: x + E.larg(txt[:i], "g", s) + E.APERTO["g"] * s + E.larg("3", "g", s) / 2
        i3 = [i for i, ch in enumerate(txt) if ch == "3" and i > 5]
        for ti, (u, v) in ((c8 + 0.5, (i3[0], i3[2])), (c8 + 0.9, (i3[3], i3[5]))):
            q = ep(t, ti, 0.45)
            E.caixa_pontilhada(c, cx(u) - 42, y - 96, cx(v) - cx(u) + 84, 118, q, COR, prog_=q)
        tq = lerp(b8, c8, 0.42)
        E.frase(c, t, tq, ps("quadrada:", "g", 72, TINTA2) + ps("2 grupos iguais", "i", 76), XE, 690, passo=0.11)
        E.frase(c, t, c8, ps("cúbica:", "g", 72, COR) + ps("3 grupos iguais, procure trios", "i", 76), XE, 785, passo=0.11)
        form(c, t, lerp(c8, d8, 0.8), "um 3 de cada trio:", XE, 925, 70, TINTA2)
        par(c, t, d8, d8 + 0.5, "3 × 3 = 9 m", "de lado", 800, 930, 100, CERTO)

    def s19():
        form(c, t, a9, "fundo = lado × lado", XE, 300, 92)
        form(c, t, b9, "9 × 9 = 81 m^2", XE, 480, 120, CERTO)
        E.frase(c, t, lerp(b9, c9, 0.35), ps("raiz cúbica,", "g", 72, COR) + ps("depois ao quadrado:", "i", 76), XE, 630, passo=0.11)
        form(c, t, c9, "729^{2/3}", XE, 800, 130, COR)
        E.frase(c, t, lerp(c9, d9, 0.35), ps("de baixo: raiz", "i", 70), 800, 740, passo=0.1)
        E.frase(c, t, lerp(c9, d9, 0.6), ps("de cima: potência", "i", 70), 800, 830, passo=0.1)
        form(c, t, d9, "9 × 9 × 9 = 729", XE, 960, 96, CERTO)
        E.foco(c, t, d9 + 0.3, 0.45, lambda p: E.selo(c, 1060, 925, 50, True, p))

    fase(c, t, C["s18"], C["s19"] - 0.1, s18)
    fase(c, t, C["s19"], 1e9, s19)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s20.a", ps("área de quadrado chama", "i", 80) + ps("raiz quadrada", "g", 72, COR)),
                 (590, "s20.b", ps("volume de cubo chama", "i", 80) + ps("raiz cúbica", "g", 72, COR)),
                 (780, "s20.c", ps("não exata só soma com", "i", 80) + ps("o mesmo número dentro", "g", 62, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p: num_bola(c, str(i + 1), 230, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 320, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a_, b_, c_, d_ = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("notação", "g", 120, COR), XE, 390)
    E.frase(c, t, a_ + 0.3, ps("científica", "g", 120, COR), XE, 520)
    E.frase(c, t, lerp(a_, b_, 0.4), ps("número enorme ou muito pequeno", "i", 76), XE, 640, passo=0.11)
    E.frase(c, t, b_, ps("com potência de dez", "g", 76, COR), XE, 750, passo=0.13)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1460, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1610, p), lerp(650, 405, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
