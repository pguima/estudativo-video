"""Visual — Estudativo · MAT-POT-016: raiz de fração e decimal, raiz cúbica e raiz de negativo.
Peças da aula: cubo em perspectiva montado com cubinhos e os sinais de menos que formam dupla (ou sobram).
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-016_raiz_fracao_decimal_cubica_negativo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fracao", "cubica", "negativo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 3 ** 2 == 9 and 4 ** 2 == 16 and 5 ** 2 == 25 and 10 ** 2 == 100 and 3 ** 3 == 27 and 2 ** 4 == 16
assert (-2) * (-2) == 4 and 4 * (-2) == -8 and 12 ** 2 == 144 and 4 ** 3 == 64 and 7 ** 2 == 49


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


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.2):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


COS30, SEN30 = math.cos(math.radians(30)), 0.5


def iso(cx, cy, u, i, j, k):
    """ponto (i, j, k) do cubo em perspectiva isométrica: i vai à direita, j à esquerda, k para cima; (cx, cy) é o canto de baixo"""
    return cx + (i - j) * u * COS30 - 0, cy - (i + j) * u * SEN30 - k * u


def face(c, pts, cor, a, tom=BR):
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    c.drawPath(p, M.paint(tom, a * 0.8, stroke=2.5))


def cubinho(c, cx, cy, u, i, j, k, a, top, dir_, esq):
    """um cubinho: só as três faces que aparecem"""
    P = lambda x, y, z: iso(cx, cy, u, x, y, z)
    face(c, [P(i, j, k), P(i + 1, j, k), P(i + 1, j, k + 1), P(i, j, k + 1)], esq, a)
    face(c, [P(i, j, k), P(i, j + 1, k), P(i, j + 1, k + 1), P(i, j, k + 1)], dir_, a)
    face(c, [P(i, j, k + 1), P(i + 1, j, k + 1), P(i + 1, j + 1, k + 1), P(i, j + 1, k + 1)], top, a)


def cubo(c, t, cx, cy, u, ti, n=3, dt=0.05):
    """cubo montado com n³ cubinhos, de baixo para cima e do fundo para a frente, cada um cai no lugar. (cx, cy) = canto de baixo"""
    top, dir_, esq = M.mix(E.COR, BR, 0.42), E.COR, M.mix(E.COR, "#000000", 0.28)
    # do fundo para a frente: i e j decrescem na direção do observador
    ordem = sorted(((i, j, k) for i in range(n) for j in range(n) for k in range(n)), key=lambda p: (p[2], -p[0] - p[1]))
    for m, (i, j, k) in enumerate(ordem):
        q = prog(t, ti + m * dt, 0.35)
        if q <= 0:
            continue
        cubinho(c, cx, cy - 34 * (1 - ease_io(q)), u, i, j, k, min(1.0, q * 2.2), top, dir_, esq)


def menos(c, t, t0, n, x, y, r=46, pares=True):
    """n sinais de menos em esferas, agrupados de dois em dois; o que fica sem dupla sai vermelho"""
    gx = x
    for i in range(n):
        ti = t0 + i * 0.12
        sobra = i == n - 1 and n % 2 == 1
        E.foco(c, t, ti, 0.4, lambda p, gx=gx, sobra=sobra: num_bola(c, "−", gx, y, r, 72, p, ERRADO if sobra else None, BR))
        if i % 2 == 0 and i + 1 < n:
            q = ep(t, t0 + 0.5 + i * 0.1, 0.4)
            E.caixa_pontilhada(c, gx - r - 14, y - r - 14, 2 * r * 2 + 44 + 28, 2 * r + 34, q, COR, prog_=q)
        gx += 2 * r + 16 if i % 2 == 0 else 2 * r + 60


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        form(c, t, a_, "r{0,25}", 200, 440, 220, COR)
        E.sinal(c, t, b_ - 0.15, "=", 960, 365, 150)
        E.foco(c, t, b_, 0.5, lambda p: num_bola(c, "0,5", 1290, 360, 190, 150, p))
        E.frase(c, t, c_, ps("maior", "g", 110, ERRADO) + ps("que o número de dentro", "i", 100), W / 2, 730, "center", 0.14)
        E.frase(c, t, lerp(c_, C["s01.end"], 0.55), ps("raiz nem sempre", "i", 110) + ps("diminui", "g", 104, COR), W / 2, 890, "center", 0.17)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        a2, b2 = C["s02.a"], C["s02.b"]
        E.frase(c, t, C["s02"] + 0.1, ps("raiz de", "i", 104) + ps("número negativo", "g", 96, COR), W / 2, 230, "center", 0.16)
        E.foco(c, t, a2, 0.45, lambda p: E.selo(c, 470, 470, 76, True, p))
        E.frase(c, t, a2, ps("existe", "g", 120, CERTO), 580, 512)
        E.foco(c, t, b2, 0.45, lambda p: E.selo(c, 470, 660, 76, False, p))
        E.frase(c, t, b2, ps("não dá número da reta", "g", 96, ERRADO), 580, 695, passo=0.14)
        E.frase(c, t, lerp(b2, C["s02.end"], 0.6), ps("uma pergunta só", "i", 96) + ps("resolve tudo isso", "g", 86, COR), W / 2, 900, "center", 0.15)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "raiz quadrada", "vezes ele mesmo dá o de dentro"), ("s03.c", "potência", "de negativo, de fração e de decimal"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 76, COR)], x + 44, y + 96)
        E.frase(c, t, C[k] + 0.3, [(l2, "i", 58)], x + 44, y + 172)
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.7), ps("faltou algo? procure no canal", "i", 62), XE, 880, passo=0.12)


# ---------------- fração ----------------
def b_fracao(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5 = C["s05.a"]
    E.frase(c, t, C["s04"] + 0.1, ps("raiz de fração", "i", 96, COR), XE, 200)
    form(c, t, a4, "r{f{9}{16}}", 210, 590, 230, COR)
    E.frase(c, t, lerp(a4, b4, 0.2), ps("de cima com de cima,", "i", 72), 830, 300, passo=0.1)
    E.frase(c, t, lerp(a4, b4, 0.5), ps("de baixo com de baixo", "i", 72), 830, 390, passo=0.1)
    form(c, t, b4, "r{9} = 3", 830, 560, 110)
    form(c, t, c4, "r{16} = 4", 830, 720, 110)
    E.resultado(c, t, d4, 3, 4, 1520, 590, 130, 170)
    E.frase(c, t, C["s05"] + 0.1, ps("conferindo:", "i", 80), XE, 930, passo=0.1)
    form(c, t, a5, "f{3}{4} × f{3}{4} = f{9}{16}", 680, 920, 110, CERTO)


# ---------------- decimal ----------------
def b_decimal(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7 = C["s07.a"], C["s07.b"]

    def conta():
        E.frase(c, t, C["s06"] + 0.1, ps("no decimal, a mesma ideia", "i", 92, COR), XE, 200, passo=0.13)
        form(c, t, a6, "0,25 = f{25}{100}", XE + 20, 490, 150)
        form(c, t, b6, "r{25} = 5", 1010, 400, 110)
        form(c, t, c6, "r{100} = 10", 1010, 580, 110)
        form(c, t, d6, "f{5}{10} = 0,5", 640, 860, 140, COR)
    E.saida(c, t, C["s07"] - 0.1, conta)

    if t >= C["s07"]:
        E.frase(c, t, C["s07"] + 0.1, ps("conferindo:", "i", 92), XE, 240, passo=0.13)
        form(c, t, a7, "0,5 × 0,5 = 0,25", 690, 250, 124, CERTO)
        E.frase(c, t, b7, ps("entre", "i", 104) + ps("0 e 1", "g", 104, COR) + ps("a raiz fica maior", "i", 104), W / 2, 500, "center", 0.15)
        fmt = lambda v: str(v).replace(".", ",")
        vx = E.reta(c, t, b7 + 0.3, 340, 1560, 760, 0, 1, [0, 0.25, 0.5, 1], fmt, size=64, tm=[b7 + 0.4, b7 + 0.6, b7 + 1.0, b7 + 0.4])
        E.salto(c, t, b7 + 1.2, vx(0.25), vx(0.5), 746, 120, rotulo="raiz", size=64)


# ---------------- cúbica ----------------
def b_cubica(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    u = 100
    cx, cy = 480, 920
    E.frase(c, t, C["s08"] + 0.1, ps("repetir", "i", 92) + ps("três vezes?", "g", 84, COR), XE, 190)
    cubo(c, t, cx, cy, u, a8)
    xt = 1000

    def pergunta():
        E.frase(c, t, a8 + 0.2, ps("27", "g", 130, COR) + ps("cubinhos", "i", 110), xt, 400, passo=0.15)
        E.frase(c, t, lerp(a8, b8, 0.6), ps("quantos em cada lado?", "i", 80), xt, 570, passo=0.11)
    E.saida(c, t, c8 - 0.1, pergunta)
    # o lado: três cubinhos marcados na aresta da frente
    q = ep(t, b8, 0.45)
    if q > 0:
        xa, ya = iso(cx, cy, u, 0, 0, 0), iso(cx, cy, u, 3, 0, 0)
        M.line(c, xa[0], xa[1] + 26, ya[0], ya[1] + 26, COR, q, 6)
        E.foco(c, t, b8, 0.45, lambda p: centro(c, "3", (xa[0] + ya[0]) / 2 + 42, (xa[1] + ya[1]) / 2 + 110, 92, "g", COR, p))
    form(c, t, b8 + 0.3, "3 × 3 × 3 = 27", xt, 760, 96)
    E.frase(c, t, c8, ps("raiz cúbica", "g", 110, COR), xt, 400)
    form(c, t, c8 + 0.3, "r3{27} = 3", xt, 590, 130, COR)


def b_indice(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    fim = C["s09.end"]
    a0 = C["s10.a"]

    def tudo():
        s, x, y = 200, 200, 460
        form(c, t, C["s09"] - 0.1, "r3{27}", x, y, s, COR)
        q = ep(t, a9, 0.45)
        E.caixa_pontilhada(c, x - 16, y - s * 0.86, s * 0.3, s * 0.44, q, ERRADO, prog_=q)
        E.frase(c, t, a9, ps("índice", "g", 90, ERRADO), XE, 180)
        E.frase(c, t, lerp(a9, b9, 0.3), ps("quantas vezes", "i", 76), XE, 620, passo=0.12)
        E.frase(c, t, lerp(a9, b9, 0.55), ps("o número se repete", "i", 76), XE, 710, passo=0.12)
        xr = 830
        E.foco(c, t, b9, 0.45, lambda p: E.pilula(c, "índice 3", xr + 150, 240, 56, estilo="g", a=p))
        E.frase(c, t, b9 + 0.1, ps("raiz cúbica", "i", 84), xr + 340, 266)
        E.foco(c, t, c9, 0.45, lambda p: E.pilula(c, "índice 4", xr + 150, 400, 56, estilo="g", a=p))
        E.frase(c, t, c9 + 0.1, ps("raiz quarta", "i", 84), xr + 340, 426)
        form(c, t, d9, "r4{16} = 2", xr, 640, 130, COR)
        form(c, t, lerp(d9, fim, 0.2), "2 × 2 × 2 × 2 = 16", xr, 800, 86)
        E.frase(c, t, lerp(d9, fim, 0.62), ps("índice par:", "g", 84, COR) + ps("fica o positivo", "i", 90), W / 2, 950, "center", 0.14)
    E.saida(c, t, C["s10"] - 0.1, tudo)

    if t >= C["s10"]:
        s, x, y = 260, 500, 640
        form(c, t, C["s10"] + 0.1, "r{9}", x + 40, y, s, COR)
        E.frase(c, t, C["s10"] + 0.1, ps("na raiz quadrada", "i", 104), W / 2, 240, "center", 0.15)
        E.foco(c, t, a0, 0.45, lambda p: (centro(c, "2", x + 14, y - s * 0.46, 104, "g", ERRADO, p), E.caixa_pontilhada(c, x - 44, y - s * 0.72, 116, 128, p, ERRADO)))
        E.frase(c, t, a0 + 0.3, ps("índice 2", "g", 110, ERRADO), 1080, 480)
        E.frase(c, t, lerp(a0, C["s10.end"], 0.6), ps("nem se escreve", "i", 110), 1080, 620, passo=0.15)


# ---------------- negativo ----------------
def b_negativo(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    a3, b3 = C["s13.a"], C["s13.b"]

    def cub():
        E.frase(c, t, C["s11"] + 0.1, ps("e com negativo?", "i", 96, COR), XE, 200, passo=0.14)
        form(c, t, a1, "r3{−8} = ?", XE + 20, 470, 170, None)
        E.frase(c, t, lerp(a1, b1, 0.3), ps("repetido três vezes,", "i", 72), XE, 610, passo=0.12)
        E.frase(c, t, lerp(a1, b1, 0.55), ps("dá menos oito?", "i", 72), XE, 700, passo=0.12)
        form(c, t, b1, "(−2) × (−2) = 4", 980, 330, 92)
        form(c, t, c1, "4 × (−2) = −8", 980, 500, 92)
        E.foco(c, t, d1, 0.5, lambda p: num_bola(c, "−2", 1350, 760, 150, 140, p))
    E.saida(c, t, C["s12"] - 0.1, cub)

    if C["s12"] <= t < C["s13"] + 0.4:
        def qua():
            form(c, t, a2, "r{−4} = ?", XE + 20, 340, 170, None)
            form(c, t, b2, "2 × 2 = 4", 980, 220, 92)
            form(c, t, c2, "(−2) × (−2) = 4", 980, 370, 92)
            form(c, t, lerp(c2, d2, 0.55), "0 × 0 = 0", 980, 520, 92)
            E.frase(c, t, d2, ps("vezes ele mesmo", "i", 92) + ps("nunca dá negativo", "g", 88, ERRADO), W / 2, 720, "center", 0.14)
            E.foco(c, t, e2, 0.45, lambda p: E.selo(c, 350, 880, 66, False, p))
            E.frase(c, t, e2, ps("não existe", "i", 100) + ps("número da reta", "g", 92, ERRADO), 450, 915, passo=0.14)
        E.saida(c, t, C["s13"] - 0.1, qua)

    if t >= C["s13"]:
        fim = C["s13.end"]
        t4, t5 = lerp(b3, fim, 0.42), lerp(b3, fim, 0.74)
        E.frase(c, t, a3, ps("índice ímpar", "g", 96, CERTO) + ps("aceita negativo", "i", 100), XE, 300, passo=0.16)
        E.frase(c, t, b3, ps("índice par", "g", 96, ERRADO) + ps("não aceita", "i", 100), XE, 620, passo=0.16)
        # ímpar: sobra um; par: todos em dupla
        E.frase(c, t, lerp(b3, fim, 0.1), ps("cada dupla de menos vira mais", "i", 84, COR), W / 2, 950, "center", 0.1)
        menos(c, t, t5, 3, 280, 420)
        E.frase(c, t, t5 + 0.5, ps("sobra um", "g", 76, ERRADO), 620, 448)
        menos(c, t, t4, 4, 280, 760)
        E.frase(c, t, t4 + 0.6, ps("todos em dupla:", "i", 72) + ps("nunca negativo", "g", 66, ERRADO), 840, 790, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_ = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.1, ps("o erro mais comum", "i", 96, ERRADO), W / 2, 200, "center", 0.14)
    form(c, t, a_, "r{−4} = −2", W / 2, 460, 170, ERRADO, "center")
    if t >= b_:
        E.risco(c, 480, 480, 1440, 310, t, b_, largura=12)
    form(c, t, b_, "(−2) × (−2) = 4", W / 2, 680, 110, None, "center")
    E.frase(c, t, b_ + 0.7, ps("positivo, não", "i", 76), W / 2 - 40, 790, "center", 0.12)
    form(c, t, b_ + 1.0, "−4", W / 2 + 130, 790, 76, ERRADO)
    E.frase(c, t, c_, ps("o sinal de menos", "i", 104) + ps("não sai de dentro", "g", 96, COR), W / 2, 950, "center", 0.15)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, C["s15"] + 0.1, ps("agora, o atalho", "i", 84, CLARO), W / 2, 170, "center")
        E.frase(c, t, a5, ps("metade", "g", 130, BR) + ps("das casas", "i", 130, BR), W / 2, 330, "center", 0.2)
        form(c, t, b5, "1,44", 340, 620, 150, BR)
        E.frase(c, t, b5 + 0.5, ps("2 casas", "i", 84, CLARO), 340, 740)
        form(c, t, c5, "r{144} = 12", 960, 620, 150, BR)
        form(c, t, d5, "r{1,44} = 1,2", W / 2, 910, 150, CLARO, "center")
    E.saida(c, t, C["s16"] - 0.1, um)

    if t >= C["s16"]:
        E.frase(c, t, a6, ps("as casas", "i", 104, CLARO) + ps("se somam", "g", 100, BR), W / 2, 210, "center", 0.17)
        form(c, t, a6 + 0.3, "1,2 × 1,2 = 1,44", 280, 400, 100, BR)
        E.frase(c, t, lerp(a6, b6, 0.4), ps("1 + 1 = 2 casas", "i", 76, CLARO), 1180, 395, passo=0.1)
        E.frase(c, t, b6, ps("com", "i", 96, CLARO) + ps("número ímpar de casas", "g", 88, BR) + ps("não compensa", "i", 96, CLARO), W / 2, 570, "center", 0.12)
        form(c, t, c6, "r{0,4} ≠ 0,2", 280, 760, 124, ERRADO)
        form(c, t, d6, "0,2 × 0,2 = 0,04", 1000, 760, 92, BR)
        E.frase(c, t, lerp(d6, C["s16.end"], 0.7), ps("aí, cerque o valor", "i", 96, CLARO), W / 2, 950, "center", 0.13)


# ---------------- questão ----------------
ITENS = ((190, 450), (660, 450), (190, 690), (660, 690))


def b_questao(c, t, C, b):
    a7, b7, c7, d7, e7, f7 = (C[f"s17.{k}"] for k in "abcdef")
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 84, COR), XE, 200)
    for ti, s, (x, y) in zip((a7, b7, c7, d7), ("r{f{25}{49}}", "r{0,09}", "r3{−64}", "r{−25}"), ITENS):
        form(c, t, ti, s, x, y, 120)
    E.frase(c, t, e7, ps("uma", "g", 72, COR) + ps("não dá número da reta: qual?", "i", 76), XE, 860, passo=0.1)
    E.frase(c, t, f7, ps("calcule as outras", "i", 76), XE, 960, passo=0.12)
    E.relogio(c, t, C["s18.a"], 1490, 400, 190)


# ---------------- resposta ----------------
def par(c, t, ta, tb, esq, dir_, x, y, s=130):
    """a raiz em ta e o resultado verde em tb, logo depois dela"""
    w = E.formula(c, esq, 0, 0, s, a=0)
    form(c, t, ta, esq, x, y, s)
    form(c, t, tb, dir_, x + w + s * 0.2, y, s, CERTO)


def b_resposta(c, t, C, b):
    a9, b9 = C["s19.a"], C["s19.b"]
    a0, b0, c0 = C["s20.a"], C["s20.b"], C["s20.c"]
    s0 = C["s19"]
    xa, xb, y1, y2 = 200, 1020, 300, 740
    par(c, t, lerp(s0, a9, 0.3), a9, "r{f{25}{49}}", "= f{5}{7}", xa, y1)
    E.frase(c, t, lerp(s0, a9, 0.5), ps("raiz de 25 e de 49", "i", 66), xa, y1 + 160, passo=0.1)
    par(c, t, lerp(a9, b9, 0.15), b9, "r{0,09}", "= 0,3", xb, y1)
    E.frase(c, t, lerp(a9, b9, 0.45), ps("2 casas: raiz de 9 é 3", "i", 66), xb, y1 + 160, passo=0.1)
    par(c, t, a0 - 0.2, b0, "r3{−64}", "= −4", xa, y2)
    E.foco(c, t, a0, 0.45, lambda p: E.formula(c, "4 × 4 × 4 = 64", xa, y2 + 150, 76, cor=TINTA, a=p))
    form(c, t, lerp(b0, c0, 0.45), "r{−25}", xb, y2, 130)
    E.foco(c, t, c0, 0.45, lambda p: E.selo(c, xb + 420, y2 - 44, 70, False, p))
    E.frase(c, t, lerp(b0, c0, 0.65), ps("índice par com negativo:", "i", 66), xb, y2 + 150, passo=0.1)
    E.frase(c, t, c0, ps("não dá número da reta", "g", 62, ERRADO), xb, y2 + 240, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.1, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        itens = ((460, "s21.a", ps("o índice diz", "i", 88) + ps("quantas vezes se repete", "g", 76, COR)),
                 (680, "s21.b", ps("índice par com negativo", "g", 76, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p: num_bola(c, str(i + 1), 230, y - 30, 58, 66, p))
            E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.14)
        E.frase(c, t, C["s21.b"] + 0.9, ps("não dá número da reta", "i", 88), 330, 800, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a_, b_, c_, d_ = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("próxima aula", "i", 84), XE, 240)
    E.frase(c, t, a_, ps("expoente", "g", 110, COR) + ps("em forma de", "i", 110), XE, 390, passo=0.15)
    E.frase(c, t, a_ + 0.5, ps("fração", "g", 110, COR), XE, 520, passo=0.15)
    form(c, t, b_, "9^{1/2} = r{9}", XE, 690, 110)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1430, 590, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1580, p), lerp(860, 635, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fracao=b_fracao, decimal=b_decimal, cubica=b_cubica, indice=b_indice, negativo=b_negativo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
