"""Visual — Progressão Geométrica, Episódio 2: propriedades que poupam conta e a soma finita (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: arvore() (a corrente de mensagens: 3 → 9 → 27 … por dia, com os contadores "neste dia" e "ao todo"),
deducao() (as linhas S e q·S deslizando uma sobre a outra; as parcelas iguais se apagam e sobram a última e a primeira),
tabuleiro() (o xadrez com 1, 2, 4, 8 … grãos), fila_pg() (fichas com arcos ligando vizinhos ou equidistantes),
linha() (texto com cor por trecho, mantém o espaço de milhar).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum047", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pg_ep2_propriedades_soma.mp4"
CARD_R = K.CARD_R
TEAL = "#0E9384"


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


def fmt(n):
    return f"{n:,}".replace(",", " ")


def ficha(c, s, cx, cy, a, col=INK, w=78, h=66, size=32, fill="#FFFFFF"):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 12, fill, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 12, 12), paint(col, a, stroke=3))
    text_mid(c, s, cx, cy, size, "black", col, a)


def ficha_m(c, s, cx, cy, a, col=INK, w=150, h=80, size=34, fill="#FFFFFF"):
    """ficha com expressão matemática (expr)"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, fill, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14), paint(col, a, stroke=3))
    K.mdraw(c, s, cx, cy, size, col, a, align="center")


def arco(c, x0, x1, y, alt, col, a, sw=5, label=None, size=26, cima=True):
    """arco ligando duas fichas, com rótulo no topo (cima=False: arco por baixo)"""
    if a <= 0:
        return
    s_ = -1 if cima else 1
    p = skia.Path()
    p.moveTo(x0, y)
    p.cubicTo(x0, y + s_ * alt, x1, y + s_ * alt, x1, y)
    c.drawPath(p, paint(col, a, stroke=sw))
    if label:
        pill(c, label, (x0 + x1) / 2, y + s_ * alt * 0.75, col, size=size, a=a, anchor="center", bounds=(0, 1920))


def fila(c, valores, x0, y, a, passo=118, col=BLUE, size=30, w=90):
    xs = [x0 + k * passo for k in range(len(valores))]
    for v, x in zip(valores, xs):
        ficha(c, str(v), x, y, a, col, w=w, size=size)
    return xs


