"""Visual — Números Complexos, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): relógio de quatro horas · cancela de pedágio · manivela ·
radar. Ícones de área (area_icone()): P(x) · ciclo trigonométrico · plano com ponto · onda · o "i" das questões.
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
_s = importlib.util.spec_from_file_location("comum051", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_complexos_ep5_revisao.mp4"
CARD_R = K.CARD_R


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra '3 + 4i', 'i² = −1', '20 questões', '135°'"""
    s = re.sub(r"(?<=[\dix²³⁴)]) ([−+=±×÷]) (?=[\dix(−√])", " \\1 ", s)
    s = re.sub(r"(?<=\d) (?=(questões|acertos|graus)\b)", " ", s)
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
# peças: os 4 ícones dos episódios
# ======================================================================

def relogio_ic(c, a, hi=None):
    """ep1: o relógio de quatro horas das potências de i (1, i, −1, −i); hi = casa acesa (0 a 3)"""
    c.drawCircle(0, 0, 150, paint("#FFFFFF", a))
    c.drawCircle(0, 0, 150, paint(PURPLE, a, stroke=8))
    casas = (("1", 0, -105), ("i", 105, 0), ("−1", 0, 105), ("−i", -105, 0))
    for k, (s, x, y) in enumerate(casas):
        on_ = hi == k
        if on_:
            c.drawCircle(x, y, 40, paint(mix("#FFFFFF", GREEN, 0.45), a))
        ftext(c, s, x, y + 17, 46, "black", GREEN if on_ else PURPLE, a, align="center")
    ang = -90 + 90 * (hi if hi is not None else 1)
    x2, y2 = 62 * math.cos(math.radians(ang)), 62 * math.sin(math.radians(ang))
    line(c, 0, 0, x2, y2, INK, a, 8)
    c.drawCircle(0, 0, 12, paint(INK, a))


def cancela_ic(c, a):
    """ep2: a cancela do pedágio do i² (i² paga e vira −1)"""
    rrect(c, -170, -60, 70, 220, 10, INK2, a)
    rrect(c, -100, -40, 290, 36, 18, RED, a)
    for k in range(3):
        rrect(c, -60 + k * 80, -40, 36, 36, 0, "#FFFFFF", a)
    rrect(c, -40, 40, 230, 96, 20, mix("#FFFFFF", PURPLE, 0.25), a, stroke=4, stroke_color=PURPLE)
    ftext(c, "i² → −1", 75, 104, 44, "black", PURPLE, a, align="center")


def manivela_ic(c, a):
    """ep3: a manivela de 90° (vezes i gira o ponto)"""
    line(c, -170, 0, 170, 0, INK2, a, 5); line(c, 0, -170, 0, 170, INK2, a, 5)
    p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(-120, -120, 240, 240), -20, -80)
    c.drawPath(p, paint(PURPLE, a, stroke=7))
    arrow(c, -14, -116, -40, -112, PURPLE, a, 7, 20)
    line(c, 0, 0, 112, -40, BLUE, a, 6); c.drawCircle(112, -40, 16, paint(BLUE, a))
    line(c, 0, 0, 40, -112, GREEN, a, 6); c.drawCircle(40, -112, 16, paint(GREEN, a))
    ftext(c, "× i", 120, 110, 50, "black", PURPLE, a, align="center")


