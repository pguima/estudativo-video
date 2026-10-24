"""Visual — Função Quadrática, Episódio 4: três formas da mesma função (geral, fatorada, canônica) e estudo do sinal (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: Graf (eixos com x e y negativos, curva amostrada, curva pintada pelo sinal: verde acima do eixo,
vermelho abaixo, e a faixa colorida no eixo x com os "+" e "−"), arco() (o arco da ponte sobre a água), cracha() (as três
"fotos" da mesma parábola), carinha() (parábola sorrindo/triste em miniatura), linha() (texto com cor por trecho).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/positivo · vermelho = erro/negativo.
"""
import importlib.util
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
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_quadratica_ep4_formas_sinal.mp4"
CARD_R = K.CARD_R
TEAL = "#0F8B8D"
AGUA = "#7FB7E6"


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


class Graf:
    """gráfico num retângulo de pixels (x0, y0 = canto superior esquerdo) para a janela [xmin, xmax] × [ymin, ymax]"""

    def __init__(self, x0, y0, w, h, xmin, xmax, ymin, ymax):
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def P(self, x, y):
        return (self.x0 + self.w * (x - self.xmin) / (self.xmax - self.xmin),
                self.y0 + self.h * (self.ymax - y) / (self.ymax - self.ymin))

    def eixos(self, c, a, ticks_x=(), ticks_y=(), rx="x", ry="y", sw=4, size=26):
        if a <= 0:
            return
        _, y0 = self.P(0, 0)
        x0, _ = self.P(0, 0)
        line(c, self.x0 - 10, y0, self.x0 + self.w + 20, y0, INK2, a, sw)
        arrow(c, self.x0 + self.w, y0, self.x0 + self.w + 34, y0, INK2, a, sw, 14)
        if self.xmin <= 0 <= self.xmax:
            line(c, x0, self.y0 + self.h + 10, x0, self.y0 - 10, INK2, a, sw)
            arrow(c, x0, self.y0, x0, self.y0 - 34, INK2, a, sw, 14)
            text(c, ry, x0 + 14, self.y0 - 14, size, "bold", INK2, a, align="left")
        text(c, rx, self.x0 + self.w + 30, y0 + 44, size, "bold", INK2, a, align="right")
        for v, s_ in ticks_x:
            px, _ = self.P(v, 0)
            line(c, px, y0 - 8, px, y0 + 8, INK2, a, 3)
            ftext(c, s_, px, y0 + 40, size, "bold", INK2, a)
        for v, s_ in ticks_y:
            _, py = self.P(0, v)
            line(c, x0 - 8, py, x0 + 8, py, INK2, a, 3)
            ftext(c, s_, x0 - 14, py + 9, size - 2, "bold", INK2, a, align="right")

    def _pts(self, f, xa, xb, n=140):
        return [(xa + (xb - xa) * k / n, f(xa + (xb - xa) * k / n)) for k in range(n + 1)]

    def curva(self, c, f, a, col=None, prog_=1.0, sw=7, sinal=False, xa=None, xb=None):
        """sinal=True: cada trecho fica verde (f > 0) ou vermelho (f < 0)"""
        if a <= 0 or prog_ <= 0:
            return
        xa = self.xmin if xa is None else xa
        xb = self.xmax if xb is None else xb
        xb = xa + (xb - xa) * prog_
        pts = self._pts(f, xa, xb)
        if not sinal:
            p = skia.Path()
            p.moveTo(*self.P(*pts[0]))
            for q in pts[1:]:
                p.lineTo(*self.P(*q))
            c.save(); c.clipRect(skia.Rect.MakeXYWH(self.x0 - 40, self.y0 - 40, self.w + 80, self.h + 80))
            c.drawPath(p, paint(col or BLUE, a, stroke=sw, cap_round=True))
            c.restore()
            return
        c.save(); c.clipRect(skia.Rect.MakeXYWH(self.x0 - 40, self.y0 - 40, self.w + 80, self.h + 80))
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            colk = GREEN if (y1 + y2) / 2 > 0 else RED
            p1, p2 = self.P(x1, y1), self.P(x2, y2)
            line(c, p1[0], p1[1], p2[0], p2[1], colk, a, sw)
        c.restore()

    def pinta(self, c, f, a, xa=None, xb=None, alpha=0.22):
        """pinta a região entre a curva e o eixo x: verde acima, vermelho abaixo"""
        if a <= 0:
            return
        xa = self.xmin if xa is None else xa
        xb = self.xmax if xb is None else xb
        c.save(); c.clipRect(skia.Rect.MakeXYWH(self.x0, self.y0, self.w, self.h))
        for (x1, y1), (x2, y2) in zip(self._pts(f, xa, xb, 200), self._pts(f, xa, xb, 200)[1:]):
            colk = GREEN if (y1 + y2) / 2 > 0 else RED
            p = skia.Path()
            p.moveTo(*self.P(x1, 0)); p.lineTo(*self.P(x1, y1)); p.lineTo(*self.P(x2, y2)); p.lineTo(*self.P(x2, 0))
            p.close()
            c.drawPath(p, paint(colk, a * alpha))
        c.restore()

    def faixa_sinal(self, c, cortes, sinais, a, rotulos=True, size=56, alfas=None):
        """barra colorida sobre o eixo x entre os cortes; sinais = '+', '−' ou '0' para cada trecho"""
        if a <= 0:
            return
        _, y0 = self.P(0, 0)
        xs = [self.xmin] + list(cortes) + [self.xmax]
        for k, s_ in enumerate(sinais):
            ak = a * (alfas or {}).get(k, 1.0)
            if ak <= 0:
                continue
            col = GREEN if s_ == "+" else RED
            pa, pb = self.P(xs[k], 0)[0], self.P(xs[k + 1], 0)[0]
            rrect(c, pa, y0 - 9, pb - pa, 18, 9, col, ak * 0.85)
            if rotulos:
                text_mid(c, s_, (pa + pb) / 2, y0 + 62, size, "black", col, ak)

    def ponto(self, c, x, y, a, col=None, r=13, vazio=False):
        if a <= 0:
            return
        px, py = self.P(x, y)
        if vazio:
            c.drawCircle(px, py, r, paint("#FFFFFF", a))
            c.drawCircle(px, py, r, paint(col or INK, a, stroke=5))
        else:
            c.drawCircle(px, py, r, paint(col or INK, a))
            c.drawCircle(px, py, r, paint("#FFFFFF", a, stroke=3))


