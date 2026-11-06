"""Visual — Estudativo · MAT-DIV-008: praticando múltiplos, primos, MMC e MDC.
Aula de prática: cinco questões, cada uma com selo de progresso, relógio de pausa e resolução na tela.
A peça própria é a régua do atalho: o MDC mora até o menor número, o MMC mora do maior em diante.
Todo instante vem de C[...]: o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, barra, montar, tabela, seta_primo, passos, produto
import motor as M
import skia

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-008_praticando_mmc_mdc.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("q1", "q3", "q5", "atalho", "fim"))
BR = "#FFFFFF"

T266 = montar((266,), (2, 7, 19))
G1 = dict(xs=(340,), xb=520, xp=640, y0=320, dy=150, s=110)
# MDC: a tabela para quando nada mais divide os dois, então o fim não vira 1 (montar exige 1 no fim)
T84 = dict(primos=(2, 3, 7), linhas=[(84, 126), (42, 63), (14, 21), (2, 3)], desceu=[(False, False)] * 4)
G3 = dict(xs=(290, 510), xb=660, xp=770, y0=310, dy=135, s=100)
assert 1278 % 6 == 0 and 2 * 7 * 19 == 266 and 14 * 19 == 266 and 133 % 7 == 0 and 133 // 7 == 19 and 1 + 3 + 3 == 7
assert 2 * 3 * 7 == 42 and 84 // 42 == 2 and 126 // 42 == 3 and 8 * 12 == 96 and 96 // 4 == 24
assert 2 * 3 == 6 and 18 * 24 == 432 and 432 // 6 == 72 and 18 % 12 == 6


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


def bola_duas(c, l1, l2, cx, cy, r, s1, s2, a=1.0, cor=None):
    """esfera com o número e a unidade embaixo"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, l1, cx, cy + s1 * 0.2, s1, "g", E.SOBRE, a)
    centro(c, l2, cx, cy + s1 * 0.2 + s2 * 1.05, s2, "i", E.SOBRE, a)


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
    """questão n de 5, com cinco pontos de progresso"""
    s = f"questão {n} de 5"
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


def marca(c, cx, cy, r, ok, a=1.0):
    """esfera com certo ou errado desenhado"""
    E.bola(c, cx, cy, r, CERTO if ok else ERRADO, a)
    k = r * 0.46
    if ok:
        M.line(c, cx - k, cy + k * 0.05, cx - k * 0.2, cy + k * 0.75, BR, a, r * 0.2)
        M.line(c, cx - k * 0.2, cy + k * 0.75, cx + k, cy - k * 0.7, BR, a, r * 0.2)
    else:
        M.line(c, cx - k, cy - k, cx + k, cy + k, BR, a, r * 0.2)
        M.line(c, cx - k, cy + k, cx + k, cy - k, BR, a, r * 0.2)


def fatores(c, t, n, fs, y, t0, t1, tc=None, comuns=(), s=100, xn=440, x0=630, dx=165):
    """n = a × b × c, fator a fator entre t0 e t1; em tc os fatores comuns ganham esfera e os outros ficam cinza"""
    E.foco(c, t, t0, 0.45, lambda a: (E.escreve(c, str(n), xn - E.larg(str(n), "g", s), y, s, "g", TINTA, a),
                                      centro(c, "=", xn + s * 0.75, y, round(s * 0.8), "g", TINTA2, a)))
    marcado = tc is not None and t >= tc
    for i, f in enumerate(fs):
        ti, cx = lerp(t0, t1, (i + 1) / len(fs)), x0 + i * dx
        if i:
            E.foco(c, t, ti - 0.1, 0.35, lambda a: centro(c, "×", cx - dx / 2, y, round(s * 0.6), "b", TINTA2, a), sobe=8)
        if tc is not None and i in comuns:
            r = s * 0.56 * ease_back(prog(t, tc + i * 0.1, 0.45))
            if r > 1:
                E.bola(c, cx, y - s * 0.36, r)
        na_bola = marcado and i in comuns
        cor, sz = (E.SOBRE, round(s * 0.8)) if na_bola else (CINZA if marcado else TINTA, s)
        E.foco(c, t, ti, 0.4, lambda a: centro(c, str(f), cx, y - s * 0.36 + sz * 0.36, sz, "g", cor, a), sobe=8)


