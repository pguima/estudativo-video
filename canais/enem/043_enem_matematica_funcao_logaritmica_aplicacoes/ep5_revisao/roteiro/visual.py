"""Visual — Função logarítmica e aplicações, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, expr, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): espelho na reta y = x · régua de pH · dois placares ·
medidor de decibéis.
Ícones de área (area_icone()): gráfico · gota · sismógrafo · alto-falante · tubo de ensaio · globo · coração · lápis.
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
_s = importlib.util.spec_from_file_location("comum043", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_logaritmica_ep5_revisao.mp4"
CARD_R = K.CARD_R
AGUA = "#9CCFE6"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'log 2', '80 dB', '1 000', 'pH 7' nem '10⁻¹²'"""
    s = re.sub(r"(?<=log) (?=[\d(xA-Z])", " ", s)
    s = re.sub(r"(?<=[₀-₉]) (?=[\d(x])", " ", s)
    s = re.sub(r"(?<=pH) (?=[\d])", " ", s)
    s = re.sub(r"(?<=\d) (?=(dB|W/m²|mol/L|vezes|vez|%)\b)", " ", s)
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

def espelho_ic(c, a):
    """ep1: a exponencial e o log, espelhados na reta y = x"""
    rrect(c, -190, -190, 380, 380, 30, "#FFFFFF", a, shadow=True)
    line(c, -150, 150, 150, -150, GRAY, a, 4)
    p = skia.Path(); q = skia.Path()
    for k in range(41):
        x = -2.4 + 4.0 * k / 40
        y = 2 ** x
        X, Y = -120 + x * 55, 120 - y * 55
        (p.moveTo if k == 0 else p.lineTo)(X, max(Y, -170))
        X2, Y2 = -120 + y * 55, 120 - x * 55
        (q.moveTo if k == 0 else q.lineTo)(min(X2, 170), Y2)
    c.drawPath(p, paint(BLUE, a, stroke=9))
    c.drawPath(q, paint(PURPLE, a, stroke=9))


def regua_ph_ic(c, a):
    """ep2: a régua de pH, de cabeça para baixo (menor pH, mais ácido)"""
    cores = ["#E5484D", "#F2994A", "#F2C94C", "#6FCF97", "#56CCF2", "#5B6CF0", "#8E5BD9"]
    for k, col in enumerate(cores):
        rrect(c, -210 + k * 60, -50, 58, 100, 8, col, a)
    ftext(c, "0", -205, 100, 34, "black", INK2, a, align="left")
    ftext(c, "7", 0, 100, 34, "black", INK2, a, align="center")
    ftext(c, "14", 205, 100, 34, "black", INK2, a, align="right")
    arrow(c, 150, -100, -150, -100, RED, a, 8, 22)
    ftext(c, "ÁCIDO", -60, -130, 30, "black", RED, a, align="center")


def placares_ic(c, a):
    """ep3: os dois placares do terremoto (amplitude ×10, energia ×32 por grau)"""
    for k, (s, v, col) in enumerate((("AMPLITUDE", "×10", BLUE), ("ENERGIA", "×32", RED))):
        y = -150 + k * 160
        rrect(c, -200, y, 400, 140, 18, INK, a, shadow=True)
        ftext(c, s, -175, y + 45, 26, "black", "#FFFFFF", a * 0.8, align="left")
        ftext(c, v, 175, y + 115, 72, "black", col, a, align="right")


def medidor_ic(c, a):
    """ep4: o medidor de decibéis"""
    rrect(c, -150, -200, 300, 400, 40, INK, a, shadow=True)
    rrect(c, -110, -160, 220, 140, 16, mix(INK, GREEN, 0.25), a)
    ftext(c, "80 dB", 0, -70, 54, "black", GREEN, a, align="center")
    for k in range(5):
        col = (GREEN, GREEN, AMBER, AMBER, RED)[k]
        rrect(c, -100 + k * 42, 30, 34, 60 + k * 14, 6, col, a)
    c.drawCircle(0, 160, 18, paint(LIGHT, a))


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (espelho_ic, regua_ph_ic, placares_ic, medidor_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def grafico(c, a):
    rrect(c, -170, -150, 340, 300, 16, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-170, -150, 340, 300), 16, 16), paint(INK2, a, stroke=6))
    line(c, -130, 120, 140, 120, INK2, a, 5)
    line(c, -130, 120, -130, -120, INK2, a, 5)
    p = skia.Path()
    for k in range(40):
        x = 0.15 + 9.85 * k / 39
        X, Y = -130 + x * 27, 70 - math.log10(x) * 150
        (p.moveTo if k == 0 else p.lineTo)(X, Y)
    c.drawPath(p, paint(PURPLE, a, stroke=9))


