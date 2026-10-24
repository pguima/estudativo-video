"""Visual — Juros Compostos, Episódio 3: potências sem calculadora e descobrir o tempo (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, erro_cards, atalho...).
Peças deste episódio: ficha() (bloco de fator), escada_pot() (1,1¹ … 1,1⁵ com "× 1,1"), conta_vertical() (somar a décima
parte), barra_prazo() (prazo quebrado em partes), regua() (régua da tentativa com a linha da meta), radar() (regra do 72),
linha().
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
_s = importlib.util.spec_from_file_location("comum029", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_compostos_ep3_potencias_tempo.mp4"
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


def m(c, s, cx, cy, size, a, col=None, align="center", cores=None):
    """expr matemática de uma cor (ou com cores por token)"""
    if cores is None:
        cores = {i: col or INK for i in range(40)}
    return K.expr(c, s, cx, cy, size, a, cores=cores, align=align)


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def ficha(c, s, cx, cy, a, col=PURPLE, size=60, w=None, sub=None):
    """bloco de fator (cartão com borda colorida)"""
    if a <= 0:
        return
    w = w or K.math_w(s, size) + 70
    h = size * 1.7
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, mix("#FFFFFF", col, 0.10), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22), paint(col, a, stroke=4))
    m(c, s, cx, cy, size, a, col)
    if sub:
        text(c, sub, cx, cy + h / 2 + 34, 24, "black", col, a)


def caixa_def(c, x, y, w, h, titulo, linhas_, a, col=BLUE, size=30):
    """caixa de definição (azul por padrão): título + linhas"""
    if a <= 0:
        return
    K.boxed(c, x, y, w, h, col, a, 0.07)
    text(c, titulo, x + w / 2, y + 46, 26, "black", col, a, tracking=2)
    for k, s in enumerate(linhas_):
        text(c, s, x + w / 2, y + 96 + k * (size + 14), size, "bold", INK, a)


def barra_prazo(c, x, y, w, partes, a, h=56, rot_total=None, prog_=1.0):
    """barra do prazo quebrada em partes: partes = [(n, rótulo, cor)]"""
    if a <= 0:
        return
    tot = sum(p[0] for p in partes)
    xx = x
    for k, (n, s, col) in enumerate(partes):
        u = clamp(prog_ * len(partes) - k)
        if u <= 0:
            break
        ww = w * n / tot
        rrect(c, xx + 4, y, (ww - 8) * u, h, 14, mix("#FFFFFF", col, 0.22), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx + 4, y, (ww - 8) * u, h), 14, 14), paint(col, a, stroke=3))
        if u >= 1:
            text_mid(c, s, xx + ww / 2, y + h / 2, 28, "black", col, a)
        xx += ww
    if rot_total:
        text(c, rot_total, x + w / 2, y - 22, 26, "black", AMBER, a)


def regua(c, x0, y0, n_on, a, meta=1.6, vals=(1.1, 1.21, 1.331, 1.4641, 1.61051), lbl=("1,1", "1,21", "1,33", "1,46", "1,61"),
          w=760, h=420, alfas=None):
    """régua da tentativa: barras 1,1¹ … 1,1⁵ (altura ∝ fator) e a linha da meta"""
    if a <= 0:
        return
    vmin, vmax = 1.0, 1.75
    base = y0 + h
    Y = lambda v: base - h * (v - vmin) / (vmax - vmin)
    line(c, x0 - 20, base, x0 + w + 20, base, INK2, a, 3)
    ym = Y(meta)
    line(c, x0 - 20, ym, x0 + w + 20, ym, AMBER, a, 4, dash=[16, 10])
    text(c, f"META: {str(meta).replace('.', ',')} × o capital", x0 - 20, ym - 16, 26, "black", AMBER, a, align="left")
    bw = w / len(vals)
    for k, v in enumerate(vals):
        ak = a * (alfas[k] if alfas else (1.0 if k < n_on else 0.0))
        if ak <= 0:
            continue
        ok = v >= meta
        col = GREEN if ok else (BLUE if k < len(vals) - 1 else BLUE)
        xx = x0 + k * bw + bw * 0.18
        rrect(c, xx, Y(v), bw * 0.64, base - Y(v), 12, mix("#FFFFFF", col, 0.30), ak)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, Y(v), bw * 0.64, base - Y(v)), 12, 12),
                    paint(col, ak, stroke=3))
        m(c, f"1,1^{k + 1}", xx + bw * 0.32, base + 40, 32, ak, INK2)
        text(c, lbl[k], xx + bw * 0.32, Y(v) - 16, 30, "black", GREEN if ok else INK, ak)
        if k == 3 and ak > 0:
            pill(c, "ainda não", xx + bw * 0.32, Y(v) + 40, RED, size=20, a=ak, anchor="center")
        if ok:
            pill(c, "passou!", xx + bw * 0.32, Y(v) + 40, GREEN, size=20, a=ak, anchor="center")


def radar(c, cx, cy, r, a, t, alvo=None):
    """radar verde da regra do 72: círculos, varredura girando e um ponto no alvo"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(mix("#FFFFFF", GREEN, 0.10), a))
    for k in (1, 2, 3):
        c.drawCircle(cx, cy, r * k / 3, paint(GREEN, a * 0.6, stroke=3))
    line(c, cx - r, cy, cx + r, cy, GREEN, a * 0.4, 2)
    line(c, cx, cy - r, cx, cy + r, GREEN, a * 0.4, 2)
    ang = (t * 140) % 360
    x1 = cx + r * math.cos(math.radians(ang))
    y1 = cy + r * math.sin(math.radians(ang))
    line(c, cx, cy, x1, y1, GREEN, a, 5)
    if alvo:
        ax, ay, s = alvo
        pulse = 0.5 + 0.5 * math.sin(t * 6)
        c.drawCircle(cx + ax, cy + ay, 14 + 6 * pulse, paint(GREEN, a * 0.35))
        c.drawCircle(cx + ax, cy + ay, 10, paint(GREEN, a))
        text(c, s, cx + ax, cy + ay - 26, 26, "black", GREEN, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "JUROS COMPOSTOS SEM CALCULADORA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 460, 240, 1000, 150, 24, "#FFFFFF", aa, shadow=True)
        text(c, "O ENUNCIADO DIZ", 960, 280, 22, "black", BLUE, aa, tracking=2)
        m(c, "1,05^6 ≈ 1,34", 960, 340, 64, aa, INK)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        pill(c, "A PERGUNTA: 12 MESES", 960, 440, AMBER, size=30, a=ab, anchor="center")
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        rrect(c, 300, 510, 560, 210, 24, mix("#FFFFFF", RED, 0.07), ac)
        m(c, "2 · 1,34", 580, 590, 60, ac, RED)
        check_icon(c, 580, 670, 26, ac, RED, "x")
        text(c, "ERRA", 640, 680, 32, "black", RED, ac, align="left")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 1060, 510, 560, 210, 24, mix("#FFFFFF", GREEN, 0.07), ad)
        m(c, "1,34^2", 1340, 590, 60, ad, GREEN)
        check_icon(c, 1300, 670, 26, ad, GREEN)
        text(c, "ACERTA", 1340, 680, 32, "black", GREEN, ad, align="left")
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        text(c, "pensar em JUROS SIMPLES", 580, 780, 30, "black", RED, ae)
        text(c, "pensar em JUROS COMPOSTOS", 1340, 780, 30, "black", GREEN, ae)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "usar as POTÊNCIAS que o enunciado der", "passo a passo · quebrar · combinar"),
            ("02.b", "descobrir o TEMPO", "por tentativa ou por logaritmo"),
            ("02.c", "ESTIMAR com a regra do 72", "o radar das alternativas")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "ANTES DE COMEÇAR", GREEN)
    cols = [(380, "03.a", "DO EPISÓDIO 1", PURPLE), (960, "03.b", "POTÊNCIA", BLUE), (1540, "03.c", "DA POTENCIAÇÃO", PURPLE)]
    for cx, cue, tit, col in cols:
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        rrect(c, cx - 270, 260 + d, 540, 470, 24, "#FFFFFF", a, shadow=True)
        rrect(c, cx - 270, 260 + d, 540, 12, 6, col, a)
        text(c, tit, cx, 320 + d, 26, "black", col, a, tracking=2)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        m(c, "M = C · (1+i)^t", 380, 450, 52, aa, None, cores={0: RED, 1: INK, 2: BLUE, 3: INK, 4: PURPLE})
        pill(c, "fator = 1 + i", 380, 580, PURPLE, size=28, a=ep(t, C["03.a"] + 3.0, 0.4), anchor="center")
        text(c, "multiplica o saldo", 380, 650, 26, "bold", INK2, ep(t, C["03.a"] + 3.0, 0.4))
        text(c, "a cada período", 380, 686, 26, "bold", INK2, ep(t, C["03.a"] + 3.0, 0.4))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        m(c, "1,1^3", 960, 430, 64, ab, BLUE)
        m(c, "= 1,1 · 1,1 · 1,1", 960, 530, 40, ab, INK)
        pill(c, "expoente = quantas vezes", 960, 640, BLUE, size=26, a=ep(t, C["03.b"] + 1.5, 0.4), anchor="center")
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        m(c, "a^{m+n} = a^m · a^n", 1540, 440, 46, ac, INK)
        m(c, "(a^n)^2 = a^{2n}", 1540, 580, 46, ep(t, C["03.c"] + 3.5, 0.4), INK)


