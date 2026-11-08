"""Visual — Estudativo · MAT-PRO-002: padrões em figuras (palitos).

Linguagem visual da trilha Progressões (definida em MAT-PRO-001): posição (n, "figura 1", "1º") em índigo (ENT); termo / valor em
preto (SAI); casa() = caixa com o valor dentro e a posição embaixo; an(k) escreve a₁, aₙ; tabela figura | palitos com "+3" em
setas curvas (seta_curva()); regra de figura em figura = o aumento numa pílula; atalho no palco escuro.
Nesta aula: palitos grossos de pontas redondas (palito(), fileira(), hexagonos()); os palitos NOVOS de cada figura acendem na cor da
matéria; o palito de partida e o palito de divisa ganham destaque; divisas contadas duas vezes piscam em vermelho no erro;
quadrados 1×1, 2×2, 3×3 (grade_q()) no "não compensa"."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # posição / índice · termo / valor
ARQUIVO_FINAL = "estudativo_MAT-PRO-002_padroes_em_figuras.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("contar", "lei", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

P = lambda n: 3 * n + 1
assert [P(n) for n in (1, 2, 3, 4)] == [4, 7, 10, 13] and P(50) == 151 and 4 + 3 * 49 == 151 and 4 * 50 - 49 == 151
assert [n * n for n in (1, 2, 3)] == [1, 4, 9]
H5 = lambda n: 5 * n + 1
assert [H5(n) for n in (1, 2, 3)] == [6, 11, 16] and H5(40) == 201 and (91 - 1) / 5 == 18


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def _pedacos(s):
    """separa a escrita em trechos normais e índices: "log_2 x" → [("log", 0), ("2", 1), (" x", 0)]; "_{f{1}{2}}" vale inteiro"""
    out, i, txt = [], 0, ""
    while i < len(s):
        if s[i] == "_" and i + 1 < len(s):
            if txt:
                out.append((txt, 0))
                txt = ""
            if s[i + 1] == "{":
                k, j = 1, i + 2
                while k:
                    k += {"{": 1, "}": -1}.get(s[j], 0)
                    j += 1
                out.append((s[i + 2:j - 1], 1))
                i = j
            else:
                out.append((s[i + 1], 1))
                i += 2
        else:
            txt += s[i]
            i += 1
    if txt:
        out.append((txt, 0))
    return out


def fl(c, s, x, y, size, est="g", cor=TINTA, a=1.0):
    """E.formula com índice: o trecho depois de "_" sai pequeno e rebaixado (a₁, aₙ₊₁). Devolve a largura"""
    w = 0.0
    for txt, sub in _pedacos(s):
        if sub:
            w += E.formula(c if a > 0 else None, txt, x + w + size * 0.02, y + size * (0.34 if "f{" in txt else 0.2), size * 0.56, est, cor,
                           a) + size * 0.04
        else:
            w += E.formula(c if a > 0 else None, txt, x + w, y, size, est, cor, a)
    return w


def fx(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """fórmula em pedaços de cor: partes = [(escrita, cor[, opacidade])]; "^x" sozinho é o expoente do pedaço anterior.
    Devolve (largura, [x de cada pedaço], [largura de cada pedaço])."""
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


def par(c, xv, yv, x, y, size, a=1.0, align="left"):
    """par ordenado (x, y): x em índigo, y em preto"""
    return fx(c, [("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA)], x, y, size, a, align)


def anel(c, t, t0, X, Y, cor=None):
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def celula(c, s, cx, cy, size, cor, a):
    if "f{" in s:
        E.formula(c, s, cx, cy + size * 0.25, size * 0.92, "g", cor, a, "center")
    else:
        E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def tabela(c, t, x0, y0, cols, tc, wc=200, hl=100, size=62, luz=None):
    """tabela em pé: cols = [(cabeçalho em partes de fx, cor dos valores, valores, instante de cada valor)]; luz(i) = destaque da linha"""
    n, nl = len(cols), len(cols[0][2])
    a = ep(t, tc, 0.5)
    if a > 0:
        for j, (cab, _, _, _) in enumerate(cols):
            fx(c, cab, x0 + wc * (j + 0.5), y0 - 34, 56, a, "center")
        M.line(c, x0, y0, x0 + n * wc, y0, TINTA, a, 4)
        for j in range(1, n):
            M.line(c, x0 + wc * j, y0, x0 + wc * j, y0 + hl * nl + 10, TINTA, a, 4)
    for i in range(nl):
        cy = y0 + 10 + hl * i + hl / 2
        if luz is not None:
            q = luz(i)
            if q > 0:
                M.rrect(c, x0 - 8, cy - hl / 2 + 4, n * wc + 16, hl - 8, 14, COR, 0.14 * q)
        for j, (_, cor, vals, tv) in enumerate(cols):
            if tv[i] is not None:
                E.foco(c, t, tv[i], 0.4, lambda q, s=vals[i], j=j, cy=cy, cor=cor: celula(c, s, x0 + wc * (j + 0.5), cy, size, cor, q), sobe=6)


def luz_de(t, ks, fim):
    """destaque da linha i entre o instante dela (ks[i]) e o próximo"""
    def luz(i):
        k = ks[i]
        if k is None:
            return 0.0
        nxt = [v for v in ks if v is not None and v > k]
        t1 = min(nxt) if nxt else fim
        return ep(t, k, 0.3) * (1 - ep(t, t1 - 0.2, 0.3))
    return luz


def eqn(c, esq, dir_, y, size, a=1.0, xi=W / 2, op="=", cor_op=SAI):
    """equação ou inequação com o sinal (op) centrado em xi: esq e dir_ em partes de fx. Devolve (xs, ws) de cada lado"""
    gap = size * 0.28
    wi = E.larg(op, "g", size)
    _, xe, we = fx(c, esq, xi - wi / 2 - gap, y, size, a, "right")
    if a > 0:
        E.escreve(c, op, xi - wi / 2, y, size, "g", cor_op, a)
    _, xd, wd = fx(c, dir_, xi + wi / 2 + gap, y, size, a)
    return (xe, we), (xd, wd)


def eqn_em(c, t, t0, esq, dir_, y, size, xi=W / 2, op="=", cor_op=SAI, d=0.5):
    E.foco(c, t, t0, d, lambda a: eqn(c, esq, dir_, y, size, a, xi, op, cor_op))


def caixa(c, x, y, w, size, a, cor=None, dois=False):
    """contorno num pedaço de fórmula (x = borda, y = linha de base, w = largura)"""
    if a <= 0:
        return
    alto = size * (1.62 if dois else 1.0)
    topo = y - size * (1.12 if dois else 0.82)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - size * 0.08, topo, w + size * 0.12, alto + size * 0.1), 16, 16),
                M.paint(cor or COR, a, stroke=5))


def nota(c, t, t0, txt, x, y, size=46, fundo=None, cor="#FFFFFF"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, x, y, size, "g", fundo=fundo or COR, cor=cor, a=a), sobe=6)


def nota_fx(c, t, t0, partes, cx, cy, size=48, fundo=None):
    """pílula com fórmula dentro (para log₂ e potências)"""
    def d(a):
        w = fx(c, partes, 0, 0, size, 0)[0]
        h = size * 1.7
        M.rrect(c, cx - w / 2 - size * 0.55, cy - h / 2, w + size * 1.1, h, h / 2, fundo or COR, a)
        fx(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.4, d, sobe=6)




def seta_curva(c, t, t0, A, B, bojo, rot=None, cor=None, size=36, d=0.5, escuro=False, largura=5):
    """seta curva de A até B (pixels), barriga de `bojo` px para a esquerda de quem anda de A para B; rot numa pílula no meio"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or (CLARO if escuro else COR)
    (x0, y0), (x1, y1) = A, B
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1.0
    nx, ny = dy / n, -dx / n
    qx, qy = (x0 + x1) / 2 + nx * bojo, (y0 + y1) / 2 + ny * bojo
    pt = lambda s: ((1 - s) ** 2 * x0 + 2 * (1 - s) * s * qx + s * s * x1, (1 - s) ** 2 * y0 + 2 * (1 - s) * s * qy + s * s * y1)
    path = skia.Path()
    path.moveTo(x0, y0)
    for i in range(1, 31):
        path.lineTo(*pt(p * i / 30))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.9:
        ex, ey = pt(1.0)
        ux, uy = ex - qx, ey - qy
        k = math.hypot(ux, uy) or 1.0
        ux, uy = ux / k, uy / k
        tri = skia.Path()
        tri.moveTo(ex + ux * 6, ey + uy * 6)
        tri.lineTo(ex - ux * 20 - uy * 12, ey - uy * 20 + ux * 12)
        tri.lineTo(ex - ux * 20 + uy * 12, ey - uy * 20 - ux * 12)
        tri.close()
        c.drawPath(tri, M.paint(cor, ep(t, t0 + d * 0.9, 0.15)))
    if rot:
        mx, my = pt(0.5)
        w = E.larg(rot, "g", size) + size * 1.1
        s = 1 if bojo >= 0 else -1
        off = abs(nx) * (w / 2 + 6) + abs(ny) * (size * 0.8 + 6)
        E.foco(c, t, t0 + d * 0.5, 0.4, lambda a: E.pilula(c, rot, mx + s * nx * off, my + s * ny * off, size, "g",
                                                          fundo=cor, cor="#07070F" if escuro else E.SOBRE, a=a), sobe=6)




