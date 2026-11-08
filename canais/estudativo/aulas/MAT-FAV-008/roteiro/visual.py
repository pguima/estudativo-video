"""Visual — Estudativo · MAT-FAV-008: praticando funções modular, composta e inversa.

Linguagem visual da trilha Funções Avançadas (MAT-FAV-001 a 007): x e entrada em índigo (ENT), saída em preto (SAI), condições em
cinza, a chave por_partes(), a reta numérica com centro e raio (MAT-FAV-003), a caixinha do "de dentro" (MAT-FAV-004), a corrente de
operações desfeita de trás para frente (MAT-FAV-006) e a dobra e a meia volta (MAT-FAV-007). Cada situação: enunciado com o relógio
de pausa, e a resposta passo a passo na tela seguinte."""
import math
import re
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções Avançadas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FAV-008_praticando_funcoes_avancadas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"

agua = lambda x: 30 if x <= 10 else 30 + 5 * (x - 10)
assert agua(14) == 50 and agua(10) == 30 and 14 - 10 == 4 and 4 * 5 == 20
assert [x for x in range(-10, 10) if abs(x - 1) <= 3] == [-2, -1, 0, 1, 2, 3, 4] and 4 - (-2) == 6
assert 3 * 6 + 5 == 23 and 3 * 7 + 5 == 26 and all(3 * (u - 1) + 2 + 3 == 3 * u + 2 for u in range(10))
assert 2 * 3 - 5 == 1 and (1 + 5) / 2 == 3
fa, fb, fc = (lambda x: x * x - 2), (lambda x: (x ** 3 - 3 * x) / 1.0), (lambda x: abs(x - 1))
assert all(fa(-x) == fa(x) and fb(-x) == -fb(x) for x in (0.5, 1, 2)) and fc(-1) != fc(1) and fc(-1) != -fc(1)

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



def situacao(c, t, t0, n, txt=None):
    E.frase(c, t, t0, [("situação", "i", 72, COR), (str(n), "g", 80, COR)], XE, 190)
    if txt:
        E.frase(c, t, t0 + 0.5, ps(txt, "i", 54, TINTA2), XE + 380, 185, passo=0.08)


def bola_res(c, t, t0, txt, cx, cy, r=110, cor=CERTO, size=72):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.6)), cor, a), fx(c, [(txt, BR)], cx, cy + size * 0.36, size, a, "center")))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 220, COR), ("situações", "i", 150)], W / 2, 420, "center")
    for i in range(5):
        E.foco(c, t, C["s01.a"] + 0.8 + 0.2 * i, 0.4, lambda a, i=i: (E.bola(c, 560 + i * 200, 610, 60, a=a),
                                                                      E.centro(c, str(i + 1), 560 + i * 200, 636, 70, "g", BR, a)))
    nota(c, t, C["s01.b"], "pause o vídeo e resolva antes da resposta", W / 2, 860, 56)


# ---------------- lembrete ----------------
FERR = (("s02.b", [("a", "i", 64), ("lei", "g", 66, COR), ("certa", "i", 64), ("para", "i", 64), ("cada", "i", 64), ("faixa", "i", 64)]),
        ("s02.c", [("módulo", "g", 66, COR), ("é", "i", 64), ("distância", "i", 64)]),
        ("s02.d", [("composta:", "g", 66, COR), ("de", "i", 64), ("dentro", "i", 64), ("para", "i", 64), ("fora", "i", 64)]),
        ("s02.e", [("inversa:", "g", 66, COR), ("desfaz", "i", 64), ("de", "i", 64), ("trás", "i", 64), ("para", "i", 64), ("frente", "i", 64)]),
        ("s02.f", [("simetria", "g", 66, COR), ("do", "i", 64), ("gráfico", "i", 64)]))


