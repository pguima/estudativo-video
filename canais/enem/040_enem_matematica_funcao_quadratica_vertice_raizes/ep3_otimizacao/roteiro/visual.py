"""Visual — Função Quadrática, Episódio 3: otimização, área máxima e receita máxima (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: cercado() (muro + horta cercada em 3 lados, com medidas), Plano (eixos + curva da parábola + ponto
que percorre a curva), etiqueta() (etiqueta de preço), fila() de clientes, onibus() (40 lugares), linha() (texto com cor por
trecho, mantém o espaço de milhar).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
ARQUIVO_FINAL = "enem_matematica_funcao_quadratica_ep3_otimizacao.mp4"
CARD_R = K.CARD_R
MURO = "#8A8F99"
HORTA = "#7BC67E"


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


def muro(c, cx, y, w, a):
    """faixa de tijolos (o muro) com o rótulo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, y - 34, w, 34, 4, MURO, a)
    for k in range(int(w // 60)):
        line(c, cx - w / 2 + 30 + k * 60, y - 34, cx - w / 2 + 30 + k * 60, y - 17, "#FFFFFF", a * 0.6, 2)
        line(c, cx - w / 2 + 60 + k * 60, y - 17, cx - w / 2 + 60 + k * 60, y, "#FFFFFF", a * 0.6, 2)
    line(c, cx - w / 2, y - 17, cx + w / 2, y - 17, "#FFFFFF", a * 0.6, 2)
    text(c, "MURO", cx + w / 2 - 10, y - 46, 22, "black", MURO, a, align="right")


def cercado(c, cx, y, lat, frente, esc, a, col=None, medidas=True, area=None, area_col=None, fill=0.22, size=26):
    """horta encostada no muro (topo em y): laterais 'lat' m, frente 'frente' m, escala esc px/m. Tela em 3 lados."""
    if a <= 0:
        return
    col = col or GREEN
    w, h = frente * esc, lat * esc
    x0 = cx - w / 2
    rrect(c, x0, y, w, h, 0, area_col or HORTA, a * fill)
    for p1, p2 in (((x0, y), (x0, y + h)), ((x0, y + h), (x0 + w, y + h)), ((x0 + w, y + h), (x0 + w, y))):
        line(c, *p1, *p2, col, a, 6)
    for k in range(int(w // 22) + 1):
        c.drawCircle(x0 + k * 22, y + h, 3, paint(col, a * 0.7))
    if medidas:
        ftext(c, f"{fmt(lat)} m", x0 - 14, y + h / 2 + 9, size, "black", INK2, a, align="right")
        ftext(c, f"{fmt(frente)} m", cx, y + h + 38, size, "black", INK2, a)
    if area is not None:
        if w < 200:
            ftext(c, area, x0 + w + 20, y + h / 2 + 12, size + 6, "black", INK, a, align="left")
        else:
            ftext(c, area, cx, y + h / 2 + 12, size + 6, "black", INK, a)


def fmt(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


class Plano:
    """eixos de um gráfico: (x0, y0) = canto inferior esquerdo em pixels; xmin..xmax, 0..ymax"""

    def __init__(self, x0, y0, w, h, xmax, ymax, xmin=0.0):
        self.x0, self.y0, self.w, self.h, self.xmax, self.ymax, self.xmin = x0, y0, w, h, xmax, ymax, xmin

    def P(self, x, y):
        return self.x0 + self.w * (x - self.xmin) / (self.xmax - self.xmin), self.y0 - self.h * y / self.ymax

    def eixos(self, c, a, rx="x", ry="y", ticks_x=(), ticks_y=()):
        if a <= 0:
            return
        line(c, self.x0, self.y0, self.x0 + self.w + 30, self.y0, INK2, a, 4)
        ox = self.P(0, 0)[0]
        line(c, ox, self.y0, ox, self.y0 - self.h - 30, INK2, a, 4)
        text(c, rx, self.x0 + self.w + 30, self.y0 + 84, 22, "bold", INK2, a, align="right")
        text(c, ry, ox - 12, self.y0 - self.h - 46, 24, "bold", INK2, a, align="left")
        for v, s_ in ticks_x:
            px, _ = self.P(v, 0)
            line(c, px, self.y0 - 8, px, self.y0 + 8, INK2, a, 3)
            ftext(c, s_, px, self.y0 + 42, 24, "bold", INK2, a)
        for v, s_ in ticks_y:
            _, py = self.P(0, v)
            line(c, ox - 8, py, ox + 8, py, INK2, a, 3)
            ftext(c, s_, ox - 16, py + 9, 22, "bold", INK2, a, align="right")

    def curva(self, c, f, xa, xb, col, a, prog_=1.0, sw=7, n=80):
        if a <= 0 or prog_ <= 0:
            return
        p = skia.Path()
        xe = xa + (xb - xa) * prog_
        for k in range(n + 1):
            x = xa + (xe - xa) * k / n
            px, py = self.P(x, f(x))
            (p.moveTo if k == 0 else p.lineTo)(px, py)
        c.drawPath(p, paint(col, a, stroke=sw))

    def ponto(self, c, x, y, col, a, r=14):
        if a <= 0:
            return
        px, py = self.P(x, y)
        c.drawCircle(px, py, r, paint(col, a))
        c.drawCircle(px, py, r, paint(INK, a, stroke=4))


def etiqueta(c, cx, cy, s, a, col=None, size=54):
    """etiqueta de preço pendurada"""
    if a <= 0:
        return
    col = col or AMBER
    w = ftext_w(s, "black", size) + 80
    p = skia.Path()
    p.moveTo(cx - w / 2 + 40, cy - 50); p.lineTo(cx + w / 2, cy - 50); p.lineTo(cx + w / 2, cy + 50)
    p.lineTo(cx - w / 2 + 40, cy + 50); p.lineTo(cx - w / 2, cy); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.25), a))
    c.drawPath(p, paint(col, a, stroke=5))
    c.drawCircle(cx - w / 2 + 34, cy, 9, paint(col, a))
    ftext(c, s, cx + 20, cy + size * 0.36, size, "black", INK, a)


def pessoa(c, cx, cy, s, a, col):
    if a <= 0:
        return
    c.drawCircle(cx, cy - s * 0.32, s * 0.18, paint(col, a))
    rrect(c, cx - s * 0.24, cy - s * 0.1, s * 0.48, s * 0.5, s * 0.2, col, a)


def fila_clientes(c, x, cy, n_on, n_tot, a, cols=10, s=34, col=None):
    """grade de bonequinhos: os primeiros n_on acesos, o resto apagado"""
    if a <= 0:
        return
    col = col or BLUE
    for k in range(n_tot):
        on = k < n_on
        pessoa(c, x + (k % cols) * (s + 6), cy + (k // cols) * (s + 14), s, a * (1 if on else 0.15), col if on else GRAY)


def onibus(c, cx, cy, a, cheios=30, lugares=40, extra=0):
    """ônibus com 40 poltronas; 'extra' desenha passageiros sobrando do lado de fora"""
    if a <= 0:
        return
    w, h = 720, 250
    rrect(c, cx - w / 2, cy - h / 2, w, h, 40, mix("#FFFFFF", BLUE, 0.18), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 40, 40), paint(BLUE, a, stroke=6))
    for k in range(lugares):
        col_, lin = k % 10, k // 10
        x = cx - w / 2 + 70 + col_ * 62
        y = cy - h / 2 + 40 + lin * 48
        rrect(c, x - 20, y - 14, 40, 32, 8, GREEN if k < cheios else "#FFFFFF", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 20, y - 14, 40, 32), 8, 8), paint(INK2, a * 0.5, stroke=2))
    for xr in (cx - w / 2 + 120, cx + w / 2 - 120):
        c.drawCircle(xr, cy + h / 2 + 6, 34, paint(INK, a))
        c.drawCircle(xr, cy + h / 2 + 6, 14, paint("#FFFFFF", a))
    for k in range(extra):
        pessoa(c, cx + w / 2 + 50 + (k % 5) * 40, cy - 80 + (k // 5) * 60, 34, a, RED)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO QUADRÁTICA · EPISÓDIO 3", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 760, 200, 400, 70, 20, mix("#FFFFFF", GREEN, 0.18), aa)
        text_mid(c, "60 m de tela + 1 muro", 960, 235, 32, "black", GREEN, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        muro(c, 520, 400, 420, ab)
        cercado(c, 520, 400, 20, 20, 12, ab, RED, area="400 m²", area_col=RED, fill=0.14)
        text(c, "20 + 20 + 20 = 60 m", 520, 720, 28, "bold", INK2, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        muro(c, 1380, 400, 480, acc)
        cercado(c, 1380, 400, 15, 30, 12, acc, GREEN, area="450 m²")
        text(c, "15 + 15 + 30 = 60 m", 1380, 720, 28, "bold", INK2, acc)
        selo(c, 1730, 560, ep(t, C["01.c"] + 1.2, 0.4), "+ 50 m²", GREEN, -4, 34)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "O MURO MUDOU A RESPOSTA", W / 2, 830, ad, 40, AMBER)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO QUADRÁTICA · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de FUNÇÃO QUADRÁTICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "MONTAR", "a área ou a receita", BLUE), ("02.b", "ACHAR O MÁXIMO", "o topo da parábola", PURPLE),
             ("02.c", "RESPONDER", "exatamente o pedido", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 38, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "episódio 2", [("xᵥ = −b ÷ 2a", PURPLE), ("   ·   no MEIO das raízes", INK)]),
             ("03.b", "geometria", [("área do retângulo = ", INK), ("base × altura", PURPLE)]),
             ("03.c", "série de Expressões algébricas", [("(a + b)(c + d) = ", INK), ("ac + ad + bc + bd", PURPLE)])]
    for k, (cue, serie, partes) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, serie, 300, y - 70, BLUE, size=22, a=a)
        linha(c, partes, 960, y + 10, 48, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS CENAS DO DIA A DIA", "O CABO DE GUERRA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 200, 700, 430, 26, "#FFFFFF", aa, shadow=True)
        text(c, "A HORTA", 580, 255, 32, "black", GREEN, aa)
        lat = 8 + 14 * (0.5 + 0.5 * __import__("math").sin(max(0, t - C["04.a"]) * 1.6))
        muro(c, 580, 320, 520, aa)
        cercado(c, 580, 320, lat, 60 - 2 * lat, 8, aa, GREEN, medidas=False)
        text(c, "lateral ↑   frente ↓", 580, 600, 28, "bold", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 990, 200, 700, 430, 26, "#FFFFFF", ab, shadow=True)
        text(c, "O PICOLÉ", 1340, 255, 32, "black", AMBER, ab)
        etiqueta(c, 1180, 370, "R$ ↑", ab, AMBER, 46)
        fila_clientes(c, 1330, 340, 7, 14, ab, cols=7, s=34, col=BLUE)
        text(c, "preço ↑   vendas ↓", 1340, 600, 28, "bold", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 380, 680, 1160, 90, 22, mix("#FFFFFF", BLUE, 0.10), acc)
        text_mid(c, "CABO DE GUERRA: duas grandezas que se multiplicam e puxam para lados opostos", 960, 725, 28,
                 "black", BLUE, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        selo(c, 960, 830, ad, "TODO CABO DE GUERRA TEM UM TOPO", GREEN, -3, 32)


# ======================================================================
# bloco a — o roteiro
# ======================================================================

def b_roteiro(c, t, C, B):
    head(c, t, B["start"], "COMO ACHAR O TOPO?", "O ROTEIRO DE QUATRO PASSOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 200, 1460, 110, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("OTIMIZAR", BLUE), (" = achar o melhor:  ", INK), ("MAXIMIZAR", GREEN), (" (maior)  ·  ", INK2),
                  ("MINIMIZAR", AMBER), (" (menor)", INK2)], 960, 255, 34, aa)
    passos = [("05.b", "ESCOLHER|O x", "a variável de decisão", BLUE), ("05.c", "MONTAR|A FUNÇÃO", "a grandeza em função de x", PURPLE),
              ("05.c", "ACHAR|O VÉRTICE", "xᵥ = −b ÷ 2a", PURPLE), ("05.d", "RESPONDER|O PEDIDO", "o que foi perguntado", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(passos):
        ak = ep(t, C[cue] + (2.4 if k == 2 else 0), 0.5)
        if ak <= 0:
            continue
        x = 400 + k * 375
        rrect(c, x - 170, 370, 340, 320, 24, "#FFFFFF", ak, shadow=True)
        badge_num(c, k + 1, x, 440, ak, 36, bg=col)
        for j, ln in enumerate(tit.split("|")):
            text(c, ln, x, 540 + j * 40, 32, "black", col, ak)
        text(c, sub, x, 650, 21, "bold", INK2, ak)
        if k < 3:
            arrow(c, x + 176, 530, x + 200, 530, INK2, ak, 4, 12)
    ad = ep(t, C["05.d"] + 2.4, 0.5)
    if ad > 0:
        selo(c, 1525, 760, ad, "AQUI O ENEM DERRUBA", AMBER, -4, 30)


# ======================================================================
# blocos b e c — área com muro
# ======================================================================

AREA = lambda x: x * (60 - 2 * x)


def b_area(c, t, C, B):
    head_seq(c, t, C, [("06", "60 m DE TELA, 1 LADO NO MURO", "PASSOS 1 E 2", BLUE),
                       ("07", "O CERCADO MUDANDO DE FORMA", "A PARÁBOLA DA ÁREA", PURPLE),
                       ("08", "PASSO 3: O VÉRTICE", "RAÍZES DE CABEÇA, VÉRTICE NO MEIO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            muro(c, 560, 290, 560, aa)
            cercado(c, 560, 290, 15, 30, 14, aa, GREEN, medidas=False)
            x0 = 560 - 15 * 14
            for xx in (x0 - 18, 560 + 15 * 14 + 18):
                ftext(c, "x", xx, 290 + 15 * 14 / 2 + 14, 44, "black", BLUE, aa, align="right" if xx < 560 else "left")
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            ftext(c, "60 − 2x", 560, 290 + 15 * 14 + 52, 44, "black", PURPLE, ab)
            text(c, "60 menos DUAS laterais", 560, 290 + 15 * 14 + 100, 26, "bold", INK2, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            text(c, "área = base × altura", 1330, 330, 30, "bold", INK2, acc)
            linha(c, [("A(x) = x · ", INK), ("(60 − 2x)", PURPLE)], 1330, 420, 50, acc)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            linha(c, [("A(x) = ", INK), ("−2", RED), ("x² + 60x", INK)], 1330, 530, 54, ad)
            rrect(c, 1080, 610, 500, 110, 22, mix("#FFFFFF", PURPLE, 0.10), ad)
            linha(c, [("a = −2 < 0  →  ", INK), ("TEM TOPO", GREEN)], 1330, 665, 34, ad)
        return
    pl = Plano(1060, 780, 560, 470, 30, 500)
    if sid == "07":
        cues = ["07.a", "07.b", "07.c", "07.d", "07.d"]
        lats = [5, 10, 15, 20, 25]
        cur = 0
        for k, cu in enumerate(cues):
            if t >= C[cu] + (2.6 if k == 4 else 0):
                cur = k
        lat = lats[cur]
        a0 = ep(t, C["07"], 0.4)
        muro(c, 560, 260, 640, a0)
        cercado(c, 560, 260, lat, 60 - 2 * lat, 11, a0, GREEN, area=f"{AREA(lat)} m²")
        pl.eixos(c, a0, "lateral x (m)", "área (m²)", ((5, "5"), (15, "15"), (25, "25"), (30, "30")),
                 ((250, "250"), (450, "450")))
        if t >= C["07.e"]:
            pl.curva(c, AREA, 0, 30, PURPLE, ep(t, C["07.e"], 0.4), ep(t, C["07.e"], 1.6))
        for k in range(cur + 1):
            pl.ponto(c, lats[k], AREA(lats[k]), AMBER if lats[k] == 15 else BLUE, a0, 12)
        if t >= C["07.c"]:
            ghost = ep(t, C["07.c"] + 1.4, 0.5)
            if ghost > 0 and cur >= 2:
                px, py = pl.P(15, 450)
                text(c, "450 m²", px, py - 30, 28, "black", AMBER, ghost)
        return
    a0 = ep(t, C["08"], 0.4)
    pl.eixos(c, a0, "x (m)", "A (m²)", ((0, "0"), (15, "15"), (30, "30")), ((450, "450"),))
    pl.curva(c, AREA, 0, 30, PURPLE, a0)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha(c, [("xᵥ = −60 ÷ (−4) = ", INK), ("15", AMBER)], 560, 300, 48, aa)
    ab = ep(t, C["08.b"], 0.5)
    K.atalho(c, 230, 380, 680, 130, "ATALHO", ["raízes de cabeça, vértice no meio"], ab, 32)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        linha(c, [("x · (60 − 2x) = 0  →  ", INK), ("0", RED), ("  e  ", INK), ("30", RED)], 570, 580, 38, acc)
        for v in (0, 30):
            pl.ponto(c, v, 0, RED, acc, 12)
        am = ep(t, C["08.c"] + 3.2, 0.5)
        if am > 0:
            px, _ = pl.P(15, 0)
            _, py = pl.P(0, 450)
            line(c, px, pl.y0, px, py, AMBER, am, 4)
            linha(c, [("meio: (0 + 30) ÷ 2 = ", INK), ("15", AMBER)], 570, 650, 38, am)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        pl.ponto(c, 15, 450, AMBER, ad, 14)
        rrect(c, 230, 700, 680, 100, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        linha(c, [("A(15) = 15 · 30 = ", INK), ("450 m²", GREEN)], 570, 750, 40, ad)


def b_quadrado(c, t, C, B):
    head(c, t, B["start"], "O MELHOR NÃO ERA O QUADRADO?", "COM MURO, NÃO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 200, 600, 140, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "SEM muro, perímetro fixo:", 530, 255, 28, "bold", INK2, aa)
        text(c, "o quadrado é o ótimo", 530, 305, 34, "black", BLUE, aa)
        pill(c, "só citado", 830, 200, GRAY, size=20, a=aa, anchor="right", bounds=(0, 1920))
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 380, 600, 200, 22, mix("#FFFFFF", GREEN, 0.12), ab)
        text(c, "COM muro:", 530, 435, 30, "black", GREEN, ab)
        text(c, "um lado sai de graça", 530, 490, 30, "bold", INK, ab)
        text(c, "→ vale esticar a frente", 530, 545, 30, "bold", INK, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        muro(c, 1320, 300, 520, acc)
        cercado(c, 1320, 300, 15, 30, 14, acc, GREEN, area="450 m²")
        selo(c, 1320, 600, ep(t, C["09.c"] + 1.6, 0.4), "FRENTE = 2 × LATERAL", PURPLE, -3, 30)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        rrect(c, 230, 640, 600, 150, 22, mix("#FFFFFF", RED, 0.08), ad)
        linha(c, [("quadrado 20 × 20 = ", INK), ("400 m²", RED)], 530, 695, 34, ad)
        linha(c, [("50 m² ATRÁS", RED)], 530, 755, 34, ad)


# ======================================================================
# blocos d e e — receita
# ======================================================================

RECEITA = lambda x: (20 + x) * (100 - 4 * x)


def b_receita(c, t, C, B):
    head_seq(c, t, C, [("10", "E O VENDEDOR QUE SOBE O PREÇO?", "PASSOS 1 E 2", BLUE),
                       ("11", "ABRINDO A CONTA", "PASSO 3: O VÉRTICE", PURPLE)])
    card(c, *CARD_R)
    if t < C["11"]:
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            etiqueta(c, 450, 290, "R$ 20,00", aa, AMBER, 50)
            fila_clientes(c, 760, 230, 10, 10, aa, cols=10, s=40)
            text(c, "100 vendas/dia", 960, 330, 26, "bold", INK2, aa)
            linha(c, [("+ R$ 1  →  ", AMBER), ("− 4 vendas", RED)], 1460, 300, 40, ep(t, C["10.a"] + 2.4, 0.4))
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            rrect(c, 230, 400, 1460, 100, 22, mix("#FFFFFF", BLUE, 0.10), ab)
            linha(c, [("RECEITA", BLUE), (" = preço × quantidade vendida", INK)], 960, 450, 40, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            linha(c, [("x = AUMENTO (R$)", BLUE), ("    preço: ", INK2), ("20 + x", AMBER), ("    vendas: ", INK2),
                      ("100 − 4x", PURPLE)], 960, 580, 38, acc)
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            linha(c, [("R(x) = ", INK), ("(20 + x)", AMBER), (" · ", INK), ("(100 − 4x)", PURPLE)], 960, 720, 60, ad)
        return
    linha(c, [("R(x) = ", INK), ("(20 + x)", AMBER), (" · ", INK), ("(100 − 4x)", PURPLE)], 960, 240, 44, 1)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        parts = ["2 000", "− 80x", "+ 100x", "− 4x²"]
        for k, s_ in enumerate(parts):
            ak = ep(t, C["11.a"] + k * 1.6, 0.4)
            chip(c, s_, 520 + k * 300, 350, PURPLE, ak, 36)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        linha(c, [("R(x) = ", INK), ("−4", RED), ("x² + 20x + 2 000", INK)], 960, 470, 52, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        linha(c, [("xᵥ = −20 ÷ (−8) = ", INK), ("2,5", AMBER)], 960, 570, 48, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        K.atalho(c, 330, 640, 1260, 170, "ATALHO · RAÍZES DE CABEÇA", ["preço zera em −20 · vendas zeram em 25",
                                                                       "meio: (−20 + 25) ÷ 2 = 2,5"], ad, 32)


def b_comando(c, t, C, B):
    head(c, t, B["start"], "O QUE FOI PEDIDO?", "LEIA O COMANDO", AMBER)
    card(c, *CARD_R)
    ab_ = ep(t, C["12.b"], 0.5)
    if ab_ > 0:
        etiqueta(c, 420, 280, "R$ 22,50" if t >= C["12.b"] + 1.5 else "R$ 20,00", ab_, AMBER, 46)
    acc_ = ep(t, C["12.c"], 0.5)
    if acc_ > 0:
        prog = min(1.0, max(0.0, (t - C["12.c"]) / 1.5))
        fila_clientes(c, 760, 220, int(round(100 - 10 * prog)) // 10, 10, acc_, cols=10, s=40)
        text(c, f"{int(round(100 - 10 * prog))} vendas", 960, 320, 28, "black", BLUE, acc_)
    ad_ = ep(t, C["12.d"], 0.5)
    if ad_ > 0:
        rrect(c, 1340, 220, 360, 110, 22, "#1E2633", ad_)
        prog = min(1.0, max(0.0, (t - C["12.d"]) / 2.0))
        v = int(round(1800 + 225 * prog)) if prog < 1 else 2025
        ftext(c, f"R$ {v // 1000}.{v % 1000:03d},00", 1520, 292, 40, "black", GREEN, ad_)
    nums = [("12.a", "AUMENTO", "R$ 2,50", INK), ("12.b", "PREÇO", "R$ 22,50", AMBER), ("12.c", "VENDAS", "90", BLUE),
            ("12.d", "RECEITA", "R$ 2.025,00", GREEN)]
    for k, (cue, rot, v, col) in enumerate(nums):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 400 + k * 375
        rrect(c, x - 170, 440, 340, 200, 24, "#FFFFFF", ak, shadow=True)
        text(c, rot, x, 500, 28, "black", INK2, ak)
        ftext(c, v, x, 590, 46, "black", col, ak)
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        regra(c, "A PROVA PODE PEDIR QUALQUER UM: CIRCULE SÓ O DO COMANDO", W / 2, 720, ae, 32, PURPLE)
        x = 400 + 1 * 375
        c.drawOval(skia.Rect.MakeXYWH(x - 190, 425, 380, 230), paint(RED, ep(t, C["12.e"] + 2.0, 0.4), stroke=7))
        text(c, "ex.: “o preço deve ser”", x, 820, 26, "bold", RED, ep(t, C["12.e"] + 2.0, 0.4))


# ======================================================================
# bloco f — o vértice precisa caber
# ======================================================================

def b_borda(c, t, C, B):
    head(c, t, B["start"], "O VÉRTICE SEMPRE VALE?", "CONFIRA SE ELE CABE", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    cheios = 30
    extra = 0
    if t >= C["13.b"]:
        extra = 15 if ep(t, C["13.b"] + 2.4, 0.4) > 0 else 0
        cheios = 40 if extra else 30
    if t >= C["13.d"]:
        cheios, extra = 40, 0
    onibus(c, 620, 420, aa, cheios, 40, extra)
    if aa > 0:
        text(c, "40 lugares · 30 passageiros a R$ 50,00", 620, 620, 28, "bold", INK2, aa)
        linha(c, [("− R$ 1  →  ", AMBER), ("+ 2 passageiros", GREEN)], 620, 680, 34, ep(t, C["13.a"] + 3.0, 0.4))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0 and t < C["13.d"]:
        rrect(c, 1180, 230, 520, 170, 22, mix("#FFFFFF", RED, 0.08), ab)
        linha(c, [("vértice: ", INK2), ("17,5", AMBER), (" de desconto", INK2)], 1440, 285, 32, ab)
        linha(c, [("→ ", INK), ("65 passageiros", RED)], 1440, 350, 38, ep(t, C["13.b"] + 2.4, 0.4))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 1180, 430, 520, 170, 22, mix("#FFFFFF", BLUE, 0.10), acc)
        text(c, "INTERVALO PERMITIDO", 1440, 485, 28, "black", BLUE, acc)
        linha(c, [("desconto de ", INK), ("0 a 5", BLUE), (" reais", INK)], 1440, 550, 36, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 1180, 630, 520, 170, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        text(c, "ÓTIMO NA BORDA: x = 5", 1440, 685, 28, "black", GREEN, ad)
        linha(c, [("45 × 40 = ", INK), ("R$ 1.800", GREEN)], 1440, 750, 38, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "40 m DE TELA", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["14.a"], 0.5)
    if t < C["15"]:
        if a0 > 0:
            muro(c, 960, 280, 600, a0)
            cercado(c, 960, 280, 10, 20, 14, a0 * 0.35, GREEN, medidas=False)
            ftext(c, "x", 960 - 140 - 18, 280 + 70 + 14, 44, "black", BLUE, a0, align="right")
            ftext(c, "x", 960 + 140 + 18, 280 + 70 + 14, 44, "black", BLUE, a0, align="left")
            text(c, "40 m de tela + muro", 960, 520, 34, "black", GREEN, a0)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            text_mid(c, "ÁREA MÁXIMA?", 960, 600, 50, "black", AMBER, ab)
        pause_timer(c, t, C["14.end"] - 1.9, 960, 730)
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        linha(c, [("A(x) = x · ", INK), ("(40 − 2x)", PURPLE)], 560, 280, 48, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("raízes: ", INK2), ("0", RED), (" e ", INK), ("20", RED), ("  →  meio: ", INK2), ("x = 10", AMBER)],
              560, 380, 40, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        muro(c, 1340, 260, 420, acc)
        cercado(c, 1340, 260, 10, 20, 14, acc, GREEN)
        linha(c, [("frente: 40 − 20 = ", INK), ("20 m", PURPLE)], 560, 480, 38, acc)
        linha(c, [("tela: 10 + 10 + 20 = 40 m", INK2)], 560, 550, 32, ep(t, C["15.c"] + 2.6, 0.4))
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        rrect(c, 240, 620, 640, 110, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        linha(c, [("10 · 20 = ", INK), ("200 m²", GREEN)], 560, 675, 46, ad)
        selo(c, 1340, 640, ep(t, C["15.d"] + 2.2, 0.4), "FRENTE = 2 × LATERAL", PURPLE, -3, 28)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Escolha o x, monte a função, ache o vértice, responda o pedido.",
          "Com muro, o melhor retângulo não é o quadrado.",
          "Confira se o vértice cabe no problema."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Com muro, supor que o ótimo é o QUADRADO: 20 × 20 = 400 m²",
          "você aprendeu que o quadrado é o retângulo mais eficiente",
          "isso vale SEM muro. Com 60 m e muro, o ótimo é 15 × 30 = 450 m²"),
         ("Responder o AUMENTO quando pedem o PREÇO: R$ 2,50", "é o número que acabou de sair da fórmula do vértice",
          "o x era o aumento: preço = 20 + 2,50 = R$ 22,50"),
         ("Esquecer a 2ª lateral: frente = 60 − x → quadrado de 30 → 900 m²", "a lateral que você desenhou é uma só",
          "confira a tela: 30 + 30 + 30 = 90 m, e só havia 60. A frente é 60 − 2x"),
         ("Errar o sinal: −20 ÷ (−8) = −2,5", "a fórmula começa com um sinal de menos",
          "menos com menos dá mais: +2,5. Com −2,5, preço R$ 17,50 e receita R$ 1.925 (menor)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19", "20"], ERROS)


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


ALTS3 = [("A", "400", "cercou os 4 lados", RED), ("B", "711", "3 partes iguais", RED), ("C", "800", "", GREEN),
         ("D", "1 200", "esqueceu a 2ª lateral", RED), ("E", "1 600", "x(80 − x)", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "ÁREA MÁXIMA COM MURO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [("Um sitiante tem 80 metros de tela para cercar uma horta retangular. Um dos lados da horta "
                           "ficará encostado num muro e não receberá tela; os outros três lados serão inteiramente "
                           "cercados com os 80 metros. A maior área possível da horta, em metros quadrados, é", INK)],
                      a0, 236, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 260, 680, 40, C["22.ok"], "C", cues_in, cues_x, gap=40)
    if t < C["22"]:
        pause_timer(c, t, C["21.end"] - 1.9, 540, yend + 120)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["22"], 0.4))
    aa = ep(t, C["22.a"], 0.4)
    if aa > 0:
        muro(c, 540, y0 + 90, 360, aa)
        cercado(c, 540, y0 + 90, 20, 40, 6.5, aa, GREEN, size=24)
        linha(c, [("A(x) = x · ", INK), ("(80 − 2x)", PURPLE)], 540, y0 + 320, 36, ep(t, C["22.a"] + 2.0, 0.4))
    ab = ep(t, C["22.b"], 0.4)
    if ab > 0:
        linha(c, [("raízes ", INK2), ("0", RED), (" e ", INK), ("40", RED), ("  →  meio ", INK2), ("20", AMBER)],
              540, y0 + 400, 34, ab)
    acc = ep(t, C["22.c"], 0.4)
    if acc > 0:
        linha(c, [("A(20) = 20 · 40 = ", INK), ("800 m²", GREEN)], 540, y0 + 480, 36, acc)
        linha(c, [("tela: 20 + 20 + 40 = 80 ✓", INK2)], 540, y0 + 545, 28, ep(t, C["22.c"] + 2.6, 0.4))
        check_icon(c, 250, y0 + 600, 20, ep(t, C["22.ok"], 0.4), GREEN)
        linha(c, [("maior área: 800 m²", GREEN)], 290, y0 + 602, 30, ep(t, C["22.ok"], 0.4), align="left")


ALTS2 = [("A", "R$ 15,00", "é o DESCONTO", RED), ("B", "R$ 30,00", "metade, sem conta", RED), ("C", "R$ 45,00", "", GREEN),
         ("D", "R$ 60,00", "manteve o preço", RED), ("E", "R$ 75,00", "sinal trocado: aumento", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · VOCÊ FAZ", "O PREÇO DA MAIOR RECEITA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Um teatro de 500 lugares vende, em média, 300 ingressos por sessão ao preço de R$ 60,00. "
                           "Uma pesquisa indicou que, para cada R$ 1,00 de desconto no preço do ingresso, são vendidos 10 "
                           "ingressos a mais por sessão. Para que a receita por sessão seja a maior possível, o preço do "
                           "ingresso deve ser", INK)], a0, 236, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 260, 680, 40, C["25.ok"], "C", cues_in, cues_x, gap=40)
    if t < C["25"]:
        pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 110)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["25"], 0.4))
    aa = ep(t, C["25.a"], 0.4)
    if aa > 0:
        linha(c, [("x = DESCONTO", BLUE)], 540, y0 + 55, 28, aa)
        linha(c, [("R = ", INK), ("(60 − x)", AMBER), ("(300 + 10x)", PURPLE)], 540, y0 + 115, 34, aa)
        linha(c, [("R = −10x² + 300x + 18 000", INK)], 540, y0 + 175, 32, ep(t, C["25.a"] + 4.0, 0.4))
    ab = ep(t, C["25.b"], 0.4)
    if ab > 0:
        linha(c, [("xᵥ = −300 ÷ (−20) = ", INK), ("15", AMBER)], 540, y0 + 250, 34, ab)
        linha(c, [("raízes 60 e −30 → meio 15", INK2)], 540, y0 + 305, 26, ep(t, C["25.b"] + 2.6, 0.4))
    acc = ep(t, C["25.c"], 0.4)
    if acc > 0:
        linha(c, [("300 + 150 = 450 ≤ 500 lugares ", INK), ("✓", GREEN)], 540, y0 + 380, 30, acc)
    ad = ep(t, C["25.d"], 0.4)
    if ad > 0:
        linha(c, [("preço = 60 − 15 = ", INK), ("R$ 45,00", GREEN)], 540, y0 + 460, 36, ad)
        linha(c, [("receita: 45 · 450 = R$ 20.250", INK2)], 540, y0 + 525, 26, ep(t, C["25.d"] + 2.4, 0.4))
        check_icon(c, 250, y0 + 590, 20, ep(t, C["25.ok"], 0.4), GREEN)
        linha(c, [("pediram o PREÇO: R$ 45,00", GREEN)], 290, y0 + 592, 28, ep(t, C["25.ok"], 0.4), align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TRÊS FORMAS E ESTUDO DO SINAL", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        pl = Plano(360, 700, 560, 360, 40, 12)
        line(c, 330, 700, 950, 700, INK2, aa, 5)
        pl.curva(c, lambda x: 10 - (x - 20) ** 2 / 40, 0, 40, BLUE, aa, ep(t, C["28.a"], 1.4), 9)
        px, py = pl.P(20, 10)
        line(c, px, py, px, 700, AMBER, aa, 4)
        text(c, "10 m", px + 16, (py + 700) / 2, 28, "black", AMBER, aa, align="left")
        text(c, "40 m", 640, 760, 28, "black", INK2, aa)
        text_mid(c, "lei = ?", 640, 260, 48, "black", BLUE, ep(t, C["28.a"] + 2.0, 0.4))
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        rrect(c, 1080, 300, 560, 200, 26, "#FFFFFF", ab, shadow=True)
        text(c, "LUCRO > 0 ?", 1360, 390, 44, "black", GREEN, ab)
        text(c, "para que valores de x?", 1360, 450, 28, "bold", INK2, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        selo(c, 1360, 640, acc, "AS 3 FORMAS + O SINAL", PURPLE, -3, 36)


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Se você tivesse 60 metros de tela, o que cercaria?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, roteiro=b_roteiro, area=b_area,
              quadrado=b_quadrado, receita=b_receita, comando=b_comando, borda=b_borda, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q3=b_q3, q2=b_q2, ponte=b_ponte, cta=b_cta)
