"""Visual — Função logarítmica, Episódio 3: terremotos (amplitude, energia e magnitude de momento) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências e frações, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: lrow() (linha com "log" e subscritos, como na série de Logaritmos), sismografo() (o papel riscado
pela onda), placar() (os DOIS PLACARES: amplitude ×10 por grau, energia ×32 por grau), formula_mw() (a fórmula de M_w com
as operações numeradas: 1º multiplica, 2º subtrai), cadeia() (as mesmas operações desfeitas na ordem contrária).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum043", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_logaritmica_ep3_terremotos.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
TINTA = "#3A4252"     # tinta do sismógrafo


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


def _txt(s):
    """parênteses sem potência vão como texto (o expr não aceita "(x" partido no espaço)"""
    return any(ch in s for ch in "([") and "^" not in s


def mx(c, s, cx, cy, size, a, col=None, align="center"):
    """expressão matemática de uma cor só (potências, frações); com parênteses e sem potência, texto"""
    if _txt(s):
        w = ftext_w(s, "black", size)
        if a > 0:
            x = cx - w / 2 if align == "center" else cx
            ftext(c, s, x, cy + size * 0.36, size, "black", col or INK, a, align="left")
        return w
    n = len(s.split())
    return K.expr(c, s, cx, cy, size, a, cores={i: col or INK for i in range(n)}, align=align)


def _pw(p, size):
    if p[0] == "log":
        return ftext_w("log", "black", size)
    if p[0] == "sb":
        return ftext_w(p[1], "black", size) + ftext_w(p[2], "black", size * 0.58) + size * 0.03
    if p[0] == "m":
        return ftext_w(p[1], "black", size) if _txt(p[1]) else K.math_w(p[1], size)
    return ftext_w(p[1], "black", size)


def lrow(c, partes, cx, cy, size, a, align="center", gap=None):
    """linha: partes = [("log", "", cor), ("sb", "M", "w", cor) (letra com subscrito), ("m", expr, cor), ("t", texto, cor)].
    Devolve a largura."""
    gap = size * 0.22 if gap is None else gap
    ws = [_pw(p, size) for p in partes]
    total = sum(ws) + gap * (len(partes) - 1)
    if a <= 0:
        return total
    x = cx - total / 2 if align == "center" else (cx - total if align == "right" else cx)
    for p, w_ in zip(partes, ws):
        col = p[-1] if len(p) > 2 and p[-1] else INK
        if p[0] == "log":
            ftext(c, "log", x, cy + size * 0.36, size, "black", col, a, align="left")
        elif p[0] == "sb":
            ftext(c, p[1], x, cy + size * 0.36, size, "black", col, a, align="left")
            ftext(c, p[2], x + ftext_w(p[1], "black", size) + size * 0.03, cy + size * 0.62, size * 0.58, "black",
                  col, a, align="left")
        elif p[0] == "m":
            mx(c, p[1], x, cy, size, a, col, align="left")
        else:
            ftext(c, p[1], x, cy + size * 0.36, size, "black", col, a, align="left")
        x += w_ + gap
    return total


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


# ---------------- o sismógrafo ----------------

def sismografo(c, x, y, w, h, a, prog_=1.0, amp=1.0, marca=0.0):
    """papel do sismógrafo com a onda riscada até prog_ (0..1); marca > 0 mostra a seta da AMPLITUDE no pico"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 14, PAPEL, a, shadow=True)
    for k in range(1, 6):
        line(c, x + 20, y + k * h / 6, x + w - 20, y + k * h / 6, mix(PAPEL, INK, 0.10), a, 2)
    cy = y + h / 2
    path = skia.Path()
    n = 260
    xe = x + 30 + (w - 60) * clamp(prog_)
    for i in range(n + 1):
        u = i / n
        xx = x + 30 + (w - 60) * u
        if xx > xe:
            break
        env = math.exp(-((u - 0.55) / 0.16) ** 2) * 0.92 + 0.06
        yy = cy - (h * 0.42) * amp * env * math.sin(u * 64)
        if i == 0:
            path.moveTo(xx, yy)
        else:
            path.lineTo(xx, yy)
    c.drawPath(path, paint(TINTA, a, stroke=4, cap_round=True))
    if prog_ < 1:
        c.drawCircle(xe, cy, 8, paint(RED, a))
    if marca > 0:
        # pico perto de u = 0,55: sin(64u) = 1 em u ≈ 0,54
        u = (math.pi / 2 + 2 * math.pi * 5) / 64
        xx = x + 30 + (w - 60) * u
        top = cy - (h * 0.42) * amp * (math.exp(-((u - 0.55) / 0.16) ** 2) * 0.92 + 0.06)
        line(c, xx + 70, cy, xx + 70, top, BLUE, a * marca, 4)
        line(c, xx + 56, cy, xx + 84, cy, BLUE, a * marca, 4)
        line(c, xx + 56, top, xx + 84, top, BLUE, a * marca, 4)
        line(c, x + 30, cy, x + w - 30, cy, mix(BLUE, "#FFFFFF", 0.4), a * marca, 2)
        pill(c, "AMPLITUDE", xx + 100, (cy + top) / 2, BLUE, size=26, a=a * marca, bounds=(0, 1920))


