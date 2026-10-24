"""Visual — Notação Científica, Episódio 5: prefixos (de tera a pico) e a armadilha de área e volume (iniciantes, tema claro).
Peças comuns em ../../comum.py (reexporta o 019/comum.py: expr com potências, fichas, atalho, alternativas, erro_cards...).
Peças deste episódio: escada vertical de prefixos, grade 100 × 100 com contador, cubo de cubinhos (isométrico), caixa d'água.
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
_s = importlib.util.spec_from_file_location("comum020", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_notacao_ep5_prefixos_area_volume.mp4"
CARD_R = K.CARD_R
AZULEJO = "#F4E6C8"
AGUA = "#5FA8E8"
CUBO_TOPO, CUBO_FRENTE, CUBO_LADO = "#C9DEF8", "#9CC3F0", "#7AAAE0"


def mil(n):
    """10000 -> '10 000' (espaço fino como separador de milhar)"""
    s = f"{int(n):,}".replace(",", " ")
    return s


def contador(c, cx, cy, valor, a, rotulo, col=None, size=84, w=380):
    if a <= 0:
        return
    col = col or BLUE
    card(c, cx - w / 2, cy - 100, w, 210, a)
    text_mid(c, mil(valor), cx, cy - 10, size, "black", col, a)
    text(c, rotulo, cx, cy + 78, 28, "black", INK2, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A ARMADILHA DA ÁREA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "1 m^2 =", 600, 400, 150, aa)
    ab = ep(t, C["01.b"], 0.5)
    acc = ep(t, C["01.c"], 0.5)
    if ab > 0:
        text_mid(c, "100 cm²", 1300, 400, 130, "black", RED, ab * (1 - 0.5 * acc))
        strike(c, 1050, 400, 1560, 400, acc, RED, acc)
    if acc > 0:
        chip(c, "erro por um fator de 100", 1300, 560, RED, acc, 40)
    ad = ep(t, C["01.d"], 0.5)
    selo(c, W / 2, 750, ad, "UM DOS ERROS MAIS CAROS DA PROVA", AMBER, -3, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "os prefixos, de tera a pico", "potências de 10 com apelido"),
            ("02.b", "converter área e volume", "sem cair na armadilha do fator")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")
    ac = ep(t, C["02.c"], 0.5)
    if ac > 0:
        boxed(c, 300, 640, 1320, 130, GREEN, ac, 0.08)
        _grade_mini(c, 400, 705, 90, 6, ac)
        text_mid(c, "sem decorar tabela: contando quadradinhos", 1010, 705, 40, "black", INK, ac)


def _grade_mini(c, cx, cy, s, n, a, col=None):
    col = col or BLUE
    x0, y0 = cx - s / 2, cy - s / 2
    rrect(c, x0, y0, s, s, 6, mix("#FFFFFF", col, 0.15), a)
    for k in range(n + 1):
        line(c, x0 + s * k / n, y0, x0 + s * k / n, y0 + s, col, a * 0.8, 2)
        line(c, x0, y0 + s * k / n, x0 + s, y0 + s * k / n, col, a * 0.8, 2)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    text(c, "POTÊNCIA DE POTÊNCIA", 560, 250, 30, "black", PURPLE, aa)
    expr(c, "(10^2)^2 = 10^2 · 10^2", 560, 380, 58, aa)
    ab = ep(t, C["03.b"], 0.5)
    expr(c, "= 10^{2·2} = 10^4", 560, 520, 58, ab, cores={1: GREEN})
    chip(c, "os expoentes se MULTIPLICAM", 560, 650, PURPLE, ab, 30)
    acc = ep(t, C["03.c"], 0.5)
    text(c, "MULTIPLICAR EM NOTAÇÃO CIENTÍFICA", 1360, 250, 30, "black", BLUE, acc)
    if acc > 0:
        text(c, "número com número · expoentes do 10 SOMAM", 1360, 320, 28, "bold", INK2, acc)
    ad = ep(t, C["03.d"], 0.5)
    expr(c, "3·10^2 · 10^3", 1360, 440, 58, ad)
    expr(c, "= 3·10^{2+3} = 3·10^5", 1360, 570, 58, ep(t, C["03.d"] + 1.6, 0.5), cores={1: GREEN})
    line(c, 960, 230, 960, 800, "#E6E6E2", acc, 3)


# ======================================================================
# a escada vertical de prefixos
# ======================================================================

PREF = [("tera", "T", "10^{12}", "terabyte"), ("giga", "G", "10^9", "gigabyte"), ("mega", "M", "10^6", "megawatt"),
        ("quilo", "k", "10^3", "quilômetro"), ("—", "", "10^0", "metro · grama · litro"),
        ("deci", "d", "10^{-1}", "decímetro"), ("centi", "c", "10^{-2}", "centímetro"), ("mili", "m", "10^{-3}", "miligrama"),
        ("micro", "μ", "10^{-6}", "micrograma"), ("nano", "n", "10^{-9}", "nanômetro"), ("pico", "p", "10^{-12}", "picossegundo")]
EX, EY, EW, EH = 190, 172, 820, 60


def _cor_pref(i):
    return PURPLE if i < 4 else (GRAY if i == 4 else BLUE)


def _escada(c, ativos, destaque=None, setas=None, rot_seta="× 1000"):
    """ativos = {i: alfa}; destaque = {i: 0..1}; setas = {i: alfa} (seta entre o degrau i e o i+1)"""
    destaque, setas = destaque or {}, setas or {}
    for i, (nome, sim, pot, ex) in enumerate(PREF):
        a = ativos.get(i, 0.0)
        if a <= 0:
            continue
        y = EY + i * EH
        col = _cor_pref(i)
        hl = destaque.get(i, 0.0)
        ind = abs(i - 4) * 18
        rrect(c, EX + ind, y, EW - 2 * ind, EH - 8, 12, mix("#FFFFFF", col, 0.08 + 0.18 * hl), a)
        rrect(c, EX + ind, y, 10, EH - 8, 5, col, a)
        text(c, nome, EX + ind + 40, y + 37, 30, "black", col if i != 4 else GRAY, a, align="left")
        if sim:
            text_mid(c, sim, EX + ind + 225, y + 26, 30, "black", INK, a)
        expr(c, pot, EX + 400, y + 26, 34, a, cores={0: col})
        text(c, ex, EX + EW - ind - 24, y + 36, 24, "bold", INK2, a, align="right")
    for i, sa in setas.items():
        if sa <= 0:
            continue
        x = EX + EW + 30
        y1, y2 = EY + (i + 1) * EH + 20, EY + i * EH + 20
        arrow(c, x, y1, x, y2 + 6, AMBER, sa, 4, 12, progress=sa)
        fmid(c, rot_seta, x + 70, (y1 + y2) / 2 + 2, 22, "black", AMBER, sa)


def _painel(c, a, linhas, x=1400, y0=300):
    """painel à direita: linhas = [(expr_ou_texto, tipo, cor)] — tipo 'm' (matemática) ou 't' (texto)"""
    for k, (s, tipo, col, ak) in enumerate(linhas):
        aa = a * ak
        if aa <= 0:
            continue
        y = y0 + k * 110
        if tipo == "m":
            expr(c, s, x, y, 50, aa, cores={i: col for i in range(12)})
        else:
            text_mid(c, s, x, y, 34, "black", col, aa)


def b_grandes(c, t, C, B):
    head_seq(c, t, C, [("04", "O QUE ELES TÊM EM COMUM?", "O PREFIXO", BLUE), ("05", "OS PREFIXOS GRANDES", "DE QUILO A TERA", PURPLE),
                       ("06", "ATALHO", "DE TRÊS EM TRÊS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05", "06"])
    if sid == "04":
        words = [("giga", "byte", "do celular"), ("quilô", "metro", "da estrada"), ("mili", "grama", "do remédio")]
        for k, (p_, r_, sub) in enumerate(words):
            a = ep(t, C["04"] + 0.6 * k, 0.5)
            x = 420 + k * 540
            wp, wr = text_w(p_, "black", 64), text_w(r_, "black", 64)
            x0 = x - (wp + wr) / 2
            aa = ep(t, C["04.a"], 0.5)
            if aa > 0:
                rrect(c, x0 - 12, 250, wp + 24, 100, 16, BLUE, 0.14 * aa)
            text(c, p_, x0, 322, 64, "black", mix(INK, BLUE, aa), a, align="left")
            text(c, r_, x0 + wp, 322, 64, "black", INK, a, align="left")
            text(c, sub, x, 390, 30, "bold", GRAY, a)
        aa = ep(t, C["04.a"], 0.5)
        chip(c, "PREFIXO = pedacinho colado na frente da unidade", W / 2, 500, BLUE, aa, 32)
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            boxed(c, 460, 590, 1000, 190, PURPLE, ab, 0.08)
            text(c, "prefixo = potência de 10 com APELIDO", W / 2, 655, 40, "black", PURPLE, ab)
            expr(c, "quilo = 10^3   ·   mega = 10^6   ·   nano = 10^{-9}", W / 2, 730, 40, ab)
        return
    if sid == "05":
        ativos = {4: ep(t, C["05"], 0.5), 3: ep(t, C["05.a"], 0.5), 2: ep(t, C["05.b"], 0.5), 1: ep(t, C["05.c"], 0.5),
                  0: ep(t, C["05.d"], 0.5)}
        k = 3 if t < C["05.b"] else 2 if t < C["05.c"] else 1 if t < C["05.d"] else 0
        _escada(c, ativos, {k: ep(t, C[["05.d", "05.c", "05.b", "05.a"][k]], 0.4)})
        exs = {3: ("1 km = 10^3 m", "mil metros"), 2: ("1 MW = 10^6 W", "um milhão de watts"),
               1: ("1 GB = 10^9 bytes", "um bilhão de bytes"), 0: ("1 TB = 10^{12} bytes", "o HD do computador")}
        s, sub = exs[k]
        a = ativos[k]
        expr(c, s, 1410, 440, 58, a, cores={3: PURPLE})
        text(c, sub, 1410, 540, 32, "bold", INK2, a)
        return
    # 06 atalho
    ativos = {i: 1.0 for i in range(5)}
    setas = {i: ep(t, C["06.c"] + 0.3 * (3 - i), 0.4) for i in range(4)}
    _escada(c, ativos, setas=setas)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        boxed(c, 1180, 200, 520, 600, GREEN, aa, 0.08)
        text(c, "ATALHO", 1440, 250, 22, "black", GREEN, aa, tracking=2)
        text(c, "de 3 em 3", 1440, 315, 44, "black", INK, aa)
        for j, (n, e) in enumerate([("quilo", "3"), ("mega", "6"), ("giga", "9"), ("tera", "12")]):
            ab = ep(t, C["06.b"] + 0.5 * j, 0.4)
            y = 400 + j * 80
            text(c, n, 1300, y, 36, "black", PURPLE, ab, align="left")
            text(c, e, 1600, y, 44, "black", GREEN, ab, align="right")
        text(c, "cada degrau: × 1000", 1440, 750, 30, "black", AMBER, ep(t, C["06.c"], 0.5))


def b_pequenos(c, t, C, B):
    head_seq(c, t, C, [("07", "OS PREFIXOS PEQUENOS", "EXPOENTE NEGATIVO", BLUE), ("08", "DESCENDO MAIS", "MICRO, NANO, PICO", BLUE),
                       ("09", "ATALHO", "O ESPELHO DOS GRANDES", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09"])
    base = {i: 0.35 for i in range(5)}
    if sid == "07":
        ativos = dict(base); ativos[4] = 1.0
        ativos.update({5: ep(t, C["07.a"], 0.5), 6: ep(t, C["07.b"], 0.5), 7: ep(t, C["07.c"], 0.5)})
        k = 5 if t < C["07.b"] else 6 if t < C["07.c"] else 7
        _escada(c, ativos, {k: 1.0})
        chip(c, "expoente negativo = DIVIDE", 1410, 250, BLUE, ep(t, C["07"], 0.5), 30)
        exs = {5: ("1 dm = 10^{-1} m", "um décimo do metro"), 6: ("1 cm = 10^{-2} m", "100 cabem num metro"),
               7: ("1 mg = 10^{-3} g", "o miligrama do remédio")}
        s, sub = exs[k]
        expr(c, s, 1410, 460, 54, ativos[k], cores={3: BLUE})
        text(c, sub, 1410, 560, 32, "bold", INK2, ativos[k])
        return
    if sid == "08":
        ativos = dict(base); ativos.update({4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0})
        ativos.update({8: ep(t, C["08.a"], 0.5), 9: ep(t, C["08.b"], 0.5), 10: ep(t, C["08.c"], 0.5)})
        k = 8 if t < C["08.b"] else 9 if t < C["08.c"] else 10
        _escada(c, ativos, {k: 1.0})
        exs = {8: ("1 μg = 10^{-6} g", "μ = a letra grega “mi”"), 9: ("1 nm = 10^{-9} m", "a escala de um vírus"),
               10: ("1 ps = 10^{-12} s", "o picossegundo")}
        s, sub = exs[k]
        expr(c, s, 1410, 460, 54, ativos[k], cores={3: BLUE})
        text(c, sub, 1410, 560, 32, "bold", INK2, ativos[k])
        return
    # 09 atalho espelho
    ativos = {i: 1.0 for i in range(11)}
    setas = {i: ep(t, C["09.b"] + 0.5 * (i - 7), 0.4) for i in range(7, 10)}
    ac = ep(t, C["09.c"], 0.5)
    _escada(c, ativos, {5: ac, 6: ac}, setas=setas, rot_seta="÷ 1000")
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        boxed(c, 1180, 200, 520, 440, GREEN, aa, 0.08)
        text(c, "ATALHO", 1440, 250, 22, "black", GREEN, aa, tracking=2)
        text(c, "a partir do mili: de 3 em 3", 1440, 310, 32, "black", INK, aa)
        for j, (n, e) in enumerate([("mili", "−3"), ("micro", "−6"), ("nano", "−9"), ("pico", "−12")]):
            ab = ep(t, C["09.b"] + 0.5 * j, 0.4)
            y = 390 + j * 66
            text(c, n, 1300, y, 34, "black", BLUE, ab, align="left")
            text(c, e, 1600, y, 40, "black", GREEN, ab, align="right")
    if ac > 0:
        boxed(c, 1180, 670, 520, 130, AMBER, ac, 0.10)
        text(c, "fogem da regra:", 1440, 718, 28, "black", AMBER, ac)
        text(c, "deci −1 · centi −2", 1440, 770, 34, "black", INK, ac)


# ======================================================================
# bloco C — a grade de quadradinhos (área)
# ======================================================================

GX, GY, GS = 250, 195, 620   # quadrado de 1 m na tela


def _grade(c, a, n_cel=0, col_fill=None, linhas=True, n=100):
    """o quadrado de 1 m com a grade 100 × 100; n_cel = quantos quadradinhos de 1 cm já estão pintados (por fileira)"""
    if a <= 0:
        return
    col_fill = col_fill or BLUE
    rrect(c, GX, GY, GS, GS, 4, "#FFFFFF", a, shadow=True)
    cel = GS / n
    rows = int(n_cel // n)
    rest = n_cel - rows * n
    if rows > 0:
        c.drawRect(skia.Rect.MakeXYWH(GX, GY, GS, rows * cel), paint(mix("#FFFFFF", col_fill, 0.45), a))
    if rest > 0:
        c.drawRect(skia.Rect.MakeXYWH(GX, GY + rows * cel, rest * cel, cel), paint(mix("#FFFFFF", col_fill, 0.75), a))
    if linhas:
        pg = paint("#C9D6E8", a * 0.9, stroke=0.8)
        for k in range(n + 1):
            x = GX + k * cel
            c.drawLine(x, GY, x, GY + GS, pg)
            c.drawLine(GX, GY + k * cel, GX + GS, GY + k * cel, pg)
    c.drawRect(skia.Rect.MakeXYWH(GX, GY, GS, GS), paint(INK, a, stroke=4))


def _cota_h(c, x0, x1, y, s, a, col=None):
    col = col or INK2
    line(c, x0, y, x1, y, col, a, 3); line(c, x0, y - 10, x0, y + 10, col, a, 3); line(c, x1, y - 10, x1, y + 10, col, a, 3)
    text(c, s, (x0 + x1) / 2, y - 16, 28, "black", col, a)


def _cota_v(c, x, y0, y1, s, a, col=None):
    col = col or INK2
    line(c, x, y0, x, y1, col, a, 3); line(c, x - 10, y0, x + 10, y0, col, a, 3); line(c, x - 10, y1, x + 10, y1, col, a, 3)
    text(c, s, x + 22, (y0 + y1) / 2 + 10, 28, "black", col, a, align="left")


def _piso(c, x, y, cols, rows, s, a):
    for i in range(cols):
        for j in range(rows):
            rrect(c, x + i * s, y + j * s, s - 6, s - 6, 6, mix(AZULEJO, "#FFFFFF", 0.3 * ((i + j) % 2)), a)


def b_area(c, t, C, B):
    head_seq(c, t, C, [("10", "A ARMADILHA DA ÁREA", "O PISO DE AZULEJOS", BLUE), ("11", "QUANTOS QUADRADINHOS?", "CONTE A GRADE", AMBER),
                       ("12", "A REGRA", "O FATOR VAI AO QUADRADO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11", "12"])
    if sid == "10":
        a0 = ep(t, C["10"], 0.5)
        _piso(c, 220, 210, 6, 5, 100, a0)
        text(c, "piso de azulejos", 515, 760, 30, "black", INK2, a0)
        aa = ep(t, C["10.a"], 0.5)
        chip(c, "ÁREA = quanto de chão a figura cobre", 1300, 260, BLUE, aa, 30)
        text(c, "medida em quadradinhos", 1300, 330, 28, "bold", INK2, aa)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            rrect(c, 1010, 400, 260, 260, 4, mix("#FFFFFF", BLUE, 0.12), ab)
            c.drawRect(skia.Rect.MakeXYWH(1010, 400, 260, 260), paint(INK, ab, stroke=3))
            text(c, "1 m", 1140, 390, 26, "black", INK2, ab)
            expr(c, "1 m^2", 1140, 540, 52, ab, cores={0: BLUE})
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            rrect(c, 1440, 600, 40, 40, 3, mix("#FFFFFF", BLUE, 0.4), acc)
            c.drawRect(skia.Rect.MakeXYWH(1440, 600, 40, 40), paint(INK, acc, stroke=2))
            text(c, "1 cm", 1460, 590, 22, "black", INK2, acc)
            expr(c, "1 cm^2", 1560, 560, 40, acc, cores={0: BLUE}, align="left")
            text(c, "≈ uma unha", 1560, 650, 26, "bold", INK2, acc, align="left")
        return
    if sid == "11":
        a0 = ep(t, C["11"], 0.4)
        ta, tc = C["11.a"], C["11.c"]
        n1 = 100 * clamp((t - ta) / 2.4)
        nr = 99 * clamp((t - tc) / 3.2)
        cells = n1 + nr * 100 if t >= tc else n1
        _grade(c, a0, cells)
        _cota_h(c, GX, GX + GS, GY - 14, "1 m = 100 cm", ep(t, C["11.a"], 0.4), BLUE)
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            text(c, "1ª fileira: 100", GX + GS + 30, GY + 12, 26, "black", BLUE, aa, align="left")
        ab = ep(t, C["11.b"], 0.5) * (1 - ep(t, C["11.c"], 0.4))
        if ab > 0:
            selo(c, 1430, 640, ab, "quase todo mundo para aqui", AMBER, -4, 30)
        acc = ep(t, C["11.c"], 0.5)
        _cota_v(c, GX + GS + 30, GY + 40, GY + GS, "100 fileiras", acc, AMBER)
        contador(c, 1420, 350, round(cells), aa, "quadradinhos de 1 cm²", GREEN if cells >= 9999.5 else BLUE)
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            rrect(c, 1150, 560, 540, 100, 18, "#FFFFFF", ad, shadow=True)
            expr(c, "100 × 100 = 10 000", 1420, 610, 48, ad, cores={4: GREEN})
        return
    # 12 regra
    a0 = ep(t, C["12"], 0.5)
    if a0 > 0:
        boxed(c, 460, 200, 1000, 150, PURPLE, a0, 0.08)
        expr(c, "1 m^2 = 10^4 cm^2", W / 2, 275, 72, a0, cores={3: PURPLE})
    aa = ep(t, C["12.a"], 0.5)
    expr(c, "1 m = 10^2 cm", 640, 470, 56, aa, cores={3: BLUE})
    text(c, "comprimento", 640, 550, 28, "black", INK2, aa)
    ab = ep(t, C["12.b"], 0.5)
    expr(c, "(10^2)^2 = 10^4", 1280, 470, 56, ab, cores={2: PURPLE})
    text(c, "na área: AO QUADRADO", 1280, 550, 28, "black", PURPLE, ab)
    if ab > 0:
        arrow(c, 880, 460, 1040, 460, AMBER, ab, 5, 16, progress=ab)
    K.atalho(c, 460, 610, 1000, 190, "ATALHO", ["em área: DOBRE o expoente do fator  (2 → 4)"], ep(t, C["12.c"], 0.5), 34)


# ======================================================================
# bloco D — o cubo de cubinhos (volume)
# ======================================================================

def _iso(cx, cy, s, x, y, z):
    """projeção isométrica: x para a direita-baixo, z para a esquerda-baixo, y para cima (0..1)"""
    return cx + (x - z) * s * 0.866, cy + (x + z) * s * 0.5 - y * s


def _poly(c, pts, col, a, stroke=None):
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    p.close()
    if stroke:
        c.drawPath(p, paint(col, a, stroke=stroke))
    else:
        c.drawPath(p, paint(col, a))


def _caixa(c, cx, cy, s, X, Y, Z, a, cores=(CUBO_TOPO, CUBO_FRENTE, CUBO_LADO), div=10, borda=None):
    """paralelepípedo [0,X]×[0,Y]×[0,Z] com faces visíveis (topo, frente = z máx, lado = x máx) e linhas de cubinhos"""
    if a <= 0 or X <= 0 or Y <= 0 or Z <= 0:
        return
    P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
    top = [P(0, Y, 0), P(X, Y, 0), P(X, Y, Z), P(0, Y, Z)]
    front = [P(0, 0, Z), P(X, 0, Z), P(X, Y, Z), P(0, Y, Z)]
    side = [P(X, 0, 0), P(X, 0, Z), P(X, Y, Z), P(X, Y, 0)]
    _poly(c, top, cores[0], a); _poly(c, front, cores[1], a); _poly(c, side, cores[2], a)
    pg = paint("#FFFFFF", a * 0.55, stroke=1.2)
    st = 1.0 / div
    k = st
    while k < X - 1e-6:
        c.drawLine(*P(k, 0, Z), *P(k, Y, Z), pg); c.drawLine(*P(k, Y, 0), *P(k, Y, Z), pg); k += st
    k = st
    while k < Y - 1e-6:
        c.drawLine(*P(0, k, Z), *P(X, k, Z), pg); c.drawLine(*P(X, k, 0), *P(X, k, Z), pg); k += st
    k = st
    while k < Z - 1e-6:
        c.drawLine(*P(X, 0, k), *P(X, Y, k), pg); c.drawLine(*P(0, Y, k), *P(X, Y, k), pg); k += st
    bc = borda or "#3E6FA8"
    for poly in (top, front, side):
        _poly(c, poly, bc, a, stroke=2.5)


def _cubo_vazio(c, cx, cy, s, a):
    P = lambda x, y, z: _iso(cx, cy, s, x, y, z)
    pe = paint(GRAY, a * 0.8, stroke=2.5)
    pe.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
    corners = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1), (0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    for i, j in edges:
        c.drawLine(*P(*corners[i]), *P(*corners[j]), pe)


def _tanque(c, cx, y_top, w, h, a, nivel=1.0, rotulo="1 000 L"):
    """caixa d'água (vista de frente, levemente em perspectiva) com nível de água 0..1"""
    if a <= 0:
        return
    rx, ry = w / 2, w * 0.14
    body = skia.Rect.MakeXYWH(cx - rx, y_top, w, h)
    c.drawRect(body, paint("#E9EEF4", a))
    if nivel > 0:
        hy = y_top + h * (1 - nivel)
        c.drawRect(skia.Rect.MakeXYWH(cx - rx, hy, w, y_top + h - hy), paint(AGUA, a * 0.85))
        c.drawOval(skia.Rect.MakeXYWH(cx - rx, hy - ry, w, 2 * ry), paint(mix(AGUA, "#FFFFFF", 0.3), a))
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top + h - ry, w, 2 * ry), paint(AGUA if nivel > 0 else "#E9EEF4", a))
    pe = paint("#5B6B7D", a, stroke=4)
    c.drawLine(cx - rx, y_top, cx - rx, y_top + h, pe); c.drawLine(cx + rx, y_top, cx + rx, y_top + h, pe)
    c.drawArc(skia.Rect.MakeXYWH(cx - rx, y_top + h - ry, w, 2 * ry), 0, 180, False, pe)
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top - ry, w, 2 * ry), paint("#CFD8E2", a))
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, y_top - ry, w, 2 * ry), pe)
    c.drawOval(skia.Rect.MakeXYWH(cx - rx * 0.35, y_top - ry * 0.45, rx * 0.7, ry * 0.9), paint("#5B6B7D", a, stroke=3))
    if rotulo:
        rrect(c, cx - 110, y_top + h * 0.38, 220, 70, 14, "#FFFFFF", a * 0.95)
        text_mid(c, rotulo, cx, y_top + h * 0.38 + 35, 38, "black", INK, a)


