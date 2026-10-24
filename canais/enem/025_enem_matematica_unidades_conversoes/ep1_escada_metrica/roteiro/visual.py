"""Visual — Unidades de Medida e Conversões, Episódio 1: a escada do sistema métrico, comprimento e massa (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: escada() (7 degraus com a bolinha e "× 10" / "÷ 10" a cada passo), vnum() (número com a vírgula andando
para a direita ou para a esquerda), regua() (1 m com 100 cm e o zoom de 1 cm com 10 mm), linha() (texto com cor por trecho).
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
_s = importlib.util.spec_from_file_location("comum025", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_unidades_ep1_escada_metrica.mp4"
CARD_R = K.CARD_R
DEGRAU = K.DEGRAU
MADEIRA = "#E9C98F"
MADEIRA_ESC = "#B98B45"

COMP = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
MASSA = ["kg", "hg", "dag", "g", "dg", "cg", "mg"]


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def escada(c, x0, y0, sw, sh, units, a, hl=None, cor_hl=None, ball=None, ball_a=0.0, path=None, size=40, base=3,
           rotulos=True):
    """escada de 7 degraus, do maior (em cima, à esquerda) para o menor (embaixo, à direita).
    hl = índices destacados; ball = posição (float, índice) da bolinha; path = (i0, i1): rótulos × 10 / ÷ 10 nas
    transições já percorridas pela bolinha; base = índice da unidade-base (pintado de azul)"""
    if a <= 0:
        return
    floor = y0 + 7 * sh + 30
    for i, u in enumerate(units):
        x, y = x0 + i * sw, y0 + i * sh
        col = DEGRAU
        if hl and i in hl:
            col = mix(DEGRAU, cor_hl or GREEN, 0.25)
        rrect(c, x + 4, y, sw - 8, floor - y, 14, col, a, shadow=True)
        tc = BLUE if i == base else INK
        if hl and i in hl:
            tc = cor_hl or GREEN
        text_mid(c, u, x + sw / 2, y + 44, size, "black", tc, a)
    if path and ball is not None and ball_a > 0:
        i0, i1 = path
        stp = 1 if i1 > i0 else -1
        for k in range(i0, i1, stp):
            j = k + (1 if stp > 0 else 0)          # transição entre k e k+stp acontece na borda do degrau j
            passou = (ball - k) * stp
            al = ball_a * clamp((passou - 0.55) / 0.3)
            if al <= 0:
                continue
            dest = k + stp
            xa = x0 + (dest + 0.5) * sw
            ya = y0 + dest * sh + 82
            lbl = "× 10" if stp > 0 else "÷ 10"
            colr = GREEN if stp > 0 else RED
            rrect(c, xa - 52, ya - 24, 104, 46, 23, "#FFFFFF", al, shadow=True)
            text_mid(c, lbl, xa, ya, 28, "black", colr, al)
    if ball is not None and ball_a > 0:
        i = clamp(ball, 0, 6)
        fi = math.floor(i)
        fr_ = i - fi
        yb = y0 + (fi + (fr_ if fr_ > 0 else 0)) * sh
        hop = math.sin(math.pi * fr_) * sh * 0.9
        xb = x0 + (i + 0.5) * sw
        c.drawCircle(xb, yb - 30 - hop, 22, paint(AMBER, ball_a))
        c.drawCircle(xb - 6, yb - 36 - hop, 7, paint("#FFFFFF", ball_a * 0.6))


def vnum(c, digitos, p0, s, cx, cy, size, a, col=None, zero_col=None):
    """número sem vírgula (ex.: '25') com a vírgula inicialmente depois de p0 algarismos; s = casas andadas
    (positivo = para a DIREITA, multiplica; negativo = para a ESQUERDA, divide). Zeros aparecem conforme a vírgula passa."""
    if a <= 0:
        return
    col = col or INK
    zero_col = zero_col or GRAY
    n = len(digitos)
    p = p0 + s
    rp = max(0, math.ceil(p - n - 1e-9))
    lp = max(0, math.ceil(1 - p - 1e-9))
    ds = "0" * lp + digitos + "0" * rp
    dw = text_w("0", "black", size) * 1.02
    x0 = cx - len(ds) * dw / 2
    for i, d in enumerate(ds):
        if i < lp:
            fade = a * clamp((1 - p) - (lp - i - 1))
            cc = zero_col
        elif i >= lp + n:
            fade = a * clamp(p - n - (i - lp - n))
            cc = zero_col
        else:
            fade, cc = a, col
        fmid(c, d, x0 + dw * (i + 0.5), cy, size, "black", cc, fade)
    ci = p + lp
    xv = x0 + dw * ci
    jump = abs(math.sin(math.pi * (abs(s) % 1))) * size * 0.35
    va = a * clamp(len(ds) - ci + 0.05)                 # vírgula no fim do número some (vira inteiro)
    fmid(c, ",", xv, cy + size * 0.18 - jump, size, "black", RED, va)


def regua(c, x0, x1, y, a, cm_a=1.0, mm_a=0.0, zoom_a=0.0):
    """régua de 1 m: 100 risquinhos de cm (rótulos de 10 em 10) e o zoom de 1 cm com 10 mm"""
    if a <= 0:
        return
    h = 90
    rrect(c, x0 - 20, y, x1 - x0 + 40, h, 10, MADEIRA, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 20, y, x1 - x0 + 40, h), 10, 10),
                paint(MADEIRA_ESC, a, stroke=3))
    step = (x1 - x0) / 100
    for i in range(101):
        x = x0 + i * step
        if i % 10 == 0:
            line(c, x, y, x, y + 44, INK, a, 3)
            text(c, str(i), x, y + 76, 22, "bold", INK, a * cm_a)
        else:
            line(c, x, y, x, y + (28 if i % 5 == 0 else 18), INK2, a * cm_a, 2)
    if zoom_a > 0:
        # destaque do 1º centímetro e o zoom
        zx = x0 + 20 * step
        c.drawRect(skia.Rect.MakeXYWH(zx, y - 6, step, h + 12), paint(GREEN, a * zoom_a, stroke=3))
        bx, by, bw, bh = 1060, y + 150, 560, 170
        line(c, zx, y + h + 6, bx, by, GREEN, a * zoom_a * 0.6, 2)
        line(c, zx + step, y + h + 6, bx + bw, by, GREEN, a * zoom_a * 0.6, 2)
        rrect(c, bx, by, bw, bh, 18, MADEIRA, a * zoom_a, shadow=True)
        for i in range(11):
            x = bx + 40 + i * (bw - 80) / 10
            ln_ = 70 if i in (0, 10) else (50 if i == 5 else 36)
            line(c, x, by, x, by + ln_, INK, a * zoom_a * (mm_a if 0 < i < 10 else 1), 3)
        text(c, "1 cm = 10 mm", bx + bw / 2, by + bh - 26, 34, "black", GREEN, a * zoom_a)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def cena(c, cx, cy, titulo, l1, l2, col, a, w=360, h=270):
    """cartão de uma medida do dia a dia"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 24, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 60, 24, col, a * 0.14)
    text(c, titulo, cx, cy - h / 2 + 42, 28, "black", col, a)
    text(c, l1, cx, cy + 20, 46, "black", INK, a)
    text(c, l2, cx, cy + 84, 30, "bold", INK2, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "UNIDADES DE MEDIDA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 560, 260, 800, 150, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("1,8 m  =  ", INK), ("18", RED), (" cm", INK)], W / 2, 335, 72, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        conferido(c, "a conta fecha", 640, 500, ab, True, 34)
        conferido(c, "o número é bonito", 1000, 500, ep(t, C["01.b"] + 1.0, 0.4), True, 34)
        conferido(c, "e está errado", 820, 580, ep(t, C["01.b"] + 2.2, 0.4), False, 40)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        selo(c, W / 2, 760, ac, "O ERRO SILENCIOSO", AMBER, -2, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "converter comprimento e massa contando degraus", "km, m, cm, mm · t, kg, g, mg"),
            ("02.b", "conferir o resultado em 2 segundos", "unidade menor, número maior")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "× 10, × 100, × 1 000", 560, 290, 40, "black", GREEN, aa)
        text(c, "a vírgula anda para a DIREITA", 560, 340, 28, "bold", INK2, aa)
        vnum(c, "47", 1, 2 * ep(t, C["03.a"] + 1.2, 1.2), 560, 480, 110, aa, INK)
        text(c, "÷ = para a ESQUERDA", 560, 640, 32, "black", RED, ep(t, C["03.a"] + 4.2, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "QUILO = MIL", 1380, 290, 44, "black", BLUE, ab)
        linha(c, [("10³", BLUE), (" = 1 000", INK)], 1380, 430, 70, ab)
        text(c, "1 km = 1 000 m", 1380, 580, 40, "black", INK2, ep(t, C["03.b"] + 2.5, 0.4))
        text(c, "1 kg = 1 000 g", 1380, 640, 40, "black", INK2, ep(t, C["03.b"] + 3.4, 0.4))
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def b_cotidiano(c, t, C, B):
    head(c, t, B["start"], "NO DIA A DIA", "QUANTAS UNIDADES VOCÊ USA?", BLUE)
    card(c, *CARD_R)
    cards = [("04.a", "SUA ALTURA", "1,75 m", "= 175 cm"), ("04.b", "ATÉ O TRABALHO", "8 km", "quilômetros"),
             ("04.c", "O REMÉDIO", "500 mg", "miligramas"), ("04.d", "O CAMINHÃO", "12 t", "toneladas")]
    for k, (cue, tit, l1, l2) in enumerate(cards):
        x = 390 + k * 380
        cena(c, x, 430, tit, l1, l2, BLUE, ep(t, C[cue], 0.5))
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        regra(c, "mesma medida, números diferentes: o erro mora na TROCA", W / 2, 700, ae, 34)


# ======================================================================
# blocos a, b — unidades-base e a escada
# ======================================================================

def b_base(c, t, C, B):
    head(c, t, B["start"], "UNIDADES-BASE", "DE ONDE AS OUTRAS SAEM", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "UNIDADE-BASE = a unidade de referência", W / 2, 260, 36, "black", BLUE, aa)
    bases = [("METRO", "m", "comprimento"), ("GRAMA", "g", "massa"), ("LITRO", "L", "capacidade")]
    for k, (n, s, q) in enumerate(bases):
        a = ep(t, C["05.b"] + 1.6 * k, 0.5)
        x = 560 + k * 400
        rrect(c, x - 170, 310, 340, 200, 22, "#FFFFFF", a, shadow=True)
        text(c, s, x, 410, 80, "black", BLUE, a)
        text(c, n, x, 460, 30, "black", INK, a)
        text(c, q, x, 494, 24, "bold", GRAY, a)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        text(c, "PREFIXO = o pedacinho antes do nome: quantas vezes maior ou menor", W / 2, 580, 30, "black", PURPLE, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        linha(c, [("quilo", GREEN), ("metro · ", INK), ("quilo", GREEN), ("grama  →  quilo = 1 000", INK)],
              W / 2, 660, 36, ad)
        linha(c, [("mili", RED), ("metro · ", INK), ("mili", RED), ("grama · ", INK), ("mili", RED),
                  ("litro  →  mili = a milésima parte", INK)], W / 2, 730, 36, ep(t, C["05.d"] + 2.2, 0.4))


ESC_X, ESC_Y, ESC_W, ESC_H = 300, 300, 190, 54


def b_escada(c, t, C, B):
    head_seq(c, t, C, [("06", "A ESCADA", "7 DEGRAUS", PURPLE), ("07", "ATALHO", "UMA FRASE PARA DECORAR", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    a0 = ep(t, C["06"], 0.5)
    if sid == "06":
        hl = {3}
        if t >= C["06.b"]:
            hl = {0, 1, 2, 3}
        if t >= C["06.c"]:
            hl = {3, 4, 5, 6}
        cor = GREEN if t < C["06.c"] else AMBER
        escada(c, ESC_X, ESC_Y, ESC_W, ESC_H, COMP, a0, hl if t >= C["06.a"] else None, cor if t >= C["06.b"] else BLUE)
        ab = ep(t, C["06.b"], 0.4) * (1 - ep(t, C["06.c"], 0.3))
        if ab > 0:
            text(c, "MÚLTIPLOS: maiores que o metro", 1220, 280, 30, "black", GREEN, ab)
            for k, s in enumerate(("dam = 10 m", "hm = 100 m", "km = 1 000 m")):
                text(c, s, 1220, 340 + k * 50, 32, "bold", INK2, ab)
        acc = ep(t, C["06.c"], 0.4)
        if acc > 0:
            text(c, "SUBMÚLTIPLOS: menores que o metro", 1220, 280, 30, "black", AMBER, acc)
            for k, s in enumerate(("dm = 0,1 m", "cm = 0,01 m", "mm = 0,001 m")):
                text(c, s, 1220, 340 + k * 50, 32, "bold", INK2, acc)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            boxed(c, 300, 712, 1320, 96, PURPLE, ad, 0.08)
            linha(c, [("DESCER um degrau: ", INK), ("× 10", GREEN), ("     SUBIR um degrau: ", INK), ("÷ 10", RED)],
                  W / 2, 760, 40, ad)
        return
    escada(c, ESC_X, ESC_Y, ESC_W, ESC_H, COMP, 1.0)
    ab = ep(t, C["07.b"], 0.5)
    palavras = ["Kátia", "Hoje", "Dançou", "Muito,", "Dançou", "Com", "Marcos"]
    for i, w_ in enumerate(palavras):
        a = ab * ep(t, C["07.b"] + 0.35 * i, 0.3)
        x = ESC_X + (i + 0.5) * ESC_W
        y = ESC_Y + i * ESC_H + 82
        text(c, w_, x, y, 28, "black", GREEN, a)
    acc = ep(t, C["07.c"], 0.4)
    if acc > 0:
        for i, u in enumerate(COMP):
            a = acc * ep(t, C["07.c"] + 0.8 * i, 0.3)
            x = ESC_X + (i + 0.5) * ESC_W
            y = ESC_Y + i * ESC_H - 34
            c.drawCircle(x, y, 22, paint(PURPLE, a))
            text_mid(c, u[0].upper(), x, y, 28, "black", "#FFFFFF", a)
    ad = ep(t, C["07.d"], 0.5)
    K.atalho(c, 300, 712, 1320, 100, "ATALHO", ["Kátia Hoje Dançou Muito, Dançou Com Marcos: K-H-D-M-D-C-M"],
             ad, 34)


# ======================================================================
# contando degraus
# ======================================================================

def b_contar(c, t, C, B):
    head_seq(c, t, C, [("08", "CONTE OS DEGRAUS", "2,5 km EM METROS", PURPLE),
                       ("09", "O CAMINHO DE VOLTA", "350 cm EM METROS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    ex, ey, ew, eh = 200, 250, 150, 50
    if sid == "08":
        a0 = ep(t, C["08"], 0.5)
        aa = ep(t, C["08.a"], 0.5)
        hl = {0, 3} if aa > 0 else None
        mv = ep(t, C["08.b"] + 0.3, 3.0)
        escada(c, ex, ey, ew, eh, COMP, a0, hl, PURPLE, ball=3 * mv if aa > 0 else None, ball_a=aa, path=(0, 3), size=34)
        cnt = int(min(3, math.floor(3 * mv + 0.45))) if t >= C["08.b"] else 0
        if t >= C["08.b"]:
            text(c, f"{cnt} degrau{'s' if cnt != 1 else ''} para BAIXO", 1440, 300, 34, "black", GREEN,
                 ep(t, C["08.b"], 0.4))
            text(c, "× 10 × 10 × 10  =  × 1 000", 1440, 360, 32, "bold", INK2, ep(t, C["08.b"] + 3.2, 0.4))
        s = 3 * ep(t, C["08.c"], 1.6)
        vnum(c, "25", 1, s, 1440, 500, 110, ep(t, C["08"], 0.5), INK)
        text(c, "km" if s < 0.05 else "m", 1440, 635, 36, "black", GRAY, a0)
        ac2 = ep(t, C["08.c"] + 2.2, 0.4)
        if ac2 > 0:
            linha(c, [("2,5 km = ", INK), ("2 500 m", GREEN)], 1440, 715, 50, ac2)
        return
    a0 = ep(t, C["09"], 0.5)
    mv = ep(t, C["09.a"] + 0.6, 2.0)
    escada(c, ex, ey, ew, eh, COMP, a0, {3, 5}, PURPLE, ball=5 - 2 * mv, ball_a=a0, path=(5, 3), size=34)
    if t >= C["09.a"]:
        text(c, "2 degraus para CIMA", 1440, 300, 34, "black", RED, ep(t, C["09.a"], 0.4))
        text(c, "÷ 10 ÷ 10  =  ÷ 100", 1440, 360, 32, "bold", INK2, ep(t, C["09.a"] + 3.0, 0.4))
    s = -2 * ep(t, C["09.b"], 1.4)
    vnum(c, "350", 3, s, 1440, 500, 110, a0, INK)
    text(c, "cm" if s > -0.05 else "m", 1440, 635, 36, "black", GRAY, a0)
    ab2 = ep(t, C["09.b"] + 2.0, 0.4)
    if ab2 > 0:
        linha(c, [("350 cm = ", INK), ("3,5 m", GREEN)], 1440, 690, 48, ab2)
    acc = ep(t, C["09.c"], 0.5)
    K.atalho(c, 1110, 742, 660, 88, "ATALHO", ["cada degrau = uma casa da vírgula"], acc, 30)


# ======================================================================
# bloco c — a conferência de sentido
# ======================================================================

def b_sentido(c, t, C, B):
    head(c, t, B["start"], "A CONFERÊNCIA DE SENTIDO", "ANDOU PARA O LADO CERTO?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        # a mesma distância: 1 m em cima (1 bloco grande) e 100 cm embaixo (100 tracinhos)
        x0, x1 = 300, 1100
        rrect(c, x0, 300, x1 - x0, 70, 12, BLUE, aa * 0.85)
        text_mid(c, "1 metro", (x0 + x1) / 2, 335, 36, "black", "#FFFFFF", aa)
        n = int(100 * ep(t, C["10.a"] + 0.8, 2.0))
        step = (x1 - x0) / 100
        for i in range(n):
            rrect(c, x0 + i * step + 1, 400, step - 2, 70, 2, AMBER, aa * 0.9)
        text(c, f"{n} centímetros", (x0 + x1) / 2, 520, 36, "black", AMBER, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        boxed(c, 1180, 300, 440, 220, PURPLE, ab, 0.08)
        text(c, "unidade MENOR", 1400, 370, 38, "black", PURPLE, ab)
        text(c, "número MAIOR", 1400, 430, 38, "black", GREEN, ab)
        text(c, "(e vice-versa)", 1400, 480, 26, "bold", GRAY, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        K.atalho(c, 300, 590, 1320, 110, "ATALHO · 2 SEGUNDOS", ["km → m: a unidade ficou menor, o número TEM que crescer"],
                 acc, 32)
        linha(c, [("2,5  →  2 500", GREEN), ("   cresceu: fecha", INK2)], W / 2, 770, 40, ep(t, C["10.c"] + 5.0, 0.4))


def b_prefixos(c, t, C, B):
    head(c, t, B["start"], "FORA DA ESCADA", "SÓ PARA CONHECER", BLUE)
    card(c, *CARD_R)
    rows = [("11.a", "mega", "M", "1 milhão", "10^6", "megawatt da usina", GREEN),
            ("11.a", "giga", "G", "1 bilhão", "10^9", "gigabyte do celular", GREEN),
            ("11.b", "micro", "μ", "a milionésima parte", "10^{-6}", "", AMBER),
            ("11.b", "nano", "n", "a bilionésima parte", "10^{-9}", "tamanho de um vírus", AMBER)]
    for k, (cue, n, s, v, p, ex_, col) in enumerate(rows):
        a = ep(t, C[cue] + (1.6 if k in (1, 3) else 0), 0.5)
        y = 290 + k * 105
        text(c, n, 330, y, 48, "black", col, a, align="left")
        text(c, v, 640, y, 36, "black", INK, a, align="left")
        expr(c, p, 1130, y - 14, 46, a)
        text(c, ex_, 1290, y, 28, "bold", GRAY, a, align="left")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        pill(c, "série de Notação científica", W / 2, 740, PURPLE, size=30, a=acc, anchor="center")


# ======================================================================
# bloco e — comprimento
# ======================================================================

def b_comprimento(c, t, C, B):
    head_seq(c, t, C, [("12", "COMPRIMENTO", "AS CONVERSÕES QUE MAIS CAEM", PURPLE),
                       ("13", "A RÉGUA DE 1 METRO", "100 cm · 1 000 mm", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        rows = [("12.a", "km → m", "3 degraus", "× 1 000", "2,5 km = 2 500 m", GREEN),
                ("12.b", "m → cm", "2 degraus", "× 100", "1,8 m = 180 cm", GREEN),
                ("12.c", "m → mm", "3 degraus", "× 1 000", "0,45 m = 450 mm", GREEN),
                ("12.d", "cm → mm", "1 degrau", "× 10", "7,2 cm = 72 mm", GREEN),
                ("12.e", "cm → m", "sobe 2", "÷ 100", "350 cm = 3,5 m", RED)]
        for k, (cue, conv, deg, f, exm, col) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            y = 270 + k * 100
            rrect(c, 200, y - 44, 1520, 84, 16, "#F7F7F5", a)
            text(c, conv, 260, y + 12, 44, "black", INK, a, align="left")
            text(c, deg, 620, y + 12, 32, "bold", GRAY, a, align="left")
            text(c, f, 920, y + 12, 46, "black", col, a, align="left")
            text(c, exm, 1220, y + 12, 36, "bold", INK2, a, align="left")
        return
    a0 = ep(t, C["13.a"], 0.5)
    regua(c, 260, 1660, 300, a0, ep(t, C["13.b"], 0.6), ep(t, C["13.c"] + 0.4, 0.8), ep(t, C["13.c"], 0.5))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        text(c, "1 m = 100 cm", 300, 520, 44, "black", BLUE, ab, align="left")
    acc = ep(t, C["13.c"] + 2.0, 0.5)
    if acc > 0:
        text(c, "10 × 100 = 1 000 mm", 300, 600, 40, "black", GREEN, acc, align="left")
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        regra(c, "1 m = 100 cm = 1 000 mm", W / 2, 770, ad, 36)


# ======================================================================
# bloco f — massa
# ======================================================================

def b_massa(c, t, C, B):
    head_seq(c, t, C, [("14", "MASSA", "A MESMA ESCADA", PURPLE), ("15", "MASSAS GRANDES", "TONELADA E ARROBA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        a0 = ep(t, C["14.a"], 0.5)
        hl = None
        if t >= C["14.b"]:
            hl = {0, 3}
        if t >= C["14.c"]:
            hl = {3, 6}
        escada(c, 200, 250, 150, 50, MASSA, a0, hl, GREEN if t < C["14.c"] else AMBER, size=34)
        ab = ep(t, C["14.b"], 0.5) * (1 - ep(t, C["14.c"], 0.3))
        if ab > 0:
            linha(c, [("1 kg = ", INK), ("1 000 g", GREEN)], 1440, 330, 56, ab)
            text(c, "3 degraus", 1440, 410, 30, "bold", GRAY, ab)
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            linha(c, [("1 mg = ", INK), ("0,001 g", AMBER)], 1440, 330, 56, acc)
            text(c, "a milésima parte do grama", 1440, 410, 28, "bold", GRAY, acc)
            rrect(c, 1290, 500, 300, 110, 55, "#FFFFFF", acc, shadow=True)
            rrect(c, 1290, 500, 150, 110, 55, BLUE, acc * 0.25)
            text(c, "500 mg", 1440, 570, 36, "black", INK, acc)
            linha(c, [("= ", INK), ("0,5 g", GREEN)], 1440, 680, 44, ep(t, C["14.c"] + 3.5, 0.4))
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 260, 620, 380, 24, "#FFFFFF", aa, shadow=True)
        text(c, "TONELADA", 570, 320, 34, "black", BLUE, aa)
        linha(c, [("1 t = ", INK), ("1 000 kg", GREEN)], 570, 410, 60, aa)
        text(c, "um QUILO de quilos", 570, 490, 34, "black", PURPLE, ep(t, C["15.a"] + 1.6, 0.4))
        linha(c, [("2 t = ", INK2), ("2 000 kg", GREEN)], 570, 580, 40, ep(t, C["15.a"] + 3.6, 0.4))
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        rrect(c, 1040, 260, 620, 380, 24, "#FFFFFF", ab, shadow=True)
        text(c, "ARROBA", 1350, 320, 34, "black", BLUE, ab)
        linha(c, [("1 arroba = ", INK), ("15 kg", GREEN)], 1350, 410, 56, ab)
        text(c, "cotação do gado", 1350, 490, 30, "bold", GRAY, ab)
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            linha(c, [("20 arrobas = 20 × 15 = ", INK2), ("300 kg", GREEN)], 1350, 580, 36, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "EM RITMO DE JOGO", GREEN), ("17", "VAMOS CONFERIR", "CONTANDO DEGRAUS", GREEN)])
    card(c, *CARD_R)
    contas = [("16.a", "3,2 km = ? m", "17.a", "3 200 m", "desce 3 · × 1 000"),
              ("16.b", "45 cm = ? m", "17.b", "0,45 m", "sobe 2 · ÷ 100"),
              ("16.c", "2,5 kg = ? g", "17.c", "2 500 g", "desce 3 · × 1 000"),
              ("16.d", "750 mg = ? g", "17.d", "0,75 g", "sobe 3 · ÷ 1 000")]
    for k, (cue, s, cr, r, how) in enumerate(contas):
        x = 470 + (k % 2) * 760
        y = 330 + (k // 2) * 230
        a = ep(t, C[cue], 0.5)
        rrect(c, x - 320, y - 90, 640, 180, 22, "#F7F7F5", a)
        text(c, s, x, y - 6, 52, "black", INK, a)
        if t >= C["17"]:
            ar = ep(t, C[cr], 0.4)
            text(c, "= " + r, x, y + 62, 46, "black", GREEN, ar)
            text(c, how, x, y + 100, 24, "bold", GRAY, ar)
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 790)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Cada degrau da escada vale 10.", "Unidade menor, número maior.", "Tonelada é mil quilos."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "25"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 60)


ERROS = [("Andar a vírgula para o lado errado", "você contou os degraus direitinho: só errou a direção",
          "unidade menor? o número tem que CRESCER (a conferência de 2 segundos)"),
         ("Achar que 1 tonelada = 100 kg", "cem é um número redondo, que soa como medida grande",
          "tonelada = 1 000 kg: um quilo de quilos"),
         ("Somar medidas em unidades diferentes", "a conta fecha: 2 m + 30 cm = \"32\"",
          "padronize antes: 200 cm + 30 cm = 230 cm")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# Questão 7 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS7 = [("A", "35 kg", "uma casa só (× 10)", RED), ("B", "350 kg", "× 100: peso de uma moto", RED),
         ("C", "3 500 kg", "", GREEN), ("D", "35 000 kg", "35 t: acima do limite", RED),
         ("E", "350 000 kg", "cinco casas", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    _enunciado(c, [("Um caminhão transporta uma carga de 3,5 toneladas de grãos.", INK),
                   ("Essa carga, expressa em quilogramas, corresponde a", BLUE)], a0, 250)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABDE"}
    if t >= C["22.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS7, 1000, 250, 680, 44, C["23.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["22.end"] - 1.9, 540, 600)
    if t >= C["23"]:
        ra = ep(t, C["23"], 0.4)
        rrect(c, 170, 440, 740, 370, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["23.a"], 0.4)
        linha(c, [("1 t = ", INK), ("1 000 kg", BLUE)], 540, 500, 40, aa)
        ab = ep(t, C["23.b"], 0.4)
        vnum(c, "35", 1, 3 * ep(t, C["23.b"] + 0.8, 1.6), 540, 600, 80, ab, INK)
        linha(c, [("3,5 × 1 000 = ", INK), ("3 500 kg", GREEN)], 540, 690, 36, ep(t, C["23.b"] + 2.8, 0.4))
        conferido(c, "unidade menor, número maior", 300, 750, ep(t, C["23.c"], 0.4), True, 26)
        conferido(c, "alguns milhares de quilos: faz sentido", 300, 790, ep(t, C["23.d"], 0.4), True, 26)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ÁREA E VOLUME", PURPLE)
    aa = ep(t, C["26.a"], 0.5)
    chip(c, "ÁREA", 760, 320, BLUE, aa, 46)
    chip(c, "VOLUME", 1180, 320, PURPLE, aa, 46)
    ab = ep(t, C["26.b"], 0.5)
    if ab > 0:
        escada(c, 360, 420, 110, 34, ["km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²"], ab, size=24)
        text(c, "cada degrau: × 100", 1340, 470, 40, "black", BLUE, ab)
        text(c, "(no volume: × 1 000)", 1340, 530, 34, "black", PURPLE, ep(t, C["26.b"] + 2.2, 0.4))
    acc = ep(t, C["26.c"], 0.5)
    if acc > 0:
        selo(c, 1340, 640, acc, "O ERRO MAIS CARO", RED, -3, 32)
    pill(c, "ep. 2 · área e volume", W / 2, 780, PURPLE, size=32, a=ep(t, C["26.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"], "Você já conhecia a frase da Kátia?",
        canal="no Estudativo", anki=C["27.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, base=b_base, escada=b_escada,
              contar=b_contar, sentido=b_sentido, prefixos=b_prefixos, comprimento=b_comprimento, massa=b_massa,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q7=b_q7, ponte=b_ponte, cta=b_cta)