def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 80, TINTA, C["s02"]), ("vai", "i", 80, TINTA, C["s02"] + 0.2), ("usar", "i", 80, TINTA, C["s02"] + 0.4),
                   ("5", "g", 86, COR, C["s02.a"]), ("ferramentas", "i", 80, TINTA, C["s02.a"] + 0.2)], W / 2, 190, "center")
    for i, (k, partes) in enumerate(FERR):
        y = 340 + i * 150
        item(c, t, C[k], i + 1, 420, y, 48)
        E.frase(c, t, C[k] + 0.1, partes, 500, y)


# ---------------- situação 1: por partes ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1, "a conta de água")
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.escreve(c, "até 10 m³:", XE, 380, 72, "g", TINTA, a),
                                             E.escreve(c, "R$ 30 fixos", XE + 420, 380, 72, "i", COR, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: (E.escreve(c, "acima de 10:", XE, 520, 72, "g", TINTA, a),
                                             E.escreve(c, "R$ 30 + R$ 5 por m³", XE + 480, 520, 66, "g", COR, a),
                                             E.escreve(c, "que passar dos 10", XE + 480, 610, 56, "i", TINTA2, a)))
    E.frase(c, t, C["s03.d"], [("gastou", "i", 84), ("14", "g", 96, COR), ("m³:", "g", 84), ("quanto", "i", 84), ("paga?", "g", 90, COR)], XE, 830)
    questao_relogio(c, t, C, "s04", cx=1560, cy=420, r=130)


AG = [([("30", SAI)], [("se 0 ≤ ", TINTA2), ("x", ENT), (" ≤ 10", TINTA2)]),
      ([("30 + 5(", SAI), ("x", ENT), (" − 10)", SAI)], [("se ", TINTA2), ("x", ENT), (" > 10", TINTA2)])]


def b_resposta1(c, t, C, b):
    luz = lambda i: ep(t, C["s05.a"], 0.4) if i == 1 else 0
    por_partes(c, t, C["s05"], AG, XE, 200, 58, 460, nome=[("f(", SAI), ("x", ENT), (") =", SAI)], dy=100, luz=luz)
    fx_em(c, t, C["s05.a"], [("14 > 10:  ", SAI), ("2ª linha", COR)], XE, 470, 70)
    fx_em(c, t, C["s05.b"], [("14 − 10 = 4", SAI)], XE, 600, 76)
    fx_em(c, t, C["s05.c"], [("4 · 5 = 20", SAI)], XE, 720, 76)
    fx_em(c, t, C["s05.d"], [("30 + 20 = ", SAI), ("R$ 50", CERTO)], XE, 840, 76)
    P = E.plano(c, t, C["s05.a"], 1150, 200, 680, 700, 0, 16, 0, 60, passo=2, passo_y=10, marcas_x=[10, 14], marcas_y=[30, 50], size=36,
                nomes=("m³", "R$"))
    E.curva(c, t, C["s05.a"] + 0.3, P, agua, 0, 16, d=1.0, cor=COR)
    if t >= C["s05.d"]:
        E.ponto(c, t, C["s05.d"], P, 14, 50, "(14, 50)", guias=True, cor=CERTO, lado=(-1, -1))
    if t >= C["s05.e"]:
        anel(c, t, C["s05.e"], *P(10, 30))
        E.ponto(c, t, C["s05.e"], P, 10, 30, cor=SAI)
        E.foco(c, t, C["s05.e"] + 0.3, 0.4, lambda a: fx(c, [("fronteira:  30  e  30 + 5 · 0 = 30", SAI)], XE, 970, 54, a))
    nota(c, t, C["s05.f"], "sem salto", P.x(10), P.y(30) + 90, 44, fundo=CERTO)


# ---------------- situação 2: inequação modular ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.b"], [("quantos", "i", 90), ("números", "i", 90), ("inteiros", "g", 96, COR)], XE, 400)
    fx_em(c, t, C["s06.b"] + 1.4, [("|", SAI), ("x", ENT), (" − 1| ≤ 3", SAI)], XE, 620, 150)
    E.frase(c, t, C["s06.b"] + 2.6, ps("satisfazem isso?", "i", 80), XE, 820)
    questao_relogio(c, t, C, "s07", cx=1560, cy=480)


