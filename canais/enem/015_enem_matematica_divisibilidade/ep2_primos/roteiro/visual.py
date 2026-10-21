"""Visual — Divisibilidade, Primos, MMC e MDC, Episódio 2: Números primos — os tijolos de todos os números (tema claro).
Animações: quadradinhos que tentam formar retângulos (o primo falha e fica em fila; o composto forma vários),
TIJOLOS (primos) e CONSTRUÇÕES (compostos), o CRIVO de 1 a 100 com os múltiplos de 2, 3, 5 e 7 riscados em cores e os
primos acendendo, e a RÉGUA da raiz no teste do 181 (13,4 = linha de chegada).
Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
"""
import math
from functools import lru_cache
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisibilidade_ep2_primos.mp4"
CARD_R = (140, 150, 1640, 690)
SYM = "C:/Windows/Fonts/seguisym.ttf"
BRICK = "#C8553D"          # tijolo
SQ = "#3B6CF6"             # quadradinho
CRIVO_COR = {2: "#E5484D", 3: "#E8A317", 5: "#7C5CFA", 7: "#3B6CF6"}


# ======================================================================
# texto com símbolos que a Inter não tem (√, ≈) — cai para a Segoe UI Symbol só nesses caracteres
# ======================================================================

@lru_cache(None)
def _symfont(size):
    f = skia.Font(skia.Typeface.MakeFromFile(SYM), size)
    f.setEmbolden(True); f.setSubpixel(True); f.setEdging(skia.Font.Edging.kAntiAlias)
    return f


@lru_cache(None)
def _has(ch, peso):
    return font(peso, 40).textToGlyphs(ch)[0] != 0


def _pieces(s, peso, size):
    cur, cur_sym = "", None
    for ch in s:
        sym = not _has(ch, peso)
        if cur and sym != cur_sym:
            yield cur, (_symfont(size) if cur_sym else font(peso, size))
            cur = ""
        cur += ch; cur_sym = sym
    if cur:
        yield cur, (_symfont(size) if cur_sym else font(peso, size))


def ftext_w(s, peso, size):
    return sum(f.measureText(p) for p, f in _pieces(s, peso, size))


def ftext(c, s, x, y, size, peso="black", color=None, a=1.0, align="center"):
    if a <= 0:
        return 0
    color = INK if color is None else color
    w = ftext_w(s, peso, size)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p, f in _pieces(s, peso, size):
        c.drawString(p, xx, y, f, paint(color, a))
        xx += f.measureText(p)
    return w


# ======================================================================
# peças gerais
# ======================================================================

def frame(c, t, t0, l1, l2, col):
    head(c, t, t0, l1, l2, col)
    card(c, *CARD_R)


def which(t, C, ids):
    cur = ids[0]
    for i in ids:
        if t >= C[i] - 0.05:
            cur = i
    return cur


def head_seq(c, t, C, heads):
    sid = which(t, C, [h[0] for h in heads])
    for h in heads:
        if h[0] == sid:
            head(c, t, C[sid], h[1], h[2], h[3])


def boxed(c, x, y, w, h, col, a, fill=0.10, r=22, sw=4):
    if a <= 0:
        return
    rrect(c, x, y, w, h, r, col, fill * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), paint(col, a, stroke=sw))


def defbox(c, cx, y, titulo, txt, col, a, w=1100, size=34):
    """caixa de definição: título colorido + frase"""
    if a <= 0:
        return
    boxed(c, cx - w / 2, y, w, 130, col, a, 0.07)
    text(c, titulo, cx - w / 2 + 36, y + 48, 24, "black", col, a, align="left", tracking=2)
    text(c, txt, cx - w / 2 + 36, y + 100, size, "black", INK, a, align="left")


def selo(c, x, y, a, s, col=None, rot=-6, size=32):
    if a <= 0:
        return
    col = col or AMBER
    c.save(); c.translate(x, y); c.rotate(rot)
    w = text_w(s, "black", size) + 50
    sc = 0.8 + 0.2 * ease_back(clamp(a))
    c.scale(sc, sc)
    boxed(c, -w / 2, -size, w, size * 2, col, a, 0.15, 12, 5)
    text_mid(c, s, 0, 0, size, "black", col, a)
    c.restore()


