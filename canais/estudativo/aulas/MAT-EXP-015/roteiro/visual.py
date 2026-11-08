"""Visual — Estudativo · MAT-EXP-015: praticando logaritmos (fim da trilha Exponencial e Logaritmo).

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001; peças de MAT-EXP-013 e 014): expoente e entrada em
índigo (ENT), base e saída em preto (SAI); fx() pinta cada pedaço da fórmula e escreve log₂ com índice; letras com índice em
Unicode (N₀, A₀). Aula de prática no modelo de MAT-EQU-017: pílula "situação n", relógio de pausa, resposta na esfera verde.
Nesta aula: o cartão fixo "log 2 ≈ 0,30 · log 3 ≈ 0,48" no canto das situações que usam esses valores; colunas da cultura
hora a hora com a linha do dobro; a reta com x > 3 e o −5 riscado; dois sismogramas, um com o dobro da altura do outro.
No fim, a prévia de Progressões: caixas com o valor dentro e a posição embaixo."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / entrada · base / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-015_praticando_logaritmos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "atalho", "fim"))
BR = "#FFFFFF"

L2, L3 = 0.30, 0.48
assert abs(math.log10(2) - L2) < 0.01 and abs(math.log10(3) - L3) < 0.01
assert round(L2 - 4, 2) == -3.70 and 3 < -math.log10(2e-4) < 4
assert round(2 * L2 + L3, 2) == 1.08 and round(2 * L2 + L3 - 1, 2) == 0.08 and round(L2 / 0.08, 2) == 3.75 and 0.75 * 60 == 45
assert (5 + 3) * (5 - 3) == 16 == 2 ** 4 and 5 ** 2 - 9 == 16 and math.log2(8) + math.log2(2) == 4
assert round(5.3 - 5.0, 1) == 0.3 and abs(10 ** 0.3 - 2) < 0.01 and 10 * L2 == 3


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



# ---------------- peças desta aula ----------------
def onda(c, x, y, w, amp, a=1.0, p=1.0, cor=None, ciclos=9, largura=5):
    """sismograma: tremor de amplitude `amp` px no meio do registro, desenhado até a fração p"""
    if a <= 0 or p <= 0:
        return
    path = skia.Path()
    n = 400
    for i in range(int(n * p) + 1):
        u = i / n
        env = math.exp(-((u - 0.45) / 0.16) ** 2)
        yy = y - amp * env * math.sin(u * ciclos * 2 * math.pi)
        path.moveTo(x + u * w, yy) if i == 0 else path.lineTo(x + u * w, yy)
    c.drawPath(path, M.paint(cor or COR, a, stroke=largura, cap_round=True))


def situacao(c, t, t0, n, y=170):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, f"situação {n}", XE + 150, y - 22, 54, "g", a=a, cor=E.SOBRE))


def cartao_logs(c, t, t0, x=1440, y=110):
    """os dois valores fixos da aula, no canto: log 2 ≈ 0,30 e log 3 ≈ 0,48"""
    def d(a):
        M.rrect(c, x, y, 400, 170, 22, "#FFFFFF", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 400, 170), 22, 22), M.paint(COR, a, stroke=4))
        fx(c, [("log 2 ≈ 0,30", COR)], x + 200, y + 70, 54, a, "center")
        fx(c, [("log 3 ≈ 0,48", TINTA)], x + 200, y + 140, 54, a, "center")
    E.foco(c, t, t0, 0.5, d, sobe=6)


def bola_res(c, t, t0, txt, cx, cy, r, size, sub=None, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor or CERTO, a), fx(c, [(txt, BR)], cx, cy + size * 0.36 - (24 if sub else 0), size, a, "center"),
                                     sub and centro(c, sub, cx, cy + size * 0.36 + 50, 48, "i", BR, a)))


def operacao(c, t, t0, txt, x, y, size=44, fundo=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, x, y, size, "g", fundo=fundo or TINTA, a=a), sobe=6)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb = C["s01.a"], C["s01.b"]
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "4", XE - 8, 560, 380, "g", COR, a))
    E.frase(c, t, ka + 0.5, ps("situações", "i", 120), XE + 250, 520)
    E.frase(c, t, ka + 1.3, ps("de ciências, criadas", "i", 60, TINTA2), XE, 680, passo=0.08)
    E.frase(c, t, ka + 2.0, ps("para esta aula", "i", 60, TINTA2), XE, 760, passo=0.08)
    x = 1080
    E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "pause e resolva", x + 260, 380, 70, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, kb + 0.6, ps("antes de ver a resposta", "i", 60), x + 260, 500, "center", 0.08)
    E.frase(c, t, kb + 3.0, [("errar", "g", 66, COR), ("aqui", "i", 62), ("ensina", "i", 62)], x + 260, 680, "center", 0.1)
    nomes = ("pH", "bactérias", "equação", "terremoto")
    ws = [E.larg(s, "i", 40) + 44 for s in nomes]
    xx = x + 260 - (sum(ws) + 24 * 3) / 2
    for i, s in enumerate(nomes):
        cx = xx + ws[i] / 2
        E.foco(c, t, kb + 4.0 + 0.3 * i, 0.4, lambda a, s=s, cx=cx: E.pilula(c, s, cx, 840, 40, "i", a=a, contorno=True, cor=COR))
        xx += ws[i] + 24


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s02.a"] - 0.6, 0.5, lambda a: E.escreve(c, "4", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s02.a"] - 0.45, 0.5, lambda a: E.escreve(c, "ferramentas", XE + 215, 700, 100, "i", TINTA, a))
    x, w = 840, 960
    itens = (("s02.a", [("log(a · b) = log a + log b", COR)], [("log a", TINTA), ("^n", TINTA), (" = n · log a", TINTA)]),
             ("s02.b", [("log 2 ≈ 0,30", COR)], [("log 3 ≈ 0,48", TINTA)]),
             ("s02.c", [("logaritmando > 0", COR)], None),
             ("s02.d", [("diferença na escala", COR)], [("→ expoente do 10", TINTA)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 200
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 170, p, prog_=p)
        if l2 and k == "s02.b":
            fx_em(c, t, C[k] + 0.1, l1, x + 40, y + 108, 58)
            fx_em(c, t, C[k] + 0.4, l2, x + 480, y + 108, 58)
        elif l2:
            fx_em(c, t, C[k] + 0.1, l1, x + 40, y + 74, 52)
            fx_em(c, t, C[k] + 0.4, l2, x + 40, y + 144, 52)
        else:
            fx_em(c, t, C[k] + 0.1, l1, x + 40, y + 108, 58)
    ys = [150 + i * 200 + 150 for i in range(4)]
    py = ys[0]
    for i in range(1, 4):
        py = lerp(py, ys[i], ease_io(prog(t, C[itens[i][0]] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s02.a"], 0.4))
    E.frase(c, t, C["s02.end"] - 2.6, ps("se alguma travar,", "i", 56, COR) + ps("procure a aula no canal", "i", 56), XE, 980, "left", 0.1)


# ---------------- situação 1: pH ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1)
    fx_em(c, t, C["s03.b"], [("pH = −log ", SAI), ("[H⁺]", ENT)], XE, 390, 110)
    fx_em(c, t, C["s03.c"], [("[H⁺] = 2 · 10", ENT), ("^{−4}", ENT)], XE, 600, 110)
    E.frase(c, t, C["s03.d"], [("qual", "i", 90), ("é", "i", 90), ("o", "i", 90), ("pH?", "g", 96, COR)], XE, 830)
    cartao_logs(c, t, C["s03.d"] + 1.5)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], 1560, 640, 150)


def b_resposta1(c, t, C, b):
    def s05():
        S = 96
        lin = [("log(2 · 10", SAI), ("^{−4}", SAI), (") = ", SAI), ("log 2", COR), (" + ", SAI), ("log 10", TINTA), ("^{−4}", TINTA)]
        w, xs, ws = fx(c, lin, XE, 0, S, 0)
        fx_em(c, t, C["s05.a"], lin, XE, 230, S)
        xlog2 = xs[3] + ws[3] / 2
        xlog10 = xs[5] + (ws[5] + ws[6]) / 2
        E.foco(c, t, C["s05.b"], 0.4, lambda a: (M.arrow(c, xlog2, 270, xlog2, 340, COR, a, 4, 16), centro(c, "0,30", xlog2, 420, 80, "g", COR, a)))
        E.foco(c, t, C["s05.c"], 0.4, lambda a: (M.arrow(c, xlog10, 270, xlog10, 340, TINTA, a, 4, 16), centro(c, "−4", xlog10, 420, 80, "g", TINTA, a)))
        fx_em(c, t, C["s05.d"], [("0,30 − 4 = ", SAI), ("−3,70", COR)], XE, 610, S)
        fx_em(c, t, C["s05.e"], [("pH = −(−3,70) = ", SAI), ("3,7", COR)], XE, 800, S)
        bola_res(c, t, C["s05.e"] + 0.8, "pH 3,7", 1580, 700, 150, 72)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"] + 0.2, [("faz", "i", 80), ("sentido?", "g", 84, COR)], W / 2, 200, "center")
    fx_em(c, t, C["s06.a"], [("10", TINTA), ("^{−4}", TINTA), ("  <  ", TINTA), ("2 · 10", COR), ("^{−4}", COR), ("  <  10", TINTA), ("^{−3}", TINTA)], W / 2, 400, 96, "center")
    y = 760
    vx = E.reta(c, t, C["s06.a"] + 0.6, 360, 1560, y, 2, 5, [2, 3, 4, 5], lambda v: f"pH {v}", size=50)
    q = ep(t, C["s06.b"], 0.6)
    if q > 0:
        M.line(c, vx(3), y, lerp(vx(3), vx(4), q), y, CERTO, 1.0, 14, cap_round=False)
    if t >= C["s06.b"]:
        bolinha(c, vx(3), y, CERTO, ep(t, C["s06.b"], 0.3))
        bolinha(c, vx(4), y, CERTO, ep(t, C["s06.b"], 0.3))
    E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: (c.drawCircle(vx(3.7), y, 20, M.paint(COR, a)), centro(c, "3,7", vx(3.7), y - 50, 60, "g", COR, a)))
    E.foco(c, t, C["s06.b"] + 1.2, 0.4, lambda a: E.selo(c, 1700, y - 20, 50, True, a))


# ---------------- situação 2: bactérias ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C["s07.a"], 2)
    E.frase(c, t, C["s07.b"], [("+20%", "g", 90, COR), ("por", "i", 80), ("hora", "i", 80)], XE, 350)
    fx_em(c, t, C["s07.c"], [("N = N₀ · 1,2", SAI), ("^t", ENT)], XE, 540, 104)
    E.foco(c, t, C["s07.c"] + 1.2, 0.4, lambda a: E.escreve(c, "t em horas", XE, 630, 50, "i", TINTA2, a))
    E.frase(c, t, C["s07.d"], [("dobra", "g", 90, COR), ("em", "i", 84), ("quanto", "i", 84), ("tempo?", "i", 84)], XE, 830)
    cartao_logs(c, t, C["s07.d"] + 2.5)
    if t < C["s08"]:
        # a cultura, hora a hora: 1,2 elevado a 0, 1, 2, 3, 4
        dados = [(str(k), round(1.2 ** k, 2)) for k in range(5)]
        x0, y0, w0, h0 = 1000, 380, 800, 520
        E.colunas(c, t, C["s07.b"] + 0.4, dados, x0, y0, w0, h0, vmax=2.4, passo=0.25, size=38)
        q = ep(t, C["s07.d"] + 0.4, 0.5)
        if q > 0:
            yy = y0 + h0 - 2 / 2.4 * h0
            M.line(c, x0 - 20, yy, x0 + w0, yy, ERRADO, q, 4, dash=E.TRACO)
            E.escreve(c, "o dobro", x0 - 10, yy - 14, 40, "b", ERRADO, q)
        E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.escreve(c, "horas", x0 + w0 - 110, y0 + h0 + 110, 40, "i", TINTA2, a))
    else:
        E.relogio(c, t, C["s08.a"], 1560, 560, 150)


def b_resposta2(c, t, C, b):
    S = 96
    cartao_logs(c, t, C["s09"] - 1)

    def s09():
        fx_em(c, t, C["s09.a"], [("1,2", SAI), ("^t", ENT), (" = 2", SAI)], XE, 300, S)
        operacao(c, t, lerp(C["s09.a"], C["s09.b"], 0.55), "log dos dois lados", 760, 420)
        fx_em(c, t, C["s09.b"], [("t", ENT), (" · log 1,2 = log 2", SAI)], XE, 600, S)
        E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.escreve(c, "o expoente desce", XE, 690, 50, "i", TINTA2, a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t:
        def s10():
            fx_em(c, t, C["s10.a"], [("1,2 = ", SAI), ("f{12}{10}", COR)], XE, 300, S)
            fx_em(c, t, C["s10.b"], [("12 = 2 · 2 · 3", SAI)], 760, 300, S)
            fx_em(c, t, C["s10.c"], [("log 12 = 0,30 + 0,30 + 0,48 = ", SAI), ("1,08", COR)], XE, 520, 84)
            fx_em(c, t, C["s10.d"], [("log 1,2 = 1,08 − 1 = ", SAI), ("0,08", COR)], XE, 720, 84)
            E.foco(c, t, C["s10.d"] + 0.6, 0.4, lambda a: E.escreve(c, "log 10 = 1", XE + 1000, 720, 50, "i", TINTA2, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    fx_em(c, t, C["s11.a"], [("t", ENT), (" = f{0,30}{0,08}", SAI)], XE, 300, 110)
    operacao(c, t, C["s11.b"] - 0.3, "× 100 em cima e embaixo", 1000, 280)
    fx_em(c, t, C["s11.b"], [("= f{30}{8} = ", SAI), ("3,75 h", COR)], XE + 150, 560, 110)
    fx_em(c, t, lerp(C["s11.b"], C["s11.c"], 0.4), [("0,75 · 60 = 45 min", SAI)], XE, 820, 90)
    E.foco(c, t, lerp(C["s11.b"], C["s11.c"], 0.4) + 0.5, 0.4, lambda a: E.escreve(c, "três quartos de hora", XE, 910, 50, "i", TINTA2, a))
    bola_res(c, t, C["s11.c"], "3 h 45 min", 1540, 700, 190, 64, "cerca de")


# ---------------- situação 3: equação ----------------
EQ3 = [("log_2", SAI), ("(x + 3)", ENT), (" + ", SAI), ("log_2", SAI), ("(x − 3)", ENT), (" = 4", SAI)]


def b_questao3(c, t, C, b):
    situacao(c, t, C["s12.a"], 3)
    S = 110
    w, xs, ws = fx(c, EQ3, W / 2, 0, S, 0, "center")
    fx_em(c, t, C["s12.b"], EQ3, W / 2, 470, S, "center")
    q = ep(t, lerp(C["s12.b"], C["s12.c"], 0.6), 0.4)
    caixa(c, xs[1], 470, ws[1] - S * 0.06, S, q)
    caixa(c, xs[4], 470, ws[4] - S * 0.06, S, q)
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "atenção às condições", W / 2, 700, 56, "g", fundo=ERRADO, a=a), sobe=6)
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], W / 2, 860, 100)


def b_resposta3(c, t, C, b):
    S = 90
    XI = 640

    def s14():
        E.foco(c, t, C["s14.a"] - 0.4, 0.4, lambda a: E.escreve(c, "condições", XE, 180, 50, "i", TINTA2, a))
        fx_em(c, t, C["s14.a"], [("x + 3 > 0  e  x − 3 > 0", SAI)], XE, 280, S)
        fx_em(c, t, C["s14.b"], [("→  x > 3", COR)], 1240, 280, S)
        fx_em(c, t, C["s14.c"], [("log_2", SAI), ("[(x + 3)(x − 3)]", ENT), (" = 4", SAI)], XE, 520, S)
        E.foco(c, t, C["s14.c"] + 0.3, 0.4, lambda a: E.escreve(c, "soma de logs = log do produto", XE, 615, 46, "i", TINTA2, a))
        fx_em(c, t, C["s14.d"], [("(x + 3)(x − 3) = 2", SAI), ("^4", COR), (" = 16", SAI)], XE, 760, S)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if C["s15"] <= t < C["s16"]:
        nota(c, t, C["s15"], "condição: x > 3", 1600, 170, 44)
        eqn_em(c, t, C["s15.a"], [("x² − 9", ENT)], [("16", SAI)], 260, S, XI)
        eqn_em(c, t, C["s15.b"], [("x²", ENT)], [("25", SAI)], 410, S, XI)
        fx_em(c, t, C["s15.c"], [("x = 5  ou  x = −5", SAI)], XI - 300, 560, S)
        w, xs, ws = fx(c, [("x = 5  ou  ", SAI), ("x = −5", SAI)], XI - 300, 0, S, 0)
        if t >= C["s15.d"]:
            E.risco(c, xs[1] - 10, 580, xs[1] + ws[1] + 10, 510, t, C["s15.d"], largura=12)
        y = 800
        vx = E.reta(c, t, C["s15.c"] + 0.6, 300, 1620, y, -6, 6, list(range(-6, 7)), E._num, size=40)
        pinta(c, t, C["s15.c"] + 0.8, C["s15.c"] + 1.0, vx, y, 3, 1, False, 260, 1680)
        E.foco(c, t, C["s15.d"], 0.4, lambda a: (c.drawCircle(vx(-5), y, 22, M.paint(ERRADO, a)),
                                                centro(c, "×", vx(-5), y - 40, 60, "g", ERRADO, a)))
        E.foco(c, t, C["s15.d"] + 1.2, 0.4, lambda a: E.pilula(c, "log₂(−2) não existe", vx(-5) + 120, y - 120, 40, "g", fundo=ERRADO, a=a), sobe=6)
        E.foco(c, t, C["s15.e"], 0.4, lambda a: c.drawCircle(vx(5), y, 22, M.paint(CERTO, a)))
        bola_res(c, t, C["s15.e"], "x = 5", 1560, 420, 150, 80)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"], [("conferindo", "i", 80, COR), ("x = 5", "g", 84)], XE, 200)
    fx_em(c, t, C["s16.a"], [("5 + 3 = 8   →   log_2 8 = ", SAI), ("3", COR)], XE, 420, S)
    fx_em(c, t, C["s16.b"], [("5 − 3 = 2   →   log_2 2 = ", SAI), ("1", COR)], XE, 610, S)
    fx_em(c, t, C["s16.c"], [("3 + 1 = 4", CERTO)], XE, 820, 110)
    E.foco(c, t, C["s16.c"] + 1.2, 0.4, lambda a: E.selo(c, XE + 620, 790, 50, True, a))


# ---------------- situação 4: terremoto ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C["s17.a"], 4)
    fx_em(c, t, C["s17.b"], [("M = log ", SAI), ("f{A}{A₀}", ENT)], XE, 420, 110)
    E.foco(c, t, C["s17.b"] + 3.0, 0.4, lambda a: E.pilula(c, "A = amplitude do tremor", 960, 400, 40, "g", a=a), sobe=6)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: (E.escreve(c, "tremor 1:", XE, 640, 66, "i", TINTA, a), E.escreve(c, "5,3", XE + 320, 640, 90, "g", COR, a)))
    E.foco(c, t, C["s17.d"], 0.5, lambda a: (E.escreve(c, "tremor 2:", XE, 760, 66, "i", TINTA, a), E.escreve(c, "5,0", XE + 320, 760, 90, "g", TINTA, a)))
    E.frase(c, t, C["s17.e"], [("quantas", "i", 80), ("vezes", "i", 80), ("maior?", "g", 84, COR)], XE, 920)
    cartao_logs(c, t, C["s17.e"] + 1.0)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], 1560, 640, 150)


def b_resposta4(c, t, C, b):
    cartao_logs(c, t, C["s19"] - 1)
    fx_em(c, t, C["s19.a"], [("5,3 − 5,0 = ", SAI), ("0,3", COR)], XE, 230, 96)
    fx_em(c, t, C["s19.b"], [("f{A₁}{A₂} = 10", SAI), ("^{0,3}", COR)], XE, 450, 96)
    E.foco(c, t, C["s19.c"] - 1.6, 0.4, lambda a: E.escreve(c, "log de quem dá 0,30?", 760, 395, 50, "i", TINTA2, a))
    fx_em(c, t, C["s19.c"], [("10", SAI), ("^{0,3}", COR), (" ≈ ", SAI), ("2", COR)], 760, 530, 96)
    bola_res(c, t, C["s19.d"], "≈ 2 vezes", 1580, 440, 130, 54)
    for k, y, amp, rot in ((C["s19.d"], 720, 38, "5,0"), (C["s19.d"] + 0.4, 912, 76, "5,3")):
        a = ep(t, k, 0.4)
        if a > 0:
            M.rrect(c, XE, y - 88, 1380, 176, 20, "#FFFFFF", a)
            M.line(c, XE + 40, y, XE + 1300, y, FIO, a, 3)
            onda(c, XE + 40, y, 1260, amp, a, prog(t, k + 0.1, 1.2), TINTA if amp < 60 else COR)
            E.foco(c, t, k, 0.4, lambda q, y=y, rot=rot: E.escreve(c, rot, XE + 1420, y + 20, 60, "g", TINTA, q))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s20():
        E.frase(c, t, C["s20"] + 0.2, [("o", "i", 90, CLARO), ("atalho", "g", 96, BR), ("na", "i", 90, CLARO), ("base", "i", 90, CLARO),
                                       ("10", "g", 96, BR)], W / 2, 210, "center")
        E.foco(c, t, C["s20.a"], 0.5, lambda a: (fx(c, [("+0,30", CLARO)], 640, 440, 130, a, "right"),
                                                 E.escreve(c, "→", 760, 430, 110, "g", BR, a), E.escreve(c, "dobrar", 920, 440, 120, "g", BR, a)))
        E.foco(c, t, C["s20.b"], 0.5, lambda a: (fx(c, [("+0,48", CLARO)], 640, 640, 130, a, "right"),
                                                 E.escreve(c, "→", 760, 630, 110, "g", BR, a), E.escreve(c, "triplicar", 920, 640, 120, "g", BR, a)))
        E.foco(c, t, C["s20.c"], 0.5, lambda a: (E.escreve(c, "em dB:", 300, 870, 70, "i", CLARO, a),
                                                 fx(c, [("10 · 0,30 = 3", BR), ("  →  dobrar = +3 dB", CLARO)], 560, 870, 80, a)))
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.foco(c, t, C["s21.a"], 0.5, lambda a: fx(c, [("log 2 ≈ 0,30", BR)], W / 2, 330, 110, a, "center"))
    E.foco(c, t, C["s21.a"] + 1.6, 0.5, lambda a: fx(c, [("10", BR), ("^{0,30}", CLARO), (" ≈ 2", BR)], W / 2, 520, 110, a, "center"))
    E.foco(c, t, C["s21.b"], 0.4, lambda a: E.pilula(c, "outros valores ou mais precisão?", W / 2, 720, 50, "g", fundo=CLARO, cor="#07070F", a=a))
    E.foco(c, t, C["s21.c"], 0.4, lambda a: E.pilula(c, "use os números da questão", W / 2, 870, 54, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- fechamento ----------------
def caixas_previa(c, t, t0, x0, y0, valores, s=120, gap=26):
    """prévia de Progressões: valor dentro da caixa, posição embaixo"""
    for i, v in enumerate(valores):
        x = x0 + i * (s + gap)
        E.foco(c, t, t0 + 0.15 * i, 0.4, lambda a, x=x, v=v, i=i: (
            M.rrect(c, x, y0, s, s, 18, "#FFFFFF", a), c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y0, s, s), 18, 18), M.paint(COR, a, stroke=5)),
            centro(c, v, x + s / 2, y0 + s / 2 + 24, 64, "g", TINTA, a), centro(c, str(i + 1), x + s / 2, y0 + s + 56, 44, "b", COR, a)), sobe=6)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s22.a", [("desmonte", "g", 84), ("em", "i", 80), ("2,", "g", 84, COR), ("3", "g", 84, COR), ("e", "i", 80), ("10", "g", 84, COR)]),
                 ("s22.b", [("confira", "g", 84), ("as", "i", 80), ("condições", "g", 84, COR)]),
                 ("s22.c", [("diferença", "g", 84), ("vira", "i", 80), ("expoente", "g", 84, COR), ("do", "i", 80), ("10", "g", 84)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.saida(c, t, C["s23.a"] - 0.3, lambda: (E.frase(c, t, C["s23"] + 0.2, [("exponencial", "g", 100), ("e", "i", 96), ("logaritmo", "g", 100)], W / 2, 480, "center"),
                                              E.foco(c, t, C["s23"] + 1.4, 0.4, lambda a: E.selo(c, W / 2, 660, 70, True, a))))
    if t < C["s23.a"] - 0.3:
        return
    E.frase(c, t, C["s23.a"] - 0.2, [("próxima", "i", 84), ("aula", "i", 84)], XE, 250)
    E.frase(c, t, C["s23.a"], [("sequências", "g", 140, COR)], XE, 410)
    caixas_previa(c, t, C["s23.b"], XE, 520, ["3", "7", "11", "15", "…"])
    E.frase(c, t, C["s23.b"] + 1.0, [("o", "i", 60), ("10º", "g", 64, COR), ("termo", "i", 60), ("pela", "i", 60), ("regra", "g", 64)], XE, 790)
    E.frase(c, t, C["s23.c"], [("posição", "g", 64, COR), ("e", "i", 60), ("valor", "g", 64)], XE, 890)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], 1450, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, atalho=b_atalho, fim=b_fim)
