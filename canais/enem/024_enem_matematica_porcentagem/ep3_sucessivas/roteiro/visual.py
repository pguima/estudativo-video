"""Visual — Porcentagem, Episódio 3: variações sucessivas, multiplicar os fatores (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações e potências, alternativas, erro_cards,
atalho...). Peças deste episódio: bola() (a bola de neve com o valor em reais), maquina() e engrenagem() (a máquina de fator
do episódio 2), esteira() (o preço passando por duas máquinas em sequência), linha() (texto com milhar e cor por trecho).
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
_s = importlib.util.spec_from_file_location("comum024", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_porcentagem_ep3_sucessivas.mp4"
CARD_R = K.CARD_R
NEVE = "#EEF4FB"
NEVE_B = "#B7CCE4"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)] (mantém os espaços dos milhares)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def bola(c, cx, cy, r, a, valor=None, col=None, vsize=None):
    """bola de neve: círculo claro com sombra, brilho e o valor em reais no centro"""
    if a <= 0 or r <= 1:
        return
    c.drawCircle(cx + r * 0.06, cy + r * 0.10, r, paint("#000000", a * 0.10))
    c.drawCircle(cx, cy, r, paint(NEVE, a))
    c.drawCircle(cx, cy, r, paint(NEVE_B, a, stroke=4))
    c.drawCircle(cx - r * 0.38, cy - r * 0.38, r * 0.16, paint("#FFFFFF", a * 0.9))
    for k, (dx, dy, rr) in enumerate(((0.45, 0.30, 0.07), (-0.25, 0.52, 0.05), (0.15, -0.55, 0.05))):
        c.drawCircle(cx + dx * r, cy + dy * r, rr * r, paint(NEVE_B, a * 0.6))
    if valor:
        text_mid(c, valor, cx, cy, vsize or max(22, r * 0.36), "black", col or INK, a)


def engrenagem(c, cx, cy, r, ang, col, a, dentes=10):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    for k in range(dentes):
        c.save(); c.rotate(360 * k / dentes)
        c.drawRect(skia.Rect.MakeXYWH(-r * 0.16, -r * 1.22, r * 0.32, r * 0.4), paint(col, a))
        c.restore()
    c.drawCircle(0, 0, r, paint(col, a))
    c.drawCircle(0, 0, r * 0.38, paint("#FFFFFF", a))
    c.restore()


def maquina(c, cx, cy, fator, a, ang=0.0, col=None, w=250, h=170, sub=None):
    """a máquina de fator: caixa com engrenagem girando e o rótulo '× fator'"""
    if a <= 0:
        return
    col = col or PURPLE
    engrenagem(c, cx + w * 0.26, cy - h / 2 - 8, 30, ang, mix(col, "#FFFFFF", 0.35), a)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, col, a, shadow=True)
    rrect(c, cx - w / 2 + 14, cy - h / 2 + 14, w - 28, h - 28, 16, mix(col, "#FFFFFF", 0.88), a)
    text_mid(c, f"× {fator}", cx, cy - (10 if sub else 0), 52, "black", col, a)
    if sub:
        text_mid(c, sub, cx, cy + 42, 24, "bold", INK2, a)


def ficha(c, s, cx, cy, a, col=None, size=40):
    """o preço viajando na esteira"""
    if a <= 0:
        return
    w = text_w(s, "black", size) + 44
    rrect(c, cx - w / 2, cy - size * 0.75, w, size * 1.5, size * 0.75, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - size * 0.75, w, size * 1.5), size * 0.75,
                                      size * 0.75), paint(col or GREEN, a, stroke=4))
    text_mid(c, s, cx, cy, size, "black", col or GREEN, a)


def esteira(c, t, x0, x1, y, a, maqs, valores, t_ini, passo=1.4):
    """o preço anda da esquerda para a direita e passa pelas máquinas (maqs = [(x, fator, col)]);
    valores = [antes, depois_da_1, depois_da_2]; t_ini = instante em que a ficha começa a andar"""
    if a <= 0:
        return
    line(c, x0, y + 70, x1, y + 70, "#CFCFC9", a, 10)
    for k in range(int((x1 - x0) / 60) + 1):
        xx = x0 + k * 60 + ((t * 40) % 60)
        if xx < x1:
            line(c, xx, y + 66, xx - 14, y + 74, "#B5B5AE", a, 3)
    for mx, f, col in maqs:
        maquina(c, mx, y - 10, f, a, ang=t * 90, col=col, w=220, h=150)
    # trajetória: antes → máquina 1 → entre → máquina 2 → depois
    pontos = [x0 + 60, maqs[0][0], (maqs[0][0] + maqs[1][0]) / 2, maqs[1][0], x1 - 70]
    u = clamp((t - t_ini) / (passo * 4))
    seg = min(int(u * 4), 3)
    f = u * 4 - seg
    xs = lerp(pontos[seg], pontos[seg + 1], ease_io(clamp(f)))
    val = valores[0] if xs < maqs[0][0] else (valores[1] if xs < maqs[1][0] else valores[2])
    dentro = any(abs(xs - mx) < 100 for mx, _, _ in maqs)
    ficha(c, val, xs, y + 160, a * (0.25 if dentro else 1.0), GREEN if val != valores[0] else INK2, 38)


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "VARIAÇÕES SUCESSIVAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        pill(c, "SALÁRIO", 560, 230, BLUE, size=26, a=aa, anchor="center", bounds=(0, 1920))
        chip(c, "+10%  jan", 420, 340, GREEN, aa, 40)
        chip(c, "+20%  jul", 710, 340, GREEN, aa * ep(t, C["01.a"] + 0.6, 0.4), 40)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        ftext(c, "= +30% ?", 560, 470, 64, "black", RED, ab)
        strike(c, 420, 452, 700, 452, ab, RED, ep(t, C["01.c"], 0.4))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        ftext(c, "+32%", 560, 600, 96, "black", GREEN, acc)
    line(c, 960, 220, 960, 800, "#E6E6E2", ep(t, C["01.d"], 0.5), 3)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "DESCONTOS", 1360, 230, AMBER, size=26, a=ad, anchor="center", bounds=(0, 1920))
        chip(c, "−30%", 1250, 340, RED, ad, 40)
        chip(c, "−10%", 1470, 340, RED, ad * ep(t, C["01.d"] + 0.4, 0.4), 40)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        ftext(c, "= −40% ?", 1360, 470, 64, "black", RED, ae)
        strike(c, 1210, 452, 1510, 452, ae, RED, ep(t, C["01.e"] + 0.6, 0.4))
        selo(c, 1360, 610, ep(t, C["01.e"] + 0.9, 0.4), "NÃO DÃO 40%", AMBER, -4, 40)
    ab2 = ep(t, C["01.c"] + 0.4, 0.5)
    if ab2 > 0:
        text(c, "a soma engana nos dois sentidos", W / 2, 760, 32, "bold", INK2, ep(t, C["01.e"] + 1.2, 0.5))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver QUALQUER sequência de aumentos e descontos", "dois, três, quantos vierem"),
            ("02.b", "com uma ÚNICA conta", "multiplicando os fatores")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 230, y - 14, 34, a, GREEN)
        text(c, s, 290, y, 46, "black", INK, a, align="left")
        text(c, sub, 290, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "O FATOR DO EPISÓDIO 2", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "AUMENTO de 10%", 560, 300, 40, "black", GREEN, aa)
        maquina(c, 560, 460, "1,10", aa, ang=t * 90, col=GREEN)
        linha(c, [("1", INK), (" + ", INK2), ("0,10", GREEN)], 560, 620, 50, aa)
        text(c, "o 1 é o que você já tinha", 560, 690, 28, "bold", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "DESCONTO de 30%", 1360, 300, 40, "black", RED, ab)
        maquina(c, 1360, 460, "0,70", ab, ang=-t * 90, col=RED)
        linha(c, [("1", INK), (" − ", INK2), ("0,30", RED)], 1360, 620, 50, ab)
        text(c, "sobra 70%", 1360, 690, 28, "bold", INK2, ab)
    line(c, 960, 260, 960, 720, "#E6E6E2", ab, 3)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        pill(c, "UMA multiplicação → o preço novo", W / 2, 800, PURPLE, size=30, a=acc, anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco B — o salário em reais, mês a mês
# ======================================================================

def b_salario(c, t, C, B):
    head_seq(c, t, C, [("04", "EM REAIS, SEM PRESSA", "MÊS A MÊS", BLUE), ("05", "QUANTO SUBIU NO ANO?", "O ACUMULADO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    aa = ep(t, C["04.a"], 0.5)
    col_x = [430, 960, 1490]
    rot = ["início", "janeiro: +10%", "julho: +20%"]
    vals = ["R$ 1 000", "R$ 1 100", "R$ 1 320"]
    cues = ["04.a", "04.b", "04.e"]
    for k in range(3):
        a = ep(t, C[cues[k]], 0.5)
        text(c, rot[k], col_x[k], 250, 32, "black", [INK2, GREEN, GREEN][k], a)
        ftext(c, vals[k], col_x[k], 360, 60, "black", INK if k == 0 else GREEN, a)
        if k > 0:
            arrow(c, col_x[k - 1] + 150, 345, col_x[k] - 150, 345, GREEN, a, 6, 20, progress=a)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        linha(c, [("10% de 1 000 = ", INK2), ("100", GREEN)], col_x[1], 450, 34, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0 and sid == "04":
        ftext(c, "20% de quê?", col_x[2], 450, 40, "black", AMBER, acc * (1 - ep(t, C["04.d"], 0.3)))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        linha(c, [("20% de ", INK2), ("1 100", BLUE), (" = ", INK2), ("220", GREEN)], col_x[2], 450, 34, ad)
        pill(c, "sobre o salário DE AGORA", col_x[2], 520, BLUE, size=24, a=ad, anchor="center", bounds=(0, 1920))
    if sid == "05":
        a5 = ep(t, C["05.a"], 0.5)
        if a5 > 0:
            linha(c, [("1 320 − 1 000 = ", INK), ("320", GREEN), (" a mais", INK2)], W / 2, 620, 46, a5)
        b5 = ep(t, C["05.b"], 0.5)
        if b5 > 0:
            linha(c, [("320 de 1 000 = ", INK), ("32%", GREEN)], W / 2, 700, 52, b5)
        c5 = ep(t, C["05.c"], 0.5)
        if c5 > 0:
            boxed(c, 560, 750, 800, 70, BLUE, c5, 0.08)
            text(c, "ACUMULADO = o efeito de todos os aumentos juntos", W / 2, 795, 28, "black", BLUE, c5)


# ======================================================================
# bloco A — a regra (e os fatores em corrente)
# ======================================================================

def b_regra(c, t, C, B):
    head_seq(c, t, C, [("06", "VARIAÇÃO SUCESSIVA", "A REGRA", PURPLE), ("07", "COM OS FATORES", "A CORRENTE DE MÁQUINAS", PURPLE),
                       ("08", "ATALHO", "DE CABEÇA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid == "06":
        a0 = ep(t, C["06"], 0.5)
        boxed(c, 410, 230, 1100, 130, BLUE, a0, 0.08)
        text(c, "VARIAÇÃO SUCESSIVA", W / 2, 292, 46, "black", BLUE, a0)
        text(c, "uma mudança DEPOIS da outra", W / 2, 340, 28, "bold", INK2, a0)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            regra(c, "MULTIPLIQUE os fatores", W / 2, 500, ab, 50)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            ftext(c, "NUNCA some as porcentagens", W / 2, 650, 50, "black", RED, acc)
            check_icon(c, 520, 632, 36, acc, RED, "x")
        return
    if sid == "07":
        a0 = ep(t, C["07.a"], 0.5)
        esteira(c, t, 220, 1700, 380, a0, [(700, "1,10", GREEN), (1220, "1,20", GREEN)],
                ["R$ 1 000", "R$ 1 100", "R$ 1 320"], C["07.a"] + 0.2, 1.1)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            linha(c, [("1,10 × 1,20 = ", INK), ("1,32", GREEN)], W / 2, 690, 56, acc)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            linha(c, [("1", INK), (" + ", INK2), ("0,32", GREEN), ("   →   +32%", GREEN)], W / 2, 780, 44, ad)
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text(c, "× 1,10  =  o número + 10% dele", W / 2, 320, 50, "black", PURPLE, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        linha(c, [("1,20", INK), (" + ", INK2), ("0,12", BLUE), (" = ", INK2), ("1,32", GREEN)], W / 2, 460, 70, ab)
        text(c, "10% de 1,20 = 0,12", 1000, 560, 30, "bold", BLUE, ab)
    acc = ep(t, C["08.c"], 0.5)
    K.atalho(c, 380, 640, 1160, 150, "ATALHO", ["× 1,10 é somar 10% do próprio número"], acc, 38)


# ======================================================================
# bloco C — a bola de neve
# ======================================================================

def b_bola(c, t, C, B):
    head(c, t, B["start"], "POR QUE NÃO 30%?", "A BOLA DE NEVE", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    grow1 = ep(t, C["09.a"] + 1.4, 0.9)
    r1 = 100 + 10 * grow1
    bola(c, 480, 470, r1, aa, "R$ 1 000" if grow1 < 0.5 else "R$ 1 100", INK if grow1 < 0.5 else GREEN, 34)
    if aa > 0:
        text(c, "1º aumento: +10%", 480, 280, 32, "black", GREEN, aa)
        text(c, "sobre 1 000 = R$ 100", 480, 680, 30, "bold", INK2, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        arrow(c, 640, 470, 860, 470, INK2, ab, 6, 20, progress=ab)
        grow2 = ep(t, C["09.c"], 0.9)
        r2 = 110 + 22 * grow2
        bola(c, 1080, 470, r2, ab, "R$ 1 100" if grow2 < 0.5 else "R$ 1 320", INK if grow2 < 0.5 else GREEN, 36)
        text(c, "2º aumento: +20%", 1080, 280, 32, "black", GREEN, ab)
        text(c, "sobre a bola que JÁ CRESCEU", 1080, 690, 28, "bold", BLUE, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        boxed(c, 1340, 330, 380, 280, GREEN, acc, 0.06)
        linha(c, [("20% de 1 100", INK)], 1530, 390, 34, acc)
        linha(c, [("= ", INK2), ("R$ 220", GREEN)], 1530, 450, 46, acc)
        linha(c, [("não 200", RED)], 1530, 530, 32, acc)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 790, ad, "OS R$ 20 A MAIS = OS 2% QUE A SOMA ESQUECE", AMBER, -2, 32)


# ======================================================================
# bloco D — a ordem não importa
# ======================================================================

def b_ordem(c, t, C, B):
    head(c, t, B["start"], "E AO CONTRÁRIO?", "A ORDEM NÃO IMPORTA", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.5)
    text(c, "+10% depois +20%", 560, 250, 34, "black", INK2, a0)
    for k, s in enumerate(("1 000", "1 100", "1 320")):
        ftext(c, s, 300 + k * 260, 340, 44, "black", GREEN if k else INK, a0)
        if k:
            arrow(c, 300 + (k - 1) * 260 + 90, 326, 300 + k * 260 - 90, 326, GREEN, a0, 5, 16, progress=a0)
    text(c, "+20% depois +10%", 1360, 250, 34, "black", INK2, ep(t, C["10.a"], 0.5))
    vals = ["1 000", "1 200", "1 320"]
    cues = ["10.a", "10.a", "10.b"]
    for k, s in enumerate(vals):
        a = ep(t, C[cues[k]] + (0.6 if k == 1 else 0), 0.5)
        ftext(c, s, 1100 + k * 260, 340, 44, "black", GREEN if k else INK, a)
        if k:
            arrow(c, 1100 + (k - 1) * 260 + 90, 326, 1100 + k * 260 - 90, 326, GREEN, a, 5, 16, progress=a)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("10% de 1 200 = ", INK2), ("120", GREEN)], 1360, 430, 32, ab)
    line(c, 960, 220, 960, 470, "#E6E6E2", a0, 3)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 520, acc, "O MESMO VALOR", GREEN, -3, 44)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        linha(c, [("1,20 × 1,10", INK), (" = ", INK2), ("1,10 × 1,20", INK)], W / 2, 650, 54, ad)
        boxed(c, 560, 715, 800, 80, BLUE, ad, 0.08)
        text(c, "COMUTATIVA: a ordem não muda o produto", W / 2, 765, 30, "black", BLUE, ad)


# ======================================================================
# bloco E — descontos cumulativos
# ======================================================================

def b_descontos(c, t, C, B):
    head_seq(c, t, C, [("11", "30% OFF + 10% NO CAIXA", "DESCONTOS CUMULATIVOS", AMBER),
                       ("12", "COM OS FATORES", "PAGA 63%", PURPLE), ("13", "A PEGADINHA", "PAGO × DESCONTADO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            rrect(c, 230, 230, 420, 200, 26, RED, aa, shadow=True)
            text_mid(c, "30% OFF", 440, 310, 70, "black", "#FFFFFF", aa)
            text_mid(c, "em tudo", 440, 385, 30, "bold", "#FFFFFF", aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            rrect(c, 700, 260, 340, 150, 22, AMBER, ab, shadow=True)
            text_mid(c, "+10% no caixa", 870, 335, 40, "black", "#FFFFFF", ab)
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            boxed(c, 1100, 250, 560, 170, BLUE, acc, 0.08)
            text(c, "CUMULATIVOS", 1380, 315, 40, "black", BLUE, acc)
            text(c, "um aplicado em cima do outro", 1380, 370, 28, "bold", INK2, acc)
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            ftext(c, "R$ 100", 380, 580, 56, "black", INK, ad)
            arrow(c, 500, 565, 720, 565, RED, ad, 6, 20, progress=ad)
            text(c, "−30%", 610, 530, 30, "black", RED, ad)
            ftext(c, "R$ 70", 840, 580, 56, "black", INK, ep(t, C["11.d"] + 0.8, 0.4))
        ae = ep(t, C["11.e"], 0.5)
        if ae > 0:
            arrow(c, 950, 565, 1170, 565, RED, ae, 6, 20, progress=ae)
            text(c, "−10% de 70 = 7", 1060, 530, 28, "black", RED, ae)
            ftext(c, "R$ 63", 1300, 580, 64, "black", GREEN, ep(t, C["11.e"] + 0.8, 0.4))
            text(c, "você paga", 1300, 660, 28, "bold", INK2, ep(t, C["11.e"] + 0.8, 0.4))
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        esteira(c, t, 220, 1700, 330, aa, [(700, "0,70", RED), (1220, "0,90", RED)], ["R$ 100", "R$ 70", "R$ 63"],
                C["12.a"], 0.9)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("0,70 × 0,90 = ", INK), ("0,63", PURPLE), ("  → paga 63%", INK2)], W / 2, 620, 46, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            linha(c, [("desconto: 100% − 63% = ", INK), ("37%", GREEN)], W / 2, 700, 46, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 790, ad, "MENOS QUE A SOMA: O PREÇO JÁ ENCOLHEU", AMBER, -2, 32)
        return
    # 13 — pago × descontado
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 260, 820 * 0.63, 130, 16, PURPLE, aa)
        text_mid(c, "0,63 → você PAGA", 300 + 820 * 0.63 / 2, 325, 36, "black", "#FFFFFF", aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 300 + 820 * 0.63 + 8, 260, 820 * 0.37 - 8, 130, 16, GREEN, ab)
        text_mid(c, "0,37 → DESCONTO", 300 + 820 * 0.63 + 820 * 0.37 / 2 + 4, 325, 26, "black", "#FFFFFF", ab)
        text(c, "1 − 0,63", 300 + 820 * 0.815, 440, 30, "bold", GREEN, ab)
        line(c, 300, 410, 1120, 410, INK2, ab, 2)
        text(c, "o preço inteiro = 1", 710, 470, 26, "bold", INK2, ab)
    acc = ep(t, C["13.c"], 0.5)
    K.atalho(c, 300, 560, 1320, 200, "ATALHO",
             ["o fator de desconto é o que você PAGA", "o desconto é 1 menos ele"], acc, 36)
    if acc > 0:
        pill(c, "leia: a questão pede o que se PAGA ou o que se DESCONTA?", W / 2, 810, AMBER, size=24,
             a=ep(t, C["13.c"] + 1.6, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco F — a mesma variação repetida vira potência
# ======================================================================

def b_potencia(c, t, C, B):
    head(c, t, B["start"], "A MESMA VARIAÇÃO 3 VEZES", "VIRA POTÊNCIA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    for k in range(3):
        a = aa * ep(t, C["14.a"] + 0.4 * k, 0.4)
        maquina(c, 520 + k * 440, 330, "1,10", a, ang=t * 90, col=GREEN, w=220, h=140)
        if k < 2:
            arrow(c, 520 + k * 440 + 125, 330, 520 + (k + 1) * 440 - 125, 330, GREEN, a, 5, 16, progress=a)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("1,10 × 1,10 × 1,10", INK)], W / 2, 500, 50, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        expr(c, "= 1,10^3", 1360, 500, 56, acc, cores={1: PURPLE})
        text(c, "o 3 lá em cima: quantas vezes multiplica", 1360, 580, 26, "bold", PURPLE, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        linha(c, [("1,331", GREEN), ("  →  +33,1%", GREEN), ("   (não 30%)", RED)], W / 2, 680, 50, ad)
    ae = ep(t, C["14.e"], 0.5)
    if ae > 0:
        pill(c, "a porta dos JUROS COMPOSTOS · série própria", W / 2, 785, BLUE, size=28, a=ae, anchor="center",
             bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("16", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    chip(c, "+50%", 760, 280, GREEN, aa, 52)
    chip(c, "depois +50%", 1120, 280, GREEN, aa * ep(t, C["15.a"] + 0.6, 0.4), 52)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        text(c, "qual foi o aumento TOTAL?", W / 2, 400, 44, "black", INK, ab)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 560)
    if t < C["16"]:
        return
    a1 = ep(t, C["16.a"], 0.5)
    if a1 > 0:
        linha(c, [("1,5 × 1,5 = ", INK), ("2,25", PURPLE)], 560, 520, 56, a1)
    b1 = ep(t, C["16.b"], 0.5)
    if b1 > 0:
        linha(c, [("1", INK), (" + ", INK2), ("1,25", GREEN), ("  →  +125%", GREEN)], 560, 620, 48, b1)
    c1 = ep(t, C["16.c"], 0.5)
    if c1 > 0:
        text(c, "EM REAIS", 1360, 470, 30, "black", INK2, c1)
        linha(c, [("100 → 150 → ", INK), ("225", GREEN)], 1360, 540, 50, c1)
    d1 = ep(t, C["16.d"], 0.5)
    if d1 > 0:
        ftext(c, "somou: +100%", 1360, 650, 40, "black", RED, d1)
        strike(c, 1230, 636, 1490, 636, d1, RED, ep(t, C["16.d"] + 0.5, 0.4))
        text(c, "errou por 25", 1360, 710, 28, "bold", RED, d1)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Variações em sequência: multiplique os fatores.", "A segunda variação incide sobre o valor já alterado.",
          "A ordem não muda o resultado."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "25"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Somar as porcentagens: +10% e +20% = +30%", "somar é o que a gente faz com tudo",
          "o 2º aumento é sobre o valor JÁ aumentado: 1,10 × 1,20 = 1,32 → +32%"),
         ("Somar os descontos: 30% e 10% = 40%", "a placa mostra dois números com por cento",
          "o desconto do caixa é sobre um preço MENOR: 0,70 × 0,90 = 0,63 → 37%"),
         ("Confundir o que se PAGA (63%) com o que se DESCONTA", "o 63 sai direto da conta",
          "0,63 é o que você paga; o desconto é 100% − 63% = 37%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


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


ALTS3 = [("A", "15%", "a média das taxas", RED), ("B", "30%", "a soma ingênua", RED), ("C", "32%", "", GREEN),
         ("D", "33%", "não sai deste enunciado", RED), ("E", "200%", "multiplicou as taxas: 10 × 20", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · A PROVA OFICIAL", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    _enunciado(c, [("O salário de um funcionário recebeu um reajuste de 10% em janeiro e outro de 20% em julho, ambos "
                    "aplicados sobre o valor vigente na data.", INK),
                   ("O aumento acumulado no ano foi de", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABDE"}
    if t >= C["21.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS3, 1000, 240, 680, 44, C["22.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["21.end"] - 1.9, 540, 640)
    if t >= C["22"]:
        ra = ep(t, C["22"], 0.4)
        rrect(c, 170, 520, 740, 290, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["22.a"], 0.4)
        linha(c, [("1,10 × 1,20 = ", INK), ("1,32", GREEN)], 540, 590, 46, aa)
        linha(c, [("→ +32%", GREEN)], 540, 655, 40, aa)
        ab = ep(t, C["22.b"], 0.4)
        linha(c, [("1 000 → 1 100 → ", INK2), ("1 320", GREEN)], 540, 735, 36, ab)
        if ab > 0:
            check_icon(c, 820, 718, 26, ab, GREEN)


ALTS6 = [("A", "33%", "30 + 10% de 30", RED), ("B", "37%", "", GREEN), ("C", "40%", "somou as taxas", RED),
         ("D", "43%", "passa da soma: impossível", RED), ("E", "63%", "é o que se PAGA", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · A PROVA OFICIAL", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Uma loja anuncia 30% de desconto em toda a coleção e oferece ainda 10% adicionais de abatimento no "
                    "caixa, aplicados sobre o valor já reduzido.", INK),
                   ("O desconto total obtido pelo cliente é de", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS6, 1000, 240, 680, 44, C["24.ok"], "B", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["23.end"] - 1.9, 540, 640)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        rrect(c, 170, 520, 740, 290, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["24.a"], 0.4)
        linha(c, [("0,70 × 0,90 = ", INK), ("0,63", PURPLE)], 540, 585, 44, aa)
        ab = ep(t, C["24.b"], 0.4)
        linha(c, [("paga 63%  →  desconto ", INK2), ("37%", GREEN)], 540, 655, 38, ab)
        acc = ep(t, C["24.c"], 0.4)
        linha(c, [("100 → 70 → ", INK2), ("63", GREEN)], 540, 735, 36, acc)
        if acc > 0:
            check_icon(c, 740, 718, 26, acc, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A BASE MUDOU", PURPLE)
    aa = ep(t, C["26.a"], 0.5)
    chip(c, "+20%", 760, 330, GREEN, aa, 52)
    chip(c, "depois −20%", 1160, 330, RED, aa * ep(t, C["26.a"] + 0.6, 0.4), 52)
    ab = ep(t, C["26.b"], 0.5)
    if ab > 0:
        ftext(c, "volta ao original?", W / 2, 470, 56, "black", INK, ab)
        selo(c, W / 2, 580, ep(t, C["26.b"] + 0.8, 0.4), "NÃO", RED, -4, 60)
    acc = ep(t, C["26.c"], 0.5)
    if acc > 0:
        text(c, "e que desconto desfaz um aumento?", W / 2, 690, 36, "black", AMBER, acc)
    pill(c, "ep. 4 · a base mudou", W / 2, 790, PURPLE, size=32, a=ep(t, C["26.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"], "Você já tinha somado dois descontos?",
        canal="no Estudativo", anki=C["27.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, salario=b_salario, regra=b_regra, bola=b_bola,
              ordem=b_ordem, descontos=b_descontos, potencia=b_potencia, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q3=b_q3, q6=b_q6, ponte=b_ponte, cta=b_cta)
