"""Visual — Estudativo · MAT-FAV-007: função par e função ímpar.

Linguagem visual da trilha Funções Avançadas (MAT-FAV-001 a 006): x e entrada em índigo (ENT), saída em preto (SAI). Nesta aula:
o teste f(−x) em índigo; a função par no plano com a metade da esquerda dobrando sobre o eixo y (dobra()), o eixo y em destaque;
a função ímpar com uma cópia que gira meia volta em torno da origem (gira()) e cai em cima da curva; x³ aparece com a escala do
eixo y própria (marcas 8 e −8). Expoentes pares em índigo, ímpares em preto no atalho do palco."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-007_funcao_par_e_impar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("teste", "impar", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert (-2) ** 2 == 2 ** 2 == 4 and (-2) ** 3 == -8 == -(2 ** 3)
h1 = lambda x: x ** 3 + 1
assert h1(2) == 9 and h1(-2) == -7 and -h1(2) == -9
assert all((-x) ** 3 - 4 * (-x) == -(x ** 3 - 4 * x) and (-x) ** 2 - 5 == x * x - 5 for x in range(-5, 6))
assert (1 + 1, 1 - 1) == (2, 0)

def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha Funções Avançadas (as mesmas em MAT-FAV-001 a 008) ----------------
# A fonte da casa não tem ℝ nem ∘: fl() desenha ℝ na Cambria e ∘ como um anel.
_CM = skia.FontMgr().makeFromFile("C:/Windows/Fonts/cambria.ttc", 1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def _reais(c, x, y, size, cor, a):
    f = skia.Font(_CM, size * 1.08)
    f.setSubpixel(True)
    f.setEmbolden(True)
    w = f.measureText("ℝ") + size * 0.06
    if c is not None and a > 0:
        c.drawString("ℝ", x + size * 0.03, y, f, M.paint(cor, a))
    return w


def _anel(c, x, y, size, cor, a):
    if c is not None and a > 0:
        c.drawCircle(x + size * 0.27, y - size * 0.34, size * 0.13, M.paint(cor, a, stroke=max(3, size * 0.065)))
    return size * 0.54


def fl(c, s, x, y, size, est="g", cor=TINTA, a=1.0):
    """E.formula com ℝ e ∘; devolve a largura"""
    w = 0.0
    for p in re.split("([ℝ∘])", s):
        if not p:
            continue
        if p == "ℝ":
            w += _reais(c, x + w, y, size, cor, a)
        elif p == "∘":
            w += _anel(c, x + w, y, size, cor, a)
        else:
            w += E.formula(c if a > 0 else None, p, x + w, y, size, est, cor, a)
    return w


def fx(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """fórmula em pedaços de cor: partes = [(escrita, cor[, opacidade])]. Devolve (largura, [x de cada pedaço], [largura de cada])"""
    ws = [fl(None, p[0], 0, 0, size, est, a=0) for p in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    xs = []
    for p, wi in zip(partes, ws):
        xs.append(xx)
        k = p[2] if len(p) > 2 else 1.0
        if a * k > 0:
            fl(c, p[0], xx, y, size, est, p[1], a * k)
        xx += wi
    return w, xs, ws


def fx_em(c, t, t0, partes, x, y, size, align="left", d=0.5):
    E.foco(c, t, t0, d, lambda a: fx(c, partes, x, y, size, a, align))


def fs(c, t, t0, s, x, y, size, cor=TINTA, align="left"):
    """uma fórmula de uma cor só, com foco"""
    fx_em(c, t, t0, [(s, cor)], x, y, size, align)


def eqn(c, esq, dir_, y, size, a=1.0, xi=W / 2, op="=", cor_op=SAI):
    """igualdade com o sinal centrado em xi; esq e dir_ em partes de fx"""
    gap = size * 0.28
    wi = E.larg(op, "g", size)
    _, xe, we = fx(c, esq, xi - wi / 2 - gap, y, size, a, "right")
    if a > 0:
        E.escreve(c, op, xi - wi / 2, y, size, "g", cor_op, a)
    _, xd, wd = fx(c, dir_, xi + wi / 2 + gap, y, size, a)
    return (xe, we), (xd, wd)


def eqn_em(c, t, t0, esq, dir_, y, size, xi=W / 2, op="=", cor_op=SAI, d=0.5):
    E.foco(c, t, t0, d, lambda a: eqn(c, esq, dir_, y, size, a, xi, op, cor_op))


def caixa(c, x, y, w, size, a, cor=None):
    """contorno num pedaço de fórmula (x = borda, y = linha de base, w = largura)"""
    if a <= 0:
        return
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - size * 0.1, y - size * 0.86, w + size * 0.2, size * 1.14), 16, 16),
                M.paint(cor or COR, a, stroke=5))


def nota(c, t, t0, txt, x, y, size=46, fundo=None, cor="#FFFFFF"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, x, y, size, "g", fundo=fundo or COR, cor=cor, a=a), sobe=6)


def anel(c, t, t0, X, Y, cor=None):
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def tenue(c, k, fn):
    """desenha fn com opacidade k"""
    if k <= 0:
        return
    if k >= 0.999:
        fn()
        return
    c.saveLayerAlpha(None, int(255 * k))
    fn()
    c.restore()


def traco(c, P, pts, cor, a=1.0, largura=7, dash=None):
    """polilinha em valores do plano, recortada na caixa"""
    if a <= 0 or len(pts) < 2:
        return
    x, y, w, h = P.caixa
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - 6, y - 6, w + 12, h + 12), True)
    path = skia.Path()
    path.moveTo(*P(*pts[0]))
    for q in pts[1:]:
        path.lineTo(*P(*q))
    pt = M.paint(cor, a, stroke=largura, cap_round=True)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        pt.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(path, pt)
    c.restore()


def amostra(f, a, b, n=240):
    return [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)]


def bolinha(c, P, x, y, cheia, cor=None, a=1.0, r=15):
    """bolinha no plano: cheia (o ponto entra) ou vazia (não entra)"""
    if a <= 0:
        return
    X, Y = P(x, y)
    k = r * ease_back(min(1.0, a * 1.2)) if a < 1 else r
    c.drawCircle(X, Y, k, M.paint(cor or COR if cheia else E.PAPEL, a))
    c.drawCircle(X, Y, k, M.paint(cor or COR, a, stroke=6))


def bolinha_em(c, t, t0, P, x, y, cheia, cor=None):
    bolinha(c, P, x, y, cheia, cor, ep(t, t0, 0.4))


def item(c, t, t0, n, x, y, r=56):
    """número do passo numa esfera; y = linha de base do texto ao lado"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, x, y - 30, r, a=a),
                                     E.escreve(c, str(n), x - E.larg(str(n), "g", r * 1.14) / 2, y - 30 + r * 0.4, r * 1.14, "g", BR, a)))


