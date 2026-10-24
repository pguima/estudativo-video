"""Visual — Números Complexos, Episódio 4: forma trigonométrica e De Moivre (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: plano() (o plano de Argand-Gauss, com anéis de radar opcionais), seta() (a seta da origem até o
ponto), arco() (o ângulo medido a partir do eixo real positivo), tabela_trig() (a tabela de seno e cosseno da tela),
tri() (o endereço ρ(cos θ + i sen θ) com a raiz bem desenhada).
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
ARQUIVO_FINAL = "enem_matematica_complexos_ep4_de_moivre.mp4"
CARD_R = K.CARD_R
RADAR = "#2E9E6B"
S3 = math.sqrt(3)


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


def plano(c, cx, cy, R, unit, a, radar=False, rotulos=True, ticks=()):
    """plano de Argand-Gauss centrado em (cx, cy); R = meio comprimento dos eixos (px). Devolve (X, Y)."""
    X = lambda v: cx + v * unit
    Y = lambda v: cy - v * unit
    if a <= 0:
        return X, Y
    if radar:
        for k in (1, 2, 3):
            c.drawCircle(cx, cy, R * k / 3, paint(RADAR, a * 0.35, stroke=2))
    arrow(c, cx - R, cy, cx + R + 10, cy, INK2, a, 4, 14)
    arrow(c, cx, cy + R, cx, cy - R - 10, INK2, a, 4, 14)
    if rotulos:
        text(c, "real", cx + R - 10, cy + 40, 24, "black", INK2, a)
        text(c, "imaginário", cx + 16, cy - R - 4, 24, "black", INK2, a, align="left")
    for v, s_, eixo in ticks:
        if eixo == "x":
            line(c, X(v), cy - 8, X(v), cy + 8, INK2, a, 3)
            text(c, s_, X(v), cy + 40, 24, "black", INK2, a)
        else:
            line(c, cx - 8, Y(v), cx + 8, Y(v), INK2, a, 3)
            text(c, s_, cx - 16, Y(v) + 9, 24, "black", INK2, a, align="right")
    return X, Y


def seta(c, cx, cy, ang, L, col, a, w=7, ponto=True):
    """seta da origem até o ponto de ângulo `ang` (graus, anti-horário) e comprimento L (px)"""
    if a <= 0 or L <= 1:
        return cx, cy
    x1 = cx + L * math.cos(math.radians(ang))
    y1 = cy - L * math.sin(math.radians(ang))
    arrow(c, cx, cy, x1, y1, col, a, w, 20)
    if ponto:
        c.drawCircle(x1, y1, 10, paint(col, a))
    return x1, y1


def arco(c, cx, cy, r, a0, a1, col, a, w=5):
    """arco do ângulo, de a0 a a1 graus (anti-horário)"""
    if a <= 0 or abs(a1 - a0) < 0.5:
        return
    rect = skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r)
    c.drawArc(rect, -a0, -(a1 - a0), False, paint(col, a, stroke=w))


def rotulo_ang(c, cx, cy, r, ang, s_, col, a, size=30):
    if a <= 0:
        return
    m = math.radians(ang)
    pill(c, s_, cx + r * math.cos(m), cy - r * math.sin(m), col, size=size, a=a, anchor="center", bounds=(0, 1920))


def tri(c, mod, ang, cx, cy, size, a, col=None, align="center"):
    """mod(cos ang + i sen ang): mod em expr (aceita √{2}), o resto em texto"""
    if a <= 0:
        return
    resto = f"(cos {ang} + i sen {ang})"
    w1 = math_w(mod, size)
    w2 = ftext_w(resto, "black", size)
    x = cx - (w1 + w2) / 2 if align == "center" else cx
    expr(c, mod, x, cy, size, a, align="left", cores={0: col} if col else None)
    ftext(c, resto, x + w1 + 4, cy + size * 0.36, size, "black", col or INK, a, align="left")


TRIG = [("30°", "√{3}/2", "1/2"), ("45°", "√{2}/2", "√{2}/2"), ("60°", "1/2", "√{3}/2"), ("90°", "0", "1"),
        ("180°", "−1", "0"), ("360°", "1", "0")]


def tabela_trig(c, x, y, a, acesos=(), cw=200, size=40):
    """a tabela de seno e cosseno (só valores, sem ciclo); acesos = índices das colunas destacadas"""
    if a <= 0:
        return
    w = 150 + cw * len(TRIG)
    rrect(c, x, y, w, 300, 22, "#FFFFFF", a, shadow=True)
    for k, (ang, co, se) in enumerate(TRIG):
        cx = x + 150 + cw * k + cw / 2
        if k in acesos:
            rrect(c, cx - cw / 2 + 8, y + 10, cw - 16, 280, 16, mix("#FFFFFF", PURPLE, 0.18), a)
        text(c, ang, cx, y + 70, size * 0.85, "black", PURPLE, a)
        expr(c, co, cx, y + 155, size, a)
        expr(c, se, cx, y + 245, size, a)
    text(c, "cos", x + 75, y + 168, size * 0.8, "black", INK2, a)
    text(c, "sen", x + 75, y + 258, size * 0.8, "black", INK2, a)
    line(c, x + 20, y + 105, x + w - 20, y + 105, LIGHT, a, 3)


def radar_tela(c, cx, cy, R, t, a):
    """a tela de um radar: disco escuro, anéis e o feixe girando"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, R, paint("#0F2A22", a))
    for k in (1, 2, 3):
        c.drawCircle(cx, cy, R * k / 3, paint("#3FD69A", a * 0.45, stroke=2))
    line(c, cx - R, cy, cx + R, cy, "#3FD69A", a * 0.45, 2)
    line(c, cx, cy - R, cx, cy + R, "#3FD69A", a * 0.45, 2)
    ang = (t * 70) % 360
    for j in range(18):
        g = ang - j * 2.2
        x1 = cx + R * math.cos(math.radians(g)); y1 = cy - R * math.sin(math.radians(g))
        line(c, cx, cy, x1, y1, "#3FD69A", a * (0.6 - j * 0.032), 5)


