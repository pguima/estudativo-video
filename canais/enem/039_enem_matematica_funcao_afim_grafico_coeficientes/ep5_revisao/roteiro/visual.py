"""Visual — Função Afim, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): taxímetro · vela · escada da reta · gráfico do equilíbrio.
Ícones de área (area_icone()): carro (MU) · velocímetro (MUV) · termômetro · cofrinho (juros) · escada de PA · e, nas
questões, caixa d'água · torneira · bolo · gráfico · celular.
Cores com função: azul = definição / b · roxo = regra, fórmula / a · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum039", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_afim_ep5_revisao.mp4"
CARD_R = K.CARD_R
CAIXA = "#2B2F37"
LCD = "#10141A"
CERA = "#F4E3B5"
AGUA = "#8CC8F0"
MASSA = "#E9C08A"
METAL = "#9AA3AD"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'R$ 12', '30 L/h' nem '1 560'"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(L|h|min|cm|m³|km|reais|bolos)\b)", " ", s)
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


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def taximetro(c, a):
    """ep1: visor do táxi com a bandeirada (azul) e o taxímetro (roxo)"""
    rrect(c, -170, -110, 340, 220, 24, CAIXA, a, shadow=True)
    rrect(c, -150, -90, 300, 100, 12, LCD, a)
    ftext(c, "R$ 5 + 2,5d", 130, -25, 40, "black", "#FFD166", a, align="right")
    rrect(c, -150, 30, 140, 60, 10, BLUE, a)
    text_mid(c, "b", -80, 60, 34, "black", "#FFFFFF", a)
    rrect(c, 10, 30, 140, 60, 10, PURPLE, a)
    text_mid(c, "a", 80, 60, 34, "black", "#FFFFFF", a)


def vela(c, a, alt=1.0):
    """ep2: a vela (alt = fração da altura) com a chama"""
    h = 220 * alt
    rrect(c, -40, 120 - h, 80, h, 10, CERA, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-40, 120 - h, 80, h), 10, 10), paint(INK2, a, stroke=4))
    line(c, 0, 120 - h, 0, 100 - h, INK, a, 4)
    p = skia.Path(); p.moveTo(0, 50 - h); p.quadTo(26, 82 - h, 0, 100 - h); p.quadTo(-26, 82 - h, 0, 50 - h); p.close()
    c.drawPath(p, paint(AMBER, a))
    rrect(c, -90, 120, 180, 22, 10, METAL, a)
    fmid(c, "Δy/Δx", 150, -40, 32, "black", PURPLE, a)


def escada(c, a):
    """ep3: a reta com os degraus e os dois pregos"""
    arrow(c, -180, 130, 190, 130, INK2, a, 4, 12)
    arrow(c, -160, 150, -160, -160, INK2, a, 4, 12)
    x0, y0, dx, dy = -150, 90, 70, -50
    line(c, x0 - 10, y0 + 7, x0 + 4 * dx + 20, y0 + 4 * dy - 14, PURPLE, a, 6)
    for k in range(4):
        xa, ya = x0 + k * dx, y0 + k * dy
        line(c, xa, ya, xa + dx, ya, AMBER, a, 4, dash=[8, 6])
        line(c, xa + dx, ya, xa + dx, ya + dy, AMBER, a, 4, dash=[8, 6])
    for k in (1, 3):
        c.drawCircle(x0 + k * dx, y0 + k * dy, 13, paint(RED, a))
        c.drawCircle(x0 + k * dx, y0 + k * dy, 5, paint("#FFFFFF", a))


def equilibrio(c, a):
    """ep4: custo e receita cruzando; prejuízo antes, lucro depois"""
    arrow(c, -180, 130, 190, 130, INK2, a, 4, 12)
    arrow(c, -160, 150, -160, -160, INK2, a, 4, 12)
    line(c, -160, 40, 170, -110, RED, a, 6)
    line(c, -160, 130, 170, -150, GREEN, a, 6)
    # cruzamento: 40 − 150s = 130 − 280s → s = 90/130
    xc, yc = -160 + 330 * (90 / 130), 40 + (-150) * (90 / 130)
    c.drawCircle(xc, yc, 13, paint(AMBER, a))
    ftext(c, "L = 0", xc + 18, yc + 46, 26, "black", AMBER, a, align="left")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (taximetro, vela, escada, equilibrio)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def carro(c, a):
    rrect(c, -170, -20, 340, 90, 26, BLUE, a)
    p = skia.Path(); p.moveTo(-100, -20); p.lineTo(-60, -90); p.lineTo(70, -90); p.lineTo(110, -20); p.close()
    c.drawPath(p, paint(BLUE, a))
    rrect(c, -50, -78, 50, 50, 6, "#FFFFFF", a)
    rrect(c, 12, -78, 60, 50, 6, "#FFFFFF", a)
    for x in (-95, 95):
        c.drawCircle(x, 75, 36, paint(INK, a))
        c.drawCircle(x, 75, 14, paint(METAL, a))
    arrow(c, 190, 10, 260, 10, GREEN, a, 7, 18)


def velocimetro(c, a):
    p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(-150, -150, 300, 300), 180, 180)
    c.drawPath(p, paint(INK2, a, stroke=16))
    p2 = skia.Path(); p2.addArc(skia.Rect.MakeXYWH(-150, -150, 300, 300), 180, 120)
    c.drawPath(p2, paint(PURPLE, a, stroke=16))
    line(c, 0, 0, 80, -100, RED, a, 9)
    c.drawCircle(0, 0, 18, paint(INK, a))
    rrect(c, -150, 40, 300, 22, 8, METAL, a)


def termometro(c, a):
    rrect(c, -26, -150, 52, 230, 26, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-26, -150, 52, 230), 26, 26), paint(INK2, a, stroke=4))
    rrect(c, -10, -60, 20, 150, 10, RED, a)
    c.drawCircle(0, 110, 46, paint(RED, a))
    for j in range(5):
        line(c, 32, -120 + j * 40, 56, -120 + j * 40, INK2, a, 4)


def cofrinho(c, a):
    c.drawOval(skia.Rect.MakeXYWH(-160, -100, 300, 200), paint(mix("#FFFFFF", RED, 0.45), a))
    c.drawCircle(150, -10, 36, paint(mix("#FFFFFF", RED, 0.45), a))
    rrect(c, -40, -112, 90, 16, 8, INK, a)
    for x in (-100, 70):
        rrect(c, x, 80, 34, 60, 10, mix("#FFFFFF", RED, 0.45), a)
    c.drawCircle(80, -40, 9, paint(INK, a))
    c.drawCircle(10, -160, 30, paint(AMBER, a))
    ftext(c, "$", 10, -148, 34, "black", "#FFFFFF", a, align="center")


def escada_pa(c, a):
    for k in range(4):
        rrect(c, -170 + k * 85, 130 - (k + 1) * 60, 80, (k + 1) * 60, 6, mix("#FFFFFF", GREEN, 0.35 + 0.15 * k), a)
        ftext(c, str(3 + 4 * k), -130 + k * 85, 115, 30, "black", INK, a, align="center")
    fmid(c, "+r", 40, -150, 40, "black", GREEN, a)


def caixa_dagua(c, a, nivel=0.6):
    rrect(c, -140, -130, 280, 240, 18, "#FFFFFF", a, shadow=True)
    h = 220 * nivel
    rrect(c, -130, 100 - h, 260, h, 12, AGUA, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-140, -130, 280, 240), 18, 18), paint(INK2, a, stroke=5))
    line(c, 140, 70, 200, 70, INK2, a, 12)
    for k in range(3):
        c.drawCircle(205, 100 + k * 30, 7, paint(AGUA, a))


def torneira(c, a):
    rrect(c, -170, -70, 220, 50, 14, METAL, a)
    rrect(c, 20, -70, 50, 120, 12, METAL, a)
    rrect(c, -110, -120, 60, 50, 8, INK2, a)
    for k in range(3):
        c.drawCircle(45, 85 + k * 40, 12, paint(AGUA, a))
    rrect(c, -10, 160, 110, 14, 6, BLUE, a)


def bolo(c, a):
    rrect(c, -150, -10, 300, 120, 14, MASSA, a)
    rrect(c, -150, -40, 300, 50, 20, "#F7D9E3", a)
    for x in (-90, 0, 90):
        rrect(c, x - 6, -110, 12, 70, 4, BLUE, a)
        c.drawCircle(x, -122, 10, paint(AMBER, a))
    rrect(c, -180, 110, 360, 20, 8, METAL, a)


def mini_grafico(c, a):
    arrow(c, -170, 130, 180, 130, INK2, a, 4, 12)
    arrow(c, -150, 150, -150, -160, INK2, a, 4, 12)
    line(c, -150, 70, 160, -130, PURPLE, a, 6)
    for (x, y) in ((-60, 12), (90, -85)):
        c.drawCircle(x, y, 14, paint(RED, a))


def celular(c, a):
    rrect(c, -90, -160, 180, 320, 26, INK, a, shadow=True)
    rrect(c, -74, -130, 148, 250, 10, mix("#FFFFFF", BLUE, 0.3), a)
    c.drawCircle(0, 140, 10, paint(METAL, a))
    ftext(c, "min", 0, 0, 40, "black", BLUE, a, align="center")


AREA_F = (carro, velocimetro, termometro, cofrinho, escada_pa, caixa_dagua, torneira, bolo, mini_grafico, celular)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# figuras das questões
# ======================================================================

def tabela_caixa(c, x, y, a, b_on=0.0):
    """t (h) | volume (L); b_on acende a linha extrapolada t = 0 → 1 800 L"""
    if a <= 0:
        return
    rows = [("2", "1 560"), ("6", "1 080"), ("10", "600")]
    rh, w1, w2 = 52, 170, 220
    if b_on > 0:
        rows = [("0", "1 800")] + rows
    rrect(c, x, y, w1 + w2, rh, 10, BLUE, a)
    ftext(c, "t (h)", x + w1 / 2, y + 36, 26, "black", "#FFFFFF", a, align="center")
    ftext(c, "volume (L)", x + w1 + w2 / 2, y + 36, 26, "black", "#FFFFFF", a, align="center")
    for j, (t_, v) in enumerate(rows):
        yy = y + rh * (j + 1)
        novo = b_on > 0 and j == 0
        bg = mix("#FFFFFF", GREEN, 0.25 * b_on) if novo else ("#FFFFFF" if j % 2 == 0 else "#F3F3F0")
        rrect(c, x, yy, w1 + w2, rh, 0, bg, a * (b_on if novo else 1))
        col = GREEN if novo else INK
        ftext(c, t_, x + w1 / 2, yy + 37, 30, "black", col, a * (b_on if novo else 1), align="center")
        ftext(c, nb(v), x + w1 + w2 / 2, yy + 37, 30, "black", col, a * (b_on if novo else 1), align="center")


def grafico_q4(c, x0, y0, w, h, a, reta=1.0, degrau=0.0):
    """eixos de 0 a 5 (x) e 0 a 12 (y), os pontos (1, 5) e (4, 11) marcados; reta e degrau até o b = 3 na resolução"""
    if a <= 0:
        return
    X = lambda v: x0 + w * v / 5
    Y = lambda v: y0 + h - h * v / 12
    rrect(c, x0 - 60, y0 - 40, w + 110, h + 100, 16, "#FFFFFF", a)
    for v in (2, 4, 6, 8, 10, 12):
        line(c, x0, Y(v), x0 + w, Y(v), mix("#FFFFFF", INK2, 0.15), a, 1.5)
        ftext(c, str(v), x0 - 12, Y(v) + 9, 22, "bold", INK2, a, align="right")
    for v in range(1, 6):
        ftext(c, str(v), X(v), y0 + h + 32, 22, "bold", INK2, a, align="center")
    arrow(c, x0, y0 + h, x0 + w + 30, y0 + h, INK2, a, 4, 12)
    arrow(c, x0, y0 + h, x0, y0 - 25, INK2, a, 4, 12)
    if reta > 0:
        line(c, X(0), Y(3), X(0) + (X(4.5) - X(0)) * reta, Y(3) + (Y(12) - Y(3)) * reta, PURPLE, a * reta, 6)
    if degrau > 0:
        line(c, X(1), Y(5), X(0), Y(5), AMBER, a * degrau, 4, dash=[10, 7])
        line(c, X(0), Y(5), X(0), Y(3), AMBER, a * degrau, 4, dash=[10, 7])
        c.drawCircle(X(0), Y(3), 12, paint(BLUE, a * degrau))
        ftext(c, "b = 3", X(0) + 18, Y(3) + 34, 26, "black", BLUE, a * degrau, align="left")
    for (px, py) in ((1, 5), (4, 11)):
        c.drawCircle(X(px), Y(py), 12, paint(RED, a))
        ftext(c, f"({px}, {py})", X(px) + 18, Y(py) - 8, 26, "black", RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 300, 200, 600, 130, 22, mix("#FFFFFF", PURPLE, 0.14), aa, shadow=True)
        mx(c, "f(x) = ax + b", W / 2, 265, 64, INK, aa)
        selo(c, W / 2 + 380, 230, aa, "A MAIS COBRADA", AMBER, -6, 28)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        pill(c, "quase toda questão = 1 linha", W / 2, 400, GREEN, size=34, a=ab, anchor="center")
    for k, (s, sub, col) in enumerate((("b", "quanto vale no início?", BLUE), ("a", "quanto muda por unidade?", PURPLE))):
        a, d = rise(t, C["01.c"] + 0.8 * k)
        if a <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 320, 470 + d, 640, 230, 24, mix("#FFFFFF", col, 0.10), a, shadow=True)
        fmid(c, s, x, 545 + d, 80, "black", col, a)
        text_mid(c, sub, x, 650 + d, 36, "black", INK, a)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 860, AMBER, ad, 32)
    chip(c, "5 QUESTÕES NOVAS", 1180, 860, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 32)


def mx(c, s, x, cy, size, col=INK, a=1.0, align="center"):
    """texto matemático de uma cor (sem quebrar)"""
    fmid(c, nb(s), x, cy, size, "black", col, a)


COBRA = [("02.a", "TARIFAS E PLANOS", "fixo + por unidade", BLUE, 6),
         ("02.b", "VARIAÇÃO NO TEMPO", "vela · tanque · carro", AMBER, 5),
         ("02.c", "CUSTO E LUCRO", "quantas vender?", GREEN, 7),
         ("02.d", "LER O GRÁFICO", "dois pontos → lei", PURPLE, 8),
         ("02.e", "PROPORCIONAL?", "dobrar x dobra y?", RED, 9)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "CINCO FORMAS", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 250 + d, 330, 480, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 28, "black", col, a, 290, 36, align="center")
        area_icone(c, ic, x, 540 + d, 0.36, a)
        para(c, sub, x, 660 + d, 24, "bold", INK2, a, 290, 30, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "DÊ NOME AOS COEFICIENTES", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 380, 220, 760, 150, 24, "#FFFFFF", aa, shadow=True)
        fmid(c, "f(x) = ax + b", W / 2, 295, 76, "black", INK, aa)
    for k, (cue, s, tit, sub, col) in enumerate((("03.b", "a", "TAXA", "quanto muda por unidade", PURPLE),
                                                 ("03.c", "b", "VALOR INICIAL", "quanto vale quando x = 0", BLUE))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 620 + k * 680
        rrect(c, x - 300, 430 + d, 600, 260, 24, mix("#FFFFFF", col, 0.10), a)
        fmid(c, s, x, 500 + d, 74, "black", col, a)
        text_mid(c, tit, x, 590 + d, 36, "black", col, a)
        text_mid(c, sub, x, 645 + d, 30, "bold", INK, a)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 790, ad, "2 FRASES = 1 LINHA DE CONTA", GREEN, -3, 32)


INDICE = [("EP. 1", "o táxi: bandeirada = b · taxímetro = a · já viu disfarçado · a bandeirada não dobra"),
          ("EP. 2", "Δy sobre Δx · a foto no instante zero · o zero: a hora em que acaba"),
          ("EP. 3", "a escada da reta · dois pregos seguram a régua"),
          ("EP. 4", "lucro zero não é lucro · quem larga na frente × quem ganha no fim")]
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
        rrect(c, x - 205, y, 410, 600, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 205, y, 410, 600), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 180, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 210, 0.62, a)
        yy = y + 360
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 26, "black", INK if on_ else INK2, a, 360, 32, align="center") + 12


ONDE = [("06.a", "MOVIMENTO UNIFORME", 0, "s = s₀ + vt", "a = velocidade", BLUE),
        ("06.b", "MUV", 1, "v = v₀ + at", "a aceleração é a taxa", PURPLE),
        ("06.c", "TERMOMETRIA", 2, "F = 1,8C + 32", "1 °C vale 1,8 °F", RED),
        ("07.d", "JUROS SIMPLES", 3, "M = C + Ci·t", "capital = b · juros = a", GREEN),
        ("07.e", "PA", 4, "aₙ = a₁ + (n − 1)r", "a razão é a taxa", AMBER)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA LEI, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 220 + d, 330, 520, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 26, "black", col, a, 300, 32, align="center")
        area_icone(c, ic, x, 440 + d, 0.42, a)
        fit(c, lei_, x, 600 + d, 34, 300, "black", INK, a, align="center")
        para(c, res, x, 650 + d, 24, "bold", INK2, a, 300, 30, align="center")
    af = ep(t, C["07.f"], 0.5)
    if af > 0:
        boxed(c, 360, 780, 1200, 80, GREEN, af, 0.10)
        text_mid(c, "início? → b   ·   por unidade? → a", W / 2, 820, 34, "black", GREEN, af)


HABITOS = [("08.a", "1", "ACHE b E a PELOS NOMES", "“fixo”, “inicial” → b · “por km”, “a cada hora” → a"),
           ("08.b", "2", "DESCONFIE DA REGRA DE TRÊS", "tem parte fixa? · a proporção está errada"),
           ("09.c", "3", "O PONTO DE PARTIDA DO TEMPO", "a tabela começa depois do zero? · volte o filme"),
           ("09.d", "4", "CONFIRA COM UM PONTO", "não bateu? · erro na taxa ou no sinal")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "QUATRO HÁBITOS NA HORA H", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 240 + d, 410, 520, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 310 + d, a, 34, bg=GREEN)
        para(c, tit, x, 400 + d, 30, "black", GREEN, a, 360, 38, align="center")
        yy = 560 + d
        for ln in sub.split(" · "):
            yy += para(c, ln, x, yy, 26, "bold", INK, a, 360, 34, align="center") + 10


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
    ("parte fixa", "R$ 50 + R$ 80/mês: 3 meses = R$ 290 → 6 meses = R$ 580", False, "dobrou o tempo, a regra de três dobra a conta",
     "a matrícula não dobra: 50 + 480", "R$ 530", 0),
    ("a taxa", "reta por (1, 5) e (3, 11) → taxa = (11 − 5)/(3 − 1) = 3", True, "tem gente que divide ao contrário: 2/6",
     "taxa = Δy/Δx · a saída fica em cima", "a = 3", 1),
    ("o valor inicial", "340 L às 2 h e 300 L às 4 h → valor inicial = 340 L", False, "é o primeiro número da tabela",
     "o b é a foto no instante zero · perde 20 L/h: volte 2 h", "b = 380 L", 1),
    ("o zero", "f(x) = 2x − 8 corta o eixo x em −8", False, "o −8 é o número sozinho",
     "−8 é onde corta o eixo y · o zero é −b/a = 8 ÷ 2", "x = 4", 1),
    ("taxa negativa", "R$ 2.000, perde R$ 300 por ano → V(t) = 2 000 − 300t", True, "a gente se acostumou com o “+” de ax + b",
     "o que diminui tem taxa negativa: escreva o “−”", "a = −300", 3),
    ("o equilíbrio", "C = 900 + 6x, R = 10x → o lucro começa em 225 peças", False, "225 é a resposta da conta",
     "225 é o equilíbrio: lucro zero não é lucro", "226 peças", 3),
    ("o tempo decorrido", "vela: 12 cm aos 20 min, −0,3 cm/min → acaba 40 min depois de acesa", False,
     "12 ÷ 0,3 dá 40", "são 40 min depois daquele instante · desde acesa: 20 + 40", "60 min", 1),
    ("ler o gráfico", "corta o eixo y em 4 e sobe 3 por degrau → y = 3x + 4", True, "o 4 aparece primeiro",
     "onde nasce = b · quanto sobe por degrau = a", "y = 3x + 4", 2),
    ("escalas", "a reta que PARECE mais inclinada tem a maior taxa", False, "o olho compara desenhos",
     "eixos em escalas diferentes: só a conta decide", "Δy/Δx", 2),
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
        text_mid(c, "na margem: o início e a taxa", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · passos: (cue, texto) · confere: (cue, texto) · fig: figura do enunciado

Q = {
    "q1": dict(ids=("21", "22"), titulo="A CAIXA D'ÁGUA", area="TABELA DEPOIS DO ZERO", ic=5, ok="D", fig="tabela",
               enun=[("a", "Uma caixa d'água esvazia a uma taxa constante:", False),
                     ("b", "Desde o início, fica vazia depois de:", True)],
               alts=[("A", "5 h", "contou da última medição", RED), ("B", "11 h", "voltou com o sinal trocado", RED),
                     ("C", "13 h", "1º dado como b", AMBER), ("D", "15 h", "", GREEN),
                     ("E", "17 h", "voltou 4 h, não 2", RED)],
               passos=[("d", "a = −480 ÷ 4 = −120 L/h"), ("a", "volte 2 h: b = 1 560 + 240 = 1 800 L"),
                       ("b", "zero: 1 800 ÷ 120 = 15 h")],
               confere=("v", "t = 6: 1 800 − 720 = 1 080 L")),
    "q2": dict(ids=("23", "24"), titulo="A CONTA DE ÁGUA", area="A REGRA DE TRÊS", ic=6, ok="C", fig=None,
               enun=[("a", "Taxa fixa de R$ 30,00 mais um valor por m³. Com 12 m³, a conta veio R$ 84,00.", False),
                     ("b", "Se o consumo dobrar (24 m³), a conta será de:", True)],
               alts=[("A", "R$ 108,00", "esqueceu a taxa fixa", RED), ("B", "R$ 114,00", "conta antiga + outra taxa", RED),
                     ("C", "R$ 138,00", "", GREEN), ("D", "R$ 168,00", "regra de três: 2 · 84", AMBER),
                     ("E", "R$ 198,00", "regra de três + 30", RED)],
               passos=[("d", "tem parte fixa: nada de regra de três"), ("a", "84 − 30 = 54 em 12 m³"),
                       ("a", "a = R$ 4,50 por m³"), ("b", "30 + 4,50 · 24 = R$ 138,00")],
               confere=None),
    "q3": dict(ids=("25", "26"), titulo="A CONFEITARIA", area="O LUCRO MÍNIMO", ic=7, ok="E", fig=None,
               enun=[("a", "Custo fixo de R$ 4.500,00 por mês. Cada bolo custa R$ 18,00 e é vendido por R$ 30,00.", False),
                     ("b", "O número mínimo de bolos por mês para ter LUCRO é:", True)],
               alts=[("A", "94", "somou 30 + 18", RED), ("B", "150", "dividiu pelo preço", RED),
                     ("C", "250", "dividiu pelo custo", RED), ("D", "375", "o equilíbrio: lucro zero", AMBER),
                     ("E", "376", "", GREEN)],
               passos=[("d", "30 − 18 = R$ 12 por bolo"), ("a", "L = 12x − 4 500"), ("a", "L = 0 em x = 375"),
                       ("b", "lucro zero não é lucro: 376 bolos")],
               confere=None),
    "q4": dict(ids=("27", "28"), titulo="A LEI PELO GRÁFICO", area="DOIS PONTOS", ic=8, ok="A", fig="grafico",
               enun=[("a", "O gráfico de uma função afim passa por (1, 5) e (4, 11).", False),
                     ("b", "A lei da função é:", True)],
               alts=[("A", "y = 2x + 3", "", GREEN), ("B", "y = 3x + 2", "trocou a e b", RED),
                     ("C", "y = 2x + 5", "1º dado como b", AMBER), ("D", "y = 0,5x + 4,5", "fração invertida", RED),
                     ("E", "y = −2x + 7", "sinal errado", RED)],
               passos=[], confere=None),
    "q5": dict(ids=("29", "30"), titulo="OS DOIS PLANOS", area="UM PLANO POR DOIS PONTOS", ic=9, ok="D", fig=None,
               enun=[("a", "Plano A: R$ 20,00 + R$ 0,50 por minuto. Plano B: 40 min custam R$ 50,00 e 100 min, R$ 74,00.", False),
                     ("b", "B fica mais barato a partir de quantos minutos inteiros?", True)],
               alts=[("A", "28", "14 ÷ 0,5: uma taxa só", RED), ("B", "35", "14 ÷ 0,4: uma taxa só", RED),
                     ("C", "140", "o empate", AMBER), ("D", "141", "", GREEN),
                     ("E", "300", "1º dado como fixo", RED)],
               passos=[("d", "B: a = 24 ÷ 60 = R$ 0,40/min · b = R$ 34"), ("a", "20 + 0,5x = 34 + 0,4x"),
                       ("a", "x = 140: empate, R$ 90"), ("b", "mais barato: 141 min")],
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
        if d["fig"] == "grafico":
            # o gráfico fica na tela também na resolução: a reta e o degrau até o b entram nela
            ya = 0
            for cue, s, dest in d["enun"]:
                a = ep(t, C[f"{s1}.{cue}"], 0.4)
                ya += para_nb(c, s, 180, 268 + ya, 26, "black" if dest else "bold", BLUE if dest else INK, a, 600, 34) + 4
            grafico_q4(c, 260, 390, 440, 290, a0, reta=ep(t, C[f"{s2}.b"], 0.8), degrau=ep(t, C[f"{s2}.a"], 0.6))
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 780, 760, a=1 - sol)
            ad = ep(t, C[f"{s2}.d"], 0.4)
            if ad > 0:
                pill(c, "a = 6/3 = 2", 430, 440, PURPLE, size=26, a=ad, anchor="center")
            conferido(c, "2 · 4 + 3 = 11", 450, 800, ep(t, C[f"{s2}.v"], 0.4), True, 26)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
            return
        area_icone(c, d["ic"], 770, 222, 0.30, a0 * (1 - sol))
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            if d["fig"] == "tabela" and dest:
                y = 640
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        if d["fig"] == "tabela":
            tabela_caixa(c, 240, 360, ep(t, C[f"{s1}.a"] + 0.5, 0.5) * (1 - sol))
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720, 470)
        else:
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        if sol > 0:
            yy = 300
            if d["fig"] == "tabela":
                tabela_caixa(c, 180, 230, sol, b_on=ep(t, C[f"{s2}.a"], 0.5))
                yy = 520
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.6 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 34 if d["fig"] != "tabela" else 30, 640, "black", GREEN if last else INK, a)
                yy += 62 if d["fig"] != "tabela" else 54
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["parte fixa + parte proporcional", "linear (b = 0) × afim"]),
         ("31.c", "EP. 2", 1, ["a = Δy/Δx, com unidade", "b = f(0) · extrapolar", "zero = −b/a"]),
         ("32.a", "EP. 3", 2, ["crescente, decrescente, constante", "lei por 2 pontos + conferir"]),
         ("32.b", "EP. 4", 3, ["estudo do sinal", "custo, receita, lucro", "comparar dois planos"]),
         ("32.c", "REVISÃO", None, ["MU, termometria, juros, PA"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 200), (150, 400), (150, 620), (990, 200), (990, 420)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        if ic is not None:
            icone(c, ic, x + 40, y0 + 90, 0.2, a)
        else:
            area_icone(c, 2, x + 40, y0 + 90, 0.2, a)
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 44
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            fit(c, it, x + 158, yy + 10, 26, 600, "bold", INK, a)
    ae = ep(t, C["32.d"], 0.5)
    if ae > 0:
        boxed(c, 990, 640, 760, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1370, 690, 32, "black", INK, ae)


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
        area_icone(c, 8, 330, 670, 0.32, ac)
        text_mid(c, "10 COM A LEI MONTADA", 1060, 640, 44, "black", BLUE, ac)
        text_mid(c, "a partir de um gráfico ou de uma tabela", 1060, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Função quadrática", W / 2, 330, 62, "black", PURPLE, aa)
    text(c, "vértice · raízes · máximo e mínimo", W / 2, 400, 36, "bold", INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    ac = ep(t, C["34.c"], 0.5)
    x0, y0, w, h = 560, 470, 800, 300
    if ab > 0:
        arrow(c, x0, y0 + h, x0 + w, y0 + h, INK2, ab, 4, 12)
        arrow(c, x0, y0 + h, x0, y0, INK2, ab, 4, 12)
        line(c, x0 + 40, y0 + h - 30, x0 + w - 60, y0 + 40, PURPLE, ab * (1 - ac), 6)
        text(c, "taxa constante", x0 + w - 40, y0 + 30, 26, "black", PURPLE, ab * (1 - ac), align="right")
    if ac > 0:
        p = skia.Path(); p.moveTo(x0 + 60, y0 + 30); p.quadTo(x0 + w / 2, y0 + 2 * h - 60, x0 + w - 60, y0 + 30)
        c.drawPath(p, paint(GREEN, ac, stroke=7))
        selo(c, x0 + w / 2, y0 + 60, ac, "A RETA VIRA CURVA", GREEN, -4, 32)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
