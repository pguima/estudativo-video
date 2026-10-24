"""Visual — Comparação de Propostas e Tomada de Decisão, Episódio 4: ponto de equilíbrio de um negócio e meta de lucro
(tema claro). Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, mdraw...).
Peças deste episódio: muro() (o CUSTO FIXO como muro de tijolinhos de R$ 20,00 que vai fechando; camada extra dourada
para a meta de lucro), placar() (contador de peças com o placar PREJUÍZO / LUCRO que vira de vermelho para verde),
fluxo() (a peça vendida entra com R$ 35,00: R$ 15,00 voltam para a matéria-prima e o tijolinho de R$ 20,00 sobe para o
muro), barra_preco() (o preço partido em custo variável + margem), fabrica(), grafico_lucro() (a reta do lucro
cruzando o zero), linha(), caixa(), conferido().
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
_s = importlib.util.spec_from_file_location("comum033", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_comparacao_propostas_ep4_equilibrio_negocio.mp4"
CARD_R = K.CARD_R
GOLD = "#C98A00"
BRICK = "#C8553D"


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


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    text(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def caixa(c, cx, cy, tit, val, col, a, w=360, sub=None, h=140):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 33, 24, "black", col, a)
    size = 44
    while text_w(val, "black", size) > w - 30:
        size -= 2
    text_mid(c, val, cx, cy + 22, size, "black", INK, a)
    if sub:
        text(c, sub, cx, cy + h / 2 + 34, 24, "bold", GRAY, a)


def muro(c, x, y, w, h, n, a, cols=20, rows=15, rotulo="CUSTO FIXO · R$ 6.000,00", extra_rows=0, extra_n=0,
         rot_extra="META"):
    """o CUSTO FIXO como muro: grade cols × rows de tijolinhos (cada um = a margem); n = tijolos já assentados
    (de baixo para cima). extra_rows/extra_n: camada dourada da meta de lucro, por cima."""
    if a <= 0:
        return
    tot_rows = rows + extra_rows
    bh = h / tot_rows
    bw = w / cols
    rrect(c, x - 10, y - 10, w + 20, h + 20, 12, "#FFFFFF", a, shadow=True)
    for r_ in range(tot_rows):
        extra = r_ >= rows
        yy = y + h - (r_ + 1) * bh
        off = bw / 2 if r_ % 2 else 0
        for k in range(cols):
            idx = r_ * cols + k if not extra else (r_ - rows) * cols + k
            cheio = (idx < n) if not extra else (idx < extra_n)
            xx = x + k * bw + off
            ww = bw if xx + bw <= x + w + 0.1 else (x + w - xx)
            if ww <= 2:
                continue
            col = (GOLD if extra else BRICK) if cheio else "#EEF0F4"
            c.drawRect(skia.Rect.MakeXYWH(xx + 1.5, yy + 1.5, ww - 3, bh - 3), paint(col, a * (1.0 if cheio else 0.9)))
        if off:
            c.drawRect(skia.Rect.MakeXYWH(x + 1.5, yy + 1.5, off - 3, bh - 3),
                       paint((GOLD if extra else BRICK) if ((r_ - (rows if extra else 0)) * cols < (extra_n if extra else n))
                             else "#EEF0F4", a))
    c.drawRect(skia.Rect.MakeXYWH(x, y + extra_rows * bh, w, rows * bh), paint(INK2, a, stroke=3))
    if extra_rows:
        c.drawRect(skia.Rect.MakeXYWH(x, y, w, extra_rows * bh), paint(GOLD, a, stroke=3))
        text(c, rot_extra, x + w / 2, y - 26, 26, "black", GOLD, a)
    if rotulo:
        text(c, rotulo, x + w / 2, y + h + 52, 28, "black", INK2, a)


def placar(c, cx, cy, q, lucro, a, w=420):
    """contador de peças + placar de lucro: vermelho (prejuízo) até 0, azul no empate, verde acima"""
    if a <= 0:
        return
    col = RED if lucro < 0 else (BLUE if lucro == 0 else GREEN)
    rrect(c, cx - w / 2, cy - 120, w, 240, 26, "#FFFFFF", a, shadow=True)
    text(c, "PEÇAS VENDIDAS", cx, cy - 76, 24, "black", GRAY, a)
    text_mid(c, f"{q}", cx, cy - 18, 72, "black", INK, a)
    rrect(c, cx - w / 2 + 20, cy + 36, w - 40, 66, 16, col, a * 0.92)
    rot = "PREJUÍZO" if lucro < 0 else ("EMPATE" if lucro == 0 else "LUCRO")
    val = f"R$ {abs(lucro):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    text_mid(c, f"{rot}  {val}" if lucro else "EMPATE  R$ 0,00", cx, cy + 69, 30, "black", "#FFFFFF", a)


def fluxo(c, x, y, u, a):
    """a peça vendida: ficha de R$ 35,00 que se parte em R$ 15,00 (volta para a matéria-prima, para baixo) e o
    tijolinho de R$ 20,00 (sobe para o muro, à esquerda). u = progresso 0..1"""
    if a <= 0:
        return
    u = clamp(u)
    s1 = ease_io(clamp(u / 0.35))
    rrect(c, x - 110, y - 50 - 40 * (1 - s1), 220, 100, 20, mix("#FFFFFF", BLUE, 0.12), a * s1, shadow=True)
    text_mid(c, "R$ 35,00", x, y - 40 * (1 - s1), 44, "black", BLUE, a * s1)
    text(c, "1 peça vendida", x, y - 70 - 40 * (1 - s1), 24, "bold", GRAY, a * s1)
    s2 = ease_io(clamp((u - 0.4) / 0.6))
    if s2 > 0:
        # R$ 15 desce para a matéria-prima
        yy = y + 70 + 150 * s2
        rrect(c, x + 40, yy - 34, 170, 68, 16, mix("#FFFFFF", GRAY, 0.2), a, shadow=True)
        text_mid(c, "R$ 15,00", x + 125, yy, 32, "black", INK2, a)
        text(c, "volta para a matéria-prima", x + 125, yy + 70, 22, "bold", GRAY, a * s2)
        # tijolinho de R$ 20 sobe para o muro
        xx = x - 60 - 260 * s2
        yb = y + 70 - 110 * s2
        c.drawRect(skia.Rect.MakeXYWH(xx - 75, yb - 30, 150, 60), paint(BRICK, a))
        text_mid(c, "R$ 20,00", xx, yb, 30, "black", "#FFFFFF", a)
        text(c, "tijolinho → muro", xx, yb - 48, 22, "black", BRICK, a * s2)


def barra_preco(c, x, y, w, a, sep=0.0, rot=True):
    """o preço de R$ 35,00 partido: R$ 15,00 (custo variável) + R$ 20,00 (margem)"""
    if a <= 0:
        return
    h = 110
    w15 = w * 15 / 35
    gap = 24 * ease_io(clamp(sep))
    rrect(c, x, y, w15, h, 16, mix("#FFFFFF", GRAY, 0.35), a)
    text_mid(c, "R$ 15,00", x + w15 / 2, y + h / 2, 40, "black", INK2, a)
    rrect(c, x + w15 + gap, y, w - w15, h, 16, GREEN, a * 0.9)
    text_mid(c, "R$ 20,00", x + w15 + gap + (w - w15) / 2, y + h / 2, 44, "black", "#FFFFFF", a)
    if rot:
        text(c, "PREÇO R$ 35,00", x + (w + gap) / 2, y - 26, 28, "black", BLUE, a)
        ar = a * clamp(sep)
        text(c, "custo da peça", x + w15 / 2, y + h + 44, 26, "bold", GRAY, ar)
        text(c, "MARGEM", x + w15 + gap + (w - w15) / 2, y + h + 44, 28, "black", GREEN, ar)


def fabrica(c, x, y, s, a):
    """fábrica estilizada: galpão com telhado em serra e chaminé"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y + 200 * s)
    p.lineTo(x, y + 60 * s)
    for k in range(3):
        p.lineTo(x + (k * 120 + 120) * s, y)
        p.lineTo(x + (k * 120 + 120) * s, y + 60 * s)
    p.lineTo(x + 360 * s, y + 200 * s)
    p.close()
    c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.18), a))
    c.drawPath(p, paint(INK2, a, stroke=5))
    rrect(c, x + 400 * s - 70 * s, y - 70 * s, 50 * s, 270 * s, 6, INK2, a)
    for k in range(3):
        c.drawCircle(x + 355 * s + k * 26 * s, y - 100 * s - k * 30 * s, (18 + k * 6) * s, paint(GRAY, a * 0.35))
    for k in range(3):
        rrect(c, x + (30 + k * 110) * s, y + 100 * s, 70 * s, 60 * s, 6, "#FFFFFF", a)
    rrect(c, x + 150 * s, y + 140 * s, 60 * s, 60 * s, 6, INK2, a)


