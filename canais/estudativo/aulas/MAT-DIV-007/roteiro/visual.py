"""Visual — Estudativo · MAT-DIV-007: problemas de MMC.
A peça central é a linha do tempo dos dois ônibus: cada um marca seus múltiplos, e o encontro é onde as duas trilhas batem.
Depois da conta, os mesmos 12 e 18 viram cordas, para mostrar que quem decide é a história.
Todo instante vem de C[...]: o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha, barra, montar, tabela, seta_primo, passos, produto
import motor as M
import skia

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-007_problemas_de_mmc.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tempo", "diferenca", "atalho", "questao", "fim"))
BR = "#FFFFFF"

T12 = montar((12, 18), (2, 2, 3, 3))  # 36
T15 = montar((15, 20), (2, 2, 3, 5))  # 60
G2 = dict(xs=(330, 590), xb=740, xp=850, y0=250, dy=125, s=96)  # tabela de dois números
assert 2 * 2 * 3 * 3 == 36 and 12 * 18 // 6 == 36 and 180 // 36 == 5 and 2 * 2 * 3 * 5 == 60


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
    for dx in (-40, 40):
        M.rrect(c, cx + dx - 20, cy - 72, 40, 144, 11, E.SOBRE, ep(t, t0 + 0.2, 0.4))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + r0 + 104, 60, "i", TINTA, a))


def onibus(c, x, y, w, cor=None, a=1.0, janela=None):
    """ônibus de perfil; (x, y) = canto de baixo à esquerda"""
    if a <= 0:
        return
    cor = cor or E.COR
    h = w * 0.42
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - h, w, h * 0.82), w * 0.06, w * 0.06), M.paint(cor, a))
    n, jw, jh = 4, w * 0.17, h * 0.3
    for i in range(n):
        M.rrect(c, x + w * 0.05 + i * w * 0.23, y - h * 0.88, jw, jh, w * 0.02, janela or E.SOBRE, a * 0.92)
    for dx in (0.22, 0.78):
        c.drawCircle(x + w * dx, y - h * 0.14, w * 0.075, M.paint(TINTA, a))
        c.drawCircle(x + w * dx, y - h * 0.14, w * 0.03, M.paint("#FFFFFF", a))


def trilha(c, t, X, y, passo_min, ate, tv, cor, a=1.0, size=60, acima=True, encontro=()):
    """uma trilha da linha do tempo: tv(v) = instante em que a saída de v aparece"""
    M.line(c, X(0), y, X(ate), y, TINTA, a, 4)
    v = passo_min
    while v <= ate:
        ti = tv(v)
        q = ease_back(prog(t, ti, 0.4))
        if q > 0:
            cx = X(v)
            if v not in encontro:
                c.drawCircle(cx, y, 15 * q, M.paint(cor, a))
            E.foco(c, t, ti, 0.35, lambda p: centro(c, str(v), cx, y - 34 if acima else y + 76, size, "g", cor, p * a), sobe=6)
        v += passo_min


def encontros(c, t, X, y1, y2, v, ti, r=52):
    """o traço que junta as duas trilhas no encontro"""
    q = ep(t, ti, 0.5)
    if q <= 0:
        return
    cx = X(v)
    M.line(c, cx, y1, cx, lerp(y1, y2, q), CERTO, 1.0, 8)
    c.drawCircle(cx, y1, 19, M.paint(CERTO))
    c.drawCircle(cx, lerp(y1, y2, q), 19, M.paint(CERTO))


def rotulo_trilha(c, t, ti, txt, y):
    E.foco(c, t, ti, 0.45, lambda a: E.escreve(c, txt, XE, y, 56, "b", TINTA2, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def terminal():
        E.frase(c, t, C["s01"] + 0.3, ps("dois ônibus", "g", 84, COR) + ps("saem juntos do terminal", "i", 90), XE, 200, passo=0.16)
        y1, y2 = 460, 720
        for y, ti, n in ((y1, a_, "12"), (y2, b_, "18")):
            E.foco(c, t, C["s01"] + 0.5, 0.5, lambda p: onibus(c, XE, y, 380, a=p))
            linha(c, t, [("a", "i", 104, TINTA, ti), ("cada", "i", 104, TINTA, ti + 0.15), (n, "g", 150, COR, ti + 0.4), ("minutos", "i", 104, TINTA, ti + 0.7)], 640, y - 20)
        E.frase(c, t, c_, ps("quando saem", "i", 124) + ps("juntos de novo?", "g", 116, COR), W / 2, 930, "center", 0.25)
    E.saida(c, t, C["s02"] - 0.1, terminal)

    if t >= C["s02"]:
        s0 = C["s02"]
        q = ease_back(prog(t, C["s02.b"] - 0.2, 0.7))
        if q > 0:
            E.bola(c, 1480, 540, 290 * q)
        E.frase(c, t, s0 + 0.35, ps("até o fim da aula", "i", 90), XE, 340)
        E.frase(c, t, s0 + 1.5, ps("você", "i", 124) + ps("responde", "g", 124), XE, 500)
        E.frase(c, t, C["s02.a"], ps("e para de", "i", 100), XE, 660, passo=0.2)
        E.frase(c, t, C["s02.a"] + 0.6, ps("confundir", "g", 100, COR), XE, 780, passo=0.2)
        E.frase(c, t, C["s02.a"] + 1.1, ps("MMC e MDC", "g", 100, COR), XE, 900, passo=0.2)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 500, 84, "g", E.SOBRE, a),
                                                      centro(c, "de prova", 1480, 585, 84, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.35, ps("para acompanhar,"), XE, 310)
    E.frase(c, t, C["s03"] + 1.4, ps("lembre de"), XE, 420)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 730, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 710, 120, "i", TINTA, a))
    x, w = 880, 860
    itens = (("s03.b", "Calcular", "o MMC"), ("s03.c", "Reconhecer", "um problema de MDC"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 240 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(410, 660, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.5), ps("procure a aula no canal", "i", 62), x, 860, passo=0.14)


# ---------------- linha do tempo ----------------
def b_tempo(c, t, C, b):
    Y1, Y2 = 370, 590
    a4, b4 = C["s04.a"], C["s04.b"]
    t72 = C["s07"] + 0.1  # a régua encolhe para caber até 108
    esc = lerp(25, 13.2, ease_io(prog(t, t72, 0.9)))
    X = lambda v: 210 + v * esc
    ate = lerp(60, 112, ease_io(prog(t, t72, 0.9)))

    def tv1(v):
        return lerp(a4 + 0.5, b4 - 0.2, v / 48) if v <= 48 else t72 + 0.7 + (v - 60) * 0.02

    def tv2(v):
        return lerp(b4 + 0.4, C["s05"] - 0.2, v / 54) if v <= 54 else t72 + 0.7 + (v - 72) * 0.02

    fica(c, t, C["s04"] + 0.3, C["s05"] - 0.1, ps("monte a", "i", 92) + ps("linha do tempo", "g", 86, COR), W / 2, 180, "center")
    rotulo_trilha(c, t, a4 - 0.2, "1º ônibus", 270)
    rotulo_trilha(c, t, b4 - 0.2, "2º ônibus", 490)
    q = ep(t, C["s04"] + 0.5, 0.5)
    enc = tuple(v for v, k in ((36, "s05.b"), (72, "s07.a"), (108, "s07.b")) if t >= C[k])
    trilha(c, t, X, Y1, 12, ate, tv1, COR, q, 56)
    trilha(c, t, X, Y2, 18, ate, tv2, TINTA, q, 56, acima=False)
    # o 0: saíram juntos
    E.foco(c, t, C["s04"] + 0.5, 0.45, lambda a: (c.drawCircle(X(0), Y1, 15, M.paint(TINTA, a)), c.drawCircle(X(0), Y2, 15, M.paint(TINTA, a))))
    encontros(c, t, X, Y1, Y2, 36, C["s05.b"])
    encontros(c, t, X, Y1, Y2, 72, C["s07.a"])
    encontros(c, t, X, Y1, Y2, 108, C["s07.b"])

    # s05: o que a linha quer dizer
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]

    def s5():
        fica(c, t, a5, b5 - 0.1, ps("cada um só sai nos", "i", 92) + ps("múltiplos do seu intervalo", "g", 76, COR), W / 2, 820, "center", 0.15)
        E.foco(c, t, b5, 0.5, lambda a: centro(c, "nas duas listas: múltiplo comum", W / 2, 790, 84, "g", TINTA, a))
        E.frase(c, t, c5, ps("a primeira vez:", "i", 96) + ps("o menor deles", "g", 88, COR), W / 2, 905, "center", 0.2)
        E.foco(c, t, d5, 0.45, lambda a: E.pilula(c, "mínimo múltiplo comum", W / 2, 180, 76, estilo="g", a=a))
    E.saida(c, t, C["s06"] - 0.1, s5)

    # s06: 36 minutos no relógio
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]

    def s6():
        E.frase(c, t, a6, ps("a primeira coincidência:", "i", 88) + ps("36 minutos", "g", 84, COR), W / 2, 180, "center", 0.2)
        E.foco(c, t, b6, 0.45, lambda a: E.pilula(c, "7h00", X(0) + 60, 800, 84, estilo="g", fundo=TINTA, cor=BR, a=a))
        if t >= c6 - 0.3:
            p = ep(t, c6 - 0.3, 0.5)
            M.arrow(c, X(0) + 240, 800, X(36) - 190, 800, TINTA, p, 5, 16, p)
        E.foco(c, t, c6, 0.45, lambda a: E.pilula(c, "7h36", X(36), 800, 84, estilo="g", fundo=CERTO, cor=BR, a=a))
    if t >= C["s06"]:
        E.saida(c, t, C["s07"] - 0.1, s6)

    # s07: o MMC é o intervalo
    if t >= C["s07"]:
        c7 = C["s07.c"]
        E.frase(c, t, C["s07"] + 0.3, ps("e não para por aí", "i", 92), W / 2, 180, "center")
        for v, k in ((36, "s07.c"), (72, "s07.c"), (108, "s07.c")):
            E.foco(c, t, C[k] + (v - 36) * 0.012, 0.45, lambda a: E.chave(c, X(v - 36), X(v), Y2 + 110, COR, a, 26, 5, abre=False))
            E.foco(c, t, C[k] + 0.2 + (v - 36) * 0.012, 0.45, lambda a: centro(c, "36", (X(v - 36) + X(v)) / 2, Y2 + 200, 60, "g", COR, a))
        E.frase(c, t, c7, ps("o MMC é", "i", 100) + ps("o intervalo", "g", 92, COR) + ps("entre um encontro e outro", "i", 100), W / 2, 930, "center", 0.17)


# ---------------- conta ----------------
def tempos_t12(C):
    a_, b_, c_, d_, e_, f_ = (C[f"s08.{k}"] for k in "abcdef")
    tp = [b_ + 0.3, c_ + 0.3, d_ + 0.3, e_ + 0.3]
    tn = [[a_, a_ + 0.5], [lerp(b_, c_, 0.5), lerp(b_, c_, 0.75)], [lerp(c_, d_, 0.5), lerp(c_, d_, 0.75)],
          [lerp(d_, e_, 0.5), lerp(d_, e_, 0.75)], [lerp(e_, f_, 0.5), lerp(e_, f_, 0.75)]]
    tb = [a_, b_, c_, d_, e_]
    ti = [b_, c_, d_, e_]
    return tp, tn, tb, ti


def b_conta(c, t, C, b):
    f_ = C["s08.f"]

    def conta():
        E.frase(c, t, C["s08"] + 0.2, ps("sem lista:", "i", 76) + ps("fatoração simultânea", "g", 70, COR), XE, 130, passo=0.2)
        tp, tn, tb, ti = tempos_t12(C)
        tabela(c, t, T12, tn, tp, tb, G2, cor_fim=CERTO if t >= tn[-1][1] else None)
        for i in range(4):
            seta_primo(c, t, ti[i], ti[i + 1] if i < 3 else f_, i, G2)
        passos(c, t, T12, ti, tp, tn, f_ - 0.1)
        if t >= f_:
            s, y0, dy, xp = G2["s"], G2["y0"], G2["dy"], G2["xp"]
            p = ep(t, f_, 0.5)
            E.caixa_pontilhada(c, xp - 70, y0 - s * 0.95, 140, dy * 3 + s * 1.2, p, COR, prog_=p)
            produto(c, t, T12, (f_ + 0.3, f_ + 0.7, f_ + 1.1, f_ + 1.5), 1120, 520, G2, 84, 150)
            E.foco(c, t, C["s09"] - 0.7, 0.5, lambda a: (E.escreve(c, "=", 1110, 780, 96, "g", TINTA, a), num_bola(c, "36", 1340, 745, 130, 120, a, CERTO, BR)))
    E.saida(c, t, C["s09"] - 0.1, conta)

    if t < C["s09"]:
        return
    a_, b_, c_ = C["s09.a"], C["s09.b"], C["s09.c"]
    E.frase(c, t, C["s09"] + 0.3, ps("com dois números,", "i", 96) + ps("o atalho", "g", 88, COR), W / 2, 330, "center", 0.2)
    E.frase(c, t, C["s09"] + 1.6, ps("da aula de MMC", "i", 80), W / 2, 440, "center", 0.17)
    y = 680
    linha(c, t, [("12", "g", 120, TINTA, a_), ("×", "g", 92, TINTA2, a_ + 0.3), ("18", "g", 120, TINTA, a_ + 0.5), ("=", "g", 100, TINTA2, a_ + 1.0), ("216", "g", 120, TINTA, a_ + 1.2)], XE, y)
    if t >= b_:
        p = ep(t, b_, 0.5)
        M.arrow(c, 1020, y - 40, 1270, y - 40, COR, p, 5, 16, p)
        E.foco(c, t, b_, 0.4, lambda a: E.pilula(c, "÷ 6", 1130, y - 115, 60, estilo="g", a=a))
        E.frase(c, t, b_ + 0.3, ps("o MDC", "i", 64), 1130, y + 60, "center", 0.15)
    E.foco(c, t, c_, 0.5, lambda a: num_bola(c, "36", 1480, y - 45, 150, 136, a, CERTO, BR))


# ---------------- diferença ----------------
ESC = 1300 / 18  # cordas em escala


def corda(c, y, m, h, a, corte=0.0):
    w = m * ESC
    cortes = [(i * 6 / m, ease_io(M.clamp(corte * (m // 6) - (i - 1)))) for i in range(1, m // 6)]
    barra(c, XE, y, w, h, 1.0, cortes, a, largura=6)


def b_diferenca(c, t, C, b):
    Y1, Y2, h = 300, 490, 120
    a0, b0 = C["s10.a"], C["s10.b"]
    a1, b1 = C["s11.a"], C["s11.b"]

    def cordas():
        fica(c, t, C["s10"] + 0.3, a1 - 0.1, ps("os mesmos números,", "i", 92) + ps("outra história", "g", 84, COR), W / 2, 180, "center", 0.18)
        corda(c, Y1, 12, h, ep(t, a0, 0.5), ep(t, b1 + 0.2, 0.7))
        corda(c, Y2, 18, h, ep(t, a0 + 0.5, 0.5), ep(t, b1 + 0.2, 0.7))
        E.foco(c, t, a0 + 0.2, 0.45, lambda p: E.escreve(c, "12 m", XE + 12 * ESC + 36, Y1 + h / 2 + 26, 76, "g", TINTA, p))
        E.foco(c, t, a0 + 0.7, 0.45, lambda p: E.escreve(c, "18 m", XE + 1300 + 30, Y2 + h / 2 + 26, 76, "g", TINTA, p))
        E.frase(c, t, b0, ps("pedaços iguais,", "g", 72, COR) + ps("os maiores possíveis,", "i", 80) + ps("sem sobra", "g", 72, COR), W / 2, 725, "center", 0.2)
        E.frase(c, t, a1, ps("o pedaço precisa caber:", "i", 88) + ps("divisor comum, o maior", "g", 80, COR), W / 2, 180, "center", 0.17)
        E.foco(c, t, b1, 0.5, lambda p: E.escreve(c, "MDC de 12 e 18 =", XE, 915, 92, "g", TINTA, p))
        E.foco(c, t, b1 + 0.5, 0.5, lambda p: bola_duas(c, "6", "metros", 1180, 885, 112, 104, 50, p))
    E.saida(c, t, C["s12"] - 0.1, cordas)

    if C["s12"] <= t < C["s13"]:
        def lados():
            E.frase(c, t, C["s12"] + 0.3, ps("mesmos números,", "i", 88) + ps("respostas diferentes", "g", 80, COR), W / 2, 180, "center", 0.18)
            M.line(c, W / 2, 260, W / 2, 780, FIO, ep(t, C["s12.a"] - 0.2, 0.4), 3)
            for cx, ti, n, l1, l2 in ((500, C["s12.a"], "36", "minutos", "nos ônibus"), (1420, C["s12.b"], "6", "metros", "nas cordas")):
                E.foco(c, t, ti, 0.5, lambda p: bola_duas(c, n, l1, cx, 490, 190, 170, 66, p))
                E.frase(c, t, ti + 0.3, ps(l2, "g", 76, COR), cx, 770, "center", 0.2)
            E.frase(c, t, lerp(C["s12.b"], C["s12.end"], 0.4), ps("quem decide é", "i", 100) + ps("a história,", "g", 92, COR) + ps("não a conta", "i", 100), W / 2, 930, "center", 0.2)
        E.saida(c, t, C["s13"] - 0.1, lados)

    if t >= C["s13"]:
        a_, b_ = C["s13.a"], C["s13.b"]
        M.line(c, W / 2, 200, W / 2, 900, FIO, ep(t, a_, 0.4), 3)
        # MDC reparte: uma barra que se divide
        E.frase(c, t, a_, ps("MDC", "g", 130, COR) + ps("reparte", "i", 130), 510, 300, "center", 0.3)
        cortes = [(i / 5, ep(t, a_ + 0.6 + i * 0.15, 0.4)) for i in range(1, 5)]
        E.foco(c, t, a_ + 0.3, 0.45, lambda p: barra(c, 170, 440, 680, 150, 1.0, cortes, p, largura=7))
        E.frase(c, t, a_ + 1.1, ps("uma coisa é dividida", "i", 76), 510, 720, "center", 0.17)
        E.frase(c, t, a_ + 1.8, ps("em partes iguais", "g", 70, COR), 510, 815, "center", 0.17)
        # MMC repete: ciclos que voltam a bater
        E.frase(c, t, b_, ps("MMC", "g", 130, COR) + ps("repete", "i", 130), 1430, 300, "center", 0.3)
        for i in (0, 6, 12):
            x = 1080 + i * 58
            q = ep(t, b_ + 1.7 + i * 0.05, 0.4)
            if q > 0:
                M.line(c, x, 450, x, 590, CERTO, q, 9)
        for y, n, cor in ((450, 2, COR), (590, 3, TINTA)):
            for i in range(0, 13, n):
                x = 1080 + i * 58
                q = ease_back(prog(t, b_ + 0.5 + i * 0.09, 0.3))
                if q > 0:
                    c.drawCircle(x, y, 25 * q, M.paint(CERTO if i % 6 == 0 else cor))
        E.frase(c, t, b_ + 1.1, ps("coisas acontecem em ciclos", "i", 70), 1430, 720, "center", 0.17)
        E.frase(c, t, b_ + 1.8, ps("e voltam a coincidir", "g", 66, COR), 1430, 815, "center", 0.17)


# ---------------- treino de decisão ----------------
def b_decidir(c, t, C, b):
    a_, b_, c_, d_ = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, C["s14"] + 0.3, ps("treine o olho,", "i", 92) + ps("sem calcular nada", "g", 84, COR), W / 2, 170, "center", 0.18)

    def caso(y, l1, l2, tl, tl2, pista, met, tr):
        p = ep(t, tl, 0.5)
        E.caixa_pontilhada(c, 130, y, 1660, 290, p, prog_=p)
        E.frase(c, t, tl + 0.1, ps(l1, "i", 72), 180, y + 110, passo=0.13)
        E.frase(c, t, tl2, ps(l2, "i", 72), 180, y + 215, passo=0.13)
        E.foco(c, t, tr, 0.45, lambda a: E.escreve(c, pista, 1240, y + 175, 84, "i", TINTA, a))
        E.foco(c, t, tr + 0.3, 0.5, lambda a: num_bola(c, met, 1615, y + 145, 112, 66, a))
    caso(240, "40 lápis e 60 canetas em estojos iguais,", "o maior número possível, sem sobra", a_, lerp(a_, b_, 0.6), "reparte", "MDC", b_)
    caso(590, "um a cada 3 dias, outro a cada 4,", "se encontraram hoje: quando de novo?", c_, lerp(c_, d_, 0.5), "repete", "MMC", d_)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a_, b_, c_ = C["s15.a"], C["s15.b"], C["s15.c"]
    E.frase(c, t, C["s15"] + 0.3, ps("o", "i", 84) + ps("erro", "g", 78, ERRADO) + ps("mais comum:", "i", 84), W / 2, 170, "center", 0.17)
    E.frase(c, t, a_, ps("usar o", "i", 84) + ps("MDC", "g", 78, ERRADO) + ps("no problema dos ônibus", "i", 84), W / 2, 280, "center", 0.17)
    X = lambda v: 260 + v * 72
    Y1, Y2 = 490, 660
    p = ep(t, a_ + 0.4, 0.5)
    trilha(c, t, X, Y1, 12, 20, lambda v: a_ + 0.6, COR, p, 72)
    trilha(c, t, X, Y2, 18, 20, lambda v: a_ + 0.9, TINTA, p, 72, acima=False)
    E.foco(c, t, a_ + 0.4, 0.45, lambda q: (E.escreve(c, "1º", XE - 30, Y1 + 18, 56, "b", TINTA2, q), E.escreve(c, "2º", XE - 30, Y2 + 18, 56, "b", TINTA2, q),
                                            c.drawCircle(X(0), Y1, 15, M.paint(TINTA, q)), c.drawCircle(X(0), Y2, 15, M.paint(TINTA, q))))
    # o 6: ninguém sai aqui
    if t >= b_:
        q = ep(t, b_, 0.45)
        M.line(c, X(6), Y1 - 40, X(6), Y2 + 40, ERRADO, q, 6, dash=[14, 11], cap_round=False)
        E.foco(c, t, b_, 0.45, lambda a: E.pilula(c, "6 minutos?", X(6), 780, 66, estilo="g", fundo=ERRADO, cor=BR, a=a))
    E.frase(c, t, c_, ps("aos 6 minutos,", "i", 84) + ps("nenhum ônibus", "g", 78, ERRADO) + ps("voltou a sair", "i", 84), W / 2, 905, "center", 0.17)
    E.frase(c, t, lerp(c_, C["s15.end"], 0.45), ps("o encontro não vem antes da próxima saída", "i", 68), W / 2, 1000, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def pista():
        s0 = C["s16"]
        E.frase(c, t, s0 + 0.35, ps("agora, o atalho", "i", 90, CLARO), W / 2, 200, "center")
        E.frase(c, t, s0 + 1.3, ps("uma", "i", 104, BR) + ps("pista", "g", 104, BR) + ps("no texto", "i", 104, BR), W / 2, 330, "center", 0.2)
        rot = (("a cada", "s16.a"), ("ao mesmo tempo", "s16.b"), ("juntos de novo", "s16.c"))
        size, gap = 68, 44
        ws = [E.larg(s, "g", size) + size * 1.1 for s, _ in rot]
        x = W / 2 - (sum(ws) + 2 * gap) / 2
        for (s, k), w_ in zip(rot, ws):
            E.foco(c, t, C[k], 0.45, lambda a: E.pilula(c, s, x + w_ / 2, 560, size, estilo="g", fundo=E.COR, cor=BR, a=a))
            x += w_ + gap
        E.frase(c, t, C["s16.d"], ps("apareceu isso,", "i", 110, CLARO) + ps("é MMC", "g", 140, BR), W / 2, 830, "center", 0.25)
    E.saida(c, t, C["s17"] - 0.1, pista)

    def nome():
        s0 = C["s17"]
        E.frase(c, t, s0 + 0.35, ps("cada pista é", "i", 90, CLARO) + ps("um pedaço do nome", "g", 84, BR), W / 2, 200, "center", 0.17)
        for y, k, l1, l2 in ((390, "s17.a", "a cada", "múltiplo"), (590, "s17.b", "junto", "comum"), (790, "s17.c", "a primeira vez de novo", "mínimo")):
            E.foco(c, t, C[k], 0.45, lambda a: E.escreve(c, l1, 830 - E.larg(l1, "i", 84), y, 84, "i", CLARO, a))
            if t >= C[k] + 0.3:
                p = ep(t, C[k] + 0.3, 0.45)
                M.arrow(c, 860, y - 30, 1040, y - 30, CLARO, p, 5, 16, p)
            E.foco(c, t, C[k] + 0.5, 0.45, lambda a: E.pilula(c, l2, 1340, y - 28, 84, estilo="g", fundo=E.COR, cor=BR, a=a))
    if t >= C["s17"]:
        E.saida(c, t, C["s19"] - 0.1, nome)

    if t >= C["s19"]:
        s0 = C["s19"]
        a_, b_, c_, d_ = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
        E.frase(c, t, s0 + 0.3, ps("quando", "i", 96, CLARO) + ps("não compensa?", "g", 90, BR), W / 2, 170, "center", 0.2)
        E.frase(c, t, a_, ps("a pergunta", "i", 80, CLARO) + ps("vai além", "g", 74, BR) + ps("do próximo encontro", "i", 80, CLARO), XE, 310, passo=0.17)
        E.frase(c, t, lerp(a_, b_, 0.3), ps("quantos encontros em", "i", 80, CLARO) + ps("3 horas?", "g", 74, BR), XE, 415, passo=0.17)
        linha(c, t, [("180 min ÷ 36", "g", 92, BR, b_), ("=", "g", 92, CLARO, c_ - 0.2)], XE, 545)
        E.foco(c, t, c_, 0.5, lambda a: E.pilula(c, "5 encontros", 1110, 515, 76, estilo="g", fundo=E.COR, cor=BR, a=a))
        E.frase(c, t, c_ + 0.7, ps("sem contar a saída do começo", "i", 66, CLARO), XE, 640, passo=0.13)
        M.line(c, XE, 700, 1750, 700, CLARO, 0.25 * ep(t, d_ - 0.3, 0.4), 2)
        E.frase(c, t, d_, ps("“a cada”,", "g", 80, BR) + ps("sozinho, não basta", "i", 88, CLARO), XE, 810, passo=0.18)
        E.frase(c, t, lerp(d_, C["s19.end"], 0.45), ps("um ônibus só: sem encontro,", "i", 80, CLARO) + ps("sem MMC", "g", 74, BR), XE, 925, passo=0.15)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a_, b_, c_, d_ = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    E.frase(c, t, C["s20"] + 0.3, ps("hora de testar", "i", 76, COR), XE, 190)
    linha(c, t, [("uma", "i", 88, TINTA, a_), ("máquina:", "i", 88, TINTA, a_ + 0.2), ("a cada", "i", 88, TINTA, a_ + 0.9), ("15 dias", "g", 84, COR, a_ + 1.3)], XE, 330)
    linha(c, t, [("outra:", "i", 88, TINTA, b_), ("a cada", "i", 88, TINTA, b_ + 0.2), ("20 dias", "g", 84, COR, b_ + 0.5)], XE, 450)
    E.frase(c, t, lerp(b_, c_, 0.5), ps("hoje, pararam juntas", "i", 80), XE, 570, passo=0.17)
    E.frase(c, t, c_, ps("é", "i", 120) + ps("MMC", "g", 116, COR) + ps("ou", "i", 120) + ps("MDC?", "g", 116, COR), XE, 750, passo=0.2)
    E.frase(c, t, d_, ps("daqui a quantos dias", "i", 88), XE, 880, passo=0.17)
    E.frase(c, t, d_ + 0.8, ps("param juntas de novo?", "g", 78, COR), XE, 980, passo=0.17)
    relogio(c, t, C["s21.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a_, b_, c_, d_, e_ = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"], C["s22.e"]
    fim = C["s22.end"]
    E.frase(c, t, C["s22"] + 0.3, ps("a cada, juntas, de novo:", "i", 72), XE, 120, passo=0.13)
    E.foco(c, t, a_, 0.45, lambda p: E.pilula(c, "MMC", 1120, 98, 66, estilo="g", a=p))
    tp = [b_ + 0.3, c_ + 0.3, d_ + 0.3, e_ + 0.3]
    tn = [[a_ + 0.1, a_ + 0.4], [lerp(b_, c_, 0.5), lerp(b_, c_, 0.75)], [lerp(c_, d_, 0.5), lerp(c_, d_, 0.75)],
          [lerp(d_, e_, 0.5), lerp(d_, e_, 0.75)], [lerp(e_, fim, 0.5), lerp(e_, fim, 0.75)]]
    tb, ti = [a_, b_, c_, d_, e_], [b_, c_, d_, e_]
    tabela(c, t, T15, tn, tp, tb, G2, cor_fim=CERTO if t >= tn[-1][1] else None)
    for i in range(4):
        seta_primo(c, t, ti[i], ti[i + 1] if i < 3 else C["s23"], i, G2)
    passos(c, t, T15, ti, tp, tn, C["s23"] - 0.1)

    if t >= C["s23"]:
        X = 1130
        p = ep(t, C["s23"] + 0.5, 0.5)
        s, y0, dy, xp = G2["s"], G2["y0"], G2["dy"], G2["xp"]
        E.caixa_pontilhada(c, xp - 70, y0 - s * 0.95, 140, dy * 3 + s * 1.2, p, COR, prog_=p)
        E.frase(c, t, C["s23"] + 0.2, ps("multiplique", "g", 76, COR) + ps("a coluna", "i", 84), X - 40, 290, passo=0.25)
        v = C["s23.a"]
        produto(c, t, T15, (v, v + 0.4, v + 0.8, v + 1.2), X, 520, G2, 84, 150)
        E.foco(c, t, C["s23.b"], 0.5, lambda a: (E.escreve(c, "=", X - 20, 800, 96, "g", TINTA, a), bola_duas(c, "60", "dias", X + 250, 760, 150, 130, 66, a, CERTO)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.35, ps("resumindo", "i", 96, COR), W / 2, 210, "center")
        a_, b_ = C["s24.a"], C["s24.b"]
        for i, (y, l1, l2, ti) in enumerate(((440, "reparte em partes iguais:", "MDC", a_), (680, "repete e volta a coincidir:", "MMC", b_))):
            E.foco(c, t, ti, 0.5, lambda a: num_bola(c, str(i + 1), 220, y - 28, 56, 64, a))
            E.frase(c, t, ti + 0.1, ps(l1, "i", 96), 310, y, passo=0.16)
            E.foco(c, t, ti + 1.0, 0.5, lambda a: E.pilula(c, l2, 1560, y - 30, 84, estilo="g", a=a))
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    s0 = C["s25"]
    E.frase(c, t, s0 + 0.5, ps("na próxima aula,", "i", 84) + ps("é a sua vez", "g", 76, COR), XE, 280, passo=0.17)
    E.frase(c, t, C["s25.a"], ps("5", "g", 170, COR) + ps("questões", "g", 150, COR), XE, 480)
    E.frase(c, t, C["s25.a"] + 0.9, ps("múltiplos, primos,", "i", 92), XE, 610, passo=0.2)
    E.frase(c, t, C["s25.a"] + 1.5, ps("MMC e MDC", "g", 92, COR), XE, 720, passo=0.2)
    E.foco(c, t, C["s25.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 400, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s25.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1740, 1590, p), lerp(700, 445, p), ep(t, C["s25.b"] + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s25.c"], ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 910, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tempo=b_tempo, conta=b_conta, diferenca=b_diferenca, decidir=b_decidir,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
