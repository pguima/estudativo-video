"""Visual — Progressão Geométrica, Episódio 3: soma infinita (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: chocolate() (barra comida pela metade do que sobra, com a fração comida), quadrado() (quadrado de
área 1 pintado por metades sucessivas, alternando corte vertical e horizontal, com contador 0,5 · 0,75 · 0,875…),
bola_trajeto() (quiques: descidas em azul e subidas em verde, cada uma q vezes a anterior), barras_bola() (descidas e
subidas empilhando em duas barras que se juntam no total), linha() (texto com cor por trecho, mantém o espaço de milhar).
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
_s = importlib.util.spec_from_file_location("comum047", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pg_ep3_soma_infinita.mp4"
CARD_R = K.CARD_R
CHOCO = "#7A4A2A"
CHOCO2 = "#A9714B"


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


def freio(c, q, cx, cy, a, size=30):
    """o selo verde de conferência: q = … está entre −1 e 1? ✓"""
    if a <= 0:
        return
    s = f"q = {q} está entre −1 e 1?  ✓"
    w = ftext_w(s, "black", size) + 60
    rrect(c, cx - w / 2, cy - size, w, size * 2, size * 0.5, mix("#FFFFFF", GREEN, 0.16), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size, w, size * 2), size * 0.5, size * 0.5),
                paint(GREEN, a, stroke=3))
    fmid(c, s, cx, cy, size, "black", GREEN, a)


def chocolate(c, x, y, w, h, comidos, a):
    """barra de chocolate; 'comidos' = quantas metades-do-que-sobrou já foram comidas (pode ser fracionário)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, CHOCO, a, shadow=True)
    for k in range(1, 8):
        line(c, x + w * k / 8, y + 8, x + w * k / 8, y + h - 8, CHOCO2, a * 0.6, 3)
    line(c, x + 8, y + h / 2, x + w - 8, y + h / 2, CHOCO2, a * 0.6, 3)
    ini = 0.0
    for k in range(6):
        f = clamp(comidos - k)
        if f <= 0:
            break
        larg = w * (0.5 ** (k + 1))
        rrect(c, x + w * ini, y - 4, larg * f, h + 8, 6, "#FFFFFF", a)
        c.drawRect(skia.Rect.MakeXYWH(x + w * ini, y - 4, larg * f, h + 8), paint(AMBER, a * 0.9, stroke=3))
        ini += larg / w
    return ini


def _pecas_quadrado(x, y, L, n):
    """retângulos das n primeiras peças (metade do que sobrou), alternando corte vertical/horizontal"""
    rx, ry, rw, rh = x, y, L, L
    out = []
    for k in range(n):
        if k % 2 == 0:
            out.append((rx, ry, rw / 2, rh)); rx += rw / 2; rw /= 2
        else:
            out.append((rx, ry, rw, rh / 2)); ry += rh / 2; rh /= 2
    return out


def quadrado(c, x, y, L, n, a, tons=(BLUE, PURPLE)):
    """quadrado de área 1 pintado por metades sucessivas: n peças (pode ser fracionário: a última entra com fade)"""
    if a <= 0:
        return
    rrect(c, x, y, L, L, 6, "#FFFFFF", a, shadow=True)
    nn = int(n) + 1
    for k, (px, py, pw, ph) in enumerate(_pecas_quadrado(x, y, L, min(nn, 12))):
        f = clamp(n - k)
        if f <= 0:
            break
        col = tons[k % 2]
        c.drawRect(skia.Rect.MakeXYWH(px + 2, py + 2, max(pw - 4, 1), max(ph - 4, 1)), paint(mix("#FFFFFF", col, 0.75), a * f))
        if k < 4:
            fr_s = ["1/2", "1/4", "1/8", "1/16"][k]
            K.expr(c, fr_s, px + pw / 2, py + ph / 2, [70, 60, 46, 34][k], a * f, cores=None)
    c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), paint(INK, a, stroke=4))


def contador(c, cx, cy, n, a, rot="ÁREA PINTADA"):
    if a <= 0:
        return
    v = 1 - 0.5 ** max(int(n), 0)
    s = f"{v:.4f}".rstrip("0").rstrip(".").replace(".", ",") if n >= 1 else "0"
    rrect(c, cx - 210, cy - 80, 420, 160, 22, "#10141A", a)
    text(c, rot, cx, cy - 36, 22, "black", "#9AA3B2", a)
    fmid(c, s, cx, cy + 30, 64, "black", "#FFD166", a)


