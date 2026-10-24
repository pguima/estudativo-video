"""Visual — Função Logarítmica, Episódio 4: decibéis, por que 80 + 80 não dá 160 (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: medidor() (o medidor de decibéis com visor e barra de 0 a 120), maquina() (máquina com ondas),
ondas() (arcos de som), balde() + copo() (o balde de intensidade com a etiqueta em dB), icones dos quatro lugares
(livro, carro, britadeira, engrenagem).
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
_s = importlib.util.spec_from_file_location("comum043", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.selo, K.pause_timer,
                                                         K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_logaritmica_ep4_decibeis.mp4"
CARD_R = K.CARD_R
METAL = "#5B6475"
AGUA = "#4FA3E0"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)]"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def mx(c, s, cx, cy, size, a, col=None, align="center"):
    """expressão de uma cor só (potências, frações)"""
    n = len(s.split())
    return K.expr(c, s, cx, cy, size, a, cores={i: col or INK for i in range(n)}, align=align)


def cartao(c, x, y, w, h, a, col=None):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if col else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


def arco(c, cx, cy, r, a0, sweep, col, a, w):
    if a <= 0:
        return
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), a0, sweep)
    c.drawPath(p, paint(col, a, stroke=w, cap_round=True))


def ondas(c, cx, cy, s, a, col=None, n=3, lado=1):
    """arcos de som saindo de (cx, cy) para a direita (lado=1) ou esquerda (lado=-1)"""
    col = col or BLUE
    for k in range(n):
        arco(c, cx, cy, s * (0.35 + 0.3 * k), -40 if lado > 0 else 140, 80, col, a * (1 - 0.18 * k), max(3, s * 0.07))


def medidor(c, cx, cy, s, val, a, col=None, rotulo=True):
    """medidor de decibéis: corpo escuro, visor com o valor e barra de 0 a 120 embaixo"""
    if a <= 0:
        return
    col = col or GREEN
    w, h = 1.5 * s, 1.15 * s
    rrect(c, cx - w / 2, cy - h / 2, w, h, 0.14 * s, "#2B2F3A", a, shadow=True)
    rrect(c, cx - w / 2 + 0.1 * s, cy - h / 2 + 0.1 * s, w - 0.2 * s, 0.55 * s, 0.08 * s, "#10141C", a)
    v = f"{round(val)}"
    text_mid(c, v, cx + 0.12 * s, cy - h / 2 + 0.38 * s, 0.42 * s, "black", col, a, align="right")
    text_mid(c, "dB", cx + 0.2 * s, cy - h / 2 + 0.42 * s, 0.2 * s, "black", col, a, align="left")
    bx, by, bw = cx - w / 2 + 0.12 * s, cy + 0.22 * s, w - 0.24 * s
    rrect(c, bx, by, bw, 0.14 * s, 0.07 * s, "#3A4050", a)
    f = clamp(val / 120)
    if f > 0:
        rrect(c, bx, by, bw * f, 0.14 * s, 0.07 * s, AMBER if val >= 85 else col, a)
    if rotulo:
        text(c, "0", bx, by + 0.34 * s, 0.11 * s, "bold", "#C9CDD6", a, align="left")
        text(c, "120", bx + bw, by + 0.34 * s, 0.11 * s, "bold", "#C9CDD6", a, align="right")


def maquina(c, cx, cy, s, a, ligada=1.0, col=None):
    """máquina estilizada (caixa com engrenagem) e ondas de som quando ligada"""
    if a <= 0:
        return
    col = col or METAL
    rrect(c, cx - 0.5 * s, cy - 0.4 * s, s, 0.8 * s, 0.1 * s, col, a, shadow=True)
    rrect(c, cx - 0.42 * s, cy + 0.4 * s, 0.84 * s, 0.1 * s, 0.04 * s, mix(col, "#000000", 0.3), a)
    engrenagem(c, cx - 0.12 * s, cy, 0.24 * s, a, "#FFFFFF")
    c.drawCircle(cx + 0.3 * s, cy - 0.2 * s, 0.06 * s, paint(GREEN if ligada > 0.5 else LIGHT, a))
    if ligada > 0:
        ondas(c, cx + 0.55 * s, cy - 0.05 * s, 0.6 * s, a * ligada, AMBER)


def engrenagem(c, cx, cy, r, a, col):
    if a <= 0:
        return
    for k in range(8):
        ang = math.radians(k * 45)
        x, y = cx + math.cos(ang) * r * 1.05, cy + math.sin(ang) * r * 1.05
        c.drawCircle(x, y, r * 0.24, paint(col, a))
    c.drawCircle(cx, cy, r * 0.88, paint(col, a))
    c.drawCircle(cx, cy, r * 0.32, paint(METAL, a))


def balde(c, cx, cy, s, nivel, a, etiqueta=None, col_et=None):
    """balde de intensidade (trapézio), água até `nivel` (0..1) e a etiqueta em dB pendurada"""
    if a <= 0:
        return
    top, bot, h = 1.0 * s, 0.74 * s, 1.0 * s
    y0 = cy - h / 2
    p = skia.Path()
    p.moveTo(cx - top / 2, y0); p.lineTo(cx + top / 2, y0); p.lineTo(cx + bot / 2, y0 + h); p.lineTo(cx - bot / 2, y0 + h)
    p.close()
    c.drawPath(p, paint(mix("#FFFFFF", METAL, 0.12), a))
    if nivel > 0:
        yl = y0 + h * (1 - clamp(nivel))
        half = lambda yy: bot / 2 + (top / 2 - bot / 2) * (1 - (yy - y0) / h)
        q = skia.Path()
        q.moveTo(cx - half(yl), yl); q.lineTo(cx + half(yl), yl); q.lineTo(cx + bot / 2, y0 + h)
        q.lineTo(cx - bot / 2, y0 + h); q.close()
        c.drawPath(q, paint(AGUA, a * 0.85))
    c.drawPath(p, paint(METAL, a, stroke=max(4, 0.03 * s)))
    arco(c, cx, y0, top / 2, 180, 180, METAL, a, max(4, 0.025 * s))
    if etiqueta:
        col_et = col_et or PURPLE
        ex, ey = cx + top / 2 + 0.08 * s, y0 + 0.28 * s
        line(c, cx + top / 2 - 0.02 * s, y0 + 0.08 * s, ex + 0.1 * s, ey - 0.02 * s, INK2, a, 3)
        w = text_w(etiqueta, "black", 0.2 * s) + 0.24 * s
        rrect(c, ex, ey, w, 0.34 * s, 0.07 * s, "#FFFFFF", a, shadow=True)
        rrect(c, ex, ey, 0.06 * s, 0.34 * s, 0.03 * s, col_et, a)
        text_mid(c, etiqueta, ex + 0.06 * s + (w - 0.06 * s) / 2, ey + 0.17 * s, 0.2 * s, "black", col_et, a)


def copo(c, cx, cy, s, a, cheio=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 0.3 * s, cy - 0.4 * s); p.lineTo(cx + 0.3 * s, cy - 0.4 * s); p.lineTo(cx + 0.22 * s, cy + 0.4 * s)
    p.lineTo(cx - 0.22 * s, cy + 0.4 * s); p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    if cheio > 0:
        q = skia.Path()
        yl = cy + 0.4 * s - 0.65 * s * cheio
        q.moveTo(cx - 0.22 * s - 0.08 * s * cheio * 0.9, yl); q.lineTo(cx + 0.22 * s + 0.08 * s * cheio * 0.9, yl)
        q.lineTo(cx + 0.22 * s, cy + 0.4 * s); q.lineTo(cx - 0.22 * s, cy + 0.4 * s); q.close()
        c.drawPath(q, paint(AGUA, a * 0.85))
    c.drawPath(p, paint(METAL, a, stroke=max(3, 0.05 * s)))


# ---------------- ícones dos quatro lugares ----------------

def ic_livro(c, cx, cy, s, a, col):
    rrect(c, cx - 0.42 * s, cy - 0.32 * s, 0.4 * s, 0.64 * s, 0.05 * s, col, a)
    rrect(c, cx + 0.02 * s, cy - 0.32 * s, 0.4 * s, 0.64 * s, 0.05 * s, mix(col, "#FFFFFF", 0.25), a)
    for k in range(3):
        y = cy - 0.15 * s + k * 0.14 * s
        line(c, cx + 0.1 * s, y, cx + 0.34 * s, y, "#FFFFFF", a, 3)


def ic_carro(c, cx, cy, s, a, col):
    rrect(c, cx - 0.5 * s, cy - 0.08 * s, s, 0.3 * s, 0.08 * s, col, a)
    rrect(c, cx - 0.26 * s, cy - 0.3 * s, 0.52 * s, 0.26 * s, 0.08 * s, col, a)
    for x in (-0.28, 0.28):
        c.drawCircle(cx + x * s, cy + 0.24 * s, 0.11 * s, paint(INK, a))


def ic_britadeira(c, cx, cy, s, a, col):
    rrect(c, cx - 0.42 * s, cy - 0.46 * s, 0.84 * s, 0.14 * s, 0.06 * s, INK, a)
    rrect(c, cx - 0.16 * s, cy - 0.34 * s, 0.32 * s, 0.46 * s, 0.06 * s, col, a)
    rrect(c, cx - 0.05 * s, cy + 0.12 * s, 0.1 * s, 0.3 * s, 0.03 * s, METAL, a)
    for k in (-1, 1):
        line(c, cx + k * 0.12 * s, cy + 0.45 * s, cx + k * 0.3 * s, cy + 0.38 * s, AMBER, a, 4)


def ic_oficina(c, cx, cy, s, a, col):
    engrenagem(c, cx - 0.12 * s, cy + 0.06 * s, 0.26 * s, a, col)
    engrenagem(c, cx + 0.26 * s, cy - 0.22 * s, 0.16 * s, a, mix(col, "#FFFFFF", 0.3))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO LOGARÍTMICA · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    acc = ep(t, C["01.c"], 0.5)
    ad = ep(t, C["01.d"], 0.5)
    # medidor: 80 → (160?) → 83 → 90
    val = 80.0
    if acc > 0:
        val = 80 + 3.01 * ease_io(clamp((t - C["01.c"]) / 1.2))
    if ad > 0:
        u = ease_io(clamp((t - C["01.d"] - 0.6) / 2.4))
        val = 83.01 + (90 - 83.01) * u
    medidor(c, 1420, 430, 300, val, aa)
    if ad <= 0:
        maquina(c, 520, 470, 260, aa)
        maquina(c, 900, 470, 260, ab)
    else:
        for k in range(10):
            ak = ad * ep(t, C["01.d"] + 0.22 * k, 0.3)
            maquina(c, 330 + (k % 5) * 170, 360 + (k // 5) * 220, 120, ak)
    if ab > 0:
        x = 1420
        sz = 70
        text_mid(c, "160 dB?", x, 690, sz, "black", AMBER if acc <= 0 else RED, ab)
        if acc > 0:
            w = text_w("160 dB?", "black", sz)
            strike(c, x - w / 2 - 10, 690, x + w / 2 + 10, 690, acc, RED, acc)
    if ad > 0:
        pill(c, "10 máquinas → 90 dB", 1420, 780, GREEN, size=30, a=ep(t, C["01.d"] + 2.6, 0.4), anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO LOGARÍTMICA · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02.t"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de FUNÇÃO LOGARÍTMICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "CALCULAR", "decibéis", PURPLE), ("02.b", "COMPARAR", "dois sons em quantas vezes", BLUE),
             ("02.c", "SOMAR FONTES", "sem cair na pegadinha", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 220, 330, 440, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 220, 330, 440, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 26, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "série de Logaritmos", 300, y - 75, BLUE, size=22, a=a)
        mx(c, "log 10^n = n", 640, y + 4, 54, a, INK)
        mx(c, "10 · log 2 ≈ 3", 1200, y + 4, 54, ep(t, C["03.a"] + 2.6, 0.4), PURPLE)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódio 2", 300, y - 75, PURPLE, size=22, a=a)
        linha(c, [("razão = ", INK)], 760, y + 4, 50, a)
        mx(c, "10^{diferença}", 1060, y + 4, 56, a, PURPLE)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "série de Notação científica", 300, y - 75, GREEN, size=22, a=a)
        mx(c, "10^a/10^b = 10^{a-b}", 960, y + 4, 52, a, INK)


# ======================================================================
# concreto e definições
# ======================================================================

LUGARES = [("04.a", "biblioteca", ic_livro, BLUE), ("04.b", "avenida", ic_carro, PURPLE),
           ("04.c", "britadeira", ic_britadeira, AMBER), ("04.d", "oficina", ic_oficina, METAL)]


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "QUATRO LUGARES", "DO MAIS BAIXO AO MAIS ALTO", BLUE)
    card(c, *CARD_R)
    for k, (cue, nome, fn, col) in enumerate(LUGARES):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        x = 400 + k * 370
        cartao(c, x - 160, 240 + d, 320, 330, ak)
        fn(c, x, 360 + d, 140, ak, col)
        text(c, nome, x, 520 + d, 34, "black", INK, ak)
        # barras de "quão alto"
        for j in range(4):
            on_ = j <= k
            rrect(c, x - 70 + j * 38, 640 - 20 * (j + 1) + d, 26, 20 * (j + 1), 6, AMBER if on_ else LINE, ak)
    ae = ep(t, C["04.e"], 0.5)
    defin(c, "FONTE SONORA", "tudo o que produz som", 300, 720, 1320, ae, BLUE, 32)


def b_definicoes(c, t, C, B):
    head(c, t, B["start"], "TRÊS NOMES", "ANTES DA FÓRMULA", BLUE)
    card(c, *CARD_R)
    aa, d = rise(t, C["05.a"])
    defin(c, "INTENSIDADE SONORA", "a força do som que chega a cada pedaço do espaço", 240, 250 + d, 1440, aa, BLUE, 30)
    if aa > 0:
        pill(c, "unidade: W/m²  (watt por metro quadrado)", 960, 380 + d, BLUE, size=26,
             a=ep(t, C["05.a"] + 3.0, 0.4), anchor="center")
    ab, d = rise(t, C["05.b"])
    defin(c, "LIMIAR DA AUDIÇÃO", "o som mais fraco que se ouve", 240, 470 + d, 1440, ab, BLUE, 30)
    if ab > 0:
        cartao(c, 1180, 570 + d, 500, 90, ab)
        mx(c, "I₀ = 10^{-12}", 1360, 615 + d, 44, ab, BLUE)
        text(c, "W/m²", 1560, 628 + d, 30, "bold", INK2, ab, align="left")
    ac, d = rise(t, C["05.c"])
    defin(c, "LIMIAR DA DOR", "o som tão forte que dói", 240, 700 + d, 1440, ac, RED, 30)


# ======================================================================
# bloco a — a fórmula
# ======================================================================

def b_formula(c, t, C, B):
    head(c, t, B["start"], "NÍVEL SONORO", "A FÓRMULA DO DECIBEL", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 200, 1200, 170, 28, mix("#FFFFFF", PURPLE, 0.10), aa, shadow=True)
        mx(c, "β = 10 · log (I/I₀)", 960, 285, 74, aa, PURPLE)
        al = ep(t, C["06.a"] + 2.2, 0.4)
        pill(c, "nível sonoro, em dB", 560, 410, PURPLE, size=22, a=al, anchor="center")
        pill(c, "intensidade, em W/m²", 1300, 410, BLUE, size=22, a=al, anchor="center")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        mx(c, "I = 10^{-5}", 560, 520, 50, ab, INK)
        text(c, "W/m²", 700, 534, 28, "bold", INK2, ab, align="left")
        ab2 = ep(t, C["06.b"] + 2.4, 0.4)
        mx(c, "I/I₀ = 10^{-5}/10^{-12} = 10^7", 1260, 520, 48, ab2, INK)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 420, 660, 1080, 120, 24, mix("#FFFFFF", GREEN, 0.14), acc)
        mx(c, "β = 10 · log 10^7 = 10 · 7 = 70", 900, 720, 52, acc, INK)
        text(c, "dB", 1370, 738, 46, "black", GREEN, acc, align="left")


def b_atalho_db(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONTE OS DEGRAUS ACIMA DO LIMIAR", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["07.t"], 0.4)
    if a0 > 0:
        K.boxed(c, 220, 200, 1480, 620, GREEN, a0, 0.08)
        text(c, "ATALHO · DECIBÉIS SEM CONTA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["07.a"], 0.5)
    xs = [380 + k * 165 for k in range(8)]
    if aa > 0:
        line(c, xs[0] - 40, 520, xs[-1] + 40, 520, INK2, aa, 4)
        for k, x in enumerate(xs):
            line(c, x, 505, x, 535, INK2, aa, 4)
            mx(c, f"10^{{{-12 + k}}}", x, 590, 36, aa, BLUE if k in (0, 7) else INK)
        pill(c, "limiar", xs[0], 650, BLUE, size=22, a=aa, anchor="center")
        pill(c, "o som", xs[-1], 650, PURPLE, size=22, a=aa, anchor="center")
    ab = ep(t, C["07.b"], 0.3)
    if ab > 0:
        n = 0
        for k in range(7):
            ak = ep(t, C["07.b"] + 0.35 * k, 0.3)
            if ak <= 0:
                continue
            n = k + 1
            arco(c, (xs[k] + xs[k + 1]) / 2, 505, 82, 200, 140, GREEN, ak, 5)
        text_mid(c, f"{n} degraus", 960, 380, 50, "black", GREEN, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 700, 700, 520, 90, 22, GREEN, acc)
        text_mid(c, "7 → 70 dB", 960, 745, 50, "black", "#FFFFFF", acc)


# ======================================================================
# bloco b — de 0 a 120
# ======================================================================

def b_escala(c, t, C, B):
    head(c, t, B["start"], "POR QUE O LOG?", "UM TRILHÃO CABE EM 120", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha(c, [("intensidade: ", INK2), ("× 1 trilhão", RED)], 960, 260, 56, aa)
        arrow(c, 420, 330, 1500, 330, RED, aa, 6, 20, progress=ep(t, C["08.a"] + 0.6, 1.4))
    ab = ep(t, C["08.b"], 0.5)
    x0, x1, y = 420, 1500, 520
    if ab > 0:
        rrect(c, x0, y - 22, x1 - x0, 44, 22, LINE, ab)
        rrect(c, x0, y - 22, (x1 - x0) * ep(t, C["08.b"] + 0.3, 1.6), 44, 22, mix(GREEN, AMBER, 0.3), ab)
        for v in (0, 20, 40, 60, 80, 100, 120):
            x = x0 + (x1 - x0) * v / 120
            text(c, str(v), x, y + 70, 28, "bold", INK2, ab)
        pill(c, "limiar da audição", x0, y - 70, BLUE, size=22, a=ab, anchor="center")
        pill(c, "limiar da dor", x1, y - 70, RED, size=22, a=ab, anchor="center")
        text(c, "dB", x1 + 70, y + 12, 32, "black", INK2, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        x = x0 + (x1 - x0) * 85 / 120
        line(c, x, y - 40, x, y + 100, AMBER, acc, 5)
        rrect(c, x - 270, 660, 540, 120, 22, mix("#FFFFFF", AMBER, 0.18), acc, shadow=True)
        text(c, "85 dB", x, 712, 46, "black", AMBER, acc)
        text(c, "limite para 8 h sem proteção", x, 758, 26, "bold", INK2, acc)


# ======================================================================
# bloco c — a tabela
# ======================================================================

TAB = [("09.a", "+10 dB", "× 10"), ("09.b", "+20 dB", "× 100"), ("09.c", "+40 dB", "× 10 000")]


def b_tabela(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head(c, t, B["start"] if sid == "09" else C["10"], "UM ZERO A MAIS", "CADA 10 dB", PURPLE)
    card(c, *CARD_R)
    # tabela à esquerda
    rows = TAB + [("10.b", "+3 dB", "≈ × 2")]
    for k, (cue, dv, fx) in enumerate(rows):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 270 + k * 130 + d
        col = GREEN if k == 3 else PURPLE
        rrect(c, 230, y - 50, 760, 100, 22, "#FFFFFF", ak, shadow=True)
        text_mid(c, dv, 380, y, 46, "black", INK, ak)
        arrow(c, 490, y, 600, y, col, ak, 5, 16)
        text_mid(c, "intensidade " + fx, 630, y, 32, "black", col, ak, align="left")
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            rrect(c, 1080, 280, 560, 120, 22, mix("#FFFFFF", PURPLE, 0.10), aa)
            mx(c, "10 · log 2 ≈ 3", 1360, 340, 50, aa, PURPLE)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            copo(c, 1220, 560, 120, acc); copo(c, 1380, 560, 120, acc * ep(t, C["10.c"] + 0.5, 0.3))
            pill(c, "dobrou o som → só +3 na etiqueta", 1360, 690, GREEN, size=26, a=acc, anchor="center")
        return
    # medidor subindo de 10 em 10 e a intensidade ganhando um zero
    a0 = ep(t, C["09.t"], 0.4)
    t0 = C["09.a"]
    t1 = C["09.d"] + 1.0
    u = clamp((t - t0) / max(1.0, t1 - t0))
    passo = min(4, int(u * 5))
    medidor(c, 1360, 330, 240, 40 + 10 * passo, a0)
    fator = 10 ** passo
    s_ = f"× {fator:,}".replace(",", " ")
    if a0 > 0:
        text_mid(c, "intensidade", 1360, 560, 30, "bold", INK2, a0)
        text_mid(c, s_, 1360, 640, 64, "black", BLUE, a0)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        selo(c, 1360, 800, ad, "CADA 10 dB = UM ZERO A MAIS", GREEN, -3, 30)


# ======================================================================
# bloco d — comparar
# ======================================================================

def b_comparar(c, t, C, B):
    head(c, t, B["start"], "QUANTAS VEZES?", "COMPARAR DOIS SONS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["11.t"], 0.4)
    medidor(c, 420, 340, 220, 90, a0)
    medidor(c, 820, 340, 220, 60, a0)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("diferença: ", INK2), ("90 − 60 = 30 dB", INK)], 620, 590, 42, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 1040, 240, 600, 140, 24, mix("#FFFFFF", PURPLE, 0.10), ab)
        text_mid(c, "30 ÷ 10 = 3", 1340, 310, 58, "black", PURPLE, ab)
        pill(c, "o 10 da fórmula come um zero", 1340, 430, AMBER, size=26, a=ep(t, C["11.b"] + 1.6, 0.4),
             anchor="center")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 1040, 520, 600, 180, 24, GREEN, acc)
        mx(c, "10^3 = 1 000", 1340, 590, 60, acc, "#FFFFFF")
        text_mid(c, "vezes mais intenso", 1340, 660, 32, "black", "#FFFFFF", acc)


def b_atalho_cmp(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O 10 COME UM ZERO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12.t"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 620, GREEN, a0, 0.08)
        text(c, "ATALHO · COMPARAR", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        text_mid(c, "diferença ÷ 10  →  depois eleve 10", 960, 350, 50, "black", INK, aa)
    for k, (dv, e) in enumerate((("30 dB", "3"), ("40 dB", "4"))):
        ak = ep(t, C["12.b"] + 1.4 * k, 0.5)
        if ak <= 0:
            continue
        y = 490 + k * 120
        text_mid(c, dv, 660, y, 50, "black", INK, ak)
        arrow(c, 800, y, 920, y, GREEN, ak, 5, 16)
        text_mid(c, e, 990, y, 54, "black", GREEN, ak)
        arrow(c, 1060, y, 1180, y, GREEN, ak, 5, 16)
        mx(c, f"10^{e}", 1290, y, 54, ak, GREEN)
        # o zero comido
        w = text_w(dv, "black", 50)
        zx = 660 - w / 2 + text_w(dv[0], "black", 50) + text_w("0", "black", 50) / 2
        strike(c, zx - 18, y + 14, zx + 18, y - 14, ak, RED, ak)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        selo(c, 960, 760, acc, "DIVIDA POR 10 ANTES DE ELEVAR", GREEN, -2, 34)


# ======================================================================
# bloco e — o balde
# ======================================================================

def _db(n):
    return 80 + 10 * math.log10(n) if n > 0 else 0


def b_somar(c, t, C, B):
    sid = which(t, C, ["13", "14"])
    head(c, t, B["start"] if sid == "13" else C["14"], "DECIBÉIS NÃO SE SOMAM",
         "O BALDE E OS COPOS" if sid == "13" else "DEZ COPOS", BLUE if sid == "13" else GREEN)
    card(c, *CARD_R)
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        n = 1 if t < C["13.d"] else 2
        cheg2 = ep(t, C["13.d"], 0.8)
        nivel = 0.25 + 0.25 * cheg2 if n == 2 else 0.25 * ep(t, C["13.a"] + 1.0, 0.8)
        et = "83 dB" if (n == 2 and cheg2 > 0.6) else "80 dB"
        balde(c, 520, 520, 380, nivel, aa, et if ep(t, C["13.c"], 0.4) > 0 else None, PURPLE)
        copo(c, 1220, 330, 110, aa)
        copo(c, 1380, 330, 110, ep(t, C["13.d"], 0.4))
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            pill(c, "intensidades SE SOMAM", 1300, 470, GREEN, size=30, a=ab, anchor="center")
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            pill(c, "o decibel é só a ETIQUETA", 1300, 560, PURPLE, size=30, a=acc, anchor="center")
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            text_mid(c, "160 dB", 1300, 700, 60, "black", RED, ad)
            w = text_w("160 dB", "black", 60)
            strike(c, 1300 - w / 2 - 10, 700, 1300 + w / 2 + 10, 700, ad, RED, ad)
            text_mid(c, "≈ 83 dB", 1300, 780, 54, "black", GREEN, ep(t, C["13.d"] + 1.4, 0.4))
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        pill(c, "+10 dB  =  intensidade × 10", 1350, 230, PURPLE, size=30, a=aa, anchor="center")
    tb = C["14.b"]
    tcc = C["14.c"] + 1.2
    n = 1
    for k in range(1, 10):
        if t >= tb + (tcc - tb) * k / 9:
            n = k + 1
    ab = ep(t, tb, 0.4)
    for k in range(10):
        ak = ep(t, tb + (tcc - tb) * k / 9, 0.3) if k > 0 else ep(t, C["14.t"], 0.4)
        copo(c, 1110 + (k % 5) * 120, 360 + (k // 5) * 150, 90, ak)
    nivel = 0.08 + 0.72 * (n - 1) / 9
    balde(c, 470, 540, 400, nivel, ep(t, C["14.t"], 0.4), f"{_db(n):.0f} dB", GREEN if n == 10 else PURPLE)
    if ab > 0:
        text_mid(c, f"{n} {'copo' if n == 1 else 'copos'}", 1350, 680, 46, "black", INK, ab)
    acc = ep(t, C["14.c"] + 1.2, 0.5)
    if acc > 0:
        selo(c, 1350, 780, acc, "10 FONTES IGUAIS → 90 dB", GREEN, -3, 32)


def b_atalho_som(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "FONTES IGUAIS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["15.t"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 620, GREEN, a0, 0.08)
        text(c, "ATALHO · CONTE OS COPOS", 960, 250, 24, "black", GREEN, a0, tracking=2)
    for k, (cue, n, s_) in enumerate((("15.b", 2, "+3 dB"), ("15.c", 10, "+10 dB"))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 400 + k * 170
        text_mid(c, f"{n} fontes iguais", 620, y, 48, "black", INK, ak)
        arrow(c, 900, y, 1040, y, GREEN, ak, 5, 16)
        text_mid(c, s_, 1250, y, 64, "black", GREEN, ak)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        selo(c, 960, 750, ad, "NUNCA SOME AS ETIQUETAS", RED, -3, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "QUANTOS DECIBÉIS?", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    yq = 300 if t < C["17"] else 250
    mx(c, "I = 10^{-6}", 900, yq, 70, aa, INK)
    text(c, "W/m²", 1080, yq + 22, 40, "bold", INK2, aa, align="left")
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, 960, 560)
        return
    aa = ep(t, C["17.a"], 0.5)
    mx(c, "I/I₀ = 10^{-6}/10^{-12} = 10^6", 960, 420, 52, aa, PURPLE)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        rrect(c, 520, 540, 880, 110, 22, mix("#FFFFFF", GREEN, 0.14), ab)
        mx(c, "β = 10 · 6 = 60", 900, 595, 54, ab, INK)
        text(c, "dB", 1110, 614, 48, "black", GREEN, ab, align="left")
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        pill(c, "atalho: 6 degraus acima do limiar → 60 dB", 960, 740, GREEN, size=28, a=acc, anchor="center")


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Cada 10 dB a mais, intensidade ×10.",
          "Para comparar, divida a diferença por 10 e eleve 10 ao resultado.",
          "Intensidades se somam; decibéis, não: dobrar a intensidade soma cerca de 3 dB."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "30"])
    frame(c, t, B["start"] if sid == "18" else C["30"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1360, 58)


ERROS = [("+1 dB = intensidade × 10",
          "o log conta zeros, e cada degrau parece valer um zero",
          "o 10 da fórmula espalha cada zero por 10 dB: dobrar já pede 3 dB; × 10 pede +10 dB."),
         ("80 dB + 80 dB = 160 dB",
          "duas máquinas somam barulho",
          "somam INTENSIDADE, não etiqueta: a intensidade dobra e o nível vai para cerca de 83 dB.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=820):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS5 = [("A", "−40 dB", "não dividiu por I₀", RED), ("B", "8 dB", "esqueceu o 10", RED), ("C", "80 dB", "", GREEN),
         ("D", "120 dB", "só o expoente de I₀", RED), ("E", "160 dB", "somou 4 + 12", RED)]


def b_q5(c, t, C, B):
    sid = which(t, C, ["21", "22", "23"])
    head(c, t, B["start"], "QUESTÃO 5 · EU FAÇO", "CALCULAR DECIBÉIS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    K.alternativas(c, t, C, ALTS5, 1180, 250, 480, 40, C["22.ok"], "C", {L: C[f"21.q{L.lower()}"] for L in "ABCDE"},
                   {L: C[f"23.x{L.lower()}"] for L in "ABDE"}, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    if sid == "21":
        y = _enunciado(c, [("O nível sonoro β, em decibéis, é dado por", INK)], a0, 260, 32)
        mx(c, "β = 10 · log (I/I₀)", 520, y + 40, 50, a0, PURPLE)
        y = _enunciado(c, [("com I₀ = 10⁻¹² W/m². Perto de uma britadeira, mediu-se I = 10⁻⁴ W/m². O nível sonoro "
                            "nesse ponto é", INK)], a0, y + 130, 30)
        return
    a1 = ep(t, C["22"], 0.4)
    rrect(c, 170, 200, 940, 630, 18, "#FFFFFF", a1, shadow=True)
    mx(c, "I/I₀ = 10^{-4}/10^{-12} = 10^8", 640, 300, 46, ep(t, C["22.a"], 0.4), PURPLE)
    ab = ep(t, C["22.b"], 0.4)
    if ab > 0:
        mx(c, "β = 10 · log 10^8 = 10 · 8 = 80", 600, 470, 46, ab, INK)
        text(c, "dB", 1000, 486, 42, "black", GREEN, ab, align="left")
    acc = ep(t, C["22.c"], 0.4)
    if acc > 0:
        medidor(c, 450, 690, 170, 80, acc)
        rrect(c, 640, 640, 420, 110, 20, mix("#FFFFFF", AMBER, 0.16), acc)
        text(c, "limite: 85 dB", 850, 690, 34, "black", AMBER, acc)
        text(c, "abaixo, mas perto", 850, 730, 26, "bold", INK2, acc)


ALTS4 = [("A", "2 vezes", "dividiu 80 ÷ 40", RED), ("B", "4 vezes", "não elevou 10", RED),
         ("C", "40 vezes", "usou a diferença", RED), ("D", "10 000 vezes", "", GREEN),
         ("E", "=10^{40} vezes", "não dividiu por 10", RED)]


def b_q4(c, t, C, B):
    sid = which(t, C, ["24", "25", "26"])
    head(c, t, B["start"], "QUESTÃO 4 · NÓS FAZEMOS", "COMPARAR DOIS SONS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    K.alternativas(c, t, C, ALTS4, 1140, 250, 520, 36, C["25.ok"], "D", {L: C[f"24.q{L.lower()}"] for L in "ABCDE"},
                   {L: C[f"26.x{L.lower()}"] for L in "ABCE"}, gap=34)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    if sid == "24":
        _enunciado(c, [("Com β = 10 · log(I/I₀), numa avenida movimentada mediu-se 80 dB; numa biblioteca, 40 dB.", INK),
                       ("A intensidade sonora na avenida é, em relação à da biblioteca, quantas vezes maior?", INK)], a0, 270, 32, 860)
        pause_timer(c, t, C["24.end"] - 1.9, 560, 660)
        return
    a1 = ep(t, C["25"], 0.4)
    rrect(c, 170, 200, 900, 630, 18, "#FFFFFF", a1, shadow=True)
    medidor(c, 360, 340, 170, 80, a1)
    medidor(c, 660, 340, 170, 40, a1)
    aa = ep(t, C["25.a"], 0.4)
    linha(c, [("diferença: ", INK2), ("80 − 40 = 40 dB", INK)], 620, 500, 40, aa)
    ab = ep(t, C["25.b"], 0.4)
    linha(c, [("40 ÷ 10 = ", INK), ("4", PURPLE)], 620, 600, 44, ab)
    acc = ep(t, C["25.c"], 0.4)
    if acc > 0:
        rrect(c, 330, 670, 580, 100, 20, GREEN, acc)
        mx(c, "10^4 = 10 000", 540, 720, 50, acc, "#FFFFFF")
        text(c, "vezes", 760, 736, 34, "black", "#FFFFFF", acc, align="left")


ALTS9 = [("A", "2", "dobrar soma só 3 dB", RED), ("B", "4", "3 dB por máquina?", RED), ("C", "8", "80 ÷ 10", RED),
         ("D", "10", "", GREEN), ("E", "11", "a 1ª já conta", RED)]


def b_q9(c, t, C, B):
    sid = which(t, C, ["27", "28", "29"])
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "SOMAR FONTES SONORAS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    K.alternativas(c, t, C, ALTS9, 1180, 250, 480, 40, C["28.ok"], "D", {L: C[f"27.q{L.lower()}"] for L in "ABCDE"},
                   {L: C[f"29.x{L.lower()}"] for L in "ABCE"}, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
         align="left")
    if sid == "27":
        _enunciado(c, [("Numa oficina, uma máquina produz 70 dB num certo ponto. O dono quer instalar outras máquinas "
                        "idênticas para que TODAS juntas produzam 80 dB nesse ponto.", INK),
                       ("As intensidades de fontes iguais se somam. O número TOTAL de máquinas deve ser", INK)],
                   a0, 270, 30, 880)
        pause_timer(c, t, C["27.end"] - 1.9, 560, 690)
        return
    a1 = ep(t, C["28"], 0.4)
    rrect(c, 170, 200, 940, 630, 18, "#FFFFFF", a1, shadow=True)
    aa = ep(t, C["28.a"], 0.4)
    linha(c, [("70 dB → 80 dB:  ", INK), ("+10 dB", PURPLE)], 640, 280, 42, aa)
    ab = ep(t, C["28.b"], 0.4)
    linha(c, [("+10 dB = intensidade ", INK), ("× 10", PURPLE)], 640, 360, 40, ab)
    acc = ep(t, C["28.c"], 0.4)
    for k in range(10):
        ak = acc * ep(t, C["28.c"] + 0.15 * k, 0.3)
        maquina(c, 290 + (k % 5) * 170, 500 + (k // 5) * 160, 100, ak)
    if acc > 0:
        pill(c, "10 máquinas no total", 640, 790, GREEN, size=30, a=ep(t, C["28.c"] + 1.8, 0.4), anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    itens = [("pH", BLUE), ("terremotos", AMBER), ("decibéis", PURPLE)]
    for k, (s_, col) in enumerate(itens):
        ak = aa * ep(t, C["31.a"] + 0.8 * k, 0.4)
        if ak <= 0:
            continue
        x = 560 + k * 400
        cartao(c, x - 170, 230, 340, 220, ak)
        if k == 0:
            p = skia.Path()
            p.moveTo(x, 270); p.cubicTo(x + 60, 340, x + 50, 400, x, 400); p.cubicTo(x - 50, 400, x - 60, 340, x, 270)
            c.drawPath(p, paint(col, ak))
        elif k == 1:
            pts = [(-110, 340), (-70, 340), (-50, 290), (-25, 390), (0, 300), (25, 380), (50, 320), (70, 340),
                   (110, 340)]
            for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
                line(c, x + x0, y0, x + x1, y1, col, ak, 6)
        else:
            medidor(c, x, 340, 100, 85, ak, rotulo=False)
        text(c, s_, x, 430, 32, "black", col, ak)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 560, ab, "CAÇA ÀS PEGADINHAS", AMBER, -3, 46)
    acc = ep(t, C["31.c"], 0.5)
    for k, (s_, col) in enumerate((("Química", BLUE), ("Física", PURPLE), ("Geografia", GREEN))):
        ak = acc * ep(t, C["31.c"] + 0.7 * k, 0.4)
        if ak > 0:
            chip(c, s_, 560 + k * 400, 720, col, ak, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Qual é o lugar mais barulhento que você frequenta?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicoes=b_definicoes,
              formula=b_formula, atalho_db=b_atalho_db, escala=b_escala, tabela=b_tabela, comparar=b_comparar,
              atalho_cmp=b_atalho_cmp, somar=b_somar, atalho_som=b_atalho_som, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q5=b_q5, q4=b_q4, q9=b_q9, ponte=b_ponte, cta=b_cta)
