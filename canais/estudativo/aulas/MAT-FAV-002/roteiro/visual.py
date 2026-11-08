"""Visual — Estudativo · MAT-FAV-002: módulo de um número e gráfico em V.

Linguagem visual da trilha Funções Avançadas (MAT-FAV-001): x e entrada em índigo (ENT), saída em preto (SAI), condições em cinza,
chave por_partes(), plano à direita e texto à esquerda. Nesta aula: a reta numérica com os saltos até o zero (E.salto) para o módulo
como distância; o V de y = |x| montado ponto a ponto; o V que anda (ve(): vértice (h, k) animado) para |x − 2| + 1; a parte de baixo
de x² − 4 que rebate para cima (achata e vira, como uma dobra no eixo x). Erro em vermelho, certo em verde. Palco escuro no atalho."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-002_modulo_e_grafico_em_v.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("modulo", "ve", "rebate", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert abs(-7) == 7 and abs(7) == 7 and abs(0) == 0
assert [abs(x) for x in (0, 1, -1, 2, -2, 3, -3)] == [0, 1, 1, 2, 2, 3, 3]
assert abs(2 - 2) + 1 == 1 and abs(0 - 2) + 1 == 3 and abs(4 - 2) + 1 == 3
assert (-2) ** 2 - 4 == 0 and 2 ** 2 - 4 == 0 and abs(0 ** 2 - 4) == 4
assert abs(-3 + 3) - 2 == -2 and abs(0 + 3) - 2 == 1

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



def ve(c, P, h, k, cor, a=1.0, largura=7, x0=None, x1=None):
    """V de y = |x − h| + k, recortado no plano"""
    x0 = P.xmin if x0 is None else x0
    x1 = P.xmax if x1 is None else x1
    traco(c, P, [(x0, abs(x0 - h) + k), (h, k), (x1, abs(x1 - h) + k)], cor, a, largura)


def ve_cresce(c, t, t0, P, h, k, cor, d=0.9, largura=7):
    """o V desenhado da esquerda para a direita"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    x0, x1 = P.xmin, P.xmax
    xe = lerp(x0, x1, p)
    pts = [(x0, abs(x0 - h) + k)]
    if xe > h:
        pts.append((h, k))
    pts.append((xe, abs(xe - h) + k))
    traco(c, P, pts, cor, 1.0, largura)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        vx = E.reta(c, t, C["s01"], 230, 1690, 470, -8, 8, [-7, 0, 7], E._num, size=56)
        for v, k in ((-7, "s01.a"), (7, "s01.a")):
            E.foco(c, t, C[k] + (0 if v < 0 else 0.4), 0.3, lambda a, v=v: c.drawCircle(vx(v), 470, 20, M.paint(COR if v > 0 else TINTA, a)))
        E.salto(c, t, C["s01.b"], vx(0), vx(-7), 470, 150, rotulo="7 passos", cor=TINTA)
        E.salto(c, t, C["s01.b"] + 0.5, vx(0), vx(7), 470, 150, rotulo="7 passos")
        E.frase(c, t, C["s01.a"], [("diferentes,", "i", 72), ("mas...", "i", 72)], XE, 200)
        E.frase(c, t, C["s01.c"], [("distância", "i", 80), ("até", "i", 80), ("o", "i", 80), ("zero:", "i", 80)], XE, 760)
        E.frase(c, t, C["s01.c"] + 0.8, [("módulo", "g", 150, COR)], XE, 930)
        E.foco(c, t, C["s01.d"], 0.5, lambda a: traco(c, E.Plano(1250, 640, 460, 360, -3, 3, 0, 3),
                                                     [(-3, 3), (0, 0), (3, 3)], COR, a, 14))
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02.a"], C["s02.end"], [(C["s02.a"] + 1.4, [("o", "i", 100), ("módulo", "g", 110, COR)]),
                                              (C["s02.b"], [("o", "i", 100), ("V", "g", 110, COR)]),
                                              (C["s02.c"], [("mover", "i", 100), ("o", "i", 100), ("V", "g", 110)]),
                                              (C["s02.d"], [("rebater", "g", 110, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def i1(a, y):
        E.escreve(c, "função por partes:", 430, y, 70, "i", TINTA, a)
        E.escreve(c, "a chave e as condições", 1030, y, 64, "g", COR, a)

    def i2(a, y):
        E.escreve(c, "raízes:", 430, y, 70, "i", TINTA, a)
        E.escreve(c, "onde a parábola corta o eixo x", 680, y, 60, "g", COR, a)
    lembrete(c, t, C, "s03", [("s03.a", i1), ("s03.b", i2)], y0=470, dy=250)


# ---------------- módulo ----------------
def b_modulo(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("distância", "g", 84, COR), ("até", "i", 84), ("o", "i", 84), ("zero", "i", 84)], W / 2, 200, "center")
        vx = E.reta(c, t, C["s04.a"] + 0.3, 260, 1660, 560, -8, 8, [-7, 0, 7], E._num, size=52)
        E.saida(c, t, C["s04.c"] - 0.1, lambda: (fx_em(c, t, C["s04.b"], [("|   |", COR)], W / 2, 400, 150, "center"),
                                                  E.frase(c, t, C["s04.b"] + 0.4, ps("duas barras em pé", "i", 56, TINTA2), 1110, 380)))
        E.salto(c, t, C["s04.c"], vx(0), vx(-7), 560, 140, rotulo="7", cor=TINTA)
        fx_em(c, t, C["s04.c"], [("|", COR), ("−7", ENT), ("| = ", COR), ("7", SAI)], 400, 840, 100, "center")
        E.salto(c, t, C["s04.d"], vx(0), vx(7), 560, 140, rotulo="7")
        fx_em(c, t, C["s04.d"], [("|", COR), ("7", ENT), ("| = ", COR), ("7", SAI)], 960, 840, 100, "center")
        E.foco(c, t, C["s04.e"], 0.4, lambda a: c.drawCircle(vx(0), 560, 20, M.paint(COR, a)))
        fx_em(c, t, C["s04.e"], [("|", COR), ("0", ENT), ("| = ", COR), ("0", SAI)], 1520, 840, 100, "center")
        nota(c, t, C["s04.f"], "o módulo nunca dá negativo", W / 2, 980, 52)
        return
    NM = [("|", COR), ("x", ENT), ("| =", COR)]
    por_partes(c, t, C["s05.a"], [([("x", ENT)], [("se ", TINTA2), ("x", ENT), (" ≥ 0", TINTA2)]),
                                  ([("−x", ENT)], [("se ", TINTA2), ("x", ENT), (" < 0", TINTA2)])],
               XE + 60, 330, 110, 300, tl=[C["s05.b"], C["s05.c"]], nome=NM, dy=180)
    E.frase(c, t, C["s05"], [("uma", "i", 66), ("função", "i", 66), ("por", "i", 66), ("partes", "g", 66, COR)], XE, 150)
    fx_em(c, t, C["s05.d"] - 1.4, [("x", ENT), (" = −7", SAI)], XE + 60, 760, 110)
    fx_em(c, t, C["s05.d"], [("−x = −(−7) = ", SAI), ("7", COR)], 760, 760, 110)
    nota(c, t, C["s05.e"], "o menos desfaz o negativo", W / 2, 930, 52)


# ---------------- o V ----------------
PV = (1000, 170, 820, 760, -4, 4, -1, 4)
LINHAS = (("s06.b", "0", "0", ((0, 0),)), ("s06.c", "±1", "1", ((1, 1), (-1, 1))), ("s06.d", "±2", "2", ((2, 2), (-2, 2))),
          ("s06.e", "±3", "3", ((3, 3), (-3, 3))))


def b_ve(c, t, C, b):
    P = E.plano(c, t, C["s06"], *PV, marcas_x=[-3, -2, -1, 1, 2, 3], marcas_y=[1, 2, 3], size=40)
    fx_em(c, t, C["s06.a"], [("y = |", SAI), ("x", ENT), ("|", SAI)], XE, 220, 96)
    q = ep(t, C["s06.a"] + 0.3, 0.5)
    if q > 0:
        fx(c, [("x", ENT)], XE + 120, 340, 64, q, "center")
        fx(c, [("y", SAI)], XE + 420, 340, 64, q, "center")
        M.line(c, XE, 365, XE + 560, 365, TINTA, q, 4)
        M.line(c, XE + 270, 300, XE + 270, 365 + 4 * 120, TINTA, q, 4)
    for i, (k, xs, ys, pts) in enumerate(LINHAS):
        y = 450 + i * 120
        E.foco(c, t, C[k], 0.4, lambda a, xs=xs, ys=ys, y=y: (fx(c, [(xs, ENT)], XE + 120, y, 70, a, "center"),
                                                              fx(c, [(ys, SAI)], XE + 420, y, 70, a, "center")), sobe=6)
        for j, (px, py) in enumerate(pts):
            E.ponto(c, t, C[k] + 0.3 + 0.2 * j, P, px, py, cor=COR)
    ve_cresce(c, t, C["s07.a"], P, 0, 0, COR)
    if t >= C["s07.b"]:
        anel(c, t, C["s07.b"], *P(0, 0))
        nota(c, t, C["s07.b"], "vértice", P.x(0), P.y(0) + 120, 46, fundo=TINTA)
    E.foco(c, t, C["s07.c"], 0.4, lambda a: (fx(c, [("y = x", COR)], *P(2.3, 3.6), 52, a),
                                             fx(c, [("y = −x", COR)], P.x(-1.6), P.y(3.6), 52, a, "right")))
    E.foco(c, t, C["s07.c"] + 0.6, 0.4, lambda a: E.pilula(c, "as duas linhas da chave", 560, 1000, 46, "g", fundo=COR, a=a))


# ---------------- deslocar ----------------
PD = (1000, 150, 820, 800, -3, 6, -1, 6)


def b_desloca(c, t, C, b):
    P = E.plano(c, t, C["s08"], *PD, marcas_x=[-2, -1, 1, 2, 3, 4, 5], marcas_y=[1, 2, 3, 4, 5], size=40)
    tenue(c, 0.3, lambda: ve(c, P, 0, 0, TINTA2, 1.0, 5))
    k = ease_io(prog(t, C["s08.b"] + 0.3, 0.9))
    h = 2 * ease_io(prog(t, C["s08.c"] + 0.3, 1.1))
    if t >= C["s08.a"]:
        ve(c, P, h, k, COR, ep(t, C["s08.a"], 0.5))
    S, Y = 104, 260
    partes = [("y = |", SAI), ("x", ENT), (" ", SAI), ("− 2", COR), ("|", SAI), ("  ", SAI), ("+ 1", COR)]
    w, xs, ws = fx(c, partes, XE, Y, S, 0)
    fx_em(c, t, C["s08.a"], partes, XE, Y, S)
    caixa(c, xs[6], Y, ws[6], S, ep(t, C["s08.b"], 0.4))
    caixa(c, xs[3], Y, ws[3], S, ep(t, C["s08.c"], 0.4))

    def s08():
        E.frase(c, t, C["s08.b"], [("+1", "g", 76, COR), ("fora:", "i", 70), ("sobe", "g", 76), ("1", "g", 76)], XE, 440)
        E.frase(c, t, C["s08.c"], [("−2", "g", 76, COR), ("dentro:", "i", 70), ("direita", "g", 76), ("2", "g", 76)], XE, 580)
        E.foco(c, t, C["s08.d"], 0.5, lambda a: (E.escreve(c, "vértice", XE, 740, 66, "i", TINTA, a),
                                                 fx(c, [("(", TINTA), ("2", ENT), (", ", TINTA), ("1", SAI), (")", TINTA)], XE + 260, 745, 96, a)))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t >= C["s08.d"]:
        E.ponto(c, t, C["s08.d"], P, 2, 1, cor=COR)
        anel(c, t, C["s08.d"], *P(2, 1))
    if t < C["s09"]:
        return
    fx_em(c, t, C["s09.a"], [("x = 2:  |0| + 1 = ", SAI), ("1", COR)], XE, 470, 80)
    E.frase(c, t, C["s09.b"], [("o", "i", 64), ("menor", "g", 64, COR), ("valor:", "i", 64), ("módulo", "i", 64), ("≥ 0", "g", 64)], XE, 600)
    fx_em(c, t, C["s09.c"], [("x = 0", ENT), (" e ", TINTA2), ("x = 4", ENT), (":  y = ", SAI), ("3", COR)], XE, 750, 72)
    E.ponto(c, t, C["s09.c"] + 0.3, P, 0, 3, cor=SAI)
    E.ponto(c, t, C["s09.c"] + 0.5, P, 4, 3, cor=SAI)
    q = ep(t, C["s09.c"] + 0.8, 0.5)
    if q > 0:
        M.line(c, P.x(0), P.y(3), P.x(4), P.y(3), TINTA2, q, 4, dash=E.TRACO)
        M.line(c, P.x(2), P.y(1), P.x(2), P.y(5.5), TINTA2, q, 4, dash=E.TRACO)
    nota(c, t, C["s09.c"] + 1.0, "simétrico", 560, 900, 48, fundo=TINTA)


# ---------------- rebater ----------------
PR = (1000, 140, 820, 820, -4, 4, -5, 5)
par4 = lambda x: x * x - 4


def b_rebate(c, t, C, b):
    P = E.plano(c, t, C["s10"], *PR, marcas_x=[-3, -2, -1, 1, 2, 3], marcas_y=[-4, -2, 2, 4], size=40)
    p = ease_io(prog(t, C["s11.c"], 1.4))
    if t >= C["s11.a"]:
        # fora de [−2, 2] fica igual; dentro, achata e vira
        traco(c, P, amostra(par4, -3.4, -2), COR)
        traco(c, P, amostra(par4, 2, 3.4), COR)
        cor = ERRADO if p < 0.5 and t >= C["s11.b"] else COR
        traco(c, P, amostra(lambda x: lerp(par4(x), abs(par4(x)), p), -2, 2), cor)
        if p > 0:
            tenue(c, 0.35 * (1 - ep(t, C["s11.d"] + 1.0, 0.6)), lambda: traco(c, P, amostra(par4, -2, 2), TINTA2, 1.0, 5, E.TRACO))
    else:
        E.curva(c, t, C["s10.b"], P, par4, -3.4, 3.4, d=1.2, cor=COR)
    q = ep(t, C["s11.a"], 0.4) * (1 - ep(t, C["s11.c"], 0.4))
    if q > 0:
        M.rrect(c, P.x(-4), P.y(5), P.caixa[2], P.y(0) - P.y(5), 0, CERTO, 0.08 * q)
    q = ep(t, C["s11.b"], 0.4) * (1 - ep(t, C["s11.c"], 0.4))
    if q > 0:
        M.rrect(c, P.x(-2), P.y(0), P.x(2) - P.x(-2), P.y(-4.2) - P.y(0), 0, ERRADO, 0.1 * q)
    for i, v in enumerate((-2, 2)):
        E.ponto(c, t, C["s10.c"] + 0.4 * i, P, v, 0, cor=SAI)
    if t < C["s11.c"]:
        E.ponto(c, t, C["s10.d"], P, 0, -4, cor=SAI)
    else:
        E.ponto(c, t, C["s11.d"], P, 0, 4, cor=COR)
        anel(c, t, C["s11.d"], *P(0, 4))

    def s10():
        E.frase(c, t, C["s10.a"], [("o", "i", 74), ("módulo", "g", 76, COR), ("dobra", "i", 74), ("gráficos", "i", 74)], XE, 230)
        fx_em(c, t, C["s10.b"], [("y = ", SAI), ("x", ENT), ("^2", ENT), (" − 4", SAI)], XE, 420, 110)
        E.foco(c, t, C["s10.c"], 0.5, lambda a: (E.escreve(c, "raízes:", XE, 580, 62, "i", TINTA2, a),
                                                 fx(c, [("−2 e 2", SAI)], XE + 240, 585, 80, a)))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: (E.escreve(c, "eixo y:", XE, 720, 62, "i", TINTA2, a),
                                                 fx(c, [("−4", SAI)], XE + 240, 725, 80, a)))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    fx_em(c, t, C["s11"], [("y = |", COR), ("x", ENT), ("^2", ENT), (" − 4", SAI), ("|", COR)], XE, 260, 110)
    E.frase(c, t, C["s11.a"], [("acima", "g", 68, CERTO), ("do", "i", 66), ("eixo:", "i", 66), ("fica", "i", 66)], XE, 440)
    E.frase(c, t, C["s11.b"], [("abaixo:", "g", 68, ERRADO), ("vira", "i", 66), ("positivo", "i", 66)], XE, 560)
    E.frase(c, t, C["s11.c"], [("rebate", "g", 90, COR), ("para", "i", 84), ("cima", "i", 84)], XE, 710)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: fx(c, [("−4", SAI), ("  →  ", TINTA2), ("4", COR)], XE, 870, 100, a))


