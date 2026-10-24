"""Visual — Equações e Inequações do 1º Grau, Episódio 3: inequações, a regra do sinal, intervalos e resposta inteira (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: reta_n() (reta numérica com marcas inteiras), bola() (bolinha aberta = porta fechada, fechada = porta
aberta), faixa() (trecho pintado, com seta quando vai ao infinito), espelho() (a reta gira no espelho: 2 e 5 viram −2 e −5 e
o < vira > com flash âmbar), placa() (as placas do cotidiano), vira() (o carimbo "O SINAL VIRA").
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
_s = importlib.util.spec_from_file_location("comum035", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_equacoes_ep3_inequacoes_intervalos.mp4"
CARD_R = K.CARD_R


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]"""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        x += w_


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def reta_n(c, x0, x1, y, v0, v1, a, rot=None, size=30, col=None, passo=1):
    """reta numérica de v0 a v1 com marcas inteiras; devolve X(v). rot = valores com rótulo (None = todos)."""
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
            s = f"{v:g}".replace("-", "−")
            ftext(c, s, xx, y + 58, size, "black", GRAY, a)
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


def vira(c, x, y, a, s="O SINAL VIRA", size=34):
    """carimbo âmbar com flash"""
    if a <= 0:
        return
    fl = max(0.0, 1 - a * 1.4)
    if fl > 0:
        c.drawCircle(x, y, 220, paint(AMBER, 0.25 * fl))
    selo(c, x, y, a, s, AMBER, -4, size)


def espelho(c, t, t_m, cx, y, a, larg=1300, sinal_y=None, t_flash=None):
    """reta de −6 a 6 com 2 e 5 marcados; a partir de t_m gira no espelho (eixo vertical no 0): 2 → −2, 5 → −5."""
    if a <= 0:
        return
    x0, x1 = cx - larg / 2, cx + larg / 2
    X = reta_n(c, x0, x1, y, -6, 6, a, rot={-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6})
    m = ease_io(clamp((t - t_m) / 1.6)) if t_m is not None else 0.0
    # espelho: o eixo no zero
    if t_m is not None and t >= t_m - 0.3:
        am = a * ep(t, t_m - 0.3, 0.4)
        line(c, X(0), y - 170, X(0), y + 40, PURPLE, am, 4, dash=(14, 10))
        text(c, "ESPELHO", X(0), y - 186, 20, "black", PURPLE, am, tracking=2)
    for v, col in ((2, BLUE), (5, PURPLE)):
        sx = math.cos(m * math.pi)            # 1 → −1 (a "virada" da página)
        xx = X(0) + (X(v) - X(0)) * sx
        r = 22 * max(0.35, abs(sx))
        c.drawCircle(xx, y, r + 4, paint("#FFFFFF", a))
        c.drawCircle(xx, y, r, paint(col, a))
        lab = f"{v}" if m < 0.5 else f"−{v}"
        ftext(c, lab, xx, y - 52, 46, "black", col, a)
    sy = sinal_y or (y - 260)
    if m < 0.5:
        linha(c, [("2", BLUE), ("  <  ", INK), ("5", PURPLE)], cx, sy, 96, a)
    else:
        af = ep(t, t_flash or (t_m + 0.8), 0.4)
        fl = 1 - af
        if fl > 0:
            rrect(c, cx - 300, sy - 80, 600, 160, 40, AMBER, a * 0.35 * fl)
        linha(c, [("−2", BLUE), ("  >  ", AMBER), ("−5", PURPLE)], cx, sy, 96, a)


def placa(c, cx, cy, w, h, a, topo, valor, sub, col):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 70, 26, col, a)
    rrect(c, cx - w / 2, cy - h / 2 + 40, w, 30, 0, col, a)
    text_mid(c, topo, cx, cy - h / 2 + 36, 26, "black", "#FFFFFF", a, tracking=2)
    fmid(c, valor, cx, cy + 10, 64, "black", INK, a)
    text(c, sub, cx, cy + h / 2 - 34, 24, "bold", GRAY, a)


