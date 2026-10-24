"""Visual — Grandezas Proporcionais, Episódio 1: a constante k (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: etiqueta() (R$/kg brilhando como o k), bolo() (os 240 km em fatias de 1 h), relogio() (0,4 h = 24 min).
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
_s = importlib.util.spec_from_file_location("comum022", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_grandezas_ep1_constante_k.mp4"
CARD_R = K.CARD_R
CARNE = "#C8553D"
BOLO = "#F3D9A4"
BOLO_BORDA = "#D9A55B"
FATIAS = ["#E8743B", "#F2A541", "#3E7BFA", "#16A36A", "#8B5CF6", "#D9468F"]


# ======================================================================
# peças do episódio
# ======================================================================

def etiqueta(c, x, y, a, linha1, linha2, glow=0.0, rot=-4, w=520, h=230, sub=None):
    """etiqueta de mercado (âmbar); (x, y) = canto superior esquerdo; glow = brilho verde no valor (o k)"""
    if a <= 0:
        return
    c.save(); c.translate(x + w / 2, y + h / 2); c.rotate(rot); c.translate(-(x + w / 2), -(y + h / 2))
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + w - 100, y); p.lineTo(x + w, y + h / 2); p.lineTo(x + w - 100, y + h)
    p.lineTo(x, y + h); p.close()
    c.drawPath(p, paint(AMBER, a)); c.drawCircle(x + w - 95, y + h / 2, 16, paint("#FFFFFF", a))
    text(c, linha1, x + (w - 100) / 2, y + 66, 30, "black", "#FFFFFF", a)
    if glow > 0:
        rrect(c, x + 30, y + 92, w - 160, 76, 18, GREEN, a * glow * 0.9)
    text(c, linha2, x + (w - 100) / 2, y + 150, 54, "black", "#FFFFFF", a)
    if sub:
        text(c, sub, x + (w - 100) / 2, y + 205, 24, "bold", "#FFFFFF", a)
    c.restore()


def bolo(c, x, y, w, h, n, a, prog=1.0, rotulo=None, hl=None):
    """o "bolo" de 240 km: uma faixa de largura w cortada em n fatias iguais (cada fatia = 1 hora de viagem)"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, BOLO, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), paint(BOLO_BORDA, a, stroke=6))
    fw_ = w / n
    vis = int(math.floor(prog * n + 1e-6))
    for k in range(n):
        ak = a * clamp(prog * n - k, 0, 1)
        if ak <= 0:
            continue
        col = FATIAS[k % len(FATIAS)]
        rrect(c, x + k * fw_ + 6, y + 6, fw_ - 12, h - 12, 16, col, ak * (0.85 if hl is None or hl == k else 0.35))
        text_mid(c, "1 h", x + k * fw_ + fw_ / 2, y + h / 2, 30, "black", "#FFFFFF", ak)
    if rotulo and vis > 0:
        text(c, rotulo, x + fw_ / 2, y + h + 44, 28, "black", INK2, a)


