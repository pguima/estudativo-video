"""Visual — Conceito de Função, Domínio e Imagem, Episódio 6: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, selo_teste...).
Índice visual da revisão: os 5 ícones dos episódios (icone()): máquina · cardápio · máquina ao contrário · régua em pé ·
porteiro.
Ícones de área (area_icone()): termômetro · tubo de ensaio · folha · mapa (outras provas) · e, nas questões, tabela da
lanchonete · termômetro (gráfico) · patinete · bicicleta · cercado com muro.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum038", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_ep6_revisao.mp4"
CARD_R = K.CARD_R
PELE = "#E8B98F"
TIJOLO = "#C9875E"
HORTA = "#CFE8B5"
METAL = "#9AA3AD"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def mx(c, s, x, cy, size, col=INK, a=1.0, align="left"):
    """linha matemática de uma cor só (expr)"""
    return K.mdraw(c, s, x, cy, size, col, a, align=align)


def nb(s):
    """espaço rígido: não quebra 'R$ 12', '30 °C' nem '60 m'"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(°C|min|m|h|graus|reais)\b)", " ", s)
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
# peças: os 5 ícones dos episódios
# ======================================================================

def boneco(c, cx, by, s, col, a=1.0):
    """bonequinho simples de pé, com os pés em by"""
    c.save(); c.translate(cx, by); c.scale(s, s)
    c.drawCircle(0, -150, 24, paint(PELE, a))
    rrect(c, -26, -122, 52, 72, 18, col, a)
    line(c, -12, -52, -16, 0, INK, a, 9)
    line(c, 12, -52, 16, 0, INK, a, 9)
    c.restore()


def maquina(c, a, volta=False):
    """ep1 (e ep3 ao contrário): funil, caixa com engrenagens, bandeja"""
    col = AMBER if volta else PURPLE
    p = skia.Path(); p.moveTo(-90, -150); p.lineTo(90, -150); p.lineTo(28, -90); p.lineTo(-28, -90); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.18), a))
    c.drawPath(p, paint(col, a, stroke=5))
    rrect(c, -150, -90, 300, 180, 24, col, a)
    for k in range(3):
        gx = -80 + k * 80
        c.drawCircle(gx, -20, 26, paint("#FFFFFF", a))
        line(c, gx - 16, -20, gx + 16, -20, col, a, 5)
    ftext(c, "f", 0, 65, 46, "black", "#FFFFFF", a, align="center")
    rrect(c, -90, 118, 180, 20, 10, METAL, a)
    line(c, 0, 90, 0, 118, METAL, a, 8)
    if volta:
        arrow(c, 175, 120, 175, -140, AMBER, a, 8, 22)
        fmid(c, "y", 175, 160, 34, "black", AMBER, a)
        fmid(c, "x?", 175, -175, 34, "black", BLUE, a)
    else:
        fmid(c, "x", -175, -150, 34, "black", BLUE, a)
        arrow(c, -175, -120, -175, 110, INK2, a, 6, 18)
        fmid(c, "y", -175, 150, 34, "black", GREEN, a)


def cardapio(c, a):
    """ep2: o cardápio (contradomínio) e o prato que sai da cozinha (imagem)"""
    rrect(c, -190, -150, 210, 300, 16, "#FFFFFF", a, shadow=True)
    rrect(c, -190, -150, 210, 56, 16, BLUE, a)
    ftext(c, "CARDÁPIO", -85, -112, 26, "black", "#FFFFFF", a, align="center")
    for j in range(5):
        y = -60 + j * 44
        line(c, -165, y, -40, y, INK2, a, 5)
        c.drawCircle(-20, y, 7, paint(GREEN if j in (0, 2) else LIGHT, a))
    c.drawOval(skia.Rect.MakeXYWH(40, 10, 160, 60), paint("#FFFFFF", a))
    c.drawOval(skia.Rect.MakeXYWH(40, 10, 160, 60), paint(INK2, a, stroke=4))
    c.drawCircle(120, 30, 30, paint(GREEN, a))
    ftext(c, "SAIU", 120, 120, 26, "black", GREEN, a, align="center")


