"""Visual — Estudativo · FIS-ELE-008: corrente elétrica.

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001):
CIRCUITO com F.fio/F.pilha/F.lampada em tinta; corrente convencional = setinhas laranja (F.corrente) saindo do + da pilha;
elétrons = bolinhas azuis andando ao contrário; gráfico i × t com F.grafico e a carga como área (F.area_graf).
Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-008_corrente_eletrica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("corrente", "grafico", "bateria", "tipos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"

# todas as contas da aula
assert 30 / 10 == 3 and 2 * 5 == 10 and 4 * 2 / 2 == 4 and 10 + 4 == 14
assert abs(1e-3 * 3600 - 3.6) < 1e-12 and 4000 / 1000 == 4 and 4 * 3600 == 14400
assert 400 * 10 == 4000 and 2000 * 2 == 4000 and 3000 / 500 == 6
assert 5000 / 1000 == 5 and 5 * 3600 == 18000 and 5000 / 500 == 10


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha Eletricidade (cópia das da FIS-ELE-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def q(c, x, y, r, s, a=1.0):
    """carga pequena: + laranja, − azul, com o sinal em branco"""
    if a <= 0:
        return
    cor = E.COR if s == "+" else NEG
    c.drawCircle(x + r * 0.08, y + r * 0.16, r, M.paint("#000000", 0.16 * a))
    c.drawCircle(x, y, r, M.paint(cor, a))
    k, lw = r * 0.52, max(3, r * 0.24)
    M.line(c, x - k, y, x + k, y, BR, a, lw)
    if s == "+":
        M.line(c, x, y - k, x, y + k, BR, a, lw)


def esfera_metal(c, cx, cy, R, a=1.0):
    E.bola(c, cx, cy, R, METAL, a)


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita potência de dez)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def _linha(c, partes, x, y, a, align="center"):
    """linha de tipografia mista parada (para a troca)"""
    w, xs = E._arranjo(partes, x, align)
    for p, xx in zip(partes, xs):
        E.escreve(c, p[0], xx, y, p[2], p[1], p[3] if len(p) > 3 else TINTA, a)


def terra(c, x, y, a=1.0, cor=TINTA):
    """símbolo de terra: três traços, o de cima em y"""
    for i, w in enumerate((90, 60, 30)):
        M.line(c, x - w / 2, y + i * 18, x + w / 2, y + i * 18, cor, a, 6)


def promessa(c, t, C, cena, itens, sz=74):
    """tela "até o fim da aula": órbita à direita e itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", sz, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, desenhos):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, cx, cy) desenha à direita da caixa"""
    if len(itens) == 2:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
        E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
        E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    else:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa", "i", 84), XE, 470, passo=0.14)
        E.frase(c, t, C[cena] + 0.6, ps("de uma coisa", "i", 84), XE, 580, passo=0.14)
    x, w = 820, 1000
    y0 = 230 if len(itens) == 2 else 340
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    if len(itens) == 2:
        q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
        E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    else:
        E.cursor(c, x + w - 30, 560, ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, dy=190):
    """tela "resumindo": itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 380 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)


def cta(c, t, C, cena):
    """inscreva-se (cue c) e bons estudos (cue d), à direita"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1580, 990, "center")


def questao_relogio(c, t, C, cena_pausa, desenho):
    """lado direito da questão: o desenho até a pausa, depois o relógio"""
    if t < C[cena_pausa]:
        desenho()
    else:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=1460, cy=440, r=200)



def celular(c, cx, cy, s, a=1.0, texto="4.000 mAh"):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.5, cy - s, s, 2 * s, s * 0.12, TINTA, a)
    M.rrect(c, cx - s * 0.44, cy - s * 0.9, s * 0.88, s * 1.75, s * 0.06, "#2C3340", a)
    # bateria na tela
    M.rrect(c, cx - s * 0.28, cy - s * 0.45, s * 0.56, s * 0.9, 10, "#FFFFFF", a)
    M.rrect(c, cx - s * 0.1, cy - s * 0.53, s * 0.2, s * 0.1, 4, "#FFFFFF", a)
    M.rrect(c, cx - s * 0.22, cy - s * 0.05, s * 0.44, s * 0.44, 6, CERTO, a)
    E.formula(c, texto, cx, cy + s * 0.75, s * 0.16, "g", "#FFFFFF", a, "center")


