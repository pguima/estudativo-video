"""Visual — Velocidade, Densidade e Vazão, Episódio 5: vazão, torneiras somando e ralos subtraindo (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: tanque() (fatiado em n fatias, com nível de água), torneira(), ralo(), balde(), banheira(),
caixa_dagua(), cano() (Q = A · v), carimbo() (conferência verde), linha().
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
_s = importlib.util.spec_from_file_location("comum027", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_velocidade_ep5_vazao_torneiras.mp4"
CARD_R = K.CARD_R
AGUA = "#5B9BF0"
T1 = BLUE       # torneira 1
T2 = PURPLE     # torneira 2


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


def carimbo(c, s, x, y, a, size=34):
    """carimbo verde de conferência (moldura dupla, girado)"""
    if a <= 0:
        return
    sc = 1.25 - 0.25 * a
    w = text_w(s, "black", size) + 100
    h = size * 2.0
    c.save()
    c.translate(x, y); c.rotate(-7); c.scale(sc, sc)
    r = skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h)
    c.drawRRect(skia.RRect.MakeRectXY(r, 14, 14), paint(GREEN, a, stroke=6))
    r2 = skia.Rect.MakeXYWH(-w / 2 + 9, -h / 2 + 9, w - 18, h - 18)
    c.drawRRect(skia.RRect.MakeRectXY(r2, 9, 9), paint(GREEN, a * 0.6, stroke=2))
    check_icon(c, -w / 2 + 40, 0, size * 0.55, a, GREEN)
    text_mid(c, s, 22, 0, size, "black", GREEN, a)
    c.restore()


def tanque(c, x, y, w, h, n, nivel, a, rot=True, cor=AGUA, apagado=0.0, pintado=0.0, cor_pint=GREEN):
    """tanque visto de frente, dividido em n fatias horizontais; nivel em fatias (0..n).
    pintado: fatias acima do nível que acabaram de entrar (destaque); apagado: fatias que o ralo tirou (vermelho tracejado)."""
    if a <= 0:
        return
    fh = h / n
    rrect(c, x - 10, y - 10, w + 20, h + 20, 18, "#FFFFFF", a, shadow=True)
    nv = max(0.0, min(n, nivel))
    if nv > 0:
        rrect(c, x, y + h - nv * fh, w, nv * fh, 8, cor, a * 0.85)
    if pintado > 0:
        y0 = y + h - nv * fh
        rrect(c, x, y0 - pintado * fh, w, pintado * fh, 6, cor_pint, a * 0.55)
    if apagado > 0:
        y0 = y + h - nv * fh
        r = skia.Rect.MakeXYWH(x + 4, y0 - apagado * fh, w - 8, apagado * fh)
        c.drawRect(r, paint(RED, a * 0.10))
        c.drawRect(r, paint(RED, a * 0.9, stroke=3))
    for k in range(1, n):
        yy = y + h - k * fh
        line(c, x, yy, x + w, yy, INK2 if k > nv else "#FFFFFF", a * 0.55, 2, dash=(10, 8))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 8, 8), paint(INK, a, stroke=5))
    if rot:
        for k in range(n):
            yy = y + h - (k + 0.5) * fh
            text_mid(c, str(k + 1), x + w + 28, yy, min(26, fh * 0.6), "bold", GRAY, a)


def torneira(c, x, y, a, col=T1, s=1.0, jato=1.0, jato_len=120):
    """torneira com a boca em (x, y), saindo água para baixo; jato 0..1"""
    if a <= 0:
        return
    rrect(c, x - 110 * s, y - 70 * s, 110 * s, 34 * s, 10 * s, col, a)          # cano horizontal
    rrect(c, x - 22 * s, y - 70 * s, 40 * s, 70 * s, 12 * s, col, a)            # bico
    rrect(c, x - 70 * s, y - 104 * s, 18 * s, 36 * s, 6 * s, INK2, a)            # haste
    rrect(c, x - 96 * s, y - 112 * s, 70 * s, 16 * s, 8 * s, INK2, a)            # registro
    if jato > 0:
        rrect(c, x - 11 * s, y, 22 * s, jato_len * jato, 8 * s, AGUA, a * 0.85)


def ralo(c, x, y, a, s=1.0, jato=1.0):
    """ralo com a saída em (x, y), água caindo para baixo"""
    if a <= 0:
        return
    rrect(c, x - 30 * s, y, 60 * s, 40 * s, 8 * s, RED, a)
    for k in range(3):
        line(c, x - 18 * s, y + (10 + 10 * k) * s, x + 18 * s, y + (10 + 10 * k) * s, "#FFFFFF", a, 3)
    if jato > 0:
        rrect(c, x - 9 * s, y + 40 * s, 18 * s, 60 * s * jato, 6 * s, AGUA, a * 0.7)


def balde(c, cx, by, a, nivel=0.5, s=1.0):
    if a <= 0:
        return
    w0, w1, h = 150 * s, 110 * s, 150 * s
    pth = skia.Path()
    pth.moveTo(cx - w0 / 2, by - h); pth.lineTo(cx + w0 / 2, by - h); pth.lineTo(cx + w1 / 2, by); pth.lineTo(cx - w1 / 2, by)
    pth.close()
    c.drawPath(pth, paint("#FFFFFF", a))
    c.save(); c.clipPath(pth, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeLTRB(cx - w0, by - h * nivel, cx + w0, by), paint(AGUA, a * 0.85))
    c.restore()
    c.drawPath(pth, paint(INK, a, stroke=5))
    c.drawArc(skia.Rect.MakeXYWH(cx - w0 / 2, by - h - 70 * s, w0, 140 * s), 180, 180, False, paint(INK2, a, stroke=4))


def caixa_dagua(c, cx, by, a, nivel=0.5, s=1.0):
    if a <= 0:
        return
    # telhado + casa
    pth = skia.Path()
    pth.moveTo(cx - 120 * s, by - 90 * s); pth.lineTo(cx, by - 170 * s); pth.lineTo(cx + 120 * s, by - 90 * s); pth.close()
    c.drawPath(pth, paint(INK2, a))
    rrect(c, cx - 100 * s, by - 90 * s, 200 * s, 90 * s, 6 * s, "#E4E4E0", a)
    rrect(c, cx - 22 * s, by - 60 * s, 44 * s, 60 * s, 4 * s, INK2, a)
    # caixa em cima
    x, y, w, h = cx - 60 * s, by - 290 * s, 120 * s, 110 * s
    rrect(c, x, y, w, h, 14 * s, "#FFFFFF", a)
    rrect(c, x, y + h * (1 - nivel), w, h * nivel, 12 * s, AGUA, a * 0.85)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14 * s, 14 * s), paint(INK, a, stroke=5))
    line(c, cx + 60 * s, y + 20 * s, cx + 90 * s, y + 20 * s, INK2, a, 8)


def banheira(c, cx, by, a, nivel=0.4, s=1.0):
    if a <= 0:
        return
    x, y, w, h = cx - 140 * s, by - 110 * s, 280 * s, 110 * s
    rrect(c, x, y, w, h, 40 * s, "#FFFFFF", a)
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 40 * s, 40 * s), doAntiAlias=True)
    c.drawRect(skia.Rect.MakeLTRB(x, y + h * (1 - nivel), x + w, y + h), paint(AGUA, a * 0.85))
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 40 * s, 40 * s), paint(INK, a, stroke=5))
    for dx in (-100, 100):
        rrect(c, cx + dx * s - 8 * s, by, 16 * s, 26 * s, 6 * s, INK2, a)
    ralo(c, cx + 80 * s, by - 6 * s, a, 0.55 * s)


def cano(c, cx, cy, a, prog_=1.0):
    """cano em perspectiva: a seção circular (área A) e a seta da velocidade v"""
    if a <= 0:
        return
    rrect(c, cx - 380, cy - 80, 600, 160, 10, "#DCE7FB", a)
    line(c, cx - 380, cy - 80, cx + 220, cy - 80, INK, a, 5)
    line(c, cx - 380, cy + 80, cx + 220, cy + 80, INK, a, 5)
    c.drawOval(skia.Rect.MakeXYWH(cx + 160, cy - 80, 120, 160), paint(AGUA, a * 0.9))
    c.drawOval(skia.Rect.MakeXYWH(cx + 160, cy - 80, 120, 160), paint(INK, a, stroke=5))
    text_mid(c, "A", cx + 220, cy, 56, "black", "#FFFFFF", a)
    arrow(c, cx - 320, cy, lerp(cx - 300, cx + 100, prog_), cy, PURPLE, a, 8, 26)
    text(c, "v", cx - 120, cy - 20, 56, "black", PURPLE, a)


def fluxo(t, t0, horas, dur_h=1.2):
    """relógio do tanque: devolve (horas inteiras completas, fase 0..1 da hora atual)"""
    u = max(0.0, (t - t0) / dur_h)
    u = min(u, horas)
    k = int(u) if u < horas else horas
    return k, (u - k if u < horas else 0.0)


def relogio(c, cx, cy, horas, a, col=INK, size=40):
    if a <= 0:
        return
    s = f"{horas} h" if isinstance(horas, int) else f"{horas:.1f} h".replace(".", ",")
    rrect(c, cx - 90, cy - 40, 180, 80, 40, "#FFFFFF", a, shadow=True)
    text_mid(c, s, cx, cy, size, "black", col, a)


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


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


def ex(c, s, cx, cy, size, a, cores=None, align="center"):
    """expr com cores por índice de token (padrão: tudo INK)"""
    n = len(s.split())
    cc = {i: INK for i in range(n)}
    cc.update(cores or {})
    return K.expr(c, s, cx, cy, size, a, cores=cc, align=align)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "VELOCIDADE, DENSIDADE E VAZÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        torneira(c, 420, 300, aa, T1, 1.0, ep(t, C["01.a"] + 0.6, 0.6))
        text(c, "6 h", 270, 255, 40, "black", T1, aa)
        a2 = ep(t, C["01.a"] + 2.0, 0.5)
        torneira(c, 640, 300, a2, T2, 1.0, ep(t, C["01.a"] + 2.4, 0.6))
        text(c, "3 h", 490, 255, 40, "black", T2, a2)
        k, f = fluxo(t, C["01.a"] + 1.0, 2, 3.0)
        tanque(c, 380, 420, 300, 360, 6, min(6, 3 * (k + f)), aa, rot=False)
        pergunta(c, "juntas: quanto tempo?", 1230, 330, ep(t, C["01.a"] + 4.0, 0.4))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        linha(c, [("6 h + 3 h = ", INK), ("9 h", RED)], 1230, 500, 64, ab)
        strike(c, 1010, 500, 1460, 500, ep(t, C["01.b"] + 1.6, 0.4), RED)
        selo(c, 1560, 590, ab, "PEGADINHA", AMBER, -8, 40)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        text(c, "2 h", 1230, 720, 130, "black", GREEN, acc)
        text(c, "sem saber o tamanho do tanque", 1230, 790, 32, "bold", GRAY, acc)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "calcular tempo de enchimento", "litros ÷ litros por minuto"),
            ("02.b", "achar a vazão de uma cidade inteira", "L por dia → m³ por hora"),
            ("02.c", "resolver torneiras e ralos", "frações do tanque")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 180 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    cols = [(380, "03.a", "EPISÓDIO 1", BLUE), (960, "03.b", "FRAÇÕES", PURPLE), (1540, "03.c", "UNIDADES", AMBER)]
    for x, cue, tit, col in cols:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        rrect(c, x - 270, 250, 540, 520, 24, mix("#FFFFFF", col, 0.07), a)
        text(c, tit, x, 315, 34, "black", col, a)
    a1 = ep(t, C["03.a"], 0.5)
    for k, (s1, s2) in enumerate([("pediu a taxa", "divida"), ("pediu o de cima", "multiplique"),
                                  ("pediu o de baixo", "divida ao contrário")]):
        ak = a1 * ep(t, C["03.a"] + 0.3 + 1.4 * k, 0.4)
        text(c, s1, 380, 420 + k * 120, 30, "bold", INK2, ak)
        text(c, s2, 380, 462 + k * 120, 36, "black", BLUE, ak)
    a2 = ep(t, C["03.b"], 0.5)
    ex(c, "1/6 + 1/3", 960, 440, 56, a2)
    ex(c, "1/3 = 2/6", 960, 610, 64, ep(t, C["03.b"] + 2.6, 0.4), {2: PURPLE})
    text(c, "mesmo denominador", 960, 720, 28, "bold", GRAY, ep(t, C["03.b"] + 1.4, 0.4))
    a3 = ep(t, C["03.c"], 0.5)
    linha(c, [("1 m³ = ", INK), ("1 000 L", AMBER)], 1540, 460, 48, a3)
    linha(c, [("1 dia = ", INK), ("24 h", AMBER)], 1540, 600, 48, ep(t, C["03.c"] + 2.4, 0.4))


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS CENAS DE CASA", "", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        torneira(c, 470, 330, aa, T1, 0.9, 1.0, 150)
        balde(c, 470, 640, aa, 0.15 + 0.5 * ep(t, C["04.a"] + 0.4, 6.0))
        text(c, "balde", 470, 720, 36, "black", INK, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        caixa_dagua(c, 960, 640, ab, 0.2 + 0.5 * ep(t, C["04.b"] + 0.4, 6.0))
        text(c, "caixa-d'água", 960, 720, 36, "black", INK, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        torneira(c, 1400, 480, acc, T1, 0.7, 1.0, 50)
        banheira(c, 1450, 640, acc, 0.25 + 0.3 * ep(t, C["04.c"] + 0.4, 6.0))
        text(c, "banheira com ralo aberto", 1450, 720, 36, "black", INK, acc)
        pill(c, "entra", 1290, 420, GREEN, size=24, a=acc, anchor="center")
        pill(c, "sai", 1650, 660, RED, size=24, a=acc, anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        pergunta(c, "em quanto tempo enche?", W / 2, 800, ad)


# ======================================================================
# bloco a: definição
# ======================================================================

def b_def(c, t, C, B):
    head_seq(c, t, C, [("05", "O QUE É VAZÃO?", "A VELOCIDADE DA ÁGUA", BLUE),
                       ("06", "E O TEMPO?", "O DE BAIXO: DIVIDA AO CONTRÁRIO", PURPLE)])
    card(c, *CARD_R)
    if t < C["06"]:
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 225, 1320, 100, BLUE, aa)
            linha(c, [("VAZÃO", BLUE), (": quanto de água passa em cada unidade de tempo", INK)], W / 2, 275, 38, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            linha(c, [("velocidade: ", GRAY), ("km/h", INK)], 620, 420, 48, ab)
            arrow(c, 860, 420, 1000, 420, BLUE, ab, 6, 20)
            linha(c, [("vazão: ", GRAY), ("L/min", BLUE)], 1250, 420, 48, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            boxed(c, 660, 500, 600, 190, PURPLE, acc)
            text(c, "Q  = ", 820, 615, 70, "black", PURPLE, acc)
            fr(c, "V (volume)", "t (tempo)", 1050, 595, 52, INK, acc, num_col=BLUE, den_col=AMBER)
        ad = ep(t, C["05.d"], 0.5)
        for k, s in enumerate(["L/s", "L/min", "m³/h"]):
            chip(c, s, 760 + k * 200, 770, BLUE, ad * ep(t, C["05.d"] + 0.8 * k, 0.4), 36)
        return
    aa = ep(t, C["06.a"], 0.4)
    if aa > 0:
        fr(c, "V", "t", 700, 400, 90, INK, 1.0, num_col=INK, den_col=AMBER)
        text(c, "Q  = ", 540, 425, 80, "black", PURPLE, 1.0)
        pill(c, "o tempo está EMBAIXO", 700, 560, AMBER, size=30, a=aa, anchor="center")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        boxed(c, 1000, 290, 620, 230, PURPLE, ab)
        text(c, "t  = ", 1170, 425, 80, "black", PURPLE, ab)
        fr(c, "V", "Q", 1360, 400, 90, INK, ab, num_col=BLUE, den_col=PURPLE)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        boxed(c, 300, 640, 1320, 130, BLUE, acc)
        linha(c, [("CAPACIDADE", BLUE), (": quantos litros cabem no ", INK), ("RESERVATÓRIO", BLUE)], W / 2, 690, 34, acc)
        text(c, "reservatório: onde a água fica guardada", W / 2, 750, 26, "bold", GRAY, acc)


# ======================================================================
# bloco b: a caixa
# ======================================================================

def b_caixa(c, t, C, B):
    head(c, t, B["start"], "NA PRÁTICA", "UMA CAIXA DE 1 500 L", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        torneira(c, 400, 300, aa, T1, 1.0, 1.0, 90)
        g = ep(t, C["07.a"] + 0.5, 14.0)
        tanque(c, 260, 400, 300, 360, 1, g, aa, rot=False)
        text(c, "1 500 L", 410, 820, 40, "black", BLUE, aa)
        pill(c, "12,5 L/min", 560, 240, BLUE, size=30, a=aa, anchor="left")
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        linha(c, [("t = ", PURPLE)], 820, 400, 60, ab, align="left")
        fr(c, "1 500 L", "12,5 L/min", 1120, 380, 60, INK, ab, num_col=BLUE, den_col=BLUE)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        strike(c, 1150, 365, 1215, 330, acc, RED)
        strike(c, 1095, 440, 1140, 410, acc, RED)
        pill(c, "litro corta litro: sobra o MINUTO", 1120, 530, GREEN, size=30, a=acc, anchor="center")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        linha(c, [("= ", INK), ("120 min", INK)], 1120, 650, 64, ad)
        linha(c, [("= ", INK), ("2 h", GREEN)], 1120, 760, 72, ep(t, C["07.d"] + 2.0, 0.4))


def b_atalho_div(c, t, C, B):
    head(c, t, B["start"], "DIVIDIR POR 12,5", "SEM CALCULADORA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 300, 240, 1320, 240, "ATALHO · DIVIDIR POR 12,5",
             ["÷ 12,5  =  × 8  e depois  ÷ 100", "porque 8 × 12,5 = 100"], aa, 42)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        linha(c, [("1 500 × 8 = 12 000", INK)], W / 2, 580, 52, ab)
        linha(c, [("12 000 ÷ 100 = ", INK), ("120 min", GREEN)], W / 2, 670, 52, ep(t, C["08.b"] + 2.4, 0.4))
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        conferido(c, "12,5 L/min × 120 min = 1 500 L", 620, 790, acc, True, 36)


# ======================================================================
# bloco c: frações do tanque
# ======================================================================

def b_fatias(c, t, C, B):
    head(c, t, B["start"], "SEM O TAMANHO DO TANQUE?", "PENSE EM PEDAÇOS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        torneira(c, 480, 270, aa, T1, 1.0, 1.0 if t >= C["09.c"] else 0.0, 70)
        pill(c, "enche em 6 h", 600, 220, T1, size=30, a=aa, anchor="left")
    ab = ep(t, C["09.b"], 0.5)
    k, f = fluxo(t, C["09.c"], 6, 1.0)
    tanque(c, 330, 360, 300, 420, 6, k + f, aa, rot=ab > 0)
    if ab > 0:
        pill(c, "6 fatias iguais", 480, 815, PURPLE, size=28, a=ab, anchor="center")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        relogio(c, 820, 470, k, acc)
        ex(c, "1/6", 1150, 440, 110, acc, {0: BLUE})
        text(c, "do tanque por hora", 1430, 455, 40, "black", INK, acc, align="center")
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        boxed(c, 780, 610, 860, 150, BLUE, ad)
        linha(c, [("FRAÇÃO DO TANQUE", BLUE), (": o pedaço que enche em 1 hora", INK)], 1210, 660, 32, ad)
        text(c, "funciona como vazão, sem saber os litros", 1210, 730, 28, "bold", GRAY, ad)


# ======================================================================
# bloco d: duas torneiras
# ======================================================================

def b_duas(c, t, C, B):
    head_seq(c, t, C, [("10", "DUAS TORNEIRAS JUNTAS", "SOMAM-SE AS FATIAS POR HORA", PURPLE),
                       ("11", "UM TIME TRABALHANDO JUNTO", "O TEMPO DIMINUI", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    ab = ep(t, C["10.b"], 0.5)
    torneira(c, 400, 270, aa, T1, 0.9, 1.0, 70)
    text(c, "6 h", 255, 228, 36, "black", T1, aa)
    torneira(c, 600, 270, ab, T2, 0.9, 1.0, 70)
    text(c, "3 h", 455, 228, 36, "black", T2, ab)
    # tanque: a cada hora, 1 fatia azul + 2 roxas
    if t < C["10.c"]:
        nivel = 0.0
    else:
        k, f = fluxo(t, C["10.c"] + 0.6, 2, 1.6)
        nivel = 3 * (k + f)
    tanque(c, 330, 360, 300, 420, 6, nivel, aa)
    if t < C["11"]:
        ex(c, "1/6", 900, 330, 64, aa, {0: T1})
        text(c, "1 fatia por hora", 1080, 345, 32, "bold", T1, aa, align="left")
        ex(c, "1/3 = 2/6", 960, 470, 64, ab, {0: T2, 2: T2})
        text(c, "2 fatias por hora", 1140, 485, 32, "bold", T2, ab, align="left")
        acc = ep(t, C["10.c"], 0.5)
        ex(c, "1/6 + 2/6 = 3/6 = 1/2", 1200, 620, 64, acc, {6: GREEN})
        text(c, "do tanque por hora", 1200, 725, 30, "bold", GRAY, acc)
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            linha(c, [("→ enche em ", INK), ("2 h", GREEN)], 1200, 790, 52, ad)
        return
    if t >= C["10.c"]:
        relogio(c, 820, 330, min(2, int(max(0.0, (t - C["10.c"] - 0.6) / 1.6))), 1.0)
    a1 = ep(t, C["11.a"], 0.5)
    if a1 > 0:
        pill(c, "TIME: um ajuda o outro", 1250, 330, GREEN, size=34, a=a1, anchor="center")
        linha(c, [("tempo ", INK), ("DIMINUI", GREEN)], 1250, 420, 48, a1)
    a2 = ep(t, C["11.b"], 0.5)
    if a2 > 0:
        linha(c, [("soma: frações por hora (", INK), ("vazões", GREEN), (")", INK)], 1250, 530, 36, a2)
        linha(c, [("nunca as horas", RED)], 1250, 590, 36, a2)
    a3 = ep(t, C["11.c"], 0.5)
    if a3 > 0:
        ex(c, "1/2 → 2/1 = 2", 1180, 720, 64, a3, {2: GREEN, 4: GREEN})
        text(c, "h", 1420, 742, 48, "black", GREEN, a3, align="left")
        pill(c, "de cabeça para baixo", 1250, 815, PURPLE, size=26, a=a3, anchor="center")


def b_atalho_prod(c, t, C, B):
    head(c, t, B["start"], "TEM ATALHO?", "PRODUTO SOBRE A SOMA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 230, 1320, 300, GREEN, aa, 0.08)
        text(c, "ATALHO · DUAS TORNEIRAS", W / 2, 280, 24, "black", GREEN, aa, tracking=2)
        text(c, "tempo juntas  =", 760, 420, 52, "black", INK, aa)
        fr(c, "t₁ · t₂", "t₁ + t₂", 1150, 400, 64, INK, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        fr(c, "6 · 3", "6 + 3", 720, 650, 60, INK, ab)
        text_mid(c, "=", 880, 650, 60, "black", INK, ab)
        fr(c, "18", "9", 1000, 650, 60, INK, ab)
        linha(c, [("= ", INK), ("2 h", GREEN)], 1200, 650, 64, ep(t, C["12.b"] + 3.0, 0.4))
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        selo(c, 1530, 700, acc, "SÓ DUAS DE CADA VEZ", AMBER, -6, 30)


# ======================================================================
# bloco e: torneira e ralo
# ======================================================================

def b_ralo(c, t, C, B):
    head_seq(c, t, C, [("13", "E SE ALGUÉM ATRAPALHAR?", "O RALO É UM SABOTADOR", RED),
                       ("14", "TORNEIRA E RALO", "PINTA 3, APAGA 2", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    ab = ep(t, C["13.b"], 0.5)
    torneira(c, 470, 260, aa, T1, 0.9, 1.0, 60)
    text(c, "4 h", 325, 218, 36, "black", T1, aa)
    # tanque 12 fatias; no 14.b: a cada hora +3 (verde) e depois −2 (vermelho)
    nivel, pint, apag = 0.0, 0.0, 0.0
    if t >= C["14.b"]:
        u = (t - C["14.b"] - 0.4) / 2.4
        if u >= 4:
            nivel = 4.0
        elif u > 0:
            k = int(u); f = u - k
            if f < 0.5:
                nivel, pint = float(k), 3 * ease_io(f / 0.5)
            else:
                g = ease_io((f - 0.5) / 0.5)
                nivel, apag = k + 3 - 2 * g, 2 * g
    tanque(c, 340, 330, 260, 450, 12, nivel, aa, rot=t >= C["14"], pintado=pint, apagado=apag)
    ralo(c, 470, 786, ab, 1.0, 0.0)
    text(c, "6 h", 560, 830, 40, "black", RED, ab, align="left")
    if t < C["14"]:
        if aa > 0:
            boxed(c, 820, 260, 800, 100, GREEN, aa)
            linha(c, [("VAZÃO DE ENTRADA", GREEN), (": a água que entra", INK)], 1220, 310, 32, aa)
        if ab > 0:
            boxed(c, 820, 390, 800, 100, RED, ab)
            linha(c, [("VAZÃO DE SAÍDA", RED), (": a água que sai pelo ralo", INK)], 1220, 440, 32, ab)
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            linha(c, [("ralo: a vazão dele ", INK), ("SUBTRAI", RED)], 1220, 570, 44, acc)
        ad = ep(t, C["13.d"], 0.5)
        ex(c, "1/4 - 1/6", 1220, 720, 80, ad, {0: GREEN, 2: RED})
        return
    a1 = ep(t, C["14.a"], 0.5)
    ex(c, "1/4 - 1/6 = 3/12 - 2/12", 1230, 330, 60, a1, {0: GREEN, 2: RED, 4: GREEN, 6: RED})
    a2 = ep(t, C["14.b"], 0.5)
    if a2 > 0:
        linha(c, [("a cada hora: ", INK), ("+3", GREEN), (" fatias  ", INK), ("−2", RED), (" fatias", INK)],
              1230, 470, 40, a2)
    a3 = ep(t, C["14.c"], 0.5)
    if a3 > 0:
        ex(c, "= 1/12", 1180, 600, 70, a3, {1: GREEN})
        text(c, "do tanque por hora", 1450, 615, 30, "bold", GRAY, a3)
    a4 = ep(t, C["14.d"], 0.5)
    if a4 > 0:
        linha(c, [("→ enche em ", INK), ("12 h", GREEN)], 1230, 760, 56, a4)


def b_ralo2(c, t, C, B):
    head(c, t, B["start"], "E SE O RALO FOSSE MAIS RÁPIDO?", "", RED)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        torneira(c, 430, 270, aa, T1, 0.8, 1.0, 50)
        ph = (t - C["15.a"]) % 2.0
        lv = 2.0 * (1 - ph / 2.0)
        tanque(c, 320, 340, 240, 380, 6, lv, aa, rot=False)
        ralo(c, 440, 726, aa, 1.3, 0.0)
        linha(c, [("sai > entra", RED)], 690, 760, 34, aa)
        check_icon(c, 620, 470, 36, aa, RED, "x")
        text(c, "nunca enche", 670, 482, 38, "black", RED, aa, align="left")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        boxed(c, 960, 260, 720, 520, GREEN, ab, 0.08)
        text(c, "ATALHO · TORNEIRA E RALO", 1320, 310, 24, "black", GREEN, ab, tracking=2)
        text(c, "produto sobre a diferença", 1320, 380, 40, "black", INK, ab)
        fr(c, "4 · 6", "6 − 4", 1120, 540, 60, INK, ab)
        text_mid(c, "=", 1260, 540, 60, "black", INK, ab)
        fr(c, "24", "2", 1370, 540, 60, INK, ab)
        linha(c, [("= ", INK), ("12 h", GREEN)], 1540, 540, 56, ab)
        conferido(c, "bateu", 1240, 710, ep(t, C["15.b"] + 5.0, 0.4), True, 36)


# ======================================================================
# bloco f: a conferência
# ======================================================================

def b_confere(c, t, C, B):
    head(c, t, B["start"], "A CONFERÊNCIA", "QUE PEGA O SINAL TROCADO", GREEN)
    card(c, *CARD_R)
    for k, (cue, tit, s, cmp_, stamp) in enumerate([
            ("16.a", "DUAS TORNEIRAS", "menor que a mais rápida sozinha", "2 h < 3 h", "TEMPO MENOR"),
            ("16.b", "COM RALO", "maior que a torneira sozinha", "12 h > 4 h", "TEMPO MAIOR")]):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 260 + k * 720
        rrect(c, x, 250 + d, 680, 400, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x + 340, 320 + d, 40, "black", PURPLE, a)
        text(c, s, x + 340, 390 + d, 30, "bold", INK2, a)
        text(c, cmp_, x + 340, 500 + d, 64, "black", INK, a)
        carimbo(c, stamp, x + 340, 595 + d, ep(t, C[cue] + 3.0, 0.4), 28)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        pill(c, "contrariou? você trocou o sinal (soma × subtração)", W / 2, 760, RED, size=32, a=acc, anchor="center")


# ======================================================================
# bloco g: Q = A · v
# ======================================================================

def b_qav(c, t, C, B):
    head(c, t, B["start"], "E NOS RIOS E CANOS?", "Q = A · v", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        cano(c, 820, 470, aa, ep(t, C["17.a"] + 0.5, 1.5))
        boxed(c, 1260, 360, 380, 220, PURPLE, aa)
        text(c, "Q = A · v", 1450, 480, 64, "black", PURPLE, aa)
        text(c, "área × velocidade", 1450, 545, 26, "bold", GRAY, aa)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        pill(c, "FÍSICA · por hoje, só saiba que existe", W / 2, 760, BLUE, size=32, a=ab, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "FATIAS POR HORA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 130, 24, "#F7F7F5", aa)
        linha(c, [("torneiras de ", INK), ("2 h", T1), (" e ", INK), ("6 h", T2), ("  →  juntas: ?", INK)], W / 2, 285, 52, aa)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 560)
    if t < C["19"]:
        return
    a1 = ep(t, C["19.a"], 0.5)
    ex(c, "1/2 + 1/6", 700, 450, 70, a1, {0: T1, 2: T2})
    a2 = ep(t, C["19.b"], 0.5)
    ex(c, "= 3/6 + 1/6 = 4/6 = 2/3", 1230, 450, 64, a2, {7: GREEN})
    text(c, "do tanque por hora", 1350, 540, 28, "bold", GRAY, a2)
    a3 = ep(t, C["19.c"], 0.5)
    if a3 > 0:
        ex(c, "2/3 → 3/2", 760, 660, 70, a3, {2: GREEN})
        linha(c, [("h = ", GREEN), ("1 h 30 min", GREEN)], 1180, 660, 60, a3)
    a4 = ep(t, C["19.d"], 0.5)
    if a4 > 0:
        carimbo(c, "TEMPO MENOR: 1,5 h < 2 h", W / 2, 790, a4, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Somam-se vazões, nunca tempos.",
          "Torneira soma, ralo subtrai.",
          "Com ajuda, o tempo diminui; com ralo, aumenta."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "36"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Somar os tempos: 6 h + 3 h = 9 h", "são dois números de horas, e \"juntas\" lembra soma",
          "mais ajuda não pode dar mais tempo: some as vazões"),
         ("Somar a vazão do ralo", "você acabou de aprender a somar as frações",
          "o ralo tira água: a vazão dele SUBTRAI"),
         ("Misturar L/min com horas", "a conta fecha e nenhum aviso aparece",
          "o resultado sai 60 vezes errado: padronize o tempo antes"),
         ("Esquecer o ÷ 24 de \"por dia\" para \"por hora\"", "já está em m³ e parece o fim",
          "faltou o tempo: 1 dia = 24 h, divida")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23", "24"], ERROS)


# ======================================================================
# questões
# ======================================================================

Q5 = ("Uma caixa-d'água com capacidade de 1 500 litros é abastecida por uma tubulação de vazão constante de 12,5 litros "
      "por minuto. Partindo da caixa vazia, o tempo necessário para enchê-la completamente é de")
ALTS5 = [("A", "1 hora", "só 750 L: meia caixa", RED), ("B", "1 hora e 30 minutos", "vizinha, sem conta", RED),
         ("C", "2 horas", "", GREEN), ("D", "2 horas e 30 minutos", "vizinha, sem conta", RED),
         ("E", "3 horas", "2 250 L: transborda", RED)]
Q9 = ("Uma cidade com 250 mil habitantes tem consumo médio de 180 litros de água por pessoa por dia. Para atender a essa "
      "demanda, o sistema de abastecimento precisa operar com vazão média, em metros cúbicos por hora, de")
ALTS9 = [("A", "187,5", "um zero a menos", RED), ("B", "1 875", "", GREEN), ("C", "18 750", "um zero a mais", RED),
         ("D", "45 000", "esqueceu o ÷ 24", AMBER), ("E", "1 080 000", "45 000 × 24: multiplicou", RED)]
Q6 = ("Uma torneira, sozinha, enche um tanque em 6 horas. Outra torneira, sozinha, enche o mesmo tanque em 3 horas. "
      "Abertas simultaneamente, as duas encherão o tanque em")
ALTS6 = [("A", "1 hora e 30 minutos", "duas iguais à de 3 h", RED), ("B", "2 horas", "", GREEN),
         ("C", "4 horas e 30 minutos", "média dos tempos", RED), ("D", "9 horas", "somou os tempos", AMBER),
         ("E", "18 horas", "multiplicou", RED)]
Q7 = ("Uma torneira enche um reservatório vazio em 4 horas. Um ralo, quando aberto, esvazia o reservatório cheio em "
      "6 horas. Com a torneira e o ralo abertos ao mesmo tempo, a partir do reservatório vazio, ele ficará cheio em")
ALTS7 = [("A", "2 horas", "impossível: menos que 4 h", RED), ("B", "5 horas", "média", RED),
         ("C", "10 horas", "somou os tempos", AMBER), ("D", "12 horas", "", GREEN), ("E", "24 horas", "multiplicou", RED)]


def _questao(c, t, C, sid_in, sid_res, sid_x, enun, alts, okL, titulo, sub, cor, ok_sid=None):
    head(c, t, C[sid_in], titulo, sub, cor)
    card(c, *CARD_R)
    a0 = ep(t, C[f"{sid_in}.a"], 0.4)
    yend = _enunciado(c, [(enun, INK)], a0, 240, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[sid_res], 0.3)),
         align="left")
    cues_in = {L: C[f"{sid_in}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in "ABCDE" if L != okL and f"{sid_x}.x{L.lower()}" in C}
    K.alternativas(c, t, C, alts, 1000, 250, 680, 40, C[f"{ok_sid or sid_res}.ok"], okL, cues_in, cues_x, gap=30)
    pause_timer(c, t, C[f"{sid_in}.end"] - 1.9, 1690, 790)
    return yend


def b_q5(c, t, C, B):
    yend = _questao(c, t, C, "25", "26", "26", Q5, ALTS5, "C", "QUESTÃO 5 · EU FAÇO", "RODADA 1 · VAZÃO DIRETA", BLUE)
    if t < C["26"]:
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["26"], 0.4))
    pill(c, "pede o TEMPO (o de baixo): divida ao contrário", 540, y0 + 40, PURPLE, size=20, a=ep(t, C["26"], 0.4),
         anchor="center")
    a1 = ep(t, C["26.a"], 0.4)
    if a1 > 0:
        fr(c, "1 500 L", "12,5 L/min", 380, y0 + 140, 34, INK, a1)
        linha(c, [("= 120 min", INK)], 650, y0 + 140, 36, ep(t, C["26.a"] + 3.0, 0.4))
    linha(c, [("= ", INK), ("2 h", GREEN)], 650, y0 + 220, 40, ep(t, C["26.b"], 0.4))


def b_q9(c, t, C, B):
    yend = _questao(c, t, C, "27", "28", "29", Q9, ALTS9, "B", "QUESTÃO 9 · NÓS FAZEMOS", "UMA CIDADE INTEIRA", BLUE)
    if t < C["28"]:
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["28"], 0.4))
    rows = [("28.a", "250 000 × 180 L = 45 000 000 L/dia", INK),
            ("28.b", "÷ 1 000 → 45 000 m³/dia", INK),
            ("28.c", "÷ 24 h → 1 875 m³/h", GREEN)]
    for k, (cue, s, col) in enumerate(rows):
        linha(c, [(s, col)], 540, y0 + 50 + k * 62, 27, ep(t, C[cue], 0.4))


def b_q6(c, t, C, B):
    yend = _questao(c, t, C, "30", "31", "32", Q6, ALTS6, "B", "QUESTÃO 6 · EU FAÇO", "RODADA 2 · FRAÇÕES DO TANQUE", PURPLE)
    if t < C["31"]:
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["31"], 0.4))
    ex(c, "1/6 + 2/6 = 3/6 = 1/2", 540, y0 + 70, 40, ep(t, C["31.a"], 0.4), {6: GREEN})
    linha(c, [("→ ", INK), ("2 h", GREEN)], 540, y0 + 160, 40, ep(t, C["31.b"], 0.4))
    carimbo(c, "TEMPO MENOR: 2 h < 3 h", 540, y0 + 240, ep(t, C["31.c"], 0.4), 24)


def b_q7(c, t, C, B):
    yend = _questao(c, t, C, "33", "34", "35", Q7, ALTS7, "D", "QUESTÃO 7 · VOCÊ FAZ", "TORNEIRA E RALO", GREEN)
    if t < C["34"]:
        return
    y0 = yend + 4
    _painel(c, y0, ep(t, C["34"], 0.4))
    ex(c, "1/4 - 1/6 = 3/12 - 2/12 = 1/12", 540, y0 + 60, 32, ep(t, C["34.a"], 0.4), {8: GREEN})
    linha(c, [("→ ", INK), ("12 h", GREEN)], 540, y0 + 140, 38, ep(t, C["34.b"], 0.4))
    carimbo(c, "TEMPO MAIOR: 12 h > 4 h", 540, y0 + 210, ep(t, C["34.c"], 0.4), 22)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "ÚLTIMO EPISÓDIO", "REVISÃO", PURPLE)
    aa = ep(t, C["37.a"], 0.5)
    for k, (s, col) in enumerate([("VELOCIDADE", BLUE), ("DENSIDADE", AMBER), ("VAZÃO", GREEN)]):
        chip(c, s, 520 + k * 440, 400, col, aa * ep(t, C["37.a"] + 0.8 * k, 0.4), 46, w=380)
    ab = ep(t, C["37.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 560, ab, "CAÇA ÀS PEGADINHAS", AMBER, -4, 40)
    acc = ep(t, C["37.c"], 0.5)
    if acc > 0:
        linha(c, [("Matemática", BLUE), ("  ·  ", GRAY), ("Física", PURPLE), ("  ·  ", GRAY), ("Geografia", GREEN)],
              W / 2, 730, 50, acc)


def b_cta(c, t, C, B):
    cta(c, t, C["38.like"], C["38.sub"], C["38.bell"], C["38.com"], C["38.bye"],
        "Você também pensou em 9 horas?", canal="no Estudativo", anki=C["38.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, **{"def": b_def}, caixa=b_caixa,
              atalho_div=b_atalho_div, fatias=b_fatias, duas=b_duas, atalho_prod=b_atalho_prod, ralo=b_ralo,
              ralo2=b_ralo2, confere=b_confere, qav=b_qav, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              q5=b_q5, q9=b_q9, q6=b_q6, q7=b_q7, ponte=b_ponte, cta=b_cta)
