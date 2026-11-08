"""Visual — Estudativo · MAT-FAV-006: calcular a inversa e ver seu gráfico.

Linguagem visual da trilha Funções Avançadas (MAT-FAV-001 a 005): x e entrada em índigo (ENT), y e saída em preto (SAI). Nesta aula:
os três passos numerados com a fórmula embaixo de cada um; a inversa final numa pílula índigo; no plano (escala igual nos dois eixos),
f em preto, f⁻¹ em índigo e a diagonal y = x tracejada; a dobra leva cada ponto (a, b) de f até (b, a), como em MAT-EXP-013.
No atalho (palco), a corrente de operações ×2 e +3 desfeita de trás para frente: −3 e ÷2."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-006_calcular_a_inversa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "grafico", "atalho", "questao", "fim"))
BR = "#FFFFFF"

f = lambda x: 2 * x + 3
fi = lambda x: (x - 3) / 2
assert f(5) == 13 and fi(13) == 5 and (13 - 3) == 10 and 10 / 2 == 5
assert (f(0), f(1)) == (3, 5) and (fi(3), fi(5)) == (0, 1) and 2 * 13 + 3 == 29
assert all(fi(f(x)) == x for x in range(-5, 6))
g = lambda x: 4 * x - 1
gi = lambda x: (x + 1) / 4
assert gi(7) == 2 and g(2) == 7 and all(gi(g(x)) == x for x in range(-5, 6))

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


FINV = [("f", SAI), ("^{−1}", COR), ("(", SAI), ("x", ENT), (")", SAI)]


def passo_(c, t, t0, n, txt, y, x=230):
    item(c, t, t0, n, x, y, 44)
    E.frase(c, t, t0 + 0.1, ps(txt, "i", 60), x + 70, y)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        fx_em(c, t, C["s01.a"], [("f(", SAI), ("x", ENT), (") = 2", SAI), ("x", ENT), (" + 3", SAI)], W / 2, 230, 120, "center")
        Y = 540
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (E.pilula(c, "5", 560, Y, 90, "g", fundo=ENT, a=a),
                                                 E.pilula(c, "13", 1360, Y, 90, "g", fundo=SAI, a=a)))
        p = ep(t, C["s01.b"] + 0.4, 0.6)
        if p > 0:
            M.arrow(c, 680, Y - 50, lerp(680, 1230, p), Y - 50, COR, 1.0, 6, 22, p)
            E.centro(c, "f", 955, Y - 80, 64, "g", COR, p)
        p = ep(t, C["s01.c"], 0.6)
        if p > 0:
            M.arrow(c, 1230, Y + 50, lerp(1230, 680, p), Y + 50, TINTA2, 1.0, 6, 22, p)
            E.centro(c, "?", 955, Y + 130, 80, "g", TINTA2, p)
        E.frase(c, t, C["s01.c"], [("saiu", "i", 70), ("13:", "g", 72), ("qual", "i", 70), ("foi", "i", 70), ("a", "i", 70), ("entrada?", "g", 72, COR)],
                W / 2, 800, "center")
        nota(c, t, C["s01.d"], "a função inversa", W / 2, 950, 64)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02.a"], C["s02.end"], [(C["s02.a"] + 1.2, [("calcular", "g", 110, COR)]),
                                              (C["s02.a"] + 1.8, [("a", "i", 100), ("inversa", "g", 110, COR)]),
                                              (C["s02.b"], [("o", "i", 100), ("gráfico", "g", 110)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def i1(a, y):
        E.escreve(c, "só a", 430, y, 70, "i", TINTA, a)
        E.escreve(c, "bijetora", 600, y, 76, "g", COR, a)
        E.escreve(c, "tem inversa", 940, y, 70, "i", TINTA, a)

    def i2(a, y):
        fx(c, [("v = f{d}{t}", SAI), ("   →   ", TINTA2), ("d = v · t", COR)], 430, y + 10, 80, a)

    def i3(a, y):
        E.formula(c, "log", 430, y, 84, "g", SAI, a)
        E.formula(c, "2", 430 + E.formula(None, "log", 0, 0, 84, "g", a=0) + 4, y + 18, 48, "g", SAI, a)
        E.formula(c, "x", 580, y, 84, "g", ENT, a)
        E.escreve(c, "é o espelho de", 680, y, 66, "i", TINTA2, a)
        fx(c, [("2", SAI), ("^x", ENT)], 1110, y, 84, a)
    lembrete(c, t, C, "s03", [("s03.a", i1), ("s03.b", i2), ("s03.c", i3)])


# ---------------- método ----------------
def b_metodo(c, t, C, b):
    if t < C["s05"]:
        fx_em(c, t, C["s04.a"], FINV, W / 2, 470, 220, "center")
        q = ep(t, C["s04.b"], 0.4)
        if q > 0:
            w, xs, ws = fx(c, FINV, W / 2, 470, 220, 0, "center")
            c.drawCircle(xs[1] + ws[1] / 2, 470 - 220 * 0.55, 70, M.paint(COR, q, stroke=6))
        nota(c, t, C["s04.b"], "não é expoente: é o nome da inversa", W / 2, 700, 56)
        E.frase(c, t, C["s04.c"], [("3", "g", 110, COR), ("passos", "i", 100)], W / 2, 920, "center")
        return
    fx_em(c, t, C["s05"], [("f(", SAI), ("x", ENT), (") = 2", SAI), ("x", ENT), (" + 3", SAI)], 230, 170, 84)
    S = 84

    def esquerda():
        passo_(c, t, C["s05.a"], 1, "troque f(x) por y", 300)
        fx_em(c, t, C["s05.b"], [("y", SAI), (" = 2", SAI), ("x", ENT), (" + 3", SAI)], 300, 400, S)
        passo_(c, t, C["s06.a"], 2, "troque as letras", 530)
        fx_em(c, t, C["s06.b"], [("x", ENT), (" = 2", SAI), ("y", SAI), (" + 3", SAI)], 300, 630, S)
        E.foco(c, t, C["s06.b"] + 1.0, 0.4, lambda a: E.escreve(c, "a entrada vira saída", 800, 625, 52, "i", COR, a))
        passo_(c, t, C["s07.a"], 3, "isole o y", 760)
        fx_em(c, t, C["s07.b"], [("x − 3 = 2", SAI), ("y", SAI)], 300, 860, S)
        nota(c, t, C["s07.b"], "− 3 nos dois lados", 925, 830, 36, fundo=TINTA)
        fx_em(c, t, C["s07.c"], [("y = ", SAI), ("f{x − 3}{2}", SAI)], 300, 990, S)
        nota(c, t, C["s07.c"], "÷ 2", 760, 970, 40, fundo=TINTA)
    esquerda()
    # a inversa final e a conferência, à direita
    E.foco(c, t, C["s07.d"], 0.5, lambda a: (M.rrect(c, 1180, 300, 640, 260, 40, COR, a),
                                             fx(c, [("f", BR), ("^{−1}", BR), ("(x) = ", BR), ("f{x − 3}{2}", BR)], 1500, 455, 96, a, "center")))
    fx_em(c, t, C["s08.a"], [("f(5) = 13", SAI)], 1500, 680, 76, "center")
    fx_em(c, t, C["s08.b"], [("f", SAI), ("^{−1}", COR), ("(13) = ", SAI), ("f{13 − 3}{2}", SAI), (" = ", SAI), ("f{10}{2}", SAI), (" = ", SAI), ("5", COR)],
          1500, 840, 70, "center")
    E.foco(c, t, C["s08.c"], 0.5, lambda a: (E.escreve(c, "voltou para o 5", 1300, 990, 60, "g", CERTO, a), E.selo(c, 1780, 970, 36, True, a)))


# ---------------- gráfico ----------------
PG = (1060, 150, 780, 780, -2, 8, -2, 8)
US = [-2.5 + 5.0 * i / 200 for i in range(201)]  # x de f de −2,5 a 2,5 (y de −2 a 8)
PF = [(u, f(u)) for u in US]


def b_grafico(c, t, C, b):
    P = E.plano(c, t, C["s09"], *PG, marcas_x=[2, 4, 6], marcas_y=[2, 4, 6], size=38)
    # f em preto
    E.curva(c, t, C["s09.b"] + 0.3, P, f, -2.5, 2.5, d=0.8, cor=SAI)
    E.foco(c, t, C["s09.b"] + 1.0, 0.4, lambda a: fx(c, [("f", SAI)], P.x(2.4) - 30, P.y(7.4), 60, a, "right"))
    for k, (x, y) in (("s09.a", (0, 3)), ("s09.b", (1, 5))):
        E.ponto(c, t, C[k], P, x, y, f"({x}, {y})", cor=SAI, lado=(1, 0))
    # pontos trocados
    for k, (x, y) in (("s09.c", (3, 0)), ("s09.d", (5, 1))):
        E.ponto(c, t, C[k], P, x, y, f"({x}, {y})", cor=COR, lado=(-1, -1) if y == 0 else (0, 1))
        if t >= C[k]:
            q = ep(t, C[k], 0.6) * (1 - ep(t, C["s10"], 0.5))
            if q > 0:
                M.line(c, *P(y, x), *P(x, y), TINTA2, q * 0.8, 4, dash=E.TRACO)
    # diagonal e dobra
    E.curva(c, t, C["s10.a"], P, lambda x: x, -2, 8, d=0.8, cor=TINTA2, largura=5, tracejada=True)
    E.foco(c, t, C["s10.a"] + 0.8, 0.4, lambda a: fx(c, [("y = x", TINTA2)], P.x(6.9), P.y(7.6), 46, a, "center"))
    tb = C["s10.b"]
    p = ease_io(prog(t, tb, 1.6))
    if 0 < p < 1:
        traco(c, P, [(lerp(a_, b_, p), lerp(b_, a_, p)) for a_, b_ in PF], COR, 0.85)
    if p >= 1:
        traco(c, P, [(b_, a_) for a_, b_ in PF], COR)
        E.foco(c, t, tb + 1.6, 0.4, lambda a: fx(c, [("f", COR), ("^{−1}", COR)], P.x(7.4), P.y(2.9), 60, a, "center"))

    # texto à esquerda
    def s09():
        E.frase(c, t, C["s09"], [("e", "i", 72), ("o", "i", 72), ("gráfico?", "g", 76, COR)], XE, 230)
        E.frase(c, t, C["s09.c"] - 1.6, ps("cada par troca de ordem", "i", 60, TINTA2), XE, 360, passo=0.1)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: fx(c, [("(0, 3)  →  ", SAI), ("(3, 0)", COR)], XE, 500, 72, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: fx(c, [("(1, 5)  →  ", SAI), ("(5, 1)", COR)], XE, 620, 72, a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("espelho", "g", 90, COR), ("na", "i", 84), ("diagonal", "g", 90)], XE, 250)
    fx_em(c, t, C["s10.a"] + 0.8, [("y = x", TINTA)], XE, 370, 84)
    E.frase(c, t, tb, [("dobre", "g", 80, COR), ("o", "i", 76), ("papel", "i", 76)], XE, 500)

    def mini(a):
        Q = E.Plano(XE, 560, 380, 300, -2.5, 4, -2.5, 4)
        M.line(c, Q.x(-2.5), Q.y(0), Q.x(4), Q.y(0), TINTA2, a * 0.5, 3)
        M.line(c, Q.x(0), Q.y(-2.5), Q.x(0), Q.y(4), TINTA2, a * 0.5, 3)
        traco(c, Q, amostra(lambda x: 2 ** x, -2.5, 2.0), SAI, a, 6)
        traco(c, Q, amostra(lambda x: math.log2(x), 0.18, 4), COR, a, 6)
        traco(c, Q, [(-2.5, -2.5), (4, 4)], TINTA2, a * 0.6, 3, E.TRACO)
        fx(c, [("2", SAI), ("^x", ENT)], Q.x(1.0) - 10, Q.y(3.4), 46, a, "right")
        E.formula(c, "log", Q.x(2.6), Q.y(1.9), 40, "g", COR, a)
        E.formula(c, "2", Q.x(2.6) + 64, Q.y(1.9) + 10, 24, "g", COR, a)
    E.foco(c, t, C["s10.c"], 0.5, mini)
    nota(c, t, C["s10.d"], "o log é a inversa da exponencial", 560, 940, 42)
    nota(c, t, C["s11.a"], "domínio de uma = imagem da outra", 560, 1020, 42, fundo=TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("cuidado:", "g", 84, ERRADO), ("o", "i", 80), ("−1", "g", 84), ("não", "i", 80), ("é", "i", 80), ("expoente", "g", 84)],
            W / 2, 190, "center")
    fx_em(c, t, C["s12.b"], [("f", SAI), ("^{−1}", ERRADO), ("(x) = ", SAI), ("f{1}{2x + 3}", ERRADO)], W / 2, 420, 120, "center")
    if t >= C["s12.b"] + 1.2:
        E.risco(c, 640, 470, 1300, 330, t, C["s12.b"] + 1.2, largura=14)
    fx_em(c, t, C["s12.c"], [("13  →  ", SAI), ("f{1}{29}", ERRADO), ("   e não ", TINTA2), ("5", COR)], W / 2, 680, 100, "center")
    nota(c, t, C["s12.d"], "a inversa desfaz a função: não é 1 dividido por ela", W / 2, 900, 50)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def corrente(y, ops, t0s, cores, sentido=1, x0=360, passo=430):
        """x → op1 → op2 → resultado; sentido −1 desenha da direita para a esquerda"""
        for i, (op, ti, cor) in enumerate(zip(ops, t0s, cores)):
            q = ep(t, ti, 0.5)
            if q <= 0:
                continue
            xa = x0 + i * passo if sentido > 0 else x0 + (len(ops) - i) * passo
            xb = xa + passo * sentido
            M.arrow(c, xa + 70 * sentido, y, lerp(xa + 70 * sentido, xb - 70 * sentido, q), y, cor, 1.0, 7, 24, q)
            E.pilula(c, op, (xa + xb) / 2, y - 70, 54, "g", fundo=cor, cor="#07070F", a=q)

    def s13():
        E.frase(c, t, C["s13.a"], [("desfaça", "g", 96, BR), ("de", "i", 90, CLARO), ("trás", "i", 90, CLARO), ("para", "i", 90, CLARO),
                                   ("frente", "g", 96, BR)], W / 2, 200, "center")
        y1, y2 = 470, 720
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.centro(c, "x", 360, y1 + 30, 90, "g", CLARO, a))
        corrente(y1, ("× 2", "+ 3"), (C["s13.b"], C["s13.b"] + 0.9), (CLARO, CLARO))
        E.foco(c, t, C["s13.b"] + 1.4, 0.4, lambda a: E.centro(c, "y", 360 + 2 * 430, y1 + 30, 90, "g", BR, a))
        corrente(y2, ("− 3", "÷ 2"), (C["s13.c"], C["s13.d"]), (BR, BR), sentido=-1)
        E.foco(c, t, C["s13.c"] - 0.2, 0.4, lambda a: E.centro(c, "x", 360 + 2 * 430, y2 + 30, 90, "g", BR, a))
        E.foco(c, t, C["s13.e"], 0.5, lambda a: fx(c, [("f", BR), ("^{−1}", CLARO), ("(x) = ", BR), ("f{x − 3}{2}", BR)], 1600, 760, 90, a, "center"))
        E.foco(c, t, C["s13.d"] + 0.4, 0.4, lambda a: E.centro(c, "?", 360, y2 + 30, 90, "g", BR, a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.foco(c, t, C["s14.a"], 0.5, lambda a: (E.escreve(c, "põe:", 300, 330, 80, "i", CLARO, a),
                                             E.escreve(c, "meia → sapato", 520, 330, 90, "g", BR, a)))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "tira:", 300, 500, 80, "i", CLARO, a),
                                             E.escreve(c, "sapato → meia", 520, 500, 90, "g", BR, a)))
    nota(c, t, C["s14.c"], "x aparece uma vez só: atalho", W / 2, 720, 56, fundo=BR, cor="#07070F")
    nota(c, t, C["s14.d"], "x em dois lugares: os três passos", W / 2, 860, 56, fundo=CLARO, cor="#07070F")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    fx_em(c, t, C["s15.a"], [("f(", SAI), ("x", ENT), (") = 4", SAI), ("x", ENT), (" − 1", SAI)], XE, 440, 130)
    E.frase(c, t, C["s15.b"], [("ache", "i", 80), ("a", "i", 80), ("inversa", "g", 84, COR)], XE, 660)
    fx_em(c, t, C["s15.c"], [("f", SAI), ("^{−1}", COR), ("(7) = ?", SAI)], XE, 860, 110)
    questao_relogio(c, t, C, "s16")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    S = 80
    rows = (("s17.a", [("y = 4", SAI), ("x", ENT), (" − 1", SAI)], 260),
            ("s17.b", [("x", ENT), (" = 4", SAI), ("y", SAI), (" − 1", SAI)], 420),
            ("s17.c", [("x + 1 = 4", SAI), ("y", SAI)], 580),
            ("s17.d", [("y = ", SAI), ("f{x + 1}{4}", COR)], 760))
    for i, (k, pt, y) in enumerate(rows):
        if i < 3:
            item(c, t, C[k], i + 1, 230, y, 40)
        fx_em(c, t, C[k], pt, 300, y, S)
    E.foco(c, t, C["s18.a"], 0.5, lambda a: (E.escreve(c, "f: × 4, − 1", 1100, 300, 66, "g", TINTA, a),
                                             E.escreve(c, "inversa: + 1, ÷ 4", 1100, 400, 66, "g", COR, a)))
    fx_em(c, t, C["s18.b"], [("f", SAI), ("^{−1}", COR), ("(7) = ", SAI), ("f{7 + 1}{4}", SAI), (" = ", SAI), ("f{8}{4}", SAI), (" = ", SAI), ("2", COR)],
          1100, 620, 76)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: (fx(c, [("f(2) = 4 · 2 − 1 = 7", CERTO)], 1100, 820, 70, a), E.selo(c, 1780, 795, 36, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.saida(c, t, C["s20"] - 0.1, lambda: resumo(c, t, C, "s19", [
        ("s19.a", [("troque", "i", 84), ("as", "i", 84), ("letras,", "g", 88, COR), ("isole", "i", 84), ("o", "i", 84), ("y", "g", 88)]),
        ("s19.b", [("desfaça", "g", 88, COR), ("de", "i", 84), ("trás", "i", 84), ("para", "i", 84), ("frente", "i", 84)]),
        ("s19.c", [("espelho", "g", 88, COR), ("na", "i", 84), ("diagonal", "i", 84)])]))
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20.a", "função par", "e ímpar", [("pela", "i", 70), ("simetria", "g", 76, COR), ("do", "i", 70), ("gráfico", "i", 70)],
            "s20.b", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, grafico=b_grafico, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
