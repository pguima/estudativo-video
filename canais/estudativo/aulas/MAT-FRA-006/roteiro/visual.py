"""Visual — Estudativo · MAT-FRA-006: praticando o que é uma fração.
Aula de prática: cinco situações, cada uma com selo de progresso, relógio de pausa e um desenho próprio:
calendário (24 de 30 dias vira 4 de 5 linhas), barras das entradas, estrada, barra do preço e tortas.
Todo instante vem de C[...]: o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, barra, ponte, pontes, frac_q, centro, linha
import motor as M
import skia

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-006_praticando_o_que_e_uma_fracao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao3", "atalho", "questao5", "fim"))
BR = "#FFFFFF"
assert 24 // 6 == 4 and 30 // 6 == 5 and 24 // 2 == 12 and 30 // 2 == 15 and 12 // 3 == 4 and 15 // 3 == 5
assert 2 * 8 == 16 and 5 * 3 == 15
assert 240 // 6 == 40 and 40 * 5 == 200 and 240 - 40 == 200
assert 450 // 3 == 150 and 150 * 7 == 1050 and 1050 // 7 == 150 and 150 * 3 == 450
assert 6 * 3 == 18 and 20 - 18 == 2 and 10 // 3 == 3 and 10 % 3 == 1


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


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.2):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


def relogio(c, t, t0, cx=1490, cy=340, r0=190):
    """relógio de pausa: enche em 3 segundos"""
    r = r0 * ease_back(prog(t, t0, 0.6))
    if r <= 0:
        return
    E.bola(c, cx, cy, r)
    f = M.clamp(prog(t, t0 + 0.8, 3.0))
    if f > 0:
        E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
    k = r0 / 190
    for dx in (-40, 40):
        M.rrect(c, cx + (dx - 20) * k, cy - 72 * k, 40 * k, 144 * k, 11, E.SOBRE, ep(t, t0 + 0.2, 0.4))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + r0 + 104, 60, "i", TINTA, a))


def selo(c, t, t0, n):
    """situação n de 5, com cinco pontos de progresso"""
    s = f"situação {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def conta(c, t, ti, s, x, y, size=64, cor=None, est="b"):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, s, x, y, size, est, cor or TINTA, a))


def misto(c, t, ti, i, n, d, cx, cy, s, cor=None):
    """número misto: o inteiro grande e a fração ao lado"""
    def fn(a):
        w = E.larg(str(i), "g", s * 1.6)
        E.escreve(c, str(i), cx - w - s * 0.2, cy + s * 0.56, s * 1.6, "g", cor or COR, a)
        E.fracao(c, n, d, cx + s * 0.45, cy, s, cor or COR, a)
    E.foco(c, t, ti, 0.5, fn)


def calendario(c, t, x, y, cel, ti, dt, tp, dtp, linhas_t=None, a=1.0):
    """o mês: 6 colunas e 5 linhas = 30 dias; tp = quando os 24 pintam; linhas_t = quando as 5 linhas se separam"""
    gap = 8
    m = ep(t, linhas_t, 0.6) if linhas_t is not None else 0
    for i in range(30):
        cx, cy = x + (i % 6) * (cel + gap), y + (i // 6) * (cel + gap + 14 * m)
        q = ease_back(prog(t, ti + i * dt, 0.35))
        if q <= 0:
            continue
        p = ep(t, tp + i * dtp, 0.3) if i < 24 else 0
        cor = M.mix(E.VAZIO, E.COR, p)
        r = cel * q
        M.rrect(c, cx + (cel - r) / 2, cy + (cel - r) / 2, r, r, 10, cor, a * min(1.0, q * 2))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx + (cel - r) / 2, cy + (cel - r) / 2, r, r), 10, 10), M.paint(TINTA, a * min(1.0, q * 2), stroke=2.5))


def torta(c, cx, cy, r, n, pint, a=1.0, cortes=None):
    """torta redonda em n fatias com `pint` pintadas; cortes = fatias cujo corte aparece (padrão: todos)"""
    if a <= 0:
        return
    rect = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    c.drawCircle(cx + 4, cy + 8, r, s)
    c.drawCircle(cx, cy, r, M.paint(E.VAZIO, a))
    if pint > 0:
        c.drawArc(rect, -90, 360 * min(pint, n) / n, True, M.paint(E.COR, a))
    for i in range(n):
        if cortes is None or i in cortes:
            ang = math.radians(-90 + i * 360 / n)
            M.line(c, cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), BR if i <= pint else FIO, a, 4)
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=3))


def carro(c, x, y, w, a=1.0):
    """carrinho de perfil; (x, y) = chão, x na frente do carro"""
    h = w * 0.34
    x0 = x - w
    p = skia.Path()
    p.moveTo(x0, y - h * 0.3); p.lineTo(x0 + w * 0.2, y - h * 0.3); p.lineTo(x0 + w * 0.34, y - h); p.lineTo(x0 + w * 0.72, y - h)
    p.lineTo(x0 + w * 0.86, y - h * 0.3); p.lineTo(x, y - h * 0.3); p.lineTo(x, y - h * 0.1); p.lineTo(x0, y - h * 0.1); p.close()
    c.drawPath(p, M.paint(TINTA, a))
    for dx in (0.22, 0.78):
        c.drawCircle(x0 + w * dx, y - h * 0.1, w * 0.09, M.paint(TINTA, a))
        c.drawCircle(x0 + w * dx, y - h * 0.1, w * 0.04, M.paint("#FFFFFF", a))


def barra_n(c, x, y, w, h, n, pint, cortes_p=1.0, a=1.0):
    """barra em n partes iguais com `pint` pintadas"""
    barra(c, x, y, w, h, pint / n, [(i / n, cortes_p) for i in range(1, n)], a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("situações", "g", 180, COR), XE, 350, passo=0.25)
    E.frase(c, t, a_ + 0.8, ps("do dia a dia", "i", 120), XE, 490, passo=0.2)
    E.frase(c, t, lerp(a_, b_, 0.5), ps("criadas para esta aula", "i", 72), XE, 590, passo=0.15)
    for i, (s, cx) in enumerate((("pause", 440), ("resolva", 960), ("confira", 1480))):
        ti = b_ + i * 0.5
        E.foco(c, t, ti, 0.5, lambda p: (num_bola(c, str(i + 1), cx - 190, 730, 56, 64, p), E.escreve(c, s, cx - 110, 755, 92, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.55), ps("errar aqui", "i", 88) + ps("não custa nada", "g", 80, COR), W / 2, 910, "center", 0.18)
    E.frase(c, t, lerp(b_, C["s01.end"], 0.8), ps("e ensina mais do que só assistir", "i", 68), W / 2, 1000, "center", 0.13)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 110), XE, 340)
    E.frase(c, t, C["s02"] + 1.0, ps("quatro", "g", 130, COR), XE, 490)
    E.frase(c, t, C["s02"] + 1.3, ps("ferramentas", "i", 110), XE, 610)
    x, w = 880, 860
    for i, (k, s) in enumerate((("s02.a", "simplificar"), ("s02.b", "comparar"), ("s02.c", "fração de uma quantidade"), ("s02.d", "número misto"))):
        y = 180 + i * 165
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 134, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 62, COR)], x + 44, y + 90)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.5), ps("travou?", "i", 62, COR), XE, 730, passo=0.13)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.6), ps("procure a aula no canal", "i", 60), XE, 810, passo=0.13)


# ---------------- situação 1: simplificar ----------------
def b_questao1(c, t, C, b):
    a_, b_, c_, d_ = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    selo(c, t, a_, 1)
    linha(c, t, [("um mês de", "i", 96, TINTA, b_ - 0.3), ("30 dias", "g", 96, COR, b_)], XE, 330)
    linha(c, t, [("trabalhou", "i", 96, TINTA, c_ - 0.4), ("24", "g", 96, COR, c_)], XE, 460)
    E.frase(c, t, d_, ps("que fração do mês?", "i", 100), XE, 680, passo=0.17)
    E.frase(c, t, d_ + 1.0, ps("na forma", "i", 100) + ps("mais simples", "g", 92, COR), XE, 810, passo=0.2)
    cel = 62
    calendario(c, t, 1190, 672, cel, b_, 0.015, c_ + 0.1, 0.02)
    relogio(c, t, C["s04.a"], 1490, 340, 190)


def b_resposta1(c, t, C, b):
    selo(c, t, C["s05"] - 0.5, 1)
    a_, b_, c_, d_, e_, f_ = (C[f"s05.{k}"] for k in "abcdef")
    cal = C["s05"] + 0.2

    def quadro():
        s, cy, x0, x1 = 150, 400, 310, 880
        fr(c, t, a_, 24, 30, x0, cy, s)
        E.foco(c, t, a_ - 0.8, 0.4, lambda p: E.escreve(c, "parte em cima, total embaixo", XE, 212, 62, "i", TINTA, p))
        E.foco(c, t, b_, 0.45, lambda p: E.pilula(c, "MDC = 6", 310, 620, 56, estilo="g", a=p))
        pontes(c, t, x0 + 130, x1 - 170, cy, s, "÷ 6", c_, d_, size=52)
        if t < e_:
            frac_q(c, t, c_, 4, 5, lerp(c_, d_, 0.6), lerp(d_, e_, 0.6), x1, cy, s)
        E.resultado(c, t, e_, 4, 5, x1, cy, 124, 166, CERTO)
        E.frase(c, t, e_ + 0.3, ps("do mês", "g", 76, CERTO), x1, 650, "center", 0.2)
        calendario(c, t, 1180, 240, 80, cal, 0.012, cal + 0.3, 0.008, linhas_t=e_)
        E.frase(c, t, f_, ps("embaixo vai", "i", 88) + ps("o mês inteiro,", "g", 80, COR) + ps("não só as folgas", "i", 88), W / 2, 930, "center", 0.18)
        q = ep(t, f_, 0.5)
        E.caixa_pontilhada(c, 1168, 228, 6 * 88 + 8, 5 * 102 + 8, q, COR, prog_=q)
    E.saida(c, t, C["s06"] - 0.1, quadro)

    if t >= C["s06"]:
        a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
        E.frase(c, t, C["s06"] + 0.2, ps("não achou o MDC", "i", 96) + ps("de primeira?", "g", 88, COR), W / 2, 280, "center", 0.2)
        E.frase(c, t, lerp(C["s06"], a6, 0.65), ps("sem problema", "i", 80), W / 2, 380, "center", 0.2)
        s, cy, x0, x1, x2 = 170, 620, 340, 960, 1570
        fr(c, t, a6 - 0.2, 24, 30, x0, cy, s)
        pontes(c, t, x0 + 140, x1 - 125, cy, s, "÷ 2", a6, a6, size=60)
        fr(c, t, a6 + 0.5, 12, 15, x1, cy, s)
        pontes(c, t, x1 + 125, x2 - 190, cy, s, "÷ 3", b6, b6, size=60)
        E.resultado(c, t, c6, 4, 5, x2, cy, 124, 166, CERTO)
        E.frase(c, t, c6 + 0.3, ps("os mesmos", "i", 92) + ps("quatro quintos", "g", 84, CERTO), W / 2, 930, "center", 0.2)


# ---------------- situação 2: comparar ----------------
def b_questao2(c, t, C, b):
    a_, b_, c_, d_ = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    selo(c, t, a_, 2)
    E.frase(c, t, lerp(a_, b_, 0.25), ps("a mesma geladeira,", "i", 92), XE, 290, passo=0.17)
    E.frase(c, t, lerp(a_, b_, 0.6), ps("o mesmo preço", "i", 92), XE, 400, passo=0.17)
    s, cy = 130, 590
    E.foco(c, t, b_, 0.45, lambda p: E.escreve(c, "loja A", XE, cy + 26, 84, "g", TINTA, p))
    fr(c, t, b_ + 0.2, 2, 5, 560, cy, s, COR)
    E.foco(c, t, c_, 0.45, lambda p: E.escreve(c, "loja B", 720, cy + 26, 84, "g", TINTA, p))
    fr(c, t, c_ + 0.2, 3, 8, 1110, cy, s, COR)
    E.frase(c, t, d_, ps("qual pede a", "i", 100) + ps("menor entrada?", "g", 96, COR), XE, 900, passo=0.2)
    relogio(c, t, C["s08.a"], 1520, 340, 170)


def b_resposta2(c, t, C, b):
    selo(c, t, C["s09"] - 0.5, 2)
    a_, b_, c_, d_, e_ = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]

    def cruz():
        E.frase(c, t, C["s09"] + 0.2, ps("mesmo preço: compare as frações", "i", 66), 810, 128, passo=0.12)
        E.frase(c, t, lerp(C["s09"], a_, 0.6), ps("teste da cruz", "g", 96, COR), W / 2, 270, "center", 0.2)
        s, xa, xb, y = 170, 700, 1220, 500
        fr(c, t, C["s09"] + 0.3, 2, 5, xa, y, s)
        fr(c, t, C["s09"] + 0.5, 3, 8, xb, y, s)
        ny, dy = y - s * 0.565, y + s * 0.535
        if t >= a_:
            M.line(c, xa + 70, ny + 8, xb - 70, dy - 8, COR, 1.0, 7, progress=ep(t, a_, 0.6))
        if t >= b_:
            M.line(c, xa + 70, dy - 8, xb - 70, ny + 8, CLARO, 1.0, 7, progress=ep(t, b_, 0.6))
        c.drawCircle((xa + xb) / 2, y, 62, M.paint(E.PAPEL))
        if t >= c_:
            sinal(c, t, c_, ">", (xa + xb) / 2, y - 3, 120, COR)
        conta(c, t, a_ + 0.5, "2 × 8", 170, y - 34, 72, TINTA2)
        conta(c, t, a_ + 0.9, "= 16", 170, y + 62, 100, COR, "g")
        conta(c, t, b_ + 0.5, "5 × 3", 1450, y - 34, 72, TINTA2)
        conta(c, t, b_ + 0.9, "= 15", 1450, y + 62, 100, COR, "g")
        E.frase(c, t, c_ + 0.3, ps("2/5", "g", 76, COR) + ps("é a fração maior", "i", 84), W / 2, 760, "center", 0.17)
        yb, sb = 880, 80
        E.frase(c, t, lerp(c_, d_, 0.6), ps("pelo MMC:", "i", 76), XE, yb + 28, passo=0.17)
        fr(c, t, d_, 16, 40, 770, yb, sb, COR)
        if t >= e_:
            sinal(c, t, e_, ">", 960, yb + 8, 90, TINTA2)
        fr(c, t, e_, 15, 40, 1150, yb, sb, COR)
    E.saida(c, t, C["s10"] - 0.1, cruz)

    if t >= C["s10"]:
        a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
        E.frase(c, t, C["s10"] + 0.2, ps("cuidado com a pergunta:", "i", 80), 810, 134, passo=0.13)
        E.frase(c, t, a0, ps("ela quer a", "i", 104) + ps("menor entrada", "g", 96, COR), W / 2, 280, "center", 0.2)
        x, w, h = 500, 1200, 120
        E.foco(c, t, C["s10"] + 0.3, 0.5, lambda p: (E.escreve(c, "loja A", XE, 410, 72, "g", TINTA, p), barra_n(c, x, 345, w, h, 5, 2, a=p)))
        E.foco(c, t, C["s10"] + 0.6, 0.5, lambda p: (E.escreve(c, "loja B", XE, 570, 72, "g", TINTA, p), barra_n(c, x, 505, w, h, 8, 3, a=p)))
        E.foco(c, t, C["s10"] + 0.3, 0.5, lambda p: E.fracao(c, 2, 5, 400, 395, 62, COR, p))
        E.foco(c, t, C["s10"] + 0.6, 0.5, lambda p: E.fracao(c, 3, 8, 400, 555, 62, COR, p))
        q = ep(t, b0, 0.5)
        E.caixa_pontilhada(c, 150, 490, 1566, 150, q, CERTO, prog_=q)
        E.frase(c, t, b0, ps("a resposta é a", "i", 92) + ps("loja B", "g", 96, CERTO), W / 2, 760, "center", 0.2)
        E.frase(c, t, c0, ps("conta certa,", "i", 76) + ps("resposta ao contrário:", "g", 70, ERRADO) + ps("o erro mais comum", "i", 76), W / 2, 880, "center", 0.15)
        E.frase(c, t, lerp(c0, C["s10.end"], 0.55), ps("leia o fim do enunciado de novo", "i", 76), W / 2, 985, "center", 0.14)


# ---------------- situação 3: fração de uma quantidade ----------------
def estrada(c, t, x, y, w, h, q, a, n=6):
    """a viagem: barra em 6 partes que se pinta até q, com o carro na frente"""
    barra(c, x, y, w, h, 1.0, [(i / n, 1) for i in range(1, n)], a, enche=q)
    carro(c, x + w * q, y - 8, 170, a)


def b_questao3(c, t, C, b):
    a_, b_, c_, d_ = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    selo(c, t, a_, 3)
    x, y, w, h = XE, 700, 1100, 100
    linha(c, t, [("viagem de", "i", 96, TINTA, b_ - 0.3), ("240 km", "g", 100, COR, b_)], XE, 310)
    linha(c, t, [("o carro já percorreu", "i", 84, TINTA, c_ - 0.6)], XE, 430)
    fr(c, t, c_, 5, 6, 1040, 400, 96, COR)
    E.foco(c, t, b_ + 0.1, 0.45, lambda p: estrada(c, t, x, y, w, h, 5 / 6 * ep(t, c_ + 0.2, 1.0) + 1e-4, p))
    E.frase(c, t, d_, ps("quantos quilômetros", "i", 96) + ps("já percorreu?", "g", 88, COR), XE, 920, passo=0.2)
    relogio(c, t, C["s12.a"], 1560, 340, 170)


def b_resposta3(c, t, C, b):
    selo(c, t, C["s13"] - 0.5, 3)
    a_, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
    x, y, w, h = XE, 330, 1580, 140
    q = 5 / 6
    E.foco(c, t, C["s13"] + 0.2, 0.45, lambda p: estrada(c, t, x, y, w, h, q, p))
    # 240 é o total
    E.foco(c, t, a_, 0.45, lambda p: (E.chave(c, x, x + w, y + h + 12, TINTA2, p, 18, 4, abre=False),
                                      centro(c, "240 km: o total", x + w / 2, y + h + 96, 64, "b", TINTA, p)))
    E.frase(c, t, lerp(a_, b_, 0.3), ps("divide pelo de baixo,", "i", 80) + ps("multiplica pelo de cima", "g", 72, COR), W / 2, 680, "center", 0.17)
    for i in range(6):
        cx = x + w * (i + 0.5) / 6
        E.foco(c, t, b_ + 0.5 + i * 0.1, 0.35, lambda p: centro(c, "40", cx, y + h / 2 + 26, 74, "g", BR if i < 5 else TINTA, p), sobe=8)
    conta(c, t, b_, "240 ÷ 6 = 40", 330, 840, 84, TINTA)
    conta(c, t, c_, "40 × 5 =", 1000, 840, 84, TINTA)
    E.foco(c, t, c_ + 0.5, 0.5, lambda p: (num_bola(c, "200", 1490, 815, 120, 90, p, CERTO, BR), E.escreve(c, "km", 1630, 840, 76, "i", CERTO, p)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a_, b_, c_ = C["s14.a"], C["s14.b"], C["s14.c"]
    x, y, w, h = 190, 400, 1540, 180

    def tirar():
        E.frase(c, t, C["s14"] + 0.3, ps("um atalho de prova", "i", 90, CLARO), W / 2, 180, "center")
        E.frase(c, t, a_, ps("tire o", "i", 104, BR) + ps("pedaço que falta", "g", 100, BR), W / 2, 310, "center", 0.2)
        sai = ep(t, b_, 0.7)
        ped = [(i, CLARO, ep(t, C["s14"] + 0.4 + i * 0.1, 0.4)) for i in range(5)] + [(5, E.ERRADO, ep(t, C["s14"] + 0.9, 0.4), 170 * sai)]
        E.foco(c, t, C["s14"] + 0.3, 0.45, lambda p: E.chocolate(c, x, y, w, h, 6, ped, p, 1.0, True))
        E.foco(c, t, lerp(a_, b_, 0.5), 0.45, lambda p: centro(c, "5/6 é tudo, menos 1/6", W / 2 - 200, 690, 72, "b", BR, p))
        linha(c, t, [("240", "g", 130, BR, b_), ("−", "g", 110, CLARO, b_ + 0.4), ("40", "g", 130, ERRADO, b_ + 0.7), ("=", "g", 110, CLARO, c_ - 0.1)], 400, 900)
        E.foco(c, t, c_, 0.5, lambda p: (num_bola(c, "200", 1250, 855, 130, 100, p, CERTO, BR), E.escreve(c, "km", 1400, 900, 90, "i", BR, p)))
    E.saida(c, t, C["s15"] - 0.1, tirar)

    if t >= C["s15"]:
        a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, C["s15"] + 0.2, ps("funciona porque", "i", 90, CLARO), W / 2, 180, "center")
        E.frase(c, t, a5, ps("falta só", "i", 104, BR) + ps("uma parte", "g", 100, BR) + ps("para o inteiro", "i", 104, BR), W / 2, 310, "center", 0.2)
        E.frase(c, t, b5 - 0.5, ps("não compensa quando falta muito", "i", 78, CLARO), XE, 480, passo=0.13)
        fr(c, t, b5, 2, 7, 280, 680, 130, BR)
        n = 7
        ped = [(i, CLARO, ep(t, b5 + 0.2 + i * 0.1, 0.4)) for i in range(2)]
        E.foco(c, t, b5 + 0.1, 0.45, lambda p: E.chocolate(c, 430, 610, 1300, 150, n, ped, p, 1.0, True))
        E.foco(c, t, b5 + 0.9, 0.45, lambda p: E.escreve(c, "faltam 5 partes", 900, 850, 72, "b", CLARO, p))
        E.frase(c, t, c5, ps("aí, vale", "i", 92, CLARO) + ps("a conta normal", "g", 88, BR), W / 2, 980, "center", 0.2)


# ---------------- situação 4: da parte para o total ----------------
def b_questao4(c, t, C, b):
    a_, b_, c_, d_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    selo(c, t, a_, 4)
    linha(c, t, [("juntou", "i", 96, TINTA, b_ - 0.3), ("R$ 450", "g", 110, COR, b_)], XE, 320)
    linha(c, t, [("que são", "i", 96, TINTA, c_ - 0.3)], XE, 510)
    fr(c, t, c_, 3, 7, 620, 480, 120, COR)
    linha(c, t, [("do preço", "i", 96, TINTA, c_ + 0.5)], 730, 510)
    x, y, w, h = XE, 630, 1120, 120
    E.foco(c, t, c_ + 0.3, 0.45, lambda p: barra_n(c, x, y, w, h, 7, 3, a=p))
    E.frase(c, t, d_, ps("quanto custa", "i", 104) + ps("a televisão?", "g", 96, COR), XE, 880, passo=0.2)
    relogio(c, t, C["s17.a"], 1560, 340, 170)


def b_resposta4(c, t, C, b):
    selo(c, t, C["s18"] - 0.5, 4)
    a_, b_ = C["s18.a"], C["s18.b"]
    a9, b9, c9, d9, e9 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"], C["s19.e"]
    x, y, w, h = XE, 300, 1580, 140
    E.foco(c, t, C["s18"] + 0.2, 0.45, lambda p: barra_n(c, x, y, w, h, 7, 3, a=p))
    # a parte: 3 de 7
    E.foco(c, t, a_, 0.45, lambda p: (E.chave(c, x, x + w * 3 / 7, y - 12, COR, p, -16, 4, abre=False),
                                      centro(c, "R$ 450 é a parte", x + w * 1.5 / 7, y - 44, 56, "b", COR, p)))
    for i in range(7):
        cx = x + w * (i + 0.5) / 7
        ti = b_ + 0.7 + i * 0.08 if i < 3 else a9 + 0.2 + (i - 3) * 0.1
        E.foco(c, t, ti, 0.35, lambda p: centro(c, "150", cx, y + h / 2 + 22, 62, "g", BR if i < 3 else TINTA, p), sobe=8)
    E.foco(c, t, a9, 0.45, lambda p: (E.chave(c, x, x + w, y + h + 12, TINTA2, p, 18, 4, abre=False)))

    def um_setimo():
        conta(c, t, b_, "450 ÷ 3 = 150", XE, 640, 92, TINTA)
        E.frase(c, t, lerp(b_, C["s18.end"], 0.65), ps("esse é o valor de", "i", 80), XE, 770, passo=0.15)
        fr(c, t, lerp(b_, C["s18.end"], 0.8), 1, 7, 900, 740, 100, COR)
    E.saida(c, t, C["s19"] - 0.1, um_setimo)

    if t >= C["s19"]:
        conta(c, t, a9, "150 × 7 =", XE, 640, 92, TINTA)
        E.foco(c, t, b9, 0.5, lambda p: E.pilula(c, "R$ 1.050", 880, 610, 84, estilo="g", fundo=CERTO, cor=BR, a=p))
        E.frase(c, t, c9, ps("maior que a parte:", "i", 80) + ps("faz sentido", "g", 76, CERTO), XE, 770, passo=0.15)
        E.frase(c, t, d9 - 0.5, ps("para conferir:", "i", 76), XE, 900, passo=0.15)
        conta(c, t, d9, "1.050 ÷ 7 = 150", 620, 900, 72, TINTA)
        conta(c, t, e9, "× 3 = 450", 1270, 900, 72, CERTO)
        E.frase(c, t, lerp(e9, C["s19.end"], 0.6), ps("bateu", "g", 84, CERTO), 1370, 770, passo=0.2)


# ---------------- situação 5: número misto ----------------
def b_questao5(c, t, C, b):
    a_, b_, c_, d_ = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    selo(c, t, a_ + 0.1, 5)
    E.frase(c, t, lerp(a_, b_, 0.25), ps("a última situação junta tudo", "i", 84), XE, 280, passo=0.15)
    E.foco(c, t, b_, 0.5, lambda p: torta(c, 370, 530, 170, 6, 0, p))
    linha(c, t, [("cada torta:", "i", 84, TINTA, b_), ("6 pedaços", "g", 84, COR, b_ + 0.4)], 590, 480)
    linha(c, t, [("hoje:", "i", 84, TINTA, c_), ("20 pedaços", "g", 84, COR, c_ + 0.3)], 590, 610)
    E.frase(c, t, d_, ps("quantas tortas?", "i", 104), XE, 830, passo=0.2)
    E.frase(c, t, d_ + 0.9, ps("em número misto,", "g", 72, COR) + ps("na forma mais simples", "i", 80), XE, 950, passo=0.15)
    relogio(c, t, C["s21.a"], 1570, 340, 170)


def b_resposta5(c, t, C, b):
    selo(c, t, C["s22"] - 0.5, 5)
    a_, b_, c_, d_ = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]
    a3, b3, c3, d3, e3, f3 = (C[f"s23.{k}"] for k in "abcdef")

    def tortas(cy, r, xs, ts):
        """3 inteiras e 2 de 6, com os cortes sumindo quando 2/6 vira 1/3"""
        for i in range(3):
            E.foco(c, t, ts + i * 0.2, 0.4, lambda p: torta(c, xs[i], cy, r, 6, 6, p))
        junta = t >= a3 + 0.4
        E.foco(c, t, ts + 0.8, 0.4, lambda p: torta(c, xs[3], cy, r, 6, 2, p, (0, 2, 4) if junta else None))

    def parte1():
        s = 140
        fr(c, t, a_, 20, 6, 340, 470, s, COR)
        E.frase(c, t, C["s22"] + 0.2, ps("cada pedaço é um sexto:", "i", 76), XE, 240, passo=0.13)
        conta(c, t, b_, "6 × 3 = 18", 620, 450, 84, TINTA)
        conta(c, t, c_, "de 18 para 20, faltam 2", 620, 570, 64, TINTA2)
        tortas(790, 120, (360, 640, 920, 1200), b_ + 0.3)
        misto(c, t, d_, 3, 2, 6, 1590, 790, 120)
    E.saida(c, t, C["s23"] - 0.1, parte1)

    if C["s23"] <= t:
        def parte2():
            E.frase(c, t, C["s23"] + 0.2, ps("dois sextos ainda simplifica", "i", 84), XE, 240, passo=0.15)
            s, cy, x0, x1 = 140, 480, 340, 940
            fr(c, t, C["s23"] + 0.3, 2, 6, x0, cy, s, COR)
            pontes(c, t, x0 + 100, x1 - 100, cy, s, "÷ 2", a3, a3, size=52)
            fr(c, t, b3, 1, 3, x1, cy, s, COR)
            E.frase(c, t, lerp(C["s23"], a3, 0.75), ps("2 e 6 são pares", "b", 58, TINTA2), x0 + 300, 670, "center", 0.12)
            tortas(820, 120, (360, 640, 920, 1200), C["s23"] + 0.2)
            misto(c, t, c3, 3, 1, 3, 1520, 470, 140, CERTO)
            E.frase(c, t, c3 + 0.4, ps("de torta", "g", 72, CERTO), 1540, 690, "center", 0.2)
        E.saida(c, t, lerp(c3, d3, 0.75), parte2)

        tb = lerp(c3, d3, 0.8)
        if t >= tb:
            E.frase(c, t, tb + 0.1, ps("outro caminho:", "i", 96) + ps("simplifique antes", "g", 90, COR), W / 2, 280, "center", 0.2)
            s, cy, x0, x1 = 150, 540, 340, 900
            fr(c, t, e3 - 0.3, 20, 6, x0, cy, s)
            pontes(c, t, x0 + 130, x1 - 110, cy, s, "÷ 2", e3, e3, size=52)
            fr(c, t, e3 + 0.4, 10, 3, x1, cy, s, COR)
            conta(c, t, lerp(e3, f3, 0.35), "10 ÷ 3 = 3", 1100, 490, 72, TINTA)
            conta(c, t, lerp(e3, f3, 0.55), "e sobra 1", 1100, 590, 72, TINTA)
            misto(c, t, f3, 3, 1, 3, 1640, 520, 110, CERTO)
            E.frase(c, t, f3, ps("com números menores,", "i", 88) + ps("a mesma resposta", "g", 80, CERTO), W / 2, 860, "center", 0.17)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s24.a", ps("leia o que", "i", 88) + ps("a pergunta pede", "g", 82, COR)),
                 (600, "s24.b", ps("veja se o número é", "i", 88) + ps("a parte ou o total", "g", 82, COR)),
                 (800, "s24.c", ps("confira se a resposta", "i", 88) + ps("faz sentido", "g", 82, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p: num_bola(c, str(i + 1), 220, y - 28, 56, 64, p))
            E.frase(c, t, C[k] + 0.1, partes, 310, y, passo=0.16)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    a_, b_, c_, d_ = C["s25.a"], C["s25.b"], C["s25.c"], C["s25.d"]
    E.frase(c, t, C["s25"] + 0.4, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, a_, ps("Somar", "g", 130, COR) + ps("e", "i", 120) + ps("subtrair", "g", 130, COR), XE, 430)
    E.frase(c, t, a_ + 0.7, ps("frações", "g", 130, COR), XE, 570)
    E.frase(c, t, b_, ps("primeiro, com", "i", 76) + ps("denominadores iguais", "g", 70, COR), XE, 700, passo=0.17)
    E.foco(c, t, c_, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 340, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c_ + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1640, p), lerp(650, 385, p), ep(t, c_ + 0.2, 0.4), TINTA)
    E.frase(c, t, d_, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 890, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
