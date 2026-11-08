"""Visual — Estudativo · MAT-FUN-007: ler um gráfico (máximo, mínimo, zeros, crescimento, domínio e imagem).

Linguagem visual da trilha Funções (MAT-FUN-001 a 006): entrada / x em índigo (eixo x índigo), saída / y em preto (eixo y preto);
plano sempre na metade direita com eixos(), texto à esquerda; par (x, y) com o x índigo e o y preto (par()).
Nesta aula:
- o gráfico da temperatura (E.curva, interpolação monótona pelos pontos do roteiro) em índigo; máximo e mínimo com E.ponto;
- ler um ponto: seta índigo que sai da entrada (eixo x) até a curva e seta preta que vai da curva até a saída (eixo y), com anda();
- guia(): tracejado do ponto até o eixo, índigo até o eixo x (o momento) e preto até o eixo y (o valor);
- zero = anel preto no ponto em que a curva toca o eixo x;
- crescente = trecho repintado de verde, decrescente = trecho repintado de vermelho (sobe / desce), por cima da curva;
- domínio = barra índigo deitada sobre o eixo x; imagem = barra preta em pé sobre o eixo y (barra()), bolinha cheia = fechado;
- atalho (palco escuro): a "sombra" do gráfico, com fios de projeção até o chão (eixo x) e até a parede (eixo y).
Peças locais: eixos(), par(), anda(), guia(), anel(), barra(), trecho(), projecao(), mini()."""
import bisect
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-007_ler_um_grafico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ler", "zeros", "dominio", "atalho", "questao", "fim"))
BR = "#FFFFFF"
SOBE, DESCE = CERTO, ERRADO


def suave(pts):
    """curva monótona entre os pontos (Fritsch-Carlson): passa por todos, sem ondas, máximos e mínimos só nos pontos dados"""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    n = len(pts)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    d = [(ys[i + 1] - ys[i]) / h[i] for i in range(n - 1)]
    m = [d[0]] + [0.0] * (n - 2) + [d[-1]]
    for i in range(1, n - 1):
        if d[i - 1] * d[i] > 0:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])

    def f(x):
        if x < xs[0] - 1e-9 or x > xs[-1] + 1e-9:
            return None
        i = min(max(bisect.bisect_right(xs, x) - 1, 0), n - 2)
        u = (x - xs[i]) / h[i]
        h00, h10, h01, h11 = 2 * u ** 3 - 3 * u ** 2 + 1, u ** 3 - 2 * u ** 2 + u, -2 * u ** 3 + 3 * u ** 2, u ** 3 - u ** 2
        return h00 * ys[i] + h10 * h[i] * m[i] + h01 * ys[i + 1] + h11 * h[i] * m[i + 1]
    return f


TEMP = [(0, -2), (6, -4), (9, 0), (15, 8), (21, 0), (24, -3)]
f = suave(TEMP)
LOJA = [(0, 2), (1, 0), (3, -4), (5, 0), (9, 6), (12, 3)]
g = suave(LOJA)
_amostra = [f(i / 10) for i in range(0, 241)]
assert max(_amostra) == 8 and min(_amostra) == -4 and abs(f(15) - 8) < 1e-9 and abs(f(6) + 4) < 1e-9
assert [round(f(x), 9) for x in (9, 21)] == [0, 0] and all(f(x / 10) < 0 for x in range(61, 90)) and all(f(x / 10) > 0 for x in range(91, 210))
_amostra = [g(i / 10) for i in range(0, 121)]
assert max(_amostra) == 6 and min(_amostra) == -4 and abs(g(9) - 6) < 1e-9 and abs(g(1)) < 1e-9 and abs(g(5)) < 1e-9
assert all(g(x / 10) > g((x - 1) / 10) for x in range(31, 91)) and all(g(x / 10) != 0 for x in range(0, 121) if x not in (10, 50))