def fio_metal(c, x, y, w, h, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x, y - h / 2, w, h, h / 2, METAL, a)


def circuito(c, t, t0, x0, y0, x1, y1, tc=None, te=None):
    """retângulo com pilha no lado esquerdo (+ em cima) e lâmpada em cima; tc = corrente; te = elétrons"""
    mx = (x0 + x1) / 2
    F.fio(c, t, t0, [(x0, (y0 + y1) / 2 - 70), (x0, y0), (mx - 60, y0)])
    F.fio(c, t, t0, [(mx + 60, y0), (x1, y0), (x1, y1), (x0, y1), (x0, (y0 + y1) / 2 + 70)])
    F.pilha(c, t, t0 + 0.3, (x0, (y0 + y1) / 2 + 70), (x0, (y0 + y1) / 2 - 70))
    F.lampada(c, t, t0 + 0.4, (mx - 60, y0), (mx + 60, y0), acesa=tc)
    loop = [(x0, (y0 + y1) / 2 - 70), (x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, (y0 + y1) / 2 + 70)]
    if tc is not None and t >= tc:
        F.corrente(c, t, tc, loop, fecha=False, vel=140)
    if te is not None and t >= te:
        rev = loop[::-1]
        L = [math.dist(rev[i], rev[i + 1]) for i in range(len(rev) - 1)]
        tot = sum(L)
        for k in range(7):
            s = ((t - te) * 110 + k * tot / 7) % tot
            for (xa, ya), (xb, yb), l_ in zip(rev, rev[1:], L):
                if s <= l_:
                    f = s / l_
                    q(c, lerp(xa, xb, f), lerp(ya, yb, f) + (26 if ya == yb else 0), 15, "−", ep(t, te, 0.4))
                    break
                s -= l_


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: celular(c, 1420, 560, 300, a))
        E.foco(c, t, C["s01.a"] + 0.3, 0.5, lambda a: F.medida(c, "4.000", "mAh", XE, 300, 120, COR, a))
        for k, txt, y in (("s01.b", "corrente?", 500), ("s01.c", "energia?", 640)):
            E.frase(c, t, C[k], [("não", "i", 84), ("é", "i", 84), (txt, "g", 80)], XE, y, passo=0.12)
            if t >= C[k] + 0.6:
                E.risco(c, XE - 10, y + 10, XE + 640, y - 50, t, C[k] + 0.6, largura=10)
        E.frase(c, t, C["s01.d"], [("é", "i", 100), ("carga!", "g", 100, CERTO)], XE, 840, passo=0.15)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1600, 560, 240 * ease_back(prog(t, C["s02.a"] + 0.4, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 84), XE, 250, passo=0.14)
        for i, (k, s, dt) in enumerate((("s02.a", "calcular a corrente", 1.4), ("s02.b", "carga pela área", 0), ("s02.c", "o miliampère-hora", 0), ("s02.d", "contínua e alternada", 0))):
            y = 410 + i * 150
            E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
            E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 66, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def eletrons(a, x, y):
        fio_metal(c, x - 170, y, 300, 50, a)
        for i in range(4):
            q(c, x - 130 + i * 75, y, 16, "−", a)

    def area(a, x, y):
        M.line(c, x - 150, y + 60, x + 110, y + 60, TINTA, a, 4)
        M.line(c, x - 150, y + 60, x - 150, y - 80, TINTA, a, 4)
        c.drawRect(skia.Rect.MakeLTRB(x - 148, y - 30, x + 60, y + 58), M.paint(E.COR, 0.35 * a))
        M.line(c, x - 150, y - 30, x + 60, y - 30, E.COR, a, 5)
        E.escreve(c, "v × t", x - 140, y - 92, 36, "b", TINTA2, a)
    lembrete(c, t, C, "s03", (("s03.b", "carga em coulomb;", "no metal: elétrons"), ("s03.c", "gráfico v × t:", "área = deslocamento")), (eletrons, area))


