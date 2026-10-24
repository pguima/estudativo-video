"""Visual — Divisão Proporcional, Episódio 1: o valor de uma parte (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: pacote() (um pacotinho de dinheiro = o k), monte() (o total antes de ser quebrado),
fileiras() (cada dono com seus pacotinhos), caixa() (a balança de caixa: as partes somadas fecham com o total).
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
ARQUIVO_FINAL = "enem_matematica_divisao_ep1_valor_de_uma_parte.mp4"
CARD_R = K.CARD_R
NOTA = "#2E9E62"          # o dinheiro (pacotinhos)
NOTA_ESC = "#1F7A4A"
DONOS = ["#E8743B", "#2BA3B8", "#D9468F"]   # as três pessoas (cores neutras, sem função)


# ======================================================================
# peças do episódio
# ======================================================================

def pacote(c, x, y, w, h, col, a, label=None, lsize=28):
    """um pacotinho de dinheiro (canto superior esquerdo em x, y)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, col, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 7, y + 7, w - 14, h - 14), 9, 9),
                paint("#FFFFFF", a * 0.45, stroke=2))
    if label:
        text_mid(c, label, x + w / 2, y + h / 2, lsize, "black", "#FFFFFF", a)


def monte(c, cx, cy, a, rotulo, w=300, n=7):
    """o total, um monte de notas empilhadas, com o valor numa etiqueta"""
    if a <= 0:
        return
    for k in range(n):
        dx = (k % 2) * 14 - 7
        rrect(c, cx - w / 2 + dx, cy - k * 22, w, 70, 12, NOTA if k % 2 == 0 else NOTA_ESC, a, shadow=k == 0)
    pill(c, rotulo, cx, cy + 110, INK, size=40, a=a, anchor="center", bounds=(0, 1920))


def fileiras(c, t, pesos, x0, y0, a, prog=1.0, k_label=None, nomes=None, pw=104, ph=84, gap=14, dy=125, partes=None,
             partes_a=0.0, xr=None, hl=None):
    """cada dono numa fileira, com `peso` pacotinhos; prog (0–1) revela os pacotinhos um a um, na ordem das fileiras;
    partes = textos à direita (ex.: "2 × 400 = 800"), com alfa partes_a (número ou lista por fileira)"""
    total = sum(pesos)
    nvis = prog * total
    idx = 0
    for j, p in enumerate(pesos):
        y = y0 + j * dy
        dim = 1.0 if hl is None or hl == j else 0.35
        if nomes:
            text(c, nomes[j], x0 - 30, y + ph / 2 + 12, 32, "black", DONOS[j % 3], a * dim, align="right")
        for i in range(p):
            ai = a * clamp(nvis - idx, 0, 1) * dim
            pacote(c, x0 + i * (pw + gap), y, pw, ph, DONOS[j % 3], ai, k_label, 26)
            idx += 1
        if partes:
            pa = partes_a[j] if isinstance(partes_a, (list, tuple)) else partes_a
            xx = xr if xr is not None else x0 + max(pesos) * (pw + gap) + 30
            ftext(c, partes[j], xx, y + ph / 2 + 14, 40, "black", INK, pa * dim, align="left")


def caixa(c, x, y, partes, total, a, ok_a=0.0, w=420, size=36, titulo="FECHANDO O CAIXA", ok=True):
    """a balança de caixa: um cupom com as partes somadas e o total; ok_a mostra o selo FECHOU (verde) ou NÃO FECHOU"""
    if a <= 0:
        return
    lh = size * 1.45
    h = 110 + len(partes) * lh + 90
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    text(c, titulo, x + w / 2, y + 52, 24, "black", GRAY, a)
    line(c, x + 30, y + 72, x + w - 30, y + 72, "#E6E6E2", a, 3)
    yy = y + 72 + lh
    for k, s in enumerate(partes):
        ftext(c, ("+ " if k else "  ") + s, x + w - 40, yy, size, "black", INK, a, align="right")
        yy += lh
    line(c, x + 30, yy - lh + 22, x + w - 30, yy - lh + 22, INK, a, 4)
    ftext(c, "= " + total, x + w - 40, yy + 18, size + 4, "black", GREEN if ok else RED, a, align="right")
    if ok_a > 0:
        selo(c, x + w / 2 - 40, y + h + 26, ok_a, "FECHOU!" if ok else "NÃO FECHOU", GREEN if ok else RED, -5, 30)


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

