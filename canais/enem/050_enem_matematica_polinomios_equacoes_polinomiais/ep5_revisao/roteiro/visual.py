"""Visual — Polinômios e Equações Polinomiais, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): caixa de papelão · esteira · molho de chaves · bola quicando.
Ícones de área (area_icone()): caixa · gráfico · moeda (lucro) · carrinho (MUV) · o "i" dos complexos.
Polinômios na tela: texto com sobrescritos unicode (x³, x²) e a esteira de Briot-Ruffini (esteira()).
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
_s = importlib.util.spec_from_file_location("comum050", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_polinomios_ep5_revisao.mp4"
CARD_R = K.CARD_R


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'x − 1', '12 m³', 'P(0) = −6', '25 questões'"""
    s = re.sub(r"(?<=[\dx²³)]) ([−+=]) (?=[\dx(−])", " \\1 ", s)
    s = re.sub(r"(?<=\d) (?=(m|cm|m²|cm²|m³|questões|acertos)\b)", " ", s)
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


# ======================================================================
# a esteira de Briot-Ruffini
# ======================================================================

def esteira(c, x, y, raiz, coefs, res, a, prog=1.0, cw=96, size=40, col_raiz=PURPLE, zero_hi=None):
    """dispositivo prático: raiz à esquerda, coeficientes em cima, resultados embaixo (aparecem com prog 0→1)"""
    if a <= 0:
        return
    n = len(coefs)
    w = cw * n
    line(c, x + cw, y - 10, x + cw, y + 130, INK, a, 4)
    line(c, x + cw - 20, y + 66, x + cw + w + 10, y + 66, INK, a, 4)
    ftext(c, raiz, x + cw / 2, y + 44, size, "black", col_raiz, a, align="center")
    for j, s in enumerate(coefs):
        cx = x + cw * (j + 1.5)
        if zero_hi is not None and j == zero_hi:
            rrect(c, cx - cw / 2 + 6, y + 4, cw - 12, 54, 10, mix("#FFFFFF", AMBER, 0.45), a)
        ftext(c, s, cx, y + 44, size, "black", INK, a, align="center")
    for j, s in enumerate(res):
        aj = a * max(0.0, min(1.0, prog * len(res) - j))
        if aj <= 0:
            continue
        cx = x + cw * (j + 1.5)
        last = j == len(res) - 1
        if last:
            rrect(c, cx - cw / 2 + 4, y + 76, cw - 8, 58, 10, mix("#FFFFFF", GREEN, 0.35), aj)
        ftext(c, s, cx, y + 118, size, "black", GREEN if last else BLUE, aj, align="center")


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def caixa_ic(c, a, lab="x"):
    """ep1: a caixa de papelão (modelagem: volume = polinômio)"""
    p = skia.Path(); p.moveTo(-150, -40); p.lineTo(60, -40); p.lineTo(140, -110); p.lineTo(-70, -110); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", AMBER, 0.55), a)); c.drawPath(p, paint(mix(AMBER, INK, 0.35), a, stroke=5))
    rrect(c, -150, -40, 210, 170, 4, mix("#FFFFFF", AMBER, 0.75), a, stroke=5, stroke_color=mix(AMBER, INK, 0.35))
    q = skia.Path(); q.moveTo(60, -40); q.lineTo(140, -110); q.lineTo(140, 60); q.lineTo(60, 130); q.close()
    c.drawPath(q, paint(mix("#FFFFFF", AMBER, 0.40), a)); c.drawPath(q, paint(mix(AMBER, INK, 0.35), a, stroke=5))
    line(c, -45, -40, 35, -110, mix(AMBER, INK, 0.35), a, 4)
    if lab:
        ftext(c, lab, -45, 175, 50, "black", BLUE, a, align="center")


def esteira_ic(c, a):
    """ep2: a esteira de Briot-Ruffini"""
    rrect(c, -190, 30, 380, 56, 28, INK2, a)
    for k in range(5):
        c.drawCircle(-150 + k * 75, 58, 16, paint("#FFFFFF", a))
    for k, (s, col) in enumerate((("1", BLUE), ("0", AMBER), ("−4", BLUE))):
        rrect(c, -165 + k * 120, -80, 96, 96, 14, mix("#FFFFFF", col, 0.30), a, stroke=4, stroke_color=col)
        ftext(c, s, -117 + k * 120, -16, 46, "black", col, a, align="center")
    arrow(c, -120, 140, 120, 140, PURPLE, a, 6, 16)