# ---------------- corrente ----------------
def b_corrente(c, t, C, b):
    def s04():
        x, y, w = 760, 540, 1000
        E.foco(c, t, C["s04"], 0.5, lambda a: fio_metal(c, x, y, w, 120, a))
        org = ep(t, C["s04.c"], 0.8)
        for i in range(9):
            bx = x + 60 + i * 105
            jit = (1 - org)
            dx = 30 * math.sin(t * 3.1 + i * 1.7) * jit + (-(t - C["s04.c"]) * 110 % 105 if t >= C["s04.c"] else 0) * org
            dy = 30 * math.cos(t * 2.3 + i * 2.1) * jit
            q(c, bx + dx, y + dy, 20, "−", ep(t, C["s04.a"], 0.4))
        if t >= C["s04.b"]:
            F.fio(c, t, C["s04.b"], [(x, y), (x - 80, y), (x - 80, y + 260), (x + w / 2 - 70, y + 260)])
            F.fio(c, t, C["s04.b"], [(x + w, y), (x + w + 80, y), (x + w + 80, y + 260), (x + w / 2 + 70, y + 260)])
            F.pilha(c, t, C["s04.b"] + 0.3, (x + w / 2 - 70, y + 260), (x + w / 2 + 70, y + 260))
        E.frase(c, t, C["s04.a"], ps("elétrons soltos, para todo lado", "i", 64), XE, 230, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("com a pilha:", "i", 64) + [("um", "g", 60), ("sentido", "g", 60), ("só", "g", 60)], XE, 340, passo=0.1)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "CORRENTE ELÉTRICA", W / 2, 960, 70, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("carga que passa por segundo", "i", 64, TINTA2), XE, 200, passo=0.1)
            F.formula_legenda(c, t, C["s05.b"], "i = f{Q}{Δt}", [("i", "corrente", "A, ampère"), ("Q", "carga que passou", "C"), ("Δt", "intervalo de tempo", "s")],
                              XE + 40, 430, 160, tl=[C["s05.c"], C["s05.d"], C["s05.e"]], size_l=58)
            E.foco(c, t, C["s05.f"], 0.5, lambda a: pilula_f(c, "1 A = 1 C/s", 1460, 400, 84, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            E.foco(c, t, C["s06.a"], 0.5, lambda a: (E.escreve(c, "Q =", XE, 300, 90, "g", TINTA, a), F.medida(c, 30, "C", XE + 190, 300, 90, COR, a)))
            E.foco(c, t, C["s06.b"], 0.5, lambda a: (E.escreve(c, "Δt =", XE + 640, 300, 90, "g", TINTA, a), F.medida(c, 10, "s", XE + 860, 300, 90, COR, a)))
            E.formula_em(c, t, C["s06.c"], "i = f{30}{10}", XE, 560, 110, "g", TINTA)
            E.foco(c, t, C["s06.d"], 0.5, lambda a: pilula_f(c, "i = 3 A", 1200, 520, 100, a=a))
            E.foco(c, t, C["s06.d"] + 0.8, 0.4, lambda a: E.escreve(c, "3 coulombs a cada segundo", XE, 800, 60, "i", TINTA2, a))
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07"], ps("um detalhe de prova", "i", 66, TINTA2), XE, 200, passo=0.1)
    circuito(c, t, C["s07"] + 0.2, 1000, 330, 1720, 900, tc=C["s07.a"], te=C["s07.c"])
    E.frase(c, t, C["s07.a"], [("corrente:", "g", 62, COR)] + ps("como uma carga +", "i", 64), XE, 360, passo=0.1)
    E.frase(c, t, C["s07.b"], ps("sai do polo + da pilha", "i", 62), XE, 470, passo=0.1)
    E.frase(c, t, C["s07.c"], [("elétrons:", "g", 62, NEG)] + ps("ao contrário", "i", 64), XE, 610, passo=0.1)
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "sentido convencional", 520, 790, 54, "g", fundo=TINTA, a=a))


# ---------------- gráfico i × t ----------------
def i_t(v):
    return 2.0 if v <= 5 else max(0.0, 2.0 - 0.5 * (v - 5))