def arvore(c, t, t0, a, x0=200, y0=250, larg=900, dy=96, dias=6.0, rotulo=True):
    """a corrente: no dia k recebem 3^k pessoas. Linhas 1–3 com bolinhas e ligações; 4–6 como faixas densas"""
    if a <= 0:
        return
    cx = x0 + larg / 2
    pos = {}
    for k in range(1, 7):
        f = clamp(dias - (k - 1))
        if f <= 0:
            break
        y = y0 + (k - 1) * dy
        n = 3 ** k
        ak = a * f
        if k <= 3:
            wk = larg * (0.30, 0.62, 1.0)[k - 1]
            xs = [cx - wk / 2 + (j + 0.5) * wk / n for j in range(n)]
            pos[k] = xs
            r = (18, 12, 7)[k - 1]
            for j, x in enumerate(xs):
                if k > 1:
                    px = pos[k - 1][j // 3]
                    line(c, px, y - dy + (18, 12, 7)[k - 2], x, y - r, mix(INK2, "#FFFFFF", 0.45), ak, 2)
                c.drawCircle(x, y, r, paint(BLUE, ak))
        else:
            wk = larg
            rrect(c, cx - wk / 2, y - 16, wk, 32, 16, mix("#FFFFFF", BLUE, 0.25 + 0.15 * (k - 4)), ak)
            for j in range(90):
                c.drawCircle(cx - wk / 2 + 8 + j * (wk - 16) / 89, y, 3.2, paint(BLUE, ak * 0.8))
        if rotulo:
            ftext(c, f"dia {k}", x0 - 30, y + 10, 24, "bold", INK2, ak, align="right")
            pill(c, fmt(n), x0 + larg + 30, y, BLUE, size=24, a=ak, bounds=(0, 1920))


def contadores(c, x, y, dia, a, total_final=False):
    """dois mostradores: NESTE DIA (3^dia) e AO TODO (soma)"""
    if a <= 0:
        return
    d = max(1, min(6, int(dia)))
    neste = 3 ** d
    todo = sum(3 ** k for k in range(1, d + 1))
    for k, (rot, val, col) in enumerate((("NESTE DIA", neste, "#FFD166"), ("AO TODO", todo, "#7CE0B0"))):
        yy = y + k * 150
        rrect(c, x, yy, 420, 128, 22, "#10141A", a)
        text(c, rot, x + 30, yy + 40, 22, "black", "#9AA3B2", a, align="left")
        ftext(c, fmt(val), x + 390, yy + 104, 58, "black", col, a, align="right")


PARC_S = ["a₁", "a₁q", "a₁q^2", "…", "a₁q^{n-1}"]
PARC_QS = ["a₁q", "a₁q^2", "a₁q^3", "…", "a₁q^n"]


def deducao(c, t, a, u, apaga, x0=420, ytop=420, passo=230):
    """linha S (azul) em cima e linha q·S (roxo) embaixo; u = 0..1 desliza q·S um degrau para a direita; apaga = 0..1 some
    com as parcelas iguais"""
    if a <= 0:
        return
    text(c, "S", x0 - 150, ytop + 12, 50, "black", BLUE, a)
    text(c, "q·S", x0 - 150, ytop + 162, 50, "black", PURPLE, a)
    for k, s_ in enumerate(PARC_S):
        x = x0 + k * passo
        fade = 1.0 if k == 0 else 1 - 0.85 * apaga
        if s_ == "…":
            text_mid(c, "…", x, ytop, 54, "black", INK2, a * fade)
        else:
            ficha_m(c, s_, x, ytop, a * fade, BLUE, w=190, h=84, size=34)
    for k, s_ in enumerate(PARC_QS):
        x = x0 + (k + u) * passo
        fade = 1.0 if k == len(PARC_QS) - 1 else 1 - 0.85 * apaga
        y = ytop + 150
        if s_ == "…":
            text_mid(c, "…", x, y, 54, "black", INK2, a * fade)
        else:
            ficha_m(c, s_, x, y, a * fade, PURPLE, w=190, h=84, size=34)
    if apaga > 0:
        for k in range(1, 5):
            x = x0 + k * passo
            strike(c, x - 70, ytop + 75, x + 70, ytop + 75, apaga, GREEN, 1)


def tabuleiro(c, cx, cy, lado, a, n_marcadas=64):
    """xadrez 8 × 8 com os grãos 1, 2, 4, 8 … nas primeiras casas e 2⁶³ na última"""
    if a <= 0:
        return
    s = lado / 8
    x0, y0 = cx - lado / 2, cy - lado / 2
    for i in range(8):
        for j in range(8):
            col = "#E9DCC3" if (i + j) % 2 == 0 else "#B98A5E"
            rrect(c, x0 + j * s, y0 + i * s, s, s, 0, col, a)
    rot = ["1", "2", "4", "8", "16", "32", "64", "128"]
    for j, r in enumerate(rot):
        if j < n_marcadas:
            text_mid(c, r, x0 + j * s + s / 2, y0 + 7 * s + s / 2, s * 0.34, "black", INK, a)
    if n_marcadas >= 64:
        K.mdraw(c, "2^{63}", x0 + 7 * s + s / 2, y0 + s / 2, s * 0.34, PURPLE, a, align="center")
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, lado, lado), paint(INK, a, stroke=4))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROGRESSÃO GEOMÉTRICA · EPISÓDIO 2", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    n = 1 + int(7 * clamp((t - C["01.a"]) / 3.5))
    tabuleiro(c, 520, 560, 560, aa, n if t < C["01.b"] else 64)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 960, 300, 760, 210, 30, "#10141A", ab, shadow=True)
        text(c, "NA 64ª CASA, A SOMA PASSA DE", 1340, 360, 26, "black", "#9AA3B2", ab)
        text_mid(c, "18 quintilhões", 1340, 440, 76, "black", "#FFD166", ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        pill(c, "centenas de vezes a produção mundial de trigo de um ano", 1340, 580, AMBER, size=24, a=acc, anchor="center",
             bounds=(0, 1920))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1340, 720, ad, "A FÓRMULA CABE NUMA LINHA", PURPLE, -3, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "PROGRESSÃO GEOMÉTRICA · EP. 2", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "2º episódio da série de PROGRESSÃO GEOMÉTRICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "SOMAR QUALQUER PG", "finita, em uma linha", PURPLE),
             ("02.b", "TRÊS NÚMEROS EM PG", "em poucas linhas", BLUE)]
    for k, (cue, tit, sub_, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 300, 330, 600, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 300, 330, 600, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 44, "black", col, ak)
        text(c, sub_, x, 625, 30, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "episódio 1 · a máquina ×q", "aₙ = a₁·q^{n-1}"),
             ("03.b", "série de Progressão aritmética", "x-r x x+r"),
             ("03.c", "série de Equação do 2º grau", "Bhaskara → as raízes de ax² + bx + c = 0")]
    for k, (cue, rot, s_) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 190 + d
        rrect(c, 260, y - 75, 1400, 150, 24, "#FFFFFF", a, shadow=True)
        pill(c, rot, 300, y - 75, BLUE, size=22, a=a, bounds=(0, 1920))
        if k == 0:
            K.expr(c, s_, W / 2, y + 8, 60, a)
        elif k == 1:
            K.expr(c, "x-r ·  x  · x+r", W / 2, y + 8, 56, a)
        else:
            text_mid(c, s_, W / 2, y + 8, 40, "black", INK, a)