def gota(c, a):
    p = skia.Path(); p.moveTo(0, -160); p.quadTo(120, 10, 100, 60); p.quadTo(60, 150, 0, 150)
    p.quadTo(-60, 150, -100, 60); p.quadTo(-120, 10, 0, -160); p.close()
    c.drawPath(p, paint(AGUA, a))
    c.drawPath(p, paint(mix(AGUA, INK, 0.4), a, stroke=6))
    c.drawCircle(-35, 60, 18, paint("#FFFFFF", a * 0.8))


def sismo(c, a):
    rrect(c, -170, -120, 340, 240, 16, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-170, -120, 340, 240), 16, 16), paint(INK2, a, stroke=6))
    p = skia.Path(); p.moveTo(-150, 0)
    for k, h in enumerate((10, -20, 30, -70, 95, -90, 60, -35, 15, -8)):
        p.lineTo(-130 + k * 28, h)
    p.lineTo(150, 0)
    c.drawPath(p, paint(RED, a, stroke=7))


def falante(c, a):
    rrect(c, -150, -50, 80, 100, 8, INK2, a)
    p = skia.Path(); p.moveTo(-70, -50); p.lineTo(10, -120); p.lineTo(10, 120); p.lineTo(-70, 50); p.close()
    c.drawPath(p, paint(INK2, a))
    for j in range(3):
        q = skia.Path(); r = 50 + j * 40
        q.addArc(skia.Rect.MakeXYWH(10 - r, -r, 2 * r, 2 * r), -45, 90)
        c.drawPath(q, paint(BLUE, a, stroke=9))


def tubo(c, a):
    rrect(c, -50, -150, 100, 270, 50, "#FFFFFF", a)
    rrect(c, -50, 0, 100, 120, 50, mix("#FFFFFF", GREEN, 0.55), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-50, -150, 100, 270), 50, 50), paint(INK2, a, stroke=6))
    rrect(c, -70, -170, 140, 30, 10, INK2, a)


def globo(c, a):
    c.drawCircle(0, 0, 140, paint(mix("#FFFFFF", AGUA, 0.8), a))
    c.drawCircle(0, 0, 140, paint(INK2, a, stroke=7))
    p = skia.Path(); p.moveTo(-60, -110); p.quadTo(10, -60, -30, -10); p.quadTo(-90, 20, -60, 80); p.lineTo(-120, 40)
    p.quadTo(-140, -40, -60, -110); p.close()
    c.drawPath(p, paint(GREEN, a))
    p = skia.Path(); p.moveTo(40, -50); p.lineTo(130, -30); p.quadTo(120, 60, 60, 110); p.quadTo(20, 30, 40, -50); p.close()
    c.drawPath(p, paint(GREEN, a))
    line(c, -20, -140, 30, 140, RED, a, 6)


def coracao(c, a):
    p = skia.Path(); p.moveTo(0, 130); p.cubicTo(-200, 0, -120, -150, 0, -60); p.cubicTo(120, -150, 200, 0, 0, 130)
    p.close()
    c.drawPath(p, paint(RED, a))
    ftext(c, "7,4", 0, 10, 60, "black", "#FFFFFF", a, align="center")


