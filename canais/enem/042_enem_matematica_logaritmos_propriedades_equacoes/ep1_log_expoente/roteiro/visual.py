"""Visual — Logaritmos, Episódio 1: logaritmo é um expoente (definição, condições e consequências) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: lrow() (linha com "log" e a base em subscrito, junto com expr e texto), balao() (a pergunta
"b elevado a quanto dá a?"), regua10() (régua de potências de 10 com os logs embaixo), digitos() (contador de algarismos
acendendo, uma caixinha por algarismo), pot_log() (10 elevado a "log 7").
Cores com função: azul = definição / base · roxo = regra / expoente · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum042", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_logaritmos_ep1_log_expoente.mp4"
CARD_R = K.CARD_R


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


def mx(c, s, cx, cy, size, a, col=None, align="center"):
    """expressão matemática de uma cor só (potências, frações)"""
    n = len(s.split())
    return K.expr(c, s, cx, cy, size, a, cores={i: col or INK for i in range(n)}, align=align)


def _pw(p, size):
    k = p[0]
    if k == "log":
        w = ftext_w("log", "black", size)
        return w + (ftext_w(p[1], "black", size * 0.58) + size * 0.04 if p[1] else 0)
    if k == "m":
        return K.math_w(p[1], size)
    return ftext_w(p[1], "black", size)


def lrow(c, partes, cx, cy, size, a, align="center", gap=None):
    """linha com logs: partes = [("log", base, cor[, cor_base]), ("m", expr, cor), ("t", texto, cor)].
    A base vai em subscrito; base "" = log decimal. Devolve a largura."""
    gap = size * 0.26 if gap is None else gap
    ws = [_pw(p, size) for p in partes]
    total = sum(ws) + gap * (len(partes) - 1)
    if a <= 0:
        return total
    x = cx - total / 2 if align == "center" else (cx - total if align == "right" else cx)
    for p, w_ in zip(partes, ws):
        col = p[2] if len(p) > 2 and p[2] else INK
        if p[0] == "log":
            ftext(c, "log", x, cy + size * 0.36, size, "black", col, a, align="left")
            if p[1]:
                cb = p[3] if len(p) > 3 else col
                ftext(c, p[1], x + ftext_w("log", "black", size) + size * 0.04, cy + size * 0.62, size * 0.58, "black",
                      cb, a, align="left")
        elif p[0] == "m":
            mx(c, p[1], x, cy, size, a, col, align="left")
        else:
            ftext(c, p[1], x, cy + size * 0.36, size, "black", col, a, align="left")
        x += w_ + gap
    return total


def logtxt(c, partes, cx, cy, size, a):
    """"log" seguido de texto colorido por trecho, centrado"""
    wl = ftext_w("log ", "black", size)
    wt = sum(ftext_w(s_, "black", size) for s_, _ in partes)
    x = cx - (wl + wt) / 2
    if a > 0:
        ftext(c, "log ", x, cy + size * 0.36, size, "black", INK, a, align="left")
        linha(c, partes, x + wl, cy, size, a, align="left")


def balao(c, s, cx, cy, a, size=40, col=None, w=None):
    """balão de pergunta com rabinho para baixo"""
    if a <= 0:
        return
    col = col or BLUE
    w = w or ftext_w(s, "black", size) + 80
    h = size + 56
    rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, col, a * 0.12)
    path = skia.Path()
    path.moveTo(cx - 26, cy + h / 2 - 2); path.lineTo(cx, cy + h / 2 + 30); path.lineTo(cx + 26, cy + h / 2 - 2)
    c.drawPath(path, paint(mix("#FFFFFF", col, 0.12), a))
    fmid(c, s, cx, cy, size, col, a)


def fmid(c, s, cx, cy, size, col, a):
    K.fmid(c, s, cx, cy, size, "black", col, a)


REGUA = [("0,01", "−2"), ("0,1", "−1"), ("1", "0"), ("10", "1"), ("100", "2"), ("1 000", "3")]


def regua10(c, x0, y, w, a, destaques=None, setas=0.0):
    """régua de potências de 10 com os logs embaixo; destaques = {índice: (alfa, cor)}"""
    if a <= 0:
        return
    n = len(REGUA)
    dx = w / (n - 1)
    line(c, x0 - 30, y, x0 + w + 30, y, INK2, a, 5)
    pill(c, "número", x0 - 60, y - 70, INK2, size=20, a=a, anchor="right", bounds=(0, 1920))
    pill(c, "log", x0 - 60, y + 80, PURPLE, size=20, a=a, anchor="right", bounds=(0, 1920))
    for k, (num, lg) in enumerate(REGUA):
        x = x0 + k * dx
        da, dc = (destaques or {}).get(k, (0, GREEN))
        if da > 0:
            rrect(c, x - 90, y - 120, 180, 250, 22, dc, a * da * 0.14)
        line(c, x, y - 16, x, y + 16, INK2, a, 5)
        text(c, num, x, y - 50, 40, "black", mix(INK, dc, da), a)
        text(c, lg, x, y + 92, 44, "black", mix(PURPLE, dc, da), a)
        if setas > 0 and k < n - 1:
            path = skia.Path()
            path.moveTo(x + 24, y - 100); path.quadTo(x + dx / 2, y - 150, x + dx - 24, y - 100)
            c.drawPath(path, paint(GREEN, a * setas, stroke=4, cap_round=True))
            text(c, "×10", x + dx / 2, y - 140, 22, "black", GREEN, a * setas)
            text(c, "+1", x + dx / 2, y + 150, 22, "black", GREEN, a * setas)


def digitos(c, s, cx, cy, a, acesos=99.0, size=60, col=None, bw=None):
    """um número em caixinhas, uma por algarismo; acesos = quantas já acenderam (float). Devolve a largura."""
    col = col or GREEN
    bw = bw or size * 0.9
    n = len(s)
    w = n * bw + (n - 1) * 8
    if a <= 0:
        return w
    x = cx - w / 2
    for k, ch in enumerate(s):
        u = clamp(acesos - k)
        rrect(c, x, cy - size * 0.75, bw, size * 1.5, 12, mix("#FFFFFF", col, 0.10 + 0.20 * u), a, shadow=True)
        text_mid(c, ch, x + bw / 2, cy, size, "black", mix(INK2, col, u), a)
        x += bw + 8
    return w


def pot_log(c, base, arg, cx, cy, size, a, col=None, align="center"):
    """base elevada a "log arg" (o expoente é escrito com o texto do log)"""
    col = col or INK
    wb = ftext_w(base, "black", size)
    we = ftext_w(f"log {arg}", "black", size * 0.6)
    tw = wb + we + size * 0.06
    if a <= 0:
        return tw
    x = cx - tw / 2 if align == "center" else cx
    ftext(c, base, x, cy + size * 0.36, size, "black", col, a, align="left")
    ftext(c, f"log {arg}", x + wb + size * 0.06, cy - size * 0.18, size * 0.6, "black", PURPLE, a, align="left")
    return tw


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, size, a, align="left")


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "LOGARITMOS · EPISÓDIO 1", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        cartao(c, 220, 230, 760, 330, aa)
        mx(c, "2^{100}", 600, 360, 150, aa, PURPLE)
        text(c, "quantos algarismos?", 600, 520, 36, "black", INK2, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        # a conta na mão que ninguém faz: caixinhas com "?"
        for k in range(10):
            ak = ab * ep(t, C["01.b"] + 0.12 * k, 0.2)
            rrect(c, 1060 + (k % 5) * 130, 250 + (k // 5) * 140, 110, 120, 14, mix("#FFFFFF", RED, 0.10), ak)
            text_mid(c, "?", 1115 + (k % 5) * 130, 310 + (k // 5) * 140, 64, "black", RED, ak)
        selo(c, 1380, 560, ab, "NA MÃO? NEM PENSAR", RED, -4, 30)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 640, 760, 150, 26, mix("#FFFFFF", GREEN, 0.12), acc, shadow=True)
        lrow(c, [("log", "", GREEN), ("m", "2 ≈ 0,301", GREEN)], 740, 715, 70, acc)
        ak = ep(t, C["01.c"] + 2.6, 0.4)
        if ak > 0:
            rrect(c, 1220, 650, 340, 130, 26, "#FFFFFF", ak, shadow=True)
            u = clamp((t - C["01.c"] - 2.6) / 2.0)
            c.drawArc(skia.Rect.MakeXYWH(1250, 670, 90, 90), -90, 360 * u, False, paint(GREEN, ak, stroke=10, cap_round=True))
            text(c, "10 s", 1450, 735, 56, "black", GREEN, ak)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "AO FINAL DESTA AULA, VOCÊ TAMBÉM", W / 2, 840, ad, 34, GREEN)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "LOGARITMOS · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de LOGARITMOS", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "LER COMO PERGUNTA", "qualquer logaritmo", BLUE), ("02.b", "QUANDO EXISTE", "as condições", PURPLE),
             ("02.c", "CONTAR ALGARISMOS", "com um único log", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 34, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "QUATRO LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a0 = ep(t, C["03"], 0.4)
    if a0 > 0:
        pill(c, "série de Potenciação e radiciação", W / 2, 230, BLUE, size=24, a=a0, anchor="center")
    itens = [("03.a", "2^5 = 32", "", BLUE), ("03.b", "3^{-2} = 1/9", "negativo INVERTE", PURPLE),
             ("03.c", "9^{1/2} = √{9} = 3", "1/2 é raiz quadrada", PURPLE), ("03.d", "a^0 = 1", "qualquer base ≠ 0", BLUE)]
    for k, (cue, s_, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 250 + (k % 2) * 720
        y = 290 + (k // 2) * 270
        cartao(c, x, y, 680, 230, ak)
        mx(c, s_, x + 340, y + 100, 72, ak, col)
        if sub:
            text(c, sub, x + 340, y + 200, 26, "black", INK2, ak)


def b_prereq10(c, t, C, B):
    frame(c, t, B["start"], "POTÊNCIAS DE 10", "SÉRIE DE NOTAÇÃO CIENTÍFICA", GREEN)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        cartao(c, 260, 260, 1400, 230, aa)
        mx(c, "10^n =", 560, 375, 84, aa, BLUE)
        linha(c, [("1", INK), ("000…0", BLUE)], 1050, 360, 84, aa)
        text(c, "n zeros", 1110, 455, 28, "black", BLUE, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        cartao(c, 260, 540, 1400, 260, ab)
        mx(c, "10^{-2} =", 640, 670, 84, ab, PURPLE)
        linha(c, [("0,", INK), ("0", PURPLE), ("1", PURPLE)], 1100, 655, 96, ab)
        text(c, "2 casas decimais", 1100, 760, 28, "black", PURPLE, ab)


# ======================================================================
# bloco a — a pergunta aberta · bloco b — definição
# ======================================================================

def b_aberta(c, t, C, B):
    head(c, t, B["start"], "A PERGUNTA QUE FICOU NO AR", "SÉRIE DE FUNÇÃO EXPONENCIAL", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["05"], 0.4)
    if a0 > 0:
        mx(c, "2^? = 10", W / 2, 260, 96, a0, INK)
    # reta dos expoentes de 2 a 5, com as potências em cima
    x0, x1, y = 360, 1560, 560
    dx = (x1 - x0) / 3
    aa, ab = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5)
    if aa > 0:
        line(c, x0 - 60, y, x1 + 60, y, INK2, aa, 5)
        for k, e in enumerate((2, 3, 4, 5)):
            line(c, x0 + k * dx, y - 14, x0 + k * dx, y + 14, INK2, aa, 4)
            text(c, str(e), x0 + k * dx, y + 60, 34, "black", PURPLE, aa)
        pill(c, "expoente", x0 - 70, y + 50, PURPLE, size=20, a=aa, anchor="right", bounds=(0, 1920))
        for k, (e, v) in enumerate(((2, "4"), (3, "8"), (4, "16"), (5, "32"))):
            ak = aa if v in ("4", "8") else (ab if v == "16" else ab * 0.6)
            if ak > 0:
                chip(c, v, x0 + k * dx, y - 90, BLUE if v != "8" and v != "16" else (AMBER if v == "8" else RED), ak,
                     size=40, w=120)
        pill(c, "8: POUCO", x0 + dx, y - 170, AMBER, size=24, a=aa, anchor="center")
    if ab > 0:
        pill(c, "16: PASSOU", x0 + 2 * dx, y - 170, RED, size=24, a=ab, anchor="center")
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, x0 + dx, y - 22, dx, 44, 22, GREEN, acc * 0.25)
        c.drawCircle(x0 + dx * 1.32, y, 16, paint(GREEN, acc))
        text(c, "10", x0 + dx * 1.32, y - 90, 44, "black", GREEN, acc)
        text(c, "entre 3 e 4 · não é inteiro", W / 2, y + 140, 32, "black", GREEN, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1500, 290, ad, "TEM NOME: LOGARITMO", BLUE, 5, 32)


def b_definicao(c, t, C, B):
    head(c, t, B["start"], "O LOGARITMO", "DEFINIÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        defin(c, "LOGARITMO", "o expoente que falta", 560, 200, 800, aa, BLUE, 32)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 320, 1400, 220, 30, mix("#FFFFFF", BLUE, 0.06), ab)
        lrow(c, [("log", "b", INK, BLUE), ("m", "a", GREEN), ("m", "= x", PURPLE)], 650, 430, 110, ab)
        text_mid(c, "⇔", 1000, 430, 90, "black", INK2, ab)
        K.expr(c, "b^x = a", 1340, 430, 110, ab, cores={0: BLUE, 2: GREEN})
    for k, (cue, nome, sub, col, xx) in enumerate((("06.c", "BASE  b", "o número que vai ser elevado", BLUE, 400),
                                                   ("06.d", "LOGARITMANDO  a", "o número que você quer alcançar", GREEN, 960),
                                                   ("06.e", "LOGARITMO  x", "o expoente que leva até lá", PURPLE, 1520))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        rrect(c, xx - 250, 600, 500, 180, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, xx - 250, 600, 500, 60, 22, col, ak * 0.16)
        text(c, nome, xx, 645, 30, "black", col, ak)
        for j, ln in enumerate(K.wrap(sub, "bold", 26, 440)):
            text(c, ln, xx, 710 + j * 36, 26, "bold", INK2, ak)


def b_pergunta(c, t, C, B):
    head(c, t, B["start"], "LEIA COMO PERGUNTA", "O EXPOENTE COM NOME PRÓPRIO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    aa = ep(t, C["07.a"], 0.5)
    # a expressão sobe e vira balão
    yexp = 300 - 60 * aa
    lrow(c, [("log", "2", INK, BLUE), ("m", "32", GREEN)], 560, yexp, 100, a0)
    ad0 = ep(t, C["07.d"] + 2.6, 0.4)
    if aa > 0:
        balao(c, "2 elevado a quanto dá 32?", 1250, 250, aa * (1 - ad0), 40, BLUE)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        vals = ["2", "4", "8", "16", "32"]
        for k, v in enumerate(vals):
            ak = ep(t, C["07.b"] + 0.7 + 0.55 * k, 0.3)
            x = 380 + k * 290
            chip(c, "2", x, 450, BLUE, ak, size=48, w=110)
            if k > 0:
                text(c, "×", x - 145, 465, 44, "black", GRAY, ak)
            text(c, v, x, 560, 44, "black", GREEN if v == "32" else INK2, ak)
            badge_num(c, k + 1, x, 625, ak, 20, bg=PURPLE)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 1080, 640, 560, 130, 24, mix("#FFFFFF", PURPLE, 0.12), acc)
        linha(c, [("cinco fatores 2", INK), ("  →  log = ", INK2), ("5", PURPLE)], 1360, 705, 44, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 230, 650, 800, 150, 24, "#FFFFFF", ad, shadow=True)
        lrow(c, [("log", "2", INK, BLUE), ("m", "32 = 5", INK)], 450, 725, 50, ad)
        K.expr(c, "2^5 = 32", 860, 725, 50, ad, cores={0: BLUE, 2: GREEN})
        arrow(c, 610, 690, 720, 690, GREEN, ad, 4, 14)
        arrow(c, 720, 760, 610, 760, GREEN, ad, 4, 14)
        selo(c, 1250, 250, ad0, "EXPOENTE COM NOME PRÓPRIO", PURPLE, -3, 30)


# ======================================================================
# bloco c — a tabela · bloco d — notações · atalho
# ======================================================================

def _linha_tab(c, y, partes_log, pergunta, valor, a, av, col=PURPLE):
    rrect(c, 200, y, 1520, 150, 22, "#FFFFFF", a, shadow=True)
    lrow(c, partes_log, 420, y + 75, 64, a)
    text_mid(c, pergunta, 1010, y + 75, 32, "bold", INK2, a)
    if av > 0:
        rrect(c, 1400, y + 20, 280, 110, 20, mix("#FFFFFF", col, 0.14), av)
        mx(c, valor, 1540, y + 75, 64, av, col)


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "RESPOSTA NEGATIVA OU FRAÇÃO", "A TABELA, LINHA A LINHA", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    if a0 > 0:
        for txt_, x in (("LOGARITMO", 420), ("PERGUNTA", 1010), ("VALOR", 1540)):
            text(c, txt_, x, 240, 24, "black", GRAY, a0, tracking=2)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        _linha_tab(c, 280, [("log", "3", INK, BLUE), ("m", "(1/9)", GREEN)], "3 elevado a quanto dá 1/9?", "-2", aa,
                   ep(t, C["08.a"] + 3.4, 0.4))
        pill(c, "1/9 = base invertida: 3⁻²", 1010, 455, PURPLE, size=22, a=ep(t, C["08.a"] + 3.4, 0.4), anchor="center")
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        _linha_tab(c, 520, [("log", "9", INK, BLUE), ("m", "3", GREEN)], "9 elevado a quanto dá 3?", "1/2", ab,
                   ep(t, C["08.b"] + 3.2, 0.4))
        pill(c, "3 = √9 → expoente 1/2", 1010, 695, PURPLE, size=22, a=ep(t, C["08.b"] + 3.2, 0.4), anchor="center")


def b_notacao(c, t, C, B):
    head(c, t, B["start"], "SEM BASE ESCRITA", "O LOG DECIMAL", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        defin(c, "LOG DECIMAL", "sem base escrita, a base é 10", 260, 200, 900, aa, BLUE, 30)
        rrect(c, 1220, 200, 440, 70, 18, mix("#FFFFFF", BLUE, 0.06), aa)
        lrow(c, [("log", "", INK), ("m", "a", GREEN), ("t", "=", INK2), ("log", "10", INK, BLUE), ("m", "a", GREEN)],
             1440, 235, 40, aa)
    ab, acc = ep(t, C["09.b"], 0.5), ep(t, C["09.c"], 0.5)
    regua10(c, 420, 560, 1100, ab, {5: (ep(t, C["09.b"] + 1.4, 0.4), GREEN), 0: (ep(t, C["09.c"] + 1.6, 0.4), PURPLE)})
    if ab > 0:
        lrow(c, [("log", "", INK), ("m", "1 000 = 3", INK)], 640, 350, 48, ep(t, C["09.b"] + 1.4, 0.4))
    if acc > 0:
        lrow(c, [("log", "", INK), ("m", "0,01 = -2", INK)], 1280, 350, 48, ep(t, C["09.c"] + 1.6, 0.4))
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 760, 1200, 70, 35, mix("#FFFFFF", GRAY, 0.10), ad)
        linha(c, [("ln", BLUE), (" = logaritmo natural · base e ≈ 2,718 · ", INK2), ("por enquanto, só o nome", GRAY)],
              W / 2, 795, 28, ad)


def b_atalho_zeros(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O LOG DECIMAL CONTA ZEROS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.4)
    K.atalho(c, 240, 200, 1440, 130, "ATALHO", ["o log decimal conta zeros"], a0, 40)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        cartao(c, 240, 370, 700, 200, aa)
        logtxt(c, [("1", INK), ("00 000", GREEN), (" = ", INK2), ("5", GREEN)], 590, 450, 56, aa)
        text(c, "5 zeros", 590, 535, 28, "black", GREEN, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        cartao(c, 980, 370, 700, 200, ab)
        logtxt(c, [("0,", INK), ("001", PURPLE), (" = ", INK2), ("−3", PURPLE)], 1330, 450, 56, ab)
        text(c, "3 casas decimais, até o 1", 1330, 535, 28, "black", PURPLE, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        regua10(c, 520, 720, 900, acc, setas=ep(t, C["10.c"] + 1.0, 0.5))


# ======================================================================
# bloco e — condições de existência
# ======================================================================

def b_existe(c, t, C, B):
    head(c, t, B["start"], "TODO LOG EXISTE?", "CONDIÇÃO DE EXISTÊNCIA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        defin(c, "CONDIÇÃO DE EXISTÊNCIA", "a regra que diz quando o log existe", 260, 200, 1400, aa, BLUE, 30)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 300, 620, 140, 24, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "1ª: LOGARITMANDO", 570, 345, 28, "black", PURPLE, ab)
        mx(c, "a > 0", 570, 400, 56, ab, PURPLE)
    acc = ep(t, C["11.c"], 0.5)
    # gráfico de 10^x sempre acima do eixo
    x0, y0, w, h = 990, 300, 640, 420
    if acc > 0:
        line(c, x0, y0 + h - 60, x0 + w, y0 + h - 60, INK2, acc, 4)
        line(c, x0 + w * 0.55, y0, x0 + w * 0.55, y0 + h, INK2, acc, 4)
        text(c, "x", x0 + w + 20, y0 + h - 30, 24, "black", GRAY, acc)
        path = skia.Path()
        for k in range(121):
            x = -3 + 4.2 * k / 120
            y = 10 ** x
            px, py = x0 + w * 0.55 + x * 110, y0 + h - 60 - min(y, 18) * 19
            (path.moveTo if k == 0 else path.lineTo)(px, py)
        c.drawPath(path, paint(BLUE, acc, stroke=7, cap_round=True))
        pill(c, "10ˣ: sempre POSITIVO", x0 + 30, y0 + 30, BLUE, size=24, a=acc, bounds=(0, 1920))
        for k, s_ in enumerate(("10^x = 0", "10^x = -5")):
            ak = ep(t, C["11.c"] + 2.4 + 1.2 * k, 0.4)
            y = 500 + k * 110
            rrect(c, 260, y, 620, 90, 18, "#FFFFFF", ak, shadow=True)
            mx(c, s_, 520, y + 45, 46, ak, RED)
            check_icon(c, 800, y + 45, 26, ak, RED, "x")
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 730, 1400, 90, 22, mix("#FFFFFF", RED, 0.10), ad)
        lrow(c, [("log", "", RED), ("m", "0", RED), ("t", "e", INK2), ("log", "", RED), ("m", "(-5)", RED),
                 ("t", "NÃO EXISTEM", RED)], W / 2, 775, 44, ad)


def b_existe2(c, t, C, B):
    head(c, t, B["start"], "E A BASE?", "E A RESPOSTA PODE SER NEGATIVA?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 640, 160, 24, mix("#FFFFFF", PURPLE, 0.10), aa)
        text(c, "2ª e 3ª: BASE", 580, 270, 28, "black", PURPLE, aa)
        mx(c, "b > 0  e  b ≠ 1", 580, 330, 50, aa, PURPLE)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        cartao(c, 260, 420, 640, 220, ab)
        mx(c, "1^x = 1", 580, 500, 64, ab, INK)
        text(c, "sempre 1: a pergunta não tem resposta", 580, 590, 24, "black", AMBER, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        cartao(c, 980, 220, 680, 420, acc, GREEN, fill=True)
        text(c, "O LOGARITMO (A RESPOSTA)", 1320, 280, 28, "black", GREEN, acc)
        lrow(c, [("log", "", INK), ("m", "0,01 = -2", INK)], 1320, 400, 64, acc)
        check_icon(c, 1320, 520, 34, acc, GREEN)
        text(c, "pode ser negativo", 1320, 600, 32, "black", GREEN, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 690, 1400, 110, 24, "#FFFFFF", ad, shadow=True)
        linha(c, [("de DENTRO (logaritmando): ", INK2), ("positivo", PURPLE), ("   ·   a RESPOSTA: ", INK2),
                  ("qualquer sinal", GREEN)], W / 2, 745, 34, ad)


# ======================================================================
# bloco f — consequências · atalho
# ======================================================================

def b_conseq(c, t, C, B):
    head(c, t, B["start"], "CONSEQUÊNCIAS DA DEFINIÇÃO", "1, 2 E 3 DE 5", PURPLE)
    card(c, *CARD_R)
    itens = [("13.a", [("log", "b", INK, BLUE), ("m", "1 = 0", PURPLE)], "b^0 = 1", [("log", "", INK), ("m", "1 = 0", INK)]),
             ("13.b", [("log", "b", INK, BLUE), ("m", "b = 1", PURPLE)], "b^1 = b", [("log", "", INK), ("m", "10 = 1", INK)]),
             ("13.c", [("log", "b", INK, BLUE), ("m", "b^n = n", PURPLE)], "o expoente à vista",
              [("log", "", INK), ("m", "10^{-7} = -7", INK)])]
    for k, (cue, regra_, porque, exemplo) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 220 + k * 500
        rrect(c, x, 230, 470, 560, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x, 230, 470, 190, 26, mix("#FFFFFF", PURPLE, 0.10), ak)
        lrow(c, regra_, x + 235, 325, 56, ak)
        pill(c, "POR QUÊ", x + 30, 470, AMBER, size=20, a=ak, bounds=(0, 1920))
        if porque.startswith("o "):
            text(c, porque, x + 235, 545, 30, "black", INK2, ak)
        else:
            mx(c, porque, x + 235, 540, 52, ak, INK2)
        pill(c, "EXEMPLO", x + 30, 630, GREEN, size=20, a=ak, bounds=(0, 1920))
        lrow(c, exemplo, x + 235, 715, 46, ak)


def b_conseq2(c, t, C, B):
    head(c, t, B["start"], "CONSEQUÊNCIAS DA DEFINIÇÃO", "4 E 5 DE 5", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 230, 720, 560, 26, "#FFFFFF", aa, shadow=True)
        rrect(c, 220, 230, 720, 190, 26, mix("#FFFFFF", PURPLE, 0.10), aa)
        pot_log(c, "10", "7", 580, 560, 90, aa, INK)
        text(c, "= 7", 580, 700, 70, "black", GREEN, aa)
        text(c, "eleve a base ao expoente que dá 7", 580, 330, 28, "black", PURPLE, aa)
        text(c, "a potência devolve o número", 580, 380, 24, "bold", INK2, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 980, 230, 720, 560, 26, "#FFFFFF", ab, shadow=True)
        rrect(c, 980, 230, 720, 190, 26, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "expoentes iguais,", 1340, 315, 30, "black", PURPLE, ab)
        text(c, "potências iguais", 1340, 365, 30, "black", PURPLE, ab)
        lrow(c, [("log", "", INK), ("m", "x =", INK), ("log", "", INK), ("m", "5", INK)], 1340, 540, 60, ab)
        mx(c, "⇒  x = 5", 1340, 680, 64, ab, GREEN)


def b_atalho_pot(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "JÁ É POTÊNCIA DA BASE?", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    K.atalho(c, 240, 200, 1440, 150, "ATALHO", ["já é potência da base? o log é o expoente"], a0, 40)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        pill(c, "sem conta", W / 2, 400, GREEN, size=28, a=aa, anchor="center")
    for k, (cue, partes, sub) in enumerate((("15.b", [("log", "2", INK, BLUE), ("m", "2^9 = 9", INK)], "o 9 já está à vista"),
                                            ("15.c", [("log", "", INK), ("m", "100 =", INK), ("log", "", INK),
                                                      ("m", "10^2 = 2", INK)], "cem é 10²"))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 240 + k * 740
        cartao(c, x, 470, 700, 300, ak)
        lrow(c, partes, x + 350, 590, 58, ak)
        text(c, sub, x + 350, 710, 30, "black", GREEN, ak)


# ======================================================================
# bloco g — contar algarismos · atalho
# ======================================================================

def b_algarismos(c, t, C, B):
    head(c, t, B["start"], "O LOG CONTA ALGARISMOS", "COMEÇANDO PEQUENO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        defin(c, "ALGARISMO", "cada símbolo de 0 a 9 usado para escrever um número", 260, 200, 1400, aa, BLUE, 28)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        for k, (n_, lg) in enumerate((("10", "1"), ("100", "2"), ("1000", "3"))):
            ak = ep(t, C["16.b"] + 2.0 * k, 0.4)
            if ak <= 0:
                continue
            y = 340 + k * 140
            rrect(c, 260, y, 1400, 120, 22, "#FFFFFF", ak, shadow=True)
            lrow(c, [("log", "", INK), ("m", f"{n_} = {lg}", PURPLE)], 520, y + 60, 46, ak)
            digitos(c, n_, 1050, y + 60, ak, (t - C["16.b"] - 2.0 * k - 0.6) / 0.25, 46, GREEN, 54)
            text(c, f"{len(n_)} algarismos", 1450, y + 75, 36, "black", GREEN, ak)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        regra(c, "ALGARISMOS = LOG + 1", W / 2, 790, acc, 38, GREEN)


def b_algarismos2(c, t, C, B):
    head(c, t, B["start"], "ENTRE DUAS POTÊNCIAS DE 10", "A PARTE INTEIRA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        mx(c, "10^7", 400, 300, 70, aa, BLUE)
        text(c, "<", 600, 320, 60, "black", INK2, aa)
        digitos(c, "25000000", 1000, 300, aa, (t - C["17.a"] - 0.8) / 0.3, 60, GREEN, 66)
        text(c, "<", 1400, 320, 60, "black", INK2, aa)
        mx(c, "10^8", 1580, 300, 70, aa, BLUE)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 420, 1200, 130, 24, mix("#FFFFFF", PURPLE, 0.10), ab)
        lrow(c, [("m", "7 <", PURPLE), ("log", "", INK), ("t", "25 000 000", INK), ("m", "< 8", PURPLE)], W / 2, 485, 50, ab)
        pill(c, "7,…", 1470, 485, PURPLE, size=30, a=ab, anchor="center")
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        defin(c, "PARTE INTEIRA", "o número antes da vírgula", 360, 600, 760, acc, BLUE, 28)
        text(c, "7", 1300, 660, 80, "black", BLUE, acc)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        regra(c, "7 + 1 = 8 ALGARISMOS", W / 2, 780, ad, 40, GREEN)


def b_atalho_alg(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONTAR ALGARISMOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["18"], 0.4)
    K.atalho(c, 240, 200, 1440, 130, "ATALHO", ["log → parte inteira → + 1"], a0, 44)
    for k, (cue, s_) in enumerate((("18.a", "ache o log"), ("18.b", "parte inteira"), ("18.c", "some 1"))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 400 + k * 560
        badge_num(c, k + 1, x - 130, 410, ak, 28, bg=GREEN)
        text(c, s_, x + 30, 425, 38, "black", INK, ak)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        rrect(c, 240, 490, 1440, 300, 26, "#FFFFFF", ad, shadow=True)
        lrow(c, [("m", "3 <", PURPLE), ("log", "", INK), ("m", "4 500 < 4", PURPLE)], 720, 590, 54, ad)
        linha(c, [("3,…  →  3 + 1 = ", INK2), ("4", GREEN)], 720, 700, 50, ep(t, C["18.d"] + 3.6, 0.4))
        digitos(c, "4500", 1370, 640, ep(t, C["18.d"] + 5.4, 0.4), (t - C["18.d"] - 6.2) / 0.35, 70, GREEN, 80)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "LEIA COMO PERGUNTA", GREEN)])
    card(c, *CARD_R)
    res = t >= C["20"]
    for k, (cue, partes, perg, resp, how) in enumerate((
            ("19.a", [("log", "5", INK, BLUE), ("m", "125", GREEN)], "5 elevado a quanto dá 125?", "3",
             "5 · 25 · 125: três cincos"),
            ("19.b", [("log", "", INK), ("m", "0,0001", GREEN)], "10 elevado a quanto dá 0,0001?", "-4",
             "4 casas decimais"))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 220 + k * 760
        cartao(c, x, 240, 720, 460, ak)
        lrow(c, partes, x + 360, 340, 70, ak)
        if not res:
            text_mid(c, "= ?", x + 360, 470, 70, "black", AMBER, ak)
            continue
        q = C["20.a"] if k == 0 else C["20.b"]
        a1 = ep(t, q, 0.4)
        text(c, perg, x + 360, 450, 28, "bold", INK2, a1)
        a2 = ep(t, q + 3.2, 0.4)
        if a2 > 0:
            mx(c, "= " + resp, x + 360, 560, 80, a2, PURPLE)
            text(c, how, x + 360, 660, 26, "black", GREEN, a2)
    if not res:
        acc = ep(t, C["19.c"], 0.5)
        if acc > 0:
            pill(c, "leia como pergunta", W / 2, 760, BLUE, size=28, a=acc, anchor="center")
        pause_timer(c, t, C["19.end"] - 1.9, 1700, 760)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = [None, "O logaritmando é sempre positivo; o logaritmo pode ser negativo.",
          "Algarismos = parte inteira do log + 1."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        if s is None:
            w1 = linha(c, [("Logaritmo é expoente: ", INK)], 320, y - 16, 50, a, align="left")
            w2 = lrow(c, [("log", "b", INK, BLUE), ("m", "a", GREEN)], 320 + w1, y - 16, 50, a, align="left")
            linha(c, [("pergunta “b elevado a quanto dá a?”", INK)], 320, y + 50, 50, a, align="left")
        else:
            para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("log 0 = 0",
          "com o zero, quase tudo dá zero: zero vezes cinco, raiz de zero",
          "10 elevado a quanto dá 0? Nenhum expoente: log 0 NÃO EXISTE. Quem vale zero é log 1."),
         ("2³⁰ tem log ≈ 9,03, então tem 9 algarismos",
          "o 9 está ali, na frente da vírgula",
          "faltou somar 1: 2³⁰ = 1 073 741 824 tem 10 algarismos")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23"], ERROS)


# ======================================================================
# questão 4 (nós fazemos)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS4 = [("A", "30", "esqueceu o + 1", RED), ("B", "31", "", GREEN), ("C", "100", "é o expoente", RED),
         ("D", "101", "expoente + 1", RED), ("E", "200", "base × expoente", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · NÓS FAZEMOS", "QUANTOS ALGARISMOS?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS4, 1060, 260, 600, 40, C["25.ok"], "B", cues_in, cues_x, gap=34)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    if t < C["25"]:
        yend = _enunciado(c, [("Um professor desafiou a turma a descobrir quantos algarismos tem o número", INK)], a0, 250,
                          30)
        mx(c, "2^{100}", 540, yend + 50, 80, a0, PURPLE)
        yend = _enunciado(c, [("quando escrito no sistema decimal, sem calculá-lo. Dado que", INK)], a0, yend + 140, 30)
        lrow(c, [("log", "", GREEN), ("m", "2 ≈ 0,301,", GREEN)], 400, yend + 20, 44, a0)
        _enunciado(c, [("a resposta correta é", INK)], a0, yend + 100, 30)
        pause_timer(c, t, C["24.end"] - 1.9, 860, 740)
        return
    y0 = 206
    a1 = ep(t, C["25"], 0.4)
    rrect(c, 170, y0, 820, 830 - y0, 18, "#FFFFFF", a1, shadow=True)
    aa = ep(t, C["25.a"], 0.4)
    if aa > 0:
        pill(c, "CASO PEQUENO", 200, y0 + 50, AMBER, size=22, a=aa, bounds=(0, 1920))
        lrow(c, [("m", "10^3 = 1 000", INK), ("t", "→", GRAY), ("log", "", INK), ("m", "1 000 = 3", PURPLE)], 650, y0 + 50, 36,
             aa)
        digitos(c, "1000", 580, y0 + 130, aa, (t - C["25.a"] - 1.4) / 0.3, 40, GREEN, 46)
        text(c, "4 algarismos", 800, y0 + 145, 30, "black", GREEN, aa)
    ab = ep(t, C["25.b"], 0.4)
    if ab > 0:
        lrow(c, [("log", "", INK), ("m", "2^{100} = 100 · 0,301 = 30,1", INK)], 580, y0 + 260, 44, ab)
        pill(c, "o expoente desce multiplicando: ep. 2 · confie por enquanto", 580, y0 + 340, PURPLE, size=20,
             a=ep(t, C["25.b"] + 6.0, 0.4), anchor="center", bounds=(170, 990))
    acc = ep(t, C["25.c"], 0.4)
    if acc > 0:
        K.expr(c, "10^{30} < 2^{100} < 10^{31}", 580, y0 + 440, 52, acc, cores={0: BLUE, 2: PURPLE, 4: BLUE})
    ad = ep(t, C["25.d"], 0.4)
    if ad > 0:
        rrect(c, 210, y0 + 510, 740, 100, 18, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("parte inteira 30  ·  30 + 1 = ", INK), ("31", GREEN)], 580, y0 + 560, 40, ad)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "SEM CALCULADORA", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    for k, (s_, col) in enumerate((("2 ≈ 0,30", BLUE), ("3 ≈ 0,48", PURPLE))):
        ak = aa * ep(t, C["28.a"] + 1.6 * k, 0.4)
        if ak <= 0:
            continue
        x = 260 + k * 720
        cartao(c, x, 240, 680, 170, ak)
        lrow(c, [("log", "", INK), ("m", s_, col)], x + 340, 325, 64, ak)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 460, 1200, 200, 26, mix("#FFFFFF", AMBER, 0.20), ab)
        lrow(c, [("log", "", INK), ("m", "6 = ?", INK)], 700, 560, 76, ab)
        lrow(c, [("log", "", INK), ("m", "72 = ?", INK)], 1220, 560, 76, ep(t, C["28.b"] + 1.6, 0.4))
    pill(c, "ep. 2 · as três propriedades e o kit log 2 e log 3", W / 2, 760, PURPLE, size=26,
         a=ep(t, C["28.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Qual log você leu como pergunta pela primeira vez?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, prereq10=b_prereq10, aberta=b_aberta,
              definicao=b_definicao, pergunta=b_pergunta, tabela=b_tabela, notacao=b_notacao,
              atalho_zeros=b_atalho_zeros, existe=b_existe, existe2=b_existe2, conseq=b_conseq, conseq2=b_conseq2,
              atalho_pot=b_atalho_pot, algarismos=b_algarismos, algarismos2=b_algarismos2, atalho_alg=b_atalho_alg,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, ponte=b_ponte, cta=b_cta)
