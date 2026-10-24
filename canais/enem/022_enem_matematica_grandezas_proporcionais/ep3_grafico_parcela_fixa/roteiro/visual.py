"""Visual — Grandezas Proporcionais, Episódio 3: o gráfico de cada relação e a armadilha da parcela fixa (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: Graf (eixos + curvas desenhadas em tempo real), taxímetro, táxi, saco de arroz, barras fixo + variável.
Gráficos exatos: arroz y = 5x · viagem x·y = 240 · táxi y = 2,5x + 6.
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
_s = importlib.util.spec_from_file_location("comum022", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_grandezas_ep3_grafico_parcela_fixa.mp4"
CARD_R = K.CARD_R
TAXI = "#F2B705"
ARROZ = "#3BAF6A"
FIXO = AMBER        # a parcela fixa (bandeirada)
VARIA = PURPLE      # a parte que varia (por km)


# ======================================================================
# peças do episódio
# ======================================================================

class Graf:
    """eixos com origem em (x0, y0) (canto inferior esquerdo, em pixels); xmax/ymax = valores no fim dos eixos"""

    def __init__(s, x0, y0, w, h, xmax, ymax):
        s.x0, s.y0, s.w, s.h, s.xmax, s.ymax = x0, y0, w, h, xmax, ymax

    def X(s, v):
        return s.x0 + v / s.xmax * s.w

    def Y(s, v):
        return s.y0 - v / s.ymax * s.h

    def eixos(s, c, a, xl="", yl="", tx=(), ty=(), size=22, col_x=None, col_y=None):
        if a <= 0:
            return
        arrow(c, s.x0, s.y0, s.x0 + s.w + 34, s.y0, col_x or INK, a, 4, 14)
        arrow(c, s.x0, s.y0, s.x0, s.y0 - s.h - 34, col_y or INK, a, 4, 14)
        for v, lab in tx:
            line(c, s.X(v), s.y0 - 8, s.X(v), s.y0 + 8, INK, a, 3)
            text(c, lab, s.X(v), s.y0 + 38, size, "bold", INK2, a)
        for v, lab in ty:
            line(c, s.x0 - 8, s.Y(v), s.x0 + 8, s.Y(v), INK, a, 3)
            text_mid(c, lab, s.x0 - 16, s.Y(v), size, "bold", INK2, a, align="right")
        if xl:
            text(c, xl, s.x0 + s.w + 34, s.y0 + 72, size, "black", INK2, a, align="right")
        if yl:
            text(c, yl, s.x0 + 18, s.y0 - s.h - 44, size, "black", INK2, a, align="left")

    def curva(s, c, f, v0, v1, col, a, prog=1.0, width=7, n=200, dash=None):
        if a <= 0 or prog <= 0:
            return
        p = skia.Path()
        started = False
        vend = v0 + (v1 - v0) * min(1.0, prog)
        for i in range(n + 1):
            v = v0 + (vend - v0) * i / n
            y = f(v)
            if y > s.ymax * 1.001 or y < -1e-9:
                continue
            if not started:
                p.moveTo(s.X(v), s.Y(y)); started = True
            else:
                p.lineTo(s.X(v), s.Y(y))
        pa = paint(col, a, stroke=width, cap_round=True)
        if dash:
            pa.setPathEffect(skia.DashPathEffect.Make(dash, 0))
        c.drawPath(p, pa)

    def ponto(s, c, xv, yv, col, a, r=11, guias=False):
        if a <= 0:
            return
        if guias:
            line(c, s.X(xv), s.y0, s.X(xv), s.Y(yv), col, a * 0.6, 3, dash=[10, 8])
            line(c, s.x0, s.Y(yv), s.X(xv), s.Y(yv), col, a * 0.6, 3, dash=[10, 8])
        c.drawCircle(s.X(xv), s.Y(yv), r * (0.6 + 0.4 * a), paint(col, a))
        c.drawCircle(s.X(xv), s.Y(yv), r * 0.45, paint("#FFFFFF", a))


def taximetro(c, x, y, valor, a, sub=""):
    """visor do taxímetro; (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    rrect(c, x, y, 250, 96, 16, "#1E2530", a, shadow=True)
    rrect(c, x + 10, y + 10, 230, 76, 10, "#0E1218", a)
    text_mid(c, valor, x + 125, y + 48, 44, "black", "#3DE38A", a)
    if sub:
        text(c, sub, x + 125, y + 130, 22, "black", INK2, a)


def taxi(c, cx, cy, a, s=1.0):
    """carrinho de táxi visto de lado; (cx, cy) = centro da carroceria"""
    if a <= 0:
        return
    rrect(c, cx - 150 * s, cy - 20 * s, 300 * s, 70 * s, 22 * s, TAXI, a, shadow=True)
    p = skia.Path()
    p.moveTo(cx - 90 * s, cy - 20 * s); p.lineTo(cx - 60 * s, cy - 70 * s); p.lineTo(cx + 60 * s, cy - 70 * s)
    p.lineTo(cx + 95 * s, cy - 20 * s); p.close()
    c.drawPath(p, paint(TAXI, a))
    for dx in (-52, 12):
        q = skia.Path(); x0 = cx + dx * s
        q.moveTo(x0, cy - 26 * s); q.lineTo(x0 + 8 * s, cy - 60 * s); q.lineTo(x0 + 48 * s, cy - 60 * s); q.lineTo(x0 + 56 * s, cy - 26 * s)
        q.close(); c.drawPath(q, paint("#DCEFFB", a))
    rrect(c, cx - 36 * s, cy - 100 * s, 72 * s, 30 * s, 8 * s, INK, a)
    text_mid(c, "TÁXI", cx, cy - 85 * s, 18 * s, "black", TAXI, a)
    for dx in (-90, 90):
        c.drawCircle(cx + dx * s, cy + 50 * s, 30 * s, paint(INK, a))
        c.drawCircle(cx + dx * s, cy + 50 * s, 12 * s, paint("#C9C9C4", a))


def saco_arroz(c, cx, cy, a, s=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 80 * s, cy - 90 * s); p.lineTo(cx + 80 * s, cy - 90 * s); p.lineTo(cx + 95 * s, cy + 90 * s)
    p.lineTo(cx - 95 * s, cy + 90 * s); p.close()
    c.drawPath(p, paint("#FFFFFF", a)); c.drawPath(p, paint("#D4D4CF", a, stroke=5))
    rrect(c, cx - 70 * s, cy - 40 * s, 140 * s, 70 * s, 12 * s, ARROZ, a)
    text_mid(c, "ARROZ", cx, cy - 18 * s, 26 * s, "black", "#FFFFFF", a)
    text_mid(c, "1 kg", cx, cy + 14 * s, 22 * s, "black", "#FFFFFF", a)
    for k in range(5):
        c.drawOval(skia.Rect.MakeXYWH(cx - 60 * s + k * 26 * s, cy + 52 * s, 14 * s, 8 * s), paint("#EDE6D2", a))


def barra(c, x, y, partes, a, esc=20, h=86, prog=1.0):
    """barra horizontal de blocos [(valor, cor, rótulo)]; esc = pixels por real. Devolve o x final."""
    xx = x
    for k, (v, col, lab) in enumerate(partes):
        ak = a * clamp(prog * len(partes) - k, 0, 1)
        if ak <= 0:
            break
        w = v * esc
        rrect(c, xx, y, w - 6, h, 14, col, ak)
        text_mid(c, lab, xx + (w - 6) / 2, y + h / 2, 30 if w > 160 else 26, "black", "#FFFFFF", ak)
        xx += w
    return xx


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ---------- ícones do dia a dia ----------

def ic_luz(c, cx, cy, a):
    c.drawCircle(cx, cy - 12, 34, paint(AMBER, a))
    rrect(c, cx - 18, cy + 18, 36, 30, 6, INK2, a)
    line(c, cx - 14, cy + 30, cx + 14, cy + 30, "#FFFFFF", a, 3)


def ic_celular(c, cx, cy, a):
    rrect(c, cx - 30, cy - 52, 60, 104, 12, INK, a)
    rrect(c, cx - 23, cy - 42, 46, 76, 6, "#DCEFFB", a)
    c.drawCircle(cx, cy + 43, 5, paint("#FFFFFF", a))


def ic_caixa(c, cx, cy, a):
    rrect(c, cx - 48, cy - 36, 96, 76, 8, "#C9955B", a)
    line(c, cx, cy - 36, cx, cy + 40, "#A0713F", a, 6)
    line(c, cx - 48, cy - 10, cx + 48, cy - 10, "#A0713F", a, 4)


def ic_salario(c, cx, cy, a):
    rrect(c, cx - 56, cy - 32, 112, 64, 8, GREEN, a)
    c.drawCircle(cx, cy, 18, paint("#FFFFFF", a * 0.85))
    text_mid(c, "$", cx, cy, 24, "black", GREEN, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A ARMADILHA DO TÁXI", AMBER)
    card(c, *CARD_R)
    a0 = ep(t, C["01.a"], 0.5)
    taxi(c, 520, 400, a0, 1.25)
    if a0 > 0:
        ftext(c, "8 km  →  R$ 26", 520, 620, 52, "black", INK, a0)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        ftext(c, "16 km  →  ?", 520, 720, 52, "black", BLUE, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        ftext(c, "R$ 52?", 1340, 460, 150, "black", RED, acc)
    ad = ep(t, C["01.d"], 0.5)
    check_icon(c, 1640, 360, 40, ad, RED, "x")
    selo(c, 1340, 640, ad, "A ARMADILHA MAIS COBRADA", AMBER, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "reconhecer a relação pelo DESENHO", "reta pela origem, hipérbole ou nenhuma das duas"),
            ("02.b", "nunca mais cair na parcela fixa", "a bandeirada do táxi não dobra")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 340 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    head_seq(c, t, C, [("03", "DOIS LEMBRETES", "O k DO EPISÓDIO 1", GREEN), ("04", "COMO LER UM GRÁFICO", "EIXOS E ORIGEM", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["03", "04"])
    if sid == "03":
        for k, (cue, nome, e, sub, col) in enumerate((("03.a", "DIRETA", "y/x = k", "a DIVISÃO não muda", BLUE),
                                                      ("03.b", "INVERSA", "x · y = k", "a MULTIPLICAÇÃO não muda", PURPLE))):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            x = 560 + k * 800
            card(c, x - 330, 250 + d, 660, 480, a)
            text(c, nome, x, 330 + d, 40, "black", col, a)
            expr(c, e, x, 490 + d, 110, a, cores={0: col})
            text(c, sub, x, 660 + d, 34, "black", INK2, a)
        return
    g = Graf(360, 760, 760, 480, 5, 25)
    aa = ep(t, C["04.a"], 0.5)
    ab, acc = ep(t, C["04.b"], 0.5), ep(t, C["04.c"], 0.5)
    g.eixos(c, ab, tx=[(k, str(k)) for k in range(1, 5)], ty=[(v, str(v)) for v in (5, 10, 15, 20)],
            col_x=mix(INK, BLUE, ab), col_y=mix(INK, BLUE, acc))
    if ab > 0:
        text(c, "eixo HORIZONTAL (deitado)", g.x0 + g.w / 2, g.y0 + 78, 26, "black", BLUE, ab)
    if acc > 0:
        c.save(); c.translate(g.x0 - 70, g.y0 - g.h / 2); c.rotate(-90)
        text(c, "eixo VERTICAL (em pé)", 0, 0, 26, "black", BLUE, acc)
        c.restore()
    ad = ep(t, C["04.d"], 0.5)
    g.ponto(c, 3, 15, PURPLE, ad, guias=True)
    if ad > 0:
        ftext(c, "(3; 15)", g.X(3) + 24, g.Y(15) - 18, 30, "black", PURPLE, ad, align="left")
        arrow(c, g.x0 + 10, g.y0 - 20, g.X(3) - 14, g.y0 - 20, GREEN, ad, 4, 12, progress=ep(t, C["04.d"] + 0.3, 0.6))
        arrow(c, g.X(3) + 20, g.y0 - 10, g.X(3) + 20, g.Y(15) + 20, GREEN, ad, 4, 12, progress=ep(t, C["04.d"] + 0.9, 0.6))
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        c.drawCircle(g.x0, g.y0, 26, paint(AMBER, ae, stroke=6))
        text(c, "ORIGEM", g.x0 - 34, g.y0 + 6, 28, "black", AMBER, ae, align="right")
        text(c, "(0; 0)", g.x0 - 34, g.y0 + 40, 24, "black", AMBER, ae, align="right")
    if aa > 0:
        boxed(c, 1250, 260, 470, 200, BLUE, aa, 0.08)
        text(c, "GRÁFICO", 1485, 320, 34, "black", BLUE, aa)
        para(c, "desenho de como uma grandeza muda com a outra", 1280, 370, 28, "bold", INK2, aa, 410, 36)
    if ad > 0:
        boxed(c, 1250, 500, 470, 160, PURPLE, ad, 0.08)
        para(c, "cada PONTO é um par: ande na horizontal e suba", 1280, 555, 28, "black", INK, ad, 410, 36)


# ======================================================================
# o concreto: arroz × táxi
# ======================================================================

def b_compras(c, t, C, B):
    head_seq(c, t, C, [("05", "DUAS COMPRAS", "LADO A LADO", BLUE), ("06", "PARECEM IGUAIS", "MAS SÓ UM É PROPORCIONAL", AMBER)])
    sid = which(t, C, ["05", "06"])
    aa, ab = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5)
    if aa > 0:
        card(c, 190, 200, 700, 440, aa)
        saco_arroz(c, 540, 360, aa)
        text(c, "R$ 5,00 o quilo", 540, 530, 40, "black", ARROZ, aa)
    if ab > 0:
        card(c, 1030, 200, 700, 440, ab)
        taxi(c, 1230, 400, ab, 0.85)
        taximetro(c, 1420, 270, "R$ 6,00", ab)
        ftext(c, "+ R$ 2,50 por km", 1545, 462, 34, "black", VARIA, ab)
        text(c, "bandeirada", 1545, 394, 22, "black", FIXO, ab)
        text(c, "táxi", 1230, 530, 40, "black", INK, ab)
    if sid == "05":
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            chip(c, "BANDEIRADA = o que o taxímetro já marca ao entrar", W / 2, 700, BLUE, acc, 30)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            boxed(c, 460, 750, 1000, 80, FIXO, ad, 0.12)
            text_mid(c, "PARCELA FIXA: cobrada uma vez só", W / 2, 790, 36, "black", INK, ad)
        return
    for cue, x, s in (("06.a", 540, "mais kg → mais caro"), ("06.b", 1380, "mais km → mais caro")):
        a = ep(t, C[cue], 0.5)
        if a > 0:
            ftext(c, s, x, 600, 32, "bold", INK2, a)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        boxed(c, 560, 690, 800, 90, AMBER, acc, 0.12)
        text_mid(c, "só UM é proporcional. Qual?", W / 2, 735, 40, "black", INK, acc)
    pill(c, "o GRÁFICO conta", W / 2, 818, PURPLE, size=28, a=ep(t, C["06.d"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco A — direta: reta pela origem (arroz)
# ======================================================================

def _g_arroz():
    return Graf(330, 770, 760, 520, 4.4, 24)


def b_arroz(c, t, C, B):
    head_seq(c, t, C, [("07", "O ARROZ", "DIRETA: COMO É O DESENHO?", BLUE), ("08", "A INCLINAÇÃO", "A SUBIDA É O k", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    g = _g_arroz()
    g.eixos(c, ep(t, C["07"], 0.5), "kg", "R$", tx=[(k, str(k)) for k in range(1, 5)], ty=[(v, str(v)) for v in (5, 10, 15, 20)])
    pts = [("07.a", 0), ("07.b", 1), ("07.c", 2), ("07.d", 3)]
    g.curva(c, lambda x: 5 * x, 0, 4.4, ARROZ, ep(t, C["07.e"], 0.4), ep(t, C["07.e"], 1.4))
    for cue, k in pts:
        g.ponto(c, k, 5 * k, ARROZ, ep(t, C[cue], 0.4), guias=sid == "07" and t < C["07.e"])
    if sid == "07":
        for j, (cue, k) in enumerate(pts):
            a = ep(t, C[cue], 0.4)
            if a > 0:
                ftext(c, f"{k} kg  →  R$ {5 * k}", 1460, 290 + j * 80, 40, "black", ARROZ if k else INK, a)
        af = ep(t, C["07.f"], 0.5)
        if af > 0:
            c.drawCircle(g.x0, g.y0, 28, paint(AMBER, af, stroke=6))
            boxed(c, 1220, 620, 480, 130, BLUE, af, 0.08)
            text(c, "DIRETA", 1460, 672, 34, "black", BLUE, af)
            text(c, "reta que NASCE na origem", 1460, 718, 28, "black", INK2, af)
        return
    aa = ep(t, C["08.a"], 0.5)
    for k in range(4):
        ak = aa * ep(t, C["08.a"] + 0.25 * k, 0.4)
        if ak <= 0:
            continue
        line(c, g.X(k), g.Y(5 * k), g.X(k + 1), g.Y(5 * k), GREEN, ak, 4, dash=[10, 8])
        line(c, g.X(k + 1), g.Y(5 * k), g.X(k + 1), g.Y(5 * k + 5), GREEN, ak, 6)
        text_mid(c, "+5", g.X(k + 1) + 16, g.Y(5 * k + 2.5), 26, "black", GREEN, ak, align="left")
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        boxed(c, 1220, 220, 500, 140, BLUE, ab, 0.08)
        text(c, "INCLINAÇÃO", 1470, 275, 34, "black", BLUE, ab)
        text(c, "o quanto a reta é íngreme", 1470, 322, 28, "bold", INK2, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        ftext(c, "inclinação = k = R$ 5/kg", 1470, 430, 36, "black", PURPLE, acc)
        K.atalho(c, 1220, 470, 500, 170, "ATALHO", ["o k é quanto a reta", "sobe a cada passo de 1"], acc, 30)
    ad = ep(t, C["08.d"], 0.5)
    g.curva(c, lambda x: 8 * x, 0, 3, AMBER, ad, ad, 6, dash=[16, 10])
    if ad > 0:
        ftext(c, "R$ 8/kg: mais em pé", g.X(2.15) - 20, g.Y(22.5), 28, "black", AMBER, ad, align="right")
        text(c, "as duas nascem na ORIGEM", 1470, 720, 30, "black", INK, ad)


# ======================================================================
# bloco B — inversa: hipérbole (viagem de 240 km)
# ======================================================================

def _g_viagem():
    return Graf(330, 770, 820, 520, 260, 9)


VIAGEM = [("09.a", 40, 6), ("09.b", 60, 4), ("09.c", 80, 3), ("09.d", 120, 2)]


def b_viagem(c, t, C, B):
    head_seq(c, t, C, [("09", "A VIAGEM DE 240 km", "INVERSA: COMO É O DESENHO?", PURPLE), ("10", "AS PONTAS DA CURVA", "ASSÍNTOTAS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    g = _g_viagem()
    g.eixos(c, ep(t, C["09"], 0.5), "km/h", "horas", tx=[(v, str(v)) for v in (40, 80, 120, 160, 200, 240)],
            ty=[(v, str(v)) for v in (2, 4, 6, 8)])
    af = ep(t, C["09.f"], 0.4)
    g.curva(c, lambda x: 240 / x, 240 / 9, 260, PURPLE, af, ep(t, C["09.f"], 1.6))
    for cue, v, h in VIAGEM:
        g.ponto(c, v, h, PURPLE, ep(t, C[cue], 0.4), guias=sid == "09" and t < C["09.f"])
    if sid == "09":
        for j, (cue, v, h) in enumerate(VIAGEM):
            a = ep(t, C[cue], 0.4)
            if a > 0:
                ftext(c, f"{v} × {h} = 240", 1490, 270 + j * 70, 36, "black", INK, a)
        ae = ep(t, C["09.e"], 0.5)
        if ae > 0:
            boxed(c, 1260, 560, 460, 90, PURPLE, ae, 0.08)
            ftext(c, "velocidade × tempo = 240", 1490, 616, 30, "black", PURPLE, ae)
        ag = ep(t, C["09.g"], 0.5)
        if ag > 0:
            boxed(c, 1260, 680, 460, 120, BLUE, ag, 0.08)
            text(c, "HIPÉRBOLE", 1490, 730, 34, "black", BLUE, ag)
            text(c, "curva que desce e vai deitando", 1490, 772, 24, "bold", INK2, ag)
        return
    aa, ab = ep(t, C["10.a"], 0.5), ep(t, C["10.b"], 0.5)
    if aa > 0:
        arrow(c, g.X(170), g.Y(2.4), g.X(250), g.Y(1.5), GREEN, aa, 5, 16, progress=ep(t, C["10.a"], 0.8))
    if ab > 0:
        line(c, g.X(150), g.y0 - 4, g.X(258), g.y0 - 4, RED, ab, 6)
        boxed(c, 1260, 690, 460, 110, RED, ab, 0.08)
        text(c, "nunca encosta:", 1490, 736, 28, "black", RED, ab)
        text(c, "o tempo nunca chega a 0", 1490, 778, 28, "black", RED, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        arrow(c, g.X(48), g.Y(4.2), g.X(30), g.Y(7.8), GREEN, acc, 5, 16, progress=ep(t, C["10.c"], 0.8))
        line(c, g.x0 + 4, g.Y(5), g.x0 + 4, g.Y(9), RED, acc, 6)
        text(c, "sem tocar", g.X(60), g.Y(8.2), 26, "black", RED, acc, align="left")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        boxed(c, 1260, 260, 460, 210, BLUE, ad, 0.08)
        text(c, "ASSÍNTOTA", 1490, 320, 36, "black", BLUE, ad)
        para(c, "a linha da qual a curva chega cada vez mais perto, sem nunca tocar", 1290, 365, 26, "bold", INK2, ad, 400, 32)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        boxed(c, 1260, 520, 460, 120, PURPLE, ae, 0.08)
        text(c, "na hipérbole, os", 1490, 570, 30, "black", INK, ae)
        text(c, "DOIS EIXOS são assíntotas", 1490, 612, 30, "black", PURPLE, ae)


# ======================================================================
# bloco C — o táxi: reta que não nasce na origem
# ======================================================================

def _g_taxi():
    return Graf(330, 770, 800, 520, 17, 50)


TAXI_PTS = [("11.a", 0, 6, "R$ 6,00"), ("11.b", 4, 16, "R$ 16,00"), ("11.c", 8, 26, "R$ 26,00")]


def b_taxi(c, t, C, B):
    head_seq(c, t, C, [("11", "E O TÁXI?", "A RETA QUE NASCE DEVENDO", AMBER), ("12", "NEM DIRETA, NEM INVERSA", "NÃO É PROPORÇÃO", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    g = _g_taxi()
    g.eixos(c, ep(t, C["11"], 0.5), "km", "R$", tx=[(v, str(v)) for v in (4, 8, 12, 16)], ty=[(v, str(v)) for v in (10, 20, 30, 40)])
    g.curva(c, lambda x: 2.5 * x + 6, 0, 16.8, TAXI, ep(t, C["11.d"], 0.4), ep(t, C["11.d"], 1.4))
    for cue, x, y, _ in TAXI_PTS:
        g.ponto(c, x, y, mix(TAXI, INK, 0.25), ep(t, C[cue], 0.4), guias=sid == "11" and t < C["11.d"] and x > 0)
    cur = None
    for cue, x, y, s in TAXI_PTS:
        if t >= C[cue]:
            cur = (x, s)
    if cur:
        taximetro(c, 1340, 250, cur[1], ep(t, C["11.a"], 0.5), f"km {cur[0]}")
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        c.drawCircle(g.x0, g.Y(6), 26, paint(FIXO, ae, stroke=6))
        c.drawCircle(g.x0, g.y0, 22, paint(RED, ae, stroke=5))
        ftext(c, "✗ origem", g.x0 - 34, g.y0 + 10, 24, "black", RED, ae, align="right")
        text_mid(c, "nasce no 6", g.x0 - 40, g.Y(6) - 4, 26, "black", FIXO, ae, align="right")
    if sid == "11":
        af = ep(t, C["11.f"], 0.5)
        if af > 0:
            boxed(c, 1240, 500, 500, 150, FIXO, af, 0.12)
            text(c, "já começa DEVENDO", 1490, 560, 34, "black", INK, af)
            text(c, "a bandeirada", 1490, 605, 34, "black", FIXO, af)
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        chip(c, "nem direta, nem inversa", 1490, 470, RED, aa, 30)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        boxed(c, 1240, 530, 500, 110, BLUE, ab, 0.08)
        text(c, "FUNÇÃO AFIM", 1490, 578, 32, "black", BLUE, ab)
        text(c, "assunto de uma série própria", 1490, 618, 24, "bold", INK2, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        boxed(c, 1240, 680, 500, 120, RED, acc, 0.08)
        text(c, "reta que NÃO passa pela", 1490, 730, 30, "black", RED, acc)
        text(c, "origem: não é proporcional", 1490, 772, 30, "black", RED, acc)


# ======================================================================
# bloco D — o teste de dois segundos
# ======================================================================

def b_teste(c, t, C, B):
    frame(c, t, B["start"], "O TESTE DE DOIS SEGUNDOS", "OLHE O EIXO EM PÉ", GREEN)
    g = Graf(330, 770, 760, 520, 10, 50)
    a0 = ep(t, C["13"], 0.5)
    g.eixos(c, a0, tx=[(v, str(v)) for v in (2, 4, 6, 8)], ty=[(v, str(v)) for v in (10, 20, 30, 40)])
    g.curva(c, lambda x: 4 * x, 0, 10, ARROZ, a0, ep(t, C["13"], 1.2))
    g.curva(c, lambda x: 3 * x + 15, 0, 10, TAXI, a0, ep(t, C["13"] + 0.4, 1.2))
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        line(c, g.x0, g.y0 + 10, g.x0, g.y0 - g.h - 10, BLUE, aa * 0.5, 14)
        arrow(c, g.x0 + 190, g.Y(30), g.x0 + 20, g.Y(30), BLUE, aa, 6, 18, progress=aa)
        text(c, "o dedo aqui", g.x0 + 200, g.Y(30) + 10, 28, "black", BLUE, aa, align="left")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        c.drawCircle(g.x0, g.y0, 24, paint(GREEN, ab, stroke=6))
        boxed(c, 1200, 230, 520, 120, GREEN, ab, 0.08)
        text(c, "corta no ZERO (origem)", 1460, 282, 30, "black", GREEN, ab)
        text(c, "pode ser direta", 1460, 324, 28, "bold", INK2, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        c.drawCircle(g.x0, g.Y(15), 24, paint(RED, acc, stroke=6))
        boxed(c, 1200, 380, 520, 150, RED, acc, 0.08)
        text(c, "corta ACIMA do zero", 1460, 432, 30, "black", RED, acc)
        text(c, "parcela fixa:", 1460, 474, 28, "bold", INK2, acc)
        text(c, "NÃO é proporcional", 1460, 512, 28, "black", INK, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1200, 570, 520, 220, "ATALHO", ["antes de qualquer conta,", "ponha o DEDO", "no eixo em pé"], ad, 30)


# ======================================================================
# bloco E — o táxi em números (bandeirada fixa × parte que varia)
# ======================================================================

def b_contas(c, t, C, B):
    head_seq(c, t, C, [("14", "DE VOLTA AO COMEÇO", "8 km × 16 km", AMBER), ("15", "POR QUÊ?", "SÓ A PARTE QUE VARIA DOBRA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    x0 = 470
    aa = ep(t, C["14.a"], 0.4)
    if aa > 0:
        text_mid(c, "8 km", 410, 300, 38, "black", INK, aa, align="right")
        xe = barra(c, x0, 257, [(6, FIXO, "6"), (20, VARIA, "2,50 × 8 = 20")], aa, prog=ep(t, C["14.a"], 1.6))
        ftext(c, "= R$ 26", xe + 20, 312, 40, "black", INK, ep(t, C["14.a"] + 2.0, 0.4), align="left")
    ab = ep(t, C["14.b"], 0.4)
    if ab > 0:
        text_mid(c, "16 km", 410, 450, 38, "black", INK, ab, align="right")
        xe = barra(c, x0, 407, [(6, FIXO, "6"), (40, VARIA, "2,50 × 16 = 40")], ab, prog=ep(t, C["14.b"], 1.6))
        ftext(c, "= R$ 46", xe + 20, 462, 40, "black", GREEN, ep(t, C["14.b"] + 2.0, 0.4), align="left")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        text_mid(c, "dobrar tudo", 410, 600, 32, "black", RED, acc, align="right")
        xe = barra(c, x0, 557, [(6, FIXO, "6"), (20, VARIA, "20"), (6, FIXO, "6"), (20, VARIA, "20")], acc * 0.75)
        strike(c, x0 - 10, 600, xe + 10, 600, ep(t, C["14.c"] + 0.4, 0.5), RED)
        ftext(c, "R$ 52 ✗", xe + 20, 612, 40, "black", RED, acc, align="left")
    if sid == "14":
        return
    a1 = ep(t, C["15.a"], 0.5)
    if a1 > 0:
        rrect(c, x0 + 6 * 20 - 8, 395, 40 * 20 + 10, 110, 18, VARIA, 0.15 * a1)
        text(c, "só a parte POR km dobrou: 20 → 40", x0 + 6 * 20 + 400, 545, 28, "black", VARIA, a1)
    a2 = ep(t, C["15.b"], 0.5)
    if a2 > 0:
        for y in (250, 400):
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 8, y, 6 * 20 + 6, 100), 18, 18), paint(FIXO, a2, stroke=5))
        text(c, "continua 6", x0 + 56, 238, 26, "black", FIXO, a2)
    a3 = ep(t, C["15.c"], 0.5)
    if a3 > 0:
        pill(c, "bandeirada cobrada DUAS vezes", 1700, 680, RED, size=26, a=a3, anchor="right", bounds=(0, 1920))
    a4 = ep(t, C["15.d"], 0.5)
    if a4 > 0:
        K.atalho(c, 230, 660, 900, 160, "ATALHO", ["separe o FIXO do que VARIA:", "só a parte que varia acompanha"], a4, 30)


# ======================================================================
# bloco F — a mesma estrutura no dia a dia
# ======================================================================

DIADIA = [("16.a", ic_luz, "luz e água", "taxa mínima", "+ consumo"),
          ("16.b", ic_celular, "celular", "franquia", "+ o que passar"),
          ("16.c", ic_caixa, "frete", "despacho", "+ preço por kg"),
          ("16.d", ic_salario, "salário", "parte fixa", "+ comissão")]


def b_diadia(c, t, C, B):
    frame(c, t, B["start"], "EM TODO LUGAR", "UM FIXO + UM QUE VARIA", AMBER)
    for k, (cue, ic, nome, fixo, varia) in enumerate(DIADIA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 360 + k * 400
        card(c, x - 175, 220 + d, 350, 420, a)
        ic(c, x, 320 + d, a)
        text(c, nome, x, 440 + d, 36, "black", INK, a)
        pill(c, fixo, x, 510 + d, FIXO, size=26, a=a, anchor="center", bounds=(0, 1920))
        text(c, varia, x, 590 + d, 28, "black", VARIA, a)
    ae = ep(t, C["16.e"], 0.5)
    if ae > 0:
        regra(c, "dobrar o consumo NÃO dobra a conta", W / 2, 740, ae, 36, RED)


# ======================================================================
# bloco G — a pergunta da origem
# ======================================================================

def b_origem(c, t, C, B):
    head_seq(c, t, C, [("17", "A PERGUNTA DA ORIGEM", "ZERO DE UM DÁ ZERO DO OUTRO?", PURPLE),
                       ("18", "ATENÇÃO", "PASSAR PELA ORIGEM NÃO BASTA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["17", "18"])
    if sid == "17":
        a0 = ep(t, C["17"], 0.5)
        selo(c, W / 2, 230, a0, "PERGUNTA DA ORIGEM", PURPLE, -2, 32)
        aa = ep(t, C["17.a"], 0.5)
        if aa > 0:
            boxed(c, 360, 290, 1200, 120, PURPLE, aa, 0.08)
            ftext(c, "a 1ª grandeza vale 0  →  a 2ª também vale 0?", W / 2, 368, 42, "black", INK, aa)
        for cue, x, ic, s1, s2, col, ok in (("17.b", 560, saco_arroz, "0 kg → R$ 0", "pode ser proporcional", GREEN, True),
                                            ("17.c", 1360, taxi, "0 km → R$ 6", "NÃO é proporcional", RED, False)):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            card(c, x - 320, 460 + d, 640, 340, a)
            ic(c, x - 160, 620 + d, a, 0.75)
            ftext(c, s1, x + 120, 590 + d, 40, "black", INK, a)
            check_icon(c, x + 120, 660 + d, 30, a, col, "check" if ok else "x")
            text(c, s2, x + 120, 740 + d, 30, "black", col, a)
        return
    a0 = ep(t, C["18"], 0.5)
    if a0 > 0:
        K.atalho(c, 1180, 210, 540, 190, "ATALHO", ["passar pela origem não basta:", "também tem de ser RETA"], a0, 28)
    g = Graf(330, 770, 640, 480, 4.2, 18)
    aa = ep(t, C["18.a"], 0.5)
    g.eixos(c, aa, "lado", "área", tx=[(k, str(k)) for k in range(1, 5)], ty=[(v, str(v)) for v in (4, 8, 12, 16)])
    g.curva(c, lambda x: x * x, 0, 4.2, BLUE, aa, ep(t, C["18.a"], 1.4))
    g.ponto(c, 2, 4, BLUE, aa); g.ponto(c, 4, 16, BLUE, ep(t, C["18.a"] + 1.0, 0.4))
    if aa > 0:
        ftext(c, "lado ×2 → área ×4", g.X(2.3), g.Y(13), 30, "black", BLUE, ep(t, C["18.a"] + 1.0, 0.4), align="right")
        text(c, "nasce no 0, mas é CURVA", 1450, 470, 32, "black", BLUE, aa)
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        chip(c, "juros compostos", 1320, 560, RED, ab, 28)
        chip(c, "tarifas por faixa", 1590, 560, RED, ab, 28)
        text(c, "também NÃO são proporcionais", 1450, 640, 28, "black", INK2, ab)
    pill(c, "já vistos na série de Razão", 1450, 720, PURPLE, size=26, a=ep(t, C["18.c"], 0.5), anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

MINI = [("19.a", "20.a", "reta pela origem", "DIRETA", GREEN), ("19.b", "20.b", "reta que corta no 10", "NENHUMA", RED),
        ("19.c", "20.c", "curva que deita", "INVERSA", PURPLE)]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "DIRETA, INVERSA OU NENHUMA?", GREEN), ("20", "VAMOS CONFERIR", "DIRETA, INVERSA OU NENHUMA?", GREEN)])
    card(c, *CARD_R)
    fs = [lambda x: 3 * x, lambda x: 2 * x + 10, lambda x: 40 / x]
    rng = [(0, 10), (0, 10), (40 / 28, 10.5)]
    for k, (cue, rc, desc, resp, col) in enumerate(MINI):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 520
        card(c, x - 30, 210 + d, 460, 440, a)
        badge_num(c, k + 1, x, 240 + d, a, 24, bg=INK)
        g = Graf(x + 40, 580 + d, 340, 290, 11, 30)
        g.eixos(c, a)
        g.curva(c, fs[k], rng[k][0], rng[k][1], INK, a, ep(t, C[cue], 1.2), 6)
        if k == 1:
            text_mid(c, "10", g.x0 - 12, g.Y(10), 24, "black", INK2, a, align="right")
            line(c, g.x0 - 6, g.Y(10), g.x0 + 6, g.Y(10), INK, a, 3)
        text(c, desc, x + 200, 630 + d, 24, "bold", INK2, a)
        if t >= C["20"]:
            ra = ep(t, C[rc], 0.5)
            if ra > 0:
                chip(c, resp, x + 200, 720, col, ra, 34)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 750)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Direta: reta que nasce na origem.", "Inversa: hipérbole que nunca toca os eixos.",
          "Zero de um dá zero do outro? Se não, há parcela fixa e não é proporção."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 58)


ERROS = [("Achar que toda reta é proporção direta", "a direta também é uma reta",
          "a direta é a reta que NASCE na origem; cortou acima do zero, tem parcela fixa"),
         ("Dobrar o preço do táxi junto com a distância", "a distância dobrou, e a gente dobra tudo no automático",
          "a bandeirada não dobra: só a parte por quilômetro"),
         ("Achar que a hipérbole toca os eixos", "no desenho ela chega bem pertinho",
          "o tempo de uma viagem nunca chega a zero: os eixos são assíntotas"),
         ("Achar que “estar relacionado” é “ser proporcional”", "uma grandeza muda quando a outra muda",
          "táxi, conta de luz e área mudam junto e nenhum é proporcional: proporção exige o k constante")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25"], ERROS)


# ======================================================================
# Questão 4 do material (alternativas longas: lista própria com coluna de motivos)
# ======================================================================

Q4_ENUN = "Entre as situações abaixo, aquela em que as duas grandezas envolvidas são diretamente proporcionais é"
ALTS4 = [("A", "o valor de uma corrida de táxi com bandeirada fixa, em função da distância", "0 km → R$ 6: não"),
         ("B", "o valor da conta de luz com taxa de disponibilidade, em função do consumo", "consumo 0 → taxa mínima"),
         ("C", "o preço total de arroz vendido a R$ 5,00 o quilo, em função da quantidade comprada", "0 kg → R$ 0 · k = 5"),
         ("D", "a área de um terreno quadrado, em função da medida do lado", "quadrática: lado ×2 → área ×4"),
         ("E", "o tempo de uma viagem de distância fixa, em função da velocidade média", "inversa")]


def _alts_longas(c, t, C, alts, okL, ok_cue, cues_in, cues_x, x=200, y0=300, w=1060, size=28, gap=12, xp=1730):
    aok = ep(t, ok_cue, 0.5)
    y = y0
    for L, s, why in alts:
        a, d = rise(t, cues_in[L])
        ok = L == okL
        lines = K.wrap(s, "bold", size, w - 60)
        hh = len(lines) * (size + 8) + 10
        ax = ep(t, cues_x.get(L, 1e9), 0.4) if not ok else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 16, y - 8 + d, xp - x + 26, hh + 12, 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + hh / 2 + d - 2, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
            for j, ln in enumerate(lines):
                yy = y + d + size + j * (size + 8)
                text(c, ln, x + 50, yy, size, "bold", INK, a * (1 - 0.5 * ax), align="left")
                if ax > 0:
                    strike(c, x + 46, yy - size * 0.35, x + 54 + text_w(ln, "bold", size), yy - size * 0.35, ax, RED, ax)
            if ax > 0:
                pill(c, why, xp, y + hh / 2 + d, RED, size=22, a=ax, anchor="right", bounds=(0, 1920))
            if ok and aok > 0:
                pill(c, why, xp, y + hh / 2 + d, GREEN, size=22, a=aok, anchor="right", bounds=(0, 1920))
        y += hh + gap
    return y


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · QUAL É DIRETA?", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    y = 222
    for ln in K.wrap(Q4_ENUN, "black", 32, 1520):
        text(c, ln, 190, y, 32, "black", INK, a0, align="left")
        y += 42
    text(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["27.xa"], "B": C["27.xb"], "D": C["28.xd"], "E": C["28.xe"]}
    _alts_longas(c, t, C, ALTS4, "C", C["27.ok"], cues_in, cues_x, y0=y + 6)
    pause_timer(c, t, C["26.end"] - 1.9, 1560, 520)
    if t >= C["27"]:
        selo(c, 1560, 810, ep(t, C["27"], 0.4) * (1 - ep(t, C["28.a"], 0.4)), "PERGUNTA DA ORIGEM", PURPLE, -2, 26)
    a = ep(t, C["28.a"], 0.5)
    if a > 0:
        pill(c, "as 5 estão RELACIONADAS · só 1 é proporcional", W / 2, 812, PURPLE, size=26, a=a, anchor="center", bounds=(0, 1920))


# ======================================================================
# Questão 5 do material (a prova oficial do gancho)
# ======================================================================

ALTS5 = [("A", "R$ 40,00", "esqueceu a bandeirada", RED), ("B", "R$ 46,00", "", GREEN), ("C", "R$ 48,00", "não sai da regra", RED),
         ("D", "R$ 52,00", "bandeirada 2 vezes", RED), ("E", "R$ 58,00", "dobrou e somou outra", RED)]


def _enunciado(c, linhas, a, y0=250, size=34, w=640):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · A PARCELA FIXA", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    _enunciado(c, [("Uma corrida de táxi custa R$ 6,00 de bandeirada mais R$ 2,50 por quilômetro rodado.", INK),
                   ("Sabendo que uma corrida de 8 km custa R$ 26,00, o valor de uma corrida de 16 km será de", BLUE)],
               a0, 240, 30, 680)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ACDE"}
    if t >= C["29.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS5, 980, 230, 720, 40, C["30.ok"], "B", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["29.end"] - 1.9, 470, 660)
    if t >= C["30"]:
        ra = ep(t, C["30"], 0.4)
        rrect(c, 170, 540, 720, 260, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["30.a"], 0.4)
        ftext(c, "0 km → R$ 6: nada de dobrar", 530, 600, 32, "black", FIXO, aa)
        ab = ep(t, C["30.b"], 0.4)
        if ab > 0:
            xe = barra(c, 210, 640, [(6, FIXO, "6"), (40, VARIA, "2,50 × 16 = 40")], ab, esc=12, h=70)
            ftext(c, "= 46", xe + 10, 690, 36, "black", GREEN, ab, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "VÁRIAS GRANDEZAS", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    if aa > 0:
        fmid(c, "y", 560, 420, 140, "black", INK, aa)
        fmid(c, "depende de", 830, 420, 40, "black", INK2, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        chip(c, "a: DIRETA", 1200, 340, BLUE, ab, 40)
        chip(c, "b: INVERSA", 1200, 500, PURPLE, ab, 40)
    acc = ep(t, C["33.c"], 0.5)
    if acc > 0:
        expr(c, "R = k · L/A", 760, 660, 80, acc, cores={0: PURPLE})
        text(c, "metade das fórmulas de Física", 1250, 680, 34, "black", INK2, acc)
    pill(c, "ep. 4 · várias grandezas ao mesmo tempo", W / 2, 800, PURPLE, size=30, a=ep(t, C["33.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Você já tinha caído na bandeirada do táxi?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, compras=b_compras, arroz=b_arroz, viagem=b_viagem,
              taxi=b_taxi, teste=b_teste, contas=b_contas, diadia=b_diadia, origem=b_origem, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q4=b_q4, q5=b_q5, ponte=b_ponte, cta=b_cta)
