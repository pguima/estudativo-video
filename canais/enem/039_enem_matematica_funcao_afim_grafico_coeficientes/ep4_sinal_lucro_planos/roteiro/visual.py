"""Visual — Função Afim, Episódio 4: estudo do sinal, custo, receita, lucro e comparação de planos (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: reta_sinal() (reta numérica com o zero marcado e os lados "−" e "+" acendendo), plano() (eixos com
grade leve e conversão de coordenadas), grafico_equilibrio() (receita saindo da origem, custo saindo de R$ 2.000,00, faixas
vermelha de prejuízo e verde de lucro, selo "200 peças: empate"), corrida() (as duas retas dos aplicativos se cruzando),
linha() (texto com cor por trecho, mantém o espaço de milhar).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/lucro · vermelho = erro/prejuízo.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum039", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_afim_ep4_sinal_lucro_planos.mp4"
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


def reta_sinal(c, cx, cy, w, a, zero, aL=0.0, aR=0.0, sL="−", sR="+", cL=None, cR=None, aberto=False, rot_zero=None):
    """reta numérica com o zero da função no meio; aL/aR acendem os lados com os sinais sL/sR (cores cL/cR).
    aberto=True desenha a bolinha vazia (desigualdade estrita)."""
    if a <= 0:
        return
    cL = cL or (RED if sL == "−" else GREEN)
    cR = cR or (GREEN if sR == "+" else RED)
    x0, x1 = cx - w / 2, cx + w / 2
    if aL > 0:
        rrect(c, x0, cy - 14, w / 2, 28, 14, cL, a * aL * 0.85)
        text_mid(c, sL, cx - w / 4, cy - 70, 90, "black", cL, a * aL)
    if aR > 0:
        rrect(c, cx, cy - 14, w / 2, 28, 14, cR, a * aR * 0.85)
        text_mid(c, sR, cx + w / 4, cy - 70, 90, "black", cR, a * aR)
    line(c, x0 - 20, cy, x1 + 20, cy, INK2, a, 4)
    arrow(c, x1, cy, x1 + 40, cy, INK2, a, 4, 16)
    if aberto:
        c.drawCircle(cx, cy, 20, paint("#FFFFFF", a))
        c.drawCircle(cx, cy, 20, paint(INK, a, stroke=6))
    else:
        c.drawCircle(cx, cy, 20, paint(INK, a))
    ftext(c, str(zero), cx, cy + 80, 50, "black", INK, a)
    if rot_zero:
        text(c, rot_zero, cx, cy + 128, 26, "bold", INK2, a)


class Plano:
    """eixos de um gráfico: (x0, y0) = canto inferior esquerdo em pixels; xmax, ymax = valores no fim dos eixos"""

    def __init__(self, x0, y0, w, h, xmax, ymax):
        self.x0, self.y0, self.w, self.h, self.xmax, self.ymax = x0, y0, w, h, xmax, ymax

    def P(self, x, y):
        return self.x0 + self.w * x / self.xmax, self.y0 - self.h * y / self.ymax

    def eixos(self, c, a, rx="x", ry="y", ticks_x=(), ticks_y=()):
        if a <= 0:
            return
        line(c, self.x0, self.y0, self.x0 + self.w + 30, self.y0, INK2, a, 4)
        line(c, self.x0, self.y0, self.x0, self.y0 - self.h - 30, INK2, a, 4)
        text(c, rx, self.x0 + self.w + 20, self.y0 + 50, 26, "bold", INK2, a, align="right")
        text(c, ry, self.x0 - 12, self.y0 - self.h - 46, 26, "bold", INK2, a, align="left")
        for v, s_ in ticks_x:
            px, _ = self.P(v, 0)
            line(c, px, self.y0 - 8, px, self.y0 + 8, INK2, a, 3)
            ftext(c, s_, px, self.y0 + 44, 26, "bold", INK2, a)
        for v, s_ in ticks_y:
            _, py = self.P(0, v)
            line(c, self.x0 - 8, py, self.x0 + 8, py, INK2, a, 3)
            ftext(c, s_, self.x0 - 16, py + 9, 24, "bold", INK2, a, align="right")

    def reta(self, c, f, xa, xb, col, a, prog_=1.0, sw=7):
        if a <= 0 or prog_ <= 0:
            return
        xe = xa + (xb - xa) * prog_
        p1, p2 = self.P(xa, f(xa)), self.P(xe, f(xe))
        line(c, p1[0], p1[1], p2[0], p2[1], col, a, sw)

    def faixa(self, c, f, g, xa, xb, col, a):
        """pinta a região entre f (em cima) e g de xa a xb"""
        if a <= 0:
            return
        p = skia.Path()
        p.moveTo(*self.P(xa, f(xa))); p.lineTo(*self.P(xb, f(xb))); p.lineTo(*self.P(xb, g(xb))); p.lineTo(*self.P(xa, g(xa)))
        p.close()
        c.drawPath(p, paint(col, a))


def grafico_equilibrio(c, t, t0, a, pl, aR=1.0, aC=1.0, aX=0.0, aF=0.0, selo_a=0.0):
    """o gráfico da seção 08: R = 25x e C = 2 000 + 15x, cruzando em (200, 5 000)"""
    R = lambda x: 25 * x
    Cx = lambda x: 2000 + 15 * x
    pl.eixos(c, a, "peças", "R$", ((100, "100"), (200, "200"), (300, "300")),
             ((2000, "2 000"), (5000, "5 000"), (8000, "8 000")))
    pl.faixa(c, Cx, R, 0, 200, RED, a * aF * 0.18)
    pl.faixa(c, R, Cx, 200, 340, GREEN, a * aF * 0.18)
    pl.reta(c, Cx, 0, 340, BLUE, a, aC)
    pl.reta(c, R, 0, 340, PURPLE, a, aR)
    if aC > 0:
        px, py = pl.P(340, Cx(340))
        text(c, "custo", px + 14, py + 10, 28, "black", BLUE, a * aC, align="left")
    if aR > 0:
        px, py = pl.P(340, R(340))
        text(c, "receita", px + 14, py + 10, 28, "black", PURPLE, a * aR, align="left")
    if aF > 0:
        px, py = pl.P(30, 1800)
        text(c, "PREJUÍZO", px, py + 10, 22, "black", RED, a * aF)
        px, py = pl.P(285, 8300)
        text(c, "LUCRO", px, py, 30, "black", GREEN, a * aF)
        arrow(c, px, py + 14, px + 20, py + 70, GREEN, a * aF, 4, 12)
    if aX > 0:
        px, py = pl.P(200, 5000)
        line(c, px, py, px, pl.y0, INK2, a * aX, 3)
        line(c, pl.x0, py, px, py, INK2, a * aX, 3)
        c.drawCircle(px, py, 16, paint(AMBER, a * aX))
        c.drawCircle(px, py, 16, paint(INK, a * aX, stroke=4))
    if selo_a > 0:
        px, py = pl.P(200, 5000)
        selo(c, px - 40, py - 120, selo_a, "200 peças: EMPATE", AMBER, -4, 30)


def corrida(c, a, pl, aA=1.0, aB=1.0, aX=0.0, aF=0.0):
    """aplicativos A = 4 + 3x (larga na frente) e B = 10 + 2x (km mais barato): cruzam em (6, 22)"""
    A = lambda x: 4 + 3 * x
    Bf = lambda x: 10 + 2 * x
    pl.eixos(c, a, "km", "R$", ((3, "3"), (6, "6"), (9, "9")), ((4, "4"), (10, "10"), (22, "22")))
    pl.faixa(c, Bf, A, 0, 6, GREEN, a * aF * 0.14)
    pl.faixa(c, A, Bf, 6, 11, RED, a * aF * 0.12)
    pl.reta(c, A, 0, 11, AMBER, a, aA)
    pl.reta(c, Bf, 0, 11, BLUE, a, aB)
    if aA > 0:
        px, py = pl.P(11, A(11))
        text(c, "A = 4 + 3x", px + 14, py + 10, 28, "black", AMBER, a * aA, align="left")
    if aB > 0:
        px, py = pl.P(11, Bf(11))
        text(c, "B = 10 + 2x", px + 14, py + 24, 28, "black", BLUE, a * aB, align="left")
    if aX > 0:
        px, py = pl.P(6, 22)
        line(c, px, py, px, pl.y0, INK2, a * aX, 3)
        c.drawCircle(px, py, 15, paint(GREEN, a * aX))
        c.drawCircle(px, py, 15, paint(INK, a * aX, stroke=4))
    if aF > 0:
        px, py = pl.P(3, 0)
        text(c, "A compensa", px, pl.y0 - 30, 26, "black", GREEN, a * aF)
        px, py = pl.P(8.5, 0)
        text(c, "B compensa", px, pl.y0 - 30, 26, "black", RED, a * aF)


def peca(c, cx, cy, s, a, col=None):
    """engrenagem estilizada (ícone de peça)"""
    if a <= 0:
        return
    col = col or "#7A818E"
    for k in range(8):
        ang = k * 45
        c.save(); c.translate(cx, cy); c.rotate(ang)
        rrect(c, -s * 0.16, -s * 0.62, s * 0.32, s * 0.3, 4, col, a)
        c.restore()
    c.drawCircle(cx, cy, s * 0.46, paint(col, a))
    c.drawCircle(cx, cy, s * 0.18, paint("#FFFFFF", a))


def camiseta(c, cx, cy, s, a, col=None):
    if a <= 0:
        return
    col = col or BLUE
    p = skia.Path()
    p.moveTo(cx - s * 0.22, cy - s * 0.5); p.lineTo(cx - s * 0.55, cy - s * 0.32); p.lineTo(cx - s * 0.42, cy - s * 0.08)
    p.lineTo(cx - s * 0.32, cy - s * 0.14); p.lineTo(cx - s * 0.32, cy + s * 0.5); p.lineTo(cx + s * 0.32, cy + s * 0.5)
    p.lineTo(cx + s * 0.32, cy - s * 0.14); p.lineTo(cx + s * 0.42, cy - s * 0.08); p.lineTo(cx + s * 0.55, cy - s * 0.32)
    p.lineTo(cx + s * 0.22, cy - s * 0.5); p.quadTo(cx, cy - s * 0.3, cx - s * 0.22, cy - s * 0.5); p.close()
    c.drawPath(p, paint(col, a))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO AFIM · EPISÓDIO 4", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        for k in range(12):
            camiseta(c, 330 + (k % 4) * 120, 300 + (k // 4) * 130, 100, aa * ep(t, C["01.a"] + k * 0.08, 0.3),
                     [BLUE, PURPLE, GREEN, AMBER][k % 4])
        rrect(c, 250, 690, 480, 110, 22, mix("#FFFFFF", AMBER, 0.25), aa)
        linha(c, [("600 camisetas = ", INK), ("EMPATE", AMBER)], 490, 745, 36, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 900, 230, 780, 130, 24, "#FFFFFF", ab, shadow=True)
        text(c, "mínimo para ter LUCRO?", 1290, 310, 44, "black", INK, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 960, 420, 300, 180, 24, mix("#FFFFFF", RED, 0.10), acc)
        ftext(c, "600", 1110, 540, 90, "black", RED, acc)
        strike(c, 990, 510, 1230, 510, ep(t, C["01.c"] + 0.8, 0.4), RED, 1)
        selo(c, 1110, 650, ep(t, C["01.c"] + 1.0, 0.4), "ESTÁ ERRADO", RED, -4, 28)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 1340, 420, 300, 180, 24, mix("#FFFFFF", GREEN, 0.16), ad)
        ftext(c, "601", 1490, 540, 90, "black", GREEN, ad)
        check_icon(c, 1490, 680, 30, ad, GREEN)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO AFIM · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de FUNÇÃO AFIM", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "O SINAL", "onde é + e onde é −", BLUE), ("02.b", "C · R · L", "custo, receita e lucro", PURPLE),
             ("02.c", "A PARTIR DE QUANDO", "um plano compensa", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "série de Equações e Inequações", [("inequação ≈ equação", INK), ("   ·   equilíbrio = EMPATE", AMBER)]),
             ("03.b", "série de Equações e Inequações", [("n > 800  →  menor inteiro: ", INK), ("801", GREEN)]),
             ("03.c", "episódio 3", [("dois pontos:  a = ", INK), ("Δy ÷ Δx", PURPLE)])]
    for k, (cue, serie, partes) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, serie, 300, y - 70, BLUE, size=22, a=a)
        linha(c, partes, 960, y + 10, 48, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA FÁBRICA E DOIS APLICATIVOS", "TUDO ISSO VIRA RETA", BLUE)
    card(c, *CARD_R)
    cols = [("04.a", "ALUGUEL + MÁQUINAS", "todo mês, vendendo ou não", BLUE),
            ("04.b", "MATERIAL", "um pouco em cada peça", PURPLE),
            ("04.c", "PREÇO DE VENDA", "o que entra por peça", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 380 + k * 340
        rrect(c, x - 150, 220, 300, 330, 24, "#FFFFFF", a, shadow=True)
        peca(c, x, 320, 110, a, col)
        para(c, tit, x - 130, 440, 28, "black", col, a, 260, 34)
        text(c, sub, x, 525, 20, "bold", INK2, a)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        for k, (nome, col) in enumerate((("APP A", AMBER), ("APP B", BLUE))):
            x = 1480
            y = 240 + k * 170
            rrect(c, x - 190, y, 380, 140, 24, mix("#FFFFFF", col, 0.14), ad, shadow=True)
            text(c, nome, x, y + 60, 40, "black", col, ad)
            text(c, "bandeirada + preço por km", x, y + 110, 24, "bold", INK2, ad)
        regra(c, "PARTE FIXA + TAXA  =  RETAS", W / 2, 720, ep(t, C["04.d"] + 2.2, 0.5), 40)


# ======================================================================
# blocos a e b — estudo do sinal e a regra
# ======================================================================

def b_sinal(c, t, C, B):
    head_seq(c, t, C, [("05", "ONDE ELA É POSITIVA?", "ESTUDO DO SINAL", BLUE),
                       ("06", "E SE O a FOR NEGATIVO?", "O SINAL VIRA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 200, 1400, 110, 22, mix("#FFFFFF", BLUE, 0.10), aa)
            text(c, "ESTUDO DO SINAL: para quais x dá  +   −   0 ?", 960, 270, 36, "black", BLUE, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            linha(c, [("f(x) = ", INK), ("2", PURPLE), ("x − 6", INK), ("    zero: 2x = 6  →  ", INK2), ("x = 3", INK)],
                  960, 390, 46, ab)
        reta_sinal(c, 960, 620, 1200, ab, 3, ep(t, C["05.c"], 0.5), ep(t, C["05.d"], 0.5))
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            linha(c, [("f(0) = ", INK2), ("−6", RED)], 660, 760, 36, acc)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            linha(c, [("f(5) = ", INK2), ("4", GREEN)], 1260, 760, 36, ad)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        linha(c, [("g(x) = ", INK), ("−1", PURPLE), ("x + 4", INK), ("    zero: ", INK2), ("x = 4", INK)], 960, 300, 46, aa)
    reta_sinal(c, 960, 560, 1200, aa, 4, ep(t, C["06.b"], 0.5), ep(t, C["06.c"], 0.5), sL="+", sR="−")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        linha(c, [("g(0) = ", INK2), ("+4", GREEN)], 660, 700, 36, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        linha(c, [("g(6) = ", INK2), ("−2", RED)], 1260, 700, 36, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        selo(c, 960, 790, ad, "AO CONTRÁRIO. POR QUÊ?", AMBER, -3, 32)


def b_regra(c, t, C, B):
    head(c, t, B["start"], "REGRA DO SINAL", "QUEM MANDA É O a", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 200, 1400, 150, 24, mix("#FFFFFF", PURPLE, 0.10), aa)
        text(c, "DEPOIS do zero: o sinal de a", 960, 262, 42, "black", PURPLE, aa)
        text(c, "ANTES do zero: o sinal contrário", 960, 322, 36, "black", INK2, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        for k, (lei_, z, sL, sR, col) in enumerate((("a = 2 > 0", 3, "−", "+", GREEN), ("a = −1 < 0", 4, "+", "−", RED))):
            ak = ep(t, C["07.b"] + k * 2.6, 0.5)
            x = 590 + k * 740
            text(c, lei_, x, 420, 34, "black", col, ak)
            reta_sinal(c, x, 540, 520, ak * 0.95, z, ak, ak, sL=sL, sR=sR)
    acc = ep(t, C["07.c"], 0.5)
    K.atalho(c, 460, 680, 1000, 130, "ATALHO", ["ache o ZERO, olhe o a"], acc, 40)


# ======================================================================
# blocos c e d — os três modelos e o exemplo
# ======================================================================

def b_modelos(c, t, C, B):
    head_seq(c, t, C, [("08", "COMO A FÁBRICA VIRA FUNÇÃO?", "CUSTO E RECEITA", BLUE),
                       ("09", "E O LUCRO?", "RECEITA MENOS CUSTO", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 210, 700, 120, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "CUSTO FIXO", 580, 255, 30, "black", BLUE, aa)
        text(c, "paga mesmo sem produzir", 580, 305, 26, "bold", INK2, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        rrect(c, 990, 210, 700, 120, 22, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "CUSTO VARIÁVEL", 1340, 255, 30, "black", PURPLE, ab)
        text(c, "custo de 1 peça × nº de peças", 1340, 305, 26, "bold", INK2, ab)
    rows = [("08.c", [("C(x) = ", INK), ("fixo", BLUE), (" + ", INK), ("c", PURPLE), ("·x", INK)], "custo"),
            ("08.d", [("R(x) = ", INK), ("p", GREEN), ("·x", INK)], "receita · sai da origem")]
    for k, (cue, partes, sub) in enumerate(rows):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 410 + k * 120
        linha(c, partes, 760, y, 54, ak)
        text(c, sub, 1220, y + 12, 28, "bold", INK2, ak, align="left")
    if t < C["09"]:
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 640, 1460, 170, 24, "#FFFFFF", aa, shadow=True)
        text(c, "LUCRO = receita − custo", 520, 700, 30, "black", PURPLE, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        linha(c, [("L(x) = R(x) − ", INK), ("(", RED), ("fixo + c·x", BLUE), (")", RED)], 1180, 700, 48, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        text(c, "o menos vale para o custo INTEIRO", 700, 780, 30, "black", RED, acc)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        pill(c, "lucro negativo = PREJUÍZO", 1660, 780, RED, size=26, a=ad, anchor="right", bounds=(0, 1920))


def b_exemplo(c, t, C, B):
    head(c, t, B["start"], "VAMOS COM NÚMEROS", "A FÁBRICA DE PEÇAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    for k, (s_, v, col) in enumerate((("custo fixo", "R$ 2.000,00", BLUE), ("por peça", "R$ 15,00", PURPLE),
                                      ("venda", "R$ 25,00", GREEN))):
        ak = aa * ep(t, C["10.a"] + k * 1.2, 0.4)
        if ak <= 0:
            continue
        x = 450 + k * 510
        rrect(c, x - 220, 210, 440, 130, 22, mix("#FFFFFF", col, 0.12), ak)
        text(c, s_, x, 255, 26, "bold", INK2, ak)
        ftext(c, v, x, 318, 46, "black", col, ak)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("L(x) = ", INK), ("25", GREEN), ("x − ", INK), ("(", RED), ("2 000", BLUE), (" + ", INK), ("15", PURPLE),
                  ("x", INK), (")", RED)], 960, 420, 56, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("L(x) = ", INK), ("10x − 2 000", PURPLE)], 960, 520, 62, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 600, 1320, 200, 24, mix("#FFFFFF", AMBER, 0.20), ad)
        text(c, "PONTO DE EQUILÍBRIO: lucro = 0", 960, 655, 34, "black", AMBER, ad)
        linha(c, [("10x = 2 000  →  ", INK), ("x = 200 peças", INK)], 960, 740, 48, ep(t, C["10.d"] + 3.0, 0.4))


def b_grafico(c, t, C, B):
    head(c, t, B["start"], "O EMPATE NO GRÁFICO", "PONTO DE EQUILÍBRIO", AMBER)
    card(c, *CARD_R)
    pl = Plano(300, 790, 900, 540, 340, 9000)
    a0 = ep(t, C["11"], 0.4)
    grafico_equilibrio(c, t, C["11"], a0, pl, aR=ep(t, C["11.a"], 1.2), aC=ep(t, C["11.b"], 1.2),
                       aX=ep(t, C["11.c"], 0.5), aF=ep(t, C["11.d"], 0.8), selo_a=ep(t, C["11.c"] + 1.0, 0.4))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        pill(c, "o aluguel já está lá", 330, pl.P(0, 2000)[1] - 130, BLUE, size=24, a=ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 1360, 260, 330, 170, 22, "#FFFFFF", acc, shadow=True)
        text(c, "em 200 peças", 1525, 315, 28, "bold", INK2, acc)
        linha(c, [("C = R = ", INK), ("R$ 5.000", AMBER)], 1525, 380, 36, acc)
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        rrect(c, 1360, 480, 330, 170, 22, mix("#FFFFFF", GREEN, 0.14), ae)
        text(c, "cada peça a mais", 1525, 535, 28, "bold", INK2, ae)
        linha(c, [("+ R$ 10", GREEN)], 1525, 600, 46, ae)


def b_margem(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O EMPATE EM UMA LINHA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 150, "ATALHO · PONTO DE EQUILÍBRIO", ["FIXO ÷ o que sobra de cada unidade"], aa, 42)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        linha(c, [("sobra por peça: 25 − 15 = ", INK), ("R$ 10", GREEN)], 960, 450, 50, ab)
        for k in range(10):
            ak = ab * ep(t, C["12.b"] + 2.0 + k * 0.15, 0.3)
            x = 560 + k * 90
            rrect(c, x - 36, 520, 72, 50, 10, mix("#FFFFFF", GREEN, 0.3), ak)
            text_mid(c, "10", x, 545, 26, "black", GREEN, ak)
        text(c, "... pagando o aluguel de R$ 2.000", 960, 625, 28, "bold", INK2, ep(t, C["12.b"] + 3.6, 0.4))
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        linha(c, [("2 000 ÷ 10 = ", INK), ("200 peças", AMBER)], 960, 740, 60, acc)


# ======================================================================
# blocos e e f — lucro é estudo do sinal, a corrida de dois planos
# ======================================================================

def b_lucrosinal(c, t, C, B):
    head(c, t, B["start"], "A PARTIR DE QUANTAS PEÇAS?", "LUCRO É ESTUDO DO SINAL", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        linha(c, [("L(x) = 10x − 2 000 ", INK), ("> 0", GREEN)], 960, 260, 56, aa)
    ab = ep(t, C["13.b"], 0.5)
    reta_sinal(c, 960, 480, 1200, ab, 200, ab * 0.6, ep(t, C["13.b"] + 1.6, 0.5), sL="−", sR="+",
               aberto=t >= C["13.c"], rot_zero="lucro = 0")
    if ab > 0:
        pill(c, "a = 10 > 0", 1460, 330, PURPLE, size=26, a=ab, anchor="center")
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 650, 680, 150, 22, mix("#FFFFFF", BLUE, 0.10), acc)
        text(c, "DESIGUALDADE ESTRITA", 600, 700, 30, "black", BLUE, acc)
        text(c, "“maior que”, sem o igual", 600, 755, 28, "bold", INK2, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        selo(c, 1300, 690, ad, "LUCRO ZERO NÃO É LUCRO", AMBER, -3, 30)
        linha(c, [("resposta: ", INK2), ("201 peças", GREEN)], 1300, 790, 42, ep(t, C["13.d"] + 2.6, 0.4))


def b_corrida(c, t, C, B):
    head_seq(c, t, C, [("14", "OS DOIS APLICATIVOS", "A CORRIDA DE DOIS PLANOS", AMBER),
                       ("15", "ONDE ELES SE CRUZAM?", "O ATALHO DA DIFERENÇA", GREEN)])
    card(c, *CARD_R)
    pl = Plano(260, 800, 720, 520, 11, 36)
    a0 = ep(t, C["14"], 0.4)
    corrida(c, a0, pl, aA=ep(t, C["14.a"], 1.0), aB=ep(t, C["14.b"], 1.0),
            aX=ep(t, C["15.b"], 0.5), aF=ep(t, C["15.d"], 0.6))
    if t < C["15"]:
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            rrect(c, 1240, 250, 460, 170, 22, mix("#FFFFFF", AMBER, 0.20), acc)
            text(c, "bandeirada menor", 1470, 305, 28, "bold", INK2, acc)
            text(c, "LARGA NA FRENTE", 1470, 375, 36, "black", AMBER, acc)
            ac2 = ep(t, C["14.c"] + 2.4, 0.5)
            rrect(c, 1240, 450, 460, 170, 22, mix("#FFFFFF", BLUE, 0.14), ac2)
            text(c, "km mais barato", 1470, 505, 28, "bold", INK2, ac2)
            text(c, "GANHA NO FIM", 1470, 575, 36, "black", BLUE, ac2)
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            text_mid(c, "onde cruzam?", 1470, 700, 44, "black", INK, ad)
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        K.boxed(c, 1230, 230, 470, 210, GREEN, aa, 0.08)
        text(c, "ATALHO DA DIFERENÇA", 1465, 275, 22, "black", GREEN, aa)
        linha(c, [("(10 − 4) ÷ (3 − 2)", INK)], 1465, 340, 38, aa)
        linha(c, [("= ", INK), ("6 km", GREEN)], 1465, 405, 44, ep(t, C["15.a"] + 3.0, 0.4))
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("A(6) = ", INK2), ("22", AMBER), ("   B(6) = ", INK2), ("22", BLUE)], 1465, 490, 32, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 1230, 540, 470, 150, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
        text(c, "A mais caro:  A − B > 0", 1465, 595, 30, "black", PURPLE, acc)
        linha(c, [("x − 6 > 0", INK)], 1465, 655, 40, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        linha(c, [("até 6 km: ", INK2), ("A", AMBER), ("   ·   depois: ", INK2), ("B", BLUE)], 1465, 750, 32, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "A DOCEIRA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    for k, (s_, v, col) in enumerate((("custo fixo / mês", "R$ 600,00", BLUE), ("por bolo", "R$ 4,00", PURPLE),
                                      ("venda", "R$ 10,00", GREEN))):
        ak = aa * ep(t, C["16.a"] + k * 1.3, 0.4)
        if ak <= 0:
            continue
        x = 450 + k * 510
        rrect(c, x - 220, 210, 440, 130, 22, mix("#FFFFFF", col, 0.12), ak)
        text(c, s_, x, 255, 26, "bold", INK2, ak)
        ftext(c, v, x, 318, 46, "black", col, ak)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0 and t < C["17"]:
        text_mid(c, "lucro a partir de quantos bolos?", 960, 470, 50, "black", AMBER, ab)
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, 960, 680)
        return
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        linha(c, [("L(x) = 10x − ", INK), ("(", RED), ("600 + 4x", BLUE), (")", RED), (" = ", INK), ("6x − 600", PURPLE)],
              960, 420, 48, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        linha(c, [("6x = 600  →  ", INK), ("x = 100", AMBER), (" (empate)", INK2)], 960, 510, 42, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 570, 600, 120, 20, "#FFFFFF", acc, shadow=True)
        linha(c, [("L(100) = ", INK2), ("0", AMBER)], 600, 630, 40, acc)
        ac2 = ep(t, C["17.c"] + 3.0, 0.4)
        rrect(c, 1020, 570, 600, 120, 20, mix("#FFFFFF", GREEN, 0.12), ac2)
        linha(c, [("L(101) = ", INK2), ("R$ 6", GREEN)], 1320, 630, 40, ac2)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        regra(c, "LUCRO A PARTIR DE 101 BOLOS", W / 2, 770, ad, 40, GREEN)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Depois do zero, a função tem o sinal de a.",
          "Lucro é receita menos custo, com o custo entre parênteses.",
          "No equilíbrio o lucro é zero: com unidades inteiras, some 1."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Responder o EMPATE como a 1ª quantidade com lucro: 200 peças", "a conta que você fez deu exatamente esse número",
          "em 200 o lucro é zero: o lucro começa em 201 peças"),
         ("Dividir o fixo pelo PREÇO DE VENDA: 2 000 ÷ 25 = 80 peças", "cada venda ajuda a pagar o aluguel",
          "cada peça custa 15: sobram só 10. Com 80 peças, prejuízo de R$ 1.200"),
         ("SOMAR as bandeiradas: (4 + 10) ÷ 1 = 14 km", "as duas bandeiradas entram na conta",
          "o que conta é quanto um larga na frente: (10 − 4) ÷ 1 = 6 km")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


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


ALTS4 = [("A", "150.", "12 000 ÷ (50 + 30)", RED), ("B", "240.", "12 000 ÷ 50: esqueceu o custo", RED),
         ("C", "400.", "12 000 ÷ 30", RED), ("D", "600.", "o empate: lucro zero", AMBER), ("E", "601.", "", GREEN)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "DO EQUILÍBRIO AO LUCRO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Uma confecção tem custo fixo mensal de R$ 12.000,00 e gasta R$ 30,00 para produzir cada "
                           "camiseta, vendida a R$ 50,00. O número mínimo de camisetas que precisam ser produzidas e "
                           "vendidas em um mês para que a confecção tenha lucro é", INK)], a0, 236, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS4, 1000, 260, 680, 40, C["23.ok"], "E", cues_in, cues_x, gap=40)
    if t < C["23"]:
        pause_timer(c, t, C["22.end"] - 1.9, 540, yend + 120)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["23"], 0.4))
    text(c, "lucro > 0 ?  →  estudo do sinal", 540, y0 + 60, 28, "black", PURPLE, ep(t, C["23"], 0.4))
    aa = ep(t, C["23.a"], 0.4)
    if aa > 0:
        linha(c, [("L = 50x − ", INK), ("(", RED), ("12 000 + 30x", BLUE), (")", RED)], 540, y0 + 140, 34, aa)
        linha(c, [("L = ", INK), ("20x − 12 000", PURPLE)], 540, y0 + 205, 40, ep(t, C["23.a"] + 3.4, 0.4))
    ab = ep(t, C["23.b"], 0.4)
    if ab > 0:
        linha(c, [("20x > 12 000  →  ", INK), ("x > 600", INK)], 540, y0 + 290, 38, ab)
    acc = ep(t, C["23.c"], 0.4)
    if acc > 0:
        linha(c, [("L(600) = ", INK2), ("0", AMBER)], 540, y0 + 375, 34, acc)
        linha(c, [("L(601) = ", INK2), ("R$ 20", GREEN)], 540, y0 + 440, 34, ep(t, C["23.c"] + 2.0, 0.4))
        check_icon(c, 250, y0 + 520, 20, ep(t, C["23.ok"], 0.4), GREEN)
        linha(c, [("mínimo: 601 camisetas", GREEN)], 290, y0 + 522, 30, ep(t, C["23.ok"], 0.4), align="left")


ALTS7 = [("A", "2 km.", "8 − 6, sem dividir", RED), ("B", "5 km.", "", GREEN), ("C", "15 km.", "6 ÷ 0,4: só a do A", RED),
         ("D", "20 km.", "8 ÷ 0,4: só a do B", RED), ("E", "35 km.", "(6 + 8) ÷ 0,4: somou", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · VOCÊ FAZ", "QUAL CORRIDA SAI MAIS CARA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("A empresa de transporte A cobra R$ 6,00 fixos mais R$ 2,40 por quilômetro. Na empresa B, o "
                           "preço também é uma função afim da distância: uma corrida de 0 km (só a bandeirada) custa "
                           "R$ 8,00, e uma de 10 km custa R$ 28,00. A empresa A passa a ser mais cara que a B para "
                           "corridas com mais de", INK)], a0, 236, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 260, 680, 40, C["26.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["26"]:
        pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 110)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["26"], 0.4))
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        text(c, "1º a lei da B: (0, 8) e (10, 28)", 540, y0 + 60, 28, "black", INK2, aa)
        linha(c, [("a = (28 − 8) ÷ 10 = ", INK), ("2", PURPLE), ("   b = ", INK), ("8", BLUE)], 540, y0 + 125, 32,
              ep(t, C["26.a"] + 2.4, 0.4))
        linha(c, [("B = 8 + 2x", BLUE)], 540, y0 + 185, 36, ep(t, C["26.a"] + 6.0, 0.4))
    ab = ep(t, C["26.b"], 0.4)
    if ab > 0:
        linha(c, [("6 + 2,4x > 8 + 2x", INK)], 540, y0 + 265, 36, ab)
        linha(c, [("0,4x > 2  →  ", INK), ("x > 5 km", INK)], 540, y0 + 330, 36, ep(t, C["26.b"] + 3.4, 0.4))
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        linha(c, [("4 km:  A 15,60 · B 16,00", GREEN)], 540, y0 + 415, 28, acc)
        linha(c, [("6 km:  A 20,40 · B 20,00", RED)], 540, y0 + 470, 28, ep(t, C["26.c"] + 2.4, 0.4))
        check_icon(c, 250, y0 + 545, 20, ep(t, C["26.ok"], 0.4), GREEN)
        linha(c, [("A fica mais cara depois de 5 km", GREEN)], 290, y0 + 547, 26, ep(t, C["26.ok"], 0.4), align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DA FUNÇÃO AFIM", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        linha(c, [("f(x) = ", INK), ("a", PURPLE), ("x + ", INK), ("b", BLUE)], W / 2, 280, 80, aa)
    itens = [("FÍSICA", "s = s₀ + v·t", BLUE), ("TERMOMETRIA", "F = 1,8C + 32", AMBER), ("JUROS SIMPLES", "M = C + C·i·t", GREEN),
             ("PROGRESSÕES", "aₙ = a₁ + (n − 1)r", PURPLE)]
    for k, (tit, f_, col) in enumerate(itens):
        ak = ep(t, C["29.b"] + k * 0.9, 0.5)
        if ak <= 0:
            continue
        x = 390 + k * 380
        rrect(c, x - 170, 380, 340, 220, 24, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 170, 380, 340, 64, 24, col, ak * 0.16)
        text(c, tit, x, 425, 28, "black", col, ak)
        ftext(c, f_, x, 530, 34, "black", INK, ak)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 720, acc, "E AS PEGADINHAS", AMBER, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Que negócio você abriria, e quantas unidades precisaria vender para empatar?", canal="no Estudativo",
        anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, sinal=b_sinal, regra=b_regra,
              modelos=b_modelos, exemplo=b_exemplo, grafico=b_grafico, margem=b_margem, lucrosinal=b_lucrosinal,
              corrida=b_corrida, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q7=b_q7, ponte=b_ponte,
              cta=b_cta)
