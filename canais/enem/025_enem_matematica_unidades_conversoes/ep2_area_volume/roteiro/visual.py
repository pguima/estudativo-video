"""Visual — Unidades de Medida e Conversões, Episódio 2: área e volume, litro e metro cúbico (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, selo...).
Peças deste episódio: escada() (degraus de unidades com setas × n), grade() (quadrado n × n enchendo fileira por fileira),
_iso/_caixa (cubo de cubinhos isométrico, copiado do 020/ep5), caixa_leite(), tanque(), balanca() com garrafa, campo().
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
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_unidades_ep2_area_volume.mp4"
CARD_R = K.CARD_R
AZULEJO = "#F4E6C8"
AGUA = "#5FA8E8"
LEITE = "#FBFBF6"
CUBO_TOPO, CUBO_FRENTE, CUBO_LADO = "#C9DEF8", "#9CC3F0", "#7AAAE0"
GRAMA, GRAMA_ESC = "#7CC47F", "#5DAA61"


# ======================================================================
# peças do episódio
# ======================================================================

def mil(n):
    """10000 -> '10 000'"""
    return f"{int(round(n)):,}".replace(",", " ")


def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)]"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def contador(c, cx, cy, valor, a, rotulo, col=None, size=72, w=340):
    if a <= 0:
        return
    col = col or BLUE
    card(c, cx - w / 2, cy - 90, w, 190, a)
    text_mid(c, mil(valor), cx, cy - 10, size, "black", col, a)
    text(c, rotulo, cx, cy + 70, 26, "black", INK2, a)


def escada(c, x0, y0, labels, a, ativos=None, setas=None, rot="× 10", passo_x=200, passo_y=46, w=170, h=84, size=40,
           col_seta=None):
    """degraus que DESCEM da esquerda para a direita; ativos = {i: 0..1} destaca o degrau; setas = {i: alfa} (do i ao i+1)"""
    if a <= 0:
        return
    col_seta = col_seta or GREEN
    ativos = ativos or {}
    for i, lab in enumerate(labels):
        x, y = x0 + i * passo_x, y0 + i * passo_y
        hl = ativos.get(i, 0.0)
        rrect(c, x, y, w, h, 16, mix("#FFFFFF", PURPLE, 0.12 * hl), a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16),
                    paint(mix("#D9D9D4", PURPLE, hl), a, stroke=3))
        text_mid(c, lab, x + w / 2, y + h / 2, size, "black", mix(INK, PURPLE, hl), a)
    for i, sa in (setas or {}).items():
        if sa <= 0 or i + 1 >= len(labels):
            continue
        x, y = x0 + i * passo_x, y0 + i * passo_y
        arrow(c, x + w * 0.55, y - 14, x + passo_x + w * 0.45, y + passo_y - 14, col_seta, a * sa, 5, 14, progress=sa)
        text(c, rot, x + w * 0.5 + passo_x / 2, y - 26, 28, "black", col_seta, a * sa)


def grade(c, x, y, s, n, cells, a, col=None, linhas=True, borda=4):
    """quadrado de lado s dividido em n × n; `cells` quadradinhos pintados, fileira por fileira (de cima para baixo)"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, s, s, 4, "#FFFFFF", a, shadow=True)
    cel = s / n
    rows = int(cells // n)
    rest = cells - rows * n
    if rows > 0:
        c.drawRect(skia.Rect.MakeXYWH(x, y, s, rows * cel), paint(mix("#FFFFFF", col, 0.40), a))
    if rest > 0 and rows < n:
        c.drawRect(skia.Rect.MakeXYWH(x, y + rows * cel, rest * cel, cel), paint(mix("#FFFFFF", col, 0.70), a))
    if linhas:
        pg = paint("#BFCDE0", a * 0.9, stroke=0.8 if n > 30 else 2)
        for k in range(1, n):
            c.drawLine(x + k * cel, y, x + k * cel, y + s, pg)
            c.drawLine(x, y + k * cel, x + s, y + k * cel, pg)
    c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), paint(INK, a, stroke=borda))


def cota_h(c, x0, x1, y, s, a, col=None, size=28):
    if a <= 0:
        return
    col = col or INK2
    line(c, x0, y, x1, y, col, a, 3); line(c, x0, y - 10, x0, y + 10, col, a, 3); line(c, x1, y - 10, x1, y + 10, col, a, 3)
    text(c, s, (x0 + x1) / 2, y - 16, size, "black", col, a)


def cota_v(c, x, y0, y1, s, a, col=None, size=28):
    if a <= 0:
        return
    col = col or INK2
    line(c, x, y0, x, y1, col, a, 3); line(c, x - 10, y0, x + 10, y0, col, a, 3); line(c, x - 10, y1, x + 10, y1, col, a, 3)
    text(c, s, x + 22, (y0 + y1) / 2 + 10, size, "black", col, a, align="left")


def _iso(cx, cy, s, x, y, z):
    """projeção isométrica: x para a direita-baixo, z para a esquerda-baixo, y para cima (0..1)"""
    return cx + (x - z) * s * 0.866, cy + (x + z) * s * 0.5 - y * s


def _poly(c, pts, col, a, stroke=None):
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    c.drawPath(p, paint(col, a, stroke=stroke) if stroke else paint(col, a))