def b_resposta2(c, t, C, b):
    fx_em(c, t, C["s08"], [("|", SAI), ("x", ENT), (" − 1| ≤ 3", SAI)], XE, 200, 90)
    Y = 560
    vx = E.reta(c, t, C["s08"], 260, 1660, Y, -4, 6, list(range(-4, 7)), E._num, size=48)
    E.foco(c, t, C["s08.a"], 0.4, lambda a: c.drawCircle(vx(1), Y, 20, M.paint(TINTA, a)))
    E.foco(c, t, C["s08.a"], 0.5, lambda a: E.escreve(c, "centro 1, raio 3", 760, 200, 64, "i", TINTA2, a))
    E.saida(c, t, C["s08.e"] - 0.1, lambda: (E.salto(c, t, C["s08.b"], vx(1), vx(-2), Y, 120, rotulo="1 − 3 = −2", cor=COR, size=46),
                                             E.salto(c, t, C["s08.c"], vx(1), vx(4), Y, 120, rotulo="1 + 3 = 4", cor=COR, size=46)))
    E.intervalo(c, t, C["s08.d"], vx, Y, -2, 4, True, True)
    nota(c, t, C["s08.d"] + 0.3, "menor ou igual: entre, com as pontas", W / 2, 400, 44, fundo=TINTA)
    if t >= C["s08.e"]:
        for i, v in enumerate(range(-2, 5)):
            ti = C["s08.e"] + 0.35 * i
            q = ep(t, ti, 0.3)
            if q > 0:
                c.drawCircle(vx(v), Y, 26, M.paint(CERTO, q))
                E.centro(c, str(i + 1), vx(v), Y - 50, 44, "g", CERTO, q)
    bola_res(c, t, C["s08.f"], "7", W / 2, 800, 90, CERTO, 90)
    nota(c, t, C["s08.g"], "de ponta a ponta: 6 passos, mas 7 inteiros", W / 2, 980, 48)


# ---------------- situação 3: composta ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C["s09.a"], 3)
    fx_em(c, t, C["s09.b"], [("f(", SAI), ("x + 1", ENT), (") = 3", SAI), ("x", ENT), (" + 5", SAI)], XE, 460, 140)
    fx_em(c, t, C["s09.c"], [("f(7) = ?", COR)], XE, 720, 140)
    questao_relogio(c, t, C, "s10", cx=1560, cy=520)


def b_resposta3(c, t, C, b):
    S, Y = 120, 260
    partes = [("f(", SAI), ("x + 1", ENT), (") = 3", SAI), ("x", ENT), (" + 5", SAI)]
    w, xs, ws = fx(c, partes, XE, Y, S, 0)
    fx_em(c, t, C["s11"], partes, XE, Y, S)
    p = ep(t, C["s11.a"], 0.5)
    if p > 0:
        E.caixa_pontilhada(c, xs[1] - 14, Y - S * 0.88, ws[1] + 28, S * 1.18, p, COR, p)
        E.centro(c, "= 7", xs[1] + ws[1] / 2, Y + 100, 64, "g", COR, p)
    fx_em(c, t, C["s11.b"], [("x + 1 = 7  →  ", SAI), ("x = 6", COR)], XE, 500, 84)
    fx_em(c, t, C["s11.c"], [("3 · 6 + 5 = 23", SAI)], XE, 640, 84)
    bola_res(c, t, C["s11.d"], "f(7) = 23", 1500, 560, 170, CERTO, 64)
    fx_em(c, t, C["s11.e"], [("errado:  3 · 7 + 5 = ", ERRADO)], XE, 860, 70)
    fx_em(c, t, C["s11.f"], [("26", ERRADO)], XE + 720, 860, 70)
    if t >= C["s11.f"] + 0.5:
        E.risco(c, XE - 10, 880, XE + 830, 800, t, C["s11.f"] + 0.5, largura=10)
    nota(c, t, C["s11.f"] + 1.0, "o 7 é o de dentro, não o x", 1400, 960, 46, fundo=TINTA)


