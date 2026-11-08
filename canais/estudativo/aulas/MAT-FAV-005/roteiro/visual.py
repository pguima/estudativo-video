"""Visual — Estudativo · MAT-FAV-005: quando existe a inversa, função bijetora.

Linguagem visual da trilha Funções Avançadas (MAT-FAV-001 a 004): x e entrada em índigo (ENT), saída em preto (SAI). Nesta aula:
o plano com a curva de y = x² montada como na aula de gráfico (a palavra parábola fica fora: não está na ficha); a reta horizontal
(tracejada) que corta a curva em dois pontos testa a injetora; a faixa vermelha no eixo y abaixo de zero mostra as saídas prometidas
que nunca saem (sobrejetora); a metade da esquerda que some ao trocar o domínio. Selos de certo e errado em cada palavra.
Palco escuro no atalho."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-005_funcao_bijetora.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("inversa", "injetora", "bijetora", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert (-2) ** 2 == 2 ** 2 == 4 and math.isqrt(4) == 2
assert all(x * x >= 0 for x in range(-10, 11))

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


PX = (1000, 130, 820, 860, -3.2, 3.2, -2, 9.5)
q2 = lambda x: x * x


def plano_x2(c, t, t0, d_curva=1.0, a=-3.05, b=3.05, curva=True):
    P = E.plano(c, t, t0, *PX, marcas_x=[-3, -2, -1, 1, 2, 3], marcas_y=[-1, 1, 4, 9], size=38)
    if curva:
        E.curva(c, t, t0 + 0.3, P, q2, a, b, d=d_curva, cor=COR)
    return P


def horizontal(c, t, t0, P, y, cor=TINTA, d=0.6, x0=None, x1=None):
    p = ep(t, t0, d)
    if p > 0:
        xa = P.x(P.xmin) if x0 is None else x0
        xb = P.x(P.xmax) if x1 is None else x1
        M.line(c, xa, P.y(y), lerp(xa, xb, p), P.y(y), cor, 0.9, 5, dash=E.TRACO)


def selo_txt(c, t, t0, txt, ok, x, y, size=74):
    E.foco(c, t, t0, 0.5, lambda a: (E.escreve(c, txt, x, y, size, "g", TINTA, a),
                                     E.selo(c, x + E.larg(txt, "g", size) + 60, y - size * 0.32, 38, ok, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01.a"], [("pensei", "i", 76), ("num", "i", 76), ("número", "g", 80, COR)], XE, 220)
        E.foco(c, t, C["s01.a"] + 0.6, 0.5, lambda a: (M.rrect(c, XE, 320, 220, 220, 30, COR, a), centro(c, "?", XE + 110, 480, 170, "g", BR, a)))
        fx_em(c, t, C["s01.b"], [("?", COR), ("^2", COR), (" = 4", SAI)], 520, 480, 150)
        fx_em(c, t, C["s01.c"], [("2", ENT), ("^2", ENT), (" = 4", SAI)], 1200, 380, 110)
        fx_em(c, t, C["s01.d"], [("(−2)", ENT), ("^2", ENT), (" = 4", SAI)], 1200, 560, 110)
        nota(c, t, C["s01.d"] + 1.0, "não dá para saber", 1420, 680, 50, fundo=TINTA)
        nota(c, t, C["s01.e"], "essa função não tem inversa", W / 2, 900, 60, fundo=ERRADO)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02.a"], C["s02.end"], [(C["s02.a"] + 1.4, [("desfazer?", "g", 110, COR)]),
                                              (C["s02.b"], [("injetora", "g", 96)]),
                                              (C["s02.b"] + 0.7, [("sobrejetora", "g", 96)]),
                                              (C["s02.b"] + 1.4, [("bijetora", "g", 96, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def i1(a, y):
        E.escreve(c, "contradomínio:", 430, y, 66, "g", TINTA, a)
        E.escreve(c, "onde a saída pode cair", 930, y, 62, "i", TINTA2, a)
        E.escreve(c, "imagem:", 430, y + 100, 66, "g", COR, a)
        E.escreve(c, "o que de fato sai", 720, y + 100, 62, "i", TINTA2, a)

    def i2(a, y):
        E.escreve(c, "ler o gráfico:", 430, y, 66, "i", TINTA, a)
        E.escreve(c, "onde sobe, onde desce", 860, y, 66, "g", COR, a)
    lembrete(c, t, C, "s03", [("s03.a", i1), ("s03.b", i2)], y0=440, dy=300)


# ---------------- a inversa ----------------
def b_inversa(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("a", "i", 80), ("inversa", "g", 86, COR), ("desfaz", "i", 80)], W / 2, 200, "center")
    E.foco(c, t, C["s04.a"] + 0.4, 0.5, lambda a: (E.pilula(c, "entrada", 560, 420, 64, "g", fundo=ENT, a=a),
                                                   E.pilula(c, "saída", 1360, 420, 64, "g", fundo=SAI, a=a)))
    p = ep(t, C["s04.a"] + 0.8, 0.6)
    if p > 0:
        M.arrow(c, 760, 380, lerp(760, 1190, p), 380, COR, 1.0, 6, 22, p)
        E.centro(c, "f", 975, 350, 64, "g", COR, p)
    p = ep(t, C["s04.a"] + 1.8, 0.6)
    if p > 0:
        M.arrow(c, 1190, 470, lerp(1190, 760, p), 470, TINTA2, 1.0, 6, 22, p)
        E.centro(c, "inversa", 975, 540, 54, "i", TINTA2, p)
    item(c, t, C["s04.b"], 1, 300, 730)
    E.frase(c, t, C["s04.b"] + 0.1, [("cada", "i", 72), ("saída", "g", 74, SAI), ("vem", "i", 72), ("de", "i", 72), ("uma", "i", 72),
                                     ("entrada", "g", 74, ENT), ("só", "i", 72)], 400, 730)
    item(c, t, C["s04.c"], 2, 300, 900)
    E.frase(c, t, C["s04.c"] + 0.1, [("toda", "i", 72), ("saída", "g", 74, SAI), ("pedida", "i", 72), ("existe", "g", 74)], 400, 900)


# ---------------- injetora e sobrejetora ----------------
def b_injetora(c, t, C, b):
    P = plano_x2(c, t, C["s05"])
    E.frase(c, t, C["s05.a"], [("injetora", "g", 110, COR)], XE, 230)
    E.frase(c, t, C["s05.b"], ps("entradas diferentes", "i", 66), XE, 360)
    E.frase(c, t, C["s05.b"] + 0.9, ps("dão saídas diferentes", "i", 66), XE, 450)
    for i, v in enumerate((-2, 2)):
        E.ponto(c, t, C["s05.c"] + 0.4 * i, P, v, 4, cor=ERRADO if t >= C["s05.d"] else COR)
    E.foco(c, t, C["s05.c"], 0.5, lambda a: fx(c, [("−2", ENT), ("  e  ", TINTA2), ("2", ENT)], XE, 600, 90, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: (E.escreve(c, "ambas dão", XE + 400, 595, 64, "i", TINTA, a),
                                             fx(c, [("4", ERRADO)], XE + 720, 600, 96, a)))
    horizontal(c, t, C["s06.a"], P, 4, ERRADO)
    E.foco(c, t, C["s06.a"] + 0.4, 0.4, lambda a: fx(c, [("y = 4", ERRADO)], P.x(3.1), P.y(4) - 20, 44, a, "right"))
    if t >= C["s06.b"]:
        anel(c, t, C["s06.b"], *P(-2, 4), ERRADO)
        anel(c, t, C["s06.b"] + 0.3, *P(2, 4), ERRADO)
    E.foco(c, t, C["s06.c"], 0.4, lambda a: (fx(c, [("x = −2", ENT)], P.x(-2), P.y(4) + 70, 44, a, "center"),
                                             fx(c, [("x = 2", ENT)], P.x(2), P.y(4) + 70, 44, a, "center")))
    nota(c, t, C["s06.d"], "reta horizontal corta 2 vezes:", 540, 760, 44, fundo=TINTA)
    E.foco(c, t, C["s06.d"] + 0.6, 0.5, lambda a: (E.escreve(c, "não é injetora", XE, 900, 76, "g", ERRADO, a),
                                                   E.selo(c, XE + 620, 875, 40, False, a)))


def b_sobrejetora(c, t, C, b):
    P = plano_x2(c, t, C["s07"] - 2.0, d_curva=0.1)
    E.frase(c, t, C["s07.a"], [("sobrejetora", "g", 110, COR)], XE, 230)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (E.escreve(c, "imagem", XE, 380, 72, "g", COR, a),
                                             E.escreve(c, "=", XE + 300, 380, 72, "g", TINTA, a),
                                             E.escreve(c, "contradomínio", XE + 370, 380, 72, "g", TINTA, a)))
    E.frase(c, t, C["s07.b"] + 1.2, ps("tudo o que promete, entrega", "i", 56, TINTA2), XE, 470, passo=0.1)
    E.foco(c, t, C["s08.a"], 0.5, lambda a: (E.escreve(c, "contradomínio:", XE, 610, 62, "i", TINTA, a),
                                             fx(c, [("ℝ", COR)], XE + 430, 615, 90, a),
                                             E.escreve(c, "tem negativos", XE + 520, 610, 56, "i", TINTA2, a)))
    q = ep(t, C["s08.a"] + 0.4, 0.5)
    if q > 0:
        M.line(c, P.ox, P.y(0), P.ox, P.y(-2), ERRADO, 0.25 * q, 30)
    fx_em(c, t, C["s08.b"], [("?", COR), ("^2", COR), (" = −1", SAI)], XE, 760, 90)
    E.frase(c, t, C["s08.b"] + 0.6, [("nenhum", "g", 70, ERRADO), ("número", "i", 66)], XE + 420, 750)
    horizontal(c, t, C["s08.c"], P, -1, ERRADO)
    E.foco(c, t, C["s08.c"] + 0.5, 0.4, lambda a: E.escreve(c, "não toca", P.x(1.1), P.y(-1) + 60, 44, "i", ERRADO, a))
    E.foco(c, t, C["s08.d"], 0.5, lambda a: (E.escreve(c, "não é sobrejetora", XE, 920, 76, "g", ERRADO, a),
                                             E.selo(c, XE + 760, 895, 40, False, a)))


# ---------------- bijetora e o conserto ----------------
def b_bijetora(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], [("injetora", "g", 96), ("+", "g", 96, COR), ("sobrejetora", "g", 96)], W / 2, 380, "center")
        E.frase(c, t, C["s09.a"], [("=", "g", 110), ("bijetora", "g", 150, COR)], W / 2, 600, "center")
        nota(c, t, C["s09.b"], "só a bijetora tem inversa", W / 2, 820, 62)
        return
    P = E.plano(c, t, C["s10"], *PX, marcas_x=[-3, -2, -1, 1, 2, 3], marcas_y=[1, 4, 9], size=38)
    k = 1 - ep(t, C["s10.b"], 0.8)
    tenue(c, k, lambda: traco(c, P, amostra(q2, -3.05, 0), COR))
    if k < 1:
        tenue(c, 0.25, lambda: traco(c, P, amostra(q2, -3.05, 0), TINTA2, 1.0, 4, E.TRACO))
    traco(c, P, amostra(q2, 0, 3.05), COR)
    if t >= C["s10.b"]:
        q = ep(t, C["s10.b"], 0.5)
        M.rrect(c, P.caixa[0], P.caixa[1], P.ox - P.caixa[0], P.caixa[3], 0, E.PAPEL2, 0.45 * q)
    fx_em(c, t, C["s10.a"], [("x", ENT), (" ≥ 0", SAI)], XE, 260, 110)
    E.frase(c, t, C["s10.b"], ps("some a metade da esquerda", "i", 60, TINTA2), XE, 370, passo=0.1)
    horizontal(c, t, C["s10.b"] + 1.0, P, 4, TINTA)
    E.ponto(c, t, C["s10.b"] + 1.4, P, 2, 4, cor=CERTO)
    selo_txt(c, t, C["s10.c"], "injetora", True, XE, 520)
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (E.escreve(c, "contradomínio:", XE, 660, 60, "i", TINTA, a),
                                             fx(c, [("[0, +∞[", COR)], XE + 420, 665, 84, a)))
    E.frase(c, t, C["s11.b"], ps("toda saída aparece", "i", 60, TINTA2), XE, 760)
    selo_txt(c, t, C["s11.c"], "bijetora", True, XE, 900, 90)
    if t >= C["s11.d"]:
        p = ep(t, C["s11.d"], 0.7)
        M.line(c, P.x(0), P.y(4), P.x(2), P.y(4), CERTO, p, 6)
        M.arrow(c, P.x(2), P.y(4), P.x(2), lerp(P.y(4), P.y(0) - 8, p), CERTO, 1.0, 6, 20, p)
        E.foco(c, t, C["s11.d"] + 0.6, 0.4, lambda a: fx(c, [("r{4} = 2", CERTO)], P.x(2) + 30, P.y(1.6), 64, a))
        nota(c, t, C["s11.d"] - 0.3, "saiu 4", P.x(-1.6), P.y(4), 44, fundo=TINTA)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("cuidado:", "g", 84, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"] + 0.4, [("a", "i", 80), ("reta", "i", 80), ("vertical", "g", 84)], XE, 300)
    P = plano_x2(c, t, C["s12"], d_curva=0.8)
    # reta vertical que desliza
    if t >= C["s12.b"]:
        u = ease_io(prog(t, C["s12.b"], 2.4))
        xv = lerp(-2.6, 1.5, u)
        k = 1 - ep(t, C["s12.d"] - 0.2, 0.4)
        if k > 0:
            M.line(c, P.x(xv), P.caixa[1], P.x(xv), P.caixa[1] + P.caixa[3], TINTA, k, 5, dash=E.TRACO)
            c.drawCircle(*P(xv, q2(xv)), 14 * k, M.paint(TINTA, k))
    E.frase(c, t, C["s12.b"], ps("testa se é função:", "i", 62), XE, 430)
    E.frase(c, t, C["s12.b"] + 1.2, ps("cada x, uma saída", "i", 62, TINTA2), XE, 520)
    selo_txt(c, t, C["s12.c"], "x² passa", True, XE, 640, 80)
    E.foco(c, t, C["s12.c"] + 1.4, 0.5, lambda a: E.escreve(c, "e não é injetora", XE, 740, 62, "i", ERRADO, a))
    horizontal(c, t, C["s12.d"], P, 4, COR)
    if t >= C["s12.d"]:
        anel(c, t, C["s12.d"] + 0.4, *P(-2, 4))
        anel(c, t, C["s12.d"] + 0.6, *P(2, 4))
    nota(c, t, C["s12.d"], "injetora: reta horizontal", 520, 900, 54)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13.a"], [("só", "i", 90, CLARO), ("sobe", "g", 96, BR), ("ou", "i", 90, CLARO), ("só", "i", 90, CLARO), ("desce?", "g", 96, BR)],
            W / 2, 210, "center")

    def mini(a, x, y, f, ok, txt):
        P = E.Plano(x, y, 520, 380, -2, 2, -1, 4.5)
        M.line(c, P.x(-2), P.y(0), P.x(2), P.y(0), CLARO, a * 0.5, 4)
        M.line(c, P.x(0), P.y(-1), P.x(0), P.y(4.5), CLARO, a * 0.5, 4)
        traco(c, P, amostra(f, -2, 2), BR if ok else CLARO, a, 8)
        E.centro(c, txt, x + 260, y + 470, 58, "g", BR, a)
        E.selo(c, x + 260, y + 560, 40, ok, a)
    E.saida(c, t, C["s14"] - 0.1, lambda: (E.foco(c, t, C["s13.b"], 0.5, lambda a: mini(a, 260, 340, lambda x: x + 2, True, "nunca vira: injetora")),
                                           E.foco(c, t, C["s13.c"], 0.5, lambda a: mini(a, 1140, 340, q2, False, "desce e sobe: repete"))))
    if t >= C["s13.c"]:
        q = ep(t, C["s13.c"] + 0.8, 0.5) * (1 - ep(t, C["s14"], 0.4))
        if q > 0:
            P = E.Plano(1140, 340, 520, 380, -2, 2, -1, 4.5)
            M.line(c, P.x(-2), P.y(2.25), P.x(2), P.y(2.25), CLARO, q, 4, dash=E.TRACO)
    if t >= C["s14"]:
        nota(c, t, C["s14.a"], "o atalho só responde se é injetora", W / 2, 500, 60, fundo=BR, cor="#07070F")
        nota(c, t, C["s14.b"], "sobrejetora: compare imagem e contradomínio", W / 2, 700, 60, fundo=CLARO, cor="#07070F")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    fx_em(c, t, C["s15.a"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("x", ENT), ("^2", ENT)], XE, 380, 120)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.escreve(c, "domínio:", XE, 540, 64, "i", TINTA, a), fx(c, [("[0, +∞[", ENT)], XE + 290, 545, 84, a)))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (E.escreve(c, "contradomínio:", XE, 680, 64, "i", TINTA, a), fx(c, [("ℝ", SAI)], XE + 460, 685, 96, a)))
    E.frase(c, t, C["s15.d"], [("injetora?", "g", 70, COR), ("sobrejetora?", "g", 70, COR), ("bijetora?", "g", 70, COR)], XE, 880)
    questao_relogio(c, t, C, "s16", cx=1560, cy=520)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = E.plano(c, t, C["s17"], *PX, marcas_x=[-3, -2, -1, 1, 2, 3], marcas_y=[-1, 1, 4, 9], size=38)
    E.curva(c, t, C["s17"] + 0.3, P, q2, 0, 3.05, d=0.8, cor=COR)
    E.foco(c, t, C["s17.a"], 0.4, lambda a: M.arrow(c, P.x(1), P.y(3.2), P.x(2.2), P.y(6.6), CERTO, a, 7, 22))
    E.frase(c, t, C["s17.a"], [("só", "i", 66), ("sobe", "g", 70, CERTO)], XE, 250)
    selo_txt(c, t, C["s17.b"], "injetora", True, XE, 380)
    q = ep(t, C["s17.c"], 0.5)
    if q > 0:
        M.line(c, P.ox, P.y(0), P.ox, P.y(-2), ERRADO, 0.25 * q, 30)
    horizontal(c, t, C["s17.c"], P, -1, ERRADO)
    E.frase(c, t, C["s17.c"], [("nenhum", "i", 60), ("quadrado", "i", 60), ("dá", "i", 60), ("negativo", "g", 62, ERRADO)], XE, 500)
    selo_txt(c, t, C["s17.d"], "sobrejetora", False, XE, 630)
    E.saida(c, t, C["s18.c"] - 0.1, lambda: selo_txt(c, t, C["s17.e"], "bijetora", False, XE, 770))
    E.foco(c, t, C["s18.a"], 0.5, lambda a: (E.escreve(c, "contradomínio:", XE, 900, 56, "i", TINTA, a), fx(c, [("[0, +∞[", CERTO)], XE + 400, 905, 80, a)))
    q = ep(t, C["s18.a"] + 0.3, 0.5)
    if q > 0:
        M.rrect(c, P.caixa[0], P.y(0), P.caixa[2], P.y(-2) - P.y(0), 0, E.PAPEL2, 0.6 * q)
    E.frase(c, t, C["s18.b"], ps("mesma lei, mesmo desenho", "i", 50, TINTA2), 1000, 1040, passo=0.1)
    if t >= C["s18.c"]:
        selo_txt(c, t, C["s18.c"], "bijetora", True, XE, 770)
        nota(c, t, C["s18.c"] + 1.0, "o contradomínio faz parte da função", 560, 1010, 40, fundo=TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.saida(c, t, C["s20"] - 0.1, lambda: resumo(c, t, C, "s19", [
        ("s19.a", [("injetora:", "g", 84, COR), ("não", "i", 80), ("repete", "i", 80), ("saída", "i", 80)]),
        ("s19.b", [("sobrejetora:", "g", 84, COR), ("entrega", "i", 80), ("tudo", "i", 80)]),
        ("s19.c", [("bijetora:", "g", 84, COR), ("as", "i", 80), ("duas,", "i", 80), ("tem", "i", 80), ("inversa", "g", 84)])]))
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20.a", "calcular", "a inversa", [("o", "i", 70), ("gráfico", "i", 70), ("é", "i", 70), ("um", "i", 70), ("espelho", "g", 76, COR)],
            "s20.b", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, inversa=b_inversa, injetora=b_injetora, sobrejetora=b_sobrejetora, bijetora=b_bijetora,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
