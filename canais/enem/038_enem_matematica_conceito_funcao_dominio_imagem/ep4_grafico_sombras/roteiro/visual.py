"""Visual — Conceito de Função, Episódio 4: o gráfico (teste da reta vertical, domínio e imagem como sombras) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: Plano (eixos com grade e conversão de coordenadas), curva() (polilinha com progresso),
sombra_x()/sombra_y() (faixa no eixo com pontas fechadas), lanterna() (luz e raios até a sombra), regua() (régua vertical
deslizando), leitura() (tracejado do ponto até os eixos), celular() (o app de previsão do tempo).
Cores com função: azul = definição (e o chão/x) · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica (e a
parede/y) · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum038", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcoes_ep4_grafico_sombras.mp4"
CARD_R = K.CARD_R
CHAO = BLUE      # eixo x / domínio
PAREDE = GREEN   # eixo y / imagem


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


def num(v):
    """número com vírgula e sinal de menos tipográfico"""
    s = f"{v:g}".replace(".", ",")
    return s.replace("-", "−")


class Plano:
    """plano cartesiano num retângulo da tela: x em [x0, x1], y em [y0, y1]"""

    def __init__(self, bx, by, bw, bh, xr, yr):
        self.bx, self.by, self.bw, self.bh = bx, by, bw, bh
        self.xr, self.yr = xr, yr

    def P(self, x, y):
        (x0, x1), (y0, y1) = self.xr, self.yr
        return (self.bx + (x - x0) / (x1 - x0) * self.bw, self.by + self.bh - (y - y0) / (y1 - y0) * self.bh)

    def desenha(self, c, a, grade=True, nums=True, size=22, eixos_cor=(INK, INK), rot=True, destaque=None):
        """destaque = 'x' ou 'y' pinta o eixo correspondente (chão azul / parede verde) com espessura maior"""
        if a <= 0:
            return
        (x0, x1), (y0, y1) = self.xr, self.yr
        if grade:
            for k in range(math.ceil(x0), math.floor(x1) + 1):
                px, _ = self.P(k, 0)
                line(c, px, self.by, px, self.by + self.bh, "#E7E7E2", a, 2)
            for k in range(math.ceil(y0), math.floor(y1) + 1):
                _, py = self.P(0, k)
                line(c, self.bx, py, self.bx + self.bw, py, "#E7E7E2", a, 2)
        ox, oy = self.P(0, 0)
        cx_ = CHAO if destaque == "x" else eixos_cor[0]
        cy_ = PAREDE if destaque == "y" else eixos_cor[1]
        arrow(c, self.bx - 10, oy, self.bx + self.bw + 24, oy, cx_, a, 7 if destaque == "x" else 4, 16)
        arrow(c, ox, self.by + self.bh + 10, ox, self.by - 24, cy_, a, 7 if destaque == "y" else 4, 16)
        if rot:
            text(c, "x", self.bx + self.bw + 34, oy + 10, 30, "black", CHAO, a, align="left")
            text(c, "y", ox + 18, self.by - 14, 30, "black", PAREDE, a, align="left")
        if nums:
            for k in range(math.ceil(x0), math.floor(x1) + 1):
                if k == 0:
                    continue
                px, _ = self.P(k, 0)
                line(c, px, oy - 7, px, oy + 7, INK, a, 3)
                fmid(c, num(k), px, oy + size * 1.05, size, "bold", GRAY, a)
            for k in range(math.ceil(y0), math.floor(y1) + 1):
                if k == 0:
                    continue
                _, py = self.P(0, k)
                line(c, ox - 7, py, ox + 7, py, INK, a, 3)
                fmid(c, num(k), ox - size * 0.9, py, size, "bold", GRAY, a, align="right")
            fmid(c, "0", ox - size * 0.6, oy + size * 0.9, size * 0.9, "bold", GRAY, a)


def curva(c, pl, pts, col, a, width=7, prog_=1.0):
    """polilinha pelos pontos (em coordenadas do plano), desenhada até a fração prog_"""
    if a <= 0 or prog_ <= 0:
        return
    n = max(2, int(round(len(pts) * prog_)))
    p = skia.Path()
    for k, (x, y) in enumerate(pts[:n]):
        px, py = pl.P(x, y)
        (p.moveTo if k == 0 else p.lineTo)(px, py)
    c.drawPath(p, paint(col, a, stroke=width, cap_round=True))


def ponto(c, pl, x, y, a, col=None, r=11, rot=None, dx=0, dy=-34, size=26):
    if a <= 0:
        return
    px, py = pl.P(x, y)
    c.drawCircle(px, py, r + 4, paint("#FFFFFF", a))
    c.drawCircle(px, py, r, paint(col or INK, a))
    if rot:
        fmid(c, rot, px + dx, py + dy, size, "black", col or INK, a)


def sombra_x(c, pl, xa, xb, a, prog_=1.0, col=CHAO, rot=None, dy=58, size=30):
    """faixa no eixo x de xa a xb (pontas fechadas = incluídas)"""
    if a <= 0 or prog_ <= 0:
        return
    (px0, oy), (px1, _) = pl.P(xa, 0), pl.P(xb, 0)
    pe = lerp(px0, px1, prog_)
    rrect(c, px0 - 4, oy - 9, pe - px0 + 8, 18, 9, col, a * 0.85)
    c.drawCircle(px0, oy, 13, paint(col, a))
    if prog_ >= 1:
        c.drawCircle(px1, oy, 13, paint(col, a))
    if rot and prog_ >= 1:
        pill(c, rot, (px0 + px1) / 2, oy + dy, col, size=size, a=a, anchor="center", bounds=(0, 1920))


def sombra_y(c, pl, ya, yb, a, prog_=1.0, col=PAREDE, rot=None, dx=-70, size=30, anchor="right"):
    """faixa no eixo y de ya a yb (pontas fechadas = incluídas)"""
    if a <= 0 or prog_ <= 0:
        return
    (ox, py0), (_, py1) = pl.P(0, ya), pl.P(0, yb)
    pe = lerp(py0, py1, prog_)
    rrect(c, ox - 9, pe - 4, 18, py0 - pe + 8, 9, col, a * 0.85)
    c.drawCircle(ox, py0, 13, paint(col, a))
    if prog_ >= 1:
        c.drawCircle(ox, py1, 13, paint(col, a))
    if rot and prog_ >= 1:
        pill(c, rot, ox + dx, (py0 + py1) / 2, col, size=size, a=a, anchor=anchor, bounds=(0, 1920))


def lanterna(c, x, y, a, ang=90, s=1.0, raio=None):
    """lanterna apontando na direção ang (graus; 90 = para baixo, 180 = para a esquerda). raio = polígono iluminado."""
    if a <= 0:
        return
    if raio:
        p = skia.Path()
        p.moveTo(*raio[0])
        for q in raio[1:]:
            p.lineTo(*q)
        p.close()
        c.drawPath(p, paint("#FFE9A8", a * 0.42))
    c.save(); c.translate(x, y); c.rotate(ang - 90); c.scale(s, s)
    rrect(c, -22, -78, 44, 70, 10, "#4A4F5A", a, shadow=True)
    p = skia.Path()
    p.moveTo(-22, -10); p.lineTo(22, -10); p.lineTo(36, 22); p.lineTo(-36, 22); p.close()
    c.drawPath(p, paint("#2F333B", a))
    rrect(c, -36, 18, 72, 12, 6, "#FFD54A", a)
    c.restore()


def regua(c, px, y0, y1, a, col=PURPLE, w=26):
    """régua vertical em px, de y0 a y1"""
    if a <= 0:
        return
    rrect(c, px - w / 2, y0, w, y1 - y0, 6, mix("#FFFFFF", col, 0.25), a * 0.9, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(px - w / 2, y0, w, y1 - y0), paint(col, a, stroke=3))
    for k in range(int((y1 - y0) // 24)):
        yy = y0 + 12 + k * 24
        line(c, px - w / 2, yy, px - w / 2 + (12 if k % 2 else 7), yy, col, a, 2)
    line(c, px, y0, px, y1, col, a * 0.6, 2, dash=[8, 6])


def leitura(c, pl, x, y, a, prog_=1.0, ate_x=True, ate_y=True, rx=None, ry=None, size=34):
    """tracejados do ponto (x, y) até os eixos, com o valor lido no chão (azul) e na parede (verde)"""
    if a <= 0:
        return
    px, py = pl.P(x, y)
    ox, oy = pl.P(0, 0)
    if ate_x:
        line(c, px, py, px, oy, CHAO, a, 4, dash=[12, 9], progress=prog_)
        if rx and prog_ >= 1:
            fbox_ = rx
            rrect(c, px - ftext_w(fbox_, "black", size) / 2 - 12, oy + 22, ftext_w(fbox_, "black", size) + 24,
                  size * 1.5, 12, CHAO, a)
            fmid(c, fbox_, px, oy + 22 + size * 0.75, size, "black", "#FFFFFF", a)
    if ate_y:
        line(c, px, py, ox, py, PAREDE, a, 4, dash=[12, 9], progress=prog_)
        if ry and prog_ >= 1:
            ww = ftext_w(ry, "black", size) + 24
            rrect(c, ox - ww - 22, py - size * 0.75, ww, size * 1.5, 12, PAREDE, a)
            fmid(c, ry, ox - ww / 2 - 22, py, size, "black", "#FFFFFF", a)


# o gráfico da seção 07: sobe de (−1, 1) até (2, 4), desce passando por (4, 3) até x = 6
def F7(x):
    if x <= 2:
        return 4 - (2 - x) ** 2 / 3
    return 4 - ((x - 2) / 2) ** 1.2


PTS7 = [(-1 + 7 * k / 140, F7(-1 + 7 * k / 140)) for k in range(141)]
SEG_EX = [(0, 2), (3, 5), (6, -1)]
SEG_Q8 = [(-2, 1), (1, 4), (5, 0)]


def segs(pts_, n=60):
    out = []
    for (xa, ya), (xb, yb) in zip(pts_, pts_[1:]):
        for k in range(n):
            u = k / n
            out.append((lerp(xa, xb, u), lerp(ya, yb, u)))
    out.append(pts_[-1])
    return out


def plano7(bx=230, by=250, bw=760, bh=470):
    return Plano(bx, by, bw, bh, (-2, 7), (-1, 5))


def celular(c, cx, cy, w, h, a):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 46, "#1E2128", a, shadow=True)
    rrect(c, cx - w / 2 + 16, cy - h / 2 + 16, w - 32, h - 32, 34, "#F7F9FC", a)
    rrect(c, cx - 60, cy - h / 2 + 26, 120, 18, 9, "#1E2128", a)


def temp(h):
    return 23 + 5 * math.cos(2 * math.pi * (h - 14) / 24)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÕES · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    pl = plano7(260, 260, 760, 470)
    aa = ep(t, C["01.a"], 0.5)
    pl.desenha(c, aa)
    curva(c, pl, PTS7, PURPLE, aa, 7, ep(t, C["01.a"] + 0.3, 1.6))
    if aa > 0:
        text(c, "EM QUE INTERVALO A FUNÇÃO CRESCE?", 1390, 300, 34, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    sombra_y(c, pl, 1, 4, ab, ep(t, C["01.b"] + 0.3, 0.8), AMBER)
    if ab > 0:
        rrect(c, 1150, 400, 480, 110, 24, mix("#FFFFFF", AMBER, 0.25), ab)
        text_mid(c, "“entre 1 e 4”", 1390, 455, 48, "black", AMBER, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        strike(c, 1190, 455, 1590, 455, acc, RED, acc)
        selo(c, 1580, 400, acc, "ALTURA!", RED, -8, 30)
        sombra_x(c, pl, -1, 2, acc, ep(t, C["01.c"] + 0.6, 0.8))
        linha(c, [("cresce para ", INK), ("x", CHAO), (" entre −1 e 2", CHAO)], 1390, 610, 44, ep(t, C["01.c"] + 1.2, 0.4))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "não troque o x pela altura", 1390, 750, ad, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÕES · EP. 4", "AO FINAL DESTA AULA", GREEN)
    itens = [("02.a", "É FUNÇÃO?", PURPLE), ("02.b", "DOMÍNIO", CHAO), ("02.b", "IMAGEM", PAREDE),
             ("02.c", "MÁXIMO", INK), ("02.c", "SOBE · DESCE", INK)]
    for k, (cue, s, col) in enumerate(itens):
        ak = ep(t, C[cue] + (k % 2) * 0.8 * (cue != "02.a"), 0.4)
        if ak <= 0:
            continue
        x = 330 + k * 315
        rrect(c, x - 140, 380, 280, 200, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 140, 380, 280, 16, 8, col, ak)
        text_mid(c, s, x, 490, 34 if len(s) < 10 else 28, "black", col, ak)
    a0 = ep(t, C["02.a"], 0.5)
    if a0 > 0:
        pill(c, "olhando SÓ o gráfico", W / 2, 280, BLUE, size=30, a=a0, anchor="center")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    pl = Plano(260, 300, 480, 400, (0, 4), (0, 3))
    pl.desenha(c, aa, size=22)
    if aa > 0:
        text(c, "PAR ORDENADO (3, 2)", 500, 250, 36, "black", INK, aa)
        u1 = ep(t, C["03.a"] + 1.4, 0.8)
        u2 = ep(t, C["03.a"] + 2.4, 0.8)
        ox, oy = pl.P(0, 0)
        p3, _ = pl.P(3, 0)
        _, p2 = pl.P(0, 2)
        arrow(c, ox, oy - 2, p3, oy - 2, CHAO, u1, 7, 18, u1)
        arrow(c, p3, oy, p3, p2, PAREDE, u2, 7, 18, u2)
        ponto(c, pl, 3, 2, ep(t, C["03.a"] + 3.2, 0.3), INK, rot="(3, 2)")
        text(c, "1º anda na horizontal · 2º sobe", 500, 780, 26, "bold", INK2, u1)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        line(c, 960, 240, 960, 800, "#E6E6E2", ab, 3)
        text(c, "INTERVALO", 1380, 250, 36, "black", INK, ab)
        text(c, "série de Equações e inequações", 1380, 300, 24, "bold", GRAY, ab)
        fmid(c, "[−1, 6]", 1380, 420, 90, "black", PURPLE, ab)
        rl = Plano(1080, 520, 600, 1, (-2, 7), (0, 1))
        y = 560
        line(c, 1060, y, 1700, y, INK, ab, 4)
        for k in range(-2, 8):
            px, _ = rl.P(k, 0)
            line(c, px, y - 8, px, y + 8, INK, ab, 3)
            fmid(c, num(k), px, y + 32, 22, "bold", GRAY, ab)
        pa, _ = rl.P(-1, 0)
        pb, _ = rl.P(6, 0)
        rrect(c, pa, y - 8, pb - pa, 16, 8, PURPLE, ab)
        c.drawCircle(pa, y, 14, paint(PURPLE, ab)); c.drawCircle(pb, y, 14, paint(PURPLE, ab))
        pill(c, "colchete fechado: a ponta ENTRA", 1380, 680, PURPLE, size=26, a=ep(t, C["03.b"] + 2.4, 0.4),
             anchor="center")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "PREVISÃO DO TEMPO", "VOCÊ JÁ LÊ GRÁFICOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, B["start"], 0.5)
    celular(c, 620, 495, 760, 640, a0)
    pl = Plano(350, 330, 560, 330, (0, 24), (14, 30))
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        text(c, "Hoje", 300, 245, 30, "black", INK, aa, align="left")
        ox, oy = pl.P(0, 14)
        line(c, ox, oy, ox + 580, oy, INK, aa, 3)
        line(c, ox, oy, ox, pl.P(0, 30)[1] - 10, INK, aa, 3)
        for h in (0, 6, 12, 18, 24):
            px, _ = pl.P(h, 14)
            fmid(c, f"{h} h", px, oy + 28, 20, "bold", CHAO, aa)
        for v in (15, 20, 25, 30):
            _, py = pl.P(0, v)
            fmid(c, f"{v}°", ox - 30, py, 20, "bold", PAREDE, aa)
        text(c, "horas", 900, oy + 66, 24, "black", CHAO, aa, align="right")
        text(c, "°C", ox - 10, pl.P(0, 30)[1] - 22, 24, "black", PAREDE, aa)
        pts = [(h / 4, temp(h / 4)) for h in range(97)]
        p = skia.Path()
        for k, (x, y) in enumerate(pts):
            px, py = pl.P(x, y)
            (p.moveTo if k == 0 else p.lineTo)(px, py)
        c.drawPath(p, paint(AMBER, aa, stroke=6, cap_round=True))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 1120, 300, 540, 150, 24, mix("#FFFFFF", AMBER, 0.2), ab)
        para(c, "Qual foi a MÁXIMA? A que horas?", 1150, 360, 34, "black", INK, ab, 480)
    acc = ep(t, C["04.c"], 0.5)
    px, py = pl.P(14, 28)
    ox, oy = pl.P(0, 14)
    if acc > 0:
        c.drawCircle(px, py, 12, paint(INK, acc))
        line(c, px, py, ox, py, PAREDE, acc, 4, dash=[10, 8], progress=ep(t, C["04.c"] + 0.4, 0.8))
        rrect(c, 1120, 500, 540, 90, 20, mix("#FFFFFF", PAREDE, 0.15), acc)
        linha(c, [("lateral: ", INK2), ("28 °C", PAREDE)], 1390, 545, 44, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        line(c, px, py, px, oy, CHAO, ad, 4, dash=[10, 8], progress=ep(t, C["04.d"] + 0.3, 0.8))
        rrect(c, 1120, 620, 540, 90, 20, mix("#FFFFFF", CHAO, 0.12), ad)
        linha(c, [("embaixo: ", INK2), ("14 h", CHAO)], 1390, 665, 44, ad)
        pill(c, "você leu um gráfico", 1390, 780, GREEN, size=28, a=ep(t, C["04.d"] + 2.2, 0.4), anchor="center")


def b_plano(c, t, C, B):
    head(c, t, B["start"], "PLANO CARTESIANO", "O MÍNIMO PARA HOJE", BLUE)
    card(c, *CARD_R)
    pl = Plano(300, 260, 760, 470, (-2, 6), (-1, 4))
    aa = ep(t, C["05.a"], 0.5)
    ab = ep(t, C["05.b"], 0.5)
    pl.desenha(c, aa, destaque="x" if ab <= 0 else None)
    if aa > 0:
        ox, oy = pl.P(0, 0)
        pill(c, "eixo x = CHÃO", 1060, oy + 60, CHAO, size=28, a=aa, anchor="right")
        rrect(c, 1160, 280, 540, 120, 22, mix("#FFFFFF", CHAO, 0.10), aa)
        para(c, "eixo HORIZONTAL (x): a reta deitada", 1190, 335, 30, "black", CHAO, aa, 480)
    if ab > 0:
        ox, oy = pl.P(0, 0)
        line(c, ox, pl.by + pl.bh + 10, ox, pl.by - 10, PAREDE, ab, 8)
        pill(c, "eixo y = PAREDE", ox + 20, pl.by - 6, PAREDE, size=28, a=ab, anchor="left")
        rrect(c, 1160, 420, 540, 120, 22, mix("#FFFFFF", PAREDE, 0.12), ab)
        para(c, "eixo VERTICAL (y): a reta de pé", 1190, 475, 30, "black", PAREDE, ab, 480)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        leitura(c, pl, 4, 3, acc, ep(t, C["05.c"] + 0.3, 0.8))
        ponto(c, pl, 4, 3, acc, PURPLE, rot="(4, 3)")
        linha(c, [("ponto = (", INK), ("x", CHAO), (", ", INK), ("y", PAREDE), (")", INK)], 1430, 620, 50, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        pill(c, "série própria: Plano cartesiano", 1430, 740, PURPLE, size=26, a=ad, anchor="center")


# ======================================================================
# bloco a — o gráfico
# ======================================================================

def b_grafico(c, t, C, B):
    head(c, t, B["start"], "O GRÁFICO DE UMA FUNÇÃO", "OS PONTOS (x, f(x))", BLUE)
    card(c, *CARD_R)
    pl = Plano(300, 270, 620, 470, (-1, 4), (-1, 5))
    a0 = ep(t, B["start"], 0.4)
    pl.desenha(c, a0)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        linha(c, [("( ", INK), ("x", CHAO), (" , ", INK), ("f(x)", PAREDE), (" )", INK)], 1380, 300, 70, aa)
        text(c, "entrada · saída", 1380, 380, 28, "bold", INK2, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        linha(c, [("f(x) = x + 1", PURPLE)], 1380, 470, 46, ab)
    for k in range(3):
        ak = ep(t, C["06.b"] + 1.0 + k * 1.1, 0.4)
        if ak <= 0:
            continue
        ponto(c, pl, k, k + 1, ak, PURPLE, rot=f"({k}, {k + 1})", dx=-48, dy=-26, size=24)
        linha(c, [(f"f({k}) = {k + 1}", INK), ("  →  ", GRAY), (f"({k}, {k + 1})", PURPLE)], 1380, 550 + k * 60, 34, ak)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        curva(c, pl, [(-1 + 4.5 * u / 60, u * 4.5 / 60) for u in range(61)], PURPLE, acc, 6, ep(t, C["06.c"], 1.2))
        pill(c, "GRÁFICO = todos os pontos juntos", 610, 800, PURPLE, size=26, a=acc, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        px, py = pl.P(2, 3)
        ox, oy = pl.P(2, 0)
        arrow(c, px + 30, oy, px + 30, py, PAREDE, ad, 6, 16, ep(t, C["06.d"], 0.8))
        text(c, "altura = saída", px + 46, (py + oy) / 2 + 10, 28, "black", PAREDE, ad, align="left")


# ======================================================================
# bloco b — a régua em pé
# ======================================================================

def onda(x):
    return 2.2 + 1.3 * math.sin(x * 1.1) + 0.25 * x


PTS_ONDA = [(-0.5 + 5 * k / 120, onda(-0.5 + 5 * k / 120)) for k in range(121)]


def b_regua(c, t, C, B):
    head(c, t, B["start"], "É GRÁFICO DE FUNÇÃO?", "O TESTE DA RÉGUA EM PÉ", PURPLE)
    card(c, *CARD_R)
    pl = Plano(240, 280, 620, 440, (-1, 5), (-1, 5))
    pr = Plano(1060, 280, 620, 440, (-3, 3), (-3, 3))
    aa = ep(t, C["07.a"], 0.5)
    pl.desenha(c, aa, nums=False)
    curva(c, pl, PTS_ONDA, BLUE, aa, 7)
    if aa > 0 and t < C["07.c"]:
        u = ep(t, C["07.a"] + 0.6, 4.0)
        xx = lerp(-0.4, 4.4, u)
        px, _ = pl.P(xx, 0)
        regua(c, px, pl.by - 20, pl.by + pl.bh + 20, aa)
        qx, qy = pl.P(xx, onda(xx))
        c.drawCircle(qx, qy, 14, paint(GREEN, aa))
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        badge_num(c, 1, 560, 780, ab, 26, bg=GREEN)
        text(c, "toca 1 vez: É FUNÇÃO", 600, 792, 32, "black", GREEN, ab, align="left")
    acc = ep(t, C["07.c"], 0.5)
    pr.desenha(c, acc, nums=False)
    if acc > 0:
        cx, cy = pr.P(0, 0)
        r = pr.P(2.2, 0)[0] - cx
        c.drawCircle(cx, cy, r, paint(BLUE, acc, stroke=7))
    ad = ep(t, C["07.d"], 0.5)
    if acc > 0:
        u = ep(t, C["07.c"] + 0.5, 2.0)
        xx = lerp(-2.6, 1.0, u)
        px, _ = pr.P(xx, 0)
        regua(c, px, pr.by - 20, pr.by + pr.bh + 20, acc)
        if ad > 0 and abs(xx) < 2.2:
            yy = math.sqrt(2.2 ** 2 - xx ** 2)
            pis = 0.5 + 0.5 * math.sin((t - C["07.d"]) * 9)
            for s_ in (1, -1):
                qx, qy = pr.P(xx, s_ * yy)
                c.drawCircle(qx, qy, 16 + 6 * pis, paint(RED, ad))
            badge_num(c, 2, 1360, 780, ad, 26, bg=RED)
            text(c, "toca 2 vezes!", 1400, 792, 32, "black", RED, ad, align="left")


def b_regua2(c, t, C, B):
    head(c, t, B["start"], "POR QUE ESTRAGA?", "UM x, DUAS SAÍDAS", RED)
    card(c, *CARD_R)
    pr = Plano(240, 260, 560, 500, (-3, 3), (-3, 3))
    a0 = ep(t, B["start"], 0.4)
    pr.desenha(c, a0, nums=False)
    cx, cy = pr.P(0, 0)
    r = pr.P(2.2, 0)[0] - cx
    c.drawCircle(cx, cy, r, paint(BLUE, a0, stroke=7))
    xx = 1.0
    yy = math.sqrt(2.2 ** 2 - xx ** 2)
    px, _ = pr.P(xx, 0)
    regua(c, px, pr.by - 20, pr.by + pr.bh + 20, a0)
    aa = ep(t, C["08.a"], 0.5)
    for s_, rot in ((1, "em cima"), (-1, "embaixo")):
        qx, qy = pr.P(xx, s_ * yy)
        c.drawCircle(qx, qy, 16, paint(RED, a0))
        if aa > 0:
            text(c, rot, qx + 30, qy + 10, 28, "black", RED, aa, align="left")
    if aa > 0:
        pill(c, "o MESMO x", px, pr.P(0, -3)[1] + 50, CHAO, size=26, a=aa, anchor="center")
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        x0, y0 = 1080, 330
        rrect(c, x0, y0, 600, 300, 26, "#FFFFFF", ab, shadow=True)
        fmid(c, "x", x0 + 120, y0 + 150, 64, "black", CHAO, ab)
        for k, s_ in enumerate(("saída 1", "saída 2")):
            yk = y0 + 90 + k * 120
            arrow(c, x0 + 170, y0 + 150, x0 + 380, yk, RED, ab, 6, 18, ep(t, C["08.b"] + 0.3 + k * 0.4, 0.5))
            text_mid(c, s_, x0 + 400, yk, 34, "black", RED, ab, align="left")
        text(c, "“duas flechas saindo” · ep. 1", x0 + 300, y0 + 350, 26, "bold", INK2, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        selo(c, 1380, 740, acc, "NÃO É FUNÇÃO", RED, -4, 40)
        pill(c, "TESTE DA RETA VERTICAL", 1380, 830, PURPLE, size=26, a=ep(t, C["08.c"] + 1.4, 0.4), anchor="center")


# ======================================================================
# bloco c — horizontal pode
# ======================================================================

def U(x):
    return (x - 2) ** 2 / 1.5 + 0.5


PTS_U = [(-0.4 + 4.8 * k / 120, U(-0.4 + 4.8 * k / 120)) for k in range(121)]


def b_horizontal(c, t, C, B):
    head(c, t, B["start"], "E A RÉGUA DEITADA?", "HORIZONTAL PODE CORTAR VÁRIAS VEZES", BLUE)
    card(c, *CARD_R)
    pl = Plano(260, 270, 700, 470, (-1, 5), (-1, 5))
    a0 = ep(t, B["start"], 0.4)
    pl.desenha(c, a0)
    curva(c, pl, PTS_U, BLUE, a0, 7)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        _, py = pl.P(0, U(1))
        line(c, pl.bx, py, lerp(pl.bx, pl.bx + pl.bw, ep(t, C["09.a"] + 0.3, 0.8)), py, AMBER, aa, 7)
        for xk in (1, 3):
            ponto(c, pl, xk, U(xk), ep(t, C["09.a"] + 1.0, 0.3), AMBER, r=13)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        for xk in (1, 3):
            leitura(c, pl, xk, U(xk), ab, 1.0, True, False, rx=f"x = {xk}", size=28)
        rrect(c, 1100, 320, 580, 150, 24, "#FFFFFF", ab, shadow=True)
        para(c, "dois x diferentes, a MESMA altura", 1130, 380, 34, "black", INK, ab, 520)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        x0, y0 = 1170, 520
        for k, s_ in enumerate(("x = 1", "x = 3")):
            yk = y0 + k * 100
            fmid(c, s_, x0 + 60, yk, 34, "black", CHAO, acc)
            arrow(c, x0 + 130, yk, x0 + 300, y0 + 50, GREEN, acc, 6, 18, ep(t, C["09.c"] + 0.3, 0.5))
        fmid(c, "mesma saída", x0 + 320, y0 + 50, 32, "black", PAREDE, acc, align="left")
        text(c, "duas flechas CHEGANDO: pode", x0 + 255, y0 + 200, 30, "black", GREEN, acc)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        u = ep(t, C["09.d"], 1.8)
        xx = lerp(-0.3, 4.3, u)
        px, _ = pl.P(xx, 0)
        regua(c, px, pl.by - 20, pl.by + pl.bh + 20, ad)
        qx, qy = pl.P(xx, U(xx))
        c.drawCircle(qx, qy, 13, paint(GREEN, ad))
        selo(c, 610, 820, ad, "É FUNÇÃO", GREEN, -4, 34)


def b_atalho1(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "RÉGUA EM PÉ, NUNCA DEITADA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 260, 220, 1400, 170, "ATALHO", ["RÉGUA EM PÉ, NUNCA DEITADA"], aa, 52)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 450, 620, 330, 28, mix("#FFFFFF", GREEN, 0.12), ab)
        regua(c, 420, 480, 750, ab, GREEN)
        para(c, "deslize pelo gráfico INTEIRO", 480, 560, 32, "black", INK, ab, 420)
        para(c, "tocou 2 vezes? NÃO É FUNÇÃO", 480, 670, 32, "black", RED, ep(t, C["10.b"] + 1.6, 0.4), 420)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 450, 620, 330, 28, "#F1F1EE", acc)
        c.save(); c.translate(1310, 560); c.rotate(-90)
        regua(c, 0, -230, 230, acc, GRAY)
        c.restore()
        text(c, "deitada: NÃO DECIDE", 1310, 700, 38, "black", GRAY, acc)


# ======================================================================
# bloco d — as sombras
# ======================================================================

def b_sombras(c, t, C, B):
    sid = which(t, C, ["11", "12"])
    head(c, t, C[sid], "DOMÍNIO E IMAGEM", "AS SOMBRAS DA CURVA", BLUE)
    card(c, *CARD_R)
    pl = plano7(250, 300, 760, 440)
    a0 = ep(t, C["11"], 0.4)
    pl.desenha(c, a0)
    curva(c, pl, PTS7, PURPLE, a0, 7, ep(t, C["11"], 1.0))
    # lanterna em cima
    aa = ep(t, C["11.a"], 0.5)
    lan_a = aa * (1 - ep(t, C["12.a"], 0.5)) if sid == "12" else aa
    (xa, oy), (xb, _) = pl.P(-1, 0), pl.P(6, 0)
    if lan_a > 0:
        lx, ly = (xa + xb) / 2, 236
        lanterna(c, lx, ly, lan_a, 90, 0.9, raio=[(lx - 26, ly + 22), (lx + 26, ly + 22), (xb + 30, oy), (xa - 30, oy)])
    curva(c, pl, PTS7, PURPLE, a0, 7)
    ab = ep(t, C["11.b"], 0.5)
    sombra_x(c, pl, -1, 6, ab, ep(t, C["11.b"] + 0.2, 1.2), rot="[−1, 6]" if t >= C["11.c"] else None)
    if ab > 0:
        rrect(c, 1290, 300, 420, 110, 22, mix("#FFFFFF", CHAO, 0.10), ab)
        para(c, "PROJEÇÃO = a sombra num eixo", 1315, 345, 28, "black", CHAO, ab, 380)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        linha(c, [("DOMÍNIO = ", INK), ("[−1, 6]", CHAO)], 1500, 480, 46, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        pill(c, "domínio = sombra no CHÃO", 1500, 560, CHAO, size=28, a=ad, anchor="center")
    if sid != "12":
        return
    ba = ep(t, C["12.a"], 0.5)
    (ox, py1), (_, py4) = pl.P(0, 1), pl.P(0, 4)
    if ba > 0:
        lx, ly = pl.bx + pl.bw + 95, (py1 + py4) / 2
        lanterna(c, lx, ly, ba, 180, 0.9, raio=[(lx - 22, ly - 26), (lx - 22, ly + 26), (ox, py1 + 30), (ox, py4 - 30)])
        curva(c, pl, PTS7, PURPLE, ba, 7)
    bb = ep(t, C["12.b"], 0.5)
    sombra_y(c, pl, 1, 4, bb, ep(t, C["12.b"], 1.0), rot="[1, 4]" if bb >= 1 else None, dx=-40)
    if bb > 0:
        linha(c, [("IMAGEM = ", INK), ("[1, 4]", PAREDE)], 1500, 650, 46, bb)
    bc = ep(t, C["12.c"], 0.5)
    if bc > 0:
        ponto(c, pl, 2, 4, bc, PAREDE, r=14, rot="mais alto: no MEIO", dy=-40, size=26)
    bd = ep(t, C["12.d"], 0.5)
    if bd > 0:
        ponto(c, pl, -1, 1, bd, PAREDE, r=14, rot="mais baixo", dx=20, dy=40, size=24)
        pill(c, "do MAIS BAIXO ao MAIS ALTO", 1500, 740, PAREDE, size=26, a=bd, anchor="center")


# ======================================================================
# bloco e — a tabela de leitura
# ======================================================================

LEIT = [("MÁXIMO", "4", "x = 2"), ("MÍNIMO", "1", "x = −1"), ("CRESCE", "", "[−1, 2]"), ("DECRESCE", "", "[2, 6]"),
        ("ZEROS", "", "não há"), ("f(4)", "3", "")]


def _tabela_leit(c, t, linhas, a):
    """quadro à direita: pergunta · parede (y) · chão (x). linhas = [(índice, alfa)]"""
    x0, y0, w = 1150, 250, 560
    if a <= 0:
        return
    rrect(c, x0, y0, w, 60, 14, PURPLE, a)
    text_mid(c, "PERGUNTA", x0 + 110, y0 + 30, 22, "black", "#FFFFFF", a)
    text_mid(c, "PAREDE (y)", x0 + 300, y0 + 30, 22, "black", "#FFFFFF", a)
    text_mid(c, "CHÃO (x)", x0 + 470, y0 + 30, 22, "black", "#FFFFFF", a)
    for k, ak in linhas:
        if ak <= 0:
            continue
        nome, vy, vx = LEIT[k]
        y = y0 + 60 + k * 82
        rrect(c, x0, y, w, 82, 0, "#FFFFFF" if k % 2 else "#F4F4F1", ak)
        text_mid(c, nome, x0 + 110, y + 41, 28, "black", INK, ak)
        fmid(c, vy, x0 + 300, y + 41, 34, "black", PAREDE, ak)
        fmid(c, vx, x0 + 470, y + 41, 30 if len(vx) > 5 else 34, "black", CHAO if vx != "não há" else GRAY, ak)


def b_leitura(c, t, C, B):
    sid = which(t, C, ["13", "14", "15"])
    tit = {"13": ("MÁXIMO E MÍNIMO", "A MAIOR E A MENOR ALTURA"), "14": ("CRESCE E DECRESCE", "DA ESQUERDA PARA A DIREITA"),
           "15": ("ZEROS E f(a)", "TOCAR O CHÃO · LER A ALTURA")}[sid]
    head(c, t, C[sid], tit[0], tit[1], BLUE)
    card(c, *CARD_R)
    pl = plano7(230, 290, 800, 440)
    a0 = ep(t, C["13"], 0.4)
    pl.desenha(c, a0)
    curva(c, pl, PTS7, PURPLE, a0, 7)
    linhas = []
    # 13 — máximo e mínimo
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            pill(c, "MÁXIMO = maior altura · MÍNIMO = menor altura", 630, 240, BLUE, size=24, a=aa, anchor="center")
        ab = ep(t, C["13.b"], 0.5)
        leitura(c, pl, 2, 4, ab, ep(t, C["13.b"] + 0.2, 0.8), rx="2", ry="4", size=28)
        ponto(c, pl, 2, 4, ab, PAREDE, r=13)
        acc = ep(t, C["13.c"], 0.5)
        leitura(c, pl, -1, 1, acc, ep(t, C["13.c"] + 0.2, 0.8), rx="−1", ry="1", size=28)
        ponto(c, pl, -1, 1, acc, PAREDE, r=13)
        linhas = [(0, ep(t, C["13.b"] + 1.4, 0.4)), (1, ep(t, C["13.c"] + 1.4, 0.4))]
    else:
        linhas = [(0, 1.0), (1, 1.0)]
    # 14 — cresce e decresce
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            u = ep(t, C["14.a"] + 0.3, 2.4)
            xx = lerp(-1, 6, u)
            qx, qy = pl.P(xx, F7(xx))
            c.drawCircle(qx, qy, 16, paint(AMBER, aa))
            pill(c, "leia como quem ANDA →", 630, 240, AMBER, size=24, a=aa, anchor="center")
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            curva(c, pl, [p for p in PTS7 if p[0] <= 2], GREEN, ab, 10)
            sombra_x(c, pl, -1, 2, ab, ep(t, C["14.b"] + 0.3, 0.8), CHAO)
            text(c, "SOBE", pl.P(0.3, 3.6)[0] - 30, pl.P(0.3, 3.6)[1], 30, "black", GREEN, ab)
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            curva(c, pl, [p for p in PTS7 if p[0] >= 2], RED, acc, 10)
            text(c, "DESCE", pl.P(4.6, 3.3)[0] + 30, pl.P(4.6, 3.3)[1] - 26, 30, "black", RED, acc)
        ad = ep(t, C["14.d"], 0.5)
        sombra_x(c, pl, 2, 6, ad, ep(t, C["14.d"] + 0.3, 0.8), PURPLE)
        linhas += [(2, ep(t, C["14.b"] + 1.4, 0.4)), (3, ep(t, C["14.d"] + 1.4, 0.4))]
    elif sid == "15":
        linhas += [(2, 1.0), (3, 1.0)]
    # 15 — zeros e f(4)
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            ox, oy = pl.P(0, 0)
            line(c, pl.bx, oy, pl.bx + pl.bw, oy, AMBER, aa * (1 - ep(t, C["15.c"], 0.4)), 9)
            pill(c, "ZERO (raiz): onde a curva TOCA o chão", 630, 240, AMBER, size=24, a=aa * (1 - ep(t, C["15.c"], 0.3)),
                 anchor="center")
        ab = ep(t, C["15.b"], 0.5)
        if ab > 0:
            selo(c, 630, 800, ab, "NÃO TOCA: SEM ZEROS", AMBER, -3, 28)
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            pill(c, "f(4) = ?", 630, 240, PURPLE, size=26, a=ep(t, C["15.c"] + 0.3, 0.4), anchor="center")
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            px, oy = pl.P(4, 0)
            _, py = pl.P(4, 3)
            ox, _ = pl.P(0, 0)
            u1 = ep(t, C["15.d"], 0.9)
            u2 = ep(t, C["15.d"] + 1.0, 0.9)
            arrow(c, px, oy, px, py, CHAO, ad, 5, 16, u1)
            arrow(c, px, py, ox, py, PAREDE, u2, 5, 16, u2)
            ponto(c, pl, 4, 3, u2, PAREDE, r=12)
            if u2 >= 1:
                rrect(c, ox - 70, py - 24, 52, 48, 12, PAREDE, ad)
                fmid(c, "3", ox - 44, py, 32, "black", "#FFFFFF", ad)
        linhas += [(4, ep(t, C["15.b"] + 0.6, 0.4)), (5, ep(t, C["15.d"] + 2.4, 0.4))]
    _tabela_leit(c, t, linhas, a0)


# ======================================================================
# bloco f — crescimento se dá em x
# ======================================================================

def b_emx(c, t, C, B):
    head(c, t, B["start"], "ONDE CRESCE?", "A RESPOSTA ESTÁ NO CHÃO", BLUE)
    card(c, *CARD_R)
    pl = plano7(260, 280, 780, 450)
    a0 = ep(t, B["start"], 0.4)
    pl.desenha(c, a0)
    curva(c, pl, PTS7, PURPLE, a0, 7)
    curva(c, pl, [p for p in PTS7 if p[0] <= 2], GREEN, a0, 10)
    aa = ep(t, C["16.a"], 0.5)
    sombra_y(c, pl, 1, 4, aa, 1.0, AMBER)
    if aa > 0:
        rrect(c, 1170, 300, 520, 150, 24, mix("#FFFFFF", AMBER, 0.22), aa)
        text_mid(c, "“cresce entre 1 e 4”", 1430, 350, 38, "black", AMBER, aa)
        text_mid(c, "1 e 4 são ALTURAS (parede)", 1430, 410, 26, "bold", INK2, aa)
        ax = ep(t, C["16.a"] + 2.6, 0.4)
        strike(c, 1200, 350, 1660, 350, ax, RED, ax)
    ab = ep(t, C["16.b"], 0.5)
    sombra_x(c, pl, -1, 2, ab, ep(t, C["16.b"] + 0.2, 0.8))
    if ab > 0:
        rrect(c, 1170, 490, 520, 150, 24, mix("#FFFFFF", CHAO, 0.12), ab)
        text_mid(c, "cresce para x entre −1 e 2", 1430, 540, 34, "black", CHAO, ab)
        check_icon(c, 1430, 600, 24, ab, GREEN)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        selo(c, 1430, 750, acc, "DISTRATOR FREQUENTE", AMBER, -4, 32)


def b_atalho2(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "QUANDO OU QUANTO?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    K.atalho(c, 260, 210, 1400, 150, "ATALHO", ["é pergunta de QUANDO ou de QUANTO?"], aa, 44)
    for k, (cue, tit, onde, col, exs) in enumerate((
            ("17.b", "QUANDO?", "CHÃO · eixo x", CHAO, ["onde cresce?", "em que x acontece?"]),
            ("17.c", "QUANTO?", "PAREDE · eixo y", PAREDE, ["qual é o máximo?", "quanto vale f(4)?"]))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 300 + k * 680
        rrect(c, x, 400, 640, 330, 28, mix("#FFFFFF", col, 0.12), ak, shadow=True)
        text(c, tit, x + 320, 470, 54, "black", col, ak)
        pill(c, onde, x + 320, 525, col, size=26, a=ak, anchor="center")
        for j, s_ in enumerate(exs):
            text(c, "• " + s_, x + 70, 610 + j * 56, 32, "bold", INK, ak, align="left")
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        regra(c, "diga o EIXO antes do NÚMERO", W / 2, 790, ad, 36)


# ======================================================================
# eu faço
# ======================================================================

EUF = [("18.a", "DOMÍNIO", "chão", "[−1, 6]", CHAO), ("18.b", "IMAGEM", "parede", "[1, 4]", PAREDE),
       ("18.c", "MÁXIMO", "parede 4", "chão 2", INK), ("18.c", "MÍNIMO", "parede 1", "chão −1", INK),
       ("18.d", "CRESCE", "chão", "[−1, 2]", CHAO), ("18.d", "DECRESCE", "chão", "[2, 6]", CHAO)]


def b_eufaco(c, t, C, B):
    head(c, t, B["start"], "EU FAÇO", "O GRÁFICO INTEIRO EM VOZ ALTA", BLUE)
    card(c, *CARD_R)
    pl = plano7(230, 290, 760, 440)
    a0 = ep(t, B["start"], 0.4)
    pl.desenha(c, a0)
    curva(c, pl, PTS7, PURPLE, a0, 7)
    sombra_x(c, pl, -1, 6, ep(t, C["18.a"], 0.5), ep(t, C["18.a"] + 0.2, 0.8))
    sombra_y(c, pl, 1, 4, ep(t, C["18.b"], 0.5), ep(t, C["18.b"] + 0.2, 0.8))
    ac = ep(t, C["18.c"], 0.5)
    ponto(c, pl, 2, 4, ac, PAREDE, r=12)
    ponto(c, pl, -1, 1, ep(t, C["18.c"] + 2.6, 0.4), PAREDE, r=12)
    vistos = {}
    for k, (cue, nome, eixo, val, col) in enumerate(EUF):
        vistos[cue] = vistos.get(cue, -1) + 1
        ak = ep(t, C[cue] + vistos[cue] * 2.6, 0.4)
        if ak <= 0:
            continue
        y = 270 + k * 88
        rrect(c, 1080, y, 600, 76, 16, "#FFFFFF" if k % 2 else "#F4F4F1", ak)
        text_mid(c, nome, 1180, y + 38, 26, "black", INK, ak)
        text_mid(c, eixo, 1370, y + 38, 26, "bold", INK2, ak)
        fmid(c, val, 1580, y + 38, 30, "black", col, ak)
    a5 = ep(t, C["18.d"] + 4.0, 0.4)
    if a5 > 0:
        pill(c, "sempre o EIXO antes do número", 1380, 820, GREEN, size=24, a=a5, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "AS DUAS SOMBRAS", GREEN)])
    card(c, *CARD_R)
    pl = Plano(260, 270, 720, 480, (-1, 7), (-2, 6))
    aa = ep(t, C["19.a"], 0.5)
    pl.desenha(c, aa)
    curva(c, pl, segs(SEG_EX), PURPLE, aa, 7, ep(t, C["19.a"] + 0.4, 2.4))
    for k, (x, y) in enumerate(SEG_EX):
        ponto(c, pl, x, y, ep(t, C["19.a"] + 0.6 + k * 1.2, 0.3), PURPLE, r=12, rot=f"({num(x)}, {num(y)})",
              dx=(78 if k == 0 else 0), dy=(-34 if k == 1 else 34 if k == 2 else -26), size=26)
    if aa > 0:
        pill(c, "pontas incluídas", 620, 230, PURPLE, size=24, a=aa, anchor="center")
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        linha(c, [("DOMÍNIO = ", INK), ("?", CHAO)], 1380, 330, 50, ab)
        linha(c, [("IMAGEM = ", INK), ("?", PAREDE)], 1380, 420, 50, ab)
    pause_timer(c, t, C["19.end"] - 1.9, 1380, 600)
    if t < C["20"]:
        return
    a1 = ep(t, C["20.a"], 0.5)
    sombra_x(c, pl, 0, 6, a1, ep(t, C["20.a"] + 0.2, 0.8))
    if a1 > 0:
        rrect(c, 1180, 290, 400, 80, 18, "#FFFFFF", a1)
        linha(c, [("DOMÍNIO = ", INK), ("[0, 6]", CHAO)], 1380, 330, 46, ep(t, C["20.a"] + 1.4, 0.4))
    a2 = ep(t, C["20.b"], 0.5)
    if a2 > 0:
        ponto(c, pl, 3, 5, a2, PAREDE, r=14)
        leitura(c, pl, 3, 5, a2, ep(t, C["20.b"], 0.6), False, True)
        a2b = ep(t, C["20.b"] + 2.4, 0.4)
        ponto(c, pl, 6, -1, a2b, PAREDE, r=14)
        leitura(c, pl, 6, -1, a2b, ep(t, C["20.b"] + 2.4, 0.6), False, True)
        text(c, "mais alto: 5 (no meio)", 1380, 520, 30, "black", PAREDE, a2)
        text(c, "mais baixo: −1 (na ponta)", 1380, 570, 30, "black", PAREDE, a2b)
    a3 = ep(t, C["20.c"], 0.5)
    sombra_y(c, pl, -1, 5, a3, ep(t, C["20.c"], 0.8))
    if a3 > 0:
        rrect(c, 1180, 380, 400, 80, 18, "#FFFFFF", a3)
        linha(c, [("IMAGEM = ", INK), ("[−1, 5]", PAREDE)], 1380, 420, 46, a3)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Régua em pé tocando duas vezes: não é função.",
          "Domínio é a sombra no chão; imagem é a sombra na parede.",
          "Cresce e decresce se responde em x."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Ler a IMAGEM no eixo x", "o eixo x é o primeiro que a gente olha",
          "imagem são as saídas, as alturas: ela mora na PAREDE (eixo y)"),
         ("Achar que a imagem vai de uma PONTA à outra do gráfico", "as pontas são os pontos que mais chamam a atenção",
          "no nosso exercício daria [−1, 2], mas o 5 está no meio: o máximo pode estar NO MEIO"),
         ("Responder o intervalo de crescimento com valores de y", "o que SOBE é a altura",
          "a pergunta é ONDE sobe: é de QUANDO, responde-se no x"),
         ("Achar que uma HORIZONTAL cortando duas vezes desqualifica a função", "dois cortes lembra o teste da régua",
          "o teste vale só para a régua EM PÉ; deitada = flechas chegando: PODE")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25"], ERROS)


# ======================================================================
# questão 8 (você faz)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS8 = [("A", "[−2, 5]", "é o DOMÍNIO (chão)", RED), ("B", "[1, 4]", "só o 1º segmento", RED),
         ("C", "[0, 5]", "y mais baixo + x mais à direita", RED), ("D", "[−2, 4]", "x mais à esquerda + y mais alto", RED),
         ("E", "[0, 4]", "", GREEN)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · VOCÊ FAZ", "IMAGEM A PARTIR DO GRÁFICO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    painel = t >= C["27"]
    ae = a0 * (1 - ep(t, C["27"], 0.4))
    yend = _enunciado(c, [("O gráfico de uma função f é formado por dois segmentos de reta: o primeiro liga os pontos "
                           "(−2, 1) e (1, 4); o segundo liga (1, 4) e (5, 0). As extremidades pertencem ao gráfico.", INK),
                          ("A imagem de f é o intervalo", INK)], ae, 250, 28, 720)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, ae, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS8, 1080, 250, 600, 40, C["27.ok"], "E", cues_in, cues_x, gap=34)
    if not painel:
        pause_timer(c, t, C["26.end"] - 1.9, 540, yend + 150)
        return
    ap = ep(t, C["27"], 0.4)
    pl = Plano(240, 260, 640, 480, (-3, 6), (-1, 5))
    pl.desenha(c, ap)
    curva(c, pl, segs(SEG_Q8), PURPLE, ap, 7, ep(t, C["27"], 1.2))
    for k, (x, y) in enumerate(SEG_Q8):
        ponto(c, pl, x, y, ap, PURPLE, r=11, rot=f"({num(x)}, {num(y)})", dx=-58 if k == 0 else 0,
              dy=(-4 if k == 0 else -32 if k == 1 else 34), size=24)
    aa = ep(t, C["27.a"], 0.5)
    if aa > 0 and t < C["28"]:
        pill(c, "QUANTO? → PAREDE", 560, 220, PAREDE, size=24, a=aa, anchor="center")
    ab = ep(t, C["27.b"], 0.5)
    leitura(c, pl, 1, 4, ab, ep(t, C["27.b"], 0.6), False, True)
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        qx, qy = pl.P(-2, 1)
        selo(c, qx + 40, qy + 60, acc * (1 - ep(t, C["27.c"] + 2.2, 0.3)), "NÃO É O 1", AMBER, -6, 22)
        leitura(c, pl, 5, 0, ep(t, C["27.c"] + 2.2, 0.4), 1.0, False, True)
        ponto(c, pl, 5, 0, ep(t, C["27.c"] + 2.2, 0.4), RED, r=14)
    ad = ep(t, C["27.d"], 0.5)
    sombra_y(c, pl, 0, 4, ad, ep(t, C["27.d"], 0.8))
    if ad >= 1:
        linha(c, [("IMAGEM = ", INK), ("[0, 4]", PAREDE)], 560, 800, 40, ad)
    if t >= C["28"]:
        a8 = ep(t, C["28.xa"], 0.5)
        sombra_x(c, pl, -2, 5, a8, ep(t, C["28.xa"], 0.8), CHAO)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DOMÍNIO PELA FÓRMULA E PELO CONTEXTO", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 1400, 90, 24, mix("#FFFFFF", PURPLE, 0.10), aa)
        text_mid(c, "sem gráfico, só a FÓRMULA?", W / 2, 285, 40, "black", PURPLE, aa)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        linha(c, [("f(x) = ", PURPLE)], 470, 520, 64, ab)
        K.fr(c, "1", "x − 3", 690, 520, 64, PURPLE, ab)
        rrect(c, 340, 650, 560, 90, 20, mix("#FFFFFF", AMBER, 0.25), ab)
        text_mid(c, "por que o 3 não pode entrar?", 620, 695, 32, "black", AMBER, ab)
    acc = ep(t, C["30.c"], 0.5)
    if acc > 0:
        # caixa de papelão
        x0, y0 = 1180, 430
        p = skia.Path()
        p.moveTo(x0, y0); p.lineTo(x0 + 300, y0); p.lineTo(x0 + 380, y0 - 70); p.lineTo(x0 + 80, y0 - 70); p.close()
        c.drawPath(p, paint("#E8C48C", acc))
        rrect(c, x0, y0, 300, 190, 0, "#D9A55B", acc)
        p2 = skia.Path()
        p2.moveTo(x0 + 300, y0); p2.lineTo(x0 + 380, y0 - 70); p2.lineTo(x0 + 380, y0 + 120); p2.lineTo(x0 + 300, y0 + 190)
        p2.close()
        c.drawPath(p2, paint("#C08A45", acc))
        fmid(c, "x", x0 + 150, y0 + 95, 54, "black", "#FFFFFF", acc)
        rrect(c, 1060, 650, 600, 90, 20, mix("#FFFFFF", AMBER, 0.25), acc)
        text_mid(c, "por que x não passa de 10 cm?", 1360, 695, 32, "black", AMBER, acc)
    pill(c, "ep. 5 · domínio pela fórmula e pelo contexto", W / 2, 810, PURPLE, size=30, a=ep(t, C["30.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Qual gráfico do seu dia a dia você mais olha?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, plano=b_plano, grafico=b_grafico,
              regua=b_regua, regua2=b_regua2, horizontal=b_horizontal, atalho1=b_atalho1, sombras=b_sombras,
              leitura=b_leitura, emx=b_emx, atalho2=b_atalho2, eufaco=b_eufaco, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q8=b_q8, ponte=b_ponte, cta=b_cta)