def passos(c, t, rows, x, y0, size, dy, xnota=1660):
    """linhas da conta: rows = [(instante, expr, nota, cor_da_nota)]"""
    for k, (t0, ex, nota, col) in enumerate(rows):
        a, d = rise(t, t0)
        if a <= 0:
            continue
        y = y0 + k * dy + d
        expr(c, ex, x, y, size, a, align="left")
        if nota:
            pill(c, nota, xnota, y, col or PURPLE, size=24, a=a, anchor="right", bounds=(0, 1920))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "INEQUAÇÕES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    espelho(c, t, C["01.b"] + 1.2, W / 2, 610, aa, sinal_y=330, t_flash=C["01.c"])
    ab = ep(t, C["01.b"], 0.4) * (1 - ep(t, C["01.c"], 0.4))
    if ab > 0:
        pill(c, "× (−1) NOS DOIS", W / 2, 460, PURPLE, size=30, a=ab, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "a ÚNICA regra nova · e a que mais derruba", W / 2, 810, AMBER, size=32, a=ad, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver inequações", "−2x + 7 > 1  →  x < 3"),
            ("02.b", "escrever a resposta como intervalo", "2 < x ≤ 5  =  ]2, 5]"),
            ("02.c", "achar o menor número inteiro que serve", "n > 800  →  801")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 58, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "O ROTEIRO", 520, 280, 34, "black", PURPLE, aa)
        text(c, "episódio 1", 520, 324, 24, "bold", GRAY, aa)
        for k, s in enumerate(["denominadores", "parênteses", "separar", "reduzir e dividir", "CONFERIR"]):
            y = 400 + k * 76
            col = GREEN if k == 4 else PURPLE
            badge_num(c, k + 1, 330, y, aa, 24, bg=col)
            text(c, s, 380, y + 12, 34, "black", col, aa, align="left")
    line(c, 860, 240, 860, 800, "#E6E6E2", aa, 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "A ORDEM NA RETA", 1300, 280, 34, "black", BLUE, ab)
        text(c, "série de Operações", 1300, 324, 24, "bold", GRAY, ab)
        X = reta_n(c, 960, 1640, 560, -6, 0, ab)
        bola(c, X(-5), 560, ab, False, RED)
        bola(c, X(-2), 560, ab, False, GREEN)
        ftext(c, "−5", X(-5), 505, 40, "black", RED, ab)
        ftext(c, "−2", X(-2), 505, 40, "black", GREEN, ab)
        arrow(c, 1000, 690, 1600, 690, BLUE, ab, 5, 18)
        text(c, "mais à direita = MAIOR", 1300, 750, 32, "black", BLUE, ab)


# ======================================================================
# concreto: as placas e os símbolos
# ======================================================================

PLACAS = [("PARQUE", "1,40 m", "altura mínima", BLUE, "h ≥ 1,40 m"),
          ("FÁBRICA", "60 °C", "no máximo", RED, "T ≤ 60 °C"),
          ("APLICATIVO", "R$ 26,00", "mais de · ganha cupom", GREEN, "C > R$ 26")]


def _placas(c, t, cues, y, a_mult=1.0):
    for k, (topo, val, sub, col, _) in enumerate(PLACAS):
        a, d = rise(t, cues[k])
        placa(c, 400 + k * 560, y + d, 460, 250, a * a_mult, topo, val, sub, col)


def b_placas(c, t, C, B):
    frame(c, t, B["start"], "VOCÊ JÁ OBEDECE INEQUAÇÕES", "SEM SABER", BLUE)
    _placas(c, t, [C["04.a"], C["04.b"], C["04.c"]], 440)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "nenhuma placa diz UM número: todas dizem uma FAIXA", W / 2, 720, ad, 34, BLUE)


def b_simbolos(c, t, C, B):
    frame(c, t, B["start"], "AS PLACAS EM SÍMBOLOS", "< · ≤ · > · ≥", PURPLE)
    _placas(c, t, [C["05"], C["05"], C["05"]], 360, 0.9)
    for k, cue in enumerate(("05.a", "05.b", "05.c")):
        a, d = rise(t, C[cue])
        if a > 0:
            fmid(c, PLACAS[k][4], 400 + k * 560, 580 + d, 54, "black", PLACAS[k][3], a)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        boxed(c, 300, 660, 1320, 150, BLUE, ad, 0.08)
        text(c, "DESIGUALDADE ESTRITA", W / 2, 715, 30, "black", BLUE, ad, tracking=2)
        fmid(c, "<  ou  >  ·  o próprio número NÃO serve", W / 2, 768, 34, "black", INK, ad)


# ======================================================================
# bloco a — o conjunto solução
# ======================================================================