def chave(c, t, t0, linhas, x, y, size, dy=None, tl=None, cor=TINTA):
    """chave de função por partes: linhas = [partes de fx]; tl = instante de cada linha. Devolve o y de cada linha"""
    dy = dy or size * 1.5
    alto, baixo = y - size * 0.95, y + (len(linhas) - 1) * dy + size * 0.35
    meio = (alto + baixo) / 2
    q = ep(t, t0, 0.5)
    if q > 0:
        p = skia.Path()
        k = size * 0.32
        p.moveTo(x, alto); p.cubicTo(x - k, alto, x - k * 0.2, meio - k, x - k, meio)
        p.cubicTo(x - k * 0.2, meio + k, x - k, baixo, x, baixo)
        c.drawPath(p, M.paint(cor, q, stroke=max(5, size * 0.07), cap_round=True))
    ys = []
    for i, l in enumerate(linhas):
        ti = tl[i] if tl else t0
        yy = y + i * dy
        ys.append(yy)
        fx_em(c, t, ti, l, x + size * 0.3, yy, size)
    return ys


def reta_sol(c, t, t0, x0, x1, y, vmin, vmax, size=44, marcas=None):
    return E.reta(c, t, t0, x0, x1, y, vmin, vmax, marcas or list(range(vmin, vmax + 1)), E._num, size=size)


