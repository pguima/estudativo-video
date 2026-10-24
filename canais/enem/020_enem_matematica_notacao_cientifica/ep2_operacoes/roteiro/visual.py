"""Visual — Notação Científica e Ordem de Grandeza, Episódio 2: multiplicar, dividir, elevar e tirar raiz (iniciantes, tema claro).
Peças comuns em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, erro_cards, atalho...).
Peças deste episódio: as DUAS PISTAS (coeficientes / expoentes) e a GANGORRA (coeficiente × 10 ⇄ expoente − 1).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum020", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.boxed, K.regra, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_notacao_ep2_operacoes.mp4"
CARD_R = K.CARD_R
COEF = BLUE        # pista dos coeficientes
EXPO = PURPLE      # pista dos expoentes


def fpara(c, s, x, y, size, peso, color, a, maxw, lh=None):
    """parágrafo com expoentes ('10^{-5}') via ftext"""
    lh = lh or size * 1.34
    out, cur = [], ""
    for w in s.split():
        tst = (cur + " " + w).strip()
        if cur and K.ftext_w(tst, peso, size) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    if a > 0:
        for k, ln in enumerate(out):
            ftext(c, ln, x, y + k * lh, size, peso, color, a, align="left")
    return len(out) * lh


def mat2f(s):
    """texto do material ('10^(−5)') → ftext ('10^{−5}')"""
    return re.sub(r"\^\(([^)]*)\)", r"^{\1}", s)


# ======================================================================
# peças do episódio
# ======================================================================

def pistas(c, x, y, w, top, bot, a_top=1.0, a_bot=1.0, h=120, size=56, res_top=None, res_bot=None, a_res=0.0):
    """as duas pistas: em cima os coeficientes (azul), embaixo os expoentes (roxo). top/bot = expressões (expr)."""
    ar = a_res if isinstance(a_res, tuple) else (a_res, a_res)
    for k, (lbl, s, aa, col, res) in enumerate([("COEFICIENTES", top, a_top, COEF, res_top), ("EXPOENTES", bot, a_bot, EXPO, res_bot)]):
        if aa <= 0:
            continue
        yy = y + k * (h + 36)
        rrect(c, x, yy, w, h, 22, mix("#FFFFFF", col, 0.08), aa)
        line(c, x + 30, yy + h - 14, x + w - 30, yy + h - 14, mix("#FFFFFF", col, 0.35), aa, 3)
        pill(c, lbl, x + 20, yy - 2, col, size=20, a=aa, bounds=(0, 1920))
        expr(c, s, x + w * 0.42, yy + h / 2, size, aa, cores={i: col for i in range(30)})
        if res is not None and ar[k] > 0:
            expr(c, res, x + w * 0.86, yy + h / 2, size, aa * ar[k], cores={i: GREEN for i in range(30)})


def gangorra(c, cx, cy, ang, esq, dir_, a, larg=760, size=64, col_e=COEF, col_d=EXPO, rot_e="coeficiente", rot_d="expoente"):
    """gangorra: viga apoiada no meio; ang > 0 = lado esquerdo para cima. esq/dir_ = expressões nas pontas."""
    if a <= 0:
        return
    pth = skia.Path(); pth.moveTo(cx, cy + 6); pth.lineTo(cx - 70, cy + 120); pth.lineTo(cx + 70, cy + 120); pth.close()
    c.drawPath(pth, paint(INK2, a))
    rrect(c, cx - 140, cy + 116, 280, 16, 8, INK2, a)
    rad = math.radians(-ang)
    dx, dy = math.cos(rad) * larg / 2, math.sin(rad) * larg / 2
    pv = skia.Paint(AntiAlias=True, Color=hexc(INK, a), StrokeWidth=16, Style=skia.Paint.kStroke_Style,
                    StrokeCap=skia.Paint.kRound_Cap)
    c.drawLine(cx - dx, cy - dy, cx + dx, cy + dy, pv)
    c.drawCircle(cx, cy, 14, paint(AMBER, a))
    for sgn, s, col, rot in ((-1, esq, col_e, rot_e), (1, dir_, col_d, rot_d)):
        ex, ey = cx + sgn * dx, cy + sgn * dy
        bw = max(170, K.math_w(s, size) + 60)
        rrect(c, ex - bw / 2, ey - 128, bw, 110, 20, "#FFFFFF", a, shadow=True)
        rrect(c, ex - bw / 2, ey - 128, bw, 110, 20, mix("#FFFFFF", col, 0.10), a)
        expr(c, s, ex, ey - 73, size, a, cores={i: col for i in range(10)})
        text(c, rot, ex, ey + 30, 26, "black", col, a)


def tilt(t, t0, de, para_, dur=0.8):
    return lerp(de, para_, ease_io(prog(t, t0, dur)))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "NOTAÇÃO CIENTÍFICA · EP. 2", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        card(c, 460, 200, 1000, 180, aa)
        expr(c, "(8·10^4) · (5·10^2) = 40·10^6", W / 2, 290, 64, aa, cores={4: INK})
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        for k, (L, s) in enumerate([("A", "1,3·10^7"), ("B", "4·10^6"), ("C", "40·10^6"), ("D", "4·10^8")]):
            x = 420 + k * 360
            hl = k == 2
            rrect(c, x - 150, 450, 300, 110, 20, mix("#FFFFFF", AMBER, 0.18) if hl else "#FFFFFF", ab, shadow=True)
            badge_num(c, L, x - 110, 505, ab, 22, bg=INK)
            expr(c, s, x + 20, 505, 46, ab)
        cur_a = fw(t, C["01.b"] + 0.6, C["01.c"] + 1.2)
        cursor(c, lerp(1500, 1180, ep(t, C["01.b"] + 0.6, 0.8)), lerp(700, 530, ep(t, C["01.b"] + 0.6, 0.8)), cur_a,
               math.sin(math.pi * prog(t, C["01.b"] + 1.5, 0.35)))
    acc = ep(t, C["01.c"], 0.4)
    if acc > 0:
        check_icon(c, 1250, 455, 40, acc, RED, "x")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "valor CERTO", 700, 660, GREEN, ad, 34)
        chip(c, "escrita ERRADA", 1220, 660, RED, ad, 34)
    selo(c, W / 2, 780, ep(t, C["01.e"], 0.5), "ARMADILHA DE PROPÓSITO", AMBER, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    ops = [("×", "multiplicar"), ("÷", "dividir"), ("x^n", "elevar"), ("√{x}", "tirar raiz")]
    for k, (sym, nome) in enumerate(ops):
        a = ep(t, C["02.a"] + 0.35 * k, 0.4)
        if a <= 0:
            continue
        x = 400 + k * 375
        card(c, x - 150, 230, 300, 250, a)
        expr(c, sym, x, 330, 80, a, cores={0: PURPLE})
        text(c, nome, x, 440, 34, "black", INK, a)
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        boxed(c, 400, 590, 1120, 130, GREEN, ab, 0.10)
        text_mid(c, "+ o ÚLTIMO PASSO que a prova adora cobrar", W / 2, 655, 44, "black", GREEN, ab)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        expr(c, "3,84 · 10^8", 560, 300, 90, aa, cores={0: COEF, 2: EXPO})
        text(c, "COEFICIENTE", 470, 400, 26, "black", COEF, aa)
        text(c, "1 algarismo (≠ 0) antes da vírgula", 560, 470, 30, "black", INK, aa)
        expr(c, "1 ≤ a < 10", 560, 560, 50, aa, cores={i: PURPLE for i in range(5)})
    line(c, 960, 230, 960, 800, "#E6E6E2", ep(t, C["03.b"], 0.5), 3)
    expr(c, "10^3 · 10^2 = 10^5", 1370, 330, 60, ep(t, C["03.b"], 0.5), cores={4: GREEN})
    text(c, "multiplicar: SOMA os expoentes", 1370, 420, 30, "black", PURPLE, ep(t, C["03.b"], 0.5))
    expr(c, "10^5 ÷ 10^2 = 10^3", 1370, 580, 60, ep(t, C["03.c"], 0.5), cores={4: GREEN})
    text(c, "dividir: SUBTRAI os expoentes", 1370, 670, 30, "black", PURPLE, ep(t, C["03.c"], 0.5))


# ======================================================================
# bloco A — multiplicar (duas pistas)
# ======================================================================

def b_multiplicar(c, t, C, B):
    head_seq(c, t, C, [("04", "MULTIPLICAR", "AS DUAS PISTAS", BLUE), ("05", "MULTIPLICAR", "UMA PISTA DE CADA VEZ", PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    # contexto: fotos no celular
    rrect(c, 230, 200, 220, 380, 34, INK, a0)
    rrect(c, 246, 230, 188, 320, 18, "#FFFFFF", a0)
    for i in range(3):
        for j in range(4):
            rrect(c, 258 + i * 60, 244 + j * 74, 50, 62, 6, mix(BLUE, "#FFFFFF", 0.3 + 0.15 * ((i + j) % 3)), a0)
    al = a0 * (1 - ep(t, C["05.c"], 0.4)) if "05.c" in C else a0
    expr(c, "3·10^4 fotos", 340, 640, 40, al, cores={0: COEF})
    expr(c, "2·10^6 bytes cada", 340, 710, 34, al, cores={0: COEF})
    expr(c, "(3·10^4) · (2·10^6)", 1100, 250, 64, ep(t, C["04.a"], 0.5))
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        ab = ep(t, C["04.b"], 0.5)
        pistas(c, 600, 360, 1000, "3 · 2", "10^4 · 10^6", ep(t, C["04.c"], 0.5), ep(t, C["04.d"], 0.5))
        text(c, "duas pistas SEPARADAS", 1100, 720, 34, "black", INK2, ab)
        return
    pistas(c, 600, 360, 1000, "3 · 2", "10^4 · 10^6", 1, 1, res_top="= 6", res_bot="= 10^{10}",
           a_res=(ep(t, C["05"] + 1.2, 0.4), ep(t, C["05.a"] + 2.5, 0.4)))
    text(c, "mesma base: SOMA  4 + 6 = 10", 1100, 650, 28, "black", EXPO, ep(t, C["05.a"] + 1.5, 0.5))
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        rrect(c, 760, 690, 680, 90, 18, "#FFFFFF", ab, shadow=True)
        expr(c, "= 6·10^{10} bytes", 1100, 735, 52, ab, cores={1: GREEN})
    K.atalho(c, 160, 610, 400, 210, "ATALHO", ["números com números,", "potências com potências"], ep(t, C["05.c"], 0.5), 28)


# ======================================================================
# bloco B — dividir (sinais em câmera lenta)
# ======================================================================

def b_dividir(c, t, C, B):
    head_seq(c, t, C, [("06", "DIVIDIR", "SUBTRAI OS EXPOENTES", PURPLE), ("07", "DEVAGAR", "MENOS COM MENOS", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    a0 = ep(t, C["06"], 0.5)
    # caixa d'água e copo
    rrect(c, 230, 260, 220, 260, 30, mix("#FFFFFF", BLUE, 0.15), a0)
    rrect(c, 230, 360, 220, 160, 30, mix("#FFFFFF", BLUE, 0.45), a0)
    rrect(c, 250, 230, 180, 40, 14, INK2, a0)
    expr(c, "6·10^3 L", 340, 580, 40, a0, cores={0: COEF})
    pth = skia.Path(); pth.moveTo(500, 380); pth.lineTo(580, 380); pth.lineTo(570, 500); pth.lineTo(510, 500); pth.close()
    c.drawPath(pth, paint(mix("#FFFFFF", BLUE, 0.35), a0))
    expr(c, "2·10^{-1} L", 540, 580, 32, a0, cores={0: COEF})
    text(c, "= 0,2 L", 540, 640, 28, "bold", INK2, a0)
    if sid == "06":
        expr(c, "(6·10^3) ÷ (2·10^{-1})", 1140, 250, 60, ep(t, C["06"], 0.5))
        pistas(c, 680, 360, 940, "6 ÷ 2", "10^3 ÷ 10^{-1}", ep(t, C["06.a"], 0.5), ep(t, C["06.b"], 0.5),
               res_top="= 3", a_res=ep(t, C["06.a"] + 0.8, 0.4))
        ab = ep(t, C["06.b"] + 1.2, 0.5)
        if ab > 0:
            expr(c, "expoente: 3 - (-1)", 1150, 720, 50, ab, cores={0: EXPO, 1: EXPO, 2: EXPO, 3: AMBER, 4: AMBER})
        return
    # câmera lenta: 3 − (−1)
    x0 = 1150
    aa = ep(t, C["07.a"], 0.4)
    toks = ["3", "−", "(−1)"]
    for k, s in enumerate(toks):
        a = ep(t, C["07.a"] + 0.55 * k, 0.4)
        col = INK if k == 0 else AMBER
        fmid(c, s, x0 - 260 + k * 200, 290, 110, "black", col, a)
    abb = ep(t, C["07.b"], 0.5)
    if abb > 0:
        rrect(c, x0 - 120, 220, 340, 150, 26, AMBER, 0.12 * abb)
        arrow(c, x0 + 40, 380, x0 + 40, 470, AMBER, abb, 5, 16, progress=abb)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        fmid(c, "3 + 1 = 4", x0, 540, 100, "black", GREEN, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 820, 640, 660, 90, 18, "#FFFFFF", ad, shadow=True)
        expr(c, "= 3·10^4 copos", 1150, 685, 50, ad, cores={1: GREEN})
        text(c, "30 000", 1150, 770, 28, "bold", INK2, ad)
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        boxed(c, 170, 690, 560, 120, GREEN, ae, 0.10)
        text(c, "ATALHO", 450, 728, 22, "black", GREEN, ae, tracking=2)
        expr(c, "- (-) → +", 450, 775, 44, ae, cores={0: INK, 1: INK, 2: INK, 3: GREEN})


# ======================================================================
# bloco C — renormalizar com a gangorra
# ======================================================================

def b_gangorra(c, t, C, B):
    head_seq(c, t, C, [("08", "O PASSO ESQUECIDO", "RENORMALIZAR", BLUE), ("09", "A GANGORRA", "MESMO VALOR", PURPLE),
                       ("10", "A GANGORRA", "FUNCIONA PARA OS DOIS LADOS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        expr(c, "40 · 10^6", W / 2, 330, 130, aa, cores={0: RED})
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            rrect(c, 640, 250, 210, 160, 24, RED, 0.12 * ab)
            text(c, "2 algarismos antes da vírgula", 745, 470, 30, "black", RED, ab)
            text(c, "ainda NÃO é notação científica", W / 2 + 280, 470, 30, "black", INK2, ab, align="left")
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            boxed(c, 360, 570, 1200, 170, BLUE, acc, 0.08)
            text(c, "RENORMALIZAR", W / 2, 630, 40, "black", BLUE, acc, tracking=2)
            text(c, "reescrever no padrão, sem mudar o valor", W / 2, 690, 36, "bold", INK, acc)
        return
    if sid == "09":
        a0 = ep(t, C["09"], 0.5)
        tb, tc = C["09.b"], C["09.c"]
        ang = tilt(t, tb, 14, -2)
        coef = "40" if t < tb + 0.4 else "4"
        exp_ = "10^6" if t < tc + 0.4 else "10^7"
        gangorra(c, W / 2, 470, ang, coef, exp_, a0, larg=820, size=70)
        ab = ep(t, tb, 0.5)
        if ab > 0:
            text(c, "÷ 10", W / 2 - 520, 300, 40, "black", COEF, ab)
        acc = ep(t, tc, 0.5)
        if acc > 0:
            text(c, "+ 1", W / 2 + 520, 300, 40, "black", EXPO, acc)
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            expr(c, "40·10^6 = 4·10^7", 560, 760, 56, ad, cores={2: GREEN})
        selo(c, 1380, 760, ep(t, C["09.e"], 0.5), "MESMO VALOR", GREEN, -5, 40)
        return
    # 10: o outro lado
    aa = ep(t, C["10.a"], 0.5)
    expr(c, "(3·10^{-4}) ÷ (6·10^{-8})", W / 2, 230, 56, aa)
    pistas(c, 180, 290, 780, "3 ÷ 6", "-4 - (-8)", ep(t, C["10.b"], 0.5), ep(t, C["10.c"], 0.5), h=100, size=46,
           res_top="= 0,5", res_bot="= 4", a_res=ep(t, C["10.c"] + 1.0, 0.4))
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        expr(c, "0,5 · 10^4", 570, 600, 64, ad, cores={0: RED})
        text(c, "pequeno demais: 0 antes da vírgula", 570, 680, 28, "black", RED, ad)
    ae = ep(t, C["10.e"], 0.5)
    ang = tilt(t, C["10.e"], -10, 4)
    gangorra(c, 1370, 400, ang, "0,5" if t < C["10.e"] + 0.5 else "5", "10^4" if t < C["10.e"] + 1.4 else "10^3", ad,
             larg=560, size=52)
    if ae > 0:
        expr(c, "= 5·10^3", 1370, 640, 60, ae, cores={1: GREEN})
    K.atalho(c, 980, 690, 780, 130, "ATALHO", ["o que um lado ganha, o outro perde"], ep(t, C["10.f"], 0.5), 32)


# ======================================================================
# bloco D — potência · bloco E — raiz
# ======================================================================

def b_potencia(c, t, C, B):
    frame(c, t, B["start"], "ELEVAR", "REVISÃO RÁPIDA", PURPLE)
    aa = ep(t, C["11.a"], 0.5)
    expr(c, "(2·10^{-2})^3", W / 2, 280, 110, aa)
    ab = ep(t, C["11.b"], 0.5)
    chip(c, "o de fora entra nos DOIS", W / 2, 410, PURPLE, ab, 32)
    pistas(c, 340, 480, 1240, "2^3 = 8", "(10^{-2})^3 = 10^{-6}", ep(t, C["11.c"], 0.5), ep(t, C["11.d"], 0.5), h=100,
           size=50)
    ad = ep(t, C["11.d"], 0.5)
    text(c, "potência de potência: MULTIPLICA  (−2) · 3 = −6", W / 2, 750, 30, "black", EXPO, ad)
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        rrect(c, 1380, 200, 380, 100, 18, "#FFFFFF", ae, shadow=True)
        expr(c, "= 8·10^{-6}", 1570, 250, 52, ae, cores={1: GREEN})


def b_raiz(c, t, C, B):
    head_seq(c, t, C, [("12", "RAIZ QUADRADA", "O EXPOENTE PRECISA SER PAR", PURPLE), ("13", "A SAÍDA", "A GANGORRA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        expr(c, "√{4,9·10^{-5}}", W / 2, 290, 110, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            expr(c, "√{10^{-6}} = 10^{-3}", 560, 500, 56, ab, cores={2: GREEN})
            text(c, "raiz quadrada: expoente ÷ 2", 560, 590, 30, "black", PURPLE, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            chip(c, "−5 é ÍMPAR", 1360, 440, AMBER, acc, 40)
            text(c, "ímpar: não se divide por 2 em partes inteiras", 1360, 510, 26, "bold", INK2, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            expr(c, "-5 ÷ 2 = -2,5", 1360, 630, 56, ad, cores={4: RED})
            check_icon(c, 1600, 600, 30, ad, RED, "x")
            text(c, "expoente quebrado: não serve", 1360, 720, 28, "black", RED, ad)
        return
    a0 = ep(t, C["13"], 0.5)
    ta, tb = C["13.a"], C["13.b"]
    ang = tilt(t, ta, -6, 10)
    gangorra(c, 560, 380, ang, "4,9" if t < ta + 0.5 else "49", "10^{-5}" if t < tb + 0.4 else "10^{-6}", a0, larg=640, size=58)
    ab = ep(t, tb, 0.5)
    if ab > 0:
        chip(c, "−6 é PAR", 560, 700, GREEN, ab, 36)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        expr(c, "√{49} = 7", 1350, 280, 64, acc, cores={2: GREEN})
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        expr(c, "√{10^{-6}} = 10^{-3}", 1350, 410, 60, ad, cores={2: GREEN})
    ae = ep(t, C["13.e"], 0.5)
    if ae > 0:
        rrect(c, 1130, 480, 440, 100, 18, "#FFFFFF", ae, shadow=True)
        expr(c, "= 7·10^{-3}", 1350, 530, 56, ae, cores={1: GREEN})
    K.atalho(c, 1010, 620, 680, 190, "ATALHO", ["antes da raiz,", "deixe o expoente PAR"], ep(t, C["13.f"], 0.5), 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("15", "VAMOS CONFERIR", "E RENORMALIZE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    expr(c, "(6·10^3) · (5·10^{-7}) = ?", W / 2, 260, 72, aa)
    chip(c, "faça a conta e RENORMALIZE", W / 2, 370, AMBER, ep(t, C["14.b"], 0.5), 32)
    if t < C["15"]:
        pause_timer(c, t, C["14.end"] - 1.9, W / 2, 560)
        return
    pistas(c, 280, 440, 820, "6 · 5", "3 + (-7)", ep(t, C["15.a"], 0.5), ep(t, C["15.b"], 0.5), h=96, size=46,
           res_top="= 30", res_bot="= -4", a_res=1.0)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        expr(c, "30·10^{-4}", 1420, 470, 60, acc, cores={0: AMBER})
        chip(c, "ainda NÃO!", 1420, 560, AMBER, ep(t, C["15.c"] + 1.2, 0.4), 30)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        text(c, "30 ÷ 10  ·  expoente + 1", 1420, 650, 28, "black", PURPLE, ad)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        rrect(c, 1190, 700, 460, 100, 18, "#FFFFFF", ae, shadow=True)
        expr(c, "= 3·10^{-3}", 1420, 750, 56, ae, cores={1: GREEN})


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Multiplicou: soma expoentes. Dividiu: subtrai.", "Fez a conta? Renormalize.", "Raiz quadrada só com expoente par."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        K.para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("Parar em 40 · 10⁶", "o valor está correto e a resposta está nas alternativas",
          "coeficiente passou de 10: renormalize → 4 · 10⁷"),
         ("Errar o sinal: 3 − (−1) = 2", "são dois menos, e a pressa junta tudo num menos só", "menos com menos vira mais: 3 + 1 = 4"),
         ("Multiplicar os expoentes num produto", "os coeficientes foram multiplicados, dá vontade de fazer igual",
          "duas pistas, duas regras: em cima multiplica, embaixo SOMA"),
         ("Tirar a raiz com expoente ímpar", "é só dividir o expoente por 2", "sai quebrado: gangorra antes, expoente PAR, depois a raiz")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19", "20"], ERROS)


# ======================================================================
# questões
# ======================================================================

def enunciado(c, a, linhas, rotulo, y0=230, maxw=640, size=31):
    y = y0
    for k, s in enumerate(linhas):
        col = BLUE if k == len(linhas) - 1 else INK
        y += fpara(c, mat2f(s), 190, y, size, "black", col, a, maxw) + 8
    text(c, rotulo, 190, 822, 18, "medium", GRAY, a, align="left")
    return y


def solucao(c, t, x, y, w, h, rows, a):
    """painel de resolução: rows = [(cue, expr, cores)]"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    n = len(rows)
    for k, (cue, s, cores) in enumerate(rows):
        expr(c, s, x + w / 2, y + 50 + (h - 100) * k / max(1, n - 1), 38, ep(t, cue, 0.4), cores=cores)


