"""Visual — Taxas Equivalentes e Inflação, Episódio 3: inflação, inflação acumulada e poder de compra (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, mdraw...).
Peças deste episódio: carrinho() (carrinho de supermercado com 100 itens de R$ 1,00; os 20 de cima saem quando o preço
vai a R$ 1,25), escada() (a ESCADA ROLANTE DE PREÇOS: degraus que andam; mais lenta com inflação menor; invertida =
deflação), cesta() (cesta de compras com etiqueta de preço), nota() (nota de R$ 100,00), linha(), caixa(), conferido().
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
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_taxas_inflacao_ep3_inflacao_poder_compra.mp4"
CARD_R = K.CARD_R


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    text(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def caixa(c, cx, cy, tit, val, col, a, w=360, sub=None, h=140):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 33, 24, "black", col, a)
    size = 44
    while text_w(val, "black", size) > w - 30:
        size -= 2
    text_mid(c, val, cx, cy + 22, size, "black", INK, a)
    if sub:
        text(c, sub, cx, cy + h / 2 + 34, 24, "bold", GRAY, a)


ITEM_CORES = ["#E8505B", "#F5A623", "#4A90E2", "#7ED321", "#9B59B6"]


def carrinho(c, cx, cy, a, sai=0.0, preco="R$ 1,00", preco_novo=None, troca=0.0, n=100, s=1.0):
    """carrinho de supermercado com n itens (10 por fileira); sai = progresso da saída dos 20 itens de cima"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    bw, bh = 460, 300                      # cesto (trapézio)
    p = skia.Path()
    p.moveTo(-bw / 2, -bh / 2); p.lineTo(bw / 2, -bh / 2); p.lineTo(bw / 2 - 50, bh / 2); p.lineTo(-bw / 2 + 50, bh / 2)
    p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    # itens: 10 colunas × 10 fileiras dentro do cesto
    cell = 34
    x0 = -cell * 5 + 2
    y_base = bh / 2 - 12
    u = ease_io(clamp(sai))
    for k in range(n):
        row, col = divmod(k, 10)
        x = x0 + col * cell
        y = y_base - (row + 1) * (cell - 6)
        alpha = a
        dx = dy = 0
        cor = ITEM_CORES[(row * 3 + col) % len(ITEM_CORES)]
        if row >= 8 and u > 0:            # os 20 de cima saem
            dx = u * (260 + col * 18)
            dy = -u * (140 + (row - 8) * 60)
            alpha = a * (1 - u)
            cor = mix(cor, RED, u)
        rrect(c, x + dx, y + dy, cell - 6, cell - 10, 6, cor, alpha)
    c.drawPath(p, paint(INK2, a, stroke=7))
    for k in range(1, 4):                   # grade do cesto
        yy = -bh / 2 + k * bh / 4
        line(c, -bw / 2 + 12 * k, yy, bw / 2 - 12 * k, yy, INK2, a * 0.25, 3)
    line(c, bw / 2, -bh / 2, bw / 2 + 70, -bh / 2 - 60, INK2, a, 8)        # alça
    line(c, bw / 2 + 70, -bh / 2 - 60, bw / 2 + 140, -bh / 2 - 60, INK2, a, 8)
    line(c, -bw / 2 + 50, bh / 2, -bw / 2 + 30, bh / 2 + 60, INK2, a, 7)
    line(c, -bw / 2 + 30, bh / 2 + 60, bw / 2 - 30, bh / 2 + 60, INK2, a, 7)
    for wx in (-bw / 2 + 70, bw / 2 - 70):
        c.drawCircle(wx, bh / 2 + 90, 24, paint(INK2, a))
        c.drawCircle(wx, bh / 2 + 90, 9, paint("#FFFFFF", a))
    # etiqueta de preço por item
    tx, ty = -bw / 2 - 150, -bh / 2 + 10
    rrect(c, tx - 100, ty - 44, 200, 88, 16, "#FFF7E0", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(tx - 100, ty - 44, 200, 88), 16, 16), paint(AMBER, a, stroke=4))
    text(c, "cada item", tx, ty - 58, 22, "bold", GRAY, a)
    tr = clamp(troca)
    text_mid(c, preco, tx, ty, 40, "black", INK, a * (1 - tr))
    if preco_novo and tr > 0:
        text_mid(c, preco_novo, tx, ty, 40, "black", RED, a * tr)
    c.restore()


