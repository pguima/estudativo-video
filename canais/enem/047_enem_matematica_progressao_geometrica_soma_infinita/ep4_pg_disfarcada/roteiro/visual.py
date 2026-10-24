"""Visual — Progressão Geométrica, Episódio 4: a PG disfarçada (juros compostos, meia-vida e depreciação) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: maquina() (a máquina ×q do episódio 1), cofre(), frasco() e carro() (ícones), esteira() (uma linha
com o ícone, os valores passando pela máquina e o contador de períodos), barras() (queda ano a ano em barras, com a queda
linear tracejada por cima), regua_tempo() (o tempo total fatiado em períodos), linha() (texto com cor por trecho).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum047", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pg_ep4_pg_disfarcada.mp4"
CARD_R = K.CARD_R
COFRE = "#3E9A5B"    # juros compostos (cresce)
FRASCO = BLUE        # meia-vida
CARRO = "#C2503A"    # depreciação


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


def maquina(c, cx, cy, s, a, col=PURPLE, w=170, h=96, size=38):
    """a máquina ×q: caixa roxa com dois dentes em cima e o fator no visor"""
    if a <= 0:
        return
    for dx in (-0.25, 0.25):
        rrect(c, cx + dx * w - 14, cy - h / 2 - 16, 28, 22, 6, col, a)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 20, col, a)
    rrect(c, cx - w / 2 + 12, cy - h / 2 + 12, w - 24, h - 24, 12, "#FFFFFF", a * 0.95)
    text_mid(c, s, cx, cy, size, "black", col, a)


def cofre(c, cx, cy, s, a):
    """cofre verde com o disco do segredo"""
    if a <= 0:
        return
    rrect(c, cx - 0.5 * s, cy - 0.45 * s, s, 0.9 * s, 0.12 * s, COFRE, a)
    rrect(c, cx - 0.4 * s, cy - 0.35 * s, 0.8 * s, 0.7 * s, 0.08 * s, mix("#FFFFFF", COFRE, 0.35), a)
    c.drawCircle(cx - 0.05 * s, cy, 0.2 * s, paint("#FFFFFF", a))
    c.drawCircle(cx - 0.05 * s, cy, 0.2 * s, paint(COFRE, a, stroke=0.05 * s))
    line(c, cx - 0.05 * s, cy, cx + 0.08 * s, cy - 0.1 * s, COFRE, a, 0.05 * s)
    rrect(c, cx + 0.24 * s, cy - 0.12 * s, 0.08 * s, 0.24 * s, 0.03 * s, COFRE, a)


def frasco(c, cx, cy, s, a):
    """frasco de remédio azul com rótulo e tampa"""
    if a <= 0:
        return
    rrect(c, cx - 0.3 * s, cy - 0.5 * s, 0.6 * s, 0.18 * s, 0.05 * s, INK2, a)
    rrect(c, cx - 0.36 * s, cy - 0.34 * s, 0.72 * s, 0.84 * s, 0.12 * s, FRASCO, a)
    rrect(c, cx - 0.28 * s, cy - 0.12 * s, 0.56 * s, 0.36 * s, 0.05 * s, "#FFFFFF", a)
    rrect(c, cx - 0.04 * s, cy - 0.06 * s, 0.08 * s, 0.24 * s, 0.02 * s, FRASCO, a)
    rrect(c, cx - 0.12 * s, cy + 0.02 * s, 0.24 * s, 0.08 * s, 0.02 * s, FRASCO, a)


def carro(c, cx, cy, s, a, col=CARRO):
    """carro de perfil com duas rodas"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 0.3 * s, cy - 0.1 * s); p.lineTo(cx - 0.18 * s, cy - 0.34 * s)
    p.lineTo(cx + 0.2 * s, cy - 0.34 * s); p.lineTo(cx + 0.34 * s, cy - 0.1 * s); p.close()
    c.drawPath(p, paint(col, a))
    rrect(c, cx - 0.56 * s, cy - 0.12 * s, 1.12 * s, 0.32 * s, 0.1 * s, col, a)
    rrect(c, cx - 0.12 * s, cy - 0.29 * s, 0.24 * s, 0.17 * s, 0.03 * s, "#FFFFFF", a * 0.9)
    for dx in (-0.32, 0.32):
        c.drawCircle(cx + dx * s, cy + 0.22 * s, 0.13 * s, paint(INK, a))
        c.drawCircle(cx + dx * s, cy + 0.22 * s, 0.05 * s, paint("#FFFFFF", a))


