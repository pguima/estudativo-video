"""Visual — Logaritmos, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, expr, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): balão de pergunta · régua de cálculo · elevador ·
segurança na porta.
Ícones de área (area_icone()): tubo de ensaio · alto-falante · sismógrafo · cifrão · placa de cultura · gota · lápis ·
relógio.
Logs escritos como texto, com a base em subscrito unicode (log₂ 32, log₃ x).
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
_s = importlib.util.spec_from_file_location("comum042", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_logaritmos_ep5_revisao.mp4"
CARD_R = K.CARD_R
METAL = "#9AA3AD"
AGUA = "#9CCFE6"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'log 2', '30 min', '1 000', '3 h' nem '−0,22'"""
    s = re.sub(r"(?<=log) (?=[\d(xM])", " ", s)
    s = re.sub(r"(?<=[₀-₉]) (?=[\d(x])", " ", s)
    s = re.sub(r"(?<=\d) (?=(h|mês|meses|dB|%)\b)", " ", s)
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
    out = _quebra(s, size, maxw, peso)
    if a > 0:
        for k, ln in enumerate(out):
            text(c, ln, x, y + k * lh, size, peso, color, a, align="left")
    return len(out) * lh


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def balao_ic(c, a):
    """ep1: o balão da pergunta ("b elevado a quanto dá a?")"""
    rrect(c, -190, -130, 380, 210, 60, "#FFFFFF", a, shadow=True)
    rrect(c, -190, -130, 380, 210, 60, BLUE, a * 0.14)
    p = skia.Path(); p.moveTo(-40, 78); p.lineTo(-90, 150); p.lineTo(20, 78); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.14), a))
    ftext(c, "log", -40, -5, 70, "black", BLUE, a, align="center")
    ftext(c, "?", 110, 10, 110, "black", PURPLE, a, align="center")


def regua_ic(c, a):
    """ep2: a régua de cálculo (somar logs = multiplicar números)"""
    rrect(c, -210, -90, 420, 80, 10, mix("#FFFFFF", AMBER, 0.35), a, shadow=True)
    rrect(c, -110, 10, 420, 80, 10, mix("#FFFFFF", GREEN, 0.30), a, shadow=True)
    for k in range(9):
        x = -200 + 50 * k
        line(c, x, -10, x, -40 if k % 2 else -55, INK2, a, 4)
        x2 = -100 + 50 * k
        line(c, x2, 10, x2, 40 if k % 2 else 55, INK2, a, 4)
    ftext(c, "×", -30, 150, 60, "black", PURPLE, a, align="center")
    ftext(c, "= +", 70, 150, 50, "black", GREEN, a, align="center")


def elevador_ic(c, a):
    """ep3: o elevador que traz o expoente para o térreo"""
    rrect(c, -120, -160, 240, 320, 14, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-120, -160, 240, 320), 14, 14), paint(INK2, a, stroke=7))
    line(c, 0, -160, 0, 160, LIGHT, a, 5)
    ftext(c, "t", 60, -80, 64, "black", PURPLE, a, align="center")
    arrow(c, 60, -50, 60, 90, PURPLE, a, 9, 26)
    rrect(c, 150, -40, 60, 120, 12, mix("#FFFFFF", INK2, 0.15), a)
    p = skia.Path(); p.moveTo(180, -25); p.lineTo(165, 0); p.lineTo(195, 0); p.close()
    c.drawPath(p, paint(GREEN, a))
    p = skia.Path(); p.moveTo(180, 65); p.lineTo(165, 40); p.lineTo(195, 40); p.close()
    c.drawPath(p, paint(GREEN, a))


