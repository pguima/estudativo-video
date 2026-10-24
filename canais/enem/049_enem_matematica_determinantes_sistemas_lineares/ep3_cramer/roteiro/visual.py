"""Visual — Determinantes e Sistemas Lineares, Episódio 3: o sistema como A · X = B e a regra de Cramer (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho...).
Peças deste episódio: matriz() (colchetes ou barras), linha() com subscrito (D_x → D com x pequeno), troca() (a TROCA DE
FIGURINHA: a coluna das respostas entra e empurra a coluna da incógnita para fora), chao() (a fração D_x sobre D com o
D principal "no chão"), sarrus() e placar() do episódio 1.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import re
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
ARQUIVO_FINAL = "enem_matematica_determinantes_ep3_cramer.mp4"
CARD_R = K.CARD_R
VERDE_T = "#1F9D55"
VERM_T = "#D64545"

TEATRO = [[1, 1], [40, 20]]
TB = [250, 7400]
NF = [[2, 1], [1, -1]]
NFB = [7, 2]
LOJA = [[1, 1], [30, 25]]
LB = [50, 1400]
Q6 = [[1, 1, 1], [2, 1, 0], [1, 0, 2]]
Q6B = [16, 15, 14]
Q6Z = [[1, 1, 16], [2, 1, 15], [1, 0, 14]]


def sg(v):
    if isinstance(v, str):
        return v
    s = f"{abs(v):,}".replace(",", " ")
    return ("−" + s) if v < 0 else s


# ======================================================================
# peças do episódio
# ======================================================================

_SUB = re.compile(r"D_([xyz])")


def _pedacos(s):
    """separa 'D_x' em ('D', normal) + ('x', subscrito)"""
    out, i = [], 0
    for m in _SUB.finditer(s):
        if m.start() > i:
            out.append((s[i:m.start()], False))
        out.append(("D", False)); out.append((m.group(1), True))
        i = m.end()
    if i < len(s):
        out.append((s[i:], False))
    return out


def lw(partes, size, peso="black"):
    w = 0
    for s_, _ in partes:
        for p_, sub in _pedacos(s_):
            w += ftext_w(p_, peso, size * (0.62 if sub else 1.0))
    return w


def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)]; 'D_x' sai com o x subscrito"""
    if a <= 0:
        return 0
    w = lw(partes, size, peso)
    x = cx - w / 2 if align == "center" else cx
    for s_, col in partes:
        for p_, sub in _pedacos(s_):
            sz = size * (0.62 if sub else 1.0)
            dy = size * 0.18 if sub else 0
            ftext(c, p_, x, cy + size * 0.36 + dy, sz, peso, col or INK, a, align="left")
            x += ftext_w(p_, peso, sz)
    return w


def colchete(c, x, y0, y1, a, lado=1, col=INK, sw=5):
    if a <= 0:
        return
    d = 16 * lado
    p = skia.Path(); p.moveTo(x + d, y0); p.lineTo(x, y0); p.lineTo(x, y1); p.lineTo(x + d, y1)
    c.drawPath(p, paint(col, a, stroke=sw))


def matriz(c, M, cx, cy, cw, ch, a, size=None, cor=None, fundo=None, alfa=None, bcol=INK, barras=False):
    """matriz M centrada em (cx, cy); barras=True = barras do determinante. cor/alfa/fundo = {(i, j): ...}"""
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


def col_fundo(M, j, col, fa):
    return {(i, j): (col, fa) for i in range(len(M))}


def troca(c, A, B, j, cx, cy, cw, ch, a, prog, size=None, barras=True, col_b=None, col_x=None):
    """TROCA DE FIGURINHA: a coluna j de A sai (desce e some) e a coluna B entra deslizando da direita (prog 0 → 1)"""
    if a <= 0:
        return
    m, n = len(A), len(A[0])
    size = size or ch * 0.5
    col_b, col_x = col_b or GREEN, col_x or AMBER
    x0, y0 = cx - n * cw / 2, cy - m * ch / 2
    base = [[None if k == j else A[i][k] for k in range(n)] for i in range(m)]
    matriz(c, base, cx, cy, cw, ch, a, size, barras=barras)
    p1 = ease_io(min(1.0, prog * 2))           # a coluna velha sai
    p2 = ease_io(max(0.0, prog * 2 - 1))       # a nova entra
    xs = x0 + (j + 0.5) * cw
    if p1 < 1:
        rrect(c, x0 + j * cw + 4, y0 + 4 + p1 * 260, cw - 8, m * ch - 8, 14, col_x, a * 0.22 * (1 - p1))
        for i in range(m):
            fmid(c, sg(A[i][j]), xs, y0 + (i + 0.5) * ch + p1 * 260, size, "black", col_x, a * (1 - p1))
    xb = lerp(x0 + n * cw + 200, xs, p2)
    ab = a * min(1.0, prog * 3)
    if ab > 0:
        rrect(c, xb - cw / 2 + 4, y0 + 4, cw - 8, m * ch - 8, 14, col_b, ab * 0.20)
        for i in range(m):
            fmid(c, sg(B[i]), xb, y0 + (i + 0.5) * ch, size * (0.9 if len(sg(B[i])) > 3 else 1), "black", col_b, ab)


