"""Visual — Função Quadrática, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): parábolas sorrindo e triste · espelho dobrado · cercado
no muro · três crachás.
Ícones de área (area_icone()): foguete · etiqueta de preço · cercado · arco de portão · estufa · gráfico do lucro ·
velocímetro · quadrado.
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
_s = importlib.util.spec_from_file_location("comum040", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_quadratica_ep5_revisao.mp4"
CARD_R = K.CARD_R
METAL = "#9AA3AD"
TIJOLO = "#C46A4A"
VIDRO = "#CFE8F2"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'R$ 12', '30 m', '1 800' nem '8 h'"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(m²|m|s|h|L|°C|pizzas)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
    return s


def fit(c, s, x, y, size, maxw, peso, col, a, align="left"):
    """texto numa linha só, encolhendo até caber em maxw"""
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


def para_nb(c, s, x, y, size, peso, color, a, maxw, lh=None):
    """quebra de linha que respeita os espaços rígidos de nb()"""
    s = nb(s)
    lh = lh or size * 1.32
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and text_w(tst, peso, size) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    if a > 0:
        for k, ln in enumerate(out):
            text(c, ln, x, y + k * lh, size, peso, color, a, align="left")
    return len(out) * lh


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def arco(c, x0, y_base, w, h, col, a, width=6, triste=True):
    """parábola de (x0, y_base) a (x0 + w, y_base); vértice h acima (triste) ou abaixo (sorrindo) do meio"""
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(x0, y_base)
    p.quadTo(x0 + w / 2, y_base - 2 * h if triste else y_base + 2 * h, x0 + w, y_base)
    c.drawPath(p, paint(col, a, stroke=width))


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def duas_parabolas(c, a):
    """ep1: a parábola sorrindo (mínimo) e a triste (máximo)"""
    arco(c, -180, -80, 150, 110, GREEN, a, 8, triste=False)
    c.drawCircle(-105, 30, 12, paint(GREEN, a))
    ftext(c, "mín", -105, 100, 30, "black", GREEN, a, align="center")
    arco(c, 30, 60, 150, 110, PURPLE, a, 8, triste=True)
    c.drawCircle(105, -50, 12, paint(PURPLE, a))
    ftext(c, "máx", 105, -80, 30, "black", PURPLE, a, align="center")
    line(c, -200, 130, 200, 130, INK2, a, 4)


def espelho(c, a):
    """ep2: a folha dobrada no eixo de simetria, o vértice no meio das raízes"""
    rrect(c, -170, -150, 340, 300, 14, "#FFFFFF", a, shadow=True)
    line(c, 0, -140, 0, 140, AMBER, a, 4, dash=[12, 8])
    line(c, -150, 90, 150, 90, INK2, a, 3)
    arco(c, -120, 90, 240, 100, PURPLE, a, 7)
    for x in (-120, 120):
        c.drawCircle(x, 90, 11, paint(RED, a))
    c.drawCircle(0, -10, 12, paint(BLUE, a))
    arrow(c, -60, 120, -10, 120, AMBER, a, 4, 10)
    arrow(c, 60, 120, 10, 120, AMBER, a, 4, 10)


def cercado(c, a):
    """ep3: o cercado encostado no muro (três lados de tela)"""
    for k in range(6):
        rrect(c, -190 + k * 64, -150, 60, 34, 4, TIJOLO, a)
    for k in range(5):
        rrect(c, -158 + k * 64, -112, 60, 34, 4, TIJOLO, a)
    pts = [(-150, -78), (-150, 120), (150, 120), (150, -78)]
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        line(c, xa, ya, xb, yb, GREEN, a, 8, dash=[16, 8])
    for (x, y) in pts:
        c.drawCircle(x, y, 9, paint(INK2, a))
    rrect(c, -110, -40, 220, 120, 10, mix("#FFFFFF", GREEN, 0.2), a)
    ftext(c, "x", -175, 30, 34, "black", BLUE, a, align="center")
    ftext(c, "x", 175, 30, 34, "black", BLUE, a, align="center")


def crachas(c, a):
    """ep4: as três fotos (crachás) da mesma função"""
    for k, (s, col) in enumerate((("geral", BLUE), ("fatorada", RED), ("canônica", PURPLE))):
        x = -150 + k * 150
        rrect(c, x - 62, -110, 124, 200, 14, "#FFFFFF", a, shadow=True)
        rrect(c, x - 62, -110, 124, 40, 14, col, a)
        rrect(c, x - 20, -128, 40, 26, 6, METAL, a)
        arco(c, x - 40, 30, 80, 50, col, a, 5)
        ftext(c, s, x, 75, 21, "black", col, a, align="center")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (duas_parabolas, espelho, cercado, crachas)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def foguete(c, a):
    rrect(c, -40, -120, 80, 180, 30, mix("#FFFFFF", BLUE, 0.35), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-40, -120, 80, 180), 30, 30), paint(INK2, a, stroke=4))
    p = skia.Path(); p.moveTo(-40, 30); p.lineTo(-80, 80); p.lineTo(-40, 60); p.close(); c.drawPath(p, paint(RED, a))
    p = skia.Path(); p.moveTo(40, 30); p.lineTo(80, 80); p.lineTo(40, 60); p.close(); c.drawPath(p, paint(RED, a))
    for k in range(3):
        c.drawCircle(-20 + k * 20, 95 + (k % 2) * 16, 12, paint(mix("#FFFFFF", BLUE, 0.6), a))
    arrow(c, 110, 60, 110, -130, GREEN, a, 7, 18)


def etiqueta(c, a):
    p = skia.Path(); p.moveTo(-160, -70); p.lineTo(90, -70); p.lineTo(160, 0); p.lineTo(90, 70); p.lineTo(-160, 70); p.close()
    c.drawPath(p, paint(AMBER, a))
    c.drawCircle(95, 0, 14, paint("#FFFFFF", a))
    ftext(c, "R$", -60, 22, 64, "black", "#FFFFFF", a, align="center")


def portao(c, a):
    rrect(c, -170, 100, 340, 22, 6, METAL, a)
    arco(c, -140, 100, 280, 110, PURPLE, a, 10)
    line(c, 0, 100, 0, -10, AMBER, a, 4, dash=[10, 7])
    for x in (-140, 140):
        c.drawCircle(x, 100, 11, paint(RED, a))


def estufa(c, a):
    p = skia.Path(); p.moveTo(-170, 120); p.lineTo(-170, -10); p.quadTo(0, -170, 170, -10); p.lineTo(170, 120); p.close()
    c.drawPath(p, paint(VIDRO, a))
    c.drawPath(p, paint(INK2, a, stroke=5))
    for x in (-60, 60):
        line(c, x, 120, x, -75 if x else -90, INK2, a, 3)
    for k, x in enumerate((-110, 0, 110)):
        rrect(c, x - 14, 60, 28, 50, 6, GREEN, a)
    rrect(c, 120, -60, 26, 120, 13, "#FFFFFF", a)
    rrect(c, 127, -10, 12, 70, 6, RED, a)


def grafico_lucro(c, a):
    arrow(c, -180, 110, 190, 110, INK2, a, 4, 12)
    arrow(c, -160, 150, -160, -160, INK2, a, 4, 12)
    arco(c, -110, 110, 260, 110, GREEN, a, 7)
    c.drawCircle(20, 0, 13, paint(AMBER, a))
    ftext(c, "L", -190, -130, 30, "black", INK2, a, align="center")


def velocimetro(c, a):
    p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(-150, -150, 300, 300), 180, 180)
    c.drawPath(p, paint(INK2, a, stroke=16))
    p2 = skia.Path(); p2.addArc(skia.Rect.MakeXYWH(-150, -150, 300, 300), 180, 120)
    c.drawPath(p2, paint(PURPLE, a, stroke=16))
    line(c, 0, 0, 80, -100, RED, a, 9)
    c.drawCircle(0, 0, 18, paint(INK, a))
    rrect(c, -150, 40, 300, 22, 8, METAL, a)


def quadrado(c, a):
    rrect(c, -120, -120, 240, 240, 8, mix("#FFFFFF", GREEN, 0.25), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-120, -120, 240, 240), 8, 8), paint(GREEN, a, stroke=8))
    ftext(c, "ℓ", 0, 165, 40, "black", GREEN, a, align="center")
    ftext(c, "ℓ", 160, 14, 40, "black", GREEN, a, align="center")


AREA_F = (foguete, etiqueta, cercado, portao, estufa, grafico_lucro, velocimetro, quadrado)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# abertura
# ======================================================================

def mx(c, s, x, cy, size, col=INK, a=1.0, align="center"):
    """texto matemático de uma cor (sem quebrar)"""
    fmid(c, nb(s), x, cy, size, "black", col, a)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        x0, yb = 260, 680
        arrow(c, x0 - 40, yb, x0 + 640, yb, INK2, aa, 4, 12)
        arrow(c, x0, yb + 30, x0, 200, INK2, aa, 4, 12)
        arco(c, x0 + 60, yb, 480, 230, PURPLE, aa, 8)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        xv, yv = 260 + 60 + 240, 680 - 230
        line(c, xv, yv, xv, 680, BLUE, ab, 5, dash=[12, 8])
        line(c, xv, yv, 260, yv, RED, ab, 5, dash=[12, 8])
        c.drawCircle(xv, yv, 16, paint(INK, ab))
        pill(c, "x do vértice", xv, 730, BLUE, size=28, a=ab, anchor="center")
        pill(c, "y do vértice", 260, yv - 50, RED, size=28, a=ab, bounds=(0, 1920))
    # as alternativas: as duas respostas estão lá, de propósito
    for k, L in enumerate("ABCDE"):
        a, d = rise(t, C["01.b"] + 0.15 * k)
        if a <= 0:
            continue
        y = 220 + k * 104
        rrect(c, 1080, y + d, 560, 88, 16, "#FFFFFF", a, shadow=True)
        badge_num(c, L, 1125, y + 44 + d, a, 24, bg=INK)
        if L == "B":
            pill(c, "x do vértice", 1180, y + 44 + d, BLUE, size=28, a=a, bounds=(0, 1920))
        elif L == "D":
            pill(c, "y do vértice", 1180, y + 44 + d, RED, size=28, a=a, bounds=(0, 1920))
        else:
            rrect(c, 1180, y + 34 + d, 260, 20, 10, LIGHT, a)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        selo(c, 1360, 800, ac, "QUAL FOI PEDIDA?", AMBER, -5, 34)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 430, 820, AMBER, ad, 30)
    chip(c, "5 QUESTÕES NOVAS", 850, 820, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 30)


COBRA = [("02.a", "MAXIMIZAR OU MINIMIZAR", "preço · área · custo", BLUE, 1),
         ("02.b", "TRAJETÓRIAS", "a altura de uma bola", AMBER, 0),
         ("02.c", "LER E MONTAR A LEI", "o arco de uma ponte", PURPLE, 3),
         ("02.d", "O SINAL", "quando o lucro é positivo?", GREEN, 5)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "QUATRO FORMAS", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 250 + d, 410, 500, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 30, "black", col, a, 360, 38, align="center")
        area_icone(c, ic, x, 560 + d, 0.42, a)
        para(c, sub, x, 690 + d, 26, "bold", INK2, a, 360, 32, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "SAIBA DE COR", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 380, 210, 760, 150, 24, mix("#FFFFFF", PURPLE, 0.12), aa, shadow=True)
        mx(c, "xV = −b ÷ 2a", W / 2, 285, 70, PURPLE, aa)
    for k, (cue, s, tit, sub, col) in enumerate((("03.b", "x do vértice", "ONDE", "qual preço · qual medida · qual instante", BLUE),
                                                 ("03.c", "y do vértice", "QUANTO", "qual receita · qual área · qual altura", RED))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 620 + k * 680
        rrect(c, x - 300, 420 + d, 600, 300, 24, mix("#FFFFFF", col, 0.10), a)
        text_mid(c, s, x, 480 + d, 40, "black", col, a)
        fmid(c, tit, x, 570 + d, 74, "black", col, a)
        para(c, sub, x, 650 + d, 28, "bold", INK, a, 540, 34, align="center")


INDICE = [("EP. 1", "sorrindo = mínimo · triste = máximo · o Δ conta os toques no chão · o a anda com o x²"),
          ("EP. 2", "o espelho dobrado · x = onde · y = quanto · o gráfico não é o caminho"),
          ("EP. 3", "o cercado no muro · o cabo de guerra: o produto tem topo"),
          ("EP. 4", "três fotos da mesma pessoa · triste é positiva no meio · nunca divida por x")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 285 + k * 450
        y = 210
        rrect(c, x - 205, y, 410, 620, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 205, y, 410, 620), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 180, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 200, 0.62, a)
        yy = y + 340
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 26, "black", INK if on_ else INK2, a, 360, 32, align="center") + 10


ONDE = [("06.a", "FÍSICA (MUV)", 0, "s = s₀ + v₀t + at²/2", "altura máxima = vértice", BLUE),
        ("06.b", "ECONOMIA", 5, "L = R − C", "o máximo do LUCRO", GREEN),
        ("07.c", "GEOMETRIA", 7, "perímetro fixo", "sem muro → quadrado", PURPLE),
        ("07.d", "ENERGIA", 6, "Ec = mv²/2", "um ramo de parábola", RED)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA PARÁBOLA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 220 + d, 410, 520, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 28, "black", col, a, 360, 34, align="center")
        area_icone(c, ic, x, 440 + d, 0.42, a)
        fit(c, lei_, x, 610 + d, 34, 370, "black", INK, a, align="center")
        para(c, res, x, 660 + d, 26, "bold", INK2, a, 360, 32, align="center")
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        boxed(c, 460, 790, 1000, 80, AMBER, ae, 0.10)
        text_mid(c, "lançamento oblíquo → fica para a Física", W / 2, 830, 34, "black", INK, ae)


HABITOS = [("08.a", "1", "SUBLINHE O QUE É PEDIDO", "“qual preço”, “em que instante” → x · “qual a receita”, “qual a altura” → y"),
           ("08.b", "2", "RAÍZES PRIMEIRO, VÉRTICE NO MEIO", "x(60 − 2x): raízes 0 e 30 · vértice em 15"),
           ("09.c", "3", "TESTE AS ALTERNATIVAS", "sinal de a · o c · as raízes")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS NA HORA H", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 380 + k * 580
        rrect(c, x - 260, 240 + d, 520, 540, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 310 + d, a, 34, bg=GREEN)
        para(c, tit, x, 400 + d, 32, "black", GREEN, a, 460, 40, align="center")
        yy = 540 + d
        for ln in sub.split(" · "):
            yy += para(c, nb(ln), x, yy, 28, "bold", INK, a, 460, 36, align="center") + 12


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


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("o sinal de menos", "x² − 6x + 1 → xV = b ÷ 2a = −3", False, "a fórmula parece completa",
     "faltou o menos: −b ÷ 2a", "xV = 3", 1),
    ("a média das raízes", "x² − 10x + 9 (raízes 1 e 9) → xV = 5", True, "−b ÷ a dá 10",
     "10 é a soma das raízes · o vértice é a média", "xV = 5", 1),
    ("quando × quanto", "h(t) = 50t − 5t² → altura máxima = 5", False, "é a primeira conta que sai",
     "5 s é o quando · a altura é o quanto: h(5)", "125 m", 1),
    ("quem é o a", "h = 24t − 4t² → a = 24", False, "é o primeiro número da lei",
     "o a anda com o t², esteja onde estiver", "a = −4", 0),
    ("máximo ou mínimo", "2x² − 8x + 3 tem máximo", False, "a positivo parece “subir até um máximo”",
     "a > 0 sorri: o vértice é o fundo", "mínimo", 0),
    ("Δ negativo", "x² + 2x + 5: Δ < 0 → positiva para todo x", True, "Δ negativo parece “função negativa”",
     "Δ < 0 = zero toques no chão · fica do lado do sinal de a", "a > 0: sempre +", 0),
    ("nunca divida por x", "x² > 6x → x < 0 ou x > 6", True, "dividindo por x, sobra só x > 6",
     "x pode ser negativo: nunca divida por x", "x < 0 ou x > 6", 3),
    ("o muro", "48 m de tela + muro → o quadrado 16 × 16 é o maior", False, "o quadrado é o campeão sem muro",
     "com muro, monte a área: x(48 − 2x) · 12 × 24", "288 m² > 256", 2),
    ("o gráfico", "o gráfico altura × tempo é o caminho da bola", False, "o desenho tem forma de arco",
     "a bola sobe e desce em linha reta · o gráfico é a altura em cada instante", "não é o caminho", 1),
]
VF_IDS = [f"{11 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 62 + k * 62, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 410, 0.55, a0)
    text(c, ctx.upper(), 960, 300, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    s = nb(conta)
    sz = 44
    while ftw(s, sz) > 760 and sz > 38:
        sz -= 2
    lines = [s] if ftw(s, sz) <= 760 else _quebra(s, sz, 760)
    riscos = []
    for j, ln in enumerate(lines):
        yj = 410 + (j - (len(lines) - 1) / 2) * (sz + 12)
        fmid(c, ln, 960, yj, sz, "black", INK, a0)
        riscos.append((ftw(ln, sz), yj + 4))
    if ar > 0 and not ver:
        for w, yl in riscos:
            strike(c, 960 - w / 2 - 10, yl, 960 + w / 2 + 10, yl, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        fit(c, engana, 640 if ver else 520, 552, 34, 1020 if ver else 1140, "bold", INK2, ae)
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        lns = []
        for parte in regra_.split(" · "):
            lns += _quebra(nb(parte), 30, 820)
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 725 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        fit(c, fix, 1420, 735, 52, 500, "black", GREEN, ag, align="center")


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
        rrect(c, W / 2 - 400, 700, 800, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "sublinhe: pedem o x ou o y?", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

def fig_arco(c, x0, yb, w, a):
    """o arco do portão da Q4: só os dados do enunciado (pés em −1 e 3, topo de 8 m)"""
    if a <= 0:
        return
    X = lambda v: x0 + w * (v + 2) / 6
    arrow(c, x0, yb, x0 + w + 20, yb, INK2, a, 4, 12)
    arrow(c, X(0), yb + 20, X(0), yb - 250, INK2, a, 4, 12)
    arco(c, X(-1), yb, X(3) - X(-1), 105, PURPLE, a, 7)
    line(c, X(1), yb - 210, X(1), yb, AMBER, a, 3, dash=[10, 7])
    ftext(c, "8 m", X(1) + 14, yb - 120, 26, "black", AMBER, a, align="left")
    for v in (-1, 3):
        c.drawCircle(X(v), yb, 11, paint(RED, a))
        ftext(c, str(v).replace("-", "−"), X(v), yb + 36, 26, "black", RED, a, align="center")
    ftext(c, "x", x0 + w + 30, yb + 10, 26, "black", INK2, a, align="left")


Q = {
    "q1": dict(ids=("21", "22"), titulo="O FOGUETE DE GARRAFA", area="ALTURA MÁXIMA", ic=0, ok="C", fig=None,
               enun=[("a", "Um foguete de garrafa PET é lançado verticalmente do chão: h(t) = 40t − 5t² (h em metros, t em segundos).", False),
                     ("b", "A ALTURA MÁXIMA é:", True)],
               alts=[("A", "4 m", "o instante", AMBER), ("B", "8 m", "a volta ao chão", RED),
                     ("C", "80 m", "", GREEN), ("D", "160 m", "esqueceu o −5t²", RED),
                     ("E", "320 m", "40 · 8", RED)],
               passos=[("d", "pedem o y do vértice: a altura"), ("a", "a = −5 · b = 40 → t = 40 ÷ 10 = 4 s"),
                       ("b", "h(4) = 160 − 80 = 80 m")],
               confere=("v", "volta ao chão em 8 s: o 4 é o meio")),
    "q2": dict(ids=("23", "24"), titulo="A PIZZARIA", area="RECEITA MÁXIMA", ic=1, ok="D", fig=None,
               enun=[("a", "200 pizzas por semana a R$ 50,00. Cada R$ 1,00 de desconto vende 10 pizzas a mais. O forno assa até 400.", False),
                     ("b", "Para a maior receita, o PREÇO deve ser:", True)],
               alts=[("A", "R$ 15,00", "o desconto", AMBER), ("B", "R$ 20,00", "−b ÷ a", RED),
                     ("C", "R$ 25,00", "a raiz −20 virou 0", RED), ("D", "R$ 35,00", "", GREEN),
                     ("E", "R$ 65,00", "sinal trocado", RED)],
               passos=[("d", "pedem o preço, não o desconto"), ("a", "R = (50 − x)(200 + 10x)"),
                       ("b", "raízes 50 e −20 → meio: x = 15"), ("b", "preço: 50 − 15 = R$ 35,00")],
               confere=("v", "350 pizzas ≤ 400: cabe no forno")),
    "q3": dict(ids=("25", "26"), titulo="O CERCADO NO MURO", area="ÁREA MÁXIMA", ic=2, ok="E", fig=None,
               enun=[("a", "120 m de tela para um cercado retangular. Um lado fica encostado no muro, sem tela.", False),
                     ("b", "A maior área possível, em m², é:", True)],
               alts=[("A", "30", "a lateral: o x", AMBER), ("B", "60", "a frente", RED),
                     ("C", "900", "quadrado, 4 lados", RED), ("D", "1 600", "quadrado com muro", AMBER),
                     ("E", "1 800", "", GREEN)],
               passos=[("d", "frente = 120 − 2x"), ("a", "A = x(120 − 2x): raízes 0 e 60"),
                       ("a", "meio: x = 30 · frente 60"), ("b", "área = 30 · 60 = 1 800 m²")],
               confere=None),
    "q4": dict(ids=("27", "28"), titulo="O ARCO DO PORTÃO", area="LEI PELO GRÁFICO", ic=3, ok="A", fig="arco",
               enun=[("a", "O arco de um portão é uma parábola: toca o chão em x = −1 e x = 3 e tem altura máxima de 8 m.", False),
                     ("b", "A lei do arco é:", True)],
               alts=[("A", "−2x² + 4x + 6", "", GREEN), ("B", "−2x² − 4x + 6", "raízes 1 e −3", RED),
                     ("C", "x² − 2x − 3", "esqueceu o a", RED), ("D", "2x² − 4x − 6", "boca para cima", RED),
                     ("E", "−2x² + 4x + 8", "topo usado como c", AMBER)],
               passos=[("d", "hábito 3: teste as alternativas"), ("a", "arco tem topo: a < 0 → caem C e D"),
                       ("b", "raízes −1 e 3: cai a B · vértice em x = 1"), ("c", "x = 1: A dá 8 · E dá 10")],
               confere=None),
    "q5": dict(ids=("29", "30"), titulo="A ESTUFA", area="O SINAL COM a < 0", ic=4, ok="B", fig=None,
               enun=[("a", "Numa estufa, T(t) = −t² + 12t + 8 (em °C), com t em horas a partir das 6 h.", False),
                     ("b", "A temperatura fica ACIMA de 28 °C:", True)],
               alts=[("A", "antes das 8 h ou depois das 16 h", "sinal invertido", RED), ("B", "entre 8 h e 16 h", "", GREEN),
                     ("C", "a partir das 8 h", "tratou como reta", RED), ("D", "entre 8 h e 12 h", "parou no vértice", AMBER),
                     ("E", "entre 6 h e 18 h", "−b ÷ a = 12", RED)],
               passos=[("d", "t² − 12t + 20 = 0 → t = 2 ou t = 10"), ("a", "a < 0: positiva no meio"),
                       ("b", "2 < t < 10: das 8 h às 16 h")],
               confere=None),
}


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
        K.alternativas(c, t, C, [(L, nb(s), w, col) for L, s, w, col in d["alts"]], 880, 230, 820, 30,
                       C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        area_icone(c, d["ic"], 770, 222, 0.30, a0 * (1 - sol))
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            if d["fig"] == "arco" and dest:
                y = 690
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        if d["fig"] == "arco":
            fig_arco(c, 250, 650, 420, ep(t, C[f"{s1}.a"] + 0.6, 0.5) * (1 - sol))
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720 if d["fig"] == "arco" else 500, 470 if d["fig"] == "arco" else 760)
        if sol > 0:
            yy = 300
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.6 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 34, 640, "black", GREEN if last else INK, a)
                yy += 66
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["a, b e c pela potência", "concavidade e corte no eixo y", "raízes e Δ"]),
         ("31.c", "EP. 2", 1, ["vértice: −b ÷ 2a e f(xV)", "simetria e imagem", "lançamentos"]),
         ("32.a", "EP. 3", 2, ["montar a função a otimizar", "pedem o x ou o y?", "o vértice cabe no problema?"]),
         ("32.b", "EP. 4", 3, ["lei pelas raízes ou pelo vértice", "sinal e inequações sem dividir por x"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 210), (150, 470), (990, 210), (990, 470)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, ic, x + 40, y0 + 100, 0.2, a)
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 50
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            fit(c, it, x + 158, yy + 10, 28, 600, "bold", INK, a)
    ae = ep(t, C["32.c"], 0.5)
    if ae > 0:
        boxed(c, 560, 740, 800, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", W / 2, 790, 34, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["33.a"], 0.5)
    ab = ep(t, C["33.b"], 0.5)
    ac = ep(t, C["33.c"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["33.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 200 + k * 82, 230 + r_ * 90
        col = mix("#E6E6E2", GREEN, ab if ok else 0)
        rrect(c, x, y, 66, 72, 12, col, a)
        if ac > 0 and i < 10:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 74, 80), 14, 14), paint(BLUE, ac, stroke=4))
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 400, 46, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 200, 580, 1520, 180, BLUE, ac, 0.08)
        area_icone(c, 1, 330, 670, 0.32, ac)
        text_mid(c, "10 DE OTIMIZAÇÃO EM CONTEXTO", 1060, 640, 44, "black", BLUE, ac)
        text_mid(c, "preço · área · altura", 1060, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Função exponencial", W / 2, 330, 62, "black", PURPLE, aa)
    text(c, "crescimento e decaimento", W / 2, 400, 36, "bold", INK2, aa)
    cols = [("34.b", "AFIM", "+3 · +3 · +3", BLUE, (1, 4, 7, 10)),
            ("34.c", "QUADRÁTICA", "+1 · +3 · +5", AMBER, (1, 2, 5, 10)),
            ("34.d", "EXPONENCIAL", "×2 · ×2 · ×2", GREEN, (1, 2, 4, 8))]
    for k, (cue, tit, passo, col, vals) in enumerate(cols):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 460 + d, 480, 380, 24, mix("#FFFFFF", col, 0.10), a)
        text_mid(c, tit, x, 510 + d, 34, "black", col, a)
        top = max(vals)
        for j, v in enumerate(vals):
            hh = 180 * v / top
            rrect(c, x - 170 + j * 90, 740 + d - hh, 70, hh, 8, col, a)
        text_mid(c, passo, x, 795 + d, 30, "black", INK, a)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