# ---------------- situação 4: inversa ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C["s12.a"], 4)
    fx_em(c, t, C["s12.b"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("f{x + 5}{2}", SAI)], XE, 480, 140)
    E.frase(c, t, C["s12.c"], [("a", "i", 80), ("inversa", "g", 86, COR), ("e", "i", 80)], XE, 720)
    fx_em(c, t, C["s12.c"] + 1.0, [("f", SAI), ("^{−1}", COR), ("(3) = ?", SAI)], XE, 880, 110)
    questao_relogio(c, t, C, "s13", cx=1560, cy=520)


def b_resposta4(c, t, C, b):
    fx_em(c, t, C["s14"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("f{x + 5}{2}", SAI)], XE, 230, 90)

    def corrente(y, ops, ts, cor, sentido, ini, fim):
        x0, passo = 520, 380
        xs = [x0 + i * passo for i in range(3)] if sentido > 0 else [x0 + (2 - i) * passo for i in range(3)]
        E.foco(c, t, ts[0], 0.4, lambda a: E.centro(c, ini, xs[0], y + 30, 80, "g", ENT, a))
        for i, (op, ti) in enumerate(zip(ops, ts)):
            q = ep(t, ti, 0.5)
            if q > 0:
                xa, xb = xs[i] + 60 * sentido, xs[i + 1] - 60 * sentido
                M.arrow(c, xa, y, lerp(xa, xb, q), y, cor, 1.0, 6, 22, q)
                E.pilula(c, op, (xs[i] + xs[i + 1]) / 2, y - 60, 48, "g", fundo=cor, a=q)
        E.foco(c, t, ts[-1] + 0.4, 0.4, lambda a: E.centro(c, fim, xs[2], y + 30, 80, "g", SAI, a))
    corrente(420, ("+ 5", "÷ 2"), (C["s14.a"], C["s14.a"] + 0.8), TINTA, 1, "x", "f")
    corrente(620, ("× 2", "− 5"), (C["s14.b"], C["s14.b"] + 0.8), COR, -1, "x", "?")
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (M.rrect(c, 1360, 360, 460, 170, 34, COR, a),
                                             fx(c, [("f", BR), ("^{−1}", BR), ("(x) = 2x − 5", BR)], 1590, 465, 66, a, "center")))
    fx_em(c, t, C["s14.d"], [("f", SAI), ("^{−1}", COR), ("(3) = 2 · 3 − 5 = ", SAI), ("1", COR)], XE, 840, 84)
    E.foco(c, t, C["s14.e"], 0.5, lambda a: (fx(c, [("confira:  f(1) = ", CERTO), ("f{1 + 5}{2}", CERTO), (" = 3", CERTO)], XE, 990, 64, a),
                                             E.selo(c, 1050, 970, 36, True, a)))


# ---------------- situação 5: paridade pelo gráfico ----------------
GR = (("A", fa, (-2.6, 2.6), 300), ("B", fb, (-2.25, 2.25), 960), ("C", fc, (-2.6, 2.6), 1620))


def planinho(c, t, t0, cx, f, ab, nome, a_extra=1.0):
    P = E.plano(c, t, t0, cx - 270, 390, 540, 430, -3, 3, -4, 4, passo=1, marcas_x=[], marcas_y=[], size=30, d=0.5)
    E.curva(c, t, t0 + 0.3, P, f, ab[0], ab[1], d=0.8, cor=COR)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, nome, cx - 230, 430, 60, "g", fundo=TINTA, a=a))
    return P


def b_questao5(c, t, C, b):
    E.frase(c, t, C["s15.a"], [("situação", "i", 72, COR), ("5", "g", 80, COR)], XE, 190)
    for (nome, f, ab, cx), k in zip(GR, ("s15.b", "s15.c", "s15.d")):
        planinho(c, t, C[k] - 0.4, cx, f, ab, nome)
    E.frase(c, t, C["s15.e"], [("qual", "i", 84), ("é", "i", 84), ("de", "i", 84), ("uma", "i", 84), ("função", "i", 84), ("ímpar?", "g", 90, COR)],
            W / 2, 960, "center")
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=700, cy=165, r=70)