def lapis(c, a):
    c.save(); c.rotate(-35)
    rrect(c, -150, -32, 240, 64, 6, AMBER, a)
    rrect(c, -190, -32, 50, 64, 8, mix(RED, "#FFFFFF", 0.3), a)
    p = skia.Path(); p.moveTo(90, -32); p.lineTo(160, 0); p.lineTo(90, 32); p.close()
    c.drawPath(p, paint("#F2D3A8", a))
    p = skia.Path(); p.moveTo(138, -10); p.lineTo(160, 0); p.lineTo(138, 10); p.close()
    c.drawPath(p, paint(INK, a))
    c.restore()


AREA_F = (grafico, gota, sismo, falante, tubo, globo, coracao, lapis)


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
    for k, (s, ic, col) in enumerate((("ACIDEZ", 1, GREEN), ("TERREMOTOS", 2, RED), ("BARULHO", 3, BLUE))):
        a, d = rise(t, C["01.a"] + 0.55 * k)
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 230, 230 + d, 460, 330, 26, mix("#F7F7F5", col, 0.10), a)
        area_icone(c, ic, x, 360 + d, 0.55, a)
        text(c, s, x, 520 + d, 40, "black", col, a)
        arrow(c, x, 575 + d, 960, 650, INK2, a * ep(t, C["01.b"], 0.4) * 0.7, 4, 12)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 660, 800, 100, 50, mix("#FFFFFF", PURPLE, 0.14), ab, shadow=True)
        text_mid(c, "UMA ÚNICA REGRA", W / 2, 710, 48, "black", PURPLE, ab)
    selo(c, W / 2, 830, ep(t, C["01.c"] + 2.0, 0.4), "“QUANTAS VEZES MAIOR?”", AMBER, -3, 40)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "9 V OU F", 260, 860, AMBER, ad, 26)
        chip(c, "5 QUESTÕES NOVAS", 1640, 860, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 26)