P = E.Plano(1060, 170, 740, 720, -1.5, 25.5, -5.5, 9.5)
MX, MY = list(range(0, 25, 3)), list(range(-4, 9, 2))
PL = E.Plano(1060, 210, 740, 680, -1, 13, -5.5, 7.5)
LX, LY = list(range(0, 13, 1)), list(range(-4, 7, 2))


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def eixos(c, t, P, tx, ty=None, tg=None, mx=MX, my=MY, nx="hora", ny="°C", size=36):
    """plano em etapas (o mesmo da MAT-FUN-001/006): grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty"""
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in mx:
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in my:
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, nx, x + w + 10 - E.larg(nx, "i", 46), P.oy - 22, 46, "i", ENT, a))
        for i, v in enumerate(mx):
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                centro(c, E._num(v), X + (14 if v == 0 else 0), P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, ny, P.ox + 22, y - 16, 46, "i", SAI, a))
        for i, v in enumerate(my):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto"""
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", TINTA), (xv, cx_), (", ", TINTA), (yv, cy_), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def anda(c, t, t0, P, A, B, cor, d=0.8, largura=10):
    """seta que anda no plano de A até B (em valores), com halo (a mesma da MAT-FUN-001)"""
    p = ease_io(prog(t, t0, d))
    if p > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, 0.22, largura * 3.2)
        M.arrow(c, x0, y0, x1, y1, cor, 1.0, largura, 30, p)


def guia(c, t, t0, P, xv, yv, eixo, cor=None, d=0.6, largura=5):
    """tracejado do ponto (xv, yv) até o eixo: "x" desce/sobe até o eixo x (índigo), "y" vai de lado até o eixo y (preto)"""
    q = ease_io(prog(t, t0, d))
    if q <= 0:
        return
    X, Y = P(xv, yv)
    if eixo == "x":
        M.line(c, X, Y, X, P.oy, cor or ENT, 1.0, largura, dash=E.TRACO, progress=q)
    else:
        M.line(c, X, Y, P.ox, Y, cor or SAI, 1.0, largura, dash=E.TRACO, progress=q)


def anel(c, t, t0, P, xv, yv, cor=SAI, r=24, largura=6):
    """anel que fecha em volta de um ponto do plano"""
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, *P(xv, yv), r, -90, 360 * q, cor, largura)


def marca_eixo(c, t, t0, P, v, eixo, cor, size=44):
    """o número do eixo ganha uma pílula da cor dele (o valor lido)"""
    s = E._num(v)
    if eixo == "x":
        cx, cy = P.x(v), P.oy + 14 + 36 - 13
    else:
        cx, cy = P.ox - 20 - E.larg(s, "b", 36) / 2, P.y(v)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor, a=a), sobe=0)


def barra(c, t, t0, P, eixo, a_, b_, cor, fecha=(True, True), d=0.8, larg=14, r=15, fundo=None):
    """o trecho do eixo ocupado: deitado no eixo x (domínio) ou em pé no eixo y (imagem); bolinha cheia = fechado"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    fundo = fundo or E.PAPEL
    if eixo == "x":
        x0, x1 = P.x(a_), P.x(b_)
        M.line(c, x0, P.oy, lerp(x0, x1, p), P.oy, cor, 1.0, larg)
        pts = ((x0, P.oy), (x1, P.oy))
    else:
        y0, y1 = P.y(a_), P.y(b_)
        M.line(c, P.ox, y0, P.ox, lerp(y0, y1, p), cor, 1.0, larg)
        pts = ((P.ox, y0), (P.ox, y1))
    q = ep(t, t0 + d * 0.6, 0.3)
    for (X, Y), fc in zip(pts, fecha):
        c.drawCircle(X, Y, r, M.paint(cor if fc else fundo, q))
        c.drawCircle(X, Y, r, M.paint(cor, q, stroke=6))


def trecho(c, t, t0, P, fn, a_, b_, cor, d=0.9, largura=13):
    """repinta um pedaço da curva (sobe = verde, desce = vermelho), da esquerda para a direita"""
    E.curva(c, t, t0, P, fn, a_, b_, d=d, cor=cor, largura=largura)


def seta_curva(c, P, fn, xv, cor, a=1.0, dx=0.6):
    """ponta de seta sobre a curva no sentido da leitura (da esquerda para a direita)"""
    if a <= 0:
        return
    (x0, y0), (x1, y1) = P(xv - dx, fn(xv - dx)), P(xv + dx, fn(xv + dx))
    M.arrow(c, x0, y0, x1, y1, cor, a, 0.1, 34)


def projecao(c, t, t0, P, fn, a_, b_, eixo, cor, d=1.2, passo=1.0, alfa=0.5, largura=3):
    """fios de projeção de cada ponto da curva até o chão (eixo x) ou a parede (eixo y), acendendo da esquerda para a direita"""
    n = int(round((b_ - a_) / passo))
    for i in range(n + 1):
        xv = a_ + i * passo
        q = ease_io(prog(t, t0 + d * i / max(n, 1), 0.4))
        if q <= 0:
            continue
        X, Y = P(xv, fn(xv))
        if eixo == "x":
            M.line(c, X, Y, X, P.oy, cor, alfa, largura, progress=q)
        else:
            M.line(c, X, Y, P.ox, Y, cor, alfa, largura, progress=q)


def mini(c, t, t0, x, y, w, h, fn, zeros=(), d=0.8):
    """mini-gráfico (o mesmo da MAT-FUN-006): eixos simples, a curva e os zeros com anel"""
    Q = E.plano(c, t, t0, x, y, w, h, -3, 3, -3, 3, grade=False, rotulos=False, size=30, d=0.5)
    E.curva(c, t, t0 + 0.3, Q, fn, -3, 3, d=d, largura=6)
    for i, z in enumerate(zeros):
        q = ease_back(prog(t, t0 + 0.3 + d + 0.15 * i, 0.4))
        if q > 0:
            c.drawCircle(*Q(z, 0), 12 * q, M.paint(SAI))
    return Q


def temp(c, t, t0, d=1.6):
    E.curva(c, t, t0, P, f, 0, 24, d=d)


def pontas(c, t, t0, P, fn, a_, b_, cor=COR):
    """o gráfico começa e termina com bolinha cheia"""
    for xv in (a_, b_):
        k = ease_back(prog(t, t0, 0.4))
        if k > 0:
            c.drawCircle(*P(xv, fn(xv)), 11 * k, M.paint(cor))