# ---------------- erro ----------------
PE = (980, 250, 840, 640, -4, 4, -1, 4)


def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("cuidado:", "g", 90, ERRADO), ("o", "i", 86), ("lado", "i", 86), ("errado", "g", 90)], W / 2, 170, "center")
    P = E.plano(c, t, C["s12"], *PE, marcas_x=[-3, -2, -1, 1, 2, 3], marcas_y=[1, 2, 3], size=38)
    fx_em(c, t, C["s12"] + 0.3, [("y = |", SAI), ("x", ENT), (" − 2", COR), ("|", SAI)], XE, 380, 110)
    certo = C["s13.a"]
    if t >= C["s12.b"]:
        E.saida(c, t, certo + 1.2, lambda: (ve(c, P, -2, 0, ERRADO, ep(t, C["s12.b"], 0.5)),
                                            E.foco(c, t, C["s12.b"] + 0.3, 0.4, lambda a: E.selo(c, P.x(-2), P.y(0) + 70, 40, False, a))))
        E.saida(c, t, certo - 0.1, lambda: E.frase(c, t, C["s12.b"], [("leva", "i", 70), ("para", "i", 70), ("a", "i", 70),
                                                                      ("esquerda", "g", 72, ERRADO)], XE, 560))
    if t >= certo:
        ve(c, P, 2, 0, CERTO, ep(t, certo + 0.6, 0.5))
        E.foco(c, t, certo + 0.9, 0.4, lambda a: E.selo(c, P.x(2), P.y(0) + 70, 40, True, a))
    fx_em(c, t, certo, [("x − 2 = 0", SAI), ("  →  ", TINTA2), ("x = 2", CERTO)], XE, 580, 90)
    nota(c, t, C["s13.b"], "dentro: menos vai para a direita", 520, 780, 44, fundo=TINTA)
    nota(c, t, C["s13.b"] + 1.6, "mais vai para a esquerda", 460, 890, 44, fundo=TINTA)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14.a"], [("o", "i", 84, CLARO), ("vértice", "g", 90, BR), ("está", "i", 84, CLARO), ("onde", "i", 84, CLARO)],
                W / 2, 220, "center")
        E.frase(c, t, C["s14.a"] + 0.9, [("o", "i", 84, CLARO), ("de", "i", 84, CLARO), ("dentro", "g", 90, BR), ("zera", "g", 90, BR)],
                W / 2, 330, "center")
        S, Y = 140, 560
        partes = [("y = |", BR), (" x − 2 ", CLARO), ("|  ", BR), ("+ 1", CLARO)]
        w, xs, ws = fx(c, partes, W / 2, Y, S, 0, "center")
        fx_em(c, t, C["s14.a"] + 1.6, partes, W / 2, Y, S, "center")
        caixa(c, xs[1], Y, ws[1], S, ep(t, C["s14.b"], 0.4), CLARO)
        caixa(c, xs[3], Y, ws[3], S, ep(t, C["s14.c"], 0.4), BR)
        E.foco(c, t, C["s14.b"] + 0.4, 0.4, lambda a: fx(c, [("= 0  →  x = 2", CLARO)], xs[1] + ws[1] / 2, Y + 150, 64, a, "center"))
        E.foco(c, t, C["s14.c"] + 0.4, 0.4, lambda a: fx(c, [("y = 1", BR)], xs[3] + ws[3] / 2, Y + 150, 64, a, "center"))
        E.foco(c, t, C["s14.d"], 0.5, lambda a: (E.escreve(c, "vértice", 600, 930, 80, "i", CLARO, a),
                                                 fx(c, [("(2, 1)", BR)], 900, 935, 120, a)))
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("o", "i", 96, CLARO), ("menor", "i", 96, CLARO), ("módulo", "g", 100, BR), ("é", "i", 96, CLARO), ("zero", "g", 100, BR)],
            W / 2, 300, "center")
    E.frase(c, t, C["s15.a"] + 1.0, [("ali", "i", 96, CLARO), ("fica", "i", 96, CLARO), ("a", "i", 96, CLARO), ("ponta", "g", 100, BR), ("do", "i", 96, CLARO),
                                     ("V", "g", 100, BR)], W / 2, 450, "center")
    nota(c, t, C["s15.b"], "com x² dentro, não vale: zera em dois lugares", W / 2, 700, 50, fundo=BR, cor="#07070F")
    q = ep(t, C["s15.b"] + 0.6, 0.5)
    if q > 0:
        P = E.Plano(760, 780, 400, 240, -3, 3, 0, 5)
        traco(c, P, amostra(lambda x: abs(x * x - 4), -2.9, 2.9), CLARO, q, 7)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    fx_em(c, t, C["s16.a"], [("y = |", SAI), ("x", ENT), (" + 3", SAI), ("| − 2", SAI)], XE, 440, 130)
    E.frase(c, t, C["s16.b"], [("onde", "i", 84), ("fica", "i", 84), ("o", "i", 84), ("vértice?", "g", 84, COR)], XE, 680)
    E.frase(c, t, C["s16.c"], [("onde", "i", 84), ("corta", "i", 84), ("o", "i", 84), ("eixo", "i", 84), ("y?", "g", 84, COR)], XE, 840)
    questao_relogio(c, t, C, "s17")


