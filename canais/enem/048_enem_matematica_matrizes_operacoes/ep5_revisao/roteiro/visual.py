"""Visual — Matrizes e Operações, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): poltrona de cinema · folhas transparentes · cupom de
supermercado · cadeado.
Ícones de área (area_icone()): tabela · pixels · moeda · prato · mapa · sistema A·X = B · placar · dominó.
Matrizes na tela: matriz() (colchetes e casas acesas) e expr() (linha com textos e matrizes lado a lado).
Cores com função: azul = definição · roxo = regra, fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum048", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_matrizes_ep5_revisao.mp4"
CARD_R = K.CARD_R


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra '2 × 3', '24 g', '25 questões' nem 'R$ 30'"""
    s = re.sub(r"(?<=\d) × (?=\d)", " × ", s)
    s = re.sub(r"(?<=\$) (?=\d)", " ", s)
    s = re.sub(r"(?<=\d) (?=(g|questões|acertos)\b)", " ", s)
    return s


def fit(c, s, x, y, size, maxw, peso, col, a, align="left"):
    """texto numa linha só (ftext), encolhendo até caber em maxw"""
    s = nb(s)
    while ftw(s, size, peso) > maxw and size > 18:
        size -= 1
    ftext(c, s, x, y, size, peso, col, a, align=align)
    return size


def _quebra(s, size, maxw, peso="black"):
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and ftw(tst, size, peso) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    return out + ([cur] if cur else [])


def para_nb(c, s, x, y, size, peso, color, a, maxw, lh=None, align="left"):
    """quebra de linha (ftext) que respeita os espaços rígidos de nb()"""
    s = nb(s)
    lh = lh or size * 1.32
    out = _quebra(s, size, maxw, peso)
    if a > 0:
        for k, ln in enumerate(out):
            ftext(c, ln, x, y + k * lh, size, peso, color, a, align=align)
    return len(out) * lh


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def sub(c, base, s, cx, cy, size, col, a, align="center"):
    """base com subscrito (c + ij), centrado em (cx, cy)"""
    if a <= 0:
        return
    wb, ws = ftw(base, size), ftw(s, size * 0.55)
    x = cx - (wb + ws) / 2 if align == "center" else cx
    ftext(c, base, x, cy + size * 0.36, size, "black", col, a, align="left")
    ftext(c, s, x + wb + 2, cy + size * 0.62, size * 0.55, "black", col, a, align="left")


# ======================================================================
# matrizes na tela
# ======================================================================

def mat_wh(vals, cw, ch):
    return len(vals[0]) * cw + 40, len(vals) * ch + 20


def matriz(c, cx, cy, vals, a, cw=90, ch=70, size=40, cores=None, hi=None, hi_col=None, br=None):
    """matriz centrada em (cx, cy): vals = linhas de strings; hi = casas acesas {(i, j)}; devolve (w, h)"""
    w, h = mat_wh(vals, cw, ch)
    if a <= 0:
        return w, h
    x0, y0 = cx - w / 2, cy - h / 2
    bcol = br or INK
    for xx, sg in ((x0, 1), (x0 + w, -1)):
        line(c, xx, y0, xx, y0 + h, bcol, a, 4)
        line(c, xx, y0, xx + 14 * sg, y0, bcol, a, 4)
        line(c, xx, y0 + h, xx + 14 * sg, y0 + h, bcol, a, 4)
    for i, row in enumerate(vals):
        for j, s_ in enumerate(row):
            ccx = x0 + 20 + cw * (j + 0.5)
            ccy = y0 + 10 + ch * (i + 0.5)
            if hi and (i, j) in hi:
                rrect(c, ccx - cw / 2 + 4, ccy - ch / 2 + 4, cw - 8, ch - 8, 10, mix("#FFFFFF", hi_col or AMBER, 0.35), a)
            sz = size if ftw(s_, size) < cw - 10 else size * (cw - 10) / ftw(s_, size)
            ftext(c, s_, ccx, ccy + sz * 0.36, sz, "black", (cores or {}).get((i, j), INK), a)
    return w, h


def M(*linhas):
    """M('1 0', '2 1') → [['1', '0'], ['2', '1']] (o '-' vira '−')"""
    return [[v.replace("-", "−") for v in ln.split()] for ln in linhas]