# ======================================================================
# bloco a — média geométrica
# ======================================================================

def b_media(c, t, C, B):
    head_seq(c, t, C, [("04", "O TERMO DO MEIO", "NA PA × NA PG", BLUE), ("05", "VAMOS TESTAR", "(4, x, 25)", PURPLE)])
    card(c, *CARD_R)
    if t < C["05"]:
        aa = ep(t, C["04.a"], 0.5)
        if aa > 0:
            pill(c, "a PG é a PA com a SOMA trocada por MULTIPLICAÇÃO", W / 2, 230, PURPLE, size=30, a=aa, anchor="center")
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            K.boxed(c, 220, 300, 700, 330, BLUE, ab, 0.06)
            text(c, "PA", 570, 360, 40, "black", BLUE, ab)
            K.expr(c, "b = (a+c)/2", 570, 480, 70, ab)
            pill(c, "soma os vizinhos ÷ 2", 570, 590, INK2, size=24, a=ab, anchor="center")
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            K.boxed(c, 1000, 300, 700, 330, PURPLE, acc, 0.06)
            text(c, "PG", 1350, 360, 40, "black", PURPLE, acc)
            K.expr(c, "b^2 = a·c", 1350, 480, 76, acc)
            pill(c, "multiplica os vizinhos", 1350, 590, INK2, size=24, a=acc, anchor="center")
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            rrect(c, 260, 680, 1400, 120, 22, mix("#FFFFFF", BLUE, 0.10), ad)
            linha(c, [("MÉDIA GEOMÉTRICA: ", BLUE), ("o número que, ao quadrado, dá o produto dos vizinhos", INK)],
                  W / 2, 740, 30, ad)
        return
    aa = ep(t, C["05.a"], 0.5)
    xs = [700, 960, 1220]
    if aa > 0:
        ficha(c, "4", xs[0], 330, aa, BLUE, w=130, h=100, size=54)
        ficha(c, "x", xs[1], 330, aa, AMBER, w=130, h=100, size=54)
        ficha(c, "25", xs[2], 330, aa, BLUE, w=130, h=100, size=54)
        pill(c, "termos positivos", W / 2, 420, INK2, size=22, a=aa, anchor="center")
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        arco(c, xs[0], xs[2], 280, 150, PURPLE, ab, 5, "4 · 25 = 100", 26)
        K.expr(c, "x^2 = 4·25 = 100", W / 2, 520, 60, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        linha(c, [("x = ", INK), ("10", GREEN)], W / 2, 630, 72, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        linha(c, [("4 ", BLUE), ("×2,5 → ", PURPLE), ("10 ", GREEN), ("×2,5 → ", PURPLE), ("25", BLUE)], W / 2, 760, 46, ad)


# ======================================================================
# bloco b — notação simétrica
# ======================================================================

def b_simetrica(c, t, C, B):
    head_seq(c, t, C, [("06", "PRODUTO DE TRÊS EM PG", "NOTAÇÃO SIMÉTRICA", BLUE), ("07", "POR QUE AJUDA?", "O q SOME", PURPLE)])
    card(c, *CARD_R)
    xs = [620, 960, 1300]
    if t < C["07"]:
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            text(c, "PA", 300, 320, 36, "black", BLUE, aa)
            for x, s_ in zip(xs, ("x-r", "x", "x+r")):
                ficha_m(c, s_, x, 310, aa, BLUE, w=220, h=96, size=46)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            text(c, "PG", 300, 520, 36, "black", PURPLE, ab)
            for x, s_ in zip(xs, ("x/q", "x", "x·q")):
                ficha_m(c, s_, x, 510, ab, PURPLE, w=220, h=120, size=46)
            pill(c, "÷ q", 790, 440, PURPLE, size=24, a=ab, anchor="center")
            pill(c, "× q", 1130, 440, PURPLE, size=24, a=ab, anchor="center")
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 680, 1400, 120, 22, mix("#FFFFFF", BLUE, 0.10), acc)
            linha(c, [("NOTAÇÃO SIMÉTRICA: ", BLUE), ("x no centro, a razão saindo igual para os dois lados", INK)],
                  W / 2, 740, 30, acc)
        return
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        K.expr(c, "x/q · x · x·q", W / 2, 300, 70, aa)
        ab = ep(t, C["07.b"], 0.5)
        strike(c, 790, 335, 850, 290, ab, RED, 1)
        strike(c, 1130, 300, 1190, 255, ab, RED, 1)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("= ", INK), ("x³", PURPLE)], W / 2, 430, 70, ab)
        pill(c, "o q some", 1340, 430, RED, size=26, a=ab, anchor="center")
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        linha(c, [("x³ = 64  →  x = ", INK), ("4", GREEN)], W / 2, 550, 56, acc)
        pill(c, "4 · 4 · 4 = 64", W / 2, 625, INK2, size=24, a=ep(t, C["07.c"] + 2.0, 0.4), anchor="center")
    ad = ep(t, C["07.d"], 0.5)
    K.atalho(c, 360, 680, 1200, 130, "ATALHO", ["o termo do meio é a RAIZ CÚBICA do produto"], ad, 36)


