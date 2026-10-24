"""Visual — Progressão Aritmética, Episódio 3: a soma de Gauss (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: pares() (as fichas 1…100 se dando as mãos em pares de 101 que empilham), escadas() (duas escadas de
bloquinhos 1 a 6 que se encaixam num retângulo 6 × 7), teatro() (o teatro visto de cima, fileiras crescendo de 2 em 2 com
contador de cadeiras), fila_pa() (fichas de uma PA com arcos ligando os pares equidistantes), linha() (texto com cor por
trecho, mantém o espaço de milhar).
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
_s = importlib.util.spec_from_file_location("comum046", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pa_ep3_soma_gauss.mp4"
CARD_R = K.CARD_R
TEAL = "#0E9384"


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


def sub(n):
    return str(n).translate(str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉"))


def ficha(c, s, cx, cy, a, col=INK, w=78, h=66, size=32, fill="#FFFFFF"):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 12, fill, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 12, 12), paint(col, a, stroke=3))
    text_mid(c, s, cx, cy, size, "black", col, a)


def arco(c, x0, x1, y, alt, col, a, sw=5, label=None, size=28):
    """arco ligando duas fichas (por cima), com rótulo no topo"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x0, y)
    p.cubicTo(x0, y - alt, x1, y - alt, x1, y)
    c.drawPath(p, paint(col, a, stroke=sw))
    if label:
        pill(c, label, (x0 + x1) / 2, y - alt * 0.75, col, size=size, a=a, anchor="center", bounds=(0, 1920))


def pares(c, t, t0, a, x0=260, x1=1660, y=560):
    """1 2 3 4 5 … 96 97 98 99 100: os arcos de 101 aparecem em sequência a partir de t0"""
    if a <= 0:
        return
    esq = [1, 2, 3, 4, 5]
    dir_ = [96, 97, 98, 99, 100]
    xs_e = [x0 + k * 96 for k in range(5)]
    xs_d = [x1 - (4 - k) * 96 for k in range(5)]
    for v, x in zip(esq, xs_e):
        ficha(c, str(v), x, y, a, BLUE)
    text_mid(c, "…", (xs_e[-1] + xs_d[0]) / 2, y, 60, "black", INK2, a)
    for v, x in zip(dir_, xs_d):
        ficha(c, str(v), x, y, a, BLUE)
    for k in range(5):
        ak = ep(t, t0 + k * 0.7, 0.4)
        arco(c, xs_e[k], xs_d[4 - k], y - 36, 120 + (4 - k) * 46, PURPLE, a * ak, 5, None)
    pill(c, "cada par = 101", (x0 + x1) / 2, y - 36 - 304 * 0.75 - 30, PURPLE, size=28, a=a * ep(t, t0, 0.4), anchor="center",
         bounds=(0, 1920))


def pilha_101(c, cx, ybase, n, a, total=50):
    """pilha de barrinhas '101' (desenha n de total, comprimida)"""
    if a <= 0:
        return
    hh = 300 / total
    for k in range(int(n)):
        rrect(c, cx - 80, ybase - (k + 1) * hh, 160, hh - 1.2, 2, PURPLE, a * (0.55 + 0.45 * (k % 2)))
    ftext(c, f"{int(n)} pares", cx, ybase + 44, 30, "black", INK, a)


def escadas(c, x0, ybase, a, u=1.0, cel=54, n=6, mostrar2=True):
    """escada 1..n (azul, apoiada à esquerda) + escada invertida (laranja) que entra por cima: u = 0..1 encaixe"""
    if a <= 0:
        return
    for col in range(n):
        h = col + 1
        for r in range(h):
            x = x0 + col * cel
            y = ybase - (r + 1) * cel
            rrect(c, x + 2, y + 2, cel - 4, cel - 4, 6, BLUE, a)
    if not mostrar2:
        return
    off = (1 - u) * 260
    for col in range(n):
        h = n - col
        for r in range(h):
            x = x0 + col * cel
            y = ybase - (n + 1) * cel + r * cel - off
            rrect(c, x + 2, y + 2, cel - 4, cel - 4, 6, AMBER, a)