def grafico(c, t, t0):
    """o gráfico da temperatura já pronto (blocos depois do primeiro)"""
    eixos(c, t, P, t0, t0, t0)
    temp(c, t, t0, 0.1)
    pontas(c, t, t0, P, f, 0, 24)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        eixos(c, t, P, C["s01.a"], C["s01.a"], C["s01.a"])
        temp(c, t, C["s01.a"] + 0.4)
        pontas(c, t, C["s01.a"] + 2.0, P, f, 0, 24)
        E.frase(c, t, C["s01.a"], ps("a temperatura de um dia", "i", 64), XE, 260, passo=0.1)
        E.frase(c, t, C["s01.a"] + 2.6, [("qual", "i", 84), ("foi", "i", 84), ("a", "i", 84), ("máxima?", "g", 84, COR)], XE, 400)
        anel(c, t, C["s01.a"] + 4.0, P, 15, 8, COR, 30)
        # o erro: 15
        guia(c, t, C["s01.b"], P, 15, 8, "x", ERRADO)
        marca_eixo(c, t, C["s01.b"] + 0.4, P, 15, "x", ERRADO)
        E.frase(c, t, C["s01.b"], [("muita", "i", 64), ("gente:", "i", 64), ("15", "g", 80, ERRADO)], XE, 560)
        if t >= C["s01.b"] + 0.6:
            X = XE + E.larg("muita gente: ", "i", 64) + 12
            E.risco(c, X - 8, 530, X + 100, 500, t, C["s01.c"], largura=8)
        E.frase(c, t, C["s01.c"], [("15", "g", 64, ENT), ("é", "i", 64), ("a", "i", 64), ("hora", "g", 64, ENT)], XE, 680)
        # a resposta: 8
        guia(c, t, C["s01.d"], P, 15, 8, "y", SAI)
        marca_eixo(c, t, C["s01.d"] + 0.4, P, 8, "y", SAI)
        E.frase(c, t, C["s01.d"], [("máxima:", "i", 72), ("8", "g", 110, SAI), ("°C", "g", 80, SAI)], XE, 850)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.e"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.e"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 280)
        E.frase(c, t, C["s02.a"] + 1.2, [("ler", "i", 100), ("o", "i", 100), ("gráfico", "g", 100, COR), ("inteiro", "i", 100)], XE, 420)
        E.frase(c, t, C["s02.b"], [("máxima", "g", 80)], XE, 580)
        E.frase(c, t, C["s02.c"], [("zeros", "g", 80)], XE, 690)
        E.frase(c, t, C["s02.d"], [("sobe", "g", 80, SOBE), ("e", "i", 76), ("desce", "g", 80, DESCE)], XE, 800)
        E.foco(c, t, C["s02.e"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "gráfico: cada ponto é", lambda a, y: par(c, "entrada", "saída", x + 44, y, 62, a)),
             ("s03.c", "domínio e imagem:", lambda a, y: E.escreve(c, "[0, 5]", x + 44, y, 66, "g", COR, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 64)], x + 44, y + 96)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, fn=fn, y=y: fn(a, y + 196))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(460, 760, q), ep(t, C["s03.b"], 0.4))


# ---------------- ler um ponto ----------------
def b_ler(c, t, C, b):
    eixos(c, t, P, C["s04.a"], C["s04.b"], C["s04"])
    x, y, w, h = P.caixa
    q = ep(t, C["s04.a"], 0.3) * (1 - ep(t, C["s04.a"] + 2.2, 0.5))
    if q > 0:
        M.line(c, x - 10, P.oy, x + w + 20, P.oy, ENT, 0.25 * q, 26)
    q = ep(t, C["s04.b"], 0.3) * (1 - ep(t, C["s04.b"] + 2.2, 0.5))
    if q > 0:
        M.line(c, P.ox, y + h + 10, P.ox, y - 20, SAI, 0.2 * q, 26)
    temp(c, t, C["s04.c"])
    pontas(c, t, C["s04.c"] + 1.4, P, f, 0, 24)

    def s04():
        E.frase(c, t, C["s04.a"], [("eixo", "i", 76), ("x:", "g", 80, ENT), ("a", "i", 76), ("hora", "g", 76, ENT)], XE, 300)
        E.frase(c, t, C["s04.a"] + 1.6, ps("de 0 a 24", "i", 56, TINTA2), XE, 380, passo=0.1)
        E.frase(c, t, C["s04.b"], [("eixo", "i", 76), ("y:", "g", 80), ("a", "i", 76), ("temperatura", "g", 76)], XE, 520)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: par(c, "hora", "graus", XE, 720, 72, a))
        E.frase(c, t, C["s04.c"] + 0.6, [("um", "i", 64), ("ponto", "g", 64, COR), ("da", "i", 64), ("curva", "i", 64)], XE, 830)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("às", "i", 80), ("6", "g", 90, ENT), ("h?", "g", 80, ENT)], XE, 300)
    anda(c, t, C["s05.b"], P, (6, 0), (6, -4), ENT, d=0.9)
    marca_eixo(c, t, C["s05.a"], P, 6, "x", ENT)
    E.frase(c, t, C["s05.a"], [("1.", "g", 60, TINTA2), ("saia", "i", 64), ("do", "i", 64), ("6", "g", 64, ENT)], XE, 450)
    E.frase(c, t, C["s05.b"], [("2.", "g", 60, TINTA2), ("vá", "i", 64), ("até", "i", 64), ("a", "i", 64), ("curva", "g", 64, COR)], XE, 560)
    anda(c, t, C["s05.c"], P, (6, -4), (0, -4), SAI, d=0.8)
    E.frase(c, t, C["s05.c"], [("3.", "g", 60, TINTA2), ("de", "i", 64), ("lado", "i", 64), ("até", "i", 64), ("o", "i", 64), ("eixo", "i", 64), ("y", "g", 64)],
            XE, 670)
    marca_eixo(c, t, C["s05.d"], P, -4, "y", SAI)
    E.frase(c, t, C["s05.d"], [("−4", "g", 110), ("°C", "g", 80)], XE, 860)


