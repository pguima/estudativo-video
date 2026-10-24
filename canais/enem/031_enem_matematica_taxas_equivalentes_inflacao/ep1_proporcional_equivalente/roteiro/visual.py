"""Visual — Taxas Equivalentes e Inflação, Episódio 1: proporcional × equivalente, trocar o período de uma taxa (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: grafico() (reta tracejada 2% por mês × curva 1,02 por mês, com a faixa "juro sobre juro"),
maquina() (taxa → fator → potência → tesoura no "1," → taxa), tesoura(), anuncio() (propaganda de banco), linha().
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
_s = importlib.util.spec_from_file_location("comum031", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_taxas_ep1_proporcional_equivalente.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def tesoura(c, cx, cy, s, a, abre=0.5, col=None):
    """tesoura com a ponta para a ESQUERDA; abre = 0 (fechada) a 1 (aberta)"""
    if a <= 0:
        return
    col = col or GREEN
    ang = 6 + 16 * clamp(abre)
    for sg in (-1, 1):
        c.save(); c.translate(cx, cy); c.rotate(sg * ang)
        p = skia.Path()
        p.moveTo(0, -s * 0.07); p.quadTo(-s * 0.55, -s * 0.09, -s * 0.95, 0); p.quadTo(-s * 0.55, s * 0.03, 0, s * 0.05)
        p.close()
        c.drawPath(p, paint("#C9CED6", a))
        c.drawPath(p, paint("#7D8590", a, stroke=2))
        c.drawCircle(s * 0.42, sg * s * 0.10, s * 0.17, paint(col, a, stroke=s * 0.07))
        line(c, 0, 0, s * 0.27, sg * s * 0.07, col, a, s * 0.07)
        c.restore()
    c.drawCircle(cx, cy, s * 0.05, paint(INK, a))


def corta_um(c, fator, taxa, cx, cy, size, a, u):
    """o fator (ex.: '1,268') perde o '1,' na tesoura (u 0 → 1) e vira a taxa (ex.: '26,8%')"""
    if a <= 0:
        return
    w1 = ftext_w("1,", "black", size)
    wr = ftext_w(fator[2:], "black", size)
    x0 = cx - (w1 + wr) / 2
    cut = ease_io(clamp((u - 0.25) / 0.35))
    fim = ease_io(clamp((u - 0.65) / 0.35))
    # o "1," cai
    ftext(c, "1,", x0, cy + size * 0.36 + cut * size * 1.2, size, "black", mix(INK, RED, cut), a * (1 - cut))
    # o resto vira a taxa
    if fim < 1:
        ftext(c, fator[2:], x0 + w1, cy + size * 0.36, size, "black", INK, a * (1 - fim), align="left")
    if fim > 0:
        fmid(c, taxa, cx, cy, size, "black", GREEN, a * fim)
    if 0 < u < 0.7:
        ab = abs(math.sin(u * math.pi * 6))
        tesoura(c, x0 + w1 + size * 0.55, cy - size * 0.95, size * 1.0, a * ep(u, 0, 0.1) * (1 - prog(u, 0.6, 0.1)), ab)


def anuncio(c, x, y, w, h, banco, taxa, periodo, col, a):
    """cartaz de propaganda de banco"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 26, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 70, 26, col, a)
    c.drawRect(skia.Rect.MakeXYWH(x, y + 44, w, 26), paint(col, a))
    text_mid(c, banco, x + w / 2, y + 36, 28, "black", "#FFFFFF", a)
    text(c, "RENDE", x + w / 2, y + 130, 26, "black", GRAY, a, tracking=3)
    text_mid(c, taxa, x + w / 2, y + 210, 92, "black", INK, a)
    text(c, periodo, x + w / 2, y + 300, 38, "black", col, a)


GX, GY, GW, GH = 280, 240, 1060, 520    # área do gráfico (eixo x = meses 0..12; eixo y = 0..28%)


def gx(m):
    return GX + GW * m / 12


def gy(p):
    return GY + GH - GH * p / 28


