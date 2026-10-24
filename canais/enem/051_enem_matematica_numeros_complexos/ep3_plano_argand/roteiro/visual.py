"""Visual — Números Complexos, Episódio 3: o plano de Argand-Gauss — módulo, distância e o giro de 90° (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, selo, regra, atalho,
pause_timer...). Peças deste episódio: Plano (o plano quadriculado com eixo real e imaginário e a conversão de
coordenadas), ponto() (o afixo com rótulo), robo() (o robô do galpão), manivela() (o braço preso na origem com o arco
do giro), tri() (o triângulo retângulo sob um caminho, com a hipotenusa acesa).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
import math
import skia
from pathlib import Path
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum051", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_complexos_ep3_plano_argand.mp4"
CARD_R = K.CARD_R


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


class Plano:
    """plano de Argand-Gauss: origem (ox, oy) na tela, u pixels por unidade, faixa [x0, x1] × [y0, y1]"""

    def __init__(self, ox, oy, u, x0, x1, y0, y1):
        self.ox, self.oy, self.u = ox, oy, u
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1

    def P(self, x, y):
        return self.ox + self.u * x, self.oy - self.u * y

    def draw(self, c, a, rotulos=True, hi_eixos=0.0, numeros=True):
        if a <= 0:
            return
        X0, Y0 = self.P(self.x0 - 0.4, self.y1 + 0.4)
        X1, Y1 = self.P(self.x1 + 0.4, self.y0 - 0.4)
        rrect(c, X0, Y0, X1 - X0, Y1 - Y0, 18, "#FFFFFF", a * 0.9)
        for k in range(self.x0, self.x1 + 1):
            x, _ = self.P(k, 0)
            line(c, x, Y0 + 8, x, Y1 - 8, LIGHT, a, 1.5)
        for k in range(self.y0, self.y1 + 1):
            _, y = self.P(0, k)
            line(c, X0 + 8, y, X1 - 8, y, LIGHT, a, 1.5)
        ex = mix(INK, BLUE, hi_eixos)
        oxx, oyy = self.P(0, 0)
        arrow(c, X0 + 6, oyy, X1 - 4, oyy, ex, a, 4 + 2 * hi_eixos, 14)
        arrow(c, oxx, Y1 - 6, oxx, Y0 + 4, ex, a, 4 + 2 * hi_eixos, 14)
        if rotulos:
            text(c, "eixo real", X1 - 10, oyy + 36, 22, "black", BLUE if hi_eixos > 0 else GRAY, a, align="right")
            text(c, "eixo imaginário", oxx + 14, Y0 + 30, 22, "black", BLUE if hi_eixos > 0 else GRAY, a, align="left")
        if numeros:
            for k in range(self.x0, self.x1 + 1):
                if k:
                    x, _ = self.P(k, 0)
                    text(c, str(k).replace("-", "−"), x, oyy + 26, 17, "bold", GRAY, a * 0.8)
            for k in range(self.y0, self.y1 + 1):
                if k:
                    _, y = self.P(0, k)
                    text(c, str(k).replace("-", "−"), oxx - 12, y + 6, 17, "bold", GRAY, a * 0.8, align="right")


def ponto(c, pl, x, y, s, col, a, dx=16, dy=-16, r=11, size=28, align="left"):
    if a <= 0:
        return
    X, Y = pl.P(x, y)
    c.drawCircle(X, Y, r + 5, paint("#FFFFFF", a))
    c.drawCircle(X, Y, r, paint(col, a))
    if s:
        ftext(c, s, X + dx, Y + dy, size, "black", col, a, align=align)


def zbar(c, pl, x, y, col, a, dx=16, dy=30, size=28):
    """o traço do conjugado sobre o rótulo "z" de ponto()"""
    if a <= 0:
        return
    X, Y = pl.P(x, y)
    w = ftext_w("z", "black", size)
    line(c, X + dx, Y + dy - size * 0.95, X + dx + w, Y + dy - size * 0.95, col, a, 3)


def projecoes(c, pl, x, y, col, a):
    """tracejado do ponto até os eixos"""
    if a <= 0:
        return
    X, Y = pl.P(x, y)
    X0, Y0 = pl.P(0, 0)
    line(c, X, Y, X, Y0, col, a * 0.7, 3, dash=[10, 8])
    line(c, X, Y, X0, Y, col, a * 0.7, 3, dash=[10, 8])


def tri(c, pl, p, q, a, ah=1.0, cat=("", ""), hip="", col_cat=None, col_hip=None, size=28):
    """triângulo retângulo sob o caminho p → q: cateto horizontal, cateto vertical, hipotenusa (alfa ah)"""
    if a <= 0:
        return
    col_cat = col_cat or AMBER
    col_hip = col_hip or GREEN
    (x0, y0), (x1, y1) = pl.P(*p), pl.P(*q)
    line(c, x0, y0, x1, y0, col_cat, a, 5)
    line(c, x1, y0, x1, y1, col_cat, a, 5)
    s = 16
    sx = -s if x1 > x0 else s
    sy = -s if y1 < y0 else s
    line(c, x1 + sx, y0, x1 + sx, y0 + sy, col_cat, a, 2.5)
    line(c, x1 + sx, y0 + sy, x1, y0 + sy, col_cat, a, 2.5)
    if cat[0]:
        pill(c, cat[0], (x0 + x1) / 2, y0 + (34 if y1 < y0 else -34), col_cat, size=size - 4, a=a, anchor="center",
             bounds=(0, 1920))
    if cat[1]:
        pill(c, cat[1], x1 + (40 if x1 > x0 else -40), (y0 + y1) / 2, col_cat, size=size - 4, a=a, anchor="center",
             bounds=(0, 1920))
    if ah > 0:
        line(c, x0, y0, x1, y1, col_hip, ah, 7)
        if hip:
            mx, my = (x0 + x1) / 2, (y0 + y1) / 2
            nx, ny = -(y1 - y0), (x1 - x0)
            nn = math.hypot(nx, ny) or 1
            pill(c, hip, mx + nx / nn * 44 * (-1 if nx > 0 else 1), my + ny / nn * 44 * (-1 if nx > 0 else 1), col_hip,
                 size=size, a=ah, anchor="center", bounds=(0, 1920))


def robo(c, x, y, a, s=1.0):
    """o robô do galpão, centrado em (x, y)"""
    if a <= 0:
        return
    rrect(c, x - 26 * s, y - 30 * s, 52 * s, 44 * s, 12 * s, PURPLE, a, shadow=True)
    c.drawCircle(x - 10 * s, y - 10 * s, 6 * s, paint("#FFFFFF", a))
    c.drawCircle(x + 10 * s, y - 10 * s, 6 * s, paint("#FFFFFF", a))
    line(c, x, y - 30 * s, x, y - 42 * s, PURPLE, a, 3)
    c.drawCircle(x, y - 45 * s, 5 * s, paint(AMBER, a))
    c.drawCircle(x - 15 * s, y + 18 * s, 8 * s, paint(INK, a))
    c.drawCircle(x + 15 * s, y + 18 * s, 8 * s, paint(INK, a))


def manivela(c, pl, ang0, ang1, raio, prog, col, a, arco=True, rot_arco="90°"):
    """o braço preso na origem girando de ang0 a ang1 (graus); devolve a ponta atual"""
    if a <= 0:
        return None
    ang = ang0 + (ang1 - ang0) * prog
    ox, oy = pl.P(0, 0)
    R = raio * pl.u
    ex, ey = ox + R * math.cos(math.radians(ang)), oy - R * math.sin(math.radians(ang))
    if arco and prog > 0.02:
        rr = 70
        pth = skia.Path()
        rect = skia.Rect.MakeLTRB(ox - rr, oy - rr, ox + rr, oy + rr)
        pth.addArc(rect, -ang0, -(ang - ang0))
        c.drawPath(pth, paint(AMBER, a, stroke=5))
        if rot_arco and prog > 0.6:
            mid = math.radians((ang0 + ang) / 2)
            pill(c, rot_arco, ox + 110 * math.cos(mid), oy - 110 * math.sin(mid), AMBER, size=22, a=a, anchor="center",
                 bounds=(0, 1920))
    line(c, ox, oy, ex, ey, col, a, 6)
    c.drawCircle(ox, oy, 12, paint(INK, a))
    return ex, ey


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


def caixa_expr(c, s, cx, cy, a, size=48, col=None, w=None):
    """faixa com uma expressão matemática centrada"""
    if a <= 0:
        return
    ww = w or K.math_w(s, size) + 80
    rrect(c, cx - ww / 2, cy - size * 0.95, ww, size * 1.9, 20, mix("#FFFFFF", col or PURPLE, 0.12), a)
    K.expr(c, s, cx, cy, size, a, cores=None)


def caixa_txt(c, s, cx, cy, a, size=48, col=None, w=None):
    """faixa com texto (sem tipografia matemática) centrado"""
    if a <= 0:
        return
    ww = w or ftext_w(s, "black", size) + 80
    rrect(c, cx - ww / 2, cy - size * 0.95, ww, size * 1.9, 20, mix("#FFFFFF", col or PURPLE, 0.12), a)
    linha(c, [(s, INK)], cx, cy, size, a)


# ======================================================================
# abertura
# ======================================================================

PL_HOOK = Plano(300, 820, 86, 0, 5, 0, 7)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "NÚMEROS COMPLEXOS · EPISÓDIO 3", BLUE)
    card(c, *CARD_R)
    pl = PL_HOOK
    aa = ep(t, C["01.a"], 0.5)
    pl.draw(c, aa, rotulos=False)
    ponto(c, pl, 1, 2, "1 + 2i", BLUE, aa, dx=18, dy=40)
    ponto(c, pl, 4, 6, "4 + 6i", BLUE, aa, dx=-22, dy=-12, align="right")
    pr = ease_io(clamp((t - C["01.a"] - 1.4) / 2.6))
    ab = ep(t, C["01.b"], 0.5)
    acc = ep(t, C["01.c"], 0.5)
    ad = ep(t, C["01.d"], 0.5)
    tri(c, pl, (1, 2), (4, 6), ab, ah=acc, cat=("3", "4") if ab > 0 else ("", ""), hip="5" if ad > 0 else "")
    if aa > 0:
        (x0, y0), (x1, y1) = pl.P(1, 2), pl.P(4, 6)
        robo(c, x0 + (x1 - x0) * pr, y0 + (y1 - y0) * pr - 30, aa, 0.9)
    if ab > 0:
        rrect(c, 1020, 300, 620, 150, 24, mix("#FFFFFF", AMBER, 0.14), ab * (1 - acc))
        linha(c, [("andou ", INK), ("3 + 4 = 7", AMBER), (" m?", INK)], 1330, 375, 52, ab * (1 - acc))
    if acc > 0:
        rrect(c, 1020, 300, 620, 150, 24, mix("#FFFFFF", GREEN, 0.14), acc)
        linha(c, [("em linha reta: ", INK), ("5 m", GREEN)], 1330, 375, 52, acc)
    if ad > 0:
        selo(c, 1330, 600, ad, "O TRIÂNGULO 3, 4, 5", PURPLE, -4, 44)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "COMPLEXOS · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de NÚMEROS COMPLEXOS", W / 2, 240, BLUE, size=28, a=a0, anchor="center")
    itens = [("02.a", "NO PLANO", "qualquer complexo vira ponto", BLUE), ("02.b", "DISTÂNCIAS", "módulo e Pitágoras", PURPLE),
             ("02.c", "GIRO DE 90°", "com uma multiplicação", GREEN)]
    for k, (cue, tit, sb, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 220, 340, 440, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 220, 340, 440, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 44, "black", col, ak)
        text(c, sb, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "par ordenado", 300, y - 75, BLUE, size=22, a=a)
        linha(c, [("(x, y)", PURPLE), ("   1º para o lado · 2º para cima", INK)], 960, y, 46, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "Pitágoras · terá série própria", 300, y - 75, PURPLE, size=22, a=a)
        linha(c, [("hipotenusa² = cateto² + cateto²", INK)], 960, y, 48, a)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódios 1 e 2", 300, y - 75, GREEN, size=22, a=a)
        linha(c, [("i² = −1", PURPLE), ("      z · (conjugado de z) = a² + b²", INK)], 960, y, 44, a)


# ======================================================================
# concreto — o galpão e o programa de desenho
# ======================================================================

PL_GAL = Plano(330, 790, 90, 0, 5, 0, 6)


def b_galpao(c, t, C, B):
    head(c, t, B["start"], "O GALPÃO E A TELA", "DOIS LUGARES ONDE MORAM OS COMPLEXOS", BLUE)
    card(c, *CARD_R)
    pl = PL_GAL
    a0 = ep(t, C["04"], 0.5)
    pl.draw(c, a0, rotulos=False, numeros=True)
    aa = ep(t, C["04.a"], 0.5)
    p1 = ease_io(clamp((t - C["04.a"] - 0.4) / 1.6))
    p2 = ease_io(clamp((t - C["04.a"] - 2.0) / 1.6))
    X0, Y0 = pl.P(0, 0)
    X3, _ = pl.P(3, 0)
    _, Y4 = pl.P(0, 4)
    if aa > 0:
        line(c, X0, Y0, X0 + (X3 - X0) * p1, Y0, AMBER, aa, 6)
        if p2 > 0:
            line(c, X3, Y0, X3, Y0 + (Y4 - Y0) * p2, AMBER, aa, 6)
        rx = X0 + (X3 - X0) * p1
        ry = Y0 + (Y4 - Y0) * p2
        robo(c, rx, ry - 30, aa, 0.9)
        if p1 > 0.95:
            pill(c, "3 m →", (X0 + X3) / 2, Y0 + 40, AMBER, size=24, a=aa, anchor="center")
        if p2 > 0.95:
            pill(c, "4 m ↑", X3 + 60, (Y0 + Y4) / 2, AMBER, size=24, a=aa, anchor="center")
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 1040, 250, 600, 420, 26, INK, ab, shadow=True)
        rrect(c, 1060, 290, 560, 360, 16, "#FFFFFF", ab)
        g = ease_io(clamp((t - C["04.b"] - 0.6) / 1.8)) * 90
        cx, cy = 1340, 470
        pth = skia.Path()
        pts = [(-90, -60), (90, -60), (90, 60), (-90, 60)]
        cs, sn = math.cos(math.radians(-g)), math.sin(math.radians(-g))
        for k, (px, py) in enumerate(pts):
            qx, qy = cx + px * cs - py * sn, cy + px * sn + py * cs
            (pth.moveTo if k == 0 else pth.lineTo)(qx, qy)
        pth.close()
        c.drawPath(pth, paint(mix("#FFFFFF", GREEN, 0.5), ab))
        c.drawPath(pth, paint(GREEN, ab, stroke=4))
        text(c, "programa de desenho: GIRAR", 1340, 710, 28, "black", INK, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        pill(c, "os dois fazem contas com NÚMEROS COMPLEXOS", 1340, 770, PURPLE, size=26, a=acc, anchor="center")


# ======================================================================
# bloco a — o afixo · bloco b — o módulo
# ======================================================================

PL_A = Plano(330, 790, 100, 0, 5, 0, 5)


def b_afixo(c, t, C, B):
    head(c, t, B["start"], "O AFIXO", "TODO COMPLEXO É UM PONTO", BLUE)
    card(c, *CARD_R)
    pl = PL_A
    aa = ep(t, C["05.a"], 0.5)
    ab = ep(t, C["05.b"], 0.5)
    pl.draw(c, aa, rotulos=ab > 0, hi_eixos=ab)
    defin(c, "PLANO DE ARGAND-GAUSS", "cada complexo vira um ponto", 960, 220, 700, aa * (1 - ep(t, C["05.c"], 0.4)),
          BLUE, 26)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        defin(c, "AFIXO", "o ponto do complexo", 960, 220, 700, acc, BLUE, 30)
        caixa_txt(c, "a + bi  →  (a, b)", 1310, 400, acc, 50, PURPLE, 640)
    ad = ep(t, C["05.d"], 0.5)
    projecoes(c, pl, 3, 4, BLUE, ad)
    ponto(c, pl, 3, 4, "3 + 4i", BLUE, ad)
    if ad > 0:
        X0, Y0 = pl.P(0, 0)
        X3, Y4 = pl.P(3, 4)
        pill(c, "3 para o lado", (X0 + X3) / 2, Y0 + 44, AMBER, size=22, a=ad, anchor="center")
        pill(c, "4 para cima", X3 + 18, (Y0 + Y4) / 2, AMBER, size=22, a=ad, anchor="left", bounds=(0, 1920))
        regra(c, "UM ENDEREÇO NO MAPA: (3, 4)", 1310, 600, ad, 36, PURPLE)


def b_modulo(c, t, C, B):
    head(c, t, B["start"], "O MÓDULO", "A DISTÂNCIA ATÉ A ORIGEM", BLUE)
    card(c, *CARD_R)
    pl = PL_A
    a0 = ep(t, C["06"], 0.4)
    pl.draw(c, a0, rotulos=False)
    ponto(c, pl, 3, 4, "3 + 4i", BLUE, a0)
    aa = ep(t, C["06.a"], 0.5)
    defin(c, "MÓDULO", "distância em linha reta até a origem", 960, 220, 700, aa, BLUE, 26)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        X0, Y0 = pl.P(0, 0)
        X3, Y4 = pl.P(3, 4)
        rrect(c, X0, Y4, X3 - X0, Y0 - Y4, 4, mix("#FFFFFF", AMBER, 0.12), ab)
    tri(c, pl, (0, 0), (3, 4), ab, ah=ab, cat=("3", "4"), hip="5" if ep(t, C["06.c"], 0.5) > 0.5 else "")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        caixa_expr(c, "|3 + 4i| = √{9+16} = √{25} = 5", 1310, 420, acc, 44, PURPLE, 680)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        caixa_txt(c, "z · conjugado = 9 + 16 = 25 = |z|²", 1310, 600, ad, 38, GREEN, 680)


# ======================================================================
# bloco c — as operações no plano e a distância
# ======================================================================

PL_O = Plano(600, 520, 60, -5, 5, -4, 4)


def b_operacoes(c, t, C, B):
    head(c, t, B["start"], "O QUE AS CONTAS FAZEM", "NO DESENHO", PURPLE)
    card(c, *CARD_R)
    pl = PL_O
    a0 = ep(t, C["07"], 0.4)
    pl.draw(c, a0, rotulos=False, numeros=False)
    ponto(c, pl, 3, 2, "z", BLUE, a0)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        X0, Y0 = pl.P(-5.2, 0)
        X1, _ = pl.P(5.2, 0)
        line(c, X0, Y0, X1, Y0, BLUE, aa * 0.5, 8)
        (xa, ya), (xb, yb) = pl.P(3, 2), pl.P(3, -2)
        line(c, xa, ya + 16, xb, yb - 16, BLUE, aa * 0.6, 3, dash=[8, 8])
    ponto(c, pl, 3, -2, "z", BLUE, aa, dy=30)
    zbar(c, pl, 3, -2, BLUE, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        (xa, ya), (xb, yb) = pl.P(3, 2), pl.P(-3, -2)
        line(c, xa, ya, xb, yb, RED, ab * 0.5, 3, dash=[8, 8])
    ponto(c, pl, -3, -2, "−z", RED, ab, dx=-16, dy=30, align="right")
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        (xa, ya), (xb, yb) = pl.P(3, 2), pl.P(-1, 3)
        pr = ease_io(clamp((t - C["07.c"] - 0.4) / 1.4))
        arrow(c, xa, ya, xa + (xb - xa) * pr, ya + (yb - ya) * pr, GREEN, acc, 5, 16)
    ponto(c, pl, -1, 3, "z + w", GREEN, acc * ep(t, C["07.c"] + 1.6, 0.4), dx=-16, align="right")
    itens = [("07.a", "conjugado", "reflexão no eixo real (espelho)", BLUE),
             ("07.b", "oposto −z", "giro de 180°", RED),
             ("07.c", "soma z + w", "translação: arrastar sem girar", GREEN)]
    for k, (cue, f, sb, col) in enumerate(itens):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 1020, y - 64, 640, 136, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, 1020, y - 64, 14, 136, 7, col, ak)
        ftext(c, f, 1060, y - 4, 36, "black", col, ak, align="left")
        para(c, sb, 1060, y + 40, 26, "bold", INK2, ak, 580, 32)


PL_D = Plano(270, 830, 60, 0, 9, 0, 10)


def b_distancia(c, t, C, B):
    head(c, t, B["start"], "DISTÂNCIA ENTRE DOIS PONTOS", "O MÓDULO DA DIFERENÇA", PURPLE)
    card(c, *CARD_R)
    pl = PL_D
    a0 = ep(t, C["08"], 0.4)
    pl.draw(c, a0, rotulos=False)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        regra(c, "distância = |z − w|", 1290, 260, aa, 40, PURPLE)
    ab = ep(t, C["08.b"], 0.5)
    ponto(c, pl, 2, 1, "2 + i", BLUE, ab, dx=16, dy=36)
    ponto(c, pl, 8, 9, "8 + 9i", BLUE, ab, dx=-16, dy=-14, align="right")
    acc = ep(t, C["08.c"], 0.5)
    tri(c, pl, (2, 1), (8, 9), ab, ah=acc, cat=("6", "8"), hip="10" if acc > 0.5 else "")
    if ab > 0:
        caixa_txt(c, "(8 + 9i) − (2 + i) = 6 + 8i", 1290, 430, ab, 40, BLUE, 700)
    if acc > 0:
        caixa_expr(c, "√{36+64} = √{100} = 10", 1290, 600, acc, 46, GREEN, 700)


def b_atalho_dist(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DISTÂNCIA EM DOIS PASSOS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · DISTÂNCIA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["09.a"], 0.5)
    for k, (s_, dt) in enumerate((("1 · SUBTRAIA", 0), ("2 · PITÁGORAS", 1.6))):
        ak = ep(t, C["09.a"] + dt, 0.4) * aa
        if ak > 0:
            x = 690 + k * 540
            rrect(c, x - 230, 320, 460, 130, 22, "#FFFFFF", ak, shadow=True)
            text_mid(c, s_, x, 385, 44, "black", INK, ak)
    if aa > 0:
        arrow(c, 930, 385, 990, 385, GREEN, ep(t, C["09.a"] + 1.6, 0.4), 5, 16)
    ab = ep(t, C["09.b"], 0.5)
    for k, s_ in enumerate(("3 · 4 · 5", "6 · 8 · 10")):
        ak = ep(t, C["09.b"] + 1.4 * k, 0.4) * ab
        if ak > 0:
            x = 690 + k * 540
            rrect(c, x - 230, 520, 460, 160, 22, mix("#FFFFFF", GREEN, 0.18), ak)
            text_mid(c, s_, x, 600, 60, "black", GREEN, ak)
    if ab > 0:
        text(c, "o triângulo famoso e os seus múltiplos", 960, 740, 30, "bold", INK2, ab)


# ======================================================================
# bloco d — o giro de 90° · bloco e — os giros prontos
# ======================================================================

PL_G = Plano(560, 640, 82, -3, 5, -1, 5)
ANG41 = math.degrees(math.atan2(1, 4))
R17 = math.sqrt(17)


def b_giro(c, t, C, B):
    head(c, t, B["start"], "MULTIPLICAR POR i", "O GIRO DE 90°", PURPLE)
    card(c, *CARD_R)
    pl = PL_G
    a0 = ep(t, C["10"], 0.4)
    pl.draw(c, a0, rotulos=False)
    aa = ep(t, C["10.a"], 0.5)
    defin(c, "ROTAÇÃO", "girar em volta da origem", 1000, 210, 660, aa * (1 - ep(t, C["10.b"], 0.4)), BLUE, 28)
    if aa > 0 and t < C["10.b"]:
        pill(c, "ANTI-HORÁRIO ↺ contra os ponteiros", 1330, 340, BLUE, size=26, a=aa, anchor="center")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        caixa_expr(c, "i(4+i) = 4i + i^2", 1330, 260, ab, 46, PURPLE, 640)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        caixa_expr(c, "= 4i - 1 = -1 + 4i", 1330, 410, acc, 46, GREEN, 640)
    ad = ep(t, C["10.d"], 0.5)
    pr = ease_io(clamp((t - C["10.d"] - 0.3) / 2.2))
    ponto(c, pl, 4, 1, "(4, 1)", BLUE, max(ab, ad) * (1 if ad <= 0 else 0.55), dx=16, dy=36)
    if ad > 0:
        tip = manivela(c, pl, ANG41, ANG41 + 90, R17, pr, PURPLE, ad)
        if tip:
            c.drawCircle(tip[0], tip[1], 13, paint(PURPLE, ad))
        if pr > 0.98:
            ponto(c, pl, -1, 4, "(−1, 4)", GREEN, ad, dx=-16, dy=-14, align="right")
    elif ab > 0:
        line(c, *pl.P(0, 0), *pl.P(4, 1), BLUE, ab * 0.6, 4)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        rrect(c, 1010, 520, 640, 200, 24, mix("#FFFFFF", GREEN, 0.14), ae)
        K.expr(c, "|4 + i| = √{17}", 1330, 580, 42, ae, cores=None)
        K.expr(c, "|-1 + 4i| = √{17}", 1330, 660, 42, ae, cores=None)


PL_E = Plano(560, 520, 62, -5, 5, -5, 5)


def b_giros(c, t, C, B):
    head(c, t, B["start"], "OS GIROS PRONTOS", "SEM MUDAR O MÓDULO", PURPLE)
    card(c, *CARD_R)
    pl = PL_E
    a0 = ep(t, C["11"], 0.4)
    pl.draw(c, a0, rotulos=False, numeros=False)
    ponto(c, pl, 4, 1, "4 + i", BLUE, a0, dx=14, dy=34)
    itens = [("11.a", (-1, 4), "× i", "90° anti-horário · (a, b) → (−b, a)", GREEN, (-16, -14, "right")),
             ("11.b", (-4, -1), "× (−1)", "180°", RED, (-16, 34, "right")),
             ("11.c", (1, -4), "× (−i)", "90° horário · (a, b) → (b, −a)", AMBER, (16, 34, "left"))]
    for k, (cue, (x, y), op, sb, col, (dx, dy, al)) in enumerate(itens):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        line(c, *pl.P(0, 0), *pl.P(x, y), col, ak * 0.6, 4)
        ponto(c, pl, x, y, op, col, ak, dx=dx, dy=dy, align=al)
        yy = 290 + k * 160 + d
        rrect(c, 1000, yy - 60, 660, 128, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, 1000, yy - 60, 14, 128, 7, col, ak)
        ftext(c, op, 1040, yy, 40, "black", col, ak, align="left")
        para(c, sb, 1040, yy + 40, 26, "bold", INK2, ak, 600, 32)
    if ep(t, C["11.a"], 0.5) > 0:
        line(c, *pl.P(0, 0), *pl.P(4, 1), BLUE, a0 * 0.6, 4)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        regra(c, "|i| = 1 → o módulo NÃO muda", 1330, 770, ad, 34, PURPLE)


def b_atalho_giro(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "GIRO POR i SEM CONTA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · VEZES i", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        pill(c, "1 · TROQUE AS PARTES DE LUGAR", 960, 340, GREEN, size=34, a=aa, anchor="center")
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        pill(c, "2 · MUDE O SINAL DA QUE FOI PARA A FRENTE", 960, 430, GREEN, size=34, a=ab, anchor="center")
    acc = ep(t, C["12.c"], 0.5)
    etapas = [("(4, 1)", INK, 0), ("(1, 4)", AMBER, 1.6), ("(−1, 4)", GREEN, 3.4)]
    for k, (s_, col, dt) in enumerate(etapas):
        ak = ep(t, C["12.c"] + dt, 0.4) * acc
        if ak <= 0:
            continue
        x = 560 + k * 400
        rrect(c, x - 160, 540, 320, 140, 24, "#FFFFFF", ak, shadow=True)
        text_mid(c, s_, x, 610, 56, "black", col, ak)
        if k:
            arrow(c, x - 240, 610, x - 172, 610, GREEN, ak, 5, 16)


# ======================================================================
# nós fazemos
# ======================================================================

PL_X = Plano(1270, 640, 62, -6, 3, -1, 5)


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("13", "SUA VEZ", "PAUSE E TENTE", GREEN), ("14", "VAMOS JUNTOS", "MÓDULO E GIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    ab = ep(t, C["13.b"], 0.5)
    sol = t >= C["14"]
    if aa > 0:
        cartao(c, 260, 230, 600, 200, aa)
        text(c, "1 · módulo", 560, 290, 32, "black", INK2, aa)
        K.expr(c, "|-5 + 12i| = ?", 560, 370, 50, aa, cores=None)
    if ab > 0:
        cartao(c, 260, 470, 600, 200, ab)
        text(c, "2 · giro de 90° anti-horário", 560, 530, 32, "black", INK2, ab)
        K.expr(c, "2 + 5i  →  ?", 560, 610, 50, ab, cores=None)
    if not sol:
        pause_timer(c, t, C["13.end"] - 1.9, 1290, 450)
        return
    a1 = ep(t, C["14.a"], 0.5)
    if a1 > 0:
        rrect(c, 260, 700, 600, 100, 20, mix("#FFFFFF", GREEN, 0.16), a1)
        K.expr(c, "√{25+144} = √{169} = 13", 560, 750, 40, a1, cores=None)
    pl = PL_X
    a2 = ep(t, C["14.b"], 0.5)
    pl.draw(c, a2, rotulos=False, numeros=False)
    ponto(c, pl, 2, 5, "2 + 5i", BLUE, a2, dx=14, dy=-12)
    a3 = ep(t, C["14.c"], 0.5)
    if a2 > 0:
        pr = ease_io(clamp((t - C["14.c"]) / 1.4)) if a3 > 0 else 0
        ang0 = math.degrees(math.atan2(5, 2))
        manivela(c, pl, ang0, ang0 + 90, math.sqrt(29), pr, PURPLE, a2, rot_arco="")
    if a3 > 0:
        ponto(c, pl, -5, 2, "−5 + 2i", GREEN, ep(t, C["14.c"] + 1.4, 0.4), dx=-14, dy=-16, align="right")


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Todo complexo é um ponto: real para o lado, imaginária para cima.",
          "Módulo é Pitágoras; distância é o módulo da diferença.",
          "Vezes i gira 90° anti-horário: (a, b) vira (−b, a)."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["15", "23"])
    frame(c, t, B["start"] if sid == "15" else C["23"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "15" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("|3 + 4i| = 3 + 4 = 7",
          "o robô anda 3 e anda 4: parece que é só somar",
          "o módulo é a linha reta, a diagonal: √(9 + 16) = 5."),
         ("conjugado = oposto",
          "os dois trocam sinais",
          "conjugado 3 − 4i: espelho no eixo real · oposto −3 − 4i: giro de 180°.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["16", "17"], ERROS)


# ======================================================================
# questão 4 (eu faço) e questão 5 (você faz)
# ======================================================================

ALTS4 = [("A", "=√{5}", "|1 + 2i|: a partida", RED), ("B", "5", "", GREEN),
         ("C", "7", "somou 3 + 4", RED), ("D", "=√{52}", "|4 + 6i|: a chegada", RED),
         ("E", "25", "esqueceu a raiz", RED)]
PL_Q4 = Plano(240, 760, 62, 0, 5, 0, 7)


def b_q4(c, t, C, B):
    sid = which(t, C, ["18", "19", "20"])
    heads = {"18": "DISTÂNCIA NO PLANO", "19": "EU FAÇO", "20": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "18" else C[sid], "QUESTÃO 4 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"18.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"20.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS4, 1240, 250, 440, 40, C["19.ok"], "B", cues_in, cues_x, gap=30)
    a0 = ep(t, C["18.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if sid == "18":
        if a0 > 0:
            rrect(c, 190, 250, 980, 220, 22, mix("#FFFFFF", BLUE, 0.10), a0)
            text(c, "Posições do robô em números complexos, em metros.", 680, 320, 32, "black", INK, a0)
            text(c, "Sai de 1 + 2i e vai em linha reta até 4 + 6i.", 680, 380, 36, "black", INK, a0)
        ab = ep(t, C["18.b"], 0.5)
        if ab > 0:
            text(c, "A distância percorrida, em metros, é", 680, 560, 38, "black", INK, ab)
        return
    pl = PL_Q4
    a1 = ep(t, C["19"], 0.4)
    pl.draw(c, a1, rotulos=False)
    aa = ep(t, C["19.a"], 0.5)
    ponto(c, pl, 1, 2, "1 + 2i", BLUE, aa, dx=6, dy=40, size=22)
    ponto(c, pl, 4, 6, "4 + 6i", BLUE, aa, dx=18, dy=-8, size=24)
    ab = ep(t, C["19.b"], 0.5)
    acc = ep(t, C["19.c"], 0.5)
    tri(c, pl, (1, 2), (4, 6), ab, ah=acc, cat=("3", "4"), hip="5 m" if acc > 0.5 else "", size=24)
    if ab > 0:
        caixa_txt(c, "(4 + 6i) − (1 + 2i) = 3 + 4i", 890, 330, ab, 30, BLUE, 560)
    if acc > 0:
        caixa_expr(c, "|3 + 4i| = 5", 890, 480, acc, 40, GREEN, 420)


ALTS5 = [("A", "2 − 3i", "giro horário", RED), ("B", "−3 − 2i", "giro de 180°", RED),
         ("C", "3 − 2i", "conjugado", RED), ("D", "−2 + 3i", "", GREEN),
         ("E", "2 + 3i", "espelho, sem sinal", RED)]
PL_Q5 = Plano(560, 590, 64, -4, 4, -2, 4)


def b_q5(c, t, C, B):
    sid = which(t, C, ["21", "22"])
    head(c, t, B["start"] if sid == "21" else C["22"], "QUESTÃO 5 · ESTILO ENEM",
         "VOCÊ FAZ" if sid == "21" else "VAMOS CONFERIR", GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS5, 1240, 250, 440, 40, C["22.ok"], "D", cues_in, cues_x, gap=30)
    a0 = ep(t, C["21.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if sid == "21":
        if a0 > 0:
            rrect(c, 190, 250, 980, 220, 22, mix("#FFFFFF", BLUE, 0.10), a0)
            para(c, "O programa gira 90° no sentido anti-horário multiplicando por i. O ponto 3 + 2i, após o giro, vira",
                 230, 315, 34, "black", INK, a0, 910, 46)
        pause_timer(c, t, C["21.end"] - 1.9, 680, 640)
        return
    pl = PL_Q5
    aa = ep(t, C["22.a"], 0.5)
    pl.draw(c, aa, rotulos=False, numeros=False)
    ponto(c, pl, 3, 2, "3 + 2i", BLUE, aa, dx=14, dy=34)
    pr = ease_io(clamp((t - C["22.a"] - 1.0) / 1.8))
    ang0 = math.degrees(math.atan2(2, 3))
    tip = manivela(c, pl, ang0, ang0 + 90, math.sqrt(13), pr, PURPLE, aa)
    if tip:
        c.drawCircle(tip[0], tip[1], 12, paint(PURPLE, aa))
    if pr > 0.98:
        ponto(c, pl, -2, 3, "−2 + 3i", GREEN, aa, dx=0, dy=-26, align="center")
    ab = ep(t, C["22.b"], 0.5)
    if ab > 0:
        X1, Y1 = pl.P(3.3, 0.6)
        X2, Y2 = pl.P(-3.3, 0.6)
        pill(c, "1º Q", X1, Y1, BLUE, size=22, a=ab, anchor="center")
        pill(c, "2º Q", X2, Y2, GREEN, size=22, a=ab, anchor="center")
        K.expr(c, "|z| = √{13}", 560, 290, 36, ab, cores=None)


# ======================================================================
# ponte e CTA
# ======================================================================

PL_P = Plano(500, 700, 150, 0, 2, 0, 2)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "UM NOVO ENDEREÇO", PURPLE)
    pl = PL_P
    aa = ep(t, C["24.a"], 0.5)
    pl.draw(c, aa, rotulos=False)
    if aa > 0:
        (x0, y0), (x1, _), (_, y2) = pl.P(0, 0), pl.P(1, 0), pl.P(1, 1)
        line(c, x0, y0, x1, y0, AMBER, aa, 6)
        line(c, x1, y0, x1, y2, AMBER, aa, 6)
        pill(c, "1 para o lado · 1 para cima", 1250, 300, AMBER, size=32, a=aa, anchor="center")
    ponto(c, pl, 1, 1, "1 + i", BLUE, aa)
    ab = ep(t, C["24.b"], 0.5)
    if ab > 0:
        manivela(c, pl, 0, 45, math.sqrt(2), 1.0, PURPLE, ab, rot_arco="45°")
        pill(c, "ande √2 na direção de 45°", 1250, 420, PURPLE, size=32, a=ab, anchor="center")
    acc = ep(t, C["24.c"], 0.5)
    if acc > 0:
        caixa_expr(c, "(1+i)^8 = ?", 1250, 580, acc, 60, GREEN, 520)
    ad = ep(t, C["24.d"], 0.5)
    if ad > 0:
        selo(c, 1250, 760, ad, "SAI DE CABEÇA · EP. 4", GREEN, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["25.like"], C["25.sub"], C["25.bell"], C["25.com"], C["25.bye"],
        "Você teria respondido 7 metros no gancho?", canal="no Estudativo", anki=C["25.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, galpao=b_galpao, afixo=b_afixo, modulo=b_modulo,
              operacoes=b_operacoes, distancia=b_distancia, atalho_dist=b_atalho_dist, giro=b_giro, giros=b_giros,
              atalho_giro=b_atalho_giro, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q5=b_q5,
              ponte=b_ponte, cta=b_cta)
