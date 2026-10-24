"""Visual — Equação do 2º Grau e Bhaskara, Episódio 3: soma e produto (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: cartas() (o jogo dos dois números: duas cartas com "?" que viram e mostram os números, com as pistas
"soma" e "produto" em cima), reta_sinais() (a reta com o zero e as duas raízes como bolinhas), semaforo() (as três
lâmpadas do produto e da soma), voo() (a trajetória da bola com a faixa dos 15 m, SEM marcar a altura máxima) e
linha_tempo() (0 a 4 s com os instantes 1 s e 3 s e o trecho acima de 15 m).
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
_s = importlib.util.spec_from_file_location("comum036", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                 K.selo, K.pause_timer)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_2grau_ep3_soma_produto.mp4"
CARD_R = K.CARD_R
VERSO = "#2F4A7A"
CEU = "#EAF3FB"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]"""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        x += w_


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def cartas(c, cx, cy, vals, flips, a, w=190, h=260, gap=70, pistas=None, a_pistas=(0, 0), size=None, pdx=440, psize=34):
    """o jogo dos dois números. vals = ('2', '5'); flips = (0→1, 0→1) a virada de cada carta;
    pistas = ('soma 7', 'produto 10') em pílulas acima das cartas."""
    if a <= 0:
        return
    size = size or h * 0.42
    for k, v in enumerate(vals):
        x = cx + (k - 0.5) * (w + gap)
        f = clamp(flips[k])
        sx = abs(math.cos(math.pi * f))
        ww = max(6.0, w * sx)
        frente = f >= 0.5
        cor = "#FFFFFF" if frente else VERSO
        rrect(c, x - ww / 2, cy - h / 2, ww, h, 22, cor, a, shadow=True)
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - ww / 2, cy - h / 2, ww, h), 22, 22)
        c.drawRRect(rr, paint(GREEN if frente else "#1E3357", a, stroke=5))
        if sx > 0.25:
            c.save(); c.translate(x, cy); c.scale(sx, 1.0)
            if frente:
                expr(c, v, 0, 0, size, a, cores={0: GREEN})
            else:
                fmid(c, "?", 0, 0, size * 1.1, "black", "#FFFFFF", a)
            c.restore()
    if pistas:
        for k, (s_, ap) in enumerate(zip(pistas, a_pistas)):
            if ap > 0:
                pill(c, s_, cx + (k - 0.5) * pdx, cy - h / 2 - 60, PURPLE if k else BLUE, size=psize, a=a * ap,
                     anchor="center")


def reta_sinais(c, x0, x1, y, pts, a, rng=(-6, 6), cor=GREEN, rotulos=True, size=26):
    """reta numérica com o zero destacado e as raízes (pts) como bolinhas"""
    if a <= 0:
        return
    lo, hi = rng
    X = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    arrow(c, x0 - 20, y, x1 + 30, y, INK2, a, 4, 14)
    for v in range(lo, hi + 1):
        line(c, X(v), y - 8, X(v), y + 8, LIGHT if v else INK, a, 3 if v else 5)
    text_mid(c, "0", X(0), y + 36, size, "black", INK, a)
    for v in pts:
        c.drawCircle(X(v), y, 15, paint(cor, a))
        if rotulos:
            pill(c, f"{v}".replace("-", "−"), X(v), y - 46, cor, size=size - 4, a=a, anchor="center")


def semaforo(c, x, y0, acesas, a, passo=170):
    """caixa escura vertical com 3 lâmpadas (vermelho, verde, azul); acesas = alfas de cada uma"""
    if a <= 0:
        return
    rrect(c, x - 52, y0 - 70, 104, passo * 2 + 140, 40, INK, a, shadow=True)
    for k, (col, al) in enumerate(zip((RED, GREEN, BLUE), acesas)):
        cy = y0 + k * passo
        c.drawCircle(x, cy, 40, paint(mix(INK, "#FFFFFF", 0.18), a))
        if al > 0:
            c.drawCircle(x, cy, 40, paint(col, a * al))


