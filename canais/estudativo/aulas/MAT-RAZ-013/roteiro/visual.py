"""Visual — Estudativo · MAT-RAZ-013: dividir em partes diretamente proporcionais.
Peças locais: pilha() empilha moedas de R$ 1.000 (3 contra 5: o peso de cada sócio se vê de longe); partes() é a barra do lucro
cortada em k pedaços iguais, pintada por grupo (índigo = o primeiro, preto = o segundo), com o valor de cada pedaço escrito dentro;
troca() faz a equação de cima evoluir no lugar. Todo instante vem de C[...] (marcadores do cenas.py)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-013_divisao_diretamente_proporcional.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tempo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula, conferidas
assert 1200 // 8 == 150 and 3 * 150 == 450 and 5 * 150 == 750 and 450 + 750 == 1200
assert 4000 * 6 == 24000 and 3000 * 10 == 30000 and 24000 // 6000 == 4 and 30000 // 6000 == 5
assert 6300 // 9 == 700 and 4 * 700 == 2800 and 5 * 700 == 3500 and 2800 + 3500 == 6300 and 3500 - 2800 == 700
assert 6300 // 7 == 900 and 4 * 900 == 3600 and 3 * 900 == 2700 and 3600 + 2700 == 6300
assert 2000 * 9 == 18000 and 3000 * 4 == 12000 and 18000 // 6000 == 3 and 12000 // 6000 == 2
assert 3000 // 5 == 600 and 3 * 600 == 1800 and 2 * 600 == 1200 and 1800 + 1200 == 3000


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


def troca(c, t, estados, cx, y, size):
    """equação que evolui no lugar: estados = [(t0, fórmula, cor)]; cada uma sai quando a próxima entra"""
    for i, (t0, s, cor) in enumerate(estados):
        if t < t0:
            break
        t1 = estados[i + 1][0] if i + 1 < len(estados) else 1e9
        E.saida(c, t, t1 - 0.15, lambda t0=t0, s=s, cor=cor: fcen(c, t, t0, s, cx, y, size, cor), d=0.3)


def moeda_deitada(c, cx, y, w, h, cor, a):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - h, w, h), h / 2, h / 2)
    c.drawRRect(r, M.paint(cor, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 7, y - h + 6, w - 14, h - 12), (h - 12) / 2, (h - 12) / 2),
                M.paint(BR, 0.35 * a, stroke=2))
    centro(c, "1.000", cx, y - h / 2 + 11, 30, "b", BR, a)


def pilha(c, t, t0, cx, base, n, cor, passo=0.12):
    """n moedas de R$ 1.000 empilhadas, caindo uma a uma a partir de t0"""
    for i in range(n):
        p = ease_back(prog(t, t0 + i * passo, 0.4))
        if p <= 0:
            continue
        y = base - i * 52 - (1 - p) * 60
        moeda_deitada(c, cx, y, 230, 44, cor, min(1.0, p * 1.5))


def partes(c, x, y, w, h, n, grupos=(), a=1.0, cortes=1.0, rotulos=(), size=56, escuro=False):
    """barra cortada em n pedaços iguais. grupos = [(i0, i1, cor, p)] pinta do pedaço i0 ao i1 (p = 0..1 enche);
    rotulos = [(i, texto, a)] escreve no meio do pedaço i"""
    if a <= 0:
        return
    rr = E._casco(c, x, y, w, h, 14, a, escuro)
    fat = w / n
    c.save(); c.clipRRect(rr, True)
    pint = set()
    for i0, i1, cor, p in grupos:
        if p > 0:
            c.drawRect(skia.Rect.MakeXYWH(x + fat * i0, y, fat * (i1 - i0) * M.clamp(p), h), M.paint(cor, a))
            if p >= 0.99:
                pint.update(range(i0, i1))
    for i in range(1, n):
        lx = x + fat * i
        M.line(c, lx, y, lx, y + h * M.clamp(cortes), BR if (i in pint or i - 1 in pint) else (CINZA if escuro else FIO), a, 4)
    c.restore()
    c.drawRRect(rr, M.paint(BR if escuro else TINTA, a, stroke=3))
    for i, s, q in rotulos:
        if q > 0:
            cor = BR if (i in pint or escuro) else TINTA
            centro(c, s, x + fat * (i + 0.5), y + h / 2 + size * 0.36, size, "g", cor, a * q)


def grupo_rot(c, t, t0, x, y, w, n, i0, i1, l1, cor, tl=None, l2=None, size=60):
    """chave embaixo dos pedaços i0..i1 e o rótulo do grupo (l2 = a conta, que entra em tl)"""
    fat = w / n
    x0, x1 = x + fat * i0 + 8, x + fat * i1 - 8
    E.chave(c, x0, x1, y, cor, ep(t, t0, 0.5), 22)
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, l1, (x0 + x1) / 2, y + 90, 54, "i", cor, a))
    if l2 is not None and tl is not None:
        fcen(c, t, tl, l2, (x0 + x1) / 2, y + 190, size, cor)


def meses(c, x, y, n, cor, a, lado=50, gap=10):
    """n quadradinhos de mês, a partir de (x, y)"""
    for i in range(n):
        M.rrect(c, x + i * (lado + gap), y, lado, lado, 9, cor, a)


def linha_peso(c, t, y, nome, conta, t0, cor, tp, tb, peso):
    """Carla: 4.000 × 6 = 24.000  —(÷ 6.000)→  (4)"""
    E.foco(c, t, t0, 0.5, lambda a: E.escreve(c, nome, 150, y, 66, "i", cor, a))
    E.formula_em(c, t, t0 + 0.2, conta, 400, y, 86, "g", TINTA)
    E.ponte(c, t, tp, 1360, 1590, y - 28, "÷ 6.000", None, 40)
    E.foco(c, t, tb, 0.5, lambda a: (E.bola(c, 1720, y - 28, 78, cor, a), centro(c, str(peso), 1720, y + 4, 92, "g", M.on(cor), a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    tm = lerp(c1, d1, 0.55)  # "Metade para cada?"

    def cena():
        E.frase(c, t, C["s01"] + 0.2, ps("dois sócios,", "i", 84) + [("um negócio", "g", 80, COR)], W / 2, 160, "center", 0.12)
        for cx, n, k, nome, val, cor in ((560, 3, a1, "sócio 1", "R$ 3.000", COR), (1360, 5, b1, "sócio 2", "R$ 5.000", TINTA)):
            pilha(c, t, k, cx, 600, n, cor)
            fcen(c, t, k + 0.3, val, cx, 720, 92, cor)
            E.foco(c, t, k + 0.4, 0.5, lambda a, cx=cx, nome=nome: centro(c, nome, cx, 790, 54, "i", TINTA2, a))
            E.foco(c, t, tm, 0.5, lambda a, cx=cx, n=n: (E.pilula(c, "R$ 600?", cx, 600 - n * 52 - 60, 50, "g", ERRADO if t > d1 else TINTA, a=a)))
            if t > d1:
                E.risco(c, cx - 140, 600 - n * 52 - 30, cx + 140, 600 - n * 52 - 90, t, d1, TINTA, 8)
        E.frase(c, t, c1, ps("lucro do mês:", "i", 76) + [("R$ 1.200", "g", 84, COR)], W / 2, 930, "center", 0.12)
        E.linha(c, t, [("metade", "i", 66, TINTA2, tm), ("para", "i", 66, TINTA2, tm + 0.1), ("cada?", "i", 66, TINTA2, tm + 0.2),
                       ("não seria justo", "g", 66, ERRADO, d1)], W / 2, 1030, "center")
    E.saida(c, t, C["s02"] - 0.1, cena)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), [("repartir", "g", 120, COR)] + ps("qualquer valor", "i", 100), XE, 470, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), ps("na", "i", 90) + [("proporção certa", "g", 96, COR)], XE, 610, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("até com", "i", 84) + [("tempos diferentes", "g", 84)], XE, 750, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a3, b3, c3, e3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.end"]
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, a3, 0.5, lambda a: E.escreve(c, "1", XE + 10, 720, 340, "g", COR, a))
    E.foco(c, t, a3 + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    p = ep(t, b3, 0.5)
    E.caixa_pontilhada(c, x, 150, w, 196, p, prog_=p)
    E.frase(c, t, b3 + 0.1, [("o truque do", "i", 64)], x + 44, 234)
    E.frase(c, t, b3 + 0.3, [("k", "g", 70, COR)], x + 44, 314)
    E.cursor(c, x + w - 30, 320, ep(t, b3, 0.4))
    E.frase(c, t, c3, ps("razão 3 para 5:", "i", 64, TINTA2), x + w / 2, 470, "center", 0.1)
    fcen(c, t, c3 + 0.4, "3k  e  5k", x + w / 2, 590, 100, COR)
    tk = lerp(c3, e3, 0.3)  # "e o cá é o tamanho de uma parte"
    E.foco(c, t, c3 + 0.6, 0.5, lambda a: partes(c, x, 650, w, 110, 8, [(0, 3, COR, 1), (3, 8, TINTA, 1)], a,
                                                  rotulos=[(i, "k", 1.0) for i in range(8)], size=52))
    E.frase(c, t, tk, [("k", "g", 64, COR)] + ps("= o tamanho de uma parte", "i", 60), x + w / 2, 860, "center", 0.1)
    E.frase(c, t, lerp(c3, e3, 0.72), ps("faltou?", "i", 54, COR) + ps("procure no canal", "i", 54, TINTA2), x + w / 2, 990, "center", 0.1)


# ---------------- a ideia ----------------
BX, BY, BW, BH = 260, 450, 1400, 170


def b_ideia(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]

    def ideia():
        E.frase(c, t, C["s04"] + 0.2, ps("dividir em partes", "i", 84), W / 2, 210, "center", 0.12)
        E.frase(c, t, a4, [("diretamente proporcionais", "g", 100, COR)], W / 2, 350, "center")
        E.frase(c, t, lerp(a4, b4, 0.3), ps("quem pôs mais", "i", 80) + [("leva mais", "g", 80, COR)], W / 2, 540, "center", 0.12)
        E.frase(c, t, lerp(a4, b4, 0.6), ps("na mesma razão", "i", 72, TINTA2), W / 2, 650, "center", 0.12)
        E.frase(c, t, b4, ps("os números da razão são os", "i", 72), W / 2 - 120, 850, "center", 0.1)
        E.foco(c, t, b4 + 0.8, 0.5, lambda a: E.pilula(c, "pesos", 1500, 828, 80, "g", a=a))
    E.saida(c, t, C["s05"] - 0.1, ideia)
    if t < C["s05"]:
        return
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    # capitais → razão 3 para 5
    E.saida(c, t, a5, lambda: (fcen(c, t, C["s05"] + 0.2, "R$ 3.000", 640, 250, 96, COR), fcen(c, t, C["s05"] + 0.5, "R$ 5.000", 1280, 250, 96)))
    E.foco(c, t, a5 + 0.1, 0.5, lambda a: (centro(c, "3", 640, 280, 150, "g", COR, a), centro(c, "para", 960, 265, 80, "i", TINTA, a),
                                            centro(c, "5", 1280, 280, 150, "g", TINTA, a)))
    E.frase(c, t, b5, ps("R$ 1.200 em", "i", 60, TINTA2) + [("8 partes iguais", "g", 60)], W / 2, 400, "center", 0.1)
    desenha_barra(c, t, C, 8, [(0, 3, COR, ep(t, c5, 0.6)), (3, 8, TINTA, ep(t, d5, 0.6))], ep(t, b5, 0.5))
    grupo_rot(c, t, c5, BX, BY + BH + 20, BW, 8, 0, 3, "3 partes: sócio 1", COR)
    grupo_rot(c, t, d5, BX, BY + BH + 20, BW, 8, 3, 8, "5 partes: sócio 2", TINTA)


def desenha_barra(c, t, C, n, grupos, a, rot=None, tr=None):
    q = ep(t, tr, 0.5) if tr is not None else 0
    partes(c, BX, BY, BW, BH, n, grupos, a, rotulos=[(i, rot, q) for i in range(n)] if rot else ())


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    troca(c, t, [(a6, "3k + 5k = 1.200", TINTA), (b6, "8k = 1.200", TINTA), (c6, "k = 1.200 ÷ 8 = 150", TINTA), (d6, "k = 150", COR)], W / 2, 300, 100)
    g = [(0, 3, COR, 1), (3, 8, TINTA, 1)]
    if t < d6:
        partes(c, BX, BY, BW, BH, 8, g, 1, rotulos=[(i, "k", ep(t, a6, 0.5)) for i in range(8)], size=64)
    else:
        partes(c, BX, BY, BW, BH, 8, g, 1, rotulos=[(i, "150", ep(t, d6 + 0.4 + i * 0.08, 0.4)) for i in range(8)], size=56)
    E.saida(c, t, a7 - 0.1, lambda: E.frase(c, t, d6 + 0.4, ps("o valor de", "i", 54, TINTA2) + [("uma parte", "g", 54, COR)], W / 2, 410, "center", 0.08))
    grupo_rot(c, t, -9, BX, BY + BH + 20, BW, 8, 0, 3, "sócio 1", COR, a7, "3 × 150 = R$ 450", 64)
    grupo_rot(c, t, -9, BX, BY + BH + 20, BW, 8, 3, 8, "sócio 2", TINTA, b7, "5 × 150 = R$ 750", 64)
    fcen(c, t, c7, "450 + 750 = 1.200", W / 2 - 50, 1010, 80, CERTO)
    E.foco(c, t, c7 + 1.0, 0.5, lambda a: E.selo(c, W / 2 + 400, 982, 44, True, a))


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    a8, b8, c8, d8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.end"]
    E.frase(c, t, a8 - 0.4, ps("o método em", "i", 76) + [("3 passos", "g", 80, COR)], XE, 170, passo=0.12)
    E.passo(c, t, b8, 1, "some", "os pesos", 330)
    E.passo(c, t, c8, 2, "divida o total pela soma:", "esse é o k", 560)
    E.passo(c, t, d8, 3, "multiplique o k", "pelo peso de cada um", 790)
    xr = 1450
    fcen(c, t, b8 + 0.4, "3 + 5 = 8", xr, 360, 76, COR)
    fcen(c, t, c8 + 0.6, "1.200 ÷ 8 = 150", xr, 590, 76, COR)
    fcen(c, t, d8 + 0.6, "3 × 150   5 × 150", xr, 820, 76, COR)
    E.frase(c, t, lerp(d8, e8, 0.65), ps("vale para", "i", 60, TINTA2) + [("quantas pessoas forem", "g", 60)], W / 2, 1000, "center", 0.1)


# ---------------- capital vezes tempo ----------------
def b_tempo(c, t, C, b):
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]

    def apresenta():
        E.frase(c, t, C["s09"] + 0.2, ps("e se ficam", "i", 80) + [("tempos diferentes?", "g", 84, COR)], W / 2, 170, "center", 0.12)
        for cx, k, nome, val, n, cor in ((520, b9, "Carla", "R$ 4.000", 6, COR), (1340, c9, "Davi", "R$ 3.000", 10, TINTA)):
            E.foco(c, t, k - 0.4, 0.5, lambda a, cx=cx, nome=nome, cor=cor: centro(c, nome, cx, 330, 76, "i", cor, a))
            fcen(c, t, k, val, cx, 460, 104, cor)
            lado, gap = 50, 10
            wq = n * (lado + gap) - gap
            q = ep(t, lerp(k, k + 2.6, 0.5), 0.5)
            for i in range(n):
                M.rrect(c, cx - wq / 2 + i * (lado + gap), 530, lado, lado, 9, cor, ep(t, lerp(k, k + 2.6, 0.5) + i * 0.05, 0.3))
            E.foco(c, t, lerp(k, k + 2.6, 0.5), 0.5, lambda a, cx=cx, n=n: centro(c, f"{n} meses", cx, 660, 62, "i", TINTA, a))
        E.frase(c, t, d9, ps("lucro:", "i", 76) + [("R$ 6.300", "g", 84, COR)], W / 2, 870, "center", 0.12)
    E.saida(c, t, C["s10"] - 0.1, apresenta)

    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    if C["s10"] <= t:
        def porque():
            E.frase(c, t, a0, ps("o peso é", "i", 84) + [("capital × tempo", "g", 96, COR)], W / 2, 210, "center", 0.12)
            x0, w, h, gap = 170, 165, 120, 14
            tq = lerp(a0, b0, 0.45)  # "Quatro mil reais trabalhando por seis meses"
            for i in range(6):
                E.foco(c, t, tq + i * 0.1, 0.4, lambda a, i=i: (M.rrect(c, x0 + i * (w + gap), 420, w, h, 14, COR, a),
                                                              centro(c, "4.000", x0 + i * (w + gap) + w / 2, 497, 46, "g", BR, a)))
            E.foco(c, t, tq + 0.7, 0.5, lambda a: centro(c, "6 meses de R$ 4.000", x0 + (6 * (w + gap) - gap) / 2, 610, 54, "i", TINTA, a))
            xe = x0 + 6 * (w + gap) + 30
            E.foco(c, t, b0 - 0.2, 0.4, lambda a: centro(c, "=", xe + 30, 505, 100, "g", TINTA, a))
            E.foco(c, t, b0, 0.5, lambda a: (M.rrect(c, xe + 90, 400, 360, 160, 18, TINTA, a), centro(c, "24.000", xe + 270, 505, 84, "g", BR, a)))
            E.foco(c, t, b0 + 0.3, 0.5, lambda a: centro(c, "1 mês só", xe + 270, 640, 54, "i", TINTA, a))
            E.frase(c, t, c0 - 0.6, ps("dinheiro e tempo", "i", 80) + [("se multiplicam", "g", 84, COR)], W / 2, 860, "center", 0.12)
        E.saida(c, t, C["s11"] - 0.1, porque)

    a1, b1, c1, e1 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.end"]
    if C["s11"] <= t:
        def pesos():
            E.frase(c, t, C["s11"] + 0.1, [("capital × tempo", "g", 64, COR)], W / 2, 160, "center")
            tp = lerp(b1, c1, 0.92)
            linha_peso(c, t, 340, "Carla", "4.000 × 6 = 24.000", a1, COR, tp, c1, 4)
            linha_peso(c, t, 530, "Davi", "3.000 × 10 = 30.000", b1, TINTA, tp, c1 + 0.2, 5)
            E.frase(c, t, lerp(b1, c1, 0.3), ps("números grandes:", "i", 58, TINTA2) + ps("divida pelo mesmo número", "i", 58), W / 2, 700, "center", 0.08)
            E.frase(c, t, lerp(b1, c1, 0.72), ps("o maior que serve:", "i", 64) + [("MDC = 6.000", "g", 68, COR)], W / 2, 810, "center", 0.1)
            E.frase(c, t, lerp(c1, e1, 0.3), ps("mesmo ÷ em todos os pesos:", "i", 58, TINTA2) + [("a divisão não muda", "g", 58)], W / 2, 960, "center", 0.08)
        E.saida(c, t, C["s12"] - 0.1, pesos)

    if t < C["s12"]:
        return
    a2, b2, c2, d2, e2 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    a3, b3 = C["s13.a"], C["s13.b"]
    troca(c, t, [(a2, "4k + 5k = 6.300", TINTA), (b2, "9k = 6.300", TINTA), (c2, "k = 6.300 ÷ 9 = 700", COR), (a3, "2.800 + 3.500 = 6.300", CERTO)], W / 2, 300, 96)
    E.foco(c, t, a3 + 1.4, 0.5, lambda a: E.selo(c, 1650, 268, 44, True, a))
    g = [(0, 4, COR, ep(t, a2 + 0.3, 0.5)), (4, 9, TINTA, ep(t, a2 + 0.8, 0.5))]
    rot = [(i, "k", ep(t, a2 + 0.5, 0.4) * (1 - ep(t, c2, 0.3))) for i in range(9)] + [(i, "700", ep(t, c2 + 0.5 + i * 0.06, 0.4)) for i in range(9)]
    E.foco(c, t, C["s12"], 0.5, lambda a: partes(c, BX, BY, BW, BH, 9, g, a, rotulos=rot, size=54))
    grupo_rot(c, t, a2 + 0.3, BX, BY + BH + 20, BW, 9, 0, 4, "Carla", COR, d2, "4 × 700 = R$ 2.800", 60)
    grupo_rot(c, t, a2 + 0.8, BX, BY + BH + 20, BW, 9, 4, 9, "Davi", TINTA, e2, "5 × 700 = R$ 3.500", 60)
    if t >= b3:
        p = ep(t, b3, 0.5)
        E.caixa_pontilhada(c, BX + BW * 4 / 9 - 12, BY - 16, BW * 5 / 9 + 24, BH + 32, p, prog_=p)
    E.frase(c, t, b3 + 0.2, [("o Davi leva mais:", "g", 60)] + ps("ficou mais tempo", "i", 64, COR), W / 2, 1020, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4, d4, e4 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.end"]

    def errado():
        E.frase(c, t, C["s14"] + 0.2, ps("o erro:", "i", 80) + [("olhar só o capital", "g", 84, ERRADO)], W / 2, 170, "center", 0.12)
        fcen(c, t, b4, "pesos 4 e 3: 7 partes", W / 2, 285, 70, TINTA2)
        troca(c, t, [(c4, "6.300 ÷ 7 = 900", ERRADO)], W / 2, 390, 72)
        g = [(0, 4, COR, 1), (4, 7, TINTA, 1)]
        rot = [(i, "900", ep(t, c4 + 0.6 + i * 0.06, 0.4)) for i in range(7)]
        E.foco(c, t, b4 + 0.3, 0.5, lambda a: partes(c, BX, BY, BW, BH, 7, g, a, rotulos=rot, size=60))
        grupo_rot(c, t, b4 + 0.5, BX, BY + BH + 20, BW, 7, 0, 4, "Carla", COR, d4, "R$ 3.600", 72)
        grupo_rot(c, t, b4 + 0.7, BX, BY + BH + 20, BW, 7, 4, 7, "Davi", TINTA, lerp(d4, e4, 0.45), "R$ 2.700", 72)
    E.saida(c, t, C["s15"] - 0.1, errado)
    if t < C["s15"]:
        return
    a5, b5 = C["s15.a"], C["s15.b"]
    fcen(c, t, C["s15"] + 0.2, "3.600 + 2.700 = 6.300", W / 2, 260, 86, TINTA2)
    E.frase(c, t, C["s15"] + 0.6, ps("a soma fecha...", "i", 60, TINTA2), W / 2, 360, "center", 0.1)
    E.frase(c, t, a5, ps("mas", "i", 90) + [("o tempo sumiu", "g", 96, ERRADO)], W / 2, 540, "center", 0.12)
    E.foco(c, t, a5 + 0.8, 0.5, lambda a: E.selo(c, 1620, 510, 54, False, a))
    E.frase(c, t, b5 - 1.2, ps("o enunciado fala em tempo?", "i", 72), W / 2, 760, "center", 0.1)
    E.foco(c, t, b5, 0.5, lambda a: E.pilula(c, "capital × tempo, antes de tudo", W / 2, 900, 70, "g", a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a6, b6 = C["s16.a"], C["s16.b"]

    def ideia():
        E.frase(c, t, C["s16"] + 0.2, ps("agora, o atalho", "i", 76, CLARO), W / 2, 200, "center", 0.12)
        E.frase(c, t, a6, ps("quanto um recebeu", "i", 92, CLARO) + [("a mais?", "g", 96, BR)], W / 2, 400, "center", 0.12)
        E.frase(c, t, lerp(a6, b6, 0.55), ps("sem calcular as duas partes", "i", 66, CLARO), W / 2, 530, "center", 0.1)
        E.frase(c, t, b6, [("diferença dos pesos", "g", 96, BR)], W / 2, 740, "center")
        E.frase(c, t, b6 + 0.6, ps("vezes", "i", 90, CLARO) + [("k", "g", 110, BR)], W / 2, 880, "center", 0.12)
    E.saida(c, t, C["s17"] - 0.1, ideia)

    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    x0, w, h = 500, 200, 120
    if C["s17"] <= t:
        def barras():
            for y, n, nome, cor, dt in ((200, 5, "Davi", BR, 0), (360, 4, "Carla", CLARO, 0.3)):
                E.foco(c, t, C["s17"] + dt, 0.5, lambda a, y=y, n=n, nome=nome, cor=cor: (
                    E.escreve(c, nome, x0 - 40 - E.larg(nome, "i", 64), y + h / 2 + 22, 64, "i", cor, a),
                    partes(c, x0, y, w * n, h, n, [(0, n, E.COR, 1)], a, rotulos=[(i, "k", 1) for i in range(n)], size=56, escuro=True)))
            if t >= a7:
                p = ep(t, a7, 0.5)
                E.caixa_pontilhada(c, x0 + 4 * w - 10, 190, w + 20, h + 20, p, BR, prog_=p)
            fcen(c, t, a7, "5 − 4 = 1", 1610, 445, 84, BR)
            E.foco(c, t, a7 + 0.3, 0.5, lambda a: centro(c, "diferença de 1 peso", 1610, 520, 50, "i", CLARO, a))
            fcen(c, t, b7, "1 × 700 = 700", W / 2, 720, 110, BR)
            E.frase(c, t, b7 + 1.0, ps("o Davi recebe", "i", 64, CLARO) + [("R$ 700 a mais", "g", 68, BR)], W / 2, 830, "center", 0.1)
            fcen(c, t, c7, "3.500 − 2.800 = 700", W / 2 - 40, 990, 76, CLARO)
            E.foco(c, t, c7 + 1.4, 0.5, lambda a: E.selo(c, W / 2 + 470, 962, 40, True, a))
        E.saida(c, t, C["s18"] - 0.1, barras)

    if t < C["s18"]:
        return
    a8, b8 = C["s18.a"], C["s18.b"]
    E.frase(c, t, a8, ps("cada parte =", "i", 76, CLARO) + [("peso × k", "g", 84, BR)], W / 2, 220, "center", 0.12)
    fcen(c, t, lerp(a8, b8, 0.4), "5k − 4k = 1k", W / 2, 400, 110, BR)
    E.frase(c, t, lerp(a8, b8, 0.6), ps("o mesmo k", "i", 64, CLARO), W / 2, 500, "center", 0.1)
    E.foco(c, t, b8, 0.5, lambda a: E.selo(c, 330, 700, 50, False, a))
    E.frase(c, t, b8 + 0.1, ps("pediu", "i", 76, CLARO) + [("todas as partes?", "g", 80, BR)], 420, 725, "left", 0.1)
    E.frase(c, t, lerp(b8, C["s18.end"], 0.6), ps("aí, calcule", "i", 76, CLARO) + [("cada uma", "g", 80, BR)], 420, 870, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a9, b9, c9, d9 = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    E.frase(c, t, C["s19"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a9 - 0.3, ps("Ana:", "i", 80) + [("R$ 2.000", "g", 84, COR)] + ps("por 9 meses", "i", 80), XE, 360, passo=0.12)
    E.frase(c, t, b9 - 0.3, ps("Bia:", "i", 80) + [("R$ 3.000", "g", 84)] + ps("por 4 meses", "i", 80), XE, 500, passo=0.12)
    E.frase(c, t, c9 - 0.3, ps("lucro:", "i", 80) + [("R$ 3.000", "g", 84, COR)], XE, 640, passo=0.12)
    E.frase(c, t, d9, ps("quanto cada uma", "i", 96) + [("recebe?", "g", 100, COR)], XE, 850, passo=0.12)
    E.relogio(c, t, C["s20.a"], 1590, 430, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]

    def pesos():
        E.frase(c, t, C["s21"] + 0.3, ps("peso =", "i", 64) + [("capital × tempo", "g", 64, COR)], W / 2, 170, "center", 0.1)
        tp = lerp(b1, c1, 0.6)
        linha_peso(c, t, 380, "Ana", "2.000 × 9 = 18.000", a1, COR, tp, c1, 3)
        linha_peso(c, t, 590, "Bia", "3.000 × 4 = 12.000", b1, TINTA, tp, c1 + 0.2, 2)
        E.frase(c, t, c1 + 0.6, ps("os pesos ficam", "i", 70) + [("3 e 2", "g", 76, COR)], W / 2, 850, "center", 0.1)
    E.saida(c, t, C["s22"] - 0.1, pesos)
    if t < C["s22"]:
        return
    a2, b2, c2, d2, e2 = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"], C["s22.e"]
    tk = lerp(b2, c2, 0.55)  # "e o cá é seiscentos"
    troca(c, t, [(a2, "3k + 2k = 3.000", TINTA), (b2, "5k = 3.000", TINTA), (tk, "k = 3.000 ÷ 5 = 600", COR), (e2, "1.800 + 1.200 = 3.000", CERTO)], W / 2, 300, 96)
    E.foco(c, t, e2 + 1.2, 0.5, lambda a: E.selo(c, 1650, 268, 44, True, a))
    g = [(0, 3, COR, ep(t, a2 + 0.3, 0.5)), (3, 5, TINTA, ep(t, a2 + 0.8, 0.5))]
    rot = [(i, "k", ep(t, a2 + 0.5, 0.4) * (1 - ep(t, tk, 0.3))) for i in range(5)] + [(i, "600", ep(t, tk + 0.5 + i * 0.08, 0.4)) for i in range(5)]
    E.foco(c, t, C["s22"], 0.5, lambda a: partes(c, BX, BY, BW, BH, 5, g, a, rotulos=rot, size=64))
    grupo_rot(c, t, a2 + 0.3, BX, BY + BH + 20, BW, 5, 0, 3, "Ana", COR, c2, "3 × 600 = R$ 1.800", 64)
    grupo_rot(c, t, a2 + 0.8, BX, BY + BH + 20, BW, 5, 3, 5, "Bia", TINTA, d2, "2 × 600 = R$ 1.200", 64)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s23.a", "some", "os pesos"), ("s23.b", "ache", "o valor de uma parte (k)"), ("s23.c", "multiplique", "pelo peso de cada um"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 360 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 72) + [(l2, "g", 72, COR if i == 1 else TINTA)], 320, y, "left", 0.1)
        E.frase(c, t, C["s23.d"] - 0.6, ps("com tempo na história:", "i", 64, TINTA2) + [("peso = capital × tempo", "g", 68, COR)], W / 2, 930, "center", 0.1)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a4, b4, c4 = C["s24.a"], C["s24.b"], C["s24.c"]
    E.frase(c, t, C["s24"] + 0.2, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, lerp(C["s24"], a4, 0.5), [("repartir ao contrário", "g", 110, COR)], XE, 400, passo=0.12)
    E.frase(c, t, a4, ps("quem falta menos", "i", 84) + [("leva mais", "g", 88, COR)], XE, 540, passo=0.12)
    E.foco(c, t, b4, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, b4 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, b4 + 0.2, 0.4))
    E.frase(c, t, c4, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, conta=b_conta, metodo=b_metodo, tempo=b_tempo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