def seta_conta(c, t, ti, x0, x1, y, rot, cor=None):
    """seta com a operação numa pílula em cima"""
    if t < ti:
        return
    p = ep(t, ti, 0.5)
    M.arrow(c, x0, y, x1, y, cor or COR, p, 5, 16, p)
    E.foco(c, t, ti, 0.4, lambda a: E.pilula(c, rot, (x0 + x1) / 2, y - 76, 60, estilo="g", a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1 = C["s01.a"]

    def conta():
        E.frase(c, t, C["s01"] + 0.3, ps("em problema de", "i", 84) + ps("MMC e MDC,", "g", 78, COR), W / 2, 220, "center", 0.18)
        E.frase(c, t, C["s01"] + 1.1, ps("muita gente", "i", 84), W / 2, 330, "center", 0.18)
        E.frase(c, t, lerp(C["s01"], a1, 0.6), ps("acerta", "i", 130) + ps("a conta", "g", 120, CERTO), 720, 540, passo=0.25)
        E.foco(c, t, lerp(C["s01"], a1, 0.75), 0.45, lambda p: marca(c, 560, 500, 72, True, p))
        E.frase(c, t, a1, ps("erra", "i", 130) + ps("a escolha", "g", 120, ERRADO), 720, 720, passo=0.25)
        E.foco(c, t, a1 + 0.2, 0.45, lambda p: marca(c, 560, 680, 72, False, p))
        E.frase(c, t, lerp(a1, C["s01.end"], 0.5), ps("resolve direitinho", "i", 84) + ps("o problema errado", "g", 78, ERRADO), W / 2, 900, "center", 0.18)
    E.saida(c, t, C["s02"] - 0.1, conta)

    if t >= C["s02"]:
        a_, b_ = C["s02.a"], C["s02.b"]
        E.frase(c, t, C["s02"] + 0.3, ps("você vai treinar", "i", 88), XE, 210)
        E.frase(c, t, a_, ps("5", "g", 240, COR) + ps("questões", "g", 190, COR), XE, 460, passo=0.25)
        E.frase(c, t, lerp(a_, b_, 0.45), ps("criadas para esta aula", "i", 76), XE, 580, passo=0.17)
        for i, (s, cx) in enumerate((("pause", 440), ("resolva", 960), ("confira", 1480))):
            ti = b_ + i * 0.6
            E.foco(c, t, ti, 0.5, lambda p: (num_bola(c, str(i + 1), cx - 190, 790, 56, 64, p), E.escreve(c, s, cx - 110, 815, 92, "g", TINTA, p)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você vai", "i", 110), XE, 430)
    E.frase(c, t, C["s03"] + 0.8, ps("usar", "g", 124, COR), XE, 570)
    x, w = 860, 860
    for i, (k, s) in enumerate((("s03.a", "regras de divisibilidade"), ("s03.b", "fatoração"), ("s03.c", "MDC"), ("s03.d", "MMC"))):
        y = 180 + i * 165
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 134, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 62, COR)], x + 44, y + 90)
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.5), ps("travou?", "i", 66, COR), XE, 700, passo=0.13)
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.6), ps("procure a aula no canal", "i", 62), XE, 785, passo=0.13)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    a_, b_, c_ = C["s04.a"], C["s04.b"], C["s04.c"]
    selo(c, t, C["s04"] + 0.2, 1)
    linha(c, t, [("1.278", "g", 170, COR, a_), ("balas", "i", 130, TINTA, a_ + 0.6)], XE, 350)
    E.frase(c, t, a_ + 1.0, ps("divididas igualmente entre", "i", 72), XE, 470, passo=0.14)
    linha(c, t, [("6", "g", 170, COR, b_), ("crianças", "i", 130, TINTA, b_ + 0.3)], XE, 640)
    E.frase(c, t, c_, ps("sem fazer a divisão,", "i", 88), XE, 790, passo=0.17)
    E.frase(c, t, c_ + 0.9, ps("diga se sobra bala", "g", 84, COR), XE, 900, passo=0.17)
    relogio(c, t, C["s05.a"])


