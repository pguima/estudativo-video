"""Visual — Comparação de Propostas e Tomada de Decisão, Episódio 5: Revisão geral, pegadinhas, treino e fechamento do bloco
de Matemática Financeira (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): bandeirinha da data focal · retas cruzando · leão do
imposto · muro de tijolinhos. Bandeira e leão no mesmo traço dos visual.py dos eps 1 e 3.
Em cada questão inédita, uma BALANÇA de duas propostas (balanca()). No fechamento do bloco, a linha do tempo com os
6 assuntos acendendo um a um (b_bloco).
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
_s = importlib.util.spec_from_file_location("comum033", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_propostas_ep5_revisao.mp4"
CARD_R = K.CARD_R
TIJOLO = "#C8643C"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def cabe(s, size, maxw, peso="black"):
    while ftw(s, size, peso) > maxw and size > 14:
        size -= 1
    return size


# ======================================================================
# peças (mesmo traço dos episódios 1–4)
# ======================================================================

def bandeira(c, x, y, a, col=None, s="DATA FOCAL", alt=150):
    """bandeirinha fincada na linha do tempo (ep1)"""
    if a <= 0:
        return
    col = col or GREEN
    line(c, x, y, x, y - alt, INK2, a, 6)
    pth = skia.Path()
    pth.moveTo(x, y - alt)
    pth.lineTo(x + 120, y - alt + 30)
    pth.lineTo(x, y - alt + 60)
    pth.close()
    c.drawPath(pth, paint(col, a))
    if s:
        pill(c, s, x, y - alt - 30, col, size=22, a=a, anchor="center", bounds=(0, 1920))


def leao(c, cx, cy, r, a, boca=0.0):
    """leão estilizado (o imposto, ep3)"""
    if a <= 0:
        return
    for k in range(14):
        ang = 2 * math.pi * k / 14
        c.drawCircle(cx + r * 0.95 * math.cos(ang), cy + r * 0.95 * math.sin(ang), r * 0.36, paint("#C8781E", a))
    c.drawCircle(cx, cy, r * 0.95, paint("#E89A2E", a))
    c.drawCircle(cx, cy + r * 0.08, r * 0.72, paint("#F6C35B", a))
    for sx in (-1, 1):
        c.drawCircle(cx + sx * r * 0.28, cy - r * 0.14, r * 0.09, paint(INK, a))
    c.drawCircle(cx, cy + r * 0.12, r * 0.11, paint("#7A3E10", a))
    hb = r * (0.10 + 0.28 * boca)
    rrect(c, cx - r * 0.30, cy + r * 0.30, r * 0.60, hb, r * 0.08, "#7A1E10", a)


def retas(c, cx, cy, a, w=300, h=200):
    """ep2: duas retas que se cruzam no ponto de equilíbrio"""
    if a <= 0:
        return
    x0, y0 = cx - w / 2, cy + h / 2
    line(c, x0, y0, x0 + w, y0, INK2, a, 4)
    line(c, x0, y0, x0, y0 - h, INK2, a, 4)
    line(c, x0 + 10, y0 - h * 0.30, x0 + w, y0 - h * 0.95, BLUE, a, 7)     # fixo baixo, variável alto
    line(c, x0 + 10, y0 - h * 0.62, x0 + w, y0 - h * 0.78, AMBER, a, 7)    # fixo alto, variável baixo
    # cruzamento
    xa, ya, xb, yb = x0 + 10, y0 - h * 0.30, x0 + w, y0 - h * 0.95
    xc, yc, xd, yd = x0 + 10, y0 - h * 0.62, x0 + w, y0 - h * 0.78
    m1 = (yb - ya) / (xb - xa); m2 = (yd - yc) / (xd - xc)
    xi = xa + (yc - ya) / (m1 - m2); yi = ya + m1 * (xi - xa)
    c.drawCircle(xi, yi, 13, paint(GREEN, a))
    c.drawCircle(xi, yi, 13, paint("#FFFFFF", a, stroke=4))


def muro(c, cx, cy, a, cheio=0.6, cols=6, rows=4, bw=52, bh=28):
    """ep4: o muro do custo fixo, feito de tijolinhos de margem (cheio = fração já construída)"""
    if a <= 0:
        return
    W_ = cols * bw
    x0, yb = cx - W_ / 2, cy + rows * bh / 2
    n = cols * rows
    feitos = int(round(n * cheio))
    k = 0
    for r_ in range(rows):
        off = (bw / 2) if r_ % 2 else 0
        for j in range(cols):
            x = x0 + j * bw + off - (bw / 2 if r_ % 2 else 0)
            y = yb - (r_ + 1) * bh
            on = k < feitos
            rrect(c, x + 2, y + 2, bw - 4, bh - 4, 4, TIJOLO if on else "#E6E6E2", a)
            if not on:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 2, y + 2, bw - 4, bh - 4), 4, 4),
                            paint(LIGHT, a, stroke=2))
            k += 1


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 bandeirinha na linha do tempo
        line(c, -150, 70, 150, 70, INK2, a, 5)
        for x in (-110, 0, 110):
            c.drawCircle(x, 70, 11, paint(INK2, a))
        bandeira(c, -110, 70, a, s="", alt=150)
    elif k == 1:    # ep2 retas cruzando
        retas(c, 0, 0, a)
    elif k == 2:    # ep3 leão
        leao(c, 0, 0, 80, a, boca=0.6)
    elif k == 3:    # ep4 muro
        muro(c, 0, 0, a, 0.62)
    c.restore()


def balanca(c, cx, cy, a, esq, dir_, pende=0, L=200):
    """balança de duas propostas: esq/dir = (rótulo, valor, cor); pende = -1 (esq. desce), 0, +1 (dir. desce)"""
    if a <= 0:
        return
    ang = math.radians(8 * pende)
    line(c, cx, cy, cx, cy + 125, INK2, a, 6)
    rrect(c, cx - 50, cy + 120, 100, 12, 6, INK2, a)
    xl, yl = cx - L * math.cos(ang), cy - L * math.sin(ang)
    xr, yr = cx + L * math.cos(ang), cy + L * math.sin(ang)
    line(c, xl, yl, xr, yr, INK2, a, 7)
    c.drawCircle(cx, cy, 10, paint(INK, a))
    for (x, y), (rot, val, col) in (((xl, yl), esq), ((xr, yr), dir_)):
        line(c, x, y, x - 70, y + 34, GRAY, a, 2)
        line(c, x, y, x + 70, y + 34, GRAY, a, 2)
        rrect(c, x - 100, y + 34, 200, 72, 14, mix("#FFFFFF", col, 0.12), a, stroke=3, stroke_color=col)
        text(c, rot, x, y + 58, cabe(rot, 18, 186, "bold"), "bold", INK2, a)
        sz = cabe(val, 28, 186)
        fmid(c, val, x, y + 84, sz, "black", col, a)


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    balanca(c, 560, 420, aa, ("PROPOSTA A", "?", BLUE), ("PROPOSTA B", "?", AMBER), 0, L=230)
    if aa > 0:
        text(c, "você no lugar de", 1360, 330, 40, "black", INK2, aa)
        text(c, "QUEM ESCOLHE", 1360, 400, 60, "black", BLUE, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        s = "o mais barato?"
        text(c, s, 1360, 520, 46, "black", INK, ab)
        w = text_w(s, "black", 46)
        strike(c, 1360 - w / 2 - 10, 505, 1360 + w / 2 + 10, 505, ab, RED, ab)
    ac = ep(t, C["01.c"], 0.5)
    chip(c, "PARA AQUELE USO", 1360, 640, GREEN, ac, 36)
    chip(c, "NA MESMA DATA", 1360, 750, PURPLE, ep(t, C["01.c"] + 0.8, 0.4), 36)


COBRA = [("02.a", "À VISTA OU A PRAZO", "o dinheiro renderia quanto?", 0, BLUE),
         ("02.b", "PLANOS", "parte fixa + variável", 1, PURPLE),
         ("02.c", "APLICAÇÕES", "imposto · períodos diferentes", 2, AMBER),
         ("02.d", "CUSTOS ESCONDIDOS", "tarifas no ato", None, RED),
         ("02.e", "EQUILÍBRIO DE UM NEGÓCIO", "quantas unidades vender", 3, GREEN)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "SEÇÃO 01", "O QUE A PROVA COBRA", BLUE)
    for k, (cue, tit, sub, ic, col) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 370
        rrect(c, x - 170, 250 + d, 340, 500, 24, mix("#F7F7F5", col, 0.08), a)
        if ic is not None:
            icone(c, ic, x, 430 + d, (0.85, 0.72, 0.9, 0.85)[ic], a)
        else:
            rrect(c, x - 115, 360 + d, 230, 140, 16, "#FFF7E0", a, shadow=True, stroke=4, stroke_color=RED)
            text(c, "taxa: 3%", x, 420 + d, 30, "black", INK2, a)
            text(c, "− tarifa", x, 470 + d, 30, "black", RED, a)
        para(c, tit, x, 610 + d, 28, "black", col, a, 310, 34, align="center")
        para(c, sub, x, 690 + d, 22, "bold", INK2, a, 310, 28, align="center")


INDICE = [("EP. 1", "data focal · taxa de oportunidade"),
          ("EP. 2", "cruzamento das retas · no empate, ninguém ganha"),
          ("EP. 3", "o que entra no bolso · o leão: só o rendimento · a tarifa encolhe"),
          ("EP. 4", "cada venda, um tijolinho · o muro do custo fixo")]
IND_CUES = ["03.a", "03.b", "04.a", "04.b"]
IND_POS = [(560, 190), (1360, 190), (560, 505), (1360, 505)]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = IND_POS[k]
        rrect(c, x - 360, y, 720, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 360, y, 720, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 330, y + 28, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x - 175, y + 160, (0.62, 0.62, 0.72, 0.62)[k], a)
        lns = s.split(" · ")
        for j, ln in enumerate(lns):
            sz = cabe(ln, 26, 330)
            if sz < 22:
                para(c, ln, x + 190, y + 150 + (j - (len(lns) - 1) / 2) * 52 - 12, 22, "black", INK if on_ else INK2, a,
                     330, 26, align="center")
            else:
                text(c, ln, x + 190, y + 150 + (j - (len(lns) - 1) / 2) * 52, sz, "black", INK if on_ else INK2, a)


ONDE = [("05.a", "FUNÇÃO AFIM", "os planos são retas", PURPLE), ("05.b", "OTIMIZAÇÃO", "série futura", BLUE),
        ("05.c", "NO DIA A DIA", "telefone · locadora · estacionamento · transporte", GREEN),
        ("05.d", "NEM TUDO É DINHEIRO", "vale o critério do enunciado", AMBER)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NA VIDA E NAS OUTRAS SÉRIES", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, sub, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 185, 260 + d, 370, 440, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 360 + d, 30, "black", INK, a, 330, 38, align="center")
        boxed(c, x - 160, 500 + d, 320, 150, col, a, 0.12)
        para(c, sub.replace(" · ", ", "), x, 560 + d, 26, "black", col, a, 290, 32, align="center")


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS", GREEN)
    cues = ("06.a", "06.b", "06.c")
    for k in range(3):
        a, d = rise(t, C[cues[k]])
        if a <= 0:
            continue
        x = 400 + k * 560
        col = (BLUE, PURPLE, GREEN)[k]
        rrect(c, x - 250, 230 + d, 500, 540, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 290 + d, a, 30, bg=col)
        if k == 0:
            for r_ in range(3):
                for j in range(3):
                    rrect(c, x - 165 + j * 112, 360 + d + r_ * 52, 104, 44, 6,
                          mix("#FFFFFF", col, 0.35 if r_ == 0 else 0.08), a)
            for j, s in enumerate(("fixo", "variável", "data")):
                text_mid(c, s, x - 113 + j * 112, 382 + d, 20, "black", col, a)
            for r_, s in enumerate(("A", "B")):
                text_mid(c, s, x - 113, 434 + d + r_ * 52, 22, "black", INK2, a)
            text(c, "MONTE A", x, 600 + d, 32, "black", col, a)
            text(c, "TABELA", x, 645 + d, 32, "black", col, a)
            text(c, "uma linha por proposta", x, 715 + d, 26, "bold", INK2, a)
        elif k == 1:
            balanca(c, x, 380 + d, a, ("A", "hoje", col), ("B", "hoje", col), 0, L=130)
            text(c, "IGUALE ANTES", x, 600 + d, 32, "black", col, a)
            text(c, "DE COMPARAR", x, 645 + d, 32, "black", col, a)
            text(c, "data · período · líquido", x, 715 + d, 26, "bold", INK2, a)
        else:
            fmid(c, "x = 601", x, 430 + d, 60, "black", INK, a)
            check_icon(c, x + 150, 425 + d, 28, a, GREEN)
            text(c, "TESTE UM VALOR", x, 600 + d, 32, "black", col, a)
            text(c, "ACIMA DO EMPATE", x, 645 + d, 32, "black", col, a)
            text(c, "a opção certa ganha?", x, 715 + d, 26, "bold", INK2, a)


# ======================================================================
# fechando o bloco (seção 10)
# ======================================================================

ASSUNTOS = ["Juros simples", "Juros compostos", "Descontos e lucro", "Taxas e inflação", "Empréstimos", "Decisões"]
ETAPAS = [("07.a", "CRESCIMENTO", (0, 1), BLUE), ("07.b", "VARIAÇÕES", (2,), AMBER), ("07.c", "TAXAS", (3,), PURPLE),
          ("07.d", "DÍVIDAS", (4,), RED), ("07.e", "DECISÕES", (5,), GREEN)]


def b_bloco(c, t, C, B):
    frame(c, t, B["start"], "FECHANDO O BLOCO", "MATEMÁTICA FINANCEIRA: 6 ASSUNTOS", PURPLE)
    a0 = ep(t, B["start"], 0.5)
    x0, x1, y = 260, 1660, 500
    passo = (x1 - x0) / 5
    line(c, x0 - 60, y, x1 + 60, y, LIGHT, a0, 8)
    acesos = {}
    for cue, et, nos, col in ETAPAS:
        ae = ep(t, C[cue], 0.5)
        for n in nos:
            acesos[n] = (ae, col)
        if ae > 0:
            xs = [x0 + n * passo for n in nos]
            xm = sum(xs) / len(xs)
            pill(c, et, xm, 330, col, size=24, a=ae, anchor="center", bounds=(0, 1920))
            if len(xs) > 1:
                line(c, xs[0], 380, xs[-1], 380, col, ae, 5)
            for xx in xs:
                line(c, xx, 380, xx, y - 30, col, ae * 0.6, 3)
    for n, s in enumerate(ASSUNTOS):
        x = x0 + n * passo
        ae, col = acesos.get(n, (0, INK2))
        c.drawCircle(x, y, 26, paint(mix("#E6E6E2", col, ae), a0))
        if ae > 0.5:
            check_icon(c, x, y, 14, ae, "#FFFFFF")
        badge = f"{13 + n}"
        text(c, badge, x, y + 70, 22, "black", GRAY, a0)
        para(c, s, x, y + 110, 26, "black", INK if ae > 0.5 else INK2, a0, 230, 32, align="center")
    ae = ep(t, C["07.e"] + 0.6, 0.5)
    pill(c, "você está aqui", x0 + 5 * passo, 700, GREEN, size=24, a=ae, anchor="center", bounds=(0, 1920))


FATORES = [("08.a", "+ 20%", "× 1,2", AMBER), ("08.b", "− 20%", "× 0,8", AMBER), ("08.c", "2 períodos a 10%", "× 1,21", BLUE),
           ("08.d", "tirar a inflação", "÷ fator", PURPLE), ("08.e", "parcela para hoje", "÷ fator do prazo", PURPLE)]


def b_fatores(c, t, C, B):
    frame(c, t, B["start"], "A IDEIA QUE ATRAVESSA O BLOCO", "FATORES E DATAS", PURPLE)
    a0 = ep(t, C["08"], 0.5)
    if a0 > 0:
        boxed(c, 260, 200, 1400, 110, PURPLE, a0, 0.10)
        text_mid(c, "trabalhe com FATORES e respeite as DATAS", W / 2, 255, 44, "black", PURPLE, a0)
    for k, (cue, de, fat, col) in enumerate(FATORES):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        r_, j = divmod(k, 3)
        x = 420 + j * 540 if r_ == 0 else 690 + j * 540
        y = 400 + r_ * 190 + d
        rrect(c, x - 240, y, 480, 150, 20, mix("#F7F7F5", col, 0.08), a)
        text(c, de, x, y + 52, 30, "bold", INK2, a)
        fmid(c, fat, x, y + 106, cabe(fat, 50, 440), "black", col, a)
    af = ep(t, C["08.f"], 0.5)
    if af > 0:
        selo(c, 420, 805, af, "PEGADINHA", AMBER, -5, 30)
        text(c, "somar o que se multiplica · misturar datas", 1060, 818, 34, "black", RED, af)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["09"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["09.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["09.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["09.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("datas diferentes", "a 10% a.a.: R$ 5.500 em 1 ano > R$ 5.000 hoje", False, "5.500 é mais",
     "leve à mesma data", "5.500 ÷ 1,1 = 5.000 · empatam", 0),
    ("o maior número", "a 10% a.a.: R$ 8.000 hoje > R$ 8.600 em 1 ano", True, "8.600 é o maior número",
     "o maior número estava mais longe", "8.000 × 1,1 = 8.800", 0),
    ("planos", "mensalidade menor = sempre mais barato", False, "é o primeiro número que você vê",
     "depende do uso: ache o equilíbrio", "depende do consumo", 1),
    ("equilíbrio", "40 + 0,30x × 70 + 0,10x → 30 ÷ 0,30 = 100 min", False, "30 é a diferença dos fixos",
     "divida pela diferença dos preços", "30 ÷ 0,20 = 150 min", 1),
    ("“a partir de”", "empate em 37,5 km → a partir de 38 km", True, "37,5 arredondaria para baixo",
     "“a partir de” é o inteiro seguinte", "38 km", 1),
    ("imposto", "R$ 2.000 a 10%, IR de 15% → imposto R$ 330", False, "15% do total dá isso",
     "o leão morde só o rendimento", "15% × 200 = R$ 30", 2),
    ("taxas", "2% ao mês > 25% ao ano", True, "2 × 12 = 24",
     "converta por fator", "1,02¹² ≈ 1,268 → 26,8%", 2),
    ("tarifa no ato", "R$ 4.000 a 3% + tarifa R$ 80 → custo 3%", False, "3% é a taxa anunciada",
     "divida pelo que você recebe", "200 ÷ 3.920 ≈ 5,1%", 2),
    ("negócio", "fixo 3.000 · custo 10 · preço 25 → 3.000 ÷ 25 = 120", False, "o preço entra no caixa",
     "divida pela margem: 25 − 10 = 15", "3.000 ÷ 15 = 200", 3),
]
VF_IDS = [f"{10 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 420, 0.62, a0)
    text(c, ctx.upper(), 980, 310, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = cabe(conta, 48, 820)
    fmid(c, conta, 980, 410, sz, "black", INK, a0)
    if ar > 0 and not ver:
        w = ftw(conta, sz)
        strike(c, 980 - w / 2 - 10, 415, 980 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1660, 410, a=1 - ar)
    selo(c, 1640, 470, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 560, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 560, ae, "PEGADINHA", AMBER, -5, 30)
        text(c, engana, 640 if ver else 520, 572, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 640, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 710, 30, "black", GREEN, ag, 760)
        fmid(c, fix, 1340, 725, cabe(fix, 42, 600), "black", GREEN, ag)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["19.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["19.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["19.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    text(c, "monte a tabela antes da conta", W / 2, 740, 32, "black", PURPLE, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · bal: (esq, dir, pende) · passos: (cue, texto) · confere: (cue, texto)
# fora: motivos das erradas à direita da lista (alternativas longas)

Q = {
    "q1": dict(ids=("20", "21"), titulo="À VISTA OU A PRAZO?", ok="A", asz=26, aw=560,
               enun=[("a", "Uma geladeira custa R$ 1.940,00 à vista ou 2 × R$ 1.000,00 (no ato e em 30 dias). O "
                      "dinheiro do comprador rende 2% ao mês. Considere 1/1,02 ≈ 0,980.", False),
                     ("b", "A melhor decisão é", True)],
               alts=[("A", "À vista: o parcelado vale hoje ≈ R$ 1.980,00, mais que R$ 1.940,00.", "", GREEN),
                     ("B", "Parcelar: o total a prazo tem só R$ 60,00 a mais.", "", RED),
                     ("C", "À vista: a taxa do parcelamento é de 3% ao mês.", "", AMBER),
                     ("D", "Tanto faz: as duas opções se equivalem.", "", AMBER),
                     ("E", "Parcelar: o dinheiro aplicado rende 2% ao mês.", "", RED)],
               fora={"B": ("datas diferentes", RED), "C": ("dividiu por 2.000", AMBER), "D": ("sem conta", AMBER),
                     "E": ("não comparou com a loja", RED)},
               bal=(("À VISTA", "R$ 1.940", BLUE), ("PARCELADO HOJE", "≈ R$ 1.980", AMBER), 1),
               passos=[("d", "1ª parcela: no ato, não viaja"), ("a", "2ª: 1.000 × 0,980 = 980"),
                       ("b", "1.980 > 1.940 → à vista")],
               confere=("v", "taxa: 60 ÷ 940 ≈ 6,4% > 2%")),
    "q2": dict(ids=("22", "23"), titulo="A LÂMPADA QUE SE PAGA", ok="C", asz=34,
               enun=[("a", "Uma lâmpada LED custa R$ 30,00 e gasta R$ 0,01 de energia por hora. Uma comum custa "
                      "R$ 6,00 e gasta R$ 0,05 por hora.", False),
                     ("b", "O número mínimo de horas inteiras de uso para que a LED fique mais barata é", True)],
               alts=[("A", "480 h", "24 ÷ 0,05", AMBER), ("B", "600 h", "é o empate", RED), ("C", "601 h", "", GREEN),
                     ("D", "900 h", "somou os preços", RED), ("E", "2.400 h", "24 ÷ 0,01", AMBER)],
               bal=(("LED", "30 + 0,01h", GREEN), ("COMUM", "6 + 0,05h", AMBER), 0),
               passos=[("d", "fixos: 30 − 6 = 24 · por hora: 0,04"), ("a", "24 ÷ 0,04 = 600 h (R$ 36 = R$ 36)"),
                       ("b", "empate não vale → 601 h")],
               confere=("v", "601 h: LED 36,01 · comum 36,05")),
    "q3": dict(ids=("24", "25"), titulo="QUAL APLICAÇÃO RENDE MAIS?", ok="E", asz=28, aw=560,
               enun=[("a", "A aplicação A rende 1% ao mês, com 20% de imposto sobre o rendimento. A aplicação B rende "
                      "10,5% ao ano, isenta. Prazo: 1 ano. Considere 1,01¹² ≈ 1,127.", False),
                     ("b", "Rende mais", True)],
               alts=[("A", "A, com 12,7% ao ano.", "", RED), ("B", "A, com 12% ao ano.", "", RED),
                     ("C", "B, porque aplicação isenta sempre rende mais.", "", AMBER),
                     ("D", "As duas rendem o mesmo.", "", AMBER),
                     ("E", "B, com 10,5% contra ≈ 10,2% da A.", "", GREEN)],
               fora={"A": ("esqueceu o imposto", RED), "B": ("taxa proporcional", RED), "C": ("motivo falso", AMBER),
                     "D": ("não igualou", AMBER)},
               bal=(("A LÍQUIDA", "≈ 10,2%", BLUE), ("B ISENTA", "10,5%", GREEN), 1),
               passos=[("d", "mesmo período e líquido"), ("a", "A: 1,01¹² ≈ 1,127 → 12,7% bruto"),
                       ("b", "12,7% × 0,8 ≈ 10,2% < 10,5% → B")],
               confere=None),
    "q4": dict(ids=("26", "27"), titulo="O CUSTO EFETIVO", ok="D", asz=34,
               enun=[("a", "Um empréstimo de R$ 10.000,00 por 1 mês, a 3%, tem tarifa de R$ 200,00 e seguro de "
                      "R$ 100,00 descontados no ato.", False), ("b", "O custo efetivo é de, aproximadamente,", True)],
               alts=[("A", "3%", "o anunciado", RED), ("B", "3,1%", "300 ÷ 9.700", AMBER), ("C", "6%", "÷ 10.000", AMBER),
                     ("D", "6,2%", "", GREEN), ("E", "9%", "3% + 6%", RED)],
               bal=(("RECEBE", "R$ 9.700", BLUE), ("PAGA", "R$ 10.300", RED), 1),
               passos=[("d", "recebe: 10.000 − 300 = 9.700"), ("a", "paga: 10.000 × 1,03 = 10.300"),
                       ("b", "600 ÷ 9.700 ≈ 6,2%")],
               confere=None),
    "q5": dict(ids=("28", "29"), titulo="O MÍNIMO PARA TER LUCRO", ok="C", asz=34,
               enun=[("a", "Uma oficina tem custo fixo de R$ 5.000,00 por mês. Cada peça custa R$ 12,00 para ser feita "
                      "e é vendida por R$ 30,00.", False),
                     ("b", "Para ter lucro, o mínimo de peças vendidas no mês é", True)],
               alts=[("A", "167", "÷ 30 (o preço)", RED), ("B", "277", "arredondou p/ baixo", AMBER),
                     ("C", "278", "", GREEN), ("D", "300", "“a centena”", AMBER), ("E", "417", "÷ 12 (o custo)", RED)],
               bal=(("CUSTO FIXO", "R$ 5.000", RED), ("278 × R$ 18", "R$ 5.004", GREEN), 1),
               passos=[("d", "margem: 30 − 12 = 18"), ("a", "5.000 ÷ 18 ≈ 277,8"),
                       ("b", "277 × 18 = 4.986 < 5.000 → 278")],
               confere=None),
}


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · INÉDITA", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        aw = d.get("aw", 820)
        K.alternativas(c, t, C, d["alts"], 880, 230, aw, d["asz"], C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if d.get("fora"):   # motivos fora da lista, à direita (alternativas longas)
            yy_ = 230
            for L, s_, _, _ in d["alts"]:
                hh = len(K.wrap(s_, "bold", d["asz"], aw - 70)) * (d["asz"] + 8) + 10
                if L in d["fora"]:
                    why, colw = d["fora"][L]
                    pill(c, why, 1470, yy_ + hh / 2, colw, size=20, a=ep(t, cues_x[L], 0.4), bounds=(0, 1920))
                yy_ += hh + 14
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            if ad > 0:
                boxed(c, 160, 230, 670, 200, PURPLE, ad, 0.05)
                esq, dir_, pende = d["bal"]
                balanca(c, 495, 268, ad, esq, dir_, pende * ep(t, C[f"{s2}.b"], 0.6), L=185)
            yy = 480
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                ftext(c, s, 180, yy, cabe(s, 34, 640), "black", GREEN if last else INK, a, align="left")
                yy += 62
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, s, 190, yy + 6, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 760, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("30.b", "EP. 1", ["data focal", "taxa de oportunidade", "à vista × a prazo"]),
         ("30.c", "EP. 2", ["custo = fixo + variável", "ponto de equilíbrio", "“a partir de”: o inteiro seguinte"]),
         ("31.a", "EP. 3", ["taxas no mesmo período", "imposto só no rendimento", "custo efetivo com tarifa"]),
         ("31.b", "EP. 4", ["equilíbrio de um negócio", "meta de lucro"]),
         ("31.c", "BLOCO", ["fatores multiplicam, datas se respeitam", "simulado dos 6 assuntos"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["30.a"], 0.5) * (1 - ep(t, C["30.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 3 else 1
        x = 150 if col_ == 0 else 990
        y0 = 190 + sum(len(CHECK[j][2]) * 46 + 34 for j in range(0 if col_ == 0 else 3, k))
        pill(c, ep_, x, y0 + 18, PURPLE if ep_ != "BLOCO" else GREEN, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 46
            rrect(c, x + 120, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            K.ftext(c, it, x + 168, yy + 10, cabe(it, 27, 640, "bold"), "bold", INK, a, align="left")
    ae = ep(t, C["31.d"], 0.5)
    if ae > 0:
        boxed(c, 990, 690, 720, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1350, 740, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["32.a"], 0.5)
    ab = ep(t, C["32.b"], 0.5)
    for i in range(20):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["32.a"] + 0.04 * i, 0.2)
        ok = ab > 0 and i < 14
        x, y = 230 + k * 82, 240 + r_ * 86
        rrect(c, x, y, 66, 70, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "20 questões", 1450, 290, 52, "black", INK, aa)
    text(c, "14 acertos = 70%", 1450, 380, 46, "black", GREEN, ab)
    text(c, "priorize planos e à vista × a prazo", W / 2, 470, 30, "bold", INK2, ab)
    ac = ep(t, C["32.c"], 0.5)
    if ac > 0:
        boxed(c, 230, 530, 1460, 240, PURPLE, ac, 0.08)
        text_mid(c, "SIMULADO DO BLOCO", W / 2, 580, 40, "black", PURPLE, ac)
        text_mid(c, "20 questões · os 6 assuntos misturados", W / 2, 640, 32, "bold", INK, ac)
        for n, s in enumerate(ASSUNTOS):
            chip(c, s, 340 + n * 248, 720, (BLUE, BLUE, AMBER, PURPLE, RED, GREEN)[n], ep(t, C["32.c"] + 0.15 * n, 0.3),
                 20)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "MATEMÁTICA FINANCEIRA COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    chip(c, "MATEMÁTICA FINANCEIRA ✓", W / 2, 230, GREEN, aa, 34)
    ab = ep(t, C["33.b"], 0.5)
    text(c, "Expressões algébricas", W / 2, 350, 58, "black", PURPLE, ab)
    text(c, "e produtos notáveis", W / 2, 420, 46, "black", PURPLE, ab)
    pill(c, "abre o bloco de Álgebra", W / 2, 490, BLUE, size=28, a=ab, anchor="center")
    ac = ep(t, C["33.c"], 0.5)
    if ac > 0:
        boxed(c, 300, 560, 600, 150, AMBER, ac, 0.10)
        text_mid(c, "TÁXI", 600, 600, 26, "black", AMBER, ac)
        text_mid(c, "R$ 6,00 + R$ 2,50 por km", 600, 660, 34, "black", INK, ac)
    ad = ep(t, C["33.d"], 0.5)
    if ad > 0:
        arrow(c, 920, 635, 1010, 635, PURPLE, ad, 5, 16)
        boxed(c, 1030, 560, 590, 150, PURPLE, ad, 0.12)
        fmid(c, "6 + 2,5x", 1325, 635, 72, "black", PURPLE, ad)
    ae = ep(t, C["33.e"], 0.5)
    text(c, "letras no lugar de números: uma regra para qualquer distância", W / 2, 790, 30, "bold", INK2, ae)


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos, bloco=b_bloco,
              fatores=b_fatores, vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"),
              q2=faz_questao("q2"), q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"),
              checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
