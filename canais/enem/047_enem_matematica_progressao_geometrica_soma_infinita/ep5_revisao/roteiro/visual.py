"""Visual — Progressão Geométrica, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): máquina ×q · árvore da corrente · bola quicando ·
carro com a etiqueta de preço caindo.
Ícones de área (area_icone()): remédio · grupo · bola · tabela · dízima · átomo · célula · moeda · som.
Índices e potências (a₁, 2⁶, 0,9ⁿ) só passam por ftext/fmid/fit (nunca text, pill, chip, head).
Cores com função: azul = definição · roxo = regra, fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum047", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_progressao_geometrica_ep5_revisao.mp4"
CARD_R = K.CARD_R


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'R$ 30', '320 mg', '10 m', '1 024' nem '8 h'"""
    s = re.sub(r"(?<=\$) (?=\d)", " ", s)
    s = re.sub(r"(?<=\d) (?=(mg|m|h|dB|%|vezes|termos|semanas|pessoas|anos)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
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


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def maquina_ic(c, a):
    """ep1: a máquina de multiplicar ×q"""
    line(c, -230, 70, 230, 70, INK2, a, 5)
    rrect(c, -110, -110, 220, 170, 24, PURPLE, a, shadow=True)
    ftext(c, "×q", 0, 10, 90, "black", "#FFFFFF", a, align="center")
    rrect(c, -220, 20, 80, 50, 10, "#FFFFFF", a, stroke=4, stroke_color=BLUE)
    ftext(c, "3", -180, 58, 34, "black", BLUE, a, align="center")
    rrect(c, 140, 20, 80, 50, 10, "#FFFFFF", a, stroke=4, stroke_color=GREEN)
    ftext(c, "6", 180, 58, 34, "black", GREEN, a, align="center")


def arvore_ic(c, a):
    """ep2: a árvore da corrente (1 → 2 → 4)"""
    pts = [[(0, -140)], [(-110, -20), (110, -20)], [(-165, 110), (-55, 110), (55, 110), (165, 110)]]
    for n in range(2):
        for k, (x, y) in enumerate(pts[n]):
            for (x2, y2) in pts[n + 1][2 * k:2 * k + 2]:
                line(c, x, y, x2, y2, INK2, a, 4)
    for n, nivel in enumerate(pts):
        col = (BLUE, PURPLE, GREEN)[n]
        for (x, y) in nivel:
            c.drawCircle(x, y - 14, 16, paint(col, a))
            rrect(c, x - 26, y + 4, 52, 30, 14, col, a)


def bola_ic(c, a):
    """ep3: a bola que quica (cada altura duas vezes)"""
    line(c, -230, 140, 230, 140, INK2, a, 5)
    p = skia.Path(); p.moveTo(-200, -150)
    x, h = -200, 290
    for _ in range(4):
        p.lineTo(x + 30, 140)
        h *= 0.55
        p.quadTo(x + 30 + 50, 140 - 2 * h, x + 130, 140)
        x += 100
    c.drawPath(p, paint(BLUE, a, stroke=5))
    c.drawCircle(-200, -165, 26, paint(AMBER, a))


def carro_ic(c, a):
    """ep4: o carro com a etiqueta de preço caindo"""
    rrect(c, -210, 0, 420, 100, 30, BLUE, a, shadow=True)
    p = skia.Path(); p.moveTo(-130, 0); p.lineTo(-80, -70); p.lineTo(90, -70); p.lineTo(140, 0); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.7), a))
    for x in (-120, 120):
        c.drawCircle(x, 105, 38, paint(INK, a)); c.drawCircle(x, 105, 15, paint(LIGHT, a))
    rrect(c, 110, -190, 150, 80, 12, AMBER, a)
    ftext(c, "−20%", 185, -136, 34, "black", "#FFFFFF", a, align="center")
    arrow(c, 185, -100, 185, -60, RED, a, 5, 14)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (maquina_ic, arvore_ic, bola_ic, carro_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def remedio_ic(c, a):
    c.save(); c.rotate(-30)
    rrect(c, -160, -60, 160, 120, 60, RED, a)
    rrect(c, 0, -60, 160, 120, 60, "#FFFFFF", a, stroke=6, stroke_color=RED)
    c.restore()
    ftext(c, "½", 0, 150, 70, "black", BLUE, a, align="center")


def grupo_ic(c, a):
    for k, (x, y, col) in enumerate(((0, -90, BLUE), (-120, 60, PURPLE), (120, 60, PURPLE))):
        c.drawCircle(x, y - 30, 36, paint(col, a))
        rrect(c, x - 56, y + 10, 112, 70, 34, col, a)
    for x2 in (-120, 120):
        arrow(c, 0, -20, x2 * 0.7, 40, GREEN, a, 4, 12)


def bola_area(c, a):
    bola_ic(c, a)


def tabela_ic(c, a):
    rrect(c, -170, -150, 340, 300, 18, "#FFFFFF", a, shadow=True)
    for k, (n, v) in enumerate((("0", "600"), ("1", "540"), ("2", "486"))):
        y = -80 + k * 80
        ftext(c, n, -110, y + 14, 38, "black", GRAY, a, align="center")
        ftext(c, v, 60, y + 14, 42, "black", INK, a, align="center")
        line(c, -150, y + 40, 150, y + 40, LIGHT, a, 2)
    ftext(c, "×0,9", 120, 190, 40, "black", GREEN, a, align="center")


def dizima_ic(c, a):
    rrect(c, -180, -100, 360, 200, 30, mix("#FFFFFF", PURPLE, 0.15), a, shadow=True)
    ftext(c, "0,3636…", 0, 30, 76, "black", PURPLE, a, align="center")


def atomo_ic(c, a):
    for ang in (0, 60, 120):
        c.save(); c.rotate(ang)
        c.drawOval(skia.Rect.MakeXYWH(-170, -60, 340, 120), paint(BLUE, a, stroke=6))
        c.restore()
    c.drawCircle(0, 0, 34, paint(RED, a))


def celula_ic(c, a):
    for x in (-80, 80):
        c.drawCircle(x, 0, 90, paint(mix("#FFFFFF", GREEN, 0.4), a))
        c.drawCircle(x, 0, 90, paint(GREEN, a, stroke=6))
        c.drawCircle(x, 0, 28, paint(PURPLE, a))
    ftext(c, "2ⁿ", 0, 170, 60, "black", GREEN, a, align="center")


def moeda(c, a):
    c.drawCircle(0, 0, 140, paint(AMBER, a))
    c.drawCircle(0, 0, 112, paint(mix(AMBER, INK, 0.25), a, stroke=8))
    ftext(c, "R$", 0, 26, 86, "black", "#FFFFFF", a, align="center")


def som_ic(c, a):
    rrect(c, -170, -50, 70, 100, 10, INK2, a)
    p = skia.Path(); p.moveTo(-100, -50); p.lineTo(-30, -120); p.lineTo(-30, 120); p.lineTo(-100, 50); p.close()
    c.drawPath(p, paint(INK2, a))
    for k, r in enumerate((60, 110, 160)):
        c.drawArc(skia.Rect.MakeXYWH(-30 - r, -r, 2 * r, 2 * r), -45, 90, False, paint(BLUE, a, stroke=8))
    ftext(c, "dB", 120, 170, 44, "black", BLUE, a, align="center")


AREA_F = (remedio_ic, grupo_ic, bola_area, tabela_ic, dizima_ic, atomo_ic, celula_ic, moeda, som_ic)


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
    for k, (s, ic, kind, col) in enumerate((("bactérias", 6, "a", GREEN), ("remédios", 0, "a", RED),
                                             ("dinheiro", 7, "a", AMBER), ("bola quicando", 2, "a", BLUE))):
        a, d = rise(t, C["01.a"] + 0.6 * k)
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 200 + d, 380, 260, 26, mix("#F7F7F5", col, 0.12), a)
        area_icone(c, ic, x, 300 + d, 0.36, a)
        fit(c, s, x, 425 + d, 32, 340, "black", col, a, align="center")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 500, 1200, 100, 50, mix("#FFFFFF", PURPLE, 0.20), ab, shadow=True)
        text_mid(c, "cresce ou diminui por um fator fixo", W / 2, 550, 46, "black", PURPLE, ab)
    for k, s in enumerate(("TERMO", "SOMA", "SOMA INFINITA")):
        chip(c, s, 480 + k * 480, 690, (BLUE, GREEN, PURPLE)[k], ep(t, C["01.c"] + 1.6 + 0.5 * k, 0.4), 36)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "9 V OU F", 640, 840, AMBER, ad, 26)
        chip(c, "5 QUESTÕES NOVAS", 1280, 840, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 26)