ICONES = dict(cofre=cofre, frasco=frasco, carro=carro)


def esteira(c, x, y, icone, rot, fator, vals, u, col, a, w=1520, h=150, com_contador=True):
    """uma esteira: ícone, valor inicial, máquina, valor, máquina, valor e o contador de períodos.
    u = quantos períodos já passaram (0 a len(vals) − 1, contínuo)."""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, "#FFFFFF", a, shadow=True)
    ICONES[icone](c, x + 90, y + h / 2 - 12, 92, a)
    text(c, rot, x + 90, y + h - 14, 22, "black", col, a)
    cy = y + h / 2
    x0, passo = x + 330, 370
    for k, v in enumerate(vals):
        ak = a * clamp(u - k + 1) if k else a
        xv = x0 + k * passo
        if ak > 0:
            rrect(c, xv - 95, cy - 44, 190, 88, 18, mix("#FFFFFF", col, 0.14), ak)
            ftext(c, v, xv, cy + 15, 42, "black", col, ak)
        if k < len(vals) - 1:
            am = a * clamp(u - k + 0.6)
            xm = xv + passo / 2
            if am > 0:
                arrow(c, xv + 100, cy, xm - 92, cy, GRAY, am, 3, 10)
                maquina(c, xm, cy, fator, am, w=150, h=84, size=32)
                arrow(c, xm + 82, cy, xm + passo / 2 - 102, cy, GRAY, am, 3, 10)
    if com_contador:
        k = int(clamp(u, 0, len(vals) - 1) + 1e-6)
        xc = x + w - 110
        rrect(c, xc - 80, cy - 52, 160, 104, 18, mix("#FFFFFF", INK, 0.05), a)
        text(c, "períodos", xc, cy - 14, 20, "bold", GRAY, a)
        ftext(c, str(k), xc, cy + 38, 46, "black", INK, a)


def barras(c, x0, ybase, hmax, vals, vmax, n_vis, a, rots, col=CARRO, bw=110, gap=60, size=24, linear=None,
           a_lin=0.0, col_lin=AMBER, perdas=None, a_perdas=0.0):
    """queda ano a ano em barras; linear = valores da queda linear (tracejada por cima, com pontinhos)"""
    if a <= 0:
        return
    for k, v in enumerate(vals):
        ak = a * clamp(n_vis - k)
        if ak <= 0:
            continue
        x = x0 + k * (bw + gap)
        hh = v / vmax * hmax
        rrect(c, x, ybase - hh, bw, hh, 12, mix("#FFFFFF", col, 0.25 + 0.6 * (k == 0)), ak)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, ybase - hh, bw, hh), 12, 12), paint(col, ak, stroke=3))
        ftext(c, rots[k][0], x + bw / 2, ybase - hh - 14, size, "black", col, ak)
        text(c, rots[k][1], x + bw / 2, ybase + 32, size - 4, "bold", GRAY, ak)
    line(c, x0 - 20, ybase, x0 + len(vals) * (bw + gap) - gap + 20, ybase, INK2, a, 3)
    if perdas and a_perdas > 0:
        for k, s_ in enumerate(perdas):
            ak = a * a_perdas * clamp(n_vis - k - 1)
            x = x0 + (k + 1) * (bw + gap) + bw / 2
            hh = vals[k + 1] / vmax * hmax
            text(c, s_, x, ybase - hh - 58, size - 4, "black", RED, ak)
    if linear and a_lin > 0:
        pts = [(x0 + k * (bw + gap) + bw / 2, ybase - v / vmax * hmax) for k, v in enumerate(linear)]
        for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
            line(c, xa, ya, xb, yb, col_lin, a * a_lin, 4, dash=(12, 8))
        for k, (xp, yp) in enumerate(pts):
            c.drawCircle(xp, yp, 8, paint(col_lin, a * a_lin))