def agua(c, x, y, w, h, a):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 10, AGUA, a * 0.55)
    for k in range(int(w // 90)):
        xx = x + 30 + k * 90
        p = skia.Path()
        p.moveTo(xx, y + 22); p.quadTo(xx + 15, y + 12, xx + 30, y + 22); p.quadTo(xx + 45, y + 32, xx + 60, y + 22)
        c.drawPath(p, paint("#FFFFFF", a * 0.8, stroke=3, cap_round=True))


def arco(c, g, a, prog_=1.0, sw=9):
    """o arco da ponte: f(x) = −x(x − 40)/40, pés em 0 e 40, topo (20, 10), sobre a água"""
    if a <= 0:
        return
    pa, pb = g.P(-4, 0), g.P(44, 0)
    agua(c, pa[0], pa[1], pb[0] - pa[0], 70, a)
    f = lambda x: -x * (x - 40) / 40
    g.curva(c, f, a, "#5A6372", prog_, sw, xa=0, xb=40)
    # tabuleiro da ponte
    yt = g.P(0, 11.2)[1]
    if prog_ >= 1:
        rrect(c, g.P(-3, 0)[0], yt - 10, g.P(43, 0)[0] - g.P(-3, 0)[0], 20, 6, "#5A6372", a)
        for xx in range(4, 40, 4):
            px, py = g.P(xx, f(xx))
            line(c, px, yt, px, py, "#8B93A1", a, 3)


def carinha(c, cx, cy, s, a, triste=False, col=None):
    """parábola miniatura (sorrindo ou triste) com o eixo x passando pelas raízes"""
    if a <= 0:
        return
    sg = -1 if triste else 1
    line(c, cx - s * 1.1, cy, cx + s * 1.1, cy, INK2, a, 3)
    pts = [(-1.0 + 2.0 * k / 60) for k in range(61)]
    for u1, u2 in zip(pts, pts[1:]):
        v1, v2 = sg * (u1 * u1 - 0.55), sg * (u2 * u2 - 0.55)
        colk = col or (GREEN if (v1 + v2) / 2 > 0 else RED)
        line(c, cx + u1 * s, cy - v1 * s * 0.9, cx + u2 * s, cy - v2 * s * 0.9, colk, a, 6)


def camera(c, cx, cy, s, col, a):
    """ícone de câmera fotográfica"""
    if a <= 0:
        return
    rrect(c, cx - s * 0.6, cy - s * 0.32, s * 1.2, s * 0.72, s * 0.14, col, a)
    rrect(c, cx - s * 0.22, cy - s * 0.46, s * 0.44, s * 0.2, s * 0.06, col, a)
    c.drawCircle(cx, cy + s * 0.04, s * 0.24, paint("#FFFFFF", a))
    c.drawCircle(cx, cy + s * 0.04, s * 0.15, paint(col, a))


def cracha(c, x, y, w, h, tit, lei, mostra, col, a, foco=1.0):
    """um "crachá" (foto) da mesma parábola: título, lei e o que ela mostra; foco < 1 apaga"""
    if a <= 0:
        return
    af = a * (0.35 + 0.65 * foco)
    rrect(c, x, y, w, h, 22, "#FFFFFF", af, shadow=foco > 0.5)
    rrect(c, x, y, w, 52, 22, col, af * 0.18)
    if foco > 0.5:
        rrect(c, x - 4, y - 4, w + 8, h + 8, 26, None, af, stroke=5, stroke_color=col)
    text(c, tit, x + w / 2, y + 36, 22, "black", col, af, tracking=2)
    ftext(c, lei, x + w / 2, y + 100, 40, "black", INK, af)
    text(c, mostra, x + w / 2, y + h - 14, 24, "bold", INK2, af)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO QUADRÁTICA · EPISÓDIO 4", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        linha(c, [("x² > 4x", INK)], 520, 300, 96, aa)
        a2 = ep(t, C["01.a"] + 2.6, 0.4)
        pill(c, "dividiu os dois lados por x", 520, 410, AMBER, size=28, a=a2, anchor="center")
        a3 = ep(t, C["01.a"] + 4.0, 0.4)
        linha(c, [("x > 4 ?", AMBER)], 520, 520, 84, a3)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 220, 640, 330, 26, "#FFFFFF", ab, shadow=True)
        text(c, "TESTE  x = −1", 1320, 290, 34, "black", INK2, ab, tracking=2)
        linha(c, [("(−1)² > 4·(−1)", INK)], 1320, 380, 50, ab)
        linha(c, [("1 > −4", GREEN)], 1320, 470, 60, ep(t, C["01.b"] + 2.2, 0.4))
        selo(c, 1500, 530, ep(t, C["01.b"] + 3.4, 0.4), "VERDADE!", GREEN, -5, 34)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        cy, x0, x1 = 660, 260, 1660
        line(c, x0, cy, x1, cy, INK2, acc, 4)
        zx, qx = 760, 1160
        pisca = 0.55 + 0.45 * abs(((t - C["01.c"]) * 1.6) % 2 - 1)
        rrect(c, x0, cy - 12, zx - x0, 24, 12, RED, acc * pisca)
        rrect(c, qx, cy - 12, x1 - qx, 24, 12, GREEN, acc * 0.9)
        for px, s_ in ((zx, "0"), (qx, "4")):
            c.drawCircle(px, cy, 16, paint("#FFFFFF", acc)); c.drawCircle(px, cy, 16, paint(INK, acc, stroke=5))
            ftext(c, s_, px, cy + 60, 40, "black", INK, acc)
        selo(c, 510, 590, acc, "A DIVISÃO APAGOU ISTO", RED, -4, 30)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "O JEITO QUE NÃO PERDE NADA", W / 2, 810, ad, 38, GREEN)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO QUADRÁTICA · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de FUNÇÃO QUADRÁTICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "A LEI", "a partir do gráfico", BLUE), ("02.b", "+ OU −", "para quais x", PURPLE),
             ("02.c", "O SENTIDO", "sem errar o < e o >", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 44, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "série de Equação do 2º grau", [("a(x − x₁)(x − x₂)", PURPLE), ("   ·   raízes por SOMA e PRODUTO", INK)]),
             ("03.b", "série de Expressões algébricas", [("(x − 2)² = ", INK), ("x² − 4x + 4", PURPLE)]),
             ("03.c", "série de Função afim", [("estudar o sinal: onde dá ", INK), ("+", GREEN), (" e onde dá ", INK),
                                              ("−", RED)])]
    for k, (cue, serie, partes) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, serie, 300, y - 70, BLUE, size=22, a=a)
        linha(c, partes, 960, y + 10, 46, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA PONTE E UMA FÁBRICA", "DUAS PARÁBOLAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    g = Graf(220, 330, 700, 330, -4, 44, 0, 12)
    arco(c, g, aa, ep(t, C["04.a"], 1.2))
    if aa > 0:
        text(c, "pés na água · topo no meio", 570, 250, 30, "black", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        g2 = Graf(1080, 260, 560, 420, 0, 14, -10, 12)
        L = lambda x: -(x - 4) * (x - 10)
        g2.eixos(c, ab, rx="x", ry="lucro")
        g2.pinta(c, L, ab * ep(t, C["04.b"] + 1.5, 0.6), 0, 14)
        g2.curva(c, L, ab, sinal=True, prog_=ep(t, C["04.b"], 1.2))
        text(c, "LUCRO", *g2.P(7, 4), 30, "black", GREEN, ab)
        text(c, "prejuízo", *g2.P(1.6, -3), 22, "black", RED, ab)
        text(c, "prejuízo", *g2.P(12.4, -3), 22, "black", RED, ab)
        text(c, "produção", 1360, 740, 24, "bold", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        regra(c, "AS DUAS SÃO PARÁBOLAS", W / 2, 800, acc, 36, PURPLE)


# ======================================================================
# bloco a e b — as três formas e a mesma parábola
# ======================================================================

FORMAS = [("GERAL", "ax² + bx + c", "mostra o c", BLUE), ("FATORADA", "a(x − x₁)(x − x₂)", "mostra as raízes", PURPLE),
          ("CANÔNICA", "a(x − xᵥ)² + yᵥ", "mostra o vértice", TEAL)]


def b_formas(c, t, C, B):
    head(c, t, B["start"], "UMA PARÁBOLA, TRÊS LEIS?", "AS TRÊS FORMAS", BLUE)
    card(c, *CARD_R)
    for k, (cue, (tit, lei, mostra, col)) in enumerate(zip(("05.a", "05.b", "05.c"), FORMAS)):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 220 + k * 520
        rrect(c, x, 230, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x, 230, 460, 70, 26, col, ak * 0.16)
        text(c, "FORMA " + tit, x + 230, 278, 30, "black", col, ak, tracking=1)
        ftext(c, lei, x + 230, 420, 44, "black", INK, ak)
        pill(c, mostra, x + 230, 510, col, size=26, a=ak * ep(t, C["05.d"] + k * 1.4, 0.4), anchor="center")
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        for k in range(3):
            camera(c, 220 + k * 520 + 230, 650, 70, FORMAS[k][3], ad)
        regra(c, "3 FOTOS DA MESMA PESSOA", W / 2, 770, ad, 38, PURPLE)


MESMA = [("GERAL", "2x² − 8x + 6", "corta o eixo y em 6", BLUE),
         ("FATORADA", "2(x − 1)(x − 3)", "raízes 1 e 3", PURPLE),
         ("CANÔNICA", "2(x − 2)² − 2", "vértice (2, −2)", TEAL)]


def b_mesma(c, t, C, B):
    head(c, t, B["start"], "A MESMA PESSOA", "NAS TRÊS FOTOS", PURPLE)
    card(c, *CARD_R)
    f = lambda x: 2 * x * x - 8 * x + 6
    g = Graf(230, 220, 560, 520, -1, 5, -3, 8)
    a0 = ep(t, C["06"], 0.4)
    g.eixos(c, a0, ((1, "1"), (2, "2"), (3, "3"), (4, "4")), ((6, "6"), (-2, "−2")))
    g.curva(c, f, a0, BLUE, ep(t, C["06"], 1.0), 7, xa=-0.35, xb=4.35)
    cues = ["06.a", "06.b", "06.c"]
    ativos = [ep(t, C[q], 0.5) for q in cues]
    foco = [0.0] * 3
    for k in range(3):
        if ativos[k] > 0:
            foco = [0.0] * 3
            foco[k] = ativos[k]
    if t >= C["06.d"]:
        foco = [1.0, 1.0, 1.0]
    for k, (tit, lei, mostra, col) in enumerate(MESMA):
        if ativos[k] <= 0:
            continue
        cracha(c, 900, 195 + k * 165, 700, 150, tit, lei, mostra, col, ativos[k], foco[k])
    # destaques no gráfico
    g.ponto(c, 0, 6, ativos[0] * foco[0], BLUE, 15)
    if ativos[0] * foco[0] > 0:
        pill(c, "(0, 6)", g.P(0, 6)[0] + 26, g.P(0, 6)[1], BLUE, size=24, a=ativos[0] * foco[0])
    for r_ in (1, 3):
        g.ponto(c, r_, 0, ativos[1] * foco[1], PURPLE, 15)
    g.ponto(c, 2, -2, ativos[2] * foco[2], TEAL, 15)
    if ativos[2] * foco[2] > 0:
        pill(c, "(2, −2)", g.P(2, -2)[0] + 26, g.P(2, -2)[1] + 10, TEAL, size=24, a=ativos[2] * foco[2])
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 900, 705, 700, 115, 20, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("2(x² − 4x + 4) − 2 = ", INK), ("2x² − 8x + 6", BLUE)], 1250, 745, 34, ad)
        text(c, "produto notável → a geral volta ✓", 1250, 800, 24, "bold", GREEN, ad)


def b_foto(c, t, C, B):
    head(c, t, B["start"], "QUAL FOTO USAR?", "ATALHO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    K.atalho(c, 360, 200, 1200, 140, "ATALHO", ["a PERGUNTA escolhe a FOTO"], aa, 44)
    ab = ep(t, C["07.b"], 0.5)
    rows = [("corta o eixo y?", "GERAL", BLUE), ("as raízes?", "FATORADA", PURPLE), ("o topo ou o fundo?", "CANÔNICA", TEAL)]
    for k, (perg, forma, col) in enumerate(rows):
        ak = ep(t, C["07.b"] + k * 1.6, 0.4) if ab > 0 else 0
        if ak <= 0:
            continue
        y = 420 + k * 105
        rrect(c, 360, y - 42, 560, 84, 18, "#FFFFFF", ak, shadow=True)
        text_mid(c, "pediram " + perg, 640, y, 32, "black", INK2, ak)
        arrow(c, 950, y, 1080, y, INK2, ak, 5, 18)
        rrect(c, 1110, y - 42, 450, 84, 18, col, ak * 0.9)
        text_mid(c, forma, 1335, y, 38, "black", "#FFFFFF", ak)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 790, acc, "A CONTA VIRA LEITURA", GREEN, -3, 32)


# ======================================================================
# bloco c — a lei pelo gráfico (o arco da ponte)
# ======================================================================

def b_ponte_lei(c, t, C, B):
    head_seq(c, t, C, [("08", "SÓ TEMOS O DESENHO", "A LEI PELO GRÁFICO", PURPLE),
                       ("09", "E SE ELE MOSTRAR O TOPO?", "COMECE PELA CANÔNICA", TEAL)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    g = Graf(220, 300, 640, 340, -4, 44, 0, 12)
    a0 = ep(t, C["08"], 0.4)
    arco(c, g, a0, ep(t, C["08"], 1.0))
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        pa, pb = g.P(0, 0), g.P(40, 0)
        line(c, pa[0], pa[1] + 100, pb[0], pb[1] + 100, INK2, aa, 3)
        arrow(c, (pa[0] + pb[0]) / 2, pa[1] + 100, pa[0], pa[1] + 100, INK2, aa, 3, 12)
        arrow(c, (pa[0] + pb[0]) / 2, pa[1] + 100, pb[0], pb[1] + 100, INK2, aa, 3, 12)
        ftext(c, "40 m", (pa[0] + pb[0]) / 2, pa[1] + 145, 32, "black", INK, aa)
        pt = g.P(20, 10)
        line(c, pt[0], pt[1], pt[0], pa[1], AMBER, aa, 3, dash=(10, 8))
        ftext(c, "10 m", pt[0] + 60, (pt[1] + pa[1]) / 2 + 10, 32, "black", AMBER, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        for xx, s_ in ((0, "0"), (40, "40")):
            g.ponto(c, xx, 0, ab, PURPLE, 14)
            ftext(c, s_, g.P(xx, 0)[0], g.P(xx, 0)[1] - 30, 30, "black", PURPLE, ab)
    if sid == "08":
        if ab > 0:
            pill(c, "mostra as raízes → FATORADA", 1290, 260, PURPLE, size=26, a=ab, anchor="center")
            linha(c, [("f(x) = ", INK), ("a", AMBER), ("·x·(x − 40)", PURPLE)], 1290, 360, 52, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            g.ponto(c, 20, 10, acc, AMBER, 15)
            rrect(c, 980, 420, 620, 230, 22, "#FFFFFF", acc, shadow=True)
            text(c, "o topo (20, 10) acha o a", 1290, 470, 28, "black", INK2, acc)
            linha(c, [("a·20·(−20) = 10", INK)], 1290, 535, 42, acc)
            linha(c, [("a = −1/40", AMBER)], 1290, 610, 52, ep(t, C["08.c"] + 4.0, 0.4))
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            carinha(c, 1060, 745, 55, ad, triste=True, col=PURPLE)
            text_mid(c, "a < 0: parábola TRISTE", 1140, 745, 32, "black", PURPLE, ad, align="left")
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        pill(c, "mostra o vértice → CANÔNICA", 1290, 260, TEAL, size=26, a=aa, anchor="center")
        linha(c, [("f(x) = ", INK), ("a", AMBER), ("(x − 20)² + 10", TEAL)], 1290, 360, 52, aa)
        g.ponto(c, 20, 10, aa, TEAL, 15)
        text(c, "o vértice entra direto · falta só o a", 1290, 440, 28, "bold", INK2, aa)
    ab = ep(t, C["09.b"], 0.5)
    K.atalho(c, 980, 500, 620, 300, "ATALHO", ["ache o a com um ponto", "que NÃO seja raiz"], ab, 34)
    if ab > 0:
        text(c, "na raiz: a · 0 = 0 → o a some", 1290, 770, 24, "bold", RED, ep(t, C["09.b"] + 3.0, 0.4))


# ======================================================================
# bloco d — estudo do sinal
# ======================================================================

def b_sinal(c, t, C, B):
    head(c, t, B["start"], "ONDE ELA É POSITIVA?", "ESTUDO DO SINAL", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 190, 1460, 90, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        text_mid(c, "ESTUDO DO SINAL: para quais x a função dá  +   −   0 ?", 960, 235, 34, "black", BLUE, aa)
    f = lambda x: x * x - 4 * x + 3
    g = Graf(300, 330, 640, 420, -0.6, 4.6, -1.6, 5)
    ab = ep(t, C["10.b"], 0.5)
    g.eixos(c, ab, ((1, "x₁"), (3, "x₂")), ())
    g.pinta(c, f, ab * ep(t, C["10.b"] + 1.2, 0.6))
    g.curva(c, f, ab, sinal=True, prog_=ep(t, C["10.b"], 1.0), xa=-0.5, xb=4.5)
    g.faixa_sinal(c, (1, 3), "+−+", ab * ep(t, C["10.b"] + 2.0, 0.5), size=48)
    if ab > 0:
        pill(c, "a > 0", 850, 360, PURPLE, size=26, a=ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 1040, 360, 600, 380, 24, mix("#FFFFFF", PURPLE, 0.10), acc)
        text(c, "REGRA DO SINAL", 1340, 410, 26, "black", PURPLE, acc, tracking=2)
        para(c, "ENTRE as raízes: o sinal CONTRÁRIO ao de a", 1080, 490, 36, "black", INK, acc, 520, 46)
        para(c, "FORA delas: o MESMO sinal de a", 1080, 640, 36, "black", INK, ep(t, C["10.c"] + 2.4, 0.4), 520, 46)


def b_carinha(c, t, C, B):
    head(c, t, B["start"], "POR QUE A REGRA FUNCIONA?", "DESENHE A CARINHA", GREEN)
    card(c, *CARD_R)
    for k, (cue, triste, tit, sub, col) in enumerate((("11.a", True, "TRISTE (a < 0)", "positiva no MEIO", GREEN),
                                                      ("11.b", False, "SORRINDO (a > 0)", "negativa no MEIO", RED))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 200, 680, 400, 26, "#FFFFFF", ak, shadow=True)
        text(c, tit, x, 255, 34, "black", PURPLE, ak)
        carinha(c, x, 420, 190, ak, triste=triste)
        sg = "−+−" if triste else "+−+"
        for j, s_ in enumerate(sg):
            text_mid(c, s_, x + (j - 1) * 210, 520, 50, "black", GREEN if s_ == "+" else RED, ak)
        text(c, sub, x, 580, 32, "black", col, ak)
    acc = ep(t, C["11.c"], 0.5)
    K.atalho(c, 360, 640, 1200, 170, "ATALHO", ["desenhe a carinha:", "FORA das raízes, o sinal é o do a"], acc, 34)


def b_delta(c, t, C, B):
    head(c, t, B["start"], "E SEM DUAS RAÍZES?", "Δ = 0 E Δ < 0 (com a > 0)", BLUE)
    card(c, *CARD_R)
    casos = [("12.a", "Δ = 0", lambda x: (x - 2) ** 2, "positiva em todo x ≠ raiz", True),
             ("12.b", "Δ < 0", lambda x: x * x - 4 * x + 5.2, "positiva para todo x", False)]
    for k, (cue, tit, f, sub, toca) in enumerate(casos):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x0 = 230 + k * 780
        rrect(c, x0, 200, 680, 600, 26, "#FFFFFF", ak, shadow=True)
        text(c, tit, x0 + 340, 260, 44, "black", PURPLE, ak)
        g = Graf(x0 + 90, 300, 500, 330, -0.4, 4.4, -1, 5)
        g.eixos(c, ak, ((2, "2"),) if toca else (), ())
        g.pinta(c, f, ak, -0.4, 4.4)
        g.curva(c, f, ak, sinal=True, xa=-0.2, xb=4.2)
        if toca:
            g.ponto(c, 2, 0, ak, INK, 12)
            text(c, "zero", *g.P(2, -0.6), 24, "bold", INK2, ak)
        text(c, sub, x0 + 340, 760, 32, "black", GREEN, ak)


# ======================================================================
# bloco e — inequação e "não divida por x"
# ======================================================================

def b_ineq(c, t, C, B):
    head(c, t, B["start"], "E A INEQUAÇÃO?", "x² − 5x + 6 ≤ 0", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 190, 1460, 90, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        text_mid(c, "INEQUAÇÃO DO 2º GRAU: onde a função é > 0, < 0, ≥ 0 ou ≤ 0?", 960, 235, 32, "black", BLUE, aa)
    f = lambda x: x * x - 5 * x + 6
    g = Graf(300, 330, 620, 400, 0.6, 4.4, -0.8, 3)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("x² − 5x + 6 ≤ 0", INK)], 1310, 345, 50, ab)
        linha(c, [("soma 5 · produto 6 → ", INK2), ("2 e 3", PURPLE)], 1310, 420, 36, ep(t, C["13.b"] + 3.0, 0.4))
    acc = ep(t, C["13.c"], 0.5)
    g.eixos(c, ab, ((2, "2"), (3, "3")), ())
    g.pinta(c, f, acc)
    g.curva(c, f, ab, sinal=acc > 0, col=BLUE, xa=0.9, xb=4.1)
    for r_ in (2, 3):
        g.ponto(c, r_, 0, ab, INK, 13)
    if acc > 0:
        g.faixa_sinal(c, (2, 3), "+−+", acc, size=44)
        pill(c, "a > 0 · sorrindo", 340, 360, PURPLE, size=24, a=acc)
        rrect(c, 1010, 470, 600, 120, 20, mix("#FFFFFF", PURPLE, 0.10), acc)
        linha(c, [("S = { x real | ", INK), ("2 ≤ x ≤ 3", RED), (" }", INK)], 1310, 515, 38, acc)
        text(c, "CONJUNTO SOLUÇÃO: os x que servem", 1310, 572, 22, "black", BLUE, ep(t, C["13.c"] + 4.0, 0.4))
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        K.boxed(c, 1010, 610, 600, 190, GREEN, ad, 0.08)
        text(c, "ATALHO · CONFIRA UMA DE CADA REGIÃO", 1310, 650, 20, "black", GREEN, ad, tracking=1)
        linha(c, [("x = 0 → 6 ", INK), ("(fora)", RED)], 1310, 705, 32, ep(t, C["13.d"] + 2.4, 0.4))
        linha(c, [("x = 2,5 → −0,25 ", INK), ("(dentro)", GREEN)], 1310, 762, 32, ep(t, C["13.d"] + 4.2, 0.4))


def b_naodivida(c, t, C, B):
    head(c, t, B["start"], "E O GANCHO?", "NUNCA DIVIDA POR x", RED)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("x² > 4x   →   ", INK), ("x² − 4x > 0", PURPLE)], 1310, 260, 46, aa)
        pill(c, "passe tudo para um lado", 1310, 330, GREEN, size=24, a=aa, anchor="center")
    f = lambda x: x * x - 4 * x
    g = Graf(280, 270, 640, 470, -2, 6, -5, 6)
    ab = ep(t, C["14.b"], 0.5)
    g.eixos(c, aa, ((0, "0"), (4, "4")), ())
    g.pinta(c, f, ab)
    g.curva(c, f, aa, sinal=ab > 0, col=BLUE, xa=-1.4, xb=5.4)
    for r_ in (0, 4):
        g.ponto(c, r_, 0, ab, INK, 13, vazio=True)
    if ab > 0:
        linha(c, [("x(x − 4) → raízes ", INK2), ("0 e 4", PURPLE)], 1310, 420, 36, ab)
        rrect(c, 1010, 470, 600, 110, 20, mix("#FFFFFF", GREEN, 0.14), ep(t, C["14.b"] + 3.0, 0.4))
        linha(c, [("x < 0", GREEN), ("  ou  ", INK), ("x > 4", GREEN)], 1310, 525, 46, ep(t, C["14.b"] + 3.0, 0.4))
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        pisca = 0.5 + 0.5 * abs(((t - C["14.c"]) * 1.6) % 2 - 1)
        pa, pb = g.P(-2, 0), g.P(0, 0)
        rrect(c, pa[0], pa[1] - 16, pb[0] - pa[0], 32, 16, AMBER, acc * pisca * 0.8)
        selo(c, 470, 795, acc, "A DIVISÃO POR x APAGOU ISTO", AMBER, -3, 26)
        rrect(c, 1010, 610, 600, 190, 22, mix("#FFFFFF", RED, 0.08), acc)
        text(c, "NUNCA DIVIDA POR x", 1310, 660, 34, "black", RED, acc)
        para(c, "você não sabe se ele é + ou −, e o sinal da desigualdade pode virar", 1040, 715, 26, "bold", INK2,
             acc, 540, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "x² − 9 < 0", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0 and t < C["16"]:
        text(c, "para quais x vale", 960, 330, 40, "bold", INK2, aa)
        linha(c, [("x² − 9 < 0", INK)], 960, 450, 110, aa)
    if t < C["16"]:
        pause_timer(c, t, C["15.end"] - 1.9, 960, 680)
        return
    linha(c, [("x² − 9 < 0", INK)], 1310, 250, 54, 1)
    f = lambda x: x * x - 9
    g = Graf(260, 250, 660, 500, -6, 6, -10, 18)
    aa = ep(t, C["16.a"], 0.5)
    g.eixos(c, ep(t, C["16"], 0.4), ((-5, "−5"), (-3, "−3"), (3, "3")), ())
    g.curva(c, f, ep(t, C["16"], 0.4), sinal=aa > 0, col=BLUE, xa=-5.4, xb=5.4)
    for r_ in (-3, 3):
        g.ponto(c, r_, 0, aa, INK, 13, vazio=True)
    if aa > 0:
        linha(c, [("x² = 9 → raízes ", INK2), ("−3 e 3", PURPLE)], 1310, 340, 36, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        g.pinta(c, f, ab, -5.4, 5.4)
        g.faixa_sinal(c, (-3, 3), "+−+", ab, size=44)
        rrect(c, 1010, 400, 600, 110, 20, mix("#FFFFFF", GREEN, 0.14), ab)
        linha(c, [("−3 < x < 3", GREEN)], 1310, 455, 50, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        rrect(c, 1010, 540, 600, 260, 22, mix("#FFFFFF", AMBER, 0.12), acc)
        linha(c, [("só  x < 3 ?", AMBER)], 1310, 590, 40, acc)
        a2 = ep(t, C["16.c"] + 2.6, 0.4)
        linha(c, [("x = −5:  25 − 9 = ", INK), ("16 > 0", RED)], 1310, 670, 36, a2)
        text(c, "positivo: −5 NÃO serve", 1310, 750, 30, "black", RED, a2)
        g.ponto(c, -5, 16, a2, RED, 14)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Geral mostra o c; fatorada, as raízes; canônica, o vértice.",
          "Entre as raízes, o sinal contrário ao de a.",
          "Inequação do 2º grau: passe tudo para um lado e nunca divida por x."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("x² > 4x  ⇒  x > 4 (dividiu por x)", "dividir os dois lados funciona nas equações",
          "x pode ser negativo: x < 0 OU x > 4"),
         ("x² − 5x + 6 é POSITIVA entre 2 e 3", "o a é positivo, e “positivo” lembra o meio",
          "x = 2,5 dá −0,25: com a > 0, o meio é NEGATIVO"),
         ("−x² + 10x − 16 cresce até 5: então lucro até 5", "crescer soa como coisa boa",
          "L(1) = −7, prejuízo subindo. Lucro positivo: entre 2 e 8"),
         ("raízes 2 e 4, corta o eixo y em 8:  8(x − 2)(x − 4)", "o 8 é o número que sobrou",
          "essa lei corta em 64. Em x = 0: a·8 = 8 → a = 1")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20", "21"], ERROS)


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


ALTS4 = [("A", "f(x) = x² + 6x + 5", "raízes −1 e −5", RED), ("B", "f(x) = x² − 6x + 5", "", GREEN),
         ("C", "f(x) = −x² + 6x − 5", "corta o eixo y em −5", RED), ("D", "f(x) = x² − 5x + 6", "raízes 2 e 3", RED),
         ("E", "f(x) = 5x² − 30x + 25", "a = 5: corta em 25", AMBER)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "A LEI A PARTIR DO GRÁFICO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("O gráfico de uma função quadrática f é uma parábola que corta o eixo das abscissas nos pontos "
                           "de abscissas 1 e 5 e corta o eixo das ordenadas no ponto (0, 5). A lei dessa função é", INK)],
                      a0, 236, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 260, 680, 36, C["23.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["23"]:
        if a0 > 0:
            g = Graf(250, yend + 20, 440, 230, -0.5, 6, -1.5, 6)
            g.eixos(c, a0, ((1, "1"), (5, "5")), ((5, "5"),))
            for xx, yy in ((1, 0), (5, 0), (0, 5)):
                g.ponto(c, xx, yy, a0, BLUE, 11)
        pause_timer(c, t, C["22.end"] - 1.9, 860, yend + 140)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["23"], 0.4))
    text(c, "mostra as raízes → FATORADA", 540, y0 + 60, 28, "black", PURPLE, ep(t, C["23"], 0.4))
    aa = ep(t, C["23.a"], 0.4)
    if aa > 0:
        linha(c, [("f(x) = ", INK), ("a", AMBER), ("(x − 1)(x − 5)", PURPLE)], 540, y0 + 140, 40, aa)
    ab = ep(t, C["23.b"], 0.4)
    if ab > 0:
        text(c, "(0, 5) acha o a:", 540, y0 + 215, 26, "bold", INK2, ab)
        linha(c, [("a·(−1)·(−5) = 5  →  ", INK), ("a = 1", AMBER)], 540, y0 + 275, 36, ab)
    acc = ep(t, C["23.c"], 0.4)
    if acc > 0:
        linha(c, [("f(x) = ", INK), ("x² − 6x + 5", GREEN)], 540, y0 + 365, 44, acc)
        linha(c, [("f(1) = 1 − 6 + 5 = ", INK2), ("0 ✓", GREEN)], 540, y0 + 445, 32, ep(t, C["23.c"] + 3.0, 0.4))
        check_icon(c, 250, y0 + 530, 20, ep(t, C["23.ok"], 0.4), GREEN)
        linha(c, [("alternativa B", GREEN)], 290, y0 + 532, 30, ep(t, C["23.ok"], 0.4), align="left")


ALTS6 = [("A", "2,5 m", "reta do pé ao topo", RED), ("B", "4,375 m", "", GREEN), ("C", "5,625 m", "o quanto DESCEU", AMBER),
         ("D", "7,5 m", "reta com os 15 m até o centro", RED), ("E", "9,375 m", "5 m a partir do CENTRO", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · NÓS FAZEMOS", "A ALTURA DO ARCO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS6, 1000, 270, 680, 40, C["26.ok"], "B", cues_in, cues_x, gap=46)
    if t < C["26"]:
        yend = _enunciado(c, [("O arco de uma ponte tem a forma de uma parábola. Seus pés estão no nível da água, a 40 m um "
                               "do outro, e o ponto mais alto fica 10 m acima da água, no meio do vão. A altura do arco "
                               "num ponto a 5 m de um dos pés, medidos na horizontal, é", INK)], a0, 236, 26)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 110)
        return
    y0 = 236 - 30
    ap = ep(t, C["26"], 0.4)
    _painel(c, y0, ap)
    g = Graf(230, y0 + 50, 620, 220, -4, 44, 0, 12)
    arco(c, g, ap, 1.0, 6)
    if ap > 0:
        linha(c, [("f(x) = ", INK), ("−1/40", AMBER), ("·x·(x − 40)", PURPLE)], 540, y0 + 360, 36, ap)
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        g.ponto(c, 5, 4.375, aa, GREEN, 12)
        px, py = g.P(5, 4.375)
        line(c, px, py, px, g.P(5, 0)[1], GREEN, aa, 3, dash=(8, 6))
        linha(c, [("x = 5:  −1/40 · 5 · (−35)", INK)], 540, y0 + 430, 32, aa)
    ab = ep(t, C["26.b"], 0.4)
    if ab > 0:
        linha(c, [("= 175/40 = ", INK), ("4,375 m", GREEN)], 540, y0 + 495, 40, ab)
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        text(c, "perto do pé: menos da metade do topo ✓", 540, y0 + 565, 24, "bold", GREEN, acc)
        check_icon(c, 250, y0 + 610, 18, ep(t, C["26.ok"], 0.4), GREEN)
        linha(c, [("alternativa B", GREEN)], 285, y0 + 612, 28, ep(t, C["26.ok"], 0.4), align="left")


ALTS5 = [("A", "menos de 400 unidades.", "pedaço errado", RED),
         ("B", "mais de 1 000 unidades.", "pedaço errado", RED),
         ("C", "menos de 400 ou mais de 1 000 unidades.", "sinal de a > 0", RED),
         ("D", "mais de 400 e menos de 1 000 unidades.", "", GREEN),
         ("E", "menos de 700 unidades.", "crescendo ≠ positivo", AMBER)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "QUANDO O LUCRO É POSITIVO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 32, C["29.ok"], "D", cues_in, cues_x, gap=30)
    if t < C["29"]:
        yend = _enunciado(c, [("O lucro mensal de uma pequena fábrica, em milhares de reais, é modelado por "
                               "L(x) = −x² + 14x − 40, em que x é a quantidade produzida, em centenas de unidades. "
                               "A fábrica tem lucro positivo quando produz", INK)], a0, 236, 28)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        pause_timer(c, t, C["28.end"] - 1.9, 540, yend + 120)
        return
    y0 = 236 - 30
    ap = ep(t, C["29"], 0.4)
    _painel(c, y0, ap)
    L = lambda x: -x * x + 14 * x - 40
    g = Graf(240, y0 + 230, 600, 300, 1, 13, -18, 12)
    aa = ep(t, C["29.a"], 0.4)
    if aa > 0:
        linha(c, [("soma 14 · produto 40 → ", INK2), ("4 e 10", PURPLE)], 540, y0 + 60, 32, aa)
    ab = ep(t, C["29.b"], 0.4)
    if ab > 0:
        linha(c, [("a = −1: TRISTE, ", INK), ("+ no meio", GREEN)], 540, y0 + 125, 32, ab)
        linha(c, [("400 < produção < 1 000", GREEN)], 540, y0 + 185, 34, ep(t, C["29.b"] + 3.0, 0.4))
    g.eixos(c, aa, ((4, "4"), (10, "10")), (), rx="x (centenas)", ry="L", size=22)
    g.pinta(c, L, ab)
    g.curva(c, L, aa, sinal=ab > 0, col=BLUE, xa=1.6, xb=12.4)
    acc = ep(t, C["29.c"], 0.4)
    if acc > 0:
        g.ponto(c, 7, 9, acc, GREEN, 11)
        g.ponto(c, 2, -16, acc, RED, 11)
        text(c, "L(7) = 9", *g.P(7, 10.6), 22, "black", GREEN, acc)
        text(c, "L(2) = −16", g.P(2, -16)[0] + 70, g.P(2, -16)[1] + 8, 22, "black", RED, acc, align="left")
        check_icon(c, 250, 800, 18, ep(t, C["29.ok"], 0.4), GREEN)
        linha(c, [("alternativa D", GREEN)], 285, 802, 28, ep(t, C["29.ok"], 0.4), align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DA FUNÇÃO QUADRÁTICA", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    if aa > 0:
        linha(c, [("f(x) = ", INK), ("ax² + bx + c", PURPLE)], W / 2, 280, 80, aa)
    itens = [("FÍSICA", "lançamentos", BLUE), ("ECONOMIA", "lucro máximo", GREEN), ("GEOMETRIA", "área máxima", TEAL)]
    for k, (tit, sub, col) in enumerate(itens):
        ak = ep(t, C["32.b"] + k * 0.9, 0.5)
        if ak <= 0:
            continue
        x = 480 + k * 480
        rrect(c, x - 200, 380, 400, 260, 24, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 200, 380, 400, 64, 24, col, ak * 0.16)
        text(c, tit, x, 425, 30, "black", col, ak)
        carinha(c, x, 540, 70, ak, triste=True, col=col)
        text(c, sub, x, 618, 26, "bold", INK2, ak)
    acc = ep(t, C["32.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 740, acc, "E AS PEGADINHAS", AMBER, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Qual das três fotos da parábola você mais vai usar na prova?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, formas=b_formas, mesma=b_mesma,
              foto=b_foto, ponte_lei=b_ponte_lei, sinal=b_sinal, carinha=b_carinha, delta=b_delta, ineq=b_ineq,
              naodivida=b_naodivida, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q6=b_q6, q5=b_q5,
              ponte=b_ponte, cta=b_cta)
