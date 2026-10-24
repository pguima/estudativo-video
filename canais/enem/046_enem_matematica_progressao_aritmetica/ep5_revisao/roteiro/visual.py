"""Visual — Progressão Aritmética, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): escada de degraus · fila de postes · pares de Gauss ·
extrato bancário.
Ícones de área (area_icone()): palitos · cofrinho · poste · reta dos meios · Σ · moeda · velocidade · molécula · montanha.
Índices (a₁, a₁₀) e "Σ" só passam por ftext/fmid/fit (nunca text, pill, chip, head).
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
_s = importlib.util.spec_from_file_location("comum046", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_progressao_aritmetica_ep5_revisao.mp4"
CARD_R = K.CARD_R
MADEIRA = "#C98A4B"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'R$ 30', '40 m', '1 000' nem '6,5 °C'"""
    s = re.sub(r"(?<=\$) (?=\d)", " ", s)
    s = re.sub(r"(?<=\d) (?=(°C|m|km|u|reais|vezes|%|termos|saltos|meses|palitos|postes)\b)", " ", s)
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

def escada_ic(c, a):
    """ep1: a escada de degraus iguais"""
    for k in range(5):
        h = 50 + k * 50
        rrect(c, -200 + k * 80, 140 - h, 74, h, 8, mix("#FFFFFF", PURPLE, 0.18 + 0.1 * k), a, shadow=True)
        rrect(c, -200 + k * 80, 140 - h, 74, 9, 4, PURPLE, a)
    arrow(c, -160, 60, 40, -100, GREEN, a, 6, 18)
    ftext(c, "+r", -90, -50, 40, "black", GREEN, a, align="center")


def poste_ic_um(c, x, yb, h, a, col=INK2):
    line(c, x, yb, x, yb - h, col, a, 9)
    line(c, x, yb - h, x + 26, yb - h, col, a, 7)
    c.drawCircle(x + 30, yb - h + 8, 11, paint(AMBER, a))


def postes_ic(c, a):
    """ep2: fila de postes e os intervalos entre eles"""
    line(c, -220, 120, 220, 120, INK2, a, 5)
    for k in range(4):
        poste_ic_um(c, -180 + k * 120, 120, 190, a)
    for k in range(3):
        x = -180 + k * 120
        p = skia.Path(); p.moveTo(x + 10, 150); p.quadTo(x + 60, 195, x + 110, 150)
        c.drawPath(p, paint(GREEN, a, stroke=5))
    ftext(c, "+1", 0, -130, 44, "black", GREEN, a, align="center")


def gauss_ic(c, a):
    """ep3: os pares de Gauss (primeiro com último, segundo com penúltimo)"""
    vals = (1, 2, 3, 4, 5, 6)
    for k, v in enumerate(vals):
        x = -200 + k * 80
        c.drawCircle(x, 40, 32, paint(mix("#FFFFFF", BLUE, 0.2), a))
        c.drawCircle(x, 40, 32, paint(BLUE, a, stroke=4))
        fmid(c, str(v), x, 40, 34, "black", BLUE, a)
    for j, col in enumerate((GREEN, AMBER, PURPLE)):
        x1, x2 = -200 + j * 80, -200 + (5 - j) * 80
        p = skia.Path(); p.moveTo(x1, 0); p.quadTo((x1 + x2) / 2, -110 + j * 30, x2, 0)
        c.drawPath(p, paint(col, a, stroke=5))
    ftext(c, "7 · 7 · 7", 0, 150, 40, "black", GREEN, a, align="center")