def b_volume(c, t, C, B):
    head_seq(c, t, C, [("13", "E O VOLUME?", "A CAIXA D'ÁGUA", BLUE), ("14", "O CUBO DE CUBINHOS", "100 × 100 × 100", AMBER),
                       ("15", "A REGRA", "O FATOR VAI AO CUBO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14", "15"])
    if sid == "13":
        a0 = ep(t, C["13"], 0.5)
        _tanque(c, 500, 300, 380, 400, a0, 0.75, rotulo=None)
        text(c, "caixa d'água", 500, 790, 30, "black", INK2, a0)
        aa = ep(t, C["13.a"], 0.5)
        chip(c, "VOLUME = o espaço que a coisa ocupa", 1300, 260, BLUE, aa, 30)
        text(c, "medido em cubinhos", 1300, 330, 28, "bold", INK2, aa)
        ab = ep(t, C["13.b"], 0.5)
        _caixa(c, 1130, 540, 150, 1, 1, 1, ab, div=1)
        expr(c, "1 m^3", 1130, 760, 46, ab, cores={0: BLUE})
        acc = ep(t, C["13.c"], 0.5)
        _caixa(c, 1530, 640, 40, 1, 1, 1, acc, div=1)
        expr(c, "1 cm^3", 1530, 730, 40, acc, cores={0: BLUE})
        text(c, "≈ um dado pequeno", 1530, 790, 24, "bold", INK2, acc)
        return
    if sid == "14":
        a0 = ep(t, C["14"], 0.4)
        cx, cy, s = 560, 430, 330
        _cubo_vazio(c, cx, cy, s, a0)
        ta, tb, tcc = C["14.a"], C["14.b"], C["14.c"]
        fx = clamp((t - ta) / 1.6)
        fz = clamp((t - tb) / 2.0) if t >= tb else 0.0
        fy = clamp((t - tcc) / 3.0) if t >= tcc else 0.0
        X = fx
        Z = 0.01 + 0.99 * fz if t >= tb else 0.01 * fx
        Y = 0.01 + 0.99 * fy
        if t >= ta:
            _caixa(c, cx, cy, s, max(X, 0.001), Y, max(Z, 0.01), a0, div=10)
        n = 100 * fx if t < tb else (100 + 9900 * fz if t < tcc else 10000 + 990000 * fy)
        n = round(n)
        contador(c, 1420, 330, n, ep(t, ta, 0.4), "cubinhos de 1 cm³", GREEN if n >= 1000000 else BLUE, size=76, w=440)
        etapas = [("14.a", "1 fileira: 100"), ("14.b", "1 camada: 100 × 100 = 10 000"), ("14.c", "100 camadas")]
        for j, (cue, s_) in enumerate(etapas):
            ak = ep(t, C[cue], 0.4)
            text(c, s_, 1420, 500 + j * 52, 30, "black", INK if j < 2 else AMBER, ak)
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            rrect(c, 1100, 650, 640, 80, 18, "#FFFFFF", ad, shadow=True)
            expr(c, "100 × 100 × 100 = 1 000 000", 1420, 690, 40, ad, cores={6: GREEN})
        ae = ep(t, C["14.e"], 0.5)
        if ae > 0:
            boxed(c, 1100, 750, 640, 70, PURPLE, ae, 0.10)
            expr(c, "1 m^3 = 10^6 cm^3", 1420, 785, 40, ae, cores={3: PURPLE})
        return
    # 15 regra + tabela comprimento/área/volume
    a0 = ep(t, C["15"], 0.5)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 460, 200, 1000, 140, PURPLE, aa, 0.08)
        expr(c, "(10^2)^3 = 10^6", W / 2, 270, 70, aa, cores={2: PURPLE})
    ab = ep(t, C["15.b"], 0.5)
    rows = [("comprimento", "1 m = 10^2 cm", "normal", INK2), ("área", "1 m^2 = 10^4 cm^2", "DOBRA", GREEN),
            ("volume", "1 m^3 = 10^6 cm^3", "TRIPLICA", GREEN)]
    if ab > 0:
        boxed(c, 300, 380, 1320, 300, GREEN, ab, 0.06)
        text(c, "ATALHO", W / 2, 420, 22, "black", GREEN, ab, tracking=2)
    for j, (nome, s_, tag, col) in enumerate(rows):
        ak = ep(t, C["15.b"] + 0.7 * j, 0.4) if ab > 0 else 0
        y = 480 + j * 72
        text(c, nome, 360, y + 12, 34, "black", INK, ak, align="left")
        expr(c, s_, 960, y, 42, ak)
        chip(c, tag, 1480, y, col, ak, 28)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        boxed(c, 460, 710, 1000, 100, AMBER, acc, 0.10)
        text_mid(c, "unidade MENOR → número MAIOR", W / 2, 760, 38, "black", INK, acc)