# ---------------- resposta ----------------
PQ = (1040, 160, 780, 780, -6, 2, -3, 4)


def b_resposta(c, t, C, b):
    P = E.plano(c, t, C["s18"], *PQ, marcas_x=[-5, -4, -3, -2, -1, 1], marcas_y=[-2, -1, 1, 2, 3], size=38)
    ve_cresce(c, t, C["s18.c"], P, -3, -2, COR)
    E.ponto(c, t, C["s18.c"], P, -3, -2, "(−3, −2)", cor=COR, lado=(0, 1))
    if t >= C["s18.c"]:
        anel(c, t, C["s18.c"], *P(-3, -2))
    E.ponto(c, t, C["s19.c"], P, 0, 1, "(0, 1)", cor=SAI, lado=(1, 0))
    if t >= C["s19.c"]:
        anel(c, t, C["s19.c"], *P(0, 1))
    fx_em(c, t, C["s18"], [("y = |", SAI), ("x", ENT), (" + 3", SAI), ("| − 2", SAI)], XE, 200, 84)
    fx_em(c, t, C["s18.a"], [("x + 3 = 0", SAI), ("  →  ", TINTA2), ("x = −3", COR)], XE, 340, 76)
    fx_em(c, t, C["s18.b"], [("fora: ", TINTA2), ("y = −2", COR)], XE, 460, 76)
    E.frase(c, t, C["s18.c"] + 0.8, ps("3 para a esquerda, 2 para baixo", "i", 52, TINTA2), XE, 560, passo=0.1)
    fx_em(c, t, C["s19.a"], [("x = 0", ENT)], XE, 700, 76)
    fx_em(c, t, C["s19.b"], [("→  |3| − 2 = ", SAI), ("1", COR)], XE + 250, 700, 76)
    nota(c, t, C["s19.d"], "o −2 de fora: ponta abaixo do eixo x", 520, 880, 44, fundo=TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.saida(c, t, C["s21"] - 0.1, lambda: resumo(c, t, C, "s20", [
        ("s20.a", [("módulo", "g", 88, COR), ("=", "i", 84), ("distância", "i", 84), ("até", "i", 84), ("o", "i", 84), ("zero", "i", 84)]),
        ("s20.b", [("o", "i", 84), ("gráfico", "i", 84), ("é", "i", 84), ("um", "i", 84), ("V", "g", 88, COR)]),
        ("s20.c", [("vértice:", "i", 84), ("onde", "i", 84), ("o", "i", 84), ("de", "i", 84), ("dentro", "i", 84), ("zera", "g", 88, COR)])]))
    if t < C["s21"]:
        return
    proxima(c, t, C, "s21.a", "equações e", "inequações", [("com", "i", 70), ("módulo", "g", 76, COR)], "s21.b", "s21.c", "s21.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, modulo=b_modulo, ve=b_ve, desloca=b_desloca, rebate=b_rebate, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
