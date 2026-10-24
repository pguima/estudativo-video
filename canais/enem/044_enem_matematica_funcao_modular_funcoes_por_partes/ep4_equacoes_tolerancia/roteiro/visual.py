"""Visual — Função Modular e Funções por Partes, Episódio 4: equações e inequações modulares e tolerância (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo...).
Peças deste episódio: reta() (reta numérica com marcas), elastico() (o ALFINETE no centro e o ELÁSTICO que estica o
raio para cada lado, com bolinhas cheias ou vazias nas pontas), fora() (as duas semirretas acesas e o meio apagado),
dois_pontos() (os dois valores a mesma distância do zero), ciclovia() (o ciclista do km 0 ao km 24, o posto no km 12 e
o medidor de distância até o posto), bike(), linha(), caixa(), casos().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum044", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_modular_ep4_equacoes_tolerancia.mp4"
CARD_R = K.CARD_R
APAGADO = "#C9CED8"


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


def caixa(c, cx, cy, tit, val, col, a, w=360, h=140, size=44):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 33, 24, "black", col, a)
    while text_w(val, "black", size) > w - 30:
        size -= 2
    text_mid(c, val, cx, cy + 22, size, "black", INK, a)


def _X(x0, x1, vmin, vmax):
    return lambda v: x0 + (x1 - x0) * (v - vmin) / (vmax - vmin)


def reta(c, x0, x1, y, vmin, vmax, a, marcas=(), size=30, col=None, sub=None):
    """reta numérica: marcas = valores com tracinho e número (sub = texto embaixo de cada marca, opcional)"""
    if a <= 0:
        return
    X = _X(x0, x1, vmin, vmax)
    line(c, x0 - 30, y, x1 + 30, y, col or INK2, a, 4)
    path = skia.Path(); path.moveTo(x1 + 44, y); path.lineTo(x1 + 24, y - 12); path.lineTo(x1 + 24, y + 12); path.close()
    c.drawPath(path, paint(col or INK2, a))
    for v in marcas:
        line(c, X(v), y - 14, X(v), y + 14, INK2, a, 3)
        s = f"{v}".replace("-", "−")
        if sub:
            s = s + sub
        text(c, s, X(v), y + 56, size, "black", INK2, a)


def bolinha(c, x, y, a, col, cheia=True, r=14):
    if a <= 0:
        return
    if cheia:
        c.drawCircle(x, y, r, paint(col, a))
    else:
        c.drawCircle(x, y, r, paint("#FFFFFF", a))
        c.drawCircle(x, y, r, paint(col, a, stroke=4))


def elastico(c, x0, x1, y, vmin, vmax, centro, raio, a, u=1.0, cheia=True, col=None, rot_c="", rot_r="",
             pontas=True):
    """o alfinete no centro e o elástico que estica 'raio' para cada lado (u de 0 a 1 = quanto já esticou)"""
    if a <= 0:
        return
    col = col or GREEN
    X = _X(x0, x1, vmin, vmax)
    uu = ease_io(clamp(u))
    xa, xb = X(centro - raio * uu), X(centro + raio * uu)
    if uu > 0:
        rrect(c, xa, y - 9, xb - xa, 18, 9, col, a * 0.85)
    # alfinete
    line(c, X(centro), y - 70, X(centro), y, INK, a, 4)
    c.drawCircle(X(centro), y - 78, 14, paint(RED, a))
    if rot_c:
        text(c, rot_c, X(centro), y - 110, 28, "black", INK, a)
    if pontas and uu > 0.98:
        bolinha(c, xa, y, a, col, cheia)
        bolinha(c, xb, y, a, col, cheia)
    if rot_r and uu > 0.3:
        for xx0, xx1 in ((xa, X(centro)), (X(centro), xb)):
            text(c, rot_r, (xx0 + xx1) / 2, y - 26, 26, "black", col, a * clamp((uu - 0.3) / 0.4))


def fora(c, x0, x1, y, vmin, vmax, k, a, col=None, cheia=False):
    """|x| > k: o meio (de −k a k) apagado e as duas semirretas acesas"""
    if a <= 0:
        return
    col = col or PURPLE
    X = _X(x0, x1, vmin, vmax)
    rrect(c, X(-k), y - 7, X(k) - X(-k), 14, 7, APAGADO, a)
    rrect(c, x0 - 30, y - 9, X(-k) - x0 + 30, 18, 9, col, a * 0.85)
    rrect(c, X(k), y - 9, x1 + 30 - X(k), 18, 9, col, a * 0.85)
    bolinha(c, X(-k), y, a, col, cheia)
    bolinha(c, X(k), y, a, col, cheia)


def dois_pontos(c, x0, x1, y, vmin, vmax, k, a, u=1.0, col=None):
    """os dois valores à mesma distância do zero: setas do 0 até k e até −k"""
    if a <= 0:
        return
    col = col or BLUE
    X = _X(x0, x1, vmin, vmax)
    uu = ease_io(clamp(u))
    for s in (1, -1):
        xe = X(0) + (X(s * k) - X(0)) * uu
        line(c, X(0), y - 40, xe, y - 40, col, a, 5)
        if uu > 0.95:
            c.drawCircle(X(s * k), y, 16, paint(col, a))
            text(c, f"{k}" if s > 0 else f"−{k}", X(s * k), y - 70, 40, "black", col, a)
    c.drawCircle(X(0), y, 10, paint(INK, a))


def bike(c, x, y, a, col=None, s=1.0):
    """um ciclista estilizado (duas rodas, quadro e cabeça), apoiado no ponto (x, y)"""
    if a <= 0:
        return
    col = col or BLUE
    r = 20 * s
    for dx in (-26 * s, 26 * s):
        c.drawCircle(x + dx, y - r, r, paint(col, a, stroke=5))
    line(c, x - 26 * s, y - r, x, y - r - 30 * s, col, a, 5)
    line(c, x, y - r - 30 * s, x + 26 * s, y - r, col, a, 5)
    line(c, x - 6 * s, y - r - 34 * s, x + 4 * s, y - r - 62 * s, col, a, 5)
    c.drawCircle(x + 8 * s, y - r - 76 * s, 12 * s, paint(col, a))


def ciclovia(c, x0, x1, y, a, km=None, medidor=0.0, fantasmas=(), posto_a=1.0):
    """a ciclovia do km 0 ao km 24, o posto no km 12 e (opcional) o ciclista no km 'km' com o medidor de distância"""
    if a <= 0:
        return
    X = _X(x0, x1, 0, 24)
    rrect(c, x0 - 20, y - 12, x1 - x0 + 40, 24, 12, "#E7EBF2", a)
    for v in (0, 4, 8, 12, 16, 20, 24):
        line(c, X(v), y - 14, X(v), y + 14, INK2, a, 3)
        text(c, f"km {v}", X(v), y + 56, 26, "black", INK2, a)
    ap = a * posto_a
    rrect(c, X(12) - 46, y - 214, 92, 70, 14, AMBER, ap)
    text_mid(c, "POSTO", X(12), y - 179, 22, "black", "#FFFFFF", ap)
    line(c, X(12), y - 144, X(12), y - 14, AMBER, ap, 5)
    for kk, col, lab in fantasmas:
        bike(c, X(kk), y - 14, a * 0.9, col)
        if lab:
            pill(c, lab, X(kk), y - 160, col, size=24, a=a, anchor="center", bounds=(0, 1920))
    if km is not None:
        bike(c, X(km), y - 14, a, BLUE)
        am = a * clamp(medidor)
        if am > 0:
            d = abs(km - 12)
            if d > 0.05:
                line(c, X(min(km, 12)), y + 100, X(max(km, 12)), y + 100, RED, am, 5)
            caixa(c, X(km), y + 190, "DISTÂNCIA ATÉ O POSTO", f"{d:.0f} km" if abs(d - round(d)) < 0.05 else f"{d:.1f} km",
                  RED, am, 320, 120, 46)


def casos(c, x, y, w, a1, a2, s1, s2, r1, r2, size=34):
    """os dois casos lado a lado (positivo em cima, negativo embaixo), cada um com o resultado em destaque"""
    for k, (aa, s, r, col) in enumerate(((a1, s1, r1, BLUE), (a2, s2, r2, PURPLE))):
        if aa <= 0:
            continue
        yy = y + k * 150
        rrect(c, x, yy, w, 126, 20, mix("#FFFFFF", col, 0.08), aa, shadow=True)
        text(c, "CASO POSITIVO" if k == 0 else "CASO NEGATIVO", x + 26, yy + 36, 22, "black", col, aa, align="left")
        text(c, s, x + 26, yy + 92, size, "black", INK, aa, align="left")
        if r:
            pill(c, r, x + w - 24, yy + 76, col, size=size - 4, a=aa, anchor="right", bounds=(0, 1920))


def _enunciado(c, s, a, y0=240, size=27, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 11
    return y + 8


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EQUAÇÕES COM MÓDULO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    fant = []
    if ab > 0:
        fant = [(8, BLUE, "AINDA VAI CHEGAR?"), (16, PURPLE, "JÁ PASSOU?")]
    ciclovia(c, 260, 1660, 600, aa, km=None if ab > 0 else 8, medidor=0, fantasmas=fant)
    X = _X(260, 1660, 0, 24)
    if aa > 0:
        for kk in ((8,) if ab <= 0 else (8, 16)):
            line(c, X(min(kk, 12)), 690, X(max(kk, 12)), 690, RED, aa, 5)
            text(c, "4 km", (X(kk) + X(12)) / 2, 740, 34, "black", RED, aa)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        regra(c, "as duas coisas podem ser verdade, em horários diferentes", W / 2, 300, acc, 36, BLUE)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 815, ad, "QUEM ESQUECE UMA DELAS ERRA", AMBER, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "resolver equações e inequações com módulo DESENHANDO A RETA", GREEN),
             ("02.b", "traduzir qualquer TOLERÂNCIA em intervalo", PURPLE)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 220 + d
        rrect(c, 220, y, 1480, 160, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
        check_icon(c, 300, y + 80, 30, a, col)
        sz = 44
        while text_w(s, "black", sz) > 1300:
            sz -= 2
        text_mid(c, s, 360, y + 80, sz, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "2 LEMBRETES", "RÁPIDOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 200, 280 + d1, 720, 460, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "EPISÓDIO 3", 560, 330 + d1, GREEN, size=26, a=a1, anchor="center", bounds=(0, 1920))
        text_mid(c, "módulo = distância até o 0", 560, 440 + d1, 40, "black", BLUE, a1)
        reta(c, 300, 820, 600 + d1, -8, 8, a1, marcas=(-7, 0, 7), size=28)
        X = _X(300, 820, -8, 8)
        line(c, X(-7), 560 + d1, X(0), 560 + d1, BLUE, a1, 5)
        text(c, "|−7| = 7", X(-3.5), 540 + d1, 34, "black", BLUE, a1)
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 280 + d2, 720, 460, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "EQUAÇÕES DO 1º GRAU", 1360, 330 + d2, GREEN, size=26, a=a2, anchor="center", bounds=(0, 1920))
        for k, (s, col) in enumerate((("2x − 5 = 7", INK), ("2x = 12", INK2), ("x = 6", GREEN))):
            text_mid(c, s, 1360, 450 + k * 95 + d2, 54, "black", col, a2)


# ======================================================================
# concreto, termos, regra
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "A QUE DISTÂNCIA DO CERTO?", "TOLERÂNCIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    caixa(c, 560, 340, "CAFÉ", "500 g · tolerância de 8 g", BLUE, aa, 640, 150, 42)
    ab = ep(t, C["04.b"], 0.5)
    caixa(c, 1360, 340, "PEÇA", "50 mm · pode variar 2 mm", BLUE, ab, 640, 150, 42)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        text_mid(c, "a que DISTÂNCIA do valor certo você pode estar?", W / 2, 560, 46, "black", INK, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        text_mid(c, "| distância |", W / 2, 720, 110, "black", PURPLE, ad)


def b_termos(c, t, C, B):
    head(c, t, B["start"], "EQUAÇÃO MODULAR", "DEFINIÇÕES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        rrect(c, 200, 230, 1520, 130, 24, mix("#FFFFFF", BLUE, 0.08), aa, shadow=True)
        text(c, "EQUAÇÃO MODULAR", 260, 278, 26, "black", BLUE, aa, align="left")
        text_mid(c, "igualdade com o x dentro das barrinhas:  |x| = 7", 260, 325, 40, "black", INK, aa, align="left")
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        rrect(c, 200, 390, 1520, 120, 24, mix("#FFFFFF", BLUE, 0.08), ab, shadow=True)
        text(c, "CONJUNTO SOLUÇÃO", 260, 436, 26, "black", BLUE, ab, align="left")
        text_mid(c, "a lista de TODOS os x que funcionam", 260, 478, 40, "black", INK, ab, align="left")
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        reta(c, 360, 1560, 740, -9, 9, acc, marcas=(-7, 0, 7), size=30)
        dois_pontos(c, 360, 1560, 740, -9, 9, 7, acc, u=ep(t, C["05.c"] + 0.8, 1.2))
        text(c, "distância 7 → no 7 ou no −7", W / 2, 600, 32, "black", BLUE, acc * ep(t, C["05.c"] + 2.0, 0.5))


def b_regra(c, t, C, B):
    head(c, t, B["start"], "A REGRA", "|A| = k", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 240, 1400, 230, 26, mix("#FFFFFF", PURPLE, 0.08), aa, shadow=True)
        text(c, "com k positivo", W / 2, 290, 28, "bold", GRAY, aa)
        linha(c, [("|A| = k   ⇔   ", INK), ("A = k", BLUE), ("   ou   ", INK2), ("A = −k", PURPLE)], W / 2, 365, 64, aa)
        text(c, "caso positivo", 1050, 445, 26, "black", BLUE, aa)
        text(c, "caso negativo", 1410, 445, 26, "black", PURPLE, aa)
    ab = ep(t, C["06.b"], 0.5)
    caixa(c, 560, 650, "SE k = 0", "só A = 0", BLUE, ab, 600, 170, 52)
    acc = ep(t, C["06.c"], 0.5)
    caixa(c, 1360, 650, "SE k < 0", "sem solução", RED, acc, 600, 170, 52)
    if acc > 0:
        text(c, "distância nunca é negativa", 1360, 790, 28, "black", RED, acc)


# ======================================================================
# blocos b, c, d — equações
# ======================================================================

def b_exemplo(c, t, C, B):
    head(c, t, B["start"], "|2x − 5| = 7", "OS DOIS CASOS", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["07.t"], 0.5)
    if a0 > 0:
        text_mid(c, "|2x − 5| = 7", W / 2, 260, 66, "black", INK, a0)
    casos(c, 220, 330, 900, ep(t, C["07.a"], 0.5), ep(t, C["07.b"], 0.5), "2x − 5 = 7  →  2x = 12",
          "2x − 5 = −7  →  2x = −2", "x = 6", "x = −1", 36)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 220, 650, 900, 150, 20, "#FFFFFF", acc, shadow=True)
        text(c, "CONFERÊNCIA", 250, 690, 22, "black", GREEN, acc, align="left")
        linha(c, [("|12 − 5| = 7 ", INK), ("✓", GREEN), ("     |−2 − 5| = |−7| = 7 ", INK), ("✓", GREEN)], 670, 750,
              34, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1200, 330, 500, 470, "ATALHO", ["DOIS CASOS", "e substitua", "os dois na", "equação original"],
                 ad, 38)


def b_dois_mod(c, t, C, B):
    head(c, t, B["start"], "MÓDULO IGUAL A MÓDULO", "LEIA COMO DISTÂNCIA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text_mid(c, "|x − 1| = |x − 7|", W / 2, 280, 70, "black", INK, aa)
    ab = ep(t, C["08.b"], 0.5)
    reta(c, 360, 1560, 640, 0, 8, ab, marcas=tuple(range(0, 9)), size=30)
    X = _X(360, 1560, 0, 8)
    if ab > 0:
        for v, col in ((1, BLUE), (7, PURPLE)):
            c.drawCircle(X(v), 640, 16, paint(col, ab))
        text(c, "x está à mesma distância do 1 e do 7", W / 2, 430, 36, "black", BLUE, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        for v0, v1 in ((1, 4), (4, 7)):
            line(c, X(v0), 580, X(v1), 580, GREEN, acc, 6)
            text(c, "3", (X(v0) + X(v1)) / 2, 560, 36, "black", GREEN, acc)
        c.drawCircle(X(4), 640, 20, paint(GREEN, acc))
        pill(c, "PONTO MÉDIO: x = 4", X(4), 780, GREEN, size=36, a=acc, anchor="center", bounds=(0, 1920))


def b_letra(c, t, C, B):
    head_seq(c, t, C, [("09", "LADO DIREITO COM LETRA", "|x − 2| = 2x − 1", AMBER),
                       ("10", "O OUTRO CASO", "CONFIRA SUBSTITUINDO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    text_mid(c, "|x − 2| = 2x − 1", W / 2, 260, 64, "black", INK, ep(t, C["09.a"], 0.5))
    a1 = ep(t, C["09.b"], 0.5)
    a2 = ep(t, C["10.a"], 0.5) if sid == "10" else 0
    casos(c, 220, 330, 960, a1, a2, "x − 2 = 2x − 1", "x − 2 = −2x + 1  →  3x = 3", "x = −1", "x = 1", 36)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        strike(c, 236, 420, 1160, 420, acc, RED, acc)
        if sid == "09":
            rrect(c, 220, 650, 960, 150, 20, mix("#FFFFFF", RED, 0.08), acc, shadow=True)
            linha(c, [("lado direito: 2 · (−1) − 1 = ", INK), ("−3", RED)], 700, 700, 36, acc)
            text(c, "módulo igual a negativo? impossível", 700, 770, 30, "black", RED, acc)
    if acc > 0:
        selo(c, 1440, 420, acc, "DESCARTE", RED, -6, 40)
    if sid != "10":
        return
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 220, 650, 960, 150, 20, "#FFFFFF", ab, shadow=True)
        text(c, "CONFERÊNCIA COM x = 1", 250, 690, 22, "black", GREEN, ab, align="left")
        linha(c, [("|1 − 2| = 1     2 · 1 − 1 = 1  ", INK), ("✓", GREEN)], 700, 750, 36, ab)
    ad = ep(t, C["10.c"], 0.5)
    if ad > 0:
        K.atalho(c, 1260, 540, 440, 290, "ATALHO", ["lado com letra:", "ZERO OU POSITIVO", "confira tudo"], ad, 32)


# ======================================================================
# blocos e, f — inequações e tolerância
# ======================================================================

def b_inequacao(c, t, C, B):
    head_seq(c, t, C, [("11", "|x| < 4", "FICA ENTRE", GREEN),
                       ("12", "|x| > 4", "FICA FORA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    x0, x1, y = 360, 1560, 640
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            rrect(c, 260, 230, 1400, 110, 22, mix("#FFFFFF", BLUE, 0.08), aa, shadow=True)
            text(c, "INEQUAÇÃO MODULAR", 300, 272, 24, "black", BLUE, aa, align="left")
            text_mid(c, "módulo com <, >, ≤ ou ≥ no lugar do =", 300, 312, 36, "black", INK, aa, align="left")
        ab = ep(t, C["11.b"], 0.5)
        reta(c, x0, x1, y, -6, 6, ab, marcas=(-4, 0, 4), size=32)
        cheia = t >= C["11.c"]
        elastico(c, x0, x1, y, -6, 6, 0, 4, ab, u=ep(t, C["11.b"] + 0.6, 1.4), cheia=cheia, col=GREEN, rot_r="< 4")
        if ab > 0:
            linha(c, [("−4 < x < 4", GREEN)], W / 2, 470, 54, ab)
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 760, 1400, 90, 18, mix("#FFFFFF", BLUE, 0.08), acc, shadow=True)
            text_mid(c, "INTERVALO FECHADO (≤): as pontas entram, bolinhas CHEIAS", W / 2, 805, 34, "black", BLUE, acc)
        return
    aa = ep(t, C["12.a"], 0.5)
    reta(c, x0, x1, y, -6, 6, aa, marcas=(-4, 0, 4), size=32)
    ab = ep(t, C["12.b"], 0.5)
    fora(c, x0, x1, y, -6, 6, 4, ab)
    if aa > 0:
        text(c, "a distância passa de 4", W / 2, 470, 36, "black", INK2, aa * (1 - ab))
    if ab > 0:
        linha(c, [("x < −4", PURPLE), ("   ou   ", INK2), ("x > 4", PURPLE)], W / 2, 470, 54, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        regra(c, "menor que fica ENTRE · maior que fica FORA", W / 2, 800, acc, 40, PURPLE)


def b_elastico(c, t, C, B):
    head(c, t, B["start"], "TOLERÂNCIA", "O ELÁSTICO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 230, 1400, 110, 22, mix("#FFFFFF", BLUE, 0.08), aa, shadow=True)
        linha(c, [("valor certo = ", INK), ("CENTRO", RED), ("   ·   tolerância = ", INK), ("RAIO", GREEN)], W / 2, 285,
              42, aa)
    ab = ep(t, C["13.b"], 0.5)
    reta(c, 360, 1560, 640, 44, 56, ab, marcas=(46, 48, 50, 52, 54), size=30)
    elastico(c, 360, 1560, 640, 44, 56, 50, 2, ab, u=ep(t, C["13.b"] + 0.6, 1.6), cheia=True, col=GREEN, rot_c="50 mm",
             rot_r="2 mm")
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        linha(c, [("|x − 50| ≤ 2", PURPLE)], W / 2, 430, 56, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        pill(c, "de 48 mm a 52 mm", W / 2, 800, GREEN, size=40, a=ad, anchor="center", bounds=(0, 1920))


def b_traducao(c, t, C, B):
    head(c, t, B["start"], "TRADUÇÃO DIRETA", "DO TEXTO PARA O MÓDULO", PURPLE)
    card(c, *CARD_R)
    rows = [("14.a", "\"difere de a em NO MÁXIMO k\"", "|x − a| ≤ k", "ENTRE", GREEN),
            ("14.b", "\"difere em MAIS DE k\"", "|x − a| > k", "FORA", PURPLE)]
    for k, (cue, frase, mod, onde, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 170 + d
        rrect(c, 200, y, 1520, 140, 22, mix("#FFFFFF", col, 0.08), a, shadow=True)
        text_mid(c, frase, 240, y + 70, 38, "black", INK, a, align="left")
        text_mid(c, mod, 1180, y + 70, 46, "black", col, a)
        pill(c, onde, 1620, y + 70, col, size=30, a=a, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 600, 1200, 220, "ATALHO", ["CENTRO − RAIO  até  CENTRO + RAIO", "com ≤, as pontas entram"],
                 acc, 40)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ · |3x − 6| = 9", "PAUSE E TENTE", GREEN),
                       ("16", "VAMOS JUNTOS", "OS DOIS CASOS", GREEN)])
    card(c, *CARD_R)
    if t < C["16"]:
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            text_mid(c, "|3x − 6| = 9", W / 2, 400, 110, "black", INK, aa)
        ab = ep(t, C["15.b"], 0.5)
        if ab > 0:
            text_mid(c, "os dois casos + a conferência", W / 2, 560, 44, "black", INK2, ab)
        pause_timer(c, t, C["15.end"] - 1.9, W / 2, 740)
        return
    casos(c, 220, 260, 1100, ep(t, C["16.a"], 0.5), ep(t, C["16.b"], 0.5), "3x − 6 = 9  →  3x = 15",
          "3x − 6 = −9  →  3x = −3", "x = 5", "x = −1", 38)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        rrect(c, 220, 580, 1100, 130, 20, "#FFFFFF", acc, shadow=True)
        linha(c, [("|15 − 6| = 9 ", INK), ("✓", GREEN), ("     |−3 − 6| = |−9| = 9 ", INK), ("✓", GREEN)], 770, 645,
              36, acc)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        caixa(c, 1520, 450, "SOLUÇÃO", "{−1, 5}", GREEN, ad, 340, 200, 70)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Módulo igual a k: o de dentro vale k ou −k.",
          "Menor que fica entre; maior que fica fora.",
          "Tolerância: centro mais ou menos o raio."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 62)


ERROS = [("|x| = 5  →  só x = 5", "5 é o número que está na conta",
          "o −5 também está a 5 do zero: são DOIS valores, {−5, 5}"),
         ("|x| = −3  →  x = ±3", "é a regra de sempre: k ou −k",
          "a regra pede k positivo; distância nunca é negativa: SEM SOLUÇÃO"),
         ("|x| < 4  →  \"x < ±4\"", "é a mesma ideia dos dois casos da equação",
          "menor que fica ENTRE: −4 < x < 4")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)


# ======================================================================
# questão 4 (eu faço), questão 2 (nós fazemos), questão 9 (você faz)
# ======================================================================

ALTS4 = [("A", "{6}", "esqueceu o caso negativo", RED), ("B", "{−6, 1}", "trocou os sinais", RED),
         ("C", "{−1, 6}", "", GREEN), ("D", "{1, 6}", "2x = 7 − 5", RED), ("E", "vazio", "confundiu com |A| = −7", RED)]

ALTS2 = [("A", "m ≤ 508", "só o limite de cima", RED), ("B", "492 < m < 508", "tirou as pontas", RED),
         ("C", "496 ≤ m ≤ 504", "dividiu o 8 por 2", RED), ("D", "492 ≤ m ≤ 508", "", GREEN),
         ("E", "m ≤ 492 ou m ≥ 508", "os de FORA", RED)]

ALTS9 = [("A", "somente em t = 2 h", "um caso só", RED), ("B", "somente em t = 4 h", "um caso só", RED),
         ("C", "em t = 2 h e em t = 3 h", "t = 3: distância zero", RED), ("D", "em t = 1 h e em t = 4 h", "4t = 4?", RED),
         ("E", "em t = 2 h e em t = 4 h", "", GREEN)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "EQUAÇÃO MODULAR", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, "Em um jogo de tabuleiro, a casa de um peão é dada por um número inteiro x, e uma regra exige "
                      "que |2x − 5| = 7. O conjunto de valores de x que cumprem a regra é", a0, size=30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 270, 680, 42, C["22.ok"], "C", cues_in, cues_x, gap=44)
    if t < C["22"]:
        return
    y0 = yend + 10
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["22"], 0.4), shadow=True)
    aa = ep(t, C["22.a"], 0.4)
    linha(c, [("2x − 5 = 7  →  ", INK), ("x = 6", BLUE)], 540, y0 + 60, 34, aa)
    linha(c, [("2x − 5 = −7  →  ", INK), ("x = −1", PURPLE)], 540, y0 + 125, 34, aa)
    linha(c, [("|12 − 5| = 7 ✓   |−2 − 5| = 7 ✓", GREEN)], 540, y0 + 200, 30, ep(t, C["22.b"], 0.4))


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "TOLERÂNCIA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    _enunciado(c, "Uma máquina embala pacotes de café com massa nominal de 500 g. O controle de qualidade aprova um "
               "pacote de massa m, em gramas, quando |m − 500| ≤ 8. Os pacotes aprovados são exatamente aqueles cuja "
               "massa satisfaz", a0, size=28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS2, 1000, 270, 680, 38, C["25.ok"], "D", cues_in, cues_x, gap=40)
    if t < C["25"]:
        pause_timer(c, t, C["24.end"] - 1.9, 540, 700)
        return
    a1 = ep(t, C["25"], 0.4)
    rrect(c, 170, 520, 740, 310, 18, "#FFFFFF", a1, shadow=True)
    reta(c, 240, 840, 720, 488, 512, a1, marcas=(492, 500, 508), size=24)
    elastico(c, 240, 840, 720, 488, 512, 500, 8, a1, u=ep(t, C["25.b"], 1.4), cheia=t >= C["25.c"], col=GREEN,
             rot_c="500 g", rot_r="8 g")
    if ep(t, C["25.c"], 0.4) > 0:
        text(c, "≤ : as pontas entram", 540, 815, 26, "black", GREEN, ep(t, C["25.c"], 0.4))


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "DISTÂNCIA AO LONGO DO TEMPO", BLUE)
    card(c, *CARD_R)
    if t < C["28"]:
        a0 = ep(t, C["27.a"], 0.4)
        _enunciado(c, "Um ciclista parte do km 0 de uma ciclovia retilínea e pedala no sentido crescente da "
                   "quilometragem a 4 km/h constantes. Um posto de apoio fica no km 12. A distância entre o ciclista "
                   "e o posto, em km, após t horas, é d(t) = |4t − 12|, para 0 ≤ t ≤ 6. Essa distância vale 4 km",
                   a0, size=27)
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
        cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
        K.alternativas(c, t, C, ALTS9, 1000, 270, 700, 36, 1e9, "E", cues_in, {}, gap=40)
        pause_timer(c, t, C["27.end"] - 2.4, 540, 740, dur=2.1)
        return
    if t < C["29"]:
        # a ciclovia: o ciclista anda de 0 a 24 km; o medidor desce até zero no posto e volta a subir
        a1 = ep(t, C["28"], 0.4)
        ta, tb = C["28.a"], C["28.b"]
        if t < tb:
            km = 4 * (1 + 3 * clamp((t - ta) / 2.5))
        else:
            km = 16 - 8 * clamp((t - tb) / 1.2)
        km = max(0.0, min(24.0, km))
        ciclovia(c, 300, 1620, 560, a1, km=km, medidor=a1)
        aa = ep(t, ta, 0.4)
        if aa > 0:
            linha(c, [("4t − 12 = 4  →  ", INK), ("t = 4 h", PURPLE), ("  (km 16: já passou)", INK2)], W / 2, 240, 36,
                  aa)
        ab = ep(t, tb, 0.4)
        if ab > 0:
            linha(c, [("4t − 12 = −4  →  ", INK), ("t = 2 h", BLUE), ("  (km 8: ainda vai chegar)", INK2)], W / 2, 300,
                  36, ab)
        aok = ep(t, C["28.ok"], 0.4)
        if aok > 0:
            pill(c, "LETRA E · t = 2 h e t = 4 h", W / 2, 880, GREEN, size=36, a=aok, anchor="center", bounds=(0, 1920))
        return
    # as erradas, sobre a ciclovia com os três instantes
    a1 = ep(t, C["29"], 0.4)
    X = _X(300, 1620, 0, 24)
    ciclovia(c, 300, 1620, 560, a1, fantasmas=[(8, BLUE, "t = 2 h · 4 km"), (16, PURPLE, "t = 4 h · 4 km")])
    axa = ep(t, C["29.xa"], 0.4)
    if axa > 0:
        selo(c, W / 2, 260, axa, "A e B: UM CASO SÓ", RED, -3, 34)
    axc = ep(t, C["29.xc"], 0.4)
    if axc > 0:
        bike(c, X(12), 546, axc, RED)
        pill(c, "t = 3 h · distância 0", X(12), 800, RED, size=28, a=axc, anchor="center", bounds=(0, 1920))
    axd = ep(t, C["29.xd"], 0.4)
    if axd > 0:
        rrect(c, 1180, 720, 560, 110, 18, mix("#FFFFFF", RED, 0.08), axd, shadow=True)
        linha(c, [("D: 4t = 4?  o certo é ", INK), ("4t = 8", GREEN)], 1460, 775, 30, axd)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    for k, (s, col) in enumerate((("TARIFAS", BLUE), ("FAIXAS PROGRESSIVAS", GREEN), ("MÓDULO", PURPLE))):
        a = aa * ep(t, C["31.a"] + 0.6 * k, 0.4)
        if a > 0:
            rrect(c, 200 + k * 520, 320, 480, 220, 26, mix("#FFFFFF", col, 0.10), a, shadow=True)
            sz = 46
            while text_w(s, "black", sz) > 440:
                sz -= 2
            text_mid(c, s, 440 + k * 520, 430, sz, "black", col, a)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 720, ab, "PEGADINHAS + TREINO PARA O ENEM", AMBER, -3, 40)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "|x − 3| ≤ 5: de onde até onde vai o x?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, termos=b_termos, regra=b_regra,
              exemplo=b_exemplo, dois_mod=b_dois_mod, letra=b_letra, inequacao=b_inequacao, elastico=b_elastico,
              traducao=b_traducao, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q2=b_q2, q9=b_q9,
              ponte=b_ponte, cta=b_cta)