def pause_timer(c, t, t0, x, y, a=1.0, dur=1.6, r=44):
    u = clamp((t - t0) / dur)
    ap = a * ep(t, t0, 0.3) * (1 - prog(t, t0 + dur + 0.4, 0.4))
    if ap <= 0:
        return
    c.drawCircle(x, y, r + 14, paint(AMBER, ap * 0.18))
    c.drawCircle(x, y, r, paint("#FFFFFF", ap))
    c.drawArc(skia.Rect.MakeLTRB(x - r, y - r, x + r, y + r), -90, 360 * (1 - u), False, paint(AMBER, ap, stroke=10, cap_round=True))
    c.drawRect(skia.Rect.MakeXYWH(x - 15, y - 20, 10, 40), paint(INK, ap)); c.drawRect(skia.Rect.MakeXYWH(x + 5, y - 20, 10, 40), paint(INK, ap))
    text(c, "PAUSE", x, y + r + 40, 26, "black", AMBER, ap)


def chip(c, s, cx, cy, col, a, size=34, fill=True):
    if a <= 0:
        return
    w = max(size * 1.7, ftext_w(s, "black", size) + size * 0.9)
    h = size * 1.6
    if fill:
        rrect(c, cx - w / 2, cy - h / 2, w, h, 14, col, a, shadow=True)
        ftext(c, s, cx, cy + size * 0.36, size, "black", on(col), a)
    else:
        boxed(c, cx - w / 2, cy - h / 2, w, h, col, a, 0.10, 14, 3)
        ftext(c, s, cx, cy + size * 0.36, size, "black", col, a)


# ======================================================================
# quadradinhos que se rearranjam
# ======================================================================

def layout(n, cols, cx, cy, cell):
    """posições (centro) de n quadradinhos em linhas de 'cols', centradas em (cx, cy)"""
    rows = math.ceil(n / cols)
    w, h = cols * cell, rows * cell
    out = []
    for k in range(n):
        r, q = divmod(k, cols)
        out.append((cx - w / 2 + q * cell + cell / 2, cy - h / 2 + r * cell + cell / 2))
    return out


def quads(c, pos, cell, a, col=SQ, bad=None):
    """bad = índices destacados em vermelho (o quadradinho que sobra)"""
    if a <= 0:
        return
    s = cell * 0.86
    for k, (x, y) in enumerate(pos):
        cc = RED if bad and k in bad else col
        rrect(c, x - s / 2, y - s / 2, s, s, s * 0.18, cc, a, shadow=True)


def morph(p0, p1, u):
    u = ease_out(clamp(u))
    return [(lerp(a[0], b[0], u), lerp(a[1], b[1], u)) for a, b in zip(p0, p1)]


# ======================================================================
# tijolos
# ======================================================================

def tijolo(c, x, y, w, h, label, a, col=BRICK, size=None):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 8, col, a, shadow=True)
    line(c, x + 8, y + h * 0.5, x + w - 8, y + h * 0.5, mix(col, "#000000", 0.18), a * 0.5, 2)
    line(c, x + w * 0.5, y + 6, x + w * 0.5, y + h * 0.5, mix(col, "#000000", 0.18), a * 0.5, 2)
    text_mid(c, str(label), x + w / 2, y + h / 2, size or h * 0.55, "black", "#FFFFFF", a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "NÚMEROS PRIMOS · EPISÓDIO 2", BLUE)
    for k, (cue, n) in enumerate((("01.a", "1"), ("01.b", "2"))):
        a, d = rise(t, C[cue])
        x = W / 2 - 330 + k * 660
        card(c, x - 240, 220 + d, 480, 380, a)
        text(c, n, x, 450 + d, 200, "black", BLUE, a)
        text(c, "é primo?", x, 550 + d, 46, "black", INK2, a)
    ac = ep(t, C["01.c"], 0.5)
    selo(c, W / 2, 690, ac, "METADE ERRA AS DUAS", AMBER, -4, 40)
    pill(c, "em 7 minutos você nunca mais erra", W / 2, 820, GREEN, size=32, a=ep(t, C["01.d"], 0.4), anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "reconhecer os PRIMOS ATÉ 100"), ("02.b", "testar qualquer número com POUCAS divisões")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 380 + j * 180 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 54, "black", INK, a, align="left")


