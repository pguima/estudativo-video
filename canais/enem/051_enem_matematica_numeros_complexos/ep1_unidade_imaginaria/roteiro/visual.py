"""Visual — Números Complexos, Episódio 1: a unidade imaginária, delta negativo e as potências de i (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: calculadora() (o visor "√−36 = erro" que vira "6i"), termometro() (os −5 °C), relogio() (o relógio
de quatro horas com 1, i, −1 e −i; o ponteiro anda uma casa a cada ×i), gemeas() (as duas raízes espelhadas).
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
_s = importlib.util.spec_from_file_location("comum051", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w, expr, math_w = K.ftext, K.ftext_w, K.expr, K.math_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_complexos_ep1_unidade_imaginaria.mp4"
CARD_R = K.CARD_R
CASAS = ["1", "i", "−1", "−i"]
CASA_COR = [BLUE, PURPLE, RED, AMBER]


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


def lembrete_i2(c, x, y, a):
    """o carimbo da regra: sempre que aparece i², a conta para e mostra i² = −1"""
    if a <= 0:
        return
    rrect(c, x - 130, y - 44, 260, 88, 20, mix("#FFFFFF", PURPLE, 0.18), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 130, y - 44, 260, 88), 20, 20), paint(PURPLE, a, stroke=4))
    expr(c, "i^2 = −1", x, y, 46, a, cores={0: PURPLE, 2: PURPLE})


def calculadora(c, cx, cy, a, vira=0.0, conta="√{−36}"):
    """celular com a calculadora: o visor mostra 'erro'; vira 0 → 1 troca por '6i' em verde"""
    if a <= 0:
        return
    w, h = 380, 640
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(c, x0, y0, w, h, 46, INK, a, shadow=True)
    rrect(c, x0 + 22, y0 + 40, w - 44, 200, 24, "#EEF1F4", a)
    expr(c, conta, cx + 120, y0 + 100, 44, a, align="right", cores={0: INK2})
    if vira < 1:
        text(c, "erro", cx + 130, y0 + 205, 64, "black", RED, a * (1 - vira), align="right")
    if vira > 0:
        expr(c, "= 6i", cx + 130, y0 + 185, 70, a * vira, align="right", cores={1: GREEN})
    teclas = ["7", "8", "9", "÷", "4", "5", "6", "×", "1", "2", "3", "−", "0", ".", "√", "="]
    for k, tk in enumerate(teclas):
        col_, row = k % 4, k // 4
        kx, ky = x0 + 38 + col_ * 80, y0 + 280 + row * 82
        rrect(c, kx, ky, 66, 66, 33, "#3A3F4A" if col_ < 3 else mix(INK, AMBER, 0.55), a)
        text(c, tk, kx + 33, ky + 45, 32, "black", "#FFFFFF", a)


def termometro(c, cx, cy, a, nivel=1.0):
    """termômetro de rua marcando −5 °C (nivel 0 → 1 desce o líquido do 0 até o −5)"""
    if a <= 0:
        return
    rrect(c, cx - 34, cy - 260, 68, 470, 34, "#FFFFFF", a, shadow=True)
    c.drawCircle(cx, cy + 230, 56, paint(BLUE, a))
    top0 = cy - 60
    y5 = cy + 40
    yl = top0 + (y5 - top0) * nivel
    rrect(c, cx - 14, yl, 28, cy + 200 - yl, 14, BLUE, a)
    for k, v in enumerate(("10", "5", "0", "−5", "−10")):
        yy = cy - 160 + k * 50
        line(c, cx + 34, yy, cx + 58, yy, INK2, a, 3)
        text(c, v, cx + 70, yy + 11, 28, "black", RED if v == "−5" else INK2, a, align="left")


def relogio(c, cx, cy, r, a, pos=0.0, acesas=None, rot_casa=True, size=58):
    """relógio de quatro horas: casas 1 (em cima), i (direita), −1 (embaixo), −i (esquerda). pos = casa (contínua) do
    ponteiro; acesas = conjunto de casas destacadas"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 16, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r + 16, paint(INK2, a, stroke=6))
    for k in range(4):
        ang = -math.pi / 2 + k * math.pi / 2
        px, py = cx + r * 0.72 * math.cos(ang), cy + r * 0.72 * math.sin(ang)
        on = acesas is not None and k in acesas
        col = CASA_COR[k]
        c.drawCircle(px, py, size * 0.95, paint(mix("#FFFFFF", col, 0.30 if on else 0.10), a))
        if on:
            c.drawCircle(px, py, size * 0.95, paint(col, a, stroke=5))
        expr(c, CASAS[k], px, py, size, a, cores={0: col})
        if rot_casa:
            lx, ly = cx + (r + 82) * math.cos(ang), cy + (r + 44) * math.sin(ang)
            text(c, f"casa {k}", lx, ly + 8, 24, "black", GRAY, a)
    ang = -math.pi / 2 + pos * math.pi / 2
    tx, ty = cx + r * 0.42 * math.cos(ang), cy + r * 0.42 * math.sin(ang)
    line(c, cx, cy, tx, ty, INK, a, 12)
    c.drawCircle(tx, ty, 12, paint(INK, a))
    c.drawCircle(cx, cy, 20, paint(INK, a))


