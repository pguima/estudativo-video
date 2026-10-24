"""Visual — Determinantes e Sistemas Lineares, Episódio 1: o que é o determinante (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: matriz() (com colchetes ou com as BARRAS do determinante), casaco() (o produto da secundária
entre parênteses), sarrus() (a 3 × 3 com as duas colunas repetidas e as setas verdes e vermelhas), placar() (verde ×
vermelho), riscar() (linha e coluna riscadas no Laplace), cadeado() (a chave que abre ou não abre).
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
_s = importlib.util.spec_from_file_location("comum049", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_determinantes_ep1_determinante_inversa.mp4"
CARD_R = K.CARD_R
VERDE_T = "#1F9D55"    # time verde do Sarrus
VERM_T = "#D64545"     # time vermelho do Sarrus

GANCHO = [[3, -2], [4, 5]]
S3 = [[2, 1, 3], [0, 4, 1], [5, 2, 1]]                  # matriz do material (det −51)
EQ = [["x", "4"], ["1", "x − 3"]]                       # bloco c (exemplo novo do prompt)
NF2 = [[-2, 3], [4, -5]]                                # nós fazemos 2 × 2
NF3 = [[1, 2, 0], [0, 1, 3], [2, 0, 1]]                 # nós fazemos 3 × 3
Q2M = [["x", "3"], ["2", "x + 1"]]                      # Questão 2
PONTE = [[1, 0, -1], [3, 2, 1], [5, 4, 3]]


def sg(v):
    """número com o sinal de menos tipográfico"""
    if isinstance(v, str):
        return v
    return ("−" + str(-v)) if v < 0 else str(v)


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


def colchete(c, x, y0, y1, a, lado=1, col=INK, sw=5):
    if a <= 0:
        return
    d = 16 * lado
    p = skia.Path(); p.moveTo(x + d, y0); p.lineTo(x, y0); p.lineTo(x, y1); p.lineTo(x + d, y1)
    c.drawPath(p, paint(col, a, stroke=sw))


def matriz(c, M, cx, cy, cw, ch, a, size=None, cor=None, fundo=None, alfa=None, bcol=INK, barras=False):
    """matriz M centrada em (cx, cy), casas cw × ch; barras=True desenha as barras verticais do determinante.
    cor/alfa/fundo = {(i, j): ...} (fundo = (cor, alfa)). Devolve (x0, y0, w, h)."""
    if a <= 0:
        return (0, 0, 0, 0)
    m, n = len(M), len(M[0])
    size = size or ch * 0.5
    w, h = n * cw, m * ch
    x0, y0 = cx - w / 2, cy - h / 2
    for (i, j), (fc, fa) in (fundo or {}).items():
        if fa > 0:
            rrect(c, x0 + j * cw + 4, y0 + i * ch + 4, cw - 8, ch - 8, 12, fc, a * fa)
    for i in range(m):
        for j in range(n):
            v = M[i][j]
            if v is None:
                continue
            aa = a * (alfa or {}).get((i, j), 1.0)
            fmid(c, sg(v), x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch, size, "black", (cor or {}).get((i, j), INK), aa)
    if barras:
        line(c, x0 - 8, y0 - 4, x0 - 8, y0 + h + 4, bcol, a, 5)
        line(c, x0 + w + 8, y0 - 4, x0 + w + 8, y0 + h + 4, bcol, a, 5)
    else:
        colchete(c, x0 - 6, y0 - 4, y0 + h + 4, a, 1, bcol)
        colchete(c, x0 + w + 6, y0 - 4, y0 + h + 4, a, -1, bcol)
    return (x0, y0, w, h)


def faixa(c, x, y, w, h, col, a, r=14):
    if a <= 0:
        return
    rrect(c, x, y, w, h, r, col, 0.16 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), paint(col, a, stroke=4))


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def halo(c, s, cx, cy, size, col, a):
    """número com contorno claro, para ficar legível por cima das setas"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size)
    rrect(c, cx - w / 2 - 8, cy - size * 0.45, w + 16, size * 0.9, 10, "#FFFFFF", a * 0.85)
    fmid(c, s, cx, cy, size, "black", col, a)


def diag(c, x0, y0, x1, y1, col, a, prog=1.0, sw=7):
    """diagonal com seta, crescendo de (x0, y0) até (x1, y1)"""
    if a <= 0 or prog <= 0:
        return
    xe, ye = lerp(x0, x1, prog), lerp(y0, y1, prog)
    arrow(c, x0, y0, xe, ye, col, a, sw, 18)


def casaco(c, s, cx, cy, size, a, vest=1.0, col=None):
    """o produto 'de casaco': o número com os parênteses fechando em volta (vest 0 → 1)"""
    if a <= 0:
        return 0
    col = col or AMBER
    w = ftext_w(s, "black", size)
    fmid(c, s, cx, cy, size, "black", col, a)
    if vest > 0:
        gap = lerp(80, 18, ease_io(vest))
        fmid(c, "(", cx - w / 2 - gap, cy, size * 1.1, "black", col, a * vest)
        fmid(c, ")", cx + w / 2 + gap, cy, size * 1.1, "black", col, a * vest)
    return w + 2 * 18 + size * 0.6


