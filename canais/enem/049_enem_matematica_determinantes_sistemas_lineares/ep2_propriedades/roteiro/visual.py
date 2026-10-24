"""Visual — Determinantes e Sistemas Lineares, Episódio 2: propriedades que poupam conta (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, selo, regra, pause_timer...).
Peças deste episódio: matriz() (matriz com barras de determinante, casas acesas), botao() (o botão de volume girando ao
lado de uma linha), contador() (o visor "det = ..."), sarrus_fig() (a matriz com as duas colunas repetidas e as
diagonais que descem em verde e sobem em vermelho), espelho() (a troca de linhas).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
import math
from pathlib import Path
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum049", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_determinantes_ep2_propriedades.mp4"
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


def matriz(c, cx, cy, vals, a, cw=110, ch=86, size=46, cores=None, alfas=None, hi=None, hi_col=None, br=None,
           barras=True, row_hi=None, row_col=None):
    """matriz centrada em (cx, cy): vals = linhas de strings; barras = traços verticais de determinante;
    hi = casas acesas; row_hi = linhas acesas (faixa inteira). Devolve (largura, altura)."""
    n, m = len(vals), len(vals[0])
    w, h = m * cw + 40, n * ch + 20
    if a <= 0:
        return w, h
    x0, y0 = cx - w / 2, cy - h / 2
    bcol = br or INK
    for xx in (x0, x0 + w):
        line(c, xx, y0, xx, y0 + h, bcol, a, 5)
        if not barras:
            sg = 1 if xx == x0 else -1
            line(c, xx, y0, xx + 18 * sg, y0, bcol, a, 5)
            line(c, xx, y0 + h, xx + 18 * sg, y0 + h, bcol, a, 5)
    for i in (row_hi or ()):
        rrect(c, x0 + 10, y0 + 10 + ch * i + 4, w - 20, ch - 8, 16, mix("#FFFFFF", row_col or AMBER, 0.28), a)
    for i, row in enumerate(vals):
        for j, s_ in enumerate(row):
            ccx = x0 + 20 + cw * (j + 0.5)
            ccy = y0 + 10 + ch * (i + 0.5)
            if hi and (i, j) in hi:
                rrect(c, ccx - cw / 2 + 6, ccy - ch / 2 + 6, cw - 12, ch - 12, 14, mix("#FFFFFF", hi_col or AMBER, 0.30),
                      a)
            if not s_:
                continue
            al = (alfas or {}).get((i, j), 1.0)
            if al <= 0:
                continue
            sz = size if ftext_w(s_, "black", size) < cw - 14 else size * (cw - 14) / ftext_w(s_, "black", size)
            ftext(c, s_, ccx, ccy + sz * 0.36, sz, "black", (cores or {}).get((i, j), INK), a * al)
    return w, h


def row_y(cy, n, ch, i):
    return cy - (n * ch + 20) / 2 + 10 + ch * (i + 0.5)


def sub(c, base, s, cx, cy, size, col, a):
    """base com subscrito (a + ij), centrado em (cx, cy)"""
    if a <= 0:
        return
    wb, ws = ftext_w(base, "black", size), ftext_w(s, "black", size * 0.55)
    x = cx - (wb + ws) / 2
    ftext(c, base, x, cy + size * 0.36, size, "black", col, a, align="left")
    ftext(c, s, x + wb + 2, cy + size * 0.62, size * 0.55, "black", col, a, align="left")


def botao(c, cx, cy, a, giro=0.0, rot="", col=None, r=40):
    """botão de volume: giro 0 → 1 leva o ponteiro do mínimo ao máximo"""
    if a <= 0:
        return
    col = col or PURPLE
    on = giro > 0.02
    c.drawCircle(cx, cy, r + 8, paint(mix("#FFFFFF", col, 0.18 if on else 0.06), a))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(col if on else GRAY, a, stroke=5))
    ang = math.radians(-225 + 270 * (0.15 + 0.7 * giro))
    line(c, cx, cy, cx + (r - 10) * math.cos(ang), cy + (r - 10) * math.sin(ang), col if on else GRAY, a, 6)
    if rot:
        pill(c, rot, cx + r + 22, cy, col, size=22, a=a * (1 if on else 0.5), anchor="left", bounds=(0, 1920))


def contador(c, cx, cy, s, a, col=None, w=360, rot="det ="):
    """o visor do determinante"""
    if a <= 0:
        return
    col = col or GREEN
    rrect(c, cx - w / 2, cy - 70, w, 140, 26, INK, a, shadow=True)
    text(c, rot, cx - w / 2 + 30, cy + 14, 34, "black", "#FFFFFF", a * 0.7, align="left")
    text(c, s, cx + w / 2 - 30, cy + 26, 76, "black", col, a, align="right")


def sarrus_fig(c, cx, cy, vals, a, cw=104, ch=84, size=42, ad=0.0, asb=0.0):
    """matriz 3 × 3 + duas colunas repetidas (apagadas); ad/asb = alfa das diagonais que descem/sobem"""
    if a <= 0:
        return
    x0 = cx - 5 * cw / 2
    y0 = cy - 3 * ch / 2
    X = lambda j: x0 + cw * (j + 0.5)
    Y = lambda i: y0 + ch * (i + 0.5)
    for xx in (x0 - 10, x0 + 3 * cw + 10):
        line(c, xx, y0 - 6, xx, y0 + 3 * ch + 6, INK, a, 5)
    for j in range(3):
        if ad > 0:
            line(c, X(j) - 22, Y(0) - 18, X(j + 2) + 22, Y(2) + 18, GREEN, ad * 0.35, 4)
        if asb > 0:
            line(c, X(j) - 22, Y(2) + 18, X(j + 2) + 22, Y(0) - 18, RED, asb * 0.35, 4)
    for i in range(3):
        for j in range(5):
            s_ = vals[i][j % 3]
            xx, yy = X(j), Y(i)
            c.drawCircle(xx, yy, size * 0.62, paint("#FFFFFF", a * 0.92))
            ftext(c, s_, xx, yy + size * 0.36, size, "black", INK if j < 3 else GRAY, a * (1 if j < 3 else 0.6))


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


# dados
M8 = [["1", "0", "−1"], ["3", "2", "1"], ["5", "4", "3"]]
M7 = [["1", "2", "0"], ["0", "1", "3"], ["1", "0", "1"]]
DOTS = [["•", "•", "•"], ["•", "•", "•"], ["•", "•", "•"]]
TRI = [["2", "9", "4"], ["0", "5", "7"], ["0", "0", "1"]]
EX = [["3", "7", "1"], ["0", "2", "5"], ["0", "0", "4"]]
DIAG = {(0, 0), (1, 1), (2, 2)}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DETERMINANTES · EPISÓDIO 2", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    dob = ab > 0
    vals = [["2·•"] * 3] * 3 if dob else DOTS
    matriz(c, 600, 470, vals, aa, 150, 110, 46, cores={(i, j): PURPLE for i in range(3) for j in range(3)} if dob
           else None)
    if aa > 0:
        pill(c, "3 × 3", 600, 240, BLUE, size=28, a=aa, anchor="center")
    contador(c, 1300, 360, "5", aa * (1 - ab), BLUE)
    if ab > 0:
        pill(c, "dobre TODOS os números", 600, 690, PURPLE, size=30, a=ab, anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    ad = ep(t, C["01.d"], 0.5)
    if acc > 0:
        contador(c, 1300, 360, "?", acc * (1 - ad), AMBER)
        selo(c, 1300, 560, acc * (1 - ad), "10 ?", AMBER, -5, 70)
    if ad > 0:
        contador(c, 1300, 360, "40", ad, GREEN)
        rrect(c, 1080, 510, 440, 100, 22, mix("#FFFFFF", RED, 0.12), ad)
        linha(c, [("10", RED), ("  não!", INK)], 1300, 560, 50, ad)
        strike(c, 1150, 560, 1215, 560, ad, RED, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "DETERMINANTES · EP. 2", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "2º episódio da série de DETERMINANTES E SISTEMAS LINEARES", W / 2, 240, BLUE, size=28, a=a0,
             anchor="center")
    itens = [("02.a", "det = 0", "em segundos", BLUE, 0), ("02.b", "QUANTO MUDA", "quando a matriz muda", PURPLE, 0),
             ("02.b", "SEM SARRUS", "só propriedades", GREEN, 2.4)]
    for k, (cue, tit, sb, col, dt) in enumerate(itens):
        ak = ep(t, C[cue] + dt, 0.5)
        if ak <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 220, 340, 440, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 220, 340, 440, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 44, "black", col, ak)
        text(c, sb, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódio 1 · Sarrus", 300, y - 75, BLUE, size=22, a=a)
        linha(c, [("det = ", INK), ("3 que descem", GREEN), ("  −  ", INK), ("3 que sobem", RED)], 960, y, 50, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "série de Matrizes", 300, y - 75, PURPLE, size=22, a=a)
        sub(c, "a", "ij", 520, y, 64, PURPLE, a)
        text(c, "linha i · coluna j · a lei diz o que pôr", 1080, y + 14, 38, "black", INK, a)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "potência", 300, y - 75, GREEN, size=22, a=a)
        K.expr(c, "2^3 = 2 · 2 · 2 = 8", 960, y, 60, a, cores=None)


# ======================================================================
# concreto — a planilha com a linha copiada
# ======================================================================

def b_planilha(c, t, C, B):
    head(c, t, B["start"], "INFORMAÇÃO REPETIDA", "UMA LINHA QUE É CÓPIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04"], 0.5)
    ab = ep(t, C["04.a"], 0.5)
    vals = [["4", "1", "6"], ["4", "1", "6"], ["2", "7", "3"]] if ab > 0 else [["4", "1", "6"], ["", "", ""],
                                                                              ["2", "7", "3"]]
    matriz(c, 660, 470, vals, aa, 150, 110, 52, barras=False, row_hi=(0, 1) if ab > 0 else None, row_col=AMBER)
    if ab > 0:
        arrow(c, 920, 395, 920, 500, AMBER, ab, 5, 16)
        pill(c, "cópia", 950, 450, AMBER, size=26, a=ab, anchor="left", bounds=(0, 1920))
    a2 = ep(t, C["04.b"], 0.5)
    if a2 > 0:
        rrect(c, 1120, 330, 520, 150, 24, mix("#FFFFFF", AMBER, 0.16), a2, shadow=True)
        para(c, "informação nova? NENHUMA", 1150, 395, 36, "black", INK, a2, 470, 46)
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        contador(c, 1380, 620, "0", ac, GREEN)


# ======================================================================
# bloco a — zero na hora · bloco b — combinação de linhas
# ======================================================================

def b_zero(c, t, C, B):
    head(c, t, B["start"], "DETERMINANTE ZERO", "SEM CONTA NENHUMA", PURPLE)
    card(c, *CARD_R)
    aa, d = rise(t, C["05.a"])
    if aa > 0:
        cartao(c, 260, 220 + d, 660, 420, aa)
        pill(c, "1 · linha de zeros", 300, 220 + d, PURPLE, size=24, a=aa)
        matriz(c, 590, 420 + d, [["4", "1", "6"], ["0", "0", "0"], ["2", "7", "3"]], aa, 110, 86, 44, row_hi=(1,),
               row_col=PURPLE)
        text(c, "det = 0", 590, 600 + d, 40, "black", GREEN, aa)
    ab, d2 = rise(t, C["05.b"])
    if ab > 0:
        cartao(c, 1000, 220 + d2, 660, 420, ab)
        pill(c, "2 · linhas iguais ou proporcionais", 1040, 220 + d2, PURPLE, size=24, a=ab)
        acc = ep(t, C["05.c"], 0.5)
        matriz(c, 1330, 420 + d2, [["1", "2", "3"], ["2", "4", "6"], ["5", "1", "7"]], ab, 110, 86, 44,
               row_hi=(0, 1) if acc > 0 else None, row_col=AMBER)
        if acc > 0:
            pill(c, "× 2", 1600, row_y(420 + d2, 3, 86, 0.5), AMBER, size=28, a=acc, anchor="center")
        text(c, "det = 0", 1330, 600 + d2, 40, "black", GREEN, ab)
    acc = ep(t, C["05.c"], 0.5)
    defin(c, "PROPORCIONAIS", "uma linha é a outra vezes um número", 260, 680, 1400, acc * (1 - ep(t, C["05.d"], 0.4)),
          BLUE, 32)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        regra(c, "LINHAS PARENTES = informação repetida = det 0", 960, 718, ad, 36, PURPLE)


def b_combinacao(c, t, C, B):
    head(c, t, B["start"], "O PARENTESCO ESCONDIDO", "UMA LINHA FEITA DAS OUTRAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    defin(c, "COMBINAÇÃO DE LINHAS", "uma linha montada com as outras", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["06.b"], 0.5)
    acc = ep(t, C["06.c"], 0.5)
    matriz(c, 640, 500, M8, ab, 130, 100, 50)
    if acc > 0:
        for i in range(2):
            y1, y2 = row_y(500, 3, 100, i), row_y(500, 3, 100, i + 1)
            arrow(c, 860, y1 + 8, 860, y2 - 8, GREEN, acc, 5, 14)
            pill(c, "+ (2, 2, 2)", 890, (y1 + y2) / 2, GREEN, size=26, a=acc, anchor="left", bounds=(0, 1920))
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 1120, 340, 520, 130, 22, mix("#FFFFFF", PURPLE, 0.12), ad)
        sub(c, "L", "3", 1190, 405, 56, PURPLE, ad)
        linha(c, [("= 2", INK)], 1290, 405, 52, ad)
        sub(c, "L", "2", 1385, 405, 56, PURPLE, ad)
        linha(c, [("−", INK)], 1460, 405, 52, ad)
        sub(c, "L", "1", 1530, 405, 56, PURPLE, ad)
    ae = ep(t, C["06.e"], 0.5)
    if ae > 0:
        selo(c, 1380, 600, ae, "det = 0, SEM CONTA", GREEN, -4, 40)


def b_atalho_prop(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ANTES DE QUALQUER SARRUS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · PROCURE A PROPRIEDADE", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        text(c, "TEM ALGUMA PROPRIEDADE AQUI?", 960, 350, 54, "black", INK, aa)
    itens = [("linha de zeros?", 0), ("linhas parentes?", 1.4), ("zeros embaixo da diagonal?", 2.8)]
    for k, (s_, dt) in enumerate(itens):
        ak = ep(t, C["07.b"] + dt, 0.4)
        if ak > 0:
            x = 470 + k * 490
            rrect(c, x - 220, 430, 440, 130, 22, "#FFFFFF", ak, shadow=True)
            badge_num(c, k + 1, x - 170, 495, ak, 26, bg=GREEN)
            para(c, s_, x - 130, 480, 32, "black", INK, ak, 330, 40)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        pill(c, "tem? a conta ENCOLHE ou SOME", 960, 680, GREEN, size=36, a=acc, anchor="center")


# ======================================================================
# bloco c — o espelho e o botão · bloco d — det(kA)
# ======================================================================

def b_espelho(c, t, C, B):
    head(c, t, B["start"], "O QUE MUDA O VALOR", "TROCAR DUAS LINHAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    v = ease_io(clamp((t - C["08.b"] - 0.4) / 1.4))
    ch = 100
    if aa > 0:
        # a matriz original; as linhas 1 e 2 trocam de lugar (a 1ª desce e a 2ª sobe)
        vals = [["", "", ""], ["", "", ""], M7[2]]
        matriz(c, 600, 480, vals, aa, 130, ch, 50)
        x0 = 600 - (3 * 130 + 40) / 2 + 20
        for i, row in ((0, M7[0]), (1, M7[1])):
            yy = row_y(480, 3, ch, i) + (ch if i == 0 else -ch) * v
            for j, s_ in enumerate(row):
                ftext(c, s_, x0 + 130 * (j + 0.5), yy + 18, 50, "black", AMBER if v > 0 else INK, aa)
        contador(c, 1300, 380, "7" if v < 0.5 else "−7", aa, GREEN if v < 0.5 else RED)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        pill(c, "trocar L1 e L2", 600, 250, AMBER, size=30, a=ab, anchor="center")
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        regra(c, "o valor fica · o SINAL troca", 1300, 600, acc, 40, PURPLE)


def b_botao(c, t, C, B):
    head(c, t, B["start"], "UM BOTÃO POR LINHA", "O APARELHO DE SOM", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.5)
    g = ease_io(clamp((t - C["09.a"] - 0.8) / 1.2))
    vals = [["3", "6", "0"], M7[1], M7[2]] if g > 0.5 else M7
    matriz(c, 560, 480, vals, a0, 130, 100, 50, cores={(0, j): PURPLE for j in range(3)} if g > 0.5 else None,
           row_hi=(0,) if g > 0 else None, row_col=PURPLE)
    for i in range(3):
        botao(c, 880, row_y(480, 3, 100, i), a0, g if i == 0 else 0.0, "× 3" if i == 0 and g > 0 else "", PURPLE)
    ab = ep(t, C["09.b"], 0.5)
    contador(c, 1360, 380, "21" if ab > 0 else "7", a0, PURPLE if ab > 0 else GREEN)
    if ab > 0:
        regra(c, "UMA linha × k  →  det × k", 1360, 600, ab, 40, PURPLE)


def b_kA(c, t, C, B):
    head(c, t, B["start"], "A ARMADILHA DO kA", "A MATRIZ INTEIRA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5) * (1 - ep(t, C["10.b"], 0.4))
    defin(c, "ORDEM n", "o número de linhas da matriz quadrada", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["10.b"], 0.5)
    giros = [C["10.c"], C["10.c"] + 2.4, C["10.c"] + 4.6]
    gs = [ease_io(clamp((t - g0) / 0.8)) for g0 in giros]
    vals = [[str(2 * int(x)) for x in M7[i]] if gs[i] > 0.5 else M7[i] for i in range(3)]
    cores = {(i, j): PURPLE for i in range(3) for j in range(3) if gs[i] > 0.5}
    matriz(c, 560, 500, vals, max(ab, aa), 130, 100, 50, cores=cores, row_hi=[i for i in range(3) if gs[i] > 0],
           row_col=PURPLE)
    if aa > 0 and ab <= 0:
        pill(c, "3 × 3: n = 3", 560, 700, BLUE, size=30, a=aa, anchor="center")
    for i in range(3):
        botao(c, 880, row_y(500, 3, 100, i), max(ab, aa), gs[i], "× 2" if gs[i] > 0 else "", PURPLE)
    nval = ["7", "14", "28", "56"][sum(g > 0.5 for g in gs)]
    contador(c, 1360, 400, nval, max(ab, aa), GREEN if nval == "56" else PURPLE)
    if ab > 0:
        pill(c, "dobrar tudo = girar OS TRÊS botões", 1360, 260, AMBER, size=28, a=ab, anchor="center")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 540, 560, 130, 22, mix("#FFFFFF", PURPLE, 0.12), ad)
        K.expr(c, "det(kA) = k^n · det A", 1360, 605, 50, ad, cores=None)
        text(c, "2³ · 7 = 56", 1360, 730, 40, "black", GREEN, ad)


# ======================================================================
# bloco e — o que não muda e a triangular
# ======================================================================

def b_nao_muda(c, t, C, B):
    head(c, t, B["start"], "O QUE NÃO MUDA", "TRÊS REGRAS DE BOLSO", PURPLE)
    card(c, *CARD_R)
    itens = [("11.a", "L2 + 2·L1", "somar a uma linha um múltiplo de outra: NÃO muda", GREEN),
             ("11.b", "det A^t = det A", "transposta: linhas viram colunas", BLUE),
             ("11.c", "det(AB) = det A · det B", "o do produto é o produto dos dets", PURPLE)]
    for k, (cue, f, sb, col) in enumerate(itens):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 260, y - 60, 1400, 130, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, 260, y - 60, 14, 130, 7, col, ak)
        K.expr(c, f, 620, y, 50, ak, cores=None)
        para(c, sb, 1000, y - 8, 30, "bold", INK2, ak, 640, 38)


def b_triangular(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "TRIANGULAR E DIAGONAL", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, aa, 0.08)
        text(c, "ATALHO · SEM SARRUS", 960, 250, 24, "black", GREEN, aa, tracking=2)
        zeros = {(1, 0), (2, 0), (2, 1)}
        matriz(c, 620, 480, TRI, aa, 120, 96, 48, hi=zeros, hi_col=BLUE)
        text(c, "TRIANGULAR: zeros abaixo da diagonal", 620, 690, 30, "black", BLUE, aa)
        a2 = ep(t, C["12.a"] + 4.5, 0.4) * (1 - ep(t, C["12.c"], 0.4))
        matriz(c, 1300, 480, [["2", "0", "0"], ["0", "5", "0"], ["0", "0", "1"]], a2, 100, 82, 42)
        text(c, "DIAGONAL: zeros fora dela", 1300, 690, 30, "black", BLUE, a2)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        matriz(c, 620, 480, TRI, ab, 120, 96, 48, hi=DIAG, hi_col=GREEN, cores={k: GREEN for k in DIAG})
        pill(c, "det = produto da diagonal", 960, 760, GREEN, size=34, a=ab, anchor="center")
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 1080, 425, 440, 110, 22, mix("#FFFFFF", GREEN, 0.18), acc)
        text_mid(c, "2 · 5 · 1 = 10", 1300, 480, 52, "black", GREEN, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("13", "SUA VEZ", "PAUSE E TENTE", GREEN), ("14", "VAMOS JUNTOS", "PROPRIEDADE ANTES DA CONTA",
                                                                            GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    ab = ep(t, C["13.b"], 0.5)
    sol = t >= C["14"]
    a1 = ep(t, C["14.a"], 0.5) if sol else 0
    matriz(c, 560, 420, EX, aa, 110, 90, 46, hi=DIAG if a1 > 0 else None, hi_col=GREEN,
           cores={k: GREEN for k in DIAG} if a1 > 0 else None)
    if aa > 0:
        text(c, "1 · det = ?", 560, 640, 40, "black", INK, aa)
    if ab > 0:
        cartao(c, 1000, 300, 640, 260, ab)
        text(c, "2 · matriz 2 × 2", 1320, 370, 36, "black", INK, ab)
        text(c, "det A = 3", 1320, 440, 44, "black", BLUE, ab)
        text(c, "det(3A) = ?", 1320, 510, 44, "black", PURPLE, ab)
    if not sol:
        pause_timer(c, t, C["13.end"] - 1.9, 960, 730)
        return
    if a1 > 0:
        rrect(c, 330, 680, 460, 90, 20, mix("#FFFFFF", GREEN, 0.16), a1)
        text_mid(c, "3 · 2 · 4 = 24", 560, 725, 44, "black", GREEN, a1)
    a2 = ep(t, C["14.b"], 0.5)
    if a2 > 0:
        rrect(c, 1000, 590, 640, 180, 22, mix("#FFFFFF", PURPLE, 0.12), a2)
        text(c, "n = 2", 1320, 640, 34, "black", BLUE, a2)
        text(c, "3² · 3 = 9 · 3 = 27", 1320, 720, 46, "black", GREEN, ep(t, C["14.b"] + 2.4, 0.4))


# ======================================================================
# recap e erro
# ======================================================================

FRASES = ["Linhas parentes zeram o determinante.",
          "Matriz inteira vezes k: o determinante vai vezes k elevado a n.",
          "Triangular: multiplique a diagonal."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["15", "23"])
    frame(c, t, B["start"] if sid == "15" else C["23"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "15" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("det(2A) = 2 · det A  (7 vira 14)",
          "com números, dobrar tudo dobra o resultado",
          "são 3 linhas, 3 botões: o fator é 2³ = 8 → 56.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["16"], ERROS)


# ======================================================================
# questão 8 (eu faço) e questão 3 (você faz)
# ======================================================================

ALTS8 = [("A", "−12", "somou as duas partes", RED), ("B", "−6", "só a parte que desce", RED),
         ("C", "0", "", GREEN), ("D", "6", "só a que sobe, com o menos", RED), ("E", "12", "somou e trocou o sinal", RED)]


def b_q8(c, t, C, B):
    sid = which(t, C, ["17", "18", "19", "20"])
    heads = {"17": "PROPRIEDADE EM VEZ DE CONTA", "18": "EU FAÇO", "19": "CONFIRO POR SARRUS", "20": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "17" else C[sid], "QUESTÃO 8 · ESTILO ENEM", heads[sid], PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"17.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"20.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS8, 1300, 260, 420, 40, C["18.ok"], "C", cues_in, cues_x, gap=34)
    a0 = ep(t, C["17.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if sid == "17":
        if a0 > 0:
            rrect(c, 190, 280, 1020, 140, 22, mix("#FFFFFF", PURPLE, 0.10), a0)
            text(c, "matriz quadrada A · ordem 3", 700, 330, 34, "bold", INK2, a0)
            sub(c, "a", "ij", 610, 385, 60, PURPLE, a0)
            text_mid(c, "= 2i − j", 770, 385, 56, "black", PURPLE, a0)
        ab = ep(t, C["17.b"], 0.5)
        if ab > 0:
            text(c, "O determinante de A é", 700, 520, 44, "black", INK, ab)
        return
    if sid == "18":
        # monta a matriz casa a casa (linha 1 narrada; linhas 2 e 3 de uma vez)
        tl1 = [C["18.a"] + 1.6, C["18.a"] + 3.6, C["18.a"] + 5.6]
        alf = {}
        for j in range(3):
            alf[(0, j)] = ep(t, tl1[j], 0.3)
            alf[(1, j)] = ep(t, C["18.b"], 0.3)
            alf[(2, j)] = ep(t, C["18.b"] + 2.0, 0.3)
        acc = ep(t, C["18.c"], 0.5)
        matriz(c, 520, 430, M8, ep(t, C["18"], 0.4), 120, 96, 46, alfas=alf)
        if acc > 0:
            for i in range(2):
                y1, y2 = row_y(430, 3, 96, i), row_y(430, 3, 96, i + 1)
                arrow(c, 730, y1 + 8, 730, y2 - 8, GREEN, acc, 5, 14)
                pill(c, "+ (2, 2, 2)", 755, (y1 + y2) / 2, GREEN, size=22, a=acc, anchor="left", bounds=(0, 1260))
        if t < C["18.c"]:
            ak = ep(t, C["18.a"], 0.4)
            if ak > 0:
                pill(c, "2·1 − 1 · 2·1 − 2 · 2·1 − 3", 520, 660, PURPLE, size=26, a=ak, anchor="center", bounds=(160, 1270))
        ad = ep(t, C["18.d"], 0.5)
        if ad > 0:
            selo(c, 620, 700, ad, "LINHA PARENTE: det = 0", GREEN, -3, 34)
        return
    # 19 e 20: Sarrus
    a1 = ep(t, C["19"], 0.4)
    sarrus_fig(c, 680, 400, M8, a1, 104, 84, 40, ad=ep(t, C["19.a"], 0.5), asb=ep(t, C["19.b"], 0.5))
    ad, asb, acc = ep(t, C["19.a"], 0.5), ep(t, C["19.b"], 0.5), ep(t, C["19.c"], 0.5)
    if ad > 0:
        linha(c, [("descem:  6 + 0 − 12 = ", INK), ("−6", GREEN)], 680, 600, 36, ad)
    if asb > 0:
        linha(c, [("sobem:  −10 + 4 + 0 = ", INK), ("−6", RED)], 680, 660, 36, asb)
    if acc > 0:
        rrect(c, 380, 700, 600, 80, 18, mix("#FFFFFF", GREEN, 0.18), acc)
        linha(c, [("−6 − (−6) = ", INK), ("0", GREEN)], 680, 740, 42, acc)


ALTS3 = [("A", "10", "uma linha só", RED), ("B", "20", "2², como se fosse 2 × 2", RED),
         ("C", "30", "× 2 e × a ordem 3", RED), ("D", "40", "", GREEN), ("E", "125", "elevou o 5 ao cubo", RED)]


def b_q3(c, t, C, B):
    sid = which(t, C, ["21", "22"])
    head(c, t, B["start"] if sid == "21" else C["22"], "QUESTÃO 3 · ESTILO ENEM",
         "VOCÊ FAZ" if sid == "21" else "VAMOS CONFERIR", GREEN)
    card(c, *CARD_R)
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS3, 1300, 260, 420, 40, C["22.ok"], "D", cues_in, cues_x, gap=34)
    a0 = ep(t, C["21.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    if a0 > 0:
        rrect(c, 190, 240, 1020, 150, 22, mix("#FFFFFF", BLUE, 0.10), a0)
        para(c, "A tem ordem 3 e det A = 5. O programa gera 2A (todos os elementos × 2).", 230, 300, 34, "black", INK,
             a0, 950, 44)
    ab = ep(t, C["21.b"], 0.5)
    if ab > 0 and sid == "21":
        text(c, "det(2A) = ?", 700, 500, 56, "black", PURPLE, ab)
    if sid == "21":
        pause_timer(c, t, C["21.end"] - 1.9, 700, 660)
        return
    aa = ep(t, C["22.a"], 0.4)
    giros = [C["22.a"] + 2.4, C["22.a"] + 3.4, C["22.a"] + 4.4]
    gs = [ease_io(clamp((t - g0) / 0.6)) for g0 in giros]
    matriz(c, 420, 560, DOTS, aa, 90, 76, 36, row_hi=[i for i in range(3) if gs[i] > 0], row_col=PURPLE)
    for i in range(3):
        botao(c, 640, row_y(560, 3, 76, i), aa, gs[i], "", PURPLE, r=30)
    nval = ["5", "10", "20", "40"][sum(g > 0.5 for g in gs)]
    contador(c, 960, 520, nval, aa, GREEN if nval == "40" else PURPLE, w=320)
    a2 = ep(t, C["22.a"] + 5.6, 0.4)
    if a2 > 0:
        text(c, "2³ · 5 = 40", 960, 680, 44, "black", GREEN, a2)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REGRA DE CRAMER", PURPLE)
    aa = ep(t, C["24.a"], 0.5)
    if aa > 0:
        contador(c, 620, 330, "≠ 0", aa, GREEN, w=380)
        arrow(c, 830, 330, 980, 330, PURPLE, aa, 6, 18)
        text_mid(c, "tem INVERSA", 1260, 330, 56, "black", PURPLE, aa)
    ab = ep(t, C["24.b"], 0.5)
    if ab > 0:
        cartao(c, 360, 450, 1200, 140, ab)
        text_mid(c, "ingressos: inteiras e meias · garante o quê?", 960, 520, 40, "black", INK, ab)
    acc = ep(t, C["24.c"], 0.5)
    if acc > 0:
        pill(c, "UMA ÚNICA RESPOSTA", 960, 660, BLUE, size=40, a=acc, anchor="center")
    ad = ep(t, C["24.d"], 0.5)
    if ad > 0:
        selo(c, 960, 770, ad, "E ELE CALCULA: CRAMER", GREEN, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["25.like"], C["25.sub"], C["25.bell"], C["25.com"], C["25.bye"],
        "Você teria respondido 10 no gancho?", canal="no Estudativo", anki=C["25.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, planilha=b_planilha, zero=b_zero,
              combinacao=b_combinacao, atalho_prop=b_atalho_prop, espelho=b_espelho, botao=b_botao, kA=b_kA,
              nao_muda=b_nao_muda, triangular=b_triangular, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q8=b_q8, q3=b_q3, ponte=b_ponte, cta=b_cta)