def b_grafico(c, t, C, b):
    P = F.grafico(c, t, C["s08.a"], 900, 300, 880, 560, 0, 10, 0, 3, eixo_x="t (s)", eixo_y="i (A)", passo=1, marcas_x=(5, 9), marcas_y=(2,))
    E.curva(c, t, C["s08.a"] + 0.6, P, i_t, 0, 9.6, d=1.0)
    E.frase(c, t, C["s08.a"], ps("gráfico da corrente", "i", 62), XE, 260, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("área embaixo da linha =", "i", 58), XE, 380, passo=0.1)
    E.frase(c, t, C["s08.c"], [("a", "i", 80), ("carga", "g", 76, COR)], XE, 480, passo=0.12)
    F.area_graf(c, t, C["s08.e"], P, i_t, 0, 5, "10 C")
    E.foco(c, t, C["s08.d"], 0.5, lambda a: E.escreve(c, "2 A por 5 s", XE, 620, 60, "g", TINTA, a))
    E.foco(c, t, C["s08.e"], 0.5, lambda a: E.formula(c, "5 · 2 = 10 C", XE, 720, 60, "g", COR, a))
    if t >= C["s09"]:
        F.area_graf(c, t, C["s09.b"], P, i_t, 5, 9, "4 C", cor=E.mix(E.COR, "#FFFFFF", 0.0), alfa=0.4)
        E.foco(c, t, C["s09.a"], 0.4, lambda a: E.escreve(c, "cai de 2 a 0 em 4 s", XE, 820, 52, "i", TINTA, a))
        E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "f{4 · 2}{2} = 4 C", XE, 920, 60, "g", COR, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: pilula_f(c, "total: 14 C", 1340, 990, 60, fundo=CERTO, a=a))


# ---------------- bateria ----------------
def b_bateria(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10"], [("a", "i", 84), ("bateria", "g", 80, COR)], XE, 230, passo=0.12)
        E.formula_em(c, t, C["s10.a"], "mAh = corrente × tempo", XE, 400, 84, "g", TINTA)
        E.formula_em(c, t, C["s10.b"], "corrente × tempo = carga", XE, 540, 84, "g", COR)
        E.formula_em(c, t, C["s10.c"], "1 mAh = 10^{−3} A · 3.600 s", XE, 740, 84, "g", TINTA)
        E.foco(c, t, C["s10.d"], 0.5, lambda a: pilula_f(c, "1 mAh = 3,6 C", 1500, 900, 80, a=a))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.foco(c, t, C["s11"], 0.5, lambda a: celular(c, 1520, 560, 300, a))
    E.formula_em(c, t, C["s11.a"], "4.000 mAh = 4 Ah", XE, 300, 90, "g", TINTA)
    E.formula_em(c, t, C["s11.b"], "4 · 3.600", XE, 470, 90, "g", TINTA2)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: pilula_f(c, "14.400 C", XE + 330, 610, 90, a=a))
    E.frase(c, t, C["s11.d"], ps("a carga entregue até descarregar", "i", 58, TINTA2), XE, 820, passo=0.1)