def caixa_iso(c, cx, cy, s, X, Y, Z, a, cores=(CUBO_TOPO, CUBO_FRENTE, CUBO_LADO), div=10, borda=None):
    """paralelepípedo [0,X]×[0,Y]×[0,Z] (frações do cubo) com faces visíveis e as linhas dos cubinhos (div por aresta)"""
    if a <= 0 or X <= 0 or Y <= 0 or Z <= 0:
        return
    P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
    top = [P(0, Y, 0), P(X, Y, 0), P(X, Y, Z), P(0, Y, Z)]
    front = [P(0, 0, Z), P(X, 0, Z), P(X, Y, Z), P(0, Y, Z)]
    side = [P(X, 0, 0), P(X, 0, Z), P(X, Y, Z), P(X, Y, 0)]
    _poly(c, top, cores[0], a); _poly(c, front, cores[1], a); _poly(c, side, cores[2], a)
    if div:
        pg = paint("#FFFFFF", a * 0.6, stroke=1.4)
        st = 1.0 / div
        k = st
        while k < X - 1e-6:
            c.drawLine(*P(k, 0, Z), *P(k, Y, Z), pg); c.drawLine(*P(k, Y, 0), *P(k, Y, Z), pg); k += st
        k = st
        while k < Y - 1e-6:
            c.drawLine(*P(0, k, Z), *P(X, k, Z), pg); c.drawLine(*P(X, k, 0), *P(X, k, Z), pg); k += st
        k = st
        while k < Z - 1e-6:
            c.drawLine(*P(X, 0, k), *P(X, Y, k), pg); c.drawLine(*P(0, Y, k), *P(X, Y, k), pg); k += st
    bc = borda or "#3E6FA8"
    for poly in (top, front, side):
        _poly(c, poly, bc, a, stroke=2.5)


def cubo_vazio(c, cx, cy, s, a, col=None):
    if a <= 0:
        return
    P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
    pe = paint(col or GRAY, a * 0.85, stroke=2.5)
    pe.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
    cs = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)]
    for i, j in [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]:
        c.drawLine(*P(*cs[i]), *P(*cs[j]), pe)


def caixa_leite(c, cx, base_y, w, h, a, rot="1 L"):
    """caixa de leite longa-vida (de frente): corpo alto, topo em telhado, rótulo azul"""
    if a <= 0:
        return
    x = cx - w / 2
    top = base_y - h
    rrect(c, x, top, w, h, 6, LEITE, a, shadow=True)
    p = skia.Path(); p.moveTo(x, top + 2); p.lineTo(cx, top - w * 0.32); p.lineTo(x + w, top + 2); p.close()
    c.drawPath(p, paint("#ECEBE3", a)); c.drawPath(p, paint("#B8B8AE", a, stroke=2.5))
    rrect(c, cx - w * 0.18, top - w * 0.42, w * 0.36, w * 0.12, 3, "#DADAD0", a)
    rrect(c, x, top + h * 0.30, w, h * 0.36, 0, BLUE, a * 0.9)
    text_mid(c, "LEITE", cx, top + h * 0.42, w * 0.2, "black", "#FFFFFF", a)
    text_mid(c, rot, cx, top + h * 0.57, w * 0.24, "black", "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, top, w, h), 6, 6), paint("#B8B8AE", a, stroke=2.5))


def tanque(c, cx, y_top, w, h, a, nivel=1.0, rotulo="1 000 L"):
    """caixa-d'água (de frente, levemente em perspectiva) com nível de água 0..1"""
    if a <= 0:
        return
    rx, ry = w / 2, w * 0.14
    c.drawRect(skia.Rect.MakeXYWH(cx - rx, y_top, w, h), paint("#E9EEF4", a))
    if nivel > 0:
        hy = y_top + h * (1 - nivel)
        c.drawRect(skia.Rect.MakeXYWH(cx - rx, hy, w, y_top + h - hy), paint(AGUA, a * 0.85))
        c.drawOval(skia.Rect.MakeXYWH(cx - rx, hy - ry, w, 2 * ry), paint(mix(AGUA, "#FFFFFF", 0.3), a))
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top + h - ry, w, 2 * ry), paint(AGUA if nivel > 0 else "#E9EEF4", a))
    pe = paint("#5B6B7D", a, stroke=4)
    c.drawLine(cx - rx, y_top, cx - rx, y_top + h, pe); c.drawLine(cx + rx, y_top, cx + rx, y_top + h, pe)
    c.drawArc(skia.Rect.MakeXYWH(cx - rx, y_top + h - ry, w, 2 * ry), 0, 180, False, pe)
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top - ry, w, 2 * ry), paint("#CFD8E2", a))
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top - ry, w, 2 * ry), pe)
    if rotulo:
        rrect(c, cx - 105, y_top + h * 0.40, 210, 64, 14, "#FFFFFF", a * 0.95)
        text_mid(c, rotulo, cx, y_top + h * 0.40 + 32, 34, "black", INK, a)


def garrafa(c, cx, base_y, h, a, rot="1 L"):
    """garrafa de água (de frente)"""
    if a <= 0:
        return
    w = h * 0.36
    body = skia.Rect.MakeXYWH(cx - w / 2, base_y - h * 0.72, w, h * 0.72)
    c.drawRRect(skia.RRect.MakeRectXY(body, w * 0.22, w * 0.22), paint(mix(AGUA, "#FFFFFF", 0.35), a))
    p = skia.Path()
    p.moveTo(cx - w / 2, base_y - h * 0.66); p.lineTo(cx - w * 0.17, base_y - h * 0.86); p.lineTo(cx - w * 0.17, base_y - h * 0.94)
    p.lineTo(cx + w * 0.17, base_y - h * 0.94); p.lineTo(cx + w * 0.17, base_y - h * 0.86); p.lineTo(cx + w / 2, base_y - h * 0.66)
    p.close()
    c.drawPath(p, paint(mix(AGUA, "#FFFFFF", 0.5), a))
    rrect(c, cx - w * 0.2, base_y - h, w * 0.4, h * 0.07, 3, BLUE, a)
    c.drawRRect(skia.RRect.MakeRectXY(body, w * 0.22, w * 0.22), paint("#3E6FA8", a, stroke=2.5))
    c.drawPath(p, paint("#3E6FA8", a, stroke=2.5))
    rrect(c, cx - w / 2, base_y - h * 0.48, w, h * 0.18, 0, "#FFFFFF", a * 0.9)
    text_mid(c, rot, cx, base_y - h * 0.39, h * 0.11, "black", BLUE, a)