def b_r1(c, t, C, b):
    selo(c, t, C["s06"] - 0.5, 1)
    a_, b_, c_, d_ = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]

    def regra():
        E.frase(c, t, C["s06"] + 0.2, ps("para dividir por", "i", 76) + ps("6:", "g", 72, COR), XE, 240, passo=0.15)
        E.frase(c, t, a_, ps("ser par", "g", 72, COR) + ps("e", "i", 76) + ps("passar no teste do 3", "g", 68, COR), 750, 240, passo=0.15)
        s, y = 230, 600
        xs = dict(um=300, dois=560, sete=780, oito=1000)
        r1, r2 = c_ + 0.5, d_ + 0.5
        E.foco(c, t, C["s06"] + 0.3, 0.5, lambda a: (centro(c, "1", xs["um"], y, s, "g", CINZA if t >= r1 else TINTA, a),
                                                    centro(c, ".", 430, y, s, "g", CINZA, a),
                                                    centro(c, "2", xs["dois"], y, s, "g", CINZA if t >= r2 else TINTA, a),
                                                    centro(c, "7", xs["sete"], y, s, "g", CINZA if t >= r2 else TINTA, a),
                                                    centro(c, "8", xs["oito"], y, s, "g", CINZA if t >= r1 else TINTA, a)))
        # o 8 de "é par"
        q = ep(t, b_, 0.4) * (1 - ep(t, c_ - 0.3, 0.3))
        E.caixa_pontilhada(c, xs["oito"] - 105, y - 200, 210, 230, q, CERTO, prog_=q)

        def par(x0, x1, fundo, ti):
            p = ep(t, ti, 0.5)
            if p <= 0:
                return
            path = skia.Path()
            path.moveTo(x0, y + 40); path.quadTo((x0 + x1) / 2, y + 40 + fundo, x1, y + 40)
            c.drawPath(path, M.paint(COR, p, stroke=7, cap_round=True))
            centro(c, "9", (x0 + x1) / 2, y + 40 + fundo / 2 + 62, 56, "g", COR, p)
        par(xs["um"], xs["oito"], 300, c_)
        par(xs["dois"], xs["sete"], 96, d_)
        if t >= r1:
            E.risco(c, xs["um"] - 70, y - 40, xs["um"] + 70, y - 130, t, r1, COR)
            E.risco(c, xs["oito"] - 70, y - 40, xs["oito"] + 70, y - 130, t, r1, COR)
        if t >= r2:
            E.risco(c, xs["dois"] - 70, y - 40, xs["dois"] + 70, y - 130, t, r2, COR)
            E.risco(c, xs["sete"] - 70, y - 40, xs["sete"] + 70, y - 130, t, r2, COR)
        X = 1200
        E.frase(c, t, b_, ps("termina em 8:", "i", 76), X, 400, passo=0.15)
        E.frase(c, t, b_ + 0.5, ps("é par", "g", 84, CERTO), X, 495, passo=0.17)
        E.frase(c, t, lerp(b_, c_, 0.6), ps("noves fora:", "i", 76), X, 610, passo=0.17)
        E.foco(c, t, c_, 0.45, lambda a: E.escreve(c, "1 com 8: risca", X, 700, 62, "b", TINTA, a))
        E.foco(c, t, d_, 0.45, lambda a: E.escreve(c, "2 com 7: risca", X, 780, 62, "b", TINTA, a))
        E.frase(c, t, lerp(d_, C["s06.end"], 0.4), ps("não sobrou nada:", "i", 76) + ps("passa no 3", "g", 72, CERTO), X - 240, 950, passo=0.15)
    E.saida(c, t, C["s07"] - 0.1, regra)

    if t >= C["s07"]:
        a7, b7 = C["s07.a"], C["s07.b"]
        E.foco(c, t, a7, 0.5, lambda p: marca(c, 330, 420, 130, True, p))
        E.frase(c, t, a7 + 0.1, ps("não sobra", "i", 140) + ps("bala", "g", 130, CERTO), 520, 465, passo=0.3)
        E.frase(c, t, C["s07"] + 0.3, ps("passou nos testes", "i", 84), XE, 250, passo=0.17)
        E.frase(c, t, b7, ps("1.278", "g", 96, COR) + ps("é múltiplo de", "i", 96) + ps("6", "g", 96, COR), XE, 700, passo=0.25)
        E.frase(c, t, lerp(b7, C["s07.end"], 0.55), ps("6", "g", 96, COR) + ps("é divisor de", "i", 96) + ps("1.278", "g", 96, COR), XE, 840, passo=0.25)


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    a_ = C["s08.a"]
    selo(c, t, C["s08"] + 0.2, 2)
    E.frase(c, t, a_, ps("escreva", "i", 110), XE, 340)
    E.frase(c, t, a_ + 0.4, ps("266", "g", 280, COR), XE, 610)
    E.frase(c, t, a_ + 0.8, ps("como multiplicação", "i", 100), XE, 770, passo=0.2)
    E.frase(c, t, a_ + 1.4, ps("de primos", "g", 100, COR), XE, 890, passo=0.2)
    relogio(c, t, C["s09.a"])


