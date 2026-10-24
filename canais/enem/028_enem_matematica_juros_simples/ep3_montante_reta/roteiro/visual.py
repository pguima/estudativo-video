"""Visual — Juros Simples, Episódio 3: o montante é uma reta (gráfico, tabela e PA) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho...).
Peças deste episódio: Graf (eixos tempo × montante com corte no eixo vertical), escada_juros() (degraus iguais,
cada um rotulado com os juros de um mês), reta_m(), tracejada do capital, juros_acum() (faixa entre a reta e o capital),
triangulo() (inclinação entre dois pontos), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import math
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
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_simples_ep3_montante_reta.mp4"
CARD_R = K.CARD_R

# cor de cada letra
COR = dict(C=BLUE, i=PURPLE, t=AMBER, J=GREEN, M=RED)


def brl(v, cents=False):
    s = f"{v:,.2f}" if cents else f"{v:,.0f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


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


class Graf:
    """eixos: horizontal = tempo (meses), vertical = montante (R$). (x, y, w, h) = área útil; o eixo vertical não começa
    no zero (marca de corte)."""

    def __init__(s, x, y, w, h, tmax, vmin, vmax):
        s.x, s.y, s.w, s.h, s.tmax, s.vmin, s.vmax = x, y, w, h, tmax, vmin, vmax

    def P(s, t, v):
        return s.x + s.w * t / s.tmax, s.y + s.h - s.h * (v - s.vmin) / (s.vmax - s.vmin)

    def eixos(s, c, a, xticks=(), yticks=(), size=22, xlab="tempo (meses)", ylab="montante (R$)", grid=True):
        if a <= 0:
            return
        x0, y0 = s.x, s.y + s.h
        if grid:
            for v in yticks:
                _, yy = s.P(0, v)
                line(c, x0, yy, x0 + s.w, yy, "#ECECE8", a, 2)
        arrow(c, x0, y0, x0 + s.w + 40, y0, INK2, a, 4, 14)
        arrow(c, x0, y0, x0, s.y - 40, INK2, a, 4, 14)
        # corte do eixo vertical (não começa no zero)
        zz = skia.Path(); zz.moveTo(x0 - 12, y0 - 18); zz.lineTo(x0 + 12, y0 - 26); zz.moveTo(x0 - 12, y0 - 30)
        zz.lineTo(x0 + 12, y0 - 38)
        c.drawPath(zz, paint(INK2, a, stroke=3))
        for tk in xticks:
            xx, _ = s.P(tk, s.vmin)
            line(c, xx, y0 - 6, xx, y0 + 6, INK2, a, 2)
            text(c, str(tk), xx, y0 + 34, size, "bold", GRAY, a)
        for v in yticks:
            _, yy = s.P(0, v)
            line(c, x0 - 6, yy, x0 + 6, yy, INK2, a, 2)
            text(c, brl(v), x0 - 14, yy + size * 0.36, size, "bold", GRAY, a, align="right")
        text(c, xlab, x0 + s.w + 30, y0 + 66, size, "black", AMBER, a, align="right")
        text(c, ylab, x0 + 10, s.y - 54, size, "black", RED, a, align="left")


def ponto(c, g, t, v, a, col=RED, r=11, rot=None, dx=18, dy=-18, size=24, align="left"):
    if a <= 0:
        return
    x, y = g.P(t, v)
    c.drawCircle(x, y, r + 5, paint("#FFFFFF", a))
    c.drawCircle(x, y, r, paint(col, a))
    if rot:
        fmid(c, rot, x + dx, y + dy, size, "black", col, a, align=align)


def escada_juros(c, g, C0, deg, n, prog_, a, rot=None, col=GREEN, size=17):
    """n degraus iguais (prog_ 0 → 1 desenha um degrau por vez); rot = rótulo de cada degrau"""
    if a <= 0 or prog_ <= 0:
        return
    for k in range(n):
        u = clamp(prog_ * n - k)
        if u <= 0:
            break
        xa, ya = g.P(k, C0 + deg * k)
        xb, yb = g.P(k + 1, C0 + deg * (k + 1))
        line(c, xa, ya, xb, ya, col, a, 5, progress=clamp(u * 2))
        if u > 0.5:
            line(c, xb, ya, xb, yb, col, a, 5, progress=clamp(u * 2 - 1))
        if rot and u >= 1:
            text(c, rot, xb + 6, (ya + yb) / 2 + size * 0.36, size, "black", col, a, align="left")


def reta_m(c, g, t0, v0, t1, v1, a, prog_=1.0, col=RED, w=6):
    xa, ya = g.P(t0, v0)
    xb, yb = g.P(t1, v1)
    line(c, xa, ya, xb, yb, col, a, w, progress=prog_)


def tracejada(c, g, v, a, rot=None, col=BLUE):
    if a <= 0:
        return
    xa, y = g.P(0, v)
    xb, _ = g.P(g.tmax, v)
    line(c, xa, y, xb, y, col, a, 3, dash=[14, 10])
    if rot:
        text(c, rot, xb, y - 14, 22, "black", col, a, align="right")


def juros_acum(c, g, C0, deg, t_ate, a, rot=None):
    """faixa entre a reta e a tracejada do capital, de 0 até t_ate, com a chave dos juros acumulados"""
    if a <= 0:
        return
    p = skia.Path()
    x0, y0 = g.P(0, C0)
    x1, y1 = g.P(t_ate, C0 + deg * t_ate)
    x2, y2 = g.P(t_ate, C0)
    p.moveTo(x0, y0); p.lineTo(x1, y1); p.lineTo(x2, y2); p.close()
    c.drawPath(p, paint(AMBER, a * 0.28))
    line(c, x1 + 22, y1, x1 + 22, y2, AMBER, a, 4)
    line(c, x1 + 14, y1, x1 + 30, y1, AMBER, a, 4)
    line(c, x1 + 14, y2, x1 + 30, y2, AMBER, a, 4)
    if rot:
        rrect(c, 1340, 560, 380, 130, 20, mix("#FFFFFF", AMBER, 0.14), a)
        text(c, f"JUROS ACUMULADOS (mês {t_ate})", 1530, 610, 22, "black", AMBER, a)
        fmid(c, rot, 1530, 650, 36, "black", INK, a)


def triangulo(c, g, t0, v0, t1, v1, a, rot_h, rot_v, col=PURPLE, size=24):
    """triângulo de inclinação: cateto horizontal (tempo) e vertical (subida)"""
    if a <= 0:
        return
    xa, ya = g.P(t0, v0)
    xb, yb = g.P(t1, v1)
    line(c, xa, ya, xb, ya, col, a, 4, dash=[10, 8])
    line(c, xb, ya, xb, yb, col, a, 4, dash=[10, 8])
    fmid(c, rot_h, (xa + xb) / 2, ya + 30, size, "black", AMBER, a)
    fmid(c, rot_v, xb + 14, (ya + yb) / 2, size, "black", GREEN, a, align="left")


def grafico_material(c, t, a, prog_esc=1.0, prog_reta=1.0, a_trac=1.0, x=330, y=280, w=900, h=420):
    """R$ 1.000,00 a 5% a.m., 10 meses"""
    g = Graf(x, y, w, h, 10, 950, 1550)
    g.eixos(c, a, range(0, 11), (1000, 1100, 1200, 1300, 1400, 1500))
    escada_juros(c, g, 1000, 50, 10, prog_esc, a * 0.9, "R$ 50,00", GREEN, 15)
    reta_m(c, g, 0, 1000, 10, 1500, a, prog_reta)
    tracejada(c, g, 1000, a * a_trac, "capital: R$ 1.000,00")
    return g


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "JUROS SIMPLES NO GRÁFICO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    g = Graf(300, 270, 820, 440, 10, 950, 1550)
    g.eixos(c, aa, (), (), grid=False)
    reta_m(c, g, 0, 1000, 10, 1500, aa, ep(t, C["01.a"] + 0.3, 1.2))
    ponto(c, g, 0, 1000, ep(t, C["01.a"] + 1.6, 0.4))
    ponto(c, g, 7, 1350, ep(t, C["01.a"] + 2.1, 0.4))
    itens = [("01.b", "o CAPITAL", BLUE), ("01.c", "os JUROS de cada mês", GREEN), ("01.d", "a TAXA", PURPLE)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 130 + d
        rrect(c, 1240, y - 50, 440, 100, 20, "#FFFFFF", a, shadow=True)
        rrect(c, 1240, y - 50, 14, 100, 7, col, a)
        text_mid(c, "?", 1300, y, 52, "black", col, a)
        text_mid(c, s, 1340, y, 32, "black", INK, a, align="left")
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, 1500, 745, ae, "SEM NENHUMA FÓRMULA NOVA", GREEN, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "ler CAPITAL e TAXA num gráfico ou numa tabela", "começo da reta · degrau ÷ capital"),
            ("02.b", "reconhecer a SEQUÊNCIA dos montantes", "1.030 · 1.060 · 1.090 · ...")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "ANTES DE COMEÇAR", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "DO EPISÓDIO 1", 540, 290, 32, "black", PURPLE, aa)
        linha(c, [("M = ", RED), ("C", BLUE), (" + ", INK), ("C · i · t", INK)], 540, 400, 60, aa)
        linha(c, [("juros de 1 mês = ", INK2), ("C · i", GREEN)], 540, 510, 44, ep(t, C["03.a"] + 2.6, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    line(c, 960, 250, 960, 760, "#E6E6E2", ab, 3)
    if ab > 0:
        g = Graf(1120, 330, 520, 300, 6, 950, 1350)
        g.eixos(c, ab, range(0, 7), (1000, 1100, 1200, 1300), 20, "tempo", "montante")
        ac = ep(t, C["03.c"], 0.5)
        if ac > 0:
            x, y = g.P(3, 1150)
            line(c, x, y, x, g.y + g.h, AMBER, ac, 3, dash=[8, 6])
            line(c, g.x, y, x, y, RED, ac, 3, dash=[8, 6])
            ponto(c, g, 3, 1150, ac, RED, 10)
            pill(c, "no mês 3, havia R$ 1.150,00", 1380, 760, INK, size=26, a=ac, anchor="center")


# ======================================================================
# concreto — o extrato e a escada
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "O EXTRATO DE UMA APLICAÇÃO", "O QUE ELE TEM DE ESPECIAL?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 230, 560, 520, 24, "#FFFFFF", aa, shadow=True)
        text(c, "EXTRATO", 500, 285, 28, "black", BLUE, aa, tracking=2)
        vals = [1000, 1050, 1100, 1150]
        for k, v in enumerate(vals):
            a = ep(t, C["04.a"] + 0.2 + k * 1.6, 0.4)
            y = 370 + k * 100
            text(c, f"mês {k}", 280, y, 32, "bold", GRAY, a, align="left")
            fmid(c, f"R$ {brl(v)},00", 720, y - 10, 38, "black", INK, a, align="right")
            if k:
                pill(c, "+ 50", 760, y - 60, GREEN, size=22, a=ep(t, C["04.b"], 0.4) * a, anchor="left")
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        g = Graf(980, 280, 640, 380, 3, 960, 1200)
        escada_juros(c, g, 1000, 50, 3, ep(t, C["04.b"], 1.5), ab, "R$ 50,00", GREEN, 22)
        for k in range(4):
            ponto(c, g, k, 1000 + 50 * k, ep(t, C["04.b"] + 0.4 * k, 0.3), RED, 9)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        regra(c, "cada degrau = os JUROS DE UM MÊS", 1300, 760, acc, 34, GREEN)


# ======================================================================
# bloco a — o montante como função do tempo
# ======================================================================

def b_funcao(c, t, C, B):
    head(c, t, B["start"], "A ESCADA NUMA LINHA SÓ", "O MONTANTE EM FUNÇÃO DO TEMPO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 460, 250, 1000, 110, 22, "#F7F7F5", aa)
        linha(c, [("você diz o MÊS ", AMBER), ("  →  ", GRAY), (" a regra devolve o MONTANTE", RED)], W / 2, 305, 36,
              aa)
    ab = ep(t, C["05.b"], 0.5)
    partes = [("M(t)", RED), (" = ", INK), ("C", BLUE), (" + ", INK), ("(C · i)", GREEN), (" · ", INK), ("t", AMBER)]
    size = 96
    if ab > 0:
        rrect(c, 360, 420, 1200, 170, 30, mix("#FFFFFF", PURPLE, 0.08), ab)
        linha(c, partes, W / 2, 505, size, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        ws = [text_w(s_, "black", size) for s_, _ in partes]
        x = W / 2 - sum(ws) / 2
        xs = []
        for w_ in ws:
            xs.append((x, x + w_)); x += w_
        notas = [(2, "onde a escada começa", BLUE, 0), (4, "a altura de cada degrau", GREEN, 0.8),
                 (6, "quantos degraus", AMBER, 1.6)]
        for idx, s, col, dt in notas:
            a = ep(t, C["05.c"] + dt * 2, 0.4)
            x0, x1 = xs[idx]
            line(c, x0 + 6, 610, x1 - 6, 610, col, a, 6)
            text(c, s, (x0 + x1) / 2, 670 + (40 if idx == 4 else 0), 28, "black", col, a)


# ======================================================================
# bloco b — o gráfico do material
# ======================================================================

def b_grafico(c, t, C, B):
    head(c, t, B["start"], "NO GRÁFICO", "R$ 1.000,00 A 5% AO MÊS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    pe = ep(t, C["06.b"], 4.0)
    pr = ep(t, C["06.b"] + 4.0, 1.2)
    ac = ep(t, C["06.c"], 0.5)
    g = grafico_material(c, t, aa, pe, pr, ac)
    if aa > 0:
        rrect(c, 1340, 250, 380, 150, 20, mix("#FFFFFF", BLUE, 0.08), aa)
        text(c, "GRÁFICO", 1530, 300, 26, "black", BLUE, aa, tracking=2)
        text(c, "como uma coisa muda", 1530, 340, 24, "bold", INK2, aa)
        text(c, "com outra", 1530, 372, 24, "bold", INK2, aa)
    if pr > 0.8:
        pill(c, "vira uma RETA", 1530, 470, RED, size=26, a=ep(t, C["06.b"] + 5.0, 0.4), anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    juros_acum(c, g, 1000, 50, 6, ad, "R$ 300,00")


# ======================================================================
# bloco c — começo e inclinação (função afim)
# ======================================================================

def b_afim(c, t, C, B):
    head(c, t, B["start"], "ONDE A RETA COMEÇA", "E QUANTO ELA SOBE", BLUE)
    card(c, *CARD_R)
    g = grafico_material(c, t, 1.0, 0.0, 1.0, 0.5, 330, 300, 880, 400)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        x, y = g.P(0, 1000)
        pulse = 0.5 + 0.5 * math.sin(t * 5)
        c.drawCircle(x, y, 26 + 8 * pulse, paint(BLUE, aa * 0.25))
        ponto(c, g, 0, 1000, aa, BLUE, 13)
        rrect(c, 1330, 250, 400, 170, 20, mix("#FFFFFF", BLUE, 0.08), aa)
        text(c, "mês 0 = dia do depósito", 1530, 300, 24, "black", BLUE, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        text(c, "PONTO INICIAL: a reta", 1530, 345, 22, "bold", INK2, ab)
        text(c, "começa no capital", 1530, 385, 26, "black", INK, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        triangulo(c, g, 3, 1150, 4, 1200, acc, "1 mês", "+ R$ 50,00")
        rrect(c, 1330, 450, 400, 150, 20, mix("#FFFFFF", PURPLE, 0.08), acc)
        text(c, "INCLINAÇÃO", 1530, 500, 26, "black", PURPLE, acc, tracking=2)
        text(c, "quanto sobe por mês", 1530, 540, 22, "bold", INK2, acc)
        linha(c, [("C · i = ", GREEN), ("R$ 50,00", INK)], 1530, 575, 28, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 1330, 630, 400, 180, 20, "#FFFFFF", ad, shadow=True)
        linha(c, [("y = ", INK), ("b", BLUE), (" + ", INK), ("a", GREEN), (" · x", INK)], 1530, 680, 40, ad)
        text(c, "b = capital  ·  a = C · i", 1530, 735, 22, "bold", INK2, ad)
        text(c, "FUNÇÃO AFIM (série própria)", 1530, 780, 22, "black", PURPLE, ad)


# ======================================================================
# bloco d — tempos iguais, juros iguais
# ======================================================================

def chave_v(c, g, t0, t1, v0, v1, a, s, col=GREEN, lado=1):
    if a <= 0:
        return
    xa, ya = g.P(t0, v0)
    xb, yb = g.P(t1, v1)
    line(c, xa, ya, xb, ya, col, a, 3, dash=[8, 6])
    line(c, xb, ya, xb, yb, col, a, 5)
    pill(c, s, xb + 16 * lado, (ya + yb) / 2, col, size=24, a=a, anchor="left" if lado > 0 else "right")


def b_iguais(c, t, C, B):
    head(c, t, B["start"], "NO COMEÇO OU NO FIM?", "TEMPOS IGUAIS", BLUE)
    card(c, *CARD_R)
    g = grafico_material(c, t, 1.0, 0.0, 1.0, 0.0, 330, 300, 1000, 400)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        xa, _ = g.P(0, 950); xb, _ = g.P(2, 950)
        rrect(c, xa, g.y + g.h - 7, xb - xa, 14, 7, AMBER, aa * 0.8)
        text(c, "2 meses", (xa + xb) / 2, g.y + g.h - 18, 22, "black", AMBER, aa)
        chave_v(c, g, 0, 2, 1000, 1100, aa, "+ R$ 100,00")
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        xa, _ = g.P(8, 950); xb, _ = g.P(10, 950)
        rrect(c, xa, g.y + g.h - 7, xb - xa, 14, 7, AMBER, ab * 0.8)
        text(c, "2 meses", (xa + xb) / 2, g.y + g.h - 18, 22, "black", AMBER, ab)
        chave_v(c, g, 8, 10, 1400, 1500, ab, "+ R$ 100,00")
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        regra(c, "TEMPOS IGUAIS, JUROS IGUAIS", 640, 260, acc, 34)


# ======================================================================
# bloco e — ler o gráfico (dois pontos) e o atalho dos 3 passos
# ======================================================================

def b_ler(c, t, C, B):
    head_seq(c, t, C, [("09", "SÓ DOIS PONTOS", "LENDO O GRÁFICO", BLUE), ("10", "ATALHO", "LER O GRÁFICO EM 3 PASSOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "10":
        steps = [("10.a", "1", "CAPITAL", "= o valor em t = 0"), ("10.b", "2", "JUROS POR MÊS", "= variação ÷ tempo"),
                 ("10.c", "3", "TAXA", "= degrau ÷ capital")]
        a0 = ep(t, C["10"], 0.4)
        K.boxed(c, 300, 230, 1320, 560, GREEN, a0, 0.06)
        text(c, "ATALHO", W / 2, 285, 26, "black", GREEN, a0, tracking=3)
        for k, (cue, n, nome, s) in enumerate(steps):
            a, d = rise(t, C[cue])
            y = 400 + k * 130 + d
            badge_num(c, n, 420, y - 12, a, 34, bg=GREEN)
            text(c, nome, 490, y, 46, "black", INK, a, align="left")
            text(c, s, 1000, y, 44, "black", GREEN, a, align="left")
        return
    g = Graf(330, 300, 720, 400, 5, 950, 1250)
    aa = ep(t, C["09.a"], 0.5)
    g.eixos(c, aa, range(0, 6), (1000, 1100, 1200))
    reta_m(c, g, 0, 1000, 5, 1250, aa * 0.5, 1.0, RED, 4)
    ponto(c, g, 0, 1000, aa, RED, 11)
    ponto(c, g, 4, 1200, ep(t, C["09.a"] + 1.5, 0.4), RED, 11, "(4; 1.200)", -18, -30, 24, "right")
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        x, y = g.P(0, 1000)
        c.drawCircle(x, y, 30, paint(BLUE, ab * 0.22))
        linha(c, [("1 ", GREEN), ("capital = ", INK), ("R$ 1.000,00", BLUE)], 1180, 330, 34, ab, align="left")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        triangulo(c, g, 0, 1000, 4, 1200, acc, "4 meses", "+ R$ 200,00")
        linha(c, [("2 ", GREEN), ("200 ÷ 4 = ", INK), ("R$ 50,00 por mês", GREEN)], 1180, 470, 34, acc, align="left")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        linha(c, [("3 ", GREEN), ("50 ÷ 1.000 = ", INK), ("0,05", PURPLE)], 1180, 610, 34, ad, align="left")
        linha(c, [("= ", INK), ("5% a.m.", PURPLE)], 1220, 670, 44, ad, align="left")
        pill(c, "÷ CAPITAL, nunca ÷ montante", 1180, 760, RED, size=24, a=ep(t, C["09.d"] + 1.4, 0.4))


# ======================================================================
# bloco f — o dobro do tempo
# ======================================================================

def b_dobro(c, t, C, B):
    head(c, t, B["start"], "O DOBRO DO TEMPO", "DÁ O DOBRO DOS JUROS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rows = [("2 meses", "R$ 100,00"), ("4 meses", "R$ 200,00")]
        for k, (tt, j) in enumerate(rows):
            a = ep(t, C["11.a"] + 1.5 + k * 1.6, 0.4)
            y = 330 + k * 150
            rrect(c, 260, y - 50, 560, 100, 20, "#FFFFFF", a, shadow=True)
            text_mid(c, tt, 400, y, 38, "black", AMBER, a)
            text_mid(c, "→", 540, y, 38, "black", GRAY, a)
            fmid(c, j, 680, y, 38, "black", GREEN, a)
        a2 = ep(t, C["11.a"] + 5.0, 0.4)
        arrow(c, 850, 340, 850, 470, PURPLE, a2, 4, 14)
        text(c, "× 2", 900, 418, 32, "black", PURPLE, a2, align="left")
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        regra(c, "juros e tempo: PROPORCIONAIS", 540, 620, ab, 32)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        K.atalho(c, 1040, 260, 640, 330, "ATALHO · REGRA DE TRÊS RÁPIDA",
                 ["3 meses → R$ 150,00", "1 mês → R$ 50,00", "12 meses → R$ 600,00"], acc, 36)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        selo(c, 1360, 700, ad, "SÓ EM JUROS SIMPLES", AMBER, -3, 36)


# ======================================================================
# bloco g — a PA dos montantes
# ======================================================================

def b_pa(c, t, C, B):
    head(c, t, B["start"], "A LISTA DOS MONTANTES", "R$ 1.000,00 A 3% AO MÊS", BLUE)
    card(c, *CARD_R)
    vals = [1030, 1060, 1090, 1120]
    xs = [360 + k * 360 for k in range(4)]
    for k, v in enumerate(vals):
        a = ep(t, C["12.a"] + 1.2 + k * 1.3, 0.4)
        if a <= 0:
            continue
        rrect(c, xs[k] - 140, 290, 280, 110, 22, "#FFFFFF", a, shadow=True)
        text(c, f"mês {k + 1}", xs[k], 275, 22, "bold", GRAY, a)
        fmid(c, brl(v), xs[k], 345, 50, "black", RED, a)
        if k:
            ab = ep(t, C["12.b"] + 0.3 * k, 0.4)
            if ab > 0:
                p = skia.Path()
                p.moveTo(xs[k - 1] + 40, 410); p.quadTo((xs[k - 1] + xs[k]) / 2, 500, xs[k] - 40, 410)
                c.drawPath(p, paint(GREEN, ab, stroke=4))
                pill(c, "+ 30", (xs[k - 1] + xs[k]) / 2, 480, GREEN, size=24, a=ab, anchor="center")
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 560, 680, 140, 20, mix("#FFFFFF", BLUE, 0.08), ab)
        text(c, "PROGRESSÃO ARITMÉTICA (PA)", 600, 610, 28, "black", BLUE, ab)
        text(c, "soma sempre o mesmo número", 600, 655, 26, "bold", INK2, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 560, 680, 140, 20, mix("#FFFFFF", BLUE, 0.08), acc)
        text(c, "RAZÃO DA PA = o número somado", 1320, 610, 26, "black", BLUE, acc)
        linha(c, [("1.000 · 0,03 = ", INK), ("R$ 30,00", GREEN)], 1320, 650, 32, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "ATALHO: razão = C · i (o degrau da escada)  ·  PA tem série própria", W / 2, 770, GREEN, size=26,
             a=ad, anchor="center")


# ======================================================================
# bloco h — onde o mercado usa
# ======================================================================

def b_mercado(c, t, C, B):
    head(c, t, B["start"], "NA VIDA REAL", "QUEM USA JUROS SIMPLES?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 240, 680, 450, 24, mix("#FFFFFF", GREEN, 0.07), aa)
        text(c, "JUROS SIMPLES · a reta", 570, 300, 32, "black", GREEN, aa)
        for k, s in enumerate(["conta atrasada (juros de mora)", "empréstimo informal", "cobranças por dia"]):
            a = ep(t, C["13.a"] + 0.8 * k, 0.4)
            check_icon(c, 300, 395 + k * 95, 22, a, GREEN)
            text(c, s, 340, 405 + k * 95, 32, "bold", INK, a, align="left")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 1010, 240, 680, 450, 24, mix("#FFFFFF", PURPLE, 0.07), ab)
        text(c, "JUROS COMPOSTOS · a curva", 1350, 300, 32, "black", PURPLE, ab)
        for k, s in enumerate(["bancos e financiamentos", "cartões de crédito"]):
            check_icon(c, 1080, 395 + k * 95, 22, ab, PURPLE)
            text(c, s, 1120, 405 + k * 95, 32, "bold", INK, ab, align="left")
        pill(c, "próxima série", 1350, 630, PURPLE, size=24, a=ab, anchor="center")
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        regra(c, "na prova, o ENUNCIADO diz o regime", W / 2, 770, acc, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "OS 3 PASSOS", GREEN)])
    card(c, *CARD_R)
    g = Graf(330, 300, 640, 380, 5, 2450, 2800)
    aa = ep(t, C["14.a"], 0.5)
    g.eixos(c, aa, range(0, 6), (2500, 2600, 2700))
    reta_m(c, g, 0, 2500, 5, 2750, aa * 0.6, 1.0, RED, 4)
    ponto(c, g, 0, 2500, aa, RED, 11, "R$ 2.500,00", 22, -30)
    ponto(c, g, 5, 2750, aa, RED, 11, "R$ 2.750,00", -20, -34, align="right")
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0 and t < C["15"]:
        linha(c, [("taxa mensal = ?", PURPLE)], 1370, 380, 50, ab)
    pause_timer(c, t, C["14.end"] - 1.9, 1370, 560)
    if t < C["15"]:
        return
    a1 = ep(t, C["15.a"], 0.4)
    if a1 > 0:
        x, y = g.P(0, 2500)
        c.drawCircle(x, y, 30, paint(BLUE, a1 * 0.22))
    linha(c, [("1 ", GREEN), ("capital = ", INK), ("R$ 2.500,00", BLUE)], 1080, 330, 34, a1, align="left")
    a2 = ep(t, C["15.b"], 0.4)
    triangulo(c, g, 0, 2500, 5, 2750, a2, "5 meses", "+ 250")
    linha(c, [("2 ", GREEN), ("250 ÷ 5 = ", INK), ("R$ 50,00 por mês", GREEN)], 1080, 450, 34, a2, align="left")
    a3 = ep(t, C["15.c"], 0.4)
    linha(c, [("3 ", GREEN), ("50 ÷ 2.500 = ", INK), ("0,02", PURPLE)], 1080, 570, 34, a3, align="left")
    if a3 > 0:
        selo(c, 1380, 700, ep(t, C["15.c"] + 2.0, 0.4), "2% AO MÊS", GREEN, -3, 44)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["O montante sobe uma escada de degraus iguais.",
          "A reta começa no capital.",
          "Taxa é o degrau dividido pelo capital."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "26"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("Dividir pelo MONTANTE FINAL: 50 ÷ 2.750 ≈ 1,8% a.m.", "o montante é o número que mais chama a atenção",
          "a taxa é sobre o CAPITAL (valor no mês 0): 50 ÷ 2.500 = 2%"),
         ("Esquecer os meses: 250 ÷ 2.500 = 10% \"ao mês\"", "R$ 250,00 é a subida que você vê no gráfico",
          "essa subida é de 5 meses: primeiro o degrau de 1 mês (R$ 50,00)"),
         ("Trocar razão e taxa: \"PA de razão 3\" ou \"taxa de 30%\"", "as duas medem o crescimento",
          "razão em REAIS (R$ 30,00) · taxa em POR CENTO (3%)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


# ======================================================================
# questão 7 (eu faço) e questão 6 (você faz)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS7 = [("A", "PG de razão 1,02", "juros compostos", PURPLE), ("B", "PA de razão 2", "razão ≠ taxa", RED),
         ("C", "PG de razão 100", "tipo errado", RED), ("D", "PA de razão 1,02", "razão dos compostos", RED),
         ("E", "PA de razão 100", "", GREEN)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · EU FAÇO", "A SEQUÊNCIA DOS MONTANTES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    yend = _enunciado(c, [("Um capital de R$ 5.000,00 é aplicado a juros simples de 2% ao mês. Os montantes ao final de "
                           "cada mês, a partir do primeiro, formam uma", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["21"], 0.3)),
         align="left")
    text(c, "PA = progressão aritmética · PG = progressão geométrica", 1000, 230, 20, "bold", GRAY, a0, align="left")
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS7, 1000, 270, 680, 36, C["21.ok"], "E", cues_in, cues_x, gap=40)
    if t >= C["21"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["21"], 0.4))
        linha(c, [("degrau: 2% de 5.000 = ", INK), ("R$ 100,00", GREEN)], 540, y0 + 50, 30, ep(t, C["21.a"], 0.4))
        ab = ep(t, C["21.b"], 0.4)
        for k, v in enumerate((5100, 5200, 5300)):
            a = ep(t, C["21.b"] + 0.6 * k, 0.3)
            fmid(c, brl(v), 300 + k * 230, y0 + 140, 36, "black", RED, a)
            if k:
                pill(c, "+100", 185 + k * 230, y0 + 190, GREEN, size=20, a=a * ab, anchor="center")
        acc = ep(t, C["21.c"], 0.4)
        if acc > 0:
            linha(c, [("soma constante → ", INK), ("PA", BLUE), (" · razão = C · i = ", INK), ("100", GREEN)], 540,
                  y0 + 270, 28, acc)


ALTS6 = [("A", "2%", "40 ÷ 2.000 (montante final)", RED), ("B", "2,5%", "", GREEN),
         ("C", "20%", "400 ÷ 2.000 (montante final)", RED), ("D", "25%", "400 ÷ 1.600: esqueceu os 10 meses", RED),
         ("E", "40%", "R$ 40,00 não é 40%", RED)]


def b_q6(c, t, C, B):
    head_seq(c, t, C, [("23", "QUESTÃO 6 · VOCÊ FAZ", "TAXA A PARTIR DO GRÁFICO", GREEN),
                       ("24", "CONFERINDO", "OS 3 PASSOS", GREEN), ("25", "AS ERRADAS", "CADA UMA É UM ERRO CLÁSSICO", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("O gráfico mostra a evolução do montante de uma aplicação a juros simples, desde o dia em que o "
                    "capital foi depositado. A taxa mensal de juros dessa aplicação é de", INK)], a0, 240, 24, 700)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["24"], 0.3)),
         align="left")
    ag = ep(t, C["23.g"], 0.5)
    g = Graf(300, 450, 520, 230, 10, 1400, 2100)
    g.eixos(c, ag, (0, 5, 10), (1600, 2000), 20, "meses", "montante (R$)")
    reta_m(c, g, 0, 1600, 10, 2000, ag, ep(t, C["23.g"], 1.0), RED, 5)
    ponto(c, g, 0, 1600, ag, RED, 10)
    ponto(c, g, 10, 2000, ag, RED, 10)
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS6, 1000, 240, 680, 32, C["24.ok"], "B", cues_in, cues_x, gap=16)
    if t < C["24"]:
        pause_timer(c, t, C["23.end"] - 1.9, 1340, 760)
        return
    a1 = ep(t, C["24.a"], 0.4)
    if a1 > 0:
        x, y = g.P(0, 1600)
        c.drawCircle(x, y, 26, paint(BLUE, a1 * 0.25))
    a2 = ep(t, C["24.b"], 0.4)
    triangulo(c, g, 0, 1600, 10, 2000, a2, "10 meses", "+ R$ 400,00", PURPLE, 20)
    if t < C["25"]:
        rrect(c, 1000, 600, 690, 220, 18, "#FFFFFF", ep(t, C["24.a"], 0.4), shadow=True)
        linha(c, [("1 ", GREEN), ("capital = ", INK), ("R$ 1.600,00", BLUE)], 1030, 635, 28, a1, align="left")
        linha(c, [("2 ", GREEN), ("400 ÷ 10 = ", INK), ("R$ 40,00 por mês", GREEN)], 1030, 690, 28, a2, align="left")
        linha(c, [("3 ", GREEN), ("40 ÷ 1.600 = 0,025 = ", INK), ("2,5% a.m.", PURPLE)], 1030, 745, 28,
              ep(t, C["24.c"], 0.4), align="left")
        conferido(c, "2,5% de 1.600 = 40: plausível", 1040, 800, ep(t, C["24.d"], 0.4), True, 24)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DESCOBRINDO CAPITAL, TAXA OU TEMPO", PURPLE)
    aa = ep(t, C["27.a"], 0.5)
    if aa > 0:
        linha(c, [("R$ 1.200,00", BLUE), ("  →  ", GRAY), ("R$ 1.500,00", RED), ("  em 10 meses", AMBER)], W / 2, 300,
              56, aa)
        linha(c, [("taxa ANUAL = ?", PURPLE)], W / 2, 400, 48, ep(t, C["27.a"] + 3.5, 0.4))
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        linha(c, [("C", BLUE), ("  →  ", GRAY), ("3 · C", RED), ("  a 2% a.m.:  ", PURPLE), ("quanto tempo?", AMBER)],
              W / 2, 540, 52, ab)
    pill(c, "ep. 4 · descobrindo capital, taxa ou tempo", W / 2, 720, PURPLE, size=30, a=ep(t, C["27.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"],
        "Você já tinha visto juros num gráfico?", canal="no Estudativo", anki=C["28.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, funcao=b_funcao,
              grafico=b_grafico, afim=b_afim, iguais=b_iguais, ler=b_ler, dobro=b_dobro, pa=b_pa, mercado=b_mercado,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q7=b_q7, q6=b_q6, ponte=b_ponte, cta=b_cta)