def seguranca_ic(c, a):
    """ep4: o segurança na porta do log (só entra número positivo)"""
    rrect(c, -40, -170, 220, 330, 12, mix("#FFFFFF", BLUE, 0.30), a, shadow=True)
    ftext(c, "log", 70, -110, 46, "black", BLUE, a, align="center")
    c.drawCircle(-130, -80, 40, paint(INK, a))
    rrect(c, -190, -35, 120, 170, 40, INK, a)
    rrect(c, -170, 0, 80, 40, 8, AMBER, a)
    ftext(c, "> 0", -130, 30, 26, "black", INK, a, align="center")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (balao_ic, regua_ic, elevador_ic, seguranca_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def tubo(c, a):
    rrect(c, -50, -150, 100, 270, 50, "#FFFFFF", a)
    rrect(c, -50, 0, 100, 120, 50, mix("#FFFFFF", GREEN, 0.55), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-50, -150, 100, 270), 50, 50), paint(INK2, a, stroke=6))
    rrect(c, -70, -170, 140, 30, 10, INK2, a)
    for (x, y, r) in ((-15, 40, 12), (18, 75, 9), (0, 10, 7)):
        c.drawCircle(x, y, r, paint("#FFFFFF", a))


def falante(c, a):
    rrect(c, -150, -50, 80, 100, 8, INK2, a)
    p = skia.Path(); p.moveTo(-70, -50); p.lineTo(10, -120); p.lineTo(10, 120); p.lineTo(-70, 50); p.close()
    c.drawPath(p, paint(INK2, a))
    for j in range(3):
        q = skia.Path(); r = 50 + j * 40
        q.addArc(skia.Rect.MakeXYWH(10 - r, -r, 2 * r, 2 * r), -45, 90)
        c.drawPath(q, paint(BLUE, a, stroke=9))


def sismo(c, a):
    rrect(c, -170, -120, 340, 240, 16, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-170, -120, 340, 240), 16, 16), paint(INK2, a, stroke=6))
    p = skia.Path(); p.moveTo(-150, 0)
    for k, h in enumerate((10, -20, 30, -70, 95, -90, 60, -35, 15, -8)):
        p.lineTo(-130 + k * 28, h)
    p.lineTo(150, 0)
    c.drawPath(p, paint(RED, a, stroke=7))


def cifrao(c, a):
    c.drawCircle(0, 0, 130, paint(AMBER, a))
    c.drawCircle(0, 0, 130, paint(mix(AMBER, INK, 0.3), a, stroke=8))
    ftext(c, "R$", 0, 40, 110, "black", "#FFFFFF", a, align="center")


def placa(c, a):
    c.drawOval(skia.Rect.MakeXYWH(-160, -70, 320, 140), paint(mix("#FFFFFF", AGUA, 0.6), a))
    c.drawOval(skia.Rect.MakeXYWH(-160, -70, 320, 140), paint(INK2, a, stroke=6))
    for (x, y, r) in ((-60, -10, 26), (20, 15, 20), (70, -20, 16), (-10, -30, 12), (-90, 25, 12)):
        c.drawCircle(x, y, r, paint(GREEN, a))


def gota(c, a):
    p = skia.Path(); p.moveTo(0, -160); p.quadTo(120, 10, 100, 60); p.quadTo(60, 150, 0, 150)
    p.quadTo(-60, 150, -100, 60); p.quadTo(-120, 10, 0, -160); p.close()
    c.drawPath(p, paint(AGUA, a))
    c.drawPath(p, paint(mix(AGUA, INK, 0.4), a, stroke=6))
    c.drawCircle(-35, 60, 18, paint("#FFFFFF", a * 0.8))


def lapis(c, a):
    c.save(); c.rotate(-35)
    rrect(c, -150, -32, 240, 64, 6, AMBER, a)
    rrect(c, -190, -32, 50, 64, 8, mix(RED, "#FFFFFF", 0.3), a)
    p = skia.Path(); p.moveTo(90, -32); p.lineTo(160, 0); p.lineTo(90, 32); p.close()
    c.drawPath(p, paint("#F2D3A8", a))
    p = skia.Path(); p.moveTo(138, -10); p.lineTo(160, 0); p.lineTo(138, 10); p.close()
    c.drawPath(p, paint(INK, a))
    c.restore()


def relogio_ic(c, a):
    c.drawCircle(0, 0, 130, paint("#FFFFFF", a))
    c.drawCircle(0, 0, 130, paint(INK2, a, stroke=10))
    line(c, 0, 0, 0, -85, INK, a, 9)
    line(c, 0, 0, 60, 35, INK, a, 7)
    c.drawCircle(0, 0, 11, paint(INK, a))