def chao(c, num, den, cx, cy, size, a, num_col=None, den_col=None, rot=1.0):
    """fração num/den com o denominador 'no chão' (faixa e rótulo CHÃO embaixo)"""
    if a <= 0:
        return
    wn, wd = lw([(num, None)], size), lw([(den, None)], size)
    w = max(wn, wd) + 30
    linha(c, [(num, num_col or PURPLE)], cx, cy - size * 0.62, size, a)
    line(c, cx - w / 2, cy, cx + w / 2, cy, INK, a, 5)
    linha(c, [(den, den_col or BLUE)], cx, cy + size * 0.62, size, a)
    if rot > 0:
        yb = cy + size * 1.25
        rrect(c, cx - w / 2 - 10, yb - 6, w + 20, 12, 6, BLUE, a * rot * 0.5)
        text(c, "CHÃO", cx, yb + 34, 22, "black", BLUE, a * rot, tracking=3)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def halo(c, s, cx, cy, size, col, a):
    if a <= 0:
        return
    w = ftext_w(s, "black", size)
    rrect(c, cx - w / 2 - 8, cy - size * 0.45, w + 16, size * 0.9, 10, "#FFFFFF", a * 0.85)
    fmid(c, s, cx, cy, size, "black", col, a)


def diag(c, x0, y0, x1, y1, col, a, prog=1.0, sw=7):
    if a <= 0 or prog <= 0:
        return
    arrow(c, x0, y0, lerp(x0, x1, prog), lerp(y0, y1, prog), col, a, sw, 18)


def sarrus(c, M, cx, cy, cw, ch, a, rep=1.0, verdes=(0, 0, 0), vermelhas=(0, 0, 0), size=None, zeros=0.0, cols=None):
    """a 3 × 3 com barras e as 2 colunas repetidas; cols = {j: cor} pinta uma coluna (a trocada)"""
    if a <= 0:
        return (0, 0)
    size = size or ch * 0.5
    x0, y0 = cx - 2.5 * cw, cy - 1.5 * ch
    for i in range(3):
        for j in range(5):
            if j >= 3 and rep <= 0:
                continue
            if zeros > 0 and M[i][j % 3] == 0:
                rrect(c, x0 + j * cw + 6, y0 + i * ch + 6, cw - 12, ch - 12, 12, AMBER, a * 0.35 * zeros)
            elif cols and (j % 3) in cols:
                rrect(c, x0 + j * cw + 6, y0 + i * ch + 6, cw - 12, ch - 12, 12, cols[j % 3], a * 0.18)
    line(c, x0 - 6, y0 - 4, x0 - 6, y0 + 3 * ch + 4, INK, a, 5)
    line(c, x0 + 3 * cw + 6, y0 - 4, x0 + 3 * cw + 6, y0 + 3 * ch + 4, INK, a, 5)
    if rep > 0:
        line(c, x0 + 3 * cw + 6, y0 - 20, x0 + 3 * cw + 6, y0 + 3 * ch + 20, GRAY, a * rep, 2, dash=(10, 8))
    e = 0.32
    for k, pg in enumerate(verdes):
        diag(c, x0 + (k + 0.5 - e) * cw, y0 + (0.5 - e) * ch, x0 + (k + 2.5 + e) * cw, y0 + (2.5 + e) * ch,
             VERDE_T, a * 0.7, pg, 5)
    for k, pg in enumerate(vermelhas):
        j = k + 2
        diag(c, x0 + (j + 0.5 + e) * cw, y0 + (0.5 - e) * ch, x0 + (j - 2 + 0.5 - e) * cw, y0 + (2.5 + e) * ch,
             VERM_T, a * 0.7, pg, 5)
    for i in range(3):
        for j in range(5):
            if j >= 3 and rep <= 0:
                continue
            aa = a if j < 3 else a * rep * 0.75
            halo(c, sg(M[i][j % 3]), x0 + (j + 0.5) * cw, y0 + (i + 0.5) * ch, size, INK if j < 3 else GRAY, aa)
    return (x0, y0)


def placar(c, x, y, w, titulo, itens, total, col, a, alfas=None, a_tot=1.0, h=300):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 54, 24, col, a * 0.16)
    text(c, titulo, x + w / 2, y + 38, 24, "black", col, a, tracking=2)
    for k, s_ in enumerate(itens):
        aa = a * (alfas[k] if alfas else 1.0)
        if aa > 0:
            ftext(c, s_, x + w / 2, y + 102 + k * 46, 30, "black", INK, aa)
    if a_tot > 0:
        line(c, x + 30, y + h - 76, x + w - 30, y + h - 76, col, a * a_tot, 3)
        ftext(c, total, x + w / 2, y + h - 26, 42, "black", col, a * a_tot)


