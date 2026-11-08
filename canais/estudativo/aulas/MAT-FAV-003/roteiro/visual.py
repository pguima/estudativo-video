"""Visual — Estudativo · MAT-FAV-003: equações e inequações modulares.

Linguagem visual da trilha Funções Avançadas (MAT-FAV-001 e 002): x em índigo (ENT), números em preto (SAI), condições em cinza.
Nesta aula tudo acontece na reta numérica: o 3 é o centro (bolinha preta), os saltos de 5 passos são arcos (E.salto) e a solução é
pintada em índigo (E.intervalo e pinta()), bolinha vazia quando a ponta não entra e cheia quando entra. A conta fica embaixo da reta.
Erro em vermelho, certo em verde. Palco escuro no atalho (centro e raio)."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-003_equacoes_e_inequacoes_modulares.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("distancia", "inequacao", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert abs(8 - 3) == 5 and abs(-2 - 3) == 5 and 3 + 5 == 8 and 3 - 5 == -2
assert [x for x in range(-20, 20) if abs(x - 3) < 5] == list(range(-1, 8)) and abs(-10 - 3) == 13
assert [x for x in range(-20, 20) if abs(x + 2) <= 4] == list(range(-6, 3)) and -2 - 4 == -6 and -2 + 4 == 2

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


X0, X1 = 240, 1680


def reta3(c, t, t0, y, vmin=-3, vmax=9, size=48):
    return E.reta(c, t, t0, X0, X1, y, vmin, vmax, list(range(vmin, vmax + 1)), E._num, size=size)


def centro3(c, t, t0, vx, y, v=3, cor=TINTA, r=20):
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        c.drawCircle(vx(v), y, r * k, M.paint(cor))


def ponto_reta(c, t, t0, vx, y, v, cor=COR, rotulo=None, r=18):
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        c.drawCircle(vx(v), y, r * k, M.paint(cor))
        anel(c, t, t0, vx(v), y, cor)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        fx_em(c, t, C["s01.a"], [("|", SAI), ("x", ENT), (" − 3| = 5", SAI)], W / 2, 330, 150, "center")
        fx_em(c, t, C["s01.b"], [("x", ENT), (" = 8", SAI)], 560, 600, 130, "center")
        E.foco(c, t, C["s01.b"] + 0.7, 0.4, lambda a: E.selo(c, 820, 560, 44, True, a))
        nota(c, t, C["s01.c"], "incompleto", 560, 760, 56, fundo=ERRADO)
        fx_em(c, t, C["s01.d"], [("x", ENT), (" = ?", CINZA)], 1360, 600, 130, "center")
        E.frase(c, t, C["s01.d"] + 0.9, [("e", "i", 66), ("é", "i", 66), ("negativo", "g", 66, COR)], 1360, 760, "center")
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02.a"], C["s02.end"], [(C["s02.a"] + 1.2, [("equações", "g", 110, COR)]),
                                              (C["s02.a"] + 1.8, [("e", "i", 100), ("inequações", "g", 110, COR)]),
                                              (C["s02.b"], [("pensando", "i", 90), ("em", "i", 90), ("distância", "g", 96)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def i1(a, y):
        fx(c, [("|−7| = 7", SAI)], 430, y, 90, a)
        E.escreve(c, "distância até o zero", 820, y, 62, "i", TINTA2, a)

    def i2(a, y):
        fx(c, [("−1 < 2", SAI), ("x", ENT), (" + 3 ≤ 9", SAI)], 430, y, 84, a)
        E.escreve(c, "a mesma conta nas três partes", 430, y + 90, 56, "i", COR, a)
    lembrete(c, t, C, "s03", [("s03.a", i1), ("s03.b", i2)], y0=450, dy=250)


# ---------------- distância ----------------
def b_distancia(c, t, C, b):
    fx_em(c, t, C["s04.a"], [("|", SAI), ("x", ENT), (" − 3|", SAI)], XE, 230, 110)
    E.frase(c, t, C["s04.a"] + 0.6, [("=", "g", 80), ("distância", "g", 80, COR), ("entre", "i", 80)], 600, 225)
    fx_em(c, t, C["s04.a"] + 1.6, [("x", ENT), (" e ", TINTA2), ("3", SAI)], 1360, 230, 110)
    Y = 580
    vx = reta3(c, t, C["s04"] + 0.3, Y)
    centro3(c, t, C["s04.a"] + 1.6, vx, Y)
    E.salto(c, t, C["s04.b"] + 0.2, vx(3), vx(8), Y, 130, rotulo="5", cor=COR)
    ponto_reta(c, t, C["s04.b"], vx, Y, 8)
    fx_em(c, t, C["s04.b"] + 0.9, [("|", SAI), ("8", ENT), (" − 3| = 5", SAI)], 1260, 820, 90, "center")
    E.salto(c, t, C["s04.c"] + 0.2, vx(3), vx(-2), Y, 130, rotulo="5", cor=COR)
    ponto_reta(c, t, C["s04.c"], vx, Y, -2)
    fx_em(c, t, C["s04.c"] + 1.4, [("|", SAI), ("−2", ENT), (" − 3| = |−5| = 5", SAI)], 560, 820, 90, "center")


# ---------------- equação ----------------
def b_equacao(c, t, C, b):
    fx_em(c, t, C["s05.a"] - 0.8, [("|", SAI), ("x", ENT), (" − 3| = 5", SAI)], W / 2, 200, 120, "center")
    Y = 500
    vx = reta3(c, t, C["s05"], Y)
    centro3(c, t, C["s05"] + 0.2, vx, Y)
    E.frase(c, t, C["s05.b"], [("a", "i", 64), ("5", "g", 66, COR), ("passos", "i", 64), ("do", "i", 64), ("3", "g", 66)], W / 2, 330, "center")

    def saltos():
        E.salto(c, t, C["s05.c"], vx(3), vx(8), Y, 120, rotulo="5", cor=COR)
        E.salto(c, t, C["s05.d"], vx(3), vx(-2), Y, 120, rotulo="5", cor=COR)
    E.saida(c, t, C["s07"] - 0.1, saltos)
    ponto_reta(c, t, C["s05.c"] + 0.6, vx, Y, 8)
    ponto_reta(c, t, C["s05.d"] + 0.6, vx, Y, -2)
    q = ep(t, C["s05.d"] + 1.2, 0.4) * (1 - ep(t, C["s07"] - 0.1, 0.3))
    if q > 0:
        for v in (8, -2):
            fx(c, [("x = " + E._num(v), COR)], vx(v), Y + 160, 64, q, "center")

    def contas():
        nota(c, t, C["s06.a"], "o de dentro vale 5 ou −5", W / 2, 720, 50, fundo=TINTA)
        eqn_em(c, t, C["s06.b"], [("x", ENT), (" − 3", SAI)], [("5", SAI), ("   →   ", TINTA2), ("x", ENT), (" = 8", COR)], 860, 100, 720)
        eqn_em(c, t, C["s06.c"], [("x", ENT), (" − 3", SAI)], [("−5", SAI), ("   →   ", TINTA2), ("x", ENT), (" = −2", COR)], 990, 100, 720)
    if t >= C["s06"]:
        E.saida(c, t, C["s07"] - 0.1, contas)
    if t < C["s07"]:
        return
    E.foco(c, t, C["s07.a"], 0.5, lambda a: (fx(c, [("|", SAI), ("x", ENT), (" − 3| = 0", SAI)], 560, 800, 96, a, "center"),
                                             E.centro(c, "só o 3", 560, 920, 66, "g", COR, a)))
    if t >= C["s07.a"]:
        anel(c, t, C["s07.a"] + 0.3, vx(3), Y, COR)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (fx(c, [("|", SAI), ("x", ENT), (" − 3| = −1", SAI)], 1360, 800, 96, a, "center"),
                                             E.centro(c, "nenhum número", 1360, 920, 66, "g", ERRADO, a)))


# ---------------- inequação ----------------
def b_inequacao(c, t, C, b):
    Y = 520
    if t < C["s10"]:
        fx_em(c, t, C["s08.a"], [("|", SAI), ("x", ENT), (" − 3| < 5", SAI)], W / 2, 200, 120, "center")
        vx = reta3(c, t, C["s08"], Y)
        centro3(c, t, C["s08"] + 0.2, vx, Y)
        E.frase(c, t, C["s08.b"], [("a", "i", 64), ("menos", "g", 66, COR), ("de", "i", 64), ("5", "g", 66), ("passos", "i", 64), ("do", "i", 64),
                                   ("3", "g", 66)], W / 2, 330, "center")
        E.intervalo(c, t, C["s08.c"], vx, Y, -2, 8)
        nota(c, t, C["s08.d"], "vazia nas pontas: 5 não é menor que 5", W / 2, 690, 46, fundo=TINTA)
        S = 100
        eqn_em(c, t, C["s09.a"], [("−5 < ", SAI), ("x", ENT), (" − 3", SAI)], [("5", SAI)], 860, S, 960, "<")
        nota(c, t, C["s09.b"], "+3 nas três partes", W / 2, 950, 46)
        E.saida(c, t, C["s09.c"] - 0.1, lambda: None)
        if t >= C["s09.c"]:
            E.foco(c, t, C["s09.c"], 0.5, lambda a: fx(c, [("−2 < ", SAI), ("x", ENT), (" < 8", SAI)], 1500, 860, S, a, "center"))
        return
    fx_em(c, t, C["s10"], [("|", SAI), ("x", ENT), (" − 3| > 5", SAI)], W / 2, 200, 120, "center")
    vx = reta3(c, t, C["s10"], Y)
    centro3(c, t, C["s10"] + 0.2, vx, Y)
    E.frase(c, t, C["s10.b"], [("a", "i", 64), ("mais", "g", 66, COR), ("de", "i", 64), ("5", "g", 66), ("passos", "i", 64), ("do", "i", 64),
                               ("3", "g", 66)], W / 2, 330, "center")
    pinta(c, t, C["s10.c"], C["s10.c"] + 0.2, vx, Y, -2, -1, False, X0 - 60, X1 + 60)
    pinta(c, t, C["s10.c"] + 0.4, C["s10.c"] + 0.6, vx, Y, 8, 1, False, X0 - 60, X1 + 60)
    E.foco(c, t, C["s10.c"] + 1.0, 0.5, lambda a: fx(c, [("x", ENT), (" < −2", COR), ("   ou   ", TINTA2), ("x", ENT), (" > 8", COR)],
                                                    W / 2, 820, 100, a, "center"))
    nota(c, t, C["s10.c"] + 1.8, "do lado de fora", W / 2, 960, 50, fundo=TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("cuidado:", "g", 84, ERRADO), ("tirar", "i", 80), ("as", "i", 80), ("barras", "g", 84)], W / 2, 170, "center")
    Y = 600
    vx = E.reta(c, t, C["s11"], 200, 1720, Y, -11, 9, [-10, -5, -2, 0, 3, 5, 8], E._num, size=46)
    fx_em(c, t, C["s11"] + 0.4, [("|", SAI), ("x", ENT), (" − 3| < 5", SAI)], 560, 330, 96, "center")
    certo = C["s12.c"]
    E.saida(c, t, certo - 0.1, lambda: (fx_em(c, t, C["s11.b"], [("x", ENT), (" − 3 < 5", ERRADO)], 1340, 330, 96, "center"),
                                        pinta(c, t, C["s11.c"], C["s11.c"] + 0.2, vx, Y, 8, -1, False, 140, 1780, ERRADO),
                                        fx_em(c, t, C["s11.c"], [("x", ENT), (" < 8", ERRADO)], 1340, 460, 96, "center")))
    centro3(c, t, C["s12.a"] - 0.3, vx, Y)
    if t >= C["s12.a"]:
        E.saida(c, t, certo + 1.5, lambda: (ponto_reta(c, t, C["s12.a"], vx, Y, -10, ERRADO),
                                            E.salto(c, t, C["s12.b"], vx(-10), vx(3), Y, 170, rotulo="13 passos", cor=ERRADO)))
    E.foco(c, t, C["s12.b"] + 0.9, 0.5, lambda a: E.escreve(c, "13 não é menor que 5", 660, 860, 64, "i", ERRADO, a))
    if t >= certo:
        E.intervalo(c, t, certo, vx, Y, -2, 8, cor=CERTO)
        nota(c, t, certo + 0.4, "faltou: x > −2", W / 2, 960, 52, fundo=CERTO)
        E.foco(c, t, certo, 0.5, lambda a: fx(c, [("−2 < ", CERTO), ("x", ENT), (" < 8", CERTO)], 1340, 460, 96, a, "center"))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13.a"], [("centro", "g", 110, BR), ("e", "i", 100, CLARO), ("raio", "g", 110, BR)], W / 2, 210, "center")
        S, Y = 130, 420
        partes = [("|", BR), ("x − 3", CLARO), ("| < ", BR), ("5", CLARO)]
        w, xs, ws = fx(c, partes, W / 2, Y, S, 0, "center")
        fx_em(c, t, C["s13.a"] + 0.6, partes, W / 2, Y, S, "center")
        caixa(c, xs[1], Y, ws[1], S, ep(t, C["s13.b"], 0.4), CLARO)
        caixa(c, xs[3], Y, ws[3], S, ep(t, C["s13.c"], 0.4), BR)
        E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: E.centro(c, "centro: 3", xs[1] + ws[1] / 2, Y + 120, 58, "g", CLARO, a))
        E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: E.centro(c, "raio: 5", xs[3] + ws[3] / 2, Y + 120, 58, "g", BR, a))
        y2 = 820
        q = ep(t, C["s13.d"], 0.5)
        if q > 0:
            vx = lambda v: 960 + (v - 3) * 120
            M.line(c, vx(-3), y2, vx(9), y2, CLARO, q * 0.6, 4)
            c.drawCircle(vx(3), y2, 18, M.paint(BR, q))
            E.salto(c, t, C["s13.d"], vx(3), vx(-2), y2, 100, cor=CLARO)
            E.salto(c, t, C["s13.d"] + 0.3, vx(3), vx(8), y2, 100, cor=CLARO)
            E.foco(c, t, C["s13.d"] + 0.8, 0.4, lambda a: (E.centro(c, "3 − 5 = −2", vx(-2), y2 + 90, 54, "g", BR, a),
                                                          E.centro(c, "3 + 5 = 8", vx(8), y2 + 90, 54, "g", BR, a)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    y = 330
    vx = lambda v: 1240 + (v - 3) * 55
    for i, (k, txt, fora) in enumerate((("s14.a", "menor: entre", False), ("s14.b", "maior: fora", True))):
        yy = y + i * 260
        q = ep(t, C[k], 0.5)
        if q <= 0:
            continue
        E.escreve(c, txt, 260, yy + 20, 84, "g", BR, q)
        M.line(c, vx(-4), yy, vx(10), yy, CLARO, q * 0.5, 4)
        if fora:
            M.line(c, vx(-4), yy, vx(-2), yy, CLARO, q, 12)
            M.line(c, vx(8), yy, vx(10), yy, CLARO, q, 12)
        else:
            M.line(c, vx(-2), yy, vx(8), yy, CLARO, q, 12)
        for v in (-2, 8):
            c.drawCircle(vx(v), yy, 16, M.paint("#07070F", q))
            c.drawCircle(vx(v), yy, 16, M.paint(CLARO, q, stroke=6))
    nota(c, t, C["s14.c"], "com número multiplicando o x: inequação dupla", W / 2, 900, 50, fundo=BR, cor="#07070F")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 220)
    fx_em(c, t, C["s15.a"], [("|", SAI), ("x", ENT), (" + 2| ≤ 4", SAI)], XE, 520, 150)
    E.frase(c, t, C["s15.b"], [("resposta", "i", 84), ("em", "i", 84), ("intervalo", "g", 84, COR)], XE, 760)
    E.foco(c, t, C["s15.b"] + 0.8, 0.5, lambda a: fx(c, [("[ ?, ? ]", COR)], XE + 200, 900, 100, a))
    questao_relogio(c, t, C, "s16")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Y = 640
    vx = E.reta(c, t, C["s17"], 300, 1620, Y, -7, 3, list(range(-7, 4)), E._num, size=46)
    fx_em(c, t, C["s17"], [("|", SAI), ("x", ENT), (" + 2| ≤ 4", SAI)], XE, 200, 90)

    def s17():
        fx_em(c, t, C["s17.a"], [("x + 2 = 0  →  centro ", SAI), ("−2", COR)], XE, 340, 72)
        fx_em(c, t, C["s17.b"], [("raio ", SAI), ("4", COR)], 1280, 340, 72)
        E.salto(c, t, C["s17.c"], vx(-2), vx(-6), Y, 120, rotulo="−2 − 4 = −6", cor=COR, size=46)
        E.salto(c, t, C["s17.d"], vx(-2), vx(2), Y, 120, rotulo="−2 + 4 = 2", cor=COR, size=46)
    E.saida(c, t, C["s18.b"], s17)
    centro3(c, t, C["s17.a"] + 0.6, vx, Y, -2)
    nota(c, t, C["s18.a"], "menor ou igual: entre, com as pontas", W / 2, 470, 46, fundo=TINTA)
    E.intervalo(c, t, C["s18.b"], vx, Y, -6, 2, True, True)
    E.foco(c, t, C["s18.b"] + 0.4, 0.5, lambda a: fx(c, [("−6 ≤ ", SAI), ("x", ENT), (" ≤ 2", SAI)], 560, 860, 90, a, "center"))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "[−6, 2]", 560, 985, 70, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s18.d"], 0.5, lambda a: (E.escreve(c, "pela conta:", 1060, 820, 50, "i", TINTA2, a),
                                             fx(c, [("−4 ≤ ", SAI), ("x", ENT), (" + 2 ≤ 4", SAI)], 1060, 900, 76, a)))
    E.foco(c, t, C["s18.e"], 0.5, lambda a: (fx(c, [("−6 ≤ ", CERTO), ("x", ENT), (" ≤ 2", CERTO)], 1060, 1000, 76, a),
                                             E.selo(c, 1620, 975, 36, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.saida(c, t, C["s20"] - 0.1, lambda: resumo(c, t, C, "s19", [
        ("s19.a", [("módulo", "g", 88, COR), ("é", "i", 84), ("distância", "i", 84)]),
        ("s19.b", [("igual:", "i", 84), ("duas", "g", 88, COR), ("respostas", "i", 84)]),
        ("s19.c", [("menor:", "i", 84), ("entre;", "g", 88, COR), ("maior:", "i", 84), ("fora", "g", 88, COR)])]))
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20.a", "função", "composta", [("a", "i", 66), ("saída", "g", 70, COR), ("de", "i", 66), ("uma", "i", 66), ("vira", "i", 66),
                                                    ("a", "i", 66), ("entrada", "g", 70, COR), ("da", "i", 66), ("outra", "i", 66)],
            "s20.b", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, distancia=b_distancia, equacao=b_equacao, inequacao=b_inequacao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
