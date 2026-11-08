"""Visual — Estudativo · MAT-RAZ-011: ler uma fórmula como proporcionalidade.
Peças locais: o fio elétrico (corpo e corte na ponta) que fica mais comprido e mais fino, a fórmula grande com a legenda de
cada letra, pílulas com o fator de cada mudança e, para manter a linguagem da trilha, a mesma tabela/seta das outras aulas.
Todo instante vem de C[...]: sem voz, os tempos são provisórios e o visual segue os marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-011_formula_como_proporcionalidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cima", "fio", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 120 / 40 == 3 and 120 / 80 == 1.5
assert 1 * 2 / Fr(1, 2) == 4 and 2 * Fr(1, 2) == 1 and Fr(2 ** 2, 2) == 2 and Fr(3 ** 2, 3) == 3


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


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


# --- tabela da regra de três (mesma linguagem em toda a trilha) ---
DY3 = 150  # distância entre as linhas da tabela


def cabeca(c, t, t0, nome, cx, y, size=56, cor=None, larg=300):
    """nome da grandeza, em itálico, com o fio embaixo"""
    E.foco(c, t, t0, 0.5, lambda a: (centro(c, nome, cx, y, size, "i", cor or TINTA2, a),
                                      M.line(c, cx - larg / 2, y + 34, cx + larg / 2, y + 34, FIO, a, 3)))


def coluna(c, t, cx, y, vals, vira=None, size=110, giro=1):
    """valores de uma coluna: vals = [(texto, cor, t0), ...], linha i na altura y + DY3*(i+1).
    vira = instante em que a coluna vira de cabeça para baixo (os dois valores trocam de linha, num arco)"""
    p = ease_io(prog(t, vira, 0.9)) if vira is not None else 0.0
    n = len(vals)
    for i, (s, cor, t0) in enumerate(vals):
        yi, yj = y + DY3 * (i + 1), y + DY3 * (n - i)
        yy = lerp(yi, yj, p)
        xx = cx + math.sin(math.pi * p) * 90 * (giro if i == 0 else -giro)
        fcen(c, t, t0, s, xx, yy + size * 0.36, size, cor)


def seta(c, t, t0, x, y, desce=True, cor=None, a=1.0, n=2):
    """seta vertical ao lado da coluna, da 1ª à última linha (desce) ou ao contrário (sobe)"""
    p = ep(t, t0, 0.6) * a
    if p <= 0:
        return
    ya, yb = y + DY3 - 40, y + DY3 * n + 40
    if not desce:
        ya, yb = yb, ya
    M.arrow(c, x, ya, x, yb, cor or COR, p, 7, 26, ease_io(prog(t, t0, 0.6)))


def cruz(c, t, t0, xa, xb, y, cor=None, fundo=None):
    """produto cruzado entre duas frações em xa e xb (barra em y): duas diagonais, com o = limpo no meio"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.line(c, xa + 60, y - 90, xb - 60, y + 110, cor or E.COR, 1.0, 7, progress=p)
    M.line(c, xa + 60, y + 110, xb - 60, y - 90, cor or E.COR, 1.0, 7, progress=p)
    c.drawCircle((xa + xb) / 2, y + 8, 46, M.paint(fundo or E.PAPEL))


def tipo(c, t, t0, s, cx, cy, cor=None, size=48, escuro=False):
    """pílula com o tipo da relação (direta / inversa)"""
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor or E.COR, cor=E.SOBRE, a=a))


def pessoa(c, cx, base, h, cor=None, a=1.0):
    """bonequinho: cabeça e corpo arredondado"""
    if a <= 0:
        return
    cor = cor or E.COR
    r = h * 0.18
    c.drawCircle(cx, base - h + r, r, M.paint(cor, a))
    w = h * 0.56
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, base - h * 0.58, w, h * 0.58), w * 0.42, w * 0.42), M.paint(cor, a))