# ---------------- máximo e mínimo ----------------
def b_maximo(c, t, C, b):
    grafico(c, t, C["s06"] - 3)

    def s06():
        E.ponto(c, t, C["s06.a"], P, 15, 8, cor=COR, r=17)
        anel(c, t, C["s06.a"] + 0.2, P, 15, 8, COR, 32)
        E.frase(c, t, C["s06.a"], [("o", "i", 80), ("mais", "i", 80), ("alto:", "i", 80), ("máximo", "g", 84, COR)], XE, 260)
        E.foco(c, t, C["s06.b"], 0.5, lambda a: par(c, "15", "8", XE, 410, 90, a))
        E.foco(c, t, C["s06.b"] + 0.3, 0.4, lambda a: par(c, "15", "8", P.x(15) - 70, P.y(8) - 46, 40, a))
        E.frase(c, t, C["s06.c"], [("2", "g", 70, COR), ("informações", "i", 66)], XE, 540)
        guia(c, t, C["s06.d"], P, 15, 8, "y")
        marca_eixo(c, t, C["s06.d"] + 0.4, P, 8, "y", SAI)
        E.frase(c, t, C["s06.d"], [("valor:", "i", 64), ("o", "i", 64), ("y", "g", 64), ("→", "g", 64, TINTA2), ("8", "g", 76), ("°C", "g", 64)], XE, 680)
        guia(c, t, C["s06.e"], P, 15, 8, "x")
        marca_eixo(c, t, C["s06.e"] + 0.4, P, 15, "x", ENT)
        E.frase(c, t, C["s06.e"], [("quando:", "i", 64), ("o", "i", 64), ("x", "g", 64, ENT), ("→", "g", 64, TINTA2), ("15", "g", 76, ENT), ("h", "g", 64, ENT)],
                XE, 800)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("o", "i", 80), ("mais", "i", 80), ("baixo:", "i", 80), ("mínimo", "g", 84, COR)], XE, 260)
    E.ponto(c, t, C["s07.a"], P, 6, -4, cor=COR, r=17)
    anel(c, t, C["s07.a"] + 0.2, P, 6, -4, COR, 32)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: par(c, "6", "−4", XE, 410, 90, a))
    E.foco(c, t, C["s07.b"] + 0.3, 0.4, lambda a: par(c, "6", "−4", P.x(6) + 30, P.y(-4) + 60, 40, a))
    guia(c, t, C["s07.c"], P, 6, -4, "y")
    marca_eixo(c, t, C["s07.c"] + 0.4, P, -4, "y", SAI)
    E.frase(c, t, C["s07.c"], [("mínima:", "i", 64), ("−4", "g", 76), ("°C", "g", 64)], XE, 600)
    guia(c, t, C["s07.d"], P, 6, -4, "x")
    marca_eixo(c, t, C["s07.d"] + 0.4, P, 6, "x", ENT)
    E.frase(c, t, C["s07.d"], [("às", "i", 64), ("6", "g", 76, ENT), ("h", "g", 64, ENT), ("da", "i", 64), ("manhã", "i", 64)], XE, 720)


# ---------------- zeros ----------------
def b_zeros(c, t, C, b):
    x, y, w, h = P.caixa

    def s08():
        grafico(c, t, C["s08"] - 3)
        E.frase(c, t, C["s08"], [("quando", "i", 76), ("fez", "i", 76), ("0", "g", 90, COR), ("°C?", "g", 76, COR)], XE, 260)
        q = ep(t, C["s08.a"], 0.3) * (1 - ep(t, C["s08.b"] + 1.0, 0.5))
        if q > 0:
            M.line(c, x - 10, P.oy, x + w + 20, P.oy, ENT, 0.25 * q, 26)
        E.frase(c, t, C["s08.a"], [("y", "g", 64), ("=", "g", 64), ("0:", "g", 64), ("o", "i", 64), ("eixo", "i", 64), ("x", "g", 64, ENT)], XE, 400)
        E.frase(c, t, C["s08.b"], [("onde", "i", 64), ("a", "i", 64), ("curva", "i", 64), ("toca", "g", 64, COR), ("o", "i", 64), ("eixo", "i", 64)], XE, 510)
        for k, xv in (("s08.c", 9), ("s08.d", 21)):
            anel(c, t, C[k], P, xv, 0, SAI, 26)
            E.ponto(c, t, C[k], P, xv, 0, cor=SAI, r=13)
            marca_eixo(c, t, C[k] + 0.3, P, xv, "x", ENT)
        E.frase(c, t, C["s08.c"], [("x", "g", 76, ENT), ("=", "g", 76), ("9", "g", 84, ENT)], XE, 660)
        E.frase(c, t, C["s08.d"], [("e", "i", 76), ("x", "g", 76, ENT), ("=", "g", 76), ("21", "g", 84, ENT)], XE + 350, 660)
        E.frase(c, t, C["s08.e"], [("9", "g", 70, ENT), ("h", "g", 70, ENT), ("e", "i", 66), ("21", "g", 70, ENT), ("h:", "g", 70, ENT), ("0", "g", 70), ("°C", "g", 70)],
                XE, 820)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"], [("zeros", "g", 110, COR), ("da", "i", 100), ("função", "i", 100)], W / 2, 250, "center")
    E.foco(c, t, C["s09.a"] + 0.8, 0.5, lambda a: E.formula(c, "os x em que y = 0", W / 2, 360, 60, "i", TINTA2, a, "center"))
    minis = ((C["s09.b"], 200, "um zero", lambda v: 0.8 * v + 0.4, (-0.5,)),
             (C["s09.b"] + 0.9, 760, "vários", lambda v: 1.4 * math.sin(1.7 * v), (-math.pi / 1.7, 0, math.pi / 1.7)),
             (C["s09.c"], 1320, "nenhum", lambda v: 0.35 * v * v + 1, ()))
    for t0, mx_, nome, fn, zs in minis:
        mini(c, t, t0, mx_, 470, 400, 380, fn, zs)
        E.foco(c, t, t0 + 0.3, 0.4, lambda a, mx_=mx_, nome=nome: centro(c, nome, mx_ + 200, 960, 58, "g", COR if nome != "nenhum" else ERRADO, a))