def regua(c, a):
    """ep4: uma curva e a régua em pé cortando-a uma vez"""
    arrow(c, -190, 130, 200, 130, INK2, a, 4, 12)
    arrow(c, -170, 150, -170, -160, INK2, a, 4, 12)
    p = skia.Path(); p.moveTo(-150, 90); p.cubicTo(-80, -150, 40, 120, 170, -110)
    c.drawPath(p, paint(BLUE, a, stroke=7))
    rrect(c, 20, -160, 40, 290, 8, mix("#FFFFFF", AMBER, 0.5), a)
    for j in range(8):
        line(c, 20, -140 + j * 36, 36, -140 + j * 36, INK2, a, 3)
    c.drawCircle(40, 8, 12, paint(RED, a))


def porteiro(c, a):
    """ep5: a porta e o porteiro do domínio"""
    rrect(c, -40, -160, 200, 300, 10, mix("#FFFFFF", BLUE, 0.25), a)
    c.drawRect(skia.Rect.MakeXYWH(-40, -160, 200, 300), paint(BLUE, a, stroke=6))
    c.drawCircle(130, 0, 9, paint(INK2, a))
    boneco(c, -120, 140, 0.95, GREEN, a)
    rrect(c, -170, -95, 100, 56, 10, "#FFFFFF", a, shadow=True)
    ftext(c, "x ✓?", -120, -57, 30, "black", PURPLE, a, align="center")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 5 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:
        maquina(c, a)
    elif k == 1:
        cardapio(c, a)
    elif k == 2:
        maquina(c, a, volta=True)
    elif k == 3:
        regua(c, a)
    else:
        porteiro(c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def termometro(c, a):
    rrect(c, -26, -150, 52, 230, 26, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-26, -150, 52, 230), 26, 26), paint(INK2, a, stroke=4))
    rrect(c, -10, -60, 20, 150, 10, RED, a)
    c.drawCircle(0, 110, 46, paint(RED, a))
    for j in range(5):
        line(c, 32, -120 + j * 40, 56, -120 + j * 40, INK2, a, 4)


def tubo(c, a):
    p = skia.Path(); p.moveTo(-40, -150); p.lineTo(-40, 90); p.arcTo(skia.Rect.MakeXYWH(-40, 50, 80, 80), 180, -180, False)
    p.lineTo(40, -150)
    c.drawPath(p, paint(INK2, a, stroke=6))
    q = skia.Path(); q.moveTo(-37, 10); q.lineTo(-37, 90); q.arcTo(skia.Rect.MakeXYWH(-37, 53, 74, 74), 180, -180, False)
    q.lineTo(37, 10); q.close()
    c.drawPath(q, paint(mix("#FFFFFF", PURPLE, 0.55), a))
    line(c, -60, -150, 60, -150, INK2, a, 8)


def folha(c, a):
    p = skia.Path(); p.moveTo(0, -150); p.quadTo(150, -40, 0, 140); p.quadTo(-150, -40, 0, -150); p.close()
    c.drawPath(p, paint(GREEN, a))
    line(c, 0, -120, 0, 170, "#FFFFFF", a, 6)
    for j in range(3):
        y = -60 + j * 55
        line(c, 0, y + 30, 50, y, "#FFFFFF", a, 4)
        line(c, 0, y + 30, -50, y, "#FFFFFF", a, 4)