CASOS = [("01.a", "LUCRO", "entre sócios"), ("01.b", "VERBA", "entre setores"), ("01.c", "HERANÇA", "entre herdeiros"),
         ("01.d", "BÔNUS", "entre funcionários")]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DIVISÃO PROPORCIONAL", BLUE)
    for k, (cue, s, sub) in enumerate(CASOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 395
        card(c, x, 220 + d, 360, 270, a)
        for j, p in enumerate((1, 2, 3)):
            pacote(c, x + 40 + j * 98, 250 + d + (3 - p) * 20, 80, 50 + p * 20, DONOS[j], a)
        text(c, s, x + 180, 430 + d, 40, "black", INK, a)
        text(c, sub, x + 180, 470 + d, 26, "bold", GRAY, a)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        boxed(c, 360, 560, 1200, 210, PURPLE, ae, 0.07)
        text(c, "O MESMO PROCEDIMENTO, EM UMA LINHA", W / 2, 620, 32, "black", PURPLE, ae)
        ftext(c, "k =", 760, 715, 64, "black", PURPLE, ae, align="right")
        fr(c, "total", "soma dos pesos", 1010, 700, 56, PURPLE, ae)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "repartir qualquer valor em partes proporcionais", "um único procedimento"),
            ("02.b", "responder EXATAMENTE a parte pedida", "a maior, a menor, a diferença, o total")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 340 + j * 200 + d
        check_icon(c, 280, y - 14, 34, a, GREEN)
        text(c, s, 340, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 340, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "SÉRIE DE RAZÃO", 420, 250, GRAY, size=22, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "O TRUQUE DO k", 420, 320, 36, "black", PURPLE, aa)
        for j in range(3):
            pacote(c, 250 + j * 80, 380, 66, 56, DONOS[0], aa, "k", 24)
        for j in range(5):
            pacote(c, 250 + j * 80, 470, 66, 56, DONOS[1], aa, "k", 24)
        text(c, "3 para 5 = 3 e 5 pacotinhos", 420, 600, 28, "bold", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "SÉRIE DE RAZÃO", 960, 250, GRAY, size=22, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "SOMA DOS DE CIMA", 960, 320, 32, "black", PURPLE, ab)
        expr(c, "a/b = c/d = a+c/b+d", 960, 460, 58, ab, cores={4: PURPLE})
        text(c, "a mesma razão", 960, 600, 28, "bold", INK2, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        pill(c, "SÉRIE DE DIVISIBILIDADE", 1500, 250, GRAY, size=22, a=acc, anchor="center", bounds=(0, 1920))
        text(c, "MDC", 1500, 320, 36, "black", PURPLE, acc)
        ftext(c, "MDC(12, 18) = 6", 1500, 470, 48, "black", INK, acc)
        text(c, "o maior que divide todos", 1500, 600, 28, "bold", INK2, acc)
    line(c, 690, 230, 690, 720, "#E6E6E2", aa, 3)
    line(c, 1230, 230, 1230, 720, "#E6E6E2", ab, 3)


# ======================================================================
# concreto e definição
# ======================================================================

SITU = [("04.a", "PRÊMIO", "conforme a pontuação", (2, 5, 3)), ("04.b", "HERANÇA", "conforme a idade", (3, 4, 5)),
        ("04.c", "A CONTA DOS AMIGOS", "conforme o consumo", (4, 1, 3))]


def b_concreto(c, t, C, B):
    frame(c, t, B["start"], "TRÊS SITUAÇÕES", "QUEM TEM MAIS, LEVA MAIS", BLUE)
    for k, (cue, s, sub, alt) in enumerate(SITU):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 510
        card(c, x, 240 + d, 460, 380, a)
        for j, hh in enumerate(alt):
            rrect(c, x + 90 + j * 105, 470 + d - hh * 36, 80, hh * 36, 10, DONOS[j], a)
        text(c, s, x + 230, 530 + d, 34, "black", INK, a)
        text(c, sub, x + 230, 575 + d, 26, "bold", GRAY, a)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "partes iguais aqui não é justo: quem tem mais, leva mais", W / 2, 760, ad, 34)


