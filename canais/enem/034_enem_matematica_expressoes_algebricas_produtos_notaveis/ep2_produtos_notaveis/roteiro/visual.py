"""Visual — Expressões Algébricas e Produtos Notáveis, Episódio 2: produtos notáveis e o sonho do calouro (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, selo_teste...).
Peças deste episódio: quadrado() (o quadrado de lado a + b em quatro pedaços: a², b² e DOIS retângulos ab), piso() (o piso
de 7 × 7 lajotas), porta() (a porta da multiplicação, aberta, e a da soma, barrada), cubo() (cubo em perspectiva), m().
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
_s = importlib.util.spec_from_file_location("comum034", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_algebra_ep2_produtos_notaveis.mp4"
CARD_R = K.CARD_R
A_COL = "#DCE8FA"   # pedaço a²
B_COL = "#DDF3E3"   # pedaço b²
R_COL = "#FBE7C2"   # retângulos ab


def m(c, s, cx, cy, size, a=1.0, hl=None, align="center", col=None):
    """linha matemática (expr) de uma cor, com destaques por token: hl = {índice: cor}"""
    n = len(s.split())
    cores = {i: col or INK for i in range(n)}
    cores.update(hl or {})
    return K.expr(c, s, cx, cy, size, a, cores=cores, align=align)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# peças do episódio
# ======================================================================

def quadrado(c, x, y, la, lb, u, a, ret=1.0, blink=0.0, labs=("a^2", "ab", "ab", "b^2"), lado=("a", "b"), size=40,
             sep=0.0, pedacos=(1, 1, 1, 1)):
    """o quadrado de lado la + lb (em unidades u px): a² (azul), b² (verde) e os DOIS retângulos ab (âmbar).
    ret = opacidade dos retângulos (0 = sumiram), blink = pisca âmbar forte, sep = afastamento entre os pedaços."""
    if a <= 0:
        return
    A, Bs = la * u, lb * u
    ret_col = mix(R_COL, AMBER, 0.55 * blink)
    pcs = [(x, y, A, A, A_COL, BLUE, labs[0], 1.0),
           (x + A + sep, y, Bs, A, ret_col, AMBER, labs[1], ret),
           (x, y + A + sep, A, Bs, ret_col, AMBER, labs[2], ret),
           (x + A + sep, y + A + sep, Bs, Bs, B_COL, GREEN, labs[3], 1.0)]
    for k, (px, py, pw, ph, fill, edge, lab, al) in enumerate(pcs):
        aa = a * al * pedacos[k]
        if aa <= 0:
            continue
        rrect(c, px, py, pw, ph, 6, fill, aa)
        c.drawRect(skia.Rect.MakeXYWH(px, py, pw, ph), paint(edge, aa, stroke=3))
        if lab:
            sz = min(size, 0.42 * min(pw, ph) + 10)
            m(c, lab, px + pw / 2, py + ph / 2, sz, aa, col=edge)
    if lado:
        for k, (l0, ln) in enumerate(((0, A), (A + sep, Bs))):
            text_mid(c, lado[k], x + l0 + ln / 2, y - 28, 34, "black", INK2, a)
            text_mid(c, lado[k], x - 30, y + l0 + ln / 2, 34, "black", INK2, a)


def piso(c, x, y, s, a, ret=1.0, blink=0.0, n=7, k=3):
    """piso de n × n lajotas; as k × k (azul), as (n−k)² (verde) e os dois retângulos (âmbar, opacidade ret)"""
    if a <= 0:
        return
    for i in range(n):
        for j in range(n):
            if i < k and j < k:
                col, al = A_COL, 1.0
            elif i >= k and j >= k:
                col, al = B_COL, 1.0
            else:
                col, al = mix(R_COL, AMBER, 0.55 * blink), ret
            aa = a * al
            if aa <= 0:
                continue
            rrect(c, x + j * s + 2, y + i * s + 2, s - 4, s - 4, 5, col, aa)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + j * s + 2, y + i * s + 2, s - 4, s - 4), 5, 5),
                        paint("#BDB7A8", aa * 0.8, stroke=1.5))


def porta(c, cx, cy, op, aberta, a, conteudo):
    """porta com o operador no alto; aberta = verde com a fórmula passando; fechada = barrada em vermelho"""
    if a <= 0:
        return
    col = GREEN if aberta else RED
    w, h = 300, 360
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x - 16, y - 16, w + 32, h + 16, 18, "#F1EEE6", a)
    rrect(c, x, y, w, h, 12, mix("#FFFFFF", col, 0.10), a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(col, a, stroke=5))
    chip(c, op, cx, y - 2, col, a, 46, True, 90)
    if aberta:
        m(c, conteudo, cx, cy + 40, 40, a)
        check_icon(c, cx, y + h - 50, 28, a, GREEN)
    else:
        m(c, conteudo, cx, cy + 40, 40, a * 0.45)
        for dy in (-40, 40):
            c.drawLine(x - 10, cy + dy, x + w + 10, cy + dy, paint(RED, a, stroke=14, cap_round=True))
        check_icon(c, cx, y + h - 50, 28, a, RED, "x")


def cubo(c, x, y, s, a, col=BLUE, fill=None, dash=False, prof=0.45):
    """cubo em perspectiva cavaleira: frente s × s em (x, y), fundo deslocado"""
    if a <= 0:
        return
    d = s * prof
    fill = fill or mix("#FFFFFF", col, 0.14)
    fr_ = skia.Path(); fr_.addRect(skia.Rect.MakeXYWH(x, y, s, s))
    top = skia.Path(); top.moveTo(x, y); top.lineTo(x + d, y - d); top.lineTo(x + s + d, y - d); top.lineTo(x + s, y); top.close()
    side = skia.Path(); side.moveTo(x + s, y); side.lineTo(x + s + d, y - d); side.lineTo(x + s + d, y + s - d)
    side.lineTo(x + s, y + s); side.close()
    pe = paint(col, a, stroke=4)
    if dash:
        pe.setPathEffect(skia.DashPathEffect.Make([16, 10], 0))
    else:
        c.drawPath(fr_, paint(fill, a)); c.drawPath(top, paint(mix(fill, "#FFFFFF", 0.4), a))
        c.drawPath(side, paint(mix(fill, col, 0.15), a))
    for pth in (fr_, top, side):
        c.drawPath(pth, pe)


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def defin(c, termo, s, y, a, w=1400):
    """faixa azul de definição: TERMO + frase"""
    if a <= 0:
        return
    x = W / 2 - w / 2
    boxed(c, x, y - 50, w, 100, BLUE, a, 0.08)
    pill(c, termo, x + 24, y, BLUE, size=26, a=a)
    tw = text_w(termo, "bold", 26) + 70
    para(c, s, x + 24 + tw, y + 12, 32, "bold", INK, a, w - tw - 60)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PRODUTOS NOTÁVEIS", PURPLE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 230, 1200, 190, 30, "#FFFFFF", aa, shadow=True)
        m(c, "(a+b)^2 = a^2 + b^2", W / 2, 325, 96, aa)
        ab = ep(t, C["01.b"], 0.5)
        if ab > 0:
            strike(c, 440, 325, 1480, 325, ab, RED, ab)
            selo(c, 1500, 230, ab, "ERRADA", RED, 8, 40)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        for k in range(14):
            xx = 330 + k * 92
            ak = acc * ep(t, C["01.c"] + 0.08 * k, 0.3)
            c.drawCircle(xx, 540, 22, paint(GRAY, ak * 0.7))
            rrect(c, xx - 26, 568, 52, 50, 18, GRAY, ak * 0.7)
        pill(c, "milhões de estudantes, todo ano", W / 2, 670, AMBER, size=30, a=acc, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 560, 730, 800, 90, 18, "#FFFFFF", ad, shadow=True)
        badge_num(c, "C", 620, 775, ad, 24, bg=INK)
        m(c, "a^2 + b^2", 760, 775, 44, ad, align="left")
        selo(c, 1180, 775, ad, "ESPERANDO POR VOCÊ", AMBER, -4, 26)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "desenvolver os produtos notáveis de cabeça", "(a+b)^2   (a-b)^2   (a+b)(a-b)   (a+b)^3"),
            ("02.b", "enxergar o termo do meio que a pegadinha esconde", "a^2 + 2ab + b^2")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 230 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        m(c, sub, 360, y + 80, 40, a, hl={2: AMBER} if j == 1 else None, align="left", col=None if j == 1 else GRAY)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "DISTRIBUTIVA = APERTO DE MÃO", 560, 290, 32, "black", BLUE, aa)
        text(c, "episódio 1", 560, 340, 26, "bold", GRAY, aa)
        m(c, "(a+b)(c+d)", 560, 450, 60, aa)
        pr = ["ac", "ad", "bc", "bd"]
        for k, s in enumerate(pr):
            ak = ep(t, C["03.a"] + 1.2 + 0.5 * k, 0.4)
            chip(c, s, 380 + k * 120, 580, BLUE, ak, 40)
        text(c, "cada termo cumprimenta cada termo", 560, 690, 28, "bold", INK2, ep(t, C["03.a"] + 3.4, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "NA SOMA: SEM PROPRIEDADE", 1370, 290, 32, "black", PURPLE, ab)
        text(c, "série de Potenciação", 1370, 340, 26, "bold", GRAY, ab)
        m(c, "(a·b)^2 = a^2·b^2", 1370, 470, 56, ab)
        check_icon(c, 1680, 452, 24, ab, GREEN)
        m(c, "(a+b)^2 = ?", 1370, 610, 56, ep(t, C["03.b"] + 1.6, 0.4), hl={2: AMBER})
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UM PISO QUADRADO", "QUANTAS LAJOTAS?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    cc = ep(t, C["04.c"] + 1.0, 0.6)
    dd = ep(t, C["04.d"], 0.4)
    blink = dd * (0.5 + 0.5 * math.sin((t - C["04.d"]) * 7)) if dd > 0 else 0
    piso(c, 260, 240, 78, aa, ret=1 - 0.75 * cc + 0.75 * dd, blink=blink)
    if aa > 0:
        text(c, "3", 260 + 117, 222, 30, "black", BLUE, aa)
        text(c, "4", 260 + 3 * 78 + 156, 222, 30, "black", GREEN, aa)
        text(c, "7 lajotas de lado", 260 + 273, 840, 28, "bold", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 260, 680, 120, 20, "#F7F7F5", ab)
        linha = "7 · 7 = 49"
        m(c, linha, 1340, 320, 56, ab, hl={4: BLUE})
    if ep(t, C["04.c"], 0.5) > 0:
        ac = ep(t, C["04.c"], 0.5)
        rrect(c, 1000, 420, 680, 120, 20, "#F7F7F5", ac)
        m(c, "3^2 + 4^2 = 25", 1340, 480, 56, ac, hl={4: AMBER})
    if dd > 0:
        rrect(c, 1000, 590, 680, 150, 20, mix("#FFFFFF", AMBER, 0.14), dd)
        text_mid(c, "faltam 24 lajotas!", 1340, 645, 50, "black", AMBER, dd)
        text_mid(c, "onde elas estão?", 1340, 705, 32, "bold", INK2, dd)


# ======================================================================
# bloco a — quadrado da soma
# ======================================================================

def b_soma(c, t, C, B):
    head_seq(c, t, C, [("05", "QUADRADO DA SOMA", "PELO DESENHO", BLUE), ("06", "O TERMO DO MEIO", "CONFIRA PELA DISTRIBUTIVA", PURPLE),
                       ("07", "ATALHO", "A FRASE DO QUADRADO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06", "07"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        defin(c, "PRODUTO NOTÁVEL", "multiplicação que aparece tanto que vale guardar o resultado pronto", 240, aa * (1 - ep(t, C["05.c"], 0.4)))
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            pill(c, "QUADRADO DA SOMA", 1340, 250 + 120 * ep(t, C["05.c"], 0.4), BLUE, size=28, a=ab, anchor="center")
            m(c, "(a+b)^2", 1340, 340 + 110 * ep(t, C["05.c"], 0.4), 72, ab)
        ac = ep(t, C["05.c"], 0.5)
        if ac > 0:
            quadrado(c, 330, 300, 4.2, 2.6, 70, ac, pedacos=(ep(t, C["05.d"], 0.4), ep(t, C["05.e"], 0.4),
                                                             ep(t, C["05.e"] + 0.5, 0.4), ep(t, C["05.d"] + 1.0, 0.4)),
                     blink=ep(t, C["05.e"], 0.4) * (1 - ep(t, C["05.f"], 0.5)))
            if ep(t, C["05.e"], 0.4) > 0:
                pill(c, "DOIS retângulos ab", 1340, 590, AMBER, size=30, a=ep(t, C["05.e"], 0.4), anchor="center")
        af = ep(t, C["05.f"], 0.5)
        if af > 0:
            rrect(c, 960, 660, 760, 120, 22, "#FFFFFF", af, shadow=True)
            m(c, "(a+b)^2 = a^2 + 2ab + b^2", 1340, 720, 56, af, hl={4: AMBER})
        return
    if sid == "06":
        quadrado(c, 260, 300, 3.4, 2.1, 70, 1.0, size=34)
        at = ep(t, C["06"], 0.5)
        m(c, "a^2 + 2ab + b^2", 1260, 260, 52, at, hl={2: AMBER})
        pill(c, "TERMO DO MEIO", 1260, 330, AMBER, size=24, a=at, anchor="center")
        aa = ep(t, C["06.a"], 0.5)
        m(c, "(a+b)·(a+b)", 1260, 420, 54, aa)
        rows = [("a·a = a^2", BLUE), ("a·b = ab", AMBER), ("b·a = ab", AMBER), ("b·b = b^2", GREEN)]
        for k, (s, col) in enumerate(rows):
            ak = ep(t, C["06.b"] + 1.1 * k, 0.4)
            m(c, s, 1060 + (k % 2) * 400, 520 + (k // 2) * 90, 44, ak, hl={2: col})
        ac = ep(t, C["06.c"], 0.5)
        if ac > 0:
            rrect(c, 980, 700, 560, 100, 22, mix("#FFFFFF", AMBER, 0.12), ac)
            m(c, "ab + ab = 2ab", 1260, 750, 50, ac, hl={4: AMBER})
        return
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 200, 1480, 170, GREEN, aa, 0.08)
        text(c, "ATALHO · A FRASE DO QUADRADO", W / 2, 244, 22, "black", GREEN, aa, tracking=2)
        text_mid(c, "quadrado do 1º  ·  2 × 1º × 2º  ·  quadrado do 2º", W / 2, 312, 46, "black", INK, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        m(c, "(x+5)^2", 560, 520, 72, ab)
        text_mid(c, "=", 790, 520, 64, "black", INK, ab)
    parts = [("07.c", "x^2", BLUE, "x · x", 960), ("07.d", "+ 10x", AMBER, "2 · x · 5", 1240), ("07.e", "+ 25", GREEN, "5 · 5", 1510)]
    for cue, s, col, why, x in parts:
        ak = ep(t, C[cue], 0.5)
        if ak > 0:
            m(c, s, x, 520, 72, ak, col=col)
            text_mid(c, why, x, 630, 32, "bold", INK2, ak)
    if ep(t, C["07.d"], 0.5) > 0:
        pill(c, "termo do meio", 1240, 700, AMBER, size=24, a=ep(t, C["07.d"], 0.5), anchor="center")


# ======================================================================
# blocos b, c — diferença e soma pela diferença
# ======================================================================

def b_diferenca(c, t, C, B):
    head(c, t, B["start"], "QUADRADO DA DIFERENÇA", "E SE FOR MENOS?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    pill(c, "QUADRADO DA DIFERENÇA", W / 2, 250, BLUE, size=28, a=aa, anchor="center")
    m(c, "(a-b)^2", W / 2, 350, 80, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        rrect(c, 460, 430, 1000, 130, 24, "#FFFFFF", ab, shadow=True)
        m(c, "a^2 - 2ab + b^2", W / 2, 495, 72, ab, hl={1: AMBER, 2: AMBER, 4: GREEN})
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        arrow(c, 860, 650, 900, 575, AMBER, acc, 5, 16)
        text(c, "só o termo do meio troca de sinal", 700, 700, 32, "black", AMBER, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        arrow(c, 1330, 650, 1300, 575, GREEN, ad, 5, 16)
        m(c, "(-b)·(-b) = +b^2", 1360, 720, 40, ad, hl={2: GREEN})
        text(c, "b² continua POSITIVO", 1360, 790, 28, "black", GREEN, ad)


def b_somadif(c, t, C, B):
    head_seq(c, t, C, [("09", "SOMA PELA DIFERENÇA", "OS DO MEIO SE CANCELAM", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    pill(c, "PRODUTO DA SOMA PELA DIFERENÇA", W / 2, 240, BLUE, size=26, a=aa, anchor="center")
    m(c, "(a+b)(a-b)", W / 2, 330, 72, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        terms = ["a^2", "- ab", "+ ab", "- b^2"]
        xs = [620, 840, 1080, 1320]
        cc = ep(t, C["09.c"], 0.5)
        for k, (s, x) in enumerate(zip(terms, xs)):
            ak = ep(t, C["09.b"] + 0.7 * k, 0.4)
            col = AMBER if k in (1, 2) else INK
            m(c, s, x, 450, 60, ak * (1 - 0.6 * cc if k in (1, 2) else 1), col=col)
            if k in (1, 2) and cc > 0:
                strike(c, x - 70, 450, x + 70, 450, cc, RED, cc)
        if cc > 0:
            pill(c, "−ab + ab = 0", 960, 530, AMBER, size=26, a=cc, anchor="center")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        rrect(c, 560, 580, 800, 100, 22, "#FFFFFF", ad, shadow=True)
        m(c, "(a+b)(a-b) = a^2 - b^2", W / 2, 630, 50, ad, hl={2: PURPLE, 3: PURPLE, 4: PURPLE})
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        boxed(c, 300, 705, 1320, 110, GREEN, ae, 0.08)
        text_mid(c, "ATALHO: quadrado do 1º − quadrado do 2º", 720, 760, 32, "black", GREEN, ae)
        m(c, "(x+7)(x-7) = x^2 - 49", 1330, 760, 40, ae)


# ======================================================================
# blocos d, e — tabela e cubo
# ======================================================================

def b_tabela(c, t, C, B):
    head(c, t, B["start"], "NÚMERO NA FRENTE", "A FRASE CONTINUA VALENDO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    m(c, "(2x-3)^2", W / 2, 250, 76, aa)
    cards = [("10.b", "quadrado do 1º", "(2x)^2 = 4x^2", BLUE, "o 2 também sobe!"),
             ("10.c", "2 × 1º × 2º", "2·2x·3 = 12x", AMBER, "com o sinal de menos"),
             ("10.d", "quadrado do 2º", "3^2 = +9", GREEN, "positivo")]
    for k, (cue, tit, s, col, nota) in enumerate(cards):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 230 + k * 500
        rrect(c, x, 330, 460, 230, 22, mix("#FFFFFF", col, 0.10), ak)
        text(c, tit, x + 230, 380, 30, "black", col, ak)
        m(c, s, x + 230, 455, 46, ak)
        text(c, nota, x + 230, 530, 26, "bold", INK2, ak)
    ar = ep(t, C["10.d"] + 1.6, 0.5)
    if ar > 0:
        rrect(c, 460, 600, 1000, 110, 22, "#FFFFFF", ar, shadow=True)
        m(c, "(2x-3)^2 = 4x^2 - 12x + 9", W / 2, 655, 56, ar, hl={3: AMBER, 4: AMBER, 6: GREEN})
    pill(c, "juros compostos:  (1 + i)²  =  1 + 2i + i²", W / 2, 780, PURPLE, size=28, a=ep(t, C["10.e"], 0.5), anchor="center")


def b_cubo(c, t, C, B):
    head(c, t, B["start"], "O CUBO", "E SE O EXPOENTE FOR 3?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        pill(c, "CUBO DA SOMA", 260, 260, BLUE, size=24, a=aa)
        m(c, "(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3", 260, 345, 54, aa, hl={4: AMBER, 6: AMBER}, align="left")
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        pill(c, "CUBO DA DIFERENÇA", 260, 440, BLUE, size=24, a=ab)
        m(c, "(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3", 260, 525, 54, ab, hl={3: RED, 5: GREEN, 7: RED}, align="left")
        text(c, "sinais: + − + −", 1560, 535, 30, "black", AMBER, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        boxed(c, 230, 610, 1460, 200, GREEN, acc, 0.08)
        text(c, "ATALHO · COEFICIENTES", 560, 652, 22, "black", GREEN, acc, tracking=2)
        for k, n in enumerate(("1", "3", "3", "1")):
            chip(c, n, 360 + k * 130, 730, GREEN, ep(t, C["11.c"] + 0.4 * k, 0.4), 56)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        m(c, "a^3  a^2  a^1  a^0", 1200, 690, 44, ad, col=BLUE)
        m(c, "b^0  b^1  b^2  b^3", 1200, 770, 44, ad, col=GREEN)
        text(c, "↓ desce", 1500, 700, 26, "black", BLUE, ad, align="left")
        text(c, "↑ sobe", 1500, 780, 26, "black", GREEN, ad, align="left")


# ======================================================================
# bloco f — o sonho do calouro
# ======================================================================

def b_calouro(c, t, C, B):
    head_seq(c, t, C, [("12", "O SONHO DO CALOURO", "O ERRO MAIS FAMOSO", RED), ("13", "COM NÚMEROS", "O ERRO FICA VISÍVEL", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        a0 = ep(t, C["12"], 0.4)
        aa = ep(t, C["12.a"], 0.5)
        blink = (0.5 + 0.5 * math.sin((t - C["12"]) * 8)) * (1 - aa) * a0
        quadrado(c, 280, 300, 3.0, 2.0, 70, a0, ret=1 - 0.85 * aa, blink=blink, size=34)
        if aa > 0:
            m(c, "a^2 + b^2", 455, 720, 48, aa, col=RED)
            selo(c, 455, 790, aa, "SONHO DO CALOURO", RED, -4, 30)
        porta(c, 1030, 500, "×", True, ep(t, C["12.b"], 0.5), "(a·b)^2 = a^2·b^2")
        pill(c, "o expoente PASSA", 1030, 730, GREEN, size=26, a=ep(t, C["12.c"], 0.5), anchor="center")
        porta(c, 1450, 500, "+", False, ep(t, C["12.d"], 0.5), "(a+b)^2")
        pill(c, "fica BARRADO", 1450, 730, RED, size=26, a=ep(t, C["12.d"] + 0.6, 0.4), anchor="center")
        return
    aa = ep(t, C["13.a"], 0.5)
    piso(c, 240, 260, 48, aa, ret=1.0, blink=ep(t, C["13.b"], 0.4) * (0.5 + 0.5 * math.sin((t - C["13.b"]) * 7)))
    if aa > 0:
        m(c, "(3+4)^2 = 49", 1050, 290, 54, aa, hl={2: BLUE})
        m(c, "3^2 + 4^2 = 25", 1050, 380, 54, aa, hl={4: RED})
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        pill(c, "49 − 25 = 24 = 2 · 3 · 4  →  o 2ab", 1050, 460, AMBER, size=28, a=ab, anchor="center")
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 640, 540, 820, 110, 20, mix("#FFFFFF", GREEN, 0.10), acc)
        m(c, "√{9+16} = √{25} = 5", 1050, 595, 50, acc, hl={4: GREEN})
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 640, 680, 820, 110, 20, mix("#FFFFFF", RED, 0.10), ad)
        m(c, "√{9} + √{16} = 3 + 4 = 7", 1050, 735, 50, ad, hl={8: RED})
        text(c, "≠", 1530, 680, 90, "black", RED, ad)


# ======================================================================
# bloco g — teste de 10 segundos
# ======================================================================

def cronometro(c, cx, cy, r, a, u=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 10, paint(GREEN, a * 0.18))
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * u, False, paint(GREEN, a, stroke=10, cap_round=True))
    rrect(c, cx - 14, cy - r - 30, 28, 22, 6, GREEN, a)
    text_mid(c, "10 s", cx, cy, r * 0.62, "black", GREEN, a)


def b_teste(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O TESTE DE 10 SEGUNDOS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    cronometro(c, 330, 330, 90, aa, ep(t, C["14.a"], 10.0))
    if aa > 0:
        boxed(c, 500, 250, 1200, 120, BLUE, aa, 0.08)
        pill(c, "EXPRESSÕES EQUIVALENTES", 530, 310, BLUE, size=24, a=aa)
        text_mid(c, "dão o MESMO resultado para qualquer número", 1305, 312, 30, "bold", INK, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "troque as letras por números pequenos", 1100, 440, 36, "black", GREEN, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        pill(c, "a = 1   ·   b = 2", 330, 560, PURPLE, size=30, a=acc, anchor="center")
        m(c, "(1+2)^2 = 9", 900, 540, 52, acc, hl={2: BLUE})
        m(c, "1^2 + 2^2 = 5", 1450, 540, 52, ep(t, C["14.c"] + 1.8, 0.4), hl={4: RED})
        sa = ep(t, C["14.c"] + 3.6, 0.4)
        if sa > 0:
            text_mid(c, "≠", 1180, 540, 70, "black", RED, sa)
            K.selo_teste(c, 1180, 650, sa, False, "DIFERENTES: NÃO SÃO IGUAIS")
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        pill(c, "evite 0 e 1 sozinhos: 1² = 1 esconde diferenças · prefira 2 e 3", W / 2, 780, AMBER, size=26, a=ad,
             anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "PELA FRASE DO QUADRADO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 560, 220, 800, 130, 24, "#F7F7F5", aa)
        m(c, "(3x-2)^2 = ?", W / 2, 285, 66, aa)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 560)
    if t < C["16"]:
        return
    parts = [("16.a", "9x^2", BLUE, "(3x)^2", 640), ("16.b", "- 12x", AMBER, "2 · 3x · 2", 960), ("16.c", "+ 4", GREEN, "2^2", 1270)]
    for cue, s, col, why, x in parts:
        ak = ep(t, C[cue], 0.5)
        if ak > 0:
            m(c, s, x, 470, 70, ak, col=col)
            m(c, why, x, 570, 38, ak, col=INK2)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 640, 1200, 130, 22, mix("#FFFFFF", GREEN, 0.08), ad)
        text(c, "teste com x = 2", 560, 690, 26, "black", GREEN, ad)
        m(c, "(6-2)^2 = 16", 560, 735, 38, ad)
        m(c, "36 - 24 + 4 = 16", 1170, 712, 44, ad, hl={6: GREEN})
        conferido(c, "bateu", 1440, 740, ep(t, C["16.ok"], 0.4), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["O quadrado da soma tem sempre o termo do meio, 2ab.",
          "Na multiplicação o expoente entra; na soma, fica barrado.",
          "Na dúvida, teste com números."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("(a + b)² = a² + b²", "o expoente entra na multiplicação, e a gente acha que entra em tudo",
          "faltam os DOIS retângulos: escreva sempre o 2ab"),
         ("(a − b)² = a² − b²", "é curtinho, e esse resultado existe mesmo… em outro produto",
          "a² − b² é a SOMA PELA DIFERENÇA · o certo é a² − 2ab + b²"),
         ("(x + 5)² = x² + 5x + 25", "TEM termo do meio… só esqueceram o 2",
          "são DOIS retângulos: 10x · teste x = 1: 36 contra 31")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS2 = [("A", "9", "sonho do calouro", RED), ("B", "6x", "esqueceu o quadradinho", RED),
         ("C", "3x + 9", "um retângulo só", RED), ("D", "6x + 9", "", GREEN), ("E", "= x^2 + 6x + 9", "área nova inteira", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "ÁREA AMPLIADA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [("Um terreno quadrado tem lado de x metros. O proprietário vai aumentar cada lado em 3 metros, "
                           "mantendo a forma quadrada. O aumento da área do terreno, em metros quadrados, é dado por", INK)],
                      a0, 230, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 40, C["22.ok"], "D", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["21.end"] - 1.9, 540, yend + 150)
    if t >= C["22"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["22"], 0.4))
        aa = ep(t, C["22.a"], 0.4)
        ab, ac = ep(t, C["22.b"], 0.4), ep(t, C["22.c"], 0.4)
        quadrado(c, 250, y0 + 70, 3.3, 1.1, 58, aa, labs=("x^2", "3x", "3x", "9"), lado=("x", "3"), size=34,
                 pedacos=(1, ab, ab, ac), sep=6 * aa)
        ad = ep(t, C["22.d"], 0.4)
        if ad > 0:
            text(c, "aumento", 720, y0 + 110, 26, "black", INK2, ad)
            m(c, "6x + 9", 720, y0 + 170, 46, ad, hl={0: AMBER, 2: GREEN})
        ae = ep(t, C["22.e"], 0.4)
        if ae > 0:
            text(c, "pela conta", 720, y0 + 250, 24, "black", INK2, ae)
            m(c, "(x+3)^2 - x^2", 720, y0 + 300, 30, ae)
            m(c, "= 6x + 9", 720, y0 + 350, 30, ae, hl={1: GREEN, 2: GREEN, 3: GREEN})


ALTS7 = [("A", "0", "sonho do calouro", RED), ("B", "= -24x", "", GREEN), ("C", "= -12x", "termo do meio 6x", RED),
         ("D", "= 24x", "errou o sinal", RED), ("E", "= 8x^2 + 18", "somou os quadrados", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · NÓS FAZEMOS", "EXPRESSÃO EQUIVALENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    text(c, "A expressão", 190, 250, 28, "black", INK, a0, align="left")
    m(c, "(2x-3)^2 - (2x+3)^2", 540, 320, 50, a0)
    text(c, "é equivalente a", 190, 400, 28, "black", INK, a0, align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 250, 680, 40, C["25.ok"], "B", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["24.end"] - 1.9, 540, 560)
    if t >= C["25"]:
        y0 = 430
        _painel(c, y0, ep(t, C["25"], 0.4))
        m(c, "4x^2 - 12x + 9", 540, y0 + 50, 38, ep(t, C["25.a"], 0.4), hl={2: AMBER})
        m(c, "- (4x^2+12x+9)", 540, y0 + 115, 38, ep(t, C["25.b"], 0.4))
        acc = ep(t, C["25.c"], 0.4)
        if acc > 0:
            line(c, 260, y0 + 160, 820, y0 + 160, INK2, acc, 3)
            m(c, "= -24x", 540, y0 + 215, 50, acc, col=GREEN)
        ad = ep(t, C["25.d"], 0.4)
        if ad > 0:
            m(c, "x = 1:  1 - 25 = -24", 540, y0 + 300, 32, ad)
            conferido(c, "bateu", 260, y0 + 370, ep(t, C["25.ok"], 0.4), True, 26)


ALTS9 = [("A", "1", "sonho do calouro cúbico", RED), ("B", "3x + 1", "esqueceu o 3x²", RED),
         ("C", "= 3x^2 + 1", "esqueceu o 3x", RED), ("D", "= 3x^2 + 3x + 1", "", GREEN),
         ("E", "= x^3 + 3x^2 + 3x + 1", "volume novo inteiro", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "CUBO DA SOMA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("Um reservatório tem a forma de um cubo de aresta x metros. Num projeto de ampliação, a aresta "
                           "será aumentada em 1 metro. O acréscimo de volume, em metros cúbicos, será", INK)], a0, 230, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
         align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS9, 1000, 250, 680, 36, C["28.ok"], "D", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 150)
    if t >= C["28"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["28"], 0.4))
        aa = ep(t, C["28.a"], 0.4)
        cubo(c, 230, y0 + 120, 150, aa, BLUE)
        cubo(c, 230, y0 + 120 - 0, 200, aa, AMBER, dash=True)
        text(c, "x", 305, y0 + 300, 26, "black", BLUE, aa)
        text(c, "x + 1", 330, y0 + 350, 24, "black", AMBER, aa)
        m(c, "(x+1)^3 - x^3", 690, y0 + 80, 38, aa)
        ab = ep(t, C["28.b"], 0.4)
        if ab > 0:
            pill(c, "1 · 3 · 3 · 1", 690, y0 + 145, GREEN, size=24, a=ab, anchor="center")
        acc = ep(t, C["28.c"], 0.4)
        if acc > 0:
            m(c, "3x^2 + 3x + 1", 690, y0 + 215, 40, acc, col=GREEN)
        ad = ep(t, C["28.d"], 0.4)
        if ad > 0:
            text(c, "x = 2:  8 → 27,  +19", 690, y0 + 290, 26, "black", INK, ad)
            text(c, "12 + 6 + 1 = 19", 690, y0 + 335, 26, "black", GREEN, ad)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O CAMINHO DE VOLTA", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        m(c, "x^2 - 25", 620, 400, 90, aa)
        g = ep(t, C["31.a"] + 2.0, 0.6)
        arrow(c, 880, 400, 1080, 400, AMBER, g, 6, 22)
        m(c, "(?)(?)", 1360, 400, 90, g, col=AMBER)
        text(c, "de soma para MULTIPLICAÇÃO", W / 2, 560, 40, "black", PURPLE, ep(t, C["31.a"] + 3.0, 0.4))
    pill(c, "ep. 3 · fatoração e frações algébricas", W / 2, 720, PURPLE, size=32, a=ep(t, C["31.b"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já tinha caído no sonho do calouro?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, soma=b_soma, diferenca=b_diferenca,
              somadif=b_somadif, tabela=b_tabela, cubo=b_cubo, calouro=b_calouro, teste=b_teste, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q2=b_q2, q7=b_q7, q9=b_q9, ponte=b_ponte, cta=b_cta)
