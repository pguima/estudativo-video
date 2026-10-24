"""Visual — Determinantes e Sistemas Lineares, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): chave · botões de volume · figurinha trocada · semáforo.
Ícones de área (area_icone()): calculadora · triângulo de pontos · frasco · circuito · moeda · ingresso.
Matrizes e determinantes na tela: matriz() (colchetes, ou barras se Det) e expr() (linha com textos e matrizes).
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
_s = importlib.util.spec_from_file_location("comum049", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_determinantes_ep5_revisao.mp4"
CARD_R = K.CARD_R


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra '3 × 3', 'R$ 2', 'k = 3', '25 questões'"""
    s = re.sub(r"(?<=\d) × (?=\d)", " × ", s)
    s = re.sub(r"(?<=\$) (?=\d)", " ", s)
    s = re.sub(r"(?<=\bk) = (?=[−\d])", " = ", s)
    s = re.sub(r"(?<=\d) (?=(questões|acertos)\b)", " ", s)
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
# matrizes e determinantes na tela
# ======================================================================

class Det(list):
    """matriz desenhada com barras (determinante)"""


def mat_wh(vals, cw, ch):
    return len(vals[0]) * cw + 40, len(vals) * ch + 20


def matriz(c, cx, cy, vals, a, cw=90, ch=70, size=40, cores=None, hi=None, hi_col=None, br=None):
    """matriz centrada em (cx, cy): vals = linhas de strings; Det → barras; hi = casas acesas {(i, j)}; devolve (w, h)"""
    w, h = mat_wh(vals, cw, ch)
    if a <= 0:
        return w, h
    x0, y0 = cx - w / 2, cy - h / 2
    bcol = br or INK
    for xx, sg in ((x0, 1), (x0 + w, -1)):
        line(c, xx, y0, xx, y0 + h, bcol, a, 4)
        if not isinstance(vals, Det):
            line(c, xx, y0, xx + 14 * sg, y0, bcol, a, 4)
            line(c, xx, y0 + h, xx + 14 * sg, y0 + h, bcol, a, 4)
    for i, row in enumerate(vals):
        for j, s_ in enumerate(row):
            ccx = x0 + 20 + cw * (j + 0.5)
            ccy = y0 + 10 + ch * (i + 0.5)
            if hi and (i, j) in hi:
                rrect(c, ccx - cw / 2 + 4, ccy - ch / 2 + 4, cw - 8, ch - 8, 10, mix("#FFFFFF", hi_col or AMBER, 0.35), a)
            sz = size if ftw(s_, size) < cw - 10 else size * (cw - 10) / ftw(s_, size)
            ftext(c, s_, ccx, ccy + sz * 0.36, sz, "black", (cores or {}).get((i, j), INK), a)
    return w, h


def M(*linhas):
    """M('1 0', '2 1') → [['1', '0'], ['2', '1']] (o '-' vira '−')"""
    return [[v.replace("-", "−") for v in ln.split()] for ln in linhas]


def DT(*linhas):
    return Det(M(*linhas))


def expr_w(items, size, cw, ch):
    tot = 0
    for it in items:
        tot += (mat_wh(it, cw, ch)[0] if isinstance(it, list) else ftw(nb(it), size)) + 18
    return tot - 18


def expr(c, items, cx, cy, a, size=40, cw=64, ch=52, col=INK, msize=None, maxw=None):
    """linha centrada em (cx, cy) com textos e matrizes; encolhe até caber em maxw; devolve a largura"""
    while maxw and expr_w(items, size, cw, ch) > maxw and size > 22:
        size -= 2; cw *= 0.94; ch *= 0.94
    w = expr_w(items, size, cw, ch)
    if a <= 0:
        return w
    x = cx - w / 2
    for it in items:
        if isinstance(it, list):
            mw, _ = mat_wh(it, cw, ch)
            matriz(c, x + mw / 2, cy, it, a, cw, ch, msize or size * 0.85, br=col,
                   cores={(i, j): col for i in range(len(it)) for j in range(len(it[0]))})
            x += mw + 18
        else:
            s = nb(it)
            ftext(c, s, x, cy + size * 0.36, size, "black", col, a, align="left")
            x += ftw(s, size) + 18
    return w


