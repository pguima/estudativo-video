"""Visual — Progressão Aritmética, Episódio 4: a PA disfarçada (juros simples, calendário, SAC) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, para, selo...).
Peças deste episódio: escada() (o EXTRATO cujas linhas viram degraus iguais; o capital fica no CHÃO, marcado "mês 0"),
extrato(), calendario() (folha de calendário com os dias da mesma semana acendendo de 7 em 7), boleto(),
juros_sac() (barras dos juros do SAC caindo 80 por vez), reta_pontos() (os montantes alinhados numa reta), linha(),
caixa(), conferido().
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
_s = importlib.util.spec_from_file_location("comum046", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pa_ep4_pa_disfarcada.mp4"
CARD_R = K.CARD_R
CHAO = "#8A7F6A"
SEMANA = ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SÁB"]


def brl(v):
    s = f"{v:,.0f}".replace(",", ".")
    return f"R$ {s}"


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


def caixa(c, cx, cy, tit, val, col, a, w=360, h=130):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 44, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 32, 24, "black", col, a)
    size = 42
    while text_w(val, "black", size) > w - 30:
        size -= 2
    text_mid(c, val, cx, cy + 20, size, "black", INK, a)


def escada(c, x, y_chao, itens, a, larg=150, passo=56, alfas=None, destaque=None, cor=PURPLE, size=30):
    """a escada de degraus iguais: itens = [(rótulo_mês, valor_texto)] da esquerda para a direita; o item 0 é o CHÃO
    (mês 0). Cada degrau sobe 'passo' px. alfas = {i: alfa}; destaque = índice que acende (verde)."""
    if a <= 0:
        return
    alfas = alfas or {}
    for i, (rot, val) in enumerate(itens):
        ai = a * alfas.get(i, 1.0)
        if ai <= 0:
            continue
        xx = x + i * larg
        if rot == "…":
            text_mid(c, "…", xx + larg / 2, y_chao - i * passo - 30, 60, "black", GRAY, ai)
            continue
        if i == 0:
            rrect(c, xx, y_chao - 92, larg - 8, 92, 10, mix("#FFFFFF", CHAO, 0.25), ai, shadow=True)
            c.drawRect(skia.Rect.MakeXYWH(xx - 30, y_chao, larg + 22, 8), paint(CHAO, ai))
            text(c, "CHÃO", xx + larg / 2 - 4, y_chao + 44, 22, "black", CHAO, ai)
            col = CHAO
            top = y_chao - 92
        else:
            hh = 92 + i * passo
            top = y_chao - hh
            col = GREEN if destaque == i else cor
            rrect(c, xx, top, larg - 8, hh, 10, mix("#FFFFFF", col, 0.12), ai, shadow=True)
            rrect(c, xx, top, larg - 8, 10, 5, col, ai * 0.85)
        sz = size
        while text_w(val, "black", sz) > larg - 18:
            sz -= 2
        text(c, val, xx + (larg - 8) / 2, top + 44, sz, "black", INK, ai)
        text(c, rot, xx + (larg - 8) / 2, top + 76, 20, "bold", col, ai)


def extrato(c, x, y, a, linhas=("R$ 1.030", "R$ 1.060", "R$ 1.090"), w=420):
    """extrato bancário estilizado"""
    if a <= 0:
        return
    rrect(c, x, y, w, 120 + 62 * len(linhas), 18, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 64, 18, BLUE, a * 0.9)
    text(c, "EXTRATO · APLICAÇÃO", x + w / 2, y + 42, 24, "black", "#FFFFFF", a)
    for k, s in enumerate(linhas):
        yy = y + 112 + k * 62
        text(c, f"mês {k + 1}", x + 30, yy, 26, "bold", GRAY, a, align="left")
        text(c, s, x + w - 30, yy, 30, "black", INK, a, align="right")
        line(c, x + 24, yy + 22, x + w - 24, yy + 22, LIGHT, a, 2)


def calendario(c, x, y, a, dia1=6, ndias=31, cel=86, acesos=None, cor=GREEN, marcas=None, titulo=None):
    """folha de calendário: dia1 = coluna do dia 1 (0 = DOM). acesos = {dia: alfa} acende o quadrado;
    marcas = {dia: (cor, alfa)} contorna."""
    if a <= 0:
        return
    acesos = acesos or {}
    marcas = marcas or {}
    w = 7 * cel
    nlin = (dia1 + ndias + 6) // 7
    rrect(c, x - 16, y - 70, w + 32, nlin * cel + 100, 20, "#FFFFFF", a, shadow=True)
    if titulo:
        text(c, titulo, x + w / 2, y - 92, 26, "black", INK2, a)
    for k, s in enumerate(SEMANA):
        text(c, s, x + k * cel + cel / 2, y - 26, 22, "black", RED if k == 0 else GRAY, a)
    for d in range(1, ndias + 1):
        pos = dia1 + d - 1
        col_, lin = pos % 7, pos // 7
        xx, yy = x + col_ * cel, y + lin * cel
        ac = a * acesos.get(d, 0.0)
        rrect(c, xx + 4, yy + 4, cel - 8, cel - 8, 10, "#F3F4F7", a)
        if ac > 0:
            rrect(c, xx + 4, yy + 4, cel - 8, cel - 8, 10, cor, ac * 0.9)
        if d in marcas:
            mc, ma = marcas[d]
            if ma > 0:
                rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx + 2, yy + 2, cel - 4, cel - 4), 12, 12)
                c.drawRRect(rr, paint(mc, a * ma, stroke=6))
        text_mid(c, str(d), xx + cel / 2, yy + cel / 2, 32, "black", "#FFFFFF" if ac > 0.5 else INK, a)


def boleto(c, x, y, a, valores=("R$ 2.400", "R$ 2.320", "R$ 2.240"), w=420):
    if a <= 0:
        return
    rrect(c, x, y, w, 120 + 62 * len(valores), 18, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, 64, 18, AMBER, a * 0.9)
    text(c, "BOLETO · FINANCIAMENTO", x + w / 2, y + 42, 24, "black", "#FFFFFF", a)
    for k, s in enumerate(valores):
        yy = y + 112 + k * 62
        text(c, f"parcela {k + 1}", x + 30, yy, 26, "bold", GRAY, a, align="left")
        text(c, s, x + w - 30, yy, 30, "black", INK, a, align="right")
        line(c, x + 24, yy + 22, x + w - 24, yy + 22, LIGHT, a, 2)


def juros_sac(c, x, y_base, a, prog_=1.0, larg=150, esc=0.7, cor=AMBER):
    """barras dos juros do SAC: 400, 320, 240, 160, 80"""
    if a <= 0:
        return
    vals = [400, 320, 240, 160, 80]
    line(c, x - 20, y_base, x + 5 * larg + 10, y_base, INK2, a, 3)
    for k, v in enumerate(vals):
        ak = a * clamp(prog_ * 5 - k)
        if ak <= 0:
            continue
        h = v * esc
        xx = x + k * larg
        rrect(c, xx, y_base - h, larg - 30, h, 10, cor, ak * 0.85)
        text(c, str(v), xx + (larg - 30) / 2, y_base - h - 16, 32, "black", INK, ak)
        text(c, f"mês {k + 1}", xx + (larg - 30) / 2, y_base + 40, 22, "bold", GRAY, ak)
        if k > 0:
            text(c, "−80", xx + (larg - 30) / 2, y_base - h - 56, 22, "black", RED, ak * 0.9)


def reta_pontos(c, x, y, w, h, a, prog_=1.0, n_max=6, reta=True):
    """montantes 2.000 + 60n como pontos alinhados (n = 0..n_max)"""
    if a <= 0:
        return
    vmin, vmax = 1950, 2000 + 60 * n_max + 30
    X = lambda n: x + w * n / n_max
    Y = lambda v: y + h * (vmax - v) / (vmax - vmin)
    rrect(c, x - 40, y - 30, w + 80, h + 90, 16, "#FFFFFF", a, shadow=True)
    line(c, x, y + h, x + w, y + h, INK2, a, 3)
    line(c, x, y, x, y + h, INK2, a, 3)
    text(c, "mês", x + w + 34, y + h + 8, 22, "bold", GRAY, a, align="left")
    if reta:
        ar = a * clamp(prog_)
        line(c, X(0), Y(2000), X(n_max * clamp(prog_)), Y(2000 + 60 * n_max * clamp(prog_)), PURPLE, ar * 0.6, 4)
    for n in range(n_max + 1):
        an = a * clamp(prog_ * (n_max + 1) - n)
        if an <= 0:
            continue
        c.drawCircle(X(n), Y(2000 + 60 * n), 11, paint(BLUE if n else CHAO, an))
        text(c, str(n), X(n), y + h + 36, 22, "bold", GRAY, an)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A PA DISFARÇADA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        pill(c, "SÉRIE DE JUROS SIMPLES", 420, 260, BLUE, size=26, a=aa, anchor="center", bounds=(0, 1920))
        caixa(c, 420, 360, "CAPITAL · TAXA", "R$ 1.000 · 3% ao mês", BLUE, aa, 520)
    ab = ep(t, C["01.b"], 0.5)
    itens = [("mês 0", "R$ 1.000"), ("mês 1", "R$ 1.030"), ("mês 2", "R$ 1.060"), ("mês 3", "R$ 1.090")]
    alf = {0: ab, 1: ep(t, C["01.b"], 0.4), 2: ep(t, C["01.b"] + 1.4, 0.4), 3: ep(t, C["01.b"] + 2.6, 0.4)}
    escada(c, 860, 720, itens, ab, larg=190, passo=70, alfas=alf)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        for k in range(3):
            xx = 860 + (k + 1) * 190 + 80
            text(c, "+30", xx - 95, 720 - 70 - (k + 1) * 70 - 26, 26, "black", GREEN, acc)
        selo(c, 420, 560, acc, "DEGRAUS DE R$ 30,00", GREEN, -3, 34)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "isso é uma PA escondida", 420, 700, ad, 36, PURPLE)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI RECONHECER A PA EM", GREEN)
    nomes = ["juros simples", "calendários", "depreciação", "treinos", "financiamentos"]
    aa = ep(t, C["02.a"], 0.5)
    for k, s in enumerate(nomes):
        a = ep(t, C["02.a"] + 0.6 * k, 0.4)
        if a <= 0:
            continue
        x = 220 + (k % 3) * 520
        y = 300 + (k // 3) * 170
        rrect(c, x, y, 460, 130, 24, mix("#FFFFFF", GREEN, 0.08), a, shadow=True)
        check_icon(c, x + 60, y + 65, 26, a, GREEN)
        text_mid(c, s, x + 110, y + 65, 40, "black", INK, a, align="left")
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 740, ab, "SEM ERRAR O \"MÊS 1\"", AMBER, -3, 36)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "2 LEMBRETES", "RÁPIDOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 180, 270 + d1, 760, 480, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "SÉRIE DE JUROS SIMPLES", 560, 320 + d1, GREEN, size=24, a=a1, anchor="center", bounds=(0, 1920))
        text(c, "C = capital (o que foi aplicado)", 560, 400 + d1, 28, "bold", BLUE, a1)
        text(c, "i = taxa (quanto rende por mês)", 560, 450 + d1, 28, "bold", BLUE, a1)
        linha(c, [("J = ", INK), ("C · i · t", PURPLE)], 560, 550 + d1, 54, a1)
        linha(c, [("M = ", INK), ("C + J", PURPLE)], 560, 650 + d1, 54, a1)
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 980, 270 + d2, 760, 480, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "EPISÓDIO 1", 1360, 320 + d2, GREEN, size=24, a=a2, anchor="center", bounds=(0, 1920))
        text(c, "o termo de posição n", 1360, 420 + d2, 30, "bold", INK2, a2)
        linha(c, [("termo n = ", INK), ("1º termo", BLUE), (" + (n − 1) · ", INK), ("r", GREEN)], 1360, 540 + d2, 44,
              a2)
        text(c, "r = razão (o degrau)", 1360, 650 + d2, 28, "bold", GRAY, a2)


# ======================================================================
# concreto e bloco a
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS PAPÉIS", "DO DIA A DIA", BLUE)
    card(c, *CARD_R)
    extrato(c, 190, 270, ep(t, C["04.a"], 0.5), w=430)
    calendario(c, 760, 330, ep(t, C["04.b"], 0.5), cel=58, acesos={d: ep(t, C["04.b"] + 0.3 * k, 0.3)
                                                                    for k, d in enumerate((3, 10, 17, 24, 31))})
    boleto(c, 1290, 270, ep(t, C["04.c"], 0.5), w=430)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "um aumento (ou uma queda) sempre igual", W / 2, 790, ad, 36, PURPLE)


TABELA = [("05.a", "juros simples", "o juro de cada mês é o mesmo", "C · i", BLUE),
          ("05.b", "depreciação linear", "perde o mesmo valor por ano", "negativa", RED),
          ("05.c", "calendário", "a semana se repete", "7", PURPLE),
          ("05.d", "treino progressivo", "mesmo aumento por dia", "o aumento", GREEN),
          ("05.e", "padrões de figuras", "mesmas peças a cada etapa", "as peças", AMBER)]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "ONDE A PA SE ESCONDE", "SITUAÇÃO · POR QUÊ · RAZÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["05.t"], 0.4)
    if a0 > 0:
        for s, x in (("SITUAÇÃO", 200), ("POR QUE É PA", 760), ("RAZÃO", 1500)):
            text(c, s, x, 250, 24, "black", GRAY, a0, align="left")
    for k, (cue, sit, pq, raz, col) in enumerate(TABELA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 104 + d
        rrect(c, 180, y, 1560, 90, 18, mix("#FFFFFF", col, 0.07), a, shadow=True)
        text_mid(c, sit, 210, y + 45, 36, "black", col, a, align="left")
        text_mid(c, pq, 760, y + 45, 30, "bold", INK2, a, align="left")
        text_mid(c, raz, 1500, y + 45, 36, "black", INK, a, align="left")
    if t > C["05.b"] + 2.5 and t < C["05.c"]:
        pass


# ======================================================================
# bloco b — juros simples e o termo zero
# ======================================================================

ESC_2000 = [("mês 0", "2.000"), ("mês 1", "2.060"), ("mês 2", "2.120"), ("mês 3", "2.180"), ("mês 4", "2.240"),
            ("mês 5", "2.300")]


def b_juros(c, t, C, B):
    head_seq(c, t, C, [("06", "JUROS SIMPLES", "ONDE FICA O CHÃO?", BLUE),
                       ("07", "O MÊS n", "O CHÃO + n DEGRAUS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    aa = ep(t, C["06.a"], 0.5)
    if sid == "06":
        if aa > 0:
            linha(c, [("degrau = C · i = 2.000 · 0,03 = ", INK), ("R$ 60", GREEN)], 560, 290, 38, aa)
        ab = ep(t, C["06.b"], 0.5)
        escada(c, 230, 720, ESC_2000[:2], ab, larg=200, passo=60,
               alfas={0: 1.0, 1: ep(t, C["06.b"] + 2.5, 0.5)})
        if ab > 0:
            text(c, "dia da aplicação", 330, 600, 24, "bold", CHAO, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            rrect(c, 900, 380, 760, 300, 24, mix("#FFFFFF", BLUE, 0.08), acc, shadow=True)
            text(c, "TERMO ZERO", 1280, 440, 34, "black", BLUE, acc)
            para(c, "o valor no instante da aplicação, antes do primeiro mês", 950, 510, 34, "bold", INK2, acc, 660)
            linha(c, [("termo zero = ", INK), ("R$ 2.000", CHAO)], 1280, 630, 44, acc)
        return
    na = 1 if t < C["07.a"] + 1.5 else (2 if t < C["07.b"] else 6)
    alf = {i: (1.0 if i < na else ep(t, C["07.b"] + 0.4 * (i - 2), 0.4)) for i in range(6)}
    escada(c, 200, 760, ESC_2000, 1.0, larg=150, passo=52, alfas=alf,
           destaque=5 if t > C["07.c"] else None)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 1120, 260, 560, 150, 22, mix("#FFFFFF", PURPLE, 0.08), ab, shadow=True)
        text(c, "montante do mês n", 1400, 300, 26, "bold", GRAY, ab)
        linha(c, [("M = ", INK), ("2.000", CHAO), (" + ", INK), ("60", GREEN), (" · n", INK)], 1400, 360, 50, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        linha(c, [("mês 5: 2.000 + 5 · 60 = ", INK), ("2.300", GREEN)], 1400, 470, 36, acc)
        K.atalho(c, 1120, 540, 560, 170, "ATALHO", ["montante = chão + n degraus"], ep(t, C["07.c"] + 2.0, 0.5), 32)


# ======================================================================
# bloco c — calendário
# ======================================================================

def b_calendario(c, t, C, B):
    head_seq(c, t, C, [("08", "O CALENDÁRIO", "PA DE RAZÃO 7", PURPLE),
                       ("09", "UMA DATA MAIS LONGE", "OLHE O RESTO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        a0 = ep(t, C["08.t"], 0.5)
        segs = (3, 10, 17, 24, 31)
        ac = {3: ep(t, C["08.a"], 0.4), 10: ep(t, C["08.a"] + 1.6, 0.4)}
        for k, d in enumerate(segs[2:]):
            ac[d] = ep(t, C["08.b"] + 0.9 * k, 0.4)
        calendario(c, 240, 300, a0, cel=84, acesos=ac)
        for k, d in enumerate(segs[:-1]):
            ak = ac.get(segs[k + 1], 0)
            if ak > 0:
                text(c, "+7", 196, 300 + k * 84 + 84, 26, "black", GREEN, ak)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            rrect(c, 1020, 360, 660, 280, 24, mix("#FFFFFF", PURPLE, 0.08), acc, shadow=True)
            text(c, "as segundas-feiras", 1350, 420, 30, "bold", GRAY, acc)
            text_mid(c, "3, 10, 17, 24, 31", 1350, 500, 52, "black", INK, acc)
            text(c, "PA de razão 7", 1350, 590, 44, "black", PURPLE, acc)
        return
    marcas = {3: (BLUE, 1.0), 20: (AMBER, ep(t, C["09.a"], 0.4))}
    ac = {3: 1.0, 10: 1.0, 17: 1.0}
    if t > C["09.c"]:
        ac[20] = ep(t, C["09.c"], 0.5)
    calendario(c, 240, 300, 1.0, cel=84, acesos=ac, marcas=marcas, cor=GREEN)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        linha(c, [("distância: 20 − 3 = ", INK), ("17 dias", AMBER)], 1340, 320, 40, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        linha(c, [("17 = ", INK), ("2", BLUE), (" · 7 + ", INK), ("3", GREEN)], 1340, 410, 52, ab)
        text(c, "2 semanas inteiras · sobram 3", 1340, 480, 28, "bold", GRAY, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        linha(c, [("segunda + 3 = ", INK), ("quinta", GREEN)], 1340, 560, 44, acc)
        K.atalho(c, 1040, 610, 600, 160, "ATALHO", ["o resto diz quantos dias andar"], ep(t, C["09.c"] + 2.4, 0.5), 32)


# ======================================================================
# bloco d — SAC; bloco e — função afim
# ======================================================================

def b_sac(c, t, C, B):
    head(c, t, B["start"], "O BOLETO QUE DIMINUI", "SAC · SÉRIE DE EMPRÉSTIMOS", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 260, 1520, 110, 22, mix("#FFFFFF", BLUE, 0.08), aa, shadow=True)
        text_mid(c, "AMORTIZAÇÃO", 240, 315, 34, "black", BLUE, aa, align="left")
        text_mid(c, "= a parte da parcela que paga a dívida em si (sempre igual)", 520, 315, 30, "bold", INK2, aa,
                 align="left")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        text(c, "JUROS DE CADA PARCELA (R$)", 640, 430, 26, "black", AMBER, ab)
    juros_sac(c, 260, 780, ab, prog_=ep(t, C["10.b"], 3.5), larg=170, esc=0.7)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 1240, 470, 440, 220, 24, mix("#FFFFFF", PURPLE, 0.08), acc, shadow=True)
        text(c, "PA de razão", 1460, 540, 34, "bold", INK2, acc)
        text_mid(c, "−80", 1460, 625, 80, "black", PURPLE, acc)


def b_afim(c, t, C, B):
    head(c, t, B["start"], "A PONTE COM A FUNÇÃO AFIM", "POR QUE PARECE UMA RETA?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    reta_pontos(c, 260, 300, 620, 380, aa, prog_=ep(t, C["11.a"], 2.5), reta=t > C["11.c"])
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        for k, (L, R, col) in enumerate((("razão", "taxa de variação", GREEN), ("termo zero", "valor inicial", CHAO))):
            y = 330 + k * 150
            rrect(c, 1040, y, 640, 120, 22, "#FFFFFF", ab, shadow=True)
            text_mid(c, L, 1080, y + 60, 38, "black", col, ab, align="left")
            text_mid(c, "=  " + R, 1300, y + 60, 34, "bold", INK2, ab, align="left")
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        linha(c, [("M(n) = ", INK), ("2.000", CHAO), (" + ", INK), ("60", GREEN), ("n", INK)], 1360, 680, 50, acc)
        text(c, "pontos alinhados numa reta", 1360, 760, 28, "bold", PURPLE, acc)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("12", "SUA VEZ · CALENDÁRIO", "PAUSE E TENTE", GREEN),
                       ("13", "VAMOS JUNTOS", "CONTE OS SALTOS", GREEN)])
    card(c, *CARD_R)
    marcas = {4: (BLUE, ep(t, C["12.a"], 0.4)), 29: (AMBER, ep(t, C["12.b"], 0.4))}
    ac = {4: ep(t, C["12.a"], 0.4)}
    if t > C["13.b"]:
        for k, d in enumerate((11, 18, 25)):
            ac[d] = ep(t, C["13.b"] + 0.5 * k, 0.3)
    if t > C["13.c"]:
        ac[29] = ep(t, C["13.c"] + 2.5, 0.5)
    calendario(c, 240, 300, ep(t, C["12.t"], 0.5), cel=84, acesos=ac, marcas=marcas, cor=GREEN)
    if t < C["13"]:
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            text_mid(c, "dia 4 = terça", 1340, 360, 50, "black", BLUE, ab)
            text_mid(c, "dia 29 = ?", 1340, 460, 64, "black", AMBER, ab)
        pause_timer(c, t, C["12.end"] - 1.9, 1340, 620)
        return
    linha(c, [("29 − 4 = ", INK), ("25 dias", AMBER)], 1340, 340, 44, ep(t, C["13.a"], 0.5))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("25 = ", INK), ("3", BLUE), (" · 7 + ", INK), ("4", GREEN)], 1340, 440, 54, ab)
        text(c, "3 semanas inteiras · sobram 4", 1340, 510, 28, "bold", GRAY, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        text(c, "terça → qua · qui · sex · sáb", 1340, 590, 32, "bold", INK2, acc)
        text_mid(c, "SÁBADO", 1340, 680, 70, "black", GREEN, ep(t, C["13.c"] + 2.5, 0.5))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Aumento constante é PA, mesmo sem o nome.",
          "Juros simples: o capital é o termo zero.",
          "A semana é uma PA de razão 7: olhe o resto da divisão."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "21"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Capital como termo 1: 1.000 + (6 − 1) · 30 = 1.150", "é a fórmula do episódio 1, com n − 1",
          "o capital é o chão (mês 0): no mês 6 são 6 degraus → 1.000 + 6 · 30 = 1.180"),
         ("Contar o dia de partida: do dia 4 ao 29 = 26 dias", "o dia 4 está ali, no calendário",
          "você já está no dia 4: contam os saltos, 29 − 4 = 25"),
         ("Juros do SAC constantes: 400 · 5 = 2.000", "a amortização é constante",
          "os juros caem com a dívida: (400 + 80) · 5 ÷ 2 = 1.200")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["15", "16", "17"], ERROS)


# ======================================================================
# questão 7 (você faz)
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


ALTS7 = [("A", "17", "partiu de 2.060 e esqueceu o + 1", RED), ("B", "18", "", GREEN),
         ("C", "19", "2.000 como termo 1: n − 1", RED), ("D", "36", "juro de R$ 30 ao mês", RED),
         ("E", "51", "3.080 ÷ 60: o montante inteiro", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · VOCÊ FAZ", "JUROS SIMPLES COMO PA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["18.a"], 0.4)
    yend = _enunciado(c, "Um capital de R$ 2.000,00 foi aplicado a juros simples de 3% ao mês. Os montantes ao fim de "
                      "cada mês formam uma progressão aritmética. O montante atinge R$ 3.080,00 ao fim do mês de "
                      "número", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["19"], 0.3)), align="left")
    cues_in = {L: C[f"18.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"20.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 250, 680, 40, C["19.ok"], "B", cues_in, cues_x, gap=34)
    if t < C["19"]:
        pause_timer(c, t, C["18.end"] - 2.4, 540, 680, dur=2.1)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["19"], 0.4), shadow=True)
    linha(c, [("mês 0 = ", INK), ("2.000", CHAO), (" (o chão)", GRAY)], 540, y0 + 50, 30, ep(t, C["19.a"], 0.4))
    linha(c, [("degrau: 0,03 · 2.000 = ", INK), ("60", GREEN)], 540, y0 + 105, 30, ep(t, C["19.b"], 0.4))
    linha(c, [("2.000 + 60n = 3.080", INK)], 540, y0 + 160, 32, ep(t, C["19.b"] + 2.5, 0.4))
    linha(c, [("60n = 1.080  →  n = ", INK), ("18", PURPLE)], 540, y0 + 215, 32, ep(t, C["19.c"], 0.4))
    ad = ep(t, C["19.d"], 0.4)
    if ad > 0:
        linha(c, [("18 · 60 = ", INK), ("1.080", GREEN), (" de juros", INK)], 470, y0 + 270, 28, ad)
        conferido(c, "", 700, y0 + 280, ad, True, 30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DA PA", PURPLE)
    itens = [("22.a", "juntamos tudo", "n − 1 · saltos · Gauss · disfarces"),
             ("22.b", "caçamos as pegadinhas", "verdadeiro ou falso"),
             ("22.c", "treinamos para o ENEM", "questões inéditas")]
    for k, (cue, s, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 300 + d, 480, 300, 24, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, x + 240, 370 + d, a, 34, bg=PURPLE)
        sz = 34
        while text_w(s, "black", sz) > 440:
            sz -= 2
        text(c, s, x + 240, 480 + d, sz, "black", INK, a)
        sz2 = 24
        while text_w(sub, "bold", sz2) > 440:
            sz2 -= 1
        text(c, sub, x + 240, 540 + d, sz2, "bold", GRAY, a)
    pill(c, "ep. 5 · revisão", W / 2, 760, PURPLE, size=30, a=ep(t, C["22.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["23.like"], C["23.sub"], C["23.bell"], C["23.com"], C["23.bye"],
        "Dia 1 é domingo: que dia é o 30?", canal="no Estudativo", anki=C["23.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, tabela=b_tabela, juros=b_juros,
              calendario=b_calendario, sac=b_sac, afim=b_afim, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q7=b_q7, ponte=b_ponte, cta=b_cta)