# ---------------- crescimento ----------------
def b_cresce(c, t, C, b):
    grafico(c, t, C["s10"] - 3)
    x, y, w, h = P.caixa

    def s10():
        E.frase(c, t, C["s10"], [("esquentou", "g", 72, SOBE), ("ou", "i", 72), ("esfriou?", "g", 72, DESCE)], XE, 260)
        p = ease_io(prog(t, C["s10.a"], 1.2))
        if p > 0:
            M.arrow(c, x + 60, y - 90, x + w, y - 90, TINTA2, 1.0, 7, 26, p)
        E.frase(c, t, C["s10.a"], [("da", "i", 60), ("esquerda", "g", 60), ("para", "i", 60), ("a", "i", 60), ("direita", "g", 60)], XE, 380)
        itens = (("s10.b", "sobe:", "crescente", SOBE, (0, -50)), ("s10.c", "desce:", "decrescente", DESCE, (0, 50)), ("s10.d", "horizontal:", "constante", TINTA2, (0, 0)))
        for i, (k, l1, l2, cor, (dx, dy)) in enumerate(itens):
            yy = 540 + i * 140
            q = ep(t, C[k], 0.5)
            if q > 0:
                M.arrow(c, XE, yy - 20 - dy / 2, XE + 100, yy - 20 + dy / 2, cor, q, 9, 28, ease_io(prog(t, C[k], 0.6)))
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 64), (l2, "g", 64, cor)], XE + 140, yy)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    for k, a_, b_, cor in (("s11.a", 0, 6, DESCE), ("s11.b", 6, 15, SOBE), ("s11.c", 15, 24, DESCE)):
        trecho(c, t, C[k], P, f, a_, b_, cor)
        seta_curva(c, P, f, (a_ + b_) / 2 + (0.5 if cor == SOBE else 0), cor, ep(t, C[k] + 0.8, 0.3))
    E.frase(c, t, C["s11.a"], [("caiu", "g", 66, DESCE), ("de", "i", 64), ("0", "g", 66), ("a", "i", 64), ("6", "g", 66), ("h", "g", 66)], XE, 260)
    E.frase(c, t, C["s11.b"], [("subiu", "g", 66, SOBE), ("de", "i", 64), ("6", "g", 66), ("a", "i", 64), ("15", "g", 66), ("h", "g", 66)], XE, 370)
    E.frase(c, t, C["s11.c"], [("caiu", "g", 66, DESCE), ("de", "i", 64), ("15", "g", 66), ("a", "i", 64), ("24", "g", 66), ("h", "g", 66)], XE, 480)
    E.frase(c, t, C["s11.d"], [("crescente:", "g", 60, SOBE), ("de", "i", 60), ("6", "g", 64, ENT), ("a", "i", 60), ("15", "g", 64, ENT)], XE, 660)
    E.frase(c, t, C["s11.e"], [("decrescente:", "g", 60, DESCE), ("de", "i", 60), ("0", "g", 64, ENT), ("a", "i", 60), ("6", "g", 64, ENT)], XE, 780)
    E.frase(c, t, C["s11.e"] + 1.6, [("e", "i", 60), ("de", "i", 60), ("15", "g", 64, ENT), ("a", "i", 60), ("24", "g", 64, ENT)], XE + 260, 880)
    for k, a_, b_, cor in (("s11.d", 6, 15, SOBE), ("s11.e", 0, 6, DESCE), ("s11.e", 15, 24, DESCE)):
        barra(c, t, C[k] + 0.2, P, "x", a_, b_, cor, larg=10, r=11)