def extrato_ic(c, a):
    """ep4: o extrato bancário (o capital é o termo zero)"""
    rrect(c, -170, -170, 340, 340, 20, "#FFFFFF", a, shadow=True)
    rrect(c, -170, -170, 340, 70, 20, BLUE, a * 0.9)
    ftext(c, "EXTRATO", 0, -122, 32, "black", "#FFFFFF", a, align="center")
    for k, s in enumerate(("mês 0  1 000", "mês 1  1 030", "mês 2  1 060")):
        ftext(c, nb(s), -140, -40 + k * 66, 30, "black", INK if k else AMBER, a, align="left")
        line(c, -150, -18 + k * 66, 150, -18 + k * 66, LIGHT, a, 2)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (escada_ic, postes_ic, gauss_ic, extrato_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def palito(c, x1, y1, x2, y2, a):
    line(c, x1, y1, x2, y2, MADEIRA, a, 12)
    c.drawCircle(x2, y2, 11, paint(RED, a))


def palitos_ic(c, a):
    """triângulos de palitos em fila"""
    for k in range(3):
        x = -150 + k * 100
        palito(c, x, 80, x + 100, 80, a)
        palito(c, x, 80, x + 50, -10, a)
        palito(c, x + 100, 80, x + 50, -10, a)


def cofrinho(c, a):
    c.drawOval(skia.Rect.MakeXYWH(-150, -90, 300, 200), paint(mix("#FFFFFF", RED, 0.45), a))
    c.drawOval(skia.Rect.MakeXYWH(-150, -90, 300, 200), paint(INK2, a, stroke=6))
    rrect(c, -40, -100, 80, 16, 6, INK2, a)
    for x in (-90, 60):
        rrect(c, x, 100, 30, 50, 8, mix("#FFFFFF", RED, 0.45), a)
    c.drawCircle(150, 0, 26, paint(mix("#FFFFFF", RED, 0.45), a))
    ftext(c, "R$", 0, 40, 64, "black", "#FFFFFF", a, align="center")


def poste_area(c, a):
    line(c, -200, 140, 200, 140, INK2, a, 6)
    poste_ic_um(c, -100, 140, 260, a)
    poste_ic_um(c, 100, 140, 260, a)
    arrow(c, -90, 170, 90, 170, GREEN, a, 4, 14)
    arrow(c, 90, 170, -90, 170, GREEN, a, 4, 14)


def meios_ic(c, a):
    line(c, -220, 0, 220, 0, INK2, a, 5)
    for k in range(6):
        x = -200 + k * 80
        ext = k in (0, 5)
        c.drawCircle(x, 0, 24, paint(PURPLE if ext else "#FFFFFF", a))
        c.drawCircle(x, 0, 24, paint(PURPLE, a, stroke=5))
        if k < 5:
            p = skia.Path(); p.moveTo(x + 6, -30); p.quadTo(x + 40, -80, x + 74, -30)
            c.drawPath(p, paint(GREEN, a, stroke=4))


def sigma_ic(c, a):
    rrect(c, -150, -150, 300, 300, 30, mix("#FFFFFF", BLUE, 0.15), a, shadow=True)
    ftext(c, "Σ", 0, 70, 220, "black", BLUE, a, align="center")


def moeda(c, a):
    c.drawCircle(0, 0, 140, paint(AMBER, a))
    c.drawCircle(0, 0, 112, paint(mix(AMBER, INK, 0.25), a, stroke=8))
    ftext(c, "R$", 0, 26, 86, "black", "#FFFFFF", a, align="center")


def queda_ic(c, a):
    """física: bola caindo, distâncias 1, 3, 5, 7"""
    y = -170
    for k, d in enumerate((1, 3, 5, 7)):
        c.drawCircle(-60, y, 22, paint(mix("#FFFFFF", BLUE, 0.3 + 0.15 * k), a))
        ftext(c, str(d), 40, y + 12, 38, "black", BLUE, a, align="center")
        y += 22 + d * 12
    arrow(c, -120, -170, -120, 160, INK2, a, 5, 16)


def molecula(c, a):
    xs = (-150, -50, 50, 150)
    for k in range(3):
        line(c, xs[k], 0, xs[k + 1], 0, INK2, a, 8)
    for x in xs:
        c.drawCircle(x, 0, 38, paint(INK, a))
        fmid(c, "C", x, 0, 36, "black", "#FFFFFF", a)
        for dy in (-80, 80):
            line(c, x, dy * 0.45, x, dy, INK2, a, 5)
            c.drawCircle(x, dy, 18, paint("#FFFFFF", a)); c.drawCircle(x, dy, 18, paint(INK2, a, stroke=4))


def montanha(c, a):
    p = skia.Path(); p.moveTo(-200, 140); p.lineTo(-30, -150); p.lineTo(60, -10); p.lineTo(110, -70); p.lineTo(220, 140)
    p.close()
    c.drawPath(p, paint(mix("#FFFFFF", GREEN, 0.45), a))
    q = skia.Path(); q.moveTo(-80, -65); q.lineTo(-30, -150); q.lineTo(20, -70); q.close()
    c.drawPath(q, paint("#FFFFFF", a))
    c.drawPath(p, paint(INK2, a, stroke=5))
    ftext(c, "−6,5 °C", 120, -110, 34, "black", BLUE, a, align="center")


AREA_F = (palitos_ic, cofrinho, poste_area, meios_ic, sigma_ic, moeda, queda_ic, molecula, montanha)


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
    a0 = ep(t, C["01.a"], 0.5)
    if a0 > 0:
        rrect(c, 560, 190, 800, 120, 60, "#FFFFFF", a0, shadow=True)
        text_mid(c, "“progressão aritmética”", W / 2, 250, 56, "black", INK2, a0)
        strike(c, W / 2 - 330, 252, W / 2 + 330, 252, ep(t, C["01.a"] + 1.4, 0.4), RED)
    for k, (s, ic, col) in enumerate((("palito de fósforo", 0, BLUE), ("fileira de teatro", 4, PURPLE),
                                      ("depósito que aumenta", 1, GREEN))):
        a, d = rise(t, C["01.b"] + 1.1 * k)
        if a <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 240, 350 + d, 480, 280, 26, mix("#F7F7F5", col, 0.12), a)
        area_icone(c, ic, x, 460 + d, 0.42, a)
        fit(c, s, x, 590 + d, 34, 440, "black", col, a, align="center")
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        rrect(c, 560, 670, 800, 110, 55, mix("#FFFFFF", AMBER, 0.25), ac, shadow=True)
        fmid(c, "o erro: n − 1", W / 2, 725, 54, "black", INK, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "9 V OU F", 330, 880, AMBER, ad, 26)
        chip(c, "5 QUESTÕES NOVAS", 1590, 880, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 26)