def b_r2(c, t, C, b):
    selo(c, t, C["s10"] - 0.5, 2)
    a_, b_, c_, d_, e_ = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"], C["s10.e"]
    a7, b7, c7, d7 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    ini = C["s10"] + 0.2
    tp = [a_ + 0.3, e_ + 0.3, a7 + 0.3]
    tn = [[ini], [a_ + 0.7], [e_ + 0.9], [a7 + 0.8]]
    tabela(c, t, T266, tn, tp, [ini, a_, e_, a7], G1, cor_fim=CERTO if t >= a7 + 0.8 else None)
    X = 850

    def testes():
        E.frase(c, t, lerp(a_, b_, 0.45), ps("133", "g", 76, COR) + ps("tem cara de primo: teste", "i", 76), X, 300, passo=0.13)
        for y, ti, s, ok in ((420, b_, "por 2: não é par", False), (530, c_, "por 3: a soma dá 7", False),
                             (640, d_, "por 5: não termina em 0 ou 5", False), (750, e_, "por 7: dá 19, sem resto", True)):
            E.foco(c, t, ti, 0.45, lambda p: (marca(c, X + 38, y - 24, 36, ok, p), E.escreve(c, s, X + 100, y, 60, "b", CERTO if ok else TINTA, p)))
    E.saida(c, t, C["s11"] - 0.1, testes)

    if t >= C["s11"]:
        E.frase(c, t, C["s11"] + 0.2, ps("19", "g", 80, COR) + ps("é primo", "i", 88), X, 300, passo=0.2)
        E.frase(c, t, b7, ps("resposta:", "i", 76), X, 430, passo=0.15)
        E.foco(c, t, b7 + 0.3, 0.5, lambda p: E.escreve(c, "266 = 2 × 7 × 19", X, 540, 96, "g", CERTO, p))
        E.frase(c, t, c7 - 0.4, ps("conferindo:", "i", 76), X, 680, passo=0.15)
        E.foco(c, t, c7, 0.45, lambda p: E.escreve(c, "2 × 7 = 14", X, 790, 76, "b", TINTA, p))
        E.foco(c, t, d7, 0.45, lambda p: (E.escreve(c, "14 × 19 = 266", X, 890, 76, "b", TINTA, p), marca(c, X + 620, 864, 44, True, p)))


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    a_, b_, c_ = C["s12.a"], C["s12.b"], C["s12.c"]
    selo(c, t, C["s12"] + 0.2, 3)
    esc = 720 / 126
    for y, cm, ti in ((230, 84, a_), (340, 126, a_ + 0.9)):
        E.foco(c, t, ti, 0.45, lambda p: (barra(c, XE, y, cm * esc, 80, 1.0, (), p), E.escreve(c, f"{cm} cm", XE + cm * esc + 26, y + 62, 72, "g", TINTA, p)))
    E.frase(c, t, b_, ps("duas tábuas em", "i", 80) + ps("pedaços iguais,", "g", 74, COR), XE, 560, passo=0.15)
    E.frase(c, t, b_ + 1.0, ps("os maiores possíveis, sem sobra", "i", 80), XE, 665, passo=0.15)
    E.frase(c, t, c_, ps("quantos pedaços saem,", "i", 110), XE, 830, passo=0.17)
    E.frase(c, t, c_ + 0.9, ps("no total?", "g", 110, COR), XE, 950, passo=0.2)
    relogio(c, t, C["s13.a"])


