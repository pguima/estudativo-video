"""Visual — Conceito de Função, Episódio 5: domínio pela fórmula e pelo contexto (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: planilha() (#DIV/0!), calculadora() (Erro na raiz de −4), porteiro(), reta_n()/bola()/faixa()
(reta numérica com bolinha fechada e furo), caixa() (folha com quadradinhos de lado x nos cantos; o lado menor some),
bola_graf() (h(t) = 20t − 5t² de 0 a 4 s) e pontos() (contagem: pontos isolados × linha contínua).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum038", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcoes_ep5_dominio_formula_contexto.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
CORTE = "#F3C9C4"


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


def m(c, s, x, cy, size, a, col=None, align="left"):
    """matemática de uma cor (frações, raízes, potências)"""
    if a <= 0:
        return
    K.mdraw(c, s, x, cy, size, col or INK, a, align=align)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def planilha(c, x, y, a, erro_a=1.0):
    """pedaço de planilha: A1 = 7, B1 = 0, C1 = A1/B1 → #DIV/0!"""
    if a <= 0:
        return
    cw, ch = 210, 74
    rrect(c, x, y, cw * 3 + 70, ch * 3, 10, "#FFFFFF", a, shadow=True)
    for j, L in enumerate("ABC"):
        rrect(c, x + 70 + j * cw, y, cw, ch, 0, "#E9EEF3", a)
        text_mid(c, L, x + 70 + j * cw + cw / 2, y + ch / 2, 26, "black", GRAY, a)
    for i in range(2):
        rrect(c, x, y + ch * (i + 1), 70, ch, 0, "#E9EEF3", a)
        text_mid(c, str(i + 1), x + 35, y + ch * (i + 1.5), 26, "black", GRAY, a)
    for j in range(4):
        line(c, x + 70 + j * cw, y, x + 70 + j * cw, y + ch * 3, "#C9CFD6", a, 2)
    for i in range(4):
        line(c, x, y + i * ch, x + 70 + 3 * cw, y + i * ch, "#C9CFD6", a, 2)
    text_mid(c, "7", x + 70 + cw / 2, y + ch * 1.5, 34, "black", INK, a)
    text_mid(c, "0", x + 70 + cw * 1.5, y + ch * 1.5, 34, "black", INK, a)
    text_mid(c, "=A1/B1", x + 70 + cw * 2.5, y + ch * 1.5, 28, "bold", INK2, a)
    if erro_a > 0:
        rrect(c, x + 70 + cw * 2 + 4, y + ch * 2 + 4, cw - 8, ch - 8, 6, mix("#FFFFFF", RED, 0.2), a * erro_a)
        text_mid(c, "#DIV/0!", x + 70 + cw * 2.5, y + ch * 2.5, 34, "black", RED, a * erro_a)


def calculadora(c, cx, cy, a, erro_a=1.0):
    if a <= 0:
        return
    w, h = 300, 420
    rrect(c, cx - w / 2, cy - h / 2, w, h, 30, "#2B2F37", a, shadow=True)
    rrect(c, cx - w / 2 + 24, cy - h / 2 + 30, w - 48, 120, 12, "#C9D8C5", a)
    m(c, "√{-4}", cx + w / 2 - 40, cy - h / 2 + 70, 34, a, "#2B2F37", align="right")
    if erro_a > 0:
        text(c, "Erro", cx + w / 2 - 40, cy - h / 2 + 136, 40, "black", RED, a * erro_a, align="right")
    for i in range(3):
        for j in range(3):
            rrect(c, cx - w / 2 + 34 + j * 82, cy - 20 + i * 66, 66, 52, 10, "#454B56", a)
    rrect(c, cx - w / 2 + 34, cy + 178, 230, 2, 0, "#2B2F37", a)


