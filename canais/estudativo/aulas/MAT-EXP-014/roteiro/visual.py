"""Visual — Estudativo · MAT-EXP-014: escalas logarítmicas, pH, Richter e decibéis.

Linguagem visual da trilha Exponencial e Logaritmo (definida em MAT-EXP-001; peças de MAT-EXP-013): expoente e entrada em índigo
(ENT); base e saída em preto (SAI); fx() pinta cada pedaço da fórmula, com índice de log ("log_2 x") e letras com índice em
Unicode (A₀, I₀, H⁺) na grotesca. Nesta aula: a régua da escala com um salto "×10" por ponto (E.reta + E.salto) e as potências
de 10 embaixo; cada fórmula entra inteira e ganha pílulas que dizem o que é cada letra; copos com o líquido mais ácido na cor
da matéria; sismogramas (onda()) com a amplitude de verdade, 100 vezes maior; colunas de intensidade 1, 10, 100."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Exponencial e Logaritmo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / expoente / entrada · base / saída
ARQUIVO_FINAL = "estudativo_MAT-EXP-014_escalas_logaritmicas_ph_richter_decibeis.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "ph", "richter", "som", "atalho", "questao", "fim"))
BR = "#FFFFFF"

lg = math.log10
assert lg(100) == 2 and lg(1000) == 3 and lg(10 ** 6) == 6 and -lg(1e-3) == 3 and abs(1e-3 / 1e-5 - 100) < 1e-9
assert 7 - 5 == 2 and 10 ** 2 == 100 and 10 / 10 == 1 and 10 ** 1 == 10 and 20 / 10 == 2 and 5 - 3 == 2 and 10 * 10 == 100
assert 90 - 60 == 30 and 30 / 10 == 3 and 10 ** 3 == 1000 and 60 + 60 / 2 == 90


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
def copo(c, cx, by, w, h, nivel, cor, a=1.0):
    """copo de vidro visto de frente, com líquido até `nivel` (0..1) na cor dada"""
    if a <= 0:
        return
    path = skia.Path()
    path.moveTo(cx - w / 2, by - h)
    path.lineTo(cx - w * 0.4, by - 14)
    path.quadTo(cx - w * 0.4, by, cx - w * 0.4 + 14, by)
    path.lineTo(cx + w * 0.4 - 14, by)
    path.quadTo(cx + w * 0.4, by, cx + w * 0.4, by - 14)
    path.lineTo(cx + w / 2, by - h)
    c.save()
    c.clipPath(path, skia.ClipOp.kIntersect, True)
    c.drawRect(skia.Rect.MakeLTRB(cx - w, by - h * nivel, cx + w, by + 2), M.paint(cor, a))
    c.restore()
    c.drawPath(path, M.paint(TINTA, a, stroke=7, cap_round=True))


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


def seta_para(c, t, t0, x0, y0, x1, y1, cor=None):
    p = ep(t, t0, 0.4)
    if p > 0:
        M.arrow(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor or TINTA2, 1.0, 4, 16, 1.0)


def bloco_texto(c, t, t0, linhas, x, y, size=46, dy=58, cor=TINTA, est="b"):
    for i, s in enumerate(linhas):
        E.foco(c, t, t0 + 0.15 * i, 0.4, lambda a, s=s, i=i: E.escreve(c, s, x, y + i * dy, size, est, cor, a), sobe=6)


def barra_int(c, t, t0, cx, base, w, h, rot, val, cor=None):
    """coluna de intensidade que cresce a partir da base, com rótulo embaixo e valor em cima"""
    q = ease_out(prog(t, t0, 0.6))
    if q <= 0:
        return
    hh = max(4, h * q)
    M.rrect(c, cx - w / 2, base - hh, w, hh, 8, cor or COR, 1.0)
    E.foco(c, t, t0, 0.4, lambda a: centro(c, rot, cx, base + 56, 42, "b", TINTA, a), sobe=6)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, val, cx, base - hh - 22, 54, "g", cor or COR, a), sobe=6)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        for k, cx, ph, nivel, cor in (("s01.a", 560, "pH 3", 0.72, COR), ("s01.b", 1060, "pH 5", 0.72, E.mix(COR, "#FFFFFF", 0.72))):
            E.foco(c, t, C[k], 0.5, lambda a, cx=cx, nivel=nivel, cor=cor: copo(c, cx, 760, 280, 400, nivel, cor, a))
            E.foco(c, t, C[k] + 0.2, 0.5, lambda a, cx=cx, ph=ph: centro(c, ph, cx, 880, 96, "g", TINTA, a))
        q = ep(t, C["s01.c"], 0.5)
        if q > 0:
            E.chave(c, 560, 1060, 960, TINTA2, q, 26)
        E.foco(c, t, C["s01.c"] + 0.2, 0.4, lambda a: centro(c, "só 2 pontos", 810, 1040, 56, "i", TINTA2, a))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (centro(c, "100", 1560, 470, 230, "g", COR, a), centro(c, "vezes", 1560, 580, 80, "i", TINTA, a),
                                                 centro(c, "mais ácido", 1560, 680, 80, "g", TINTA, a)))
        if t >= C["s01.d"]:
            anel(c, t, C["s01.d"] + 0.3, 560, 560)
    E.saida(c, t, C["s02.b"] - 0.1, cena1)
    E.saida(c, t, C["s02.b"] - 0.1, lambda: E.foco(c, t, C["s02.a"], 0.5, lambda a: E.pilula(c, "escala logarítmica", W / 2, 150, 60, "g", a=a)))
    if t < C["s02.b"]:
        return
    tb, te = C["s02.b"], C["s02.end"]
    E.foco(c, t, te - 1.8, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, te - 1.8, 0.7))), blur=0)
    E.frase(c, t, tb, ps("até o fim da aula", "i", 84), XE, 280)
    E.frase(c, t, tb + 2.0, [("acidez", "g", 120, COR)], XE, 440)
    E.frase(c, t, tb + 2.4, [("terremotos", "g", 120, COR)], XE, 600)
    E.frase(c, t, tb + 2.8, [("barulho", "g", 120, COR)], XE, 760)
    E.frase(c, t, tb + 3.6, ps("com a fórmula da questão", "i", 60, TINTA2), XE, 880)
    E.foco(c, t, te - 1.4, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                           E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("2", "g", 90, COR, C["s03"] + 0.6), ("coisas", "i", 84, TINTA, C["s03"] + 0.8)], W / 2, 220, "center")
    itens = (("s03.a", lambda a, y: (fx(c, [("log 1.000 = ", SAI), ("3", COR)], 430, y, 100, a),
                                     E.escreve(c, "base 10 escondida", 1080, y, 60, "i", TINTA2, a))),
             ("s03.b", lambda a, y: (fx(c, [("log f{A}{B} = log A − log B", SAI)], 430, y + 10, 92, a),
                                     E.escreve(c, "divisão vira diferença", 1300, y, 56, "i", TINTA2, a))))
    for i, (k, fn) in enumerate(itens):
        y = 480 + i * 260
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                     E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
        E.foco(c, t, C[k] + 0.2, 0.5, lambda a, fn=fn, y=y: fn(a, y))


# ---------------- a ideia: o log conta os zeros ----------------
def b_ideia(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("de", "i", 70), ("0,001", "b", 50, TINTA2), ("a", "i", 70), ("1.000.000", "g", 110, COR)], W / 2, 200, "center")
    E.frase(c, t, C["s04.b"], [("o", "i", 76), ("log", "g", 80, COR), ("conta", "i", 76), ("os", "i", 76), ("zeros", "g", 80)], W / 2, 330, "center")
    linhas = (("s04.c", [("log 1", SAI), ("00", COR), (" = ", SAI), ("2", COR)]),
              ("s04.d", [("log 1.", SAI), ("000", COR), (" = ", SAI), ("3", COR)]),
              ("s04.e", [("log 1.", SAI), ("000", COR), (".", SAI), ("000", COR), (" = ", SAI), ("6", COR)]))
    for i, (k, partes) in enumerate(linhas):
        fx_em(c, t, C[k], partes, 560, 470 + i * 115, 90)
    # a régua: cada ponto, ×10
    y, x0, x1 = 860, 300, 1620
    vx = E.reta(c, t, C["s04.f"] - 0.5, x0, x1, y, 0, 6, list(range(7)), lambda v: "", tm=[C["s04.f"] - 0.4 + 0.08 * i for i in range(7)])
    for k in range(7):
        E.foco(c, t, C["s04.f"] - 0.3 + 0.08 * k, 0.4, lambda a, k=k: (centro(c, str(k), vx(k), y + 70, 50, "g", COR, a),
                                                                     E.formula(c, f"10^{k}", vx(k), y + 150, 46, "b", TINTA2, a, "center")), sobe=6)
    for k in range(6):
        E.salto(c, t, C["s04.f"] + 0.3 + 0.18 * k, vx(k) + 8, vx(k + 1) - 8, y - 6, 70, rotulo="×10", size=40)


# ---------------- pH ----------------
def b_ph(c, t, C, b):
    S = 120
    partes = [("pH = −log ", SAI), ("[H⁺]", ENT)]
    w, xs, ws = fx(c, partes, W / 2, 0, S, 0, "center")

    def s05_06():
        fx_em(c, t, C["s05.a"], partes, W / 2, 260, S, "center")
        q = ep(t, C["s05.b"], 0.4)
        caixa(c, xs[1], 260, ws[1] - S * 0.04, S, q)
        seta_para(c, t, C["s05.b"] + 0.1, xs[1] + ws[1] / 2, 310, xs[1] + ws[1] / 2 + 60, 380, COR)
        E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: E.pilula(c, "hidrogênio em cada litro", xs[1] + ws[1] / 2 + 60, 420, 44, "g", a=a), sobe=6)
        E.saida(c, t, C["s06"] - 0.1, lambda: E.frase(c, t, C["s05.c"], [("mais", "i", 80), ("H⁺,", "g", 84, ENT), ("mais", "i", 80), ("ácido", "g", 84)],
                                                       W / 2, 640, "center"))
        if t >= C["s06"]:
            fx_em(c, t, C["s06.a"], [("[H⁺] = 10", ENT), ("^{−3}", ENT)], 560, 600, 100)
            fx_em(c, t, C["s06.b"], [("log 10", SAI), ("^{−3}", ENT), (" = −3", SAI)], 560, 750, 100)
            fx_em(c, t, C["s06.c"], [("pH = −(−3) = ", SAI), ("3", COR)], 560, 900, 100)
            nota(c, t, C["s06.d"], "o menos deixa o pH positivo", 1460, 870, 40, fundo=TINTA)
    E.saida(c, t, C["s07"] - 0.1, s05_06)
    if t < C["s07"]:
        return
    # pH 3 contra pH 5
    fx_em(c, t, C["s07"], [("pH 3:  ", SAI), ("[H⁺] = 10", ENT), ("^{−3}", ENT)], XE, 220, 76)
    fx_em(c, t, C["s07.a"], [("pH 5:  ", SAI), ("[H⁺] = 10", ENT), ("^{−5}", ENT)], 1000, 220, 76)
    fx_em(c, t, C["s07.a"] + 2.2, [("f{10^{−3}}{10^{−5}}", SAI)], XE + 60, 480, 120)
    fx_em(c, t, C["s07.b"], [("= 10", SAI), ("^{−3 − (−5)}", COR)], XE + 380, 480, 110)
    fx_em(c, t, C["s07.c"], [("= 10", SAI), ("^2", COR), (" = ", SAI), ("100", COR)], XE + 1000, 480, 110)
    y = 820
    vx = E.reta(c, t, C["s07.b"] - 0.3, 260, 900, y, -5, -3, [-5, -4, -3], E._num, size=46)
    E.foco(c, t, C["s07.b"] - 0.3, 0.4, lambda a: E.escreve(c, "expoente", 260 - 40, y - 150, 44, "i", TINTA2, a))
    E.salto(c, t, C["s07.b"] + 0.2, vx(-5) + 8, vx(-4) - 8, y - 6, 80, rotulo="1", size=40)
    E.salto(c, t, C["s07.b"] + 0.6, vx(-4) + 8, vx(-3) - 8, y - 6, 80, rotulo="2", size=40)
    E.frase(c, t, C["s07.d"], [("pH", "g", 84), ("menor,", "i", 80), ("mais", "i", 80), ("ácido", "g", 84, COR)], 1060, 780)
    nota(c, t, C["s07.e"], "cada ponto a menos: × 10", 1440, 900, 46)


# ---------------- Richter ----------------
def b_richter(c, t, C, b):
    S = 130
    partes = [("M", SAI), (" = log ", SAI), ("f{A}{A₀}", ENT)]
    w, xs, ws = fx(c, partes, W / 2, 0, S, 0, "center")

    def s08():
        fx_em(c, t, C["s08.a"], partes, W / 2, 300, S, "center")
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "magnitude", xs[0] + ws[0] / 2, 470, 44, "g", fundo=TINTA, a=a), sobe=6)
        xf = xs[2] + ws[2]
        seta_para(c, t, C["s08.c"], xf + 170, 200, xf + 10, 220, COR)
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "amplitude: o tremor", xf + 330, 190, 40, "g", a=a), sobe=6)
        seta_para(c, t, C["s08.d"], xf + 170, 380, xf + 10, 360, TINTA2)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "referência: fixa", xf + 320, 390, 40, "g", fundo=TINTA2, a=a), sobe=6)
        # o sismograma: a amplitude é a altura do tremor
        a = ep(t, C["s08.c"], 0.4)
        if a > 0:
            M.rrect(c, 360, 610, 1200, 340, 24, "#FFFFFF", a)
            M.line(c, 400, 780, 1520, 780, FIO, a, 3)
            p = prog(t, C["s08.c"] + 0.2, 1.6)
            onda(c, 400, 780, 1120, 130, a, p)
            if p >= 1:
                E.foco(c, t, C["s08.c"] + 1.8, 0.4, lambda q: (M.line(c, 1440, 780, 1440, 650, COR, q, 5), M.line(c, 1420, 650, 1460, 650, COR, q, 5),
                                                               E.escreve(c, "A", 1470, 735, 56, "g", COR, q)))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return

    def s09():
        E.frase(c, t, C["s09.a"], [("magnitude", "i", 66), ("7", "g", 76, COR), ("contra", "i", 66), ("5", "g", 76, COR)], W / 2, 170, "center")
        fx_em(c, t, C["s09.b"], [("7 − 5 = ", SAI), ("2", COR)], W / 2, 320, 100, "center")
        fx_em(c, t, C["s09.c"], [("M = log A − log A₀", SAI)], W / 2, 480, 84, "center")
        S2 = 76
        lin = [("(log A₇ − ", SAI), ("log A₀", TINTA2), (") − (log A₅ − ", SAI), ("log A₀", TINTA2), (")", SAI)]
        _, lx, lw = fx(c, lin, W / 2, 0, S2, 0, "center")
        fx_em(c, t, C["s09.c"] + 1.2, lin, W / 2, 640, S2, "center")
        if t >= C["s09.d"]:
            for k, d in ((1, 0), (3, 0.3)):
                E.risco(c, lx[k] - 6, 660, lx[k] + lw[k] - 10, 600, t, C["s09.d"] + d, cor=ERRADO, largura=10)
        fx_em(c, t, C["s09.e"], [("log f{A₇}{A₅} = ", SAI), ("2", COR)], W / 2, 860, 110, "center")
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    fx_em(c, t, C["s10"], [("log f{A₇}{A₅} = 2", SAI)], XE, 260, 90)
    fx_em(c, t, C["s10.a"], [("f{A₇}{A₅} = 10", SAI), ("^2", COR)], 800, 260, 90)
    fx_em(c, t, C["s10.a"] + 0.6, [(" = 100", COR)], 1260, 260, 90)
    for k, y, amp, rot in (("s10", 520, 1.3, "magnitude 5"), ("s10.b", 820, 125, "magnitude 7")):
        a = ep(t, C[k], 0.4)
        if a > 0:
            M.rrect(c, 360, y - 160, 1100, 290, 24, "#FFFFFF", a)
            M.line(c, 400, y, 1420, y, FIO, a, 3)
            onda(c, 400, y, 1020, amp, a, prog(t, C[k] + 0.2, 1.4), TINTA if amp < 10 else COR)
            E.foco(c, t, C[k], 0.4, lambda q, y=y, rot=rot: E.escreve(c, rot, 1500, y + 16, 52, "g", TINTA, q))
    E.foco(c, t, C["s10.b"] + 1.6, 0.5, lambda a: (E.bola(c, 1660, 680, 90, a=a), centro(c, "×100", 1660, 700, 56, "g", BR, a)))


# ---------------- decibéis ----------------
def b_som(c, t, C, b):
    S = 120
    partes = [("β", SAI), (" = ", SAI), ("10 ·", COR), (" log ", SAI), ("f{I}{I₀}", ENT)]
    w, xs, ws = fx(c, partes, W / 2, 0, S, 0, "center")

    def s11():
        fx_em(c, t, C["s11.a"], partes, W / 2, 320, S, "center")
        E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "nível em decibéis", xs[0] + ws[0] / 2, 500, 44, "g", fundo=TINTA, a=a), sobe=6)
        xf = xs[4] + ws[4]
        seta_para(c, t, C["s11.c"], xf + 150, 210, xf + 10, 240, COR)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "intensidade: a energia do som", xf + 280, 170, 40, "g", a=a), sobe=6)
        seta_para(c, t, C["s11.d"], xf + 150, 420, xf + 10, 390, TINTA2)
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "referência: o som mais fraco", xf + 250, 450, 40, "g", fundo=TINTA2, a=a), sobe=6)
        q = ep(t, C["s11.e"], 0.4)
        caixa(c, xs[2], 320, ws[2] - S * 0.2, S, q)
        anel(c, t, C["s11.e"], xs[2] + ws[2] / 2 - 20, 280)
        E.frase(c, t, C["s11.e"] + 0.5, [("o", "i", 70), ("10", "g", 76, COR), ("na", "i", 70), ("frente", "i", 70), ("muda", "i", 70), ("a", "i", 70),
                                         ("conta", "g", 76)], W / 2, 760, "center")
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], [("+10", "g", 110, COR), ("dB", "g", 90)], XE, 220)
    fx_em(c, t, C["s12.b"], [("10 · log ", SAI), ("f{I₂}{I₁}", ENT), (" = 10", SAI)], XE, 450, 96)
    E.foco(c, t, C["s12.c"] - 0.4, 0.4, lambda a: E.pilula(c, "÷ 10", XE + 640, 540, 44, "g", fundo=TINTA, a=a), sobe=6)
    fx_em(c, t, C["s12.c"], [("log ", SAI), ("f{I₂}{I₁}", ENT), (" = 1", SAI)], XE, 690, 96)
    fx_em(c, t, C["s12.d"], [("f{I₂}{I₁}", ENT), (" = 10", COR)], XE, 920, 96)
    E.foco(c, t, C["s12.d"] + 0.5, 0.4, lambda a: E.escreve(c, "10 vezes", XE + 430, 910, 64, "g", COR, a))
    # colunas de intensidade
    base, hmax = 880, 560
    barra_int(c, t, C["s12.a"] + 0.4, 1180, base, 120, hmax / 100, "o outro", "1", TINTA2)
    barra_int(c, t, C["s12.d"], 1400, base, 120, hmax / 10, "+10 dB", "10")
    barra_int(c, t, C["s12.e"], 1620, base, 120, hmax, "+20 dB", "100")
    if t >= C["s12.a"]:
        M.line(c, 1080, base, 1720, base, TINTA, ep(t, C["s12.a"], 0.5), 5)
    E.foco(c, t, C["s12.e"] + 0.8, 0.4, lambda a: E.escreve(c, "intensidade", 1110, 260, 50, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("régua", "g", 90, ERRADO), ("comum?", "i", 90)], W / 2, 190, "center")
    y = 520
    vx = E.reta(c, t, C["s13.a"] + 0.3, 360, 1560, y, 1, 7, list(range(1, 8)), E._num, size=50)
    for v in (3, 5):
        E.foco(c, t, C["s13.a"] + 1.0, 0.4, lambda a, v=v: (c.drawCircle(vx(v), y, 22, M.paint(COR, a)),
                                                           centro(c, f"pH {v}", vx(v), y + 160, 52, "g", COR, a)))
    certo = C["s14.a"]
    E.saida(c, t, certo - 0.1, lambda: (fx_em(c, t, C["s13.b"], [("5 − 3 = 2", SAI)], W / 2, 820, 100, "center"),
                                        E.frase(c, t, C["s13.c"], [("2", "g", 100, ERRADO), ("vezes", "i", 90, ERRADO), ("mais", "i", 90, ERRADO),
                                                                   ("ácido", "i", 90, ERRADO)], W / 2, 970, "center")))
    if C["s13.c"] + 1.0 <= t < certo:
        E.risco(c, 640, 1000, 1280, 910, t, C["s13.c"] + 1.0, largura=14)
    if t >= certo:
        E.salto(c, t, certo + 0.2, vx(5) - 8, vx(4) + 8, y - 30, 90, rotulo="×10", size=46)
        E.salto(c, t, certo + 0.7, vx(4) - 8, vx(3) + 8, y - 30, 90, rotulo="×10", size=46)
        E.frase(c, t, certo, [("cada", "i", 76), ("ponto:", "i", 76), ("×", "g", 80, COR), ("10", "g", 80, COR)], W / 2, 830, "center")
        fx_em(c, t, C["s14.b"], [("10 × 10 = ", SAI), ("100", CERTO), (" vezes", CERTO)], W / 2, 980, 100, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15.a"], [("a", "i", 90, CLARO), ("diferença", "g", 96, BR), ("vira", "i", 90, CLARO), ("expoente", "g", 96, BR),
                                   ("do", "i", 90, CLARO), ("10", "g", 96, CLARO)], W / 2, 210, "center", passo=0.15)
        E.foco(c, t, C["s15.b"], 0.5, lambda a: (E.escreve(c, "pH e Richter", XE, 420, 70, "i", CLARO, a),
                                                 fx(c, [("diferença 2  →  10", BR), ("^2", CLARO), (" = 100", BR)], 720, 420, 90, a)))
        E.foco(c, t, C["s15.c"], 0.5, lambda a: (E.escreve(c, "decibéis", XE, 640, 70, "i", CLARO, a),
                                                 fx(c, [("÷ 10", CLARO), (" antes", BR)], 720, 640, 90, a)))
        E.foco(c, t, C["s15.c"] + 2.0, 0.5, lambda a: fx(c, [("+30 dB  →  30 ÷ 10 = 3", BR)], 720, 800, 84, a))
        E.foco(c, t, C["s15.d"], 0.5, lambda a: fx(c, [("10", BR), ("^3", CLARO), (" = 1.000", BR), (" vezes", CLARO)], 720, 950, 96, a))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.foco(c, t, C["s16.a"], 0.5, lambda a: fx(c, [("log A − log B = log ", BR), ("f{A}{B}", CLARO)], W / 2, 260, 100, a, "center"))
    E.frase(c, t, C["s16.b"], [("não", "g", 76, BR), ("compensa:", "i", 72, CLARO)], XE, 500)
    E.foco(c, t, C["s16.b"] + 0.8, 0.5, lambda a: fx(c, [("pH 3 contra pH 3,3  →  10", BR), ("^{0,3}", CLARO)], XE, 620, 84, a))
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.pilula(c, "pede log 2: outra aula", 1440, 500, 44, "g", fundo=CLARO, cor="#07070F", a=a))
    E.foco(c, t, C["s16.d"], 0.4, lambda a: E.pilula(c, "leia sempre a fórmula do enunciado", W / 2, 860, 54, "g", fundo=BR, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s17"] + 1.0, ps("valores criados para esta aula", "i", 44, TINTA2), XE + 480, 190)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: (E.escreve(c, "liquidificador:", XE, 350, 72, "i", TINTA, a),
                                             E.escreve(c, "90 dB", XE + 520, 350, 90, "g", COR, a)))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: (E.escreve(c, "conversa:", XE, 480, 72, "i", TINTA, a),
                                             E.escreve(c, "60 dB", XE + 520, 480, 90, "g", TINTA, a)))
    fx_em(c, t, C["s17.c"], [("β = 10 · log ", SAI), ("f{I}{I₀}", ENT)], XE, 690, 96)
    E.frase(c, t, C["s17.d"], [("quantas", "i", 80), ("vezes", "i", 80), ("mais", "i", 80), ("intenso?", "g", 84, COR)], XE, 920)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1540, cy=520, r=150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        fx_em(c, t, C["s19.a"], [("90 − 60 = ", SAI), ("30 dB", COR)], XE, 230, 96)
        fx_em(c, t, C["s19.b"], [("30 ÷ 10 = ", SAI), ("3", COR)], XE, 400, 96)
        fx_em(c, t, C["s19.c"], [("log ", SAI), ("f{liquidificador}{conversa}", ENT), (" = 3", SAI)], XE, 600, 96)
        fx_em(c, t, C["s19.d"], [("10", SAI), ("^3", COR), (" = 1.000", SAI)], XE, 820, 110)
        E.foco(c, t, C["s19.d"] + 0.8, 0.5, lambda a: (E.bola(c, 1420, 560, 210, CERTO, a), centro(c, "1.000", 1420, 560, 110, "g", BR, a),
                                                       centro(c, "vezes", 1420, 640, 56, "i", BR, a)))
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("o nível", "i", 66, TINTA2), 400, 200)
    E.colunas(c, t, C["s20.a"] - 0.3, [("conversa", 60, TINTA), ("liquidificador", 90)], 400, 230, 1200, 280, vmax=100, deitado=True,
              fmt=lambda v: f"{v} dB", passo=0.3)
    E.foco(c, t, C["s20.a"] + 1.0, 0.4, lambda a: E.escreve(c, "só a metade a mais", 640, 200, 48, "i", TINTA2, a))
    E.frase(c, t, C["s20.b"], ps("a intensidade", "i", 66, TINTA2), 400, 620)
    E.colunas(c, t, C["s20.b"], [("conversa", 1, TINTA), ("liquidificador", 1000)], 400, 650, 1200, 280, vmax=1100, deitado=True,
              fmt=lambda v: "1" if v == 1 else "1.000", passo=0.3)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s21.a", [("cada", "i", 80), ("ponto:", "i", 80), ("× 10", "g", 84, COR)]),
                 ("s21.b", [("diferença,", "g", 84), ("ajustada", "i", 80), ("pela", "i", 80), ("fórmula", "g", 84)]),
                 ("s21.c", [("vira", "i", 80), ("o", "i", 80), ("expoente", "g", 84, COR), ("do", "i", 80), ("10", "g", 84)]))
        for i, (k, partes) in enumerate(itens):
            y = 430 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s22.a"], [("prática:", "g", 130, COR)], XE, 460)
    E.frase(c, t, C["s22.a"] + 0.4, [("logaritmos", "g", 130, COR)], XE, 600)
    E.frase(c, t, C["s22.a"] + 1.4, ps("propriedades, equações e escalas", "i", 58, TINTA2), XE, 720)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 445, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, ph=b_ph, richter=b_richter, som=b_som, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