def chaves_ic(c, a):
    """ep3: o molho de chaves das candidatas"""
    c.drawCircle(0, -110, 44, paint(INK2, a, stroke=10))
    for k, (ang, col) in enumerate(((-35, AMBER), (0, GREEN), (35, BLUE))):
        c.save(); c.translate(0, -70); c.rotate(ang)
        c.drawCircle(0, 30, 26, paint(col, a))
        c.drawCircle(0, 30, 10, paint("#FFFFFF", a))
        rrect(c, -9, 52, 18, 150, 6, col, a)
        rrect(c, 9, 160, 26, 14, 4, col, a); rrect(c, 9, 182, 18, 12, 4, col, a)
        c.restore()


def bola_ic(c, a):
    """ep4: a bola que quica ou atravessa"""
    line(c, -200, 90, 200, 90, INK, a, 5)
    p = skia.Path(); p.moveTo(-190, -60); p.quadTo(-110, 250, -40, 90); p.quadTo(30, -80, 90, 90)
    p.quadTo(140, 230, 190, 160)
    c.drawPath(p, paint(PURPLE, a, stroke=6))
    c.drawCircle(-40, 66, 24, paint(AMBER, a))
    c.drawCircle(90, 90, 12, paint(GREEN, a))


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (caixa_ic, esteira_ic, chaves_ic, bola_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def grafico_ic(c, a):
    line(c, -170, 60, 170, 60, INK2, a, 5); line(c, -60, -170, -60, 160, INK2, a, 5)
    p = skia.Path(); p.moveTo(-160, 150); p.cubicTo(-110, -200, 0, 200, 60, 60); p.cubicTo(100, -40, 140, -60, 165, -150)
    c.drawPath(p, paint(BLUE, a, stroke=7))


def moeda_ic(c, a):
    c.drawCircle(0, 0, 140, paint(AMBER, a))
    c.drawCircle(0, 0, 112, paint(mix(AMBER, INK, 0.25), a, stroke=8))
    ftext(c, "R$", 0, 26, 86, "black", "#FFFFFF", a, align="center")


def carro_ic(c, a):
    rrect(c, -160, -40, 320, 90, 26, BLUE, a)
    rrect(c, -90, -100, 170, 70, 24, mix(BLUE, "#FFFFFF", 0.3), a)
    for x in (-90, 90):
        c.drawCircle(x, 60, 36, paint(INK, a)); c.drawCircle(x, 60, 14, paint("#FFFFFF", a))
    line(c, -200, 110, 200, 110, INK2, a, 4)
    ftext(c, "s(t)", 0, 175, 50, "black", PURPLE, a, align="center")


def complexo_ic(c, a):
    c.drawCircle(0, 0, 140, paint(mix("#FFFFFF", PURPLE, 0.22), a))
    c.drawCircle(0, 0, 140, paint(PURPLE, a, stroke=7))
    ftext(c, "i² = −1", 0, 22, 62, "black", PURPLE, a, align="center")


AREA_F = (caixa_ic, grafico_ic, moeda_ic, carro_ic, complexo_ic)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# abertura
# ======================================================================

FRASES = [("01.b", "a é raiz  ⇔  P(a) = 0", BLUE), ("01.c", "resto por x − a  =  P(a)", PURPLE),
          ("01.d", "raiz conhecida baixa o grau até o 2º", GREEN)]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    a0 = ep(t, C["01.a"], 0.5)
    fmid(c, "3 FRASES", W / 2, 250, 64, "black", INK, a0)
    for k, (cue, s, col) in enumerate(FRASES):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 340 + k * 130
        rrect(c, 360, y + d, 1200, 106, 53, mix("#FFFFFF", col, 0.16), a, shadow=True)
        badge_num(c, k + 1, 420, y + 53 + d, a, 30, bg=col)
        fit(c, s, 960, y + 70 + d, 46, 1020, "black", col, a, align="center")
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        chip(c, "9 V OU F", 760, 790, AMBER, ae, 30)
        chip(c, "5 QUESTÕES NOVAS", 1200, 790, GREEN, ep(t, C["01.e"] + 0.5, 0.4), 30)


COBRA = [("02.a", "MODELAR", "volume · área · lucro", BLUE, 0),
         ("02.b", "VALOR E RAÍZES", "o lucro se anula · a altura volta a zero", PURPLE, 2),
         ("02.c", "LER GRÁFICOS", "corta ou toca o eixo", GREEN, 1),
         ("02.d", "RAÍZES × COEFICIENTES", "soma e produto sem resolver", AMBER, 4)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "QUATRO USOS", BLUE)
    for k, (cue, tit, sub_, col, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 185, 230 + d, 370, 560, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 290 + d, a, 26, bg=col)
        para(c, tit, x, 370 + d, 30, "black", col, a, 340, 36, align="center")
        if ic == 4:
            fmid(c, "Girard", x, 540 + d, 60, "black", AMBER, a)
        else:
            area_icone(c, ic, x, 540 + d, 0.42, a)
        yy = 670 + d
        for ln in sub_.split(" · "):
            yy += para_nb(c, ln, x, yy, 26, "black", INK2, a, 330, 32, align="center") + 6


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "UM AVISO DO MATERIAL", "NO ENEM, O POLINÔMIO É MODELO", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 260, 1480, 200, AMBER, aa, 0.10)
        fit(c, "teoria completa", 280, 345, 56, 700, "black", AMBER, aa)
        fit(c, "→ cai mais nos vestibulares tradicionais", 280, 420, 40, 1380, "bold", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        boxed(c, 220, 520, 1480, 240, GREEN, ab, 0.10)
        area_icone(c, 0, 400, 640, 0.55, ab)
        fit(c, "no ENEM: o polinômio é modelo", 600, 610, 46, 1060, "black", GREEN, ab)
        fit(c, "use a ferramenta certa", 600, 690, 40, 1060, "bold", INK, ab)


INDICE = [("EP. 1", "o grau: o andar mais alto · P(1): o raio X · a identidade: notas fiscais item por item"),
          ("EP. 2", "a esteira de Briot-Ruffini · o atalho do pedágio · a raiz mora do lado oposto"),
          ("EP. 3", "raiz e fator: espelhos · o molho de chaves · cada raiz derruba um andar"),
          ("EP. 4", "Girard: menos, mais, menos · a bola quica ou atravessa · o par de meias")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 300, 380, 1320, 160, 30, "#FFFFFF", aq, shadow=True)
        fmid(c, "soma dos coeficientes: P(?)", W / 2, 460, 54, "black", INK, aq)
        pause_timer(c, t, C["04.t"] + 3.2, 1480, 640, a=aq)
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
        icone(c, k, x, y + 190, 0.55, a)
        yy = y + 350
        for ln in s.split(" · "):
            yy += para_nb(c, ln, x, yy, 24, "black", INK if on_ else INK2, a, 340, 30, align="center") + 10


ONDE = [("06.a", "GEOMETRIA ESPACIAL", 0, "volume da caixa: grau 3", BLUE),
        ("06.b", "ECONOMIA", 2, "raízes do lucro = equilíbrio", AMBER),
        ("07.c", "FÍSICA", 3, "voltar à origem é raiz", GREEN),
        ("07.d", "NÚMEROS COMPLEXOS", 4, "raízes não reais aos pares", PURPLE)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS ÁREAS", "O MESMO POLINÔMIO, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 185, 230 + d, 370, 560, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 290 + d, 30, "black", col, a, 340, 36, align="center")
        area_icone(c, ic, x, 480 + d, 0.42, a)
        para_nb(c, res, x, 660 + d, 28, "black", INK, a, 330, 34, align="center")
    sa = ep(t, C["07.d"] + 2.0, 0.4)
    if sa > 0:
        pill(c, "próxima série", 1558, 770, PURPLE, size=22, a=sa, anchor="center")


HABITOS = [("08.a", "RAIZ? SUBSTITUA", "calcule P(a) · é mais rápido que dividir"),
           ("08.b", "RAIZ DADA", "convite a Briot-Ruffini · sobra um 2º grau"),
           ("09.c", "SOMA OU PRODUTO?", "Girard · nem resolva"),
           ("09.d", "GRÁFICO?", "P(0) de cada alternativa · depois raízes e multiplicidades")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "QUATRO HÁBITOS NA HORA H", GREEN)
    for k, (cue, tit, sub_) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 185, 240 + d, 370, 540, 24, mix("#F7F7F5", GREEN, 0.10), a, shadow=True)
        badge_num(c, k + 1, x, 310 + d, a, 34, bg=GREEN)
        para(c, tit, x, 410 + d, 32, "black", GREEN, a, 330, 40, align="center")
        yy = 540 + d
        for ln in sub_.split(" · "):
            yy += para_nb(c, ln, x, yy, 28, "bold", INK, a, 330, 36, align="center") + 14


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
    ("raiz e fator", "raiz −2  →  fator (x − 2)", False, "o 2 aparece nos dois lugares",
     "raiz e fator são espelhos: sinais opostos", "fator (x + 2)", 2),
    ("a esteira", "x³ − 4x + 1  →  1, 0, −4, 1", True, "o x² nem aparece",
     "todo andar tem lugar: o que falta entra com 0", "1 · 0 · −4 · 1", 1),
    ("dividir por x + 3", "por x + 3, a esteira usa 3", False, "o 3 está escrito ali",
     "a raiz do divisor mora do lado oposto", "usa −3", 1),
    ("o teorema do resto", "resto por x − a  =  P(−a)", False, "tem um menos no divisor",
     "o atalho do pedágio usa a raiz do divisor: x − a zera em a", "resto = P(a)", 1),
    ("Girard no 3º grau", "produto das raízes  =  −d/a", True, "no 2º grau era c/a, sem o menos",
     "no 3º grau: menos, mais, menos", "1 · 2 · 3 = 6 = −(−6)/1", 3),
    ("raízes e polinômio", "sabendo as raízes, o polinômio está identificado", False, "as raízes parecem dizer tudo",
     "falta o coeficiente dominante | x² − 3x + 2 e 2x² − 6x + 4", "P = a(x − r₁)(x − r₂)", 2),
    ("multiplicidade", "raiz dupla só toca o eixo", True, "parece que toda raiz corta o eixo",
     "a bola quica: (x − 2)² nunca fica negativo", "toca, não atravessa", 3),
    ("raiz não real", "1 − i pode ser raiz sozinha", False, "o enunciado só cita uma",
     "coeficientes reais: as não reais vêm aos pares", "1 + i também", 3),
    ("soma dos coeficientes", "soma dos coeficientes  =  P(0)", False, "o zero parece o ponto de partida",
     "P(0) é só o termo independente | a soma é o raio X", "soma = P(1)", 0),
]
VF_IDS = [f"{11 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, afirm, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 62 + k * 62, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 300, 420, 0.40, a0)
    fmid(c, ctx.upper(), 960, 280, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = fit(c, afirm, 960, 436, 50, 820, "black", INK, a0, align="center")
    w = ftw(nb(afirm), sz)
    if ar > 0 and not ver:
        strike(c, 960 - w / 2 - 10, 420, 960 + w / 2 + 10, 420, ar, RED, ar)
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
        lns = [x for p_ in regra_.split(" | ") for x in _quebra(nb(p_), 30, 880)]
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 735 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        fit(c, fix, 1460, 740, 40, 440, "black", GREEN, ag, align="center")


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
        text_mid(c, "escolha a ferramenta · resolva · confira", W / 2, 750, 34, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="O RESERVATÓRIO", area="MODELAGEM", ok="C", ic=0, fer="testar a raiz + baixar o grau",
               enun=[("a", "Base quadrada de lado x m · altura (x + 1) m · volume 12 m³", False),
                     ("b", "O lado da base mede:", True)],
               alts=[("A", "3 m", "é a altura", AMBER), ("B", "4 m", "área da base", RED), ("C", "2 m", "", GREEN),
                     ("D", "6 m", "coeficiente lido como raiz", RED), ("E", "12 m", "termo independente", RED)],
               passos=[("d", "x²(x + 1) = 12"), ("a", "x³ + x² − 12 = 0"), ("a", "teste 2: 8 + 4 − 12 = 0"),
                       ("b", "sobra x² + 3x + 6 · Δ < 0"), ("b", "lado = 2 m")]),
    "q2": dict(ids=("23", "24"), titulo="O RESTO SEM DIVIDIR", area="TEOREMA DO RESTO", ok="A", ic="est",
               fer="resto = P(raiz do divisor)",
               enun=[("a", "Resto de x⁴ − 3x² + x + 2 por x + 2:", True)],
               alts=[("A", "4", "", GREEN), ("B", "8", "usou P(2)", AMBER), ("C", "2", "é P(0)", RED),
                     ("D", "1", "é P(1)", RED), ("E", "−20", "esqueceu o 0 na esteira", RED)],
               passos=[("d", "x + 2 zera em −2"), ("a", "P(−2) = 16 − 12 − 2 + 2"), ("a", "resto = 4")]),
    "q3": dict(ids=("25", "26"), titulo="A CAIXA DE GIRARD", area="RELAÇÕES DE GIRARD", ok="E", ic=0,
               fer="Girard (hábito 3)",
               enun=[("a", "Arestas, em cm, são as raízes de · x³ − 9x² + 26x − 24", False),
                     ("b", "A área total, em cm², é:", True)],
               alts=[("A", "9", "soma das arestas", RED), ("B", "24", "é o volume", RED),
                     ("C", "26", "esqueceu de dobrar", AMBER), ("D", "36", "as 12 arestas (4 · 9)", RED),
                     ("E", "52", "", GREEN)],
               passos=[("d", "área = 2 · (ab + ac + bc)"), ("a", "ab + ac + bc = 26"), ("a", "2 · 26 = 52 cm²"),
                       ("v", "arestas 2, 3, 4: 6 + 8 + 12 = 26 ✓")]),
    "q4": dict(ids=("27", "28"), titulo="A LEI DO GRÁFICO", area="LEITURA DE GRÁFICO", ok="E", ic=1,
               fer="raiz vira fator + P(0)",
               enun=[("a", "Grau 3 · toca em x = 1 · atravessa em x = −3 · corta o eixo y em (0, −6)", False),
                     ("b", "A lei é:", True)],
               alts=[("A", "(x − 1)²(x + 3)", "sem o a: P(0) = 3", AMBER),
                     ("B", "−2(x + 1)²(x − 3)", "trocou os sinais", RED),
                     ("C", "−2(x − 1)(x + 3)²", "inverteu as multiplicidades", RED),
                     ("D", "2(x − 1)²(x + 3)", "sinal de a: P(0) = 6", RED),
                     ("E", "−2(x − 1)²(x + 3)", "", GREEN)],
               passos=[("a", "toca em 1: (x − 1)²"), ("a", "atravessa em −3: (x + 3)"), ("b", "P(0) = 3a = −6"),
                       ("b", "a = −2")]),
    "q5": dict(ids=("29", "30"), titulo="O PAR DE MEIAS", area="RAÍZES CONJUGADAS", ok="A", ic=4,
               fer="raiz vira fator + o par conjugado",
               enun=[("a", "Grau 3 · coeficientes reais · dominante 1 · raízes 1 e 2i", False),
                     ("b", "(i² = −1) · Ele é:", True)],
               alts=[("A", "x³ − x² + 4x − 4", "", GREEN), ("B", "x³ − x² − 4x + 4", "usou i² = 1", AMBER),
                     ("C", "x³ + x² + 4x + 4", "trocou o sinal da raiz 1", RED),
                     ("D", "x² + 4", "esqueceu a raiz 1", RED),
                     ("E", "x² − (1 + 2i)x + 2i", "esqueceu o −2i", RED)],
               passos=[("d", "2i é raiz → −2i também"), ("a", "(x − 2i)(x + 2i) = x² + 4"),
                       ("a", "(x − 1)(x² + 4)"), ("a", "x³ − x² + 4x − 4")]),
}


def caixa_q(c, cx, cy, a, rot=("x", "x", "x + 1"), s=1.0):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    caixa_ic(c, a * 0.95, rot[0])
    c.restore()
    ftext(c, rot[2], cx + 175 * s, cy + 30 * s, 34 * s, "black", PURPLE, a, align="left")
    ftext(c, rot[1], cx + 125 * s, cy - 110 * s, 34 * s, "black", BLUE, a, align="left")


def grafico_q4(c, cx, cy, a, mostra_lei=False):
    """o gráfico de −2(x − 1)²(x + 3): toca em 1, atravessa em −3, corta y em −6"""
    if a <= 0:
        return
    sx, sy = 70, 5.5
    line(c, cx - 300, cy, cx + 220, cy, INK2, a, 4)
    line(c, cx, cy - 140, cx, cy + 115, INK2, a, 4)
    p = skia.Path()
    first = True
    xv = -3.6
    while xv <= 1.95:
        yv = -2 * (xv - 1) ** 2 * (xv + 3)
        X, Y = cx + xv * sx, cy - yv * sy
        Y = max(cy - 140, min(cy + 115, Y))
        if first:
            p.moveTo(X, Y); first = False
        else:
            p.lineTo(X, Y)
        xv += 0.05
    c.drawPath(p, paint(BLUE, a, stroke=6))
    for xr, s_, col in ((1, "toca", AMBER), (-3, "atravessa", GREEN)):
        c.drawCircle(cx + xr * sx, cy, 12, paint(col, a))
        if xr == 1:
            ftext(c, s_, cx + xr * sx, cy - 22, 26, "black", col, a, align="center")
        else:
            ftext(c, s_, cx + xr * sx - 18, cy + 44, 26, "black", col, a, align="right")
    c.drawCircle(cx, cy + 6 * sy, 12, paint(PURPLE, a))
    ftext(c, "(0, −6)", cx - 18, cy + 6 * sy + 10, 26, "black", PURPLE, a, align="right")


def fig_q1(c, a, sol, prog):
    if not sol:
        caixa_q(c, 460, 640, a, s=0.9)


def fig_q2(c, a, sol, prog):
    if sol:
        esteira(c, 180, 590, "−2", ["1", "0", "−3", "1", "2"], ["1", "−2", "1", "−1", "4"], a, min(1.0, prog / 3.0),
                cw=100, size=36, zero_hi=1)
    else:
        icone(c, 1, 470, 600, 0.6, a)


def fig_q3(c, a, sol, prog):
    if not sol:
        caixa_q(c, 460, 640, a, rot=("a", "b", "c"), s=0.9)


def fig_q4(c, a, sol, prog):
    if not sol:
        grafico_q4(c, 560, 690, a)


def fig_q5(c, a, sol, prog):
    if not sol:
        area_icone(c, 4, 470, 620, 0.7, a)


FIGS = dict(q1=fig_q1, q2=fig_q2, q3=fig_q3, q4=fig_q4, q5=fig_q5)
Y_PASSOS = dict(q1=280, q2=280, q3=280, q4=280, q5=280)


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
        if d["ic"] == "est":
            icone(c, 1, 770, 222, 0.18, a0)
        else:
            area_icone(c, d["ic"], 770, 222, 0.18, a0)
        y = 250
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            for p_ in s.split(" · "):
                h = para_nb(c, p_, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 560, 40)
                y += h + 8
            y += 4
        FIGS[nome](c, ep(t, C[f"{s1}.a"], 0.4) * (1 - sol), False, 0)
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 760, 790)
        if sol > 0:
            af = ep(t, C[f"{s2}.d"], 0.4) * sol
            pill(c, "FERRAMENTA: " + d["fer"], 180, 250, GREEN, size=22, a=af, bounds=(0, 860))
            yy = 320
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 30, 640, "black", GREEN if last else INK, a)
                yy += 56
            FIGS[nome](c, sol, True, t - C[f"{s2}.a"])
            result_box(c, f"Letra {d['ok']}", 1290, 790, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["grau, P(0) e P(1)", "identidade: coeficiente a coeficiente", "modelo volumes e áreas"]),
         ("31.c", "EP. 2", 1, ["P = D · Q + R", "Briot-Ruffini com os zeros", "resto sem dividir: P(a)"]),
         ("32.a", "EP. 3", 2, ["forma fatorada sem errar sinal", "candidatas do termo independente", "raiz baixa o grau"]),
         ("32.b", "EP. 4", 3, ["Girard: −, +, −", "toca × atravessa", "conjugadas vêm aos pares"])]


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
        if ac > 0 and i < 5:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 86, 86), 14, 14),
                        paint(PURPLE, ac, stroke=4))
        if ok:
            check_icon(c, x + 39, y + 39, 20, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 39, y + 39, 26, "black", INK2, a)
    text(c, "25 questões", 1260, 300, 56, "black", INK, aa)
    text(c, "18 acertos", 1260, 400, 48, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 800, 500, 920, 260, PURPLE, ac, 0.08)
        area_icone(c, 1, 890, 630, 0.30, ac)
        fit(c, "5 de modelagem", 990, 605, 40, 680, "black", PURPLE, ac)
        fit(c, "ou leitura de gráfico", 990, 670, 36, 680, "bold", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 240, 28, "black", GRAY, aa, tracking=2)
    text(c, "Números complexos", W / 2, 330, 72, "black", PURPLE, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 420, 1200, 120, 30, mix("#FFFFFF", BLUE, 0.14), ab, shadow=True)
        text_mid(c, "as raízes não reais que apareceram aqui", W / 2, 480, 40, "black", BLUE, ab)
    ac = ep(t, C["34.c"], 0.5)
    for k, s in enumerate(("1 − i", "2i")):
        a = ac * ep(t, C["34.c"] + 0.5 * k, 0.4)
        if a > 0:
            x = 760 + k * 400
            rrect(c, x - 160, 600, 320, 160, 30, mix("#FFFFFF", PURPLE, 0.20), a, shadow=True)
            text_mid(c, s, x, 680, 72, "black", PURPLE, a)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
