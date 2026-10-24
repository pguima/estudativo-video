"""Visual — Polinômios e Equações Polinomiais, Episódio 2: divisão, Briot-Ruffini e o teorema do resto (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: esteira() (o dispositivo de Briot-Ruffini como esteira: o número desce, é multiplicado pela raiz —
seta curva — e cai somado na casa seguinte, até o resto acender na ponta, verde se for zero; a casa do coeficiente zero
pisca em âmbar), balas() (17 balas para 5 crianças), pedagio() (a cancela do teorema do resto).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum050", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w, expr, math_w = K.ftext, K.ftext_w, K.expr, K.math_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_polinomios_ep2_briot_ruffini_resto.mp4"
CARD_R = K.CARD_R


# ======================================================================
# peças do episódio
# ======================================================================

def fmt(v):
    return f"−{-v}" if v < 0 else str(v)


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


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


def curva(c, x1, y1, x2, y2, col, a, sw=5, curv=-60):
    """seta curva de (x1, y1) a (x2, y2); curv desloca o ponto de controle para cima (negativo) ou para baixo"""
    if a <= 0:
        return
    mx_, my_ = (x1 + x2) / 2, (y1 + y2) / 2 + curv
    p = skia.Path()
    p.moveTo(x1, y1)
    p.quadTo(mx_, my_, x2, y2)
    c.drawPath(p, paint(col, a, stroke=sw))
    ang = math.atan2(y2 - my_, x2 - mx_)
    tri = skia.Path()
    tri.moveTo(x2, y2)
    tri.lineTo(x2 - 22 * math.cos(ang - 0.45), y2 - 22 * math.sin(ang - 0.45))
    tri.lineTo(x2 - 22 * math.cos(ang + 0.45), y2 - 22 * math.sin(ang + 0.45))
    tri.close()
    c.drawPath(tri, paint(col, a))


def esteira(c, t, x0, y0, raiz, coefs, a, p, cw=170, size=54, falta=None, falta_a=0.0, rot_resto=True):
    """dispositivo de Briot-Ruffini. p = [0..1] por coluna (resultado k entra com p[k]); a coluna 0 'desce', as outras
    recebem raiz · resultado anterior (seta curva) e somam. falta = índice do coeficiente zero (pisca em âmbar)."""
    if a <= 0:
        return
    n = len(coefs)
    res = [coefs[0]]
    for cf in coefs[1:]:
        res.append(res[-1] * (raiz or 0) + cf)
    xr = x0 + 170
    xs = [xr + 40 + cw * (k + 0.5) for k in range(n)]
    yc, yp, yl, yb = y0, y0 + 96, y0 + 146, y0 + 214
    x_end = xr + 40 + cw * n + 20
    # trilho da esteira
    rrect(c, x0 - 20, y0 - 70, x_end - x0 + 40, 360, 26, "#FFFFFF", a, shadow=True)
    line(c, xr, y0 - 50, xr, yb + 60, INK2, a, 4)
    line(c, xr, yl, x_end - 10, yl, INK2, a, 4)
    if raiz is not None:
        rrect(c, x0 + 10, yc - 46, 130, 92, 18, mix("#FFFFFF", PURPLE, 0.18), a)
        expr(c, fmt(raiz), x0 + 75, yc, size, a, cores={0: PURPLE})
        text(c, "raiz", x0 + 75, yc + 84, 22, "bold", PURPLE, a)
    else:
        text(c, "?", x0 + 75, yc + 20, size, "black", GRAY, a)
    if falta is not None and falta_a > 0:
        blink = 0.45 + 0.35 * abs(math.sin(t * 4.0))
        rrect(c, xs[falta] - cw / 2 + 12, yc - 44, cw - 24, 88, 16, mix("#FFFFFF", AMBER, 0.45), a * falta_a * blink)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[falta] - cw / 2 + 12, yc - 44, cw - 24, 88), 16, 16),
                    paint(AMBER, a * falta_a, stroke=4))
    for k, cf in enumerate(coefs):
        expr(c, fmt(cf), xs[k], yc, size, a)
    # casa do resto
    xrest = xs[-1] - cw / 2 + 6
    pr = p[-1] if p else 0
    line(c, xrest - 6, yl - 10, xrest - 6, yb + 60, GRAY, a, 3)
    for k in range(n):
        pk = p[k] if k < len(p) else 0
        if pk <= 0:
            continue
        if k == 0:
            if pk < 1:
                arrow(c, xs[0], yc + 40, xs[0], yb - 40, GREEN, a, 4, 14)
        else:
            prod = res[k - 1] * raiz
            expr(c, fmt(prod), xs[k], yp, size * 0.62, a * pk, cores={0: INK2})
            if pk < 1:
                curva(c, xs[k - 1] + 20, yb - 34, xs[k] - 30, yp + 8, PURPLE, a * min(1, pk * 3), 4, -110)
                pill(c, f"× {fmt(raiz)}", (xs[k - 1] + xs[k]) / 2, yp + 40, PURPLE, size=20, a=a * min(1, pk * 3),
                     anchor="center", bounds=(0, 1920))
        last = k == n - 1
        if last:
            col = GREEN if res[k] == 0 else PURPLE
            rrect(c, xs[k] - cw / 2 + 14, yb - 46, cw - 28, 92, 18, mix("#FFFFFF", col, 0.28), a * pk)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xs[k] - cw / 2 + 14, yb - 46, cw - 28, 92), 18, 18),
                        paint(col, a * pk, stroke=4))
            expr(c, fmt(res[k]), xs[k], yb, size, a * pk, cores={0: col})
            if rot_resto:
                text(c, "resto", xs[k], yb + 82, 22, "bold", col, a * pk)
        else:
            expr(c, fmt(res[k]), xs[k], yb, size, a * pk, cores={0: BLUE})
    return xs, yb


def esteira_cues(t, cues, dur=0.6):
    return [ep(t, q, dur) for q in cues]


def balas(c, t, x0, y0, a, prog):
    """17 balas: 5 crianças com 3 cada (prog 0 → 1 distribui) e 2 sobrando"""
    if a <= 0:
        return
    cores = [RED, AMBER, GREEN, BLUE, PURPLE]
    for k in range(5):
        x = x0 + k * 190
        rrect(c, x, y0, 160, 230, 22, "#FFFFFF", a, shadow=True)
        c.drawCircle(x + 80, y0 + 52, 30, paint(mix("#FFFFFF", cores[k], 0.35), a))
        c.drawCircle(x + 80, y0 + 52, 30, paint(cores[k], a, stroke=3))
        for j in range(3):
            aj = clamp(prog * 15 - (k * 3 + j)) * a
            c.drawCircle(x + 40 + j * 40, y0 + 160, 16, paint(cores[(k + j) % 5], aj))
    ar = clamp(prog * 15 - 15 + 2) * a if prog >= 1 else 0
    for j in range(2):
        c.drawCircle(x0 + 5 * 190 + 60 + j * 46, y0 + 160, 16, paint(AMBER, ar or (a if prog >= 1 else 0)))
    if prog >= 1:
        text(c, "sobram", x0 + 5 * 190 + 83, y0 + 220, 24, "bold", AMBER, a)


def pedagio(c, cx, cy, a, aberta=0.0):
    """cancela de pedágio: estrada, cabine e a barra que levanta"""
    if a <= 0:
        return
    rrect(c, cx - 420, cy + 40, 840, 70, 10, "#BDB8AC", a)
    for k in range(6):
        rrect(c, cx - 400 + k * 140, cy + 70, 70, 10, 4, "#FFFFFF", a)
    rrect(c, cx - 60, cy - 120, 120, 160, 14, PURPLE, a, shadow=True)
    text(c, "R$", cx, cy - 30, 40, "black", "#FFFFFF", a)
    ang = -60 * aberta
    c.save()
    c.translate(cx + 60, cy + 10)
    c.rotate(ang)
    rrect(c, 0, -10, 240, 20, 10, RED, a)
    for k in range(3):
        rrect(c, 30 + k * 72, -10, 32, 20, 0, "#FFFFFF", a)
    c.restore()


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "POLINÔMIOS · EPISÓDIO 2", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        linha(c, [("2x³ − x + 5", PURPLE), ("   ÷   ", INK), ("x + 1", BLUE)], 960, 300, 84, aa)
        text(c, "resto = ?", 960, 430, 48, "black", INK2, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        selo(c, 1520, 250, ab * (1 - ep(t, C["01.c"], 0.4)), "armar a conta? NÃO", AMBER, -6, 32)
        pill(c, "troque x por −1", 960, 520, GREEN, size=40, a=ab, anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 460, 590, 1000, 130, 24, mix("#FFFFFF", GREEN, 0.16), acc)
        expr(c, "P(−1) = −2 + 1 + 5 = 4", 960, 655, 60, acc, cores={8: GREEN})
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 700, ad, "PRONTO", GREEN, -6, 46)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "POLINÔMIOS · EP. 2", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "2º episódio da série de POLINÔMIOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    itens = [("02.a", "EM 1 LINHA", "dividir por x − a", PURPLE), ("02.b", "RESTO", "sem dividir", GREEN),
             ("02.c", "O VALOR DE k", "que deixa divisível", AMBER)]
    for k, (cue, tit, sb, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 340, 480, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 240, 340, 480, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 44, "black", col, ak)
        text(c, sb, x, 625, 30, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Divisibilidade", 300, y - 75, BLUE, size=22, a=a)
        linha(c, [("dividendo = divisor · quociente + resto", INK), ("   (resto < divisor)", AMBER)], 960, y, 40, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódio 1", 300, y - 75, PURPLE, size=22, a=a)
        linha(c, [("P(a)", PURPLE), (" = trocar x por a", INK)], 960, y, 50, a)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Sistemas lineares", 300, y - 75, GREEN, size=22, a=a)
        text_mid(c, "2 equações · 2 incógnitas", 960, y, 50, "black", INK, a)


# ======================================================================
# concreto — as balas
# ======================================================================

def b_balas(c, t, C, B):
    head(c, t, B["start"], "DIVISÃO COM RESTO", "17 BALAS PARA 5 CRIANÇAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    prog = clamp((t - C["04.b"]) / 2.4)
    ad = ep(t, C["04.d"], 0.5)
    balas(c, t, 300, 210 - 40 * ad, aa * (1 - 0.0 * ad), prog)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        cores = {0: BLUE, 2: PURPLE, 4: GREEN, 6: AMBER} if ad > 0 else None
        expr(c, "17 = 5 · 3 + 2", 960, 560 - 20 * ad, 80, acc, cores=cores)
    if ad > 0:
        for k, (s_, x, col) in enumerate((("DIVIDENDO", 690, BLUE), ("DIVISOR", 900, PURPLE),
                                          ("QUOCIENTE", 1060, GREEN), ("RESTO", 1250, AMBER))):
            ak = ep(t, C["04.d"] + 1.6 * k, 0.4)
            pill(c, s_, x, 640, col, size=24, a=ak, anchor="center", bounds=(0, 1920))
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        regra(c, "DIVISÍVEL = resto ZERO", 960, 750, ae, 38, PURPLE)


# ======================================================================
# bloco a — a relação e a cara do resto
# ======================================================================

def b_relacao(c, t, C, B):
    head(c, t, B["start"], "A MESMA CONTA", "COM POLINÔMIOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 220, 1200, 150, 26, mix("#FFFFFF", PURPLE, 0.14), aa)
        expr(c, "P(x) = D(x) · Q(x) + R(x)", 960, 295, 70, aa, cores={0: BLUE, 2: PURPLE, 4: GREEN, 6: AMBER})
    ab, d = rise(t, C["05.b"])
    if ab > 0:
        cartao(c, 360, 420 + d, 1200, 120, ab)
        linha(c, [("grau R", AMBER), ("  <  ", INK), ("grau D", PURPLE)], 960, 480 + d, 50, ab)
    acc, d = rise(t, C["05.c"])
    if acc > 0:
        cartao(c, 360, 580 + d, 1200, 170, acc)
        linha(c, [("grau Q", GREEN), (" = grau P − grau D", INK)], 960, 630 + d, 46, acc)
        text(c, "3 − 1 = 2", 960, 715 + d, 40, "black", GREEN, acc)


def b_grau_resto(c, t, C, B):
    head(c, t, B["start"], "A CARA DO RESTO", "DEPENDE DO DIVISOR", PURPLE)
    card(c, *CARD_R)
    for k, (cue, tit, f, r, col) in enumerate((("06.a", "divisor de GRAU 1", "x − 2", "resto = um NÚMERO", BLUE),
                                               ("06.b", "divisor de GRAU 2", "(x−1)(x−2)", "resto = ax + b", PURPLE))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 300 + k * 700
        cartao(c, x, 230 + d, 620, 460, ak)
        text(c, tit, x + 310, 310 + d, 38, "black", col, ak)
        expr(c, f, x + 310, 430 + d, 70, ak)
        pill(c, r, x + 310, 590 + d, col, size=36, a=ak, anchor="center")


# ======================================================================
# bloco b — a esteira
# ======================================================================

def b_esteira_def(c, t, C, B):
    head(c, t, B["start"], "BRIOT-RUFFINI", "DIVIDIR POR x − a EM UMA LINHA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    defin(c, "BRIOT-RUFFINI", "tabelinha que divide por x − a em uma linha", 260, 200, 1400, aa, BLUE, 30)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        defin(c, "RAIZ DO DIVISOR", "o número que zera o divisor (vai à esquerda)", 260, 300, 1400, ab, PURPLE, 30)
    acc = ep(t, C["07.c"], 0.5)
    for k, (dv, rz) in enumerate((("x − 2", "2"), ("x + 3", "−3"))):
        ak = ep(t, C["07.c"] + 2.2 * k, 0.5)
        if ak <= 0:
            continue
        x = 330 + k * 700
        cartao(c, x, 450, 560, 220, ak)
        expr(c, dv, x + 150, 560, 64, ak)
        arrow(c, x + 260, 560, x + 360, 560, PURPLE, ak, 5, 16)
        expr(c, rz, x + 450, 560, 70, ak, cores={0: PURPLE})
    if acc > 0:
        pill(c, "mora do LADO OPOSTO", 960, 740, AMBER, size=36, a=acc, anchor="center")


POLY_B = [2, -3, -5, 6]


def b_esteira(c, t, C, B):
    sid = which(t, C, ["08", "09"])
    head(c, t, B["start"] if sid == "08" else C["09"], "A ESTEIRA",
         "DESCE · MULTIPLICA · SOMA" if sid == "08" else "COMO SE LÊ", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    linha(c, [("2x³ − 3x² − 5x + 6", PURPLE), ("   ÷   ", INK), ("x − 2", BLUE)], 960, 230, 58, a0)
    if sid == "08":
        p = esteira_cues(t, [C["08.a"], C["08.b"], C["08.c"], C["08.d"]])
    else:
        p = [1, 1, 1, 1]
    esteira(c, t, 420, 400, 2, POLY_B, ep(t, C["08.a"] - 0.6, 0.5), p)
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0:
            rrect(c, 590, 670, 510, 4, 2, BLUE, aa)
            linha(c, [("quociente: ", INK2), ("2x² + x − 3", BLUE)], 845, 730, 40, aa)
            pill(c, "um grau a menos", 845, 790, BLUE, size=24, a=aa, anchor="center")
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            selo(c, 1560, 330, acc, "2 É RAIZ", GREEN, -6, 44)


def b_atalho_esteira(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ANTES DE LIGAR A ESTEIRA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · PREPARE A ESTEIRA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, s_) in enumerate((("10.a", "1. TODOS os coeficientes, do maior para o menor expoente"),
                                   ("10.b", "2. à esquerda, a raiz do LADO OPOSTO"),
                                   ("10.c", "3. desce · multiplica pela raiz · soma"))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 360 + k * 150 + d
        rrect(c, 330, y - 55, 1260, 110, 22, "#FFFFFF", ak, shadow=True)
        text(c, s_, 380, y + 14, 38, "black", INK if k < 2 else GREEN, ak, align="left")


# ======================================================================
# bloco c — as duas armadilhas da esteira
# ======================================================================

def b_armadilhas(c, t, C, B):
    head(c, t, B["start"], "ONDE A ESTEIRA TRAVA", "DUAS ARMADILHAS", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("x³", INK), ("  ___  ", AMBER), ("− 4x + 1", INK)], 960, 240, 64, aa)
        pill(c, "falta o x²", 1300, 240, AMBER, size=28, a=aa * (1 - ep(t, C["11.b"], 0.4)), anchor="left",
             bounds=(0, 1920))
    ab = ep(t, C["11.b"], 0.5)
    acc = ep(t, C["11.c"], 0.5)
    esteira(c, t, 420, 430, None, [1, 0, -4, 1], ab * (1 - acc), [], falta=1, falta_a=ab)
    if ab > 0:
        pill(c, "o x² entra com ZERO", 960, 720, AMBER, size=34, a=ab * (1 - acc), anchor="center")
    if acc > 0:
        cartao(c, 460, 380, 1000, 300, acc)
        expr(c, "x + 3", 760, 530, 90, acc)
        arrow(c, 920, 530, 1060, 530, PURPLE, acc, 6, 18)
        expr(c, "−3", 1190, 530, 100, acc, cores={0: PURPLE})
        pill(c, "raiz do LADO OPOSTO", 960, 740, PURPLE, size=34, a=acc, anchor="center")


# ======================================================================
# bloco d — teorema do resto
# ======================================================================

def b_resto(c, t, C, B):
    head(c, t, B["start"], "TEOREMA DO RESTO", "SÓ O RESTO, SEM DIVIDIR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    defin(c, "TEOREMA DO RESTO", "o resto da divisão por x − a é P(a)", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["12.b"], 0.5)
    acc = ep(t, C["12.c"], 0.5)
    if ab > 0:
        z = ep(t, C["12.b"] + 3.0, 0.6)
        expr(c, "P(a) = (a−a)·Q(a) + R", 960, 380, 58, ab * (1 - acc), cores={2: RED})
        if z > 0:
            expr(c, "P(a) = 0·Q(a) + R = R", 960, 500, 58, z * (1 - acc), cores={2: RED, 6: GREEN})
    if acc > 0:
        pedagio(c, 820, 540, acc, ep(t, C["12.c"] + 2.0, 0.8))
        rrect(c, 1180, 380, 420, 150, 22, mix("#FFFFFF", GREEN, 0.16), acc)
        text_mid(c, "substitua a raiz", 1390, 430, 34, "black", INK, acc)
        text_mid(c, "pague só o RESTO", 1390, 485, 36, "black", GREEN, acc)
        pill(c, "o PEDÁGIO", 820, 720, PURPLE, size=32, a=acc, anchor="center")


def b_resto_ex(c, t, C, B):
    head(c, t, B["start"], "VOLTE AO GANCHO", "DOIS CAMINHOS, UM RESTO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        linha(c, [("2x³ − x + 5", PURPLE), ("   ÷   ", INK), ("x + 1", BLUE), ("   →   raiz −1", PURPLE)], 960, 230, 50,
              aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 320, 1400, 110, 22, mix("#FFFFFF", GREEN, 0.14), ab)
        expr(c, "P(−1) = −2 + 1 + 5 = 4", 960, 375, 52, ab, cores={8: GREEN})
    acc = ep(t, C["13.c"], 0.5)
    q = C["13.c"]
    esteira(c, t, 420, 540, -1, [2, 0, -1, 5], acc, [ep(t, q + 0.8 * k, 0.5) for k in range(3)] + [ep(t, C["13.c2"], 0.5)],
            cw=160, size=48, falta=1, falta_a=acc)
    a2 = ep(t, C["13.c2"] + 0.6, 0.5)
    if a2 > 0:
        selo(c, 1580, 640, a2, "BATEM!", GREEN, -6, 40)


def b_atalho_resto(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "RESTO OU QUOCIENTE?", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · O QUE FOI PEDIDO?", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, q, r, col) in enumerate((("14.a", "pediu só o RESTO?", "calcule P(a)", GREEN),
                                          ("14.b", "pediu o QUOCIENTE?", "esteira", PURPLE))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 400 + k * 190 + d
        rrect(c, 340, y - 65, 1240, 130, 22, "#FFFFFF", ak, shadow=True)
        text(c, q, 400, y + 14, 46, "black", INK, ak, align="left")
        pill(c, r, 1520, y, col, size=44, a=ak, anchor="right", bounds=(0, 1920))


# ======================================================================
# bloco e — D'Alembert · bloco f — resto por grau 2
# ======================================================================

def b_dalembert(c, t, C, B):
    head(c, t, B["start"], "D'ALEMBERT", "DIVISÃO EXATA = RAIZ", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 200, 1400, 120, 22, mix("#FFFFFF", BLUE, 0.12), aa)
        linha(c, [("divisível por x − a", BLUE), ("   ⟺   ", INK), ("P(a) = 0", PURPLE), ("   (a é raiz)", INK2)], 960,
              260, 40, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("x³ + kx − 4", PURPLE), ("   ÷   ", INK), ("x − 2", BLUE)], 960, 420, 60, ab)
        text(c, "k = ?", 960, 510, 44, "black", INK2, ab * (1 - ep(t, C["15.c"], 0.4)))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        cartao(c, 360, 480, 1200, 300, acc, GREEN, True)
        expr(c, "P(2) = 8 + 2k − 4 = 0", 960, 560, 54, acc)
        expr(c, "2k = −4", 960, 645, 54, acc)
        expr(c, "k = −2", 960, 730, 62, acc, cores={2: GREEN})


def b_grau2(c, t, C, B):
    head(c, t, B["start"], "DIVISOR DE GRAU 2", "O RESTO É mx + n", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        linha(c, [("P", PURPLE), ("   ÷   ", INK), ("(x − 1)(x − 2)", BLUE), ("   →   ", INK), ("R(x) = mx + n", AMBER)],
              960, 230, 50, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        pill(c, "nas raízes 1 e 2, P e R dão o MESMO valor", 960, 330, PURPLE, size=32, a=ab, anchor="center")
    for k, (dt, f) in enumerate(((0.0, "R(1) = m + n = 5"), (3.4, "R(2) = 2m + n = 7"))):
        ak, d = rise(t, C["16.c"] + dt)
        if ak <= 0:
            continue
        y = 450 + k * 120 + d
        cartao(c, 460, y - 50, 1000, 100, ak)
        expr(c, f, 960, y, 50, ak)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 680, 1000, 110, 22, mix("#FFFFFF", GREEN, 0.18), ad)
        linha(c, [("m = 2,  n = 3   →   ", INK), ("R(x) = 2x + 3", GREEN)], 960, 735, 46, ad)
    text(c, "Exemplo nosso", 190, 822, 18, "medium", GRAY, aa, align="left")


def b_atalho_sistema(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "SUBTRAIA AS EQUAÇÕES", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["17"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · O n SOME", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        expr(c, "(2m+n) − (m+n) = 7 − 5", 960, 400, 58, aa)
        expr(c, "m = 2", 960, 500, 66, aa, cores={2: GREEN})
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        pill(c, "confira: R(1) = 5 e R(2) = 7", 960, 640, GREEN, size=36, a=ab, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "ESTEIRA E TEOREMA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    linha(c, [("x³ − 4x + 1", PURPLE), ("   ÷   ", INK), ("x − 1", BLUE)], 960, 230, 58, aa)
    ab = ep(t, C["18.b"], 0.5)
    sol = t >= C["19"]
    if not sol:
        if ab > 0:
            pill(c, "esteira + confira com P(1)", 960, 330, GREEN, size=32, a=ab, anchor="center")
        pause_timer(c, t, C["18.end"] - 1.9, 960, 560)
        return
    a1 = ep(t, C["19.a"], 0.5)
    p = esteira_cues(t, [C["19.b"], C["19.b2"], C["19.b3"], C["19.b4"]])
    esteira(c, t, 420, 400, 1, [1, 0, -4, 1], a1, p, falta=1, falta_a=a1 * (1 - p[1]))
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        linha(c, [("quociente: ", INK2), ("x² + x − 3", BLUE), ("      resto: ", INK2), ("−2", PURPLE)], 960, 730, 40, acc)
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0:
        rrect(c, 1370, 380, 330, 170, 18, mix("#FFFFFF", GREEN, 0.18), ad)
        expr(c, "P(1) = 1 − 4 + 1", 1535, 430, 30, ad)
        expr(c, "= −2", 1535, 495, 40, ad, cores={1: GREEN})
        selo(c, 1540, 610, ad, "BATEU!", GREEN, -6, 36)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["O resto por x − a é P(a).",
          "Desce, multiplica pela raiz, soma.",
          "Não pule o zero; x + 3 usa −3."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "30"])
    frame(c, t, B["start"] if sid == "20" else C["30"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("sem o zero: x³ − 4x + 1 por x − 2 com 1, −4, 1 → resto −3",
          "o zero não aparece escrito no polinômio",
          "a casa do x² existe: 1, 0, −4, 1 dá resto 1 · e P(2) = 1 confirma."),
         ("dividir por x + 3 usando 3: x² + 2x − 5 → P(3) = 10",
          "o 3 está escrito ali, à vista",
          "a raiz mora do lado oposto: P(−3) = −2."),
         ("resto por x − a = P(−a): x² − 3x + 4 por x − 2 → P(−2) = 14",
          "a pessoa decorou que \"o sinal troca\"",
          "troca mesmo: x − 2 mora em +2. O resto é P(2) = 2.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questão 2 (eu faço) e questão 9 (você faz)
# ======================================================================

ALTS2 = [("A", "= −15", "parou em 3k", RED), ("B", "= −13", "usou P(−3)", RED), ("C", "= −5", "", GREEN),
         ("D", "= 5", "sinal no fim", RED), ("E", "= 13", "os dois erros", RED)]


def b_q2(c, t, C, B):
    sid = which(t, C, ["24", "25", "26"])
    heads = {"24": "DIVISÍVEL: ACHE O k", "25": "EU FAÇO", "26": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "24" else C[sid], "QUESTÃO 2 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1250, 250, 440, 40, C["25.ok"], "C", cues_in, cues_x, gap=34)
    a0 = ep(t, C["24.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        expr(c, "P(x) = x^3 − 2x^2 + kx + 6", 660, 270, 46, a0, cores={6: AMBER})
        linha(c, [("divisível por ", INK), ("x − 3", BLUE), ("   ·   k = ?", INK)], 660, 360, 36, a0)
    if sid == "24":
        return
    aa = ep(t, C["25.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 420, 860, 80, 18, mix("#FFFFFF", PURPLE, 0.14), aa)
        linha(c, [("raiz 3  ·  D'Alembert: ", INK), ("P(3) = 0", PURPLE)], 660, 460, 36, aa)
    ab = ep(t, C["25.b"], 0.5)
    if ab > 0:
        expr(c, "27 − 18 + 3k + 6 = 0", 660, 560, 42, ab)
        expr(c, "3k = −15", 660, 630, 42, ab)
    acc = ep(t, C["25.c"], 0.5)
    if acc > 0:
        expr(c, "k = −5", 660, 710, 52, acc, cores={2: GREEN})
    ad = ep(t, C["25.d"], 0.5) * (1 - ep(t, C["26"], 0.4))
    if ad > 0:
        pill(c, "confere: 27 − 18 − 15 + 6 = 0", 660, 780, GREEN, size=26, a=ad, anchor="center")


ALTS9 = [("A", "= −3", "somou os restos", RED), ("B", "= 3x", "", GREEN), ("C", "= −18", "multiplicou", RED),
         ("D", "= 3x − 6", "−6 no termo indep.", RED), ("E", "= −3x − 3", "raízes trocadas", RED)]


def b_q9(c, t, C, B):
    sid = which(t, C, ["27", "28", "29"])
    heads = {"27": "VOCÊ FAZ", "28": "VAMOS CONFERIR", "29": "AS ERRADAS"}
    head(c, t, B["start"] if sid == "27" else C[sid], "QUESTÃO 9 · ESTILO ENEM", heads[sid], GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS9, 1250, 250, 440, 38, C["28.ok"], "B", cues_in, cues_x, gap=32)
    a0 = ep(t, C["27.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        linha(c, [("P ÷ ", INK), ("(x − 1)", BLUE), ("  →  resto ", INK), ("3", PURPLE)], 660, 250, 38, a0)
        linha(c, [("P ÷ ", INK), ("(x + 2)", BLUE), ("  →  resto ", INK), ("−6", PURPLE)], 660, 320, 38, a0)
        linha(c, [("P ÷ ", INK), ("(x − 1)(x + 2)", BLUE), ("  →  resto ?", AMBER)], 660, 400, 38, a0)
    if sid == "27":
        adi = ep(t, C["27.dica"], 0.5)
        if adi > 0:
            pill(c, "DICA: o resto é mx + n", 660, 500, GREEN, size=32, a=adi, anchor="center")
        pause_timer(c, t, C["27.end"] - 1.9, 660, 650)
        return
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        pill(c, "raízes do divisor: 1 e −2", 660, 480, PURPLE, size=28, a=aa, anchor="center")
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        expr(c, "m + n = 3", 660, 560, 42, ab)
        expr(c, "−2m + n = −6", 660, 625, 42, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        linha(c, [("3m = 9  →  ", INK), ("m = 3,  n = 0", GREEN)], 660, 700, 40, acc)
    ad = ep(t, C["28.d"], 0.5)
    if ad > 0:
        rrect(c, 430, 740, 460, 70, 16, mix("#FFFFFF", GREEN, 0.18), ad)
        text_mid(c, "R(x) = 3x", 660, 775, 40, "black", GREEN, ad)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "CAÇANDO RAÍZES", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        cartao(c, 300, 230, 1320, 220, aa)
        text(c, "lucro da fábrica", 960, 290, 30, "bold", INK2, aa)
        expr(c, "L(x) = x^3 − 6x^2 + 11x − 6", 960, 360, 60, aa)
        pill(c, "zera em x = 1", 960, 450, GREEN, size=30, a=aa, anchor="center")
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        text(c, "e os OUTROS DOIS valores?", 960, 560, 46, "black", INK, ab)
    acc = ep(t, C["31.c"], 0.5)
    if acc > 0:
        pill(c, "com a ESTEIRA de hoje", 960, 650, PURPLE, size=40, a=acc, anchor="center")
    ad = ep(t, C["31.d"], 0.5)
    if ad > 0:
        selo(c, 960, 770, ad, "PRÓXIMO EPISÓDIO", PURPLE, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já tinha usado o teorema do resto?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, balas=b_balas, relacao=b_relacao,
              grau_resto=b_grau_resto, esteira_def=b_esteira_def, esteira=b_esteira, atalho_esteira=b_atalho_esteira,
              armadilhas=b_armadilhas, resto=b_resto, resto_ex=b_resto_ex, atalho_resto=b_atalho_resto,
              dalembert=b_dalembert, grau2=b_grau2, atalho_sistema=b_atalho_sistema, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q2=b_q2, q9=b_q9, ponte=b_ponte, cta=b_cta)