PARES36 = [("1", "36"), ("2", "18"), ("3", "12"), ("4", "9"), ("6", "6")]


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO, RAPIDINHO", "DIVISORES E RAIZ QUADRADA", BLUE)
    aa = ep(t, C["03.a"], 0.4)
    text(c, "DIVISOR = divide certinho, sem sobrar", 220, 230, 30, "black", BLUE, aa, align="left")
    for k, (p, q) in enumerate(PARES36):
        a = ep(t, C["03.b"] + 0.5 * k, 0.4)
        y = 320 + k * 88
        ftext(c, f"{p} × {q} = 36", 300, y, 46, "black", INK, a, align="left")
    ac = ep(t, C["03.c"], 0.5)
    boxed(c, 980, 200, 640, 140, BLUE, ac, 0.07)
    text(c, "RAIZ QUADRADA", 1020, 248, 22, "black", BLUE, ac, align="left", tracking=2)
    text(c, "o número que, vezes ele mesmo, dá o número", 1020, 300, 26, "bold", INK, ac, align="left")
    ad = ep(t, C["03.d"], 0.5)
    ftext(c, "√36 = 6", 1300, 430, 70, "black", PURPLE, ad)
    quads(c, layout(36, 6, 1300, 610, 34), 34, ad)
    text(c, "6 × 6 = 36", 1300, 800, 32, "black", INK2, ad)


# ======================================================================
# fila × retângulo
# ======================================================================

def b_fila(c, t, C, B):
    frame(c, t, B["start"], "O DESAFIO", "QUE RETÂNGULOS DÁ PARA MONTAR?", BLUE)
    cell = 64
    # o seis
    a6 = ep(t, C["04.a"], 0.4)
    p_fila6 = layout(6, 6, 520, 420, cell)
    p_ret6 = layout(6, 3, 520, 420, cell)
    quads(c, morph(p_fila6, p_ret6, prog(t, C["04.b"], 0.8)), cell, a6)
    text(c, "6", 520, 280, 60, "black", INK, a6)
    lab6 = "1 × 6" if t < C["04.b"] + 0.4 else "2 × 3"
    pill(c, lab6, 520, 590, BLUE, size=30, a=a6, anchor="center", bounds=(0, 1920))
    # o sete
    a7 = ep(t, C["04.c"], 0.4)
    cx = 1300
    p_fila7 = layout(7, 7, cx, 420, cell)
    p_2 = layout(7, 4, cx, 420, cell)
    p_3 = layout(7, 3, cx, 420, cell)
    text(c, "7", cx, 280, 60, "black", INK, a7)
    if t < C["04.d"]:
        quads(c, p_fila7, cell, a7)
    elif t < C["04.e"]:
        quads(c, morph(p_fila7, p_2, prog(t, C["04.d"], 0.7)), cell, a7, bad={6} if t > C["04.d"] + 0.7 else None)
        pill(c, "sobra 1", cx, 590, RED, size=30, a=ep(t, C["04.d"] + 0.7, 0.3), anchor="center", bounds=(0, 1920))
    elif t < C["04.f"]:
        quads(c, morph(p_2, p_3, prog(t, C["04.e"], 0.7)), cell, a7, bad={6} if t > C["04.e"] + 0.7 else None)
        pill(c, "sobra 1", cx, 590, RED, size=30, a=ep(t, C["04.e"] + 0.7, 0.3), anchor="center", bounds=(0, 1920))
    else:
        quads(c, morph(p_3, p_fila7, prog(t, C["04.f"], 0.7)), cell, a7)
        pill(c, "só UMA fila", cx, 590, GREEN, size=30, a=ep(t, C["04.f"] + 0.4, 0.3), anchor="center", bounds=(0, 1920))


# ======================================================================
# primo, composto, o 1, o 2
# ======================================================================

def b_primo(c, t, C, B):
    frame(c, t, B["start"], "DEFINIÇÃO", "NÚMERO PRIMO", BLUE)
    defbox(c, W / 2, 200, "PRIMO", "exatamente 2 divisores: o 1 e ele mesmo", BLUE, ep(t, C["05.a"], 0.5))
    ab = ep(t, C["05.b"], 0.5)
    text(c, "um TIJOLO: não se quebra em pedaços menores", W / 2, 400, 34, "black", BRICK, ab)
    for k, n in enumerate((2, 3, 5, 7)):
        a = ep(t, C["05.c"] + 0.4 * k, 0.4)
        x = 380 + k * 390
        tijolo(c, x - 90, 450, 180, 100, n, a)
        quads(c, layout(n, n, x, 640, 30), 30, a)
        text(c, f"só 1 × {n}", x, 720, 26, "bold", INK2, a)