def balanca(c, cx, base_y, a, visor="1,000 kg", visor_a=1.0, w=360):
    """balança de cozinha: prato em cima, corpo com visor digital"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, base_y - 110, w, 110, 22, "#E8ECEF", a, shadow=True)
    rrect(c, cx - w * 0.58, base_y - 132, w * 1.16, 24, 12, "#C7CED6", a)
    rrect(c, cx - 110, base_y - 82, 220, 60, 10, "#2E3B33", a)
    if visor_a > 0:
        text_mid(c, visor, cx, base_y - 52, 34, "black", "#8EF0A8", a * visor_a)


def campo(c, x, y, w, h, a):
    """campo de futebol visto de cima"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 6, GRAMA, a, shadow=True)
    for k in range(6):
        if k % 2:
            c.drawRect(skia.Rect.MakeXYWH(x + k * w / 6, y, w / 6, h), paint(GRAMA_ESC, a * 0.35))
    pe = paint("#FFFFFF", a, stroke=3)
    c.drawRect(skia.Rect.MakeXYWH(x + 8, y + 8, w - 16, h - 16), pe)
    c.drawLine(x + w / 2, y + 8, x + w / 2, y + h - 8, pe)
    c.drawCircle(x + w / 2, y + h / 2, h * 0.16, pe)
    c.drawRect(skia.Rect.MakeXYWH(x + 8, y + h * 0.3, w * 0.12, h * 0.4), pe)
    c.drawRect(skia.Rect.MakeXYWH(x + w - 8 - w * 0.12, y + h * 0.3, w * 0.12, h * 0.4), pe)


def piscina(c, x, y, w, h, a):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, "#E6EEF5", a, shadow=True)
    rrect(c, x + 12, y + 12, w - 24, h - 24, 6, AGUA, a * 0.8)
    for k in range(1, 4):
        line(c, x + 12, y + 12 + k * (h - 24) / 4, x + w - 12, y + 12 + k * (h - 24) / 4, "#FFFFFF", a * 0.6, 2)


def piso(c, x, y, cols, rows, s, a):
    for i in range(cols):
        for j in range(rows):
            rrect(c, x + i * s, y + j * s, s - 5, s - 5, 5, mix(AZULEJO, "#FFFFFF", 0.35 * ((i + j) % 2)), a)


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    text(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "ÁREA E VOLUME", BLUE)
    acc = ep(t, C["01.c"], 0.5)
    for k, (cue, s) in enumerate((("01.a", "1 m²  =  100 cm² ?"), ("01.b", "1 m³  =  1 litro ?"))):
        a, d = rise(t, C[cue])
        y = 380 + k * 200 + d
        rrect(c, 460, y - 80, 1000, 160, 26, "#FFFFFF", a, shadow=True)
        text_mid(c, s, W / 2, y, 84, "black", INK, a)
        if acc > 0:
            xa = ep(t, C["01.c"] + 0.3 * k, 0.4)
            check_icon(c, 1400, y - 26, 34, a * xa, RED, "x")
    if acc > 0:
        selo(c, W / 2, 850, acc, "OS DOIS ERROS MAIS CAROS", RED, -2, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "converter área e volume sem errar", "m², cm², hectare, m³, cm³"),
            ("02.b", "passar de metro cúbico para litro e para quilo de água", "m³ → L → kg")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


ESC7 = ["km", "hm", "dam", "m", "dm", "cm", "mm"]


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "A ESCADA DO EPISÓDIO 1", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    acc = ep(t, C["03.c"], 0.5)
    setas = {i: acc * ep(t, C["03.c"] + 0.25 * i, 0.4) for i in range(6)}
    escada(c, 250, 290, ESC7, aa, ativos={3: aa}, setas=setas, passo_x=210, passo_y=46, w=170)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        partes = [("K", PURPLE), ("átia ", INK2), ("H", PURPLE), ("oje ", INK2), ("D", PURPLE), ("ançou ", INK2),
                  ("M", PURPLE), ("uito, ", INK2), ("D", PURPLE), ("ançou ", INK2), ("C", PURPLE), ("om ", INK2),
                  ("M", PURPLE), ("arcos", INK2)]
        linha(c, partes, W / 2, 680, 44, ab)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        regra(c, "1 m = 10 dm = 100 cm", W / 2, 790, ad, 36)


# ======================================================================
# concreto e definições
# ======================================================================

