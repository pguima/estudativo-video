"""Visual — Equação do 2º grau, Episódio 1: o método de Po-Shen Loh (média ± u) (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica/resultado · vermelho = erro.
Reaproveita a série 015 (ep. 4 → ftext/fbox/regra do 010 ep1, alternativas e helpers do 014).
Símbolos usados (², √, ±, ≠, ·, −, ≈, Δ, ✓) existem na Inter: nada cai na fonte reserva da Segoe.
Peças próprias deste episódio:
- reta(): reta numérica com marcas inteiras.
- gangorra(): a analogia âncora — a média é o apoio do meio; as duas raízes são duas crianças à mesma distância u.
  u anima (cresce, encolhe, vira 0 na raiz dupla; some com "?" quando u² é negativo).
- passos(): as contas linha a linha, cada uma aparecendo quando é dita.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_ROOT = Path(__file__).resolve().parents[3]          # canais/enem


def _load(nome, rel):
    sp = importlib.util.spec_from_file_location(nome, _ROOT / rel)
    mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    return mod


V4 = _load("v015_ep4", "015_enem_matematica_divisibilidade/ep4_mmc/roteiro/visual.py")
motor.set_theme("claro")
M, V1 = V4.M, V4.V1

ftext, fmid, ftext_w, fbox, regra = M.ftext, M.fmid, M.ftext_w, M.fbox, M.regra
pause_timer, which, para, wrap, frame, head_seq, boxed, selo = (V1.pause_timer, V1.which, V1.para, V1.wrap, V1.frame,
                                                                 V1.head_seq, V1.boxed, V1.selo)
alts_panel = V4.alts_panel

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_po_shen_loh_ep1_metodo.mp4"
CARD_R = (140, 150, 1640, 690)

KID_A, KID_B = "#3B6CF6", "#F97316"     # as duas "crianças" (raízes)
MADEIRA = "#C8955C"


def nf(v):
    """número no formato brasileiro: vírgula decimal e sinal de menos tipográfico"""
    s = f"{v:.2f}".rstrip("0").rstrip(".") if abs(v - round(v)) > 1e-9 else str(int(round(v)))
    return s.replace("-", "−").replace(".", ",")


def passo(t, C, cue):
    return ep(t, C[cue], 0.45)


def linhas(c, t, C, rows, x, y, size=40, dy=66, align="left"):
    """rows = [(cue, texto, cor)] — cada conta entra quando é dita (subindo um pouco)"""
    for k, (cue, s, col) in enumerate(rows):
        if cue is None:
            continue
        a, d = rise(t, C[cue])
        fmid(c, s, x, y + k * dy + d, size, "black", col, a, align=align)


# ======================================================================
# reta numérica e gangorra
# ======================================================================

def reta(c, x0, x1, y, v0, v1, a=1.0, step=1, lab=26, hide=()):
    if a <= 0:
        return None
    X = lambda v: x0 + (x1 - x0) * (v - v0) / (v1 - v0)
    line(c, x0 - 20, y, x1 + 20, y, INK2, a, 3)
    n = round((v1 - v0) / step)
    for k in range(n + 1):
        v = v0 + k * step
        inteiro = abs(v - round(v)) < 1e-9
        line(c, X(v), y - (9 if inteiro else 6), X(v), y + (9 if inteiro else 6), INK2, a, 2.5)
        if not any(abs(v - h) < 1e-9 for h in hide):
            text(c, nf(v), X(v), y + 44, lab if inteiro else lab - 4, "bold", GRAY, a)
    return X


def crianca(c, x, y, col, a, s=1.0):
    """criança sentada (cabeça + corpo) com o 'assento' em y"""
    if a <= 0:
        return
    rrect(c, x - 17 * s, y - 46 * s, 34 * s, 44 * s, 12 * s, col, a, shadow=True)
    c.drawCircle(x, y - 64 * s, 17 * s, paint(mix(col, "#FFFFFF", 0.35), a))
    c.drawCircle(x, y - 64 * s, 17 * s, paint(col, a, stroke=3))


def gangorra(c, X, y, m, u, a=1.0, kids=1.0, show_u=0.0, show_val=0.0, show_m=0.0, col_ok=None, labels=None,
             sumir=0.0, h=110, s=1.3):
    """X = função da reta · y = altura da reta · gangorra com apoio em m e crianças em m − u e m + u.
    show_u: setas com 'u' · show_val: valores das raízes na reta · show_m: rótulo 'média' · sumir: crianças somem com '?'
    labels: textos das raízes (padrão: os números)."""
    if a <= 0:
        return
    yp = y - h                                  # altura da tábua
    xm = X(m)
    # apoio
    p = skia.Path(); p.moveTo(xm, yp + 6); p.lineTo(xm - 34, y - 6); p.lineTo(xm + 34, y - 6); p.close()
    c.drawPath(p, paint(PURPLE, a))
    xa, xb = X(m - u), X(m + u)
    if abs(xb - xa) < 30:                       # u ≈ 0: as duas juntas no meio
        xa, xb = xm - 15 + (xa - xm), xm + 15 + (xb - xm)
    # tábua
    rrect(c, min(xa, xm - 40) - 34, yp - 6, max(xb, xm + 40) - min(xa, xm - 40) + 68, 14, 6, MADEIRA, a, shadow=True)
    ak = a * kids * (1 - sumir)
    crianca(c, xa, yp - 6, KID_A, ak, s)
    crianca(c, xb, yp - 6, KID_B, ak, s)
    if sumir > 0:
        for xx in (xa, xb):
            text(c, "?", xx, yp - 30, 72, "black", RED, a * sumir)
    # média
    if show_m > 0:
        c.drawCircle(xm, y, 11, paint(PURPLE, a * show_m))
        pill(c, "média", xm, y + 156, PURPLE, size=22, a=a * show_m, anchor="center", bounds=(0, 1920))
    # setas u
    if show_u > 0 and xb - xa > 90:
        yy = y - h * 0.28
        for x0, x1 in ((xm - 30, xa + 6), (xm + 30, xb - 6)):
            if abs(x1 - x0) > 24:
                arrow(c, x0, yy, x1, yy, PURPLE, a * show_u, 3.5, 12)
        text_mid(c, "u", (xm + xa) / 2 - 10, yy - 26, 34, "black", PURPLE, a * show_u)
        text_mid(c, "u", (xm + xb) / 2 + 10, yy - 26, 34, "black", PURPLE, a * show_u)
    # valores das raízes
    if show_val > 0:
        for xx, v, col, k in ((xa, m - u, KID_A, 0), (xb, m + u, KID_B, 1)):
            line(c, xx, yp + 8, xx, y - 4, col, a * show_val, 2.5, dash=(6, 6))
            c.drawCircle(xx, y, 12, paint(col_ok or col, a * show_val))
            s = labels[k] if labels else nf(v)
            if abs(xb - xa) < 40 and k == 1:
                continue
            fbox(c, s, xx, y + 100, 34, a * show_val, col_ok or col)


# ======================================================================
# abertura
# ======================================================================

def bhaskara_formula(c, cx, cy, a, size=44, col=None):
    """x = (−b ± √Δ) / 2a desenhada com fração"""
    if a <= 0:
        return
    col = col or INK
    fmid(c, "x =", cx - 150, cy, size, "black", col, a)
    w = text_w("−b ± √Δ", "black", size) + 20
    text(c, "−b ± √Δ", cx + 40, cy - 14, size, "black", col, a)
    line(c, cx + 40 - w / 2, cy + 2, cx + 40 + w / 2, cy + 2, col, a, 4, cap_round=False)
    text(c, "2a", cx + 40, cy + size + 16, size, "black", col, a)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EQUAÇÃO DO 2º GRAU SEM BHASKARA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    pill(c, "SOMA = 8", 520, 260, BLUE, size=40, a=aa, anchor="center")
    pill(c, "PRODUTO = 12", 520, 360, BLUE, size=40, a=ep(t, C["01.a"] + 0.9, 0.4), anchor="center")
    ab = ep(t, C["01.b"], 0.4)
    fmid(c, "? e ?", 520, 480, 70, "black", GRAY, ep(t, C["01.a"] + 1.6, 0.4) * (1 - ab))
    fbox(c, "2 e 6", 520, 480, 64, ab, GREEN)
    X = reta(c, 1000, 1560, 700, 0, 8, ep(t, C["01.b"], 0.5))
    if X:
        gangorra(c, X, 700, 4, 2, ab, show_val=ep(t, C["01.b"] + 0.6, 0.4), h=110)
    fbox(c, "x² − 8x + 12 = 0", 1280, 280, 52, ep(t, C["01.c"], 0.5), PURPLE)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        bhaskara_formula(c, 520, 640, ad, 40, GRAY)
        line(c, 320, 690, 720, 590, RED, ad, 7, progress=ep(t, C["01.d"] + 0.9, 0.5))
        text(c, "sem decorar", 520, 790, 32, "black", RED, ep(t, C["01.d"] + 0.9, 0.4))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "1 · achar as raízes em 3 PASSOS curtos"), ("02.b", "2 · entender DE ONDE vem cada passo")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 190 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 56, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    sid = which(t, C, ["03", "04"])
    head_seq(c, t, C, [("03", "LEMBRANDO", "EQUAÇÃO DO 2º GRAU E RAIZ", BLUE), ("04", "LEMBRANDO", "OS NÚMEROS b E c", BLUE)])
    card(c, *CARD_R)
    if sid == "03":
        aa = ep(t, C["03.a"], 0.5)
        boxed(c, 220, 200, 700, 150, BLUE, aa, 0.07)
        text(c, "EQUAÇÃO DO 2º GRAU", 250, 240, 20, "black", BLUE, aa, align="left", tracking=2)
        text(c, "tem x², e nenhuma potência maior", 250, 300, 34, "black", INK, aa, align="left")
        fbox(c, "x² − 8x + 12 = 0", 1300, 275, 56, ep(t, C["03.b"], 0.5), INK)
        ac = ep(t, C["03.c"], 0.5)
        boxed(c, 220, 400, 700, 150, BLUE, ac, 0.07)
        text(c, "RAIZ", 250, 440, 20, "black", BLUE, ac, align="left", tracking=2)
        text(c, "o número que ZERA a conta", 250, 500, 34, "black", INK, ac, align="left")
        pill(c, "teste x = 2", 1300, 420, AMBER, size=28, a=ep(t, C["03.d"], 0.4), anchor="center")
        fmid(c, "2² − 8 · 2 + 12", 1300, 510, 48, "black", INK, ep(t, C["03.d"], 0.4))
        fmid(c, "= 4 − 16 + 12 = 0", 1300, 590, 48, "black", INK, ep(t, C["03.e"], 0.4))
        af = ep(t, C["03.f"], 0.4)
        fbox(c, "2 é raiz ✓", 1300, 720, 50, af, GREEN)
        return
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        size = 80
        parts = [("x²", INK), (" + ", INK), ("b", BLUE), ("x", INK), (" + ", INK), ("c", PURPLE), (" = 0", INK)]
        w = sum(ftext_w(s, "black", size) for s, _ in parts)
        x = W / 2 - w / 2
        for s, col in parts:
            ftext(c, s, x, 300, size, "black", col, aa, align="left")
            x += ftext_w(s, "black", size)
    pill(c, "b = o número que acompanha o x, COM o sinal", 560, 400, BLUE, size=28, a=ep(t, C["04.b"], 0.4), anchor="center")
    pill(c, "c = o número sozinho", 1360, 400, PURPLE, size=28, a=ep(t, C["04.c"], 0.4), anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        fmid(c, "x² − 8x + 12 = 0", 560, 520, 50, "black", INK, ad)
        fmid(c, "b = −8    c = 12", 1360, 520, 50, "black", INK, ad)
        fmid(c, "b = −8", 1360 - ftext_w("b = −8    c = 12", "black", 50) / 2, 520, 50, "black", BLUE, ad, align="left")
    ae = ep(t, C["04.e"], 0.5)
    boxed(c, 300, 610, 1320, 190, AMBER, ae, 0.08)
    text(c, "CUIDADO: RAIZ QUADRADA É OUTRA COISA", 340, 650, 20, "black", AMBER, ae, align="left", tracking=2)
    text(c, "o número que, ao quadrado, dá o valor", 340, 712, 34, "black", INK, ae, align="left")
    fmid(c, "√4 = 2,  porque 2² = 4", 1250, 700, 46, "black", AMBER, ep(t, C["04.f"], 0.4))


# ======================================================================
# bloco A: de onde vêm a soma e o produto
# ======================================================================

def b_fatores(c, t, C, B):
    sid = which(t, C, ["05", "06", "07"])
    head_seq(c, t, C, [("05", "POR QUE SOMA E PRODUTO?", "O PRODUTO QUE DÁ ZERO", BLUE),
                       ("06", "MULTIPLICANDO TUDO", "VOLTA A EQUAÇÃO", PURPLE),
                       ("07", "VALE SEMPRE", "SOMA E PRODUTO DAS RAÍZES", PURPLE)])
    card(c, *CARD_R)
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        fmid(c, "(x − 2) · (x − 6) = 0", W / 2, 270, 70, "black", INK, aa)
        for cue, x, s1, s2 in (("05.b", 560, "x = 2", "(2 − 2) · (2 − 6)"), ("05.c", 1360, "x = 6", "(6 − 2) · (6 − 6)")):
            a, d = rise(t, C[cue])
            pill(c, s1, x, 400 + d, AMBER, size=30, a=a, anchor="center")
            fmid(c, s2, x, 490 + d, 44, "black", INK, a)
            fmid(c, "0 · (−4) = 0" if x < W / 2 else "4 · 0 = 0", x, 570 + d, 44, "black", GREEN, a)
        regra(c, "zero vezes qualquer coisa = zero", W / 2, 690, ep(t, C["05.d"], 0.5), 40)
        fbox(c, "raízes: 2 e 6", W / 2, 790, 40, ep(t, C["05.e"], 0.4), GREEN)
        return
    if sid == "06":
        a0 = ep(t, C["06.t"], 0.5)
        fmid(c, "(x − 2) · (x − 6)", W / 2, 260, 64, "black", INK, a0)
        rows = [("06.a", "x · x = x²", BLUE), ("06.b", "− 6x − 2x = − 8x", PURPLE), ("06.c", "(−2) · (−6) = + 12", GREEN)]
        linhas(c, t, C, rows, W / 2, 370, 46, 72, align="center")
        fbox(c, "x² − 8x + 12", W / 2, 620, 60, ep(t, C["06.d"], 0.5), INK)
        pill(c, "8 = 2 + 6  (SOMA)", 560, 760, BLUE, size=32, a=ep(t, C["06.e"], 0.4), anchor="center")
        pill(c, "12 = 2 · 6  (PRODUTO)", 1360, 760, BLUE, size=32, a=ep(t, C["06.f"], 0.4), anchor="center")
        return
    fmid(c, "x² + bx + c = 0", W / 2, 260, 64, "black", INK, ep(t, C["07.a"], 0.5))
    regra(c, "SOMA das raízes = −b", 560, 420, ep(t, C["07.b"], 0.5), 46, PURPLE, 640)
    text(c, "o b com o sinal trocado", 560, 510, 28, "bold", PURPLE, ep(t, C["07.b"] + 0.8, 0.4))
    regra(c, "PRODUTO das raízes = c", 1360, 420, ep(t, C["07.c"], 0.5), 46, PURPLE, 640)
    ad = ep(t, C["07.d"], 0.5)
    fmid(c, "b = −8  →  soma = 8", 560, 660, 46, "black", INK, ad)
    fmid(c, "c = 12  →  produto = 12", 1360, 660, 46, "black", INK, ad)


# ======================================================================
# bloco B: a gangorra (analogia âncora)
# ======================================================================

PARES = [("08.c", 1), ("08.d", 2), ("08.e", 3)]


def b_gangorra(c, t, C, B):
    sid = which(t, C, ["08", "09", "10"])
    head_seq(c, t, C, [("08", "A IDEIA GENIAL", "UMA GANGORRA EQUILIBRADA", BLUE),
                       ("09", "O MEIO DA GANGORRA", "MÉDIA E DISTÂNCIA u", BLUE),
                       ("10", "QUEM DIZ O u?", "O PRODUTO", PURPLE)])
    card(c, *CARD_R)
    if sid == "08":
        X = reta(c, 380, 1540, 700, 0, 8, ep(t, C["08.a"], 0.5))
        u = 2.0
        for k, (cue, uu) in enumerate(PARES):
            if t >= C[cue] - 0.3:
                u_prev = PARES[k - 1][1] if k else 2.0
                u = lerp(u_prev, uu, ease_io(prog(t, C[cue] - 0.3, 0.6)))
        gangorra(c, X, 700, 4, u, ep(t, C["08.a"], 0.5), show_val=ep(t, C["08.c"], 0.4), h=140)
        text(c, "mesma distância do meio", W / 2, 260, 34, "black", BLUE, ep(t, C["08.a"] + 1.2, 0.4))
        ab = ep(t, C["08.b"], 0.4)
        pill(c, "soma = 8", 300, 300, BLUE, size=30, a=ab, bounds=(0, 1920))
        atual = max([uu for cue, uu in PARES if t >= C[cue] - 0.3], default=None)
        for k, (cue, uu) in enumerate(PARES):
            a, d = rise(t, C[cue])
            text(c, f"{4 - uu} + {4 + uu} = 8", 1640, 300 + k * 56 + d, 34, "black", GREEN if uu == atual else GRAY, a, align="right")
        af = ep(t, C["08.f"], 0.4)
        if af > 0:
            c.drawCircle(X(4), 700, 16, paint(PURPLE, af))
            pill(c, "o meio: 4", X(4), 800, PURPLE, size=28, a=af, anchor="center", bounds=(0, 1920))
        return
    if sid == "09":
        X = reta(c, 260, 1060, 630, 0, 8, 1.0)
        gangorra(c, X, 630, 4, 2, 1.0, show_u=ep(t, C["09.c"], 0.4), show_m=ep(t, C["09.t"], 0.4), h=170,
                 show_val=ep(t, C["09.d"], 0.4), labels=["m − u", "m + u"])
        fmid(c, "MÉDIA = soma ÷ 2", 1420, 260, 40, "black", BLUE, ep(t, C["09.t"], 0.4))
        fmid(c, "8 ÷ 2 = 4", 1420, 330, 44, "black", INK, ep(t, C["09.a"], 0.4))
        regra(c, "m = −b/2", 1420, 440, ep(t, C["09.b"], 0.5), 50, PURPLE, 400)
        pill(c, "u = distância de cada raiz até o meio", 1420, 545, BLUE, size=24, a=ep(t, C["09.c"], 0.4), anchor="center",
             bounds=(0, 1920))
        fmid(c, "raízes:", 1420, 640, 32, "bold", GRAY, ep(t, C["09.d"], 0.4))
        fmid(c, "m − u   e   m + u", 1420, 710, 50, "black", GREEN, ep(t, C["09.d"], 0.4))
        return
    # cena 10: o produto
    rows = [("10.a", "(4 − u) · (4 + u) = 12", INK), ("10.b", "16 + 4u − 4u − u² = 12", INK),
            ("10.c", "16 − u² = 12", INK), ("10.d", "u² = 4", PURPLE), ("10.e", "u = 2", GREEN)]
    linhas(c, t, C, rows, 220, 250, 44, 88)
    ab = ep(t, C["10.b"] + 0.9, 0.4)
    if ab > 0:   # os termos do meio se cancelam
        x0 = 220 + ftext_w("16 + ", "black", 44)
        x1 = 220 + ftext_w("16 + 4u − 4u", "black", 44)
        line(c, x0 - 4, 338 + 14, x1 + 4, 338 - 18, RED, ab, 5, progress=ab)
        text(c, "se cancelam", (x0 + x1) / 2, 384, 22, "black", RED, ab)
    X = reta(c, 1000, 1600, 700, 0, 8, ep(t, C["10.t"], 0.5), hide=(2, 6) if t >= C["10.f"] else ())
    if X:
        u = 2 if t >= C["10.e"] else 2 + 0.9 * math.sin(2.2 * (t - C["10.t"]))
        gangorra(c, X, 700, 4, u, ep(t, C["10.t"], 0.5), show_val=ep(t, C["10.f"], 0.4), col_ok=GREEN, h=150)
        if t < C["10.e"]:
            text(c, "u = ?", 1300, 300, 40, "black", PURPLE, ep(t, C["10.t"], 0.4))
        else:
            fbox(c, "4 − 2 = 2   e   4 + 2 = 6", 1300, 300, 36, ep(t, C["10.f"], 0.4), GREEN)


# ======================================================================
# crédito
# ======================================================================

def tabuleta(c, x, y, a, s=1.0):
    """tabuleta de argila com marcas em cunha (ilustração da Babilônia)"""
    if a <= 0:
        return
    rrect(c, x, y, 220 * s, 150 * s, 26 * s, "#D9B98C", a, shadow=True)
    for r in range(4):
        for k in range(5 - r % 2):
            px, py = x + (28 + k * 38 + (r % 2) * 18) * s, y + (30 + r * 30) * s
            p = skia.Path(); p.moveTo(px, py); p.lineTo(px + 18 * s, py + 5 * s); p.lineTo(px, py + 12 * s); p.close()
            c.drawPath(p, paint("#9C7A4E", a))


def b_credito(c, t, C, B):
    frame(c, t, B["start"], "DE ONDE VEM O MÉTODO", "PO-SHEN LOH", BLUE)
    a0 = ep(t, C["11.t"], 0.5)
    text(c, "PO-SHEN LOH", 250, 280, 72, "black", INK, a0, align="left")
    text(c, "professor de Matemática da Carnegie Mellon (EUA)", 250, 345, 32, "bold", INK2, a0, align="left")
    rows = [("11.a", "foi técnico da seleção dos EUA na Olimpíada Internacional de Matemática"),
            ("11.b", "divulgou o método em 2019")]
    for k, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        check_icon(c, 270, 440 + k * 80 + d - 12, 22, a, BLUE)
        text(c, s, 310, 440 + k * 80 + d, 32, "black", INK, a, align="left")
    ac = ep(t, C["11.c"], 0.5)
    tabuleta(c, 1200, 600, ac, 1.3)
    pill(c, "ideia antiga: os BABILÔNIOS, há milhares de anos", 700, 700, AMBER, size=32, a=ac, anchor="center")


# ======================================================================
# a receita
# ======================================================================

RECEITA = [("12.z", "0", "x² sozinho: divida tudo pelo número da frente", AMBER),
           ("12.a", "1", "média:  m = −b/2", PURPLE),
           ("12.b", "2", "u² = m² − c   →   u = √u²", PURPLE),
           ("12.c", "3", "raízes:  m − u   e   m + u", GREEN)]


def b_receita(c, t, C, B):
    frame(c, t, B["start"], "A RECEITA", "EM 3 PASSOS", PURPLE)
    for k, (cue, n, s, col) in enumerate(RECEITA):
        a, d = rise(t, C[cue])
        y = 260 + k * 140 + d
        if a > 0:
            rrect(c, 230, y - 52, 1460, 104, 22, mix("#FFFFFF", col, 0.08), a)
            badge_num(c, n, 290, y, a, 32, bg=col)
            fmid(c, s, 350, y, 44 if k else 36, "black", col if k else INK, a, align="left")


# ======================================================================
# exemplos resolvidos (mesmo esqueleto: equação no topo, contas à esquerda, gangorra à direita)
# ======================================================================

def exemplo(c, t, C, eq, eq_cue, rows, rx, m, u, g_cue, v_cue, x_lo=None, x_hi=None, dy=70, size=40, labels=None, sumir=0.0,
            u_anim=None, eq2=None, step=1):
    """rx = (v0, v1) da reta · g_cue: a gangorra aparece · v_cue: valores das raízes"""
    fbox(c, eq, W / 2, 230, 50, ep(t, C[eq_cue], 0.5), INK)
    if eq2:
        eq2(c, t)
    linhas(c, t, C, rows, 200, 330, size, dy)
    ag = ep(t, C[g_cue], 0.5)
    X = reta(c, x_lo or 1060, x_hi or 1660, 620, rx[0], rx[1], ag, step=step)
    if X:
        uu = u_anim(t) if u_anim else u
        gangorra(c, X, 620, m, uu, ag, show_val=ep(t, C[v_cue], 0.4) if v_cue else 0.0, col_ok=GREEN, labels=labels,
                 show_m=ag, sumir=sumir, h=150)


def b_ex_impar(c, t, C, B):
    frame(c, t, B["start"], "EXEMPLO", "UMA MÉDIA QUEBRADA", BLUE)
    rows = [("13.b", "b = −5    c = 6", INK),
            ("13.c", "1)  m = 5/2 = 2,5", PURPLE),
            ("13.d", "2)  u² = 2,5² − 6 = 6,25 − 6", PURPLE),
            ("13.e", "      u² = 0,25", PURPLE),
            ("13.f", "      u = 0,5   (0,5 · 0,5 = 0,25)", PURPLE),
            ("13.g", "3)  2,5 − 0,5 = 2", GREEN),
            ("13.h", "      2,5 + 0,5 = 3", GREEN)]
    exemplo(c, t, C, "x² − 5x + 6 = 0", "13.a", rows, (1, 4), 2.5, 0.5, "13.c", "13.g", dy=64, size=38, step=0.5)


def b_ex_a(c, t, C, B):
    frame(c, t, B["start"], "EXEMPLO", "NÚMERO NA FRENTE DO x²", BLUE)
    ab = ep(t, C["14.b"], 0.5)
    rows = [("14.c", "x² + 2x − 3 = 0", INK),
            ("14.d", "1)  m = −2/2 = −1", PURPLE),
            ("14.e", "2)  u² = (−1)² − (−3) = 1 + 3 = 4", PURPLE),
            ("14.e", "      u = 2", PURPLE),
            ("14.f", "3)  −1 − 2 = −3", GREEN),
            ("14.g", "      −1 + 2 = 1", GREEN)]
    rows[3] = ("14.e", rows[3][1], PURPLE)

    def eq2(c, t):
        pill(c, "passo 0:  ÷ 2", 1480, 230, AMBER, size=30, a=ab, anchor="center", bounds=(0, 1920))
    exemplo(c, t, C, "2x² + 4x − 6 = 0", "14.a", rows, (-4, 2), -1, 2, "14.d", "14.f", eq2=eq2, dy=70, size=38)
    pill(c, "atenção ao sinal!", 900, 400, AMBER, size=26, a=ep(t, C["14.d"] + 1.6, 0.4), anchor="center", bounds=(0, 1920))


def b_ex_irracional(c, t, C, B):
    frame(c, t, B["start"], "CASO ESPECIAL", "u NÃO É EXATO", BLUE)
    rows = [("16.b", "1)  m = 6/2 = 3", PURPLE),
            ("16.c", "2)  u² = 3² − 7 = 9 − 7 = 2", PURPLE),
            ("16.d", "      u = √2  ≈ 1,41", PURPLE),
            ("16.e", "3)  3 − √2   e   3 + √2", GREEN),
            ("16.e", "      ≈ 1,59   e   ≈ 4,41", GRAY)]
    exemplo(c, t, C, "x² − 6x + 7 = 0", "16.a", rows, (0, 6), 3, math.sqrt(2), "16.b", "16.e",
            labels=["3 − √2", "3 + √2"], dy=86, size=42)
    pill(c, "nenhum inteiro ao quadrado dá 2", 200, 780, AMBER, size=26, a=ep(t, C["16.d"], 0.4), anchor="left",
         bounds=(0, 1920))


def b_ex_dupla(c, t, C, B):
    frame(c, t, B["start"], "CASO ESPECIAL", "u = 0: RAIZ DUPLA", BLUE)
    rows = [("17.b", "1)  m = 10/2 = 5", PURPLE),
            ("17.c", "2)  u² = 5² − 25 = 25 − 25 = 0", PURPLE),
            ("17.c", "      u = 0", PURPLE),
            ("17.e", "3)  5 − 0 = 5   e   5 + 0 = 5", GREEN)]
    rows[2] = ("17.c", rows[2][1], PURPLE)
    uanim = lambda tt: 2.0 * (1 - ep(tt, C["17.d"], 1.2))
    exemplo(c, t, C, "x² − 10x + 25 = 0", "17.a", rows, (2, 8), 5, 0, "17.b", "17.e", u_anim=uanim, dy=86, size=42)
    fbox(c, "raiz dupla: x = 5", 560, 760, 44, ep(t, C["17.e"], 0.5), GREEN)
    pill(c, "as duas juntas, bem no meio", 1360, 330, BLUE, size=26, a=ep(t, C["17.d"] + 0.8, 0.4), anchor="center",
         bounds=(0, 1920))


def b_ex_negativo(c, t, C, B):
    frame(c, t, B["start"], "CASO ESPECIAL", "u² NEGATIVO", AMBER)
    rows = [("18.b", "1)  m = 2/2 = 1", PURPLE),
            ("18.c", "2)  u² = 1² − 5 = 1 − 5 = −4", RED),
            ("18.d", "      2² = 4    (−2)² = 4", AMBER),
            ("18.d", "      ao quadrado: nunca negativo", AMBER)]
    exemplo(c, t, C, "x² − 2x + 5 = 0", "18.a", rows, (-2, 4), 1, 1.6, "18.b", None, dy=86, size=42,
            sumir=ep(t, C["18.e"], 0.6))
    fbox(c, "NÃO TEM RAIZ REAL", 560, 730, 44, ep(t, C["18.f"], 0.5), BLUE)
    pill(c, "não é erro de conta", 560, 810, AMBER, size=26, a=ep(t, C["18.f"] + 1.2, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# recap
# ======================================================================

FRASES = ["A média é menos b sobre dois.", "O u ao quadrado é a média ao quadrado, menos c.",
          "As raízes são a média menos u e a média mais u."]
FORMULAS = ["m = −b/2", "u² = m² − c", "m − u  e  m + u"]


def b_recap(c, t, C, B):
    sid = which(t, C, ["15", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "15" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        text(c, s, 330, y, 44, "black", INK, a, align="left")
        fmid(c, FORMULAS[k], 330, y + 58, 38, "black", PURPLE, ep(t, C[f"{sid}.{'abc'[k]}"] + 0.6, 0.4), align="left")


# ======================================================================
# Bhaskara e atalho de prova
# ======================================================================

def b_bhaskara(c, t, C, B):
    frame(c, t, B["start"], "E A FÓRMULA DE BHASKARA?", "A MESMA CONTA, DISFARÇADA", GREEN)
    fmid(c, "x² − 8x + 12 = 0", 520, 240, 46, "black", INK, ep(t, C["19.t"], 0.5))
    fmid(c, "Δ = b² − 4 · a · c", 520, 340, 42, "black", INK, ep(t, C["19.a"], 0.4))
    fmid(c, "Δ = 64 − 48 = 16", 520, 410, 42, "black", INK, ep(t, C["19.a"] + 1.2, 0.4))
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        fmid(c, "x =", 300, 560, 46, "black", INK, ab)
        hl_m = ep(t, C["19.c"], 0.4)
        hl_u = ep(t, C["19.d"], 0.4)
        text(c, "8", 420, 530, 50, "black", mix(INK, PURPLE, hl_m), ab)
        text(c, "±", 470, 530, 50, "black", INK, ab)
        text(c, "4", 520, 530, 50, "black", mix(INK, GREEN, hl_u), ab)
        line(c, 390, 548, 550, 548, INK, ab, 4, cap_round=False)
        text(c, "2", 470, 606, 50, "black", INK, ab)
        fmid(c, "= 6  ou  2", 700, 560, 46, "black", GREEN, ep(t, C["19.b"] + 1.0, 0.4))
    # lado direito: as peças da média e do u
    fmid(c, "8 ÷ 2 = 4  →  a MÉDIA", 1330, 330, 42, "black", PURPLE, ep(t, C["19.c"], 0.4))
    fmid(c, "4 ÷ 2 = 2  →  o u", 1330, 430, 42, "black", GREEN, ep(t, C["19.d"], 0.4))
    ae = ep(t, C["19.e"], 0.5)
    fbox(c, "Bhaskara = média ± u", 1330, 560, 48, ae, GREEN)
    fmid(c, "com x² sozinho:  −b/2 = m   e   √Δ/2 = u", 1330, 650, 30, "black", GRAY, ae)
    pill(c, "ATALHO: mesma resposta, sem decorar fórmula", W / 2, 780, GREEN, size=30, a=ep(t, C["19.e"] + 1.5, 0.4),
         anchor="center")


def b_atalho(c, t, C, B):
    frame(c, t, B["start"], "ATALHO DE PROVA", "O MÉTODO EM 3 CHECAGENS", GREEN)
    dicas = [("20.a", "número na frente do x²? DIVIDA tudo por ele", "2x² + 4x − 6 = 0  →  x² + 2x − 3 = 0"),
             ("20.b", "média = metade do b, com o SINAL TROCADO", "b = −8  →  m = +4"),
             ("20.c", "no fim, CONFIRA: somam −b e multiplicam c", "2 + 6 = 8   ·   2 · 6 = 12  ✓")]
    for k, (cue, s1, s2) in enumerate(dicas):
        a, d = rise(t, C[cue])
        y = 280 + k * 170 + d
        badge_num(c, k + 1, 270, y - 14, a, 34, bg=GREEN)
        text(c, s1, 330, y, 42, "black", INK, a, align="left")
        fmid(c, s2, 330, y + 56, 32, "black", GREEN, a, align="left")


# ======================================================================
# erros clássicos
# ======================================================================

ERROS = [("21", "Esquecer de dividir pelo número da frente", "2x² + 4x − 6:  usa b = 4  →  m = −2",
          "o 4 está ali, à vista", "divida primeiro: x² + 2x − 3  →  m = −1"),
         ("22", "Errar o sinal da média", "x² − 8x + 12:  m = −4", "tem um menos na frente do 8",
          "m = −b/2 = −(−8)/2 = +4"),
         ("23", "Esquecer o ± e dar uma raiz só", "x² − 8x + 12:  “x = 6”", "a primeira conta já deu um número que funciona",
          "a gangorra tem DUAS crianças: m − u e m + u"),
         ("24", "Achar que u² negativo é erro de conta", "u² = −4  →  “errei, vou refazer...”",
          "a gente se acostuma a sempre achar resposta", "u² negativo É a resposta: não tem raiz real")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, ex, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 4", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(4):
        badge_num(c, k + 1, 840 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 320, 34, aa, RED, "x")
    text(c, err, 360, 335, 44, "black", RED, aa, align="left")
    ftext(c, ex, 360, 405, 36, "bold", INK2, ep(t, cue("a") + 0.8, 0.4), align="left")
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 500, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 575, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 690, 34, ac, GREEN)
    ftext(c, fix, 360, 705, 38, "black", GREEN, ac, align="left")
    if sid == "23":     # a gangorra com uma criança só tomba
        tomba(c, 1480, 560, ep(t, cue("c"), 0.5), ease_io(prog(t, cue("c") + 0.8, 0.9)))


def tomba(c, cx, cy, a, f):
    """gangorra com uma criança só: inclina f (0..1) até encostar no chão"""
    if a <= 0:
        return
    line(c, cx - 230, cy + 60, cx + 230, cy + 60, LIGHT, a, 3)
    p = skia.Path(); p.moveTo(cx, cy); p.lineTo(cx - 34, cy + 58); p.lineTo(cx + 34, cy + 58); p.close()
    c.drawPath(p, paint(PURPLE, a))
    c.save(); c.translate(cx, cy); c.rotate(-17 * f)
    rrect(c, -200, -8, 400, 14, 6, MADEIRA, a, shadow=True)
    crianca(c, -170, -8, KID_A, a, 1.3)
    c.restore()
    text(c, "uma só: tomba!", cx, cy + 120, 30, "black", RED, a * f)


# ======================================================================
# questão estilo ENEM
# ======================================================================

QTXT = ("Um terreno retangular tem perímetro de 40 metros e área de 96 metros quadrados. "
        "Quais são as medidas dos lados do terreno, em metros?")
ALTS = [("A", "4 e 24", "25.c", "28.xa", "área 96, mas a volta dá 56", RED),
        ("B", "6 e 14", "25.d", "28.xb", "usou u = 4: esqueceu a raiz quadrada", RED),
        ("C", "6 e 16", "25.e", "28.xc", "área 96, mas a volta dá 44", RED),
        ("D", "8 e 12", "25.f", None, "", GREEN),
        ("E", "10 e 10", "25.g", "28.xe", "parou na média: área 100", RED)]


def alts_rows(c, t, C, alts, x, y0, dy, size, ok_cue, okL):
    """alternativas uma por linha; a errada é riscada e ganha o motivo AO LADO, na mesma linha"""
    aok = ep(t, C[ok_cue], 0.5)
    for k, (L, s, cue_in, cx, why, col) in enumerate(alts):
        a, d = rise(t, C[cue_in])
        if a <= 0:
            continue
        y = y0 + k * dy + d
        ok = L == okL
        if ok and aok > 0:
            rrect(c, x - 24, y - 44, 820, 88, 16, GREEN, 0.15 * aok)
        badge_num(c, L, x + 10, y, a, 24, bg=GREEN if ok and aok > 0.5 else INK)
        ax = ep(t, C[cx], 0.4) if cx else 0
        tw = text_w(s, "black", size)
        text_mid(c, s, x + 56, y, size, "black", GREEN if ok and aok > 0.5 else INK, a * (1 - 0.5 * ax), align="left")
        if ax > 0:
            strike(c, x + 50, y, x + 62 + tw, y, ax, RED, ax)
            pill(c, why, x + 90 + tw, y, col, size=22, a=ax, bounds=(0, 1920))
        if ok and aok > 0:
            check_icon(c, x + 90 + tw, y, 22, aok, GREEN)


def terreno(c, x, y, w, h, a, lado_a="?", lado_b="?", col=None):
    if a <= 0:
        return
    col = col or GREEN
    rrect(c, x, y, w, h, 6, mix("#FFFFFF", col, 0.22), a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(col, a, stroke=4))
    text(c, lado_a, x + w / 2, y - 14, 28, "black", INK2, a)
    text(c, lado_b, x + w + 16, y + h / 2 + 10, 28, "black", INK2, a, align="left")


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO NO ESTILO ENEM", "O TERRENO RETANGULAR", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["25.a"], 0.5)
    res = ep(t, C["26"], 0.5)
    para(c, QTXT, 180, 250, 32, "bold", INK, a * (1 - res), 640, 44)
    terreno(c, 260, 520, 380, 200, ep(t, C["25.a"] + 1.0, 0.5) * (1 - res), "comprimento", "largura")
    text(c, "perímetro 40 m · área 96 m²", 450, 790, 26, "black", GREEN, ep(t, C["25.a"] + 2.0, 0.4) * (1 - res))
    if res > 0:
        rows = [("26.a", "perímetro = volta inteira = 40", INK), ("26.a", "comprimento + largura = 20", BLUE),
                ("26.b", "comprimento · largura = 96", BLUE), ("26.c", "x² − 20x + 96 = 0", INK)]
        rows[1] = ("26.a", rows[1][1], BLUE)
        k = which(t, C, ["26", "27"])
        if k == "26":
            for j, (cue, s, col) in enumerate(rows):
                aj, d = rise(t, C[cue] + (1.4 if j == 1 else 0))
                fmid(c, s, 190, 260 + j * 80 + d, 36, "black", col, aj, align="left")
            pill(c, "ATALHO: soma e produto já estão no enunciado", 480, 620, GREEN, size=22, a=ep(t, C["26.d"], 0.4),
                 anchor="center", bounds=(0, 1920))
            fmid(c, "soma 20 · produto 96", 190, 700, 40, "black", GREEN, ep(t, C["26.d"], 0.4), align="left")
        else:
            fmid(c, "soma 20 · produto 96", 190, 250, 34, "black", GREEN, 1.0, align="left")
            rr = [("27.a", "1)  m = 20 ÷ 2 = 10", PURPLE), ("27.b", "2)  u² = 10² − 96 = 100 − 96 = 4", PURPLE),
                  ("27.c", "      u = 2", PURPLE), ("27.d", "3)  10 − 2 = 8   e   10 + 2 = 12", GREEN),
                  ("27.e", "8 + 12 = 20 ✓    8 · 12 = 96 ✓", GREEN)]
            linhas(c, t, C, rr, 190, 330, 32, 66)
            ag = ep(t, C["27.d"], 0.5)
            terreno(c, 300, 662, 220, 140, ag, "12", "8")
    if t >= C["25.c"] - 0.2:
        alts_rows(c, t, C, ALTS, 940, 270, 108, 44, "27.ok", "D")
    pause_timer(c, t, C["25.end"] - 1.9, 1600, 730)


# ======================================================================
# ponte e CTA
# ======================================================================

TREINO = [("x² − 6x + 8 = 0", "2 e 4"), ("x² + 4x − 5 = 0", "−5 e 1"), ("3x² − 12x + 9 = 0", "1 e 3")]


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "AGORA É COM VOCÊ", "TREINE O MÉTODO", GREEN)
    aa = ep(t, C["30.a"], 0.5)
    text(c, "resolva pela média e pelo u:", 260, 260, 34, "black", INK2, aa, align="left")
    for k, (eq, r) in enumerate(TREINO):
        a, d = rise(t, C["30.a"] + 0.6 + 0.5 * k)
        y = 350 + k * 100 + d
        badge_num(c, k + 1, 290, y - 2, a, 28, bg=PURPLE)
        fmid(c, eq, 350, y, 48, "black", INK, a, align="left")
    ab = ep(t, C["30.b"], 0.5)
    fbox(c, "depois, confira com Bhaskara", 1340, 400, 40, ab, BLUE)
    fbox(c, "a mesma resposta ✓", 1340, 530, 44, ep(t, C["30.c"], 0.4), GREEN)
    text(c, "respostas:  " + "   ·   ".join(r for _, r in TREINO), W / 2, 790, 26, "bold", GRAY, ep(t, C["30.c"] + 0.8, 0.4))


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Você já conhecia esse jeito de resolver sem Bhaskara?", canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, fatores=b_fatores, gangorra=b_gangorra,
              credito=b_credito, receita=b_receita, ex_impar=b_ex_impar, ex_a=b_ex_a, recap=b_recap,
              ex_irracional=b_ex_irracional, ex_dupla=b_ex_dupla, ex_negativo=b_ex_negativo, bhaskara=b_bhaskara,
              atalho=b_atalho, erros=b_erros, questao=b_questao, ponte=b_ponte, cta=b_cta)