COBRA = [("02.a", "COMPARAR NUMA ESCALA", "quantas vezes? · a campeã", AMBER, 1),
         ("02.b", "CALCULAR COM A FÓRMULA", "pH · decibéis · magnitude", BLUE, 4),
         ("02.c", "LER O GRÁFICO", "(1, 0) · cresce devagar", PURPLE, 0),
         ("02.d", "ACHAR O DOMÍNIO", "o que vai dentro do log", GREEN, 7)]


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
        para(c, nb(sub), x, 690 + d, 26, "bold", INK2, a, 340, 32, align="center")
        if k == 0:
            selo(c, x + 120, 260 + d, ep(t, C[cue] + 2.4, 0.4), "CAMPEÃ", AMBER, 8, 24)


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "UMA REGRA SÓ", BLUE)
    a0 = ep(t, C["03.t"], 0.5)
    if a0 > 0:
        boxed(c, 260, 210, 1400, 130, PURPLE, a0, 0.10)
        text_mid(c, "diferença das leituras = expoente da razão", W / 2, 275, 50, "black", PURPLE, a0)
    for k, (cue, l1, l2, dif, res, col) in enumerate((("03.a", "pH 3", "pH 6", "diferença 3", "10³ = 1 000 vezes", GREEN),
                                                      ("03.b", "+40 dB", "÷ 10 antes", "4", "10⁴ vezes", BLUE))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 410 + k * 230
        area_icone(c, 1 if k == 0 else 3, 300, y + 80 + d, 0.40, a)
        rrect(c, 420, y + d, 1240, 170, 22, "#FFFFFF", a, shadow=True)
        fit(c, f"{l1}  ×  {l2}" if k == 0 else f"{l1}  →  {l2}", 470, y + 70 + d, 44, 620, "black", INK, a)
        fit(c, dif, 470, y + 135 + d, 34, 500, "bold", INK2, a)
        arrow(c, 1050, y + 85 + d, 1140, y + 85 + d, col, a, 6, 16)
        fit(c, res, 1170, y + 105 + d, 54, 470, "black", col, a)


INDICE = [("EP. 1", "o espelho na reta y = x · o retorno decrescente · a porta do log: nada de zero nem negativo"),
          ("EP. 2", "a régua de zeros · diferença = expoente da razão · o pH de cabeça para baixo"),
          ("EP. 3", "os dois placares · a constante se cancela · desfaça de fora para dentro"),
          ("EP. 4", "cada 10 dB, um zero a mais · o 10 come um zero · os copos no balde")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
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
        icone(c, k, x, y + 210, 0.58, a)
        yy = y + 370
        for ln in s.split(" · "):
            yy += para(c, nb(ln), x, yy, 26, "black", INK if on_ else INK2, a, 330, 32, align="center") + 10


ONDE = [("06.a", "QUÍMICA", 4, "pH das soluções", "chuva com pH abaixo de 5,6 é ácida", GREEN),
        ("06.b", "FÍSICA", 3, "nível sonoro", "+10 dB = ×10 · o volume que você sente não é proporcional", BLUE),
        ("07.c", "GEOGRAFIA", 5, "terremotos", "danos dependem da profundidade e das construções", RED),
        ("07.d", "BIOLOGIA", 6, "pH do sangue", "pequena variação de pH, grande variação de H⁺", PURPLE)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA REGRA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 220 + d, 380, 600, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 30, "black", col, a, 360, 36, align="center")
        area_icone(c, ic, x, 450 + d, 0.42, a)
        fit(c, lei_, x, 630 + d, 32, 340, "black", INK, a, align="center")
        para(c, nb(res), x, 680 + d, 25, "bold", INK2, a, 340, 31, align="center")


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS NA HORA H", GREEN)
    a, d = rise(t, C["08.a"])
    if a > 0:
        rrect(c, 120, 230 + d, 1000, 600, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, 1, 190, 300 + d, a, 34, bg=GREEN)
        fit(c, "“QUANTAS VEZES” PEDE RAZÃO", 250, 315 + d, 40, 840, "black", GREEN, a)
        fit(c, "ache a diferença e ajuste pelo coeficiente:", 170, 395 + d, 32, 900, "bold", INK2, a)
        for k, (ic, esc, op, col) in enumerate(((3, "decibéis", "÷ 10", BLUE), (2, "energia do sismo", "× 1,5", RED),
                                                (1, "pH e amplitude", "já é o expoente", GREEN))):
            ak = ep(t, C["08.a2"] + 1.3 * k, 0.4) * a
            if ak <= 0:
                continue
            y = 450 + k * 105
            rrect(c, 170, y + d, 900, 90, 16, "#FFFFFF", ak, shadow=True)
            area_icone(c, ic, 230, y + 45 + d, 0.20, ak)
            fit(c, esc, 290, y + 58 + d, 32, 380, "black", INK, ak)
            fit(c, op, 1040, y + 60 + d, 40, 360, "black", col, ak, align="right")
        a3 = ep(t, C["08.a3"], 0.4) * a
        if a3 > 0:
            fit(c, "depois: eleve 10 ao resultado", 620, 800 + d, 34, 900, "black", PURPLE, a3, align="center")
    for k, (cue, n, tit, sub) in enumerate((("09.b", "2", "ISOLE O LOG", "opere na ordem certa | para voltar: de fora para dentro"),
                                            ("09.c", "3", "CONFIRA O SENTIDO", "pH: menor leitura, mais H⁺ | nas outras: maior, maior"))):
        ak, dk = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 230 + k * 310
        rrect(c, 1160, y + dk, 600, 290, 24, mix("#F7F7F5", GREEN, 0.10), ak)
        badge_num(c, n, 1230, y + 60 + dk, ak, 30, bg=GREEN)
        fit(c, tit, 1285, y + 74 + dk, 36, 450, "black", GREEN, ak)
        yy = y + 150 + dk
        for ln in sub.split(" | "):
            yy += para(c, nb(ln), 1460, yy, 28, "bold", INK, ak, 540, 34, align="center") + 8


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
    ("diferença de leitura", "pH 2 é 3 vezes mais ácido que pH 5", False, "o 3 está bem ali, na diferença",
     "a diferença é o expoente da razão", "10³ = 1 000", 1),
    ("o 10 come um zero", "+1 dB → intensidade × 10", False, "no pH, um passo já vale × 10",
     "são 10 dB para cada × 10", "+10 dB", 3),
    ("os copos no balde", "80 dB + 80 dB = 160 dB", False, "parece uma soma comum",
     "intensidades se somam; dobrar soma ≈ 3 dB", "≈ 83 dB", 3),
    ("o outro placar", "+2 graus → energia × 1 000", True, "na amplitude, 2 graus dão só × 100",
     "energia: 1,5 · 2 = 3 → 10³", "× 1 000", 2),
    ("de cabeça para baixo", "pH maior = mais ácido", False, "número maior parece “mais”",
     "o sinal de menos inverte a relação", "pH menor", 1),
    ("log do produto", "log(2 · 10⁻⁵) = 0,30 − 5", True, "muita gente multiplica: log 2 · (−5)",
     "log do produto é soma", "−4,70", 1),
    ("a porta fechada", "domínio de log(2x − 6): x ≥ 3", False, "o “igual” parece inofensivo",
     "x = 3 zera o log: desigualdade estrita", "x > 3", 0),
    ("base menor que 1", "log₀,₅ x > 2 ⇒ x > 0,25", False, "o primeiro passo parece o de sempre",
     "base < 1 inverte o sentido · e x > 0", "0 < x < 0,25", 0),
    ("retorno decrescente", "o log cresce cada vez mais devagar", True, "o gráfico nunca para de subir",
     "para subir 1, x é multiplicado pela base", "1 · 10 · 100", 0),
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
        rrect(c, W / 2 - 520, 700, 1040, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "escreva a diferença · resolva · confira o sentido", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="ONDE O LOG EXISTE?", area="DOMÍNIO", ic=0, ok="E",
               enun=[("a", "Para quais valores reais de x a função abaixo está definida?", True)],
               formula=("a", "f(x) = log(x² − 16)"),
               alts=[("A", "x > 4", "esqueceu o ramo negativo", AMBER), ("B", "x > 16", "comparou x com 16", RED),
                     ("C", "−4 < x < 4", "inverteu a região", RED), ("D", "x ≤ −4 ou x ≥ 4", "deixou entrar o zero", AMBER),
                     ("E", "x < −4 ou x > 4", "", GREEN)],
               passos=[("d", "x² − 16 > 0 → x² > 16"), ("a", "x > 4  ou  x < −4")],
               confere=("a", "x = −5: 25 − 16 = 9 > 0")),
    "q2": dict(ids=("23", "24"), titulo="QUEM TEM MAIS H⁺?", area="COMPARAR ACIDEZ", ic=1, ok="D",
               enun=[("a", "Refrigerante: pH 2,5. Iogurte: pH 4,5.", False),
                     ("b", "A [H⁺] no refrigerante, em relação à do iogurte, é:", True)],
               formula=None,
               alts=[("A", "1,8 vez maior", "dividiu os pHs", RED), ("B", "2 vezes maior", "parou na diferença", AMBER),
                     ("C", "20 vezes maior", "diferença × 10", RED), ("D", "100 vezes maior", "", GREEN),
                     ("E", "100 vezes menor", "inverteu o sentido", AMBER)],
               passos=[("d", "diferença: 4,5 − 2,5 = 2"), ("a", "10² = 100 vezes"),
                       ("b", "pH menor → mais H⁺ → MAIOR")],
               confere=None),
    "q3": dict(ids=("25", "26"), titulo="A CHUVA É ÁCIDA?", area="pH COM COEFICIENTE", ic=1, ok="A",
               enun=[("a", "Água de chuva: [H⁺] = 4 · 10⁻⁶ mol/L. Use log 2 = 0,30.", False),
                     ("b", "O pH da amostra é:", True)],
               formula=None,
               alts=[("A", "5,4", "", GREEN), ("B", "5,7", "usou log 2 no lugar de log 4", AMBER),
                     ("C", "6,0", "ignorou o 4", RED), ("D", "6,3", "somou log 2", RED),
                     ("E", "6,6", "somou log 4: sinal", RED)],
               passos=[("d", "k · 10⁻⁶ → pH entre 5 e 6"), ("a", "log 4 = 2 · 0,30 = 0,60"),
                       ("a", "pH = 6 − 0,60 = 5,4")],
               confere=("v", "5,4 < 5,6: chuva ácida")),
    "q4": dict(ids=("27", "28"), titulo="QUAL PLACAR?", area="AMPLITUDE × ENERGIA", ic=2, ok="D",
               enun=[("a", "Com M = log(A/A₀), um tremor de magnitude 4 e outro de magnitude 7.", False),
                     ("b", "A AMPLITUDE no segundo, em relação ao primeiro, é:", True)],
               formula=None,
               alts=[("A", "1,75 vez maior", "dividiu as magnitudes", RED), ("B", "3 vezes maior", "parou na diferença", AMBER),
                     ("C", "30 vezes maior", "diferença × 10", RED), ("D", "1 000 vezes maior", "", GREEN),
                     ("E", "cerca de 31 600 vezes maior", "razão das ENERGIAS", AMBER)],
               passos=[("d", "diferença: 7 − 4 = 3 graus"), ("a", "amplitude: 10³ = 1 000 vezes")],
               confere=("xe", "energia seria 10^4,5 ≈ 31 600")),
    "q5": dict(ids=("29", "30"), titulo="QUANTOS DECIBÉIS?", area="CALCULAR DECIBÉIS", ic=3, ok="C",
               enun=[("a", "Num show, perto do palco, I = 10⁻¹ W/m².", False),
                     ("b", "Com a fórmula abaixo e I₀ = 10⁻¹² W/m², o nível é:", True)],
               formula=("b", "β = 10 · log(I/I₀)"),
               alts=[("A", "−10 dB", "não dividiu por I₀", RED), ("B", "11 dB", "esqueceu o fator 10", AMBER),
                     ("C", "110 dB", "", GREEN), ("D", "120 dB", "só o expoente de I₀", RED),
                     ("E", "130 dB", "somou 1 + 12 sem sinal", RED)],
               passos=[("d", "I/I₀ = 10⁻¹ ÷ 10⁻¹² = 10¹¹"), ("a", "β = 10 · 11 = 110 dB")],
               confere=("v", "bem acima dos 85 dB do limite")),
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

CHECK = [("31.b", "EP. 1", 0, ["lei, domínio e imagem", "gráficos espelhados · (1, 0) e (b, 1)", "sinal e inequações"]),
         ("31.c", "EP. 2", 1, ["diferença de leituras em razão", "pH a partir de [H⁺] e de volta", "comparar acidez"]),
         ("32.a", "EP. 3", 2, ["amplitude × energia por grau", "magnitude pela fórmula e de volta"]),
         ("32.b", "EP. 4", 3, ["decibéis com I₀ = 10⁻¹²", "duas fontes iguais: ≈ +3 dB"])]


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
        for k, ic in enumerate((1, 2, 3)):
            area_icone(c, ic, 290 + k * 110, 670, 0.22, ac)
        text_mid(c, "10 DE COMPARAÇÃO EM ESCALA", 1100, 640, 44, "black", BLUE, ac)
        text_mid(c, "pH · Richter · decibéis", 1100, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 260, 28, "black", GRAY, aa, tracking=2)
    text(c, "Função modular", W / 2, 350, 76, "black", PURPLE, aa)
    text(c, "e funções definidas por partes", W / 2, 420, 36, "bold", INK2, aa)
    for k, s in enumerate(("conta de água", "estacionamento", "imposto por faixas")):
        a, d = rise(t, C["34.b"] + 0.9 * k)
        if a <= 0:
            continue
        x = 480 + k * 480
        rrect(c, x - 200, 500 + d, 400, 150, 24, mix("#F7F7F5", BLUE, 0.10), a)
        # degraus: a fórmula muda por faixa
        text(c, s, x, 556 + d, 30, "black", INK, a)
        p = skia.Path(); p.moveTo(x - 105, 625 + d)
        for j, h in enumerate((0, 18, 36)):
            p.lineTo(x - 105 + j * 70, 625 + d - h); p.lineTo(x - 35 + j * 70, 625 + d - h)
        c.drawPath(p, paint(BLUE, a, stroke=7))
    selo(c, W / 2, 760, ep(t, C["34.c"], 0.5), "A FÓRMULA MUDA COM A ENTRADA", GREEN, -3, 34)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
