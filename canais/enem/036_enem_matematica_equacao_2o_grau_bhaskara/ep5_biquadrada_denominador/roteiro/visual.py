"""Visual — Equação do 2º Grau e Bhaskara, Episódio 5: biquadradas e x no denominador (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: fantasia() (o x² vestindo a fantasia roxa de "y" e tirando no fim), divide() (cada y positivo se
abrindo em duas raízes, + e −), bilhete() (o y negativo como bilhete rasgado com o selo "sem raiz real"), proibido() (a
placa "x ≠ 0" do valor proibido).
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
_s = importlib.util.spec_from_file_location("comum036", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                 K.selo, K.pause_timer)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_2grau_ep5_biquadrada_denominador.mp4"
CARD_R = K.CARD_R


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]"""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        x += w_


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def fantasia(c, cx, cy, size, a, vestido):
    """o x² e a fantasia de y: vestido 0 → só o x²; 1 → a fantasia roxa (com máscara) cobre o x² e mostra 'y'."""
    if a <= 0:
        return
    v = clamp(vestido)
    expr(c, "x^2", cx, cy, size, a * (1 - 0.85 * v), cores={0: BLUE})
    if v <= 0:
        return
    w, h = size * 1.7, size * 1.55
    drop = (1 - ease_io(v)) * -size * 1.2
    av = a * clamp(v * 1.6)
    rrect(c, cx - w / 2, cy - h / 2 + drop, w, h, size * 0.32, PURPLE, av, shadow=True)
    # a máscara: faixa escura com dois olhos
    rrect(c, cx - w * 0.42, cy - h * 0.36 + drop, w * 0.84, h * 0.2, h * 0.1, mix(PURPLE, INK, 0.55), av)
    for sx in (-1, 1):
        c.drawOval(skia.Rect.MakeXYWH(cx + sx * w * 0.18 - w * 0.08, cy - h * 0.33 + drop, w * 0.16, h * 0.13),
                   paint("#FFFFFF", av))
    fmid(c, "y", cx, cy + h * 0.14 + drop, size * 0.95, "black", "#FFFFFF", av)


def divide(c, cx, cy, yval, raiz, a, abre, size=48, dx=170):
    """caixa 'y = 4' que se abre em duas raízes (+raiz e −raiz) abaixo"""
    if a <= 0:
        return
    w = ftext_w(f"y = {yval}", "black", size) + 60
    rrect(c, cx - w / 2, cy - size * 0.85, w, size * 1.7, 20, mix("#FFFFFF", PURPLE, 0.14), a, shadow=True)
    fmid(c, f"y = {yval}", cx, cy, size, "black", PURPLE, a)
    if abre <= 0:
        return
    m = ease_io(clamp(abre))
    for sx, s_ in ((-1, f"x = {raiz}"), (1, f"x = −{raiz}")):
        x2 = cx + sx * dx * m
        arrow(c, cx + sx * 20, cy + size, x2, cy + size * 2.3, INK2, a * m, 4, 12)
        rrect(c, x2 - 110, cy + size * 2.4, 220, size * 1.5, 18, mix("#FFFFFF", GREEN, 0.18), a * m)
        fmid(c, s_, x2, cy + size * 3.15, size * 0.85, "black", GREEN, a * m)


def bilhete(c, cx, cy, s, a, rasga, size=46, w=300, h=150):
    """o y negativo: bilhete que se rasga ao meio (rasga 0→1) e ganha o selo 'SEM RAIZ REAL'"""
    if a <= 0:
        return
    r = ease_io(clamp(rasga))
    for sx in (-1, 1):
        c.save()
        c.translate(cx + sx * 26 * r, cy + 18 * r)
        c.rotate(sx * 9 * r)
        x0 = -w / 2 if sx < 0 else 0
        rrect(c, x0, -h / 2, w / 2, h, 14, "#FFF6D9", a, shadow=True, stroke=3, stroke_color=AMBER)
        # o recorte em zigue-zague
        pth = skia.Path()
        pth.moveTo(0, -h / 2)
        for k in range(1, 7):
            pth.lineTo((8 if k % 2 else -8) * r, -h / 2 + h * k / 6)
        c.drawPath(pth, paint(AMBER, a * r, stroke=3))
        c.restore()
    fmid(c, s, cx, cy, size, "black", RED if r > 0.5 else INK, a * (1 - 0.4 * r))
    if r > 0.3:
        selo(c, cx, cy + h * 0.85, a * clamp((r - 0.3) / 0.5), "SEM RAIZ REAL", RED, -6, 28)


