"""Visual — Estudativo · MAT-POT-001: o que é potência.
Identidade em _ferramentas/editorial.py. Peças desta aula: folha que dobra e pilha de camadas, piso de lajotas que cresce,
caixinhas em perspectiva, escada dos quadrados e o piso de 35 cortado e colado. Expoente sempre com E.formula."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, sinal, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-001_o_que_e_potencia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("papel", "quadrados", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 2 ** 5 == 32 and 3 ** 4 == 81 and 3 ** 2 == 9 and 2 ** 3 == 8 and 5 ** 4 == 625 and 35 ** 2 == 1225 and 45 ** 2 == 2025
assert 30 * 40 + 25 == 1225 and 30 * 42 + 36 == 36 ** 2 and 13 + 14 == 14 ** 2 - 13 ** 2
assert 2 * 2 == 2 ** 2 and 3 * 2 == 6
ESCADA = [(n, n ** 2, 2 * n - 1) for n in range(1, 16)]  # lado, quadrado, pulo que chegou nele
assert all(ESCADA[i][1] + ESCADA[i + 1][2] == ESCADA[i + 1][1] for i in range(14))


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


def fm(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, cor=cor, align=align)


def fl(c, t, partes, x, y, size, align="left", gap=None):
    """linha de fórmulas em que cada parte entra no seu instante: partes = [(escrita, cor, t0), ...]; devolve o x e a largura de cada uma"""
    gap = size * 0.2 if gap is None else gap
    ws = [E.formula(None, p[0], 0, 0, size, a=0) for p in partes]
    tot = sum(ws) + gap * (len(ws) - 1)
    xx = x - tot / 2 if align == "center" else x
    xs = []
    for p, w in zip(partes, ws):
        fm(c, t, p[2], p[0], xx, y, size, p[1])
        xs.append(xx)
        xx += w + gap
    return xs, ws


def cadeia(c, t, ti, tf, n, b, x, y, size, cor=None, align="left"):
    """b × b × b ... com cada termo entrando na fala, de ti a tf"""
    partes = []
    for i in range(n):
        q = lerp(ti, tf, i / n)
        if i:
            partes.append(("×", cor, q - 0.05))
        partes.append((str(b), cor, q))
    return fl(c, t, partes, x, y, size, align)


def folha(c, cx, cy, w0, h0, k, p, a=1.0):
    """folha de papel vista de cima: k dobras feitas e a dobra seguinte em p (0..1). Dobras alternam o eixo"""
    w, h = w0 / 2 ** math.ceil(k / 2), h0 / 2 ** (k // 2)
    e = ease_io(p)
    giro = math.cos(math.pi * e)
    tinta = M.paint(TINTA, a, stroke=3)
    verso = M.mix(E.VAZIO, CLARO, 0.5)
    frente = M.mix(E.VAZIO, CLARO, min(0.42, k * 0.1))
    if k % 2 == 0:
        x0, y0 = cx - w / 2 + w / 4 * e, cy - h / 2
        r0 = skia.Rect.MakeXYWH(x0, y0, w / 2, h)
        hx = x0 + w / 2
        xa, xb = sorted((hx, hx + w / 2 * giro))
        r1 = skia.Rect.MakeLTRB(xa, y0, xb, y0 + h)
    else:
        x0, y0 = cx - w / 2, cy - h / 2 + h / 4 * e
        r0 = skia.Rect.MakeXYWH(x0, y0, w, h / 2)
        hy = y0 + h / 2
        ya, yb = sorted((hy, hy + h / 2 * giro))
        r1 = skia.Rect.MakeLTRB(x0, ya, x0 + w, yb)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.16 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRect(r0.makeOffset(5, 12), s)
    c.drawRect(r0, M.paint(frente, a)); c.drawRect(r0, tinta)
    c.drawRect(r1, M.paint(verso if giro < 0 else frente, a)); c.drawRect(r1, tinta)


def camadas(c, t, cx, base, w, h, gap, tempos):
    """pilha de camadas vista de lado; tempos = instante de cada camada"""
    for i, ti in enumerate(tempos):
        q = ep(t, ti, 0.35)
        if q > 0:
            M.rrect(c, cx - w / 2, base - i * (h + gap) - h - (1 - q) * 30, w, h, 5, E.COR, q)


def piso(c, t, x, y, cel, n, ti, dt=0.02, cor=None, a=1.0):
    """piso n por n, lajota a lajota, a partir do canto de cima"""
    for i in range(n * n):
        q = ease_back(prog(t, ti + i * dt, 0.3))
        if q > 0:
            E.tablete(c, x + (i % n) * cel, y + (i // n) * cel, cel, cel, cor or E.COR, a * min(1.0, q * 2), lerp(0.55, 1.0, q))


def lajotas(c, t, cels, x, y, cel, ti, dt, cor):
    """lajotas soltas nas casas (coluna, linha) da grade"""
    for i, (cx, cy) in enumerate(cels):
        q = ease_back(prog(t, ti + i * dt, 0.35))
        if q > 0:
            E.tablete(c, x + cx * cel, y + cy * cel, cel, cel, cor, min(1.0, q * 2), lerp(0.55, 1.0, q))


def caixinhas(c, t, cx, cy, s, n, tempos):
    """cubo n × n × n em perspectiva, caixinha por caixinha; (cx, cy) = canto da frente, embaixo"""
    ux, uy, uz = (s * 0.866, s * 0.5), (-s * 0.866, s * 0.5), (0, -s)

    def pt(i, j, k, dz=0.0):
        return skia.Point(cx + (i - n) * ux[0] + (j - n) * uy[0], cy + (i - n) * ux[1] + (j - n) * uy[1] + k * uz[1] - dz)

    def face(pts, cor, a, dz):
        p = skia.Path()
        p.moveTo(pt(*pts[0], dz))
        for q in pts[1:]:
            p.lineTo(pt(*q, dz))
        p.close()
        c.drawPath(p, M.paint(cor, a))
        c.drawPath(p, M.paint(BR, a, stroke=3))

    ordem = sorted(((i, j, k) for k in range(n) for j in range(n) for i in range(n)), key=lambda b: (b[2], b[0] + b[1]))
    for num, (i, j, k) in enumerate(ordem):
        q = ease_io(prog(t, tempos[num], 0.4))
        if q <= 0:
            continue
        dz = (1 - q) * s * 1.2
        a = min(1.0, q * 2)
        face(((i, j, k + 1), (i + 1, j, k + 1), (i + 1, j + 1, k + 1), (i, j + 1, k + 1)), M.mix(E.COR, BR, 0.3), a, dz)
        face(((i, j + 1, k), (i + 1, j + 1, k), (i + 1, j + 1, k + 1), (i, j + 1, k + 1)), E.COR, a, dz)
        face(((i + 1, j, k), (i + 1, j + 1, k), (i + 1, j + 1, k + 1), (i + 1, j, k + 1)), M.mix(E.COR, "#000000", 0.32), a, dz)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_ = C["s01.a"], C["s01.b"], C["s01.c"]

    def conta():
        y = 620
        fm(c, t, a_, "2^5", 230, y, 330)
        sinal(c, t, b_ - 0.15, "=", 800, y - 110, 200)
        E.foco(c, t, b_, 0.5, lambda a: centro(c, "10", 1120, y, 300, "g", ERRADO, a))
        if t >= c_ - 0.2:
            E.risco(c, 930, y + 40, 1310, y - 250, t, c_ - 0.2, largura=20)
        E.foco(c, t, c_, 0.5, lambda a: num_bola(c, "32", 1560, y - 110, 190, 180, a, CERTO, BR))
        E.frase(c, t, lerp(b_, c_, 0.3), ps("o", "i", 84) + ps("erro", "g", 76, ERRADO) + ps("mais comum", "i", 84), W / 2, 880, "center")
    E.saida(c, t, C["s02"] - 0.1, conta)

    if t >= C["s02"]:
        a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
        E.frase(c, t, a2, ps("até o fim desta aula", "i", 92), XE, 270)
        E.frase(c, t, lerp(a2, b2, 0.5), ps("qualquer", "i", 110) + ps("potência", "g", 110, COR), XE, 440)
        E.frase(c, t, b2, ps("quadrados", "g", 110, COR) + ps("de 1 a 15", "i", 110), XE, 610)
        E.frase(c, t, lerp(b2, c2, 0.55), ps("sem decorar lista", "i", 92), XE, 730)
        E.foco(c, t, c2 - 0.1, 0.6, lambda a: E.bola(c, 1490, 800, 220 * ease_back(prog(t, c2 - 0.1, 0.6))), blur=0)
        E.foco(c, t, c2 + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1490, 790, 80, "g", E.SOBRE, a), centro(c, "de prova", 1490, 870, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    a_, b_, c_ = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.1, ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, a_, 0.5, lambda p: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, p))
    E.foco(c, t, a_ + 0.15, 0.5, lambda p: E.escreve(c, "coisas", XE + 225, 700, 120, "i", TINTA, p))
    x, w = 880, 860
    for i, (k, l1, l2) in enumerate(((b_, "a", "tabuada"), (c_, "multiplicar por", "dois algarismos"))):
        y = 240 + i * 290
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 72)], x + 44, y + 96)
        E.frase(c, t, k + 0.3, [(l2, "g", 72, COR)], x + 44, y + 186)
    E.cursor(c, x + w - 50, lerp(430, 720, ease_io(prog(t, c_ - 0.35, 0.5))), ep(t, b_, 0.4))
    E.frase(c, t, lerp(c_, C["s03.end"], 0.6), ps("faltou alguma?", "i", 66, COR) + ps("procure no canal", "i", 66), W / 2, 960, "center", 0.15)


# ---------------- dobrar o papel ----------------
def b_papel(c, t, C, b):
    a_, b_, c_, d_ = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    e_ = C["s04.end"]

    def dobras():
        ds = [ease_io(prog(t, x, y - x)) for x, y in ((lerp(a_, b_, 0.55), b_), (lerp(b_, c_, 0.5), c_), (lerp(c_, d_, 0.45), d_))]
        k = 0
        while k < 3 and ds[k] >= 1:
            k += 1
        E.foco(c, t, a_, 0.5, lambda q: folha(c, 480, 500, 760, 640, k, ds[k] if k < 3 else 0, q))
        camadas(c, t, 1270, 640, 460, 36, 10, [b_ - 0.1] * 2 + [c_ - 0.1] * 2 + [d_ - 0.1] * 4)
        ys, s = 860, 130
        xs = (960, 1270, 1580)
        for x, n, k_ in zip(xs, (2, 4, 8), (b_, c_, d_)):
            E.foco(c, t, k_, 0.45, lambda q, x=x, n=n: centro(c, str(n), x, ys, s, "g", COR, q))
        E.frase(c, t, b_ + 0.1, ps("camadas", "i", 72), 1270, 970, "center")
        q = lerp(d_, e_, 0.35)
        for x0, x1 in ((xs[0] + 90, xs[1] - 90), (xs[1] + 90, xs[2] - 70)):
            E.ponte(c, t, q, x0, x1, ys - 45, "× 2", size=44)
    E.saida(c, t, C["s05"] - 0.1, dobras)

    if t >= C["s05"]:
        a5, b5, c5, d5, e5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.end"]
        E.frase(c, t, a5, ps("depois de", "i", 88) + ps("5 dobras", "g", 84, COR), XE, 230)
        xs, ws = cadeia(c, t, b5, c5 - 0.1, 5, 2, XE, 420, 120)
        xf = xs[-1] + ws[-1] + 40
        fm(c, t, c5 - 0.1, "=", xf, 420, 120)
        E.foco(c, t, c5, 0.5, lambda q: num_bola(c, "32", xf + 240, 375, 130, 130, q, None, E.SOBRE))
        E.frase(c, t, c5 + 0.2, ps("camadas", "i", 84), xf + 400, 400)
        tg = lerp(d5, e5, 0.3)
        E.frase(c, t, d5, ps("a forma curta", "i", 96, COR), XE, 700)
        E.foco(c, t, d5 + 0.3, 0.5, lambda q: E.formula(c, "2", 800, 840, 330, a=q))
        wb = E.formula(None, "2", 0, 0, 330, a=0)
        E.foco(c, t, tg, 0.5, lambda q: E.formula(c, "^5", 800 + wb, 840, 330, cor=COR, a=q))
        E.frase(c, t, lerp(d5, e5, 0.72), ps("dois elevado a cinco", "i", 80), 1180, 760, passo=0.15)


# ---------------- nomes ----------------
def b_nomes(c, t, C, b):
    a_, b_, c_, d_ = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]

    def s06():
        E.frase(c, t, a_, ps("potência", "g", 130, COR), XE, 230)
        y, s, x = 660, 340, 330
        wb = E.formula(None, "2", 0, 0, s, a=0)
        E.foco(c, t, a_, 0.5, lambda q: E.formula(c, "2", x, y, s, cor=COR if t >= b_ else TINTA, a=q))
        E.foco(c, t, a_, 0.5, lambda q: E.formula(c, "^5", x + wb, y, s, cor=COR if t >= c_ else TINTA, a=q))
        pb, pc = ep(t, b_, 0.45), ep(t, c_, 0.45)
        if pb > 0:
            M.line(c, x + wb / 2, y + 30, x + wb / 2, 790, COR, 1.0, 5, progress=pb)
        E.foco(c, t, b_, 0.45, lambda q: E.pilula(c, "base", x + wb / 2, 850, 72, estilo="g", fundo=E.COR, cor=E.SOBRE, a=q))
        xe = x + wb + 100
        if pc > 0:
            M.line(c, xe + 40, 420, 870, 420, COR, 1.0, 5, progress=pc)
        E.foco(c, t, c_, 0.45, lambda q: E.pilula(c, "expoente", 1060, 420, 72, estilo="g", fundo=E.COR, cor=E.SOBRE, a=q))
        E.frase(c, t, lerp(b_, c_, 0.45), ps("é ele que se repete", "i", 66), XE, 980, passo=0.14)
        E.frase(c, t, d_, ps("quantas vezes", "g", 76, COR) + ps("a base aparece", "i", 84), 840, 620, passo=0.16)
        xs, ws = cadeia(c, t, d_ + 0.5, d_ + 1.7, 5, 2, 840, 790, 108)
        q = ep(t, d_ + 1.8, 0.45)
        E.chave(c, xs[0], xs[-1] + ws[-1], 815, COR, q, 22, 5, abre=False)
        E.foco(c, t, d_ + 1.9, 0.45, lambda p: centro(c, "5 vezes", (xs[0] + xs[-1] + ws[-1]) / 2, 920, 66, "g", COR, p))
    E.saida(c, t, C["s07"] - 0.1, s06)

    if C["s07"] <= t < C["s08"] + 0.4:
        a7, b7, c7, d7, e7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"]

        def s07():
            E.frase(c, t, C["s07"] + 0.1, ps("mais uma", "i", 76, COR), XE, 150)
            fm(c, t, a7, "3^4", XE, 340, 170)
            fm(c, t, b7 - 0.1, "=", 500, 330, 120)
            cadeia(c, t, b7, c7 - 0.4, 4, 3, 610, 330, 120)
            fm(c, t, c7, "3 × 3 = 9", 610, 530, 110)
            fm(c, t, d7, "9 × 3 = 27", 610, 690, 110)
            fm(c, t, e7, "27 × 3 =", 610, 850, 110)
            E.foco(c, t, e7 + 0.2, 0.5, lambda q: num_bola(c, "81", 1190, 815, 110, 110, q, CERTO, BR))
            E.frase(c, t, b7 + 0.3, ps("o 3 aparece", "i", 66), XE, 520, passo=0.14)
            E.frase(c, t, b7 + 0.7, ps("4 vezes", "g", 66, COR), XE, 610)
        E.saida(c, t, C["s08"] - 0.1, s07)

    if t >= C["s08"]:
        a8, b8, c8, d8, e8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"], C["s08.e"]
        xa, xb = 500, 1400
        E.frase(c, t, C["s08"] + 0.1, ps("expoentes com nome próprio", "i", 64, COR), W / 2, 110, "center", 0.13)
        E.foco(c, t, a8 - 0.5, 0.45, lambda q: centro(c, "elevado a 2", xa, 215, 64, "i", TINTA, q))
        E.frase(c, t, a8, ps("ao quadrado", "g", 84, COR), xa, 305, "center")
        E.foco(c, t, b8 - 0.5, 0.45, lambda q: centro(c, "elevado a 3", xb, 215, 64, "i", TINTA, q))
        E.frase(c, t, b8, ps("ao cubo", "g", 84, COR), xb, 305, "center")
        cel = 120
        piso(c, t, xa - cel * 1.5, 370, cel, 3, c8, 0.12)
        fm(c, t, lerp(c8, d8, 0.55), "3^2 = 9", xa, 960, 110, align="center")
        tempos = [lerp(d8, e8, 0.1 + 0.8 * i / 8) for i in range(8)]
        caixinhas(c, t, xb, 850, 106, 2, tempos)
        fm(c, t, e8 - 0.1, "2^3 = 8", xb - 240, 985, 100)
        E.frase(c, t, e8, ps("caixinhas", "i", 76), xb + 110, 975)


# ---------------- quadrados ----------------
def degraus(c, t, itens, tempos, x0, pw, chao=960, y0=800, dy=100):
    """escada: itens = (lado, quadrado, pulo); tempos = instante de cada degrau (None = o degrau de onde se parte, já está lá)"""
    for i, ((lado, qd, pulo), ti) in enumerate(zip(itens, tempos)):
        yi, xi = y0 - i * dy, x0 + i * pw
        t0 = ti if ti is not None else -1.0

        def degrau(a, yi=yi, xi=xi, qd=qd, lado=lado, ti=ti):
            M.rrect(c, xi + 4, yi, pw - 8, chao - yi, 10, E.COR if ti is not None else CINZA, a)
            centro(c, str(qd), xi + pw / 2, yi + 76, 78, "g", BR, a)
            E.formula(c, f"{lado}^2", xi + pw / 2, yi + 136, 48, cor=BR, a=a, align="center")
        E.foco(c, t, t0, 0.45, degrau, sobe=26)
        if ti is not None and pulo > 1:
            E.foco(c, t, t0, 0.45, lambda a, yi=yi, xi=xi, pulo=pulo: E.pilula(c, f"+{pulo}", xi + pw / 2, yi - 56, 50, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))


def b_quadrados(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]

    def s09():
        E.frase(c, t, a9, ps("os quadrados", "g", 130, COR), XE, 300)
        E.frase(c, t, a9 + 0.6, ps("de 1 a 15", "i", 130), XE, 450)
        E.frase(c, t, lerp(a9, b9, 0.5), ps("na ponta da língua", "i", 92), XE, 580)
        E.frase(c, t, lerp(a9, b9, 0.85), ps("não decore", "g", 76, ERRADO) + ps("lista", "i", 84), XE, 720)
        E.frase(c, t, b9, ps("veja o piso crescer", "i", 92, COR), XE, 860)
        cel, x, y = 92, 1180, 680
        for n, ti in ((1, b9), (2, b9 + 0.5), (3, b9 + 1.0), (4, b9 + 1.5)):
            cels = [(i, j) for i in range(n) for j in range(n) if i == n - 1 or j == n - 1]
            lajotas(c, t, [(cx, -cy) for cx, cy in cels], x, y, cel, ti, 0.03, E.COR if n % 2 else CLARO)
    E.saida(c, t, C["s10"] - 0.1, s09)

    if C["s10"] <= t < C["s11"] + 0.4:
        a, b_, c_, d, e, f, g = (C[f"s10.{k}"] for k in "abcdefg")

        def s10():
            cel, x, y = 150, 240, 300
            # o piso de 3 fica embaixo à esquerda; a faixa nova entra em cima e à direita
            piso(c, t, x, y + cel, cel, 3, a, 0.04)
            lajotas(c, t, [(3, 3), (3, 2), (3, 1)], x, y, cel, c_, 0.12, CLARO)
            lajotas(c, t, [(0, 0), (1, 0), (2, 0)], x, y, cel, d, 0.12, CLARO)
            lajotas(c, t, [(3, 0)], x, y, cel, e, 0, CERTO)
            X = 1000
            E.frase(c, t, a, ps("3 por 3:", "i", 84) + ps("9 lajotas", "g", 80, COR), X, 250)
            E.frase(c, t, b_, ps("para virar", "i", 84) + ps("4 por 4", "g", 80, COR), X, 390)
            fl(c, t, [("3", CLARO, c_), ("+", None, d - 0.1), ("3", CLARO, d), ("+", None, e - 0.1), ("1", CERTO, e), ("=", None, f - 0.1), ("7", COR, f)], X, 570, 120)
            E.frase(c, t, f + 0.2, ps("lajotas novas", "i", 72), X, 670)
            fl(c, t, [("9", COR, g - 0.2), ("+", None, g - 0.15), ("7", None, g - 0.1), ("=", None, g - 0.05)], X, 860, 130)
            E.foco(c, t, g, 0.5, lambda q: num_bola(c, "16", X + 560, 815, 125, 120, q, CERTO, BR))
        E.saida(c, t, C["s11"] - 0.1, s10)

    if t >= C["s11"] and t < C["s12"] + 0.4:
        a, b_, c_, d, e, f = (C[f"s11.{k}"] for k in "abcdef")

        def s11():
            E.frase(c, t, C["s11"] + 0.1, ps("a faixa nova ganha sempre", "i", 72), XE, 170, passo=0.14)
            E.frase(c, t, a, ps("2 lajotas a mais", "g", 76, COR), XE, 270)
            E.frase(c, t, lerp(a, b_, 0.55), ps("a escada", "i", 92), XE, 400)
            degraus(c, t, ESCADA[:5], [b_, c_, d, e, f], 200, 300)
        E.saida(c, t, C["s12"] - 0.1, s11)

    if C["s12"] <= t < C["s13"] + 0.4:
        a, b_, c_, d, e, f, g, h, i_, j = (C[f"s12.{k}"] for k in "abcdefghij")
        tv = lerp(e, f, 0.8)

        def p2():
            E.frase(c, t, lerp(e, f, 0.25), ps("a tabuada", "i", 76) + ps("confere", "g", 72, COR), XE, 200)
            E.frase(c, t, lerp(e, f, 0.4), ps("cada degrau", "i", 76), XE, 300)
            degraus(c, t, ESCADA[4:10], [None, a, b_, c_, d, e], 200, 255)
        E.saida(c, t, tv, p2)
        if t >= tv:
            def p3():
                E.frase(c, t, tv + 0.2, ps("depois do", "i", 84) + ps("100", "g", 80, COR), XE, 200)
                E.frase(c, t, tv + 0.5, ps("a escada continua", "i", 76), XE, 300)
                degraus(c, t, ESCADA[9:15], [None, f, g, h, i_, j], 200, 255)
            E.saida(c, t, C["s13"] - 0.1, p3)

    if t >= C["s13"]:
        a, b_, c_ = C["s13.a"], C["s13.b"], C["s13.c"]
        E.frase(c, t, C["s13"] + 0.1, ps("o pulo", "g", 110, COR), W / 2, 200, "center")
        E.frase(c, t, a, ps("é o lado antigo", "i", 92) + ps("+", "g", 84, COR) + ps("o lado novo", "i", 92), W / 2, 320, "center")
        y = 610
        fm(c, t, b_ - 0.5, "13^2", 330, y, 170)
        fm(c, t, b_ - 0.3, "14^2", 1300, y, 170)
        E.ponte(c, t, b_, 680, 1240, y - 55, "13 + 14 = 27", size=64)
        E.frase(c, t, c_, ps("guarde", "i", 96) + ps("uma regra", "g", 96, COR), W / 2, 830, "center")
        E.frase(c, t, c_ + 0.8, ps("e suba a escada", "i", 96), W / 2, 950, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a, b_, c_, d = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
    E.frase(c, t, C["s14"] + 0.1, ps("o erro do começo", "i", 72, ERRADO), XE, 130)
    y1, y2 = 290, 460
    s = 100
    fm(c, t, a, "2 × 5", XE, y1, s, ERRADO)
    fm(c, t, a + 0.5, "= 2 + 2 + 2 + 2 + 2 = 10", XE + 300, y1, s)
    fm(c, t, b_, "2^5", XE, y2, s, COR)
    fm(c, t, b_ + 0.5, "= 2 × 2 × 2 × 2 × 2 = 32", XE + 300, y2, s)
    E.frase(c, t, b_ + 1.2, ps("cada", "i", 72) + ps("+", "g", 64) + ps("vira", "i", 72) + ps("×", "g", 64, COR), XE, 590)
    M.line(c, XE, 640, W - XE, 640, FIO, ep(t, c_, 0.5), 3)
    y3, y4 = 790, 950
    fm(c, t, c_, "2^2 = 4", XE, y3, 110)
    fm(c, t, c_ + 0.5, "2 × 2 = 4", 660, y3, 110)
    E.frase(c, t, lerp(c_, d, 0.65), ps("coincidência", "g", 76, ERRADO), 1250, y3 - 15)
    fm(c, t, d, "3^2 = 9", XE, y4, 110, CERTO)
    fm(c, t, d + 0.8, "3 × 2 = 6", 660, y4, 110, ERRADO)
    E.foco(c, t, d + 1.0, 0.5, lambda q: E.selo(c, 1290, y4 - 38, 58, False, q))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        a, b_, c_, d, e, f = (C[f"s15.{k}"] for k in "abcdef")
        E.frase(c, t, C["s15"] + 0.1, ps("agora, o atalho", "i", 76, CLARO), W / 2, 130, "center")
        E.frase(c, t, a, ps("quadrado de número", "i", 84, BR) + ps("terminado em 5", "g", 76, BR), W / 2, 240, "center", 0.17)
        y, s, x = 560, 220, 200
        E.foco(c, t, b_, 0.5, lambda q: E.formula(c, "35^2", x, y, s, cor=BR, a=q))
        w3 = E.formula(None, "3", 0, 0, s, a=0)
        w5 = E.formula(None, "5", 0, 0, s, a=0)
        if t >= c_:
            E.risco(c, x + w3 + 10, y + 12, x + w3 + w5 - 4, y - 165, t, c_, largura=16)
        X = 900
        E.frase(c, t, c_ + 0.1, ps("tire o 5:", "i", 84, CLARO) + ps("sobra o 3", "g", 80, BR), X, 400)
        fm(c, t, d, "3 × 4 = 12", X, 560, 130, BR)
        E.frase(c, t, d + 0.5, ps("o 3 vezes o seguinte", "i", 60, CLARO), X, 650, passo=0.12)
        ye = 880
        E.frase(c, t, e - 0.1, ps("12", "g", 170, BR), 330, ye)
        E.foco(c, t, e + 0.2, 0.5, lambda q: E.escreve(c, "25", 330 + E.larg("12", "g", 170) + 16, ye, 170, "g", CLARO, q))
        sinal(c, t, f - 0.2, "=", 880, ye - 60, 130, BR)
        E.foco(c, t, f, 0.5, lambda q: num_bola(c, "1.225", 1290, ye - 60, 160, 96, q, CERTO, BR))
    E.saida(c, t, C["s16"] - 0.1, s15)

    if C["s16"] <= t < C["s17"] + 0.4:
        a, b_, c_, d, e, f, g = (C[f"s16.{k}"] for k in "abcdefg")

        def s16():
            E.frase(c, t, C["s16"] + 0.1, ps("por que funciona?", "i", 80, CLARO), W / 2, 130, "center")
            k, x, y = 13.5, 300, 340  # 1 unidade = k px; (x, y) = canto de cima do piso depois de colar
            base = y + 5 * k  # topo do piso original
            q0 = ep(t, a, 0.5)
            if q0 > 0:
                L = 30 * k
                M.rrect(c, x, base, L, 35 * k, 6, CLARO, q0)
                for i in range(1, 7):
                    M.line(c, x + i * 5 * k, base, x + i * 5 * k, base + 35 * k, "#0A0820", 0.2 * q0, 2)
                for j in range(1, 7):
                    M.line(c, x, base + j * 5 * k, x + L, base + j * 5 * k, "#0A0820", 0.2 * q0, 2)
                pf = ease_io(prog(t, c_, 0.9))
                # a faixa de 5: gira 90° e sobe; a ponta fica para fora
                cx0, cy0 = x + 32.5 * k, base + 17.5 * k
                cx1, cy1 = x + 17.5 * k, base - 2.5 * k
                c.save()
                c.translate(lerp(cx0, cx1, pf), lerp(cy0, cy1, pf))
                c.rotate(-90 * pf)
                c.translate(-2.5 * k, -17.5 * k)
                M.rrect(c, 0, 0, 5 * k, 35 * k, 4, BR if t >= b_ else CLARO, q0)
                c.restore()
                if t >= f:
                    M.rrect(c, x + 30 * k, y, 5 * k, 5 * k, 4, CERTO, ep(t, f, 0.4))
                if t < c_:
                    E.foco(c, t, a, 0.45, lambda p: centro(c, "35", x + 17.5 * k, base - 20, 56, "b", BR, p))
                else:
                    E.foco(c, t, d, 0.45, lambda p: centro(c, "30", x + 15 * k, y - 22, 56, "b", BR, p))
                    E.foco(c, t, d, 0.45, lambda p: E.escreve(c, "40", x - 92, y + 20 * k + 20, 56, "b", BR, p))
            X = 960
            fm(c, t, d, "30 × 40", X, 330, 130, BR)
            E.frase(c, t, d + 0.6, ps("é o", "i", 68, CLARO) + ps("3 × 4", "g", 64, BR) + ps("com dois zeros", "i", 68, CLARO), X, 440, passo=0.14)
            E.foco(c, t, e, 0.5, lambda q: E.formula(c, "= 1.200", X, 590, 130, cor=CLARO, a=q))
            E.frase(c, t, f + 0.1, ps("a ponta da faixa:", "i", 68, CLARO), X, 720, passo=0.14)
            fm(c, t, f + 0.4, "5 × 5 = 25", X, 830, 100, BR)
            fm(c, t, g, "1.200 + 25 =", X, 960, 88, BR)
            E.foco(c, t, g + 0.3, 0.5, lambda q: num_bola(c, "1.225", 1640, 915, 125, 72, q, CERTO, BR))
        E.saida(c, t, C["s17"] - 0.1, s16)

    if t >= C["s17"]:
        a, b_, c_ = C["s17.a"], C["s17.b"], C["s17.c"]
        E.frase(c, t, C["s17"] + 0.1, ps("com final 5", "i", 92, CLARO), XE, 230)
        fm(c, t, a, "30 × 40", XE, 400, 140, BR)
        E.frase(c, t, a + 0.3, ps("dois números", "i", 80, CLARO) + ps("redondos", "g", 76, BR), 820, 390, passo=0.15)
        M.line(c, XE, 480, W - XE, 480, CLARO, 0.3 * ep(t, b_ - 0.5, 0.5), 3)
        E.frase(c, t, lerp(a, b_, 0.75), ps("com outro final", "i", 92, CLARO), XE, 590)
        fm(c, t, b_, "36^2", XE, 760, 140, BR)
        fl(c, t, [("=", CLARO, b_ + 0.4), ("30 × 42", BR, b_ + 0.5), ("+", CLARO, b_ + 2.2), ("6 × 6", BR, b_ + 2.3)], 520, 750, 110)
        E.frase(c, t, c_, ps("aí", "i", 100, BR) + ps("não compensa:", "g", 92, ERRADO) + ps("arme a conta", "g", 92, BR), XE, 930, passo=0.17)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a, b_, c_ = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 170)
    fl(c, t, [("5^4", COR, a), ("=", None, a + 0.2), ("?", CINZA, a + 0.2)], XE, 400, 170)
    E.frase(c, t, b_, ps("uma praça com", "i", 84), XE, 590, passo=0.15)
    E.frase(c, t, lerp(b_, c_, 0.3), ps("45", "g", 92, COR) + ps("fileiras de", "i", 84) + ps("45", "g", 92, COR) + ps("lajotas", "i", 84), XE, 700, passo=0.17)
    E.frase(c, t, c_, ps("quantas", "i", 110) + ps("lajotas?", "g", 110, COR), XE, 860)
    E.relogio(c, t, C["s19.a"], 1520, 360, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a, b_, c_ = C["s20.a"], C["s20.b"], C["s20.c"]

    def s20():
        fl(c, t, [("5^4", COR, C["s20"] + 0.1), ("=", None, C["s20"] + 0.3)], XE, 300, 170)
        fm(c, t, lerp(C["s20"], a, 0.5), "5 × 5 × 5 × 5", 570, 295, 120)
        fm(c, t, a, "5 × 5 = 25", 570, 480, 110)
        fm(c, t, b_, "25 × 5 = 125", 570, 640, 110)
        fm(c, t, c_ - 0.1, "125 × 5 =", 570, 800, 110)
        E.foco(c, t, c_, 0.5, lambda q: num_bola(c, "625", 1270, 765, 125, 96, q, CERTO, BR))
        tq = lerp(c_, C["s20.end"], 0.5)
        fm(c, t, tq, "5 × 4 = 20", XE, 980, 88, ERRADO)
        if t >= tq + 0.3:
            E.risco(c, XE - 10, 985, XE + 480, 930, t, tq + 0.3, largura=10)
        E.frase(c, t, tq + 0.4, ps("o erro de sempre", "i", 72, ERRADO), 720, 965, passo=0.14)
    E.saida(c, t, C["s21"] - 0.1, s20)

    if t >= C["s21"]:
        a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
        E.frase(c, t, C["s21"] + 0.1, ps("na praça", "i", 92, COR), XE, 230)
        fm(c, t, a1, "45^2", XE, 450, 190)
        fm(c, t, b1, "4 × 5 = 20", 830, 330, 120)
        E.frase(c, t, b1 + 0.4, ps("o 4 vezes o seguinte", "i", 60, TINTA2), 830, 420, passo=0.12)
        ye = 780
        E.escreve(c, "20", 400, ye, 200, "g", TINTA, ep(t, c1, 0.4))
        E.foco(c, t, c1 + 0.3, 0.5, lambda q: E.escreve(c, "25", 400 + E.larg("20", "g", 200) + 16, ye, 200, "g", COR, q))
        sinal(c, t, d1 - 0.2, "=", 1040, ye - 70, 130)
        E.foco(c, t, d1, 0.5, lambda q: num_bola(c, "2.025", 1400, ye - 70, 170, 98, q, CERTO, BR))
        E.frase(c, t, d1 + 0.3, ps("lajotas", "g", 76, CERTO), 1400, 960, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    a, b_ = C["s22.a"], C["s22.b"]

    def resumo():
        E.frase(c, t, C["s22"] + 0.1, ps("resumindo", "i", 92, COR), W / 2, 190, "center")
        fm(c, t, a, "2^5", XE, 470, 170, COR)
        E.frase(c, t, a + 0.3, ps("o expoente diz", "i", 76), 550, 360, passo=0.14)
        E.frase(c, t, a + 0.8, ps("quantas vezes", "g", 88, COR) + ps("a base aparece", "i", 88), 550, 470, passo=0.16)
        E.frase(c, t, b_, ps("a escada", "g", 96, COR) + ps("monta os quadrados", "i", 96), W / 2, 760, "center")
        fm(c, t, b_ + 0.9, "1, 4, 9, 16, 25...", W / 2, 910, 96, align="center")
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a2, b2, c2, d2 = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula: a base muda", "i", 84), XE, 240)
    fl(c, t, [("(−2)^3", COR, a2), ("(f{2}{3})^3", COR, a2 + 0.5), ("0,3^2", COR, a2 + 1.0)], XE, 430, 120, gap=90)
    E.frase(c, t, b2, ps("na", "i", 88) + ps("ordem", "g", 88, COR) + ps("das operações", "i", 88), XE, 640)
    E.foco(c, t, c2, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1480, 360, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1620, p), lerp(650, 400, p), ep(t, c2 + 0.2, 0.4), TINTA)
    E.frase(c, t, d2, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 880, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, papel=b_papel, nomes=b_nomes, quadrados=b_quadrados, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