COBRA = [("02.a", "CRESCIMENTO POR FATOR", "dobra · repassa", GREEN, 6),
         ("02.b", "DECAIMENTO", "meia-vida · depreciação", RED, 0),
         ("02.c", "SOMA FINITA", "o total da corrente", BLUE, 1),
         ("02.d", "SOMA INFINITA", "a bola até parar · dízimas", PURPLE, 2)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "QUATRO FORMAS", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 250 + d, 380, 500, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 30, "black", col, a, 340, 38, align="center")
        area_icone(c, ic, x, 570 + d, 0.42, a)
        fit(c, sub, x, 715 + d, 28, 340, "black", INK2, a, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "DUAS HABILIDADES", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate((("03.a", "CONTAR OS PERÍODOS", "a cada 20 min, por 2 h: 6 vezes ×2", PURPLE, 0),
                                                  ("03.b", "RECONHECER A SOMA INFINITA", "−1 < q < 1  →  S∞ = a₁ ÷ (1 − q)", GREEN, 2))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 290
        rrect(c, 200, y + d, 1520, 250, 26, mix("#F7F7F5", col, 0.10), a, shadow=True)
        badge_num(c, k + 1, 280, y + 125 + d, a, 36, bg=col)
        icone(c, ic, 480, y + 125 + d, 0.48, a)
        fit(c, tit, 680, y + 115 + d, 54, 1000, "black", col, a)
        fit(c, sub, 680, y + 182 + d, 38, 1000, "bold", INK2, a)


INDICE = [("EP. 1", "a máquina ×q · do 1º ao 6º, age 5 vezes · na PG se tira a raiz"),
          ("EP. 2", "a PA com soma trocada por × · x/q, x, x·q · as parcelas deslizam"),
          ("EP. 3", "metade do que sobrou · a fórmula com freio · a bola: o resto 2 vezes"),
          ("EP. 4", "o fator é o que sobra · conte os períodos antes da conta")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 300, 380, 1320, 160, 30, "#FFFFFF", aq, shadow=True)
        fmid(c, "do 1º ao 6º termo: quantas vezes ×q?", W / 2, 460, 52, "black", INK, aq)
        pause_timer(c, t, C["04.t"] + 2.4, 1500, 640, a=aq)
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
        icone(c, k, x, y + 210, 0.62, a)
        yy = y + 380
        for ln in s.split(" · "):
            yy += para_nb(c, ln, x, yy, 26, "black", INK if on_ else INK2, a, 330, 32, align="center") + 10


ONDE = [("06.a", "QUÍMICA", 5, "meia-vida", "a massa do isótopo ÷ 2", BLUE),
        ("06.b", "BIOLOGIA", 6, "mitose: 2ⁿ", "pirâmide de energia: q ≈ 0,1", GREEN),
        ("07.c", "FINANCEIRA", 7, "juros compostos", "montantes em PG de razão 1 + i", AMBER),
        ("07.d", "FÍSICA", 8, "decibéis", "+10 dB → intensidade ×10", PURPLE)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA MÁQUINA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 220 + d, 380, 600, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 30, "black", col, a, 360, 36, align="center")
        area_icone(c, ic, x, 450 + d, 0.42, a)
        fit(c, lei_, x, 630 + d, 34, 340, "black", INK, a, align="center")
        para_nb(c, res, x, 685 + d, 26, "bold", INK2, a, 340, 32, align="center")


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS NA HORA H", GREEN)
    a, d = rise(t, C["08.a"])
    if a > 0:
        rrect(c, 120, 230 + d, 1000, 600, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, 1, 190, 300 + d, a, 34, bg=GREEN)
        fit(c, "CONTE OS PERÍODOS COM CALMA", 250, 315 + d, 40, 840, "black", GREEN, a)
        rrect(c, 170, 380 + d, 900, 230, 18, "#FFFFFF", a, shadow=True)
        fit(c, "meia-vida de 8 h · em 2 dias", 620, 450 + d, 38, 820, "black", INK, a, align="center")
        a2 = ep(t, C["08.a2"], 0.4) * a
        if a2 > 0:
            fit(c, "2 dias = 48 h", 400, 540 + d, 40, 400, "black", BLUE, a2, align="center")
            arrow(c, 600, 528 + d, 700, 528 + d, GREEN, a2, 5, 14)
            fit(c, "48 ÷ 8 = 6", 860, 540 + d, 44, 340, "black", GREEN, ep(t, C["08.a2"] + 1.2, 0.4) * a)
            selo(c, 620, 720 + d, ep(t, C["08.a2"] + 2.4, 0.4) * a, "O EXPOENTE = QUANTAS VEZES", AMBER, -2, 28)
    for k, (cue, n, tit, sub) in enumerate((("09.b", "2", "TERMO, SOMA OU SOMA ∞?", "“no fim” → termo | “ao todo” → soma | “até parar” → soma ∞"),
                                            ("09.c", "3", "USE AS POTÊNCIAS DADAS", "deu 2¹⁰ = 1 024? | a conta usa esse número"))):
        ak, dk = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 230 + k * 310
        rrect(c, 1160, y + dk, 600, 290, 24, mix("#F7F7F5", GREEN, 0.10), ak)
        badge_num(c, n, 1230, y + 60 + dk, ak, 30, bg=GREEN)
        fit(c, tit, 1285, y + 74 + dk, 34, 450, "black", GREEN, ak)
        yy = y + 140 + dk
        for ln in sub.split(" | "):
            yy += para_nb(c, ln, 1460, yy, 28, "bold", INK, ak, 540, 34, align="center") + 4


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


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone do episódio)
VF = [
    ("quantas vezes a máquina age", "a₁ = 3, q = 2: a₆ = 3 · 2⁶ = 192", False, "o 6 da posição parece o expoente",
     "do 1º ao 6º termo, a máquina age 5 vezes", "3 · 2⁵ = 96", 0),
    ("razão = quociente", "a razão de (90, 30, 10) é −60", False, "na PA, a razão é a diferença",
     "na PG, a razão é o quociente: 30 ÷ 90", "q = 1/3", 0),
    ("fator repetido", "triplica 4 vezes: 100 · 3⁴ = 8 100", True, "dá vontade de fazer 100 · 3 · 4",
     "fator repetido é potência, não produto pelo número de vezes", "8 100", 0),
    ("taxa × fator", "cresce 8% ao ano: q = 0,08", False, "o 8% está escrito ali",
     "a razão é o fator: tudo o que havia + 8%", "q = 1,08", 3),
    ("o denominador", "30 + 10 + 10/3 + …: S∞ = 30 ÷ (1/3) = 90", False, "parece que é só dividir pela razão",
     "o denominador é 1 − q: 30 ÷ (2/3)", "S∞ = 45", 2),
    ("a fórmula com freio", "1 + 3 + 9 + 27 + … não tem soma infinita", True, "existe uma fórmula pronta",
     "com q = 3 não há freio: a soma não para de crescer", "|q| < 1", 2),
    ("a bola", "solta de 5 m, sobe metade: total = 5 ÷ (1/2) = 10 m", False, "a fórmula parece resolver tudo",
     "isso são só as descidas: o resto, 2 vezes", "5 + 2 · 5 = 15 m", 2),
    ("termo × soma", "corrente 4, 16, 64: o total em 3 dias não é 4³", True, "o 4³ está bem ali",
     "4³ é só o último dia: some os três", "4 + 16 + 64 = 84", 1),
    ("a dízima", "0,4545… = 45/100", False, "começa mesmo com 45",
     "dízima é soma infinita, não corte: 45/99", "5/11", 2),
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
    icone(c, ic, 330, 410, 0.5, a0)
    fmid(c, ctx.upper(), 960, 290, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    s = nb(conta)
    sz = 50
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
        lns = _quebra(nb(regra_), 30, 820)
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 725 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        fit(c, fix, 1420, 735, 44, 520, "black", GREEN, ag, align="center")


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
        text_mid(c, "o fator · os períodos · termo, soma ou soma infinita?", W / 2, 750, 34, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="QUANTO RESTA?", area="MEIA-VIDA", ic=0, ok="B",
               enun=[("a", "Um paciente tem 320 mg de um remédio no sangue. A meia-vida do remédio é de 6 h.", False),
                     ("b", "Quanto resta depois de 1 dia?", True)],
               alts=[("A", "10 mg", "uma meia-vida a mais", RED), ("B", "20 mg", "", GREEN),
                     ("C", "40 mg", "uma a menos", AMBER), ("D", "80 mg", "320 ÷ 4", RED),
                     ("E", "160 mg", "só a 1ª meia-vida", RED)],
               passos=[("d", "fator: ½"), ("d", "24 h ÷ 6 h = 4 meias-vidas"), ("a", "320 · (½)⁴ = 20 mg")],
               confere=None),
    "q2": dict(ids=("23", "24"), titulo="QUANTOS AO TODO?", area="SOMA FINITA", ic=1, ok="D",
               enun=[("a", "Na 1ª semana, 2 pessoas entram num grupo. Cada pessoa que entra convida 2 novas na semana "
                           "seguinte.", False),
                     ("b", "Quantas pessoas entraram ao todo até o fim da 5ª semana?", True)],
               alts=[("A", "32", "só a 5ª semana", AMBER), ("B", "10", "linear: 2 por semana", RED),
                     ("C", "64", "2⁶", RED), ("D", "62", "", GREEN), ("E", "126", "seis semanas", RED)],
               passos=[("d", "“ao todo” → SOMA FINITA · q = 2"), ("a", "2 + 4 + 8 + 16 + 32"), ("a", "S₅ = 62")],
               confere=("v", "atalho: (64 − 2) ÷ (2 − 1) = 62")),
    "q3": dict(ids=("25", "26"), titulo="ATÉ PARAR", area="SOMA INFINITA", ic=2, ok="A",
               enun=[("a", "Uma bola é solta de 10 m de altura. A cada quique, sobe 3/5 da altura anterior.", False),
                     ("b", "Qual é a distância total percorrida até parar?", True)],
               alts=[("A", "40 m", "", GREEN), ("B", "25 m", "só as descidas", AMBER), ("C", "15 m", "só as subidas", RED),
                     ("D", "30 m", "dobrou as subidas, sem a queda", RED), ("E", "50 m", "dobrou as descidas", RED)],
               passos=[("d", "“até parar” → SOMA ∞ · q = 3/5 (freio)"), ("a", "descidas: 10 ÷ (2/5) = 25 m"),
                       ("a", "subidas: 6 ÷ (2/5) = 15 m · total 40 m")],
               confere=None),
    "q4": dict(ids=("27", "28"), titulo="QUAL É O MODELO?", area="TABELA", ic=3, ok="E",
               enun=[("a", "O valor de um equipamento nos anos 0, 1, 2 e 3: 600, 540, 486 e 437,4.", False),
                     ("b", "Qual é o modelo?", True)],
               alts=[("A", "=600 − 60n", "PA: no ano 2, 480", RED), ("B", "=600 · 0,1^{n}", "a taxa no lugar do fator", AMBER),
                     ("C", "=600 · 0,9 · n", "dá 0 no ano 0", RED), ("D", "=540 · 0,9^{n}", "começa no valor errado", RED),
                     ("E", "=600 · 0,9^{n}", "", GREEN)],
               passos=[("d", "540 ÷ 600 = 0,9 (sempre)"), ("a", "perde 10%: sobra 90%"), ("a", "V = 600 · 0,9ⁿ")],
               confere=None),
    "q5": dict(ids=("29", "30"), titulo="A DÍZIMA VIRA FRAÇÃO", area="DÍZIMA", ic=4, ok="C",
               enun=[("a", "A dízima 0,3636… pode ser vista como uma soma infinita.", False),
                     ("b", "Qual fração ela representa?", True)],
               alts=[("A", "36/100", "cortou a dízima", AMBER), ("B", "2/5", "36/90", RED), ("C", "4/11", "", GREEN),
                     ("D", "4/111", "36/999: três noves", RED), ("E", "1/3", "só um valor parecido", RED)],
               passos=[("d", "0,36 + 0,0036 + …"), ("d", "a₁ = 0,36 · q = 0,01"), ("a", "0,36 ÷ 0,99 = 36/99 = 4/11")],
               confere=None),
}


def metades_q1(c, x0, y0, a, prog):
    """as barras 320 → 160 → 80 → 40 → 20 (cada meia-vida corta pela metade)"""
    if a <= 0:
        return
    for k, v in enumerate((320, 160, 80, 40, 20)):
        ak = a * ep(prog * 5, k, 0.6)
        h = v * 0.5
        x = x0 + k * 120
        rrect(c, x, y0 - h, 80, h, 8, RED if k == 4 else mix("#FFFFFF", RED, 0.5), ak)
        ftext(c, str(v), x + 40, y0 + 34, 26, "black", GREEN if k == 4 else INK2, ak, align="center")
        if k < 4:
            ftext(c, "÷2", x + 100, y0 - 20, 22, "black", PURPLE, ak, align="center")


def bola_q3(c, x0, ybase, a, prog):
    """os quiques da bola de 10 m (descidas azuis, subidas verdes)"""
    if a <= 0:
        return
    line(c, x0 - 20, ybase, x0 + 600, ybase, INK2, a, 4)
    segs = [(10, "d")]
    h = 10.0
    for _ in range(4):
        h *= 0.6
        segs += [(h, "s"), (h, "d")]
    esc = 12
    for k, (hh, tipo) in enumerate(segs):
        f = clamp(prog * len(segs) - k)
        if f <= 0:
            break
        x = x0 + 60 * ((k + 1) // 2) + (0 if tipo == "d" else 22)
        col = BLUE if tipo == "d" else GREEN
        y_top = ybase - hh * esc
        if tipo == "d":
            line(c, x, y_top, x, y_top + (ybase - y_top) * f, col, a, 6)
        else:
            line(c, x, ybase, x, ybase - (ybase - y_top) * f, col, a, 6)
        if k == 0:
            c.drawCircle(x, y_top - 14, 14, paint(AMBER, a))
    ftext(c, "10 m", x0 - 10, ybase - 130, 24, "black", BLUE, a, align="right")


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
        area_icone(c, d["ic"], 770, 222, 0.24, a0 * (1 - sol))
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720, 760)
        if sol > 0:
            yy = 290
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 32, 640, "black", GREEN if last else INK, a)
                yy += 66
            if nome == "q1":
                metades_q1(c, 210, yy + 220, sol, ep(t, C[f"{s2}.a"], 2.5))
                yy += 260
            if nome == "q3":
                bola_q3(c, 220, yy + 200, sol, ep(t, C[f"{s2}.a"], 3.0))
                yy += 230
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"] + 0.4, 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 790, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["razão = quociente · fator 1 ± i", "aₙ = a₁ · qⁿ⁻¹ e o instante zero", "tabela: PA × PG"]),
         ("31.c", "EP. 2", 1, ["b² = a · c", "x/q, x, x·q", "a soma finita Sₙ"]),
         ("32.a", "EP. 3", 2, ["S∞ = a₁ ÷ (1 − q), com |q| < 1", "dízimas como soma de PG", "a bola: queda + 2 × o resto"]),
         ("32.b", "EP. 4", 3, ["meia-vida: contar períodos", "juros compostos: 1 + i", "depreciação: 1 − i"])]


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
        icone(c, ic, x + 60, y0 + 140, 0.26, a)
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
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["33.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 200 + k * 82, 220 + r_ * 86
        col = mix("#E6E6E2", GREEN, ab if ok else 0)
        rrect(c, x, y, 66, 70, 12, col, a)
        if ac > 0 and i < 8:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 74, 78), 14, 14), paint(PURPLE, ac, stroke=4))
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos (70%)", 1450, 400, 44, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 200, 600, 1520, 180, PURPLE, ac, 0.08)
        for k, ic in enumerate((2, 0)):
            area_icone(c, ic, 300 + k * 130, 690, 0.22, ac)
        text_mid(c, "8 DE SOMA INFINITA OU DECAIMENTO", 1110, 660, 42, "black", PURPLE, ac)
        text_mid(c, "meia-vida · quiques", 1110, 730, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 240, 28, "black", GRAY, aa, tracking=2)
    text(c, "Matrizes e operações", W / 2, 330, 76, "black", PURPLE, aa)
    text(c, "a parte de álgebra linear", W / 2, 400, 40, "bold", INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        x0, y0, u = 560, 450, 110
        vals = ((2, 5, 1), (4, 0, 3))
        for i, row in enumerate(vals):
            for j, v in enumerate(row):
                aij = ab * ep(t, C["34.b"] + 0.15 * (3 * i + j), 0.3)
                rrect(c, x0 + j * u, y0 + i * u, u - 14, u - 14, 14, "#FFFFFF", aij, shadow=True)
                fmid(c, str(v), x0 + j * u + (u - 14) / 2, y0 + i * u + (u - 14) / 2, 48, "black", INK, aij)
        fit(c, "a₂₃ = 3", x0 + 3 * u + 60, y0 + u + 60, 44, 300, "black", BLUE, ab)
        selo(c, x0 + 3 * u + 180, y0 + 40, ab, "ENDEREÇO", BLUE, -3, 26)
    ac = ep(t, C["34.c"], 0.5)
    if ac > 0:
        rrect(c, 560, 700, 800, 90, 45, mix("#FFFFFF", GREEN, 0.25), ac, shadow=True)
        text_mid(c, "linha × coluna", W / 2, 745, 44, "black", GREEN, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