# ======================================================================
# bloco c — equidistantes
# ======================================================================

def b_equidist(c, t, C, B):
    head(c, t, B["start"], "NUMA PG MAIS COMPRIDA", "TERMOS EQUIDISTANTES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 205, 1400, 90, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "EQUIDISTANTES: à mesma distância das pontas", W / 2, 262, 34, "black", BLUE, aa)
    ab = ep(t, C["08.b"], 0.5)
    xs = fila(c, [1, 3, 5, 7, 9, 11], 560, 430, ab, passo=150, col=BLUE, size=32, w=96)
    if ab > 0:
        text(c, "PA", 380, 445, 40, "black", BLUE, ab)
        arco(c, xs[0], xs[5], 395, 120, BLUE, ab, 4, None)
        arco(c, xs[1], xs[4], 395, 75, BLUE, ab, 4, None)
        arco(c, xs[2], xs[3], 395, 40, BLUE, ab, 4, None)
        pill(c, "cada par SOMA 12", 1520, 340, BLUE, size=26, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["08.c"], 0.5)
    xs2 = fila(c, [1, 2, 4, 8, 16, 32], 560, 650, acc, passo=150, col=PURPLE, size=32, w=96)
    if acc > 0:
        text(c, "PG", 380, 665, 40, "black", PURPLE, acc)
        for k, (i, j, h) in enumerate(((0, 5, 120), (1, 4, 75), (2, 3, 40))):
            arco(c, xs2[i], xs2[j], 690, h, PURPLE, acc * ep(t, C["08.c"] + 2.0 + k * 1.0, 0.4), 4, None, cima=False)
        pill(c, "cada par: PRODUTO 32", 1520, 790, PURPLE, size=26, a=ep(t, C["08.c"] + 4.5, 0.4), anchor="center",
             bounds=(0, 1920))
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        regra(c, "soma da PA  →  PRODUTO na PG", W / 2, 540, ad, 30)


# ======================================================================
# bloco d — a soma finita (dedução) · atalho
# ======================================================================

def b_soma(c, t, C, B):
    head_seq(c, t, C, [("09", "SOMAR SEM SOMAR UM POR UM?", "A SOMA FINITA", BLUE),
                       ("10", "E SE SUBTRAIR?", "SOBRAM DUAS PARCELAS", PURPLE)])
    card(c, *CARD_R)
    if t < C["10"]:
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 210, 1400, 110, 24, mix("#FFFFFF", BLUE, 0.10), aa)
            linha(c, [("Sₙ", BLUE), (" = soma do 1º até o termo de posição n", INK)], W / 2, 265, 38, aa)
        ab = ep(t, C["09.b"], 0.5)
        acc = ep(t, C["09.c"], 0.5)
        deducao(c, t, ab, 0, 0)
        if acc <= 0 and ab > 0:
            # esconde a linha q·S até o "multiplique por q"
            rrect(c, 230, 500, 1460, 140, 0, "#FFFFFF", ab)
        if acc > 0:
            pill(c, "× q: cada parcela SOBE UM DEGRAU", W / 2, 690, PURPLE, size=28, a=acc, anchor="center")
        return
    u = ep(t, C["10.a"], 1.2)
    ap = ep(t, C["10.b"], 0.8)
    deducao(c, t, 1.0, u, ap)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0 and t < C["10.d"]:
        K.expr(c, "q·S - S = a₁q^n - a₁", W / 2, 700, 56, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 650, 1200, 170, 26, mix("#FFFFFF", PURPLE, 0.10), ad)
        K.expr(c, "Sₙ = a₁·(q^n-1)/{q-1}", W / 2, 735, 64, ad)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        pill(c, "q ≠ 1   ·   se q = 1:  Sₙ = n · a₁", W / 2, 228, AMBER, size=28, a=ae, anchor="center")


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "SEM DECORAR", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 160, "ATALHO · A SOMA DA PG",
             [("m", "Sₙ = (próximo-1º)/{q-1}")], aa, 44)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        ficha_m(c, "a₁q^n", 760, 520, ab, PURPLE, w=200, h=90, size=40)
        text_mid(c, "−", 960, 520, 60, "black", INK, ab)
        ficha_m(c, "a₁", 1160, 520, ab, BLUE, w=200, h=90, size=40)
        pill(c, "o que sobrou na subtração", W / 2, 610, INK2, size=24, a=ab, anchor="center")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 460, 680, 1000, 120, 22, mix("#FFFFFF", GREEN, 0.12), acc)
        linha(c, [("razão 2: divide por 1 → ", INK), ("próximo − primeiro", GREEN)], W / 2, 740, 36, acc)