def grafico(c, a, ur=1.0, uc=1.0, faixa=0.0, rot=True):
    """reta tracejada (proporcional, 2% por mês) × curva (equivalente, × 1,02 por mês); ur/uc = quanto já foi desenhado"""
    if a <= 0:
        return
    line(c, GX, GY + GH, GX + GW + 30, GY + GH, INK2, a, 3)
    line(c, GX, GY + GH, GX, GY - 20, INK2, a, 3)
    for m in (0, 3, 6, 9, 12):
        text(c, str(m), gx(m), GY + GH + 38, 24, "bold", GRAY, a)
    text(c, "meses", GX + GW + 10, GY + GH + 76, 24, "bold", GRAY, a, align="right")
    for p in (0, 10, 20):
        text(c, f"{p}%", GX - 20, gy(p) + 8, 22, "bold", GRAY, a, align="right")
        line(c, GX, gy(p), GX + GW, gy(p), "#ECECE8", a, 2)
    N = 60
    if faixa > 0:
        pf = skia.Path()
        pts_r = [(gx(12 * k / N), gy(2 * 12 * k / N)) for k in range(N + 1)]
        pts_c = [(gx(12 * k / N), gy((1.02 ** (12 * k / N) - 1) * 100)) for k in range(N + 1)]
        pf.moveTo(*pts_r[0])
        for q in pts_r[1:]:
            pf.lineTo(*q)
        for q in reversed(pts_c):
            pf.lineTo(*q)
        pf.close()
        c.drawPath(pf, paint(AMBER, a * faixa * 0.35))
    # reta (proporcional)
    if ur > 0:
        line(c, gx(0), gy(0), gx(12 * ur), gy(24 * ur), PURPLE, a, 5, dash=(16, 12))
    # curva (equivalente)
    if uc > 0:
        pc = skia.Path(); pc.moveTo(gx(0), gy(0))
        for k in range(1, int(N * uc) + 1):
            m = 12 * k / N
            pc.lineTo(gx(m), gy((1.02 ** m - 1) * 100))
        c.drawPath(pc, paint(GREEN, a, stroke=6, cap_round=True))
    if rot and ur >= 1:
        pill(c, "24% (soma 2% por mês)", gx(12) + 30, gy(24) + 22, PURPLE, size=22, a=a)
    if rot and uc >= 1:
        pill(c, "26,8% (× 1,02 por mês)", gx(12) + 30, gy(26.8) - 22, GREEN, size=22, a=a)
    if faixa > 0:
        pill(c, "JURO SOBRE JURO", gx(9.4), gy(22.5), AMBER, size=22, a=a * faixa, anchor="center")


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def maquina(c, t, t0, y, a, taxa="2% a.m.", fator="1,02", pot="1,02^{12}", res="1,268", fim="26,8% a.a."):
    """a máquina de fatores: taxa → fator → potência → tesoura no '1,' → taxa"""
    if a <= 0:
        return
    xs = [330, 760, 1190, 1590]
    tit = ["TAXA", "FATOR", "ELEVE", "TIRE O 1"]
    cols = [BLUE, PURPLE, PURPLE, GREEN]
    for k in range(4):
        ak = a * ep(t, t0 + k * 0.9, 0.4)
        if ak <= 0:
            continue
        rrect(c, xs[k] - 175, y - 110, 350, 220, 22, "#FFFFFF", ak, shadow=True)
        rrect(c, xs[k] - 175, y - 110, 350, 48, 22, cols[k], ak * 0.16)
        text(c, tit[k], xs[k], y - 76, 22, "black", cols[k], ak, tracking=2)
        if k == 0:
            fmid(c, taxa, xs[k], y + 20, 50, "black", INK, ak)
        elif k == 1:
            fmid(c, fator, xs[k], y + 20, 60, "black", INK, ak)
            text(c, "1 + taxa", xs[k], y + 86, 22, "bold", GRAY, ak)
        elif k == 2:
            expr(c, pot, xs[k], y + 20, 54, ak)
            text(c, "= " + res, xs[k], y + 86, 26, "black", INK2, ak)
        else:
            corta_um(c, res, fim.split(" ")[0], xs[k], y + 14, 56, ak, ep(t, t0 + 3 * 0.9 + 0.3, 1.6))
            text(c, fim.split(" ", 1)[1] if " " in fim else "", xs[k], y + 86, 24, "black", GREEN,
                 ak * ep(t, t0 + 3 * 0.9 + 1.6, 0.4))
        if k < 3:
            arrow(c, xs[k] + 180, y, xs[k + 1] - 180, y, AMBER, a * ep(t, t0 + k * 0.9 + 0.5, 0.4), 5, 16)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "TAXAS EQUIVALENTES E INFLAÇÃO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 240, 1200, 150, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("10% ao mês  =  ", INK), ("? ao ano", PURPLE)], W / 2, 315, 72, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        linha(c, [("10% × 12 = ", INK2), ("120%", RED)], 600, 520, 64, ab)
        strike(c, 420, 520, 790, 500, ep(t, C["01.c"], 0.5), RED, ep(t, C["01.c"], 0.5))
        pill(c, "errou por quase 100 pontos", 600, 610, RED, size=26, a=ab, anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        expr(c, "1,1^{12} ≈ 3,14", 1330, 500, 64, acc)
        linha(c, [("≈ ", INK2), ("214% ao ano", GREEN)], 1330, 600, 60, ep(t, C["01.c"] + 1.0, 0.4))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 760, ad, "ROTATIVO DO CARTÃO: 3 DÍGITOS AO ANO", AMBER, -2, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "converter de MENSAL para ANUAL", "2% a.m.  →  26,8% a.a."),
            ("02.b", "e de ANUAL para SEMESTRAL", "44% a.a.  →  ? a.s."),
            ("02.c", "sem multiplicar nem dividir", "pelo número de períodos")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN if j < 2 else AMBER, "check" if j < 2 else "x")
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "JUROS SIMPLES", 560, 280, 32, "black", PURPLE, aa, tracking=2)
        text(c, "taxa proporcional", 560, 324, 24, "bold", GRAY, aa)
        linha(c, [("2% a.m. × 12 = ", INK), ("24% a.a.", PURPLE)], 560, 470, 56, aa)
    line(c, 960, 240, 960, 760, "#E6E6E2", aa, 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "JUROS COMPOSTOS", 1370, 280, 32, "black", PURPLE, ab, tracking=2)
        fmid(c, "M = C · (1 + i)ᵗ", 1370, 420, 64, "black", INK, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        expr(c, "1,1^2 = 1,21", 1370, 560, 52, acc)
        expr(c, "1,1^3 = 1,331", 1370, 670, 52, ep(t, C["03.c"] + 2.0, 0.4))


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS PROPAGANDAS", "QUAL RENDE MAIS?", BLUE)
    card(c, *CARD_R)
    anuncio(c, 230, 220, 560, 340, "BANCO A", "2%", "AO MÊS", BLUE, ep(t, C["04.a"], 0.5))
    anuncio(c, 870, 220, 560, 340, "BANCO B", "26,8%", "AO ANO", GREEN, ep(t, C["04.b"], 0.5))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        text_mid(c, "?", 1580, 390, 160, "black", AMBER, acc * (1 - ep(t, C["04.d"], 0.3)))
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        text_mid(c, "=", 830, 390, 90, "black", GREEN, ad)
        selo(c, 1560, 390, ad, "A MESMA COISA", GREEN, -6, 36)
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        rrect(c, 230, 610, 1200, 170, 22, PAPEL, ae, shadow=True)
        text(c, "FATURA DO CARTÃO", 400, 660, 24, "black", GRAY, ae, tracking=2)
        linha(c, [("rotativo: ", INK), ("9,9% ao mês", RED)], 830, 720, 48, ae)
        pill(c, "parece pequena...", 1560, 700, AMBER, size=28, a=ae, anchor="center")


def b_definicao(c, t, C, B):
    frame(c, t, B["start"], "AS PALAVRAS", "TAXA E PERÍODO", BLUE)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 220, 700, 170, 22, mix("#FFFFFF", BLUE, 0.08), aa)
        text(c, "TAXA", 570, 280, 40, "black", BLUE, aa)
        text(c, "quanto o dinheiro cresce (em %)", 570, 340, 28, "bold", INK2, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 220, 700, 170, 22, mix("#FFFFFF", BLUE, 0.08), ab)
        text(c, "PERÍODO", 1350, 280, 40, "black", BLUE, ab)
        text(c, "o tempo em que a taxa vale", 1350, 340, 28, "bold", INK2, ab)
    acc = ep(t, C["05.c"], 0.5)
    for k, (ab_, s_) in enumerate((("a.m.", "ao mês"), ("a.s.", "ao semestre (6 meses)"), ("a.a.", "ao ano"))):
        ak = acc * ep(t, C["05.c"] + k * 0.9, 0.4)
        if ak > 0:
            x = 380 + k * 580
            chip(c, ab_, x, 500, PURPLE, ak, 54)
            text(c, s_, x, 590, 28, "black", INK2, ak)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        regra(c, "hoje: TROCAR O PERÍODO de uma taxa", W / 2, 720, ad, 38, PURPLE)