def b_definicao(c, t, C, B):
    frame(c, t, B["start"], "O NOME DISSO", "DIVISÃO PROPORCIONAL", BLUE)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 240, 230, 1440, 140, BLUE, aa, 0.08)
        text(c, "DIVISÃO PROPORCIONAL", W / 2, 285, 36, "black", BLUE, aa)
        text(c, "repartir um total de acordo com números que dizem quanto cada um merece", W / 2, 340, 30, "bold", INK, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        boxed(c, 240, 410, 1440, 110, BLUE, ab, 0.08)
        text_mid(c, "PESO = o número de cada um na divisão", W / 2, 465, 36, "black", BLUE, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        for j, p in enumerate((2, 3, 4)):
            x = 470 + j * 340
            rrect(c, x, 780 - p * 52, 150, p * 52, 12, DONOS[j], acc, shadow=True)
            text(c, f"peso {p}", x + 75, 815, 30, "black", DONOS[j], acc)
        selo(c, 1560, 640, ep(t, C["05.c"] + 1.2, 0.4), "peso 4 = 2 × peso 2", GREEN, -4, 28)


# ======================================================================
# bloco A — o procedimento (R$ 3.600 em 2, 3 e 4)
# ======================================================================

PESOS_A = [2, 3, 4]
NOMES_A = ["peso 2", "peso 3", "peso 4"]
PARTES_A = ["2 × 400 = 800", "3 × 400 = 1.200", "4 × 400 = 1.600"]


def b_passo(c, t, C, B):
    head_seq(c, t, C, [("06", "PASSO 1", "SOME OS PESOS", PURPLE), ("07", "PASSO 2", "DIVIDA: O k", PURPLE),
                       ("08", "PASSO 3", "MULTIPLIQUE CADA PESO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    a0 = ep(t, C["06.a"], 0.5)
    pv = ep(t, C["06.c"], 2.0)
    kl = "400" if t >= C["07.b"] else None
    pa = [ep(t, C[cue], 0.4) for cue in ("08.a", "08.b", "08.c")] if t >= C["08"] else 0.0
    fileiras(c, t, PESOS_A, 380, 250, a0, pv, kl, NOMES_A, partes=PARTES_A, partes_a=pa, xr=900)
    if sid in ("06", "07"):
        monte(c, 1440, 380, a0, "R$ 3.600")
        ab = ep(t, C["06.b"], 0.5)
        if sid == "06" and ab > 0:
            ftext(c, "2 + 3 + 4 = 9", 1440, 640, 56, "black", PURPLE, ab)
            text(c, "9 pacotinhos iguais", 1440, 710, 30, "bold", INK2, ep(t, C["06.c"], 0.5))
        if sid == "07":
            expr(c, "3.600/9 = 400", 1440, 620, 60, ep(t, C["07.a"], 0.5), cores={2: GREEN})
            ab2 = ep(t, C["07.b"], 0.5)
            if ab2 > 0:
                boxed(c, 1220, 710, 440, 90, PURPLE, ab2, 0.08)
                text_mid(c, "k = 400 = 1 pacotinho", 1440, 755, 32, "black", PURPLE, ab2)
        return
    ad = ep(t, C["08.d"], 0.5)
    caixa(c, 1300, 220, ["800", "1.200", "1.600"], "3.600", ad, ep(t, C["08.e"], 0.4))


def b_atalho(c, t, C, B):
    frame(c, t, B["start"], "O PROCEDIMENTO", "EM UMA LINHA", PURPLE)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        boxed(c, 460, 220, 1000, 200, PURPLE, aa, 0.07)
        ftext(c, "k =", 820, 340, 72, "black", PURPLE, aa, align="right")
        fr(c, "total", "soma dos pesos", 1090, 320, 60, PURPLE, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        steps = ["1. SOME os pesos", "2. DIVIDA o total pela soma (o k)", "3. MULTIPLIQUE o k por cada peso"]
        K.atalho(c, 260, 470, 900, 300, "ATALHO · SOME, DIVIDA, MULTIPLIQUE", steps, ab, 34)
    acc = ep(t, C["09.c"], 0.5)
    caixa(c, 1240, 420, ["800", "1.200", "1.600"], "3.600", acc, ep(t, C["09.c"] + 0.8, 0.4), w=400, size=30)


# ======================================================================
# bloco B — o k significa alguma coisa
# ======================================================================

def b_significa(c, t, C, B):
    frame(c, t, B["start"], "O k TEM SIGNIFICADO", "O VALOR DE UM PONTO DE PESO", BLUE)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        pacote(c, 330, 260, 300, 200, NOTA, aa, "k", 90)
        text(c, "1 ponto de peso", 480, 520, 34, "black", BLUE, aa)
    for j, (cue, s1, s2) in enumerate((("10.b", "pesos = DIAS trabalhados", "k = o valor de 1 dia"),
                                       ("10.c", "pesos = PONTOS no concurso", "k = o valor de 1 ponto"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + j * 180 + d
        card(c, 800, y, 860, 140, a)
        text(c, s1, 840, y + 58, 34, "black", INK, a, align="left")
        text(c, s2, 840, y + 108, 32, "black", GREEN, a, align="left")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        regra(c, "pergunte sempre: um pacotinho DE QUÊ?", W / 2, 750, ad, 36)


# ======================================================================
# bloco C — por que dividir pela soma funciona
# ======================================================================

def b_porque(c, t, C, B):
    frame(c, t, B["start"], "POR QUE FUNCIONA?", "A SOMA DOS DE CIMA", PURPLE)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        expr(c, "800/2 = 1.200/3 = 1.600/4 = 400", W / 2, 330, 68, aa, cores={6: GREEN})
        text(c, "cada parte ÷ o seu peso = o mesmo k", W / 2, 450, 30, "bold", INK2, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        boxed(c, 460, 510, 1000, 200, PURPLE, ab, 0.07)
        expr(c, "800+1.200+1.600/2+3+4 = 3.600/9 = 400", W / 2, 610, 54, ab, cores={2: PURPLE, 4: GREEN})
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        regra(c, "juntando tudo: total ÷ soma dos pesos também dá k", W / 2, 785, acc, 32)


# ======================================================================
# bloco D — proporções equivalentes e o MDC
# ======================================================================

EQUIV = [("12.a", (2, 3), "2 : 3"), ("12.a", (4, 6), "4 : 6"), ("12.a", (20, 30), "20 : 30")]


def b_equivalentes(c, t, C, B):
    frame(c, t, B["start"], "UMA SURPRESA", "PESOS EQUIVALENTES", BLUE)
    for j, (cue, (p, q), lab) in enumerate(EQUIV):
        a = ep(t, C[cue] + 0.8 * j, 0.5)
        if a <= 0:
            continue
        y = 250 + j * 150
        text(c, lab, 380, y + 64, 44, "black", INK, a, align="right")
        x0, wtot = 440, 1100
        n = p + q
        cw = wtot / n
        for i in range(n):
            col = DONOS[0] if i < p else DONOS[1]
            rrect(c, x0 + i * cw + 2, y, cw - 4, 90, 6 if n > 10 else 10, col, a)
        line(c, x0 + p * cw, y - 14, x0 + p * cw, y + 104, INK, ep(t, C["12.b"], 0.5) * a, 5)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        text(c, "pacotinhos de tamanhos diferentes, mas o corte cai no MESMO lugar: 40% e 60%", W / 2, 720, 30, "bold",
             INK2, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 790, acc, "AS PARTES FINAIS SÃO IDÊNTICAS", GREEN, -2, 32)


def b_mdc(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "SIMPLIFIQUE PELO MDC", GREEN)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        monte(c, 400, 330, aa, "R$ 5.000", w=240, n=5)
    ab = ep(t, C["13.b"], 0.5)
    for j, (g, s) in enumerate(((12, 2), (18, 3), (30, 5))):
        x = 820 + j * 240
        if aa > 0:
            chip(c, str(g), x, 270, INK2, aa, 48)
        if ab > 0:
            arrow(c, x, 320, x, 400, GREEN, ab, 5, 14, progress=ab)
            chip(c, str(s), x, 450, GREEN, ab, 52)
    if ab > 0:
        text(c, "÷ 6", 1580, 380, 40, "black", GREEN, ab)
        text(c, "MDC = 6", 1580, 430, 30, "bold", INK2, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        ftext(c, "soma 10  →  k = 5.000 ÷ 10 = 500", 1060, 590, 40, "black", PURPLE, acc)
        ftext(c, "1.000  ·  1.500  ·  2.500", 1060, 670, 44, "black", INK, acc)
    ad = ep(t, C["13.d"], 0.5)
    caixa(c, 220, 520, ["1.000", "1.500", "2.500"], "5.000", ad, ep(t, C["13.d"] + 0.8, 0.4), w=380, size=28)


# ======================================================================
# blocos E e F — a herança (direta) e a diferença
# ======================================================================

HERD = [(15, 45), (20, 60), (25, 75)]


def _barras_heranca(c, t, a, partes_a, hl=None, x0=520, y0=270, esc=11.0):
    for j, (idade, mil) in enumerate(HERD):
        y = y0 + j * 130
        dim = 1.0 if hl is None or j in hl else 0.3
        text(c, f"{idade} anos", x0 - 40, y + 58, 36, "black", DONOS[j], a * dim, align="right")
        w = mil * esc * partes_a
        if w > 1:
            rrect(c, x0, y, w, 86, 14, DONOS[j], a * dim, shadow=True)
        if partes_a > 0.95:
            ftext(c, f"R$ {mil}.000", x0 + mil * esc + 24, y + 58, 38, "black", INK, a * dim, align="left")


def b_heranca(c, t, C, B):
    frame(c, t, B["start"], "DIVISÃO DIRETA", "A HERANÇA POR IDADES", BLUE)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        pill(c, "R$ 180.000 por idades 15, 20 e 25", W / 2, 230, INK, size=32, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        ftext(c, "15 + 20 + 25 = 60   →   k = 180.000 ÷ 60 = 3.000", W / 2, 330, 40, "black", PURPLE, ab)
        text(c, "R$ 3.000 por ano de idade", W / 2, 385, 28, "bold", INK2, ab)
    _barras_heranca(c, t, ep(t, C["14.c"], 0.5), ep(t, C["14.c"], 1.2), y0=430, esc=10.0)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 470, ad, "maior peso → maior parte", GREEN, -3, 30)


def b_diferenca(c, t, C, B):
    frame(c, t, B["start"], "SÓ A DIFERENÇA?", "NÃO CALCULE AS DUAS", GREEN)
    a0 = ep(t, C["15"], 0.5)
    ab = ep(t, C["15.b"], 0.5)
    for j, (idade, n) in enumerate(((15, 15), (25, 25))):
        y = 260 + j * 150
        col = DONOS[0] if j == 0 else DONOS[2]
        text(c, f"{idade} anos", 330, y + 52, 34, "black", col, a0, align="right")
        for i in range(n):
            extra = j == 1 and i >= 15
            ai = a0 if not extra else a0 * (0.35 + 0.65 * ab)
            rrect(c, 360 + i * 46, y, 40, 76, 7, GREEN if (extra and ab > 0) else col, ai)
    if ab > 0:
        x1, x2 = 360 + 15 * 46, 360 + 25 * 46
        line(c, x1, 520, x2 - 6, 520, GREEN, ab, 5)
        text(c, "25 − 15 = 10 pacotinhos", (x1 + x2) / 2, 570, 32, "black", GREEN, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        ftext(c, "10 × 3.000 = 30.000", 640, 680, 52, "black", PURPLE, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        ftext(c, "75.000 − 45.000 = 30.000 ✓", 640, 770, 36, "black", INK2, ad)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1180, 620, 480, 190, "ATALHO", ["diferença das partes =", "diferença dos pesos × k"], ae, 30)


# ======================================================================
# bloco G — o total pela parte conhecida
# ======================================================================

def b_total(c, t, C, B):
    frame(c, t, B["start"], "E SEM O TOTAL?", "UMA PARTE DÁ O k", BLUE)
    aa = ep(t, C["16.a"], 0.5)
    ab = ep(t, C["16.b"], 0.5)
    kl = "300" if t >= C["16.b"] + 1.5 else None
    pa = [0.0, 0.0, aa] if t < C["16.c"] else [ep(t, C["16.c"], 0.5)] * 2 + [aa]
    partes = ["300", "600", "1.200"]
    fileiras(c, t, [1, 2, 4], 400, 260, aa, 1.0, kl, ["peso 1", "peso 2", "peso 4"], partes=partes, partes_a=pa, xr=920,
             hl=2 if t < C["16.c"] else None)
    if ab > 0:
        ftext(c, "4 pacotinhos = 1.200", 1400, 300, 40, "black", INK, ab)
        ftext(c, "k = 1.200 ÷ 4 = 300", 1400, 380, 44, "black", PURPLE, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        ftext(c, "total = 7 × 300 = 2.100", 1400, 480, 44, "black", GREEN, acc)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        ftext(c, "300 + 600 + 1.200 = 2.100 ✓", 640, 700, 40, "black", INK2, ad)
        selo(c, 640, 775, ep(t, C["16.d"] + 0.8, 0.4), "FECHOU!", GREEN, -4, 30)
    ae = ep(t, C["16.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1180, 580, 480, 170, "ATALHO", ["conhece uma parte?", "ela dá o k"], ae, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("18", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        monte(c, 430, 360, aa, "R$ 1.500", w=260, n=6)
        text(c, "pesos 1, 2 e 3", 430, 560, 40, "black", INK, aa)
    pause_timer(c, t, C["17.end"] - 1.9, 430, 680)
    if t >= C["18"]:
        ra = ep(t, C["18.a"], 0.5)
        ftext(c, "1 + 2 + 3 = 6", 1150, 280, 44, "black", PURPLE, ra)
        rb = ep(t, C["18.b"], 0.5)
        ftext(c, "k = 1.500 ÷ 6 = 250", 1150, 360, 44, "black", PURPLE, rb)
        rc = ep(t, C["18.c"], 0.5)
        fileiras(c, t, [1, 2, 3], 860, 420, rc, 1.0, "250", None, pw=92, ph=70, dy=95,
                 partes=["250", "500", "750"], partes_a=rc, xr=1240)
        rd = ep(t, C["18.d"], 0.5)
        if rd > 0:
            selo(c, 1150, 760, rd, "250 + 500 + 750 = 1.500 · FECHOU!", GREEN, -2, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Some os pesos, divida o total, multiplique cada peso.", "O k é o valor de um pacotinho.",
          "A soma das partes tem que dar o total."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 58)


ERROS = [("Dividir o total pelo número de pessoas", "são três pessoas, então ÷ 3",
          "são 9 pacotinhos, não 3: divida pela SOMA DOS PESOS"),
         ("Responder uma parte quando pedem a diferença (ou o contrário)", "a conta estava perfeita",
          "a pergunta era outra: SUBLINHE o que foi pedido antes de calcular"),
         ("Não simplificar pesos grandes", "os números do enunciado são aqueles",
          "dividir todos pelo MDC dá as MESMAS partes, com contas leves")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# Questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=32, w=680):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS1 = [("A", "R$ 800,00", "a MENOR parte", RED), ("B", "R$ 1.200,00", "÷ 3 pessoas", RED),
         ("C", "R$ 1.440,00", "somou 10, não 9", RED), ("D", "R$ 1.600,00", "", GREEN), ("E", "R$ 1.800,00", "÷ 2", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO", "DIVISÃO DIRETA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Um prêmio de R$ 3.600,00 será dividido entre três participantes em partes diretamente proporcionais "
                    "a 2, 3 e 4.", INK),
                   ("O participante que receber a maior quantia ficará com", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABCE"}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS1, 1000, 230, 680, 40, C["24.ok"], "D", cues_in, cues_x, gap=22)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        rrect(c, 170, 470, 740, 340, 18, "#FFFFFF", ra, shadow=True)
        text(c, "pedido: a MAIOR quantia", 540, 525, 28, "black", AMBER, ep(t, C["24.a"], 0.4))
        ftext(c, "2 + 3 + 4 = 9  →  k = 400", 540, 600, 40, "black", PURPLE, ep(t, C["24.b"], 0.4))
        ftext(c, "4 × 400 = 1.600", 540, 680, 46, "black", GREEN, ep(t, C["24.c"], 0.4))
        ftext(c, "800 + 1.200 + 1.600 = 3.600 ✓", 540, 770, 30, "black", INK2, ep(t, C["24.d"], 0.4))


ALTS9 = [("A", "R$ 20.000,00", "idades vizinhas", RED), ("B", "R$ 40.000,00", "", GREEN),
         ("C", "R$ 60.000,00", "é a menor PARTE", RED), ("D", "R$ 80.000,00", "é a parte do meio", RED),
         ("E", "R$ 100.000,00", "é a maior PARTE", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · NÓS FAZEMOS", "A DIFERENÇA ENTRE PARTES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    _enunciado(c, [("Uma herança de R$ 240.000,00 foi dividida entre três herdeiros em partes diretamente proporcionais às "
                    "suas idades: 15, 20 e 25 anos.", INK),
                   ("A diferença entre a maior e a menor parte recebida foi de", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ACDE"}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS9, 1000, 230, 680, 40, C["27.ok"], "B", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["26.end"] - 1.9, 470, 690)
    if t >= C["26.p"] and t < C["27"]:
        chip(c, "k = ?", 470, 580, PURPLE, ep(t, C["26.p"], 0.4), 40)
    if t >= C["27"]:
        ra = ep(t, C["27"], 0.4)
        rrect(c, 170, 485, 740, 330, 18, "#FFFFFF", ra, shadow=True)
        ftext(c, "k = 240.000 ÷ 60 = 4.000", 540, 545, 36, "black", PURPLE, ep(t, C["27.a"], 0.4))
        text(c, "CURTO", 230, 610, 24, "black", GREEN, ep(t, C["27.b"], 0.4), align="left")
        ftext(c, "(25 − 15) × 4.000 = 40.000", 560, 610, 34, "black", GREEN, ep(t, C["27.b"], 0.4))
        text(c, "LONGO", 230, 685, 24, "black", INK2, ep(t, C["27.c"], 0.4), align="left")
        ftext(c, "60.000 · 80.000 · 100.000", 560, 685, 34, "black", INK, ep(t, C["27.c"], 0.4))
        ftext(c, "soma 240.000 ✓   100.000 − 60.000 = 40.000 ✓", 540, 770, 26, "black", INK2, ep(t, C["27.d"], 0.4))


ALTS6 = [("A", "R$ 5.400,00", "1.800 × 3: a parte não é o k", RED), ("B", "R$ 7.200,00", "600 × 12: faltou o peso 3", RED),
         ("C", "R$ 9.000,00", "", GREEN), ("D", "R$ 10.800,00", "não fecha o caixa", RED),
         ("E", "R$ 12.600,00", "1.800 × 7", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "O TOTAL PELA PARTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    _enunciado(c, [("Um valor foi dividido entre três pessoas em partes diretamente proporcionais a 3, 5 e 7.", INK),
                   ("Sabendo que a menor parte foi de R$ 1.800,00, o valor total dividido foi de", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ABDE"}
    if t >= C["29.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS6, 1000, 230, 680, 40, C["30.ok"], "C", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["29.end"] - 1.9, 470, 680)
    if t >= C["30"]:
        ra = ep(t, C["30"], 0.4)
        rrect(c, 170, 470, 740, 340, 18, "#FFFFFF", ra, shadow=True)
        text(c, "menor parte = menor peso (3)", 540, 525, 28, "black", AMBER, ep(t, C["30.a"], 0.4))
        ftext(c, "3k = 1.800  →  k = 600", 540, 600, 40, "black", PURPLE, ep(t, C["30.a"], 0.4))
        ftext(c, "15 × 600 = 9.000", 540, 685, 46, "black", GREEN, ep(t, C["30.b"], 0.4))
        ftext(c, "1.800 + 3.000 + 4.200 = 9.000 ✓", 540, 770, 30, "black", INK2, ep(t, C["30.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A DIVISÃO INVERSA", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    for j, (f, h) in enumerate(((2, 3), (3, 2), (6, 1))):
        a = aa * ep(t, C["33.a"] + 0.25 * j, 0.4)
        if a <= 0:
            continue
        x = 560 + j * 400
        text(c, f"{f} faltas", x, 290, 36, "black", INK, a)
        rrect(c, x - 70, 680 - h * 110, 140, h * 110, 12, DONOS[j], a, shadow=True)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 360, ab, "MENOS FALTAS → MAIS BÔNUS", AMBER, -3, 34)
    pill(c, "ep. 2 · divisão inversa", W / 2, 780, PURPLE, size=32, a=ep(t, C["33.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Quanto deu o k do exercício?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao, passo=b_passo,
              atalho=b_atalho, significa=b_significa, porque=b_porque, equivalentes=b_equivalentes, mdc=b_mdc,
              heranca=b_heranca, diferenca=b_diferenca, total=b_total, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q1=b_q1, q9=b_q9, q6=b_q6, ponte=b_ponte, cta=b_cta)
