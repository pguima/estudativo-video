"""Visual — Estudativo · MAT-EQU-019: sistema de equações pelo método da adição.
A soma de equações aparece como conta armada em colunas (x, sinal, y, =, número), para a letra que some ficar à vista.
A balança mostra por que pode somar: juntar coisas que valem o mesmo nos dois pratos. Peças locais: conta_sis, balanca2, destaca."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
import math

E.usar("Matemática", "Equações do 1º Grau")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-EQU-019_sistema_metodo_da_adicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("balanca", "multiplicar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
assert 3 * 4 + 2 * 2 == 16 and 5 * 4 - 2 * 2 == 16 and 32 / 8 == 4
assert 2 * 3 + 3 * 2 == 12 and 3 * 3 + 2 * 2 == 13 and 6 * 3 + 9 * 2 == 36 and 6 * 3 + 4 * 2 == 26
assert abs((12 - 26) / 5 - (-2.8)) < 1e-9 and 25 / 5 == 5
assert 5 + 2 * 3 == 11 and 3 * 5 - 4 * 3 == 3 and 2 * 11 == 22


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def destaca(c, s, sub, x, y, size, cor, a, n=0):
    """realce translúcido atrás de um trecho de uma linha escrita em x (borda), y (base); n = qual ocorrência"""
    if a <= 0:
        return
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(sub, i0 + 1)
    ap = E.APERTO["g"] * size
    x0 = x + (E.larg(s[:i0], "g", size) + ap if i0 > 0 else 0)
    w = E.larg(sub, "g", size)
    M.rrect(c, x0 - size * 0.14, y - size * 0.92, w + size * 0.28, size * 1.2, size * 0.2, cor, 0.2 * a)


def linha_sis(sis_x, size, i, dy=None):
    """x da borda e y da base da linha i de um E.sistema"""
    return sis_x + size * 0.3, (dy or size * 1.45) * i


def conta_sis(c, t, cols, linhas, tl, op, top, res, y0, size, dy, marcas=(), escuro=False):
    """duas equações armadas em colunas (x, sinal, y, =, número), com o sinal da operação, a barra e a linha do resultado.
    res = [(coluna, texto, t0[, cor])]; marcas = [(linha, coluna, t0, cor)] realça uma casa (linha = len(linhas) é o resultado)"""
    tinta = BR if escuro else TINTA
    n = len(linhas)
    ys = [y0 + i * dy for i in range(n)] + [y0 + n * dy + size * 0.2]
    for (li, ci, t0, cor) in marcas:
        q = ep(t, t0, 0.35)
        if q > 0:
            w = E.larg(linhas[li][ci] if li < n else next(r[1] for r in res if r[0] == ci), "g", size)
            M.rrect(c, cols[ci] - w / 2 - size * 0.16, ys[li] - size * 0.92, w + size * 0.32, size * 1.2, size * 0.2, cor, 0.22 * q)
    for i, (lin, ti) in enumerate(zip(linhas, tl)):
        for x, s in zip(cols, lin):
            if s:
                cen(c, t, ti, s, x, ys[i], size, tinta)
    xo = cols[0] - size * 1.05
    cen(c, t, top, op, xo, ys[n - 1], size, CLARO if escuro else COR)
    p = ep(t, top + 0.15, 0.5)
    if p > 0:
        yb = ys[n - 1] + size * 0.42
        M.line(c, xo - size * 0.4, yb, lerp(xo - size * 0.4, cols[-1] + size * 0.8, p), yb, tinta, 1.0, 6)
    for r in res:
        cen(c, t, r[2], r[1], cols[r[0]], ys[n], size, r[3] if len(r) > 3 else tinta)
    return ys


def balanca2(c, cx, cy, esq, dir_, inclina=0.0, a=1.0, hw=(260, 200), braco=1000, k=1.0, escuro=False):
    """balança como E.balanca, com pratos de largura fixa e conteúdo desenhado por fn(px, base): o conteúdo pode entrar aos poucos"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    c.save(); c.translate(cx, cy); c.scale(k, k)
    ang = math.radians(9 * max(-1, min(1, inclina)))
    topo = -250
    M.rrect(c, -150, 220, 300, 26, 13, tinta, a)
    M.line(c, 0, 220, 0, topo, tinta, a, 12)
    pontas = [(lado * braco / 2 * math.cos(ang), topo + lado * braco / 2 * math.sin(ang)) for lado in (-1, 1)]
    M.line(c, pontas[0][0], pontas[0][1], pontas[1][0], pontas[1][1], tinta, a, 12)
    c.drawCircle(0, topo, 20, M.paint(E.COR, a))
    for (px, py), fn, h in zip(pontas, (esq, dir_), hw):
        yp = py + 300
        for dx in (-h, h):
            M.line(c, px, py, px + dx, yp, CINZA, a, 3)
        p = skia.Path()
        p.moveTo(px - h, yp); p.lineTo(px + h, yp); p.lineTo(px + h - 50, yp + 34); p.lineTo(px - h + 50, yp + 34); p.close()
        c.drawPath(p, M.paint(E.COR, a))
        if fn:
            fn(px, yp - 24)
    c.restore()