def porteiro(c, cx, cy, s, a, col=None):
    """porta com o porteiro ao lado (boné e prancheta)"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, cx - s * 0.55, cy - s * 0.6, s * 0.5, s * 1.1, 10, mix("#FFFFFF", col, 0.18), a)
    c.drawRect(skia.Rect.MakeXYWH(cx - s * 0.55, cy - s * 0.6, s * 0.5, s * 1.1), paint(col, a, stroke=5))
    c.drawCircle(cx - s * 0.13, cy, s * 0.03, paint(col, a))
    # pessoa
    px = cx + s * 0.25
    c.drawCircle(px, cy - s * 0.32, s * 0.12, paint(col, a))
    rrect(c, px - s * 0.17, cy - s * 0.38, s * 0.34, s * 0.06, 6, INK, a)
    rrect(c, px - s * 0.15, cy - s * 0.17, s * 0.30, s * 0.55, s * 0.08, col, a)
    rrect(c, px + s * 0.10, cy - s * 0.05, s * 0.16, s * 0.22, 4, "#FFFFFF", a)
    text(c, "PORTEIRO", px, cy + s * 0.56, s * 0.10, "black", col, a)


def reta_n(c, x0, x1, y, v0, v1, a, rot=None, size=30, col=None, passo=1):
    """reta numérica de v0 a v1 com marcas; devolve X(v). rot = valores com rótulo (None = todos)."""
    X = lambda v: x0 + (v - v0) / (v1 - v0) * (x1 - x0)
    if a <= 0:
        return X
    line(c, x0 - 30, y, x1 + 30, y, col or INK2, a, 5)
    arrow(c, x1 + 10, y, x1 + 46, y, col or INK2, a, 5, 18)
    v = v0
    while v <= v1 + 1e-9:
        xx = X(v)
        line(c, xx, y - 14, xx, y + 14, col or INK2, a, 4)
        if rot is None or v in rot:
            ftext(c, f"{v:g}".replace("-", "−"), xx, y + 58, size, "black", GRAY, a)
        v += passo
    return X


def bola(c, x, y, a, aberta, col, r=16):
    if a <= 0:
        return
    c.drawCircle(x, y, r, paint("#FFFFFF" if aberta else col, a))
    c.drawCircle(x, y, r, paint(col, a, stroke=6))


def faixa(c, xa, xb, y, a, col, inf_esq=False, inf_dir=False, prog_=1.0):
    """trecho pintado de xa a xb (com seta se for ao infinito); prog_ desenha da esquerda para a direita"""
    if a <= 0:
        return
    xe = xa + (xb - xa) * clamp(prog_)
    line(c, xa, y - 22, xe, y - 22, col, a, 12)
    if inf_esq and prog_ > 0.95:
        arrow(c, xa + 20, y - 22, xa - 26, y - 22, col, a, 12, 26)
    if inf_dir and prog_ > 0.95:
        arrow(c, xb - 20, y - 22, xb + 26, y - 22, col, a, 12, 26)


def caixa(c, cx, cy, Wcm, Hcm, x, esc, a, rotulos=True, internos=True):
    """folha Wcm × Hcm (escala esc px/cm) com quadradinhos de lado x nos cantos. Se Hcm − 2x ≤ 0, o lado menor some."""
    if a <= 0:
        return
    w, h = Wcm * esc, Hcm * esc
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(c, x0, y0, w, h, 4, PAPEL, a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, w, h), paint("#B89B6A", a, stroke=3))
    q = min(x, Hcm / 2) * esc
    if q > 0:
        for (qx, qy) in ((x0, y0), (x0 + w - q, y0), (x0, y0 + h - q), (x0 + w - q, y0 + h - q)):
            c.drawRect(skia.Rect.MakeXYWH(qx, qy, q, q), paint(CORTE, a))
            c.drawRect(skia.Rect.MakeXYWH(qx, qy, q, q), paint(RED, a, stroke=3))
        # dobras
        line(c, x0 + q, y0 + q, x0 + w - q, y0 + q, "#9C8156", a, 2.5, dash=(10, 8))
        line(c, x0 + q, y0 + h - q, x0 + w - q, y0 + h - q, "#9C8156", a, 2.5, dash=(10, 8))
        line(c, x0 + q, y0 + q, x0 + q, y0 + h - q, "#9C8156", a, 2.5, dash=(10, 8))
        line(c, x0 + w - q, y0 + q, x0 + w - q, y0 + h - q, "#9C8156", a, 2.5, dash=(10, 8))
        if q > 26:
            text_mid(c, "x", x0 + q / 2, y0 + q / 2, min(34, q * 0.6), "black", RED, a)
    if rotulos:
        text(c, f"{Wcm:g} cm", cx, y0 - 22, 32, "black", INK2, a)
        text_mid(c, f"{Hcm:g} cm", x0 - 22, cy, 32, "black", INK2, a, align="right")
    if internos and q > 0:
        larg = Hcm - 2 * x
        comp = Wcm - 2 * x
        fmt = lambda v: f"{v:.1f}".replace(".", ",").replace(",0", "")
        text(c, f"{fmt(comp)} cm", cx, cy - 6, 30, "black", BLUE if comp > 0 else RED, a)
        text(c, f"largura {fmt(larg)} cm", cx, cy + 34, 26, "black", GREEN if larg > 0 else RED, a)


def bola_graf(c, x0, y0, w, h, a, prog_=1.0):
    """gráfico de h(t) = 20t − 5t², t de 0 a 4 s (eixos e curva)"""
    if a <= 0:
        return
    line(c, x0, y0 + h, x0 + w + 20, y0 + h, INK2, a, 4)
    line(c, x0, y0 + h, x0, y0 - 20, INK2, a, 4)
    text(c, "t (s)", x0 + w + 30, y0 + h + 10, 24, "black", GRAY, a, align="left")
    text(c, "altura", x0, y0 - 34, 24, "black", GRAY, a)
    p = skia.Path()
    n = int(60 * clamp(prog_)) + 1
    for k in range(n):
        tt = 4 * k / 60
        X = x0 + tt / 4 * w
        Y = y0 + h - (20 * tt - 5 * tt * tt) / 20 * h
        (p.moveTo if k == 0 else p.lineTo)(X, Y)
    c.drawPath(p, paint(BLUE, a, stroke=6, cap_round=True))
    for tt in (0, 4):
        ftext(c, f"{tt} s", x0 + tt / 4 * w, y0 + h + 44, 26, "black", INK2, a)


def pontos(c, x0, y0, w, h, a, linha_a=0.0):
    """contagem: preço de n ingressos (R$ 20 cada), n = 0..5 → pontos isolados; linha_a desenha a linha errada"""
    if a <= 0:
        return
    line(c, x0, y0 + h, x0 + w + 20, y0 + h, INK2, a, 4)
    line(c, x0, y0 + h, x0, y0 - 20, INK2, a, 4)
    text(c, "ingressos", x0 + w + 36, y0 + h + 8, 24, "black", GRAY, a, align="left")
    text(c, "R$", x0 - 14, y0 - 30, 24, "black", GRAY, a)
    P = [(x0 + n / 5 * w, y0 + h - n / 5 * h) for n in range(6)]
    if linha_a > 0:
        line(c, P[0][0], P[0][1], P[-1][0], P[-1][1], RED, a * linha_a, 5)
    for k, (X, Y) in enumerate(P):
        c.drawCircle(X, Y, 11, paint(GREEN, a))
        ftext(c, str(k), X, y0 + h + 30, 22, "black", INK2, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÕES · EPISÓDIO 5", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    xg = 3.0 * ep(t, C["01.a"] + 1.2, 2.0)
    caixa(c, 560, 520, 30, 20, xg, 22, aa, internos=False)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1080, 260, 640, 150, 24, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "FÓRMULA", 1400, 300, 26, "black", PURPLE, ab)
        linha(c, [("x = 12 cm", BLUE), ("  →  V = −288", PURPLE)], 1400, 360, 40, ab)
        conferido(c, "a conta sai", 1200, 460, ep(t, C["01.b"] + 1.5, 0.4), True, 30)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1080, 520, 640, 150, 24, mix("#FFFFFF", RED, 0.10), acc)
        text(c, "FOLHA", 1400, 560, 26, "black", RED, acc)
        linha(c, [("largura: 20 − 24 = ", INK), ("−4 cm", RED)], 1400, 620, 38, acc)
        selo(c, 1400, 730, ep(t, C["01.c"] + 1.6, 0.4), "UM LADO SOME", RED, -5, 32)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "ouça as duas: a FÓRMULA e o PROBLEMA", W / 2, 840, ad, 36, BLUE)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÕES · EP. 5", "AO FINAL DESTA AULA", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    for k, s in enumerate(("1/{x-3}", "√{x-2}")):
        ak = aa * ep(t, C["02.a"] + 0.5 + k * 0.6, 0.4)
        if ak <= 0:
            continue
        x = 620 + k * 680
        rrect(c, x - 260, 250, 520, 200, 24, "#FFFFFF", ak, shadow=True)
        text(c, ("FRAÇÃO", "RAIZ")[k], x, 300, 30, "black", PURPLE, ak)
        m(c, s, x, 380, 64, ak, PURPLE, "center")
    ab = ep(t, C["02.b"], 0.5)
    itens = [("medida", "> 0"), ("contagem", "0, 1, 2, ..."), ("tempo", "≥ 0")]
    for k, (tit, sub) in enumerate(itens):
        ak = ab * ep(t, C["02.b"] + 1.2 + k * 0.5, 0.4)
        if ak <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 210, 540, 420, 170, 24, mix("#FFFFFF", GREEN, 0.12), ak)
        text(c, tit, x, 600, 36, "black", GREEN, ak)
        text(c, sub, x, 670, 40, "black", INK, ak)
    if ab > 0:
        text(c, "CONTEXTO", W / 2, 800, 34, "black", GREEN, ab, tracking=3)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "DOMÍNIO", 520, 300, 40, "black", BLUE, aa)
        text(c, "episódio 2", 520, 350, 26, "bold", GRAY, aa)
        para(c, "o conjunto das entradas PERMITIDAS", 300, 460, 40, "black", INK, aa, 440, 50)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        line(c, 960, 240, 960, 780, "#E6E6E2", ab, 3)
        text(c, "DIVIDIU POR NEGATIVO?", 1400, 300, 36, "black", AMBER, ab)
        text(c, "série de Equações e inequações", 1400, 350, 24, "bold", GRAY, ab)
        m(c, "-3x ≥ 12", 1400, 470, 60, ab, INK, "center")
        a2 = ep(t, C["03.b"] + 3.4, 0.4)
        m(c, "x ≤ -4", 1400, 600, 60, a2, PURPLE, "center")
        if a2 > 0:
            selo(c, 1400, 710, a2, "O SINAL VIRA", AMBER, -4, 32)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "QUANDO A CONTA DÁ ERRO", "AS DUAS PROIBIÇÕES", RED)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    planilha(c, 230, 300, aa, ep(t, C["04.a"] + 1.6, 0.4))
    if aa > 0:
        text(c, "PLANILHA", 560, 260, 30, "black", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    calculadora(c, 1350, 470, ab, ep(t, C["04.b"] + 1.8, 0.4))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 230, 700, 1460, 120, 24, mix("#FFFFFF", RED, 0.10), acc)
        linha(c, [("1. ", RED), ("dividir por ZERO", INK), ("     2. ", RED), ("raiz de NEGATIVO", INK)], W / 2, 760, 42, acc)


# ======================================================================
# bloco a — o porteiro
# ======================================================================

def b_porteiro(c, t, C, B):
    head(c, t, B["start"], "DOMÍNIO DA FÓRMULA", "QUEM PODE ENTRAR?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 220, 1460, 120, 24, mix("#FFFFFF", BLUE, 0.10), aa)
        para(c, "DOMÍNIO DA FÓRMULA: o maior conjunto de números reais com o qual a conta EXISTE", 270, 270, 36,
             "black", BLUE, aa, 1400, 44)
    ab = ep(t, C["05.b"], 0.5)
    X = reta_n(c, 300, 1000, 560, -3, 3, ab, size=28)
    if ab > 0:
        text(c, "NÚMEROS REAIS = todos os números da reta", 650, 440, 32, "black", BLUE, ab)
        for v, s in ((-2.5, "−2,5"), (0.5, "1/2"), (1.8, "1,8")):
            av = ep(t, C["05.b"] + 2.0 + abs(v) * 0.3, 0.4)
            c.drawCircle(X(v), 560, 10, paint(PURPLE, ab * av))
            text(c, s, X(v), 520, 26, "black", PURPLE, ab * av)
    acc = ep(t, C["05.c"], 0.5)
    porteiro(c, 1400, 560, 340, acc)
    if acc > 0:
        pill(c, "só entra o x com o qual a conta NÃO dá erro", 1400, 810, BLUE, size=24, a=acc, anchor="center")
        pill(c, "cada proibição = uma RESTRIÇÃO", 650, 720, PURPLE, size=26, a=ep(t, C["05.c"] + 3.2, 0.4),
             anchor="center")


# ======================================================================
# blocos b e c — denominador e radicando
# ======================================================================

def b_denominador(c, t, C, B):
    head(c, t, B["start"], "PROIBIÇÃO 1", "DENOMINADOR ≠ 0", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        frac(c, "a", "b", 400, 320, 80, INK, aa, "black")
        arrow(c, 470, 370, 560, 370, AMBER, aa, 5, 16)
        text(c, "DENOMINADOR = o número de baixo", 580, 382, 32, "black", AMBER, aa, align="left")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        m(c, "f(x) = 1/{x-3}", 260, 540, 70, ab, PURPLE)
        rrect(c, 900, 470, 760, 120, 22, mix("#FFFFFF", RED, 0.10), ep(t, C["06.b"] + 2.2, 0.4))
        m(c, "x = 3 → 1/{0}", 940, 530, 56, ep(t, C["06.b"] + 2.2, 0.4), RED)
        conferido(c, "proibido", 1400, 545, ep(t, C["06.b"] + 3.6, 0.4), False, 34)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 900, 620, 760, 120, 22, mix("#FFFFFF", GREEN, 0.10), acc)
        m(c, "x = 4 → 1/{1} = 1", 940, 680, 56, acc, GREEN)
        conferido(c, "pode", 1480, 695, ep(t, C["06.c"] + 1.6, 0.4), True, 34)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 230, 640, 600, 140, 24, PURPLE, ad, shadow=True)
        text(c, "DOMÍNIO", 530, 690, 26, "black", "#FFFFFF", ad)
        m(c, "x ≠ 3", 530, 742, 52, ad, "#FFFFFF", "center")


def b_radicando(c, t, C, B):
    head(c, t, B["start"], "PROIBIÇÃO 2", "RADICANDO ≥ 0", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        m(c, "√{9} = 3", 260, 300, 60, aa, BLUE)
        text(c, "porque 3 · 3 = 9", 260, 380, 30, "black", INK2, aa, align="left")
        a2 = ep(t, C["07.a"] + 4.4, 0.4)
        if a2 > 0:
            rrect(c, 868, 256, 64, 84, 12, mix("#FFFFFF", AMBER, 0.45), a2)
            m(c, "√{9}", 820, 300, 70, a2, INK)
            text(c, "RADICANDO = o que fica dentro", 820, 390, 28, "black", AMBER, a2, align="left")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        m(c, "g(x) = √{x-2}", 260, 500, 62, ab, PURPLE)
        m(c, "x - 2 ≥ 0", 900, 470, 48, ep(t, C["07.b"] + 2.0, 0.4), INK)
        m(c, "x ≥ 2", 900, 545, 56, ep(t, C["07.b"] + 3.8, 0.4), PURPLE)
    acc = ep(t, C["07.c"], 0.5)
    X = reta_n(c, 360, 1040, 720, -1, 5, ep(t, C["07.b"] + 3.8, 0.4), size=28)
    if acc > 0:
        bola(c, X(2), 720, acc, False, GREEN)
        faixa(c, X(2), X(5), 720, acc, GREEN, inf_dir=True, prog_=ep(t, C["07.c"], 1.0))
        rrect(c, 1180, 460, 500, 110, 22, mix("#FFFFFF", GREEN, 0.12), acc)
        m(c, "x = 2 → √{0} = 0", 1210, 515, 44, acc, GREEN)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 1180, 600, 500, 110, 22, mix("#FFFFFF", RED, 0.10), ad)
        m(c, "x = 1 → √{-1}", 1210, 655, 44, ad, RED)
        conferido(c, "proibido", 1440, 775, ad, False, 30)


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "BOLINHA FECHADA OU FURO?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 150, "ATALHO", ["ache a FRONTEIRA: iguale a zero o que está em perigo"], aa, 36)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 420, 660, 380, 26, "#FFFFFF", ab, shadow=True)
        text(c, "RAIZ", 590, 480, 40, "black", PURPLE, ab)
        m(c, "√{0} = 0", 590, 560, 50, ab, INK, "center")
        X = reta_n(c, 360, 820, 680, 0, 4, ab, rot=(2,), size=26)
        bola(c, X(2), 680, ab, False, GREEN, 20)
        faixa(c, X(2), X(4), 680, ab, GREEN, inf_dir=True)
        text(c, "o zero ENTRA: bolinha fechada", 590, 780, 26, "black", GREEN, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 420, 660, 380, 26, "#FFFFFF", acc, shadow=True)
        text(c, "DENOMINADOR", 1330, 480, 40, "black", PURPLE, acc)
        m(c, "1/{0}", 1330, 560, 50, acc, RED, "center")
        X = reta_n(c, 1100, 1560, 680, 0, 4, acc, rot=(3,), size=26)
        faixa(c, X(0), X(4), 680, acc, GREEN, inf_esq=True, inf_dir=True)
        bola(c, X(3), 680, acc, True, RED, 20)
        text(c, "o zero NÃO entra: furo", 1330, 780, 26, "black", RED, acc)


# ======================================================================
# bloco d — as duas juntas · sem restrição
# ======================================================================

def b_juntas(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head_seq(c, t, C, [("09", "AS DUAS JUNTAS", "DOIS PORTEIROS", PURPLE), ("10", "SEM PROIBIÇÃO", "ENTRA TODO MUNDO", GREEN)])
    card(c, *CARD_R)
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        m(c, "h(x) = 5/√{x}", 260, 330, 72, aa, PURPLE)
        if aa > 0:
            rrect(c, 900, 240, 760, 110, 22, mix("#FFFFFF", BLUE, 0.10), ep(t, C["09.a"] + 1.4, 0.4))
            linha(c, [("porteiro 1 · raiz:  ", BLUE), ("x ≥ 0", INK)], 1280, 295, 36, ep(t, C["09.a"] + 1.4, 0.4))
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            rrect(c, 900, 380, 760, 110, 22, mix("#FFFFFF", RED, 0.10), ab)
            linha(c, [("porteiro 2 · denominador:  ", RED), ("√0 = 0 → 5/0", INK)], 1280, 435, 34, ab)
        acc = ep(t, C["09.c"], 0.5)
        X = reta_n(c, 380, 1300, 680, -2, 4, acc, size=28)
        if acc > 0:
            faixa(c, X(0), X(4), 680, acc, GREEN, inf_dir=True, prog_=ep(t, C["09.c"], 1.0))
            bola(c, X(0), 680, acc, True, RED, 20)
            pill(c, "o 0 passa no 1º e é barrado no 2º", 840, 790, AMBER, size=26, a=acc, anchor="center")
            rrect(c, 1400, 600, 280, 130, 24, PURPLE, ep(t, C["09.c"] + 2.4, 0.4))
            m(c, "x > 0", 1540, 665, 52, ep(t, C["09.c"] + 2.4, 0.4), "#FFFFFF", "center")
        return
    aa = ep(t, C["10.a"], 0.5)
    m(c, "p(x) = 3x^2 - x + 7", W / 2, 360, 80, aa, PURPLE, "center")
    if aa > 0:
        chip(c, "sem divisão por x", 720, 500, GREEN, ep(t, C["10.a"] + 2.0, 0.4), 34)
        chip(c, "sem raiz", 1200, 500, GREEN, ep(t, C["10.a"] + 2.6, 0.4), 34)
    ab = ep(t, C["10.b"], 0.5)
    X = reta_n(c, 460, 1460, 690, -5, 5, ab, rot=(-5, 0, 5), size=28)
    if ab > 0:
        faixa(c, X(-5), X(5), 690, ab, GREEN, inf_esq=True, inf_dir=True, prog_=ep(t, C["10.b"], 1.0))
        rrect(c, 730, 770, 460, 80, 20, PURPLE, ab)
        text_mid(c, "DOMÍNIO = todos os reais", 960, 810, 30, "black", "#FFFFFF", ab)


# ======================================================================
# bloco e — contexto
# ======================================================================

def b_contexto(c, t, C, B):
    sid = which(t, C, ["11", "12"])
    head_seq(c, t, C, [("11", "O CONTEXTO", "FAZ SENTIDO AQUI?", BLUE), ("12", "O CONTEXTO", "TEMPO E MEDIDAS", BLUE)])
    card(c, *CARD_R)
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        porteiro(c, 420, 470, 300, aa)
        if aa > 0:
            rrect(c, 640, 240, 1040, 110, 22, mix("#FFFFFF", BLUE, 0.10), aa)
            text_mid(c, "2ª pergunta: isso FAZ SENTIDO aqui?", 1160, 295, 36, "black", BLUE, aa)
            pill(c, "CONTEXTO = a situação real do problema", 1160, 390, BLUE, size=26,
                 a=ep(t, C["11.a"] + 3.0, 0.4), anchor="center")
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            text(c, "CONTAGEM → números NATURAIS", 1160, 480, 32, "black", GREEN, ab)
            text(c, "0, 1, 2, 3, ...", 1160, 530, 30, "black", INK, ab)
            selo(c, 1520, 520, ep(t, C["11.b"] + 4.0, 0.4), "½ INGRESSO?", RED, -6, 26)
        acc = ep(t, C["11.c"], 0.5)
        pontos(c, 900, 600, 480, 170, acc)
        if acc > 0:
            pill(c, "PONTOS ISOLADOS", 1560, 700, GREEN, size=26, a=acc, anchor="center")
        return
    aa = ep(t, C["12.a"], 0.5)
    bola_graf(c, 330, 330, 520, 360, aa, ep(t, C["12.a"] + 2.0, 1.6))
    if aa > 0:
        text(c, "TEMPO ≥ 0 e às vezes LIMITADO", 590, 260, 30, "black", BLUE, aa)
        m(c, "0 ≤ t ≤ 4 s", 590, 820, 46, ep(t, C["12.a"] + 3.0, 0.4), PURPLE, "center")
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        line(c, 960, 240, 960, 820, "#E6E6E2", ab, 3)
        text(c, "MEDIDAS > 0", 1380, 290, 38, "black", BLUE, ab)
        rrect(c, 1180, 360, 400, 260, 8, mix("#FFFFFF", BLUE, 0.12), ab)
        c.drawRect(skia.Rect.MakeXYWH(1180, 360, 400, 260), paint(BLUE, ab, stroke=5))
        text(c, "lado > 0", 1380, 350, 26, "black", INK2, ab)
        text(c, "altura > 0", 1600, 500, 26, "black", INK2, ab, align="left")
        text(c, "largura > 0", 1380, 670, 26, "black", INK2, ab)


# ======================================================================
# bloco f — a caixa (exemplo NOSSO: folha 36 × 16)
# ======================================================================

def b_caixa(c, t, C, B):
    sid = which(t, C, ["13", "14"])
    head_seq(c, t, C, [("13", "VÁRIAS CONDIÇÕES", "A CAIXA DE PAPELÃO", PURPLE),
                       ("14", "QUAL MANDA?", "O ELO MAIS FRACO", PURPLE)])
    card(c, *CARD_R)
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        xg = 3.0 * ep(t, C["13.a"] + 1.4, 1.6)
        caixa(c, 620, 520, 36, 16, xg, 25, aa, internos=False)
        conds = [("13.b", "altura:", "x > 0"), ("13.c", "comprimento:", "36 - 2x > 0  →  x < 18"),
                 ("13.d", "largura:", "16 - 2x > 0  →  x < 8")]
        for k, (cue, rot, s) in enumerate(conds):
            ak = ep(t, C[cue], 0.5)
            if ak <= 0:
                continue
            y = 300 + k * 160
            rrect(c, 1120, y - 55, 560, 120, 20, "#FFFFFF", ak, shadow=True)
            text(c, rot, 1150, y - 14, 24, "black", GRAY, ak, align="left")
            m(c, s.replace("  ", " "), 1150, y + 30, 34, ak, PURPLE)
        return
    aa = ep(t, C["14.a"], 0.5)
    xg = lerp(3.0, 8.0, ep(t, C["14.a"], 2.2))
    caixa(c, 620, 470, 36, 16, xg, 25, max(aa, ep(t, C["14"], 0.3)))
    if aa > 0 and xg >= 7.95:
        selo(c, 620, 700, ep(t, C["14.a"] + 2.2, 0.4), "A LARGURA SUMIU", RED, -5, 32)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        # corrente: três elos, o fraco em vermelho
        for k in range(3):
            col = RED if k == 2 else INK2
            rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1160 + k * 150, 280, 170, 80), 40, 40)
            c.drawRRect(rr, paint(col, ab, stroke=10 if k < 2 else 5))
        text(c, "x > 0", 1245, 410, 26, "black", INK2, ab)
        text(c, "x < 18", 1395, 410, 26, "black", INK2, ab)
        text(c, "x < 8", 1545, 410, 26, "black", RED, ab)
        pill(c, "vale a MAIS RESTRITIVA", 1400, 480, PURPLE, size=28, a=ep(t, C["14.b"] + 2.0, 0.4), anchor="center")
    acc = ep(t, C["14.c"], 0.5)
    X = reta_n(c, 1130, 1630, 640, 0, 10, acc, rot=(0, 8), size=26, passo=2)
    if acc > 0:
        faixa(c, X(0), X(8), 640, acc, GREEN, prog_=ep(t, C["14.c"], 1.0))
        bola(c, X(0), 640, acc, True, GREEN)
        bola(c, X(8), 640, acc, True, GREEN)
        m(c, "0 < x < 8", 1380, 770, 48, acc, PURPLE, "center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "O SINAL VIRA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    m(c, "g(x) = √{10-2x}", 260 if t >= C["16"] else W / 2, 300, 66, aa, PURPLE,
      "left" if t >= C["16"] else "center")
    if t < C["16"]:
        if aa > 0:
            text(c, "domínio = ?", W / 2, 470, 52, "black", INK, aa)
        pause_timer(c, t, C["15.end"] - 1.9, W / 2, 640)
        return
    passos = [("16.a", "10 - 2x ≥ 0", INK), ("16.b", "-2x ≥ -10", INK), ("16.c", "x ≤ 5", PURPLE)]
    for k, (cue, s, col) in enumerate(passos):
        ak = ep(t, C[cue], 0.5)
        m(c, s, 300, 430 + k * 120, 54, ak, col)
    avc = ep(t, C["16.c"], 0.4)
    if avc > 0:
        selo(c, 720, 668, avc, "dividiu por −2: O SINAL VIRA", AMBER, -4, 26)
    ad = ep(t, C["16.d"], 0.5)
    X = reta_n(c, 1050, 1600, 400, 2, 7, ad, size=26)
    if ad > 0:
        faixa(c, X(2), X(5), 400, ad, GREEN, inf_esq=True)
        bola(c, X(5), 400, ad, False, GREEN)
        rrect(c, 1020, 500, 640, 90, 18, mix("#FFFFFF", GREEN, 0.12), ad)
        m(c, "x = 5 → √{0} = 0", 1050, 545, 38, ad, GREEN)
        a2 = ep(t, C["16.d"] + 2.4, 0.4)
        rrect(c, 1020, 610, 640, 90, 18, mix("#FFFFFF", RED, 0.10), a2)
        m(c, "x = 6 → √{-2}", 1050, 655, 38, a2, RED)
    ae = ep(t, C["16.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1020, 730, 640, 100, "ATALHO", ["teste a FRONTEIRA e um VIZINHO"], ae, 28)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Denominador não pode ser zero; raiz quadrada não aceita negativo.",
          "O contexto corta ainda mais: medida positiva, contagem inteira.",
          "Com várias condições, vale a mais restritiva."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Esquecer o CONTEXTO: a fórmula aceita x = 9 na folha 36 × 16", "a conta sai: V = −324",
          "largura 16 − 18 = −2 cm: a caixa não existe"),
         ("Excluir à toa o 2 em √(x − 2)", "o zero assusta, como no denominador",
          "√0 = 0: TESTE na fórmula antes de expulsar"),
         ("Usar só UMA condição: em 5/√x, responder x ≥ 0", "você viu a raiz e parou",
          "a raiz está no denominador: o zero cai (x > 0)"),
         ("Linha CONTÍNUA num problema de contagem", "a fórmula aceita 2,5 ingressos",
          "meio ingresso não se vende: PONTOS ISOLADOS")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20", "21"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        if s.startswith("="):
            m(c, s[1:].strip(), 190, y + size * 1.7, size * 1.5, a, col)
            y += size * 4.2
            continue
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS3 = [("A", "=x ≥ 2", "esquece o denominador", RED),
         ("B", "=x ≠ 5", "esquece a raiz", RED),
         ("C", "=x > 2 e x ≠ 5", "exclui o 2 à toa", RED),
         ("D", "=x ≥ 2 e x ≠ 5", "", GREEN),
         ("E", "=x > 5", "x = 3 funciona", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "DOMÍNIO DE UMA FÓRMULA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Uma planilha calcula um índice pela fórmula", INK), ("=f(x) = √{x-2}/{x-5}", PURPLE),
                          ("e mostra ERRO sempre que a conta não pode ser feita com números reais. Os valores de x "
                           "SEM erro são os que satisfazem", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS3, 1000, 240, 680, 30, C["23.ok"], "D", cues_in, cues_x, gap=30)
    if t < C["23"]:
        pause_timer(c, t, C["22.end"] - 1.9, 540, min(yend + 120, 740))
        return
    y0 = 230
    ap = ep(t, C["23"], 0.4)
    _painel(c, y0 - 20, ap)
    aa = ep(t, C["23.a"], 0.4)
    if aa > 0:
        text(c, "RAIZ", 230, y0 + 40, 24, "black", BLUE, aa, align="left")
        m(c, "x - 2 ≥ 0 → x ≥ 2", 230, y0 + 90, 38, aa, INK)
    ab = ep(t, C["23.b"], 0.4)
    if ab > 0:
        text(c, "DENOMINADOR", 230, y0 + 160, 24, "black", RED, ab, align="left")
        m(c, "x - 5 ≠ 0 → x ≠ 5", 230, y0 + 210, 38, ab, INK)
    acc = ep(t, C["23.c"], 0.4)
    X = reta_n(c, 260, 820, y0 + 340, 0, 7, max(aa, 0) * ep(t, C["23.c"], 0.4), size=24)
    if acc > 0:
        faixa(c, X(2), X(7), y0 + 340, acc, GREEN, inf_dir=True)
        bola(c, X(2), y0 + 340, acc, False, GREEN)
        m(c, "x = 2 → √{0}/{-3} = 0", 230, y0 + 450, 32, acc, GREEN)
    ad = ep(t, C["23.d"], 0.4)
    if ad > 0:
        bola(c, X(5), y0 + 340, ad, True, RED, 18)
        m(c, "x = 5 → √{3}/{0}", 230, y0 + 540, 32, ad, RED)
        pill(c, "o 2 ENTRA · o 5 fica de FORA", 540, y0 + 580, PURPLE, size=22, a=ad, anchor="center")
    if t >= C["24.xe"]:
        ae = ep(t, C["24.xe"] + 1.6, 0.4)
        if ae > 0:
            rrect(c, 200, y0 + 380, 680, 230, 16, "#FFFFFF", ae)
            m(c, "x = 3 → √{1}/{-2} = -1/2", 230, y0 + 480, 34, ae, GREEN)
            text(c, "entre 2 e 5 a conta FUNCIONA", 540, y0 + 570, 26, "black", GREEN, ae)


ALTS5 = [("A", "=0 < x < 15", "só o lado de 30 cm", RED),
         ("B", "=0 < x < 10", "", GREEN),
         ("C", "=x > 0", "ignora o tamanho da folha", RED),
         ("D", "=0 < x < 20", "tira só UM x do lado de 20", RED),
         ("E", "=10 < x < 15", "largura negativa", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "DOMÍNIO PELO CONTEXTO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS5, 1060, 240, 620, 30, C["26.ok"], "B", cues_in, cues_x, gap=30)
    if t < C["26"]:
        yend = _enunciado(c, [("De uma folha de 30 cm por 20 cm recortam-se, nos quatro cantos, quadrados de lado x cm, e "
                               "dobram-se as abas para formar uma caixa sem tampa. O volume é", INK),
                              ("=V(x) = x(30-2x)(20-2x)", PURPLE),
                              ("Para a caixa existir, o domínio de V deve ser", INK)], a0, 240, 27, 760)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        pause_timer(c, t, C["25.end"] - 1.9, 540, min(yend + 110, 750))
        return
    # resolução: a animação principal da folha 30 × 20 (o lado de 20 some em x = 10)
    ap = ep(t, C["26"], 0.4)
    _painel(c, 210, ap, 840)
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        for k, s in enumerate(("x > 0", "30 - 2x > 0 → x < 15", "20 - 2x > 0 → x < 10")):
            ak = ep(t, C["26.a"] + k * 2.4, 0.4)
            m(c, s, 210, 255 + k * 50, 30, ak, PURPLE if k == 2 else INK)
    ab = ep(t, C["26.b"], 0.4)
    xg = lerp(4.0, 10.0, ep(t, C["26.b"] - 1.2, 2.6)) if t >= C["26.b"] - 1.2 else 4.0
    caixa(c, 540, 610, 30, 20, xg, 13, aa, rotulos=True)
    if aa > 0:
        fmt = f"{xg:.1f}".replace(".", ",")
        pill(c, f"x = {fmt} cm", 830, 560, RED, size=22, a=aa, anchor="center")
    if ab > 0 and xg >= 9.95:
        selo(c, 540, 790, ab, "A CAIXA NÃO EXISTE", RED, -5, 28)
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        pill(c, "elo mais fraco: o lado de 20 cm", 540, 408, PURPLE, size=22, a=acc, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DE FUNÇÕES", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        text(c, "último episódio deste assunto: JUNTAMOS TUDO", W / 2, 290, 40, "black", INK, aa)
    ab = ep(t, C["29.b"], 0.5)
    areas = [("FÍSICA", BLUE), ("QUÍMICA", PURPLE), ("BIOLOGIA", GREEN), ("GEOGRAFIA", AMBER)]
    for k, (s, col) in enumerate(areas):
        ak = ab * ep(t, C["29.b"] + 0.5 + k * 0.4, 0.4)
        if ak <= 0:
            continue
        x = 390 + k * 380
        rrect(c, x - 160, 400, 320, 150, 26, mix("#FFFFFF", col, 0.14), ak, shadow=True)
        text_mid(c, s, x, 475, 36, "black", col, ak)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 680, acc, "CAÇA ÀS PEGADINHAS", AMBER, -4, 40)
    pill(c, "ep. 6 · revisão de Conceito de função", W / 2, 820, PURPLE, size=30, a=ep(t, C["29.c"] + 1.0, 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Qual proibição da calculadora você já viu dar erro?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, porteiro=b_porteiro,
              denominador=b_denominador, radicando=b_radicando, atalho=b_atalho, juntas=b_juntas, contexto=b_contexto,
              caixa=b_caixa, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q3=b_q3, q5=b_q5, ponte=b_ponte,
              cta=b_cta)