def pinta(c, t, tb, tp, vx, y, v, lado, fecha, xa, xb, cor=None, r=17):
    """semirreta de solução: bolinha em v (cheia se fecha) e faixa para o lado (+1 direita, −1 esquerda), com seta"""
    cor = cor or COR
    X = vx(v)
    p = ease_out(prog(t, tp, 0.8))
    if p > 0:
        fim = xb if lado > 0 else xa
        M.line(c, X, y, lerp(X, fim, p), y, cor, 1.0, 12, cap_round=False)
        if p > 0.98:
            M.line(c, fim, y, fim - 26 * lado, y - 18, cor, 1.0, 8)
            M.line(c, fim, y, fim - 26 * lado, y + 18, cor, 1.0, 8)
    q = ep(t, tb, 0.3)
    if q > 0:
        k = ease_back(prog(t, tb, 0.45))
        c.drawCircle(X, y, r * k, M.paint(cor if fecha else E.PAPEL, q))
        c.drawCircle(X, y, r * k, M.paint(cor, q, stroke=6))


def resumo(c, t, C, k0, itens, y0=430, dy=190, x=260, size=84):
    """'resumindo' e até três linhas numeradas: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[k0], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        item(c, t, C[k], i + 1, x, y)
        E.frase(c, t, C[k] + 0.1, partes, x + 100, y)


def proxima(c, t, C, k, l1, l2, sub, k_sub, k_insc, k_bons, size=120):
    """próxima aula, Inscreva-se com o cursor e bons estudos"""
    E.frase(c, t, C[k], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C[k] + 0.8, [(l1, "g", size, COR)], XE, 410)
    if l2:
        E.frase(c, t, C[k] + 1.1, [(l2, "g", size, COR)], XE, 540)
    if sub:
        E.frase(c, t, C[k_sub], sub, XE, 690 if l2 else 560)
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


def promessa(c, t, tb, te, linhas, extra=True):
    """tela do 'até o fim desta aula': linhas = [(instante, partes de E.frase)]; esfera com o atalho à direita"""
    if extra:
        E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
        E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                               E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 280)
    for i, (ti, partes) in enumerate(linhas):
        E.frase(c, t, ti, partes, XE, 440 + i * 150)


def lembrete(c, t, C, k0, itens, y0=430, dy=210):
    """'você precisa de N coisas' e os itens numerados: itens = [(cue, fn(a, y))]"""
    n = len(itens)
    nome = {1: "1", 2: "2", 3: "3"}[n]
    E.linha(c, t, [("você", "i", 84, TINTA, C[k0]), ("precisa", "i", 84, TINTA, C[k0] + 0.2), ("de", "i", 84, TINTA, C[k0] + 0.4),
                   (nome, "g", 90, COR, C[k0] + 0.6), ("coisa" if n == 1 else "coisas", "i", 84, TINTA, C[k0] + 0.8)], W / 2, 220, "center")
    for i, (k, fn) in enumerate(itens):
        y = y0 + i * dy
        item(c, t, C[k], i + 1, 300, y)
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


def questao_relogio(c, t, C, k, cx=1540, cy=640, r=150):
    if t >= C[k]:
        E.relogio(c, t, C[k + ".a"], cx=cx, cy=cy, r=r)


def por_partes(c, t, t0, linhas, x, y, size, xc, tl=None, tc=None, nome=None, dy=None, luz=None):
    """f(x) = { lei, condição }: nome = partes de fx antes da chave; linhas = [(lei, condição)]; xc = onde começa a condição,
    contado da chave; luz(i) = destaque da linha i (0..1). Devolve (y de cada linha, x da chave)"""
    dy = dy or size * 1.5
    n = len(linhas)
    xx = x
    if nome:
        w = fx(c, nome, 0, 0, size, 0)[0]
        fx_em(c, t, t0, nome, x, y + (n - 1) * dy / 2 + size * 0.0, size)
        xx = x + w + size * 0.55
    if luz:
        for i in range(n):
            q = luz(i)
            if q > 0:
                M.rrect(c, xx - 10, y + i * dy - size * 0.95, xc + size * 5.2, size * 1.3, 18, COR, 0.12 * q)
    ys = chave(c, t, t0, [l for l, _ in linhas], xx, y, size, dy, tl)
    tl = tl or [t0] * n
    tc = tc or tl
    for i, (_, cond) in enumerate(linhas):
        fx_em(c, t, tc[i] + 0.2, cond, xx + xc, ys[i], size * 0.82)
    return ys, xx


q2 = lambda x: x * x
q3 = lambda x: x ** 3
PP = (1000, 140, 820, 820, -3.2, 3.2, -1, 9.5)
PI = (1000, 120, 820, 860, -2.6, 2.6, -10, 10)


def dobra(c, t, t0, P, f, a, b, cor, d=1.4):
    """a metade [a, b] da curva dobra sobre o eixo y: cada x anda até −x"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    pts = [(lerp(x, -x, p), y) for x, y in amostra(f, a, b)]
    traco(c, P, pts, cor, 0.85 if p < 1 else 0.5, 9)