def escada(c, x0, y0, w, h, a, t=0.0, vel=1.0, sobe=True, col=None, rot="", n=9):
    """ESCADA ROLANTE DE PREÇOS: trilho inclinado com degraus que andam (vel = velocidade); sobe=False inverte (deflação)"""
    if a <= 0:
        return
    col = col or (PURPLE if sobe else RED)
    xa, ya, xb, yb = x0, y0 + h, x0 + w, y0           # trilho de baixo-esquerda para cima-direita
    # corpo
    p = skia.Path()
    p.moveTo(xa - 30, ya + 30); p.lineTo(xb + 30, yb + 30); p.lineTo(xb + 30, yb + 90); p.lineTo(xa - 30, ya + 90)
    p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.12), a))
    line(c, xa - 30, ya - 50, xb + 30, yb - 50, col, a, 8)      # corrimão
    line(c, xa - 30, ya + 30, xb + 30, yb + 30, INK2, a, 6)
    # degraus andando
    ph = (t * 0.22 * vel) % 1.0
    if not sobe:
        ph = 1.0 - ph
    for k in range(n):
        u = (k + ph) / n
        sx = xa + (xb - xa) * u
        sy = ya + (yb - ya) * u
        rrect(c, sx - 26, sy - 10, 52, 36, 6, col, a * 0.85)
    # seta de sentido
    if sobe:
        arrow(c, xb - 40, yb - 120, xb + 40, yb - 170, col, a, 7, 24)
    else:
        arrow(c, xa + 40, ya - 170, xa - 40, ya - 120, col, a, 7, 24)
    if rot:
        pill(c, rot, (xa + xb) / 2, (ya + yb) / 2 + 150, col, size=30, a=a, anchor="center", bounds=(0, 1920))


