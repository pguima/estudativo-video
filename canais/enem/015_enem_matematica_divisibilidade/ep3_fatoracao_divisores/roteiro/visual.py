"""Visual — Matemática ENEM, Divisibilidade, Episódio 3: Fatoração em primos e a fórmula dos divisores (tema claro).
Reaproveita o texto matemático do 010 ep1 (F.ftext: expoente com ^, ex.: "2^3 · 3^2 · 5") e as peças de layout do
014 ep1 (V1: frame, head_seq, which, para, selo, pause_timer).
Peças próprias:
- varal(): divisões sucessivas escritas linha por linha (números à esquerda, primo à direita da barra). Reaproveitável
  para a decomposição simultânea do MMC (o lado esquerdo pode ser "12, 18, 30").
- tijolo(): primo como tijolo · caixinhas(): as escolhas de cada primo (0 … expoente) · tabela do lanche do 12.
Cores: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_ENEM = Path(__file__).resolve().parents[3]


def _load(nome, rel):
    s = importlib.util.spec_from_file_location(nome, _ENEM / rel)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


F = _load("v010_ep1", "010_enem_matematica_conjuntos/ep1_ordem_e_sinais/roteiro/visual.py")
V1 = _load("v014_ep1", "014_enem_redacao_leitura_proposta/ep1_o_que_a_prova_pede/roteiro/visual.py")
motor.set_theme("claro")
ftext, fmid, ftext_w = F.ftext, F.fmid, F.ftext_w
frame, head_seq, which, para, selo, pause_timer, boxed = V1.frame, V1.head_seq, V1.which, V1.para, V1.selo, V1.pause_timer, V1.boxed

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisibilidade_ep3_fatoracao_divisores.mp4"
CARD_R = (140, 150, 1640, 690)
BRICK = "#C0563B"


# ======================================================================
# peças
# ======================================================================

def tijolo(c, cx, cy, n, a, w=110, h=70, col=BRICK):
    """um primo desenhado como tijolo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 8, col, a, shadow=True)
    line(c, cx - w / 2 + 8, cy, cx + w / 2 - 8, cy, mix(col, "#000000", 0.18), a * 0.5, 2)
    text_mid(c, str(n), cx, cy, h * 0.55, "black", "#FFFFFF", a)


def varal(c, x, y, linhas, alphas, size=46, lh=70, wleft=230, col_p=PURPLE, hl=None, a=1.0):
    """linhas = [(esquerda, primo|None), ...]; alphas = [(alfa_esquerda, alfa_primo), ...]; hl = {i: cor} realça primos.
    A barra vertical cresce junto com as linhas. Retorna a altura usada."""
    if a <= 0:
        return 0
    bx = x + wleft
    vis = [i for i, (al, _) in enumerate(alphas) if al > 0]
    if vis:
        last = max(vis)
        line(c, bx, y - size * 0.95, bx, y + last * lh + size * 0.35, INK2, a, 4)
    for i, ((esq, p), (al, ap)) in enumerate(zip(linhas, alphas)):
        yy = y + i * lh
        ftext(c, str(esq), bx - 26, yy, size, "black", INK, a * al, align="right")
        if p is not None and ap > 0:
            col = (hl or {}).get(i, col_p)
            ftext(c, str(p), bx + 26, yy, size, "black", col, a * ap, align="left")
    return len(linhas) * lh


def chip(c, s, cx, cy, col, a, size=34, w=None, fill=0.12):
    if a <= 0:
        return
    w = w or ftext_w(s, "black", size) + 40
    h = size * 1.55
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, mix("#FFFFFF", col, fill), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14), paint(col, a, stroke=3))
    fmid(c, s, cx, cy, size, "black", col, a)


