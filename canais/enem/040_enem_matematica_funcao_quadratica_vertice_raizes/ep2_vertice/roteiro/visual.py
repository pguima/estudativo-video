"""Visual — Função Quadrática, Episódio 2: o vértice, o eixo de simetria, o máximo ou mínimo e as trajetórias (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: Plano (eixos com grade e conversão de coordenadas, como no ep. 4 de Conceito de função),
parab() (curva de uma função com progresso e dobra em torno de um eixo), ponto(), eixo_sim() (o espelho tracejado),
bola_col() (a bola subindo e descendo numa coluna vertical), carinha() (a parábola que sorri ou fica triste), skate().
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
_s = importlib.util.spec_from_file_location("comum040", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_quadratica_ep2_vertice.mp4"
CARD_R = K.CARD_R
XV = "xᵥ = -b/2a"
YV = "yᵥ = f(xᵥ)"


def m(c, s, cx, cy, size, a=1.0, hl=None, align="center", col=None):
    """linha matemática (expr) de uma cor, com destaques por token: hl = {índice: cor}"""
    n = len(s.split())
    cores = {i: col or INK for i in range(n)}
    cores.update(hl or {})
    return K.expr(c, s, cx, cy, size, a, cores=cores, align=align)


def num(v):
    s = f"{v:g}".replace(".", ",")
    return s.replace("-", "−")


def defin(c, termo, s, y, a, w=1400, x=None, size=30):
    """faixa azul de definição: TERMO + frase"""
    if a <= 0:
        return
    x = W / 2 - w / 2 if x is None else x
    boxed(c, x, y - 50, w, 100, BLUE, a, 0.08)
    pill(c, termo, x + 24, y, BLUE, size=24, a=a)
    tw = text_w(termo, "bold", 24) + 70
    para(c, s, x + 24 + tw, y + 11, size, "bold", INK, a, w - tw - 50)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# peças do episódio
# ======================================================================

class Plano:
    """plano cartesiano num retângulo da tela: x em xr, y em yr; passo das marcas em xs, ys"""

    def __init__(self, bx, by, bw, bh, xr, yr, xs=1, ys=1):
        self.bx, self.by, self.bw, self.bh = bx, by, bw, bh
        self.xr, self.yr, self.xs, self.ys = xr, yr, xs, ys

    def P(self, x, y):
        (x0, x1), (y0, y1) = self.xr, self.yr
        return (self.bx + (x - x0) / (x1 - x0) * self.bw, self.by + self.bh - (y - y0) / (y1 - y0) * self.bh)

    def desenha(self, c, a, grade=True, nums=True, size=22, rx="x", ry="y"):
        if a <= 0:
            return
        (x0, x1), (y0, y1) = self.xr, self.yr
        xs = [k * self.xs for k in range(math.ceil(x0 / self.xs), math.floor(x1 / self.xs) + 1)]
        ys = [k * self.ys for k in range(math.ceil(y0 / self.ys), math.floor(y1 / self.ys) + 1)]
        if grade:
            for k in xs:
                px, _ = self.P(k, 0)
                line(c, px, self.by, px, self.by + self.bh, "#E7E7E2", a, 2)
            for k in ys:
                _, py = self.P(0, k)
                line(c, self.bx, py, self.bx + self.bw, py, "#E7E7E2", a, 2)
        ox, oy = self.P(0, 0)
        ox = min(max(ox, self.bx), self.bx + self.bw)
        arrow(c, self.bx - 10, oy, self.bx + self.bw + 24, oy, INK, a, 4, 16)
        arrow(c, ox, self.by + self.bh + 10, ox, self.by - 24, INK, a, 4, 16)
        text(c, rx, self.bx + self.bw + 34, oy + 10, 28, "black", INK2, a, align="left")
        text(c, ry, ox + 18, self.by - 14, 28, "black", INK2, a, align="left")
        if nums:
            for k in xs:
                if k == 0:
                    continue
                px, _ = self.P(k, 0)
                line(c, px, oy - 7, px, oy + 7, INK, a, 3)
                fmid(c, num(k), px, oy + size * 1.05, size, "bold", GRAY, a)
            for k in ys:
                if k == 0:
                    continue
                _, py = self.P(0, k)
                line(c, ox - 7, py, ox + 7, py, INK, a, 3)
                fmid(c, num(k), ox - size * 0.9, py, size, "bold", GRAY, a, align="right")


def parab(c, pl, f, x0, x1, col, a, width=7, prog_=1.0, eixo=None, dobra=0.0, so=None, n=120):
    """curva y = f(x) de x0 a x1 (até a fração prog_). Com eixo e dobra (0..1), a metade da direita gira sobre a da esquerda.
    so = 'esq' / 'dir' desenha só uma metade."""
    if a <= 0 or prog_ <= 0:
        return
    pts = []
    for k in range(int(n * prog_) + 1):
        x = x0 + (x1 - x0) * k / n
        if so == "esq" and eixo is not None and x > eixo:
            break
        if so == "dir" and eixo is not None and x < eixo:
            continue
        y = f(x)
        if eixo is not None and dobra > 0 and x > eixo:
            x = eixo + (x - eixo) * (1 - 2 * dobra)
        pts.append(pl.P(x, y))
    if len(pts) < 2:
        return
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(pl.bx - 4, pl.by - 30, pl.bw + 8, pl.bh + 34))
    p = skia.Path()
    for k, q in enumerate(pts):
        (p.moveTo if k == 0 else p.lineTo)(*q)
    c.drawPath(p, paint(col, a, stroke=width, cap_round=True))
    c.restore()


def ponto(c, pl, x, y, a, col=None, r=11, rot=None, dx=0, dy=-38, size=26, rot_col=None):
    if a <= 0:
        return
    px, py = pl.P(x, y)
    c.drawCircle(px, py, r + 4, paint("#FFFFFF", a))
    c.drawCircle(px, py, r, paint(col or INK, a))
    if rot:
        pill(c, rot, px + dx, py + dy, rot_col or col or INK, size=size, a=a, anchor="center", bounds=(0, 1920))


def eixo_sim(c, pl, x, a, col=PURPLE, rot="eixo de simetria", prog_=1.0):
    if a <= 0:
        return
    (px, py0), (_, py1) = pl.P(x, pl.yr[1]), pl.P(x, pl.yr[0])
    line(c, px, py0, px, py1, col, a, 4, dash=[14, 10], progress=prog_)
    if rot:
        text(c, rot, px + 14, py0 + 24, 22, "black", col, a, align="left")


def leitura(c, pl, x, y, a, rx=None, ry=None, size=28, cx=None, cy=None):
    """tracejados do ponto (x, y) até os eixos, com os valores lidos"""
    if a <= 0:
        return
    px, py = pl.P(x, y)
    ox, oy = pl.P(0, 0)
    line(c, px, py, px, oy, cx or BLUE, a, 4, dash=[10, 8])
    line(c, px, py, ox, py, cy or GREEN, a, 4, dash=[10, 8])
    if rx:
        pill(c, rx, px, oy + (34 if py < oy else -34), cx or BLUE, size=size, a=a, anchor="center", bounds=(0, 1920))
    if ry:
        pill(c, ry, ox - 16, py, cy or GREEN, size=size, a=a, anchor="right", bounds=(0, 1920))


def carinha(c, cx, cy, s, a, feliz=True, col=None, rotulo=True):
    """mini parábola com cara: sorri (a > 0, fundo marcado) ou triste (a < 0, topo marcado)"""
    if a <= 0:
        return
    col = col or (GREEN if feliz else RED)
    p = skia.Path()
    for k in range(41):
        u = -1 + k / 20
        y = cy - (1 if feliz else -1) * s * 0.55 * (u * u - 0.5)
        (p.moveTo if k == 0 else p.lineTo)(cx + u * s * 0.7, y)
    c.drawPath(p, paint(col, a, stroke=7, cap_round=True))
    vy = cy + (1 if feliz else -1) * s * 0.275
    c.drawCircle(cx, vy, 13, paint("#FFFFFF", a))
    c.drawCircle(cx, vy, 10, paint(col, a))
    if rotulo:
        text(c, "a > 0 · sorri" if feliz else "a < 0 · triste", cx, cy + s * 0.75, 26, "black", col, a)


def bola_col(c, x, ychao, ytopo, frac, a, col=AMBER, trilha=True):
    """a bola numa coluna vertical: frac 0 = chão, 1 = topo"""
    if a <= 0:
        return
    line(c, x - 80, ychao + 22, x + 80, ychao + 22, INK2, a, 5)
    if trilha:
        line(c, x, ychao, x, ytopo, GREEN, a * 0.55, 5, dash=[12, 10])
    y = lerp(ychao, ytopo, frac)
    c.drawCircle(x, y, 26, paint(col, a))
    c.drawCircle(x - 8, y - 8, 7, paint("#FFFFFF", a * 0.6))


def h20(t):
    return -5 * t * t + 20 * t


def f286(x):
    return 2 * x * x - 8 * x + 6


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "O VÉRTICE DA PARÁBOLA", PURPLE)
    card(c, *CARD_R)
    pl = Plano(260, 230, 760, 520, (0, 6.5), (0, 50), 1, 10)
    aa = ep(t, C["01.a"], 0.5)
    pl.desenha(c, aa, size=20, rx="t (s)", ry="h (m)")
    parab(c, pl, lambda x: -5 * x * x + 30 * x, 0, 6, PURPLE, aa, prog_=ep(t, C["01.a"] + 0.3, 1.6))
    if aa > 0:
        u = ep(t, C["01.a"] + 1.6, 0.4)
        px, py = pl.P(3, 45)
        for k in range(10):
            ang = k * 36
            line(c, px + 22 * math.cos(math.radians(ang)), py + 22 * math.sin(math.radians(ang)),
                 px + 60 * math.cos(math.radians(ang)), py + 60 * math.sin(math.radians(ang)), AMBER, u, 5)
        ponto(c, pl, 3, 45, u, AMBER)
        text(c, "explode no ponto mais alto", 1380, 280, 34, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        leitura(c, pl, 3, 45, ab * 0.9, rx="3 s", cx=AMBER, cy=GREEN)
        chip(c, "3 s", 1240, 440, AMBER, ab, 54)
        text(c, "x do vértice", 1240, 520, 28, "bold", AMBER, ab)
        selo(c, 1240, 610, ep(t, C["01.b"] + 1.4, 0.4), "ESTÁ NAS ALTERNATIVAS", AMBER, -5, 22)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        leitura(c, pl, 3, 45, acc, ry="45 m", cx=AMBER, cy=GREEN)
        chip(c, "45 m", 1560, 440, GREEN, acc, 54)
        text(c, "y do vértice", 1560, 520, 28, "bold", GREEN, acc)
        text(c, "a pergunta: ALTURA", 1560, 565, 24, "black", GREEN, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 680, 640, 110, 22, mix("#FFFFFF", RED, 0.08), ad)
        text_mid(c, "pediram o y, respondeu o x", 1400, 735, 34, "black", RED, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "achar o vértice de qualquer parábola", XV + "   ·   " + YV),
            ("02.b", "dizer se ele é máximo ou mínimo", "a > 0 → mínimo   ·   a < 0 → máximo"),
            ("02.c", "altura máxima, instante e volta ao solo", "quando → x   ·   quanto → y")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 290 + j * 190 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        m(c, sub, 360, y + 74, 34, a, align="left", col=PURPLE)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    cols = [("03.a", "SORRI OU FICA TRISTE", "episódio 1", 380), ("03.b", "SOMA DAS RAÍZES", "série de Equação do 2º grau", 960),
            ("03.c", "IMAGEM = SOMBRA", "série de Conceito de função", 1540)]
    for cue, tit, src, x in cols:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        rrect(c, x - 270, 230, 540, 560, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x, 290, 28, "black", BLUE, a)
        text(c, src, x, 332, 22, "bold", GRAY, a)
        if cue == "03.a":
            carinha(c, x - 120, 500, 200, a, True)
            carinha(c, x + 120, 500, 200, a, False)
            text(c, "raízes = toques no eixo x", x, 720, 24, "bold", INK2, a)
        elif cue == "03.b":
            m(c, "x₁ + x₂ = -b/a", x, 520, 52, a, col=PURPLE)
        else:
            line(c, x - 150, 680, x + 170, 680, INK2, a, 4)
            line(c, x - 150, 680, x - 150, 400, INK2, a, 4)
            p = skia.Path()
            for k in range(31):
                u = -1 + k / 15
                (p.moveTo if k == 0 else p.lineTo)(x + 10 + u * 130, 470 + 160 * u * u)
            c.drawPath(p, paint(BLUE, a, stroke=6, cap_round=True))
            rrect(c, x - 159, 466, 18, 166, 9, GREEN, a * 0.85)
            text(c, "a sombra na parede", x + 40, 740, 24, "bold", GREEN, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS IMAGENS DO DIA A DIA", "O MESMO PONTO ESPECIAL", BLUE)
    card(c, *CARD_R)
    xs = (420, 960, 1500)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        x = xs[0]
        rrect(c, x - 240, 220, 480, 470, 24, "#FFFFFF", aa, shadow=True)
        u = 0.5 + 0.5 * math.sin((t - C["04.a"]) * 1.6 - math.pi / 2)
        bola_col(c, x, 620, 300, 1 - (1 - u) ** 2, aa)
        text(c, "para um instante no alto", x, 650 + 80, 26, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        x = xs[1]
        rrect(c, x - 240, 220, 480, 470, 24, "#FFFFFF", ab, shadow=True)
        p = skia.Path()
        for k in range(41):
            u = -1 + k / 20
            (p.moveTo if k == 0 else p.lineTo)(x + u * 190, 600 - 300 * u * u)
        c.drawPath(p, paint(INK2, ab, stroke=14, cap_round=True))
        u = math.sin((t - C["04.b"]) * 1.3)
        sx, sy = x + u * 150, 600 - 300 * (u * 150 / 190) ** 2 - 22
        rrect(c, sx - 40, sy - 8, 80, 14, 7, AMBER, ab)
        c.drawCircle(x, 600, 11, paint(BLUE, ab))
        text(c, "o ponto mais baixo", x, 730, 26, "black", INK, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        x = xs[2]
        u = ep(t, C["04.c"] + 0.8, 1.4)
        rrect(c, x - 240, 220, 480, 470, 10, K.PAPEL, acc, shadow=True)
        line(c, x, 230, x, 680, PURPLE, acc, 3, dash=[12, 9])
        for lado in (-1, 1):
            p = skia.Path()
            for k in range(21):
                w_ = k / 20
                dxx = w_ * 180 * lado
                if lado == 1:
                    dxx *= (1 - 2 * u)
                (p.moveTo if k == 0 else p.lineTo)(x + dxx, 610 - 340 * w_ * w_)
            c.drawPath(p, paint(BLUE, acc, stroke=7, cap_round=True))
        text(c, "dobrada: as metades coincidem", x, 730, 26, "black", INK, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        for x, y in ((xs[0], 300), (xs[1], 600), (xs[2], 610)):
            c.drawCircle(x, y, 34, paint(PURPLE, ad * 0.25))
        pill(c, "VÉRTICE", W / 2, 800, PURPLE, size=34, a=ad, anchor="center")


# ======================================================================
# bloco a — vértice e eixo
# ======================================================================

def b_vertice(c, t, C, B):
    head(c, t, B["start"], "O VÉRTICE E O EIXO DE SIMETRIA", "O PONTO DA VIRADA", BLUE)
    card(c, *CARD_R)
    pl = Plano(1010, 220, 640, 560, (-0.5, 4.5), (-3, 7), 1, 1)
    a0 = ep(t, C["05"], 0.5)
    pl.desenha(c, a0, size=20)
    parab(c, pl, f286, -0.2, 4.2, BLUE, a0, prog_=ep(t, C["05"] + 0.2, 1.2))
    aa = ep(t, C["05.a"], 0.5)
    defin(c, "VÉRTICE", "onde a curva para de descer e começa a subir (ou o contrário)", 290, aa, 820, 170, 24)
    ponto(c, pl, 2, -2, aa, PURPLE, rot="vértice", dy=46)
    ab = ep(t, C["05.b"], 0.5)
    defin(c, "EIXO DE SIMETRIA", "reta vertical pelo vértice: divide a parábola em metades iguais", 470, ab, 820, 170, 24)
    eixo_sim(c, pl, 2, ab, prog_=ep(t, C["05.b"] + 0.3, 0.8))
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, 180, 590, 800, 180, 22, K.PAPEL, acc, shadow=True)
        line(c, 580, 600, 580, 760, PURPLE, acc, 3, dash=[10, 8])
        text(c, "◀  espelho  ▶", 580, 700, 40, "black", PURPLE, acc)


# ======================================================================
# bloco b — as coordenadas
# ======================================================================

def b_coord(c, t, C, B):
    head_seq(c, t, C, [("06", "AS COORDENADAS DO VÉRTICE", "SEM DESENHAR", PURPLE),
                       ("07", "AS COORDENADAS DO VÉRTICE", "TESTE: 2x² − 8x + 6", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 230, 1320, 170, PURPLE, aa, 0.10)
            text(c, "x do vértice", 480, 330, 34, "black", PURPLE, aa)
            m(c, XV, 1080, 315, 80, aa, col=PURPLE, hl={2: AMBER})
            text(c, "o menos vem ANTES", 1440, 380, 22, "black", AMBER, ep(t, C["06.a"] + 1.2, 0.4))
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            boxed(c, 300, 450, 1320, 170, GREEN, ab, 0.08)
            text(c, "y do vértice", 480, 550, 34, "black", GREEN, ab)
            m(c, "yᵥ = -Δ/4a", 1000, 535, 72, ab, col=GREEN)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            m(c, "= f(xᵥ)", 1380, 535, 62, acc, col=GREEN)
            text(c, "a altura da curva naquele x", W / 2, 720, 32, "bold", INK2, acc)
        return
    pl = Plano(1150, 240, 520, 520, (-0.5, 4.5), (-3, 7), 1, 1)
    pl.desenha(c, ep(t, C["07"], 0.5), size=20)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        m(c, "a = 2   b = -8   c = 6", 640, 250, 40, aa, hl={5: AMBER})
        m(c, "xᵥ = -(-8)/2·2 = 8/4 = 2", 640, 360, 50, ep(t, C["07.a"] + 1.0, 0.4), hl={6: PURPLE})
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        m(c, "f(2) = 8 - 16 + 6 = -2", 640, 490, 50, ab, hl={8: GREEN})
        parab(c, pl, f286, -0.2, 4.2, BLUE, ab, prog_=ep(t, C["07.b"], 1.0))
        ponto(c, pl, 2, -2, ep(t, C["07.b"] + 1.0, 0.4), PURPLE, rot="(2, −2)", dy=46)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        m(c, "Δ = 64 - 48 = 16", 470, 620, 40, acc)
        m(c, "-Δ/4a = -16/8 = -2", 860, 620, 40, acc, hl={4: GREEN})
    conferido(c, "as duas concordam", 470, 740, ep(t, C["07.ok"], 0.4), True, 36)


# ======================================================================
# bloco c — substitua
# ======================================================================

def b_substitua(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ACHE O x, DEPOIS SUBSTITUA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 180, "ATALHO · O y DO VÉRTICE", ["1º  o x do vértice      2º  f(x do vértice)"], aa, 40)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        m(c, "-Δ/4a", 620, 540, 70, ab, col=GRAY)
        strike(c, 540, 540, 700, 540, ab, AMBER, ep(t, C["08.b"] + 0.8, 0.5))
        text(c, "sem Δ, sem sinal de menos", 620, 640, 30, "black", AMBER, ab)
        m(c, "f(xᵥ)", 1300, 540, 76, ab, col=GREEN)
        text(c, "mais seguro", 1300, 640, 30, "black", GREEN, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        pill(c, "fórmula com Δ: quando o x der uma fração feia", W / 2, 760, PURPLE, size=28, a=acc, anchor="center")


# ======================================================================
# bloco d — no meio das raízes (a dobra)
# ======================================================================

def b_meio(c, t, C, B):
    head_seq(c, t, C, [("09", "O VÉRTICE MORA NO MEIO", "DAS RAÍZES", PURPLE),
                       ("10", "ATALHO", "DOIS PONTOS DE MESMA ALTURA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        pl = Plano(240, 230, 880, 560, (-0.5, 4.5), (-3, 7), 1, 1)
        a0 = ep(t, C["09"], 0.5)
        pl.desenha(c, a0, size=22)
        u = ep(t, C["09.b"], 2.0)
        aa = ep(t, C["09.a"], 0.5)
        parab(c, pl, f286, -0.2, 2, BLUE, a0, so="esq", eixo=2)
        parab(c, pl, f286, 2, 4.2, BLUE, a0 * (1 - 0.35 * u), eixo=2, dobra=u)
        ponto(c, pl, 1, 0, aa, RED, rot="1", dy=40)
        ponto(c, pl, 3 - 2 * u, 0, aa, RED, rot=("3" if u < 0.6 else None), dy=40)
        eixo_sim(c, pl, 2, ep(t, C["09.b"] - 0.2, 0.4), rot="x = 2")
        acc = ep(t, C["09.c"], 0.5)
        ponto(c, pl, 2, -2, acc, PURPLE, rot="mínimo", dy=48, rot_col=GREEN)
        if acc > 0:
            boxed(c, 1180, 300, 520, 170, PURPLE, acc, 0.10)
            m(c, "xᵥ = 1+3/2 = 2", 1440, 385, 50, acc, col=PURPLE)
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            m(c, "-b/a = soma", 1440, 560, 44, ad)
            m(c, "-b/2a = média", 1440, 660, 44, ad, col=PURPLE)
        return
    pl = Plano(240, 230, 820, 560, (-0.5, 6.5), (-4, 7), 1, 1)
    g = lambda x: x * x - 6 * x + 5
    a0 = ep(t, C["10"], 0.5)
    pl.desenha(c, a0, size=22)
    parab(c, pl, g, -0.3, 6.3, BLUE, a0, prog_=ep(t, C["10"], 1.0))
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 1120, 240, 600, 170, "ATALHO", ["mesma altura → eixo no meio"], aa, 30)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        m(c, "x^2 - 6x + 5", 1420, 480, 40, ab)
        ponto(c, pl, 0, 5, ab, AMBER, rot="f(0) = 5", dx=80, dy=0)
        ponto(c, pl, 6, 5, ab, AMBER, rot="f(6) = 5", dx=-80, dy=0)
        p0, p6 = pl.P(0, 5), pl.P(6, 5)
        line(c, p0[0], p0[1], p6[0], p6[1], AMBER, ab, 4, dash=[10, 8])
    acc = ep(t, C["10.c"], 0.5)
    eixo_sim(c, pl, 3, acc, rot="x = 3", prog_=ep(t, C["10.c"], 0.8))
    if acc > 0:
        m(c, "0+6/2 = 3", 1420, 620, 50, acc, col=PURPLE)


# ======================================================================
# bloco e — máximo ou mínimo
# ======================================================================

def b_maxmin(c, t, C, B):
    head_seq(c, t, C, [("11", "MÍNIMO OU MÁXIMO?", "DEPENDE DO a", BLUE), ("12", "E A IMAGEM?", "A SOMBRA NA PAREDE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 220, 640, 400, 24, mix("#FFFFFF", GREEN, 0.06), aa)
            carinha(c, 580, 420, 260, aa, True)
            pill(c, "PONTO DE MÍNIMO · o fundo", 580, 290, GREEN, size=26, a=aa, anchor="center")
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            rrect(c, 1020, 220, 640, 400, 24, mix("#FFFFFF", RED, 0.06), ab)
            carinha(c, 1340, 420, 260, ab, False)
            pill(c, "PONTO DE MÁXIMO · o topo", 1340, 290, RED, size=26, a=ab, anchor="center")
        defin(c, "VALOR MÍNIMO / MÁXIMO", "o yᵥ: o menor (ou o maior) resultado da função", 720, ep(t, C["11.c"], 0.5), 1400)
        return
    pl = Plano(260, 230, 700, 560, (-0.5, 4.5), (-3, 7), 1, 1)
    a0 = ep(t, C["12"], 0.5)
    pl.desenha(c, a0, size=22)
    parab(c, pl, f286, -0.2, 4.2, BLUE, a0)
    aa = ep(t, C["12.a"], 0.5)
    ponto(c, pl, 2, -2, aa, GREEN, rot="mínimo (2, −2)", dy=48)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        u = ep(t, C["12.b"], 1.2)
        ox, py0 = pl.P(0, -2)
        _, py1 = pl.P(0, 7)
        rrect(c, ox - 9, lerp(py0, py1, u), 18, (py0 - lerp(py0, py1, u)) + 4, 9, GREEN, ab * 0.85)
        c.drawCircle(ox, py0, 13, paint(GREEN, ab))
        boxed(c, 1060, 260, 620, 150, GREEN, ab, 0.08)
        text(c, "IMAGEM", 1370, 310, 26, "black", GREEN, ab)
        m(c, "[ -2, +∞ [", 1370, 365, 50, ab, col=GREEN)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        p1, p2, p3 = pl.P(0.6, f286(0.6)), pl.P(1.6, f286(1.6)), pl.P(3.4, f286(3.4))
        arrow(c, p1[0] - 50, p1[1] - 40, p2[0] - 40, p2[1] + 10, RED, acc, 5, 16)
        arrow(c, pl.P(2.4, 0)[0] + 40, pl.P(2.4, f286(2.4))[1] + 10, p3[0] + 50, p3[1] - 40, GREEN, acc, 5, 16)
        text(c, "desce até x = 2, depois sobe", 1370, 500, 30, "black", INK, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        boxed(c, 1060, 570, 620, 190, RED, ad, 0.06)
        text(c, "a < 0: tudo se inverte", 1370, 625, 28, "black", RED, ad)
        m(c, "] -∞, yᵥ ]", 1370, 690, 40, ad, col=RED)
        text(c, "sobe, depois desce", 1370, 745, 24, "bold", INK2, ad)


# ======================================================================
# bloco f — trajetórias (tela dividida) e bloco g — gráfico × caminho
# ======================================================================

def _tela_dividida(c, t, frac_t, a, pl, marcas=()):
    """à esquerda a bola numa coluna; à direita o gráfico h × t desenhado até o instante frac_t (0..4 s)"""
    if a <= 0:
        return
    rrect(c, 180, 200, 420, 610, 24, "#FFFFFF", a, shadow=True)
    text(c, "a bola no espaço", 390, 250, 26, "black", INK2, a)
    bola_col(c, 390, 740, 300, h20(frac_t) / 20, a)
    pl.desenha(c, a, size=20, rx="t (s)", ry="h (m)")
    parab(c, pl, h20, 0, 4, PURPLE, a, prog_=frac_t / 4)
    px, py = pl.P(frac_t, h20(frac_t))
    c.drawCircle(px, py, 12, paint(AMBER, a))
    yb = lerp(740, 300, h20(frac_t) / 20)
    line(c, 420, yb, px - 16, py, AMBER, a * 0.35, 3, dash=[8, 8])


def b_trajeto(c, t, C, B):
    head_seq(c, t, C, [("13", "A BOLA LANÇADA PARA CIMA", "h(t) = −5t² + 20t", PURPLE),
                       ("14", "A VOLTA AO CHÃO", "SOBE EM 2, DESCE EM 2", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    pl = Plano(760, 260, 640, 470, (0, 4.6), (0, 24), 1, 5)
    a0 = ep(t, C["13"], 0.5)
    if sid == "13":
        u = ep(t, C["13.c"], 2.0)
        _tela_dividida(c, t, 2 * u, a0, pl)
        ab = ep(t, C["13.b"], 0.5)
        pill(c, "a = −5 < 0 → máximo", 1420, 220, RED, size=24, a=ab, anchor="center")
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            m(c, "tᵥ = -20/-10 = 2 s", 1580, 330, 34, acc, col=AMBER)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            leitura(c, pl, 2, 20, ad, rx="2 s", ry="20 m", cx=AMBER, cy=GREEN, size=24)
            m(c, "h(2) = -20 + 40 = 20 m", 1580, 420, 30, ad, col=GREEN)
        return
    u = ep(t, C["14.a"], 2.0)
    _tela_dividida(c, t, 2 + 2 * u, 1.0, pl)
    ponto(c, pl, 2, 20, 1.0, PURPLE, rot="(2 s, 20 m)", dy=-36, size=22)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        m(c, "-5t(t-4) = 0", 1600, 330, 34, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        ponto(c, pl, 0, 0, ab, GRAY, rot="lançamento", dx=40, dy=-40, size=20)
        ponto(c, pl, 4, 0, ab, RED, rot="volta: 4 s", dx=0, dy=-40, size=20)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        ponto(c, pl, 1, 15, acc, BLUE)
        ponto(c, pl, 3, 15, acc, BLUE)
        p1, p3 = pl.P(1, 15), pl.P(3, 15)
        line(c, p1[0], p1[1], p3[0], p3[1], BLUE, acc, 4, dash=[10, 8])
        eixo_sim(c, pl, 2, acc, rot=None)
        text(c, "15 m: 1 s e 3 s", 1600, 430, 28, "black", BLUE, acc)
        text(c, "1 s de cada lado", 1600, 475, 24, "bold", INK2, acc)
        pill(c, "você já resolveu isso", 1600, 540, GRAY, size=20, a=acc, anchor="center")


def b_caminho(c, t, C, B):
    head(c, t, B["start"], "GRÁFICO × CAMINHO", "A BOLA FAZ CURVA NO AR?", AMBER)
    card(c, *CARD_R)
    pl = Plano(760, 260, 640, 470, (0, 4.6), (0, 24), 1, 5)
    a0 = ep(t, C["15"], 0.5)
    ciclo = ((t - C["15"]) % 4.0)
    _tela_dividida(c, t, ciclo, a0, pl)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        pill(c, "caminho: RETA", 390, 790, GREEN, size=24, a=aa, anchor="center")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        pill(c, "parábola: o DESENHO h × t", 1080, 220, PURPLE, size=24, a=ab, anchor="center")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        boxed(c, 1450, 300, 300, 200, BLUE, acc, 0.08)
        text(c, "TRAJETÓRIA", 1600, 350, 24, "black", BLUE, acc)
        para(c, "o caminho no espaço: aqui, a reta", 1470, 400, 22, "bold", INK, acc, 260)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        boxed(c, 1450, 540, 300, 230, GRAY, ad, 0.06)
        p = skia.Path()
        for k in range(21):
            u = k / 20
            (p.moveTo if k == 0 else p.lineTo)(1480 + 240 * u, 720 - 600 * u * (1 - u))
        c.drawPath(p, paint(BLUE, ad, stroke=5, cap_round=True))
        text(c, "oblíquo: Física", 1600, 760, 22, "black", GRAY, ad)


def b_pergunta(c, t, C, B):
    head(c, t, B["start"], "ATALHO DE PROVA", "SUBLINHE A PERGUNTA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["16"], 0.5)
    K.atalho(c, 260, 210, 1400, 120, "ATALHO · SUBLINHE A PERGUNTA", [""], a0, 30)
    cols = [("16.a", "QUANDO? ONDE?", "x do vértice", "instante · peças · posição", BLUE, 560),
            ("16.b", "QUANTO?", "y do vértice", "altura · custo · lucro", GREEN, 1360)]
    for cue, q, r, ex, col, x in cols:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        boxed(c, x - 330, 370, 660, 280, col, a, 0.08)
        text(c, q, x, 450, 50, "black", col, a)
        line(c, x - 200, 470, x + 200, 470, col, a, 6)
        text(c, "→ " + r, x, 545, 40, "black", INK, a)
        text(c, ex, x, 610, 26, "bold", INK2, a)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        chip(c, "quando: 2 s", 560, 740, BLUE, acc, 38)
        chip(c, "quanto: 20 m", 1360, 740, GREEN, acc, 38)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "VÉRTICE · MÍNIMO · IMAGEM", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        rrect(c, 320, 200, 1280, 120, 24, "#F7F7F5", aa)
        m(c, "f(x) = x^2 - 4x + 3", W / 2, 260, 60, aa)
        if t < C["18"]:
            for k, s in enumerate(("vértice?", "máximo ou mínimo?", "imagem?")):
                chip(c, s, 520 + k * 440, 430, BLUE, ep(t, C["17.a"] + 1.0 + 0.6 * k, 0.4), 34)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 620)
    if t < C["18"]:
        return
    pl = Plano(1180, 380, 480, 400, (-0.5, 4.5), (-2, 4), 1, 1)
    pl.desenha(c, 1.0, size=18)
    parab(c, pl, lambda x: x * x - 4 * x + 3, -0.2, 4.2, BLUE, 1.0, prog_=ep(t, C["18"], 1.0))
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        m(c, "xᵥ = 4/2 = 2", 640, 420, 50, aa, hl={4: PURPLE})
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        m(c, "f(2) = 4 - 8 + 3 = -1", 640, 530, 48, ab, hl={8: GREEN})
        ponto(c, pl, 2, -1, ab, GREEN, rot="(2, −1)", dy=44, size=22)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        text(c, "a > 0 → MÍNIMO", 640, 650, 40, "black", GREEN, acc)
        m(c, "Im = [ -1, +∞ [", 640, 730, 44, acc, col=GREEN)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        ponto(c, pl, 1, 0, ad, RED, r=9)
        ponto(c, pl, 3, 0, ad, RED, r=9)
        m(c, "1+3/2 = 2", 1420, 300, 36, ad)
        conferido(c, "bateu", 1340, 820, ep(t, C["18.ok"], 0.4), True, 28)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["xᵥ = −b sobre 2a; o yᵥ é f(xᵥ).",
          "O vértice fica no meio das raízes.",
          "x do vértice: onde ou quando. y do vértice: quanto."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("xᵥ = b/2a (sem o menos) → −2", "o menos é pequeno e some na pressa",
          "escreva o menos ANTES do número: −(−8)/4 = 2 · sem ele, o vértice sai espelhado"),
         ("xᵥ = −b/a → 4", "é a fórmula da série passada (soma das raízes)",
          "4 é a SOMA (1 + 3); o vértice é a MÉDIA: metade, 2"),
         ("pediram o máximo, respondeu 2 s", "o 2 sai primeiro e está nas alternativas",
          "instante não é altura: topo em 2 s, altura máxima de 20 m"),
         ("a > 0 tem máximo", "positivo soa como topo",
          "a > 0 sorri, e sorriso tem fundo: o vértice é MÍNIMO"),
         ("o gráfico h × t é o caminho da bola", "o desenho lembra um arremesso",
          "o eixo horizontal é o TEMPO · no lançamento vertical, o caminho é uma reta")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22", "23", "24"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y=230, size=26, w=700, x=190):
    if a <= 0:
        return y
    for ln in K.wrap(s, "black", size, w):
        ftext(c, ln, x, y, size, "black", INK, a, align="left")
        y += size * 1.45
    return y


def _painel(c, t, y0, a):
    if a > 0:
        rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ENUN1 = ("Em uma demonstração de fogos, um artefato é lançado verticalmente a partir do solo, e sua altura, em metros, é "
         "dada por h(t) = −5t² + 30t, em que t é o tempo em segundos após o lançamento. O artefato explode no ponto mais "
         "alto da trajetória. A altura da explosão, em metros, é")
ALTS1 = [("A", "3", "é o instante (o x)", RED), ("B", "45", "", GREEN), ("C", "90", "só 30 · 3", RED),
         ("D", "135", "sinal trocado: 45 + 90", RED), ("E", "180", "volta ao solo: 30 · 6", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "ALTURA MÁXIMA DE UM LANÇAMENTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, ENUN1, a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 260, 680, 40, C["26.ok"], "B", cues_in, cues_x, gap=34)
    if t < C["26"]:
        return
    y0 = yend + 10
    _painel(c, t, y0, ep(t, C["26"], 0.4))
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        text(c, "pedem a ALTURA → y do vértice", 540, y0 + 50, 28, "black", GREEN, aa)
    ab = ep(t, C["26.b"], 0.4)
    if ab > 0:
        m(c, "tᵥ = -30/-10 = 3 s", 540, y0 + 110, 36, ab, hl={4: AMBER, 5: AMBER})
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        m(c, "h(3) = -45 + 90 = 45 m", 540, y0 + 180, 36, acc, hl={6: GREEN, 7: GREEN})
    ad = ep(t, C["26.d"], 0.4)
    if ad > 0:
        text(c, "volta em 6 s · 3 é o meio de 0 e 6", 540, y0 + 250, 24, "bold", INK2, ad)


ENUN8 = ("O custo diário de produção de uma oficina, em reais, é C(x) = 2x² − 120x + 5 000, em que x é o número de peças "
         "produzidas no dia. A quantidade de peças que torna o custo mínimo e o valor desse custo são, respectivamente,")
ALTS8 = [("A", "30 peças e R$ 3 200,00", "", GREEN), ("B", "60 peças e R$ 5 000,00", "usou −b/a", RED),
         ("C", "30 peças e R$ 10 400,00", "somou 120 · 30", RED), ("D", "15 peças e R$ 3 650,00", "dividiu por 4a", RED),
         ("E", "30 peças e R$ 5 000,00", "custo de zero peças", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · NÓS FAZEMOS", "CUSTO MÍNIMO DE PRODUÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, ENUN8, a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["29"], 0.3)),
         align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS8, 1000, 250, 700, 32, C["29.ok"], "A", cues_in, cues_x, gap=30)
    if t < C["29"]:
        pause_timer(c, t, C["28.p"] + 0.1, 540, yend + 140)
        return
    y0 = yend + 10
    _painel(c, t, y0, ep(t, C["29"], 0.4))
    aa = ep(t, C["29.a"], 0.4)
    if aa > 0:
        text(c, "pedem o x E o y · a = 2 > 0 → mínimo", 540, y0 + 50, 26, "black", GREEN, aa)
    ab = ep(t, C["29.b"], 0.4)
    if ab > 0:
        m(c, "xᵥ = 120/4 = 30", 540, y0 + 115, 38, ab, hl={4: PURPLE})
    acc = ep(t, C["29.c"], 0.4)
    if acc > 0:
        m(c, "2·900 - 3600 + 5000", 540, y0 + 195, 34, acc)
        m(c, "= 3200", 540, y0 + 260, 40, ep(t, C["29.c"] + 2.0, 0.4), col=GREEN)


ENUN9 = ("Num parque aquático, a trajetória do salto de um golfinho, fora da água, é descrita por y = −0,5(x − 4)² + 2, "
         "em que x é a distância horizontal, em metros, a partir de um marco na borda do tanque e y é a altura acima da "
         "superfície da água, em metros. A distância horizontal entre o ponto em que o golfinho sai da água e o ponto em "
         "que volta a ela é")
ALTS9 = [("A", "2 m", "altura máxima (yᵥ)", RED), ("B", "2√2 m", "ignorou o 0,5", RED), ("C", "4 m", "", GREEN),
         ("D", "6 m", "ponto de volta, do marco", RED), ("E", "8 m", "dobrou o 4", RED)]


def b_q9(c, t, C, B):
    head_seq(c, t, C, [("30", "QUESTÃO 9 · VOCÊ FAZ", "A DISTÂNCIA DE UM SALTO", BLUE),
                       ("31", "QUESTÃO 9 · CONFIRA", "ALTURA ZERO NA ÁGUA", BLUE),
                       ("32", "QUESTÃO 9 · AS ERRADAS", "QUEM CAIU EM QUÊ", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    yend = _enunciado(c, ENUN9, a0, size=24)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["31"], 0.3)),
         align="left")
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS9, 1000, 260, 680, 40, C["31.ok"], "C", cues_in, cues_x, gap=34)
    if t < C["31"]:
        pause_timer(c, t, C["30.p"] + 0.1, 540, yend + 120)
        return
    y0 = yend + 10
    _painel(c, t, y0, ep(t, C["31"], 0.4))
    aa = ep(t, C["31.a"], 0.4)
    if aa > 0:
        text(c, "na água: y = 0", 540, y0 + 45, 28, "black", BLUE, aa)
    ab = ep(t, C["31.b"], 0.4)
    if ab > 0:
        m(c, "0,5(x-4)^2 = 2  →  (x-4)^2 = 4", 540, y0 + 105, 30, ab)
    acc = ep(t, C["31.c"], 0.4)
    if acc > 0:
        m(c, "x - 4 = ±2  →  x = 2  ou  x = 6", 540, y0 + 170, 30, acc, hl={8: GREEN, 12: GREEN})
    ad = ep(t, C["31.d"], 0.4)
    if ad > 0:
        m(c, "6 - 2 = 4 m", 540, y0 + 235, 38, ad, col=GREEN)
    ae = ep(t, C["31.e"], 0.4)
    if ae > 0:
        text(c, "vértice em x = 4: 2 m para cada lado", 540, y0 + 290, 22, "bold", PURPLE, ae)
    af = ep(t, C["32.f"], 0.4)
    if af > 0:
        pill(c, "por que essa forma entrega o vértice? · ep. 4", 540, 800, PURPLE, size=20, a=af, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "OTIMIZAÇÃO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        rrect(c, 520, 300, 880, 40, 6, "#B9A88E", aa)
        for k in range(12):
            line(c, 540 + k * 74, 300, 520 + k * 74, 340, "#8E7D63", aa, 3)
        text(c, "MURO", W / 2, 290, 26, "black", INK2, aa)
        line(c, 700, 340, 700, 620, GREEN, aa, 6, dash=[14, 8])
        line(c, 700, 620, 1220, 620, GREEN, aa, 6, dash=[14, 8])
        line(c, 1220, 620, 1220, 340, GREEN, aa, 6, dash=[14, 8])
        text(c, "60 m de tela", 960, 680, 34, "black", GREEN, aa)
        text_mid(c, "maior horta?", 960, 480, 44, "black", INK, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        selo(c, 1480, 470, ab, "QUADRADO? PERDE", RED, -6, 30)
    pill(c, "ep. 3 · otimização", W / 2, 780, PURPLE, size=32, a=ep(t, C["34.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Você já respondeu o x quando pediam o y?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, vertice=b_vertice, coord=b_coord,
              substitua=b_substitua, meio=b_meio, maxmin=b_maxmin, trajeto=b_trajeto, caminho=b_caminho,
              pergunta=b_pergunta, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q8=b_q8, q9=b_q9,
              ponte=b_ponte, cta=b_cta)