def bola_trajeto(c, x0, ybase, esc, h0, q, n, a, passo=110):
    """quiques: descida de h0 (azul), subida q·h0 (verde), descida q·h0 (azul)…; n = segmentos visíveis (fracionário)"""
    if a <= 0:
        return
    line(c, x0 - 40, ybase, x0 + passo * 6, ybase, INK2, a, 4)
    segs = [(h0, "d")]
    h = h0
    for _ in range(5):
        h *= q
        segs += [(h, "s"), (h, "d")]
    for k, (hh, tipo) in enumerate(segs):
        f = clamp(n - k)
        if f <= 0:
            break
        x = x0 + passo * ((k + 1) // 2) * 0.9 + (0 if tipo == "d" else 26)
        col = BLUE if tipo == "d" else GREEN
        y_top = ybase - hh * esc
        if tipo == "d":
            line(c, x, y_top, x, y_top + (ybase - y_top) * f, col, a, 7)
        else:
            line(c, x, ybase, x, ybase - (ybase - y_top) * f, col, a, 7)
        if k == 0:
            c.drawCircle(x, y_top - 18, 18, paint(AMBER, a))


def barras_bola(c, x, ybase, esc, desc, sub, ud, us, utot, a, lab=True):
    """duas barras (descidas azul, subidas verde) que enchem com ud, us e depois se juntam num total (utot)"""
    if a <= 0:
        return
    w = 120
    hd, hs = desc * esc * ud, sub * esc * us
    if utot < 1:
        rrect(c, x, ybase - hd, w, hd, 10, BLUE, a * (1 - utot))
        rrect(c, x + 180, ybase - hs, w, hs, 10, GREEN, a * (1 - utot))
        if lab:
            text(c, f"descidas: {fmt(desc * ud) if ud < 1 else fmt(desc)} m", x + w / 2, ybase + 40, 26, "black", BLUE,
                 a * ep_val(ud) * (1 - utot))
            text(c, f"subidas: {fmt(sub * us) if us < 1 else fmt(sub)} m", x + 180 + w / 2, ybase + 80, 26, "black", GREEN,
                 a * ep_val(us) * (1 - utot))
    if utot > 0:
        xm = x + 90
        rrect(c, xm, ybase - hd - hs, w, hd, 10, BLUE, a * utot)
        rrect(c, xm, ybase - hs, w, hs, 10, GREEN, a * utot)
        text(c, f"total: {fmt(desc + sub)} m", xm + w / 2, ybase + 50, 34, "black", INK, a * utot)


def ep_val(u):
    return 1.0 if u > 0.02 else 0.0


def fmt(v):
    v = round(v, 1)
    return (str(int(v)) if v == int(v) else f"{v:.1f}").replace(".", ",")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROGRESSÃO GEOMÉTRICA · EPISÓDIO 3", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    n = 11 * clamp((t - C["01.a"] - 0.4) / 6.0)
    bola_trajeto(c, 260, 820, 52, 8, 0.75, n, aa)
    if aa > 0:
        pill(c, "solta de 8 m · sobe 3/4 da altura anterior", 260, 230, INK2, size=28, a=aa, bounds=(0, 1920))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        selo(c, 1420, 330, ab, "INFINITOS QUIQUES", AMBER, -4, 40)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        linha(c, [("distância total = ", INK), ("?", AMBER)], 1420, 470, 54, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 1160, 560, 520, 170, 30, mix("#FFFFFF", GREEN, 0.14), ad, shadow=True)
        fmid(c, "56 m", 1420, 645, 100, "black", GREEN, ad)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        pill(c, "nem um centímetro a mais", 1420, 790, PURPLE, size=30, a=ae, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "PROGRESSÃO GEOMÉTRICA · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de PROGRESSÃO GEOMÉTRICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "SOMAR INFINITOS", "termos de uma PG", PURPLE), ("02.b", "DÍZIMA → FRAÇÃO", "0,2727… = ?", BLUE),
             ("02.c", "A BOLA", "sem cair nos distratores", AMBER)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        ftext(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    for k, (cue, rot, ex) in enumerate((("03.a", "episódio 2 · soma finita", "Sₙ = a₁·(q^n-1)/(q-1)"),
                                        ("03.b", "série de Frações", "1 - 3/4 = 1/4  ·  5 ÷ 1/4 = 5 · 4 = 20"),
                                        ("03.c", "série de dízimas", "0,2727… = 27/99"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 290 + k * 190 + d
        rrect(c, 260, y - 80, 1400, 160, 24, "#FFFFFF", a, shadow=True)
        pill(c, rot, 300, y - 80, BLUE, size=22, a=a, bounds=(0, 1920))
        K.expr(c, ex, W / 2, y + 10, 50, a)
        if k == 0:
            pill(c, "o qⁿ está aqui dentro", 1560, y + 50, AMBER, size=20, a=a, anchor="right", bounds=(0, 1920))


# ======================================================================
# concreto — o chocolate
# ======================================================================

def b_chocolate(c, t, C, B):
    head_seq(c, t, C, [("04", "SOMAR INFINITAS COISAS", "E NÃO DAR INFINITO?", BLUE),
                       ("05", "DEFINIÇÕES", "SOMA INFINITA · SOMA PARCIAL · LIMITE", BLUE)])
    card(c, *CARD_R)
    if t < C["05"]:
        aa = ep(t, C["04.a"], 0.5)
        n = 0.0
        if t > C["04.a"] + 1.2:
            n = clamp((t - C["04.a"] - 1.2) / 0.8)
        if t > C["04.b"]:
            n = 1 + clamp((t - C["04.b"] - 0.3) / 0.8)
        if t > C["04.c"]:
            n = 2 + 3 * clamp((t - C["04.c"]) / 3.5)
        chocolate(c, 360, 300, 1200, 260, n, aa)
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            for k, s in enumerate(("1/2", "3/4", "7/8")):
                ak = ep(t, C["04.c"] + k * 0.9, 0.4)
                K.expr(c, s, 700 + k * 260, 680, 64, ak)
            text_mid(c, "…  →  1", 1430, 680, 54, "black", GREEN, ep(t, C["04.c"] + 2.8, 0.4))
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            regra(c, "nunca passa do inteiro · chega tão perto quanto quiser", W / 2, 800, ad, 32, GREEN)
        return
    defs = [("05.a", "SOMA INFINITA", "somar os termos da PG sem parar nunca"),
            ("05.b", "SOMA PARCIAL", "a soma dos primeiros pedaços: 1/2, 3/4, 7/8…"),
            ("05.c", "CONVERGE · LIMITE", "as somas parciais chegam cada vez mais perto de um número")]
    for k, (cue, tit, sub) in enumerate(defs):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 180 + d
        rrect(c, 260, y - 70, 1400, 140, 22, mix("#FFFFFF", BLUE, 0.10), a)
        text(c, tit, 300, y - 10, 34, "black", BLUE, a, align="left")
        ftext(c, sub, 300, y + 40, 28, "bold", INK2, a, align="left")


# ======================================================================
# bloco a/b — o freio e a fórmula
# ======================================================================

def b_freio(c, t, C, B):
    head_seq(c, t, C, [("06", "POR QUE A SOMA PARA?", "O FREIO DA RAZÃO", BLUE),
                       ("07", "A FÓRMULA", "SOMA INFINITA", PURPLE)])
    card(c, *CARD_R)
    if t < C["07"]:
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            chip(c, "q = 1/2", W / 2, 250, PURPLE, aa, 40)
        ab = ep(t, C["06.b"], 0.5)
        vals = ["1/2", "1/4", "1/8", "1/16", "…", "1/1024"]
        for k, s in enumerate(vals):
            ak = ab * ep(t, C["06.b"] + k * 0.5, 0.3)
            if ak <= 0:
                continue
            x = 380 + k * 230
            hh = 220 * (0.5 ** k) if s != "…" else 0
            if s == "1/1024":
                hh = 3
            if hh:
                rrect(c, x - 50, 640 - hh, 100, hh, 8, BLUE, ak)
            K.expr(c, s, x, 690, 40, ak)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            linha(c, [("qⁿ → ", INK), ("perto de zero", GREEN)], W / 2, 330, 50, acc)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            regra(c, "razão entre −1 e 1   ·   |q| < 1", W / 2, 790, ad, 38)
        return
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        K.expr(c, "Sₙ = a₁·(q^n-1)/(q-1)", W / 2, 280, 56, aa)
        strike(c, 980, 268, 1090, 268, ep(t, C["07.a"] + 1.6, 0.4), RED, 1)
        pill(c, "qⁿ vira zero", 1180, 200, RED, size=24, a=ep(t, C["07.a"] + 1.6, 0.4), anchor="center", bounds=(0, 1920))
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        K.boxed(c, 560, 390, 800, 220, PURPLE, ab, 0.08)
        K.expr(c, "S∞ = a₁/{1-q}", W / 2, 500, 90, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        pill(c, "é o LIMITE das somas parciais: elas se aproximam, sem nunca passar", W / 2, 720, BLUE, size=28, a=acc,
             anchor="center")


# ======================================================================
# bloco c — o quadrado pintado · atalho do k
# ======================================================================

def b_quadrado(c, t, C, B):
    head(c, t, B["start"], "A FÓRMULA FUNCIONA?", "O QUADRADO DE ÁREA 1", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    n = 0
    if t > C["08.a"]:
        n = 1 + 2 * clamp((t - C["08.a"] - 0.8) / 2.0)
    if t > C["08.b"]:
        n = 3 + 7 * clamp((t - C["08.b"]) / 5.0)
    quadrado(c, 240, 230, 560, n, aa)
    contador(c, 1050, 330, n, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        pill(c, "nunca passa de 1", 1050, 450, AMBER, size=26, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["08.c"], 0.5)
    freio(c, "1/2", 1290, 560, acc, 30)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        K.expr(c, "S∞ = 1/2 ÷ (1-{1/2}) = 1/2 ÷ 1/2 = 1", 1290, 720, 50, ad)


def b_atalho_k(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DIVIDIR POR 1 − q SEM SOFRER", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        K.atalho(c, 260, 210, 1400, 170, "ATALHO", [("m", "1 - q = 1/k   →   S∞ = k · a₁")], aa, 50)
    linhas = [("09.b", "q = 3/4", "1 - 3/4 = 1/4", "S = 4 · a₁"), ("09.c", "q = 1/2", "1 - 1/2 = 1/2", "S = 2 · a₁"),
              ("09.c", "q = 2/3", "1 - 2/3 = 1/3", "S = 3 · a₁")]
    for k, (cue, q, um, res) in enumerate(linhas):
        ak = ep(t, C[cue] + (1.8 if k == 2 else 0), 0.5)
        if ak <= 0:
            continue
        y = 470 + k * 130
        rrect(c, 360, y - 55, 1200, 110, 20, "#FFFFFF", ak, shadow=True)
        K.expr(c, q, 520, y, 44, ak)
        K.expr(c, um, 900, y, 44, ak)
        linha(c, [(res, GREEN)], 1350, y, 44, ak)


# ======================================================================
# bloco d — sem freio
# ======================================================================

def b_semfreio(c, t, C, B):
    head(c, t, B["start"], "E SE q = 2?", "SEM FREIO", RED)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    for k, v in enumerate((1, 2, 4, 8, 16)):
        ak = aa * ep(t, C["10.a"] + k * 0.5, 0.3)
        if ak <= 0:
            continue
        x = 340 + k * 150
        hh = v * 24
        rrect(c, x - 45, 600 - hh, 90, hh, 8, RED, ak * 0.85)
        text(c, str(v), x, 640, 30, "black", INK, ak)
    if aa > 0:
        pill(c, "a soma não para de crescer", 640, 230, RED, size=28, a=ep(t, C["10.a"] + 2.6, 0.4), anchor="center")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 1100, 300, 560, 220, 24, "#FFFFFF", ab, shadow=True)
        K.expr(c, "1/{1-2} = -1", 1380, 410, 64, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        selo(c, 1380, 600, acc, "ABSURDO", RED, -5, 50)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        regra(c, "a fórmula só funciona COM FREIO: razão entre −1 e 1", W / 2, 790, ad, 34)


# ======================================================================
# bloco e — a dízima como PG
# ======================================================================

def b_dizima(c, t, C, B):
    head_seq(c, t, C, [("11", "DÍZIMA PERIÓDICA", "É UMA PG", BLUE), ("12", "TEM FREIO?", "A FRAÇÃO E OS NOVES", PURPLE)])
    card(c, *CARD_R)
    if t < C["12"]:
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 210, 1400, 110, 22, mix("#FFFFFF", BLUE, 0.10), aa)
            ftext(c, "DÍZIMA PERIÓDICA: casas que se repetem · PERÍODO: o bloco que se repete", W / 2, 278, 30, "black",
                  BLUE, aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            linha(c, [("0,", INK), ("27", PURPLE), ("27", PURPLE), ("27", PURPLE), ("…", INK)], W / 2, 410, 90, ab)
            pill(c, "período = 27", W / 2, 490, PURPLE, size=26, a=ab, anchor="center")
        acc = ep(t, C["11.c"], 0.5)
        pecas = ["0,27", "0,0027", "0,000027", "…"]
        for k, s in enumerate(pecas):
            ak = acc * ep(t, C["11.c"] + k * 0.8, 0.3)
            if ak <= 0:
                continue
            x = 420 + k * 330
            if s != "…":
                chip(c, s, x, 610, BLUE, ak, 38)
            else:
                text_mid(c, "…", x, 610, 50, "black", INK2, ak)
            if k:
                text_mid(c, "+", x - 165, 610, 44, "black", INK2, ak)
        ad = ep(t, C["11.c"] + 4.5, 0.5)
        if ad > 0:
            linha(c, [("a₁ = 0,27", BLUE), ("     ", INK), ("q = 0,01", PURPLE)], W / 2, 750, 46, ad)
        return
    aa = ep(t, C["12.a"], 0.5)
    freio(c, "0,01", W / 2, 250, aa, 30)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        K.expr(c, "S∞ = 0,27/{1-0,01} = 0,27/0,99 = 27/99 = 3/11", W / 2, 420, 54, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 540, 1200, 130, "ATALHO", ["os NOVES da regra prática são o 1 − q (0,99 → 99)"], acc, 36)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "a regra dos noves da série de Frações tem ESTA explicação", W / 2, 760, INK2, size=28, a=ad,
             anchor="center")


# ======================================================================
# bloco f — a bola (exemplo nosso: 9 m e 2/3) · atalho da bola
# ======================================================================

def b_bola(c, t, C, B):
    head(c, t, B["start"], "A BOLA QUE QUICA", "PARA SEMPRE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    n = 11 * clamp((t - C["13.b"]) / 5.0)
    bola_trajeto(c, 240, 800, 52, 9, 2 / 3, n, aa)
    if aa > 0:
        pill(c, "solta de 9 m · sobe 2/3 da anterior", 240, 222, INK2, size=26, a=aa, bounds=(0, 1920))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        K.atalho(c, 1060, 200, 600, 120, "A REGRA DA BOLA", ["cai UMA vez de 9 m · o resto, DUAS"], ab, 28)
    ud = ep(t, C["13.c"], 1.6)
    us = ep(t, C["13.d"], 1.6)
    ut = ep(t, C["13.d"] + 4.0, 1.0)
    barras_bola(c, 1050, 640, 6, 27, 18, ud, us, ut, ud, lab=False)
    if ud > 0:
        linha(c, [("descidas: 9 ÷ 1/3 = ", BLUE), ("27 m", BLUE)], 1360, 735, 30, ud)
    if us > 0:
        linha(c, [("subidas: 6 ÷ 1/3 = ", GREEN), ("18 m", GREEN)], 1360, 785, 30, us)
    if ut > 0:
        linha(c, [("9 + 2 · 18 = ", INK), ("45 m", GREEN)], 1500, 500, 38, ut)


def b_bola_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "A BOLA EM UMA CONTA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("total = queda inicial + ", INK), ("2 × subidas", GREEN)], W / 2, 260, 46, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        K.atalho(c, 360, 340, 1200, 200, "ATALHO DA BOLA", [("m", "total = h · {1+q}/{1-q}")], ab, 60)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 600, 1200, 180, 24, "#FFFFFF", acc, shadow=True)
        K.expr(c, "9 · 5/3 ÷ 1/3 = 9 · 5 = 45", W / 2, 690, 54, acc)
        check_icon(c, 1500, 690, 22, ep(t, C["14.c"] + 3.0, 0.4), GREEN)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "FREIO PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 130, 24, "#FFFFFF", aa, shadow=True)
        K.expr(c, "9 + 3 + 1 + 1/3 + … = ?", W / 2, 275, 60, aa)
    if t < C["16"]:
        pause_timer(c, t, C["15.end"] - 1.9, 960, 560)
        return
    ab = ep(t, C["16.a"], 0.5)
    if ab > 0:
        K.expr(c, "q = 3/9 = 1/3", 600, 450, 54, ab)
        freio(c, "1/3", 600, 560, ep(t, C["16.a"] + 2.4, 0.4), 26)
    acc = ep(t, C["16.b"], 0.5)
    if acc > 0:
        K.expr(c, "1 - 1/3 = 2/3", 1320, 450, 54, acc)
    ad = ep(t, C["16.c"], 0.5)
    if ad > 0:
        rrect(c, 460, 640, 1000, 170, 24, mix("#FFFFFF", GREEN, 0.12), ad)
        K.expr(c, "9/{2/3} = 9 · 3/2 = 27/2 = 13,5", W / 2, 725, 54, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Com razão entre −1 e 1, a soma infinita é a₁ sobre (1 − q).",
          "Razão fora disso: a soma não para de crescer.",
          "Bola: a primeira queda uma vez; o resto, duas."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1380, 56)


ERROS = [("Dividir pela razão: 9 ÷ 1/3 = 27", "o q é o número que aparece na PG",
          "o denominador é 1 − q: 9 ÷ 2/3 = 13,5"),
         ("Somar PG infinita de razão 2: 3 + 6 + 12 + … “= −3”", "a fórmula aceita qualquer número",
          "ela só vale com freio: razão entre −1 e 1"),
         ("Bola: só h ÷ (1 − q) = 9 ÷ 1/3 = 27 m", "é a fórmula da soma infinita",
          "isso é só a descida; com as subidas: 9 + 2 · 18 = 45 m"),
         ("0,2727… = 27/100", "são duas casas depois da vírgula",
          "27/100 para no 7; a dízima continua: 27/99 = 3/11")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20", "21"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _questao(c, t, C, sid_q, sid_r, sid_x, alts, okL, xs, txt, pausa=True, size=27):
    a0 = ep(t, C[f"{sid_q}.a"], 0.4)
    yend = _enunciado(c, [(txt, INK)], a0, 236, size)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[sid_r], 0.3)),
         align="left")
    cues_in = {L: C[f"{sid_q}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in xs}
    K.alternativas(c, t, C, alts, 1000, 260, 680, 38, C[f"{sid_r}.ok"], okL, cues_in, cues_x, gap=34)
    if t < C[sid_r]:
        if pausa:
            pause_timer(c, t, C[f"{sid_q}.end"] - 1.9, 540, yend + 120)
        return None
    y0 = 236 - 30
    _painel(c, y0, ep(t, C[sid_r], 0.4))
    return y0


ALTS8 = [("A", "12 cm²", "só a 1ª etapa", RED), ("B", "15,75 cm²", "só três etapas", RED), ("C", "16 cm²", "", GREEN),
         ("D", "24 cm²", "razão 1/2", RED), ("E", "48 cm²", "dividiu pela razão", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · EU FAÇO", "O LOGOTIPO FRACTAL", BLUE)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "22", "23", "24", ALTS8, "C", "ABDE",
                  "Um designer cria um logotipo em etapas. Na primeira etapa desenha um triângulo de 12 cm² de área. Em "
                  "cada etapa seguinte, acrescenta pequenos triângulos cuja área total é 1/4 da área acrescentada na "
                  "etapa anterior, sem sobreposição. Se o processo for repetido indefinidamente, a área do logotipo se "
                  "aproxima de", size=25)
    if y0 is None:
        return
    aa = ep(t, C["23.a"], 0.4)
    if aa > 0:
        linha(c, [("“indefinidamente” → ", INK), ("SOMA INFINITA", PURPLE)], 540, y0 + 60, 30, aa)
    ab = ep(t, C["23.b"], 0.4)
    if ab > 0:
        linha(c, [("12 + 3 + 0,75 + …", BLUE)], 540, y0 + 140, 36, ab)
        freio(c, "1/4", 540, y0 + 220, ep(t, C["23.b"] + 2.4, 0.4), 24)
    acc = ep(t, C["23.c"], 0.4)
    if acc > 0:
        K.expr(c, "12/{3/4} = 12 · 4/3 = 16", 540, y0 + 340, 44, acc)
        linha(c, [("16 cm²", GREEN)], 540, y0 + 450, 54, ep(t, C["23.c"] + 3.0, 0.4))


ALTS6 = [("A", "=27/100", "só o 1º termo", RED), ("B", "=3/11", "", GREEN), ("C", "=27/90", "1 − q = 0,9", RED),
         ("D", "=1/37", "três noves: 27/999", RED), ("E", "=2/7", "aproximação: 0,2857…", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · NÓS FAZEMOS", "A DÍZIMA COMO SOMA INFINITA", PURPLE)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "25", "26", "27", ALTS6, "B", "ACDE",
                  "Um programa exibe o número 0,272727…, em que o bloco “27” se repete indefinidamente. Escrevendo esse "
                  "número como 0,27 + 0,0027 + 0,000027 + … e somando os infinitos termos, obtém-se a fração")
    if y0 is None:
        return
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        linha(c, [("a₁ = 0,27", BLUE), ("   ·   ", INK2), ("q = 0,01", PURPLE)], 540, y0 + 70, 36, aa)
        freio(c, "0,01", 540, y0 + 150, ep(t, C["26.a"] + 2.4, 0.4), 24)
    ab = ep(t, C["26.b"], 0.4)
    if ab > 0:
        K.expr(c, "0,27/0,99 = 27/99 = 3/11", 540, y0 + 280, 46, ab)
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        rrect(c, 230, y0 + 380, 620, 100, 18, mix("#FFFFFF", GREEN, 0.12), acc)
        linha(c, [("conferência: 3 ÷ 11 = 0,2727…  ✓", GREEN)], 540, y0 + 430, 30, acc)


ALTS3 = [("A", "24 m", "só as subidas", RED), ("B", "32 m", "só as descidas", RED),
         ("C", "48 m", "esqueceu a queda de 8 m", RED), ("D", "56 m", "", GREEN), ("E", "64 m", "dobrou tudo", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "A BOLA DE 8 METROS", GREEN)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "28", "29", "30", ALTS3, "D", "ABCE",
                  "Uma bola é solta de uma altura de 8 m e, a cada vez que toca o chão, sobe verticalmente até 3/4 da "
                  "altura de que caiu. Supondo que esse padrão se mantenha indefinidamente, a distância vertical total "
                  "percorrida pela bola, em metros, até parar, é")
    if y0 is None:
        return
    aa = ep(t, C["29.a"], 0.4)
    freio(c, "3/4", 540, y0 + 55, aa, 24)
    if aa > 0:
        pill(c, "1 − 3/4 = 1/4  →  4 vezes o 1º termo", 540, y0 + 120, GREEN, size=22, a=ep(t, C["29.a"] + 2.0, 0.4),
             anchor="center", bounds=(0, 1920))
    ud = ep(t, C["29.b"], 1.4)
    us = ep(t, C["29.c"], 1.4)
    ut = ep(t, C["29.d"], 1.0)
    barras_bola(c, 330, y0 + 430, 5, 32, 24, ud, us, ut, ud)
    if ut > 0:
        K.expr(c, "8 · 7/4 ÷ 1/4 = 8 · 7 = 56", 540, y0 + 560, 34, ep(t, C["29.d"] + 2.0, 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A PG DISFARÇADA", PURPLE)
    itens = [("JUROS COMPOSTOS", "× 1,05 × 1,05 …"), ("REMÉDIO", "cai à metade"), ("CARRO", "perde valor todo ano")]
    aa = ep(t, C["32.a"], 0.5)
    for k, (tit, sub) in enumerate(itens):
        ak = aa * ep(t, C["32.a"] + k * 0.8, 0.4)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 260, 460, 260, 26, "#FFFFFF", ak, shadow=True)
        text(c, tit, x, 350, 36, "black", PURPLE, ak)
        ftext(c, sub, x, 420, 28, "bold", INK2, ak)
        selo(c, x, 490, ak, "É PG?", AMBER, -4, 24)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        pill(c, "você já esbarrou na PG sem que ela dissesse o nome", W / 2, 620, INK2, size=28, a=ab, anchor="center")
    pill(c, "ep. 4 · a PG disfarçada", W / 2, 730, PURPLE, size=32, a=ep(t, C["32.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Você achava que infinitos termos podiam dar um número finito?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, chocolate=b_chocolate, freio=b_freio,
              quadrado=b_quadrado, atalho_k=b_atalho_k, semfreio=b_semfreio, dizima=b_dizima, bola=b_bola,
              bola_atalho=b_bola_atalho, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q8=b_q8, q6=b_q6, q3=b_q3,
              ponte=b_ponte, cta=b_cta)
