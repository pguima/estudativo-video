"""Visual — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 1: lucro e prejuízo, porcentagem de quê? (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho, pizza...).
Peças deste episódio: barra_reais() (uma barra de valor em reais, na escala), dono() (a etiqueta "DONO: custo/venda"),
etiqueta() (etiqueta de preço), pilha() (o markup empilhado em cima do custo), linha(), conferido().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Cores das grandezas: CUSTO = azul · VENDA = roxo · LUCRO = verde · PREJUÍZO = vermelho.
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
_s = importlib.util.spec_from_file_location("comum030", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_lucro_ep1_lucro_base.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
CUSTO, VENDA, LUCRO, PREJ = BLUE, PURPLE, GREEN, RED


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


def barra_reais(c, x, y, w, h, col, a, rotulo=None, dentro=None, u=1.0):
    """barra de valor: largura w (já na escala), cresce da esquerda (u). rotulo à esquerda; dentro = texto no meio."""
    if a <= 0 or u <= 0:
        return
    ww = w * ease_io(clamp(u))
    rrect(c, x, y, ww, h, 12, mix("#FFFFFF", col, 0.30), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, ww, h), 12, 12), paint(col, a, stroke=4))
    if dentro and u > 0.6:
        fmid(c, dentro, x + ww / 2, y + h / 2, h * 0.42, "black", col, a)
    if rotulo:
        text(c, rotulo, x - 24, y + h * 0.62, h * 0.40, "black", col, a, align="right")


def dono(c, s, cx, cy, col, a, size=30):
    """etiqueta 'DONO: ...' (a base da porcentagem)"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 70
    rrect(c, cx - w / 2, cy - size, w, size * 2, size, col, a, shadow=True)
    c.drawCircle(cx - w / 2 + 26, cy, size * 0.22, paint("#FFFFFF", a))
    fmid(c, s, cx + 12, cy, size, "black", "#FFFFFF", a)


def etiqueta(c, cx, cy, w, h, a, preco, col=None, rot=0):
    if a <= 0:
        return
    col = col or AMBER
    c.save(); c.translate(cx, cy); c.rotate(rot)
    x, y = -w / 2, -h / 2
    p = skia.Path(); p.moveTo(x + h * 0.35, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h); p.lineTo(x + h * 0.35, y + h)
    p.lineTo(x, 0); p.close()
    c.drawPath(p, paint(col, a))
    c.drawCircle(x + h * 0.32, 0, h * 0.09, paint("#FFFFFF", a))
    fmid(c, preco, h * 0.15, 0, h * 0.40, "black", "#FFFFFF", a)
    c.restore()


def mochila(c, cx, cy, s, a, col=None):
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, cx - s * 0.5, cy - s * 0.45, s, s * 1.0, s * 0.22, col, a, shadow=True)
    rrect(c, cx - s * 0.36, cy + s * 0.05, s * 0.72, s * 0.34, s * 0.10, mix(col, "#FFFFFF", 0.25), a)
    c.drawArc(skia.Rect.MakeXYWH(cx - s * 0.28, cy - s * 0.78, s * 0.56, s * 0.66), 180, 180, False,
              paint(mix(col, INK, 0.3), a, stroke=s * 0.07))


def pilha(c, x, yb, w, hu, n_custo, n_extra, a, u=1.0):
    """o custo como bloco (n_custo unidades de altura hu) e o markup empilhado em cima (n_extra unidades, cresce com u)"""
    if a <= 0:
        return
    rrect(c, x, yb - n_custo * hu, w, n_custo * hu, 10, mix("#FFFFFF", CUSTO, 0.30), a)
    fmid(c, "CUSTO", x + w / 2, yb - n_custo * hu / 2, 26, "black", CUSTO, a)
    k = n_extra * clamp(u)
    if k > 0:
        rrect(c, x, yb - (n_custo + k) * hu - 6, w, k * hu, 10, mix("#FFFFFF", LUCRO, 0.35), a)