COBRA = [("02.a", "PADRÕES DE FIGURAS", "a figura 50", BLUE, 0),
         ("02.b", "TERMO DISTANTE", "quanto no 12º mês", PURPLE, 5),
         ("02.c", "SOMA DE MUITOS TERMOS", "as cadeiras do teatro", GREEN, 4),
         ("02.d", "CONTAGEM", "postes · múltiplos de 7", AMBER, 2)]


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
        fit(c, sub, x, 715 + d, 30, 340, "black", INK2, a, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "DUAS HABILIDADES", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate((("03.a", "O n − 1", "do 1º ao 12º termo: 11 saltos, não 12", PURPLE, 0),
                                                  ("03.b", "A SOMA PELA MÉDIA", "S = n · (a₁ + aₙ) ÷ 2", GREEN, 2))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 290
        rrect(c, 200, y + d, 1520, 250, 26, mix("#F7F7F5", col, 0.10), a, shadow=True)
        badge_num(c, k + 1, 280, y + 125 + d, a, 36, bg=col)
        icone(c, ic, 480, y + 125 + d, 0.48, a)
        fit(c, tit, 680, y + 115 + d, 54, 1000, "black", col, a)
        fit(c, sub, 680, y + 182 + d, 38, 1000, "bold", INK2, a)


INDICE = [("EP. 1", "escada de degraus iguais · do 1º ao 20º, 19 saltos · teste com n = 1"),
          ("EP. 2", "postes e intervalos · o + 1 conta o primeiro · x − r, x, x + r"),
          ("EP. 3", "o truque de Gauss · duas escadas, um retângulo · termos × média"),
          ("EP. 4", "o capital é o termo zero · a semana: PA de razão 7")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 360, 380, 1200, 160, 30, "#FFFFFF", aq, shadow=True)
        fmid(c, "do 1º ao 20º termo: quantos saltos?", W / 2, 460, 52, "black", INK, aq)
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


ONDE = [("06.a", "FINANCEIRA", 5, "juros simples", "os montantes sobem sempre C · i", GREEN),
        ("06.b", "FÍSICA", 6, "MUV", "velocidades em PA · do repouso: 1, 3, 5, 7…", BLUE),
        ("07.c", "QUÍMICA", 7, "série homóloga", "cada carbono: + CH₂, + 14 u", PURPLE),
        ("07.d", "GEOGRAFIA", 8, "altitude", "≈ 6,5 °C a menos a cada 1 000 m", AMBER)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA ESCADA, OUTRA ROUPA", BLUE)
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
        fit(c, "ESCREVA OS TRÊS PRIMEIROS TERMOS", 250, 315 + d, 40, 840, "black", GREEN, a)
        rrect(c, 170, 380 + d, 900, 230, 18, "#FFFFFF", a, shadow=True)
        for j, (nome, v) in enumerate((("a₁", "30"), ("a₂", "40"), ("a₃", "50"))):
            aj = ep(t, C["08.a"] + 1.6 + 0.5 * j, 0.4) * a
            x = 300 + j * 300
            ftext(c, nome, x, 455 + d, 40, "black", BLUE, aj, align="center")
            ftext(c, v, x, 540 + d, 58, "black", INK, aj, align="center")
            if j < 2:
                arrow(c, x + 70, 520 + d, x + 230, 520 + d, GREEN, aj, 5, 14)
                ftext(c, "+10", x + 150, 495 + d, 30, "black", GREEN, aj, align="center")
        a2 = ep(t, C["08.a2"], 0.4) * a
        if a2 > 0:
            for k, s in enumerate(("é PA?", "a razão", "teste a fórmula")):
                chip(c, s, 320 + k * 300, 690 + d, GREEN, a2 * ep(t, C["08.a2"] + 0.6 * k, 0.3), 26)
            selo(c, 620, 785 + d, a2, "ANTES DA FÓRMULA", AMBER, -2, 30)
    for k, (cue, n, tit, sub) in enumerate((("09.b", "2", "TERMO OU SOMA?", "“no 12º mês” → termo | “em 12 meses” → soma"),
                                            ("09.c", "3", "A MÉDIA NA SOMA", "8, 11, 14, 17, 20 | 5 · 14 = 70"))):
        ak, dk = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 230 + k * 310
        rrect(c, 1160, y + dk, 600, 290, 24, mix("#F7F7F5", GREEN, 0.10), ak)
        badge_num(c, n, 1230, y + 60 + dk, ak, 30, bg=GREEN)
        fit(c, tit, 1285, y + 74 + dk, 36, 450, "black", GREEN, ak)
        yy = y + 150 + dk
        for ln in sub.split(" | "):
            yy += para_nb(c, ln, 1460, yy, 30, "bold", INK, ak, 540, 36, align="center") + 8


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
    ("n − 1 saltos", "a₁ = 6, r = 4: a₁₀ = 6 + 10 · 4 = 46", False, "o 10 da posição parece o número de saltos",
     "do 1º ao 10º degrau: 9 saltos", "6 + 9 · 4 = 42", 0),
    ("a soma divide por 2", "5, 9, …, 41: S = 10 · 46 = 460", False, "juntar os extremos parece a conta inteira",
     "duas escadas formam um retângulo: divida por 2", "S = 230", 2),
    ("termo ou soma?", "R$ 20 e +R$ 5 por mês: “no 6º mês” é termo; “em 6 meses” é soma", True,
     "as duas frases quase não mudam", "“no” é um depósito (R$ 45) · “em” é o total", "no ≠ em", 3),
    ("razão = 2º − 1º", "a razão de (50, 43, 36) é 7", False, "a distância entre os números é 7",
     "43 − 50 = −7: a escada desce", "r = −7", 0),
    ("o + 1 do primeiro", "múltiplos de 6 de 102 a 498: (498 − 102) ÷ 6 + 1 = 67", True, "o + 1 parece sobrar",
     "a divisão conta os intervalos; o + 1, o primeiro poste", "67 múltiplos", 1),
    ("meios + 2 extremos", "3 meios entre 2 e 18: r = 16 ÷ 3", False, "são 3 números novos",
     "5 termos, 4 saltos: 2, 6, 10, 14, 18", "r = 4", 1),
    ("diferença constante", "(3, 6, 12, 24) é uma PA", False, "a sequência cresce certinha",
     "diferenças 3, 6, 12 mudam: cada termo dobra (PG)", "é PG", 0),
    ("lados divididos", "fila de quadrados de palitos: figura n = 3n + 1", True, "cada quadrado tem 4 lados",
     "vizinhos dividem um lado · n = 1 → 4", "4, 7, 10", 0),
    ("o termo zero", "R$ 500 a 2%: mês 6 = 500 + 5 · 10", False, "o n − 1 virou costume",
     "o capital é o chão: no mês 6 subiram 6 degraus", "R$ 560", 3),
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
        rrect(c, W / 2 - 560, 700, 1120, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "primeiros termos · termo ou soma? · a conta", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="QUANTOS PALITOS?", area="PADRÃO DE FIGURAS", ic=0, ok="C",
               enun=[("a", "Uma fila de triângulos é feita com palitos. A figura 1 tem 3 palitos, e cada triângulo novo "
                           "acrescenta 2.", False),
                     ("b", "Quantos palitos tem a figura 40?", True)],
               alts=[("A", "79", "39 triângulos", AMBER), ("B", "80", "esqueceu o palito inicial", AMBER),
                     ("C", "81", "", GREEN), ("D", "83", "40 saltos", RED), ("E", "120", "3 por triângulo", RED)],
               passos=[("d", "3, 5, 7, …   r = 2"), ("a", "da figura 1 à 40: 39 saltos"), ("a", "3 + 39 · 2 = 81")],
               confere=("v", "2n + 1 · n = 1 → 3")),
    "q2": dict(ids=("23", "24"), titulo="TERMO OU SOMA?", area="POUPANÇA", ic=1, ok="A",
               enun=[("a", "Uma pessoa deposita R$ 30,00 no 1º mês e, a cada mês, R$ 10,00 a mais.", False),
                     ("b", "Quanto terá depositado ao todo em 10 meses?", True)],
               alts=[("A", "R$ 750,00", "", GREEN), ("B", "R$ 120,00", "só o 10º depósito", AMBER),
                     ("C", "R$ 300,00", "30 · 10, sem os aumentos", RED), ("D", "R$ 800,00", "a₁₀ = 130: 10 saltos", RED),
                     ("E", "R$ 1.500,00", "sem dividir por 2", RED)],
               passos=[("d", "“ao todo” → SOMA"), ("a", "a₁₀ = 30 + 9 · 10 = 120"), ("a", "S = (30 + 120) · 10 ÷ 2 = 750")],
               confere=None),
    "q3": dict(ids=("25", "26"), titulo="QUANTOS POSTES?", area="CONTAGEM", ic=2, ok="E",
               enun=[("a", "Ao longo de 1 km de estrada, serão instalados postes a cada 40 m, com um poste em cada ponta.",
                      False),
                     ("b", "Quantos postes serão instalados?", True)],
               alts=[("A", "24", "tirou uma ponta", RED), ("B", "25", "contou os intervalos", AMBER),
                     ("C", "27", "um a mais em cada ponta", RED), ("D", "40", "o espaçamento, em metros", RED),
                     ("E", "26", "", GREEN)],
               passos=[("d", "1 km = 1 000 m"), ("d", "1 000 ÷ 40 = 25 intervalos"), ("a", "postes = 25 + 1 = 26")],
               confere=None),
    "q4": dict(ids=("27", "28"), titulo="OS MEIOS ARITMÉTICOS", area="INTERPOLAÇÃO", ic=3, ok="B",
               enun=[("a", "Entre 10 e 35 serão colocados 4 meios aritméticos.", False),
                     ("b", "Qual é a razão dessa PA?", True)],
               alts=[("A", "≈ 4,17", "dividiu pelos 6 termos", RED), ("B", "5", "", GREEN),
                     ("C", "6,25", "dividiu pelos 4 meios", AMBER), ("D", "7", "35 ÷ 5, sem tirar o 10", RED),
                     ("E", "25", "esqueceu de dividir", RED)],
               passos=[("d", "4 meios + 2 extremos = 6 termos"), ("d", "6 termos → 5 saltos"), ("a", "(35 − 10) ÷ 5 = 5")],
               confere=("v", "10, 15, 20, 25, 30, 35")),
    "q5": dict(ids=("29", "30"), titulo="SOMA PELO TERMO DO MEIO", area="SOMA", ic=4, ok="D",
               enun=[("a", "Uma PA tem 15 termos, e o 8º termo (o do meio) vale 12.", False),
                     ("b", "Qual é a soma dos 15 termos?", True)],
               alts=[("A", "90", "dividiu por 2 sem precisar", AMBER), ("B", "168", "14 termos", RED),
                     ("C", "192", "16 termos", RED), ("D", "180", "", GREEN), ("E", "360", "15 · 24, sem ÷ 2", RED)],
               passos=[("d", "ímpar: o do meio é a média"), ("a", "S = termos × média"), ("a", "S = 15 · 12 = 180")],
               confere=None),
}


def triangulos_q1(c, x0, y0, n, a, u=56):
    """a fila de triângulos de palitos, figura n"""
    if a <= 0:
        return
    for k in range(n):
        x = x0 + k * u
        if k == 0:
            palito_s(c, x, y0, x + u / 2, y0 - u * 0.86, a)
        palito_s(c, x, y0, x + u, y0, a)
        palito_s(c, x + u, y0, x + u / 2, y0 - u * 0.86, a)


def palito_s(c, x1, y1, x2, y2, a):
    line(c, x1, y1, x2, y2, MADEIRA, a, 7)
    c.drawCircle(x2, y2, 6, paint(RED, a))


def postes_q3(c, x0, y0, a, prog):
    """trecho com postes: 25 intervalos, 26 postes (esquemático: 6 visíveis com '…')"""
    if a <= 0:
        return
    line(c, x0, y0, x0 + 600, y0, INK2, a, 5)
    xs = [x0 + 20, x0 + 120, x0 + 220, x0 + 380, x0 + 480, x0 + 580]
    for k, x in enumerate(xs):
        ak = a * ep(prog * 6, k, 0.6)
        poste_ic_um(c, x, y0, 110, ak, GREEN if k in (0, 5) else INK2)
    text_mid(c, "…", x0 + 300, y0 - 50, 50, "black", GRAY, a)
    for k in (0, 1, 3, 4):
        p = skia.Path(); p.moveTo(xs[k] + 8, y0 + 14); p.quadTo((xs[k] + xs[k + 1]) / 2, y0 + 50, xs[k + 1] - 8, y0 + 14)
        c.drawPath(p, paint(AMBER, a, stroke=4))
    ftext(c, "40 m", (xs[0] + xs[1]) / 2, y0 + 80, 24, "black", AMBER, a, align="center")


def meios_q4(c, x0, y0, a, prog):
    """os 6 termos da PA, com os 5 saltos de +5"""
    if a <= 0:
        return
    vals = (10, 15, 20, 25, 30, 35)
    for k, v in enumerate(vals):
        ak = a * ep(prog * 6, k, 0.6)
        x = x0 + k * 105
        ext = k in (0, 5)
        c.drawCircle(x, y0, 40, paint(PURPLE if ext else "#FFFFFF", ak))
        c.drawCircle(x, y0, 40, paint(PURPLE, ak, stroke=5))
        fmid(c, str(v), x, y0, 34, "black", "#FFFFFF" if ext else PURPLE, ak)
        if k < 5:
            p = skia.Path(); p.moveTo(x + 12, y0 - 46); p.quadTo(x + 52, y0 - 96, x + 93, y0 - 46)
            c.drawPath(p, paint(GREEN, ak, stroke=4))
            ftext(c, "+5", x + 52, y0 - 88, 24, "black", GREEN, ak, align="center")


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
        if nome == "q1":
            triangulos_q1(c, 220, 700, 3, ep(t, C[f"{s1}.a"] + 1.0, 0.4) * (1 - sol))
            fit(c, "figuras 1, 2, 3 …", 470, 690, 26, 300, "bold", INK2, ep(t, C[f"{s1}.a"] + 1.0, 0.4) * (1 - sol))
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720, 760)
        if sol > 0:
            yy = 290
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 34, 640, "black", GREEN if last else INK, a)
                yy += 66
            if nome == "q1":
                triangulos_q1(c, 200, yy + 110, 3, sol)
                fit(c, "3 → 5 → 7", 470, yy + 90, 32, 300, "black", GREEN, sol)
                yy += 140
            if nome == "q3":
                postes_q3(c, 180, yy + 150, sol, ep(t, C[f"{s2}.d"], 2.5))
                yy += 200
            if nome == "q4":
                meios_q4(c, 230, yy + 130, sol, ep(t, C[f"{s2}.a"], 2.0))
                yy += 170
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"] + 0.4, 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 790, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["razão = 2º − 1º", "aₙ = a₁ + (n − 1)r e o porquê", "figuras → termo geral · PA e afim"]),
         ("31.c", "EP. 2", 1, ["média dos vizinhos · x − r, x, x + r", "meios: contar termos e saltos", "múltiplos com o + 1"]),
         ("32.a", "EP. 3", 2, ["S = (a₁ + aₙ) · n ÷ 2 e Gauss", "termos equidistantes", "termo ou soma?"]),
         ("32.b", "EP. 4", 3, ["juros simples: o termo zero", "calendário: razão 7", "treinos progressivos"])]


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
        if ac > 0 and i < 10:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 74, 78), 14, 14), paint(BLUE, ac, stroke=4))
        if ok:
            check_icon(c, x + 33, y + 35, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 35, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos (70%)", 1450, 400, 44, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 200, 600, 1520, 180, BLUE, ac, 0.08)
        for k, ic in enumerate((0, 1, 2)):
            area_icone(c, ic, 290 + k * 110, 690, 0.2, ac)
        text_mid(c, "10 DE CONTEXTO", 1100, 660, 46, "black", BLUE, ac)
        text_mid(c, "padrões · cotidiano · contagem", 1100, 730, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 240, 28, "black", GRAY, aa, tracking=2)
    text(c, "Progressão geométrica", W / 2, 330, 76, "black", PURPLE, aa)
    text(c, "e a soma dos infinitos termos", W / 2, 400, 40, "bold", INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    ac = ep(t, C["34.c"], 0.5)
    for j, (vals, op, col, aj, y) in enumerate((((2, 5, 8, 11, 14), "+3", INK2, ab, 540),
                                                ((2, 6, 18, 54, 162), "×3", GREEN, ac, 710))):
        if aj <= 0:
            continue
        fit(c, "PA" if j == 0 else "PG", 300, y + 14, 40, 120, "black", col, aj, align="center")
        for k, v in enumerate(vals):
            a = aj * ep(t, (C["34.b"] if j == 0 else C["34.c"]) + 0.3 * k, 0.3)
            x = 520 + k * 240
            c.drawCircle(x, y, 56, paint(mix("#FFFFFF", col, 0.18), a))
            c.drawCircle(x, y, 56, paint(col, a, stroke=5))
            fmid(c, str(v), x, y, 44, "black", col, a)
            if k < 4:
                arrow(c, x + 60, y, x + 178, y, col, a, 4, 12)
                ftext(c, op, x + 120, y - 30, 28, "black", col, a, align="center")
    if ac > 0:
        selo(c, 1570, 415, ac, "POR MULTIPLICAÇÃO", GREEN, -3, 26)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