def b_conjunto(c, t, C, B):
    frame(c, t, B["start"], "DA EQUAÇÃO À INEQUAÇÃO", "A RESPOSTA VIRA UM CONJUNTO", BLUE)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 200, 1320, 100, BLUE, aa, 0.08)
        linha(c, [("INEQUAÇÃO", BLUE), (": uma desigualdade no lugar do igual", INK)], W / 2, 250, 34, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        expr(c, "x + 2 = 5", 420, 400, 56, ab)
        X = reta_n(c, 700, 1600, 400, 0, 6, ab)
        bola(c, X(3), 400, ab, False, BLUE)
        pill(c, "UM número", 1700, 330, BLUE, size=24, a=ab, anchor="right", bounds=(0, 1920))
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        expr(c, "x + 2 > 5", 420, 600, 56, acc)
        X = reta_n(c, 700, 1600, 600, 0, 6, acc)
        faixa(c, X(3), X(6) + 30, 600, acc, GREEN, inf_dir=True, prog_=ep(t, C["06.c"] + 0.4, 1.0))
        bola(c, X(3), 600, acc, True, GREEN)
        for k, (v, s) in enumerate(((3.5, "3,5"), (4, "4"), (5.6, "100…"))):
            a2 = ep(t, C["06.c"] + 1.4 + k * 0.6, 0.3)
            chip(c, s, X(v), 515, GREEN, a2, 26)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        boxed(c, 300, 720, 1320, 100, BLUE, ad, 0.08)
        linha(c, [("CONJUNTO SOLUÇÃO", BLUE), (": todos os números que servem", INK)], W / 2, 770, 34, ad)


# ======================================================================
# bloco b — a regra de ouro e o espelho
# ======================================================================

def b_regra(c, t, C, B):
    frame(c, t, B["start"], "SOMAR E MULTIPLICAR POR POSITIVO", "O SINAL FICA", PURPLE)
    a0 = ep(t, C["07"], 0.5)
    expr(c, "2 < 5", W / 2, 270, 96, a0)
    rows = [("07.a", "2 + 3 < 5 + 3", "5 < 8", "+ 3 nos dois lados"),
            ("07.b", "2 · 3 < 5 · 3", "6 < 15", "× 3 nos dois lados")]
    for k, (cue, e1, e2, nota) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 430 + k * 150 + d
        expr(c, e1, 420, y, 60, a, align="left")
        expr(c, "→ " + e2, 900, y, 60, a, align="left")
        conferido(c, "continua certo", 1260, y + 12, a, True, 30)
        pill(c, nota, 420, y - 62, PURPLE, size=22, a=a)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "número POSITIVO: o sinal NÃO muda", W / 2, 760, acc, 36)


