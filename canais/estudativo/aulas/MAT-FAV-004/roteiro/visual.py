"""Visual — Estudativo · MAT-FAV-004: função composta.

Linguagem visual da trilha Funções Avançadas (MAT-FAV-001 a 003): x e entrada em índigo (ENT), saída em preto (SAI). Nesta aula:
cada função é uma máquina (maquina(): caixa índigo para f, preta para g, com a letra e o que ela faz); a composta é a fila de máquinas,
com o número entrando na primeira, saindo e entrando na segunda (fila()). A fórmula f(g(x)) ganha caixa na parte de dentro (1º) e na
de fora (2º). No caminho de volta, o de dentro vira "u" numa caixa pontilhada. Erro em vermelho, certo em verde. Palco no atalho."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-004_funcao_composta.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("maquinas", "lei", "volta", "atalho", "questao", "fim"))
BR = "#FFFFFF"

f = lambda x: 2 * x + 1
g = lambda x: x * x
assert f(g(3)) == 19 and g(f(3)) == 49 and f(3) * g(3) == 63 and 36 + 12 + 1 == 49
assert all(f(2 * x + 1) == 4 * x + 3 and (2 * x + 1) ** 2 == 4 * x * x + 4 * x + 1 for x in range(-5, 6))
assert 4 * 2 + 3 == 11 == f(5)
f2, g2 = (lambda x: x - 4), (lambda x: 3 * x)
assert f2(g2(2)) == 2 and g2(f2(2)) == -6

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


LEIS = dict(f=("2x + 1", COR), g=("x^2", TINTA))


def maquina(c, cx, cy, nome, a=1.0, w=300, h=200, lei=True):
    """máquina: caixa com a letra e a lei embaixo"""
    if a <= 0:
        return
    cor = LEIS[nome][1]
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 28, cor, a)
    for dy in (-h * 0.18, h * 0.18):  # funil de entrada e de saída
        M.line(c, cx - w / 2 - 26, cy + dy, cx - w / 2, cy + dy, cor, a, 6)
        M.line(c, cx + w / 2, cy + dy, cx + w / 2 + 26, cy + dy, cor, a, 6)
    centro(c, nome, cx, cy + (h * 0.02 if lei else h * 0.18), h * (0.42 if lei else 0.6), "g", BR, a)
    if lei:
        fx(c, [(LEIS[nome][0], BR)], cx, cy + h * 0.36, h * 0.2, a, "center")


def numero(c, s, cx, cy, a=1.0, cor=None, size=72):
    if a <= 0:
        return
    w = max(E.larg(s, "g", size) + size * 0.8, size * 1.5)
    M.rrect(c, cx - w / 2, cy - size * 0.75, w, size * 1.5, size * 0.75, E.PAPEL, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size * 0.75, w, size * 1.5), size * 0.75, size * 0.75),
                M.paint(cor or ENT, a, stroke=5))
    centro(c, s, cx, cy + size * 0.36, size, "g", cor or ENT, a)


def fila(c, t, y, ordem, vals, tv, x0=260, x1=1660, mw=260, mh=170, size=64, cor_fim=None):
    """entrada → máquina 1 → meio → máquina 2 → saída. vals = (entrada, meio, saída); tv = (máquinas, entrada, meio, saída)"""
    xs = [x0, lerp(x0, x1, 0.3), W / 2 if (x0 + x1) / 2 == W / 2 else (x0 + x1) / 2, lerp(x0, x1, 0.7), x1]
    am = ep(t, tv[0], 0.5)
    maquina(c, xs[1], y, ordem[0], am, mw, mh)
    maquina(c, xs[3], y, ordem[1], am, mw, mh)
    for i, (xa, xb) in enumerate(((xs[0], xs[1]), (xs[1], xs[2]), (xs[2], xs[3]), (xs[3], xs[4]))):
        p = ep(t, tv[1 + (i + 1) // 2] if i else tv[1], 0.4)
        ga = 70 if i % 2 == 0 else mw / 2 + 30
        gb = mw / 2 + 30 if i % 2 == 0 else 70
        if p > 0:
            M.arrow(c, xa + ga, y, xb - gb, y, TINTA2, p * 0.8, 5, 16, p)
    for j, (s, ti) in enumerate(zip(vals, tv[1:])):
        if ti is not None:
            cor = cor_fim if (j == 2 and cor_fim) else (ENT if j == 0 else SAI)
            E.foco(c, t, ti, 0.4, lambda a, s=s, j=j, cor=cor: numero(c, s, xs[2 * j], y, a, cor, size), sobe=6)
    return xs


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        fx_em(c, t, C["s01.a"], [("f(", SAI), ("x", ENT), (") = 2", SAI), ("x", ENT), (" + 1", SAI)], XE, 220, 96)
        fx_em(c, t, C["s01.b"], [("g(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^2", ENT)], 1100, 220, 96)
        fila(c, t, 520, "gf", ("3", "9", "19"), (C["s01.c"] - 1.6, C["s01.c"] - 1.6, C["s01.c"] - 0.8, C["s01.c"]), cor_fim=COR)
        fila(c, t, 820, "fg", ("3", "7", "49"), (C["s01.d"] - 0.9, C["s01.d"] - 0.9, C["s01.d"] - 0.5, C["s01.d"]), cor_fim=TINTA)
        nota(c, t, C["s01.d"] + 1.2, "a ordem muda tudo", W / 2, 990, 52)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02.a"], C["s02.end"], [(C["s02.a"] + 1.2, [("calcular", "g", 110, COR)]),
                                              (C["s02.b"], [("a", "i", 100), ("lei", "g", 110, COR)]),
                                              (C["s02.c"], [("a", "i", 100), ("função", "g", 110), ("escondida", "g", 110, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def i1(a, y):
        fx(c, [("f(", SAI), ("2", ENT), (")", SAI)], 430, y, 90, a)
        E.escreve(c, "troque o x pelo 2", 720, y, 62, "i", TINTA2, a)

    def i2(a, y):
        fx(c, [("(a + b)^2 = a^2 + 2ab + b^2", SAI)], 430, y, 80, a)

    def i3(a, y):
        fx(c, [("v = f{d}{t}", SAI), ("   →   ", TINTA2), ("d = v · t", COR)], 430, y + 10, 80, a)
    lembrete(c, t, C, "s03", [("s03.a", i1), ("s03.b", i2), ("s03.c", i3)])


# ---------------- máquinas ----------------
MY = 470


def b_maquinas(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("cada", "i", 80), ("função", "i", 80), ("é", "i", 80), ("uma", "i", 80), ("máquina", "g", 84, COR)], W / 2, 200,
                "center")
        E.foco(c, t, C["s04.b"], 0.5, lambda a: (maquina(c, 660, MY, "f", a, 380, 250),
                                                 E.centro(c, "dobra e soma 1", 660, MY + 230, 60, "i", TINTA, a)))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: (maquina(c, 1260, MY, "g", a, 380, 250),
                                                 E.centro(c, "eleva ao quadrado", 1260, MY + 230, 60, "i", TINTA, a)))
        E.foco(c, t, C["s04.a"] + 0.6, 0.4, lambda a: (numero(c, "entra", 300, MY, a, ENT, 46), numero(c, "sai", 1640, MY, a, SAI, 46)))
        return
    # topo: a fórmula
    if t < C["s07"]:
        S, Y = 110, 200
        partes = [("f(", SAI), ("g(", TINTA), ("x", ENT), (")", TINTA), (")", SAI)]
        w, xs, ws = fx(c, partes, W / 2, Y, S, 0, "center")
        fx_em(c, t, C["s05.c"], partes, W / 2, Y, S, "center")
        q = ep(t, C["s05.d"], 0.4)
        caixa(c, xs[1], Y, xs[3] + ws[3] - xs[1], S, q, TINTA)
        if q > 0:
            E.centro(c, "1º", xs[2], Y + 90, 44, "g", TINTA, q)
            E.centro(c, "2º", xs[0] - 20, Y + 90, 44, "g", COR, ep(t, C["s05.d"] + 0.6, 0.4))
        E.saida(c, t, C["s06"] - 0.1, lambda: (E.frase(c, t, C["s05.a"], ps("as máquinas em fila", "i", 64, TINTA2), W / 2, 700, "center"),
                                               nota(c, t, C["s05.b"], "a saída da primeira entra na segunda", W / 2, 820, 50)))
        if t < C["s06"]:
            fila(c, t, MY, "gf", ("x", "g(x)", "f(g(x))"), (C["s05"], C["s05.a"], C["s05.b"], C["s05.b"] + 0.4))
        else:
            fila(c, t, MY, "gf", ("3", "9", "19"), (C["s06"], C["s06.a"], C["s06.b"], C["s06.c"]), cor_fim=COR)
            fx_em(c, t, C["s06.b"], [("g(3) = 3", SAI), ("^2", SAI), (" = 9", COR)], 520, 800, 84, "center")
            fx_em(c, t, C["s06.c"], [("f(9) = 2 · 9 + 1 = 19", SAI)], 1380, 800, 84, "center")
        return
    if t < C["s08"]:
        S, Y = 110, 200
        fx_em(c, t, C["s07.a"], [("g(", TINTA), ("f(", SAI), ("x", ENT), (")", SAI), (")", TINTA)], W / 2, Y, S, "center")
        fila(c, t, MY, "fg", ("3", "7", "49"), (C["s07"], C["s07.a"], C["s07.b"], C["s07.c"]), cor_fim=COR)
        fx_em(c, t, C["s07.b"], [("f(3) = 2 · 3 + 1 = 7", SAI)], 520, 800, 84, "center")
        fx_em(c, t, C["s07.c"], [("g(7) = 7", SAI), ("^2", SAI), (" = 49", SAI)], 1380, 800, 84, "center")
        nota(c, t, C["s07.d"], "19 ≠ 49: a ordem importa", W / 2, 960, 54, fundo=ERRADO)
        return
    fx_em(c, t, C["s08.a"], [("(f ∘ g)(", SAI), ("x", ENT), (")", SAI)], 960, 450, 130, "right")
    fx_em(c, t, C["s08.a"] + 0.8, [(" = f(g(", SAI), ("x", ENT), ("))", SAI)], 960, 450, 130)
    E.frase(c, t, C["s08.a"], [("nas", "i", 72), ("provas:", "i", 72), ("f", "g", 76), ("bola", "g", 76, COR), ("g", "g", 76)], W / 2, 230, "center")
    nota(c, t, C["s08.b"], "a bolinha: faça o g primeiro", W / 2, 700, 56)


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    S = 96
    partes = [("f(", SAI), ("x", ENT), (") = 2 ", SAI), ("x", ENT), (" + 1", SAI)]
    w, xs, ws = fx(c, partes, XE, 0, S, 0)
    fx_em(c, t, C["s09.b"] - 0.6, partes, XE, 300, S)
    caixa(c, xs[3], 300, ws[3], S, ep(t, C["s09.b"], 0.4))
    E.frase(c, t, C["s09.a"], ps("troque o x do f pelo g(x) inteiro", "i", 60, TINTA2), XE, 170, passo=0.12)
    nota(c, t, C["s09.c"], "x  →  x²", 1300, 270, 54)
    partes2 = [("f(g(", SAI), ("x", ENT), (")) = 2 ", SAI), ("x^2", COR), (" + 1", SAI)]
    w2, xs2, ws2 = fx(c, partes2, XE, 0, S, 0)
    fx_em(c, t, C["s09.d"], partes2, XE, 470, S)
    caixa(c, xs2[3], 470, ws2[3], S, ep(t, C["s09.d"] + 0.5, 0.4))
    fx_em(c, t, C["s09.e"], [("com o 3:  2 · 9 + 1 = ", TINTA2), ("19", COR)], 1000, 470, 64)
    fx_em(c, t, C["s10.a"], [("g(f(", SAI), ("x", ENT), (")) = (2", SAI), ("x", ENT), (" + 1)", SAI), ("^2", COR)], XE, 680, S)
    fx_em(c, t, C["s10.b"], [("= 4", SAI), ("x", ENT), ("^2", ENT), (" + 4", SAI), ("x", ENT), (" + 1", SAI)], XE + 300, 820, S)
    fx_em(c, t, C["s10.c"], [("com o 3:  36 + 12 + 1 = ", TINTA2), ("49", COR)], XE + 300, 960, 64)


# ---------------- caminho de volta ----------------
def b_volta(c, t, C, b):
    S, Y = 110, 230
    partes = [("f(", SAI), ("2x + 1", ENT), (") = 4", SAI), ("x", ENT), (" + 3", SAI)]
    w, xs, ws = fx(c, partes, XE, Y, S, 0)
    fx_em(c, t, C["s11.a"], partes, XE, Y, S)
    p = ep(t, C["s12.a"], 0.5)
    if p > 0:
        E.caixa_pontilhada(c, xs[1] - 14, Y - S * 0.88, ws[1] + 28, S * 1.18, p, COR, p)
        E.centro(c, "u", xs[1] + ws[1] / 2, Y + 90, 70, "g", COR, p)

    def pergunta():
        fx_em(c, t, C["s11.b"], [("f(", SAI), ("x", ENT), (") = ?", COR)], 1300, Y, S)
    E.saida(c, t, C["s12"] - 0.1, pergunta)
    if t < C["s12"]:
        return
    L = 72
    rows = (("s12.b", [("x = ", ENT), ("f{u − 1}{2}", SAI)], 420),
            ("s12.c", [("f(u) = 4 · ", SAI), ("f{u − 1}{2}", SAI), (" + 3", SAI)], 560),
            ("s12.d", [("= 2 · (u − 1) + 3", SAI)], 700),
            ("s12.e", [("= 2u − 2 + 3 = ", SAI), ("2u + 1", COR)], 840))
    for k, pt, y in rows:
        xo = XE + (180 if k in ("s12.d", "s12.e") else 0)
        E.foco(c, t, C[k], 0.5, lambda a, pt=pt, y=y, xo=xo: fx(c, pt, xo, y, L, a))
    E.saida(c, t, C["s13"] - 0.1, lambda: nota(c, t, C["s12.a"] + 0.4, "2x + 1 = u", 1300, 400, 50, fundo=TINTA))
    E.saida(c, t, C["s13"] - 0.1, lambda: nota(c, t, C["s12.d"] - 0.3, "4 ÷ 2 = 2", 1300, 680, 46, fundo=TINTA))
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13.a"], 0.5, lambda a: fx(c, [("f(u) = 2u + 1", SAI)], 1400, 470, 76, a, "center"))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (E.pilula(c, "f(x) = 2x + 1", 1400, 620, 80, "g", fundo=CERTO, a=a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (fx(c, [("2(2", SAI), ("x", ENT), (" + 1) + 1 = 4", SAI), ("x", ENT), (" + 3", SAI)], 1400, 820, 60, a,
                                                "center"), E.selo(c, 1400, 920, 40, True, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14.a"], [("cuidado:", "g", 84, ERRADO), ("não", "i", 80), ("é", "i", 80), ("multiplicar", "g", 84)], W / 2, 180, "center")
    certo = C["s15"]
    E.saida(c, t, certo + 0.6, lambda: (
        fx_em(c, t, C["s14.b"], [("f(g(", SAI), ("x", ENT), (")) ≠ f(", SAI), ("x", ENT), (") · g(", SAI), ("x", ENT), (")", SAI)], W / 2, 380, 100,
              "center"),
        fx_em(c, t, C["s14.c"], [("7 · 9 = 63", ERRADO)], W / 2, 560, 120, "center"),
        t >= C["s14.c"] + 0.9 and E.risco(c, 700, 590, 1220, 470, t, C["s14.c"] + 0.9, largura=14)))
    if t < certo:
        return
    E.frase(c, t, C["s15.a"], [("a", "i", 80), ("composta", "g", 84, COR), ("encadeia", "i", 80)], W / 2, 360, "center")
    fila(c, t, 620, "gf", ("3", "9", "19"), (C["s15.b"] - 0.4, C["s15.b"] - 0.2, C["s15.b"] + 0.4, C["s15.c"]), cor_fim=CERTO)
    E.foco(c, t, C["s15.c"] + 0.3, 0.4, lambda a: E.selo(c, 1660, 760, 40, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        E.frase(c, t, C["s16.a"], [("só", "i", 84, CLARO), ("um", "i", 84, CLARO), ("valor:", "i", 84, CLARO)], W / 2, 200, "center")
        fx_em(c, t, C["s16.a"] + 0.6, [("f(5) = ?", BR)], W / 2, 330, 110, "center")
        S, Y = 110, 540
        partes = [("f(", BR), ("2x + 1", CLARO), (") = 4", BR), ("x", CLARO), (" + 3", BR)]
        w, xs, ws = fx(c, partes, W / 2, Y, S, 0, "center")
        fx_em(c, t, C["s16.b"] - 0.4, partes, W / 2, Y, S, "center")
        caixa(c, xs[1], Y, ws[1], S, ep(t, C["s16.b"], 0.4), CLARO)
        E.foco(c, t, C["s16.b"] + 0.3, 0.4, lambda a: E.centro(c, "= 5", xs[1] + ws[1] / 2, Y + 110, 64, "g", CLARO, a))
        E.foco(c, t, C["s16.c"], 0.5, lambda a: fx(c, [("2x + 1 = 5  →  x = 2", CLARO)], W / 2, 770, 90, a, "center"))
        E.foco(c, t, C["s16.d"], 0.5, lambda a: fx(c, [("f(5) = 4 · 2 + 3 = ", BR), ("11", CLARO)], W / 2, 930, 100, a, "center"))
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.foco(c, t, C["s17.a"], 0.5, lambda a: fx(c, [("x = 2:  2 · 2 + 1 = ", CLARO), ("5", BR)], W / 2, 330, 96, a, "center"))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: fx(c, [("f(5) = 11", BR)], W / 2, 520, 130, a, "center"))
    nota(c, t, C["s17.c"], "lei inteira ou muitos valores: use o u", W / 2, 760, 54, fundo=BR, cor="#07070F")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 200)
    fx_em(c, t, C["s18.a"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), (" − 4", SAI)], XE, 400, 110)
    fx_em(c, t, C["s18.b"], [("g(", SAI), ("x", ENT), (") = 3", SAI), ("x", ENT)], XE, 560, 110)
    fx_em(c, t, C["s18.c"], [("f(g(2)) = ?", COR)], XE, 760, 100)
    fx_em(c, t, C["s18.d"], [("g(f(2)) = ?", COR)], XE, 920, 100)
    questao_relogio(c, t, C, "s19")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    LEIS["f"], LEIS["g"] = ("x − 4", COR), ("3x", TINTA)
    try:
        fx_em(c, t, C["s20"], [("f(g(2))", SAI)], XE, 220, 84)
        fila(c, t, 380, "gf", ("2", "6", "2"), (C["s20"], C["s20"] + 0.3, C["s20.a"], C["s20.b"]), cor_fim=COR)
        fx_em(c, t, C["s20.a"], [("3 · 2 = 6", SAI)], 560, 530, 60, "center")
        fx_em(c, t, C["s20.b"], [("6 − 4 = 2", SAI)], 1360, 530, 60, "center")
        fx_em(c, t, C["s21"], [("g(f(2))", SAI)], XE, 680, 84)
        fila(c, t, 840, "fg", ("2", "−2", "−6"), (C["s21"], C["s21"] + 0.3, C["s21.a"], C["s21.b"]), cor_fim=COR)
        fx_em(c, t, C["s21.a"], [("2 − 4 = −2", SAI)], 560, 990, 60, "center")
        fx_em(c, t, C["s21.b"], [("3 · (−2) = −6", SAI)], 1360, 990, 60, "center")
        nota(c, t, C["s21.c"], "2 e −6: a ordem mudou o resultado", 1300, 680, 44, fundo=TINTA)
    finally:
        LEIS["f"], LEIS["g"] = ("2x + 1", COR), ("x^2", TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.saida(c, t, C["s23"] - 0.1, lambda: resumo(c, t, C, "s22", [
        ("s22.a", [("de", "i", 84), ("dentro", "g", 88, COR), ("para", "i", 84), ("fora", "g", 88)]),
        ("s22.b", [("a", "i", 84), ("saída", "g", 88, COR), ("de", "i", 84), ("uma", "i", 84), ("é", "i", 84), ("a", "i", 84), ("entrada", "g", 88, COR),
                   ("da", "i", 84), ("outra", "i", 84)]),
        ("s22.c", [("a", "i", 84), ("ordem", "g", 88, COR), ("importa", "i", 84)])]))
    if t < C["s23"]:
        return
    proxima(c, t, C, "s23.a", "quando existe", "a inversa", [("dá", "i", 70), ("para", "i", 70), ("desfazer", "g", 76, COR), ("uma", "i", 70),
                                                             ("função?", "i", 70)], "s23.b", "s23.c", "s23.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, maquinas=b_maquinas, lei=b_lei, volta=b_volta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