# ======================================================================
# bloco E — quilômetro
# ======================================================================

def b_km(c, t, C, B):
    frame(c, t, B["start"], "QUALQUER PREFIXO", "O MESMO COM QUILÔMETRO", PURPLE)
    rows = [("16.a", "1 km = 10^3 m", "comprimento", "", BLUE), ("16.b", "1 km^2 = (10^3)^2 = 10^6 m^2", "área", "ao quadrado", PURPLE),
            ("16.c", "1 km^3 = (10^3)^3 = 10^9 m^3", "volume", "ao cubo", PURPLE)]
    for j, (cue, s, nome, tag, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        text(c, nome, 300, y + 14, 34, "black", INK2, a, align="left")
        expr(c, s, 1010, y, 64, a, cores={len(s.split()) - 2: col})
        if tag:
            chip(c, tag, 1620, y, col, a, 26)


# ======================================================================
# bloco F — equivalências
# ======================================================================

def b_equiv(c, t, C, B):
    head_seq(c, t, C, [("17", "CAPACIDADE", "O LITRO", BLUE), ("18", "A MAIS IMPORTANTE", "1 m³ = 1 000 LITROS", PURPLE),
                       ("19", "NO CAMPO", "O HECTARE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["17", "18", "19"])
    if sid == "17":
        aa = ep(t, C["17.a"], 0.5)
        chip(c, "CAPACIDADE = o quanto cabe dentro · em LITROS", W / 2, 215, BLUE, aa, 30)
        ab = ep(t, C["17.b"], 0.5)
        _caixa(c, 640, 470, 200, 1, 1, 1, ab, div=10)
        if ab > 0:
            text(c, "10 cm de lado", 640, 690, 26, "black", INK2, ab)
            boxed(c, 380, 700, 520, 100, PURPLE, ab, 0.08)
            expr(c, "1 L = 1 dm^3", 640, 750, 52, ab, cores={0: PURPLE, 1: PURPLE})
        acc = ep(t, C["17.c"], 0.5)
        _caixa(c, 1380, 520, 60, 1, 1, 1, acc, div=1)
        if acc > 0:
            text(c, "1 cm", 1300, 590, 24, "black", INK2, acc)
            boxed(c, 1120, 700, 520, 100, PURPLE, acc, 0.08)
            expr(c, "1 mL = 1 cm^3", 1380, 750, 52, acc, cores={0: PURPLE, 1: PURPLE})
            text(c, "o dado pequeno", 1380, 420, 28, "bold", INK2, acc)
        return
    if sid == "18":
        aa = ep(t, C["18.a"], 0.5)
        if aa > 0:
            boxed(c, 220, 200, 880, 130, PURPLE, aa, 0.08)
            expr(c, "1 m^3 = 1 000 L", 660, 265, 70, aa, cores={3: PURPLE, 4: PURPLE})
        ab = ep(t, C["18.b"], 0.5)
        expr(c, "1 m = 10 dm", 660, 420, 50, ab, cores={3: BLUE})
        expr(c, "10 × 10 × 10 = 1 000 dm^3", 660, 540, 50, ep(t, C["18.b"] + 1.5, 0.5), cores={6: GREEN, 7: GREEN})
        acc = ep(t, C["18.c"], 0.5)
        expr(c, "= 1 000 L", 660, 650, 56, acc, cores={1: GREEN, 2: GREEN})
        ad = ep(t, C["18.d"], 0.5)
        nivel = clamp((t - C["18.d"]) / 2.5)
        _tanque(c, 1400, 300, 420, 420, ad, nivel)
        text(c, "a caixa d'água do telhado", 1400, 800, 28, "black", INK2, ad)
        return
    # 19 hectare
    a0 = ep(t, C["19"], 0.5)
    aa = ep(t, C["19.a"], 0.5)
    x0, y0, s = 260, 230, 520
    if aa > 0:
        rrect(c, x0, y0, s, s, 4, mix("#FFFFFF", GREEN, 0.18), aa, shadow=True)
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, s, s), paint(INK, aa, stroke=4))
        _cota_h(c, x0, x0 + s, y0 - 14, "100 m", aa, GREEN)
        _cota_v(c, x0 + s + 24, y0, y0 + s, "100 m", aa, GREEN)
        text_mid(c, "1 hectare", x0 + s / 2, y0 + s / 2, 50, "black", GREEN, aa)
        expr(c, "100 × 100 = 10^4 m^2", 1290, 330, 52, aa, cores={4: GREEN, 5: GREEN})
        chip(c, "1 ha = área de um quadrado de 100 m de lado", 1290, 420, BLUE, aa, 26)
    ab = ep(t, C["19.b"], 0.5)
    if ab > 0:
        gx, gy, gs = 1060, 480, 300
        rrect(c, gx, gy, gs, gs, 4, "#FFFFFF", ab, shadow=True)
        for i in range(10):
            for j in range(10):
                aij = ab * ep(t, C["19.b"] + 0.02 * (i * 10 + j), 0.2)
                rrect(c, gx + 3 + i * 29.4, gy + 3 + j * 29.4, 26, 26, 3, mix("#FFFFFF", GREEN, 0.35), aij)
        c.drawRect(skia.Rect.MakeXYWH(gx, gy, gs, gs), paint(INK, ab, stroke=3))
        text(c, "1 km²", gx + gs / 2, gy + gs + 44, 30, "black", INK, ab)
        expr(c, "1 km^2 = 10^6 m^2", 1580, 560, 40, ab)
        text(c, "= 100 hectares", 1580, 660, 40, "black", GREEN, ab)


# ======================================================================
# nós fazemos
# ======================================================================

EXS = [("20.a", "3 m^2 = ? cm^2", "3·10^4 cm^2", "cada m² = 10⁴ cm²"), ("20.b", "2 m^3 = ? L", "2 000 L", "cada m³ = 1 000 L")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("20", "SUA VEZ", "PAUSE E CONVERTA", GREEN), ("21", "VAMOS CONFERIR", "PAUSE E CONVERTA", GREEN)])
    card(c, *CARD_R)
    for k, (cue, q, r, why) in enumerate(EXS):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 330, 210, 660, 260, 24, "#F7F7F5", a)
        text(c, f"{k + 1}ª CONVERSÃO", x, 255, 22, "black", GRAY, a, tracking=1)
        expr(c, q, x, 360, 62, a)
        if t >= C["21"]:
            ra = ep(t, C["21." + "ab"[k]], 0.5)
            expr(c, r, x, 590, 76, ra, cores={i: GREEN for i in range(4)})
            text(c, why, x, 700, 28, "bold", INK2, ra)
    pause_timer(c, t, C["20.end"] - 1.9, W / 2, 620)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Prefixo é potência de 10 com apelido.", "Área: o fator vai ao quadrado. Volume: ao cubo.",
          "1 m³ são 1 000 litros."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["22", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "22" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("1 m² = 100 cm²", "um metro tem 100 centímetros", "isso é UMA fileira; são 100 fileiras: 10 000 cm²"),
         ("1 m³ = 100 cm³ (ou 10 000 cm³)", "são os números que a gente já viu", "o cubo tem 3 direções: 100 × 100 × 100 = 1 000 000 cm³"),
         ("confundir mili com micro", "os dois começam com m e os dois são pequenos",
          "mili = 10⁻³ e micro = 10⁻⁶: mil vezes menor")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["23", "24", "25"], ERROS)