def item_card(c, x, y, nome, preco, col, a, destaque=0.0):
    """cartão de item da lanchonete: nome e preço (? ou valor)"""
    if a <= 0:
        return
    rrect(c, x, y, 300, 300, 30, "#FFFFFF", a, shadow=True)
    if destaque > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 6, y - 6, 312, 312), 34, 34),
                    paint(col, a * destaque, stroke=8))
    rrect(c, x, y, 300, 70, 30, col, a * 0.16)
    text(c, nome, x + 150, y + 48, 32, "black", col, a, tracking=2)
    fmid(c, preco, x + 150, y + 190, 110, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DETERMINANTES · CRAMER", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    ad = ep(t, C["01.d"], 0.5)
    for k, (nome, col) in enumerate((("SUCO", GRAY), ("SANDUÍCHE", GRAY), ("SALADA", PURPLE))):
        a_ = ep(t, C["01.a"] + k * 0.5, 0.5)
        if k < 2:
            a_ *= 1 - 0.6 * ad
        item_card(c, 300 + k * 470, 290, nome, "R$ ?", col, a_, ab if k == 2 else 0)
    if ab > 0:
        pill(c, "A QUESTÃO PEDE SÓ ESTE", 300 + 2 * 470 + 150, 640, PURPLE, size=24, a=ab, anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 560, 720, 800, 120, 26, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("só 2 determinantes:  ", INK), ("D", BLUE), ("  e  ", INK), ("D_z", PURPLE)], W / 2, 780, 50, acc)
    if ad > 0:
        pill(c, "os outros preços: nem precisa", 300 + 470 // 2 + 150, 640, GRAY, size=22, a=ad, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "escrever um sistema como A · X = B", "multiplicação de matrizes"),
            ("02.b", "achar a incógnita pedida pela regra de Cramer", "e saber quando ela compensa")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "SISTEMAS", [("quantidades numa equação · ", INK), ("valores", GREEN), (" na outra", INK)], BLUE),
             ("03.b", "MATRIZES", [("multiplicar = ", INK), ("linha por coluna", PURPLE)], PURPLE),
             ("03.c", "EP. 1", [("2 × 2: principal − secundária  ·  3 × 3: ", INK), ("Sarrus", GREEN)], GREEN)]
    for k, (cue, tag, partes, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        y = 320 + k * 175 + d
        if a > 0:
            rrect(c, 240, y - 70, 1440, 140, 24, "#FFFFFF", a, shadow=True)
            pill(c, tag, 290, y, col, size=24, a=a)
            linha(c, partes, 560, y, 44, a, align="left")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "A BILHETERIA DO TEATRO", "250 INGRESSOS · R$ 7 400", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        for k, (tit, val, col) in enumerate((("INTEIRA", "R$ 40", BLUE), ("MEIA", "R$ 20", PURPLE))):
            x = 260 + k * 380
            rrect(c, x, 270, 330, 200, 26, mix("#FFFFFF", col, 0.10), aa, shadow=True)
            line(c, x + 250, 285, x + 250, 455, col, aa * 0.6, 3, dash=(10, 8))
            text(c, tit, x + 125, 330, 28, "black", col, aa, tracking=2)
            fmid(c, val, x + 125, 410, 54, "black", INK, aa)
        rrect(c, 1080, 270, 600, 200, 26, "#F2F4F7", aa)
        text(c, "VENDIDOS", 1250, 330, 24, "black", INK2, aa, tracking=2)
        fmid(c, "250", 1250, 410, 64, "black", INK, aa)
        text(c, "NO CAIXA", 1520, 330, 24, "black", INK2, aa, tracking=2)
        fmid(c, "R$ 7 400", 1520, 410, 50, "black", GREEN, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        pill(c, "o mesmo tipo da série de Sistemas · agora por OUTRO CAMINHO", W / 2, 560, PURPLE, size=28, a=ab,
             anchor="center")
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        for k, nome in enumerate(("suco", "sanduíche", "salada")):
            x = 520 + k * 300
            rrect(c, x, 650, 260, 110, 22, "#FFFFFF", acc, shadow=True)
            text(c, nome, x + 130, 718, 32, "black", INK, acc)
        text(c, "3 itens → 3 incógnitas", 1460, 718, 34, "black", PURPLE, acc, align="left")


# ======================================================================
# bloco a — forma matricial
# ======================================================================

def b_forma(c, t, C, B):
    head_seq(c, t, C, [("05", "O SISTEMA EM MATRIZES", "A, X E B", BLUE), ("06", "A · X = B", "FORMA MATRICIAL", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        linha(c, [("x + y = 250", INK)], 560, 290, 46, aa)
        linha(c, [("40x + 20y = 7 400", INK)], 1300, 290, 46, aa)
        ab = ep(t, C["05.b"], 0.5)
        acc = ep(t, C["05.c"], 0.5)
        ad = ep(t, C["05.d"], 0.5)
        matriz(c, TEATRO, 470, 560, 130, 110, ab, 54, bcol=BLUE)
        if ab > 0:
            text(c, "A", 470, 430, 48, "black", BLUE, ab)
            text(c, "MATRIZ DOS COEFICIENTES", 470, 740, 24, "black", BLUE, ab, tracking=1)
            text(c, "os números das letras", 470, 780, 24, "bold", INK2, ab)
        matriz(c, [["x"], ["y"]], 960, 560, 110, 110, acc, 54, bcol=BLUE)
        if acc > 0:
            text(c, "X", 960, 430, 48, "black", BLUE, acc)
            text(c, "COLUNA DAS INCÓGNITAS", 960, 740, 24, "black", BLUE, acc, tracking=1)
        matriz(c, [[250], [7400]], 1430, 560, 180, 110, ad, 50, bcol=GREEN)
        if ad > 0:
            text(c, "B", 1430, 430, 48, "black", GREEN, ad)
            text(c, "TERMOS INDEPENDENTES", 1430, 740, 24, "black", GREEN, ad, tracking=1)
            text(c, "as respostas", 1430, 780, 24, "bold", INK2, ad)
        return
    aa = ep(t, C["06.a"], 0.5)
    ab = ep(t, C["06.b"], 0.5)
    acc = ep(t, C["06.c"], 0.5)
    ad = ep(t, C["06.d"], 0.5)
    hl = 0 if ab > 0 and acc <= 0 else (1 if acc > 0 and ad <= 0 else -1)
    fundo = {(hl, j): (PURPLE, 0.22) for j in range(2)} if hl >= 0 else {}
    matriz(c, TEATRO, 420, 430, 120, 100, aa, 48, fundo=fundo, bcol=BLUE)
    matriz(c, [["x"], ["y"]], 690, 430, 100, 100, aa, 48, bcol=BLUE,
           fundo={(0, 0): (PURPLE, 0.22 if hl >= 0 else 0), (1, 0): (PURPLE, 0.22 if hl >= 0 else 0)})
    if aa > 0:
        fmid(c, "·", 575, 430, 60, "black", INK, aa)
        fmid(c, "=", 800, 430, 60, "black", INK, aa)
    matriz(c, [[250], [7400]], 960, 430, 170, 100, aa, 44, bcol=GREEN)
    if aa > 0:
        text(c, "FORMA MATRICIAL:  A · X = B", 690, 290, 30, "black", PURPLE, aa, tracking=1)
    if ab > 0:
        linha(c, [("1·x + 1·y = ", INK), ("250", GREEN)], 1460, 380, 44, ab)
        conferido(c, "a 1ª equação reaparece", 1250, 450, ab, True, 28)
    if acc > 0:
        linha(c, [("40·x + 20·y = ", INK), ("7 400", GREEN)], 1460, 530, 44, acc)
    if ad > 0:
        rrect(c, 260, 640, 1400, 170, 26, mix("#FFFFFF", BLUE, 0.06), ad)
        mx, mw = 560, 130
        matriz(c, [[1, 1, 250], [40, 20, 7400]], mx, 725, mw, 66, ad, 34, bcol=BLUE)
        line(c, mx - 1.5 * mw + 2 * mw, 690, mx - 1.5 * mw + 2 * mw, 760, GRAY, ad, 3, dash=(8, 6))
        text(c, "MATRIZ COMPLETA (ou AMPLIADA)", 1220, 715, 32, "black", BLUE, ad)
        text(c, "A com a coluna B ao lado", 1220, 765, 28, "bold", INK2, ad)


# ======================================================================
# bloco b — solução única
# ======================================================================

def cadeado(c, cx, cy, s, aberto, col, a):
    if a <= 0:
        return
    rrect(c, cx - s * 0.55, cy - s * 0.1, s * 1.1, s * 0.85, s * 0.14, col, a)
    c.drawCircle(cx, cy + s * 0.28, s * 0.11, paint("#FFFFFF", a))
    c.save()
    c.translate(cx + s * 0.32, cy - s * 0.1 - aberto * s * 0.25)
    c.rotate(-28 * aberto)
    p = skia.Path()
    p.moveTo(-s * 0.64, 0); p.lineTo(-s * 0.64, -s * 0.28)
    p.arcTo(skia.Rect.MakeXYWH(-s * 0.64, -s * 0.6, s * 0.64, s * 0.64), 180, 180, False)
    p.lineTo(0, 0)
    c.drawPath(p, paint(col, a, stroke=s * 0.13))
    c.restore()


def b_unica(c, t, C, B):
    head(c, t, B["start"], "SOLUÇÃO ÚNICA", "QUANDO det A ≠ 0", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 270, 700, 260, 26, mix("#FFFFFF", GREEN, 0.10), aa)
        cadeado(c, 350, 410, 80, ep(t, C["07.a"] + 1.2, 0.6), GREEN, aa)
        text(c, "det A ≠ 0", 650, 380, 54, "black", GREEN, aa)
        text(c, "A tem inversa", 650, 450, 32, "black", GREEN, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 990, 270, 700, 260, 26, mix("#FFFFFF", PURPLE, 0.08), ab)
        text(c, "SOLUÇÃO ÚNICA", 1340, 340, 28, "black", PURPLE, ab, tracking=2)
        linha(c, [("X = A⁻¹ · B", PURPLE)], 1340, 430, 60, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 230, 600, 1460, 170, 26, mix("#FFFFFF", BLUE, 0.06), acc)
        text(c, "REGRA DE CRAMER", 960, 665, 30, "black", BLUE, acc, tracking=2)
        text(c, "a mesma conta, SEM montar a inversa", 960, 730, 38, "black", INK, acc)


# ======================================================================
# bloco c — a regra
# ======================================================================

def b_regra(c, t, C, B):
    head_seq(c, t, C, [("08", "REGRA DE CRAMER", "TROCA DE FIGURINHA", PURPLE), ("09", "O MESMO PARA y E z", "O CHÃO É SEMPRE D", PURPLE),
                       ("10", "ATALHO", "A COLUNA CERTA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10"])
    AL = [["a", "b"], ["c", "d"]]
    BL = ["e", "f"]
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        ab = ep(t, C["08.b"], 0.5)
        matriz(c, AL, 420, 470, 140, 120, aa, 60, barras=True, bcol=BLUE)
        if aa > 0:
            linha(c, [("D", BLUE), (" = det A", INK)], 420, 300, 44, aa)
            text(c, "a x + b y = e", 420, 680, 30, "bold", INK2, aa)
            text(c, "c x + d y = f", 420, 720, 30, "bold", INK2, aa)
        if ab > 0:
            pr = ep(t, C["08.b"] + 1.5, 2.2)
            troca(c, AL, BL, 0, 1000, 470, 140, 120, ab, pr, 60)
            linha(c, [("D_x", PURPLE)], 1000, 300, 48, ab)
            text(c, "sai a coluna de x", 930, 690, 26, "black", AMBER, ab * ep(t, C["08.b"] + 1.5, 0.4), align="left")
            text(c, "entram as respostas", 930, 730, 26, "black", GREEN, ab * ep(t, C["08.b"] + 3.0, 0.4), align="left")
            pill(c, "TROCA DE FIGURINHA", 1000, 820, PURPLE, size=22, a=ab, anchor="center")
        acc = ep(t, C["08.c"], 0.5)
        ad = ep(t, C["08.d"], 0.5)
        if acc > 0:
            linha(c, [("x =", INK)], 1420, 470, 60, acc, align="left")
            chao(c, "D_x", "D", 1610, 470, 64, acc, rot=ad)
        return
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        matriz(c, [["a", "e"], ["c", "f"]], 450, 430, 130, 110, aa, 54, barras=True,
               fundo=col_fundo(AL, 1, GREEN, 0.22))
        if aa > 0:
            linha(c, [("D_y", PURPLE)], 450, 280, 46, aa)
            text(c, "sai a coluna de y", 450, 590, 26, "black", AMBER, aa)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            linha(c, [("y =", INK)], 720, 430, 56, ab, align="left")
            chao(c, "D_y", "D", 900, 430, 60, ab)
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            M3 = [["·", "·", "e"], ["·", "·", "f"], ["·", "·", "g"]]
            matriz(c, M3, 1350, 430, 90, 80, acc, 40, barras=True, fundo=col_fundo(M3, 2, GREEN, 0.22))
            linha(c, [("D_z", PURPLE), (": troca a 3ª coluna", INK)], 1350, 280, 36, acc)
            linha(c, [("x = ", INK), ("D_x", PURPLE), (" ÷ ", INK), ("D", BLUE), ("   y = ", INK), ("D_y", PURPLE),
                      (" ÷ ", INK), ("D", BLUE), ("   z = ", INK), ("D_z", PURPLE), (" ÷ ", INK), ("D", BLUE)],
                  W / 2, 720, 44, ep(t, C["09.c"] + 2.0, 0.5))
            pill(c, "o D principal: SEMPRE o mesmo, SEMPRE embaixo", W / 2, 810, BLUE, size=26,
                 a=ep(t, C["09.c"] + 3.5, 0.5), anchor="center")
        return
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 960, 230, 720, 150, "ATALHO", ["coluna = POSIÇÃO da incógnita", "x 1ª · y 2ª · z 3ª"], aa, 30)
    M3 = [["x", "y", "z"], ["·", "·", "·"], ["·", "·", "·"]]
    ab = ep(t, C["10.b"], 0.5)
    matriz(c, M3, 520, 540, 130, 100, aa, 48, cor={(0, 0): BLUE, (0, 1): PURPLE, (0, 2): GREEN},
           fundo=col_fundo(M3, 2, AMBER, 0.30 * ab))
    if aa > 0:
        for j, s_ in enumerate(("1ª", "2ª", "3ª")):
            text(c, s_, 520 + (j - 1) * 130, 410, 30, "black", INK2, aa)
    if ab > 0:
        linha(c, [("pediu z?  pinte a ", INK), ("3ª coluna", AMBER)], 1320, 500, 42, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("ela sai ", INK), ("INTEIRA", AMBER), (", de cima a baixo", INK)], 1320, 610, 40, acc)


# ======================================================================
# bloco d — o exemplo do teatro
# ======================================================================

def b_exemplo(c, t, C, B):
    head_seq(c, t, C, [("11", "O TEATRO POR CRAMER", "PRIMEIRO, O CHÃO", BLUE), ("12", "D DE x", "AS INTEIRAS", PURPLE),
                       ("13", "D DE y", "AS MEIAS · E A CONFERÊNCIA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        ab = ep(t, C["11.b"], 0.5)
        matriz(c, TEATRO, 480, 480, 160, 130, aa, 60, barras=True,
               cor={(0, 0): mix(INK, BLUE, ab), (1, 1): mix(INK, BLUE, ab), (0, 1): mix(INK, AMBER, ab),
                    (1, 0): mix(INK, AMBER, ab)})
        if aa > 0:
            linha(c, [("D", BLUE), (" =", INK)], 170, 480, 56, aa, align="left")
        if ab > 0:
            linha(c, [("principal: 1 · 20 = ", INK), ("20", BLUE)], 1250, 360, 44, ab)
            linha(c, [("secundária: 1 · 40 = ", INK), ("40", AMBER)], 1250, 450, 44, ep(t, C["11.b"] + 2.5, 0.5))
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            rrect(c, 960, 540, 600, 130, 24, mix("#FFFFFF", BLUE, 0.10), acc)
            linha(c, [("20 − 40 = ", INK), ("−20", BLUE)], 1260, 605, 56, acc)
            pill(c, "ESTE É O CHÃO", 1260, 720, BLUE, size=24, a=acc, anchor="center")
        return
    if t >= C["12"] and sid == "12":
        linha(c, [("D = −20", BLUE)], 1700, 250, 30, 1.0)
        aa = ep(t, C["12.a"], 0.4)
        pr = ep(t, C["12.a"] + 0.5, 3.0)
        troca(c, TEATRO, TB, 0, 480, 470, 180, 130, aa, pr, 54)
        if aa > 0:
            linha(c, [("D_x", PURPLE)], 480, 300, 50, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("250 · 20 = 5 000", INK)], 1260, 330, 40, ab)
            linha(c, [("1 · 7 400 = 7 400", INK)], 1260, 400, 40, ab)
            linha(c, [("D_x", PURPLE), (" = 5 000 − 7 400 = ", INK), ("−2 400", PURPLE)], 1260, 480, 40,
                  ep(t, C["12.b"] + 3.5, 0.5))
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            linha(c, [("x =", INK)], 980, 680, 50, acc, align="left")
            chao(c, "−2 400", "−20", 1200, 680, 50, acc, rot=0)
            linha(c, [("= ", INK), ("120", GREEN), (" inteiras", INK)], 1340, 680, 50, ep(t, C["12.c"] + 3.0, 0.5),
                  align="left")
            pill(c, "(−) ÷ (−) = +", 1260, 820, GREEN, size=26, a=ep(t, C["12.c"] + 2.0, 0.5), anchor="center")
        return
    linha(c, [("D = −20", BLUE), ("    x = 120", GREEN)], 1600, 250, 30, 1.0)
    aa = ep(t, C["13.a"], 0.5)
    matriz(c, [[1, 250], [40, 7400]], 480, 450, 180, 120, aa, 52, barras=True,
           fundo=col_fundo(TEATRO, 1, GREEN, 0.22))
    if aa > 0:
        linha(c, [("D_y", PURPLE)], 480, 300, 50, aa)
        linha(c, [("1 · 7 400 − 250 · 40 = ", INK), ("−2 600", PURPLE)], 1260, 360, 40, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("y =", INK)], 1000, 500, 46, ab, align="left")
        chao(c, "−2 600", "−20", 1210, 500, 46, ab, rot=0)
        linha(c, [("= ", INK), ("130", GREEN), (" meias", INK)], 1350, 500, 46, ep(t, C["13.b"] + 2.0, 0.5),
              align="left")
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 640, 1400, 170, 26, mix("#FFFFFF", GREEN, 0.08), acc)
        text(c, "CONFIRA NAS EQUAÇÕES ORIGINAIS", 960, 690, 24, "black", GREEN, acc, tracking=2)
        conferido(c, "120 + 130 = 250", 420, 760, acc, True, 36)
        conferido(c, "4 800 + 2 600 = 7 400", 1000, 760, ep(t, C["13.c"] + 3.5, 0.5), True, 36)


# ======================================================================
# bloco e — quando vale a pena
# ======================================================================

def b_quando(c, t, C, B):
    head(c, t, B["start"], "QUANDO CRAMER COMPENSA?", "FERRAMENTA DE PRECISÃO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    ab = ep(t, C["14.b"], 0.5)
    acc = ep(t, C["14.c"], 0.5)
    nomes = [("D", BLUE), ("D_x", PURPLE), ("D_y", PURPLE), ("D_z", PURPLE)]
    for k, (s_, col) in enumerate(nomes):
        a_ = ep(t, C["14.a"] + 0.4 * k, 0.4)
        apaga = 1 - 0.75 * ab if k in (1, 2) else 1.0
        if a_ > 0:
            x = 280 + k * 360
            rrect(c, x, 280, 300, 200, 26, "#FFFFFF", a_ * apaga, shadow=True)
            linha(c, [(s_, col)], x + 150, 360, 60, a_ * apaga)
            text(c, "Sarrus", x + 150, 450, 26, "bold", INK2, a_ * apaga)
    if aa > 0:
        text(c, "3 × 3 completo: 4 determinantes", W / 2, 540, 34, "black", INK2, aa * (1 - ab))
    if ab > 0:
        rrect(c, 260, 520, 1400, 120, 24, mix("#FFFFFF", GREEN, 0.10), ab)
        linha(c, [("pediu SÓ o z?  ", INK), ("D", BLUE), (" e ", INK), ("D_z", PURPLE), (":  2 Sarrus", GREEN)], W / 2,
              580, 44, ab)
    if acc > 0:
        rrect(c, 260, 680, 1400, 120, 24, "#F2F4F7", acc)
        linha(c, [("pediu TODAS?  substituição ou escalonamento costumam ser mais rápidos", INK)], W / 2, 740, 36, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "TRÊS CONTAS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        linha(c, [("2x + y = 7", INK)], W / 2, 330, 56, aa)
        linha(c, [("x − y = 2", INK)], W / 2, 420, 56, aa)
        linha(c, [("D = ?    ", BLUE), ("D_x", PURPLE), (" = ?    x = ?", PURPLE)], W / 2, 540, 50,
              ep(t, C["15.a"] + 3.0, 0.5))
        pause_timer(c, t, C["15.end"] - 1.9, W / 2, 720)
        return
    linha(c, [("2x + y = 7   ·   x − y = 2", INK2)], W / 2, 250, 32, 1.0)
    aa = ep(t, C["16.a"], 0.5)
    matriz(c, NF, 380, 430, 110, 100, aa, 46, barras=True,
           cor={(0, 0): BLUE, (1, 1): BLUE, (0, 1): AMBER, (1, 0): AMBER})
    if aa > 0:
        linha(c, [("D = 2·(−1) − 1·1 = ", INK), ("−3", BLUE)], 380, 590, 34, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        troca(c, NF, NFB, 0, 900, 430, 110, 100, ab, ep(t, C["16.b"] + 0.4, 1.6), 46)
        linha(c, [("D_x", PURPLE), (" = 7·(−1) − 1·2 = ", INK), ("−9", PURPLE)], 900, 590, 34,
              ep(t, C["16.b"] + 3.0, 0.5))
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        linha(c, [("x =", INK)], 1260, 430, 50, acc, align="left")
        chao(c, "−9", "−3", 1420, 430, 50, acc, rot=0)
        linha(c, [("= ", INK), ("3", GREEN)], 1500, 430, 56, ep(t, C["16.c"] + 2.0, 0.5), align="left")
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 660, 1400, 150, 26, mix("#FFFFFF", GREEN, 0.08), ad)
        linha(c, [("D_y", PURPLE), (" = 2·2 − 7·1 = −3  →  ", INK), ("y = 1", GREEN)], W / 2, 705, 38, ad)
        conferido(c, "6 + 1 = 7     3 − 1 = 2", 700, 785, ep(t, C["16.d"] + 2.5, 0.5), True, 34)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["D_x: a coluna de x sai, entra a coluna das respostas.",
          "x é D_x dividido por D: o D principal fica embaixo.",
          "Pediu uma incógnita só? Calcule só D e o dela."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        linha(c, [(s, INK)], 320, y - 6, 48, a, align="left")


ERROS = [("Trocar a LINHA de x em vez da coluna", "a gente lê a equação na horizontal",
          "no teatro, isso dá 14 550 ingressos num total de 250: o x mora numa COLUNA, é ela que sai"),
         ("Escrever x = D ÷ Dx", "o D principal parece o mais importante, e vai na frente",
          "assim x = −20 ÷ (−2 400) ≈ 0,008 ingresso: o D principal é o CHÃO, fica embaixo")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19"], ERROS)


# ======================================================================
# questão nova — camisetas e bonés (eu faço)
# ======================================================================

def _enunciado(c, linhas, a, y0=240, size=26, w=1000):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 10
        y += 6
    return y


ALTSN = [("A", "25.", "dividiu ao meio", RED), ("B", "30.", "são as camisetas", RED), ("C", "20.", "", GREEN),
         ("D", "cerca de 47.", "1 400 ÷ 30", RED), ("E", "56.", "1 400 ÷ 25", RED)]


def b_qnova(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO", "CAMISETAS E BONÉS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    resolve = ep(t, C["21"], 0.4)
    _enunciado(c, [("Uma loja vendeu, em um dia, 50 peças entre camisetas, a R$ 30,00 cada, e bonés, a R$ 25,00 cada, "
                    "arrecadando R$ 1 400,00. O número de bonés vendidos foi", INK)], a0 * (1 - resolve), 236,
               26, 1000)
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTSN, 1240, 250, 470, 30, C["21.ok"], "C", cues_in, cues_x, gap=22)
    if t < C["21"]:
        return
    linha(c, [("x camisetas · y bonés", INK2)], 190, 300, 28, resolve, align="left")
    aa = ep(t, C["21.a"], 0.4)
    linha(c, [("x + y = 50   ·   30x + 25y = 1 400", INK)], 190, 360, 32, aa, align="left")
    ab = ep(t, C["21.b"], 0.4)
    if ab > 0:
        pill(c, "pediu só y → D e D_y".replace("D_y", "Dy"), 190, 430, GREEN, size=22, a=ab)
    acc = ep(t, C["21.c"], 0.4)
    matriz(c, LOJA, 330, 590, 100, 80, acc, 40, barras=True,
           cor={(0, 0): BLUE, (1, 1): BLUE, (0, 1): AMBER, (1, 0): AMBER})
    if acc > 0:
        linha(c, [("D = 25 − 30 = ", INK), ("−5", BLUE)], 330, 720, 30, acc)
    ad = ep(t, C["21.d"], 0.4)
    if ad > 0:
        troca(c, LOJA, LB, 1, 730, 590, 110, 80, ad, ep(t, C["21.d"] + 0.4, 1.4), 38)
        linha(c, [("D_y", PURPLE), (" = 1 400 − 1 500 = ", INK), ("−100", PURPLE)], 730, 720, 30,
              ep(t, C["21.d"] + 2.5, 0.4))
    ae = ep(t, C["21.e"], 0.4)
    if ae > 0:
        linha(c, [("y = −100 ÷ (−5) = ", INK), ("20", GREEN)], 190, 790, 34, ae, align="left")
        ftext(c, "conferindo: 30 · 30 + 25 · 20 = 900 + 500 = 1 400 ✓", 190, 835, 24, "black", GREEN,
              ep(t, C["21.e"] + 3.5, 0.4), align="left")


# ======================================================================
# questão 6 — a lanchonete (nós fazemos)
# ======================================================================

ALTS6 = [("A", "3.", "o tamanho do D", RED), ("B", "4.", "é o suco", RED), ("C", "5.", "", GREEN),
         ("D", "7.", "é o sanduíche", RED), ("E", "15.", "D_z sem dividir".replace("D_z", "Dz"), RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · NÓS FAZEMOS", "SÓ O PREÇO DA SALADA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    resolve = ep(t, C["24"], 0.4)
    _enunciado(c, [("Em uma lanchonete, os preços do suco, do sanduíche e da salada são fixos. Três pedidos custaram: "
                    "1 suco, 1 sanduíche e 1 salada, R$ 16,00; 2 sucos e 1 sanduíche, R$ 15,00; 1 suco e 2 saladas, "
                    "R$ 14,00. O preço de uma salada, em reais, é", INK)], a0 * (1 - resolve), 236, 26, 1000)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 832, 18, "medium", GRAY, a0 * (1 - resolve), align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS6, 1240, 250, 470, 30, C["26.ok"], "C", cues_in, cues_x, gap=22)
    if t < C["24"]:
        return
    sid = which(t, C, ["24", "25", "26", "27"])
    if sid == "24":
        linha(c, [("suco x · sanduíche y · salada z", INK2)], 190, 290, 28, resolve, align="left")
        aa = ep(t, C["24.a"], 0.4)
        ab = ep(t, C["24.b"], 0.4)
        eqs = [[("x + y + z = 16", INK)], [("2x + y ", INK), ("+ 0z", AMBER), (" = 15", INK)],
               [("x ", INK), ("+ 0y", AMBER), (" + 2z = 14", INK)]]
        for k, e in enumerate(eqs):
            if ab <= 0:
                e = [(s_, INK) for s_, col in e if not s_.startswith("+ 0")]
            linha(c, e, 190, 360 + k * 56, 32, aa, align="left")
        acc = ep(t, C["24.c"], 0.4)
        sarrus(c, Q6, 800, 560, 84, 72, max(ab, acc), 1.0 if acc > 0 else 0.0,
               [ep(t, C["24.c"] + 0.3 * k, 0.5) for k in range(3)] if acc > 0 else (0, 0, 0),
               [ep(t, C["24.c"] + 2.0 + 0.3 * k, 0.5) for k in range(3)] if acc > 0 else (0, 0, 0), size=34,
               zeros=ab * (1 - acc * 0.5))
        if ab > 0:
            pill(c, "NÃO ESQUEÇA O ZERO", 190, 560, AMBER, size=22, a=ab)
        if acc > 0:
            linha(c, [("verde 2 − vermelho 5 → ", INK), ("D = −3", BLUE)], 190, 800, 32, ep(t, C["24.c"] + 3.5, 0.4),
                  align="left")
        return
    linha(c, [("D = −3", BLUE)], 190, 290, 30, 1.0, align="left")
    if sid == "25":
        aa = ep(t, C["25.a"], 0.4)
        sarrus(c, Q6Z, 700, 520, 96, 80, aa, 0.0, size=38, cols={2: GREEN})
        if aa > 0:
            linha(c, [("D_z", PURPLE), (": a 3ª coluna sai, entram 16, 15, 14", INK)], 190, 360, 28, aa, align="left")
        pause_timer(c, t, C["25.end"] - 1.9, 700, 780)
        return
    aa = ep(t, C["26.a"], 0.4)
    ab = ep(t, C["26.b"], 0.4)
    g = [ep(t, C["26.a"] + 0.4 * k, 0.5) for k in range(3)]
    r = [ep(t, C["26.b"] + 0.4 * k, 0.5) for k in range(3)]
    sarrus(c, Q6Z, 520, 520, 80, 68, 1.0, 1.0, g, r if ab > 0 else (0, 0, 0), size=30, cols={2: GREEN})
    c.save(); c.translate(860, 300); c.scale(0.7, 0.7)
    placar(c, 0, 0, 280, "VERDE", ["14", "15", "0"], "29", VERDE_T, aa, alfas=g, a_tot=ep(t, C["26.a"] + 2.5, 0.4))
    placar(c, 0, 330, 280, "VERMELHO", ["16", "0", "28"], "44", VERM_T, ab, alfas=r,
           a_tot=ep(t, C["26.b"] + 2.5, 0.4))
    c.restore()
    if ab > 0:
        linha(c, [("D_z", PURPLE), (" = 29 − 44 = ", INK), ("−15", PURPLE)], 190, 725, 30, ep(t, C["26.b"] + 4.0, 0.4),
              align="left")
    acc = ep(t, C["26.c"], 0.4)
    if acc > 0:
        linha(c, [("z = −15 ÷ (−3) = ", INK), ("5", GREEN)], 190, 778, 32, acc, align="left")
    ad = ep(t, C["26.d"], 0.4)
    if ad > 0:
        ftext(c, "suco 4 · sanduíche 7 · salada 5 → 16 ✓ 15 ✓ 14 ✓", 190, 830, 22, "black", GREEN, ad, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "UMA, INFINITAS OU NENHUMA", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        linha(c, [("x =", INK)], 520, 450, 64, aa, align="left")
        chao(c, "D_x", "0", 760, 450, 70, aa, den_col=RED, rot=0)
        selo(c, 760, 620, aa, "÷ 0 NÃO EXISTE", RED, -3, 28)
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        text(c, "nenhuma solução?", 1350, 400, 50, "black", INK, ab)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        text(c, "às vezes: INFINITAS", 1350, 500, 50, "black", PURPLE, acc)
    pill(c, "ep. 4 · classificar e discutir pelo determinante", W / 2, 790, PURPLE, size=30, a=ep(t, C["29.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Você já tinha usado a regra de Cramer?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, forma=b_forma, unica=b_unica,
              regra=b_regra, exemplo=b_exemplo, quando=b_quando, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              qnova=b_qnova, q6=b_q6, ponte=b_ponte, cta=b_cta)