def b_cotidiano(c, t, C, B):
    head(c, t, B["start"], "OLHE AO REDOR", "NEM TUDO SE MEDE COM RÉGUA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    piso(c, 230, 260, 4, 3, 70, aa)
    text(c, "piso", 370, 530, 30, "black", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    caixa_leite(c, 640, 500, 110, 210, ab)
    text(c, "caixa de leite", 640, 560, 30, "black", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    tanque(c, 920, 300, 200, 190, acc, 0.7, None)
    text(c, "caixa-d'água", 920, 560, 30, "black", INK2, acc)
    ad = ep(t, C["04.d"], 0.5)
    piscina(c, 1110, 320, 260, 170, ad)
    text(c, "piscina", 1240, 560, 30, "black", INK2, ad)
    campo(c, 1420, 320, 280, 175, ep(t, C["04.d"] + 0.8, 0.5))
    text(c, "campo", 1560, 560, 30, "black", INK2, ep(t, C["04.d"] + 0.8, 0.5))
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        chip(c, "largura × comprimento", 370, 680, BLUE, ae, 30)
        chip(c, "largura × comprimento × altura", 920, 680, PURPLE, ep(t, C["04.e"] + 2.0, 0.5), 30)


def b_defs(c, t, C, B):
    head_seq(c, t, C, [("05", "ÁREA", "QUANTO CHÃO COBRE", BLUE), ("06", "VOLUME", "QUANTO ESPAÇO OCUPA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        a0 = ep(t, C["05"], 0.5)
        chip(c, "ÁREA = o tamanho de uma superfície", 1240, 260, BLUE, a0, 32)
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            rrect(c, 330, 280, 360, 360, 4, mix("#FFFFFF", BLUE, 0.14), aa)
            c.drawRect(skia.Rect.MakeXYWH(330, 280, 360, 360), paint(INK, aa, stroke=4))
            cota_h(c, 330, 690, 266, "1 m", aa, INK2)
            cota_v(c, 712, 280, 640, "1 m", aa, INK2)
            text_mid(c, "1 m²", 510, 460, 84, "black", BLUE, aa)
            text(c, "metro quadrado: um quadrado de 1 m de lado", 1240, 380, 32, "black", INK, aa)
            text(c, "o 2 pequenininho: duas medidas multiplicadas", 1240, 430, 28, "bold", INK2, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            rrect(c, 1100, 560, 36, 36, 3, mix("#FFFFFF", BLUE, 0.45), ab)
            c.drawRect(skia.Rect.MakeXYWH(1100, 560, 36, 36), paint(INK, ab, stroke=2))
            text(c, "1 cm²", 1160, 590, 44, "black", BLUE, ab, align="left")
            text(c, "≈ do tamanho de uma unha", 1160, 650, 28, "bold", INK2, ab, align="left")
        return
    a0 = ep(t, C["06"], 0.5)
    chip(c, "VOLUME = o espaço que uma coisa ocupa", 1240, 260, BLUE, a0, 32)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        caixa_iso(c, 520, 520, 230, 1, 1, 1, aa, div=0)
        P = lambda x, y, z: _iso(520, 520, 230, x, y, z)
        x1, y1 = P(1, 0, 1); x2, y2 = P(1, 0, 0)
        line(c, x1 + 14, y1 + 8, x2 + 14, y2 + 8, AMBER, aa, 6)
        text(c, "aresta = 1 m", x2 + 30, (y1 + y2) / 2 + 40, 30, "black", AMBER, aa, align="left")
        text_mid(c, "1 m³", 300, 720, 60, "black", BLUE, aa)
        text(c, "metro cúbico: um cubo de 1 m de aresta", 1240, 380, 32, "black", INK, aa)
        text(c, "aresta = cada beirada do cubo", 1240, 430, 28, "bold", INK2, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        boxed(c, 940, 530, 600, 150, PURPLE, ab, 0.08)
        text(c, "CAPACIDADE = quanto cabe dentro", 1240, 590, 32, "black", PURPLE, ab)
        text(c, "medida em LITROS", 1240, 645, 30, "black", INK2, ab)


# ======================================================================
# bloco a — área: a grade 10 × 10
# ======================================================================

def b_grade(c, t, C, B):
    head(c, t, B["start"], "1 dm² TEM QUANTOS cm²?", "DESENHE O QUADRADO", AMBER)
    card(c, *CARD_R)
    gx, gy, gs = 300, 250, 480
    aa = ep(t, C["07.a"], 0.5)
    tb, tc = C["07.b"], C["07.c"]
    cells = 10 * clamp((t - tb) / 1.8)
    if t >= tc:
        cells = 10 + 90 * clamp((t - tc) / 2.6)
    grade(c, gx, gy, gs, 10, cells, aa, BLUE, borda=4)
    cota_h(c, gx, gx + gs, gy - 16, "1 dm = 10 cm", aa, BLUE)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        text(c, "1ª fileira: 10", gx + gs + 30, gy + 34, 30, "black", BLUE, ab, align="left")
    acc = ep(t, C["07.c"], 0.5)
    cota_v(c, gx + gs + 26, gy + 70, gy + gs, "10 fileiras", acc, AMBER)
    contador(c, 1420, 360, cells, ab, "quadradinhos de 1 cm²", GREEN if cells >= 99.5 else BLUE)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 1190, 520, 460, 100, 18, "#FFFFFF", ad, shadow=True)
        linha(c, [("10 × 10 = ", INK), ("100", GREEN)], 1420, 570, 52, ad)
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        regra(c, "ÁREA: cada degrau é uma grade 10 × 10  →  vale × 100", W / 2, 790, ae, 34)


def b_escada_area(c, t, C, B):
    head(c, t, B["start"], "A ESCADA DA ÁREA", "CADA DEGRAU VALE × 100", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.5)
    labs = ["m²", "dm²", "cm²", "mm²"]
    cues = ["08.a", "08.b", "08.c"]
    setas = {i: ep(t, C[cue], 0.5) for i, cue in enumerate(cues)}
    ativos = {0: a0}
    for i, cue in enumerate(cues):
        ativos[i + 1] = ep(t, C[cue], 0.5)
    escada(c, 260, 260, labs, a0, ativos=ativos, setas=setas, rot="× 100", passo_x=230, passo_y=60, w=180, size=44)
    vals = [("1 m²", "08"), ("= 100 dm²", "08.a"), ("= 10 000 cm²", "08.b"), ("= 1 000 000 mm²", "08.c")]
    for k, (s, cue) in enumerate(vals):
        a = ep(t, C[cue], 0.5)
        text(c, s, 1250, 290 + k * 62, 42, "black", INK if k == 0 else BLUE, a, align="left")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        linha(c, [("1 km² = 100 × 100 × 100 = ", INK2), ("1 000 000 m²", PURPLE)], 760, 640, 38, ad)
        text(c, "km² → hm² → dam² → m²: três degraus", 760, 700, 28, "bold", GRAY, ad)
    K.atalho(c, 1180, 590, 560, 170, "ATALHO", ["área: DOIS zeros por degrau"], ep(t, C["08.e"], 0.5), 34)


# ======================================================================
# bloco b — confirmação: 100 × 100
# ======================================================================

def b_confirma(c, t, C, B):
    head(c, t, B["start"], "ESQUECEU?", "CONFIRA SEM DECORAR", GREEN)
    card(c, *CARD_R)
    gx, gy, gs = 280, 230, 540
    aa = ep(t, C["09.a"], 0.5)
    tb = C["09.b"]
    cells = 100 * clamp((t - tb) / 1.6) + 9900 * clamp((t - tb - 2.0) / 3.0)
    grade(c, gx, gy, gs, 100, cells, aa, BLUE, borda=4)
    cota_h(c, gx, gx + gs, gy - 14, "1 m = 100 cm", aa, BLUE)
    ab = ep(t, C["09.b"], 0.5)
    cota_v(c, gx + gs + 26, gy + 20, gy + gs, "100 fileiras", ab, AMBER)
    contador(c, 1360, 360, cells, aa, "quadradinhos de 1 cm²", GREEN if cells >= 9999.5 else BLUE, w=420)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 1110, 520, 500, 100, 18, "#FFFFFF", acc, shadow=True)
        linha(c, [("100 × 100 = ", INK), ("10 000", GREEN)], 1360, 570, 50, acc)
    K.atalho(c, 1000, 650, 720, 150, "ATALHO", ["converta o LADO e multiplique lado × lado"], ep(t, C["09.d"], 0.5), 32)


# ======================================================================
# bloco c — hectare, are, campo de futebol
# ======================================================================

def b_hectare(c, t, C, B):
    head_seq(c, t, C, [("10", "NO CAMPO", "O HECTARE", BLUE), ("11", "UMA REFERÊNCIA", "O CAMPO DE FUTEBOL", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 270, 400, 400, 6, mix("#FFFFFF", GRAMA, 0.55), aa, shadow=True)
            c.drawRect(skia.Rect.MakeXYWH(260, 270, 400, 400), paint(GRAMA_ESC, aa, stroke=4))
            cota_h(c, 260, 660, 254, "100 m", aa, INK2)
            cota_v(c, 682, 270, 670, "100 m", aa, INK2)
            text_mid(c, "1 ha", 460, 470, 90, "black", "#2F6B33", aa)
            linha(c, [("1 hectare = 100 × 100 = ", INK), ("10 000 m²", BLUE)], 1250, 300, 40, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            text(c, "100 m = 1 hm  →  1 ha = 1 hm²", 1250, 380, 36, "black", PURPLE, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 270, 40, 40, 2, mix("#FFFFFF", AMBER, 0.6), acc)
            c.drawRect(skia.Rect.MakeXYWH(260, 270, 40, 40), paint(AMBER, acc, stroke=3))
            text(c, "1 are", 312, 302, 26, "black", AMBER, acc, align="left")
            linha(c, [("1 are = 10 × 10 = ", INK), ("100 m²", AMBER)], 1250, 480, 38, acc)
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            grade(c, 1080, 560, 210, 10, 100, ad, GRAMA, borda=3)
            text(c, "1 km²", 1185, 548, 26, "black", INK2, ad)
            text(c, "= 100 ha", 1320, 680, 46, "black", GREEN, ad, align="left")
        return
    aa = ep(t, C["11.a"], 0.5)
    campo(c, 260, 290, 560, 362, aa)
    cota_h(c, 260, 820, 274, "≈ 105 m", aa, INK2)
    cota_v(c, 842, 290, 652, "≈ 68 m", aa, INK2)
    if aa > 0:
        linha(c, [("105 × 68 ≈ ", INK), ("7 000 m²", BLUE)], 1340, 340, 44, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("≈ ", INK), ("0,7 hectare", GREEN)], 1340, 440, 52, ab)
    K.atalho(c, 1020, 560, 650, 170, "ATALHO", ["hectare → m²:  × 10 000  (quatro zeros)"], ep(t, C["11.c"], 0.5), 32)


# ======================================================================
# bloco d — volume: o cubo 10 × 10 × 10
# ======================================================================

def b_cubo(c, t, C, B):
    head(c, t, B["start"], "1 dm³ TEM QUANTOS cm³?", "O CUBO DE CUBINHOS", AMBER)
    card(c, *CARD_R)
    cx, cy, s = 540, 520, 270
    aa = ep(t, C["12.a"], 0.5)
    cubo_vazio(c, cx, cy, s, aa)
    if aa > 0:
        P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
        x1, y1 = P(0, 0, 1); x2, y2 = P(1, 0, 1)
        text(c, "10 cm", (x1 + x2) / 2 + 10, (y1 + y2) / 2 + 52, 30, "black", INK2, aa)
    tb, tc = C["12.b"], C["12.c"]
    camada = clamp((t - tb) / 1.6)
    altura = 0.1 * camada
    if t >= tc:
        altura = 0.1 + 0.9 * clamp((t - tc) / 3.0)
    n = 100 * camada if t < tc else 100 * round(altura * 10, 3)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0 and altura > 0:
        caixa_iso(c, cx, cy, s, 1, altura, camada if t < tc else 1, ab, div=10)
    contador(c, 1360, 330, min(1000, n), ab, "cubinhos de 1 cm³", GREEN if n >= 999.5 else BLUE)
    if ab > 0:
        text(c, "camada do fundo: 10 × 10 = 100", 1360, 500, 30, "black", BLUE, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        text(c, "10 camadas", 1360, 550, 30, "black", AMBER, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        rrect(c, 1130, 590, 460, 96, 18, "#FFFFFF", ad, shadow=True)
        linha(c, [("100 × 10 = ", INK), ("1 000", GREEN)], 1360, 638, 48, ad)
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        regra(c, "VOLUME: cada degrau vale × 1 000", 1360, 760, ae, 32)


def b_escada_vol(c, t, C, B):
    head(c, t, B["start"], "A ESCADA DO VOLUME", "CADA DEGRAU VALE × 1 000", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["13"], 0.5)
    labs = ["m³", "dm³", "cm³"]
    setas = {0: ep(t, C["13.a"], 0.5), 1: ep(t, C["13.b"], 0.5)}
    escada(c, 300, 300, labs, a0, ativos={0: a0, 1: setas[0], 2: setas[1]}, setas=setas, rot="× 1 000",
           passo_x=270, passo_y=80, w=200, size=48)
    vals = [("1 m³", "13"), ("= 1 000 dm³", "13.a"), ("= 1 000 000 cm³", "13.b")]
    for k, (s, cue) in enumerate(vals):
        text(c, s, 1200, 330 + k * 74, 48, "black", INK if k == 0 else BLUE, ep(t, C[cue], 0.5), align="left")
    K.atalho(c, 560, 620, 800, 150, "ATALHO", ["volume: TRÊS zeros por degrau"], ep(t, C["13.c"], 0.5), 36)


# ======================================================================
# bloco e — a caixa de leite explica o litro
# ======================================================================

def b_leite(c, t, C, B):
    head(c, t, B["start"], "E O LITRO?", "A CAIXA DE LEITE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.5)
    caixa_leite(c, 420, 700, 170, 330, a0)
    if a0 > 0:
        text(c, "≈ 6 × 9 × 17 cm", 420, 760, 26, "bold", GRAY, a0)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        pill(c, "não é um cubo: alta e fininha", 420, 290, AMBER, size=26, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["14.b"], 0.5)
    cx, cy, s = 1060, 560, 200
    cubo_vazio(c, cx, cy, s, ab, BLUE)
    if ab > 0:
        arrow(c, 560, 470, 820, 470, BLUE, ab, 6, 18, progress=ab)
        text(c, "despeje o leite", 690, 450, 28, "black", BLUE, ab)
        P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
        x1, y1 = P(0, 0, 1); x2, y2 = P(1, 0, 1)
        text(c, "10 cm", (x1 + x2) / 2 + 10, (y1 + y2) / 2 + 48, 28, "black", INK2, ab)
    nivel = clamp((t - C["14.b"] - 0.8) / 2.4)
    if t >= C["14.c"]:
        nivel = 1.0
    if ab > 0 and nivel > 0:
        caixa_iso(c, cx, cy, s, 1, nivel, 1, ab, cores=("#FFFFFF", "#F1F1EA", "#E2E2DA"), div=0, borda="#B8B8AE")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        conferido(c, "enche até a boca", 1010, 330, acc, True, 30)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        boxed(c, 1320, 470, 420, 190, PURPLE, ad, 0.08)
        text(c, "10 cm = 1 dm", 1530, 530, 32, "black", INK2, ad)
        text(c, "1 L = 1 dm³", 1530, 610, 56, "black", PURPLE, ad)


def b_ponte_litro(c, t, C, B):
    head(c, t, B["start"], "DA CAIXA DE LEITE", "SAEM AS OUTRAS", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.5)
    caixa_leite(c, 300, 420, 90, 170, a0)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        text(c, "1 dm³ = 1 000 cm³     e     1 L = 1 000 mL", 1000, 300, 38, "black", INK2, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        caixa_iso(c, 470, 520, 40, 1, 1, 1, ab, div=0)
        linha(c, [("1 mL = ", INK), ("1 cm³", GREEN)], 760, 470, 54, ab)
        text(c, "um cubinho de 1 cm  ·  a seringa de remédio marca mL ou cm³", 1150, 560, 28, "bold", INK2, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        text(c, "1 m³ = 1 000 dm³", 760, 660, 42, "black", INK2, acc)
    ad = ep(t, C["15.d"], 0.5)
    tanque(c, 1500, 610, 210, 170, ad, 1.0, "1 000 L")
    if ad > 0:
        linha(c, [("1 m³ = ", INK), ("1 000 L", BLUE)], 760, 750, 54, ad)


# ======================================================================
# bloco f — 1 m³ não é 1 litro: mil caixinhas
# ======================================================================

def b_mil_caixas(c, t, C, B):
    head(c, t, B["start"], "1 m³ = 1 LITRO?", "NÃO: CONTE AS CAIXINHAS", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        linha(c, [("1 m³ ", INK), ("≠", RED), (" 1 L", INK)], 1380, 280, 64, aa)
    cx, cy, s = 560, 530, 280
    ab = ep(t, C["16.b"], 0.5)
    cubo_vazio(c, cx, cy, s, ab, BLUE)
    if ab > 0:
        P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
        x1, y1 = P(0, 0, 1); x2, y2 = P(1, 0, 1)
        text(c, "1 m", (x1 + x2) / 2 + 10, (y1 + y2) / 2 + 50, 30, "black", INK2, ab)
    tc = C["16.c"]
    fx = clamp((t - tc) / 1.2)
    fz = clamp((t - tc - 1.4) / 1.4)
    fy = clamp((t - tc - 3.0) / 1.6)
    X = max(0.1, fx) if t >= tc else 0
    Z = 0.1 + 0.9 * fz
    Y = 0.1 + 0.9 * fy
    if t >= tc:
        caixa_iso(c, cx, cy, s, X, Y, Z, ab, cores=("#FFFFFF", "#F1F1EA", "#E2E2DA"), div=10, borda="#9A9A90")
    n = 0
    if t >= tc:
        n = round(10 * X) * round(10 * Z) * round(10 * Y)
    acc = ep(t, C["16.c"], 0.5)
    contador(c, 1380, 470, n, acc, "caixinhas de 1 L", GREEN if n >= 1000 else BLUE)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        rrect(c, 1090, 640, 580, 100, 18, "#FFFFFF", ad, shadow=True)
        linha(c, [("10 × 10 × 10 = ", INK), ("1 000 L", GREEN)], 1380, 690, 46, ad)


# ======================================================================
# bloco g — a massa da água
# ======================================================================

def b_agua(c, t, C, B):
    head(c, t, B["start"], "QUANTO PESA?", "A ÁGUA FECHA A PONTE", BLUE)
    card(c, *CARD_R)
    ab = ep(t, C["17.b"], 0.5)
    balanca(c, 460, 720, ab, "1,000 kg", ep(t, C["17.b"] + 3.0, 0.4))
    garrafa(c, 460, 588, 300, ab)
    rows = [("17.a", "1 cm³ de água", "1 g"), ("17.b", "1 L de água", "1 kg"), ("17.c", "1 m³ de água", "1 tonelada")]
    for k, (cue, s, r) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        y = 290 + k * 110
        text(c, s, 880, y, 44, "black", INK, a, align="left")
        text(c, "→  " + r, 1300, y, 44, "black", BLUE, a, align="left")
    K.atalho(c, 860, 620, 860, 160, "ATALHO", ["para água: litros e quilos são o MESMO número"], ep(t, C["17.d"], 0.5), 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E CONVERTA", GREEN), ("19", "VAMOS CONFERIR", "DEGRAU POR DEGRAU", GREEN)])
    card(c, *CARD_R)
    contas = [("18.a", "3 m²", "cm²", "19.a", "30 000 cm²", "2 degraus de área: × 10 000"),
              ("18.b", "0,5 m³", "litros", "19.b", "500 L", "× 1 000"),
              ("18.c", "250 mL", "cm³", "19.c", "250 cm³", "mL = cm³")]
    for k, (cue, v, para_, cr, r, como) in enumerate(contas):
        y = 300 + k * 160
        a = ep(t, C[cue], 0.5)
        rrect(c, 240, y - 64, 1440, 128, 22, "#F7F7F5", a)
        text(c, v, 330, y + 16, 54, "black", INK, a, align="left")
        text(c, "em " + para_, 600, y + 16, 40, "black", INK2, a, align="left")
        if t >= C["19"]:
            ar = ep(t, C[cr], 0.4)
            text(c, "= " + r, 950, y + 16, 54, "black", GREEN, ar, align="left")
            text(c, como, 1530, y + 12, 24, "bold", GRAY, ar)
        else:
            text(c, "= ?", 950, y + 16, 54, "black", AMBER, a, align="left")
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 790)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Área: cada degrau vale 100. Volume: cada degrau vale 1 000.",
          "1 litro é 1 decímetro cúbico; 1 metro cúbico são 1 000 litros.",
          "1 litro de água pesa 1 quilo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 42 if k == 0 else 46, "black", INK, a, 1420, 58)


ERROS = [("1 m² = 100 cm²", "um metro tem cem centímetros", "isso é o LADO: área é lado × lado = 10 000 cm²"),
         ("1 m³ = 1 000 cm³", "volume vale mil por degrau", "do m ao cm são DOIS degraus: 1 000 × 1 000 = 1 000 000 cm³"),
         ("1 m³ = 1 litro", "os dois parecem a unidade principal de volume",
          "o litro é o DECÍMETRO cúbico (a caixa de leite): 1 m³ = 1 000 L"),
         ("1 hectare = 1 000 m²", "mil é o número das conversões de sempre",
          "hectare = quadrado de 100 m de lado: 100 × 100 = 10 000 m²")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23", "24"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _rotulo(c, a):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a, align="left")


ALTS1 = [("A", "250 m²", "× 100: como se fosse o are", RED), ("B", "2 500 m²", "hectare de 1 000 m²", RED),
         ("C", "25 000 m²", "", GREEN), ("D", "250 000 m²", "um zero a mais", RED),
         ("E", "2 500 000 m²", "tratou como km²", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "EU FAÇO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    _enunciado(c, [("Um produtor rural pretende cercar uma área de plantio de 2,5 hectares.", INK),
                   ("Essa área, expressa em metros quadrados, corresponde a", BLUE)], a0, 240)
    _rotulo(c, a0)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS1, 1000, 240, 680, 40, C["26.ok"], "C", cues_in, cues_x, gap=30)
    if t >= C["26"]:
        ra = ep(t, C["26"], 0.4)
        rrect(c, 170, 440, 760, 360, 18, "#FFFFFF", ra, shadow=True)
        linha(c, [("1 ha = 100 × 100 = ", INK), ("10 000 m²", BLUE)], 550, 490, 32, ep(t, C["26.a"], 0.4))
        linha(c, [("2,5 × 10 000 = ", INK), ("25 000 m²", GREEN)], 550, 560, 38, ep(t, C["26.b"], 0.4))
        acc = ep(t, C["26.c"], 0.4)
        if acc > 0:
            for k in range(4):
                campo(c, 230 + k * 150, 620, 130 * (0.5 if k == 3 else 1), 84, acc)
            text(c, "≈ 3,5 campos de 0,7 ha ≈ 25 000 m²", 550, 750, 28, "black", INK2, acc)
            conferido(c, "fecha", 470, 790, ep(t, C["26.c"] + 6.0, 0.4), True, 26)


ALTS2 = [("A", "1,2 L", "trocou m³ por litro", RED), ("B", "12 L", "degrau de 10", RED), ("C", "120 L", "degrau de 100", RED),
         ("D", "1 200 L", "", GREEN), ("E", "12 000 L", "fator de área (× 10 000)", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "NÓS FAZEMOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    _enunciado(c, [("Uma caixa-d'água tem capacidade de 1,2 m³.", INK),
                   ("O volume de água que ela comporta, em litros, é de", BLUE)], a0, 240)
    _rotulo(c, a0)
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABCE"}
    if t >= C["28.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS2, 1000, 240, 680, 40, C["29.ok"], "D", cues_in, cues_x, gap=30)
    ap = ep(t, C["28.p"], 0.4) * (1 - ep(t, C["29"], 0.3))
    if ap > 0:
        chip(c, "a ponte entre m³ e litro?", 540, 560, AMBER, ap, 32)
    pause_timer(c, t, C["28.end"] - 1.4, 540, 680, dur=1.2)
    if t >= C["29"]:
        ra = ep(t, C["29"], 0.4)
        rrect(c, 170, 440, 760, 360, 18, "#FFFFFF", ra, shadow=True)
        linha(c, [("1 m³ = ", INK), ("1 000 L", BLUE)], 550, 490, 40, ra)
        linha(c, [("1,2 × 1 000 = ", INK), ("1 200 L", GREEN)], 550, 570, 40, ep(t, C["29.a"], 0.4))
        ab = ep(t, C["29.b"], 0.4)
        tanque(c, 400, 640, 150, 110, ab, 0.85, None)
        if ab > 0:
            text(c, "caixas de casa:", 690, 680, 26, "black", INK2, ab)
            text(c, "500 a 2 000 L", 690, 720, 30, "black", GREEN, ab)
            conferido(c, "fecha", 610, 785, ep(t, C["29.b"] + 3.0, 0.4), True, 26)


ALTS9 = [("A", "60 litros", "parou no m³", RED), ("B", "600 litros", "fator 10", RED), ("C", "6 000 litros", "fator 100", RED),
         ("D", "60 000 litros", "", GREEN), ("E", "600 000 litros", "fator de área", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "VOCÊ FAZ", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    _enunciado(c, [("Uma piscina retangular tem 8 metros de comprimento, 5 metros de largura e 1,5 metro de "
                    "profundidade uniforme.", INK),
                   ("Cheia até a borda, ela comporta", BLUE)], a0, 240)
    _rotulo(c, a0)
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABCE"}
    if t >= C["30.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS9, 1000, 240, 680, 40, C["31.ok"], "D", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["30.end"] - 1.9, 540, 660)
    if t >= C["31"]:
        ra = ep(t, C["31"], 0.4)
        rrect(c, 170, 440, 760, 360, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["31.a"], 0.4)
        if aa > 0:
            text(c, "volume = comprimento × largura × altura", 550, 490, 28, "black", PURPLE, aa)
            text(c, "(quantos cubinhos de 1 m cabem)", 550, 528, 22, "bold", GRAY, aa)
        linha(c, [("8 × 5 × 1,5 = ", INK), ("60 m³", BLUE)], 550, 600, 40, ep(t, C["31.b"], 0.4))
        acc = ep(t, C["31.c"], 0.4)
        if acc > 0:
            linha(c, [("60 × 1 000 = ", INK), ("60 000 L", GREEN)], 550, 680, 40, acc)
        a32 = ep(t, C["32.c"], 0.4)
        if a32 > 0:
            text(c, "= 60 caixas-d'água de 1 000 L = 60 toneladas", 550, 760, 26, "black", INK2, a32)
            conferido(c, "faz sentido", 440, 800, ep(t, C["32.c"] + 4.0, 0.4), True, 24)


# ======================================================================
# ponte e CTA
# ======================================================================

def relogio(c, cx, cy, r, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(INK, a, stroke=6))
    for k in range(12):
        ang = math.radians(k * 30)
        x0, y0 = cx + math.sin(ang) * r * 0.82, cy - math.cos(ang) * r * 0.82
        x1, y1 = cx + math.sin(ang) * r * 0.94, cy - math.cos(ang) * r * 0.94
        line(c, x0, y0, x1, y1, INK, a, 4)
    line(c, cx, cy, cx, cy - r * 0.62, INK, a, 7)
    line(c, cx, cy, cx + r * 0.45, cy, INK, a, 7)
    c.drawCircle(cx, cy, 8, paint(RED, a))


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A EXCEÇÃO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    for k, s in enumerate(("m", "g", "L")):
        chip(c, f"{s}:  × 10", 420, 300 + k * 110, GREEN, aa * ep(t, C["34.a"] + 0.3 * k, 0.4), 40)
    ab = ep(t, C["34.b"], 0.5)
    relogio(c, 1250, 440, 170, ab)
    if ab > 0:
        text(c, "60 min = 1 h", 1250, 680, 42, "black", AMBER, ab)
    acc = ep(t, C["34.c"], 0.5)
    if acc > 0:
        selo(c, 1250, 760, acc, "NÃO É DECIMAL", RED, -3, 32)
    pill(c, "ep. 3 · o tempo e as unidades compostas", 640, 760, PURPLE, size=30, a=ep(t, C["34.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Quantos litros cabem na caixa-d'água da sua casa?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, defs=b_defs, grade=b_grade,
              escada_area=b_escada_area, confirma=b_confirma, hectare=b_hectare, cubo=b_cubo, escada_vol=b_escada_vol,
              leite=b_leite, ponte_litro=b_ponte_litro, mil_caixas=b_mil_caixas, agua=b_agua, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q1=b_q1, q2=b_q2, q9=b_q9, ponte=b_ponte, cta=b_cta)