def mapa(c, a):
    xs = (-150, -50, 50, 150)
    for j in range(3):
        p = skia.Path(); p.moveTo(xs[j], -120 + (j % 2) * 20); p.lineTo(xs[j + 1], -120 + ((j + 1) % 2) * 20)
        p.lineTo(xs[j + 1], 130 + ((j + 1) % 2) * 20); p.lineTo(xs[j], 130 + (j % 2) * 20); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", (AMBER, GREEN, AMBER)[j], 0.35), a))
        c.drawPath(p, paint(INK2, a, stroke=3))
    line(c, -120, 60, -20, -20, BLUE, a, 6, dash=[14, 10])
    line(c, -20, -20, 110, 30, BLUE, a, 6, dash=[14, 10])
    c.drawCircle(110, 30, 14, paint(RED, a))


def calendario(c, a):
    rrect(c, -160, -130, 320, 260, 16, "#FFFFFF", a, shadow=True)
    rrect(c, -160, -130, 320, 60, 16, BLUE, a)
    for j, d in enumerate(("S", "T", "Q", "Q", "S")):
        ftext(c, d, -128 + j * 64, -88, 26, "black", "#FFFFFF", a, align="center")
        h = (40, 52, 52, 61, 40)[j]
        rrect(c, -150 + j * 64, 110 - h * 2.6, 44, h * 2.6, 6, mix("#FFFFFF", AMBER, 0.6), a)


def patinete(c, a):
    c.drawCircle(-120, 100, 36, paint(INK, a, stroke=10))
    c.drawCircle(130, 100, 36, paint(INK, a, stroke=10))
    line(c, -120, 100, 130, 100, INK2, a, 14)
    line(c, 110, 100, 70, -140, INK2, a, 12)
    line(c, 30, -140, 110, -140, INK2, a, 12)
    rrect(c, -90, 80, 170, 26, 10, GREEN, a)


def bicicleta(c, a):
    for x in (-110, 110):
        c.drawCircle(x, 70, 70, paint(INK, a, stroke=9))
    p = skia.Path(); p.moveTo(-110, 70); p.lineTo(-20, 70); p.lineTo(60, -40); p.lineTo(-50, -40); p.close()
    c.drawPath(p, paint(BLUE, a, stroke=9))
    line(c, -20, 70, -60, -70, BLUE, a, 9)
    line(c, 60, -40, 110, 70, BLUE, a, 9)
    line(c, 60, -40, 50, -100, INK2, a, 9)
    line(c, 20, -100, 80, -100, INK2, a, 9)
    rrect(c, -90, -86, 70, 20, 8, INK, a)


def cercado(c, a):
    rrect(c, -190, -150, 380, 40, 6, TIJOLO, a)
    for j in range(6):
        line(c, -190 + j * 64, -150, -190 + j * 64, -110, "#FFFFFF", a, 2)
    rrect(c, -150, -110, 300, 220, 4, HORTA, a)
    for x in (-150, 150):
        line(c, x, -110, x, 110, INK2, a, 5, dash=[10, 8])
    line(c, -150, 110, 150, 110, INK2, a, 5, dash=[10, 8])
    fmid(c, "x", -185, 0, 36, "black", BLUE, a)
    fmid(c, "x", 185, 0, 36, "black", BLUE, a)


AREA_F = (termometro, tubo, folha, mapa, calendario, termometro, patinete, bicicleta, cercado)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# o gráfico da temperatura (questão 2)
# ======================================================================
PTS = [(0, 16), (6, 12), (14, 30), (24, 18)]