def potencia_anim(c, cx, cy, t, t0, dur, ang0, n, rho0, a, col=None, escala=lambda r: 70 * r ** 0.6, fim=None):
    """a seta girando de ang0 em ang0 (n passos) enquanto o comprimento cresce: rho0^k. Devolve o passo atual."""
    u = clamp((t - t0) / dur) if dur > 0 else 1.0
    k = min(n, int(u * n + 1e-9)) if u < 1 else n
    frac = u * n - k if u < 1 else 0
    ang = ang0 * (k + frac)
    rho = rho0 ** (k + frac)
    for j in range(1, k + 1):
        aj = a * 0.25
        seta(c, cx, cy, ang0 * j, escala(rho0 ** j), LIGHT, aj, 4, False)
    arco(c, cx, cy, 60, 0, ang, AMBER, a, 5)
    seta(c, cx, cy, ang, escala(rho), col or PURPLE, a, 8)
    return k, ang, rho


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "NÚMEROS COMPLEXOS · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    plano(c, 560, 500, 300, 1, aa, radar=True, rotulos=False)
    if aa > 0:
        expr(c, "(1+i)^8", 1260, 280, 90, aa, cores={0: PURPLE})
        u = clamp((t - C["01.a"] - 0.8) / 2.0)
        n = int(u * 8)
        if t < C["01.b"]:
            linha(c, [("(1 + i)·" * max(1, n) + "…", INK2)], 1260, 400, 30, aa * 0.9)
            pill(c, "8 multiplicações?", 1260, 470, AMBER, size=30, a=ep(t, C["01.a"] + 1.4, 0.4), anchor="center")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        t_end = C["01.d"] - 0.3
        k, ang, rho = potencia_anim(c, 560, 500, t, C["01.b"] + 0.3, max(1.0, t_end - C["01.b"] - 0.3), 45, 8,
                                    math.sqrt(2), ab, PURPLE, lambda r: 60 * r ** 0.6)
        cartao(c, 1000, 380, 560, 110, ab)
        expr(c, "(√{2})^8 = 16", 1280, 435, 50, ab, cores={2: GREEN})
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        cartao(c, 1000, 520, 560, 110, acc)
        expr(c, "8 · 45° = 360°", 1280, 575, 50, acc, cores={4: AMBER})
        pill(c, "uma volta inteira", 1280, 668, AMBER, size=26, a=acc, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "16", 560 + 60 * 16 ** 0.6 + 50, 500, GREEN, size=40, a=ad, anchor="left", bounds=(0, 1920))
        selo(c, 1280, 770, ad, "= 16, EM UMA LINHA", GREEN, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "COMPLEXOS · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de NÚMEROS COMPLEXOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    itens = [("02.a", "DISTÂNCIA E ÂNGULO", "o endereço do radar", BLUE),
             ("02.b", "MULTIPLICAR", "esticar e girar", PURPLE), ("02.c", "DE MOIVRE", "potências altas", GREEN)]
    for k, (cue, tit, sb, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 220, 340, 440, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 220, 340, 440, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 38, "black", col, ak)
        text(c, sb, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    rows = [("03.a", "episódio 3", "a + bi  →  ponto (a, b)   ·   módulo = distância até a origem", BLUE),
            ("03.b", "episódio 1", "o relógio do i:  1  →  i  →  −1  →  −i", PURPLE),
            ("03.c", "Trigonometria", "tabela de seno e cosseno na tela (série própria)", AMBER)]
    for k, (cue, rot, s_, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 170 + d
        cartao(c, 260, y - 62, 1400, 124, a)
        pill(c, rot, 300, y - 62, col, size=22, a=a)
        text_mid(c, s_, 960, y + 8, 38, "black", INK, a)


def b_tabela(c, t, C, B):
    frame(c, t, B["start"], "A TABELA DA TELA", "SENO E COSSENO", AMBER)
    a0 = ep(t, C["04"], 0.5)
    acesos = []
    for k, cue in enumerate(("04.a", "04.b", "04.c")):
        if C[cue] <= t < (C[("04.b", "04.c", "04.d")[k]]):
            acesos = [k]
    if t >= C["04.d"]:
        acesos = [3, 4, 5]
    tabela_trig(c, 260, 270, a0, acesos)
    if a0 > 0:
        pill(c, "isso tem série própria: TRIGONOMETRIA", W / 2, 680, AMBER, size=28, a=a0, anchor="center")
    ab = ep(t, C["04.b"], 0.4) * (1 - ep(t, C["04.c"], 0.3))
    if ab > 0:
        text_mid(c, "em 45°, seno = cosseno", W / 2, 760, 36, "black", PURPLE, ab)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "A TELA DO RADAR", "O CONCRETO ANTES DA CONTA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["05"], 0.5)
    cx, cy, R = 560, 500, 300
    radar_tela(c, cx, cy, R, t, a0)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        cartao(c, 960, 260, 680, 120, aa)
        text_mid(c, "“a 2 milhas, na direção de 60°”", 1300, 320, 38, "black", BLUE, aa)
    ab = ep(t, C["05.b"], 0.5)
    L = R * 2 / 3
    if ab > 0:
        x1, y1 = cx + L * math.cos(math.radians(60)), cy - L * math.sin(math.radians(60))
        arrow(c, cx, cy, x1, y1, "#FFD166", ab, 6, 18)
        arco(c, cx, cy, 70, 0, 60, "#FFD166", ab, 5)
        c.drawCircle(x1, y1, 16, paint("#FFD166", ab))
        text(c, "60°", cx + 100, cy - 40, 30, "black", "#FFD166", ab)
        text(c, "2", (cx + x1) / 2 - 30, (cy + y1) / 2, 32, "black", "#FFD166", ab)
        cartao(c, 960, 420, 680, 110, ab, BLUE, True)
        text_mid(c, "distância  +  direção", 1300, 475, 40, "black", BLUE, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        x1, y1 = cx + L * math.cos(math.radians(60)), cy - L * math.sin(math.radians(60))
        line(c, x1, y1, x1, cy, "#FFFFFF", acc * 0.8, 3)
        line(c, cx, cy, x1, cy, "#FFFFFF", acc * 0.8, 5)
        cartao(c, 960, 560, 680, 110, acc, PURPLE, True)
        text_mid(c, "para o lado  +  para cima", 1300, 615, 40, "black", PURPLE, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1300, 760, ad, "O MESMO ENDEREÇO", GREEN, -4, 34)


# ======================================================================
# bloco a — módulo e argumento
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "O ENDEREÇO DO RADAR", "MÓDULO E ARGUMENTO", BLUE)
    card(c, *CARD_R)
    cx, cy = 470, 560
    a0 = ep(t, C["06"], 0.5)
    plano(c, cx, cy, 260, 1, a0, radar=True)
    ang, L = 35, 220
    aa = ep(t, C["06.a"], 0.5)
    x1, y1 = seta(c, cx, cy, ang, L * aa if aa > 0 else 0, BLUE, aa)
    if aa > 0:
        pill(c, "ρ", (cx + x1) / 2 - 30, (cy + y1) / 2 - 40, BLUE, size=34, a=aa, anchor="center")
        defin(c, "MÓDULO  ρ (rô)", "distância até a origem", 800, 200, 860, aa, BLUE, 30)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        arco(c, cx, cy, 80, 0, ang * ab, AMBER, ab, 6)
        text(c, "θ", cx + 112, cy - 22, 36, "black", AMBER, ab)
        defin(c, "ARGUMENTO  θ (teta)", "ângulo com o eixo real positivo", 800, 300, 860, ab, BLUE, 30)
        text(c, "de 0° a 360°", 1230, 420, 28, "black", INK2, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        line(c, x1, y1, x1, cy, PURPLE, acc, 4)
        line(c, cx, cy + 4, x1, cy + 4, PURPLE, acc, 6)
        text(c, "a", (cx + x1) / 2, cy + 44, 32, "black", PURPLE, acc)
        text(c, "b", x1 + 26, (cy + y1) / 2, 32, "black", PURPLE, acc)
        cartao(c, 800, 470, 860, 110, acc)
        linha(c, [("a = ρ·cos θ", PURPLE), ("      ", INK), ("b = ρ·sen θ", PURPLE)], 1230, 525, 42, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        K.boxed(c, 800, 610, 860, 170, PURPLE, ad, 0.10)
        text(c, "FORMA TRIGONOMÉTRICA (POLAR)", 1230, 650, 22, "black", PURPLE, ad, tracking=2)
        linha(c, [("z = ρ(cos θ + i sen θ)", PURPLE)], 1230, 722, 54, ad)


# ======================================================================
# bloco b — o exemplo √3 + i e a tabela de endereços
# ======================================================================

def b_exemplo(c, t, C, B):
    head(c, t, B["start"], "TESTANDO", "√3 + i NO RADAR", PURPLE)
    card(c, *CARD_R)
    cx, cy, u = 400, 600, 140
    a0 = ep(t, C["07"], 0.5)
    X, Y = plano(c, cx, cy, 300, u, a0, ticks=((S3, "√3", "x"), (1, "1", "y")))
    if a0 > 0:
        expr(c, "z = √{3} + i", 1180, 240, 56, a0, cores={2: PURPLE})
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        line(c, X(S3), Y(1), X(S3), cy, LIGHT, aa, 3)
        line(c, cx, Y(1), X(S3), Y(1), LIGHT, aa, 3)
        c.drawCircle(X(S3), Y(1), 12, paint(PURPLE, aa))
        pill(c, "1º quadrante", X(S3) + 20, Y(1) - 50, BLUE, size=26, a=aa, anchor="left", bounds=(0, 1920))
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        seta(c, cx, cy, 30, 2 * u, PURPLE, ab)
        cartao(c, 860, 310, 760, 110, ab)
        expr(c, "ρ = √{3+1} = √{4} = 2", 1240, 365, 46, ab, cores={6: GREEN})
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        cartao(c, 860, 450, 760, 140, acc)
        expr(c, "cos θ = √{3}/2", 1050, 520, 44, acc)
        expr(c, "sen θ = 1/2", 1440, 520, 44, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        arco(c, cx, cy, 90, 0, 30, AMBER, ad, 6)
        text(c, "30°", cx + 130, cy - 20, 32, "black", AMBER, ad)
        rrect(c, 860, 620, 760, 130, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        tri(c, "2", "30°", 1240, 685, 52, ad, GREEN)


def b_tabela07(c, t, C, B):
    head(c, t, B["start"], "ENDEREÇOS PRONTOS", "MÓDULO E ARGUMENTO", PURPLE)
    card(c, *CARD_R)
    cx, cy, u = 430, 520, 170
    a0 = ep(t, C["08"], 0.5)
    plano(c, cx, cy, 270, u, a0, ticks=((1, "1", "x"), (-1, "−1", "x")))
    if a0 > 0:
        cartao(c, 860, 220, 800, 90, a0)
        for j, s_ in enumerate(("complexo", "módulo", "argumento")):
            text(c, s_, 1000 + j * 260, 278, 30, "black", INK2, a0)
    rows = [("08.a", "1 + i", "√{2}", "45°", 45, math.sqrt(2), PURPLE),
            ("08.b", "i", "1", "90°", 90, 1, BLUE), ("08.c", "−1", "1", "180°", 180, 1, GREEN)]
    for k, (cue, z, m, g, ang, r, col) in enumerate(rows):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 390 + k * 130 + d
        cartao(c, 860, y - 52, 800, 104, ak)
        expr(c, z, 1000, y, 46, ak, cores={0: col})
        expr(c, m, 1260, y, 46, ak)
        text_mid(c, g, 1520, y, 46, "black", col, ak)
        seta(c, cx, cy, ang, r * u, col, ak)
        arco(c, cx, cy, 50 + k * 22, 0, ang, col, ak * 0.7, 4)


def b_atalho_tabela(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ACHAR O ÂNGULO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · DIVIDA PELO MÓDULO E PROCURE NA TABELA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        badge_num(c, 1, 380, 360, aa, 30, bg=GREEN)
        expr(c, "ρ = √{a^2+b^2}", 700, 360, 52, aa)
        badge_num(c, 2, 380, 500, aa, 30, bg=GREEN)
        expr(c, "cos θ = a/ρ", 760, 500, 50, aa, cores={0: PURPLE, 1: PURPLE})
        expr(c, "sen θ = b/ρ", 1260, 500, 50, aa, cores={0: PURPLE, 1: PURPLE})
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        badge_num(c, 3, 380, 650, ab, 30, bg=GREEN)
        text_mid(c, "procure o PAR na tabela  →  o ângulo aparece", 960, 650, 42, "black", INK, ab)


# ======================================================================
# bloco c — o quadrante
# ======================================================================

def quadrantes(c, X, Y, cx, cy, R, a, destaque=None):
    if a <= 0:
        return
    for q, (sx, sy, s_) in enumerate(((1, 1, "1º"), (-1, 1, "2º"), (-1, -1, "3º"), (1, -1, "4º")), 1):
        if destaque == q:
            x0 = cx if sx > 0 else cx - R
            y0 = cy - R if sy > 0 else cy
            rrect(c, x0, y0, R, R, 0, BLUE, a * 0.10)
        text(c, s_, cx + sx * R * 0.88, cy - sy * R * 0.88 + 12, 34, "black", mix(INK2, "#FFFFFF", 0.3), a)


def b_quadrante(c, t, C, B):
    head(c, t, B["start"], "E DO OUTRO LADO?", "OS SINAIS ESCOLHEM O QUADRANTE", BLUE)
    card(c, *CARD_R)
    cx, cy, u = 470, 520, 190
    a0 = ep(t, C["10"], 0.5)
    X, Y = plano(c, cx, cy, 280, u, a0, ticks=((-1, "−1", "x"), (1, "1", "y")))
    aa = ep(t, C["10.a"], 0.5)
    quadrantes(c, X, Y, cx, cy, 280, aa, 2 if aa > 0 else None)
    if aa > 0:
        line(c, X(-1), Y(1), X(-1), cy, LIGHT, aa, 3)
        c.drawCircle(X(-1), Y(1), 12, paint(PURPLE, aa))
        expr(c, "z = −1 + i", 1230, 240, 54, aa, cores={2: PURPLE})
        defin(c, "QUADRANTE", "um dos 4 pedaços do plano", 860, 300, 760, aa, BLUE, 28)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        seta(c, cx, cy, 135, math.sqrt(2) * u, PURPLE, ab)
        arco(c, cx, cy, 100, 135, 180, AMBER, ab, 6)
        text(c, "45°", cx - 150, cy - 30, 30, "black", AMBER, ab)
        defin(c, "ÂNGULO DE REFERÊNCIA", "o dos números SEM sinal", 860, 400, 760, ab, BLUE, 28)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        cartao(c, 860, 510, 760, 100, acc)
        linha(c, [("a < 0", RED), ("  e  ", INK2), ("b > 0", GREEN), ("  →  2º quadrante", BLUE)], 1240, 560, 38, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        arco(c, cx, cy, 64, 0, 135 * ad, PURPLE, ad, 7)
        rrect(c, 860, 640, 760, 120, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        expr(c, "θ = 180° − 45° = 135°", 1240, 700, 48, ad, cores={6: GREEN})


def b_atalho_quadrante(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O ÂNGULO PELO QUADRANTE", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    cx, cy, R = 960, 500, 300
    if a0 > 0:
        K.boxed(c, 260, 190, 1400, 620, GREEN, a0, 0.06)
        line(c, cx - R - 60, cy, cx + R + 60, cy, INK2, a0, 4)
        line(c, cx, cy - R + 20, cx, cy + R - 20, INK2, a0, 4)
        text(c, "ref = ângulo de referência", 960, 790, 26, "black", INK2, a0)
    itens = [("11.a", 1, 1, "1º", "θ = ref"), ("11.b", -1, 1, "2º", "θ = 180° − ref"),
             ("11.c", -1, -1, "3º", "θ = 180° + ref"), ("11.d", 1, -1, "4º", "θ = 360° − ref")]
    for cue, sx, sy, q, s_ in itens:
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = cx + sx * 330
        y = cy - sy * 150
        pill(c, q, x, y - 52, BLUE, size=28, a=ak, anchor="center")
        linha(c, [(s_, PURPLE)], x, y + 16, 44, ak)


# ======================================================================
# bloco d — multiplicar é girar
# ======================================================================

def b_produto(c, t, C, B):
    head(c, t, B["start"], "MULTIPLICAR É GIRAR", "ESTICA E GIRA", PURPLE)
    card(c, *CARD_R)
    cx, cy, u = 470, 610, 52
    a0 = ep(t, C["12"], 0.5)
    plano(c, cx, cy, 340, u, a0)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        regra(c, "× os módulos  ·  + os ângulos", 1240, 240, aa, 36)
    ab = ep(t, C["12.b"], 0.5)
    ad = ep(t, C["12.d"], 0.5)
    if ab > 0:
        seta(c, cx, cy, 30, 2 * u, BLUE, ab * (1 - 0.6 * ad))
        seta(c, cx, cy, 60, 3 * u, GREEN, ab * (1 - 0.6 * ad))
        cartao(c, 860, 320, 760, 110, ab)
        linha(c, [("2, com 30°", BLUE), ("   ×   ", INK2), ("3, com 60°", GREEN)], 1240, 375, 42, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        cartao(c, 860, 460, 760, 150, acc)
        linha(c, [("módulo: 2 · 3 = ", INK), ("6", PURPLE)], 1240, 505, 38, acc)
        linha(c, [("ângulo: 30° + 60° = ", INK), ("90°", PURPLE)], 1240, 565, 38, acc)
        if ad <= 0:
            seta(c, cx, cy, 90, 6 * u, PURPLE, acc)
            pill(c, "6i", cx + 20, cy - 6 * u, PURPLE, size=34, a=acc, anchor="left", bounds=(0, 1920))
    if ad > 0:
        g = clamp((t - C["12.d"]) / 2.2)
        ang = 30 + 60 * g
        L = (2 + 4 * g) * u
        seta(c, cx, cy, ang, L, PURPLE, ad)
        arco(c, cx, cy, 70, 30, ang, AMBER, ad, 6)
        if g >= 1:
            pill(c, "6i", cx + 20, cy - 6 * u, PURPLE, size=34, a=ad, anchor="left", bounds=(0, 1920))
        selo(c, 1240, 680, ad, "ESTICOU E GIROU", AMBER, -4, 32)
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        pill(c, "dividir:  ÷ os módulos  ·  − os ângulos", 1240, 775, BLUE, size=28, a=ae, anchor="center")


def b_vezes_i(c, t, C, B):
    head(c, t, B["start"], "A MANIVELA DO EPISÓDIO 3", "VEZES i GIRA 90°", PURPLE)
    card(c, *CARD_R)
    cx, cy, u = 520, 560, 120
    a0 = ep(t, C["13"], 0.5)
    plano(c, cx, cy, 290, u, a0)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        seta(c, cx, cy, 90, u, BLUE, aa * (1 - ep(t, C["13.c"], 0.4) * 0.7))
        cartao(c, 960, 230, 700, 110, aa)
        linha(c, [("i:  ", BLUE), ("módulo 1", INK), ("  ·  ", INK2), ("ângulo 90°", INK)], 1310, 285, 40, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        regra(c, "× 1 no módulo  ·  + 90° no ângulo", 1310, 420, ab, 32)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        seta(c, cx, cy, 30, 2 * u, LIGHT if t > C["13.c"] + 1.5 else BLUE, acc)
        g = clamp((t - C["13.c"] - 1.5) / 1.8)
        ang = 30 + 90 * g
        if g > 0:
            seta(c, cx, cy, ang, 2 * u, PURPLE, acc)
            arco(c, cx, cy, 90, 30, ang, AMBER, acc, 6)
        cartao(c, 960, 500, 700, 150, acc)
        expr(c, "√{3} + i", 1130, 575, 44, acc, cores={0: BLUE})
        text_mid(c, "→", 1290, 575, 44, "black", INK2, acc)
        expr(c, "−1 + √{3}i", 1470, 575, 44, acc * ep(t, C["13.c"] + 2.5, 0.4), cores={0: PURPLE})
        text(c, "30°", 1130, 640, 26, "black", INK2, acc)
        text(c, "120°", 1470, 640, 26, "black", INK2, acc * ep(t, C["13.c"] + 2.5, 0.4))
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        selo(c, 1310, 740, ad, "GIRA 90°, SEM ESTICAR", GREEN, -4, 32)


# ======================================================================
# bloco e — De Moivre
# ======================================================================

def b_moivre(c, t, C, B):
    head(c, t, B["start"], "FÓRMULA DE DE MOIVRE", "POTÊNCIAS ALTAS", PURPLE)
    card(c, *CARD_R)
    cx, cy = 500, 540
    a0 = ep(t, C["14"], 0.5)
    plano(c, cx, cy, 290, 1, a0, rotulos=False)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        pill(c, "elevar a n = multiplicar n vezes", 1260, 230, BLUE, size=28, a=aa, anchor="center")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        K.boxed(c, 860, 280, 800, 140, PURPLE, ab, 0.10)
        expr(c, "z^n = ρ^n [cos(nθ) + i·sen(nθ)]", 1260, 350, 46, ab, cores={0: PURPLE, 2: PURPLE})
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        esc = lambda r: 30 * r ** 0.5
        k, ang, rho = potencia_anim(c, cx, cy, t, C["14.c"] + 0.3, 3.2, 30, 6, 2, acc, PURPLE, esc)
        cartao(c, 860, 450, 800, 150, acc)
        expr(c, "(√{3}+i)^6", 1060, 525, 44, acc)
        expr(c, "2^6 = 64", 1300, 495, 38, acc, cores={2: GREEN})
        expr(c, "6 · 30° = 180°", 1300, 560, 38, acc, cores={4: AMBER})
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        pill(c, "−64", cx - 240 - 20, cy - 50, GREEN, size=34, a=ad, anchor="right", bounds=(0, 1920))
        rrect(c, 860, 630, 800, 130, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        linha(c, [("cos 180° = −1,  sen 180° = 0   →   ", INK), ("−64", GREEN)], 1260, 695, 38, ad)


def b_atalho_voltas(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TIRE AS VOLTAS INTEIRAS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · PASSOU DE 360°? TIRE AS VOLTAS", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["15.a"], 0.5)
    cx, cy = 560, 540
    if aa > 0:
        c.drawCircle(cx, cy, 170, paint(LIGHT, aa, stroke=4))
        text_mid(c, "1 volta = 360°", 1180, 400, 46, "black", INK, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        g = clamp((t - C["15.b"]) / 2.4)
        ang = 405 * g
        arco(c, cx, cy, 170, 0, min(ang, 360), AMBER, ab, 8)
        if ang > 360:
            arco(c, cx, cy, 130, 0, ang - 360, PURPLE, ab, 8)
        seta(c, cx, cy, ang, 210, PURPLE, ab)
        linha(c, [("405° − 360° = ", INK), ("45°", PURPLE)], 1180, 560, 56, ab * ep(t, C["15.b"] + 2.4, 0.4))


# ======================================================================
# bloco f — raízes
# ======================================================================

def b_raizes(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO DE VOLTA", "AS RAÍZES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    defin(c, "RAÍZES n-ÉSIMAS", "elevadas a n, voltam ao número de partida", 260, 196, 1400, aa, BLUE, 30)
    cx, cy, u = 560, 560, 200
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        for k, s_ in enumerate(("MESMO MÓDULO", "IGUALMENTE ESPAÇADAS", "POLÍGONO REGULAR")):
            ak, d = rise(t, C["16.b"] + k * 1.2)
            rrect(c, 960, 330 + k * 120 + d, 700, 92, 18, "#FFFFFF", ak, shadow=True)
            badge_num(c, k + 1, 1010, 376 + k * 120 + d, ak, 26, bg=PURPLE)
            text(c, s_, 1060, 390 + k * 120 + d, 36, "black", PURPLE, ak, align="left")
    acc = ep(t, C["16.c"], 0.5)
    plano(c, cx, cy, 260, u, max(ab, acc) * 0.8, rotulos=False)
    if acc > 0:
        c.drawCircle(cx, cy, u, paint(LIGHT, acc, stroke=3))
        pts = [(1, 0, "1"), (0, 1, "i"), (-1, 0, "−1"), (0, -1, "−i")]
        p = skia.Path()
        for j, (x, y, _) in enumerate(pts):
            (p.moveTo if j == 0 else p.lineTo)(cx + x * u, cy - y * u)
        p.close()
        c.drawPath(p, paint(PURPLE, acc * 0.12))
        c.drawPath(p, paint(PURPLE, acc, stroke=5))
        for j, (x, y, s_) in enumerate(pts):
            aj = ep(t, C["16.c"] + j * 0.5, 0.4)
            c.drawCircle(cx + x * u, cy - y * u, 14, paint(GREEN, aj))
            pill(c, s_, cx + x * u * 1.28, cy - y * u * 1.28, GREEN, size=30, a=aj, anchor="center", bounds=(0, 1920))
        pill(c, "o relógio do episódio 1", 1310, 740, PURPLE, size=28, a=ep(t, C["16.c"] + 2.5, 0.4), anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "1 − i NO RADAR", GREEN)])
    card(c, *CARD_R)
    cx, cy, u = 470, 470, 170
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        expr(c, "z = 1 − i", 1240, 250, 60, aa, cores={2: PURPLE})
        text(c, "na forma trigonométrica", 1240, 320, 30, "black", INK2, aa)
    sol = t >= C["18"]
    ab = ep(t, C["17.b"], 0.5)
    rows = [("18.a", "quadrante", "4º  (a > 0, b < 0)"), ("18.b", "módulo", "ρ = √{1+1} = √{2}"),
            ("18.c", "ângulo", "θ = 360° − 45° = 315°")]
    for k, (cue, rot, s_) in enumerate(rows):
        y = 420 + k * 110
        if ab > 0:
            cartao(c, 860, y - 45, 800, 90, ab)
            text(c, rot, 900, y + 12, 28, "black", INK2, ab, align="left")
        ak = ep(t, C[cue], 0.5) if sol else 0
        if ak > 0:
            if k == 0:
                text(c, s_, 1100, y + 14, 38, "black", BLUE, ak, align="left")
            else:
                expr(c, s_, 1100, y, 38, ak, align="left", cores={4 if k == 1 else 6: GREEN})
        elif ab > 0:
            text(c, "= ?", 1100, y + 14, 38, "black", GRAY, ab, align="left")
    if not sol:
        pause_timer(c, t, C["17.end"] - 1.9, 470, 470)
        return
    X, Y = plano(c, cx, cy, 260, u, 1, ticks=((1, "1", "x"), (-1, "−1", "y")))
    a1 = ep(t, C["18.a"], 0.5)
    quadrantes(c, X, Y, cx, cy, 260, a1, 4)
    if a1 > 0:
        c.drawCircle(X(1), Y(-1), 12, paint(PURPLE, a1))
    a2 = ep(t, C["18.b"], 0.5)
    if a2 > 0:
        seta(c, cx, cy, -45, math.sqrt(2) * u, PURPLE, a2)
    a3 = ep(t, C["18.c"], 0.5)
    if a3 > 0:
        arco(c, cx, cy, 70, 315, 360, AMBER, a3, 6)
        g = clamp((t - C["18.c"] - 1.2) / 2.0)
        arco(c, cx, cy, 110, 0, 315 * g, GREEN, a3, 6)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        rrect(c, 860, 700, 800, 100, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        tri(c, "√{2}", "315°", 1260, 750, 44, ad, GREEN)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Módulo e argumento: distância e direção.",
          "Multiplicar: multiplica os módulos e soma os ângulos.",
          "Potência: módulo elevado a n, ângulo vezes n."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "27"])
    frame(c, t, B["start"] if sid == "19" else C["27"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("o argumento de −1 + i é 45°",
          "a conta com os números sem sinal dá mesmo 45°",
          "45° é o endereço de 1 + i (1º quadrante); −1 + i está no 2º: θ = 135°.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20"], ERROS)


# ======================================================================
# questão 6 (eu faço)
# ======================================================================

ALTS6 = [("A", "4(cos 60° + i sen 60°)", "", RED), ("B", "2(cos 60° + i sen 60°)", "", GREEN),
         ("C", "2(cos 30° + i sen 30°)", "", RED), ("D", "2(cos 120° + i sen 120°)", "", RED),
         ("E", "2(cos 300° + i sen 300°)", "", RED)]
MOTIVOS6 = [("A", "esqueceu a raiz no módulo (parou no 4)"), ("C", "trocou seno e cosseno (30°)"),
            ("D", "2º quadrante, mas a e b são positivos"), ("E", "é o conjugado 1 − √3 i (4º quadrante)")]


def b_q6(c, t, C, B):
    sid = which(t, C, ["21", "22", "23"])
    heads = {"21": "1 + √3 i NA FORMA TRIGONOMÉTRICA", "22": "EU FAÇO", "23": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "21" else C[sid], "QUESTÃO 6 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS6, 1080, 250, 600, 32, C["22.ok"], "B", cues_in, cues_x, gap=22)
    a0 = ep(t, C["21.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        expr(c, "z = 1 + √{3}i", 620, 250, 56, a0, cores={2: PURPLE})
    cx, cy, u = 330, 620, 100
    if sid == "21":
        return
    if sid == "23":
        for k, (L, s_) in enumerate(MOTIVOS6):
            ak, d = rise(t, C[f"23.x{L.lower()}"])
            if ak <= 0:
                continue
            y = 360 + k * 110 + d
            rrect(c, 190, y - 42, 840, 84, 18, mix("#FFFFFF", RED, 0.08), ak)
            badge_num(c, L, 240, y, ak, 22, bg=RED)
            text(c, s_, 285, y + 12, 30, "black", RED, ak, align="left")
        return
    X, Y = plano(c, cx, cy, 190, u, 1, rotulos=False, ticks=((1, "1", "x"), (S3, "√3", "y")))
    if sid == "22":
        aa = ep(t, C["22.a"], 0.5)
        if aa > 0:
            line(c, X(1), Y(S3), X(1), cy, LIGHT, aa, 3)
            c.drawCircle(X(1), Y(S3), 12, paint(PURPLE, aa))
            pill(c, "1º quadrante", X(1) + 24, Y(S3) + 30, BLUE, size=24, a=aa, anchor="left", bounds=(0, 1920))
        ab = ep(t, C["22.b"], 0.5)
        if ab > 0:
            seta(c, cx, cy, 60, 2 * u, PURPLE, ab)
            expr(c, "ρ = √{1+3} = 2", 820, 350, 40, ab, cores={4: GREEN})
        acc = ep(t, C["22.c"], 0.5)
        if acc > 0:
            expr(c, "cos θ = 1/2", 820, 450, 38, acc)
            expr(c, "sen θ = √{3}/2", 820, 550, 38, acc)
            arco(c, cx, cy, 70, 0, 60, AMBER, acc, 6)
            text(c, "60°", cx + 95, cy - 30, 28, "black", AMBER, acc)
        ad = ep(t, C["22.d"], 0.5)
        if ad > 0:
            pill(c, "2 · ½ = 1   ·   2 · √3/2 = √3", 820, 650, GREEN, size=24, a=ad, anchor="center", bounds=(0, 1920))
        return


# ======================================================================
# questão 7 (você faz)
# ======================================================================

ALTS7 = [("A", "−16", "usou i⁴ = −1", RED), ("B", "8i", "multiplicou 2i por 4", RED), ("C", "16", "", GREEN),
         ("D", "16i", "usou i⁴ = i", RED), ("E", "256", "módulo 2, não √2", RED)]


def b_q7(c, t, C, B):
    sid = which(t, C, ["24", "25", "26"])
    heads = {"24": "VOCÊ FAZ", "25": "DOIS CAMINHOS", "26": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "24" else C[sid], "QUESTÃO 7 · ESTILO ENEM", heads[sid], GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS7, 1300, 260, 380, 36, C["25.ok"], "C", cues_in, cues_x, gap=26)
    a0 = ep(t, C["24.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if sid == "24":
        if a0 > 0:
            expr(c, "(1+i)^8 = ?", 700, 400, 90, a0, cores={0: PURPLE})
            text(c, "i = unidade imaginária", 700, 520, 32, "black", INK2, a0)
        pause_timer(c, t, C["24.end"] - 1.9, 700, 660)
        return
    cx, cy = 430, 520
    plano(c, cx, cy, 250, 1, 1, rotulos=False)
    if sid == "25":
        aa = ep(t, C["25.a"], 0.5)
        if aa > 0:
            potencia_anim(c, cx, cy, t, C["25.a"] + 1.0, 4.5, 45, 8, math.sqrt(2), aa, PURPLE, lambda r: 55 * r ** 0.6)
            cartao(c, 740, 230, 520, 200, aa)
            text(c, "DE MOIVRE", 1000, 270, 24, "black", PURPLE, aa, tracking=2)
            expr(c, "(√{2})^8 = 16", 1000, 330, 38, aa, cores={2: GREEN})
            expr(c, "8 · 45° = 360°", 1000, 395, 38, aa)
        ab = ep(t, C["25.b"], 0.5)
        if ab > 0:
            cartao(c, 740, 460, 520, 300, ab)
            text(c, "ALGÉBRICO", 1000, 500, 24, "black", BLUE, ab, tracking=2)
            expr(c, "(1+i)^2 = 2i", 1000, 565, 38, ab)
        acc = ep(t, C["25.c"], 0.5)
        if acc > 0:
            expr(c, "(2i)^4 = 16·i^4", 1000, 640, 38, acc)
            expr(c, "= 16·1 = 16", 1000, 715, 38, acc, cores={4: GREEN})
        return
    seta(c, cx, cy, 0, 55 * 16 ** 0.6, PURPLE, 1)
    pill(c, "16", cx + 55 * 16 ** 0.6 + 16, cy - 40, GREEN, size=30, a=1, anchor="left", bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DE NÚMEROS COMPLEXOS", PURPLE)
    for k, (cue, s_, col) in enumerate((("28.a", "JUNTAMOS TUDO", PURPLE), ("28.b", "CAÇAMOS AS PEGADINHAS", AMBER),
                                        ("28.c", "QUESTÕES INÉDITAS", GREEN))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 330 + k * 150 + d
        rrect(c, 460, y - 55, 1000, 110, 24, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, 530, y, ak, 30, bg=col)
        text(c, s_, 600, y + 16, 46, "black", col, ak, align="left")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Já tinha pensado num complexo como uma seta que gira?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, tabela=b_tabela, concreto=b_concreto,
              definicao=b_definicao, exemplo=b_exemplo, tabela07=b_tabela07, atalho_tabela=b_atalho_tabela,
              quadrante=b_quadrante, atalho_quadrante=b_atalho_quadrante, produto=b_produto, vezes_i=b_vezes_i,
              moivre=b_moivre, atalho_voltas=b_atalho_voltas, raizes=b_raizes, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q6=b_q6, q7=b_q7, ponte=b_ponte, cta=b_cta)