def sistema(c, eqs, x, y, size, a, col=INK, lh=None):
    """sistema com chave à esquerda: eqs = lista de strings; (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    lh = lh or size * 1.5
    h = lh * len(eqs)
    p = skia.Path()
    p.moveTo(x + 22, y); p.quadTo(x + 6, y, x + 8, y + h * 0.25); p.lineTo(x + 8, y + h * 0.42)
    p.quadTo(x + 8, y + h * 0.5, x - 4, y + h * 0.5); p.quadTo(x + 8, y + h * 0.5, x + 8, y + h * 0.58)
    p.lineTo(x + 8, y + h * 0.75); p.quadTo(x + 6, y + h, x + 22, y + h)
    c.drawPath(p, paint(col, a, stroke=4))
    for k, s in enumerate(eqs):
        ftext(c, nb(s), x + 40, y + lh * (k + 0.5) + size * 0.36, size, "black", col, a, align="left")


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def chave_ic(c, a):
    """ep1: o teste da chave (det ≠ 0, a inversa existe)"""
    c.drawCircle(-110, 0, 80, paint(AMBER, a))
    c.drawCircle(-110, 0, 34, paint("#FFFFFF", a))
    rrect(c, -40, -20, 240, 40, 12, AMBER, a)
    rrect(c, 130, 20, 26, 54, 6, AMBER, a); rrect(c, 80, 20, 26, 40, 6, AMBER, a)
    ftext(c, "det ≠ 0", 20, 170, 54, "black", BLUE, a, align="center")


def botoes_ic(c, a):
    """ep2: os botões de volume (k^n)"""
    for k in range(3):
        x = -150 + k * 150
        c.drawCircle(x, -20, 62, paint(mix("#FFFFFF", PURPLE, 0.25), a))
        c.drawCircle(x, -20, 62, paint(PURPLE, a, stroke=8))
        line(c, x, -20, x + 34, -62, PURPLE, a, 10)
    ftext(c, "kⁿ", 0, 150, 76, "black", PURPLE, a, align="center")


def figurinha_ic(c, a):
    """ep3: a troca de figurinha do Dₓ (sai a coluna do x, entram os resultados)"""
    rrect(c, -200, -130, 300, 230, 20, "#FFFFFF", a, shadow=True, stroke=4, stroke_color=INK2)
    rrect(c, -180, -110, 110, 190, 14, mix("#FFFFFF", RED, 0.25), a * 0.7, stroke=3, stroke_color=RED)
    ftext(c, "x", -125, 0, 60, "black", RED, a, align="center")
    line(c, -55, -110, -55, 80, LIGHT, a, 3)
    rrect(c, 120, -150, 110, 190, 14, mix("#FFFFFF", GREEN, 0.25), a, shadow=True, stroke=4, stroke_color=GREEN)
    ftext(c, "=", 175, -40, 60, "black", GREEN, a, align="center")
    arrow(c, 120, 80, -60, 130, GREEN, a, 6, 16)


def semaforo_ic(c, a):
    """ep4: o semáforo (verde = uma solução; amarelo = olhe as equações)"""
    rrect(c, -80, -200, 160, 380, 30, INK, a, shadow=True)
    for k, col in enumerate((RED, AMBER, GREEN)):
        on = k > 0
        c.drawCircle(0, -125 + k * 120, 46, paint(col if on else mix(col, INK, 0.65), a))
    rrect(c, -14, 180, 28, 60, 6, INK2, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (chave_ic, botoes_ic, figurinha_ic, semaforo_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def calc_ic(c, a):
    rrect(c, -130, -170, 260, 340, 30, INK, a, shadow=True)
    rrect(c, -100, -140, 200, 80, 12, mix("#FFFFFF", GREEN, 0.35), a)
    ftext(c, "D", 70, -82, 52, "black", INK, a, align="right")
    for i in range(3):
        for j in range(3):
            rrect(c, -100 + j * 72, -40 + i * 66, 56, 52, 10, "#FFFFFF" if (i, j) != (2, 2) else AMBER, a)


def triangulo_ic(c, a):
    pts = [(-140, 110), (20, -130), (150, 80)]
    p = skia.Path(); p.moveTo(*pts[0]); p.lineTo(*pts[1]); p.lineTo(*pts[2]); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.20), a)); c.drawPath(p, paint(BLUE, a, stroke=6))
    for x, y in pts:
        c.drawCircle(x, y, 22, paint(BLUE, a))


def frasco_ic(c, a):
    p = skia.Path(); p.moveTo(-40, -160); p.lineTo(40, -160); p.lineTo(40, -40); p.lineTo(130, 140)
    p.lineTo(-130, 140); p.lineTo(-40, -40); p.close()
    c.drawPath(p, paint("#FFFFFF", a)); c.drawPath(p, paint(INK2, a, stroke=6))
    q = skia.Path(); q.moveTo(-85, 50); q.lineTo(85, 50); q.lineTo(127, 135); q.lineTo(-127, 135); q.close()
    c.drawPath(q, paint(mix("#FFFFFF", GREEN, 0.55), a))
    for x, y in ((-30, 90), (25, 110), (60, 80)):
        c.drawCircle(x, y, 12, paint("#FFFFFF", a))


def circuito_ic(c, a):
    for x0, y0, x1, y1 in ((-150, -100, 150, -100), (150, -100, 150, 110), (150, 110, -150, 110), (-150, 110, -150, -100),
                           (0, -100, 0, 110)):
        line(c, x0, y0, x1, y1, INK2, a, 7)
    for x in (-75, 75):
        p = skia.Path(); p.moveTo(x - 36, -100)
        for k in range(6):
            p.lineTo(x - 30 + k * 12, -100 + (-18 if k % 2 == 0 else 18))
        p.lineTo(x + 36, -100)
        rrect(c, x - 40, -118, 80, 36, 6, "#FFFFFF", a)
        c.drawPath(p, paint(AMBER, a, stroke=6))
    line(c, -168, 0, -132, 0, INK, a, 8); line(c, -160, 22, -140, 22, INK, a, 8)


def moeda_ic(c, a):
    c.drawCircle(0, 0, 140, paint(AMBER, a))
    c.drawCircle(0, 0, 112, paint(mix(AMBER, INK, 0.25), a, stroke=8))
    ftext(c, "R$", 0, 26, 86, "black", "#FFFFFF", a, align="center")


def ingresso_ic(c, a):
    rrect(c, -170, -90, 340, 180, 20, mix("#FFFFFF", PURPLE, 0.25), a, shadow=True, stroke=4, stroke_color=PURPLE)
    for y in range(-70, 80, 26):
        c.drawCircle(70, y, 5, paint(PURPLE, a))
    ftext(c, "R$ 40", -50, 18, 52, "black", PURPLE, a, align="center")


AREA_F = (calc_ic, triangulo_ic, frasco_ic, circuito_ic, moeda_ic, ingresso_ic)


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
    for k, (s, ic, col, x) in enumerate((("ingressos", 5, PURPLE, 520), ("lanchonete", 4, AMBER, 1400))):
        a, d = rise(t, C["01.a"] + 0.6 * k)
        if a <= 0:
            continue
        rrect(c, x - 230, 200 + d, 460, 280, 26, mix("#F7F7F5", col, 0.12), a)
        area_icone(c, ic, x, 310 + d, 0.48, a)
        fit(c, s, x, 445 + d, 36, 400, "black", col, a, align="center")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 760, 230, 400, 220, 30, "#FFFFFF", ab, shadow=True)
        area_icone(c, 0, 960, 340, 0.45, ab)
        pill(c, "o atalho: D", W / 2, 500, GREEN, size=30, a=ab, anchor="center")
    for k, (cue, s, col) in enumerate((("01.c", "qual é o valor pedido?", BLUE), ("01.d", "existe uma resposta só?", PURPLE))):
        a = ep(t, C[cue], 0.5)
        if a > 0:
            x = 520 + k * 880
            rrect(c, x - 400, 570, 800, 110, 55, mix("#FFFFFF", col, 0.18), a, shadow=True)
            text_mid(c, s, x, 625, 44, "black", col, a)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        chip(c, "9 V OU F", 760, 790, AMBER, ae, 30)
        chip(c, "5 QUESTÕES NOVAS", 1200, 790, GREEN, ep(t, C["01.e"] + 0.5, 0.4), 30)


COBRA = [("02.a", "DETERMINANTE", "o número que diz se há inversa", BLUE, "ic", 0),
         ("02.b", "REGRA DE CRAMER", "cada incógnita = divisão de determinantes", PURPLE, "ic", 2),
         ("02.c", "CLASSIFICAÇÃO", "uma · infinitas · nenhuma", GREEN, "ic", 3)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "TRÊS FERRAMENTAS", BLUE)
    for k, (cue, tit, sub_, col, _, ic) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 240 + d, 460, 520, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 300 + d, a, 28, bg=col)
        para(c, tit, x, 380 + d, 34, "black", col, a, 420, 40, align="center")
        icone(c, ic, x, 540 + d, 0.48, a)
        para_nb(c, sub_, x, 690 + d, 28, "black", INK2, a, 400, 34, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "O SEMÁFORO DO D", BLUE)
    icone(c, 3, 330, 500, 0.85, ep(t, C["03.t"], 0.5))
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        boxed(c, 560, 230, 1140, 150, GREEN, aa, 0.10)
        fit(c, "D ≠ 0", 610, 325, 64, 260, "black", GREEN, aa)
        fit(c, "uma solução só", 900, 325, 50, 760, "black", INK, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        boxed(c, 560, 420, 1140, 150, AMBER, ab, 0.10)
        fit(c, "D = 0", 610, 515, 64, 260, "black", AMBER, ab)
        fit(c, "olhe as equações", 900, 515, 50, 760, "black", INK, ab)
    for k, (cue, s1, s2, col) in enumerate((("03.c", "brigam", "nenhuma solução", RED),
                                            ("03.d", "repetidas", "infinitas", BLUE))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 700 + k * 560
        rrect(c, x - 250, 620 + d, 500, 160, 22, mix("#FFFFFF", col, 0.14), a, shadow=True)
        text_mid(c, s1, x, 670 + d, 36, "black", col, a)
        text_mid(c, s2, x, 730 + d, 34, "bold", INK, a)


INDICE = [("EP. 1", "o teste da chave: det ≠ 0, abre · o produto de casaco · time verde × time vermelho"),
          ("EP. 2", "linhas parentes zeram o det · os botões de volume: kⁿ"),
          ("EP. 3", "a troca de figurinha: sai a coluna do x · D é o chão da fração"),
          ("EP. 4", "o semáforo: verde = uma; amarelo = olhe · gêmeas e brigadas · a porta (0, 0)")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 300, 380, 1320, 160, 30, "#FFFFFF", aq, shadow=True)
        fmid(c, "2 × 2: e o produto da secundária?", W / 2, 460, 54, "black", INK, aq)
        pause_timer(c, t, C["04.t"] + 2.6, 1480, 640, a=aq)
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
        icone(c, k, x, y + 200, 0.56, a)
        yy = y + 360
        for ln in s.split(" · "):
            yy += para_nb(c, ln, x, yy, 24, "black", INK if on_ else INK2, a, 340, 30, align="center") + 10


ONDE = [("06.a", "GEOMETRIA ANALÍTICA", 1, "área e alinhamento de 3 pontos", BLUE),
        ("06.b", "QUÍMICA", 2, "balanceamento = sistema homogêneo", GREEN),
        ("07.c", "FÍSICA", 3, "malhas de circuitos", AMBER),
        ("07.d", "ECONOMIA", 4, "misturas, cestas e combos", PURPLE)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS ÁREAS", "O MESMO SISTEMA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 185, 230 + d, 370, 560, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 290 + d, 30, "black", col, a, 340, 36, align="center")
        area_icone(c, ic, x, 480 + d, 0.42, a)
        para_nb(c, res, x, 660 + d, 28, "black", INK, a, 330, 34, align="center")
    sa = ep(t, C["06.a"] + 2.6, 0.4) * (1 - ep(t, C["06.b"], 0.3))
    if sa > 0:
        pill(c, "série própria", 358, 770, BLUE, size=22, a=sa, anchor="center")


HABITOS = [("08.a", "PROCURE A PROPRIEDADE", "zeros · linhas parentes → det = 0 na hora"),
           ("08.b", "SÓ O NECESSÁRIO", "uma incógnita? Cramer nela · quantas soluções? classifique"),
           ("09.c", "CONFIRA NAS ORIGINAIS", "substituir pega quase todo erro de sinal")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS NA HORA H", GREEN)
    for k, (cue, tit, sub_) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 240, 240 + d, 480, 520, 24, mix("#F7F7F5", GREEN, 0.10), a, shadow=True)
        badge_num(c, k + 1, x, 310 + d, a, 34, bg=GREEN)
        para(c, tit, x, 410 + d, 36, "black", GREEN, a, 420, 44, align="center")
        yy = 540 + d
        for ln in sub_.split(" · "):
            yy += para_nb(c, ln, x, yy, 30, "bold", INK, a, 420, 38, align="center") + 14


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


# (contexto, afirmação [itens], verdadeira?, por que engana, regra certa, versão certa [itens], ícone do episódio)
VF = [
    ("o 2 × 2", [DT("3 -2", "4 5"), "= 15 − 8 = 7"], False, "o 8 aparece mesmo na conta",
     "o produto entra de casaco: (−2) · 4 = −8", ["15 − (−8) = 23"], 0),
    ("Sarrus", ["o menos vale só para o 1º produto vermelho"], False, "os produtos vêm um atrás do outro",
     "time contra time: subtraia o bloco vermelho inteiro", ["verde − (todo o vermelho)"], 0),
    ("os botões de volume", ["3 × 3, det A = 2  →  det(2A) = 16"], True, "dá vontade de responder 4",
     "três botões: 2³ · 2", ["8 · 2 = 16"], 1),
    ("D = 0", ["D = 0  →  impossível"], False, "o zero parece dizer “não tem jeito”",
     "D = 0: olhe as equações | x + y = 2 e 2x + 2y = 4", ["gêmeas: infinitas"], 3),
    ("achou uma solução", ["achou (1, 1)  →  solução única"], False, "a conta deu certo",
     "com D = 0, ela é só uma entre muitas", ["(0, 2) · (3, −1)"], 3),
    ("o Dₓ", ["Dₓ: tire a COLUNA do x, ponha os resultados"], True, "muita gente troca a linha",
     "a figurinha trocada é a coluna", ["coluna do x → resultados"], 2),
    ("Cramer", ["x = D ÷ Dₓ"], False, "os dois determinantes estão ali",
     "D é o chão da fração: x = Dₓ ÷ D", ["−6 ÷ (−2) = 3"], 2),
    ("o homogêneo", ["um homogêneo nunca é impossível"], True, "ele pode ter D = 0",
     "a porta (0, 0) sempre resolve | a pergunta é se há outras", ["(0, 0) sempre"], 3),
    ("o parâmetro", ["k² = 4  →  k = 2"], False, "o 2 é a resposta que vem primeiro",
     "é do 2º grau: duas raízes", ["k = 2 ou k = −2"], 3),
]
VF_IDS = [f"{11 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, itens, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 62 + k * 62, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 300, 420, 0.40, a0)
    fmid(c, ctx.upper(), 960, 280, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    w = expr(c, itens, 960, 420, a0, 46, 66, 56, maxw=820)
    if ar > 0 and not ver:
        strike(c, 960 - w / 2 - 10, 424, 960 + w / 2 + 10, 424, ar, RED, ar)
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
        expr(c, fix, 1460, 725, ag, 40, 52, 44, col=GREEN, maxw=440)


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
        text_mid(c, "calcule o D primeiro · resolva · confira", W / 2, 750, 34, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="O DETERMINANTE 2 × 2", area="DETERMINANTE", ok="C",
               enun=[("a", "O determinante da matriz abaixo é:", False)],
               alts=[("A", "14", "20 − 6", AMBER), ("B", "−14", "os dois erros", RED), ("C", "26", "", GREEN),
                     ("D", "−26", "secundária − principal", RED), ("E", "9", "somou a diagonal", RED)],
               passos=[("d", "principal − secundária, com casaco"), ("a", "4 · 5 − (−3) · 2"), ("a", "20 + 6 = 26")]),
    "q2": dict(ids=("23", "24"), titulo="OS BOTÕES DE VOLUME", area="PROPRIEDADES", ok="C",
               enun=[("a", "A de ordem 2 · det A = 4", True), ("b", "O determinante de 3A é:", False)],
               alts=[("A", "7", "3 + 4", RED), ("B", "12", "um botão só", AMBER), ("C", "36", "", GREEN),
                     ("D", "64", "4³", RED), ("E", "108", "3³: como se fosse 3 × 3", RED)],
               passos=[("d", "ordem 2 → dois botões"), ("a", "det(3A) = 3² · 4"), ("a", "9 · 4 = 36")]),
    "q3": dict(ids=("25", "26"), titulo="O PREÇO DA CANETA", area="REGRA DE CRAMER", ok="B",
               enun=[("a", "3 cadernos + 2 canetas = R$ 34 · 2 cadernos + 5 canetas = R$ 30", False),
                     ("b", "O preço de uma caneta é:", True)],
               alts=[("A", "R$ 0,50", "D ÷ Dₚ (invertida)", RED), ("B", "R$ 2,00", "", GREEN),
                     ("C", "R$ 10,00", "é o caderno", AMBER), ("D", "R$ 11,00", "é o próprio D", RED),
                     ("E", "R$ 22,00", "Dₚ sem dividir", RED)],
               passos=[("d", "só a caneta: Cramer só em p"), ("a", "D = 15 − 4 = 11"), ("a", "Dₚ = 90 − 68 = 22"),
                       ("a", "p = 22 ÷ 11 = R$ 2"), ("v", "caderno R$ 10: 20 + 10 = 30 ✓")]),
    "q4": dict(ids=("27", "28"), titulo="E SE O D ZERAR?", area="DISCUSSÃO COM PARÂMETRO", ok="B",
               enun=[("a", "Sobre o sistema, é correto afirmar que ele:", False)],
               alts=[("A", "é impossível se k = 3", "D = 0 ≠ impossível", AMBER),
                     ("B", "tem infinitas se k = 3", "", GREEN), ("C", "solução única p/ todo k", "ignorou D = 0", RED),
                     ("D", "tem infinitas se k = −3", "erro de sinal", RED),
                     ("E", "é impossível se k ≠ 3", "aí é solução única", RED)],
               passos=[("d", "D = 2k − 6 = 0  →  k = 3"), ("a", "6, 3, 12 = 3 · (2, 1, 4)"), ("a", "gêmeas: infinitas"),
                       ("v", "nenhum k dá impossível")]),
    "q5": dict(ids=("29", "30"), titulo="A PORTA (0, 0)", area="SISTEMA HOMOGÊNEO", ok="A",
               enun=[("a", "Há soluções além de (0, 0) quando:", True)],
               alts=[("A", "k = 3", "", GREEN), ("B", "k = −3", "erro de sinal", RED),
                     ("C", "k = 0", "D = −3: só a trivial", AMBER), ("D", "k ≠ 3", "é a solução única", RED),
                     ("E", "nunca", "D = 0 abre outras", RED)],
               passos=[("d", "a pergunta: há outras?"), ("a", "D = k − 3 = 0  →  k = 3"), ("v", "(1, −1) resolve as duas")]),
}


def fig_q1(c, a, sol, prog):
    matriz(c, 480, 600 if not sol else 690, DT("4 -3", "2 5"), a, 110, 86, 48,
           cores={(0, 0): BLUE, (1, 1): BLUE, (0, 1): AMBER, (1, 0): AMBER} if sol else None)


def fig_q2(c, a, sol, prog):
    if not sol:
        icone(c, 1, 480, 590, 0.62, a)


def fig_q3(c, a, sol, prog):
    if not sol:
        sistema(c, ["3c + 2p = 34", "2c + 5p = 30"], 300, 520, 44, a)


def fig_q4(c, a, sol, prog):
    sistema(c, ["2x + y = 4", "6x + ky = 12"], 300, 340 if not sol else 610, 44 if not sol else 34, a)


def fig_q5(c, a, sol, prog):
    sistema(c, ["x + y = 0", "3x + ky = 0"], 300, 330 if not sol else 600, 44 if not sol else 34, a)


FIGS = dict(q1=fig_q1, q2=fig_q2, q3=fig_q3, q4=fig_q4, q5=fig_q5)
Y_ENUN = dict(q1=280, q2=280, q3=280, q4=540, q5=540)


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
        area_icone(c, 0, 770, 222, 0.18, a0)
        y = Y_ENUN[nome]
        ae = ep(t, C[f"{s1}.a"], 0.4) * (1 - sol)
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            parts = s.split(" · ")
            for p_ in parts:
                h = para_nb(c, p_, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 620, 40)
                y += h + 10
            y += 4
        FIGS[nome](c, ae, False, 0)
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 760, 790)
        if sol > 0:
            yy = 280
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 30, 640, "black", GREEN if last else INK, a)
                yy += 60
            FIGS[nome](c, sol, True, t - C[f"{s2}.a"])
            result_box(c, f"Letra {d['ok']}", 1290, 790, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["2 × 2 sem errar o sinal", "Sarrus e Laplace", "det ≠ 0 ↔ tem inversa"]),
         ("31.c", "EP. 2", 1, ["det = 0 por linhas parentes", "det(kA) = kⁿ · det A", "det(AB) = det A · det B"]),
         ("32.a", "EP. 3", 2, ["escrevo A · X = B", "Cramer: troco a coluna certa", "e divido por D"]),
         ("32.b", "EP. 4", 3, ["SPD, SPI e SI · D = 0 não é SI", "parâmetro em dois passos", "homogêneo: há outras?"])]


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
        if ac > 0 and i < 6:
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
        icone(c, 3, 890, 630, 0.30, ac)
        fit(c, "6 de classificação", 970, 605, 40, 700, "black", PURPLE, ac)
        fit(c, "ou discussão de sistemas", 970, 670, 36, 700, "bold", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 240, 28, "black", GRAY, aa, tracking=2)
    text(c, "Polinômios e equações polinomiais", W / 2, 330, 66, "black", PURPLE, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 420, 620, 260, 30, mix("#FFFFFF", BLUE, 0.14), ab, shadow=True)
        text_mid(c, "várias incógnitas", 570, 480, 38, "black", BLUE, ab)
        sistema(c, ["x + y + z = 6", "2x − y = 1"], 380, 520, 34, ab, col=INK)
    ac = ep(t, C["34.c"], 0.5)
    if ac > 0:
        arrow(c, 910, 550, 1030, 550, PURPLE, ac, 6, 16)
        rrect(c, 1050, 420, 620, 260, 30, mix("#FFFFFF", PURPLE, 0.18), ac, shadow=True)
        text_mid(c, "uma incógnita, grau alto", 1360, 480, 38, "black", PURPLE, ac)
        text_mid(c, "x⁴ − 5x² + 4 = 0", 1360, 590, 54, "black", INK, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