def grafico_lucro(c, x, y, w, h, a, q_max=400, mark=300, prog_=1.0):
    """reta do lucro L = 20q − 6000 de 0 a q_max: abaixo do zero, vermelha; acima, verde; cruza em 300"""
    if a <= 0:
        return
    L = lambda q: 20 * q - 6000
    lmin, lmax = L(0), L(q_max)
    X = lambda q: x + w * q / q_max
    Y = lambda v: y + h * (lmax - v) / (lmax - lmin)
    rrect(c, x - 20, y - 20, w + 40, h + 40, 16, "#FFFFFF", a, shadow=True)
    line(c, x, Y(0), x + w, Y(0), INK2, a, 3)
    text(c, "lucro zero", x + 8, Y(0) - 14, 22, "bold", GRAY, a, align="left")
    u = clamp(prog_)
    qe = q_max * u
    if qe > 0:
        q1 = min(qe, mark)
        line(c, X(0), Y(L(0)), X(q1), Y(L(q1)), RED, a, 7)
        if qe > mark:
            line(c, X(mark), Y(0), X(qe), Y(L(qe)), GREEN, a, 7)
    if u >= mark / q_max:
        c.drawCircle(X(mark), Y(0), 14, paint(BLUE, a))
        text(c, "300", X(mark), Y(0) + 52, 28, "black", BLUE, a)
    text(c, "prejuízo", X(80), Y(L(60)) + 50, 24, "black", RED, a)
    if u > 0.9:
        text(c, "lucro", X(370), Y(L(370)) + 50, 24, "black", GREEN, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PONTO DE EQUILÍBRIO DE UM NEGÓCIO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    caixa(c, 520, 330, "CUSTO FIXO", "R$ 6.000,00 / mês", BLUE, aa, 560)
    caixa(c, 520, 530, "PREÇO DA PEÇA", "R$ 35,00", BLUE, ep(t, C["01.a"] + 1.5, 0.5), 560)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 960, 260, 740, 160, 26, "#FFFFFF", ab, shadow=True)
        linha(c, [("6.000 ÷ 35 ≈ ", INK), ("172 peças", AMBER), (" ?", INK)], 1330, 340, 50, ab)
        sc = ep(t, C["01.c"], 0.5)
        strike(c, 1000, 340, 1660, 340, sc, RED, sc)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 960, 460, 740, 200, 26, mix("#FFFFFF", GREEN, 0.10), acc, shadow=True)
        text(c, "para pagar as contas", 1330, 520, 30, "bold", GRAY, acc)
        text_mid(c, "300 peças", 1330, 595, 80, "black", GREEN, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 520, 720, ad, "+ R$ 15,00 PARA FAZER CADA PEÇA", RED, -3, 30)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "quantas unidades para EMPATAR", GREEN),
             ("02.b", "quantas unidades para bater a META DE LUCRO", AMBER)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 220 + d
        rrect(c, 260, y, 1400, 160, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
        check_icon(c, 340, y + 80, 30, a, col)
        text_mid(c, s, 400, y + 80, 44, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "2 LEMBRETES", "RÁPIDOS", GREEN)
    a1, d1 = rise(t, C["03.a"])
    if a1 > 0:
        rrect(c, 200, 280 + d1, 720, 440, 24, "#FFFFFF", a1, shadow=True)
        pill(c, "DESCONTOS E LUCRO", 560, 330 + d1, GREEN, size=26, a=a1, anchor="center", bounds=(0, 1920))
        text_mid(c, "lucro =", 560, 470 + d1, 54, "black", INK2, a1)
        text_mid(c, "venda − custo", 560, 560 + d1, 60, "black", PURPLE, a1)
    a2, d2 = rise(t, C["03.b"])
    if a2 > 0:
        rrect(c, 1000, 280 + d2, 720, 440, 24, "#FFFFFF", a2, shadow=True)
        pill(c, "EPISÓDIO 2", 1360, 330 + d2, GREEN, size=26, a=a2, anchor="center", bounds=(0, 1920))
        x0, y0 = 1110, 420 + d2
        line(c, x0, y0 + 220, x0 + 500, y0 + 220, INK2, a2, 3)
        line(c, x0, y0 + 60, x0 + 500, y0 + 180, BLUE, a2, 6)
        line(c, x0, y0 + 160, x0 + 500, y0 + 20, PURPLE, a2, 6)
        c.drawCircle(x0 + 208, y0 + 110, 14, paint(AMBER, a2))
        text(c, "EMPATE", x0 + 208, y0 + 80, 26, "black", AMBER, a2)


# ======================================================================
# concreto e blocos a, b, c
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA PEQUENA FÁBRICA", "DE PEÇAS", BLUE)
    card(c, *CARD_R)
    fabrica(c, 260, 360, 1.15, ep(t, C["04.a"], 0.6))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        pill(c, "TODO MÊS", 1260, 300, BLUE, size=28, a=ab, anchor="center", bounds=(0, 1920))
        caixa(c, 1100, 420, "ALUGUEL", "chega todo mês", BLUE, ab, 300, h=120)
        caixa(c, 1430, 420, "SALÁRIOS", "chega todo mês", BLUE, ab, 300, h=120)
        text(c, "venda 1 peça ou 1.000", 1265, 540, 30, "bold", GRAY, ep(t, C["04.b"] + 1.6, 0.5))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        pill(c, "A CADA PEÇA", 1260, 620, AMBER, size=28, a=acc, anchor="center", bounds=(0, 1920))
        caixa(c, 1265, 730, "MATÉRIA-PRIMA", "gasta em cada peça", AMBER, acc, 520, h=120)


def b_custos(c, t, C, B):
    head(c, t, B["start"], "FIXO × VARIÁVEL", "QUE CONTA É QUAL?", BLUE)
    card(c, *CARD_R)
    for k, (cue, nome, sig, val, col) in enumerate(
            (("05.a", "CUSTO FIXO", "paga mesmo sem produzir", "R$ 6.000,00 por mês", BLUE),
             ("05.b", "CUSTO VARIÁVEL POR UNIDADE", "o que cada peça gasta para existir", "R$ 15,00 por peça", BLUE))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 200 + k * 780
        rrect(c, x, 280 + d, 740, 460, 26, mix("#FFFFFF", col, 0.06), a, shadow=True)
        text(c, nome, x + 370, 350 + d, 40 if k == 0 else 34, "black", col, a)
        text(c, sig, x + 370, 420 + d, 30, "bold", INK2, a)
        rrect(c, x + 60, 500 + d, 620, 150, 22, "#FFFFFF", a, shadow=True)
        text_mid(c, val, x + 370, 575 + d, 50, "black", INK, a)
        text(c, "aluguel, salários" if k == 0 else "matéria-prima", x + 370, 710 + d, 26, "bold", GRAY, a)


def b_margem(c, t, C, B):
    head_seq(c, t, C, [("06", "MARGEM DE CONTRIBUIÇÃO", "O PREÇO NÃO É TODO SEU", BLUE),
                       ("07", "O MURO DO CUSTO FIXO", "CADA PEÇA, UM TIJOLINHO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.t"], 0.5)
        barra_preco(c, 360, 330, 1200, aa, sep=ep(t, C["06.a"] + 1.2, 0.8))
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            linha(c, [("35 − 15 = ", INK), ("20", GREEN)], W / 2, 590, 56, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            rrect(c, 300, 660, 1320, 140, 24, mix("#FFFFFF", BLUE, 0.10), acc, shadow=True)
            text(c, "MARGEM DE CONTRIBUIÇÃO", W / 2, 712, 30, "black", BLUE, acc)
            text(c, "= preço − custo variável", W / 2, 768, 40, "black", PURPLE, acc)
        return
    aa = ep(t, C["07.t"], 0.5)
    n = int(round(300 * clamp((t - C["07.a"]) / 12.0))) if t > C["07.a"] else 0
    muro(c, 200, 270, 640, 420, n, aa)
    if aa > 0:
        text(c, f"{n} tijolinhos", 520, 245, 26, "black", BRICK, aa)
    u = ((t - C["07.a"]) % 3.0) / 3.0 if t > C["07.a"] else 0.0
    fluxo(c, 1320, 380, u if t < C["07.c"] else 1.0, ep(t, C["07.a"], 0.4))
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        regra(c, "tijolinho = margem de contribuição = R$ 20,00", W / 2 + 160, 790, acc, 34, PURPLE)


def b_formula(c, t, C, B):
    head(c, t, B["start"], "O LUCRO DO MÊS", "A FÓRMULA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 280, 1460, 150, 24, mix("#FFFFFF", PURPLE, 0.08), aa, shadow=True)
        linha(c, [("lucro = ", INK), ("(preço − custo variável)", GREEN), (" · q − ", INK), ("custo fixo", BLUE)],
              W / 2, 355, 50, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        text(c, "q = quantidade vendida", W / 2, 500, 32, "bold", GRAY, ab)
        linha(c, [("lucro = ", INK), ("20", GREEN), (" · q − ", INK), ("6.000", BLUE)], W / 2, 580, 64, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        K.atalho(c, 460, 660, 1000, 150, "ATALHO", ["margem primeiro, divisão depois"], acc, 38)


# ======================================================================
# bloco d — equilíbrio (eu faço), bloco e — dividir pelo preço
# ======================================================================

def b_equilibrio(c, t, C, B):
    head_seq(c, t, C, [("09", "EU FAÇO · O EMPATE", "LUCRO ZERO", PURPLE),
                       ("10", "CONFIRA O LUCRO", "O MESMO CRUZAMENTO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.t"], 0.5)
        n = int(round(300 * clamp((t - C["09.a"]) / max(1.0, C["09.c"] - C["09.a"])))) if t > C["09.a"] else 0
        muro(c, 200, 270, 600, 400, n, aa)
        pa = ep(t, C["09.a"], 0.4)
        if pa > 0:
            text(c, f"{n} peças", 500, 245, 28, "black", BRICK, pa)
        a1 = ep(t, C["09.a"], 0.5)
        if a1 > 0:
            pill(c, "LUCRO ZERO", 1290, 300, BLUE, size=28, a=a1, anchor="center", bounds=(0, 1920))
            linha(c, [("q = ", INK), ("6.000", BLUE), (" ÷ ", INK), ("20", GREEN)], 1290, 400, 60, a1)
        a2 = ep(t, C["09.b"], 0.5)
        if a2 > 0:
            K.atalho(c, 960, 470, 660, 190, "ATALHO · CORTE O MESMO ZERO", [("m", "600 ÷ 2 = 300")], a2, 48)
        a3 = ep(t, C["09.c"], 0.5)
        if a3 > 0:
            selo(c, 1290, 740, a3, "300 PEÇAS POR MÊS: O MURO FECHA", GREEN, -3, 30)
        return
    aa = ep(t, C["10.a"], 0.5)
    if t < C["10.b"]:
        q, lu = 300, 0
    else:
        k = int((t - C["10.b"]) / 1.8) % 3
        q = (299, 301, 300)[k] if t < C["10.c"] else 300
        lu = 20 * q - 6000
    placar(c, 450, 420, q, lu, aa)
    if aa > 0:
        linha(c, [("300 · 20 − 6.000 = ", INK), ("0", BLUE)], 450, 620, 40, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        linha(c, [("299 → ", INK2), ("− R$ 20", RED), ("   ·   301 → ", INK2), ("+ R$ 20", GREEN)], 450, 700, 34, ab)
    grafico_lucro(c, 940, 300, 720, 400, ep(t, C["10.c"], 0.5), prog_=ep(t, C["10.c"], 2.0))


def b_preco(c, t, C, B):
    head(c, t, B["start"], "E AS 172 DO COMEÇO?", "DIVIDIR PELO PREÇO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("6.000 ÷ ", INK), ("35", AMBER), (" ≈ 172 peças", INK)], 1270, 320, 50, aa)
    ab = ep(t, C["11.b"], 0.5)
    muro(c, 200, 270, 600, 400, int(172 * ab), ep(t, C["11.t"], 0.5))
    if ab > 0:
        linha(c, [("172 · ", INK), ("20", GREEN), (" = 3.440", INK)], 1270, 450, 50, ab)
        text(c, "faltam 128 tijolinhos no muro", 1270, 530, 30, "bold", GRAY, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        placar(c, 1270, 680, 172, 3440 - 6000, acc, w=520)


# ======================================================================
# bloco f — meta de lucro
# ======================================================================

def b_meta(c, t, C, B):
    head_seq(c, t, C, [("12", "META DE LUCRO", "MAIS UM PEDAÇO DE MURO", PURPLE),
                       ("13", "NÃO DEU EXATO?", "NO MÍNIMO: PARA CIMA", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.t"], 0.5)
        ext = ep(t, C["12.a"], 0.6)
        n = 300 if t > C["12.a"] else 0
        en = int(round(50 * clamp((t - C["12.b"]) / 3.0))) if t > C["12.b"] else 0
        muro(c, 200, 250, 600, 460, n, aa, extra_rows=3 if ext > 0 else 0, extra_n=en,
             rot_extra="META R$ 1.000", rotulo="FIXO + META")
        a1 = ep(t, C["12.a"], 0.5)
        if a1 > 0:
            linha(c, [("6.000", BLUE), (" + ", INK), ("1.000", GOLD), (" = 7.000", INK)], 1290, 330, 52, a1)
        a2 = ep(t, C["12.b"], 0.5)
        if a2 > 0:
            linha(c, [("7.000 ÷ ", INK), ("20", GREEN), (" = ", INK), ("350 peças", PURPLE)], 1290, 450, 52, a2)
        a3 = ep(t, C["12.c"], 0.5)
        if a3 > 0:
            rrect(c, 960, 560, 660, 150, 22, "#FFFFFF", a3, shadow=True)
            linha(c, [("350 · 20 − 6.000 = ", INK), ("1.000", GREEN)], 1290, 610, 40, a3)
            conferido(c, "bateu a meta", 1150, 680, ep(t, C["12.c"] + 2.5, 0.4), True, 32)
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        linha(c, [("(6.000 + 1.010) ÷ 20 = ", INK), ("350,5", AMBER)], W / 2, 300, 54, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        x0, x1, y = 360, 1560, 470
        line(c, x0, y, x1, y, INK2, ab, 5)
        for v, lab, col in ((350, "350", RED), (350.5, "350,5", AMBER), (351, "351", GREEN)):
            xx = x0 + (x1 - x0) * (v - 349.5) / 2.0
            c.drawCircle(xx, y, 14, paint(col, ab))
            text(c, lab, xx, y - 30, 34, "black", col, ab)
        text(c, "lucro R$ 1.000: NÃO bate", x0 + (x1 - x0) * 0.25, y + 70, 28, "black", RED, ab)
        text(c, "lucro R$ 1.020: bate", x0 + (x1 - x0) * 0.75, y + 70, 28, "black", GREEN,
             ep(t, C["13.c"], 0.5))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        K.atalho(c, 360, 610, 1200, 190, "ATALHO",
                 ["\"no mínimo\" + resultado quebrado", "suba para o próximo inteiro → 351"], acc, 36)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ · FOOD TRUCK", "PAUSE E TENTE", GREEN),
                       ("15", "VAMOS JUNTOS", "MARGEM PRIMEIRO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        for k, (L, v, col) in enumerate((("CUSTO FIXO", "R$ 3.600,00 / mês", BLUE), ("CADA LANCHE CUSTA", "R$ 8,00", AMBER),
                                         ("PREÇO DO LANCHE", "R$ 23,00", BLUE))):
            caixa(c, W / 2 + (k - 1) * 520, 300, L, v, col, aa, 480)
    if t < C["15"]:
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            text_mid(c, "empatar?   ·   lucrar R$ 1.500,00?", W / 2, 470, 44, "black", INK, ab)
        pause_timer(c, t, C["14.end"] - 1.9, W / 2, 640)
        return
    rows = [("15.a", [("margem: 23 − 8 = ", INK), ("15", GREEN)]),
            ("15.b", [("empate: 3.600 ÷ 15 = ", INK), ("240 lanches", PURPLE)]),
            ("15.c", [("meta: (3.600 + 1.500) ÷ 15 = 5.100 ÷ 15 = ", INK), ("340 lanches", PURPLE)])]
    for k, (cue, partes) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        linha(c, partes, W / 2, 460 + k * 95, 42, a)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        linha(c, [("340 · 15 − 3.600 = ", INK), ("1.500", GREEN)], 860, 770, 40, ad)
        conferido(c, "confere", 1260, 782, ep(t, C["15.d"] + 2.8, 0.4), True, 34)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Divida o custo fixo pela margem, não pelo preço.",
          "A meta de lucro entra junto com o custo fixo.",
          "\"No mínimo\" com resultado quebrado: arredonde para cima."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "22"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Equilíbrio dividindo pelo preço: 6.000 ÷ 35", "o dinheiro que entra é o preço",
          "parte do preço volta para a peça: divida pela margem (35 − 15 = 20)"),
         ("Arredondar para baixo: 5.000 ÷ 30 = 166,7 → 166", "é a regra de arredondar da escola",
          "com 166 ainda há R$ 20 de prejuízo: o mínimo é 167")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18"], ERROS)


# ======================================================================
# questão 5 (você faz)
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


ALTS5 = [("A", "100 peças", "2.000 ÷ 20: esqueceu o fixo", RED), ("B", "229 peças", "8.000 ÷ 35: dividiu pelo preço", RED),
         ("C", "300 peças", "o equilíbrio: esqueceu a meta", RED), ("D", "400 peças", "", GREEN),
         ("E", "534 peças", "8.000 ÷ 15: pelo custo", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "META DE LUCRO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["19.a"], 0.4)
    yend = _enunciado(c, "Uma pequena fábrica tem custo fixo mensal de R$ 6.000,00. Cada peça custa R$ 15,00 para ser "
                      "produzida e é vendida por R$ 35,00. Para obter lucro de R$ 2.000,00 em um mês, a fábrica precisa "
                      "produzir e vender, no mínimo,", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["20"], 0.3)), align="left")
    cues_in = {L: C[f"19.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"21.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 40, C["20.ok"], "D", cues_in, cues_x, gap=38)
    if t < C["20"]:
        pause_timer(c, t, C["19.end"] - 2.4, 540, 720, dur=2.1)
        return
    y0 = yend + 4
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["20"], 0.4), shadow=True)
    linha(c, [("margem: 35 − 15 = ", INK), ("20", GREEN)], 540, y0 + 55, 32, ep(t, C["20.a"], 0.4))
    linha(c, [("6.000 + 2.000 = ", INK), ("8.000", GOLD)], 540, y0 + 115, 32, ep(t, C["20.b"], 0.4))
    linha(c, [("8.000 ÷ 20 = ", INK), ("400", PURPLE)], 540, y0 + 175, 34, ep(t, C["20.b"] + 3.0, 0.4))
    linha(c, [("400 · 20 − 6.000 = ", INK), ("2.000", GREEN)], 540, y0 + 235, 30, ep(t, C["20.c"], 0.4))
    if t > C["21.c"]:
        text(c, "B e E ainda arredondam para cima", 540, y0 + 290, 24, "bold", AMBER, ep(t, C["21.c"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DO BLOCO", PURPLE)
    itens = [("23.a", "juntamos este assunto", "mesma data · planos · líquido · equilíbrio"),
             ("23.b", "fechamos o bloco", "toda a Matemática Financeira"),
             ("23.c", "pegadinhas e inéditas", "no formato do ENEM")]
    for k, (cue, s, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 300 + d, 480, 300, 24, "#FFFFFF", a, shadow=True)
        badge_num(c, k + 1, x + 240, 370 + d, a, 34, bg=PURPLE)
        sz = 34
        while text_w(s, "black", sz) > 440:
            sz -= 2
        text(c, s, x + 240, 480 + d, sz, "black", INK, a)
        sz2 = 24
        while text_w(sub, "bold", sz2) > 440:
            sz2 -= 1
        text(c, sub, x + 240, 540 + d, sz2, "bold", GRAY, a)
    pill(c, "ep. 5 · revisão", W / 2, 760, PURPLE, size=30, a=ep(t, C["23.c"] + 1.0, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["24.like"], C["24.sub"], C["24.bell"], C["24.com"], C["24.bye"],
        "Peça a R$ 45,00: quantas para empatar?", canal="no Estudativo", anki=C["24.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, custos=b_custos, margem=b_margem,
              formula=b_formula, equilibrio=b_equilibrio, preco=b_preco, meta=b_meta, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q5=b_q5, ponte=b_ponte, cta=b_cta)