# ---------------- peças de Progressões (as próximas aulas copiam daqui) ----------------
def casa(c, cx, cy, val, pos=None, a=1.0, s=150, borda=None, cor_val=None, luz=0.0, size=None, pos_size=44):
    """o termo numa caixa: valor dentro (preto), posição embaixo (índigo). luz (0..1) pinta o fundo de índigo claro.
    val = "?" sai em cinza; val = "" deixa a caixa vazia."""
    if a <= 0:
        return
    x, y = cx - s / 2, cy - s / 2
    M.rrect(c, x, y, s, s, 22, "#FFFFFF", a)
    if luz > 0:
        M.rrect(c, x, y, s, s, 22, COR, 0.16 * luz * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, s, s), 22, 22), M.paint(borda or COR, a, stroke=5))
    if val != "":
        k = size or (s * 0.46 if len(val) <= 2 else s * 0.36 if len(val) <= 3 else s * 0.28)
        centro(c, val, cx, cy + k * 0.36, k, "g", cor_val or (CINZA if val == "?" else TINTA), a)
    if pos:
        centro(c, pos, cx, cy + s / 2 + pos_size + 14, pos_size, "b", COR, a)


def casa_em(c, t, t0, cx, cy, val, pos=None, s=150, **kw):
    E.foco(c, t, t0, 0.45, lambda a: casa(c, cx, cy, val, pos, a, s, **kw), sobe=10)