def voo(c, x0, y0, w, h, a, faixa=0.0, marcas=0.0, prog_=1.0):
    """trajetória de h = 20t − 5t² (0 a 4 s) num retângulo; faixa = linha dos 15 m; marcas = as duas passagens (sem tempo)"""
    if a <= 0:
        return
    rrect(c, x0, y0, w, h, 20, CEU, a)
    chao = y0 + h - 40
    line(c, x0 + 20, chao, x0 + w - 20, chao, "#8FB07A", a, 6)
    Hm = 22.0
    X = lambda tt: x0 + 50 + tt / 4 * (w - 100)
    Y = lambda hh: chao - hh / Hm * (h - 80)
    pth = skia.Path()
    n = int(80 * clamp(prog_)) + 1
    for i in range(n):
        tt = 4 * i / 80
        hh = 20 * tt - 5 * tt * tt
        (pth.moveTo if i == 0 else pth.lineTo)(X(tt), Y(hh))
    pp = paint(INK2, a, stroke=4)
    pp.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    c.drawPath(pth, pp)
    if faixa > 0:
        hline(c, x0 + 20, x0 + w - 20, Y(15), AMBER, a * faixa, 4, dash=[18, 10])
        pill(c, "15 m", x0 + w - 24, Y(15) - 30, AMBER, size=24, a=a * faixa, anchor="right")
    if marcas > 0:
        for tt in (1, 3):
            c.drawCircle(X(tt), Y(15), 18, paint(RED, a * marcas))
            c.drawCircle(X(tt), Y(15), 9, paint("#FFFFFF", a * marcas))
    if prog_ < 1:
        tt = 4 * clamp(prog_)
        c.drawCircle(X(tt), Y(20 * tt - 5 * tt * tt) - 18, 18, paint(MOLHO, a))


MOLHO = K.MOLHO if hasattr(K, "MOLHO") else "#E8743B"


def linha_tempo(c, x0, x1, y, a, marcas=0.0, faixa=0.0, rot=True):
    """0 a 4 s; marcas = os instantes 1 s e 3 s; faixa = o trecho de 1 s a 3 s (acima de 15 m)"""
    if a <= 0:
        return
    X = lambda tt: x0 + tt / 4 * (x1 - x0)
    arrow(c, x0 - 10, y, x1 + 40, y, INK2, a, 4, 14)
    for tt in range(5):
        line(c, X(tt), y - 10, X(tt), y + 10, INK, a, 3)
        text_mid(c, f"{tt} s", X(tt), y + 40, 26, "bold", GRAY, a)
    if faixa > 0:
        rrect(c, X(1), y - 22, (X(3) - X(1)) * clamp(faixa), 44, 22, GREEN, a * 0.35)
        if faixa > 0.9 and rot:
            pill(c, "acima de 15 m: 2 s", (X(1) + X(3)) / 2, y - 60, GREEN, size=26, a=a, anchor="center")
    if marcas > 0:
        for tt, s_ in ((1, "subindo"), (3, "descendo")):
            c.drawCircle(X(tt), y, 16, paint(RED, a * marcas))
            text_mid(c, s_, X(tt), y + 80, 24, "black", RED, a * marcas)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EQUAÇÃO DO 2º GRAU", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    pr = clamp((t - C["01.a"]) / 4.0)
    voo(c, 180, 230, 1000, 600, aa, faixa=ep(t, C["01.a"] + 1.5, 0.5), marcas=ep(t, C["01.b"], 0.5), prog_=pr)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        pill(c, "subindo: t = ?", 1260, 340, RED, size=34, a=ab)
        pill(c, "descendo: t = ?", 1260, 440, RED, size=34, a=ep(t, C["01.b"] + 1.0, 0.5))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1260, 520, 480, 120, 24, mix("#FFFFFF", GREEN, 0.14), acc)
        fmid(c, "3 segundos", 1500, 560, 46, "black", GREEN, acc)
        ftext(c, "sem Bhaskara", 1500, 612, 28, "bold", GRAY, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        cartas(c, 1500, 760, ("?", "?"), (0, 0), ad, w=110, h=150, gap=40)
        selo(c, 1500, 900, ad, "O JOGO DOS DOIS NÚMEROS", BLUE, -3, 28)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "achar raízes de cabeça", "x² − 7x + 10 = 0  →  2 e 5"),
            ("02.b", "saber os sinais delas sem resolver", "o produto entrega os sinais"),
            ("02.c", "montar a equação a partir das raízes", "raízes 3 e −5  →  equação?")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "EXPRESSÕES ALGÉBRICAS", 560, 280, 30, "black", PURPLE, aa)
        text(c, "o trinômio soma e produto", 560, 330, 26, "bold", GRAY, aa)
        expr(c, "x^2 + 5x + 6", 560, 430, 60, aa)
        expr(c, "= (x+2)(x+3)", 560, 520, 60, aa, cores={1: GREEN})
        pill(c, "2 + 3 = 5   ·   2 × 3 = 6", 560, 640, GREEN, size=30, a=ep(t, C["03.a"] + 4.0, 0.5),
             anchor="center")
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "EPISÓDIO 1", 1360, 280, 30, "black", BLUE, ab)
        text(c, "o produto nulo", 1360, 330, 26, "bold", GRAY, ab)
        fmid(c, "▢ · ▢ = 0", 1360, 470, 70, "black", INK, ab)
        regra(c, "alguém ali é zero", 1360, 620, ab, 32)
    line(c, 960, 240, 960, 780, "#E6E6E2", ab, 3)


