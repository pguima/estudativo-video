"""Visual — Velocidade, Densidade e Vazão, Episódio 4: densidade, identificar o material e decidir se flutua (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: cubo() (cubinho de 1 cm³ em perspectiva, na cor do material), balanca(), aquario() (água, camada
de óleo, quem boia fica com a fração d submersa e quem afunda desce até o fundo), triangulo() (o triângulo da densidade,
com o dedo tampando o que se procura), prego(), portao(), ranking() (a tabela como barras, com a régua da água em 1).
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
ARQUIVO_FINAL = "enem_matematica_velocidade_densidade_vazao_ep4_densidade.mp4"
CARD_R = K.CARD_R
AGUA = "#9CC9F0"
AGUA_ESC = "#5B9BD5"
VIDRO = "#7FA7C9"
DEDO = "#F1C29C"

# material: (nome, densidade, cor)
MATS = [("óleo", 0.8, "#E9C46A"), ("gelo", 0.92, "#D8EEFB"), ("água", 1.0, AGUA), ("água do mar", 1.03, AGUA_ESC),
        ("alumínio", 2.7, "#C3C9D0"), ("ferro", 7.8, "#7A818B"), ("chumbo", 11.3, "#55606E"), ("ouro", 19.3, "#E3B341")]
COR = {n: col for n, _, col in MATS}


def dv(d):
    """densidade com vírgula: 0.92 -> '0,92'"""
    s = f"{d:g}".replace(".", ",")
    return s + (",0" if d == 1 else "")


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def cubo(c, cx, cy, s, col, a, rotulo=None, rsize=None, pontos=0):
    """cubinho em perspectiva (frente s × s centrada em cx, cy); pontos = bolinhas de 'massa espremida' na frente"""
    if a <= 0:
        return
    d = s * 0.32
    x0, y0 = cx - s / 2, cy - s / 2
    top = skia.Path(); top.moveTo(x0, y0); top.lineTo(x0 + d, y0 - d); top.lineTo(x0 + s + d, y0 - d)
    top.lineTo(x0 + s, y0); top.close()
    side = skia.Path(); side.moveTo(x0 + s, y0); side.lineTo(x0 + s + d, y0 - d); side.lineTo(x0 + s + d, y0 + s - d)
    side.lineTo(x0 + s, y0 + s); side.close()
    c.drawPath(top, paint(mix(col, "#FFFFFF", 0.35), a))
    c.drawPath(side, paint(mix(col, INK, 0.22), a))
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, s, s), paint(col, a))
    edge = paint(mix(col, INK, 0.45), a, stroke=max(1.5, s * 0.025))
    for p in (top, side):
        c.drawPath(p, edge)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, s, s), edge)
    if pontos:
        n = int(math.ceil(math.sqrt(pontos)))
        k = 0
        for i in range(n):
            for j in range(n):
                if k >= pontos:
                    break
                px = x0 + s * (i + 0.5) / n + (j % 2) * s * 0.04
                py = y0 + s * (j + 0.5) / n
                c.drawCircle(px, py, max(2.0, s / n * 0.22), paint(mix(col, INK, 0.7), a))
                k += 1
    if rotulo:
        text(c, rotulo, cx + d / 2, cy + s / 2 + (rsize or 22) + 10, rsize or 22, "black", INK2, a)


def balanca(c, cx, cy, w, a, leitura="", col=INK):
    """balança de cozinha: prato em cy (o objeto fica em cima), corpo e visor embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w * 0.5, cy, w, 16, 8, "#AEB4BC", a)
    rrect(c, cx - w * 0.06, cy + 16, w * 0.12, 18, 4, "#8E949C", a)
    rrect(c, cx - w * 0.42, cy + 34, w * 0.84, 110, 22, "#E9ECEF", a, shadow=True)
    rrect(c, cx - w * 0.3, cy + 56, w * 0.6, 64, 12, "#22313F", a)
    if leitura:
        text_mid(c, leitura, cx, cy + 88, 36, "black", "#7CF2B0", a)


def nuvem(c, cx, cy, s, a):
    """saco de algodão (nuvem branca)"""
    if a <= 0:
        return
    for dx, dy, r in ((-0.45, 0.1, 0.42), (0.0, -0.15, 0.55), (0.45, 0.08, 0.45), (-0.15, 0.3, 0.45), (0.25, 0.3, 0.42)):
        c.drawCircle(cx + dx * s, cy + dy * s, r * s, paint("#FFFFFF", a))
    for dx, dy, r in ((-0.45, 0.1, 0.42), (0.0, -0.15, 0.55), (0.45, 0.08, 0.45)):
        c.drawCircle(cx + dx * s, cy + dy * s, r * s, paint("#D9DDE2", a, stroke=3))