def turma(c, t, t0, n, x, base, h=90, gap=22, cor=None, passo=0.08):
    """n bonecos lado a lado, a partir de x; entram um por um"""
    for i in range(n):
        E.foco(c, t, t0 + i * passo, 0.4, lambda a, i=i: pessoa(c, x + i * (h * 0.56 + gap) + h * 0.28, base, h, cor, a))
    return n * (h * 0.56 + gap) - gap


CLARA = E.mix(E.COR, "#FFFFFF", 0.5)


def fio(c, x, cy, comp, r, a=1.0, cor=None):
    """fio elétrico deitado: corpo arredondado e o corte (a bolinha) na ponta direita"""
    if a <= 0:
        return
    cor = cor or E.COR
    M.rrect(c, x, cy - r, comp, 2 * r, r * 0.5, cor, a)
    M.rrect(c, x + r * 0.4, cy - r * 0.55, comp - r * 0.8, r * 0.22, r * 0.11, "#FFFFFF", 0.25 * a)
    ov = skia.Rect.MakeXYWH(x + comp - r * 0.45, cy - r, r * 0.9, 2 * r)
    c.drawOval(ov, M.paint(CLARA, a))
    c.drawOval(ov, M.paint(TINTA, a, stroke=3))


def larg_f(s, size):
    return E.formula(None, s, 0, 0, size, a=0)


def no_formula(s, prefixo, cx, size):
    """x do começo da fórmula centrada em cx e o x logo depois de `prefixo`"""
    x0 = cx - larg_f(s, size) / 2
    return x0, x0 + (larg_f(prefixo, size) if prefixo else 0)


