"""Visual — Função Exponencial, Episódio 6: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, expr, pause_timer, selo, chip...).
Índice visual da revisão: os 5 ícones dos episódios (icone()): escada que multiplica · máquina de tradução · relógio que
apita · tartaruga e lebre · balança dos expoentes.
Ícones de área (area_icone()): bactéria · átomo · termômetro · cifrão · pessoas · tanque · peixe.
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
_s = importlib.util.spec_from_file_location("comum041", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_exponencial_ep6_revisao.mp4"
CARD_R = K.CARD_R
METAL = "#9AA3AD"
AGUA = "#9CCFE6"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'R$ 12', '30 min', '1 280' nem '6 h'"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(mg|min|h|°C|meses|mês|anos|km|%)\b)", " ", s)
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


def curva_exp(c, x0, y0, w, h, col, a, width=6, desce=False, n=40):
    """curva exponencial dentro da caixa (x0, y0, w, h): sobe (ou desce) cada vez mais rápido"""
    if a <= 0:
        return
    p = skia.Path()
    for i in range(n + 1):
        u = i / n
        v = (2 ** (5 * u) - 1) / 31
        if desce:
            v = (2 ** (5 * (1 - u)) - 1) / 31
        x, y = x0 + w * u, y0 + h - h * v
        (p.moveTo if i == 0 else p.lineTo)(x, y)
    c.drawPath(p, paint(col, a, stroke=width))


# ======================================================================
# peças: os 5 ícones dos episódios
# ======================================================================

def escada(c, a):
    """ep1: a escada que multiplica (1, 2, 4, 8) e a parede invisível embaixo"""
    for k, v in enumerate((1, 2, 4, 8)):
        hh = 26 * v
        rrect(c, -170 + k * 88, 120 - hh, 70, hh, 8, mix("#FFFFFF", BLUE, 0.25 + 0.18 * k), a)
        if k:
            ftext(c, "×2", -150 + k * 88 - 30, 100 - hh - 18, 24, "black", GREEN, a, align="center")
    line(c, -200, 140, 200, 140, AMBER, a, 4, dash=[12, 8])


def maquina(c, a):
    """ep2: a máquina de tradução (frase → fator)"""
    rrect(c, -90, -90, 180, 180, 20, mix("#FFFFFF", PURPLE, 0.25), a, shadow=True)
    c.drawCircle(0, 0, 42, paint(PURPLE, a, stroke=10))
    for k in range(8):
        ang = k * math.pi / 4
        line(c, 42 * math.cos(ang), 42 * math.sin(ang), 60 * math.cos(ang), 60 * math.sin(ang), PURPLE, a, 10)
    rrect(c, -205, -30, 100, 60, 10, "#FFFFFF", a, shadow=True)
    ftext(c, "−15%", -155, 12, 26, "black", RED, a, align="center")
    arrow(c, 95, 0, 135, 0, INK2, a, 5, 12)
    rrect(c, 140, -30, 90, 60, 10, "#FFFFFF", a, shadow=True)
    ftext(c, "0,85", 185, 12, 26, "black", GREEN, a, align="center")


def relogio(c, a):
    """ep3: o relógio que apita (o expoente conta os intervalos)"""
    c.drawCircle(0, 10, 120, paint("#FFFFFF", a))
    c.drawCircle(0, 10, 120, paint(INK2, a, stroke=10))
    for k in range(12):
        ang = k * math.pi / 6
        line(c, 100 * math.cos(ang), 10 + 100 * math.sin(ang), 112 * math.cos(ang), 10 + 112 * math.sin(ang), INK2, a, 4)
    line(c, 0, 10, 0, -70, INK, a, 8)
    line(c, 0, 10, 55, 40, INK, a, 6)
    c.drawCircle(0, 10, 10, paint(INK, a))
    for k, (dx, dy) in enumerate(((-150, -110), (150, -110))):
        for j in range(3):
            p = skia.Path(); r = 18 + j * 14
            p.addArc(skia.Rect.MakeXYWH(dx - r, dy - r, 2 * r, 2 * r), 200 if dx < 0 else -20, 140)
            c.drawPath(p, paint(AMBER, a, stroke=5))


def corrida(c, a):
    """ep4: a tartaruga (reta) sai na frente; a lebre (curva) alcança e passa"""
    arrow(c, -180, 130, 190, 130, INK2, a, 4, 12)
    arrow(c, -170, 150, -170, -150, INK2, a, 4, 12)
    line(c, -170, 40, 170, -60, BLUE, a, 7)
    curva_exp(c, -170, -140, 340, 260, GREEN, a, 7)
    c.drawCircle(95, -38, 13, paint(AMBER, a))
    ftext(c, "reta", 130, -80, 24, "black", BLUE, a, align="center")
    ftext(c, "curva", 30, -120, 24, "black", GREEN, a, align="center")


def balanca_exp(c, a):
    """ep5: a balança dos expoentes (2ˣ = 2⁵ → x = 5)"""
    line(c, 0, 120, 0, -70, INK2, a, 8)
    rrect(c, -60, 120, 120, 20, 6, INK2, a)
    line(c, -170, -70, 170, -70, INK2, a, 7)
    for s_, x in (("2ˣ", -130), ("2⁵", 130)):
        line(c, x, -70, x - 40, 0, METAL, a, 3)
        line(c, x, -70, x + 40, 0, METAL, a, 3)
        p = skia.Path(); p.moveTo(x - 60, 0); p.quadTo(x, 50, x + 60, 0); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", PURPLE, 0.35), a))
        ftext(c, s_, x, -10, 40, "black", PURPLE, a, align="center")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 5 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (escada, maquina, relogio, corrida, balanca_exp)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def bacteria(c, a):
    for (x, y, r) in ((-60, -30, 60), (60, 30, 52), (-20, 80, 38)):
        c.drawOval(skia.Rect.MakeXYWH(x - r * 1.4, y - r, r * 2.8, r * 2), paint(mix("#FFFFFF", GREEN, 0.45), a))
        c.drawOval(skia.Rect.MakeXYWH(x - r * 1.4, y - r, r * 2.8, r * 2), paint(GREEN, a, stroke=5))
        c.drawCircle(x, y, r * 0.3, paint(GREEN, a))


def atomo(c, a):
    for ang in (0, 60, 120):
        c.save(); c.rotate(ang)
        c.drawOval(skia.Rect.MakeXYWH(-150, -50, 300, 100), paint(BLUE, a, stroke=6))
        c.restore()
    c.drawCircle(0, 0, 26, paint(RED, a))


def termometro(c, a):
    rrect(c, -28, -150, 56, 230, 28, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-28, -150, 56, 230), 28, 28), paint(INK2, a, stroke=5))
    c.drawCircle(0, 110, 50, paint(RED, a))
    rrect(c, -12, -60, 24, 170, 12, RED, a)
    for k in range(5):
        line(c, 34, -120 + k * 40, 60, -120 + k * 40, INK2, a, 4)


def cifrao(c, a):
    c.drawCircle(0, 0, 130, paint(AMBER, a))
    c.drawCircle(0, 0, 130, paint(mix(AMBER, INK, 0.3), a, stroke=8))
    ftext(c, "R$", 0, 40, 110, "black", "#FFFFFF", a, align="center")


def pessoas(c, a):
    for k, x in enumerate((-110, 0, 110)):
        c.drawCircle(x, -50 + (k % 2) * 20, 38, paint(mix("#FFFFFF", PURPLE, 0.5), a))
        rrect(c, x - 50, -5 + (k % 2) * 20, 100, 120, 40, PURPLE, a)


def tanque(c, a):
    rrect(c, -140, -130, 280, 260, 20, "#FFFFFF", a)
    rrect(c, -140, -10, 280, 140, 20, AGUA, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-140, -130, 280, 260), 20, 20), paint(INK2, a, stroke=6))
    for (x, y) in ((-60, 40), (30, 80), (70, 20)):
        c.drawCircle(x, y, 14, paint(mix(AGUA, INK, 0.45), a))


def peixe(c, a):
    p = skia.Path(); p.moveTo(-120, 0); p.quadTo(0, -110, 110, 0); p.quadTo(0, 110, -120, 0); p.close()
    c.drawPath(p, paint(BLUE, a))
    t = skia.Path(); t.moveTo(100, 0); t.lineTo(170, -60); t.lineTo(170, 60); t.close()
    c.drawPath(t, paint(BLUE, a))
    c.drawCircle(-60, -14, 12, paint("#FFFFFF", a))


AREA_F = (bacteria, atomo, termometro, cifrao, pessoas, tanque, peixe)


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
    """texto de uma cor (sem quebrar)"""
    fmid(c, nb(s), x, cy, size, "black", col, a)


MANCHETES = [("01.b", "VÍRUS", 0), ("01.b", "BACTÉRIAS", 0), ("01.b", "DÍVIDAS", 3), ("01.b", "REMÉDIOS", 1),
             ("01.b", "RADIOATIVIDADE", 1)]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        x0, yb = 200, 720
        arrow(c, x0 - 20, yb, x0 + 620, yb, INK2, aa, 4, 12)
        arrow(c, x0, yb + 20, x0, 230, INK2, aa, 4, 12)
        curva_exp(c, x0 + 10, 260, 580, 450, GREEN, aa, 9)
    for k, (cue, s, ic) in enumerate(MANCHETES):
        a, d = rise(t, C[cue] + 0.35 * k)
        if a <= 0:
            continue
        y = 220 + k * 108
        rrect(c, 1000, y + d, 700, 92, 14, "#FFFFFF", a, shadow=True)
        rrect(c, 1000, y + d, 16, 92, 6, RED, a)
        area_icone(c, ic, 1075, y + 46 + d, 0.26, a)
        ftext(c, s, 1140, y + 60 + d, 40, "black", INK, a, align="left")
        ftext(c, "MANCHETE", 1680, y + 56 + d, 20, "black", GRAY, a, align="right")
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        rrect(c, 200, 760, 640, 66, 14, mix("#FFFFFF", AMBER, 0.25), ac)
        text_mid(c, "“resolva a equação”?  quase nunca", 520, 793, 30, "black", INK, ac)
    ad = ep(t, C["01.d"], 0.5)
    selo(c, 1350, 800, ad, "TRADUZA A HISTÓRIA", PURPLE, -4, 36)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        chip(c, "9 V OU F", 330, 866, AMBER, ae, 26)
        chip(c, "5 QUESTÕES NOVAS", 640, 866, GREEN, ep(t, C["01.e"] + 0.5, 0.4), 26)


COBRA = [("02.a", "CRESCIMENTO POR FATOR", "bactérias · populações · seguidores", GREEN, 0),
         ("02.b", "DECAIMENTO E MEIA-VIDA", "remédios · radioatividade · depreciação", RED, 1),
         ("02.c", "RECONHECER O MODELO", "tabela ou gráfico", BLUE, 5),
         ("02.d", "DESCOBRIR O TEMPO", "quando chega lá?", PURPLE, 2)]


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
        area_icone(c, ic, x, 570 + d, 0.42, a)
        para(c, sub, x, 690 + d, 26, "bold", INK2, a, 360, 32, align="center")


RENDE = [("03.a", "“dobra a cada 20 min”", "2", "por período de 20 min", GREEN),
         ("03.b", "“cresce 3% ao ano”", "1,03", "1 + 0,03", GREEN),
         ("03.c", "“perde 15% ao ano”", "0,85", "o que sobra", RED),
         ("03.d", "“meia-vida de 8 dias”", "1/2", "a cada 8 dias", RED)]


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "TRADUZA A FRASE NO FATOR", PURPLE)
    a0 = ep(t, C["03.t"], 0.5)
    text(c, "FRASE DO ENUNCIADO", 520, 230, 26, "black", GRAY, a0, tracking=2)
    text(c, "FATOR", 1280, 230, 26, "black", GRAY, a0, tracking=2)
    for k, (cue, frase, fator, sub, col) in enumerate(RENDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 125
        rrect(c, 200, y + d, 640, 100, 16, "#FFFFFF", a, shadow=True)
        fit(c, frase, 520, y + 62 + d, 36, 600, "black", INK, a, align="center")
        arrow(c, 870, y + 50 + d, 1080, y + 50 + d, PURPLE, a, 6, 16)
        rrect(c, 1110, y + d, 340, 100, 16, mix("#FFFFFF", col, 0.15), a)
        fit(c, fator, 1280, y + 68 + d, 56, 300, "black", col, a, align="center")
        fit(c, sub, 1490, y + 62 + d, 28, 330, "bold", INK2, a)
    ae = ep(t, C["03.e"], 0.5)
    if ae > 0:
        boxed(c, 400, 800, 1120, 76, GREEN, ae, 0.10)
        text_mid(c, "fator + valor inicial → a lei sai sozinha", W / 2, 838, 34, "black", GREEN, ae)


INDICE = [("EP. 1", "a escada que multiplica · a parede invisível · expoente negativo: de cabeça para baixo"),
          ("EP. 2", "a receita: Q₀ e a · o fator é o que sobra · juros de terno e gravata"),
          ("EP. 3", "o relógio que apita · a pizza que sobrou"),
          ("EP. 4", "a tartaruga e a lebre ao contrário · o teste da razão"),
          ("EP. 5", "as duas fotos idênticas · tire a embalagem · a ladeira inverte")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b", "05.c"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 240 + k * 360
        y = 210
        rrect(c, x - 165, y, 330, 620, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 165, y, 330, 620), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 145, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 200, 0.62, a)
        yy = y + 350
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 25, "black", INK if on_ else INK2, a, 290, 31, align="center") + 10


ONDE = [("06.a", "BIOLOGIA", 0, "curva em J", "recursos limitados → S", GREEN),
        ("06.b", "QUÍMICA", 1, "carbono-14", "meia-vida ≈ 5 730 anos", BLUE),
        ("07.c", "FÍSICA", 2, "resfriamento", "tende à temperatura da sala", RED),
        ("07.d", "FINANCEIRA", 3, "juros compostos", "fator 1 + i", AMBER),
        ("07.e", "GEOGRAFIA", 4, "Malthus", "população × alimentos", PURPLE)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA CURVA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 240 + k * 360
        rrect(c, x - 165, 220 + d, 330, 560, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 28, "black", col, a, 300, 34, align="center")
        area_icone(c, ic, x, 450 + d, 0.40, a)
        fit(c, lei_, x, 630 + d, 32, 300, "black", INK, a, align="center")
        para(c, res, x, 680 + d, 25, "bold", INK2, a, 290, 31, align="center")
    ae = ep(t, C["07.e"] + 1.2, 0.5)
    if ae > 0:
        boxed(c, 460, 820, 1000, 72, AMBER, ae, 0.10)
        text_mid(c, "população em PG × alimentos em PA = exponencial × afim", W / 2, 856, 30, "black", INK, ae)


HABITOS = [("08.a", "1", "CONTE OS INTERVALOS", "2 h dobrando a cada 20 min · 120 ÷ 20 = 6 · converta as unidades antes"),
           ("08.b", "2", "TESTE EM t = 0, 1 E 2", "a reta acerta dois pontos · e erra o terceiro"),
           ("09.c", "3", "NÃO FECHOU? LOGARITMO", "deu log 2 ou log 3? · próxima série")]


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
    ("o fator é o que sobra", "perde 10% ao ano → fator 0,1", False, "o 10% está escrito no enunciado",
     "perdeu 10, ficou com 90", "fator 0,9", 1),
    ("taxa vira fator", "cresce 5% ao ano → fator 1,05", True, "muita gente escreve 5 como fator",
     "some 1: os 100% de antes + 5%", "1 + 0,05", 1),
    ("a pizza que sobrou", "3 meias-vidas → sobra 12,5%", True, "três metades parecem não deixar nada",
     "cada meia-vida corta o que sobrou: 50 · 25 · 12,5", "12,5%", 2),
    ("duplicações", "dobra 5 vezes → fica 10 vezes maior", False, "5 × 2 parece a conta",
     "duplicações se multiplicam: 2 · 4 · 8 · 16 · 32", "×2⁵ = ×32", 0),
    ("expoente negativo", "2⁻² = −4", False, "o sinal parece passar para o resultado",
     "o expoente negativo vira a fração de cabeça para baixo", "2⁻² = 1/4", 0),
    ("o número da frente", "5 · 2³ = 10³ = 1 000", False, "5 × 2 = 10 parece andar junto",
     "o número da frente não entra na base: 5 · 8", "= 40", 4),
    ("a ladeira", "(1/2)ˣ > 8 → x < −3", True, "8 = (1/2)⁻³ dá vontade de escrever x > −3",
     "base entre 0 e 1: a desigualdade vira", "x < −3", 4),
    ("tire a embalagem", "100 · 3ᵗ = 2 700 → 300ᵗ = 2 700", False, "parece só uma multiplicação",
     "divida por 100 primeiro: 3ᵗ = 27 = 3³", "t = 3", 4),
    ("três pontos", "10, 20, 40: a lei 10 + 10t acerta t = 0 e t = 1 → é a certa", False,
     "dois pontos certos parecem prova", "teste o terceiro: em t = 2 dá 30, não 40", "10 · 2ᵗ", 3),
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
        text_mid(c, "escreva o fator e o número de intervalos", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

def fig_tabela(c, x0, y0, a):
    """a tabela da Q3: poluente (mg) a cada hora"""
    if a <= 0:
        return
    rrect(c, x0, y0, 600, 150, 14, "#FFFFFF", a, shadow=True)
    line(c, x0, y0 + 75, x0 + 600, y0 + 75, LIGHT, a, 3)
    ftext(c, "t (h)", x0 + 70, y0 + 50, 28, "black", INK2, a, align="center")
    ftext(c, "N (mg)", x0 + 70, y0 + 125, 28, "black", INK2, a, align="center")
    for k, v in enumerate((64, 48, 36, 27)):
        x = x0 + 210 + k * 110
        ftext(c, str(k), x, y0 + 50, 30, "black", INK2, a, align="center")
        ftext(c, str(v), x, y0 + 125, 36, "black", BLUE, a, align="center")


Q = {
    "q1": dict(ids=("21", "22"), titulo="O CELULAR QUE DESVALORIZA", area="DEPRECIAÇÃO", ic=3, ok="C", fig=None,
               enun=[("a", "Um celular custou R$ 2.000,00 e perde 20% do valor por ano, sempre sobre o valor do ano anterior.", False),
                     ("b", "O valor depois de 2 anos é:", True)],
               formula=None,
               alts=[("A", "R$ 80,00", "fator 0,2", RED), ("B", "R$ 1.200,00", "−40% de uma vez", AMBER),
                     ("C", "R$ 1.280,00", "", GREEN), ("D", "R$ 1.600,00", "um ano só", AMBER),
                     ("E", "R$ 2.880,00", "fator 1,2", RED)],
               passos=[("d", "fator = o que sobra: 0,8 · 2 intervalos"), ("a", "2 000 · 0,8² = 2 000 · 0,64"),
                       ("b", "= R$ 1.280,00")],
               confere=("v", "perdeu 36%: menos que os 40% “somados”")),
    "q2": dict(ids=("23", "24"), titulo="O REMÉDIO NO SANGUE", area="MEIA-VIDA", ic=1, ok="B", fig=None,
               enun=[("a", "Um paciente tem 240 mg de um remédio no sangue. A meia-vida é de 6 h.", False),
                     ("b", "Depois de 24 h, restam:", True)],
               formula=None,
               alts=[("A", "7,5 mg", "5 meias-vidas", AMBER), ("B", "15 mg", "", GREEN),
                     ("C", "30 mg", "3 meias-vidas", AMBER), ("D", "60 mg", "dividiu por 4", RED),
                     ("E", "0 mg", "−50% duas vezes", RED)],
               passos=[("d", "24 ÷ 6 = 4 meias-vidas"), ("a", "240 → 120 → 60 → 30 → 15 mg")],
               confere=("xe", "nunca zera: a parede invisível")),
    "q3": dict(ids=("25", "26"), titulo="O POLUENTE NO TANQUE", area="QUAL É A LEI?", ic=5, ok="E", fig="tabela",
               enun=[("a", "Um poluente num tanque (mg), medido a cada hora:", False),
                     ("b", "A lei é:", True)],
               formula=None,
               alts=[("A", "=64 − 16t", "erra t = 2: 32", AMBER), ("B", "=64 · 0,25^t", "a taxa, não o fator", RED),
                     ("C", "=48 · 0,75^t", "começa em t = 1", RED), ("D", "=64 · 0,75 · t", "dá 0 em t = 0", RED),
                     ("E", "=64 · 0,75^t", "", GREEN)],
               passos=[("d", "48 ÷ 64 = 36 ÷ 48 = 27 ÷ 36 = 0,75"), ("a", "teste em t = 0, 1 e 2"),
                       ("b", "só a E dá 64, 48 e 36")],
               confere=None),
    "q4": dict(ids=("27", "28"), titulo="OS PEIXES DO LAGO", area="EQUAÇÃO COM COEFICIENTE", ic=6, ok="C", fig=None,
               enun=[("a", "Os peixes de um lago seguem a lei abaixo, com t em meses.", False),
                     ("b", "A população chega a 6 400 em:", True)],
               formula=("a", "P(t) = 200 · 2^{t/3}"),
               alts=[("A", "cerca de 1,7 mês", "dividiu 5 por 3", RED), ("B", "5 meses", "esqueceu o ÷ 3", AMBER),
                     ("C", "15 meses", "", GREEN), ("D", "48 meses", "potência como produto", RED),
                     ("E", "96 meses", "t/3 = 32", RED)],
               passos=[("d", "tire a embalagem: 6 400 ÷ 200 = 32"), ("a", "32 = 2⁵ → t/3 = 5"),
                       ("b", "t = 15 meses")],
               confere=None),
    "q5": dict(ids=("29", "30"), titulo="O FORNO DESLIGADO", area="RESFRIAMENTO E INEQUAÇÃO", ic=2, ok="D", fig=None,
               enun=[("a", "Um forno foi desligado. Temperatura em °C, com t em minutos:", False),
                     ("b", "Fica ACIMA de 40 °C:", True)],
               formula=("a", "T(t) = 20 + 160 · 0,5^{t/10}"),
               alts=[("A", "por menos de 3 min", "esqueceu o ÷ 10", RED), ("B", "por menos de 20 min", "não tirou os 20 °C", AMBER),
                     ("C", "por mais de 30 min", "não inverteu", RED), ("D", "por menos de 30 min", "", GREEN),
                     ("E", "sempre: nunca cai abaixo de 40 °C", "a parede é 20 °C", RED)],
               passos=[("d", "=160 · 0,5^{t/10} > 20"), ("a", "=0,5^{t/10} > 1/8 = 0,5^3"),
                       ("b", "ladeira: t/10 < 3 → t < 30 min")],
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
        K.alternativas(c, t, C, [(L, s if s.startswith("=") else nb(s), w, col) for L, s, w, col in d["alts"]],
                       880, 230, 820, 30, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        area_icone(c, d["ic"], 770, 222, 0.26, a0 * (1 - sol))
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
            if not dest and d["formula"]:
                af = ep(t, C[f"{s1}.{d['formula'][0]}"] + 0.6, 0.4) * (1 - sol)
                K.expr(c, d["formula"][1], 180, y + 40, 48, af, cores={i: PURPLE for i in range(12)}, align="left")
                y += 110
            if not dest and d["fig"] == "tabela":
                fig_tabela(c, 180, y, ep(t, C[f"{s1}.a"] + 0.8, 0.4) * (1 - sol))
                y += 180
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720, 760)
        if sol > 0:
            yy = 300
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.6 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                if s.startswith("="):
                    K.expr(c, s[1:], 180, yy + 2, 40, a, align="left")
                    yy += 90
                    continue
                fit(c, s, 180, yy + 14, 34, 640, "black", GREEN if last else INK, a)
                yy += 66
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 760, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["base > 0 e ≠ 1 · expoente negativo", "gráfico, (0, 1) e assíntota"]),
         ("31.c", "EP. 2", 1, ["taxa vira fator", "a lei Q₀ · aᵗ por dois pontos"]),
         ("31.d", "EP. 3", 2, ["duplicação e meia-vida", "contar os intervalos"]),
         ("32.a", "EP. 4", 3, ["afim × exponencial", "teste da diferença e da razão"]),
         ("32.b", "EP. 5", 4, ["equações: isole e iguale bases", "evidência e inequações"]),
         ("32.c", "PRÓXIMA", None, ["quando precisa de logaritmo"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 200), (150, 380), (150, 560), (990, 200), (990, 380), (990, 560)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE if ic is not None else BLUE, size=20, a=a, bounds=(0, 1920))
        if ic is not None:
            icone(c, ic, x + 50, y0 + 100, 0.2, a)
        for j, it in enumerate(itens):
            yy = y0 + 30 + j * 52
            rrect(c, x + 130, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            fit(c, it, x + 178, yy + 10, 28, 600, "bold", INK, a)
    ae = ep(t, C["32.d"], 0.5)
    if ae > 0:
        boxed(c, 560, 760, 800, 90, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", W / 2, 805, 34, "black", INK, ae)


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
        icone(c, 2, 330, 670, 0.40, ac)
        text_mid(c, "10 DE MEIA-VIDA OU DUPLICAÇÃO", 1060, 640, 44, "black", BLUE, ac)
        text_mid(c, "em contexto: remédio · bactéria · radioatividade", 1060, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 360, 230, 720, 170, 24, "#FFFFFF", aa, shadow=True)
        K.expr(c, "2^x = 10", W / 2, 315, 96, aa, cores={0: INK, 1: INK, 2: RED})
        selo(c, W / 2 + 330, 250, ep(t, C["34.a"] + 1.5, 0.4), "NÃO FECHA", AMBER, -6, 28)
    ab = ep(t, C["34.b"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 490, 28, "black", GRAY, ab, tracking=2)
    text(c, "Logaritmos", W / 2, 580, 80, "black", PURPLE, ab)
    text(c, "definição · propriedades · equações", W / 2, 650, 36, "bold", INK2, ab)
    ac = ep(t, C["34.c"], 0.5)
    if ac > 0:
        boxed(c, 460, 720, 1000, 100, GREEN, ac, 0.10)
        text_mid(c, "a ferramenta que tira a incógnita do expoente", W / 2, 770, 36, "black", GREEN, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
