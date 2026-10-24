"""Visual — Taxas Equivalentes e Inflação, Episódio 4: taxa real de juros e a armadilha da subtração (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: fatores() (os três fatores lado a lado: nominal ÷ inflação = real), escada_rolante() (os preços na
escada rolante e o seu dinheiro subindo a pé ao lado), pessoa(), barra_105() (R$ 100 → 105 → 115,50), nota() (cédula),
reta_zero() (a taxa real mais perto do zero que a subtração), linha().
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
_s = importlib.util.spec_from_file_location("comum031", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_taxas_ep4_taxa_real.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
CINZA = "#9AA0A8"
DEGRAU_ESC = "#C9CED6"


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


def contorno(c, x, y, w, h, r, col, a, sw=4):
    if a <= 0:
        return
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), paint(col, a, stroke=sw))


def caixa_fator(c, rot, val, cx, cy, col, a, w=300, size=56):
    """um fator numa caixa, com o rótulo em cima"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - 62, w, 124, 22, mix("#FFFFFF", col, 0.10), a, shadow=True)
    contorno(c, cx - w / 2, cy - 62, w, 124, 22, col, a)
    text(c, rot, cx, cy - 80, 24, "black", col, a)
    fmid(c, val, cx, cy, size, "black", INK, a)


def fatores(c, cx, cy, nom, inf, real, a, a_real=1.0, real_col=None, sinal="=", w=300, gap=110, size=56,
            rots=("NOMINAL", "INFLAÇÃO", "REAL"), op="÷", cols=(BLUE, INK2)):
    """os três fatores lado a lado: nominal ÷ inflação = real"""
    if a <= 0:
        return
    real_col = real_col or GREEN
    xs = [cx - w - gap, cx, cx + w + gap]
    caixa_fator(c, rots[0], nom, xs[0], cy, cols[0], a, w, size)
    fmid(c, op, (xs[0] + xs[1]) / 2, cy, 64, "black", PURPLE, a)
    caixa_fator(c, rots[1], inf, xs[1], cy, cols[1], a, w, size)
    if a_real > 0:
        fmid(c, sinal, (xs[1] + xs[2]) / 2, cy, 64, "black", PURPLE, a * a_real)
        caixa_fator(c, rots[2], real, xs[2], cy, real_col, a * a_real, w, size)


def pessoa(c, x, y, s, a, fase=0.0, col=None):
    """bonequinho andando; (x, y) = os pés; s = altura"""
    if a <= 0:
        return
    col = col or GREEN
    sw = max(4, s * 0.09)
    hip = (x, y - s * 0.45)
    sh = (x, y - s * 0.78)
    c.drawCircle(x, y - s * 0.9, s * 0.11, paint(col, a))
    line(c, hip[0], hip[1], sh[0], sh[1], col, a, sw)
    sp = math.sin(fase) * 0.45
    for sg in (-1, 1):
        line(c, hip[0], hip[1], x + sg * sp * s * 0.4, y, col, a, sw)
        line(c, sh[0], sh[1] + s * 0.05, x - sg * sp * s * 0.35, y - s * 0.5, col, a, sw)


def etiqueta(c, x, y, a, s="PREÇOS"):
    """etiqueta de preço (base em y)"""
    if a <= 0:
        return
    w = ftext_w(s, "black", 24) + 40
    rrect(c, x - w / 2, y - 52, w, 46, 10, "#FFFFFF", a, shadow=True)
    contorno(c, x - w / 2, y - 52, w, 46, 10, CINZA, a, 3)
    c.drawCircle(x - w / 2 + 14, y - 29, 5, paint(CINZA, a))
    fmid(c, s, x + 8, y - 29, 24, "black", INK2, a)


ESC = (360, 770, 1080, 420)     # escada rolante: de (x0, y0) embaixo à esquerda até (x1, y1) em cima à direita