def radar_ic(c, a):
    """ep4: o radar (distância e direção)"""
    for r in (60, 110, 160):
        c.drawCircle(0, 0, r, paint(mix("#FFFFFF", GREEN, 0.15) if r == 160 else "#FFFFFF", a))
        c.drawCircle(0, 0, r, paint(GREEN, a, stroke=4))
    line(c, -160, 0, 160, 0, mix(GREEN, INK, 0.3), a, 3); line(c, 0, -160, 0, 160, mix(GREEN, INK, 0.3), a, 3)
    x, y = 150 * math.cos(math.radians(-45)), 150 * math.sin(math.radians(-45))
    line(c, 0, 0, x, y, INK, a, 7)
    c.drawCircle(x * 0.72, y * 0.72, 18, paint(AMBER, a))
    p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(-50, -50, 100, 100), 0, -45)
    c.drawPath(p, paint(PURPLE, a, stroke=6))
    ftext(c, "θ", 70, -16, 40, "black", PURPLE, a, align="center")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (relogio_ic, cancela_ic, manivela_ic, radar_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def polinomio_ic(c, a):
    rrect(c, -160, -100, 320, 200, 30, mix("#FFFFFF", BLUE, 0.18), a, stroke=6, stroke_color=BLUE)
    ftext(c, "P(x)", 0, 30, 90, "black", BLUE, a, align="center")


def ciclo_ic(c, a):
    line(c, -170, 0, 170, 0, INK2, a, 4); line(c, 0, -170, 0, 170, INK2, a, 4)
    c.drawCircle(0, 0, 130, paint(AMBER, a, stroke=7))
    x, y = 130 * math.cos(math.radians(-60)), 130 * math.sin(math.radians(-60))
    line(c, 0, 0, x, y, INK, a, 6); c.drawCircle(x, y, 14, paint(AMBER, a))


def plano_ic(c, a):
    line(c, -170, 120, 170, 120, INK2, a, 5); line(c, -120, -170, -120, 170, INK2, a, 5)
    for (x, y, col) in ((40, -60, BLUE), (130, 40, GREEN)):
        c.drawCircle(x, y, 18, paint(col, a))
    line(c, 40, -60, 130, 40, PURPLE, a, 5)


def onda_ic(c, a):
    line(c, -180, 0, 180, 0, INK2, a, 4)
    p = skia.Path(); p.moveTo(-180, 0)
    for k in range(1, 73):
        x = -180 + k * 5
        p.lineTo(x, -110 * math.sin(math.radians(k * 10)))
    c.drawPath(p, paint(GREEN, a, stroke=7))


def i_ic(c, a):
    c.drawCircle(0, 0, 140, paint(mix("#FFFFFF", PURPLE, 0.22), a))
    c.drawCircle(0, 0, 140, paint(PURPLE, a, stroke=7))
    ftext(c, "i", 0, 48, 150, "black", PURPLE, a, align="center")


AREA_F = (polinomio_ic, ciclo_ic, plano_ic, onda_ic, i_ic)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# abertura
# ======================================================================

IDEIAS = [("Δ < 0", "sem raiz real, mas com um par conjugado", BLUE),
          ("i² = −1", "em toda conta", PURPLE),
          ("um ponto", "todo complexo mora no plano", GREEN)]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    a0 = ep(t, C["01.a"], 0.5) * (1 - ep(t, C["01.b"], 0.4))
    if a0 > 0:
        rrect(c, 360, 300, 1200, 300, 30, mix("#FFFFFF", AMBER, 0.14), a0, shadow=True)
        fmid(c, "SENDO HONESTO", W / 2, 400, 40, "black", AMBER, a0)
        fit(c, "quase não cai de forma direta no ENEM", 960, 500, 50, 1100, "black", INK, a0, align="center")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        fmid(c, "3 IDEIAS QUE SE REAPROVEITAM", W / 2, 250, 52, "black", INK, ab)
    for k, (tit, sub_, col) in enumerate(IDEIAS):
        a, d = rise(t, C["01.b"] + 0.6 + 0.5 * k)
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 320 + d, 500, 380, 28, mix("#FFFFFF", col, 0.14), a, shadow=True)
        badge_num(c, k + 1, x, 380 + d, a, 28, bg=col)
        fit(c, tit, x, 520 + d, 66, 440, "black", col, a, align="center")
        para_nb(c, sub_, x, 600 + d, 30, "bold", INK, a, 420, 38, align="center")
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        chip(c, "9 V OU F", 760, 800, AMBER, ae, 30)
        chip(c, "5 QUESTÕES NOVAS", 1200, 800, GREEN, ep(t, C["01.e"] + 0.5, 0.4), 30)