# ======================================================================
# Questão 6 do material
# ======================================================================

ALTS = [("A", "= 2,5·10^5", "usou 10² em vez de 10⁴", RED), ("B", "= 2,5·10^6", "usou 10³: centi virou mili", RED),
        ("C", "= 2,5·10^7", "", GREEN), ("D", "= 2,5·10^9", "fator ao cubo: é volume", RED),
        ("E", "= 2,5·10^1", "dividiu em vez de multiplicar", RED)]
ENUNCIADO = "Um terreno retangular tem área de 2,5 · 10³ m². Essa área, expressa em centímetros quadrados, corresponde a"


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · CONVERSÃO DE ÁREA", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    para(c, ENUNCIADO, 190, 250, 36, "black", INK, a0, 640, 50)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["28.xa"], "B": C["28.xb"], "D": C["28.xd"], "E": C["28.xe"]}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS, 920, 210, 780, 40, C["27.ok"], "C", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["26.end"] - 1.9, 470, 640)
    if t >= C["27"]:
        ra = ep(t, C["27"], 0.4)
        rrect(c, 170, 470, 700, 330, 18, "#FFFFFF", ra, shadow=True)
        expr(c, "1 m^2 = (10^2)^2 = 10^4 cm^2", 520, 525, 36, ep(t, C["27.a"], 0.4), cores={5: PURPLE})
        expr(c, "2,5·10^3 · 10^4", 520, 615, 40, ep(t, C["27.b"], 0.4))
        expr(c, "3 + 4 = 7", 520, 690, 36, ep(t, C["27.c"], 0.4), cores={4: GREEN})
        expr(c, "= 2,5·10^7 cm^2", 520, 765, 44, ep(t, C["27.d"], 0.4), cores={1: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO E TREINO", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    text(c, "juntamos tudo", W / 2, 300, 56, "black", INK, aa)
    ab = ep(t, C["30.b"], 0.5)
    selo(c, W / 2, 420, ab, "PEGADINHAS", AMBER, -4, 40)
    areas = [("Matemática", BLUE), ("Física", PURPLE), ("Química", GREEN), ("Biologia", AMBER)]
    for k, (s, col) in enumerate(areas):
        a = ep(t, C["30.c"] + 0.4 * k, 0.4)
        x = 420 + k * 360
        card(c, x - 160, 540, 320, 150, a)
        text_mid(c, s, x, 615, 40, "black", col, a)
    pill(c, "ep. 6 · revisão geral e treino para o ENEM", W / 2, 780, PURPLE, size=32, a=ep(t, C["30.c"] + 1.8, 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Você achava que 1 m² tinha 100 cm²?",
        canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, grandes=b_grandes, pequenos=b_pequenos, area=b_area,
              volume=b_volume, km=b_km, equiv=b_equiv, exercicio=b_exercicio, recap=b_recap, erros=b_erros,
              questao=b_questao, ponte=b_ponte, cta=b_cta)