def teatro(c, cx, ytop, a, nfil, px=9.5, row_h=17):
    """teatro visto de cima: nfil fileiras (pode ser fracionário), fileira k com 20 + 2k cadeiras"""
    if a <= 0:
        return 0
    rrect(c, cx - 200, ytop - 60, 400, 40, 10, "#3A3F4A", a)
    text_mid(c, "PALCO", cx, ytop - 40, 22, "black", "#FFFFFF", a)
    total = 0
    for k in range(25):
        f = clamp(nfil - k)
        if f <= 0:
            break
        nc = 20 + 2 * k
        y = ytop + k * row_h
        w = nc * px
        for j in range(nc):
            x = cx - w / 2 + j * px + px / 2
            c.drawCircle(x, y, px * 0.36, paint(BLUE if k not in (0, 24) else PURPLE, a * f))
        total += nc if f >= 1 else 0
    return total


def fila_pa(c, valores, x0, y, a, passo=118, col=BLUE, size=30, w=90):
    xs = [x0 + k * passo for k in range(len(valores))]
    for v, x in zip(valores, xs):
        ficha(c, str(v), x, y, a, col, w=w, size=size)
    return xs


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROGRESSÃO ARITMÉTICA · EPISÓDIO 3", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        linha(c, [("1 + 2 + 3 + … + 100 = ", INK), ("?", AMBER)], W / 2, 290, 84, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 560, 380, 800, 200, 30, mix("#FFFFFF", GREEN, 0.14), ab, shadow=True)
        text(c, "UM MENINO DE 10 ANOS · EM SEGUNDOS", W / 2, 440, 30, "black", GREEN, ab)
        text_mid(c, "5 050", W / 2, 520, 92, "black", GREEN, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        pill(c, "não era mais rápido nas contas", W / 2, 660, INK2, size=30, a=acc, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 770, ad, "JUNTOU DO JEITO CERTO", PURPLE, -3, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "PROGRESSÃO ARITMÉTICA · EP. 3", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "3º episódio da série de PROGRESSÃO ARITMÉTICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "SOMAR QUALQUER PA", "em uma linha", PURPLE), ("02.b", "TERMO OU SOMA?", "ler o enunciado certo", AMBER)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 300, 330, 600, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 300, 330, 600, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 44, "black", col, ak)
        text(c, sub, x, 625, 30, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 330 + d
        rrect(c, 260, y - 90, 1400, 180, 24, "#FFFFFF", a, shadow=True)
        pill(c, "episódio 1 · termo geral", 300, y - 90, BLUE, size=22, a=a, bounds=(0, 1920))
        linha(c, [("aₙ = a₁ + (n − 1) · r", INK)], W / 2, y + 10, 64, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 600 + d
        rrect(c, 260, y - 90, 1400, 180, 24, "#FFFFFF", a, shadow=True)
        pill(c, "média de dois números", 300, y - 90, BLUE, size=22, a=a, bounds=(0, 1920))
        linha(c, [("(20 + 68) ÷ 2 = 88 ÷ 2 = ", INK), ("44", GREEN)], W / 2, y + 10, 58, a)


# ======================================================================
# bloco a — Gauss
# ======================================================================

def b_gauss(c, t, C, B):
    head_seq(c, t, C, [("04", "COMO SOMAR 100 NÚMEROS", "EM SEGUNDOS?", BLUE), ("05", "QUANTOS PARES?", "O TRUQUE DE GAUSS", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0 and t < C["05"]:
        pill(c, "Gauss · um dos maiores matemáticos da história", W / 2, 230, BLUE, size=28, a=aa, anchor="center")
    ab = ep(t, C["04.b"], 0.5)
    if t < C["05"]:
        pares(c, t, C["04.b"] + 0.6, ab, y=640)
        acc = ep(t, C["04.c"], 0.5)
        if acc > 0:
            regra(c, "1 + 100 = 2 + 99 = 3 + 98 = 101", W / 2, 790, acc, 36)
        return
    # cena 05: a pilha de pares e a conta
    a5 = ep(t, C["05.a"], 0.5)
    n = 50 * clamp((t - C["05.a"] - 0.3) / 2.6)
    pilha_101(c, 520, 640, max(1, n), a5)
    if a5 > 0:
        linha(c, [("100 números ÷ 2 = ", INK), ("50 pares", PURPLE)], 1200, 290, 44, a5)
    ab5 = ep(t, C["05.b"], 0.5)
    if ab5 > 0:
        linha(c, [("50 · 101 = ", INK), ("5 050", GREEN)], 1200, 420, 76, ab5)
    ac5 = ep(t, C["05.c"], 0.5)
    if ac5 > 0:
        rrect(c, 900, 500, 600, 110, 22, mix("#FFFFFF", BLUE, 0.10), ac5)
        linha(c, [("EXTREMOS: ", BLUE), ("o primeiro e o último", INK)], 1200, 555, 32, ac5)
    ad5 = ep(t, C["05.d"], 0.5)
    if ad5 > 0:
        regra(c, "todos os pares dão a MESMA soma", 1200, 720, ad5, 36)


# ======================================================================
# bloco b — as duas escadas
# ======================================================================

def b_escadas(c, t, C, B):
    head(c, t, B["start"], "POR QUE DÁ SEMPRE IGUAL?", "AS DUAS ESCADAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    ab = ep(t, C["06.b"], 0.5)
    u = ep(t, C["06.c"], 1.2)
    escadas(c, 300, 760, aa, u if ab > 0 else 0, 64, 6, mostrar2=ab > 0)
    if aa > 0:
        for k in range(6):
            text(c, str(k + 1), 300 + k * 64 + 32, 805, 30, "black", BLUE, aa)
    acc = ep(t, C["06.c"] + 1.2, 0.5)
    if acc > 0:
        line(c, 300, 820 - 10, 300 + 6 * 64, 820 - 10, INK2, acc, 0)
        pill(c, "6 colunas", 300 + 3 * 64, 850, INK, size=24, a=acc, anchor="center")
        pill(c, "7 em cada", 300 + 6 * 64 + 90, 760 - 3.5 * 64, AMBER, size=24, a=acc, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 1020, 260, 620, 330, 26, "#FFFFFF", ad, shadow=True)
        linha(c, [("2S = 6 · 7 = ", INK), ("42", PURPLE)], 1330, 350, 54, ad)
        linha(c, [("S = 42 ÷ 2 = ", INK), ("21", GREEN)], 1330, 450, 54, ep(t, C["06.d"] + 2.4, 0.4))
        regra(c, "por isso se DIVIDE POR 2", 1330, 680, ep(t, C["06.d"] + 4.2, 0.5), 34)


# ======================================================================
# bloco c — a fórmula · atalho da metade
# ======================================================================

def b_formula(c, t, C, B):
    head(c, t, B["start"], "DEFINIÇÃO E FÓRMULA", "A SOMA DOS n PRIMEIROS TERMOS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 120, 24, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("Sₙ", BLUE), (" = soma do 1º até o termo de posição n", INK)], W / 2, 270, 38, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        K.boxed(c, 460, 380, 1000, 190, PURPLE, ab, 0.08)
        K.expr(c, "Sₙ = (a₁+aₙ)·n/2", W / 2, 475, 76, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "NÚMERO DE TERMOS × MÉDIA DOS EXTREMOS", W / 2, 670, acc, 38)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        pill(c, "média do 1º com o último · vezes quantos termos há", W / 2, 775, INK2, size=28, a=ad, anchor="center")


def b_metade(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DIVIDA POR 2 ANTES", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 150, "ATALHO · SEM CALCULADORA", ["corte pela metade o número PAR, antes de multiplicar"], aa, 40)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        chip(c, "a₁ + aₙ par?", 700, 440, PURPLE, ab, 38)
        text_mid(c, "ou", W / 2, 440, 34, "bold", INK2, ab)
        chip(c, "n par?", 1220, 440, PURPLE, ab, 38)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 360, 540, 1200, 240, 24, "#FFFFFF", acc, shadow=True)
        linha(c, [("101 · 100 ÷ 2", INK)], W / 2, 610, 50, acc)
        linha(c, [("= 101 · ", INK), ("50", GREEN), (" = 5 050", INK)], W / 2, 700, 58, ep(t, C["08.c"] + 2.6, 0.4))
        strike(c, 880, 610, 1040, 610, ep(t, C["08.c"] + 2.2, 0.4), GREEN, 1)


# ======================================================================
# bloco d — o teatro
# ======================================================================

def b_teatro(c, t, C, B):
    head(c, t, B["start"], "E SE NÃO COMEÇA NO 1?", "O TEATRO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    nfil = 25 * clamp((t - C["09.a"] - 0.5) / 4.0)
    teatro(c, 560, 300, aa, nfil)
    if aa > 0:
        pill(c, "1ª fileira: 20", 120, 300, PURPLE, size=22, a=aa, bounds=(0, 1920))
        pill(c, "+2 por fileira", 120, 360, INK2, size=22, a=aa, bounds=(0, 1920))
        cad = sum(20 + 2 * k for k in range(int(nfil)))
        rrect(c, 1080, 220, 560, 110, 22, "#10141A", aa)
        text(c, "CADEIRAS", 1180, 262, 22, "black", "#9AA3B2", aa, align="left")
        ftext(c, f"{cad:,}".replace(",", " ") if t < C["09.c"] else "1 100", 1610, 300, 54, "black", "#FFD166", aa,
              align="right")
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 1080, 370, 560, 170, 22, "#FFFFFF", ab, shadow=True)
        text(c, "ÚLTIMA FILEIRA (25ª)", 1360, 415, 24, "black", AMBER, ab)
        linha(c, [("20 + 24 · 2 = ", INK), ("68", PURPLE)], 1360, 485, 46, ab)
        pill(c, "24 saltos = n − 1", 1360, 560, AMBER, size=22, a=ep(t, C["09.b"] + 2.0, 0.4), anchor="center")
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rrect(c, 1080, 610, 560, 190, 22, mix("#FFFFFF", GREEN, 0.10), acc)
        linha(c, [("média: (20 + 68) ÷ 2 = ", INK), ("44", PURPLE)], 1360, 660, 34, acc)
        linha(c, [("44 · 25 = ", INK), ("1 100", GREEN)], 1360, 745, 56, ep(t, C["09.c"] + 2.0, 0.4))


# ======================================================================
# bloco e — somas para decorar
# ======================================================================

def b_decorar(c, t, C, B):
    head(c, t, B["start"], "VALE A PENA DECORAR", "DUAS SOMAS PRONTAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        K.boxed(c, 220, 220, 700, 420, PURPLE, aa, 0.06)
        text(c, "OS n PRIMEIROS NATURAIS", 570, 280, 30, "black", PURPLE, aa)
        linha(c, [("1 + 2 + … + n", INK)], 570, 370, 44, aa)
        K.expr(c, "= n(n+1)/2", 570, 480, 60, aa)
        pill(c, "o Gauss em uma linha", 570, 590, INK2, size=24, a=aa, anchor="center")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        K.boxed(c, 1000, 220, 700, 420, TEAL, ab, 0.06)
        text(c, "OS n PRIMEIROS ÍMPARES", 1350, 280, 30, "black", TEAL, ab)
        linha(c, [("1 + 3 + 5 + …", INK)], 1350, 370, 44, ab)
        K.expr(c, "= n^2", 1350, 480, 72, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        # quadrados crescendo: 1, 4, 9
        for k, n in enumerate((1, 2, 3)):
            ak = ep(t, C["10.c"] + k * 1.0, 0.4)
            x0 = 1060 + k * 180
            for i in range(n):
                for j in range(n):
                    rrect(c, x0 + i * 30, 620 + j * 30 + 70, 27, 27, 4, TEAL, ak * (0.5 if (i == n - 1 or j == n - 1) else 1))
            text(c, str(n * n), x0 + n * 15, 820, 30, "black", INK, ak)
        linha(c, [("10 primeiros ímpares = ", INK), ("100", GREEN)], 570, 760, 40, ep(t, C["10.c"] + 3.6, 0.4))


# ======================================================================
# bloco f — termos equidistantes
# ======================================================================

VAL_F = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]


def b_equidist(c, t, C, B):
    head(c, t, B["start"], "SEM O 1º E O ÚLTIMO?", "TERMOS EQUIDISTANTES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 205, 1400, 90, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "EQUIDISTANTES: à mesma distância das pontas", W / 2, 262, 34, "black", BLUE, aa)
    ab = ep(t, C["11.b"], 0.5)
    xs = fila_pa(c, VAL_F, 310, 560, ab, passo=118, col=BLUE, size=30, w=92)
    if ab > 0:
        for k, x in enumerate(xs):
            ftext(c, "a" + sub(k + 1), x, 625, 24, "bold", GRAY, ab)
        arco(c, xs[0], xs[11], 520, 270, PURPLE, ep(t, C["11.b"] + 0.5, 0.4), 5, "3 + 25 = 28", 24)
        arco(c, xs[1], xs[10], 520, 120, GREEN, ep(t, C["11.b"] + 2.0, 0.4), 5, "5 + 23 = 28", 24)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        K.atalho(c, 260, 660, 640, 150, "ATALHO", ["índices somam n + 1:  2 + 11 = 13"], acc, 30)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        rrect(c, 960, 660, 700, 150, 22, "#FFFFFF", ad, shadow=True)
        linha(c, [("S = 28 · 12 ÷ 2 = ", INK), ("168", GREEN)], 1310, 735, 46, ad)


# ======================================================================
# bloco g — o termo médio · bloco h — o SAC
# ======================================================================

def b_medio(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O TERMO MÉDIO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 205, 1400, 90, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "TERMO MÉDIO: o que fica no meio da fila (quantidade ímpar)", W / 2, 262, 32, "black", BLUE, aa)
    ab = ep(t, C["12.b"], 0.5)
    K.atalho(c, 360, 330, 1200, 130, "ATALHO", ["o termo do meio JÁ É a média dos extremos"], ab, 38)
    acc = ep(t, C["12.c"], 0.5)
    xs = fila_pa(c, [8, 11, 14, 17, 20], 720, 580, acc, passo=120, col=BLUE, size=34, w=96)
    if acc > 0:
        ficha(c, "14", xs[2], 580, ep(t, C["12.c"] + 1.8, 0.4), GREEN, w=96, size=34, fill=mix("#FFFFFF", GREEN, 0.15))
        linha(c, [("5 · 14 = ", INK), ("70", GREEN)], W / 2, 720, 64, ep(t, C["12.c"] + 3.0, 0.4))
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "sem somar nada", W / 2, 810, GREEN, size=28, a=ad, anchor="center")


def b_sac(c, t, C, B):
    head(c, t, B["start"], "VOCÊ JÁ USOU ISSO", "DISFARÇADO: OS JUROS DO SAC", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        pill(c, "série de Empréstimos · juros do SAC", W / 2, 230, INK2, size=26, a=aa, anchor="center")
        vals = [400, 320, 240, 160, 80]
        for k, v in enumerate(vals):
            ak = ep(t, C["13.a"] + 1.4 + k * 0.6, 0.4)
            x = 520 + k * 220
            h = v * 0.7
            rrect(c, x - 60, 600 - h, 120, h, 10, PURPLE, ak * 0.85)
            text(c, str(v), x, 600 - h - 16, 30, "black", INK, ak)
        line(c, 400, 600, 1520, 600, INK2, aa, 3)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        linha(c, [("(400 + 80) · 5 ÷ 2 = ", INK), ("1 200", GREEN)], W / 2, 690, 52, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 790, acc, "ERA A SOMA DE GAUSS", PURPLE, -3, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "ÚLTIMO TERMO PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 210, 1400, 120, 24, "#FFFFFF", aa, shadow=True)
        linha(c, [("(5, 8, 11, …)", BLUE), ("   ·   ", INK2), ("S₂₀", PURPLE), (" = ?", AMBER)], W / 2, 270, 56, aa)
    if t < C["15"]:
        pause_timer(c, t, C["14.end"] - 1.9, 960, 560)
        return
    ab = ep(t, C["15.a"], 0.5)
    if ab > 0:
        rrect(c, 260, 380, 680, 230, 24, "#FFFFFF", ab, shadow=True)
        text(c, "1º · O ÚLTIMO TERMO", 600, 425, 26, "black", AMBER, ab)
        linha(c, [("a₂₀ = 5 + 19 · 3", INK)], 600, 500, 42, ab)
        linha(c, [("= 5 + 57 = ", INK), ("62", PURPLE)], 600, 570, 42, ep(t, C["15.a"] + 2.6, 0.4))
    acc = ep(t, C["15.b"], 0.5)
    if acc > 0:
        rrect(c, 980, 380, 680, 230, 24, "#FFFFFF", acc, shadow=True)
        text(c, "2º · A SOMA", 1320, 425, 26, "black", PURPLE, acc)
        linha(c, [("(5 + 62) · 20 ÷ 2", INK)], 1320, 500, 42, acc)
        linha(c, [("= 67 · 20 ÷ 2", INK)], 1320, 570, 42, ep(t, C["15.b"] + 1.6, 0.4))
    ad = ep(t, C["15.c"], 0.5)
    if ad > 0:
        rrect(c, 560, 650, 800, 150, 24, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("67 · 10 = ", INK), ("670", GREEN)], W / 2, 725, 64, ad)
        pill(c, "a metade antes: 20 → 10", 1360, 650, GREEN, size=22, a=ad, anchor="right", bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Primeiro com último: todos os pares dão a mesma soma.",
          "Soma é número de termos vezes a média dos extremos.",
          "“No 12º” é termo; “em 12” ou “ao todo” é soma."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Esquecer o ÷ 2: 67 · 20 = 1 340", "você juntou os extremos e multiplicou pelos termos",
          "assim somou a fila DUAS vezes (as duas escadas): S = 670"),
         ("Responder o termo quando pedem a soma: 62 no lugar de 670", "as duas contas aparecem, e as duas estão nas alternativas",
          "sublinhe a palavra: “no 20º” é termo; “ao todo” é soma"),
         ("Último termo com n saltos: 5 + 20 · 3 = 65, e S = 700", "são 20 termos, então parecem 20 saltos",
          "do 1º ao 20º são 19 saltos: sempre n − 1")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19"], ERROS)


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


def _questao(c, t, C, sid_q, sid_r, sid_x, alts, okL, xs, txt, pausa=True):
    a0 = ep(t, C[f"{sid_q}.a"], 0.4)
    yend = _enunciado(c, [(txt, INK)], a0, 236, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[sid_r], 0.3)),
         align="left")
    cues_in = {L: C[f"{sid_q}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in xs}
    K.alternativas(c, t, C, alts, 1000, 260, 680, 38, C[f"{sid_r}.ok"], okL, cues_in, cues_x, gap=34)
    if t < C[sid_r]:
        if pausa:
            pause_timer(c, t, C[f"{sid_q}.end"] - 1.9, 540, yend + 120)
        return None
    y0 = 236 - 30
    _painel(c, y0, ep(t, C[sid_r], 0.4))
    return y0


ALTS3 = [("A", "1 100", "", GREEN), ("B", "1 125", "um salto a mais: 70", RED), ("C", "1 150", "500 + 650", RED),
         ("D", "1 700", "todas com 68", RED), ("E", "2 200", "sem ÷ 2", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "AS FILEIRAS DO TEATRO", BLUE)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "20", "21", "22", ALTS3, "A", "BCDE",
                  "Um teatro tem 25 fileiras de cadeiras. A primeira fileira tem 20 cadeiras e cada fileira seguinte tem "
                  "2 cadeiras a mais que a anterior. O número total de cadeiras do teatro é")
    if y0 is None:
        return
    aa = ep(t, C["21.a"], 0.4)
    if aa > 0:
        linha(c, [("“total” → ", INK), ("SOMA", PURPLE)], 540, y0 + 60, 36, aa)
    ab = ep(t, C["21.b"], 0.4)
    if ab > 0:
        linha(c, [("a₂₅ = 20 + 24 · 2 = ", INK), ("68", PURPLE)], 540, y0 + 150, 36, ab)
    acc = ep(t, C["21.c"], 0.4)
    if acc > 0:
        linha(c, [("(20 + 68) ÷ 2 = ", INK), ("44", PURPLE)], 540, y0 + 240, 36, acc)
        linha(c, [("44 · 25 = ", INK), ("1 100", GREEN)], 540, y0 + 320, 48, ep(t, C["21.c"] + 2.6, 0.4))
    ad = ep(t, C["21.d"], 0.4)
    if ad > 0:
        check_icon(c, 250, y0 + 420, 20, ad, GREEN)
        linha(c, [("fileira do meio: 44 cadeiras · bate", GREEN)], 290, y0 + 422, 26, ad, align="left")


ALTS8 = [("A", "45", "esqueceu o 1º termo", RED), ("B", "57", "", GREEN), ("C", "60", "12 saltos: último = 8", RED),
         ("D", "90", "7,5 todos os dias", RED), ("E", "114", "sem ÷ 2", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · NÓS FAZEMOS", "A DISTÂNCIA ACUMULADA", PURPLE)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "23", "24", "25", ALTS8, "B", "ACDE",
                  "Um atleta iniciante correu 2 km no primeiro dia de treino e, a cada dia seguinte, correu 0,5 km a mais "
                  "que no dia anterior. Ao fim dos 12 primeiros dias de treino, a distância total percorrida por ele, "
                  "em quilômetros, foi")
    if y0 is None:
        return
    aa = ep(t, C["24.a"], 0.4)
    if aa > 0:
        linha(c, [("“ao fim dos 12 dias” → ", INK), ("SOMA", PURPLE)], 540, y0 + 60, 32, aa)
    ab = ep(t, C["24.b"], 0.4)
    if ab > 0:
        linha(c, [("a₁₂ = 2 + 11 · 0,5 = ", INK), ("7,5 km", PURPLE)], 540, y0 + 150, 34, ab)
    acc = ep(t, C["24.c"], 0.4)
    if acc > 0:
        linha(c, [("(2 + 7,5) · 12 ÷ 2", INK)], 540, y0 + 240, 36, acc)
        linha(c, [("= 9,5 · 6 = ", INK), ("57 km", GREEN)], 540, y0 + 320, 46, ep(t, C["24.c"] + 3.0, 0.4))
        pill(c, "a metade antes: 12 → 6", 540, y0 + 410, GREEN, size=22, a=ep(t, C["24.c"] + 3.0, 0.4), anchor="center")


ALTS9 = [("A", "250", "÷ 2 duas vezes", RED), ("B", "450", "18 termos", RED), ("C", "475", "19 termos", RED),
         ("D", "500", "", GREEN), ("E", "1 000", "sem ÷ 2", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "TERMOS EQUIDISTANTES", GREEN)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "26", "27", "28", ALTS9, "D", "ABCE",
                  "Em uma progressão aritmética de 20 termos, a soma do 3º com o 18º termo é igual a 50. A soma de todos "
                  "os 20 termos dessa progressão é")
    if y0 is None:
        return
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        linha(c, [("3 + 18 = ", INK), ("21", PURPLE), ("   ·   1 + 20 = ", INK), ("21", PURPLE)], 540, y0 + 60, 32, aa)
        pill(c, "EQUIDISTANTES", 540, y0 + 115, BLUE, size=22, a=ep(t, C["27.a"] + 2.6, 0.4), anchor="center")
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        linha(c, [("a₁ + a₂₀ = ", INK), ("50", PURPLE)], 540, y0 + 200, 40, ab)
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        linha(c, [("50 · 20 ÷ 2 = 50 · 10 = ", INK), ("500", GREEN)], 540, y0 + 300, 38, acc)
    ad = ep(t, C["27.d"], 0.4)
    if ad > 0:
        pill(c, "sem achar a₁ · sem achar r", 540, y0 + 400, GREEN, size=24, a=ad, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A PA DISFARÇADA", PURPLE)
    itens = [("JUROS SIMPLES", "1 030 · 1 060 · 1 090 …"), ("CALENDÁRIO", "dia 3 · 10 · 17 · 24 …"),
             ("FINANCIAMENTO", "juros caindo em escada")]
    aa = ep(t, C["30.a"], 0.5)
    for k, (tit, sub) in enumerate(itens):
        ak = aa * ep(t, C["30.a"] + k * 0.8, 0.4)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 260, 460, 260, 26, "#FFFFFF", ak, shadow=True)
        text(c, tit, x, 350, 36, "black", PURPLE, ak)
        text(c, sub, x, 420, 26, "bold", INK2, ak)
        selo(c, x, 490, ak, "É PA?", AMBER, -4, 24)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        pill(c, "você já esbarrou nela em outras séries", W / 2, 620, INK2, size=28, a=ab, anchor="center")
    pill(c, "ep. 4 · a PA disfarçada", W / 2, 730, PURPLE, size=32, a=ep(t, C["30.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Você conseguiria somar de 1 a 100 antes do Gauss?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, gauss=b_gauss, escadas=b_escadas, formula=b_formula,
              metade=b_metade, teatro=b_teatro, decorar=b_decorar, equidist=b_equidist, medio=b_medio, sac=b_sac,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q3=b_q3, q8=b_q8, q9=b_q9, ponte=b_ponte, cta=b_cta)