COBRA = [("02.a", "DELTA NEGATIVO", "sem raiz real · com par conjugado", BLUE, 4),
         ("02.b", "FORMA a + bi", "contas · potências de i", PURPLE, 4),
         ("02.c", "NO PLANO", "módulo = distância · × i = giro de 90°", GREEN, 2),
         ("02.d", "TRIGONOMÉTRICA", "potências grandes", AMBER, 1)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "QUANDO APARECE", BLUE)
    for k, (cue, tit, sub_, col, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 185, 230 + d, 370, 560, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 290 + d, a, 26, bg=col)
        para(c, tit, x, 370 + d, 30, "black", col, a, 340, 36, align="center")
        if k == 0:
            fmid(c, "Δ < 0", x, 540 + d, 64, "black", BLUE, a)
        elif k == 1:
            fmid(c, "3 + 4i", x, 540 + d, 64, "black", PURPLE, a)
        else:
            area_icone(c, ic, x, 540 + d, 0.42, a)
        yy = 670 + d
        for ln in sub_.split(" · "):
            yy += para_nb(c, ln, x, yy, 26, "black", INK2, a, 330, 32, align="center") + 6


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "A DICA QUE MAIS RENDE", "DO PRÓPRIO MATERIAL", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 250, 1480, 200, BLUE, aa, 0.10)
        area_icone(c, 4, 380, 350, 0.45, aa)
        fit(c, "trate o i como uma letra qualquer", 540, 370, 52, 1100, "black", BLUE, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        boxed(c, 220, 500, 1480, 260, GREEN, ab, 0.10)
        fit(c, "no fim:  i²  →  −1", 280, 600, 64, 1300, "black", GREEN, ab)
        fit(c, "esquecer a troca ou errar o sinal: quase todo erro vem daqui", 280, 690, 34, 1380, "bold", INK, ab)


INDICE = [("EP. 1", "i: a letra com superpoder · o relógio de 4 horas · as gêmeas espelhadas"),
          ("EP. 2", "o pedágio do i² · o conjugado: espelho · limpar o i do andar de baixo"),
          ("EP. 3", "o endereço no mapa · o módulo: diagonal do retângulo · a manivela de 90°"),
          ("EP. 4", "o endereço do radar: distância e direção · multiplicar: esticar e girar")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 300, 380, 1320, 160, 30, "#FFFFFF", aq, shadow=True)
        fmid(c, "i² = ?", W / 2, 460, 70, "black", INK, aq)
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
        icone(c, k, x, y + 200, 0.58, a)
        yy = y + 360
        for ln in s.split(" · "):
            yy += para_nb(c, ln, x, yy, 24, "black", INK if on_ else INK2, a, 340, 30, align="center") + 10


ONDE = [("06.a", "POLINÔMIOS", 0, "raízes não reais aos pares", BLUE),
        ("06.b", "TRIGONOMETRIA", 1, "multiplicar soma os ângulos", AMBER),
        ("07.c", "GEOMETRIA ANALÍTICA", 2, "distância e rotação de pontos", PURPLE),
        ("07.d", "FÍSICA E ENGENHARIA", 3, "módulo = amplitude · argumento = fase", GREEN)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS ÁREAS", "O MESMO COMPLEXO, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 185, 230 + d, 370, 560, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 290 + d, 30, "black", col, a, 340, 36, align="center")
        area_icone(c, ic, x, 490 + d, 0.42, a)
        yy = 660 + d
        for ln in res.split(" · "):
            yy += para_nb(c, ln, x, yy, 28, "black", INK, a, 330, 34, align="center") + 6


HABITOS = [("08.a", "POTÊNCIA DE i", "resto por 4 · só o resto importa"),
           ("08.b", "DIVISÃO", "× conjugado do denominador · confira de volta"),
           ("09.c", "POTÊNCIA ALTA", "forma trigonométrica · ou (1 + i)² = 2i"),
           ("09.d", "GEOMETRIA?", "desenhe o ponto · elimina o quadrante errado")]


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
    ("a definição", "i² = 1", False, "um número vezes ele mesmo costuma dar positivo",
     "o superpoder do i: i² = −1 é a definição", "i² = −1", 0),
    ("a parte imaginária", "Im(3 − 4i) = −4", True, "a gente quer levar o i junto",
     "a parte imaginária é só o número, sem o i", "−4, sem o i", 0),
    ("o produto", "(2 + 3i)(1 − i) = 2 − 3i", False, "real com real e i com i parece natural",
     "distributiva completa | o i² paga o pedágio", "5 + i", 1),
    ("a divisão", "(4 + 2i) ÷ (1 + i): parte por parte", False, "na soma é parte com parte",
     "limpe o i do andar de baixo: × conjugado", "3 − i", 1),
    ("raízes de negativos", "√−4 · √−9 = −6", True, "juntar daria √36 = 6",
     "escreva com i antes: 2i · 3i = 6i² = −6", "−6", 0),
    ("o módulo", "|3 + 4i| = 7", False, "somar as partes é o mais rápido",
     "módulo é a diagonal do retângulo: Pitágoras", "√(9 + 16) = 5", 2),
    ("o conjugado", "conjugado de 3 + 4i = 3 − 4i", True, "parece que troca os dois sinais",
     "o espelho troca só a parte imaginária | −3 − 4i é o oposto", "3 − 4i", 1),
    ("o argumento", "arg(−1 + i) = 45°", False, "45° é o ângulo da tabela",
     "os sinais escolhem o quadrante: 2º quadrante", "135°", 3),
    ("delta negativo", "Δ < 0: não há raízes", False, "era o que se dizia no 2º grau",
     "não há raízes REAIS | há duas complexas, gêmeas espelhadas", "par conjugado", 0),
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
        text_mid(c, "escreva i² = −1 · resolva · confira", W / 2, 750, 34, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="AS POTÊNCIAS DE i", area="POTÊNCIAS", ok="B", ic=0,
               fer="resto por 4 (o relógio)",
               enun=[("a", "O valor de i⁴⁵ + i⁶² é:", True)],
               alts=[("A", "1 + i", "usou i² = 1", AMBER), ("B", "−1 + i", "", GREEN),
                     ("C", "−1 − i", "errou o resto de 45", RED), ("D", "0", "acha que se anulam", RED),
                     ("E", "−i", "multiplicou: i¹⁰⁷", RED)],
               passos=[("a", "45 = 4 · 11 + 1  →  i"), ("b", "62 = 4 · 15 + 2  →  −1"), ("b", "i + (−1) = −1 + i")]),
    "q2": dict(ids=("23", "24"), titulo="A DIVISÃO", area="DIVISÃO", ok="C", ic=1,
               fer="× conjugado do denominador",
               enun=[("a", "(7 + i) ÷ (1 + i), na forma a + bi, é:", True)],
               alts=[("A", "8 − 6i", "esqueceu o ÷ 2", AMBER), ("B", "7 + i", "dividiu só pelo 1", RED),
                     ("C", "4 − 3i", "", GREEN), ("D", "−3 + 4i", "trocou as partes", RED),
                     ("E", "4 + 3i", "errou o sinal", RED)],
               passos=[("d", "conjugado de 1 + i: 1 − i"), ("a", "em cima: 7 − 7i + i − i² = 8 − 6i"),
                       ("a", "embaixo: 1 + 1 = 2"), ("a", "(8 − 6i) ÷ 2 = 4 − 3i"),
                       ("v", "(4 − 3i)(1 + i) = 7 + i ✓")]),
    "q3": dict(ids=("25", "26"), titulo="O DELTA NEGATIVO", area="EQUAÇÃO DO 2º GRAU", ok="A", ic=4,
               fer="Bhaskara + √−36 = 6i",
               enun=[("a", "Raízes de x² − 2x + 10 = 0 · nos complexos:", True)],
               alts=[("A", "1 ± 3i", "", GREEN), ("B", "−1 ± 3i", "usou b, não −b", RED),
                     ("C", "1 ± 6i", "dividiu só a parte real", AMBER), ("D", "2 ± 6i", "não dividiu por 2a", RED),
                     ("E", "inexistentes", "só vale nos reais", RED)],
               passos=[("a", "Δ = 4 − 40 = −36"), ("a", "√−36 = 6i"), ("b", "x = (2 ± 6i) ÷ 2 = 1 ± 3i"),
                       ("v", "soma 2 · produto 1 + 9 = 10 ✓")]),
    "q4": dict(ids=("27", "28"), titulo="O GIRO HORÁRIO", area="GEOMETRIA NO PLANO", ok="D", ic=2,
               fer="desenhe o ponto · × (−i)",
               enun=[("a", "Gira 5 + 2i em 90° no sentido HORÁRIO · em torno da origem (× −i)", False),
                     ("b", "O novo ponto é:", True)],
               alts=[("A", "−2 + 5i", "giro anti-horário", AMBER), ("B", "5 − 2i", "é o conjugado", RED),
                     ("C", "−5 − 2i", "giro de 180°", RED), ("D", "2 − 5i", "", GREEN),
                     ("E", "2 + 5i", "trocou sem o sinal", RED)],
               passos=[("a", "−i(5 + 2i) = −5i − 2i²"), ("a", "= 2 − 5i"), ("b", "(a, b)  →  (b, −a)")]),
    "q5": dict(ids=("29", "30"), titulo="A POTÊNCIA ALTA", area="POTÊNCIA", ok="B", ic=3,
               fer="uma potência pequena simples",
               enun=[("a", "(1 − i)⁴ vale:", True)],
               alts=[("A", "4", "esqueceu i² = −1", AMBER), ("B", "−4", "", GREEN), ("C", "16", "módulo 2", RED),
                     ("D", "−4i", "ângulo final 270°", RED), ("E", "−8i", "−2i · 4", RED)],
               passos=[("a", "(1 − i)² = 1 − 2i + i² = −2i"), ("a", "(−2i)² = 4i² = −4"),
                       ("v", "radar: (√2)⁴ = 4 · 4 · 315° = 1 260°"), ("v", "= 3 voltas + 180° ✓")]),
}


