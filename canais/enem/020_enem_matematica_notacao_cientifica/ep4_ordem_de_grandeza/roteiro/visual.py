"""Visual — Notação Científica e Ordem de Grandeza, Episódio 4: ordem de grandeza e a conta de guardanapo (iniciantes, tema claro).
Peças comuns em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, erro_cards, atalho...).
Peças deste episódio: rua de casas (potências de 10), régua de multiplicar (1 · 3,16 · 10), zoom do átomo ao Sol, guardanapo.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum020", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_notacao_ep4_ordem_de_grandeza.mp4"
CARD_R = K.CARD_R
GUARD = "#FFFDF4"        # papel do guardanapo
GUARD_B = "#E3D9BF"
CANETA = "#2B4C9A"       # tinta de caneta azul


def mono(n, col):
    return {i: col for i in range(n)}


def caixa_atalho(c, x, y, w, h, titulo, linha, a, size=32):
    if a <= 0:
        return
    boxed(c, x, y, w, h, GREEN, a, 0.10)
    text(c, titulo, x + w / 2, y + 40, 20, "black", GREEN, a, tracking=2)
    ftext(c, linha, x + w / 2, y + h / 2 + 22, size, "black", INK, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "ORDEM DE GRANDEZA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text_mid(c, "850 000", W / 2, 300, 150, "black", INK, aa)
    text(c, "ordem de grandeza = ?", W / 2, 430, 40, "black", BLUE, aa)
    ab = ep(t, C["01.b"], 0.5)
    ac = ep(t, C["01.c"], 0.5)
    if ab > 0:
        expr(c, "8,5·10^5", 620, 590, 80, ab, cores={0: INK})
        expr(c, "→ 10^5 ?", 620, 720, 70, ab * (1 - 0.6 * ac), cores={0: AMBER, 1: RED})
        if ac > 0:
            strike(c, 560, 720, 760, 720, ac, RED, ac)
        selo(c, 900, 640, ab * (1 - ac), "QUASE TODO MUNDO", AMBER, -6, 28)
    if ac > 0:
        rrect(c, 1080, 520, 520, 260, 30, GREEN, 0.10 * ac)
        text(c, "a resposta", 1340, 580, 30, "black", GREEN, ac)
        expr(c, "10^6", 1340, 690, 120, ac, cores={0: GREEN})
    pill(c, "muitas questões: 15 segundos", W / 2, 810, GREEN, size=28, a=ep(t, C["01.d"], 0.5), anchor="center", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "achar a ordem de grandeza", "pelo critério certo (não é o expoente escrito)"),
            ("02.b", "estimar para eliminar", "sem fazer a conta inteira")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 52, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "FORMA EXATA", 560, 250, 30, "black", BLUE, aa, tracking=1)
        expr(c, "8,5·10^5", 560, 420, 110, aa)
        rrect(c, 380, 340, 150, 150, 18, BLUE, 0.12 * aa)
        arrow(c, 455, 580, 455, 500, BLUE, aa, 5, 16, progress=aa)
        text(c, "COEFICIENTE", 455, 625, 30, "black", BLUE, aa)
        text(c, "1 algarismo (≠ 0) antes da vírgula", 560, 700, 30, "bold", INK2, aa)
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "MULTIPLICAR", 1360, 250, 30, "black", PURPLE, ab, tracking=1)
        text(c, "coeficiente × coeficiente", 1360, 340, 34, "black", INK, ab)
        text(c, "expoente + expoente", 1360, 400, 34, "black", PURPLE, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        text(c, "a GANGORRA conserta", 1360, 520, 28, "black", AMBER, acc)
        expr(c, "40·10^6 = 4·10^7", 1360, 620, 60, acc, cores={2: GREEN})
        text(c, "coeficiente ÷ 10, expoente + 1", 1360, 720, 26, "bold", INK2, acc)


# ======================================================================
# concreto: escalas
# ======================================================================

def _icone(c, kind, cx, cy, r, a):
    if a <= 0:
        return
    if kind == "cabelo":
        p = skia.Path(); p.moveTo(cx - r, cy + r * 0.6); p.cubicTo(cx - r * 0.3, cy - r, cx + r * 0.3, cy + r, cx + r, cy - r * 0.6)
        c.drawPath(p, paint("#6B4A2B", a, stroke=r * 0.16, cap_round=True))
    elif kind == "virus":
        for k in range(10):
            ang = 2 * math.pi * k / 10
            x1, y1 = cx + r * 0.62 * math.cos(ang), cy + r * 0.62 * math.sin(ang)
            x2, y2 = cx + r * 0.95 * math.cos(ang), cy + r * 0.95 * math.sin(ang)
            c.drawLine(x1, y1, x2, y2, paint("#C0392B", a, stroke=6, cap_round=True))
            c.drawCircle(x2, y2, 7, paint("#C0392B", a))
        c.drawCircle(cx, cy, r * 0.62, paint("#E8735F", a))
    elif kind == "celula":
        c.drawCircle(cx, cy, r * 0.9, paint("#BDE3C9", a))
        c.drawCircle(cx, cy, r * 0.9, paint("#3E9B63", a, stroke=5))
        c.drawCircle(cx + r * 0.15, cy - r * 0.1, r * 0.32, paint("#6A5ACD", a * 0.85))
    elif kind == "atomo":
        c.drawCircle(cx, cy, r * 0.18, paint(RED, a))
        for k in range(3):
            c.save(); c.translate(cx, cy); c.rotate(60 * k)
            c.drawOval(skia.Rect.MakeLTRB(-r * 0.95, -r * 0.35, r * 0.95, r * 0.35), paint(BLUE, a, stroke=4))
            c.restore()
    elif kind == "terra":
        c.drawCircle(cx, cy, r * 0.9, paint("#3A7BD5", a))
        for (dx, dy, rr) in ((-0.3, -0.2, 0.32), (0.3, 0.25, 0.26), (0.25, -0.4, 0.18)):
            c.drawCircle(cx + dx * r, cy + dy * r, rr * r, paint("#4CAF6A", a))
    elif kind == "sol":
        for k in range(12):
            ang = 2 * math.pi * k / 12
            c.drawLine(cx + r * 0.75 * math.cos(ang), cy + r * 0.75 * math.sin(ang), cx + r * math.cos(ang),
                       cy + r * math.sin(ang), paint("#F5A623", a, stroke=6, cap_round=True))
        c.drawCircle(cx, cy, r * 0.62, paint("#FFC93C", a))
    elif kind == "gente":
        for k in range(3):
            x = cx + (k - 1) * r * 0.62
            c.drawCircle(x, cy - r * 0.35, r * 0.2, paint(BLUE, a))
            rrect(c, x - r * 0.24, cy - r * 0.1, r * 0.48, r * 0.6, r * 0.2, BLUE, a)
    elif kind == "mapa":
        rrect(c, cx - r, cy - r * 0.7, 2 * r, 1.4 * r, 14, "#E8F1E4", a)
        p = skia.Path(); p.moveTo(cx - r * 0.5, cy - r * 0.5); p.lineTo(cx + r * 0.4, cy - r * 0.4); p.lineTo(cx + r * 0.6, cy + r * 0.2)
        p.lineTo(cx, cy + r * 0.55); p.lineTo(cx - r * 0.6, cy + r * 0.1); p.close()
        c.drawPath(p, paint("#4CAF6A", a))


ESCALAS = [("04.a", "cabelo", "fio de cabelo", "0,0001 m"), ("04.b", "virus", "vírus", "0,0000001 m"),
           ("04.c", "gente", "população do Brasil", "200 000 000"), ("04.d", "sol", "Terra → Sol", "150 000 000 000 m")]


def b_escala(c, t, C, B):
    frame(c, t, B["start"], "NÚMEROS MUITO DIFERENTES", "COMO COMPARAR?", BLUE)
    for k, (cue, kind, nome, val) in enumerate(ESCALAS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 340 + k * 413
        rrect(c, x - 185, 210 + d, 370, 380, 24, "#F7F7F5", a)
        _icone(c, kind, x, 330 + d, 80, a)
        text(c, nome, x, 470 + d, 32, "black", INK, a)
        size = 34
        while text_w(val, "black", size) > 340:
            size -= 2
        text(c, val, x, 540 + d, size, "black", PURPLE, a)
    ae = ep(t, C["04.e"], 0.5)
    text(c, "o valor exato quase não importa", W / 2, 660, 34, "bold", INK2, ae)
    af = ep(t, C["04.f"], 0.5)
    if af > 0:
        boxed(c, 420, 700, 1080, 110, BLUE, af, 0.10)
        text(c, "ESCALA = o tamanho aproximado", W / 2, 750, 36, "black", BLUE, af)
        text(c, "milhares · milhões · bilhões", W / 2, 792, 26, "bold", INK2, af)


# ======================================================================
# bloco A — definição (a rua das casas)
# ======================================================================

CASAS = ["10^1", "10^2", "10^3", "10^4", "10^5", "10^6"]
CASAS_V = ["10", "100", "1 000", "10 000", "100 000", "1 000 000"]


def _casa(c, x, y, w, h, s, v, a, hl=0.0):
    col = mix("#FFFFFF", GREEN, 0.25 * hl)
    p = skia.Path(); p.moveTo(x - 10, y); p.lineTo(x + w / 2, y - h * 0.42); p.lineTo(x + w + 10, y); p.close()
    c.drawPath(p, paint(mix(PURPLE, GREEN, hl), a))
    rrect(c, x, y, w, h, 10, col, a, shadow=True)
    expr(c, s, x + w / 2, y + h * 0.38, 40, a, cores={0: mix(PURPLE, GREEN, hl)})
    text(c, v, x + w / 2, y + h * 0.82, 22, "black", INK2, a)


def b_definicao(c, t, C, B):
    frame(c, t, B["start"], "COMO MEDIR A ESCALA?", "ORDEM DE GRANDEZA", BLUE)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 200, 1320, 120, BLUE, aa, 0.08)
        text(c, "ORDEM DE GRANDEZA", W / 2, 245, 24, "black", BLUE, aa, tracking=2)
        text(c, "a potência de 10 mais próxima do número", W / 2, 298, 40, "black", INK, aa)
    ab = ep(t, C["05.b"], 0.5)
    acc = ep(t, C["05.c"], 0.5)
    if ab > 0:
        line(c, 200, 640, 1720, 640, "#CFCFC8", ab, 6)
        for k, (s, v) in enumerate(zip(CASAS, CASAS_V)):
            ak = ab * ep(t, C["05.b"] + 0.25 * k, 0.3)
            _casa(c, 230 + k * 250, 450, 190, 190, s, v, ak, acc if k == 5 else 0.0)
    if acc > 0:
        bx = 230 + 5 * 250 + 95
        u = ep(t, C["05.c"], 0.9)
        x = lerp(bx - 380, bx, u)
        c.drawCircle(x, 690, 22, paint(AMBER, acc))
        text(c, "850 000 mora aqui", x, 745, 28, "black", AMBER, acc)
    chip(c, "não diz o valor: diz a ESCALA", W / 2, 800, PURPLE, ep(t, C["05.d"], 0.5), 30)


# ======================================================================
# bloco B — a intuição (reta linear)
# ======================================================================

def b_intuicao(c, t, C, B):
    frame(c, t, B["start"], "850 000", "MAIS PERTO DE QUEM?", BLUE)
    x0, x1, y = 260, 1660, 470
    X = lambda v: lerp(x0, x1, v / 1_000_000)
    aa = ep(t, C["06.a"], 0.5)
    a0 = ep(t, C["06"], 0.5)
    line(c, x0, y, x1, y, INK2, a0, 5)
    for v in range(0, 1_000_001, 100_000):
        line(c, X(v), y - 10, X(v), y + 10, LIGHT, a0, 3)
    if aa > 0:
        for v, lab, s in ((100_000, "100 000", "10^5"), (1_000_000, "1 000 000", "10^6")):
            c.drawCircle(X(v), y, 14, paint(PURPLE, aa))
            text(c, lab, X(v), y + 60, 28, "black", INK, aa)
            expr(c, s, X(v), y + 120, 44, aa, cores={0: PURPLE})
    xv = X(850_000)
    c.drawCircle(xv, y, 18, paint(AMBER, a0))
    text(c, "850 000", xv, y - 40, 34, "black", AMBER, a0)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        p = skia.Path(); p.moveTo(X(100_000), y - 70); p.quadTo((X(100_000) + xv) / 2, y - 170, xv - 20, y - 80)
        c.drawPath(p, paint(LIGHT, ab, stroke=4, cap_round=True))
        text(c, "750 000", (X(100_000) + xv) / 2, y - 150, 30, "black", GRAY, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        p = skia.Path(); p.moveTo(xv + 20, y - 80); p.quadTo((xv + X(1_000_000)) / 2, y - 150, X(1_000_000), y - 40)
        c.drawPath(p, paint(GREEN, acc, stroke=5, cap_round=True))
        text(c, "faltam 150 000", (xv + X(1_000_000)) / 2 - 10, y - 140, 28, "black", GREEN, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        chip(c, "ordem 10⁶", X(1_000_000) - 60, y + 210, GREEN, ad, 34)
    ae = ep(t, C["06.e"], 0.5)
    if ae > 0:
        expr(c, "8,5·10^5", 520, 760, 50, ae, cores={0: INK})
        text_mid(c, "expoente escrito: 5   →   resposta: 6", 1080, 760, 34, "black", AMBER, ae)


# ======================================================================
# bloco C — o critério
# ======================================================================

TABELA = [("08.a", "2,3·10^5", "2,3 < 3,16", "10^5", False), ("08.b", "8,5·10^5", "8,5 ≥ 3,16", "10^6", True),
          ("08.c", "1,1·10^{12}", "1,1 < 3,16", "10^{12}", False), ("08.d", "5·10^{-8}", "5 ≥ 3,16", "10^{-7}", True)]


def b_criterio(c, t, C, B):
    head_seq(c, t, C, [("07", "UMA REGRA PARA NÃO DEPENDER DO OLHO", "O CRITÉRIO", PURPLE), ("08", "TESTANDO", "O CRITÉRIO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        expr(c, "a·10^n", W / 2, 280, 110, aa, cores={0: INK})
        text(c, "olhe o COEFICIENTE a", W / 2, 390, 32, "black", BLUE, aa)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            boxed(c, 250, 460, 660, 250, PURPLE, ab, 0.08)
            expr(c, "a < 3,16", 580, 540, 64, ab, cores={1: PURPLE, 2: PURPLE})
            expr(c, "→ 10^n", 580, 640, 64, ab, cores={1: PURPLE})
            text(c, "fica", 820, 645, 28, "black", INK2, ab)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            boxed(c, 1010, 460, 660, 250, GREEN, acc, 0.08)
            expr(c, "a ≥ 3,16", 1340, 540, 64, acc, cores={1: GREEN, 2: GREEN})
            expr(c, "→ 10^{n+1}", 1340, 640, 64, acc, cores={1: GREEN})
            text(c, "sobe um", 1590, 645, 28, "black", INK2, acc)
        return
    a0 = ep(t, C["08"], 0.4)
    for j, h in enumerate(("número", "coeficiente", "ordem")):
        text(c, h.upper(), [450, 960, 1450][j], 230, 24, "black", GRAY, a0, tracking=2)
    for k, (cue, n, cmp_, o, sobe) in enumerate(TABELA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 120 + d
        rrect(c, 220, y - 50, 1480, 100, 18, "#F7F7F5", a)
        expr(c, n, 450, y, 50, a)
        ftext(c, cmp_, 960, y + 14, 38, "black", GREEN if sobe else PURPLE, a)
        expr(c, o, 1450, y, 54, a, cores={0: GREEN if sobe else PURPLE})
        if sobe:
            text(c, "sobe", 1600, y + 10, 24, "black", GREEN, a)
    ae = ep(t, C["08.e"], 0.5)
    if ae > 0:
        rrect(c, 1180, 780, 520, 50, 14, mix("#FFFFFF", GREEN, 0.16), ae)
        ftext(c, "−8 + 1 = −7", 1440, 816, 30, "black", GREEN, ae)


# ======================================================================
# bloco D — por que 3,16: a régua de multiplicar
# ======================================================================

def _arco(c, xa, xb, y, col, a, rotulo, h=90, size=34):
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(xa, y); p.quadTo((xa + xb) / 2, y - h * 2, xb, y)
    c.drawPath(p, paint(col, a, stroke=5, cap_round=True))
    ang = math.atan2(y - (y - h * 2), xb - (xa + xb) / 2)
    pe = paint(col, a, stroke=5, cap_round=True)
    for s_ in (-1, 1):
        c.drawLine(xb, y, xb - 16 * math.cos(ang + s_ * 0.5), y - 16 * math.sin(ang + s_ * 0.5), pe)
    fmid(c, rotulo, (xa + xb) / 2, y - h - 22, size, "black", col, a)


def _regua_log(c, x0, x1, y, a, marcas=True):
    line(c, x0, y, x1, y, INK2, a, 6)
    for v in range(1, 11):
        x = x0 + (x1 - x0) * math.log10(v)
        line(c, x, y - 14, x, y + 14, LIGHT if v not in (1, 10) else INK2, a, 4)
        if marcas:
            text(c, str(v), x, y + 56, 28, "bold", INK2 if v in (1, 10) else GRAY, a)


def b_regua(c, t, C, B):
    head_seq(c, t, C, [("09", "POR QUE 3,16?", "E NÃO 5?", AMBER), ("10", "O MEIO DE VERDADE", "RAIZ DE 10", PURPLE),
                       ("11", "NUM CASO REAL", "400 000", BLUE), ("12", "ATALHO", "SEM FAZER CONTA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10", "11", "12"])
    if sid == "09":
        x0, x1, y = 300, 1620, 560
        a0 = ep(t, C["09"], 0.4)
        X = lambda v: lerp(x0, x1, (v - 1) / 9)
        line(c, x0, y, x1, y, INK2, a0, 6)
        for v in range(1, 11):
            line(c, X(v), y - 14, X(v), y + 14, LIGHT, a0, 4)
            text(c, str(v), X(v), y + 56, 28, "bold", GRAY, a0)
        text(c, "régua de SOMAR: o 5 parece o meio", W / 2, 250, 34, "black", AMBER, a0)
        aa = ep(t, C["09.a"], 0.5)
        pill(c, "entre potências de 10, a gente anda MULTIPLICANDO", W / 2, 320, PURPLE, size=28, a=aa, anchor="center", bounds=(0, 1920))
        _arco(c, X(1), X(5), y - 30, RED, ep(t, C["09.b"], 0.5), "× 5", 70)
        _arco(c, X(5), X(10), y - 30, RED, ep(t, C["09.c"], 0.5), "× 2", 70)
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 740, ad, "PASSOS DIFERENTES: O 5 NÃO É O MEIO", RED, -3, 30)
        return
    if sid == "10":
        x0, x1, y = 300, 1620, 580
        a0 = ep(t, C["10"], 0.4)
        _regua_log(c, x0, x1, y, a0)
        text(c, "régua de MULTIPLICAR", W / 2, 250, 34, "black", PURPLE, a0)
        aa = ep(t, C["10.a"], 0.5)
        xm = (x0 + x1) / 2
        if aa > 0:
            c.drawCircle(xm, y, 18, paint(GREEN, aa))
            expr(c, "√{10} ≈ 3,16", xm, y + 120, 50, aa, cores={0: GREEN, 2: GREEN})
        _arco(c, x0, xm, y - 30, GREEN, ep(t, C["10.b"], 0.5), "× 3,16", 70)
        _arco(c, xm, x1, y - 30, GREEN, ep(t, C["10.c"], 0.5), "× 3,16", 70)
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            rrect(c, 560, 300, 800, 70, 16, "#FFFFFF", ad, shadow=True)
            expr(c, "3,16 × 3,16 ≈ 10", W / 2, 335, 40, ad, cores={4: GREEN})
        return
    if sid == "11":
        x0, x1, y = 300, 1620, 560
        a0 = ep(t, C["11"], 0.4)
        _regua_log(c, x0, x1, y, a0, marcas=False)
        for v, lab in ((1, "100 000"), (10, "1 000 000")):
            x = x0 + (x1 - x0) * math.log10(v)
            text(c, lab, x, y + 60, 28, "black", INK, a0)
        xm = (x0 + x1) / 2
        line(c, xm, y - 24, xm, y + 24, GREEN, a0, 5)
        text(c, "3,16", xm, y + 60, 24, "black", GREEN, a0)
        x4 = x0 + (x1 - x0) * math.log10(4)
        c.drawCircle(x4, y, 18, paint(AMBER, a0))
        text(c, "400 000", x4, y + 100, 30, "black", AMBER, a0)
        aa = ep(t, C["11.a"], 0.5)
        text(c, "em distância: parece mais perto de 100 000", W / 2, 250, 30, "bold", GRAY, aa * (1 - 0.5 * ep(t, C["11.b"], 0.4)))
        _arco(c, x0, x4, y - 30, BLUE, ep(t, C["11.b"], 0.5), "× 4", 70)
        _arco(c, x4, x1, y - 30, GREEN, ep(t, C["11.c"], 0.5), "× 2,5", 60)
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            boxed(c, 470, 700, 980, 110, GREEN, ad, 0.10)
            text(c, "perto na escala = perto EM VEZES", W / 2, 745, 34, "black", GREEN, ad)
            ftext(c, "4 ≥ 3,16  →  ordem 10^6", W / 2, 795, 30, "black", INK, ad)
        return
    # 12 atalho
    x0, x1, y = 300, 1620, 520
    a0 = ep(t, C["12"], 0.4)
    _regua_log(c, x0, x1, y, a0)
    X = lambda v: x0 + (x1 - x0) * math.log10(v)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, X(1), y - 120, X(3) - X(1), 80, 14, PURPLE, 0.14 * aa)
        text_mid(c, "até 3: FICA", (X(1) + X(3)) / 2, y - 80, 30, "black", PURPLE, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        rrect(c, X(4), y - 120, X(10) - X(4), 80, 14, GREEN, 0.14 * ab)
        text_mid(c, "de 4 para cima: SOBE", (X(4) + X(10)) / 2, y - 80, 30, "black", GREEN, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, X(3), y - 120, X(4) - X(3), 80, 14, AMBER, 0.22 * acc)
        text_mid(c, "?", (X(3) + X(4)) / 2, y - 80, 34, "black", AMBER, acc)
        caixa_atalho(c, 410, 640, 1100, 150, "ATALHO", "entre 3 e 4: compare com 3,16 de verdade", acc, 34)


# ======================================================================
# bloco E — diferença de ordens
# ======================================================================

def b_ordens(c, t, C, B):
    frame(c, t, B["start"], "PARA QUE SERVE?", "COMPARAR", BLUE)
    x0, sp, y = 380, 380, 520
    X = lambda e: x0 + (e + 7) * sp
    a0 = ep(t, C["13"], 0.4)
    line(c, X(-7) - 60, y, X(-4) + 60, y, INK2, a0, 5)
    for e in range(-7, -3):
        line(c, X(e), y - 14, X(e), y + 14, INK2, a0, 4)
        expr(c, f"10^{{{e}}}", X(e), y + 70, 40, a0, cores={0: INK2})
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        _icone(c, "cabelo", X(-4), y - 260, 70, aa)
        text(c, "fio de cabelo", X(-4), y - 160, 28, "black", INK, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        _icone(c, "virus", X(-7), y - 260, 70, ab)
        text(c, "vírus", X(-7), y - 160, 28, "black", INK, ab)
    acc = ep(t, C["13.c"], 0.5)
    chip(c, "3 ordens de diferença", W / 2, 250, PURPLE, acc, 30)
    for k in range(3):
        ak = ep(t, C["13.d"] + 0.5 * k, 0.4)
        _arco(c, X(-7 + k) + 20, X(-6 + k) - 20, y - 30, AMBER, ak, "× 10", 45, 30)
    ae = ep(t, C["13.e"], 0.5)
    if ae > 0:
        caixa_atalho(c, 410, 680, 1100, 130, "ATALHO", "cada ordem de diferença = × 10  →  3 ordens ≈ 1 000 vezes", ae, 30)


# ======================================================================
# nós fazemos
# ======================================================================

EXS = [("14.a", "2,9·10^4", "10^4", "2,9 < 3,16: fica"), ("14.b", "3,5·10^4", "10^5", "3,5 ≥ 3,16: sobe"),
       ("14.c", "9,8·10^{-4}", "10^{-3}", "−4 + 1 = −3")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E RESPONDA", GREEN), ("15", "VAMOS CONFERIR", "PAUSE E RESPONDA", GREEN)])
    card(c, *CARD_R)
    for k, (cue, q, r, why) in enumerate(EXS):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 235, 210, 470, 260, 24, "#F7F7F5", a)
        text(c, f"{k + 1}º NÚMERO", x, 255, 22, "black", GRAY, a, tracking=1)
        expr(c, q, x, 360, 64, a)
        if t >= C["15"]:
            ra = ep(t, C["15." + "abc"[k]], 0.5)
            expr(c, r, x, 590, 90, ra, cores={0: GREEN})
            ftext(c, why, x, 710, 28, "bold", INK2, ra)
    pause_timer(c, t, C["14.end"] - 1.9, W / 2, 610)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Ordem de grandeza é a potência de 10 mais próxima.", "Coeficiente a partir de 3,16: sobe uma ordem.",
          "Alternativas em escalas diferentes? Estime."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1340, 58)


ERROS = [("repetir o expoente escrito como ordem de grandeza", "o expoente está ali, prontinho",
          "compare o coeficiente com 3,16: a partir dele, sobe um"),
         ("usar o 5 como ponto de corte", "5 é a metade de 10, e é assim que a gente arredonda",
          "na escala se anda multiplicando: o meio é 3,16"),
         ("fazer a conta exata quando a estimativa já resolvia", "parece mais seguro fazer tudo certinho",
          "custa minutos: alternativas em escalas diferentes? Estime")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["23", "24", "25"], ERROS)


# ======================================================================
# blocos F e G — a conta de guardanapo e quando usar
# ======================================================================

def guardanapo(c, cx, cy, w, h, a, rot=-3):
    """papel de guardanapo com borda ondulada"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    p = skia.Path()
    n = 14
    x0, y0 = -w / 2, -h / 2
    p.moveTo(x0, y0)
    for i in range(n):
        p.quadTo(x0 + w * (i + 0.5) / n, y0 - 10, x0 + w * (i + 1) / n, y0)
    for i in range(n):
        p.quadTo(x0 + w + 10, y0 + h * (i + 0.5) / n, x0 + w, y0 + h * (i + 1) / n)
    for i in range(n):
        p.quadTo(x0 + w - w * (i + 0.5) / n, y0 + h + 10, x0 + w - w * (i + 1) / n, y0 + h)
    for i in range(n):
        p.quadTo(x0 - 10, y0 + h - h * (i + 0.5) / n, x0, y0 + h - h * (i + 1) / n)
    p.close()
    sh = skia.Paint(AntiAlias=True, Color=hexc("#000000", 0.10 * a), MaskFilter=skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.save(); c.translate(0, 10); c.drawPath(p, sh); c.restore()
    c.drawPath(p, paint(GUARD, a))
    c.drawPath(p, paint(GUARD_B, a, stroke=3))
    for k in range(1, 4):
        line(c, x0 + 30, y0 + h * k / 4, x0 + w - 30, y0 + h * k / 4, "#F0E8D2", a, 2)
    c.restore()


def escrita(c, s, x, y, size, a, prog_=1.0, col=None, align="left"):
    """texto 'à mão': revela da esquerda para a direita (prog_ 0..1), em tinta de caneta"""
    if a <= 0 or prog_ <= 0:
        return
    w = K.math_w(s, size)
    xl = x if align == "left" else x - w / 2
    c.save()
    c.clipRect(skia.Rect.MakeLTRB(xl - 10, y - size * 1.4, xl + w * prog_ + 6, y + size * 1.4))
    expr(c, s, x, y, size, a, cores=mono(12, col or CANETA), align=align, peso="bold")
    c.restore()


def b_guardanapo(c, t, C, B):
    head_seq(c, t, C, [("17", "O QUE É ESTIMAR?", "A CONTA DE GUARDANAPO", BLUE), ("18", "NO GUARDANAPO", "ARREDONDE E ACERTE A ESCALA", GREEN),
                       ("19", "E A CONTA EXATA?", "O GUARDANAPO ACERTOU", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["17", "18", "19"])
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        if aa > 0:
            boxed(c, 220, 200, 1480, 110, BLUE, aa, 0.08)
            text(c, "ESTIMAR = conta aproximada, de propósito, só para acertar a escala", W / 2, 268, 34, "black", INK, aa)
        ab = ep(t, C["17.b"], 0.5)
        guardanapo(c, 520, 560, 520, 380, ab)
        escrita(c, "≈ ?", 520, 560, 90, ab, ep(t, C["17.b"] + 0.3, 0.8))
        passos = ["arredonde cada coeficiente para 1 algarismo", "multiplique de cabeça", "some os expoentes"]
        for k, s in enumerate(passos):
            a = ep(t, C["17.c"] + 0.6 * k, 0.4)
            y = 420 + k * 120
            badge_num(c, k + 1, 960, y - 12, a, 28, bg=GREEN)
            text(c, s, 1010, y, 32, "black", INK, a, align="left")
        return
    if sid == "18":
        a0 = ep(t, C["18"], 0.5)
        expr(c, "4,7·10^3 × 8,2·10^5", W / 2, 240, 60, a0)
        guardanapo(c, W / 2, 560, 1100, 500, a0, -2)
        lines = [("18.a", "4,7 → 5", 420), ("18.b", "8,2 → 8", 420), ("18.c", "5 × 8 = 40", 1030), ("18.d", "3 + 5 = 8", 1030)]
        for k, (cue, s, x) in enumerate(lines):
            y = 420 + (k % 2) * 110
            escrita(c, s, x + 100, y, 52, 1.0, ep(t, C[cue], 0.9))
        ae = ep(t, C["18.e"], 0.5)
        escrita(c, "40·10^8 = 4·10^9", W / 2, 680, 64, 1.0, ep(t, C["18.e"], 1.0), align="center")
        if ae > 0:
            text(c, "gangorra", W / 2 + 360, 745, 24, "black", AMBER, ae)
        return
    a0 = ep(t, C["19"], 0.5)
    guardanapo(c, 540, 470, 640, 330, a0, -3)
    escrita(c, "≈ 4·10^9", 540, 470, 80, a0)
    text(c, "guardanapo", 540, 690, 28, "black", CANETA, a0)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        rrect(c, 1060, 330, 620, 280, 24, "#F7F7F5", aa)
        text(c, "conta exata", 1370, 390, 28, "black", PURPLE, aa)
        expr(c, "3,854·10^9", 1370, 500, 76, aa, cores={0: PURPLE})
    ab = ep(t, C["19.b"], 0.5)
    chip(c, "erro: menos de 4%", W / 2, 720, AMBER, ab, 32)
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        check_icon(c, 760, 795, 26, acc, GREEN)
        ftext(c, "a escala certa: 10^9", 1000, 808, 34, "black", GREEN, acc)


QUANDO_E = ["10^6", "10^8", "10^{10}"]
QUANDO_X = ["2,1·10^8", "2,4·10^8", "2,7·10^8"]


def b_quando(c, t, C, B):
    frame(c, t, B["start"], "QUANDO VALE ESTIMAR?", "OLHE AS ALTERNATIVAS", GREEN)
    aa = ep(t, C["20.a"], 0.5)
    if aa > 0:
        caixa_atalho(c, 410, 190, 1100, 120, "ATALHO", "olhe as alternativas ANTES de calcular", aa, 36)
    ab = ep(t, C["20.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 350, 680, 460, 24, "#F7F7F5", ab)
        text(c, "ESCALAS DIFERENTES", 570, 405, 26, "black", GRAY, ab, tracking=1)
        for k, s in enumerate(QUANDO_E):
            expr(c, s, 570, 500 + k * 85, 54, ab * ep(t, C["20.b"] + 0.3 * k, 0.3), cores={0: INK})
        chip(c, "ESTIME", 570, 760, GREEN, ab, 36)
    acc = ep(t, C["20.c"], 0.5)
    if acc > 0:
        rrect(c, 1010, 350, 680, 460, 24, "#F7F7F5", acc)
        text(c, "MESMA POTÊNCIA", 1350, 405, 26, "black", GRAY, acc, tracking=1)
        for k, s in enumerate(QUANDO_X):
            expr(c, s, 1350, 500 + k * 85, 54, acc * ep(t, C["20.c"] + 0.3 * k, 0.3), cores={0: INK})
        chip(c, "CONTA EXATA", 1350, 760, PURPLE, acc, 36)


# ======================================================================
# bloco H — zoom do átomo ao Sol
# ======================================================================

STOPS = [(-10, "atomo", "átomo", "21.a"), (-7, "virus", "vírus", "21.b"), (-5, "celula", "célula", "21.c"),
         (-4, "cabelo", "fio de cabelo", "21.d"), (7, "terra", "raio da Terra", "22.a"), (11, "sol", "Terra → Sol", "22.b")]
ZSP = 190      # pixels por ordem de grandeza


def b_zoom(c, t, C, B):
    head_seq(c, t, C, [("21", "DO MUITO PEQUENO…", "VALORES APROXIMADOS, EM METROS", BLUE),
                       ("22", "…AO MUITO GRANDE", "VALORES APROXIMADOS", BLUE)])
    card(c, *CARD_R)
    # a câmera desliza pela escala: centro em 10^-7 na cena 21; viaja até 10^9 no começo da 22
    u = ease_io(clamp((t - (C["22"] - 0.2)) / 1.6))
    centro = lerp(-7, 9, u)
    y = 430
    a0 = ep(t, C["21"], 0.4)
    xl, xr = CARD_R[0] + 30, CARD_R[0] + CARD_R[2] - 30
    c.save(); c.clipRect(skia.Rect.MakeLTRB(xl, 160, xr, 640))
    X = lambda e: W / 2 + (e - centro) * ZSP
    line(c, xl, y, xr, y, INK2, a0, 5)
    for e in range(-14, 16):
        x = X(e)
        if x < xl - 50 or x > xr + 50:
            continue
        line(c, x, y - 12, x, y + 12, LIGHT, a0, 3)
        expr(c, f"10^{{{e}}}", x, y + 60, 30, a0 * 0.8, cores={0: GRAY})
    for e, kind, nome, cue in STOPS:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = X(e)
        c.drawCircle(x, y, 14, paint(BLUE, a))
        _icone(c, kind, x, y - 150, 62, a)
        text(c, nome, x, y - 60, 26, "black", INK, a)
        rrect(c, x - 70, y + 92, 140, 56, 14, mix("#FFFFFF", BLUE, 0.14), a)
        expr(c, f"10^{{{e}}}", x, y + 120, 36, a, cores={0: BLUE})
    c.restore()
    sid = which(t, C, ["21", "22"])
    if sid == "22":
        aa = ep(t, C["22.a"] + 1.0, 0.5)
        if aa > 0:
            rrect(c, 230, 660, 640, 150, 20, "#F7F7F5", aa)
            ftext(c, "6,4·10^6 m", 550, 720, 38, "black", INK, aa)
            ftext(c, "6,4 ≥ 3,16  →  ordem 10^7", 550, 780, 28, "black", GREEN, aa)
        acc = ep(t, C["22.c"], 0.5)
        if acc > 0:
            rrect(c, 920, 660, 360, 150, 20, "#F7F7F5", acc)
            _icone(c, "mapa", 990, 735, 44, acc)
            text(c, "Brasil", 1150, 710, 26, "black", INK, acc)
            ftext(c, "≈ 2·10^8 → 10^8", 1150, 770, 28, "black", BLUE, acc)
        ad = ep(t, C["22.d"], 0.5)
        if ad > 0:
            rrect(c, 1310, 660, 380, 150, 20, mix("#FFFFFF", GREEN, 0.10), ad)
            _icone(c, "gente", 1370, 740, 50, ad)
            text(c, "mundo", 1540, 705, 26, "black", INK, ad)
            ftext(c, "≈ 8·10^9 → 10^{10}", 1540, 765, 28, "black", GREEN, ad)
            text(c, "8 ≥ 3,16: sobe!", 1540, 800, 22, "bold", INK2, ad)


# ======================================================================
# Questões 5 e 9 do material
# ======================================================================

ALTS5 = [("A", "= 10^4", "nem 10⁵ nem 10⁶", RED), ("B", "= 10^5", "repetiu o expoente escrito", RED), ("C", "= 10^6", "", GREEN),
         ("D", "= 10^7", "nem 10⁵ nem 10⁶", RED), ("E", "= 7·10^5", "nem é potência de 10", RED)]
ENUN5 = "Um estudo estima em 7,2 · 10⁵ o número de árvores de uma reserva florestal. A ordem de grandeza dessa quantidade é"


def b_questao5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ORDEM DE GRANDEZA", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    para(c, ENUN5, 190, 250, 34, "black", INK, a0, 640, 46)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["28.xa"], "B": C["28.xb"], "D": C["28.xd"], "E": C["28.xe"]}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS5, 980, 210, 720, 40, C["27.ok"], "C", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["26.end"] - 1.9, 480, 640)
    if t >= C["27"]:
        ra = ep(t, C["27"], 0.4)
        rrect(c, 170, 470, 700, 330, 18, "#FFFFFF", ra, shadow=True)
        ftext(c, "coeficiente: 7,2", 520, 530, 38, "black", INK, ep(t, C["27.a"], 0.4))
        ftext(c, "7,2 ≥ 3,16 → sobe", 520, 610, 38, "black", GREEN, ep(t, C["27.b"], 0.4))
        ftext(c, "10^5 → 10^6", 520, 690, 42, "black", GREEN, ep(t, C["27.c"], 0.4))
        text(c, "720 000 está perto de 1 000 000", 520, 765, 26, "bold", INK2, ep(t, C["27.d"], 0.4))
    ax = ep(t, C["28.xa"], 0.5)
    if ax > 0:
        rrect(c, 980, 740, 720, 70, 16, mix("#FFFFFF", GREEN, 0.14), ax)
        ftext(c, "ATALHO: expoente escrito ou o seguinte", 1340, 787, 28, "black", GREEN, ax)


ALTS9 = [("A", "= 1,8·10^7", "escala 10⁷ · só 15 L por pessoa", RED), ("B", "= 1,8·10^8", "", GREEN),
         ("C", "= 2,7·10^8", "somou 1,2 + 1,5", RED), ("D", "= 1,8·10^{12}", "escala 10¹² · multiplicou expoentes", RED),
         ("E", "= 8·10^3", "escala 10⁴ · dividiu", RED)]
ENUN9 = ("Uma cidade com 1,2 · 10⁶ habitantes registra consumo médio de 1,5 · 10² litros de água por pessoa por dia. "
         "O consumo diário total da cidade, em litros, é de aproximadamente")


def b_questao9(c, t, C, B):
    head_seq(c, t, C, [("29", "QUESTÃO · ESTIMATIVA EM CONTEXTO", "PAUSE E TENTE", BLUE), ("30", "PRIMEIRO, O GUARDANAPO", "ELIMINE PELA ESCALA", GREEN),
                       ("31", "AGORA A CONTA EXATA", "DECIDE ENTRE AS FINALISTAS", PURPLE)])
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    sid = which(t, C, ["29", "30", "31"])
    ar = ep(t, C["30"], 0.5)
    para(c, ENUN9, 190, 250, 30, "black", INK, a0 * (1 - ar), 700, 40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["30.xa"], "D": C["30.xd"], "E": C["30.xe"], "C": C["31.xc"]}
    if t >= C["29.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS9, 980, 210, 720, 40, C["31.ok"], "B", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["29.end"] - 1.9, 480, 690)
    if sid == "30" or sid == "31":
        guardanapo(c, 520, 480, 660, 480, ar, -2)
        pb, pc = ep(t, C["30.b"], 1.0), ep(t, C["30.c"], 1.0)
        escrita(c, "1,2 → 1", 320, 330, 42, ar, pb)
        escrita(c, "1,5 → 2", 600, 330, 42, ar, ep(t, C["30.b"] + 1.0, 1.0))
        escrita(c, "1 × 2 = 2", 320, 430, 42, ar, pc)
        escrita(c, "6 + 2 = 8", 600, 430, 42, ar, ep(t, C["30.c"] + 1.0, 1.0))
        escrita(c, "≈ 2·10^8", 520, 560, 64, ar, ep(t, C["30.c"] + 2.0, 0.8), align="center")
        ae = ep(t, C["30.e"], 0.5)
        if ae > 0:
            chip(c, "finalistas: B e C", 520, 670, GREEN, ae, 30)
    if sid == "31":
        aa = ep(t, C["31.a"], 0.5)
        if aa > 0:
            rrect(c, 980, 650, 720, 150, 18, "#FFFFFF", aa, shadow=True)
            ftext(c, "1,2 × 1,5 = 1,8", 1340, 710, 40, "black", PURPLE, aa)
            ftext(c, "1,8·10^8 L por dia", 1340, 775, 34, "black", GREEN, ep(t, C["31.b"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

PREFIXOS = [("mega", "10^6"), ("giga", "10^9"), ("nano", "10^{-9}"), ("micro", "10^{-6}")]


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PREFIXOS, ÁREA E VOLUME", PURPLE)
    for k, (nome, p) in enumerate(PREFIXOS):
        a = ep(t, C["33.a"] + 0.35 * k, 0.4)
        x = 400 + k * 373
        rrect(c, x - 160, 220, 320, 220, 24, "#F7F7F5", a)
        text(c, nome, x, 300, 44, "black", INK, a)
        expr(c, "= " + p, x, 380, 48, a, cores={1: PURPLE})
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        gx, gy, gs = 760, 500, 260
        for i in range(11):
            line(c, gx + gs * i / 10, gy, gx + gs * i / 10, gy + gs, LIGHT, ab, 2)
            line(c, gx, gy + gs * i / 10, gx + gs, gy + gs * i / 10, LIGHT, ab, 2)
        c.drawRect(skia.Rect.MakeXYWH(gx, gy, gs, gs), paint(AMBER, ab, stroke=4))
        ftext(c, "1 m^2 = ? cm^2", 1250, 640, 50, "black", AMBER, ab)
    pill(c, "ep. 5 · prefixos e a armadilha de área e volume", W / 2, 810, PURPLE, size=30, a=ep(t, C["33.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Você também usava o 5 como ponto de corte?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, escala=b_escala, definicao=b_definicao, intuicao=b_intuicao,
              criterio=b_criterio, regua=b_regua, ordens=b_ordens, exercicio=b_exercicio, recap=b_recap,
              guardanapo=b_guardanapo, quando=b_quando, zoom=b_zoom, erros=b_erros, questao5=b_questao5,
              questao9=b_questao9, ponte=b_ponte, cta=b_cta)
