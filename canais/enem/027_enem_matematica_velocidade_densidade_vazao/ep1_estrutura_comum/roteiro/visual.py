"""Visual — Velocidade, Densidade e Vazão, Episódio 1: a estrutura comum (toda taxa é "quanto por unidade") (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: barra() (a barra da unidade virando traço de fração), triangulo() (o triângulo da taxa: numerador
em cima, taxa e denominador embaixo), velocimetro(), etiqueta(), conta_agua(), pacote(), cidade(), linha().
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
_s = importlib.util.spec_from_file_location("comum027", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_taxas_ep1_estrutura_comum.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
AGUA = "#9CC3EE"
ARROZ = "#F4EBD3"


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


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def barra(c, num, den, cx, cy, size, a, u, num_col=None, den_col=None, bar_col=None):
    """a unidade 'num/den' em linha (u = 0) virando fração empilhada (u = 1): a barra deita e vira o traço"""
    if a <= 0:
        return
    u = ease_io(clamp(u))
    num_col, den_col, bar_col = num_col or BLUE, den_col or GREEN, bar_col or RED
    wn, wd = ftext_w(num, "black", size), ftext_w(den, "black", size)
    gap = size * 0.55
    # posições em linha
    xn0 = cx - (wn + gap * 2 + wd) / 2 + wn / 2
    xs0 = cx - (wn + gap * 2 + wd) / 2 + wn + gap
    xd0 = xs0 + gap + wd / 2
    # posições empilhadas
    yn1, yd1 = cy - size * 0.62, cy + size * 0.70
    xn = lerp(xn0, cx, u); yn = lerp(cy, yn1, u)
    xd = lerp(xd0, cx, u); yd = lerp(cy, yd1, u)
    fmid(c, num, xn, yn, size, "black", num_col, a)
    fmid(c, den, xd, yd, size, "black", den_col, a)
    xs = lerp(xs0, cx, u)
    ang = math.radians(lerp(68, 0, u))
    L = lerp(size * 0.95, max(wn, wd) + size * 0.4, u)
    dx, dy = math.cos(ang) * L / 2, math.sin(ang) * L / 2
    line(c, xs - dx, cy + size * 0.02 + dy, xs + dx, cy + size * 0.02 - dy, bar_col, a, max(4, size * 0.09))


def triangulo(c, cx, cy, s, a, top, bl, br, foco=None, valores=None):
    """triângulo da taxa: top = numerador; bl = taxa; br = denominador. foco = 'top'|'bl'|'br' (o que se procura, em âmbar);
    valores = dict(slot: texto) substitui os rótulos."""
    if a <= 0:
        return
    h = s * 0.92
    pa, pb, pc = (cx, cy - h * 0.62), (cx - s * 0.62, cy + h * 0.38), (cx + s * 0.62, cy + h * 0.38)
    p = skia.Path(); p.moveTo(*pa); p.lineTo(*pb); p.lineTo(*pc); p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint(PURPLE, a, stroke=6))
    ym = cy - h * 0.06
    xl = lerp(pa[0], pb[0], (ym - pa[1]) / (pb[1] - pa[1]))
    xr = lerp(pa[0], pc[0], (ym - pa[1]) / (pc[1] - pa[1]))
    line(c, xl, ym, xr, ym, PURPLE, a, 5)
    line(c, cx, ym, cx, pb[1], PURPLE, a, 5)
    valores = valores or {}
    slots = {"top": (cx, cy - h * 0.24, top, BLUE), "bl": (cx - s * 0.26, cy + h * 0.17, bl, PURPLE),
             "br": (cx + s * 0.26, cy + h * 0.17, br, GREEN)}
    for k, (x, y, rot, col) in slots.items():
        sz = s * 0.11
        txt = valores.get(k, rot)
        if foco == k:
            rrect(c, x - s * 0.22, y - sz * 0.9, s * 0.44, sz * 1.8, 16, mix("#FFFFFF", AMBER, 0.35), a)
            col = AMBER
        while ftext_w(txt, "black", sz) > s * 0.40 and sz > 14:
            sz -= 2
        fmid(c, txt, x, y, sz, "black", col, a)


def velocimetro(c, cx, cy, r, a, frac=0.4):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#22262E", a))
    c.drawCircle(cx, cy, r, paint("#5B6270", a, stroke=6))
    rect = skia.Rect.MakeXYWH(cx - r * 0.78, cy - r * 0.78, r * 1.56, r * 1.56)
    c.drawArc(rect, 150, 240, False, paint("#5B6270", a, stroke=10))
    c.drawArc(rect, 150, 240 * frac, False, paint(GREEN, a, stroke=10))
    ang = math.radians(150 + 240 * frac)
    line(c, cx, cy, cx + math.cos(ang) * r * 0.66, cy + math.sin(ang) * r * 0.66, RED, a, 6)
    c.drawCircle(cx, cy, r * 0.08, paint("#FFFFFF", a))


def etiqueta(c, cx, cy, w, h, a, preco="R$ 4,50", unid="/kg"):
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    p = skia.Path(); p.moveTo(x + h * 0.35, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h); p.lineTo(x + h * 0.35, y + h)
    p.lineTo(x, cy); p.close()
    c.drawPath(p, paint(AMBER, a))
    c.drawCircle(x + h * 0.32, cy, h * 0.09, paint("#FFFFFF", a))
    linha(c, [(preco, "#FFFFFF"), (unid, "#FFF4D6")], cx + h * 0.15, cy, h * 0.34, a)


def conta_agua(c, cx, cy, w, h, a):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 10, PAPEL, a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, h * 0.2, 10, AGUA, a)
    text(c, "CONSUMO MÉDIO", cx, cy - h / 2 + h * 0.14, h * 0.08, "black", "#FFFFFF", a)
    for k in range(3):
        line(c, cx - w * 0.36, cy - h * 0.12 + k * h * 0.11, cx + w * 0.36, cy - h * 0.12 + k * h * 0.11, "#E2DED2", a, 4)
    linha(c, [("150 L", BLUE), ("/dia", INK2)], cx, cy + h * 0.32, h * 0.13, a)


def pacote(c, cx, cy, w, h, a, kg, preco, col=ARROZ):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 18, col, a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, h * 0.16, 18, "#D9C9A0", a)
    text(c, "ARROZ", cx, cy - h * 0.12, w * 0.16, "black", "#8A6D2E", a)
    text(c, kg, cx, cy + h * 0.10, w * 0.22, "black", INK, a)
    rrect(c, cx - w * 0.42, cy + h * 0.26, w * 0.84, h * 0.18, 12, AMBER, a)
    text_mid(c, preco, cx, cy + h * 0.35, min(w * 0.15, h * 0.11), "black", "#FFFFFF", a)


def cidade(c, x, y, w, h, a, n, seed=1, col=None):
    """retângulo (área) com n pontinhos (pessoas)"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, h, 12, mix("#FFFFFF", col, 0.10), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 12, 12), paint(col, a, stroke=4))
    k = seed * 7919
    for i in range(n):
        k = (k * 1103515245 + 12345) % 2147483648
        fx = (k % 1000) / 1000
        k = (k * 1103515245 + 12345) % 2147483648
        fy = (k % 1000) / 1000
        c.drawCircle(x + 10 + fx * (w - 20), y + 10 + fy * (h - 20), 5, paint(col, a * 0.75))


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    """faixa com a pergunta do bloco"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

UNIDS = [("km", "h"), ("g", "cm³"), ("L", "min"), ("km", "L"), ("R$", "kg"), ("hab", "km²")]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "VELOCIDADE, DENSIDADE E VAZÃO", BLUE)
    for k, (n_, d_) in reversed(list(enumerate(UNIDS))):
        a = ep(t, C["01.a"] + k * 0.75, 0.4)
        if a <= 0:
            continue
        x = 330 + (k % 3) * 630
        y = 330 + (k // 3) * 220
        m = ep(t, C["01.c"], 1.0)
        xx, yy = lerp(x, W / 2, m), lerp(y, 440, m)
        aa = a * (1 - m) if k else a
        rrect(c, xx - 170, yy - 80, 340, 160, 24, "#FFFFFF", aa, shadow=True)
        barra(c, n_, d_, xx, yy, 64, aa, ep(t, C["01.c"] + 0.4, 0.8) if k == 0 else 0)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        chip(c, "6 ASSUNTOS?", W / 2, 230, AMBER, ab * (1 - ep(t, C["01.c"], 0.4)), 36)
    acc = ep(t, C["01.c"] + 1.2, 0.5)
    if acc > 0:
        pill(c, "UM SÓ: quanto de uma coisa POR unidade de outra", W / 2, 640, BLUE, size=34, a=acc, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1500, 760, ad, "ESTUDE 6× MENOS", GREEN, -4, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    a, d = rise(t, C["02.a"])
    check_icon(c, 300, 346 + d, 34, a, GREEN)
    text(c, "olhar para qualquer unidade com barra...", 360, 360 + d, 48, "black", INK, a, align="left")
    if a > 0:
        rrect(c, 760, 430 + d, 400, 170, 26, "#FFFFFF", a, shadow=True)
        barra(c, "km", "h", 960, 515 + d, 72, a, 0)
    ab, db = rise(t, C["02.b"])
    if ab > 0:
        text(c, "...e saber na hora:", 360, 690 + db, 44, "black", INK, ab, align="left")
        chip(c, "× MULTIPLICAR", 1010, 676 + db, GREEN, ab, 40)
        chip(c, "÷ DIVIDIR", 1420, 676 + db, PURPLE, ab, 40)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "RAZÃO = comparação por DIVISÃO", 560, 290, 34, "black", BLUE, aa)
        text(c, "série de Razão", 560, 340, 26, "bold", GRAY, aa)
        fr(c, "2", "5", 460, 470, 90, INK, aa)
        text_mid(c, "= 2 ÷ 5", 650, 480, 64, "black", INK, ep(t, C["03.a"] + 2.5, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "UNIDADE COMPOSTA = duas unidades numa só", 1370, 290, 30, "black", BLUE, ab)
        text(c, "série de Unidades", 1370, 340, 26, "bold", GRAY, ab)
        rrect(c, 1170, 400, 400, 170, 26, "#FFFFFF", ab, shadow=True)
        barra(c, "km", "h", 1370, 485, 72, ab, 0)
        text(c, "quilômetro POR hora", 1370, 640, 32, "black", INK2, ep(t, C["03.b"] + 2.0, 0.4))
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    cols = [("04.a", "PAINEL DO CARRO"), ("04.b", "ETIQUETA DO MERCADO"), ("04.c", "CONTA DE ÁGUA")]
    for k, (cue, tit) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 220, 460, 470, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 220, 460, 60, 24, BLUE, a * 0.14)
        text(c, tit, x + 230, 262, 26, "black", BLUE, a)
        if k == 0:
            velocimetro(c, x + 230, 420, 105, a, 0.42)
            linha(c, [("80 km", INK), ("/h", RED)], x + 230, 580, 40, a)
            linha(c, [("12 km", INK), ("/L", RED)], x + 230, 640, 40, a)
        elif k == 1:
            etiqueta(c, x + 230, 430, 340, 130, a, "R$ 4,50", "/kg")
            text(c, "arroz tipo 1", x + 230, 560, 28, "bold", GRAY, a)
        else:
            conta_agua(c, x + 230, 455, 300, 340, a)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "a palavra que se repete:  POR", W / 2, 765, ad, 40, BLUE)


# ======================================================================
# bloco a — a estrutura comum
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "O QUE É TAXA", "QUANTO POR UNIDADE", BLUE), ("06", "AS TRÊS ESTRELAS", "A MESMA FORMA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            text(c, "TAXA", W / 2, 280, 64, "black", BLUE, aa)
            text(c, "quanto de uma coisa POR unidade de outra", W / 2, 350, 38, "black", INK, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            text_mid(c, "TAXA  =", 640, 540, 64, "black", INK, ab)
            fr(c, "quanto de uma coisa", "unidade de outra", 1080, 530, 52, INK, ab, num_col=BLUE, den_col=GREEN)
            pill(c, "RAZÃO: uma divisão", 640, 640, PURPLE, size=26, a=ab, anchor="center")
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            pill(c, "NUMERADOR: em cima, o quanto", 1080, 430, BLUE, size=24, a=acc, anchor="center")
            pill(c, "DENOMINADOR: embaixo, a referência", 1080, 650, GREEN, size=24,
                 a=ep(t, C["05.c"] + 1.8, 0.4), anchor="center")
        return
    rows = [("06.a", "VELOCIDADE", "km", "h", "distância ÷ tempo", "v = d ÷ t"),
            ("06.b", "DENSIDADE", "g", "cm³", "massa ÷ volume", "d = m ÷ V"),
            ("06.c", "VAZÃO", "L", "min", "volume ÷ tempo", "Q = V ÷ t")]
    for k, (cue, nome, n_, d_, words, simb) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 300 + k * 660
        text(c, nome, x + 2, 270, 38, "black", PURPLE, a)
        rrect(c, x - 200, 310, 400, 220, 24, "#FFFFFF", a, shadow=True)
        barra(c, n_, d_, x, 420, 70, a, ep(t, C[cue] + 0.8, 1.0))
        text(c, words, x, 590, 32, "black", INK, a)
        text(c, simb, x, 640, 28, "bold", GRAY, a)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        regra(c, "a MESMA forma: uma coisa em cima, outra embaixo", W / 2, 750, ad, 36)


# ======================================================================
# bloco b — a unidade escreve a fórmula
# ======================================================================

def b_unidade(c, t, C, B):
    head(c, t, B["start"], "ESQUECEU A FÓRMULA?", "A UNIDADE ESCREVE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        pergunta(c, "não decore: LEIA A UNIDADE", W / 2, 240, aa, BLUE, 38)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        u = ep(t, C["07.b"] + 0.6, 1.2)
        rrect(c, 260, 320, 700, 300, 26, "#FFFFFF", ab, shadow=True)
        barra(c, "km", "h", 610, 470, 96, ab, u)
        text(c, "quilômetro POR hora  =  quilômetro ÷ hora", 610, 680, 30, "black", INK, ab)
        regra(c, "a BARRA da unidade é um sinal de DIVIDIR", 610, 760, ep(t, C["07.b"] + 2.4, 0.4), 30)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        for k, (n_, d_, s_) in enumerate((("g", "cm³", "massa ÷ volume"), ("L", "min", "volume ÷ tempo"))):
            a = ep(t, C["07.c"] + k * 2.0, 0.4)
            y = 360 + k * 170
            rrect(c, 1020, y - 70, 640, 140, 22, "#F7F7F5", a)
            barra(c, n_, d_, 1160, y, 50, a, ep(t, C["07.c"] + k * 2.0 + 0.3, 0.8))
            text_mid(c, "= " + s_, 1470, y, 32, "black", INK, a)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1020, 640, 640, 130, "HÁBITO", ["unidade ao lado de cada número"], ad, 30)


# ======================================================================
# bloco c — as três perguntas
# ======================================================================

def b_perguntas(c, t, C, B):
    head_seq(c, t, C, [("08", "PERGUNTA 1", "ACHAR A TAXA → DIVIDA", PURPLE),
                       ("09", "PERGUNTA 2", "ACHAR O NUMERADOR → MULTIPLIQUE", PURPLE),
                       ("10", "PERGUNTA 3", "ACHAR O DENOMINADOR → DIVIDA AO CONTRÁRIO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10"])
    TX, TY, TS = 540, 560, 520
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        foco = "bl" if t >= C["08.b"] else None
        triangulo(c, TX, TY, TS, aa, "km", "km/h", "h", foco,
                  valores={"top": "160 km", "br": "2 h"} if t >= C["08.b"] else None)
        if aa > 0:
            text(c, "TRIÂNGULO DA TAXA", TX, 225, 30, "black", PURPLE, aa)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            linha(c, [("160 km", BLUE), (" em ", INK), ("2 h", GREEN), ("  →  ? km/h", AMBER)], 1300, 330, 44, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            fr(c, "160 km", "2 h", 1130, 500, 60, INK, acc, num_col=BLUE, den_col=GREEN)
            linha(c, [("=  ", INK), ("80 km/h", PURPLE)], 1440, 520, 60, ep(t, C["08.c"] + 2.4, 0.4))
            regra(c, "TAXA: DIVIDA", 1300, 700, acc, 40)
        return
    if sid == "09":
        aa = ep(t, C["09"], 0.4)
        triangulo(c, TX, TY, TS, aa, "km", "km/h", "h", "top", valores={"bl": "80 km/h", "br": "3 h"})
        ab = ep(t, C["09.a"], 0.5)
        if ab > 0:
            linha(c, [("80 km/h", PURPLE), (" durante ", INK), ("3 h", GREEN), ("  →  ? km", AMBER)], 1300, 330, 44, ab)
        acc = ep(t, C["09.b"], 0.5)
        if acc > 0:
            linha(c, [("80 km/h × 3 h = ", INK), ("240 km", BLUE)], 1300, 510, 56, acc)
            regra(c, "NUMERADOR: MULTIPLIQUE", 1300, 700, acc, 40)
        return
    aa = ep(t, C["10"], 0.4)
    triangulo(c, TX, TY, TS, aa, "km", "km/h", "h", "br", valores={"top": "240 km", "bl": "80 km/h"})
    ab = ep(t, C["10.a"], 0.5)
    if ab > 0:
        linha(c, [("240 km", BLUE), (" a ", INK), ("80 km/h", PURPLE), ("  →  ? h", AMBER)], 1300, 330, 44, ab)
    acc = ep(t, C["10.b"], 0.5)
    if acc > 0:
        fr(c, "240 km", "80 km/h", 1120, 500, 56, INK, acc, num_col=BLUE, den_col=PURPLE)
        linha(c, [("=  ", INK), ("3 h", GREEN)], 1420, 520, 60, ep(t, C["10.b"] + 2.8, 0.4))
        regra(c, "DENOMINADOR: DIVIDA AO CONTRÁRIO", 1300, 700, acc, 36)


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DEIXE A UNIDADE SE CANCELAR", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 120, "ATALHO", ["faça a conta com as UNIDADES: o que sobra é a resposta"], aa, 36)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        y = 450
        fr(c, "km", "h", 560, y - 14, 64, INK, ab, num_col=BLUE, den_col=RED)
        text_mid(c, "×", 720, y, 64, "black", INK, ab)
        text_mid(c, "h", 820, y, 64, "black", RED, ab)
        st = ep(t, C["11.b"] + 1.6, 0.4)
        if st > 0:
            strike(c, 535, y + 70, 590, y + 20, st, RED, st)
            strike(c, 795, y + 25, 850, y - 25, st, RED, st)
        linha(c, [("=  ", INK), ("km", BLUE)], 1000, y, 64, ep(t, C["11.b"] + 2.4, 0.4))
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        y = 640
        text_mid(c, "km", 470, y, 60, "black", BLUE, acc)
        text_mid(c, "÷", 580, y, 60, "black", INK, acc)
        fr(c, "km", "h", 690, y - 14, 60, INK, acc, num_col=BLUE, den_col=GREEN)
        st = ep(t, C["11.c"] + 1.8, 0.4)
        if st > 0:
            strike(c, 435, y + 25, 505, y - 25, st, RED, st)
            strike(c, 655, y - 20, 725, y - 70, st, RED, st)
        linha(c, [("=  ", INK), ("h", GREEN)], 880, y, 60, ep(t, C["11.c"] + 2.6, 0.4))
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        conferido(c, "sobrou a unidade pedida?", 1150, 470, ad, True, 36)
        conferido(c, "a conta está certa", 1150, 560, ad, True, 36)


# ======================================================================
# bloco d — a taxa não muda com a quantidade
# ======================================================================

def b_constante(c, t, C, B):
    head_seq(c, t, C, [("12", "DOBROU O TEMPO", "A TAXA DOBRA?", BLUE), ("13", "E A DENSIDADE?", "A MESMA ÁGUA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        for k, (d_, t_) in enumerate((("80 km", "1 h"), ("160 km", "2 h"))):
            a = ep(t, C["12.a"] + k * 1.6, 0.4)
            if a <= 0:
                continue
            y = 330 + k * 190
            g = (k + 1) / 2
            rrect(c, 230, y - 22, 720 * g, 44, 12, mix("#FFFFFF", BLUE, 0.3), a)
            text(c, d_ + " em " + t_, 230 + 720 * g + 30, y + 14, 38, "black", INK, a, align="left")
            linha(c, [("→  80 km/h", PURPLE)], 1500, y, 44, ep(t, C["12.a"] + k * 1.6 + 0.8, 0.4))
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            pill(c, "distância × 2  ·  tempo × 2  →  taxa IGUAL", W / 2, 580, PURPLE, size=30, a=ab, anchor="center")
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            pacote(c, 560, 720, 120, 150, acc, "1 kg", "R$ 4,50")
            pacote(c, 760, 715, 170, 170, acc, "10 kg", "R$ 45")
            regra(c, "o PREÇO DO QUILO não muda: R$ 4,50/kg", 1300, 720, acc, 34, GREEN)
        return
    for k, (cue, nome, g, v, w_, h_) in enumerate((("13.a", "COPO", "200 g", "200 cm³", 120, 160),
                                                    ("13.b", "GARRAFA", "1 000 g", "1 000 cm³", 150, 300))):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 420 + k * 560
        yb = 600
        rrect(c, x - w_ / 2, yb - h_, w_, h_, 16, mix("#FFFFFF", AGUA, 0.25), a)
        rrect(c, x - w_ / 2, yb - h_ * 0.85, w_, h_ * 0.85, 16, AGUA, a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w_ / 2, yb - h_, w_, h_), 16, 16),
                    paint("#6E95C2", a, stroke=4))
        text(c, nome, x, 280, 30, "black", BLUE, a)
        fr(c, g, v, x, 680, 40, INK, a, num_col=BLUE, den_col=GREEN)
        text(c, "= 1 g/cm³", x, 790, 40, "black", PURPLE, ep(t, C[cue] + 1.8, 0.4))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 1240, 330, 420, 300, 24, mix("#FFFFFF", BLUE, 0.08), acc)
        text(c, "quantidade mudou", 1450, 400, 32, "black", INK2, acc)
        text(c, "densidade NÃO", 1450, 460, 40, "black", PURPLE, acc)
        text(c, "identifica o MATERIAL", 1450, 540, 32, "black", BLUE, acc)
        text(c, "(você viu em Química)", 1450, 590, 24, "bold", GRAY, acc)


# ======================================================================
# bloco e — as outras taxas
# ======================================================================

TAXAS = [("14.a", "Rendimento", "distância ÷ combustível", "km/L"),
         ("14.b", "Concentração", "massa ÷ volume", "g/L"),
         ("14.c", "Densidade demográfica", "habitantes ÷ área", "hab/km²"),
         ("14.d", "Produtividade", "colheita ÷ área", "sacas/ha"),
         ("15.a", "Preço unitário", "preço ÷ quantidade", "R$/kg"),
         ("15.b", "Pressão", "força ÷ área", "N/m²"),
         ("15.c", "Natalidade", "nascimentos ÷ população", "por mil hab.")]


def b_outras(c, t, C, B):
    head(c, t, B["start"], "A PROVA INVENTA OUTRAS", "TODAS COM A MESMA FORMA", BLUE)
    card(c, *CARD_R)
    for k, (cue, nome, razao, unid) in enumerate(TAXAS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 225 + k * 76 + d
        rrect(c, 200, y, 1520, 64, 14, "#F7F7F5" if k % 2 else "#FFFFFF", a)
        text(c, nome, 230, y + 44, 32, "black", BLUE, a, align="left")
        text(c, razao, 1010, y + 44, 30, "bold", INK2, a)
        pill(c, unid, 1560, y + 32, PURPLE, size=26, a=a, anchor="center")
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        selo(c, 1440, 790, ad, "7 NOMES · 1 DIVISÃO", GREEN, -3, 36)


# ======================================================================
# bloco f — a taxa serve para comparar
# ======================================================================

def b_comparar(c, t, C, B):
    head(c, t, B["start"], "QUAL CIDADE É MAIS APERTADA?", "COMPARE PELA TAXA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["16"], 0.5)
    aa = ep(t, C["16.a"], 0.5)
    cidade(c, 230, 300, 560, 380, a0, 110, 3, BLUE)
    cidade(c, 900, 430, 180, 130, a0, 42, 5, AMBER)
    if a0 > 0:
        text(c, "1 000 000 hab", 510, 270, 34, "black", BLUE, a0)
        text(c, "200 000 hab", 990, 400, 30, "black", AMBER, a0)
    if aa > 0:
        text(c, "500 km²", 510, 730, 34, "black", INK2, aa)
        text(c, "50 km²", 990, 610, 30, "black", INK2, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        linha(c, [("1 000 000 ÷ 500 = ", INK), ("2 000 hab/km²", BLUE)], 1420, 380, 34, ab)
        linha(c, [("200 000 ÷ 50 = ", INK), ("4 000 hab/km²", AMBER)], 1420, 470, 34, ep(t, C["16.b"] + 2.6, 0.4))
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        selo(c, 1420, 590, acc, "A MENOR É A MAIS APERTADA", AMBER, -3, 30)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        regra(c, "quantidades diferentes: compare pela TAXA", W / 2, 790, ad, 34, GREEN)


# ======================================================================
# bloco g — valores de referência
# ======================================================================

REFS = [("Caminhada", "5 km/h"), ("Carro na rodovia", "100 km/h"), ("Rendimento de carro", "10 a 15 km/L"),
        ("Torneira comum", "12 L/min"), ("Consumo por pessoa", "150 L/dia"), ("Densidade da água", "1 g/cm³")]


def b_referencia(c, t, C, B):
    head(c, t, B["start"], "VALORES DE REFERÊNCIA", "O DETECTOR DE ERRO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        text(c, "VALOR DE REFERÊNCIA = número típico do mundo real", W / 2, 240, 34, "black", BLUE, aa)
    ab = ep(t, C["17.b"], 0.5)
    for k, (nome, val) in enumerate(REFS):
        a = ab * ep(t, C["17.b"] + k * 0.5, 0.4)
        if a <= 0:
            continue
        x = 220 + (k % 2) * 760
        y = 300 + (k // 2) * 120
        rrect(c, x, y, 720, 96, 18, "#F7F7F5", a)
        text(c, nome, x + 30, y + 60, 32, "bold", INK2, a, align="left")
        text(c, val, x + 690, y + 60, 36, "black", GREEN, a, align="right")
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        rrect(c, 420, 680, 1080, 120, 22, mix("#FFFFFF", RED, 0.10), acc)
        check_icon(c, 490, 740, 28, acc, RED, "x")
        linha(c, [("carro a ", INK), ("500 km/h", RED), ("?", INK)], 790, 740, 44, acc)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        selo(c, 1300, 740, ad, "UNIDADE TROCADA!", RED, -4, 36)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "REAIS POR QUILO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    pacote(c, 420, 420, 220, 300, aa, "5 kg", "R$ 22,50")
    ab = ep(t, C["18.b"], 0.5)
    pacote(c, 760, 450, 170, 240, ab, "2 kg", "R$ 9,60")
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0 and t < C["19"]:
        text(c, "qual é mais barato POR QUILO?", 1340, 330, 36, "black", INK, acc)
    pause_timer(c, t, C["18.end"] - 1.9, 1340, 520)
    if t < C["19"]:
        return
    a1 = ep(t, C["19.a"], 0.4)
    if a1 > 0:
        rrect(c, 1060, 240, 560, 140, 24, "#FFFFFF", a1, shadow=True)
        barra(c, "R$", "kg", 1340, 310, 54, a1, ep(t, C["19.a"] + 0.6, 0.8))
        text(c, "a barra manda: reais ÷ quilos", 1340, 420, 28, "black", PURPLE, a1)
    ab2 = ep(t, C["19.b"], 0.5)
    if ab2 > 0:
        linha(c, [("22,50 ÷ 5 = ", INK), ("R$ 4,50/kg", GREEN)], 1340, 510, 40, ab2)
    acc2 = ep(t, C["19.c"], 0.5)
    if acc2 > 0:
        linha(c, [("9,60 ÷ 2 = ", INK), ("R$ 4,80/kg", RED)], 1340, 590, 40, acc2)
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0:
        selo(c, 420, 640, ad, "MAIS BARATO POR kg", GREEN, -5, 30)
        text(c, "mesmo custando mais no caixa", 1340, 700, 30, "bold", GRAY, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["A barra da unidade é um sinal de dividir.",
          "Taxa: divida. Numerador: multiplique. Denominador: divida ao contrário.",
          "A taxa não muda com a quantidade."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Decorar três fórmulas diferentes", "cada assunto ganha a sua fórmula: parece mais seguro",
          "é o triplo de coisa para lembrar: leia a UNIDADE, ela é a fórmula"),
         ("Comparar embalagens pelo preço total", "R$ 9,60 é bem menos que R$ 22,50",
          "os pacotes têm tamanhos diferentes: compare o PREÇO POR QUILO"),
         ("Aceitar um resultado absurdo sem conferir", "a conta foi feita com cuidado",
          "carro a 500 km/h denuncia unidade trocada: compare com os VALORES DE REFERÊNCIA")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questão 8 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS8 = [("A", "8 km/L", "abaixo da faixa", RED), ("B", "10 km/L", "35 × 10 = 350 km", RED), ("C", "12 km/L", "", GREEN),
         ("D", "14 km/L", "35 × 14 = 490 km", RED), ("E", "15 km/L", "35 × 15 = 525 km", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · EU FAÇO", "RENDIMENTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Um automóvel percorreu 420 quilômetros consumindo 35 litros de combustível. O rendimento "
                           "médio desse veículo foi de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS8, 1000, 250, 680, 44, C["25.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 140)
    if C["25"] <= t < C["26"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        linha(c, [("420 km", BLUE), ("  ·  ", INK), ("35 L", GREEN)], 540, y0 + 50, 34, ep(t, C["25"], 0.4))
        pill(c, "pede km/L → TAXA → divida", 540, y0 + 115, PURPLE, size=24, a=ep(t, C["25.a"], 0.4), anchor="center")
        ab = ep(t, C["25.b"], 0.4)
        if ab > 0:
            fr(c, "420 km", "35 L", 400, y0 + 200, 40, INK, ab, num_col=BLUE, den_col=GREEN)
            linha(c, [("= ", INK), ("12 km/L", PURPLE)], 680, y0 + 216, 44, ep(t, C["25.b"] + 2.4, 0.4))
        conferido(c, "referência: 10 a 15 km/L", 230, y0 + 330, ep(t, C["25.c"], 0.4), True, 28)
    if t >= C["26"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["26"], 0.4))
        aa = ep(t, C["26.a"], 0.4)
        if aa > 0:
            # faixa de referência 10–15 com as alternativas
            x0, x1, yb = 230, 850, y0 + 90
            line(c, x0, yb, x1, yb, INK2, aa, 4)
            xr = lambda v: lerp(x0, x1, (v - 6) / 11)
            rrect(c, xr(10), yb - 16, xr(15) - xr(10), 32, 10, mix("#FFFFFF", GREEN, 0.4), aa)
            for v, L in ((8, "A"), (10, "B"), (12, "C"), (14, "D"), (15, "E")):
                c.drawCircle(xr(v), yb, 9, paint(RED if v == 8 else INK, aa))
                text(c, L, xr(v), yb - 26, 22, "black", INK2, aa)
            text(c, "faixa 10 a 15: B, C, D e E estão DENTRO", 540, yb + 60, 24, "black", AMBER, aa)
        ab = ep(t, C["26.b"], 0.4)
        if ab > 0:
            K.atalho(c, 210, y0 + 190, 660, 110, "ATALHO", ["multiplique de volta: 35 L × taxa = 420 km?"], ab, 26)
        acc = ep(t, C["26.c"], 0.4)
        if acc > 0:
            linha(c, [("35 L × 12 km/L = ", INK), ("420 km", GREEN)], 540, y0 + 350, 30, acc)


def b_mais(c, t, C, B):
    head_seq(c, t, C, [("27", "O MESMO RENDIMENTO", "ACHAR O NUMERADOR", PURPLE), ("28", "VOCÊ FAZ", "PAUSE E RESOLVA", GREEN),
                       ("29", "CONFERINDO", "ACHAR O DENOMINADOR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["27", "28", "29"])
    TX, TY, TS = 520, 520, 540
    if sid == "27":
        a0 = ep(t, C["27"], 0.4)
        triangulo(c, TX, TY, TS, a0, "km", "km/L", "L", "top", valores={"bl": "12 km/L", "br": "50 L"})
        aa = ep(t, C["27.a"], 0.5)
        if aa > 0:
            linha(c, [("50 L", GREEN), ("  →  ? km", AMBER)], 1300, 300, 50, aa)
        ab = ep(t, C["27.b"], 0.5)
        if ab > 0:
            linha(c, [("12 km/L × 50 L = ", INK), ("600 km", BLUE)], 1300, 470, 52, ab)
        acc = ep(t, C["27.c"], 0.5)
        if acc > 0:
            y = 640
            fr(c, "km", "L", 1150, y - 14, 50, INK, acc, num_col=BLUE, den_col=RED)
            text_mid(c, "×", 1240, y, 50, "black", INK, acc)
            text_mid(c, "L", 1320, y, 50, "black", RED, acc)
            linha(c, [("=  ", INK), ("km", BLUE)], 1450, y, 50, acc)
            st = ep(t, C["27.c"] + 1.0, 0.4)
            if st > 0:
                strike(c, 1130, y + 50, 1170, y + 10, st, RED, st)
                strike(c, 1300, y + 22, 1340, y - 22, st, RED, st)
        return
    if sid == "28":
        a0 = ep(t, C["28"], 0.4)
        triangulo(c, TX, TY, TS, a0, "km", "km/L", "L", "br", valores={"top": "300 km", "bl": "12 km/L"})
        aa = ep(t, C["28.a"], 0.5)
        if aa > 0:
            linha(c, [("300 km", BLUE), ("  →  ? L", AMBER)], 1300, 300, 50, aa)
        pause_timer(c, t, C["28.end"] - 1.9, 1300, 520)
        return
    a0 = ep(t, C["29"], 0.4)
    triangulo(c, TX, TY, TS, a0, "km", "km/L", "L", "br", valores={"top": "300 km", "bl": "12 km/L"})
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        fr(c, "300 km", "12 km/L", 1150, 300, 50, INK, aa, num_col=BLUE, den_col=PURPLE)
        linha(c, [("=  ", INK), ("25 L", GREEN)], 1450, 316, 56, ep(t, C["29.a"] + 3.0, 0.4))
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        pill(c, "o km cancela: sobra L", 1300, 490, PURPLE, size=28, a=ab, anchor="center")
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        linha(c, [("12 km/L × 25 L = ", INK), ("300 km", BLUE)], 1300, 620, 42, acc)
        conferido(c, "bateu", 1200, 730, ep(t, C["29.c"] + 2.4, 0.4), True, 34)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "VELOCIDADE MÉDIA", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        g = ep(t, C["31.a"] + 0.4, 2.0)
        line(c, 260, 400, 1660, 400, "#C9CED6", aa, 10)
        x = lerp(260, 1600, g)
        rrect(c, x - 70, 350, 140, 60, 14, BLUE, aa)
        rrect(c, x - 50, 362, 40, 26, 6, "#DCE6FF", aa)
        rrect(c, x + 10, 362, 40, 26, 6, "#DCE6FF", aa)
        linha(c, [("180 km", BLUE), ("  em  ", INK), ("2 h 30 min", GREEN)], W / 2, 500, 56, aa)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 580, 800, 120, 24, mix("#FFFFFF", RED, 0.10), ab)
        linha(c, [("180 ÷ 2,30", RED)], W / 2, 640, 56, ab)
        strike(c, 760, 640, 1160, 640, ep(t, C["31.b"] + 1.6, 0.4), RED, 1)
        selo(c, 1440, 650, ep(t, C["31.b"] + 1.6, 0.4), "ERROU", RED, -6, 40)
    pill(c, "ep. 2 · velocidade média", W / 2, 790, PURPLE, size=30, a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Qual taxa você usa no seu dia a dia?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              unidade=b_unidade, perguntas=b_perguntas, atalho=b_atalho, constante=b_constante, outras=b_outras,
              comparar=b_comparar, referencia=b_referencia, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q8=b_q8, mais=b_mais, ponte=b_ponte, cta=b_cta)