def grafico_temp(c, x0, y0, w, h, a, prog_=1.0, sombra=0.0, marcas=0.0):
    """temperatura (°C, eixo de 0 a 40) × hora (0 a 24). sombra: a sombra na parede [12, 30]; marcas: máx e mín."""
    if a <= 0:
        return
    X = lambda v: x0 + w * v / 24
    Y = lambda v: y0 + h - h * v / 40
    rrect(c, x0 - 70, y0 - 50, w + 120, h + 120, 16, "#FFFFFF", a)
    for v in (10, 20, 30, 40):
        line(c, x0, Y(v), x0 + w, Y(v), mix("#FFFFFF", INK2, 0.18), a, 1.5)
        ftext(c, str(v), x0 - 14, Y(v) + 9, 22, "bold", INK2, a, align="right")
    for v in (6, 12, 18, 24):
        ftext(c, str(v), X(v), y0 + h + 34, 22, "bold", INK2, a, align="center")
    ftext(c, "0", x0 - 14, y0 + h + 9, 22, "bold", INK2, a, align="right")
    arrow(c, x0, y0 + h, x0 + w + 30, y0 + h, INK2, a, 4, 12)
    arrow(c, x0, y0 + h, x0, y0 - 30, INK2, a, 4, 12)
    ftext(c, "hora", x0 + w + 10, y0 + h - 14, 22, "black", BLUE, a, align="right")
    ftext(c, "°C", x0 + 14, y0 - 16, 22, "black", AMBER, a, align="left")
    if sombra > 0:
        rrect(c, x0 - 14, Y(30), 28, Y(12) - Y(30), 6, GREEN, a * sombra * 0.85)
        line(c, X(14), Y(30), x0, Y(30), GREEN, a * sombra, 3, dash=[10, 8])
        line(c, X(6), Y(12), x0, Y(12), GREEN, a * sombra, 3, dash=[10, 8])
    p = skia.Path()
    tot = len(PTS) - 1
    u = prog_ * tot
    p.moveTo(X(PTS[0][0]), Y(PTS[0][1]))
    for k in range(tot):
        f = clamp(u - k)
        if f <= 0:
            break
        (xa, ya), (xb, yb) = PTS[k], PTS[k + 1]
        p.lineTo(X(xa + (xb - xa) * f), Y(ya + (yb - ya) * f))
    c.drawPath(p, paint(RED, a, stroke=6))
    if marcas > 0:
        for (xv, yv), col, s in (((14, 30), GREEN, "30"), ((6, 12), BLUE, "12")):
            c.drawCircle(X(xv), Y(yv), 11, paint(col, a * marcas))
            ftext(c, s + " °C", X(xv) + 18, Y(yv) + (-14 if yv > 20 else 34), 26, "black", col, a * marcas, align="left")


def tabela_dias(c, x, y, a, dest=0.0):
    """dia | clientes; dest acende as saídas repetidas (52 e 40) em âmbar"""
    if a <= 0:
        return
    rows = [("seg", "40"), ("ter", "52"), ("qua", "52"), ("qui", "61"), ("sex", "40")]
    rh, w1, w2 = 50, 150, 180
    rrect(c, x, y, w1 + w2, rh, 10, BLUE, a)
    ftext(c, "dia", x + w1 / 2, y + 34, 26, "black", "#FFFFFF", a, align="center")
    ftext(c, "clientes", x + w1 + w2 / 2, y + 34, 26, "black", "#FFFFFF", a, align="center")
    for j, (d, v) in enumerate(rows):
        yy = y + rh * (j + 1)
        bg = "#FFFFFF" if j % 2 == 0 else "#F3F3F0"
        rrect(c, x, yy, w1 + w2, rh, 0, bg, a)
        ftext(c, d, x + w1 / 2, yy + 35, 28, "bold", INK, a, align="center")
        col = mix(INK, AMBER, dest) if v in ("52", "40") else INK
        ftext(c, v, x + w1 + w2 / 2, yy + 35, 30, "black", col, a, align="center")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 200, 200, 400, 120, 22, mix("#FFFFFF", PURPLE, 0.14), aa, shadow=True)
        fmid(c, "y = f(x)", W / 2, 260, 56, "black", PURPLE, aa)
    areas = (("FÍSICA", BLUE, 0), ("QUÍMICA", PURPLE, 1), ("BIOLOGIA", GREEN, 2), ("GEOGRAFIA", AMBER, 3))
    for k, (s, col, ic) in enumerate(areas):
        a, d = rise(t, C["01.b"] + 0.5 * k)
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 180, 380 + d, 360, 300, 22, mix("#FFFFFF", col, 0.10), a, shadow=True)
        area_icone(c, ic, x, 500 + d, 0.5, a)
        text_mid(c, s, x, 640 + d, 32, "black", col, a)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        pill(c, "4 provas · 1 habilidade", W / 2, 760, GREEN, size=34, a=ac, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 860, AMBER, ad, 32)
    chip(c, "5 QUESTÕES NOVAS", 1180, 860, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 32)


