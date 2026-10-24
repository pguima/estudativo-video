"""Visual — Sistemas de Equações Lineares, Episódio 3: concorrentes, paralelas ou coincidentes (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, fr, alternativas, erro_cards, atalho...).
Peças deste episódio: plano() (plano cartesiano com retas a·x + b·y = c, pontos e a reta que "pisca" quando coincide),
trilhos() / cruzamento() / rua_dupla() (as três cenas da rua), caixas() (as três razões a₁/a₂, b₁/b₂, c₁/c₂ em caixinhas
lado a lado, com = ou ≠ surgindo entre elas) e mini() (as três situações lado a lado, com os selos 0 = 2 e 0 = 0).
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
_s = importlib.util.spec_from_file_location("comum037", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr, fr = K.fmid, K.ftext, K.ftext_w, K.expr, K.fr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_sistemas_ep3_tres_posicoes.mp4"
CARD_R = K.CARD_R
COR_R = BLUE
COR_S = "#E0731F"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]."""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        x += w_


def defin(c, termo, s, x, y, w, a, col=None):
    """faixa azul de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 70, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 35, 30, a, align="left")


def plano(c, cx, cy, s, a, retas=(), pontos=(), xr=(-1, 6), yr=(-1, 6), passo=1, rot=("x", "y"), num=True):
    """plano cartesiano quadrado de lado s centrado em (cx, cy). retas = [(A, B, C, cor, u, pisca)] para A·x + B·y = C
    (u = quanto já foi desenhado, 0..1; pisca > 0 faz a reta pulsar); pontos = [(x, y, cor, alfa, rotulo)]."""
    if a <= 0:
        return
    x0, y0 = cx - s / 2, cy - s / 2
    px = lambda x: x0 + (x - xr[0]) / (xr[1] - xr[0]) * s
    py = lambda y: y0 + s - (y - yr[0]) / (yr[1] - yr[0]) * s
    rrect(c, x0 - 16, y0 - 16, s + 32, s + 32, 18, "#FFFFFF", a, shadow=True)
    v = xr[0]
    while v <= xr[1] + 1e-9:
        line(c, px(v), y0, px(v), y0 + s, "#EEEEEA", a, 2)
        v += passo
    v = yr[0]
    while v <= yr[1] + 1e-9:
        line(c, x0, py(v), x0 + s, py(v), "#EEEEEA", a, 2)
        v += passo
    if xr[0] <= 0 <= xr[1]:
        line(c, px(0), y0, px(0), y0 + s, INK2, a, 3)
    if yr[0] <= 0 <= yr[1]:
        line(c, x0, py(0), x0 + s, py(0), INK2, a, 3)
    text(c, rot[0], x0 + s - 8, py(max(0, yr[0])) - 12, 22, "black", GRAY, a, align="right")
    text(c, rot[1], px(max(0, xr[0])) + 12, y0 + 26, 22, "black", GRAY, a, align="left")
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x0, y0, s, s))
    for A, B, Cc, col, u, pisca in retas:
        if u <= 0:
            continue
        xa, xb = xr[0] - 1, xr[1] + 1
        ya, yb = (Cc - A * xa) / B, (Cc - A * xb) / B
        al = a
        if pisca > 0:
            al = a * (0.55 + 0.45 * math.cos(pisca * 6.0))
        line(c, px(xa), py(ya), px(xa + (xb - xa) * u), py(ya + (yb - ya) * u), col, al, 7, cap_round=True)
    c.restore()
    for x, y, col, al, rot_ in pontos:
        if al <= 0:
            continue
        c.drawCircle(px(x), py(y), 11, paint("#FFFFFF", a * al))
        c.drawCircle(px(x), py(y), 8, paint(col, a * al))
        if rot_:
            pill(c, rot_, px(x) + 18, py(y) - 30, col, size=22, a=a * al, bounds=(0, 1920))


def trilhos(c, cx, cy, w, a):
    if a <= 0:
        return
    for k in range(9):
        x = cx - w / 2 + 20 + k * (w - 40) / 8
        rrect(c, x - 8, cy - 46, 16, 92, 4, "#B98B5E", a)
    for dy in (-30, 30):
        rrect(c, cx - w / 2, cy + dy - 6, w, 12, 6, "#7D8590", a)


def _rua(c, x1, y1, x2, y2, a, larg=48):
    line(c, x1, y1, x2, y2, "#9AA0A6", a, larg)
    n = 7
    for k in range(n):
        u0, u1 = (k + 0.25) / n, (k + 0.65) / n
        line(c, x1 + (x2 - x1) * u0, y1 + (y2 - y1) * u0, x1 + (x2 - x1) * u1, y1 + (y2 - y1) * u1, "#FFFFFF", a, 5)


def cruzamento(c, cx, cy, w, a):
    if a <= 0:
        return
    _rua(c, cx - w / 2, cy - 90, cx + w / 2, cy + 90, a)
    _rua(c, cx - w / 2, cy + 90, cx + w / 2, cy - 90, a)
    c.drawCircle(cx, cy, 16, paint(PURPLE, a))


def rua_dupla(c, cx, cy, w, a, u):
    """uma rua e a mesma rua desenhada de novo, descendo até ficar em cima (u = 0..1)"""
    if a <= 0:
        return
    _rua(c, cx - w / 2, cy + 50, cx + w / 2, cy - 50, a)
    off = (1 - u) * 70
    c.save(); c.translate(0, -off)
    line(c, cx - w / 2, cy + 50, cx + w / 2, cy - 50, PURPLE, a * 0.55, 14)
    c.restore()


def caixas(c, cx, cy, fracs, sinais, a, size=48, alfas=None, cores=None, gap=70):
    """as razões em caixinhas lado a lado: fracs = [(num, den)], sinais entre elas ('=' ou '≠', '' esconde);
    alfas = alfa de cada caixa; cores = cor de cada caixa. Devolve a largura total."""
    if a <= 0:
        return 0
    n = len(fracs)
    bw = max(K.fr_w(nm, dn, size) for nm, dn in fracs) + 60
    tot = n * bw + (n - 1) * gap
    x = cx - tot / 2
    for k, (nm, dn) in enumerate(fracs):
        al = a * (alfas[k] if alfas else 1)
        col = (cores[k] if cores else None) or PURPLE
        if al > 0:
            rrect(c, x, cy - size * 1.15, bw, size * 2.5, 18, mix("#FFFFFF", col, 0.10), al)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - size * 1.15, bw, size * 2.5), 18, 18),
                        paint(col, al, stroke=3))
            fr(c, nm, dn, x + bw / 2, cy - size * 0.05, size, INK, al)
        if k < n - 1 and k < len(sinais) and sinais[k]:
            sg, sal = sinais[k] if isinstance(sinais[k], tuple) else (sinais[k], 1.0)
            if sal > 0:
                fmid(c, sg, x + bw + gap / 2, cy + size * 0.1, size * 1.1, "black", GREEN if sg == "=" else RED, a * sal)
        x += bw + gap
    return tot


def mini(c, cx, cy, s, a, tipo, t=0.0):
    """uma das três situações num plano pequeno: 'conc', 'par', 'coin'"""
    if tipo == "conc":
        plano(c, cx, cy, s, a, [(1, 1, 5, COR_R, 1, 0), (1, -1, -1, COR_S, 1, 0)], [(2, 3, PURPLE, 1, "")], num=False)
    elif tipo == "par":
        plano(c, cx, cy, s, a, [(1, 2, 4, COR_R, 1, 0), (2, 4, 10, COR_S, 1, 0)], num=False)
    else:
        plano(c, cx, cy, s, a, [(1, 2, 4, COR_R, 1, 0), (2, 4, 8, PURPLE, 1, t)], num=False)


def _passos(c, t, rows, x, y0, size, dy):
    for k, (t0, ex, nota, col) in enumerate(rows):
        a, d = rise(t, t0)
        if a <= 0:
            continue
        y = y0 + k * dy + d
        expr(c, ex, x, y, size, a, align="left", cores={i: col for i in range(30)} if col in (RED, GREEN) else None)
        if nota:
            text(c, nota, x, y + size * 0.85, 22, "bold", GRAY, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "SISTEMAS · EPISÓDIO 3", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    rows = [(C["01.a"], "x + 2y = 4", "", None), (C["01.a"] + 0.8, "2x + 4y = 10", "", None)]
    _passos(c, t, rows, 330, 330, 66, 110)
    a3 = ep(t, C["01.a"] + 2.4, 0.5)
    if a3 > 0:
        line(c, 320, 470, 820, 470, INK, a3, 4)
        expr(c, "0 = 2", 570, 560, 110, a3, cores={0: RED, 1: RED, 2: RED})
    if ab > 0:
        mv = ep(t, C["01.b"], 1.6)
        ex = 300 + 600 * mv
        c.save(); c.translate(ex, 450); c.rotate(-18)
        rrect(c, -70, -40, 140, 80, 14, "#F2B8C6", ab, shadow=True)
        rrect(c, -70, 10, 140, 30, 10, "#5B7DB1", ab)
        c.restore()
        text(c, "apagar tudo?", 570, 700, 40, "black", AMBER, ab * (1 - ep(t, C["01.c"], 0.4)))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        boxed(c, 980, 260, 680, 520, GREEN, acc, 0.06)
        text(c, "NÃO ERROU", 1320, 340, 54, "black", GREEN, acc)
        trilhos(c, 1320, 500, 520, acc)
        text(c, "a conta diz:", 1320, 640, 32, "bold", GRAY, acc)
        text(c, "NÃO EXISTE RESPOSTA", 1320, 710, 46, "black", INK, acc)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    aa = ep(t, C["02.a"], 0.5)
    for k, (s, sub, col) in enumerate((("UMA", "solução", BLUE), ("NENHUMA", "solução", RED), ("INFINITAS", "soluções", PURPLE))):
        ak = aa * ep(t, C["02.a"] + 0.5 + 0.7 * k, 0.4)
        if ak <= 0:
            continue
        x = 480 + k * 480
        rrect(c, x - 200, 280, 400, 240, 26, mix("#FFFFFF", col, 0.12), ak)
        text(c, s, x, 395, 64 if k else 72, "black", col, ak)
        text(c, sub, x, 460, 32, "bold", GRAY, ak)
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 680, ab, "MUITAS VEZES SEM RESOLVER NADA", GREEN, -3, 44)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "MÉTODO DA ADIÇÃO", 560, 290, 34, "black", PURPLE, aa)
        text(c, "episódio 2", 560, 334, 24, "bold", GRAY, aa)
        text(c, "multiplique a equação INTEIRA", 560, 410, 28, "bold", INK2, aa)
        text(c, "some ou subtraia: uma letra some", 560, 455, 28, "bold", INK2, aa)
        expr(c, "x + y = 5", 560, 560, 56, aa)
        expr(c, "x − y = −1", 560, 640, 56, aa)
        expr(c, "2x = 4", 560, 735, 56, ep(t, C["03.a"] + 3.0, 0.4), cores={0: GREEN, 1: GREEN, 2: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "OS FRETES", 1360, 290, 34, "black", BLUE, ab)
        text(c, "Equações do 1º grau", 1360, 334, 24, "bold", GRAY, ab)
        text(c, "R$ 40 + R$ 3 por km  ×  R$ 36 + R$ 3 por km", 1360, 430, 26, "bold", INK2, ab)
        expr(c, "40 + 3x = 3x + 36", 1360, 560, 56, ab)
        a2 = ep(t, C["03.b"] + 4.5, 0.4)
        expr(c, "0x = −4", 1360, 660, 64, a2, cores={0: RED, 1: RED, 2: RED})
        if a2 > 0:
            pill(c, "nunca empatam", 1360, 745, RED, size=26, a=a2, anchor="center")
    line(c, 960, 250, 960, 790, "#E6E6E2", ab, 3)


# ======================================================================
# concreto e a estrada de soluções
# ======================================================================

def b_concreto(c, t, C, B):
    frame(c, t, B["start"], "TRÊS CENAS DA RUA", "QUANTOS PONTOS EM COMUM?", BLUE)
    itens = [("04.a", "TRILHOS", "nunca se encontram", "0 pontos", RED),
             ("04.b", "CRUZAMENTO", "um único ponto", "1 ponto", BLUE),
             ("04.c", "A MESMA RUA 2 VEZES", "todos os pontos", "infinitos", PURPLE)]
    for k, (cue, tit, sub, n, col) in enumerate(itens):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 240, 240, 480, 540, 26, "#FFFFFF", a, shadow=True)
        text(c, tit, x, 310, 32 if k < 2 else 28, "black", col, a)
        if k == 0:
            trilhos(c, x, 470, 400, a)
        elif k == 1:
            cruzamento(c, x, 470, 380, a)
        else:
            rua_dupla(c, x, 470, 380, a, ep(t, C[cue] + 1.2, 1.4))
        text(c, sub, x, 640, 30, "bold", INK2, a)
        pill(c, n, x, 715, col, size=30, a=a, anchor="center")


def b_estrada(c, t, C, B):
    frame(c, t, B["start"], "CADA EQUAÇÃO", "UMA ESTRADA DE SOLUÇÕES", BLUE)
    aa = ep(t, C["05.a"], 0.5)
    pts = [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
    if aa > 0:
        expr(c, "x + y = 5", 470, 300, 64, aa, cores={i: COR_R for i in range(5)})
        for k, (x, y) in enumerate(pts[:3]):
            ak = ep(t, C["05.a"] + 1.4 + 0.9 * k, 0.4)
            if ak > 0:
                fmid(c, f"x = {x} · y = {y}", 470, 400 + k * 80, 42, "black", INK, ak)
        ak = ep(t, C["05.b"], 0.4)
        if ak > 0:
            text(c, "(3, 2) · (4, 1) · (5, 0) ...", 470, 640, 34, "black", GRAY, ak)
    ub = ep(t, C["05.b"] + 1.0, 1.5)
    uc = ep(t, C["05.c"], 1.2)
    pontos = [(x, y, COR_R, ep(t, C["05.a"] + 1.4 + 0.9 * min(k, 2) + (0 if k < 3 else C["05.b"] - C["05.a"] - 1.4), 0.4), "")
              for k, (x, y) in enumerate(pts)]
    hl = ep(t, C["05.c"] + 1.4, 0.4)
    pontos.append((2, 3, PURPLE, hl, "cruzamento (2, 3)"))
    plano(c, 1230, 500, 500, aa, [(1, 1, 5, COR_R, ub, 0), (1, -1, -1, COR_S, uc, 0)], pontos)
    if ub > 0.5:
        defin(c, "ESTRADA", "todos os pares que servem", 240, 670, 680, ep(t, C["05.b"] + 2.0, 0.4))
    if uc > 0:
        pill(c, "x − y = −1", 1450, 290, COR_S, size=26, a=uc, anchor="center")
        pill(c, "solução do sistema = o CRUZAMENTO", 580, 790, PURPLE, size=28, a=hl, anchor="center")


# ======================================================================
# bloco a — as três posições
# ======================================================================

def b_concorrentes(c, t, C, B):
    frame(c, t, B["start"], "1ª POSIÇÃO", "RETAS QUE SE CRUZAM", BLUE)
    rows = [(C["06.a"], "x + y = 5", "", None), (C["06.a"] + 1.4, "x − y = −1", "", None),
            (C["06.b"], "2x = 4", "somando: o y some", PURPLE), (C["06.b"] + 3.0, "x = 2 · y = 3", "", GREEN)]
    _passos(c, t, rows, 260, 290, 58, 100)
    acc = ep(t, C["06.c"], 0.5)
    plano(c, 1310, 450, 440, ep(t, C["06.a"], 0.5),
          [(1, 1, 5, COR_R, ep(t, C["06.a"], 1.0), 0), (1, -1, -1, COR_S, ep(t, C["06.a"] + 1.4, 1.0), 0)],
          [(2, 3, PURPLE, acc, "(2, 3)")])
    defin(c, "CONCORRENTES", "se cruzam num único ponto", 240, 700, 760, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 1050, 720, 520, 90, 20, mix("#FFFFFF", BLUE, 0.16), ad)
        linha(c, [("SPD", BLUE), (" · possível e determinado", INK)], 1310, 752, 28, ad)
        text(c, "UMA única solução", 1310, 795, 24, "black", GREEN, ad)


def b_paralelas(c, t, C, B):
    frame(c, t, B["start"], "2ª POSIÇÃO", "TRILHOS", RED)
    rows = [(C["07.a"], "x + 2y = 4", "", None), (C["07.a"] + 1.6, "2x + 4y = 10", "", None),
            (C["07.b"], "2x + 4y = 8", "o dobro da primeira", PURPLE)]
    _passos(c, t, rows, 260, 290, 58, 100)
    ab2 = ep(t, C["07.b"] + 3.4, 0.5)
    if ab2 > 0:
        line(c, 250, 575, 760, 575, INK, ab2, 4)
        text(c, "subtraindo", 770, 560, 22, "bold", GRAY, ab2, align="left")
        expr(c, "0 = 2", 420, 640, 76, ab2, cores={0: RED, 1: RED, 2: RED})
    acc = ep(t, C["07.c"], 0.5)
    plano(c, 1310, 450, 440, ep(t, C["07.a"], 0.5),
          [(1, 2, 4, COR_R, ep(t, C["07.a"], 1.0), 0), (2, 4, 10, COR_S, ep(t, C["07.a"] + 1.6, 1.0), 0)])
    if acc > 0:
        selo(c, 1440, 330, acc, "0 = 2", RED, -6, 40)
    defin(c, "PARALELAS", "lado a lado, sem ponto comum", 240, 700, 760, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 1050, 720, 520, 90, 20, mix("#FFFFFF", RED, 0.12), ad)
        linha(c, [("SI", RED), (" · sistema impossível", INK)], 1310, 752, 28, ad)
        text(c, "NENHUMA solução", 1310, 795, 24, "black", RED, ad)


def b_coincidentes(c, t, C, B):
    frame(c, t, B["start"], "3ª POSIÇÃO", "A MESMA ESTRADA DUAS VEZES", PURPLE)
    rows = [(C["08.a"], "x + 2y = 4", "", None), (C["08.a"] + 1.6, "2x + 4y = 8", "", None)]
    _passos(c, t, rows, 260, 290, 58, 100)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        text(c, "dobro da primeira − a segunda", 260, 500, 24, "bold", GRAY, ab, align="left")
        expr(c, "0 = 0", 420, 590, 76, ab, cores={0: PURPLE, 1: PURPLE, 2: PURPLE})
    acc = ep(t, C["08.c"], 0.5)
    pis = (t - C["08.c"]) if acc > 0 else 0
    pts = [(x, y, PURPLE, ep(t, C["08.c"] + 2.5 + 0.7 * k, 0.4), f"({x}, {y})") for k, (x, y) in enumerate(((4, 0), (2, 1), (0, 2)))]
    plano(c, 1310, 450, 440, ep(t, C["08.a"], 0.5),
          [(1, 2, 4, COR_R, ep(t, C["08.a"], 1.0), 0), (2, 4, 8, PURPLE, ep(t, C["08.a"] + 1.6, 1.0), pis)], pts)
    if acc > 0:
        selo(c, 1440, 330, acc, "0 = 0", PURPLE, -6, 40)
    defin(c, "COINCIDENTES", "a mesma reta, todos os pontos", 240, 700, 760, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 1050, 720, 520, 90, 20, mix("#FFFFFF", PURPLE, 0.12), ad)
        linha(c, [("SPI", PURPLE), (" · possível e indeterminado", INK)], 1310, 752, 28, ad)
        text(c, "INFINITAS soluções", 1310, 795, 24, "black", PURPLE, ad)


def b_painel(c, t, C, B):
    frame(c, t, B["start"], "LADO A LADO", "SÓ EXISTEM 3 POSIÇÕES", PURPLE)
    itens = [("09.a", "conc", "CONCORRENTES", "1 solução · SPD", BLUE, ""),
             ("09.b", "par", "PARALELAS", "nenhuma · SI", RED, "0 = 2"),
             ("09.c", "coin", "COINCIDENTES", "infinitas · SPI", PURPLE, "0 = 0")]
    for k, (cue, tp, tit, sub, col, sl) in enumerate(itens):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 440 + k * 520
        mini(c, x, 450, 330, a, tp, t - C[cue])
        text(c, tit, x, 680, 34, "black", col, a)
        text(c, sub, x, 728, 28, "bold", INK2, a)
        if sl:
            selo(c, x + 110, 330, a, sl, col, -6, 32)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        pill(c, "não existe 4ª posição", W / 2, 800, AMBER, size=28, a=ad, anchor="center")


# ======================================================================
# bloco b — preços
# ======================================================================

def b_precos(c, t, C, B):
    frame(c, t, B["start"], "NA PROVA", "MESMA TARIFA = TRILHOS", RED)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 250, 640, 110, 20, mix("#FFFFFF", COR_R, 0.10), aa)
        text(c, "FRETE 1:  R$ 40 + R$ 3 por km", 560, 318, 32, "black", COR_R, aa)
        rrect(c, 240, 380, 640, 110, 20, mix("#FFFFFF", COR_S, 0.10), aa)
        text(c, "FRETE 2:  R$ 36 + R$ 3 por km", 560, 448, 32, "black", COR_S, aa)
    ub = ep(t, C["10.b"], 1.4)
    plano(c, 1290, 470, 470, aa, [(-3, 1, 40, COR_R, ub, 0), (-3, 1, 36, COR_S, ub, 0)], xr=(0, 14), yr=(30, 86), passo=2,
          rot=("km", "R$"))
    ab = ep(t, C["10.b"] + 1.6, 0.4)
    if ab > 0:
        pill(c, "sobem juntas · sempre R$ 4 acima", 1290, 780, AMBER, size=26, a=ab, anchor="center")
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        text(c, "quando custam o mesmo?", 560, 570, 34, "black", INK, acc)
        expr(c, "0x = −4", 560, 660, 60, acc, cores={0: RED, 1: RED, 2: RED})
        text(c, "= um 0 = 2 disfarçado", 560, 750, 32, "black", RED, ep(t, C["10.c"] + 3.0, 0.4))


# ======================================================================
# bloco c — as razões
# ======================================================================

def b_razoes(c, t, C, B):
    frame(c, t, B["start"], "SEM RESOLVER", "AS TRÊS RAZÕES", PURPLE)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        linha(c, [("a₁", BLUE), ("x + ", INK), ("b₁", COR_S), ("y = ", INK), ("c₁", PURPLE)], W / 2, 280, 56, aa)
        linha(c, [("a₂", BLUE), ("x + ", INK), ("b₂", COR_S), ("y = ", INK), ("c₂", PURPLE)], W / 2, 370, 56, aa)
        defin(c, "COEFICIENTES", "os números de cada lugar", 560, 430, 800, ep(t, C["11.a"] + 2.5, 0.4))
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        defin(c, "RAZÃO ENTRE COEFICIENTES", "1ª ÷ 2ª, no mesmo lugar", 460, 520, 1000, ab)
    acc = ep(t, C["11.c"], 0.5)
    caixas(c, W / 2, 700, [("a₁", "a₂"), ("b₁", "b₂"), ("c₁", "c₂")], ["", ""], acc, 44,
           alfas=[ep(t, C["11.c"] + 0.8 * k, 0.4) for k in range(3)], cores=[BLUE, COR_S, PURPLE])


def b_regra(c, t, C, B):
    frame(c, t, B["start"], "A REGRA", "O QUE AS CAIXINHAS DIZEM", PURPLE)
    rows = [("12.a", [("1", "1"), ("1", "−1")], [("≠", 1)], "SPD · concorrentes", BLUE),
            ("12.b", [("1", "2"), ("2", "4"), ("4", "10")], [("=", 1), ("≠", 1)], "SI · paralelas", RED),
            ("12.c", [("1", "2"), ("2", "4"), ("4", "8")], [("=", 1), ("=", 1)], "SPI · coincidentes", PURPLE)]
    for k, (cue, fr_, sg, res, col) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        y = 300 + k * 180
        regra_txt = ["a ≠ b", "a = b ≠ c", "a = b = c"][k]
        if k == 0:
            text(c, "comparando as razões de", 260, y - 50, 22, "bold", GRAY, a, align="left")
        text(c, regra_txt, 260, y + 14, 36, "black", col, a, align="left")
        sg2 = [(s_, ep(t, C[cue] + 2.2 + 0.6 * j, 0.4)) for j, (s_, _) in enumerate(sg)]
        caixas(c, 920, y, fr_, sg2, a, 34, gap=56)
        pill(c, res, 1460, y, col, size=28, a=ep(t, C[cue] + 3.0, 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco d — em palavras (atalho do fator)
# ======================================================================

def b_palavras(c, t, C, B):
    frame(c, t, B["start"], "EM PALAVRAS", "MÚLTIPLA SÓ À ESQUERDA × INTEIRA", PURPLE)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 240, 680, 230, 22, mix("#FFFFFF", RED, 0.08), aa)
        text(c, "SÓ À ESQUERDA → PARALELAS", 580, 290, 28, "black", RED, aa)
        expr(c, "x + 2y = 4", 580, 338, 40, aa)
        expr(c, "2x + 4y = 10", 580, 392, 40, aa, cores={4: RED})
        pill(c, "× 2 ... mas 2 · 4 = 8 ≠ 10", 580, 448, RED, size=22, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 240, 680, 230, 22, mix("#FFFFFF", PURPLE, 0.08), ab)
        text(c, "INTEIRA → A MESMA RETA", 1340, 290, 28, "black", PURPLE, ab)
        expr(c, "x + 2y = 4", 1340, 338, 40, ab)
        expr(c, "2x + 4y = 8", 1340, 392, 40, ab, cores={4: GREEN})
        pill(c, "× 2 em tudo", 1340, 448, PURPLE, size=22, a=ab, anchor="center", bounds=(0, 1920))
    acc = ep(t, C["13.c"], 0.5)
    K.atalho(c, 240, 495, 1440, 255, "ATALHO · ACHE O FATOR",
             ["divida um número da 2ª pelo da 1ª: 2 ÷ 1 = 2", "teste o fator nos outros: 2 · 2 = 4 ✓",
              "o lado direito POR ÚLTIMO: 2 · 4 = 8 ?"], acc, 34)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 795, ad, "O LADO DIREITO SEPARA PARALELAS DE COINCIDENTES", GREEN, -2, 26)


# ======================================================================
# bloco e — parâmetro · bloco f — determinante
# ======================================================================

def b_parametro(c, t, C, B):
    frame(c, t, B["start"], "PARÂMETRO", "UMA LETRA A MAIS", BLUE)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        expr(c, "3x + 2y = 7", 560, 290, 56, aa)
        expr(c, "6x + ky = 14", 560, 380, 56, aa, cores={2: AMBER})
        defin(c, "PARÂMETRO", "um número que a questão deixou para você escolher", 240, 450, 1440,
              ep(t, C["14.a"] + 2.6, 0.4))
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "infinitas soluções = múltipla INTEIRA", 1300, 300, 30, "black", PURPLE, ab)
        caixas(c, 1300, 375, [("3", "6"), ("7", "14")], [("=", ep(t, C["14.b"] + 3.5, 0.4))], ab, 30, gap=60)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        K.atalho(c, 240, 560, 860, 240, "ATALHO · O FATOR VEM DO PAR COMPLETO",
                 ["6 = 2 · 3   e   14 = 2 · 7  →  fator 2", "k = 2 · 2 = 4"], acc, 32)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 1140, 560, 540, 240, 22, mix("#FFFFFF", BLUE, 0.10), ad)
        text(c, "k = 4", 1410, 630, 46, "black", PURPLE, ad)
        text(c, "infinitas soluções (SPI)", 1410, 680, 26, "bold", INK2, ad)
        text(c, "qualquer outro k", 1410, 740, 30, "black", BLUE, ad)
        text(c, "uma única solução (SPD)", 1410, 780, 26, "bold", INK2, ad)


def b_determinante(c, t, C, B):
    frame(c, t, B["start"], "SÓ PARA CITAR", "O DETERMINANTE", GRAY)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        text(c, "DETERMINANTE", W / 2, 360, 72, "black", INK2, aa)
        text(c, "outro jeito de fazer a mesma classificação", W / 2, 430, 32, "bold", GRAY, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        pill(c, "série própria: Determinantes e sistemas lineares", W / 2, 560, PURPLE, size=32, a=ab, anchor="center")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 700, acc, "AQUI: AS RAZÕES RESOLVEM", GREEN, -3, 40)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "CLASSIFIQUE", GREEN), ("17", "VAMOS JUNTOS", "AS TRÊS RAZÕES", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        expr(c, "x − 3y = 2", 520, 280, 54, aa)
        c5 = ep(t, C["17.c"], 0.4)
        expr(c, "−2x + 6y = −4", 520, 370, 54, aa * (1 - c5))
        if c5 > 0:
            expr(c, "−2x + 6y = 5", 520, 370, 54, c5, cores={4: RED})
    ab = ep(t, C["16.b"], 0.5) * (1 - ep(t, C["17"], 0.4))
    if ab > 0:
        rrect(c, 1000, 240, 660, 150, 22, mix("#FFFFFF", AMBER, 0.12), ab)
        text(c, "e se o lado direito", 1330, 300, 32, "black", INK, ab)
        text(c, "da 2ª fosse 5?", 1330, 352, 32, "black", AMBER, ab)
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 600)
    if t < C["17"]:
        return
    a1 = ep(t, C["17.a"], 0.5)
    sg = [("=", ep(t, C["17.a"] + 4.0, 0.4)), ("=", ep(t, C["17.a"] + 4.4, 0.4))]
    c5 = ep(t, C["17.c"], 0.4)
    if c5 <= 0:
        caixas(c, 760, 560, [("1", "−2"), ("−3", "6"), ("2", "−4")], sg, a1, 40, gap=60)
    else:
        caixas(c, 760, 560, [("1", "−2"), ("−3", "6"), ("2", "5")], [("=", 1), ("≠", c5)], c5, 40, gap=60,
               cores=[None, None, RED])
    if a1 > 0:
        text(c, "todas valem −1/2", 760, 720, 32, "black", PURPLE, a1 * ep(t, C["17.a"] + 4.8, 0.4) * (1 - c5))
    a2 = ep(t, C["17.b"], 0.5) * (1 - c5)
    if a2 > 0:
        rrect(c, 1280, 470, 400, 200, 22, mix("#FFFFFF", PURPLE, 0.12), a2)
        text(c, "SPI", 1480, 545, 54, "black", PURPLE, a2)
        text(c, "coincidentes · fator −2", 1480, 610, 26, "bold", INK2, a2)
    if c5 > 0:
        rrect(c, 1280, 470, 400, 200, 22, mix("#FFFFFF", RED, 0.10), c5)
        text(c, "SI", 1480, 545, 54, "black", RED, c5)
        text(c, "paralelas · 2/5 ≠ −1/2", 1480, 610, 26, "bold", INK2, c5)
        text(c, "múltipla só à esquerda", 760, 730, 30, "black", RED, ep(t, C["17.c"] + 3.0, 0.4))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Concorrentes: uma solução. Paralelas: nenhuma. Coincidentes: infinitas.",
          "0 = 2 é impossível; 0 = 0 é infinitas.",
          "Múltipla só à esquerda, paralelas; múltipla inteira, a mesma reta."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Sobrou 0 = 2: “errei a conta”", "zero nunca é igual a dois, então parece engano",
          "o absurdo É a resposta: nenhum par serve nas duas · sistema impossível (SI)"),
         ("Sobrou 0 = 0: “a solução é x = 0 e y = 0”", "só aparece o zero na tela",
          "0 = 0 é sempre verdade: qualquer ponto da estrada serve · infinitas soluções (SPI)"),
         ("x − 3y = 2 e −2x + 6y = 5: “a mesma reta”", "os números das letras batem (fator −2)",
          "faltou o lado direito: −2 · 2 = −4, não 5 · são PARALELAS")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões 6 e 3 do material
# ======================================================================

def _enunciado(c, s, a, y0=250, size=29, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS6 = [("A", "concorrentes · 1 solução", "ignora a inclinação", RED),
         ("B", "coincidentes · infinitas", "só com 8 à direita", AMBER),
         ("C", "perpendiculares · 1 solução", "ignora a inclinação", RED),
         ("D", "concorrentes na origem · (0, 0)", "0 + 0 ≠ 4", RED),
         ("E", "paralelas distintas · sem solução", "", GREEN)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · EU FAÇO", "POSIÇÃO DE DUAS RETAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4) * (1 - ep(t, C["23"], 0.4))
    yend = _enunciado(c, "Um estudante representou no plano cartesiano as retas r: x + 2y = 4 e s: 2x + 4y = 10, para resolver "
                         "graficamente o sistema formado por elas. Ele deve concluir que as retas são", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["24.xa"], "B": C["24.xb"], "C": C["24.xc"], "D": C["24.xd"]}
    K.alternativas(c, t, C, ALTS6, 1000, 260, 680, 30, C["23.ok"], "E", cues_in, cues_x, gap=40)
    pause_timer(c, t, C["22.end"] - 1.9, 540, yend + 100)
    if t >= C["23"]:
        ap = ep(t, C["23"], 0.4)
        _painel(c, ap)
        text(c, "as três razões de r e s", 550, 285, 26, "black", PURPLE, ap)
        aa = ep(t, C["23.a"], 0.4)
        caixas(c, 550, 380, [("1", "2"), ("2", "4"), ("4", "10")],
               [("=", ep(t, C["23.a"] + 3.5, 0.4)), ("≠", ep(t, C["23.a"] + 5.0, 0.4))], aa, 34, gap=46)
        ab = ep(t, C["23.b"], 0.4)
        if ab > 0:
            rrect(c, 200, 510, 700, 110, 18, mix("#FFFFFF", PURPLE, 0.10), ab)
            text(c, "esquerda: × 2  ·  direita: 2 · 4 = 8 ≠ 10", 550, 578, 26, "black", INK, ab)
        acc = ep(t, C["23.c"], 0.4)
        if acc > 0:
            rrect(c, 200, 645, 700, 160, 18, mix("#FFFFFF", RED, 0.08), acc)
            text(c, "adição: s − 2r", 550, 690, 26, "bold", GRAY, acc)
            expr(c, "0 = 2", 550, 755, 56, acc, cores={0: RED, 1: RED, 2: RED})
    if t >= C["24"]:
        apx = ep(t, C["24.xc"], 0.4)
        if apx > 0:
            selo(c, 1340, 795, apx, "PERPENDICULAR: CRUZA EM CANTO RETO, COMO UM L", BLUE, -2, 22)


ALTS3 = [("A", "6", "", GREEN),
         ("B", "−6", "trocou o sinal", RED),
         ("C", "3", "copiou o 3", RED),
         ("D", "12", "multiplicou por 4", RED),
         ("E", "qualquer valor diferente de 6", "1 solução", AMBER)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · VOCÊ FAZ", "INFINITAS SOLUÇÕES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4) * (1 - ep(t, C["26"], 0.4))
    yend = _enunciado(c, "Um aplicativo resolve sistemas lineares e informa quando há infinitas soluções. Um usuário digitou o "
                         "sistema formado por 2x + 3y = 5 e 4x + ky = 10 e recebeu a mensagem “infinitas soluções”. "
                         "O valor de k digitado foi", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS3, 1000, 270, 680, 34, C["26.ok"], "A", cues_in, cues_x, gap=40)
    pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 100)
    if t >= C["26"]:
        ap = ep(t, C["26"], 0.4)
        _painel(c, ap)
        text(c, "INFINITAS → múltipla INTEIRA", 550, 285, 26, "black", PURPLE, ap)
        aa = ep(t, C["26.a"], 0.4)
        if aa > 0:
            expr(c, "2x + 3y = 5", 550, 370, 46, aa)
            expr(c, "4x + ky = 10", 550, 440, 46, aa, cores={2: AMBER})
            K.atalho(c, 200, 490, 700, 150, "O FATOR VEM DO PAR COMPLETO", ["4 = 2 · 2   e   10 = 2 · 5  →  × 2"], aa, 28)
        ab = ep(t, C["26.b"], 0.4)
        if ab > 0:
            rrect(c, 200, 660, 700, 150, 18, mix("#FFFFFF", GREEN, 0.12), ab)
            text(c, "k = 2 · 3 = 6", 550, 725, 46, "black", GREEN, ab)
            text(c, "razões: 1/2 = 1/2 = 1/2", 550, 780, 26, "bold", INK2, ep(t, C["26.b"] + 2.0, 0.4))
    ax = ep(t, C["27.xd"] + 2.5, 0.4)
    if ax > 0:
        selo(c, 1340, 760, ax, "−6, 3 OU 12: CONCORRENTES", RED, -2, 26)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TRÊS INCÓGNITAS", PURPLE)
    itens = [("29.a", "Ana + Beto = 125 kg", BLUE), ("29.b", "Beto + Caio = 145 kg", COR_S), ("29.c", "Ana + Caio = 140 kg", PURPLE)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        y = 300 + k * 120 + d
        rrect(c, 560, y - 50, 800, 96, 22, mix("#FFFFFF", col, 0.12), a)
        text(c, s, W / 2, y + 14, 46, "black", col, a)
    ad = ep(t, C["29.d"], 0.5)
    if ad > 0:
        text(c, "Beto = ?", W / 2, 700, 64, "black", INK, ad)
    ae = ep(t, C["29.e"], 0.5)
    if ae > 0:
        selo(c, W / 2, 790, ae, "UM ATALHO EM DUAS LINHAS", GREEN, -3, 36)


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Você já apagou uma conta que deu 0 = 2?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, estrada=b_estrada,
              concorrentes=b_concorrentes, paralelas=b_paralelas, coincidentes=b_coincidentes, painel=b_painel,
              precos=b_precos, razoes=b_razoes, regra=b_regra, palavras=b_palavras, parametro=b_parametro,
              determinante=b_determinante, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q6=b_q6, q3=b_q3,
              ponte=b_ponte, cta=b_cta)