def b_r3(c, t, C, b):
    selo(c, t, C["s14"] - 0.5, 3)
    a_, b_, c_, d_, e_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    a5, b5, c5, d5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    E.foco(c, t, a_, 0.45, lambda p: E.pilula(c, "MDC", 915, 110, 66, estilo="g", a=p))
    E.frase(c, t, lerp(C["s14"], a_, 0.3), ps("iguais, sem sobra, os maiores", "i", 56), 1055, 128, passo=0.11)
    tp = [b_ + 0.3, c_ + 0.3, d_ + 0.3]
    tn = [[C["s14"] + 0.2, C["s14"] + 0.4], [lerp(b_, c_, 0.5), lerp(b_, c_, 0.75)], [lerp(c_, d_, 0.5), lerp(c_, d_, 0.75)], [lerp(d_, e_, 0.4), lerp(d_, e_, 0.65)]]
    tabela(c, t, T84, tn, tp, [C["s14"] + 0.2, b_, c_, d_], G3, cor_fim=COR)
    ti = [b_, c_, d_]
    for i in range(3):
        seta_primo(c, t, ti[i], ti[i + 1] if i < 2 else e_, i, G3)
    passos(c, t, T84, ti, tp, tn, e_ - 0.1)
    X = 1000
    if t >= e_:
        s, y0, dy, xp = G3["s"], G3["y0"], G3["dy"], G3["xp"]
        p = ep(t, e_, 0.5)
        E.caixa_pontilhada(c, xp - 66, y0 - s * 0.95, 132, dy * 2 + s * 1.2, p, COR, prog_=p)
        produto(c, t, T84, (e_ + 0.2, e_ + 0.5, e_ + 0.8), X + 20, 320, G3, 84, 140)
        E.foco(c, t, lerp(e_, C["s14.end"], 0.7), 0.5, lambda a: (E.escreve(c, "=", X + 400, 320, 88, "g", TINTA, a), bola_duas(c, "42", "cm", X + 610, 290, 130, 116, 60, a)))
    E.foco(c, t, a5, 0.45, lambda p: E.escreve(c, "84 ÷ 42 = 2 pedaços", X, 540, 68, "b", TINTA, p))
    E.foco(c, t, b5, 0.45, lambda p: E.escreve(c, "126 ÷ 42 = 3 pedaços", X, 640, 68, "b", TINTA, p))
    E.frase(c, t, c5, ps("no total,", "i", 88), X, 790, passo=0.2)
    E.foco(c, t, c5 + 0.4, 0.5, lambda p: (num_bola(c, "5", X + 370, 760, 90, 110, p, CERTO, BR), E.escreve(c, "pedaços", X + 475, 790, 76, "g", CERTO, p)))
    q = ep(t, d5, 0.5)
    y_fim = G3["y0"] + 3 * G3["dy"]
    E.caixa_pontilhada(c, 200, y_fim - 100, 400, 124, q, CERTO, prog_=q)
    E.frase(c, t, d5, ps("o", "i", 76) + ps("2", "g", 72, CERTO) + ps("e o", "i", 76) + ps("3", "g", 72, CERTO) + ps("do fim já eram essa resposta", "i", 76), XE + 30, 950, passo=0.13)


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    a_, b_, c_, d_ = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]
    selo(c, t, C["s16"] + 0.2, 4)
    linha(c, t, [("um", "i", 96, TINTA, a_), ("remédio", "i", 96, TINTA, a_ + 0.2), ("a cada", "i", 96, TINTA, a_ + 0.5), ("8 horas", "g", 92, COR, a_ + 0.8)], XE, 340)
    linha(c, t, [("outro", "i", 96, TINTA, b_), ("a cada", "i", 96, TINTA, b_ + 0.2), ("12 horas", "g", 92, COR, b_ + 0.5)], XE, 480)
    linha(c, t, [("às", "i", 96, TINTA, c_), ("6 da manhã,", "g", 92, COR, c_ + 0.2), ("juntos", "i", 96, TINTA, c_ + 1.0)], XE, 630)
    E.frase(c, t, d_, ps("quando toma", "i", 110), XE, 810, passo=0.2)
    E.frase(c, t, d_ + 0.6, ps("juntos de novo?", "g", 104, COR), XE, 930, passo=0.2)
    relogio(c, t, C["s17.a"])


def b_r4(c, t, C, b):
    selo(c, t, C["s18"] - 0.5, 4)
    a_, b_, c_, d_ = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def conta():
        E.frase(c, t, C["s18"] + 0.2, ps("a cada, juntos, de novo:", "i", 88), XE, 280, passo=0.13)
        E.foco(c, t, a_, 0.45, lambda p: E.pilula(c, "MMC", 1160, 250, 76, estilo="g", a=p))
        E.frase(c, t, lerp(a_, b_, 0.25), ps("cabe o atalho:", "i", 76) + ps("multiplique e divida pelo MDC", "g", 62, COR), XE, 400, passo=0.13)
        E.foco(c, t, b_, 0.5, lambda p: E.escreve(c, "MDC de 8 e 12 = 4", XE, 550, 88, "g", TINTA, p))
        y = 800
        linha(c, t, [("8", "g", 130, TINTA, c_), ("×", "g", 96, TINTA2, c_ + 0.2), ("12", "g", 130, TINTA, c_ + 0.4), ("=", "g", 110, TINTA2, c_ + 0.8), ("96", "g", 130, TINTA, c_ + 1.0)], XE, y)
        seta_conta(c, t, d_, 860, 1170, y - 44, "÷ 4")
        E.foco(c, t, d_ + 0.5, 0.5, lambda p: bola_duas(c, "24", "horas", 1430, y - 50, 170, 136, 70, p, CERTO))
    E.saida(c, t, C["s19"] - 0.1, conta)

    if t >= C["s19"]:
        a9, b9 = C["s19.a"], C["s19.b"]
        E.frase(c, t, a9, ps("24 horas", "g", 104, COR) + ps("depois", "i", 110), W / 2, 280, "center", 0.25)
        X = lambda v: 310 + v * 54
        Y1, Y2 = 480, 610
        q = ep(t, a9 + 0.2, 0.5)
        for y, p_, cor, acima in ((Y1, 8, COR, True), (Y2, 12, TINTA, False)):
            M.line(c, X(0), y, X(24), y, TINTA, q, 4)
            c.drawCircle(X(0), y, 15, M.paint(TINTA, q))
            for v in range(p_, 25, p_):
                z = ease_back(prog(t, a9 + 0.4 + v * 0.03, 0.4))
                if z > 0:
                    if v < 24:
                        c.drawCircle(X(v), y, 15 * z, M.paint(cor))
                    E.foco(c, t, a9 + 0.4 + v * 0.03, 0.4, lambda p: centro(c, f"{v} h", X(v), y - 34 if acima else y + 76, 56, "g", cor, p), sobe=6)
        z = ep(t, a9 + 1.2, 0.5)
        if z > 0:
            M.line(c, X(24), Y1, X(24), lerp(Y1, Y2, z), CERTO, 1.0, 8)
            c.drawCircle(X(24), Y1, 19, M.paint(CERTO)); c.drawCircle(X(24), lerp(Y1, Y2, z), 19, M.paint(CERTO))
        E.foco(c, t, a9 + 0.2, 0.45, lambda p: E.pilula(c, "6h", X(0), 800, 76, estilo="g", fundo=TINTA, cor=BR, a=p))
        E.foco(c, t, b9, 0.5, lambda p: E.pilula(c, "6h do dia seguinte", 1200, 800, 76, estilo="g", fundo=CERTO, cor=BR, a=p))
        if t >= b9:
            p = ep(t, b9, 0.5)
            M.arrow(c, X(0) + 110, 800, 780, 800, TINTA, p, 5, 16, p)