COBRA = [("02.a", "CALCULAR", "o preço da corrida", BLUE, "f(8) = ?"),
         ("02.b", "CAMINHO DE VOLTA", "f(x) = 30", AMBER, "x = ?"),
         ("02.c", "LER GRÁFICOS", "máximo · sobe · desce", GREEN, "máx?"),
         ("02.d", "DOMÍNIO", "o que faz sentido", PURPLE, "x > 0"),
         ("02.e", "RECONHECER", "tabela · diagrama · curva", RED, "é função?")]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "CINCO TAREFAS", BLUE)
    for k, (cue, tit, sub, col, ex) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 250 + d, 330, 480, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 28, "black", col, a, 290, 36, align="center")
        fit(c, ex, x, 560 + d, 42, 290, "black", INK, a, align="center")
        para(c, sub, x, 640 + d, 24, "bold", INK2, a, 290, 30, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "ENTRADA × SAÍDA", GREEN)
    x0, y0, w, h = 560, 280, 800, 420
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        arrow(c, x0, y0 + h, x0 + w, y0 + h, INK2, aa, 5, 16)
        arrow(c, x0, y0 + h, x0, y0, INK2, aa, 5, 16)
        p = skia.Path(); p.moveTo(x0 + 80, y0 + h - 60); p.cubicTo(x0 + 300, y0 - 40, x0 + 500, y0 + 260, x0 + 720, y0 + 80)
        c.drawPath(p, paint(PURPLE, aa, stroke=6))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        rrect(c, x0 + 80, y0 + h + 14, 640, 14, 7, BLUE, ab * 0.85)
        pill(c, "ENTRADA · x · DOMÍNIO", x0 + w / 2, y0 + h + 80, BLUE, size=30, a=ab, anchor="center")
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        rrect(c, x0 - 30, y0 + 60, 14, h - 120, 7, GREEN, ac * 0.85)
        pill(c, "SAÍDA · y · IMAGEM", 300, y0 + h / 2, GREEN, size=30, a=ac, anchor="center")
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        selo(c, 1580, 300, ad, "NÃO TROQUE!", AMBER, -6, 34)


INDICE = [("EP. 1", "a máquina · data de nascimento: chegar junto pode"),
          ("EP. 2", "cardápio × o que sai · a cadeira vazia do x"),
          ("EP. 3", "ida e volta · as gavetas"),
          ("EP. 4", "a régua em pé · sombras: chão e parede"),
          ("EP. 5", "o porteiro do domínio")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b", "05.c"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 250 + k * 355
        y = 210
        rrect(c, x - 165, y, 330, 600, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 165, y, 330, 600), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 140, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 220, 0.68, a)
        yy = y + 380
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 27, "black", INK if on_ else INK2, a, 290, 33, align="center") + 14


ONDE = [("06.a", "FÍSICA", 0, "v × t não mostra ONDE o carro está", BLUE),
        ("06.b", "QUÍMICA", 1, "cada temperatura: UMA solubilidade", PURPLE),
        ("07.c", "BIOLOGIA", 2, "o ponto mais alto é o “ótimo”", GREEN),
        ("07.d", "GEOGRAFIA", 3, "domínio = o período mostrado", AMBER)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "ONDE A FUNÇÃO APARECE", BLUE)
    for k, (cue, tit, ic, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 220 + d, 410, 520, 24, mix("#F7F7F5", col, 0.08), a)
        text(c, tit, x, 290 + d, 32, "black", col, a)
        area_icone(c, ic, x, 440 + d, 0.55, a)
        para(c, res, x, 610 + d, 30, "black", INK, a, 360, 38, align="center")
    ad = ep(t, C["07.d"] + 2.4, 0.5)
    if ad > 0:
        selo(c, 1540, 790, ad, "NÃO EXTRAPOLE", AMBER, -4, 30)