def regua_tempo(c, x, y, w, n, u, a, rot_seg="8 h", col=FRASCO):
    """o tempo total como uma régua fatiada em n períodos; u = quantos já acenderam (contínuo)"""
    if a <= 0:
        return
    sw = w / n
    for k in range(n):
        ak = clamp(u - k)
        rrect(c, x + k * sw + 4, y, sw - 8, 70, 14, mix("#FFFFFF", col, 0.12 + 0.5 * ak), a)
        text_mid(c, rot_seg, x + k * sw + sw / 2, y + 35, 26, "black", col if ak < 0.5 else "#FFFFFF", a)
        if ak > 0:
            badge_num(c, k + 1, x + k * sw + sw / 2, y + 110, a * ak, 22, bg=col)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROGRESSÃO GEOMÉTRICA · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        pill(c, "você já estudou PG sem saber", W / 2, 215, PURPLE, size=28, a=aa, anchor="center")
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        cofre(c, 290, 380, 120, ab)
        text(c, "dobra a cada 7 anos", 290, 490, 26, "black", COFRE, ab)
        vals = ["1", "2", "4", "8"]
        for k, v in enumerate(vals):
            ak = ep(t, C["01.b"] + 0.8 + k * 0.9, 0.4)
            x = 620 + k * 300
            rrect(c, x - 80, 320, 160, 120, 22, mix("#FFFFFF", COFRE, 0.16), ak)
            ftext(c, v, x, 400, 60, "black", COFRE, ak)
            text(c, f"{7 * k} anos", x, 480, 24, "bold", GRAY, ak)
            if k:
                text(c, "×2", x - 150, 360, 32, "black", PURPLE, ak)
        a2 = ep(t, C["01.b"] + 4.4, 0.5)
        if a2 > 0:
            linha(c, [("21 anos ÷ 7 = ", INK), ("3 períodos", PURPLE), ("   →   2³ = ", INK), ("8", GREEN)], 1070, 570,
                  40, a2)
            selo(c, 1520, 660, ep(t, C["01.b"] + 5.6, 0.4), "× 8, NÃO × 3", GREEN, -4, 34)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 220, 700, 1480, 110, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
        text(c, "a mesma máquina:", 470, 768, 32, "black", PURPLE, acc)
        for k, (ic, rot_) in enumerate((("frasco", "remédios"), ("cofre", "populações"), ("carro", "carros usados"))):
            x = 820 + k * 330
            ak = ep(t, C["01.c"] + 0.5 + k * 0.5, 0.4)
            ICONES[ic](c, x, 750, 62, ak)
            text(c, rot_, x + 50, 770, 24, "bold", INK2, ak, align="left")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "PROGRESSÃO GEOMÉTRICA · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de PROGRESSÃO GEOMÉTRICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "RECONHECER A PG", "em crescimento ou queda percentual", BLUE),
             ("02.b", "CONTAR OS PERÍODOS", "sem errar o expoente", PURPLE)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 640 + k * 640
        rrect(c, x - 290, 330, 580, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 290, 330, 580, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 26, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "série de Juros Compostos", COFRE), ("03.b", "série de Função Exponencial", FRASCO),
             ("03.c", "episódio 1", PURPLE)]
    for k, (cue, tag, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 280 + k * 190 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, tag, 300, y - 70, col, size=22, a=a)
        if k == 0:
            K.expr(c, "M = C · (1+i)^{t}", 700, y + 4, 54, a, cores={i: PURPLE for i in range(40)})
            linha(c, [("montante", BLUE), (" = o saldo final", INK)], 1290, y + 4, 34, a)
        elif k == 1:
            linha(c, [("MEIA-VIDA", BLUE), (" = o tempo para cair ", INK), ("à metade", BLUE)], 960, y + 4, 42, a)
        else:
            linha(c, [("do instante zero:  ", INK)], 760, y + 4, 38, a)
            K.expr(c, "a₀ · q^{t}", 1130, y + 4, 58, a, cores={i: PURPLE for i in range(40)})


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS COISAS DO DIA A DIA", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    cards = [("04.a", "EXTRATO DA POUPANÇA", COFRE, "cofre"), ("04.b", "BULA DO REMÉDIO", FRASCO, "frasco"),
             ("04.c", "CARRO USADO", CARRO, "carro")]
    for k, (cue, tit, col, ic) in enumerate(cards):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 220, 460, 420, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 220, 460, 64, 26, col, ak * 0.16)
        text(c, tit, x, 264, 26, "black", col, ak)
        ICONES[ic](c, x, 370, 110, ak)
        if k == 0:
            for j, s_ in enumerate(("jan  R$ 1.000,00", "fev  R$ 1.005,00", "mar  R$ 1.010,03")):
                text(c, s_, x, 480 + j * 44, 26, "bold", INK2, ak)
        elif k == 1:
            text(c, "MEIA-VIDA:", x, 500, 30, "black", INK2, ak)
            text(c, "8 horas", x, 560, 48, "black", FRASCO, ak)
        else:
            text(c, "VENDE-SE", x, 500, 34, "black", INK2, ak)
            text(c, "perde valor todo ano", x, 560, 26, "bold", CARRO, ak)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 690, 1320, 110, 22, mix("#FFFFFF", PURPLE, 0.12), ad)
        linha(c, [("a cada período: ", INK), ("× o MESMO número", PURPLE)], 960, 745, 42, ad)


