"""Visual — Porcentagem, Episódio 1: os três cálculos básicos e a conta de cabeça (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: triangulo() (PARTE / TOTAL × TAXA com o dedo tapando o que se procura), virgula() (a vírgula pulando
uma ou duas casas), seta_var() (as variações 40 → 50 e 50 → 40 com a base destacada), linha() (texto com cor por trecho).
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
_s = importlib.util.spec_from_file_location("comum024", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_porcentagem_ep1_tres_calculos.mp4"
CARD_R = K.CARD_R
PELE = "#F2C7A5"
PELE_ESC = "#D9A17E"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)] (mantém espaços e o símbolo %)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def dedo(c, cx, cy, s, a):
    """ponta de dedo (vista de cima) tapando um ponto: retângulo arredondado cor de pele com a unha"""
    if a <= 0:
        return
    w, h = s * 0.78, s * 1.15
    rrect(c, cx - w / 2, cy - h * 0.3, w, h, w / 2, PELE, a, shadow=True)
    rrect(c, cx - w * 0.3, cy - h * 0.22, w * 0.6, h * 0.34, w * 0.3, "#F8DCCB", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h * 0.3, w, h), w / 2, w / 2), paint(PELE_ESC, a, stroke=3))


def triangulo(c, cx, cy, s, a, tapa=None, tapa_a=0.0, hl=None, hl_a=0.0):
    """triângulo da porcentagem: PARTE em cima; TOTAL × TAXA embaixo. tapa = 'parte' | 'total' | 'taxa' (o dedo cobre);
    hl = peças destacadas em verde (o que sobra para a conta)"""
    if a <= 0:
        return
    h = s * 0.9
    top, left, right = (cx, cy - h / 2), (cx - s / 2, cy + h / 2), (cx + s / 2, cy + h / 2)
    p = skia.Path(); p.moveTo(*top); p.lineTo(*left); p.lineTo(*right); p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint(PURPLE, a, stroke=6))
    ym = cy + h * 0.08
    xl = cx - (ym - top[1]) / h * s / 2
    line(c, xl, ym, 2 * cx - xl, ym, PURPLE, a, 5)
    line(c, cx, ym, cx, cy + h / 2, PURPLE, a, 5)
    pos = {"parte": (cx, cy - h * 0.12), "total": (cx - s * 0.2, cy + h * 0.3), "taxa": (cx + s * 0.2, cy + h * 0.3)}
    size = s * 0.085
    for k, (x, y) in pos.items():
        col = GREEN if hl and k in hl and hl_a > 0 else INK
        text_mid(c, k.upper(), x, y, size, "black", mix(INK, col, hl_a if hl and k in hl else 0), a)
    if tapa_a > 0 and tapa:
        x, y = pos[tapa]
        dedo(c, x, y, s * 0.42, a * tapa_a)
        text_mid(c, "?", x, y + s * 0.02, s * 0.11, "black", AMBER, a * tapa_a)


def virgula(c, digitos, cx, cy, size, casas, a, col=None):
    """número sem vírgula (ex.: '240') com a vírgula saindo do fim e pulando `casas` (float, 0..n) para a esquerda;
    zeros à esquerda aparecem quando a vírgula passa do primeiro algarismo"""
    if a <= 0:
        return
    col = col or INK
    n = len(digitos)
    pad = max(0, math.ceil(casas) - n + 1)
    ds = "0" * pad + digitos
    dw = text_w("0", "black", size) * 1.05
    x0 = cx - len(ds) * dw / 2
    for i, d in enumerate(ds):
        fade = a * (clamp(casas - (n - 1) - (pad - i - 1)) if i < pad else 1.0)
        fmid(c, d, x0 + dw * (i + 0.5), cy, size, "black", col if i >= pad else GRAY, fade)
    k_pos = len(ds) - casas
    xv = x0 + dw * k_pos
    jump = abs(math.sin(math.pi * (casas % 1))) * size * 0.35
    fmid(c, ",", xv, cy + size * 0.18 - jump, size, "black", RED, a)


def seta_var(c, x0, x1, y, v0, v1, a, col, base_a=0.0, pct=None, pct_a=0.0, size=64):
    """variação de v0 para v1 numa seta; base_a destaca o v0 (o denominador) com um anel âmbar"""
    if a <= 0:
        return
    fmid(c, str(v0), x0, y, size, "black", INK, a)
    fmid(c, str(v1), x1, y, size, "black", INK, a)
    arrow(c, x0 + 70, y, x1 - 70, y, col, a, 7, 22, progress=a)
    if base_a > 0:
        c.drawCircle(x0, y, size * 0.85, paint(AMBER, a * base_a, stroke=6))
        text(c, "BASE", x0, y + size * 1.25, 26, "black", AMBER, a * base_a)
    if pct and pct_a > 0:
        text(c, pct, (x0 + x1) / 2, y - 40, 44, "black", col, a * pct_a)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def cena(c, cx, cy, titulo, linhas, col, a, w=440, h=330):
    """cartão de uma cena do dia a dia"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 24, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 64, 24, col, a * 0.14)
    text(c, titulo, cx, cy - h / 2 + 44, 30, "black", col, a)
    for k, s in enumerate(linhas):
        text(c, s, cx, cy - h / 2 + 130 + k * 52, 34, "black" if k == 0 else "bold", INK if k == 0 else INK2, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PORCENTAGEM", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        fmid(c, "%", W / 2, 360, 220, "black", BLUE, aa)
    ab = ep(t, C["01.b"], 0.5)
    for k, (s, col) in enumerate((("Matemática", BLUE), ("Biologia", GREEN), ("Geografia", AMBER))):
        chip(c, s, 560 + k * 400, 560, col, ab * ep(t, C["01.b"] + 0.4 * k, 0.4), 36)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        for k, s in enumerate(("a PARTE?", "a TAXA?", "o TOTAL?")):
            x = 560 + k * 400
            a = ac * ep(t, C["01.c"] + 0.35 * k, 0.4)
            rrect(c, x - 160, 680, 320, 110, 22, "#FFFFFF", a, shadow=True)
            text_mid(c, s, x, 735, 44, "black", PURPLE, a)
        selo(c, W / 2, 870, ac, "SÓ TRÊS PERGUNTAS", PURPLE, -2, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "reconhecer qual das 3 perguntas a questão faz", "a parte, a taxa ou o total"),
            ("02.b", "calcular 10%, 5%, 15% e 1% de cabeça", "sem calculadora")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "DA SÉRIE DE FRAÇÕES", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "POR CENTO = A CADA CEM", 560, 300, 42, "black", BLUE, aa)
        expr(c, "15% = 15/100", 560, 470, 90, aa, cores={2: BLUE})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "÷ 100: a vírgula anda 2 casas", 1380, 300, 36, "black", INK2, ab)
        virgula(c, "15", 1380, 470, 110, 2 * ep(t, C["03.b"] + 1.4, 1.2), ab, GREEN)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        boxed(c, 1080, 640, 600, 110, BLUE, acc, 0.08)
        text(c, "FORMA DECIMAL: 0,15", 1380, 712, 44, "black", BLUE, acc)
    line(c, 960, 240, 960, 780, "#E6E6E2", ab, 3)