def b_espelho(c, t, C, B):
    head_seq(c, t, C, [("08", "E POR NEGATIVO?", "O ESPELHO", AMBER), ("09", "A REGRA DE OURO", "O SINAL VIRA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        espelho(c, t, C["08.b"] + 1.0, W / 2, 620, aa, sinal_y=320, t_flash=C["08.d"])
        acc = ep(t, C["08.c"], 0.4) * (1 - ep(t, C["08.d"], 0.4))
        if acc > 0:
            pill(c, "eles trocam de lado", W / 2, 790, PURPLE, size=30, a=acc, anchor="center")
        ad = ep(t, C["08.d"], 0.5)
        vira(c, W / 2, 790, ad, "−2 MAIS À DIREITA: O SINAL VIRA", 30)
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        boxed(c, 240, 230, 1440, 230, PURPLE, aa, 0.08)
        text(c, "MULTIPLICOU OU DIVIDIU POR NEGATIVO", W / 2, 300, 40, "black", PURPLE, aa, tracking=1)
        linha(c, [("<", INK), ("  vira  ", GRAY), (">", AMBER), ("        ", INK), ("≤", INK), ("  vira  ", GRAY),
                   ("≥", AMBER)], W / 2, 395, 60, aa)
    ab = ep(t, C["09.b"], 0.5)
    K.atalho(c, 240, 510, 1440, 280, "ATALHO · O ESPELHO SÓ APARECE COM O MENOS",
             ["× ou ÷ por NEGATIVO  →  vira", "somar, subtrair, × ou ÷ por positivo  →  nunca vira"], ab, 34)


# ======================================================================
# bloco c — o exemplo e o teste
# ======================================================================

def b_exemplo(c, t, C, B):
    frame(c, t, B["start"], "VAMOS USAR", "−2x + 7 > 1", PURPLE)
    rows = [(C["10.a"], "-2x + 7 > 1", "", None),
            (C["10.b"], "-2x > -6", "− 7 nos dois lados", PURPLE),
            (C["10.d"], "x < 3", "÷ (−2): o > virou <", AMBER)]
    passos(c, t, rows, 380, 300, 86, 170, xnota=1600)
    acc = ep(t, C["10.c"], 0.4)
    if acc > 0 and t < C["10.d"] + 0.3:
        pill(c, "÷ (−2) nos dois lados", 1600, 470, PURPLE, size=24, a=acc * (1 - ep(t, C["10.d"], 0.3)), anchor="right",
             bounds=(0, 1920))
    av = ep(t, C["10.v"], 0.4)
    vira(c, 1250, 640, av * (1 - ep(t, C["10.d"], 0.4)))
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        fmid(c, "−6 ÷ (−2) = 3", 700, 800, 36, "black", GRAY, ad)


def b_teste(c, t, C, B):
    frame(c, t, B["start"], "ERREI O SINAL?", "TESTE UM DE DENTRO E UM DE FORA", GREEN)
    a0 = ep(t, C["11"], 0.5)
    expr(c, "-2x + 7 > 1  →  x < 3", W / 2, 230, 50, a0)
    X = reta_n(c, 420, 1500, 420, -2, 6, a0)
    faixa(c, X(-2) - 30, X(3), 420, a0, GREEN, inf_esq=True)
    bola(c, X(3), 420, a0, True, GREEN)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        chip(c, "x = 0", X(0), 330, GREEN, aa, 28)
        conferido(c, "−2 · 0 + 7 = 7 > 1  ·  verdade", 300, 570, aa, True, 32)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        chip(c, "x = 4", X(4), 330, RED, ab, 28)
        conferido(c, "−2 · 4 + 7 = −1 > 1 ?  ·  falso", 300, 640, ab, False, 32)
    acc = ep(t, C["11.c"], 0.5)
    K.atalho(c, 300, 690, 1320, 140, "ATALHO", ["o de dentro PASSA · o de fora FALHA"], acc, 32)


# ======================================================================
# bloco d — bolinhas e intervalos
# ======================================================================

def porta(c, x, y, a, aberta, col, s=1.0):
    """ícone de porta: fechada (retângulo cheio) ou aberta (folha em perspectiva)"""
    if a <= 0:
        return
    rrect(c, x - 34 * s, y - 60 * s, 68 * s, 120 * s, 6, "#FFFFFF", a)
    c.drawRect(skia.Rect.MakeXYWH(x - 34 * s, y - 60 * s, 68 * s, 120 * s), paint(col, a, stroke=4))
    if aberta:
        p = skia.Path()
        p.moveTo(x - 34 * s, y - 60 * s); p.lineTo(x - 70 * s, y - 46 * s); p.lineTo(x - 70 * s, y + 74 * s)
        p.lineTo(x - 34 * s, y + 60 * s); p.close()
        c.drawPath(p, paint(col, a * 0.85))
    else:
        rrect(c, x - 28 * s, y - 54 * s, 56 * s, 108 * s, 4, col, a * 0.85)
        c.drawCircle(x + 18 * s, y, 5 * s, paint("#FFFFFF", a))


def b_bolinhas(c, t, C, B):
    frame(c, t, B["start"], "NA RETA", "BOLINHA ABERTA OU FECHADA?", BLUE)
    aa = ep(t, C["12.a"], 0.5)
    X = reta_n(c, 300, 1000, 360, -2, 6, aa)
    faixa(c, X(-2) - 30, X(3), 360, aa, GREEN, inf_esq=True, prog_=ep(t, C["12.a"] + 0.3, 1.0))
    fmid(c, "x < 3", 1150, 290, 56, "black", INK, aa)
    a2 = ep(t, C["12.a"] + 2.2, 0.4)
    if a2 > 0:
        pill(c, "EXTREMO: o número da ponta", X(3), 250, BLUE, size=22, a=a2, anchor="center")
    ab = ep(t, C["12.b"], 0.5)
    bola(c, X(3), 360, max(aa * 0.4, ab), True, GREEN)
    if ab > 0:
        porta(c, 1150, 420, ab, False, RED, 0.8)
        ftext(c, "bolinha ABERTA = porta fechada", 1220, 410, 30, "black", INK, ab, align="left")
        text(c, "o extremo NÃO entra", 1220, 455, 26, "bold", GRAY, ab, align="left")
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        X2 = reta_n(c, 300, 1000, 680, -2, 6, acc)
        faixa(c, X2(-2) - 30, X2(3), 680, acc, GREEN, inf_esq=True)
        bola(c, X2(3), 680, acc, False, GREEN)
        fmid(c, "x ≤ 3", 1150, 610, 56, "black", INK, acc)
        porta(c, 1150, 740, acc, True, GREEN, 0.8)
        ftext(c, "bolinha FECHADA = porta aberta", 1220, 730, 30, "black", INK, acc, align="left")
        text(c, "o extremo entra", 1220, 775, 26, "bold", GRAY, acc, align="left")


TAB = [("13.b", "2 < x ≤ 5", "]2, 5]", 2, 5, True, False, False, False),
       ("13.c", "x ≥ −1", "[−1, +∞[", -1, 6, False, True, False, True),
       ("13.d", "x < 3", "]−∞, 3[", -2, 3, True, True, True, False)]


def b_intervalos(c, t, C, B):
    head_seq(c, t, C, [("13", "INTERVALO", "UM TRECHO DA RETA COM COLCHETES", BLUE),
                       ("14", "ATALHO", "COMO LER OS COLCHETES", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            text(c, "DESIGUALDADE", 380, 250, 22, "black", GRAY, aa, tracking=2)
            text(c, "INTERVALO", 760, 250, 22, "black", GRAY, aa, tracking=2)
            text(c, "NA RETA", 1300, 250, 22, "black", GRAY, aa, tracking=2)
        for k, (cue, des, itv, va, vb, ab_a, ab_b, ie, idr) in enumerate(TAB):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 350 + k * 130 + d
            fmid(c, des, 380, y, 44, "black", INK, a)
            fmid(c, itv, 760, y, 50, "black", BLUE, a)
            X = reta_n(c, 1000, 1600, y + 26, -2, 6, a, rot=set(), col=LIGHT)
            xa = X(va) - (30 if ie else 0)
            xb = X(vb) + (30 if idr else 0)
            faixa(c, xa, xb, y + 26, a, GREEN, inf_esq=ie, inf_dir=idr)
            if not ie:
                bola(c, X(va), y + 26, a, ab_a, GREEN, 13)
                ftext(c, f"{va:g}".replace("-", "−"), X(va), y + 70, 22, "black", GRAY, a)
            if not idr:
                bola(c, X(vb), y + 26, a, ab_b, GREEN, 13)
                ftext(c, f"{vb:g}", X(vb), y + 70, 22, "black", GRAY, a)
        ae = ep(t, C["13.e"], 0.5)
        if ae > 0:
            boxed(c, 300, 730, 1320, 90, AMBER, ae, 0.12)
            fmid(c, "o ∞ nunca entra: o colchete do lado dele fica sempre ABERTO", W / 2, 775, 32, "black", INK, ae)
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 240, 1400, 560, GREEN, aa, 0.06)
        text(c, "ATALHO", W / 2, 290, 22, "black", GREEN, aa, tracking=2)
        for k, (s, sub, ok) in enumerate((("[2", "colchete ABRAÇANDO: o 2 entra", True),
                                          ("]2", "colchete VIRADO PARA FORA: o 2 fica de fora", False))):
            y = 430 + k * 210
            fmid(c, s, 520, y, 120, "black", GREEN if ok else RED, aa)
            bola(c, 700, y, aa, not ok, GREEN if ok else RED, 22)
            ftext(c, sub, 790, y + 12, 36, "black", INK, aa, align="left")


# ======================================================================
# bloco e — inequação dupla
# ======================================================================

def b_dupla(c, t, C, B):
    frame(c, t, B["start"], "INEQUAÇÃO DUPLA", "DOIS LIMITES DE UMA VEZ", PURPLE)
    rows = [(C["15.a"], "1 < 2x - 3 ≤ 7", "", None),
            (C["15.c"], "4 < 2x ≤ 10", "+ 3 nas TRÊS partes", PURPLE),
            (C["15.d"], "2 < x ≤ 5", "÷ 2 nas TRÊS partes", PURPLE)]
    passos(c, t, rows, 340, 260, 68, 120, xnota=1600)
    ab = ep(t, C["15.b"], 0.5) * (1 - ep(t, C["15.c"], 0.4))
    if ab > 0:
        regra(c, "a MESMA operação nas TRÊS partes", W / 2, 430, ab, 34)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        X = reta_n(c, 480, 1240, 700, 0, 7, ae)
        faixa(c, X(2), X(5), 700, ae, GREEN, prog_=ep(t, C["15.e"], 1.0))
        bola(c, X(2), 700, ae, True, GREEN)
        bola(c, X(5), 700, ae, False, GREEN)
        fmid(c, "]2, 5]", 1460, 680, 72, "black", BLUE, ae)


# ======================================================================
# bloco f — a resposta inteira
# ======================================================================

def b_inteira(c, t, C, B):
    frame(c, t, B["start"], "QUANDO A RESPOSTA É INTEIRA", "PESSOAS NÃO VÊM EM PEDAÇOS", BLUE)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        fmid(c, "n > 800", 360, 330, 64, "black", INK, aa)
        X = reta_n(c, 640, 1560, 330, 798, 803, aa, size=28)
        faixa(c, X(800), X(803) + 30, 330, aa, GREEN, inf_dir=True)
        bola(c, X(800), 330, aa, True, RED)
        pill(c, "800 não serve", X(800), 240, RED, size=22, a=aa, anchor="center")
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        X = reta_n(c, 640, 1560, 330, 798, 803, 0)
        c.drawCircle(X(801), 330, 26, paint(GREEN, ab))
        fmid(c, "801", X(801), 330, 22, "black", "#FFFFFF", ab)
        pill(c, "o menor que serve: 801", 1100, 450, GREEN, size=30, a=ab, anchor="center")
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        fmid(c, "n > 342,8   →   343", W / 2, 560, 60, "black", INK, acc)
    ad = ep(t, C["16.d"], 0.5)
    K.atalho(c, 300, 640, 1320, 190, "ATALHO",
             ["“maior que”: pule para o próximo inteiro", "“maior ou igual”: o próprio número já serve"], ad, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "E ESCREVA COMO INTERVALO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    expr(c, "5 - 3x ≥ -7", W / 2, 260, 80, aa)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 520)
    if t < C["18"]:
        return
    rows = [(C["18.a"], "-3x ≥ -12", "− 5 nos dois lados", PURPLE),
            (C["18.v"], "x ≤ 4", "÷ (−3): o ≥ virou ≤", AMBER)]
    passos(c, t, rows, 300, 390, 66, 110, xnota=1000)
    av = ep(t, C["18.v"], 0.4)
    vira(c, 1340, 420, av * (1 - ep(t, C["18.c"], 0.4)), "O SINAL VIRA", 30)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        X = reta_n(c, 1080, 1620, 470, 0, 6, acc, size=24)
        faixa(c, X(0) - 30, X(4), 470, acc, GREEN, inf_esq=True)
        bola(c, X(4), 470, acc, False, GREEN)
        fmid(c, "]−∞, 4]", 1350, 600, 60, "black", BLUE, acc)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        conferido(c, "x = 0:  5 ≥ −7  ·  verdade", 300, 690, ad, True, 32)
        conferido(c, "x = 5:  −10 ≥ −7  ·  falso", 300, 770, ep(t, C["18.d"] + 2.2, 0.4), False, 32)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Multiplicou ou dividiu por negativo, o sinal vira.",
          "Bolinha aberta: o extremo fica de fora.",
          "Teste um número de dentro e um de fora."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("−2x > −6  →  x > 3", "na equação, o sinal de igual nunca muda",
          "dividiu por negativo: o sinal vira  →  x < 3"),
         ("n > 800  →  n = 800", "800 é o número que aparece na conta",
          "a desigualdade estrita exclui o extremo: 801"),
         ("2 < x ≤ 5  →  [2, 5]", "os dois números são as pontas do mesmo trecho",
          "cada ponta tem o seu sinal: ]2, 5]")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, s, a, y0=250, size=29, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        ftext(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _questao(c, t, C, sid_q, sid_r, sid_x, titulo, sub, texto, alts, okL, size_alt=30):
    head(c, t, C[sid_q], titulo, sub, BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C[f"{sid_q}.a"], 0.4) * (1 - ep(t, C[sid_r], 0.4))
    yend = _enunciado(c, texto, a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"{sid_q}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in "ABCDE" if L != okL}
    K.alternativas(c, t, C, alts, 1000, 240, 680, size_alt, C[f"{sid_r}.ok"], okL, cues_in, cues_x, gap=26)
    return yend, ep(t, C[sid_r], 0.4)


ALTS4 = [("A", "no máximo 7,5 minutos.", "60 ÷ 8", RED),
         ("B", "no máximo 20 minutos.", "não inverteu o sinal", RED),
         ("C", "no mínimo 20 minutos.", "", GREEN),
         ("D", "no mínimo 27,5 minutos.", "220 ÷ 8: chegaria a 0 °C", RED),
         ("E", "no mínimo 35 minutos.", "280 ÷ 8: sinal do 60", RED)]


def b_q4(c, t, C, B):
    yend, ap = _questao(c, t, C, "23", "24", "25", "QUESTÃO 4 · EU FAÇO", "O FORNO QUE ESFRIA",
                        "Após ser desligado, um forno industrial esfria segundo o modelo T = 220 − 8t, em que T é a "
                        "temperatura, em °C, e t o tempo, em minutos, válido nos primeiros 25 minutos. Por segurança, "
                        "uma peça só pode ser retirada quando a temperatura for de, no máximo, 60 °C. Para isso, "
                        "deve-se esperar", ALTS4, "C")
    if ap > 0:
        _painel(c, ap)
        aa = ep(t, C["24.a"], 0.4)
        if aa > 0:
            linha(c, [("no máximo 60", AMBER), ("  →  T ≤ 60", INK)], 550, 290, 34, aa)
        rows = [(C["24.b"], "220 - 8t ≤ 60", "", None),
                (C["24.b"] + 3.4, "-8t ≤ -160", "", None),
                (C["24.v"], "t ≥ 20", "", None)]
        passos(c, t, rows, 240, 380, 50, 90)
        av = ep(t, C["24.v"], 0.4)
        if av > 0:
            pill(c, "÷ (−8): O SINAL VIRA", 880, 560, AMBER, size=22, a=av, anchor="right", bounds=(0, 1920))
        ad = ep(t, C["24.d"], 0.4)
        if ad > 0:
            rrect(c, 200, 640, 700, 170, 18, mix("#FFFFFF", GREEN, 0.10), ad)
            text(c, "o forno ESFRIA: é preciso ESPERAR", 550, 690, 26, "black", INK2, ad)
            ftext(c, "t = 25:  220 − 200 = 20 °C  ✓", 550, 760, 28, "black", GREEN, ad)


ALTS8 = [("A", "[10, 20]", "colchetes iguais", RED),
         ("B", "]10, 20[", "colchetes iguais", RED),
         ("C", "]10, 20]", "", GREEN),
         ("D", "]13, 23]", "esqueceu a tarifa fixa", RED),
         ("E", "]16, 26]", "somou 6", RED)]


def b_q8(c, t, C, B):
    yend, ap = _questao(c, t, C, "26", "27", "28", "QUESTÃO 8 · NÓS FAZEMOS", "A CORRIDA E O CUPOM",
                        "Um aplicativo cobra, por corrida, C = 6 + 2d reais, em que d é a distância em quilômetros. Um "
                        "passageiro só ganha um cupom de desconto se a corrida custar mais de R$ 26,00, e ele tem R$ 46,00 "
                        "disponíveis para pagá-la. As distâncias d que lhe permitem ganhar o cupom e pagar a corrida "
                        "formam o intervalo", ALTS8, "C", 34)
    pause_timer(c, t, C["26.end"] - 1.9, 550, min(yend + 90, 760))
    if ap > 0:
        _painel(c, ap)
        aa = ep(t, C["27.a"], 0.4)
        if aa > 0:
            linha(c, [("mais de 26", AMBER), ("  →  <", INK)], 550, 280, 30, aa)
            linha(c, [("tem 46", AMBER), ("  →  ≤", INK)], 550, 330, 30, aa)
        rows = [(C["27.b"], "26 < 6 + 2d ≤ 46", "", None),
                (C["27.c"], "20 < 2d ≤ 40", "", None),
                (C["27.d"], "10 < d ≤ 20", "", None)]
        passos(c, t, rows, 240, 420, 48, 86)
        ae = ep(t, C["27.e"], 0.4)
        if ae > 0:
            X = reta_n(c, 260, 640, 720, 0, 25, ae, rot={10, 20}, size=22, passo=5)
            faixa(c, X(10), X(20), 720, ae, GREEN)
            bola(c, X(10), 720, ae, True, GREEN, 12)
            bola(c, X(20), 720, ae, False, GREEN, 12)
            ftext(c, "d = 15 → R$ 36 ✓", 790, 715, 24, "black", GREEN, ae)


ALTS7 = [("A", "6,0", "média 5,4", RED),
         ("B", "7,0", "", GREEN),
         ("C", "7,5", "média simples", RED),
         ("D", "8,5", "esqueceu o peso da prova", RED),
         ("E", "10,5", "21 ÷ 2", RED)]


def b_q7(c, t, C, B):
    yend, ap = _questao(c, t, C, "29", "30", "31", "QUESTÃO 7 · VOCÊ FAZ", "A NOTA MÍNIMA",
                        "Em uma disciplina, a média final é calculada com peso 2 para a prova e peso 3 para o trabalho. "
                        "Para ser aprovado, o aluno precisa de média final igual ou superior a 6,0. Um aluno tirou 4,5 na "
                        "prova. A menor nota que ele precisa tirar no trabalho para ser aprovado é", ALTS7, "B", 34)
    af = ep(t, C["29.f"], 0.4) * (1 - ap)
    if af > 0:
        rrect(c, 180, yend + 10, 740, 120, 18, mix("#FFFFFF", PURPLE, 0.10), af)
        text(c, "MÉDIA COM PESOS", 550, yend + 50, 20, "black", PURPLE, af, tracking=2)
        expr(c, "2·4,5+3T/5", 550, yend + 96, 34, af)
    pause_timer(c, t, C["29.end"] - 2.4, 550, min(yend + 220, 770), dur=2.0)
    if ap > 0:
        _painel(c, ap)
        aa = ep(t, C["30.a"], 0.4)
        if aa > 0:
            linha(c, [("igual ou superior a 6", AMBER), ("  →  ≥ 6", INK)], 550, 285, 30, aa)
        rows = [(C["30.b"], "2·4,5+3T/5 ≥ 6", "", None),
                (C["30.c"], "9 + 3T ≥ 30", "", None),
                (C["30.d"], "T ≥ 7", "", None)]
        passos(c, t, rows, 240, 400, 46, 100)
        acc = ep(t, C["30.c"], 0.4)
        if acc > 0:
            pill(c, "× 5 (positivo): o sinal FICA", 880, 500, GREEN, size=20, a=acc, anchor="right", bounds=(0, 1920))
        ae = ep(t, C["30.e"], 0.4)
        if ae > 0:
            rrect(c, 200, 690, 700, 110, 18, mix("#FFFFFF", GREEN, 0.10), ae)
            ftext(c, "T = 7:  (9 + 21) ÷ 5 = 6,0  ✓", 550, 760, 28, "black", GREEN, ae)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O PONTO DE EQUILÍBRIO", PURPLE)
    for k, (cue, nome, l1, l2, col) in enumerate((("33.a", "LOCADORA A", "R$ 90,00 por dia", "+ R$ 0,50 por km", BLUE),
                                                  ("33.b", "LOCADORA B", "R$ 60,00 por dia", "+ R$ 0,80 por km", PURPLE))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 360 + k * 700
        rrect(c, x, 250 + d, 500, 300, 26, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250 + d, 500, 70, 26, col, a)
        rrect(c, x, 290 + d, 500, 30, 0, col, a)
        text_mid(c, nome, x + 250, 285 + d, 30, "black", "#FFFFFF", a, tracking=2)
        text(c, l1, x + 250, 410 + d, 44, "black", INK, a)
        text(c, l2, x + 250, 480 + d, 40, "black", col, a)
    acc = ep(t, C["33.c"], 0.5)
    if acc > 0:
        fmid(c, "?", W / 2, 400, 120, "black", AMBER, acc)
        pill(c, "depende de quanto você vai rodar", W / 2, 640, AMBER, size=32, a=acc, anchor="center")
    pill(c, "ep. 4 · o ponto de equilíbrio", W / 2, 760, PURPLE, size=32, a=ep(t, C["33.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"],
        "Você já esqueceu de virar o sinal?", canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, placas=b_placas, simbolos=b_simbolos,
              conjunto=b_conjunto, regra=b_regra, espelho=b_espelho, exemplo=b_exemplo, teste=b_teste,
              bolinhas=b_bolinhas, intervalos=b_intervalos, dupla=b_dupla, inteira=b_inteira, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q4=b_q4, q8=b_q8, q7=b_q7, ponte=b_ponte, cta=b_cta)