# ======================================================================
# bloco a — proporcional × equivalente (o gráfico)
# ======================================================================

def b_formas(c, t, C, B):
    head_seq(c, t, C, [("06", "JEITO 1", "TAXA PROPORCIONAL", BLUE), ("07", "JEITO 2", "TAXA EQUIVALENTE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 230, 1400, 230, 24, mix("#FFFFFF", BLUE, 0.07), aa)
            text(c, "PROPORCIONAL: multiplica ou divide pelo nº de períodos", W / 2, 300, 36, "black", BLUE, aa)
            linha(c, [("2% a.m. × 12 = ", INK), ("24% a.a.", PURPLE)], W / 2, 400, 60, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            rrect(c, 260, 520, 1400, 220, 24, "#FFFFFF", ab, shadow=True)
            text(c, "CERTA nos JUROS SIMPLES", W / 2, 590, 38, "black", GREEN, ab)
            text(c, "juros calculados sempre sobre o valor do começo", W / 2, 660, 30, "bold", INK2, ab)
        return
    aa = ep(t, C["07.a"], 0.5)
    pill(c, "EQUIVALENTE = certa nos JUROS COMPOSTOS: juro também rende juro", W / 2, 205, GREEN, size=24, a=aa,
         anchor="center")
    ab = ep(t, C["07.b"], 0.4)
    ur = ep(t, C["07.b"] + 0.6, 2.2)
    uc = ep(t, C["07.c"] + 0.4, 2.4)
    grafico(c, ab, ur, uc, ep(t, C["07.d"], 0.8))


# ======================================================================
# bloco b — mesmo destino
# ======================================================================

def b_mesmo(c, t, C, B):
    head(c, t, B["start"], "EQUIVALENTE", "MESMO DESTINO, CAMINHOS DIFERENTES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        for k, s_ in enumerate(("mesmo CAPITAL", "mesmo PRAZO", "mesmo MONTANTE")):
            chip(c, s_, 470 + k * 490, 250, BLUE, aa * ep(t, C["08.a"] + k * 0.7, 0.4), 34)
    rows = [("08.b", "2% a.m. por 12 meses", "R$ 100 × 1,02¹²", "≈ R$ 126,80", GREEN, True),
            ("08.c", "26,8% a.a. por 1 ano", "R$ 100 × 1,268", "= R$ 126,80", GREEN, True),
            ("08.d", "24% a.a. por 1 ano", "R$ 100 × 1,24", "= R$ 124,00", RED, False)]
    for k, (cue, cam, conta, res, col, ok) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 390 + k * 135 + d
        rrect(c, 220, y - 55, 1480, 110, 18, "#FFFFFF", a, shadow=True)
        ftext(c, cam, 260, y + 12, 34, "black", INK, a, align="left")
        ftext(c, conta, 860, y + 12, 32, "bold", INK2, a, align="left")
        ftext(c, res, 1270, y + 12, 40, "black", col, a, align="left")
        check_icon(c, 1640, y, 26, a, col, "check" if ok else "x")
    ad = ep(t, C["08.d"] + 2.4, 0.5)
    if ad > 0:
        pill(c, "outro destino: 24% a.a. NÃO é equivalente a 2% a.m.", W / 2, 790, RED, size=26, a=ad, anchor="center")


# ======================================================================
# bloco c — o fator, a fórmula, a tabela e o atalho
# ======================================================================

def b_fator(c, t, C, B):
    head(c, t, B["start"], "O FATOR", "1 + TAXA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        regra(c, "FATOR = 1 + taxa (em decimal)", W / 2, 240, aa, 40, BLUE)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        linha(c, [("2%  →  ", INK2), ("1,02", PURPLE)], 640, 360, 60, ab)
        linha(c, [("44%  →  ", INK2), ("1,44", PURPLE)], 1280, 360, 60, ep(t, C["09.b"] + 1.6, 0.4))
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        pill(c, "FATOR PRIMEIRO, TAXA DEPOIS", W / 2, 470, PURPLE, size=28, a=acc, anchor="center")
        maquina(c, t, C["09.c"] + 0.6, 660, acc)


def b_formula(c, t, C, B):
    head_seq(c, t, C, [("10", "A FÓRMULA", "ELEVE O FATOR", PURPLE), ("11", "OS FATORES QUE CAEM", "RECONHEÇA DE CARA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            boxed(c, 400, 200, 1120, 140, PURPLE, aa, 0.08)
            linha(c, [("fator do LONGO", PURPLE), ("  =  (", INK), ("fator do CURTO", BLUE), (")ⁿ", INK)], W / 2, 270, 58, aa)
            text(c, "n = quantos períodos curtos cabem no longo", W / 2, 380, 28, "bold", GRAY, aa)
        rows = [("10.b", "10% a.m. · BIMESTRE (2 meses)", "1,1^2 = 1,21", "21%", "não 20%"),
                ("10.c", "10% a.m. · TRIMESTRE (3 meses)", "1,1^3 = 1,331", "33,1%", "não 30%")]
        for k, (cue, s_, e_, r_, n_) in enumerate(rows):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 500 + k * 160 + d
            rrect(c, 220, y - 62, 1480, 124, 18, "#FFFFFF", a, shadow=True)
            ftext(c, s_, 250, y + 12, 30, "black", INK2, a, align="left")
            expr(c, e_, 1000, y, 48, a)
            ar = ep(t, C[cue] + 2.6, 0.4)
            fmid(c, r_, 1360, y, 52, "black", GREEN, ar)
            pill(c, n_, 1600, y, RED, size=22, a=ar, anchor="center")
        return
    rows = [("11.a", "20% a.s.", "1,2^2 = 1,44", "44% a.a.", "40%"),
            ("11.b", "1% a.m.", "1,01^{12} ≈ 1,1268", "12,68% a.a.", "12%"),
            ("11.c", "2% a.m.", "1,02^{12} ≈ 1,268", "26,8% a.a.", "24%")]
    a0 = ep(t, C["11"], 0.4)
    if a0 > 0:
        for x_, s_ in ((330, "TAXA CURTA"), (790, "FATOR ELEVADO"), (1260, "EQUIVALENTE"), (1580, "PROPORCIONAL")):
            text(c, s_, x_, 230, 22, "black", GRAY, a0, tracking=2)
    for k, (cue, tc, e_, eq, pr) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 320 + k * 130 + d
        rrect(c, 200, y - 55, 1520, 110, 16, "#F7F7F5", a)
        fmid(c, tc, 330, y, 40, "black", BLUE, a)
        expr(c, e_, 790, y, 44, a)
        fmid(c, eq, 1260, y, 40, "black", GREEN, a)
        fmid(c, pr, 1580, y, 36, "black", GRAY, a)
        strike(c, 1530, y + 2, 1630, y - 6, ep(t, C[cue] + 2.0, 0.4), RED, ep(t, C[cue] + 2.0, 0.4))
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        pill(c, "potência de 12? o ENEM DÁ o valor no enunciado", W / 2, 760, GREEN, size=28, a=ad, anchor="center")


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DOIS PERÍODOS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 300, 200, 1320, 140, "ATALHO · 2 PERÍODOS", ["DOBRE a taxa e SOME o quadrado dela"], aa, 42)
    rows = [("12.b", "10%", "20%", "1%", "21%"), ("12.c", "20%", "40%", "4%", "44%")]
    for k, (cue, tx, dob, q, r) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 450 + k * 150 + d
        rrect(c, 300, y - 60, 1320, 120, 18, "#FFFFFF", a, shadow=True)
        fmid(c, tx, 420, y, 50, "black", BLUE, a)
        fmid(c, "→", 540, y, 44, "black", GRAY, a)
        linha(c, [("dobro ", GRAY), (dob, INK), ("  +  quadrado ", GRAY), (q, AMBER)], 900, y, 42, a)
        fmid(c, "=  " + r, 1440, y, 56, "black", GREEN, ep(t, C[cue] + 2.4, 0.4))
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "o quadrado é o JURO SOBRE JURO", W / 2, 780, AMBER, size=30, a=ad, anchor="center")


# ======================================================================
# bloco d — o caminho inverso (raiz)
# ======================================================================

def b_raiz(c, t, C, B):
    head_seq(c, t, C, [("13", "O CAMINHO CONTRÁRIO", "RAIZ DO FATOR", PURPLE), ("14", "E SE DIVIDISSE?", "A ARMADILHA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 210, 1400, 150, 22, mix("#FFFFFF", BLUE, 0.08), aa)
            text(c, "RAIZ: o número que, vezes ele mesmo, dá o fator", W / 2, 275, 36, "black", BLUE, aa)
            text(c, "o contrário de elevar ao quadrado", W / 2, 330, 26, "bold", GRAY, aa)
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            linha(c, [("69% a.a.  →  fator ", INK2), ("1,69", PURPLE)], W / 2, 450, 52, ab)
            linha(c, [("? × ? = 1,69   →   ", INK2), ("1,3 × 1,3", GREEN)], W / 2, 560, 52, ep(t, C["13.b"] + 2.4, 0.4))
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            corta_um(c, "1,3", "30%", 760, 690, 72, acc, ep(t, C["13.c"] + 0.2, 1.6))
            text(c, "ao semestre", 880, 714, 44, "black", GREEN, ep(t, C["13.c"] + 1.6, 0.4), align="left")
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("69% ÷ 2 = ", INK2), ("34,5% a.s.", RED)], W / 2, 260, 56, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        expr(c, "1,345^2 ≈ 1,81", W / 2, 390, 60, ab)
        linha(c, [("≈ 81% no ano   ", RED), ("≠ 69%", INK)], W / 2, 490, 48, ep(t, C["14.b"] + 2.0, 0.4))
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        K.atalho(c, 300, 570, 1320, 230, "ATALHO DA VOLTA · TESTE O FATOR AO QUADRADO", [], acc, 46)
        for k, e_ in enumerate(("1,1^2 = 1,21", "1,2^2 = 1,44", "1,3^2 = 1,69")):
            expr(c, e_, 520 + k * 440, 710, 50, acc * ep(t, C["14.c"] + 1.6 + k * 0.6, 0.4))


# ======================================================================
# bloco e — o efeito cresce com a taxa
# ======================================================================

def b_efeito(c, t, C, B):
    head(c, t, B["start"], "A DIFERENÇA CRESCE", "COM A TAXA", AMBER)
    card(c, *CARD_R)
    cols = [("15.a", "1% AO MÊS", "12%", "12,68%", "perto", GREEN),
            ("15.b", "10% AO MÊS", "120%", "≈ 214%", "explode!", RED)]
    for k, (cue, tit, pr, eq, tag, col) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 240 + k * 760
        rrect(c, x, 220, 680, 500, 26, "#FFFFFF", a, shadow=True)
        rrect(c, x, 220, 680, 70, 26, col, a * 0.14)
        text(c, tit, x + 340, 268, 32, "black", col, a)
        # barras: proporcional × equivalente (altura proporcional ao valor, escala por coluna)
        mx = 330 if k else 16
        for j, (lb, v, cc) in enumerate((("proporcional", pr, PURPLE), ("equivalente", eq, GREEN))):
            vv = float(v.replace("≈", "").replace("%", "").replace(",", ".").strip())
            g = ep(t, C[cue] + 0.6 + j * 0.8, 1.0) if k == 0 else ep(t, (C["15.b"] + 0.6) if j == 0 else C["15.c"], 1.0)
            hb = 300 * vv / mx * g
            bx = x + 140 + j * 260
            rrect(c, bx, 650 - hb, 140, hb, 10, cc, a * 0.85)
            text(c, v, bx + 70, 640 - hb - 14, 34, "black", cc, a * g)
            text(c, lb, bx + 70, 690, 22, "bold", GRAY, a)
        pill(c, tag, x + 340, 330, col, size=24, a=a * ep(t, C[cue] + 2.4, 0.4), anchor="center")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        expr(c, "1,1^{12} ≈ 3,14", 1240, 390, 36, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 780, ad, "É O ROTATIVO DO CARTÃO", AMBER, -2, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "FATOR PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("3% a.m.", BLUE), ("  (compostos)  =  ", INK), ("? ao bimestre", PURPLE)], W / 2, 285, 56, aa)
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 560)
    if t < C["17"]:
        return
    a1 = ep(t, C["17.a"], 0.4)
    if a1 > 0:
        linha(c, [("fator ", GRAY), ("1,03", PURPLE), ("  ·  2 meses → ao quadrado", INK2)], W / 2, 430, 44, a1)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        expr(c, "1,03^2 = 1,0609", W / 2, 540, 64, ab)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("6,09% ao bimestre", GREEN), ("   (não 6%)", RED)], W / 2, 650, 52, acc)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        linha(c, [("atalho: dobro 6 + quadrado 0,09 = 6,09", GREEN)], W / 2, 750, 36, ad)
        conferido(c, "bateu", 1520, 760, ep(t, C["17.d"] + 3.0, 0.4), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Taxa equivalente: eleve o fator, não multiplique a taxa.",
          "Do período longo para o curto: raiz do fator, nunca divisão.",
          "No fim, tire o 1 do fator."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("2% a.m. = 24% a.a. em juros compostos", "foi assim que você aprendeu nos juros simples",
          "nos compostos, eleve o fator: 1,02¹² − 1 ≈ 26,8% a.a."),
         ("Dividir a anual pelo nº de períodos: 69% a.a. → 34,5% a.s.",
          "dividir parece a volta da multiplicação",
          "a volta de uma POTÊNCIA é a RAIZ: 1,69 = 1,3² → 30% a.s."),
         ("Esquecer de tirar o 1: 1,268 → 126,8%", "o número está ali, prontinho",
          "o 1 é o dinheiro que você já tinha: a taxa é 26,8%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS1 = [("A", "1,27%", "vírgula deslocada", RED), ("B", "12,00%", "proporcional", RED),
         ("C", "12,12%", "1,01 × 12", RED), ("D", "12,68%", "", GREEN), ("E", "112,68%", "não tirou o 1", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "DO MÊS PARA O ANO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Uma aplicação rende 1% ao mês no regime de juros compostos. Considere 1,01¹² ≈ 1,1268. "
                           "A taxa anual equivalente a essa aplicação é, aproximadamente,", INK)], a0, 240, 28)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
          align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["23.ok"], "D", cues_in, cues_x, gap=34)
    if t >= C["23"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["23"], 0.4))
        linha(c, [("1%  →  fator ", INK2), ("1,01", PURPLE), ("  · 12 meses", INK2)], 540, y0 + 50, 30, ep(t, C["23.a"], 0.4))
        ab = ep(t, C["23.b"], 0.4)
        if ab > 0:
            expr(c, "1,01^{12} ≈ 1,1268", 540, y0 + 125, 40, ab)
        acc = ep(t, C["23.c"], 0.4)
        if acc > 0:
            corta_um(c, "1,1268", "12,68%", 540, y0 + 210, 44, acc, ep(t, C["23.c"] + 0.2, 1.4))
        conferido(c, "um pouco ACIMA dos 12%", 230, y0 + 285, ep(t, C["23.d"], 0.4), True, 26)


ALTS2 = [("A", "1,10%", "fator virou taxa", RED), ("B", "3,31%", "vírgula deslocada", RED), ("C", "10,00%", "", GREEN),
         ("D", "11,03%", "33,1 ÷ 3", RED), ("E", "33,10%", "taxa do trimestre", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "DO TRIMESTRE PARA O MÊS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("Um investimento rendeu 33,1% em um trimestre, no regime de juros compostos, com a mesma taxa "
                           "em cada mês. A taxa mensal desse investimento foi de", INK)], a0, 240, 28)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
          align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["26.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 140)
    if t >= C["26"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["26"], 0.4))
        linha(c, [("fator do trimestre: ", INK2), ("1,331", PURPLE)], 540, y0 + 50, 30, ep(t, C["26"], 0.4))
        aa = ep(t, C["26.a"], 0.4)
        if aa > 0:
            fmid(c, "(1 + i)³ = 1,331", 540, y0 + 120, 38, "black", INK, aa)
        ab = ep(t, C["26.b"], 0.4)
        if ab > 0:
            linha(c, [("1,1 · 1,1 · 1,1 = 1,331", BLUE)], 540, y0 + 185, 30, ab)
        acc = ep(t, C["26.c"], 0.4)
        if acc > 0:
            corta_um(c, "1,1", "10% a.m.", 540, y0 + 250, 40, acc, ep(t, C["26.c"] + 0.4, 1.4))
        conferido(c, "um pouco ABAIXO dos 11%", 230, y0 + 310, ep(t, C["26.d"], 0.4), True, 24)


ALTS9 = [("A", "3,67% ao mês", "44 ÷ 12", RED), ("B", "11% ao trimestre", "44 ÷ 4", RED),
         ("C", "14,67% ao quadrimestre", "44 ÷ 3", RED), ("D", "22% ao semestre", "44 ÷ 2", RED),
         ("E", "20% ao semestre", "", GREEN)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "RECONHECER A EQUIVALENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, [("Um fundo rende 44% ao ano no regime de juros compostos. Qual das taxas a seguir, aplicada "
                           "no mesmo regime, é equivalente à desse fundo?", INK)], a0, 240, 28)
    ftext(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["29"], 0.3)),
          align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS9, 1000, 250, 700, 36, C["29.ok"], "E", cues_in, cues_x, gap=30)
    aq = ep(t, C["28.qc"] + 1.0, 0.4) * (1 - ep(t, C["29"], 0.3))
    pill(c, "quadrimestre = 4 meses", 540, yend + 30, BLUE, size=22, a=aq, anchor="center")
    pause_timer(c, t, C["28.end"] - 1.9, 540, yend + 160)
    if t >= C["29"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["29"], 0.4))
        linha(c, [("1 ano = 2 semestres  ·  fator ", INK2), ("1,44", PURPLE)], 540, y0 + 50, 28, ep(t, C["29.a"], 0.4))
        ab = ep(t, C["29.b"], 0.4)
        if ab > 0:
            linha(c, [("raiz: ? × ? = 1,44  →  ", INK2), ("1,2", GREEN)], 540, y0 + 120, 32, ab)
        acc = ep(t, C["29.c"], 0.4)
        if acc > 0:
            corta_um(c, "1,2", "20% a.s.", 540, y0 + 190, 40, acc, ep(t, C["29.c"] + 0.2, 1.2))
            linha(c, [("atalho: 40 + 4 = 44 ✓", GREEN)], 540, y0 + 260, 26, ep(t, C["29.c"] + 2.4, 0.4))
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        selo(c, 1350, 765, aa, "4 PROPORCIONAIS: A D DÁ ≈ 49% NO ANO", RED, -2, 24)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        pill(c, "DESCONFIE DA DIVISÃO", 540, 790, AMBER, size=26, a=ab, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "NOMINAL × EFETIVA", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    if aa > 0:
        rrect(c, 460, 230, 1000, 300, 12, PAPEL, aa, shadow=True)
        text(c, "CONTRATO", W / 2, 290, 26, "black", GRAY, aa, tracking=4)
        text(c, "24% ao ano,", W / 2, 390, 60, "black", INK, aa)
        text(c, "capitalizados mensalmente", W / 2, 470, 44, "black", PURPLE, aa)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        text(c, "você paga 24% ao ano?", W / 2, 620, 46, "black", INK2, ab)
    acc = ep(t, C["32.c"], 0.5)
    if acc > 0:
        selo(c, 1500, 610, acc, "NÃO", RED, -8, 56)
    pill(c, "ep. 2 · taxa nominal × efetiva e taxas acumuladas", W / 2, 760, PURPLE, size=30, a=ep(t, C["32.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Você já tinha caído na conta do 24%?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              formas=b_formas, mesmo=b_mesmo, fator=b_fator, formula=b_formula, atalho=b_atalho, raiz=b_raiz,
              efeito=b_efeito, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q2=b_q2, q9=b_q9,
              ponte=b_ponte, cta=b_cta)