def pizza_lucro(c, cx, cy, r, n, a, rot=-90.0, pull=0.6, label=True):
    """o preço de venda como pizza: 1 de n fatias é LUCRO (verde), o resto paga o CUSTO"""
    if a <= 0:
        return
    K.pizza(c, cx, cy, r, n, 1, a, sel_col=LUCRO, pull=pull, rot=rot)
    if label:
        ang = math.radians(rot + 180 / n)
        fmid(c, "LUCRO", cx + math.cos(ang) * r * 0.55 + math.cos(ang) * r * 0.06, cy + math.sin(ang) * r * 0.55, r * 0.14,
             "black", "#FFFFFF", a)


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    """faixa com a pergunta do bloco"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "LUCRO E PREJUÍZO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        mochila(c, 330, 470, 190, aa)
        etiqueta(c, 700, 380, 300, 100, aa, "R$ 80", CUSTO, -4)
        text(c, "comprei", 700, 470, 30, "black", CUSTO, aa)
        etiqueta(c, 1180, 380, 300, 100, ep(t, C["01.a"] + 1.6, 0.4), "R$ 100", VENDA, 4)
        text(c, "vendi", 1180, 470, 30, "black", VENDA, ep(t, C["01.a"] + 1.6, 0.4))
        line(c, 870, 380, 1000, 380, INK2, ep(t, C["01.a"] + 1.6, 0.4), 5)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        chip(c, "25%?", 760, 620, LUCRO, ab, 64)
        chip(c, "20%?", 1160, 620, LUCRO, ep(t, C["01.b"] + 1.4, 0.4), 64)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        check_icon(c, 915, 620, 26, acc, GREEN)
        check_icon(c, 1315, 620, 26, acc, GREEN)
        text(c, "AS DUAS ESTÃO CERTAS", 960, 740, 40, "black", GREEN, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 470, ad, "SÓ UMA RESPONDE", AMBER, -6, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    for k, (cue, s) in enumerate((("02.a", "calcular lucro e prejuízo na BASE CERTA"),
                                  ("02.b", "formar o preço de venda para qualquer margem"),
                                  ("02.c", "sem cair na armadilha da base"))):
        a, d = rise(t, C[cue])
        check_icon(c, 300, 330 + k * 160 + d, 34, a, GREEN)
        text(c, s, 360, 345 + k * 160 + d, 50, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "SÉRIE DE PORCENTAGEM", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "QUE % A PARTE REPRESENTA?", 560, 300, 34, "black", BLUE, aa)
        fr(c, "parte", "todo", 560, 470, 80, INK, aa, num_col=GREEN, den_col=BLUE)
        linha(c, [("20 ÷ 80 = ", INK), ("25%", GREEN)], 560, 650, 50, ep(t, C["03.a"] + 1.8, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "O FATOR", 1370, 300, 34, "black", BLUE, ab)
        linha(c, [("+20%  →  ", INK), ("× 1,20", PURPLE)], 1370, 470, 66, ab)
        text(c, "1 + 20/100", 1370, 600, 34, "bold", GRAY, ab)
    line(c, 960, 260, 960, 760, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS BALCÕES", "A MESMA PERGUNTA", BLUE)
    card(c, *CARD_R)
    cols = [("04.a", "A MOCHILA"), ("04.b", "A ARTESÃ"), ("04.c", "O APLICATIVO")]
    for k, (cue, tit) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 220, 460, 440, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x + 230, 272, 30, "black", BLUE, a)
        if k == 0:
            mochila(c, x + 230, 440, 150, a)
            linha(c, [("R$ 80", CUSTO), ("  →  ", INK2), ("R$ 100", VENDA)], x + 230, 610, 34, a)
        elif k == 1:
            c.drawCircle(x + 230, 430, 90, paint(mix("#FFFFFF", AMBER, 0.35), a))
            c.drawCircle(x + 230, 430, 90, paint(AMBER, a, stroke=6))
            c.drawCircle(x + 230, 430, 40, paint(AMBER, a, stroke=6))
            text(c, "preço = ?", x + 230, 610, 34, "black", AMBER, a)
        else:
            rrect(c, x + 160, 330, 140, 230, 24, INK, a)
            rrect(c, x + 172, 350, 116, 180, 10, mix("#FFFFFF", BLUE, 0.2), a)
            text(c, "−15%", x + 230, 455, 40, "black", RED, a)
            text(c, "taxa por venda", x + 230, 610, 30, "black", RED, a)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "QUANTO EU GANHO?", W / 2, 760, ad, 44, BLUE)


# ======================================================================
# bloco a — custo, venda, lucro
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "CUSTO, VENDA E LUCRO", "AS DEFINIÇÕES", BLUE), ("06", "E SE A VENDA FOR MENOR?", "PREJUÍZO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    X0, ESC = 520, 9.0
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        barra_reais(c, X0, 280, 80 * ESC, 90, CUSTO, aa, "CUSTO", "R$ 80", ep(t, C["05.a"], 1.0))
        if aa > 0:
            text(c, "quanto o comerciante PAGOU", X0 + 80 * ESC / 2, 410, 28, "bold", CUSTO, aa)
        ab = ep(t, C["05.b"], 0.5)
        barra_reais(c, X0, 460, 100 * ESC, 90, VENDA, ab, "VENDA", "R$ 100", ep(t, C["05.b"], 1.0))
        if ab > 0:
            text(c, "quanto o cliente PAGA", X0 + 100 * ESC / 2, 590, 28, "bold", VENDA, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, X0 + 80 * ESC, 450, 20 * ESC, 110, 12, mix("#FFFFFF", LUCRO, 0.45), acc)
            line(c, X0 + 80 * ESC, 260, X0 + 80 * ESC, 580, LUCRO, acc, 3)
            text(c, "R$ 20", X0 + 90 * ESC, 520, 34, "black", LUCRO, acc)
            regra(c, "LUCRO = VENDA − CUSTO", W / 2, 720, acc, 44, PURPLE)
        return
    aa = ep(t, C["06.a"], 0.5)
    barra_reais(c, X0, 280, 120 * ESC * 0.85, 90, CUSTO, aa, "CUSTO", "R$ 120", ep(t, C["06.a"], 0.8))
    barra_reais(c, X0, 420, 90 * ESC * 0.85, 90, VENDA, aa, "VENDA", "R$ 90", ep(t, C["06.a"] + 0.4, 0.8))
    if aa > 0:
        x1, x2 = X0 + 90 * ESC * 0.85, X0 + 120 * ESC * 0.85
        rrect(c, x1, 410, x2 - x1, 110, 12, mix("#FFFFFF", PREJ, 0.35), aa)
        text(c, "−R$ 30", (x1 + x2) / 2, 560, 34, "black", PREJ, aa)
        pill(c, "PREJUÍZO: o dinheiro que se perdeu", W / 2, 640, PREJ, size=28, a=aa, anchor="center")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        conferido(c, "em REAIS: nenhuma dúvida", 420, 750, ab, True, 34)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        selo(c, 1420, 740, acc, "EM % : CONFUSÃO", AMBER, -4, 34)


# ======================================================================
# bloco b — o mesmo lucro em duas bases (animação principal)
# ======================================================================

def b_base(c, t, C, B):
    head_seq(c, t, C, [("07", "R$ 20 DE LUCRO", "SÃO QUANTOS POR CENTO?", BLUE), ("08", "A REGRA DA AULA", "TODA % TEM DONO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    X0, ESC = 330, 8.0
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            pergunta(c, "POR CENTO DE QUÊ?", W / 2, 230, aa, AMBER, 40)
        # 1) o lucro em cima do custo
        ab = ep(t, C["07.b"], 0.5)
        barra_reais(c, X0, 320, 80 * ESC, 80, CUSTO, ab, None, "CUSTO R$ 80")
        if ab > 0:
            m = ep(t, C["07.b"] + 0.6, 0.8)
            xl = X0 + 80 * ESC
            rrect(c, lerp(X0 + 60 * ESC, xl, m), 320, 20 * ESC, 80, 12, mix("#FFFFFF", LUCRO, 0.5), ab)
            fmid(c, "+20", lerp(X0 + 70 * ESC, xl + 10 * ESC, m), 360, 30, "black", LUCRO, ab)
            fr(c, "20", "80", 1220, 350, 46, INK, ep(t, C["07.b"] + 1.6, 0.4), num_col=LUCRO, den_col=CUSTO)
            linha(c, [("= ", INK), ("25% do CUSTO", CUSTO)], 1460, 364, 40, ep(t, C["07.b"] + 2.4, 0.4))
            dono(c, "DONO: custo", 1500, 450, CUSTO, ep(t, C["07.b"] + 2.4, 0.4) * (1 - ep(t, C["07.c"], 0.4) * 0.6), 24)
        # 2) o lucro dentro da venda
        acc = ep(t, C["07.c"], 0.5)
        barra_reais(c, X0, 560, 100 * ESC, 80, VENDA, acc, None, "VENDA R$ 100")
        if acc > 0:
            m = ep(t, C["07.c"] + 0.6, 0.8)
            xr = X0 + 100 * ESC
            rrect(c, xr - 20 * ESC, lerp(470, 560, m), 20 * ESC, 80, 12, mix("#FFFFFF", LUCRO, 0.5), acc)
            fmid(c, "20", xr - 10 * ESC, lerp(510, 600, m), 30, "black", LUCRO, acc)
            fr(c, "20", "100", 1220, 590, 46, INK, ep(t, C["07.c"] + 1.6, 0.4), num_col=LUCRO, den_col=VENDA)
            linha(c, [("= ", INK), ("20% da VENDA", VENDA)], 1470, 604, 40, ep(t, C["07.c"] + 2.4, 0.4))
            dono(c, "DONO: venda", 1500, 690, VENDA, ep(t, C["07.c"] + 2.4, 0.4), 24)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            regra(c, "UM LUCRO · DUAS PORCENTAGENS", W / 2, 780, ad, 36, PURPLE)
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text(c, "TODA PORCENTAGEM TEM DONO", W / 2, 290, 56, "black", PURPLE, aa)
        fr(c, "parte", "BASE (o dono)", W / 2, 440, 56, INK, aa, num_col=LUCRO, den_col=AMBER)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        boxed(c, 260, 580, 640, 150, BLUE, ab, 0.08)
        text(c, "SEM AVISO", 580, 635, 28, "black", BLUE, ab)
        text(c, "a base é o CUSTO", 580, 690, 38, "black", INK, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        boxed(c, 1020, 580, 640, 150, AMBER, acc, 0.10)
        text(c, "NO ENEM, PROCURE", 1340, 635, 28, "black", AMBER, acc)
        linha(c, [("“do CUSTO”", CUSTO), ("  ou  ", INK), ("“da VENDA”", VENDA)], 1340, 680, 36, acc)


# ======================================================================
# bloco c — prejuízo também tem base
# ======================================================================

def b_prejuizo(c, t, C, B):
    head(c, t, B["start"], "E O PREJUÍZO?", "TAMBÉM TEM DONO", BLUE)
    card(c, *CARD_R)
    X0, ESC = 330, 6.5
    aa = ep(t, C["09.a"], 0.5)
    barra_reais(c, X0, 260, 120 * ESC, 80, CUSTO, aa, None, "CUSTO R$ 120")
    barra_reais(c, X0, 370, 90 * ESC, 80, VENDA, aa, None, "VENDA R$ 90", ep(t, C["09.a"] + 0.6, 0.8))
    if aa > 0:
        x1, x2 = X0 + 90 * ESC, X0 + 120 * ESC
        ap = ep(t, C["09.a"] + 1.6, 0.4)
        rrect(c, x1, 360, x2 - x1, 100, 12, mix("#FFFFFF", PREJ, 0.40), ap)
        text(c, "−R$ 30", (x1 + x2) / 2, 500, 32, "black", PREJ, ap)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        fr(c, "30", "120", 1340, 290, 44, INK, ab, num_col=PREJ, den_col=CUSTO)
        linha(c, [("= ", INK), ("25% do CUSTO", CUSTO)], 1560, 304, 34, ep(t, C["09.b"] + 1.6, 0.4))
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        fr(c, "30", "90", 1340, 440, 44, INK, acc, num_col=PREJ, den_col=VENDA)
        linha(c, [("≈ ", INK), ("33,3% da VENDA", VENDA)], 1570, 454, 34, ep(t, C["09.c"] + 1.6, 0.4))
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        regra(c, "SALVO AVISO: prejuízo também é sobre o CUSTO", W / 2, 680, ad, 36, PURPLE)


# ======================================================================
# bloco d — markup × margem sobre a venda (a pizza)
# ======================================================================

def b_pizza(c, t, C, B):
    head_seq(c, t, C, [("10", "VENDEU PELO DOBRO", "LUCROU 100%?", BLUE), ("11", "QUAL É MAIOR?", "MARKUP × MARGEM", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            pilha(c, 330, 700, 220, 4.4, 50, 50, aa, ep(t, C["10.a"] + 1.0, 1.0))
            text(c, "R$ 50", 440, 760, 30, "black", CUSTO, aa)
            text(c, "+R$ 50", 440, 230, 30, "black", LUCRO, ep(t, C["10.a"] + 1.8, 0.4))
            pill(c, "MARKUP: em CIMA do custo · 100%", 440, 800, LUCRO, size=24, a=ep(t, C["10.a"] + 2.6, 0.4),
                 anchor="center")
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            pizza_lucro(c, 1100, 470, 210, 2, ab, rot=-90, pull=ep(t, C["10.c"], 0.6))
            text(c, "PREÇO DE VENDA = R$ 100", 1100, 750, 32, "black", VENDA, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            boxed(c, 1360, 360, 330, 220, LUCRO, acc, 0.08)
            text(c, "50%", 1525, 470, 80, "black", LUCRO, acc)
            text(c, "da VENDA", 1525, 530, 30, "black", VENDA, acc)
            pill(c, "MARGEM: DENTRO do preço", 1525, 640, VENDA, size=22, a=acc, anchor="center")
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("MARGEM SOBRE A VENDA", VENDA), ("  é sempre a MENOR", INK)], W / 2, 240, 38, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        n = 2 if t < C["11.b"] + 1.5 else 4
        g = ep(t, C["11.b"] + 0.4, 2.0)
        frac = lerp(0.25, 0.92, g)
        cx, cy, r = 560, 520, 210
        c.drawCircle(cx, cy, r, paint(BORDA_, ab))
        c.drawCircle(cx, cy, r * 0.88, paint(QUEIJO_, ab))
        c.drawPath(K._wedge(cx, cy, r * 0.88, -90, -90 + 360 * frac), paint(LUCRO, ab))
        text(c, f"{round(frac * 100)}%", cx, cy + 20, 64, "black", "#FFFFFF" if frac > 0.5 else INK, ab)
        selo(c, cx, 800, ep(t, C["11.b"] + 2.6, 0.4), "NUNCA CHEGA A 100%", RED, -3, 30)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        g = ep(t, C["11.c"], 2.4)
        pilha(c, 1280, 780, 240, 1.0, 100, 300 * g, acc, 1.0)
        text(c, "CUSTO R$ 100", 1400, 820, 26, "black", CUSTO, acc)
        pct = round(300 * g)
        text(c, f"markup +{pct}%", 1400, 780 - (100 + 300 * g) * 1.0 - 24, 32, "black", LUCRO, acc)
        pill(c, "pilha sem limite", 1680, 500, LUCRO, size=24, a=acc, anchor="center")


BORDA_, QUEIJO_ = "#D9A55B", "#FFE9A8"


# ======================================================================
# bloco e — converter as margens
# ======================================================================

def b_converter(c, t, C, B):
    head(c, t, B["start"], "DE UMA MARGEM PARA A OUTRA", "A CONVERSÃO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 230, 1480, 250, PURPLE, aa, 0.06)
        text(c, "CUSTO → VENDA", 300, 280, 26, "black", PURPLE, aa, align="left")
        text_mid(c, "sobre a venda  =", 420, 380, 34, "black", VENDA, aa)
        fr(c, "sobre o custo", "1 + sobre o custo", 760, 366, 34, INK, aa, num_col=CUSTO, den_col=CUSTO)
        fr(c, "0,25", "1,25", 1130, 366, 52, INK, ep(t, C["12.a"] + 2.6, 0.4), num_col=CUSTO, den_col=CUSTO)
        linha(c, [("= ", INK), ("0,20", VENDA), ("  (20% da venda)", GRAY)], 1470, 380, 34, ep(t, C["12.a"] + 3.6, 0.4))
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        boxed(c, 220, 520, 1480, 250, PURPLE, ab, 0.06)
        text(c, "VENDA → CUSTO", 300, 570, 26, "black", PURPLE, ab, align="left")
        text_mid(c, "sobre o custo  =", 420, 670, 34, "black", CUSTO, ab)
        fr(c, "sobre a venda", "1 − sobre a venda", 760, 656, 34, INK, ab, num_col=VENDA, den_col=VENDA)
        fr(c, "0,20", "0,80", 1130, 656, 52, INK, ep(t, C["12.b"] + 2.6, 0.4), num_col=VENDA, den_col=VENDA)
        linha(c, [("= ", INK), ("0,25", CUSTO), ("  (25% do custo)", GRAY)], 1470, 670, 34, ep(t, C["12.b"] + 3.6, 0.4))


def b_atalho1(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "INVENTE UM CUSTO DE R$ 100", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 120, "ATALHO", ["esqueceu a fórmula? invente CUSTO = R$ 100"], aa, 36)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        X0, ESC = 330, 5.6
        barra_reais(c, X0, 400, 100 * ESC, 80, CUSTO, ab, None, "CUSTO R$ 100")
        rrect(c, X0 + 100 * ESC, 400, 25 * ESC, 80, 12, mix("#FFFFFF", LUCRO, 0.5), ep(t, C["13.b"] + 0.8, 0.4))
        fmid(c, "+25", X0 + 112.5 * ESC, 440, 28, "black", LUCRO, ep(t, C["13.b"] + 0.8, 0.4))
        linha(c, [("VENDA ", INK), ("R$ 125", VENDA), (" · LUCRO ", INK), ("R$ 25", LUCRO)], X0 + 62 * ESC, 550, 34,
              ep(t, C["13.b"] + 1.8, 0.4))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        fr(c, "25", "125", 1250, 440, 56, INK, acc, num_col=LUCRO, den_col=VENDA)
        linha(c, [("= ", INK), ("20% da VENDA", VENDA)], 1530, 456, 40, ep(t, C["13.c"] + 1.8, 0.4))
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 720, ad, "COM 100, CABE DE CABEÇA", GREEN, -3, 36)


# ======================================================================
# bloco f — formar o preço
# ======================================================================

def b_preco(c, t, C, B):
    head_seq(c, t, C, [("14", "CUSTO R$ 72 · MARGEM 20%", "QUAL É O PREÇO?", PURPLE),
                       ("15", "E SE FOR SOBRE A VENDA?", "DIVIDA PELA FATIA DO CUSTO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            pergunta(c, "20% DE QUÊ?", W / 2, 250, aa, AMBER, 44)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            dono(c, "SOBRE O CUSTO", 520, 400, CUSTO, ab, 28)
            text(c, "é um ACRÉSCIMO: multiplique pelo fator", 520, 490, 30, "black", INK2, ab)
            linha(c, [("R$ 72 × 1,20 = ", INK), ("R$ 86,40", VENDA)], W / 2, 620, 64, ep(t, C["14.b"] + 2.0, 0.4))
            pill(c, "V = C · (1 + m)", W / 2, 740, PURPLE, size=30, a=ep(t, C["14.b"] + 3.0, 0.4), anchor="center")
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        K.pizza(c, 480, 480, 200, 5, 1, aa, sel_col=LUCRO, pull=0.6)
        text(c, "20% lucro", 640, 270, 30, "black", LUCRO, aa)
        text(c, "80% = CUSTO", 420, 730, 36, "black", CUSTO, ep(t, C["15.a"] + 1.6, 0.4))
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("0,80 · V = ", INK), ("R$ 72", CUSTO)], 1250, 320, 50, ab)
        fr(c, "R$ 72", "0,80", 1120, 470, 56, INK, ep(t, C["15.b"] + 2.0, 0.4), num_col=CUSTO, den_col=INK)
        linha(c, [("= ", INK), ("R$ 90,00", VENDA)], 1400, 486, 56, ep(t, C["15.b"] + 3.0, 0.4))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        boxed(c, 940, 600, 680, 170, LUCRO, acc, 0.08)
        text(c, "CONFIRA EM REAIS", 1280, 650, 26, "black", LUCRO, acc)
        linha(c, [("lucro R$ 18 ÷ ", INK), ("R$ 90", VENDA), (" = 20% ✓", LUCRO)], 1280, 715, 40, acc)


def b_atalho2(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "MULTIPLICA OU DIVIDE?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    K.atalho(c, 220, 200, 1480, 150, "ATALHO",
             ["sobre a VENDA: divida o custo pela fatia que sobra (1 − m)"], aa, 38)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        for k, (m, f) in enumerate((("20%", "÷ 0,80"), ("25%", "÷ 0,75"))):
            a = ep(t, C["16.b"] + k * 1.6, 0.4)
            x = 560 + k * 800
            rrect(c, x - 300, 410, 600, 170, 24, "#FFFFFF", a, shadow=True)
            text(c, "margem de " + m + " da venda", x, 470, 30, "black", VENDA, a)
            text(c, "custo " + f, x, 545, 50, "black", PURPLE, a)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        regra(c, "SEMPRE CONFIRA: lucro em R$ ÷ base pedida", W / 2, 700, acc, 38, GREEN)


# ======================================================================
# bloco g — imposto e comissão
# ======================================================================

def b_imposto(c, t, C, B):
    head(c, t, B["start"], "IMPOSTO E COMISSÃO", "TAMBÉM SÃO SOBRE A VENDA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        text(c, "COMISSÃO = a parte do preço que fica com quem intermediou", W / 2, 240, 30, "black", BLUE, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        X0, ESC = 300, 2.4
        barra_reais(c, X0, 320, 400 * ESC, 90, VENDA, ab, None, "PREÇO = 100%")
        g = ep(t, C["17.b"] + 0.8, 0.8)
        xr = X0 + 400 * ESC
        rrect(c, xr - 60 * ESC, lerp(320, 450, g), 60 * ESC, 90, 12, mix("#FFFFFF", RED, 0.35), ab)
        fmid(c, "−15%", xr - 30 * ESC, lerp(365, 495, g), 34, "black", RED, ab)
        text(c, "vai embora", xr - 30 * ESC, lerp(440, 570, g), 26, "black", RED, ab * g)
        linha(c, [("fica com ", INK), ("85%", LUCRO)], X0 + 170 * ESC, 470, 38, ep(t, C["17.b"] + 1.6, 0.4))
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("quer receber ", INK), ("R$ 340", LUCRO), (":", INK)], 520, 640, 40, acc)
        fr(c, "R$ 340", "0,85", 1060, 626, 50, INK, ep(t, C["17.c"] + 1.4, 0.4), num_col=LUCRO, den_col=INK)
        linha(c, [("= ", INK), ("R$ 400", VENDA)], 1320, 640, 52, ep(t, C["17.c"] + 2.4, 0.4))
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        conferido(c, "15% de 400 = 60  →  400 − 60 = 340", 520, 770, ad, True, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "UM LUCRO, DOIS DONOS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        etiqueta(c, 420, 300, 300, 100, aa, "R$ 50", CUSTO, -4)
        text(c, "CUSTO", 420, 390, 28, "black", CUSTO, aa)
        etiqueta(c, 820, 300, 300, 100, aa, "R$ 80", VENDA, 4)
        text(c, "VENDA", 820, 390, 28, "black", VENDA, aa)
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0 and t < C["19"]:
        text(c, "lucro sobre o CUSTO = ?", 620, 520, 40, "black", CUSTO, ab)
        text(c, "lucro sobre a VENDA = ?", 620, 600, 40, "black", VENDA, ab)
    pause_timer(c, t, C["18.end"] - 1.9, 1400, 420)
    if t < C["19"]:
        return
    a1 = ep(t, C["19.a"], 0.4)
    if a1 > 0:
        linha(c, [("lucro: 80 − 50 = ", INK), ("R$ 30", LUCRO)], 620, 490, 40, a1)
    ab2 = ep(t, C["19.b"], 0.5)
    if ab2 > 0:
        fr(c, "30", "50", 380, 640, 40, INK, ab2, num_col=LUCRO, den_col=CUSTO)
        linha(c, [("= ", INK), ("60% do CUSTO", CUSTO)], 620, 654, 34, ab2)
    acc2 = ep(t, C["19.c"], 0.5)
    if acc2 > 0:
        fr(c, "30", "80", 1100, 640, 40, INK, acc2, num_col=LUCRO, den_col=VENDA)
        linha(c, [("= ", INK), ("37,5% da VENDA", VENDA)], 1370, 654, 34, acc2)
    ad = ep(t, C["19.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 250, 560, 190, 24, mix("#FFFFFF", PURPLE, 0.08), ad)
        text(c, "PELA CONVERSÃO", 1360, 300, 26, "black", PURPLE, ad)
        linha(c, [("0,6 ÷ 1,6 = ", INK), ("0,375", VENDA)], 1360, 370, 40, ad)
        conferido(c, "bateu", 1250, 780, ad, True, 34)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Toda porcentagem tem dono: escreva a base antes de calcular.",
          "Margem sobre o custo, multiplique; margem sobre a venda, divida por 1 − m.",
          "Lucro sobre a venda nunca chega a 100%."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "34"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1360, 60)


ERROS = [("Lucro sobre a VENDA dividindo pelo CUSTO", "o custo é a base de sempre, a convenção",
          "R$ 20 numa venda de R$ 100: 20% da VENDA e 25% do CUSTO. Leia o dono"),
         ("Margem sobre a VENDA multiplicando o custo", "R$ 60 + 25% = R$ 75, rapidinho",
          "o lucro de R$ 15 é só 20% de 75. Divida: 60 ÷ 0,75 = R$ 80"),
         ("Descontar o imposto da margem em pontos: 40% − 10% = 30%", "as duas são porcentagens, parece só subtrair",
          "bases diferentes! custo 100, venda 140, imposto 14: lucro de 26%. Calcule em REAIS"),
         ("Aceitar margem SOBRE A VENDA acima de 100%", "markup de 125% existe",
          "a fatia nunca é maior que a pizza: ELIMINE a alternativa")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23", "24"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _fonte(c, t, C, cue_out, a0):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[cue_out], 0.3)),
         align="left")


ALTS1 = [("A", "20%", "dividiu pela VENDA", RED), ("B", "25%", "", GREEN), ("C", "30%", "R$ 30 virou 30%", RED),
         ("D", "80%", "custo ÷ venda", RED), ("E", "125%", "venda ÷ custo (fator 1,25)", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "LUCRO SOBRE O CUSTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("Um comerciante comprou uma mochila por R$ 120,00 e a vendeu por R$ 150,00. O lucro obtido, "
                           "em relação ao preço de custo, foi de", INK)], a0, 240, 28)
    _fonte(c, t, C, "26", a0)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["26.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 140)
    if t >= C["26"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["26"], 0.4))
        if t < C["27"]:
            dono(c, "DONO: custo (R$ 120)", 540, y0 + 60, CUSTO, ep(t, C["26"], 0.4), 24)
            linha(c, [("lucro: 150 − 120 = ", INK), ("R$ 30", LUCRO)], 540, y0 + 150, 34, ep(t, C["26.a"], 0.4))
            ab = ep(t, C["26.b"], 0.4)
            if ab > 0:
                fr(c, "30", "120", 420, y0 + 250, 40, INK, ab, num_col=LUCRO, den_col=CUSTO)
                linha(c, [("= ", INK), ("25% do CUSTO", CUSTO)], 680, y0 + 264, 36, ab)
        else:
            ax = ep(t, C["27"], 0.4)
            dono(c, "pediu o CUSTO", 540, y0 + 60, CUSTO, ax, 24)
            text(c, "a VENDA é outro dono", 540, y0 + 150, 30, "black", VENDA, ax)
            text(c, "R$ 30 ≠ 30%", 540, y0 + 220, 34, "black", RED, ep(t, C["27.xc"], 0.4))
            text(c, "1,25 é FATOR, não %", 540, y0 + 290, 30, "black", AMBER, ep(t, C["27.xe"], 0.4))


ALTS2 = [("A", "R$ 45,00", "60 × 0,75", RED), ("B", "R$ 75,00", "+25% ao custo", RED), ("C", "R$ 80,00", "", GREEN),
         ("D", "R$ 85,00", "+R$ 25", RED), ("E", "R$ 240,00", "60 ÷ 0,25", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "PREÇO COM MARGEM SOBRE A VENDA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, [("Uma artesã gasta R$ 60,00 para produzir cada peça. Ela quer que o lucro corresponda a 25% do "
                           "preço de venda. O preço de venda de cada peça deve ser", INK)], a0, 240, 28)
    _fonte(c, t, C, "29", a0)
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["29.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["28.end"] - 1.9, 540, yend + 140)
    if t >= C["29"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["29"], 0.4))
        ap = ep(t, C["29"], 0.4)
        K.pizza(c, 300, y0 + 150, 100, 4, 1, ap, sel_col=LUCRO, pull=0.6)
        dono(c, "DONO: venda", 640, y0 + 60, VENDA, ap, 22)
        text(c, "75% = custo R$ 60", 640, y0 + 150, 28, "black", CUSTO, ep(t, C["29.a"], 0.4))
        ab = ep(t, C["29.b"], 0.4)
        if ab > 0:
            linha(c, [("60 ÷ 0,75 = ", INK), ("R$ 80", VENDA)], 640, y0 + 220, 34, ab)
        acc = ep(t, C["29.c"], 0.4)
        if acc > 0:
            linha(c, [("20 ÷ 80 = 25% ✓", LUCRO)], 540, y0 + 320, 32, acc)


ALTS7 = [("A", "cerca de 18%", "dividiu pela VENDA", RED), ("B", "27,5%", "", GREEN),
         ("C", "35%", "50 − 15: bases diferentes", RED), ("D", "42,5%", "15% da margem", RED),
         ("E", "50%", "lucro bruto", RED)]


def b_q7(c, t, C, B):
    head_seq(c, t, C, [("31", "QUESTÃO 7 · VOCÊ FAZ", "PAUSE E RESOLVA", GREEN), ("32", "QUESTÃO 7 · CONFERINDO", "LUCRO LÍQUIDO", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["31.a"], 0.4)
    yend = _enunciado(c, [("Um revendedor compra um produto por R$ 400,00 e o vende por R$ 600,00. Sobre o preço de venda, "
                           "ele paga 10% de imposto e 5% de comissão ao vendedor. O lucro líquido do revendedor, em "
                           "relação ao preço de custo, é de", INK)], a0, 230, 26, 700)
    _fonte(c, t, C, "32", a0)
    cues_in = {L: C[f"31.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"33.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 250, 680, 44, C["32.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["31.end"] - 2.4, 540, yend + 120)
    if t >= C["32"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["32"], 0.4))
        if t < C["33"]:
            aa = ep(t, C["32.a"], 0.4)
            if aa > 0:
                linha(c, [("15% de ", INK), ("R$ 600", VENDA), (" = ", INK), ("R$ 90", RED)], 540, y0 + 50, 32, aa)
            ab = ep(t, C["32.b"], 0.4)
            if ab > 0:
                linha(c, [("600 − 90 = ", INK), ("R$ 510", INK)], 540, y0 + 110, 32, ab)
                linha(c, [("510 − 400 = ", INK), ("R$ 110", LUCRO)], 540, y0 + 170, 32, ep(t, C["32.b"] + 2.0, 0.4))
            acc = ep(t, C["32.c"], 0.4)
            if acc > 0:
                fr(c, "110", "400", 400, y0 + 250, 34, INK, acc, num_col=LUCRO, den_col=CUSTO)
                linha(c, [("= ", INK), ("27,5% do CUSTO", CUSTO)], 660, y0 + 262, 30, acc)
        else:
            ax = ep(t, C["33"], 0.4)
            text(c, "imposto: base VENDA", 540, y0 + 60, 28, "black", VENDA, ax)
            text(c, "lucro: base CUSTO", 540, y0 + 110, 28, "black", CUSTO, ax)
            selo(c, 540, y0 + 200, ep(t, C["33.xc"], 0.4), "50 − 15 = 35? NÃO", RED, -3, 28)
            text(c, "calcule em REAIS", 540, y0 + 290, 30, "black", GREEN, ep(t, C["33.xd"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DESCONTOS ENCADEADOS", PURPLE)
    aa = ep(t, C["35.a"], 0.5)
    for k, (s, col) in enumerate((("−20% liquidação", RED), ("−5% no Pix", RED), ("+10% frete", AMBER))):
        a = aa * ep(t, C["35.a"] + k * 1.4, 0.4)
        if a > 0:
            chip(c, s, 470 + k * 490, 360, col, a, 48)
    ab = ep(t, C["35.b"], 0.5)
    if ab > 0:
        linha(c, [("−20 − 5 + 10 = ", INK), ("−15%", AMBER), ("  ?", INK)], W / 2, 560, 64, ab)
        selo(c, 1480, 580, ep(t, C["35.b"] + 1.4, 0.4), "SERÁ?", AMBER, -6, 44)
    pill(c, "ep. 2 · descontos encadeados", W / 2, 760, PURPLE, size=30, a=ep(t, C["35.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["36.like"], C["36.sub"], C["36.bell"], C["36.com"], C["36.bye"],
        "Você já vendeu alguma coisa? Quanto lucrou?", canal="no Estudativo", anki=C["36.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              base=b_base, prejuizo=b_prejuizo, pizza=b_pizza, converter=b_converter, atalho1=b_atalho1,
              preco=b_preco, atalho2=b_atalho2, imposto=b_imposto, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q1=b_q1, q2=b_q2, q7=b_q7, ponte=b_ponte, cta=b_cta)