def aquario(c, x, y, w, h, a, itens=(), oleo=0.0, nivel=0.30):
    """aquário: água a partir de y + h·nivel. itens = [(nome, d, xfrac, u, rotulo)] com u = 0 → 1 (caindo).
    d < 1: boia com a fração d submersa; d > 1: afunda até o fundo. oleo = espessura (0 → 1) da camada de óleo."""
    if a <= 0:
        return
    wy = y + h * nivel
    rrect(c, x, y, w, h, 18, "#FFFFFF", a * 0.6)
    c.drawRect(skia.Rect.MakeXYWH(x + 6, wy, w - 12, y + h - wy - 6), paint(mix("#FFFFFF", AGUA, 0.75), a))
    eo = 0
    if oleo > 0:
        eo = 34 * oleo
        c.drawRect(skia.Rect.MakeXYWH(x + 6, wy - eo, w - 12, eo), paint(mix("#FFFFFF", COR["óleo"], 0.85), a))
        text(c, "óleo 0,8", x + w - 90, wy - eo / 2 + 9, 22, "black", mix(COR["óleo"], INK, 0.45), a * oleo)
    line(c, x + 6, wy - eo, x + w - 6, wy - eo, AGUA_ESC if not eo else mix(COR["óleo"], INK, 0.3), a, 3)
    s = 74
    for nome, d, xf, u, rot in itens:
        if u <= 0:
            continue
        cx = x + w * xf
        if d < 1:
            yf = wy - eo + s * (d - 0.5)                    # centro: fração d abaixo da linha
        else:
            yf = y + h - 10 - s / 2
        uu = ease_out(clamp(u))
        cy = lerp(y - s * 0.4, yf, uu)
        cubo(c, cx, cy, s, COR[nome], a * clamp(u * 4))
        if rot and u >= 0.98:
            pill(c, rot, cx, (cy - s / 2 - 40) if d < 1 else (cy - s / 2 - 34), mix(COR[nome], INK, 0.5) if d >= 1
                 else BLUE, size=20, a=a, anchor="center")
    # água por cima (transparência sobre o que está submerso)
    c.drawRect(skia.Rect.MakeXYWH(x + 6, wy, w - 12, y + h - wy - 6), paint(AGUA, a * 0.28))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(VIDRO, a, stroke=5))


def triangulo(c, cx, cy, R, a, tampa=None, ta=0.0):
    """o triângulo da densidade: m em cima; d × V embaixo. tampa = 'd' | 'm' | 'V' (o dedo cobre essa letra)"""
    if a <= 0:
        return
    h = R * 1.5
    top, bl, br = (cx, cy - h * 0.62), (cx - R * 0.95, cy + h * 0.38), (cx + R * 0.95, cy + h * 0.38)
    p = skia.Path(); p.moveTo(*top); p.lineTo(*bl); p.lineTo(*br); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", PURPLE, 0.10), a))
    c.drawPath(p, paint(PURPLE, a, stroke=6))
    ym = cy - h * 0.08
    xl = lerp(top[0], bl[0], (ym - top[1]) / (bl[1] - top[1]))
    line(c, xl, ym, 2 * cx - xl, ym, PURPLE, a, 5)
    line(c, cx, ym, cx, bl[1], PURPLE, a, 5)
    pos = dict(m=(cx, cy - h * 0.27), d=(cx - R * 0.36, cy + h * 0.17), V=(cx + R * 0.36, cy + h * 0.17))
    cols = dict(m=GREEN, d=BLUE, V=AMBER)
    for k, (px, py) in pos.items():
        fmid(c, k, px, py, R * 0.42, "black", cols[k], a)
    text_mid(c, "×", cx, cy + h * 0.17 - 4, R * 0.22, "black", INK2, a * 0.8)
    if tampa and ta > 0:
        px, py = pos[tampa]
        rr = R * 0.30
        yy = lerp(py - R * 0.9, py, ease_out(ta))
        rrect(c, px - rr * 0.8, yy - rr, rr * 1.6, rr * 2.4, rr * 0.8, DEDO, a * clamp(ta * 3), shadow=True)
        rrect(c, px - rr * 0.5, yy - rr * 0.8, rr * 1.0, rr * 0.7, rr * 0.3, "#F8DCC6", a * clamp(ta * 3))


def prego(c, x, y, L, a):
    """prego deitado: cabeça em x, ponta em x + L"""
    if a <= 0:
        return
    rrect(c, x, y - L * 0.09, L * 0.05, L * 0.18, 3, "#6E7681", a)
    p = skia.Path(); p.moveTo(x + L * 0.05, y - L * 0.03); p.lineTo(x + L * 0.88, y - L * 0.03); p.lineTo(x + L, y)
    p.lineTo(x + L * 0.88, y + L * 0.03); p.lineTo(x + L * 0.05, y + L * 0.03); p.close()
    c.drawPath(p, paint("#8C939C", a))
    c.drawPath(p, paint("#5A616B", a, stroke=2))


def portao(c, x, y, w, h, a):
    if a <= 0:
        return
    st = paint("#5A616B", a, stroke=10)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), st)
    n = 7
    for i in range(1, n):
        xx = x + w * i / n
        c.drawLine(xx, y, xx, y + h, paint("#6E7681", a, stroke=7))
        c.drawCircle(xx, y - 10, 7, paint("#6E7681", a))
    c.drawLine(x, y + h * 0.5, x + w, y + h * 0.5, paint("#6E7681", a, stroke=7))


def etiqueta(c, s, cx, cy, a, col=PURPLE, size=30):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 50
    rrect(c, cx - w / 2, cy - size * 0.95, w, size * 1.9, 12, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - size * 0.95, 14, size * 1.9, 6, col, a)
    fmid(c, s, cx + 6, cy, size, "black", col, a)


