"""Visual — Divisão Proporcional, Episódio 3: divisão composta e regra de sociedade (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: pessoa() (bonequinho), quadros() (retângulo de quadradinhos pessoas × dias, que vira o peso),
tabela() (séries lado a lado, com a linha dos produtos), area() (barra capital × barra tempo = área do peso).
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
_s = importlib.util.spec_from_file_location("comum023", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisao_ep3_composta_sociedade.mp4"
CARD_R = K.CARD_R
AZUL_EQ = "#3E7BFA"
VERDE_EQ = "#16A36A"
LARANJA = "#E8743B"
CORES_EQ = ["#3E7BFA", "#E8743B", "#8B5CF6"]
DINHEIRO = "#2F9E6B"


# ======================================================================
# peças do episódio
# ======================================================================

def pessoa(c, x, y, s, col, a):
    """bonequinho: (x, y) = centro da cabeça; s = altura total"""
    if a <= 0:
        return
    c.drawCircle(x, y, s * 0.18, paint(col, a))
    rrect(c, x - s * 0.22, y + s * 0.24, s * 0.44, s * 0.52, s * 0.16, col, a)


def quadros(c, x, y, cols, rows, cell, a, prog=1.0, col=None, gap=6):
    """retângulo de quadradinhos cols × rows; prog = 0..1 vai preenchendo; devolve quantos já apareceram"""
    if a <= 0:
        return 0
    col = col or GREEN
    n = cols * rows
    vis = prog * n
    for r in range(rows):
        for k in range(cols):
            i = r * cols + k
            ak = a * clamp(vis - i, 0, 1)
            rrect(c, x + k * cell, y + r * cell, cell - gap, cell - gap, 8, "#E9EDF3", a)
            if ak > 0:
                rrect(c, x + k * cell, y + r * cell, cell - gap, cell - gap, 8, col, ak)
    return int(min(n, math.floor(vis + 1e-6)))


def tabela(c, x, y, cab, linhas, a, colw=170, rowh=86, labw=300, hl_col=None, hl_a=0.0):
    """séries lado a lado. cab = ['eq 1', ...]; linhas = [(rótulo, [valores], cor, alfa)]. hl_col = índice da coluna
    em destaque (termos correspondentes)"""
    if a <= 0:
        return
    n = len(cab)
    for j, s in enumerate(cab):
        cx = x + labw + j * colw + colw / 2
        pill(c, s, cx, y + 30, CORES_EQ[j % len(CORES_EQ)], size=24, a=a, anchor="center")
    if hl_col is not None and hl_a > 0:
        cx = x + labw + hl_col * colw
        boxed(c, cx + 8, y + 64, colw - 16, rowh * len(linhas) + 8, AMBER, a * hl_a, 0.10)
    for i, (rot, vals, col, al) in enumerate(linhas):
        ai = a * al
        if ai <= 0:
            continue
        yy = y + 70 + i * rowh + rowh / 2
        text(c, rot, x + labw - 24, yy + 11, 30, "black", col, ai, align="right")
        for j, v in enumerate(vals):
            ftext(c, v, x + labw + j * colw + colw / 2, yy + 16, 46, "black", col, ai)


def area(c, x, y, w, h, a, col, rot_w, rot_h, prog=1.0, rot_area=None):
    """capital (largura) × tempo (altura) = área do peso; (x, y) = canto inferior esquerdo"""
    if a <= 0:
        return
    pw = w * clamp(prog * 2, 0, 1)
    ph = h * clamp(prog * 2 - 1, 0, 1)
    rrect(c, x, y - 18, w, 18, 6, col, a * 0.35)
    rrect(c, x, y - 18, pw, 18, 6, col, a)
    rrect(c, x - 18, y - h, 18, h, 6, col, a * 0.35)
    if ph > 0:
        rrect(c, x - 18, y - ph, 18, ph, 6, col, a)
        rrect(c, x, y - ph, w, ph - 18 if ph > 18 else 0, 10, col, a * 0.22)
    text(c, rot_w, x + w / 2, y + 44, 28, "black", col, a)
    ftext(c, rot_h, x - 34, y - h / 2 + 10, 28, "black", col, a, align="right")
    if rot_area and prog >= 1:
        ftext(c, rot_area, x + w / 2, y - h / 2 + 4, 38, "black", INK, a)


def caixa(c, x, y, s, ok, a):
    """a balança de caixa: a soma das partes fecha (verde) ou não (vermelho)"""
    if a <= 0:
        return
    w = max(420, ftext_w(s) + 120)
    rrect(c, x, y, w, 70, 16, GREEN if ok else RED, a * 0.12)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, 70), 16, 16), paint(GREEN if ok else RED, a, stroke=4))
    check_icon(c, x + 38, y + 35, 20, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + 72, y + 47, 30, "black", GREEN if ok else RED, a, align="left")


def ftext_w(s, size=30):
    return K.ftext_w(s, "black", size)


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "MULTIPLICAR, NUNCA SOMAR", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        card(c, 260, 220, 520, 330, aa)
        for k in range(5):
            pessoa(c, 330 + k * 95, 300, 110, AZUL_EQ, aa * ep(t, C["01.a"] + 0.1 * k, 0.3))
        text(c, "PESSOAS", 520, 500, 40, "black", AZUL_EQ, aa)
        card(c, 1140, 220, 520, 330, aa)
        for k in range(2):
            rrect(c, 1290 + k * 130, 270, 100, 110, 14, "#FFFFFF", aa, shadow=True)
            rrect(c, 1290 + k * 130, 270, 100, 30, 10, RED, aa)
            text(c, str(k + 1), 1340 + k * 130, 362, 46, "black", INK, aa)
        text(c, "DIAS", 1400, 500, 40, "black", LARANJA, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        s = 1 + 0.1 * math.sin(math.pi * prog(t, C["01.b"] + 0.2, 0.5))
        c.save(); c.translate(960, 385); c.scale(s, s); c.translate(-960, -385)
        fmid(c, "+ ?", 960, 385, 120, "black", AMBER, ab)
        c.restore()
        text(c, "o instinto: somar", 960, 500, 30, "bold", AMBER, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        card(c, 640, 600, 640, 170, acc)
        badge_num(c, "D", 720, 685, acc, 26, bg=INK)
        ftext(c, "5 + 2 = 7", 960, 705, 64, "black", RED, acc)
        selo(c, 1240, 780, acc, "ESPERANDO POR VOCÊ", RED, -6, 28)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "dividir com DOIS critérios", "pessoas e dias, área e moradores..."),
            ("02.b", "resolver questões de sociedade", "lucro e prejuízo pelo capital"),
            ("02.c", "sócios com tempos diferentes", "capital × tempo")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", BLUE)
    cols = [("03.a", "EPISÓDIO 1", "OS PACOTINHOS", BLUE), ("03.b", "EPISÓDIO 2", "A INVERSA", PURPLE),
            ("03.c", "MDC", "SIMPLIFICAR", GREEN)]
    for j, (cue, l1, l2, col) in enumerate(cols):
        a, d = rise(t, C[cue])
        x = 200 + j * 520
        if a <= 0:
            continue
        boxed(c, x, 250 + d, 480, 520, col, a, 0.06)
        pill(c, l1, x + 240, 300 + d, col, size=22, a=a, anchor="center")
        text(c, l2, x + 240, 380 + d, 38, "black", col, a)
        if j == 0:
            ftext(c, "k = total ÷ soma", x + 240, 500 + d, 40, "black", INK, a)
            ftext(c, "parte = k × peso", x + 240, 590 + d, 40, "black", INK, a)
            text(c, "k = valor de UM pacotinho", x + 240, 690 + d, 26, "bold", GRAY, a)
        elif j == 1:
            expr(c, "2 → 1/2", x + 240, 520 + d, 62, a, cores={2: PURPLE})
            text(c, "troque pelo INVERSO", x + 240, 660 + d, 28, "bold", GRAY, a)
        else:
            ftext(c, "60 : 40", x + 240, 500 + d, 48, "black", INK, a)
            ftext(c, "÷ 20", x + 240, 570 + d, 34, "black", GREEN, a)
            ftext(c, "3 : 2", x + 240, 640 + d, 48, "black", GREEN, a)
            text(c, "a mesma divisão", x + 240, 720 + d, 26, "bold", GRAY, a)


# ======================================================================
# concreto: as equipes e as amigas
# ======================================================================

def b_historia(c, t, C, B):
    head_seq(c, t, C, [("04", "UMA HISTÓRIA", "A VERBA DO MUTIRÃO", BLUE), ("05", "E NOS NEGÓCIOS", "A LOJA DAS AMIGAS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        for j, (cue, nome, np_, dias, col) in enumerate([("04.a", "AZUL", 2, 3, AZUL_EQ), ("04.b", "VERDE", 5, 2, VERDE_EQ)]):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            x = 230 + j * 760
            boxed(c, x, 220, 700, 420, col, a, 0.06)
            pill(c, f"EQUIPE {nome}", x + 350, 270, col, size=26, a=a, anchor="center")
            for k in range(np_):
                pessoa(c, x + 350 - (np_ - 1) * 55 + k * 110, 340, 120, col, a * ep(t, C[cue] + 0.12 * k, 0.3))
            text(c, f"{np_} pessoas", x + 350, 520, 40, "black", INK, a)
            for k in range(dias):
                rrect(c, x + 350 - dias * 45 + k * 90 + 10, 545, 70, 70, 10, "#FFFFFF", a, shadow=True)
                rrect(c, x + 350 - dias * 45 + k * 90 + 10, 545, 70, 20, 8, RED, a)
                text(c, str(k + 1), x + 350 - dias * 45 + k * 90 + 45, 605, 30, "black", INK, a)
            text(c, f"{dias} dias", x + 350 + dias * 45 + 70, 595, 32, "black", LARANJA, a, align="left")
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            text(c, "Quem trabalhou mais?", W / 2, 720, 44, "black", AMBER, acc)
        selo(c, W / 2, 790, ep(t, C["04.d"], 0.5), "OS DOIS CRITÉRIOS CONTAM", PURPLE, -2, 30)
        return
    for j, (cue, nome, cap, mes, col) in enumerate([("05.a", "AMIGA 1", "R$ 10 mil", "12 meses", AZUL_EQ),
                                                     ("05.b", "AMIGA 2", "R$ 20 mil", "3 meses", LARANJA)]):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 230 + j * 760
        boxed(c, x, 230, 700, 380, col, a, 0.06)
        pessoa(c, x + 130, 360, 170, col, a)
        pill(c, nome, x + 130, 520, col, size=24, a=a, anchor="center")
        ftext(c, cap, x + 450, 380, 56, "black", DINHEIRO, a)
        ftext(c, mes, x + 450, 480, 44, "black", INK, a)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        text(c, "Quem merece mais do lucro?", W / 2, 720, 46, "black", AMBER, acc)


# ======================================================================
# bloco A — a regra da composta
# ======================================================================

def b_regra(c, t, C, B):
    head_seq(c, t, C, [("06", "A REGRA", "DIVISÃO COMPOSTA", PURPLE), ("07", "E SE UM CRITÉRIO FOR INVERSO?", "INVERTA ANTES", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        a0 = ep(t, C["06"], 0.5)
        boxed(c, 200, 190, 1520, 70, BLUE, a0, 0.08)
        text_mid(c, "DIVISÃO COMPOSTA = dividir por DOIS critérios ao mesmo tempo", W / 2, 225, 30, "black", BLUE, a0)
        aa = ep(t, C["06.a"], 0.5)
        hl = ep(t, C["06.b"], 0.5) * (1 - ep(t, C["06.d"] + 0.5, 0.5) * 0.5)
        dd = ep(t, C["06.d"], 0.5)
        tabela(c, 300, 300, ["eq 1", "eq 2", "eq 3"],
               [("integrantes", ["2", "3", "5"], AZUL_EQ, 1), ("dias", ["3", "4", "2"], LARANJA, 1),
                ("PESOS", ["6", "12", "10"], GREEN, dd)], aa, colw=230, hl_col=2 if t < C["06.c"] else None, hl_a=hl)
        if aa > 0:
            text(c, "SÉRIE = uma lista, na ordem das equipes", 1500, 420, 24, "black", BLUE, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            text(c, "TERMOS CORRESPONDENTES =", 1500, 520, 24, "black", AMBER, ab)
            text(c, "os da mesma equipe", 1500, 556, 24, "black", AMBER, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            for j in range(3):
                ftext(c, "×", 300 + 300 + j * 230 + 115, 466, 26, "black", PURPLE, acc)
            selo(c, 1500, 680, acc, "MULTIPLIQUE OS DA MESMA EQUIPE", PURPLE, -3, 24)
        return
    aa = ep(t, C["07.a"], 0.5)
    bb = ep(t, C["07.b"], 0.5)
    cc = ep(t, C["07.c"], 0.5)
    tabela(c, 330, 220, ["grupo 1", "grupo 2"],
           [("pessoas (direta)", ["2", "3"], AZUL_EQ, 1), ("faltas (INVERSA)", ["1", "3"], RED, 1 - 0.6 * bb)], aa, colw=260)
    if bb > 0:
        text(c, "inverta só a série inversa", 1430, 360, 28, "black", RED, bb)
        text(c, "inversos", 330 + 276, 560 + 30, 30, "black", PURPLE, bb, align="right")
        ftext(c, "1", 330 + 300 + 130, 600, 46, "black", PURPLE, bb)
        expr(c, "1/3", 330 + 300 + 260 + 130, 585, 46, bb, cores={0: PURPLE})
    if cc > 0:
        text(c, "PESOS", 330 + 276, 700 + 30, 30, "black", GREEN, cc, align="right")
        ftext(c, "2 × 1 = 2", 330 + 300 + 130, 740, 38, "black", GREEN, cc)
        ftext(c, "3 × ⅓ = 1", 330 + 300 + 260 + 130, 740, 38, "black", GREEN, cc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        boxed(c, 1270, 560, 420, 200, GREEN, ad, 0.08)
        text(c, "pesos", 1480, 620, 30, "black", GREEN, ad)
        ftext(c, "2 : 1", 1480, 715, 72, "black", GREEN, ad)


# ======================================================================
# bloco B — eu faço (R$ 5 600)
# ======================================================================

def b_eufaco(c, t, C, B):
    head_seq(c, t, C, [("08", "EU FAÇO", "R$ 5 600 PARA 3 EQUIPES", BLUE), ("09", "O PROCEDIMENTO DE SEMPRE", "SOME, DIVIDA, MULTIPLIQUE", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["08.a"], 0.5)
    if a0 > 0:
        ftext(c, "R$ 5 600", 1480, 260, 64, "black", DINHEIRO, a0)
    ab, ac, ad = ep(t, C["08.b"], 0.5), ep(t, C["08.c"], 0.5), ep(t, C["08.d"], 0.5)
    pa = ep(t, C["09.c"], 0.5) if t >= C["09"] else 0
    tabela(c, 180, 200, ["eq 1", "eq 2", "eq 3"],
           [("integrantes", ["2", "3", "5"], AZUL_EQ, ab), ("dias", ["3", "4", "2"], LARANJA, ac),
            ("pesos", ["6", "12", "10"], GREEN, ad), ("partes", ["1 200", "2 400", "2 000"], DINHEIRO, pa)],
           max(ab, a0), colw=210, rowh=110, labw=260)
    if t < C["09"]:
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        ftext(c, "6 + 12 + 10 = 28", 1480, 380, 46, "black", INK, aa)
    abb = ep(t, C["09.b"], 0.5)
    if abb > 0:
        boxed(c, 1240, 430, 480, 130, PURPLE, abb, 0.08)
        ftext(c, "k = 5 600 ÷ 28", 1480, 482, 38, "black", PURPLE, abb)
        ftext(c, "= 200", 1480, 538, 46, "black", PURPLE, abb)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        text(c, "parte = 200 × peso", 1480, 620, 30, "black", DINHEIRO, acc)
    caixa(c, 1190, 690, "1 200 + 2 400 + 2 000 = 5 600", True, ep(t, C["09.d"], 0.5))


# ======================================================================
# bloco C — por que multiplicar
# ======================================================================

def b_porque(c, t, C, B):
    head_seq(c, t, C, [("10", "POR QUE MULTIPLICAR?", "PESSOA-DIA", BLUE), ("11", "O RETÂNGULO", "UNIDADES COMBINADAS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "equipe 3: 5 pessoas × 2 dias", 600, 250, 36, "black", INK, aa)
        n = quadros(c, 300, 300, 5, 2, 110, aa, ep(t, C["10.b"], 1.6), GREEN)
        if aa > 0:
            for k in range(5):
                pessoa(c, 300 + k * 110 + 52, 560, 70, AZUL_EQ, aa)
            text(c, "dia 1", 280, 365, 24, "black", LARANJA, aa, align="right")
            text(c, "dia 2", 280, 475, 24, "black", LARANJA, aa, align="right")
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            ftext(c, f"{n}", 600, 700, 90, "black", GREEN, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            pill(c, "PESSOA-DIA = 1 pessoa trabalhando 1 dia", 600, 790, BLUE, size=24, a=acc, anchor="center")
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            boxed(c, 1180, 300, 480, 300, RED, ad, 0.06)
            ftext(c, "5 + 2 = 7", 1420, 430, 64, "black", RED, ad)
            text(c, "7 o quê? não mede nada", 1420, 520, 28, "black", RED, ad)
            check_icon(c, 1640, 330, 30, ad, RED, "x")
        return
    aa = ep(t, C["11.a"], 0.5)
    quadros(c, 330, 280, 5, 2, 130, ep(t, C["11"], 0.5), ep(t, C["11.a"], 1.2), GREEN)
    if aa > 0:
        arrow(c, 330, 560, 330 + 5 * 130 - 6, 560, AZUL_EQ, aa, 4, 14)
        text(c, "largura = 5 pessoas", 330 + 325, 610, 30, "black", AZUL_EQ, aa)
        ftext(c, "2 dias", 310, 415, 30, "black", LARANJA, aa, align="right")
        ftext(c, "área = 10", 330 + 325, 690, 48, "black", GREEN, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        boxed(c, 1100, 250, 580, 170, BLUE, ab, 0.08)
        text(c, "UNIDADE COMBINADA", 1390, 305, 28, "black", BLUE, ab)
        text(c, "junta dois critérios numa coisa só", 1390, 360, 26, "bold", INK2, ab)
        text(c, "pessoa-dia · homem-hora · capital-mês", 1390, 400, 24, "bold", GRAY, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        selo(c, 1390, 490, acc, "SÓ EXISTEM MULTIPLICANDO", PURPLE, -3, 28)
    ad = ep(t, C["11.d"], 0.5)
    K.atalho(c, 1100, 570, 580, 220, "ATALHO", ["um critério = largura", "o outro = altura", "o peso = a ÁREA"], ad, 30)


# ======================================================================
# bloco D — simplificar só depois
# ======================================================================

def b_simplificar(c, t, C, B):
    head_seq(c, t, C, [("12", "DÁ PARA SIMPLIFICAR?", "SÓ DEPOIS DE MULTIPLICAR", AMBER), ("13", "A ORDEM", "GUARDE ASSIM", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        ab = ep(t, C["12.b"], 0.5)
        tabela(c, 240, 210, ["grupo 1", "grupo 2"],
               [("pessoas", ["6", "8"], AZUL_EQ, 1), ("dias", ["10", "5"], LARANJA, 1), ("produtos", ["60", "40"], GREEN, ab)],
               aa, colw=230)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            boxed(c, 300, 600, 640, 170, GREEN, acc, 0.08)
            ftext(c, "60 : 40   ÷ 20", 620, 665, 40, "black", INK, acc)
            ftext(c, "= 3 : 2", 620, 740, 56, "black", GREEN, acc)
            check_icon(c, 900, 640, 26, acc, GREEN)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            boxed(c, 1080, 360, 600, 300, RED, ad, 0.06)
            text(c, "simplificou SÓ as pessoas", 1380, 420, 30, "black", RED, ad)
            ftext(c, "6 : 8 = 3 : 4", 1380, 520, 56, "black", RED, ad)
            text(c, "e os dias sumiram!", 1380, 610, 30, "black", RED, ad)
            check_icon(c, 1650, 390, 28, ad, RED, "x")
        return
    passos = [("13.a", "MULTIPLIQUE", "as séries"), ("13.b", "SIMPLIFIQUE", "os pesos finais"), ("13.c", "SOME", "os pesos"),
              ("13.d", "ACHE O k", "total ÷ soma"), ("13.e", "MULTIPLIQUE", "k × cada peso")]
    for j, (cue, s, sub) in enumerate(passos):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + j * 312
        boxed(c, x, 300 + d, 280, 300, GREEN, a, 0.08)
        badge_num(c, j + 1, x + 140, 360 + d, a, 30, bg=GREEN)
        text(c, s, x + 140, 470 + d, 32, "black", INK, a)
        text(c, sub, x + 140, 530 + d, 24, "bold", GRAY, a)
        if j < 4:
            arrow(c, x + 284, 450 + d, x + 308, 450 + d, GREEN, a, 4, 10)
    selo(c, W / 2, 720, ep(t, C["13.e"] + 1.0, 0.5), "SIMPLIFICAR SÓ DEPOIS DE MULTIPLICAR", AMBER, -2, 30)


# ======================================================================
# bloco E — regra de sociedade
# ======================================================================

def _barras(c, x, base, vals, rots, cores, a, escala, larg=150, gap=60):
    for j, (v, r, col) in enumerate(zip(vals, rots, cores)):
        aj = a
        h = v * escala
        xx = x + j * (larg + gap)
        rrect(c, xx, base - h, larg, h, 12, col, aj)
        ftext(c, r, xx + larg / 2, base - h - 16, 32, "black", col, aj)


def b_sociedade(c, t, C, B):
    head_seq(c, t, C, [("14", "REGRA DE SOCIEDADE", "O LUCRO SEGUE O CAPITAL", PURPLE), ("15", "E O PREJUÍZO?", "FUNCIONA IGUAL", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        defs = [("14.a", "CAPITAL", "o dinheiro que cada sócio colocou", BLUE),
                ("14.b", "LUCRO", "o que a empresa ganhou", BLUE),
                ("14.c", "REGRA DE SOCIEDADE", "lucro proporcional ao capital", PURPLE)]
        for j, (cue, s, sub, col) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            boxed(c, 200, 210 + j * 135 + d, 640, 115, col, a, 0.08)
            text(c, s, 230, 258 + j * 135 + d, 30, "black", col, a, align="left")
            text(c, sub, 230, 300 + j * 135 + d, 26, "bold", INK2, a, align="left")
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            _barras(c, 960, 640, [30, 45, 75], ["30 000", "45 000", "75 000"], CORES_EQ, ad, 4.6, 190, 50)
        ae = ep(t, C["14.e"], 0.5)
        if ae > 0:
            ftext(c, "÷ 15 000", 1340, 700, 34, "black", GREEN, ae)
            for j, s in enumerate(["2", "3", "5"]):
                chip(c, s, 960 + 95 + j * 240, 775, GREEN, ae, 44)
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 200, 210, 700, 110, RED, aa, 0.06)
        text(c, "PREJUÍZO = quando a empresa perde dinheiro", 550, 278, 28, "black", RED, aa)
        text(c, "quem colocou mais, absorve mais", 550, 380, 30, "black", INK2, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        ftext(c, "R$ 10 000 em 2 : 3 : 5", 550, 480, 40, "black", INK, ab)
        ftext(c, "k = 10 000 ÷ 10 = 1 000", 550, 550, 36, "black", PURPLE, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        for j, s in enumerate(["− 2 000", "− 3 000", "− 5 000"]):
            pill(c, s, 260 + j * 220, 650, RED, size=30, a=acc * ep(t, C["15.c"] + 0.25 * j, 0.4))
        caixa(c, 240, 720, "2 000 + 3 000 + 5 000 = 10 000", True, ep(t, C["15.c"] + 1.0, 0.5))
    ad = ep(t, C["15.d"], 0.5)
    K.atalho(c, 1060, 300, 600, 280, "ATALHO", ["capitais grandes?", "simplifique pelo MDC", "ANTES de somar"], ad, 32)


# ======================================================================
# bloco F — sócios com tempos diferentes
# ======================================================================

def b_tempos(c, t, C, B):
    head_seq(c, t, C, [("16", "TEMPOS DIFERENTES", "CAPITAL × TEMPO", PURPLE), ("17", "O LUCRO DE R$ 9 000", "PACOTINHOS DE NOVO", PURPLE)])
    card(c, *CARD_R)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        boxed(c, 560, 190, 800, 72, PURPLE, ab, 0.08)
        text_mid(c, "PESO = CAPITAL × TEMPO", 960, 226, 36, "black", PURPLE, ab)
    acc = ep(t, C["16.c"], 0.5)
    area(c, 330, 680, 10 * 30, 6 * 40, acc, AZUL_EQ, "R$ 10 mil", "6 meses", ep(t, C["16.c"], 1.4), "60 mil")
    if acc > 0:
        pill(c, "SÓCIA A", 480, 330, AZUL_EQ, size=24, a=acc, anchor="center")
    ad = ep(t, C["16.d"], 0.5)
    area(c, 820, 680, 15 * 30, 8 * 40, ad, LARANJA, "R$ 15 mil", "8 meses", ep(t, C["16.d"], 1.4), "120 mil")
    if ad > 0:
        pill(c, "SÓCIA B", 1045, 330, LARANJA, size=24, a=ad, anchor="center")
    if t < C["17"]:
        return
    a0 = ep(t, C["17"], 0.5)
    if a0 > 0:
        chip(c, "1", 480, 770, GREEN, a0, 40)
        chip(c, "2", 1045, 770, GREEN, a0, 40)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        ftext(c, "9 000 ÷ 3", 1520, 330, 40, "black", INK, aa)
        ftext(c, "k = 3 000", 1520, 400, 46, "black", PURPLE, aa)
    abb = ep(t, C["17.b"], 0.5)
    if abb > 0:
        ftext(c, "A: 3 000", 1520, 480, 40, "black", AZUL_EQ, abb)
        ftext(c, "B: 6 000", 1520, 540, 40, "black", LARANJA, abb)
    caixa(c, 1300, 580, "3 000 + 6 000 = 9 000", True, ep(t, C["17.c"], 0.5))
    K.atalho(c, 1300, 670, 440, 150, "ATALHO", ["corte os zeros iguais"], ep(t, C["17.d"], 0.5), 30)


# ======================================================================
# bloco G — capital maior nem sempre leva mais
# ======================================================================

def b_capital(c, t, C, B):
    frame(c, t, B["start"], "CAPITAL MAIOR LEVA MAIS?", "NEM SEMPRE", AMBER)
    if t < C["18.d"]:
        aa = ep(t, C["18.a"], 0.5)
        area(c, 300, 640, 20 * 18, 12 * 30, aa, AZUL_EQ, "R$ 20 mil", "12 meses", ep(t, C["18.a"], 1.3), "240 mil")
        ab = ep(t, C["18.b"], 0.5)
        area(c, 960, 640, 30 * 18, 8 * 30, ab, LARANJA, "R$ 30 mil", "8 meses", ep(t, C["18.b"], 1.3), "240 mil")
        acc = ep(t, C["18.c"], 0.5)
        if acc > 0:
            fmid(c, "=", 790, 520, 90, "black", GREEN, acc)
            selo(c, W / 2, 780, acc, "MESMO PESO → PARTES IGUAIS", GREEN, -2, 30)
        return
    ad = ep(t, C["18.d"], 0.5)
    area(c, 300, 640, 10 * 30, 12 * 30, ad, AZUL_EQ, "R$ 10 mil", "12 meses", ep(t, C["18.d"], 1.3), "120 mil")
    area(c, 960, 640, 20 * 30, 3 * 30, ad, LARANJA, "R$ 20 mil", "3 meses", ep(t, C["18.d"] + 0.6, 1.3), "60 mil")
    if ad > 0:
        pill(c, "AMIGA 1", 450, 240, AZUL_EQ, size=24, a=ad, anchor="center")
        pill(c, "AMIGA 2", 1260, 460, LARANJA, size=24, a=ad, anchor="center")
    ae = ep(t, C["18.e"], 0.5)
    if ae > 0:
        selo(c, 1300, 300, ae, "COLOCOU MENOS, LEVA O DOBRO", GREEN, -3, 28)
        text(c, "quem manda é o PRODUTO", W / 2, 790, 34, "black", PURPLE, ae)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("20", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    rows = [("19.b", "GRUPO 1", "4 pessoas", "5 dias", "20.a", "4 × 5 = 20"),
            ("19.c", "GRUPO 2", "6 pessoas", "2 dias", "20.b", "6 × 2 = 12")]
    for j, (cue, g, p, d, rc, r) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 260 + j * 170
        pill(c, g, 250, y + 40, CORES_EQ[j], size=26, a=a)
        ftext(c, p, 520, y + 52, 44, "black", AZUL_EQ, a)
        ftext(c, d, 800, y + 52, 44, "black", LARANJA, a)
        if t >= C["20"]:
            ftext(c, r, 1180, y + 52, 46, "black", GREEN, ep(t, C[rc], 0.5))
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0 and t < C["20"]:
        text(c, "Quais são os PESOS?", W / 2, 640, 48, "black", PURPLE, ad)
    if t >= C["20"]:
        acc = ep(t, C["20.c"], 0.5)
        if acc > 0:
            boxed(c, 1000, 590, 560, 130, GREEN, acc, 0.08)
            ftext(c, "20 : 12  =  5 : 3", 1280, 672, 52, "black", GREEN, acc)
        add = ep(t, C["20.d"], 0.5)
        if add > 0:
            text(c, "o grupo MENOR leva mais: trabalhou mais dias", 600, 790, 30, "black", AMBER, add)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 740)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Dois critérios? Multiplique, nunca some.", "Unidades combinadas só existem multiplicando.",
          "Na sociedade, quem manda é capital vezes tempo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 58)


ERROS = [("Somar as duas séries (5 + 2 = 7)", "os dois critérios contam",
          "5 pessoas por 2 dias = 10 pessoa-dia, não 7: multiplique"),
         ("Simplificar uma série e esquecer a outra", "os números ficam pequenos e bonitos",
          "um critério sumiu da conta: multiplique primeiro, simplifique depois"),
         ("Dividir o lucro em partes iguais", "todos são sócios",
          "a regra de sociedade é proporcional ao capital: quem colocou mais, leva mais"),
         ("Achar que o capital maior sempre leva mais", "dinheiro maior assusta",
          "com tempos diferentes, o peso é capital × tempo: faça a conta")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25"], ERROS)


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


def _resolucao(c, a, y0, h):
    rrect(c, 170, y0, 740, h, 18, "#FFFFFF", a, shadow=True)


ALTS4 = [("A", "R$ 1.200,00", "a menor parte", RED), ("B", "R$ 1.600,00", "não sai da conta", RED),
         ("C", "R$ 2.000,00", "a equipe de 5 pessoas", RED), ("D", "R$ 2.400,00", "", GREEN),
         ("E", "R$ 2.800,00", "só os integrantes", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · DIVISÃO COMPOSTA", "EU FAÇO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    if t < C["27"]:
        _enunciado(c, [("Uma verba de R$ 5.600,00 será distribuída entre três equipes, proporcionalmente ao número de "
                        "integrantes de cada uma — 2, 3 e 5 — e ao número de dias trabalhados — 3, 4 e 2, respectivamente.", INK),
                       ("A equipe que receberá a maior verba ficará com", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABCE"}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS4, 1000, 230, 680, 40, C["27.ok"], "D", cues_in, cues_x, gap=26)
    if t >= C["27"]:
        ra = ep(t, C["27"], 0.4)
        _resolucao(c, ra, 220, 590)
        ftext(c, "2·3 = 6   3·4 = 12   5·2 = 10", 540, 300, 36, "black", INK, ep(t, C["27.a"], 0.4))
        ftext(c, "soma 28 → k = 200", 540, 370, 38, "black", PURPLE, ep(t, C["27.a"] + 0.8, 0.4))
        ftext(c, "1 200 · 2 400 · 2 000", 540, 450, 40, "black", DINHEIRO, ep(t, C["27.b"], 0.4))
        ftext(c, "maior: 12 × 200 = 2 400", 540, 520, 38, "black", GREEN, ep(t, C["27.b"], 0.4))
        ac = ep(t, C["27.c"], 0.4)
        if ac > 0:
            boxed(c, 200, 570, 680, 200, AMBER, ac, 0.08)
            text(c, "5 pessoas, mas só 2 dias:", 540, 630, 30, "black", AMBER, ac)
            text(c, "a equipe MAIOR ficou com MENOS", 540, 680, 30, "black", AMBER, ac)
            text(c, "que a segunda", 540, 730, 30, "black", AMBER, ac)


ALTS3 = [("A", "R$ 9.000,00", "o 1º sócio", RED), ("B", "R$ 13.500,00", "", GREEN), ("C", "R$ 15.000,00", "partes iguais", RED),
         ("D", "R$ 18.000,00", "não sai de peso nenhum", RED), ("E", "R$ 22.500,00", "o 3º sócio", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · REGRA DE SOCIEDADE", "NÓS FAZEMOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    if t < C["30"]:
        _enunciado(c, [("Três sócios investiram, respectivamente, R$ 30.000,00, R$ 45.000,00 e R$ 75.000,00 na abertura de "
                        "uma empresa. Ao fim do primeiro ano, o lucro de R$ 45.000,00 foi dividido proporcionalmente ao "
                        "capital investido.", INK), ("O segundo sócio recebeu", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ACDE"}
    if t >= C["29.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS3, 1000, 230, 680, 40, C["30.ok"], "B", cues_in, cues_x, gap=26)
    if t >= C["30"]:
        ra = ep(t, C["30"], 0.4)
        _resolucao(c, ra, 220, 590)
        ftext(c, "30 000 : 45 000 : 75 000", 540, 300, 34, "black", INK, ra)
        ftext(c, "= 2 : 3 : 5", 540, 370, 44, "black", GREEN, ra)
        ftext(c, "soma 10 → k = 4 500", 540, 450, 38, "black", PURPLE, ep(t, C["30.b"], 0.4))
        ftext(c, "2º sócio: 3 × 4 500 = 13 500", 540, 530, 36, "black", GREEN, ep(t, C["30.c"], 0.4))
        ad = ep(t, C["30.d"], 0.4)
        if ad > 0:
            ftext(c, "9 000 + 13 500 + 22 500", 540, 630, 32, "black", INK2, ad)
            caixa(c, 330, 670, "= 45 000", True, ad)


ALTS5 = [("A", "R$ 6.000,00", "o sócio C", RED), ("B", "R$ 11.000,00", "partes iguais", RED), ("C", "R$ 12.000,00", "o sócio A", RED),
         ("D", "R$ 15.000,00", "", GREEN), ("E", "R$ 16.500,00", "a metade: sem conta", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · CAPITAL E TEMPO", "VOCÊ FAZ", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["32.a"], 0.4)
    if t < C["33"]:
        _enunciado(c, [("Em uma sociedade, o sócio A entrou com R$ 20.000,00 e permaneceu 12 meses; o sócio B, com R$ 30.000,00 "
                        "por 10 meses; e o sócio C, com R$ 15.000,00 por 8 meses. O lucro de R$ 33.000,00 foi dividido "
                        "proporcionalmente ao capital e ao tempo de permanência.", INK), ("O sócio B recebeu", BLUE)],
                   a0, 240, 28, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"32.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"34.x{L.lower()}"] for L in "ABCE"}
    if t >= C["32.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS5, 1000, 230, 680, 40, C["33.ok"], "D", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["32.end"] - 1.9, 540, 740)
    if t >= C["33"]:
        ra = ep(t, C["33"], 0.4)
        _resolucao(c, ra, 220, 590)
        ftext(c, "peso = capital × tempo", 540, 290, 32, "black", PURPLE, ra)
        ftext(c, "240 000 · 300 000 · 120 000", 540, 360, 34, "black", INK, ep(t, C["33.a"], 0.4))
        ftext(c, "÷ 60 000 → 4 : 5 : 2", 540, 430, 38, "black", GREEN, ep(t, C["33.b"], 0.4))
        ftext(c, "soma 11 → k = 3 000", 540, 500, 38, "black", PURPLE, ep(t, C["33.c"], 0.4))
        ftext(c, "B: 5 × 3 000 = 15 000", 540, 575, 40, "black", GREEN, ep(t, C["33.d"], 0.4))
        ae = ep(t, C["33.e"], 0.4)
        if ae > 0:
            ftext(c, "12 000 + 15 000 + 6 000", 540, 655, 32, "black", INK2, ae)
            caixa(c, 330, 690, "= 33 000", True, ae)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUANDO NÃO É PROPORCIONAL", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    if aa > 0:
        rrect(c, 700, 250, 520, 150, 20, DINHEIRO, aa, shadow=True)
        ftext(c, "R$ 10 000", 960, 345, 60, "black", "#FFFFFF", aa)
    ab = ep(t, C["36.b"], 0.5)
    if ab > 0:
        for j in range(3):
            aj = ab * ep(t, C["36.b"] + 0.2 * j, 0.4)
            rrect(c, 520 + j * 320, 470, 240, 110, 16, "#FFFFFF", aj, shadow=True)
            ftext(c, "R$ 1 000", 640 + j * 320, 538, 36, "black", DINHEIRO, aj)
            pill(c, "FIXO", 640 + j * 320, 470, AMBER, size=20, a=aj, anchor="center")
        text(c, "a proporção NÃO vale sobre o total", W / 2, 670, 38, "black", AMBER, ab)
    pill(c, "ep. 4 · parte fixa e conferências", W / 2, 780, PURPLE, size=32, a=ep(t, C["36.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"], "Você também tinha o instinto de somar?",
        canal="no Estudativo", anki=C["37.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, historia=b_historia, regra=b_regra, eufaco=b_eufaco,
              porque=b_porque, simplificar=b_simplificar, sociedade=b_sociedade, tempos=b_tempos, capital=b_capital,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q3=b_q3, q5=b_q5, ponte=b_ponte, cta=b_cta)