def cesta(c, cx, cy, a, preco, col=INK, s=1.0):
    """cesta de compras com produtos e uma etiqueta de preço"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    for k, (dx, hh, cor) in enumerate(((-90, 120, "#F5A623"), (-30, 160, "#E8505B"), (40, 130, "#4A90E2"),
                                        (100, 100, "#7ED321"))):
        rrect(c, dx - 26, -hh + 10, 52, hh, 10, cor, a)
    p = skia.Path()
    p.moveTo(-170, -10); p.lineTo(170, -10); p.lineTo(130, 150); p.lineTo(-130, 150); p.close()
    c.drawPath(p, paint("#C98B4B", a))
    for k in range(1, 4):
        line(c, -170 + 12 * k, -10 + k * 40, 170 - 12 * k, -10 + k * 40, "#8A5A2B", a, 4)
    c.drawArc(skia.Rect.MakeLTRB(-130, -170, 130, 70), 200, 140, False, paint("#8A5A2B", a, stroke=10))
    rrect(c, 60, 110, 220, 80, 14, "#FFFFFF", a, shadow=True)
    text_mid(c, preco, 170, 150, 40, "black", col, a)
    c.restore()


def nota(c, cx, cy, a, w=420, h=200):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 18, "#BFE3C8", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 12, cy - h / 2 + 12, w - 24, h - 24), 12, 12),
                paint("#3E8E5A", a, stroke=4))
    c.drawCircle(cx - w / 2 + 90, cy, 50, paint("#3E8E5A", a * 0.25))
    text_mid(c, "100", cx + 60, cy - 8, 96, "black", "#2C6B42", a)
    text(c, "REAIS", cx + 60, cy + 70, 26, "black", "#2C6B42", a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "INFLAÇÃO E PODER DE COMPRA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        caixa(c, 520, 330, "PREÇOS", "× 2", RED, aa, 380, sub="inflação de 100%")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        nota(c, 520, 640, ab * (1 - 0.6 * ep(t, C["01.c"], 0.6)), 380, 180)
        text_mid(c, "vira pó?", 520, 800, 50, "black", AMBER, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 260, 720, 260, 26, mix("#FFFFFF", BLUE, 0.10), acc, shadow=True)
        text(c, "o dinheiro compra", 1360, 330, 34, "bold", GRAY, acc)
        text_mid(c, "METADE", 1360, 420, 96, "black", BLUE, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        linha(c, [("perda de ", INK2), ("50%", GREEN)], 1360, 610, 58, ad)
        linha(c, [("não de 100%", RED)], 1360, 700, 44, ad)
        strike(c, 1240, 700, 1480, 700, ep(t, C["01.d"] + 1.0, 0.4), RED, ep(t, C["01.d"] + 1.0, 0.4))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "calcular a inflação acumulada", PURPLE),
             ("02.b", "calcular a perda de poder de compra", BLUE)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 200 + d
        rrect(c, 260, y, 1400, 160, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
        check_icon(c, 340, y + 80, 30, a, col)
        text_mid(c, s, 400, y + 80, 46, "black", INK, a, align="left")
    a3 = ep(t, C["02.b"] + 1.6, 0.5)
    if a3 > 0:
        selo(c, W / 2, 760, a3, "SEM CONFUNDIR AS DUAS", AMBER, -3, 36)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "2 LEMBRETES", "RÁPIDOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 200, 280 + d1, 720, 460, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "VARIAÇÃO PERCENTUAL", 560, 330 + d1, GREEN, size=26, a=a1, anchor="center", bounds=(0, 1920))
        K.mdraw(c, "novo/antigo − 1", 560, 500 + d1, 64, PURPLE, a1, align="center")
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 280 + d2, 720, 460, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "SÉRIE DE PORCENTAGEM", 1360, 330 + d2, GREEN, size=26, a=a2, anchor="center", bounds=(0, 1920))
        text(c, "voltar ao original:", 1360, 430 + d2, 36, "black", INK2, a2)
        text(c, "DIVIDA PELO FATOR", 1360, 485 + d2, 40, "black", PURPLE, a2)
        a3 = ep(t, C["03.b"] + 3.4, 0.4)
        linha(c, [("100", INK), (" → ", GRAY), ("125", RED), (" → ", GRAY), ("100", BLUE)], 1360, 600 + d2, 48, a3)
        text(c, "+25%          −20%", 1360, 680 + d2, 30, "black", GRAY, a3)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "A CESTA DE COMPRAS", "A MESMA CESTA, MAIS CARA", BLUE),
                       ("05", "A NOTA NA GAVETA", "COMPRA CADA VEZ MENOS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        ab = ep(t, C["04.b"], 0.5)
        cesta(c, 560, 470, ab, "R$ 500,00", BLUE, 1.15)
        if ab > 0:
            pill(c, "COMEÇO DO ANO", 560, 720, BLUE, size=28, a=ab, anchor="center", bounds=(0, 1920))
        acc = ep(t, C["04.c"], 0.5)
        cesta(c, 1340, 470, acc, "R$ 540,00", RED, 1.15)
        if acc > 0:
            pill(c, "FIM DO ANO", 1340, 720, RED, size=28, a=acc, anchor="center", bounds=(0, 1920))
            arrow(c, 820, 420, 1080, 420, GRAY, acc, 6, 22)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 810, ad, "MESMOS PRODUTOS · MAIS CARO", AMBER, -2, 30)
        return
    aa = ep(t, C["05.a"], 0.5)
    nota(c, 520, 470, aa)
    if aa > 0:
        text(c, "R$ 100,00", 520, 640, 40, "black", INK, aa)
    for k in range(3):
        a = ep(t, C["05.c"] + k * 0.8, 0.5)
        if a <= 0:
            continue
        y = 320 + k * 150
        text(c, f"ano {k + 1}", 960, y + 14, 30, "black", GRAY, a, align="left")
        n = 10 - 2 * k
        for j in range(n):
            rrect(c, 1080 + j * 56, y - 24, 44, 52, 8, ITEM_CORES[j % 5], a)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1380, 790, ad, "O QUE VAMOS MEDIR HOJE", BLUE, -3, 30)


# ======================================================================
# bloco a — inflação e índice
# ======================================================================

def b_indice(c, t, C, B):
    head_seq(c, t, C, [("06", "O QUE É INFLAÇÃO", "E COMO SE MEDE", BLUE),
                       ("07", "A INFLAÇÃO DA CESTA", "FATOR PRIMEIRO, TAXA DEPOIS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        defs = [("06.a", "INFLAÇÃO", "aumento geral dos preços num período"),
                ("06.b", "ÍNDICE DE PREÇOS", "acompanha o custo de uma CESTA FIXA"),
                ("06.c", "IPCA · IBGE", "o índice oficial do Brasil e quem calcula")]
        for k, (cue, nome, sig) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 250 + k * 190 + d
            rrect(c, 230, y, 1460, 160, 22, mix("#FFFFFF", BLUE, 0.07), a, shadow=True)
            badge_num(c, k + 1, 310, y + 80, a, 30, bg=BLUE)
            text(c, nome, 380, y + 70, 44, "black", BLUE, a, align="left")
            text(c, sig, 380, y + 122, 32, "bold", INK2, a, align="left")
        return
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        K.mdraw(c, "540/500 = 1,08", W / 2, 360, 80, INK, aa, align="center")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("fator ", GRAY), ("1,08", PURPLE), ("  →  1,08 − 1 = 0,08  →  ", INK2), ("8%", RED)], W / 2, 540,
              50, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        K.atalho(c, 410, 640, 1100, 170, "ATALHO", ["fator primeiro, taxa depois:  taxa = fator − 1"], acc, 36)


# ======================================================================
# bloco b — inflação acumulada
# ======================================================================

def b_acumulada(c, t, C, B):
    head_seq(c, t, C, [("08", "INFLAÇÃO ACUMULADA", "MULTIPLIQUE OS FATORES", PURPLE),
                       ("09", "DE ONDE VEM O 0,2?", "PREÇO QUE JÁ SUBIU", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            rrect(c, 230, 240, 1460, 120, 22, mix("#FFFFFF", BLUE, 0.07), aa)
            text(c, "INFLAÇÃO ACUMULADA = a alta total de vários períodos seguidos", W / 2, 312, 36, "black", BLUE, aa)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            K.chip(c, "ano 1: 5%  →  × 1,05", 620, 450, PURPLE, ab, 36)
            K.chip(c, "ano 2: 4%  →  × 1,04", 1300, 450, PURPLE, ab, 36)
            linha(c, [("5% + 4% = 9% ?", AMBER)], W / 2, 560, 44, ab)
            strike(c, 790, 560, 1130, 560, ep(t, C["08.c"], 0.4), RED, ep(t, C["08.c"], 0.4))
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            linha(c, [("1,05 · 1,04 = ", INK), ("1,092", PURPLE)], W / 2, 670, 56, acc)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 790, ad, "9,2%, NÃO 9%", GREEN, -3, 40)
        return
    aa = ep(t, C["09.a"], 0.5)
    for k, (tit, val, sub, col) in enumerate((("COMEÇO", "R$ 100,00", "", BLUE),
                                              ("ANO 1 (+5%)", "R$ 105,00", "5% de 100 = 5", PURPLE),
                                              ("ANO 2 (+4%)", "R$ 109,20", "4% de 105 = 4,20", RED))):
        a = ep(t, C["09.t"] + k * 0.8, 0.5) if k < 2 else aa
        caixa(c, 440 + k * 520, 330, tit, val, col, a, 440, sub=sub)
        if k:
            arrow(c, 440 + (k - 1) * 520 + 225, 330, 440 + k * 520 - 225, 330, col, a, 5, 18)
    if aa > 0:
        selo(c, 1480, 500, ep(t, C["09.a"] + 2.0, 0.4), "+ 0,20 A MAIS", AMBER, -4, 28)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        K.atalho(c, 360, 560, 1200, 250, "ATALHO · DUAS TAXAS",
                 [("m", "a + b + {a·b}/100"), "5 + 4 + 20 ÷ 100 = 9,2%"], ab, 40)


# ======================================================================
# bloco c — a escada rolante
# ======================================================================

def b_escada(c, t, C, B):
    head_seq(c, t, C, [("10", "INFLAÇÃO CAIU, PREÇO CAIU?", "A ESCADA ROLANTE DE PREÇOS", AMBER),
                       ("11", "PREÇO DESCENDO DE VERDADE", "DEFLAÇÃO", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        ab = ep(t, C["10.b"], 0.5)
        escada(c, 270, 400, 520, 280, ab, t, vel=2.0, rot="8% ao ano · rápida")
        acc = ep(t, C["10.c"], 0.5)
        escada(c, 1050, 470, 560, 200, acc, t, vel=1.0, rot="4% ao ano · mais lenta")
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 770, ad, "AS DUAS AINDA SOBEM", AMBER, -3, 34)
        return
    aa = ep(t, C["11.a"], 0.5)
    escada(c, 260, 380, 520, 280, aa, t, vel=1.2, sobe=False, rot="preços caindo")
    if aa > 0:
        selo(c, 520, 300, ep(t, C["11.a"] + 1.2, 0.4), "DEFLAÇÃO", RED, -4, 44)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        x0, y0 = 1000, 270
        rrect(c, x0, y0, 330, 470, 20, "#FFFFFF", ab, shadow=True)
        rrect(c, x0 + 360, y0, 330, 470, 20, "#FFFFFF", ab, shadow=True)
        text(c, "TAXA", x0 + 165, y0 + 50, 28, "black", AMBER, ab)
        text(c, "PREÇO", x0 + 525, y0 + 50, 28, "black", PURPLE, ab)
        for k, v in enumerate((8, 6, 4)):
            hh = v * 34
            rrect(c, x0 + 50 + k * 85, y0 + 420 - hh, 60, hh, 8, AMBER, ab)
            text(c, f"{v}%", x0 + 80 + k * 85, y0 + 405 - hh, 26, "black", AMBER, ab)
        pts = [100, 108, 114.48, 119.06]
        X = lambda k: x0 + 400 + k * 85
        Y = lambda v: y0 + 420 - (v - 90) * 9
        for k in range(3):
            line(c, X(k), Y(pts[k]), X(k + 1), Y(pts[k + 1]), PURPLE, ab, 7)
        for k, v in enumerate(pts):
            c.drawCircle(X(k), Y(v), 9, paint(PURPLE, ab))
        text(c, "desce", x0 + 165, y0 + 455, 24, "bold", GRAY, ab)
        text(c, "sobe", x0 + 525, y0 + 455, 24, "bold", GRAY, ab)
        text(c, "≠", x0 + 345, y0 + 260, 60, "black", RED, ab)


# ======================================================================
# bloco d — poder de compra
# ======================================================================

def b_poder(c, t, C, B):
    head_seq(c, t, C, [("12", "PODER DE COMPRA", "O CARRINHO DE R$ 100", BLUE),
                       ("13", "PODER DE COMPRA", "UMA DIVISÃO", PURPLE),
                       ("14", "A PERDA SEM RODEIO", "PERDEU OU RESTOU?", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            rrect(c, 230, 230, 1460, 90, 20, mix("#FFFFFF", BLUE, 0.07), aa)
            text(c, "PODER DE COMPRA = quanto o seu dinheiro consegue comprar", W / 2, 290, 34, "black", BLUE, aa)
        ab = ep(t, C["12.b"], 0.5)
        carrinho(c, 900, 540, ab, sai=ep(t, C["12.d"], 1.6), preco_novo="R$ 1,25", troca=ep(t, C["12.c"] + 1.4, 0.5),
                 s=0.95)
        if ab > 0:
            text(c, "R$ 100,00", 1560, 420, 44, "black", INK, ab)
            text(c, "no bolso", 1560, 465, 26, "bold", GRAY, ab)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            pill(c, "inflação de 25%", 420, 760, RED, size=30, a=acc, anchor="center", bounds=(0, 1920))
        ad = ep(t, C["12.d"] + 1.2, 0.5)
        if ad > 0:
            text_mid(c, "sobram 80", 1560, 600, 50, "black", BLUE, ad)
        ae = ep(t, C["12.e"], 0.5)
        if ae > 0:
            selo(c, 1500, 760, ae, "PERDA DE 20%, NÃO DE 25%", GREEN, -4, 30)
        return
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        if aa > 0:
            rrect(c, 430, 230, 1060, 150, 22, mix("#FFFFFF", PURPLE, 0.10), aa, shadow=True)
            text_mid(c, "poder de compra =", 760, 305, 42, "black", PURPLE, aa)
            K.mdraw(c, "1/{1+π}", 1120, 305, 64, PURPLE, aa, align="left")
            text(c, "π = inflação", 1380, 320, 24, "bold", GRAY, aa)
        rows = [("13.b", "25%", "1 ÷ 1,25 = 0,80", "20%", "80%"),
                ("13.c", "100%", "1 ÷ 2 = 0,50", "50%", "50%"),
                ("13.d", "10%", "1 ÷ 1,1 ≈ 0,909", "≈ 9,1%", "≈ 90,9%")]
        hdr = ep(t, C["13.b"], 0.4)
        for x, s_, col in ((380, "INFLAÇÃO", RED), (820, "CONTA", PURPLE), (1240, "RESTOU", BLUE),
                           (1560, "PERDEU", GREEN)):
            text(c, s_, x, 450, 26, "black", col, hdr)
        for k, (cue, inf, conta, perda, resto) in enumerate(rows):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 480 + k * 110 + d
            rrect(c, 250, y, 1420, 90, 16, "#FFFFFF", a, shadow=True)
            text_mid(c, inf, 380, y + 45, 40, "black", RED, a)
            text_mid(c, conta, 820, y + 45, 38, "black", INK2, a)
            text_mid(c, resto, 1240, y + 45, 40, "black", BLUE, a)
            text_mid(c, perda, 1560, y + 45, 40, "black", GREEN, a)
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 240, 1200, 200, 24, mix("#FFFFFF", GREEN, 0.08), aa, shadow=True)
        text(c, "ATALHO", W / 2, 285, 22, "black", GREEN, aa, tracking=2)
        text_mid(c, "perda =", 820, 360, 50, "black", INK, aa)
        K.mdraw(c, "π/{1+π}", 960, 360, 70, GREEN, aa, align="left")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        K.mdraw(c, "25/125 = 20%", 620, 560, 60, INK, ab, align="center")
        K.mdraw(c, "100/200 = 50%", 1300, 560, 60, INK, ep(t, C["14.b"] + 2.6, 0.5), align="center")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        K.chip(c, "PERDEU?", 780, 740, GREEN, acc, 44)
        text_mid(c, "ou", W / 2, 740, 40, "black", GRAY, acc)
        K.chip(c, "RESTOU?", 1140, 740, BLUE, acc, 44)


# ======================================================================
# bloco e — por que a perda é menor
# ======================================================================

def b_menor(c, t, C, B):
    head(c, t, B["start"], "POR QUE A PERDA É MENOR?", "VOLTAR AO VALOR ORIGINAL", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    for k, (tit, val, sub, col) in enumerate((("PREÇO ANTIGO", "100", "", BLUE),
                                              ("PREÇO NOVO (+25%)", "125", "+ 25 sobre 100", RED),
                                              ("DE VOLTA (−20%)", "100", "− 25 sobre 125", GREEN))):
        a = ep(t, C["15.b"] + k * 0.9, 0.5) if k else aa
        caixa(c, 440 + k * 520, 340, tit, val, col, a, 440, sub=sub)
        if k:
            arrow(c, 440 + (k - 1) * 520 + 225, 340, 440 + k * 520 - 225, 340, col, a, 5, 18)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        linha(c, [("inflação: base ", INK2), ("100", BLUE), ("   ·   perda: base ", INK2), ("125", RED)], W / 2, 560,
              42, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        regra(c, "base maior, porcentagem menor", W / 2, 720, ad, 46, PURPLE)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "DIVIDA PELO FATOR", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        caixa(c, 640, 300, "INFLAÇÃO", "60%", RED, aa, 440)
        caixa(c, 1280, 300, "SALÁRIO", "congelado", BLUE, aa, 440)
    ab = ep(t, C["16.b"], 0.5)
    if t < C["17"]:
        if ab > 0:
            text_mid(c, "quanto perdeu de poder de compra?", W / 2, 470, 44, "black", INK, ab)
        pause_timer(c, t, C["16.end"] - 1.9, W / 2, 640)
        return
    a1 = ep(t, C["17.a"], 0.5)
    if a1 > 0:
        pill(c, "FATOR 1,6", 300, 470, PURPLE, size=26, a=a1, anchor="center", bounds=(0, 1920))
        K.mdraw(c, "1/1,6 = 0,625", 760, 470, 56, INK, a1, align="center")
    a2 = ep(t, C["17.b"], 0.5)
    if a2 > 0:
        linha(c, [("restou ", INK2), ("62,5%", BLUE), ("   ·   perdeu ", INK2), ("37,5%", GREEN)], 1430, 470, 36, a2)
    a3 = ep(t, C["17.c"], 0.5)
    if a3 > 0:
        pill(c, "ATALHO", 300, 640, GREEN, size=26, a=a3, anchor="center", bounds=(0, 1920))
        K.mdraw(c, "60/160 = 37,5%", 760, 640, 56, INK, a3, align="center")
        conferido(c, "abaixo dos 60%", 1180, 652, ep(t, C["17.c"] + 3.0, 0.4), True, 36)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Inflação se acumula multiplicando fatores.",
          "Poder de compra: divida pelo fator da inflação.",
          "Inflação caindo não é preço caindo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Somar inflações: 10% e 10% = 20%", "as duas são porcentagens, uma depois da outra",
          "a segunda incide sobre preço que já subiu: 1,1 · 1,1 = 1,21 → 21%"),
         ("Perda igual à inflação: inflação de 100% tira 100%", "o preço subiu 100, o dinheiro perdeu 100",
          "o dinheiro ainda compra metade: divida pelo fator → perda de 50%"),
         ("Inflação de 8% caiu para 4%: os preços caíram", "o número desceu",
          "desceu a velocidade da escada; preço caindo só com deflação")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


ALTSN = [("A", "5%", "25 − 20: diferença", RED), ("B", "22,5%", "média das taxas", RED),
         ("C", "45%", "soma das taxas", RED), ("D", "50%", "", GREEN), ("E", "150%", "leu o fator 1,50", RED)]


def b_qnova(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EU FAÇO", "INFLAÇÃO ACUMULADA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, "Em um país, a inflação foi de 25% em um ano e de 20% no ano seguinte. A inflação acumulada "
                      "nesses dois anos foi de", a0, size=32)
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTSN, 1000, 250, 680, 42, C["23.ok"], "D", cues_in, cues_x, gap=40)
    if t < C["23"]:
        pause_timer(c, t, C["22.end"] - 1.9, 540, 680)
        return
    y0 = yend + 10
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["23"], 0.4), shadow=True)
    pill(c, "MULTIPLIQUE OS FATORES", 540, y0 + 44, PURPLE, size=24, a=ep(t, C["23.a"], 0.4), anchor="center")
    linha(c, [("1,25 · 1,20 = ", INK), ("1,50", PURPLE), (" → ", INK2), ("50%", GREEN)], 540, y0 + 115, 36,
          ep(t, C["23.a"] + 1.5, 0.4))
    linha(c, [("100 → 125 → 150", INK)], 540, y0 + 190, 34, ep(t, C["23.b"], 0.4))
    linha(c, [("acima da soma (45%)", AMBER)], 480, y0 + 260, 30, ep(t, C["23.c"], 0.4))
    conferido(c, "faz sentido", 680, y0 + 270, ep(t, C["23.c"] + 2.0, 0.4), True, 28)


ALTS5 = [("A", "12,5%", "metade de 25, sem base", RED), ("B", "20%", "", GREEN),
         ("C", "25%", "perda = inflação", RED), ("D", "75%", "100 − 25: mistura", RED),
         ("E", "80%", "é o que RESTOU", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "PODER DE COMPRA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, "Durante um período, os preços de uma cidade subiram, em média, 25%, enquanto o salário de um "
                      "trabalhador permaneceu o mesmo. Em relação ao início do período, o poder de compra desse salário "
                      "diminuiu", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["26"], 0.3)), align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 42, C["26.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["26"]:
        pause_timer(c, t, C["25.end"] - 2.4, 540, 720, dur=2.1)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["26"], 0.4), shadow=True)
    linha(c, [("1 ÷ 1,25 = ", INK), ("0,80", BLUE), ("  restou 80%", INK2)], 540, y0 + 60, 32, ep(t, C["26.a"], 0.4))
    linha(c, [("diminuiu ", INK), ("20%", GREEN)], 540, y0 + 125, 36, ep(t, C["26.b"], 0.4))
    linha(c, [("100 unidades → 80 unidades", INK2)], 540, y0 + 190, 30, ep(t, C["26.c"], 0.4))
    conferido(c, "20% < 25%", 440, y0 + 255, ep(t, C["26.c"] + 3.0, 0.4), True, 30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TAXA REAL", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        caixa(c, 620, 380, "RENDEU", "+ 26%", GREEN, aa, 460)
        caixa(c, 1300, 380, "INFLAÇÃO", "+ 20%", RED, aa, 460)
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        linha(c, [("ficou ", INK), ("6%", AMBER), (" mais rico?", INK)], W / 2, 590, 64, ab)
    acc = ep(t, C["29.c"], 0.5)
    if acc > 0:
        pill(c, "ep. 4 · taxa real", W / 2, 760, PURPLE, size=34, a=acc, anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Inflação de 50%: quanto um salário congelado perde de poder de compra?", canal="no Estudativo",
        anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, indice=b_indice,
              acumulada=b_acumulada, escada=b_escada, poder=b_poder, menor=b_menor, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, qnova=b_qnova, q5=b_q5, ponte=b_ponte, cta=b_cta)