# ---------------- os dois placares ----------------

def placar(c, cx, y, titulo, valor, col, a, sub=""):
    if a <= 0:
        return
    rrect(c, cx - 300, y, 600, 300, 28, "#FFFFFF", a, shadow=True)
    rrect(c, cx - 300, y, 600, 74, 28, col, a * 0.16)
    text(c, titulo, cx, y + 50, 30, "black", col, a, tracking=2)
    text_mid(c, valor, cx, y + 175, 96, "black", col, a)
    if sub:
        text(c, sub, cx, y + 272, 24, "bold", INK2, a)


def _mag(c, cx, cy, m, a, col=PURPLE):
    """o mostrador da magnitude"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, 78, paint(mix("#FFFFFF", col, 0.14), a))
    c.drawCircle(cx, cy, 78, paint(col, a, stroke=6))
    text_mid(c, str(m), cx, cy - 6, 70, "black", col, a)
    text(c, "magnitude", cx, cy + 112, 24, "bold", INK2, a)


# ---------------- a fórmula de M_w ----------------

MW = [("sb", "M", "w", PURPLE), ("t", "=", INK), ("m", "2/3", INK), ("t", "·", INK), ("log", "", INK),
      ("t", "M₀", INK), ("t", "− 10,7", INK)]


def formula_mw(c, cx, cy, size, a, nums=0.0):
    """M_w = 2/3 · log M₀ − 10,7, com os badges 1º multiplica / 2º subtrai (nums = 0..1)"""
    w = lrow(c, MW, cx, cy, size, a)
    if nums > 0 and a > 0:
        x0 = cx - w / 2
        gap = size * 0.22
        ws = [_pw(p, size) for p in MW]
        xs = [x0 + sum(ws[:k]) + gap * k for k in range(len(MW))]
        xm = (xs[2] + xs[5] + ws[5]) / 2
        xsub = xs[6] + ws[6] / 2
        for k, (xx, s_, col) in enumerate(((xm, "multiplica", PURPLE), (xsub, "subtrai", AMBER))):
            ak = a * nums
            badge_num(c, k + 1, xx - 60, cy - size * 1.15, ak, 24, bg=col)
            text(c, s_, xx - 28, cy - size * 1.15 + 9, 26, "black", col, ak, align="left")
    return w


# ---------------- a cadeia de ida e volta ----------------

def cadeia(c, t, nos, ops, x0, y, passo, a, cues, col, setas_para_esquerda=False):
    """nós em linha com as operações nas setas; cues[k] = instante em que o nó k+1 (e a seta k) aparecem"""
    if a <= 0:
        return
    for k, s_ in enumerate(nos):
        ak = a if k == 0 else a * ep(t, cues[k - 1], 0.4)
        if ak <= 0:
            continue
        xx = x0 + k * passo
        rrect(c, xx - 110, y - 50, 220, 100, 22, mix("#FFFFFF", col, 0.10), ak)
        mx(c, s_, xx, y, 46, ak, col)
        if k < len(nos) - 1:
            ak2 = a * ep(t, cues[k], 0.4)
            if ak2 > 0:
                x1, x2 = xx + 120, xx + passo - 120
                if setas_para_esquerda:
                    x1, x2 = x2, x1
                arrow(c, x1, y, x2, y, col, ak2, 5, 14)
                pill(c, ops[k], (xx + xx + passo) / 2, y - 66, col, size=24, a=ak2, anchor="center", bounds=(0, 1920))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO LOGARÍTMICA · EPISÓDIO 3", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        linha(c, [("magnitude ", INK2), ("5", PURPLE), ("  →  ", INK2), ("7", PURPLE)], 960, 230, 44, aa)
    placar(c, 620, 300, "AMPLITUDE", "× 100", BLUE, aa, "o risco do sismógrafo")
    ab = ep(t, C["01.b"], 0.5)
    placar(c, 1300, 300, "ENERGIA", "× 1 000", PURPLE, ab, "a força liberada")
    acc = ep(t, C["01.c"], 0.5)
    alts = [("A", "3"), ("B", "100"), ("C", "1 000"), ("D", "10 000"), ("E", "63 000")]
    for k, (L, s_) in enumerate(alts):
        ak = acc * ep(t, C["01.c"] + 0.15 * k, 0.3)
        if ak <= 0:
            continue
        x = 420 + k * 270
        hot = L in "BC"
        col = AMBER if hot else INK2
        rrect(c, x - 115, 650, 230, 110, 20, mix("#FFFFFF", col, 0.16 if hot else 0.04), ak, shadow=True)
        badge_num(c, L, x, 650, ak, 20, bg=col if hot else INK)
        text_mid(c, s_, x, 712, 40, "black", col if hot else INK, ak)
    if acc > 0:
        selo(c, 960, 800, ep(t, C["01.c"] + 1.6, 0.4), "AS DUAS ESTÃO NAS ALTERNATIVAS", AMBER, -2, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO LOGARÍTMICA · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de FUNÇÃO LOGARÍTMICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "AMPLITUDE × ENERGIA", "sem confundir os fatores", PURPLE),
             ("02.b", "MAGNITUDE POR FÓRMULA", "substituir e operar na ordem", GREEN)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 640 + k * 640
        rrect(c, x - 290, 330, 580, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 290, 330, 580, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 38, "black", col, ak)
        text(c, sub, x, 625, 26, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódio 2", 300, y - 75, BLUE, size=22, a=a)
        lrow(c, [("t", "quantas vezes  =", INK), ("m", "10^{diferença}", BLUE)], 960, y + 4, 52, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "série de Logaritmos", 300, y - 75, PURPLE, size=22, a=a)
        lrow(c, [("log", "", INK), ("m", "A/A₀", INK), ("t", "=", INK), ("log", "", PURPLE), ("t", "A −", PURPLE),
                 ("log", "", PURPLE), ("t", "A₀", PURPLE)], 960, y + 4, 52, a)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "conta que vai aparecer", 300, y - 75, GREEN, size=22, a=a)
        lrow(c, [("m", "10^{1,5}", INK), ("t", "= 10 · √10  ≈", INK2), ("t", "31,6", GREEN)], 960, y + 4, 54, a)


# ======================================================================
# concreto — a manchete e o sismógrafo
# ======================================================================

def b_manchete(c, t, C, B):
    head(c, t, B["start"], "A MANCHETE", "SETE O QUÊ?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    if a0 > 0:
        rrect(c, 300, 200, 640, 300, 10, "#FFFFFF", a0, shadow=True)
        text(c, "JORNAL DO DIA", 620, 245, 22, "black", INK2, a0, tracking=4)
        line(c, 330, 265, 910, 265, INK2, a0, 2)
        text(c, "TERREMOTO DE", 620, 335, 52, "black", INK, a0)
        text(c, "MAGNITUDE 7", 620, 400, 52, "black", RED, a0)
        text(c, "na escala Richter", 620, 450, 28, "bold", INK2, a0)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        selo(c, 1300, 340, aa, "7 O QUÊ?", AMBER, -6, 52)
    ab = ep(t, C["04.b"], 0.5)
    sismografo(c, 300, 540, 1320, 260, ab, prog_=clamp((t - C["04.b"]) / 4.0), amp=1.0,
               marca=ep(t, C["04.c"], 0.5))
    if ab > 0:
        pill(c, "SISMÓGRAFO: risca o papel quando o chão treme", 1620, 520, BLUE, size=24, a=ab, anchor="right",
             bounds=(0, 1920))


# ======================================================================
# bloco a — amplitude · bloco b — energia
# ======================================================================

def b_amplitude(c, t, C, B):
    head(c, t, B["start"], "MAGNITUDE PELA AMPLITUDE", "O RISCO VIRA NÚMERO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    defin(c, "AMPLITUDE DE REFERÊNCIA (A₀)", "um tremor pequenininho, combinado como padrão", 260, 220, 1400, aa,
          BLUE, 30)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        K.boxed(c, 460, 350, 1000, 200, PURPLE, ab, 0.08)
        lrow(c, [("t", "M  =", PURPLE), ("log", "", PURPLE), ("m", "A/A₀", PURPLE)], 960, 450, 76, ab)
        text(c, "MAGNITUDE: o log da comparação", 960, 600, 28, "black", BLUE, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, 460, 660, 1000, 110, 22, "#FFFFFF", acc, shadow=True)
        linha(c, [("+1 grau  →  amplitude ", INK), ("× 10", BLUE)], 960, 715, 44, acc)


def b_energia(c, t, C, B):
    head(c, t, B["start"], "A ENERGIA LIBERADA", "OUTRA FÓRMULA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    defin(c, "ENERGIA LIBERADA (E)", "o tanto de energia que o tremor solta, em joules (J)", 260, 220, 1400, aa, BLUE,
          30)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        K.boxed(c, 400, 360, 1120, 200, PURPLE, ab, 0.08)
        lrow(c, [("log", "", PURPLE), ("t", "E  =  4,8  +", PURPLE), ("t", "1,5", PURPLE), ("t", "M", PURPLE)], 960, 460,
             76, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        w_all = lrow(c, [("log", "", PURPLE), ("t", "E  =  4,8  +", PURPLE), ("t", "1,5", PURPLE), ("t", "M", PURPLE)],
                     960, 460, 76, 0)
        gap = 76 * 0.22
        x15 = 960 - w_all / 2 + ftext_w("log", "black", 76) + gap + ftext_w("E  =  4,8  +", "black", 76) + gap
        w15 = ftext_w("1,5", "black", 76)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x15 - 12, 405, w15 + 24, 110), 18, 18),
                    paint(AMBER, acc, stroke=7))
        pill(c, "é ele que muda tudo", x15 + w15 / 2, 640, AMBER, size=30, a=acc, anchor="center")


def b_placares(c, t, C, B):
    head(c, t, B["start"], "DOIS PLACARES", "O MESMO TERREMOTO", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.5)
    m = 5 if t < C["07.a"] else (6 if t < C["07.b"] else 7)
    _mag(c, 960, 330, m, a0)
    if t < C["07.a"]:
        va, ve = "× 1", "× 1"
    elif t < C["07.b"]:
        va, ve = "× 10", "× 32"
    else:
        va, ve = "× 100", "× 1 000"
    placar(c, 470, 220, "AMPLITUDE", va, BLUE, a0, "× 10 por grau")
    placar(c, 1450, 220, "ENERGIA", ve, PURPLE, a0, "× 32 por grau")
    for k, cue in enumerate(("07.a", "07.b")):
        ak = ep(t, C[cue], 0.4) * (1 - ep(t, C[cue] + 3.5, 0.4))
        if ak > 0:
            pill(c, "× 10", 470, 570, BLUE, size=34, a=ak, anchor="center")
            pill(c, "× 10 elevado a 1,5 ≈ 32", 1450, 570, PURPLE, size=34, a=ak, anchor="center")
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 640, 1200, 130, 24, "#FFFFFF", acc, shadow=True)
        linha(c, [("5 → 7:   amplitude ", INK), ("× 100", BLUE), ("   ·   energia ", INK), ("× 1 000", PURPLE)], 960,
              690, 40, acc)
        mx(c, "10^2  e  10^3", 960, 740, 30, acc, INK2)


# ======================================================================
# bloco c — comparação (a constante se cancela)
# ======================================================================

def b_comparacao(c, t, C, B):
    head(c, t, B["start"], "COMPARAR SEM CALCULAR", "A CONSTANTE SE CANCELA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    ab = ep(t, C["08.b"], 0.5)
    for k, (sub, m) in enumerate((("7", "7"), ("5", "5"))):
        y = 260 + k * 110
        if aa <= 0:
            continue
        lrow(c, [("log", "", INK), ("sb", "E", sub, INK), ("t", "=", INK), ("t", "4,8", INK), ("t", "+  1,5 · " + m,
                 INK)], 900, y, 54, aa)
        if ab > 0:
            w = lrow(c, [("log", "", INK), ("sb", "E", sub, INK), ("t", "=", INK)], 900, y, 54, 0)
            wt = lrow(c, [("log", "", INK), ("sb", "E", sub, INK), ("t", "=", INK), ("t", "4,8", INK),
                          ("t", "+  1,5 · " + m, INK)], 900, y, 54, 0)
            x48 = 900 - wt / 2 + w + 54 * 0.22
            strike(c, x48 - 6, y, x48 + ftext_w("4,8", "black", 54) + 6, y, ab, RED, ab)
    if aa > 0:
        line(c, 520, 418, 1280, 418, INK2, aa * ep(t, C["08.a"] + 1.2, 0.4), 3)
        text(c, "−", 480, 390, 60, "black", INK2, aa * ep(t, C["08.a"] + 1.2, 0.4))
    if ab > 0:
        selo(c, 1440, 320, ab, "4,8 SE CANCELA", GREEN, -6, 30)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        lrow(c, [("log", "", PURPLE), ("sb", "E", "7", PURPLE), ("t", "−", PURPLE), ("log", "", PURPLE),
                 ("sb", "E", "5", PURPLE), ("t", "=  1,5 · (7 − 5)  =  3", PURPLE)], 960, 510, 52, acc)
        pill(c, "MULTIPLIQUE a diferença pelo coeficiente", 960, 590, PURPLE, size=28, a=ep(t, C["08.c"] + 3.0, 0.4),
             anchor="center")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 560, 660, 800, 120, 24, mix("#FFFFFF", GREEN, 0.14), ad)
        lrow(c, [("m", "E₇/E₅", INK), ("t", "=", INK), ("m", "10^3", GREEN), ("t", "=  1 000", GREEN)], 960, 720, 54,
             ad)


def b_atalho_zeros(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONTE OS ZEROS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 620, GREEN, a0, 0.08)
        text(c, "ATALHO · ENERGIA DOS TERREMOTOS", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        linha(c, [("a cada ", INK), ("2 graus", PURPLE), (" → ", INK), ("+3 zeros", GREEN)], 960, 360, 60, aa)
    ab = ep(t, C["09.b"], 0.5)
    for k, (g, v) in enumerate((("2 graus", "× 1 000"), ("4 graus", "× 1 000 000"))):
        ak = ab * ep(t, C["09.b"] + 1.4 * k, 0.4)
        if ak > 0:
            x = 660 + k * 600
            rrect(c, x - 260, 450, 520, 150, 24, "#FFFFFF", ak, shadow=True)
            text(c, g, x, 500, 30, "bold", INK2, ak)
            text_mid(c, v, x, 555, 50, "black", PURPLE, ak)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        linha(c, [("na amplitude: ", INK2), ("1 zero por grau", BLUE)], 960, 700, 40, acc)


# ======================================================================
# bloco d — magnitude de momento · atalho dos 2/3
# ======================================================================

def b_momento(c, t, C, B):
    head(c, t, B["start"], "MAGNITUDE DE MOMENTO", "A ESCALA DOS SISMÓLOGOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    defin(c, "MOMENTO SÍSMICO (M₀)", "o tamanho da ruptura da rocha, em dina·cm", 260, 200, 1400, aa, BLUE, 30)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        K.boxed(c, 360, 320, 1200, 170, PURPLE, ab, 0.08)
        formula_mw(c, 960, 420, 64, ab, ep(t, C["10.d"], 0.4))
        pill(c, "no noticiário: “escala Richter”", 1560, 490, INK2, size=20, a=ab, anchor="right", bounds=(0, 1920))
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        lrow(c, [("t", "M₀ =", INK), ("m", "10^{24}", INK), ("t", "→", INK2), ("log", "", INK), ("t", "M₀ =", INK),
                 ("t", "24", BLUE)], 960, 560, 46, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        badge_num(c, 1, 560, 655, ad, 24, bg=PURPLE)
        lrow(c, [("m", "2/3", PURPLE), ("t", "· 24  =  16", PURPLE)], 600, 660, 46, ad, align="left")
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        badge_num(c, 2, 560, 760, ae, 24, bg=AMBER)
        linha(c, [("16 − 10,7  =  ", INK), ("5,3", GREEN)], 600, 760, 46, ae, align="left")
        selo(c, 1400, 720, ep(t, C["10.e"] + 2.0, 0.4), "Mw = 5,3", GREEN, -4, 40)


def b_atalho_terco(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DOIS TERÇOS SEM SOFRER", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 620, GREEN, a0, 0.08)
        text(c, "ATALHO · 2/3 DE UM NÚMERO", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("÷ 3", GREEN), ("   e depois   ", INK), ("dobre", GREEN)], 960, 360, 64, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 460, 450, 1000, 120, 22, "#FFFFFF", ab, shadow=True)
        linha(c, [("24 ÷ 3 = 8   →   8 · 2 = ", INK), ("16", GREEN)], 960, 510, 46, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        lrow(c, [("log", "", INK), ("m", "10^{n}", INK), ("t", "=", INK), ("t", "n", GREEN)], 960, 690, 64, acc)
        text(c, "o log da potência de 10 é o próprio expoente", 960, 780, 28, "bold", INK2, acc)


# ======================================================================
# bloco e — o caminho inverso · bloco f — qual dos dois?
# ======================================================================

def _roupa(c, cx, cy, s, col, a, casaco=False):
    """camiseta (ou casaco, com zíper) estilizada"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 0.30 * s, cy - 0.45 * s)
    p.lineTo(cx - 0.62 * s, cy - 0.20 * s)
    p.lineTo(cx - 0.48 * s, cy + (0.20 if casaco else 0.0) * s)
    p.lineTo(cx - 0.34 * s, cy - 0.08 * s)
    p.lineTo(cx - 0.34 * s, cy + 0.50 * s)
    p.lineTo(cx + 0.34 * s, cy + 0.50 * s)
    p.lineTo(cx + 0.34 * s, cy - 0.08 * s)
    p.lineTo(cx + 0.48 * s, cy + (0.20 if casaco else 0.0) * s)
    p.lineTo(cx + 0.62 * s, cy - 0.20 * s)
    p.lineTo(cx + 0.30 * s, cy - 0.45 * s)
    p.lineTo(cx + 0.12 * s, cy - 0.45 * s)
    p.quadTo(cx, cy - 0.30 * s, cx - 0.12 * s, cy - 0.45 * s)
    p.close()
    c.drawPath(p, paint(col, a))
    if casaco:
        line(c, cx, cy - 0.36 * s, cx, cy + 0.50 * s, mix(col, "#000000", 0.35), a, max(3, 0.04 * s))


