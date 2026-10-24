"""Visual — Porcentagem, Episódio 5: ponto percentual × por cento, e gráfico de setores (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: termometro() (a taxa como temperatura: os graus = pontos percentuais), setor() / pizza_setores()
(o gráfico de setores de 360°), transferidor(), boneco() / turma() (os dois grupos de tamanhos diferentes com 30% pintado),
alts_longas() (alternativas longas com o motivo do erro embaixo) e linha() (texto com cor por trecho).
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
ARQUIVO_FINAL = "enem_matematica_porcentagem_ep5_pontos_e_setores.mp4"
CARD_R = K.CARD_R
VIDRO = "#F4F4F1"
TEAL = "#1BA39C"
# fatias da família (somam 100%): moradia, comida, transporte, lazer, outros
FAMILIA = [(35, BLUE, "moradia"), (25, GREEN, "comida"), (15, AMBER, "transporte"), (10, PURPLE, "lazer"),
           (15, TEAL, "outros")]


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


def termometro(c, cx, y_top, y_bot, vmax, v, a, col=None, marcas=(), rotulo="%", passo=1, v_ini=None):
    """termômetro vertical de 0 a vmax; v = nível atual (pode animar); marcas = [(valor, texto, cor)] à direita;
    v_ini = nível de antes (traço fantasma)"""
    if a <= 0:
        return
    col = col or RED
    w = 46
    y_of = lambda val: lerp(y_bot, y_top, val / vmax)
    rrect(c, cx - w / 2, y_top - 20, w, y_bot - y_top + 40, w / 2, VIDRO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y_top - 20, w, y_bot - y_top + 40), w / 2, w / 2),
                paint("#BDBDB6", a, stroke=4))
    c.drawCircle(cx, y_bot + 46, 44, paint(col, a))
    c.drawCircle(cx, y_bot + 46, 44, paint("#BDBDB6", a, stroke=4))
    yv = y_of(clamp(v / vmax) * vmax)
    rrect(c, cx - 13, yv, 26, y_bot + 20 - yv, 13, col, a)
    k = 0
    while k <= vmax + 1e-9:
        yy = y_of(k)
        line(c, cx - w / 2 - 22, yy, cx - w / 2 - 6, yy, INK2, a, 3)
        text(c, f"{k:g}".replace(".", ","), cx - w / 2 - 30, yy + 10, 26, "bold", INK2, a, align="right")
        k += passo
    if v_ini is not None:
        yi = y_of(v_ini)
        line(c, cx - w / 2 - 4, yi, cx + w / 2 + 4, yi, INK, a * 0.6, 4)
    ys_txt = []
    for val, s, mc in sorted(marcas):
        yy = y_of(val)
        yt = yy
        for yo in ys_txt:
            if abs(yt - yo) < 40:
                yt = yo - 40
        ys_txt.append(yt)
        line(c, cx + w / 2 + 6, yy, cx + w / 2 + 34, yy, mc, a, 4)
        text(c, s, cx + w / 2 + 44, yt + 12, 32, "black", mc, a, align="left")
    text(c, rotulo, cx, y_top - 40, 28, "black", INK2, a)


def setor(c, cx, cy, r, ang0, ang1, col, a, pull=0.0):
    """fatia de pizza de ang0 a ang1 (graus, 0 = topo, sentido horário); pull afasta a fatia do centro"""
    if a <= 0 or ang1 <= ang0:
        return
    mid = math.radians((ang0 + ang1) / 2 - 90)
    ox, oy = cx + pull * math.cos(mid), cy + pull * math.sin(mid)
    p = skia.Path()
    p.moveTo(ox, oy)
    p.arcTo(skia.Rect.MakeXYWH(ox - r, oy - r, 2 * r, 2 * r), ang0 - 90, ang1 - ang0, False)
    p.close()
    c.drawPath(p, paint(col, a))
    c.drawPath(p, paint("#FFFFFF", a, stroke=4))


def pizza_setores(c, cx, cy, r, fatias, a, prog_=1.0, destaque=None, rotulos=True, pull=18, size=26):
    """fatias = [(porcentagem, cor, nome)]; prog_ 0..1 desenha em sentido horário; destaque = índice afastado"""
    if a <= 0:
        return
    total = 360 * clamp(prog_)
    ang = 0.0
    for i, (pct, col, nome) in enumerate(fatias):
        a0, a1 = ang, min(ang + pct * 3.6, total)
        if a1 > a0:
            setor(c, cx, cy, r, a0, a1, col, a, pull if destaque == i else 0)
            if rotulos and a1 >= ang + pct * 3.6 - 1e-6:
                mid = math.radians((ang + a1) / 2 - 90)
                rr = r * 0.64 + (pull if destaque == i else 0)
                tx, ty = cx + rr * math.cos(mid), cy + rr * math.sin(mid)
                text_mid(c, f"{pct}%", tx, ty, size, "black", "#FFFFFF", a)
        ang += pct * 3.6


def transferidor(c, cx, cy, r, ang0, ang1, a, col=None, rot=""):
    """arco do ângulo central entre ang0 e ang1 (graus, 0 = topo) com o valor escrito"""
    if a <= 0:
        return
    col = col or INK
    p = skia.Path()
    p.addArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ang0 - 90, ang1 - ang0)
    c.drawPath(p, paint(col, a, stroke=6))
    for ang in (ang0, ang1):
        rad = math.radians(ang - 90)
        line(c, cx, cy, cx + (r + 26) * math.cos(rad), cy + (r + 26) * math.sin(rad), col, a, 4)
    if rot:
        mid = math.radians((ang0 + ang1) / 2 - 90)
        tx, ty = cx + (r + 70) * math.cos(mid), cy + (r + 70) * math.sin(mid)
        pill(c, rot, tx, ty, col, size=28, a=a, anchor="center", bounds=(0, 1920))


def boneco(c, x, y, s, col, a):
    """bonequinho simples: cabeça e corpo"""
    if a <= 0:
        return
    c.drawCircle(x, y - s * 0.62, s * 0.28, paint(col, a))
    rrect(c, x - s * 0.36, y - s * 0.28, s * 0.72, s * 0.78, s * 0.3, col, a)


def turma(c, x0, y0, n, cols, s, n_pinta, col_on, a, prog_=1.0, rot=""):
    """grade de n bonecos (cols por linha); os n_pinta primeiros acendem com prog_"""
    if a <= 0:
        return
    acesos = int(round(n_pinta * clamp(prog_)))
    for k in range(n):
        x = x0 + (k % cols) * s * 1.05
        y = y0 + (k // cols) * s * 1.25
        boneco(c, x, y, s * 0.9, col_on if k < acesos else "#D6D6D0", a)
    if rot:
        text(c, rot, x0 + (cols - 1) * s * 1.05 / 2, y0 - s * 1.15, 30, "black", INK2, a)


def alts_longas(c, t, C, alts, x, y0, w, size, ok_cue, okL, cues_in, cues_x, gap=16):
    """alternativas de texto longo; quando riscada, o motivo do erro aparece numa linha embaixo (não em cima do texto)"""
    aok = ep(t, ok_cue, 0.5)
    y = y0
    for L, s, why, col in alts:
        a, d = rise(t, cues_in.get(L, 1e9))
        ok = L == okL
        lines = K.wrap(s, "bold", size, w - 70)
        ax = ep(t, cues_x.get(L, 1e9), 0.4) if not ok else 0
        hh = len(lines) * (size + 8) + 6 + (size * 0.95 if why else 0)
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 18, y - 8 + d, w + 26, len(lines) * (size + 8) + 22, 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + size * 0.62 + d, a, 20, bg=GREEN if ok and aok > 0.5 else INK)
            for j, ln in enumerate(lines):
                yy = y + d + size + j * (size + 8)
                text(c, ln, x + 50, yy, size, "bold", INK, a * (1 - 0.5 * ax), align="left")
                if ax > 0:
                    strike(c, x + 46, yy - size * 0.35, x + 54 + text_w(ln, "bold", size), yy - size * 0.35, ax, RED, ax)
            if ax > 0 and why:
                text(c, why, x + 50, y + d + len(lines) * (size + 8) + size * 0.8, size * 0.85,
                     "black", col or RED, ax, align="left")
        y += hh + gap
    return y


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PONTO PERCENTUAL × POR CENTO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    sobe = ep(t, C["01.a"] + 0.6, 1.2)
    termometro(c, 470, 260, 700, 5, lerp(2, 4, sobe), aa, RED,
               [(2, "2%", INK2), (4, "4%", RED)] if sobe > 0.9 else [(2, "2%", INK2)], "JUROS", 1, v_ini=2)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        ftext(c, "subiram 2% ?", 1180, 320, 60, "black", RED, ab)
        strike(c, 1000, 302, 1360, 302, ab, RED, ep(t, C["01.c"], 0.4))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        ftext(c, "+2 pontos percentuais", 1180, 450, 54, "black", BLUE, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1180, 590, ad, "O CUSTO DO DINHEIRO DOBROU", GREEN, -3, 40)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        text(c, "“aumento de 2%” esconde a notícia", 1180, 730, 34, "black", AMBER, ae)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "distinguir PONTO PERCENTUAL de POR CENTO", "a diferença × o quanto ela representa"),
            ("02.b", "ler qualquer GRÁFICO DE SETORES", "a pizza de 360°")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 230, y - 14, 34, a, GREEN)
        text(c, s, 290, y, 46, "black", INK, a, align="left")
        text(c, sub, 290, y + 60, 34, "bold", GRAY, a, align="left")
    a2 = ep(t, C["02.b"], 0.5)
    pizza_setores(c, 1560, 470, 120, FAMILIA, a2, ep(t, C["02.b"] + 0.3, 1.0), rotulos=False)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "O DENOMINADOR DO EPISÓDIO 1", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        ftext(c, "40", 640, 400, 90, "black", INK, aa)
        arrow(c, 740, 370, 1060, 370, GREEN, aa, 6, 20, progress=aa)
        ftext(c, "50", 1180, 400, 90, "black", GREEN, aa)
        text(c, "+10", 900, 330, 40, "black", GREEN, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        linha(c, [("10 ÷ ", INK), ("40", BLUE), (" = ", INK2), ("25%", GREEN)], W / 2, 560, 64, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        pill(c, "o denominador é sempre O QUE ERA ANTES", W / 2, 700, BLUE, size=32, a=acc, anchor="center",
             bounds=(0, 1920))


# ======================================================================
# bloco A — ponto percentual
# ======================================================================

def _jornal(c, x, y, w, h, a, titulo, sub):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 16, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 56, 16, INK, a)
    text(c, "NOTÍCIAS", x + 30, y + 40, 26, "black", "#FFFFFF", a, align="left", tracking=2)
    text(c, titulo, x + 30, y + 120, 40, "black", INK, a, align="left")
    text(c, sub, x + 30, y + 170, 28, "bold", INK2, a, align="left")


def b_manchete(c, t, C, B):
    head(c, t, B["start"], "UMA MANCHETE", "SUBIU QUANTO?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    _jornal(c, 230, 250, 860, 220, aa, "Inflação vai de 5% para 6%", "no mês, segundo o levantamento")
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        boxed(c, 1160, 250, 520, 220, BLUE, ab, 0.08)
        text(c, "TAXA", 1420, 320, 44, "black", BLUE, ab)
        text(c, "uma porcentagem que mede algo:", 1420, 380, 26, "bold", INK2, ab)
        text(c, "quantos em cada cem", 1420, 420, 26, "bold", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        ftext(c, "a inflação SUBIU QUANTO?", W / 2, 590, 56, "black", INK, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        chip(c, "2 respostas certas", 720, 720, GREEN, ad, 36)
        chip(c, "1 errada (a do jornal)", 1220, 720, RED, ad * ep(t, C["04.d"] + 0.8, 0.4), 36)


def b_pp(c, t, C, B):
    head_seq(c, t, C, [("05", "1ª RESPOSTA", "PONTO PERCENTUAL", BLUE), ("06", "PENSE NUM TERMÔMETRO", "O GRAU DAS TAXAS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        a0 = ep(t, C["05"], 0.5)
        sobe = ep(t, C["05.a"], 1.0)
        termometro(c, 480, 280, 680, 8, lerp(5, 6, sobe), a0, RED, [(5, "5%", INK2), (6, "6%", RED)], "INFLAÇÃO", 1,
                   v_ini=5)
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            linha(c, [("6 − 5 = ", INK), ("1", BLUE)], 1180, 330, 70, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            ftext(c, "1 ponto percentual", 1180, 450, 56, "black", BLUE, ab)
            pill(c, "escreve-se: 1 p.p.", 1180, 540, BLUE, size=30, a=ab, anchor="center", bounds=(0, 1920))
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            boxed(c, 840, 620, 680, 130, BLUE, acc, 0.08)
            text(c, "PONTO PERCENTUAL", 1180, 675, 36, "black", BLUE, acc)
            text(c, "a DIFERENÇA entre duas taxas: uma subtração", 1180, 722, 26, "bold", INK2, acc)
        return
    aa = ep(t, C["06.a"], 0.5)
    sobe = ep(t, C["06.a"] + 0.4, 1.0)
    termometro(c, 470, 270, 690, 30, lerp(20, 22, sobe), aa, AMBER, [(20, "20°", INK2), (22, "22°", AMBER)], "°C", 5,
               v_ini=20)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        ftext(c, "“subiu 2%”", 1180, 330, 52, "black", RED, ab)
        strike(c, 1040, 312, 1320, 312, ab, RED, ep(t, C["06.b"] + 0.8, 0.4))
        ftext(c, "subiu 2 GRAUS", 1180, 440, 60, "black", AMBER, ep(t, C["06.b"] + 1.0, 0.5))
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        boxed(c, 820, 560, 720, 170, BLUE, acc, 0.08)
        text(c, "ponto percentual = o GRAU das taxas", 1180, 630, 36, "black", BLUE, acc)
        text(c, "quanto a taxa andou, na régua dela", 1180, 685, 28, "bold", INK2, acc)


# ======================================================================
# bloco B — por cento (variação relativa)
# ======================================================================

def b_relativa(c, t, C, B):
    head_seq(c, t, C, [("07", "2ª RESPOSTA", "POR CENTO", PURPLE), ("08", "ATALHO", "SUBTRAIA… E DIVIDA?", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            text(c, "esse 1 ponto é MUITO ou POUCO perto do que era?", W / 2, 290, 40, "black", INK, aa)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            expr(c, "1/5", 700, 470, 110, ab, cores={0: INK})
            text(c, "a diferença", 860, 425, 28, "bold", INK2, ab, align="left")
            text(c, "o de ANTES (5%)", 860, 535, 28, "black", BLUE, ab, align="left")
            linha(c, [("= ", INK2), ("20%", PURPLE)], 1360, 470, 96, ep(t, C["07.b"] + 1.4, 0.5))
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            boxed(c, 460, 640, 1000, 130, PURPLE, acc, 0.08)
            text(c, "VARIAÇÃO RELATIVA", W / 2, 695, 36, "black", PURPLE, acc)
            text(c, "o tamanho da mudança EM RELAÇÃO ao que era", W / 2, 742, 26, "bold", INK2, acc)
        return
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 300, 230, 1320, 250, "ATALHO · PONTO PERCENTUAL", ["só SUBTRAIA", "6 − 5 = 1 p.p."], aa, 40)
    ab = ep(t, C["08.b"], 0.5)
    K.atalho(c, 300, 520, 1320, 250, "ATALHO · POR CENTO", ["subtraia e DIVIDA pelo de ANTES", "(6 − 5) ÷ 5 = 20%"], ab, 40)


# ======================================================================
# bloco C — as duas estão certas
# ======================================================================

def b_certas(c, t, C, B):
    head(c, t, B["start"], "QUEM ESTÁ CERTO?", "A MESMA MUDANÇA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        check_icon(c, 300, 280, 34, aa, GREEN)
        text(c, "subiu 1 ponto percentual", 360, 296, 46, "black", INK, aa, align="left")
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        check_icon(c, 300, 390, 34, ab, GREEN)
        text(c, "subiu 20%", 360, 406, 46, "black", INK, ab, align="left")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        pill(c, "as duas descrevem A MESMA MUDANÇA", 1340, 345, GREEN, size=30, a=acc, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        check_icon(c, 300, 530, 34, ad, RED, "x")
        text(c, "“subiu 1%”", 360, 546, 46, "black", RED, ad, align="left")
        linha(c, [("1% de 5 = ", INK2), ("0,05", RED)], 1180, 530, 44, ad)
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        linha(c, [("levaria a 5,05%", RED), ("   não a 6%", INK)], W / 2, 690, 50, ae)


# ======================================================================
# bloco D — os juros que dobraram
# ======================================================================

def b_juros(c, t, C, B):
    head(c, t, B["start"], "O CASO DO COMEÇO", "OS JUROS DOBRARAM", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    sobe = ep(t, C["10.a"] + 0.4, 1.0)
    termometro(c, 450, 270, 690, 5, lerp(2, 4, sobe), aa, RED, [(2, "2%", INK2), (4, "4%", RED)], "JUROS", 1, v_ini=2)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        text(c, "PONTOS PERCENTUAIS", 1200, 290, 30, "black", BLUE, ab)
        linha(c, [("4 − 2 = ", INK), ("2 p.p.", BLUE)], 1200, 360, 60, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        text(c, "POR CENTO", 1200, 470, 30, "black", PURPLE, acc)
        linha(c, [("2 ÷ 2 = ", INK), ("100%", PURPLE)], 1200, 540, 60, acc)
        selo(c, 1200, 640, ep(t, C["10.c"] + 1.2, 0.4), "DOBROU", GREEN, -4, 50)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        text(c, "“só 2%” faz parecer pequeno o que DOBROU", W / 2, 790, 32, "black", AMBER, ad)


# ======================================================================
# bloco E — a pizza de 360°
# ======================================================================

def b_pizza(c, t, C, B):
    head_seq(c, t, C, [("11", "GRÁFICO DE PIZZA", "GRÁFICO DE SETORES", BLUE), ("12", "QUANTO VALE 1%?", "A PIZZA DE 360°", PURPLE),
                       ("13", "ATALHO", "TRÊS FATIAS DE CABEÇA", GREEN), ("14", "O CAMINHO DE VOLTA", "DE GRAUS PARA %", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13", "14"])
    cx, cy, r = 600, 500, 230
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        pizza_setores(c, cx, cy, r, FAMILIA, aa, ep(t, C["11.a"], 1.4), rotulos=False)
        if aa > 0:
            boxed(c, 1000, 260, 680, 150, BLUE, aa, 0.08)
            text(c, "GRÁFICO DE SETORES", 1340, 320, 38, "black", BLUE, aa)
            text(c, "círculo cortado em fatias: cada fatia, um setor", 1340, 368, 24, "bold", INK2, aa)
        ab = ep(t, C["11.b"], 0.5)
        for k, (pct, col, nome) in enumerate(FAMILIA[:4]):
            a = ab * ep(t, C["11.b"] + 0.45 * k, 0.3)
            if a > 0:
                rrect(c, 1060, 460 + k * 60, 34, 34, 8, col, a)
                text(c, nome, 1110, 488 + k * 60, 32, "black", INK, a, align="left")
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            pill(c, "a pizza inteira = 100% do gasto", cx, 790, INK, size=30, a=acc, anchor="center", bounds=(0, 1920))
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            c.drawCircle(cx, cy, r, paint("#EDEDE8", aa))
            prog_ = ep(t, C["12.a"], 1.4)
            p = skia.Path()
            p.addArc(skia.Rect.MakeXYWH(cx - r - 20, cy - r - 20, 2 * r + 40, 2 * r + 40), -90, 359.9 * prog_)
            c.drawPath(p, paint(PURPLE, aa, stroke=8))
            text_mid(c, "360°", cx, cy + 90, 80, "black", PURPLE, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("100%", INK), (" = 360°", PURPLE)], 1340, 300, 50, ab)
            linha(c, [("1% = 360 ÷ 100 = ", INK), ("3,6°", PURPLE)], 1340, 390, 46, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            setor(c, cx, cy, r, 0, 45, AMBER, acc)
            transferidor(c, cx, cy, 80, 0, 45, acc, INK)
            boxed(c, 1000, 470, 680, 120, BLUE, acc, 0.08)
            text(c, "ÂNGULO CENTRAL", 1340, 520, 34, "black", BLUE, acc)
            text(c, "o ângulo da fatia, medido no centro", 1340, 562, 24, "bold", INK2, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            regra(c, "ângulo = porcentagem × 3,6", 1340, 690, ad, 40)
        return
    if sid == "13":
        refs = [("13.a", 90, "90°", "25%", "um canto reto"), ("13.b", 180, "180°", "50%", "meia pizza"),
                ("13.c", 36, "36°", "10%", "")]
        for k, (cue, ang, sg, sp, sub) in enumerate(refs):
            a = ep(t, C[cue], 0.5)
            x = 420 + k * 540
            if a > 0:
                c.drawCircle(x, 470, 160, paint("#EDEDE8", a))
                setor(c, x, 470, 160, 0, ang, GREEN, a)
                text(c, sg, x, 700, 50, "black", INK, a)
                text(c, f"= {sp}", x, 760, 50, "black", GREEN, a)
                if sub:
                    text(c, sub, x, 270, 28, "bold", INK2, a)
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        c.drawCircle(cx, cy, r, paint("#EDEDE8", aa))
        setor(c, cx, cy, r, 0, 72, BLUE, aa)
        transferidor(c, cx, cy, 80, 0, 72, aa, INK, "72°")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("% → graus: ", INK2), ("× 3,6", PURPLE)], 1340, 290, 40, ab)
        linha(c, [("graus → %: ", INK2), ("÷ 3,6", PURPLE)], 1340, 360, 40, ab)
        linha(c, [("72 ÷ 3,6 = ", INK), ("20%", BLUE)], 1340, 470, 58, ep(t, C["14.b"] + 1.6, 0.5))
    acc = ep(t, C["14.c"], 0.5)
    K.atalho(c, 1000, 560, 680, 200, "ATALHO", ["72° = 2 × 36°", "= 2 × 10% = 20%"], acc, 36)


# ======================================================================
# bloco F — bases diferentes
# ======================================================================

def b_grupos(c, t, C, B):
    head_seq(c, t, C, [("15", "30% + 30% = 60%?", "BASES DIFERENTES", AMBER), ("16", "O QUE ACONTECEU?", "POR CENTO DE QUEM?", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    a0 = ep(t, C["15.a"], 0.5)
    acen = ep(t, C["15.d"], 1.2)
    turma(c, 260, 400, 20, 5, 46, 6, BLUE, a0, acen, "HOMENS: 20")
    ab = ep(t, C["15.b"], 0.5)
    turma(c, 720, 400, 80, 16, 46, 24, PURPLE, ab, acen, "MULHERES: 80")
    if a0 > 0:
        pill(c, "30% dos homens", 360, 280, BLUE, size=26, a=a0, anchor="center", bounds=(0, 1920))
    if ab > 0:
        pill(c, "30% das mulheres", 1090, 280, PURPLE, size=26, a=ab, anchor="center", bounds=(0, 1920))
    if sid == "15":
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            ftext(c, "= 60% do grupo?", 1500, 280, 40, "black", RED, acc * (1 - ep(t, C["15.e"], 0.4)))
        ad = ep(t, C["15.d"] + 0.8, 0.5)
        if ad > 0:
            text(c, "6 praticam", 360, 720, 32, "black", BLUE, ad)
            text(c, "24 praticam", 1090, 720, 32, "black", PURPLE, ad)
        ae = ep(t, C["15.e"], 0.5)
        if ae > 0:
            linha(c, [("6 + 24 = 30 de 100 = ", INK), ("30%", GREEN), ("   não 60%", RED)], W / 2, 800, 40, ae)
        return
    text(c, "6 praticam", 360, 720, 32, "black", BLUE, 1)
    text(c, "24 praticam", 1090, 720, 32, "black", PURPLE, 1)
    aa = ep(t, C["16.a"], 0.5)
    ab2 = ep(t, C["16.b"], 0.5)
    acc = ep(t, C["16.c"], 0.5)
    if aa > 0:
        pill(c, "cada 30% é de um TODO DIFERENTE", W / 2, 790, AMBER, size=30, a=aa * (1 - ab2), anchor="center",
             bounds=(0, 1920))
    if ab2 > 0:
        pill(c, "o mesmo 30%: 6 de um lado, 24 do outro", W / 2, 790, AMBER, size=30, a=ab2 * (1 - acc),
             anchor="center", bounds=(0, 1920))
    if acc > 0:
        boxed(c, 560, 752, 800, 72, GREEN, acc, 0.10)
        text_mid(c, "ATALHO:  por cento DE QUEM?", W / 2, 788, 36, "black", GREEN, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("18", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    desce = ep(t, C["18.a"], 1.0) if t >= C["18"] else 0
    termometro(c, 420, 270, 690, 50, lerp(40, 30, desce), aa, BLUE,
               [(40, "40%", INK2), (30, "30%", BLUE)] if desce > 0.9 else [(40, "40%", INK2)], "APROVAÇÃO", 10, v_ini=40)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        text(c, "caiu quantos PONTOS PERCENTUAIS?", 1180, 300, 40, "black", INK, ab)
        text(c, "e quantos POR CENTO?", 1180, 370, 40, "black", INK, ab)
    pause_timer(c, t, C["17.end"] - 1.9, 1180, 520)
    if t < C["18"]:
        return
    a1 = ep(t, C["18.a"], 0.5)
    if a1 > 0:
        linha(c, [("40 − 30 = ", INK), ("10 p.p.", BLUE)], 1180, 500, 56, a1)
    b1 = ep(t, C["18.b"], 0.5)
    if b1 > 0:
        linha(c, [("10 ÷ ", INK), ("40", BLUE), (" = ", INK2), ("25%", PURPLE)], 1180, 610, 56, b1)
    c1 = ep(t, C["18.c"], 0.5)
    if c1 > 0:
        pill(c, "queda de 1/4 do que era", 1180, 720, PURPLE, size=30, a=c1, anchor="center", bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Ponto percentual: a diferença. Por cento: em relação ao que era.", "Na pizza, 1% vale 3,6°.",
          "Só se somam porcentagens do mesmo todo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Dizer “subiu 2%” quando subiu 2 pontos percentuais", "os dois números têm o sinal de por cento",
          "diferença de taxas se mede em PONTOS; de 2% para 4% é +2 p.p. = +100%"),
         ("Usar o valor final como base: de 5% para 6%, 1 ÷ 6", "o 6 é o número mais recente",
          "a base é o que era ANTES: 1 ÷ 5 = 20%"),
         ("Somar porcentagens de grupos diferentes: 30% + 30% = 60%", "são porcentagens da mesma pesquisa",
          "cada uma é de um todo diferente; contando as pessoas, deu 30%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


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


ALTS7 = [("A", "aumentou 2%", "subir 2% levaria 8% a 8,16%", RED),
         ("B", "aumentou 2 pontos percentuais, o que corresponde a um aumento relativo de 25%", "", GREEN),
         ("C", "aumentou 20%", "usou o valor final como base: 2 ÷ 10", RED),
         ("D", "aumentou 10 pontos percentuais", "leu a taxa nova como a diferença", RED),
         ("E", "dobrou", "dobrar seria ir de 8% para 16%", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Um levantamento apontou que a taxa de desemprego de uma região passou de 8% para 10% em um ano.", INK),
                   ("Sobre essa mudança, é correto afirmar que a taxa", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    if t >= C["23.qa"] - 0.3:
        alts_longas(c, t, C, ALTS7, 990, 225, 720, 30, C["24.ok"], "B", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["23.end"] - 1.9, 540, 640)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        rrect(c, 170, 520, 740, 290, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["24.a"], 0.4)
        linha(c, [("10 − 8 = ", INK), ("2 p.p.", BLUE)], 540, 590, 46, aa)
        ab = ep(t, C["24.b"], 0.4)
        linha(c, [("2 ÷ ", INK), ("8", BLUE), (" = ", INK2), ("25%", PURPLE)], 540, 680, 46, ab)
        if ab > 0:
            text(c, "dividido pelo de ANTES", 540, 760, 26, "bold", INK2, ab)


ALTS8 = [("A", "5,4%", "dividiu por 10", RED), ("B", "10%", "é a fatia de 36°", RED), ("C", "15%", "", GREEN),
         ("D", "18%", "dividiu por 3, não por 3,6", RED), ("E", "54%", "leu o grau como %", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · ESTILO ENEM", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    _enunciado(c, [("Em um gráfico de setores que representa a distribuição de gastos de uma família, o setor "
                    "correspondente aos gastos com transporte tem ângulo central de 54°.", INK),
                   ("Esse setor representa, do total de gastos,", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABDE"}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS8, 1000, 240, 680, 44, C["26.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["25.end"] - 1.9, 540, 640)
    if t >= C["26"]:
        ra = ep(t, C["26"], 0.4)
        rrect(c, 170, 520, 740, 290, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["26.a"], 0.4)
        linha(c, [("54 ÷ 3,6 = ", INK), ("15%", GREEN)], 540, 585, 46, aa)
        ab = ep(t, C["26.b"], 0.4)
        linha(c, [("36° + 18° = ", INK2), ("10% + 5%", GREEN)], 540, 665, 38, ab)
        acc = ep(t, C["26.c"], 0.4)
        linha(c, [("15 × 3,6 = 54", INK2)], 540, 745, 36, acc)
        if acc > 0:
            check_icon(c, 700, 728, 26, acc, GREEN)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    itens = [("28.b", "juntamos tudo", BLUE), ("28.c", "caçamos as pegadinhas", AMBER), ("28.d", "questões novas", GREEN)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        chip(c, s, 480 + k * 480, 470 + d, col, a, 44)
    pill(c, "ep. 6 · revisão e treino para o ENEM", W / 2, 690, PURPLE, size=32, a=ep(t, C["28.a"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"], "Já viu manchete trocar p.p. por %?",
        canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, manchete=b_manchete, pp=b_pp, relativa=b_relativa,
              certas=b_certas, juros=b_juros, pizza=b_pizza, grupos=b_grupos, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q7=b_q7, q8=b_q8, ponte=b_ponte, cta=b_cta)