def expr_w(items, size, cw, ch):
    tot = 0
    for it in items:
        tot += (mat_wh(it, cw, ch)[0] if isinstance(it, list) else ftw(nb(it), size)) + 18
    return tot - 18


def expr(c, items, cx, cy, a, size=40, cw=64, ch=52, col=INK, msize=None, maxw=None):
    """linha centrada em (cx, cy) com textos e matrizes; encolhe até caber em maxw; devolve a largura"""
    while maxw and expr_w(items, size, cw, ch) > maxw and size > 22:
        size -= 2; cw *= 0.94; ch *= 0.94
    w = expr_w(items, size, cw, ch)
    if a <= 0:
        return w
    x = cx - w / 2
    for it in items:
        if isinstance(it, list):
            mw, _ = mat_wh(it, cw, ch)
            matriz(c, x + mw / 2, cy, it, a, cw, ch, msize or size * 0.85, cores={(i, j): col for i in range(len(it))
                                                                                  for j in range(len(it[0]))})
            x += mw + 18
        else:
            s = nb(it)
            ftext(c, s, x, cy + size * 0.36, size, "black", col, a, align="left")
            x += ftw(s, size) + 18
    return w


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def poltrona_ic(c, a):
    """ep1: o assento do cinema (fileira 2, poltrona 3)"""
    for f in range(3):
        for p in range(4):
            on = (f, p) == (1, 2)
            x, y = -170 + p * 90, -120 + f * 90
            rrect(c, x, y, 70, 46, 12, AMBER if on else mix("#FFFFFF", INK2, 0.35), a)
            rrect(c, x + 6, y + 46, 58, 22, 8, mix(AMBER, INK, 0.25) if on else mix("#FFFFFF", INK2, 0.55), a)
    ftext(c, "a₂₃", 0, 190, 60, "black", BLUE, a, align="center")


def folhas_ic(c, a):
    """ep2: as folhas transparentes da soma"""
    for k, col in enumerate((BLUE, GREEN)):
        x, y = -170 + k * 70, -130 + k * 60
        rrect(c, x, y, 260, 200, 18, mix("#FFFFFF", col, 0.25), a * 0.85, stroke=5, stroke_color=col)
        for i in range(1, 3):
            line(c, x + 15, y + i * 66, x + 245, y + i * 66, mix("#FFFFFF", col, 0.6), a, 3)
        line(c, x + 130, y + 15, x + 130, y + 185, mix("#FFFFFF", col, 0.6), a, 3)
    ftext(c, "+", 170, -90, 80, "black", PURPLE, a, align="center")


def cupom_ic(c, a):
    """ep3: o cupom do caixa do supermercado (linha vezes coluna)"""
    p = skia.Path(); p.moveTo(-130, -170); p.lineTo(130, -170); p.lineTo(130, 150)
    for k in range(8):
        p.lineTo(130 - 32.5 * (k + 0.5), 170 if k % 2 == 0 else 150)
    p.lineTo(-130, 150); p.close()
    c.drawPath(p, paint("#FFFFFF", a)); c.drawPath(p, paint(INK2, a, stroke=4))
    for k, s in enumerate(("2 × 5", "3 × 4", "1 × 6")):
        ftext(c, s, -95, -105 + k * 62, 40, "black", INK, a, align="left")
    line(c, -100, 85, 100, 85, INK2, a, 3)
    ftext(c, "= 28", 95, 135, 44, "black", GREEN, a, align="right")


