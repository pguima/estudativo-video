"""Visual — Frações, Decimais e Dízimas, Episódio 1: O que é uma fração (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (pizza, barra, expr com frações empilhadas, reta, alternativas, erro_cards...).
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
_s = importlib.util.spec_from_file_location("comum018", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr, expr, expr_w, pizza, barra = K.fr, K.expr, K.expr_w, K.pizza, K.barra
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep1_o_que_e_fracao.mp4"
CARD_R = K.CARD_R
ROSA = "#E85D9A"


def pessoa(c, cx, by, col, a, s=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, by - 120 * s, 30 * s, paint(col, a))
    rrect(c, cx - 42 * s, by - 82 * s, 84 * s, 82 * s, 30 * s, col, a)


def nota(c, x, y, a, val="50", col="#2FA36B", w=150, h=72):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 8, col, a, shadow=True)
    rrect(c, x + 8, y + 8, w - 16, h - 16, 6, mix(col, "#FFFFFF", 0.25), a)
    text_mid(c, val, x + w / 2, y + h / 2, 30, "black", "#FFFFFF", a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FRAÇÕES DO ZERO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 560, 190, 800, 120, AMBER, aa, 0.10)
        text_mid(c, "questões “de frações”: quase nenhuma", W / 2, 250, 40, "black", INK, aa)
    temas = ["probabilidade", "porcentagem", "estatística", "Física"]
    fracs = [("1", "6"), ("3", "4"), ("2", "5"), ("d", "t")]
    for k, (s, (n_, d_)) in enumerate(zip(temas, fracs)):
        a = ep(t, C["01.c"] + 0.35 * k, 0.4)
        if a <= 0:
            continue
        x = 330 + k * 420
        card(c, x - 180, 360, 360, 230, a)
        fr(c, n_, d_, x, 430, 58, PURPLE, a)
        text(c, s, x, 560, 32, "black", INK, a)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "mas a fração está dentro de DEZENAS delas", W / 2, 660, 36, "black", BLUE, ab * (1 - ep(t, C["01.d"], 0.4)))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        xs = (420, 960, 1500)
        for k, (lab, col) in enumerate((("enunciado", INK2), ("FRAÇÃO", PURPLE), ("gabarito", GREEN))):
            chip(c, lab, xs[k], 700, col, ad * ep(t, C["01.d"] + 0.3 * k, 0.3), 34)
        arrow(c, 560, 700, 820, 700, LIGHT, ad, 5, 16)
        arrow(c, 1100, 700, 1360, 700, LIGHT, ad, 5, 16)
        selo(c, 1230, 790, ep(t, C["01.d"] + 1.6, 0.4), "QUEM PARA NO MEIO", RED, -5, 28)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "entender o que a fração SIGNIFICA", "em cada enunciado"), ("02.b", "simplificar qualquer fração", "de uma vez só")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")
    ac = ep(t, C["02.c"], 0.5)
    pizza(c, 1500, 700, 110, 8, 3, ac)
    pill(c, "do zero, com pizza", 900, 730, BLUE, size=34, a=ac, anchor="center", bounds=(0, 1920))


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "DIVIDIR = repartir em partes iguais", 560, 240, 32, "black", BLUE, aa)
        for g in range(4):
            gx = 240 + g * 165
            rrect(c, gx, 290, 145, 150, 16, mix("#FFFFFF", BLUE, 0.08), aa * ep(t, C["03.a"] + 0.5, 0.4))
            for k in range(3):
                c.drawCircle(gx + 35 + k * 38, 365, 15, paint(BLUE, aa))
        K.expr(c, "12 ÷ 4 = 3", 560, 520, 54, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "MDC = a maior régua que mede tudo certinho", 1340, 240, 30, "black", PURPLE, ab)
        for k, (n_, y) in enumerate(((12, 320), (18, 420))):
            text(c, str(n_), 1010, y + 18, 40, "black", INK, ab, align="right")
            for j in range(n_ // 6):
                rrect(c, 1040 + j * 186, y - 22, 180, 52, 8, PURPLE if j % 2 == 0 else mix(PURPLE, "#FFFFFF", 0.35),
                      ab * ep(t, C["03.b"] + 0.4 + 0.25 * j, 0.3))
                text_mid(c, "6", 1040 + j * 186 + 90, y + 4, 28, "black", "#FFFFFF", ab)
        ac = ep(t, C["03.c"], 0.5)
        fmid(c, "MDC(12, 18) = 6", 1340, 560, 50, "black", PURPLE, ac)


# ======================================================================
# bloco A — a pizza
# ======================================================================

def b_pizza(c, t, C, B):
    head_seq(c, t, C, [("04", "UMA PIZZA EM 4 FATIAS", "VOCÊ COME 3", BLUE), ("05", "O NÚMERO DE BAIXO", "DENOMINADOR", BLUE),
                       ("06", "O NÚMERO DE CIMA", "NUMERADOR", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["04.t"], 0.5)
    sel = 3 if t > C["04.t"] + 2.0 else int(clamp((t - C["04.t"] - 0.8) / 1.2) * 3)
    pizza(c, 560, 470, 260, 4, sel, a0, cut=ep(t, C["04.t"] + 0.3, 1.0), pull=ep(t, C["04.a"], 0.5) * 0.6)
    ab = ep(t, C["04.b"], 0.5)
    hl_d = ep(t, C["05.a"], 0.4)
    hl_n = ep(t, C["06.a"], 0.4)
    if ab > 0:
        if hl_d > 0:
            rrect(c, 1080, 520, 200, 150, 20, BLUE, 0.14 * hl_d)
        if hl_n > 0:
            rrect(c, 1080, 285, 200, 150, 20, MOLHO_(), 0.18 * hl_n)
        fr(c, "3", "4", 1180, 470, 150, INK, ab, num_col=mix(INK, "#C9532A", hl_n), den_col=mix(INK, BLUE, hl_d))
        text(c, "três quartos", 1180, 760, 40, "black", GRAY, ab * (1 - max(hl_d, hl_n)))
    ac = ep(t, C["04.c"], 0.5) * (1 - hl_d)
    pill(c, "FRAÇÃO = pedaços de um inteiro", 1180, 820, BLUE, size=30, a=ac, anchor="center", bounds=(0, 1920))
    if hl_d > 0:
        arrow(c, 1520, 600, 1300, 600, BLUE, hl_d, 5, 18, progress=hl_d)
        para(c, "em quantas fatias a pizza foi cortada", 1530, 585, 32, "black", BLUE, hl_d, 260)
    if hl_n > 0:
        arrow(c, 1520, 350, 1300, 350, "#C9532A", hl_n, 5, 18, progress=hl_n)
        para(c, "quantas fatias você pegou", 1530, 335, 32, "black", "#C9532A", hl_n, 260)
    regra(c, "denominador: em quantas fatias · numerador: quantas você pegou", W / 2, 800, ep(t, C["06.b"], 0.5), 30)


def MOLHO_():
    return K.MOLHO


# ======================================================================
# bloco B — os quatro significados
# ======================================================================

SIG = [("08", "PARTE-TODO"), ("09", "QUOCIENTE"), ("10", "RAZÃO"), ("11", "OPERADOR")]


def b_significados(c, t, C, B):
    sid = which(t, C, ["07", "08", "09", "10", "11"])
    heads = {"07": ("3/4 NEM SEMPRE É PIZZA", "QUATRO SIGNIFICADOS"), "08": ("SIGNIFICADO 1", "PARTE-TODO"),
             "09": ("SIGNIFICADO 2", "QUOCIENTE"), "10": ("SIGNIFICADO 3", "RAZÃO"), "11": ("SIGNIFICADO 4", "OPERADOR")}
    head(c, t, C[sid], heads[sid][0], heads[sid][1], BLUE)
    card(c, *CARD_R)
    # fila de 4 abas no topo do cartão
    a0 = ep(t, C["07.a"], 0.5)
    for k, (cid, lab) in enumerate(SIG):
        x = 360 + k * 400
        on_ = 1.0 if sid == cid else 0.0
        a = a0 * ep(t, C["07.a"] + 0.3 * k, 0.3)
        if a <= 0:
            continue
        rrect(c, x - 175, 180, 350, 76, 18, BLUE if on_ else "#F2F2EF", a)
        text_mid(c, lab, x, 218, 30, "black", "#FFFFFF" if on_ else INK2, a)
    if sid == "07":
        fr(c, "3", "4", W / 2, 470, 150, INK, ep(t, C["07.t"], 0.5))
        pill(c, "qual está em jogo? → a conta certa", W / 2, 760, GREEN, size=32, a=ep(t, C["07.b"], 0.5), anchor="center")
        return
    if sid == "08":
        a = ep(t, C["08"], 0.5)
        pizza(c, 620, 530, 220, 4, 3, a, pull=0.5)
        fr(c, "3", "4", 1200, 470, 110, INK, a)
        text(c, "o todo foi dividido em 4", 1200, 680, 34, "bold", INK2, ep(t, C["08.a"], 0.4))
        text(c, "e você pegou 3", 1200, 730, 34, "black", "#C9532A", ep(t, C["08.a"] + 1.0, 0.4))
    elif sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        cols = [BLUE, GREEN, AMBER, ROSA]
        for b in range(3):
            x = 290 + b * 260
            sp = ep(t, C["09.b"], 0.6)
            sel = {i: cols[i] for i in range(4)}
            # cada barra: 4 pedaços, um para cada pessoa
            c.save()
            for k in range(4):
                col = mix(K.CHOCO, cols[k], sp)
                rrect(c, x, 300 + k * (88 + 8 * sp), 210, 86, 10, col, aa, shadow=True)
            c.restore()
        for k in range(4):
            pessoa(c, 1180 + k * 150, 560, cols[k], ep(t, C["09.a"] + 0.3 * k, 0.3))
        expr(c, "3 ÷ 4 = 0,75", 1400, 680, 60, ep(t, C["09.c"], 0.5), cores={4: GREEN})
        text(c, "de barra para cada pessoa", 1400, 760, 30, "bold", INK2, ep(t, C["09.d"], 0.4))
        text(c, "QUOCIENTE = resultado de uma divisão", 560, 810, 28, "black", BLUE, ep(t, C["09"], 0.5))
    elif sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        for k in range(3):
            pessoa(c, 330 + k * 130, 540, BLUE, aa * ep(t, C["10.a"] + 0.2 * k, 0.3))
        for k in range(4):
            pessoa(c, 900 + k * 130, 540, ROSA, aa * ep(t, C["10.a"] + 0.6 + 0.2 * k, 0.3))
        text(c, "3 meninos", 460, 620, 34, "black", BLUE, aa)
        text(c, "para cada 4 meninas", 1095, 620, 34, "black", ROSA, aa)
        fr(c, "3", "4", 1560, 420, 90, INK, aa, num_col=BLUE, den_col=ROSA)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            boxed(c, 480, 690, 960, 110, AMBER, ab, 0.14)
            text_mid(c, "o 4 NÃO é o total (o total é 3 + 4 = 7)", W / 2, 745, 34, "black", INK, ab)
        text(c, "RAZÃO = comparação entre duas quantidades", W / 2, 300, 30, "black", BLUE, ep(t, C["10"], 0.5) * (1 - ab))
    else:   # 11 operador
        aa = ep(t, C["11.a"], 0.5)
        text(c, "OPERADOR = a fração que age sobre uma quantidade", W / 2, 300, 30, "black", BLUE, ep(t, C["11"], 0.5))
        expr(c, "3/4 de R$200", 560, 430, 64, aa)
        ab = ep(t, C["11.b"], 0.5)
        for k in range(4):
            on_ = ep(t, C["11.c"] + 0.3 * k, 0.4) if k < 3 else 0
            x = 220 + k * 175
            nota(c, x, 560, ab * ep(t, C["11.b"] + 0.25 * k, 0.3), "50", mix("#8BC9A4", "#16A36A", on_))
        expr(c, "200 ÷ 4 = 50", 1300, 470, 54, ab)
        expr(c, "3 · 50 = 150", 1300, 600, 54, ep(t, C["11.c"], 0.5), cores={4: GREEN})
        text(c, "R$ 150", 1300, 740, 60, "black", GREEN, ep(t, C["11.c"] + 1.6, 0.4))


# ======================================================================
# bloco C — "de" é vezes
# ======================================================================

def de_vezes(c, s_left, s_right, cx, cy, size, a, m, res=None, res_a=0.0):
    """desenha 's_left de s_right' com o 'de' se transformando em '·' (m = 0..1)"""
    tok = f"{s_left} de {s_right}"
    w = expr_w(tok, size)
    x0 = cx - w / 2
    wl = expr_w(s_left, size)
    wde = expr_w("de", size)
    gap = size * 0.32
    expr(c, s_left, x0, cy, size, a, align="left")
    xd = x0 + wl + gap + wde / 2
    fmid(c, "de", xd, cy - 30 * m, size, "black", AMBER, a * (1 - m))
    fmid(c, "×", xd, cy, size * 1.1, "black", PURPLE, a * m)
    expr(c, s_right, x0 + wl + 2 * gap + wde, cy, size, a, align="left")
    if res and res_a > 0:
        fmid(c, "= " + res, x0 + w + gap + expr_w("= " + res, size) / 2, cy, size, "black", GREEN, res_a)


def b_de(c, t, C, B):
    head_seq(c, t, C, [("12", "A PALAVRA QUE RESOLVE", "“DE” É VEZES", PURPLE), ("13", "MAIS UM EXEMPLO", "2/5 DE 300 ALUNOS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        m = ep(t, C["12.b"], 0.8)
        de_vezes(c, "3/4", "200", 860, 420, 96, aa, m, "150", ep(t, C["12.c"], 0.5))
        pill(c, "fração + “de” + quantidade = MULTIPLICAR", W / 2, 680, PURPLE, size=34, a=ep(t, C["12.b"] + 0.8, 0.4), anchor="center")
        return
    a0 = ep(t, C["13"], 0.5)
    de_vezes(c, "2/5", "300", 560, 300, 70, a0, ep(t, C["13.a"], 0.6))
    # 300 alunos em 5 grupos de 60
    ac = ep(t, C["13.c"], 0.5)
    for g in range(5):
        on_ = ep(t, C["13.d"] + 0.3 * g, 0.4) if g < 2 else 0
        x = 220 + g * 150
        a = ac * ep(t, C["13.c"] + 0.15 * g, 0.3)
        if a <= 0:
            continue
        rrect(c, x, 440, 130, 220, 16, mix("#F2F2EF", GREEN, 0.7 * on_), a)
        for r_ in range(4):
            for k in range(3):
                c.drawCircle(x + 30 + k * 35, 480 + r_ * 42, 12, paint(mix(INK2, "#FFFFFF", on_), a))
        text(c, "60", x + 65, 700, 32, "black", GREEN if on_ > 0.5 else INK2, a)
    ab = ep(t, C["13.a"], 0.5)
    if ab > 0:
        boxed(c, 1050, 420, 620, 150, GREEN, ab, 0.08)
        text(c, "ATALHO", 1360, 462, 22, "black", GREEN, ab, tracking=2)
        text(c, "divida pelo de BAIXO", 1360, 510, 34, "black", INK, ab)
        text(c, "multiplique pelo de CIMA", 1360, 552, 34, "black", INK, ep(t, C["13.b"], 0.4))
    expr(c, "300 ÷ 5 = 60", 1360, 650, 50, ac)
    expr(c, "60 · 2 = 120", 1360, 750, 50, ep(t, C["13.d"], 0.5), cores={4: GREEN})


# ======================================================================
# bloco D — frações equivalentes
# ======================================================================

def b_equivalentes(c, t, C, B):
    head_seq(c, t, C, [("14", "2 FATIAS GRANDES OU 4 PEQUENAS?", "METADE É METADE", BLUE),
                       ("15", "A MESMA METADE", "RECORTADA", BLUE), ("16", "A REGRA", "MESMO NÚMERO EM CIMA E EMBAIXO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16"])
    if sid == "14":
        a0 = ep(t, C["14.t"], 0.5)
        pizza(c, 600, 470, 210, 2, 1, a0, sel_col=BLUE)
        pizza(c, 1320, 470, 210, 4, 2, ep(t, C["14.t"] + 0.6, 0.5), sel_col=BLUE)
        fmid(c, "=", W / 2 + 0, 470, 120, "black", GREEN, ep(t, C["14.a"], 0.4))
        pill(c, "FRAÇÕES EQUIVALENTES = mesma quantidade, outro jeito de escrever", W / 2, 790, BLUE, size=28,
             a=ep(t, C["14.c"], 0.5), anchor="center")
        return
    if sid == "15":
        items = [("15.a", 2, "1/2"), ("15.b", 4, "2/4"), ("15.c", 6, "3/6")]
        for k, (cue, n, lab) in enumerate(items):
            a = ep(t, C[cue], 0.5)
            x = 340 + k * 400
            pizza(c, x, 370, 140, n, n // 2, a, sel_col=BLUE)
            n_, d_ = lab.split("/")
            fr(c, n_, d_, x, 570, 60, BLUE, a)
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            # 100 quadradinhos com 50 acesos
            for i in range(100):
                r_, k = divmod(i, 10)
                rrect(c, 1450 + k * 25, 250 + r_ * 25, 21, 21, 4, BLUE if k < 5 else "#E6E6E2", ad)
            fr(c, "50", "100", 1575, 570, 56, BLUE, ad)
        expr(c, "1/2 = 2/4 = 3/6 = 50/100 = 0,5", W / 2, 790, 52, ep(t, C["15.e"], 0.5), cores={8: GREEN})
        return
    # 16 regra
    aa = ep(t, C["16.a"], 0.5)
    regra(c, "× ou ÷ em cima e embaixo pelo MESMO número", W / 2, 240, aa, 38)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        expr(c, "1/2 → 2/4", 520, 430, 80, ab, cores={0: BLUE, 2: BLUE})
        fmid(c, "×2", 520, 330, 34, "black", PURPLE, ab)
        fmid(c, "×2", 520, 545, 34, "black", PURPLE, ab)
        text(c, "o valor não muda", 520, 650, 34, "black", GREEN, ab)
    acc = ep(t, C["16.c"], 0.5)
    split = ep(t, C["16.c"] + 1.0, 0.8)
    n = 2 if split < 0.5 else 4
    pizza(c, 1300, 480, 210, n, n // 2, acc, sel_col=BLUE, cut=1)
    text(c, "cada fatia cortada em 2", 1300, 760, 30, "bold", INK2, acc)
    text(c, "pegou o dobro · a pizza tem o dobro", 1300, 810, 30, "black", GREEN, ep(t, C["16.d"], 0.4))


# ======================================================================
# bloco E — produto cruzado
# ======================================================================

def b_cruzado(c, t, C, B):
    frame(c, t, B["start"], "SÃO EQUIVALENTES?", "O PRODUTO CRUZADO", PURPLE)
    aa = ep(t, C["17.a"], 0.5)
    fr(c, "6", "9", 700, 400, 120, INK, aa)
    fr(c, "10", "15", 1220, 400, 120, INK, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        line(c, 760, 330, 1150, 470, PURPLE, ab, 6, progress=ep(t, C["17.c"], 0.6))
        line(c, 760, 470, 1150, 330, AMBER, ab, 6, progress=ep(t, C["17.d"], 0.6))
        pill(c, "PRODUTO CRUZADO = multiplicar em X", W / 2, 230, PURPLE, size=28, a=ab, anchor="center", bounds=(0, 1920))
    fmid(c, "6 · 15 = 90", 640, 660, 54, "black", PURPLE, ep(t, C["17.c"], 0.5))
    fmid(c, "9 · 10 = 90", 1280, 660, 54, "black", AMBER, ep(t, C["17.d"], 0.5))
    ae = ep(t, C["17.e"], 0.5)
    check_icon(c, 760, 780, 26, ae, GREEN)
    text(c, "deu o mesmo → EQUIVALENTES", 800, 794, 40, "black", GREEN, ae, align="left")


# ======================================================================
# bloco F — simplificar
# ======================================================================

def b_simplificar(c, t, C, B):
    head_seq(c, t, C, [("18", "84/120 ASSUSTA?", "SIMPLIFICAR", BLUE), ("19", "NÃO SIMPLIFICA MAIS", "FRAÇÃO IRREDUTÍVEL", BLUE),
                       ("20", "ATALHO", "DIVIDA PELO MDC", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19", "20"])
    if sid in ("18", "19"):
        steps = [("18.t", "84", "120", None), ("18.b", "42", "60", "÷2"), ("18.c", "21", "30", "÷2"), ("18.d", "7", "10", "÷3")]
        for k, (cue, n_, d_, op) in enumerate(steps):
            a = ep(t, C[cue], 0.5)
            x = 330 + k * 420
            last = k == 3
            col = BLUE if last and t > C["18.d"] else INK
            if last and sid == "19":
                rrect(c, x - 110, 300, 220, 260, 22, BLUE, 0.12 * ep(t, C["19"], 0.4))
            fr(c, n_, d_, x, 410, 96, col, a)
            if op:
                arrow(c, x - 330, 420, x - 120, 420, LIGHT, a, 5, 16, progress=a)
                fmid(c, op, x - 225, 380, 34, "black", PURPLE, a)
        pill(c, "SIMPLIFICAR = ÷ em cima e embaixo pelo mesmo número", W / 2, 650, BLUE, size=28,
             a=ep(t, C["18.a"], 0.5) * (1 - ep(t, C["19"], 0.4)), anchor="center")
        if sid == "19":
            a = ep(t, C["19.a"], 0.5)
            text(c, "só o 1 divide o 7 e o 10 ao mesmo tempo", W / 2, 660, 36, "black", INK2, a)
            pill(c, "IRREDUTÍVEL = simplificada ao máximo", W / 2, 760, BLUE, size=32, a=ep(t, C["19.b"], 0.5), anchor="center")
        return
    # 20: o varal e o MDC
    aa = ep(t, C["20.a"], 0.5)
    rows = [("84", "120", "2"), ("42", "60", "2"), ("21", "30", "3"), ("7", "10", "")]
    acv = ep(t, C["20.c"], 0.5)
    for k, (x1, x2, dv) in enumerate(rows):
        a = acv * ep(t, C["20.c"] + 0.7 * k, 0.3)
        y = 280 + k * 90
        text(c, x1, 330, y, 48, "black", INK, a, align="right")
        text(c, x2, 520, y, 48, "black", INK, a, align="right")
        if dv:
            line(c, 560, y - 50, 560, y + 30, INK2, a, 4)
            text(c, dv, 600, y, 48, "black", GREEN, a, align="left")
            check_icon(c, 690, y - 16, 18, a, GREEN)
    ad = ep(t, C["20.d"], 0.5)
    fmid(c, "MDC = 2 · 2 · 3 = 12", 470, 690, 50, "black", GREEN, ad)
    pill(c, "o varal da série anterior", 470, 780, GREEN, size=26, a=aa, anchor="center", bounds=(0, 1920))
    ae = ep(t, C["20.e"], 0.5)
    if ae > 0:
        fr(c, "84", "120", 1050, 420, 90, INK, ae)
        arrow(c, 1150, 430, 1330, 430, GREEN, ae, 6, 18, progress=ae)
        fmid(c, "÷12", 1240, 380, 36, "black", GREEN, ae)
        fr(c, "7", "10", 1450, 420, 90, BLUE, ep(t, C["20.f"], 0.4))
        pill(c, "de uma vez só", 1250, 640, GREEN, size=34, a=ep(t, C["20.f"], 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco G — dica de prova
# ======================================================================

def b_dica(c, t, C, B):
    frame(c, t, B["start"], "DICA DE PROVA", "SIMPLIFIQUE ANTES DA CONTA", GREEN)
    aa = ep(t, C["21.a"], 0.5)
    expr(c, "15/25 de 40", W / 2, 260, 64, aa)
    ab = ep(t, C["21.b"], 0.5)
    if ab > 0:
        text(c, "o caminho longo", 520, 400, 26, "bold", GRAY, ab)
        expr(c, "15 · 40 = 600", 520, 480, 44, ab * 0.55)
        expr(c, "600 ÷ 25 = 24", 520, 570, 44, ab * 0.55)
        boxed(c, 1000, 360, 700, 300, GREEN, ab, 0.06)
        text(c, "simplificando ANTES", 1350, 405, 26, "black", GREEN, ab)
        expr(c, "15/25 = 3/5", 1350, 490, 54, ab, cores={2: GREEN})
    acc = ep(t, C["21.c"], 0.5)
    expr(c, "40 ÷ 5 = 8 → 8 · 3 = 24", 1350, 610, 42, acc, cores={8: GREEN})
    pill(c, "números pequenos = menos erro", W / 2, 780, GREEN, size=32, a=ep(t, C["21.d"], 0.5), anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("22", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("23", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    a1, a2 = ep(t, C["22.a"], 0.5), ep(t, C["22.b"], 0.5)
    for k, (a, s) in enumerate(((a1, "3/4 de 60"), (a2, "18/24"))):
        x = 560 + k * 800
        if a <= 0:
            continue
        rrect(c, x - 330, 220, 660, 240, 24, "#F7F7F5", a)
        text(c, "1ª CONTA" if k == 0 else "2ª CONTA (simplifique)", x, 270, 24, "black", GRAY, a, tracking=1)
        expr(c, s + " = ?", x, 380, 72, a)
    pause_timer(c, t, C["22.end"] - 1.9, W / 2, 560)
    if t >= C["23"]:
        ra = ep(t, C["23.a"], 0.5)
        expr(c, "60 ÷ 4 = 15 → 15 · 3 = 45", 560, 590, 40, ra, cores={8: GREEN})
        rb = ep(t, C["23.b"], 0.5)
        text(c, "MDC(18, 24) = 6", 1360, 560, 36, "black", PURPLE, rb)
        expr(c, "18/24 = 3/4", 1360, 680, 60, ep(t, C["23.c"], 0.5), cores={2: GREEN})


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Denominador: em quantas fatias. Numerador: quantas você pegou.", "“De” significa vezes.",
          "Simplificar é ÷ em cima e embaixo pelo mesmo número; pelo MDC, de uma vez."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["24", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "24" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1340, 54)


ERROS = [("Somar ou subtrair quando o enunciado diz “3/4 DE”", "a palavra “de” não tem cara de conta",
          "“de” é vezes: divida pelo de baixo e multiplique pelo de cima"),
         ("Simplificar só o numerador (ou dividir por números diferentes)", "os números ficam menores",
          "em cima e embaixo, sempre pelo MESMO número"),
         ("Deixar sem simplificar quando pedem a irredutível", "a fração tem o mesmo valor",
          "a não simplificada é alternativa errada: confira se ainda dá para dividir")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["25", "26", "27"], ERROS)


# ======================================================================
# questão inédita
# ======================================================================

ALTS = [("A", "= 3/20", "esqueceu o “de”: 18 de 120", RED), ("B", "= 1/4", "subtraiu: 18 de 72", RED),
        ("C", "= 3/8", "", GREEN), ("D", "= 18/48", "não simplificou", AMBER), ("E", "= 3/48", "dividiu só o numerador", RED)]


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "A HORA EXTRA DO TURNO DA NOITE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.5)
    rows = [("28.a", "Uma empresa tem 120 funcionários."), ("28.b", "Desses, 2/5 trabalham no turno da noite."),
            ("28.c", "Entre os da noite, 18 fazem hora extra."),
            ("28.d", "Que fração dos funcionários da noite faz hora extra, na forma irredutível?")]
    y = 240
    for cue, s in rows:
        a = ep(t, C[cue], 0.4)
        y += para(c, s, 190, y, 30, "black" if cue != "28.d" else "bold", INK if cue != "28.d" else BLUE, a, 560, 38) + 14
    text(c, "Situação elaborada para fins didáticos.", 190, 830, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"29.{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["31.xa"], "B": C["31.xb"], "D": C["31.xd"], "E": C["31.xe"]}
    if t >= C["29"] - 0.3:
        K.alternativas(c, t, C, ALTS, 870, 205, 820, 42, C["30.ok"], "C", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["29.end"] - 1.9, 470, 720)
    # resolução (cena 30) embaixo do enunciado
    ra = ep(t, C["30.a"], 0.4) * (1 - ep(t, C["31"], 0.4))
    if ra > 0:
        rrect(c, 170, 560, 600, 250, 18, "#FFFFFF", ra, shadow=True)
        expr(c, "2/5 · 120 = 48", 470, 620, 44, ep(t, C["30.b"], 0.4), cores={4: GREEN})
        expr(c, "18/48 = 3/8", 470, 740, 52, ep(t, C["30.d"], 0.4), cores={2: GREEN})
    result_box(c, "Letra C", 470, 700, 50, ep(t, C["31"], 0.5), GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MISTOS E QUAL É MAIOR", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    pizza(c, 330, 420, 130, 4, 4, aa)
    pizza(c, 620, 420, 130, 4, 4, aa)
    pizza(c, 910, 420, 130, 4, 3, aa)
    expr(c, "2|3/4", 620, 650, 70, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        expr(c, "3/5 ou 3/7 ?", 1400, 420, 80, ab)
        text(c, "qual é MAIOR?", 1400, 560, 44, "black", AMBER, ab)
    pill(c, "ep. 2 · números mistos e comparação de frações", W / 2, 780, PURPLE, size=32, a=ep(t, C["33.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Quanto deu 3/4 de 60 para você?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, pizza=b_pizza, significados=b_significados, de=b_de,
              equivalentes=b_equivalentes, cruzado=b_cruzado, simplificar=b_simplificar, dica=b_dica, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, questao=b_questao, ponte=b_ponte, cta=b_cta)