def selo_em(c, t, t0, cx, cy, r, ok=True):
    E.foco(c, t, t0, 0.5, lambda a: E.selo(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), ok, a), blur=0)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def sis():
        sx, sy, sz = 640, 330, 120
        E.sistema(c, t, ka, ["3x + 2y = 16", "5x − 2y = 16"], sx, sy, sz, tl=(ka, kb))
        y2 = sy + sz * 1.45
        cen(c, t, kc, "+", sx - 100, y2, 120, COR)
        p = ep(t, kc + 0.2, 0.5)
        if p > 0:
            M.line(c, sx - 160, y2 + 60, lerp(sx - 160, 1420, p), y2 + 60, TINTA, 1.0, 7)
        E.saida(c, t, kc - 0.1, lambda: E.frase(c, t, lerp(kb, kc, 0.45), ps("nenhuma letra está sozinha", "i", 84), W / 2, 820, "center", 0.12))
        E.frase(c, t, kc + 0.1, [("some", "g", 96, COR)] + ps("uma equação com a outra", "i", 88), W / 2, 820, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, sis)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1490, 540, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), ps("por que", "i", 96) + [("pode somar", "g", 110, COR)], XE, 470, passo=0.14)
        E.frase(c, t, tb, ps("e quando", "i", 96) + [("não basta", "g", 110)], XE, 640, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1490, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1490, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.2, ps("lembre", "i", 84), XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "a solução vale", "nas duas equações"), ("s03.c", "menos antes do parêntese", "troca todos os sinais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 220 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    py = lerp(390, 650, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.62), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 820, "left", 0.12)


# ---------------- por que pode somar: a balança ----------------
def b_balanca(c, t, C, b):
    ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    E.saida(c, t, a5 - 0.1, lambda: E.frase(c, t, ka - 0.4, ps("a primeira equação é uma", "i", 76) + [("balança equilibrada", "g", 76, COR)], W / 2, 150, "center", 0.12))
    E.linha(c, t, [("5x − 2y", "g", 92, COR, a5), ("vale", "i", 88, TINTA, a5 + 0.4), ("16", "g", 92, COR, a5 + 0.7),
                   ("na segunda equação", "i", 70, TINTA2, a5 + 1.0)], W / 2, 150, "center")
    inc = -0.7 * ep(t, b5 + 0.4, 0.7) + 0.7 * ep(t, c5 + 0.3, 0.7)
    cy = 520

    def esq(px, yb):
        E.foco(c, t, kb, 0.5, lambda a: E.formula(c, "3x + 2y", px, yb, 92, cor=TINTA, a=a, align="center"))
        E.foco(c, t, b5, 0.5, lambda a: E.formula(c, "+ 5x − 2y", px, yb - 100, 80, cor=COR, a=a, align="center"))

    def dir_(px, yb):
        E.foco(c, t, kc, 0.5, lambda a: E.formula(c, "16", px, yb, 92, cor=TINTA, a=a, align="center"))
        E.foco(c, t, c5, 0.5, lambda a: E.formula(c, "+ 16", px, yb - 100, 80, cor=COR, a=a, align="center"))
    E.foco(c, t, ka, 0.6, lambda a: balanca2(c, 960, cy, esq, dir_, inc, a, hw=(400, 250)))

    def pesos():
        for x in (460, 1460):
            E.foco(c, t, kd, 0.5, lambda a, x=x: E.pilula(c, "+ mesmo peso", x, 690, 50, estilo="b", a=a), sobe=10)
        E.frase(c, t, kd + 0.6, ps("continua", "i", 80) + [("equilibrada", "g", 76, CERTO)], W / 2, 930, "center", 0.14)
    E.saida(c, t, a5 - 0.1, pesos)
    E.frase(c, t, d5, ps("mesmo peso nos dois pratos:", "i", 76) + [("continua equilibrada", "g", 72, CERTO)], W / 2, 930, "center", 0.12)


# ---------------- somando ----------------
COLS = (380, 520, 660, 800, 950)


def b_somar(c, t, C, b):
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    a7, b7, c7, d7, e7, f7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"], C["s07.e"], C["s07.f"]

    def tela():
        E.frase(c, t, C["s06"], ps("somando", "i", 80) + [("as duas", "g", 76, COR)], XE, 160)
        sz = 100
        ys = conta_sis(c, t, COLS, [["3x", "+", "2y", "=", "16"], ["5x", "−", "2y", "=", "16"]], (C["s06"] + 0.2, C["s06"] + 0.4),
                       "+", C["s06"] + 0.6, [(0, "8x", a6, COR), (1, "+", b6), (2, "0", b6, COR), (3, "=", d6), (4, "32", d6, COR)], 330, sz, 150,
                       marcas=[(0, 0, a6, COR), (1, 0, a6, COR), (0, 2, b6, COR), (1, 2, b6, COR), (0, 4, d6, COR), (1, 4, d6, COR)])
        E.foco(c, t, c6, 0.4, lambda a: E.pilula(c, "o y sumiu!", COLS[2], ys[2] + 110, 46, estilo="b", a=a), sobe=8)
        E.foco(c, t, e6, 0.5, lambda a: (E.caixa_pontilhada(c, 300, 790, 600, 170, a), E.formula(c, "8x = 32", 600, 910, 120, cor=TINTA, a=a, align="center")))
        # resolvendo à direita
        xr = 1430
        E.foco(c, t, a7, 0.4, lambda a: E.pilula(c, "÷ 8 nos dois lados", xr, 240, 46, estilo="b", a=a), sobe=8)
        fcen(c, t, b7, "x = 4", xr, 400, 120, COR)
        cen(c, t, lerp(b7, c7, 0.55), "3x = 3 × 4 = 12", xr, 490, 50, TINTA2, "b")
        fcen(c, t, c7, "12 + 2y = 16", xr, 600, 96)
        E.foco(c, t, d7, 0.4, lambda a: E.pilula(c, "− 12 nos dois lados", xr, 690, 46, estilo="b", a=a), sobe=8)
        fcen(c, t, e7, "2y = 4", xr, 820, 96)
        fcen(c, t, f7, "y = 2", xr, 970, 120, COR)
    E.saida(c, t, C["s08"] - 0.1, tela)
    if t < C["s08"]:
        return
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    E.frase(c, t, C["s08"], ps("conferindo na", "i", 80) + [("segunda", "g", 76, COR)], XE, 170)
    E.foco(c, t, C["s08"] + 0.3, 0.4, lambda a: (E.pilula(c, "x = 4", 1340, 145, 52, estilo="g", a=a), E.pilula(c, "y = 2", 1600, 145, 52, estilo="g", a=a)))
    fcen(c, t, C["s08"] + 0.5, "5x − 2y = 16", W / 2, 380, 110)
    fcen(c, t, a8, "5 × 4 = 20", 560, 590, 100, COR)
    fcen(c, t, b8, "2 × 2 = 4", 1360, 590, 100, COR)
    fcen(c, t, c8, "20 − 4 = 16", 880, 820, 130)
    selo_em(c, t, d8, 1430, 780, 70)
    E.frase(c, t, d8 + 0.2, [("bateu", "g", 80, CERTO)], 1530, 810)


# ---------------- quando não basta: multiplicar antes ----------------
S2 = ["2x + 3y = 12", "3x + 2y = 13"]


def b_multiplicar(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]

    def opostos():
        sx, sy, sz = 560, 330, 110
        E.sistema(c, t, C["s09"], ["3x + 2y = 16", "5x − 2y = 16"], sx, sy, sz)
        x0 = sx + sz * 0.3
        destaca(c, "3x + 2y = 16", "+ 2y", x0, sy, sz, COR, ep(t, a9, 0.4))
        destaca(c, "5x − 2y = 16", "− 2y", x0, sy + sz * 1.45, sz, COR, ep(t, a9 + 0.3, 0.4))
        E.frase(c, t, lerp(a9, b9, 0.42), [("opostos", "g", 110, COR)] + ps("se anulam", "i", 110), W / 2, 820, "center", 0.14)
    E.saida(c, t, b9 - 0.1, opostos)
    if t < b9 - 0.1:
        return
    a12 = C["s12.a"]

    # tela 2: o sistema novo, a ideia de multiplicar e o x com 6 na frente
    sx, sy, sz = 250, 300, 90

    def tela2():
        E.sistema(c, t, b9, S2, sx, sy, sz, tl=(b9, c9))
        E.saida(c, t, C["s10.a"] - 0.1, lambda: E.frase(c, t, b9 - 0.4, ps("e neste sistema?", "i", 90), W / 2, 640, "center", 0.12))
        a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]

        def ideia():
            E.saida(c, t, b10 - 0.1, lambda: E.frase(c, t, a10, ps("somando direto,", "i", 84) + [("nenhuma letra some", "g", 80, ERRADO)], W / 2, 640, "center", 0.12))

            def mult():
                E.frase(c, t, b10, [("multiplique antes", "g", 100, COR)], W / 2, 620, "center")
                E.frase(c, t, b10 + 0.6, ps("até uma letra ter o", "i", 72) + [("mesmo número na frente", "g", 68)], W / 2, 740, "center", 0.1)
            E.saida(c, t, c10 - 0.1, mult)

            def esq(px, yb):
                E.formula(c, "2x + 3y", px, yb, 92, cor=TINTA, align="center")

            def dir_(px, yb):
                E.formula(c, "12", px, yb, 92, cor=TINTA, align="center")

            def bal():
                balanca2(c, 960, 690, esq, dir_, 0, 1.0, hw=(230, 150), braco=900, k=0.72)
                for x in (960 - 324, 960 + 324):
                    E.foco(c, t, c10 + 0.6, 0.4, lambda a, x=x: E.pilula(c, "× 3", x, 830, 52, estilo="g", a=a), sobe=8)
            E.foco(c, t, c10, 0.5, lambda a: bal())
        E.saida(c, t, C["s11"] - 0.1, ideia)

        a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
        y1, y2 = sy, sy + sz * 1.45
        E.ponte(c, t, a11, 840, 1110, y1 - 30, "× 3", None, 50)
        E.ponte(c, t, c11, 840, 1110, y2 - 30, "× 2", None, 50)
        xn = 1160
        destaca(c, "6x + 9y = 36", "6x", xn, y1, sz, COR, ep(t, e11, 0.4))
        destaca(c, "6x + 4y = 26", "6x", xn, y2, sz, COR, ep(t, e11 + 0.2, 0.4))
        E.formula_em(c, t, b11, "6x + 9y = 36", xn, y1, sz)
        E.formula_em(c, t, d11, "6x + 4y = 26", xn, y2, sz)
        E.frase(c, t, e11, ps("o x ficou com", "i", 84) + [("6 na frente", "g", 84, COR)] + ps("nas duas", "i", 84), W / 2, 760, "center", 0.12)
    E.saida(c, t, a12 - 0.1, tela2)
    if t < a12 - 0.1:
        return

    # tela 3: subtrair e resolver
    a12, b12, c12, d12, e12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
    a13, b13, c13, d13, e13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]

    def tela3():
        E.frase(c, t, a12, [("subtraia", "g", 80, COR)] + ps("a segunda da primeira", "i", 80), XE, 150, "left", 0.12)
        E.frase(c, t, b12, ps("tirar o mesmo peso de cada prato", "i", 56, TINTA2), XE, 225, "left", 0.08)
        ys = conta_sis(c, t, COLS, [["6x", "+", "9y", "=", "36"], ["6x", "+", "4y", "=", "26"]], (a12, a12 + 0.2), "−", a12 + 0.4,
                       [(0, "0", c12, COR), (1, "+", d12), (2, "5y", d12, COR), (3, "=", e12), (4, "10", e12, COR)], 360, 100, 150,
                       marcas=[(0, 0, c12, COR), (1, 0, c12, COR), (0, 2, d12, COR), (1, 2, d12, COR), (0, 4, e12, COR), (1, 4, e12, COR)])
        tm = lerp(b12, c12, 0.35)
        E.frase(c, t, tm, ps("o menos vale para", "i", 60) + [("cada termo", "g", 58, COR)], XE, 850, "left", 0.1)
        fcen(c, t, tm + 1.2, "−(6x + 4y) = −6x − 4y", 600, 950, 66, TINTA2)
        xr = 1430
        fcen(c, t, a13, "5y = 10", xr, 330, 100)
        fcen(c, t, b13, "y = 2", xr, 480, 120, COR)
        cen(c, t, lerp(b13, c13, 0.45), "na 1ª: 3y = 3 × 2 = 6", xr, 570, 48, TINTA2, "b")
        fcen(c, t, c13, "2x + 6 = 12", xr, 680, 96)
        fcen(c, t, d13, "2x = 6", xr, 820, 96)
        fcen(c, t, e13, "x = 3", xr, 970, 120, COR)
    E.saida(c, t, C["s14"] - 0.1, tela3)
    if t < C["s14"] - 0.1:
        return

    # tela 4: conferir e a regra
    a14, b14, c14, d14, e14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]

    def confere():
        E.frase(c, t, C["s14"], ps("conferindo na", "i", 80) + [("segunda", "g", 76, COR)], XE, 170)
        E.foco(c, t, C["s14"] + 0.3, 0.4, lambda a: (E.pilula(c, "x = 3", 1340, 145, 52, estilo="g", a=a), E.pilula(c, "y = 2", 1600, 145, 52, estilo="g", a=a)))
        fcen(c, t, C["s14"] + 0.5, "3x + 2y = 13", W / 2, 400, 110)
        fcen(c, t, a14, "3 × 3 = 9", 560, 620, 100, COR)
        fcen(c, t, lerp(a14, b14, 0.5), "9 + 4 = 13", 1300, 620, 100, COR)
        selo_em(c, t, b14, 880, 830, 70)
        E.frase(c, t, b14 + 0.2, [("bateu", "g", 80, CERTO)], 980, 860)
    E.saida(c, t, c14 - 0.1, confere)
    if t < c14:
        return
    E.frase(c, t, c14 - 0.1, [("a regra", "i", 90, COR)], XE, 200)
    regras = ((c14, "+2y  −2y", "números opostos", "some"), (d14, "6x  6x", "números iguais", "subtraia"),
              (e14, "3y  2y", "nem um nem outro", "multiplique antes"))
    for i, (k, ex, l1, l2) in enumerate(regras):
        y = 400 + i * 210
        E.foco(c, t, k, 0.5, lambda a, ex=ex, y=y: (M.rrect(c, XE - 20, y - 82, 360, 112, 22, E.COR, 0.12 * a),
                                                    E.formula(c, ex, XE + 160, y, 72, cor=TINTA, a=a, align="center")))
        E.frase(c, t, k + 0.2, [(l1, "i", 72)], 580, y)
        E.frase(c, t, k + 0.5, [(l2, "g", 80, COR)], 1180, y)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a15, b15 = C["s15.a"], C["s15.b"]
    a16, b16, c16, d16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"]

    def um():
        E.frase(c, t, C["s15"], [("cuidado", "g", 110, ERRADO)] + ps("com o erro mais comum", "i", 90), W / 2, 200, "center", 0.14)
        E.frase(c, t, a15, ps("multiplicar", "i", 84) + [("só um lado", "g", 84, ERRADO)], W / 2, 350, "center", 0.12)
        fcen(c, t, b15 - 0.8, "2x + 3y = 12", 480, 600, 100)
        E.ponte(c, t, b15 - 0.4, 860, 1060, 570, "× 3", None, 50)
        s = "6x + 9y = 12"
        w = E.formula(c, s, 0, 0, 100, a=0)
        x0 = 1460 - w / 2
        destaca(c, s, "12", x0, 600, 100, ERRADO, ep(t, b15 + 1.2, 0.4))
        fcen(c, t, b15, s, 1460, 600, 100)
        E.frase(c, t, b15 + 1.4, ps("o", "i", 76) + [("12", "g", 76, ERRADO)] + ps("ficou sem multiplicar", "i", 76), W / 2, 800, "center", 0.12)
    E.saida(c, t, a16 - 0.1, um)
    if t < a16 - 0.1:
        return

    def bal():
        inc = -0.9 * ep(t, a16 + 0.6, 0.8)

        def esq(px, yb):
            E.formula(c, "6x + 9y", px, yb, 92, cor=TINTA, align="center")
            E.pilula(c, "× 3", px, yb - 120, 50, estilo="g")

        def dir_(px, yb):
            E.formula(c, "12", px, yb, 92, cor=ERRADO, align="center")
        E.foco(c, t, a16, 0.5, lambda a: balanca2(c, 960, 520, esq, dir_, inc, a, hw=(290, 170), braco=1000, k=0.9))
        E.frase(c, t, a16 + 0.9, [("desequilibra", "g", 88, ERRADO)], W / 2, 930, "center")
    E.saida(c, t, b16 - 0.1, bal)

    def depois():
        fcen(c, t, b16, "y = −2,8", W / 2, 360, 150, ERRADO)
        E.frase(c, t, b16 + 0.5, ps("negativo e quebrado", "i", 84), W / 2, 500, "center", 0.12)
        selo_em(c, t, c16, 560, 720, 70, ok=False)
        E.frase(c, t, c16 + 0.2, ps("não confere nas", "i", 80) + [("duas equações", "g", 76)], 660, 750, "left", 0.12)
    if t >= b16 - 0.1:
        E.saida(c, t, d16 - 0.1, depois)
    if t >= d16:
        E.frase(c, t, d16, ps("multiplique a", "i", 96) + [("equação inteira", "g", 96, CERTO)], W / 2, 330, "center", 0.12)
        fcen(c, t, d16 + 0.4, "2x + 3y = 12", 480, 640, 100)
        E.ponte(c, t, d16 + 0.7, 860, 1060, 610, "× 3", None, 50)
        s = "6x + 9y = 36"
        w = E.formula(c, s, 0, 0, 100, a=0)
        destaca(c, s, "36", 1460 - w / 2, 640, 100, CERTO, ep(t, d16 + 1.4, 0.4))
        fcen(c, t, d16 + 1.0, s, 1460, 640, 100)
        E.frase(c, t, d16 + 1.6, ps("os dois lados", "i", 76) + [("vezes 3", "g", 76, CERTO)], W / 2, 840, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    cols = (330, 470, 610, 750, 890)

    def tela():
        tv = lerp(a17, b17, 0.55)

        def grande():
            E.frase(c, t, C["s17"] + 0.2, [("agora,", "i", 100, CLARO), ("o atalho", "g", 110, BR)], W / 2, 380, "center", 0.14)
            E.frase(c, t, a17, ps("antes de resolver,", "i", 84, CLARO), W / 2, 560, "center", 0.1)
            E.frase(c, t, a17 + 0.9, ps("olhe o que a", "i", 96, BR) + [("pergunta pede", "g", 96, BR)], W / 2, 700, "center", 0.12)
        E.saida(c, t, tv - 0.5, grande)
        E.frase(c, t, tv - 0.2, [("o atalho:", "i", 80, CLARO)] + ps("olhe o que a", "i", 80, BR) + [("pergunta pede", "g", 76, BR)], W / 2, 160, "center", 0.06)
        ys = conta_sis(c, t, cols, [["2x", "+", "3y", "=", "12"], ["3x", "+", "2y", "=", "13"]], (tv, tv + 0.3), "+", c17 - 0.5,
                       [(0, "5x", c17, CLARO), (1, "+", c17), (2, "5y", c17, CLARO), (3, "=", c17), (4, "25", c17, CLARO)], 380, 96, 145,
                       escuro=True, marcas=[(2, 0, a18, E.COR), (2, 2, a18, E.COR)])
        E.foco(c, t, b17, 0.5, lambda a: E.pilula(c, "pergunta: x + y", 1450, 360, 60, estilo="g", a=a), sobe=8)
        E.ponte(c, t, d17 - 0.4, 1060, 1260, ys[2] - 30, "÷ 5", None, 50)
        E.foco(c, t, d17, 0.5, lambda a: (E.bola(c, 1560, ys[2] - 30, 150, a=a), E.formula(c, "x + y = 5", 1560, ys[2] + 4, 76, cor=BR, a=a, align="center")))
        E.frase(c, t, a18 + 0.2, ps("cada letra ficou com", "i", 76, CLARO) + [("5 na frente", "g", 76, BR)], W / 2, 900, "center", 0.12)
    E.saida(c, t, b18 - 0.1, tela)
    if t < b18:
        return
    E.frase(c, t, b18, ps("não compensa quando", "i", 84, CLARO), W / 2, 230, "center", 0.12)
    E.foco(c, t, b18 + 0.4, 0.5, lambda a: E.formula(c, "4x + 7y", 600, 460, 110, cor=BR, a=a, align="center"))
    E.frase(c, t, b18 + 0.8, [("números diferentes", "g", 76, BR)] + ps("na frente", "i", 76, CLARO), 900, 450, "left", 0.12)
    E.foco(c, t, c18, 0.5, lambda a: E.formula(c, "x = ?  y = ?", 600, 680, 100, cor=BR, a=a, align="center"))
    E.frase(c, t, c18 + 0.4, [("cada valor", "g", 76, BR)] + ps("separado", "i", 76, CLARO), 900, 670, "left", 0.12)
    E.frase(c, t, lerp(c18, C["s18.end"], 0.55), ps("aí,", "i", 84, CLARO) + [("resolva o sistema inteiro", "g", 84, CLARO)], W / 2, 900, "center", 0.12)


# ---------------- questão ----------------
S3 = ["x + 2y = 11", "3x − 4y = 3"]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s19"] + 0.8, ps("resolva pela", "i", 64) + [("adição", "g", 64, COR)], XE, 290)
    E.sistema(c, t, C["s19.a"], S3, XE + 90, 470, 110, tl=(C["s19.a"], C["s19.b"]))
    E.frase(c, t, C["s19.c"], ps("quanto valem", "i", 96) + [("x e y?", "g", 100, COR)], XE, 850)
    E.relogio(c, t, C["s20.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a21, b21, c21, d21, e21, f21 = (C[f"s21.{k}"] for k in "abcdef")
    a22, b22, c22, d22, e22, f22 = (C[f"s22.{k}"] for k in "abcdef")
    sx, sy, sz = 230, 300, 90

    def tela():
        E.sistema(c, t, C["s21"], S3, sx, sy, sz)
        x0 = sx + sz * 0.3
        destaca(c, S3[0], "+ 2y", x0, sy, sz, COR, ep(t, a21, 0.4))
        destaca(c, S3[1], "− 4y", x0, sy + sz * 1.45, sz, COR, ep(t, a21 + 0.4, 0.4))
        cols = (1150, 1280, 1410, 1540, 1680)
        E.ponte(c, t, b21, 760, 990, sy - 30, "× 2", None, 50)
        ys = conta_sis(c, t, cols, [["2x", "+", "4y", "=", "22"], ["3x", "−", "4y", "=", "3"]], (c21, d21 - 0.3), "+", d21,
                       [(0, "5x", e21, COR), (1, "+", e21), (2, "0", e21, COR), (3, "=", e21), (4, "25", e21, COR)], sy, sz, sz * 1.45,
                       marcas=[(0, 2, d21, COR), (1, 2, d21, COR)])
        E.foco(c, t, f21, 0.5, lambda a: (E.caixa_pontilhada(c, 1170, 760, 480, 170, a), E.formula(c, "x = 5", 1410, 880, 120, cor=COR, a=a, align="center")))
    E.saida(c, t, C["s22"] - 0.1, tela)
    if t < C["s22"]:
        return
    E.foco(c, t, C["s22"], 0.4, lambda a: E.pilula(c, "x = 5", 330, 170, 56, estilo="g", a=a), sobe=8)
    E.frase(c, t, C["s22"] + 0.2, ps("na primeira", "i", 64), 460, 190)
    xl = 520
    fcen(c, t, a22, "5 + 2y = 11", xl, 400, 100)
    fcen(c, t, b22, "2y = 6", xl, 570, 100)
    fcen(c, t, c22, "y = 3", xl, 760, 130, COR)
    xr = 1400
    E.frase(c, t, c22 + 1.0, ps("na segunda:", "i", 64), 1080, 190)
    fcen(c, t, c22 + 1.3, "3x − 4y = 3", xr, 290, 84, TINTA2)
    fcen(c, t, d22, "3 × 5 = 15", xr, 440, 96)
    fcen(c, t, e22, "4 × 3 = 12", xr, 590, 96)
    fcen(c, t, f22, "15 − 12 = 3", xr, 760, 110, COR)
    selo_em(c, t, f22 + 1.0, 1100, 935, 56)
    E.frase(c, t, f22 + 1.1, [("bateu:", "g", 72, CERTO)] + [("x = 5", "g", 72), ("e", "i", 72), ("y = 3", "g", 72)], 1180, 960, "left", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s23.a", "opostos ou iguais"), ("s23.b", "some ou subtraia"), ("s23.c", "confira nas duas"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 470, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 470 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 100)], 570, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"] + 0.2, ps("próxima aula", "i", 84), XE, 330)
    E.frase(c, t, C["s24.a"], [("Montar o sistema", "g", 120, COR)], XE, 480)
    E.frase(c, t, C["s24.a"] + 0.4, [("do problema", "g", 120, COR)], XE, 620)
    E.frase(c, t, C["s24.b"], ps("e supor que tudo é de um tipo só", "i", 60, TINTA2), XE, 730, "left", 0.08)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(720, 425, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, balanca=b_balanca, somar=b_somar, multiplicar=b_multiplicar,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