def plano_q4(c, cx, cy, a, sol, prog, u=34, ext=7):
    """o plano com 5 + 2i e, na solução, o giro horário até 2 − 5i"""
    if a <= 0:
        return
    line(c, cx - ext * u, cy, cx + ext * u, cy, INK2, a, 4)
    line(c, cx, cy - ext * u, cx, cy + ext * u, INK2, a, 4)
    ftext(c, "real", cx + ext * u - 6, cy + 30, 22, "bold", GRAY, a, align="right")
    ftext(c, "imag.", cx + 10, cy - ext * u + 20, 22, "bold", GRAY, a, align="left")
    px, py = cx + 5 * u, cy - 2 * u
    line(c, cx, cy, px, py, BLUE, a, 5)
    c.drawCircle(px, py, 13, paint(BLUE, a))
    ftext(c, "5 + 2i", px + 10, py - 18, 26, "black", BLUE, a, align="left")
    if sol:
        ag = a * min(1.0, max(0.0, (prog - 1.0) / 2.0))
        if ag > 0:
            qx, qy = cx + 2 * u, cy + 5 * u
            p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(cx - 90, cy - 90, 180, 180), -21.8, 90 * ag)
            c.drawPath(p, paint(PURPLE, ag, stroke=5))
            line(c, cx, cy, qx, qy, GREEN, ag, 5)
            c.drawCircle(qx, qy, 13, paint(GREEN, ag))
            ftext(c, "2 − 5i", qx + 14, qy + 10, 26, "black", GREEN, ag, align="left")