# ======================================================================
# bloco e — a corrente · termo ou soma
# ======================================================================

def b_corrente(c, t, C, B):
    head(c, t, B["start"], "QUANTOS RECEBEM?", "A CORRENTE DE MENSAGENS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    dias = 1 + 5 * clamp((t - C["12.b"]) / 6.0) if t >= C["12.b"] else 1
    arvore(c, t, C["12.a"], aa, x0=260, y0=260, larg=860, dy=100, dias=dias)
    contadores(c, 1300, 260, dias, aa)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        selo(c, 1510, 590, acc, "SÓ O 6º DIA: 729", AMBER, -3, 28)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        rrect(c, 1240, 640, 470, 170, 22, "#FFFFFF", ad, shadow=True)
        K.expr(c, "3·(3^6-1)/2", 1475, 700, 40, ad)
        linha(c, [("= 3 · 728 ÷ 2 = ", INK), ("1 092", GREEN)], 1475, 775, 30, ep(t, C["12.d"] + 3.0, 0.4))


def b_termosoma(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TERMO OU SOMA?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 360, 210, 1200, 130, "ATALHO · ANTES DE QUALQUER CONTA", ["escreva: TERMO OU SOMA?"], aa, 40)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        for k, (tit, sub_, col) in enumerate((("“NO 6º DIA”", "termo · 729", BLUE), ("“AO TODO”", "soma · 1 092", PURPLE))):
            x = 640 + k * 640
            rrect(c, x - 270, 390, 540, 170, 24, "#FFFFFF", ab, shadow=True)
            text(c, tit, x, 455, 40, "black", col, ab)
            text(c, sub_, x, 520, 30, "bold", INK2, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 610, 1200, 190, 24, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("liste: 3 + 9 + 27 = ", INK), ("39", GREEN)], W / 2, 660, 40, acc)
        a2 = ep(t, C["13.c"] + 4.0, 0.4)
        if a2 > 0:
            K.expr(c, "3·(3^3-1)/2 = 3·26/2 = 39", W / 2, 745, 40, a2)
            check_icon(c, 1500, 745, 20, a2, GREEN)