AREA_F = (tubo, falante, sismo, cifrao, placa, gota, lapis, relogio_ic)


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
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 240, 760, 300, 24, "#FFFFFF", aa, shadow=True)
        rrect(c, 200, 240, 18, 300, 8, BLUE, aa)
        text(c, "ENUNCIADO", 260, 300, 24, "black", GRAY, aa, align="left", tracking=2)
        text(c, "o logaritmo é o tema?", 260, 400, 42, "black", INK2, aa, align="left")
        ar = ep(t, C["01.a"] + 2.0, 0.4)
        if ar > 0:
            w_ = ftw("o logaritmo é o tema?", 42)
            strike(c, 250, 386, 270 + w_, 386, ar, RED, ar)
        selo(c, 760, 470, ep(t, C["01.a"] + 2.2, 0.4), "É A FERRAMENTA", PURPLE, -5, 32)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 600, 700, 110, 18, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        fmid(c, nb("“use log 2 = 0,30”"), 580, 655, 52, "black", INK, ab)
    for k, (s, col, ic) in enumerate((("UM TEMPO", GREEN, 7), ("UMA CONTAGEM", BLUE, 6), ("UM EXPOENTE", PURPLE, None))):
        a, d = rise(t, C["01.c"] + 0.5 * k)
        if a <= 0:
            continue
        y = 260 + k * 160
        arrow(c, 960, 655, 1100, y + 60 + d, INK2, a * 0.7, 4, 12)
        rrect(c, 1120, y + d, 600, 120, 18, "#FFFFFF", a, shadow=True)
        if ic is None:
            icone(c, 2, 1200, y + 60 + d, 0.28, a)
        else:
            area_icone(c, ic, 1200, y + 60 + d, 0.28, a)
        ftext(c, s, 1280, y + 76 + d, 44, "black", col, a, align="left")
    ad = ep(t, C["01.d"], 0.5)
    selo(c, 1420, 790, ad, "TREINE A FERRAMENTA", GREEN, -4, 34)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        chip(c, "9 V OU F", 330, 866, AMBER, ae, 26)
        chip(c, "5 QUESTÕES NOVAS", 640, 866, GREEN, ep(t, C["01.e"] + 0.5, 0.4), 26)


COBRA = [("02.a", "DESCOBRIR UM TEMPO", "dobra · cresce · cai à metade", GREEN, 7),
         ("02.b", "CALCULAR COM VALORES DADOS", "log 72 com log 2 e log 3", BLUE, 6),
         ("02.c", "EQUAÇÕES LOGARÍTMICAS", "com as condições de existência", PURPLE, None),
         ("02.d", "ESCALAS", "pH · Richter · decibéis — próxima série", AMBER, 2)]


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
        if ic is None:
            icone(c, 3, x, 570 + d, 0.42, a)
        else:
            area_icone(c, ic, x, 570 + d, 0.42, a)
        para(c, nb(sub), x, 690 + d, 26, "bold", INK2, a, 360, 32, align="center")