def selo_txt(c, t, t0, txt, cx, cy, size=50, fundo=None, cor=BR):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, txt, cx, cy, size, "g", fundo=fundo or E.COR, cor=cor, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        muda = ease_io(prog(t, lerp(ka, kb, 0.35), 1.2))
        comp, r = lerp(520, 1040, muda), lerp(70, 70 / math.sqrt(2), muda)
        E.foco(c, t, ka, 0.6, lambda a: fio(c, 300, 380, comp, r, a))
        E.foco(c, t, lerp(ka, kb, 0.35), 0.5, lambda a: E.pilula(c, "comprimento × 2", 820, 230, 50, "g", a=a, cor=E.SOBRE))
        E.foco(c, t, lerp(ka, kb, 0.6), 0.5, lambda a: E.pilula(c, "área do corte ÷ 2", 1340, 530, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, kb - 0.6, ps("a dificuldade para passar", "i", 70), 560, 720, "center", 0.1)
        if t < kc:
            E.foco(c, t, kb, 0.5, lambda a: centro(c, "igual?", 1100, 730, 90, "g", CINZA, a))
        else:
            E.foco(c, t, kc, 0.5, lambda a: (centro(c, "× 4", 1100, 750, 150, "g", COR, a)))
        E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "sem nenhum número do fio", W / 2, 930, 54, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), ps("ler uma", "i", 90) + [("fórmula", "g", 104, COR)], XE, 450, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("e dizer o que", "i", 84), XE, 580, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.65), [("acontece", "g", 96, COR)], XE, 710)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("lembre de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "distância =", "velocidade × tempo"), ("s03.c", "dividir por um meio", "é multiplicar por 2"),
             ("s03.d", "dobrar o lado do quadrado", "quadruplica a área"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 160)
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 580, q1), 820, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- letra que multiplica ----------------
def b_cima(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    s, size, cx, y = "d = v · t", 170, W / 2, 400
    fcen(c, t, a4, s, cx, y, size, TINTA)
    E.foco(c, t, a4 + 0.6, 0.5, lambda a: centro(c, "distância = velocidade × tempo", cx, y + 110, 52, "i", TINTA2, a))
    x0, xt = no_formula(s, "d = v · ", cx, size)
    xt += larg_f("t", size) / 2
    xd = x0 + larg_f("d", size) / 2
    selo_txt(c, t, b4, "× 2", xt, y - 220, 60)
    E.foco(c, t, b4 + 0.6, 0.5, lambda a: centro(c, "2 h vira 4 h", xt, y - 300, 48, "g", TINTA2, a))
    selo_txt(c, t, c4, "× 2", xd, y - 220, 60)
    E.foco(c, t, b4 + 0.3, 0.5, lambda a: centro(c, "v fixa", (xd + xt) / 2 + 20, y - 220, 46, "i", TINTA2, a))
    E.frase(c, t, d4, ps("a letra que multiplica:", "i", 70) + [("direta", "g", 76, COR)], W / 2, 800, "center", 0.12)


# ---------------- letra que divide ----------------
def b_baixo(c, t, C, b):
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]

    def tempo():
        fcen(c, t, a5, "t = f{d}{v}", 520, 470, 170, TINTA)
        fcen(c, t, b5, "f{120}{40} = 3 h", 1360, 380, 100, TINTA)
        fcen(c, t, c5, "f{120}{80} = 1,5 h", 1360, 620, 100, TINTA)
        selo_txt(c, t, d5, "v × 2", 1150, 820, 60, TINTA)
        E.foco(c, t, d5 + 0.3, 0.5, lambda a: E.escreve(c, "t ÷ 2", 1360, 842, 72, "g", COR, a))
    E.saida(c, t, C["s06"] - 0.1, tempo)
    if t < C["s06"]:
        return
    E.frase(c, t, a6, ps("a letra de baixo:", "i", 70) + [("inversa", "g", 76, COR)], W / 2, 200, "center", 0.12)
    # a fração-modelo: em cima / embaixo
    cx, cy = 560, 560
    E.foco(c, t, b6 - 0.4, 0.5, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 220, cy - 8, 440, 16), 8, 8), M.paint(TINTA, a)))
    E.foco(c, t, b6, 0.5, lambda a: centro(c, "em cima", cx, cy - 70, 90, "g", TINTA, a))
    E.foco(c, t, c6, 0.5, lambda a: centro(c, "embaixo", cx, cy + 130, 90, "g", TINTA, a))
    E.frase(c, t, b6 + 0.2, ps("direto", "g", 96, COR), 960, cy - 70, passo=0.1)
    E.frase(c, t, c6 + 0.2, ps("inverso", "g", 96, COR), 960, cy + 130, passo=0.1)
    E.frase(c, t, d6, ps("ao quadrado:", "i", 70) + ps("o fator vai ao quadrado", "g", 70, COR), W / 2, 860, "center", 0.12)
    E.foco(c, t, d6 + 1.4, 0.5, lambda a: E.formula(c, "lado × 2: área × 2^2 = 4", W / 2, 970, 60, "g", TINTA2, a, "center"))


# ---------------- a fórmula do fio ----------------
FIO_F, FS, FCX, FY = "R = k · f{L}{A}", 170, 470, 560


