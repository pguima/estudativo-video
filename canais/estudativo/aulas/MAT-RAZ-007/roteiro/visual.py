"""Visual — Estudativo · MAT-RAZ-007: regra de três inversa.
Peças locais: a tabela da regra de três (coluna com nome em itálico e fio embaixo, valores grandes, xis na cor da matéria,
seta ao lado de cada coluna: setas no mesmo sentido = direta, em sentidos opostos = inversa), a coluna que vira de cabeça
para baixo, bonecos de pintor e a grade de 36 quadradinhos (dias de trabalho de um pintor) que se rearruma em 4×9, 1×36 e 6×6.
Todo instante vem de C[...]: sem voz, os tempos são provisórios e o visual segue os marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-007_regra_de_tres_inversa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "metodo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 4 * 9 == 36 == 6 * 6 and 36 / 6 == 6
assert 4 * 13.5 == 9 * 6 == 54
assert 60 * 4 == 240 == 80 * 3
assert 5 * 6 == 30 == 3 * 10


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


# --- grade de 36 dias de trabalho ---
GRADE = {(4, 9): 84, (1, 36): 44, (6, 6): 74}  # (linhas, colunas): passo


def _pos(i, lay, cx, cy):
    lin, col = lay
    st = GRADE[lay]
    r, k = divmod(i, col)
    return cx - (col * st) / 2 + k * st + st / 2, cy - (lin * st) / 2 + r * st + st / 2, st * 0.84


def grade(c, t, cx, cy, lays, a=1.0, t_enche=None):
    """36 quadradinhos; lays = [(layout, t0)] em ordem: muda de arrumação em cada t0. t_enche = os quadradinhos entram em sequência"""
    if a <= 0:
        return
    for i in range(36):
        if t_enche is not None:
            q = ep(t, t_enche + i * 0.045, 0.25)
            if q <= 0:
                continue
        else:
            q = 1.0
        x, y, s = _pos(i, lays[0][0], cx, cy)
        for lay, t0 in lays[1:]:
            p = ease_io(prog(t, t0 + (i % 9) * 0.02, 0.9))
            if p <= 0:
                break
            x2, y2, s2 = _pos(i, lay, cx, cy)
            x, y, s = lerp(x, x2, p), lerp(y, y2, p), lerp(s, s2, p)
        M.rrect(c, x - s / 2, y - s / 2, s, s, s * 0.18, E.COR, a * q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.frase(c, t, ka, ps("4 pintores", "g", 84, TINTA), 300, 300)
        turma(c, t, ka + 0.4, 4, 300, 420, 92)
        E.frase(c, t, ka + 1.2, ps("pintam a casa em", "i", 72), 820, 300)
        E.foco(c, t, lerp(ka, kb, 0.75), 0.5, lambda a: centro(c, "9 dias", 1520, 420, 120, "g", COR, a))
        E.frase(c, t, kb, ps("6 pintores", "g", 84, TINTA), 300, 590)
        turma(c, t, kb + 0.4, 6, 300, 710, 92)
        if t < kc:
            E.foco(c, t, kb + 0.8, 0.5, lambda a: centro(c, "? dias", 1520, 710, 120, "g", CINZA, a))
        else:
            E.foco(c, t, kc, 0.5, lambda a: centro(c, "13,5 dias", 1520, 710, 120, "g", ERRADO, a))
            E.frase(c, t, kc + 1.2, ps("mais gente,", "i", 76) + ps("obra mais lenta?", "g", 70, ERRADO), W / 2, 920, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("regra de três", "g", 104, COR)], XE, 450)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("uma grandeza", "i", 84) + [("sobe", "g", 84, COR)], XE, 590, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.65), ps("a outra", "i", 84) + [("desce", "g", 84, COR)], XE, 710, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("lembre de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "o teste do dobro", "direta ou inversa?"), ("s03.c", "a regra de três direta", "tabela e produto cruzado"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 710, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- por que o produto não muda ----------------
def b_ideia(c, t, C, b):
    # 1. teste do dobro
    def dobro():
        E.frase(c, t, C["s04"] + 0.2, ps("teste do", "i", 90) + [("dobro", "g", 90, COR)], W / 2, 200, "center", 0.14)
        a4 = C["s04.a"]
        cabeca(c, t, a4, "pintores", 640, 360, 64)
        cabeca(c, t, a4, "dias", 1280, 360, 64)
        E.foco(c, t, a4 + 0.4, 0.5, lambda a: centro(c, "× 2", 640, 560, 150, "g", COR, a))
        p = ep(t, a4 + 0.4, 0.6)
        M.arrow(c, 800, 640, 800, 440, COR, p, 9, 32, p)
        E.foco(c, t, lerp(a4, C["s04.b"], 0.55), 0.5, lambda a: centro(c, "÷ 2", 1280, 560, 150, "g", TINTA, a))
        q = ep(t, lerp(a4, C["s04.b"], 0.55), 0.6)
        M.arrow(c, 1440, 440, 1440, 640, TINTA, q, 9, 32, q)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.pilula(c, "inversa", W / 2, 840, 96, "g", cor=E.SOBRE, a=a))
    E.saida(c, t, C["s05"] - 0.1, dobro)

    # 2. o trabalho todo: 36 dias de trabalho de um pintor
    def trabalho():
        a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
        a6, b6 = C["s06.a"], C["s06.b"]
        if t < a6 - 0.2:
            E.saida(c, t, a5 - 0.1, lambda: E.frase(c, t, C["s05"] + 0.2, ps("o trabalho", "i", 84) + [("todo", "g", 84, COR)], W / 2, 170, "center", 0.14))
        if t >= a5:
            E.saida(c, t, b5, lambda: E.frase(c, t, a5 + 0.3, [("4", "g", 72, COR)] + ps("pintores ×", "i", 66) + [("9", "g", 72, COR)] + ps("dias", "i", 66),
                                           W / 2, 170, "center", 0.12))
        if t >= b5:
            E.saida(c, t, a6 - 0.1, lambda: E.frase(c, t, b5, [("1", "g", 72, COR)] + ps("pintor sozinho:", "i", 66) + [("36", "g", 72, COR)] + ps("dias", "i", 66),
                                                    W / 2, 170, "center", 0.12))
        if t >= a6:
            E.frase(c, t, a6, [("36", "g", 72, COR)] + ps("dias de trabalho ÷", "i", 66) + [("6", "g", 72, COR)] + ps("pintores", "i", 66), W / 2, 170, "center", 0.12)
        # bonecos à esquerda de cada linha da grade
        def linha_bonecos(lay, t_in, t_out):
            def f():
                for r in range(lay[0]):
                    _, y, s = _pos(r * lay[1], lay, 960, 500)
                    x0, _, _ = _pos(r * lay[1], lay, 960, 500)
                    E.foco(c, t, t_in + r * 0.08, 0.4, lambda a, y=y, x0=x0, s=s: pessoa(c, x0 - s * 1.1, y + s * 0.45, s * 0.95, TINTA, a))
            if t_out is None:
                f()
            else:
                E.saida(c, t, t_out, f, 0.3)
        linha_bonecos((4, 9), a5 + 0.2, b5 - 0.1)
        linha_bonecos((1, 36), b5 + 1.0, a6 - 0.1)
        linha_bonecos((6, 6), a6 + 1.0, None)
        grade(c, t, 960, 500, [((4, 9), 0), ((1, 36), b5), ((6, 6), a6)], t_enche=a5)
        if t < a6 - 0.2:
            E.saida(c, t, b5 - 0.1, lambda: fcen(c, t, a5 + 1.8, "4 · 9 = 36", W / 2, 790, 96, TINTA))
        E.saida(c, t, a6 - 0.1, lambda: E.foco(c, t, c5, 0.5, lambda a: E.pilula(c, "o total não muda", W / 2, 800, 70, "g", cor=E.SOBRE, a=a)))
        if t >= a6:
            fcen(c, t, a6 + 0.6, "36 ÷ 6 =", 880, 870, 96, TINTA)
            E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "6 dias", 1240, 836, 80, "g", cor=E.SOBRE, a=a))
    if C["s05"] <= t:
        E.saida(c, t, C["s06.c"] - 0.1, trabalho)

    # 3. faz sentido + o mesmo caminho do preço de um quilo
    def sentido():
        c6, d6 = C["s06.c"], C["s06.d"]
        E.frase(c, t, c6, ps("mais pintores,", "i", 96) + [("menos dias", "g", 96, COR)], W / 2, 330, "center", 0.12)
        E.foco(c, t, c6 + 0.4, 0.5, lambda a: E.selo(c, W / 2, 500, 70, True, a))
        E.frase(c, t, d6 - 1.8, ps("como o preço de", "i", 70) + [("1 quilo", "g", 70)], W / 2, 720, "center", 0.12)
        E.frase(c, t, d6, ps("primeiro,", "i", 70) + [("1 pintor só", "g", 76, COR)], W / 2, 850, "center", 0.12)
    if C["s06.c"] <= t:
        E.saida(c, t, C["s07"] - 0.1, sentido)

    # 4. a marca da inversa
    if t >= C["s07"]:
        E.frase(c, t, C["s07"] + 0.2, ps("a marca da", "i", 84) + [("inversa", "g", 84, COR)], W / 2, 200, "center", 0.14)
        E.foco(c, t, C["s07.a"], 0.5, lambda a: E.formula(c, "pintores · dias = sempre igual", W / 2, 400, 80, "b", TINTA, a, "center"))
        fcen(c, t, C["s07.b"], "4 · 9 = 36", W / 2, 620, 130, TINTA)
        fcen(c, t, C["s07.c"], "6 · 6 = 36", W / 2, 820, 130, TINTA)
        w = E.formula(c, "4 · 9 = 36", 0, 0, 130, a=0)
        E.foco(c, t, C["s07.c"] + 0.6, 0.5, lambda a: E.caixa_pontilhada(c, W / 2 + w / 2 - 205, 510, 230, 360, a, E.COR))


# ---------------- método das colunas ----------------
XP, XD, YT = 430, 830, 300  # colunas pintores e dias, linha do nome


def tabela_pintores(c, t, C, vira=None, cor_x=None):
    cabeca(c, t, C["s08.a"], "pintores", XP, YT)
    cabeca(c, t, C["s08.a"] + 0.2, "dias", XD, YT)
    coluna(c, t, XP, YT, [("4", TINTA, C["s08.b"]), ("6", TINTA, C["s08.b"] + 0.5)], vira)
    coluna(c, t, XD, YT, [("9", TINTA, C["s08.c"]), ("x", cor_x or COR, C["s08.c"] + 0.5)])


def b_metodo(c, t, C, b):
    E.frase(c, t, C["s08"] + 0.2, ps("monte a", "i", 80) + [("tabela", "g", 80, COR)], XE, 170, passo=0.14)
    a9, b9 = C["s09.a"], C["s09.b"]
    tabela_pintores(c, t, C, vira=a9 + 0.8)
    # setas: dias desce; pintores sobe (inversa) e, depois de virar, desce também
    seta(c, t, C["s09"] + 0.3, XD + 130, YT)
    vira = ep(t, a9 + 0.8, 0.9)
    seta(c, t, C["s09"] + 0.6, XP + 130, YT, desce=False, cor=TINTA, a=1 - vira)
    seta(c, t, a9 + 1.5, XP + 130, YT, desce=True, cor=TINTA)
    tipo(c, t, C["s09"] + 0.8, "inversa", 630, 830)
    E.foco(c, t, a9, 0.5, lambda a: E.caixa_pontilhada(c, XP - 150, YT + 70, 300, 330, a * (1 - ep(t, b9, 0.4)), E.COR))
    E.foco(c, t, a9 + 0.2, 0.5, lambda a: centro(c, "vire a coluna sem o x", XP + 200, 960, 52, "i", COR, a * (1 - ep(t, b9, 0.4))))

    # direita: 9/x = 6/4, produto cruzado
    xa, xb, y = 1300, 1600, 470
    E.foco(c, t, b9, 0.5, lambda a: E.fracao(c, 9, "x", xa, y, 120, TINTA, a))
    E.foco(c, t, b9 + 0.5, 0.5, lambda a: E.fracao(c, 6, 4, xb, y, 120, TINTA, a))
    cruz(c, t, C["s10.a"], xa, xb, y)
    E.foco(c, t, b9 + 0.3, 0.5, lambda a: centro(c, "=", (xa + xb) / 2, y + 40, 110, "g", TINTA, a))
    fcen(c, t, C["s10.b"], "6 · x = 4 · 9 = 36", 1450, 730, 84, TINTA)
    fcen(c, t, C["s10.c"], "x = 36 ÷ 6", 1360, 880, 84, TINTA)
    bola_res(c, t, C["s10.d"], "6", 1700, 850, 100, 110)
    E.foco(c, t, C["s10.d"] + 0.3, 0.5, lambda a: centro(c, "dias", 1700, 1010, 56, "i", TINTA, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    E.frase(c, t, C["s11"] + 0.2, ps("de onde saiu o", "i", 80) + [("13,5?", "g", 80, ERRADO)], XE, 170, passo=0.14)
    cabeca(c, t, a11, "pintores", XP, YT)
    cabeca(c, t, a11 + 0.2, "dias", XD, YT)
    coluna(c, t, XP, YT, [("4", TINTA, a11 + 0.4), ("6", TINTA, a11 + 0.6)])
    coluna(c, t, XD, YT, [("9", TINTA, a11 + 0.5), ("x", COR, a11 + 0.7)])
    seta(c, t, a11 + 1.0, XP + 130, YT, cor=ERRADO)
    seta(c, t, a11 + 1.0, XD + 130, YT, cor=ERRADO)
    tipo(c, t, a11 + 1.3, "montou direta", 630, 830, ERRADO)
    fcen(c, t, b11, "4 · x = 9 · 6 = 54", 1430, 520, 84, TINTA)
    fcen(c, t, c11, "x = 13,5", 1430, 680, 110, ERRADO)
    if t >= C["s12.a"]:
        E.risco(c, XP - 170, YT + 380, XD + 200, YT + 40, t, C["s12.a"], largura=16)
    E.frase(c, t, C["s12.a"] + 0.4, ps("a conta está certa,", "i", 54) + ps("a montagem não", "g", 54, ERRADO), 1430, 830, "center", 0.1)

    if t >= C["s12.b"]:
        E.frase(c, t, C["s12.b"], ps("mais gente,", "i", 64) + [("mais dias?", "g", 64, ERRADO)], 640, 990, "center", 0.12)
        E.foco(c, t, C["s12.b"] + 1.6, 0.5, lambda a: E.selo(c, 1060, 968, 46, False, a))
        E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "3 segundos", 1430, 968, 54, "g", cor=E.SOBRE, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def linhas():
        E.frase(c, t, C["s13"] + 0.2, ps("o atalho:", "i", 80, CLARO), W / 2, 190, "center", 0.12)
        E.frase(c, t, C["s13.a"], ps("na inversa,", "i", 92, CLARO) + ps("multiplique na linha", "g", 92, BR), W / 2, 320, "center", 0.12)
        b13, c13 = C["s13.b"], C["s13.c"]
        cabeca(c, t, b13 - 0.3, "pintores", 520, 450, 52, CLARO, 260)
        cabeca(c, t, b13 - 0.3, "dias", 860, 450, 52, CLARO, 260)
        for i, (n, d, t0) in enumerate((("4", "9", b13), ("6", "x", c13))):
            y = 450 + DY3 * (i + 1) + 40
            fcen(c, t, t0, n, 520, y, 110, BR)
            fcen(c, t, t0 + 0.3, d, 860, y, 110, CLARO if d == "x" else BR)
            p = ep(t, t0 + 0.5, 0.5)
            if p > 0:  # a faixa da linha: multiplica na horizontal
                M.rrect(c, 420, y - 120, 540, 150, 75, CLARO, 0.16 * p)
                centro(c, "×", 690, y - 22, 64, "g", CLARO, p)
        fcen(c, t, c13 + 0.4, "4 · 9 = 6 · x", 1420, 560, 100, BR)
        fcen(c, t, C["s13.d"], "36 = 6x", 1420, 720, 100, BR)
        E.foco(c, t, C["s13.e"], 0.5, lambda a: (E.bola(c, 1420, 880, 95, a=a), E.formula(c, "x = 6", 1420, 908, 72, "g", BR, a, "center")))
    E.saida(c, t, C["s14"] - 0.1, linhas)

    def porque():
        E.frase(c, t, C["s14.a"], ps("cada linha =", "i", 80, CLARO) + ps("trabalho total", "g", 80, BR), W / 2, 220, "center", 0.12)
        b14, c14, d14 = C["s14.b"], C["s14.c"], C["s14.d"]
        cabeca(c, t, b14, "km/h", 520, 380, 52, CLARO, 260)
        cabeca(c, t, b14, "horas", 860, 380, 52, CLARO, 260)
        fcen(c, t, b14 + 0.3, "60", 520, 570, 110, BR)
        fcen(c, t, b14 + 0.6, "4", 860, 570, 110, BR)
        fcen(c, t, c14, "80", 520, 720, 110, BR)
        fcen(c, t, c14 + 0.3, "x", 860, 720, 110, CLARO)
        fcen(c, t, lerp(c14, d14, 0.45), "60 · 4 = 80 · x", 1430, 600, 90, BR)
        E.foco(c, t, d14, 0.5, lambda a: (E.bola(c, 1430, 800, 120, a=a), E.formula(c, "3 h", 1430, 830, 84, "g", BR, a, "center")))
    if C["s14"] <= t:
        E.saida(c, t, C["s15"] - 0.1, porque)

    if t >= C["s15"]:
        a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, a15, ps("só depois do", "i", 90, CLARO) + ps("teste do dobro", "g", 90, BR), W / 2, 280, "center", 0.12)
        E.frase(c, t, b15 - 1.6, ps("se for direta,", "i", 80, CLARO), 760, 490, "center", 0.12)
        E.foco(c, t, b15, 0.5, lambda a: E.pilula(c, "dá errado", 1280, 466, 70, "g", fundo=ERRADO, cor=BR, a=a))
        E.frase(c, t, c15 - 0.8, ps("3 grandezas:", "i", 76, CLARO), W / 2, 700, "center", 0.12)
        E.frase(c, t, c15 - 0.4, ps("pintores · horas · dias", "g", 76, BR), W / 2, 810, "center", 0.12)
        E.frase(c, t, c15, ps("outra aula", "i", 76, CLARO), W / 2, 930, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    a16, b16 = C["s16.a"], C["s16.b"]
    E.frase(c, t, a16, ps("1 saco de ração", "i", 72), XE, 330, passo=0.12)
    cabeca(c, t, a16 + 0.6, "cachorros", 400, 450, 56)
    cabeca(c, t, a16 + 0.6, "semanas", 800, 450, 56)
    fcen(c, t, lerp(a16, b16, 0.4), "5", 400, 640, 110, TINTA)
    fcen(c, t, lerp(a16, b16, 0.7), "6", 800, 640, 110, TINTA)
    fcen(c, t, b16 + 0.3, "3", 400, 790, 110, TINTA)
    fcen(c, t, b16 + 1.5, "?", 800, 790, 110, CINZA)
    E.frase(c, t, b16 + 2.0, ps("quantas", "i", 84) + [("semanas?", "g", 84, COR)], XE, 950, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1450, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def dobro():
        E.frase(c, t, a18, ps("dobro de cachorros,", "i", 70) + ps("metade do tempo", "g", 70, COR), W / 2, 190, "center", 0.12)
        tipo(c, t, b18, "inversa", W / 2, 300, size=56)
    E.saida(c, t, C["s19.c"] - 0.1, dobro)
    cabeca(c, t, a18, "cachorros", 400, 420, 56)
    cabeca(c, t, a18, "semanas", 800, 420, 56)
    vira = C["s19.d"]
    coluna(c, t, 400, 420, [("5", TINTA, a18 + 0.2), ("3", TINTA, a18 + 0.4)], vira)
    coluna(c, t, 800, 420, [("6", TINTA, a18 + 0.3), ("x", COR, a18 + 0.5)])
    # a linha de cada situação: 5 · 6 e 3 · x
    for i, t0 in enumerate((c18, d18)):
        p = ep(t, t0, 0.5) * (1 - ep(t, vira - 0.3, 0.3))
        if p > 0:
            y = 420 + DY3 * (i + 1) - 4
            M.rrect(c, 300, y - 70, 610, 140, 70, E.COR, 0.10 * p)

    def linha_conta():
        fcen(c, t, c18, "5 · 6 = 30", 1420, 540, 96, TINTA)
        fcen(c, t, d18, "= 3 · x", 1420, 680, 96, TINTA)
        fcen(c, t, C["s19.a"], "x = 30 ÷ 3", 1420, 820, 96, TINTA)
    E.saida(c, t, vira - 0.2, linha_conta)
    bola_res(c, t, C["s19.b"], "10", 1700, 960 - 30, 90, 100, E.CERTO)
    E.foco(c, t, C["s19.b"] + 0.3, 0.5, lambda a: centro(c, "semanas", 1480, 958, 60, "i", TINTA, a))
    if t >= C["s19.c"]:
        E.saida(c, t, vira - 0.2, lambda: (E.frase(c, t, C["s19.c"], ps("menos cachorros,", "i", 70) + ps("dura mais", "g", 70, CERTO), W / 2, 190, "center", 0.12),
                                           E.foco(c, t, C["s19.c"] + 0.5, 0.5, lambda a: E.selo(c, 1530, 290, 46, True, a))))
    if t >= vira:
        E.frase(c, t, vira, ps("pelas colunas,", "i", 70) + ps("virando a dos cachorros", "g", 70, COR), W / 2, 190, "center", 0.1)
        xa, xb, y = 1290, 1560, 600
        E.foco(c, t, vira + 1.4, 0.5, lambda a: (E.fracao(c, 6, "x", xa, y, 110, TINTA, a), centro(c, "=", (xa + xb) / 2, y + 38, 100, "g", TINTA, a),
                                                 E.fracao(c, 3, 5, xb, y, 110, TINTA, a)))
        fcen(c, t, vira + 2.6, "3 · x = 30", 1425, 820, 84, TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", "teste do dobro primeiro"), ("s20.b", "inversa: linha × linha igual"), ("s20.c", "o resultado faz sentido?"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                          centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s21.a"], [("3 grandezas", "g", 150, COR)], XE, 470)
    E.frase(c, t, C["s21.b"], ps("máquinas · horas · peças", "i", 84), XE, 600, passo=0.14)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(720, 425, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, metodo=b_metodo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
