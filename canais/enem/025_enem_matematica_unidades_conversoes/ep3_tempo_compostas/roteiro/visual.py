"""Visual — Unidades e conversões, Episódio 3: o tempo não é decimal e a conversão de unidades compostas (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, pause_timer...).
Peças deste episódio: relogio() (setor pintado e marcas de quartos ou décimos), andares() (a fração de dois andares, cada
andar com sua seta de conversão), velocimetro() (mostrador em km/h) e painel() (visor digital em m/s), cronometro(),
torneira(), linha() (texto com cor por trecho, mantém espaços de milhar).
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
_s = importlib.util.spec_from_file_location("comum025", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_unidades_ep3_tempo_compostas.mp4"
CARD_R = K.CARD_R
AGUA = "#4FA3E0"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)]"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def relogio(c, cx, cy, r, minutos, a, col=None, div=4, marcas_a=1.0, num_a=1.0):
    """relógio analógico: setor de 0 até `minutos` pintado, marcas fortes a cada 60/div minutos (4 = quartos, 10 = décimos)"""
    if a <= 0:
        return
    col = col or GREEN
    c.drawCircle(cx, cy, r + 10, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r + 10, paint(INK, a, stroke=8))
    if minutos > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, min(minutos, 59.99) / 60 * 360, False); p.close()
        c.drawPath(p, paint(col, a * 0.28))
    for k in range(60):
        ang = -math.pi / 2 + k * math.pi / 30
        big = k % 5 == 0
        r0 = r - (22 if big else 10)
        c.drawLine(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang), cx + r * math.cos(ang), cy + r * math.sin(ang),
                   paint(INK if big else INK2, a * (0.8 if big else 0.4), stroke=4 if big else 2))
    passo = 60 / div
    for j in range(div):
        m = j * passo
        ang = -math.pi / 2 + m / 60 * 2 * math.pi
        c.drawLine(cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), paint(PURPLE, a * marcas_a * 0.35, stroke=3))
        if num_a > 0:
            lab = f"{m:g}"
            text_mid(c, lab, cx + (r + 46) * math.cos(ang), cy + (r + 46) * math.sin(ang), 28, "black", PURPLE, a * num_a)
    ang = -math.pi / 2 + minutos / 60 * 2 * math.pi
    c.drawLine(cx, cy, cx + (r - 26) * math.cos(ang), cy + (r - 26) * math.sin(ang), paint(col, a, stroke=9, cap_round=True))
    c.drawCircle(cx, cy, 11, paint(INK, a))


def andares(c, cx, cy, cima, baixo, a, size=72, col=None, w=None):
    """fração de dois andares com texto (unidades): cima / baixo, traço roxo no meio"""
    if a <= 0:
        return
    col = col or INK
    w = w or max(text_w(cima, "black", size), text_w(baixo, "black", size)) + 60
    text_mid(c, cima, cx, cy - size * 0.62, size, "black", col, a)
    line(c, cx - w / 2, cy, cx + w / 2, cy, PURPLE, a, 6)
    text_mid(c, baixo, cx, cy + size * 0.62, size, "black", col, a)
    return w


def seta_andar(c, x0, x1, y, rot, col, a):
    """seta horizontal com o rótulo da conversão de um andar"""
    if a <= 0:
        return
    arrow(c, x0, y, x1, y, col, a, 6, 18, progress=a)
    text(c, rot, (x0 + x1) / 2, y - 18, 32, "black", col, a)


def velocimetro(c, cx, cy, r, val, vmax, a, unidade="km/h"):
    """mostrador de velocímetro (meia-lua) com ponteiro em `val`"""
    if a <= 0:
        return
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 180, 180)
    c.drawPath(p, paint(INK, a, stroke=14))
    for k in range(0, 11):
        ang = math.pi + k / 10 * math.pi
        r0 = r - 30
        c.drawLine(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang), cx + (r - 8) * math.cos(ang),
                   cy + (r - 8) * math.sin(ang), paint(INK2, a, stroke=4))
    ang = math.pi + clamp(val / vmax) * math.pi
    c.drawLine(cx, cy, cx + (r - 40) * math.cos(ang), cy + (r - 40) * math.sin(ang), paint(RED, a, stroke=8, cap_round=True))
    c.drawCircle(cx, cy, 14, paint(INK, a))
    fmid(c, f"{val:g}".replace(".", ","), cx, cy + 70, 80, "black", INK, a)
    text(c, unidade, cx, cy + 150, 34, "black", INK2, a)


def painel(c, cx, cy, val, a, unidade="m/s", col=None):
    """visor digital retangular (placa de atletismo)"""
    if a <= 0:
        return
    col = col or GREEN
    rrect(c, cx - 190, cy - 110, 380, 220, 26, "#1F2430", a, shadow=True)
    fmid(c, val, cx, cy - 10, 96, "black", col, a)
    text(c, unidade, cx, cy + 80, 34, "black", "#C9CED8", a)


def cronometro(c, cx, cy, s, a):
    """cronômetro com visor"""
    if a <= 0:
        return
    rrect(c, cx - 20, cy - 175, 40, 40, 8, INK, a)
    c.drawCircle(cx, cy, 150, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, 150, paint(INK, a, stroke=10))
    rrect(c, cx - 115, cy - 45, 230, 90, 16, "#1F2430", a)
    fmid(c, s, cx, cy, 56, "black", AMBER, a)


def torneira(c, cx, cy, a, fluxo=1.0):
    """torneira com filete de água"""
    if a <= 0:
        return
    rrect(c, cx - 150, cy - 40, 170, 50, 14, "#9AA3AE", a)
    rrect(c, cx + 10, cy - 40, 50, 110, 14, "#9AA3AE", a)
    rrect(c, cx - 110, cy - 80, 40, 40, 8, "#7D8792", a)
    if fluxo > 0:
        rrect(c, cx + 22, cy + 70, 26, 150 * fluxo, 10, AGUA, a * 0.8)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "UNIDADES E CONVERSÕES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    cronometro(c, 470, 470, "3,25 h", aa)
    ab = ep(t, C["01.b"], 0.5)
    if aa > 0:
        linha(c, [("3 h 25 min?", RED)], 470, 720, 44, aa * (1 - ab))
        if ab > 0:
            linha(c, [("3 h ", INK), ("15 min", GREEN)], 470, 720, 52, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        text(c, "72 km/h", 1380, 330, 70, "black", INK, acc)
        arrow(c, 1380, 370, 1380, 450, PURPLE, acc, 6, 18, progress=acc)
        linha(c, [("20 m/s", GREEN)], 1380, 520, 80, acc)
        linha(c, [("259?", RED)], 1380, 640, 52, acc)
        strike(c, 1320, 640, 1440, 640, acc, RED, acc)
    line(c, 960, 240, 960, 780, "#E6E6E2", acc, 3)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 820, ad, "HOJE VOCÊ PARA DE ERRAR AS DUAS", PURPLE, -2, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "converter tempo sem errar", "horas quebradas em horas e minutos"),
            ("02.b", "passar velocidade, densidade e vazão", "de uma unidade para outra")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 52, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EPISÓDIOS 1, 2 E A SÉRIE DE GRANDEZAS", GREEN)
    rows = [("03.a", "a escada: cada degrau vale 10", "1 km = 1 000 m", BLUE),
            ("03.b", "o volume", "1 m³ = 1 000 L", BLUE),
            ("03.c", "o décimo de hora", "0,4 h = 24 min (não 40)", AMBER)]
    for j, (cue, s, r, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 160 + d
        badge_num(c, j + 1, 300, y - 14, a, 30, bg=col)
        text(c, s, 360, y, 42, "black", INK, a, align="left")
        text(c, r, 1180, y, 46, "black", GREEN, a, align="left")


def b_cotidiano(c, t, C, B):
    head(c, t, B["start"], "TRÊS CENAS DO DIA A DIA", "CADA NÚMERO TEM SUA UNIDADE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    cronometro(c, 430, 440, "3,25 h", aa)
    text(c, "quanto é no relógio?", 430, 680, 32, "black", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        velocimetro(c, 960, 470, 170, 72, 160, ab)
        text(c, "km/h  ou  m/s?", 960, 680, 32, "black", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        torneira(c, 1450, 360, acc, ep(t, C["04.c"] + 0.4, 1.0))
        text(c, "litros por minuto", 1490, 680, 32, "black", INK2, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "o número só faz sentido na unidade certa", W / 2, 780, ad, 32)


# ======================================================================
# blocos a, b, c — o tempo
# ======================================================================

def b_sexagesimal(c, t, C, B):
    head(c, t, B["start"], "O TEMPO", "NÃO É DECIMAL", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "km · hm · dam · m · dm · cm · mm", 560, 300, 36, "black", INK2, aa)
        text(c, "de 10 em 10", 560, 360, 40, "black", BLUE, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        boxed(c, 240, 430, 640, 150, AMBER, ab, 0.08)
        text(c, "SEXAGESIMAL", 560, 495, 50, "black", AMBER, ab)
        text(c, "= conta de 60 em 60", 560, 548, 32, "bold", INK2, ab)
    acc = ep(t, C["05.c"], 0.5)
    relogio(c, 1380, 450, 190, 60 * ep(t, C["05.c"], 2.0) if acc > 0 else 0, acc, BLUE, 4)
    if acc > 0:
        text(c, "1 h = 60 min", 1100, 720, 38, "black", INK, acc, align="left")
        text(c, "1 min = 60 s", 1100, 770, 38, "black", INK, ep(t, C["05.c"] + 1.6, 0.4), align="left")
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        linha(c, [("1 h = 60 × 60 = ", INK), ("3 600 s", GREEN)], 560, 690, 44, ad)


def b_decimo(c, t, C, B):
    head_seq(c, t, C, [("06", "HORA QUEBRADA", "2,4 h", PURPLE), ("07", "HORA QUEBRADA", "2,5 h", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        a0 = ep(t, C["06"], 0.5)
        fmid(c, "2,4 h", 520, 330, 110, "black", INK, a0)
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            linha(c, [("2", GREEN), (" h", INK2)], 380, 520, 60, aa)
            text(c, "parte inteira", 380, 600, 28, "bold", GRAY, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            linha(c, [("0,4 × 60 = ", INK), ("24", GREEN), (" min", INK2)], 700, 520, 54, ab)
            text(c, "parte decimal × 60", 700, 600, 28, "bold", GRAY, ab)
        relogio(c, 1420, 470, 180, 24 * ep(t, C["06.b"] + 1.0, 1.2) if ab > 0 else 0, a0, GREEN, 4)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            linha(c, [("2 h 24 min", GREEN)], 560, 720, 56, acc)
            linha(c, [("2 h 40 min", RED)], 1420, 760, 40, acc)
            strike(c, 1320, 760, 1520, 760, acc, RED, acc)
        return
    a0 = ep(t, C["07"], 0.5)
    fmid(c, "2,5 h", 520, 330, 110, "black", INK, a0)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        linha(c, [("0,5 × 60 = ", INK), ("30", GREEN), (" min", INK2)], 560, 520, 54, aa)
        linha(c, [("2 h 30 min", GREEN)], 560, 640, 56, ep(t, C["07.a"] + 1.8, 0.4))
    relogio(c, 1420, 470, 180, 30 * ep(t, C["07.a"] + 0.6, 1.2) if aa > 0 else 0, a0, GREEN, 4)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        regra(c, "meia hora é metade de 60, não de 100", 560, 770, ab, 32)


def b_relogio(c, t, C, B):
    head_seq(c, t, C, [("08", "FRAÇÕES DE HORA", "O RELÓGIO EM QUARTOS", BLUE),
                       ("09", "FRAÇÕES DE HORA", "O RELÓGIO EM DÉCIMOS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        rows = [("08.b", "0,25 h", "15 min", 15), ("08.c", "0,5 h", "30 min", 30), ("08.d", "0,75 h", "45 min", 45)]
        m = 0
        for k, (cue, h, mi, mm) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            if a > 0:
                m = mm
            y = 330 + k * 150
            text(c, h, 1150, y, 56, "black", INK, a, align="left")
            text(c, "=", 1390, y, 56, "black", GRAY, a)
            text(c, mi, 1450, y, 56, "black", GREEN, a, align="left")
        relogio(c, 600, 500, 230, m, ep(t, C["08.a"], 0.5), GREEN, 4)
        return
    rows = [("09.a", "0,1 h", "6 min", 6), ("09.b", "0,2 h", "12 min", 12), ("09.c", "0,8 h", "48 min", 48)]
    m = 0
    for k, (cue, h, mi, mm) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a > 0:
            m = mm
        y = 300 + k * 120
        text(c, h, 1150, y, 52, "black", INK, a, align="left")
        text(c, "=", 1390, y, 52, "black", GRAY, a)
        text(c, mi, 1450, y, 52, "black", GREEN, a, align="left")
    relogio(c, 600, 480, 220, m, ep(t, C["09"], 0.5), GREEN, 10)
    ad = ep(t, C["09.d"], 0.5)
    K.atalho(c, 1060, 640, 640, 150, "ATALHO", ["1 décimo de hora = 6 min", "1 quarto de hora = 15 min (não 25)"], ad, 30)


# ======================================================================
# bloco d — unidade composta
# ======================================================================

def b_composta(c, t, C, B):
    head_seq(c, t, C, [("10", "UNIDADE COMPOSTA", "UMA FRAÇÃO DE DOIS ANDARES", BLUE),
                       ("11", "COMO CONVERTER", "CADA ANDAR NA SUA ESCADA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "km/h", 480, 360, 110, "black", INK, aa)
            text(c, "distância  ÷  tempo", 480, 450, 34, "bold", INK2, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            boxed(c, 200, 540, 560, 110, BLUE, ab, 0.08)
            text(c, "UNIDADE COMPOSTA", 480, 590, 40, "black", BLUE, ab)
            text(c, "duas unidades juntas", 480, 632, 26, "bold", INK2, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            andares(c, 1360, 460, "km", "h", acc, 110)
            text(c, "NUMERADOR (em cima)", 1360, 300, 30, "black", PURPLE, acc)
            text(c, "DENOMINADOR (embaixo)", 1360, 650, 30, "black", PURPLE, ep(t, C["10.c"] + 2.0, 0.4))
        return
    a0 = ep(t, C["11"], 0.5)
    andares(c, 520, 470, "km", "h", a0, 110)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        text(c, "cada andar desce a sua escada", W / 2, 260, 34, "black", INK2, aa)
    ab = ep(t, C["11.b"], 0.5)
    seta_andar(c, 640, 1100, 400, "× 1 000", BLUE, ab)
    if ab > 0:
        text(c, "m", 1200, 425, 80, "black", BLUE, ab)
    acc = ep(t, C["11.c"], 0.5)
    seta_andar(c, 640, 1100, 560, "× 3 600", AMBER, acc)
    if acc > 0:
        text(c, "s", 1200, 585, 80, "black", AMBER, acc)
    if acc > 0:
        line(c, 1150, 480, 1260, 480, PURPLE, acc, 6)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        regra(c, "converta os DOIS andares", 1400, 720, ad, 34)


# ======================================================================
# bloco e — km/h e m/s
# ======================================================================

def b_velocidade(c, t, C, B):
    head_seq(c, t, C, [("12", "DE ONDE VEM", "O 3,6", PURPLE), ("13", "km/h E m/s", "DIVIDE OU MULTIPLICA", PURPLE),
                       ("14", "ATALHO", "OLHE O TAMANHO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            linha(c, [("1 km/h  =  ", INK), ("1 000 m", BLUE), ("  em  ", INK2), ("3 600 s", AMBER)], W / 2, 320, 56, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            expr(c, "1000/3600 = 1/3,6", W / 2, 490, 88, ab, cores={0: BLUE, 2: GREEN})
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            boxed(c, 460, 640, 1000, 120, PURPLE, acc, 0.08)
            text(c, "km/h  →  m/s:   ÷ 3,6", W / 2, 718, 52, "black", PURPLE, acc)
        return
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            velocimetro(c, 470, 470, 170, 90, 160, aa)
            arrow(c, 700, 470, 880, 470, PURPLE, aa, 6, 18, progress=ep(t, C["13.a"] + 1.0, 0.6))
            text(c, "÷ 3,6", 790, 440, 34, "black", PURPLE, ep(t, C["13.a"] + 1.0, 0.4))
            painel(c, 1100, 470, "25", ep(t, C["13.a"] + 2.4, 0.5))
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            boxed(c, 1340, 300, 380, 110, PURPLE, ab, 0.08)
            text(c, "m/s → km/h:  × 3,6", 1530, 368, 34, "black", PURPLE, ab)
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            linha(c, [("5 m/s × 3,6 = ", INK), ("18 km/h", GREEN)], 1530, 560, 36, acc)
            text(c, "um corredor", 1530, 620, 28, "bold", GRAY, acc)
        return
    a0 = ep(t, C["14"], 0.5)
    velocimetro(c, 470, 470, 170, 72, 160, a0)
    painel(c, 1050, 470, "20", a0)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        text(c, "1 m/s = uma caminhada apressada", 760, 720, 32, "black", INK2, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        selo(c, 1050, 270, ab, "O MENOR", GREEN, -4, 32)
    acc = ep(t, C["14.c"], 0.5)
    K.atalho(c, 1290, 360, 430, 280, "ATALHO", ["÷ 3,6 → diminui", "× 3,6 → aumenta", "m/s é sempre", "o número menor"],
             acc, 30)


# ======================================================================
# blocos f, g — densidade e vazão
# ======================================================================

def b_densidade(c, t, C, B):
    head(c, t, B["start"], "DENSIDADE", "SÓ A TROCA DE UNIDADE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        pill(c, "hoje: só converter", W / 2, 250, GRAY, size=28, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        andares(c, 520, 460, "g", "cm³", ab, 96)
        text(c, "dois andares de novo", 520, 640, 30, "bold", GRAY, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        arrow(c, 720, 460, 960, 460, PURPLE, acc, 6, 18, progress=acc)
        text(c, "× 1 000", 840, 425, 38, "black", PURPLE, acc)
        andares(c, 1160, 460, "kg", "m³", acc, 96)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        linha(c, [("alumínio: 2,7 g/cm³  →  ", INK), ("2 700 kg/m³", GREEN)], W / 2, 720, 44, ad)
        pill(c, "o porquê: próximo episódio", 1500, 290, AMBER, size=24, a=ep(t, C["15.d"] + 2.5, 0.4), anchor="center",
             bounds=(0, 1920))


def b_vazao(c, t, C, B):
    head_seq(c, t, C, [("16", "VAZÃO", "L/min → m³/h", BLUE), ("17", "O CAMINHO SEGURO", "UM ANDAR DE CADA VEZ", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17"])
    torneira(c, 380, 380, ep(t, C["16"], 0.5), 1.0)
    if sid == "16":
        aa = ep(t, C["16.a"], 0.5)
        if aa > 0:
            boxed(c, 700, 290, 920, 120, PURPLE, aa, 0.08)
            text(c, "L/min  →  m³/h:   × 0,06", 1160, 368, 48, "black", PURPLE, aa)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            linha(c, [("50 L/min × 0,06 = ", INK), ("3 m³/h", GREEN)], 1160, 560, 52, ab)
        return
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        text(c, "1º  o tempo:  1 h = 60 min", 700, 310, 40, "black", AMBER, aa, align="left")
        linha(c, [("50 × 60 = ", INK), ("3 000 L/h", GREEN)], 1160, 400, 48, ep(t, C["17.a"] + 2.0, 0.4))
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        text(c, "2º  os litros:  1 000 L = 1 m³", 700, 520, 40, "black", BLUE, ab, align="left")
        linha(c, [("3 000 L = ", INK), ("3 m³", GREEN)], 1160, 610, 48, ep(t, C["17.b"] + 2.0, 0.4))
    acc = ep(t, C["17.c"], 0.5)
    K.atalho(c, 700, 680, 920, 120, "ATALHO", ["na dúvida, padronize o tempo primeiro"], acc, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E CONVERTA", GREEN), ("19", "VAMOS CONFERIR", "PAUSE E CONVERTA", GREEN)])
    card(c, *CARD_R)
    contas = [("18.a", "1,75 h", "19.a", "1 h 45 min"), ("18.b", "36 km/h", "19.b", "10 m/s"),
              ("18.c", "15 m/s", "19.c", "54 km/h")]
    for k, (cue, s, cr, r) in enumerate(contas):
        y = 310 + k * 150
        a = ep(t, C[cue], 0.5)
        rrect(c, 300, y - 65, 1320, 130, 22, "#F7F7F5", a)
        text(c, s, 560, y + 18, 60, "black", INK, a)
        text(c, "=", 900, y + 18, 60, "black", GRAY, a)
        if t >= C["19"]:
            text(c, r, 1240, y + 20, 60, "black", GREEN, ep(t, C[cr], 0.4))
        else:
            text(c, "?", 1240, y + 20, 60, "black", AMBER, a)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 790)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["O relógio conta de 60 em 60.", "Unidade composta: converta os dois andares.",
          "Em m/s, o número é sempre o menor."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Ler 2,4 h como 2 h 40 min", "o número depois da vírgula parece ser os minutos",
          "o relógio conta de 60 em 60: 0,4 × 60 = 24 min"),
         ("Multiplicar por 3,6 para ir de km/h para m/s", "o metro é menor que o km, e o número cresce",
          "o segundo também é menor que a hora: divida. Em m/s, o número é o menor"),
         ("Converter só o andar de cima de uma unidade composta", "o km virou metro e a conta deu um número",
          "o andar de baixo continua em horas: converta os DOIS"),
         ("Parar nos litros quando a questão pede m³", "a conta está pronta e o número está nas alternativas",
          "releia a unidade pedida: 1 000 L = 1 m³, divida por mil")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23", "24"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=32, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _rodape(c, a):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a, align="left")


ALTS3 = [("A", "3 h 15 min", "", GREEN), ("B", "3 h 25 min", "leu o 25 como minutos", RED),
         ("C", "3 h 40 min", "0,25 h < meia hora", RED), ("D", "3 h 45 min", "trocou ¼ por ¾", RED),
         ("E", "3 h 50 min", "0,25 h < meia hora", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "EU FAÇO COM VOCÊ", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    _enunciado(c, [("Um percurso foi cronometrado em 3,25 horas.", INK), ("Esse tempo corresponde a", BLUE)], a0, 250)
    _rodape(c, a0)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "BCDE"}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 44, C["26.ok"], "A", cues_in, cues_x, gap=34)
    if t >= C["26"]:
        ra = ep(t, C["26"], 0.4)
        rrect(c, 170, 440, 740, 360, 18, "#FFFFFF", ra, shadow=True)
        linha(c, [("3", GREEN), (" h  +  0,25 h", INK)], 540, 490, 44, ra)
        aa = ep(t, C["26.a"], 0.4)
        if aa > 0:
            linha(c, [("0,25 × 60 = ", INK), ("15 min", GREEN)], 540, 570, 44, aa)
            relogio(c, 540, 690, 64, 15, aa, GREEN, 4, num_a=0)


ALTS4 = [("A", "2 m/s", "dividiu por 36", RED), ("B", "20 m/s", "", GREEN), ("C", "200 m/s", "dividiu por 0,36", RED),
         ("D", "259,2 m/s", "multiplicou por 3,6", RED), ("E", "20 000 m/s", "converteu só o km", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "NÓS FAZEMOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    _enunciado(c, [("Um veículo trafega a 72 km/h em uma rodovia.", INK),
                   ("Essa velocidade, expressa em metros por segundo, é de", BLUE)], a0, 250)
    _rodape(c, a0)
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ACDE"}
    if t >= C["27.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS4, 1000, 250, 680, 44, C["28.ok"], "B", cues_in, cues_x, gap=34)
    ap = ep(t, C["27.p"], 0.4) * (1 - ep(t, C["28"], 0.3))
    if ap > 0:
        text(c, "divide ou multiplica?", 540, 600, 40, "black", AMBER, ap)
    if t >= C["28"]:
        ra = ep(t, C["28"], 0.4)
        rrect(c, 170, 470, 740, 330, 18, "#FFFFFF", ra, shadow=True)
        text(c, "m/s: o número tem que DIMINUIR", 540, 530, 30, "black", PURPLE, ra)
        linha(c, [("72 ÷ 3,6 = ", INK), ("20", GREEN)], 540, 630, 64, ep(t, C["28.a"], 0.4))
        conferido(c, "menor que 72", 420, 730, ep(t, C["28.a"] + 1.5, 0.4), True, 30)


ALTS6 = [("A", "0,18 m³", "vírgula no lugar errado", RED), ("B", "1,8 m³", "", GREEN),
         ("C", "18 m³", "vírgula no lugar errado", RED), ("D", "180 m³", "vírgula no lugar errado", RED),
         ("E", "1 800 m³", "parou nos litros", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "VOCÊ FAZ", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    _enunciado(c, [("Uma torneira despeja água a uma vazão constante de 15 litros por minuto. Deixada aberta por 2 horas, "
                    "ela terá despejado um volume de", INK)], a0, 250)
    _rodape(c, a0)
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ACDE"}
    if t >= C["29.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS6, 1000, 250, 680, 44, C["30.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["29.end"] - 1.9, 540, 660)
    sid = which(t, C, ["29", "30", "31"])
    if sid == "30":
        ra = ep(t, C["30"], 0.4)
        rrect(c, 170, 440, 740, 370, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["30.a"], 0.4)
        if aa > 0:
            linha(c, [("1º  2 h = ", AMBER), ("120 min", GREEN)], 540, 490, 38, aa)
        ab = ep(t, C["30.b"], 0.4)
        if ab > 0:
            linha(c, [("15 × 120 = ", INK), ("1 800 L", GREEN)], 540, 570, 40, ab)
        acc = ep(t, C["30.c"], 0.4)
        if acc > 0:
            linha(c, [("2º  1 800 ÷ 1 000 = ", BLUE), ("1,8 m³", GREEN)], 540, 650, 40, acc)
        ad = ep(t, C["30.d"], 0.4)
        if ad > 0:
            linha(c, [("atalho: 15 × 0,06 = 0,9 m³/h  ·  × 2 = ", INK2), ("1,8", GREEN)], 540, 740, 26, ad)
    elif sid == "31":
        ra = ep(t, C["31"], 0.4)
        rrect(c, 170, 470, 740, 330, 18, "#FFFFFF", ra, shadow=True)
        ae = ep(t, C["31.xe"], 0.4)
        if ae > 0:
            text(c, "1 800 m³: quase uma piscina olímpica", 540, 540, 28, "black", RED, ae)
            text(c, "(uma olímpica tem cerca de 2 500 m³)", 540, 585, 24, "bold", GRAY, ae)
        ax = ep(t, C["31.xa"], 0.4)
        if ax > 0:
            text(c, "0,18 · 1,8 · 18 · 180", 540, 670, 40, "black", INK, ax)
            text(c, "o mesmo 18, com a vírgula em outro lugar", 540, 725, 26, "bold", AMBER, ax)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ANÁLISE DIMENSIONAL", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    if aa > 0:
        for k, s in enumerate(("3,6 ?", "1 000 ?")):
            chip(c, s, 760 + k * 420, 330, AMBER, aa * ep(t, C["33.a"] + 0.5 * k, 0.4), 48)
        text(c, "esqueceu o fator?", W / 2, 450, 38, "black", INK2, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        boxed(c, 560, 520, 800, 140, GREEN, ab, 0.08)
        text(c, "um método que nunca falha", W / 2, 584, 42, "black", GREEN, ab)
        text(c, "e se confere sozinho", W / 2, 632, 30, "bold", GREEN, ab)
    pill(c, "ep. 4 · análise dimensional", W / 2, 750, PURPLE, size=32, a=ep(t, C["33.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Quanto deu 1,75 h para você?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, sexagesimal=b_sexagesimal,
              decimo=b_decimo, relogio=b_relogio, composta=b_composta, velocidade=b_velocidade, densidade=b_densidade,
              vazao=b_vazao, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q3=b_q3, q4=b_q4, q6=b_q6,
              ponte=b_ponte, cta=b_cta)