def b_composto(c, t, C, B):
    frame(c, t, B["start"], "DEFINIÇÃO", "NÚMERO COMPOSTO", BLUE)
    defbox(c, W / 2, 200, "COMPOSTO", "mais de 2 divisores", BLUE, ep(t, C["06.a"], 0.5))
    for k, n in enumerate((1, 2, 3, 6)):
        chip(c, str(n), 300 + k * 110, 420, BLUE, ep(t, C["06.b"] + 0.3 * k, 0.3), 34)
    text(c, "divisores do 6", 465, 500, 24, "bold", GRAY, ep(t, C["06.b"], 0.4))
    ac = ep(t, C["06.c"], 0.5)
    text(c, "uma CONSTRUÇÃO feita com tijolos", 1250, 380, 32, "black", BRICK, ac)
    tijolo(c, 1070, 440, 160, 90, 2, ac)
    text_mid(c, "×", 1250, 485, 50, "black", INK2, ac)
    tijolo(c, 1270, 440, 160, 90, 3, ac)
    text_mid(c, "= 6", 1510, 485, 50, "black", INK, ac)
    ad = ep(t, C["06.d"], 0.5)
    quads(c, layout(6, 6, 620, 680, 40), 40, ad)
    quads(c, layout(6, 3, 1250, 680, 50), 50, ad)
    text(c, "1 × 6", 620, 790, 26, "black", BLUE, ad)
    text(c, "2 × 3", 1250, 790, 26, "black", BLUE, ad)


def bin_(c, x, y, w, h, titulo, col, a):
    rrect(c, x, y, w, h, 20, mix("#FFFFFF", col, 0.08), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 20, 20), paint(col, a, stroke=3))
    text(c, titulo, x + w / 2, y + 44, 24, "black", col, a, tracking=2)


def b_um(c, t, C, B):
    frame(c, t, B["start"], "O CASO QUE DERRUBA GENTE", "O 1 É PRIMO?", AMBER)
    aa = ep(t, C["07.a"], 0.4)
    text(c, "1", 380, 470, 220, "black", INK, ep(t, C["07.t"], 0.4))
    selo(c, 380, 560, aa, "NÃO É PRIMO", RED, -6, 34)
    ab = ep(t, C["07.b"], 0.4)
    text(c, "divisores do 1:", 640, 300, 30, "bold", INK2, ab, align="left")
    chip(c, "1", 920, 290, BLUE, ab, 34)
    text(c, "só UM divisor", 990, 300, 32, "black", INK, ab, align="left")
    text(c, "a definição exige DOIS", 640, 380, 32, "black", RED, ep(t, C["07.c"], 0.4), align="left")
    ad = ep(t, C["07.d"], 0.4)
    text(c, "também não é composto", 640, 450, 32, "black", INK2, ad, align="left")
    ae = ep(t, C["07.e"], 0.5)
    bin_(c, 600, 530, 360, 260, "TIJOLOS", BRICK, ae)
    tijolo(c, 640, 620, 120, 70, 2, ae); tijolo(c, 780, 620, 120, 70, 3, ae)
    bin_(c, 990, 530, 360, 260, "CONSTRUÇÕES", BLUE, ae)
    chip(c, "4", 1080, 660, BLUE, ae, 34); chip(c, "6", 1180, 660, BLUE, ae, 34); chip(c, "9", 1280, 660, BLUE, ae, 34)
    bin_(c, 1380, 530, 240, 260, "À PARTE", AMBER, ae)
    text(c, "1", 1500, 720, 90, "black", AMBER, ae)


def b_dois(c, t, C, B):
    frame(c, t, B["start"], "O OUTRO CASO", "O 2 É PRIMO?", AMBER)
    aa = ep(t, C["08.a"], 0.4)
    tijolo(c, 260, 260, 260, 150, 2, ep(t, C["08.t"], 0.4))
    selo(c, 390, 480, aa, "É PRIMO", GREEN, -6, 34)
    text(c, "divisores:", 620, 300, 30, "bold", INK2, aa, align="left")
    chip(c, "1", 820, 290, BLUE, aa, 34); chip(c, "2", 920, 290, BLUE, aa, 34)
    text(c, "exatamente dois", 990, 300, 32, "black", GREEN, aa, align="left")
    pill(c, "o ÚNICO primo par", 900, 420, GREEN, size=34, a=ep(t, C["08.b"], 0.4), anchor="center", bounds=(0, 1920))
    ac = ep(t, C["08.c"], 0.4)
    text(c, "outro par: o 4", 620, 560, 32, "black", INK, ac, align="left")
    for k, n in enumerate((1, 2, 4)):
        chip(c, str(n), 960 + k * 110, 550, AMBER if n == 2 else BLUE, ac, 34)
    text(c, "o 2 é divisor EXTRA", 1300, 560, 28, "black", AMBER, ac, align="left")
    pill(c, "composto", 900, 700, BLUE, size=32, a=ep(t, C["08.d"], 0.4), anchor="center", bounds=(0, 1920))