ENUN_BACT = ["Uma bactéria tem massa aproximada de 2 · 10^(−12) g. Uma colônia contém cerca de 3 · 10^8 bactérias.",
             "A massa total da colônia, em gramas, é de aproximadamente"]
ALTS_BACT = [("A", "= 6·10^{-20}", "−12 − 8 = −20 (sinal)", RED), ("B", "= 6·10^{-4}", "", GREEN),
             ("C", "= 5·10^{-4}", "somou 2 + 3", RED), ("D", "= 6·10^4", "perdeu o sinal do −12", RED),
             ("E", "= 6·10^{96}", "multiplicou: 12 · 8 = 96", RED)]


def b_q_bact(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO", "AS BACTÉRIAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    enunciado(c, a0, ENUN_BACT, "Questão extra da série (estilo ENEM)")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS_BACT, 890, 200, 800, 38, C["22.ok"], "B", cues_in, cues_x, gap=14)
    if t >= C["22"]:
        solucao(c, t, 170, 480, 680, 320, [(C["22.a"], "2 · 3 = 6", {4: COEF}),
                                           (C["22.b"], "-12 + 8 = -4", {4: EXPO}),
                                           (C["22.c"], "6·10^{-4} g = 0,0006 g", {0: GREEN})], ep(t, C["22"], 0.4))


