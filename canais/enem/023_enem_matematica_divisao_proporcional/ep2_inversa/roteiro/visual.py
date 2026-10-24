"""Visual — Divisão Proporcional, Episódio 2: divisão inversa, inverter o valor, não a ordem (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: flip() (o número virando de cabeça para baixo e virando 1/n), caixa() (os números da fila),
pacote() e linha() (os pacotinhos do episódio 1 e textos com milhar), pessoa() (os funcionários do bônus).
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
_s = importlib.util.spec_from_file_location("comum023", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisao_ep2_inversa.mp4"
CARD_R = K.CARD_R
CAIXA = "#C98B4B"
PESSOAS = [("Ana", "2 faltas", BLUE), ("Bruno", "3 faltas", PURPLE), ("Caio", "4 faltas", AMBER)]


# ======================================================================
# peças do episódio
# ======================================================================

def caixa(c, s, cx, cy, col, a, size=56, w=120, h=110, fill=None):
    """um número da fila, numa caixinha com borda colorida"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 18, fill or "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18), paint(col, a, stroke=5))
    fmid(c, s, cx, cy, size, "black", col, a)


def flip(c, n, cx, cy, size, u, a, col_n=None, col_f=None):
    """o número n gira de cabeça para baixo (u = 0..1) e reaparece como a fração 1/n"""
    if a <= 0:
        return
    u = clamp(u)
    sy = math.cos(math.pi * u)
    c.save(); c.translate(cx, cy); c.scale(1, max(abs(sy), 0.02)); c.translate(-cx, -cy)
    if u < 0.5:
        fmid(c, str(n), cx, cy, size, "black", col_n or INK, a)
    else:
        expr(c, f"1/{n}", cx, cy, size * 0.75, a, cores={0: col_f or GREEN})
    c.restore()


def pacote(c, x, y, s, col, a, abre=0.0, valor=None, vsize=30):
    """pacotinho fechado (laço) centrado em (x, y); abre = 0..1 levanta a tampa e mostra o valor"""
    if a <= 0:
        return
    sc = 0.85 + 0.15 * ease_back(clamp(a))
    w, h = s * sc, s * 0.8 * sc
    rrect(c, x - w / 2, y - h / 2, w, h, 10, col, a, shadow=True)
    lid = h * 0.28
    dy = -abre * s * 0.45
    rrect(c, x - w / 2 - 6, y - h / 2 - lid * 0.5 + dy, w + 12, lid, 8, mix(col, "#000000", 0.12), a)
    line(c, x, y - h / 2 + 8, x, y + h / 2, "#FFFFFF", a * 0.85, 6)
    line(c, x, y - h / 2 - lid * 0.5 + dy, x, y - h / 2 + lid * 0.5 + dy, "#FFFFFF", a * 0.85, 6)
    if abre > 0 and valor:
        text_mid(c, valor, x, y - h / 2 - s * 0.1 + dy * 0.2, vsize, "black", GREEN, a * clamp(abre * 1.6))


def pacotes(c, t, x0, y, n, a, ins=None, abre=0.0, valor=None, col=CAIXA, s=66, gap=80):
    for i in range(n):
        ai = a * (ep(t, ins + 0.15 * i, 0.35) if ins is not None else 1.0)
        pacote(c, x0 + i * gap, y, s, col, ai, abre, valor)