# ======================================================================
# o crivo
# ======================================================================

def risco_de(n):
    """menor primo (2, 3, 5, 7) que risca n; 0 para primo; 1 para o próprio 1"""
    if n == 1:
        return 1
    for p in (2, 3, 5, 7):
        if n % p == 0 and n != p:
            return p
    return 0


PRIMOS100 = [n for n in range(2, 101) if risco_de(n) == 0]


def crivo(c, t, C, x0, y0, cell, a=1.0, acende=0.0, dim_pairs=0.0):
    if a <= 0:
        return
    tempos = {1: C["09.b"], 2: C["09.c"], 3: C["09.d"], 5: C["09.e"], 7: C["09.f"]}
    for n in range(1, 101):
        r, q = divmod(n - 1, 10)
        x, y = x0 + q * cell, y0 + r * cell
        p = risco_de(n)
        if p:
            t0 = tempos[p] + 0.6 + 0.012 * n
            u = prog(t, t0, 0.25)
            col = GRAY if p == 1 else CRIVO_COR[p]
            rrect(c, x + 3, y + 3, cell - 6, cell - 6, 8, "#FFFFFF", a)
            text_mid(c, str(n), x + cell / 2, y + cell / 2, cell * 0.38, "bold", mix(INK, LIGHT, u), a)
            if u > 0:
                line(c, x + 10, y + cell - 12, x + 10 + (cell - 20) * u, y + 12 + (cell - 24) * (1 - u), col, a, 4)
        else:
            on_ = acende
            rrect(c, x + 3, y + 3, cell - 6, cell - 6, 8, mix("#FFFFFF", GREEN, on_), a)
            text_mid(c, str(n), x + cell / 2, y + cell / 2, cell * 0.38, "black", mix(INK, "#FFFFFF", on_), a)