# ---------------- questão 5 ----------------
def cartao(c, t, y, letra, tl, fim, l1, l2, l3, x=130, w=1130, h=300):
    p = ep(t, tl, 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.foco(c, t, tl, 0.45, lambda a: num_bola(c, letra, x + 74, y + 92, 48, 56, a))
    E.frase(c, t, tl + 0.1, ps(l1, "i", 68), x + 150, y + 90, passo=0.12)
    E.frase(c, t, lerp(tl, fim, 0.35), ps(l2, "i", 68), x + 150, y + 176, passo=0.12)
    E.frase(c, t, lerp(tl, fim, 0.72), ps(l3, "g", 60, COR), x + 150, y + 258, passo=0.12)


def b_q5(c, t, C, b):
    a_, b_ = C["s20.a"], C["s20.b"]
    a1, b1 = C["s21.a"], C["s21.b"]
    selo(c, t, C["s20"] + 0.2, 5)
    linha(c, t, [("mesmos", "i", 72, TINTA, a_ - 0.5), ("números:", "i", 72, TINTA, a_ - 0.3), ("18", "g", 76, COR, a_), ("e", "i", 72, TINTA, a_ + 0.3), ("24", "g", 76, COR, a_ + 0.5)], 830, 134)
    cartao(c, t, 200, "A", b_, C["s20.end"], "cordas de 18 e de 24 metros", "pedaços iguais, os maiores, sem sobra", "qual é o tamanho do pedaço?")
    cartao(c, t, 530, "B", a1, b1, "um sinal a cada 18 s, outro a cada 24 s", "tocaram juntos agora", "quando tocam juntos de novo?")
    E.frase(c, t, b1, ps("decida entre", "i", 84) + ps("MMC e MDC", "g", 78, COR) + ps("em cada caso, e resolva", "i", 84), W / 2, 950, "center", 0.15)
    relogio(c, t, C["s22.a"], 1570, 400, 170)


def b_r5(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"], C["s23.e"]
    selo(c, t, C["s23"] - 0.5, 5)
    # caso A: reparte
    E.foco(c, t, a_ - 0.3, 0.45, lambda p: num_bola(c, "A", 950, 110, 44, 52, p))
    E.frase(c, t, a_, ps("reparte:", "i", 76) + ps("é MDC", "g", 72, COR), 1020, 134, passo=0.2)
    s, xn, x0, dx = 78, 300, 450, 130
    fatores(c, t, 18, (2, 3, 3), 270, b_, lerp(b_, c_, 0.85), d_, (0, 1), s, xn, x0, dx)
    fatores(c, t, 24, (2, 2, 2, 3), 380, c_, lerp(c_, d_, 0.85), d_, (0, 3), s, xn, x0, dx)
    linha(c, t, [("em", "i", 72, TINTA, d_), ("comum:", "i", 72, TINTA, d_ + 0.15), ("2", "g", 80, COR, d_ + 0.3), ("×", "b", 58, TINTA2, d_ + 0.5), ("3", "g", 80, COR, d_ + 0.6)], 930, 300)
    E.foco(c, t, e_, 0.5, lambda p: bola_duas(c, "6", "metros", 1620, 290, 120, 110, 54, p))
    M.line(c, XE, 480, 1750, 480, FIO, ep(t, C["s24"], 0.4), 3)
    # caso B: repete
    a2, b2, c2, d2 = C["s24.a"], C["s24.b"], C["s24.c"], C["s24.d"]
    E.foco(c, t, a2 - 0.3, 0.45, lambda p: num_bola(c, "B", 214, 570, 44, 52, p))
    E.frase(c, t, a2, ps("repete:", "i", 76) + ps("é MMC", "g", 72, COR), 290, 594, passo=0.2)
    y = 800
    linha(c, t, [("18", "g", 110, TINTA, b2), ("×", "g", 86, TINTA2, b2 + 0.3), ("24", "g", 110, TINTA, b2 + 0.6), ("=", "g", 96, TINTA2, b2 + 1.1), ("432", "g", 110, TINTA, b2 + 1.5)], XE, y)
    seta_conta(c, t, c2, 930, 1230, y - 40, "÷ 6")
    E.frase(c, t, c2 + 0.5, ps("o MDC", "i", 60), 1080, y + 56, "center", 0.15)
    E.foco(c, t, d2, 0.5, lambda p: bola_duas(c, "72", "segundos", 1500, y - 50, 160, 136, 62, p))


# ---------------- atalho (palco escuro) ----------------
RX = lambda v: 190 + v * 20  # a régua: de 0 a 80


def regua(c, t, t0, y, ti_mdc, ti_mmc, y_lab=70):
    """régua de 0 a 80 com as zonas do MDC (até o menor) e do MMC (do maior em diante)"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    M.line(c, RX(0), y, RX(80), y, BR, q, 5)
    for v in range(0, 81, 6):
        M.line(c, RX(v), y, RX(v), y + (22 if v % 18 == 0 else 13), BR, q * 0.7, 3)
    for ti, v0, v1, cor in ((ti_mdc, 0, 18, CLARO), (ti_mmc, 24, 80, CLARO)):
        p = ep(t, ti, 0.6)
        if p > 0:
            c.drawRect(skia.Rect.MakeXYWH(RX(v0), y - 66, (RX(v1) - RX(v0)) * p, 62), M.paint(cor, 0.3))
            centro(c, "MDC" if v0 == 0 else "MMC", RX(12 if v0 == 0 else 50), y - 18, 44, "g", BR, ep(t, ti + 0.3, 0.4))
    for v in (18, 24):
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, str(v), RX(v), y + y_lab + 6, 60, "g", BR, a))


def pino(c, t, ti, v, y, s, ok=True):
    """o resultado cai na régua, dentro da zona certa"""
    q = ease_back(prog(t, ti, 0.5))
    if q > 0:
        M.line(c, RX(v), y - 4, RX(v), y - 100, CERTO if ok else BR, min(1.0, q), 4)
        num_bola(c, s, RX(v), y - 150, 62 * q, 66, min(1.0, q * 2), CERTO if ok else E.COR, BR)


def b_atalho(c, t, C, b):
    palco(c, t)
    a_, b_, c_, d_, e_ = C["s25.a"], C["s25.b"], C["s25.c"], C["s25.d"], C["s25.e"]

    def tela_regua():
        E.frase(c, t, C["s25"] + 0.3, ps("para fechar, um atalho que confere a escolha", "i", 72, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, a_, ps("a", "i", 130, BR) + ps("régua", "g", 130, BR), W / 2, 290, "center", 0.2)
        y = 630
        regua(c, t, a_ + 0.2, y, b_, c_)
        E.frase(c, t, b_, ps("o", "i", 70, CLARO) + ps("MDC", "g", 66, BR) + ps("nunca passa do menor", "i", 70, CLARO), XE, 810, passo=0.14)
        E.frase(c, t, c_, ps("o", "i", 70, CLARO) + ps("MMC", "g", 66, BR) + ps("nunca fica abaixo do maior", "i", 70, CLARO), XE, 900, passo=0.14)
        pino(c, t, d_, 6, y, "6")
        pino(c, t, e_, 72, y, "72")
        E.frase(c, t, lerp(e_, C["s25.end"], 0.45), ps("tudo no lugar", "g", 80, CERTO), 1240, 860, passo=0.2)
    E.saida(c, t, C["s26"] - 0.1, tela_regua)

    def porque():
        a6, b6 = C["s26.a"], C["s26.b"]
        E.frase(c, t, C["s26"] + 0.2, ps("funciona porque", "i", 92, CLARO), W / 2, 200, "center")
        E.frase(c, t, a6, ps("o", "i", 84, CLARO) + ps("MDC divide", "g", 80, BR) + ps("os números", "i", 84, CLARO), XE, 380, passo=0.18)
        E.frase(c, t, a6 + 1.0, ps("nenhum divisor passa do próprio número", "i", 76, CLARO), XE, 490, passo=0.13)
        E.frase(c, t, b6, ps("o", "i", 84, CLARO) + ps("MMC é múltiplo", "g", 80, BR) + ps("deles", "i", 84, CLARO), XE, 690, passo=0.18)
        E.frase(c, t, b6 + 1.0, ps("um múltiplo não fica abaixo do número", "i", 76, CLARO), XE, 800, passo=0.13)
    if t >= C["s26"]:
        E.saida(c, t, C["s27"] - 0.1, porque)

    if t >= C["s27"]:
        a7, b7, c7 = C["s27.a"], C["s27.b"], C["s27.c"]
        E.frase(c, t, C["s27"] + 0.3, ps("quando", "i", 96, CLARO) + ps("não compensa?", "g", 90, BR), W / 2, 170, "center", 0.2)
        E.frase(c, t, a7, ps("ela denuncia", "i", 80, CLARO) + ps("o método trocado,", "g", 74, BR) + ps("não a conta errada", "i", 80, CLARO), W / 2, 300, "center", 0.15)
        E.frase(c, t, b7, ps("errou e achou", "i", 88, CLARO) + ps("MDC = 12?", "g", 84, ERRADO), XE, 480, passo=0.17)
        E.frase(c, t, lerp(b7, c7, 0.4), ps("12 não passa de 18:", "i", 80, CLARO) + ps("a régua deixa passar", "g", 70, BR), XE, 590, passo=0.14)
        M.line(c, XE, 670, 1750, 670, CLARO, 0.25 * ep(t, c7 - 0.3, 0.4), 2)
        E.frase(c, t, c7, ps("divida os números pelo", "i", 84, CLARO) + ps("MDC:", "g", 80, BR), XE, 780, passo=0.15)
        E.frase(c, t, c7 + 1.1, ps("não pode sobrar resto", "g", 80, BR), XE, 890, passo=0.17)
        E.foco(c, t, lerp(c7, C["s27.end"], 0.6), 0.45, lambda p: E.pilula(c, "18 ÷ 12 sobra 6", 1370, 862, 58, estilo="g", fundo=ERRADO, cor=BR, a=p))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a_, b_, c_ = C["s28.a"], C["s28.b"], C["s28.c"]

    def resumo():
        E.frase(c, t, C["s28"] + 0.3, ps("resumindo", "i", 96, COR), W / 2, 190, "center")
        for i, (y, ti, l1, l2) in enumerate(((380, a_, "reparte:", "MDC"), (560, b_, "repete:", "MMC"))):
            E.foco(c, t, ti, 0.5, lambda p: num_bola(c, str(i + 1), 220, y - 28, 56, 64, p))
            E.frase(c, t, ti + 0.1, ps(l1, "i", 104) + ps(l2, "g", 100, COR), 310, y, passo=0.3)
        E.foco(c, t, c_, 0.5, lambda p: num_bola(c, "3", 220, 712, 56, 64, p))
        E.frase(c, t, c_ + 0.1, ps("fatorar", "g", 100, COR) + ps("resolve as duas contas", "i", 104), 310, 740, passo=0.2)
        E.frase(c, t, lerp(c_, C["s28.end"], 0.6), ps("você fechou o módulo", "g", 88, CERTO), W / 2, 930, "center", 0.2)
    E.saida(c, t, C["s29"] - 0.1, resumo)
    if t < C["s29"]:
        return
    a9, b9, c9 = C["s29.a"], C["s29.b"], C["s29.c"]
    E.frase(c, t, C["s29"] + 0.5, ps("o próximo passo", "i", 84), XE, 270)
    E.frase(c, t, a9, ps("Frações", "g", 170, COR), XE, 440)
    E.frase(c, t, lerp(a9, b9, 0.25), ps("o", "i", 76) + ps("MDC", "g", 72, COR) + ps("ajuda a simplificar", "i", 76), XE, 580, passo=0.17)
    E.frase(c, t, lerp(a9, b9, 0.6), ps("o", "i", 76) + ps("MMC", "g", 72, COR) + ps("ajuda a somar", "i", 76), XE, 680, passo=0.17)
    E.foco(c, t, b9, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1440, 380, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, b9 + 0.3, 0.8))
    E.cursor(c, lerp(1740, 1590, p), lerp(690, 425, p), ep(t, b9 + 0.2, 0.4), TINTA)
    E.frase(c, t, c9, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 890, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, atalho=b_atalho, fim=b_fim)