def gemeas(c, cx, y, a, z1, z2, size=64, espelho=1.0):
    """as duas raízes, uma em cima da outra, com o eixo do espelho"""
    if a <= 0:
        return
    expr(c, z1, cx, y, size, a, cores={0: BLUE, 1: BLUE, 2: BLUE})
    expr(c, z2, cx, y + size * 1.7, size, a * espelho, cores={0: BLUE, 1: BLUE, 2: BLUE})
    if espelho > 0:
        yy = y + size * 0.85
        for xx in range(int(cx - 260), int(cx + 260), 32):
            line(c, xx, yy, xx + 16, yy, PURPLE, a * espelho, 4)
        pill(c, "espelho", cx + 300, yy, PURPLE, size=24, a=a * espelho, anchor="left", bounds=(0, 1920))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "NÚMEROS COMPLEXOS · EPISÓDIO 1", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        expr(c, "x^2 + 2x + 5 = 0", 960, 290, 92, aa)
        linha(c, [("Δ = ", INK), ("−16", RED)], 640, 440, 64, ep(t, C["01.a"] + 3.0, 0.5))
        ar = ep(t, C["01.a"] + 4.5, 0.5)
        if ar > 0:
            rrect(c, 900, 390, 680, 100, 22, mix("#FFFFFF", AMBER, 0.14), ar)
            linha(c, [("nenhuma raiz ", INK), ("REAL", AMBER)], 1240, 440, 50, ar)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        c.drawCircle(1488, 440, 96, paint(AMBER, ab, stroke=6))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        cartao(c, 360, 560, 1200, 220, acc, GREEN, True)
        expr(c, "x = −1 + 2i", 660, 670, 66, acc, cores={2: GREEN, 3: GREEN, 4: GREEN})
        expr(c, "x = −1 − 2i", 1260, 670, 66, acc, cores={2: GREEN, 3: GREEN, 4: GREEN})
        selo(c, 1560, 560, acc, "DUAS RAÍZES", GREEN, -6, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "NÚMEROS COMPLEXOS · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de NÚMEROS COMPLEXOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    for k, (cue, tit, f, col) in enumerate((("02.a", "DELTA NEGATIVO", "Δ < 0 → resolver", PURPLE),
                                            ("02.b", "QUALQUER POTÊNCIA", "i^{2026} de cabeça", GREEN))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 320, 340, 640, 340, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 320, 340, 640, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 575, 46, "black", col, ak)
        expr(c, f, x, 630, 40, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "QUATRO LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "Bhaskara", "Δ = b^2 − 4ac · x = −b±√{Δ}/2a", BLUE),
             ("03.b", "Δ negativo", "Δ < 0  →  nenhuma raiz real", AMBER),
             ("03.c", "Potenciação", "√{−4} ∉ reais · a^m · a^n = a^{m+n}", PURPLE),
             ("03.d", "divisão com resto", "2026 = 4 · 506 + 2", GREEN)]
    for k, (cue, rot, f, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 150 + d
        cartao(c, 260, y - 60, 1400, 124, a)
        pill(c, rot, 300, y - 60, col, size=22, a=a)
        expr(c, f, 960, y + 4, 40, a)


# ======================================================================
# concreto — os números que "não existiam"
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "OS NÚMEROS QUE NÃO EXISTIAM", "E PASSARAM A EXISTIR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    ab = ep(t, C["04.b"], 0.5)
    sai = ep(t, C["04.c"], 0.5)
    if aa > 0 and sai < 1:
        a1 = aa * (1 - sai)
        cartao(c, 260, 220, 640, 520, a1)
        text(c, "contar laranjas", 580, 300, 34, "black", INK2, a1)
        expr(c, "−5 laranjas?", 580, 420, 64, a1, cores={0: RED})
        selo(c, 580, 560, a1 * (1 - ab), "NÃO EXISTE?", RED, -5, 36)
        if ab > 0:
            termometro(c, 1280, 470, ab * (1 - sai), ep(t, C["04.b"] + 0.4, 1.2))
            pill(c, "−5 °C existe, sim", 580, 560, GREEN, size=34, a=ab * (1 - sai), anchor="center")
    if sai > 0:
        calculadora(c, 640, 500, sai, ep(t, C["04.e"], 0.8))
        ad = ep(t, C["04.d"], 0.4) * (1 - ep(t, C["04.e"], 0.5))
        if ad > 0:
            selo(c, 1240, 400, ad, "ERRO", RED, -6, 60)
        ae = ep(t, C["04.e"], 0.5)
        if ae > 0:
            rrect(c, 960, 420, 640, 150, 26, mix("#FFFFFF", GREEN, 0.16), ae)
            text_mid(c, "o erro vira um NÚMERO", 1280, 495, 44, "black", GREEN, ae)


# ======================================================================
# bloco a — i² = −1
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "A UNIDADE IMAGINÁRIA", "i TEM UM SUPERPODER", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    defin(c, "UNIDADE IMAGINÁRIA", "o número i, tal que i² = −1", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        cartao(c, 260, 310, 640, 300, ab, PURPLE, True)
        expr(c, "i", 580, 410, 120, ab, cores={0: PURPLE})
        text(c, "ao quadrado vira", 580, 520, 32, "black", INK2, ab)
        expr(c, "−1", 580, 580, 56, ab, cores={0: RED})
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        expr(c, "√{−36} = 6i", 1290, 380, 78, acc, cores={2: GREEN})
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        expr(c, "(6i)^2 = 36 · i^2", 1290, 520, 56, ad)
    ae = ep(t, C["05.e"], 0.5)
    if ae > 0:
        lembrete_i2(c, 1050, 680, ae)
        expr(c, "= −36", 1400, 680, 60, ae, cores={1: GREEN})


def b_atalho_raiz(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "RAIZ DE NEGATIVO EM 3 PASSOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["06"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · TIRE O MENOS, TIRE A RAIZ, COLE O i", 960, 250, 24, "black", GREEN, a0, tracking=2)
    passos = [("06.a", "tire o menos", "√{−16} → √{16}"), ("06.b", "tire a raiz", "√{16} = 4"),
              ("06.c", "cole o i", "4 → 4i")]
    for k, (cue, rot, f) in enumerate(passos):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 500 + k * 460
        rrect(c, x - 200, 320 + d, 400, 230, 24, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, x, 360 + d, ak, 26, bg=GREEN)
        text(c, rot, x, 440 + d, 34, "black", INK2, ak)
        expr(c, f, x, 505 + d, 44, ak, cores={2: GREEN} if k == 2 else None)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        expr(c, "√{−16} = 4i", 700, 680, 56, ad, cores={2: GREEN})
        expr(c, "√{−9} = 3i", 1220, 680, 56, ad, cores={2: GREEN})


# ======================================================================
# bloco b — a forma algébrica e os nomes
# ======================================================================

def b_forma(c, t, C, B):
    head(c, t, B["start"], "A FORMA ALGÉBRICA", "PARTE REAL E PARTE IMAGINÁRIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    defin(c, "NÚMERO COMPLEXO", "z = a + bi, com a e b reais (forma algébrica)", 260, 200, 1400, aa, BLUE, 30)
    ab, acc = ep(t, C["07.b"], 0.5), ep(t, C["07.c"], 0.5)
    ad = ep(t, C["07.d"], 0.5)
    if aa > 0 and ad <= 0:
        cores = {}
        if ab > 0:
            cores[2] = GREEN
        if acc > 0:
            cores[4] = PURPLE
        expr(c, "z = a + bi", 960, 420, 120, aa, cores=cores)
        if ab > 0:
            pill(c, "PARTE REAL: Re(z) = a", 680, 580, GREEN, size=32, a=ab, anchor="center")
        if acc > 0:
            pill(c, "PARTE IMAGINÁRIA: Im(z) = b, sem o i", 1260, 580, PURPLE, size=32, a=acc, anchor="center")
    if ad > 0:
        expr(c, "2 − 3i", 960, 400, 130, ad, cores={0: GREEN, 2: PURPLE})
        cartao(c, 360, 540, 560, 140, ad)
        linha(c, [("Re = ", INK), ("2", GREEN)], 640, 610, 52, ad)
        cartao(c, 1000, 540, 560, 140, ad)
        linha(c, [("Im = ", INK), ("−3", PURPLE)], 1280, 610, 52, ad)
        pill(c, "sem o i", 1280, 720, AMBER, size=26, a=ad, anchor="center")


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "OS NOMES", "REAL · IMAGINÁRIO PURO · NÃO REAL", BLUE)
    card(c, *CARD_R)
    linhas_ = [("08.a", "REAL", "b = 0", "−7 = −7 + 0i", BLUE), ("08.b", "IMAGINÁRIO PURO", "a = 0 e b ≠ 0", "5i", PURPLE),
               ("08.c", "NÃO REAL", "b ≠ 0", "2 − 3i", AMBER)]
    for k, (cue, nome, cond, ex, col) in enumerate(linhas_):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 300 + k * 140 + d
        rrect(c, 260, y - 56, 1400, 112, 20, "#FFFFFF", ak, shadow=True)
        rrect(c, 260, y - 56, 14, 112, 7, col, ak)
        text(c, nome, 310, y + 13, 36, "black", col, ak, align="left")
        expr(c, cond, 960, y, 40, ak)
        expr(c, ex, 1450, y, 44, ak)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        c.drawCircle(960, 730, 0, paint(INK, 0))
        rrect(c, 460, 680, 1000, 100, 22, mix("#FFFFFF", PURPLE, 0.14), ad)
        linha(c, [("REAIS ", BLUE), ("⊂", INK), (" COMPLEXOS (ℂ)", PURPLE)], 960, 730, 46, ad)


# ======================================================================
# bloco c — delta negativo e as gêmeas espelhadas
# ======================================================================

def b_delta(c, t, C, B):
    head(c, t, B["start"], "DELTA NEGATIVO", "A EQUAÇÃO DO GANCHO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        expr(c, "x^2 + 2x + 5 = 0", 960, 260, 70, aa)
        cartao(c, 260, 330, 1400, 110, aa)
        linha(c, [("DISCRIMINANTE: ", BLUE), ("Δ = 4 − 20 = ", INK), ("−16", RED)], 960, 385, 44, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        expr(c, "√{−16} = 4i", 960, 520, 56, ab, cores={2: GREEN})
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        expr(c, "x = −2±4i/2", 700, 690, 60, acc)
        pill(c, "÷ 2 nas DUAS partes", 700, 790, AMBER, size=26, a=acc, anchor="center")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        arrow(c, 1000, 690, 1100, 690, PURPLE, ad, 5, 16)
        expr(c, "−1 ± 2i", 1340, 690, 72, ad, cores={0: GREEN, 1: GREEN, 2: GREEN})


def b_gemeas(c, t, C, B):
    head(c, t, B["start"], "AS GÊMEAS ESPELHADAS", "RAÍZES CONJUGADAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.4)
    gemeas(c, 520, 340, a0, "−1 + 2i", "−1 − 2i", 70, ep(t, C["10.a"], 0.6))
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        defin(c, "CONJUGADAS", "mesma parte real, imaginária com sinal trocado", 260, 210, 1400, ab, BLUE, 28)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        cartao(c, 960, 330, 700, 150, acc)
        linha(c, [("soma = ", INK), ("−2", GREEN), (" = −b/a", PURPLE)], 1310, 405, 44, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        cartao(c, 960, 520, 700, 260, ad)
        expr(c, "produto = 1 − 4i^2", 1310, 580, 40, ad)
        lembrete_i2(c, 1150, 670, ad)
        linha(c, [("= 5", GREEN), (" = c/a", PURPLE)], 1480, 670, 44, ad)


def b_atalho_gemea(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "UMA RAIZ DÁ A OUTRA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · A GÊMEA ESPELHADA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        expr(c, "3 + 5i", 640, 420, 80, aa, cores={0: BLUE, 1: BLUE, 2: BLUE})
        arrow(c, 820, 420, 1060, 420, GREEN, aa, 6, 18)
        text(c, "troque só o sinal do i", 940, 380, 26, "bold", GREEN, aa)
        expr(c, "3 − 5i", 1280, 420, 80, ep(t, C["11.a"] + 1.4, 0.5), cores={0: BLUE, 1: BLUE, 2: BLUE})
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        pill(c, "confira: SOMA e PRODUTO · 10 segundos", 960, 620, GREEN, size=38, a=ab, anchor="center")


# ======================================================================
# questão 8 (nós fazemos)
# ======================================================================

ALTS8 = [("A", "= 2 ± 3i", "", GREEN), ("B", "= −2 ± 3i", "b no lugar de −b", RED),
         ("C", "= 2 ± 6i", "dividiu só o 4", RED), ("D", "= 4 ± 6i", "não dividiu por 2a", RED),
         ("E", "inexistentes (Δ < 0)", "só nos reais", RED)]


def b_q8(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head(c, t, B["start"] if sid == "12" else C["13"], "QUESTÃO 8 · ESTILO ENEM",
         "NÓS FAZEMOS" if sid == "12" else "VAMOS JUNTOS", GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"12.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"13.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS8, 1130, 250, 600, 34, C["13.ok"], "A", cues_in, cues_x, gap=28)
    a0 = ep(t, C["12.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        expr(c, "x^2 − 4x + 13 = 0", 640, 300, 62, a0)
        text(c, "raízes nos complexos = ?", 640, 390, 34, "black", INK2, a0)
    if sid == "12":
        pause_timer(c, t, C["12.end"] - 1.9, 640, 600)
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 450, 880, 90, 18, "#FFFFFF", aa, shadow=True)
        expr(c, "Δ = 16 − 52 = −36 · √{−36} = 6i", 640, 495, 36, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 200, 560, 880, 100, 18, mix("#FFFFFF", GREEN, 0.14), ab)
        expr(c, "x = 4±6i/2 = 2 ± 3i", 640, 610, 40, ab, cores={4: GREEN, 5: GREEN, 6: GREEN})
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        expr(c, "soma = 4 · produto = 4 + 9 = 13", 640, 720, 34, acc)


# ======================================================================
# bloco d — o cuidado com raízes de negativos
# ======================================================================

def b_cuidado(c, t, C, B):
    head(c, t, B["start"], "PEGADINHA", "RAIZ DE NEGATIVO VEZES RAIZ DE NEGATIVO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        expr(c, "√{−4} · √{−9} = ?", 960, 270, 72, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        cartao(c, 260, 360, 660, 320, ab, RED, True)
        expr(c, "√{(−4)(−9)}", 590, 450, 52, ab)
        expr(c, "= √{36} = 6", 590, 560, 52, ab, cores={3: RED})
        acx = ep(t, C["14.c"], 0.4)
        if acx > 0:
            line(c, 300, 620, 880, 400, RED, acx, 8)
            selo(c, 590, 660, acx, "NÃO", RED, -6, 40)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        cartao(c, 1000, 360, 660, 320, acc, GREEN, True)
        text(c, "com i PRIMEIRO", 1330, 410, 30, "black", GREEN, acc)
        expr(c, "2i · 3i = 6i^2", 1330, 490, 52, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        lembrete_i2(c, 1180, 600, ad)
        expr(c, "= −6", 1500, 600, 56, ad, cores={1: GREEN})


# ======================================================================
# bloco e — o relógio de quatro horas e o resto por 4
# ======================================================================

def b_relogio(c, t, C, B):
    head(c, t, B["start"], "AS POTÊNCIAS DE i", "UM RELÓGIO DE QUATRO HORAS", PURPLE)
    card(c, *CARD_R)
    cues = ["15.a", "15.b", "15.c", "15.d", "15.e"]
    pot = [("i^0 = 1", ""), ("i^1 = i", ""), ("i^2 = −1", ""), ("i^3 = i^2 · i = −i", ""),
           ("i^4 = (i^2)^2 = 1", "")]
    n = sum(1 for cu in cues if t >= C[cu])
    for k, cu in enumerate(cues):
        ak, d = rise(t, C[cu])
        if ak <= 0:
            continue
        y = 250 + k * 108 + d
        expr(c, pot[k][0], 330, y, 48, ak, align="left", cores={0: CASA_COR[k % 4]})
    a0 = ep(t, C["15"], 0.4)
    if n:
        k_last = n - 1
        t_last = C[cues[k_last]]
        pos = (k_last - 1) + ep(t, t_last, 0.6) if k_last >= 1 else 0
        if k_last == 0:
            pos = 0
        relogio(c, 1300, 520, 240, a0, pos, acesas={k_last % 4})
    else:
        relogio(c, 1300, 520, 240, a0, 0)
    af = ep(t, C["15.f"], 0.5)
    if af > 0:
        pill(c, "× i = o ponteiro ANDA UMA CASA", 560, 790, PURPLE, size=30, a=af, anchor="center")


def b_resto(c, t, C, B):
    head(c, t, B["start"], "EXPOENTE ENORME", "SÓ IMPORTA O RESTO POR 4", PURPLE)
    card(c, *CARD_R)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        regra(c, "só importa o RESTO da divisão por 4", 600, 250, ab, 36, PURPLE)
    a0 = ep(t, C["16"], 0.4)
    aa = ep(t, C["16.a"], 0.4)
    # a volta completa (16.a) e as 506 voltas (16.d)
    pos = 0.0
    voltas = 0
    t_d = C["16.d"]
    ae = ep(t, C["16.e"], 0.5)
    if t >= t_d and ae <= 0:
        prog = clamp((t - t_d) / 3.2)
        voltas = int(506 * prog)
        pos = 4 * 506 * prog + 1 * ep(t, t_d + 3.2, 0.5)
        pos = pos % 4 if prog < 1 else 1 * ep(t, t_d + 3.2, 0.5)
    elif ae > 0:
        pos = 3 * ep(t, C["16.e"] + 1.2, 0.6)
    elif aa > 0:
        pos = 4 * clamp((t - C["16.a"]) / 2.0)
    acesa = {1} if (t >= t_d + 3.2 and ae <= 0) else ({3} if ae > 0 and t > C["16.e"] + 1.8 else None)
    relogio(c, 1380, 520, 240, a0, pos, acesas=acesa)
    if t >= t_d and ae <= 0:
        rrect(c, 490, 720, 260, 70, 18, INK, a0)
        text(c, f"{voltas} voltas", 620, 768, 32, "black", "#FFFFFF", a0)
    acc = ep(t, C["16.c"], 0.5) * (1 - ae)
    if acc > 0:
        cartao(c, 220, 340, 800, 330, acc)
        expr(c, "i^{2025}", 620, 420, 80, acc, cores={0: PURPLE})
        expr(c, "2025 = 4 · 506 + 1", 620, 530, 46, acc, cores={6: GREEN})
        ad = ep(t, t_d + 3.4, 0.5)
        if ad > 0:
            linha(c, [("casa 1  →  ", INK), ("i", GREEN)], 620, 620, 48, ad)
    if ae > 0:
        cartao(c, 220, 340, 800, 330, ae)
        expr(c, "i^{103}", 620, 420, 80, ae, cores={0: PURPLE})
        expr(c, "103 = 4 · 25 + 3", 620, 530, 46, ae, cores={6: AMBER})
        linha(c, [("casa 3  →  ", INK), ("−i", AMBER)], 620, 620, 48, ep(t, C["16.e"] + 1.8, 0.5))


def b_atalho_resto(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "OS DOIS ÚLTIMOS ALGARISMOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["17"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · O RESTO MORA NO FIM DO NÚMERO", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        for cx_, ini, fim in ((620, "20", "25"), (1300, "1", "03")):
            text(c, ini, cx_, 440, 110, "black", "#B9B9B9", aa, align="right")
            text(c, fim, cx_, 440, 110, "black", GREEN, aa, align="left")
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        pill(c, "100 é múltiplo de 4", 960, 520, PURPLE, size=32, a=ab, anchor="center")
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("25 → resto ", INK), ("1", GREEN)], 620, 650, 46, acc)
        linha(c, [("03 → resto ", INK), ("3", GREEN)], 1300, 650, 46, ep(t, C["17.c"] + 2.2, 0.5))


# ======================================================================
# bloco f — quatro seguidas somam zero
# ======================================================================

def b_soma4(c, t, C, B):
    head(c, t, B["start"], "QUATRO SEGUIDAS", "UMA VOLTA INTEIRA SOMA ZERO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        expr(c, "1 + i + (−1) + (−i)", 900, 300, 72, aa)
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        expr(c, "= 0", 1450, 300, 80, ab, cores={1: GREEN})
        pill(c, "4 seguidas = ZERO", 960, 410, GREEN, size=34, a=ab, anchor="center")
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        cartao(c, 260, 480, 1400, 260, acc)
        expr(c, "i + i^2 + i^3 + ... + i^{100}", 960, 550, 56, acc)
        linha(c, [("100 termos = ", INK), ("25 grupos de 4", PURPLE)], 960, 640, 42, acc)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        selo(c, 1520, 700, ad, "SOMA = 0", GREEN, -6, 40)


# ======================================================================
# nós fazemos — i^35 e i^48
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "O RESTO POR 4", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    sol = t >= C["20"]
    for k, (e, cue, conta, res, casa) in enumerate((("i^{35}", "20.a", "35 = 4 · 8 + 3", "−i", 3),
                                                    ("i^{48}", "20.b", "48 = 4 · 12 + 0", "1", 0))):
        y = 330 + k * 220
        if aa > 0:
            cartao(c, 260, y - 90, 860, 180, aa)
            expr(c, e, 400, y, 80, aa, cores={0: PURPLE})
        ak = ep(t, C[cue], 0.5) if sol else 0
        if ak > 0:
            expr(c, conta, 800, y - 30, 40, ak)
            linha(c, [(f"casa {casa}  →  ", INK), (res, GREEN)], 800, y + 45, 44, ak)
        elif aa > 0:
            text(c, "= ?", 800, y + 18, 56, "black", GRAY, aa)
    if not sol:
        pause_timer(c, t, C["19.end"] - 1.9, 1420, 520)
    else:
        ab = ep(t, C["20.b"], 0.5)
        pos = 3 * ep(t, C["20.a"], 0.8) + (1 * ep(t, C["20.b"], 0.8))
        relogio(c, 1420, 520, 220, ep(t, C["20"], 0.4), pos, acesas={0} if ab > 0.5 else {3}, rot_casa=False, size=46)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["i ao quadrado é −1.",
          "Delta negativo: nenhuma raiz real, mas duas raízes complexas conjugadas.",
          "Potência de i: só importa o resto por 4."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "28"])
    frame(c, t, B["start"] if sid == "21" else C["28"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("i² = 1  →  (3i)² = 9",
          "todo quadrado que você conhecia dava positivo",
          "i² = −1: (3i)² = 9 · i² = −9."),
         ("Im(3 − 4i) = −4i",
          "o i \"mora\" na parte imaginária",
          "a parte imaginária é só o número que multiplica o i: −4."),
         ("√−4 · √−9 = √36 = 6",
          "nos positivos, raiz vezes raiz é a raiz do produto",
          "com negativo, escreva com i primeiro: 2i · 3i = −6."),
         ("Δ < 0: não há raízes",
          "foi exatamente o que você aprendeu na série de Bhaskara",
          "não há raízes REAIS; nos complexos, há duas (conjugadas).")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25"], ERROS)


# ======================================================================
# questão 1 (você faz)
# ======================================================================

ALTS1 = [("A", "= 1 + i", "i² = 1 e i³ = i", RED), ("B", "= −1 + i", "errou só o i³", RED),
         ("C", "= −1 − i", "", GREEN), ("D", "= 1 − i", "errou só o i²", RED),
         ("E", "= 0", "duas seguidas não somam 0", RED)]


def b_q1(c, t, C, B):
    sid = which(t, C, ["26", "27"])
    head(c, t, B["start"] if sid == "26" else C["27"], "QUESTÃO 1 · ESTILO ENEM",
         "VOCÊ FAZ" if sid == "26" else "VAMOS CONFERIR", GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS1, 1260, 250, 460, 38, C["27.ok"], "C", cues_in, cues_x, gap=30)
    a0 = ep(t, C["26.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        expr(c, "i^{2026} + i^{2027} = ?", 660, 290, 70, a0, cores={0: PURPLE, 2: PURPLE})
    if sid == "26":
        pause_timer(c, t, C["26.end"] - 1.9, 660, 560)
        return
    aa = ep(t, C["27.a"], 0.5)
    ab = ep(t, C["27.b"], 0.5)
    pos = 2 * ep(t, C["27.a"], 0.8) + ep(t, C["27.b"], 0.6)
    relogio(c, 1000, 560, 150, aa, pos, acesas={3} if ab > 0.5 else {2}, rot_casa=False, size=34)
    if aa > 0:
        linha(c, [("2026: resto 2 → ", INK), ("−1", RED)], 470, 420, 38, aa)
    if ab > 0:
        linha(c, [("2027: resto 3 → ", INK), ("−i", AMBER)], 470, 500, 38, ab)
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        rrect(c, 200, 600, 560, 110, 20, mix("#FFFFFF", GREEN, 0.16), acc)
        expr(c, "soma = −1 − i", 480, 655, 48, acc, cores={2: GREEN, 3: GREEN, 4: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AS OPERAÇÕES", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        cartao(c, 360, 240, 1200, 300, aa)
        expr(c, "(2+3i)(1−i)", 960, 320, 78, aa, cores={0: PURPLE})
        expr(c, "= 2 − 2i + 3i − 3i^2", 960, 450, 56, aa, cores={6: AMBER, 7: AMBER})
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        pill(c, "o −3i² decide: a CERTA ou a PEGADINHA?", 960, 640, AMBER, size=36, a=ab, anchor="center")
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        selo(c, 960, 770, acc, "PRÓXIMO EPISÓDIO", PURPLE, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Quanto vale i elevado a 2030?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              atalho_raiz=b_atalho_raiz, forma=b_forma, tabela=b_tabela, delta=b_delta, gemeas=b_gemeas,
              atalho_gemea=b_atalho_gemea, q8=b_q8, cuidado=b_cuidado, relogio=b_relogio, resto=b_resto,
              atalho_resto=b_atalho_resto, soma4=b_soma4, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1,
              ponte=b_ponte, cta=b_cta)