def cadeado(c, cx, cy, s, aberto, col, a):
    """cadeado: corpo + arco; aberto (0 → 1) levanta e gira o arco"""
    if a <= 0:
        return
    rrect(c, cx - s * 0.55, cy - s * 0.1, s * 1.1, s * 0.85, s * 0.14, col, a)
    c.drawCircle(cx, cy + s * 0.28, s * 0.11, paint("#FFFFFF", a))
    c.save()
    c.translate(cx + s * 0.32, cy - s * 0.1 - aberto * s * 0.25)
    c.rotate(-28 * aberto)
    p = skia.Path()
    p.moveTo(-s * 0.64, 0)
    p.lineTo(-s * 0.64, -s * 0.28)
    p.arcTo(skia.Rect.MakeXYWH(-s * 0.64, -s * 0.6, s * 0.64, s * 0.64), 180, 180, False)
    p.lineTo(0, 0)
    c.drawPath(p, paint(col, a, stroke=s * 0.13))
    c.restore()


# --- Sarrus -----------------------------------------------------------------------------------------------------------

def sarrus(c, M, cx, cy, cw, ch, a, rep=1.0, verdes=(0, 0, 0), vermelhas=(0, 0, 0), size=None, fundo=None, zeros=0.0):
    """a 3 × 3 com barras e as 2 colunas repetidas à direita (rep 0 → 1); verdes/vermelhas = progresso de cada seta.
    zeros > 0 marca de âmbar as casas com zero. Devolve (x0, y0)."""
    if a <= 0:
        return (0, 0)
    size = size or ch * 0.5
    x0, y0 = cx - 2.5 * cw, cy - 1.5 * ch
    fz = dict(fundo or {})
    if zeros > 0:
        for i in range(3):
            for j in range(5):
                if M[i][j % 3] == 0 and (j < 3 or rep > 0.5):
                    fz[(i, j)] = (AMBER, 0.35 * zeros)
    for (i, j), (fc, fa) in fz.items():
        if fa > 0:
            rrect(c, x0 + j * cw + 6, y0 + i * ch + 6, cw - 12, ch - 12, 12, fc, a * fa)
    line(c, x0 - 6, y0 - 4, x0 - 6, y0 + 3 * ch + 4, INK, a, 5)
    line(c, x0 + 3 * cw + 6, y0 - 4, x0 + 3 * cw + 6, y0 + 3 * ch + 4, INK, a, 5)
    if rep > 0:
        line(c, x0 + 3 * cw + 6, y0 - 20, x0 + 3 * cw + 6, y0 + 3 * ch + 20, GRAY, a * rep, 2, dash=(10, 8))
    e = 0.32
    for k, pg in enumerate(verdes):
        xs, ys = x0 + (k + 0.5 - e) * cw, y0 + (0.5 - e) * ch
        xe, ye = x0 + (k + 2.5 + e) * cw, y0 + (2.5 + e) * ch
        diag(c, xs, ys, xe, ye, VERDE_T, a * 0.7, pg, 5)
    for k, pg in enumerate(vermelhas):
        j = k + 2
        xs, ys = x0 + (j + 0.5 + e) * cw, y0 + (0.5 - e) * ch
        xe, ye = x0 + (j - 2 + 0.5 - e) * cw, y0 + (2.5 + e) * ch
        diag(c, xs, ys, xe, ye, VERM_T, a * 0.7, pg, 5)
    for i in range(3):
        for j in range(5):
            if j >= 3 and rep <= 0:
                continue
            aa = a if j < 3 else a * rep * 0.75
            halo(c, sg(M[i][j % 3]), x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch, size, INK if j < 3 else GRAY, aa)
    return (x0, y0)


def placar(c, x, y, w, titulo, itens, total, col, a, alfas=None, a_tot=1.0):
    """placar de um time: lista de produtos e o total embaixo"""
    if a <= 0:
        return
    rrect(c, x, y, w, 330, 24, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 58, 24, col, a * 0.16)
    text(c, titulo, x + w / 2, y + 40, 26, "black", col, a, tracking=2)
    for k, s_ in enumerate(itens):
        aa = a * (alfas[k] if alfas else 1.0)
        if aa > 0:
            ftext(c, s_, x + w / 2, y + 112 + k * 52, 32, "black", INK, aa)
    if a_tot > 0:
        line(c, x + 30, y + 250, x + w - 30, y + 250, col, a * a_tot, 3)
        ftext(c, total, x + w / 2, y + 302, 44, "black", col, a * a_tot)


