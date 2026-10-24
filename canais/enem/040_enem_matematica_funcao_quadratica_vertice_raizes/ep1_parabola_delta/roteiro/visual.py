"""Visual — Função Quadrática, Episódio 1: a parábola, concavidade, corte no eixo y e o que o Δ desenha (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: plano() + eixos() + curva() (gráfico cartesiano com a parábola desenhada aos poucos e cortada nas
bordas), olhos() (os dois olhinhos que fazem a parábola "sorrir" ou ficar "triste"), chao() (o eixo x como chão),
icone_bola() / icone_bebedouro() / icone_antena() (os três arcos do dia a dia), linha() (texto com cor por trecho).
Cores com função: azul = definição / o c · roxo = regra / o a · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum040", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_quadratica_ep1_parabola_delta.mp4"
CARD_R = K.CARD_R
CHAO = "#8A6A4A"


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


def lei(c, cx, cy, size, a, f="f(x)"):
    """f(x) = ax² + bx + c com a roxo e c azul"""
    return expr(c, f"{f} = ax^2 + bx + c", cx, cy, size, a, cores={2: PURPLE, 6: BLUE})


class plano:
    """retângulo de gráfico (gx, gy, gw, gh) para a janela [x0, x1] × [y0, y1]"""

    def __init__(self, gx, gy, gw, gh, x0, x1, y0, y1):
        self.gx, self.gy, self.gw, self.gh = gx, gy, gw, gh
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1

    def px(self, x):
        return self.gx + (x - self.x0) / (self.x1 - self.x0) * self.gw

    def py(self, y):
        return self.gy + self.gh - (y - self.y0) / (self.y1 - self.y0) * self.gh

    def pt(self, x, y):
        return self.px(x), self.py(y)


def eixos(c, g, a, xl="x", yl="y", col=None, w=4, ticks_x=(), ticks_y=(), size=24, chao_=False):
    """eixos que passam pela origem (ou pela borda, se a origem estiver fora)"""
    if a <= 0:
        return
    col = col or INK2
    yx = g.py(0) if g.y0 <= 0 <= g.y1 else g.py(g.y0)
    xy = g.px(0) if g.x0 <= 0 <= g.x1 else g.px(g.x0)
    if chao_:
        rrect(c, g.gx - 10, yx, g.gw + 20, 14, 4, CHAO, a * 0.25)
        line(c, g.gx - 10, yx, g.gx + g.gw + 10, yx, CHAO, a, 6)
    else:
        arrow(c, g.gx - 10, yx, g.gx + g.gw + 20, yx, col, a, w, 16)
    arrow(c, xy, g.gy + g.gh + 10, xy, g.gy - 20, col, a, w, 16)
    if xl:
        ftext(c, xl, g.gx + g.gw + 30, yx + 10, size + 4, "black", col, a, align="left")
    if yl:
        ftext(c, yl, xy + 16, g.gy - 8, size + 4, "black", col, a, align="left")
    for v in ticks_x:
        x = g.px(v)
        line(c, x, yx - 8, x, yx + 8, col, a, 3)
        ftext(c, f"{v:g}".replace(".", ","), x, yx + 40, size, "bold", col, a)
    for v in ticks_y:
        y = g.py(v)
        line(c, xy - 8, y, xy + 8, y, col, a, 3)
        ftext(c, f"{v:g}".replace(".", ","), xy - 16, y + size * 0.36, size, "bold", col, a, align="right")


def curva(c, g, f, a, col, prog_=1.0, w=7, xa=None, xb=None, n=160):
    """desenha y = f(x) de xa a xb (padrão: a janela toda), só o que cabe na janela; prog_ revela da esquerda p/ a direita"""
    if a <= 0 or prog_ <= 0:
        return
    xa = g.x0 if xa is None else xa
    xb = g.x1 if xb is None else xb
    xe = xa + (xb - xa) * clamp(prog_)
    p = skia.Path()
    pen = False
    for i in range(n + 1):
        x = xa + (xe - xa) * i / n
        y = f(x)
        if g.y0 - 0.02 * (g.y1 - g.y0) <= y <= g.y1 + 0.02 * (g.y1 - g.y0):
            X, Y = g.pt(x, y)
            if pen:
                p.lineTo(X, Y)
            else:
                p.moveTo(X, Y); pen = True
        else:
            pen = False
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(g.gx - 4, g.gy - 4, g.gw + 8, g.gh + 8))
    c.drawPath(p, paint(col, a, stroke=w, cap_round=True))
    c.restore()


def ponto(c, g, x, y, a, col, r=12, rot=None, size=26, dx=0, dy=-34, rcol=None):
    if a <= 0:
        return
    X, Y = g.pt(x, y)
    c.drawCircle(X, Y, r + 5, paint("#FFFFFF", a))
    c.drawCircle(X, Y, r, paint(col, a))
    if rot:
        ftext(c, rot, X + dx, Y + dy, size, "black", rcol or col, a)


def olhos(c, g, xc, yb, a, triste=False, col=None):
    """os olhinhos acima do fundo (sorri) ou abaixo... da boca: para a parábola parecer um rosto"""
    if a <= 0:
        return
    col = col or INK
    X, Y = g.pt(xc, yb)
    off = 70 if not triste else 70
    for s in (-1, 1):
        c.drawCircle(X + s * 54, Y - off, 13, paint(col, a))


def icone_bola(c, cx, cy, a, prog_=1.0):
    if a <= 0:
        return
    line(c, cx - 190, cy + 120, cx + 190, cy + 120, CHAO, a, 6)
    p = skia.Path()
    n = 40
    u = clamp(prog_)
    pts = [(cx - 160 + 320 * i / n, cy + 110 - 230 * (1 - ((i / n) * 2 - 1) ** 2)) for i in range(n + 1)]
    m = max(1, int(n * u))
    p.moveTo(*pts[0])
    for q in pts[1:m + 1]:
        p.lineTo(*q)
    pe = paint(PURPLE, a, stroke=5, cap_round=True)
    pe.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
    c.drawPath(p, pe)
    bx, by = pts[m]
    c.drawCircle(bx, by - 16, 22, paint("#FFFFFF", a))
    c.drawCircle(bx, by - 16, 22, paint(INK, a, stroke=4))
    c.drawCircle(bx - 6, by - 22, 7, paint(INK, a))


def icone_bebedouro(c, cx, cy, a, prog_=1.0):
    if a <= 0:
        return
    rrect(c, cx - 170, cy + 40, 150, 100, 14, "#B8C0CC", a)
    rrect(c, cx - 110, cy + 10, 30, 40, 6, "#8A93A1", a)
    p = skia.Path()
    n = 40
    u = clamp(prog_)
    x0, y0 = cx - 95, cy + 10
    pts = [(x0 + 230 * i / n, y0 - 150 * (1 - ((i / n) * 2 - 1) ** 2) + 120 * (i / n) ** 2) for i in range(n + 1)]
    m = max(1, int(n * u))
    p.moveTo(*pts[0])
    for q in pts[1:m + 1]:
        p.lineTo(*q)
    c.drawPath(p, paint("#3BA3E0", a, stroke=12, cap_round=True))
    rrect(c, cx + 60, cy + 120, 140, 20, 8, "#B8C0CC", a)


def icone_antena(c, cx, cy, a):
    if a <= 0:
        return
    p = skia.Path()
    n = 40
    for i in range(n + 1):
        x = -130 + 260 * i / n
        y = 0.0062 * x * x
        X, Y = cx + x, cy - 20 + y
        if i == 0:
            p.moveTo(X, Y - 100)
        p.lineTo(X, Y - 100 + 0)
    pts = [(cx - 130 + 260 * i / n, cy - 120 + 0.0062 * (-130 + 260 * i / n) ** 2) for i in range(n + 1)]
    q = skia.Path(); q.moveTo(*pts[0])
    for pt_ in pts[1:]:
        q.lineTo(*pt_)
    c.drawPath(q, paint("#8A93A1", a, stroke=14, cap_round=True))
    line(c, cx, cy - 120, cx, cy - 40, "#8A93A1", a, 5)
    c.drawCircle(cx, cy - 40, 12, paint(INK2, a))
    line(c, cx, cy - 120, cx, cy + 120, "#5B6270", a, 8)
    line(c, cx - 70, cy + 120, cx + 70, cy + 120, CHAO, a, 6)


# ======================================================================
# abertura
# ======================================================================

BOLA = [(0, 0), (1, 15), (2, 20), (3, 15), (4, 0)]


def h_bola(t_):
    return 20 * t_ - 5 * t_ * t_


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO QUADRÁTICA · EPISÓDIO 1", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    g = plano(980, 230, 700, 470, -0.3, 4.6, -2, 23)
    if aa > 0:
        # tabela
        rrect(c, 160, 230, 700, 200, 24, "#FFFFFF", aa, shadow=True)
        text(c, "t (s)", 240, 300, 30, "black", INK2, aa)
        text(c, "h (m)", 240, 390, 30, "black", INK2, aa)
        line(c, 180, 335, 840, 335, LIGHT, aa, 3)
        for k, (tt, hh) in enumerate(BOLA):
            ak = ep(t, C["01.a"] + 1.2 + k * 0.45, 0.3)
            x = 380 + k * 112
            text(c, str(tt), x, 300, 40, "black", INK, ak)
            text(c, str(hh), x, 390, 40, "black", BLUE, ak)
        eixos(c, g, aa, "t (s)", "h (m)", ticks_x=(1, 2, 3, 4), ticks_y=(5, 10, 15, 20))
        for k, (tt, hh) in enumerate(BOLA):
            ponto(c, g, tt, hh, ep(t, C["01.a"] + 1.4 + k * 0.45, 0.3), BLUE, 11)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        degs = ["+15", "+5", "−5", "−15"]
        for k in range(4):
            ak = ep(t, C["01.b"] + k * 0.6, 0.3)
            x1, y1 = g.pt(*BOLA[k]); x2, y2 = g.pt(*BOLA[k + 1])
            line(c, x1, y1, x2, y1, AMBER, ak, 4, dash=[10, 8])
            line(c, x2, y1, x2, y2, AMBER, ak, 5)
            ftext(c, degs[k], x2 + (18 if k < 2 else -18), (y1 + y2) / 2 + 12, 30, "black", AMBER, ak,
                  align="left" if k < 2 else "right")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        ga = plano(200, 500, 560, 260, -0.3, 4.6, -1, 22)
        rrect(c, 160, 470, 700, 340, 24, "#FFFFFF", acc, shadow=True)
        text(c, "FUNÇÃO AFIM: degraus iguais", 510, 510, 28, "black", PURPLE, acc)
        line(c, ga.px(0), ga.py(0), ga.px(4), ga.py(20), PURPLE, acc, 5)
        for k in range(4):
            x1, y1 = ga.pt(k, 5 * k); x2, y2 = ga.pt(k + 1, 5 * k + 5)
            line(c, x1, y1, x2, y1, PURPLE, acc, 3, dash=[8, 6])
            line(c, x2, y1, x2, y2, PURPLE, acc, 4)
            ftext(c, "+5", x2 + 12, (y1 + y2) / 2 + 10, 24, "black", PURPLE, acc, align="left")
        selo(c, 1330, 790, ep(t, C["01.c"] + 1.6, 0.4), "AQUI: DEGRAUS DIFERENTES", AMBER, -3, 30)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        curva(c, g, h_bola, ad, BLUE, ep(t, C["01.d"], 1.6), 7, -0.15, 4.15)
        pill(c, "PARÁBOLA", g.px(2), g.py(20) - 60, BLUE, size=30, a=ep(t, C["01.d"] + 1.4, 0.4), anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO QUADRÁTICA · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de FUNÇÃO QUADRÁTICA", W / 2, 230, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "PARA ONDE ABRE", "boca para cima ou para baixo", PURPLE),
             ("02.b", "ONDE CORTA", "o eixo vertical", BLUE),
             ("02.c", "QUANTOS TOQUES", "no eixo horizontal", AMBER)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 310, 460, 360, 26, "#FFFFFF", ak, shadow=True)
        g = plano(x - 150, 350, 300, 170, -1, 5, -3, 6)
        line(c, g.gx, g.py(0), g.gx + g.gw, g.py(0), LIGHT, ak, 3)
        line(c, g.px(0), g.gy, g.px(0), g.gy + g.gh, LIGHT, ak, 3)
        curva(c, g, lambda x: (x - 1) * (x - 3), ak, col, 1.0, 5)
        if k == 1:
            ponto(c, g, 0, 3, ak, BLUE, 9)
        if k == 2:
            ponto(c, g, 1, 0, ak, AMBER, 9); ponto(c, g, 3, 0, ak, AMBER, 9)
        text(c, tit, x, 590, 38, "black", col, ak)
        text(c, sub, x, 640, 26, "bold", INK2, ak)
    pill(c, "sem desenhar", W / 2, 750, GREEN, size=30, a=ep(t, C["02.c"] + 1.6, 0.4), anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        rrect(c, 260, y - 80, 1400, 160, 24, "#FFFFFF", a, shadow=True)
        pill(c, "série de Equação do 2º grau", 300, y - 80, BLUE, size=22, a=a)
        text(c, "Bhaskara", 480, y + 20, 40, "black", INK, a)
        expr(c, "Δ = b^2 − 4ac", 960, y + 10, 50, a, cores={0: PURPLE})
        text(c, "soma e produto", 1440, y + 20, 40, "black", INK, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 480 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, "série de Função afim", 300, y - 70, BLUE, size=22, a=a)
        linha(c, [("reta: sobe sempre no ", INK), ("MESMO RITMO", PURPLE)], 960, y + 10, 44, a)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 650 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, "série de Conceito de função", 300, y - 70, BLUE, size=22, a=a)
        linha(c, [("gráfico = os pontos ", INK), ("(x, f(x))", BLUE)], 960, y + 10, 44, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS ARCOS DO DIA A DIA", "O QUE ELES TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    for k, (cue, tit) in enumerate((("04.a", "BOLA CHUTADA"), ("04.b", "BEBEDOURO"), ("04.c", "ANTENA PARABÓLICA"))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 450 + k * 510
        rrect(c, x - 230, 210, 460, 470, 24, "#FFFFFF", ak, shadow=True)
        if k == 0:
            icone_bola(c, x, 430, ak, ep(t, C[cue], 1.6))
        elif k == 1:
            icone_bebedouro(c, x, 430, ak, ep(t, C[cue], 1.2))
        else:
            icone_antena(c, x, 440, ak)
        text(c, tit, x, 640, 32, "black", INK, ak)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "A MESMA CURVA · E ELA TEM UMA LEI", W / 2, 760, ad, 38, BLUE)


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "DEFINIÇÃO", "FUNÇÃO QUADRÁTICA", BLUE), ("06", "E SE O a FOR ZERO?", "a ≠ 0", BLUE)])
    card(c, *CARD_R)
    if t < C["06"]:
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            rrect(c, 460, 200, 1000, 140, 26, mix("#FFFFFF", BLUE, 0.10), aa)
            lei(c, W / 2, 270, 76, aa)
            pill(c, "função quadrática = função do 2º grau", W / 2, 375, BLUE, size=26, a=aa, anchor="center")
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            for k, (s_, col) in enumerate((("a", PURPLE), ("b", INK), ("c", BLUE))):
                x = 420 + k * 230
                c.drawCircle(x, 500, 50, paint(col, ab * 0.14))
                text_mid(c, s_, x, 500, 64, "black", col, ab)
            text(c, "COEFICIENTES", 650, 610, 32, "black", INK, ab)
            text(c, "os números fixos da lei", 650, 655, 26, "bold", INK2, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, 1040, 430, 560, 320, 24, "#FFFFFF", acc, shadow=True)
            g = plano(1110, 470, 420, 190, -0.3, 4.6, -2, 23)
            curva(c, g, h_bola, acc, BLUE, ep(t, C["05.c"], 1.0), 6, -0.1, 4.1)
            text(c, "PARÁBOLA: a curva em arco", 1320, 715, 30, "black", BLUE, acc)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        expr(c, "0x^2 + bx + c", 660, 300, 70, aa, cores={0: RED})
        strike(c, 470, 300, 620, 300, ep(t, C["06.a"] + 1.0, 0.4), RED, ep(t, C["06.a"] + 1.0, 0.4))
        selo(c, 660, 420, ep(t, C["06.a"] + 1.4, 0.4), "o x² SOME", RED, -4, 32)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        expr(c, "f(x) = bx + c", 660, 560, 64, ab, cores={2: INK, 4: BLUE})
        pill(c, "FUNÇÃO AFIM", 660, 650, PURPLE, size=28, a=ab, anchor="center")
        rrect(c, 1080, 230, 520, 420, 24, "#FFFFFF", ab, shadow=True)
        g = plano(1140, 280, 400, 300, -1, 5, -1, 8)
        eixos(c, g, ab, "x", "y")
        curva(c, g, lambda x: 1.2 * x + 1, ab, PURPLE, ep(t, C["06.b"], 1.0), 6)
        text(c, "reta", 1340, 620, 30, "black", PURPLE, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        regra(c, "QUEM FAZ A CURVA É O x²", W / 2, 770, acc, 38)


# ======================================================================
# bloco b — concavidade
# ======================================================================

def b_concavidade(c, t, C, B):
    head(c, t, B["start"], "CONCAVIDADE", "QUEM DECIDE É SÓ O a", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        pill(c, "concavidade = para onde a boca aponta", W / 2, 215, BLUE, size=28, a=aa, anchor="center")
    for k, (cue, s_, f, col, tit, sub, yb) in enumerate((
            ("07.b", "a > 0", lambda x: 0.6 * (x - 2) ** 2 - 1.6, GREEN, "SORRI", "fundo = MÍNIMO", -1.6),
            ("07.c", "a < 0", lambda x: -0.6 * (x - 2) ** 2 + 1.6, RED, "FICA TRISTE", "topo = MÁXIMO", 1.6))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x0 = 220 + k * 760
        rrect(c, x0, 270, 720, 470, 24, "#FFFFFF", ak, shadow=True)
        g = plano(x0 + 60, 330, 380, 330, -0.2, 4.2, -2.6, 2.6)
        curva(c, g, f, ak, col, ep(t, C[cue], 1.0), 8)
        if k == 0:
            olhos(c, g, 2, 0.4, ep(t, C[cue] + 0.8, 0.4))
        else:
            olhos(c, g, 2, 1.7, ep(t, C[cue] + 0.8, 0.4), True)
        ponto(c, g, 2, yb, ep(t, C[cue] + 1.6, 0.4), PURPLE, 11)
        expr(c, s_, x0 + 580, 400, 56, ak, cores={0: PURPLE, 2: PURPLE})
        text(c, tit, x0 + 580, 520, 40, "black", col, ak)
        text(c, sub, x0 + 580, 590, 28, "black", PURPLE, ep(t, C[cue] + 1.6, 0.4))
        text(c, "sem " + ("máximo" if k == 0 else "mínimo"), x0 + 580, 640, 26, "bold", INK2, ep(t, C[cue] + 2.4, 0.4))
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        pill(c, "a bola sobe e desce: tem TOPO → a < 0", W / 2, 785, PURPLE, size=30, a=ad, anchor="center")


def b_abertura(c, t, C, B):
    head(c, t, B["start"], "E O TAMANHO DO a?", "A ABERTURA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    g = plano(320, 220, 760, 560, -3, 3, -0.5, 9)
    eixos(c, g, aa, "x", "y")
    itens = [(0.5, "½x²", BLUE), (1, "x²", PURPLE), (3, "3x²", RED)]
    for k, (aa_, s_, col) in enumerate(itens):
        ak = ep(t, C["08.a"] + 0.8 + k * 0.9, 0.4)
        curva(c, g, lambda x, q=aa_: q * x * x, ak, col, ep(t, C["08.a"] + 0.8 + k * 0.9, 0.9), 6)
        if ak > 0:
            rrect(c, 1180, 260 + k * 120, 380, 90, 18, mix("#FFFFFF", col, 0.10), ak)
            ftext(c, s_, 1370, 320 + k * 120, 46, "black", col, ak)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        regra(c, "MAIOR |a| → MAIS FECHADA", 1370, 680, ab, 30)


# ======================================================================
# bloco c — o c
# ======================================================================

def f1(x):
    return 2 * x * x - 8 * x + 6


def b_corte_y(c, t, C, B):
    head(c, t, B["start"], "O COEFICIENTE c", "ONDE CORTA O EIXO VERTICAL", BLUE)
    card(c, *CARD_R)
    g = plano(240, 220, 640, 560, -0.8, 4.6, -3, 8)
    aa = ep(t, C["09.a"], 0.5)
    eixos(c, g, aa, "x", "y", ticks_x=(1, 2, 3, 4), ticks_y=(2, 4, 6))
    if aa > 0:
        line(c, g.px(0), g.gy - 10, g.px(0), g.gy + g.gh, BLUE, aa * 0.6, 8)
        pill(c, "aqui x = 0", g.px(0) + 20, g.gy + 30, BLUE, size=24, a=aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        expr(c, "f(0) = a · 0^2 + b · 0 + c", 1340, 290, 46, ab)
        expr(c, "f(0) = c", 1340, 380, 60, ep(t, C["09.b"] + 2.0, 0.4), cores={2: BLUE})
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        curva(c, g, f1, acc, PURPLE, ep(t, C["09.c"], 1.2), 6)
        rrect(c, 1000, 450, 680, 110, 20, "#FFFFFF", acc, shadow=True)
        expr(c, "2x^2 − 8x + 6", 1340, 505, 50, acc, cores={4: BLUE})
        ponto(c, g, 0, 6, ep(t, C["09.c"] + 1.6, 0.4), BLUE, 13, "(0, 6)", 30, 80, 10)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        pill(c, "o b (com o a): de que lado fica a ponta · ep. 2", 1340, 650, GRAY, size=24, a=ad, anchor="center")


def b_atalho_c(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "PONHA x = 0", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 260, 210, 1400, 170, "ATALHO · CORTE NO EIXO VERTICAL", ["ponha x = 0: sobra o c"], aa, 48)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("c = ", INK), ("ALTURA", BLUE), (" do corte no eixo vertical", INK)], W / 2, 470, 40, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 560, 540, 800, 220, 24, "#FFFFFF", acc, shadow=True)
        expr(c, "h(t) = 20t − 5t^2 + 0", 960, 610, 50, acc, cores={6: BLUE})
        linha(c, [("h(0) = ", INK), ("0", BLUE), ("  →  sai do chão", INK2)], 960, 700, 40, acc)


# ======================================================================
# bloco d — o a anda com o x²
# ======================================================================

def b_potencia(c, t, C, B):
    head(c, t, B["start"], "O a ANDA COM O x²", "PELA POTÊNCIA, NÃO PELA POSIÇÃO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, 410, 210, 1100, 150, 26, "#FFFFFF", aa, shadow=True)
        hi = ep(t, C["11.c"], 0.5)
        expr(c, "h(t) = 20t − 5t^2", W / 2, 285, 80, aa, cores={2: mix(INK, AMBER, ep(t, C["11.b"], 0.4) * (1 - hi)),
                                                                   3: mix(INK, PURPLE, hi), 4: mix(INK, PURPLE, hi)})
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        selo(c, 700, 440, ab, "a = 20?", AMBER, -5, 40)
        strike(c, 600, 440, 800, 440, ep(t, C["11.c"], 0.4), RED, ep(t, C["11.c"], 0.4))
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        for k, (s_, v, col) in enumerate((("a", "−5", PURPLE), ("b", "20", INK), ("c", "0", BLUE))):
            ak = ep(t, C["11.c"] + 1.6 + k * 0.6, 0.4)
            x = 1000 + k * 200
            rrect(c, x - 85, 400, 170, 170, 22, mix("#FFFFFF", col, 0.10), ak)
            text(c, s_, x, 460, 40, "black", col, ak)
            ftext(c, v, x, 535, 54, "black", col, ak)
        regra(c, "o a está com o t²: a = −5", W / 2, 700, ep(t, C["11.c"] + 1.0, 0.4), 38)


def b_atalho_abc(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "a, b E c PELA POTÊNCIA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 150, "ATALHO", ["identifique pela POTÊNCIA, não pela posição"], aa, 42)
    ab = ep(t, C["12.b"], 0.5)
    for k, (tit, s_, col) in enumerate((("com o x²", "a", PURPLE), ("com o x", "b", INK), ("sem x", "c", BLUE))):
        ak = ep(t, C["12.b"] + k * 1.1, 0.4) * (1 if ab > 0 else 0)
        if ak <= 0:
            continue
        x = 450 + k * 510
        rrect(c, x - 220, 400, 440, 220, 24, "#FFFFFF", ak, shadow=True)
        ftext(c, tit, x, 470, 38, "black", INK2, ak)
        text(c, s_, x, 580, 90, "black", col, ak)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 730, acc, "ESCREVA COM O SINAL", AMBER, -3, 36)


# ======================================================================
# bloco e — raízes
# ======================================================================

def b_raizes(c, t, C, B):
    head(c, t, B["start"], "AS RAÍZES", "ONDE CORTA O EIXO HORIZONTAL", BLUE)
    card(c, *CARD_R)
    g = plano(220, 230, 560, 520, -0.8, 4.6, -3, 8)
    aa = ep(t, C["13.a"], 0.5)
    eixos(c, g, aa, "x", "y", ticks_x=(1, 2, 3, 4))
    curva(c, g, f1, aa, PURPLE, 1.0, 6)
    if aa > 0:
        for r in (1, 3):
            ponto(c, g, r, 0, ep(t, C["13.a"] + 1.0, 0.4), AMBER, 13)
        rrect(c, 900, 200, 780, 110, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "RAIZ ou ZERO: o x em que f(x) = 0", 1290, 268, 34, "black", BLUE, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        expr(c, "ax^2 + bx + c = 0", 1290, 370, 50, ab, cores={0: PURPLE, 4: BLUE})
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 900, 425, 780, 225, 20, "#FFFFFF", acc, shadow=True)
        expr(c, "Δ = (−8)^2 − 4 · 2 · 6", 1290, 480, 46, acc, cores={0: PURPLE})
        expr(c, "Δ = 64 − 48 = 16", 1290, 545, 46, ep(t, C["13.c"] + 3.0, 0.4), cores={0: PURPLE, 6: PURPLE})
        linha(c, [("raízes: ", INK), ("1", AMBER), (" e ", INK), ("3", AMBER)], 1290, 610, 38,
              ep(t, C["13.c"] + 4.6, 0.4))
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 900, 670, 780, 130, 20, mix("#FFFFFF", GREEN, 0.10), ad)
        expr(c, "x^2 − 7x + 10", 1290, 708, 40, ad)
        linha(c, [("S = 7 · P = 10  →  ", INK2), ("2 e 5", GREEN)], 1290, 768, 34, ad)


# ======================================================================
# bloco f — o Δ desenha
# ======================================================================

DELTAS = [("14.b", "Δ > 0", "2 toques", lambda x: (x - 1) * (x - 3), "x² − 4x + 3", (1, 3)),
          ("14.c", "Δ = 0", "1 toque · raiz dupla", lambda x: (x - 2) ** 2, "x² − 4x + 4", (2,)),
          ("14.d", "Δ < 0", "nenhum toque", lambda x: x * x - 2 * x + 3, "x² − 2x + 3", ())]


def b_delta(c, t, C, B):
    head(c, t, B["start"], "O Δ DESENHA", "QUANTAS VEZES ENCOSTA NO CHÃO?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("Δ = discriminante: ", PURPLE), ("conta os toques no CHÃO (o eixo x)", INK)], W / 2, 215, 32, aa)
    for k, (cue, s_, sub, f, lei_, raizes) in enumerate(DELTAS):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x0 = 200 + k * 520
        rrect(c, x0, 260, 480, 520, 24, "#FFFFFF", ak, shadow=True)
        g = plano(x0 + 40, 330, 400, 280, -1.5 if k == 2 else -0.5, 3.5 if k == 2 else 4.5, -1.5, 6.5)
        eixos(c, g, ak, None, None, chao_=True)
        curva(c, g, f, ak, PURPLE if k < 2 else BLUE, ep(t, C[cue], 1.0), 6)
        for r in raizes:
            ponto(c, g, r, 0, ep(t, C[cue] + 1.0, 0.4), AMBER, 12)
        ftext(c, s_, x0 + 240, 680, 50, "black", PURPLE, ak)
        text(c, sub, x0 + 240, 735, 28, "black", AMBER if raizes else INK2, ak)
        ftext(c, lei_, x0 + 240, 315, 26, "bold", INK2, ak)


def b_delta_lado(c, t, C, B):
    head(c, t, B["start"], "Δ < 0: DE QUE LADO?", "QUEM ESCOLHE É O a", PURPLE)
    card(c, *CARD_R)
    g = plano(300, 230, 760, 540, -1, 5, -6, 6)
    aa = ep(t, C["15.a"], 0.5)
    eixos(c, g, aa, "x", "y", chao_=True)
    vira = ep(t, C["15.c"], 1.2)
    s = 1 - 2 * vira
    col = mix(GREEN, RED, vira)
    curva(c, g, lambda x: s * (x * x - 2 * x + 3), aa, col, 1.0, 7)
    if aa > 0:
        pill(c, "inteira de UM LADO SÓ", 1380, 280, BLUE, size=28, a=aa, anchor="center")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        rrect(c, 1140, 360, 480, 160, 22, mix("#FFFFFF", GREEN, 0.10), ab)
        expr(c, "a > 0", 1380, 410, 46, ab, cores={0: PURPLE, 2: PURPLE})
        text(c, "TODA ACIMA do eixo", 1380, 485, 32, "black", GREEN, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 1140, 560, 480, 160, 22, mix("#FFFFFF", RED, 0.08), acc)
        expr(c, "a < 0", 1380, 610, 46, acc, cores={0: PURPLE, 2: PURPLE})
        text(c, "TODA ABAIXO do eixo", 1380, 685, 32, "black", RED, acc)


def b_atalho_olhadas(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "LEITURA EM 3 OLHADAS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 130, "ATALHO", ["leitura em 3 olhadas"], aa, 44)
    for k, (cue, s_, o_que, col) in enumerate((("16.b", "sinal do a", "a BOCA", PURPLE),
                                                ("16.c", "o c", "o CORTE no eixo vertical", BLUE),
                                                ("16.d", "o Δ", "quantos TOQUES no eixo x", AMBER))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 450 + k * 510
        rrect(c, x - 230, 380, 460, 280, 24, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, x, 440, ak, 30, bg=col)
        ftext(c, s_, x, 540, 46, "black", col, ak)
        text(c, o_que, x, 610, 28, "bold", INK2, ak)
    ae = ep(t, C["16.e"], 0.5)
    if ae > 0:
        pill(c, "sem desenhar nada", W / 2, 750, GREEN, size=32, a=ae, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def f2(x):
    return -x * x + 4 * x + 5


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "TRÊS OLHADAS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 195, 1400, 120, 24, "#FFFFFF", aa, shadow=True)
        expr(c, "f(x) = −x^2 + 4x + 5", W / 2, 255, 64, aa)
    perg = [("ABRE PARA?", "17.b", 0.0), ("CORTA O EIXO y EM?", "17.b", 1.6), ("RAÍZES?", "17.b", 3.2)]
    for k, (s_, cue, dt) in enumerate(perg):
        ak = ep(t, C[cue] + dt, 0.4)
        if ak <= 0:
            continue
        y = 380 + k * 120
        rrect(c, 220, y - 45, 620, 90, 18, "#FFFFFF", ak, shadow=True)
        text_mid(c, s_, 250, y, 30, "black", INK, ak, align="left")
    if t < C["18"]:
        pause_timer(c, t, C["17.end"] - 1.9, 1340, 520)
        return
    resp = [("18.a", "boca p/ baixo (a = −1)", PURPLE), ("18.b", "(0, 5)", BLUE), ("18.d", "5 e −1", AMBER)]
    for k, (cue, s_, col) in enumerate(resp):
        ak = ep(t, C[cue], 0.4)
        if ak > 0:
            ftext(c, s_, 820, 380 + k * 120 + 12, 30, "black", col, ak, align="right")
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0 and t < C["18.d"] + 0.3:
        rrect(c, 920, 380, 760, 300, 22, mix("#FFFFFF", GREEN, 0.08), acc)
        text(c, "× (−1) nos dois lados", 1300, 440, 30, "black", GREEN, acc)
        expr(c, "x^2 − 4x − 5 = 0", 1300, 520, 50, acc)
        linha(c, [("S = 4 · P = −5", INK2)], 1300, 610, 36, acc)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        g = plano(960, 330, 640, 420, -2, 6, -3, 10)
        eixos(c, g, ad, "x", "y")
        curva(c, g, f2, ad, PURPLE, ep(t, C["18.d"], 1.0), 6)
        ponto(c, g, 0, 5, ad, BLUE, 11, "(0, 5)", 26, 70, 8)
        ponto(c, g, -1, 0, ad, AMBER, 11, "−1", 26, -10, 44)
        ponto(c, g, 5, 0, ad, AMBER, 11, "5", 26, 10, 44)
        check_icon(c, 300, 760, 22, ep(t, C["18.d"] + 2.0, 0.4), GREEN)
        linha(c, [("5 + (−1) = 4 · 5 · (−1) = −5 · bate", GREEN)], 340, 762, 28, ep(t, C["18.d"] + 2.0, 0.4),
              align="left")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["a positivo sorri e tem mínimo; a negativo fica triste e tem máximo.",
          "c é onde a parábola corta o eixo vertical.",
          "Δ conta quantas vezes a parábola encosta no eixo x."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 60)


ERROS = [("Ler a = 20 em h = 20t − 5t²", "na definição, o a vem primeiro",
          "o a anda com o t²: a = −5"),
         ("Achar que a > 0 tem máximo", "positivo lembra subir, e subir lembra topo",
          "a > 0 sorri: tem FUNDO, tem MÍNIMO"),
         ("Achar que Δ < 0 é função negativa", "os dois são “negativos”",
          "Δ < 0 só diz: sem raiz. x² − 2x + 3 é positiva para todo x (tem o sinal do a)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# questão nova (você faz)
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


ALTS = [("A", "k < 25.", "Δ > 0: dois cortes", RED), ("B", "k = 25.", "Δ = 0: encosta", RED),
        ("C", "k > 25.", "", GREEN), ("D", "k > 100.", "esqueceu o 4: 100 − k", RED),
        ("E", "k < −25.", "sinal trocado: 100 + 4k", RED)]


def b_qnova(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO INÉDITA · VOCÊ FAZ", "TODA ABAIXO DO EIXO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    yend = _enunciado(c, [("Em um programa de computador, o gráfico de f(x) = −x² + 10x − k aparece inteiramente abaixo "
                           "do eixo das abscissas, sem tocá-lo, para certos valores reais da constante k. Esses valores "
                           "são os que satisfazem", INK)], a0, 236, 28)
    text(c, "Questão inédita no estilo ENEM (não está no material)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["24"], 0.3)), align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS, 1000, 260, 680, 40, C["24.ok"], "C", cues_in, cues_x, gap=40)
    if t < C["24"]:
        pause_timer(c, t, C["23.end"] - 1.9, 540, yend + 120)
        return
    y0 = 206
    _painel(c, y0, ep(t, C["24"], 0.4))
    if t < C["25"]:
        aa = ep(t, C["24.a"], 0.4)
        if aa > 0:
            linha(c, [("a = −1 → boca p/ baixo", PURPLE)], 540, y0 + 55, 32, aa)
            linha(c, [("toda abaixo: ", INK), ("Δ < 0", PURPLE)], 540, y0 + 110, 34, ep(t, C["24.a"] + 2.4, 0.4))
        ab = ep(t, C["24.b"], 0.4)
        if ab > 0:
            linha(c, [("a = −1 · b = 10 · c = ", INK), ("−k", BLUE)], 540, y0 + 190, 34, ab)
        acc = ep(t, C["24.c"], 0.4)
        if acc > 0:
            expr(c, "Δ = 10^2 − 4 · (−1) · (−k)", 540, y0 + 280, 38, acc, cores={0: PURPLE})
            expr(c, "Δ = 100 − 4k", 540, y0 + 360, 46, ep(t, C["24.c"] + 3.2, 0.4), cores={0: PURPLE, 4: PURPLE})
        ad = ep(t, C["24.d"], 0.4)
        if ad > 0:
            expr(c, "100 − 4k < 0", 540, y0 + 450, 40, ad)
            expr(c, "k > 25", 540, y0 + 530, 56, ep(t, C["24.d"] + 1.6, 0.4), cores={0: GREEN, 1: GREEN, 2: GREEN})
        return
    aa = ep(t, C["25.a"], 0.4)
    if aa > 0:
        linha(c, [("topo em ", INK), ("x = 5", PURPLE), ("  (o porquê: ep. 2)", GRAY)], 540, y0 + 60, 32, aa)
    ab = ep(t, C["25.b"], 0.4)
    if ab > 0:
        expr(c, "f(5) = −25 + 50 − k", 540, y0 + 150, 40, ab)
        expr(c, "f(5) = 25 − k", 540, y0 + 230, 46, ep(t, C["25.b"] + 2.4, 0.4))
    acc = ep(t, C["25.c"], 0.4)
    if acc > 0:
        g = plano(250, y0 + 290, 560, 240, 0.5, 9.5, -10, 1.5)
        line(c, g.gx, g.py(0), g.gx + g.gw, g.py(0), CHAO, acc, 5)
        curva(c, g, lambda x: -x * x + 10 * x - 30, acc, BLUE, ep(t, C["25.c"], 1.0), 5)
        ponto(c, g, 5, -5, acc, PURPLE, 10, "topo abaixo do chão", 24, 190, 10)
        expr(c, "25 − k < 0 → k > 25", 540, y0 + 580, 38, ep(t, C["25.c"] + 2.0, 0.4))
    if t >= C["26"]:
        check_icon(c, 230, y0 + 50, 18, ep(t, C["26"], 0.4), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O VÉRTICE", PURPLE)
    g = plano(260, 230, 760, 520, -0.3, 6.5, -3, 52)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        line(c, g.gx, g.py(0), g.gx + g.gw, g.py(0), CHAO, aa, 6)
        u = ep(t, C["28.a"], 2.4)
        curva(c, g, lambda x: -5 * x * x + 30 * x, aa, PURPLE, u * 0.46, 5, 0, 6)
        tx = 6 * u * 0.46
        X, Y = g.pt(tx, -5 * tx * tx + 30 * tx)
        c.drawCircle(X, Y, 12, paint(RED, aa))
        rrect(c, 1080, 230, 600, 130, 22, "#FFFFFF", aa, shadow=True)
        expr(c, "h(t) = −5t^2 + 30t", 1380, 295, 50, aa, cores={2: PURPLE})
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        X, Y = g.pt(3, 45)
        for k in range(10):
            ang = k * math.pi / 5
            line(c, X + math.cos(ang) * 20, Y + math.sin(ang) * 20, X + math.cos(ang) * 60 * ab, Y + math.sin(ang) * 60 * ab,
                 AMBER, ab, 5)
        rrect(c, 1080, 400, 600, 200, 22, mix("#FFFFFF", AMBER, 0.20), ab)
        linha(c, [("instante: ", INK), ("t = ?", AMBER)], 1380, 460, 40, ab)
        linha(c, [("altura: ", INK), ("h = ?", AMBER)], 1380, 540, 40, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        text(c, "a resposta mora num PONTO SÓ", 1380, 670, 32, "black", PURPLE, acc)
    pill(c, "ep. 2 · o vértice", 1380, 760, PURPLE, size=30, a=ep(t, C["28.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Onde você já viu uma parábola hoje?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              concavidade=b_concavidade, abertura=b_abertura, corte_y=b_corte_y, atalho_c=b_atalho_c,
              potencia=b_potencia, atalho_abc=b_atalho_abc, raizes=b_raizes, delta=b_delta, delta_lado=b_delta_lado,
              atalho_olhadas=b_atalho_olhadas, exercicio=b_exercicio, recap=b_recap, erros=b_erros, qnova=b_qnova,
              ponte=b_ponte, cta=b_cta)
