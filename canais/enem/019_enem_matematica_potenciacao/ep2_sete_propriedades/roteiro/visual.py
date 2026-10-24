"""Visual — Potenciação e Radiciação, Episódio 2: As sete propriedades da potenciação (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (tipografia de potências no expr, fila de fatores, selo de teste, atalho...).
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
_s = importlib.util.spec_from_file_location("comum019", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_potenciacao_ep2_sete_propriedades.mp4"
CARD_R = K.CARD_R
MACA, LARANJA = "#E0483E", "#F29A2E"


def ficha(c, cx, cy, s, col, a, size=56, cut=0.0):
    """um fator numa ficha, centrado em cx; cut = risco vermelho (cancelado)"""
    if a <= 0:
        return
    w = size * 1.25
    K.fila(c, cx - w / 2, cy, [s], a * (1 - 0.55 * cut), {0: col}, size)
    if cut > 0:
        line(c, cx - w * 0.42, cy + w * 0.42, cx - w * 0.42 + w * 0.84 * cut, cy + w * 0.42 - w * 0.84 * cut, RED, a, 6)


def fila_c(c, cx, cy, n, s, col, a, size=56, gap=12, alfas=None):
    """fila de n fatores centrada em cx"""
    w = n * (size * 1.25 + gap) - gap
    K.fila(c, cx - w / 2, cy, [s] * n, a, {i: col for i in range(n)}, size, gap, alfas)
    return w


def atalho_box(c, cx, y, w, s, a, h=96, size=32):
    if a <= 0:
        return
    boxed(c, cx - w / 2, y, w, h, GREEN, a, 0.10)
    text(c, "ATALHO", cx, y + 30, 18, "black", GREEN, a, tracking=2)
    ftext(c, s, cx, y + 72, size, "black", INK, a)


def regra_box(c, s, cx, cy, a, size=64, w=None):
    if a <= 0:
        return
    w = w or K.math_w(s, size) + 120
    boxed(c, cx - w / 2, cy - size * 1.0, w, size * 2.0, PURPLE, a, 0.08)
    expr(c, s, cx, cy, size, a, cores={i: PURPLE for i in range(12)})


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "AS SETE PROPRIEDADES", PURPLE)
    aa = ep(t, C["01.a"], 0.5)
    text_mid(c, "7", 420, 470, 300, "black", PURPLE, aa)
    text(c, "regras. Só sete.", 420, 700, 44, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    for k in range(7):
        a = ab * ep(t, C["01.b"] + 0.15 * k, 0.3)
        x = 800 + (k % 4) * 240
        y = 250 + (k // 4) * 250
        card(c, x, y, 200, 200, a)
        badge_num(c, k + 1, x + 100, y + 100, a, 44, bg=PURPLE)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        boxed(c, 1520, 520, 200, 200, GREEN, ac, 0.10)
        text_mid(c, "sem", 1620, 590, 36, "black", GREEN, ac)
        text_mid(c, "decorar", 1620, 645, 36, "black", GREEN, ac)
    pill(c, "você vai ver de onde cada uma vem", 1240, 800, GREEN, size=30, a=ac, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "aplicar as 7 propriedades sem pensar", "cada uma aberta antes da regra"),
            ("02.b", "quando elas NÃO valem", "a condição que ninguém lê")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")
    selo(c, W / 2, 700, ep(t, C["02.c"], 0.5), "É AÍ QUE A PROVA TENTA TE PEGAR", AMBER, -3, 34)


def b_prereq(c, t, C, B):
    head_seq(c, t, C, [("03", "TRÊS LEMBRETES", "DO EPISÓDIO 1", GREEN), ("04", "UMA PALAVRA NOVA", "PROPRIEDADE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["03", "04"])
    if sid == "03":
        items = [("03.a", "2^3", "fila de fatores iguais"), ("03.b", "a^0 = 1", "menos o zero"), ("03.c", "2^{-3} = 1/8", "o menos inverte")]
        for k, (cue, f_, sub) in enumerate(items):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            x = 420 + k * 540
            rrect(c, x - 230, 230, 460, 520, 24, "#F7F7F5", a)
            badge_num(c, k + 1, x, 280, a, 26, bg=GREEN)
            expr(c, f_, x, 420, 76, a, cores={0: PURPLE})
            if k == 0:
                fila_c(c, x, 580, 3, "2", BLUE, a, 44)
            text(c, sub, x, 700, 30, "black", INK2, a)
        return
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 230, 1320, 150, BLUE, aa, 0.08)
        text(c, "PROPRIEDADE", W / 2, 285, 30, "black", BLUE, aa, tracking=2)
        text(c, "uma regra que vale SEMPRE, para qualquer número", W / 2, 345, 40, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    text(c, "não é lei inventada: é um ATALHO para uma conta que você já sabe", W / 2, 470, 34, "bold", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        expr(c, "2^3", 640, 640, 110, acc, cores={0: PURPLE})
        arrow(c, 760, 640, 960, 640, LIGHT, acc, 6, 18, progress=acc)
        text(c, "abrir", 860, 600, 30, "black", GREEN, acc)
        fila_c(c, 1260, 640, 3, "2", BLUE, ep(t, C["04.c"] + 0.5, 0.4), 60)


# ======================================================================
# propriedade 1 — juntar as filas
# ======================================================================

def b_p1(c, t, C, B):
    head_seq(c, t, C, [("05", "2³ · 2⁴ = ?", "ABRA E JUNTE AS FILAS", BLUE), ("06", "PROPRIEDADE 1", "PRODUTO DE MESMA BASE: SOMA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        a0 = ep(t, C["05"], 0.5)
        expr(c, "2^3 · 2^4", W / 2, 250, 80, a0, cores={0: BLUE, 2: PURPLE})
        jn = ep(t, C["05.c"], 1.0)
        size, wch = 64, 64 * 1.25 + 14
        for i in range(7):
            grp = 0 if i < 3 else 1
            ai = ep(t, C["05.a"] if grp == 0 else C["05.b"], 0.4) * ep(t, C["05.a"] + (0.15 * i if grp == 0 else 0), 0.3)
            x_sep = 560 + i * wch if grp == 0 else 1000 + (i - 3) * wch
            x_jun = W / 2 - 3 * wch + i * wch
            x = lerp(x_sep, x_jun, jn)
            y = lerp(440, 470, jn)
            ficha(c, x, y, "2", BLUE if grp == 0 else PURPLE, ai, size)
        if jn < 0.5:
            text(c, "3 fatores", 560 + wch, 560, 30, "black", BLUE, ep(t, C["05.a"], 0.4) * (1 - 2 * jn))
            text(c, "4 fatores", 1000 + 1.5 * wch, 560, 30, "black", PURPLE, ep(t, C["05.b"], 0.4) * (1 - 2 * jn))
        ad = ep(t, C["05.d"], 0.5)
        for i in range(7):
            badge_num(c, i + 1, W / 2 - 3 * wch + i * wch, 580, ad * ep(t, C["05.d"] + 0.2 * i, 0.25), 20, bg=GREEN)
        ae = ep(t, C["05.e"], 0.5)
        if ae > 0:
            rrect(c, 660, 650, 600, 120, 20, "#FFFFFF", ae, shadow=True)
            expr(c, "= 2^7", W / 2, 712, 80, ae, cores={1: GREEN})
        return
    a0 = ep(t, C["06"], 0.5)
    expr(c, "2^3 · 2^4 = 2^{3+4} = 2^7", W / 2, 260, 70, a0, cores={4: GREEN})
    aa = ep(t, C["06.a"], 0.5)
    chip(c, "os expoentes SE SOMARAM", W / 2, 350, GREEN, aa, 30)
    ab = ep(t, C["06.b"], 0.5)
    regra_box(c, "a^m · a^n = a^{m+n}", W / 2, 490, ab, 70, 820)
    acc = ep(t, C["06.c"], 0.5)
    text(c, "a = a base  ·  m e n = os expoentes", W / 2, 610, 30, "bold", INK2, acc)
    ad = ep(t, C["06.d"], 0.5)
    pill(c, "MESMA BASE = o mesmo número embaixo nas duas potências", W / 2, 670, BLUE, size=28, a=ad * (1 - ep(t, C["06.e"], 0.4)),
         anchor="center", bounds=(0, 1920))
    atalho_box(c, W / 2, 640, 1240, "mesma base multiplicando? copie a base e SOME os expoentes", ep(t, C["06.e"], 0.5), 110, 32)


# ======================================================================
# propriedade 2 — cancelar em pares
# ======================================================================

def _divisao(c, t, cima, baixo, cx, cy0, t_in, t_cut, col_c, col_b, s="2", size=56, t_left=None):
    """fração de fichas: cima/baixo fatores; pares cancelam a partir de t_cut (um par a cada 0,35 s)"""
    wch = size * 1.25 + 12
    a = ep(t, t_in, 0.5)
    n = max(cima, baixo)
    wl = n * wch + 30
    line(c, cx - wl / 2, cy0, cx + wl / 2, cy0, INK, a, 5)
    pares = min(cima, baixo)
    x0 = cx - (n - 1) * wch / 2
    for i in range(cima):
        cut = ep(t, t_cut + 0.35 * i, 0.3) if i < pares else 0
        ficha(c, x0 + i * wch, cy0 - 70, s, col_c, a, size, cut)
    for i in range(baixo):
        cut = ep(t, t_cut + 0.35 * i, 0.3) if i < pares else 0
        ficha(c, x0 + i * wch, cy0 + 70, s, col_b, a, size, cut)
    if t_left is not None:
        al = ep(t, t_left, 0.4)
        if cima > baixo:
            for i in range(pares, cima):
                rrect(c, x0 + i * wch - wch / 2, cy0 - 70 - wch / 2 - 4, wch, wch + 8, 16, GREEN, 0.14 * al)
        elif baixo > cima:
            for i in range(pares, baixo):
                rrect(c, x0 + i * wch - wch / 2, cy0 + 70 - wch / 2 - 4, wch, wch + 8, 16, GREEN, 0.14 * al)


def b_p2(c, t, C, B):
    head_seq(c, t, C, [("07", "2⁷ ÷ 2³ = ?", "CANCELE EM PARES", BLUE), ("08", "PROPRIEDADE 2", "QUOCIENTE DE MESMA BASE: SUBTRAI", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        a0 = ep(t, C["07"], 0.5)
        expr(c, "2^7 ÷ 2^3", 430, 300, 76, a0, cores={0: BLUE, 2: PURPLE})
        text(c, "como fração:", 430, 400, 30, "bold", INK2, ep(t, C["07.a"], 0.4))
        _divisao(c, t, 7, 3, 1180, 470, C["07.a"], C["07.b"] + 0.4, BLUE, PURPLE, t_left=C["07.d"])
        ab = ep(t, C["07.b"], 0.5)
        expr(c, "2 ÷ 2 = 1", 430, 520, 54, ab, cores={4: GREEN})
        chip(c, "3 pares somem", 430, 620, RED, ep(t, C["07.c"], 0.5), 30)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            rrect(c, 230, 680, 400, 110, 20, "#FFFFFF", ad, shadow=True)
            expr(c, "= 2^4", 430, 735, 70, ad, cores={1: GREEN})
        return
    a0 = ep(t, C["08"], 0.5)
    expr(c, "2^7/2^3 = 2^{7-3} = 2^4", W / 2, 270, 70, a0, cores={2: GREEN})
    chip(c, "os expoentes SE SUBTRAEM", W / 2, 380, GREEN, ep(t, C["08.a"], 0.5), 30)
    regra_box(c, "a^m ÷ a^n = a^{m-n}", W / 2, 510, ep(t, C["08.b"], 0.5), 70, 820)
    pill(c, "QUOCIENTE = o resultado de uma divisão", W / 2, 630, BLUE, size=28, a=ep(t, C["08.c"], 0.5), anchor="center", bounds=(0, 1920))
    atalho_box(c, W / 2, 690, 1160, "dividiu mesma base? expoente de CIMA menos o de BAIXO", ep(t, C["08.d"], 0.5), 110, 32)


# ======================================================================
# propriedade 3 — copiar a fila
# ======================================================================

def b_p3(c, t, C, B):
    head_seq(c, t, C, [("09", "(2³)² = ?", "A FILA É COPIADA", BLUE), ("10", "PROPRIEDADE 3", "POTÊNCIA DE POTÊNCIA: MULTIPLICA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        a0 = ep(t, C["09"], 0.5)
        expr(c, "(2^3)^2", 430, 330, 110, a0, cores={0: BLUE})
        chip(c, "POTÊNCIA DE POTÊNCIA", 430, 480, BLUE, ep(t, C["09.a"], 0.5), 30)
        text(c, "ao quadrado = a fila aparece 2 vezes", 430, 570, 28, "bold", INK2, ep(t, C["09.b"], 0.5))
        ab = ep(t, C["09.b"], 0.5)
        cp = ep(t, C["09.c"], 0.9)
        wch = 56 * 1.25 + 12
        x0 = 1060
        for i in range(3):
            ficha(c, x0 + i * wch, 330, "2", BLUE, ab, 56)
        if cp > 0:
            for i in range(3):
                ficha(c, x0 + i * wch + lerp(0, 3 * wch + 20, cp), lerp(330, 330, cp), "2", PURPLE, cp, 56)
        text(c, "3 fatores", x0 + wch, 430, 28, "black", BLUE, ab)
        text(c, "+ a cópia: 3 fatores", x0 + 4 * wch + 20, 430, 28, "black", PURPLE, cp)
        ad = ep(t, C["09.d"], 0.5)
        for i in range(6):
            xx = x0 + i * wch + (20 if i >= 3 else 0)
            badge_num(c, i + 1, xx, 510, ad * ep(t, C["09.d"] + 0.15 * i, 0.25), 20, bg=GREEN)
        if ad > 0:
            rrect(c, 1080, 600, 440, 110, 20, "#FFFFFF", ad, shadow=True)
            expr(c, "= 2^6", 1300, 655, 70, ad, cores={1: GREEN})
        return
    a0 = ep(t, C["10"], 0.5)
    expr(c, "(2^3)^2 = 2^{3·2} = 2^6", W / 2, 270, 70, a0, cores={2: GREEN})
    chip(c, "os expoentes SE MULTIPLICAM", W / 2, 380, GREEN, ep(t, C["10.a"], 0.5), 30)
    regra_box(c, "(a^m)^n = a^{m·n}", W / 2, 520, ep(t, C["10.b"], 0.5), 70, 820)
    atalho_box(c, W / 2, 660, 1440, "expoente de fora do parêntese, em cima de outro? MULTIPLIQUE os dois", ep(t, C["10.c"], 0.5), 110, 30)


# ======================================================================
# propriedade 4 — o expoente se distribui no produto
# ======================================================================

def b_p4(c, t, C, B):
    head_seq(c, t, C, [("11", "(2 · 5)³ = ?", "ABRA E REORGANIZE", BLUE), ("12", "PROPRIEDADE 4", "POTÊNCIA DE UM PRODUTO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        a0 = ep(t, C["11"], 0.5)
        expr(c, "(2·5)^3", W / 2, 260, 90, a0, cores={0: INK})
        aa = ep(t, C["11.a"], 0.5)
        mv = ep(t, C["11.c"], 1.0)
        wch = 52 * 1.25 + 10
        for g in range(3):
            for j, (s, col) in enumerate((("2", BLUE), ("5", AMBER))):
                ag = aa * ep(t, C["11.a"] + 0.35 * g, 0.3)
                x_ab = 470 + g * 3 * wch + j * wch
                y_ab = 450
                k = j * 3 + g
                x_or = W / 2 - 2.5 * wch - 30 + k * wch + (60 if j == 1 else 0)
                y_or = 600
                ficha(c, lerp(x_ab, x_or, mv), lerp(y_ab, y_or, mv), s, col, ag, 52)
            if mv < 0.5:
                ga = aa * ep(t, C["11.a"] + 0.35 * g, 0.3) * (1 - 2 * mv)
                text(c, "(2·5)", 470 + g * 3 * wch + wch / 2, 540, 26, "black", INK2, ga)
                if g < 2:
                    fmid(c, "·", 470 + g * 3 * wch + 2 * wch - 8, 450, 40, "black", INK2, ga)
        ab = ep(t, C["11.b"], 0.5)
        pill(c, "na multiplicação, a ORDEM não importa", W / 2, 360, GREEN, size=28, a=ab * (1 - ep(t, C["11.d"], 0.4)), anchor="center",
             bounds=(0, 1920))
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            rrect(c, 660, 700, 600, 110, 20, "#FFFFFF", ad, shadow=True)
            expr(c, "= 2^3 · 5^3", W / 2, 755, 64, ad, cores={1: BLUE, 3: AMBER})
        return
    a0 = ep(t, C["12"], 0.5)
    expr(c, "(2·5)^3 = 2^3 · 5^3", W / 2, 250, 66, a0, cores={2: BLUE, 4: AMBER})
    pill(c, "DISTRIBUIR = entregar para cada um que está dentro", W / 2, 340, BLUE, size=28, a=a0, anchor="center", bounds=(0, 1920))
    regra_box(c, "(a·b)^n = a^n · b^n", W / 2, 470, ep(t, C["12.a"], 0.5), 66, 820)
    ab = ep(t, C["12.b"], 0.5)
    expr(c, "10^3 = 1000", 620, 620, 52, ab, cores={2: GREEN})
    acc = ep(t, C["12.c"], 0.5)
    expr(c, "8 · 125 = 1000", 1300, 620, 52, acc, cores={4: GREEN})
    check_icon(c, 1560, 606, 28, acc, GREEN)
    atalho_box(c, W / 2, 690, 900, "o expoente de fora ENTRA em cada fator de dentro", ep(t, C["12.d"], 0.5), 110, 32)


# ======================================================================
# propriedade 5 — fração: os dois andares
# ======================================================================

def b_p5(c, t, C, B):
    frame(c, t, B["start"], "PROPRIEDADE 5", "POTÊNCIA DE UM QUOCIENTE", PURPLE)
    a0 = ep(t, C["13"], 0.5)
    aa = ep(t, C["13.a"], 0.5)
    expr(c, "(2/3)^3 = 2/3 · 2/3 · 2/3", W / 2, 270, 70, a0, alfas={1: aa, 2: aa, 3: aa, 4: aa, 5: aa, 6: aa})
    ab = ep(t, C["13.b"], 0.5)
    chip(c, "fração × fração: em cima com em cima, embaixo com embaixo", W / 2, 390, BLUE, ab, 28)
    acc = ep(t, C["13.c"], 0.5)
    expr(c, "2·2·2/3·3·3 = 2^3/3^3 = 8/27", W / 2, 520, 62, acc, cores={4: GREEN})
    ad = ep(t, C["13.d"], 0.5)
    regra_box(c, "(a/b)^n = a^n/b^n", 760, 720, ad, 56, 620)
    if ad > 0:
        text(c, "o expoente vai para", 1330, 700, 30, "black", INK2, ad)
        text(c, "os DOIS andares", 1330, 745, 30, "black", PURPLE, ad)


# ======================================================================
# propriedades 6 e 7 — saem da propriedade 2
# ======================================================================

def b_p6(c, t, C, B):
    frame(c, t, B["start"], "PROPRIEDADE 6", "SAI DA PROPRIEDADE 2", PURPLE)
    _divisao(c, t, 3, 3, 520, 440, C["14.a"], C["14.c"], BLUE, BLUE, s="a", size=56)
    ab = ep(t, C["14.b"], 0.5)
    expr(c, "a^3/a^3 = a^{3-3} = a^0", 1290, 330, 60, ab, cores={4: PURPLE})
    acc = ep(t, C["14.c"], 0.5)
    text(c, "todo número dividido por ele mesmo dá 1", 1290, 470, 30, "black", INK2, acc)
    expr(c, "a^3/a^3 = 1", 1290, 560, 60, acc, cores={2: GREEN})
    regra_box(c, "a^0 = 1", 1290, 710, ep(t, C["14.d"], 0.5), 60, 420)
    pill(c, "o mesmo degrau da escada do ep. 1", 520, 720, GREEN, size=28, a=ep(t, C["14.e"], 0.5), anchor="center", bounds=(0, 1920))


def b_p7(c, t, C, B):
    frame(c, t, B["start"], "PROPRIEDADE 7", "MAIS FATORES EMBAIXO", PURPLE)
    a0 = ep(t, C["15.a"], 0.5)
    expr(c, "a^2/a^5", 300, 330, 70, a0)
    _divisao(c, t, 2, 5, 780, 440, C["15.a"], C["15.b"], BLUE, BLUE, s="a", size=52, t_left=C["15.b"] + 1.0)
    ab = ep(t, C["15.b"], 0.5)
    expr(c, "= 1/a^3", 300, 560, 64, ab, cores={1: GREEN})
    text(c, "sobram 3 embaixo", 300, 670, 28, "black", GREEN, ab)
    acc = ep(t, C["15.c"], 0.5)
    expr(c, "a^{2-5} = a^{-3}", 1440, 330, 60, acc, cores={2: PURPLE})
    text(c, "pela propriedade 2", 1440, 420, 28, "bold", INK2, acc)
    regra_box(c, "a^{-n} = 1/a^n", 1440, 560, ep(t, C["15.d"], 0.5), 56, 460)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        rrect(c, 1230, 680, 420, 100, 20, "#FFFFFF", ae, shadow=True)
        expr(c, "3^{-2} = 1/3^2 = 1/9", 1440, 730, 44, ae, cores={4: GREEN})


# ======================================================================
# as sete, lado a lado
# ======================================================================

SETE = [("a^m · a^n = a^{m+n}", "produto de mesma base: SOMA", "16.a"), ("a^m ÷ a^n = a^{m-n}", "quociente de mesma base: SUBTRAI", "16.b"),
        ("(a^m)^n = a^{m·n}", "potência de potência: MULTIPLICA", "16.c"), ("(a·b)^n = a^n · b^n", "entra em cada fator", "16.d"),
        ("(a/b)^n = a^n/b^n", "entra em cada andar", "16.d"), ("a^0 = 1", "base diferente de zero", "16.e"),
        ("a^{-n} = 1/a^n", "negativo INVERTE", "16.e")]


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "AS SETE", "LADO A LADO", PURPLE)
    for k, (f_, s, cue) in enumerate(SETE):
        a = ep(t, C[cue] + (0.5 if k in (4, 6) else 0), 0.4)
        y = 200 + k * 82
        hl = ep(t, C[cue], 0.3) * (1 - ep(t, C[cue] + 2.0, 0.6)) if t < C["16.f"] else 0
        rrect(c, 220, y - 8, 1480, 72, 14, mix("#F7F7F5", PURPLE, 0.12 * hl), a)
        badge_num(c, k + 1, 270, y + 28, a, 24, bg=PURPLE)
        expr(c, f_, 660, y + 28, 40, a, cores={i: PURPLE for i in range(8)})
        text(c, s, 1060, y + 41, 30, "black", INK2, a, align="left")
    selo(c, W / 2, 800, ep(t, C["16.f"], 0.5), "TODAS ABERTAS, NENHUMA DECORADA", GREEN, -2, 30)


# ======================================================================
# a condição: mesma fruta
# ======================================================================

def _frutas(c, x, y, n, col, a, r=24, gap=62):
    for i in range(n):
        ai = a * ep(1, 0, 0.1)
        c.drawCircle(x + i * gap, y, r, paint(col, ai))
        c.drawCircle(x + i * gap + r * 0.25, y - r * 0.95, r * 0.25, paint("#4C9A3A", ai))


def b_condicao(c, t, C, B):
    frame(c, t, B["start"], "A CONDIÇÃO QUE NINGUÉM LÊ", "SÓ COM A MESMA FRUTA", AMBER)
    aa = ep(t, C["17.a"], 0.5)
    pill(c, "propriedades 1 e 2: MESMA BASE", W / 2, 230, PURPLE, size=32, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        _frutas(c, 300, 380, 3, MACA, ab)
        fmid(c, "+", 500, 380, 50, "black", INK2, ab)
        _frutas(c, 560, 380, 4, MACA, ab)
        arrow(c, 820, 380, 900, 380, LIGHT, ab, 5, 14, progress=ab)
        _frutas(c, 950, 380, 7, MACA, ep(t, C["17.b"] + 0.8, 0.4), 22, 54)
        text(c, "uma fila de 7 maçãs", 1110, 460, 28, "black", GREEN, ep(t, C["17.b"] + 0.8, 0.4))
        expr(c, "2^3 · 2^4 = 2^7", 1580, 390, 44, ab, cores={4: GREEN})
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        _frutas(c, 300, 570, 3, MACA, acc)
        fmid(c, "+", 500, 570, 50, "black", INK2, acc)
        _frutas(c, 560, 570, 4, LARANJA, acc)
        check_icon(c, 880, 560, 30, acc, RED, "x")
        text(c, "não vira uma fila só", 1060, 582, 30, "black", RED, acc)
        expr(c, "2^3 · 3^4", 1580, 570, 44, acc)
        line(c, 1480, 600, 1680, 540, RED, acc, 5)
    pill(c, "propriedades 4 e 5: MESMO EXPOENTE", W / 2, 720, PURPLE, size=32, a=ep(t, C["17.d"], 0.5), anchor="center", bounds=(0, 1920))


def b_mesma_base(c, t, C, B):
    head_seq(c, t, C, [("18", "O PRIMEIRO MOVIMENTO", "TUDO NA MESMA BASE", GREEN), ("19", "ATALHO", "VÁ DOBRANDO A PARTIR DO 2", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19"])
    vals = [2, 4, 8, 16, 32]
    if sid == "18":
        chip(c, "transforme tudo na MESMA FRUTA", W / 2, 240, GREEN, ep(t, C["18.a"], 0.5), 32)
        for k, v in enumerate(vals):
            a = ep(t, C["18.b"] + 0.35 * k, 0.35)
            x = 400 + k * 280
            card(c, x - 110, 320, 220, 160, a)
            text_mid(c, str(v), x, 400, 80, "black", INK, a)
            ad = ep(t, C["18.d"] + (0 if k < 2 else 1.1 * (k - 1)), 0.4)
            if k == 0:
                ad = ep(t, C["18.c"] + 0.4, 0.4)
            expr(c, f"= 2^{k + 1}", x, 560, 60, ad, cores={1: GREEN})
        text(c, "todos viram potência de 2", W / 2, 700, 34, "black", GREEN, ep(t, C["18.c"], 0.5))
        return
    a0 = ep(t, C["19.a"], 0.5)
    boxed(c, 220, 200, 1480, 560, GREEN, a0, 0.06)
    text(c, "ATALHO", W / 2, 250, 24, "black", GREEN, a0, tracking=2)
    text(c, "comece no 2 e vá dobrando", W / 2, 310, 44, "black", INK, a0)
    hl = ep(t, C["19.c"], 0.4)
    for k, v in enumerate(vals):
        a = ep(t, C["19.a"] + 0.4 * k, 0.35)
        x = 380 + k * 290
        col = GREEN if (k == 2 and hl > 0) else INK
        text_mid(c, str(v), x, 460, 90, "black", col, a)
        if k > 0:
            arrow(c, x - 220, 460, x - 80, 460, LIGHT, a, 5, 14, progress=a)
            fmid(c, "×2", x - 150, 405, 30, "black", AMBER, a)
        badge_num(c, k + 1, x, 560, ep(t, C["19.b"] + 0.2 * k, 0.3), 24, bg=GREEN)
    text(c, "a posição na fila = o expoente", W / 2, 640, 34, "bold", INK2, ep(t, C["19.b"], 0.5))
    expr(c, "8 é o 3º → 8 = 2^3", W / 2, 720, 48, hl, cores={5: GREEN})


# ======================================================================
# três coisas que não existem
# ======================================================================

FALSAS = {
    "20": dict(h=("FALSA REGRA 1", "SOMA DE POTÊNCIAS"), q="a^m + a^n = a^{m+n} ?", l="2^2 + 2^3 = 4 + 8 = 12", r="2^5 = 32",
               lc={6: RED}, rc={2: RED}, cues=("20.b", "20.c", "20.d"), fim="na SOMA não existe propriedade nenhuma"),
    "21": dict(h=("FALSA REGRA 2", "QUADRADO DE UMA SOMA"), q="(a+b)^2 = a^2 + b^2 ?", l="(2+3)^2 = 5^2 = 25", r="2^2 + 3^2 = 4 + 9 = 13",
               lc={4: RED}, rc={6: RED}, cues=("21.a", "21.b", "21.c"), fim="o expoente entra nos fatores de uma MULTIPLICAÇÃO, não de uma soma"),
}


def b_falsas(c, t, C, B):
    sid = which(t, C, ["20", "21", "22"])
    if sid == "22":
        frame(c, t, C["22"], "FALSA REGRA 3", "A TORRE", AMBER)
        a0 = ep(t, C["22"], 0.5)
        expr(c, "(2^3)^2 = 2^{3^2} ?", W / 2, 260, 70, a0)
        K.selo_teste(c, 1560, 250, a0)
        aa = ep(t, C["22.a"], 0.5)
        if aa > 0:
            rrect(c, 230, 380, 680, 300, 22, "#F7F7F5", aa)
            text(c, "potência de potência", 570, 430, 28, "black", PURPLE, aa)
            expr(c, "(2^3)^2 = 2^6 = 64", 570, 540, 56, aa, cores={4: GREEN})
        ab = ep(t, C["22.b"], 0.5)
        if ab > 0:
            rrect(c, 1010, 380, 680, 300, 22, "#F7F7F5", ab)
            text(c, "torre: o expoente tem expoente", 1350, 430, 28, "black", AMBER, ab)
            acc = ep(t, C["22.c"], 0.5)
            expr(c, "2^{3^2} = 2^9 = 512", 1350, 550, 56, ab, cores={4: RED}, alfas={2: acc, 3: acc, 4: acc})
            if acc > 0:
                arrow(c, 1150, 470, 1150, 610, AMBER, acc, 4, 14, progress=acc)
                text(c, "de cima para baixo: 3² = 9", 1350, 640, 26, "black", AMBER, acc)
            fmid(c, "≠", W / 2, 530, 80, "black", RED, acc)
        K.selo_teste(c, W / 2, 760, ep(t, C["22.c"] + 1.5, 0.5))
        return
    d = FALSAS[sid]
    frame(c, t, C[sid], d["h"][0], d["h"][1], AMBER)
    q_ = C[f"{sid}.a"] if sid == "20" else C["21"]
    a0 = ep(t, q_, 0.5)
    expr(c, d["q"], W / 2, 260, 70, a0)
    K.selo_teste(c, 1600, 250, ep(t, C[d["cues"][0]], 0.5))
    c1, c2, c3 = (C[x] for x in d["cues"])
    al = ep(t, c1, 0.5)
    if al > 0:
        rrect(c, 230, 380, 680, 240, 22, "#F7F7F5", al)
        text(c, "lado esquerdo", 570, 430, 26, "black", GRAY, al, tracking=1)
        expr(c, d["l"], 570, 530, 50, al, cores=d["lc"])
    ar = ep(t, c2, 0.5)
    if ar > 0:
        rrect(c, 1010, 380, 680, 240, 22, "#F7F7F5", ar)
        text(c, "lado direito", 1350, 430, 26, "black", GRAY, ar, tracking=1)
        expr(c, d["r"], 1350, 530, 50, ar, cores=d["rc"])
    a3 = ep(t, c3, 0.5)
    fmid(c, "≠", W / 2, 510, 80, "black", RED, a3)
    regra(c, d["fim"], W / 2, 720, a3, 32, RED)


def b_teste(c, t, C, B):
    frame(c, t, B["start"], "O QUE SALVOU NAS TRÊS", "O TESTE COM NÚMEROS PEQUENOS", GREEN)
    aa = ep(t, C["23.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 230, 1320, 420, GREEN, aa, 0.06)
        text(c, "ATALHO", W / 2, 285, 24, "black", GREEN, aa, tracking=2)
        text(c, "TESTE COM 2 E 3", W / 2, 370, 64, "black", GREEN, aa)
    ab = ep(t, C["23.b"], 0.5)
    for k, s in enumerate(["troque as letras por 2 e 3", "faça a conta dos dois lados", "bateu? a regra existe"]):
        a = ab * ep(t, C["23.b"] + 0.6 * k, 0.35)
        badge_num(c, k + 1, 520, 450 + k * 62, a, 22, bg=GREEN)
        text(c, s, 570, 462 + k * 62, 34, "black", INK, a, align="left")
    acc = ep(t, C["23.c"], 0.5)
    if acc > 0:
        pause_timer(c, t, -10, 1430, 520, acc)
        text(c, "5 segundos", 1430, 610, 32, "black", GREEN, acc)
    pill(c, "muito melhor do que apostar", W / 2, 740, GREEN, size=32, a=acc, anchor="center", bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Multiplicou mesma base: soma. Dividiu: subtrai. Potência de potência: multiplica.", "Primeiro tudo na mesma base.",
          "Na soma não existe propriedade. Na dúvida, teste com 2 e 3."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["24", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "24" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 280 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1340, 56)


ERROS = [("somar expoentes numa SOMA: 2² + 2³ = 2⁵", "a regra de somar expoentes existe",
          "ela é do PRODUTO: 2² + 2³ = 4 + 8 = 12, não 32"),
         ("(2³)² = 2⁵", "somar expoentes é a regra mais famosa", "a fila foi COPIADA: 3 · 2 = 6 → 2⁶"),
         ("(a + b)² = a² + b²", "com multiplicação funciona: (a · b)² = a² · b²", "com soma, não: (2 + 3)² = 25, mas 4 + 9 = 13"),
         ("usar as propriedades com bases diferentes", "são todas potências", "maçã com laranja não junta: PRIMEIRO tudo na mesma base")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["25", "26", "27", "28"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, a, s_expr, rotulo):
    text(c, "Simplificando a expressão", 190, 250, 36, "black", INK, a, align="left")
    expr(c, s_expr, 190, 360, 62, a, align="left")
    text(c, "obtém-se", 190, 470, 36, "black", INK, a, align="left")
    text(c, rotulo, 190, 822, 18, "medium", GRAY, a, align="left")


ALTS_X = [("A", "2", "não sai de conta certa", RED), ("B", "4", "esqueceu o ² do 4²", RED), ("C", "8", "fez 4² = 4 · 2", RED),
          ("D", "16", "", GREEN), ("E", "32", "não sai de conta certa", RED)]


def b_extra(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO", "TUDO NA MESMA BASE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    _enunciado(c, a0, "{2^3·4^2}/8", "Questão extra da série (estilo ENEM)")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["31.xa"], "B": C["31.xb"], "C": C["31.xc"], "E": C["31.xa"] + 0.6}
    if t >= C["29.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS_X, 1000, 220, 680, 44, C["30.ok"], "D", cues_in, cues_x, gap=22)
    if t >= C["30"]:
        ra = ep(t, C["30"], 0.4)
        rrect(c, 170, 500, 780, 310, 18, "#FFFFFF", ra, shadow=True)
        expr(c, "4^2 = (2^2)^2 = 2^4", 560, 550, 40, ep(t, C["30.a"], 0.4), cores={4: GREEN})
        expr(c, "8 = 2^3", 560, 620, 40, ep(t, C["30.b"], 0.4), cores={2: GREEN})
        expr(c, "2^3 · 2^4 = 2^7", 560, 690, 40, ep(t, C["30.c"], 0.4), cores={4: PURPLE})
        expr(c, "2^7/2^3 = 2^4 = 16", 560, 765, 40, ep(t, C["30.d"], 0.4), cores={4: GREEN})
    if t >= C["31.xe"]:
        ae = ep(t, C["31.xe"], 0.4)
        rrect(c, 170, 500, 780, 310, 18, "#FFFFFF", ae, shadow=True)
        K.selo_teste(c, 560, 560, ae, ok=True)
        expr(c, "8 · 16 = 128", 560, 670, 48, ae)
        expr(c, "128 ÷ 8 = 16", 560, 750, 48, ae, cores={4: GREEN})


ALTS_Q = [("A", "8", "não sai de conta certa", RED), ("B", "16", "somou no 4³: (2²)³ = 2⁵", RED), ("C", "32", "", GREEN),
          ("D", "64", "somou no 8²: (2³)² = 2⁵", RED), ("E", "128", "fez 8² = 8 · 2 = 16", RED)]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["32.a"], 0.4)
    _enunciado(c, a0, "{2^5·4^3}/8^2", "Questão do material de estudo (seção 12)")
    cues_in = {L: C[f"32.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["34.xa"], "B": C["34.xb"], "D": C["34.xd"], "E": C["34.xe"]}
    if t >= C["32.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS_Q, 1000, 220, 680, 44, C["33.ok"], "C", cues_in, cues_x, gap=22)
    ap = ep(t, C["32.p"], 0.4) * (1 - ep(t, C["33"], 0.3))
    pill(c, "comece pela mesma base", 470, 600, GREEN, size=28, a=ap, anchor="center", bounds=(0, 1920))
    pause_timer(c, t, C["32.end"] - 1.9, 470, 700)
    if t >= C["33"]:
        ra = ep(t, C["33"], 0.4)
        rrect(c, 170, 500, 780, 310, 18, "#FFFFFF", ra, shadow=True)
        expr(c, "4^3 = (2^2)^3 = 2^6", 560, 550, 40, ep(t, C["33.a"], 0.4), cores={4: GREEN})
        expr(c, "8^2 = (2^3)^2 = 2^6", 560, 620, 40, ep(t, C["33.b"], 0.4), cores={4: GREEN})
        expr(c, "2^5 · 2^6 = 2^{11}", 560, 690, 40, ep(t, C["33.c"], 0.4), cores={4: PURPLE})
        expr(c, "2^{11}/2^6 = 2^5 = 32", 560, 765, 40, ep(t, C["33.d"], 0.4), cores={4: GREEN})
    if t >= C["34.chk"]:
        ak = ep(t, C["34.chk"], 0.4)
        rrect(c, 170, 500, 780, 310, 18, "#FFFFFF", ak, shadow=True)
        expr(c, "4^3 = 64  e  8^2 = 64", 560, 570, 44, ak, cores={2: GREEN, 6: GREEN})
        expr(c, "{2^5·64}/64 = 2^5 = 32", 560, 720, 46, ak, cores={4: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "POTÊNCIAS DE 10", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    text(c, "a base que mais aparece no ENEM", W / 2, 250, 40, "black", INK, aa)
    ab = ep(t, C["36.b"], 0.5)
    expr(c, "10^n", W / 2, 420, 170, ab, cores={0: PURPLE})
    for k, (nome, f_) in enumerate((("população", "10^6"), ("distâncias", "10^9"), ("energia", "10^{-3}"))):
        a = ep(t, C["36.c"] + 0.5 * k, 0.4)
        x = 560 + k * 400
        card(c, x - 160, 560, 320, 160, a)
        expr(c, f_, x, 620, 50, a, cores={0: PURPLE})
        text(c, nome, x, 695, 30, "black", INK, a)
    pill(c, "ep. 3 · potências de 10", W / 2, 790, PURPLE, size=32, a=ep(t, C["36.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"], "Qual das 7 propriedades você não conhecia?",
        canal="no Estudativo", anki=C["37.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, p1=b_p1, p2=b_p2, p3=b_p3, p4=b_p4, p5=b_p5, p6=b_p6, p7=b_p7,
              tabela=b_tabela, condicao=b_condicao, mesma_base=b_mesma_base, falsas=b_falsas, teste=b_teste, recap=b_recap,
              erros=b_erros, extra=b_extra, questao=b_questao, ponte=b_ponte, cta=b_cta)
