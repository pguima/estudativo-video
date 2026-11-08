"""Visual — Estudativo · MAT-EXP-013: função logarítmica, gráfico e inequações.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001): x, expoente e entrada em índigo (ENT); base e saída
em preto (SAI); fx() pinta cada pedaço da fórmula com a sua cor; plano à direita e contas à esquerda; eqn() alinha cada linha
pelo sinal; pinta() mostra a solução na reta (bolinha aberta/fechada e faixa com seta), como em MAT-EXP-005.
Logaritmo na tela: "log_2 x" em fx() escreve a base pequena e rebaixada (log₂ x); "_{f{1}{2}}" aceita base em fração.
Nesta aula: no plano, 2ˣ em preto (a curva já conhecida), log₂ x em índigo e a diagonal y = x tracejada; a dobra leva cada
ponto (a, b) até (b, a) andando na perpendicular da diagonal (dobra()). O eixo y que a curva não toca = faixa clara vertical."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / entrada · base / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-013_funcao_logaritmica_grafico_e_inequacoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("tabela", "dominio", "inequacao", "atalho", "questao", "fim"))
BR = "#FFFFFF"

lg = math.log2
assert [lg(v) for v in (0.25, 0.5, 1, 2, 4, 8)] == [-2, -1, 0, 1, 2, 3] and lg(1024) == 10 and 1024 // 8 == 128 and 10 - 3 == 7
assert 2 ** 3 == 8 and 8 + 1 == 9 and lg(5 - 1) == 2 < 3


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
    """E.formula com índice: o trecho depois de "_" sai pequeno e rebaixado (a base do log). Devolve a largura"""
    w = 0.0
    for txt, sub in _pedacos(s):
        if sub:
            w += E.formula(c if a > 0 else None, txt, x + w + size * 0.02, y + size * (0.34 if "f{" in txt else 0.2), size * 0.56, est, cor,
                           a) + size * 0.14
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


def pinta(c, t, tb, tp, vx, y, v, lado, fecha, xa, xb, cor=None, r=17):
    """solução na reta: bolinha em v (cheia se fecha) em tb e a faixa que pinta para o lado (+1 direita, −1 esquerda) em tp, com seta"""
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


def bolinha(c, X, y, cor, a, r=17):
    if a > 0:
        c.drawCircle(X, y, r, M.paint(E.PAPEL, a))
        c.drawCircle(X, y, r, M.paint(cor, a, stroke=6))


def reta_sol(c, t, t0, x0, x1, y, vmin, vmax, size=44):
    return E.reta(c, t, t0, x0, x1, y, vmin, vmax, list(range(vmin, vmax + 1)), E._num, size=size)


def tenue(c, k, fn):
    """desenha fn com opacidade k (curva que sai de cena sem sumir)"""
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


# ---------------- o plano do espelho ----------------
def plano_espelho(c, t, t0):
    return E.plano(c, t, t0, 1060, 150, 780, 780, -3, 9, -3, 9, marcas_x=[-2, 2, 4, 6, 8], marcas_y=[-2, 2, 4, 6, 8], size=36)


PE = E.Plano(1060, 150, 780, 780, -3, 9, -3, 9)
US = [-3.2 + (math.log2(9.2) + 3.2) * i / 300 for i in range(301)]  # expoentes de 2ˣ do canto de baixo ao topo
PONTOS_EXP = [(u, 2 ** u) for u in US]
PONTOS_LOG = [(2 ** u, u) for u in US]


def dobra(p):
    """2ˣ dobrada na diagonal: cada ponto (a, b) anda em linha reta até (b, a)"""
    return [(lerp(a_, b_, p), lerp(b_, a_, p)) for a_, b_ in PONTOS_EXP]


def rot_log(c, P, x, y, base="2", size=52, cor=None, a=1.0):
    X, Y = P(x, y)
    fx(c, [(f"log_{base} x" if len(base) == 1 else f"log_{{{base}}} x", cor or COR)], X, Y, size, a, "center")


def rot_exp(c, P, x, y, size=52, a=1.0):
    X, Y = P(x, y)
    fx(c, [("2", SAI), ("^x", ENT)], X, Y, size, a, "center")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        fx_em(c, t, C["s01.a"], [("log_2 8 = ", SAI), ("3", COR)], XE, 260, 120)
        E.foco(c, t, C["s01.a"] + 1.0, 0.4, lambda a: (E.escreve(c, "porque", 1180, 250, 54, "i", TINTA2, a),
                                                       fx(c, [("2", SAI), ("^3", COR), (" = 8", SAI)], 1370, 250, 76, a)))
        fx_em(c, t, C["s01.b"], [("log_2 1.024 = ", SAI), ("10", COR)], XE, 430, 120)
        E.foco(c, t, C["s01.b"] + 1.0, 0.4, lambda a: (E.escreve(c, "porque", 1180, 420, 54, "i", TINTA2, a),
                                                       fx(c, [("2", SAI), ("^{10}", COR), (" = 1.024", SAI)], 1370, 420, 76, a)))
        E.frase(c, t, C["s01.c"], [("o", "i", 70), ("número:", "i", 70)], XE, 640)
        fx_em(c, t, C["s01.c"] + 0.3, [("8  →  1.024", SAI)], 640, 640, 100)
        nota(c, t, C["s01.c"] + 0.9, "mais de 100 vezes", 1470, 610, 50, fundo=TINTA)
        E.frase(c, t, C["s01.d"], [("o", "i", 70), ("logaritmo:", "i", 70)], XE, 820)
        fx_em(c, t, C["s01.d"] + 0.3, [("3  →  10", COR)], 640, 820, 100)
        nota(c, t, C["s01.d"] + 0.9, "só + 7", 1270, 790, 50)
        E.frase(c, t, C["s01.d"] + 2.2, [("crescimento", "i", 70), ("preguiçoso", "g", 66, COR)], XE, 990)
    E.saida(c, t, C["s02"] - 0.1, cena1)
    if t < C["s02"]:
        return
    tb, te = C["s02.a"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 280)
    E.frase(c, t, tb + 1.2, [("o", "i", 110), ("gráfico", "g", 120, COR)], XE, 440)
    E.frase(c, t, tb + 2.6, [("o", "i", 110), ("domínio", "g", 120, COR)], XE, 600)
    E.frase(c, t, tb + 4.4, [("inequações", "g", 120, COR)], XE, 760)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("3", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("log_2 8 = 3", SAI)], 430, y, 96, a), E.escreve(c, "é", 1000, y, 70, "i", TINTA2, a),
                                     fx(c, [("2", SAI), ("^3", ENT), (" = 8", SAI)], 1080, y, 96, a))),
             ("s03.b", lambda a, y: (fx(c, [("y = 2", SAI), ("^x", ENT)], 430, y, 100, a),
                                     E.escreve(c, "e o gráfico dela", 860, y, 64, "i", TINTA2, a))),
             ("s03.c", lambda a, y: (fx(c, [("(f{1}{2})", SAI), ("^x", ENT), (" > 8", SAI)], 430, y + 10, 92, a),
                                     E.escreve(c, "base entre 0 e 1:", 860, y - 20, 56, "i", TINTA2, a),
                                     E.escreve(c, "o sinal vira", 860, y + 50, 64, "g", COR, a))))
    for i, (k, fn) in enumerate(itens):
        y = 450 + i * 210
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- tabela do log ----------------
XL = ("f{1}{4}", "f{1}{2}", "1", "2", "4", "8")
YL = ("−2", "−1", "0", "1", "2", "3")
XEX = ("−2", "−1", "0", "1", "2", "3")
YEX = XL
TY = 330


def contas(c, t, C, itens, x=900, y1=640, y2=820, size=110):
    """a conta da vez, à direita: itens = [(k0, k1, partes da conta, partes do resultado, atraso do resultado)]"""
    for k0, k1, l1, l2, dr in itens:
        def d(k0=k0, l1=l1, l2=l2, dr=dr):
            fx_em(c, t, C[k0], l1, x, y1, size)
            fx_em(c, t, C[k0] + dr, l2, x + 60, y2, size)
        if t >= C[k0]:
            if k1:
                E.saida(c, t, C[k1] - 0.1, d)
            else:
                d()


def b_tabela(c, t, C, b):
    fx_em(c, t, C["s04.a"], [("y = log_2 ", SAI), ("x", ENT)], XE, 170, 84)
    ks = [C["s05.b"], C["s05.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]]
    tvy = [k + 1.0 for k in ks]
    luz = luz_de(t, ks, C["s05.end"])
    tabela(c, t, XE, TY, [([("x", ENT)], ENT, XL, ks), ([("y", SAI)], SAI, YL, tvy)], C["s04.a"] + 0.5, luz=luz)
    E.saida(c, t, C["s04.b"] - 0.1, lambda: E.frase(c, t, C["s04.a"] + 2.2, ps("para cada x, pergunte:", "i", 62, TINTA2), 900, 290))
    fx_em(c, t, C["s04.a"] + 3.0, [("2", SAI), ("^?", ENT), (" = ", SAI), ("x", ENT)], 900, 450, 130)
    E.frase(c, t, C["s05"], ps("e abaixo de 1?", "i", 62, TINTA2), 900, 290)
    contas(c, t, C, [("s04.b", "s04.c", [("2", SAI), ("^0", COR), (" = 1", SAI)], [("y = ", SAI), ("0", COR)], 1.0),
                     ("s04.c", "s04.d", [("2", SAI), ("^1", COR), (" = 2", SAI)], [("y = ", SAI), ("1", COR)], 0.8),
                     ("s04.d", "s04.e", [("2", SAI), ("^2", COR), (" = 4", SAI)], [("y = ", SAI), ("2", COR)], 0.8),
                     ("s04.e", "s05.a", [("2", SAI), ("^3", COR), (" = 8", SAI)], [("y = ", SAI), ("3", COR)], 0.8),
                     ("s05.a", "s05.b", [("2", SAI), ("^{−1}", COR), (" = f{1}{2}", SAI)], [("y = ", SAI), ("−1", COR)], 1.0),
                     ("s05.b", None, [("2", SAI), ("^{−2}", COR), (" = f{1}{4}", SAI)], [("y = ", SAI), ("−2", COR)], 1.0)])


# ---------------- o espelho ----------------
def b_espelho(c, t, C, b):
    if t < C["s07"]:
        espelho_tabelas(c, t, C)
        return
    espelho_plano(c, t, C)


def espelho_tabelas(c, t, C):
    vai = ease_io(prog(t, C["s06"] + 0.1, 0.9))
    xl = lerp(XE, 1260, vai)
    E.foco(c, t, C["s06"] - 1, 0.1, lambda a: fx(c, [("y = log_2 ", SAI), ("x", ENT)], xl + 200, 190, 72, a, "center"))
    tabela(c, t, xl, TY, [([("x", ENT)], ENT, XL, [0] * 6), ([("y", SAI)], SAI, YL, [0] * 6)], 0,
           luz=lambda i: (ep(t, C["s06.c"], 0.3) * (1 - ep(t, C["s06.d"] + 1.5, 0.4))) if i == 4 else 0)
    x0 = 260
    E.foco(c, t, C["s06.a"], 0.5, lambda a: fx(c, [("y = 2", SAI), ("^x", ENT)], x0 + 200, 190, 72, a, "center"))
    tabela(c, t, x0, TY, [([("x", ENT)], ENT, XEX, [C["s06.a"] + 0.2] * 6), ([("y", SAI)], SAI, YEX, [C["s06.a"] + 0.4] * 6)],
           C["s06.a"], luz=lambda i: (ep(t, C["s06.b"], 0.3) * (1 - ep(t, C["s06.d"] + 1.5, 0.4))) if i == 4 else 0)
    # os pares no meio: (2, 4) e (4, 2)
    cx = 960
    S = 92
    _, xa, wa = fx(c, [("(", TINTA), ("2", ENT), (", ", TINTA), ("4", SAI), (")", TINTA)], cx, 0, S, 0, "center")
    _, xb, wb = fx(c, [("(", TINTA), ("4", ENT), (", ", TINTA), ("2", SAI), (")", TINTA)], cx, 0, S, 0, "center")
    E.foco(c, t, C["s06.b"] + 0.3, 0.5, lambda a: par(c, "2", "4", cx, 500, S, a, "center"))
    E.foco(c, t, C["s06.c"] + 0.3, 0.5, lambda a: par(c, "4", "2", cx, 760, S, a, "center"))
    if t >= C["s06.d"]:
        # cada número muda de casa: o 2 da entrada vira saída, o 4 da saída vira entrada
        for (x0_, x1_, cor) in ((xa[1] + wa[1] / 2, xb[3] + wb[3] / 2, ENT), (xa[3] + wa[3] / 2, xb[1] + wb[1] / 2, SAI)):
            p = ease_io(prog(t, C["s06.d"] + (0 if cor == ENT else 0.3), 0.7))
            if p > 0:
                M.arrow(c, x0_, 530, lerp(x0_, x1_, p), lerp(530, 680, p), cor, 1.0, 5, 18, 1.0)
    E.saida(c, t, C["s06.e"] - 0.1, lambda: nota(c, t, C["s06.d"] + 0.5, "colunas trocadas", cx, 900, 46, fundo=TINTA))
    if t >= C["s06.e"]:
        nota(c, t, C["s06.e"], "o caminho de volta", cx, 900, 46)
        p = ease_io(prog(t, C["s06.e"] + 0.3, 0.6))
        if p > 0:
            M.arrow(c, 1240, 990, lerp(1240, 680, p), 990, COR, 1.0, 6, 22, 1.0)


def espelho_plano(c, t, C):
    P = plano_espelho(c, t, C["s07"])
    sai_s09 = 1 - ep(t, C["s09"], 0.6)
    # 2ˣ (preto) e o ponto (2, 4)
    k_exp = lerp(1.0, 0.3, ep(t, C["s08"], 0.6)) * sai_s09
    tenue(c, k_exp, lambda: (E.curva(c, t, C["s07"] + 0.4, P, lambda x: 2 ** x, -3.2, math.log2(9.2), d=1.2, cor=SAI)))
    tenue(c, k_exp, lambda: E.foco(c, t, C["s07"] + 1.4, 0.4, lambda a: rot_exp(c, P, 1.2, 7.6, 56, a)))
    sai_pts = 1 - ep(t, C["s08"], 0.5)
    tenue(c, sai_pts, lambda: (E.ponto(c, t, C["s07"] + 1.2, P, 2, 4, cor=SAI),
                               E.foco(c, t, C["s07"] + 1.4, 0.4, lambda a: par(c, "2", "4", *P(-0.2, 4.9), 46, a, "right"))))
    # a diagonal y = x
    k_diag = lerp(1.0, 0.35, ep(t, C["s08"], 0.6)) * sai_s09
    tenue(c, k_diag, lambda: E.curva(c, t, C["s07.a"], P, lambda x: x, -3, 9, d=1.0, cor=TINTA2, largura=5, tracejada=True))
    tenue(c, k_diag, lambda: E.foco(c, t, C["s07.a"] + 0.8, 0.4, lambda a: fx(c, [("y = x", TINTA2)], *P(7.2, 8.3), 46, a, "center")))
    # a dobra
    tb = C["s07.b"]
    p = ease_io(prog(t, tb, 1.6))
    if 0 < p < 1:
        traco(c, P, dobra(p), COR, 0.85)
    if p >= 1:
        traco(c, P, PONTOS_LOG, COR)
        E.foco(c, t, tb + 1.6, 0.4, lambda a: rot_log(c, P, 7.2, 3.9, a=a))
    tenue(c, sai_pts, lambda: (E.ponto(c, t, tb + 1.7, P, 4, 2, cor=COR),
                               E.foco(c, t, tb + 1.9, 0.4, lambda a: par(c, "4", "2", *P(4.4, 0.9), 46, a)),
                               t >= tb + 1.9 and M.line(c, *P(2, 4), *P(4, 2), TINTA2, 0.8, 4, dash=E.TRACO, progress=ep(t, tb + 1.9, 0.5))))

    # texto à esquerda
    def s07():
        E.frase(c, t, C["s07"], ps("trocar x com y", "i", 70), XE, 260)
        E.frase(c, t, C["s07.a"], [("é", "i", 70), ("refletir", "i", 70), ("na", "i", 70)], XE, 380)
        E.frase(c, t, C["s07.a"] + 0.5, [("diagonal", "g", 110, COR)], XE, 520)
        E.foco(c, t, C["s07.a"] + 1.0, 0.4, lambda a: fx(c, [("y = x", TINTA)], XE, 640, 80, a))
        mid = lerp(C["s07.a"], C["s07.b"], 0.3)
        E.frase(c, t, mid, [("não", "g", 58, ERRADO), ("é", "i", 60, TINTA2), ("o", "i", 60, TINTA2), ("eixo", "i", 60, TINTA2),
                            ("y", "i", 60, TINTA2)], XE, 760)
        E.frase(c, t, tb, [("dobre", "g", 90, COR), ("o", "i", 84), ("papel", "i", 84)], XE, 910)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return

    def s08():
        E.frase(c, t, C["s08"], ps("a curva do log", "i", 70), XE, 230)
        if t >= C["s08.a"]:
            E.ponto(c, t, C["s08.a"], P, 1, 0, cor=COR)
            anel(c, t, C["s08.a"], *P(1, 0))
            anel(c, t, C["s08.a"] + 0.8, *P(1, 0))
            E.foco(c, t, C["s08.a"] + 0.3, 0.4, lambda a: par(c, "1", "0", *P(1.3, -1.9), 46, a))
        fx_em(c, t, C["s08.a"] + 0.3, [("log_2 1 = 0", SAI)], XE, 380, 90)
        E.frase(c, t, C["s08.b"], [("sobe", "g", 96, COR)], XE, 530)
        E.foco(c, t, C["s08.b"] + 0.3, 0.4, lambda a: M.arrow(c, XE + 300, 530, XE + 410, 450, COR, a, 8, 26))
        E.foco(c, t, C["s08.b"] + 0.5, 0.4, lambda a: E.escreve(c, "base 2 > 1", XE + 470, 515, 54, "i", TINTA2, a))
        E.frase(c, t, C["s08.c"], ps("cada vez mais devagar", "i", 66), XE, 670)
        # escada: o x dobra (1 → 2 → 4 → 8) para o log subir só 1
        for i, (x0, x1) in enumerate(((1, 2), (2, 4), (4, 8))):
            ti = C["s08.c"] + 0.4 + 0.5 * i
            q = ep(t, ti, 0.4)
            if q > 0:
                M.line(c, *P(x0, i), *P(x1, i), TINTA2, q, 4, dash=E.TRACO)
                M.line(c, *P(x1, i), *P(x1, i + 1), COR, q, 7)
                E.foco(c, t, ti + 0.2, 0.3, lambda a, x1=x1, i=i: E.escreve(c, "+1", P.x(x1) + 12, P.y(i + 0.5) + 16, 40, "g", COR, a))
        E.frase(c, t, C["s08.d"], [("nunca", "g", 90, COR), ("encosta", "g", 90, COR)], XE, 830)
        E.frase(c, t, C["s08.d"] + 0.8, [("no", "i", 70), ("eixo", "i", 70), ("y", "g", 76)], XE, 940)
        q = ep(t, C["s08.d"] + 0.3, 0.5)
        if q > 0:
            M.line(c, P.ox, P.y(-3), P.ox, P.y(0.6), COR, 0.18 * q, 34)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    # base 1/2: desce
    E.curva(c, t, C["s09.a"], P, lambda x: -math.log2(x), 0.11, 9, d=1.2, cor=TINTA)
    E.foco(c, t, C["s09.a"] + 1.0, 0.4, lambda a: rot_log(c, P, 6.6, -1.8, "f{1}{2}", 52, TINTA, a))
    fx_em(c, t, C["s09"], [("base ", TINTA), ("f{1}{2}", TINTA)], XE, 300, 90)
    E.frase(c, t, C["s09.a"], [("desce", "g", 96)], XE + 400, 290)
    E.foco(c, t, C["s09.a"] + 0.3, 0.4, lambda a: M.arrow(c, XE + 720, 230, XE + 820, 310, TINTA, a, 8, 26))
    E.frase(c, t, C["s09.b"] - 0.6, ps("a mesma regra", "i", 66, TINTA2), XE, 500)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (fx(c, [("base > 1", COR)], XE, 660, 80, a), E.escreve(c, "sobe", XE + 470, 660, 76, "g", COR, a)))
    E.foco(c, t, C["s09.b"] + 0.8, 0.5, lambda a: (fx(c, [("0 < base < 1", TINTA)], XE, 820, 80, a),
                                                   E.escreve(c, "desce", XE + 560, 820, 76, "g", TINTA, a)))


# ---------------- domínio ----------------
def b_dominio(c, t, C, b):
    if t < C["s11"]:
        P = plano_espelho(c, t, C["s10"] - 2)
        q = ep(t, C["s10.a"], 0.6)
        if q > 0:
            x, y, w, h = P.caixa
            M.rrect(c, P.ox, y, x + w - P.ox, h, 0, COR, 0.07 * q)
            M.rrect(c, x, y, P.ox - x, h, 0, E.PAPEL2, 0.55 * q)
            E.escreve(c, "nada", P.x(-2.6), P.y(5), 44, "i", TINTA2, q)
        traco(c, P, PONTOS_LOG, COR)
        rot_log(c, P, 7.2, 3.9)
        q = ep(t, C["s10.a"] + 0.4, 0.5)
        if q > 0:
            M.line(c, P.ox, P.y(-3), P.ox, P.y(9), COR, 0.2 * q, 30)
        E.frase(c, t, C["s10.a"], ps("só existe à direita", "i", 66), XE, 250)
        E.frase(c, t, C["s10.a"] + 0.8, [("do", "i", 66), ("eixo", "i", 66), ("y", "g", 70)], XE, 340)
        fx_em(c, t, C["s10.b"], [("2", SAI), ("^{qualquer}", ENT), (" > 0", COR)], XE, 520, 96)
        E.frase(c, t, C["s10.b"] + 0.8, ps("sempre positivo", "i", 54, TINTA2), XE, 600)
        w, xs, ws = fx(c, [("log_2 ", SAI), ("x", ENT)], XE, 0, 110, 0)
        fx_em(c, t, C["s10.c"] - 0.6, [("log_2 ", SAI), ("x", ENT)], XE, 770, 110)
        caixa(c, xs[1], 770, ws[1], 110, ep(t, C["s10.c"], 0.4))
        nota(c, t, C["s10.c"] + 0.3, "logaritmando > 0", XE + 560, 735, 46)
        E.foco(c, t, C["s10.d"], 0.5, lambda a: (E.escreve(c, "domínio:", XE, 930, 66, "i", TINTA, a),
                                                 fx(c, [("]0, +∞[", COR)], XE + 300, 935, 96, a)))
        return
    # log(x − 3): base 10 escondida
    S = 150
    q10 = ep(t, C["s11.b"], 0.5)
    partes = [("log", SAI), ("_{10}", COR, q10), ("(x − 3)", ENT)]
    w, xs, ws = fx(c, partes, W / 2, 0, S, 0, "center")
    fx_em(c, t, C["s11.a"], partes, W / 2, 260, S, "center")
    nota(c, t, C["s11.b"] + 0.2, "base 10 escondida", xs[1] - 60, 400, 44, fundo=TINTA)
    caixa(c, xs[2], 260, ws[2] - S * 0.06, S, ep(t, C["s11.c"], 0.4))
    nota(c, t, C["s11.c"] + 0.3, "precisa ser > 0", xs[2] + ws[2] / 2 + 80, 400, 44)
    XI = 640
    eqn_em(c, t, C["s11.d"], [("x − 3", ENT)], [("0", SAI)], 580, 110, XI, ">")
    eqn_em(c, t, C["s11.e"], [("x", ENT)], [("3", SAI)], 740, 110, XI, ">")
    vx = reta_sol(c, t, C["s11.f"] - 0.4, 300, 1500, 900, -1, 8)
    pinta(c, t, C["s11.f"], C["s11.f"] + 0.3, vx, 900, 3, 1, False, 260, 1560)
    E.foco(c, t, C["s11.f"] + 0.5, 0.5, lambda a: fx(c, [("]3, +∞[", COR)], 1100, 740, 110, a))
    nota(c, t, C["s11.f"] + 2.2, "x = 3: log 0 não existe", 1400, 580, 44, fundo=ERRADO)


# ---------------- inequação ----------------
P4 = (1100, 200, 690, 700, -1, 10, -4, 5)


def b_inequacao(c, t, C, b):
    P = E.plano(c, t, C["s12"], *P4, marcas_x=[2, 4, 6, 8], marcas_y=[-3, -2, -1, 1, 2, 3, 4], size=36)
    E.curva(c, t, C["s12"] + 0.3, P, math.log2, 0.05, 10, d=1.0, cor=COR)
    E.foco(c, t, C["s12"] + 1.0, 0.4, lambda a: rot_log(c, P, 5.0, 3.9, a=a))
    S, XI = 96, 520
    eqn_em(c, t, C["s12.a"], [("log_2 ", SAI), ("x", ENT)], [("3", SAI)], 260, S, XI, ">")
    E.saida(c, t, C["s13"] - 0.1, lambda: nota_fx(c, t, C["s12.b"], [("3 = log_2 8", BR)], XI + 380, 230, 40))
    l2 = eqn(c, [("log_2 ", SAI), ("x", ENT)], [("log_2 ", SAI), ("8", SAI)], 430, S, 0, XI, ">")
    eqn_em(c, t, C["s12.c"], [("log_2 ", SAI), ("x", ENT)], [("log_2 ", SAI), ("8", SAI)], 430, S, XI, ">")
    q = ep(t, C["s12.c"] + 0.8, 0.4)
    caixa(c, l2[0][0][0], 430, l2[0][1][0] - S * 0.2, S, q)
    caixa(c, l2[1][0][0], 430, l2[1][1][0] - S * 0.2, S, q)
    if t >= C["s13"]:
        E.saida(c, t, C["s14"] - 0.1, lambda: nota(c, t, C["s13.a"], "logaritmando maior", XI + 20, 520, 40, fundo=TINTA))
    eqn_em(c, t, C["s13.b"], [("x", ENT)], [("8", SAI)], 640, S, XI, ">")
    nota(c, t, C["s13.b"] + 0.6, "o sinal se mantém", XI + 360, 610, 36, fundo=CERTO)

    def solucao():
        vx = reta_sol(c, t, C["s13.b"] + 0.2, 220, 920, 820, 0, 10, 38)
        pinta(c, t, C["s13.b"] + 0.6, C["s13.b"] + 0.9, vx, 820, 8, 1, False, 180, 980)
    E.saida(c, t, C["s14"] - 0.1, solucao)
    # no gráfico: a linha y = 3 e a curva acima dela depois do 8
    q = ep(t, C["s13.c"], 0.6)
    if q > 0:
        M.line(c, P.x(-1), P.y(3), P.x(10), P.y(3), SAI, 0.8, 4, dash=E.TRACO, progress=q)
        E.foco(c, t, C["s13.c"] + 0.3, 0.3, lambda a: E.escreve(c, "y = 3", P.x(2.2), P.y(3) - 16, 40, "b", SAI, a))
    E.area(c, t, C["s13.d"], P, math.log2, 8, 10, g=lambda x: 3, alfa=0.3)
    if t >= C["s13.d"]:
        M.line(c, P.x(8), P.y(3), P.x(8), P.oy, ENT, 0.9, 5, dash=E.TRACO, progress=ease_io(prog(t, C["s13.d"], 0.5)))
        anel(c, t, C["s13.d"], *P(8, 3))
    if t >= C["s14"]:
        nota(c, t, C["s14.a"], "base entre 0 e 1: o sinal vira", 540, 800, 44, fundo=TINTA)
        nota(c, t, C["s14.b"], "confira: logaritmando > 0", 540, 930, 44)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15.a"], [("cuidado:", "g", 90, ERRADO), ("esquecer", "i", 90), ("o", "i", 90), ("domínio", "g", 90)], W / 2, 190, "center")
    XI = 660
    eqn_em(c, t, C["s15.b"], [("log_2 ", SAI), ("x", ENT)], [("3", SAI)], 400, 110, XI, "<")
    certo = C["s16.c"]
    E.saida(c, t, certo - 0.1, lambda: (eqn_em(c, t, C["s15.c"], [("x", ENT)], [("8", SAI)], 570, 110, XI, "<"),
                                        E.frase(c, t, C["s15.c"] + 0.7, ps("e para aí", "i", 60, ERRADO), XI + 300, 560)))
    E.foco(c, t, certo, 0.5, lambda a: fx(c, [("0 < x < 8", CERTO)], XI - 230, 570, 110, a))
    vx = reta_sol(c, t, C["s15.c"] + 0.4, 300, 1620, 790, -2, 10)
    E.saida(c, t, certo - 0.1, lambda: pinta(c, t, C["s15.c"] + 0.8, C["s15.c"] + 1.1, vx, 790, 8, -1, False, 250, 1680, ERRADO))
    if t >= C["s16.a"]:
        for i, v in enumerate((0, -1)):
            E.saida(c, t, certo - 0.1, lambda v=v, i=i: (
                E.foco(c, t, C["s16.a"] + 0.4 * i, 0.3, lambda a: c.drawCircle(vx(v), 790, 22, M.paint(ERRADO, a))),
                anel(c, t, C["s16.a"] + 0.4 * i, vx(v), 790, ERRADO)))
    E.saida(c, t, certo - 0.1, lambda: (fx_em(c, t, C["s16.a"] + 2.0, [("2", SAI), ("^?", ENT), (" = −1", SAI)], 1220, 400, 90),
                                        E.frase(c, t, C["s16.b"], [("nenhum", "g", 64, ERRADO), ("expoente", "g", 64, ERRADO)], 1220, 520)))
    E.intervalo(c, t, certo + 0.4, vx, 790, 0, 8, cor=CERTO)
    if t >= C["s16.d"]:
        anel(c, t, C["s16.d"], vx(0), 790, CERTO)
        anel(c, t, C["s16.d"], vx(8), 790, CERTO)
    E.foco(c, t, C["s16.d"], 0.5, lambda a: (E.escreve(c, "aberto no 0 e no 8:", 520, 990, 60, "i", TINTA, a),
                                             fx(c, [("]0, 8[", CERTO)], 1080, 995, 96, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s17():
        E.frase(c, t, C["s17.a"], [("a", "i", 96, CLARO), ("base", "g", 100, BR), ("sobe", "g", 100, BR)], W / 2, 230, "center")
        E.frase(c, t, C["s17.a"] + 0.9, [("e", "i", 96, CLARO), ("vira", "i", 96, CLARO), ("potência", "g", 100, BR)], W / 2, 350, "center")
        S, Y = 160, 640
        ini = [("log", BR), ("_2", CLARO), (" x", BR), (" > ", BR), ("3", CLARO)]
        fim = [("x", BR), (" > ", BR), ("2", CLARO), ("^3", CLARO)]
        _, xs0, _ = fx(c, ini, W / 2, Y, S, 0, "center")
        _, xs1, _ = fx(c, fim, W / 2, Y, S, 0, "center")
        sp = E.larg(" ", "g", S)
        tb = C["s17.b"]
        p = ease_io(prog(t, tb, 1.1))
        if p <= 0:
            fx_em(c, t, C["s17.a"] + 1.8, ini, W / 2, Y, S, "center")
        elif p < 1:
            E.escreve(c, "log", xs0[0], Y, S, "g", BR, 1 - min(1, p * 2.5))
            moves = (("2", (xs0[1] + S * 0.02, Y + S * 0.2, S * 0.56), (xs1[2], Y, S), CLARO),
                     ("x", (xs0[2] + sp, Y, S), (xs1[0], Y, S), BR),
                     (">", (xs0[3] + sp, Y, S), (xs1[1] + sp, Y, S), BR),
                     ("3", (xs0[4], Y, S), (xs1[3] + S * 0.02, Y - S * 0.42, S * 0.58), CLARO))
            for s, a0, a1, cor in moves:
                E.escreve(c, s, lerp(a0[0], a1[0], p), lerp(a0[1], a1[1], p), lerp(a0[2], a1[2], p), "g", cor, 1.0)
        else:
            fx(c, fim, W / 2, Y, S, 1.0, "center")
        if t >= tb:
            q = pulso(t, tb + 1.1, 1.8)
            if q > 0:
                c.drawCircle(xs1[2] + 60, Y - 60, 130, M.paint(CLARO, q, stroke=6))
        E.foco(c, t, C["s17.c"], 0.5, lambda a: (fx(c, [("x > 8", CLARO)], W / 2, 900, 150, a, "center")))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"] + 0.2, [("o", "i", 90, CLARO), ("log", "g", 96, BR), ("é", "i", 90, CLARO), ("um", "i", 90, CLARO),
                                   ("expoente", "g", 96, BR)], W / 2, 220, "center")
    E.foco(c, t, C["s18.a"] + 1.0, 0.5, lambda a: fx(c, [("2", BR), ("^{mais que 3}", CLARO), (" = x", BR)], W / 2, 450, 140, a, "center"))
    E.foco(c, t, C["s18.b"], 0.5, lambda a: fx(c, [("x > 2", BR), ("^3", CLARO)], W / 2, 640, 130, a, "center"))
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.pilula(c, "base entre 0 e 1: vire o sinal", W / 2, 800, 50, "g", fundo=CLARO, cor="#07070F", a=a))
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.pilula(c, "junte o domínio no fim", W / 2, 935, 50, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 220)
    S = 130
    partes = [("log_2", SAI), ("(x − 1)", ENT), (" < 3", SAI)]
    w, xs, ws = fx(c, partes, XE, 0, S, 0)
    fx_em(c, t, C["s19.a"], partes, XE, 480, S)
    caixa(c, xs[1], 480, ws[1] - S * 0.06, S, ep(t, C["s19.a"] + 2.0, 0.4))
    E.frase(c, t, C["s19.a"] + 2.2, ps("tudo dentro do log", "i", 56, TINTA2), xs[1], 600)
    E.frase(c, t, C["s19.b"], [("resposta", "i", 80), ("em", "i", 80), ("intervalo:", "g", 80, COR)], XE, 790)
    E.foco(c, t, C["s19.b"] + 0.8, 0.5, lambda a: fx(c, [("] ?, ? [", COR)], XE + 200, 930, 100, a))
    if t >= C["s20"]:
        E.relogio(c, t, C["s20.a"], cx=1540, cy=640, r=150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    S = 90

    def item(k, n, y):
        E.foco(c, t, C[k], 0.5, lambda a: (E.bola(c, 230, y - 30, 46, a=a),
                                           E.escreve(c, n, 230 - E.larg(n, "g", 54) / 2, y - 10, 54, "g", BR, a)))
    item("s21.a", "1", 260)
    E.foco(c, t, C["s21.a"], 0.5, lambda a: E.escreve(c, "domínio", 310, 230, 44, "i", TINTA2, a))
    fx_em(c, t, C["s21.a"] + 0.2, [("x − 1 > 0", SAI)], 310, 310, S)
    fx_em(c, t, C["s21.a"] + 1.4, [("→  x > 1", COR)], 820, 310, S)
    item("s21.b", "2", 480)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.escreve(c, "a base sobe", 310, 450, 44, "i", TINTA2, a))
    fx_em(c, t, C["s21.b"] + 0.2, [("x − 1 < 2", SAI), ("^3", COR), (" = 8", SAI)], 310, 530, S)
    fx_em(c, t, C["s21.c"], [("→  x < 9", COR)], 1000, 530, S)
    nota(c, t, C["s21.c"] + 0.5, "base 2: o sinal fica", 1210, 600, 36, fundo=TINTA)
    Y = 810
    vx = reta_sol(c, t, C["s22.a"] - 0.3, 300, 1620, Y, 0, 10)
    q = ep(t, C["s22.a"] + 0.2, 0.5) * (1 - ep(t, C["s22.b"], 0.4))
    if q > 0:  # as duas condições: à direita do 1 e à esquerda do 9
        M.line(c, vx(1), Y - 40, W - 120, Y - 40, TINTA2, q, 6)
        M.line(c, 180, Y - 70, vx(9), Y - 70, TINTA2, q, 6)
        bolinha(c, vx(1), Y - 40, TINTA2, q, 12)
        bolinha(c, vx(9), Y - 70, TINTA2, q, 12)
    E.intervalo(c, t, C["s22.b"], vx, Y, 1, 9)
    E.foco(c, t, C["s22.a"], 0.5, lambda a: (E.escreve(c, "juntando:", 310, 680, 54, "i", TINTA2, a),
                                             fx(c, [("1 < x < 9", COR)], 560, 685, S, a)))
    E.foco(c, t, C["s22.b"] + 0.4, 0.5, lambda a: (E.bola(c, 1640, 640, 110, CERTO, a), fx(c, [("]1, 9[", BR)], 1640, 665, 72, a, "center")))
    E.foco(c, t, C["s22.c"], 0.5, lambda a: (E.escreve(c, "teste:", 310, 990, 60, "i", TINTA, a),
                                             fx(c, [("5 − 1 = 4", SAI)], 500, 990, 70, a)))
    E.foco(c, t, C["s22.c"] + 1.6, 0.5, lambda a: fx(c, [("log_2 4 = 2 < 3", CERTO)], 960, 990, 70, a))
    E.foco(c, t, C["s22.c"] + 2.6, 0.4, lambda a: E.selo(c, 1620, 970, 46, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s23.a", [("espelho", "g", 84), ("de", "i", 80), ("2ˣ", "g", 84), ("na", "i", 80), ("diagonal", "g", 84, COR)]),
                 ("s23.b", [("logaritmando", "g", 84), ("positivo", "g", 84, COR)]),
                 ("s23.c", [("base > 1", "g", 84, COR), ("mantém;", "i", 80), ("0 < base < 1", "g", 84), ("vira", "i", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s24"] + 1.0, [("escalas", "g", 120, COR)], XE, 410)
    E.frase(c, t, C["s24"] + 1.3, [("logarítmicas", "g", 120, COR)], XE, 540)
    E.frase(c, t, C["s24.a"], [("pH,", "g", 64), ("terremoto", "i", 66), ("e", "i", 66), ("decibéis", "i", 66)], XE, 680)
    E.foco(c, t, C["s24.b"], 0.5, lambda a: (E.escreve(c, "pH 3:", XE, 810, 70, "g", TINTA, a),
                                             E.escreve(c, "100 vezes", XE + 210, 810, 70, "g", COR, a),
                                             E.escreve(c, "mais ácido que pH 5", XE + 560, 810, 62, "i", TINTA, a)))
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, tabela=b_tabela, espelho=b_espelho, dominio=b_dominio, inequacao=b_inequacao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