def ranking(c, t, ts, x, y0, a, wmax=930, dy=62):
    """a tabela como barras; ts = instante de entrada de cada linha; régua da água em d = 1"""
    if a <= 0:
        return
    k = wmax / 19.3
    for i, (nome, d, col) in enumerate(MATS):
        ai = a * ep(t, ts[i], 0.4)
        if ai <= 0:
            continue
        y = y0 + i * dy
        text(c, nome, x - 24, y + 12, 28, "black", INK, ai, align="right")
        g = ep(t, ts[i], 0.8)
        rrect(c, x, y - 18, max(8, d * k * g), 40, 8, col, ai)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - 18, max(8, d * k * g), 40), 8, 8),
                    paint(mix(col, INK, 0.3), ai, stroke=2))
        text(c, dv(d) + " g/cm³", x + max(8, d * k * g) + 16, y + 12, 26, "black", INK2, ai, align="left")
    xa = x + k
    line(c, xa, y0 - 50, xa, y0 + 7.5 * dy, BLUE, a, 3, dash=(10, 8))
    text(c, "água = 1", xa, y0 - 60, 24, "black", BLUE, a)


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DENSIDADE", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        balanca(c, 520, 520, 420, aa, "156 g" if t > C["01.a"] + 1.0 else "0 g")
        cubo(c, 500, 456, 110, COR["ferro"], aa * ep(t, C["01.a"] + 0.6, 0.4))
        etiqueta(c, "20 cm³", 760, 380, ep(t, C["01.a"] + 2.4, 0.4), BLUE, 28)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        linha(c, [("156 g ÷ 20 cm³ = ", INK), ("7,8 g/cm³", PURPLE)], 1300, 300, 46, ab)
        for k, (nome, d) in enumerate((("alumínio", 2.7), ("ferro", 7.8), ("chumbo", 11.3), ("ouro", 19.3))):
            y = 420 + k * 82
            ak = ep(t, C["01.b"] + 1.2 + 0.3 * k, 0.4)
            ok = nome == "ferro"
            rrect(c, 1040, y - 34, 520, 68, 16, mix("#FFFFFF", GREEN if ok else LIGHT, 0.18 if ok else 0.25), ak)
            cubo(c, 1090, y, 40, COR[nome], ak)
            text(c, nome, 1140, y + 11, 32, "black", INK, ak, align="left")
            text(c, dv(d) + " g/cm³", 1530, y + 11, 28, "bold", INK2, ak, align="right")
            if ok:
                check_icon(c, 1600, y, 26, ep(t, C["01.b"] + 2.6, 0.4), GREEN)
            else:
                xs = ep(t, C["01.b"] + 2.6, 0.4)
                strike(c, 1135, y, 1535, y, xs, RED, xs)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, 1330, 770, acc, "BALANÇA + RÉGUA = LABORATÓRIO", GREEN, -3, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular a densidade", "d = m ÷ V  ·  em g/cm³"),
            ("02.b", "achar a massa a partir do volume", "m = d × V"),
            ("02.c", "decidir se algo flutua", "só comparando números")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "AS 3 PERGUNTAS DA TAXA (ep. 1)", 560, 290, 32, "black", PURPLE, aa)
        rows = [("quer a taxa?", "÷  divida"), ("quer o de cima?", "×  multiplique"), ("quer o de baixo?", "÷  ao contrário")]
        for k, (q, r) in enumerate(rows):
            ak = ep(t, C["03.a"] + 1.2 + 1.3 * k, 0.4)
            y = 390 + k * 100
            text(c, q, 520, y, 32, "bold", INK2, ak, align="right")
            text(c, r, 560, y, 38, "black", PURPLE, ak, align="left")
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "DA SÉRIE DE UNIDADES", 1380, 290, 32, "black", BLUE, ab)
        linha(c, [("1 mL = ", INK), ("1 cm³", BLUE)], 1380, 410, 56, ab)
        a2 = ep(t, C["03.b"] + 2.4, 0.4)
        linha(c, [("1 L de água = ", INK), ("1 kg", BLUE)], 1380, 540, 56, a2)
    line(c, 960, 260, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "O QUE PESA MAIS?", "1 kg DE CHUMBO OU 1 kg DE ALGODÃO", BLUE),
                       ("05", "QUEM SOBE, QUEM DESCE?", "GELO NO COPO · ÓLEO NA PANELA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        a0 = ep(t, C["04"], 0.5)
        balanca(c, 560, 560, 420, a0, "1 kg")
        balanca(c, 1360, 560, 420, a0, "1 kg")
        g = ep(t, C["04.b"], 1.0)
        cubo(c, 545, 560 - 24 - 18 * (1 + g * 0.2), 48 * (1 + g * 0.2), COR["chumbo"], a0)
        nuvem(c, 1360, 560 - 60 - 70 * (0.6 + g * 0.6), 120 * (0.6 + g * 0.6), a0)
        text(c, "chumbo", 560, 790, 30, "black", INK2, a0)
        text(c, "algodão", 1360, 790, 30, "black", INK2, a0)
        aa = ep(t, C["04.a"], 0.4)
        text_mid(c, "=", W / 2, 640, 110, "black", GREEN, aa)
        text(c, "pesam IGUAL", W / 2, 740, 30, "black", GREEN, aa)
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            pill(c, "mesma MASSA, espaços MUITO diferentes", W / 2, 270, AMBER, size=30, a=acc, anchor="center")
        return
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        x, y, w, h = 300, 300, 360, 400
        rrect(c, x, y, w, h, 30, "#FFFFFF", aa * 0.6)
        wy = y + h * 0.35
        c.drawRect(skia.Rect.MakeXYWH(x + 6, wy, w - 12, h - (wy - y) - 6), paint(mix("#FFFFFF", AGUA, 0.7), aa))
        bob = math.sin(t * 2.2) * 4
        cubo(c, x + w / 2, wy + 90 * (0.92 - 0.5) + bob, 90, COR["gelo"], aa)
        c.drawRect(skia.Rect.MakeXYWH(x + 6, wy, w - 12, h - (wy - y) - 6), paint(AGUA, aa * 0.25))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), paint(VIDRO, aa, stroke=5))
        text(c, "gelo BOIA", x + w / 2, 770, 32, "black", BLUE, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        x, y, w, h = 780, 420, 460, 260
        c.drawRect(skia.Rect.MakeXYWH(x, y + 90, w, h - 90), paint(mix("#FFFFFF", AGUA, 0.7), ab))
        c.drawRect(skia.Rect.MakeXYWH(x, y + 50, w, 40), paint(mix("#FFFFFF", COR["óleo"], 0.6), ab))
        p = skia.Path(); p.moveTo(x, y + 20); p.lineTo(x, y + h - 20); p.quadTo(x, y + h, x + 30, y + h)
        p.lineTo(x + w - 30, y + h); p.quadTo(x + w, y + h, x + w, y + h - 20); p.lineTo(x + w, y + 20)
        c.drawPath(p, paint("#4B5563", ab, stroke=12))
        rrect(c, x + w, y + 40, 180, 26, 12, "#4B5563", ab)
        text(c, "óleo POR CIMA", x + w / 2, 770, 32, "black", mix(COR["óleo"], INK, 0.45), ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        text_mid(c, "?", 1530, 470, 160, "black", AMBER, acc * (1 - ep(t, C["05.d"], 0.3)))
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        chip(c, "DENSIDADE", 1540, 480, BLUE, ad, 46)


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("06", "DUAS PALAVRAS", "MASSA · VOLUME", BLUE), ("07", "DENSIDADE", "MASSA SOBRE VOLUME", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            text(c, "MASSA", 520, 290, 52, "black", BLUE, aa)
            text(c, "quantidade de matéria: o que a balança mede", 520, 345, 26, "bold", GRAY, aa)
            balanca(c, 520, 540, 360, aa, "g · kg")
            cubo(c, 505, 488, 70, COR["alumínio"], aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            text(c, "VOLUME", 1400, 290, 52, "black", BLUE, ab)
            text(c, "o espaço que o objeto ocupa", 1400, 345, 26, "bold", GRAY, ab)
            cubo(c, 1380, 520, 170, mix("#FFFFFF", BLUE, 0.25), ab)
            text(c, "cm³ · L", 1400, 690, 40, "black", INK, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            pill(c, "1 cm³ = um cubinho de 1 cm de lado (um dado pequeno)", W / 2, 780, BLUE, size=28, a=acc,
                 anchor="center")
        line(c, 960, 270, 960, 720, "#E6E6E2", ab, 3)
        return
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        text_mid(c, "d  =", 560, 400, 96, "black", PURPLE, aa)
        fr(c, "m", "V", 780, 385, 96, INK, aa, num_col=GREEN, den_col=AMBER)
        text(c, "massa", 960, 360, 30, "black", GREEN, aa, align="left")
        text(c, "volume", 960, 470, 30, "black", AMBER, aa, align="left")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        cubo(c, 1340, 400, 150, COR["chumbo"], ab, "muito espremido", 24, pontos=36)
        cubo(c, 1620, 400, 150, "#F4F5F7", ab, "quase nada", 24, pontos=4)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "g/cm³ = quantos GRAMAS cabem em cada CUBINHO", W / 2, 700, acc, 38, BLUE)


# ======================================================================
# atalhos (verde): triângulo · comparar com 1 · 1 L pesa d kg
# ======================================================================

def b_atalho(c, t, C, B):
    sid = which(t, C, ["08", "14", "16"])
    titulos = {"08": ("ATALHO", "O TRIÂNGULO DA DENSIDADE"), "14": ("ATALHO", "COMPARE COM 1"),
               "16": ("ATALHO", "1 L PESA d QUILOS")}
    head(c, t, C[sid], *titulos[sid], GREEN)
    card(c, *CARD_R)
    if sid == "08":
        a0 = ep(t, C["08.a"], 0.5)
        tampa, ta, res = None, 0.0, None
        for cue, k, fo in (("08.b", "d", "d = m ÷ V"), ("08.c", "m", "m = d × V"), ("08.d", "V", "V = m ÷ d")):
            if t >= C[cue] + (1.2 if k == "d" else 0):
                tampa, ta, res = k, ep(t, C[cue] + (1.2 if k == "d" else 0), 0.5), fo
        triangulo(c, 620, 500, 280, a0, tampa, ta)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            pill(c, "tampe com o dedo o que você procura", 620, 800, GREEN, size=28, a=ab, anchor="center")
        rows = [("08.b", "tampou d", "d = m ÷ V", "a taxa: divida"), ("08.c", "tampou m", "m = d × V", "o de cima: multiplique"),
                ("08.d", "tampou V", "V = m ÷ d", "o de baixo: divida ao contrário")]
        for k, (cue, q, fo, sub) in enumerate(rows):
            ak = ep(t, C[cue] + 1.2, 0.4)
            if ak <= 0:
                continue
            y = 330 + k * 150
            on_ = res == fo
            rrect(c, 1060, y - 55, 640, 120, 20, mix("#FFFFFF", GREEN, 0.16 if on_ else 0.05), ak)
            text(c, q, 1090, y - 10, 26, "bold", GRAY, ak, align="left")
            text(c, fo, 1090, y + 40, 46, "black", GREEN if on_ else INK, ak, align="left")
            text(c, sub, 1680, y + 30, 24, "bold", PURPLE, ak, align="right")
        ae = ep(t, C["08.e"], 0.5)
        if ae > 0:
            selo(c, 1390, 790, ae, "3 PERGUNTAS, 1 DESENHO", GREEN, -3, 28)
        return
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            x0, x1, y = 300, 1620, 470
            k = (x1 - x0) / 3.0
            xa = x0 + k
            rrect(c, x0, y - 30, xa - x0, 60, 12, mix("#FFFFFF", GREEN, 0.25), aa)
            rrect(c, xa, y - 30, x1 - xa, 60, 12, mix("#FFFFFF", RED, 0.18), aa)
            for v in (0, 1, 2, 3):
                xx = x0 + v * k
                line(c, xx, y - 44, xx, y + 44, INK if v != 1 else BLUE, aa, 4 if v != 1 else 7)
                text(c, str(v), xx, y + 90, 36, "black", BLUE if v == 1 else INK2, aa)
            text(c, "ÁGUA = 1", xa, y + 140, 30, "black", BLUE, aa)
            ab = ep(t, C["14.b"], 0.5)
            text(c, "BOIA", (x0 + xa) / 2, y + 12, 34, "black", GREEN, ab)
            text(c, "AFUNDA", xa + k * 1.5, y + 12, 34, "black", RED, ab)
            for nome, d, col in MATS:
                if nome in ("água", "água do mar") or d > 3:
                    continue
                am = ab * ep(t, C["14.b"] + 0.6, 0.4)
                xx = x0 + d * k
                dy_ = {"óleo": 100, "gelo": 170}.get(nome, 100)
                line(c, xx, y - 34, xx, y - dy_ + 14, col if nome != "gelo" else AGUA_ESC, am, 3)
                c.drawCircle(xx, y - dy_, 14, paint(col, am)); c.drawCircle(xx, y - dy_, 14, paint(INK2, am, stroke=2))
                text(c, f"{nome} {dv(d)}", xx + 26, y - dy_ + 9, 26, "black", INK2, am, align="left")
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            linha(c, [("0,...", GREEN), (" → boia     ", INK), ("1,... ou mais", RED), (" → afunda", INK)],
                  W / 2, 700, 44, ab)
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        K.atalho(c, 260, 220, 1400, 130, "ATALHO", ["1 L de um material de densidade d  pesa  d kg"], aa, 40)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        for k, (d, col, s) in enumerate(((1.0, AGUA, "água: 1 L = 1 kg"), (2.0, "#C9A46A", "densidade 2: 1 L = 2 kg"))):
            x = 560 + k * 800
            balanca(c, x, 520, 380, ab, f"{dv(d) if d != 1 else '1'} kg")
            rrect(c, x - 55, 400, 110, 120, 14, col, ab)
            text(c, "1 L", x, 472, 30, "black", INK, ab)
            text(c, s, x, 712, 30, "black", INK2, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        pill(c, "menos denso que a água → pesa MENOS que a mesma quantidade de água", W / 2, 780, GREEN, size=26,
             a=acc, anchor="center")


# ======================================================================
# bloco b — impressão digital
# ======================================================================

def b_digital(c, t, C, B):
    head_seq(c, t, C, [("09", "O PORTÃO É MAIS DENSO?", "PREGO × PORTÃO", BLUE),
                       ("10", "IMPRESSÃO DIGITAL", "DO MATERIAL, NÃO DA QUANTIDADE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    aa = ep(t, C["09.a"], 0.5)
    ab = ep(t, C["09.b"], 0.5)
    if sid == "09":
        if aa > 0:
            prego(c, 330, 380, 360, aa)
            linha(c, [("3,9 g ÷ 0,5 cm³", INK)], 520, 520, 38, aa)
            linha(c, [("= ", INK), ("7,8 g/cm³", PURPLE)], 520, 590, 46, ep(t, C["09.a"] + 2.4, 0.4))
        if ab > 0:
            portao(c, 1180, 300, 420, 200, ab)
            linha(c, [("78 kg = 78 000 g", INK2)], 1390, 560, 30, ab)
            linha(c, [("78 000 g ÷ 10 000 cm³", INK)], 1390, 615, 36, ep(t, C["09.b"] + 2.2, 0.4))
            linha(c, [("= ", INK), ("7,8 g/cm³", PURPLE)], 1390, 680, 46, ep(t, C["09.b"] + 3.4, 0.4))
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            selo(c, W / 2, 470, acc, "IGUAL", GREEN, -5, 50)
        return
    prego(c, 330, 330, 260, 1)
    portao(c, 1260, 260, 300, 140, 1)
    etiqueta(c, "7,8 g/cm³", 460, 420, 1)
    etiqueta(c, "7,8 g/cm³", 1410, 450, 1)
    a1 = ep(t, C["10.a"], 0.5)
    if a1 > 0:
        linha(c, [("massa ", GREEN), ("e ", INK), ("volume", AMBER), (" crescem JUNTOS", INK)], W / 2, 560, 44, a1)
    a2 = ep(t, C["10.b"], 0.5)
    if a2 > 0:
        # impressão digital estilizada
        cx, cy = 560, 700
        for k in range(5):
            r = 18 + k * 14
            c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r * 1.2, 2 * r, 2.4 * r), 200, 220, False,
                      paint(BLUE, a2, stroke=5, cap_round=True))
        regra(c, "não depende da QUANTIDADE (como em Química)", 1150, 710, a2, 34, BLUE)


# ======================================================================
# bloco c — a tabela como ranking
# ======================================================================

def b_tabela(c, t, C, B):
    head(c, t, B["start"], "A IMPRESSÃO DIGITAL", "DE CADA MATERIAL", BLUE)
    card(c, *CARD_R)
    ta, tb = C["11.a"], C["11.b"]
    ts = [ta + 1.0, ta + 2.6, ta + 4.6, ta + 5.6, tb + 0.4, tb + 1.8, tb + 3.2, tb + 4.6]
    ranking(c, t, ts, 520, 270, ep(t, ta, 0.4))
    pill(c, "do mais LEVE ao mais PESADO", 1450, 260, BLUE, size=24, a=ep(t, ta, 0.4), anchor="center")


# ======================================================================
# bloco d — flutuação
# ======================================================================

def b_flutua(c, t, C, B):
    head_seq(c, t, C, [("12", "QUEM BOIA?", "O CRITÉRIO DA FLUTUAÇÃO", PURPLE), ("13", "TUDO NO AQUÁRIO", "BOIA OU AFUNDA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 230, 1400, 110, 20, mix("#FFFFFF", BLUE, 0.08), aa)
            linha(c, [("FLUTUAR", BLUE), (" = ficar na superfície, sem ir para o fundo", INK)], W / 2, 285, 38, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            regra(c, "flutua quem tem densidade MENOR que a do líquido", W / 2, 440, ab, 40)
            text(c, "maior que a do líquido → afunda", W / 2, 530, 32, "black", RED, ep(t, C["12.b"] + 2.6, 0.4))
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            pill(c, "NA ÁGUA, A RÉGUA É O 1", W / 2, 640, BLUE, size=34, a=acc, anchor="center")
            linha(c, [("menor que 1: ", INK), ("boia", GREEN), ("     maior que 1: ", INK), ("afunda", RED)], W / 2, 740,
                  40, ep(t, C["12.c"] + 1.4, 0.4))
        return
    a0 = ep(t, C["13"], 0.5)
    ua = ep(t, C["13.a"], 1.2)
    ub = ep(t, C["13.b"], 1.0)
    ud = [ep(t, C["13.d"] + 0.35 * k, 0.9) for k in range(4)]
    itens = [("gelo", 0.92, 0.18, ub, "gelo 0,92"),
             ("alumínio", 2.7, 0.40, ud[0], "alumínio 2,7"), ("ferro", 7.8, 0.58, ud[1], "ferro 7,8"),
             ("chumbo", 11.3, 0.76, ud[2], "chumbo 11,3"), ("ouro", 19.3, 0.92, ud[3], "ouro 19,3")]
    aquario(c, 220, 260, 1060, 520, a0, itens, oleo=ua)
    if ub > 0.9:
        # marca dos 92%
        x = 220 + 1060 * 0.18 + 60
        wy = 260 + 520 * 0.30 - 34 * ua
        line(c, x, wy - 74 * 0.08, x, wy + 74 * 0.92 - 74 * 0.08, BLUE, ep(t, C["13.b"] + 3.0, 0.4), 4)
    ab = ep(t, C["13.b"] + 3.0, 0.4)
    if ab > 0:
        rrect(c, 1320, 280, 400, 150, 20, mix("#FFFFFF", BLUE, 0.10), ab)
        text(c, "gelo: ≈ 92%", 1520, 340, 40, "black", BLUE, ab)
        text(c, "SUBMERSO (abaixo da água)", 1520, 392, 22, "black", INK2, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        # iceberg
        cx, wy = 1520, 560
        p = skia.Path(); p.moveTo(cx - 40, wy); p.lineTo(cx - 10, wy - 40); p.lineTo(cx + 25, wy - 28); p.lineTo(cx + 45, wy)
        c.drawPath(p, paint("#FFFFFF", acc)); c.drawPath(p, paint(VIDRO, acc, stroke=3))
        q = skia.Path(); q.moveTo(cx - 40, wy); q.lineTo(cx - 120, wy + 120); q.lineTo(cx - 40, wy + 200)
        q.lineTo(cx + 90, wy + 180); q.lineTo(cx + 130, wy + 70); q.lineTo(cx + 45, wy); q.close()
        c.drawPath(q, paint(mix("#FFFFFF", AGUA, 0.45), acc)); c.drawPath(q, paint(VIDRO, acc, stroke=3))
        line(c, cx - 170, wy, cx + 170, wy, AGUA_ESC, acc, 4)
        text(c, "a PONTA do iceberg", cx, wy - 70, 28, "black", BLUE, acc)
    ad = ep(t, C["13.d"] + 2.4, 0.4)
    if ad > 0:
        pill(c, "maiores que 1: AFUNDAM", 750, 815, RED, size=26, a=ad, anchor="center")


# ======================================================================
# bloco e — a água amarra tudo · bloco f — outra roupa
# ======================================================================

def b_agua(c, t, C, B):
    head(c, t, B["start"], "A ÁGUA AMARRA TUDO", "POR QUE ELA VALE 1?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        cubo(c, 400, 330, 90, AGUA, aa)
        linha(c, [("1 g", GREEN), (" de água ocupa ", INK), ("1 cm³", AMBER)], 920, 330, 46, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("1 L", AMBER), (" de água pesa ", INK), ("1 kg", GREEN)], 760, 480, 46, ab)
        linha(c, [("1 m³", AMBER), (" de água pesa ", INK), ("1 t", GREEN), ("  (1 000 kg)", GRAY)], 760, 570, 46,
              ep(t, C["15.b"] + 2.2, 0.4))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 650, 1200, 130, 26, mix("#FFFFFF", PURPLE, 0.10), acc)
        linha(c, [("1 g/cm³", PURPLE), ("  =  ", INK), ("1 000 kg/m³", PURPLE)], W / 2, 715, 60, acc)


def b_demografica(c, t, C, B):
    head(c, t, B["start"], "A MESMA RAZÃO", "COM OUTRA ROUPA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        x, y, s = 300, 260, 400
        rrect(c, x, y, s, s, 12, mix("#FFFFFF", GREEN, 0.15), aa)
        c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), paint(GREEN, aa, stroke=4))
        for i in range(6):
            for j in range(6):
                px, py = x + 40 + i * 64 + (j % 2) * 18, y + 40 + j * 64
                c.drawCircle(px, py - 10, 9, paint(INK2, aa))
                rrect(c, px - 10, py, 20, 20, 8, INK2, aa)
        text(c, "1 km²", x + s / 2, y + s + 50, 34, "black", GREEN, aa)
        linha(c, [("DENSIDADE DEMOGRÁFICA", BLUE)], 1220, 330, 44, aa)
        linha(c, [("habitantes ÷ área  =  ", INK), ("hab/km²", BLUE)], 1220, 420, 40, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        text(c, "não é massa, mas a estrutura é a mesma:", 1220, 540, 30, "bold", GRAY, ab)
        text(c, "quanto de uma coisa POR unidade de outra", 1220, 600, 34, "black", PURPLE, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        chip(c, "cai em GEOGRAFIA", 1220, 720, GREEN, acc, 36)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "DENSIDADE · MATERIAL · BOIA?", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 220, 1460, 130, 24, "#F7F7F5", aa)
        linha(c, [("bloco: ", INK), ("10 cm³", AMBER), ("  ·  ", INK), ("27 g", GREEN),
                  ("  →  d = ?  material?  boia?", INK)], W / 2, 285, 50, aa)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 560)
    if t < C["19"]:
        return
    a1 = ep(t, C["19.a"], 0.5)
    if a1 > 0:
        pill(c, "pergunta = a TAXA → divida", 560, 410, PURPLE, size=26, a=a1, anchor="center")
        linha(c, [("27 g ÷ 10 cm³ = ", INK), ("2,7 g/cm³", PURPLE)], 560, 510, 50, a1)
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        cubo(c, 1170, 480, 110, COR["alumínio"], ab)
        text(c, "ALUMÍNIO", 1280, 490, 50, "black", INK, ab, align="left")
        text(c, "2,7 g/cm³ na tabela", 1280, 540, 26, "bold", GRAY, ab, align="left")
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        linha(c, [("2,7 > 1", RED), ("  →  ", INK), ("AFUNDA", RED)], W / 2, 690, 60, acc)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Densidade é massa sobre volume.",
          "A densidade é do material, não da quantidade.",
          "Menor que a água boia; maior afunda."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("O portão de ferro é mais denso que o prego", "o portão é muito mais PESADO",
          "ele também é muito MAIOR: massa e volume crescem juntos → os dois têm 7,8 g/cm³"),
         ("Ferro com 7,8 kg/m³ (como se fosse igual a 7,8 g/cm³)", "o número é o mesmo",
          "1 m³ de ferro (mil litros) pesando 7,8 kg? × mil → 7 800 kg/m³"),
         ("Massa de 200 cm³ de óleo (0,8 g/cm³): 200 ÷ 0,8 = 250 g", "densidade é uma divisão",
          "a massa é o número de CIMA: multiplique → 0,8 × 200 = 160 g")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


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


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS3 = [("A", "alumínio, densidade 2,7 g/cm³", "54 g", RED),
         ("B", "ferro, densidade 7,8 g/cm³", "", GREEN),
         ("C", "chumbo, densidade 11,3 g/cm³", "226 g", RED),
         ("D", "ouro, densidade 19,3 g/cm³", "386 g", RED),
         ("E", "gelo, densidade 0,92 g/cm³", "< 20 g", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "IDENTIFICAR O MATERIAL", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Um objeto maciço tem massa de 156 gramas e ocupa um volume de 20 cm³. Consultando uma tabela "
                           "de densidades, conclui-se que esse objeto é provavelmente de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS3, 990, 250, 720, 26, C["25.ok"], "B", cues_in, cues_x, gap=40)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 140)
    if t >= C["25"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        pill(c, "MACIÇO = sem buraco, sem ar dentro", 540, y0 + 40, BLUE, size=22, a=ep(t, C["25"], 0.4), anchor="center")
        linha(c, [("156 g ÷ 20 cm³ = ", INK), ("7,8 g/cm³", PURPLE)], 540, y0 + 105, 34, ep(t, C["25.a"], 0.4))
        linha(c, [("na tabela: ", INK2), ("FERRO", GREEN)], 540, y0 + 170, 34, ep(t, C["25.b"], 0.4))
        linha(c, [("312 g ÷ 40 cm³ = ", INK2), ("7,8 g/cm³", PURPLE)], 540, y0 + 235, 30, ep(t, C["25.c"], 0.4))
        conferido(c, "dobrou tudo, densidade igual", 230, y0 + 300, ep(t, C["25.c"] + 3.0, 0.4), True, 24)
    a26 = ep(t, C["26"], 0.4)
    if a26 > 0:
        pill(c, "20 cm³ de cada um pesariam:", 1690, 222, AMBER, size=20, a=a26, anchor="right")


ALTS4 = [("A", "0,46 g", "errou a vírgula", RED), ("B", "46 g", "errou a vírgula", RED), ("C", "460 g", "", GREEN),
         ("D", "500 g", "densidade da água", RED), ("E", "543 g", "dividiu 500 ÷ 0,92", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · NÓS FAZEMOS", "A MASSA PELA DENSIDADE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("Um bloco de gelo tem volume de 500 cm³. Sabendo que a densidade do gelo é 0,92 g/cm³, a massa "
                           "desse bloco é de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
         align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 250, 680, 44, C["28.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 140)
    if t >= C["28"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["28"], 0.4))
        pill(c, "pergunta = a MASSA (o de cima) → ×", 540, y0 + 40, PURPLE, size=22, a=ep(t, C["28"], 0.4), anchor="center")
        linha(c, [("m = 0,92 g/cm³ × 500 cm³ = ", INK), ("460 g", GREEN)], 540, y0 + 105, 30, ep(t, C["28.a"], 0.4))
        linha(c, [("500 cm³ de ÁGUA = ", INK2), ("500 g", BLUE)], 540, y0 + 175, 30, ep(t, C["28.b"], 0.4))
        linha(c, [("gelo é menos denso → ", INK2), ("menos de 500 g", GREEN)], 540, y0 + 240, 28, ep(t, C["28.c"], 0.4))
        conferido(c, "460 g < 500 g: faz sentido", 230, y0 + 305, ep(t, C["28.c"] + 2.4, 0.4), True, 24)
    ae = ep(t, C["29.xe"] + 2.0, 0.4)
    if ae > 0 and t < C["29.xa"] + 0.5:
        selo(c, 1340, 800, ae, "543 > 500: A CONFERÊNCIA DENUNCIA", AMBER, -2, 24)


# ======================================================================
# você faz
# ======================================================================

def b_vocefaz(c, t, C, B):
    head_seq(c, t, C, [("30", "VOCÊ FAZ", "PAUSE E RESOLVA", GREEN), ("31", "CONFERINDO", "1 L DE ÓLEO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 220, 1460, 130, 24, "#F7F7F5", aa)
        linha(c, [("1 L", AMBER), (" de óleo  ·  ", INK), ("0,8 g/cm³", PURPLE), ("  →  massa = ?", INK)], W / 2, 285, 54, aa)
    pause_timer(c, t, C["30.end"] - 1.9, W / 2, 560)
    if t < C["31"]:
        return
    a1 = ep(t, C["31.a"], 0.5)
    if a1 > 0:
        linha(c, [("1 L = ", INK), ("1 000 cm³", AMBER)], 560, 430, 50, a1)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        linha(c, [("0,8 g/cm³ × 1 000 cm³ = ", INK), ("800 g", GREEN)], 560, 540, 44, ab)
    acc = ep(t, C["31.c"], 0.5)
    if acc > 0:
        K.atalho(c, 1040, 390, 680, 210, "ATALHO", ["1 L de d = 0,8 → 0,8 kg", "menos que 1 kg de água ✓"], acc, 32)
        conferido(c, "bateu", 1240, 690, ep(t, C["31.c"] + 3.0, 0.4), True, 34)


# ======================================================================
# ponte e CTA
# ======================================================================

def torneira(c, x, y, s, a, col=BLUE):
    if a <= 0:
        return
    rrect(c, x, y, s * 1.2, s * 0.32, s * 0.1, "#8E949C", a)
    rrect(c, x + s * 0.95, y, s * 0.3, s * 0.6, s * 0.1, "#8E949C", a)
    rrect(c, x + s * 0.2, y - s * 0.22, s * 0.5, s * 0.16, s * 0.08, col, a)
    for k in range(3):
        c.drawCircle(x + s * 1.1, y + s * 0.75 + k * s * 0.22, s * 0.05, paint(AGUA_ESC, a))


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "VAZÃO", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    if aa > 0:
        torneira(c, 380, 330, 160, aa)
        text(c, "6 h", 480, 560, 56, "black", INK, aa)
        torneira(c, 760, 330, 160, ep(t, C["33.a"] + 1.6, 0.4), GREEN)
        text(c, "3 h", 860, 560, 56, "black", INK, ep(t, C["33.a"] + 1.6, 0.4))
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        text(c, "JUNTAS:", 1420, 330, 40, "black", INK2, ab)
        x9 = ep(t, C["33.c"], 0.4)
        for k, s in enumerate(("9 h?", "4,5 h?")):
            ak = ep(t, C["33.b"] + 1.4 * k, 0.4)
            y = 450 + k * 120
            text_mid(c, s, 1420, y, 72, "black", AMBER, ak)
            w = text_w(s, "black", 72)
            strike(c, 1420 - w / 2 - 10, y, 1420 + w / 2 + 10, y, x9, RED, x9)
    if ep(t, C["33.c"], 0.4) > 0:
        selo(c, 1420, 700, ep(t, C["33.c"], 0.4), "NENHUMA DAS DUAS", RED, -4, 30)
    pill(c, "ep. 5 · vazão e o método das frações do tanque", W / 2, 790, PURPLE, size=30, a=ep(t, C["33.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"],
        "Você sabia que o gelo fica 92% embaixo da água?", canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              atalho=b_atalho, digital=b_digital, tabela=b_tabela, flutua=b_flutua, agua=b_agua,
              demografica=b_demografica, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q3=b_q3, q4=b_q4,
              vocefaz=b_vocefaz, ponte=b_ponte, cta=b_cta)