# ---------------- domínio e imagem ----------------
def b_dominio(c, t, C, b):
    grafico(c, t, C["s12"] - 3)
    E.frase(c, t, C["s12.a"], [("domínio:", "g", 76, ENT), ("as", "i", 70), ("horas", "i", 70)], XE, 270)
    barra(c, t, C["s12.b"], P, "x", 0, 24, ENT, d=1.2)
    projecao(c, t, C["s12.b"] - 0.4, P, f, 0, 24, "x", ENT, d=1.2, alfa=0.3)
    E.frase(c, t, C["s12.b"], [("de", "i", 64), ("0", "g", 70, ENT), ("a", "i", 64), ("24", "g", 70, ENT)], XE, 380)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "D = [0, 24]", XE, 500, 90, "g", ENT, a))
    E.frase(c, t, C["s13.a"], [("imagem:", "g", 76), ("as", "i", 70), ("temperaturas", "i", 70)], XE, 680)
    barra(c, t, C["s13.b"], P, "y", -4, 8, SAI, d=1.0)
    projecao(c, t, C["s13.b"] - 0.4, P, f, 0, 24, "y", SAI, d=1.2, alfa=0.22)
    E.frase(c, t, C["s13.b"], [("de", "i", 64), ("−4", "g", 70), ("a", "i", 64), ("8", "g", 70)], XE, 790)
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "Im = [−4, 8]", XE, 910, 90, "g", SAI, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    eixos(c, t, P, C["s14"] - 3, C["s14"] - 3, C["s14"] - 3)
    x, y, w, h = P.caixa
    q = ep(t, C["s14.b"], 0.5)
    if q > 0:
        c.drawRect(skia.Rect.MakeLTRB(P.x(6), y, P.x(9), y + h), M.paint(TINTA, 0.06 * q))
    E.area(c, t, C["s14.c"], P, f, 6, 9, cor=TINTA2, alfa=0.22)
    temp(c, t, C["s14"] - 3, 0.1)
    pontas(c, t, C["s14"] - 3, P, f, 0, 24)
    trecho(c, t, C["s14.e"], P, f, 6, 9, SOBE, d=0.6)
    seta_curva(c, P, f, 7.9, SOBE, ep(t, C["s14.e"] + 0.5, 0.3), 0.5)
    E.frase(c, t, C["s14.a"], [("abaixo", "g", 66, ERRADO), ("do", "i", 64), ("eixo", "i", 64), ("=", "g", 66, ERRADO), ("descendo?", "g", 66, ERRADO)], XE, 230)
    if t >= C["s14.a"] + 1.0:
        E.risco(c, XE - 10, 210, XE + 820, 192, t, C["s14.e"], largura=8)
    marca_eixo(c, t, C["s14.b"], P, 6, "x", ENT)
    marca_eixo(c, t, C["s14.b"] + 0.2, P, 9, "x", ENT)
    E.frase(c, t, C["s14.b"], [("das", "i", 64), ("6", "g", 70, ENT), ("às", "i", 64), ("9", "g", 70, ENT), ("h", "g", 64, ENT)], XE, 360)
    E.frase(c, t, C["s14.c"], [("negativa", "g", 64, TINTA2), ("o", "i", 62), ("tempo", "i", 62), ("todo", "i", 62)], XE, 460)
    E.ponto(c, t, C["s14.d"], P, 6, -4, cor=SAI, r=14)
    E.ponto(c, t, C["s14.d"] + 0.6, P, 9, 0, cor=SAI, r=14)
    E.frase(c, t, C["s14.d"], [("−4", "g", 76), ("→", "g", 76, TINTA2), ("0", "g", 76)], XE, 570)
    E.frase(c, t, C["s14.e"], [("está", "i", 76), ("subindo", "g", 80, SOBE)], XE + 370, 570)
    E.frase(c, t, C["s14.f"], [("negativo:", "g", 60), ("onde", "i", 62), ("ela", "i", 62), ("está", "g", 62, COR)], XE, 740)
    E.frase(c, t, C["s14.g"], [("crescente:", "g", 60, SOBE), ("para", "i", 62), ("onde", "i", 62), ("vai", "g", 62, COR)], XE, 850)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    PE = E.plano(c, t, C["s15"] - 2, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, passo=3, passo_y=2, marcas_x=MX, marcas_y=MY, grade=False,
                 nomes=("hora", "°C"), size=34, escuro=True)
    E.curva(c, t, C["s15"] - 1.6, PE, f, 0, 24, d=0.1, cor=CLARO, largura=8)
    x, y, w, h = PE.caixa
    aberto = ep(t, C["s16.b"], 0.4)
    for xv, fecha in ((0, True), (24, False)):
        k = ep(t, C["s15"] - 1.5, 0.3)
        X, Y = PE(xv, f(xv))
        c.drawCircle(X, Y, 12, M.paint(CLARO, k))
        if not fecha and aberto > 0:
            c.drawCircle(X, Y, 12, M.paint("#0B0B16", aberto))
            c.drawCircle(X, Y, 12, M.paint(CLARO, aberto, stroke=5))

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 66, CLARO), XE, 200)
        E.frase(c, t, C["s15.a"], [("a", "i", 90, CLARO), ("sombra", "g", 96, BR)], XE, 340)
        E.frase(c, t, C["s15.a"] + 0.6, [("do", "i", 90, CLARO), ("gráfico", "g", 96, BR)], XE, 450)
    E.saida(c, t, C["s16"] - 0.1, s15)
    # lanterna em cima: fios até o chão, sombra no eixo x
    q = ep(t, C["s15.b"], 0.4)
    if q > 0:
        lx = P.x(12)
        E.foco(c, t, C["s15.b"], 0.4, lambda a: (c.drawCircle(lx, y - 70, 22, M.paint("#FFE680", a)),
                                                c.drawCircle(lx, y - 70, 44, M.paint("#FFE680", 0.25 * a))), blur=0)
    projecao(c, t, C["s15.b"] + 0.2, PE, f, 0, 24, "x", "#FFE680", d=1.4, passo=1, alfa=0.5, largura=4)
    barra(c, t, C["s15.b"] + 0.8, PE, "x", 0, 24, CLARO, (True, aberto <= 0), d=1.2, fundo="#0B0B16")
    E.frase(c, t, C["s15.b"], [("em", "i", 62, CLARO), ("cima:", "i", 62, CLARO), ("chão", "g", 64, BR), ("=", "g", 64, CLARO), ("domínio", "g", 64, CLARO)], XE, 620)
    # lanterna de lado: fios até a parede, sombra no eixo y
    q = ep(t, C["s15.c"], 0.4)
    if q > 0:
        ly = P.y(5)
        E.foco(c, t, C["s15.c"], 0.4, lambda a: (c.drawCircle(x + w + 30, ly, 22, M.paint("#FFE680", a)),
                                                c.drawCircle(x + w + 30, ly, 44, M.paint("#FFE680", 0.25 * a))), blur=0)
    projecao(c, t, C["s15.c"] + 0.2, PE, f, 0, 24, "y", "#FFE680", d=1.4, passo=1, alfa=0.4, largura=4)
    barra(c, t, C["s15.c"] + 0.8, PE, "y", -4, 8, BR, d=1.0, fundo="#0B0B16")
    E.frase(c, t, C["s15.c"], [("de", "i", 62, CLARO), ("lado:", "i", 62, CLARO), ("parede", "g", 64, BR), ("=", "g", 64, CLARO), ("imagem", "g", 64, BR)], XE, 740)
    if t < C["s16"]:
        return
    # cada ponto projeta o x no chão e o y na parede
    xv = lerp(3, 19, ease_io(prog(t, C["s16.a"], 3.0)))
    a = ep(t, C["s16.a"], 0.4) * (1 - ep(t, C["s16.b"] - 0.3, 0.4))
    if a > 0:
        X, Y = PE(xv, f(xv))
        M.line(c, X, Y, X, PE.oy, BR, a, 5, dash=E.TRACO)
        M.line(c, X, Y, PE.ox, Y, BR, a, 5, dash=E.TRACO)
        c.drawCircle(X, Y, 16, M.paint(BR, a))
        c.drawCircle(X, PE.oy, 10, M.paint(CLARO, a))
        c.drawCircle(PE.ox, Y, 10, M.paint(BR, a))
    E.frase(c, t, C["s16.a"], [("x", "g", 70, CLARO), ("no", "i", 66, CLARO), ("chão,", "g", 66, BR), ("y", "g", 70, BR), ("na", "i", 66, CLARO), ("parede", "g", 66, BR)],
            XE, 260)
    E.frase(c, t, C["s16.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 62, CLARO), ("bolinha", "i", 62, CLARO), ("aberta", "g", 62, BR)], XE, 380)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.formula(c, "D = [0, 24[", XE, 900, 96, "g", BR, a))
    E.frase(c, t, C["s16.c"], [("a", "i", 60, CLARO), ("ponta", "i", 60, CLARO), ("fica", "i", 60, CLARO), ("de", "g", 60, BR), ("fora", "g", 60, BR)], XE, 480)
    anel(c, t, C["s16.b"] + 0.2, PE, 24, f(24), "#FFE680", 30)
    if t >= C["s16.c"]:
        E.arco(c, PE.x(24), PE.oy, 32, -90, 360 * ease_out(prog(t, C["s16.c"], 0.5)), "#FFE680", 6)


# ---------------- questão ----------------
def loja(c, t, t0, d=1.6):
    eixos(c, t, PL, t0, t0, t0, LX, LY, "mês", "mil R$", size=34)
    E.curva(c, t, t0 + 0.3, PL, g, 0, 12, d=d)
    pontas(c, t, t0 + 0.3 + d, PL, g, 0, 12)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 64, COR), XE, 160)
    loja(c, t, C["s17.a"])
    E.frase(c, t, C["s17.a"], [("saldo", "g", 70), ("de", "i", 66), ("uma", "i", 66), ("lojinha", "g", 70, COR)], XE, 280)
    E.frase(c, t, C["s17.b"], [("12", "g", 60, ENT), ("meses", "i", 58), ("·", "g", 58, TINTA2), ("y", "g", 60), ("em", "i", 58), ("mil", "i", 58), ("R$", "g", 60)],
            XE, 370)
    perguntas = (("s17.c", "1", [("maior", "i", 56), ("saldo?", "g", 56), ("mês?", "g", 56, ENT)]),
                 ("s17.d", "2", [("saldo", "i", 56), ("zero:", "i", 56), ("meses?", "g", 56, ENT)]),
                 ("s17.e", "3", [("cresceu", "g", 56, SOBE), ("quando?", "i", 56)]),
                 ("s17.f", "4", [("imagem?", "g", 56)]))
    for i, (k, n, partes) in enumerate(perguntas):
        yy = 520 + i * 115
        E.foco(c, t, C[k], 0.5, lambda a, n=n, yy=yy: (E.bola(c, XE + 34, yy - 20, 34, a=a), centro(c, n, XE + 34, yy - 4, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 100, yy)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=820, cy=820, r=70)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    loja(c, t, C["s19"] - 3, 0.1)

    def s19():
        E.ponto(c, t, C["s19.a"], PL, 9, 6, cor=COR, r=17)
        anel(c, t, C["s19.a"] + 0.2, PL, 9, 6, COR, 32)
        E.foco(c, t, C["s19.a"], 0.5, lambda a: par(c, "9", "6", XE, 260, 90, a))
        E.foco(c, t, C["s19.a"] + 0.3, 0.4, lambda a: par(c, "9", "6", PL.x(9) - 50, PL.y(6) - 46, 40, a))
        guia(c, t, C["s19.b"], PL, 9, 6, "y")
        marca_eixo(c, t, C["s19.b"] + 0.4, PL, 6, "y", SAI)
        E.frase(c, t, C["s19.b"], [("maior", "i", 60), ("saldo:", "i", 60), ("6", "g", 76), ("mil", "g", 66), ("reais", "g", 66)], XE, 400)
        guia(c, t, C["s19.c"], PL, 9, 6, "x")
        marca_eixo(c, t, C["s19.c"] + 0.4, PL, 9, "x", ENT)
        E.frase(c, t, C["s19.c"], [("no", "i", 60), ("mês", "i", 60), ("9", "g", 76, ENT)], XE, 510)
        for i, xv in enumerate((1, 5)):
            anel(c, t, C["s19.d"] + 0.4 * i, PL, xv, 0, SAI, 26)
            E.ponto(c, t, C["s19.d"] + 0.4 * i, PL, xv, 0, cor=SAI, r=13)
            marca_eixo(c, t, C["s19.d"] + 0.4 * i + 0.3, PL, xv, "x", ENT)
        E.frase(c, t, C["s19.d"], [("saldo", "i", 60), ("zero:", "i", 60), ("meses", "i", 60), ("1", "g", 76, ENT), ("e", "i", 60), ("5", "g", 76, ENT)], XE, 680)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    trecho(c, t, C["s20.a"], PL, g, 0, 3, DESCE)
    seta_curva(c, PL, g, 1.6, DESCE, ep(t, C["s20.a"] + 0.8, 0.3), 0.4)
    trecho(c, t, C["s20.b"], PL, g, 3, 9, SOBE)
    seta_curva(c, PL, g, 6.4, SOBE, ep(t, C["s20.b"] + 0.8, 0.3), 0.4)
    E.frase(c, t, C["s20.a"], [("desce", "g", 64, DESCE), ("até", "i", 62), ("o", "i", 62), ("mês", "i", 62), ("3", "g", 66, ENT)], XE, 260)
    E.frase(c, t, C["s20.b"], [("sobe", "g", 64, SOBE), ("do", "i", 62), ("3", "g", 66, ENT), ("ao", "i", 62), ("9", "g", 66, ENT)], XE, 370)
    barra(c, t, C["s20.c"], PL, "x", 3, 9, SOBE, larg=10, r=11)
    E.frase(c, t, C["s20.c"], [("cresceu:", "g", 62, SOBE), ("de", "i", 62), ("3", "g", 66, ENT), ("a", "i", 62), ("9", "g", 66, ENT)], XE, 500)
    projecao(c, t, C["s20.d"] - 0.3, PL, g, 0, 12, "y", SAI, d=1.0, passo=0.5, alfa=0.2)
    barra(c, t, C["s20.d"] + 0.4, PL, "y", -4, 6, SAI, d=1.0)
    E.frase(c, t, C["s20.d"], [("sombra", "i", 62), ("no", "i", 62), ("y:", "g", 62), ("−4", "g", 66), ("a", "i", 62), ("6", "g", 66)], XE, 650)
    E.foco(c, t, C["s20.e"], 0.5, lambda a: E.formula(c, "Im = [−4, 6]", XE, 820, 96, "g", SAI, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", [("valor", "g", 76), ("é", "i", 76), ("o", "i", 76), ("y,", "g", 76), ("momento", "g", 76, ENT), ("é", "i", 76), ("o", "i", 76), ("x", "g", 76, ENT)]),
                 ("s21.b", [("zero:", "g", 76), ("a", "i", 76), ("curva", "i", 76), ("toca", "g", 76, COR), ("o", "i", 76), ("eixo", "i", 76), ("x", "g", 76, ENT)]),
                 ("s21.c", [("crescente:", "g", 76, SOBE), ("leia", "i", 76), ("da", "i", 76), ("esquerda", "i", 76), ("para", "i", 76), ("a", "i", 76),
                            ("direita", "i", 76)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a),
                                                         E.escreve(c, str(i + 1), 230 - E.larg(str(i + 1), "g", 60) / 2, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s22.a"], [("praticar", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s22.a"] + 0.8, ps("fórmulas, tabelas e gráficos", "i", 60, TINTA2), XE, 580, passo=0.1)
    E.frase(c, t, C["s22.b"], [("pede", "i", 76), ("o", "i", 76), ("x", "g", 90, ENT), ("ou", "i", 76), ("o", "i", 76), ("y?", "g", 90)], XE, 720)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ler=b_ler, maximo=b_maximo, zeros=b_zeros, cresce=b_cresce, dominio=b_dominio,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