HABITOS = [("08.a", "1", "LEIA OS EIXOS", "o que está em cada eixo · com as unidades"),
           ("08.b", "2", "DÃO O x OU O y?", "x: calcule f(x) · y: caminho de volta"),
           ("09.c", "3", "DESCUBRA A GAVETA", "função por partes: qual faixa?"),
           ("09.d", "4", "TESTE OS EXTREMOS", "domínio: o porteiro barra o que não serve")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "QUATRO HÁBITOS NA HORA H", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 240 + d, 410, 520, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 310 + d, a, 34, bg=GREEN)
        para(c, tit, x, 400 + d, 32, "black", GREEN, a, 360, 40, align="center")
        yy = 540 + d
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
    ("flechas chegando", "mesmo aniversário → “aluno → data” não é função", False, "duas flechas chegam na mesma data",
     "chegar junto pode · proibido: um aluno com duas datas", "é função", 0),
    ("sem flecha", "um elemento ficou sem flecha → ainda pode ser função", False, "os outros estão certinhos",
     "na máquina, toda entrada tem saída", "não é função", 0),
    ("imagem × contradomínio", "f(x) = x + 1, A = {1, 2, 3}, B = {0, …, 5} → Im = {2, 3, 4}", True,
     "a tentação é responder o B inteiro", "o B é o cardápio · a imagem é o que sai da cozinha", "Im ⊂ B", 1),
    ("a cadeira vazia", "f(x) = x² + 3 → f(3x) = 3x² + 9", False, "o 3 parece multiplicar tudo",
     "o 3x senta na cadeira, com parênteses", "f(3x) = 9x² + 3", 1),
    ("f não é número", "f(x) = x² → f(2 + 3) = f(2) + f(3)", False, "o f parece um número",
     "f é o nome da máquina: 5² = 25, não 4 + 9", "25 ≠ 13", 1),
    ("o caminho de volta", "C(n) = 10 + 4n; pagou R$ 50 → calculo C(50)", False, "o 50 salta aos olhos",
     "deram a saída: 10 + 4n = 50", "n = 10", 2),
    ("eixo da imagem", "a imagem se lê no eixo vertical", True, "a gente lê da esquerda para a direita",
     "a imagem é a sombra na parede · o chão é do domínio", "eixo y", 3),
    ("as pontas", "começa em y = 2 e termina em y = 5 → Im = [2, 5]", False, "o olho vê as pontas primeiro",
     "o máximo pode estar no meio: do mais baixo ao mais alto", "mín → máx", 3),
    ("o contexto", "a fórmula aceita x = −2, mas um comprimento não", True, "a conta dá certo",
     "o porteiro escuta a fórmula E o problema", "medida > 0", 4),
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
    sz = 46
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
            lns += _quebra(parte, 30, 820)
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
        rrect(c, W / 2 - 330, 700, 660, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "na margem: dão o x ou o y?", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · passos: (cue, texto) · confere: (cue, texto) · fig: figura do enunciado

Q = {
    "q1": dict(ids=("21", "22"), titulo="A LANCHONETE", area="RECONHECER FUNÇÃO", ic=4, ok="B", fig="tabela",
               enun=[("a", "Clientes de uma lanchonete, por dia:", False),
                     ("b", "Sobre a relação dia → nº de clientes:", True)],
               alts=[("A", "não é: o 52 aparece em 2 dias", "flechas CHEGANDO podem", RED),
                     ("B", "é função; Im = {40, 52, 61}", "", GREEN),
                     ("C", "é função; Im = {seg, …, sex}", "é o domínio", AMBER),
                     ("D", "não é: o número sobe e desce", "sobe e desce não decide", RED),
                     ("E", "é função; Im = todos de 40 a 61", "o 45 nunca saiu", RED)],
               passos=[("d", "cada dia → UMA saída"), ("a", "é função"), ("a", "Im = o que sai: {40, 52, 61}")],
               confere=None),
    "q2": dict(ids=("23", "24"), titulo="A TEMPERATURA DO DIA", area="GRÁFICO DE OUTRA ÁREA", ic=5, ok="E", fig="grafico",
               enun=[("a", "Temperatura ao longo de um dia:", False),
                     ("b", "a máxima e todas as registradas?", True)],
               alts=[("A", "18 °C; de 16 a 18 °C", "as pontas", RED),
                     ("B", "30 °C; de 0 a 24", "é o domínio (hora)", AMBER),
                     ("C", "14 °C; de 12 a 30 °C", "respondeu QUANDO", RED),
                     ("D", "30 °C; de 0 a 40 °C", "a escala do eixo", AMBER),
                     ("E", "30 °C; de 12 a 30 °C", "", GREEN)],
               passos=[], confere=None),
    "q3": dict(ids=("25", "26"), titulo="O PATINETE", area="O CAMINHO DE VOLTA", ic=6, ok="C", fig=None,
               enun=[("a", "Um patinete cobra R$ 3 para desbloquear e R$ 0,50 por minuto: P(m) = 3 + 0,5m.", False),
                     ("b", "Uma pessoa pagou R$ 12. Quantos minutos andou?", True)],
               alts=[("A", "4 min", "12 ÷ 3: a tarifa fixa", RED), ("B", "9 min", "calculou P(12): a ida", AMBER),
                     ("C", "18 min", "", GREEN), ("D", "24 min", "esqueceu os R$ 3", RED),
                     ("E", "30 min", "somou os R$ 3", RED)],
               passos=[("d", "dão o y: R$ 12 é a saída"), ("a", "3 + 0,5m = 12"), ("a", "0,5m = 9"),
                       ("b", "m = 9 ÷ 0,5 = 18 min")],
               confere=("v", "3 + 0,5 · 18 = 12")),
    "q4": dict(ids=("27", "28"), titulo="A BICICLETA", area="FUNÇÃO POR PARTES", ic=7, ok="D", fig=None,
               enun=[("a", "R$ 5 pela 1ª meia hora e R$ 2 por meia hora adicional OU FRAÇÃO.", False),
                     ("b", "Uso de 1 h 40 min. Quanto pagou?", True)],
               alts=[("A", "R$ 8,00", "sem a 1ª gaveta", RED), ("B", "R$ 9,00", "ignorou a fração", RED),
                     ("C", "R$ 9,67", "cobrou proporcional", AMBER), ("D", "R$ 11,00", "", GREEN),
                     ("E", "R$ 13,00", "1ª também como adicional", RED)],
               passos=[("d", "1 h 40 min = 100 min"), ("a", "1ª meia hora: R$ 5"),
                       ("a", "sobram 70 min = 30 + 30 + 10"), ("b", "3 adicionais: 5 + 3 · 2 = R$ 11")],
               confere=None),
    "q5": dict(ids=("29", "30"), titulo="O CERCADO", area="DOMÍNIO PELO CONTEXTO", ic=8, ok="A", fig=None,
               enun=[("a", "60 m de tela e um muro como um dos lados: os lados medem x, x e 60 − 2x.", False),
                     ("b", "Para que o cercado exista, o domínio de x é:", True)],
               alts=[("A", "0 < x < 30", "", GREEN), ("B", "x > 0", "esqueceu a frente", RED),
                     ("C", "0 < x < 60", "x = 45: área negativa", RED), ("D", "0 ≤ x ≤ 30", "lado zero: sem área", AMBER),
                     ("E", "x < 30", "esqueceu o zero", RED)],
               passos=[("d", "todo lado > 0"), ("a", "x > 0"), ("a", "60 − 2x > 0 → x < 30"),
                       ("b", "as duas: 0 < x < 30")],
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
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 30, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if d["fig"] == "grafico":
            # o gráfico fica na tela também na resolução: a sombra na parede e as marcas entram nela
            ya = 0
            for cue, s, dest in d["enun"]:
                a = ep(t, C[f"{s1}.{cue}"], 0.4)
                ya += para_nb(c, s, 180, 268 + ya, 26, "black" if dest else "bold", BLUE if dest else INK, a, 540, 34) + 4
            area_icone(c, d["ic"], 770, 250, 0.22, a0)
            grafico_temp(c, 270, 400, 470, 290, a0, ep(t, C[s1] + 0.6, 2.0),
                         sombra=ep(t, C[f"{s2}.b"], 0.6), marcas=ep(t, C[f"{s2}.a"], 0.5))
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 760, 760, a=1 - sol)
            ad = ep(t, C[f"{s2}.d"], 0.4)
            if ad > 0:
                pill(c, "QUANTO? → parede (y)", 500, 790, GREEN, size=24, a=ad * (1 - ep(t, C[f"{s2}.ok"], 0.4)),
                     anchor="center")
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
            return
        area_icone(c, d["ic"], 770, 222, 0.30, a0 * (1 - sol))
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            if d["fig"] == "tabela" and dest:
                y = 680
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        if d["fig"] == "tabela":
            tabela_dias(c, 240, 350, ep(t, C[f"{s1}.a"] + 0.5, 0.5) * (1 - sol))
        if d["fig"] == "tabela":
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 700, 480)
        else:
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        if sol > 0:
            yy = 300
            if d["fig"] == "tabela":
                tabela_dias(c, 180, 250, sol, dest=ep(t, C[f"{s2}.xa"], 0.5))
                yy = 590
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.6 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 36 if d["fig"] != "tabela" else 30, 620, "black", GREEN if last else INK, a)
                yy += 62 if d["fig"] != "tabela" else 52
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["a cada x, um único y", "variável independente e dependente",
                               "flechas e tabelas: é função?"]),
         ("31.c", "EP. 2", 1, ["domínio, contradomínio e imagem", "f(a), f(2x) e f(a + b)"]),
         ("32.a", "EP. 3", 2, ["resolver f(x) = k", "por partes: “hora ou fração”"]),
         ("32.b", "EP. 4", 3, ["régua em pé", "domínio e imagem no gráfico", "máximo, zeros, sobe e desce"]),
         ("32.c", "EP. 5", 4, ["domínio: denominador e raiz", "domínio pelo contexto"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 200), (150, 400), (150, 560), (990, 200), (990, 400)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, ic, x + 40, y0 + 90, 0.2, a)
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
        for j in range(3):
            area_icone(c, j * 2 if j < 2 else 3, 300 + j * 110, 670, 0.28, ac)
        text_mid(c, "10 DE GRÁFICOS DE OUTRAS ÁREAS", 1100, 640, 44, "black", BLUE, ac)
        text_mid(c, "Física · Química · Geografia", 1100, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Função afim", W / 2, 330, 62, "black", PURPLE, aa)
    text(c, "gráfico · coeficientes · aplicações", W / 2, 400, 36, "bold", INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    text(c, "a primeira família de funções do bloco", W / 2, 470, 32, "bold", INK2, ab)
    ac = ep(t, C["34.c"], 0.5)
    if ac > 0:
        rrect(c, W / 2 - 420, 530, 840, 160, 24, mix("#FFFFFF", PURPLE, 0.10), ac, shadow=True)
        mx(c, "P(d) = 5 + 2,5d", W / 2, 610, 66, INK, ac, align="center")
    ad = ep(t, C["34.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 760, ad, "NOME E SOBRENOME", GREEN, -4, 34)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