# ======================================================================
# bloco f — o tabuleiro
# ======================================================================

def b_tabuleiro(c, t, C, B):
    head(c, t, B["start"], "E O TABULEIRO DO GANCHO?", "RAZÃO 2 · 64 CASAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    tabuleiro(c, 520, 540, 520, aa)
    if aa > 0:
        linha(c, [("a₁ = 1 · q = 2 · n = 64", INK)], 1300, 260, 40, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 960, 320, 700, 170, 24, "#FFFFFF", ab, shadow=True)
        K.expr(c, "S₆₄ = 1·(2^{64}-1)/{2-1}", 1310, 405, 48, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        K.expr(c, "= 2^{64}-1", 1310, 560, 64, acc, cores={1: PURPLE})
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 960, 640, 700, 160, 24, "#10141A", ad)
        K.expr(c, "≈ 1,8·10^{19}", 1310, 700, 56, ad, cores={0: "#FFD166", 1: "#FFD166"})
        text(c, "grãos · 18 quintilhões", 1310, 775, 26, "black", "#9AA3B2", ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "TERMO OU SOMA?", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 120, 24, "#FFFFFF", aa, shadow=True)
        linha(c, [("2 + 6 + 18 + …", BLUE), ("   ·   6 termos   ·   ", INK2), ("S₆ = ?", AMBER)], W / 2, 270, 52, aa)
    if t < C["16"]:
        pause_timer(c, t, C["15.end"] - 1.9, 960, 560)
        return
    ab = ep(t, C["16.a"], 0.5)
    if ab > 0:
        rrect(c, 260, 380, 520, 230, 24, "#FFFFFF", ab, shadow=True)
        text(c, "SOMA · A RAZÃO", 520, 425, 26, "black", AMBER, ab)
        linha(c, [("q = 6 ÷ 2 = ", INK), ("3", PURPLE)], 520, 520, 46, ab)
    acc = ep(t, C["16.b"], 0.5)
    if acc > 0:
        rrect(c, 820, 380, 840, 230, 24, "#FFFFFF", acc, shadow=True)
        text(c, "A FÓRMULA", 1240, 425, 26, "black", PURPLE, acc)
        K.expr(c, "S₆ = 2·(3^6-1)/{3-1}", 1240, 500, 44, acc)
        linha(c, [("= 2 · 728 ÷ 2 = ", INK), ("728", GREEN)], 1240, 575, 40, ep(t, C["16.b"] + 4.0, 0.4))
    ad = ep(t, C["16.c"], 0.5)
    if ad > 0:
        rrect(c, 260, 650, 1400, 150, 24, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("2 + 6 + 18 + 54 + 162 + 486 = ", INK), ("728", GREEN)], W / 2, 725, 46, ad)
        check_icon(c, 1600, 725, 20, ep(t, C["16.c"] + 4.5, 0.4), GREEN)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Na PG, o termo do meio ao quadrado é o produto dos vizinhos.",
          "Três em PG: x/q, x e x·q.",
          "Soma finita: a₁ vezes (qⁿ − 1), dividido por (q − 1)."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Total da corrente = 3⁶ = 729", "3⁶ é o número que aparece no 6º dia",
          "esse é SÓ O ÚLTIMO DIA: o total soma os seis dias = 1 092"),
         ("Esquecer o ÷ (q − 1): 2 · 728 = 1 456", "o começo da fórmula está todo ali",
          "na subtração sobrou (q − 1) · S: divida → 728"),
         ("Fórmula da PA na PG: (2 + 486) · 6 ÷ 2 = 1 464", "na série de PA essa conta sempre funcionou",
          "ela vale quando se cresce SOMANDO; a PG cresce MULTIPLICANDO")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _questao(c, t, C, sid_q, sid_r, sid_x, alts, okL, xs, txt, pausa=True, ok_sid=None):
    a0 = ep(t, C[f"{sid_q}.a"], 0.4)
    yend = _enunciado(c, [(txt, INK)], a0, 236, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[sid_r], 0.3)),
         align="left")
    cues_in = {L: C[f"{sid_q}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in xs}
    K.alternativas(c, t, C, alts, 1000, 260, 680, 38, C[f"{ok_sid or sid_r}.ok"], okL, cues_in, cues_x, gap=34)
    if t < C[sid_r]:
        if pausa:
            pause_timer(c, t, C[f"{sid_q}.end"] - 1.9, 540, yend + 120)
        return None
    y0 = 236 - 30
    _painel(c, y0, ep(t, C[sid_r], 0.4))
    return y0


ALTS4 = [("A", "18", "linear: 3 por dia × 6", RED), ("B", "729", "só o 6º dia", RED), ("C", "1 092", "", GREEN),
         ("D", "2 184", "sem ÷ (q − 1)", RED), ("E", "2 187", "3⁷: o 7º dia", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "A CORRENTE DE MENSAGENS", BLUE)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "21", "22", "23", ALTS4, "C", "ABDE",
                  "No primeiro dia de uma campanha, 3 pessoas recebem uma mensagem. Cada pessoa que recebe a mensagem a "
                  "repassa, no dia seguinte, a exatamente 3 pessoas que ainda não a tinham recebido, e o processo continua "
                  "assim. O total de pessoas que terão recebido a mensagem ao fim do 6º dia é")
    if y0 is None:
        return
    aa = ep(t, C["22.a"], 0.4)
    if aa > 0:
        linha(c, [("“total” → ", INK), ("SOMA", PURPLE)], 540, y0 + 60, 36, aa)
    ab = ep(t, C["22.b"], 0.4)
    if ab > 0:
        linha(c, [("3 · 9 · 27 · 81 · 243 · 729", BLUE)], 540, y0 + 150, 30, ab)
        pill(c, "PG de razão 3", 540, y0 + 210, PURPLE, size=22, a=ab, anchor="center")
    acc = ep(t, C["22.c"], 0.4)
    if acc > 0:
        K.expr(c, "3·(3^6-1)/2", 540, y0 + 300, 40, acc)
        linha(c, [("= 3 · 728 ÷ 2 = ", INK), ("1 092", GREEN)], 540, y0 + 390, 40, ep(t, C["22.c"] + 2.4, 0.4))


ALTS5 = [("A", "4", "o mais novo", RED), ("B", "6", "o do meio", RED), ("C", "9", "", GREEN),
         ("D", "12", "razão 2: 3 + 6 + 12 = 21", RED), ("E", "13", "19 − 6", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "AS IDADES EM PG", GREEN)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "24", "25", "27", ALTS5, "C", "ABDE",
                  "As idades de três irmãos, em anos, são números inteiros que formam uma progressão geométrica crescente. "
                  "O produto das três idades é 216 e a soma é 19. A idade do irmão mais velho é", ok_sid="26")
    if y0 is None:
        return
    if t < C["26"]:
        aa = ep(t, C["25.a"], 0.4)
        if aa > 0:
            K.expr(c, "x/q · x · x·q", 540, y0 + 70, 40, aa)
            linha(c, [("x³ = 216  →  x = ", INK), ("6", PURPLE)], 540, y0 + 150, 36, aa)
        ab = ep(t, C["25.b"], 0.4)
        if ab > 0:
            K.expr(c, "6/q + 6 + 6q = 19", 540, y0 + 240, 38, ab)
            K.expr(c, "6q^2 - 13q + 6 = 0", 540, y0 + 325, 40, ep(t, C["25.b"] + 4.0, 0.4), cores={0: PURPLE})
        acc = ep(t, C["25.c"], 0.4)
        if acc > 0:
            linha(c, [("Δ = 169 − 144 = 25", INK)], 540, y0 + 410, 32, acc)
            K.expr(c, "q = 3/2  ou  q = 2/3", 540, y0 + 500, 38, ep(t, C["25.c"] + 3.5, 0.4))
        return
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        linha(c, [("crescente → ", INK), ("q = 3/2", PURPLE)], 540, y0 + 80, 38, aa)
    ab = ep(t, C["26.b"], 0.4)
    if ab > 0:
        for k, v in enumerate((4, 6, 9)):
            ficha(c, str(v), 400 + k * 140, y0 + 210, ab, GREEN if v == 9 else BLUE, w=110, h=90, size=48)
        pill(c, "÷ 3/2", 470, y0 + 140, PURPLE, size=20, a=ab, anchor="center")
        pill(c, "× 3/2", 610, y0 + 140, PURPLE, size=20, a=ab, anchor="center")
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        linha(c, [("4 + 6 + 9 = 19", INK)], 540, y0 + 340, 34, acc)
        linha(c, [("4 · 6 · 9 = 216", INK)], 540, y0 + 410, 34, acc)
        check_icon(c, 790, y0 + 375, 20, acc, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A SOMA INFINITA", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        x0, y0, L = 660, 250, 520
        rrect(c, x0, y0, L, L, 0, "#FFFFFF", aa, shadow=True)
        # metade, metade do que sobrou… (6 pinceladas)
        x, y, w, h = x0, y0, L, L
        n = 1 + int(5 * clamp((t - C["29.a"]) / 4.0))
        for k in range(n):
            col = (PURPLE, BLUE, GREEN, AMBER, PURPLE, BLUE)[k]
            if k % 2 == 0:
                rrect(c, x, y, w / 2, h, 0, col, aa * 0.75)
                x += w / 2; w /= 2
            else:
                rrect(c, x, y, w, h / 2, 0, col, aa * 0.75)
                y += h / 2; h /= 2
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, L, L), paint(INK, aa, stroke=4))
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        selo(c, 1500, 470, ab, "ÁREA INFINITA?", AMBER, -4, 34)
    pill(c, "ep. 3 · a soma infinita", W / 2, 830, PURPLE, size=32, a=ep(t, C["29.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Quantos grãos você chutaria para o tabuleiro?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, media=b_media, simetrica=b_simetrica,
              equidist=b_equidist, soma=b_soma, atalho=b_atalho, corrente=b_corrente, termosoma=b_termosoma,
              tabuleiro=b_tabuleiro, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q5=b_q5,
              ponte=b_ponte, cta=b_cta)