def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)] (mantém os espaços dos milhares)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def pessoa(c, cx, cy, s, col, a):
    """bonequinho simples: cabeça e tronco (cy = centro do tronco)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - s * 0.62, s * 0.26, paint(col, a))
    p = skia.Path(); p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.4, cy - s * 0.3, s * 0.8, s * 0.7), s * 0.3, s * 0.3))
    c.drawPath(p, paint(col, a))


def conferido(c, s, x, y, a, ok=True, size=32):
    """linha de conferência com ✓ (verde) ou ✗ (vermelho)"""
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DIVISÃO INVERSA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        text(c, "dividir INVERSAMENTE a", W / 2, 270, 44, "black", INK, aa)
        for k, n in enumerate((2, 3, 4)):
            caixa(c, str(n), 800 + k * 160, 380, BLUE, aa * ep(t, C["01.a"] + 0.2 * k, 0.4))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        # a fila virada: 4, 3, 2 em vermelho
        text(c, "pesos usados por muita gente:", W / 2, 520, 32, "bold", INK2, ab)
        for k, n in enumerate((4, 3, 2)):
            caixa(c, str(n), 800 + k * 160, 610, RED, ab * ep(t, C["01.b"] + 0.2 * k, 0.4), fill="#FDECEC")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        check_icon(c, 1330, 610, 44, acc, RED, "x")
        selo(c, 1520, 610, acc, "ERRADO", RED, -6, 40)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        ftext(c, "≈ 1 155,56   ·   866,67   ·   577,78", W / 2, 750, 44, "black", RED, ad)
    ae = ep(t, C["01.e"], 0.5)
    selo(c, W / 2, 860, ae, "NÚMERO QUEBRADO = SINAL DO ERRO", AMBER, -2, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "fazer qualquer divisão inversa SEM frações", "o atalho do MMC"),
            ("02.b", "não cair na armadilha da ordem invertida", "inverter o valor, não a ordem")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "EPISÓDIO 1", 420, 250, GRAY, size=22, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "PACOTINHOS", 420, 330, 40, "black", PURPLE, aa)
        pacotes(c, t, 340, 450, 3, aa, C["03.a"] + 0.3)
        text(c, "some · divida · multiplique", 420, 580, 30, "black", INK2, aa)
        text(c, "cada pacotinho vale k", 420, 640, 30, "black", GREEN, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "SÉRIE DE FRAÇÕES", 960, 250, GRAY, size=22, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "INVERSO", 960, 330, 40, "black", BLUE, ab)
        flip(c, 2, 960, 470, 130, ep(t, C["03.b"] + 1.2, 0.9), ab)
        text(c, "de cabeça para baixo", 960, 640, 30, "black", INK2, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        pill(c, "SÉRIE DE DIVISIBILIDADE", 1500, 250, GRAY, size=22, a=acc, anchor="center", bounds=(0, 1920))
        text(c, "MMC", 1500, 330, 40, "black", PURPLE, acc)
        text(c, "o menor que todos", 1500, 420, 30, "black", INK2, acc)
        text(c, "dividem certinho", 1500, 465, 30, "black", INK2, acc)
        ftext(c, "MMC(2, 3, 4) = 12", 1500, 580, 46, "black", GREEN, acc)
    line(c, 690, 230, 690, 800, "#E6E6E2", aa, 3)
    line(c, 1230, 230, 1230, 800, "#E6E6E2", ab, 3)


# ======================================================================
# concreto — menos é mais
# ======================================================================

def b_menos(c, t, C, B):
    head_seq(c, t, C, [("04", "O BÔNUS DE FIM DE ANO", "MENOS É MAIS", BLUE),
                       ("05", "DEFINIÇÃO", "INVERSAMENTE PROPORCIONAL", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        for k, (nome, falt, col) in enumerate(PESSOAS):
            a = ep(t, C["04.a"] + 0.4 * k, 0.5)
            x = 420 + k * 360
            destaque = ep(t, C["04.c"], 0.5) if k == 0 else 0
            if destaque > 0:
                rrect(c, x - 150, 200, 300, 450, 26, GREEN, 0.12 * destaque)
            pessoa(c, x, 400, 150, col, a)
            text(c, nome, x, 530, 40, "black", INK, a)
            text(c, falt, x, 590, 34, "black", col, a)
            if destaque > 0:
                pill(c, "MERECE MAIS", x, 232, GREEN, size=24, a=destaque, anchor="center", bounds=(0, 1920))
        ab = ep(t, C["04.b"], 0.5) * (1 - ep(t, C["04.c"], 0.4))
        fmid(c, "?", 1500, 400, 160, "black", AMBER, ab)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            regra(c, "MENOR número  →  MAIOR parte", 760, 720, ad, 38)
        ae = ep(t, C["04.e"], 0.5)
        if ae > 0:
            chip(c, "menos erros", 1480, 360, AMBER, ae, 30)
            chip(c, "menos tempo", 1480, 470, AMBER, ae * ep(t, C["04.e"] + 0.4, 0.4), 30)
            chip(c, "menos faltas", 1480, 580, AMBER, ae * ep(t, C["04.e"] + 0.8, 0.4), 30)
        return
    a0 = ep(t, C["05"], 0.5)
    boxed(c, 360, 230, 1200, 140, BLUE, a0, 0.08)
    text(c, "DIVISÃO INVERSAMENTE PROPORCIONAL", W / 2, 296, 44, "black", BLUE, a0)
    text(c, "quanto maior o número, menor a parte", W / 2, 346, 28, "bold", INK2, a0)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "número MAIOR", 640, 480, 44, "black", INK, aa)
        arrow(c, 640, 640, 640, 520, INK, aa, 8, 24, progress=aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        text(c, "parte MENOR", 1280, 480, 44, "black", RED, ab)
        arrow(c, 1280, 520, 1280, 640, RED, ab, 8, 24, progress=ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 740, acc, "QUAIS SÃO OS PESOS?", AMBER, -3, 44)


# ======================================================================
# bloco A — a regra (virar a fração, não a fila)
# ======================================================================

def b_regra(c, t, C, B):
    head_seq(c, t, C, [("06", "A REGRA", "VIRE CADA NÚMERO", PURPLE), ("07", "POR QUE FUNCIONA?", "O MENOR VIRA O MAIOR", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        text(c, "INVERSAMENTE a", 520, 300, 42, "black", RED, aa)
        ab = ep(t, C["06.b"], 0.5)
        text(c, "= DIRETAMENTE aos INVERSOS", 1240, 300, 42, "black", GREEN, ab)
        for k, n in enumerate((2, 3, 4)):
            x = 640 + k * 320
            u = ep(t, C["06.c"] + 0.5 * k, 0.9)
            caixa(c, "", x, 490, GREEN if u > 0.5 else BLUE, aa, w=200, h=200)
            flip(c, n, x, 490, 120, u, aa, BLUE, GREEN)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            regra(c, "inverter é virar a FRAÇÃO, não a FILA", W / 2, 740, ad, 40)
        return
    aa = ep(t, C["07.a"], 0.5)
    for k, n in enumerate((2, 3, 4)):
        x = 560 + k * 400
        a = aa * ep(t, C["07.a"] + 0.3 * k, 0.4)
        hl = ep(t, C["07.b"], 0.5) if k == 0 else 0
        K.pizza(c, x, 450, 150, n, 1, a, sel_col=GREEN if k == 0 and hl > 0 else K.MOLHO)
        expr(c, f"1/{n}", x, 690, 64, a, cores={0: GREEN if k == 0 and hl > 0 else INK})
        text(c, f"veio do {n}", x, 780, 26, "bold", GRAY, a)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        pill(c, "O MAIOR PEDAÇO", 560, 255, GREEN, size=24, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        selo(c, 1360, 255, acc, "QUEM FALTOU MENOS VAI NA FRENTE", GREEN, -3, 28)


# ======================================================================
# bloco B — o atalho do MMC
# ======================================================================

def b_mmc(c, t, C, B):
    head_seq(c, t, C, [("08", "O ATALHO", "O MMC TIRA AS FRAÇÕES", GREEN), ("09", "VEZES 12", "PACOTINHOS INTEIROS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        a0 = ep(t, C["08"], 0.5)
        expr(c, "1/2  1/3  1/4", W / 2, 320, 96, a0, cores={0: INK, 1: INK, 2: INK}, gap=90)
        text(c, "pesos em fração = trabalho", W / 2, 450, 32, "bold", AMBER, a0)
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            chip(c, "× o MESMO número", W / 2, 540, PURPLE, aa, 36)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            text(c, "não muda a divisão: só deixa os pacotinhos INTEIROS", W / 2, 640, 34, "black", INK2, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            boxed(c, 660, 690, 600, 110, GREEN, acc, 0.08)
            ftext(c, "MMC(2, 3, 4) = 12", W / 2, 765, 50, "black", GREEN, acc)
        return
    rows = [("09.a", "1/2 × 12 = 6", 6, BLUE), ("09.b", "1/3 × 12 = 4", 4, PURPLE), ("09.c", "1/4 × 12 = 3", 3, AMBER)]
    for k, (cue, s, n, col) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        y = 290 + k * 130
        expr(c, s, 470, y, 56, a, cores={4: col})
        pacotes(c, t, 880, y, n, a, C[cue] + 0.3, col=mix(CAIXA, col, 0.25))
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        chip(c, "pesos 6, 4 e 3", 1560, 420, GREEN, ad, 40)
        text(c, "inteiros!", 1560, 510, 30, "black", GREEN, ad)
    ae = ep(t, C["09.e"], 0.5)
    K.atalho(c, 300, 650, 1320, 170, "ATALHO", ["peso = MMC ÷ número", "12 ÷ 2 = 6   ·   12 ÷ 3 = 4   ·   12 ÷ 4 = 3"], ae, 34)


# ======================================================================
# bloco C — daí em diante, divisão direta
# ======================================================================

def b_direta(c, t, C, B):
    head(c, t, B["start"], "DAÍ EM DIANTE", "DIVISÃO DIRETA DO EPISÓDIO 1", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    chip(c, "bônus: R$ 2 600", W / 2, 225, INK2, aa, 32)
    pesos = [6, 4, 3]
    partes = ["1 200", "800", "600"]
    ab = ep(t, C["10.b"], 0.5)
    abre = ep(t, C["10.c"] + 0.6, 0.6)
    for k, (nome, falt, col) in enumerate(PESSOAS):
        y = 345 + k * 140
        text(c, nome, 240, y + 4, 36, "black", col, ab, align="left")
        text(c, falt, 240, y + 44, 24, "bold", GRAY, ab, align="left")
        pacotes(c, t, 470, y, pesos[k], ab, C["10.b"] + 0.3 * k, abre, "200", col=mix(CAIXA, col, 0.25), s=62, gap=76)
        ad = ep(t, C["10.d"] + 0.9 * k, 0.5)
        linha(c, [("= R$ ", INK2), (partes[k], GREEN)], 1080, y, 44, ad)
    if ab > 0:
        rrect(c, 1290, 290, 440, 330, 22, "#FFFFFF", ab, shadow=True)
        text(c, "6 + 4 + 3 = 13", 1510, 360, 40, "black", INK, ab)
        text(c, "pacotinhos", 1510, 405, 28, "bold", INK2, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("2 600 ÷ 13 = ", INK), ("200", GREEN)], 1510, 490, 42, acc)
        text(c, "= k, o valor de 1 pacotinho", 1510, 570, 26, "bold", GREEN, acc)


# ======================================================================
# bloco E — as duas conferências
# ======================================================================

def b_confere(c, t, C, B):
    head(c, t, B["start"], "AS DUAS CONFERÊNCIAS", "ANTES DE MARCAR", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.5)
    text(c, "1ª  A SOMA FECHA?", 540, 270, 36, "black", PURPLE, a0)
    text(c, "2ª  MENOR NÚMERO, MAIOR PARTE?", 1340, 270, 36, "black", PURPLE, a0)
    line(c, 940, 240, 940, 720, "#E6E6E2", a0, 3)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        for k, s in enumerate(("1 200", "+ 800", "+ 600")):
            ftext(c, s, 680, 380 + k * 80, 50, "black", INK, aa * ep(t, C["11.a"] + 0.4 * k, 0.4), align="right")
        line(c, 400, 600, 700, 600, INK, aa, 4)
        ftext(c, "2 600", 680, 670, 54, "black", GREEN, ep(t, C["11.a"] + 1.6, 0.4), align="right")
        check_icon(c, 790, 650, 34, ep(t, C["11.a"] + 1.8, 0.4), GREEN)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        alt = [300, 200, 150]
        vals = ["1 200", "800", "600"]
        for k, (nome, falt, col) in enumerate(PESSOAS):
            x = 1130 + k * 210
            h = alt[k] * ep(t, C["11.b"] + 0.3 * k, 0.5)
            rrect(c, x - 60, 660 - h, 120, h, 12, col, ab * 0.85)
            text(c, vals[k], x, 640 - h, 30, "black", INK, ab)
            text(c, falt, x, 705, 26, "black", col, ab)
        check_icon(c, 1700, 400, 34, ep(t, C["11.b"] + 1.5, 0.4), GREEN)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 790, acc, "PASSOU NAS DUAS: PODE MARCAR", GREEN, -2, 34)


# ======================================================================
# bloco D — a armadilha da fila virada
# ======================================================================

def b_armadilha(c, t, C, B):
    head_seq(c, t, C, [("12", "E SE VIRAR A FILA?", "A ARMADILHA", RED), ("13", "O QUE DEU ERRADO", "ACERTA QUEM, ERRA QUANTO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        # à esquerda, o caminho certo (verde)
        a0 = ep(t, C["12"], 0.5)
        pill(c, "CERTO", 520, 230, GREEN, size=24, a=a0, anchor="center", bounds=(0, 1920))
        text(c, "vira cada NÚMERO", 520, 300, 30, "black", GREEN, a0)
        for k, n in enumerate((2, 3, 4)):
            flip(c, n, 380 + k * 140, 400, 80, 1.0, a0, BLUE, GREEN)
        ftext(c, "× 12  →  6 · 4 · 3", 520, 520, 40, "black", GREEN, a0)
        ftext(c, "1 200 · 800 · 600", 520, 610, 40, "black", GREEN, a0)
        conferido(c, "números redondos", 380, 700, a0, True, 30)
        line(c, 920, 230, 920, 790, "#E6E6E2", a0, 3)
        # à direita, a fila virada (vermelho)
        aa = ep(t, C["12.a"], 0.5)
        pill(c, "ERRADO", 1340, 230, RED, size=24, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "vira a FILA", 1340, 300, 30, "black", RED, aa)
        u = ep(t, C["12.a"] + 0.3, 1.0)
        orig = [2, 3, 4]
        for k, n in enumerate(orig):
            x0 = 1200 + k * 140
            x1 = 1200 + (2 - k) * 140
            x = lerp(x0, x1, u)
            y = 400 - 60 * math.sin(math.pi * u) * (1 if k != 1 else 0)
            caixa(c, str(n), x, y, RED, aa, 60, 100, 96, fill="#FDECEC")
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            ftext(c, "4 + 3 + 2 = 9", 1340, 520, 40, "black", INK, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            ftext(c, "2 600 ÷ 9 = 288,888…", 1340, 600, 40, "black", RED, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            ftext(c, "≈ 1 155,56 · 866,67 · 577,78", 1340, 690, 36, "black", RED, ad)
            conferido(c, "números quebrados", 1200, 770, ad, False, 30)
        return
    # 13 — acerta quem, erra quanto
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        conferido(c, "QUEM recebe mais: a Ana (acertou)", 300, 270, aa, True, 34)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        conferido(c, "QUANTO ela recebe a mais que o Bruno?", 300, 350, ab, False, 34)
        boxed(c, 260, 410, 640, 220, GREEN, ab, 0.06)
        text(c, "CERTO", 580, 460, 28, "black", GREEN, ab)
        expr(c, "1/2 ÷ 1/3 = 1,5", 580, 525, 56, ab, cores={4: GREEN})
        text(c, "uma vez e meia", 580, 612, 28, "bold", GREEN, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        boxed(c, 1020, 410, 640, 220, RED, acc, 0.06)
        text(c, "FILA VIRADA", 1340, 460, 28, "black", RED, acc)
        ftext(c, "4 ÷ 3 ≈ 1,33", 1340, 540, 56, "black", RED, acc)
        text(c, "só uma vez e um terço", 1340, 610, 28, "bold", RED, acc)
    ad = ep(t, C["13.d"], 0.5)
    K.atalho(c, 360, 670, 1200, 150, "ATALHO", ["número quebrado = sinal de caminho errado"], ad, 36)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("15", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    text(c, "pesos para dividir INVERSAMENTE a", W / 2, 260, 40, "black", INK, aa)
    conf = t >= C["15"]
    for k, n in enumerate((3, 4, 6)):
        x = 700 + k * 260
        u = ep(t, C["15.a"] + 0.4 * k, 0.8) if conf else 0
        caixa(c, "", x, 400, GREEN if u > 0.5 else BLUE, aa, w=170, h=170)
        flip(c, n, x, 400, 100, u, aa, BLUE, GREEN)
    ab = ep(t, C["14.b"], 0.5) * (1 - (ep(t, C["15"], 0.3) if conf else 0))
    if ab > 0:
        pill(c, "só os pesos, sem o dinheiro", W / 2, 560, AMBER, size=30, a=ab, anchor="center", bounds=(0, 1920))
    pause_timer(c, t, C["14.end"] - 1.9, W / 2, 690)
    if not conf:
        return
    bb = ep(t, C["15.b"], 0.5)
    if bb > 0:
        ftext(c, "MMC(3, 4, 6) = 12", 420, 600, 42, "black", PURPLE, bb)
    cc = ep(t, C["15.c"], 0.5)
    if cc > 0:
        ftext(c, "12 ÷ 3 = 4  ·  12 ÷ 4 = 3  ·  12 ÷ 6 = 2", 1220, 600, 38, "black", INK, cc)
        chip(c, "pesos 4, 3 e 2", W / 2, 700, GREEN, ep(t, C["15.c"] + 1.6, 0.4), 44)
    dd = ep(t, C["15.d"], 0.5)
    if dd > 0:
        ftext(c, "6, 4, 3", 1500, 730, 36, "black", RED, dd)
        strike(c, 1435, 718, 1565, 718, dd, RED, ep(t, C["15.d"] + 0.4, 0.4))
        text(c, "fila virada", 1500, 772, 22, "bold", RED, dd)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Inversa: troque cada número pelo seu inverso.", "Multiplique pelo MMC e as frações somem.",
          "Inverter o valor, não a ordem."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "26"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Usar os próprios números (2, 3, 4) como pesos", "é assim na divisão direta",
          "aí quem faltou mais ganha mais: na inversa, use os INVERSOS"),
         ("Inverter a ORDEM (4, 3, 2) em vez dos valores", "a palavra é \"inversa\", e a fila de trás para frente parece inversa",
          "inverter é virar cada número: 2, 3, 4 → 1/2, 1/3, 1/4 → pesos 6, 4, 3"),
         ("Não conferir se o menor número levou a maior parte", "a soma das partes fechou",
          "a soma fecha até com pesos errados: só a 2ª conferência pega a troca")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


# ======================================================================
# Questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS2 = [("A", "R$ 600,00", "a MENOR parte", RED), ("B", "R$ 800,00", "a parte do meio", RED),
         ("C", "R$ 1.100,00", "não sai de conta certa", RED), ("D", "R$ 1.200,00", "", GREEN),
         ("E", "R$ 1.300,00", "metade do total", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO COM VOCÊ", "DIVISÃO INVERSA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    _enunciado(c, [("Uma quantia de R$ 2.600,00 será repartida entre três funcionários em partes inversamente proporcionais "
                    "aos números 2, 3 e 4.", INK),
                   ("A maior parte corresponde a", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABCE"}
    if t >= C["20.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS2, 1000, 240, 680, 42, C["21.ok"], "D", cues_in, cues_x, gap=30)
    if t >= C["21"]:
        ra = ep(t, C["21"], 0.4)
        rrect(c, 170, 460, 740, 350, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["21.a"], 0.4)
        expr(c, "1/2 · 1/3 · 1/4", 400, 530, 44, aa, cores=mono("1/2 · 1/3 · 1/4", INK))
        ftext(c, "× 12  →  6 · 4 · 3", 720, 530, 32, "black", PURPLE, aa)
        linha(c, [("soma 13  →  k = ", INK), ("200", GREEN)], 540, 620, 38, ep(t, C["21.b"], 0.4))
        linha(c, [("1 200 · 800 · 600", GREEN)], 540, 695, 40, ep(t, C["21.c"], 0.4))
        ad = ep(t, C["21.d"], 0.4)
        conferido(c, "soma 2 600", 210, 775, ad, True, 26)
        conferido(c, "menor nº, maior parte", 520, 775, ad, True, 26)


ALTS8 = [("A", "R$ 700,00", "parte de quem teve 6 faltas", RED), ("B", "R$ 1.050,00", "não fecha a soma", RED),
         ("C", "R$ 1.400,00", "", GREEN), ("D", "R$ 1.800,00", "não fecha a soma", RED),
         ("E", "R$ 2.100,00", "parte de quem teve 2 faltas", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · VOCÊ FAZ", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Uma empresa distribuirá um bônus de R$ 4.200,00 entre três funcionários, em partes inversamente "
                    "proporcionais ao número de faltas de cada um no semestre: 2, 3 e 6 faltas.", INK),
                   ("O funcionário com 3 faltas receberá", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABDE"}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS8, 1000, 240, 680, 42, C["24.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["23.end"] - 1.9, 540, 660)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        rrect(c, 170, 520, 740, 290, 18, "#FFFFFF", ra, shadow=True)
        if t < C["25"]:
            aa = ep(t, C["24.a"], 0.4)
            expr(c, "1/2 · 1/3 · 1/6", 400, 580, 42, aa, cores=mono("1/2 · 1/3 · 1/6", INK))
            ftext(c, "MMC 6", 730, 580, 32, "black", PURPLE, aa)
            ftext(c, "pesos 3 · 2 · 1", 540, 650, 36, "black", PURPLE, ep(t, C["24.b"], 0.4))
            linha(c, [("4 200 ÷ 6 = ", INK), ("700", GREEN)], 540, 715, 36, ep(t, C["24.c"], 0.4))
            linha(c, [("3 faltas: 2 × 700 = ", INK), ("1 400", GREEN)], 540, 780, 36, ep(t, C["24.d"], 0.4))
        else:
            ab = ep(t, C["25"], 0.4)
            text(c, "AS DUAS CONFERÊNCIAS", 540, 575, 26, "black", PURPLE, ab)
            linha(c, [("2 100 + 1 400 + 700 = ", INK), ("4 200", GREEN)], 540, 650, 34, ep(t, C["25.a"], 0.4))
            conferido(c, "a soma fecha", 260, 720, ep(t, C["25.a"] + 0.8, 0.4), True, 28)
            conferido(c, "faltou menos, levou mais", 260, 780, ep(t, C["25.b"], 0.4), True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DOIS CRITÉRIOS", PURPLE)
    aa = ep(t, C["27.a"], 0.5)
    chip(c, "pessoas", 760, 330, BLUE, aa, 46)
    chip(c, "dias trabalhados", 1180, 330, AMBER, aa, 46)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        ftext(c, "5 + 2 = 7 ?", 760, 520, 60, "black", RED, ab)
        strike(c, 620, 500, 900, 500, ab, RED, ep(t, C["27.b"] + 0.6, 0.4))
        text(c, "o instinto", 760, 590, 28, "bold", RED, ab)
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        ftext(c, "5 × 2 = 10", 1180, 520, 60, "black", GREEN, acc)
        text(c, "o certo", 1180, 590, 28, "bold", GREEN, acc)
    pill(c, "ep. 3 · divisão composta", W / 2, 720, PURPLE, size=32, a=ep(t, C["27.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"], "Já virou a fila em vez dos números?",
        canal="no Estudativo", anki=C["28.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, menos=b_menos, regra=b_regra, mmc=b_mmc, direta=b_direta,
              confere=b_confere, armadilha=b_armadilha, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q8=b_q8,
              ponte=b_ponte, cta=b_cta)