def ordinal(n):
    return f"{n}º"


def an(k, cor_a=None, cor_i=None):
    """partes de fx para "a" com índice k (a₁, aₙ, aₙ₊₁): letra em preto, índice (a posição) em índigo"""
    return [("a", cor_a or SAI), ("_{" + str(k) + "}", cor_i or ENT)]


def xs_fila(x0, n, s=150, gap=30):
    return [x0 + s / 2 + i * (s + gap) for i in range(n)]


def reticencias(c, cx, cy, a=1.0, cor=None):
    if a > 0:
        for dx in (-26, 0, 26):
            c.drawCircle(cx + dx, cy, 8, M.paint(cor or TINTA2, a))


# ---------------- a máquina (a mesma de MAT-FUN-003): a posição entra, o termo sai ----------------
def esfera(c, X, Y, s, cor, a=1.0, r=62, size=None):
    if a <= 0:
        return
    size = size or (r * 0.95 if len(s) < 3 else r * 0.62 if len(s) < 5 else r * 0.5)
    E.bola(c, X, Y, r, cor, a)
    centro(c, s, X, Y + size * 0.36, size, "g", BR, a)


def maquina(c, cx, cy, regra, a=1.0, w=520, h=280, size=72, rotulos=("posição", "termo"), nome="a"):
    """caixa escura com a regra; boca de entrada (índigo, a posição) à esquerda e de saída (o termo) à direita"""
    if a <= 0:
        return
    sh = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a))
    sh.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 10, cy - h / 2 + 18, w, h), 40, 40), sh)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 40, TINTA, a)
    M.rrect(c, cx - w / 2 - 22, cy - 66, 44, 132, 14, ENT, a)
    M.rrect(c, cx + w / 2 - 22, cy - 66, 44, 132, 14, TINTA2, a)
    if nome:
        E.escreve(c, nome, cx - w / 2 + 36, cy - h / 2 + 74, 64, "i", CLARO, a)
    if regra:
        E.formula(c, regra, cx, cy + size * 0.36 + 14, size, "g", BR, a, "center")
    if rotulos:
        centro(c, rotulos[0], cx - w / 2 - 150, cy + 120, 44, "i", ENT, a)
        centro(c, rotulos[1], cx + w / 2 + 150, cy + 120, 44, "i", SAI, a)


def passa(c, t, cx, cy, ent, sai, t_in, t_out, w=520, some=None, r=58, dist=260):
    """a posição rola até a boca e some; o termo nasce na outra boca e anda para fora. some = instante em que tudo vai embora"""
    fim = 1.0 if some is None else 1 - ep(t, some, 0.4)
    if fim <= 0:
        return
    p = ease_io(prog(t, t_in, 0.8))
    if ent is not None:
        if 0 < p < 1:
            esfera(c, lerp(cx - w / 2 - dist, cx - w / 2 - 10, p), cy, ent, ENT, (1 - ep(t, t_in + 0.55, 0.25)) * fim, r)
        elif p <= 0 and t >= t_in - 0.6:
            esfera(c, cx - w / 2 - dist, cy, ent, ENT, ep(t, t_in - 0.6, 0.4) * fim, r)
    if sai is not None:
        q = ease_out(prog(t, t_out, 0.8))
        if q > 0:
            esfera(c, lerp(cx + w / 2, cx + w / 2 + dist, q), cy, sai, SAI, min(1, q * 3) * fim, r)


def passos(c, t, xs, cy, ts, rot, s=150, cor=None, escuro=False, size=34):
    """setas curvas por cima da fila, de uma caixa para a seguinte, com a regra numa pílula: a recorrência"""
    for i, t0 in enumerate(ts):
        if t0 is None:
            continue
        A = (xs[i] + s * 0.18, cy - s / 2 - 8)
        B = (xs[i + 1] - s * 0.18, cy - s / 2 - 8)
        seta_curva(c, t, t0, A, B, 70, rot, cor=cor, escuro=escuro, size=size)


def bola_res(c, t, t0, txt, cx, cy, r, size, sub=None, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor or CERTO, a), fx(c, txt if isinstance(txt, list) else [(txt, BR)], cx,
                                                                                 cy + size * 0.36 - (24 if sub else 0), size, a, "center"),
                                     sub and centro(c, sub, cx, cy + size * 0.36 + 50, 46, "i", BR, a)))