# ======================================================================
# concreto — três cenas
# ======================================================================

def b_cotidiano(c, t, C, B):
    head_seq(c, t, C, [("04", "TRÊS CENAS DO DIA A DIA", "O QUE FALTA EM CADA UMA?", BLUE),
                       ("05", "AS TRÊS PEÇAS", "TOTAL · PARTE · TAXA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    cards = [("04.a", "RESTAURANTE", ["10% de gorjeta", "quanto em reais?"], "a PARTE"),
             ("04.b", "PROVA", ["18 de 20 acertos", "que porcentagem?"], "a TAXA"),
             ("04.c", "LOJA", ["vendeu uma parte", "qual era o estoque?"], "o TOTAL")]
    for k, (cue, tit, ls, falta) in enumerate(cards):
        x = 470 + k * 490
        a = ep(t, C[cue], 0.5)
        cena(c, x, 420, tit, ls, BLUE, a)
        if sid == "05":
            ad = ep(t, C["05.d"] + 0.35 * k, 0.4)
            if ad > 0:
                pill(c, "falta " + falta, x, 640, AMBER, size=28, a=ad, anchor="center", bounds=(0, 1920))
    if sid == "05":
        defs = [("05.a", "TOTAL = o todo", "o valor de referência"), ("05.b", "PARTE = um pedaço", "do todo"),
                ("05.c", "TAXA = a porcentagem", "o \"por cento\"")]
        xs = {"05.a": 1450, "05.b": 470, "05.c": 960}
        for cue, s, sub in defs:
            a = ep(t, C[cue], 0.5)
            text(c, s, xs[cue], 730, 30, "black", BLUE, a)
            text(c, sub, xs[cue], 772, 24, "bold", INK2, a)


# ======================================================================
# blocos a, b, c — as três perguntas
# ======================================================================

def _pergunta(c, t, C, sid, num, pergunta, tem, quer, conta, res, extra=None):
    head(c, t, C[sid], f"PERGUNTA {num}", pergunta, PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C[sid], 0.5)
    linha(c, [(tem, INK), ("   →   ", GRAY), (quer, GREEN)], W / 2, 250, 38, ep(t, C[f"{sid}.a"], 0.5))
    ab = ep(t, C[f"{sid}.b"], 0.5)
    if ab > 0:
        expr(c, conta, W / 2, 390, 80, ab, cores=res)
    if extra:
        extra(c, t, C, a0)


def b_p1(c, t, C, B):
    def extra(c, t, C, a0):
        ac = ep(t, C["06.c"], 0.5)
        if ac > 0:
            linha(c, [("15% de 200 = ", INK), ("30", GREEN)], W / 2, 540, 64, ac)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            text(c, "200 tem DOIS cens: 15 + 15 = 30", W / 2, 660, 36, "black", INK2, ad)
    _pergunta(c, t, C, "06", 1, "QUANTO É x% DE UM TOTAL?", "tem: TOTAL e TAXA", "quer: a PARTE",
              "0,15 × 200", {}, extra)
    regra(c, "PARTE = TOTAL × TAXA (forma decimal)", W / 2, 770, ep(t, C["06.c"] + 1.0, 0.5), 32)


def b_p2(c, t, C, B):
    def extra(c, t, C, a0):
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            linha(c, [("30 ÷ 200 = ", INK), ("0,15", GREEN)], W / 2, 530, 64, ab)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            linha(c, [("0,15 × 100 = ", INK2), ("15%", GREEN)], W / 2, 640, 56, acc)
            text(c, "a vírgula anda 2 casas para a DIREITA", W / 2, 712, 28, "bold", GRAY, acc)
    _pergunta(c, t, C, "07", 2, "QUE PORCENTAGEM A PARTE REPRESENTA?", "tem: PARTE e TOTAL", "quer: a TAXA",
              "30/200", {}, extra)
    regra(c, "TAXA = PARTE ÷ TOTAL", W / 2, 785, ep(t, C["07.b"] + 1.0, 0.5), 32)


def b_p3(c, t, C, B):
    def extra(c, t, C, a0):
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            linha(c, [("18 ÷ 0,15 = ", INK), ("120", GREEN)], W / 2, 530, 64, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            linha(c, [("confere: 15% de 120 = 12 + 6 = ", INK2), ("18", GREEN)], W / 2, 630, 40, acc)
            conferido(c, "fecha com o enunciado", 790, 700, ep(t, C["08.c"] + 2.5, 0.4), True, 30)
    _pergunta(c, t, C, "08", 3, "QUAL É O TOTAL?", "tem: PARTE e TAXA", "quer: o TOTAL", "18/0,15", {}, extra)
    regra(c, "TOTAL = PARTE ÷ TAXA (forma decimal)", W / 2, 785, ep(t, C["08.b"] + 1.0, 0.5), 32)


# ======================================================================
# bloco d — o triângulo
# ======================================================================

def b_triangulo(c, t, C, B):
    head_seq(c, t, C, [("09", "O TRIÂNGULO", "TAPE O QUE VOCÊ PROCURA", PURPLE),
                       ("10", "ATALHO", "AS PALAVRAS ENTREGAM", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        tapa, hl, res = None, None, ""
        for cue, tp, h_, r in (("09.c", "parte", ("total", "taxa"), "PARTE = TOTAL × TAXA"),
                               ("09.d", "taxa", ("parte", "total"), "TAXA = PARTE ÷ TOTAL"),
                               ("09.e", "total", ("parte", "taxa"), "TOTAL = PARTE ÷ TAXA")):
            if t >= C[cue]:
                tapa, hl, res, t0 = tp, h_, r, C[cue]
        ta = ep(t, t0, 0.4) if tapa else ep(t, C["09.b"], 0.5) * 0
        triangulo(c, 640, 480, 520, aa, tapa, ta, hl, ta)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0 and not tapa:
            dedo(c, 1000, 560, 120, ab)
            text(c, "tape o que você quer achar", 1300, 480, 36, "black", INK2, ab)
        if tapa:
            boxed(c, 1000, 400, 620, 150, PURPLE, ta, 0.08)
            text(c, res, 1310, 492, 44, "black", PURPLE, ta)
            done = [r for cue, r in (("09.c", "PARTE = TOTAL × TAXA"), ("09.d", "TAXA = PARTE ÷ TOTAL"),
                                     ("09.e", "TOTAL = PARTE ÷ TAXA")) if t >= C[cue] and r != res]
            for k, r in enumerate(done):
                text(c, r, 1310, 640 + k * 56, 32, "black", GRAY, ta)
        return
    a0 = ep(t, C["10"], 0.5)
    triangulo(c, 380, 470, 360, a0)
    rows = [("10.a", "\"x% DE ...\"", "multiplique", "TOTAL × TAXA"),
            ("10.b", "\"que parte representa?\"", "parte ÷ total", "TAXA"),
            ("10.c", "\"é x% de QUANTO?\"", "divida pela taxa", "TOTAL")]
    for k, (cue, s, acao, _) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        y = 290 + k * 130
        text(c, s, 700, y, 40, "black", INK, a, align="left")
        text(c, "→  " + acao, 1240, y, 40, "black", GREEN, a, align="left")
    ad = ep(t, C["10.d"], 0.5)
    K.atalho(c, 640, 680, 1000, 130, "ATALHO", ["no fim, volte ao enunciado e confira"], ad, 36)


# ======================================================================
# bloco e — o denominador
# ======================================================================

def b_denominador(c, t, C, B):
    head_seq(c, t, C, [("11", "VARIAÇÃO PERCENTUAL", "DE 40 PARA 50", BLUE),
                       ("12", "A VOLTA", "DE 50 PARA 40", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    aa = ep(t, C["11.a"], 0.5)
    sobe_pct = ep(t, C["11.c"], 0.5)
    seta_var(c, 520, 1000, 330, 40, 50, aa, GREEN, ep(t, C["11.c"], 0.5), "+25%", sobe_pct)
    ab = ep(t, C["11.b"], 0.5)
    if sid == "11" and ab > 0:
        boxed(c, 300, 470, 1320, 100, BLUE, ab, 0.08)
        text(c, "VARIAÇÃO PERCENTUAL = a mudança ÷ o valor de onde você partiu", W / 2, 532, 32, "black", BLUE, ab)
    if sobe_pct > 0:
        expr(c, "10/40 = 25%", 1420, 330, 56, sobe_pct, cores={0: INK})
    if sid != "12":
        return
    a0 = ep(t, C["12"], 0.5)
    base2 = ep(t, C["12.b"], 0.5)
    seta_var(c, 520, 1000, 560, 50, 40, a0, RED, base2, "−20%", base2)
    if base2 > 0:
        expr(c, "10/50 = 20%", 1420, 560, 56, base2, cores={0: INK})
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        selo(c, 1420, 730, acc, "MESMA DIFERENÇA, BASES DIFERENTES", AMBER, -3, 28)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        regra(c, "o denominador é de ONDE VOCÊ PARTIU", 640, 760, ad, 34)


# ======================================================================
# bloco f — conta de cabeça
# ======================================================================

def b_mental(c, t, C, B):
    head_seq(c, t, C, [("13", "DE CABEÇA", "A VÍRGULA PULA", GREEN), ("14", "DE CABEÇA", "O RESTO SAI DOS 10%", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            text(c, "10%  =  ÷ 10  =  1 casa", 540, 270, 38, "black", PURPLE, aa)
            virgula(c, "240", 540, 450, 120, ep(t, C["13.a"] + 1.6, 0.8), aa, INK)
            linha(c, [("10% de 240 = ", INK2), ("24", GREEN)], 540, 640, 46, ep(t, C["13.a"] + 3.0, 0.4))
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            text(c, "1%  =  ÷ 100  =  2 casas", 1380, 270, 38, "black", PURPLE, ab)
            virgula(c, "240", 1380, 450, 120, 2 * ep(t, C["13.b"] + 1.2, 1.2), ab, INK)
            linha(c, [("1% de 240 = ", INK2), ("2,4", GREEN)], 1380, 640, 46, ep(t, C["13.b"] + 2.6, 0.4))
        line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)
        return
    rows = [("14", "10% de 240", "24", INK), ("14.a", "5% = metade dos 10%", "12", BLUE),
            ("14.b", "15% = 10% + 5%  =  24 + 12", "36", GREEN)]
    for k, (cue, s, r, col) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        y = 290 + k * 120
        text(c, s, 300, y, 46, "black", col if k else INK, a, align="left")
        text(c, r, 1380, y, 56, "black", GREEN, a)
    acc = ep(t, C["14.c"], 0.5)
    K.atalho(c, 300, 650, 1320, 150, "ATALHO", ["ache os 10% primeiro: 5% é a metade, 15% é 10% + 5%"], acc, 36)


def b_fracoes(c, t, C, B):
    head(c, t, B["start"], "REVISÃO RELÂMPAGO", "DA SÉRIE DE FRAÇÕES", GREEN)
    card(c, *CARD_R)
    rows = [("15.a", "25%", "1/4", "÷ 4", "50"), ("15.b", "20%", "1/5", "÷ 5", "40"), ("15.c", "12,5%", "1/8", "÷ 8", "25")]
    text(c, "de 200", 1460, 230, 30, "bold", GRAY, ep(t, C["15.a"], 0.5))
    for k, (cue, p, f, op, r) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        y = 330 + k * 150
        text(c, p, 420, y + 20, 64, "black", INK, a)
        expr(c, "= " + f, 700, y, 64, a, cores={1: BLUE})
        text(c, "→  " + op, 1060, y + 20, 56, "black", GREEN, a)
        text(c, r, 1460, y + 20, 64, "black", GREEN, a)
    ab = ep(t, C["15.c"] + 1.6, 0.5)
    if ab > 0:
        regra(c, "conhece a fração? divida e pronto", W / 2, 790, ab, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "EM RITMO DE JOGO", GREEN), ("17", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    contas = [("16.a", "10% de 350", "17.a", "35"), ("16.b", "5% de 80", "17.b", "4"),
              ("16.c", "15% de 60", "17.c", "9"), ("16.d", "25% de 48", "17.d", "12")]
    for k, (cue, s, cr, r) in enumerate(contas):
        x = 430 + (k % 2) * 760
        y = 330 + (k // 2) * 220
        a = ep(t, C[cue], 0.5)
        rrect(c, x - 300, y - 80, 600, 160, 22, "#F7F7F5", a)
        text(c, s, x - 40, y + 18, 54, "black", INK, a)
        text(c, "=", x + 150, y + 18, 54, "black", GRAY, a)
        if t >= C["17"]:
            ar = ep(t, C[cr], 0.4)
            text(c, r, x + 230, y + 18, 60, "black", GREEN, ar)
        else:
            text(c, "?", x + 230, y + 18, 60, "black", AMBER, a)
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 790)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Três perguntas: a parte, a taxa ou o total.", "O denominador é sempre de onde você partiu.",
          "10% é andar a vírgula uma casa."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "25"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Usar o valor FINAL como denominador numa variação", "o valor final é o mais recente, está na sua frente",
          "a variação se mede de onde você PARTIU: o valor inicial vai embaixo"),
         ("Multiplicar quando deveria DIVIDIR para achar o total", "multiplicar foi o que você fez na pergunta 1",
          "falta o total? tape no triângulo: PARTE ÷ TAXA (e o total é maior que a parte)"),
         ("Achar que 40 → 50 e 50 → 40 são a mesma porcentagem", "a diferença é a mesma: 10",
          "as bases são diferentes: subir é +25%, cair é −20%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# Questão 1 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS1 = [("A", "60 unidades", "45 + 15: juntou os números", RED), ("B", "150 unidades", "15% de 150 = 22,5", RED),
         ("C", "270 unidades", "15% de 270 = 40,5", RED), ("D", "300 unidades", "", GREEN),
         ("E", "675 unidades", "multiplicou 45 × 15", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    _enunciado(c, [("Uma loja vendeu 45 unidades de um produto em um dia, o que corresponde a 15% de todo o estoque "
                    "disponível.", INK),
                   ("O estoque inicial dessa loja era de", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCE"}
    if t >= C["22.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS1, 1000, 240, 680, 42, C["23.ok"], "D", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["22.end"] - 1.9, 540, 660)
    if t >= C["23"]:
        ra = ep(t, C["23"], 0.4)
        rrect(c, 170, 470, 740, 340, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["23.a"], 0.4)
        triangulo(c, 330, 600, 200, aa, "total", ep(t, C["23.a"] + 3.0, 0.4), ("parte", "taxa"), ep(t, C["23.b"], 0.4))
        text(c, "pergunta 3: falta o TOTAL", 640, 520, 26, "black", PURPLE, aa)
        linha(c, [("45 ÷ 0,15 = ", INK), ("300", GREEN)], 640, 610, 40, ep(t, C["23.b"], 0.4))
        acc = ep(t, C["23.c"], 0.4)
        if acc > 0:
            linha(c, [("15% de 300 = 30 + 15 = ", INK2), ("45", GREEN)], 640, 690, 28, acc)
            conferido(c, "fecha", 560, 765, ep(t, C["23.c"] + 2.5, 0.4), True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AUMENTOS E DESCONTOS", PURPLE)
    aa = ep(t, C["26.a"], 0.5)
    chip(c, "AUMENTO", 760, 320, GREEN, aa, 46)
    chip(c, "DESCONTO", 1180, 320, RED, aa, 46)
    ab = ep(t, C["26.b"], 0.5)
    if ab > 0:
        text(c, "calcula a parte  +  depois soma", 640, 500, 36, "black", INK2, ab)
        text(c, "duas contas", 640, 560, 28, "bold", GRAY, ab)
    acc = ep(t, C["26.c"], 0.5)
    if acc > 0:
        boxed(c, 1070, 440, 460, 170, GREEN, acc, 0.08)
        text(c, "UMA multiplicação", 1300, 515, 40, "black", GREEN, acc)
        text(c, "só", 1300, 570, 32, "black", GREEN, acc)
    pill(c, "ep. 2 · o fator de multiplicação", W / 2, 720, PURPLE, size=32, a=ep(t, C["26.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"], "Quanto deu 15% de 60 para você?",
        canal="no Estudativo", anki=C["27.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, p1=b_p1, p2=b_p2, p3=b_p3,
              triangulo=b_triangulo, denominador=b_denominador, mental=b_mental, fracoes=b_fracoes, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q1=b_q1, ponte=b_ponte, cta=b_cta)