def escada_rolante(c, a, u_tag, u_p, fase, rapido=True, lado=1.0, xr=1560):
    """a escada rolante dos preços (com a etiqueta subindo nela) e o seu dinheiro (a pessoa) subindo a pé ao lado.
    u_tag, u_p ∈ [0, 1]: posição ao longo da escada. lado = intensidade das marcações de nível à direita."""
    if a <= 0:
        return
    x0, y0, x1, y1 = ESC
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = uy, -ux                       # normal "para cima"
    nx, ny = (-nx, -ny) if ny > 0 else (nx, ny)
    th = 34
    # trilho da pessoa (rampa fixa ao lado, acima da escada)
    off = 190
    px0, py0, px1, py1 = x0 + off, y0, x1 + off, y1
    line(c, px0, py0, px1, py1, "#D9DCD5", a, 10)
    # escada rolante: faixa + degraus andando
    p = skia.Path()
    p.moveTo(x0, y0); p.lineTo(x1, y1); p.lineTo(x1 - nx * th, y1 - ny * th); p.lineTo(x0 - nx * th, y0 - ny * th)
    p.close()
    c.drawPath(p, paint("#E9EBEE", a))
    c.drawPath(p, paint(CINZA, a, stroke=3))
    n = 16
    for k in range(n):
        v = (k / n + fase) % 1.0
        sx, sy = x0 + dx * v, y0 + dy * v
        line(c, sx, sy, sx - nx * th, sy - ny * th, DEGRAU_ESC, a, 4)
    # corrimão
    line(c, x0 + nx * 10, y0 + ny * 10 - 4, x1 + nx * 10, y1 + ny * 10 - 4, INK2, a, 5)
    text(c, "ESCADA ROLANTE DOS PREÇOS", x0 + 10, y0 + 50, 22, "black", CINZA, a, align="left")
    # etiqueta e pessoa
    tx, ty = x0 + dx * u_tag, y0 + dy * u_tag
    etiqueta(c, tx, ty - 4, a)
    qx, qy = px0 + (px1 - px0) * u_p, py0 + (py1 - py0) * u_p
    col = GREEN if rapido else RED
    pessoa(c, qx, qy - 4, 110, a, fase * 40, col)
    text(c, "seu dinheiro", qx + 20, qy + 34, 22, "black", col, a, align="left")
    # níveis à direita
    if lado > 0:
        al = a * lado
        yt, yp = ty - 30, qy - 30
        line(c, tx + 60, yt, xr - 60, yt, CINZA, al, 3, dash=(12, 10))
        line(c, qx + 40, yp, xr - 60, yp, col, al, 3, dash=(12, 10))
        text(c, "preços", xr + 10, yt + 8, 24, "black", CINZA, al, align="left")
        text(c, "você", xr + 10, yp + 8, 24, "black", col, al, align="left")
        line(c, xr - 30, yt, xr - 30, yp, col, al, 6)
        for yy in (yt, yp):
            line(c, xr - 44, yy, xr - 16, yy, col, al, 5)


def barra_105(c, x, a, g1, g2, w=170, base=760, k=13.0, v0=80.0):
    """barra de R$ 100 que cresce até 105 (cinza) e depois até 115,50 (verde). Eixo cortado em v0 (≈ na base)."""
    if a <= 0:
        return
    yv = lambda v: base - (v - v0) * k
    rrect(c, x, yv(100), w, base - yv(100), 8, BLUE, a)
    if g1 > 0:
        top = lerp(yv(100), yv(105), g1)
        c.drawRect(skia.Rect.MakeXYWH(x, top, w, yv(100) - top), paint(CINZA, a))
    if g2 > 0:
        top = lerp(yv(105), yv(115.5), g2)
        c.drawRect(skia.Rect.MakeXYWH(x, top, w, yv(105) - top), paint(GREEN, a))
    # corte do eixo
    for k_ in range(2):
        yy = base - 40 - k_ * 14
        p = skia.Path(); p.moveTo(x - 10, yy + 8); p.lineTo(x + w + 10, yy - 8)
        c.drawPath(p, paint("#FFFFFF", a, stroke=7))
    line(c, x - 40, base, x + w + 40, base, INK2, a, 4)
    return yv