RENDE = [("03.a", "log₂ 32", "2 elevado a quanto dá 32?", "5"),
         ("03.b", "log 0,001", "10 elevado a quanto dá 0,001?", "−3"),
         ("03.c", "log₉ 3", "9 elevado a quanto dá 3?", "1/2")]


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "LEIA O LOG COMO PERGUNTA", BLUE)
    a0 = ep(t, C["03.t"], 0.5)
    if a0 > 0:
        rrect(c, 460, 210, 1000, 110, 55, mix("#FFFFFF", BLUE, 0.12), a0)
        ftext(c, "log", 600, 280, 44, "black", BLUE, a0, align="left")
        ftext(c, "b", 600 + ftw("log", 44) + 2, 294, 26, "black", BLUE, a0, align="left")
        ftext(c, "a   →   “b elevado a quanto dá a?”", 600 + ftw("log", 44) + 30, 280, 40, "black", BLUE, a0,
              align="left")
    for k, (cue, lg, perg, val) in enumerate(RENDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 370 + k * 150
        rrect(c, 200, y + d, 440, 110, 16, "#FFFFFF", a, shadow=True)
        fit(c, lg, 420, y + 72 + d, 58, 400, "black", INK, a, align="center")
        arrow(c, 660, y + 55 + d, 760, y + 55 + d, PURPLE, a, 6, 16)
        fit(c, perg, 790, y + 68 + d, 36, 640, "bold", INK2, a)
        rrect(c, 1470, y + d, 250, 110, 16, mix("#FFFFFF", PURPLE, 0.15), a)
        fit(c, val, 1595, y + 74 + d, 62, 220, "black", PURPLE, a, align="center")


INDICE = [("EP. 1", "o log é uma pergunta · um expoente com nome próprio · o log decimal conta zeros"),
          ("EP. 2", "potência lida de trás para frente · o kit 2, 3 e 10 · soma no log: porta trancada"),
          ("EP. 3", "o elevador desce o expoente · a base vai para o porão · estime entre dois inteiros"),
          ("EP. 4", "o segurança na porta do log · toda raiz mostra documento")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 300 + k * 440
        y = 210
        rrect(c, x - 200, y, 400, 620, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 200, y, 400, 620), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 180, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 200, 0.62, a)
        yy = y + 360
        for ln in s.split(" · "):
            yy += para(c, nb(ln), x, yy, 26, "black", INK if on_ else INK2, a, 350, 32, align="center") + 10


ONDE = [("06.a", "QUÍMICA", 0, "pH = −log[H⁺]", "cada unidade = fator 10", GREEN),
        ("06.b", "FÍSICA", 1, "decibéis", "+10 dB = intensidade ×10", BLUE),
        ("06.c", "GEOGRAFIA", 2, "terremotos", "um grau a mais = amplitude ×10", RED),
        ("07.d", "FINANCEIRA", 3, "t = log(M/C) ÷ log(1 + i)", "o tempo do montante", AMBER),
        ("07.e", "QUÍMICA E BIOLOGIA", 4, "meia-vida · culturas", "log da razão ÷ log do fator", PURPLE)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA FERRAMENTA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 240 + k * 360
        rrect(c, x - 165, 220 + d, 330, 560, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 28, "black", col, a, 300, 34, align="center")
        area_icone(c, ic, x, 450 + d, 0.40, a)
        fit(c, lei_, x, 630 + d, 30, 300, "black", INK, a, align="center")
        para(c, nb(res), x, 680 + d, 25, "bold", INK2, a, 290, 31, align="center")
    af = ep(t, C["07.f"], 0.5)
    if af > 0:
        boxed(c, 460, 820, 1000, 72, AMBER, af, 0.10)
        text_mid(c, "pH, decibéis e Richter: a próxima série", W / 2, 856, 30, "black", INK, af)


HABITOS = [("08.a", "1", "DECOMPONHA EM 2, 3 E 10", "72 = 2³ · 3² | 50 = 100/2 | 0,9 = 9/10"),
           ("08.b", "2", "ESTIME ANTES DE MARCAR", "3ᵗ = 50 | 3³ = 27 e 3⁴ = 81 | t entre 3 e 4"),
           ("09.c", "3", "DUAS RAÍZES? DESCONFIE", "teste cada raiz | nos logaritmandos originais")]


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
        for ln in sub.split(" | "):
            yy += para(c, nb(ln), x, yy, 30, "bold", INK, a, 460, 38, align="center") + 12


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
    ("porta trancada", "log(M + N) = log M + log N", False, "parece a regra do produto",
     "soma dentro do log não tem regra", "só log(M · N)", 1),
    ("quociente", "log M ÷ log N = log M − log N", False, "“divisão” aparece nas duas",
     "a diferença é o log do quociente", "log(M/N)", 1),
    ("produto vira soma", "log 72 = log 8 + log 9", True, "muita gente escreve log 8 · log 9",
     "potência lida de trás para frente: produto vira soma", "72 = 8 · 9", 1),
    ("a base no porão", "log₂ 10 = log 2 ÷ log 10", False, "o 2 aparece primeiro",
     "a base vai para baixo: log 10 ÷ log 2", "≈ 3,32", 2),
    ("entre 0 e 1", "log 0,9 é negativo", True, "log 9 é positivo: 0,954",
     "0,9 = 9/10: tire 1", "≈ −0,046", 1),
    ("log de zero", "log 0 = 0", False, "zero parece dar zero em tudo",
     "nenhum expoente dá zero: não existe", "log 1 = 0", 0),
    ("o segurança", "log x + log(x + 3) = 1 → x = 2 ou x = −5", False, "as duas raízes saem da conta",
     "log de número negativo não existe: −5 fica na porta", "só x = 2", 3),
    ("o 1 000 vira parcela", "log(1 000 · 3ᵗ) = 3 + t · log 3", True, "muita gente escreve 3t · log 3",
     "log 1 000 = 3 · só o t desce no elevador", "3 + t · log 3", 2),
    ("contar algarismos", "2¹⁰⁰ tem 30 algarismos", False, "o log dá 30,1",
     "algarismos = parte inteira + 1", "31", 0),
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
        rrect(c, W / 2 - 440, 700, 880, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "decomponha · estime · resolva", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="O LOG QUE SAI DO KIT", area="LOG POR DECOMPOSIÇÃO", ic=6, ok="D",
               enun=[("a", "Considere log 2 = 0,30 e log 3 = 0,48.", False),
                     ("b", "O valor de log 0,6 é:", True)],
               formula=None,
               alts=[("A", "0,78", "é log 6: esqueceu o ÷ 10", AMBER), ("B", "0,22", "erro de sinal", RED),
                     ("C", "0,144", "log 2 · log 3", RED), ("D", "−0,22", "", GREEN),
                     ("E", "−0,78", "sinal trocado e sem o ÷ 10", RED)],
               passos=[("d", "0,6 está entre 0 e 1 → log negativo"), ("a", "0,6 = 6/10 = (2 · 3)/10"),
                       ("b", "0,30 + 0,48 − 1 = −0,22")],
               confere=None),
    "q2": dict(ids=("23", "24"), titulo="A CULTURA QUE DOBRA", area="TEMPO DE CRESCIMENTO", ic=0, ok="C",
               enun=[("a", "Uma cultura de bactérias cresce 25% por hora. Use log 2 = 0,30.", False),
                     ("b", "A cultura dobra em:", True)],
               formula=None,
               alts=[("A", "0,2 h", "subtraiu os logs", RED), ("B", "cerca de 0,33 h", "inverteu a divisão", RED),
                     ("C", "3 h", "", GREEN), ("D", "4 h", "linear: 100% ÷ 25%", AMBER),
                     ("E", "8 h", "2 ÷ 0,25", RED)],
               passos=[("d", "1,25ᵗ = 2"), ("a", "log 1,25 = log(10/8) = 1 − 3 · 0,30 = 0,10"),
                       ("b", "t = 0,30 ÷ 0,10 = 3 h")],
               confere=("v", "1,25³ ≈ 1,95: quase o dobro")),
    "q3": dict(ids=("25", "26"), titulo="O POLUENTE NO LAGO", area="TEMPO DE DECAIMENTO", ic=5, ok="D",
               enun=[("a", "Um lago perde 20% de um poluente por mês, sempre sobre o que restou. Use log 2 = 0,30.", False),
                     ("b", "Resta a metade em:", True)],
               formula=None,
               alts=[("A", "cerca de 0,33 mês", "inverteu a divisão", RED), ("B", "cerca de 0,43 mês", "fator 0,2", RED),
                     ("C", "2,5 meses", "linear: 50% ÷ 20%", AMBER), ("D", "3 meses", "", GREEN),
                     ("E", "5 meses", "perder tudo, linear", AMBER)],
               passos=[("d", "0,8ᵗ = 0,5"), ("a", "log 0,8 = 0,90 − 1 = −0,10 · log 0,5 = −0,30"),
                       ("b", "t = (−0,30) ÷ (−0,10) = 3 meses")],
               confere=("v", "0,8³ = 0,512")),
    "q4": dict(ids=("27", "28"), titulo="A EQUAÇÃO DAS DUAS RAÍZES", area="EQUAÇÃO LOGARÍTMICA", ic=6, ok="A",
               enun=[("a", "O conjunto solução da equação abaixo é:", True)],
               formula=("a", "log₃ x + log₃ (x − 8) = 2"),
               alts=[("A", "{9}", "", GREEN), ("B", "{−1}", "a raiz proibida", RED),
                     ("C", "{−1, 9}", "não verificou", AMBER), ("D", "{8,5}", "somou os logaritmandos", RED),
                     ("E", "∅", "jogou fora a raiz boa", RED)],
               passos=[("d", "condições: x > 0 e x > 8 → x > 8"), ("a", "x · (x − 8) = 3² = 9"),
                       ("a", "x² − 8x − 9 = 0 → 9 ou −1"), ("b", "−1 fica na porta → {9}")],
               confere=("b", "log₃ 9 + log₃ 1 = 2 + 0")),
    "q5": dict(ids=("29", "30"), titulo="QUANTOS ALGARISMOS?", area="CONTAR ALGARISMOS", ic=6, ok="B",
               enun=[("a", "Use log 3 = 0,477.", False),
                     ("b", "O número 3⁵⁰ tem quantos algarismos?", True)],
               formula=None,
               alts=[("A", "23", "esqueceu o + 1", AMBER), ("B", "24", "", GREEN),
                     ("C", "50", "o expoente", RED), ("D", "51", "expoente + 1", RED),
                     ("E", "150", "base × expoente", RED)],
               passos=[("d", "log 3⁵⁰ = 50 · 0,477 = 23,85"), ("a", "parte inteira 23 + 1 = 24")],
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
        K.alternativas(c, t, C, [(L, nb(s), w, col) for L, s, w, col in d["alts"]],
                       880, 230, 820, 30, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        area_icone(c, d["ic"], 770, 222, 0.26, a0 * (1 - sol))
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        if d["formula"]:
            af = ep(t, C[f"{s1}.{d['formula'][0]}"] + 0.6, 0.4) * (1 - sol)
            if af > 0:
                rrect(c, 180, y + 10, 620, 100, 16, mix("#FFFFFF", PURPLE, 0.10), af)
                fit(c, d["formula"][1], 490, y + 76, 44, 580, "black", PURPLE, af, align="center")
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720, 760)
        if sol > 0:
            yy = 300
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.8 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 34, 640, "black", GREEN if last else INK, a)
                yy += 70
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"] + 1.6, 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 760, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["traduzir log em potência e vice-versa", "condições · logs de cabeça", "contar algarismos"]),
         ("31.c", "EP. 2", 1, ["produto, quociente e potência", "as propriedades falsas", "o kit log 2 e log 3"]),
         ("32.a", "EP. 3", 2, ["mudança de base", "equação exponencial com log", "tempo de dobrar ou cair à metade"]),
         ("32.b", "EP. 4", 3, ["equações logarítmicas", "verificar cada raiz"])]


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
        icone(c, ic, x + 55, y0 + 130, 0.24, a)
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
        area_icone(c, 6, 330, 670, 0.40, ac)
        text_mid(c, nb("10 COM log 2 E log 3 NO ENUNCIADO"), 1060, 640, 44, "black", BLUE, ac)
        text_mid(c, "a ferramenta dada pronta: decomponha e use", 1060, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 260, 28, "black", GRAY, aa, tracking=2)
    text(c, "Função logarítmica", W / 2, 350, 76, "black", PURPLE, aa)
    text(c, "e aplicações: pH · Richter · decibéis", W / 2, 420, 36, "bold", INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    selo(c, W / 2, 500, ab, "AS ESCALAS DO MUNDO REAL", GREEN, -3, 32)
    for k, (s, ic, col) in enumerate((("mais ácido", 0, GREEN), ("mais energia", 2, RED), ("mais barulho", 1, BLUE))):
        a, d = rise(t, C["34.c"] + 1.1 * k)
        if a <= 0:
            continue
        x = 480 + k * 480
        rrect(c, x - 200, 580 + d, 400, 250, 24, mix("#F7F7F5", col, 0.10), a)
        area_icone(c, ic, x, 670 + d, 0.36, a)
        text(c, "quantas vezes", x, 770 + d, 26, "bold", INK2, a)
        text(c, s, x, 808 + d, 34, "black", col, a)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