def b_fio(c, t, C, b):
    a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]
    a8, b8 = C["s08.a"], C["s08.b"]
    fcen(c, t, a7, FIO_F, FCX, FY, FS, TINTA)
    x0, xf = no_formula(FIO_F, "R = k · ", FCX, FS)
    xf_d = xf + larg_f("f{L}{A}", FS)

    def legenda():
        X = 980
        linhas = (("R", "resistência:", "o quanto o fio dificulta a corrente", b7), ("L", "comprimento", "do fio", c7),
                  ("A", "área do corte", "a bolinha do fio cortado", d7), ("k", "número fixo", "depende do material", e7))
        for i, (letra, l1, l2, t0) in enumerate(linhas):
            y = 250 + i * 190
            E.foco(c, t, t0, 0.5, lambda a, letra=letra, y=y: (E.bola(c, X, y - 26, 50, a=a), centro(c, letra, X, y - 4, 64, "g", E.SOBRE, a)))
            E.frase(c, t, t0 + 0.1, [(l1, "g", 56)], X + 80, y - 16)
            E.frase(c, t, t0 + 0.3, ps(l2, "i", 50, TINTA2), X + 80, y + 44, passo=0.06)
        E.foco(c, t, d7 + 0.4, 0.5, lambda a: fio(c, 1650, 650 - 26, 160, 34, a))
    E.saida(c, t, C["s08"] + 1.0, legenda)
    E.foco(c, t, C["s08"] + 1.4, 0.5, lambda a: centro(c, "a física fica para outra aula", FCX, 880, 44, "i", TINTA2, a * (1 - ep(t, C["s09"], 0.4))))
    # em cima: direto; embaixo: inverso
    selo_txt(c, t, a8, "direto", xf_d + 130, FY - 100, 50)
    selo_txt(c, t, b8, "inverso", xf_d + 140, FY + 110, 50, TINTA)
    if t < C["s09"]:
        return
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    XR = 1430
    E.frase(c, t, a9, ps("uma mudança", "i", 66) + ps("de cada vez", "g", 66, COR), XR, 220, "center", 0.12)
    fcen(c, t, b9, "L × 2:  R × 2", XR, 380, 84, TINTA)
    fcen(c, t, c9, "A × f{1}{2}:  R ÷ f{1}{2}", XR, 540, 84, TINTA)
    fcen(c, t, d9, "÷ f{1}{2} = × 2", XR, 700, 84, COR)
    fcen(c, t, a10, "× 2 · 2", XR - 120, 860, 90, TINTA)
    E.foco(c, t, b10, 0.5, lambda a: E.pilula(c, "R × 4", XR + 210, 830, 72, "g", cor=E.SOBRE, a=a))
    E.frase(c, t, c10, ps("mais comprido e mais fino:", "i", 54), FCX, 860, "center", 0.08)
    E.frase(c, t, c10 + 1.0, ps("mais difícil passar", "g", 56, COR), FCX, 940, "center", 0.08)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    E.frase(c, t, C["s11"] + 0.2, ps("o erro:", "i", 70) + ps("tratar a de baixo como de cima", "g", 64, ERRADO), XE, 170, passo=0.1)
    fcen(c, t, a11, FIO_F, 470, 520, 150, TINTA)
    XR = 1320

    def errado():
        fcen(c, t, b11, "L × 2:  × 2", XR, 380, 80, TINTA)
        fcen(c, t, c11, "A × f{1}{2}:  × f{1}{2}", XR, 540, 80, ERRADO)
        fcen(c, t, d11, "2 · f{1}{2} = 1", XR, 720, 90, ERRADO)
        E.foco(c, t, d11 + 0.8, 0.5, lambda a: centro(c, "não muda?", XR, 830, 64, "i", ERRADO, a))
        if t >= a12:
            E.risco(c, XR - 260, 760, XR + 260, 640, t, a12, largura=12)
    E.saida(c, t, b12 - 0.2, errado)
    E.foco(c, t, a12, 0.5, lambda a: E.pilula(c, "A divide", 470, 760, 64, "g", fundo=TINTA, a=a))
    if t >= b12 - 0.2:
        E.frase(c, t, b12, ps("diminuir o de baixo", "i", 70), XR + 60, 440, "center", 0.12)
        E.frase(c, t, b12 + 1.0, ps("aumenta o resultado", "g", 76, COR), XR + 60, 540, "center", 0.12)
        E.foco(c, t, c12, 0.5, lambda a: E.pilula(c, "veja o lado da fração", XR + 60, 720, 64, "g", cor=E.SOBRE, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]

    def um():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho:", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, a13, ps("troque cada letra", "i", 80, CLARO) + ps("pelo fator", "g", 80, BR), W / 2, 290, "center", 0.12)
        fcen(c, t, a13 + 0.8, FIO_F, 560, 560, 150, CLARO)
        E.foco(c, t, b13, 0.5, lambda a: centro(c, "k e o que não muda: 1", 560, 760, 52, "i", CLARO, a))
        fcen(c, t, c13, "1 · 2 ÷ f{1}{2}", 1340, 560, 120, BR)
        E.foco(c, t, d13, 0.5, lambda a: (E.bola(c, 1340, 780, 100, a=a), centro(c, "4", 1340, 820, 110, "g", BR, a)))
    E.saida(c, t, C["s14"] - 0.1, um)

    def dois():
        a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
        E.frase(c, t, a14, ps("só os fatores", "g", 72, BR) + ps("decidem", "i", 72, CLARO), W / 2, 200, "center", 0.12)
        fcen(c, t, b14, "y = k · f{x^2}{z}", 560, 520, 140, CLARO)
        E.foco(c, t, b14 + 1.0, 0.5, lambda a: centro(c, "x e z dobram", 560, 720, 56, "i", CLARO, a))
        fcen(c, t, c14, "f{2^2}{2}", 1240, 520, 130, BR)
        fcen(c, t, d14, "= f{4}{2} = 2", 1540, 520, 110, BR)
        E.foco(c, t, d14 + 0.8, 0.5, lambda a: E.pilula(c, "o resultado dobra", 1420, 760, 60, "g", cor=BR, a=a))
    if t >= C["s14"]:
        E.saida(c, t, C["s15"] - 0.1, dois)

    if t >= C["s15"]:
        a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, a15, ps("não vale com", "i", 80, CLARO) + ps("parte somada", "g", 80, BR), W / 2, 260, "center", 0.12)
        E.foco(c, t, b15, 0.5, lambda a: centro(c, "táxi: bandeirada + quilômetros", W / 2, 470, 70, "g", BR, a))
        E.frase(c, t, b15 + 1.4, ps("km × 2, preço × 2?", "g", 70, ERRADO), W / 2, 600, "center", 0.1)
        E.foco(c, t, b15 + 2.6, 0.5, lambda a: centro(c, "a bandeirada não muda", W / 2, 700, 56, "i", CLARO, a))
        E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "faça a conta com números", W / 2, 860, 66, "g", cor=BR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.formula_em(c, t, a16, "y = k · f{x^2}{z}", XE, 450, 150, "g", TINTA)
    selo_txt(c, t, b16, "x × 3", 330, 680, 60)
    selo_txt(c, t, c16, "z × 3", 640, 680, 60, TINTA)
    E.frase(c, t, d16, ps("e o", "i", 84) + ps("y?", "g", 90, COR), XE, 900, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1450, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    a19, b19 = C["s19.a"], C["s19.b"]
    E.formula_em(c, t, C["s18"], "y = k · f{x^2}{z}", XE, 400, 130, "g", TINTA)
    XR = 1340
    fcen(c, t, a18, "x em cima, ao quadrado: 3^2 = 9", XR, 300, 66, TINTA)
    fcen(c, t, b18, "z embaixo: ÷ 3", XR, 440, 66, TINTA)
    fcen(c, t, c18, "9 ÷ 3 = 3", XR, 600, 100, COR)
    E.foco(c, t, d18, 0.5, lambda a: E.pilula(c, "y fica 3 vezes maior", XR, 760, 66, "g", fundo=CERTO, cor=BR, a=a))
    E.frase(c, t, a19, ps("x e z triplicaram,", "i", 60) + ps("e y mudou", "g", 60, COR), XE, 700, passo=0.1)
    E.frase(c, t, b19, ps("nada muda?", "i", 60) + ps("esqueceu o x²", "g", 60, ERRADO), XE, 860, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s20.a", "em cima, direto"), ("s20.b", "embaixo, inverso"), ("s20.c", "ao quadrado: fator²"), ("s20.d", "multiplique os efeitos"))
        for i, (k, s) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 52, a=a),
                                                          centro(c, str(i + 1), 330, y - 8, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 80)], 430, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s21.a"], [("praticando", "g", 140, COR)], XE, 460)
    E.frase(c, t, C["s21.b"], ps("tipo de relação · regra de três", "i", 70), XE, 590, passo=0.12)
    E.frase(c, t, C["s21.b"] + 1.4, ps("simples e composta", "i", 70), XE, 680, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1530, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1660, p), lerp(560, 360, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cima=b_cima, baixo=b_baixo, fio=b_fio, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
