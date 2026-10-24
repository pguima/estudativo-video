"""Visual — Porcentagem, Episódio 4: a base mudou (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações e potências, alternativas, erro_cards,
atalho...). Peças deste episódio: colunas() (as barras 100 → +20 → 120 → −24 → 96 com a linha tracejada no 100),
selo_base() (o selo A BASE MUDOU), linha() (texto com milhar e cor por trecho), etiqueta() (preço de etiqueta).
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
_s = importlib.util.spec_from_file_location("comum024", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_porcentagem_ep4_a_base_mudou.mp4"
CARD_R = K.CARD_R
BASE_COL = "#9DB8D9"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)] (mantém os espaços dos milhares)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def tracejada(c, x0, x1, y, col, a, w=3, dash=18):
    if a <= 0:
        return
    x = x0
    while x < x1:
        line(c, x, y, min(x + dash, x1), y, col, a, w)
        x += dash * 1.8


def bloco(c, cx, y_top, h, col, a, w=150, txt=None, txt_col="#FFFFFF", hachura=False):
    """um pedaço de barra (retângulo) com rótulo no meio; hachura = pedaço que SAI (contorno tracejado)"""
    if a <= 0 or h <= 0.5:
        return
    if hachura:
        rrect(c, cx - w / 2, y_top, w, h, 6, col, a * 0.18)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y_top, w, h), 6, 6), paint(col, a, stroke=4))
    else:
        rrect(c, cx - w / 2, y_top, w, h, 6, col, a)
    if txt and h > 30:
        text_mid(c, txt, cx, y_top + h / 2, 30, "black", txt_col if not hachura else col, a)


def colunas(c, t, yb, esc, a, passos, xs=(420, 840, 1260), w=170, com_selo=True):
    """as três barras da história: passos = (a_base, a_sobe, a_tira, a_final) em [0,1]; valores 100 → 120 → 96.
    yb = linha de baixo; esc = pixels por real. A linha tracejada do 100 fica por cima de tudo."""
    a_base, a_sobe, a_tira, a_final = passos
    if a <= 0:
        return
    line(c, xs[0] - w, yb, xs[2] + w, yb, "#CFCFC9", a, 3)
    # 1) a base 100
    h100 = 100 * esc
    bloco(c, xs[0], yb - h100, h100, BASE_COL, a * a_base, w, "100", INK)
    text(c, "base 100", xs[0], yb + 46, 28, "black", BLUE, a * a_base)
    # 2) 100 + 20 = 120
    if a_sobe > 0:
        bloco(c, xs[1], yb - h100, h100, BASE_COL, a * a_sobe, w, "100", INK)
        hh = 20 * esc * a_sobe
        bloco(c, xs[1], yb - h100 - hh, hh, GREEN, a, w, "+20")
        text(c, "+20% de 100", xs[1], yb + 46, 28, "black", GREEN, a * a_sobe)
        text(c, "= 120", xs[1], yb - 120 * esc - 24, 34, "black", INK, a * a_sobe)
    # 3) 120 − 24 = 96
    if a_tira > 0:
        h96 = 96 * esc
        bloco(c, xs[2], yb - h96, h96, BASE_COL, a * a_tira, w, "96", INK)
        hh = 24 * esc
        bloco(c, xs[2], yb - h96 - hh, hh, RED, a * a_tira * (1 - 0.4 * a_final), w, "−24", hachura=True)
        text(c, "−20% de 120", xs[2], yb + 46, 28, "black", RED, a * a_tira)
    tracejada(c, xs[0] - w / 2 - 20, xs[2] + w / 2 + 60, yb - h100, INK2, a * a_base)
    if a_base > 0:
        text(c, "100", xs[2] + w / 2 + 100, yb - h100 + 10, 28, "black", INK2, a * a_base)
    if a_final > 0 and com_selo:
        selo(c, xs[2] + 250, yb - 96 * esc + 150, a * a_final, "4% ABAIXO", RED, -6, 30)


def selo_base(c, x, y, a, size=38, rot=-5):
    selo(c, x, y, a, "A BASE MUDOU", AMBER, rot, size)


def etiqueta(c, cx, cy, s, a, col=None, sub=None, w=300):
    """etiqueta de preço com furinho"""
    if a <= 0:
        return
    col = col or INK
    h = 130 if sub else 100
    rrect(c, cx - w / 2, cy - h / 2, w, h, 18, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18), paint(col, a, stroke=4))
    c.drawCircle(cx - w / 2 + 26, cy, 9, paint(col, a, stroke=3))
    text_mid(c, s, cx + 10, cy - (16 if sub else 0), 46, "black", col, a)
    if sub:
        text_mid(c, sub, cx + 10, cy + 38, 24, "bold", INK2, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A BASE MUDOU", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    chip(c, "+20%", 700, 250, GREEN, aa, 50)
    chip(c, "depois −20%", 1100, 250, RED, aa * ep(t, C["01.a"] + 0.6, 0.4), 50)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        ftext(c, "volta ao original?", W / 2, 370, 56, "black", INK, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        linha(c, [("100 → 120 → ", INK2), ("96", RED)], W / 2, 500, 70, acc)
        selo(c, W / 2, 640, ep(t, C["01.c"] + 0.6, 0.4), "4% MAIS BARATO", RED, -4, 50)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "cai no ENEM com frequência", W / 2, 785, AMBER, size=30, a=ad, anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "entender POR QUE +20% e −20% não se anulam", "a base mudou"),
            ("02.b", "que desconto DESFAZ um aumento", "voltar ao valor de antes"),
            ("02.c", "qual era o preço ANTES do desconto", "o preço de etiqueta")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 230, y - 14, 34, a, GREEN)
        text(c, s, 290, y, 44, "black", INK, a, align="left")
        text(c, sub, 290, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EPISÓDIOS 2 E 3", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "o FATOR (ep. 2)", 560, 290, 38, "black", PURPLE, aa)
        linha(c, [("+20%  →  × ", INK2), ("1,20", GREEN)], 560, 400, 52, aa)
        linha(c, [("−20%  →  × ", INK2), ("0,80", RED)], 560, 500, 52, aa)
    line(c, 960, 260, 960, 620, "#E6E6E2", ep(t, C["03.b"], 0.5), 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "em sequência (ep. 3)", 1360, 290, 38, "black", PURPLE, ab)
        text(c, "MULTIPLIQUE", 1360, 420, 60, "black", GREEN, ab)
        text(c, "os fatores", 1360, 490, 40, "black", GREEN, ab)


# ======================================================================
# bloco A — a loja, em reais
# ======================================================================

def b_loja(c, t, C, B):
    head_seq(c, t, C, [("04", "SEGUNDA E SEXTA", "EM REAIS", BLUE), ("05", "COM OS FATORES", "NUMA CONTA SÓ", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    a_base = ep(t, C["04.a"], 0.5)
    a_sobe = ep(t, C["04.b"], 0.8)
    a_tira = ep(t, C["04.d"] + 0.8, 0.8)
    a_fim = ep(t, C["04.e"], 0.5)
    if sid == "04":
        colunas(c, t, 740, 3.6, 1.0, (a_base, a_sobe, a_tira, a_fim), xs=(420, 840, 1260))
        if a_base > 0:
            text(c, "segunda", 420, 230, 30, "bold", INK2, a_base)
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            text(c, "sexta: −20%", 1180, 230, 30, "bold", INK2, acc)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            pill(c, "20% de QUÊ? do preço de agora: 120", 1530, 260, AMBER, size=22, a=ad, anchor="center",
                 bounds=(0, 1920))
        return
    colunas(c, t, 560, 2.2, 1.0, (1, 1, 1, 1), xs=(420, 760, 1100), w=130, com_selo=False)
    a5 = ep(t, C["05.a"], 0.5)
    if a5 > 0:
        linha(c, [("1,20 × 0,80 = ", INK), ("0,96", PURPLE)], W / 2, 700, 60, a5)
    b5 = ep(t, C["05.b"], 0.5)
    if b5 > 0:
        text(c, "o preço final = 96% do inicial", 1500, 300, 30, "black", INK2, b5)
    c5 = ep(t, C["05.c"], 0.5)
    if c5 > 0:
        selo(c, 1500, 420, c5, "4% MAIS BARATO", RED, -4, 40)


# ======================================================================
# bloco B — a causa
# ======================================================================

def b_causa(c, t, C, B):
    head(c, t, B["start"], "POR QUÊ?", "A BASE DE CÁLCULO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 220, 1320, 110, BLUE, aa, 0.08)
        text(c, "BASE DE CÁLCULO = o valor do qual você parte", W / 2, 290, 40, "black", BLUE, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 390, 600, 220, 22, GREEN, 0.10 * ab)
        text(c, "AUMENTO de 20%", 600, 450, 34, "black", GREEN, ab)
        linha(c, [("sobre ", INK2), ("100", BLUE), (" = R$ ", INK), ("20", GREEN)], 600, 530, 48, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 390, 600, 220, 22, RED, 0.10 * acc)
        text(c, "DESCONTO de 20%", 1320, 450, 34, "black", RED, acc)
        linha(c, [("sobre ", INK2), ("120", BLUE), (" = R$ ", INK), ("24", RED)], 1320, 530, 48, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        selo_base(c, W / 2, 680, ad, 50)
        text(c, "mesma taxa · base diferente · valor diferente", W / 2, 790, 32, "black", INK2, ep(t, C["06.d"] + 0.8, 0.5))


# ======================================================================
# bloco C — a regra (e a curiosidade da fórmula)
# ======================================================================

def b_regra(c, t, C, B):
    head_seq(c, t, C, [("07", "E SE O DESCONTO VIER ANTES?", "SEMPRE ABAIXO", PURPLE),
                       ("08", "QUANTO SE PERDE?", "CURIOSIDADE E ATALHO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            linha(c, [("100 − 20% = ", INK2), ("80", RED)], 560, 300, 50, aa)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            linha(c, [("80 + 20% de 80 (16) = ", INK2), ("96", RED)], 560, 400, 44, ab)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            text(c, "o aumento incidiu sobre uma base MENOR", 560, 480, 30, "bold", AMBER, acc)
            selo_base(c, 1380, 360, acc, 40, -6)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            boxed(c, 300, 560, 1320, 200, PURPLE, ad, 0.08)
            text(c, "aumento e desconto do MESMO percentual", W / 2, 630, 40, "black", PURPLE, ad)
            text(c, "SEMPRE terminam abaixo, em qualquer ordem", W / 2, 700, 40, "black", PURPLE, ad)
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        pill(c, "CURIOSIDADE", 560, 240, BLUE, size=24, a=aa, anchor="center", bounds=(0, 1920))
        expr(c, "1 - x^2/10000", 560, 340, 64, aa, cores={1: PURPLE, 2: PURPLE})
        text(c, "x = a taxa · x² = x vezes x", 560, 440, 28, "bold", INK2, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        text(c, "com 50%:", 1300, 250, 32, "black", INK2, ab)
        linha(c, [("1,5 × 0,5 = ", INK), ("0,75", PURPLE)], 1300, 330, 52, ab)
        linha(c, [("perda de ", INK2), ("25%", RED)], 1300, 420, 46, ab)
    acc = ep(t, C["08.c"], 0.5)
    K.atalho(c, 300, 520, 1320, 230, "ATALHO DE CABEÇA",
             ["a perda = taxa × taxa ÷ 100", "20 × 20 = 400 → ÷ 100 → 4%"], acc, 40)


# ======================================================================
# bloco D — que desconto desfaz um aumento
# ======================================================================

def b_desfaz(c, t, C, B):
    head_seq(c, t, C, [("09", "A PERGUNTA DO AVESSO", "QUE DESCONTO DESFAZ?", AMBER),
                       ("10", "O JEITO CERTO", "DIVIDA PELO FATOR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0:
            linha(c, [("100 + 50% = ", INK2), ("150", GREEN)], 560, 290, 54, aa)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            ftext(c, "−50% para voltar?", 560, 400, 46, "black", AMBER, ab)
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            linha(c, [("50% de 150 = 75 → ", INK2), ("75", RED)], 560, 510, 46, acc)
            selo(c, 560, 610, ep(t, C["09.c"] + 0.8, 0.4), "PASSOU DO PONTO", RED, -4, 36)
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            selo_base(c, 1360, 360, ad, 44)
            text(c, "agora a base é 150", 1360, 470, 36, "black", BLUE, ad)
        return
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        text(c, "ida: × 1,5      volta: ÷ 1,5", W / 2, 290, 50, "black", PURPLE, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("1 ÷ 1,5 = ", INK), ("0,666…", PURPLE)], W / 2, 400, 56, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("desconto de ", INK2), ("1/3 ≈ 33,3%", GREEN)], W / 2, 500, 50, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        linha(c, [("1/3 de 150 = 50  →  150 − 50 = ", INK2), ("100", GREEN)], W / 2, 620, 44, ad)
        check_icon(c, 1500, 600, 30, ad, GREEN)
        pill(c, "VOLTOU!", W / 2, 720, GREEN, size=32, a=ep(t, C["10.d"] + 0.8, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco E — a fórmula do retorno
# ======================================================================

def b_formula(c, t, C, B):
    head(c, t, B["start"], "O DESCONTO DE RETORNO", "A FÓRMULA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        text(c, "RETORNO = voltar ao valor de antes", W / 2, 240, 32, "black", BLUE, aa)
        expr(c, "d = x/100+x", 700, 380, 80, aa, cores={0: PURPLE, 2: PURPLE})
        text(c, "x = o aumento", 1200, 340, 32, "black", GREEN, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        text(c, "100 + x = o PREÇO NOVO", 1200, 420, 32, "black", BLUE, ab)
        text(c, "(a base nova)", 1200, 465, 26, "bold", INK2, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        linha(c, [("x = 50:  50/150 = ", INK), ("1/3", GREEN)], W / 2, 560, 50, acc)
        check_icon(c, 1260, 540, 28, acc, GREEN)
    ad = ep(t, C["11.d"], 0.5)
    K.atalho(c, 300, 630, 1320, 150, "ATALHO", ["desconto de volta = o que entrou ÷ o novo total"], ad, 38)


# ======================================================================
# bloco F — o preço antes do desconto
# ======================================================================

def b_antes(c, t, C, B):
    head_seq(c, t, C, [("12", "JÁ COM 20% DE DESCONTO", "QUAL ERA O ORIGINAL?", AMBER),
                       ("13", "A BASE MUDOU", "DIVIDA PELO FATOR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    aa = ep(t, C["12.a"], 0.5)
    etiqueta(c, 460, 320, "R$ 150", aa, INK, "já com 20% de desconto", 380)
    if sid == "12":
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            text(c, "PREÇO DE ETIQUETA = o valor original", 1260, 300, 32, "black", BLUE, ab)
            text(c, "antes do desconto: ?", 1260, 360, 40, "black", INK, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            ftext(c, "150 + 20% = 180 ?", 960, 520, 54, "black", RED, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            linha(c, [("teste: 180 − 20% = ", INK2), ("144", RED)], 960, 640, 46, ad)
            selo(c, 960, 750, ep(t, C["12.d"] + 0.8, 0.4), "NÃO DÁ 150", RED, -3, 40)
        return
    aa13 = ep(t, C["13.a"], 0.5)
    if aa13 > 0:
        selo_base(c, 1260, 300, aa13, 40)
        text(c, "os 20% saíram do preço ORIGINAL (maior)", 1260, 400, 30, "black", INK2, aa13)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("150 ÷ 0,80 = ", INK), ("R$ 187,50", GREEN)], 960, 530, 60, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        linha(c, [("20% de 187,50 = 37,50  →  187,50 − 37,50 = ", INK2), ("150", GREEN)], 960, 650, 38, acc)
        pill(c, "FECHOU!", 960, 740, GREEN, size=32, a=ep(t, C["13.c"] + 0.8, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco G — a regra geral
# ======================================================================

def b_geral(c, t, C, B):
    head(c, t, B["start"], "A REGRA GERAL", "IDA E VOLTA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        etiqueta(c, 420, 400, "antes", aa, INK, None, 240)
        arrow(c, 580, 360, 1340, 360, GREEN, aa, 6, 22, progress=aa)
        text(c, "IDA: × fator", 960, 320, 44, "black", GREEN, aa)
        etiqueta(c, 1500, 400, "depois", aa, INK, None, 240)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        arrow(c, 1340, 450, 580, 450, PURPLE, ab, 6, 22, progress=ab)
        text(c, "VOLTA: ÷ fator", 960, 520, 44, "black", PURPLE, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        text(c, "desfazer um aumento · achar o preço antes do desconto", W / 2, 620, 30, "bold", INK2, acc)
    ad = ep(t, C["14.d"], 0.5)
    K.atalho(c, 400, 680, 1120, 120, "ATALHO", ["sem o valor? comece com 100"], ad, 38)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("16", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    etiqueta(c, 560, 300, "R$ 90", aa, INK, "depois de 10% de desconto", 380)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        text(c, "preço original = ?", 1300, 320, 48, "black", INK, ab)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 520)
    if t < C["16"]:
        return
    a1 = ep(t, C["16.a"], 0.5)
    if a1 > 0:
        linha(c, [("fator 0,9  →  90 ÷ 0,9 = ", INK), ("100", GREEN)], W / 2, 500, 54, a1)
    b1 = ep(t, C["16.b"], 0.5)
    if b1 > 0:
        linha(c, [("10% de 100 = 10  →  100 − 10 = ", INK2), ("90", GREEN)], W / 2, 610, 42, b1)
        check_icon(c, 1380, 592, 28, b1, GREEN)
    c1 = ep(t, C["16.c"], 0.5)
    if c1 > 0:
        ftext(c, "90 + 10% = 99", W / 2, 720, 44, "black", RED, c1)
        strike(c, 820, 706, 1100, 706, c1, RED, ep(t, C["16.c"] + 0.5, 0.4))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Mesma taxa, base diferente, valor diferente.", "Aumento e desconto iguais sempre terminam abaixo.",
          "Para voltar, divida pelo fator."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Achar que +20% e −20% voltam ao original", "os números são iguais",
          "o desconto é sobre uma base MAIOR: termina em 96"),
         ("Achar que o desconto que desfaz +25% é de 25%", "desfazer lembra repetir o mesmo número",
          "o desconto é sobre o preço JÁ aumentado: é menor. Divida pelo fator"),
         ("Somar 20% a um preço com desconto para achar o original", "somar parece o contrário de descontar",
          "o desconto saiu do preço original, que é MAIOR: divida pelo fator"),
         ("Subtrair as taxas: +10% e −20% = −10%", "uma parece cancelar a outra",
          "bases diferentes: 1,10 × 0,80 = 0,88 → −12%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20", "21"], ERROS)


# ======================================================================
# Questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _quadro(c, t, t0, linhas, y0=520, h=290):
    """quadro branco da resolução por cima do enunciado: linhas = [(cue, partes, size, check)]"""
    ra = ep(t, t0, 0.4)
    rrect(c, 170, y0, 740, h, 18, "#FFFFFF", ra, shadow=True)
    y = y0 + 66
    for cue, partes, size, chk in linhas:
        a = ep(t, cue, 0.4)
        linha(c, partes, 540, y, size, a)
        if chk and a > 0:
            check_icon(c, 860, y - 18, 24, a, GREEN)
        y += size + 30


ALTS4 = [("A", "4% menor", "", GREEN), ("B", "4% maior", "errou o sentido", RED),
         ("C", "igual", "esqueceu que a base mudou", RED), ("D", "20% menor", "só o último desconto", RED),
         ("E", "40% maior", "somou as taxas", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO", "A BASE MUDOU", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    _enunciado(c, [("O preço de uma mercadoria sofreu um aumento de 20% e, algumas semanas depois, um desconto de 20% "
                    "sobre o preço já reajustado.", INK),
                   ("Em relação ao preço inicial, o preço final ficou", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "BCDE"}
    if t >= C["22.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS4, 1000, 240, 680, 44, C["23.ok"], "A", cues_in, cues_x, gap=30)
    if t >= C["23"]:
        _quadro(c, t, C["23"], [(C["23.a"], [("1,20 × 0,80 = ", INK), ("0,96", PURPLE)], 46, False),
                               (C["23.a"] + 0.6, [("→ 4% menor", GREEN)], 40, False),
                               (C["23.b"], [("100 → 120 → ", INK2), ("96", GREEN)], 36, True)])


ALTS9 = [("A", "5% mais barato", "subtraiu: 25 − 20", RED), ("B", "5% mais caro", "subtraiu e trocou o sentido", RED),
         ("C", "10% mais barato", "", GREEN), ("D", "10% mais caro", "errou o sentido", RED),
         ("E", "45% mais barato", "somou: 20 + 25", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · NÓS FAZEMOS", "ESCREVA OS FATORES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    _enunciado(c, [("O preço de um insumo agrícola subiu 20% em um semestre e caiu 25% no semestre seguinte, sempre em "
                    "relação ao preço vigente.", INK),
                   ("Ao final do ano, em relação ao preço do início do período, o insumo ficou", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABDE"}
    if t >= C["24.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS9, 1000, 240, 680, 40, C["25.ok"], "C", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["24.end"] - 1.9, 540, 640)
    if t >= C["25"]:
        _quadro(c, t, C["25"], [(C["25"] + 0.3, [("+20% → ", INK2), ("1,20", GREEN), ("   −25% → ", INK2), ("0,75", RED)],
                                 34, False),
                                (C["25.a"], [("1,20 × 0,75 = ", INK), ("0,90", PURPLE)], 44, False),
                                (C["25.b"], [("100 → 120 → −30 → ", INK2), ("90", GREEN)], 34, True)])
        if t >= C["25.b"]:
            selo_base(c, 1340, 720, ep(t, C["25.b"] + 1.5, 0.4), 34, -3)


ALTS5 = [("A", "15%", "100 → 106,25", RED), ("B", "20%", "", GREEN), ("C", "22,5%", "100 → 96,875", RED),
         ("D", "25%", "esqueceu que a base é 125", RED), ("E", "30%", "100 → 87,50", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    _enunciado(c, [("Após um reajuste de 25%, uma loja decidiu promover um desconto sobre o novo preço, de modo que o "
                    "produto voltasse a custar exatamente o valor anterior ao reajuste.", INK),
                   ("O desconto concedido foi de", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS5, 1000, 240, 680, 44, C["27.ok"], "B", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["26.end"] - 1.9, 540, 640)
    if t >= C["27"]:
        _quadro(c, t, C["27"], [(C["27.a"], [("1 ÷ 1,25 = ", INK), ("0,80", PURPLE), ("  → 20%", GREEN)], 44, False),
                                (C["27.b"], [("100 → 125 → ", INK2), ("100", GREEN)], 36, True),
                                (C["27.c"], [("25/125 = ", INK2), ("20%", GREEN)], 36, False)])


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PONTO PERCENTUAL", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        text(c, "DESEMPREGO", W / 2, 260, 34, "black", INK2, aa)
        linha(c, [("8%  →  10%", INK)], W / 2, 360, 90, aa)
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        ftext(c, "subiu 2% ?", W / 2, 500, 64, "black", AMBER, ab)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        text(c, "o erro de linguagem mais comum da imprensa", W / 2, 620, 36, "black", RED, acc)
    pill(c, "ep. 5 · ponto percentual × por cento", W / 2, 760, PURPLE, size=32, a=ep(t, C["29.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Você achava que +20% e −20% voltavam ao original?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, loja=b_loja, causa=b_causa, regra=b_regra,
              desfaz=b_desfaz, formula=b_formula, antes=b_antes, geral=b_geral, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q4=b_q4, q9=b_q9, q5=b_q5, ponte=b_ponte, cta=b_cta)