def b_resposta5(c, t, C, b):
    Ps = []
    for nome, f, ab, cx in GR:
        Ps.append(planinho(c, t, C["s17"] - 2.0, cx, f, ab, nome))
    # A: dobra no eixo y
    PA, PB, PC = Ps
    p = ease_io(prog(t, C["s17.a"] + 0.3, 1.3))
    if p > 0:
        traco(c, PA, [(lerp(x, -x, p), y) for x, y in amostra(fa, -2.6, 0)], TINTA, 0.7, 8)
        M.line(c, PA.ox, PA.caixa[1], PA.ox, PA.caixa[1] + PA.caixa[3], COR, 0.2 * ep(t, C["s17.a"], 0.4), 22)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.pilula(c, "par", 300, 890, 60, "g", fundo=COR, a=a))
    # C: não dobra
    q = ep(t, C["s17.c"], 0.4)
    if q > 0:
        traco(c, PC, [(-x, y) for x, y in amostra(fc, -2.6, 2.6)], ERRADO, 0.6 * q, 6, E.TRACO)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: (E.pilula(c, "nenhuma", 1620, 890, 60, "g", fundo=TINTA, a=a), E.selo(c, 1850, 860, 34, False, a)))
    # B: meia volta
    p = ease_io(prog(t, C["s17.e"] + 0.3, 1.6))
    if p > 0:
        ang = math.pi * p
        ox, oy = PB(0, 0)
        pts = []
        for xv, yv in amostra(fb, -2.25, 2.25):
            X, Y = PB(xv, yv)
            dx, dy = X - ox, Y - oy
            pts.append((ox + dx * math.cos(ang) - dy * math.sin(ang), oy + dx * math.sin(ang) + dy * math.cos(ang)))
        x, y, w, h = PB.caixa
        c.save(); c.clipRect(skia.Rect.MakeXYWH(x - 6, y - 6, w + 12, h + 12), True)
        path = skia.Path(); path.moveTo(*pts[0])
        for q_ in pts[1:]:
            path.lineTo(*q_)
        c.drawPath(path, M.paint(TINTA, 0.7, stroke=8, cap_round=True))
        c.restore()
        E.arco(c, ox, oy, 60, -90, 180 * p, CERTO, 6)
    E.foco(c, t, C["s17.f"], 0.5, lambda a: (E.pilula(c, "ímpar", 960, 890, 70, "g", fundo=CERTO, a=a), E.selo(c, 1140, 860, 36, True, a)))
    E.frase(c, t, C["s17.f"] + 0.6, [("resposta:", "i", 72), ("B", "g", 84, CERTO)], W / 2, 1020, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def s18():
        E.frase(c, t, C["s18.a"], [("cada", "i", 84), ("ferramenta,", "i", 84), ("uma", "i", 84), ("pergunta", "g", 90, COR)], W / 2, 220, "center")
        perguntas = ("qual faixa?", "qual distância?", "quem vem primeiro?", "como desfazer?", "que espelho?")
        for i, s in enumerate(perguntas):
            E.foco(c, t, C["s18.b"] + 0.75 * i, 0.4, lambda a, s=s, i=i: (item(c, t, C["s18.b"] + 0.75 * i, i + 1, 560, 380 + i * 130, 44),
                                                                          E.escreve(c, s, 640, 380 + i * 130, 70, "g", TINTA, a)))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19.a"], [("você", "i", 84), ("fechou", "i", 84), ("a", "i", 84), ("trilha", "i", 84)], XE, 260)
    E.frase(c, t, C["s19.a"] + 1.0, [("modular,", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s19.a"] + 1.3, [("composta", "g", 110, COR)], XE, 550)
    E.frase(c, t, C["s19.a"] + 1.6, [("e", "i", 100), ("inversa", "g", 110, COR)], XE, 680)
    nota(c, t, C["s19.b"], "travou? procure a aula no canal", 560, 800, 46, fundo=TINTA)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5,
              resposta5=b_resposta5, fim=b_fim)
