"""Visual — Potenciação e Radiciação, Episódio 3: Potências de base 10 (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (tipografia de potências no expr, contador, escada, atalho...).
Peças próprias: `numeral()` = o "1 com zeros" (zeros entram um a um / a vírgula corre para a esquerda) e `cubo()`.
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
_s = importlib.util.spec_from_file_location("comum019", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_potenciacao_ep3_base_10.mp4"
CARD_R = K.CARD_R


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# o "1 com zeros"
# ======================================================================

def numeral(c, cx, cy, size, zeros, a=1.0, col_um=None, col_zero=None, pop=1.0):
    """1 seguido de `zeros` zeros (agrupados de 3 em 3), centrado em cx. `pop` = entrada do último zero (0–1)."""
    if a <= 0:
        return
    col_um, col_zero = col_um or INK, col_zero or BLUE
    dw = size * 0.62
    grp = size * 0.22
    chars = ["1"] + ["0"] * zeros
    n = len(chars)
    # posições: grupos de 3 contados da direita
    xs, x = [], 0.0
    for i in range(n):
        xs.append(x)
        x += dw
        rest = n - 1 - i
        if rest > 0 and rest % 3 == 0:
            x += grp
    total = x
    x0 = cx - total / 2
    for i, ch in enumerate(chars):
        ai = a * (pop if (i == n - 1 and zeros > 0) else 1.0)
        dy = (1 - (pop if i == n - 1 and zeros > 0 else 1.0)) * -30
        text_mid(c, ch, x0 + xs[i] + dw / 2, cy + dy, size, "black", col_um if i == 0 else col_zero, ai)


def decimal(c, cx, cy, size, casas, a=1.0, mov=1.0, col=None, marcar=0.0):
    """0,00…1 com `casas` casas decimais; o 1 fica parado e a vírgula 'corre' para a esquerda (mov = progresso do último
    passo). marcar > 0 numera as casas embaixo."""
    if a <= 0:
        return
    col = col or BLUE
    dw = size * 0.62
    cw = size * 0.32
    x1 = cx + dw * 1.5           # centro do algarismo 1 (fixo)
    # algarismos à esquerda do 1: casas-1 zeros decimais + o 0 inteiro
    if casas == 0:
        text_mid(c, "1", x1, cy, size, "black", INK, a)
        return
    for k in range(1, casas):
        ak = a * (mov if k == casas - 1 else 1.0)
        text_mid(c, "0", x1 - k * dw, cy, size, "black", INK, ak)
    text_mid(c, "1", x1, cy, size, "black", col, a)
    # vírgula: entre o 0 inteiro e a 1ª casa
    xv_new = x1 - (casas - 1) * dw - dw / 2 - cw / 2
    xv_old = x1 - (casas - 2) * dw - dw / 2 - cw / 2 if casas > 1 else x1 + dw / 2 + cw / 2
    xv = lerp(xv_old, xv_new, mov)
    text_mid(c, ",", xv, cy, size, "black", AMBER, a)
    text_mid(c, "0", xv - cw / 2 - dw / 2, cy, size, "black", INK, a)
    if marcar > 0:
        for k in range(casas):
            xx = x1 - (casas - 1 - k) * dw
            badge_num(c, k + 1, xx, cy + size * 0.75, a * ep(marcar, 0.25 * k, 0.25), 22, bg=BLUE)


def cubo(c, cx, cy, s, a=1.0, col=None, rot="", rot_col=None, cheio=0.0):
    """cubo em perspectiva simples, aresta s px; `rot` = rótulo da aresta; cheio = preenchimento (volume)."""
    if a <= 0:
        return
    col = col or BLUE
    d = s * 0.45
    x0, y0 = cx - (s + d) / 2, cy - (s - d) / 2
    front = skia.Path(); front.addRect(skia.Rect.MakeXYWH(x0, y0, s, s))
    top = skia.Path(); top.moveTo(x0, y0); top.lineTo(x0 + d, y0 - d); top.lineTo(x0 + s + d, y0 - d); top.lineTo(x0 + s, y0); top.close()
    side = skia.Path(); side.moveTo(x0 + s, y0); side.lineTo(x0 + s + d, y0 - d); side.lineTo(x0 + s + d, y0 + s - d)
    side.lineTo(x0 + s, y0 + s); side.close()
    for pth, f in ((front, 0.10 + 0.25 * cheio), (top, 0.18 + 0.25 * cheio), (side, 0.26 + 0.25 * cheio)):
        c.drawPath(pth, paint(col, a * f))
        c.drawPath(pth, paint(col, a, stroke=4))
    if rot:
        line(c, x0, y0 + s + 28, x0 + s, y0 + s + 28, rot_col or AMBER, a, 4)
        line(c, x0, y0 + s + 16, x0, y0 + s + 40, rot_col or AMBER, a, 4)
        line(c, x0 + s, y0 + s + 16, x0 + s, y0 + s + 40, rot_col or AMBER, a, 4)
        ftext(c, rot, x0 + s / 2, y0 + s + 80, 30, "black", rot_col or AMBER, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "POTÊNCIAS DE 10", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "1 000 000 × 0,001 = ?", W / 2, 330, 104, aa, cores={3: AMBER, 6: AMBER})
    ab = ep(t, C["01.b"], 0.5) * (1 - ep(t, C["01.c"], 0.4))
    selo(c, 1500, 470, ab, "calculadora?", AMBER, -6, 40)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        # cronômetro de 3 segundos
        cx, cy, r = 640, 590, 80
        c.drawCircle(cx, cy, r, paint("#FFFFFF", acc))
        c.drawCircle(cx, cy, r, paint(GREEN, acc, stroke=8))
        u = prog(t, C["01.c"] + 0.3, 3.0)
        pth = skia.Path(); pth.addArc(skia.Rect(cx - r + 14, cy - r + 14, cx + r - 14, cy + r - 14), -90, 360 * u)
        c.drawPath(pth, paint(GREEN, acc, stroke=14))
        text_mid(c, "3 s", cx, cy, 44, "black", INK, acc)
        text(c, "de cabeça", 900, 600, 50, "black", GREEN, acc, align="left")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        boxed(c, 560, 720, 800, 100, GREEN, ad, 0.10)
        text_mid(c, "é só SOMAR dois números", W / 2, 770, 44, "black", INK, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "ler potências de 10", "10^6 = 1 000 000 · 10^{-3} = 0,001"),
            ("02.b", "multiplicar e dividir de cabeça", "soma e subtrai os expoentes")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 340 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 54, "black", INK, a, align="left")
        expr(c, sub, 360, y + 70, 34, a, align="left", cores=mono(sub, GRAY)) if "^" in sub else \
            text(c, sub, 360, y + 66, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "DOS EPISÓDIOS 1 E 2", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    expr(c, "a^m · a^n = a^{m+n}", 560, 300, 64, aa, cores={4: PURPLE})
    text(c, "multiplicou: SOMA", 560, 390, 30, "black", PURPLE, aa)
    expr(c, "a^m ÷ a^n = a^{m-n}", 1360, 300, 64, aa, cores={4: PURPLE})
    text(c, "dividiu: SUBTRAI", 1360, 390, 30, "black", PURPLE, aa)
    ab = ep(t, C["03.b"], 0.5)
    expr(c, "(a^m)^n = a^{m·n}", 560, 560, 64, ab, cores={2: PURPLE})
    text(c, "potência de potência: MULTIPLICA", 560, 650, 30, "black", PURPLE, ab)
    acc = ep(t, C["03.c"], 0.5)
    expr(c, "2^{-3} = 1/8", 1360, 560, 64, acc, cores={2: GREEN})
    text(c, "negativo INVERTE (não deixa negativo)", 1360, 650, 30, "black", GREEN, acc)
    line(c, 960, 230, 960, 760, "#E6E6E2", aa, 3)


# ======================================================================
# blocos 04–06 — zeros demais e o contador de zeros
# ======================================================================

NOTICIAS = [("04.a", "população do Brasil", "200 000 000", "pessoas"), ("04.b", "tamanho de um vírus", "0,0000001", "metro"),
            ("04.c", "luz de uma cidade", "7 200 000 000", "kWh por ano")]


def b_zeros(c, t, C, B):
    head_seq(c, t, C, [("04", "NÚMEROS DO NOTICIÁRIO", "ZEROS DEMAIS", AMBER), ("05", "POTÊNCIA DE 10", "O CONTADOR DE ZEROS", BLUE),
                       ("06", "ATALHO", "TRÊS NOMES PARA GUARDAR", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05", "06"])
    if sid == "04":
        ad = ep(t, C["04.d"], 0.5)
        for k, (cue, nome, num, un) in enumerate(NOTICIAS):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 260 + k * 150
            text(c, nome, 220, y + 12, 32, "black", INK2, a, align="left")
            # zeros piscando em âmbar no "zeros demais"
            x = 760
            for ch in num:
                colz = mix(INK, AMBER, ad) if ch == "0" else INK
                text(c, ch, x, y + 20, 64, "black", colz, a, align="left")
                x += text_w(ch, "black", 64) + (0 if ch != " " else -6)
            text(c, un, x + 24, y + 14, 30, "bold", GRAY, a, align="left")
        if ad > 0:
            selo(c, 1540, 700, ad, "zeros demais!", AMBER, -6, 36)
        ae = ep(t, C["04.e"], 0.5)
        pill(c, "a prova escreve assim: POTÊNCIAS DE 10", W / 2, 770, BLUE, size=34, a=ae, anchor="center", bounds=(0, 1920))
        return
    if sid == "05":
        steps = [("05.a", 1), ("05.b", 2), ("05.c", 3), ("05.e", 6)]
        n, pop, ct = 0, 1.0, C["05"]
        for cue, z in steps:
            if t >= C[cue] - 0.1:
                n, ct = z, C[cue]
        a0 = ep(t, C["05"], 0.5)
        text(c, "potência de 10 = o 10 multiplicado por ele mesmo", W / 2, 240, 34, "black", BLUE, a0)
        if n == 6:
            zeros = min(6, 3 + int((t - ct) / 0.25) + 1)
            pop = clamp(((t - ct) - 0.25 * (zeros - 4)) / 0.25)
        else:
            zeros = n
            pop = ep(t, ct, 0.35) if n > 0 else 1.0
        if n > 0:
            expr(c, f"10^{n} =", 560, 450, 120, a0, cores={0: INK})
            numeral(c, 1180, 450, 150, zeros, a0, pop=pop if zeros == n or n == 6 else 1.0)
            ad = ep(t, C["05.d"], 0.5)
            if ad > 0:
                rrect(c, 548, 360, 64, 64, 14, PURPLE, 0.15 * ad)
                arrow(c, 680, 640, 600, 440, PURPLE, ad, 4, 14, progress=ad)
            text(c, f"{zeros} zero{'s' if zeros != 1 else ''}", 1180, 600, 40, "black", PURPLE, a0)
            regra(c, "o expoente = o número de zeros", 560, 720, ad, 34)
        nomes = {1: "dez", 2: "cem", 3: "mil", 6: "um milhão"}
        if n in nomes:
            chip(c, nomes[n], 1180, 680, BLUE, a0 * ep(t, ct + 0.3, 0.4), 34)
        return
    # 06 atalho: mil, milhão, bilhão
    a0 = ep(t, C["06"], 0.5)
    text_mid(c, "o expoente do 10 é um CONTADOR DE ZEROS", W / 2, 240, 40, "black", BLUE, a0)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 300, 1400, 470, GREEN, aa, 0.06)
        text(c, "ATALHO", W / 2, 350, 22, "black", GREEN, aa, tracking=2)
    linhas = [("06.b", "mil", "1 000", "10^3"), ("06.c", "milhão", "1 000 000", "10^6"), ("06.d", "bilhão", "1 000 000 000", "10^9")]
    for k, (cue, nome, num, pot) in enumerate(linhas):
        a, d = rise(t, C[cue])
        y = 440 + k * 110 + d
        text(c, nome, 360, y + 14, 48, "black", INK, a, align="left")
        text(c, num, 1020, y + 14, 48, "black", INK2, a, align="center")
        expr(c, pot, 1500, y, 64, a, cores={0: GREEN})


# ======================================================================
# blocos 07–08 — expoente negativo: a escada que divide por 10
# ======================================================================

DEG10 = [("10^3", "1000"), ("10^2", "100"), ("10^1", "10"), ("10^0", "1"), ("10^{-1}", "0,1"), ("10^{-2}", "0,01"), ("10^{-3}", "0,001")]


def b_decimais(c, t, C, B):
    head_seq(c, t, C, [("07", "E O EXPOENTE NEGATIVO?", "A ESCADA DO EPISÓDIO 1", PURPLE), ("08", "CASA DECIMAL", "O 1 NA ÚLTIMA CASA", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        ativos = {0: ep(t, C["07.b"], 0.4), 1: ep(t, C["07.b"] + 0.5, 0.4), 2: ep(t, C["07.b"] + 1.0, 0.4),
                  3: ep(t, C["07.b"] + 1.5, 0.4), 4: ep(t, C["07.c"], 0.4), 5: ep(t, C["07.d"], 0.4), 6: ep(t, C["07.e"], 0.4)}
        setas = {0: ep(t, C["07.b"] + 0.4, 0.4), 1: ep(t, C["07.b"] + 0.9, 0.4), 2: ep(t, C["07.b"] + 1.4, 0.4),
                 3: ep(t, C["07.c"] - 0.2, 0.4), 4: ep(t, C["07.d"] - 0.2, 0.4), 5: ep(t, C["07.e"] - 0.2, 0.4)}
        K.escada(c, 200, 330, DEG10, 222, 62, 1.0, ativos, PURPLE, 64, 208, 130, setas, "÷ 10")
        pill(c, "cada degrau para baixo: ÷ 10", 1450, 250, PURPLE, size=30, a=ep(t, C["07.a"], 0.5), anchor="center", bounds=(0, 1920))
        return
    a0 = ep(t, C["08"], 0.5)
    # a vírgula correndo: 10^-1 → 10^-2 → 10^-3
    u = ep(t, C["08"], 1.6)
    casas = 1 + min(2, int(u * 3))
    mov = clamp(u * 3 - (casas - 1)) if casas > 1 else 1.0
    if u >= 1:
        casas, mov = 3, 1.0
    expr(c, f"10^{{-{casas}}} =", 560, 420, 110, a0, cores={0: INK})
    decimal(c, 1080, 420, 150, casas, a0, mov, BLUE, marcar=(t - C["08.a"]) if t > C["08.a"] else 0.0)
    text(c, "casa decimal = cada algarismo depois da vírgula", W / 2, 260, 32, "black", BLUE, a0)
    aa = ep(t, C["08.a"], 0.5)
    text(c, "3 casas depois da vírgula", 1180, 600, 32, "black", BLUE, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        boxed(c, 240, 640, 640, 110, AMBER, ab, 0.10)
        text_mid(c, "NÃO são 3 zeros: 2 zeros + o 1", 560, 695, 32, "black", INK, ab)
    acc = ep(t, C["08.c"], 0.5)
    K.atalho(c, 1000, 640, 680, 140, "ATALHO", ["o 1 ocupa a ÚLTIMA casa"], acc, 34)


# ======================================================================
# blocos 09–11 — multiplicar
# ======================================================================

def b_multiplicar(c, t, C, B):
    head_seq(c, t, C, [("09", "MULTIPLICAR", "JUNTA OS ZEROS", PURPLE), ("10", "A CONTA DO COMEÇO", "EM 3 SEGUNDOS", GREEN),
                       ("11", "COM NÚMERO NA FRENTE", "NÚMEROS COM NÚMEROS", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10", "11"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0:
            x = 470
            for ch, col in [("1", INK), ("0", BLUE), ("0", BLUE), ("0", BLUE), ("0", BLUE)]:
                text(c, ch, x, 340, 80, "black", col, aa, align="left"); x += 50
            text(c, "×", 760, 340, 80, "black", INK, aa, align="left")
            x = 860
            for ch, col in [("1", INK), ("0", PURPLE), ("0", PURPLE)]:
                text(c, ch, x, 340, 80, "black", col, aa, align="left"); x += 50
            text(c, "=", 1050, 340, 80, "black", INK, aa, align="left")
            u = ep(t, C["09.a"] + 1.2, 0.6)
            x = 1130
            for k, (ch, col) in enumerate([("1", INK)] + [("0", BLUE)] * 4 + [("0", PURPLE)] * 2):
                text(c, ch, x, 340, 80, "black", col, aa * (u if k > 0 else 1), align="left"); x += 50
            text(c, "4 zeros + 2 zeros = 6 zeros", W / 2, 440, 34, "black", INK2, u)
        ab = ep(t, C["09.b"], 0.5)
        expr(c, "10^4 · 10^2 = 10^6", W / 2, 560, 90, ab, cores={0: BLUE, 2: PURPLE, 4: GREEN})
        regra(c, "multiplicou (mesma base): SOMA os expoentes", W / 2, 720, ep(t, C["09.c"], 0.5), 36)
        return
    if sid == "10":
        a0 = ep(t, C["10"], 0.5)
        expr(c, "1 000 000 × 0,001", W / 2, 250, 70, a0)
        aa, ab = ep(t, C["10.a"], 0.5), ep(t, C["10.b"], 0.5)
        expr(c, "10^6", 760, 400, 90, aa, cores={0: BLUE})
        expr(c, "×", W / 2, 400, 70, ab)
        expr(c, "10^{-3}", 1160, 400, 90, ab, cores={0: PURPLE})
        if aa > 0:
            arrow(c, 760, 290, 760, 340, LIGHT, aa, 4, 12, progress=aa)
        if ab > 0:
            arrow(c, 1160, 290, 1160, 340, LIGHT, ab, 4, 12, progress=ab)
        acc = ep(t, C["10.c"], 0.5)
        expr(c, "6 + (-3) = 6 - 3 = 3", W / 2, 540, 64, acc, cores={8: GREEN})
        ad = ep(t, C["10.d"], 0.5)
        expr(c, "10^3 = 1 000", W / 2, 680, 90, ad, cores={0: GREEN, 2: GREEN, 3: GREEN})
        chip(c, "3 segundos!", 1500, 680, GREEN, ad, 34)
        return
    a0 = ep(t, C["11.a"], 0.5)
    ab, acc = ep(t, C["11.b"], 0.5), ep(t, C["11.c"], 0.5)
    cores = {}
    expr(c, "(3·10^5) · (2·10^{-8})", W / 2, 270, 84, a0)
    if ab > 0:
        boxed(c, 420, 360, 480, 120, BLUE, ab, 0.08)
        text(c, "números com números", 660, 395, 24, "black", BLUE, ab)
        expr(c, "3 · 2 = 6", 660, 440, 54, ab, cores={4: BLUE})
    if acc > 0:
        boxed(c, 1020, 360, 480, 120, PURPLE, acc, 0.08)
        text(c, "expoentes com expoentes", 1260, 395, 24, "black", PURPLE, acc)
        expr(c, "5 + (-8) = -3", 1260, 440, 54, acc, cores={4: PURPLE})
    ad = ep(t, C["11.d"], 0.5)
    expr(c, "= 6·10^{-3}", W / 2, 580, 90, ad, cores={1: GREEN})
    ae = ep(t, C["11.e"], 0.5)
    K.atalho(c, 460, 670, 1000, 130, "ATALHO", ["números com números, potências com potências"], ae, 34)


# ======================================================================
# bloco 12 — dividir
# ======================================================================

def b_dividir(c, t, C, B):
    frame(c, t, B["start"], "DIVIDIR", "DIVIDE OS NÚMEROS, SUBTRAI OS EXPOENTES", PURPLE)
    aa = ep(t, C["12.a"], 0.5)
    expr(c, "{9·10^7}/{3·10^4}", 520, 420, 100, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        boxed(c, 900, 230, 700, 140, BLUE, ab, 0.08)
        text(c, "números: DIVIDE", 1250, 275, 26, "black", BLUE, ab)
        expr(c, "9 ÷ 3 = 3", 1250, 325, 56, ab, cores={4: BLUE})
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        boxed(c, 900, 400, 700, 140, PURPLE, acc, 0.08)
        text(c, "expoentes: SUBTRAI", 1250, 445, 26, "black", PURPLE, acc)
        expr(c, "7 - 4 = 3", 1250, 495, 56, acc, cores={4: PURPLE})
    ad = ep(t, C["12.d"], 0.5)
    expr(c, "= 3·10^3 = 3 000", 1060, 680, 80, ad, cores={1: GREEN, 3: GREEN, 4: GREEN})


# ======================================================================
# bloco 13 — elevar
# ======================================================================

def b_elevar(c, t, C, B):
    frame(c, t, B["start"], "A CONTA INTEIRA ELEVADA", "O DE FORA PEGA TODO MUNDO", PURPLE)
    aa = ep(t, C["13.a"], 0.5)
    expr(c, "(2·10^{-2})^3", W / 2, 360, 120, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        # o 3 de fora "entra" nos dois fatores
        for x2 in (800, 1010):
            p = skia.Path(); p.moveTo(1150, 270); p.quadTo((1150 + x2) / 2, 190, x2, 280)
            c.drawPath(p, paint(AMBER, ab, stroke=5, cap_round=True))
            c.drawCircle(x2, 284, 7, paint(AMBER, ab))
        text(c, "o 3 entra nos DOIS fatores", 1290, 235, 28, "black", AMBER, ab, align="left")
    acc = ep(t, C["13.c"], 0.5)
    expr(c, "2^3", 640, 550, 90, acc, cores={0: BLUE})
    text(c, "o número da frente", 640, 650, 28, "black", BLUE, acc)
    ad = ep(t, C["13.d"], 0.5)
    expr(c, "10^{-2·3} = 10^{-6}", 1240, 550, 90, ad, cores={0: PURPLE, 2: PURPLE})
    text(c, "potência de potência: multiplica", 1240, 650, 28, "black", PURPLE, ad)
    ae = ep(t, C["13.e"], 0.5)
    K.atalho(c, 460, 700, 1000, 120, "ATALHO", ["o expoente de fora entra em TODO MUNDO de dentro"], ae, 32)


# ======================================================================
# nós fazemos
# ======================================================================

EXS = [("14.a", "10^4 · 10^{-6}", "4 + (-6) = -2", "10^{-2}"), ("14.b", "(4·10^8) ÷ (2·10^3)", "4 ÷ 2 = 2 e 8 - 3 = 5", "2·10^5")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("15", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    for k, (cue, q, passo, r) in enumerate(EXS):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 360, 210, 720, 230, 24, "#F7F7F5", a)
        text(c, f"{k + 1}ª CONTA", x, 255, 22, "black", GRAY, a, tracking=1)
        expr(c, q + " = ?", x, 350, 56, a)
        if t >= C["15"]:
            ra = ep(t, C["15." + "ab"[k]], 0.5)
            expr(c, passo, x, 560, 40, ra, cores=mono(passo, INK2))
            expr(c, r, x, 690, 90, ra, cores={0: GREEN})
    pause_timer(c, t, C["14.end"] - 1.9, W / 2, 620)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["O expoente do 10 conta os zeros.", "Multiplicou: soma os expoentes. Dividiu: subtrai.",
          "O expoente de fora pega todos os fatores de dentro."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "26"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("Multiplicar quando a pergunta é “por habitante”", "multiplicar parece o natural",
          "por habitante = repartir: total ÷ número de pessoas"),
         ("Elevar só o 10 e esquecer o número da frente", "o 10 é quem tem expoente",
          "o expoente de fora pega TODOS: (2·10⁻²)³ = 2³ · 10⁻⁶"),
         ("2³ = 6", "2 · 3 dá 6", "a folha dobrada: 2 · 2 · 2 = 8")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


# ======================================================================
# Questão 2 do material
# ======================================================================

Q2_LINHAS = ["Uma cidade consome 7,2 · 10⁹ kWh de", "energia elétrica por ano e tem", "1,2 · 10⁶ habitantes. O consumo médio",
             "anual por habitante, em kWh, é de"]
Q2_ALTS = [("A", "= 6 · 10^2", "erro no expoente", RED), ("B", "= 6 · 10^3", "", GREEN), ("C", "= 6 · 10^4", "erro no expoente", RED),
           ("D", "= 8,4 · 10^3", "somou 7,2 + 1,2", RED), ("E", "= 8,64 · 10^{15}", "multiplicou", RED)]


def enunciado(c, linhas, x, y, a, size=32, lh=48, destaque=None):
    for k, s in enumerate(linhas):
        col = BLUE if destaque and k in destaque else INK
        ftext(c, s, x, y + k * lh, size, "black", col, a, align="left")


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · POTÊNCIAS DE 10 EM CONTEXTO", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["20.a"], 0.4)
    enunciado(c, Q2_LINHAS, 190, 250, a0, destaque={3} if t >= C["20.b"] else None)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    ak = ep(t, C["20.k"], 0.4) * (1 - ep(t, C["21"], 0.3))
    chip(c, "kWh = quilowatt-hora: a unidade da conta de luz", 470, 480, BLUE, ak, 24)
    cues_in = {L: C[f"20.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"22.x{L.lower()}"] for L in "ACDE"}
    if t >= C["20.qa"] - 0.3:
        K.alternativas(c, t, C, Q2_ALTS, 1000, 210, 700, 40, C["21.ok"], "B", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["20.end"] - 1.9, 470, 620)
    if t >= C["21"]:
        ra = ep(t, C["21"], 0.4)
        rrect(c, 170, 430, 780, 370, 18, "#FFFFFF", ra, shadow=True)
        chip(c, "por habitante = DIVIDIR", 560, 475, AMBER, ep(t, C["21.a"], 0.4), 28)
        expr(c, "{7,2·10^9}/{1,2·10^6}", 330, 610, 50, ep(t, C["21.a"], 0.4))
        expr(c, "7,2 ÷ 1,2 = 6", 720, 570, 38, ep(t, C["21.b"], 0.4), cores={4: BLUE})
        expr(c, "9 - 6 = 3", 720, 650, 38, ep(t, C["21.c"], 0.4), cores={4: PURPLE})
        expr(c, "= 6·10^3 = 6 000 kWh", 560, 750, 42, ep(t, C["21.d"], 0.4), cores={1: GREEN})
        apr = ep(t, C["22.pr"], 0.4)
        if apr > 0:
            rrect(c, 170, 430, 780, 370, 18, "#FFFFFF", apr, shadow=True)
            check_icon(c, 230, 520, 30, apr, GREEN)
            text(c, "PROVA REAL", 280, 530, 28, "black", GREEN, apr, align="left")
            expr(c, "6·10^3 × 1,2·10^6 = 7,2·10^9", 560, 640, 42, apr, cores={4: GREEN})
            text(c, "voltou ao consumo total da cidade", 560, 730, 26, "bold", INK2, apr)


# ======================================================================
# Questão 9 do material
# ======================================================================

Q9_LINHAS = ["Um cubo tem aresta medindo", "2 · 10⁻² metro. O volume desse", "cubo, em metros cúbicos, é"]
Q9_ALTS = [("A", "= 6 · 10^{-6}", "fez 2 · 3 = 6", RED), ("B", "= 8 · 10^{-6}", "", GREEN), ("C", "= 8 · 10^{-5}", "somou −2 + (−3)", RED),
           ("D", "= 2 · 10^{-6}", "elevou só o 10", RED), ("E", "= 6 · 10^{-2}", "3 vezes a aresta", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · POTÊNCIA DE UM PRODUTO", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    enunciado(c, Q9_LINHAS, 190, 250, a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ACDE"}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, Q9_ALTS, 1000, 210, 700, 40, C["24.ok"], "B", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["23.end"] - 1.9, 760, 520)
    sid = which(t, C, ["23", "24", "25"])
    if sid == "23":
        ak = ep(t, C["23.k"], 0.4)
        cubo(c, 400, 560, 150, ak, BLUE, "aresta", AMBER)
        av = ep(t, C["23.v"], 0.4)
        if av > 0:
            text(c, "VOLUME = o espaço lá dentro", 560, 450, 26, "black", BLUE, av, align="left")
            expr(c, "V = aresta^3", 560, 520, 44, av, cores={0: BLUE, 1: BLUE, 2: BLUE}, align="left")
            text(c, "aresta × aresta × aresta", 560, 590, 24, "bold", INK2, av, align="left")
        return
    ra = ep(t, C["24"], 0.4)
    rrect(c, 170, 400, 780, 400, 18, "#FFFFFF", ra, shadow=True)
    expr(c, "V = (2·10^{-2})^3", 560, 450, 44, ep(t, C["24.a"], 0.4))
    # o cubo "inflando": 2 → 4 → 8
    ws = [K.WT(C, "24", "dois", 2), K.WT(C, "24", "quatro"), K.WT(C, "24", "oito")]
    vals = [2, 4, 8]
    k = sum(1 for w in ws if t >= w - 0.1)
    if t >= C["24.c"] - 0.1:
        ac = ep(t, C["24.c"], 0.4)
        cubo(c, 330, 610, 70 + 24 * max(0, k - 1), ac, GREEN, cheio=0.3 * k)
        expr(c, f"2^3 = {vals[k - 1] if k else 2}", 660, 580, 46, ac, cores={2: GREEN})
        text(c, "2 · 2 · 2", 660, 640, 26, "bold", INK2, ac)
    ad = ep(t, C["24.d"], 0.4)
    expr(c, "(10^{-2})^3 = 10^{-6}", 640, 700, 40, ad, cores={2: PURPLE})
    ae = ep(t, C["24.e"], 0.4)
    expr(c, "V = 8·10^{-6} m^3", 560, 770, 40, ae, cores={2: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A RAIZ", PURPLE)
    aa = ep(t, C["27.a"], 0.5)
    text_mid(c, "9", 560, 420, 160, "black", INK, aa)
    text_mid(c, "81", 1360, 420, 160, "black", INK, aa)
    if aa > 0:
        p = skia.Path(); p.moveTo(660, 350); p.quadTo(W / 2, 220, 1240, 350)
        c.drawPath(p, paint(BLUE, aa, stroke=6, cap_round=True))
        expr(c, "ao quadrado", W / 2, 240, 34, aa, cores={0: BLUE, 1: BLUE})
        text(c, "IDA", W / 2, 320, 30, "black", BLUE, aa)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        p = skia.Path(); p.moveTo(1240, 500); p.quadTo(W / 2, 630, 660, 500)
        c.drawPath(p, paint(PURPLE, ab, stroke=6, cap_round=True))
        text(c, "VOLTA", W / 2, 560, 30, "black", PURPLE, ab)
        text_mid(c, "?", W / 2, 640, 70, "black", PURPLE, ep(t, C["27.c"], 0.5))
    pill(c, "ep. 4 · a raiz: a operação que desfaz a potência", W / 2, 780, PURPLE, size=32, a=ep(t, C["27.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"], "Você fez a conta do milhão de cabeça?",
        canal="no Estudativo", anki=C["28.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, zeros=b_zeros, decimais=b_decimais, multiplicar=b_multiplicar,
              dividir=b_dividir, elevar=b_elevar, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q9=b_q9,
              ponte=b_ponte, cta=b_cta)