def proibido(c, cx, cy, a, size=48, s="x ≠ 0"):
    if a <= 0:
        return
    tw = ftext_w(s, "black", size)
    w = tw + size * 2.2
    sw = max(4, size * 0.1)
    rrect(c, cx - w / 2, cy - size * 0.9, w, size * 1.8, size * 0.9, mix("#FFFFFF", RED, 0.10), a, stroke=sw,
           stroke_color=RED)
    ox = cx - w / 2 + size * 0.85
    c.drawCircle(ox, cy, size * 0.42, paint(RED, a, stroke=sw))
    line(c, ox - size * 0.3, cy + size * 0.3, ox + size * 0.3, cy - size * 0.3, RED, a, sw)
    fmid(c, s, ox + size * 0.65, cy, size, "black", RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EQUAÇÃO DO 2º GRAU", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        expr(c, "x^4 - 13x^2 + 36 = 0", 760, 330, 84, aa)
        rrect(c, 1290, 280, 330, 100, 24, mix("#FFFFFF", GREEN, 0.16), ep(t, C["01.a"] + 4.0, 0.4))
        fmid(c, "4 respostas", 1455, 330, 44, "black", GREEN, ep(t, C["01.a"] + 4.0, 0.4))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        expr(c, "x^4 - 5x^2 - 36 = 0", 760, 520, 84, ab)
        pill(c, "parece igual", 760, 610, GRAY, size=26, a=ep(t, C["01.b"] + 3.4, 0.4), anchor="center")
        rrect(c, 1290, 470, 330, 100, 24, mix("#FFFFFF", AMBER, 0.18), ep(t, C["01.b"] + 4.6, 0.4))
        fmid(c, "só 2", 1455, 520, 48, "black", AMBER, ep(t, C["01.b"] + 4.6, 0.4))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 780, acc, "O DETALHE QUE MUITA GENTE IGNORA", RED, -3, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver equações biquadradas", "x⁴ − 13x² + 36 = 0"),
            ("02.b", "resolver equações com x no denominador", "6/x = x − 1"),
            ("02.c", "usando o que você já sabe", "soma e produto · Bhaskara · raiz com ±")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    cols = [("03.a", "EPISÓDIO 3", "soma e produto", PURPLE),
            ("03.b", "EPISÓDIO 1", "raiz com ±", BLUE),
            ("03.c", "POTENCIAÇÃO", "potência de potência", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(cols):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 240 + d, 480, 520, 26, "#FFFFFF", a, shadow=True)
        text(c, tit, x, 300 + d, 28, "black", col, a, tracking=1)
        text(c, sub, x, 345 + d, 26, "bold", GRAY, a)
        if k == 0:
            linha(c, [("soma ", INK), ("7", PURPLE), (" · produto ", INK), ("10", PURPLE)], x, 460 + d, 34, a)
            arrow(c, x, 510 + d, x, 570 + d, INK2, a, 4, 12)
            fmid(c, "2 e 5", x, 640 + d, 60, "black", GREEN, a)
        elif k == 1:
            expr(c, "x^2 = 25", x, 470 + d, 60, a)
            arrow(c, x, 520 + d, x, 570 + d, INK2, a, 4, 12)
            fmid(c, "5 ou −5", x, 640 + d, 56, "black", GREEN, a)
        else:
            expr(c, "(x^2)^2", x, 470 + d, 64, a)
            arrow(c, x, 520 + d, x, 570 + d, INK2, a, 4, 12)
            expr(c, "x^4", x, 650 + d, 70, a, cores={0: GREEN})


# ======================================================================
# concreto: 3⁴ = 81 = 9²
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UM QUADRADO DE UM QUADRADO", "QUANTO É 3⁴?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    expr(c, "3^4 = ?", W / 2, 280, 96, a0 * (1 - ep(t, C["04.a"], 0.3)))
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        expr(c, "3 · 3 · 3 · 3 = 81", W / 2, 280, 84, aa, cores={8: GREEN})
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        # chaves juntando de dois em dois
        for k in range(2):
            x0 = 640 + k * 240
            line(c, x0 - 70, 350, x0 + 70, 350, PURPLE, ab, 5)
            line(c, x0 - 70, 350, x0 - 70, 330, PURPLE, ab, 5)
            line(c, x0 + 70, 350, x0 + 70, 330, PURPLE, ab, 5)
            fmid(c, "9", x0, 410, 56, "black", PURPLE, ab)
        expr(c, "9 · 9 = 81", W / 2, 520, 80, ep(t, C["04.b"] + 2.4, 0.4), cores={4: GREEN})
        pill(c, "3⁴ = 9² = (3²)²", W / 2, 620, PURPLE, size=34, a=ep(t, C["04.b"] + 3.4, 0.4), anchor="center")
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 460, 690, 1000, 120, 24, mix("#FFFFFF", BLUE, 0.12), acc)
        expr(c, "x^4 = (x^2)^2", W / 2, 750, 70, acc, cores={0: BLUE, 2: BLUE})


# ======================================================================
# bloco a — biquadrada e a troca de variável
# ======================================================================

def b_biquadrada(c, t, C, B):
    head_seq(c, t, C, [("05", "EQUAÇÃO BIQUADRADA", "A TROCA DE VARIÁVEL", BLUE),
                       ("06", "x² = y", "VIROU DO 2º GRAU", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        expr(c, "x^4 - 13x^2 + 36 = 0", W / 2, 280, 84, aa, cores={0: BLUE, 2: BLUE, 4: BLUE})
        if aa > 0:
            rrect(c, 360, 360, 1200, 110, 22, mix("#FFFFFF", BLUE, 0.10), aa)
            linha(c, [("BIQUADRADA", BLUE), (": só x⁴, x² e número · nenhum x sozinho", INK)], W / 2, 415, 32, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            pill(c, "TROCA DE VARIÁVEL: um nome novo para um pedaço", W / 2, 530, BLUE, size=28, a=ab, anchor="center")
        acc = ep(t, C["05.c"], 0.5)
        fantasia(c, 820, 690, 92, acc, ep(t, C["05.c"] + 1.2, 1.0))
        if acc > 0:
            arrow(c, 960, 690, 1060, 690, INK2, acc, 5, 14)
            pill(c, "x² = y", 1220, 690, PURPLE, size=44, a=acc, anchor="center")
        return
    # 06
    a0 = ep(t, C["06"], 0.4)
    expr(c, "x^4 - 13x^2 + 36 = 0", 560, 280, 64, a0, cores={0: BLUE, 2: BLUE})
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        pill(c, "x² = y", 1200, 250, PURPLE, size=30, a=aa, anchor="center")
        pill(c, "x⁴ = (x²)² = y²", 1200, 320, PURPLE, size=30, a=aa, anchor="center")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        arrow(c, W / 2, 380, W / 2, 430, INK2, ab, 5, 14)
        rrect(c, 460, 450, 1000, 130, 24, mix("#FFFFFF", PURPLE, 0.12), ab, shadow=True)
        expr(c, "y^2 - 13y + 36 = 0", W / 2, 515, 76, ab, cores={0: PURPLE, 2: PURPLE})
    acc = ep(t, C["06.c"], 0.5) * (1 - ep(t, C["06.d"], 0.4))
    if acc > 0:
        linha(c, [("soma ", INK), ("13", PURPLE), (" · produto ", INK), ("36", PURPLE), ("   →   y = 4  ou  y = 9", GREEN)],
              W / 2, 680, 44, acc)
    ad = ep(t, C["06.d"], 0.5)
    K.atalho(c, 360, 620, 1200, 200, "ATALHO · NO y, SOMA E PRODUTO", ["dois números de soma 13 e produto 36:  4 e 9"],
             ad, 34)


# ======================================================================
# bloco b — a volta para x
# ======================================================================

def b_volta(c, t, C, B):
    head(c, t, B["start"], "ACABOU?", "A FANTASIA TEM DE SAIR", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        linha(c, [("y = 4  e  y = 9", PURPLE), ("  ainda não são a resposta", INK)], W / 2, 260, 40, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        fantasia(c, W / 2, 360, 64, ab, 1 - ep(t, C["07.b"] + 0.6, 1.2))
    divide(c, 620, 470, "4", "2", ep(t, C["07.c"], 0.5), ep(t, C["07.c"] + 2.0, 0.8))
    divide(c, 1300, 470, "9", "3", ep(t, C["07.d"], 0.5), ep(t, C["07.d"] + 2.0, 0.8))
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        pill(c, "4 RAÍZES:  2 · −2 · 3 · −3", W / 2, 720, GREEN, size=36, a=ae, anchor="center")
        conferido(c, "x = 2:  16 − 52 + 36 = 0", 620, 800, ep(t, C["07.e"] + 2.0, 0.4), True, 30)


# ======================================================================
# bloco c — a regra da volta
# ======================================================================

def b_regra(c, t, C, B):
    head(c, t, B["start"], "A REGRA DA VOLTA", "QUANTAS RAÍZES CADA y DÁ?", PURPLE)
    card(c, *CARD_R)
    cols = [("08.a", "y POSITIVO", "2 raízes", "x² = 9  →  3 e −3", GREEN),
            ("08.b", "y = 0", "1 raiz", "x² = 0  →  0", BLUE),
            ("08.c", "y NEGATIVO", "nenhuma", "x² = −4  →  ?", RED)]
    for k, (cue, tit, n, ex, col) in enumerate(cols):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 240 + d, 500, 330, 26, mix("#FFFFFF", col, 0.10), a, shadow=True)
        text(c, tit, x, 300 + d, 34, "black", col, a)
        fmid(c, n, x, 410 + d, 64, "black", INK, a)
        text(c, ex, x, 510 + d, 30, "bold", INK2, a)
    ad = ep(t, C["08.d"], 0.5)
    bilhete(c, 1520, 720, "y = −4", ad, ep(t, C["08.d"] + 3.0, 0.8), 40, 260, 120)
    if ad > 0:
        rrect(c, 200, 650, 1000, 140, 22, mix("#FFFFFF", AMBER, 0.14), ad)
        linha(c, [("nenhum número ao quadrado dá ", INK), ("negativo", RED)], 700, 695, 34, ad)
        linha(c, [("y negativo = ", INK), ("BILHETE SEM VALOR", AMBER)], 700, 750, 34, ad)


# ======================================================================
# bloco d — x no denominador
# ======================================================================

def b_denominador(c, t, C, B):
    head_seq(c, t, C, [("09", "x NO DENOMINADOR", "A CONDIÇÃO DE EXISTÊNCIA", BLUE),
                       ("10", "RESOLVA E CONFIRA", "O PROIBIDO APARECEU?", PURPLE),
                       ("11", "ATALHO", "ANOTE O PROIBIDO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10", "11"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        expr(c, "6/x = x - 1", W / 2, 300, 100, aa, cores={0: INK})
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            rrect(c, 300, 430, 900, 110, 22, mix("#FFFFFF", BLUE, 0.10), ab)
            linha(c, [("CONDIÇÃO DE EXISTÊNCIA", BLUE), (": o valor que o x não pode ter", INK)], 750, 485, 30, ab)
            proibido(c, 1460, 485, ab)
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            pill(c, "× x  nos dois lados", 600, 650, PURPLE, size=30, a=acc, anchor="center")
            expr(c, "6 = x^2 - x", 1220, 650, 72, ep(t, C["09.c"] + 1.6, 0.4))
        return
    if sid == "10":
        proibido(c, 1560, 260, ep(t, C["10"], 0.4), 36)
        rows = [(C["10.a"], "x^2 - x - 6 = 0"), (C["10.b"], "x = 3   ou   x = -2")]
        for k, (t0, ex) in enumerate(rows):
            a, d = rise(t, t0)
            expr(c, ex, 760, 290 + k * 120 + d, 66, a, cores={2: GREEN, 6: GREEN} if k == 1 else None)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            pill(c, "soma 1 · produto −6", 760, 470, PURPLE, size=26, a=ab, anchor="center")
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            rrect(c, 300, 530, 1320, 100, 22, mix("#FFFFFF", GREEN, 0.14), acc)
            linha(c, [("nenhuma é 0", GREEN), ("  →  as duas servem", INK)], W / 2, 580, 36, acc)
        ad = ep(t, C["10.d"], 0.5)
        conferido(c, "x = 3:   6/3 = 2   e   3 − 1 = 2", 420, 700, ad, True, 32)
        conferido(c, "x = −2:   6/(−2) = −3   e   −2 − 1 = −3", 420, 780, ep(t, C["10.d"] + 3.4, 0.4), True, 32)
        return
    aa = ep(t, C["11.a"], 0.5)
    K.atalho(c, 360, 260, 1200, 300, "ATALHO · x NO DENOMINADOR", ["1. anote o proibido ANTES de multiplicar",
                                                                    "2. no fim, risque quem cair nele"], aa, 36)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        proibido(c, W / 2, 680, ab, 52)
        pill(c, "o valor proibido continua proibido", W / 2, 790, RED, size=28, a=ab, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("12", "SUA VEZ", "PAUSE E TENTE", GREEN), ("13", "VAMOS JUNTOS", "x² VIRA y · E VOLTA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    expr(c, "x^4 - 10x^2 + 9 = 0", W / 2, 280, 80, aa)
    if aa > 0 and t < C["13"]:
        pill(c, "quantas raízes reais? quais?", W / 2, 380, AMBER, size=30, a=aa, anchor="center")
    if t < C["13"]:
        pause_timer(c, t, C["12.end"] - 1.9, W / 2, 560)
        return
    a1 = ep(t, C["13.a"], 0.5)
    if a1 > 0:
        pill(c, "x² = y", 420, 390, PURPLE, size=28, a=a1, anchor="center")
        expr(c, "y^2 - 10y + 9 = 0", 1000, 390, 56, a1, cores={0: PURPLE})
    b1 = ep(t, C["13.b"], 0.5)
    if b1 > 0:
        linha(c, [("soma 10 · produto 9  →  ", INK), ("y = 1  ou  y = 9", PURPLE)], W / 2, 480, 34, b1)
    divide(c, 620, 560, "1", "1", ep(t, C["13.c"], 0.5), ep(t, C["13.c"] + 1.4, 0.8), 40, 150)
    divide(c, 1300, 560, "9", "3", ep(t, C["13.c"] + 3.6, 0.5), ep(t, C["13.c"] + 4.6, 0.8), 40, 150)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        pill(c, "4 RAÍZES:  1 · −1 · 3 · −3", W / 2, 800, GREEN, size=34, a=ad, anchor="center")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Na biquadrada, x² vira y.",
          "Não pare no y: volte para x.",
          "y negativo não gera raiz real."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "22"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 58, "black", INK, a, 1360, 68)


ERROS = [("x⁴ − 13x² + 36 = 0  →  4 e 9", "4 e 9 resolvem a equação em y",
          "a pergunta é o x: volte  →  2, −2, 3 e −3"),
         ("x² = −4  →  x = ±2", "o 4 tem raiz, e ela é 2",
          "2² = 4 e (−2)² = 4: ninguém ao quadrado dá −4  →  sem raiz real"),
         ("x²/x = 5  →  × x  →  0 e 5", "as contas estão certas",
          "o 0 zera o denominador: era proibido desde o começo  →  só 5")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["15", "16", "17"], ERROS)


# ======================================================================
# questão 8 do material (você faz)
# ======================================================================

ALTS8 = [("A", "nenhuma.", "y negativo não invalida tudo", RED),
         ("B", "uma.", "ficou só com o 3", RED),
         ("C", "duas.", "", GREEN),
         ("D", "três.", "contou o y = −4 como resposta", RED),
         ("E", "quatro.", "aceitou x² = −4 como ±2", RED)]


def b_q8(c, t, C, B):
    head_seq(c, t, C, [("18", "QUESTÃO 8 · VOCÊ FAZ", "EQUAÇÃO BIQUADRADA", BLUE),
                       ("20", "ATALHO", "O PRODUTO DOS y", GREEN),
                       ("21", "QUESTÃO 8", "E AS ERRADAS?", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19", "20", "21"])
    a0 = ep(t, C["18.a"], 0.4) * (1 - ep(t, C["19"], 0.4))
    if a0 > 0:
        y = 260
        for ln in K.wrap("Considere a equação", "black", 30, 720):
            text(c, ln, 190, y, 30, "black", INK, a0, align="left"); y += 42
        expr(c, "x^4 - 5x^2 - 36 = 0", 550, y + 50, 60, a0)
        y += 140
        for ln in K.wrap("O número de soluções reais dessa equação é", "black", 30, 720):
            text(c, ln, 190, y, 30, "black", INK, a0, align="left"); y += 42
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        pause_timer(c, t, C["18.end"] - 1.9, 540, y + 110)
    cues_in = {L: C[f"18.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["21.xa"], "B": C["21.xb"], "D": C["21.xd"], "E": C["21.xe"]}
    K.alternativas(c, t, C, ALTS8, 1000, 260, 680, 34, C["19.ok"], "C", cues_in, cues_x, gap=34)
    if t < C["19"]:
        return
    ap = ep(t, C["19"], 0.4)
    rrect(c, 170, 230, 760, 600, 18, "#FFFFFF", ap, shadow=True)
    if sid in ("19", "21"):
        text(c, "x² = y", 550, 280, 26, "black", PURPLE, ap, tracking=1)
        rows = [(C["19.a"], "y^2 - 5y - 36 = 0", None), (C["19.b"], "Δ = 25 + 144 = 169", None),
                (C["19.c"], "y = (5±13)/2", None)]
        for k, (t0, ex, cor) in enumerate(rows):
            a, d = rise(t, t0)
            expr(c, ex, 550, 340 + k * 90 + d, 44, a)
        acc = ep(t, C["19.c"] + 2.6, 0.4)
        if acc > 0:
            linha(c, [("y = 9", PURPLE), ("   ou   ", INK), ("y = −4", RED)], 550, 630, 38, acc)
        ad = ep(t, C["19.d"], 0.5)
        if ad > 0:
            linha(c, [("x² = 9  →  ", INK), ("3 e −3", GREEN)], 380, 720, 34, ad)
        bilhete(c, 760, 710, "x² = −4", ep(t, C["19.e"], 0.5), ep(t, C["19.e"] + 1.2, 0.8), 30, 220, 90)
        return
    # 20 — atalho do produto dos y
    aa = ep(t, C["20.a"], 0.5)
    if aa > 0:
        expr(c, "y^2 - 5y - 36 = 0", 550, 300, 50, aa, cores={4: AMBER})
        linha(c, [("produto dos y = ", INK), ("−36", AMBER)], 550, 390, 36, aa)
    ab = ep(t, C["20.b"], 0.5)
    if ab > 0:
        linha(c, [("um y ", INK), ("positivo", GREEN), (" e um ", INK), ("negativo", RED)], 550, 480, 36, ab)
    acc = ep(t, C["20.c"], 0.5)
    K.atalho(c, 200, 540, 700, 260, "ATALHO · PRODUTO DOS y NEGATIVO", ["um y dá 2 raízes, o outro 0",
                                                                          "→ exatamente DUAS"], acc, 30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    itens = [("23.a", "juntamos tudo", "forma geral · Bhaskara · soma e produto · biquadrada", BLUE),
             ("23.b", "caçamos as pegadinhas", "verdadeiro ou falso", AMBER),
             ("23.c", "Física e Economia", "a equação do 2º grau fora da sala", GREEN)]
    for k, (cue, s, sub, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 300, y - 14, a, 32, bg=col)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 30, "bold", GRAY, a, align="left")


def b_cta(c, t, C, B):
    cta(c, t, C["24.like"], C["24.sub"], C["24.bell"], C["24.com"], C["24.bye"],
        "Você já tinha parado no y alguma vez?", canal="no Estudativo", anki=C["24.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, biquadrada=b_biquadrada,
              volta=b_volta, regra=b_regra, denominador=b_denominador, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q8=b_q8, ponte=b_ponte, cta=b_cta)