# ---------------- palitos ----------------
def palito(c, x0, y0, x1, y1, cor=None, a=1.0, w=10, gap=9):
    """um palito: segmento grosso com as pontas arredondadas, um pouco mais curto que o lado (os cantos ficam abertos)"""
    if a <= 0:
        return
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1.0
    ux, uy = dx / n, dy / n
    M.line(c, x0 + ux * gap, y0 + uy * gap, x1 - ux * gap, y1 - uy * gap, cor or TINTA, a, w)


def fileira(c, x, y, n, l, a=1.0, cor=None, w=10):
    """fileira de n quadradinhos de lado l; (x, y) = canto de cima à esquerda. cor(id) → cor (ou None para não desenhar);
    ids: "p" = palito de partida (em pé, na ponta esquerda); (i, "c"), (i, "b"), (i, "d") = cima, baixo e direita do quadradinho i (de 0)"""
    if a <= 0:
        return
    cor = cor or (lambda k: TINTA)
    k = cor("p")
    if k:
        palito(c, x, y, x, y + l, k, a, w)
    for i in range(n):
        x0 = x + i * l
        for lado, (p0, p1) in (("c", ((x0, y), (x0 + l, y))), ("b", ((x0, y + l), (x0 + l, y + l))), ("d", ((x0 + l, y), (x0 + l, y + l)))):
            k = cor((i, lado))
            if k:
                palito(c, *p0, *p1, k, a, w)


def hexagonos(c, cx0, cy, n, r, a=1.0, cor=None, w=9):
    """fileira de n hexágonos de lados em pé, vizinhos dividindo o lado vertical; cx0, cy = centro do primeiro.
    cor(id) → cor; ids: (i, k) com k = 0..5 (0 = lado esquerdo em pé; o lado direito de i é o esquerdo de i + 1)"""
    if a <= 0:
        return
    cor = cor or (lambda k: TINTA)
    dxh = r * math.sqrt(3)
    for i in range(n):
        cx = cx0 + i * dxh
        pts = [(cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))) for ang in (150, 210, 270, 330, 30, 90)]
        # lados: 0 = esquerda (150→210), 1 = baixo-esq, 2 = baixo-dir, 3 = direita (330→30), 4 = cima-dir, 5 = cima-esq
        for k in range(6):
            if k == 0 and i > 0:
                continue  # o lado esquerdo é o direito do vizinho
            q = cor((i, k))
            if q:
                palito(c, *pts[k], *pts[(k + 1) % 6], q, a, w, gap=8)


def grade_q(c, x, y, n, l, a=1.0, cor=None, w=7):
    """quadrado n × n de quadradinhos de lado l (contagem de quadradinhos, não de palitos)"""
    if a <= 0:
        return
    cor = cor or TINTA
    for i in range(n + 1):
        M.line(c, x, y + i * l, x + n * l, y + i * l, cor, a, w)
        M.line(c, x + i * l, y, x + i * l, y + n * l, cor, a, w)


def rotulo_fig(c, t, t0, n, x, y, size=50):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, f"figura {n}", x, y, size, "i", TINTA2, a), sobe=6)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        l = 130
        E.foco(c, t, C["s01.a"], 0.5, lambda a: fileira(c, XE, 260, 1, l, a, lambda k: COR, 11))
        E.foco(c, t, C["s01.a"] + 0.8, 0.4, lambda a: E.escreve(c, "4 palitos", XE + l + 50, 345, 64, "g", TINTA, a))
        # a fileira longa, que some à direita
        l2 = 90
        p = ease_out(prog(t, C["s01.b"], 1.4))
        if p > 0:
            n = max(1, int(round(17 * p)))
            for i in range(n):  # some aos poucos à direita: a fileira continua
                k = 1 - max(0.0, (i - 10) / 7)
                x0 = XE + i * l2
                if i == 0:
                    palito(c, x0, 560, x0, 560 + l2, TINTA, k, 8)
                palito(c, x0, 560, x0 + l2, 560, TINTA, k, 8)
                palito(c, x0, 560 + l2, x0 + l2, 560 + l2, TINTA, k, 8)
                palito(c, x0 + l2, 560, x0 + l2, 560 + l2, TINTA, k, 8)
        E.foco(c, t, C["s01.b"] + 0.6, 0.4, lambda a: E.pilula(c, "50 quadradinhos", 1560, 480, 50, "g", a=a), sobe=6)
        E.foco(c, t, C["s01.c"], 0.4, lambda a: fx(c, [("4 × 50 = 200", ERRADO)], XE, 860, 100, a))
        if t >= C["s01.c"] + 0.6:
            E.risco(c, XE - 10, 880, XE + 640, 790, t, C["s01.c"] + 0.6, largura=12)
        bola_res(c, t, C["s01.d"], "151", 1300, 830, 130, 110)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 300)
    E.frase(c, t, tb + 1.2, [("de", "i", 100), ("onde", "i", 100), ("vem", "i", 100), ("o", "i", 100), ("151", "g", 120, COR)], XE, 470)
    E.frase(c, t, tb + 3.0, [("a", "i", 100), ("lei", "g", 120, COR), ("da", "i", 100), ("figura", "g", 110)], XE, 640)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