def riscar(c, x0, y0, cw, ch, i, j, a, col=None):
    """risca a linha i e a coluna j de uma 3 × 3"""
    if a <= 0:
        return
    col = col or GRAY
    yy = y0 + (i + 0.5) * ch
    xx = x0 + (j + 0.5) * cw
    line(c, x0 - 10, yy, x0 + 3 * cw + 10, yy, col, a * 0.8, 6)
    line(c, xx, y0 - 10, xx, y0 + 3 * ch + 10, col, a * 0.8, 6)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DETERMINANTES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    matriz(c, GANCHO, 520, 520, 170, 150, aa, 80, barras=True)
    ab = ep(t, C["01.b"], 0.5)
    acc = ep(t, C["01.c"], 0.5)
    if ab > 0:
        rrect(c, 960, 300, 760, 170, 26, mix("#FFFFFF", RED, 0.08), ab)
        linha(c, [("15 − 8 = ", INK), ("7", RED)], 1340, 385, 76, ab)
        if ab >= 1:
            strike(c, 1150, 385, 1530, 385, ep(t, C["01.b"] + 2.2, 0.4), RED)
        pill(c, "METADE DA TURMA", 1340, 300, RED, size=24, a=ab, anchor="center")
    if acc > 0:
        rrect(c, 960, 530, 760, 170, 26, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("15 − (−8) = ", INK), ("23", GREEN)], 1340, 615, 76, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 960, 800, ad, "ESTE NÚMERO DIZ SE TEM INVERSA", PURPLE, -2, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular determinantes 2 × 2 e 3 × 3", "sem errar sinal"),
            ("02.b", "saber, só por ele, se a matriz tem inversa", "o teste da chave")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "SINAIS", [("(−) · (−) = ", INK), ("+", GREEN), ("      (−) · (+) = ", INK), ("−", RED)], BLUE),
             ("03.b", "MATRIZES", [("a inversa 2 × 2 divide por  ", INK), ("ad − bc", PURPLE)], PURPLE),
             ("03.c", "2º GRAU", [("x² − 5x + 6 = 0  →  soma 5 · produto 6  →  ", INK), ("2 e 3", GREEN)], GREEN)]
    for k, (cue, tag, partes, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        y = 320 + k * 175 + d
        if a > 0:
            rrect(c, 240, y - 70, 1440, 140, 24, "#FFFFFF", a, shadow=True)
            pill(c, tag, 290, y, col, size=24, a=a)
            linha(c, partes, 560, y, 44, a, align="left")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "A CHAVE DA CRIPTOGRAFIA", "POR QUE ÀS VEZES NÃO ABRE?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 300, 300, 150, 22, "#F2F4F7", aa)
        text(c, "MENSAGEM", 380, 340, 24, "black", INK2, aa, tracking=2)
        text(c, "8 · 15 · 12 · 1", 380, 410, 40, "black", INK, aa)
        arrow(c, 560, 375, 700, 375, INK2, aa, 5, 16)
        matriz(c, [[2, 1], [1, 1]], 820, 375, 90, 80, aa, 40, bcol=PURPLE)
        text(c, "CHAVE", 820, 290, 24, "black", PURPLE, aa, tracking=2)
        arrow(c, 940, 375, 1080, 375, INK2, aa, 5, 16)
        rrect(c, 1110, 300, 300, 150, 22, mix("#FFFFFF", PURPLE, 0.10), aa)
        text(c, "EMBARALHADA", 1260, 340, 24, "black", PURPLE, aa, tracking=2)
        text(c, "31 · 23 · 25 · 13", 1260, 410, 36, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        arrow(c, 1260, 470, 1260, 560, GREEN, ab, 5, 16)
        text(c, "INVERSA DA CHAVE → lê de volta", 1260, 610, 30, "black", GREEN, ab)
        cadeado(c, 1640, 600, 70, ep(t, C["04.b"] + 0.6, 0.6), GREEN, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        cadeado(c, 420, 640, 80, 0, RED, acc)
        check_icon(c, 520, 600, 30, acc, RED, "x")
        text(c, "esta chave NÃO ABRE: não tem inversa", 580, 650, 32, "black", RED, acc, align="left")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "UM ÚNICO NÚMERO AVISA ANTES: o DETERMINANTE", W / 2, 770, ad, 36, BLUE)


# ======================================================================
# bloco a — só quadradas
# ======================================================================

def b_definicao(c, t, C, B):
    head(c, t, B["start"], "DETERMINANTE", "SÓ MATRIZ QUADRADA TEM", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "DETERMINANTE = um número calculado a partir de uma matriz QUADRADA", W / 2, 245, 32, "black", BLUE, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        matriz(c, [[1, 2], [3, 4]], 400, 450, 90, 80, ab, 40)
        conferido(c, "2 × 2", 345, 600, ab, True, 30)
        matriz(c, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 830, 450, 80, 66, ab, 34)
        conferido(c, "3 × 3", 775, 600, ab, True, 30)
        matriz(c, [[1, 2, 3], [4, 5, 6]], 1300, 450, 90, 80, ab, 40, bcol=RED)
        conferido(c, "2 × 3: NÃO TEM", 1170, 600, ab, False, 30)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        pill(c, "ORDEM = o tamanho da quadrada  ·  ordem 2 = 2 × 2", W / 2, 690, BLUE, size=28, a=acc, anchor="center")
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        linha(c, [("ordem 1:   det [−7] = ", INK), ("−7", PURPLE)], W / 2, 780, 44, ad)


# ======================================================================
# bloco b — ordem 2
# ======================================================================

def b_ordem2(c, t, C, B):
    head_seq(c, t, C, [("06", "ORDEM 2", "PRINCIPAL MENOS SECUNDÁRIA", PURPLE), ("07", "O PRODUTO DE CASACO", "O SINAL VAI JUNTO", AMBER),
                       ("08", "ATALHO", "OS DOIS PRODUTOS COMPLETOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    mx, my, cw, ch = 470, 500, 170, 150
    x0, y0 = mx - cw, my - ch
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        ab = ep(t, C["06.b"], 0.5)
        matriz(c, [["a", "b"], ["c", "d"]], mx, my, cw, ch, 1.0, 80, barras=True,
               cor={(0, 0): mix(INK, BLUE, aa), (1, 1): mix(INK, BLUE, aa), (0, 1): mix(INK, AMBER, ab),
                    (1, 0): mix(INK, AMBER, ab)})
        diag(c, x0 + 30, y0 + 30, x0 + 2 * cw - 30, y0 + 2 * ch - 30, BLUE, aa * 0.7, ep(t, C["06.a"], 0.8))
        diag(c, x0 + 2 * cw - 30, y0 + 30, x0 + 30, y0 + 2 * ch - 30, AMBER, ab * 0.7, ep(t, C["06.b"], 0.8))
        if aa > 0:
            text(c, "DIAGONAL PRINCIPAL: desce para a direita", 1250, 360, 30, "black", BLUE, aa)
            linha(c, [("a · d", BLUE)], 1250, 420, 48, aa)
        if ab > 0:
            text(c, "DIAGONAL SECUNDÁRIA: a outra", 1250, 510, 30, "black", AMBER, ab)
            linha(c, [("b · c", AMBER)], 1250, 570, 48, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            regra(c, "det = ad − bc", 1250, 720, acc, 54)
        return
    matriz(c, GANCHO, mx, my, cw, ch, 1.0, 80, barras=True,
           cor={(0, 0): BLUE, (1, 1): BLUE, (0, 1): AMBER, (1, 0): AMBER})
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        ab = ep(t, C["07.b"], 0.5)
        diag(c, x0 + 30, y0 + 30, x0 + 2 * cw - 30, y0 + 2 * ch - 30, BLUE, aa * 0.6, ep(t, C["07.a"], 0.8))
        diag(c, x0 + 2 * cw - 30, y0 + 30, x0 + 30, y0 + 2 * ch - 30, AMBER, ab * 0.6, ep(t, C["07.b"], 0.8))
        if aa > 0:
            linha(c, [("3 · 5 = ", INK), ("15", BLUE)], 1250, 320, 50, aa)
        if ab > 0:
            linha(c, [("(−2) · 4 = ", INK), ("−8", AMBER)], 1250, 410, 50, ab)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            rrect(c, 960, 480, 580, 150, 24, mix("#FFFFFF", AMBER, 0.10), acc)
            fmid(c, "15 −", 1130, 555, 64, "black", INK, acc)
            casaco(c, "−8", 1330, 555, 64, acc, ep(t, C["07.c"] + 1.4, 0.8))
            pill(c, "DE CASACO", 1250, 480, AMBER, size=22, a=acc, anchor="center")
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            linha(c, [("= 15 + 8 = ", INK), ("23", GREEN)], 1250, 720, 60, ad)
        return
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 960, 230, 720, 160, "ATALHO", ["escreva os 2 produtos COM SINAL", "só depois subtraia"], aa, 30)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        fmid(c, "15", 1110, 520, 64, "black", BLUE, ab)
        fmid(c, "e", 1220, 520, 40, "bold", GRAY, ab)
        casaco(c, "−8", 1360, 520, 64, ab, 1.0)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 960, 620, 720, 140, 24, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("15 − (−8) = ", INK), ("23", GREEN), ("  ✓", GREEN)], 1320, 690, 56, acc)


# ======================================================================
# bloco c — determinante numa equação
# ======================================================================

def b_equacao(c, t, C, B):
    head(c, t, B["start"], "DETERMINANTE NUMA EQUAÇÃO", "QUANDO DÁ ZERO?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    ab = ep(t, C["09.b"], 0.5)
    matriz(c, EQ, 430, 470, 170, 140, aa, 60, barras=True,
           cor={(0, 0): mix(INK, BLUE, ab), (1, 1): mix(INK, BLUE, ab), (0, 1): mix(INK, AMBER, ab),
                (1, 0): mix(INK, AMBER, ab)})
    if aa > 0:
        linha(c, [("= 0", PURPLE)], 680, 470, 60, aa, align="left")
        text(c, "x = ?", 430, 720, 44, "black", PURPLE, aa)
    xl = 900
    if ab > 0:
        linha(c, [("x · (x − 3)", BLUE), ("  −  ", INK), ("(4 · 1)", AMBER), ("  = 0", INK)], xl, 300, 46, ab,
              align="left")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        linha(c, [("x² − 3x − 4 = 0", PURPLE)], xl, 400, 52, acc, align="left")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        linha(c, [("soma 3 · produto −4  →  ", INK), ("x = 4", GREEN), ("  ou  ", INK), ("x = −1", GREEN)], xl, 500,
              40, ad, align="left")
        a2 = ep(t, C["09.d"] + 3.5, 0.5)
        conferido(c, "x = 4:  4 · 1 − 4 = 0", xl, 600, a2, True, 34)
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        chip(c, "det = 0 → a chave NÃO ABRE", 1260, 730, RED, ae, 34)


# ======================================================================
# bloco d — Sarrus
# ======================================================================

SX, SY, SCW, SCH = 560, 520, 130, 110


def b_sarrus(c, t, C, B):
    head_seq(c, t, C, [("10", "REGRA DE SARRUS", "ORDEM 3", PURPLE), ("11", "O TIME VERDE", "DESCE PARA A DIREITA", GREEN),
                       ("12", "O TIME VERMELHO", "VERDE MENOS VERMELHO, EM BLOCO", RED),
                       ("13", "ATALHO", "PLACAR EM DUAS COLUNAS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11", "12", "13"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        rep = ep(t, C["10.b"], 0.8)
        acc = ep(t, C["10.c"], 0.5)
        g = [ep(t, C["10.c"] + 0.6 + k * 0.5, 0.6) for k in range(3)]
        r = [ep(t, C["10.c"] + 3.5 + k * 0.5, 0.6) for k in range(3)]
        sarrus(c, S3, SX, SY, SCW, SCH, max(aa, 0.001) if t >= C["10"] else 0, rep, g, r if acc > 0 else (0, 0, 0))
        if aa > 0:
            text(c, "SARRUS: o determinante 3 × 3 pelas diagonais", 1330, 300, 28, "black", PURPLE, aa)
        if rep > 0:
            pill(c, "repita as 2 primeiras colunas", 1330, 380, GRAY, size=24, a=rep, anchor="center")
        if acc > 0:
            text(c, "VERDE: descem para a DIREITA", 1330, 520, 32, "black", VERDE_T, ep(t, C["10.c"] + 0.6, 0.4))
            text(c, "VERMELHO: descem para a ESQUERDA", 1330, 600, 32, "black", VERM_T, ep(t, C["10.c"] + 3.5, 0.4))
        return
    if sid == "11":
        cues = ["11.a", "11.b", "11.c"]
        g = [ep(t, C[q], 0.7) for q in cues]
        fundo = {}
        cells = [((0, 0), (1, 1), (2, 2)), ((0, 1), (1, 2), (2, 3)), ((0, 2), (1, 3), (2, 4))]
        for k, q in enumerate(cues):
            on = ep(t, C[q], 0.4) * (1 - ep(t, C[cues[k + 1]] if k < 2 else C["11.d"], 0.3))
            for ij in cells[k]:
                fundo[ij] = (VERDE_T, 0.30 * on)
        sarrus(c, S3, SX - 60, SY, SCW, SCH, 1.0, 1.0, g, (0, 0, 0), fundo=fundo)
        placar(c, 1290, 290, 360, "TIME VERDE", ["2 · 4 · 1 = 8", "1 · 1 · 5 = 5", "3 · 0 · 2 = 0"], "13", VERDE_T, 1.0,
               alfas=g, a_tot=ep(t, C["11.d"], 0.5))
        return
    if sid == "12":
        cues = ["12.a", "12.b", "12.b"]
        r = [ep(t, C["12.a"], 0.7), ep(t, C["12.b"], 0.7), ep(t, C["12.b"] + 3.4, 0.7)]
        sarrus(c, S3, SX - 60, SY, SCW, SCH, 1.0, 1.0, (1, 1, 1), r)
        placar(c, 1100, 230, 300, "VERDE", ["8", "5", "0"], "13", VERDE_T, 1.0)
        placar(c, 1440, 230, 300, "VERMELHO", ["60", "4", "0"], "64", VERM_T, 1.0, alfas=r,
               a_tot=ep(t, C["12.b"] + 5.5, 0.5))
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            rrect(c, 1100, 600, 640, 120, 24, mix("#FFFFFF", PURPLE, 0.08), acc)
            linha(c, [("13", VERDE_T), (" − ", INK), ("64", VERM_T), (" = ", INK), ("−51", PURPLE)], 1420, 660, 60, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            pill(c, "Sarrus SÓ vale para 3 × 3", 1420, 780, AMBER, size=28, a=ad, anchor="center")
        return
    aa = ep(t, C["13.a"], 0.5)
    ab = ep(t, C["13.b"], 0.5)
    sarrus(c, S3, SX - 60, SY, SCW, SCH, 1.0, 1.0, (1, 1, 1), (1, 1, 1), zeros=ab)
    K.atalho(c, 1080, 220, 640, 150, "ATALHO", ["placar em DUAS colunas", "passou por um ZERO? produto 0"], aa, 28)
    if aa > 0:
        placar(c, 1080, 400, 300, "VERDE", ["8", "5", "0"], "13", VERDE_T, aa)
        placar(c, 1420, 400, 300, "VERMELHO", ["60", "4", "0"], "64", VERM_T, aa)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        for x, y in ((1230, 616), (1570, 616)):
            c.drawCircle(x, y - 12, 36, paint(AMBER, acc, stroke=5))
        pill(c, "zero direto, sem conta", 1400, 770, AMBER, size=24, a=acc, anchor="center")


# ======================================================================
# bloco e — Laplace
# ======================================================================

LX, LY, LCW, LCH = 470, 500, 120, 100
SINAIS = [["+", "−", "+"], ["−", "+", "−"], ["+", "−", "+"]]


def b_laplace(c, t, C, B):
    head_seq(c, t, C, [("14", "DESENVOLVIMENTO DE LAPLACE", "UM ELEMENTO DE CADA VEZ", PURPLE),
                       ("15", "LAPLACE NA PRÁTICA", "PELA 1ª LINHA", PURPLE), ("16", "ATALHO", "A LINHA COM MAIS ZEROS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16"])
    x0, y0 = LX - 1.5 * LCW, LY - 1.5 * LCH
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        ab = ep(t, C["14.b"], 0.5)
        matriz(c, S3, LX, LY, LCW, LCH, 1.0, 50, barras=True, fundo={(0, j): (BLUE, 0.25 * aa) for j in range(3)},
               cor={(0, 0): mix(INK, PURPLE, ab)})
        riscar(c, x0, y0, LCW, LCH, 0, 0, ab)
        if aa > 0:
            text(c, "LAPLACE: escolha uma linha", 1250, 290, 32, "black", PURPLE, aa)
        if ab > 0:
            text(c, "risque a linha e a coluna do elemento", 1250, 370, 28, "black", INK2, ab)
            matriz(c, [[4, 1], [2, 1]], 1250, 500, 90, 76, ab, 40, barras=True, bcol=PURPLE)
            text(c, "COFATOR: o determinante que sobra", 1250, 620, 28, "black", PURPLE, ab)
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            gx, gy, gs = 1530, 470, 62
            for i in range(3):
                for j in range(3):
                    col = GREEN if (i + j) % 2 == 0 else RED
                    rrect(c, gx + j * gs, gy + i * gs, gs - 6, gs - 6, 10, mix("#FFFFFF", col, 0.18), acc)
                    fmid(c, SINAIS[i][j], gx + j * gs + (gs - 6) / 2, gy + i * gs + (gs - 6) / 2, 40, "black", col, acc)
            text(c, "sinais: + − + (tabuleiro)", 1250, 730, 30, "black", INK2, acc)
        return
    if sid == "15":
        matriz(c, S3, LX, LY, LCW, LCH, 1.0, 50, barras=True, fundo={(0, j): (BLUE, 0.20) for j in range(3)})
        cues = ["15.a", "15.b", "15.c"]
        termos = [[("+2 · ", INK), ("(4 − 2)", PURPLE), (" = ", INK), ("4", GREEN)],
                  [("−1 · ", INK), ("(0 − 5)", PURPLE), (" = ", INK), ("+5", GREEN)],
                  [("+3 · ", INK), ("(0 − 20)", PURPLE), (" = ", INK), ("−60", RED)]]
        cur = None
        for k, q in enumerate(cues):
            a_ = ep(t, C[q], 0.5)
            if a_ > 0:
                cur = k
                linha(c, termos[k], 960, 300 + k * 110, 46, a_, align="left")
        if cur is not None and t < C["15.d"]:
            riscar(c, x0, y0, LCW, LCH, 0, cur, 1.0)
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            rrect(c, 950, 620, 760, 130, 24, mix("#FFFFFF", PURPLE, 0.08), ad)
            linha(c, [("4 + 5 − 60 = ", INK), ("−51", PURPLE), ("  ✓", GREEN)], 1330, 685, 56, ad)
        return
    aa = ep(t, C["16.a"], 0.5)
    ab = ep(t, C["16.b"], 0.5)
    matriz(c, S3, LX, LY, LCW, LCH, 1.0, 50, barras=True, fundo={(1, j): (GREEN, 0.25 * ab) for j in range(3)},
           cor={(1, 0): mix(INK, AMBER, ab)})
    K.atalho(c, 960, 220, 720, 150, "ATALHO", ["escolha a linha com MAIS ZEROS", "zero · qualquer coisa = 0"], aa, 28)
    if ab > 0:
        linha(c, [("linha 2:  sinais  ", INK2), ("−", RED), ("  ", INK), ("+", GREEN), ("  ", INK), ("−", RED)], 1320,
              430, 40, ab)
        for j, s_ in enumerate(("−", "+", "−")):
            fmid(c, s_, x0 + (j + 0.5) * LCW + 42, y0 + 1.5 * LCH - 30, 26, "black", RED if s_ == "−" else GREEN, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        linha(c, [("−0 · (…)", GRAY), ("  +  ", INK), ("4 · (2 − 15)", PURPLE), ("  −  ", INK), ("1 · (4 − 5)", PURPLE)],
              1320, 530, 36, acc)
        linha(c, [("0", GRAY), ("  −  52  +  1", INK)], 1320, 610, 44, ep(t, C["16.c"] + 3.0, 0.5))
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        rrect(c, 1010, 670, 620, 110, 24, mix("#FFFFFF", GREEN, 0.10), ad)
        linha(c, [("= ", INK), ("−51", PURPLE), ("   uma conta a menos", GREEN)], 1320, 725, 44, ad)


# ======================================================================
# bloco f — o teste da inversa
# ======================================================================

def b_inversa(c, t, C, B):
    head_seq(c, t, C, [("17", "O TESTE DA CHAVE", "TEM INVERSA?", BLUE), ("18", "MAIS DUAS CONSEQUÊNCIAS", "DET DA INVERSA · det = 0", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["17", "18"])
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        if aa > 0:
            rrect(c, 230, 260, 700, 250, 26, mix("#FFFFFF", GREEN, 0.10), aa)
            cadeado(c, 340, 400, 80, ep(t, C["17.a"] + 1.0, 0.6), GREEN, aa)
            text(c, "det ≠ 0", 640, 360, 56, "black", GREEN, aa)
            text(c, "INVERSÍVEL: tem inversa", 640, 440, 30, "black", GREEN, aa)
        ab = ep(t, C["17.b"], 0.5)
        if ab > 0:
            rrect(c, 990, 260, 700, 250, 26, mix("#FFFFFF", RED, 0.08), ab)
            cadeado(c, 1100, 400, 80, 0, RED, ab)
            text(c, "det = 0", 1400, 360, 56, "black", RED, ab)
            text(c, "SINGULAR: não tem inversa", 1400, 440, 30, "black", RED, ab)
            a2 = ep(t, C["17.b"] + 3.0, 0.5)
            if a2 > 0:
                matriz(c, [[2, 4], [1, 2]], 1150, 640, 80, 70, a2, 36, barras=True)
                linha(c, [("2 · 2 − 4 · 1 = ", INK), ("0", RED)], 1440, 640, 40, a2)
        acc = ep(t, C["17.c"], 0.5)
        if acc > 0:
            rrect(c, 230, 560, 700, 200, 26, "#F7F7F5", acc)
            linha(c, [("A⁻¹ = ", INK), ("1 ÷ (ad − bc)", PURPLE), (" · …", INK)], 580, 620, 40, acc)
            text(c, "det = 0 → divisão IMPOSSÍVEL", 580, 720, 30, "black", RED, acc)
        return
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 260, 1460, 170, 26, mix("#FFFFFF", PURPLE, 0.08), aa)
        linha(c, [("det(A⁻¹) = 1 ÷ det A", PURPLE)], 620, 345, 52, aa)
        linha(c, [("det A = 4  →  det A⁻¹ = ", INK), ("0,25", GREEN)], 1300, 345, 40, ep(t, C["18.a"] + 3.0, 0.5))
        text(c, "porque A · A⁻¹ = I  e  det I = 1", W / 2, 470, 28, "bold", INK2, ep(t, C["18.a"] + 6.0, 0.5))
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 530, 1460, 170, 26, mix("#FFFFFF", AMBER, 0.08), ab)
        linha(c, [("x que ESTRAGAM a chave:  resolva  ", INK), ("det = 0", RED)], W / 2, 615, 46, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        pill(c, "como o 4 e o −1 do exemplo", W / 2, 760, BLUE, size=28, a=acc, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "2 × 2 E SARRUS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    ab = ep(t, C["19.b"], 0.5)
    sid = which(t, C, ["19", "20"])
    if sid == "19":
        matriz(c, NF2, 560, 430, 130, 110, aa, 54, barras=True)
        linha(c, [("= ?", PURPLE)], 740, 430, 54, aa, align="left")
        matriz(c, NF3, 1280, 430, 110, 92, ab, 46, barras=True)
        linha(c, [("= ?", PURPLE)], 1470, 430, 54, ab, align="left")
        pause_timer(c, t, C["19.end"] - 1.9, W / 2, 700)
        return
    matriz(c, NF2, 420, 360, 110, 92, 1.0, 46, barras=True,
           cor={(0, 0): BLUE, (1, 1): BLUE, (0, 1): AMBER, (1, 0): AMBER})
    a1 = ep(t, C["20.a"], 0.5)
    if a1 > 0:
        linha(c, [("(−2)(−5)", BLUE), (" − ", INK), ("(3 · 4)", AMBER)], 420, 540, 36, a1)
        linha(c, [("= 10 − 12 = ", INK), ("−2", GREEN)], 420, 610, 44, a1)
    g = [ep(t, C["20.b"] + 0.6 + k * 0.9, 0.5) for k in range(3)]
    r = [ep(t, C["20.c"] + 0.4 + k * 0.4, 0.5) for k in range(3)]
    a2 = ep(t, C["20.b"], 0.5)
    if a2 > 0:
        line(c, 760, 220, 760, 800, "#E3E6EB", a2, 3)
        sarrus(c, NF3, 1180, 370, 96, 80, a2, 1.0, g, r, size=38, zeros=ep(t, C["20.c"], 0.5))
        c.save(); c.translate(1520, 220); c.scale(0.62, 0.62)
        placar(c, 0, 0, 300, "VERDE", ["1 · 1 · 1 = 1", "2 · 3 · 2 = 12", "0 · 0 · 0 = 0"], "13", VERDE_T, a2,
               alfas=g, a_tot=ep(t, C["20.b"] + 3.5, 0.5))
        c.restore()
    acc = ep(t, C["20.c"], 0.5)
    if acc > 0:
        c.save(); c.translate(1520, 450); c.scale(0.62, 0.62)
        placar(c, 0, 0, 300, "VERMELHO", ["0", "0", "0"], "0", VERM_T, acc, alfas=r, a_tot=ep(t, C["20.c"] + 2.0, 0.5))
        c.restore()
        pill(c, "as 3 vermelhas passam por um ZERO", 1180, 600, AMBER, size=24, a=acc, anchor="center")
        linha(c, [("13 − 0 = ", INK), ("13", GREEN)], 1180, 720, 52, ep(t, C["20.c"] + 3.5, 0.5))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Ordem 2: principal menos secundária, com o sinal dentro do produto.",
          "Sarrus: some cada time e subtraia o bloco vermelho inteiro.",
          "Determinante zero: a matriz não tem inversa."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Escrever 15 − 8 em vez de 15 − (−8)", "a regra diz MENOS, e o 8 parece só um número",
          "o produto era −8: entra de casaco → 15 + 8 = 23, não 7"),
         ("Em Sarrus, subtrair só o 1º produto vermelho", "o menos aparece uma vez só, na frente do 60",
          "o menos vale para o time inteiro: some 60 + 4 + 0 = 64 e subtraia EM BLOCO"),
         ("Usar Sarrus numa 4 × 4", "a ideia das diagonais parece crescer junto com a matriz",
          "Sarrus SÓ vale para 3 × 3; numa 4 × 4, use Laplace")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24"], ERROS)


# ======================================================================
# questão do material
# ======================================================================

def _enunciado(c, linhas, a, y0=240, size=26, w=1000):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 10
        y += 6
    return y


ALTS2 = [("A", "0 e −1.", "esqueceu a secundária", RED), ("B", "−2 e 3.", "sinais trocados", RED),
         ("C", "nenhum: ela sempre tem inversa.", "", RED), ("D", "−3 e 2.", "", GREEN),
         ("E", "apenas 2.", "parou numa raiz", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · VOCÊ FAZ", "A CHAVE QUE NÃO ABRE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    _enunciado(c, [("Um sistema de criptografia só pode usar como chave uma matriz que tenha inversa. Para a matriz "
                    "abaixo, os valores reais de x que a tornam inadequada como chave são", INK)], a0, 236, 26, 1000)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
          align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS2, 1240, 250, 470, 30, C["26.ok"], "D", cues_in, cues_x, gap=22)
    am = ep(t, C["25.a"] + 3.0, 0.4)
    ab = ep(t, C["26.b"], 0.4)
    matriz(c, Q2M, 420, 470, 150, 110, am, 50, bcol=PURPLE,
           cor={(0, 0): mix(INK, BLUE, ab), (1, 1): mix(INK, BLUE, ab), (0, 1): mix(INK, AMBER, ab),
                (1, 0): mix(INK, AMBER, ab)})
    pause_timer(c, t, C["25.end"] - 1.9, 900, 600)
    if t < C["26"]:
        return
    aa = ep(t, C["26.a"], 0.4)
    if aa > 0:
        pill(c, "inadequada = sem inversa = det 0", 700, 400, RED, size=22, a=aa)
    if ab > 0:
        linha(c, [("x(x + 1)", BLUE), (" − ", INK), ("(3 · 2)", AMBER), (" = 0", INK)], 200, 620, 34, ab, align="left")
        linha(c, [("x² + x − 6 = 0", PURPLE)], 200, 680, 38, ep(t, C["26.b"] + 4.0, 0.4), align="left")
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        linha(c, [("soma −1 · produto −6 → ", INK), ("−3 e 2", GREEN)], 200, 740, 32, acc, align="left")
    ad = ep(t, C["26.d"], 0.4)
    if ad > 0:
        ftext(c, "x = 2: 2·3 − 6 = 0 ✓   x = −3: (−3)(−2) − 6 = 0 ✓", 200, 800, 24, "black", GREEN, ad, align="left")
    axc = ep(t, C["27.xc"], 0.4)
    if axc > 0:
        pill(c, "C somou o 6: x² + x + 6 = 0 não tem raiz real", 700, 470, RED, size=22, a=axc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PROPRIEDADES QUE POUPAM CONTA", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    matriz(c, PONTE, 700, 470, 130, 110, aa, 54, barras=True)
    if aa > 0:
        linha(c, [("= ?", PURPLE)], 940, 470, 70, aa, align="left")
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        cadeado(c, 1350, 470, 90, 0, AMBER, ab)
        text(c, "ZERO, sem conta nenhuma?", 1350, 640, 40, "black", AMBER, ab)
    pill(c, "ep. 2 · propriedades que poupam conta", W / 2, 790, PURPLE, size=30, a=ep(t, C["29.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Você já tinha escrito 15 − 8?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              ordem2=b_ordem2, equacao=b_equacao, sarrus=b_sarrus, laplace=b_laplace, inversa=b_inversa,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, ponte=b_ponte, cta=b_cta)