# ======================================================================
# bloco a — a tabela da seção 08 (as esteiras)
# ======================================================================

def _u(t, t0, passo=1.0):
    return clamp((t - t0) / passo, 0, 2.0)


def b_maquinas(c, t, C, B):
    head(c, t, B["start"], "QUE MÁQUINA É ESSA?", "A MÁQUINA ×q DO EPISÓDIO 1", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        maquina(c, 960, 225, "×q", aa, w=150, h=70, size=34)
    rows = [("05.b", "cofre", "juros compostos", "×1,05", ["100", "105", "110,25"], COFRE, "1 + i"),
            ("05.c", "frasco", "meia-vida", "×1/2", ["100", "50", "25"], FRASCO, "1/2"),
            ("05.d", "carro", "depreciação", "×0,8", ["100", "80", "64"], CARRO, "1 − i")]
    for k, (cue, ic, rot_, fat, vals, col, q) in enumerate(rows):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        y = 290 + k * 170
        esteira(c, 200, y, ic, rot_, fat, vals, _u(t, C[cue] + 0.8, 1.2), col, ak, w=1380)
        pill(c, f"q = {q}", 1600, y + 75, col, size=26, a=ep(t, C[cue] + 3.0, 0.4), anchor="left", bounds=(0, 1920))
    ab = ep(t, C["05.b"] + 1.0, 0.5) * (1 - ep(t, C["05.c"], 0.3))
    if ab > 0:
        pill(c, "JUROS COMPOSTOS = juros sobre juros", W / 2, 800, BLUE, size=26, a=ab, anchor="center")
    ad = ep(t, C["05.d"] + 1.0, 0.5) * (1 - ep(t, C["05.e"], 0.3))
    if ad > 0:
        pill(c, "DEPRECIAÇÃO PERCENTUAL = perde uma % fixa por período", W / 2, 800, BLUE, size=26, a=ad,
             anchor="center")
    ae = ep(t, C["05.e"], 0.5)
    if ae > 0:
        pill(c, "população crescendo i% ao ano:  q = 1 + i", W / 2, 800, COFRE, size=28, a=ae, anchor="center")


def b_atalho_fator(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O FATOR É O QUE SOBRA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["06"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · ACHAR A MÁQUINA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        text_mid(c, "O FATOR É O QUE SOBRA", 960, 330, 56, "black", GREEN, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        cofre(c, 420, 470, 90, ab)
        linha(c, [("ganhou i%  →  fica com  ", INK), ("1 + i", COFRE)], 1000, 470, 46, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        carro(c, 420, 600, 100, acc)
        linha(c, [("perdeu i%  →  fica com  ", INK), ("1 − i", CARRO)], 1000, 600, 46, acc)
        a2 = ep(t, C["06.c"] + 2.4, 0.5)
        if a2 > 0:
            linha(c, [("perde 20%  →  fica com 80%  →  ", INK2), ("× 0,8", GREEN)], 960, 730, 40, a2)


# ======================================================================
# blocos b e c — meia-vida e contar períodos
# ======================================================================

def b_meiavida(c, t, C, B):
    head(c, t, B["start"], "E A MEIA-VIDA?", "REVISÃO · SÉRIE DE FUNÇÃO EXPONENCIAL", FRASCO)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        frasco(c, 300, 330, 120, aa)
        linha(c, [("80 g", FRASCO), ("  ·  meia-vida de ", INK), ("5 anos", FRASCO), ("  ·  em ", INK),
                   ("20 anos?", AMBER)], 1000, 330, 42, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 540, 400, 840, 90, 20, mix("#FFFFFF", PURPLE, 0.12), ab)
        linha(c, [("20 ÷ 5 = ", INK), ("4 meias-vidas", PURPLE)], 960, 445, 42, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        vals = ["80", "40", "20", "10", "5"]
        u = clamp((t - C["07.c"]) / 3.0) * 4
        for k, v in enumerate(vals):
            ak = acc * clamp(u - k + 1) if k else acc
            x = 380 + k * 290
            rrect(c, x - 80, 540, 160, 90, 18, mix("#FFFFFF", FRASCO, 0.14), ak)
            ftext(c, v + " g", x, 600, 40, "black", FRASCO, ak)
            if k:
                text(c, "×½", x - 145, 545, 28, "black", PURPLE, ak)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        s_ = "80 · (1/2)^{4} = 80/16 = 5"
        wx = K.math_w(s_, 50)
        K.expr(c, s_, 900, 740, 50, ad, cores={i: PURPLE for i in range(60)})
        text(c, "g", 900 + wx / 2 + 14, 758, 50, "black", PURPLE, ad, align="left")
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        check_icon(c, 1500, 735, 30, ae, GREEN)


def b_periodos(c, t, C, B):
    head(c, t, B["start"], "UNIDADES DIFERENTES?", "CONTE OS PERÍODOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        frasco(c, 300, 300, 110, aa)
        linha(c, [("meia-vida de ", INK), ("8 horas", FRASCO), ("  ·  em ", INK), ("2 dias", AMBER),
                   ("  ·  quantas?", INK)], 1000, 300, 42, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        ax = ab * (1 - ep(t, C["08.b"] + 2.2, 0.4))
        if ax > 0:
            linha(c, [("2 ÷ 8 ?", RED)], 560, 420, 44, ax)
            check_icon(c, 700, 412, 22, ax, RED, "x")
        a2 = ep(t, C["08.b"] + 2.0, 0.5)
        if a2 > 0:
            linha(c, [("2 dias = ", INK), ("48 horas", FRASCO)], 1200, 420, 44, a2)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        regua_tempo(c, 260, 500, 1400, 6, clamp((t - C["08.c"]) / 2.6) * 6, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 700, 1000, 100, 22, mix("#FFFFFF", PURPLE, 0.12), ad)
        linha(c, [("48 ÷ 8 = 6  →  ", INK), ("o expoente é 6", PURPLE)], 960, 750, 40, ad)


def b_atalho_periodos(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ANTES DE QUALQUER CONTA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 560, GREEN, a0, 0.08)
        text(c, "ATALHO · CONTE OS PERÍODOS", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        text_mid(c, "nº de períodos", 960, 350, 50, "black", INK, aa)
        text_mid(c, "=", 960, 420, 50, "black", GRAY, aa)
        text_mid(c, "tempo total ÷ duração de UM período", 960, 490, 46, "black", GREEN, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        pill(c, "sempre na MESMA unidade", W / 2, 600, AMBER, size=32, a=ab, anchor="center")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        selo(c, 960, 700, acc, "ESSE NÚMERO É O EXPOENTE", PURPLE, -3, 34)


# ======================================================================
# bloco d — percentual × linear; bloco e — termo ou soma
# ======================================================================

V40 = [40000, 30000, 22500, 16875]
L40 = [40000, 30000, 20000, 10000]


def b_linear(c, t, C, B):
    head(c, t, B["start"], "PERDE SEMPRE O MESMO VALOR?", "PERCENTUAL × LINEAR", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        carro(c, 290, 280, 110, aa)
        linha(c, [("R$ 40.000,00", CARRO), ("  ·  perde ", INK), ("25% ao ano", CARRO)], 820, 285, 40, aa)
    rots = [("40.000", "hoje"), ("30.000", "1 ano"), ("22.500", "2 anos"), ("16.875", "3 anos")]
    n_vis = 1.0
    if t >= C["10.b"]:
        n_vis = 1 + clamp((t - C["10.b"]) / 0.8)
    if t >= C["10.c"]:
        n_vis = 2 + clamp((t - C["10.c"]) / 0.8)
    if t >= C["10.e"]:
        n_vis = 3 + clamp((t - C["10.e"]) / 0.8)
    a_lin = ep(t, C["10.d"], 0.6)
    barras(c, 260, 760, 340, V40, 40000, n_vis, aa, rots, perdas=["−10.000", "−7.500", "−5.625"],
           a_perdas=1.0, linear=L40, a_lin=a_lin)
    if a_lin > 0:
        rrect(c, 1120, 380, 560, 150, 22, mix("#FFFFFF", AMBER, 0.16), a_lin)
        text(c, "tracejado: perder SEMPRE 10.000", 1400, 432, 24, "black", AMBER, a_lin)
        linha(c, [("queda linear = ", INK), ("PA", AMBER)], 1400, 488, 36, a_lin)
        text(c, "série de Função Afim", 1400, 560, 22, "bold", GRAY, a_lin)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        rrect(c, 1120, 600, 560, 150, 22, mix("#FFFFFF", PURPLE, 0.14), ae)
        text(c, "a porcentagem tira cada vez MENOS", 1400, 652, 24, "black", PURPLE, ae)
        linha(c, [("queda percentual = ", INK), ("PG", PURPLE)], 1400, 708, 36, ae)


def b_leitura(c, t, C, B):
    head(c, t, B["start"], "QUAL É A PERGUNTA?", "TERMO, SOMA FINITA OU INFINITA", BLUE)
    card(c, *CARD_R)
    itens = [("11.a", "QUANTO VALE NO FIM?", "TERMO", PURPLE), ("11.b", "QUANTO AO TODO?", "SOMA FINITA", BLUE),
             ("11.c", "SE CONTINUAR PARA SEMPRE?", "SOMA INFINITA", GREEN)]
    ad = ep(t, C["11.d"], 0.5)
    for k, (cue, perg, tipo, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        destaque = k == 0
        ak2 = ak * (1 - 0.6 * ad * (not destaque))
        rrect(c, x - 230, 260, 460, 380, 26, "#FFFFFF", ak2, shadow=True)
        if destaque and ad > 0:
            K.boxed(c, x - 236, 254, 472, 392, PURPLE, ad, 0.0, 28, 6)
        for j, ln in enumerate(K.wrap(perg, "black", 34, 400)):
            text(c, ln, x, 350 + j * 46, 34, "black", INK2, ak2)
        rrect(c, x - 190, 500, 380, 96, 20, mix("#FFFFFF", col, 0.18), ak2)
        text_mid(c, tipo, x, 548, 40, "black", col, ak2)
    if ad > 0:
        pill(c, "juros, remédio e carro: quase sempre TERMO", W / 2, 730, PURPLE, size=30, a=ad, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("12", "SUA VEZ", "PAUSE E TENTE", GREEN), ("13", "VAMOS JUNTOS", "O FATOR É O QUE SOBRA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        carro(c, 300, 300, 120, aa)
        linha(c, [("R$ 50.000,00", CARRO), ("  ·  perde ", INK), ("10% ao ano", CARRO)], 880, 300, 44, aa)
    if t < C["13"]:
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            linha(c, [("razão q = ?", PURPLE), ("      valor em 2 anos = ?", AMBER)], 960, 460, 46, ab)
        pause_timer(c, t, C["12.end"] - 1.9, 960, 640)
        return
    a1 = ep(t, C["13.a"], 0.5)
    if a1 > 0:
        linha(c, [("perde 10%  →  fica com 90%  →  ", INK), ("q = 0,9", PURPLE)], 960, 440, 44, a1)
    a2 = ep(t, C["13.b"], 0.5)
    if a2 > 0:
        linha(c, [("2 anos = ", INK), ("2 períodos", PURPLE), ("   →   0,9² = ", INK), ("0,81", PURPLE)], 960, 560, 44,
              a2)
    a3 = ep(t, C["13.c"], 0.5)
    if a3 > 0:
        rrect(c, 380, 640, 1160, 120, 22, mix("#FFFFFF", GREEN, 0.14), a3)
        linha(c, [("50.000 · 0,81 = ", INK), ("R$ 40.500,00", GREEN)], 960, 700, 50, a3)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Porcentagem fixa por período é PG.",
          "Conte os períodos: tempo total dividido pela duração de um período.",
          "O fator é o que sobra: perder 20% é multiplicar por 0,8."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "21"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Usar a TAXA no lugar do FATOR (q = 0,1 para \"perde 10%\")", "é o número que está no enunciado",
          "50.000 · 0,1² = R$ 500,00, absurdo: use o que sobra, q = 0,9"),
         ("Tratar a queda percentual como LINEAR", "no primeiro ano a perda é mesmo 5.000",
          "tirar 5.000 duas vezes dá 40.000; o certo é 40.500: no 2º ano a perda é menor"),
         ("Contar UM PERÍODO a mais ou a menos", "a gente conta os momentos, e não os intervalos",
          "meia-vida de 8 h em 2 dias: 48 ÷ 8 = 6, nem 5 nem 7")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["15", "16", "17"], ERROS)


# ======================================================================
# questão nova (você faz)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS = [("A", "R$ 640,00.", "taxa como fator: 0,2³", RED), ("B", "R$ 32.000,00.", "linear: −16.000 por ano", RED),
        ("C", "R$ 40.960,00.", "", GREEN), ("D", "R$ 51.200,00.", "n − 1: parou em 2 anos", RED),
        ("E", "R$ 64.000,00.", "a queda uma vez só", RED)]
V80 = [80000, 64000, 51200, 40960]
L80 = [80000, 64000, 48000, 32000]


def b_q(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO NOVA · VOCÊ FAZ", "DEPRECIAÇÃO PERCENTUAL", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["18.a"], 0.4)
    yend = _enunciado(c, [("Um carro novo custa R$ 80.000,00 e, segundo uma projeção, perde 20% do seu valor a cada "
                           "ano, sempre em relação ao valor do ano anterior. Três anos após a compra, o valor projetado "
                           "do carro será de", INK)], a0, 250, 30)
    cues_in = {L: C[f"18.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"20.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS, 1000, 260, 680, 34, C["19.ok"], "C", cues_in, cues_x, gap=34)
    if t < C["19"]:
        pause_timer(c, t, C["18.end"] - 1.9, 540, yend + 110)
        return
    y0 = 206
    a1 = ep(t, C["19"], 0.4)
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a1, shadow=True)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        linha(c, [("q = 1 − 0,2 = ", INK), ("0,8", PURPLE)], 540, y0 + 50, 36, aa)
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        linha(c, [("3 anos = ", INK), ("3 períodos", PURPLE), (" (do instante zero)", INK2)], 540, y0 + 110, 30, ab)
    acc = ep(t, C["19.c"], 0.5)
    if acc > 0:
        linha(c, [("80.000 · 0,8³ = 80.000 · 0,512", INK)], 540, y0 + 170, 30, acc)
        linha(c, [("= R$ 40.960,00", GREEN)], 540, y0 + 222, 36, acc)
    ad = ep(t, C["19.d"], 0.5)
    rots = [("80.000", "hoje"), ("64.000", "1 ano"), ("51.200", "2 anos"), ("40.960", "3 anos")]
    a_lin = ep(t, C["20.xb"], 0.6)
    barras(c, 225, 760, 270, V80, 80000, clamp((t - C["19.d"]) / 2.4) * 4 if ad > 0 else 0, ad, rots, bw=120, gap=52,
           size=22, linear=L80, a_lin=a_lin)
    if a_lin > 0:
        text(c, "linear (B): 32.000", 880, y0 + 300, 22, "black", AMBER, a_lin, align="right")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DA PG", PURPLE)
    itens = [("22.a", "JUNTAMOS TUDO", PURPLE), ("22.b", "CAÇAMOS AS PEGADINHAS", AMBER), ("22.c", "TREINO PARA O ENEM", GREEN)]
    for k, (cue, s_, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 300, 460, 260, 26, mix("#FFFFFF", col, 0.12), ak)
        badge_num(c, k + 1, x, 380, ak, 34, bg=col)
        text(c, s_, x, 490, 32, "black", col, ak)
    ac = ep(t, C["22.c"] + 1.2, 0.5)
    if ac > 0:
        selo(c, W / 2, 700, ac, "ÚLTIMO EPISÓDIO DO ASSUNTO", AMBER, -3, 38)


def b_cta(c, t, C, B):
    cta(c, t, C["23.like"], C["23.sub"], C["23.bell"], C["23.com"], C["23.bye"],
        "Em que outro lugar do seu dia a dia você já viu essa máquina de multiplicar?", canal="no Estudativo",
        anki=C["23.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, maquinas=b_maquinas,
              atalho_fator=b_atalho_fator, meiavida=b_meiavida, periodos=b_periodos,
              atalho_periodos=b_atalho_periodos, linear=b_linear, leitura=b_leitura, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q=b_q, ponte=b_ponte, cta=b_cta)
