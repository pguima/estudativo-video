"""Visual — Escalas, Plantas e Mapas, Episódio 3: plantas e maquetes, área usa n² e volume usa n³ (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, selo...).
Peças deste episódio: planta_baixa() (apartamento estilizado com medidas em cm), quadradinho que cresce até 2 m × 2 m,
_iso/caixa_iso/cubo_vazio (cubo isométrico do 025/ep2), tanque(), predio() (maquete com caixa-d'água), regua_cm().
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
_s = importlib.util.spec_from_file_location("comum026", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_escalas_ep3_plantas_maquetes.mp4"
CARD_R = K.CARD_R
PAPEL = "#FBF8EF"
PAREDE = "#3B4A5C"
AGUA = "#5FA8E8"
CUBO_TOPO, CUBO_FRENTE, CUBO_LADO = "#C9DEF8", "#9CC3F0", "#7AAAE0"
MAQ = ("#FFFFFF", "#F1F1EA", "#E2E2DA")


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


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    text(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


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
        pg = paint("#FFFFFF", a * 0.6, stroke=1.2)
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


def tanque(c, cx, y_top, w, h, a, nivel=1.0, rotulo=None, rsize=34):
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
    pe = paint("#5B6B7D", a, stroke=max(2, w / 50))
    c.drawLine(cx - rx, y_top, cx - rx, y_top + h, pe); c.drawLine(cx + rx, y_top, cx + rx, y_top + h, pe)
    c.drawArc(skia.Rect.MakeXYWH(cx - rx, y_top + h - ry, w, 2 * ry), 0, 180, False, pe)
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top - ry, w, 2 * ry), paint("#CFD8E2", a))
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top - ry, w, 2 * ry), pe)
    if rotulo:
        rw = text_w(rotulo, "black", rsize) + 30
        rrect(c, cx - rw / 2, y_top + h * 0.40, rw, rsize * 1.8, 12, "#FFFFFF", a * 0.95)
        text_mid(c, rotulo, cx, y_top + h * 0.40 + rsize * 0.9, rsize, "black", INK, a)


def predio(c, x, base_y, w, h, a, andares=6, tanque_a=1.0):
    """maquete de prédio (de frente) com uma caixa-d'água no telhado"""
    if a <= 0:
        return
    rrect(c, x - 30, base_y, w + 60, 22, 6, "#C9D3C0", a)
    rrect(c, x, base_y - h, w, h, 6, "#EEF1F5", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, base_y - h, w, h), 6, 6), paint(PAREDE, a, stroke=3))
    ah = (h - 40) / andares
    for i in range(andares):
        for j in range(3):
            rrect(c, x + 18 + j * (w - 36) / 3, base_y - h + 20 + i * ah, (w - 36) / 3 - 14, ah - 16, 3, "#BFD7EF", a)
    tanque(c, x + w / 2, base_y - h - 70, w * 0.42, 62, a * tanque_a, 0.8)


def planta_baixa(c, x, y, s, a, cotas=True, foco=None, foco_a=0.0):
    """apartamento estilizado visto de cima; s = pixels por centímetro do papel; foco = nome do cômodo destacado"""
    if a <= 0:
        return
    comodos = [("sala", 0, 0, 5, 4), ("quarto", 5, 0, 4, 4), ("cozinha", 0, 4, 3, 2.5), ("banho", 3, 4, 2, 2.5),
               ("varanda", 5, 4, 4, 2.5)]
    rrect(c, x - 26, y - 26, 9 * s + 52, 6.5 * s + 52, 10, PAPEL, a, shadow=True)
    for nome, i, j, w_, h_ in comodos:
        hl = foco_a if nome == foco else 0.0
        c.drawRect(skia.Rect.MakeXYWH(x + i * s, y + j * s, w_ * s, h_ * s), paint(mix("#FFFFFF", BLUE, 0.10 + 0.25 * hl), a))
    for nome, i, j, w_, h_ in comodos:
        c.drawRect(skia.Rect.MakeXYWH(x + i * s, y + j * s, w_ * s, h_ * s), paint(PAREDE, a, stroke=5))
        hl = foco_a if nome == foco else 0.0
        text_mid(c, nome, x + (i + w_ / 2) * s, y + (j + h_ / 2) * s, max(18, s * 0.42), "black", mix(INK2, BLUE, hl), a)
    # portas (aberturas)
    for px, py, horiz in ((x + 4.2 * s, y + 4 * s, True), (x + 5 * s, y + 1.8 * s, False), (x + 1.2 * s, y + 4 * s, True)):
        if horiz:
            c.drawRect(skia.Rect.MakeXYWH(px, py - 4, s * 0.6, 8), paint(mix("#FFFFFF", BLUE, 0.10), a))
        else:
            c.drawRect(skia.Rect.MakeXYWH(px - 4, py, 8, s * 0.6), paint(mix("#FFFFFF", BLUE, 0.10), a))
    if cotas:
        cota_h(c, x, x + 5 * s, y - 40, "5 cm", a, BLUE, 24)
        cota_v(c, x - 44, y, y + 4 * s, "", a, BLUE, 24)
        text(c, "4 cm", x - 56, y + 2 * s + 8, 24, "black", BLUE, a, align="right")