def b_inverso(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO INVERSO", "DESFAÇA DE FORA PARA DENTRO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.5) * (1 - ep(t, C["12.a"], 0.4))
    if a0 > 0:
        lrow(c, [("sb", "M", "w", INK), ("t", "= 5,3", INK), ("t", "→", INK2), ("t", "M₀ = ?", AMBER)], 960, 460, 80, a0)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0 and t < C["12.b"] + 0.5:
        ak = aa * (1 - ep(t, C["12.b"], 0.5))
        _roupa(c, 760, 450, 220, mix(BLUE, "#FFFFFF", 0.3), ak)
        dx = 360 * ep(t, C["12.a"] + 2.8, 0.8)
        _roupa(c, 1160 + dx, 450, 250, AMBER, ak, casaco=True)
        text(c, "1º vestiu", 760, 650, 28, "bold", INK2, ak)
        text(c, "2º vestiu · 1º a tirar", 1160 + dx, 650, 28, "bold", AMBER, ak)
        return
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        text(c, "IDA (a fórmula)", 260, 250, 26, "black", PURPLE, ab, align="left")
        cadeia(c, t, ["24", "16", "5,3"], ["× 2/3", "− 10,7"], 560, 340, 420, ab, [-1e9, -1e9], PURPLE)
        text(c, "VOLTA (desfaça na ordem contrária)", 260, 500, 26, "black", GREEN, ab, align="left")
    cadeia(c, t, ["5,3", "16", "24", "10^{24}"], ["+ 10,7", "× 3/2", "10 elevado"], 400, 600, 420, ab,
           [C["12.b"] + 1.5, C["12.c"], C["12.d"]], GREEN)
    ad = ep(t, C["12.d"] + 2.4, 0.4)
    if ad > 0:
        pill(c, "M₀ = 10²⁴ · voltamos ao começo", 960, 780, GREEN, size=28, a=ad, anchor="center")