def fig_q1(c, a, sol, prog):
    if not sol:
        icone(c, 0, 470, 590, 0.75, a)


def fig_q2(c, a, sol, prog):
    if not sol:
        icone(c, 1, 470, 600, 0.75, a)


def fig_q3(c, a, sol, prog):
    if not sol:
        area_icone(c, 4, 470, 600, 0.7, a)


def fig_q4(c, a, sol, prog):
    if not sol:
        plano_q4(c, 470, 640, a, False, 0, u=28, ext=6)


def fig_q5(c, a, sol, prog):
    if not sol:
        icone(c, 3, 470, 600, 0.75, a)


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
        area_icone(c, 4, 770, 222, 0.18, a0)
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
            if nome == "q4":
                plano_q4(c, 470, 640, sol * ep(t, C[f"{s2}.d"], 0.4), True, t - C[f"{s2}.b"], u=26, ext=6)
            result_box(c, f"Letra {d['ok']}", 1290, 790, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["i² = −1 e raízes de negativos", "parte real e parte imaginária", "Δ < 0 e potências de i"]),
         ("31.c", "EP. 2", 1, ["somar e multiplicar em a + bi", "(a + bi)(a − bi) = a² + b²", "divisão e equações com o conjugado"]),
         ("32.a", "EP. 3", 2, ["o ponto no plano e o módulo", "distância: |z − w|", "vezes i: giro de 90°"]),
         ("32.b", "EP. 4", 3, ["forma trigonométrica e quadrante", "multiplicar: esticar e girar", "De Moivre"])]


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
    for i in range(20):
        r_, k = divmod(i, 5)
        a = aa * ep(t, C["33.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 14
        x, y = 220 + k * 96, 220 + r_ * 100
        col = mix("#E6E6E2", GREEN, ab if ok else 0)
        rrect(c, x, y, 78, 78, 12, col, a)
        if ac > 0 and i < 8:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 86, 86), 14, 14),
                        paint(PURPLE if i < 5 else BLUE, ac, stroke=4))
        if ok:
            check_icon(c, x + 39, y + 39, 20, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 39, y + 39, 26, "black", INK2, a)
    text(c, "20 questões", 1260, 300, 56, "black", INK, aa)
    text(c, "14 acertos", 1260, 400, 48, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 800, 500, 920, 280, PURPLE, ac, 0.08)
        fit(c, "5 de divisão ou potência", 860, 600, 40, 800, "black", PURPLE, ac)
        fit(c, "3 de interpretação no plano", 860, 690, 40, 800, "black", BLUE, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "BLOCO COMPLETO", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 210, 1200, 110, 30, mix("#FFFFFF", GREEN, 0.18), aa, shadow=True)
        text_mid(c, "Álgebra e Funções: concluído", W / 2, 265, 44, "black", GREEN, aa)
    ab = ep(t, C["34.b"], 0.5)
    text(c, "PRÓXIMO: GEOMETRIA PLANA", W / 2, 390, 28, "black", GRAY, ab, tracking=2)
    fit(c, "Ângulos, retas paralelas e transversais", 960, 470, 58, 1500, "black", PURPLE, ab, align="center")
    ac = ep(t, C["34.c"], 0.5)
    if ac > 0:
        rrect(c, 360, 560, 1200, 230, 30, mix("#FFFFFF", AMBER, 0.16), ac, shadow=True)
        icone(c, 3, 520, 675, 0.45, ac)
        fit(c, "somar e comparar ângulos", 700, 650, 46, 820, "black", AMBER, ac)
        fit(c, "é o jogo inteiro", 700, 720, 40, 820, "bold", INK, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