def nota(c, cx, cy, val, a, col=GREEN, w=330, h=160, rot=""):
    """cédula estilizada com um valor"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 16, mix("#FFFFFF", col, 0.16), a, shadow=True)
    contorno(c, cx - w / 2 + 12, cy - h / 2 + 12, w - 24, h - 24, 10, col, a, 3)
    fmid(c, val, cx, cy, 48, "black", INK, a)
    if rot:
        text(c, rot, cx, cy + h / 2 + 40, 24, "black", col, a)


def reta_zero(c, x0, x1, y, a, marcas, vmin=-1, vmax=7):
    """reta numérica com o zero destacado; marcas = [(valor, rótulo, cor, alfa)]"""
    if a <= 0:
        return
    X = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    line(c, x0, y, x1, y, INK2, a, 4)
    for v in range(math.ceil(vmin), math.floor(vmax) + 1):
        line(c, X(v), y - 10, X(v), y + 10, INK2, a, 3)
        text(c, str(v).replace("-", "−"), X(v), y + 44, 24, "bold", GRAY, a)
    c.drawCircle(X(0), y, 12, paint(PURPLE, a))
    text(c, "ZERO", X(0), y - 30, 22, "black", PURPLE, a)
    for k, (v, rot, col, al) in enumerate(marcas):
        if al <= 0:
            continue
        c.drawCircle(X(v), y, 14, paint(col, a * al))
        text(c, rot, X(v), y - 34 - (34 if k % 2 else 0), 24, "black", col, a * al)


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

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "TAXAS E INFLAÇÃO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 250, 640, 300, 26, "#FFFFFF", aa, shadow=True)
        text(c, "EXTRATO DA POUPANÇA", 550, 300, 26, "black", BLUE, aa)
        linha(c, [("rendeu ", INK), ("+8%", GREEN)], 550, 380, 60, aa)
        rrect(c, 1050, 250, 640, 300, 26, "#FFFFFF", ep(t, C["01.a"] + 1.6, 0.5), shadow=True)
        a2 = ep(t, C["01.a"] + 1.6, 0.5)
        text(c, "INFLAÇÃO DO ANO", 1370, 300, 26, "black", INK2, a2)
        linha(c, [("preços ", INK), ("+10%", RED)], 1370, 380, 60, a2)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        arrow(c, 420, 515, 420, 470, GREEN, ab, 6, 16)
        text(c, "saldo CRESCEU", 445, 505, 30, "black", GREEN, ab, align="left")
        arrow(c, 1170, 515, 1170, 470, RED, ab, 6, 16)
        text(c, "preços cresceram MAIS", 1195, 505, 30, "black", RED, ab, align="left")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 660, acc, "E MESMO ASSIM: MAIS POBRE", RED, -3, 44)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "QUANTO?", W / 2, 790, PURPLE, ad, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular a TAXA REAL de qualquer rendimento ou reajuste", "poupança · aplicação · salário · preço"),
            ("02.b", "saber quando a SUBTRAÇÃO engana", "12% − 5% = 7%?")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 260, y - 14, 34, a, GREEN)
        ftext(c, s, 320, y, 46, "black", INK, a, align="left")
        ftext(c, sub, 320, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "DO EPISÓDIO 3", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 270, 720, 450, 26, "#FFFFFF", aa, shadow=True)
        text(c, "FATOR DA INFLAÇÃO", 560, 330, 32, "black", BLUE, aa)
        linha(c, [("1 + taxa", PURPLE)], 560, 430, 60, aa)
        linha(c, [("20%  →  ", INK), ("1,20", BLUE)], 560, 580, 66, ep(t, C["03.a"] + 2.0, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 270, 720, 450, 26, "#FFFFFF", ab, shadow=True)
        text(c, "PODER DE COMPRA", 1360, 330, 32, "black", BLUE, ab)
        text(c, "o quanto o seu dinheiro compra", 1360, 380, 24, "bold", GRAY, ab)
        linha(c, [("÷ fator da inflação", PURPLE)], 1360, 500, 52, ab)
        fr(c, "1", "1 + π", 1360, 620, 54, INK, ep(t, C["03.b"] + 1.6, 0.4))


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "AUMENTOU DE VERDADE?", BLUE)
    card(c, *CARD_R)
    items = [("04.a", "MANCHETE", ["juros de 12%", "inflação de 5%", "ganho real de 7%"], BLUE),
             ("04.b", "EXTRATO", ["poupança", "RENDEU", "+ R$ 80"], GREEN),
             ("04.c", "AVISO", ["reajuste salarial", "da categoria", "+6%"], PURPLE)]
    for k, (cue, tit, lns, col) in enumerate(items):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 240, 460, 400, 24, PAPEL if k == 0 else "#FFFFFF", a, shadow=True)
        rrect(c, x, 240, 460, 64, 24, col, a * 0.14)
        text(c, tit, x + 230, 284, 28, "black", col, a)
        for j, s in enumerate(lns):
            ftext(c, s, x + 230, 400 + j * 70, 38 if j < 2 else 46, "black", INK if j < 2 else col, a)
        if k == 0:
            for j in range(4):
                line(c, x + 40, 590 + j * 0 - 20, x + 420, 590 - 20, "#E1E1DC", a, 3)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pergunta(c, "o dinheiro aumentou DE VERDADE?", W / 2, 740, ad, PURPLE, 40)


def b_escada(c, t, C, B):
    head(c, t, B["start"], "A ESCADA ROLANTE", "DE PREÇOS (EPISÓDIO 3)", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["05"], 0.5)
    t1, t2 = C["05.a"], C["05.c"]
    if t < t2:
        g = clamp((t - t1) / max(1.0, t2 - t1 - 0.5))
        u_tag, u_p, rap = 0.10 + 0.55 * g, 0.10 + 0.85 * g, True
    else:
        g = clamp((t - t2) / max(1.0, C["05.end"] - t2 - 0.5))
        u_tag, u_p, rap = 0.10 + 0.70 * g, 0.10 + 0.30 * g, False
    fase = (t - B["start"]) * 0.18
    lado = ep(t, C["05.b"], 0.5) if t < t2 else ep(t, C["05.d"], 0.5)
    escada_rolante(c, a0, u_tag, u_p, fase, rap, lado)
    ab = ep(t, C["05.b"], 0.5) * (1 - ep(t, C["05.c"], 0.3))
    if ab > 0:
        pill(c, "ACIMA da escada = subiu DE VERDADE", 1380, 760, GREEN, size=28, a=ab, anchor="center")
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1380, 260, ad, "TAXA REAL NEGATIVA", RED, -4, 36)
        pill(c, "mais devagar que a escada = DESCENDO", 1380, 760, RED, size=28, a=ad, anchor="center")


# ======================================================================
# bloco a — deflacionar
# ======================================================================

def b_deflacionar(c, t, C, B):
    head_seq(c, t, C, [("06", "DEFLACIONAR", "O DINHEIRO DE ANTIGAMENTE", BLUE), ("07", "DEFLACIONAR", "2 400 ÷ 1,20", PURPLE),
                       ("08", "ATALHO", "TIRE A VÍRGULA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid == "06":
        a0 = ep(t, C["06"], 0.5)
        if a0 > 0:
            nota(c, 560, 330, "R$ 2.000", a0, BLUE, rot="salário ANTES")
            arrow(c, 760, 330, 1150, 330, AMBER, a0, 6, 20)
            text(c, "inflação de 20%", 955, 300, 26, "black", AMBER, a0)
            nota(c, 1360, 330, "R$ 2.400", a0, GREEN, rot="salário DEPOIS")
            pergunta(c, "aumentou DE VERDADE?", W / 2, 500, ep(t, C["06"] + 4.5, 0.4), PURPLE, 34)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            boxed(c, 260, 580, 1400, 200, BLUE, ab, 0.08)
            text(c, "DEFLACIONAR", W / 2, 630, 30, "black", BLUE, ab, tracking=2)
            ftext(c, "traduzir um valor de HOJE para o dinheiro de ANTIGAMENTE", W / 2, 690, 36, "black", INK, ab)
            linha(c, [("÷ fator da inflação", PURPLE)], W / 2, 742, 34, ab)
        return
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            nota(c, 470, 330, "R$ 2.400", aa, GREEN, rot="dinheiro de HOJE")
            arrow(c, 670, 330, 1050, 330, PURPLE, aa, 6, 20)
            text(c, "÷ 1,20", 860, 300, 40, "black", PURPLE, aa)
            a2 = ep(t, C["07.a"] + 2.4, 0.5)
            nota(c, 1250, 330, "R$ 2.000", a2, BLUE, rot="")
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            pill(c, "VALOR EM DINHEIRO DA DATA ANTIGA", 1250, 450, BLUE, size=24, a=ab, anchor="center")
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            linha(c, [("antes: ", INK2), ("R$ 2.000", BLUE), ("   =   ", INK), ("hoje, deflacionado: ", INK2),
                      ("R$ 2.000", BLUE)], W / 2, 560, 40, acc)
            conferido(c, "poder de compra IGUAL", 760, 650, ep(t, C["07.c"] + 2.0, 0.4), True, 36)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            regra(c, "+20% em reais só REPÔS a inflação: aumento real = 0", W / 2, 760, ad, 36)
        return
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 300, 230, 1320, 170, "ATALHO · TIRE A VÍRGULA", ["multiplique os DOIS números por 10"], aa, 40)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        linha(c, [("2 400 ÷ 1,20", INK)], W / 2, 500, 70, ab)
        a2 = ep(t, C["08.b"] + 1.6, 0.4)
        text_mid(c, "× 10        × 10", W / 2, 580, 34, "black", GREEN, a2)
        linha(c, [("24 000 ÷ 12 = ", INK), ("2 000", GREEN)], W / 2, 680, 70, ep(t, C["08.b"] + 3.0, 0.4))


# ======================================================================
# bloco b — nominal × real
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "DUAS TAXAS EM JOGO", "NOMINAL × REAL", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 250, 700, 360, BLUE, aa, 0.08)
        text(c, "TAXA NOMINAL", 570, 310, 38, "black", BLUE, aa)
        text(c, "(ou APARENTE)", 570, 360, 28, "bold", BLUE, aa)
        ftext(c, "quanto o saldo cresceu", 570, 460, 36, "black", INK, aa)
        ftext(c, "EM REAIS", 570, 520, 44, "black", BLUE, aa)
        text(c, "a do extrato", 570, 580, 24, "bold", GRAY, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        boxed(c, 1000, 250, 700, 360, GREEN, ab, 0.08)
        text(c, "TAXA REAL", 1350, 310, 38, "black", GREEN, ab)
        text(c, "(descontada a inflação)", 1350, 360, 28, "bold", GREEN, ab)
        ftext(c, "quanto cresceu o seu", 1350, 460, 36, "black", INK, ab)
        ftext(c, "PODER DE COMPRA", 1350, 520, 44, "black", GREEN, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 660, 1400, 130, 24, "#F7F7F5", acc)
        linha(c, [("escada: nominal = quanto você ", INK2), ("subiu", BLUE)], W / 2, 700, 32, acc)
        linha(c, [("real = quanto você subiu ", INK2), ("ACIMA da escada", GREEN)], W / 2, 755, 32,
              ep(t, C["09.c"] + 1.8, 0.4))


# ======================================================================
# bloco c — R$ 100 → 105 → 115,50 e a relação dos fatores
# ======================================================================

def b_barra(c, t, C, B):
    head(c, t, B["start"], "SOMAR OU SUBTRAIR?", "R$ 100 → 105 → 115,50", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    g1 = ep(t, C["10.b"] + 0.4, 1.4)
    g2 = ep(t, C["10.d"] + 0.3, 1.6)
    x = 360
    yv = barra_105(c, x, aa, g1, g2) if aa > 0 else None
    if aa > 0:
        text_mid(c, "R$ 100", x + 85, yv(100) + 70, 34, "black", "#FFFFFF", aa)
        linha(c, [("R$ 100 aplicados  ·  inflação de ", INK), ("5%", INK2)], 1180, 260, 36, aa)
    if g1 > 0:
        line(c, x + 180, yv(105), x + 260, yv(105), CINZA, g1, 3)
        text(c, "R$ 105", x + 270, yv(105) + 12, 34, "black", INK2, g1, align="left")
        ftext(c, "+ R$ 5: só ACOMPANHOU a inflação", 1180, 420, 32, "black", INK2, ep(t, C["10.b"] + 1.6, 0.4))
        ftext(c, "(não é ganho)", 1180, 465, 26, "bold", GRAY, ep(t, C["10.b"] + 1.6, 0.4))
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("ganho real de 10% ", GREEN), ("DE QUÊ?", AMBER)], 1180, 560, 40, acc)
        linha(c, [("10% de ", INK), ("105", INK2), (" = R$ 10,50", GREEN)], 1180, 625, 36, ep(t, C["10.c"] + 2.4, 0.4))
    if g2 > 0:
        line(c, x + 180, yv(115.5), x + 260, yv(115.5), GREEN, g2, 3)
        text(c, "R$ 115,50", x + 270, yv(115.5) + 12, 38, "black", GREEN, g2, align="left")
        linha(c, [("105 × 1,10 = ", INK), ("115,50", GREEN)], 1180, 730, 46, ep(t, C["10.d"] + 1.0, 0.4))


def b_relacao(c, t, C, B):
    head_seq(c, t, C, [("11", "OS FATORES", "SE MULTIPLICAM", PURPLE), ("12", "A TAXA REAL", "DIVIDA OS FATORES", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            linha(c, [("rendimento: ", INK), ("R$ 15,50", GREEN), ("  (não R$ 15)", AMBER)], W / 2, 270, 44, aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            fatores(c, W / 2, 470, "1,10", "1,05", "1,155", ab, ep(t, C["11.b"] + 2.6, 0.4), BLUE, sinal="=",
                    rots=("REAL", "INFLAÇÃO", "NOMINAL"), op="×", cols=(GREEN, INK2))
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            regra(c, "fator NOMINAL  =  fator REAL  ×  fator da INFLAÇÃO", W / 2, 700, acc, 38)
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        text_mid(c, "1 + taxa real  =", 640, 380, 56, "black", INK, aa)
        fr(c, "fator NOMINAL", "fator da INFLAÇÃO", 1180, 370, 54, INK, aa, num_col=BLUE, den_col=INK2)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        regra(c, "DIVIDA os fatores, NUNCA subtraia as taxas", W / 2, 620, ab, 44)
        linha(c, [("12% − 5%", RED)], 1500, 740, 40, ab)
        strike(c, 1410, 744, 1590, 744, ab, RED, ep(t, C["12.b"] + 1.2, 0.4))


# ======================================================================
# bloco d — os dois exemplos
# ======================================================================

def b_exemplos(c, t, C, B):
    head_seq(c, t, C, [("13", "EXEMPLO 1", "RENDEU 15,5% · INFLAÇÃO 5%", PURPLE),
                       ("14", "EXEMPLO 2", "RENDEU 8% · INFLAÇÃO 10%", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        fatores(c, W / 2, 330, "1,155", "1,05", "1,10", aa, ep(t, C["13.b"], 0.4))
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            selo(c, W / 2 + 410, 460, ab, "GANHO REAL DE 10%", GREEN, -3, 32)
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            K.atalho(c, 360, 560, 1200, 210, "ATALHO · MULTIPLIQUE DE VOLTA",
                     ["real × inflação = nominal?", "1,10 × 1,05 = 1,155  ✓"], acc, 38)
        return
    aa = ep(t, C["14.a"], 0.5)
    fatores(c, W / 2, 330, "1,08", "1,10", "≈ 0,982", aa, ep(t, C["14.a"] + 2.6, 0.4), RED, sinal="=")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("fator ABAIXO de 1  →  taxa real ≈ ", INK), ("−1,8%", RED), ("  =  PERDA", RED)], W / 2, 490, 40, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        selo(c, 640, 640, acc, "TAXA REAL NEGATIVA", RED, -4, 40)
        ftext(c, "andou MAIS DEVAGAR que a escada", 640, 740, 30, "black", RED, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 1100, 580, 560, 200, 22, "#FFFFFF", ad, shadow=True)
        linha(c, [("saldo em reais ", INK), ("↑", GREEN)], 1380, 640, 40, ad)
        linha(c, [("o que ele compra ", INK), ("↓", RED)], 1380, 720, 40, ep(t, C["14.d"] + 1.4, 0.4))


# ======================================================================
# bloco e — a aproximação por subtração
# ======================================================================

def _linha_tab(c, y, nom, inf, sub, exa, veredito, ok, a):
    if a <= 0:
        return
    rrect(c, 200, y - 50, 1520, 100, 18, "#F7F7F5", a)
    ftext(c, nom, 330, y + 12, 34, "black", BLUE, a)
    ftext(c, inf, 610, y + 12, 34, "black", INK2, a)
    ftext(c, sub, 900, y + 12, 34, "black", AMBER, a)
    ftext(c, exa, 1220, y + 12, 34, "black", GREEN, a)
    ftext(c, veredito, 1560, y + 12, 30, "black", GREEN if ok else RED, a)


def b_aproximacao(c, t, C, B):
    head_seq(c, t, C, [("15", "A MANCHETE ERRA?", "A APROXIMAÇÃO", AMBER), ("16", "COM TAXAS GRANDES", "A SUBTRAÇÃO FALHA", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["15.b"], 0.5)
    if a0 > 0:
        for x_, s in ((330, "NOMINAL"), (610, "INFLAÇÃO"), (900, "SUBTRAÇÃO"), (1220, "EXATA"), (1560, "ERRO")):
            text(c, s, x_, 408, 22, "black", GRAY, a0)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 260, 1320, 120, AMBER, aa, 0.08)
        text(c, "APROXIMAÇÃO: uma conta que só chega PERTO do valor certo", W / 2, 305, 28, "black", AMBER, aa)
        linha(c, [("taxa real  ≈  nominal − inflação", PURPLE)], W / 2, 348, 34, aa)
    _linha_tab(c, 470, "1% ao mês", "0,5% ao mês", "0,5%", "≈ 0,4975%", "desprezível", True, ep(t, C["15.b"], 0.5))
    if t >= C["15.c"]:
        conferido(c, "taxas pequenas: a subtração quase acerta", 560, 580, ep(t, C["15.c"], 0.4), True, 32)
    if t < C["16"]:
        return
    _linha_tab(c, 580, "26%", "20%", "6%", "5%", "1 ponto!", False, ep(t, C["16.a"], 0.5))
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        linha(c, [("1,26 ÷ 1,20 = ", INK), ("1,05", GREEN), ("  →  5%", GREEN)], 640, 690, 36, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        pill(c, "NA PROVA: conta EXATA · a subtração só confere a ordem de grandeza", 640, 790, PURPLE, size=22,
             a=acc, anchor="center")
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        reta_zero(c, 1150, 1700, 762, ad, [(5, "real 5", GREEN, ep(t, C["16.d"] + 0.8, 0.4)),
                                           (6, "subtr. 6", AMBER, ep(t, C["16.d"] + 1.4, 0.4))])
        text(c, "a real fica MAIS PERTO DO ZERO", 1425, 668, 24, "black", GREEN, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "OS TRÊS FATORES", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("rendeu ", INK), ("32%", BLUE), ("  ·  inflação ", INK), ("10%", INK2), ("  →  taxa real = ?", INK)],
              W / 2, 285, 52, aa)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 560)
    if t < C["18"]:
        return
    a1 = ep(t, C["18.a"], 0.4)
    fatores(c, W / 2, 490, "1,32", "1,10", "1,20", a1, ep(t, C["18.b"], 0.4))
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        linha(c, [("tire a vírgula: 132 ÷ 110 = 1,20  →  ", INK2), ("20%", GREEN)], W / 2, 640, 36, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        conferido(c, "de volta: 1,20 × 1,10 = 1,32", 420, 730, acc, True, 32)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        linha(c, [("subtração: 32 − 10 = ", AMBER), ("22%", RED)], 1380, 730, 34, ad)
        strike(c, 1260, 734, 1530, 734, ad, RED, ep(t, C["18.d"] + 1.0, 0.4))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Taxa real: divida o fator nominal pelo fator da inflação.",
          "Subtrair as taxas é só uma estimativa; na prova, divida.",
          "Rendimento abaixo da inflação é perda, mesmo com saldo maior."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Taxa real = nominal − inflação: 26% − 20% = 6%", "é o que a manchete faz",
          "divida os fatores: 1,26 ÷ 1,20 = 1,05 → 5%, não 6%"),
         ("Rendimento positivo é sempre ganho", "o número no extrato aumentou",
          "render 8% com inflação de 10% é PERDER poder de compra: compare com a escada")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21"], ERROS)


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


def _fatores_mini(c, cx, cy, nom, inf, real, a, a_real, real_col=None):
    fatores(c, cx, cy, nom, inf, real, a, a_real, real_col, w=190, gap=50, size=36)


ALTS6 = [("A", "4,76%", "divisão invertida", RED), ("B", "5,00%", "", GREEN), ("C", "6,00%", "subtração", AMBER),
         ("D", "46,00%", "somou as taxas", RED), ("E", "51,20%", "multiplicou os fatores", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · EU FAÇO", "TAXA REAL", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Um investidor aplicou suas economias por um ano e obteve rendimento de 26%. No mesmo ano, a "
                           "inflação foi de 20%. A taxa real de rendimento dessa aplicação foi de", INK)], a0, 240, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS6, 1000, 250, 680, 44, C["23.ok"], "B", cues_in, cues_x, gap=34)
    if t >= C["23"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["23"], 0.4))
        _fatores_mini(c, 540, y0 + 110, "1,26", "1,20", "1,05", ep(t, C["23.a"], 0.4), ep(t, C["23.b"], 0.4))
        linha(c, [("12,6 ÷ 12 = 1,05  →  ", INK2), ("5%", GREEN)], 540, y0 + 220, 30, ep(t, C["23.b"], 0.4))
        conferido(c, "5 fica mais perto do zero que 6", 230, y0 + 290, ep(t, C["23.c"], 0.4), True, 26)


ALTS8 = [("A", "15%", "", GREEN), ("B", "18%", "subtraiu 38 − 20", AMBER), ("C", "38%", "aumento nominal", RED),
         ("D", "58%", "somou 38 + 20", RED), ("E", "138%", "fator lido como taxa", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · NÓS FAZEMOS", "AUMENTO REAL DE UM PREÇO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("O preço de um eletrodoméstico passou de R$ 200,00 para R$ 276,00 em um período no qual a "
                           "inflação acumulada foi de 20%. Descontada a inflação, o preço desse eletrodoméstico teve um "
                           "aumento real de", INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS8, 1000, 250, 680, 44, C["26.ok"], "A", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 140)
    if t >= C["26"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["26"], 0.4))
        pill(c, "AUMENTO REAL = descontada a inflação", 540, y0 + 38, BLUE, size=20, a=ep(t, C["26"], 0.4),
             anchor="center")
        linha(c, [("1º deflacione: 276 ÷ 1,20 = ", INK), ("230", BLUE)], 540, y0 + 95, 28, ep(t, C["26.a"], 0.4))
        linha(c, [("230 ÷ 200 = ", INK), ("1,15", GREEN)], 540, y0 + 145, 28, ep(t, C["26.a"] + 4.0, 0.4))
        linha(c, [("2º fatores: 276 ÷ 200 = 1,38", INK)], 540, y0 + 205, 28, ep(t, C["26.b"], 0.4))
        linha(c, [("1,38 ÷ 1,20 = ", INK), ("1,15", GREEN)], 540, y0 + 255, 28, ep(t, C["26.b"] + 3.4, 0.4))
        conferido(c, "os dois batem: 15%", 300, y0 + 315, ep(t, C["26.c"], 0.4), True, 28)


ALTS7 = [("A", "ganho de 4%.", "trocou o sinal", RED), ("B", "ganho de cerca de 3,6%.", "trocou o sinal", RED),
         ("C", "perda de 16%.", "somou 6 + 10", RED), ("D", "perda de 4%.", "subtração: exagera", AMBER),
         ("E", "perda de cerca de 3,6%.", "", GREEN)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · VOCÊ FAZ", "REAJUSTE E INFLAÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, [("Uma categoria profissional recebeu reajuste salarial de 6% em um ano no qual a inflação foi "
                           "de 10%. Considere 1,06 ÷ 1,10 ≈ 0,964. Em termos reais, esses trabalhadores tiveram", INK)],
                      a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["29"], 0.3)),
         align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS7, 1000, 250, 680, 40, C["29.ok"], "E", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["28.end"] - 1.9, 540, yend + 140)
    if t >= C["29"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["29"], 0.4))
        pill(c, "6% < 10%: mais devagar que a escada → PERDA", 540, y0 + 40, RED, size=20, a=ep(t, C["29.a"], 0.4),
             anchor="center")
        _fatores_mini(c, 540, y0 + 175, "1,06", "1,10", "≈ 0,964", ep(t, C["29.b"], 0.4), ep(t, C["29.b"] + 1.6, 0.4),
                      RED)
        linha(c, [("compra 96,4%  →  perda ≈ ", INK2), ("3,6%", RED)], 540, y0 + 280, 28, ep(t, C["29.b"] + 3.0, 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    for k, (cue, s, col) in enumerate((("32.a", "juntamos TUDO", BLUE), ("32.b", "caçamos as PEGADINHAS", AMBER),
                                       ("32.c", "QUESTÕES INÉDITAS", GREEN))):
        a = ep(t, C[cue], 0.5)
        chip(c, s, W / 2, 330 + k * 150, col, a, 48)
    pill(c, "ep. 5 · revisão de Taxas Equivalentes e Inflação", W / 2, 790, PURPLE, size=30,
         a=ep(t, C["32.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Seu último reajuste ganhou ou perdeu da inflação?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, escada=b_escada,
              deflacionar=b_deflacionar, definicao=b_definicao, barra=b_barra, relacao=b_relacao, exemplos=b_exemplos,
              aproximacao=b_aproximacao, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q6=b_q6, q8=b_q8, q7=b_q7,
              ponte=b_ponte, cta=b_cta)
