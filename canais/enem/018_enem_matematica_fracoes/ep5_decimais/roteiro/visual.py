"""Visual — Frações, Decimais e Dízimas, Episódio 5: Operações com decimais sem calculadora (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (expr com frações empilhadas, alternativas, erro_cards...).
Peças deste episódio: notas e moedas (decimal = DINHEIRO), contas armadas com a vírgula alinhada (numcol),
a vírgula que pula casas (hop) e a pilha de moedas de 12 centavos até R$ 4,80.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum018", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr, expr, expr_w = K.fr, K.expr, K.expr_w
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep5_decimais.mp4"
CARD_R = K.CARD_R
OURO = "#E2B04A"
PRATA = "#C3CAD3"
NOTA = "#6F9BC9"


# ======================================================================
# peças: dinheiro, conta armada, vírgula que pula
# ======================================================================

def moeda(c, cx, cy, r, s, a, col=OURO, sub=None):
    if a <= 0:
        return
    c.drawCircle(cx, cy + 5, r, paint("#000000", 0.12 * a))
    c.drawCircle(cx, cy, r, paint(mix(col, "#000000", 0.22), a))
    c.drawCircle(cx, cy, r * 0.84, paint(col, a))
    text_mid(c, s, cx, cy - (r * 0.12 if sub else 0), r * 0.62, "black", mix(col, "#000000", 0.62), a)
    if sub:
        text_mid(c, sub, cx, cy + r * 0.42, r * 0.26, "black", mix(col, "#000000", 0.55), a)


def nota(c, x, y, val, a, w=230, h=112, col=NOTA):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, col, a, shadow=True)
    rrect(c, x + 9, y + 9, w - 18, h - 18, 7, mix(col, "#FFFFFF", 0.28), a)
    c.drawCircle(x + w * 0.24, y + h / 2, h * 0.26, paint(mix(col, "#FFFFFF", 0.55), a))
    text_mid(c, val, x + w * 0.62, y + h / 2, h * 0.36, "black", "#FFFFFF", a)


def moeda_lado(c, cx, cy, a, col=OURO, rx=62, ry=15):
    """moeda vista de lado (para a pilha)"""
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeLTRB(cx - rx, cy - ry + 7, cx + rx, cy + ry + 7), paint(mix(col, "#000000", 0.30), a))
    c.drawOval(skia.Rect.MakeLTRB(cx - rx, cy - ry, cx + rx, cy + ry), paint(col, a))
    c.drawOval(skia.Rect.MakeLTRB(cx - rx * 0.78, cy - ry * 0.7, cx + rx * 0.78, cy + ry * 0.7),
               paint(mix(col, "#FFFFFF", 0.25), a))


def reais(v):
    return f"R$ {v:.2f}".replace(".", ",")


def numcol(c, s, xv, cy, size, color=None, a=1.0, cols=None, alphas=None, comma=0.0, gap=None):
    """escreve s com a vírgula em xv e os algarismos em colunas fixas (contas armadas).
    cols = {índice em s: cor} · alphas = {índice: alpha} · comma = brilho da vírgula (0..1). Devolve {índice: x do centro}."""
    color = INK if color is None else color
    cw = size * 0.64
    gap = size * 0.2 if gap is None else gap
    ip, dp = (s.split(",") + [""])[:2] if "," in s else (s, None)
    by = cy + size * 0.36
    xs = {}
    for k, ch in enumerate(ip):
        xs[k] = xv - gap - (len(ip) - k - 0.5) * cw
    if dp is not None:
        xs[len(ip)] = xv
        for j in range(len(dp)):
            xs[len(ip) + 1 + j] = xv + gap + (j + 0.5) * cw
    if a <= 0:
        return xs
    for i, ch in enumerate(s):
        aa = a * (alphas.get(i, 1.0) if alphas else 1.0)
        if aa <= 0:
            continue
        col = (cols or {}).get(i, color)
        if ch == ",":
            if comma > 0:
                c.drawCircle(xv, by - size * 0.06, size * 0.26, paint(PURPLE, 0.18 * comma * aa))
            text(c, ",", xv, by, size, "black", mix(col, PURPLE, comma), aa)
        else:
            text(c, ch, xs[i], by, size, "black", col, aa)
    return xs


def hop(c, digs, base, b0, b1, m, cx, cy, size, a, zero_a=0.0, col=None, comma_a=1.0, marks=True):
    """a vírgula pulando casas: digs em colunas fixas; a vírgula fica numa fronteira (0..len) e vai de b0 a b1 aos pulinhos.
    base = índices dos algarismos originais (os outros são zeros de complemento, em âmbar, com alpha zero_a)."""
    if a <= 0:
        return
    col = INK if col is None else col
    cw = size * 0.78
    n = len(digs)
    x0 = cx - n * cw / 2
    by = cy + size * 0.36
    for i, ch in enumerate(digs):
        on = i in base
        aa = a if on else a * zero_a
        if aa > 0:
            text(c, ch, x0 + (i + 0.5) * cw, by, size, "black", col if on else AMBER, aa)
    steps = abs(b1 - b0)
    sg = 1 if b1 >= b0 else -1
    seg = clamp(m) * steps
    k = min(int(seg), steps - 1) if steps else 0
    f = ease_io(clamp(seg - k)) if steps else 0
    p = b0 + sg * (k + f)
    jump = math.sin(math.pi * f) * size * 0.42 if steps and 0 < f < 1 else 0
    xc = x0 + p * cw
    if marks and steps:
        for j in range(steps):
            on = clamp(seg - j)
            if on <= 0:
                continue
            xa, xb = x0 + (b0 + sg * j) * cw, x0 + (b0 + sg * (j + 1)) * cw
            # arco tracejado do pulo + número da casa
            pth = skia.Path()
            pth.moveTo(xa, by + size * 0.16)
            pth.quadTo((xa + xb) / 2, by + size * 0.62, xb, by + size * 0.16)
            c.drawPath(pth, paint(PURPLE, 0.55 * a * on, stroke=4))
            badge_num(c, j + 1, (xa + xb) / 2, by + size * 0.62, a * on, size * 0.15, bg=PURPLE)
    c.drawCircle(xc, by - size * 0.06 - jump, size * 0.24, paint(PURPLE, 0.16 * a * comma_a))
    text(c, ",", xc, by - jump, size, "black", PURPLE, a * comma_a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DECIMAIS SEM CALCULADORA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "4,8 ÷ 0,12 = 40", W / 2, 330, 120, aa, cores={4: GREEN})
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        boxed(c, 560, 470, 800, 130, AMBER, ab, 0.12)
        fmid(c, "40  >  4,8  ?!", W / 2, 535, 64, "black", INK, ab)
        text(c, "o resultado ficou MAIOR que o número dividido", W / 2, 650, 36, "black", AMBER, ab)
    ac = ep(t, C["01.c"], 0.4)
    ad = ep(t, C["01.d"], 0.4)
    text(c, "Errei?", 520, 780, 60, "black", RED, ac * (1 - 0.6 * ad))
    selo(c, 800, 760, ad, "NÃO!", GREEN, -6, 44)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        pill(c, "isso salva questões inteiras do ENEM", 1330, 765, GREEN, size=30, a=ae, anchor="center",
             bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "somar, multiplicar e dividir decimais", "sem calculadora"),
            ("02.b", "sem medo do resultado", "nem quando ele cresce")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")
    ac = ep(t, C["02.c"], 0.5)
    nota(c, 1180, 640, "R$ 2", ac)
    moeda(c, 1500, 700, 62, "50", ac * ep(t, C["02.c"] + 0.3, 0.3), OURO, "centavos")
    moeda(c, 1640, 700, 52, "12", ac * ep(t, C["02.c"] + 0.5, 0.3), PRATA, "centavos")
    pill(c, "o segredo: DINHEIRO", 700, 700, BLUE, size=36, a=ac, anchor="center", bounds=(0, 1920))


# ======================================================================
# pré-requisitos: decimal = dinheiro
# ======================================================================

def b_dinheiro(c, t, C, B):
    frame(c, t, B["start"], "UM NÚMERO COM VÍRGULA", "NÚMERO DECIMAL", BLUE)
    a0 = ep(t, C["03.t"], 0.5)
    nota(c, 240, 250, "R$ 2", a0)
    moeda(c, 560, 306, 64, "50", ep(t, C["03.t"] + 0.5, 0.4), OURO, "centavos")
    text(c, "dois reais e cinquenta centavos", 400, 470, 32, "bold", INK2, a0)
    aa = ep(t, C["03.a"], 0.5)
    glow = ep(t, C["03.c"], 0.5)
    xv = 1240
    xs = numcol(c, "2,50", xv, 400, 190, INK, aa, comma=glow)
    ab = ep(t, C["03.b"], 0.5)
    pill(c, "NÚMERO DECIMAL = número com vírgula", 960, 640, BLUE, size=34, a=ab * (1 - glow), anchor="center",
         bounds=(0, 1920))
    if glow > 0:
        text(c, "VÍRGULA", xv, 210, 30, "black", PURPLE, glow, tracking=2)
        arrow(c, xv, 225, xv, 300, PURPLE, glow, 5, 16, progress=glow)
        pill(c, "VÍRGULA = separa o inteiro dos pedaços menores", 960, 640, BLUE, size=32, a=glow, anchor="center",
             bounds=(0, 1920))
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        xl0, xl1 = xs[0] - 60, xv - 30
        xr0, xr1 = xv + 30, xs[3] + 60
        for x_0, x_1, lab, col in ((xl0, xl1, "reais", GREEN), (xr0, xr1, "centavos", AMBER)):
            line(c, x_0, 520, x_1, 520, col, ad, 6, progress=ad)
            line(c, x_0, 505, x_0, 520, col, ad, 6)
            line(c, x_1, 505, x_1, 520, col, ad, 6)
            text(c, lab, (x_0 + x_1) / 2, 570, 38, "black", col, ad)
        text(c, "no dinheiro: reais , centavos", 960, 790, 36, "black", INK2, ad)


def b_casas(c, t, C, B):
    frame(c, t, B["start"], "DEPOIS DA VÍRGULA", "CASAS DECIMAIS", BLUE)
    a0 = ep(t, C["04.t"], 0.5)
    pill(c, "CASA DECIMAL = cada posição depois da vírgula", W / 2, 215, BLUE, size=32, a=a0, anchor="center",
         bounds=(0, 1920))
    cols_ = [("04.a", "0,1", "DÉCIMO", "10", "dez centavos", "um décimo do real", OURO),
             ("04.b", "0,01", "CENTÉSIMO", "1", "um centavo", "", PRATA),
             ("04.c", "0,001", "MILÉSIMO", "", "um décimo de centavo", "moeda disso não existe", None)]
    for k, (cue, num, nome, mv, s1, s2, mc) in enumerate(cols_):
        a = ep(t, C[cue], 0.5)
        x = 420 + k * 540
        if a <= 0:
            continue
        rrect(c, x - 240, 280, 480, 520, 24, mix("#FFFFFF", BLUE, 0.06), a)
        text(c, f"{k + 1}ª casa", x, 330, 28, "black", GRAY, a, tracking=1)
        dp = len(num) - 2
        numcol(c, num, x - 40 * (dp - 1), 410, 84, INK, a, cols={len(num) - 1: BLUE})
        text(c, nome, x, 520, 40, "black", BLUE, a)
        if mc:
            moeda(c, x, 620, 58, mv, a, mc, "centavos")
        else:
            c.drawCircle(x, 620, 58, paint(LIGHT, a, stroke=4))
            fmid(c, "?", x, 620, 50, "black", LIGHT, a)
        text(c, s1, x, 720, 30, "black", INK2, a)
        if s2:
            text(c, s2, x, 762, 26, "bold", AMBER if not mc else GRAY, a)


# ======================================================================
# bloco A — somar e subtrair
# ======================================================================

def soma_armada(c, t, C, xv, top, a, zero_a, glow, cues_res, res_a_comma, labels=0.0):
    """2,50 + 0,75 = 3,25 armada; cues_res = instantes de cada algarismo do resultado (da direita para a esquerda)"""
    size = 104
    lh = 126
    if a <= 0:
        return
    if labels > 0:
        text(c, "reais", xv - 70, top - 70, 28, "black", GREEN, labels)
        text(c, "centavos", xv + 85, top - 70, 28, "black", AMBER, labels)
    if glow > 0:
        line(c, xv, top - 50, xv, top + 2 * lh + 70, PURPLE, glow * 0.6 * a, 3, dash=(10, 10))
    numcol(c, "2,50", xv, top, size, INK, a, cols={3: AMBER}, alphas={3: zero_a}, comma=glow)
    numcol(c, "0,75", xv, top + lh, size, INK, a, comma=glow)
    text(c, "+", xv - 230, top + lh + size * 0.36, size, "black", INK2, a)
    line(c, xv - 260, top + lh + 80, xv + 200, top + lh + 80, INK, a, 6)
    ra = [ep(t, q, 0.4) for q in cues_res]      # unidades de centavo, dezena de centavo, real
    xs = numcol(c, "3,25", xv, top + 2 * lh + 10, size, GREEN, a, alphas={3: ra[0], 2: ra[1], 0: ra[2], 1: res_a_comma},
                comma=glow * res_a_comma)
    # o "vai um" em cima do real
    v1 = ra[1] * (1 - ra[2] * 0.4) * (1 - labels)
    if v1 > 0:
        text(c, "1", xs[0], top - 52, 44, "black", RED, a * v1)


def b_somar(c, t, C, B):
    head_seq(c, t, C, [("05", "R$ 2,50 + R$ 0,75", "COM QUANTO FICA?", BLUE),
                       ("06", "NO CADERNO", "VÍRGULA EMBAIXO DE VÍRGULA", PURPLE),
                       ("07", "POR QUE ALINHAR?", "REAIS COM REAIS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06", "07"])
    if sid == "05":
        a0 = ep(t, C["05.t"], 0.5)
        nota(c, 220, 230, "R$ 2", a0)
        moeda(c, 560, 286, 60, "50", ep(t, C["05.t"] + 0.4, 0.4), OURO, "centavos")
        fmid(c, "+", 750, 286, 80, "black", INK2, ep(t, C["05.t"] + 1.2, 0.4))
        moeda(c, 920, 286, 60, "50", ep(t, C["05.t"] + 1.5, 0.4), OURO, "centavos")
        moeda(c, 1070, 286, 50, "25", ep(t, C["05.t"] + 1.7, 0.4), PRATA, "centavos")
        text(c, "R$ 2,50", 420, 420, 38, "black", INK2, a0)
        text(c, "R$ 0,75", 995, 420, 38, "black", INK2, ep(t, C["05.t"] + 1.5, 0.4))
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            boxed(c, 1250, 225, 440, 200, AMBER, aa, 0.10)
            text(c, "só os centavos", 1470, 280, 28, "black", AMBER, aa)
            fmid(c, "50 + 75 = 125", 1470, 350, 52, "black", INK, aa)
        fmid(c, "125 centavos = R$ 1,25", W / 2, 560, 60, "black", INK, ep(t, C["05.b"], 0.5))
        ac = ep(t, C["05.c"], 0.5)
        fmid(c, "R$ 2 + R$ 1,25 = R$ 3,25", W / 2, 720, 64, "black", GREEN, ac)
        return
    m07 = ep(t, C["07"], 0.8) if sid == "07" else 0.0
    xv = lerp(W / 2 + 20, 560, m07)
    a0 = ep(t, C["06"], 0.5)
    glow = ep(t, C["06.a"], 0.5)
    zero_a = ep(t, C["06.b"], 0.5)
    c0 = C["06.c"]
    soma_armada(c, t, C, xv, 290, a0, zero_a, glow, [c0 + 0.3, c0 + 1.6, c0 + 3.0], ep(t, C["06.d"], 0.5),
                labels=ep(t, C["07.a"], 0.5) if sid == "07" else 0.0)
    if sid == "06":
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            arrow(c, xv + 420, 290, xv + 230, 290, AMBER, ab, 5, 16, progress=ab)
            para(c, "complete com zero: 2,5 vira 2,50", xv + 440, 270, 30, "black", AMBER, ab, 330)
        ac = ep(t, C["06.c"], 0.5) * (1 - ep(t, C["06.d"], 0.4))
        if ac > 0:
            para(c, "some da direita para a esquerda", xv + 440, 560, 30, "black", INK2, ac, 330)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            arrow(c, xv + 420, 560, xv + 230, 560, GREEN, ad, 5, 16, progress=ad)
            para(c, "desça a vírgula no mesmo lugar", xv + 440, 540, 30, "black", GREEN, ad, 330)
        return
    # 07: soma à esquerda, subtração à direita
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        xv2 = 1320
        top = 290
        size, lh = 104, 126
        z = ep(t, C["07.c"], 0.5)
        glow2 = z
        if glow2 > 0:
            line(c, xv2, top - 50, xv2, top + 2 * lh + 70, PURPLE, glow2 * 0.6 * ab, 3, dash=(10, 10))
        # 5 → 5,00
        numcol(c, "5,00", xv2, top, size, INK, ab, cols={2: AMBER, 3: AMBER}, alphas={1: z, 2: z, 3: z}, comma=glow2)
        numcol(c, "2,75", xv2, top + lh, size, INK, ab, comma=glow2)
        text(c, "−", xv2 - 230, top + lh + size * 0.36, size, "black", INK2, ab)
        line(c, xv2 - 260, top + lh + 80, xv2 + 200, top + lh + 80, INK, ab, 6)
        r = ep(t, C["07.c"] + 2.2, 0.5)
        numcol(c, "2,25", xv2, top + 2 * lh + 10, size, GREEN, ab * r, comma=glow2)
        text(c, "R$ 5,00 − R$ 2,75", xv2, 200, 30, "black", INK2, ab)
    aa = ep(t, C["07.a"], 0.5) * (1 - ab)
    if aa > 0:
        para(c, "reais com reais, centavos com centavos", 1000, 420, 44, "black", PURPLE, aa, 640)


# ======================================================================
# bloco B — multiplicar
# ======================================================================

def b_multiplicar(c, t, C, B):
    head_seq(c, t, C, [("08", "0,3 × 0,04", "MULTIPLICAR DECIMAIS", PURPLE),
                       ("09", "3 CASAS NO RESULTADO", "ZERO NA FRENTE", PURPLE),
                       ("10", "ATALHO", "SOME AS CASAS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10"])
    if sid == "08":
        a0 = ep(t, C["08.t"], 0.5)
        hb = ep(t, C["08.b"], 0.5)
        numcol(c, "0,3", 600, 300, 120, INK, a0, cols={2: mix(INK, AMBER, hb)})
        fmid(c, "×", 830, 300, 100, "black", INK2, a0)
        numcol(c, "0,04", 1080, 300, 120, INK, a0, cols={2: mix(INK, AMBER, hb), 3: mix(INK, AMBER, hb)})
        fmid(c, "= ?", 1420, 300, 100, "black", GRAY, a0)
        if hb > 0:
            for x_0, x_1, lab in ((640, 720, "1 casa"), (1120, 1290, "2 casas")):
                line(c, x_0, 390, x_1, 390, AMBER, hb, 6, progress=hb)
                chip(c, lab, (x_0 + x_1) / 2, 440, AMBER, ep(t, C["08.b"] + 0.4 + (0.9 if lab == "2 casas" else 0), 0.4), 30)
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            text(c, "1º · sem vírgula", 520, 560, 30, "black", GRAY, aa)
            fmid(c, "3 × 4 = 12", 520, 640, 76, "black", INK, aa)
        ac = ep(t, C["08.c"], 0.5)
        if ac > 0:
            text(c, "2º · conte as casas", 1300, 560, 30, "black", GRAY, ac)
            fmid(c, "1 + 2 = 3 casas", 1300, 640, 70, "black", PURPLE, ac)
        regra(c, "Multiplicar: some as casas decimais", W / 2, 775, ep(t, C["08.c"] + 1.4, 0.5), 32)
        return
    if sid == "09":
        a0 = ep(t, C["09.t"], 0.5)
        m = ep(t, C["09.a"], 2.4)
        done = ep(t, C["09.b"], 0.5)
        hop(c, "0012", {2, 3}, 4, 1, m, W / 2, 290, 120, a0, zero_a=ep(t, C["09.a"] + 2.2, 0.4),
            col=mix(INK, GREEN, done), comma_a=ep(t, C["09.t"] + 0.8, 0.4))
        text(c, "conte 3 casas da direita para a esquerda", W / 2, 200, 28, "black", GRAY, a0 * (1 - done))
        pill(c, "0,3 × 0,04 = 0,012", W / 2, 490, GREEN, size=40, a=done,
             anchor="center", bounds=(0, 1920))
        ac = ep(t, C["09.c"], 0.5)
        text(c, "E POR QUE FUNCIONA?", W / 2, 560, 30, "black", BLUE, ac * (1 - ep(t, C["09.d"], 0.4)), tracking=2)
        ad = ep(t, C["09.d"], 0.5)
        ae = ep(t, C["09.e"], 0.5)
        ad *= 1 - ae
        if ad > 0:
            expr(c, "0,3 = 3/10", 560, 600, 56, ad, cores={2: BLUE})
            text(c, "três décimos", 560, 720, 28, "black", BLUE, ad)
            expr(c, "0,04 = 4/100", 1360, 600, 56, ep(t, C["09.d"] + 1.6, 0.5), cores={2: BLUE})
            text(c, "quatro centésimos", 1360, 720, 28, "black", BLUE, ep(t, C["09.d"] + 1.6, 0.5))
        if ae > 0:
            expr(c, "3/10 · 4/100 = 12/1000 = 0,012", W / 2, 680, 62, ae, cores={4: GREEN, 6: GREEN})
            text(c, "doze milésimos", W / 2, 800, 28, "black", GREEN, ae)
        return
    # 10: atalho
    steps = [("10.a", "multiplique sem vírgula", INK), ("10.b", "some as casas dos dois números", INK),
             ("10.c", "conte as casas da DIREITA para a ESQUERDA", INK), ("10.d", "faltou algarismo? zero na frente", AMBER)]
    boxed(c, 200, 200, 820, 600, GREEN, ep(t, C["10.t"], 0.5), 0.06)
    text(c, "ATALHO", 610, 255, 26, "black", GREEN, ep(t, C["10.t"], 0.5), tracking=3)
    for k, (cue, s, col) in enumerate(steps):
        a, d = rise(t, C[cue])
        y = 350 + k * 120 + d
        badge_num(c, k + 1, 270, y - 14, a, 28, bg=GREEN if col == INK else AMBER)
        para(c, s, 320, y, 36, "black", col, a, 660, 42)
    ae = ep(t, C["10.a"], 0.5)
    fmid(c, "0,3 × 0,04", 1370, 290, 64, "black", INK2, ae)
    fmid(c, "12", 1370, 400, 64, "black", INK, ep(t, C["10.a"] + 0.6, 0.4))
    hop(c, "0012", {2, 3}, 4, 1, ep(t, C["10.c"], 2.0), 1370, 580, 100, ep(t, C["10.b"], 0.5),
        zero_a=ep(t, C["10.d"], 0.5))
    text(c, "1 + 2 = 3 casas", 1370, 480, 30, "black", PURPLE, ep(t, C["10.b"], 0.5))


# ======================================================================
# bloco C — dividir
# ======================================================================

def b_dividir(c, t, C, B):
    head_seq(c, t, C, [("11", "4,8 ÷ 0,12", "QUANTAS MOEDAS CABEM?", BLUE),
                       ("12", "SEM CALCULADORA", "IGUALE AS CASAS", PURPLE),
                       ("13", "A DIVISÃO FICOU INTEIRA", "480 ÷ 12", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        fmid(c, "4,8 ÷ 0,12", 500, 260, 80, "black", INK, aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            para(c, "quantas moedas de 12 centavos cabem em R$ 4,80?", 220, 370, 40, "black", BLUE, ab, 600, 50)
            moeda(c, 810, 260, 54, "12", ab, PRATA, "centavos")
        ac = ep(t, C["11.c"], 0.4)
        dur = max(1.5, min(3.2, C["11.d"] - C["11.c"] - 1.0))
        n = int(round(clamp((t - C["11.c"] - 0.6) / dur) * 40))
        if ac > 0:
            for i in range(40):
                if i >= n:
                    break
                s_, l_ = divmod(i, 10)
                drop = 1 - ep(t, C["11.c"] + 0.6 + i * dur / 40, 0.25)
                moeda_lado(c, 1080 + s_ * 170, 770 - l_ * 30 - drop * 80, ac * (1 - drop * 0.6), PRATA)
            for s_ in range(4):
                if n > s_ * 10:
                    text(c, f"{min(10, n - s_ * 10)}", 1080 + s_ * 170, 830, 26, "black", GRAY, ac)
            fin = 1.0 if n >= 40 else 0.0
            fmid(c, f"{n} moedas", 500, 600, 72, "black", GREEN if fin else INK, ac)
            fmid(c, f"= {reais(n * 0.12)}", 500, 700, 60, "black", GREEN if fin else INK2, ac)
        pill(c, "por isso o resultado CRESCE", 500, 790, GREEN, size=32, a=ep(t, C["11.d"], 0.5), anchor="center",
             bounds=(0, 1920))
        return
    if sid == "12":
        xv = 640
        aa = ep(t, C["12.a"], 0.5)
        z = ep(t, C["12.a"] + 1.2, 0.5)
        sem = ep(t, C["12.b"], 0.6)
        a0 = ep(t, C["12"], 0.5)
        numcol(c, "4,80", xv, 300, 120, INK, a0, cols={3: AMBER}, alphas={3: z, 1: 1 - sem}, comma=aa * (1 - sem))
        numcol(c, "0,12", xv, 460, 120, INK, a0, alphas={1: 1 - sem}, comma=aa * (1 - sem))
        text(c, "÷", xv - 300, 460 + 43, 110, "black", INK2, a0)
        for y in (300, 460):
            chip(c, "2 casas", xv + 330, y, AMBER, aa * (1 - sem), 30)
        if sem > 0:
            arrow(c, 900, 380, 1080, 380, PURPLE, sem, 6, 18, progress=sem)
            fmid(c, "480 ÷ 12", 1360, 380, 96, "black", PURPLE, sem)
            text(c, "tire as vírgulas dos dois", 1360, 490, 30, "black", PURPLE, sem)
        ac = ep(t, C["12.c"], 0.5)
        if ac > 0:
            boxed(c, 300, 620, 1320, 160, BLUE, ac, 0.08)
            moeda(c, 400, 700, 52, "12", ac, PRATA, "centavos")
            fmid(c, "480 centavos ÷ 12 centavos", 1000, 700, 52, "black", BLUE, ac)
        return
    # 13: conta armada pelo método da chave
    size = 96
    cw = 60
    x0 = 560
    by = 360
    a0 = ep(t, C["13.a"], 0.5)
    hb = ep(t, C["13.b"], 0.5)
    hc = ep(t, C["13.c"], 0.5)
    if hb > 0:
        rrect(c, x0 - 34, by - 82, cw * 2 + 8, 100, 12, AMBER, 0.20 * hb * (1 - hc))
    for k, ch in enumerate("480"):
        text(c, ch, x0 + k * cw, by, size, "black", INK, a0)
    line(c, x0 + 3 * cw, by - 90, x0 + 3 * cw, by + 30, INK, a0, 5)
    line(c, x0 + 3 * cw, by + 30, x0 + 3 * cw + 230, by + 30, INK, a0, 5)
    text(c, "12", x0 + 3 * cw + 100, by, size, "black", INK, a0)
    text(c, "4", x0 + 3 * cw + 70, by + 110, size, "black", GREEN, hb)
    text(c, "0", x0 + 3 * cw + 70 + cw, by + 110, size, "black", GREEN, ep(t, C["13.c"] + 1.4, 0.4))
    text(c, "−", x0 - cw - 6, by + 110, size, "black", INK2, ep(t, C["13.b"] + 1.0, 0.4))
    for k, ch in enumerate("48"):
        text(c, ch, x0 + k * cw, by + 110, size, "black", INK2, ep(t, C["13.b"] + 1.0, 0.4))
    line(c, x0 - cw - 20, by + 135, x0 + 2 * cw - 10, by + 135, INK2, ep(t, C["13.b"] + 1.0, 0.4), 4)
    text(c, "0", x0 + cw, by + 230, size, "black", INK2, hc)
    if hc > 0:
        dn = ep(t, C["13.c"] + 0.6, 0.6)
        text(c, "0", x0 + 2 * cw, lerp(by, by + 230, dn), size, "black", AMBER, hc * (0.4 + 0.6 * dn))
        arrow(c, x0 + 2 * cw + 50, by + 20, x0 + 2 * cw + 50, by + 180, AMBER, hc, 4, 14, progress=dn)
    if hb > 0:
        boxed(c, 1180, 230, 480, 140, AMBER, hb, 0.08)
        fmid(c, "12 × 4 = 48", 1420, 300, 56, "black", INK, hb)
    if hc > 0:
        text(c, "sobra 0 · desce o 0", 1420, 450, 34, "black", INK2, hc)
    result_box(c, "480 ÷ 12 = 40", 1420, 620, 60, ep(t, C["13.d"], 0.5), GREEN)


# ======================================================================
# bloco D — por 10, 100, 1000
# ======================================================================

def b_vezes100(c, t, C, B):
    head_seq(c, t, C, [("14", "× 10, × 100, × 1000", "A VÍRGULA ANDA", PURPLE),
                       ("15", "÷ 100", "O CAMINHO DE VOLTA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        m = ep(t, C["14.b"] + 0.8, 1.8)
        done = ep(t, C["14.c"], 0.5)
        hop(c, "347", {0, 1, 2}, 1, 3, m, 820, 360, 160, aa, col=mix(INK, GREEN, done), comma_a=1 - done)
        fmid(c, "× 100", 1340, 360, 96, "black", PURPLE, aa)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            text(c, "dois zeros → duas casas para a DIREITA", W / 2, 230, 34, "black", PURPLE, ab)
        fmid(c, "3,47 × 100 = 347", W / 2, 620, 64, "black", GREEN, done)
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            text(c, "100 pacotes de R$ 3,47 custam R$ 347", W / 2, 750, 36, "black", INK2, ad)
        return
    aa = ep(t, C["15.a"], 0.5)
    m = ep(t, C["15.b"], 1.8)
    done = ep(t, C["15.c"], 0.5)
    ad = ep(t, C["15.d"], 0.5)
    yy = lerp(360, 300, ad)
    hop(c, "00347", {2, 3, 4}, 3, 1, m, 780, yy, 150 - 30 * ad, aa, zero_a=ep(t, C["15.b"] + 1.6, 0.5),
        col=mix(INK, GREEN, done), marks=ad < 0.5)
    fmid(c, "÷ 100", 1360, yy, 96 - 20 * ad, "black", PURPLE, aa)
    text(c, "duas casas para a ESQUERDA · faltou casa? zero", W / 2, 215, 32, "black", PURPLE, aa * (1 - ad))
    fmid(c, "3,47 ÷ 100 = 0,0347", W / 2, 600 - 120 * ad, 64, "black", GREEN, done)
    if ad > 0:
        boxed(c, 360, 560, 1200, 240, GREEN, ad, 0.07)
        text(c, "ATALHO", W / 2, 610, 26, "black", GREEN, ad, tracking=3)
        fmid(c, "cada zero é uma casa", W / 2, 670, 54, "black", INK, ad)
        fmid(c, "× → direita       ÷ → esquerda", W / 2, 750, 44, "black", GREEN, ep(t, C["15.d"] + 1.2, 0.4))


# ======================================================================
# bloco E — o resultado que assusta
# ======================================================================

def b_assusta(c, t, C, B):
    frame(c, t, B["start"], "O RESULTADO QUE ASSUSTA", "E ESTÁ CERTO", AMBER)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        boxed(c, 200, 200, 740, 400, AMBER, aa, 0.07)
        text(c, "DIVIDIR por menos de 1", 570, 265, 36, "black", INK, aa)
        fmid(c, "4,8 ÷ 0,12 = 40", 570, 360, 60, "black", INK, aa)
        arrow(c, 570, 540, 570, 430, GREEN, aa, 8, 24, progress=aa)
        text(c, "CRESCE", 680, 505, 44, "black", GREEN, aa, align="left")
        text(c, "40 moedas", 460, 505, 30, "bold", GRAY, aa, align="right")
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        boxed(c, 980, 200, 740, 400, AMBER, ab, 0.07)
        text(c, "MULTIPLICAR por menos de 1", 1350, 265, 36, "black", INK, ab)
        fmid(c, "10 × 0,5 = 5", 1350, 360, 60, "black", INK, ab)
        arrow(c, 1350, 430, 1350, 540, RED, ab, 8, 24, progress=ab)
        text(c, "ENCOLHE", 1460, 505, 44, "black", RED, ab, align="left")
        text(c, "a metade", 1240, 505, 30, "bold", GRAY, ab, align="right")
    ac = ep(t, C["16.c"], 0.5)
    pill(c, "na dúvida? confira multiplicando de volta", W / 2, 670, GREEN, size=34, a=ac, anchor="center",
         bounds=(0, 1920))
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        fmid(c, "40 × 0,12 = 4,8", W / 2 - 40, 775, 60, "black", GREEN, ad)
        check_icon(c, W / 2 + 280, 775, 30, ep(t, C["16.d"] + 1.6, 0.4), GREEN)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("18", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    a1, a2 = ep(t, C["17.a"], 0.5), ep(t, C["17.b"], 0.5)
    for k, (a, s) in enumerate(((a1, "1,2 × 0,5"), (a2, "2,4 ÷ 0,6"))):
        x = 560 + k * 800
        if a <= 0:
            continue
        rrect(c, x - 330, 210, 660, 230, 24, "#F7F7F5", a)
        text(c, "1ª CONTA" if k == 0 else "2ª CONTA", x, 260, 24, "black", GRAY, a, tracking=1)
        fmid(c, s + " = ?", x, 360, 72, "black", INK, a)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 560)
    if t >= C["18"]:
        ra = ep(t, C["18.a"], 0.5)
        if ra > 0:
            fmid(c, "12 × 5 = 60", 560, 520, 50, "black", INK2, ra)
            text(c, "1 casa + 1 casa = 2 casas", 560, 600, 30, "black", PURPLE, ep(t, C["18.a"] + 1.2, 0.4))
            fmid(c, "0,60 = 0,6", 560, 700, 64, "black", GREEN, ep(t, C["18.a"] + 2.6, 0.4))
        rb = ep(t, C["18.b"], 0.5)
        if rb > 0:
            text(c, "as casas já são iguais", 1360, 500, 30, "black", PURPLE, rb)
            fmid(c, "24 ÷ 6 = 4", 1360, 590, 64, "black", GREEN, ep(t, C["18.b"] + 1.4, 0.4))
        rc = ep(t, C["18.c"], 0.5)
        if rc > 0:
            fmid(c, "conferindo: 4 × 0,6 = 2,4", 1330, 720, 40, "black", GREEN, rc)
            check_icon(c, 1640, 720, 24, rc, GREEN)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Somar: vírgula embaixo de vírgula.", "Multiplicar: some as casas decimais.",
          "Dividir por menos de 1 faz o número crescer."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1340, 58)


ERROS = [("Dizer que 0,3 × 0,04 = 0,12", "3 × 4 é mesmo 12",
          "faltou contar as casas: 1 + 2 = 3 casas → 0,012"),
         ("Achar que errou porque a divisão deu um número MAIOR", "na escola, dividir sempre diminuía",
          "dividir por menos de 1 aumenta: confira multiplicando de volta"),
         ("Somar decimais sem alinhar as vírgulas", "você alinha pela direita, como nos inteiros",
          "aí soma centavos com reais: vírgula embaixo de vírgula")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# questão 5
# ======================================================================

ALTS = [("A", "4", "4 × 0,12 = 0,48 m", RED), ("B", "40", "", GREEN), ("C", "57", "57 × 0,12 = 6,84 m: passa da fita", RED),
        ("D", "400", "400 × 0,12 = 48 m", RED), ("E", "576", "multiplicou: 4,8 × 0,12 = 0,576", AMBER)]


def fita(c, x, y, w, a, cortes=0.0):
    if a <= 0:
        return
    rrect(c, x, y, w, 46, 8, "#F3B6C9", a, shadow=True)
    rrect(c, x, y + 8, w, 8, 3, "#FFFFFF", 0.4 * a)
    for i in range(1, 40):
        f = clamp(cortes * 40 - i + 1)
        if f > 0:
            xx = x + w * i / 40
            line(c, xx, y - 4, xx, y + 50, "#B04A6E", a * f, 2)
    text(c, "4,8 m", x + w / 2, y + 96, 30, "black", INK2, a)


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "A FITA CORTADA EM PEDAÇOS", BLUE)
    card(c, *CARD_R)
    rows = [("23.a", "Uma fita de 4,8 metros será cortada em pedaços de 0,12 metro cada."),
            ("23.b", "Quantos pedaços serão obtidos?")]
    y = 240
    for cue, s in rows:
        a = ep(t, C[cue], 0.4)
        y += para(c, s, 190, y, 34, "black" if cue != "23.b" else "bold", INK if cue != "23.b" else BLUE, a, 600, 44) + 18
    rs = ep(t, C["25.a"], 0.4)
    fita(c, 190, 470, 590, ep(t, C["23.a"] + 1.0, 0.5) * (1 - rs), ep(t, C["23.b"], 2.0))
    cues_in = {L: C[f"24.{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["26.xa"], "C": C["26.xc"], "D": C["26.xd"], "E": C["26.xe"]}
    if t >= C["24"] - 0.3:
        K.alternativas(c, t, C, ALTS, 870, 205, 820, 42, C["25.ok"], "B", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["24.end"] - 1.9, 470, 720)
    ra = rs * (1 - ep(t, C["26"], 0.4))
    if ra > 0:
        rrect(c, 170, 460, 620, 350, 18, "#FFFFFF", ra, shadow=True)
        text(c, "quantos cabem → DIVISÃO", 480, 520, 28, "black", BLUE, ra)
        fmid(c, "4,80 ÷ 0,12", 480, 590, 46, "black", INK2, ep(t, C["25.b"], 0.4) * ra)
        fmid(c, "480 ÷ 12 = 40", 480, 670, 50, "black", GREEN, ep(t, C["25.b"] + 2.4, 0.4) * ra)
        fmid(c, "40 × 0,12 = 4,8", 450, 755, 42, "black", GREEN, ep(t, C["25.c"], 0.4) * ra)
        check_icon(c, 680, 755, 22, ep(t, C["25.c"] + 1.4, 0.4) * ra, GREEN)
    result_box(c, "Letra B", 480, 640, 56, ep(t, C["26"], 0.5), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "EXATO OU DÍZIMA?", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    expr(c, "1/4 = 0,25", 520, 340, 90, aa, cores={2: GREEN})
    chip(c, "e acaba", 520, 480, GREEN, ep(t, C["28.a"] + 1.6, 0.4), 32)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        expr(c, "1/3 =", 1020, 340, 90, ab, align="left")
        n = 3 + int(clamp((t - C["28.b"]) / 3.0) * 2)
        s = "0," + "3" * n
        x = 1020 + expr_w("1/3 =", 90) + 30
        for i, ch in enumerate(s):
            fa = 1.0 if i < 4 else max(0.2, 1 - (i - 3) * 0.25)
            text(c, ch, x, 340 + 32, 90, "black", AMBER, ab * fa, align="left")
            x += text_w(ch, "black", 90)
        chip(c, "e NUNCA acaba", 1330, 480, AMBER, ep(t, C["28.b"] + 1.6, 0.4), 32)
    text(c, "dá para saber ANTES de dividir", W / 2, 640, 48, "black", PURPLE, ep(t, C["28.c"], 0.5))
    pill(c, "ep. 6 · decimal exato ou dízima?", W / 2, 770, PURPLE, size=32, a=ep(t, C["28.d"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Você já levou susto com uma divisão que cresceu?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, dinheiro=b_dinheiro, casas=b_casas, somar=b_somar, multiplicar=b_multiplicar,
              dividir=b_dividir, vezes100=b_vezes100, assusta=b_assusta, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, questao=b_questao, ponte=b_ponte, cta=b_cta)
