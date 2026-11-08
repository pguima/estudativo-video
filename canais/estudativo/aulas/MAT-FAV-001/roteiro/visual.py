"""Visual — Estudativo · MAT-FAV-001: função definida por partes.

Linguagem visual da trilha Funções Avançadas (vem da trilha Funções): x e entrada em índigo (ENT), saída e f(x) em preto (SAI);
condições em cinza; a chave da função por partes (por_partes()) com a lei à esquerda e a condição à direita; plano à direita e texto
à esquerda. Nesta aula: a reta das faixas do frete; o plano com o pedaço de reta 2x (índigo) e a reta deitada 9 (preto), bolinha
cheia = o ponto entra, vazia = não entra; o salto como seta dupla na fronteira. Palco escuro só no atalho."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-001_funcao_definida_por_partes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "grafico", "atalho", "questao", "fim"))
BR = "#FFFFFF"

F = lambda x: 2 * x if 0 < x <= 3 else 9
Q = lambda x: x + 4 if x < 1 else 3 * x
assert (F(2), F(5), F(3)) == (4, 9, 6) and 2 * 5 == 10 and 2 * 3 == 6
assert (Q(-2), Q(1), Q(4)) == (2, 3, 12) and 1 + 4 == 5 and 3 * 1 == 3

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


NOME = [("f(", SAI), ("x", ENT), (") =", SAI)]
FRETE = [([("2", SAI), ("x", ENT)], [("se 0 < ", TINTA2), ("x", ENT), (" ≤ 3", TINTA2)]),
         ([("9", SAI)], [("se ", TINTA2), ("x", ENT), (" > 3", TINTA2)])]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01.a"], [("o", "i", 80), ("frete", "g", 90, COR)], XE, 220)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (E.escreve(c, "até 3 kg", XE, 400, 76, "g", TINTA, a),
                                                 E.escreve(c, "R$ 2 por kg", XE + 380, 400, 76, "i", COR, a)))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (E.escreve(c, "acima de 3 kg", XE, 540, 76, "g", TINTA, a),
                                                 E.escreve(c, "R$ 9 fixos", XE + 560, 540, 76, "i", TINTA, a)))
        # a caixa de 5 kg
        def pacote(a):
            k = ease_back(prog(t, C["s01.d"], 0.6))
            cx, cy, s = 1500, 420, 300 * k
            M.rrect(c, cx - s / 2, cy - s / 2, s, s, 26, COR, a)
            M.line(c, cx - s / 2, cy - s * 0.18, cx + s / 2, cy - s * 0.18, BR, 0.5 * a, 6)
            centro(c, "5 kg", cx, cy + s * 0.2, 96 * k, "g", BR, a)
        E.foco(c, t, C["s01.d"], 0.5, pacote)
        E.foco(c, t, C["s01.d"] + 0.4, 0.4, lambda a: centro(c, "quanto custa?", 1500, 680, 64, "i", TINTA, a))
        fx_em(c, t, C["s01.e"], [("2 · 5 = 10", ERRADO)], XE, 800, 120)
        if t >= C["s01.e"] + 0.9:
            E.risco(c, XE - 20, 830, XE + 660, 700, t, C["s01.e"] + 0.9, largura=14)
        E.frase(c, t, C["s01.e"] + 1.6, [("depois", "i", 70), ("de", "i", 70), ("3", "g", 70, COR), ("kg,", "i", 70), ("a", "i", 70),
                                         ("regra", "i", 70), ("é", "i", 70), ("outra", "g", 70, COR)], XE, 960)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02.a"], C["s02.end"], [(C["s02.a"] + 1.4, [("calcular", "g", 120, COR)]),
                                              (C["s02.b"], [("o", "i", 110), ("gráfico", "g", 120, COR)]),
                                              (C["s02.b"] + 0.6, [("em", "i", 110), ("pedaços", "g", 120)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def i1(a, y):
        E.escreve(c, "intervalos:", 430, y, 70, "i", TINTA, a)
        x0 = 860
        M.line(c, x0, y - 22, x0 + 420, y - 22, COR, a, 12)
        c.drawCircle(x0, y - 22, 17, M.paint(COR, a))
        c.drawCircle(x0 + 420, y - 22, 17, M.paint(E.PAPEL, a))
        c.drawCircle(x0 + 420, y - 22, 17, M.paint(COR, a, stroke=6))
        E.escreve(c, "cheia entra, vazia não", 1340, y, 52, "i", TINTA2, a)

    def i2(a, y):
        fx(c, [("f(", SAI), ("2", ENT), (")", SAI)], 430, y, 96, a)
        E.escreve(c, "troque o x pelo 2", 720, y, 62, "i", TINTA2, a)

    def i3(a, y):
        E.escreve(c, "função afim:", 430, y, 70, "i", TINTA, a)
        E.escreve(c, "uma reta", 860, y, 76, "g", COR, a)
    lembrete(c, t, C, "s03", [("s03.a", i1), ("s03.b", i2), ("s03.c", i3)])


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("função", "i", 110), ("definida", "i", 110)], W / 2, 330, "center")
        E.frase(c, t, C["s04.a"] + 0.7, [("por", "i", 130), ("partes", "g", 140, COR)], W / 2, 490, "center")
        E.frase(c, t, C["s04.a"] + 1.6, ps("mais de uma lei, cada uma na sua faixa", "i", 56, TINTA2), W / 2, 600, "center", passo=0.1)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: (fx(c, [("x", ENT)], 560, 820, 110, a, "center"),
                                                 E.escreve(c, "peso (kg)", 520, 920, 56, "i", TINTA2, a)))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: (fx(c, NOME[:2] + [(")", SAI)], 1360, 820, 110, a, "center"),
                                                 E.escreve(c, "preço (R$)", 1250, 920, 56, "i", TINTA2, a)))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("na", "i", 72), ("prova:", "i", 72), ("uma", "i", 72), ("chave", "g", 72, COR)], XE, 200)
    ys, xx = por_partes(c, t, C["s05.a"], FRETE, 300, 470, 110, 360, tl=[C["s05.b"], C["s05.c"]], nome=NOME, dy=200)
    q = ep(t, C["s05.d"], 0.5)
    if q > 0:
        E.caixa_pontilhada(c, xx + 340, ys[0] - 110, 640, 340, q, COR, q)
        nota(c, t, C["s05.d"] + 0.2, "diz qual lei usar", xx + 660, ys[1] + 150, 50)


# ---------------- calcular ----------------
RX0, RX1, RY = 300, 1620, 690


def b_calcular(c, t, C, b):
    def luz(i):
        if i == 0:
            return ep(t, C["s07.a"], 0.3) * (1 - ep(t, C["s07.c"] - 0.2, 0.3))
        return ep(t, C["s07.c"], 0.3)
    por_partes(c, t, C["s06"] - 0.4, FRETE, XE, 200, 74, 230, nome=NOME, dy=120, luz=luz)
    item(c, t, C["s06.a"], 1, 1080, 230, 44)
    E.frase(c, t, C["s06.a"] + 0.1, ps("veja a faixa do x", "i", 60), 1150, 230)
    item(c, t, C["s06.b"], 2, 1080, 350, 44)
    E.frase(c, t, C["s06.b"] + 0.1, [("use", "i", 60), ("só", "i", 60), ("a", "i", 60), ("lei", "g", 60, COR), ("dela", "i", 60)], 1150, 350)
    # a reta das faixas
    vx = E.reta(c, t, C["s06.a"], RX0, RX1, RY, 0, 6, list(range(0, 7)), E._num, size=48)
    q = ep(t, C["s06.a"] + 0.4, 0.6)
    if q > 0:
        M.rrect(c, vx(0), RY - 70, vx(3) - vx(0), 50, 12, COR, 0.85 * q)
        M.rrect(c, vx(3), RY - 70, RX1 + 40 - vx(3), 50, 12, TINTA, 0.85 * q)
        fx(c, [("2x", BR)], (vx(0) + vx(3)) / 2, RY - 30, 40, q, "center")
        fx(c, [("9", BR)], (vx(3) + RX1) / 2, RY - 30, 40, q, "center")

    def marca(v, t0, cor):
        p = ease_back(prog(t, t0, 0.5))
        if p > 0:
            X, Y = vx(v), RY - 100
            pa = skia.Path(); pa.moveTo(X, Y + 20); pa.lineTo(X - 22 * p, Y - 20 * p); pa.lineTo(X + 22 * p, Y - 20 * p); pa.close()
            c.drawPath(pa, M.paint(cor))
            anel(c, t, t0, vx(v), RY)

    def conta1():
        marca(2, C["s07.a"], COR)
        fx_em(c, t, C["s07.a"], [("f(", SAI), ("2", ENT), (")", SAI)], 560, 930, 110)
        fx_em(c, t, C["s07.b"], [(" = 2 · 2 = ", SAI), ("4", COR)], 790, 930, 110)
    if t >= C["s07"]:
        E.saida(c, t, C["s07.c"] - 0.1, conta1)
    if t >= C["s07.c"]:
        marca(5, C["s07.c"], TINTA)
        fx_em(c, t, C["s07.c"], [("f(", SAI), ("5", ENT), (")", SAI)], 560, 930, 110)
        fx_em(c, t, C["s07.d"], [(" = ", SAI), ("9", COR)], 790, 930, 110)
        E.frase(c, t, C["s07.d"] + 0.8, ps("nem tem conta", "i", 60, TINTA2), 1130, 920)


# ---------------- gráfico ----------------
PB = (980, 130, 820, 840, -1, 6.5, -1, 11)


def plano_frete(c, t, t0):
    return E.plano(c, t, t0, *PB, marcas_x=[1, 2, 3, 4, 5, 6], marcas_y=[3, 6, 9], size=40, nomes=("x", "f(x)"))


def desenho_frete(c, t, P, tr1, tr2, tb=None, tz=None, tc=None, tv=None):
    """pedaço 2x de 0 a 3 e a reta 9 depois do 3"""
    if tr1 is not None:
        E.curva(c, t, tr1, P, lambda x: 2 * x, 0, 3, d=0.9, cor=ENT, largura=8)
    if tr2 is not None:
        E.curva(c, t, tr2, P, lambda x: 9, 3, 6.5, d=0.8, cor=SAI, largura=8)
    if tz is not None:
        bolinha_em(c, t, tz, P, 0, 0, False, ENT)
    if tc is not None:
        bolinha_em(c, t, tc, P, 3, 6, True, ENT)
    if tv is not None:
        bolinha_em(c, t, tv, P, 3, 9, False, SAI)


def b_grafico(c, t, C, b):
    P = plano_frete(c, t, C["s08"])
    # 2x inteira, tracejada, e depois só o pedaço
    k = ep(t, C["s08.b"], 0.4) * (1 - ep(t, C["s08.c"] + 0.6, 0.6))
    tenue(c, k * 0.5, lambda: E.curva(c, t, C["s08.b"], P, lambda x: 2 * x, -0.5, 6, d=0.9, cor=ENT, largura=5, tracejada=True))
    if t >= C["s08.c"]:
        q = ep(t, C["s08.c"], 0.4)
        M.rrect(c, P.x(0), P.caixa[1], P.x(3) - P.x(0), P.caixa[3], 0, COR, 0.06 * q)
    tv = C["s10.d"]
    desenho_frete(c, t, P, C["s08.c"], C["s09.a"], tz=C["s10.e"], tc=C["s10.c"], tv=tv)
    if t >= C["s09.b"]:
        M.line(c, P.x(3), P.y(-0.6), P.x(3), P.y(10.6), TINTA2, 0.8, 4, dash=E.TRACO, progress=ep(t, C["s09.b"], 0.5))
    # o salto
    q = ep(t, C["s09.c"], 0.5) * (1 - ep(t, C["s10.c"] - 0.3, 0.4))
    if q > 0:
        X = P.x(3) - 46
        M.arrow(c, X, P.y(6), X, P.y(9) + 6, ERRADO, q, 6, 18, q)
        nota(c, t, C["s09.c"] + 0.2, "salto", X - 110, P.y(7.5), 44, fundo=ERRADO)

    # texto à esquerda
    def s08():
        E.frase(c, t, C["s08.a"], ps("cada lei só", "i", 72), XE, 260)
        E.frase(c, t, C["s08.a"] + 0.6, [("na", "i", 72), ("sua", "i", 72), ("faixa", "g", 76, COR)], XE, 360)
        fx_em(c, t, C["s08.b"], [("2", SAI), ("x", ENT)], XE, 540, 120)
        E.frase(c, t, C["s08.b"] + 0.4, ps("é uma reta", "i", 70), XE + 230, 530)
        E.frase(c, t, C["s08.c"], [("só", "i", 70), ("de", "i", 70), ("0", "g", 72, COR), ("até", "i", 70), ("3", "g", 72, COR)], XE, 700)
    E.saida(c, t, C["s09"] - 0.1, s08)

    def s09():
        fx_em(c, t, C["s09.a"], [("9", SAI)], XE, 300, 140)
        E.frase(c, t, C["s09.a"] + 0.4, ps("reta deitada", "i", 70), XE + 130, 290)
        E.frase(c, t, C["s09.b"], [("depois", "i", 70), ("do", "i", 70), ("3", "g", 76, COR)], XE, 450)
        E.frase(c, t, C["s09.c"], [("pula", "i", 74), ("de", "i", 74), ("6", "g", 80, COR), ("para", "i", 74), ("9", "g", 80)], XE, 640)
    if t >= C["s09"]:
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], ps("quem fica com a fronteira?", "i", 62), XE, 230)
    fx_em(c, t, C["s10.b"], [("x", ENT), (" ≤ 3", TINTA2)], XE, 380, 96)
    E.frase(c, t, C["s10.b"] + 0.4, ps("o 3 entra", "i", 60, CERTO), XE + 330, 375)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: (c.drawCircle(XE + 30, 500, 22, M.paint(ENT, a)),
                                             E.escreve(c, "cheia em (3, 6)", XE + 80, 520, 60, "g", TINTA, a)))
    fx_em(c, t, C["s10.d"] - 0.6, [("x", ENT), (" > 3", TINTA2)], XE, 670, 96)
    E.frase(c, t, C["s10.d"] - 0.2, ps("o 3 não entra", "i", 60, ERRADO), XE + 330, 665)

    def vazia(a, y, txt):
        c.drawCircle(XE + 30, y - 20, 22, M.paint(E.PAPEL, a))
        c.drawCircle(XE + 30, y - 20, 22, M.paint(SAI, a, stroke=6))
        E.escreve(c, txt, XE + 80, y, 60, "g", TINTA, a)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: vazia(a, 790, "vazia em (3, 9)"))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: vazia(a, 920, "vazia em (0, 0)"))
    for k, (x, y) in (("s10.c", (3, 6)), ("s10.d", (3, 9)), ("s10.e", (0, 0))):
        anel(c, t, C[k], *P(x, y))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 100, ERRADO), ("na", "i", 96), ("fronteira", "g", 100)], W / 2, 190, "center")
    S, Y = 130, 430
    fx_em(c, t, C["s11.b"], [("f(", SAI), ("3", ENT), (") = ", SAI)], 560, Y, S)
    certo = C["s12.c"]
    E.saida(c, t, certo - 0.1, lambda: (fx_em(c, t, C["s11.c"], [("9", ERRADO)], 990, Y, S),
                                        E.frase(c, t, C["s11.c"] + 0.5, ps("pacote grande?", "i", 60, ERRADO), 1130, Y - 20)))
    fx_em(c, t, certo, [("2 · 3 = ", SAI), ("6", CERTO)], 990, Y, S)
    # as duas condições
    def cond(a, x, partes, txt, cor, ok):
        fx(c, partes, x, 700, 100, a, "center")
        E.centro(c, txt, x, 800, 56, "i", cor, a)
        E.selo(c, x + 260, 670, 40, ok, a)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: cond(a, 560, [("x", ENT), (" > 3", TINTA2)], "não aceita o 3", ERRADO, False))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: cond(a, 1340, [("0 < ", TINTA2), ("x", ENT), (" ≤ 3", TINTA2)], "aceita o 3", CERTO, True))
    nota(c, t, C["s12.d"], "quem decide: o sinal com o igual", W / 2, 950, 54)


# ---------------- atalho (palco) ----------------
def mini(c, x, y, salto, cor, a):
    """dois pedaços que se encontram (salto=False) ou não, numa caixinha de 360 x 220"""
    if a <= 0:
        return
    M.line(c, x, y + 200, x + 380, y + 200, CLARO, a * 0.6, 4)
    M.line(c, x, y + 200, x, y - 10, CLARO, a * 0.6, 4)
    xm = x + 180
    M.line(c, x + 20, y + 180, xm, y + 90, cor, a, 8)
    y2 = y + 20 if salto else y + 90
    M.line(c, xm, y2, x + 360, y2 - (0 if salto else 50), BR, a, 8)
    c.drawCircle(xm, y + 90, 13, M.paint(cor, a))
    if salto:
        c.drawCircle(xm, y2, 13, M.paint("#07070F", a))
        c.drawCircle(xm, y2, 13, M.paint(BR, a, stroke=5))


def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13.a"], [("na", "i", 84, CLARO), ("fronteira,", "g", 88, BR)], W / 2, 210, "center")
        E.frase(c, t, C["s13.a"] + 0.8, [("calcule", "i", 84, CLARO), ("as", "i", 84, CLARO), ("duas", "g", 88, BR), ("leis", "g", 88, BR)],
                W / 2, 320, "center")
        fx_em(c, t, C["s13.b"], [("2 · 3 = 6", CLARO)], 560, 520, 120, "center")
        fx_em(c, t, C["s13.c"], [("9", BR)], 1360, 520, 120, "center")
        E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: E.centro(c, "≠", 960, 520, 120, "g", BR, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: (mini(c, 380, 650, True, CLARO, a), E.centro(c, "diferente: salto", 570, 960, 64, "g", BR, a)))
        E.foco(c, t, C["s13.e"], 0.5, lambda a: (mini(c, 1160, 650, False, CLARO, a),
                                                 E.centro(c, "igual: sem salto", 1350, 960, 64, "g", CLARO, a)))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("pedaço", "i", 90, CLARO), ("de", "i", 90, CLARO), ("reta:", "i", 90, CLARO)], W / 2, 300, "center")
    E.frase(c, t, C["s14.a"] + 0.8, [("só", "i", 120, CLARO), ("as", "i", 120, CLARO), ("pontas", "g", 130, BR)], W / 2, 460, "center")
    E.foco(c, t, C["s14.b"], 0.5, lambda a: (M.line(c, 640, 640, 1280, 560, CLARO, a, 9),
                                             c.drawCircle(640, 640, 20, M.paint(BR, a)), c.drawCircle(1280, 560, 20, M.paint(BR, a))))
    nota(c, t, C["s14.c"], "pedaço que não é reta: marque pontos no meio", W / 2, 860, 50, fundo=BR, cor="#07070F")


# ---------------- questão ----------------
QL = [([("x + 4", SAI)], [("se ", TINTA2), ("x", ENT), (" < 1", TINTA2)]),
      ([("3", SAI), ("x", ENT)], [("se ", TINTA2), ("x", ENT), (" ≥ 1", TINTA2)])]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    por_partes(c, t, C["s15.a"], QL, XE, 380, 96, 300, tl=[C["s15.a"], C["s15.b"]], nome=NOME, dy=150)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: fx(c, [("f(", SAI), ("−2", ENT), (")    f(", SAI), ("1", ENT), (")    f(", SAI), ("4", ENT),
                                                    (")", SAI)], XE, 790, 92, a))
    E.frase(c, t, C["s15.d"], [("salto", "g", 80, COR), ("em", "i", 80), ("x = 1?", "g", 80)], XE, 940)
    questao_relogio(c, t, C, "s16")


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        por_partes(c, t, C["s17"] - 0.5, QL, XE, 200, 70, 230, nome=NOME, dy=110)
        S = 100
        for y, k0, k1, lin, conta, res in ((480, "s17.a", "s17.b", "1ª linha", "−2 + 4 = ", "2"),
                                           (670, "s17.c", "s17.d", "2ª linha", "3 · 1 = ", "3"),
                                           (860, "s17.e", "s17.f", "2ª linha", "3 · 4 = ", "12")):
            arg = {480: "−2", 670: "1", 860: "4"}[y]
            fx_em(c, t, C[k0], [("f(", SAI), (arg, ENT), (")", SAI)], XE, y, S)
            nota(c, t, C[k0] + 0.3, lin, 680, y - 34, 40, fundo=TINTA)
            fx_em(c, t, C[k1] - 0.6, [(conta, SAI)], 900, y, S)
            E.foco(c, t, C[k1], 0.5, lambda a, res=res, y=y: fx(c, [(res, COR)], 1340, y, S, a))
        nota(c, t, C["s17.c"] + 0.8, "maior ou igual: o 1 entra aqui", 690, 745, 36)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    P = E.plano(c, t, C["s18"], 980, 120, 820, 860, -3.5, 4.5, -1, 13, marcas_x=[-3, -2, -1, 1, 2, 3, 4], marcas_y=[3, 5, 12], size=40,
                nomes=("x", "f(x)"))
    E.curva(c, t, C["s18"] + 0.4, P, lambda x: x + 4, -3.5, 1, d=0.8, cor=SAI)
    E.curva(c, t, C["s18"] + 1.0, P, lambda x: 3 * x, 1, 4.3, d=0.8, cor=ENT)
    bolinha_em(c, t, C["s18.d"], P, 1, 5, False, SAI)
    bolinha_em(c, t, C["s18.e"], P, 1, 3, True, ENT)
    anel(c, t, C["s18.d"], *P(1, 5))
    anel(c, t, C["s18.e"], *P(1, 3))
    E.frase(c, t, C["s18"], ps("na fronteira, x = 1:", "i", 66), XE, 240)
    fx_em(c, t, C["s18.a"], [("1 + 4 = ", SAI), ("5", SAI)], XE, 400, 100)
    fx_em(c, t, C["s18.b"], [("3 · 1 = ", SAI), ("3", COR)], XE, 540, 100)
    E.frase(c, t, C["s18.c"], [("diferente:", "i", 74), ("salto", "g", 80, ERRADO)], XE, 690)
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.escreve(c, "vazia em (1, 5)", XE, 830, 58, "g", TINTA, a))
    E.foco(c, t, C["s18.e"], 0.4, lambda a: E.escreve(c, "cheia em (1, 3)", XE, 940, 58, "g", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.saida(c, t, C["s20"] - 0.1, lambda: resumo(c, t, C, "s19", [
        ("s19.a", [("ache", "i", 84), ("a", "i", 84), ("faixa", "g", 88, COR), ("do", "i", 84), ("x", "g", 88)]),
        ("s19.b", [("use", "i", 84), ("só", "i", 84), ("a", "i", 84), ("lei", "g", 88, COR), ("dela", "i", 84)]),
        ("s19.c", [("fronteira:", "i", 84), ("o", "i", 84), ("sinal", "i", 84), ("com", "i", 84), ("igual", "g", 88, COR)])]))
    if t < C["s20"]:
        return
    proxima(c, t, C, "s20.a", "módulo", "de um número", [("gráfico", "i", 70), ("em", "i", 70), ("V", "g", 76, COR)], "s20.b", "s20.c", "s20.d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, calcular=b_calcular, grafico=b_grafico, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