def gira(c, t, t0, P, f, a, b, cor, d=1.8):
    """cópia da curva girando meia volta em torno da origem (em pixels)"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    ang = math.pi * p
    ox, oy = P(0, 0)
    x, y, w, h = P.caixa
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - 6, y - 6, w + 12, h + 12), True)
    path = skia.Path()
    for i, (xv, yv) in enumerate(amostra(f, a, b)):
        X, Y = P(xv, yv)
        dx, dy = X - ox, Y - oy
        Xr, Yr = ox + dx * math.cos(ang) - dy * math.sin(ang), oy + dx * math.sin(ang) + dy * math.cos(ang)
        path.lineTo(Xr, Yr) if i else path.moveTo(Xr, Yr)
    c.drawPath(path, M.paint(cor, 0.85 if p < 1 else 0.5, stroke=9, cap_round=True))
    c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        fx_em(c, t, C["s01.a"], [("(−2)", ENT), ("^2", ENT), (" = 4", SAI)], 400, 330, 120)
        fx_em(c, t, C["s01.b"], [("2", ENT), ("^2", ENT), (" = 4", SAI)], 1100, 330, 120)
        E.foco(c, t, C["s01.b"] + 0.5, 0.4, lambda a: E.pilula(c, "igual", 1700, 290, 50, "g", fundo=CERTO, a=a))
        fx_em(c, t, C["s01.c"], [("(−2)", ENT), ("^3", ENT), (" = −8", SAI)], 400, 560, 120)
        fx_em(c, t, C["s01.d"], [("2", ENT), ("^3", ENT), (" = 8", SAI)], 1100, 560, 120)
        E.foco(c, t, C["s01.d"] + 0.5, 0.4, lambda a: E.pilula(c, "oposto", 1710, 520, 50, "g", fundo=COR, a=a))
        E.frase(c, t, C["s01.e"], [("funções", "i", 90), ("pares", "g", 96, COR), ("e", "i", 90), ("ímpares", "g", 96)], W / 2, 850, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02.a"], C["s02.end"], [(C["s02.a"] + 1.2, [("par", "g", 120, COR)]),
                                              (C["s02.a"] + 1.8, [("ímpar", "g", 120)]),
                                              (C["s02.b"], [("pela", "i", 100), ("simetria", "g", 110, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def i1(a, y):
        fx(c, [("(−2)", ENT), ("^2", ENT), (" = 4", SAI)], 430, y, 76, a)
        fx(c, [("(−2)", ENT), ("^3", ENT), (" = −8", SAI)], 880, y, 76, a)
        E.escreve(c, "par: positivo · ímpar: mantém o sinal", 430, y + 90, 54, "i", COR, a)

    def i2(a, y):
        E.escreve(c, "eixo de simetria:", 430, y, 66, "i", TINTA, a)
        E.escreve(c, "dobra e coincide", 940, y, 66, "g", COR, a)
        cx = 1640
        pa = skia.Path(); pa.addPoly([(cx - 120, y + 60), (cx, y - 120), (cx + 120, y + 60)], True)
        c.drawPath(pa, M.paint(COR, a * 0.15)); c.drawPath(pa, M.paint(COR, a, stroke=6))
        M.line(c, cx, y - 150, cx, y + 90, TINTA, a, 4, dash=E.TRACO)
    lembrete(c, t, C, "s03", [("s03.a", i1), ("s03.b", i2)], y0=450, dy=290)


# ---------------- o teste ----------------
def b_teste(c, t, C, b):
    E.frase(c, t, C["s04"], [("o", "i", 90), ("teste", "g", 96, COR), ("é", "i", 90), ("um", "i", 90), ("só", "i", 90)], W / 2, 230, "center")
    fx_em(c, t, C["s04.a"], [("x", ENT), ("   →   ", TINTA2), ("−x", ENT)], W / 2, 480, 140, "center")
    E.foco(c, t, C["s04.b"], 0.5, lambda a: (fx(c, [("f(", SAI), ("−x", ENT), (")", SAI)], 600, 760, 140, a, "center"),
                                             E.centro(c, "compare com", 960, 740, 56, "i", TINTA2, a),
                                             fx(c, [("f(", SAI), ("x", ENT), (")", SAI)], 1320, 760, 140, a, "center")))


# ---------------- par ----------------
def b_par(c, t, C, b):
    P = E.plano(c, t, C["s05"], *PP, marcas_x=[-2, -1, 1, 2], marcas_y=[1, 4, 9], size=38)
    E.curva(c, t, C["s05.a"] + 0.3, P, q2, -3.05, 3.05, d=1.0, cor=COR)

    def s05():
        fx_em(c, t, C["s05.a"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^2", ENT)], XE, 240, 100)
        fx_em(c, t, C["s05.b"], [("f(", SAI), ("−x", ENT), (") = (", SAI), ("−x", ENT), (")", SAI), ("^2", ENT), (" = ", SAI), ("x", ENT), ("^2", ENT)],
              XE, 400, 90)
        E.frase(c, t, C["s05.c"], [("voltou", "i", 76), ("igual", "g", 80, CERTO)], XE, 540)
        E.frase(c, t, C["s05.d"], [("função", "i", 110), ("par", "g", 130, COR)], XE, 720)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.ponto(c, t, C["s06.a"], P, 2, 4, "(2, 4)", cor=SAI)
    E.ponto(c, t, C["s06.a"] + 0.3, P, -2, 4, "(−2, 4)", cor=SAI, lado=(-1, -1))
    q = ep(t, C["s06.a"] + 0.5, 0.5)
    if q > 0:
        M.line(c, *P(-2, 4), *P(2, 4), TINTA2, q, 4, dash=E.TRACO)
    q = ep(t, C["s06.c"], 0.5)
    if q > 0:
        M.line(c, P.ox, P.caixa[1], P.ox, P.caixa[1] + P.caixa[3], COR, 0.2 * q, 30)
    dobra(c, t, C["s06.d"] + 0.3, P, q2, -3.05, 0, TINTA)
    E.frase(c, t, C["s06.a"], [("mesma", "i", 74), ("altura:", "i", 74), ("4", "g", 80, COR)], XE, 260)
    E.frase(c, t, C["s06.b"], ps("todo número e o seu oposto", "i", 60, TINTA2), XE, 380, passo=0.1)
    E.frase(c, t, C["s06.c"], [("eixo", "i", 76), ("y:", "g", 80), ("eixo", "i", 76), ("de", "i", 76), ("simetria", "g", 80, COR)], XE, 560)
    E.frase(c, t, C["s06.d"], [("dobre", "g", 80, COR), ("no", "i", 76), ("eixo", "i", 76), ("y:", "g", 80)], XE, 720)
    E.frase(c, t, C["s06.d"] + 0.8, ps("as metades se cobrem", "i", 66, TINTA2), XE, 820)


# ---------------- ímpar ----------------
def b_impar(c, t, C, b):
    P = E.plano(c, t, C["s07"], *PI, passo=1, passo_y=2, marcas_x=[-2, -1, 1, 2], marcas_y=[-8, 8], size=38)
    E.curva(c, t, C["s07.a"] + 0.3, P, q3, -2.3, 2.3, d=1.0, cor=COR)

    def s07():
        fx_em(c, t, C["s07.a"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^3", ENT)], XE, 240, 100)
        fx_em(c, t, C["s07.b"], [("f(", SAI), ("−x", ENT), (") = (", SAI), ("−x", ENT), (")", SAI), ("^3", ENT), (" = −", SAI), ("x", ENT), ("^3", ENT)],
              XE, 400, 90)
        E.frase(c, t, C["s07.c"], [("voltou", "i", 76), ("o", "i", 76), ("oposto", "g", 80, COR)], XE, 540)
        E.frase(c, t, C["s07.d"], [("função", "i", 110), ("ímpar", "g", 130, COR)], XE, 720)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.ponto(c, t, C["s08.a"], P, 2, 8, "(2, 8)", cor=SAI, lado=(-1, 0))
    E.ponto(c, t, C["s08.b"], P, -2, -8, "(−2, −8)", cor=SAI, lado=(1, 0))
    q = ep(t, C["s08.b"] + 0.4, 0.5)
    if q > 0:
        M.line(c, *P(-2, -8), *P(2, 8), TINTA2, q, 4, dash=E.TRACO)
        c.drawCircle(*P(0, 0), 12, M.paint(COR, q))
    gira(c, t, C["s08.c"] + 0.3, P, q3, -2.3, 2.3, TINTA)
    if t >= C["s08.c"]:
        p = ease_io(prog(t, C["s08.c"] + 0.3, 1.8))
        if p > 0:
            E.arco(c, *P(0, 0), 90, -90, 180 * p, COR, 6)
    E.frase(c, t, C["s08.a"], [("x = 2:", "g", 70), ("8", "g", 76, COR)], XE, 250)
    E.frase(c, t, C["s08.b"], [("x = −2:", "g", 70), ("−8", "g", 76, COR)], XE, 360)
    E.frase(c, t, C["s08.c"] - 1.6, ps("a dobra não funciona", "i", 60, ERRADO), XE, 480, passo=0.1)
    E.frase(c, t, C["s08.c"], [("meia", "g", 80, COR), ("volta", "g", 80, COR), ("na", "i", 76), ("origem", "i", 76)], XE, 620)
    E.frase(c, t, C["s08.d"], ps("cai em cima de si mesmo", "i", 60, TINTA2), XE, 730, passo=0.1)
    nota(c, t, C["s08.e"], "simetria em relação à origem", 560, 880, 48)


# ---------------- nenhuma ----------------
def b_nenhuma(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("nem", "i", 90), ("uma,", "i", 90), ("nem", "i", 90), ("outra", "g", 96, COR)], W / 2, 220, "center")
    fx_em(c, t, C["s09.b"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), (" + 1", SAI)], W / 2, 400, 110, "center")
    fx_em(c, t, C["s09.c"], [("f(", SAI), ("−x", ENT), (") = ", SAI), ("−x", ENT), (" + 1", SAI)], W / 2, 560, 110, "center")
    E.foco(c, t, C["s09.d"], 0.5, lambda a: (fx(c, [("≠  ", ERRADO), ("x + 1", SAI)], 560, 740, 90, a, "center"),
                                             E.centro(c, "não é igual", 560, 830, 52, "i", ERRADO, a)))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: (fx(c, [("≠  ", ERRADO), ("−x − 1", SAI)], 1360, 740, 90, a, "center"),
                                             E.centro(c, "nem o oposto", 1360, 830, 52, "i", ERRADO, a)))
    nota(c, t, C["s09.f"], "nem par, nem ímpar", W / 2, 960, 60, fundo=TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10.a"], [("cuidado:", "g", 84, ERRADO), ("olhar", "i", 80), ("só", "i", 80), ("o", "i", 80), ("expoente", "g", 84)], W / 2, 190, "center")
    fx_em(c, t, C["s10.b"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^3", ERRADO), (" + 1", SAI)], 560, 400, 110, "center")
    E.saida(c, t, C["s11.c"], lambda: nota(c, t, C["s10.b"] + 1.0, "expoente 3: ímpar?", 1340, 370, 52, fundo=ERRADO))
    fx_em(c, t, C["s11.a"], [("f(2) = 8 + 1 = ", SAI), ("9", COR)], 300, 600, 84)
    fx_em(c, t, C["s11.b"], [("f(−2) = −8 + 1 = ", SAI), ("−7", COR)], 300, 740, 84)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: (E.escreve(c, "oposto de 9:", 1150, 600, 60, "i", TINTA2, a),
                                             fx(c, [("−9 ≠ −7", ERRADO)], 1150, 720, 100, a), E.selo(c, 1640, 690, 40, False, a)))
    nota(c, t, C["s11.d"], "o + 1 estragou a simetria", W / 2, 920, 56)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("soma de potências de x:", "i", 74, CLARO), W / 2, 190, "center")
        linhas = (("s12.a", "só pares", "par", "x^4 + x^2 + 5", 390),
                  ("s12.b", "só ímpares, sem número sozinho", "ímpar", "x^3 + 2x", 600),
                  ("s12.c", "misturou", "nenhuma", "x^2 + x", 810))
        for k, txt, res, ex, y in linhas:
            E.foco(c, t, C[k], 0.5, lambda a, txt=txt, res=res, ex=ex, y=y: (
                E.escreve(c, txt, 200, y, 60, "i", CLARO, a), fx(c, [(ex, BR)], 200, y + 100, 76, a),
                E.pilula(c, res, 1560, y + 30, 70, "g", fundo=BR, cor="#07070F", a=a)))
        E.foco(c, t, C["s12.a"] + 2.0, 0.4, lambda a: E.escreve(c, "o número sozinho conta como par", 900, 490, 46, "i", CLARO, a))
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13.a"], 0.5, lambda a: (fx(c, [("(−x)", CLARO), ("^{par}", CLARO), ("  =  ", BR), ("x", BR), ("^{par}", BR)], W / 2, 330, 120, a, "center"),
                                             E.centro(c, "perde o sinal", W / 2, 420, 54, "i", CLARO, a)))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (fx(c, [("(−x)", CLARO), ("^{ímpar}", CLARO), ("  =  −", BR), ("x", BR), ("^{ímpar}", BR)], W / 2, 600, 120, a,
                                                "center"), E.centro(c, "mantém o sinal", W / 2, 690, 54, "i", CLARO, a)))
    nota(c, t, C["s13.c"], "só vale para soma de potências de x", W / 2, 840, 54, fundo=BR, cor="#07070F")
    nota(c, t, C["s13.d"], "outras leis: faça o teste do −x", W / 2, 970, 54, fundo=CLARO, cor="#07070F")


# ---------------- questão ----------------
QS = (("s14.a", [("f(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^3", ENT), (" − 4", SAI), ("x", ENT)], 460),
      ("s14.b", [("g(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^2", ENT), (" − 5", SAI)], 640),
      ("s14.c", [("h(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^2", ENT), (" + ", SAI), ("x", ENT)], 820))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14"] + 1.0, [("par,", "g", 64), ("ímpar", "g", 64), ("ou", "i", 60), ("nenhuma?", "g", 64, COR)], XE, 290)
    for k, pt, y in QS:
        fx_em(c, t, C[k], pt, XE, y, 110)
    questao_relogio(c, t, C, "s15")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    S = 84
    for (k, pt, _), y, kr, res, ok, kf in zip(QS, (290, 500, 680), ("s16.b", "s17.b", "s17.d"), ("ímpar", "par", "nenhuma"), (COR, COR, TINTA),
                                               ("s16.a", "s17.a", "s17.c")):
        fx_em(c, t, C[kf] - 0.3, pt, XE, y, S)
        E.foco(c, t, C[kr], 0.5, lambda a, res=res, y=y, ok=ok: E.pilula(c, res, 1540, y - 25, 64, "g", fundo=ok, a=a))
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.escreve(c, "expoentes 3 e 1", 860, 290, 54, "i", TINTA2, a))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: fx(c, [("f(−x) = −x", SAI), ("^3", SAI), (" + 4x = −f(x)", SAI)], XE + 60, 385, 60, a))
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.escreve(c, "2 e o −5: tudo par", 860, 500, 54, "i", TINTA2, a))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.escreve(c, "2 com 1: misturou", 860, 680, 54, "i", TINTA2, a))
    E.foco(c, t, C["s17.e"], 0.5, lambda a: (fx(c, [("h(1) = 2", SAI), ("     h(−1) = 0", SAI)], XE + 60, 800, 70, a),
                                             E.escreve(c, "nem igual, nem oposto", XE + 60, 900, 54, "i", COR, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.saida(c, t, C["s19"] - 0.1, lambda: resumo(c, t, C, "s18", [
        ("s18.a", [("troque", "i", 84), ("x", "g", 88), ("por", "i", 84), ("−x", "g", 88, COR)]),
        ("s18.b", [("igual:", "i", 84), ("par,", "g", 88, COR), ("espelho", "i", 84), ("no", "i", 84), ("eixo", "i", 84), ("y", "g", 88)]),
        ("s18.c", [("oposto:", "i", 84), ("ímpar,", "g", 88, COR), ("meia", "i", 84), ("volta", "i", 84)])]))
    if t < C["s19"]:
        return
    proxima(c, t, C, "s19.a", "praticando", "a trilha", [("módulo,", "i", 64), ("composta,", "i", 64), ("inversa", "i", 64), ("e", "i", 64),
                                                          ("paridade", "g", 70, COR)], "s19.b", "s19.c", "s19.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, teste=b_teste, par=b_par, impar=b_impar, nenhuma=b_nenhuma, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