def cadeado_ic(c, a):
    """ep4: o cadeado e a chave (a inversa)"""
    c.drawArc(skia.Rect.MakeXYWH(-90, -170, 180, 190), 180, 180, False, paint(INK2, a, stroke=24))
    line(c, -90, -75, -90, -20, INK2, a, 24); line(c, 90, -75, 90, -20, INK2, a, 24)
    rrect(c, -140, -30, 280, 200, 26, AMBER, a, shadow=True)
    c.drawCircle(0, 50, 26, paint(INK, a)); rrect(c, -10, 60, 20, 60, 8, INK, a)
    c.drawCircle(200, 150, 34, paint(GREEN, a, stroke=12))
    line(c, 200, 184, 200, 280, GREEN, a, 14)
    line(c, 200, 240, 236, 240, GREEN, a, 12); line(c, 200, 268, 228, 268, GREEN, a, 12)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (poltrona_ic, folhas_ic, cupom_ic, cadeado_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def tabela_ic(c, a):
    rrect(c, -170, -140, 340, 280, 18, "#FFFFFF", a, shadow=True)
    rrect(c, -170, -140, 340, 64, 18, BLUE, a)
    for i in range(1, 4):
        line(c, -150, -76 + i * 52, 150, -76 + i * 52, LIGHT, a, 3)
    for j in (-55, 55):
        line(c, j, -66, j, 125, LIGHT, a, 3)


def pixels_ic(c, a):
    P = ["01110", "10001", "10101", "10001", "01110"]
    for i, ln in enumerate(P):
        for j, v in enumerate(ln):
            rrect(c, -150 + j * 60, -150 + i * 60, 54, 54, 6, INK if v == "1" else "#FFFFFF", a, stroke=2,
                  stroke_color=LIGHT)


def moeda_ic(c, a):
    c.drawCircle(0, 0, 140, paint(AMBER, a))
    c.drawCircle(0, 0, 112, paint(mix(AMBER, INK, 0.25), a, stroke=8))
    ftext(c, "R$", 0, 26, 86, "black", "#FFFFFF", a, align="center")


def prato_ic(c, a):
    c.drawCircle(0, 0, 150, paint("#FFFFFF", a)); c.drawCircle(0, 0, 150, paint(INK2, a, stroke=6))
    c.drawCircle(0, 0, 105, paint(LIGHT, a, stroke=4))
    for x, y, col in ((-40, -30, "#F2EFE6"), (40, 20, mix(INK, AMBER, 0.45))):
        c.drawCircle(x, y, 55, paint(col, a))


def mapa_ic(c, a):
    pts = [(-130, 90), (0, -110), (140, 60)]
    for (x1, y1), (x2, y2) in ((pts[0], pts[1]), (pts[1], pts[2]), (pts[0], pts[2])):
        line(c, x1, y1, x2, y2, INK2, a, 6)
    for x, y in pts:
        c.drawCircle(x, y, 32, paint(BLUE, a))
    ftext(c, "120", -100, -20, 34, "black", INK, a, align="center")


def sistema_ic(c, a):
    rrect(c, -190, -90, 380, 180, 30, mix("#FFFFFF", PURPLE, 0.18), a, shadow=True)
    ftext(c, "A · X = B", 0, 22, 66, "black", PURPLE, a, align="center")


def placar_ic(c, a):
    rrect(c, -180, -100, 360, 200, 24, INK, a, shadow=True)
    ftext(c, "3 × 1", 0, 30, 84, "black", "#FFFFFF", a, align="center")


def domino_ic(c, a):
    for k, (s1, s2) in enumerate((("2", "3"), ("3", "2"))):
        x = -200 + k * 210
        rrect(c, x, -70, 190, 120, 18, "#FFFFFF", a, shadow=True, stroke=4, stroke_color=INK2)
        line(c, x + 95, -60, x + 95, 40, INK2, a, 4)
        ftext(c, s1, x + 48, 12, 56, "black", INK if k == 0 else GREEN, a, align="center")
        ftext(c, s2, x + 142, 12, 56, "black", GREEN if k == 0 else INK, a, align="center")
    arrow(c, -12, 95, -12, 60, GREEN, a, 5, 12)
    ftext(c, "encaixa", -12, 140, 34, "black", GREEN, a, align="center")


AREA_F = (tabela_ic, pixels_ic, moeda_ic, prato_ic, mapa_ic, sistema_ic, placar_ic, domino_ic, cadeado_ic, cupom_ic)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    for k, (s, ic, col) in enumerate((("tabela de jogos", 6, BLUE), ("distâncias", 4, GREEN),
                                       ("compras", 9, AMBER), ("foto digital", 1, PURPLE))):
        a, d = rise(t, C["01.b"] + 0.6 * k)
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 210 + d, 380, 270, 26, mix("#F7F7F5", col, 0.12), a)
        area_icone(c, ic, x, 320 + d, 0.40, a)
        fit(c, s, x, 445 + d, 32, 340, "black", col, a, align="center")
    aa = ep(t, C["01.a"], 0.5) * (1 - ep(t, C["01.b"], 0.4))
    if aa > 0:
        rrect(c, 460, 380, 1000, 140, 30, "#FFFFFF", aa, shadow=True)
        text_mid(c, "a matriz quase nunca vem com o nome", W / 2, 450, 44, "black", INK, aa)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        rrect(c, 410, 540, 1100, 110, 55, mix("#FFFFFF", PURPLE, 0.20), ac, shadow=True)
        text_mid(c, "reconheça o disfarce", W / 2, 595, 54, "black", PURPLE, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "9 V OU F", 640, 790, AMBER, ad, 30)
        chip(c, "5 QUESTÕES NOVAS", 1280, 790, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 30)