LEI = an("n") + [(" = 3", SAI), ("n", ENT), (" + 1", SAI)]


def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("1", "g", 90, COR, C["s03"] + 0.6), ("coisa:", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    E.frase(c, t, C["s03.a"], [("lei", "g", 110, COR), ("de", "i", 100), ("formação", "g", 110, COR)], W / 2, 420, "center")
    cx, cy = W / 2, 720
    E.foco(c, t, C["s03.a"] + 1.0, 0.5, lambda a: maquina(c, cx, cy, "3n + 1", a))
    passa(c, t, cx, cy, "2", "7", C["s03.a"] + 2.0, C["s03.a"] + 3.4)


# ---------------- contar ----------------
L, FX0 = 110, 420
FY = (230, 450, 670)


def novos_de(n, cor_novo, cor_velho=TINTA):
    """cor dos palitos da figura n: os três do último quadradinho na cor nova"""
    def f(k):
        if k != "p" and k[0] == n - 1 and n > 1:
            return cor_novo
        return cor_velho
    return f


def b_contar(c, t, C, b):
    luz_novos = ep(t, C["s05.d"], 0.4)
    for i, (n, k, conta) in enumerate(((1, "s04.a", "4"), (2, "s04.b", "7"), (3, "s05.a", "10"))):
        y = FY[i]
        rotulo_fig(c, t, C[k], n, XE, y + L / 2 + 16)
        cor_n = mix_cor(TINTA, COR, luz_novos)
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, n=n, y=y: fileira(c, FX0, y, n, L, a, novos_de(n, cor_n)))
        tc = C["s04.c"] if n == 2 else C[k] + 0.8
        E.foco(c, t, tc, 0.4, lambda a, n=n, y=y, conta=conta: E.escreve(c, conta, FX0 + n * L + 50, y + L / 2 + 26, 76, "g", COR, a), sobe=6)
    E.saida(c, t, C["s05"] - 0.1, lambda: E.foco(c, t, C["s04.c"] + 0.4, 0.4, lambda a: E.escreve(c, "não 8", FX0 + 2 * L + 160, FY[1] + L / 2 + 22, 56, "i", ERRADO, a)))
    # o palito do meio: dividido
    q = pulso(t, C["s04.d"], 3.0)
    if q > 0:
        X = FX0 + L
        palito(c, X, FY[1], X, FY[1] + L, COR, q, 16)
        E.foco(c, t, C["s04.d"] + 0.2, 0.3, lambda a: E.pilula(c, "dividido", X, FY[1] - 46, 40, "g", a=a * q), sobe=4)
    # o da esquerda do quadradinho novo já estava
    q = pulso(t, C["s05.e"], 3.0)
    if q > 0:
        for i, n in ((1, 2), (2, 3)):
            X = FX0 + (n - 1) * L
            palito(c, X, FY[i], X, FY[i] + L, TINTA2, q, 16)
        E.foco(c, t, C["s05.e"] + 0.2, 0.3, lambda a: E.pilula(c, "já estava", FX0 + 2 * L, FY[2] + L + 60, 40, "g", fundo=TINTA2, a=a * q), sobe=4)
    if t < C["s05"]:
        return
    # tabela figura | palitos, com +3 entre as linhas
    TX, TYb = 1100, 330
    ks = [C["s05.b"], C["s05.b"] + 0.7, C["s05.b"] + 1.4]
    tabela(c, t, TX, TYb, [([("figura", ENT)], ENT, ["1", "2", "3"], [C["s05.b"] - 0.3] * 3), ([("palitos", SAI)], SAI, ["4", "7", "10"], ks)],
           C["s05.b"] - 0.4, wc=220, hl=110)
    ry = lambda i: TYb + 10 + 110 * i + 55
    X = TX + 2 * 220 + 20
    for i in range(2):
        seta_curva(c, t, C["s05.c"] + 0.3 * i, (X, ry(i)), (X, ry(i + 1)), -46, "+3", size=34)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "3 palitos novos", TX + 220, 760, 48, "g", a=a), sobe=6)
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "cima, baixo e direita", TX + 20, 880, 50, "i", COR, a))


def mix_cor(c1, c2, k):
    return E.mix(c1, c2, max(0.0, min(1.0, k)))