def b_qual(c, t, C, B):
    head(c, t, B["start"], "DE 5 PARA 7", "CEM OU MIL?", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        selo(c, 960, 260, aa, "DEPENDE DA PERGUNTA", AMBER, -3, 44)
    ab = ep(t, C["13.b"], 0.5)
    placar(c, 620, 360, "AMPLITUDE", "× 100", BLUE, ab, "“amplitude” · “risco do sismógrafo”")
    acc = ep(t, C["13.c"], 0.5)
    placar(c, 1300, 360, "ENERGIA", "× 1 000", PURPLE, acc, "“energia liberada”")
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        pill(c, "LEIA qual das duas o enunciado pede", 960, 760, GREEN, size=32, a=ad, anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "MULTIPLICA, DEPOIS SUBTRAI",
                                                                         GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        formula_mw(c, 960, 260, 50, aa)
        lrow(c, [("t", "M₀ =", INK), ("m", "10^{21}", BLUE), ("t", "dina·cm", INK2)], 960, 360, 52, aa)
    if t < C["15"]:
        pause_timer(c, t, C["14.end"] - 1.9, 960, 600)
        return
    a1 = ep(t, C["15.a"], 0.5)
    if a1 > 0:
        lrow(c, [("log", "", INK), ("m", "10^{21}", INK), ("t", "=  21", BLUE)], 960, 470, 46, a1)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        badge_num(c, 1, 560, 565, ab, 24, bg=PURPLE)
        lrow(c, [("m", "2/3", PURPLE), ("t", "· 21  =  14", PURPLE)], 600, 570, 46, ab, align="left")
        text(c, "21 ÷ 3 = 7 · dobrado = 14", 1560, 580, 24, "bold", GREEN, ab, align="right")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        badge_num(c, 2, 560, 670, acc, 24, bg=AMBER)
        linha(c, [("14 − 10,7  =  ", INK), ("3,3", GREEN)], 600, 670, 46, acc, align="left")
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        pill(c, "expoente menor (21 < 24) → magnitude menor (3,3 < 5,3)", 960, 780, GREEN, size=26, a=ad,
             anchor="center")


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Um grau a mais: amplitude ×10, energia cerca de ×32.",
          "Na comparação, a constante se cancela: multiplique a diferença pelo coeficiente e eleve 10.",
          "Na fórmula, multiplique primeiro e subtraia depois; para voltar, desfaça de fora para dentro."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "25"])
    frame(c, t, B["start"] if sid == "16" else C["25"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else
          "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 280 + k * 190 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1360, 56)


ERROS = [("Dois graus a mais: energia × 100",
          "na amplitude é assim: um zero por grau",
          "na energia, o fator por grau é 10 elevado a 1,5 ≈ 32. Dois graus: 10³ = × 1 000."),
         ("Subtrair 10,7 antes: 2/3 · (24 − 10,7) ≈ 8,9",
          "parece que o 2/3 multiplica tudo o que vem depois dele",
          "multiplique primeiro: 2/3 · 24 = 16. Depois subtraia: 16 − 10,7 = 5,3.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=820):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS3 = [("A", "3 vezes maior", "esqueceu de elevar 10", RED), ("B", "100 vezes maior", "é a das amplitudes", RED),
         ("C", "1 000 vezes maior", "", GREEN), ("D", "10 000 vezes maior", "amplitudes ao quadrado", RED),
         ("E", "63 000 vezes maior", "manteve o 4,8", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "ENERGIA DE DOIS TERREMOTOS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["19.a"], 0.4)
    cues_in = {L: C[f"19.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"21.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS3, 1095, 250, 655, 32, C["20.ok"], "C", cues_in, cues_x, gap=34)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["20"], 0.3)),
         align="left")
    if t < C["20"]:
        y = _enunciado(c, [("A energia E, em joules, liberada por um terremoto de magnitude M pode ser estimada por",
                            INK)], a0, 260, 30)
        lrow(c, [("log", "", PURPLE), ("t", "E = 4,8 + 1,5M", PURPLE)], 190, y + 30, 46, a0, align="left")
        ab = ep(t, C["19.b"], 0.4)
        _enunciado(c, [("Comparado a um tremor de magnitude 5, um terremoto de magnitude 7 libera uma energia "
                        "aproximadamente", INK)], ab, y + 110, 30)
        return
    a1 = ep(t, C["20"], 0.4)
    rrect(c, 170, 200, 900, 630, 18, "#FFFFFF", a1, shadow=True)
    if a1 > 0:
        pill(c, "pergunta: QUANTAS VEZES · ENERGIA", 620, 250, PURPLE, size=24, a=a1, anchor="center")
    aa = ep(t, C["20.a"], 0.4)
    if aa > 0:
        lrow(c, [("log", "", INK), ("sb", "E", "7", INK), ("t", "−", INK), ("log", "", INK), ("sb", "E", "5", INK),
                 ("t", "→  4,8 − 4,8 = 0", INK2)], 620, 340, 38, aa)
    ab = ep(t, C["20.b"], 0.4)
    if ab > 0:
        linha(c, [("1,5 · (7 − 5)  =  ", INK), ("3", PURPLE)], 620, 450, 48, ab)
    acc = ep(t, C["20.c"], 0.4)
    if acc > 0:
        lrow(c, [("m", "E₇/E₅", INK), ("t", "=", INK), ("m", "10^3", GREEN), ("t", "=  1 000", GREEN)], 620, 570, 50,
             acc)
    ad = ep(t, C["20.d"], 0.4)
    if ad > 0:
        rrect(c, 230, 680, 780, 90, 16, mix("#FFFFFF", GREEN, 0.14), ad)
        linha(c, [("energia (1 000) > amplitude (100)  ", INK), ("FAZ SENTIDO", GREEN)], 620, 725, 28, ad)


ALTS8 = [("A", "7,3", "", GREEN), ("B", "10,9", "subtraiu antes", RED), ("C", "18,0", "esqueceu o − 10,7", RED),
         ("D", "28,7", "somou 10,7", RED), ("E", "29,8", "inverteu a fração (3/2)", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · VOCÊ FAZ", "MAGNITUDE DE MOMENTO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS8, 1200, 250, 480, 40, C["23.ok"], "A", cues_in, cues_x, gap=40)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["23"], 0.3)),
         align="left")
    if t < C["23"]:
        if a0 > 0:
            text(c, "A magnitude de momento é calculada por", 190, 260, 30, "black", INK, a0, align="left")
            formula_mw(c, 600, 340, 46, a0)
            text(c, "com M₀ (momento sísmico) em dina·cm.", 190, 420, 30, "black", INK, a0, align="left")
        ab = ep(t, C["22.b"], 0.4)
        if ab > 0:
            lrow(c, [("t", "Para M₀ =", INK), ("m", "10^{27}", BLUE), ("t", "dina·cm, a magnitude é", INK)], 190, 510, 32,
                 ab, align="left")
        pause_timer(c, t, C["22.end"] - 1.9, 600, 680)
        return
    a1 = ep(t, C["23"], 0.4)
    rrect(c, 170, 200, 960, 630, 18, "#FFFFFF", a1, shadow=True)
    if a1 > 0:
        lrow(c, [("log", "", INK), ("m", "10^{27}", INK), ("t", "=  27", BLUE)], 650, 280, 44, a1)
    aa = ep(t, C["23.a"], 0.4)
    if aa > 0:
        badge_num(c, 1, 260, 385, aa, 22, bg=PURPLE)
        lrow(c, [("m", "2/3", PURPLE), ("t", "· 27  =  18", PURPLE)], 300, 390, 44, aa, align="left")
        text(c, "27 ÷ 3 = 9 · dobrado = 18", 1090, 400, 22, "bold", GREEN, aa, align="right")
    ab = ep(t, C["23.b"], 0.4)
    if ab > 0:
        badge_num(c, 2, 260, 500, ab, 22, bg=AMBER)
        linha(c, [("18 − 10,7  =  ", INK), ("7,3", GREEN)], 300, 500, 44, ab, align="left")
    acc = ep(t, C["23.c"], 0.4)
    if acc > 0:
        rrect(c, 220, 590, 860, 170, 16, mix("#FFFFFF", GREEN, 0.12), acc)
        text(c, "DE VOLTA (fora para dentro)", 650, 630, 22, "black", GREEN, acc, tracking=2)
        lrow(c, [("t", "7,3 + 10,7 = 18   →   18 ·", INK), ("m", "3/2", INK), ("t", "= 27", GREEN)], 650, 700, 36, acc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DECIBÉIS", PURPLE)
    aa = ep(t, C["26.a"], 0.5)
    for k in range(2):
        ak = aa * ep(t, C["26.a"] + 0.6 * k, 0.4)
        if ak > 0:
            x = 560 + k * 400
            rrect(c, x - 140, 260, 280, 220, 24, "#FFFFFF", ak, shadow=True)
            c.drawCircle(x, 340, 52, paint(mix("#FFFFFF", PURPLE, 0.2), ak))
            c.drawCircle(x, 340, 52, paint(PURPLE, ak, stroke=6))
            c.drawCircle(x, 340, 16, paint(PURPLE, ak))
            text(c, "80 dB", x, 450, 40, "black", INK, ak)
    if aa > 0:
        text_mid(c, "+", 760, 370, 70, "black", INK2, aa)
        linha(c, [("=  ", INK2), ("160 dB ?", AMBER)], 1340, 370, 70, ep(t, C["26.a"] + 1.4, 0.4))
    ab = ep(t, C["26.b"], 0.5)
    if ab > 0:
        selo(c, 960, 600, ab, "MAIS BARULHO QUE UM AVIÃO?", RED, -3, 40)
    acc = ep(t, C["26.c"], 0.5)
    if acc > 0:
        pill(c, "próximo episódio", 960, 740, PURPLE, size=32, a=acc, anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"],
        "Você teria marcado cem ou mil na questão da energia?", canal="no Estudativo", anki=C["27.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, manchete=b_manchete, amplitude=b_amplitude,
              energia=b_energia, placares=b_placares, comparacao=b_comparacao, atalho_zeros=b_atalho_zeros,
              momento=b_momento, atalho_terco=b_atalho_terco, inverso=b_inverso, qual=b_qual, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q3=b_q3, q8=b_q8, ponte=b_ponte, cta=b_cta)