def regua(c, x, y, cm, s, a, rot=True):
    """régua de `cm` centímetros (s px por cm)"""
    if a <= 0:
        return
    rrect(c, x - 14, y - 10, cm * s + 28, 70, 8, "#F5E6A8", a, shadow=True)
    for k in range(cm * 10 + 1):
        hh = 34 if k % 10 == 0 else (22 if k % 5 == 0 else 12)
        line(c, x + k * s / 10, y - 10, x + k * s / 10, y - 10 + hh, INK2, a, 2 if k % 10 == 0 else 1)
        if rot and k % 10 == 0:
            text(c, str(k // 10), x + k * s / 10, y + 50, 20, "bold", INK2, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PLANTAS E MAQUETES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    predio(c, 270, 720, 220, 330, aa)
    if aa > 0:
        pill(c, "maquete 1 : 20", 380, 790, PURPLE, size=26, a=aa, anchor="center", bounds=(0, 1920))
        tanque(c, 720, 470, 150, 140, aa, 0.85, "5 L", 40)
    ab = ep(t, C["01.b"], 0.5)
    tanque(c, 1300, 320, 300, 280, ab, 0.85, None)
    if ab > 0:
        text(c, "a caixa real", 1300, 280, 30, "black", INK2, ab)
        arrow(c, 830, 540, 1110, 470, INK2, ab, 5, 16, progress=ab)
        ax = ep(t, C["01.c"], 0.4)
        linha(c, [("100 L ?", RED if ax > 0 else AMBER)], 1300, 690, 64, ab)
        if ax > 0:
            line(c, 1180, 690, 1420, 690, RED, ax, 7)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        linha(c, [("40 000 L", GREEN)], 1300, 780, 70, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 760, 300, ad, "O ERRO MAIS CARO", RED, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular ÁREAS a partir de plantas", "m² de cada cômodo"),
            ("02.b", "calcular VOLUMES a partir de maquetes", "litros e m³ da caixa real"),
            ("02.c", "sem esquecer o quadrado e o cubo", "n²  e  n³")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "3 LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 250, 700, 230, BLUE, aa, 0.06)
        text(c, "do episódio 1", 570, 300, 26, "black", BLUE, aa)
        linha(c, [("real = desenho × ", INK), ("n", PURPLE)], 570, 370, 44, aa)
        text(c, "papel → mundo: o número CRESCE", 570, 445, 28, "bold", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        boxed(c, 1000, 250, 700, 230, PURPLE, ab, 0.06)
        rrect(c, 1060, 300, 200, 130, 4, mix("#FFFFFF", PURPLE, 0.15), ab)
        c.drawRect(skia.Rect.MakeXYWH(1060, 300, 200, 130), paint(INK, ab, stroke=3))
        text(c, "base", 1160, 455, 22, "bold", INK2, ab)
        text(c, "altura", 1274, 372, 22, "bold", INK2, ab, align="left")
        text(c, "ÁREA = base × altura", 1520, 352, 30, "black", PURPLE, ab)
        text(c, "quantos quadradinhos cabem", 1520, 400, 22, "bold", GRAY, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        boxed(c, 220, 540, 700, 230, BLUE, acc, 0.06)
        linha(c, [("1 m² = 100 × 100 = ", INK), ("10 000 cm²", BLUE)], 570, 640, 38, acc)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        boxed(c, 1000, 540, 700, 230, BLUE, ad, 0.06)
        tanque(c, 1150, 590, 120, 110, ad, 0.85, None)
        linha(c, [("1 m³ = ", INK), ("1 000 L", BLUE)], 1470, 650, 44, ad)


# ======================================================================
# concreto e definições
# ======================================================================

def b_cotidiano(c, t, C, B):
    head(c, t, B["start"], "UM APARTAMENTO À VENDA", "O DESENHO E A MINIATURA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        pill(c, "VENDE-SE · desenho visto de cima", 210, 236, BLUE, size=24, a=aa, bounds=(0, 1920))
    ab = ep(t, C["04.b"], 0.5)
    planta_baixa(c, 290, 345, 66, aa, cotas=ab > 0, foco="sala", foco_a=ab)
    acc = ep(t, C["04.c"], 0.5)
    predio(c, 1240, 760, 230, 280, acc)
    if acc > 0:
        text(c, "a miniatura na entrada", 1355, 820, 26, "black", INK2, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        chip(c, "a sala de verdade: ?  m²", 1480, 250, AMBER, ad, 30)
        chip(c, "a caixa de verdade: ?  litros", 1480, 330, AMBER, ep(t, C["04.d"] + 1.6, 0.5), 30)


def b_defs(c, t, C, B):
    head(c, t, B["start"], "OS NOMES", "PLANTA, CORTE, FACHADA, MAQUETE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    planta_baixa(c, 230, 330, 40, aa, cotas=False)
    if aa > 0:
        text(c, "PLANTA BAIXA", 410, 640, 30, "black", BLUE, aa)
        text(c, "vista de cima, sem o teto", 410, 680, 24, "bold", INK2, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        x, y = 700, 330
        rrect(c, x, y, 280, 230, 4, "#EEF1F5", ab)
        for k in range(1, 3):
            line(c, x, y + k * 230 / 3, x + 280, y + k * 230 / 3, PAREDE, ab, 4)
        c.drawRect(skia.Rect.MakeXYWH(x, y, 280, 230), paint(PAREDE, ab, stroke=4))
        text(c, "CORTE", x + 140, 640, 30, "black", BLUE, ab)
        text(c, "o prédio fatiado de cima a baixo", x + 140, 680, 24, "bold", INK2, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        predio(c, 1080, 560, 220, 230, acc, andares=4, tanque_a=0)
        text(c, "FACHADA", 1190, 640, 30, "black", BLUE, acc)
        text(c, "a vista de fora", 1190, 680, 24, "bold", INK2, acc)
        text(c, "todas na MESMA escala", 840, 770, 30, "black", PURPLE, ep(t, C["05.c"] + 1.6, 0.5))
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        caixa_iso(c, 1560, 470, 130, 1, 1.3, 0.8, ad, cores=MAQ, div=0, borda="#9A9A90")
        text(c, "MAQUETE", 1560, 640, 30, "black", BLUE, ad)
        text(c, "modelo 3D encolhido", 1560, 680, 24, "bold", INK2, ad)


# ======================================================================
# bloco a — plantas e projetos
# ======================================================================

PLANTAS = [("06.a", "1 : 20", "móveis, detalhes", "20 cm"), ("06.b", "1 : 50", "planta de casa", "50 cm"),
           ("06.c", "1 : 100", "planta de prédio", "1 m"), ("06.d", "1 : 500", "loteamento", "5 m"),
           ("06.e", "1 : 1 000", "plano de cidade", "10 m")]


def b_plantas(c, t, C, B):
    head(c, t, B["start"], "1 cm NA PLANTA VALE QUANTO?", "DEPENDE DA ESCALA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["06"], 0.5)
    for k, s in enumerate(("escala", "uso típico", "1 cm vale")):
        text(c, s, (420, 900, 1420)[k], 270, 28, "black", GRAY, a0)
    line(c, 240, 290, 1680, 290, LIGHT, a0, 3)
    for k, (cue, e, uso, v) in enumerate(PLANTAS):
        a, d = rise(t, C[cue])
        y = 360 + k * 92 + d
        hl = 1.0 if k == 2 else 0.0
        if a > 0 and hl:
            rrect(c, 240, y - 48, 1440, 86, 14, mix("#FFFFFF", GREEN, 0.14), a)
        text(c, e, 420, y + 14, 44, "black", PURPLE, a)
        text(c, uso, 900, y + 12, 34, "bold", INK2, a)
        text(c, v, 1420, y + 14, 44, "black", GREEN if hl else BLUE, a)


def b_cem(c, t, C, B):
    head(c, t, B["start"], "A ESCALA MAIS AMIGÁVEL", "1 : 100", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    regua(c, 260, 290, 7, 100, aa)
    if aa > 0:
        rrect(c, 260, 400, 100, 30, 4, BLUE, aa)
        linha(c, [("1 cm × 100 = 100 cm = ", INK), ("1 m", GREEN)], 1300, 300, 42, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 400, 700 * clamp((t - C["07.b"]) / 1.2), 30, 4, PAREDE, ab)
        text(c, "parede: 7 cm no papel", 610, 480, 30, "black", INK2, ab)
        linha(c, [("7 cm  →  ", INK), ("7 m", GREEN)], 1300, 400, 52, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        selo(c, 1300, 500, acc, "A MAIS AMIGÁVEL", GREEN, -3, 30)
    K.atalho(c, 220, 580, 720, 200, "ATALHO", ["1 : 100 → troque cm por m"], ep(t, C["07.d"], 0.5), 34)
    K.atalho(c, 980, 580, 720, 200, "ATALHO", ["1 : 50 → a METADE dá os metros", "6 cm → 3 m"], ep(t, C["07.e"], 0.5), 30)


# ======================================================================
# bloco b — as três escalas
# ======================================================================

def b_tres(c, t, C, B):
    head(c, t, B["start"], "E A ÁREA?", "AS TRÊS ESCALAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha(c, [("1 : ", INK), ("n", PURPLE), ("    n = o número de baixo", GRAY)], W / 2, 260, 40, aa)
    rows = [("08.b", "COMPRIMENTO", "1 : n", "escala linear", 1), ("08.c", "ÁREA", "1 : n²", "2 medidas: n × n", 2),
            ("08.d", "VOLUME", "1 : n³", "3 medidas: n × n × n", 3)]
    for k, (cue, nome, f, sub, dim) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 360 + k * 150 + d
        rrect(c, 260, y - 60, 1400, 124, 20, "#FFFFFF", a, shadow=True)
        ix = 360
        if dim == 1:
            line(c, ix - 50, y, ix + 50, y, BLUE, a, 8)
        elif dim == 2:
            rrect(c, ix - 44, y - 44, 88, 88, 4, mix("#FFFFFF", BLUE, 0.35), a)
            c.drawRect(skia.Rect.MakeXYWH(ix - 44, y - 44, 88, 88), paint(BLUE, a, stroke=3))
        else:
            caixa_iso(c, ix, y - 40, 62, 1, 1, 1, a, div=0)
        text(c, nome, 470, y + 14, 40, "black", INK, a, align="left")
        text_mid(c, f, 1050, y, 56, "black", PURPLE, a)
        text(c, sub, 1440, y + 12, 28, "bold", INK2, a)


# ======================================================================
# bloco c — o quadradinho que vira 4 m²
# ======================================================================

def b_quadradinho(c, t, C, B):
    head_seq(c, t, C, [("09", "1 cm² NA PLANTA 1 : 200", "VALE QUANTO?", AMBER),
                       ("10", "PARECE MÁGICA?", "O QUADRADINHO CRESCE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0:
            text(c, "escala de área: 1 : 200²", W / 2, 290, 36, "black", PURPLE, aa)
            linha(c, [("200² = 200 × 200 = ", INK), ("40 000", PURPLE)], W / 2, 390, 52, aa)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            linha(c, [("1 cm²  →  ", INK), ("40 000 cm²", BLUE)], W / 2, 510, 56, ab)
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            rrect(c, 560, 600, 800, 130, 22, "#FFFFFF", acc, shadow=True)
            linha(c, [("40 000 ÷ 10 000 = ", INK), ("4 m²", GREEN)], W / 2, 665, 60, acc)
        return
    # cena 10: 1 cm² vira 2 m × 2 m
    x0, y0 = 300, 280
    aa = ep(t, C["10.a"], 0.5)
    g = clamp((t - C["10.b"]) / 2.2) if t >= C["10.b"] else 0.0
    gs = 40 + (480 - 40) * (1 - (1 - g) ** 3)
    if aa > 0:
        rrect(c, x0, y0, gs, gs, 3, mix("#FFFFFF", BLUE, 0.30), aa)
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, gs, gs), paint(INK, aa, stroke=4 if g > 0 else 3))
        lado = "1 cm" if g < 0.5 else "200 cm = 2 m"
        cota_h(c, x0, x0 + gs, y0 - 16, lado, aa, BLUE if g < 0.5 else GREEN, 26)
        if g < 0.05:
            text(c, "1 cm²", x0 + 70, y0 + 30, 30, "black", BLUE, aa, align="left")
    if g > 0.98:
        cota_v(c, x0 + gs + 24, y0, y0 + gs, "2 m", aa, GREEN, 28)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        line(c, x0 + gs / 2, y0, x0 + gs / 2, y0 + gs, INK, ad, 3)
        line(c, x0, y0 + gs / 2, x0 + gs, y0 + gs / 2, INK, ad, 3)
        for i in range(2):
            for j in range(2):
                text_mid(c, "1 m²", x0 + gs / 4 + i * gs / 2, y0 + gs / 4 + j * gs / 2, 40, "black", BLUE,
                         ad * ep(t, C["10.d"] + 0.3 * (2 * j + i), 0.4))
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("2 m × 2 m", INK)] + ([(" = ", INK), ("4 m²", GREEN)] if ad > 0 else []), 1300, 330, 56, acc)
    if ad > 0:
        text(c, "4 quadrados de 1 m²", 1300, 420, 32, "black", INK2, ad)
    K.atalho(c, 960, 520, 700, 210, "ATALHO", ["ache o LADO real em metros", "e eleve ao quadrado"],
             ep(t, C["10.e"], 0.5), 32)


# ======================================================================
# bloco d — converta os lados primeiro
# ======================================================================

def sala(c, x, y, s, wcm, hcm, a, real_a=0.0, real=("", ""), rotulo=None):
    """retângulo de cômodo com cotas em cm que viram cotas reais (real_a 0..1)"""
    if a <= 0:
        return
    rrect(c, x, y, wcm * s, hcm * s, 4, mix("#FFFFFF", BLUE, 0.14), a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, wcm * s, hcm * s), paint(PAREDE, a, stroke=6))
    cota_h(c, x, x + wcm * s, y - 18, f"{wcm} cm", a * (1 - real_a), BLUE, 28)
    cota_h(c, x, x + wcm * s, y - 18, real[0], a * real_a, GREEN, 30)
    cota_v(c, x + wcm * s + 24, y, y + hcm * s, f"{hcm} cm", a * (1 - real_a), BLUE, 28)
    cota_v(c, x + wcm * s + 24, y, y + hcm * s, real[1], a * real_a, GREEN, 30)
    if rotulo:
        text_mid(c, rotulo, x + wcm * s / 2, y + hcm * s / 2, 34, "black", INK2, a)


def b_lados(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO MAIS SEGURO", "CONVERTA OS LADOS PRIMEIRO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.5)
    ra = ep(t, C["11.b"], 0.8)
    sala(c, 280, 320, 80, 5, 4, a0, ra, ("5 m", "4 m"), "sala")
    if a0 > 0:
        pill(c, "planta 1 : 100", 280, 760, PURPLE, size=26, a=a0, bounds=(0, 1920))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("5 cm → ", INK), ("5 m", GREEN), ("      4 cm → ", INK), ("4 m", GREEN)], 1250, 330, 42, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 900, 410, 700, 120, 22, "#FFFFFF", acc, shadow=True)
        linha(c, [("5 m × 4 m = ", INK), ("20 m²", GREEN)], 1250, 470, 56, acc)
    K.atalho(c, 860, 580, 780, 190, "ATALHO", ["converta os LADOS primeiro:", "o quadrado acontece sozinho"],
             ep(t, C["11.d"], 0.5), 32)


# ======================================================================
# bloco e — a maquete e o cubo
# ======================================================================

def b_maquete(c, t, C, B):
    head_seq(c, t, C, [("12", "A MAQUETE ENCOLHE", "EM TRÊS DIREÇÕES", AMBER), ("13", "O PASSO ESQUECIDO", "× 5 LITROS", PURPLE)])
    card(c, *CARD_R)
    cx, cy, s = 600, 470, 300
    sid = which(t, C, ["12", "13"])
    a0 = ep(t, C["12"], 0.5)
    # a caixinha da maquete (1/20 da real) no canto
    if a0 > 0:
        caixa_iso(c, 250, 700, s / 20 * 1.8, 1, 1, 1, a0, cores=MAQ, div=0, borda="#9A9A90")
        text(c, "maquete: 5 L", 250, 790, 26, "black", INK2, a0)
    aa = ep(t, C["12.a"], 0.5)
    cubo_vazio(c, cx, cy, s, aa, BLUE)
    if aa > 0:
        text(c, "a caixa real", cx, cy + s * 1.05 + 30, 28, "black", BLUE, aa)
    if sid == "12":
        tb, tcc, td = C["12.b"], C["12.c"], C["12.d"]
        X = 0.05 + 0.95 * clamp((t - tb) / 1.6) if t >= tb else 0
        Z = 0.05 + 0.95 * clamp((t - tcc) / 1.6) if t >= tcc else 0.05
        Y = 0.05 + 0.95 * clamp((t - td) / 1.8) if t >= td else 0.05
        if t >= tb:
            caixa_iso(c, cx, cy, s, X, Y, Z, 1.0, cores=MAQ, div=20, borda="#9A9A90")
        n = round(20 * X) * round(20 * Z) * round(20 * Y) if t >= tb else 0
        rows = [("12.b", "comprimento", "× 20", "20"), ("12.c", "largura", "× 20", "400"), ("12.d", "altura", "× 20", "8 000")]
        for k, (cue, nome, f, acum) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            y = 300 + k * 80
            text(c, nome, 1110, y, 36, "black", INK, a, align="left")
            text(c, f, 1400, y, 36, "black", AMBER, a, align="left")
        contador(c, 1360, 610, n, ep(t, C["12.b"], 0.5), "caixinhas da maquete", GREEN if n >= 8000 else BLUE, w=420)
        ae = ep(t, C["12.e"], 0.5)
        if ae > 0:
            rrect(c, 1040, 720, 640, 90, 18, "#FFFFFF", ae, shadow=True)
            linha(c, [("20 × 20 × 20 = ", INK), ("8 000", GREEN)], 1360, 765, 44, ae)
        return
    caixa_iso(c, cx, cy, s, 1, 1, 1, 1.0, cores=MAQ, div=20, borda="#9A9A90")
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        linha(c, [("8 000 caixinhas × ", INK), ("5 L", AMBER)], 1360, 300, 44, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 1040, 360, 640, 110, 20, "#FFFFFF", ab, shadow=True)
        linha(c, [("5 × 8 000 = ", INK), ("40 000 L", GREEN)], 1360, 415, 52, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        linha(c, [("40 000 L ÷ 1 000 = ", INK2), ("40 m³", BLUE)], 1360, 530, 40, acc)
    K.atalho(c, 1010, 610, 700, 180, "ATALHO", ["capacidade real = maquete × n³"], ep(t, C["13.d"], 0.5), 32)


def b_maquete_fachada(c, t, C, B):
    head(c, t, B["start"], "NA MESMA MAQUETE 1 : 20", "UMA ESCALA, TRÊS FATORES", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.5)
    predio(c, 260, 760, 260, 400, a0, andares=6, tanque_a=1.0)
    rows = [("14.a", "alturas", "comprimento", "÷ 20", BLUE), ("14.b", "área da fachada", "área", "÷ 400", PURPLE),
            ("14.c", "volume", "volume", "÷ 8 000", AMBER)]
    for k, (cue, nome, tipo, f, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 320 + k * 150 + d
        rrect(c, 700, y - 60, 960, 120, 20, "#FFFFFF", a, shadow=True)
        text(c, nome, 760, y - 4, 40, "black", INK, a, align="left")
        text(c, tipo, 760, y + 38, 24, "bold", GRAY, a, align="left")
        text(c, f, 1600, y + 18, 56, "black", col, a, align="right")


# ======================================================================
# bloco f — referências rápidas
# ======================================================================

TABELA = [("15.b", "1 : 50", "50 cm", "0,25 m²"), ("15.c", "1 : 100", "1 m", "1 m²"), ("15.d", "1 : 1 000", "10 m", "100 m²"),
          ("15.e", "1 : 50 000", "0,5 km", "25 ha")]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "REFERÊNCIAS RÁPIDAS", "UMA REGRA GERA A TABELA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 230, 1400, 120, PURPLE, aa, 0.07)
        linha(c, [("em 1 : n →  1 cm vale ", INK), ("n cm", BLUE), ("   e   1 cm² vale ", INK), ("n² cm²", PURPLE)],
              W / 2, 290, 38, aa)
    for k, s in enumerate(("escala", "1 cm vale", "1 cm² vale")):
        text(c, s, (480, 960, 1440)[k], 410, 28, "black", GRAY, aa)
    for k, (cue, e, v, ar) in enumerate(TABELA):
        a, d = rise(t, C[cue])
        y = 480 + k * 84 + d
        if a > 0 and k == 1:
            rrect(c, 260, y - 44, 1400, 80, 14, mix("#FFFFFF", GREEN, 0.14), a)
        text(c, e, 480, y + 14, 42, "black", PURPLE, a)
        text(c, v, 960, y + 14, 42, "black", BLUE, a)
        text(c, ar, 1440, y + 14, 42, "black", GREEN, a)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        text(c, "1 ha = 10 000 m²  ·  500 m × 500 m = 250 000 m² = 25 ha", W / 2, 822, 22, "bold", GRAY, ae)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("17", "VAMOS CONFERIR", "LADOS PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    ra = ep(t, C["17.a"], 0.8) if t >= C["17"] else 0.0
    sala(c, 300, 300, 60, 6, 8, aa, ra, ("3 m", "4 m"), "quarto")
    if aa > 0:
        pill(c, "planta 1 : 50", 300, 820, PURPLE, size=26, a=aa, bounds=(0, 1920))
    if t < C["17"]:
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            linha(c, [("área real = ", INK), ("?  m²", AMBER)], 1250, 400, 56, ab)
        pause_timer(c, t, C["16.end"] - 1.9, 1250, 600)
        return
    ra2 = ep(t, C["17.a"], 0.5)
    if ra2 > 0:
        text(c, "1 : 50 → cada cm é meio metro", 1250, 330, 32, "black", INK2, ra2)
        linha(c, [("6 cm → ", INK), ("3 m", GREEN), ("     8 cm → ", INK), ("4 m", GREEN)], 1250, 420, 44, ra2)
    rb = ep(t, C["17.b"], 0.5)
    if rb > 0:
        rrect(c, 920, 490, 660, 120, 22, "#FFFFFF", rb, shadow=True)
        linha(c, [("3 m × 4 m = ", INK), ("12 m²", GREEN)], 1250, 550, 56, rb)
    conferido(c, "um quarto de 3 × 4: faz sentido", 980, 690, ep(t, C["17.c"], 0.5), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Comprimento usa n; área usa n²; volume usa n³.",
          "Em planta, converta os lados antes de calcular a área.",
          "Em 1 : 100, 1 centímetro é 1 metro."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1420, 60)


ERROS = [("1 cm² em 1 : 200 = 200 cm²", "a escala diz 200",
          "o 200 é para COMPRIMENTO: 200 × 200 = 40 000 cm² = 4 m²"),
         ("maquete 1 : 20 → volume × 20", "é o número da escala",
          "a maquete encolhe em 3 direções: 20 × 20 × 20 = 8 000"),
         ("achar 8 000 e responder 8 000 litros", "o cubo da escala era o difícil",
          "8 000 é quantas maquetes cabem: falta × a capacidade da maquete"),
         ("uma parede de 35 m numa sala", "a conta foi feita",
          "35 m é um prédio: em planta, você SABE o tamanho de um cômodo")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21", "22"], ERROS)


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


def _resol(c, a):
    rrect(c, 170, 440, 760, 360, 18, "#FFFFFF", a, shadow=True)


ALTS9 = [("A", "0,35 m", "× 5, e não × 50", RED), ("B", "3,5 m", "", GREEN), ("C", "7 m", "leu como 1 : 100", RED),
         ("D", "35 m", "÷ 10 em vez de ÷ 100", RED), ("E", "350 m", "chamou cm de m", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "AQUECIMENTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Na planta baixa de uma residência, desenhada na escala 1 : 50, uma parede da sala está representada "
                    "por um segmento de 7 cm.", INK),
                   ("O comprimento real dessa parede é de", BLUE)], a0, 240)
    _rotulo(c, a0)
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS9, 1000, 240, 680, 40, C["24.ok"], "B", cues_in, cues_x, gap=30)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        _resol(c, ra)
        linha(c, [("7 cm × 50 = ", INK), ("350 cm", BLUE)], 550, 500, 40, ra)
        linha(c, [("350 cm ÷ 100 = ", INK), ("3,5 m", GREEN)], 550, 590, 40, ep(t, C["24.a"], 0.4))
        conferido(c, "parede de sala: faz sentido", 330, 690, ep(t, C["24.b"], 0.4), True, 28)


ALTS5 = [("A", "0,2 m²", "fator linear na área", RED), ("B", "2 m²", "÷ 100 000", RED), ("C", "20 m²", "", GREEN),
         ("D", "200 m²", "÷ 1 000", RED), ("E", "2 000 m²", "÷ 100", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "EU FAÇO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    _enunciado(c, [("Em uma planta baixa desenhada na escala 1 : 100, uma sala aparece como um retângulo de 5 cm por "
                    "4 cm.", INK),
                   ("A área real dessa sala é de", BLUE)], a0, 240)
    _rotulo(c, a0)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS5, 1000, 240, 680, 40, C["26.ok"], "C", cues_in, cues_x, gap=30)
    if t >= C["26"]:
        ra = ep(t, C["26"], 0.4)
        _resol(c, ra)
        text(c, "CAMINHO 1 · o seguro", 550, 485, 24, "black", GREEN, ra)
        linha(c, [("5 cm → 5 m    4 cm → 4 m", INK)], 550, 530, 30, ep(t, C["26.a"], 0.4))
        linha(c, [("5 m × 4 m = ", INK), ("20 m²", GREEN)], 550, 585, 36, ep(t, C["26.b"], 0.4))
        acc = ep(t, C["26.c"], 0.4)
        if acc > 0:
            line(c, 200, 625, 900, 625, LIGHT, acc, 2)
            text(c, "CAMINHO 2 · o fator de área", 550, 665, 24, "black", PURPLE, acc)
            linha(c, [("20 cm² × 100² = 200 000 cm²", INK)], 550, 712, 30, acc)
        linha(c, [("200 000 ÷ 10 000 = ", INK), ("20 m²", GREEN)], 550, 765, 32, ep(t, C["26.d"], 0.4))
    a27 = ep(t, C["27.c"], 0.4)
    if a27 > 0:
        chip(c, "cm² → m²: sempre ÷ 10 000", 1340, 790, PURPLE, a27, 28)


ALTS6 = [("A", "0,02 m²", "fator 200 uma vez só", RED), ("B", "2 m²", "200 cm² ÷ 100", RED), ("C", "4 m²", "", GREEN),
         ("D", "20 m²", "uma sala inteira", RED), ("E", "40 m²", "÷ 1 000", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "NÓS FAZEMOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    _enunciado(c, [("Em um projeto desenhado na escala 1 : 200, cada centímetro quadrado do papel representa, na "
                    "realidade, uma área de", BLUE)], a0, 240)
    _rotulo(c, a0)
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    if t >= C["28.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS6, 1000, 240, 680, 40, C["29.ok"], "C", cues_in, cues_x, gap=30)
    ap = ep(t, C["28.p"], 0.4) * (1 - ep(t, C["29"], 0.3))
    if ap > 0:
        chip(c, "quanto mede o LADO real?", 540, 520, AMBER, ap, 32)
    pause_timer(c, t, C["28.end"] - 1.4, 540, 660, dur=1.2)
    if t >= C["29"]:
        ra = ep(t, C["29"], 0.4)
        _resol(c, ra)
        linha(c, [("lado: 1 cm × 200 = 200 cm = ", INK), ("2 m", BLUE)], 550, 500, 32, ra)
        aa = ep(t, C["29.a"], 0.4)
        if aa > 0:
            rrect(c, 260, 545, 110, 110, 3, mix("#FFFFFF", BLUE, 0.3), aa)
            line(c, 315, 545, 315, 655, INK, aa, 2); line(c, 260, 600, 370, 600, INK, aa, 2)
            c.drawRect(skia.Rect.MakeXYWH(260, 545, 110, 110), paint(INK, aa, stroke=3))
            linha(c, [("2 m × 2 m = ", INK), ("4 m²", GREEN)], 640, 600, 40, aa)
        linha(c, [("1 × 200² = 40 000 cm² = ", INK), ("4 m²", GREEN)], 550, 720, 30, ep(t, C["29.b"], 0.4))
        conferido(c, "bate", 470, 785, ep(t, C["29.b"] + 3.0, 0.4), True, 26)


ALTS7 = [("A", "100 litros", "fator linear: 5 × 20", RED), ("B", "2 000 litros", "fator de área: 5 × 400", RED),
         ("C", "8 000 litros", "esqueceu os 5 L", RED), ("D", "40 000 litros", "", GREEN),
         ("E", "400 000 litros", "um zero a mais", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "VOCÊ FAZ", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    _enunciado(c, [("Uma maquete construída na escala 1 : 20 reproduz um reservatório de água. A maquete comporta "
                    "5 litros.", INK),
                   ("O reservatório real comporta", BLUE)], a0, 240)
    _rotulo(c, a0)
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABCE"}
    if t >= C["30.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS7, 1000, 240, 680, 40, C["31.ok"], "D", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["30.end"] - 1.9, 540, 660)
    if t >= C["31"]:
        ra = ep(t, C["31"], 0.4)
        _resol(c, ra)
        text(c, "capacidade = volume → 3 dimensões", 550, 490, 26, "black", PURPLE, ra)
        linha(c, [("20³ = 20 × 20 × 20 = ", INK), ("8 000", AMBER)], 550, 560, 36, ep(t, C["31.a"], 0.4))
        linha(c, [("5 L × 8 000 = ", INK), ("40 000 L", GREEN)], 550, 640, 40, ep(t, C["31.b"], 0.4))
        acc = ep(t, C["31.c"], 0.4)
        if acc > 0:
            text(c, "= 40 m³ ≈ 4 m × 4 m × 2,5 m", 550, 715, 28, "black", INK2, acc)
            conferido(c, "faz sentido", 440, 775, ep(t, C["31.c"] + 4.0, 0.4), True, 26)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O ÚLTIMO DESTE ASSUNTO", PURPLE)
    rows = [("34.b", "juntamos tudo", BLUE), ("34.c", "caçamos as pegadinhas", AMBER),
            ("34.d", "treinamos: Matemática + Geografia", GREEN)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 420, y - 14, a, 34, bg=col)
        text(c, s, 480, y, 50, "black", INK, a, align="left")
    pill(c, "ep. 4 · revisão e treino para o ENEM", W / 2, 800, PURPLE, size=30, a=ep(t, C["34.a"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Quantos metros quadrados tem o seu quarto?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, defs=b_defs, plantas=b_plantas,
              cem=b_cem, tres=b_tres, quadradinho=b_quadradinho, lados=b_lados, maquete=b_maquete,
              maquete_fachada=b_maquete_fachada, tabela=b_tabela, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q9=b_q9, q5=b_q5, q6=b_q6, q7=b_q7, ponte=b_ponte, cta=b_cta)
