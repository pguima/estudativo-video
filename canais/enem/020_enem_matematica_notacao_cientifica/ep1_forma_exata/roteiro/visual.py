"""Visual — Notação Científica e Ordem de Grandeza, Episódio 1: a forma exata, converter e algarismos significativos
(iniciantes, tema claro). Peças comuns em ../../comum.py (reexporta o comum.py da série 019: expr com potências, fichas...).
Peças deste episódio: digitos() = fila de algarismos com a vírgula andando casa por casa, placa() = placa de carro,
cadeira() = cadeira vazia (zero à esquerda).
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
expr = K.expr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_notacao_ep1_forma_exata.mp4"
CARD_R = K.CARD_R
CINZA_CAD = "#B9B6AE"


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# peças do episódio
# ======================================================================

def digitos(c, s, cx, cy, size, a=1.0, virg=None, cores=None, alfas=None, cor=None, vcol=None):
    """fila de algarismos em células iguais; virg = nº de algarismos antes da vírgula (pode ser fracionário: a vírgula
    desliza). Devolve (x0, cw) para posicionar setas e marcas."""
    cw = size * 0.70
    x0 = cx - len(s) * cw / 2
    if a <= 0:
        return x0, cw
    cores, alfas = cores or {}, alfas or {}
    for i, ch in enumerate(s):
        text_mid(c, ch, x0 + (i + 0.5) * cw, cy, size, "black", cores.get(i, cor or INK), a * alfas.get(i, 1.0))
    if virg is not None:
        xv = x0 + virg * cw
        yv = cy + size * 0.40
        c.drawCircle(xv, yv, size * 0.075, paint(vcol or AMBER, a))
        p = skia.Path(); p.moveTo(xv + size * 0.06, yv); p.quadTo(xv + size * 0.05, yv + size * 0.16, xv - size * 0.06, yv + size * 0.24)
        c.drawPath(p, paint(vcol or AMBER, a, stroke=size * 0.055, cap_round=True))
    return x0, cw


def pulos(c, x0, cw, cy, size, p0, k, d, a=1.0, col=None):
    """arcos dos pulos já dados pela vírgula (p0 = posição inicial, k = pulos completos, d = −1 esquerda / +1 direita)"""
    col = col or AMBER
    for j in range(int(k)):
        xa, xb = x0 + (p0 + d * j) * cw, x0 + (p0 + d * (j + 1)) * cw
        y = cy + size * 0.72
        p = skia.Path(); p.moveTo(xa, y); p.quadTo((xa + xb) / 2, y + size * 0.36, xb, y)
        c.drawPath(p, paint(col, a * 0.85, stroke=4, cap_round=True))


def andar(t, t0, t1, n):
    """quantos pulos a vírgula já deu (contínuo) entre t0 e t1"""
    dur = max(0.18, min(0.55, (t1 - t0 - 0.3) / max(1, n)))
    return clamp((t - t0) / dur, 0, n)


def cadeira(c, cx, cy, s, a, col=None):
    """cadeira vazia, vista de lado (s = altura)"""
    if a <= 0:
        return
    col = col or CINZA_CAD
    pe = paint(col, a, stroke=s * 0.07, cap_round=True)
    rrect(c, cx - s * 0.30, cy - s * 0.55, s * 0.60, s * 0.36, s * 0.08, col, a * 0.55)   # encosto (almofada)
    rrect(c, cx - s * 0.34, cy - s * 0.02, s * 0.68, s * 0.14, s * 0.05, col, a)          # assento
    c.drawLine(cx - s * 0.26, cy - s * 0.19, cx - s * 0.26, cy, pe)                      # hastes do encosto
    c.drawLine(cx + s * 0.26, cy - s * 0.19, cx + s * 0.26, cy, pe)
    c.drawLine(cx - s * 0.28, cy + s * 0.12, cx - s * 0.32, cy + s * 0.5, pe)             # pernas
    c.drawLine(cx + s * 0.28, cy + s * 0.12, cx + s * 0.32, cy + s * 0.5, pe)


def placa(c, cx, cy, w, a, s="BRA2E19"):
    """placa de carro genérica (faixa azul em cima, caracteres em formato fixo)"""
    if a <= 0:
        return
    h = w * 0.33
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, w, h * 0.24, 18, BLUE, a)
    c.drawRect(skia.Rect.MakeXYWH(x, y + h * 0.12, w, h * 0.12), paint(BLUE, a))
    text_mid(c, "BRASIL", cx, y + h * 0.13, h * 0.13, "black", "#FFFFFF", a, tracking=3)
    text_mid(c, s, cx, y + h * 0.62, h * 0.48, "black", INK, a, tracking=6)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(INK, a, stroke=5))


# ======================================================================
# abertura
# ======================================================================

AREAS = [("01.b", "MATEMÁTICA", "3,844 · 10^8", "m: Terra–Lua", BLUE), ("01.c", "CIÊNCIAS DA NATUREZA", "6 · 10^{23}", "Física · Química · Biologia", GREEN),
         ("01.d", "HUMANAS", "2 · 10^8", "habitantes", PURPLE)]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "NOTAÇÃO CIENTÍFICA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "aparece em quase toda a prova", W / 2, 250, 46, "black", INK, aa)
    for k, (cue, nome, f_, sub, col) in enumerate(AREAS):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 420 + k * 540
        card(c, x - 240, 320, 480, 300, a)
        rrect(c, x - 240, 320, 480, 12, 6, col, a)
        text(c, nome, x, 390, 30, "black", col, a)
        expr(c, f_, x, 490, 56, a, cores={0: INK})
        text(c, sub, x, 580, 26, "bold", INK2, a)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        chip(c, "número GIGANTE", 700, 730, AMBER, ae, 34)
        chip(c, "número MINÚSCULO", 1220, 730, AMBER, ep(t, C["01.e"] + 0.6, 0.4), 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "escrever QUALQUER número", "em notação científica"), ("02.b", "perceber na hora", "a alternativa escrita do jeito errado")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 190 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")
    ab = ep(t, C["02.b"] + 0.6, 0.5)
    if ab > 0:
        expr(c, "25 · 10^3", 1100, 680, 60, ab, cores=mono("25 · 10^3", RED))
        strike(c, 980, 680, 1220, 680, ab, RED, ab)
        expr(c, "→ 2,5 · 10^4", 1450, 680, 56, ep(t, C["02.b"] + 1.2, 0.5), cores={0: INK2, 1: GREEN, 2: GREEN, 3: GREEN})


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "DA SÉRIE DE POTENCIAÇÃO", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        expr(c, "10^3 = 1 000", 560, 360, 80, aa, cores={2: PURPLE})
        text(c, "1 seguido de 3 zeros", 560, 470, 32, "black", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        expr(c, "10^{-3} = 0,001", 1360, 360, 80, ab, cores={2: BLUE})
        text(c, "3 casas depois da vírgula, o 1 na última", 1360, 470, 30, "black", INK2, ab)
    line(c, 960, 260, 960, 560, "#E6E6E2", ab, 3)
    chip(c, "pequeno, mas POSITIVO", 1360, 640, GREEN, ep(t, C["03.c"], 0.5), 34)


# ======================================================================
# números enormes e minúsculos
# ======================================================================

TERRA = "5 970 000 000 000 000 000 000 000"


def b_zeros(c, t, C, B):
    frame(c, t, B["start"], "CONTE OS ZEROS", "SE CONSEGUIR", AMBER)
    a0 = ep(t, C["04"], 0.5)
    text(c, "massa da Terra, em kg", W / 2, 245, 30, "black", GRAY, a0)
    aa = ep(t, C["04.a"], 0.5)
    ab = ep(t, C["04.b"], 0.5)
    size = 62
    w = text_w(TERRA, "black", size)
    x = W / 2 - w / 2
    for ch in TERRA:
        cw = text_w(ch, "black", size)
        col = INK if ch != "0" else mix(INK, AMBER, ab)
        if ch != " ":
            text(c, ch, x + cw / 2, 360, size, "black", col, aa)
        x += cw
    selo(c, 1500, 450, ab, "quantos zeros?", AMBER, -5, 34)
    ac = ep(t, C["04.c"], 0.5)
    text(c, "tamanho de um vírus, em metros", W / 2, 545, 30, "black", GRAY, ac)
    text(c, "0,0000001 m", W / 2, 640, 70, "black", mix(INK, AMBER, ep(t, C["04.c"] + 1.6, 0.5)), ac)
    regra(c, "contar zeros = o jeito mais fácil de errar", W / 2, 765, ep(t, C["04.d"], 0.5), 34, RED)


# ======================================================================
# bloco A — a forma exata
# ======================================================================

def b_forma(c, t, C, B):
    head_seq(c, t, C, [("05", "A FORMA EXATA", "NOTAÇÃO CIENTÍFICA", BLUE), ("06", "A REGRA DO COEFICIENTE", "ENTRE 1 E 10", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        pill(c, "NOTAÇÃO CIENTÍFICA = jeito padronizado de escrever números muito grandes ou pequenos", W / 2, 230, BLUE,
             size=26, a=ep(t, C["05"], 0.5), anchor="center", bounds=(0, 1920))
        aa = ep(t, C["05.a"], 0.5)
        cx, cy = W / 2, 470
        expr(c, "a · 10^n", cx, cy, 190, aa, cores={0: INK})
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            rrect(c, cx - 345, cy - 110, 150, 200, 22, BLUE, 0.12 * ab)
            arrow(c, cx - 270, cy + 220, cx - 270, cy + 100, BLUE, ab, 5, 16, progress=ab)
            text(c, "COEFICIENTE", cx - 270, cy + 270, 34, "black", BLUE, ab)
            text(c, "o número da frente", cx - 270, cy + 310, 26, "bold", INK2, ab)
        ac = ep(t, C["05.c"], 0.5)
        if ac > 0:
            rrect(c, cx + 210, cy - 175, 100, 130, 20, PURPLE, 0.14 * ac)
            arrow(c, cx + 520, cy - 110, cx + 325, cy - 110, PURPLE, ac, 5, 16, progress=ac)
            text(c, "EXPOENTE", cx + 640, cy - 125, 34, "black", PURPLE, ac)
            text(c, "número INTEIRO, sem vírgula", cx + 640, cy - 85, 24, "bold", INK2, ac)
        return
    a0 = ep(t, C["06"], 0.5)
    expr(c, "1 ≤ |a| < 10", W / 2, 260, 90, a0, cores={0: GREEN, 4: RED})
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        x0, x1, y = 300, 1620, 430
        val = lambda v: lerp(x0, x1, v / 12)
        line(c, x0, y, x1, y, INK2, aa, 4)
        for v in range(0, 13):
            line(c, val(v), y - 10, val(v), y + 10, INK2, aa, 3)
            text(c, str(v), val(v), y + 50, 26, "bold", INK2, aa)
        pr = ep(t, C["06.a"] + 0.3, 0.9)
        rrect(c, val(1), y - 9, (val(10) - val(1)) * pr, 18, 9, GREEN, aa * 0.85)
        c.drawCircle(val(1), y, 15, paint(GREEN, aa))
        c.drawCircle(val(10), y, 15, paint("#FFFFFF", aa * pr)); c.drawCircle(val(10), y, 15, paint(RED, aa * pr, stroke=5))
        text(c, "pode ser 1", val(1), y - 40, 26, "black", GREEN, aa)
        text(c, "não chega a 10", val(10), y - 40, 26, "black", RED, aa * pr)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        boxed(c, 300, 560, 560, 90, BLUE, ab, 0.08)
        expr(c, "|a|", 390, 605, 46, ab, cores={0: BLUE})
        text_mid(c, "= o número sem o sinal", 640, 605, 30, "black", INK, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        boxed(c, 960, 550, 660, 230, PURPLE, acc, 0.06)
        text(c, "na prática", 1290, 595, 24, "black", PURPLE, acc, tracking=2)
        for k in range(4):
            bx = 1110 + k * 80 + (34 if k > 0 else 0)
            rrect(c, bx, 625, 64, 84, 12, mix("#FFFFFF", GREEN if k == 0 else GRAY, 0.25), acc)
        text_mid(c, ",", 1185, 690, 60, "black", AMBER, acc)
        text_mid(c, "1–9", 1142, 667, 26, "black", GREEN, acc)
        text(c, "1 algarismo ≠ 0 antes da vírgula", 1290, 760, 26, "black", INK, acc)


def b_placa(c, t, C, B):
    frame(c, t, B["start"], "A ANALOGIA", "A PLACA DE CARRO", BLUE)
    a0 = ep(t, C["07"], 0.5)
    placa(c, 560, 420, 600, a0)
    aa = ep(t, C["07.a"], 0.5)
    text(c, "formato fixo: letras e números, sempre na mesma ordem", 560, 600, 26, "bold", INK2, aa)
    ab = ep(t, C["07.b"], 0.5)
    chip(c, "UM só jeito certo", 560, 680, BLUE, ab, 32)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        line(c, 960, 240, 960, 800, "#E6E6E2", acc, 3)
        expr(c, "3,844 · 10^8", 1380, 330, 70, acc, cores={0: GREEN})
        check_icon(c, 1660, 320, 30, acc, GREEN)
        expr(c, "38,44 · 10^7", 1380, 450, 56, acc, cores=mono("38,44 · 10^7", GRAY))
        strike(c, 1230, 450, 1530, 450, acc, RED, acc)
        expr(c, "0,3844 · 10^9", 1380, 550, 56, acc, cores=mono("0,3844 · 10^9", GRAY))
        strike(c, 1210, 550, 1550, 550, acc, RED, acc)
    ad = ep(t, C["07.d"], 0.5)
    regra(c, "1 algarismo antes da vírgula: nem menos, nem mais", 1380, 690, ad, 28)


# ======================================================================
# bloco B — a tabela e o renormalizar
# ======================================================================

LINHAS = [("08.b", "3,84 · 10^8", True, "coeficiente entre 1 e 10"), ("08.c", "25 · 10^3", False, "25 passou de 10"),
          ("08.d", "0,5 · 10^4", False, "0,5 ficou abaixo de 1"), ("08.e", "1 · 10^{-6}", True, "o 1 é permitido")]


def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("08", "POR QUE TANTA REGRA?", "UMA ÚNICA ESCRITA", PURPLE), ("09", "CONSERTANDO", "RENORMALIZAR", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        pill(c, "a prova cobra justamente a escrita certa", W / 2, 225, AMBER, size=28, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "ESCRITA", 480, 300, 24, "black", GRAY, aa, tracking=2)
        text(c, "É NOTAÇÃO CIENTÍFICA?", 980, 300, 24, "black", GRAY, aa, tracking=2)
        text(c, "POR QUÊ", 1430, 300, 24, "black", GRAY, aa, tracking=2)
        for k, (cue, s, ok, why) in enumerate(LINHAS):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 380 + k * 110
            rrect(c, 230, y - 45, 1460, 90, 16, mix("#FFFFFF", GREEN if ok else RED, 0.07), a)
            expr(c, s, 480, y, 50, a, cores=mono(s, INK))
            col = GREEN if ok else RED
            check_icon(c, 900, y, 26, a, col, "check" if ok else "x")
            text_mid(c, "SIM" if ok else "NÃO", 990, y, 34, "black", col, a)
            text_mid(c, why, 1430, y, 28, "bold", INK2, a)
        return
    aa = ep(t, C["09.a"], 0.5)
    pill(c, "RENORMALIZAR = arrumar para a forma exata, sem mudar o valor", W / 2, 225, BLUE, size=28, a=aa, anchor="center",
         bounds=(0, 1920))
    for k, (cb, cc, de, para_, fc, fe, coef_txt, exp_txt) in enumerate([
            ("09.b", "09.c", "25 · 10^3", "2,5 · 10^4", "÷ 10", "+ 1", "coeficiente 10× MENOR", "expoente SOBE 1"),
            ("09.d", "09.e", "0,5 · 10^4", "5 · 10^3", "× 10", "− 1", "coeficiente 10× MAIOR", "expoente DESCE 1")]):
        a = ep(t, C[cb], 0.5)
        if a <= 0:
            continue
        y = 400 + k * 230
        expr(c, de, 520, y, 64, a, cores=mono(de, RED))
        arrow(c, 760, y, 900, y, INK2, a, 5, 16, progress=a)
        a2 = ep(t, C[cc], 0.5)
        expr(c, para_, 1140, y, 64, a2, cores=mono(para_, GREEN))
        chip(c, fc + "  no coeficiente", 1500, y - 40, AMBER, a, 24)
        ftext(c, fe + "  no expoente", 1500, y + 30, 26, "black", PURPLE, a)
        text(c, coef_txt + " · " + exp_txt, 830, y + 90, 24, "bold", INK2, a2)


# ======================================================================
# bloco C — expoente negativo, número positivo
# ======================================================================

def b_negativo(c, t, C, B):
    frame(c, t, B["start"], "EXPOENTE NEGATIVO", "NÚMERO NEGATIVO?", AMBER)
    aa = ep(t, C["10.a"], 0.5)
    expr(c, "10^{-3} = 0,001", W / 2, 300, 100, aa, cores={2: GREEN})
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        x0, x1, y = 360, 1560, 480
        line(c, x0, y, x1, y, INK2, ab, 4)
        for v, s in ((x0, "−1"), ((x0 + x1) / 2, "0"), (x1, "1")):
            line(c, v, y - 12, v, y + 12, INK2, ab, 3)
            text(c, s, v, y + 50, 28, "bold", INK2, ab)
        xv = (x0 + x1) / 2 + 30
        c.drawCircle(xv, y, 14, paint(GREEN, ab))
        text(c, "0,001: à direita do zero → POSITIVO", xv + 30, y - 40, 28, "black", GREEN, ab, align="left")
    regra(c, "o sinal do expoente NÃO é o sinal do número", W / 2, 640, ep(t, C["10.c"], 0.5), 34)
    chip(c, "ele diz para que lado a vírgula anda", W / 2, 750, PURPLE, ep(t, C["10.d"], 0.5), 32)


# ======================================================================
# bloco D — a vírgula que anda
# ======================================================================

LUA = "384400000"
VIRUS = "000000042"


def b_virgula(c, t, C, B):
    head_seq(c, t, C, [("11", "A REGRA ÚNICA", "ANDE COM A VÍRGULA", PURPLE), ("12", "NÚMERO PEQUENO", "A VÍRGULA ANDA PARA A DIREITA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        pill(c, "ande com a vírgula até sobrar 1 algarismo antes dela", W / 2, 225, PURPLE, size=28, a=aa, anchor="center", bounds=(0, 1920))
        chip(c, "EXPOENTE = contador de casas que a vírgula andou", W / 2, 290, BLUE, ep(t, C["11.b"], 0.5), 26)
        ac = ep(t, C["11.c"], 0.5)
        text(c, "Terra → Lua, em metros", 760, 370, 28, "black", GRAY, ac)
        k = andar(t, C["11.e"], C["11.f"] + 0.4, 8) if t >= C["11.e"] else 0.0
        virg = 9 - k if t >= C["11.d"] else None
        x0, cw = digitos(c, LUA, 760, 470, 96, ac, virg=virg, cores={0: GREEN} if k >= 8 else None,
                         vcol=AMBER if t >= C["11.d"] else None)
        if t >= C["11.d"]:
            ad = ep(t, C["11.d"], 0.4)
            if t < C["11.e"]:
                selo(c, x0 + 9 * cw + 60, 380, ad, "escondida no fim", AMBER, -6, 26)
        pulos(c, x0, cw, 470, 96, 9, k, -1, ac)
        if t >= C["11.e"]:
            K.contador(c, 1460, 470, int(k), ep(t, C["11.e"], 0.4), "casas ←", PURPLE)
        ag = ep(t, C["11.g"], 0.5)
        if ag > 0:
            rrect(c, 420, 680, 1080, 110, 22, "#FFFFFF", ag, shadow=True)
            expr(c, "384 400 000 = 3,844 · 10^8", W / 2, 735, 54, ag, cores={4: GREEN, 6: GREEN})
        return
    a0 = ep(t, C["12"], 0.5)
    text(c, "0,000 000 42", 760, 330, 34, "black", GRAY, a0)
    k = andar(t, C["12.a"], C["12.b"] + 0.4, 7) if t >= C["12.a"] else 0.0
    cores = {i: CINZA_CAD for i in range(7)}
    cores.update({7: INK, 8: INK})
    if k >= 7:
        cores[7] = GREEN
    x0, cw = digitos(c, VIRUS, 760, 450, 96, a0, virg=1 + k, cores=cores)
    pulos(c, x0, cw, 450, 96, 1, k, 1, a0)
    if t >= C["12.a"]:
        K.contador(c, 1460, 450, int(k), ep(t, C["12.a"], 0.4), "casas →", BLUE)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 420, 610, 1080, 100, 22, "#FFFFFF", acc, shadow=True)
        expr(c, "0,000 000 42 = 4,2 · 10^{-7}", W / 2, 660, 50, acc, cores={5: GREEN, 7: GREEN})
    ad, ae = ep(t, C["12.d"], 0.5), ep(t, C["12.e"], 0.5)
    if ad > 0:
        ftext(c, "← vírgula para a esquerda · número GRANDE · expoente +", 560, 780, 26, "black", PURPLE, ad)
    if ae > 0:
        ftext(c, "vírgula para a direita → · número PEQUENO · expoente −", 1360, 780, 26, "black", BLUE, ae)


def b_atalho_conta(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "CONTE SEM CONTAR CASA POR CASA", GREEN)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        boxed(c, 210, 210, 1500, 270, GREEN, aa, 0.05)
        text(c, "NÚMERO GRANDE: conte os algarismos DEPOIS do primeiro", W / 2, 260, 30, "black", GREEN, aa)
        al = ep(t, C["13.a"] + 1.4, 0.5)
        x0, cw = digitos(c, LUA, 700, 370, 70, aa, cores={0: INK}, alfas={i: 1.0 for i in range(9)})
        for i in range(1, 9):
            badge_num(c, i, x0 + (i + 0.5) * cw, 440, al * ep(t, C["13.a"] + 1.4 + 0.15 * i, 0.25), 18, bg=GREEN)
        expr(c, "→ 10^8", 1350, 370, 66, al, cores={1: GREEN})
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        boxed(c, 210, 510, 1500, 290, GREEN, ab, 0.05)
        text(c, "NÚMERO PEQUENO: conte os zeros da FRENTE, inclusive o de antes da vírgula", W / 2, 560, 28, "black", GREEN, ab)
        acc = ep(t, C["13.c"], 0.5)
        x0, cw = digitos(c, VIRUS, 700, 670, 70, ab, virg=1, cores={i: (GREEN if acc > 0 else INK) for i in range(7)})
        for i in range(7):
            badge_num(c, i + 1, x0 + (i + 0.5) * cw, 745, acc * ep(t, C["13.c"] + 0.15 * i, 0.25), 18, bg=GREEN)
        expr(c, "→ 10^{-7}", 1350, 670, 66, acc, cores={1: GREEN})


# ======================================================================
# bloco E — a conferência de dois segundos
# ======================================================================

def b_conferencia(c, t, C, B):
    frame(c, t, B["start"], "A CONFERÊNCIA", "DE DOIS SEGUNDOS", GREEN)
    aa = ep(t, C["14.a"], 0.5)
    text(c, "olhe o número ORIGINAL", W / 2, 250, 36, "black", INK, aa)
    for k, (cue, s1, s2, ex, col) in enumerate([("14.b", "MAIOR que 1", "expoente POSITIVO", "384 400 000 → 10^8", PURPLE),
                                                 ("14.c", "MENOR que 1", "expoente NEGATIVO", "0,000 000 42 → 10^{-7}", BLUE)]):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 560 + k * 800
        card(c, x - 340, 310, 680, 330, a)
        text(c, s1, x, 380, 44, "black", INK, a)
        arrow(c, x, 410, x, 470, col, a, 5, 14, progress=a)
        text(c, s2, x, 520, 40, "black", col, a)
        expr(c, ex, x, 590, 36, a, cores=mono(ex, INK2))
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        boxed(c, 460, 690, 1000, 100, GREEN, ad, 0.10)
        text(c, "ATALHO", 600, 750, 22, "black", GREEN, ad, tracking=2)
        text(c, "pega o erro de sinal sem recontar nada", 1040, 750, 32, "black", INK, ad)


# ======================================================================
# nós fazemos
# ======================================================================

EXS = [("15.a", "72 000", "7,2 · 10^4", "4 casas para a esquerda"), ("15.b", "0,0035", "3,5 · 10^{-3}", "3 casas para a direita"),
       ("15.c", "45 · 10^2", "4,5 · 10^3", "45 passou de 10: expoente sobe 1")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS CONFERIR", "PAUSE E TENTE", GREEN)])
    card(c, *CARD_R)
    for k, (cue, q, r, why) in enumerate(EXS):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 420 + k * 540
        rrect(c, x - 230, 210, 460, 250, 24, "#F7F7F5", a)
        text(c, "CORRIJA" if k == 2 else f"{k + 1}º NÚMERO", x, 255, 22, "black", AMBER if k == 2 else GRAY, a, tracking=1)
        expr(c, q, x, 360, 64, a)
        if t >= C["16"]:
            ra = ep(t, C["16." + "abc"[k]], 0.5)
            expr(c, r, x, 580, 62, ra, cores=mono(r, GREEN))
            text(c, why, x, 680, 24, "bold", INK2, ra)
    pause_timer(c, t, C["15.end"] - 1.9, W / 2, 620)


# ======================================================================
# recap
# ======================================================================

FRASES = ["Um único algarismo, diferente de zero, antes da vírgula.", "Número grande: expoente positivo. Pequeno: negativo.",
          "Expoente negativo não deixa o número negativo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


# ======================================================================
# blocos F, G, H — algarismos significativos e arredondamento
# ======================================================================

REGRAS = [("18.b", "diferente de zero", "CONTA", GREEN), ("18.c", "zero ENTRE algarismos que contam", "CONTA", GREEN),
          ("18.d", "zero À ESQUERDA", "NÃO CONTA", RED), ("18.e", "zero À DIREITA, depois da vírgula", "CONTA", GREEN)]


def b_signif(c, t, C, B):
    head_seq(c, t, C, [("18", "ALGARISMOS SIGNIFICATIVOS", "AS 4 REGRAS", BLUE), ("19", "CADEIRAS VAZIAS", "ZEROS À ESQUERDA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19"])
    if sid == "18":
        aa = ep(t, C["18.a"], 0.5)
        pill(c, "SIGNIFICATIVOS = os algarismos que carregam informação da medida", W / 2, 225, BLUE, size=28, a=aa,
             anchor="center", bounds=(0, 1920))
        for k, (cue, s, v, col) in enumerate(REGRAS):
            a, d = rise(t, C[cue])
            y = 330 + k * 120 + d
            badge_num(c, k + 1, 300, y - 12, a, 32, bg=PURPLE)
            text(c, s, 360, y, 40, "black", INK, a, align="left")
            chip(c, v, 1480, y - 12, col, a, 32)
        return
    a0 = ep(t, C["19"], 0.5)
    for i in range(3):
        cadeira(c, 330 + i * 120, 330, 90, a0 * ep(t, C["19"] + 0.2 * i, 0.3))
    text(c, "só guardam lugar", 450, 420, 28, "black", GRAY, a0)
    aa = ep(t, C["19.a"], 0.5)
    ab, ac, ad = ep(t, C["19.b"], 0.5), ep(t, C["19.c"], 0.5), ep(t, C["19.d"], 0.5)
    cores = {0: mix(INK, CINZA_CAD, ab), 1: mix(INK, CINZA_CAD, ab), 2: mix(INK, CINZA_CAD, ab),
             3: mix(INK, GREEN, ac), 4: mix(INK, GREEN, ac), 5: mix(INK, GREEN, ad)}
    x0, cw = digitos(c, "000420", 1250, 360, 110, aa, virg=1, cores=cores, vcol=INK)
    for i in range(3):
        cadeira(c, x0 + (i + 0.5) * cw, 470, 56, ab)
    for i in range(3, 6):
        check_icon(c, x0 + (i + 0.5) * cw, 470, 22, ac if i < 5 else ad, GREEN)
    chip(c, "3 significativos", 1250, 560, GREEN, ad, 32)
    ae = ep(t, C["19.e"], 0.5)
    if ae > 0:
        line(c, 240, 620, 1680, 620, "#E6E6E2", ae, 3)
        x0, cw = digitos(c, "1002", 480, 715, 100, ae, cores={i: GREEN for i in range(4)})
        text_mid(c, "zeros no MEIO: contam", 1000, 715, 34, "black", INK, ae)
        chip(c, "4 significativos", 1480, 715, GREEN, ep(t, C["19.e"] + 1.0, 0.5), 32)


def b_vantagem(c, t, C, B):
    frame(c, t, B["start"], "A VANTAGEM ESCONDIDA", "SEM DISCUSSÃO", GREEN)
    aa = ep(t, C["20.a"], 0.5)
    if aa > 0:
        text_mid(c, "4 200", 560, 330, 110, "black", INK, aa)
        selo(c, 560, 470, ep(t, C["20.a"] + 1.4, 0.5), "2, 3 ou 4? não dá para saber", AMBER, -4, 28)
    ab = ep(t, C["20.b"], 0.5)
    if ab > 0:
        expr(c, "4,20 · 10^3", 1360, 330, 96, ab, cores={0: GREEN})
        chip(c, "exatamente 3", 1360, 470, GREEN, ab, 32)
    line(c, 960, 240, 960, 540, "#E6E6E2", ab, 3)
    regra(c, "no coeficiente, TODOS os algarismos contam", W / 2, 610, ep(t, C["20.c"], 0.5), 34)
    ad = ep(t, C["20.d"], 0.5)
    if ad > 0:
        boxed(c, 360, 690, 1200, 100, GREEN, ad, 0.10)
        text(c, "ATALHO", 500, 750, 22, "black", GREEN, ad, tracking=2)
        text(c, "na dúvida: notação científica e conte o coeficiente", 1010, 750, 32, "black", INK, ad)


def b_arredondar(c, t, C, B):
    frame(c, t, B["start"], "ARREDONDAR", "OLHE O ALGARISMO SEGUINTE", PURPLE)
    aa = ep(t, C["21.a"], 0.5)
    pill(c, "ARREDONDAR = cortar o que sobra e ajustar o último que fica", W / 2, 225, BLUE, size=28, a=aa, anchor="center",
         bounds=(0, 1920))
    ab = ep(t, C["21.b"], 0.5)
    if ab > 0:
        boxed(c, 360, 280, 560, 90, GREEN, ab, 0.08)
        text_mid(c, "seguinte < 5 → MANTÉM", 640, 325, 34, "black", INK, ab)
        boxed(c, 1000, 280, 560, 90, AMBER, ab, 0.08)
        text_mid(c, "seguinte ≥ 5 → SOMA 1", 1280, 325, 34, "black", INK, ab)
    for k, (cue, s, virg, alvo, res, nota) in enumerate([("21.c", "3844", 1, 2, "3,8", "o seguinte é 4: mantém"),
                                                          ("21.d", "597", 1, 2, "6,0", "o seguinte é 7: o 9 vira 10")]):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 480 + k * 170
        cores = {i: GREEN for i in range(alvo)}
        cores[alvo] = AMBER
        for i in range(alvo + 1, len(s)):
            cores[i] = CINZA_CAD
        x0, cw = digitos(c, s, 560, y, 90, a, virg=virg, cores=cores, vcol=INK)
        rrect(c, x0 + alvo * cw + 4, y - 58, cw - 8, 116, 12, AMBER, a * 0.15)
        arrow(c, 820, y, 960, y, INK2, a, 5, 16, progress=a)
        ar = ep(t, C[cue] + 2.2, 0.5)
        text_mid(c, res, 1120, y, 90, "black", GREEN, ar)
        text(c, nota, 1300, y + 12, 28, "bold", INK2, ar, align="left")
    text(c, "com 2 significativos", 560, 820, 24, "bold", GRAY, ep(t, C["21.c"], 0.5))


# ======================================================================
# erros
# ======================================================================

ERROS = [("aceitar 25 · 10³ como notação científica", "o número está certo", "a escrita não: 2,5 · 10⁴"),
         ("errar o sinal do expoente", "você contou as casas direitinho", "conferência: maior que 1 → expoente positivo"),
         ("achar que 10⁻³ é um número negativo", "o sinal de menos está ali", "10⁻³ = 0,001: positivo"),
         ("contar zeros à esquerda como significativos", "eles estão escritos ali", "são cadeiras vazias: não contam")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25"], ERROS)


# ======================================================================
# Questão 1 do material
# ======================================================================

ALTS = [("A", "= 5,97 · 10^{21}", "contou só os grupos de 000", RED), ("B", "= 59,7 · 10^{23}", "valor certo, fora da forma", AMBER),
        ("C", "= 5,97 · 10^{24}", "", GREEN), ("D", "= 5,97 · 10^{-24}", "inverteu o sinal", RED),
        ("E", "= 0,597 · 10^{25}", "valor certo, fora da forma", AMBER)]
ENUNCIADO = ("A massa da Terra é de aproximadamente 5 970 000 000 000 000 000 000 000 kg. "
             "Em notação científica, esse valor é")
TERRA_D = "5970000000000000000000000"


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · CONVERSÃO", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    para(c, ENUNCIADO, 190, 240, 34, "black", INK, a0, 640, 46)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["28.xa"], "B": C["28.xb"], "D": C["28.xd"], "E": C["28.xb"] + 0.6}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS, 890, 200, 800, 40, C["27.ok"], "C", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["26.end"] - 1.9, 470, 640)
    if t >= C["27"]:
        ra = ep(t, C["27"], 0.4)
        rrect(c, 170, 470, 680, 330, 18, "#FFFFFF", ra, shadow=True)
        k = andar(t, C["27.b"], C["27.c"] + 0.3, 24) if t >= C["27.b"] else 0.0
        x0, cw = digitos(c, TERRA_D, 510, 560, 30, ep(t, C["27.a"], 0.4), virg=25 - k,
                         cores={0: GREEN} if k >= 24 else None)
        pulos(c, x0, cw, 560, 30, 25, k, -1, ra)
        text(c, "vírgula escondida no fim → para depois do 5", 510, 520, 22, "black", AMBER, ep(t, C["27.a"], 0.4))
        if t >= C["27.b"]:
            text_mid(c, f"{int(k)} casas ←", 510, 660, 40, "black", PURPLE, ep(t, C["27.b"], 0.4))
        expr(c, "5,97 · 10^{24}", 510, 740, 52, ep(t, C["27.d"], 0.4), cores={0: GREEN, 2: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "CONTAS EM NOTAÇÃO CIENTÍFICA", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    expr(c, "(8·10^4) · (5·10^2) = ?", W / 2, 330, 80, aa)
    ab = ep(t, C["30.b"], 0.5)
    chip(c, "multiplicar e dividir: fácil", W / 2, 470, GREEN, ab, 34)
    acc = ep(t, C["30.c"], 0.5)
    selo(c, W / 2, 590, acc, "o passo que quase todo mundo ESQUECE", AMBER, -3, 36)
    pill(c, "ep. 2 · multiplicar, dividir, elevar e tirar raiz", W / 2, 760, PURPLE, size=32, a=ep(t, C["30.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Quantos zeros você contou na massa da Terra?",
        canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, zeros=b_zeros, forma=b_forma, placa=b_placa,
              tabela=b_tabela, negativo=b_negativo, virgula=b_virgula, atalho_conta=b_atalho_conta,
              conferencia=b_conferencia, exercicio=b_exercicio, recap=b_recap, signif=b_signif, vantagem=b_vantagem,
              arredondar=b_arredondar, erros=b_erros, questao=b_questao, ponte=b_ponte, cta=b_cta)
