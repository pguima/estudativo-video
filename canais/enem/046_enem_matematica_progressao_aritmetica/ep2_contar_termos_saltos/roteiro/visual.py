"""Visual — Progressão Aritmética, Episódio 2: contar termos e saltos (meios, postes, múltiplos e três termos) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: fila() (bolinhas = termos, arcos = saltos, com os dois contadores lado a lado), rodovia() (os postes
do km 3 e do km 27, os 5 novos caindo do céu e os 6 vãos acendendo), cerca() (estacas e pedaços), trio() (x − r, x, x + r
com o r se cancelando), triangulo() (o terreno da Q6), linha().
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
_s = importlib.util.spec_from_file_location("comum046", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr = K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pa_ep2_contar_termos_saltos.mp4"
CARD_R = K.CARD_R
ASFALTO = "#5E6168"
GRAMA = "#E6EFD9"
MADEIRA = "#B58552"


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


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    """faixa com a pergunta do bloco"""
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def arco(c, x1, x2, y, a, col=AMBER, alt=None, sw=5, rot=""):
    """arco (salto) entre duas bolinhas, por cima"""
    if a <= 0:
        return
    alt = alt if alt is not None else min(70, (x2 - x1) * 0.45)
    p = skia.Path(); p.moveTo(x1, y); p.quadTo((x1 + x2) / 2, y - alt * 2, x2, y)
    c.drawPath(p, paint(col, a, stroke=sw, cap_round=True))
    if rot:
        fmid(c, rot, (x1 + x2) / 2, y - alt - 26, 26, "black", col, a)


def fila(c, x0, x1, cy, valores, a, pb=None, pa=None, r=36, size=34, col=BLUE, arc_col=AMBER, rot_arco="",
         cores=None):
    """fila de termos: bolinhas com os valores (strings) e arcos entre vizinhas.
    pb = quantas bolinhas já apareceram (float), pa = quantos arcos (float). Devolve as posições x."""
    n = len(valores)
    xs = [x0 + (x1 - x0) * k / (n - 1) for k in range(n)] if n > 1 else [(x0 + x1) / 2]
    if a <= 0:
        return xs
    pb = n if pb is None else pb
    pa = n - 1 if pa is None else pa
    for k in range(n - 1):
        arco(c, xs[k] + r * 0.7, xs[k + 1] - r * 0.7, cy - r * 0.4, a * clamp(pa - k), arc_col, rot=rot_arco)
    for k, v in enumerate(valores):
        ak = a * clamp(pb - k)
        if ak <= 0:
            continue
        cc = (cores or {}).get(k, col)
        c.drawCircle(xs[k], cy, r, paint(mix("#FFFFFF", cc, 0.16), ak))
        c.drawCircle(xs[k], cy, r, paint(cc, ak, stroke=4))
        if v:
            fmid(c, v, xs[k], cy, size if ftext_w(v, "black", size) < r * 1.8 else size * 0.72, "black", INK, ak)
    return xs


def contadores(c, cx, cy, nb, na, a, gap=330):
    """os dois contadores lado a lado: bolinhas (termos) e arcos (saltos)"""
    if a <= 0:
        return
    for k, (v, rot, col) in enumerate(((nb, "bolinhas (termos)", BLUE), (na, "arcos (saltos)", AMBER))):
        x = cx + (k - 0.5) * gap
        rrect(c, x - 140, cy - 62, 280, 124, 20, "#FFFFFF", a, shadow=True)
        fmid(c, str(v), x, cy - 16, 60, "black", col, a)
        text(c, rot, x, cy + 46, 22, "black", INK2, a)


def poste(c, x, ybase, h, a, col=INK, luz=0.0):
    if a <= 0:
        return
    line(c, x, ybase, x, ybase - h, col, a, 7)
    line(c, x, ybase - h, x + 26, ybase - h, col, a, 6)
    c.drawCircle(x + 30, ybase - h + 6, 9, paint(mix(GRAY, "#F5C542", luz), a))


def rodovia(c, x0, x1, y, a, queda=1.0, vaos=0.0, rotulos=True, novos=5, cor_vao=GREEN, txt_vao="4 km"):
    """rodovia do km 3 ao km 27: postes das pontas fixos, `novos` postes caindo do céu (queda 0 → 1),
    e os vãos acendendo um a um (vaos = 0 → n − 1)"""
    if a <= 0:
        return
    n = novos + 2
    rrect(c, x0 - 60, y, x1 - x0 + 120, 70, 12, ASFALTO, a)
    for k in range(int((x1 - x0 + 120) / 60)):
        rrect(c, x0 - 50 + k * 60, y + 32, 30, 6, 3, "#FFFFFF", a * 0.8)
    xs = [x0 + (x1 - x0) * k / (n - 1) for k in range(n)]
    for k in range(n - 1):
        av = a * clamp(vaos - k)
        if av > 0:
            rrect(c, xs[k] + 6, y - 22, xs[k + 1] - xs[k] - 12, 14, 7, cor_vao, av)
            fmid(c, txt_vao, (xs[k] + xs[k + 1]) / 2, y - 48, 24, "black", cor_vao, av)
    for k, x in enumerate(xs):
        if k in (0, n - 1):
            poste(c, x, y, 150, a, INK, 1.0)
            if rotulos:
                fmid(c, f"km {3 if k == 0 else 27}", x, y + 104, 30, "black", PURPLE, a)
        else:
            u = clamp(queda * (novos + 1) - (k - 1) * 0.9) if novos else 1
            u = 1 - (1 - u) ** 3
            poste(c, x, y - (1 - u) * 520, 150, a * clamp(u * 3), BLUE, u)


def cerca(c, x0, x1, y, a, pe=11.0, pv=10.0, n=10, rot=True):
    """cerca de 30 m: n pedaços e n + 1 estacas; pe/pv = quantas estacas/pedaços já aparecem"""
    if a <= 0:
        return
    xs = [x0 + (x1 - x0) * k / n for k in range(n + 1)]
    c.drawRect(skia.Rect.MakeLTRB(x0 - 40, y + 4, x1 + 40, y + 40), paint(GRAMA, a))
    for k in range(n):
        av = a * clamp(pv - k)
        if av > 0:
            for dy in (-70, -30):
                line(c, xs[k], y + dy, xs[k + 1], y + dy, MADEIRA, av, 8)
            fmid(c, str(k + 1), (xs[k] + xs[k + 1]) / 2, y - 110, 26, "black", AMBER, av)
    for k, x in enumerate(xs):
        ae = a * clamp(pe - k)
        if ae > 0:
            rrect(c, x - 9, y - 100, 18, 104, 4, mix(MADEIRA, INK, 0.25), ae)
    if rot:
        fmid(c, "3 m", (xs[0] + xs[1]) / 2, y + 70, 24, "black", INK2, a)


def triangulo(c, x, y, s, a, lados=("12 − r", "x", "12 + r"), cores=(BLUE, BLUE, PURPLE)):
    """triângulo retângulo: cateto vertical (lados[0]), cateto horizontal (lados[1]) e hipotenusa (lados[2]);
    (x, y) = vértice do ângulo reto; s = escala (px por metro, base 12 m)"""
    if a <= 0:
        return
    h, b = 9 * s, 12 * s
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + b, y); p.lineTo(x, y - h); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", GREEN, 0.18), a))
    line(c, x, y, x, y - h, cores[0], a, 7)
    line(c, x, y, x + b, y, cores[1], a, 7)
    line(c, x + b, y, x, y - h, cores[2], a, 7)
    q = 26
    c.drawPath(_quad(x, y, q), paint(INK, a, stroke=3))
    fmid(c, lados[0], x - 20 - ftext_w(lados[0], "black", 32) / 2, y - h / 2, 32, "black", cores[0], a)
    fmid(c, lados[1], x + b / 2, y + 38, 32, "black", cores[1], a)
    nrm = math.hypot(h, b)
    off = 30 + ftext_w(lados[2], "black", 32) / 2
    fmid(c, lados[2], x + b / 2 + h / nrm * off, y - h / 2 - b / nrm * off * 0.55, 32, "black", cores[2], a)


def _quad(x, y, q):
    p = skia.Path(); p.moveTo(x, y - q); p.lineTo(x + q, y - q); p.lineTo(x + q, y)
    return p


def trio(c, cx, cy, a, cancela=0.0, size=64, vals=("x − r", "x", "x + r")):
    """os três termos em notação simétrica; cancela 0 → 1 risca o − r e o + r"""
    if a <= 0:
        return
    xs = [cx - 360, cx, cx + 360]
    for k, (x, v) in enumerate(zip(xs, vals)):
        rrect(c, x - 150, cy - 70, 300, 140, 26, mix("#FFFFFF", PURPLE if k == 1 else BLUE, 0.10), a)
        fmid(c, v, x, cy, size, "black", INK, a)
    for k, x in enumerate((xs[0] + 80, xs[2] + 80)):
        if cancela > 0:
            u = clamp(cancela * 1.4 - k * 0.3)
            line(c, x - 64, cy + 30, x - 64 + 120 * u, cy - 30, RED, a, 6)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROGRESSÃO ARITMÉTICA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 220, 1460, 130, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("múltiplos de 7: ", INK), ("105", BLUE), ("  ...  ", GRAY), ("497", BLUE), ("   quantos?", PURPLE)],
              W / 2, 285, 56, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        linha(c, [("(497 − 105) ÷ 7 = ", INK), ("56", AMBER)], 640, 470, 62, ab)
        check_icon(c, 1060, 452, 26, ab * (1 - ep(t, C["01.c"], 0.4)), AMBER, "check")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        check_icon(c, 1060, 452, 26, acc, RED, "x")
        rrect(c, 1180, 400, 420, 140, 24, mix("#FFFFFF", GREEN, 0.12), acc)
        linha(c, [("certo: ", INK2), ("57", GREEN)], 1390, 470, 62, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        fila(c, 420, 1500, 680, ["105", "112", "119", "...", "490", "497"], ad, pb=6, pa=5, r=46, size=30)
        selo(c, 1460, 790, ep(t, C["01.d"] + 1.2, 0.4), "A ALTERNATIVA ERRADA ESTÁ LÁ", AMBER, -3, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "contar termos, saltos e postes", "sem errar por um"),
            ("02.b", "três números em PA", "resolvidos em uma linha")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 52, "black", INK, a, align="left")
        text(c, sub, 360, y + 62, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    sid = which(t, C, ["03", "04"])
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    if sid == "03":
        aa = ep(t, C["03.a"], 0.5)
        if aa > 0:
            text(c, "TERMO GERAL (episódio 1)", 560, 300, 32, "black", PURPLE, aa)
            linha(c, [("aₙ = a₁ + (n − 1) · r", INK)], 560, 430, 60, aa)
            text(c, "o primeiro + (n − 1) saltos", 560, 540, 30, "bold", GRAY, aa)
        ab = ep(t, C["03.b"], 0.5)
        if ab > 0:
            text(c, "MÚLTIPLOS DE 7 (Divisibilidade)", 1370, 300, 30, "black", BLUE, ab)
            for k in range(6):
                chip(c, str(7 * (k + 1)), 1170 + (k % 3) * 200, 420 + (k // 3) * 120, BLUE,
                     ab * ep(t, C["03.b"] + 0.4 + k * 0.25, 0.3), 44)
            text(c, "a tabuada do 7", 1370, 650, 30, "bold", GRAY, ab)
        line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)
        return
    aa = ep(t, C["04.a"], 0.5)
    triangulo(c, 380, 700, 32, aa, ("cateto", "cateto", "hipotenusa"), (BLUE, BLUE, PURPLE))
    if aa > 0:
        ab = ep(t, C["04.b"], 0.5)
        pill(c, "catetos: formam o canto reto", 1040, 300, BLUE, size=28, a=ab)
        pill(c, "hipotenusa: o maior lado", 1040, 380, PURPLE, size=28, a=ab * ep(t, C["04.b"] + 1.6, 0.4))
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            rrect(c, 1000, 450, 700, 120, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
            linha(c, [("hip² = cat² + cat²", PURPLE)], 1350, 510, 48, acc)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            rrect(c, 1000, 600, 700, 120, 22, mix("#FFFFFF", BLUE, 0.10), ad)
            linha(c, [("área = cat · cat ÷ 2", BLUE)], 1350, 660, 48, ad)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA CERCA DE 30 m", "CONTE COMIGO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    pv = 10 * ep(t, C["05.b"] + 0.3, 3.0)
    pe = 11 * ep(t, C["05.c"] + 0.2, 1.6) if t >= C["05.c"] else 0
    cerca(c, 360, 1560, 560, aa, pe=pe if pe > 0 else 0, pv=pv)
    if aa > 0:
        fmid(c, "30 m · uma estaca a cada 3 m", W / 2, 250, 40, "black", INK, aa)
    ab = ep(t, C["05.b"], 0.5)
    acc = ep(t, C["05.c"], 0.5)
    if ab > 0:
        rrect(c, 520, 660, 380, 120, 20, "#FFFFFF", ab, shadow=True)
        linha(c, [("pedaços: ", INK2), (str(int(round(pv))), AMBER)], 710, 720, 46, ab)
    if acc > 0:
        rrect(c, 1020, 660, 380, 120, 20, "#FFFFFF", acc, shadow=True)
        linha(c, [("estacas: ", INK2), (str(int(round(max(pe, 0)))), BLUE)], 1210, 720, 46, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 320, ad, "SEMPRE + 1", GREEN, -4, 40)


# ======================================================================
# blocos a, b — interpolar e os postes
# ======================================================================

def b_interpolar(c, t, C, B):
    head_seq(c, t, C, [("06", "INTERPOLAR", "COLOCAR NÚMEROS NO MEIO", BLUE), ("07", "QUANTOS TERMOS?", "QUANTOS SALTOS?", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    vals = ["2", "?", "?", "?", "14"]
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            regra(c, "interpolar = colocar números no meio, formando uma PA", W / 2, 250, aa, 34, BLUE)
        ab = ep(t, C["06.b"], 0.5)
        xs = fila(c, 420, 1500, 520, vals, ab, pb=5, pa=0, r=56, size=46,
                  cores={0: PURPLE, 4: PURPLE})
        if ab > 0:
            pill(c, "extremo", xs[0], 630, PURPLE, size=24, a=ab, anchor="center")
            pill(c, "extremo", xs[4], 630, PURPLE, size=24, a=ab, anchor="center")
            pill(c, "meios aritméticos", xs[2], 630, BLUE, size=24, a=ep(t, C["06.b"] + 2.0, 0.4), anchor="center")
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            fmid(c, "3 meios entre 2 e 14", W / 2, 760, 40, "black", INK, acc)
        return
    pa = 4 * ep(t, C["07.b"] + 0.4, 1.6)
    vals2 = ["2", "5", "8", "11", "14"] if t >= C["07.d"] else vals
    ys = 470
    fila(c, 420, 1500, ys, vals2, 1, pb=5, pa=pa if t >= C["07.b"] else 0, r=56, size=46, cores={0: PURPLE, 4: PURPLE},
         rot_arco="+3" if t >= C["07.c"] + 2 else "")
    contadores(c, W / 2, 650, 5 if t >= C["07.a"] else "?", int(round(pa)) if t >= C["07.b"] else "?",
               ep(t, C["07.a"], 0.4))
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        linha(c, [("14 − 2 = 12  ·  12 ÷ 4 = ", INK), ("3", GREEN)], W / 2, 250, 40, acc)
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        rrect(c, 300, 740, 1320, 80, 40, mix("#FFFFFF", PURPLE, 0.12), ae)
        fmid(c, "k meios  →  k + 2 termos  e  k + 1 saltos", W / 2, 780, 38, "black", PURPLE, ae)


def b_postes(c, t, C, B):
    head_seq(c, t, C, [("08", "A RODOVIA", "5 POSTES NOVOS", BLUE), ("09", "A CONTA É COM OS VÃOS", "6 r = 24", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    queda = ep(t, C["08.b"] + 0.2, 2.6) if sid == "08" else 1
    vaos = 6 * ep(t, C["08.d"] + 0.3, 2.4) if sid == "08" else 6
    txt = "?" if t < C["09.b"] else "4 km"
    rodovia(c, 330, 1590, 560, ep(t, C["08.a"], 0.5), queda, vaos if t >= C["08.d"] else 0, txt_vao=txt,
            cor_vao=AMBER if t < C["09.b"] else GREEN)
    if sid == "08":
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            linha(c, [("5 novos + 2 das pontas = ", INK), ("7 postes", BLUE)], W / 2, 260, 44, acc)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            linha(c, [("entre 7 postes: ", INK), ("6 vãos", AMBER)], W / 2, 760, 44, ad)
        return
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        linha(c, [("27 − 3 = ", INK), ("24 km", BLUE)], 620, 260, 48, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        linha(c, [("6 · r = 24  →  r = ", INK), ("4 km", GREEN)], 1300, 260, 48, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        regra(c, "entre 7 postes há 6 vãos", W / 2, 770, acc, 38, PURPLE)


def b_atalho_fila(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DESENHE A FILA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    K.atalho(c, 260, 190, 1400, 130, "ANTES DE DIVIDIR", ["desenhe a fila: bolinhas = termos · arcos = saltos"], aa, 36)
    pb = 7 * ep(t, C["10.b"], 2.0)
    pa = 6 * ep(t, C["10.b"] + 1.0, 2.0)
    fila(c, 400, 1520, 500, [""] * 7, ep(t, C["10.b"], 0.4), pb=pb, pa=pa, r=40)
    contadores(c, W / 2, 660, int(round(pb)), int(round(pa)), ep(t, C["10.c"], 0.4))
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        selo(c, 1540, 640, ep(t, C["10.c"] + 1.6, 0.4), "UM ARCO A MENOS", AMBER, -4, 30)
        pill(c, "divida pelos ARCOS", W / 2, 790, GREEN, size=30, a=ep(t, C["10.c"] + 3.0, 0.4), anchor="center")


# ======================================================================
# bloco c — contar termos
# ======================================================================

def b_contar(c, t, C, B):
    head_seq(c, t, C, [("11", "QUANTOS TERMOS?", "MÚLTIPLOS DE 7 ENTRE 100 E 500", BLUE),
                       ("12", "PELO TERMO GERAL", "n − 1 = 56", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            pergunta(c, "múltiplos de 7 entre 100 e 500: quantos?", W / 2, 230, aa, BLUE, 38)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            regra(c, "múltiplo de 7: dividido por 7, não sobra nada", W / 2, 340, ab, 32, BLUE)
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 420, 640, 330, 22, "#FFFFFF", acc, shadow=True)
            text(c, "O PRIMEIRO", 580, 470, 28, "black", BLUE, acc)
            linha(c, [("100 ÷ 7 = 14 e sobra", INK2)], 580, 550, 34, acc)
            linha(c, [("15 · 7 = ", INK), ("105", GREEN)], 580, 650, 50, ep(t, C["11.c"] + 2.4, 0.4))
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            rrect(c, 1020, 420, 640, 330, 22, "#FFFFFF", ad, shadow=True)
            text(c, "O ÚLTIMO", 1340, 470, 28, "black", BLUE, ad)
            linha(c, [("500 ÷ 7 = 71 e sobra", INK2)], 1340, 550, 34, ad)
            linha(c, [("71 · 7 = ", INK), ("497", GREEN)], 1340, 650, 50, ep(t, C["11.d"] + 1.6, 0.4))
        return
    fila(c, 360, 1560, 300, ["105", "112", "119", "...", "490", "497"], 1, r=50, size=30, rot_arco="")
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        linha(c, [("497 = 105 + (n − 1) · 7", INK)], W / 2, 450, 50, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        linha(c, [("392 ÷ 7 = 56  →  n − 1 = ", INK), ("56", AMBER)], W / 2, 560, 46, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        linha(c, [("n = ", INK), ("57", GREEN)], W / 2, 660, 60, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        contadores(c, W / 2, 760, 57, 56, ad, 360)


def b_atalho_contar(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "QUANTOS TERMOS?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 170, "CONTAR TERMOS", ["n = (último − primeiro) ÷ r + 1"], aa, 52)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 420, 430, 560, 110, 22, mix("#FFFFFF", AMBER, 0.12), ab)
        fmid(c, "a divisão → os SALTOS", 700, 485, 34, "black", AMBER, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 430, 520, 110, 22, mix("#FFFFFF", BLUE, 0.12), acc)
        fmid(c, "o + 1 → o 1º TERMO", 1280, 485, 34, "black", BLUE, acc)
        xs = fila(c, 560, 1360, 690, [""] * 5, acc, pb=5, pa=4, r=34, cores={0: GREEN})
        pill(c, "não é salto", xs[0], 770, GREEN, size=24, a=ep(t, C["13.c"] + 1.4, 0.4), anchor="center")


# ======================================================================
# bloco d — a cerca fora da fórmula
# ======================================================================

def b_cerca(c, t, C, B):
    head(c, t, B["start"], "FORA DA FÓRMULA", "OBJETOS OU ESPAÇOS?", AMBER)
    card(c, *CARD_R)
    cerca(c, 360, 1560, 470, 1.0)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        linha(c, [("30 ÷ 3 = ", INK), ("10 intervalos", AMBER)], 640, 620, 44, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        linha(c, [("10 + 1 = ", INK), ("11 estacas", BLUE)], 1300, 620, 44, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        pill(c, "o mesmo + 1 do termo geral", W / 2, 700, GREEN, size=28, a=acc, anchor="center")
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        pergunta(c, "pediu os OBJETOS ou os ESPAÇOS entre eles?", W / 2, 790, ad, AMBER, 34)


# ======================================================================
# blocos e, f — média dos vizinhos e notação simétrica
# ======================================================================

def b_media(c, t, C, B):
    head_seq(c, t, C, [("15", "O TERMO DO MEIO", "MÉDIA DOS VIZINHOS", BLUE), ("16", "EXEMPLO", "x, 10, 16", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            regra(c, "média aritmética = soma ÷ 2", W / 2, 240, aa, 36, BLUE)
        ab = ep(t, C["15.b"], 0.5)
        xs = fila(c, 560, 1360, 450, ["a", "b", "c"], ab, r=60, size=50, cores={1: PURPLE}, rot_arco="r")
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            rrect(c, 560, 600, 800, 140, 26, mix("#FFFFFF", PURPLE, 0.10), acc)
            linha(c, [("2b = a + c", PURPLE)], W / 2, 670, 64, acc)
        return
    aa = ep(t, C["16.a"], 0.5)
    vals = ["x", "10", "16"] if t < C["16.b"] else ["4", "10", "16"]
    fila(c, 560, 1360, 330, vals, 1, r=60, size=50, cores={0: AMBER if t < C["16.b"] else GREEN},
         rot_arco="+6" if t >= C["16.c"] else "")
    if aa > 0:
        linha(c, [("2 · 10 = x + 16", INK)], W / 2, 530, 56, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        linha(c, [("20 − 16 = ", INK), ("x = 4", GREEN)], W / 2, 640, 56, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        conferido(c, "saltos de 6: é PA", 760, 770, acc, True, 36)


def b_simetrica(c, t, C, B):
    head(c, t, B["start"], "TRÊS NÚMEROS EM PA", "NOTAÇÃO SIMÉTRICA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        regra(c, "notação simétrica: nomes a partir do termo do meio", W / 2, 240, aa, 34, BLUE)
    ab = ep(t, C["17.b"], 0.5)
    trio(c, W / 2, 440, ab, ep(t, C["17.c"] + 0.6, 1.2))
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("(x − r) + x + (x + r) = ", INK), ("3x", GREEN)], W / 2, 640, 54, acc)
        pill(c, "o r se cancela e SOME", W / 2, 750, RED, size=30, a=ep(t, C["17.c"] + 2.0, 0.4), anchor="center")


def b_atalho_simetrica(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "SOMA ÷ 3 = O DO MEIO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    K.atalho(c, 260, 190, 1400, 130, "TRÊS EM PA COM SOMA DADA", ["divida a soma por 3: é o termo do meio"], aa, 38)
    if aa > 0:
        pergunta(c, "três números em PA · soma 45", W / 2, 400, aa, INK, 40)
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        trio(c, W / 2, 560, ab, 0, 56, ("15 − r", "15", "15 + r"))
        linha(c, [("3x = 45  →  x = ", INK), ("15", GREEN)], W / 2, 720, 50, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        selo(c, 1560, 790, acc, "NA HORA", GREEN, -4, 36)


# ======================================================================
# nós fazemos, recap, erros
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "PRIMEIRO, ÚLTIMO, + 1", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 200, 1400, 120, 24, "#F7F7F5", aa)
        linha(c, [("múltiplos de ", INK), ("6", PURPLE), (" entre ", INK), ("50", BLUE), (" e ", INK), ("200", BLUE),
                  (": quantos?", INK)], W / 2, 260, 52, aa)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 540)
    if t < C["20"]:
        return
    a1 = ep(t, C["20.a"], 0.5)
    if a1 > 0:
        linha(c, [("primeiro: 9 · 6 = ", INK), ("54", GREEN)], 620, 420, 46, a1)
    a2 = ep(t, C["20.b"], 0.5)
    if a2 > 0:
        linha(c, [("último: 33 · 6 = ", INK), ("198", GREEN)], 1300, 420, 46, a2)
    a3 = ep(t, C["20.c"], 0.5)
    if a3 > 0:
        linha(c, [("(198 − 54) ÷ 6 = 144 ÷ 6 = ", INK), ("24 saltos", AMBER)], W / 2, 560, 48, a3)
    a4 = ep(t, C["20.d"], 0.5)
    if a4 > 0:
        rrect(c, 610, 640, 700, 130, 26, mix("#FFFFFF", GREEN, 0.12), a4)
        linha(c, [("24 + 1 = ", INK), ("25 termos", GREEN)], W / 2, 705, 58, a4)


FRASES = ["k meios entre dois números: k + 2 termos e k + 1 saltos.",
          "Contar termos: (último − primeiro) ÷ razão, mais 1.",
          "Três em PA: x − r, x e x + r."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 62)


ERROS = [("5 meios entre 3 e 27: r = 24 ÷ 5", "o enunciado falou CINCO",
          "5 são os novos: com os extremos, 7 termos e 6 saltos → 24 ÷ 6 = 4"),
         ("Esquecer o + 1 na contagem de múltiplos", "a divisão dá 56, redondinho",
          "a divisão contou os SALTOS: falta o primeiro termo → 56 + 1 = 57"),
         ("Contar intervalos quando pedem objetos (ou o contrário)", "30 ÷ 3 dá 10, um número limpo",
          "10 são os pedaços da cerca; estacas, 11. Desenhe a fila!")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24"], ERROS)


# ======================================================================
# questões do material
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


ALTS4 = [("A", "3 km", "÷ 8", RED), ("B", "3,43 km", "÷ 7: os postes", RED), ("C", "4 km", "", GREEN),
         ("D", "4,8 km", "÷ 5: só os novos", RED), ("E", "6 km", "÷ 4", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "INTERPOLAÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("Em um trecho reto de rodovia, há postes no km 3 e no km 27. A concessionária vai instalar "
                           "mais 5 postes entre esses dois, de modo que todos os 7 postes fiquem igualmente espaçados. A "
                           "distância entre dois postes vizinhos será de", INK)], a0, 230, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 250, 680, 44, C["26.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["26"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["26"], 0.4))
        aa = ep(t, C["26.a"], 0.4)
        fila(c, 230, 850, y0 + 80, [""] * 7, aa, r=20)
        if aa > 0:
            linha(c, [("7 postes · ", BLUE), ("6 vãos", AMBER)], 540, y0 + 150, 28, aa)
        linha(c, [("24 km ÷ 6 = ", INK), ("4 km", GREEN)], 540, y0 + 210, 34, ep(t, C["26.b"], 0.4))
        linha(c, [("3 · 7 · 11 · 15 · 19 · 23 · 27", INK2)], 540, y0 + 270, 26, ep(t, C["26.c"], 0.4))


ALTS5 = [("A", "55", "sem o + 1 e sem o 497", RED), ("B", "56", "esqueceu o + 1", RED), ("C", "57", "", GREEN),
         ("D", "58", "começou no 98", RED), ("E", "71", "contou desde o 7", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · NÓS FAZEMOS", "CONTAGEM DE MÚLTIPLOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    yend = _enunciado(c, [("Uma gráfica numera ingressos de 100 a 500. Os ingressos cujo número é múltiplo de 7 dão "
                           "direito a um brinde. A quantidade de ingressos premiados é", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["29"], 0.3)),
         align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 44, C["29.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["28.end"] - 1.9, 540, yend + 140)
    if t >= C["29"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["29"], 0.4))
        linha(c, [("105", BLUE), (" ... ", GRAY), ("497", BLUE)], 540, y0 + 70, 36, ep(t, C["29"], 0.4))
        linha(c, [("(497 − 105) ÷ 7 = ", INK), ("56", AMBER)], 540, y0 + 140, 32, ep(t, C["29.a"], 0.4))
        linha(c, [("56 + 1 = ", INK), ("57", GREEN)], 540, y0 + 210, 40, ep(t, C["29.a"] + 2.2, 0.4))


ALTS6 = [("A", "36", "é o perímetro", RED), ("B", "54", "", GREEN), ("C", "67,5", "hipotenusa como cateto", RED),
         ("D", "72", "12 · 12 ÷ 2", RED), ("E", "108", "esqueceu o ÷ 2", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · VOCÊ FAZ", "TRÊS TERMOS E PITÁGORAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["30.a"], 0.4)
    yend = _enunciado(c, [("Um terreno tem a forma de um triângulo retângulo cujos lados, em metros, formam uma "
                           "progressão aritmética. O perímetro do terreno é 36 m. A área do terreno, em metros quadrados, é",
                           INK)], a0, 230, 26)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["31"], 0.3)),
         align="left")
    cues_in = {L: C[f"30.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"32.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS6, 1000, 250, 680, 44, C["32.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["30.end"] - 1.9, 540, yend + 140)
    if t >= C["31"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["31"], 0.4))
        sid = which(t, C, ["31", "32"])
        if sid == "31":
            linha(c, [("3x = 36  →  x = ", INK), ("12", GREEN)], 540, y0 + 60, 32, ep(t, C["31.a"], 0.4))
            linha(c, [("hipotenusa: ", INK2), ("12 + r", PURPLE)], 540, y0 + 115, 30, ep(t, C["31.b"], 0.4))
            linha(c, [("(12 + r)² = 12² + (12 − r)²", INK)], 540, y0 + 175, 30, ep(t, C["31.c"], 0.4))
            linha(c, [("48r = 144  →  r = ", INK), ("3", GREEN)], 540, y0 + 240, 32, ep(t, C["31.d"], 0.4))
        else:
            sc = 17
            triangulo(c, 250, y0 + 270, sc, ep(t, C["32"], 0.4), ("9", "12", "15"), (BLUE, BLUE, PURPLE))
            linha(c, [("81 + 144 = 225 = 15²", INK2)], 720, y0 + 90, 24, ep(t, C["32.a"], 0.4))
            linha(c, [("9 · 12 ÷ 2 = ", INK), ("54 m²", GREEN)], 720, y0 + 170, 30, ep(t, C["32.b"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A SOMA DE GAUSS", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        linha(c, [("1 + 2 + 3 + ... + 100 = ", INK), ("?", AMBER)], W / 2, 360, 80, aa)
        text(c, "em segundos, sem calculadora", W / 2, 470, 36, "bold", GRAY, ep(t, C["34.a"] + 2.0, 0.4))
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        regra(c, "o truque soma QUALQUER PA", W / 2, 600, ab, 44, PURPLE)
    pill(c, "ep. 3 · a soma de Gauss", W / 2, 760, PURPLE, size=34, a=ep(t, C["34.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Você já errou por um contando postes?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, interpolar=b_interpolar,
              postes=b_postes, atalho_fila=b_atalho_fila, contar=b_contar, atalho_contar=b_atalho_contar, cerca=b_cerca,
              media=b_media, simetrica=b_simetrica, atalho_simetrica=b_atalho_simetrica, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q4=b_q4, q5=b_q5, q6=b_q6, ponte=b_ponte, cta=b_cta)
