"""Visual — Juros Compostos, Episódio 2: simples × compostos (reta e curva, PA e PG) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: Graf (eixos tempo × montante), reta_s() (simples, AZUL), curva_c() (compostos, ROXO), lupa() (zoom
entre t = 0 e t = 1), escadas() (degraus iguais × degraus 10% maiores), pilhas() (notas que dobram), fator_par() (os dois
fatores lado a lado), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
No gráfico: reta (simples) = AZUL e curva (compostos) = ROXO, como pede o prompt.
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
ARQUIVO_FINAL = "enem_matematica_juros_compostos_ep2_simples_compostos.mp4"
CARD_R = K.CARD_R

SIMP = BLUE      # reta / juros simples
COMP = PURPLE    # curva / juros compostos


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
    """eixos: horizontal = tempo, vertical = montante. (x, y, w, h) = área útil."""

    def __init__(s, x, y, w, h, t0, t1, v0, v1):
        s.x, s.y, s.w, s.h, s.t0, s.t1, s.v0, s.v1 = x, y, w, h, t0, t1, v0, v1

    def P(s, t, v):
        return (s.x + s.w * (t - s.t0) / (s.t1 - s.t0),
                s.y + s.h - s.h * (v - s.v0) / (s.v1 - s.v0))

    def eixos(s, c, a, xticks=(), yticks=(), size=22, xlab="tempo (anos)", ylab="montante (R$)", corte=True,
              xfmt=str):
        if a <= 0:
            return
        x0, y0 = s.x, s.y + s.h
        for v in yticks:
            _, yy = s.P(s.t0, v)
            line(c, x0, yy, x0 + s.w, yy, "#ECECE8", a, 2)
        arrow(c, x0, y0, x0 + s.w + 40, y0, INK2, a, 4, 14)
        arrow(c, x0, y0, x0, s.y - 40, INK2, a, 4, 14)
        if corte:
            zz = skia.Path(); zz.moveTo(x0 - 12, y0 - 18); zz.lineTo(x0 + 12, y0 - 26); zz.moveTo(x0 - 12, y0 - 30)
            zz.lineTo(x0 + 12, y0 - 38)
            c.drawPath(zz, paint(INK2, a, stroke=3))
        for tk in xticks:
            xx, _ = s.P(tk, s.v0)
            line(c, xx, y0 - 6, xx, y0 + 6, INK2, a, 2)
            text(c, xfmt(tk), xx, y0 + 34, size, "bold", GRAY, a)
        for v in yticks:
            _, yy = s.P(s.t0, v)
            line(c, x0 - 6, yy, x0 + 6, yy, INK2, a, 2)
            text(c, brl(v), x0 - 14, yy + size * 0.36, size, "bold", GRAY, a, align="right")
        text(c, xlab, x0 + s.w + 30, y0 + 66, size, "black", AMBER, a, align="right")
        text(c, ylab, x0 + 10, s.y - 54, size, "black", INK2, a, align="left")


def _curva(c, g, f, ta, tb, a, prog_=1.0, col=COMP, w=6, n=80):
    if a <= 0 or prog_ <= 0:
        return
    tb2 = ta + (tb - ta) * clamp(prog_)
    p = skia.Path()
    for k in range(n + 1):
        tt = ta + (tb2 - ta) * k / n
        x, y = g.P(tt, f(tt))
        p.moveTo(x, y) if k == 0 else p.lineTo(x, y)
    c.drawPath(p, paint(col, a, stroke=w))


def reta_s(c, g, C0, i, ta, tb, a, prog_=1.0, w=6):
    _curva(c, g, lambda tt: C0 * (1 + i * tt), ta, tb, a, prog_, SIMP, w, 2)


def curva_c(c, g, C0, i, ta, tb, a, prog_=1.0, w=6):
    _curva(c, g, lambda tt: C0 * (1 + i) ** tt, ta, tb, a, prog_, COMP, w)


def ponto(c, g, t, v, a, col=RED, r=11, rot=None, dx=18, dy=-18, size=24, align="left"):
    if a <= 0:
        return
    x, y = g.P(t, v)
    c.drawCircle(x, y, r + 5, paint("#FFFFFF", a))
    c.drawCircle(x, y, r, paint(col, a))
    if rot:
        fmid(c, rot, x + dx, y + dy, size, "black", col, a, align=align)


def legenda(c, x, y, a, size=26):
    if a <= 0:
        return
    line(c, x, y, x + 50, y, SIMP, a, 6)
    text(c, "simples (reta)", x + 64, y + size * 0.36, size, "black", SIMP, a, align="left")
    line(c, x, y + 46, x + 50, y + 46, COMP, a, 6)
    text(c, "compostos (curva)", x + 64, y + 46 + size * 0.36, size, "black", COMP, a, align="left")


def escadas(c, x, y, a, prog_s=1.0, prog_c=1.0, n=5, passo=110, d0=56, size=22):
    """duas escadas lado a lado: degraus iguais (simples) × cada degrau 10% mais alto que o anterior (compostos)"""
    for k_e, (col, prog_, fator, x0) in enumerate(((SIMP, prog_s, 1.0, x), (COMP, prog_c, 1.1, x + 640))):
        if a <= 0 or prog_ <= 0:
            continue
        yy = y
        hh = d0
        for k in range(n):
            u = clamp(prog_ * n - k)
            if u <= 0:
                break
            xa = x0 + k * passo
            rrect(c, xa, yy - hh, passo - 8, hh, 6, col, a * u * 0.85)
            text(c, f"{hh / d0 * 10:.1f}".replace(".0", "").replace(".", ",") if k_e else "10",
                 xa + (passo - 8) / 2, yy - hh / 2 + size * 0.36, size, "black", "#FFFFFF", a * u)
            yy -= hh
            hh *= fator


def pilha(c, cx, base, a, n=1, w=70, h=16, col=GREEN):
    """pilha de notas: n blocos empilhados"""
    if a <= 0:
        return
    for k in range(n):
        y = base - (k + 1) * (h + 4)
        rrect(c, cx - w / 2, y, w, h, 4, col, a)
        line(c, cx - w / 2 + 8, y + h / 2, cx + w / 2 - 8, y + h / 2, "#FFFFFF", a * 0.6, 2)


def fator_par(c, x, y, a, simp, comp, size=56, w=620):
    """os dois fatores lado a lado (simples à esquerda, compostos à direita)"""
    if a <= 0:
        return
    for k, (rot, s, col) in enumerate((("SIMPLES", simp, SIMP), ("COMPOSTOS", comp, COMP))):
        xx = x + k * (w + 40)
        rrect(c, xx, y, w, 190, 24, mix("#FFFFFF", col, 0.08), a)
        text(c, rot, xx + w / 2, y + 50, 26, "black", col, a, tracking=2)
        K.expr(c, s, xx + w / 2, y + 125, size, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "SIMPLES OU COMPOSTO?", BLUE)
    for k, (cue, nome, col) in enumerate((("01.a", "SIMPLES", SIMP), ("01.b", "COMPOSTA", COMP))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 700
        rrect(c, x, 250 + d, 600, 260, 28, "#FFFFFF", a, shadow=True)
        rrect(c, x, 250 + d, 600, 16, 8, col, a)
        text(c, "EMPRÉSTIMO", x + 300, 320 + d, 28, "black", GRAY, a, tracking=2)
        text(c, nome, x + 300, 400 + d, 64, "black", col, a)
        text(c, "10% ao mês", x + 300, 470 + d, 40, "black", INK, a)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        rrect(c, 360, 580, 1200, 110, 55, mix("#FFFFFF", AMBER, 0.16), ac)
        text_mid(c, "“a composta é SEMPRE mais cara”", W / 2, 635, 44, "black", AMBER, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        strike(c, 420, 635, 1500, 635, ad, RED, ad)
        selo(c, W / 2, 790, ad, "15 DIAS: É O CONTRÁRIO", RED, -3, 50)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "saber QUAL REGIME rende mais", "em cada prazo"),
            ("02.b", "reconhecer a RETA e a CURVA", "simples × compostos"),
            ("02.c", "calcular DUPLICAÇÕES sucessivas", "dobra, dobra, dobra")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 46, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "ANTES DE COMEÇAR", GREEN)
    for k, (cue, rot, f, sub, col) in enumerate((
            ("03.a", "SÉRIE DE JUROS SIMPLES", "M = C · (1+i·t)", "no gráfico: uma RETA", SIMP),
            ("03.b", "DO EPISÓDIO 1", "M = C · (1+i)^{t}", "juros compostos", COMP))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 780
        rrect(c, x, 280 + d, 700, 380, 28, mix("#FFFFFF", col, 0.07), a)
        text(c, rot, x + 350, 340 + d, 28, "black", col, a, tracking=2)
        K.expr(c, f, x + 350, 470 + d, 64, a)
        text(c, sub, x + 350, 590 + d, 34, "bold", INK2, a)


# ======================================================================
# concreto — as duas cenas
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS CENAS DA VIDA REAL", "GUARDE AS DUAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 250, 680, 480, 26, "#FFFFFF", aa, shadow=True)
        text(c, "NO BANCO", 570, 310, 28, "black", BLUE, aa, tracking=2)
        for k, (nome, col) in enumerate((("simples · 10% a.m.", SIMP), ("composta · 10% a.m.", COMP))):
            rrect(c, 290, 360 + k * 110, 560, 86, 18, mix("#FFFFFF", col, 0.10), aa)
            text_mid(c, nome, 570, 403 + k * 110, 34, "black", col, aa)
        text_mid(c, "qual é a mais BARATA?", 570, 660, 40, "black", INK, ep(t, C["04.a"] + 2.5, 0.4))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 1010, 250, 680, 480, 26, mix("#FFFFFF", GREEN, 0.08), ab)
        text(c, "PROPAGANDA", 1350, 310, 28, "black", GREEN, ab, tracking=2)
        text_mid(c, "DOBRA A CADA", 1350, 400, 52, "black", INK, ab)
        text_mid(c, "7 ANOS", 1350, 470, 72, "black", GREEN, ab)
        for k in range(4):
            pilha(c, 1140 + k * 140, 650, ab, 2 ** k if k < 3 else 8, 80, 10)
        text(c, "?", 1600, 560, 60, "black", AMBER, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        pill(c, "as duas VOLTAM na aula", W / 2, 790, AMBER, size=30, a=acc, anchor="center")


# ======================================================================
# bloco a — soma × multiplica; os dois fatores
# ======================================================================

def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("05", "A DIFERENÇA DE VERDADE", "SOMA × MULTIPLICA", BLUE),
                       ("06", "NUMA CONTA SÓ", "OS DOIS FATORES, LADO A LADO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            rrect(c, 360, 230, 1200, 110, 22, "#F7F7F5", aa)
            linha(c, [("FATOR", PURPLE), (" = o número que multiplica o ", INK2), ("capital", BLUE)], W / 2, 285, 40,
                  aa)
        ab = ep(t, C["06.b"], 0.5)
        acc = ep(t, C["06.c"], 0.5)
        for k, (al, rot, f, col) in enumerate(((ab, "SIMPLES", "1 + i · t", SIMP), (acc, "COMPOSTOS", "(1+i)^{t}", COMP))):
            if al <= 0:
                continue
            x = 300 + k * 700
            rrect(c, x, 400, 620, 250, 28, mix("#FFFFFF", col, 0.08), al)
            text(c, rot, x + 310, 460, 30, "black", col, al, tracking=2)
            K.expr(c, f, x + 310, 570, 96, al)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            regra(c, "FATOR MAIOR → RENDE MAIS", W / 2, 750, ad, 40)
        return
    # 05: a tabela em duas colunas + as duas escadas
    aa = ep(t, C["05.a"], 0.5)
    ab = ep(t, C["05.b"], 0.5)
    for k, (al, nome, sobre, op, col) in enumerate(((aa, "SIMPLES", "juros sobre o CAPITAL inicial", "+ C · i", SIMP),
                                                    (ab, "COMPOSTOS", "juros sobre o SALDO anterior", "× (1 + i)", COMP))):
        if al <= 0:
            continue
        x = 230 + k * 760
        rrect(c, x, 220, 700, 190, 24, mix("#FFFFFF", col, 0.08), al)
        text(c, nome, x + 350, 270, 30, "black", col, al, tracking=2)
        text(c, sobre, x + 350, 320, 30, "bold", INK2, al)
        linha(c, [("cada mês: ", INK2), (op, col)], x + 350, 370, 36, al)
    acc = ep(t, C["05.c"], 0.5)
    adc = ep(t, C["05.d"], 0.5)
    escadas(c, 300, 800, 1.0, ep(t, C["05.c"], 1.5) if acc > 0 else 0, ep(t, C["05.d"], 1.5) if adc > 0 else 0)
    if acc > 0:
        text(c, "degraus IGUAIS", 500, 470, 30, "black", SIMP, acc)
    if adc > 0:
        text(c, "cada degrau 10% MAIOR", 1100, 470, 30, "black", COMP, adc)


# ======================================================================
# bloco b — o gráfico: reta × curva, a lupa
# ======================================================================

def grafico_10(c, a, prog_r=1.0, prog_c=1.0, x=300, y=280, w=900, h=440):
    g = Graf(x, y, w, h, 0, 10, 80, 280)
    g.eixos(c, a, range(0, 11), (100, 150, 200, 250))
    reta_s(c, g, 100, 0.10, 0, 10, a, prog_r)
    curva_c(c, g, 100, 0.10, 0, 10, a, prog_c)
    return g


def lupa(c, x, y, w, h, a):
    """zoom em volta de t = 0,5: a reta ligeiramente acima da curva"""
    if a <= 0:
        return
    rrect(c, x - 20, y - 70, w + 60, h + 140, 24, "#FFFFFF", a, shadow=True)
    text(c, "LUPA: entre 0 e 1 ano", x + w / 2, y - 25, 24, "black", AMBER, a)
    g = Graf(x + 30, y + 20, w - 40, h - 40, 0.45, 0.55, 104.2, 105.8)
    line(c, g.x, g.y + g.h, g.x + g.w, g.y + g.h, INK2, a, 3)
    reta_s(c, g, 100, 0.10, 0.45, 0.55, a, 1.0, 6)
    curva_c(c, g, 100, 0.10, 0.45, 0.55, a, 1.0, 6)
    xs, ys = g.P(0.5, 105)
    xc, yc = g.P(0.5, 100 * 1.1 ** 0.5)
    line(c, xs, ys, xc, yc, AMBER, a, 3, dash=[6, 5])
    text(c, "1/2 ano", xs, g.y + g.h + 34, 22, "bold", GRAY, a)
    pill(c, "reta por CIMA", x + w / 2, y + h + 40, SIMP, size=22, a=a, anchor="center")


def b_grafico(c, t, C, B):
    head(c, t, B["start"], "NO GRÁFICO", "R$ 100,00 A 10% AO ANO", BLUE)
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    aa = ep(t, C["07.a"], 0.5)
    pr = ep(t, C["07.b"], 1.5)
    pc = ep(t, C["07.c"], 2.0)
    g = grafico_10(c, aa, pr, pc)
    legenda(c, 1290, 260, ep(t, C["07.b"], 0.5))
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0 and sid == "07":
        rrect(c, 1290, 380, 420, 150, 20, mix("#FFFFFF", COMP, 0.08), acc)
        text(c, "CURVA EXPONENCIAL", 1500, 430, 24, "black", COMP, acc, tracking=1)
        text(c, "sobe cada vez", 1500, 470, 24, "bold", INK2, acc)
        text(c, "mais rápido", 1500, 502, 24, "bold", INK2, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        ponto(c, g, 10, 200, ad, SIMP, 11, "R$ 200,00", -20, 34, align="right")
        ponto(c, g, 10, 259.37, ad, COMP, 11, "R$ 259,37", -20, -30, align="right")
    if sid != "08":
        return
    a1 = ep(t, C["08.a"], 0.5)
    if a1 > 0:
        x, y = g.P(0, 100)
        c.drawCircle(x, y, 28, paint(AMBER, a1 * 0.3))
        ponto(c, g, 0, 100, a1, INK, 9)
    lupa(c, 1290, 420, 400, 260, ep(t, C["08.b"], 0.5))
    a3 = ep(t, C["08.c"], 0.5)
    if a3 > 0:
        x, y = g.P(1, 110)
        pulse = 0.5 + 0.5 * math.sin(t * 5)
        c.drawCircle(x, y, 26 + 8 * pulse, paint(AMBER, a3 * 0.3))
        ponto(c, g, 1, 110, a3, AMBER, 11)
        pill(c, "encontro em t = 1", x + 30, y + 50, AMBER, size=22, a=a3, anchor="left")
    a4 = ep(t, C["08.d"], 0.5)
    if a4 > 0:
        pill(c, "antes de 1 período: RETA por cima · depois: a CURVA dispara", W / 2, 800, AMBER, size=28, a=a4,
             anchor="center")


# ======================================================================
# bloco c — o prazo decide
# ======================================================================

PRAZOS = [("09.b", "MEIO ANO", "1,05", "1,0488", "SIMPLES GANHA", SIMP),
          ("09.c", "1 ANO", "1,10", "1,10", "EMPATE", AMBER),
          ("09.d", "2 ANOS", "1,20", "1,21", "COMPOSTO GANHA", COMP)]


def b_prazo(c, t, C, B):
    head_seq(c, t, C, [("09", "QUEM RENDE MAIS?", "DEPENDE DO PRAZO", BLUE), ("10", "ATALHO", "O PRAZO DECIDE", GREEN)])
    card(c, *CARD_R)
    if which(t, C, ["09", "10"]) == "10":
        a0 = ep(t, C["10"], 0.4)
        K.boxed(c, 300, 230, 1320, 560, GREEN, a0, 0.06)
        text(c, "ATALHO · 10% ao ano", W / 2, 285, 26, "black", GREEN, a0, tracking=3)
        rows = [("10.a", "prazo MENOR que 1 período", "SIMPLES rende mais", SIMP),
                ("10.b", "EXATAMENTE 1 período", "EMPATE", AMBER),
                ("10.c", "prazo MAIOR que 1 período", "COMPOSTOS rendem mais", COMP)]
        for k, (cue, s1, s2, col) in enumerate(rows):
            a, d = rise(t, C[cue])
            y = 400 + k * 130 + d
            text(c, s1, 380, y, 42, "black", INK, a, align="left")
            text(c, "→", 1000, y, 42, "black", GRAY, a)
            text(c, s2, 1060, y, 42, "black", col, a, align="left")
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        linha(c, [("fator simples  ", SIMP), ("1 + i · t", SIMP), ("     ×     ", GRAY), ("fator compostos  ", COMP),
                   ("(1 + i)ᵗ", COMP)], W / 2, 250, 34, aa)
    for k, (cue, nome, fs, fc, res, col) in enumerate(PRAZOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 310 + d, 460, 420, 26, "#FFFFFF", a, shadow=True)
        text(c, nome, x + 230, 370 + d, 36, "black", INK, a)
        text(c, "simples", x + 120, 440 + d, 24, "bold", SIMP, a)
        text(c, "compostos", x + 340, 440 + d, 24, "bold", COMP, a)
        text_mid(c, fs, x + 120, 510 + d, 48, "black", SIMP, a)
        text_mid(c, fc, x + 345, 510 + d, 48 if len(fc) < 6 else 40, "black", COMP, a)
        text_mid(c, "×", x + 230, 510 + d, 36, "black", GRAY, a)
        if k == 0:
            text(c, "compostos ≈ √1,1 (vezes ele mesmo dá 1,1)", x + 230, 580 + d, 20, "bold", GRAY, a)
        ar = ep(t, C[cue] + 2.5 + (1.5 if k == 0 else 0), 0.4)
        if ar > 0:
            rrect(c, x + 40, 620 + d, 380, 70, 35, col, ar)
            text_mid(c, res, x + 230, 655 + d, 30, "black", "#FFFFFF", ar)


# ======================================================================
# bloco d — juros de mora
# ======================================================================

def b_mora(c, t, C, B):
    head(c, t, B["start"], "NO MUNDO REAL", "POR QUE A MORA É SIMPLES?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 240, 640, 470, 26, "#FFFFFF", aa, shadow=True)
        rrect(c, 230, 240, 640, 80, 26, RED, aa)
        text_mid(c, "CONTA ATRASADA", 550, 280, 34, "black", "#FFFFFF", aa)
        for k in range(15):
            col_ = RED if k < 5 else "#E6E6E2"
            rrect(c, 280 + (k % 5) * 110, 360 + (k // 5) * 100, 90, 80, 14, col_, aa * (0.85 if k < 5 else 1))
            text_mid(c, str(k + 1), 325 + (k % 5) * 110, 400 + (k // 5) * 100, 30, "black",
                     "#FFFFFF" if k < 5 else GRAY, aa)
        text(c, "5 dias de atraso", 550, 690, 28, "black", RED, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 980, 260, 680, 200, 24, mix("#FFFFFF", AMBER, 0.12), ab)
        text(c, "poucos dias = FRAÇÃO de mês", 1320, 330, 34, "black", AMBER, ab)
        text(c, "aí o fator SIMPLES é o maior", 1320, 400, 32, "black", SIMP, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        regra(c, "MORA DE POUCOS DIAS → JUROS SIMPLES", 1320, 560, acc, 30)
        pill(c, "o empréstimo de 15 dias do gancho: SIMPLES mais caro", 1320, 680, AMBER, size=24, a=acc,
             anchor="center")


# ======================================================================
# bloco e — PG e exponencial
# ======================================================================

def b_pg(c, t, C, B):
    head(c, t, B["start"], "A LISTA DOS MONTANTES COMPOSTOS", "R$ 100,00 A 10% AO ANO", BLUE)
    card(c, *CARD_R)
    vals = ["100", "110", "121", "133,10"]
    xs = [360 + k * 400 for k in range(4)]
    for k, v in enumerate(vals):
        a = ep(t, C["12.a"] + 0.2 + k * 1.2, 0.4)
        if a <= 0:
            continue
        rrect(c, xs[k] - 150, 270, 300, 110, 22, "#FFFFFF", a, shadow=True)
        text(c, f"ano {k}", xs[k], 255, 22, "bold", GRAY, a)
        fmid(c, f"R$ {v}", xs[k], 325, 44, "black", COMP, a)
        if k:
            ab = ep(t, C["12.b"] + 0.3 * k, 0.4)
            if ab > 0:
                p = skia.Path()
                p.moveTo(xs[k - 1] + 60, 390); p.quadTo((xs[k - 1] + xs[k]) / 2, 480, xs[k] - 60, 390)
                c.drawPath(p, paint(COMP, ab, stroke=4))
                pill(c, "× 1,1", (xs[k - 1] + xs[k]) / 2, 460, COMP, size=24, a=ab, anchor="center")
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        rrect(c, 230, 540, 700, 150, 20, mix("#FFFFFF", BLUE, 0.08), ab)
        text(c, "PROGRESSÃO GEOMÉTRICA (PG)", 580, 595, 28, "black", BLUE, ab)
        text(c, "multiplica sempre pelo mesmo número", 580, 645, 26, "bold", INK2, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 990, 540, 700, 150, 20, mix("#FFFFFF", BLUE, 0.08), acc)
        text(c, "RAZÃO DA PG = o número multiplicado", 1340, 595, 26, "black", BLUE, acc)
        linha(c, [("aqui: ", INK2), ("1 + i = 1,1", COMP)], 1340, 640, 32, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "a curva = FUNÇÃO EXPONENCIAL  ·  PG e exponencial têm SÉRIES PRÓPRIAS", W / 2, 775, PURPLE, size=26,
             a=ad, anchor="center")


# ======================================================================
# bloco f — tempo de duplicação
# ======================================================================

def b_dobra(c, t, C, B):
    head_seq(c, t, C, [("13", "DOBRA A CADA 7 ANOS", "O TEMPO DE DUPLICAÇÃO", BLUE),
                       ("14", "ATALHO", "CONTE E ELEVE 2", GREEN)])
    card(c, *CARD_R)
    if which(t, C, ["13", "14"]) == "14":
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            K.boxed(c, 260, 230, 640, 560, GREEN, aa, 0.06)
            text(c, "1 · CONTE AS DUPLICAÇÕES", 580, 290, 26, "black", GREEN, aa, tracking=1)
            linha(c, [("prazo ÷ tempo de dobrar", INK)], 580, 400, 38, aa)
            linha(c, [("21 anos ÷ 7 anos = ", INK2), ("3", GREEN)], 580, 500, 38, ep(t, C["14.a"] + 1.5, 0.4))
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            K.boxed(c, 1000, 230, 660, 560, GREEN, ab, 0.06)
            text(c, "2 · ELEVE 2 A ESSE NÚMERO", 1330, 290, 26, "black", GREEN, ab, tracking=1)
            for k, (n, f) in enumerate(((1, 2), (2, 4), (3, 8), (4, 16))):
                a = ep(t, C["14.b"] + 1.0 + k * 0.9, 0.4)
                y = 390 + k * 100
                text(c, f"{n} duplicaç{'ão' if n == 1 else 'ões'}", 1100, y, 34, "black", INK, a, align="left")
                linha(c, [(f"× {f}", GREEN)], 1530, y - 12, 40, a)
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 230, 1440, 90, 20, mix("#FFFFFF", BLUE, 0.08), aa)
        linha(c, [("TEMPO DE DUPLICAÇÃO", BLUE), (" = o tempo para o dinheiro dobrar · na curva, SEMPRE O MESMO", INK2)],
              W / 2, 275, 28, aa)
    base = 700
    marcos = [("hoje", "× 1", 1), ("7 anos", "× 2", 2), ("14 anos", "× 4", 4), ("21 anos", "× 8", 8)]
    line(c, 260, base + 10, 1660, base + 10, INK2, ep(t, C["13.b"], 0.4), 4)
    for k, (rot, f, n) in enumerate(marcos):
        a = ep(t, C["13.b"] + k * 1.6, 0.4)
        if a <= 0:
            continue
        cx = 380 + k * 390
        por_fila = min(n, 4)
        for j in range(n):
            col_, fila_ = j % 4, j // 4
            x = cx + (col_ - (por_fila - 1) / 2) * 84
            pilha(c, x, base - fila_ * 70, a, 3, 74, 14)
        text(c, rot, cx, base + 60, 28, "bold", GRAY, a)
        text(c, f, cx, base - 120 - (n // 5) * 70, 44, "black", GREEN, a)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        selo(c, 1500, 420, acc, "3 DUPLICAÇÕES = × 8, NÃO × 3", AMBER, -3, 32)


# ======================================================================
# bloco g — decaimento
# ======================================================================

def b_decai(c, t, C, B):
    head(c, t, B["start"], "E SE O FATOR FOR MENOR QUE 1?", "DECAIMENTO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 240, 640, 160, 22, mix("#FFFFFF", BLUE, 0.08), aa)
        text(c, "DECAIMENTO", 550, 300, 30, "black", BLUE, aa, tracking=2)
        text(c, "o valor ENCOLHE a cada período", 550, 355, 28, "bold", INK2, aa)
    ab = ep(t, C["15.b"], 0.5)
    vals = [100, 80, 64, 51.2]
    for k, v in enumerate(vals):
        a = ep(t, C["15.b"] + 0.6 + k * 0.8, 0.4)
        if a <= 0:
            continue
        x = 990 + k * 170
        hh = v * 4
        rrect(c, x, 760 - hh, 120, hh, 10, COMP, a * 0.85)
        fmid(c, (f"{v:.1f}".replace(".", ",") if v % 1 else f"{v:.0f}") + "%", x + 60, 740 - hh, 26, "black", INK, a)
        text(c, f"ano {k}", x + 60, 790, 22, "bold", GRAY, a)
    pill(c, "× 0,8 a cada ano", 1300, 822, AMBER, size=24, a=ep(t, C["15.b"] + 3.5, 0.4), anchor="center")
    if ab > 0:
        text(c, "carro que perde 20% ao ano", 550, 470, 30, "black", INK, ab)
        K.expr(c, "valor = V · 0,8^{t}", 550, 570, 60, ab)
        text(c, "V = valor inicial", 550, 650, 24, "bold", GRAY, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        pill(c, "também tem SÉRIE PRÓPRIA", 550, 740, PURPLE, size=26, a=acc, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "FATOR AO LADO DE FATOR", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        linha(c, [("R$ 1.000,00", BLUE), ("  a  ", INK2), ("20% ao ano", PURPLE), ("  por  ", INK2), ("2 anos", AMBER)],
              W / 2, 260, 50, aa)
    ab = ep(t, C["16.b"], 0.5)
    if t < C["17"]:
        if ab > 0:
            linha(c, [("simples = ?", SIMP), ("     ", INK), ("compostos = ?", COMP)], W / 2, 420, 54, ab)
        pause_timer(c, t, C["16.end"] - 1.9, W / 2, 620)
        return
    for k, (cue, rot, conta, fat, m, col) in enumerate((
            ("17.a", "SIMPLES", "1 + 0,2 · 2", "= 1,40", "R$ 1.400,00", SIMP),
            ("17.b", "COMPOSTOS", "1,2^{2}", "= 1,44", "R$ 1.440,00", COMP))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 260 + k * 720
        rrect(c, x, 330 + d, 660, 360, 26, mix("#FFFFFF", col, 0.08), a)
        text(c, rot, x + 330, 385 + d, 28, "black", col, a, tracking=2)
        K.expr(c, conta + " " + fat, x + 330, 490 + d, 64, a)
        text(c, "montante", x + 330, 580 + d, 26, "bold", GRAY, a)
        fmid(c, m, x + 330, 640 + d, 52, "black", col, a)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 780, acc, "COMPOSTO GANHA: + R$ 40,00 = JUROS SOBRE JUROS", GREEN, -2, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Simples soma; composto multiplica.",
          "Antes de um período, o simples rende mais; depois, o composto.",
          "Cada duplicação multiplica por 2: três duplicações, vezes 8."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("\"Juros compostos SEMPRE rendem mais\"", "no longo prazo a curva dispara, e é isso que todo mundo vê",
          "antes do 1º período o SIMPLES rende mais (1,05 × 1,0488)"),
         ("Decidir pela REGRA GERAL: simples 11% × compostos 10%, 2 anos",
          "as regras gerais valem quando o resto é igual",
          "faça a conta: 1,22 × 1,21 → aqui o SIMPLES ganha"),
         ("Multiplicar pelas duplicações: R$ 1.000,00, dobra a cada 5 anos, 15 anos → R$ 3.000,00?",
          "são TRÊS períodos",
          "cada período DOBRA: 2, 4, 8 → R$ 8.000,00 (2³, não 2 · 3)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões
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


ALTS4 = [("A", "compostos SEMPRE mais cara", "só vale depois de 1 mês", RED),
         ("B", "as duas SEMPRE iguais", "regimes diferentes", RED),
         ("C", "< 1 mês: simples mais cara; > 1 mês: compostos", "", GREEN),
         ("D", "< 1 mês: compostos mais cara; > 1 mês: simples", "inverte as faixas", RED),
         ("E", "simples SEMPRE mais cara", "só vale abaixo de 1 mês", RED)]


def b_q4(c, t, C, B):
    head_seq(c, t, C, [("22", "QUESTÃO 4 · EU FAÇO", "SIMPLES OU COMPOSTOS, CONFORME O PRAZO", BLUE),
                       ("23", "RESOLVENDO", "FATOR AO LADO DE FATOR", BLUE), ("24", "AS ERRADAS", "POR QUE ENGANAM", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    yend = _enunciado(c, [("Um banco oferece duas modalidades de empréstimo com a mesma taxa de 10% ao mês: uma a juros "
                           "simples e outra a juros compostos. Comparando o valor a pagar ao final do prazo, conclui-se "
                           "que", INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS4, 980, 240, 720, 26, C["23.ok"], "C", cues_in, cues_x, gap=22)
    if t < C["23"]:
        pause_timer(c, t, C["22.end"] - 1.9, 540, 680)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["23"], 0.4))
    text(c, "simples", 600, y0 + 50, 24, "black", SIMP, ep(t, C["23"], 0.4))
    text(c, "compostos", 790, y0 + 50, 24, "black", COMP, ep(t, C["23"], 0.4))
    rows = [("23.a", "meio mês", "1,05", "≈ 1,049"), ("23.b", "1 mês", "1,10", "1,10"), ("23.c", "2 meses", "1,20", "1,21")]
    for k, (cue, p_, fs, fc) in enumerate(rows):
        a = ep(t, C[cue], 0.4)
        y = y0 + 110 + k * 70
        text(c, p_, 210, y, 30, "black", INK, a, align="left")
        text(c, fs, 600, y, 34, "black", SIMP, a)
        text(c, fc, 790, y, 34, "black", COMP, a)
    ad = ep(t, C["23.d"], 0.4)
    if ad > 0 and y0 + 330 < 820:
        text(c, "o cruzamento da reta com a curva", 540, y0 + 330, 26, "black", AMBER, ad)


ALTS8 = [("A", "I rende R$ 2.000,00 a mais", "II calculada como simples", RED),
         ("B", "II rende R$ 2.000,00 a mais", "inverte o erro da A", RED),
         ("C", "I rende mais: taxa maior", "regra geral, sem conta", RED),
         ("D", "II rende mais: compostos sempre superam", "regra geral, sem conta", RED),
         ("E", "rendem exatamente o mesmo", "", GREEN)]


def b_q8(c, t, C, B):
    head_seq(c, t, C, [("25", "QUESTÃO 8 · NÓS FAZEMOS", "DUAS PROPOSTAS DE INVESTIMENTO", GREEN),
                       ("26", "VAMOS JUNTOS", "A CONTA DECIDE", GREEN), ("27", "AS ERRADAS", "POR QUE ENGANAM", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("Um investidor tem R$ 50.000,00 para aplicar por 2 anos e recebe duas propostas:", INK),
                          ("I) juros simples de 22% ao ano;", SIMP), ("II) juros compostos de 20% ao ano.", COMP),
                          ("Sobre os juros obtidos ao final dos 2 anos:", INK)], a0, 240, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABCD"}
    cues_x["D"] = C["27.xc"] + 0.6
    K.alternativas(c, t, C, ALTS8, 980, 240, 720, 28, C["26.ok"], "E", cues_in, cues_x, gap=26)
    if t < C["26"]:
        pause_timer(c, t, C["25.end"] - 1.9, 540, 720)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["26"], 0.4))
    a1 = ep(t, C["26.a"], 0.4)
    linha(c, [("I: ", SIMP), ("50.000 · 0,22 · 2 = ", INK), ("R$ 22.000,00", SIMP)], 540, y0 + 55, 28, a1)
    a2 = ep(t, C["26.b"], 0.4)
    if a2 > 0:
        K.expr(c, "1,2^{2} = 1,44", 540, y0 + 125, 34, a2)
        linha(c, [("II: ", COMP), ("50.000 · 0,44 = ", INK), ("R$ 22.000,00", COMP)], 540, y0 + 190, 28,
              ep(t, C["26.b"] + 3.5, 0.4))
    a3 = ep(t, C["26.c"], 0.4)
    if a3 > 0 and t < C["27"]:
        selo(c, 540, y0 + 270, a3, "EMPATE!", GREEN, -3, 38)
    if t >= C["27"]:
        ax = ep(t, C["27.xa"], 0.4)
        if ax > 0:
            linha(c, [("erro da A: ", RED), ("50.000 · 0,20 · 2 = 20.000", INK)], 540, y0 + 270, 26, ax)


ALTS9 = [("A", "R$ 15.000,00", "× 3 (nº de períodos)", RED), ("B", "R$ 20.000,00", "+ 5.000 por período", RED),
         ("C", "R$ 30.000,00", "× 2 · 3", RED), ("D", "R$ 40.000,00", "", GREEN),
         ("E", "R$ 45.000,00", "somou o capital de novo", RED)]


def b_q9(c, t, C, B):
    head_seq(c, t, C, [("28", "QUESTÃO 9 · VOCÊ FAZ", "DUPLICAÇÕES SUCESSIVAS", GREEN),
                       ("29", "CONFERINDO", "DOBRAR, DOBRAR, DOBRAR", GREEN), ("30", "AS ERRADAS", "POR QUE ENGANAM", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, [("Em uma aplicação a juros compostos, o saldo dobra a cada 7 anos. Uma pessoa depositou "
                           "R$ 5.000,00 e não fez retiradas. Após 21 anos, o saldo será de", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["29"], 0.3)),
         align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS9, 1000, 260, 680, 36, C["29.ok"], "D", cues_in, cues_x, gap=34)
    if t < C["29"]:
        pause_timer(c, t, C["28.end"] - 1.9, 540, 680)
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["29"], 0.4))
    a1 = ep(t, C["29.a"], 0.4)
    linha(c, [("21 ÷ 7 = ", INK), ("3 duplicações", GREEN)], 540, y0 + 55, 32, a1)
    vals = ["5 mil", "10 mil", "20 mil", "40 mil"]
    for k, v in enumerate(vals):
        a = ep(t, C["29.b"] + 0.6 * k, 0.3)
        x = 250 + k * 190
        fmid(c, v, x, y0 + 160, 30, "black", GREEN if k == 3 else INK, a)
        if k:
            pill(c, "× 2", x - 95, y0 + 210, GREEN, size=20, a=a, anchor="center")
    ab = ep(t, C["29.b"] + 3.0, 0.4)
    if ab > 0:
        K.expr(c, "5.000 · 2^{3} = 5.000 · 8", 540, y0 + 290, 34, ab)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "POTÊNCIAS SEM CALCULADORA", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    if aa > 0:
        K.expr(c, "1,05^{12} = ?", W / 2, 330, 96, aa)
        text(c, "sem calculadora", W / 2, 430, 34, "bold", GRAY, aa)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 480, 800, 150, 26, mix("#FFFFFF", GREEN, 0.10), ab)
        text(c, "PISTA DA PROVA", W / 2, 525, 24, "black", GREEN, ab, tracking=2)
        K.expr(c, "1,05^{6} ≈ 1,34", W / 2, 590, 60, ab)
    pill(c, "o que fazer com ela?  ·  ep. 3", W / 2, 720, PURPLE, size=30, a=ep(t, C["32.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"],
        "Você também achava que juros compostos sempre rendem mais?", canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, tabela=b_tabela,
              grafico=b_grafico, prazo=b_prazo, mora=b_mora, pg=b_pg, dobra=b_dobra, decai=b_decai,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q8=b_q8, q9=b_q9, ponte=b_ponte, cta=b_cta)