def b_crivo(c, t, C, B):
    sid = which(t, C, ["09", "10", "11"])
    head_seq(c, t, C, [("09", "A PENEIRA DOS PRIMOS", "O CRIVO DE 1 A 100", GREEN), ("10", "SOBRARAM", "OS 25 PRIMOS ATÉ 100", GREEN),
                       ("11", "DICA PARA NÃO ERRAR", "COMO TERMINAM OS PRIMOS", GREEN)])
    card(c, *CARD_R)
    cell = 62
    x0, y0 = 200, 180
    acende = ep(t, C["09.g"], 0.6) if sid == "09" else 1.0
    crivo(c, t, C, x0, y0, cell, ep(t, C["09.t"], 0.4), acende)
    xr = 900
    if sid == "09":
        text(c, "CRIVO = uma peneira", xr, 230, 30, "black", BLUE, ep(t, C["09.a"], 0.4), align="left")
        rows = [("09.b", "risque o 1", GRAY), ("09.c", "múltiplos de 2 (menos o 2)", CRIVO_COR[2]),
                ("09.d", "múltiplos de 3 (menos o 3)", CRIVO_COR[3]), ("09.e", "múltiplos de 5 (menos o 5)", CRIVO_COR[5]),
                ("09.f", "múltiplos de 7 (menos o 7)", CRIVO_COR[7])]
        for k, (cue, s, col) in enumerate(rows):
            a = ep(t, C[cue], 0.4)
            y = 320 + k * 80
            line(c, xr, y - 10, xr + 50, y - 10, col, a, 6)
            text(c, s, xr + 80, y, 32, "black", INK, a, align="left")
        pill(c, "quem sobrou aceso é PRIMO", xr + 330, 760, GREEN, size=30, a=ep(t, C["09.g"], 0.4), anchor="center", bounds=(0, 1920))
        return
    if sid == "10":
        text(c, "25 primos", xr + 340, 250, 56, "black", GREEN, 1.0)
        for k, p in enumerate(PRIMOS100):
            a = ep(t, C["10.a"] + 0.35 * k if k < 15 else C["10.b"] + 0.35 * (k - 15), 0.3)
            chip(c, str(p), xr + 70 + (k % 5) * 135, 340 + (k // 5) * 82, GREEN, a, 30)
        pill(c, "vale decorar", xr + 340, 790, PURPLE, size=30, a=ep(t, C["10.c"], 0.4), anchor="center", bounds=(0, 1920))
        return
    aa = ep(t, C["11.a"], 0.4)
    text(c, "nenhum termina em", xr + 340, 260, 34, "black", INK, aa)
    for k, d in enumerate("024568"):
        x = xr + 90 + k * 100
        chip(c, d, x, 360, LIGHT, aa, 40)
        strike(c, x - 30, 385, x + 30, 335, ep(t, C["11.a"] + 0.3 + 0.2 * k, 0.3), RED)
    ab = ep(t, C["11.b"], 0.4)
    text(c, "exceções:", xr + 340, 500, 30, "bold", INK2, ab)
    chip(c, "2", xr + 270, 590, GREEN, ab, 44); chip(c, "5", xr + 410, 590, GREEN, ab, 44)
    text(c, "(o próprio 2 e o 5)", xr + 340, 690, 28, "bold", GREEN, ab)


# ======================================================================
# o teste da raiz
# ======================================================================

def regua(c, x0, x1, y, a, lim=15, chegada=None, marcas=(), t=0.0):
    if a <= 0:
        return
    line(c, x0, y, x1, y, INK2, a, 4)
    X = lambda v: lerp(x0, x1, v / lim)
    for v in range(0, lim + 1):
        line(c, X(v), y - 10, X(v), y + 10, INK2, a, 2)
        text(c, str(v), X(v), y + 44, 22, "bold", GRAY, a)
    for v, al, col in marcas:
        c.drawCircle(X(v), y, 16, paint(col, a * al))
    if chegada:
        v, al = chegada
        xx = X(v)
        line(c, xx, y - 120, xx, y + 20, GREEN, a * al, 5)
        rrect(c, xx, y - 120, 70, 40, 4, GREEN, a * al)
        ftext(c, "√181 ≈ 13,4", xx, y - 140, 30, "black", GREEN, a * al)


def b_raiz(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head_seq(c, t, C, [("12", "O MÉTODO RÁPIDO", "DIVIDA SÓ ATÉ A RAIZ", PURPLE), ("13", "TESTANDO O 181", "A LINHA DE CHEGADA", PURPLE)])
    card(c, *CARD_R)
    if sid == "12":
        a0 = ep(t, C["12.t"], 0.4)
        text(c, "181 é primo?", 420, 260, 60, "black", INK, a0)
        boxed(c, 760, 200, 860, 130, PURPLE, ep(t, C["12.b"], 0.4), 0.08)
        text(c, "REGRA", 800, 248, 22, "black", PURPLE, ep(t, C["12.b"], 0.4), align="left", tracking=2)
        text(c, "teste os PRIMOS até a RAIZ QUADRADA", 800, 300, 34, "black", INK, ep(t, C["12.b"], 0.4), align="left")
        ac = ep(t, C["12.c"], 0.4)
        for k, (p, q) in enumerate(PARES36):
            a = ac * ep(t, C["12.c"] + 0.3 * k, 0.3)
            y = 430 + k * 72
            chip(c, p, 420, y, BLUE, a, 30)
            text_mid(c, "×", 520, y, 34, "black", INK2, a)
            chip(c, q, 620, y, BLUE, a, 30)
        ad = ep(t, C["12.d"], 0.4)
        boxed(c, 350, 430 + 4 * 72 - 40, 340, 80, GREEN, ad, 0.12)
        text(c, "os pares se encontram na RAIZ", 1180, 520, 34, "black", GREEN, ad)
        ftext(c, "√36 = 6", 1180, 600, 50, "black", GREEN, ad)
        text(c, "passou da raiz: nenhum par novo", 1180, 720, 32, "black", PURPLE, ep(t, C["12.e"], 0.4))
        return
    aa = ep(t, C["13.a"], 0.4)
    ftext(c, "13 × 13 = 169  <  181  <  196 = 14 × 14", W / 2, 230, 38, "black", INK2, aa)
    testes = [("13.c", 2, "ímpar"), ("13.d", 3, "1 + 8 + 1 = 10"), ("13.e", 5, "termina em 1"),
              ("13.f", 7, "sobra 6"), ("13.g", 11, "sobra 5"), ("13.h", 13, "sobra 12")]
    marcas = [(p, ep(t, C[cue], 0.3), RED) for cue, p, _ in testes]
    regua(c, 260, 1660, 400, ep(t, C["13.t"], 0.4), 15, (13.45, ep(t, C["13.b"], 0.4)), marcas, t)
    for k, (cue, p, why) in enumerate(testes):
        a = ep(t, C[cue], 0.3)
        x = 300 + (k % 3) * 470
        y = 540 + (k // 3) * 80
        ftext(c, f"÷ {p}", x, y, 34, "black", INK, a, align="left")
        check_icon(c, x + 110, y - 12, 18, a, RED, "x")
        text(c, why, x + 150, y, 28, "bold", INK2, a, align="left")
    ai = ep(t, C["13.i"], 0.4)
    selo(c, W / 2, 760, ai, "181 É PRIMO", GREEN, -3, 40)


def b_entresi(c, t, C, B):
    frame(c, t, B["start"], "UM NOME QUE CONFUNDE", "PRIMOS ENTRE SI", BLUE)
    defbox(c, W / 2, 200, "PRIMOS ENTRE SI", "o único divisor em comum é o 1", BLUE, ep(t, C["14.a"], 0.5))
    for row, (cue, n, ds) in enumerate((("14.b", "8", (1, 2, 4, 8)), ("14.c", "9", (1, 3, 9)))):
        a = ep(t, C[cue], 0.4)
        y = 420 + row * 120
        text(c, f"divisores do {n}:", 300, y + 12, 34, "black", INK, a, align="left")
        for k, d in enumerate(ds):
            hl = d == 1 and t >= C["14.d"]
            chip(c, str(d), 680 + k * 120, y, GREEN if hl else BLUE, a, 34)
    pill(c, "em comum: só o 1", 1400, 480, GREEN, size=32, a=ep(t, C["14.d"], 0.4), anchor="center", bounds=(0, 1920))
    ae = ep(t, C["14.e"], 0.4)
    boxed(c, 300, 690, 1320, 100, AMBER, ae, 0.10)
    text_mid(c, "8 e 9 são COMPOSTOS, mas são primos entre si", W / 2, 740, 34, "black", AMBER, ae)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Primo tem exatamente dois divisores.", "O 1 não é primo; o 2 é o único primo par.",
          "Para testar, divida pelos primos até a raiz."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["15", "25"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "15" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 50, "black", INK, a, align="left")


ERROS = [("16", "Achar que o 1 é primo", "ele só é divisível por 1 e por ele mesmo", "1 e ele mesmo são o MESMO número: um divisor só"),
         ("17", "Achar que o 2 não é primo “porque é par”", "todos os outros pares são compostos", "divisores do 2: 1 e 2, exatamente dois"),
         ("18", "Achar que todo ímpar é primo", "muitos primos são ímpares", "21 = 3·7 · 27 = 3·9 · 33 = 3·11 · 39 = 3·13"),
         ("19", "Testar divisões depois da raiz", "parece mais seguro", "depois da linha de chegada não aparece divisor novo")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 4", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(4):
        badge_num(c, k + 1, 840 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 330, 34, aa, RED, "x")
    text(c, err, 360, 345, 46, "black", RED, aa, align="left")
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 480, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 560, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 678, 34, ac, GREEN)
    text(c, fix, 360, 694, 40, "black", GREEN, ac, align="left")


# ======================================================================
# exercício 51 e 53
# ======================================================================

def b_exercicio(c, t, C, B):
    sid = which(t, C, ["20", "21"])
    head_seq(c, t, C, [("20", "SUA VEZ", "PAUSE E DIGA", GREEN), ("21", "CONFERINDO", "51 E 53", GREEN)])
    card(c, *CARD_R)
    for k, (cue, n) in enumerate((("20.a", "51"), ("20.b", "53"))):
        a = ep(t, C[cue], 0.4)
        x = 520 + k * 880
        text(c, n, x, 380, 150, "black", INK, a)
        if sid == "20":
            text(c, "é primo?", x, 460, 40, "black", INK2, a)
    if sid == "20":
        pause_timer(c, t, C["20.end"] - 1.9, W / 2, 620)
        return
    a = ep(t, C["21.a"], 0.4)
    ftext(c, "5 + 1 = 6 → divisível por 3", 520, 500, 34, "black", INK2, a)
    ab = ep(t, C["21.b"], 0.4)
    ftext(c, "51 = 3 × 17", 520, 600, 54, "black", RED, ab)
    selo(c, 520, 720, ab, "COMPOSTO", RED, -5, 34)
    ac = ep(t, C["21.c"], 0.4)
    ftext(c, "√53 ≈ 7,3 → testar 2, 3, 5, 7", 1400, 500, 32, "black", INK2, ac)
    ad = ep(t, C["21.d"], 0.4)
    for k, (p, why) in enumerate(((2, "ímpar"), (3, "soma 8"), (5, "termina em 3"), (7, "sobra 4"))):
        x = 1200 + (k % 2) * 260
        y = 570 + (k // 2) * 56
        ftext(c, f"÷{p}", x, y, 28, "black", INK, ad, align="left")
        text(c, why, x + 70, y, 24, "bold", GRAY, ad, align="left")
    selo(c, 1400, 740, ep(t, C["21.e"], 0.4), "PRIMO", GREEN, -5, 34)


# ======================================================================
# questão 7
# ======================================================================

ALTS = [("A", "2"), ("B", "3"), ("C", "4"), ("D", "5"), ("E", "6")]
CAND = {21: "3 · 7", 23: None, 27: "3 · 9", 29: None, 31: None, 33: "3 · 11", 37: None, 39: "3 · 13"}


def b_q7(c, t, C, B):
    sid = which(t, C, ["22", "23", "24"])
    head(c, t, B["start"], "QUESTÃO NO ESTILO ENEM", "NÚMEROS PRIMOS", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["22.a"], 0.4)
    pill(c, "QUESTÃO", 180, 210, BLUE, size=22, a=a, bounds=(0, 1920))
    text(c, "Quantos números primos existem entre 20 e 40?", 180, 290, 34, "black", INK, a, align="left")
    aok = ep(t, C["24.ok"], 0.4)
    for k, (L, v) in enumerate(ALTS):
        ak = ep(t, C[f"22.{'bcdef'[k]}"], 0.3)
        x = 1180 + k * 100
        ok = L == "C" and aok > 0
        if ok:
            rrect(c, x - 44, 236, 88, 120, 14, GREEN, 0.15 * aok)
        badge_num(c, L, x, 260, ak, 22, bg=GREEN if ok else INK)
        text(c, v, x, 340, 40, "black", GREEN if ok else INK, ak)
    pause_timer(c, t, C["22.end"] - 1.9, 1600, 650)
    if sid == "22":
        return
    # 21 a 39 numa faixa
    ae = ep(t, C["23.a"], 0.4)
    for k, n in enumerate(range(21, 40)):
        x = 220 + k * 79
        y = 470
        fora = (n % 2 == 0 or n % 10 == 5)
        fade = ae if fora else 0
        res = None
        if sid == "24" and n in CAND:
            cue = "24." + "abcdefgh"[sorted(CAND).index(n)]
            res = ep(t, C[cue], 0.3)
        col = LIGHT if fora else BLUE
        if res and res > 0:
            col = RED if CAND[n] else GREEN
        al = 1 - 0.75 * fade
        rrect(c, x - 34, y - 34, 68, 68, 12, mix("#FFFFFF", col, 0.9 if (res and res > 0) else (0.15 if not fora else 0.0)), al)
        text_mid(c, str(n), x, y, 28, "black", "#FFFFFF" if (res and res > 0) else (GRAY if fora else INK), al)
        if res and res > 0 and CAND[n]:
            text(c, CAND[n], x, y + 70, 20, "black", RED, res)
    text(c, "fora: pares e terminados em 5", 220, 600, 28, "bold", GRAY, ae, align="left")
    text(c, "8 candidatos", 220, 650, 32, "black", BLUE, ep(t, C["23.b"], 0.4), align="left")
    if sid == "24":
        ai = ep(t, C["24.i"], 0.4)
        text(c, "23, 29, 31, 37 → 4 primos", 220, 750, 42, "black", GREEN, ai, align="left")
        pill(c, "marcou 5 ou 6? um ímpar composto passou como primo", 1250, 760, AMBER, size=22,
             a=ep(t, C["24.x"], 0.4), anchor="center", bounds=(0, 1920))
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "FATORAÇÃO", PURPLE)
    aa = ep(t, C["26.a"], 0.5)
    text(c, "todo número é uma CONSTRUÇÃO de tijolos primos", W / 2, 260, 40, "black", BRICK, aa)
    ab = ep(t, C["26.b"], 0.5)
    for k, n in enumerate((2, 2, 2, 3, 3, 5)):
        a = ab * ep(t, C["26.b"] + 0.25 * k, 0.3)
        tijolo(c, 560 + (k % 3) * 160, 560 - (k // 3) * 90, 150, 80, "?", a)
    text(c, "360", 1330, 540, 120, "black", INK, ab)
    text(c, "quais tijolos?", 1330, 620, 32, "black", INK2, ab)
    pill(c, "próximo episódio: FATORAÇÃO", W / 2, 760, PURPLE, size=32, a=ep(t, C["26.c"], 0.4), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"], "Antes desta aula, você achava que o 1 era primo?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, fila=b_fila, primo=b_primo, composto=b_composto, um=b_um,
              dois=b_dois, crivo=b_crivo, raiz=b_raiz, entresi=b_entresi, recap=b_recap, erros=b_erros, exercicio=b_exercicio,
              q7=b_q7, ponte=b_ponte, cta=b_cta)
