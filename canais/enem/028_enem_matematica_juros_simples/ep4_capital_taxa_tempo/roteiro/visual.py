"""Visual — Juros Simples, Episódio 4: descobrindo capital, taxa ou tempo (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: mesa() (a MESA DE QUATRO PERNAS J, C, i, t; a perna que falta é reconstruída pela divisão),
pilhas() (o triplo: três pilhas de notas, a primeira é o capital, "já estava lá"), linha_tempo() (entrada no dia 0
riscada como "não financiada" e o pagamento no mês N), etiqueta() (C, i, t, J ou M com a unidade), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum028", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_simples_ep4_capital_taxa_tempo.mp4"
CARD_R = K.CARD_R
NOTA = "#7FBF8E"
NOTA2 = "#5FA371"
MADEIRA = "#C99A6B"
MADEIRA2 = "#A97C50"

# cor de cada letra da fórmula
COR = dict(C=BLUE, i=PURPLE, t=AMBER, J=GREEN, M=RED, k=INK)


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


def formula(c, cx, cy, size, a, s="J = C · i · t"):
    """fórmula com cada letra na sua cor"""
    if a <= 0:
        return
    linha(c, [(ch, COR.get(ch, INK)) for ch in s], cx, cy, size, a)


def contorno(c, x, y, w, h, r, col, a, width=3):
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r)
    pt = paint(col, a, stroke=width)
    pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    c.drawRRect(rr, pt)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def etiqueta(c, letra, valor, cx, cy, a, size=34, falta=False):
    """cartão com a letra (C, i, t, J, M) em cima e o valor com unidade embaixo; falta=True → '?' tracejado"""
    if a <= 0:
        return
    col = COR[letra]
    w = max(ftext_w(valor, "black", size) + 60, 150)
    rrect(c, cx - w / 2, cy - 60, w, 130, 18, "#FFFFFF" if not falta else mix("#FFFFFF", col, 0.06), a, shadow=not falta)
    if falta:
        contorno(c, cx - w / 2, cy - 60, w, 130, 18, col, a)
    rrect(c, cx - w / 2, cy - 60, w, 50, 18, col, a * 0.16)
    text_mid(c, letra, cx, cy - 35, 34, "black", col, a)
    fmid(c, valor, cx, cy + 32, size, "black", col if falta else INK, a)


PERNAS = ["J", "C", "i", "t"]


def mesa(c, cx, top, a, falta=None, prog=1.0, w=760, h=300, size=58):
    """a MESA DE QUATRO PERNAS: tampo + pernas J, C, i, t. A perna `falta` aparece tracejada e é reconstruída com prog"""
    if a <= 0:
        return
    rrect(c, cx - w / 2 - 30, top - 46, w + 60, 50, 14, MADEIRA, a, shadow=True)
    rrect(c, cx - w / 2 - 30, top - 10, w + 60, 14, 6, MADEIRA2, a)
    for k, L in enumerate(PERNAS):
        x = cx - w / 2 + 40 + k * (w - 80) / 3
        col = COR[L]
        if L == falta:
            u = clamp(prog)
            contorno(c, x - 30, top + 4, 60, h, 10, col, a * 0.9)
            if u > 0:
                hh = h * ease_io(u)
                rrect(c, x - 30, top + 4 + h - hh, 60, hh, 10, mix("#FFFFFF", col, 0.45), a * u)
            text_mid(c, L if u > 0.6 else "?", x, top + 4 + h / 2, size, "black", col, a)
        else:
            rrect(c, x - 30, top + 4, 60, h, 10, mix("#FFFFFF", col, 0.30), a)
            text_mid(c, L, x, top + 4 + h / 2, size, "black", col, a)


def nota(c, x, y, w, h, a, col=NOTA, col2=NOTA2):
    rrect(c, x, y, w, h, 8, col, a, shadow=True)
    rrect(c, x + 8, y + 8, w - 16, h - 16, 6, col2, a * 0.35)
    c.drawCircle(x + w / 2, y + h / 2, h * 0.28, paint("#FFFFFF", a * 0.6))
    text_mid(c, "R$", x + w / 2, y + h / 2, h * 0.32, "black", col2, a)


def pilha(c, cx, base, a, n=6, w=210, h=58, col=NOTA, col2=NOTA2):
    if a <= 0:
        return
    for k in range(n):
        nota(c, cx - w / 2 + (k % 2) * 6, base - h - k * 20, w, h, a, col, col2)


def pilhas(c, cx, base, a, n_juros=2, cues=None, gap=330):
    """capital + n_juros pilhas iguais. A 1ª é o capital (azul, 'já estava lá'); as outras são juros (verde)."""
    tot = 1 + n_juros
    x0 = cx - (tot - 1) * gap / 2
    for k in range(tot):
        ak = a if cues is None else a * cues[k]
        if ak <= 0:
            continue
        x = x0 + k * gap
        if k == 0:
            pilha(c, x, base, ak, col="#8FB4E8", col2="#4F7FC4")
            text(c, "CAPITAL", x, base + 46, 30, "black", BLUE, ak)
            text(c, "já estava lá", x, base + 84, 24, "bold", GRAY, ak)
        else:
            pilha(c, x, base, ak)
            text(c, f"JUROS {k}", x, base + 46, 30, "black", GREEN, ak)
            text(c, "= 1 capital", x, base + 84, 24, "bold", GRAY, ak)


def linha_tempo(c, x0, x1, y, a, entrada, pagto, mes_pag, risca=0.0, financiado=None, af=0.0):
    """linha do tempo: entrada no dia 0 (riscada como 'não financiada') e o pagamento no mês `mes_pag`"""
    if a <= 0:
        return
    arrow(c, x0, y, x1 + 40, y, INK2, a, 5, 16)
    for m in range(mes_pag + 1):
        x = x0 + (x1 - x0) * m / mes_pag
        line(c, x, y - 14, x, y + 14, INK2, a, 4)
        text(c, "dia 0" if m == 0 else f"mês {m}", x, y + 52, 24, "bold", GRAY, a)
    rrect(c, x0 - 120, y - 150, 240, 100, 18, "#FFFFFF", a, shadow=True)
    text(c, "ENTRADA", x0, y - 118, 22, "black", GRAY, a)
    fmid(c, entrada, x0, y - 78, 34, "black", INK, a)
    if risca > 0:
        strike(c, x0 - 110, y - 80, x0 + 110, y - 110, risca, RED, risca)
        pill(c, "não financiada", x0, y - 180, RED, size=22, a=risca, anchor="center", bounds=(0, 1920))
    rrect(c, x1 - 130, y - 150, 260, 100, 18, "#FFFFFF", a, shadow=True)
    text(c, "PAGAMENTO", x1, y - 118, 22, "black", GRAY, a)
    fmid(c, pagto, x1, y - 78, 34, "black", INK, a)
    if financiado and af > 0:
        pill(c, financiado, (x0 + x1) / 2, y - 100, BLUE, size=26, a=af, anchor="center", bounds=(0, 1920))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "JUROS SIMPLES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 330, 220, 1260, 120, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("2% a.m.", PURPLE), ("  ·  ", GRAY), ("juros simples", INK2), ("  ·  ", GRAY), ("TRIPLICAR?", AMBER)],
              W / 2, 280, 54, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 420, 640, 260, 24, mix("#FFFFFF", RED, 0.06), ab)
        text(c, "“3 capitais em juros”", 580, 480, 32, "black", INK2, ab)
        linha(c, [("12 anos e meio", RED)], 580, 580, 56, ab)
        if t >= C["01.c"]:
            strike(c, 380, 600, 780, 570, ep(t, C["01.c"], 0.4), RED, ep(t, C["01.c"], 0.4))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 420, 640, 260, 24, mix("#FFFFFF", GREEN, 0.10), acc)
        text(c, "a resposta", 1340, 480, 32, "black", INK2, acc)
        linha(c, [("8 anos e 4 meses", GREEN)], 1340, 580, 56, acc)
        selo(c, W / 2, 790, acc, "POR QUÊ?", AMBER, -3, 44)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "descobrir QUALQUER uma das 4 letras", "J · C · i · t"),
            ("02.b", "achar a taxa escondida na compra parcelada", "entrada + pagamento a prazo"),
            ("02.c", "calcular o tempo para dobrar ou triplicar", "o capital se cancela")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "3 LEMBRETES", "DOS EPISÓDIOS 1, 2 E 3", GREEN)
    itens = [("03.a", "EP. 1", [("J = C · i · t", None)], "M = C + J"),
             ("03.b", "EP. 2", [("taxa e tempo", None)], "na MESMA unidade"),
             ("03.c", "EP. 3", [("taxa = degrau ÷ C", None)], "dividido pelo CAPITAL")]
    for k, (cue, ep_, top, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 280 + d, 480, 380, 24, "#FFFFFF", a, shadow=True)
        pill(c, ep_, x + 240, 330 + d, GREEN, size=26, a=a, anchor="center", bounds=(0, 1920))
        if k == 0:
            formula(c, x + 240, 460 + d, 54, a)
            formula(c, x + 240, 560 + d, 44, a, "M = C + J")
        elif k == 1:
            linha(c, [("i", PURPLE), (" a.m.  ·  ", INK), ("t", AMBER), (" em meses", INK)], x + 240, 460 + d, 38, a)
            text(c, sub, x + 240, 570 + d, 32, "black", GRAY, a)
        else:
            linha(c, [("i = degrau ÷ ", INK), ("C", BLUE)], x + 240, 460 + d, 46, a)
            text(c, sub, x + 240, 570 + d, 30, "black", GRAY, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS CENAS", "DA VIDA REAL", BLUE)
    card(c, *CARD_R)
    a1 = ep(t, C["04.a"], 0.5)
    if a1 > 0:
        rrect(c, 220, 230, 700, 430, 24, "#FFFFFF", a1, shadow=True)
        text(c, "GELADEIRA", 570, 285, 32, "black", BLUE, a1)
        linha(c, [("à vista: ", INK2), ("R$ 1.000,00", INK)], 570, 380, 40, a1)
        linha(c, [("ou ", INK2), ("R$ 400,00", INK), (" + ", INK2), ("R$ 660,00", INK)], 570, 470, 40, a1)
        text(c, "(daqui a 2 meses)", 570, 530, 28, "bold", GRAY, a1)
        selo(c, 570, 610, ep(t, C["04.a"] + 4.5, 0.4), "QUANTO DE JUROS?", AMBER, -3, 30)
    a2 = ep(t, C["04.b"], 0.5)
    if a2 > 0:
        rrect(c, 1000, 230, 700, 430, 24, "#FFFFFF", a2, shadow=True)
        text(c, "O SEU DINHEIRO", 1350, 285, 32, "black", BLUE, a2)
        pilha(c, 1230, 560, a2, 4, 170, 50)
        text_mid(c, "→", 1350, 470, 70, "black", GRAY, a2)
        pilha(c, 1480, 560, a2, 8, 170, 50)
        text(c, "dobra em quanto tempo?", 1350, 620, 30, "black", AMBER, a2)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        regra(c, "INCÓGNITA = a letra que falta na fórmula", W / 2, 750, acc, 40, BLUE)


# ======================================================================
# bloco a — a mesa de quatro pernas e as três fórmulas
# ======================================================================

def b_mesa(c, t, C, B):
    head_seq(c, t, C, [("05", "A MESA DE 4 PERNAS", "J = C · i · t", PURPLE),
                       ("06", "AS 3 FÓRMULAS", "A PERNA QUE FALTA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        ab = ep(t, C["05.b"], 0.5)
        prog = ep(t, C["05.b"] + 1.6, 1.4)
        mesa(c, 620, 330, aa, falta="C" if ab > 0 else None, prog=prog)
        if aa > 0:
            formula(c, 620, 250, 50, aa)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, 1120, 300, 580, 340, 24, mix("#FFFFFF", BLUE, 0.07), acc)
            text(c, "ISOLAR", 1410, 360, 40, "black", BLUE, acc)
            para(c, "deixar a letra procurada sozinha de um lado do igual", 1150, 430, 32, "bold", INK2, acc, 520)
            linha(c, [("C", BLUE), (" = ...", INK)], 1410, 590, 56, acc)
        return
    rows = [("06.a", "C", "C = J ÷ (i · t)"), ("06.b", "i", "i = J ÷ (C · t)"), ("06.c", "t", "t = J ÷ (C · i)")]
    for k, (cue, L, f) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 270 + k * 130 + d
        rrect(c, 360, y, 1200, 110, 22, "#FFFFFF", a, shadow=True)
        text(c, "falta", 470, y + 66, 28, "bold", GRAY, a)
        text_mid(c, L, 580, y + 55, 64, "black", COR[L], a)
        formula(c, 1080, y + 55, 58, a, f)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        K.atalho(c, 360, 670, 1200, 130, "ATALHO", ["a perna que falta  =  J  ÷  (produto das outras duas)"], ad, 34)


# ======================================================================
# blocos b, c, d — achar capital, taxa e tempo
# ======================================================================

def b_capital(c, t, C, B):
    head(c, t, B["start"], "ACHAR O CAPITAL", "FALTA A PERNA C", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["07.t"], 0.4)
    aa = ep(t, C["07.a"], 0.5)
    etiqueta(c, "J", "R$ 360,00", 460, 320, a0)
    etiqueta(c, "i", "1,5% a.m. = 0,015", 860, 320, a0)
    etiqueta(c, "t", "8 meses", 1260, 320, a0)
    etiqueta(c, "C", "?", 1600, 320, aa, falta=True)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("i · t = 0,015 · 8 = ", INK), ("0,12", PURPLE)], W / 2, 500, 50, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        linha(c, [("C = 360 ÷ 0,12 = ", INK), ("R$ 3.000,00", BLUE)], W / 2, 610, 60, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        linha(c, [("confere: 45 por mês × 8 = 360", INK2)], W / 2, 730, 34, ad)
        conferido(c, "bateu", 1420, 745, ep(t, C["07.d"] + 2.0, 0.4), True, 30)


def b_taxa(c, t, C, B):
    head_seq(c, t, C, [("08", "ACHAR A TAXA", "FALTA A PERNA i", BLUE), ("09", "A ARMADILHA DA TAXA", "CAPITAL × MONTANTE", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["08.t"], 0.4)
    etiqueta(c, "J", "R$ 240,00", 460, 310, a0)
    etiqueta(c, "C", "R$ 1.000,00", 860, 310, a0)
    etiqueta(c, "t", "6 meses", 1260, 310, a0)
    etiqueta(c, "i", "?", 1600, 310, a0, falta=True)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            linha(c, [("C · t = 1.000 · 6 = 6.000", INK2)], W / 2, 470, 40, ab)
            linha(c, [("i = 240 ÷ 6.000 = 0,04 = ", INK), ("4% a.m.", PURPLE)], W / 2, 560, 56,
                  ep(t, C["08.b"] + 2.5, 0.4))
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            K.atalho(c, 360, 650, 1200, 150, "ATALHO · OS JUROS DE UM MÊS SÓ",
                     ["240 ÷ 6 meses = R$ 40,00 por mês  →  40 de 1.000 = 4%"], acc, 32)
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 440, 700, 300, 24, mix("#FFFFFF", RED, 0.06), aa)
        text(c, "pelo MONTANTE", 570, 500, 32, "black", RED, aa)
        linha(c, [("240 ÷ (1.240 · 6)", INK)], 570, 580, 40, aa)
        linha(c, [("≈ 3,2%", RED)], 570, 660, 50, aa)
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            selo(c, 570, 760, ab, "MENOR QUE A REAL", AMBER, -3, 30)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 440, 700, 300, 24, mix("#FFFFFF", GREEN, 0.10), acc)
        text(c, "pelo CAPITAL", 1350, 500, 32, "black", GREEN, acc)
        linha(c, [("240 ÷ (1.000 · 6)", INK)], 1350, 580, 40, acc)
        linha(c, [("= 4%", GREEN)], 1350, 660, 50, acc)
        conferido(c, "sempre o dinheiro do começo", 1060, 790, acc, True, 28)


def b_tempo(c, t, C, B):
    head(c, t, B["start"], "ACHAR O TEMPO", "FALTA A PERNA t", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["10.t"], 0.4)
    etiqueta(c, "J", "R$ 400,00", 460, 310, a0)
    etiqueta(c, "C", "R$ 2.000,00", 860, 310, a0)
    etiqueta(c, "i", "2,5% a.m. = 0,025", 1270, 310, a0)
    etiqueta(c, "t", "?", 1620, 310, a0, falta=True)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("C · i = 2.000 · 0,025 = ", INK), ("R$ 50,00 por mês", GREEN)], W / 2, 480, 46, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        linha(c, [("t = 400 ÷ 50 = ", INK), ("8 meses", AMBER)], W / 2, 580, 60, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        for k in range(8):
            u = ep(t, C["10.d"] + 0.2 * k, 0.3)
            x = W / 2 - 3.5 * 120 + k * 120
            if u > 0:
                c.drawCircle(x, 720, 46, paint("#F2B632", u))
                c.drawCircle(x, 720, 36, paint("#C98E12", u, stroke=3))
                text_mid(c, "50", x, 720, 30, "black", INK, u)
        text(c, "8 moedinhas de 50 cabem em 400", W / 2, 810, 28, "black", GREEN, ad)


# ======================================================================
# bloco e — dobrar e triplicar
# ======================================================================

def b_dobrar(c, t, C, B):
    head_seq(c, t, C, [("11", "DOBRAR E TRIPLICAR", "O MONTANTE JÁ TEM O CAPITAL", BLUE),
                       ("12", "O CAPITAL SE CANCELA", "i · t = k − 1", PURPLE),
                       ("13", "MESES EM ANOS", "DIVISÃO INTEIRA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            linha(c, [("DOBRAR: ", BLUE), ("M = 2C", INK), ("      TRIPLICAR: ", BLUE), ("M = 3C", INK)], W / 2, 260, 40, aa)
        ab = ep(t, C["11.b"], 0.5)
        acc = ep(t, C["11.c"], 0.5)
        pilhas(c, W / 2, 620, 1.0, 2, [ab, acc, ep(t, C["11.c"] + 0.4, 0.4)])
        if acc > 0:
            regra(c, "triplicar = ganhar DUAS vezes o capital em juros", W / 2, 780, ep(t, C["11.c"] + 2.0, 0.4), 36)
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            linha(c, [("dobrar: ", GRAY), ("J = C", GREEN), ("      triplicar: ", GRAY), ("J = 2C", GREEN)], W / 2, 270, 44, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("C", BLUE), (" · i · t = 2", INK), ("C", BLUE)], W / 2, 380, 64, ab)
            u = ep(t, C["12.b"] + 1.6, 0.5)
            if u > 0:
                x0 = W / 2 - text_w("C · i · t = 2C", "black", 64) / 2
                strike(c, x0 - 6, 400, x0 + text_w("C", "black", 64) + 6, 360, u, RED, u)
                x1 = x0 + text_w("C · i · t = 2", "black", 64)
                strike(c, x1 - 6, 400, x1 + text_w("C", "black", 64) + 6, 360, u, RED, u)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            rrect(c, 560, 450, 800, 120, 26, mix("#FFFFFF", PURPLE, 0.10), acc)
            linha(c, [("i · t = ", PURPLE), ("k − 1", INK)], W / 2, 510, 64, acc)
            text(c, "k = quantas vezes o capital", W / 2, 610, 26, "bold", GRAY, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            linha(c, [("4% a.m.:  dobrar  0,04 · t = 1 → ", INK), ("25 meses", AMBER)], W / 2, 690, 40, ad)
            linha(c, [("triplicar  0,04 · t = 2 → ", INK), ("50 meses", AMBER)], W / 2, 770, 40,
                  ep(t, C["12.d"] + 4.0, 0.4))
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        linha(c, [("50 meses ÷ 12", INK)], W / 2, 290, 56, aa)
        linha(c, [("4 · 12 = 48", INK2), ("   →   sobram ", GRAY), ("2", AMBER)], W / 2, 400, 48, ep(t, C["13.a"] + 1.4, 0.4))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("4 anos e 2 meses", GREEN)], W / 2, 520, 70, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 610, 1200, 200, "ATALHO",
                 ["tempo para multiplicar por k  =  (k − 1) ÷ i", "anos = divisão inteira por 12 · o resto são os meses"],
                 acc, 30)


# ======================================================================
# bloco f — a taxa embutida
# ======================================================================

def b_embutida(c, t, C, B):
    head_seq(c, t, C, [("14", "A COMPRA PARCELADA", "A ENTRADA NÃO É EMPRÉSTIMO", BLUE),
                       ("15", "A TAXA EMBUTIDA", "UMA TV EM 3 MESES", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        defs = [("14.a", "ENTRADA", "o que você paga no ato"),
                ("14.b", "VALOR FINANCIADO", "preço à vista − entrada"),
                ("14.c", "TAXA EMBUTIDA", "os juros escondidos no preço a prazo")]
        for k, (cue, nome, sig) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 260 + k * 140 + d
            rrect(c, 300, y, 1320, 115, 22, mix("#FFFFFF", BLUE, 0.06), a)
            text(c, nome, 340, y + 70, 38, "black", BLUE, a, align="left")
            text(c, sig, 1580, y + 70, 34, "bold", INK2, a, align="right")
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            regra(c, "a loja só financia o que FALTA pagar", W / 2, 750, ad, 40)
        return
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        linha(c, [("TV: ", INK2), ("R$ 2.000,00", INK), (" à vista", INK2)], W / 2, 250, 38, aa)
    linha_tempo(c, 460, 1460, 520, aa, "R$ 500,00", "R$ 1.590,00", 3, risca=ep(t, C["15.b"], 0.4),
                financiado="financiado: 2.000 − 500 = R$ 1.500,00", af=ep(t, C["15.b"] + 0.6, 0.4))
    ab = ep(t, C["15.b"] + 3.0, 0.4)
    if ab > 0:
        linha(c, [("J = 1.590 − 1.500 = ", INK), ("R$ 90,00", GREEN)], W / 2, 660, 40, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        linha(c, [("i = 90 ÷ (1.500 · 3) = 90 ÷ 4.500 = ", INK), ("2% a.m.", PURPLE)], W / 2, 760, 42, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "TAXA E DOBRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 230, 700, 260, 24, "#FFFFFF", aa, shadow=True)
        text(c, "1 · A TAXA MENSAL", 570, 280, 28, "black", PURPLE, aa)
        linha(c, [("C ", BLUE), ("R$ 1.500,00", INK)], 570, 350, 34, aa)
        linha(c, [("J ", GREEN), ("R$ 180,00", INK), ("   t ", AMBER), ("4 meses", INK)], 570, 420, 34, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 230, 700, 260, 24, "#FFFFFF", ab, shadow=True)
        text(c, "2 · DOBRAR", 1350, 280, 28, "black", PURPLE, ab)
        linha(c, [("i ", PURPLE), ("5% a.m.", INK)], 1350, 350, 34, ab)
        linha(c, [("t ", AMBER), ("= ?", INK)], 1350, 420, 34, ab)
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 640)
    if t < C["17"]:
        return
    linha(c, [("C · t = 6.000  →  i = 180 ÷ 6.000 = ", INK), ("3% a.m.", PURPLE)], 570, 580, 30, ep(t, C["17.a"], 0.4))
    linha(c, [("J = C  →  0,05 · t = 1", INK)], 1350, 580, 34, ep(t, C["17.b"], 0.4))
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("20 meses", AMBER), (" = 1 ano e 8 meses", INK2)], 1350, 670, 40, acc)
        conferido(c, "3% a.m.", 470, 680, ep(t, C["17.a"] + 4, 0.4), True, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Dadas três letras, a quarta sai dividindo os juros pelas outras duas.",
          "Triplicar é ganhar duas vezes o capital em juros.",
          "A entrada não é empréstimo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Achar a taxa dividindo pelo MONTANTE", "o montante é o número que salta do enunciado",
          "a taxa é sobre o CAPITAL · pelo montante ela sai menor"),
         ("Triplicar com J = 3C", "a palavra é “triplicar”",
          "o capital já está no montante: J = 2C (com 3C, o tempo sai 50% maior)"),
         ("100 meses = 8,33 anos = “8 anos e 3 meses”", "o 3 está ali, depois da vírgula",
          "0,33 ano × 12 = 4 meses · 8 · 12 = 96, sobram 4: 8 anos e 4 meses"),
         ("Incluir a ENTRADA no valor financiado", "a entrada também faz parte do preço",
          "ela é paga no ato: capital = preço à vista − entrada")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21", "22"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


def _questao(c, t, C, sid_q, texto, alts, okL, ok_cue, xs, sid_x, fonte=True):
    a0 = ep(t, C[f"{sid_q}.a"], 0.4)
    yend = _enunciado(c, texto, a0)
    if fonte:
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
             a0 * (1 - ep(t, C[f"{int(sid_q) + 1:02d}"], 0.3)), align="left")
    cues_in = {L: C[f"{sid_q}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in xs}
    K.alternativas(c, t, C, alts, 1000, 250, 680, 42, ok_cue, okL, cues_in, cues_x, gap=34)
    return yend


ALTS3 = [("A", "2%", "÷ montante (ao mês)", RED), ("B", "2,5%", "é a taxa MENSAL", RED), ("C", "24%", "÷ montante (ao ano)", RED),
         ("D", "25%", "não dividiu pelo tempo", RED), ("E", "30%", "", GREEN)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "DESCOBRIR A TAXA", BLUE)
    card(c, *CARD_R)
    yend = _questao(c, t, C, "23", "Um capital de R$ 1.200,00, aplicado a juros simples, gerou um montante de R$ 1.500,00 "
                    "após 10 meses. A taxa anual de juros dessa aplicação foi de", ALTS3, "E", C["24.ok"], "ABCD", "25")
    if t >= C["24"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["24"], 0.4))
        aa = ep(t, C["24.a"], 0.4)
        if aa > 0:
            for k, (L, v) in enumerate((("C", "1.200"), ("M", "1.500"), ("t", "10 meses"))):
                x = 250 + k * 225
                rrect(c, x - 10, y0 + 22, 210, 56, 14, mix("#FFFFFF", COR[L], 0.14), aa)
                linha(c, [(L + " ", COR[L]), (v, INK)], x + 95, y0 + 50, 26, aa)
        linha(c, [("J = 1.500 − 1.200 = ", INK), ("300", GREEN)], 540, y0 + 120, 30, ep(t, C["24.b"], 0.4))
        linha(c, [("i = 300 ÷ 12.000 = ", INK), ("2,5% a.m.", PURPLE)], 540, y0 + 180, 30, ep(t, C["24.c"], 0.4))
        linha(c, [("anual: 2,5% × 12 = ", INK), ("30% a.a.", GREEN)], 540, y0 + 240, 30, ep(t, C["24.d"], 0.4))
        pill(c, "pede a ANUAL", 540, y0 + 300, AMBER, size=22, a=ep(t, C["24.d"], 0.4), anchor="center")


ALTS8 = [("A", "5%", "", GREEN), ("B", "6%", "preço total E sem ÷ 2", RED), ("C", "7,5%", "sobre a entrada (÷ 2)", RED),
         ("D", "10%", "não dividiu pelos 2 meses", RED), ("E", "15%", "sobre a entrada (sem ÷ 2)", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · NÓS FAZEMOS", "A TAXA EMBUTIDA", GREEN)
    card(c, *CARD_R)
    if t < C["27"] or t >= C["28"]:
        _questao(c, t, C, "26", "Uma loja vende uma geladeira por R$ 1.000,00 à vista ou, a prazo, com entrada de R$ 400,00 "
                 "e um pagamento de R$ 660,00 dois meses após a compra. Considerando juros simples, a taxa mensal cobrada "
                 "na compra a prazo é de", ALTS8, "A", C["27.ok"], "BCDE", "28")
        if t < C["27"]:
            pause_timer(c, t, C["26.end"] - 1.9, 540, 760)
        return
    # 27: a linha do tempo ocupa a tela
    aa = ep(t, C["27.a"], 0.5)
    linha_tempo(c, 460, 1460, 470, aa, "R$ 400,00", "R$ 660,00", 2,
                risca=ep(t, C["27.a"] + 2.0, 0.4), financiado="C = 1.000 − 400 = R$ 600,00", af=ep(t, C["27.b"], 0.4))
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        linha(c, [("J = 660 − 600 = ", INK), ("R$ 60,00", GREEN)], W / 2, 620, 44, acc)
    ad = ep(t, C["27.d"], 0.5)
    if ad > 0:
        linha(c, [("i = 60 ÷ (600 · 2) = 60 ÷ 1.200 = ", INK), ("5% a.m.", PURPLE)], W / 2, 710, 44, ad)
    aok = ep(t, C["27.ok"], 0.4)
    if aok > 0:
        selo(c, W / 2, 800, aok, "LETRA A", GREEN, -3, 40)


ALTS4 = [("A", "4 anos e 2 meses", "é o tempo de DOBRAR", RED), ("B", "8 anos e 3 meses", "leu 8,33 errado", RED),
         ("C", "8 anos e 4 meses", "", GREEN), ("D", "12 anos e 6 meses", "fez J = 3C", RED),
         ("E", "100 anos", "taxa mensal como anual", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · VOCÊ FAZ", "TRIPLICAR A 2% A.M.", GREEN)
    card(c, *CARD_R)
    yend = _questao(c, t, C, "29", "Um investidor deseja triplicar seu capital em uma aplicação que paga juros simples de 2% "
                    "ao mês. O tempo mínimo necessário é de", ALTS4, "C", C["30.ok"], "ABDE", "31")
    if t < C["30"]:
        pause_timer(c, t, C["29.end"] - 1.9, 540, 680)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["30"], 0.4))
    linha(c, [("triplicar: ", GRAY), ("J = 2C", GREEN)], 540, y0 + 50, 32, ep(t, C["30.a"], 0.4))
    linha(c, [("0,02 · t = 2  →  ", INK), ("t = 100 meses", AMBER)], 540, y0 + 120, 32, ep(t, C["30.b"], 0.4))
    linha(c, [("8 · 12 = 96, sobram 4", INK2)], 540, y0 + 190, 30, ep(t, C["30.c"], 0.4))
    linha(c, [("8 anos e 4 meses", GREEN)], 540, y0 + 260, 38, ep(t, C["30.c"] + 2.0, 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DE JUROS SIMPLES", PURPLE)
    itens = [("33.a", "juntamos tudo", "J · C · i · t · M"), ("33.b", "caçamos as pegadinhas", "montante · vírgula · entrada"),
             ("33.c", "treinamos no formato do ENEM", "questões inéditas")]
    for k, (cue, s, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 300 + d, 480, 300, 24, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, x + 240, 370 + d, a, 34, bg=PURPLE)
        text(c, s, x + 240, 480 + d, 34 if len(s) < 24 else 28, "black", INK, a)
        text(c, sub, x + 240, 540 + d, 26, "bold", GRAY, a)
    pill(c, "ep. 5 · revisão", W / 2, 760, PURPLE, size=30, a=ep(t, C["33.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"],
        "Em quanto tempo seu dinheiro dobraria a 1% ao mês?", canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, mesa=b_mesa, capital=b_capital,
              taxa=b_taxa, tempo=b_tempo, dobrar=b_dobrar, embutida=b_embutida, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q3=b_q3, q8=b_q8, q4=b_q4, ponte=b_ponte, cta=b_cta)