# ---------------- lei ----------------
def b_lei(c, t, C, b):
    if t < C["s08"]:
        l, x0, y0 = 200, 460, 170
        qb = ep(t, C["s06.b"], 0.4)
        E.foco(c, t, C["s06"] - 0.5, 0.5, lambda a: fileira(c, x0, y0, 3, l, a, lambda k: TINTA if k == "p" else mix_cor(TINTA, COR, qb), 13))
        q = pulso(t, C["s06.a"], 2.5)
        if q > 0:
            palito(c, x0, y0, x0, y0 + l, COR, q, 22)
        E.foco(c, t, C["s06.a"] + 0.2, 0.4, lambda a: E.pilula(c, "1 de partida", x0 - 10, y0 + l + 60, 42, "g", fundo=TINTA, a=a), sobe=6)
        for i in range(3):
            E.foco(c, t, C["s06.b"] + 0.25 * i, 0.4, lambda a, i=i: E.pilula(c, "+3", x0 + l * (i + 0.6), y0 - 46, 40, "g", a=a), sobe=6)
        E.foco(c, t, C["s06.b"] + 1.0, 0.4, lambda a: E.escreve(c, "n quadradinhos: n vezes 3", x0 + 3 * l + 60, y0 + l / 2 + 18, 48, "i", TINTA2, a))
        fx_em(c, t, C["s06.c"], [("P = 3", SAI), ("n", ENT), (" + 1", SAI)], W / 2, 640, 140, "center")
        E.foco(c, t, C["s06.c"] + 1.6, 0.4, lambda a: E.escreve(c, "P = número de palitos", W / 2 - 280, 730, 48, "i", TINTA2, a))
        if t >= C["s07"]:
            fx_em(c, t, C["s07.a"], [("figura ", TINTA2), ("1", ENT), (":  3 · 1 + 1 = ", SAI), ("4", COR)], XE, 860, 64)
            fx_em(c, t, C["s07.b"], [("figura ", TINTA2), ("2", ENT), (":  3 · 2 + 1 = ", SAI), ("7", COR)], XE, 960, 64)
            E.foco(c, t, C["s07.b"] + 1.6, 0.4, lambda a: E.selo(c, XE + 760, 900, 44, True, a))
            E.foco(c, t, C["s07.c"], 0.4, lambda a: (E.pilula(c, "a mesma lei da aula passada", 1440, 870, 44, "g", fundo=TINTA, a=a),
                                                     fx(c, LEI, 1440, 990, 70, a, "center")), sobe=6)
        return

    def s08():
        fx_em(c, t, C["s08"], [("figura ", TINTA2), ("50", ENT)], XE, 230, 90)
        fx_em(c, t, C["s08.a"], [("P = 3 · ", SAI), ("50", ENT), (" + 1 = 150 + 1", SAI)], XE, 450, 110)
        fx_em(c, t, C["s08.b"], [("= ", SAI), ("151", COR)], 815, 620, 120)
        bola_res(c, t, C["s08.b"] + 0.6, "151", 1500, 330, 140, 100, "palitos")
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], ps("outro jeito de ver", "i", 70, TINTA2), XE, 200)
    l, x0, y0 = 120, XE, 300
    qa, qb = ep(t, C["s09.a"], 0.4), ep(t, C["s09.b"], 0.4)

    def cor4(k):
        primeiro = k == "p" or k[0] == 0
        return mix_cor(TINTA, COR, qa) if primeiro else mix_cor(TINTA, TINTA2, qb)
    E.foco(c, t, C["s09"], 0.5, lambda a: fileira(c, x0, y0, 5, l, a, cor4, 11))
    E.foco(c, t, C["s09"] + 0.3, 0.4, lambda a: reticencias(c, x0 + 5 * l + 70, y0 + l / 2, a))
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "4", x0 + l / 2, y0 + l + 60, 46, "g", a=a), sobe=6)
    if qb > 0:
        E.chave(c, x0 + l + 6, x0 + 5 * l + 120, y0 + l + 34, TINTA2, qb, 24)
    E.foco(c, t, C["s09.b"] + 0.2, 0.4, lambda a: E.escreve(c, "os outros 49: 3 cada", x0 + 2 * l, y0 + l + 110, 50, "i", TINTA2, a))
    fx_em(c, t, C["s09.b"] + 2.4, [("49 · 3 = 147", SAI)], XE, 700, 96)
    fx_em(c, t, C["s09.c"], [("4", COR), (" + 147 = ", SAI), ("151", COR)], XE, 860, 110)
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "mesma contagem", 1400, 830, 54, "g", fundo=CERTO, a=a), sobe=6)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    l, y0, n = 140, 330, 5
    junta = ease_io(prog(t, C["s11.a"] - 0.2, 1.0))
    gap = lerp(50, 0, junta)
    x0 = 260
    E.frase(c, t, C["s10.a"], [("4", "g", 90, ERRADO), ("×", "g", 90, ERRADO), ("50?", "g", 90, ERRADO)], XE, 200)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "= 200", XE + 420, 200, 90, "g", ERRADO, a))
    E.foco(c, t, C["s10.b"] + 0.8, 0.4, lambda a: E.escreve(c, "cada um com 4 só para ele", XE + 800, 190, 50, "i", TINTA2, a))
    for i in range(n):
        x = x0 + i * (l + gap)
        E.foco(c, t, C["s10.a"] + 0.15 * i, 0.4, lambda a, x=x: (
            palito(c, x, y0, x + l, y0, TINTA, a, 11), palito(c, x, y0 + l, x + l, y0 + l, TINTA, a, 11),
            palito(c, x, y0, x, y0 + l, TINTA, a, 11), palito(c, x + l, y0, x + l, y0 + l, TINTA, a, 11)), sobe=8)
    E.foco(c, t, C["s10.a"] + 0.8, 0.4, lambda a: reticencias(c, x0 + n * (l + gap) + 60, y0 + l / 2, a))
    if junta > 0.98:
        q = ep(t, C["s11.a"] + 0.8, 0.4)
        for i in range(1, n):
            X = x0 + i * l
            palito(c, X, y0, X, y0 + l, ERRADO, q, 15)
        E.foco(c, t, C["s11.a"] + 1.0, 0.4, lambda a: E.pilula(c, "divisa: contada 2 vezes", x0 + l * 2, y0 + l + 70, 44, "g", fundo=ERRADO, a=a), sobe=6)
    fx_em(c, t, C["s11.b"], [("50 quadradinhos → ", SAI), ("49 divisas", ERRADO)], XE, 720, 80)
    fx_em(c, t, C["s11.c"], [("200 − 49 = ", SAI), ("151", CERTO)], XE, 900, 120)
    E.foco(c, t, C["s11.c"] + 1.6, 0.4, lambda a: E.selo(c, XE + 900, 860, 50, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12.a"], [("o", "i", 84, CLARO), ("aumento", "g", 90, BR), ("vira", "i", 84, CLARO), ("o", "i", 84, CLARO),
                                   ("número", "g", 90, BR), ("do", "i", 84, CLARO), ("n", "g", 90, CLARO)], W / 2, 190, "center", passo=0.14)
        xs = [400, 640, 880, 1120]
        for i, v in enumerate(("4", "7", "10", "13")):
            E.foco(c, t, C["s12.b"] - 0.6 + 0.15 * i, 0.4, lambda a, i=i, v=v: (centro(c, v, xs[i], 450, 110, "g", BR, a),
                                                                               centro(c, f"fig. {i + 1}", xs[i], 530, 40, "b", CLARO, a)), sobe=6)
        for i in range(3):
            seta_curva(c, t, C["s12.b"] + 0.3 * i, (xs[i] + 30, 360), (xs[i + 1] - 30, 360), 50, "+3", escuro=True, size=34)
        fx_em(c, t, C["s12.c"], [("3", BR), ("n", CLARO), (" + ?", BR)], 1400, 450, 110)
        fx_em(c, t, C["s12.d"], [("figura 1:  3 · 1 = 3", BR), ("   tem 4", CLARO)], XE, 760, 76)
        fx_em(c, t, C["s12.e"], [("falta 1  →  ", CLARO), ("3", BR), ("n", CLARO), (" + 1", BR)], XE, 920, 96)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return

    def s13a():
        fx_em(c, t, C["s13.a"], [("n", CLARO), (" sobe 1  →  3", BR), ("n", CLARO), (" sobe 3", BR)], W / 2, 330, 96, "center")
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.pilula(c, "o número solto acerta a partida", W / 2, 540, 54, "g", fundo=CLARO, cor="#07070F", a=a))
    E.saida(c, t, C["s13.c"] - 0.1, s13a)
    if t < C["s13.c"]:
        return
    E.frase(c, t, C["s13.c"], [("não", "g", 84, BR), ("compensa:", "i", 80, CLARO), ("o", "i", 80, CLARO), ("aumento", "g", 84, BR),
                               ("muda", "g", 84, CLARO)], W / 2, 190, "center", passo=0.12)
    base = 680
    for i, (n, x) in enumerate(((1, 330), (2, 650), (3, 1050))):
        l = 80
        E.foco(c, t, C["s13.c"] + 1.6 + 0.5 * i, 0.4, lambda a, n=n, x=x, l=l: grade_q(c, x, base - n * l, n, l, a, CLARO, 6))
        E.foco(c, t, C["s13.d"] + 0.4 * i, 0.4, lambda a, n=n, x=x, l=l: centro(c, str(n * n), x + n * l / 2, base + 100, 80, "g", BR, a), sobe=6)
    for i, (rot, xa, xb) in enumerate((("+3", 370, 730), ("+5", 730, 1170))):
        seta_curva(c, t, C["s13.d"] + 1.6 + 0.4 * i, (xa + 30, base + 140), (xb - 30, base + 140), -50, rot, escuro=True, size=34)
    E.foco(c, t, C["s13.e"], 0.4, lambda a: E.pilula(c, "lei: n · n", 1550, 520, 60, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 170)
    r = 62
    dxh = r * math.sqrt(3)
    posic = ((1, XE + 60, "s14.a"), (2, XE + 360, "s14.b"), (3, XE + 820, "s14.b"))
    for n, x, k in posic:
        def cor(kk, n=n):
            if n == 2 and kk == (1, 0):
                return COR
            return TINTA
        hx = x + dxh / 2
        E.foco(c, t, C[k] + (0.4 if n == 3 else 0), 0.5, lambda a, n=n, hx=hx, cor=cor: hexagonos(c, hx, 380, n, r, a, cor))
    q = pulso(t, C["s14.b"] + 0.6, 2.4)
    if q > 0:
        X = XE + 360 + dxh / 2 + dxh / 2
        palito(c, X, 380 - r / 2, X, 380 + r / 2, COR, q, 16, gap=6)
    for n, x, v in ((1, XE + 60, "6"), (2, XE + 360, "11"), (3, XE + 820, "16")):
        E.foco(c, t, C["s14.c"] + 0.5 * (n - 1), 0.4, lambda a, n=n, x=x, v=v: (centro(c, v, x + n * dxh / 2, 540, 70, "g", COR, a),
                                                                              centro(c, f"figura {n}", x + n * dxh / 2, 600, 40, "i", TINTA2, a)), sobe=6)
    E.foco(c, t, C["s14.d"], 0.4, lambda a: (E.escreve(c, "1)", XE, 740, 64, "g", COR, a), E.escreve(c, "a lei", XE + 90, 740, 64, "i", TINTA, a)))
    E.foco(c, t, C["s14.e"], 0.4, lambda a: (E.escreve(c, "2)", XE, 840, 64, "g", COR, a), E.escreve(c, "palitos da figura 40", XE + 90, 840, 64, "i", TINTA, a)))
    E.foco(c, t, C["s14.f"], 0.4, lambda a: (E.escreve(c, "3)", XE, 940, 64, "g", COR, a), E.escreve(c, "qual figura usa 91 palitos", XE + 90, 940, 64, "i", TINTA, a)))
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], 1580, 660, 110)
        E.frase(c, t, C["s15.a"] + 1.4, ps("pista: o que entra?", "i", 50, COR), 1580, 1010, "center", passo=0.08)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s16():
        xs = [400, 640, 880]
        for i, v in enumerate(("6", "11", "16")):
            E.foco(c, t, C["s16"] + 0.2 + 0.15 * i, 0.4, lambda a, i=i, v=v: (centro(c, v, xs[i], 350, 110, "g", TINTA, a),
                                                                             centro(c, f"fig. {i + 1}", xs[i], 430, 40, "b", COR, a)), sobe=6)
        for i in range(2):
            seta_curva(c, t, C["s16.a"] + 0.3 * i, (xs[i] + 30, 260), (xs[i + 1] - 30, 260), 50, "+5", size=34)
        fx_em(c, t, C["s16.b"], [("5", SAI), ("n", ENT), (" + ?", SAI)], 1200, 350, 110)
        fx_em(c, t, C["s16.c"] - 2.0, [("figura 1:  5 · 1 = 5", SAI), ("   são 6", COR)], XE, 620, 76)
        fx_em(c, t, C["s16.c"], [("P = 5", SAI), ("n", ENT), (" + 1", SAI)], XE, 820, 120)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    fx_em(c, t, C["s17"], [("P = 5", SAI), ("n", ENT), (" + 1", SAI)], XE, 190, 80)
    fx_em(c, t, C["s17.a"], [("figura 40:  5 · ", SAI), ("40", ENT), (" + 1 = 200 + 1 = ", SAI), ("201", COR)], XE, 360, 80)
    E.foco(c, t, C["s17.b"] - 1.4, 0.4, lambda a: E.pilula(c, "91 é valor: equação", 1500, 470, 44, "g", fundo=TINTA, a=a), sobe=6)
    fx_em(c, t, C["s17.b"], [("5", SAI), ("n", ENT), (" + 1 = 91", SAI)], XE, 580, 90)
    fx_em(c, t, C["s17.c"], [("5", SAI), ("n", ENT), (" = 90", SAI)], XE + 60, 730, 90)
    fx_em(c, t, C["s17.d"], [("n", ENT), (" = 18", COR)], XE + 120, 880, 90)
    bola_res(c, t, C["s17.d"] + 0.5, "figura 18", 1460, 780, 150, 60)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s18.a", [("conte", "g", 84), ("o", "i", 80), ("que", "i", 80), ("entra", "g", 84, COR)]),
                 ("s18.b", [("o", "i", 80), ("aumento", "g", 84, COR), ("multiplica", "i", 80), ("o", "i", 80), ("n", "g", 84, COR)]),
                 ("s18.c", [("a", "i", 80), ("figura 1", "g", 84), ("acerta", "i", 80), ("o", "i", 80), ("resto", "g", 84, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 250)
    E.frase(c, t, C["s19.a"], [("padrões", "g", 110, COR)], XE, 390)
    E.frase(c, t, C["s19.a"] + 0.3, [("que", "i", 100), ("dão", "i", 100), ("voltas", "g", 110, COR)], XE, 510)
    xs = xs_fila(XE, 7, 100, 18)
    for i, v in enumerate("ABCABC"):
        casa_em(c, t, C["s19.a"] + 0.6 + 0.12 * i, xs[i], 640, v, ordinal(i + 1), 100, pos_size=34)
    E.foco(c, t, C["s19.a"] + 1.4, 0.4, lambda a: reticencias(c, xs[6], 640, a))
    E.foco(c, t, C["s19.b"], 0.4, lambda a: (E.escreve(c, "a letra da posição", XE, 850, 60, "i", TINTA, a),
                                             E.escreve(c, "2.026", XE + 520, 850, 70, "g", COR, a)))
    E.foco(c, t, C["s19.c"], 0.4, lambda a: (E.escreve(c, "o dia daqui a", XE, 950, 60, "i", TINTA, a),
                                             E.escreve(c, "100 dias", XE + 380, 950, 70, "g", COR, a)))
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C["s19.d"] + 0.2, 0.4))
    E.frase(c, t, C["s19.e"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], 1450, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, contar=b_contar, lei=b_lei, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