def caixinha(c, x, y, base, n_exp, a, alphas=None, col=BLUE, size=30, gap=92, label=True):
    """caixa de escolhas de um primo: base^0 … base^n_exp; retorna a largura"""
    if a <= 0:
        return 0
    k = n_exp + 1
    w = k * gap + 30
    rrect(c, x, y, w, 120, 18, "#FFFFFF", a, shadow=True)
    if label:
        text(c, f"o {base} entra", x + w / 2, y - 16, 22, "bold", GRAY, a)
    for j in range(k):
        aj = a * (alphas[j] if alphas else 1)
        chip(c, f"{base}^{j}", x + 15 + gap / 2 + j * gap, y + 60, col, aj, size, w=gap - 14)
    return w


def frase_fat(c, s, cx, cy, size, col, a):
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FATORAÇÃO E DIVISORES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "360", 560, 470, 220, "black", INK, aa)
    text(c, "tem", 560, 560, 40, "bold", GRAY, aa)
    chip(c, "24 divisores", 560, 650, GREEN, ep(t, C["01.a"] + 1.4, 0.4), 50)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        r = 110
        c.drawCircle(1300, 400, r + 12, paint(AMBER, ab * 0.16))
        c.drawCircle(1300, 400, r, paint("#FFFFFF", ab))
        c.drawArc(skia.Rect.MakeLTRB(1300 - r, 400 - r, 1300 + r, 400 + r), -90, 360 * (1 - prog(t, C["01.b"], 4)), False,
                  paint(AMBER, ab, stroke=18, cap_round=True))
        text_mid(c, "15 s", 1300, 400, 54, "black", INK, ab)
    ac = ep(t, C["01.c"], 0.5)
    divs = "1, 2, 3, 4, 5, 6, 8, 9, 10, 12, …"
    text(c, divs, 1300, 640, 30, "bold", LIGHT, ac)
    strike(c, 1080, 630, 1520, 630, ac, RED)
    text(c, "sem listar nenhum", 1300, 700, 32, "black", RED, ac)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "FATORAR qualquer número em primos"), ("02.b", "CONTAR os divisores com uma fórmula")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 180 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 56, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    head_seq(c, t, C, [("03", "LEMBRANDO O EPISÓDIO 2", "PRIMOS SÃO TIJOLOS", BLUE), ("04", "LEMBRANDO", "POTÊNCIA", BLUE)])
    card(c, *CARD_R)
    if t < C["04"] - 0.05:
        aa = ep(t, C["03.a"], 0.5)
        boxed(c, 300, 220, 1320, 120, BLUE, aa, 0.07)
        text_mid(c, "PRIMO = exatamente 2 divisores: o 1 e ele mesmo", W / 2, 280, 40, "black", BLUE, aa)
        for k, n in enumerate((2, 3, 5, 7, 11)):
            tijolo(c, 560 + k * 200, 480, n, ep(t, C["03.b"] + 0.35 * k, 0.4), 150, 90)
        text(c, "os TIJOLOS do episódio 2", W / 2, 640, 36, "black", BRICK, ep(t, C["03.c"], 0.4))
        return
    aa = ep(t, C["04.a"], 0.5)
    ftext(c, "2^3 = 2 · 2 · 2 = 8", 640, 360, 80, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        arrow(c, 530, 230, 465, 290, PURPLE, ab, 4, 14)
        text(c, "EXPOENTE", 600, 220, 26, "black", PURPLE, ab, align="left", tracking=2)
        text(c, "quantas vezes o número aparece", 600, 254, 22, "bold", INK2, ab, align="left")
    ac = ep(t, C["04.c"], 0.5)
    boxed(c, 1180, 430, 440, 200, GREEN, ac, 0.08)
    fmid(c, "2^0 = 1", 1400, 500, 70, "black", GREEN, ac)
    text(c, "qualquer número elevado a 0 dá 1", 1400, 590, 22, "bold", INK2, ac)


# ======================================================================
# bloco A — a receita e o teorema
# ======================================================================

def receita_card(c, x, y, a, titulo, itens, alphas):
    rrect(c, x, y, 520, 470, 20, "#FFFDF4", a, shadow=True)
    text(c, titulo, x + 260, y + 64, 30, "black", INK, a, tracking=2)
    line(c, x + 40, y + 92, x + 480, y + 92, LIGHT, a, 3)
    for k, (s, q) in enumerate(itens):
        ak = a * alphas[k]
        yy = y + 160 + k * 80
        c.drawCircle(x + 60, yy - 10, 8, paint(BRICK, ak))
        text(c, s, x + 90, yy, 34, "black", INK, ak, align="left")
        if q:
            text(c, q, x + 480, yy, 34, "black", GREEN, ak * alphas[-1], align="right")


def b_receita(c, t, C, B):
    head_seq(c, t, C, [("05", "O QUE UMA RECEITA", "TE DIZ?", BLUE), ("06", "O NÚMERO TAMBÉM TEM", "FATORAR", BLUE),
                       ("07", "SÓ COM TIJOLOS PRIMOS", "A RECEITA DO 12", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06", "07"])
    if sid == "05":
        al = [ep(t, C["05.a"] + 0.4 * k, 0.4) for k in range(3)] + [ep(t, C["05.b"], 0.4)]
        receita_card(c, 300, 200, ep(t, C["05.t"], 0.5), "BOLO", [("farinha", "2 xícaras"), ("ovos", "3"), ("açúcar", "1 xícara")], al)
        ac = ep(t, C["05.c"], 0.5)
        text(c, "quais ingredientes", 1240, 380, 44, "black", INK, ep(t, C["05.a"], 0.4))
        text(c, "e QUANTO de cada", 1240, 450, 44, "black", GREEN, ep(t, C["05.b"], 0.4))
        pill(c, "você sabe do que ele é feito", 1240, 590, BLUE, size=30, a=ac, anchor="center", bounds=(0, 1920))
        return
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        boxed(c, 300, 220, 1320, 120, BLUE, aa, 0.07)
        text_mid(c, "FATORAR = escrever o número como uma multiplicação", W / 2, 280, 40, "black", BLUE, aa)
        ab = ep(t, C["06.b"], 0.5)
        fmid(c, "12 = 2 × 6", W / 2, 470, 110, "black", INK, ab)
        acc = ep(t, C["06.c"], 0.5)
        for xx in (1010, 1190):
            arrow(c, xx, 600, xx, 545, PURPLE, acc, 4, 14)
        text(c, "FATORES", 1100, 650, 34, "black", PURPLE, acc, tracking=2)
        return
    a0 = ep(t, C["07.t"], 0.4)
    fmid(c, "6 = 2 × 3", 560, 260, 60, "black", INK2, a0)
    aa = ep(t, C["07.a"], 0.5)
    boxed(c, 900, 210, 720, 110, BLUE, aa, 0.07)
    text_mid(c, "FATORAÇÃO EM PRIMOS: só fatores primos", 1260, 265, 32, "black", BLUE, aa)
    ab = ep(t, C["07.b"], 0.5)
    fmid(c, "12 = 2 · 2 · 3", 560, 440, 90, "black", INK, ab)
    for k, n in enumerate((2, 2, 3)):
        tijolo(c, 400 + k * 160, 600, n, ep(t, C["07.b"] + 0.3 * k, 0.4))
    acc = ep(t, C["07.c"], 0.5)
    receita_card(c, 1100, 360, acc, "RECEITA DO 12", [("tijolo 2", "× 2"), ("tijolo 3", "× 1")], [1, 1, 1])


def b_teorema(c, t, C, B):
    frame(c, t, B["start"], "DUAS RECEITAS PARA O MESMO NÚMERO?", "NÃO: A RECEITA É ÚNICA", PURPLE)
    aa = ep(t, C["08.a"], 0.5)
    text(c, "TEOREMA FUNDAMENTAL DA ARITMÉTICA", W / 2, 250, 40, "black", PURPLE, aa, tracking=1)
    ab = ep(t, C["08.b"], 0.5)
    boxed(c, 260, 300, 1400, 150, PURPLE, ab, 0.07)
    text(c, "todo número maior que 1 é uma multiplicação de primos", W / 2, 365, 38, "black", INK, ab)
    text(c, "de UMA ÚNICA maneira", W / 2, 420, 38, "black", PURPLE, ab)
    acc = ep(t, C["08.c"], 0.5)
    fmid(c, "2 · 2 · 3  =  3 · 2 · 2", W / 2, 540, 60, "black", INK2, acc)
    text(c, "só a ordem muda", W / 2, 610, 28, "bold", GRAY, acc)
    selo(c, W / 2, 720, ep(t, C["08.d"], 0.4), "RECEITA ÚNICA", GREEN, -4, 40)


# ======================================================================
# bloco B — o varal do 360
# ======================================================================

L360 = [(360, 2), (180, 2), (90, 2), (45, 3), (15, 3), (5, 5), (1, None)]


def _alphas360(t, C):
    def e(x):
        return ep(t, x, 0.35)
    return [(e(C["09.b"]), e(C["10.a"])), (e(C["10.a"] + 1.4), e(C["10.b"])), (e(C["10.b"] + 1.4), e(C["10.c"])),
            (e(C["10.c"] + 1.4), e(C["11.a"])), (e(C["11.a"] + 1.4), e(C["11.b"])), (e(C["11.b"] + 0.9), e(C["11.c"] + 1.4)),
            (e(C["11.c"] + 2.4), 0)]


def b_varal(c, t, C, B):
    sid = which(t, C, ["09", "10", "11", "12"])
    head_seq(c, t, C, [("09", "EU FAÇO", "A RECEITA DO 360", GREEN), ("12", "LENDO A COLUNA", "DA DIREITA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    boxed(c, 980, 200, 620, 140, PURPLE, aa, 0.07)
    text(c, "REGRA", 1010, 236, 18, "black", PURPLE, aa, align="left", tracking=2)
    text(c, "divida pelo MENOR primo possível", 1290, 285, 32, "black", INK, aa)
    text(c, "até chegar a 1", 1290, 325, 30, "black", PURPLE, aa)
    hl = {}
    if sid == "12":
        hl = {0: BLUE, 1: BLUE, 2: BLUE, 3: GREEN, 4: GREEN, 5: AMBER}
    varal(c, 260, 250, L360, _alphas360(t, C), size=50, lh=74, wleft=240, hl=hl)
    if sid in ("10", "11"):
        notas = [("10.d", "45 é ímpar: o 2 não divide mais → 3"), ("11.a", "4 + 5 = 9 → o 3 divide"),
                 ("11.c", "5 não divide por 3 → 5")]
        y = 440
        for cue, s in notas:
            a = ep(t, C[cue], 0.4) * (1 - ep(t, C["12"], 0.3))
            if a > 0:
                pill(c, s, 1000, y, AMBER if "não" in s else GREEN, size=24, a=a, bounds=(0, 1920))
                y += 80
        selo(c, 1290, 700, ep(t, C["11.d"], 0.4), "CHEGOU A 1: ACABOU", GREEN, -4, 30)
    if sid == "12":
        grupos = [("12.a", "2^3", BLUE, "três vezes o 2"), ("12.b", "3^2", GREEN, "duas vezes o 3"), ("12.c", "5", AMBER, "um 5")]
        for k, (cue, s, col, sub) in enumerate(grupos):
            a = ep(t, C[cue], 0.4)
            chip(c, s, 1050 + k * 190, 460, col, a, 52, w=150)
            text(c, sub, 1050 + k * 190, 530, 18, "bold", GRAY, a)
        ad = ep(t, C["12.d"], 0.5)
        boxed(c, 900, 580, 720, 110, PURPLE, ad, 0.10)
        fmid(c, "360 = 2^3 · 3^2 · 5", 1260, 635, 54, "black", PURPLE, ad)
        fmid(c, "8 · 9 · 5 = 360 ✓", 1260, 750, 36, "black", GREEN, ep(t, C["12.e"], 0.4))


# ======================================================================
# nós fazemos — 72 e 120
# ======================================================================

L72 = [(72, 2), (36, 2), (18, 2), (9, 3), (3, 3), (1, None)]
L120 = [(120, 2), (60, 2), (30, 2), (15, 3), (5, 5), (1, None)]


def b_nos(c, t, C, B):
    head_seq(c, t, C, [("13", "SUA VEZ", "FATORE 72 E 120", GREEN), ("14", "CONFERINDO", "72 E 120", GREEN)])
    card(c, *CARD_R)
    a1 = ep(t, C["13.a"], 0.4)
    a2 = ep(t, C["13.b"], 0.4)
    if t < C["14"] - 0.05:
        fmid(c, "72 = ?", 560, 420, 110, "black", INK, a1)
        fmid(c, "120 = ?", 1300, 420, 110, "black", INK, a2)
        pill(c, "menor primo · até chegar a 1", W / 2, 620, PURPLE, size=30, a=ep(t, C["13.c"], 0.4), anchor="center")
        pause_timer(c, t, C["13.end"] - 1.9, W / 2, 760)
        return
    ra = ep(t, C["14.a"], 0.3)
    al72 = [(ep(t, C["14.a"] + 0.9 * i, 0.3), ep(t, C["14.a"] + 0.9 * i + 0.4, 0.3)) for i in range(6)]
    al120 = [(ep(t, C["14.c"] + 0.8 * i, 0.3), ep(t, C["14.c"] + 0.8 * i + 0.4, 0.3)) for i in range(6)]
    varal(c, 230, 240, L72, al72, size=42, lh=62, wleft=180)
    varal(c, 980, 240, L120, al120, size=42, lh=62, wleft=200)
    chip(c, "72 = 2^3 · 3^2", 640, 690, BLUE, ep(t, C["14.b"], 0.4), 40)
    chip(c, "120 = 2^3 · 3 · 5", 1440, 690, BLUE, ep(t, C["14.d"], 0.4), 40)


def b_importa(c, t, C, B):
    frame(c, t, B["start"], "PARA QUE SERVE", "A RECEITA?", PURPLE)
    a0 = ep(t, C["15.a"], 0.5)
    boxed(c, 660, 230, 600, 130, PURPLE, a0, 0.10)
    fmid(c, "FATORAÇÃO", W / 2, 295, 56, "black", PURPLE, a0)
    alvos = [("15.b", "MMC", "episódio 4", 460), ("15.c", "MDC", "episódio 5", 960), ("15.d", "Nº DE DIVISORES", "hoje", 1460)]
    for cue, s, sub, x in alvos:
        a = ep(t, C[cue], 0.4)
        arrow(c, W / 2, 370, x, 520, PURPLE, a, 5, 16, progress=a)
        chip(c, s, x, 580, GREEN if sub == "hoje" else BLUE, a, 40)
        text(c, sub, x, 660, 24, "bold", GRAY, a)


# ======================================================================
# bloco E/F — o lanche e a fórmula
# ======================================================================

def pao(c, cx, cy, a, col):
    rrect(c, cx - 50, cy - 26, 100, 52, 24, col, a, shadow=True)


def b_lanche(c, t, C, B):
    sid = which(t, C, ["16", "17", "18"])
    head_seq(c, t, C, [("16", "NA LANCHONETE", "QUANTOS LANCHES?", GREEN), ("17", "DIVISORES DO 12", "COMO UM LANCHE", GREEN),
                       ("18", "MONTANDO", "OS 6 DIVISORES", GREEN)])
    card(c, *CARD_R)
    if sid == "16":
        paes = ["#D9A35E", "#8B5A2B"]
        rech = [RED, GREEN, AMBER]
        aa, ab = ep(t, C["16.a"], 0.4), ep(t, C["16.b"], 0.4)
        text(c, "PÃO", 330, 230, 24, "black", GRAY, aa, tracking=2)
        for k, col in enumerate(paes):
            pao(c, 330, 300 + k * 110, aa, col)
        text(c, "RECHEIO", 560, 230, 24, "black", GRAY, ab, tracking=2)
        for k, col in enumerate(rech):
            c.drawCircle(560, 300 + k * 90, 30, paint(col, ab))
        ad = ep(t, C["16.d"], 0.4)
        for i in range(2):
            for j in range(3):
                a = ad * ep(t, C["16.d"] + 0.25 * (i * 3 + j), 0.3)
                x, y = 860 + j * 220, 300 + i * 170
                pao(c, x, y, a, paes[i])
                c.drawCircle(x, y, 20, paint(rech[j], a))
        fmid(c, "2 × 3 = 6 lanches", 1080, 690, 48, "black", GREEN, ep(t, C["16.d"] + 1.6, 0.4))
        pill(c, "escolhas independentes: MULTIPLICA", 1080, 790, PURPLE, size=28, a=ep(t, C["16.e"], 0.4), anchor="center", bounds=(0, 1920))
        return
    aa = ep(t, C["17.a"], 0.4)
    fmid(c, "12 = 2^2 · 3", W / 2, 230, 56, "black", INK, aa)
    if sid == "17":
        text(c, "todo divisor do 12 é feito só com esses tijolos", W / 2, 320, 30, "bold", INK2, ep(t, C["17.b"], 0.4))
        acc = ep(t, C["17.c"], 0.4)
        w = caixinha(c, 330, 420, 2, 2, acc, [ep(t, C["17.c"] + 0.4 * j, 0.3) for j in range(3)])
        text(c, "3 escolhas", 330 + w / 2, 590, 30, "black", BLUE, acc)
        ad = ep(t, C["17.d"], 0.4)
        w2 = caixinha(c, 1000, 420, 3, 1, ad, [ep(t, C["17.d"] + 0.4 * j, 0.3) for j in range(2)], col=GREEN)
        text(c, "2 escolhas", 1000 + w2 / 2, 590, 30, "black", GREEN, ad)
        fmid(c, "3 × 2 = 6 divisores", W / 2, 720, 50, "black", PURPLE, ep(t, C["17.e"], 0.4))
        return
    # 18: tabela do lanche
    cols = ["2^0", "2^1", "2^2"]
    rows = ["3^0", "3^1"]
    x0, y0, cw, rh = 560, 330, 230, 120
    for j, s in enumerate(cols):
        chip(c, s, x0 + cw / 2 + j * cw, y0 - 40, BLUE, 1.0, 30, w=110)
    for i, s in enumerate(rows):
        chip(c, s, x0 - 80, y0 + rh / 2 + i * rh + 20, GREEN, 1.0, 30, w=110)
    cues = [("18.a", 0, 0, "1"), ("18.b", 0, 1, "2"), ("18.c", 0, 2, "4"), ("18.d", 1, 0, "3"), ("18.e", 1, 1, "6"), ("18.f", 1, 2, "12")]
    for cue, i, j, v in cues:
        a = ep(t, C[cue], 0.35)
        x, y = x0 + j * cw, y0 + i * rh + 20
        rrect(c, x + 10, y, cw - 20, rh - 16, 14, "#FFFFFF", 1.0, stroke=2, stroke_color=LINE)
        text_mid(c, v, x + cw / 2, y + (rh - 16) / 2, 48, "black", INK, a)
    ag = ep(t, C["18.g"], 0.4)
    fmid(c, "D(12) = {1, 2, 3, 4, 6, 12}", W / 2, 640, 44, "black", GREEN, ag)
    text(c, "a mesma lista do episódio 1 ✓", W / 2, 710, 28, "bold", INK2, ag)


def b_mais1(c, t, C, B):
    frame(c, t, B["start"], "REPARE NO ZERO", "POR QUE O +1?", PURPLE)
    aa = ep(t, C["19.a"], 0.5)
    chip(c, "2^0 · 3^0 = 1", 560, 330, BLUE, aa, 56)
    text(c, "o lanche sem nenhum tijolo", 560, 430, 30, "bold", INK2, aa)
    fmid(c, "2^0 = 1", 560, 560, 70, "black", GREEN, ep(t, C["19.b"], 0.4))
    ac = ep(t, C["19.c"], 0.5)
    boxed(c, 1000, 260, 620, 200, PURPLE, ac, 0.08)
    text(c, "escolhas =", 1310, 340, 40, "black", INK, ac)
    text(c, "expoente + 1", 1310, 410, 52, "black", PURPLE, ac)
    ad = ep(t, C["19.d"], 0.5)
    caixinha(c, 1110, 560, 2, 2, ad, label=False)
    text(c, "expoente 2 → 3 escolhas", 1310, 720, 28, "black", BLUE, ad)


def b_formula(c, t, C, B):
    sid = which(t, C, ["20", "21"])
    head_seq(c, t, C, [("20", "A FÓRMULA", "QUANTOS DIVISORES?", PURPLE), ("21", "O 360", "EM QUINZE SEGUNDOS", PURPLE)])
    card(c, *CARD_R)
    if sid == "20":
        passos = [("20.a", "1", "fatore o número"), ("20.b", "2", "some 1 a cada expoente"), ("20.c", "3", "multiplique os resultados")]
        for k, (cue, n, s) in enumerate(passos):
            a, d = rise(t, C[cue])
            badge_num(c, n, 420, 300 + k * 140 + d - 14, a, 38, bg=PURPLE)
            text(c, s, 490, 300 + k * 140 + d, 56, "black", INK, a, align="left")
        return
    fmid(c, "360 = 2^3 · 3^2 · 5^1", W / 2, 230, 54, "black", INK, ep(t, C["21.t"], 0.4))
    specs = [("21.a", 2, 3, BLUE, "4"), ("21.b", 3, 2, GREEN, "3"), ("21.c", 5, 1, AMBER, "2")]
    x = 230
    for cue, base, e, col, n in specs:
        a = ep(t, C[cue], 0.4)
        w = caixinha(c, x, 360, base, e, a, [ep(t, C[cue] + 0.35 * j, 0.3) for j in range(e + 1)], col=col, size=26, gap=84)
        text(c, f"{n} escolhas", x + w / 2, 530, 30, "black", col, a)
        x += w + 60
    ad = ep(t, C["21.d"], 0.5)
    boxed(c, 460, 590, 1000, 110, PURPLE, ad, 0.10)
    fmid(c, "(3+1)(2+1)(1+1) = 4 · 3 · 2 = 24", W / 2, 645, 50, "black", PURPLE, ad)
    pill(c, "sem listar nenhum", W / 2, 780, GREEN, size=28, a=ep(t, C["21.e"], 0.4), anchor="center")


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Fatorar é achar a receita de primos do número.", "Divida sempre pelo menor primo possível.",
          "Divisores: some 1 em cada expoente e multiplique."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["22", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "22" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 48, "black", INK, a, align="left")


ERROS = [("23", "Multiplicar os expoentes sem somar 1", "3 · 2 · 1 = 6", "os expoentes contam os primos",
          "(3+1)(2+1)(1+1) = 24", "esqueceu a escolha do ZERO"),
         ("24", "Esquecer o expoente 1 de quem aparece sozinho", "(3+1)(2+1) = 12", "o expoente 1 nem vem escrito",
          "5 = 5^1 → (1+1)", "o 5 também ganha o seu +1"),
         ("25", "Parar a fatoração antes de chegar a 1", "360 = 2^3 · 45", "o número já ficou pequeno",
          "45 = 3^2 · 5", "só pare no 1")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, conta_err, parece, conta_ok, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 320, 34, aa, RED, "x")
    text(c, err, 360, 335, 42, "black", RED, aa, align="left")
    ftext(c, conta_err, 360, 420, 46, "black", RED, aa, align="left")
    strike(c, 356, 405, 370 + ftext_w(conta_err, "black", 46), 405, ep(t, cue("c"), 0.4), RED)
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 510, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 585, 36, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 690, 34, ac, GREEN)
    ftext(c, conta_ok, 360, 708, 46, "black", GREEN, ac, align="left")
    text(c, fix, 1620, 708, 30, "black", GREEN, ac, align="right")


# ======================================================================
# questão 4
# ======================================================================

ALT = [("A", "12"), ("B", "18"), ("C", "20"), ("D", "24"), ("E", "36")]


def b_q4(c, t, C, B):
    sid = which(t, C, ["26", "27", "28"])
    head(c, t, B["start"], "QUESTÃO 4", "CONTAGEM DE DIVISORES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["26.a"], 0.5)
    text(c, "QUESTÃO", 200, 230, 20, "black", BLUE, aa, align="left", tracking=2)
    para(c, "Quantos divisores positivos tem o número 360?", 200, 290, 40, "black", INK, aa, 620, 50)
    aok = ep(t, C["27.ok"], 0.4)
    for k, (L, v) in enumerate(ALT):
        a, d = rise(t, C[f"26.{'bcdef'[k]}"])
        y = 450 + k * 72 + d
        ok = L == "D"
        if ok and aok > 0:
            rrect(c, 190, y - 34, 420, 64, 14, GREEN, 0.15 * aok)
        badge_num(c, L, 230, y - 2, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
        text(c, v, 280, y + 12, 38, "black", INK, a, align="left")
        why = {"A": ("28.xa", "esqueceu o +1 do 5: 4 · 3"), "B": ("28.xb", "2² no lugar de 2³: 3 · 3 · 2")}.get(L)
        if why:
            ax = ep(t, C[why[0]], 0.4)
            pill(c, why[1], 380, y, RED, size=20, a=ax, bounds=(0, 1920))
    pause_timer(c, t, C["26.end"] - 1.9, 1260, 520)
    if sid in ("27", "28"):
        x0 = 980
        rrect(c, x0 - 40, 220, 700, 560, 20, mix("#FFFFFF", GREEN, 0.05), ep(t, C["27"], 0.4))
        text(c, "RESOLUÇÃO", x0, 270, 20, "black", GREEN, ep(t, C["27"], 0.4), align="left", tracking=2)
        ftext(c, "360 = 2^3 · 3^2 · 5^1", x0, 360, 44, "black", INK, ep(t, C["27.a"], 0.4), align="left")
        ftext(c, "(3+1)(2+1)(1+1)", x0, 450, 44, "black", PURPLE, ep(t, C["27.b"], 0.4), align="left")
        ftext(c, "= 4 · 3 · 2 = 24", x0, 530, 44, "black", GREEN, ep(t, C["27.c"], 0.4), align="left")
        selo(c, x0 + 300, 640, aok, "LETRA D", GREEN, -4, 40)
        a6 = ep(t, C["28.x6"], 0.4)
        pill(c, "3 · 2 · 1 = 6: nem está nas opções", x0 + 310, 735, AMBER, size=22, a=a6, anchor="center", bounds=(0, 1920))
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, aa, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MMC", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    chip(c, "receita de primos na mão", W / 2, 260, BRICK, aa, 36)
    itens = [("ônibus", BLUE), ("lâmpadas", AMBER), ("remédios", GREEN)]
    for k, (s, col) in enumerate(itens):
        a = ep(t, C["30.b"] + 0.5 * k, 0.4)
        x = 560 + k * 400
        c.drawCircle(x, 450, 70, paint(mix("#FFFFFF", col, 0.18), a))
        c.drawArc(skia.Rect.MakeLTRB(x - 70, 380, x + 70, 520), -90, 300, False, paint(col, a, stroke=8, cap_round=True))
        text(c, s, x, 580, 34, "black", INK, a)
    text(c, "que voltam a coincidir", W / 2, 670, 36, "bold", INK2, ep(t, C["30.b"] + 1.5, 0.4))
    pill(c, "próximo episódio: MMC", W / 2, 770, PURPLE, size=32, a=ep(t, C["30.c"], 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Quantos divisores tem o 72?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, receita=b_receita, teorema=b_teorema, varal=b_varal,
              nos=b_nos, importa=b_importa, lanche=b_lanche, mais1=b_mais1, formula=b_formula, recap=b_recap,
              erros=b_erros, q4=b_q4, ponte=b_ponte, cta=b_cta)
