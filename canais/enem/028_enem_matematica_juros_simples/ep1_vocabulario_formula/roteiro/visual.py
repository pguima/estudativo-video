"""Visual — Juros Simples, Episódio 1: o vocabulário do dinheiro e a fórmula J = C · i · t (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: pilha() (a pilha de notas do capital, parada) e moedas() (uma moedinha IGUAL caindo a cada mês),
etiqueta() (C, i, t, J ou M com a unidade), linha().
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
ARQUIVO_FINAL = "enem_matematica_juros_simples_ep1_vocabulario_formula.mp4"
CARD_R = K.CARD_R
NOTA = "#7FBF8E"
NOTA2 = "#5FA371"
MOEDA = "#F2B632"
MOEDA2 = "#C98E12"

# cor de cada letra da fórmula
COR = dict(C=BLUE, i=PURPLE, t=AMBER, J=GREEN, M=RED)


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
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def nota(c, x, y, w, h, a):
    rrect(c, x, y, w, h, 8, NOTA, a, shadow=True)
    rrect(c, x + 8, y + 8, w - 16, h - 16, 6, NOTA2, a * 0.35)
    c.drawCircle(x + w / 2, y + h / 2, h * 0.28, paint("#FFFFFF", a * 0.6))
    text_mid(c, "R$", x + w / 2, y + h / 2, h * 0.32, "black", NOTA2, a)


def pilha(c, cx, base, a, rot="R$ 1.500,00", n=7, w=230, h=64):
    """a pilha de notas do capital (fica PARADA)"""
    if a <= 0:
        return
    for k in range(n):
        nota(c, cx - w / 2 + (k % 2) * 6, base - h - k * 22, w, h, a)
    if rot:
        text(c, rot, cx, base + 50, 34, "black", BLUE, a)
        text(c, "capital", cx, base + 88, 26, "bold", GRAY, a)


def moeda(c, cx, cy, r, a, s="30"):
    if a <= 0:
        return
    c.drawCircle(cx, cy + 4, r, paint(MOEDA2, a))
    c.drawCircle(cx, cy, r, paint(MOEDA, a))
    c.drawCircle(cx, cy, r * 0.78, paint(MOEDA2, a, stroke=3))
    text_mid(c, s, cx, cy, r * 0.72, "black", INK, a)


def moedas(c, x0, base, quedas, a, s="30", r=52, gap=128, rot_mes=True):
    """uma moedinha IGUAL por mês: quedas = lista de progresso (0 → 1) de cada moeda caindo"""
    for k, u in enumerate(quedas):
        if u <= 0:
            continue
        cx = x0 + k * gap
        cy = lerp(base - 420, base - r, ease_io(clamp(u)))
        moeda(c, cx, cy, r, a * clamp(u * 3), s)
        if rot_mes:
            text(c, f"mês {k + 1}", cx, base + 44, 24, "bold", GRAY, a * clamp(u * 3))


def etiqueta(c, letra, valor, cx, cy, a, size=36):
    """cartão com a letra (C, i, t, J, M) em cima e o valor com unidade embaixo"""
    if a <= 0:
        return
    col = COR[letra]
    w = max(ftext_w(valor, "black", size) + 60, 150)
    rrect(c, cx - w / 2, cy - 60, w, 130, 18, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - 60, w, 50, 18, col, a * 0.16)
    text_mid(c, letra, cx, cy - 35, 34, "black", col, a)
    fmid(c, valor, cx, cy + 32, size, "black", INK, a)


def formula(c, cx, cy, size, a, s="J = C · i · t", alfas=None):
    """fórmula com cada letra na sua cor"""
    if a <= 0:
        return
    partes = []
    for ch in s:
        partes.append((ch, COR.get(ch, INK)))
    linha(c, partes, cx, cy, size, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "JUROS SIMPLES", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 220, 1460, 120, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("R$ 2.400,00", BLUE), ("  ·  ", GRAY), ("1,5% a.m.", PURPLE), ("  ·  ", GRAY), ("8 meses", AMBER)],
              W / 2, 280, 58, aa)
    resp = ["R$ 28,80", "R$ 36,00", "R$ 288,00", "R$ 2.688,00", "R$ 2.880,00"]
    for k, s in enumerate(resp):
        a = ep(t, C[f"01.r{k + 1}"], 0.4)
        if a > 0:
            x = 330 + k * 315
            rrect(c, x - 140, 420, 280, 110, 20, "#FFFFFF", a, shadow=True)
            text_mid(c, "ABCDE"[k], x, 395, 30, "black", GRAY, a)
            fmid(c, s, x, 475, 38, "black", INK, a)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        for k in (0, 1, 3, 4):
            x = 330 + k * 315
            strike(c, x - 120, 500, x + 120, 450, acc, RED, ep(t, C["01.c"] + 0.3 * k, 0.4))
        selo(c, W / 2, 680, acc, "4 DELAS: CONTA CERTA, JEITO ERRADO", AMBER, -3, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "distinguir JUROS de MONTANTE", "o acréscimo × o total"),
            ("02.b", "calcular os dois sem errar a vírgula da taxa", "2% → 0,02 · 1,5% → 0,015")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "DA SÉRIE DE PORCENTAGEM", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "% = DIVIDIDO POR 100", 560, 290, 38, "black", BLUE, aa)
        linha(c, [("2% = ", INK), ("0,02", GREEN)], 560, 420, 64, aa)
        linha(c, [("1,5% = ", INK), ("0,015", GREEN)], 560, 540, 64, ep(t, C["03.a"] + 2.5, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "O FATOR DE AUMENTO", 1370, 290, 38, "black", PURPLE, ab)
        linha(c, [("+12%", AMBER), ("  →  ", GRAY), ("× 1,12", PURPLE)], 1370, 420, 64, ab)
        linha(c, [("1", BLUE), (" + ", INK), ("0,12", AMBER)], 1370, 540, 56, ep(t, C["03.b"] + 1.8, 0.4))
        text(c, "o que tinha + o acréscimo", 1370, 610, 26, "bold", GRAY, ep(t, C["03.b"] + 1.8, 0.4))
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


def bicicleta(c, cx, cy, s, a, col=BLUE):
    if a <= 0:
        return
    st = paint(col, a, stroke=s * 0.06)
    c.drawCircle(cx - s * 0.55, cy, s * 0.35, st)
    c.drawCircle(cx + s * 0.55, cy, s * 0.35, st)
    p = skia.Path(); p.moveTo(cx - s * 0.55, cy); p.lineTo(cx - s * 0.1, cy - s * 0.45); p.lineTo(cx + s * 0.35, cy - s * 0.45)
    p.lineTo(cx + s * 0.55, cy); p.moveTo(cx - s * 0.1, cy - s * 0.45); p.lineTo(cx + 0.05 * s, cy)
    p.lineTo(cx - s * 0.55, cy); p.moveTo(cx + 0.05 * s, cy); p.lineTo(cx + s * 0.35, cy - s * 0.45)
    c.drawPath(p, st)
    line(c, cx - s * 0.2, cy - s * 0.6, cx, cy - s * 0.6, INK, a, s * 0.07)
    line(c, cx + s * 0.35, cy - s * 0.45, cx + s * 0.42, cy - s * 0.7, col, a, s * 0.06)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS SITUAÇÕES", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    a1 = ep(t, C["04.a"], 0.5)
    if a1 > 0:
        rrect(c, 220, 230, 700, 420, 24, "#FFFFFF", a1, shadow=True)
        text(c, "EMPRÉSTIMO DO TIO", 570, 280, 30, "black", BLUE, a1)
        pilha(c, 440, 560, a1, None, 5, 200, 56)
        linha(c, [("R$ 1.500,00", BLUE)], 720, 420, 40, a1)
        linha(c, [("+ 2% por mês", AMBER)], 720, 490, 36, a1)
    a2 = ep(t, C["04.b"], 0.5)
    if a2 > 0:
        rrect(c, 1000, 230, 700, 420, 24, "#FFFFFF", a2, shadow=True)
        text(c, "ALUGUEL DE BICICLETA", 1350, 280, 30, "black", BLUE, a2)
        bicicleta(c, 1200, 470, 150, a2)
        linha(c, [("R$ 20,00 por dia", AMBER)], 1520, 420, 34, a2)
        linha(c, [("3 dias = R$ 60,00", INK)], 1520, 490, 34, ep(t, C["04.b"] + 2.2, 0.4))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        regra(c, "JUROS = o ALUGUEL do dinheiro", W / 2, 730, acc, 42, BLUE)
        text(c, "quem usa o dinheiro de outra pessoa paga por cada mês de uso", W / 2, 810, 28, "bold", GRAY, acc)


# ======================================================================
# blocos a, b, c — as cinco palavras, juros × montante, siglas
# ======================================================================

PALAVRAS = [("05.a", "C", "CAPITAL", "o valor do começo", "R$ 1.500,00"),
            ("05.b", "i", "TAXA", "% por período", "2% a.m."),
            ("05.c", "t", "TEMPO", "quantos períodos", "6 meses"),
            ("06.a", "J", "JUROS", "o acréscimo", "R$ 180,00"),
            ("06.b", "M", "MONTANTE", "o total no fim", "R$ 1.680,00")]


def b_palavras(c, t, C, B):
    head(c, t, B["start"], "AS 5 PALAVRAS", "QUE APARECEM EM TODA QUESTÃO", BLUE)
    card(c, *CARD_R)
    for k, (cue, L, nome, def_, ex_) in enumerate(PALAVRAS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 180 + k * 318
        col = COR[L]
        rrect(c, x, 250 + d, 290, 470, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250 + d, 290, 70, 24, col, a * 0.16)
        text(c, nome, x + 145, 298 + d, 30, "black", col, a)
        text_mid(c, L, x + 145, 420 + d, 110, "black", col, a)
        text(c, def_, x + 145, 540 + d, 26, "bold", INK2, a)
        fmid(c, ex_, x + 145, 640 + d, 34, "black", INK, a)
    if t >= C["06"]:
        a2 = ep(t, C["06.b"] + 2.0, 0.4)
        pill(c, "M = C + J", W / 2, 790, PURPLE, size=32, a=a2, anchor="center")


def b_jm(c, t, C, B):
    head(c, t, B["start"], "JUROS NÃO É MONTANTE", "QUAL A PERGUNTA PEDE?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 250, 700, 380, 24, mix("#FFFFFF", GREEN, 0.08), aa)
        text(c, "“quanto RENDEU?”", 570, 330, 44, "black", INK, aa)
        text(c, "“qual o valor dos juros?”", 570, 400, 34, "bold", INK2, aa)
        text_mid(c, "J", 570, 520, 120, "black", GREEN, aa)
        text(c, "só o acréscimo", 570, 610, 28, "bold", GRAY, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 250, 700, 380, 24, mix("#FFFFFF", RED, 0.06), ab)
        text(c, "“quanto TERÁ?”", 1350, 330, 44, "black", INK, ab)
        text(c, "“quanto pagará no total?”", 1350, 400, 34, "bold", INK2, ab)
        text_mid(c, "M", 1350, 520, 120, "black", RED, ab)
        text(c, "o total", 1350, 610, 28, "bold", GRAY, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 730, acc, "O ENEM COLOCA AS DUAS NAS ALTERNATIVAS", AMBER, -2, 34)


SIGLAS = [("07", "a.d.", "ao dia"), ("07", "a.m.", "ao mês"), ("07", "a.b.", "ao bimestre"),
          ("08", "a.t.", "ao trimestre"), ("08", "a.s.", "ao semestre"), ("08", "a.a.", "ao ano")]


def b_siglas(c, t, C, B):
    head(c, t, B["start"], "AS SIGLAS DA TAXA", "O PERÍODO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text(c, "PERÍODO = o pedaço de tempo em que a taxa é cobrada uma vez", W / 2, 270, 32, "black", BLUE, aa)
    for k, (_, sg, sig) in enumerate(SIGLAS):
        cue = C["08.b"] + k * 1.0 if k < 3 else C["08.c"] + (k - 3) * 1.0
        a = ep(t, cue, 0.4)
        if a <= 0:
            continue
        x = 250 + (k % 3) * 470
        y = 360 + (k // 3) * 170
        rrect(c, x, y, 420, 130, 22, "#FFFFFF", a, shadow=True)
        text_mid(c, sg, x + 120, y + 65, 52, "black", PURPLE, a)
        text_mid(c, sig, x + 300, y + 65, 32, "bold", INK2, a)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        regra(c, "a taxa nunca anda sozinha:  2% a.m.", W / 2, 750, ad, 38)


# ======================================================================
# bloco d — juros simples: a pilha parada e as moedinhas iguais
# ======================================================================

def b_simples(c, t, C, B):
    head(c, t, B["start"], "JUROS SIMPLES", "O ALUGUEL É SEMPRE O MESMO", BLUE)
    card(c, *CARD_R)
    base = 640
    aa = ep(t, C["09.a"], 0.5)
    pilha(c, 400, base, aa)
    if aa > 0:
        text(c, "2% de R$ 1.500,00 = R$ 30,00 por mês", 1150, 270, 30, "black", INK2, ep(t, C["09.b"], 0.4))
    q = [ep(t, C["09.b"] + 0.3, 1.0), ep(t, C["09.c"] + 0.2, 1.0), ep(t, C["09.c"] + 2.4, 1.0),
         ep(t, C["09.d"] - 0.4, 0.8), ep(t, C["09.d"] + 0.4, 0.8), ep(t, C["09.d"] + 1.2, 0.8)]
    moedas(c, 720, base, q, 1.0)
    ad = ep(t, C["09.d"] + 1.6, 0.5)
    if ad > 0:
        pill(c, "as moedinhas NUNCA crescem: sempre sobre o capital inicial", W / 2, 780, BLUE, size=28, a=ad,
             anchor="center")
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        rrect(c, 1340, 300, 400, 150, 20, mix("#FFFFFF", AMBER, 0.12), ae)
        text(c, "juros rendendo juros?", 1540, 350, 26, "black", AMBER, ae)
        text(c, "isso é juros COMPOSTOS", 1540, 395, 24, "bold", INK2, ae)
        text(c, "(série própria)", 1540, 430, 22, "bold", GRAY, ae)


# ======================================================================
# bloco e — a fórmula
# ======================================================================

def b_formula(c, t, C, B):
    head_seq(c, t, C, [("10", "A FÓRMULA", "J = C · i · t", PURPLE), ("11", "O MONTANTE", "M = C · (1 + i · t)", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            text(c, "cada mês gera:", 560, 290, 34, "bold", GRAY, aa)
            formula(c, 560, 380, 80, aa, "C · i")
            moeda(c, 560, 520, 60, aa, "C·i")
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            text(c, "t meses:", 1350, 290, 34, "bold", GRAY, ab)
            for k in range(6):
                moeda(c, 1110 + k * 96, 400, 42, ep(t, C["10.b"] + 0.25 * k, 0.3), "C·i")
            linha(c, [("t", AMBER), (" × ", INK), ("C · i", PURPLE)], 1350, 520, 60, ep(t, C["10.b"] + 1.8, 0.4))
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            rrect(c, 560, 640, 800, 140, 28, mix("#FFFFFF", PURPLE, 0.10), acc)
            formula(c, W / 2, 710, 90, acc)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        formula(c, W / 2, 300, 80, aa, "M = C + J")
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 460, 400, 1000, 150, 28, mix("#FFFFFF", PURPLE, 0.10), ab)
        formula(c, W / 2, 475, 84, ab, "M = C · (1 + i · t)")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        x0 = W / 2 - text_w("M = C · (1 + i · t)", "black", 84) / 2
        x1 = x0 + text_w("M = C · (", "black", 84)
        x2 = x1 + text_w("1", "black", 84)
        x3 = x2 + text_w(" + ", "black", 84)
        x4 = x3 + text_w("i · t", "black", 84)
        line(c, x1, 560, x2, 560, BLUE, acc, 6)
        text(c, "o capital", (x1 + x2) / 2, 610, 28, "black", BLUE, acc)
        line(c, x3, 560, x4, 560, AMBER, acc, 6)
        text(c, "o acréscimo", (x3 + x4) / 2, 610, 28, "black", AMBER, acc)
        pill(c, "é o FATOR da Porcentagem", W / 2, 740, PURPLE, size=32, a=ep(t, C["11.c"] + 2.0, 0.4), anchor="center")


# ======================================================================
# bloco f — a taxa na forma decimal
# ======================================================================

def b_decimal(c, t, C, B):
    head(c, t, B["start"], "A TAXA NA FÓRMULA", "SEMPRE NA FORMA DECIMAL", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        text(c, "FORMA DECIMAL = a porcentagem dividida por 100", W / 2, 280, 34, "black", BLUE, aa)
    rows = [("2%", "0,02"), ("1,5%", "0,015"), ("18%", "0,18")]
    for k, (p_, d_) in enumerate(rows):
        a = ep(t, C["12.b"] + k * 2.6, 0.5)
        if a <= 0:
            continue
        y = 390 + k * 110
        fmid(c, p_, 640, y, 64, "black", INK, a)
        arrow(c, 800, y, 1000, y, GRAY, a, 5, 16)
        fmid(c, d_, 1200, y, 64, "black", GREEN, ep(t, C["12.b"] + k * 2.6 + 0.8, 0.4))
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 700, 1200, 120, "ATALHO",
                 ["tire o %  e ande com a vírgula 2 casas para a esquerda (faltou algarismo? zero)"], acc, 30)


# ======================================================================
# bloco g — o exemplo completo e o fator
# ======================================================================

def b_exemplo(c, t, C, B):
    head_seq(c, t, C, [("13", "O EMPRÉSTIMO DO TIO", "J E M", PURPLE), ("14", "PELO FATOR", "UM AUMENTO ÚNICO", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    etiqueta(c, "C", "R$ 1.500,00", 560, 320, aa)
    etiqueta(c, "i", "2% a.m. = 0,02", 960, 320, ep(t, C["13.a"] + 1.4, 0.4))
    etiqueta(c, "t", "6 meses", 1360, 320, ep(t, C["13.a"] + 3.4, 0.4))
    sid = which(t, C, ["13", "14"])
    if sid == "13":
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            linha(c, [("J = 1.500 · 0,02 · 6 = ", INK), ("R$ 180,00", GREEN)], W / 2, 520, 56, ab)
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            linha(c, [("M = 1.500 + 180 = ", INK), ("R$ 1.680,00", RED)], W / 2, 640, 56, acc)
        return
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("1 + 0,02 · 6 = ", INK), ("1,12", PURPLE)], W / 2, 500, 56, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("1.500 · 1,12 = ", INK), ("R$ 1.680,00", RED)], W / 2, 610, 56, ab)
        conferido(c, "o mesmo valor", 1460, 625, ep(t, C["14.b"] + 2.0, 0.4), True, 28)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        regra(c, "6 meses a 2%  =  um aumento único de 12%", W / 2, 750, acc, 38)


# ======================================================================
# bloco h — a conta de um mês só
# ======================================================================

def b_cabeca(c, t, C, B):
    head(c, t, B["start"], "SEM CALCULADORA", "A CONTA DE UM MÊS SÓ", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        moeda(c, 420, 420, 90, aa, "?")
        text(c, "1 mês", 420, 560, 30, "black", GRAY, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("1% de 1.500 = ", INK), ("15", INK2)], 1100, 330, 50, ab)
        linha(c, [("2% de 1.500 = ", INK), ("R$ 30,00", GREEN)], 1100, 420, 56, ep(t, C["15.b"] + 2.4, 0.4))
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        linha(c, [("30 × 6 meses = ", INK), ("R$ 180,00", GREEN)], 1100, 530, 56, acc)
        K.atalho(c, 360, 660, 1200, 120, "ATALHO", ["juros de UM período  ×  número de períodos"], acc, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "A CONTA DE UM MÊS SÓ", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    etiqueta(c, "C", "R$ 800,00", 560, 300, aa)
    etiqueta(c, "i", "3% a.m. = 0,03", 960, 300, aa)
    etiqueta(c, "t", "5 meses", 1360, 300, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        linha(c, [("J = ?", GREEN), ("     ", INK), ("M = ?", RED)], W / 2, 450, 56, ab * (1 - ep(t, C["17"], 0.3)))
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 600)
    if t < C["17"]:
        return
    linha(c, [("3% de 800 = ", INK), ("R$ 24,00 por mês", GREEN)], W / 2, 450, 44, ep(t, C["17.a"], 0.4))
    linha(c, [("J = 24 × 5 = ", INK), ("R$ 120,00", GREEN)], W / 2, 540, 48, ep(t, C["17.b"], 0.4))
    linha(c, [("M = 800 + 120 = ", INK), ("R$ 920,00", RED)], W / 2, 630, 48, ep(t, C["17.c"], 0.4))
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        linha(c, [("fator 1,15:  800 · 1,15 = 920", INK2)], W / 2, 730, 34, ad)
        conferido(c, "bateu", 1460, 745, ep(t, C["17.d"] + 2.4, 0.4), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Juros são o aluguel do dinheiro, sempre sobre o capital inicial.",
          "Juros é o acréscimo; montante é o total.",
          "Calcule um período e multiplique pelo tempo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Responder o montante quando pedem os juros (ou o contrário)", "a conta está perfeita e o número está lá",
          "leia a pergunta: RENDEU é J · TOTAL é M"),
         ("Usar 2 em vez de 0,02: 1.500 · 2 · 6 = R$ 18.000,00", "a taxa é mesmo 2%",
          "o % é um ÷ 100 escondido: 2% = 0,02"),
         ("1,5% virando 0,15 (R$ 600,00) ou 0,0015 (R$ 6,00)", "os algarismos 1 e 5 estão lá",
          "1,5% = 0,015 → R$ 1.000,00 por 4 meses: R$ 60,00")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questão 1 (eu faço) e você faz
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


ALTS1 = [("A", "R$ 28,80", "usou 0,15% (0,0015)", RED), ("B", "R$ 36,00", "juro de 1 mês só", RED),
         ("C", "R$ 288,00", "", GREEN), ("D", "R$ 2.688,00", "é o montante", RED), ("E", "R$ 2.880,00", "usou 15% (0,15)", RED)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "JUROS DE UMA APLICAÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Uma pessoa aplicou R$ 2.400,00 em um investimento que paga juros simples de 1,5% ao mês. "
                           "Ao final de 8 meses, o valor dos juros recebidos será de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 44, C["23.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["23"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["23"], 0.4))
        aa = ep(t, C["23.a"], 0.4)
        if aa > 0:
            for k, (L, v) in enumerate((("C", "2.400"), ("i", "0,015 a.m."), ("t", "8 meses"))):
                x = 250 + k * 225
                rrect(c, x - 10, y0 + 22, 210, 56, 14, mix("#FFFFFF", COR[L], 0.14), aa)
                linha(c, [(L + " ", COR[L]), (v, INK)], x + 95, y0 + 50, 26, aa)
        pill(c, "pede os JUROS → J", 540, y0 + 115, GREEN, size=24, a=ep(t, C["23.b"], 0.4), anchor="center")
        linha(c, [("1 mês: 24 + 12 = ", INK), ("36", GREEN)], 540, y0 + 180, 32, ep(t, C["23.c"], 0.4))
        linha(c, [("J = 36 × 8 = ", INK), ("R$ 288,00", GREEN)], 540, y0 + 240, 32, ep(t, C["23.d"], 0.4))
        conferido(c, "12% de 2.400 ≈ 288: plausível", 230, y0 + 300, ep(t, C["23.e"], 0.4), True, 24)
    af = ep(t, C["24.f"], 0.5)
    if af > 0:
        selo(c, 1340, 790, af, "OS DOIS ERROS DE VÍRGULA", AMBER, -2, 26)


def b_voce(c, t, C, B):
    head_seq(c, t, C, [("25", "VOCÊ FAZ", "E O MONTANTE?", GREEN), ("26", "CONFERINDO", "M = C + J", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["25.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 230, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("C = R$ 2.400,00", BLUE), ("  ·  ", GRAY), ("J = R$ 288,00", GREEN), ("  ·  ", GRAY), ("M = ?", RED)],
              W / 2, 295, 50, aa)
    pause_timer(c, t, C["25.end"] - 1.9, W / 2, 560)
    if t < C["26"]:
        return
    linha(c, [("M = 2.400 + 288 = ", INK), ("R$ 2.688,00", RED)], W / 2, 470, 60, ep(t, C["26.a"], 0.4))
    linha(c, [("fator 1 + 0,015 · 8 = 1,12  →  2.400 · 1,12 = 2.688", INK2)], W / 2, 580, 36, ep(t, C["26.b"], 0.4))
    acc = ep(t, C["26.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 720, acc, "É A ALTERNATIVA D: A ARMADILHA DA QUESTÃO 1", AMBER, -2, 32)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TAXA E TEMPO NA MESMA UNIDADE", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        linha(c, [("18% a.a.", PURPLE), ("   ·   ", GRAY), ("8 meses", AMBER)], W / 2, 300, 72, aa)
        text(c, "ao ANO × em MESES", W / 2, 380, 30, "black", GRAY, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        linha(c, [("5.000 · 0,18 · 8 = ", INK), ("R$ 7.200,00", RED)], W / 2, 500, 64, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 640, acc, "MAIS QUE O PRÓPRIO CAPITAL?!", RED, -3, 44)
    pill(c, "ep. 2 · taxa e tempo na mesma unidade", W / 2, 790, PURPLE, size=30, a=ep(t, C["28.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Você já confundiu juros com montante?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, palavras=b_palavras, jm=b_jm,
              siglas=b_siglas, simples=b_simples, formula=b_formula, decimal=b_decimal, exemplo=b_exemplo,
              cabeca=b_cabeca, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, voce=b_voce,
              ponte=b_ponte, cta=b_cta)