# ======================================================================
# concreto: o jogo
# ======================================================================

def b_jogo(c, t, C, B):
    head_seq(c, t, C, [("04", "ADIVINHE", "PENSEI EM DOIS NÚMEROS", BLUE), ("05", "E A EQUAÇÃO?", "OS NÚMEROS DO JOGO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        aa = ep(t, C["04.a"], 0.5)
        fl = clamp((t - C["04.e"]) / 0.8)
        cartas(c, W / 2, 500, ("2", "5"), (fl, clamp((t - C["04.e"] - 0.4) / 0.8)), aa,
               pistas=("soma 7", "produto 10"), a_pistas=(ep(t, C["04.b"], 0.4), ep(t, C["04.c"], 0.4)))
        ad = ep(t, C["04.d"], 0.4) * (1 - ep(t, C["04.e"], 0.3))
        if ad > 0:
            fmid(c, "quais são?", W / 2, 720, 44, "black", INK2, ad)
        ae = ep(t, C["04.e"] + 1.2, 0.5)
        if ae > 0:
            pill(c, "2 + 5 = 7   ·   2 × 5 = 10", W / 2, 740, GREEN, size=36, a=ae, anchor="center")
        return
    cartas(c, 420, 470, ("2", "5"), (1, 1), 1.0, w=150, h=210, gap=50, size=90)
    aa = ep(t, C["05.a"], 0.5)
    expr(c, "x^2 - 7x + 10 = 0", 1180, 290, 72, aa)
    rows = [(C["05.b"], "x = 2:", "4 - 14 + 10 = 0"), (C["05.c"], "x = 5:", "25 - 35 + 10 = 0")]
    for k, (t0, l, ex) in enumerate(rows):
        a, d = rise(t, t0)
        if a <= 0:
            continue
        y = 430 + k * 110 + d
        fmid(c, l, 800, y, 40, "black", GREEN, a, align="left")
        expr(c, ex, 970, y, 46, a, align="left", cores={6: GREEN})
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 690, 1200, 110, 22, mix("#FFFFFF", BLUE, 0.10), ad)
        linha(c, [("os números do jogo são as ", INK), ("RAÍZES", BLUE), (" da equação", INK)], W / 2, 745, 38, ad)


# ======================================================================
# bloco a — as relações
# ======================================================================

def b_relacoes(c, t, C, B):
    head_seq(c, t, C, [("06", "AS RELAÇÕES", "SOMA E PRODUTO DAS RAÍZES", PURPLE),
                       ("07", "QUANDO a = 1", "O SINAL DO MEIO VEM TROCADO", PURPLE),
                       ("08", "ATALHO", "COMECE PELO PRODUTO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            text(c, "raízes:  x₁  e  x₂", W / 2, 270, 44, "black", INK, aa)
        for k, (cue, nome, ex, rhs, col) in enumerate((("06.b", "SOMA DAS RAÍZES", "S = x₁ + x₂", "= -b/a", BLUE),
                                                       ("06.c", "PRODUTO DAS RAÍZES", "P = x₁ · x₂", "= c/a", BLUE))):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            x = 560 + k * 800
            rrect(c, x - 360, 330, 720, 330, 24, mix("#FFFFFF", col, 0.10), a)
            text(c, nome, x, 385, 28, "black", col, a, tracking=1)
            fmid(c, ex, x, 470, 52, "black", INK, a)
            expr(c, rhs, x, 580, 76, ep(t, C[cue] + 2.2, 0.4), cores={0: PURPLE, 1: PURPLE})
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            regra(c, "RELAÇÕES DE GIRARD", W / 2, 750, ad, 40)
        return
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        expr(c, "x^2 - Sx + P = 0", W / 2, 280, 100, aa, cores={2: BLUE, 4: PURPLE})
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            expr(c, "x^2 - 7x + 10 = 0", W / 2, 470, 84, ab, cores={2: AMBER, 4: PURPLE})
            pill(c, "aparece −7", 760, 580, AMBER, size=30, a=ab, anchor="center")
            arrow(c, 860, 580, 1020, 580, INK2, ep(t, C["07.b"] + 1.6, 0.4), 4, 14)
            pill(c, "soma = +7", 1140, 580, GREEN, size=30, a=ep(t, C["07.b"] + 1.6, 0.4), anchor="center")
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            pill(c, "produto = 10", 1140, 670, PURPLE, size=30, a=acc, anchor="center")
        ab2 = ep(t, C["07.b"] + 2.4, 0.5)
        if ab2 > 0:
            regra(c, "o sinal do meio vem trocado", W / 2, 780, ab2, 36, AMBER)
        return
    a0 = ep(t, C["08.a"], 0.5)
    if a0 > 0:
        pill(c, "produto 10", 480, 270, PURPLE, size=34, a=a0, anchor="center")
        pill(c, "soma 7", 1440, 270, BLUE, size=34, a=ep(t, C["08.c"], 0.4), anchor="center")
    pares = [("1 × 10", "1 + 10 = 11", False), ("2 × 5", "2 + 5 = 7", True)]
    for k, (p_, s_, ok) in enumerate(pares):
        a = ep(t, C["08.b"] + 1.0 + 1.2 * k, 0.4)
        if a <= 0:
            continue
        y = 400 + k * 120
        rrect(c, 300, y - 50, 1320, 100, 18, "#FFFFFF", a, shadow=True)
        fmid(c, p_, 480, y, 46, "black", INK, a)
        ac = ep(t, C["08.c"] + 0.6, 0.4)
        if ac > 0:
            fmid(c, s_, 1300, y, 44, "black", GREEN if ok else GRAY, ac)
            check_icon(c, 1600, y - 4, 26, ac, GREEN if ok else RED, "check" if ok else "x")
    ad = ep(t, C["08.d"], 0.5)
    K.atalho(c, 360, 640, 1200, 180, "ATALHO · PRODUTO PRIMEIRO, SOMA DEPOIS", ["confira: multiplique e some"], ad, 34)


# ======================================================================
# bloco b — a tabela da seção 06
# ======================================================================

TAB = [("x^2 - 7x + 10", "7", "10", "2 e 5"),
       ("x^2 + x - 12", "-1", "-12", "3 e −4"),
       ("x^2 + 8x + 15", "-8", "15", "−3 e −5"),
       ("2x^2 - 7x + 3", "7/2", "3/2", "3 e 1/2")]


def _tabela(c, t, linhas_a, y0=250):
    """linhas_a = [(alfa_linha, alfa_sp, alfa_raizes)] para as 4 linhas da tabela"""
    a0 = max(x[0] for x in linhas_a)
    if a0 <= 0:
        return
    cols = (520, 930, 1170, 1480)
    rrect(c, 200, y0, 1520, 80, 16, mix("#FFFFFF", BLUE, 0.14), a0)
    for x, s_ in zip(cols, ("equação", "soma", "produto", "raízes")):
        text_mid(c, s_, x, y0 + 40, 30, "black", BLUE, a0)
    for k, ((eq, S, P, R), (al, asp, ar)) in enumerate(zip(TAB, linhas_a)):
        if al <= 0:
            continue
        y = y0 + 140 + k * 125
        rrect(c, 200, y - 55, 1520, 110, 16, "#FFFFFF", al, shadow=True)
        expr(c, eq, cols[0], y, 46, al)
        expr(c, S, cols[1], y, 46, asp, cores={0: GREEN if not S.startswith("-") else AMBER})
        expr(c, P, cols[2], y, 46, asp, cores={0: PURPLE})
        if ar > 0:
            fmid(c, R, cols[3], y, 46, "black", GREEN, ar)


def b_tabela(c, t, C, B):
    head_seq(c, t, C, [("09", "E COM SINAIS NEGATIVOS?", "A TABELA DA SEÇÃO 06", PURPLE),
                       ("10", "PRODUTO +, SOMA −", "AS DUAS NEGATIVAS", PURPLE),
                       ("11", "E QUANDO a ≠ 1?", "USE −b/a E c/a INTEIROS", PURPLE)])
    card(c, *CARD_R)
    E = lambda cue, d=0.0: ep(t, C[cue] + d, 0.4)
    L = [(1, 1, 1),
         (E("09.a"), E("09.b"), E("09.c")),
         (E("10.a"), E("10.b"), E("10.c")),
         (E("11.a"), E("11.b"), E("11.c"))]
    _tabela(c, t, L)
    ad = E("11.d")
    if ad > 0:
        pill(c, "3 + 1/2 = 7/2   ·   3 × 1/2 = 3/2", W / 2, 830, GREEN, size=30, a=ad, anchor="center")


# ======================================================================
# bloco c — os sinais (o semáforo)
# ======================================================================

def b_sinais(c, t, C, B):
    head_seq(c, t, C, [("12", "OS SINAIS SEM RESOLVER", "O PRODUTO ENTREGA OS SINAIS", PURPLE),
                       ("13", "PRODUTO POSITIVO", "A SOMA DIZ QUAL LADO", PURPLE),
                       ("14", "ATALHO DE PROVA", "RISQUE ANTES DE FAZER CONTA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13", "14"])
    E = lambda cue, d=0.0: ep(t, C[cue] + d, 0.5)
    r1, r2, r3 = E("12.b"), E("13.b", 1.0), E("13.c")
    if sid == "14":
        r1 = r2 = r3 = 1.0
    a0 = E("12.a")
    passo, y0 = (130, 290) if sid == "14" else (170, 330)
    semaforo(c, 290, y0, (r1, r2, r3), a0, passo)
    rows = [(r1, "P < 0", "uma de cada lado do zero", (-4, 3), RED),
            (r2, "P > 0  e  S > 0", "as duas positivas", (2, 5), GREEN),
            (r3, "P > 0  e  S < 0", "as duas negativas", (-5, -3), BLUE)]
    for k, (al, cond, s_, pts, col) in enumerate(rows):
        if al <= 0:
            continue
        y = y0 + k * passo
        fmid(c, cond, 400, y - 30, 38, "black", col, al, align="left")
        ftext(c, s_, 400, y + 26, 28, "bold", INK2, al, align="left")
        reta_sinais(c, 960, 1680, y, pts, al, cor=col, size=24)
    a13 = E("13.a") * (1 - r2)
    if a13 > 0 and sid == "13":
        pill(c, "as duas do mesmo lado", 1320, 500, PURPLE, size=30, a=a13, anchor="center")
    if sid == "14":
        aa = E("14.a")
        K.atalho(c, 360, 670, 1200, 150, "ATALHO · SINAIS OPOSTOS?",
                 ["risque as alternativas com as duas raízes positivas"], aa, 32)


# ======================================================================
# bloco d — o caminho inverso
# ======================================================================

def b_inverso(c, t, C, B):
    head(c, t, B["start"], "O CAMINHO INVERSO", "RAÍZES DADAS → EQUAÇÃO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    cartas(c, 480, 400, ("3", "-5"), (1, 1), aa, w=150, h=210, gap=50, size=86)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        expr(c, "S = 3 + (-5) = -2", 1240, 330, 52, ab, cores={6: BLUE})
        expr(c, "P = 3 · (-5) = -15", 1240, 430, 52, ep(t, C["15.b"] + 2.0, 0.4), cores={6: PURPLE})
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        expr(c, "x^2 - Sx + P = 0", W / 2, 600, 64, acc, cores={2: BLUE, 4: PURPLE})
        pill(c, "− (−2)x  =  + 2x", 1500, 600, AMBER, size=28, a=ep(t, C["15.c"] + 2.4, 0.4), anchor="center")
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 690, 1000, 120, 24, mix("#FFFFFF", GREEN, 0.14), ad)
        expr(c, "x^2 + 2x - 15 = 0", W / 2, 750, 70, ad, cores={2: GREEN, 4: GREEN})


# ======================================================================
# bloco e — a forma fatorada
# ======================================================================

def b_fatorada(c, t, C, B):
    head(c, t, B["start"], "A FORMA FATORADA", "A EQUAÇÃO COMO MULTIPLICAÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 220, 1200, 100, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("FORMA FATORADA", BLUE), (": escrever como multiplicação, usando as raízes", INK)], W / 2, 270, 32, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        fmid(c, "ax² + bx + c  =  a(x − x₁)(x − x₂)", W / 2, 410, 60, "black", PURPLE, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        expr(c, "2x^2 - 7x + 3 = 2(x-3)(x-{1/2})", W / 2, 540, 60, acc, cores={6: GREEN})
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        expr(c, "= (x-3)(2x-1)", W / 2 + 120, 650, 60, ad, cores={1: GREEN})
        pill(c, "o 2 entra no último parêntese", 560, 650, PURPLE, size=26, a=ad, anchor="center")
    ae = ep(t, C["16.e"], 0.5)
    if ae > 0:
        pill(c, "produto nulo:  x = 3  ou  x = 1/2", W / 2, 780, GREEN, size=34, a=ae, anchor="center")


# ======================================================================
# bloco f — quando desistir
# ======================================================================

def b_desistir(c, t, C, B):
    head(c, t, B["start"], "QUANDO DESISTIR DO JOGO", "SEM PAR INTEIRO? BHASKARA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    expr(c, "x^2 - 3x - 5 = 0", W / 2, 260, 76, aa)
    if aa > 0:
        pill(c, "soma 3", 760, 360, BLUE, size=30, a=aa, anchor="center")
        pill(c, "produto −5", 1160, 360, PURPLE, size=30, a=aa, anchor="center")
    for k, (p_, s_) in enumerate((("5 e −1", "soma 4"), ("−5 e 1", "soma −4"))):
        a = ep(t, C["17.b"] + 1.6 * k, 0.4)
        if a <= 0:
            continue
        y = 470 + k * 100
        rrect(c, 460, y - 42, 1000, 84, 18, "#FFFFFF", a, shadow=True)
        fmid(c, p_, 700, y, 42, "black", INK, a)
        fmid(c, s_, 1150, y, 42, "black", GRAY, a)
        check_icon(c, 1380, y - 4, 24, a, RED, "x")
    acc = ep(t, C["17.c"], 0.5)
    K.atalho(c, 360, 650, 1200, 170, "ATALHO · DEU POUCOS SEGUNDOS E NADA?", ["vá para Bhaskara (Δ = 29 aqui)"], acc, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "SOMA, PRODUTO, CONFIRA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    ab = ep(t, C["18.b"], 0.5)
    badge_num(c, 1, 260, 280, aa, 28, bg=PURPLE)
    expr(c, "x^2 - x - 20 = 0", 320, 280, 58, aa, align="left")
    badge_num(c, 2, 1000, 280, ab, 28, bg=PURPLE)
    fmid(c, "raízes 2 e 6  →  equação?", 1060, 280, 44, "black", INK, ab, align="left")
    if t < C["19"]:
        pause_timer(c, t, C["18.end"] - 1.9, W / 2, 560)
        return
    a1 = ep(t, C["19.a"], 0.5)
    if a1 > 0:
        pill(c, "soma 1 · produto −20", 600, 390, PURPLE, size=28, a=a1, anchor="center")
        pill(c, "P < 0: sinais opostos", 600, 470, RED, size=26, a=ep(t, C["19.a"] + 3.0, 0.4), anchor="center")
    b1 = ep(t, C["19.b"], 0.5)
    cartas(c, 600, 640, ("5", "-4"), (clamp((t - C["19.b"]) / 0.8), clamp((t - C["19.b"] - 0.4) / 0.8)), a1,
           w=120, h=170, gap=40, size=70)
    c1 = ep(t, C["19.c"], 0.5)
    if c1 > 0:
        pill(c, "soma 8 · produto 12", 1320, 390, PURPLE, size=28, a=c1, anchor="center")
    d1 = ep(t, C["19.d"], 0.5)
    if d1 > 0:
        rrect(c, 1000, 560, 640, 140, 24, mix("#FFFFFF", GREEN, 0.14), d1)
        expr(c, "x^2 - 8x + 12 = 0", 1320, 630, 54, d1, cores={2: GREEN, 4: GREEN})


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Soma é −b/a; produto é c/a.",
          "Dois números de soma S e produto P.",
          "Raízes dadas: x² − Sx + P = 0."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 58, "black", INK, a, 1360, 66)


ERROS = [("x² − 7x + 10:  soma = b/a = −7", "o número escrito na equação é o −7",
          "soma = −b/a = +7: o sinal do meio vem trocado"),
         ("raízes 2 e 6  →  x² + 8x + 12 = 0", "a soma é mesmo 8",
          "essa tem raízes −2 e −6; o certo é −Sx: x² − 8x + 12 = 0"),
         ("x² − 6x + 4: procurar o par sem parar", "o jogo funcionou nos outros exemplos",
          "1 e 4 somam 5, 2 e 2 somam 4: Bhaskara → x = 3 ± √5")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS3 = [("A", "= x^2 - 2x - 15 = 0", "+Sx: raízes −3 e 5", RED),
         ("B", "= x^2 + 2x + 15 = 0", "sinal do P: sem raiz real", RED),
         ("C", "= x^2 - 8x + 15 = 0", "raízes 3 e 5", RED),
         ("D", "= x^2 + 2x - 15 = 0", "", GREEN),
         ("E", "= x^2 + 15x - 2 = 0", "trocou S e P", RED)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · EU FAÇO", "MONTAR A EQUAÇÃO PELAS RAÍZES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4) * (1 - ep(t, C["25"], 0.4))
    yend = _enunciado(c, [("Um professor pediu aos alunos uma equação do 2º grau, com coeficiente de x² igual a 1, cujas "
                           "raízes fossem 3 e −5. A equação correta é", INK)], a0, 250, 30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["26.xa"], "B": C["26.xb"], "C": C["26.xc"], "E": C["26.xe"]}
    K.alternativas(c, t, C, ALTS3, 1000, 240, 680, 28, C["25.ok"], "D", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 110)
    if t >= C["25"]:
        ap = ep(t, C["25"], 0.4)
        rrect(c, 170, 230, 760, 600, 18, "#FFFFFF", ap, shadow=True)
        text(c, "CAMINHO INVERSO", 550, 285, 22, "black", PURPLE, ap, tracking=1)
        rows = [(C["25.a"], "S = -2   ·   P = -15", None), (C["25.b"], "x^2 - Sx + P = 0", None),
                (C["25.b"] + 2.0, "x^2 + 2x - 15 = 0", GREEN), (C["25.c"], "(x-3)(x+5) ✓", None)]
        for k, (t0, ex, col) in enumerate(rows):
            a, d = rise(t, t0)
            expr(c, ex, 550, 380 + k * 105 + d, 46, a, cores={i: col for i in range(9)} if col else None)


ALTS4 = [("A", "1 s", "um instante só", RED),
         ("B", "2 s", "", GREEN),
         ("C", "3 s", "um instante só", RED),
         ("D", "4 s", "voo inteiro (h = 0 em t = 4)", RED),
         ("E", "Nenhum: a bola não chega a 15 m.", "falsa", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · VOCÊ FAZ", "TEMPO ACIMA DE UMA ALTURA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4) * (1 - ep(t, C["28"], 0.4))
    yend = _enunciado(c, [("Uma bola é lançada verticalmente para cima, e sua altura, em metros, t segundos após o "
                           "lançamento, é dada por h(t) = 20t − 5t². Durante quanto tempo a bola permanece acima de 15 m "
                           "de altura?", INK)], a0, 250, 30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["29.xa"], "C": C["29.xc"], "D": C["29.xd"], "E": C["29.xe"]}
    K.alternativas(c, t, C, ALTS4, 1000, 240, 680, 30, C["28.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 110)
    if t < C["28"]:
        return
    ap = ep(t, C["28"], 0.4)
    rrect(c, 170, 230, 760, 600, 18, "#FFFFFF", ap, shadow=True)
    sid = which(t, C, ["28", "29"])
    if sid == "28" and t < C["28.c"]:
        rows = [(C["28.a"], "20t - 5t^2 = 15"), (C["28.b"], "5t^2 - 20t + 15 = 0"), (C["28.b"] + 4.0, "t^2 - 4t + 3 = 0")]
        for k, (t0, ex) in enumerate(rows):
            a, d = rise(t, t0)
            expr(c, ex, 550, 340 + k * 120 + d, 50, a, cores={0: GREEN, 2: GREEN, 4: GREEN} if k == 2 else None)
        if ep(t, C["28.b"] + 4.0, 0.4) > 0:
            pill(c, "÷ 5", 860, 580, PURPLE, size=26, a=ep(t, C["28.b"] + 4.0, 0.4), anchor="center")
        return
    # o jogo da bola: soma 4, produto 3 → 1 e 3; depois a linha do tempo
    expr(c, "t^2 - 4t + 3 = 0", 550, 268, 40, ap)
    ad = ep(t, C["28.d"], 0.1)
    cartas(c, 550, 500, ("1", "3"), (clamp((t - C["28.d"]) / 0.8), clamp((t - C["28.d"] - 0.4) / 0.8)), ap,
           w=120, h=170, gap=50, size=70, pistas=("soma 4", "produto 3"), a_pistas=(1, 1), pdx=320, psize=28)
    ae = ep(t, C["28.e"], 0.5)
    linha_tempo(c, 260, 820, 690, ae, marcas=ae, faixa=clamp((t - C["28.e"] - 3.0) / 1.2))
    af = ep(t, C["29.t"], 0.5) if sid == "29" else 0
    if af > 0:
        pill(c, "t = 2:  40 − 20 = 20 m", 1340, 760, GREEN, size=26, a=af, anchor="center")
    ag = ep(t, C["29.f"], 0.5)
    if ag > 0:
        pill(c, "altura máxima: série de Função Quadrática", 1340, 830, PURPLE, size=24, a=ag, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DO TEXTO À EQUAÇÃO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        # jardim com calçada em volta
        rrect(c, 300, 300, 520, 400, 20, "#D9D4C7", aa, shadow=True)
        rrect(c, 380, 380, 360, 240, 14, "#B9DDA5", aa)
        text_mid(c, "jardim", 560, 500, 34, "black", "#2F5D24", aa)
        pill(c, "calçada", 560, 330, INK2, size=22, a=aa, anchor="center")
        pill(c, "raízes:  2  e  −10", 1300, 330, PURPLE, size=36, a=aa, anchor="center")
    ab = ep(t, C["31.b"], 0.5)
    for k, s_ in enumerate(("2", "10", "−10")):
        a = ep(t, C["31.b"] + 0.8 * k, 0.4)
        if a > 0:
            rrect(c, 1050 + k * 180, 440, 150, 130, 22, "#FFFFFF", a, shadow=True)
            fmid(c, s_, 1125 + k * 180, 505, 56, "black", INK, a)
    if ab > 0:
        fmid(c, "?", 1300, 640, 70, "black", AMBER, ab)
    pill(c, "ep. 4 · do texto à equação", W / 2, 780, PURPLE, size=32, a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você achou o 2 e o 5 antes de mim?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, jogo=b_jogo, relacoes=b_relacoes, tabela=b_tabela,
              sinais=b_sinais, inverso=b_inverso, fatorada=b_fatorada, desistir=b_desistir, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q3=b_q3, q4=b_q4, ponte=b_ponte, cta=b_cta)