# ======================================================================
# concreto
# ======================================================================

def cartao(c, x, y, a):
    rrect(c, x, y, 300, 190, 22, PURPLE, a, shadow=True)
    rrect(c, x + 30, y + 50, 56, 40, 8, "#F2C94C", a)
    text(c, "•••• 2000", x + 30, y + 150, 26, "black", "#FFFFFF", a, align="left")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS PERGUNTAS DA VIDA REAL", "E NENHUMA CALCULADORA", BLUE)
    card(c, *CARD_R)
    aa, d = rise(t, C["04.a"])
    if aa > 0:
        cartao(c, 260, 290 + d, aa)
        linha(c, [("R$ 2.000,00", BLUE), ("  a  ", INK2), ("5% ao mês", PURPLE)], 830, 330 + d, 42, aa, align="left")
        linha(c, [("1 ano sem pagar = ", INK), ("?", RED)], 830, 420 + d, 46, ep(t, C["04.a"] + 3.0, 0.4), align="left")
    ab, d = rise(t, C["04.b"])
    if ab > 0:
        c.drawCircle(410, 640 + d, 90, paint(mix("#FFFFFF", GREEN, 0.18), ab))
        text_mid(c, "R$", 410, 640 + d, 64, "black", GREEN, ab)
        linha(c, [("o dinheiro DOBRA em ", INK), ("quanto tempo?", AMBER)], 830, 640 + d, 46, ab, align="left")
    ac = ep(t, C["04.c"], 0.5)
    if ac > 0:
        m(c, "1,05^{12} = ?", 1500, 520, 54, ac, RED)
        selo(c, 1500, 760, ac, "SEM CALCULADORA", RED, -4, 34)


