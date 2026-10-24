"""Visual — Frações, Decimais e Dízimas, Episódio 4: A armadilha do "do restante" (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (pizza, expr com frações empilhadas, alternativas, erro_cards...).
Peças deste episódio: carteira com notas de R$ 100 que saem para cada gasto, faixa que ENCOLHE a cada etapa
(o 1/4 da 2ª etapa desenhado sobre a faixa já diminuída) e, ao lado, a versão errada sobre a faixa inteira com X vermelho.
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
fr, expr, expr_w, pizza = K.fr, K.expr, K.expr_w, K.pizza
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep4_do_restante.mp4"
CARD_R = K.CARD_R
GASTO1 = "#E8743B"      # 1ª etapa (aluguel / moradia)
GASTO2 = "#2BA6A0"      # 2ª etapa (transporte)
RESTO = "#F3E6C4"       # o que ainda está lá
NOTA = "#2FA36B"


# ======================================================================
# peças do episódio
# ======================================================================

def faixa(c, x, y, w, h, n, cores, a, rot=None, rot_size=34, gap=5, apagadas=(), rot_cor="#FFFFFF"):
    """faixa dividida em n partes iguais. cores[i] = cor da parte (None = resto); apagadas = partes que saíram
    (só contorno tracejado); rot[i] = rótulo (texto ou fração 'a/b')."""
    if a <= 0:
        return
    sw = (w - gap * (n - 1)) / n
    for i in range(n):
        xx = x + i * (sw + gap)
        if i in apagadas:
            pe = paint(LIGHT, a, stroke=3)
            pe.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, y, sw, h), 10, 10), pe)
            continue
        col = cores[i] if i < len(cores) and cores[i] else RESTO
        rrect(c, xx, y, sw, h, 10, col, a)
        rrect(c, xx + 5, y + 5, sw - 10, h * 0.22, 6, "#FFFFFF", a * 0.18)
        if rot and i < len(rot) and rot[i]:
            cor = rot_cor if col != RESTO else INK2
            expr(c, rot[i], xx + sw / 2, y + h / 2 + (0 if "/" in rot[i] else 0), rot_size, a, cores={0: cor})


def tracejado(c, x0, y0, x1, y1, col, a, sw=3):
    if a <= 0:
        return
    pe = paint(col, a, stroke=sw)
    pe.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    c.drawLine(x0, y0, x1, y1, pe)


def encolhe(c, t, x, y, w, h, a1, a2, a3, rots1=None, rots2=None, dy=150, size=34):
    """a faixa que ENCOLHE: linha 1 = o total em 3 partes, a 1ª sai; linha 2 = só o que sobrou (2/3), em 4 partes;
    a 1ª parte da linha 2 é o 1/4 DO QUE SOBROU."""
    faixa(c, x, y, w, h, 3, [GASTO1], a1, rots1, size)
    if a2 <= 0:
        return
    x2, w2 = x + w / 3 + 2, w * 2 / 3 - 2
    tracejado(c, x2, y + h + 6, x2, y + dy - 6, GRAY, a2)
    tracejado(c, x + w, y + h + 6, x + w, y + dy - 6, GRAY, a2)
    faixa(c, x2, y + dy, w2, h, 4, [GASTO2 if a3 > 0 else None], a2, rots2 if a3 > 0 else None, size)


def errada(c, x, y, w, h, a, ax, rots=None, size=34):
    """a versão ERRADA com o mesmo desenho: o 1/4 tirado da faixa INTEIRA, com X vermelho."""
    faixa(c, x, y, w, h, 4, [RED], a, rots, size)
    check_icon(c, x + w + 50, y + h / 2, 34, ax, RED, "x")


def nota(c, x, y, a, val="100", col=NOTA, w=130, h=62):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 8, col, a, shadow=True)
    rrect(c, x + 7, y + 7, w - 14, h - 14, 6, mix(col, "#FFFFFF", 0.25), a)
    text_mid(c, val, x + w / 2, y + h / 2, 26, "black", "#FFFFFF", a)


def carteira(c, x, y, w, h, a):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 28, "#7B4A2A", a, shadow=True)
    rrect(c, x + 14, y + 14, w - 28, h - 28, 20, "#9A6238", a)
    rrect(c, x + w - 110, y + h / 2 - 34, 130, 68, 20, "#5A341C", a)
    c.drawCircle(x + w - 50, y + h / 2, 12, paint("#E8C07A", a))


def _slot(i):
    return 250 + (i % 4) * 140, 290 + (i // 4) * 85


ALUG = [8, 9, 10, 11]      # as 4 notas que vão para o aluguel (1/3 de 12)
TRANSP = [6, 7]            # as 2 notas que vão para o transporte (1/4 das 8 que sobraram)


def notas_salario(c, t, C, a):
    """12 notas de R$ 100 na carteira; 4 voam para o aluguel (06.d) e 2 para o transporte (07.c)."""
    for i in range(12):
        x, y = _slot(i)
        if i in ALUG:
            j = ALUG.index(i)
            u = ep(t, C["06.d"] + 0.2 * j, 0.8)
            dx, dy = 1030 + j * 44, 290
        elif i in TRANSP:
            j = TRANSP.index(i)
            u = ep(t, C["07.c"] + 0.25 * j, 0.8)
            dx, dy = 1030 + j * 44, 560
        else:
            u, dx, dy = 0, x, y
        arco = -90 * math.sin(math.pi * u)
        nota(c, lerp(x, dx, u), lerp(y, dy, u) + arco, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A ARMADILHA DO “DO RESTANTE”", AMBER)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 360, 190, 1200, 120, AMBER, aa, 0.10)
        fmid(c, "o erro que MAIS CUSTA PONTO em frações", W / 2, 250, 46, "black", INK, aa)
    alts = [("A", "5/12"), ("B", "1/2"), ("C", "7/12"), ("D", "2/3"), ("E", "3/4")]
    ac = ep(t, C["01.c"], 0.5)
    for k, (L, f) in enumerate(alts):
        a = ep(t, C["01.b"] + 0.25 * k, 0.4)
        if a <= 0:
            continue
        x = 400 + k * 280
        trap = L == "A"
        card(c, x - 115, 380, 230, 250, a)
        if trap and ac > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 115, 380, 230, 250), 24, 24), paint(RED, a * ac, stroke=6))
        badge_num(c, L, x, 425, a, 24, bg=RED if trap and ac > 0.5 else INK)
        n_, d_ = f.split("/")
        fr(c, n_, d_, x, 540, 66, RED if trap and ac > 0.5 else INK, a)
    selo(c, 400, 720, ac, "ESPERANDO POR VOCÊ", RED, -5, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "identificar o “do restante”", "no enunciado"), ("02.b", "resolver em UM passo", "com um atalho")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 54, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 34, "bold", GRAY, a, align="left")
    ab = ep(t, C["02.b"], 0.5)
    pizza(c, 1470, 480, 170, 6, {2}, ab, sel_col=GASTO2, gone={0, 1}, pull=0.5)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "EPISÓDIO 1", 560, 230, GRAY, size=24, a=aa, anchor="center", bounds=(0, 1920))
        fmid(c, "“DE” = VEZES", 560, 320, 54, "black", PURPLE, aa)
        expr(c, "1/4 de 800", 560, 470, 70, aa, cores={1: AMBER})
        fmid(c, "800 ÷ 4 = 200", 560, 640, 56, "black", INK, ep(t, C["03.a"] + 1.4, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        line(c, W / 2, 220, W / 2, 780, LINE, ab, 3)
        pill(c, "EPISÓDIO 3", 1360, 230, GRAY, size=24, a=ab, anchor="center", bounds=(0, 1920))
        fmid(c, "MULTIPLICAR FRAÇÕES", 1360, 320, 46, "black", PURPLE, ab)
        text(c, "em cima × em cima", 1360, 400, 34, "bold", INK2, ab)
        text(c, "embaixo × embaixo", 1360, 450, 34, "bold", INK2, ab)
        expr(c, "1/2 × 1/3 = 1/6", 1360, 620, 70, ep(t, C["03.c"], 0.5), cores={4: GREEN})


# ======================================================================
# a pizza que encolhe
# ======================================================================

def b_encolhe(c, t, C, B):
    head_seq(c, t, C, [("04", "A ANALOGIA", "A PIZZA QUE ENCOLHE", AMBER), ("05", "DUAS PALAVRAS", "TOTAL E RESTANTE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        pizza(c, 560, 450, 200, 6, 0, aa)
        pill(c, "TOTAL", 560, 710, BLUE, size=34, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "o tudo do começo", 560, 790, 32, "bold", INK2, aa)
        ab = ep(t, C["05.b"], 0.5)
        pizza(c, 1360, 450, 200, 6, 0, ab, gone={0, 1})
        pill(c, "RESTANTE", 1360, 710, BLUE, size=34, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "o que sobrou depois de uma parte sair", 1360, 790, 32, "bold", INK2, ab)
        return
    a0 = ep(t, C["04.t"], 0.5)
    comeu = ep(t, C["04.a"] + 0.9, 0.4)
    sel = {0, 1} if comeu < 0.5 else set()
    gone = {0, 1} if comeu >= 0.5 else set()
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        sel = {2}
    pizza(c, 560, 430, 190, 6, sel, a0, sel_col=GASTO2 if ab > 0 else None, gone=gone,
          pull=ep(t, C["04.a"], 0.5) * (1 - comeu) + ab * 0.6)
    text(c, "você come 1/3", 560, 675, 34, "black", GASTO1, ep(t, C["04.a"], 0.4) * (1 - ab))
    text(c, "irmão: 1/4 do que SOBROU", 560, 675, 34, "black", GASTO2, ab)
    text(c, "1 das 4 fatias que sobraram", 560, 718, 28, "bold", INK2, ab)
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        pill(c, "CERTO", 560, 205, GREEN, size=28, a=ac, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pill(c, "ERRADO", 1360, 205, RED, size=28, a=ad, anchor="center", bounds=(0, 1920))
        pizza(c, 1360, 430, 190, 4, {0}, ad, sel_col=RED, pull=0.6)
        check_icon(c, 1600, 260, 34, ad, RED, "x")
        text(c, "1/4 da pizza INTEIRA", 1360, 675, 34, "black", RED, ad)
    regra(c, "a pizza ENCOLHEU antes de ele chegar", W / 2, 790, ep(t, C["04.e"], 0.5), 34, AMBER)


# ======================================================================
# bloco A — o salário em reais
# ======================================================================

def b_salario(c, t, C, B):
    head_seq(c, t, C, [("06", "DINHEIRO DE VERDADE", "SALÁRIO DE R$ 1.200", BLUE),
                       ("07", "SEGUNDA ETAPA", "1/4 DO QUE SOBROU", BLUE),
                       ("08", "LADO A LADO", "1/4 DE QUÊ?", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid in ("06", "07"):
        aa = ep(t, C["06.a"], 0.5)
        carteira(c, 210, 250, 700, 330, aa)
        notas_salario(c, t, C, aa)
        s07 = ep(t, C["07.a"], 0.4)
        text(c, "R$ 1.200 = 12 notas de R$ 100", 560, 660, 36, "black", INK, aa * (1 - s07))
        pill(c, "sobram na carteira: R$ 800", 560, 650, GREEN, size=36, a=s07, anchor="center", bounds=(0, 1920))
        ab = ep(t, C["06.b"], 0.5)
        text(c, "ETAPA = cada passo da história", 560, 760, 30, "black", BLUE, ab)
        for k, (cue, tit, sub, calc, val) in enumerate((("06.c", "ETAPA 1 · ALUGUEL", "1/3 do salário", "1.200 ÷ 3 = 400", "R$ 400"),
                                                        ("07.b", "ETAPA 2 · TRANSPORTE", "1/4 do que SOBROU", "800 ÷ 4 = 200",
                                                         "R$ 200"))):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 220 + k * 270
            col = GASTO1 if k == 0 else GASTO2
            boxed(c, 1000, y, 660, 230, col, a, 0.08)
            text(c, tit, 1030, y + 44, 26, "black", col, a, align="left")
            text(c, sub, 1630, y + 44, 26, "black", INK2, a, align="right")
            ar = ep(t, C["06.d" if k == 0 else "07.c"] + 0.9, 0.4)
            fmid(c, calc, 1330, y + 190, 36, "black", INK, ar)
            text(c, val, 1625, y + 130, 50, "black", col, ar, align="right")
        return
    # 08: certo × errado, o mesmo desenho
    aa = ep(t, C["08.a"], 0.5)
    a0 = ep(t, C["08.t"], 0.5)
    ac = ep(t, C["08.c"], 0.5)
    pill(c, "CERTO", 560, 215, GREEN, size=28, a=a0, anchor="center", bounds=(0, 1920))
    encolhe(c, t, 260, 290, 600, 90, a0, a0, a0, ["400", "", ""], ["200", "", "", ""], 160)
    text(c, "R$ 800", 860, 275, 26, "black", INK2, a0, align="right")
    text(c, "1/4 de 800 = R$ 200", 560, 620, 38, "black", GREEN, a0)
    check_icon(c, 300, 606, 22, ac, GREEN)
    if ac > 0:
        boxed(c, 220, 560, 680, 110, GREEN, ac, 0.06)
    pill(c, "ERRADO", 1360, 215, RED, size=28, a=aa, anchor="center", bounds=(0, 1920))
    errada(c, 1060, 290, 600, 90, aa, aa, ["300", "", "", ""])
    text(c, "R$ 1.200", 1660, 275, 26, "black", INK2, aa, align="right")
    text(c, "1/4 de 1.200 = R$ 300", 1360, 460, 38, "black", RED, aa)
    ab = ep(t, C["08.b"], 0.5)
    para(c, "parece certo: o 1/4 “parece” ser do salário", 1080, 540, 30, "bold", AMBER, ab, 580)
    line(c, W / 2, 200, W / 2, 680, LINE, a0, 3)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        pill(c, "no fim, sobram R$ 600 = METADE do salário", W / 2, 765, GREEN, size=34, a=ad, anchor="center",
             bounds=(0, 1920))


# ======================================================================
# bloco B — a mesma conta em frações
# ======================================================================

def b_fracoes(c, t, C, B):
    head_seq(c, t, C, [("09", "AGORA EM FRAÇÕES", "QUANTO SOBRA?", BLUE), ("10", "A SEGUNDA ETAPA", "1/4 DE 2/3", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        a0 = ep(t, C["09.t"], 0.5)
        faixa(c, 360, 240, 1200, 110, 3, [GASTO1], a0, ["1/3", "", ""], 44)
        text(c, "aluguel", 560, 225, 26, "black", GASTO1, a0)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            rrect(c, 765, 370, 795, 8, 4, GREEN, ab)
            line(c, 765, 360, 765, 378, GREEN, ab, 4)
            line(c, 1560, 360, 1560, 378, GREEN, ab, 4)
            fr(c, "2", "3", 1162, 450, 54, GREEN, ab)
        expr(c, "1 − 1/3 = 2/3", W / 2, 590, 70, ab, cores={4: GREEN})
        pill(c, "COMPLEMENTO = o que falta para completar o inteiro", W / 2, 700, BLUE, size=30, a=ab, anchor="center",
             bounds=(0, 1920))
        ac = ep(t, C["09.c"], 0.5)
        check_icon(c, 690, 785, 24, ac, GREEN)
        text(c, "confere: R$ 800 é 2/3 de R$ 1.200", 730, 800, 36, "black", GREEN, ac, align="left")
        return
    # 10: 1/4 de 2/3 na faixa que encolhe × 1/4 da faixa inteira
    a0 = ep(t, C["10.t"], 0.5)
    aa = ep(t, C["10.a"], 0.5)
    ac = ep(t, C["10.c"], 0.5)
    pill(c, "CERTO", 560, 215, GREEN, size=28, a=a0, anchor="center", bounds=(0, 1920))
    encolhe(c, t, 260, 280, 600, 90, a0, a0, aa, ["1/3", "", ""], ["1/6" if ac > 0.5 else "1/4", "", "", ""], 150, 30)
    fr(c, "2", "3", 900, 475, 34, INK2, a0)
    expr(c, "1/4 × 2/3", 560, 600, 56, aa)
    expr(c, "= 2/12 = 1/6", 560, 720, 56, ep(t, C["10.b"], 0.5), alfas={2: ac, 3: ac}, cores={3: GREEN})
    ad = ep(t, C["10.d"], 0.5)
    line(c, W / 2, 200, W / 2, 680, LINE, ad, 3)
    pill(c, "ERRADO", 1360, 215, RED, size=28, a=ad, anchor="center", bounds=(0, 1920))
    errada(c, 1060, 280, 600, 90, ad, ad, ["1/4", "", "", ""], 30)
    text(c, "1/4 do salário inteiro", 1360, 450, 36, "black", RED, ad)
    ae = ep(t, C["10.d"] + 1.6, 0.5)
    check_icon(c, 1100, 586, 22, ae, GREEN)
    expr(c, "1/6 de 1.200 = 200", 1380, 600, 48, ae, cores={4: GREEN})
    text(c, "os mesmos R$ 200", 1380, 720, 34, "black", GREEN, ae)


# ======================================================================
# bloco C — o erro de somar direto
# ======================================================================

def b_somar(c, t, C, B):
    frame(c, t, B["start"], "A RESPOSTA QUE SEMPRE APARECE", "SOMAR DIRETO", AMBER)
    aa = ep(t, C["11.a"], 0.5)
    pill(c, "ERRADO", 560, 215, RED, size=28, a=aa, anchor="center", bounds=(0, 1920))
    faixa(c, 260, 290, 600, 90, 12, [GASTO1] * 4 + [RED] * 3, aa, gap=4)
    expr(c, "1/3 + 1/4", 560, 470, 60, aa)
    ab = ep(t, C["11.b"], 0.5)
    expr(c, "= 7/12", 560, 580, 60, ab, cores={1: RED})
    acc = ep(t, C["11.c"], 0.5)
    text(c, "parece: gastos se somam", 560, 680, 32, "black", AMBER, acc * (1 - ep(t, C["11.d"], 0.4)))
    ad = ep(t, C["11.d"], 0.5)
    text(c, "= R$ 700 de gasto", 560, 680, 40, "black", RED, ad)
    check_icon(c, 920, 335, 34, ad, RED, "x")
    line(c, W / 2, 200, W / 2, 740, LINE, aa, 3)
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        pill(c, "CERTO", 1360, 215, GREEN, size=28, a=ae, anchor="center", bounds=(0, 1920))
        faixa(c, 1060, 290, 600, 90, 12, [GASTO1] * 4 + [GASTO2] * 2, ae, gap=4)
        expr(c, "1/3 + 1/6", 1360, 470, 60, ae)
        expr(c, "= 1/2", 1360, 580, 60, ae, cores={1: GREEN})
        text(c, "= R$ 600 de gasto", 1360, 680, 40, "black", GREEN, ae)
        check_icon(c, 1720, 335, 34, ae, GREEN)
    regra(c, "a errada (7/12) está nas alternativas, esperando", W / 2, 785, ep(t, C["11.e"] + 2.0, 0.5), 30, AMBER)


# ======================================================================
# bloco D — o atalho
# ======================================================================

def b_atalho(c, t, C, B):
    frame(c, t, B["start"], "O ATALHO", "MULTIPLIQUE O QUE FICA", GREEN)
    aa = ep(t, C["12.a"], 0.5)
    chip(c, "o que SAI", 330, 300, GRAY, aa, 34)
    strike(c, 250, 300, 410, 300, aa, RED, aa)
    chip(c, "o que FICA", 330, 420, GREEN, ep(t, C["12.a"] + 0.8, 0.4), 34)
    X1, X2 = 560, 1360
    ab = ep(t, C["12.b"], 0.5)
    a0 = ep(t, C["12.t"], 0.5)
    w1 = X2 - X1
    faixa(c, X1, 240, w1, 80, 3, [GREEN if ab > 0.5 else None] * 3, a0, apagadas={0} if ab > 0.5 else ())
    expr(c, "fica 2/3", X2 + 40, 280, 40, ab, cores={1: GREEN}, align="left")
    acc = ep(t, C["12.c"], 0.5)
    w2 = w1 * 2 / 3
    faixa(c, X2 - w2, 380, w2, 80, 4, [GREEN if acc > 0.5 else None] * 4, ab, apagadas={0} if acc > 0.5 else ())
    tracejado(c, X2 - w2, 326, X2 - w2, 374, GRAY, ab)
    expr(c, "fica 3/4", X2 + 40, 420, 40, acc, cores={1: GREEN}, align="left")
    text(c, "do que havia", X2 + 40, 478, 26, "bold", INK2, acc, align="left")
    ad = ep(t, C["12.d"], 0.5)
    w3 = w2 * 3 / 4
    faixa(c, X2 - w3, 520, w3, 80, 1, [GREEN], ad)
    tracejado(c, X2 - w3, 466, X2 - w3, 514, GRAY, ad)
    expr(c, "sobra 1/2", X2 + 40, 560, 40, ad, cores={1: GREEN}, align="left")
    text(c, "do salário", X2 + 40, 618, 26, "bold", INK2, ad, align="left")
    expr(c, "3/4 × 2/3 = 6/12 = 1/2", 860, 700, 60, ad, cores={6: GREEN})
    ae = ep(t, C["12.e"], 0.5)
    pill(c, "1/2 de R$ 1.200 = R$ 600 · em um passo", 860, 790, GREEN, size=30, a=ae, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco E — palavras de alerta
# ======================================================================

def b_alerta(c, t, C, B):
    frame(c, t, B["start"], "COMO RECONHECER", "AS PALAVRAS DE ALERTA", AMBER)
    text(c, "viu uma destas? a 2ª fração NÃO é do total", W / 2, 240, 34, "black", INK2, ep(t, C["13.a"], 0.5))
    pal = [("13.b", "do restante"), ("13.c", "do que sobrou"), ("13.d", "do que havia"), ("13.e", "do volume que havia")]
    for k, (cue, s) in enumerate(pal):
        a, d = rise(t, C[cue])
        x = 560 + (k % 2) * 760
        y = 360 + (k // 2) * 150 + d
        chip(c, "“" + s + "”", x, y, AMBER, a, 48, w=660)
    af = ep(t, C["13.f"], 0.5)
    pizza(c, 700, 730, 70, 6, {2}, af, sel_col=GASTO2, gone={0, 1}, pull=0.5)
    text(c, "a 2ª fração é de uma pizza MENOR", 790, 744, 38, "black", AMBER, af, align="left")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["“Do restante” é fração do que sobrou, não do total.", "Primeiro descubra o que sobrou; depois tire a fração dele.",
          "Atalho: multiplique o que sobra em cada etapa."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "23"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=GREEN if k == 2 else PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1340, 54)


ERROS = [("Somar as duas frações: 1/3 + 1/4 = 7/12", "foram dois gastos, e gastos se somam",
          "a 2ª fração é de uma pizza menor: primeiro descubra o que sobrou"),
         ("Subtrair a 2ª fração do total: 3/5 − 1/4", "tirar é subtrair",
          "o 1/4 é do que havia: calcule sobre a parte que sobrou"),
         ("Responder o que foi gasto quando a pergunta é o que sobrou (ou o contrário)", "a conta estava certa",
          "a alternativa do gasto está lá, esperando: releia a pergunta no fim")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["15", "16", "17"], ERROS)


# ======================================================================
# questões
# ======================================================================

NOTA_Q = "Questão no estilo do ENEM, do material de estudo."


def enunciado(c, t, C, rows, y=240, alerta=None):
    """rows = [(cue, texto, estilo)]; alerta = (índice da linha, instante) → a linha vira âmbar (palavra de alerta)."""
    for k, (cue, s, est) in enumerate(rows):
        a = ep(t, C[cue], 0.4)
        col = BLUE if est == "q" else INK
        if alerta and alerta[0] == k:
            col = mix(col, AMBER, ep(t, alerta[1], 0.4))
        y += para(c, s, 190, y, 30, "bold" if est == "q" else "black", col, a, 560, 38) + 14
    return y


ALTS7 = [("A", "= 5/12", "somou 1/3 + 1/4 e tirou de 1", RED), ("B", "= 1/2", "", GREEN), ("C", "= 7/12", "", RED),
         ("D", "= 2/3", "", RED), ("E", "= 3/4", "", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "ESTILO ENEM · EU FAÇO COM VOCÊ", "MORADIA E TRANSPORTE", BLUE)
    card(c, *CARD_R)
    rows = [("18.a", "Um trabalhador gasta 1/3 do salário com moradia e, do que resta, gasta 1/4 com transporte.", "t"),
            ("18.b", "Que fração do salário sobra depois desses dois gastos?", "q")]
    enunciado(c, t, C, rows, alerta=(0, C["19.t"]))
    text(c, NOTA_Q, 190, 830, 18, "medium", GRAY, ep(t, C["18.a"], 0.5), align="left")
    cues_in = {L: C[f"18.{x}"] for L, x in zip("ABCDE", "cdefg")}
    K.alternativas(c, t, C, ALTS7, 870, 205, 820, 42, C["20.ok"], "B", cues_in, {"A": C["20.x"]}, gap=14)
    pill(c, "alerta: “do que resta”", 190, 500, AMBER, size=26, a=ep(t, C["19.t"], 0.5), bounds=(0, 1920))
    ra = ep(t, C["19.a"], 0.4)
    if ra > 0:
        rrect(c, 170, 550, 620, 260, 18, "#FFFFFF", ra, shadow=True)
        longo = 1 - ep(t, C["20.t"], 0.4)
        expr(c, "1 − 1/3 = 2/3", 480, 600, 40, ra * longo)
        expr(c, "1/4 × 2/3 = 1/6", 480, 680, 40, ep(t, C["19.b"], 0.4) * longo)
        expr(c, "2/3 − 1/6 = 3/6 = 1/2", 480, 760, 40, ep(t, C["19.c"], 0.4) * longo, cores={6: GREEN})
        at = ep(t, C["20.t"], 0.4)
        text(c, "ATALHO: sobra 3/4 de 2/3", 480, 600, 30, "black", GREEN, at)
        expr(c, "3/4 × 2/3 = 1/2", 480, 680, 46, ep(t, C["20.a"], 0.4), cores={4: GREEN})
        result_box(c, "Letra B", 480, 765, 40, ep(t, C["20.ok"], 0.5), GREEN)


ALTS1 = [("A", "= 7/20", "fez 3/5 − 1/4: tirou do total", RED), ("B", "= 2/5", "", RED), ("C", "= 9/20", "", GREEN),
         ("D", "= 1/2", "", RED), ("E", "= 3/4", "", RED)]


def b_q1(c, t, C, B):
    head_seq(c, t, C, [("21", "ESTILO ENEM · AGORA É COM VOCÊ", "O RESERVATÓRIO", GREEN),
                       ("22", "VAMOS CONFERIR", "O RESERVATÓRIO", GREEN)])
    card(c, *CARD_R)
    rows = [("21.a", "Um reservatório está com 3/5 de sua capacidade total.", "t"),
            ("21.b", "Para a limpeza, retira-se 1/4 do volume que havia no reservatório.", "t"),
            ("21.c", "Após a retirada, que fração da capacidade total permanece com água?", "q")]
    resol = ep(t, C["22.b"], 0.4)
    enunciado(c, t, C, rows, alerta=(1, C["22.a"]))
    text(c, NOTA_Q, 190, 830, 18, "medium", GRAY, ep(t, C["21.a"], 0.5), align="left")
    cues_in = {L: C[f"21.{x}"] for L, x in zip("ABCDE", "defgh")}
    K.alternativas(c, t, C, ALTS1, 870, 205, 820, 42, C["22.ok"], "C", cues_in, {"A": C["22.x"]}, gap=14)
    pause_timer(c, t, C["21.end"] - 1.9, 470, 700)
    if resol > 0:
        rrect(c, 170, 596, 620, 206, 18, "#FFFFFF", resol, shadow=True)
        text(c, "saiu 1/4 → ficam 3/4 do que havia", 480, 638, 28, "black", GREEN, resol)
        expr(c, "3/4 × 3/5 = 9/20", 480, 702, 44, ep(t, C["22.c"], 0.4), cores={4: GREEN})
        result_box(c, "Letra C", 480, 768, 32, ep(t, C["22.ok"], 0.5), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DECIMAIS SEM CALCULADORA", PURPLE)
    aa = ep(t, C["24.a"], 0.5)
    fr(c, "1", "2", 520, 400, 110, INK, aa)
    arrow(c, 620, 400, 820, 400, LIGHT, aa, 6, 18, progress=aa)
    fmid(c, "0,5", 1000, 400, 120, "black", PURPLE, aa)
    ab = ep(t, C["24.b"], 0.5)
    for k, s in enumerate(("3,2 + 1,45", "0,3 × 0,04")):
        fmid(c, s, 1440, 300 + k * 110, 52, "black", INK, ab * ep(t, C["24.b"] + 0.4 * k, 0.4))
    acc = ep(t, C["24.c"], 0.5)
    fmid(c, "4,8 ÷ 0,12 = 40 ?!", 1440, 560, 52, "black", AMBER, acc)
    text(c, "assusta, mas está certo", 1440, 630, 30, "bold", INK2, acc)
    pill(c, "ep. 5 · operações com decimais", W / 2, 770, PURPLE, size=32, a=ep(t, C["24.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["25.like"], C["25.sub"], C["25.bell"], C["25.com"], C["25.bye"], "Você já tinha caído no “do restante”?",
        canal="no Estudativo", anki=C["25.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, encolhe=b_encolhe, salario=b_salario, fracoes=b_fracoes,
              somar=b_somar, atalho=b_atalho, alerta=b_alerta, recap=b_recap, erros=b_erros, q7=b_q7, q1=b_q1,
              ponte=b_ponte, cta=b_cta)
