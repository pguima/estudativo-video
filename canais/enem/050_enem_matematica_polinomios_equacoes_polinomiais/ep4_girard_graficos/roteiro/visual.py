"""Visual — Polinômios e Equações Polinomiais, Episódio 4: Girard e gráficos (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: bloco_iso() (a caixa de sapato / o bloco retangular em perspectiva, com as arestas nas pílulas),
grafico() (eixos + curva desenhada até `prog`, devolve as funções de posição), bola() (a bola que quica ou atravessa),
girard_card() (as três relações com os sinais − + − destacados), meias() (o par de meias das raízes conjugadas).
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
_s = importlib.util.spec_from_file_location("comum050", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w, expr, math_w = K.ftext, K.ftext_w, K.expr, K.math_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_polinomios_ep4_girard_graficos.mp4"
CARD_R = K.CARD_R
CAIXA = "#E9D2B4"
CAIXA_D = "#C9A57A"
CAIXA_E = "#DDBE96"


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


def poly(c, pts, col, a, stroke=None):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, paint(col, a))
    if stroke:
        c.drawPath(p, paint(stroke[0], a, stroke=stroke[1]))


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


def bloco_iso(c, cx, cy, L, P, H, a, rots=None, alfa_rot=1.0, cor=None):
    """bloco retangular fechado em perspectiva: L = comprimento (frente), P = profundidade, H = altura.
    rots = (rótulo do comprimento, da profundidade, da altura)"""
    if a <= 0:
        return
    f1, f2, f3 = (cor or CAIXA), mix(cor or CAIXA, "#000000", 0.10), mix(cor or CAIXA, "#FFFFFF", 0.25)
    dx, dy = P * 0.62, -P * 0.42
    x0, y0 = cx - (L + dx) / 2, cy + (H - dy) / 2
    A = (x0, y0); B = (x0 + L, y0); Cc = (x0 + L + dx, y0 + dy); D = (x0 + dx, y0 + dy)
    At, Bt, Ct, Dt = [(px, py - H) for px, py in (A, B, Cc, D)]
    poly(c, [B, Cc, Ct, Bt], f2, a, (CAIXA_D, 3))       # lado direito
    poly(c, [A, B, Bt, At], f1, a, (CAIXA_D, 3))        # frente
    poly(c, [At, Bt, Ct, Dt], f3, a, (CAIXA_D, 3))      # tampa
    if rots and alfa_rot > 0:
        r1, r2, r3 = rots
        ar = a * alfa_rot
        pill(c, r1, (A[0] + B[0]) / 2, A[1] + 44, PURPLE, size=28, a=ar, anchor="center", bounds=(0, 1920))
        pill(c, r2, (B[0] + Cc[0]) / 2 + 30, (B[1] + Cc[1]) / 2 + 26, PURPLE, size=28, a=ar, anchor="left",
             bounds=(0, 1920))
        pill(c, r3, A[0] - 26, (A[1] + At[1]) / 2, PURPLE, size=28, a=ar, anchor="right", bounds=(0, 1920))


def grafico(c, f, xr, yr, box, a, prog=1.0, col=None, ticks=(), lw=6, n=240, rot_x="x", rot_y="y"):
    """eixos + a curva y = f(x) desenhada da esquerda até a fração `prog`. Devolve (X, Y) para posicionar peças."""
    x, y, w, h = box
    X = lambda v: x + (v - xr[0]) / (xr[1] - xr[0]) * w
    Y = lambda v: y + h - (v - yr[0]) / (yr[1] - yr[0]) * h
    if a <= 0:
        return X, Y
    ya, xa = Y(0), X(0)
    arrow(c, x - 10, ya, x + w + 20, ya, INK2, a, 4, 14)
    arrow(c, xa, y + h + 10, xa, y - 20, INK2, a, 4, 14)
    text(c, rot_x, x + w + 30, ya + 40, 28, "black", INK2, a)
    text(c, rot_y, xa - 30, y - 10, 28, "black", INK2, a)
    for v, s_ in ticks:
        line(c, X(v), ya - 8, X(v), ya + 8, INK2, a, 3)
        text(c, s_, X(v), ya + 44, 28, "black", INK2, a)
    if prog > 0:
        p = skia.Path()
        k_max = max(2, int(n * clamp(prog)))
        first = True
        for k in range(k_max + 1):
            v = xr[0] + (xr[1] - xr[0]) * k / n
            yy = min(max(Y(f(v)), y - 30), y + h + 30)
            if first:
                p.moveTo(X(v), yy); first = False
            else:
                p.lineTo(X(v), yy)
        c.save()
        c.clipRect(skia.Rect.MakeXYWH(x - 20, y - 30, w + 40, h + 60))
        c.drawPath(p, paint(col or PURPLE, a, stroke=lw))
        c.restore()
    return X, Y


def bola(c, x, y, a, col=None, r=20):
    if a <= 0:
        return
    c.drawCircle(x, y, r, paint(col or AMBER, a))
    c.drawCircle(x, y, r, paint(mix(col or AMBER, "#000000", 0.25), a, stroke=3))
    c.drawCircle(x - r * 0.35, y - r * 0.35, r * 0.28, paint("#FFFFFF", a * 0.7))


def girard_card(c, x, y, w, a, linhas_on=(True, True, True), size=50, acesos=()):
    """as três relações de Girard; acesos = índices destacados"""
    if a <= 0:
        return
    rrect(c, x, y, w, 330, 24, "#FFFFFF", a, shadow=True)
    itens = [("soma", "r_1 + r_2 + r_3", "− b/a", RED), ("pares", "r_1r_2 + r_1r_3 + r_2r_3", "+ c/a", GREEN),
             ("produto", "r_1r_2r_3", "− d/a", RED)]
    for k, (rot, lado, fr_, col) in enumerate(itens):
        if not linhas_on[k]:
            continue
        yy = y + 60 + k * 105
        if k in acesos:
            rrect(c, x + 14, yy - 46, w - 28, 92, 16, mix("#FFFFFF", PURPLE, 0.16), a)
        text(c, rot, x + 30, yy + 12, 28, "black", INK2, a, align="left")
        expr(c, lado.replace("r_1", "r₁").replace("r_2", "r₂").replace("r_3", "r₃") + " =", x + 180, yy, size * 0.72,
             a, align="left")
        expr(c, fr_, x + w - 40, yy, size, a, align="right", cores={0: col})


def meias(c, cx, cy, a, z1, z2, a2=1.0, col=None):
    """o par de meias: duas meias com as raízes conjugadas; a segunda entra com a2"""
    col = col or BLUE
    for k, (s_, ak) in enumerate(((z1, a), (z2, a * a2))):
        if ak <= 0:
            continue
        x = cx - 150 + k * 300
        p = skia.Path()
        p.moveTo(x - 50, cy - 130); p.lineTo(x + 30, cy - 130); p.lineTo(x + 30, cy + 20)
        p.quadTo(x + 30, cy + 70, x + 90, cy + 80); p.quadTo(x + 120, cy + 90, x + 110, cy + 120)
        p.lineTo(x - 30, cy + 120); p.quadTo(x - 60, cy + 120, x - 50, cy + 60); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", col, 0.35 if k == 0 else 0.22), ak))
        c.drawPath(p, paint(col, ak, stroke=4))
        rrect(c, x - 52, cy - 140, 84, 26, 8, col, ak)
        expr(c, s_, x + 20, cy - 190, 44, ak, cores={0: col})


def f_ex(v):          # (x + 1)²(x − 3) — bloco c e erro 2
    return (v + 1) ** 2 * (v - 3)


def f_q5(v):          # (x + 1)(x − 2)² — Questão 5
    return (v + 1) * (v - 2) ** 2


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "POLINÔMIOS · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        expr(c, "2x^3 − 14x^2 + 28x − 16 = 0", 960, 290, 70, aa, cores={0: PURPLE})
        pill(c, "as RAÍZES são as arestas", 960, 390, BLUE, size=30, a=aa, anchor="center")
    g = ep(t, C["01.a"] + 1.5, 1.2)
    bloco_iso(c, 620, 610, 300, 200, 150, g, ("?", "?", "?"), g)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        cartao(c, 1040, 500, 560, 170, ab, GREEN, True)
        text_mid(c, "volume = 8 m³", 1320, 585, 60, "black", GREEN, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, 1320, 760, acc, "SEM ACHAR NENHUMA ARESTA", AMBER, -4, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "POLINÔMIOS · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de POLINÔMIOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    itens = [("02.a", "GIRARD", "soma e produto direto", PURPLE), ("02.b", "O GRÁFICO", "a lei pelas raízes", BLUE),
             ("02.c", "O PAR", "as raízes não reais", GREEN)]
    for k, (cue, tit, sb, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 220, 340, 440, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 220, 340, 440, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 42, "black", col, ak)
        text(c, sb, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "QUATRO LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    rows = [("03.a", "2º grau", "soma = − b/a      produto = c/a", BLUE, True),
            ("03.b", "episódio 3", "(x − 2)²  →  raiz 2 de multiplicidade 2", PURPLE, False),
            ("03.c", "Função quadrática", "raiz = onde a curva encontra o eixo x", GREEN, False),
            ("03.d", "Números complexos", "i² = −1   (série própria: a próxima)", AMBER, False)]
    for k, (cue, rot, s_, col, ex) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 140 + d
        cartao(c, 260, y - 58, 1400, 116, a)
        pill(c, rot, 300, y - 58, col, size=22, a=a)
        if ex:
            expr(c, "soma = − b/a", 760, y + 6, 40, a)
            expr(c, "produto = c/a", 1200, y + 6, 40, a)
        else:
            text_mid(c, s_, 960, y + 6, 38, "black", INK, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA CAIXA E DUAS BOLAS", "O CONCRETO ANTES DA CONTA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    aa = ep(t, C["04.a"], 0.5)
    bloco_iso(c, 520, 520, 360, 220, 160, a0, ("a", "b", "c"), aa)
    if aa > 0:
        text_mid(c, "V = a · b · c", 520, 760, 46, "black", PURPLE, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        line(c, 980, 600, 1260, 600, INK, ab, 6)
        u = clamp((t - C["04.b"] - 0.6) / 2.0)
        yb = 600 - 22 - 220 * abs(1 - 2 * u) if u < 1 else 600 - 22 - 120
        bola(c, 1120, yb, ab)
        text(c, "o chão: QUICA", 1120, 680, 30, "black", INK, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 1340, 594, 300, 12, 4, mix("#FFFFFF", BLUE, 0.45), acc)
        u = clamp((t - C["04.c"] - 0.4) / 1.8)
        bola(c, 1490, 380 + 300 * u, acc * (1 - clamp((u - 0.75) / 0.25)))
        text(c, "o vidro: ATRAVESSA", 1490, 680, 30, "black", INK, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pill(c, "caixa → EQUAÇÃO   ·   bolas → GRÁFICO", 1310, 780, PURPLE, size=30, a=ad, anchor="center")


# ======================================================================
# bloco a — Girard
# ======================================================================

def b_girard(c, t, C, B):
    head(c, t, B["start"], "RELAÇÕES DE GIRARD", "AS RAÍZES ESTÃO NOS COEFICIENTES", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    defin(c, "GIRARD", "contas que ligam os coeficientes às raízes", 260, 196, 1400, aa, BLUE, 32)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        expr(c, "ax^3 + bx^2 + cx + d = 0", 960, 340, 62, ab, cores={0: PURPLE})
    on = (t >= C["05.c"], t >= C["05.d"], t >= C["05.e"])
    girard_card(c, 410, 410, 1100, ep(t, C["05.c"], 0.5), on, 56)
    af = ep(t, C["05.f"], 0.5)
    if af > 0:
        linha(c, [("menos", RED), ("  ·  ", INK2), ("mais", GREEN), ("  ·  ", INK2), ("menos", RED)], 960, 790, 46, af)


def b_girard_teste(c, t, C, B):
    head(c, t, B["start"], "SERÁ QUE FUNCIONA?", "CONFERÊNCIA COM RAÍZES CONHECIDAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        expr(c, "x^3 − 2x^2 − 5x + 6 = 0", 960, 250, 60, aa)
        pill(c, "raízes: −2, 1 e 3", 960, 330, BLUE, size=30, a=aa, anchor="center")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        for k, (L, v) in enumerate((("a", "1"), ("b", "−2"), ("c", "−5"), ("d", "6"))):
            x = 560 + k * 270
            rrect(c, x - 110, 380, 220, 90, 18, mix("#FFFFFF", PURPLE, 0.12), ab)
            linha(c, [(L + " = ", INK2), (v, PURPLE)], x, 425, 40, ab)
    rows = [("06.c", "soma", "−2 + 1 + 3 = 2", "− b/a = 2"),
            ("06.d", "pares", "−2 − 6 + 3 = −5", "c/a = −5"),
            ("06.e", "produto", "(−2)·1·3 = −6", "− d/a = −6")]
    for k, (cue, rot, l1, l2) in enumerate(rows):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 540 + k * 100 + d
        cartao(c, 300, y - 42, 1320, 84, ak)
        text(c, rot, 340, y + 12, 30, "black", INK2, ak, align="left")
        expr(c, l1, 820, y, 40, ak)
        expr(c, l2, 1340, y, 40, ak, cores={0: PURPLE})
        check_icon(c, 1560, y, 22, ak, GREEN)


def b_atalho_sinais(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "OS SINAIS PRIMEIRO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · ESCREVA a, b, c, d COM OS SINAIS", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        expr(c, "2x^3 − 14x^2 + 28x − 16", 960, 360, 60, aa)
        linha(c, [("a = 2   ", PURPLE), ("b = −14   ", PURPLE), ("c = 28   ", PURPLE), ("d = −16", PURPLE)], 960, 470,
              44, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("só depois:  ", INK), ("menos", RED), (" · ", INK2), ("mais", GREEN), (" · ", INK2), ("menos", RED)],
              960, 600, 46, ab)
        pill(c, "sinal do coeficiente ≠ sinal da fórmula", 960, 710, AMBER, size=30, a=ab, anchor="center")


# ======================================================================
# bloco b — a caixa de sapato
# ======================================================================

def b_caixa(c, t, C, B):
    head(c, t, B["start"], "A LEITURA GEOMÉTRICA", "ARESTAS = RAÍZES", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.5)
    ad = ep(t, C["08.d"], 0.5)
    bloco_iso(c, 520, 520, 380, 230, 170, a0, ("2", "3", "5") if ad > 0 else ("a", "b", "c"), a0)
    rows = [("08.a", "produto", "volume", "30"), ("08.b", "pares", "metade da área total", "31"),
            ("08.c", "soma", "¼ de todas as arestas", "10")]
    for k, (cue, rot, s_, num) in enumerate(rows):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 300 + k * 160 + d
        cartao(c, 900, y - 60, 760, 120, ak)
        text(c, rot, 940, y + 12, 32, "black", PURPLE, ak, align="left")
        text(c, "= " + s_, 1110, y + 12, 32, "bold", INK, ak, align="left")
        if ad > 0:
            pill(c, num, 1620, y, GREEN, size=34, a=ad, anchor="right", bounds=(0, 1920))


# ======================================================================
# bloco c — o gráfico conta as raízes
# ======================================================================

GBOX = (240, 300, 860, 500)


def b_grafico(c, t, C, B):
    head(c, t, B["start"], "O GRÁFICO CONTA AS RAÍZES", "TOCA OU ATRAVESSA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    defin(c, "RAÍZES REAIS", "os pontos onde a curva encontra o eixo horizontal", 260, 196, 1400, aa, BLUE, 30)
    ab = ep(t, C["09.b"], 0.5)
    prog = clamp((t - C["09.b"] - 0.4) / 2.6)
    X, Y = grafico(c, f_ex, (-2.2, 3.6), (-11, 11), GBOX, ab, prog, PURPLE, ((-1, "−1"), (3, "3")))
    if ab > 0:
        expr(c, "P(x) = (x+1)^2 (x−3)", 1400, 390, 46, ab, cores={2: PURPLE})
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        u = clamp((t - C["09.c"]) / 2.2)
        v = -1.9 + 1.6 * u
        bola(c, X(v), Y(f_ex(v)) - 22, acc * (1 - ep(t, C["09.d"], 0.3)))
        pill(c, "par: TOCA", X(-1), Y(0) - 70, GREEN, size=28, a=acc, anchor="center", bounds=(0, 1920))
        cartao(c, 1140, 460, 520, 100, acc)
        expr(c, "(x+1)^2 → toca e volta", 1400, 510, 34, acc, cores={0: GREEN})
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        u = clamp((t - C["09.d"]) / 2.0)
        v = 2.2 + 1.1 * u
        bola(c, X(v), Y(f_ex(v)) - 22, ad)
        pill(c, "ímpar: ATRAVESSA", X(3) - 30, Y(0) - 120, RED, size=28, a=ad, anchor="right", bounds=(0, 1920))
        cartao(c, 1140, 590, 520, 100, ad)
        expr(c, "(x−3) → atravessa", 1400, 640, 34, ad, cores={0: RED})
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        c.drawCircle(X(0), Y(-3), 14, paint(AMBER, ae))
        pill(c, "(0, −3)", X(0) + 30, Y(-3) + 4, AMBER, size=28, a=ae, anchor="left", bounds=(0, 1920))
        expr(c, "P(0) = 1·(−3) = −3", 1400, 755, 38, ae, cores={0: AMBER})


def b_multiplicidade(c, t, C, B):
    head(c, t, B["start"], "POR QUE QUICA?", "PAR NÃO TROCA DE SINAL", PURPLE)
    card(c, *CARD_R)
    for k, (cue, tit, f_, s1, s2, col) in enumerate((
            ("10.a", "MULTIPLICIDADE PAR", "(x+1)^2", "nunca é negativo", "TOCA E VOLTA", GREEN),
            ("10.b", "MULTIPLICIDADE ÍMPAR", "(x−3)", "troca de sinal", "ATRAVESSA", RED))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 300 + k * 700
        cartao(c, x, 220 + d, 620, 560, ak)
        text(c, tit, x + 310, 290 + d, 34, "black", col, ak)
        expr(c, f_, x + 310, 400 + d, 80, ak, cores={0: col})
        text(c, s1, x + 310, 510 + d, 34, "bold", INK2, ak)
        # mini-gráfico
        gx, gy = x + 140, 560 + d
        line(c, gx, gy + 90, gx + 340, gy + 90, INK2, ak, 3)
        p = skia.Path()
        for j in range(61):
            u = j / 60
            yy = gy + 90 - 140 * (u - 0.5) if k == 1 else gy + 90 - 120 * ((u - 0.5) * 2) ** 2
            xx = gx + 340 * u
            (p.moveTo if j == 0 else p.lineTo)(xx, yy)
        c.save(); c.clipRect(skia.Rect.MakeXYWH(gx - 10, gy - 10, 360, 200))
        c.drawPath(p, paint(col, ak, stroke=6)); c.restore()
        pill(c, s2, x + 310, 770 + d, col, size=28, a=ak, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco d — fatos que eliminam alternativas
# ======================================================================

def b_fatos(c, t, C, B):
    head(c, t, B["start"], "FATOS QUE ELIMINAM", "O GRÁFICO NA PROVA", PURPLE)
    card(c, *CARD_R)
    itens = [("11.a", "grau n", "no máximo n encontros com o eixo", PURPLE),
             ("11.b", "grau ímpar, coeficientes reais", "pelo menos UMA raiz real", PURPLE),
             ("11.c", "grau ímpar, dominante positivo", "começa EMBAIXO e termina EM CIMA", PURPLE)]
    for k, (cue, q, r, col) in enumerate(itens):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 260, y - 65, 1400, 140, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, 260, y - 65, 14, 140, 7, col, ak)
        text(c, q, 310, y - 8, 30, "black", INK2, ak, align="left")
        text(c, "→ " + r, 310, y + 42, 38, "black", col, ak, align="left")
        if k == 2:
            p = skia.Path()
            for j in range(41):
                u = j / 40
                xx = 1380 + 220 * u
                yy = y + 55 - 110 * u
                (p.moveTo if j == 0 else p.lineTo)(xx, yy)
            c.drawPath(p, paint(GREEN, ak, stroke=6))
            arrow(c, 1580, y - 45, 1606, y - 58, GREEN, ak, 6, 14)


def b_atalho_grafico(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TRÊS LEITURAS DO GRÁFICO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · LENDO O GRÁFICO", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, s_) in enumerate((("12.a", "conte os ENCONTROS com o eixo"), ("12.b", "TOCA (par) ou ATRAVESSA (ímpar)?"),
                                   ("12.c", "leia P(0) no eixo vertical"))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 360 + k * 140 + d
        rrect(c, 340, y - 55, 1240, 110, 22, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, 410, y, ak, 30, bg=GREEN)
        text(c, s_, 470, y + 14, 42, "black", INK, ak, align="left")


# ======================================================================
# bloco e — raízes conjugadas
# ======================================================================

def b_conjugadas(c, t, C, B):
    head(c, t, B["start"], "RAÍZES NÃO REAIS", "O PAR DE MEIAS", BLUE)
    card(c, *CARD_R)
    for k, (cue, termo, s_) in enumerate((("13.a", "UNIDADE IMAGINÁRIA", "o número i, com i² = −1"),
                                          ("13.b", "RAIZ NÃO REAL", "uma raiz que usa o i, como 1 − i"),
                                          ("13.c", "CONJUGADO", "o mesmo número com o sinal do i trocado"))):
        ak = ep(t, C[cue], 0.5)
        defin(c, termo, s_, 260, 200 + k * 96, 1400, ak, BLUE, 28)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        meias(c, 760, 690, ad, "1 − i", "1 + i", ep(t, C["13.d"] + 4.2, 0.6))
        cartao(c, 1120, 560, 540, 200, ad, PURPLE, True)
        text_mid(c, "coeficientes reais:", 1390, 620, 32, "bold", INK2, ad)
        text_mid(c, "as raízes andam EM DUPLA", 1390, 690, 36, "black", PURPLE, ad)


def b_conjugadas_conta(c, t, C, B):
    head(c, t, B["start"], "O PAR GERA O QUÊ?", "O i SOME", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    meias(c, 560, 560, aa, "2 + i", "2 − i")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        cartao(c, 960, 230, 700, 130, ab)
        expr(c, "soma: (2+i) + (2−i) = 4", 1310, 295, 40, ab, cores={6: GREEN})
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        cartao(c, 960, 390, 700, 190, acc)
        expr(c, "produto: 4 − i^2", 1310, 440, 40, acc)
        expr(c, "= 4 + 1 = 5", 1310, 520, 40, acc, cores={4: GREEN})
        pill(c, "i² = −1", 1620, 440, AMBER, size=24, a=acc, anchor="right", bounds=(0, 1920))
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 960, 620, 700, 150, 22, mix("#FFFFFF", PURPLE, 0.14), ad)
        expr(c, "x^2 − 4x + 5", 1310, 680, 56, ad, cores={0: PURPLE})
        text(c, "coeficientes REAIS", 1310, 750, 28, "black", GREEN, ad)


def b_atalho_par(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O FATOR DO PAR CONJUGADO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · SOMA E PRODUTO DO PAR", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        linha(c, [("x² − ", INK), ("(soma)", GREEN), ("·x + ", INK), ("(produto)", PURPLE)], 960, 420, 66, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        expr(c, "− i^2 = + 1", 960, 600, 70, ab, cores={0: AMBER, 2: GREEN})


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "AS TRÊS RELAÇÕES", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        expr(c, "x^3 − 6x^2 + 11x − 6 = 0", 960, 260, 62, aa)
        pill(c, "raízes: 1, 2 e 3", 960, 340, BLUE, size=30, a=aa, anchor="center")
    sol = t >= C["17"]
    a1 = ep(t, C["17.a"], 0.5) if sol else 0
    if a1 > 0:
        linha(c, [("a = 1    b = −6    c = 11    d = −6", PURPLE)], 960, 410, 40, a1)
    ab = ep(t, C["16.b"], 0.5)
    rows = [("17.b", "soma", "1 + 2 + 3 = 6", "− b/a = 6"), ("17.c", "pares", "2 + 3 + 6 = 11", "c/a = 11"),
            ("17.d", "produto", "1·2·3 = 6", "− d/a = 6")]
    for k, (cue, rot, l1, l2) in enumerate(rows):
        y = 500 + k * 100
        if ab > 0:
            cartao(c, 300, y - 42, 1320, 84, ab)
            text(c, rot, 340, y + 12, 30, "black", INK2, ab, align="left")
        ak = ep(t, C[cue], 0.5) if sol else 0
        if ak > 0:
            expr(c, l1, 820, y, 40, ak)
            expr(c, l2, 1340, y, 40, ak, cores={0: PURPLE})
            check_icon(c, 1560, y, 22, ak, GREEN)
        elif ab > 0:
            text(c, "= ?", 820, y + 14, 40, "black", GRAY, ab)
    if not sol:
        pause_timer(c, t, C["16.end"] - 1.9, 1700, 290)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Girard no 3º grau: menos, mais, menos, sempre dividindo por a.",
          "Multiplicidade par toca; ímpar atravessa.",
          "Raiz não real chega com o conjugado."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "31"])
    frame(c, t, B["start"] if sid == "18" else C["31"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("produto no 3º grau = d/a  (diz 6)",
          "no 2º grau o produto é c/a, sem o sinal de menos",
          "no 3º grau os sinais alternam: produto = −d/a = −6."),
         ("toda raiz atravessa o eixo  (cruza em −1)",
          "raiz parece sinônimo de \"cortar o eixo\"",
          "(x + 1)² não troca de sinal: em −1 a curva toca e volta."),
         ("grau 2, coeficientes reais, raízes 3 e 1 − i",
          "são só duas raízes para um grau dois",
          "1 − i traz 1 + i: seriam três raízes, grau pelo menos 3.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questão 4 (eu faço)
# ======================================================================

ALTS4 = [("A", "= 7 m^3", "é a soma, −b/a", RED), ("B", "= 8 m^3", "", GREEN), ("C", "= 14 m^3", "c/a: metade da área", RED),
         ("D", "= 16 m^3", "não dividiu por 2", RED), ("E", "= 28 m^3", "área total", RED)]


def b_q4(c, t, C, B):
    sid = which(t, C, ["22", "23", "24"])
    heads = {"22": "O BLOCO E A EQUAÇÃO", "23": "EU FAÇO", "24": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "22" else C[sid], "QUESTÃO 4 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS4, 1250, 250, 460, 34, C["23.ok"], "B", cues_in, cues_x, gap=30)
    a0 = ep(t, C["22.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        expr(c, "2x^3 − 14x^2 + 28x − 16 = 0", 680, 270, 46, a0)
        text(c, "arestas (em m) = raízes · volume = ?", 680, 340, 30, "black", INK2, a0)
    if sid == "22":
        bloco_iso(c, 680, 590, 320, 200, 150, ep(t, C["22.a"] + 1.0, 0.6), ("?", "?", "?"), 1.0)
        return
    if sid == "23":
        aa = ep(t, C["23.a"], 0.5)
        if aa > 0:
            pill(c, "volume = PRODUTO das raízes", 680, 410, BLUE, size=28, a=aa, anchor="center")
        ab = ep(t, C["23.b"], 0.5)
        if ab > 0:
            linha(c, [("a = 2   b = −14   c = 28   d = −16", PURPLE)], 680, 480, 34, ab)
        acc = ep(t, C["23.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 530, 840, 120, 22, mix("#FFFFFF", GREEN, 0.14), acc)
            expr(c, "− d/a = − (−16)/2 = 8", 680, 590, 46, acc, cores={0: RED, 1: RED, 5: GREEN})
        ad = ep(t, C["23.d"], 0.5)
        if ad > 0:
            g = ep(t, C["23.d"] + 2.0, 1.4)
            sc = 0.4 + 0.6 * g
            bloco_iso(c, 420, 735, 200 * sc, 110 * sc, 60 * sc, ad)
            expr(c, "2(x−1)(x−2)(x−4)", 830, 700, 34, ad)
            if g > 0.5:
                pill(c, "arestas 1, 2, 4 · V = 8 m³", 830, 770, GREEN, size=28, a=ep(t, C["23.d"] + 3.0, 0.4),
                     anchor="center")
        return
    bloco_iso(c, 600, 560, 340, 200, 120, ep(t, C["24"], 0.4), ("4", "2", "1"), 1.0)


# ======================================================================
# questão 5 (nós fazemos)
# ======================================================================

ALTS5 = [("A", "= (x−1)(x+2)^2", "sinais das raízes trocados", RED), ("B", "= (x+1)^2 (x−2)", "multiplicidades invertidas", RED),
         ("C", "= −(x+1)(x−2)^2", "P(0) = −4", RED), ("D", "= (x+1)(x−2)", "grau 2", RED),
         ("E", "= (x+1)(x−2)^2", "", GREEN)]
G5 = (230, 300, 640, 420)


def b_q5(c, t, C, B):
    sid = which(t, C, ["25", "26", "27"])
    heads = {"25": "LEI A PARTIR DO GRÁFICO", "26": "NÓS FAZEMOS", "27": "AS OUTRAS"}
    head(c, t, B["start"] if sid == "25" else C[sid], "QUESTÃO 5 · ESTILO ENEM", heads[sid], BLUE)
    card(c, *CARD_R)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCD"}
    a0 = ep(t, C["25.a"], 0.4)
    if a0 > 0:
        text(c, "P(x) =", 1110, 240, 30, "black", INK2, a0, align="left")
    K.alternativas(c, t, C, ALTS5, 1110, 270, 600, 30, C["26.ok"], "E", cues_in, cues_x, gap=24)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    X, Y = grafico(c, f_q5, (-1.7, 3.3), (-5.5, 6.5), G5, a0, 1.0, PURPLE, ((-1, "−1"), (2, "2")))
    if a0 > 0:
        c.drawCircle(X(0), Y(4), 12, paint(AMBER, a0))
        pill(c, "(0, 4)", X(0) + 26, Y(4) - 30, AMBER, size=24, a=a0, anchor="left", bounds=(0, 1920))
        text(c, "grau 3", 330, 270, 28, "black", PURPLE, a0)
    if sid == "25":
        pause_timer(c, t, C["25.end"] - 1.4, 1000, 760, dur=1.2)
        return
    if sid == "26":
        aa = ep(t, C["26.a"], 0.5)
        if aa > 0:
            pill(c, "cruza: (x + 1)", X(-1) - 20, Y(0) - 40, RED, size=24, a=aa, anchor="right", bounds=(0, 1920))
        ab = ep(t, C["26.b"], 0.5)
        if ab > 0:
            pill(c, "toca: (x − 2)²", X(2), Y(0) - 50, GREEN, size=24, a=ab, anchor="center", bounds=(0, 1920))
        acc = ep(t, C["26.c"], 0.5)
        ad = ep(t, C["26.d"], 0.5)
        if acc > 0:
            rrect(c, 230, 740, 820, 70, 16, mix("#FFFFFF", PURPLE, 0.14), acc * (1 - ad))
            expr(c, "P(x) = a(x+1)(x−2)^2", 640, 775, 34, acc * (1 - ad))
        if ad > 0:
            rrect(c, 230, 740, 820, 70, 16, mix("#FFFFFF", GREEN, 0.14), ad)
            expr(c, "P(0) = a·1·4 = 4 → a = 1", 640, 775, 34, ad, cores={6: GREEN})
        return


# ======================================================================
# questão 6 (você faz)
# ======================================================================

ALTS6 = [("A", "= x^3 + 4x^2 + 6x + 4", "sinais trocados", RED), ("B", "= x^3 − 4x^2 + 6x − 4", "", GREEN),
         ("C", "= x^3 − 4x^2 + 4x", "produto do par = 0", RED), ("D", "= x^3 − 2x^2 + 2x − 4", "usou x² + 2", RED),
         ("E", "= x^2 − 2x + 2", "grau 2: sem a raiz 2", RED)]


def b_q6(c, t, C, B):
    sid = which(t, C, ["28", "29", "30"])
    heads = {"28": "VOCÊ FAZ", "29": "VAMOS CONFERIR", "30": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "28" else C[sid], "QUESTÃO 6 · ESTILO ENEM", heads[sid], GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS6, 1150, 250, 560, 30, C["29.ok"], "B", cues_in, cues_x, gap=30)
    a0 = ep(t, C["28.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        text(c, "grau 3 · coeficientes reais · dominante 1", 650, 260, 30, "black", INK2, a0)
        linha(c, [("raízes: ", INK), ("2", PURPLE), ("  e  ", INK), ("1 − i", BLUE)], 650, 340, 50, a0)
        text(c, "i² = −1", 650, 410, 30, "black", AMBER, a0)
    if sid == "28":
        pause_timer(c, t, C["28.end"] - 1.9, 650, 600)
        return
    if sid == "29":
        aa = ep(t, C["29.a"], 0.5)
        meias(c, 650, 640, aa * (1 - ep(t, C["29.c"], 0.4)), "1 − i", "1 + i", ep(t, C["29.a"] + 1.4, 0.5))
        ab = ep(t, C["29.b"], 0.5) * (1 - ep(t, C["29.c"], 0.4))
        if ab > 0:
            expr(c, "(1−i)(1+i) = 1 − i^2 = 2", 650, 470, 36, ab, cores={4: GREEN})
        acc = ep(t, C["29.c"], 0.5)
        if acc > 0:
            cartao(c, 240, 470, 820, 110, acc)
            expr(c, "par → x^2 − 2x + 2", 650, 525, 42, acc, cores={2: PURPLE})
        ad = ep(t, C["29.d"], 0.5)
        if ad > 0:
            rrect(c, 240, 610, 820, 120, 22, mix("#FFFFFF", GREEN, 0.14), ad)
            expr(c, "(x−2)(x^2−2x+2)", 650, 650, 34, ad)
            expr(c, "= x^3 − 4x^2 + 6x − 4", 650, 700, 34, ad, cores={0: GREEN})
        ae = ep(t, C["29.e"], 0.5)
        if ae > 0:
            pill(c, "Girard: soma 2 + 2 = 4 = −(−4)/1", 650, 770, PURPLE, size=26, a=ae, anchor="center")
        return
    meias(c, 650, 640, ep(t, C["30"], 0.4), "1 − i", "1 + i")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DE POLINÔMIOS", PURPLE)
    for k, (cue, s_, col) in enumerate((("32.a", "JUNTAMOS TUDO", PURPLE), ("32.b", "CAÇAMOS AS PEGADINHAS", AMBER),
                                        ("32.c", "QUESTÕES INÉDITAS", GREEN))):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 330 + k * 150 + d
        rrect(c, 460, y - 55, 1000, 110, 24, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, 530, y, ak, 30, bg=col)
        text(c, s_, 600, y + 16, 46, "black", col, ak, align="left")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Você já conhecia a bola que quica no eixo?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, girard=b_girard,
              girard_teste=b_girard_teste, atalho_sinais=b_atalho_sinais, caixa=b_caixa, grafico=b_grafico,
              multiplicidade=b_multiplicidade, fatos=b_fatos, atalho_grafico=b_atalho_grafico, conjugadas=b_conjugadas,
              conjugadas_conta=b_conjugadas_conta, atalho_par=b_atalho_par, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q4=b_q4, q5=b_q5, q6=b_q6, ponte=b_ponte, cta=b_cta)