COBRA = [("02.a", "LER O ENDEREÇO", "a casa · a soma da linha · a da coluna", BLUE, 0, True),
         ("02.b", "MULTIPLICAR COM SENTIDO", "quantidade × preço", GREEN, 9, False),
         ("02.c", "A CONTA EXISTE?", "as ordens encaixam?", AMBER, 7, False),
         ("02.d", "IMAGENS E CÓDIGOS", "pixels · mensagem secreta", PURPLE, 1, False)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "QUATRO FORMAS", BLUE)
    for k, (cue, tit, sub_, col, ic, ep1) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 250 + d, 380, 500, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 30, "black", col, a, 340, 38, align="center")
        if ep1:
            icone(c, 0, x, 565 + d, 0.48, a)
        else:
            area_icone(c, ic, x, 570 + d, 0.48, a)
        para_nb(c, sub_, x, 705 + d, 26, "black", INK2, a, 340, 32, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "O QUE CADA CASA DO PRODUTO SIGNIFICA", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 220, 1200, 100, 50, mix("#FFFFFF", PURPLE, 0.18), aa, shadow=True)
        text_mid(c, "cada elemento do produto tem um significado", W / 2, 270, 40, "black", PURPLE, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab <= 0:
        return
    # A: a linha i acesa (o que a filial i compra)
    A_ = [["", "", ""], ["", "", ""]]
    matriz(c, 440, 520, A_, ab, 90, 80, 36, hi={(1, 0), (1, 1), (1, 2)}, hi_col=BLUE)
    fit(c, "linha i: o que a filial i compra", 440, 660, 30, 460, "black", BLUE, ab, align="center")
    ftext(c, "·", 700, 540, 70, "black", INK, ab)
    B_ = [["", ""], ["", ""], ["", ""]]
    ab2 = ep(t, C["03.b"] + 1.8, 0.5)
    matriz(c, 900, 520, B_, ab2, 90, 70, 36, hi={(0, 1), (1, 1), (2, 1)}, hi_col=GREEN)
    fit(c, "coluna j: os preços do fornecedor j", 900, 660, 30, 420, "black", GREEN, ab2, align="center")
    ab3 = ep(t, C["03.b"] + 4.0, 0.5)
    if ab3 > 0:
        arrow(c, 1110, 520, 1250, 520, PURPLE, ab3, 6, 16)
        rrect(c, 1270, 440, 400, 160, 24, mix("#FFFFFF", PURPLE, 0.18), ab3, shadow=True)
        sub(c, "c", "ij", 1470, 500, 64, PURPLE, ab3)
        fit(c, "quanto a filial i gasta no fornecedor j", 1470, 570, 22, 370, "black", INK, ab3, align="center")


INDICE = [("EP. 1", "o assento do cinema: fileira, depois poltrona · a tabela de mão dupla é um espelho · linha = fez, coluna = sofreu"),
          ("EP. 2", "as folhas transparentes: casa com casa · número × matriz: aumento geral"),
          ("EP. 3", "o caixa do supermercado: linha × coluna · a regra do dominó: os de dentro encaixam"),
          ("EP. 4", "meia e sapato: a ordem importa · identidade = o número 1 · a inversa é a chave do cadeado")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 360, 380, 1200, 160, 30, "#FFFFFF", aq, shadow=True)
        fmid(c, "em a₂₃, qual número é a linha?", W / 2, 460, 54, "black", INK, aq)
        pause_timer(c, t, C["04.t"] + 2.4, 1480, 640, a=aq)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 358 + k * 400
        y = 210
        rrect(c, x - 190, y, 380, 620, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 190, y, 380, 620), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 170, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 200, 0.56, a)
        yy = y + 360
        for ln in s.split(" · "):
            yy += para_nb(c, ln, x, yy, 24, "black", INK if on_ else INK2, a, 340, 30, align="center") + 10