# ---------------- contínua e alternada ----------------
def b_tipos(c, t, C, b):
    E.frase(c, t, C["s12"], ps("dois tipos de corrente", "i", 70, TINTA2), W / 2, 180, "center", 0.12)
    P1 = F.grafico(c, t, C["s12.a"], 200, 320, 620, 360, 0, 4, -2, 2, eixo_x="t", eixo_y="i", passo=1, marcas_x=(), marcas_y=(), grade=False)
    E.curva(c, t, C["s12.a"] + 0.5, P1, lambda v: 1.3, 0, 3.8, d=0.8)
    P2 = F.grafico(c, t, C["s12.c"], 1080, 320, 620, 360, 0, 4, -2, 2, eixo_x="t", eixo_y="i", passo=1, marcas_x=(), marcas_y=(), grade=False)
    E.curva(c, t, C["s12.c"] + 0.5, P2, lambda v: 1.4 * math.sin(2 * math.pi * v / 1.3), 0, 3.8, d=1.0)
    E.foco(c, t, C["s12.a"] + 0.3, 0.4, lambda a: centro(c, "pilha e bateria", 510, 800, 52, "i", TINTA, a))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.pilula(c, "CONTÍNUA", 510, 900, 60, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s12.c"] + 0.3, 0.4, lambda a: centro(c, "tomada: vai e volta", 1390, 800, 52, "i", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "60 vezes por segundo", 1390, 250, 40, "b", fundo=TINTA2, a=a))
    E.foco(c, t, C["s12.e"], 0.5, lambda a: E.pilula(c, "ALTERNADA", 1390, 900, 60, "g", fundo=NEG, a=a))
    E.foco(c, t, C["s12.f"], 0.5, lambda a: E.pilula(c, "carregador: alternada → contínua", W / 2, 1010, 42, "b", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("mAh é corrente?", "i", 80), XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s13.b"], "4.000 mAh  ≠  4.000 mA", XE, 400, 90, "g", ERRADO)
    E.formula_em(c, t, C["s13.c"], "400 mA × 10 h = 4.000 mAh", XE, 590, 84, "g", TINTA)
    E.formula_em(c, t, C["s13.d"], "2.000 mA × 2 h = 4.000 mAh", XE, 740, 84, "g", TINTA)
    E.foco(c, t, C["s13.e"], 0.5, lambda a: E.pilula(c, "o que não muda é a carga", W / 2, 920, 60, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s14.a"], ps("quanto tempo a bateria dura?", "i", 72, CLARO), W / 2, 290, "center", 0.12)
        E.formula_em(c, t, C["s14.b"], "tempo = f{mAh}{mA}", W / 2, 500, 110, "g", BR, "center")
        E.foco(c, t, C["s14.c"], 0.5, lambda a: E.escreve(c, "mA corta com mA: sobra h", W / 2 - 330, 660, 56, "i", CLARO, a))
        E.formula_em(c, t, C["s14.d"], "f{3.000}{500}", W / 2 - 150, 860, 100, "g", BR, "center")
        E.foco(c, t, C["s14.e"], 0.5, lambda a: pilula_f(c, "6 h", W / 2 + 200, 830, 90, a=a))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.formula_em(c, t, C["s15.a"], "Q = i · Δt   →   Δt = f{Q}{i}", W / 2, 360, 96, "g", BR, "center")
    E.frase(c, t, C["s15.b"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("corrente mudando", "i", 70, CLARO), W / 2, 640, "center", 0.12)
    E.frase(c, t, C["s15.b"] + 1.6, [("→", "g", 66, CLARO), ("área", "g", 66, BR), ("do", "i", 70, CLARO), ("gráfico", "g", 66, BR)], W / 2, 770, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"] - 0.5, [("bateria", "i", 76), ("portátil:", "i", 76)], XE, 330, passo=0.12)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: F.medida(c, "5.000", "mAh", XE, 460, 100, COR, a))
    E.frase(c, t, C["s16.b"], [("quantos", "i", 76), ("coulombs?", "g", 72, COR)], XE, 620, passo=0.15)
    E.frase(c, t, C["s16.c"], [("quantas", "i", 76), ("horas", "g", 72, COR), ("a", "i", 76)], XE, 760, passo=0.15)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: F.medida(c, 500, "mA?", XE + 530, 760, 76, COR, a))
    questao_relogio(c, t, C, "s17", lambda: E.foco(c, t, C["s16.a"], 0.5, lambda a: celular(c, 1460, 560, 300, a, "5.000 mAh")))


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s18.a"], "5.000 mAh = 5 Ah", XE, 260, 90, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "5 · 3.600", XE, 430, 90, "g", TINTA2)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: pilula_f(c, "18.000 C", XE + 900, 400, 90, a=a))
    E.formula_em(c, t, C["s18.d"], "tempo = f{5.000}{500}", XE, 720, 96, "g", TINTA)
    E.foco(c, t, C["s18.e"], 0.5, lambda a: pilula_f(c, "10 h", XE + 1000, 690, 96, fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s19", (("s19.a", [("i = Q ÷ Δt,", "g", 70), ("em", "i", 72), ("ampère", "g", 68, COR)]),
                                ("s19.b", [("gráfico", "i", 72), ("i × t:", "g", 68), ("área", "i", 72), ("=", "g", 68), ("carga", "g", 68, COR)]),
                                ("s19.c", [("mAh", "g", 70), ("é", "i", 72), ("carga,", "g", 68, COR), ("não", "i", 72), ("corrente", "i", 72)])))
    E.saida(c, t, C["s20"] - 0.1, tela)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("tensão", "g", 110, COR), ("e", "i", 110), ("resistência", "g", 110, COR)], XE, 400, passo=0.15)
    F.fio(c, t, C["s20.b"], [(300, 760), (420, 760)])
    F.fio(c, t, C["s20.b"], [(620, 760), (740, 760)])
    F.resistor(c, t, C["s20.b"] + 0.2, (420, 760), (620, 760), "R")
    E.foco(c, t, C["s20.b"] + 0.5, 0.5, lambda a: E.formula(c, "U = R · i", 900, 790, 90, "g", TINTA, a))
    cta(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, corrente=b_corrente, grafico=b_grafico, bateria=b_bateria, tipos=b_tipos,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
