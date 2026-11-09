"""Visual — Estudativo · FIS-OND-004: interferência e polarização.
Linguagem visual da trilha Ondas e Som: docstring do visual.py da FIS-OND-001. Nesta aula: primeira onda laranja (COR),
segunda onda azul (F.NEG), a soma em tinta e mais grossa; reforço = verde, cancelamento = vermelho; caixas de som como
retângulos escuros com o cone laranja; a grade de ripas da polarização em tinta."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-004_interferencia_e_polarizacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("soma", "fone", "prever", "polariza", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def par_impar(d, meio):
    """regra da aula: diferença ÷ meio λ; par → reforço, ímpar → cancelamento"""
    k = d / meio
    assert abs(k - round(k)) < 1e-9
    return "reforço" if round(k) % 2 == 0 else "cancelamento"


# todas as contas da aula
assert 2 + 2 == 4                                          # duas cristas de 2 cm → 4 cm
assert par_impar(7 - 5, 1) == "reforço" and 7 - 5 == 2     # λ = 2 m: 5 e 7 m → diferença 2 m = 1 λ
assert par_impar(6 - 5, 1) == "cancelamento"               # 5 e 6 m → 1 m = meio λ
assert par_impar(3.5 - 3, 0.5) == "cancelamento"           # erro: λ = 1 m, 3 e 3,5 m → meio λ
assert 340 / 170 == 2 and 8 - 5 == 3 and par_impar(3, 1) == "cancelamento"   # questão


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete2(c, t, C, cena, itens, desenhos):
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def curva(c, x0, x1, fy, cor, a=1.0, largura=7, dash=None):
    """desenha y = fy(x) de x0 a x1"""
    if a <= 0:
        return
    n = max(2, int((x1 - x0) / 4))
    F.poli(c, [(x0 + (x1 - x0) * i / n, fy(x0 + (x1 - x0) * i / n)) for i in range(n + 1)], 1.0, cor, a, largura, dash)


def senoide(c, x0, x1, y, A, lam, fase=0.0, cor=None, a=1.0, largura=7, eixo=True):
    """senoide parada: crista em x0 + lam/4 + fase; A < 0 inverte"""
    if a <= 0:
        return
    if eixo:
        M.line(c, x0 - 20, y, x1 + 20, y, TINTA, 0.35 * a, 3, dash=E.TRACO)
    curva(c, x0, x1, lambda x: y - A * math.sin(2 * math.pi * (x - x0 - fase) / lam), cor or E.COR, a, largura)


def caixa_som(c, x, y, s, a=1.0, vira=1):
    """caixa de som com o cone virado para a direita (vira=1) ou esquerda (-1); (x, y) = centro"""
    if a <= 0:
        return
    M.rrect(c, x - s * 0.45, y - s * 0.7, s * 0.9, s * 1.4, s * 0.12, "#2A2A33", a)
    c.drawCircle(x + vira * s * 0.05, y + s * 0.18, s * 0.3, M.paint(E.COR, a))
    c.drawCircle(x + vira * s * 0.05, y + s * 0.18, s * 0.11, M.paint("#2A2A33", a))
    c.drawCircle(x + vira * s * 0.05, y - s * 0.4, s * 0.13, M.paint(E.COR, a))


def ouvido(c, x, y, s, a=1.0):
    """orelha estilizada: arco grosso com a dobra"""
    if a <= 0:
        return
    E.arco(c, x, y, s, -110, 250, TINTA, s * 0.22, a)
    E.arco(c, x + s * 0.1, y + s * 0.05, s * 0.45, -60, 200, TINTA, s * 0.14, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("fone", "g", 96, COR)] + ps("apaga o barulho", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("jogando", "i", 84) + [("mais som", "g", 84)], XE, 410, passo=0.12)
        x0, x1 = 300, 1650
        senoide(c, x0, x1, 620, 70, 280, a=ep(t, C["s01.b"], 0.5), eixo=False, cor=TINTA2, largura=6)
        senoide(c, x0, x1, 760, -70, 280, a=ep(t, C["s01.b"] + 0.5, 0.5), eixo=False, cor=F.NEG, largura=6)
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.escreve(c, "ruído", 1690, 640, 50, "b", TINTA2, a))
        E.foco(c, t, C["s01.b"] + 0.5, 0.4, lambda a: E.escreve(c, "fone", 1690, 780, 50, "b", F.NEG, a))
        q = ep(t, C["s01.c"], 0.6)
        if q > 0:
            M.line(c, x0, 920, lerp(x0, x1, q), 920, TINTA, 1.0, 8)
        E.frase(c, t, C["s01.c"], [("som", "g", 70), ("+", "g", 70, COR), ("som", "g", 70), ("=", "g", 70, COR), ("silêncio", "g", 70, CERTO)], XE, 1020, passo=0.15)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, cor) in enumerate((("s02.b", "reforço", CERTO), ("s02.c", "cancelamento", ERRADO), ("s02.d", "polarização", COR))):
        y = 460 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 84, cor)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def desenho(a, x, y):
        senoide(c, x - 140, x + 110, y, 40, 125, a=a, largura=6)

    def tipos(a, x, y):
        senoide(c, x - 30, x + 120, y - 40, 22, 75, a=a, largura=5, eixo=False)
        for i, dx in enumerate((0, 14, 22, 28, 34, 48, 66, 84, 98, 106, 112, 126)):
            M.line(c, x - 30 + dx, y + 10, x - 30 + dx, y + 70, E.COR, a, 5)
    lembrete2(c, t, C, "s03", (("s03.b", "no desenho da onda:", "crista, vale, A e λ"), ("s03.c", "a diferença entre", "transversal e longitudinal")), (desenho, tipos))


# ---------------- interferência ----------------
def pulsos(c, t, t0, y, x0, x1, A1, A2, w=90, vel=260, a=1.0):
    """dois pulsos que andam um contra o outro sobre a mesma corda; desenha os dois finos e a soma grossa"""
    L = x1 - x0
    s = min(860.0, vel * max(0.0, t - t0))
    xa = x0 + 140 + s
    xb = x1 - 140 - s
    g = lambda x, xc: math.exp(-((x - xc) / w) ** 2)
    curva(c, x0, x1, lambda x: y - A1 * g(x, xa), E.COR, 0.5 * a, 4)
    curva(c, x0, x1, lambda x: y - A2 * g(x, xb), F.NEG, 0.5 * a, 4)
    curva(c, x0, x1, lambda x: y - A1 * g(x, xa) - A2 * g(x, xb), TINTA, a, 8)


def b_soma(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("duas ondas no mesmo ponto:", "i", 70), XE, 230, passo=0.12)
        E.frase(c, t, C["s04.a"], [("elas", "i", 84), ("se somam", "g", 84, COR)], XE, 340, passo=0.12)
        t0p = C["s04.a"] - 0.3
        vel = 530 / max(1.0, C["s04.b"] + 0.3 - t0p)  # os pulsos se encontram no meio quando a fala diz "interferência"
        if t >= C["s04"]:
            pulsos(c, t, t0p, 680, 290, 1630, 110, 110, vel=vel, a=ep(t, C["s04"], 0.5))
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.pilula(c, "interferência", W / 2, 880, 64, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s04.c"], ps("depois, cada uma segue", "i", 60, TINTA2), W / 2, 1000, "center", 0.1)
        return
    x0, x1, lam = 600, 1700, 360
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("crista", "g", 76, COR), ("com", "i", 80), ("crista", "g", 76, F.NEG)], XE, 220, passo=0.12)
        senoide(c, x0, x1, 360, 50, lam, a=ep(t, C["s05.a"], 0.4))
        senoide(c, x0, x1, 520, 50, lam, cor=F.NEG, a=ep(t, C["s05.a"] + 0.3, 0.4))
        E.foco(c, t, C["s05.a"] + 0.8, 0.4, lambda a: E.formula(c, "+", 420, 470, 80, "g", TINTA2, a))
        senoide(c, x0, x1, 760, 100, lam, cor=TINTA, a=ep(t, C["s05.a"] + 1.2, 0.5), largura=9)
        E.foco(c, t, C["s05.a"] + 1.2, 0.4, lambda a: E.formula(c, "=", 420, 790, 80, "g", TINTA2, a))
        pilula(c, t, C["s05.b"], "construtiva", 330, 900, 56, CERTO)
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, "2 cm + 2 cm = 4 cm", W / 2 + 200, 1000, 64, "g", CERTO, a, "center"))
        return
    E.frase(c, t, C["s06.a"], [("crista", "g", 76, COR), ("com", "i", 80), ("vale", "g", 76, F.NEG)], XE, 220, passo=0.12)
    senoide(c, x0, x1, 360, 50, lam, a=ep(t, C["s06.a"], 0.4))
    senoide(c, x0, x1, 520, -50, lam, cor=F.NEG, a=ep(t, C["s06.a"] + 0.3, 0.4))
    E.foco(c, t, C["s06.a"] + 0.8, 0.4, lambda a: E.formula(c, "+", 420, 470, 80, "g", TINTA2, a))
    E.foco(c, t, C["s06.a"] + 1.2, 0.4, lambda a: E.formula(c, "=", 420, 790, 80, "g", TINTA2, a))
    if t >= C["s06.a"] + 1.2:
        q = ep(t, C["s06.a"] + 1.2, 0.6)
        M.line(c, x0, 760, lerp(x0, x1, q), 760, TINTA, 1.0, 9)
    pilula(c, t, C["s06.b"], "destrutiva", 330, 900, 56, ERRADO)
    E.frase(c, t, C["s06.c"], [("amplitudes", "i", 64), ("iguais:", "i", 64), ("soma", "g", 60), ("zero", "g", 60, ERRADO)], W / 2 + 200, 1000, "center", 0.12)


# ---------------- fone ----------------
def b_fone(c, t, C, b):
    E.frase(c, t, C["s07"], ps("o que o", "i", 84) + [("fone", "g", 90, COR)] + ps("faz", "i", 84), XE, 220, passo=0.12)
    x0, x1, lam = 300, 1350, 300
    # 1: o microfone pega o ruído
    E.foco(c, t, C["s07.a"], 0.4, lambda a: (E.escreve(c, "ruído", XE, 410, 54, "b", TINTA2, a), c.drawCircle(1430, 380, 26, M.paint(TINTA, a)),
                                             E.escreve(c, "microfone", 1480, 400, 50, "i", TINTA2, a)))
    senoide(c, x0, x1, 380, 60, lam, cor=TINTA2, a=ep(t, C["s07.a"], 0.5), largura=6)
    # 2: o fone toca a onda invertida
    E.foco(c, t, C["s07.b"], 0.4, lambda a: (E.escreve(c, "fone", XE, 590, 54, "b", F.NEG, a), caixa_som(c, 1440, 560, 90, a, -1)))
    senoide(c, x0, x1, 560, -60, lam, cor=F.NEG, a=ep(t, C["s07.b"], 0.5), largura=6)
    if t >= C["s07.b"] + 0.8:  # crista sobre vale
        xc = x0 + lam / 4
        q = ep(t, C["s07.b"] + 0.8, 0.4)
        M.line(c, xc, 320, xc, 620, ERRADO, q, 4, dash=E.TRACO)
        E.foco(c, t, C["s07.b"] + 0.9, 0.4, lambda a: E.pilula(c, "crista ↔ vale", xc, 470, 40, "b", fundo=TINTA, a=a))
    # 3: no ouvido, silêncio
    if t >= C["s07.c"]:
        q = ep(t, C["s07.c"], 0.6)
        M.line(c, x0, 800, lerp(x0, x1, q), 800, TINTA, 1.0, 9)
        E.foco(c, t, C["s07.c"], 0.4, lambda a: (E.escreve(c, "soma", XE, 770, 54, "b", TINTA, a), ouvido(c, 1490, 790, 80, a)))
        E.frase(c, t, C["s07.c"] + 0.6, [("silêncio", "g", 70, CERTO)], 1340, 980)


# ---------------- prever ----------------
def cena_caixas(c, t, t0, P, d1, d2, A=(380, 380), B=(380, 760), cor_lin=TINTA2, a=1.0, size=60):
    """duas caixas à esquerda e o ponto P; as linhas até P com as distâncias"""
    if t < t0:
        return
    q = ep(t, t0, 0.5) * a
    caixa_som(c, A[0], A[1], 110, q)
    caixa_som(c, B[0], B[1], 110, q)
    for (X, d, k) in ((A, d1, 0), (B, d2, 1)):
        qq = ep(t, t0 + 0.3 + 0.3 * k, 0.5) * a
        if qq > 0:
            M.line(c, X[0] + 60, X[1], lerp(X[0] + 60, P[0], qq), lerp(X[1], P[1], qq), cor_lin, qq, 4, dash=E.TRACO)
            mx, my = (X[0] + 60 + P[0]) / 2, (X[1] + P[1]) / 2 + (-50 if k == 0 else 70)
            F.medida(c, d, "m", mx, my, size, TINTA, qq, "center")
    c.drawCircle(P[0], P[1], 18, M.paint(E.COR, q))
    E._meio(c, "P", P[0] + 50, P[1] - 40, 56, "g", COR, q)


def b_prever(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08"], ps("como prever", "i", 84), XE, 220, passo=0.12)
        E.foco(c, t, C["s08.a"], 0.5, lambda a: (caixa_som(c, 380, 420, 110, a), caixa_som(c, 380, 800, 110, a)))
        E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: E.escreve(c, "a mesma onda, juntas", 470, 620, 50, "i", TINTA2, a))
        if t >= C["s08.b"] - 1.5:
            P = (1500, 600)
            q = ep(t, C["s08.b"] - 1.5, 0.5)
            c.drawCircle(*P, 18, M.paint(E.COR, q))
            for Y in (420, 800):
                M.line(c, 440, Y, lerp(440, P[0], q), lerp(Y, P[1], q), TINTA2, q, 4, dash=E.TRACO)
        E.frase(c, t, C["s08.b"], [("o que decide:", "i", 66), ("a diferença", "g", 66, COR)], W / 2, 1000, "center", 0.12)
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09"], [("diferença", "g", 76, COR), ("de caminho", "i", 80)], XE, 220, passo=0.12)
        for i, (k, rot, nums, res, cor) in enumerate((("s09.a", "inteiro de λ", "0 · 1λ · 2λ", "reforço", CERTO),
                                                       ("s09.c", "meio λ a mais", "f{1}{2}λ · 1f{1}{2}λ · 2f{1}{2}λ", "cancelamento", ERRADO))):
            y = 430 + i * 330
            p = ep(t, C[k], 0.5)
            E.caixa_pontilhada(c, XE, y - 120, 1580, 260, p, prog_=p)
            E.foco(c, t, C[k], 0.4, lambda a, y=y, rot=rot: E.formula(c, rot, XE + 40, y - 30, 56, "b", TINTA, a))
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, y=y, nums=nums: E.formula(c, nums, XE + 40, y + 80, 70, "g", COR, a))
            kk = "s09.b" if i == 0 else "s09.d"
            E.foco(c, t, C[kk], 0.4, lambda a, y=y, res=res, cor=cor: E.pilula(c, res, 1480, y + 10, 64, "g", fundo=cor, a=a))
            sub = "crista com crista" if i == 0 else "crista com vale"
            E.foco(c, t, C[kk] - 0.6, 0.4, lambda a, y=y, sub=sub: E.escreve(c, sub, 830, y + 30, 54, "i", TINTA2, a))
        return
    E.frase(c, t, C["s10.a"], [("λ =", "g", 76), ("2 m", "g", 76, COR)], XE, 200, passo=0.12)
    if t < C["s10.d"]:
        cena_caixas(c, t, C["s10.b"], (1300, 600), 5, 7)
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "7 − 5 = 2 m = 1λ", 1000, 900, 70, "g", TINTA, a))
        pilula(c, t, C["s10.c"] + 1.2, "reforço", 1580, 600, 60, CERTO)
    else:
        cena_caixas(c, t, C["s10.d"], (1300, 600), 5, 6)
        E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "6 − 5 = 1 m = f{1}{2}λ", 1000, 900, 70, "g", TINTA, a))
        pilula(c, t, C["s10.e"] + 1.4, "cancelamento", 1620, 600, 56, ERRADO)


# ---------------- polarização ----------------
def grade(c, x, y0, y1, a=1.0, n=5, gap=36):
    """grade de ripas em pé, centrada em x; a fresta do meio é por onde a corda passa"""
    if a <= 0:
        return
    for i in range(n):
        xx = x + (i - (n - 1) / 2) * gap
        M.rrect(c, xx - 9, y0, 18, y1 - y0, 5, "#8B5E3C", a)


def b_polariza(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("polarização", "g", 90, COR)], XE, 220)
        xg, y = 1000, 640
        E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: E.escreve(c, "ripas em pé", xg - 120, 960, 46, "i", TINTA2, a))
        # vibração para cima e para baixo: passa
        if t >= C["s11.c"]:
            ph = 2.4 * (t - C["s11.c"])
            k = ep(t, C["s11.c"], 0.6)
            curva(c, 220, lerp(220, 1750, k), lambda x: y - 110 * math.sin(2 * math.pi * x / 300 - ph), E.COR, 1.0, 7)
            E.foco(c, t, C["s11.c"], 0.4, lambda a: (F.seta(c, 160, y + 60, 160, y - 120, TINTA, a, 6), F.seta(c, 160, y - 60, 160, y + 120, TINTA, a, 6)))
        # vibração para os lados (vista em perspectiva, achatada): para na grade
        if t >= C["s11.d"]:
            ph = 2.4 * (t - C["s11.d"])
            k = ep(t, C["s11.d"], 0.6)
            yy = y + 200
            curva(c, 220, lerp(220, xg - 40, k), lambda x: yy - 30 * math.sin(2 * math.pi * x / 300 - ph), F.NEG, 1.0, 7)
            curva(c, xg + 40, 1750, lambda x: yy, F.NEG, 0.5 * k, 5, dash=E.TRACO)
            E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "para os lados: bate e para", 560, yy + 110, 40, "b", fundo=F.NEG, a=a))
            E.foco(c, t, C["s11.c"] + 0.4, 0.4, lambda a: E.pilula(c, "sobe e desce: passa", 560, 420, 40, "b", fundo=E.COR, a=a))
        E.foco(c, t, C["s11.b"], 0.5, lambda a: grade(c, xg, 380, 900, a))
        E.frase(c, t, C["s11.e"], [("uma", "i", 60), ("só", "i", 60), ("direção:", "i", 60), ("polarizada", "g", 60, COR)], 1450, 420, "center", 0.12)
        return
    E.frase(c, t, C["s12.a"], ps("só a", "i", 80) + [("transversal", "g", 80, COR)] + ps("polariza", "i", 80), XE, 220, passo=0.12)
    x1, x2, w, y, h = 170, 1000, 750, 320, 520
    for x, k in ((x1, "s12.b"), (x2, "s12.d")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.frase(c, t, C["s12.b"], [("longitudinal", "g", 60)], x1 + 50, y + 90)
    if t >= C["s12.b"]:
        q = ep(t, C["s12.b"], 0.5)
        ph = 2.4 * (t - C["s12.b"])
        for i in range(22):
            xe = x1 + 70 + i * 28
            xx = xe - 10 * math.sin(2 * math.pi * xe / 200 - ph)
            M.line(c, xx, y + 160, xx, y + 300, E.COR, q, 5)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "som: não polariza", x1 + w / 2, y + 400, 50, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s12.d"], [("transversal", "g", 60, COR)], x2 + 50, y + 90)
    if t >= C["s12.d"]:
        senoide(c, x2 + 70, x2 + w - 70, y + 230, 60, 200, a=ep(t, C["s12.d"], 0.5), eixo=False)
    E.foco(c, t, C["s12.d"] + 0.4, 0.4, lambda a: E.pilula(c, "luz: polariza", x2 + w / 2, y + 400, 50, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s12.e"], [("óculos", "g", 56), ("polarizados:", "g", 56, COR)] + ps("cortam o brilho da água e do asfalto", "i", 56), W / 2, 980, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("olhe a", "i", 70) + [("diferença,", "g", 70, COR)] + ps("não as distâncias", "i", 70), XE + 480, 190, passo=0.1)
    cena_caixas(c, t, C["s13.b"], (1300, 600), 3, "3,5")
    E.foco(c, t, C["s13.b"] + 0.8, 0.4, lambda a: E.formula(c, "λ = 1 m", 1500, 380, 64, "g", TINTA, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "quase iguais: reforço?", XE, 920, 64, "g", ERRADO, a))
    if t >= C["s13.c"] + 1.2:
        E.risco(c, XE - 10, 930, XE + 700, 860, t, C["s13.c"] + 1.2, largura=10)
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "3,5 − 3 = 0,5 m = f{1}{2}λ", XE, 1030, 64, "g", TINTA, a))
    pilula(c, t, C["s13.e"], "cancela", 1580, 600, 60, ERRADO)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "f{diferença}{meio λ}", W / 2, 380, 110, "g", BR, a, "center"))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.pilula(c, "par", 640, 600, 80, "g", fundo=E.COR, a=a, cor=BR),
                                             F.seta(c, 760, 600, 900, 600, CLARO, a, 7), E.pilula(c, "reforço", 1110, 600, 80, "g", fundo=CERTO, a=a, cor=BR)))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.pilula(c, "ímpar", 640, 750, 80, "g", fundo=E.COR, a=a, cor=BR),
                                             F.seta(c, 790, 750, 900, 750, CLARO, a, 7), E.pilula(c, "cancela", 1110, 750, 80, "g", fundo=ERRADO, a=a, cor=BR)))
    E.foco(c, t, C["s14.c"] + 1.0, 0.4, lambda a: E.escreve(c, "zero conta como par", 1360, 610, 48, "i", CLARO, a))
    E.foco(c, t, C["s14.c"] + 4.5, 0.4, lambda a: E.escreve(c, "não inteiro: meio-termo", 1360, 760, 48, "i", CLARO, a))
    E.frase(c, t, C["s14.d"], ps("só com fontes", "i", 56, CLARO) + [("juntas;", "g", 56, BR)] + ps("fonte invertida:", "i", 56, CLARO) + [("regra inverte", "g", 56, BR)],
            W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], ps("duas caixas, juntas:", "i", 64), XE, 340, passo=0.1)
    E.foco(c, t, C["s15.a"] + 0.6, 0.5, lambda a: F.medida(c, 170, "Hz", XE + 620, 340, 84, COR, a))
    E.frase(c, t, C["s15.b"], ps("som:", "i", 64), XE, 470, passo=0.1)
    E.foco(c, t, C["s15.b"] + 0.4, 0.5, lambda a: F.medida(c, 340, "m/s", XE + 180, 470, 84, TINTA, a))
    E.frase(c, t, C["s15.c"], ps("ponto a", "i", 64) + [("5 m", "g", 64, COR), ("e", "i", 64), ("8 m:", "g", 64, COR)], XE, 600, passo=0.1)
    E.frase(c, t, C["s15.c"] + 1.6, [("reforça", "g", 64, CERTO), ("ou", "i", 64), ("cancela?", "g", 64, ERRADO)], XE, 700, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("e o som", "i", 64) + [("polariza?", "g", 64, COR)], XE, 830, passo=0.12)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1460, cy=440, r=200)
    elif t >= C["s15.c"]:
        cena_caixas(c, t, C["s15.c"], (1650, 640), 5, 8, A=(1100, 450), B=(1100, 830), size=56)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    conta(c, t, [(C["s17.a"], "λ = 340 ÷ 170 = 2 m"), (C["s17.b"], "meio λ = 1 m"), (C["s17.c"], "8 − 5 = 3 m"), (C["s17.d"], "3 ÷ 1 = 3: ímpar")], XE, 260, 150, 84)
    pilula(c, t, C["s17.e"], "cancelamento", 1450, 600, 80, ERRADO)
    E.frase(c, t, C["s17.f"], ps("o som", "i", 64) + [("não polariza:", "g", 60, ERRADO)] + ps("é longitudinal", "i", 64), XE, 900, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("crista + crista:", "g", 64), ("reforça;", "i", 66, CERTO), ("crista + vale:", "g", 64), ("cancela", "i", 66, ERRADO)]),
                 ("s18.b", [("diferença ÷ meio λ:", "g", 64), ("par", "g", 64, CERTO), ("reforça,", "i", 66), ("ímpar", "g", 64, ERRADO), ("cancela", "i", 66)]),
                 ("s18.c", [("só", "i", 66), ("transversal", "g", 64, COR), ("polariza", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("praticando", "g", 110, COR)], XE, 400)
    for i, s in enumerate(("pêndulo e mola", "v = λ · f", "cada fenômeno")):
        E.foco(c, t, C["s19.b"] + 0.5 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, XE + 200 + i * 400, 580, 52, "g", fundo=E.COR if i == 1 else TINTA, a=a))
    F.onda(c, t, C["s19.a"], XE, 1250, 800, 50, 220, d=1.2, velocidade=120)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, soma=b_soma, fone=b_fone, prever=b_prever, polariza=b_polariza, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
