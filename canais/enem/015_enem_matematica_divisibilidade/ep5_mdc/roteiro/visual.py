"""Visual — Divisibilidade, Primos, MMC e MDC, Episódio 5: MDC — o maior pedaço que cabe certinho (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Reaproveita o ep. 4 (V4: ícones, varal, alternativas, ftext/fbox/regra do 010 ep1).
Peças próprias deste episódio (reaproveitáveis no ep. 6, "repete × reparte"):
- medir(): uma tábua medida por uma régua — pedaços alternados; a sobra que não cabe fica vermelha.
- regua(): régua com marcações de centímetro.
- euclides(): retângulo 120 × 72 cortado em quadrados (72, 48, 24, 24) até não sobrar nada.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_ROOT = Path(__file__).resolve().parents[2]          # 015_enem_matematica_divisibilidade


def _load(nome, rel):
    sp = importlib.util.spec_from_file_location(nome, _ROOT / rel)
    mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
    return mod


V4 = _load("v015_ep4", "ep4_mmc/roteiro/visual.py")
motor.set_theme("claro")
M, V1 = V4.M, V4.V1

ftext, fmid, ftext_w, fbox, regra = M.ftext, M.fmid, M.ftext_w, M.fbox, M.regra
pause_timer, which, para, wrap, frame, head_seq, boxed, selo = (V1.pause_timer, V1.which, V1.para, V1.wrap, V1.frame,
                                                                 V1.head_seq, V1.boxed, V1.selo)
alts_panel = V4.alts_panel

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisibilidade_ep5_mdc.mp4"
CARD_R = (140, 150, 1640, 690)

MADEIRA, MADEIRA2 = "#C8955C", "#E0B784"
COR_M, COR_F = "#3B6CF6", "#F97316"     # meninos, meninas


# ======================================================================
# tábuas e réguas
# ======================================================================

def tabua(c, x, y, w, a, h=46, col=MADEIRA):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 6, col, a, shadow=True)
    for k in range(3):
        line(c, x + 10, y + 12 + k * 11, x + w - 10, y + 12 + k * 11, mix(col, "#000000", 0.12), a * 0.5, 1.5)


def medir(c, x, y, L, r, sc, a, prog_=1.0, h=46, label=True, ok_col=None):
    """tábua de L unidades medida por uma régua de r (sc px por unidade); pedaços alternados; sobra em vermelho.
    prog_ revela os pedaços da esquerda para a direita. Retorna (nº de pedaços, sobra)."""
    if a <= 0:
        return 0, 0
    n, sobra = int(L // r), L % r
    tabua(c, x, y, L * sc, a, h)
    vis = prog_ * (n + (1 if sobra else 0))
    for k in range(n):
        al = clamp(vis - k)
        if al <= 0:
            break
        col = ok_col or (GREEN if sobra == 0 else MADEIRA2)
        rrect(c, x + k * r * sc + 2, y + 3, r * sc - 4, h - 6, 4, col if k % 2 == 0 else mix(col, "#FFFFFF", 0.35), a * al * 0.85)
        if k:
            line(c, x + k * r * sc, y - 8, x + k * r * sc, y + h + 8, INK2, a * al, 2.5, dash=(6, 5))
    if sobra:
        al = clamp(vis - n)
        if al > 0:
            rrect(c, x + n * r * sc + 2, y + 3, sobra * sc - 4, h - 6, 4, RED, a * al * 0.85)
            line(c, x + n * r * sc, y - 8, x + n * r * sc, y + h + 8, RED, a * al, 2.5, dash=(6, 5))
            if label:
                text(c, f"sobra {sobra:g}", x + (n * r + sobra / 2) * sc, y + h + 34, 22, "black", RED, a * al)
    return n, sobra


def regua(c, x, y, L, sc, a, col=AMBER, txt=None):
    if a <= 0:
        return
    rrect(c, x, y, L * sc, 34, 6, mix("#FFFFFF", col, 0.55), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, L * sc, 34), 6, 6), paint(col, a, stroke=2.5))
    for k in range(int(L) + 1):
        line(c, x + k * sc, y, x + k * sc, y + (16 if k % 5 == 0 else 9), INK2, a, 1.5)
    if txt:
        text(c, txt, x + L * sc / 2, y + 28, 18, "black", INK, a)


# ======================================================================
# varal do MDC: todos os números juntos, ✓ nos primos que dividem TODOS
# ======================================================================

def varal_mdc(c, x, y, rows, final, k, a=1.0, size=44, lh=64, colw=130, juntar=0.0, final_hl=0.0):
    """rows = [([números], primo, marcado)] · final = números da última linha · k = passos feitos (float):
    a linha i aparece com k ≥ i, o primo/✓ da linha i com k ≥ i + 1. Primo marcado = círculo verde + ✓;
    não marcado = cinza (só serve para o MMC). juntar > 0 destaca os marcados (vão para o MDC);
    final_hl destaca a última linha (o que sobrou)."""
    if a <= 0:
        return
    n = len(final)
    xbar = x + n * colw + 16
    todas = [r[0] for r in rows] + [final]
    for i, nums in enumerate(todas):
        al = a * clamp(k - i + 1)
        if al <= 0:
            break
        yy = y + i * lh
        if i == len(todas) - 1 and final_hl > 0:
            rrect(c, x - 10, yy - lh / 2 + 4, n * colw + 20, lh - 8, 12, GREEN, a * final_hl * 0.16)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 10, yy - lh / 2 + 4, n * colw + 20, lh - 8), 12, 12),
                        paint(GREEN, a * final_hl, stroke=3))
        for j, v in enumerate(nums):
            fmid(c, str(v), x + j * colw + colw / 2, yy, size, "black", GRAY if v == 1 else INK, al)
        if i < len(rows):
            p, marcado = rows[i][1], rows[i][2]
            ap = a * clamp(k - i)
            if ap > 0:
                px = xbar + size * 1.1
                if marcado:
                    c.drawCircle(px, yy, size * 0.62, paint(mix("#FFFFFF", GREEN, 0.18 + 0.25 * juntar), ap))
                    c.drawCircle(px, yy, size * 0.62, paint(GREEN, ap, stroke=3))
                    check_icon(c, px + size * 1.25, yy, size * 0.32, ap, GREEN)
                fmid(c, str(p), px, yy, size, "black", GREEN if marcado else GRAY, ap)
    nlin = min(len(todas), max(1, math.ceil(k + 0.001)))
    line(c, xbar, y - lh / 2, xbar, y - lh / 2 + nlin * lh, INK2, a, 4)


V72 = [([72, 120], 2, True), ([36, 60], 2, True), ([18, 30], 2, True), ([9, 15], 3, True), ([3, 5], 3, False), ([1, 5], 5, False)]
V30 = [([30, 45], 3, True), ([10, 15], 5, True)]
VQ2 = [([120, 180, 300], 2, True), ([60, 90, 150], 2, True), ([30, 45, 75], 3, True), ([10, 15, 25], 5, True)]
VQ6 = [([48, 36], 2, True), ([24, 18], 2, True), ([12, 9], 3, True)]


def passos(t, C, cues, d=0.4):
    return sum(ep(t, C[q], d) for q in cues)


# ======================================================================
# Euclides: retângulo cortado em quadrados
# ======================================================================

EUC = [(0, 0, 72, BLUE), (72, 0, 48, PURPLE), (72, 48, 24, GREEN), (96, 48, 24, GREEN)]


def euclides(c, x, y, sc, a, cortes):
    """retângulo 120 × 72 (sc px/unidade); cortes = quantos quadrados já foram cortados (float)"""
    if a <= 0:
        return
    rrect(c, x, y, 120 * sc, 72 * sc, 4, "#F3EEE4", a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x, y, 120 * sc, 72 * sc), paint(INK2, a, stroke=3))
    for k, (qx, qy, s, col) in enumerate(EUC):
        al = clamp(cortes - k)
        if al <= 0:
            break
        rrect(c, x + qx * sc + 3, y + qy * sc + 3, s * sc - 6, s * sc - 6, 4, col, a * al * 0.22)
        c.drawRect(skia.Rect.MakeXYWH(x + qx * sc, y + qy * sc, s * sc, s * sc), paint(col, a * al, stroke=4))
        fmid(c, str(s), x + (qx + s / 2) * sc, y + (qy + s / 2) * sc, 26 + s * 0.35, "black", col, a * al)
    text(c, "120", x + 60 * sc, y - 16, 24, "black", GRAY, a)
    text(c, "72", x - 30, y + 36 * sc + 8, 24, "black", GRAY, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "O MAIOR PEDAÇO QUE CABE", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    medir(c, 260, 260, 600, 60, 1.6, aa, prog(t, C["01.a"], 2.0))
    fbox(c, "MDC = 60 ✓", 740, 400, 52, ep(t, C["01.a"] + 1.4, 0.4), GREEN)
    ab = ep(t, C["01.b"], 0.5)
    check_icon(c, 1360, 400, 44, ab, RED, "x")
    text(c, "e ainda erra a questão", 1360, 500, 34, "black", RED, ab)
    acc = ep(t, C["01.c"], 0.5)
    pill(c, "quantos PEDAÇOS?", 560, 580, AMBER, size=34, a=acc, anchor="center")
    pill(c, "quantas PESSOAS?", 1300, 580, AMBER, size=34, a=ep(t, C["01.c"] + 0.8, 0.4), anchor="center")
    fbox(c, "hoje: os 2 PASSOS", W / 2, 720, 50, ep(t, C["01.d"], 0.4), PURPLE)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "1 · calcular o MDC"), ("02.b", "2 · dar o PASSO FINAL que a questão pede")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 190 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 56, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO", "EM 30 SEGUNDOS", BLUE)
    cards = [("03.a", "DIVISOR", "divide certinho, sem sobrar bala", "12 ÷ 3 = 4", BLUE),
             ("03.b", "FATORAR", "a receita de primos", "12 = 2^2 · 3", PURPLE),
             ("03.c", "MMC", "o reencontro: coisas que se repetem", "MMC(6, 8) = 24", GREEN)]
    for k, (cue, t1, t2, ex, col) in enumerate(cards):
        a, d = rise(t, C[cue])
        x = 220 + k * 500
        rrect(c, x, 220 + d, 460, 330, 22, mix("#FFFFFF", col, 0.08), a, shadow=True)
        text(c, t1, x + 230, 290 + d, 40, "black", col, a)
        para(c, t2, x + 230, 350 + d, 26, "bold", INK2, a, 400, 32, align="center")
        fmid(c, ex, x + 230, 480 + d, 40, "black", INK, a)
    ad = ep(t, C["03.d"], 0.5)
    pill(c, "hoje: em vez de REPETIR, REPARTIR", W / 2, 680, AMBER, size=34, a=ad, anchor="center")


# ======================================================================
# bloco A: as tábuas e as réguas
# ======================================================================

SC_T = 55          # px por cm nas tábuas de 12 e 18
X_T = 240
REGUAS = [("05.a", 1), ("05.b", 2), ("05.c", 3), ("05.d", 4), ("06.a", 6)]


def b_regua(c, t, C, B):
    sid = which(t, C, ["04", "05", "06"])
    head_seq(c, t, C, [("04", "O MARCENEIRO", "PEDAÇOS IGUAIS, O MAIOR POSSÍVEL", BLUE), ("05", "TESTANDO", "RÉGUA POR RÉGUA", BLUE),
                       ("06", "A MAIOR RÉGUA", "QUE MEDE AS DUAS", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["04.a"], 0.5)
    text(c, "12 cm", X_T - 20, 300, 30, "black", INK2, a0, align="right")
    text(c, "18 cm", X_T - 20, 430, 30, "black", INK2, a0, align="right")
    cur = None
    for cue, r in REGUAS:
        if t >= C[cue] - 0.05:
            cur = (cue, r)
    if sid == "04" or cur is None:
        tabua(c, X_T, 270, 12 * SC_T, a0)
        tabua(c, X_T, 400, 18 * SC_T, a0)
        pill(c, "pedaços IGUAIS · sem sobrar", 1280, 560, BLUE, size=30, a=ep(t, C["04.b"], 0.4), anchor="center")
        pill(c, "do MAIOR tamanho possível?", 1280, 650, AMBER, size=30, a=ep(t, C["04.c"], 0.4), anchor="center")
        return
    cue, r = cur
    pr = prog(t, C[cue], 1.2)
    ok_col = GREEN if r == 6 else None
    medir(c, X_T, 270, 12, r, SC_T, 1.0, pr, ok_col=ok_col)
    medir(c, X_T, 400, 18, r, SC_T, 1.0, pr, ok_col=ok_col)
    regua(c, X_T, 200, r, SC_T, ep(t, C[cue], 0.3), GREEN if r == 6 else AMBER, f"{r} cm")
    # placar das réguas testadas
    x0 = 1330
    text(c, "RÉGUA", x0, 520, 20, "black", GRAY, 1.0, align="left", tracking=2)
    for k, (cq, rr) in enumerate(REGUAS):
        al = ep(t, C[cq] + 1.0, 0.3)
        ok = 12 % rr == 0 and 18 % rr == 0
        y = 560 + k * 52
        check_icon(c, x0 + 14, y, 16, al, GREEN if ok else RED, "check" if ok else "x")
        text(c, f"{rr} cm", x0 + 44, y + 10, 28, "black", GREEN if (rr == 6 and ok) else (INK if ok else RED), al, align="left")
    if sid == "06":
        ab = ep(t, C["06.b"], 0.4)
        regua(c, X_T, 520, 13, SC_T, ab * (1 - ep(t, C["06.c"], 0.3)), RED, "maior que 12: nem cabe")
        fbox(c, "a MAIOR régua: 6 cm", 640, 720, 50, ep(t, C["06.c"], 0.4), GREEN)


# ======================================================================
# bloco B: definição
# ======================================================================

def b_definicao(c, t, C, B):
    frame(c, t, B["start"], "O NOME DA MAIOR RÉGUA", "MDC", BLUE)
    a0 = ep(t, C["07.t"], 0.5)
    letras = [("M", "MÁXIMO", "o maior", "07.a"), ("D", "DIVISOR", "divide certinho", "07.b"), ("C", "COMUM", "de todos", "07.b")]
    for k, (L, w1, w2, cue) in enumerate(letras):
        a = ep(t, C[cue] + (0.6 if k == 2 else 0), 0.4)
        x = 520 + k * 440
        text(c, L, x, 330, 120, "black", BLUE, a0)
        text(c, w1, x, 400, 30, "black", INK, a)
        text(c, w2, x, 445, 26, "bold", GRAY, a)
    ac = ep(t, C["07.c"], 0.5)
    boxed(c, 260, 500, 1400, 140, BLUE, ac, 0.07)
    text(c, "DEFINIÇÃO", 300, 540, 18, "black", BLUE, ac, align="left", tracking=2)
    text(c, "o maior número que divide todos os dados ao mesmo tempo, sem resto", W / 2, 600, 34, "black", INK, ac)
    fbox(c, "MDC(12, 18) = 6", W / 2, 740, 50, ep(t, C["07.d"], 0.4), GREEN)


# ======================================================================
# bloco C: pela fatoração
# ======================================================================

def b_fatoracao(c, t, C, B):
    sid = which(t, C, ["08", "09", "10"])
    head_seq(c, t, C, [("08", "O PORQUÊ", "PELA RECEITA DE PRIMOS", PURPLE), ("09", "TESTANDO", "MDC(12, 18)", PURPLE),
                       ("10", "EU FAÇO", "MDC(72, 120)", PURPLE)])
    card(c, *CARD_R)
    if sid == "08":
        regra(c, "fatores COMUNS, com o MENOR expoente", W / 2, 300, ep(t, C["08.b"], 0.5), 44)
        ac = ep(t, C["08.c"], 0.5)
        text(c, "o divisor comum precisa CABER nos dois números", W / 2, 430, 34, "black", INK, ac)
        ad = ep(t, C["08.d"], 0.5)
        fmid(c, "2^3  e  2^1  →  2^1", W / 2, 540, 50, "black", PURPLE, ad)
        text(c, "manda o expoente MENOR", W / 2, 610, 28, "bold", PURPLE, ad)
        pill(c, "fator que falta em algum número: FICA DE FORA", W / 2, 720, AMBER, size=28, a=ep(t, C["08.e"], 0.4), anchor="center")
        return
    if sid == "09":
        fmid(c, "12 = 2^2 · 3", 560, 290, 60, "black", INK, ep(t, C["09.a"], 0.4))
        fmid(c, "18 = 2 · 3^2", 560, 390, 60, "black", INK, ep(t, C["09.b"], 0.4))
        pill(c, "comuns: 2 e 3", 1300, 290, BLUE, size=30, a=ep(t, C["09.c"], 0.4), anchor="center")
        pill(c, "menores expoentes: 2^1 e 3^1".replace("^1", "¹"), 1300, 390, PURPLE, size=30, a=ep(t, C["09.d"], 0.4), anchor="center")
        fbox(c, "MDC = 2 · 3 = 6", W / 2, 540, 56, ep(t, C["09.e"], 0.4), GREEN)
        text(c, "a mesma régua do marceneiro!", W / 2, 680, 32, "black", GREEN, ep(t, C["09.f"], 0.4))
        return
    fmid(c, "72 = 2^3 · 3^2", 520, 270, 54, "black", INK, ep(t, C["10.a"], 0.4))
    fmid(c, "120 = 2^3 · 3 · 5", 520, 360, 54, "black", INK, ep(t, C["10.b"], 0.4))
    ac = ep(t, C["10.c"], 0.4)
    for k, (f, e) in enumerate((("2", "^3"), ("3", ""))):
        x = 1180 + k * 200
        c.drawCircle(x, 300, 60, paint(mix("#FFFFFF", PURPLE, 0.14), ac))
        fmid(c, f + (e if ep(t, C["10.d"] + 0.4 * k, 0.3) > 0.5 else ""), x, 300, 52, "black", PURPLE, ac)
    text(c, "comuns · menor expoente", 1280, 400, 26, "bold", GRAY, ep(t, C["10.d"], 0.4))
    fbox(c, "MDC = 2^3 · 3 = 8 · 3 = 24", W / 2, 520, 52, ep(t, C["10.e"], 0.4), GREEN)
    af = ep(t, C["10.f"], 0.4)
    if af > 0:
        c.drawCircle(1400, 680, 52, paint(mix("#FFFFFF", RED, 0.12), af))
        fmid(c, "5", 1400, 680, 52, "black", RED, af)
        line(c, 1360, 720, 1440, 640, RED, af, 6)
        text(c, "o 5 não aparece nos dois: fica de fora", 1320, 690, 28, "black", RED, af, align="right")


def b_varal(c, t, C, B):
    sid = which(t, C, ["10b", "10c", "10d"])
    head_seq(c, t, C, [("10b", "O ATALHO DE PROVA", "TODOS OS NÚMEROS JUNTOS", GREEN),
                       ("10c", "UM VARAL", "DOIS RESULTADOS", GREEN), ("10d", "DICAS DE PROVA", "PARA O VARAL", GREEN)])
    card(c, *CARD_R)
    if sid == "10d":
        dicas = [("10d.a", "teste os primos EM ORDEM: 2, 3, 5, 7...", "use os critérios de divisibilidade (ep. 1)"),
                 ("10d.b", "só MARQUE o primo que divide TODOS da linha", "dividiu só um? não marca"),
                 ("10d.c", "só quer o MDC? PARE quando nenhum primo divide todos", "o resto do varal não muda o MDC")]
        for k, (cue, s1, s2) in enumerate(dicas):
            a, d = rise(t, C[cue])
            y = 290 + k * 165 + d
            badge_num(c, k + 1, 290, y - 14, a, 34, bg=GREEN)
            text(c, s1, 350, y, 42, "black", INK, a, align="left")
            text(c, s2, 350, y + 52, 28, "bold", GREEN, a, align="left")
        return
    x0, y0 = 330, 250
    if sid == "10b":
        k = passos(t, C, ["10b.r1", "10b.r2", "10b.r3", "10b.r4"])
        am = ep(t, C["10b.m"], 0.5)
        varal_mdc(c, x0, y0, V72[:4], [3, 5], k, ep(t, C["10b.a"], 0.4), juntar=am)
        text(c, "marca ✓ só quando o primo divide OS DOIS", 1250, 270, 28, "black", GREEN, ep(t, C["10b.r1"], 0.4))
        pill(c, "3 e 5: nenhum primo divide os dois → PARA", 1250, 560, AMBER, size=26, a=ep(t, C["10b.r5"], 0.4), anchor="center",
             bounds=(0, 1920))
        fbox(c, "MDC = 2 · 2 · 2 · 3 = 24", 1250, 680, 48, am, GREEN)
        return
    k = 4 + 2 * ep(t, C["10c.a"], 1.0)
    ab = ep(t, C["10c.b"], 0.5)
    varal_mdc(c, x0, y0 - 20, V72, [1, 1], k, 1.0, size=40, lh=58, juntar=ep(t, C["10c.d"], 0.5))
    if ab > 0:
        rrect(c, x0 + 2 * 130 + 40, y0 - 52, 100, 6 * 58 + 10, 16, PURPLE, ab * 0.10)
    ftext(c, "todos: 2 · 2 · 2 · 3 · 3 · 5", 1050, 300, 40, "black", PURPLE, ab, align="left")
    fbox(c, "MMC = 360", 1300, 400, 52, ep(t, C["10c.c"], 0.4), PURPLE)
    ad = ep(t, C["10c.d"], 0.4)
    fbox(c, "TODOS os primos → MMC = 360", 1260, 560, 40, ad, PURPLE)
    fbox(c, "só os MARCADOS ✓ → MDC = 24", 1260, 670, 40, ep(t, C["10c.d"] + 1.2, 0.4), GREEN)


def b_nosfazemos(c, t, C, B):
    frame(c, t, B["start"], "SUA VEZ", "MDC(30, 45) PELO VARAL", GREEN)
    fbox(c, "MDC(30, 45) = ?", 1300, 260, 60, ep(t, C["11.a"], 0.4), BLUE)
    pause_timer(c, t, C["11.p"] + 0.3, 1660, 400)
    ab = ep(t, C["11.b"], 0.4)
    if ab > 0:
        text(c, "o 2 divide o 30, mas NÃO o 45 → pula", 1280, 400, 30, "black", AMBER, ab)
    k = passos(t, C, ["11.c", "11.d"])
    varal_mdc(c, 360, 300, V30, [2, 3], k, ep(t, C["11.a"], 0.4), size=50, lh=80, colw=140,
              juntar=ep(t, C["11.f"], 0.4))
    pill(c, "2 e 3: nenhum primo divide os dois → PARA", 1280, 500, AMBER, size=26, a=ep(t, C["11.e"], 0.4), anchor="center",
         bounds=(0, 1920))
    fbox(c, "MDC = 3 · 5 = 15", 1280, 650, 56, ep(t, C["11.f"], 0.4), GREEN)


# ======================================================================
# bloco D: Euclides
# ======================================================================

def b_euclides(c, t, C, B):
    sid = which(t, C, ["12", "13"])
    head_seq(c, t, C, [("12", "NÚMERO DIFÍCIL DE FATORAR?", "ALGORITMO DE EUCLIDES", PURPLE),
                       ("13", "EUCLIDES", "CORTANDO EM QUADRADOS", PURPLE)])
    card(c, *CARD_R)
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        text(c, "ALGORITMO DE EUCLIDES", W / 2, 260, 52, "black", PURPLE, aa)
        pill(c, "ALGORITMO = uma sequência de passos, como uma receita", W / 2, 350, BLUE, size=28, a=ep(t, C["12.b"], 0.4), anchor="center")
        regra(c, "divida o maior pelo menor, depois o divisor pelo resto...", W / 2, 490, ep(t, C["12.c"], 0.5), 34)
        regra(c, "o último resto diferente de zero é o MDC", W / 2, 620, ep(t, C["12.d"], 0.5), 38, GREEN)
        return
    cortes = sum(ep(t, C[k], 0.6) for k in ("13.a", "13.b")) + 2 * ep(t, C["13.c"], 0.8)
    euclides(c, 240, 230, 6.0, ep(t, C["13.t"], 0.5), cortes)
    eqs = [("13.a", "120 = 1 · 72 + 48", BLUE), ("13.b", "72 = 1 · 48 + 24", PURPLE), ("13.c", "48 = 2 · 24 + 0", GREEN)]
    for k, (cue, s, col) in enumerate(eqs):
        fmid(c, s, 1360, 290 + k * 100, 46, "black", col, ep(t, C[cue], 0.4))
    ad = ep(t, C["13.d"], 0.4)
    pill(c, "← parou", 1640, 490, GREEN, size=24, a=ad, anchor="center", bounds=(0, 1920))
    fbox(c, "MDC = 24", 1360, 640, 56, ad, GREEN)


# ======================================================================
# blocos E, F, G
# ======================================================================

def b_reconhecer(c, t, C, B):
    frame(c, t, B["start"], "COMO RECONHECER", "AS PALAVRAS DO ENUNCIADO", GREEN)
    frases = [("14.a", "“o maior tamanho possível”"), ("14.b", "“dividir em partes iguais sem sobra”"),
              ("14.c", "“o maior número de grupos”"), ("14.d", "“a maior medida que cabe exatamente”")]
    for k, (cue, s) in enumerate(frases):
        a, d = rise(t, C[cue])
        x = 560 if k % 2 == 0 else 1360
        y = 290 + (k // 2) * 150 + d
        rrect(c, x - 370, y - 50, 740, 100, 18, mix("#FFFFFF", GREEN, 0.10), a)
        text_mid(c, s, x, y, 30, "black", INK, a)
    fbox(c, "repartir em pedaços iguais, o maior possível → MDC", W / 2, 680, 42, ep(t, C["14.e"], 0.4), GREEN)


def b_sanidade(c, t, C, B):
    frame(c, t, B["start"], "CHECAGEM RÁPIDA", "O MDC NUNCA É MAIOR", GREEN)
    regra(c, "MDC  ≤  menor dos números dados", W / 2, 270, ep(t, C["15.a"], 0.5), 46)
    ab = ep(t, C["15.b"], 0.4)
    tabua(c, 560, 400, 400, ab)
    regua(c, 560, 470, 9.1, 55, ab, RED, "régua maior que a tábua")
    text(c, "nem cabe!", 1180, 500, 34, "black", RED, ab, align="left")
    fbox(c, "24 ≤ 72 ✓", W / 2, 680, 56, ep(t, C["15.c"], 0.4), GREEN)


def b_passo2(c, t, C, B):
    frame(c, t, B["start"], "O SEGUNDO PASSO", "LEIA DE NOVO A PERGUNTA", AMBER)
    aa = ep(t, C["16.a"], 0.5)
    fbox(c, "MDC(12, 18) = 6 cm", 560, 250, 46, aa, GREEN)
    pill(c, "agora: o que foi perguntado?", 1340, 250, AMBER, size=30, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["16.b"], 0.4)
    text(c, "o TAMANHO do pedaço?", 300, 380, 34, "black", INK, ab, align="left")
    text(c, "→ 6 cm (o próprio MDC)", 760, 380, 34, "black", GREEN, ab, align="left")
    acc = ep(t, C["16.c"], 0.4)
    text(c, "QUANTOS pedaços?", 300, 470, 34, "black", INK, acc, align="left")
    pr = prog(t, C["16.d"], 1.4)
    medir(c, 300, 520, 12, 6, 30, ep(t, C["16.d"], 0.4), pr, h=40, ok_col=GREEN)
    medir(c, 740, 520, 18, 6, 30, ep(t, C["16.d"], 0.4), pr, h=40, ok_col=GREEN)
    fmid(c, "12 ÷ 6 = 2   ·   18 ÷ 6 = 3", 760, 630, 38, "black", INK, ep(t, C["16.d"], 0.4))
    fbox(c, "2 + 3 = 5 pedaços", 1440, 640, 44, ep(t, C["16.e"], 0.4), GREEN)
    pill(c, "o MDC é 6, mas a resposta é 5", W / 2, 760, AMBER, size=30, a=ep(t, C["16.f"], 0.4), anchor="center")


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Repartir em pedaços iguais, o maior possível: MDC.", "No varal, só entram os primos que dividem todos.",
          "Achou o MDC? Agora responda o que foi perguntado."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        text(c, s, 350, y, 48, "black", INK, a, align="left")


ERROS = [("18", "No MDC, multiplicar TODOS os primos do varal", "2 · 2 · 2 · 3 · 3 · 5 = 360 → isso é o MMC",
          "é assim que se faz o MMC", "360 > 72: a régua nem cabe. No MDC, só os MARCADOS ✓"),
         ("19", "Responder o MDC quando pedem PEDAÇOS ou ALUNOS", "“quantos pedaços?” → responde 6 cm", "a conta difícil já foi feita",
          "MDC é o meio do caminho: dê o SEGUNDO PASSO"),
         ("20", "Confundir MDC com MMC", "MMC = reencontro · MDC = maior régua", "nomes parecidos, mesma receita",
          "repete → MMC · reparte → MDC (próximo episódio)")]


def b_erros(c, t, C, B):
    sid = which(t, C, [e[0] for e in ERROS])
    n = [e[0] for e in ERROS].index(sid)
    _, err, ex, parece, fix = ERROS[n]
    head(c, t, C[sid], f"ERRO {n + 1} DE 3", "OS ERROS CLÁSSICOS", RED)
    card(c, *CARD_R)
    for k in range(3):
        badge_num(c, k + 1, 880 + k * 80, 210, 1, 22, bg=RED if k == n else LIGHT)
    cue = lambda x: C[f"{sid}.{x}"]
    aa = ep(t, cue("a"), 0.5)
    check_icon(c, 300, 320, 34, aa, RED, "x")
    text(c, err, 360, 335, 44, "black", RED, aa, align="left")
    ftext(c, ex, 360, 405, 34, "bold", INK2, ep(t, cue("a") + 0.8, 0.4), align="left")
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 500, AMBER, size=26, a=ab, bounds=(0, 1920))
    text(c, parece, 300, 575, 38, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 690, 34, ac, GREEN)
    text(c, fix, 360, 705, 38, "black", GREEN, ac, align="left")


# ======================================================================
# questões 2 e 6
# ======================================================================

Q2 = ("Um marceneiro tem três tábuas medindo 120 cm, 180 cm e 300 cm. Ele quer cortá-las em pedaços de mesmo comprimento, "
      "o maior possível, sem que sobre nenhum pedaço menor. Quantos pedaços obterá ao todo?")
ALT2 = [("A", "6", "21.d", "24.y", "não sai de nenhuma régua comum", RED),
        ("B", "10", "21.e", None, "", GREEN),
        ("C", "12", "21.f", "24.y", "não sai de nenhuma régua comum", RED),
        ("D", "15", "21.g", "24.y", "não sai de nenhuma régua comum", RED),
        ("E", "20", "21.h", "24.x", "usou 30 cm: comum, mas não a MAIOR", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2", "MDC EM CORTES", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["21.a"], 0.5)
    res = ep(t, C["22"], 0.5)
    para(c, Q2, 180, 240, 26, "bold", INK, a * (1 - res), 600, 34)
    for k, L in enumerate((120, 180, 300)):
        tabua(c, 190, 560 + k * 70, L * 1.9, ep(t, C["21.a"] + 0.4 * k, 0.4) * (1 - res), h=40)
        text(c, f"{L} cm", 190 + L * 1.9 + 14, 590 + k * 70, 22, "black", INK2, ep(t, C["21.a"] + 0.4 * k, 0.4) * (1 - res), align="left")
    if res > 0:
        pill(c, "pedaços iguais, o maior, sem sobra → MDC", 470, 230, GREEN, size=22, a=ep(t, C["22.a"], 0.4), anchor="center", bounds=(0, 1920))
        k = passos(t, C, ["22.r1", "22.r2", "22.r3", "22.r4"])
        am = ep(t, C["23.m"], 0.4)
        varal_mdc(c, 200, 300, VQ2, [2, 3, 5], k, ep(t, C["22.b"], 0.4), size=30, lh=48, colw=96,
                  juntar=ep(t, C["22.f"], 0.4), final_hl=am)
        if am > 0:
            text(c, "2 + 3 + 5 = 10 ✓", 520, 500, 28, "black", GREEN, am, align="left")
        pill(c, "nenhum divide os três → PARA", 400, 545, AMBER, size=20, a=ep(t, C["22.r5"], 0.4) * (1 - ep(t, C["22.f"], 0.3)),
             anchor="center", bounds=(0, 1920))
        ftext(c, "MDC = 2 · 2 · 3 · 5 = 60 cm", 190, 560, 34, "black", GREEN, ep(t, C["22.f"], 0.4), align="left")
        q = ep(t, C["23"], 0.4)
        pill(c, "60 ≤ 120 ✓", 300, 612, GREEN, size=22, a=ep(t, C["22.g"], 0.4) * (1 - q), anchor="center", bounds=(0, 1920))
        pill(c, "QUANTOS pedaços → segundo passo", 400, 612, AMBER, size=22, a=q, anchor="center", bounds=(0, 1920))
        ftext(c, "120 + 180 + 300 = 600", 190, 690, 32, "black", INK, ep(t, C["23.a"], 0.4), align="left")
        ftext(c, "600 ÷ 60 = 10 pedaços", 190, 755, 36, "black", GREEN, ep(t, C["23.b"], 0.4), align="left")
    if t >= C["21.d"] - 0.2:
        alts_panel(c, t, C, ALT2, 880, 260, 840, 34, "23.ok", "B", 26)
    if C.get("21.p"):
        pause_timer(c, t, C["21.end"] - 1.9, 1560, 720)
    pill(c, "60 nem está nas alternativas", 1300, 818, AMBER, size=24, a=ep(t, C["24.z"], 0.4), anchor="center", bounds=(0, 1920))
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


Q6 = ("Uma escola vai organizar 48 meninos e 36 meninas em grupos de trabalho. Todos os grupos devem ter o mesmo número de "
      "meninos e o mesmo número de meninas, sem que sobre nenhum aluno. Formando o maior número possível de grupos, quantos "
      "alunos haverá em cada grupo?")
ALT6 = [("A", "4", "26.a", "29.y", "contou só os meninos", RED),
        ("B", "7", "26.b", None, "", GREEN),
        ("C", "12", "26.c", "29.x", "parou no MDC", RED),
        ("D", "14", "26.d", "29.z", "6 grupos: não é o maior número", RED),
        ("E", "21", "26.e", "29.z", "4 grupos: não é o maior número", RED)]


def grupos(c, x, y, n, a, sc=1.0):
    """n grupos de 4 meninos + 3 meninas (bolinhas)"""
    if a <= 0:
        return
    for g in range(n):
        gx = x + (g % 6) * 92 * sc
        gy = y + (g // 6) * 92 * sc
        al = a * clamp(a * n - g)
        rrect(c, gx, gy, 80 * sc, 80 * sc, 12, "#F4F5F7", al)
        for k in range(4):
            c.drawCircle(gx + (16 + (k % 2) * 18) * sc, gy + (22 + (k // 2) * 18) * sc, 7 * sc, paint(COR_M, al))
        for k in range(3):
            c.drawCircle(gx + 58 * sc, gy + (16 + k * 18) * sc, 7 * sc, paint(COR_F, al))


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6", "MDC FORMANDO GRUPOS", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["25.a"], 0.5)
    res = ep(t, C["27"], 0.5)
    para(c, Q6, 180, 240, 25, "bold", INK, a * (1 - res), 620, 33)
    if res > 0:
        pill(c, "repartir sem sobra, maior nº de grupos → MDC", 480, 230, GREEN, size=22, a=ep(t, C["27.t"], 0.4), anchor="center", bounds=(0, 1920))
        k = passos(t, C, ["27.r1", "27.r2", "27.r3"])
        am = ep(t, C["28.m"], 0.4)
        varal_mdc(c, 200, 300, VQ6, [4, 3], k, ep(t, C["27.a"], 0.4), size=34, lh=54, colw=110,
                  juntar=ep(t, C["27.c"], 0.4), final_hl=am)
        if am > 0:
            text(c, "= meninos e meninas!", 520, 472, 24, "black", GREEN, am, align="left")
        pill(c, "4 e 3: nenhum divide os dois → PARA", 400, 525, AMBER, size=20, a=ep(t, C["27.r4"], 0.4) * (1 - ep(t, C["27.c"], 0.3)),
             anchor="center", bounds=(0, 1920))
        ftext(c, "MDC = 2 · 2 · 3 = 12 grupos", 190, 560, 34, "black", GREEN, ep(t, C["27.c"], 0.4), align="left")
        pill(c, "12 ≤ 36 ✓", 300, 612, GREEN, size=22, a=ep(t, C["27.e"], 0.4), anchor="center", bounds=(0, 1920))
        ftext(c, "48 ÷ 12 = 4 meninos", 190, 670, 30, "black", COR_M, ep(t, C["28.a"], 0.4), align="left")
        ftext(c, "36 ÷ 12 = 3 meninas", 190, 720, 30, "black", COR_F, ep(t, C["28.b"], 0.4), align="left")
        ftext(c, "4 + 3 = 7 alunos por grupo", 190, 785, 34, "black", GREEN, ep(t, C["28.c"], 0.4), align="left")
    if t >= C["26"] - 0.2:
        alts_panel(c, t, C, ALT6, 880, 260, 840, 34, "28.ok", "B", 26)
        pause_timer(c, t, C["26.end"] - 1.9, 1560, 720)
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MMC OU MDC?", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    rrect(c, 260, 230, 620, 340, 22, mix("#FFFFFF", GREEN, 0.08), aa, shadow=True)
    text(c, "REPETE", 570, 300, 44, "black", GREEN, aa)
    for k, col in enumerate((V4.COR_A, V4.COR_B)):
        V4.onibus(c, 470 + k * 200, 420, 1.0, aa, col)
    text(c, "MMC", 570, 530, 40, "black", GREEN, aa)
    rrect(c, 1040, 230, 620, 340, 22, mix("#FFFFFF", PURPLE, 0.08), aa, shadow=True)
    text(c, "REPARTE", 1350, 300, 44, "black", PURPLE, aa)
    medir(c, 1110, 390, 12, 3, 40, aa, 1.0, h=40, label=False, ok_col=PURPLE)
    text(c, "MDC", 1350, 530, 40, "black", PURPLE, aa)
    text(c, "o enunciado NÃO diz qual usar", W / 2, 650, 38, "black", AMBER, ep(t, C["31.b"], 0.4))
    fbox(c, "ep. 6 · a decisão em 10 segundos", W / 2, 760, 44, ep(t, C["31.c"], 0.4), PURPLE)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já respondeu o MDC quando a questão pedia outra coisa?", canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, regua=b_regua, definicao=b_definicao, fatoracao=b_fatoracao,
              varal=b_varal, nosfazemos=b_nosfazemos, euclides=b_euclides, reconhecer=b_reconhecer, sanidade=b_sanidade, passo2=b_passo2,
              recap=b_recap, erros=b_erros, q2=b_q2, q6=b_q6, ponte=b_ponte, cta=b_cta)