def relogio(c, cx, cy, r, minutos, a, col=GREEN, mostra_num=True):
    """relógio analógico com o setor de 0 até `minutos` pintado e o ponteiro dos minutos"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 10, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r + 10, paint(INK, a, stroke=8))
    if minutos > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, minutos / 60 * 360, False); p.close()
        c.drawPath(p, paint(col, a * 0.28))
    for k in range(60):
        ang = -math.pi / 2 + k * math.pi / 30
        big = k % 5 == 0
        r0 = r - (26 if big else 12)
        c.drawLine(cx + r0 * math.cos(ang), cy + r0 * math.sin(ang), cx + r * math.cos(ang), cy + r * math.sin(ang),
                   paint(INK if big else INK2, a * (1 if big else 0.5), stroke=5 if big else 2))
    if mostra_num:
        for k in (0, 15, 30, 45):
            ang = -math.pi / 2 + k * math.pi / 30
            text_mid(c, str(k), cx + (r - 58) * math.cos(ang), cy + (r - 58) * math.sin(ang), 30, "black", INK2, a)
    ang = -math.pi / 2 + minutos / 60 * 2 * math.pi
    c.drawLine(cx, cy, cx + (r - 30) * math.cos(ang), cy + (r - 30) * math.sin(ang), paint(col, a, stroke=10, cap_round=True))
    c.drawCircle(cx, cy, 12, paint(INK, a))


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A CONSTANTE k", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        card(c, 220, 220, 640, 420, aa)
        text(c, "REGRA DE TRÊS", 540, 290, 30, "black", INK2, aa)
        expr(c, "3/60 = 5/x", 540, 440, 76, aa, cores=mono("3/60 = 5/x", INK))
        text(c, "resolvia a proporção", 540, 590, 30, "bold", GRAY, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        arrow(c, 900, 430, 1080, 430, PURPLE, ab, 6, 18, progress=ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        card(c, 1110, 220, 600, 420, acc)
        text(c, "o número escondido", 1410, 290, 30, "black", INK2, acc)
        s = 1 + 0.08 * math.sin(math.pi * prog(t, C["01.c"] + 0.3, 0.6))
        c.save(); c.translate(1410, 440); c.scale(s, s); c.translate(-1410, -440)
        fmid(c, "k", 1410, 440, 220, "black", PURPLE, acc)
        c.restore()
    ad = ep(t, C["01.d"], 0.5)
    selo(c, W / 2, 760, ad, "QUALQUER PROBLEMA = UMA MULTIPLICAÇÃO", GREEN, -2, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "achar o k com UM par de valores", "um único par basta"),
            ("02.b", "montar a fórmula", "y = k · x   ou   y = k ÷ x"),
            ("02.c", "prever qualquer outro valor", "numa única conta")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "SÉRIE DE RAZÃO", 560, 250, GRAY, size=22, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "TESTE DO DOBRO", 560, 330, 40, "black", PURPLE, aa)
        ftext(c, "dobrou também?  →  DIRETA", 560, 450, 40, "black", GREEN, aa)
        ftext(c, "virou metade?  →  INVERSA", 560, 540, 40, "black", BLUE, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "SÉRIE DE FRAÇÕES", 1360, 250, GRAY, size=22, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "÷ FRAÇÃO = × FRAÇÃO VIRADA", 1360, 330, 36, "black", PURPLE, ab)
        expr(c, "5 ÷ 1/2 = 5 × 2 = 10", 1360, 490, 64, ab, cores={6: GREEN})
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)


# ======================================================================
# concreto — a etiqueta do mercado
# ======================================================================

COMPRAS = [("04.a", "1 kg", "R$ 20"), ("04.b", "2 kg", "R$ 40"), ("04.c", "3 kg", "R$ 60")]


def b_etiqueta(c, t, C, B):
    frame(c, t, B["start"], "NO MERCADO", "O NÚMERO QUE NÃO MUDA", BLUE)
    a0 = ep(t, C["04.a"], 0.5)
    ae = ep(t, C["04.e"], 0.5)
    etiqueta(c, 230, 270, a0, "CARNE", "R$ 20,00/kg", glow=ae)
    ad = ep(t, C["04.d"], 0.5)
    for k, (cue, kg, rs) in enumerate(COMPRAS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 150 + d
        card(c, 900, y, 760, 120, a)
        text(c, kg, 1010, y + 76, 40, "black", INK, a)
        text(c, rs, 1220, y + 76, 40, "black", CARNE, a)
        if ad > 0:
            num = rs.replace("R$ ", "")
            ftext(c, f"{num} ÷ {kg.split()[0]} =", 1460, y + 74, 32, "black", INK2, ad, align="right")
            text(c, "20", 1560, y + 76, 44, "black", GREEN, ad)
    if ae > 0:
        regra(c, "o preço muda, os quilos mudam… o 20 NÃO muda", W / 2, 790, ae, 34)


# ======================================================================
# bloco A — as duas constantes
# ======================================================================

def b_constante(c, t, C, B):
    head_seq(c, t, C, [("05", "GRANDEZA E CONSTANTE", "O QUE NÃO MUDA", BLUE), ("06", "DIRETA", "O QUOCIENTE É O k", PURPLE),
                       ("07", "INVERSA", "O PRODUTO É O k", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06", "07"])
    if sid == "05":
        a0 = ep(t, C["05"], 0.5)
        boxed(c, 260, 220, 640, 150, BLUE, a0, 0.08)
        text(c, "GRANDEZA", 580, 280, 36, "black", BLUE, a0)
        text(c, "o que dá para medir ou contar", 580, 330, 28, "bold", INK2, a0)
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            boxed(c, 1020, 220, 640, 150, BLUE, aa, 0.08)
            text(c, "QUOCIENTE", 1340, 280, 36, "black", BLUE, aa)
            text(c, "o resultado da divisão", 1340, 330, 28, "bold", INK2, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            ftext(c, "40 ÷ 2 = 20     60 ÷ 3 = 20     80 ÷ 4 = 20", W / 2, 500, 44, "black", INK, ab)
            text(c, "CONSTANTE: não muda nunca", W / 2, 580, 34, "black", GREEN, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            boxed(c, 460, 640, 1000, 150, PURPLE, acc, 0.08)
            text(c, "CONSTANTE DE PROPORCIONALIDADE", W / 2, 700, 34, "black", PURPLE, acc)
            fmid(c, "= k", W / 2, 755, 44, "black", PURPLE, acc)
        return
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        expr(c, "y/x = k", 640, 380, 130, aa, cores={2: PURPLE})
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            arrow(c, 900, 380, 1060, 380, PURPLE, ab, 5, 16, progress=ab)
            expr(c, "y = k · x", 1340, 380, 110, ab, cores={2: PURPLE})
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            etiqueta(c, 260, 540, acc, "ETIQUETA", "preço = 20 × kg", 0.0, -2, 700, 210)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            K.atalho(c, 1080, 560, 560, 200, "SERVE PARA", ["QUALQUER compra:", "5 kg → 20 × 5 = R$ 100"], ad, 30)
        return
    aa = ep(t, C["07.a"], 0.5)
    bolo(c, 260, 230, 700, 120, 4, aa, 1.0, None)
    text(c, "240 km", 610, 400, 34, "black", INK, aa)
    text(c, "mais rápido → menos tempo", 610, 450, 28, "bold", INK2, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        boxed(c, 1060, 220, 600, 150, BLUE, ab, 0.08)
        text(c, "PRODUTO", 1360, 280, 36, "black", BLUE, ab)
        text(c, "o resultado da multiplicação", 1360, 330, 28, "bold", INK2, ab)
    acc = ep(t, C["07.c"], 0.5)
    expr(c, "x · y = k", 500, 600, 100, acc, cores={4: PURPLE})
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        arrow(c, 760, 600, 880, 600, PURPLE, ad, 5, 16, progress=ad)
        expr(c, "y = k/x", 1060, 600, 100, ad, cores={2: PURPLE})
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1260, 470, 420, 300, "ATALHO", ["direta: DIVIDA", "inversa: MULTIPLIQUE", "o que dá sempre", "igual é o k"], ae, 28)


# ======================================================================
# bloco B — o k sempre significa algo
# ======================================================================

SIGN = [("08.a", "preço e quantidade", "direta", "preço por unidade", "R$/kg"),
        ("08.b", "distância e tempo", "direta", "velocidade", "km/h"),
        ("08.c", "massa e volume", "direta", "densidade", "g/cm³"),
        ("09.a", "velocidade e tempo", "inversa", "a distância", "km"),
        ("09.b", "operários e prazo", "inversa", "o total de trabalho", "pessoa·dia")]


def b_significa(c, t, C, B):
    head_seq(c, t, C, [("08", "O k NÃO É UM NÚMERO SOLTO", "ELE SIGNIFICA ALGO", BLUE), ("09", "NAS INVERSAS TAMBÉM", "O QUE ESSE NÚMERO SIGNIFICA?", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.4)
    text(c, "SITUAÇÃO", 420, 230, 24, "black", GRAY, a0)
    text(c, "RELAÇÃO", 830, 230, 24, "black", GRAY, a0)
    text(c, "O QUE É O k", 1300, 230, 24, "black", GRAY, a0)
    for k, (cue, sit, rel, sig, u) in enumerate(SIGN):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 92 + d
        rrect(c, 200, y - 40, 1520, 78, 16, "#F6F6F3" if k % 2 == 0 else "#FFFFFF", a)
        text(c, sit, 420, y + 12, 32, "black", INK, a)
        pill(c, rel, 830, y, GREEN if rel == "direta" else BLUE, size=24, a=a, anchor="center", bounds=(0, 1920))
        text(c, sig, 1240, y + 12, 34, "black", PURPLE, a)
        ftext(c, u, 1600, y + 10, 30, "black", INK2, a)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        regra(c, "achou o k? pergunte: o que esse número SIGNIFICA?", W / 2, 790, acc, 32)


# ======================================================================
# bloco C — achar o k com um par
# ======================================================================

def b_par(c, t, C, B):
    head_seq(c, t, C, [("10", "COMO ACHAR O k?", "UM PAR DE VALORES BASTA", PURPLE), ("11", "NA INVERSA", "O MESMO CAMINHO, MULTIPLICANDO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            chip(c, "y = 15 quando x = 5", 560, 260, BLUE, aa, 34)
            pill(c, "direta", 560, 330, GREEN, size=24, a=aa, anchor="center", bounds=(0, 1920))
        ab = ep(t, C["10.b"], 0.5)
        expr(c, "k = 15/5 = 3", 560, 480, 90, ab, cores={4: PURPLE})
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            boxed(c, 1050, 230, 560, 170, PURPLE, acc, 0.08)
            text(c, "A FÓRMULA", 1330, 290, 26, "black", PURPLE, acc)
            expr(c, "y = 3x", 1330, 350, 70, acc, cores=mono("y = 3x", PURPLE))
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            ftext(c, "x = 8  →  y = 3 · 8 = 24", 1330, 520, 48, "black", GREEN, ad)
            text(c, "qualquer valor: UMA multiplicação", 1330, 600, 28, "bold", INK2, ad)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        chip(c, "y = 6 quando x = 4", 560, 260, BLUE, aa, 34)
        pill(c, "inversa", 560, 330, BLUE, size=24, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["11.b"], 0.5)
    ftext(c, "k = 6 · 4 = 24", 560, 480, 80, "black", INK, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        boxed(c, 1050, 230, 560, 170, PURPLE, acc, 0.08)
        text(c, "A FÓRMULA", 1330, 290, 26, "black", PURPLE, acc)
        expr(c, "y = 24/x", 1330, 350, 64, acc, cores=mono("y = 24/x", PURPLE))
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        ftext(c, "x = 8  →  y = 24 ÷ 8 = 3", 1330, 500, 48, "black", GREEN, ad)
    ae = ep(t, C["11.e"], 0.5)
    if ae > 0:
        K.atalho(c, 300, 590, 1320, 200, "ATALHO", ["UM PAR BASTA:  ache o k  →  escreva a fórmula  →  acabou"], ae, 36)


# ======================================================================
# bloco D — direta na prática: o combustível
# ======================================================================

VIAG = [("12.a", "180 km", "15 L", "15/180"), ("12.b", "360 km", "30 L", "30/360"), ("12.c", "540 km", "45 L", "45/540")]


def _bomba(c, x, y, a, s=1.0):
    rrect(c, x, y, 90 * s, 150 * s, 14, GREEN, a)
    rrect(c, x + 14 * s, y + 18 * s, 62 * s, 42 * s, 8, "#FFFFFF", a)
    p = skia.Path(); p.moveTo(x + 88 * s, y + 40 * s); p.quadTo(x + 130 * s, y + 40 * s, x + 124 * s, y + 100 * s)
    p.lineTo(x + 124 * s, y + 120 * s)
    c.drawPath(p, paint(INK, a, stroke=6, cap_round=True))
    rrect(c, x - 14 * s, y + 150 * s, 120 * s, 14 * s, 6, INK, a)


def b_combustivel(c, t, C, B):
    head_seq(c, t, C, [("12", "DIRETA NA VIDA REAL", "O COMBUSTÍVEL", BLUE), ("13", "O k DO COMBUSTÍVEL", "LITROS ÷ QUILÔMETROS", PURPLE),
                       ("14", "E COMO SE USA?", "LITROS = k × DISTÂNCIA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14"])
    _bomba(c, 230, 260, ep(t, C["12"], 0.5))
    for k, (cue, km, L, q) in enumerate(VIAG):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 120 + d
        card(c, 430, y, 560, 100, a)
        text(c, km, 560, y + 64, 40, "black", INK, a)
        fmid(c, "→", 700, y + 50, 40, "black", GRAY, a)
        text(c, L, 830, y + 64, 40, "black", GREEN, a)
        if sid == "13":
            cue2 = ["13.a", "13.b", "13.c"][k]
            a2 = ep(t, C[cue2], 0.5)
            if a2 > 0:
                expr(c, f"{q} = 1/12", 1260, y + 50, 50, a2, cores={2: PURPLE})
    if sid == "12":
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            selo(c, 1330, 360, ad, "TESTE DO DOBRO: DIRETA", GREEN, -4, 32)
            text(c, "dobro de km → dobro de litros", 1330, 460, 30, "bold", INK2, ad)
        ae = ep(t, C["12.e"], 0.5)
        if ae > 0:
            regra(c, "direta? DIVIDA: litros ÷ quilômetros", W / 2, 720, ae, 34)
        return
    if sid == "13":
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            boxed(c, 300, 640, 1320, 150, PURPLE, ad, 0.08)
            expr(c, "k = 1/12", 600, 715, 64, ad, cores={2: PURPLE})
            text(c, "litro por quilômetro", 1060, 700, 36, "black", PURPLE, ad)
            text(c, "cada km gasta 1/12 de litro", 1060, 750, 28, "bold", INK2, ep(t, C["13.e"], 0.5))
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        expr(c, "litros = 1/12 × km", 1300, 300, 54, aa, cores={2: PURPLE})
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        K.atalho(c, 1060, 380, 560, 160, "ATALHO", [("m", "× 1/12 = ÷ 12")], ab, 40)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        ftext(c, "120 km ÷ 12 = 10 L", 710, 680, 52, "black", GREEN, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 1060, 600, 560, 170, 18, "#F6F6F3", ad)
        text(c, "o 12 do painel:", 1340, 650, 28, "bold", INK2, ad)
        text(c, "12 km/L", 1340, 715, 52, "black", BLUE, ad)
        text(c, "o mesmo k, de cabeça para baixo", 1340, 760, 22, "bold", INK2, ad)


def b_sequencia(c, t, C, B):
    frame(c, t, B["start"], "LISTAS INTEIRAS", "SEQUÊNCIAS PROPORCIONAIS", BLUE)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 460, 220, 1000, 100, BLUE, aa, 0.08)
        text_mid(c, "SEQUÊNCIA = lista de números em ordem", W / 2, 270, 34, "black", BLUE, aa)
    A_ = ["2", "3", "5"]
    B_ = ["6", "9", "15"]
    ab, acc, ad = ep(t, C["15.b"], 0.5), ep(t, C["15.c"], 0.5), ep(t, C["15.d"], 0.5)
    for k in range(3):
        x = 620 + k * 340
        card(c, x - 120, 380, 240, 110, ab)
        text(c, A_[k], x, 455, 56, "black", INK, ab)
        card(c, x - 120, 520, 240, 110, acc)
        text(c, B_[k], x, 595, 56, "black", BLUE, acc)
        ak = ep(t, C["15.d"] + 0.5 * k, 0.4)
        if ak > 0:
            ftext(c, f"{B_[k]} ÷ {A_[k]} = 3", x, 690, 36, "black", GREEN, ak)
    text(c, "1ª", 400, 455, 30, "black", GRAY, ab)
    text(c, "2ª", 400, 595, 30, "black", GRAY, acc)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        regra(c, "sequências DIRETAMENTE proporcionais, com k = 3", W / 2, 790, ae, 34)


# ======================================================================
# bloco E — inversa na prática: o bolo de 240 km
# ======================================================================

FAT = [("16.a", 6, "40 km/h", "6 h", "40 × 6"), ("16.b", 4, "60 km/h", "4 h", "60 × 4"), ("16.c", 3, "80 km/h", "3 h", "80 × 3")]


def b_bolo(c, t, C, B):
    head_seq(c, t, C, [("16", "A VIAGEM DE 240 km", "UM BOLO DE TAMANHO FIXO", BLUE), ("17", "MULTIPLIQUE CADA PAR", "O k DA INVERSA", PURPLE),
                       ("18", "A FÓRMULA PREVÊ", "QUALQUER VELOCIDADE", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["16", "17", "18"])
    if sid in ("16", "17"):
        for k, (cue, n, v, tt, prod) in enumerate(FAT):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 230 + k * 170
            text(c, v, 330, y + 70, 36, "black", INK, a)
            bolo(c, 470, y + 10, 900, 100, n, a, ep(t, C[cue] + 0.2, 1.2))
            text(c, tt, 1450, y + 72, 44, "black", BLUE, a)
            if sid == "17":
                ak = ep(t, C[["17.a", "17.b", "17.c"][k]], 0.5)
                if ak > 0:
                    ftext(c, f"{prod} = 240", 1640, y + 70, 30, "black", GREEN, ak)
        if sid == "16":
            text(c, "240 km: o bolo inteiro não muda", W / 2, 790, 32, "black", INK2, ep(t, C["16"], 0.5))
            return
        ad = ep(t, C["17.d"], 0.5)
        if ad > 0:
            boxed(c, 300, 720, 760, 100, PURPLE, ad, 0.08)
            text_mid(c, "k = 240 = a própria DISTÂNCIA", 680, 770, 34, "black", PURPLE, ad)
        ae = ep(t, C["17.e"], 0.5)
        if ae > 0:
            K.atalho(c, 1100, 700, 560, 130, "ATALHO", ["o k é o que fica FIXO"], ae, 32)
        return
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        expr(c, "tempo = 240/velocidade", W / 2, 320, 70, aa, cores={2: PURPLE})
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        bolo(c, 360, 450, 1200, 110, 2, ab, ep(t, C["18.b"], 1.0))
        ftext(c, "120 km/h  →  240 ÷ 120 = 2 h", W / 2, 640, 48, "black", GREEN, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 760, acc, "DOBRO DA VELOCIDADE (60 → 120) = METADE DO TEMPO (4 → 2)", GREEN, -2, 28)


# ======================================================================
# bloco F — a ponte: y inversa de x = y direta de 1/x
# ======================================================================

def b_ponte1x(c, t, C, B):
    frame(c, t, B["start"], "UMA CURIOSIDADE", "INVERSA DE x = DIRETA DE 1/x", PURPLE)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 230, 620, 180, BLUE, aa, 0.08)
        text(c, "INVERSO de um número", 610, 290, 32, "black", BLUE, aa)
        expr(c, "4 → 1/4", 610, 360, 54, aa, cores={2: BLUE})
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        expr(c, "t = 240/v = 240 · 1/v", 1340, 320, 60, ab, cores={4: PURPLE})
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        boxed(c, 300, 520, 1320, 230, PURPLE, acc, 0.06)
        text(c, "y INVERSA de x", 620, 620, 44, "black", BLUE, acc)
        fmid(c, "=", 900, 605, 60, "black", INK2, acc)
        text(c, "y DIRETA de", 1140, 620, 44, "black", GREEN, acc)
        expr(c, "1/x", 1380, 605, 60, acc, cores={0: GREEN})
        text(c, "a mesma relação, vista por outro ângulo", W / 2, 710, 28, "bold", INK2, acc)


# ======================================================================
# bloco G — o relógio não é decimal
# ======================================================================

def b_relogio(c, t, C, B):
    head_seq(c, t, C, [("20", "CUIDADO", "O RELÓGIO NÃO É DECIMAL", AMBER), ("21", "O MAIS FAMOSO", "0,4 h NÃO É 40 min", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["20", "21"])
    if sid == "20":
        aa = ep(t, C["20.a"], 0.5)
        if aa > 0:
            ftext(c, "240 ÷ 150 = 1,6 h", 520, 290, 56, "black", INK, aa)
        ab = ep(t, C["20.b"], 0.5)
        if ab > 0:
            ftext(c, "1 h 60 min?", 520, 420, 52, "black", RED, ab)
            strike(c, 380, 405, 660, 405, ab, RED, ep(t, C["20.b"] + 0.5, 0.4))
        acc = ep(t, C["20.c"], 0.5)
        if acc > 0:
            text(c, "1 hora = 60 minutos, não 100", 520, 540, 32, "black", AMBER, acc)
        ad = ep(t, C["20.d"], 0.5)
        if ad > 0:
            ftext(c, "0,6 × 60 = 36 min", 520, 660, 52, "black", GREEN, ad)
            ftext(c, "1,6 h = 1 h 36 min", 520, 750, 44, "black", GREEN, ad)
        m = 36 * ep(t, C["20.d"], 1.4)
        relogio(c, 1280, 490, 230, m, ep(t, C["20"], 0.5))
        if ad > 0:
            text(c, f"{int(round(m))} min", 1280, 800, 40, "black", GREEN, ad)
        return
    aa = ep(t, C["21.a"], 0.5)
    if aa > 0:
        ftext(c, "0,4 h = 40 min?", 520, 300, 56, "black", RED, aa)
        strike(c, 330, 285, 710, 285, aa, RED, ep(t, C["21.a"] + 0.8, 0.4))
    ab = ep(t, C["21.b"], 0.5)
    if ab > 0:
        ftext(c, "0,4 × 60 = 24 min", 520, 440, 56, "black", GREEN, ab)
    acc = ep(t, C["21.c"], 0.5)
    if acc > 0:
        K.atalho(c, 220, 520, 600, 260, "ATALHO", ["cada DÉCIMO de hora", "= 6 minutos", "0,4 → 4 × 6 = 24"], acc, 32)
    m = 24 * ep(t, C["21.b"], 1.4)
    a0 = ep(t, C["21"], 0.5)
    relogio(c, 1280, 470, 230, m, a0)
    if a0 > 0 and t < C["21.b"]:
        # o "fantasma" dos 40 minutos, para mostrar o tamanho do erro
        ang = -math.pi / 2 + 40 / 60 * 2 * math.pi
        c.drawLine(1280, 470, 1280 + 200 * math.cos(ang), 470 + 200 * math.sin(ang), paint(RED, aa * 0.6, stroke=8, cap_round=True))
        text(c, "40 min", 1280, 800, 40, "black", RED, aa)
    if ab > 0:
        text(c, f"{int(round(m))} min", 1280, 800, 40, "black", GREEN, ab)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("22", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("23", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["22.a"], 0.5)
    etiqueta(c, 230, 260, aa, "PRODUTO", "R$ 36 por 4 kg", 0.0, -3, 680, 230)
    q = [("22.b", "1.  Qual é o k?", "23.a", "36 ÷ 4 = 9  →  k = R$ 9/kg"), ("22.c", "2.  Quanto custam 7 kg?", "23.c", "9 × 7 = R$ 63")]
    for j, (cue, s, rc, r) in enumerate(q):
        a = ep(t, C[cue], 0.5)
        y = 300 + j * 210
        text(c, s, 1000, y, 40, "black", INK, a, align="left")
        if t >= C["23"]:
            ra = ep(t, C[rc], 0.5)
            ftext(c, r, 1000, y + 80, 42, "black", GREEN, ra, align="left")
    if t >= C["23"]:
        ab = ep(t, C["23.b"], 0.5)
        if ab > 0:
            boxed(c, 230, 600, 680, 130, PURPLE, ab, 0.08)
            ftext(c, "preço = 9 × kg", 570, 682, 48, "black", PURPLE, ab)
    pause_timer(c, t, C["22.end"] - 1.9, 570, 680)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Direta: o quociente não muda. Inversa: o produto não muda.", "Um par de valores basta para achar o k.",
          "Décimo de hora não é minuto: multiplique por 60."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["24", "34"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "24" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 58)


ERROS = [("Quociente na inversa (ou produto na direta)", "as duas contas sempre dão algum número",
          "só a certa dá SEMPRE o mesmo número: faça o teste do dobro antes"),
         ("Ler 2,4 h como 2 h 40 min", "o 4 está ali, logo depois da vírgula",
          "a hora tem 60 minutos: 0,4 × 60 = 24 → 2 h 24 min"),
         ("Tratar o k como letra sem significado", "na fórmula ele é só uma letra",
          "o k é o preço por quilo, a velocidade, a distância… muitas vezes, é a própria resposta")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["25", "26", "27"], ERROS)


# ======================================================================
# Questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=32, w=680):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS2 = [("A", "18 litros", "cresce pouco demais", RED), ("B", "20 litros", "fez 300 ÷ 15", RED),
         ("C", "25 litros", "", GREEN), ("D", "30 litros", "dobrou: 300 não é 2 × 180", RED),
         ("E", "36 litros", "mais que dobra", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ACHAR O k E PREVER", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    _enunciado(c, [("O consumo de combustível de um automóvel é diretamente proporcional à distância percorrida. Em um trajeto "
                    "de 180 km, o veículo consumiu 15 litros.", INK),
                   ("Mantidas as condições, o consumo em um trajeto de 300 km será de", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ABDE"}
    if t >= C["28.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS2, 1000, 230, 680, 40, C["29.ok"], "C", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["28.end"] - 1.9, 470, 680)
    if t >= C["29"]:
        ra = ep(t, C["29"], 0.4)
        rrect(c, 170, 500, 740, 310, 18, "#FFFFFF", ra, shadow=True)
        text(c, "DIRETA → o quociente é o k", 540, 555, 28, "black", PURPLE, ep(t, C["29.a"], 0.4))
        expr(c, "k = 15/180 = 1/12", 540, 630, 46, ep(t, C["29.b"], 0.4), cores={4: PURPLE})
        ftext(c, "300 ÷ 12 = 25 L", 540, 720, 44, "black", GREEN, ep(t, C["29.c"], 0.4))
        ftext(c, "km × 1,7  →  litros × 1,7 ✓", 540, 785, 28, "black", AMBER, ep(t, C["29.d"], 0.4))


ALTS3 = [("A", "2 h 24 min", "", GREEN), ("B", "2 h 40 min", "leu 2,4 como 2 h 40", RED), ("C", "2 h 50 min", "não sai da conta", RED),
         ("D", "3 h 45 min", "tratou como direta", RED), ("E", "3 h 75 min", "direta + 75 minutos", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · RELAÇÃO INVERSA", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["31.a"], 0.4)
    _enunciado(c, [("Um motorista percorre determinado trajeto em 3 horas, mantendo velocidade média de 80 km/h.", INK),
                   ("Se aumentar a velocidade média para 100 km/h, o mesmo trajeto será percorrido em", BLUE)], a0, 240, 30, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"31.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"33.x{L.lower()}"] for L in "BCDE"}
    if t >= C["31.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS3, 1000, 230, 680, 40, C["32.ok"], "A", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["31.end"] - 1.9, 470, 680)
    if t >= C["32"]:
        ra = ep(t, C["32"], 0.4)
        rrect(c, 170, 470, 740, 340, 18, "#FFFFFF", ra, shadow=True)
        text(c, "INVERSA → o produto é o k", 540, 525, 28, "black", PURPLE, ep(t, C["32.a"], 0.4))
        ftext(c, "k = 80 × 3 = 240 km", 540, 595, 42, "black", PURPLE, ep(t, C["32.b"], 0.4))
        ftext(c, "240 ÷ 100 = 2,4 h", 540, 665, 42, "black", INK, ep(t, C["32.c"], 0.4))
        ftext(c, "0,4 × 60 = 24 min", 540, 735, 42, "black", GREEN, ep(t, C["32.d"], 0.4))
        ftext(c, "2 h 24 < 3 h ✓", 540, 795, 28, "black", AMBER, ep(t, C["32.ok"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A TABELA", PURPLE)
    aa = ep(t, C["35.a"], 0.5)
    linhas = [("x", "y"), ("3", "40"), ("5", "24"), ("8", "15")]
    for k, (x, y) in enumerate(linhas):
        a = aa * ep(t, C["35.a"] + 0.2 * k, 0.4)
        if a <= 0:
            continue
        yy = 250 + k * 100
        rrect(c, 640, yy, 640, 86, 12, "#EEF3FE" if k == 0 else "#FFFFFF", a, shadow=k > 0)
        text(c, x, 800, yy + 58, 40, "black", BLUE if k == 0 else INK, a)
        text(c, y, 1120, yy + 58, 40, "black", BLUE if k == 0 else INK, a)
    ab = ep(t, C["35.b"], 0.5)
    if ab > 0:
        chip(c, "÷ ?", 500, 450, GREEN, ab, 40)
        chip(c, "× ?", 1420, 450, BLUE, ab, 40)
        text(c, "DUAS contas resolvem qualquer tabela", W / 2, 700, 36, "black", PURPLE, ab)
    pill(c, "ep. 2 · reconhecer na tabela", W / 2, 790, PURPLE, size=32, a=ep(t, C["35.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["36.like"], C["36.sub"], C["36.bell"], C["36.com"], C["36.bye"], "Já leu 2,4 h como 2 h 40 min?",
        canal="no Estudativo", anki=C["36.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, etiqueta=b_etiqueta, constante=b_constante,
              significa=b_significa, par=b_par, combustivel=b_combustivel, sequencia=b_sequencia, bolo=b_bolo,
              ponte1x=b_ponte1x, relogio=b_relogio, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2,
              q3=b_q3, ponte=b_ponte, cta=b_cta)
