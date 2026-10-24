"""Visual — Matrizes e Operações, Episódio 3: multiplicação de matrizes, linha por coluna (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, frações...).
Peças deste episódio: matriz() (colchetes, linha e coluna destacadas em cores diferentes, casas acendendo), caixa_lxc()
(a linha DEITADA girando para o lado da coluna: os pares se multiplicam um a um e caem numa soma), domino() (as ordens como
peças de dominó: dentro encaixa ou é rejeitado; fora dá o tamanho), voos() (mapa de quatro cidades com setas de voo e rotas
acendendo), cupom() (o cupom do supermercado), linha() (texto com cor por trecho).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Destaque fixo das contas: LINHA da primeira matriz em AZUL, COLUNA da segunda em LARANJA, resultado em VERDE.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum048", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_matrizes_ep3_linha_por_coluna.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
LIN = BLUE            # a linha da primeira matriz
COL = "#E8743B"       # a coluna da segunda matriz
RES = GREEN           # o resultado


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def colchetes(c, x0, y0, w, h, a, col=None, sw=5):
    col = col or INK
    s = min(22, w * 0.18)
    for xb, d in ((x0 - 10, 1), (x0 + w + 10, -1)):
        p = skia.Path()
        p.moveTo(xb + d * s, y0 - 8); p.lineTo(xb, y0 - 8); p.lineTo(xb, y0 + h + 8); p.lineTo(xb + d * s, y0 + h + 8)
        c.drawPath(p, paint(col, a, stroke=sw))


def matriz(c, M, cx, cy, a, cell=86, size=None, row=None, col=None, hl=1.0, cores=None, alfas=None, rotulo=None,
           ordem=None, rot_col=None, cellh=None, fundo=None):
    """matriz com colchetes, centrada em (cx, cy). row/col = linha/coluna destacadas (azul/laranja), hl = intensidade;
    cores/alfas = {(i, j): cor/alfa} por casa; rotulo = nome acima (ex.: 'A'); ordem = texto abaixo (ex.: '2 × 3')."""
    if a <= 0:
        return None
    nr, nc = len(M), len(M[0])
    ch = cellh or cell
    size = size or cell * 0.52
    w, h = nc * cell, nr * ch
    x0, y0 = cx - w / 2, cy - h / 2
    if fundo:
        rrect(c, x0 - 4, y0 - 4, w + 8, h + 8, 10, fundo, a)
    if row is not None and hl > 0:
        rrect(c, x0 - 6, y0 + row * ch + 5, w + 12, ch - 10, min(22, ch / 2 - 6), mix("#FFFFFF", LIN, 0.22), a * hl)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 6, y0 + row * ch + 5, w + 12, ch - 10),
                                          min(22, ch / 2 - 6), min(22, ch / 2 - 6)), paint(LIN, a * hl, stroke=3))
    if col is not None and hl > 0:
        rrect(c, x0 + col * cell + 5, y0 - 6, cell - 10, h + 12, min(22, cell / 2 - 6), mix("#FFFFFF", COL, 0.22), a * hl)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + col * cell + 5, y0 - 6, cell - 10, h + 12),
                                          min(22, cell / 2 - 6), min(22, cell / 2 - 6)), paint(COL, a * hl, stroke=3))
    for i in range(nr):
        for j in range(nc):
            v = M[i][j]
            if v is None:
                continue
            cc = (cores or {}).get((i, j))
            if cc is None:
                cc = mix(INK, LIN, hl) if i == row else mix(INK, COL, hl) if j == col else INK
            aa = a * (alfas or {}).get((i, j), 1.0)
            if aa > 0:
                fmid(c, str(v), x0 + (j + 0.5) * cell, y0 + (i + 0.5) * ch, size, "black", cc, aa)
    colchetes(c, x0, y0, w, h, a)
    if rotulo:
        fmid(c, rotulo, cx, y0 - 44, size * 0.9, "black", rot_col or INK, a)
    if ordem:
        fmid(c, ordem, cx, y0 + h + 40, max(20, size * 0.5), "black", GRAY, a)
    return x0, y0, w, h


def casa(cx, cy, M, cell, i, j, cellh=None):
    ch = cellh or cell
    nr, nc = len(M), len(M[0])
    return cx - nc * cell / 2 + (j + 0.5) * cell, cy - nr * ch / 2 + (i + 0.5) * ch


def caixa_lxc(c, lin, colv, cx, cy, u, a, size=46, dy=64, rot=None):
    """a LINHA deitada gira para o lado da COLUNA (u: 0 → 0,3); os pares se multiplicam um a um (0,3 → 0,75) e caem
    numa soma (0,75 → 1). Desenha centrado em (cx, cy)."""
    if a <= 0:
        return
    n = len(lin)
    xl, xc_, xe, xp = cx - 200, cx - 40, cx + 60, cx + 170
    y_top = cy - (n - 1) * dy / 2 - 20
    g = ease_io(clamp(u / 0.3))
    for k in range(n):
        yk = cy - (n - 1) * dy / 2 + k * dy - 20
        # linha: começa deitada (no alto, lado a lado) e termina em pé ao lado da coluna
        xh = xl - (n - 1) * 70 / 2 + k * 70 - 140
        yh = y_top - 90
        x_, y_ = lerp(xh, xl, g), lerp(yh, yk, g)
        fmid(c, str(lin[k]), x_, y_, size, "black", LIN, a)
        fmid(c, str(colv[k]), xc_, yk, size, "black", COL, a)
        ak = ep(u, 0.3 + 0.45 * k / n, 0.12)
        if ak > 0:
            fmid(c, "×", (xl + xc_) / 2, yk, size * 0.8, "black", GRAY, a * ak)
            fmid(c, "=", xe, yk, size * 0.8, "black", GRAY, a * ak)
            fmid(c, str(lin[k] * colv[k]), xp, yk, size, "black", INK, a * ak)
    if rot:
        fmid(c, rot[0], xh_lbl(xl, n), y_top - 150, 24, "black", LIN, a * (1 - g) + a * 0.0)
    asum = ep(u, 0.78, 0.15)
    if asum > 0:
        yb = cy + (n - 1) * dy / 2 + dy * 0.55 - 20
        line(c, xp - 70, yb - 26, xp + 70, yb - 26, INK2, a * asum, 4)
        fmid(c, "+", xp - 96, cy + (n - 1) * dy / 2 - 20 - dy / 2, size * 0.7, "black", GRAY, a * asum)
        fmid(c, str(sum(x * y for x, y in zip(lin, colv))), xp, yb + 24, size * 1.15, "black", RES, a * asum)


def xh_lbl(xl, n):
    return xl - 140


def domino(c, o1, o2, cx, cy, a, u=1.0, size=52, ok=None, res_a=1.0, tw=230, th=110):
    """as ordens como peças de dominó: o1 = (m, n), o2 = (n2, p). u: 0 (afastadas) → 1 (encostadas).
    dentro iguais: as metades de dentro ficam verdes e o resultado m × p aparece embaixo (res_a);
    dentro diferentes: as peças tremem e ficam vermelhas (selo NÃO ENCAIXA)."""
    if a <= 0:
        return
    ok = (o1[1] == o2[0]) if ok is None else ok
    gap = lerp(140, 10 if ok else 60, ease_io(clamp(u)))
    shake = 0 if ok else 8 * math.sin(u * 40) * clamp((u - 0.6) / 0.2) * (1 - clamp((u - 0.9) / 0.1))
    for k, (o, sx) in enumerate(((o1, -1), (o2, 1))):
        x = cx + sx * (gap / 2 + tw / 2) - tw / 2 + (shake if k else -shake)
        rrect(c, x, cy - th / 2, tw, th, 18, "#FFFFFF", a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - th / 2, tw, th), 18, 18), paint(INK, a, stroke=4))
        line(c, x + tw / 2, cy - th / 2 + 14, x + tw / 2, cy + th / 2 - 14, INK, a, 4)
        dentro = 1 if k == 0 else 0
        for h in range(2):
            hx = x + tw * (0.25 + 0.5 * h)
            inner = (h == 1) if k == 0 else (h == 0)
            if inner:
                cc = mix(INK, GREEN if ok else RED, clamp(u))
                rrect(c, x + tw * 0.5 * h + 8, cy - th / 2 + 8, tw / 2 - 16, th - 16, 12,
                      mix("#FFFFFF", GREEN if ok else RED, 0.18), a * clamp(u))
            else:
                cc = mix(INK, PURPLE, res_a if ok else 0)
            fmid(c, str(o[h]), hx, cy, size, "black", cc, a)
    if ok and res_a > 0:
        fmid(c, "×", cx - gap / 2 - tw - 30, cy, size * 0.7, "black", GRAY, 0)
        y2 = cy + th / 2 + 70
        x1 = cx - gap / 2 - tw * 0.75
        x2 = cx + gap / 2 + tw * 0.75
        arrow(c, x1, cy + th / 2 + 6, cx - 70, y2 - 24, PURPLE, a * res_a, 4, 14)
        arrow(c, x2, cy + th / 2 + 6, cx + 70, y2 - 24, PURPLE, a * res_a, 4, 14)
        chip(c, f"{o1[0]} × {o2[1]}", cx, y2 + 10, PURPLE, a * res_a, size * 0.8)
    if not ok and u > 0.7:
        selo(c, cx + gap / 2 + tw + 160, cy - th * 0.2, a * ep(u, 0.7, 0.2), "NÃO ENCAIXA", RED, -4, 34)


POS_SQ = {1: (-1, -1), 2: (1, -1), 3: (1, 1), 4: (-1, 1)}


def voos(c, arestas, cx, cy, a, L=150, r=42, rotas=(), rotas_a=(), cor_rota=GREEN, faltando=(), faltando_a=0.0,
         arestas_a=None, size=36):
    """mapa com 4 cidades nos cantos de um quadrado (1 ↖, 2 ↗, 3 ↘, 4 ↙) e setas de voo direto.
    rotas = lista de caminhos [(1, 2, 4), ...] que acendem (rotas_a); faltando = setas tracejadas em vermelho (sem voo)."""
    if a <= 0:
        return
    pos = {k: (cx + L * dx, cy + L * dy) for k, (dx, dy) in POS_SQ.items()}
    pares = set(arestas)

    def seta(i, j, col, aa, w=4, dash=None):
        (x0, y0), (x1, y1) = pos[i], pos[j]
        d = math.hypot(x1 - x0, y1 - y0)
        ux, uy = (x1 - x0) / d, (y1 - y0) / d
        off = 12 if (j, i) in pares else 0
        nx, ny = -uy * off, ux * off
        xa, ya = x0 + ux * (r + 6) + nx, y0 + uy * (r + 6) + ny
        xb, yb = x1 - ux * (r + 8) + nx, y1 - uy * (r + 8) + ny
        if dash:
            line(c, xa, ya, xb, yb, col, aa, w, dash=dash)
        else:
            arrow(c, xa, ya, xb, yb, col, aa, w, 16)

    for k, e in enumerate(arestas):
        ae = a * ((arestas_a or {}).get(e, 1.0))
        if ae > 0:
            seta(*e, LIGHT if rotas_a and max(rotas_a) > 0 else INK2, ae, 4)
    for rt, ra in zip(rotas, rotas_a):
        if ra <= 0:
            continue
        for p_, q_ in zip(rt[:-1], rt[1:]):
            seta(p_, q_, cor_rota, a * ra, 8)
    for e in faltando:
        if faltando_a > 0:
            seta(*e, RED, a * faltando_a, 4, dash=(10, 8))
    acesas = set()
    for rt, ra in zip(rotas, rotas_a):
        if ra > 0.5:
            acesas |= set(rt)
    for k, (x, y) in pos.items():
        c.drawCircle(x, y, r + 4, paint("#FFFFFF", a))
        c.drawCircle(x, y, r, paint(cor_rota if k in acesas else BLUE, a))
        fmid(c, str(k), x, y, size, "black", "#FFFFFF", a)


def cupom(c, x, y, w, itens, a, total_a, total="R$ 127"):
    """o cupom do supermercado: itens = [(nome, qtd, preço, subtotal, alfa)]"""
    if a <= 0:
        return
    h = 120 + 78 * len(itens) + 110
    rrect(c, x, y, w, h, 6, PAPEL, a, shadow=True)
    text(c, "SUPERMERCADO", x + w / 2, y + 56, 28, "black", INK2, a, tracking=3)
    line(c, x + 24, y + 84, x + w - 24, y + 84, LIGHT, a, 3, dash=(8, 6))
    yy = y + 140
    for nome, q, p, st, ai in itens:
        if ai > 0:
            text(c, nome, x + 34, yy, 28, "bold", INK2, a * ai, align="left")
            linha(c, [(q, LIN), (" × ", GRAY), (p, COL)], x + w * 0.60, yy - 10, 30, a * ai)
            text(c, st, x + w - 34, yy, 30, "black", INK, a * ai, align="right")
        yy += 78
    line(c, x + 24, yy - 40, x + w - 24, yy - 40, LIGHT, a, 3, dash=(8, 6))
    if total_a > 0:
        text(c, "TOTAL", x + 34, yy + 20, 32, "black", INK, a * total_a, align="left")
        text(c, total, x + w - 34, yy + 20, 40, "black", RES, a * total_a, align="right")


def pergunta(c, s, cx, cy, a, col=PURPLE, size=36):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 38, w, 76, 38, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "MATRIZES · LINHA POR COLUNA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 230, 1520, 140, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("10", LIN), (" · ", GRAY), ("5", COL), ("  +  ", INK), ("5", LIN), (" · ", GRAY), ("9", COL),
                  ("  +  ", INK), ("4", LIN), (" · ", GRAY), ("8", COL), ("  =  ", INK), ("127", RES)], W / 2, 300, 70, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        pill(c, "o gasto de UMA filial em UM fornecedor (R$)", W / 2, 430, BLUE, size=30, a=ab, anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        matriz(c, [[10, 5, 4]], 560, 640, acc, cell=96, row=0, hl=1.0)
        fmid(c, "·", 800, 640, 70, "black", GRAY, acc)
        matriz(c, [[5], [9], [8]], 940, 640, acc, cell=96, cellh=74, col=0, hl=1.0)
        fmid(c, "=", 1090, 640, 70, "black", GRAY, acc)
        matriz(c, [[127]], 1240, 640, acc, cell=150, cores={(0, 0): RES})
        selo(c, 1560, 560, ep(t, C["01.c"] + 1.6, 0.4), "TODA A MULTIPLICAÇÃO", GREEN, -4, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "se o produto EXISTE", "a regra do dominó"),
            ("02.b", "qual o TAMANHO dele", "linhas × colunas do resultado"),
            ("02.c", "o que cada número SIGNIFICA", "o endereço diz quem multiplica quem")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "DO EPISÓDIO 1", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "aᵢⱼ = o assento do cinema", 560, 290, 38, "black", BLUE, aa)
        x0, y0 = 300, 360
        for i in range(3):
            for j in range(4):
                on_ = (i == 1 and j == 2)
                rrect(c, x0 + j * 130, y0 + i * 100, 110, 80, 14, mix("#FFFFFF", BLUE, 0.6 if on_ else 0.10), aa)
        text(c, "fileira 2 = LINHA", 560, 720, 30, "black", LIN, ep(t, C["03.a"] + 1.4, 0.4))
        text(c, "poltrona 3 = COLUNA", 560, 765, 30, "black", COL, ep(t, C["03.a"] + 2.6, 0.4))
        fmid(c, "a₂₃", x0 + 2 * 130 + 55, y0 + 100 + 40, 36, "black", "#FFFFFF", ep(t, C["03.a"] + 2.6, 0.4))
    line(c, 960, 240, 960, 790, "#E6E6E2", ep(t, C["03.b"], 0.5), 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "o rótulo da tabela", 1370, 290, 34, "black", PURPLE, ab)
        x0, y0 = 1080, 360
        rrect(c, x0, y0, 580, 330, 18, "#FFFFFF", ab, shadow=True)
        heads = ["", "arroz", "feijão", "óleo"]
        for j, h in enumerate(heads):
            text(c, h, x0 + 80 + j * 140, y0 + 56, 26, "black", COL, ab)
        for i, nm in enumerate(["filial 1", "filial 2"]):
            text(c, nm, x0 + 80, y0 + 150 + i * 100, 26, "black", LIN, ab)
            for j in range(3):
                text(c, "•", x0 + 220 + j * 140, y0 + 150 + i * 100, 40, "black", LIGHT, ab)
        pill(c, "LINHA = QUEM", 1230, 740, LIN, size=26, a=ep(t, C["03.b"] + 1.2, 0.4), anchor="center")
        pill(c, "COLUNA = O QUÊ", 1520, 740, COL, size=26, a=ep(t, C["03.b"] + 2.2, 0.4), anchor="center")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "O CAIXA DO SUPERMERCADO", "QUANTIDADE × PREÇO, E SOMA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04.a"], 0.5)
    ab = ep(t, C["04.b"], 0.5)
    acc = ep(t, C["04.c"], 0.5)
    itens = [("arroz", "10 kg", "R$ 5", "R$ 50", ep(t, C["04.c"], 0.4)),
             ("feijão", "5 kg", "R$ 9", "R$ 45", ep(t, C["04.c"] + 1.6, 0.4)),
             ("óleo", "4 L", "R$ 8", "R$ 32", ep(t, C["04.c"] + 3.0, 0.4))]
    if a0 > 0:
        text(c, "NO CARRINHO", 470, 260, 28, "black", LIN, a0)
        for k, (nm, q) in enumerate((("arroz", "10 kg"), ("feijão", "5 kg"), ("óleo", "4 L"))):
            linha(c, [(q, LIN), ("  de " + nm, INK)], 470, 330 + k * 66, 40, a0)
    if ab > 0:
        text(c, "PREÇOS", 470, 560, 28, "black", COL, ab)
        linha(c, [("R$ 5 / kg", COL), ("   ", INK), ("R$ 9 / kg", COL), ("   ", INK), ("R$ 8 / L", COL)], 470, 620, 34, ab)
    cupom(c, 1000, 210, 640, itens, max(acc, ep(t, C["04.d"], 0.5)), ep(t, C["04.d"], 0.5))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pill(c, "o caixa SOMA TUDO num número só", 470, 740, GREEN, size=28, a=ad, anchor="center")


# ======================================================================
# bloco a — por que a regra é estranha
# ======================================================================

def b_estranha(c, t, C, B):
    head(c, t, B["start"], "ONDE ESTÃO AS MATRIZES?", "LINHA × COLUNA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "a COMPRA, deitada: uma LINHA", 470, 250, 30, "black", LIN, aa)
        matriz(c, [[10, 5, 4]], 470, 340, aa, cell=100, row=0)
        for k, nm in enumerate(("arroz", "feijão", "óleo")):
            text(c, nm, 370 + k * 100, 420, 20, "bold", GRAY, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        text(c, "os PREÇOS, em pé: uma COLUNA", 470, 500, 30, "black", COL, ab)
        matriz(c, [[5], [9], [8]], 470, 650, ab, cell=110, cellh=62, col=0)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, 900, 220, 760, 470, 24, "#F7F7F5", acc)
        text(c, "o cupom = LINHA × COLUNA", 1280, 270, 30, "black", PURPLE, acc)
        caixa_lxc(c, [10, 5, 4], [5, 9, 8], 1300, 500, ep(t, C["05.c"], 4.5), acc, size=46, dy=70)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        rrect(c, 900, 710, 760, 100, 20, "#FFFFFF", ad, shadow=True)
        tx = "casa com casa (soma)"
        x0 = 1040
        text(c, tx, x0, 772, 28, "black", GRAY, ad, align="left")
        strike(c, x0 - 6, 762, x0 + text_w(tx, "black", 28) + 6, 762, ad, RED, ad)
        text(c, "→  o CAIXA", 1450, 772, 30, "black", GREEN, ad, align="left")


# ======================================================================
# bloco b — a regra e o exemplo da seção 05
# ======================================================================

MA = [[1, 2, 3], [0, 1, 4]]
MB = [[2, 4], [1, 0], [0, 5]]
MC = [[4, 19], [1, 20]]
CONTAS = {(0, 0): [(1, 2), (2, 1), (3, 0)], (0, 1): [(1, 4), (2, 0), (3, 5)],
          (1, 0): [(0, 2), (1, 1), (4, 0)], (1, 1): [(0, 4), (1, 0), (4, 5)]}
AX, BX, CX_, MY = 470, 900, 1420, 420
# palavra que fala o resultado de cada casa (e qual ocorrência dela depois do cue)
RES_W = {"07.b": ("quatro", 1), "07.c": ("dezenove", 1), "08.a": ("um", 4), "08.b": ("vinte", 1)}


def _t_res(C, cue):
    w, k = RES_W[cue]
    return K.WT(C, cue.split(".")[0], w, k, depois=C[cue])


def b_regra(c, t, C, B):
    head_seq(c, t, C, [("06", "A REGRA", "PRODUTO DE MATRIZES", PURPLE), ("07", "VAMOS VER FUNCIONANDO", "A 1ª LINHA", PURPLE),
                       ("08", "A 2ª LINHA", "O ENDEREÇO DO RESULTADO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            rrect(c, 300, 230, 1320, 150, 24, mix("#FFFFFF", BLUE, 0.08), aa)
            text(c, "PRODUTO DE MATRIZES", W / 2, 285, 30, "black", BLUE, aa, tracking=2)
            text(c, "multiplicar uma matriz por outra:  A · B", W / 2, 350, 40, "black", INK, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            rrect(c, 300, 420, 1320, 220, 24, mix("#FFFFFF", PURPLE, 0.08), ab)
            linha(c, [("cᵢⱼ", RES), ("  =  ", INK), ("linha i de A", LIN), ("  ×  ", INK), ("coluna j de B", COL)],
                  W / 2, 500, 54, ab)
            text(c, "termo a termo (1º com 1º, 2º com 2º...) e SOMA", W / 2, 600, 32, "bold", INK2, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            regra(c, "LINHA VEZES COLUNA: o caixa, feito para cada casa", W / 2, 720, acc, 34)
        return
    a0 = ep(t, C["07"], 0.4)
    # qual casa está sendo calculada
    passos = [("07.b", (0, 0)), ("07.c", (0, 1)), ("08.a", (1, 0)), ("08.b", (1, 1))]
    atual, t_at, cue_at = None, None, None
    for cue, ij in passos:
        if t >= C[cue]:
            atual, t_at, cue_at = ij, C[cue], cue
    fim = t >= C["08.c"]
    hl = ep(t, t_at, 0.4) * (1 - ep(t, C["08.c"], 0.4)) if atual else 0
    matriz(c, MA, AX, MY, a0, cell=100, row=atual[0] if atual else None, hl=hl, rotulo="A", ordem="2 × 3")
    fmid(c, "·", 685, MY, 70, "black", GRAY, a0)
    matriz(c, MB, BX, MY, a0, cell=100, cellh=78, col=atual[1] if atual else None, hl=hl, rotulo="B", ordem="3 × 2")
    fmid(c, "=", 1130, MY, 70, "black", GRAY, a0)
    feitos = {}
    for cue, ij in passos:
        feitos[ij] = ep(t, _t_res(C, cue), 0.4)
    alf = {ij: max(0.0, v) for ij, v in feitos.items()}
    cores = {ij: RES for ij in feitos}
    Mq = [[MC[i][j] for j in range(2)] for i in range(2)]
    x0y = matriz(c, Mq, CX_, MY, a0, cell=130, cellh=100, alfas=alf, cores=cores, rotulo="C = A · B", ordem="2 × 2")
    # interrogações nas casas ainda não calculadas
    for (i, j), v in alf.items():
        if v < 1:
            x, y = casa(CX_, MY, MC, 130, i, j, 100)
            fmid(c, "?", x, y, 44, "black", LIGHT, a0 * (1 - v))
    if atual and not fim:
        i, j = atual
        pares = CONTAS[atual]
        partes = []
        sid_ = cue_at.split(".")[0]
        for k, (p, q) in enumerate(pares):
            ak = ep(t, K.WT(C, sid_, "vezes", k + 1, depois=t_at) - 0.4, 0.3)
            partes += [(str(p), mix("#FFFFFF", LIN, ak)), (" · ", mix("#FFFFFF", GRAY, ak)), (str(q), mix("#FFFFFF", COL, ak))]
            if k < 2:
                partes.append(("  +  ", mix("#FFFFFF", INK, ak)))
        s_ = sum(p * q for p, q in pares)
        ar = ep(t, _t_res(C, cue_at), 0.3)
        partes += [("  =  ", mix("#FFFFFF", INK, ar)), (str(s_), mix("#FFFFFF", RES, ar))]
        rrect(c, 330, 640, 1260, 120, 24, "#F7F7F5", a0)
        linha(c, [(f"c{'₁₂'[i]}{'₁₂'[j]}", RES), (f" = linha {i + 1} × coluna {j + 1}:   ", INK2)] + partes, W / 2, 700, 40,
              a0 * hl if hl > 0 else 0)
    if fim:
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            pill(c, "RESULTADO:  (4  19 / 1  20)", W / 2, 680, GREEN, size=30, a=acc, anchor="center")
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            x, y = casa(CX_, MY, MC, 130, 1, 0, 100)
            c.drawCircle(x, y, 46, paint(AMBER, ad, stroke=5))
            linha(c, [("c₂₁", RES), ("  =  ", INK), ("linha 2 de A", LIN), ("  ×  ", INK), ("coluna 1 de B", COL)],
                  W / 2, 770, 38, ad)


# ======================================================================
# bloco c — quando existe e que tamanho tem (o dominó)
# ======================================================================

def b_ordem(c, t, C, B):
    head_seq(c, t, C, [("09", "QUANDO EXISTE?", "A REGRA DO DOMINÓ", PURPLE), ("10", "POR QUE ENCAIXAR?", "QUANDO NÃO EXISTE", RED),
                       ("11", "ATALHO", "AS ORDENS ANTES DA CONTA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10", "11"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0:
            pergunta(c, "ORDEM = linhas × colunas", W / 2, 250, aa, BLUE, 34)
            linha(c, [("A: ", INK), ("2 × 3", INK)], 640, 340, 48, aa)
            linha(c, [("B: ", INK), ("3 × 2", INK)], 1280, 340, 48, aa)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            domino(c, (2, 3), (3, 2), W / 2, 500, ab, u=ep(t, C["09.b"] + 0.5, 1.2), res_a=ep(t, C["09.c"], 0.5))
            text(c, "DENTRO: iguais → encaixa", W / 2, 420, 28, "black", GREEN, ep(t, C["09.b"] + 2.0, 0.4))
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            regra(c, "FORA: o tamanho do resultado  →  2 × 2", W / 2, 760, acc, 34)
        return
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "cada QUANTIDADE da linha precisa do seu PREÇO na coluna", W / 2, 260, 32, "black", PURPLE, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            linha(c, [("3 × 2", INK), ("   ·   ", GRAY), ("3 × 2", INK)], W / 2, 350, 50, ab)
            domino(c, (3, 2), (3, 2), W / 2, 500, ab, u=ep(t, C["10.b"] + 0.6, 1.6))
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            # linha com 2 números x coluna com 3: sobra um preço
            matriz(c, [["q", "q"]], 560, 700, acc, cell=86, row=0)
            matriz(c, [["p"], ["p"], ["p"]], 820, 700, acc, cell=86, cellh=50, col=0)
            text(c, "sobra 1 preço SEM quantidade", 1260, 720, 34, "black", RED, acc)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        K.atalho(c, 300, 240, 1320, 420, "ATALHO · ANTES DE QUALQUER CONTA",
                 ["1. escreva as ordens lado a lado:  (m × n) · (n × p)",
                  "2. dentro DIFERENTE?  pare: não existe",
                  "3. dentro IGUAL?  risque os de dentro: (m × p) é o tamanho"], aa, 34)
    pill(c, "dez segundos", W / 2, 740, GREEN, size=30, a=ep(t, C["11.c"] + 2.0, 0.4), anchor="center")


# ======================================================================
# bloco d — só o elemento pedido
# ======================================================================

def b_pedido(c, t, C, B):
    head(c, t, B["start"], "UM NÚMERO SÓ?", "CALCULE SÓ A CASA PEDIDA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    rw = 1 if t >= C["12.c"] else None
    hl = ep(t, C["12.c"], 0.4)
    if aa > 0:
        dot = "•"
        matriz(c, [[dot] * 3, [dot] * 3], 470, 420, aa, cell=90, row=rw, hl=hl, rotulo="compras", ordem="filiais × itens")
        fmid(c, "·", 700, 420, 60, "black", GRAY, aa)
        matriz(c, [[dot] * 2, [dot] * 2, [dot] * 2], 900, 420, aa, cell=90, cellh=70, col=0 if rw else None, hl=hl,
               rotulo="preços", ordem="itens × fornecedores")
        fmid(c, "=", 1120, 420, 60, "black", GRAY, aa)
        a21 = ep(t, C["12.c"] + 1.0, 0.4)
        cores = {(1, 0): RES}
        Mr = [["?", "?"], ["?", "?"]]
        matriz(c, Mr, 1360, 420, aa, cell=110, cellh=90, cores={(i, j): (RES if (i, j) == (1, 0) else LIGHT)
                                                                   for i in range(2) for j in range(2)},
               alfas={(i, j): (1.0 if (i, j) != (1, 0) else 1 - a21) for i in range(2) for j in range(2)},
               rotulo="gastos", ordem="filiais × fornecedores")
        if a21 > 0:
            x, y = casa(1360, 420, Mr, 110, 1, 0, 90)
            fmid(c, "c₂₁", x, y, 40, "black", RES, a21)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        pergunta(c, "quanto a FILIAL 2 gasta no FORNECEDOR 1?", W / 2, 615, ab, PURPLE, 34)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        pill(c, "c₂₁ = linha 2 × coluna 1  ·  UMA conta, não quatro", W / 2, 688, GREEN, size=28, a=acc, anchor="center")
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        K.atalho(c, 460, 722, 1000, 110, "ATALHO", ["leia o endereço e calcule SÓ a casa pedida"], ad, 30)


# ======================================================================
# bloco e — matriz de ligações e A²
# ======================================================================

VOOS_E = [(1, 2), (1, 4), (2, 3), (3, 1), (4, 2)]
ME = [[0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]
VOOS_7 = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 1), (3, 4), (4, 1), (4, 2)]
M7 = [[0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 0, 0]]


def b_ligacoes(c, t, C, B):
    head_seq(c, t, C, [("13", "MATRIZ DE LIGAÇÕES", "1 = TEM VOO DIRETO", BLUE), ("14", "A² CONTA ROTAS", "COM UMA ESCALA", PURPLE),
                       ("15", "ATALHO", "CONTE OS ENCONTROS 1 COM 1", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14", "15"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        ac = ep(t, C["13.c"], 0.5)
        ea = {e: ep(t, C["13.c"] + 0.4 + k * 1.3, 0.4) for k, e in enumerate(VOOS_E)}
        voos(c, VOOS_E, 520, 500, aa, arestas_a=ea if ac > 0 else {e: 0 for e in VOOS_E})
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            rrect(c, 900, 230, 760, 130, 22, mix("#FFFFFF", BLUE, 0.08), ab)
            linha(c, [("aᵢⱼ = 1", BLUE), ("  se tem voo direto de i para j", INK)], 1280, 278, 32, ab)
            linha(c, [("aᵢⱼ = 0", GRAY), ("  se não tem", INK)], 1280, 330, 32, ab)
            # zeros cinza desde o início; cada 1 aparece junto com a sua seta
            cores = {(i, j): (BLUE if ME[i][j] else LIGHT) for i in range(4) for j in range(4)}
            alfas = {(i, j): (ea.get((i + 1, j + 1), 0) if ME[i][j] else 1.0) for i in range(4) for j in range(4)}
            matriz(c, ME, 1280, 590, ab, cell=78, size=40, cores=cores, alfas=alfas, rotulo="A",
                   ordem="de (linha) → para (coluna)")
        return
    if sid == "14":
        a0 = ep(t, C["14"], 0.4)
        hl = ep(t, C["14.b"], 0.5)
        voos(c, VOOS_E, 420, 470, a0, L=130, r=38, rotas=[(1, 2, 3)], rotas_a=[ep(t, C["14.d"], 0.5)],
             faltando=[(4, 3)], faltando_a=ep(t, K.WT(C, "14", "nao", 1, depois=C["14.d"]), 0.4))
        pill(c, "ESCALA: uma parada no meio", 420, 750, BLUE, size=26, a=a0, anchor="center")
        if hl > 0:
            matriz(c, ME, 900, 400, a0, cell=64, size=34, row=0, hl=hl, rotulo="A")
            fmid(c, "·", 1060, 400, 50, "black", GRAY, a0)
            matriz(c, ME, 1220, 400, a0, cell=64, size=34, col=2, hl=hl, rotulo="A")
            linha(c, [("(A²)₁₃", RES), (" = linha 1 × coluna 3", INK2)], 1450, 300, 30, hl, align="left")
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            pares = [(0, 0), (1, 1), (0, 0), (1, 0)]
            partes = []
            for k, (p, q) in enumerate(pares):
                on_ = p * q == 1
                ak = ep(t, K.WT(C, "14", "vezes", k + 1, depois=C["14.c"]) - 0.4, 0.3)
                cc = RES if on_ else INK
                partes += [(f"{p}·{q}", mix("#FFFFFF", cc, ak))]
                if k < 3:
                    partes.append(("  +  ", mix("#FFFFFF", GRAY, ak)))
            ar = ep(t, K.WT(C, "14", "uma", 1, depois=C["14.d"]), 0.4)
            partes += [("  =  ", mix("#FFFFFF", INK, ar)), ("1", mix("#FFFFFF", RES, ar))]
            rrect(c, 760, 590, 900, 110, 22, "#F7F7F5", acc)
            linha(c, partes, 1210, 645, 44, acc)
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            linha(c, [("1 → 2 → 3", RES), ("  ✓   ", RES), ("1 → 4 → 3", RED), ("  sem voo 4 → 3", RED)], 1210, 760, 30, ad)
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        text(c, "linha da PARTIDA", 600, 270, 30, "black", LIN, aa)
        g = ep(t, C["15.a"] + 0.6, 1.2)
        lin, col = [0, 1, 0, 1], [0, 1, 0, 0]
        for k in range(4):
            x = 450 + k * 100
            yl = lerp(330, 430, g)
            fmid(c, str(lin[k]), x, yl, 50, "black", LIN, aa)
            fmid(c, str(col[k]), x, 520, 50, "black", COL, aa)
            if lin[k] and col[k]:
                c.drawCircle(x, 475, 70 * ep(t, C["15.b"], 0.4) + 1, paint(GREEN, aa * ep(t, C["15.b"], 0.4), stroke=5))
        text(c, "coluna da CHEGADA", 600, 600, 30, "black", COL, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        K.atalho(c, 1000, 270, 640, 250, "ATALHO", ["conte os encontros 1 com 1", "cada encontro = 1 escala"], ab, 34)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        pill(c, "casa de A = voo DIRETO", 900, 720, BLUE, size=30, a=acc, anchor="center")
        pill(c, "casa de A² = rotas com UMA escala", 1300, 780, PURPLE, size=30, a=acc, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "DOMINÓ E LINHA × COLUNA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    i_ = 0 if t >= C["17.b"] and t < C["17.c"] else 1 if t >= C["17.c"] and t < C["17.d"] else None
    hl = 1.0 if i_ is not None else 0
    if aa > 0:
        matriz(c, [[2, 1], [0, 3]], 560, 360, aa, cell=100, row=i_, hl=hl)
        fmid(c, "·", 720, 360, 70, "black", GRAY, aa)
        matriz(c, [[1], [4]], 830, 360, aa, cell=100, col=0 if i_ is not None else None, hl=hl)
        fmid(c, "=", 960, 360, 70, "black", GRAY, aa)
        r0 = ep(t, K.WT(C, "17", "seis"), 0.4) if t >= C["17"] else 0
        r1 = ep(t, K.WT(C, "17", "doze"), 0.4) if t >= C["17"] else 0
        matriz(c, [[6], [12]], 1100, 360, aa, cell=110, cores={(0, 0): RES, (1, 0): RES}, alfas={(0, 0): r0, (1, 0): r1})
        for k, rr in enumerate((r0, r1)):
            fmid(c, "?", 1100, 360 - 50 + k * 110, 44, "black", LIGHT, aa * (1 - rr))
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0 and t < C["17"]:
        pergunta(c, "e qual é a ORDEM do resultado?", 1440, 360, ab, PURPLE, 30)
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, W / 2, 640)
        return
    a1 = ep(t, C["17.a"], 0.4)
    if a1 > 0:
        domino(c, (2, 2), (2, 1), 1480, 360, a1, u=ep(t, C["17.a"] + 0.4, 1.0), size=40, tw=170, th=84,
               res_a=ep(t, C["17.a"] + 2.6, 0.4))
    for k, (cue, s_) in enumerate((("17.b", [("2·1", LIN), ("  +  ", INK), ("1·4", COL), ("  =  ", INK), ("6", RES)]),
                                   ("17.c", [("0·1", LIN), ("  +  ", INK), ("3·4", COL), ("  =  ", INK), ("12", RES)]))):
        ak = ep(t, C[cue], 0.4)
        if ak > 0:
            linha(c, [(f"linha {k + 1}:  ", INK2)] + s_, 700, 600 + k * 80, 42, ak)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        conferido(c, "a coluna (6 / 12), ordem 2 × 1", 1150, 690, ad, True, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Linha da primeira vezes coluna da segunda, e soma.",
          "Os números de dentro encaixam; os de fora dão o tamanho.",
          "cᵢⱼ é a linha i com a coluna j."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Multiplicar posição com posição, como na soma",
          "na SOMA é casa com casa: (1 2 / 3 4) e (5 6 / 7 8) dariam (5 12 / 21 32)",
          "o produto é LINHA × COLUNA: (19 22 / 43 50)"),
         ("Achar que (2 × 3) · (2 × 3) existe", "as duas têm o MESMO tamanho, como a soma exige",
          "o dominó: dentro, 3 e 2 não encaixam → NÃO EXISTE")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=28, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


def _fonte(c, t, C, a0, sid_fim):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[sid_fim], 0.3)),
         align="left")


ALTS3 = [("A", "uma matriz 2 × 4.", "parou no 1º produto", RED), ("B", "uma matriz 3 × 3.", "os de dentro do 1º", RED),
         ("C", "uma matriz 4 × 4.", "os de dentro do 2º", RED),
         ("D", "inexistente, pois as ordens não são compatíveis.", "", RED),
         ("E", "uma matriz 2 × 2.", "", GREEN)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "QUANDO O PRODUTO EXISTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [("Um programa de planilhas guarda três tabelas como matrizes: A, com 2 linhas e 3 colunas; B, com "
                           "3 linhas e 4 colunas; e C, com 4 linhas e 2 colunas. Um usuário pede o produto A · B · C, "
                           "nessa ordem. O resultado será", INK)], a0, 240, 28)
    _fonte(c, t, C, a0, "22")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 40, C["22.ok"], "E", cues_in, cues_x, gap=30)
    if t >= C["22"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["22"], 0.4))
        a1 = ep(t, C["22.a"], 0.4)
        a2 = ep(t, C["22.b"], 0.4)
        if a1 > 0 and a2 < 1:
            text(c, "1º  A · B", 540, y0 + 50, 26, "black", PURPLE, a1 * (1 - a2))
            domino(c, (2, 3), (3, 4), 540, y0 + 150, a1 * (1 - a2), u=ep(t, C["22.a"] + 0.4, 1.0), size=36, tw=160,
                   th=76, res_a=ep(t, K.WT(C, "22", "quatro", 2, depois=C["22.a"]), 0.4))
        if a2 > 0:
            pill(c, "1º  A · B  =  2 × 4", 540, y0 + 44, PURPLE, size=24, a=a2, anchor="center")
            domino(c, (2, 4), (4, 2), 540, y0 + 150, a2, u=ep(t, C["22.b"] + 0.4, 1.0), size=36, tw=160, th=76,
                   res_a=ep(t, C["22.ok"] - 1.2, 0.4))
        axd = ep(t, C["23.xd"], 0.4)
        if axd > 0:
            pill(c, "D: basta os VIZINHOS encaixarem", 540, 800, RED, size=22, a=axd, anchor="center")


QM = [[10, 5, 4], [8, 6, 2]]
PM = [[5, 6], [9, 7], [8, 9]]
CQ = [[127, 131], [110, 108]]
ALTS2 = [("A", "215.", "mistura fornecedores: PROIBIDO", RED), ("B", "235.", "", GREEN),
         ("C", "237.", "as duas no X", RED), ("D", "239.", "as duas no Y", RED), ("E", "241.", "as piores opções", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "PRODUTO COMO CUSTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    res = t >= C["25"]
    at = a0 * (1 - ep(t, C["25"], 0.4))
    if at > 0:
        y = _enunciado(c, [("Duas filiais de um restaurante compram arroz (kg), feijão (kg) e óleo (L). As quantidades estão "
                            "na matriz Q (linha 1: filial 1; linha 2: filial 2), e os preços unitários de dois "
                            "fornecedores, X e Y, estão nas colunas da matriz P, em reais:", INK)], at, 236, 24)
        ab = ep(t, C["24.b"], 0.4)
        matriz(c, QM, 380, y + 70, at, cell=58, size=30, rotulo=None)
        fmid(c, "Q =", 230, y + 70, 30, "black", INK, at)
        fmid(c, "e  P =", 580, y + 70, 28, "black", INK, at * ab)
        matriz(c, PM, 740, y + 70, at * ab, cell=64, cellh=42, size=28)
        _enunciado(c, [("Cada filial faz a compra completa em um único fornecedor e escolhe o que lhe sai mais barato. "
                        "O gasto total das duas filiais, em reais, é", INK)], at * ep(t, C["24.c"], 0.4), y + 170, 24)
    _fonte(c, t, C, a0, "25")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["26.ok"], "B", cues_in, cues_x, gap=34)
    if not res:
        pause_timer(c, t, C["24.end"] - 1.9, 540, 790)
        return
    a1 = ep(t, C["25"], 0.4)
    _painel(c, 230, a1)
    domino(c, (2, 3), (3, 2), 540, 300, a1, u=ep(t, C["25"] + 0.5, 0.8), size=30, tw=130, th=62,
           res_a=ep(t, C["25"] + 3.0, 0.4))
    aa = ep(t, C["25.a"], 0.4)
    if aa > 0:
        text(c, "fornecedor X", 640, 486, 20, "black", COL, aa)
        text(c, "fornecedor Y", 800, 486, 20, "black", COL, aa)
        text(c, "filial 1", 330, 545, 24, "black", LIN, aa)
        text(c, "filial 2", 330, 635, 24, "black", LIN, aa)
    vis = {(0, 0): ep(t, K.WT(C, "25", "sete", 1, depois=C["25.b"]), 0.4),
           (0, 1): ep(t, K.WT(C, "25", "trinta", 1, depois=C["25.b"]), 0.4),
           (1, 0): ep(t, K.WT(C, "25", "dez", 1, depois=C["25.c"]), 0.4),
           (1, 1): ep(t, K.WT(C, "25", "oito", 2, depois=C["25.c"]), 0.4)}
    escolha = ep(t, C["26.a"], 0.4)
    cores = {ij: (RES if escolha > 0.5 and ij in ((0, 0), (1, 1)) else INK) for ij in vis}
    if aa > 0:
        text(c, "C = Q · P", 330, 470, 26, "black", INK, aa)
    matriz(c, CQ, 720, 590, aa, cell=160, cellh=90, size=46, alfas=vis, cores=cores)
    if escolha > 0:
        for (i, j) in ((0, 0), (1, 1)):
            x, y = casa(720, 590, CQ, 160, i, j, 90)
            c.drawCircle(x, y, 52, paint(GREEN, escolha, stroke=5))
    ab2 = ep(t, C["26.b"], 0.4)
    if ab2 > 0:
        linha(c, [("127 + 108 = ", INK), ("235", RES)], 540, 770, 40, ab2)


ALTS7 = [("A", "0.", "leu o voo direto a₁₄", RED), ("B", "1.", "rotas com DUAS escalas", RED), ("C", "2.", "", GREEN),
         ("D", "3.", "somou 1 escala + 2 escalas", RED), ("E", "4.", "somou a linha 1 de A²", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · VOCÊ FAZ", "CONTAR ROTAS COM A²", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    res = t >= C["28"]
    at = a0 * (1 - ep(t, C["28"], 0.4))
    if at > 0:
        y = _enunciado(c, [("Uma companhia aérea atende quatro cidades. Na matriz A, aᵢⱼ = 1 se há voo direto da cidade i "
                            "para a cidade j e aᵢⱼ = 0 caso contrário:", INK)], at, 236, 24)
        matriz(c, M7, 540, y + 104, at, cell=48, size=28)
        fmid(c, "A =", 400, y + 104, 30, "black", INK, at)
        _enunciado(c, [("O elemento da linha 1 e coluna 4 de A² = A · A indica o número de maneiras de ir da cidade 1 à "
                        "cidade 4 com exatamente uma escala. Esse número é", INK)], at * ep(t, C["27.b"], 0.4), y + 250, 24)
    _fonte(c, t, C, a0, "28")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 250, 680, 44, C["28.ok"], "C", cues_in, cues_x, gap=34)
    if not res:
        pause_timer(c, t, C["27.end"] - 1.9, 540, 790)
        return
    a1 = ep(t, C["28"], 0.4)
    _painel(c, 230, a1)
    matriz(c, M7, 360, 340, a1, cell=48, size=26, row=0, hl=a1, rotulo=None)
    fmid(c, "·", 490, 340, 44, "black", GRAY, a1)
    matriz(c, M7, 620, 340, a1, cell=48, size=26, col=3, hl=a1)
    linha(c, [("(A²)₁₄", RES)], 820, 340, 30, a1)
    aa = ep(t, C["28.a"], 0.4)
    if aa > 0:
        linha(c, [("0·0", INK), (" + ", GRAY), ("1·1", RES), (" + ", GRAY), ("1·1", RES), (" + ", GRAY), ("0·0", INK),
                  (" = ", GRAY), ("2", RES)], 540, 480, 36, aa)
    rb, rc = ep(t, C["28.b"], 0.5), ep(t, C["28.c"], 0.5)
    voos(c, VOOS_7, 540, 660, a1 * ep(t, C["28.b"] - 0.6, 0.4), L=90, r=28, size=26,
         rotas=[(1, 2, 4), (1, 3, 4)], rotas_a=[rb * (1 - rc * 0.0), rc], cor_rota=GREEN)
    if rb > 0:
        pill(c, "1 → 2 → 4", 780, 620, GREEN, size=24, a=rb, anchor="center")
    if rc > 0:
        pill(c, "1 → 3 → 4", 780, 690, GREEN, size=24, a=rc, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AB = BA? E A INVERSA", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        linha(c, [("2 × 3 = 3 × 2", INK)], 560, 360, 60, aa)
        conferido(c, "com números", 420, 450, aa, True, 34)
        linha(c, [("A · B  =  B · A", PURPLE)], 1360, 360, 60, ep(t, C["31.a"] + 2.2, 0.4))
        fmid(c, "?", 1660, 360, 90, "black", AMBER, ep(t, C["31.a"] + 2.6, 0.4))
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        linha(c, [("÷", AMBER), ("  desfaz o  ", INK), ("×", INK)], 560, 600, 56, ab)
        linha(c, [("e com matrizes?", PURPLE)], 1360, 600, 52, ab)
    pill(c, "ep. 4 · o que muda em relação aos números e a matriz inversa", W / 2, 780, PURPLE, size=28,
         a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você sabia que o cupom do mercado é um produto de matrizes?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, estranha=b_estranha, regra=b_regra,
              ordem=b_ordem, pedido=b_pedido, ligacoes=b_ligacoes, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q3=b_q3, q2=b_q2, q7=b_q7, ponte=b_ponte, cta=b_cta)