ENUN_DATA = ["Um data center possui 8 · 10^4 servidores, e cada servidor consome, em média, 5 · 10^2 watts.",
             "A potência total consumida, em watts, é"]
ALTS_DATA = [("A", "= 1,3·10^7", "somou 8 + 5", RED), ("B", "= 4·10^6", "cortou o zero, não subiu o expoente", RED),
             ("C", "= 4·10^7", "", GREEN), ("D", "= 40·10^6", "parou um passo antes", AMBER),
             ("E", "= 4·10^8", "subiu o expoente 2 vezes", RED)]


def b_q_data(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · NÓS FAZEMOS", "O DATA CENTER", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    enunciado(c, a0, ENUN_DATA, "Questão do material de estudo (seção 12)")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"D": C["26.xd"], "A": C["26.xa"], "B": C["26.xb"], "E": C["26.xe"]}
    K.alternativas(c, t, C, ALTS_DATA, 890, 200, 800, 38, C["25.ok"], "C", cues_in, cues_x, gap=14)
    if t >= C["25"]:
        solucao(c, t, 170, 480, 680, 320, [(C["25"], "8 · 5 = 40", {4: COEF}), (C["25.a"], "4 + 2 = 6", {4: EXPO}),
                                           (C["25.c"], "40·10^6 = 4·10^7", {2: GREEN})], ep(t, C["25"], 0.4))
        ab = ep(t, C["25.b"], 0.4) * (1 - ep(t, C["25.c"], 0.4))
        if ab > 0:
            chip(c, "o número do começo da aula!", 510, 445, AMBER, ab, 26)
    elif t >= C["24.p"]:
        chip(c, "1º passo: as duas pistas", 510, 560, GREEN, ep(t, C["24.p"], 0.4), 30)


ENUN_IMP = ["Uma impressora 3D deposita material em camadas de 5 · 10^(−5) metro de espessura. Para produzir uma peça com "
            "2 · 10^(−2) metro de altura,", "o número de camadas necessárias é"]
ALTS_IMP = [("A", "25", "2,5 = 5 ÷ 2: dividiu ao contrário", RED), ("B", "40", "gangorra: desceu demais", RED),
            ("C", "250", "2,5 = 5 ÷ 2: dividiu ao contrário", RED), ("D", "400", "", GREEN),
            ("E", "4 000", "gangorra: não desceu", RED)]


def b_q_imp(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "A IMPRESSORA 3D", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    enunciado(c, a0, ENUN_IMP, "Questão do material de estudo (seção 12)", size=29)
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS_IMP, 890, 210, 800, 40, C["28.ok"], "D", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["27.end"] - 1.9, 510, 640)
    if t < C["28"]:
        return
    sid = which(t, C, ["28", "29"])
    ra = ep(t, C["28"], 0.4)
    rrect(c, 170, 470, 680, 340, 18, "#FFFFFF", ra, shadow=True)
    expr(c, "2 ÷ 5 = 0,4", 510, 520, 38, ep(t, C["28.a"], 0.4), cores={4: COEF})
    if sid == "28":
        # câmera lenta do expoente
        tb = C["28.b"]
        for k, s in enumerate(["−2", "−", "(−5)"]):
            fmid(c, s, 360 + k * 140, 610, 64, "black", AMBER if k else INK, ep(t, tb + 0.7 * k + 0.4, 0.35))
        acc = ep(t, C["28.c"], 0.4)
        if acc > 0:
            expr(c, "-2 + 5 = +3", 510, 700, 50, acc, cores={4: GREEN})
        ad = ep(t, C["28.d"], 0.4)
        if ad > 0:
            expr(c, "0,4·10^3 = 4·10^2 = 400", 510, 775, 36, ad, cores={4: GREEN})
        return
    expr(c, "-2 - (-5) = +3", 510, 610, 44, 1, cores={4: GREEN})
    expr(c, "0,4·10^3 = 4·10^2 = 400", 510, 680, 36, 1, cores={4: GREEN})
    a29 = ep(t, C["29"], 0.4) * (1 - ep(t, C["29.xa"], 0.4))
    if a29 > 0:
        expr(c, "-2 - 5 = -7 → 0,4·10^{-7}", 510, 760, 34, a29, cores={i: RED for i in range(8)})
    ab = ep(t, C["29.xa"], 0.4)
    if ab > 0:
        text(c, "menos de UMA camada: absurdo", 510, 770, 28, "black", RED, ab)


ENUN_PLACA = ["Uma placa quadrada tem área de 1,6 · 10^(−5) m².", "A medida do lado dessa placa, em metros, é"]
ALTS_PLACA = [("A", "= 4·10^{-3}", "", GREEN), ("B", "= 4·10^{-2,5}", "dividiu o ímpar por 2", RED),
              ("C", "= 1,26·10^{-3}", "√1,6 e arredondou o expoente", RED), ("D", "= 8·10^{-3}", "fez 16 ÷ 2", RED),
              ("E", "= 4·10^{-6}", "esqueceu a raiz do 10⁻⁶", RED)]


def b_q_placa(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "A PLACA QUADRADA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    enunciado(c, a0, ENUN_PLACA, "Questão do material de estudo (seção 12)")
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS_PLACA, 890, 200, 800, 38, C["31.ok"], "A", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["30.end"] - 1.9, 510, 600)
    if t < C["31"]:
        # quadradinho da placa
        rrect(c, 420, 420, 180, 180, 6, mix("#FFFFFF", BLUE, 0.2), a0)
        text(c, "lado = ?", 510, 650, 28, "black", BLUE, a0)
        return
    ra = ep(t, C["31"], 0.4)
    rrect(c, 170, 400, 680, 410, 18, "#FFFFFF", ra, shadow=True)
    text(c, "lado = √área", 510, 450, 30, "black", BLUE, ra)
    aa = ep(t, C["31.a"], 0.4)
    if aa > 0:
        expr(c, "1,6·10^{-5}", 510, 520, 44, aa)
        chip(c, "ímpar", 700, 500, AMBER, aa, 22)
    ab = ep(t, C["31.b"], 0.4)
    if ab > 0:
        expr(c, "= 16·10^{-6}", 510, 590, 44, ab, cores={1: GREEN})
    acc = ep(t, C["31.c"], 0.4)
    if acc > 0:
        expr(c, "√{16·10^{-6}} = 4·10^{-3}", 510, 670, 40, acc, cores={2: GREEN})
    ad = ep(t, C["31.d"], 0.4)
    if ad > 0:
        expr(c, "(4·10^{-3})^2 = 16·10^{-6}", 510, 750, 36, ad, cores={2: GREEN})
        check_icon(c, 790, 735, 24, ad, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "SOMAR EM NOTAÇÃO CIENTÍFICA", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        expr(c, "× ÷", 560, 330, 100, aa, cores={0: GREEN, 1: GREEN})
        text(c, "expoentes diferentes: OK", 560, 440, 34, "black", GREEN, aa)
        check_icon(c, 560, 520, 34, aa, GREEN)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        expr(c, "+ −", 1360, 330, 100, ab, cores={0: RED, 1: RED})
        text(c, "expoentes diferentes: NÃO", 1360, 440, 34, "black", RED, ab)
        check_icon(c, 1360, 520, 34, ab, RED, "x")
    acc = ep(t, C["34.c"], 0.5)
    expr(c, "3·10^5 + 8·10^4 = ?", W / 2, 650, 64, acc)
    pill(c, "ep. 3 · somar e comparar grandezas", W / 2, 780, PURPLE, size=32, a=ep(t, C["34.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Você já tinha parado no 40 · 10⁶?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, multiplicar=b_multiplicar, dividir=b_dividir,
              gangorra=b_gangorra, potencia=b_potencia, raiz=b_raiz, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q_bact=b_q_bact, q_data=b_q_data, q_imp=b_q_imp, q_placa=b_q_placa, ponte=b_ponte, cta=b_cta)