# ======================================================================
# bloco a — passo a passo e a décima parte
# ======================================================================

POT = [("1,1^1", "1,1"), ("1,1^2", "1,21"), ("1,1^3", "1,331"), ("1,1^4", "1,4641"), ("1,1^5", "1,61051")]


def b_passo(c, t, C, B):
    head_seq(c, t, C, [("05", "TÉCNICA 1", "MULTIPLICAR PASSO A PASSO", PURPLE),
                       ("06", "ATALHO", "× 1,1 = SOMAR A DÉCIMA PARTE", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            pill(c, "10% → fator 1,1", 960, 245, PURPLE, size=30, a=aa, anchor="center")
        tins = [C["05.a"] + 0.6, C["05.b"], C["05.b"] + 3.0, C["05.c"], C["05.c"] + 3.6]
        for k, (p_, v) in enumerate(POT):
            a, d = rise(t, tins[k])
            if a <= 0:
                continue
            y = 330 + k * 92 + d
            m(c, p_, 760, y, 50, a, PURPLE, align="right")
            text_mid(c, "=", 820, y, 50, "black", GRAY, a)
            m(c, v, 880, y, 50, a, INK, align="left")
            if k:
                pill(c, "× 1,1", 1130, y - 46, GREEN, size=22, a=a, anchor="left")
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            pill(c, "bom para expoentes PEQUENOS", 960, 800, BLUE, size=28, a=ad, anchor="center")
        return
    aa = ep(t, C["06.a"], 0.4)
    K.boxed(c, 260, 230, 1400, 580, GREEN, aa, 0.06)
    if aa > 0:
        regra(c, "× 1,1  =  o número + a sua DÉCIMA PARTE", 960, 310, aa, 36, GREEN)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        x = 1100
        rows = [("", "1,331", INK, 0.0), ("+", "0,1331", GREEN, 1.6), ("", "1,4641", PURPLE, 3.6)]
        for k, (op, v, col, dt) in enumerate(rows):
            a = ep(t, C["06.b"] + dt, 0.4)
            y = 440 + k * 100 + (20 if k == 2 else 0)
            text(c, op, x - 330, y, 60, "black", GREEN, a, align="left")
            text(c, v, x, y, 60, "black", col, a, align="right")
        line(c, x - 340, 600, x + 10, 600, INK, ep(t, C["06.b"] + 3.2, 0.3), 4)
        text(c, "a décima parte", x + 40, 525, 26, "bold", GREEN, ep(t, C["06.b"] + 1.6, 0.4), align="left")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        pill(c, "ande com a vírgula 1 casa e some", 960, 760, GREEN, size=30, a=acc, anchor="center")


# ======================================================================
# blocos b e c — quebrar e combinar
# ======================================================================

def b_quebrar(c, t, C, B):
    head(c, t, B["start"], "TÉCNICA 2", "QUEBRAR O EXPOENTE", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    caixa_def(c, 230, 220, 640, 150, "QUEBRAR O EXPOENTE", ["prazo = soma de prazos IGUAIS"], aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        barra_prazo(c, 1000, 290, 660, [(10, "10 meses", BLUE), (10, "10 meses", BLUE)], ab,
                    rot_total="20 meses", prog_=ep(t, C["07.b"], 1.2))
        K.boxed(c, 560, 410, 800, 120, PURPLE, ab, 0.08)
        m(c, "(1+i)^{2n} = ((1+i)^n)^2", 960, 470, 50, ab, PURPLE)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        pill(c, "DADO NO ENUNCIADO", 520, 600, BLUE, size=22, a=acc, anchor="center")
        m(c, "1,03^{10} ≈ 1,34", 520, 680, 50, acc, INK)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        m(c, "1,03^{20} ≈ 1,34^2 ≈ 1,80", 1330, 660, 50, ad, None,
          cores={0: INK, 1: INK, 2: INK, 3: INK, 4: GREEN})
        text(c, "exato: 1,34² = 1,7956", 1330, 760, 26, "bold", GRAY, ep(t, C["07.d"] + 2.4, 0.4))


def b_combinar(c, t, C, B):
    head_seq(c, t, C, [("08", "TÉCNICA 3", "COMBINAR POTÊNCIAS", PURPLE),
                       ("09", "ATALHO", "AS 3 TÉCNICAS NA PROVA", GREEN)])
    card(c, *CARD_R)
    if which(t, C, ["08", "09"]) == "09":
        a0 = ep(t, C["09"], 0.4)
        K.boxed(c, 300, 230, 1320, 560, GREEN, a0, 0.06)
        text(c, "ATALHO", 960, 285, 26, "black", GREEN, a0, tracking=3)
        steps = [("09.a", "1", "ache as POTÊNCIAS DADAS", "1,05⁶ ≈ 1,34"),
                 ("09.b", "2", "prazo = SOMA dos expoentes", "12 = 6 + 6"),
                 ("09.c", "3", "multiplique; REAIS só no fim", "2.000 · 1,7956")]
        for k, (cue, n, s, ex) in enumerate(steps):
            a, d = rise(t, C[cue])
            y = 400 + k * 130 + d
            badge_num(c, n, 400, y - 12, a, 34, bg=GREEN)
            text(c, s, 470, y, 44, "black", INK, a, align="left")
            ftext(c, ex, 1560, y, 36, "black", GREEN, a, align="right")
        return
    aa = ep(t, C["08.a"], 0.5)
    caixa_def(c, 230, 220, 700, 150, "COMBINAR POTÊNCIAS", ["multiplicar prazos que SOMAM o pedido"], aa)
    if aa > 0:
        K.boxed(c, 1020, 240, 660, 110, PURPLE, aa, 0.08)
        m(c, "(1+i)^{a+b} = (1+i)^a · (1+i)^b", 1350, 295, 40, aa, PURPLE)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        barra_prazo(c, 360, 470, 1200, [(5, "5 anos", BLUE), (2, "2 anos", GREEN)], ab, rot_total="7 anos a 10%",
                    prog_=ep(t, C["08.b"], 1.0))
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        m(c, "1,1^7 = 1,1^5 · 1,1^2 ≈ 1,61 · 1,21", 960, 640, 52, acc, INK)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        m(c, "≈ 1,95", 960, 750, 64, ad, GREEN)


# ======================================================================
# bloco d — dobrar o tempo
# ======================================================================

def b_dobrar(c, t, C, B):
    head(c, t, B["start"], "A PEGADINHA DO GANCHO", "DOBRAR O TEMPO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        barra_prazo(c, 560, 250, 800, [(6, "6 meses", BLUE), (6, "6 meses", BLUE)], aa, h=50,
                    prog_=ep(t, C["10.a"], 1.0))
        ficha(c, "1,34", 760, 380, aa, PURPLE, 46)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        # cópia que desliza do primeiro semestre para o segundo
        u = ease_out(clamp((t - C["10.b"]) / 1.2))
        ficha(c, "1,34", 760 + 400 * u, 380, ab, PURPLE, 46)
        text_mid(c, "×", 960, 380, 52, "black", PURPLE, ab * u)
        rrect(c, 240, 470, 660, 300, 24, mix("#FFFFFF", GREEN, 0.07), ab)
        text(c, "COMPOSTOS: o fator × ele mesmo", 570, 520, 26, "black", GREEN, ab)
        m(c, "1,34 · 1,34 = 1,34^2", 570, 610, 46, ab, INK)
        m(c, "≈ 1,80", 570, 700, 56, ep(t, C["10.b"] + 3.5, 0.4), GREEN)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 470, 660, 300, 24, mix("#FFFFFF", RED, 0.06), acc)
        m(c, "1,34 + 1,34 = 2,68", 1350, 560, 46, acc, RED)
        strike(c, 1150, 560, 1550, 560, ep(t, C["10.c"] + 1.4, 0.4), RED)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        m(c, "1 + 0,34 + 0,34 = 1,68", 1350, 680, 42, ad, RED)
        strike(c, 1150, 680, 1550, 680, ep(t, C["10.d"] + 0.8, 0.4), RED)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        regra(c, "dobrar o TEMPO = elevar o FATOR AO QUADRADO", 960, 805, ae, 34)


# ======================================================================
# bloco e — tentativa
# ======================================================================

def b_tentativa(c, t, C, B):
    head(c, t, B["start"], "QUANDO A PERGUNTA É O TEMPO", "1º CAMINHO: TENTATIVA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        m(c, "1,1^t ≥ 1,6", 400, 300, 64, aa, None, cores={0: INK, 1: INK, 2: AMBER})
        pill(c, "t está no EXPOENTE", 400, 390, AMBER, size=26, a=aa, anchor="center")
    ab = ep(t, C["11.b"], 0.5)
    caixa_def(c, 210, 470, 380, 230, "TENTATIVA", ["testar os expoentes", "até passar da meta"], ab, BLUE, 28)
    acc = ep(t, C["11.c"], 0.5)
    t0 = C["11.d"]
    alfas = [ep(t, t0 + dt, 0.3) for dt in (0.0, 1.2, 2.6, 4.0)] + [ep(t, C["11.e"], 0.3)]
    regua(c, 820, 290, 0, acc, alfas=alfas)
    ae = ep(t, C["11.e"] + 1.6, 0.4)
    if ae > 0:
        selo(c, 400, 790, ae, "5 MESES", GREEN, -4, 40)


# ======================================================================
# bloco f — logaritmo dado
# ======================================================================

def b_log(c, t, C, B):
    head_seq(c, t, C, [("12", "2º CAMINHO", "O LOGARITMO DADO", PURPLE), ("13", "ATALHO", "O TEMPO PELO LOG EM 3 PASSOS", GREEN)])
    card(c, *CARD_R)
    if which(t, C, ["12", "13"]) == "13":
        a0 = ep(t, C["13"], 0.4)
        K.boxed(c, 300, 230, 1320, 560, GREEN, a0, 0.06)
        text(c, "ATALHO", 960, 285, 26, "black", GREEN, a0, tracking=3)
        steps = [("13.a", "1", "M ÷ C", "dobrar = 2 · triplicar = 3"), ("13.b", "2", "o LOG desse número", "log 2 · log 3"),
                 ("13.c", "3", "÷ LOG DO FATOR", "log(1 + i), nunca a taxa")]
        for k, (cue, n, s, ex) in enumerate(steps):
            a, d = rise(t, C[cue])
            y = 400 + k * 130 + d
            badge_num(c, n, 400, y - 12, a, 34, bg=GREEN)
            text(c, s, 470, y, 46, "black", INK, a, align="left")
            text(c, ex, 1560, y, 34, "black", GREEN if k < 2 else RED, a, align="right")
        return
    aa = ep(t, C["12.a"], 0.5)
    caixa_def(c, 220, 220, 600, 250, "LOGARITMO (DADO)", ["um número que", "o enunciado ENTREGA"], aa, BLUE, 32)
    if aa > 0:
        pill(c, "como numa tabela", 520, 430, BLUE, size=22, a=aa, anchor="center")
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        K.boxed(c, 900, 220, 780, 250, PURPLE, ab, 0.08)
        text(c, "TEMPO EM JUROS COMPOSTOS", 1290, 268, 24, "black", PURPLE, ab, tracking=2)
        m(c, "t = log(M/C)/log(1+i)", 1290, 370, 52, ab, PURPLE)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        pill(c, "DOBRAR A 10% AO ANO", 520, 540, AMBER, size=24, a=acc, anchor="center")
        m(c, "M/C = 2", 520, 640, 50, acc, INK)
        linha(c, [("t = log 2 ÷ log 1,1", INK)], 1290, 570, 40, acc)
        linha(c, [("= 0,301 ÷ 0,041", INK)], 1290, 640, 40, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        linha(c, [("≈ ", INK), ("7,3 anos", GREEN)], 1290, 720, 56, ad)
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        pill(c, "por que o log \"derruba\" o expoente? → série de Logaritmos", 960, 812, PURPLE, size=24, a=ae,
             anchor="center")


# ======================================================================
# bloco g — regra do 72
# ======================================================================

def b_regra72(c, t, C, B):
    head(c, t, B["start"], "3º CAMINHO: ESTIMAR", "A REGRA DO 72", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    caixa_def(c, 210, 220, 640, 170, "ESTIMAR", ["achar um valor APROXIMADO"], aa, BLUE, 32)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        K.boxed(c, 210, 420, 640, 130, GREEN, ab, 0.10)
        text(c, "TEMPO PARA DOBRAR", 530, 462, 22, "black", GREEN, ab, tracking=2)
        linha(c, [("≈ 72 ÷ ", INK), ("taxa (%)", PURPLE)], 530, 510, 46, ab)
    acc = ep(t, C["14.c"], 0.5)
    rows = [("10%", "≈ 7,2"), ("6%", "≈ 12"), ("8%", "≈ 9")]
    for k, (tx, tt) in enumerate(rows):
        a = ep(t, C["14.c"] + k * 1.4, 0.4) * (acc > 0)
        y = 610 + k * 70
        text(c, tx, 330, y, 36, "black", PURPLE, a, align="left")
        text(c, "→", 460, y, 36, "black", GRAY, a)
        text(c, f"{tt} períodos", 520, y, 36, "black", INK, a, align="left")
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        radar(c, 1300, 480, 240, ad, t, (-80, -60, "≈ 7"))
        text(c, "≈ 25?", 1300 + 170, 480 + 170, 28, "black", GRAY, ad)
        text(c, "o RADAR das alternativas", 1300, 790, 30, "black", GREEN, ad)
    ae = ep(t, C["14.e"], 0.5)
    if ae > 0:
        pill(c, "boa entre 2% e 20%", 1300, 210, GREEN, size=24, a=ae, anchor="center")


# ======================================================================
# bloco h — triplicar
# ======================================================================

def b_triplicar(c, t, C, B):
    head(c, t, B["start"], "E PARA TRIPLICAR?", "CADA PERGUNTA TEM O SEU LOG", AMBER)
    card(c, *CARD_R)
    cards = [("15.a", "DOBRAR", "M/C = 2 → log 2", BLUE, 0.0), ("15.a", "TRIPLICAR", "M/C = 3 → log 3", PURPLE, 2.0),
             ("15.c", "QUADRUPLICAR", "dobrar 2 vezes", GREEN, 0.0)]
    for k, (cue, tit, s, col, dt) in enumerate(cards):
        a, d = rise(t, C[cue] + dt)
        if a <= 0:
            continue
        x = 250 + k * 480
        rrect(c, x, 240 + d, 440, 180, 22, mix("#FFFFFF", col, 0.08), a)
        text(c, tit, x + 220, 290 + d, 30, "black", col, a, tracking=2)
        text(c, s, x + 220, 370 + d, 32, "black", INK, a)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        text(c, "A 10% AO ANO", 960, 490, 24, "black", AMBER, ab, tracking=2)
        linha(c, [("triplicar: ", PURPLE), ("0,477 ÷ 0,041 ≈ ", INK), ("11,6 anos", PURPLE)], 960, 570, 44, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        linha(c, [("quadruplicar: ", GREEN), ("7,3 + 7,3 ≈ ", INK), ("14,6 anos", GREEN)], 960, 680, 44, acc)
        pill(c, "o dobro do tempo de dobrar = QUADRUPLICAR", 960, 790, AMBER, size=26, a=ep(t, C["15.c"] + 2.0, 0.4),
             anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "QUEBRAR E ESTIMAR", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        badge_num(c, "1", 260, 300, aa, 30, bg=PURPLE)
        m(c, "1,02^{10} ≈ 1,22", 320, 300, 46, aa, INK, align="left")
        linha(c, [("fator de ", INK), ("20 meses", AMBER), (" a 2% a.m. = ?", INK)], 320, 390, 38, aa, align="left")
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        badge_num(c, "2", 260, 520, ab, 30, bg=GREEN)
        linha(c, [("regra do 72: ", GREEN), ("dobra a ", INK), ("9% a.a.", PURPLE), (" em ?", INK)], 320, 520, 38, ab,
              align="left")
    pause_timer(c, t, C["16.end"] - 1.9, 1460, 420)
    if t < C["17"]:
        return
    a1 = ep(t, C["17.a"], 0.4)
    if a1 > 0:
        m(c, "1,02^{20} = (1,02^{10})^2 ≈ 1,22^2", 1150, 300, 40, a1, PURPLE)
    a2 = ep(t, C["17.b"], 0.4)
    if a2 > 0:
        m(c, "= 1,4884 ≈ 1,49", 1150, 390, 46, a2, GREEN)
        linha(c, [("2 · 1,22 = 2,44", RED)], 1150, 460, 30, a2)
        strike(c, 1040, 460, 1260, 460, ep(t, C["17.b"] + 2.4, 0.3), RED)
    a3 = ep(t, C["17.c"], 0.4)
    if a3 > 0:
        linha(c, [("72 ÷ 9 = ", INK), ("8 anos", GREEN)], 1150, 560, 46, a3)
        radar(c, 1150, 720, 90, a3, t)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Dobrar o tempo é elevar o fator ao quadrado.",
          "O tempo está no expoente: tentativa, logaritmo ou regra do 72.",
          "Divida pelo log do fator, nunca pela taxa."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 62)


ERROS = [("Tempo dobrou → dobrar o fator: 2 · 1,34 = 2,68", "em juros simples, o dobro do tempo dava o dobro dos juros",
          "em compostos, o fator vai AO QUADRADO: 1,34² ≈ 1,80"),
         ("Somar as taxas: 34% + 34% = 68%", "cada semestre rende mesmo 34%",
          "o 2º semestre rende sobre um saldo MAIOR: somar é pensar em simples"),
         ("log 2 ÷ taxa: 0,301 ÷ 0,1 ≈ 3 anos", "a taxa é o número que mais aparece",
          "÷ log(1 + i) = 0,041 → 7,3 anos · o radar já dizia: perto de 7"),
         ("Triplicar = 1,5 vez (ou o dobro) do tempo de dobrar", "3 está entre 2 e 4",
          "triplicar usa LOG 3 · o dobro do tempo de dobrar é QUADRUPLICAR")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21", "22"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            ftext(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS6 = [("A", "R$ 2.680,00", "só o fator de 6 meses", RED), ("B", "R$ 3.200,00", "juros simples: 60%", RED),
         ("C", "R$ 3.360,00", "somou os semestres: 68%", RED), ("D", "R$ 3.590,00", "", GREEN),
         ("E", "R$ 5.360,00", "fator × 2", RED)]


def b_q6(c, t, C, B):
    head_seq(c, t, C, [("23", "QUESTÃO 6 · EU FAÇO", "POTÊNCIA DADA NO ENUNCIADO", BLUE),
                       ("24", "RESOLVENDO", "QUEBRAR O EXPOENTE", BLUE), ("25", "AS ERRADAS", "CADA UMA É UM ERRO CLÁSSICO", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    yend = _enunciado(c, [("Uma dívida de R$ 2.000,00 no cartão de crédito cresce a juros compostos de 5% ao mês. "
                           "Considere 1,05⁶ ≈ 1,34. Se nada for pago, após 12 meses a dívida será de, aproximadamente,",
                           INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["24"], 0.3)),
         align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS6, 1000, 260, 680, 38, C["24.ok"], "D", cues_in, cues_x, gap=40)
    if t >= C["24"]:
        y0 = yend + 10
        _painel(c, y0, ep(t, C["24"], 0.4))
        a1 = ep(t, C["24.a"], 0.4)
        m(c, "1,05^{12} = (1,05^6)^2 ≈ 1,34^2", 540, y0 + 60, 36, a1, PURPLE)
        m(c, "= 1,7956", 540, y0 + 130, 40, ep(t, C["24.a"] + 2.0, 0.4), GREEN)
        a2 = ep(t, C["24.b"], 0.4)
        linha(c, [("2.000 · 1,7956 ≈ ", INK), ("R$ 3.591,20", GREEN)], 540, y0 + 210, 32, a2)
        conferido(c, "radar: 72 ÷ 5 ≈ 14 meses p/ dobrar", 200, y0 + 290, ep(t, C["24.c"], 0.4), True, 24)


ALTS7 = [("A", "4", "parou em 1,46", RED), ("B", "5", "", GREEN), ("C", "6", "juros simples: 1.000 + 100 · 6", RED),
         ("D", "7", "um mês a mais", RED), ("E", "16", "1.600 ÷ 100", RED)]


def b_q7(c, t, C, B):
    head_seq(c, t, C, [("26", "QUESTÃO 7 · NÓS FAZEMOS", "TEMPO POR TENTATIVA", GREEN),
                       ("27", "JUNTOS", "A RÉGUA DA TENTATIVA", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    yend = _enunciado(c, [("R$ 1.000,00 foram aplicados a juros compostos de 10% ao mês. Considere 1,1⁴ ≈ 1,46 e "
                           "1,1⁵ ≈ 1,61. O número mínimo de meses completos para que o saldo atinja pelo menos "
                           "R$ 1.600,00 é", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 260, 680, 38, C["27.ok"], "B", cues_in, cues_x, gap=40)
    if t >= C["27"]:
        y0 = yend + 10
        _painel(c, y0, ep(t, C["27"], 0.4))
        linha(c, [("meta: 1.600 ÷ 1.000 = ", INK), ("1,6", AMBER)], 540, y0 + 50, 30, ep(t, C["27"], 0.4))
        a1 = ep(t, C["27.a"], 0.4)
        linha(c, [("4 meses: ", INK), ("R$ 1.460,00", RED), ("  não basta", RED)], 540, y0 + 130, 30, a1)
        a2 = ep(t, C["27.b"], 0.4)
        linha(c, [("5 meses: ", INK), ("R$ 1.610,00", GREEN), ("  passou", GREEN)], 540, y0 + 200, 30, a2)


ALTS2 = [("A", "3,75 anos", "tempo para DOBRAR", RED), ("B", "6 anos", "", GREEN),
         ("C", "7,5 anos", "dobro de dobrar = quadruplicar", RED), ("D", "10 anos", "triplicar em simples", RED),
         ("E", "15 anos", "J = 3C em simples", RED)]


def b_q2(c, t, C, B):
    head_seq(c, t, C, [("28", "QUESTÃO 2 · VOCÊ FAZ", "TEMPO PARA TRIPLICAR", GREEN),
                       ("29", "CONFERINDO", "O LOG CERTO", GREEN), ("30", "AS ERRADAS", "CADA UMA É UM ERRO CLÁSSICO", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, [("Um fundo rende juros compostos de 20% ao ano. Para estimar em quanto tempo um capital "
                           "aplicado nesse fundo triplica, um analista usou log 2 ≈ 0,30, log 3 ≈ 0,48 e "
                           "log 1,2 ≈ 0,08. O tempo obtido foi de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["29"], 0.3)),
         align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 260, 680, 38, C["29.ok"], "B", cues_in, cues_x, gap=40)
    if t < C["29"]:
        pause_timer(c, t, C["28.end"] - 1.9, 540, 700)
        return
    y0 = yend + 10
    _painel(c, y0, ep(t, C["29"], 0.4))
    a1 = ep(t, C["29.a"], 0.4)
    linha(c, [("triplicar: M/C = 3 → ", INK), ("log 3", PURPLE)], 540, y0 + 45, 28, a1)
    a2 = ep(t, C["29.b"], 0.4)
    if a2 > 0:
        m(c, "t = 0,48/0,08 = 6", 540, y0 + 130, 40, a2, GREEN)
    conferido(c, "1,2⁶ ≈ 2,99 ≈ 3", 200, y0 + 220, ep(t, C["29.c"], 0.4), True, 26)
    conferido(c, "radar: dobra ≈ 3,6 · 4× ≈ 7,2", 200, y0 + 275, ep(t, C["29.d"], 0.4), True, 24)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TRAZENDO VALORES PARA HOJE", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    if aa > 0:
        linha(c, [("HOJE: ", INK), ("?", RED), ("   →   ", GRAY), ("R$ 12.100,00", GREEN), ("  em 2 anos", AMBER)], W / 2,
              320, 56, aa)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        linha(c, [("quanto aplicar ", INK), ("HOJE?", RED)], W / 2, 440, 50, ab)
    acc = ep(t, C["32.c"], 0.5)
    if acc > 0:
        linha(c, [("12.100 − 10% − 10%", RED)], W / 2, 560, 48, acc)
        strike(c, W / 2 - 240, 560, W / 2 + 240, 560, ep(t, C["32.c"] + 1.2, 0.4), RED)
        check_icon(c, W / 2 + 300, 560, 26, ep(t, C["32.c"] + 1.2, 0.4), RED, "x")
    pill(c, "ep. 4 · trazendo valores para hoje", W / 2, 720, PURPLE, size=30, a=ep(t, C["32.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Você já conhecia a regra do 72?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, passo=b_passo, quebrar=b_quebrar,
              combinar=b_combinar, dobrar=b_dobrar, tentativa=b_tentativa, log=b_log, regra72=b_regra72,
              triplicar=b_triplicar, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q6=b_q6, q7=b_q7, q2=b_q2,
              ponte=b_ponte, cta=b_cta)