ONDE = [("06.a", "TECNOLOGIA", 1, "cada pixel é um elemento", BLUE),
        ("06.b", "ECONOMIA", 2, "quantidade × preço", AMBER),
        ("06.c", "NUTRIÇÃO", 3, "porções × nutrientes", GREEN),
        ("07.d", "GEOGRAFIA", 4, "distâncias e redes", BLUE),
        ("07.e", "SISTEMAS", 5, "a próxima série", PURPLE)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS ÁREAS", "A MESMA TABELA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 310 + k * 325
        rrect(c, x - 150, 230 + d, 300, 560, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 290 + d, 30, "black", col, a, 280, 36, align="center")
        area_icone(c, ic, x, 470 + d, 0.40, a)
        para_nb(c, res, x, 660 + d, 28, "black", INK, a, 270, 34, align="center")


HABITOS = [("08.a", "ROTULE LINHA E COLUNA", "boa parte dos erros é de leitura"),
           ("08.b", "CONFIRA AS ORDENS", "(2 × 3) · (3 × 2): os de dentro batem?"),
           ("09.c", "SÓ O ELEMENTO PEDIDO", "uma casa? não monte a matriz inteira"),
           ("09.d", "CONFIRA A INVERSA", "original × inversa = identidade")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "QUATRO HÁBITOS NA HORA H", GREEN)
    for k, (cue, tit, sub_) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 140 + (k % 2) * 830
        y = 230 + (k // 2) * 300
        rrect(c, x, y + d, 800, 270, 24, mix("#F7F7F5", GREEN, 0.10), a, shadow=True)
        badge_num(c, k + 1, x + 70, y + 70 + d, a, 34, bg=GREEN)
        fit(c, tit, x + 130, y + 84 + d, 40, 640, "black", GREEN, a)
        para_nb(c, sub_, x + 400, y + 170 + d, 32, "bold", INK, a, 700, 40, align="center")


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["10.t"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["10.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["10.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["10.b"], 0.5), anchor="center")


# (contexto, afirmação [itens], verdadeira?, por que engana, regra certa, versão certa [itens], ícone do episódio)
VF = [
    ("o endereço", ["a₂₃ → linha 3, coluna 2"], False, "os dois números estão ali; a ordem parece detalhe",
     "como no cinema: primeiro a fileira (linha)", ["linha 2, coluna 3"], 0),
    ("multiplicar", [M("1 0", "2 1"), "·", M("3 1", "1 2"), "=", M("3 0", "2 2")], False,
     "a soma é mesmo casa a casa", "o produto é linha por coluna", [M("3 1", "7 4")], 2),
    ("o dominó", ["(2 × 3) · (2 × 3) não existe"], True, "as duas são do mesmo tamanho",
     "colunas da 1ª (3) = linhas da 2ª (2)? não encaixa", ["3 ≠ 2"], 2),
    ("a ordem", ["A · B = B · A sempre"], False, "com números, a ordem não importa",
     "meia e sapato: a ordem muda o resultado", [M("2 1", "1 1"), "≠", M("1 1", "1 2")], 3),
    ("produto nulo", ["A · B = 0  →  A = 0 ou B = 0"], False, "com números, produto zero obriga um fator zero",
     "duas matrizes não nulas podem dar produto nulo", [M("1 2", "2 4"), "·", M("2 -2", "-1 1"), "= 0"], 3),
    ("a inversa", ["a inversa de", M("4 1", "3 1"), "é", M("1 -1", "-3 4")], True, "não é só trocar a diagonal",
     "troca a diagonal, muda o sinal da outra, divide por 1", ["confere: dá I"], 3),
    ("a transposta", ["transposta de 2 × 3 → 2 × 3"], False, "os números são os mesmos",
     "linhas viram colunas", ["3 × 2"], 0),
    ("tabela de jogos", ["coluna = gols sofridos"], True, "dá vontade de ler a coluna como gols marcados",
     "linha = o que o time fez · coluna = o que sofreu", ["releia a definição"], 0),
    ("número × matriz", ["3 ·", M("1 2", "0 4"), "=", M("3 6", "0 4")], False, "o 3 parece ficar na 1ª linha",
     "aumento geral: atinge todas as casas", [M("3 6", "0 12")], 1),
]
VF_IDS = [f"{11 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, itens, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 62 + k * 62, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 410, 0.42, a0)
    fmid(c, ctx.upper(), 960, 280, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    w = expr(c, itens, 960, 420, a0, 46, 66, 56, maxw=780)
    if ar > 0 and not ver:
        strike(c, 960 - w / 2 - 10, 424, 960 + w / 2 + 10, 424, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 560, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 560, ae, "PEGADINHA", AMBER, -5, 30)
        fit(c, engana, 640 if ver else 520, 572, 32, 1020 if ver else 1140, "bold", INK2, ae)
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 640, 1520, 170, GREEN, ag, 0.07)
        lns = _quebra(nb(regra_), 30, 880)
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 735 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        expr(c, fix, 1460, 725, ag, 40, 52, 44, col=GREEN, maxw=440)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["20.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["20.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 140 + k * 140
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["20.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    if ab > 0:
        rrect(c, W / 2 - 600, 700, 1200, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "rotule linha e coluna · escreva as ordens · confira", W / 2, 750, 34, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

V_ = M("12 8 15", "10 14 6", "7 11 13")
QA, QB = M("1 4", "2 0"), M("5 6", "4 8")
QQ, QN = M("2 1", "1 3"), M("3 28", "7 15")
CH_A, CH_E = M("2 1", "5 3"), M("7", "18")

Q = {
    "q1": dict(ids=("21", "22"), titulo="O TOTAL DO MÊS", area="LEITURA DE TABELA", ok="C",
               enun=[("a", "linha i, coluna j: unidades do vendedor i no mês j", False),
                     ("b", "Total do mês 2, pelos 3 vendedores?", True)],
               alts=[("A", "14", "só a casa v₂₂", RED), ("B", "30", "somou a linha 2", AMBER),
                     ("C", "33", "", GREEN), ("D", "35", "somou a linha 1", RED), ("E", "96", "a tabela inteira", RED)],
               passos=[("d", "linha = vendedor · coluna = mês"), ("a", "mês 2 = coluna 2"), ("a", "8 + 14 + 11 = 33")]),
    "q2": dict(ids=("23", "24"), titulo="ACHE O X", area="EQUAÇÃO DE MATRIZES", ok="B",
               enun=[("a", "2X + A = B", True), ("b", "A soma dos elementos de X é:", False)],
               alts=[("A", "4,5", "B ÷ 2 − A", RED), ("B", "8", "", GREEN), ("C", "9", "B − 2A", RED),
                     ("D", "15", "(B + A) ÷ 2", RED), ("E", "16", "esqueceu o ÷ 2", AMBER)],
               passos=[("d", "X = (B − A) ÷ 2"), ("a", "B − A, casa a casa, ÷ 2"), ("a", "soma de X = 8")]),
    "q3": dict(ids=("25", "26"), titulo="A PROTEÍNA DA REFEIÇÃO 2", area="PRODUTO EM CONTEXTO", ok="D",
               enun=[("a", "Q: porções por refeição · N: nutrientes por porção", False),
                     ("b", "Proteína da refeição 2, em gramas?", True)],
               alts=[("A", "10", "sem as porções", RED), ("B", "13", "a refeição 1", AMBER),
                     ("C", "16", "trocou as porções", RED), ("D", "24", "", GREEN), ("E", "73", "os carboidratos", RED)],
               passos=[("d", "só a casa pedida: linha 2 de Q × coluna 1 de N"), ("a", "1 · 3 + 3 · 7 = 24 g")]),
    "q4": dict(ids=("27", "28"), titulo="QUAL CONTA EXISTE?", area="AS ORDENS", ok="C",
               enun=[("a", "A: 3 × 2  ·  B: 2 × 4  ·  C: 3 × 4", True), ("b", "A única operação possível é:", False)],
               alts=[("A", "B · A", "4 ≠ 3", RED), ("B", "A + B", "ordens diferentes", RED),
                     ("C", "A · B + C", "", GREEN), ("D", "C · A", "4 ≠ 3", RED), ("E", "A · C", "2 ≠ 3", AMBER)],
               passos=[("d", "escreva as ordens, confira o meio"), ("a", "(3 × 2) · (2 × 4) = 3 × 4"),
                       ("a", "3 × 4 + 3 × 4: dá para somar")]),
    "q5": dict(ids=("29", "30"), titulo="O CÓDIGO SECRETO", area="A INVERSA", ok="B",
               enun=[("a", "chave A · mensagem recebida E", False), ("b", "Os números originais, de cima para baixo?", True)],
               alts=[("A", "1 e 3", "inverteu a ordem", RED), ("B", "3 e 1", "", GREEN),
                     ("C", "−3 e −1", "sinais da diagonal errada", AMBER), ("D", "39 e 71", "só trocou a diagonal", RED),
                     ("E", "32 e 89", "trancou de novo com A", RED)],
               passos=[("d", "ad − bc = 6 − 5 = 1"), ("a", "inversa · E = (3, 1)"), ("v", "confere: 2 · 3 + 1 · 1 = 7")]),
}


def rotulos(c, x0, y0, cw, ch, linhas_, cols, a, size=20, col_l=INK2, col_c=INK2):
    """rótulos de linha (à esquerda) e de coluna (em cima) de uma matriz com canto (x0, y0)"""
    for i, s in enumerate(linhas_):
        ftext(c, s, x0 - 8, y0 + 10 + ch * (i + 0.5) + size * 0.36, size, "black", col_l, a, align="right")
    for j, s in enumerate(cols):
        ftext(c, s, x0 + 20 + cw * (j + 0.5), y0 - 12, size, "black", col_c, a, align="center")


def fig_q1(c, a, sol, prog):
    cw, ch = 96, 66
    w, h = mat_wh(V_, cw, ch)
    cx, cy = 520, 600
    hi = {(i, 1) for i in range(3)} if sol else None
    cores = {(i, 1): GREEN for i in range(3)} if sol else None
    matriz(c, cx, cy, V_, a, cw, ch, 36, cores=cores, hi=hi, hi_col=GREEN)
    rotulos(c, cx - w / 2, cy - h / 2, cw, ch, ("vend. 1", "vend. 2", "vend. 3"), ("mês 1", "mês 2", "mês 3"), a,
            col_c=GREEN if sol else INK2)


def fig_q2(c, a, sol, prog):
    if not sol:
        ftext(c, "A =", 250, 616, 38, "black", INK, a, align="center")
        matriz(c, 400, 604, QA, a, 70, 60, 34)
        ftext(c, "B =", 560, 616, 38, "black", INK, a, align="center")
        matriz(c, 700, 604, QB, a, 70, 60, 34)
        return
    expr(c, [M("4 2", "2 8"), "÷ 2 =", M("2 1", "1 4")], 480, 630, a * ep(prog, 0.2, 0.3), 34, 60, 52, maxw=600)


def fig_q3(c, a, sol, prog):
    cw, ch = 72, 60
    hiQ = {(1, 0), (1, 1)} if sol else None
    hiN = {(0, 0), (1, 0)} if sol else None
    for (vals, cx, nome, ls, cs, hi) in ((QQ, 380, "Q", ("ref. 1", "ref. 2"), ("arroz", "feijão"), hiQ),
                                         (QN, 680, "N", ("arroz", "feijão"), ("prot.", "carb."), hiN)):
        w, h = mat_wh(vals, cw, ch)
        cy = 620
        matriz(c, cx, cy, vals, a, cw, ch, 32, hi=hi, hi_col=AMBER)
        rotulos(c, cx - w / 2, cy - h / 2, cw, ch, ls, cs, a, size=18)
        ftext(c, nome, cx, cy + h / 2 + 40, 30, "black", BLUE, a, align="center")


def fig_q4(c, a, sol, prog):
    for k, (n, o, col) in enumerate((("A", "3 × 2", BLUE), ("B", "2 × 4", GREEN), ("C", "3 × 4", PURPLE))):
        x = 270 + k * 190
        rrect(c, x - 80, 560, 160, 120, 18, mix("#FFFFFF", col, 0.15), a, shadow=True)
        ftext(c, n, x, 605, 36, "black", col, a, align="center")
        fit(c, o, x, 655, 32, 140, "black", INK, a, align="center")
    if sol:
        area_icone(c, 7, 640, 620, 0.40, a * ep(prog, 0.3, 0.3))


def fig_q5(c, a, sol, prog):
    if not sol:
        icone(c, 3, 260, 610, 0.30, a)
        ftext(c, "A =", 390, 622, 36, "black", INK, a, align="center")
        matriz(c, 520, 610, CH_A, a, 64, 56, 32)
        ftext(c, "E =", 650, 622, 36, "black", INK, a, align="center")
        matriz(c, 740, 610, CH_E, a, 70, 56, 32)
        return
    expr(c, [M("3 -1", "-5 2"), "·", CH_E, "=", M("3", "1")], 480, 560, a * ep(prog, 0.2, 0.3), 34, 60, 50,
         col=INK, maxw=600)


FIGS = dict(q1=fig_q1, q2=fig_q2, q3=fig_q3, q4=fig_q4, q5=fig_q5)


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · {d['area']}", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        K.alternativas(c, t, C, [(L, nb(s), w, col) for L, s, w, col in d["alts"]],
                       880, 230, 820, 30, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        area_icone(c, 0, 770, 222, 0.20, a0)
        y = 270
        ae = ep(t, C[f"{s1}.a"], 0.4) * (1 - sol)
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 620, 40)
            y += h + 14
        FIGS[nome](c, ae, False, 0)
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 760, 790)
        if sol > 0:
            yy = 280
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 30, 640, "black", GREEN if last else INK, a)
                yy += 60
            FIGS[nome](c, sol, True, t - C[f"{s2}.a"])
            result_box(c, f"Letra {d['ok']}", 1290, 790, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["a casa a₂₃ sem trocar", "lei de formação e tipos", "tabelas: jogos e distâncias"]),
         ("31.c", "EP. 2", 1, ["soma casa a casa", "número × matriz: tudo", "igualdade vira sistema"]),
         ("32.a", "EP. 3", 2, ["o produto existe? qual a ordem?", "linha por coluna, com sentido", "A²: rotas com 1 escala"]),
         ("32.b", "EP. 4", 3, ["AB ≠ BA · AB = 0 sem fator nulo", "a inversa da 2 × 2", "conferir multiplicando"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 210), (150, 480), (990, 210), (990, 480)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, ic, x + 60, y0 + 140, 0.24, a)
        for j, it in enumerate(itens):
            yy = y0 + 40 + j * 62
            rrect(c, x + 150, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            fit(c, it, x + 198, yy + 10, 28, 580, "bold", INK, a)
    ac = ep(t, C["32.c"], 0.5)
    if ac > 0:
        boxed(c, 560, 760, 800, 90, AMBER, ac, 0.10)
        text_mid(c, "não marcou? reveja o episódio", W / 2, 805, 34, "black", INK, ac)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["33.a"], 0.5)
    ab = ep(t, C["33.b"], 0.5)
    ac = ep(t, C["33.c"], 0.5)
    for i in range(25):
        r_, k = divmod(i, 5)
        a = aa * ep(t, C["33.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 18
        x, y = 220 + k * 96, 200 + r_ * 92
        col = mix("#E6E6E2", GREEN, ab if ok else 0)
        rrect(c, x, y, 78, 78, 12, col, a)
        if ac > 0 and i < 13:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 86, 86), 14, 14),
                        paint(BLUE if i < 8 else PURPLE, ac, stroke=4))
        if ok:
            check_icon(c, x + 39, y + 39, 20, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 39, y + 39, 26, "black", INK2, a)
    text(c, "25 questões", 1260, 300, 56, "black", INK, aa)
    text(c, "18 acertos", 1260, 400, 48, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 800, 500, 920, 260, PURPLE, ac, 0.08)
        area_icone(c, 0, 890, 580, 0.22, ac)
        fit(c, "8 de leitura de tabela", 970, 595, 40, 700, "black", BLUE, ac)
        area_icone(c, 9, 890, 690, 0.22, ac)
        fit(c, "5 de produto em contexto", 970, 705, 40, 700, "black", PURPLE, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 240, 28, "black", GRAY, aa, tracking=2)
    text(c, "Determinantes e sistemas lineares", W / 2, 330, 70, "black", PURPLE, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        rrect(c, 660, 400, 600, 150, 30, mix("#FFFFFF", PURPLE, 0.18), ab, shadow=True)
        text_mid(c, "ad − bc", W / 2, 475, 84, "black", PURPLE, ab)
        selo(c, 1380, 430, ep(t, C["34.b"] + 1.0, 0.4), "GANHA NOME", BLUE, -4, 26)
    ac = ep(t, C["34.c"], 0.5)
    for k, (s, col) in enumerate((("1 solução", GREEN), ("nenhuma", RED), ("infinitas", BLUE))):
        chip(c, s, 560 + k * 400, 690, col, ep(t, C["34.c"] + 1.2 + 0.5 * k, 0.4) * ac if ac > 0 else 0, 38)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
