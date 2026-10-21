"""Visual — Divisibilidade, Primos, MMC e MDC, Episódio 6: MMC ou MDC? A decisão em 10 segundos (iniciantes, tema claro).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
Reaproveita o ep. 4 (V4: linha_tempo, varal, ônibus, lâmpada, engrenagem, tábua) e, por ele, o 010 ep1 (ftext/fmid/fbox/regra)
e o 014 (alternativas, pausa, frame).
Peças novas:
- lado_repete() / lado_reparte(): a tela dividida (relógio girando, ônibus, setas circulares × tesoura, tábuas, fatias).
- regua_num(): a reta MDC ≤ menor ≤ maior ≤ MMC, com marcadores que acendem em vermelho quando fora do lugar.
- cerca(): retângulo do terreno com as estacas aparecendo uma a uma pelo perímetro (estacas = espaços).
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_EP = Path(__file__).resolve().parents[2]       # pasta da série
_sp = importlib.util.spec_from_file_location("v_div_ep4", _EP / "ep4_mmc" / "roteiro" / "visual.py")
V4 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(V4)
motor.set_theme("claro")

ftext, fmid, ftext_w, fbox, regra = V4.ftext, V4.fmid, V4.ftext_w, V4.fbox, V4.regra
pause_timer, which, para, wrap, frame, head_seq, boxed, selo = (V4.pause_timer, V4.which, V4.para, V4.wrap, V4.frame,
                                                                 V4.head_seq, V4.boxed, V4.selo)
alts_panel, linha_tempo, onibus, lampada, engrenagem, capsula, tabua = (V4.alts_panel, V4.linha_tempo, V4.onibus, V4.lampada,
                                                                        V4.engrenagem, V4.capsula, V4.tabua)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisibilidade_ep6_mmc_ou_mdc.mp4"
CARD_R = (140, 150, 1640, 690)

REP = BLUE      # REPETE → MMC
PAR = "#C2410C"  # REPARTE → MDC (laranja-terra, distinto do âmbar de armadilha)
MADEIRA = "#C8955C"


# ======================================================================
# ícones: repete × reparte
# ======================================================================

def relogio(c, cx, cy, r, a, t, col=REP):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(col, a, stroke=r * 0.1))
    for k in range(12):
        ang = math.radians(k * 30)
        line(c, cx + math.sin(ang) * r * 0.78, cy - math.cos(ang) * r * 0.78, cx + math.sin(ang) * r * 0.88,
             cy - math.cos(ang) * r * 0.88, INK2, a, 3)
    am = math.radians(t * 90)
    ah = math.radians(t * 8)
    line(c, cx, cy, cx + math.sin(am) * r * 0.72, cy - math.cos(am) * r * 0.72, INK, a, 5)
    line(c, cx, cy, cx + math.sin(ah) * r * 0.5, cy - math.cos(ah) * r * 0.5, col, a, 7)
    c.drawCircle(cx, cy, 6, paint(INK, a))


def setas_circ(c, cx, cy, r, a, t, col=REP):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(t * 40)
    for k in range(2):
        c.save(); c.rotate(k * 180)
        c.drawArc(skia.Rect.MakeLTRB(-r, -r, r, r), 200, 130, False, paint(col, a, stroke=r * 0.16, cap_round=True))
        ang = math.radians(330)
        px, py = math.cos(ang) * r, math.sin(ang) * r
        p = skia.Path()
        p.moveTo(px + 14, py - 12); p.lineTo(px - 4, py + 18); p.lineTo(px - 22, py - 10); p.close()
        c.drawPath(p, paint(col, a))
        c.restore()
    c.restore()


def tesoura(c, cx, cy, s, a, col=PAR, abre=0.5):
    if a <= 0:
        return
    ang = 12 + 18 * abre
    for sg in (-1, 1):
        c.save(); c.translate(cx, cy); c.rotate(sg * ang)
        rrect(c, 0, -6 * s, 110 * s, 12 * s, 6 * s, "#9CA3AF", a)
        c.drawCircle(-34 * s, 0, 20 * s, paint(col, a, stroke=9 * s))
        c.restore()
    c.drawCircle(cx, cy, 6 * s, paint(INK, a))


def fatias(c, cx, cy, r, a, n=6, cut=1.0, col="#F4B6C2"):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(col, a))
    c.drawCircle(cx, cy, r * 0.82, paint(mix(col, "#FFFFFF", 0.35), a))
    c.drawCircle(cx, cy, r, paint(mix(col, INK, 0.3), a, stroke=3))
    for k in range(n):
        if k >= cut * n:
            break
        ang = math.radians(-90 + k * 360 / n)
        line(c, cx, cy, cx + math.cos(ang) * r, cy + math.sin(ang) * r, "#FFFFFF", a, 5)


def lado_repete(c, x, y, w, h, a, t, titulo=True):
    """painel REPETE (MMC): relógio girando, ônibus, setas circulares"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", REP, 0.07), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), paint(REP, a, stroke=3))
    if titulo:
        text(c, "REPETE", x + w / 2, y + 62, 46, "black", REP, a)
        text(c, "MMC · resposta GRANDE", x + w / 2, y + 104, 24, "black", INK2, a)
    cy = y + (175 if titulo else 90)
    relogio(c, x + w * 0.22, cy, 52, a, t)
    onibus(c, x + w * 0.52, cy + 6, 0.85, a, REP)
    setas_circ(c, x + w * 0.80, cy, 44, a, t)


def lado_reparte(c, x, y, w, h, a, t, titulo=True):
    """painel REPARTE (MDC): tesoura, tábuas, fatias"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", PAR, 0.07), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), paint(PAR, a, stroke=3))
    if titulo:
        text(c, "REPARTE", x + w / 2, y + 62, 46, "black", PAR, a)
        text(c, "MDC · resposta PEQUENA", x + w / 2, y + 104, 24, "black", INK2, a)
    cy = y + (175 if titulo else 90)
    tesoura(c, x + w * 0.20, cy, 0.7, a, PAR, 0.5 + 0.5 * math.sin(t * 6))
    for k in range(2):
        rrect(c, x + w * 0.38, cy - 26 + k * 34, w * 0.24, 22, 5, MADEIRA, a)
        for j in range(1, 4):
            xx = x + w * 0.38 + w * 0.24 * j / 4
            line(c, xx, cy - 30 + k * 34, xx, cy - 0 + k * 34, PAR, a, 2)
    fatias(c, x + w * 0.80, cy, 46, a, 6)


# ======================================================================
# régua de conferência
# ======================================================================

REG = [("MDC", 24), ("menor", 72), ("maior", 120), ("MMC", 360)]


def regua_num(c, x0, y, w, a, vmax=400, marks=REG, show=None, wrong=None, wrong_a=0.0):
    """reta numérica; marks = [(rótulo, valor)]; show[i] = alfa de cada marcador;
    wrong = (rótulo, valor, valor_certo) — marcador vermelho fora do lugar"""
    if a <= 0:
        return
    X = lambda v: x0 + w * v / vmax
    line(c, x0, y, x0 + w, y, INK2, a, 4)
    for v in range(0, vmax + 1, 40):
        line(c, X(v), y - 6, X(v), y + 6, LIGHT, a, 2)
    cols = [PAR, INK, INK, REP]
    for i, (lab, v) in enumerate(marks):
        al = a * (show[i] if show else 1.0)
        if al <= 0:
            continue
        col = cols[i % 4]
        c.drawCircle(X(v), y, 16, paint(col, al))
        fmid(c, str(v), X(v), y - 50, 34, "black", col, al)
        text(c, lab, X(v), y + 52, 22, "black", col if lab in ("MDC", "MMC") else GRAY, al)
        if i < len(marks) - 1 and (show is None or (show[i + 1] if show else 1) > 0.5):
            fmid(c, "≤", (X(v) + X(marks[i + 1][1])) / 2, y - 50, 30, "black", PURPLE, al)
    if wrong and wrong_a > 0:
        lab, v, _ = wrong
        rrect(c, X(v) - 34, y - 150, 68, 250, 16, RED, a * 0.12 * wrong_a)
        c.drawCircle(X(v), y, 18, paint(RED, a * wrong_a))
        fmid(c, str(v), X(v), y - 110, 38, "black", RED, a * wrong_a)
        text(c, lab + "?", X(v), y + 90, 26, "black", RED, a * wrong_a)


# ======================================================================
# a cerca com estacas
# ======================================================================

def _pontos_cerca(L=60, A=24, d=12):
    pts, per = [], 2 * (L + A)
    k = 0
    while k * d < per:
        s = k * d
        if s <= L:
            pts.append((s, 0))
        elif s <= L + A:
            pts.append((L, s - L))
        elif s <= 2 * L + A:
            pts.append((L - (s - L - A), A))
        else:
            pts.append((0, A - (s - 2 * L - A)))
        k += 1
    return pts


ESTACAS = _pontos_cerca()   # 14 pontos


def cerca(c, x, y, w, a, n_show=0.0, cotas=True, cont=True):
    """terreno 60 × 24 m desenhado com largura w; estacas surgem uma a uma (n_show)"""
    if a <= 0:
        return
    sc = w / 60
    h = 24 * sc
    rrect(c, x, y, w, h, 6, "#E8F2E1", a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(MADEIRA, a * 0.8, stroke=3))
    if cotas:
        text(c, "60 m", x + w / 2, y - 22, 24, "black", INK2, a)
        text(c, "24 m", x - 18, y + h / 2 + 8, 24, "black", INK2, a, align="right")
    for i, (px, py) in enumerate(ESTACAS):
        r = clamp(n_show - i)
        if r <= 0:
            break
        cx, cy = x + px * sc, y + py * sc
        c.drawCircle(cx, cy, 13 * (0.6 + 0.4 * ease_back(r)), paint(PAR, a * r))
        if i == 0:
            c.drawCircle(cx, cy, 20, paint(GREEN, a * r, stroke=3))
    if cont and n_show > 0:
        fmid(c, f"{min(len(ESTACAS), int(n_show + 0.001))} estacas", x + w / 2, y + h / 2, 34, "black", PAR, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "O ERRO NÃO É A CONTA", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    rrect(c, 260, 230, 620, 300, 22, mix("#FFFFFF", GREEN, 0.07), aa)
    text(c, "A CONTA", 570, 290, 28, "black", GREEN, aa, tracking=2)
    fmid(c, "MDC(72, 120) = 24", 570, 380, 48, "black", INK, aa)
    check_icon(c, 570, 470, 30, ep(t, C["01.a"] + 0.6, 0.3), GREEN)
    ab = ep(t, C["01.b"], 0.5)
    rrect(c, 1040, 230, 620, 300, 22, mix("#FFFFFF", RED, 0.06), ab)
    text(c, "A ESCOLHA", 1350, 290, 28, "black", RED, ab, tracking=2)
    text(c, "a questão pedia o MMC", 1350, 390, 40, "black", INK, ab)
    check_icon(c, 1350, 470, 30, ep(t, C["01.b"] + 0.6, 0.3), RED, "x")
    selo(c, W / 2, 660, ep(t, C["01.c"], 0.4), "PROBLEMA ERRADO, RESOLVIDO PERFEITAMENTE", RED, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "MMC ou MDC em 10 segundos"), ("02.b", "uma RÉGUA para conferir a resposta")]
    for j, (cue, s) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 190 + d
        check_icon(c, 330, y - 14, 36, a, GREEN)
        text(c, s, 400, y, 56, "black", INK, a, align="left")


def b_cenas(c, t, C, B):
    frame(c, t, B["start"], "DUAS CENAS", "O QUE ACONTECE EM CADA UMA?", BLUE)
    aa = ep(t, C["03.a"], 0.5)
    # pista com dois corredores em ritmos diferentes
    cx, cy = 560, 410
    if aa > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(cx - 260, cy - 140, cx + 260, cy + 140), 140, 140),
                    paint("#E7C9B0", aa, stroke=40))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(cx - 260, cy - 140, cx + 260, cy + 140), 140, 140),
                    paint("#FFFFFF", aa * 0.8, stroke=2))
        line(c, cx, cy + 120, cx, cy + 160, INK, aa, 4)
        tt = max(0.0, t - C["03.a"])
        for k, (per, col) in enumerate(((4.0, REP), (6.0, GREEN))):
            ang = 2 * math.pi * tt / per + math.pi / 2
            px = cx + 260 * math.cos(ang) * (1 if abs(math.cos(ang)) > 0 else 1)
            py = cy + 140 * math.sin(ang)
            c.drawCircle(px, py, 16, paint(col, aa))
    text(c, "juntos na largada DE NOVO?", cx, 640, 30, "black", INK2, aa)
    ab = ep(t, C["03.b"], 0.5)
    fatias(c, 1360, 410, 150, ab, 8, prog(t, C["03.b"] + 0.5, 2.0))
    text(c, "fatias IGUAIS, sem sobrar", 1360, 640, 30, "black", INK2, ab)
    pill(c, "SE REPETE e se reencontra", cx, 730, REP, size=28, a=ep(t, C["03.c"], 0.4), anchor="center", bounds=(0, 1920))
    pill(c, "é REPARTIDA", 1360, 730, PAR, size=28, a=ep(t, C["03.d"], 0.4), anchor="center", bounds=(0, 1920))


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRANDO OS EPISÓDIOS 4 E 5", "EM 45 SEGUNDOS", BLUE)
    aa = ep(t, C["04.a"], 0.5)
    text(c, "MMC = o REENCONTRO", 560, 250, 42, "black", REP, aa)
    series = [dict(step=6, col=REP, label="6"), dict(step=8, col=GREEN, label="8")]
    linha_tempo(c, t, 230, 290, 660, 26, series, coinc=(24,), coinc_a=aa, unit="", tick=6, a=aa, row_h=50, label_w=90)
    regra(c, "todos os fatores, MAIOR expoente", 560, 520, ep(t, C["04.b"], 0.4), 28)
    fbox(c, "MMC(72, 120) = 360", 560, 640, 42, ep(t, C["04.c"], 0.4), REP)
    ad = ep(t, C["04.d"], 0.5)
    text(c, "MDC = a MAIOR RÉGUA", 1360, 250, 42, "black", PAR, ad)
    for k, (w_, n) in enumerate(((480, 4), (720, 6))):
        tabua(c, 1360 - 360, 300 + k * 70, w_ * 0.9, ad, MADEIRA, cortes=n, cut_a=ep(t, C["04.d"] + 0.8, 0.4))
    regra(c, "fatores comuns, MENOR expoente", 1360, 520, ep(t, C["04.e"], 0.4), 28)
    fbox(c, "MDC(72, 120) = 24", 1360, 640, 42, ep(t, C["04.f"], 0.4), PAR)
    line(c, W / 2, 220, W / 2, 700, LINE, max(aa, ad), 2)


def b_ancora(c, t, C, B):
    frame(c, t, B["start"], "A PERGUNTA DE 10 SEGUNDOS", "REPETE OU REPARTE?", PURPLE)
    lado_repete(c, 200, 200, 740, 300, ep(t, C["05.a"], 0.5), t)
    lado_reparte(c, 980, 200, 740, 300, ep(t, C["05.c"], 0.5), t)
    text(c, "coisas em ciclo, que se reencontram no futuro", 570, 560, 26, "black", INK2, ep(t, C["05.a"], 0.5))
    text(c, "algo cortado em pedaços iguais", 1350, 560, 26, "black", INK2, ep(t, C["05.c"], 0.5))
    fbox(c, "MMC → GRANDE", 570, 680, 44, ep(t, C["05.b"], 0.4), REP)
    fbox(c, "MDC → PEQUENA", 1350, 680, 44, ep(t, C["05.d"], 0.4), PAR)


# ======================================================================
# bloco A: a tabela de decisão
# ======================================================================

TAB = [("06.a", "06.a1", "06.a2", "O que acontece no problema?", "Coisas se repetem em ciclos", "Algo é repartido em pedaços"),
       ("06.b", "06.b1", "06.b2", "O que se procura?", "Quando voltam a coincidir", "Que tamanho cada parte terá"),
       ("07.c", "07.c1", "07.c2", "Palavra-chave", "“juntos”, “ao mesmo tempo”, “novamente”", "“iguais”, “sem sobra”, “o maior possível”"),
       ("07.d", "07.d1", "07.d2", "A resposta é…", "Maior que todos os dados", "Menor ou igual ao menor dado"),
       ("08.e", "08.e1", "08.e2", "Exemplo típico", "Ônibus, lâmpadas, engrenagens, remédios", "Tábuas, grupos, ladrilhos, estacas")]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "A TABELA DE DECISÃO", "LINHA POR LINHA", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["06.t"], 0.4)
    x0, x1, x2 = 180, 690, 1180
    rrect(c, x1 - 10, 180, 480, 56, 12, mix("#FFFFFF", REP, 0.14), a0)
    text_mid(c, "MMC · REPETE", x1 + 230, 208, 28, "black", REP, a0)
    rrect(c, x2 - 10, 180, 480, 56, 12, mix("#FFFFFF", PAR, 0.14), a0)
    text_mid(c, "MDC · REPARTE", x2 + 230, 208, 28, "black", PAR, a0)
    text_mid(c, "PERGUNTE-SE", x0 + 230, 208, 22, "black", GRAY, a0)
    for k, (cq, c1, c2, q, s1, s2) in enumerate(TAB):
        y = 300 + k * 108
        aq, d = rise(t, C[cq])
        if aq <= 0:
            continue
        line(c, x0, y - 44, x2 + 470, y - 44, LINE, aq, 2)
        para(c, q, x0, y - 4 + d, 28, "black", INK, aq, 460, 32)
        para(c, s1, x1, y - 4, 26, "bold", REP, ep(t, C[c1], 0.4), 460, 30)
        para(c, s2, x2, y - 4, 26, "bold", PAR, ep(t, C[c2], 0.4), 460, 30)


# ======================================================================
# blocos B, C e D: régua, relação, limite
# ======================================================================

def b_regua(c, t, C, B):
    sid = which(t, C, ["09", "10"])
    head_seq(c, t, C, [("09", "A RÉGUA DE CONFERÊNCIA", "TUDO NO LUGAR", GREEN), ("10", "FORA DO LUGAR?", "MÉTODO TROCADO", RED)])
    card(c, *CARD_R)
    regra(c, "MDC  ≤  menor dado  ≤  maior dado  ≤  MMC", W / 2, 250, ep(t, C["09.a"], 0.5), 40)
    show = [ep(t, C[k], 0.4) for k in ("09.b", "09.c", "09.d", "09.e")]
    if sid == "10":
        show = [1.0] * 4
    regua_num(c, 260, 480, 1400, 1.0, 400, show=show)
    text(c, "com 72 e 120", 260, 380, 24, "bold", GRAY, ep(t, C["09.f"], 0.4), align="left")
    if sid == "09":
        pill(c, "tudo no lugar ✓", W / 2, 680, GREEN, size=30, a=ep(t, C["09.f"] + 2.5, 0.4), anchor="center")
        return
    wa = ep(t, C["10.t"], 0.5)
    wb = ep(t, C["10.b"], 0.5)
    if wb < 0.5:
        regua_num(c, 260, 480, 1400, 1.0, 400, marks=[], wrong=("MDC", 90, 24), wrong_a=wa)
        pill(c, "MDC 90 > 72: fora do lugar", W / 2, 680, RED, size=28, a=ep(t, C["10.a"], 0.4), anchor="center")
    else:
        regua_num(c, 260, 480, 1400, 1.0, 400, marks=[], wrong=("MMC", 60, 360), wrong_a=wb)
        pill(c, "MMC 60 < 120: fora do lugar", W / 2, 680, RED, size=28, a=wb, anchor="center")
    pill(c, "o erro quase sempre é o MÉTODO, não a conta", W / 2, 770, AMBER, size=26,
         a=ep(t, C["10.c"], 0.4) * (1 - ep(t, C["10.d"], 0.3)), anchor="center")
    pill(c, "não coube? troque o método", W / 2, 770, GREEN, size=28, a=ep(t, C["10.d"], 0.4), anchor="center")


def b_relacao(c, t, C, B):
    frame(c, t, B["start"], "SÓ PARA DOIS NÚMEROS", "MDC · MMC = a · b", PURPLE)
    regra(c, "MDC(a, b) · MMC(a, b) = a · b", W / 2, 260, ep(t, C["11.a"], 0.5), 46)
    fmid(c, "24 · 360 = 8 640", 600, 420, 52, "black", INK, ep(t, C["11.b"], 0.4))
    fmid(c, "72 · 120 = 8 640", 1320, 420, 52, "black", INK, ep(t, C["11.c"], 0.4))
    fmid(c, "=", W / 2, 420, 52, "black", GREEN, ep(t, C["11.c"] + 1.0, 0.3))
    check_icon(c, W / 2, 500, 26, ep(t, C["11.c"] + 1.0, 0.3), GREEN)
    pill(c, "1 · CONFERIR o MDC e o MMC", 620, 650, GREEN, size=28, a=ep(t, C["11.d"], 0.4), anchor="center", bounds=(0, 1920))
    pill(c, "2 · ACHAR o valor que falta", 1300, 650, GREEN, size=28, a=ep(t, C["11.e"], 0.4), anchor="center", bounds=(0, 1920))


def b_limite(c, t, C, B):
    frame(c, t, B["start"], "CUIDADO COM O LIMITE", "COM TRÊS NÚMEROS, QUEBRA", RED)
    regra(c, "vale apenas para DOIS números", W / 2, 250, ep(t, C["12.a"], 0.5), 40, RED)
    ab = ep(t, C["12.b"], 0.4)
    fmid(c, "4, 6 e 10", W / 2, 360, 48, "black", INK, ab)
    fmid(c, "MDC = 2   ·   MMC = 60", W / 2, 440, 40, "black", INK2, ab)
    fbox(c, "2 · 60 = 120", 600, 580, 50, ep(t, C["12.c"], 0.4), PAR)
    fbox(c, "4 · 6 · 10 = 240", 1320, 580, 50, ep(t, C["12.d"], 0.4), REP)
    fmid(c, "≠", W / 2, 580, 70, "black", RED, ep(t, C["12.e"], 0.3))
    pill(c, "a igualdade simplesmente quebra", W / 2, 720, RED, size=28, a=ep(t, C["12.e"], 0.4), anchor="center")


# ======================================================================
# recap
# ======================================================================

FRASES = [("Repete: MMC, resposta grande. Reparte: MDC, resposta pequena.", 42),
          ("MDC ≤ menor ≤ maior ≤ MMC.", 50),
          ("MDC · MMC = a · b, só para dois números.", 50)]


def b_recap(c, t, C, B):
    sid = which(t, C, ["13", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "13" else "PARA FECHAR", PURPLE)
    for k, (s, sz) in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 280, y - 16, a, 36, bg=PURPLE)
        ftext(c, s, 350, y, sz, "black", INK, a, align="left")


# ======================================================================
# treino rápido: repete ou reparte?
# ======================================================================

TREINO = [("14", "Dois faróis piscam a cada 15 e a cada 20 segundos. Piscaram juntos agora. Quando piscam juntos de novo?",
           "R", "“juntos de novo”"),
          ("15", "Um piso de 2,4 m × 3,6 m vai ser coberto com ladrilhos quadrados, os maiores possíveis, sem cortar nenhum.",
           "P", "“os maiores possíveis”"),
          ("16", "Uma professora tem 48 lápis e 60 borrachas e quer montar o maior número possível de kits iguais, sem sobrar nada.",
           "P", "“kits iguais, sem sobrar”"),
          ("17", "Duas engrenagens: uma completa a volta a cada 8 s, a outra a cada 12 s. Quando as marcas voltam ao início ao mesmo tempo?",
           "R", "“ao mesmo tempo”"),
          ("18", "Um marceneiro quer cortar tábuas de 90 cm e de 150 cm em pedaços iguais, do maior tamanho possível.",
           "P", "“pedaços iguais, o maior possível”"),
          ("19", "Uma pessoa vai à academia a cada 4 dias, e uma amiga, a cada 6. Hoje se encontraram lá. Quando se encontram novamente?",
           "R", "“novamente”")]


def b_treino(c, t, C, B):
    ids = [x[0] for x in TREINO]
    sid = which(t, C, ids)
    n = ids.index(sid)
    head(c, t, C["14"], "TREINO RÁPIDO", "REPETE OU REPARTE?", PURPLE)
    card(c, *CARD_R)
    # placar lateral com as já decididas
    lado_repete(c, 170, 170, 360, 650, 1.0, t, titulo=False)
    lado_reparte(c, 1390, 170, 360, 650, 1.0, t, titulo=False)
    text(c, "REPETE · MMC", 350, 362, 30, "black", REP, 1.0)
    text(c, "REPARTE · MDC", 1570, 362, 30, "black", PAR, 1.0)
    cnt = {"R": 0, "P": 0}
    for k, (_, s, lado, pal) in enumerate(TREINO[:n + 1]):
        if k == n and t < C[f"{sid}.r"] + 0.6:
            continue
        x = 350 if lado == "R" else 1570
        y = 400 + cnt[lado] * 120
        cnt[lado] += 1
        rrect(c, x - 160, y, 320, 100, 14, "#FFFFFF", 1.0, shadow=True)
        badge_num(c, k + 1, x - 125, y + 50, 1.0, 20, bg=REP if lado == "R" else PAR)
        para(c, pal, x - 95, y + 44, 20, "black", INK2, 1.0, 240, 24)
    # o enunciado atual, no centro, voando para o lado na resposta
    _, s, lado, pal = TREINO[n]
    aq = ep(t, C[f"{sid}.q"], 0.4)
    fly = ease_out(prog(t, C[f"{sid}.r"], 0.6))
    tx = (350 if lado == "R" else 1570) - 960
    cx = 960 + tx * fly
    cy = 420 + (60 if lado else 0) * fly
    sc = 1 - 0.6 * fly
    a_card = aq * (1 - fly)
    if a_card > 0:
        c.save(); c.translate(cx, cy); c.scale(sc, sc)
        rrect(c, -390, -150, 780, 300, 22, "#FFFFFF", a_card, shadow=True)
        badge_num(c, n + 1, -340, -100, a_card, 26, bg=PURPLE)
        para(c, s, -300, -90, 30, "black", INK, a_card, 660, 38)
        c.restore()
    pause_timer(c, t, C[f"{sid}.p"] + 0.3, 960, 660, dur=4.6)
    ar = ep(t, C[f"{sid}.r"], 0.4)
    if ar > 0:
        selo(c, 960, 600, ar, "REPETE → MMC" if lado == "R" else "REPARTE → MDC", REP if lado == "R" else PAR, -4, 40)
    pill(c, "entregou: " + pal, 960, 720, GREEN, size=26, a=ep(t, C[f"{sid}.w"], 0.4), anchor="center", bounds=(0, 1920))
    for k in range(6):
        badge_num(c, k + 1, 760 + k * 80, 210, 1, 18, bg=PURPLE if k == n else (INK2 if k < n else LIGHT))
    text(c, "Situações elaboradas para fins didáticos.", 180, 860, 16, "medium", GRAY, 1.0, align="left")


# ======================================================================
# erros
# ======================================================================

ERROS = [("20", "Escolher o método ERRADO e fazer a conta CERTA", "cada passo da conta confere",
          "antes: repete ou reparte? depois: a RÉGUA"),
         ("21", "MDC · MMC = a · b · c com três números", "com dois números funciona",
          "com três quebra: 120 ≠ 240"),
         ("22", "Estacas: esquecer de DOBRAR o perímetro", "24 + 60 = 84 m parece a volta",
          "o retângulo tem 4 lados: 2 · (24 + 60) = 168 m"),
         ("23", "Figura fechada: SOMAR 1 estaca no final", "numa linha reta há 1 estaca a mais",
          "na figura fechada, estacas = espaços")]


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
    check_icon(c, 300, 320, 34, aa, RED, "x")
    ftext(c, err, 360, 335, 42, "black", RED, aa, align="left")
    if sid == "22":
        pill(c, "PERÍMETRO = a volta inteira da figura", 1360, 410, BLUE, size=22, a=ep(t, cue("a") + 1.0, 0.4), anchor="center",
             bounds=(0, 1920))
    if sid == "23":
        pill(c, "FIGURA FECHADA = termina onde começou", 1360, 410, BLUE, size=22, a=ep(t, cue("a") + 1.0, 0.4), anchor="center",
             bounds=(0, 1920))
    ab = ep(t, cue("b"), 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 500, AMBER, size=26, a=ab, bounds=(0, 1920))
    ftext(c, parece, 300, 575, 36, "bold", INK2, ab, align="left")
    ac = ep(t, cue("c"), 0.5)
    check_icon(c, 300, 690, 34, ac, GREEN)
    ftext(c, fix, 360, 705, 38, "black", GREEN, ac, align="left")


# ======================================================================
# questões 9 e 8
# ======================================================================

Q9 = ("Um terreno retangular mede 24 m por 60 m e será cercado com estacas igualmente espaçadas, obrigatoriamente com uma "
      "estaca em cada um dos quatro cantos. Adotando a maior distância possível entre estacas consecutivas, quantas estacas "
      "serão usadas?")
ALT9 = [("A", "7", "24.c", "27.xa", "esqueceu de dobrar: 84 ÷ 12", RED),
        ("B", "12", "24.d", "27.xb", "parou no MDC", RED),
        ("C", "14", "24.e", None, "", GREEN),
        ("D", "16", "24.f", "27.xd", "não sai de 168 ÷ 12", RED),
        ("E", "28", "24.g", "27.xd", "não sai de 168 ÷ 12", RED)]


def b_q9(c, t, C, B):
    sid = which(t, C, ["24", "25", "26", "27"])
    head(c, t, B["start"], "QUESTÃO 9", "A CERCA COM ESTACAS", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["24.a"], 0.5)
    res = ep(t, C["25"], 0.5)
    para(c, Q9, 180, 240, 26, "bold", INK, a * (1 - res), 600, 34)
    cerca(c, 240, 600, 480, a * (1 - res), 0, cotas=True, cont=False)
    if res > 0:
        pill(c, "repartir os lados, o maior possível → REPARTE → MDC", 470, 220, PAR, size=20, a=ep(t, C["25.a"], 0.4),
             anchor="center", bounds=(0, 1920))
        rows = [("25.c", "24 = 2^3 · 3", INK), ("25.d", "60 = 2^2 · 3 · 5", INK), ("25.e", "MDC = 2^2 · 3 = 12 m", PAR)]
        for k, (cue, s, col) in enumerate(rows):
            ftext(c, s, 190, 300 + k * 60, 34, "black", col, ep(t, C[cue], 0.4), align="left")
        pill(c, "12 ≤ 24 ✓", 700, 420, GREEN, size=22, a=ep(t, C["25.f"], 0.4), anchor="center", bounds=(0, 1920))
        if t >= C["26"] - 0.1:
            ftext(c, "P = 2 · (24 + 60) = 168 m", 190, 500, 32, "black", INK, ep(t, C["26.a"], 0.4), align="left")
            ftext(c, "168 ÷ 12 = 14 estacas", 190, 556, 34, "black", GREEN, ep(t, C["26.b"], 0.4), align="left")
            n_show = 14 * prog(t, C["26.b"], 3.0) if t < C["27"] else 14
            cerca(c, 240, 650, 460, 1.0, n_show, cotas=True, cont=False)
            pill(c, "figura fechada: estacas = espaços", 470, 790, BLUE, size=20, a=ep(t, C["26.c"], 0.4), anchor="center",
                 bounds=(0, 1920))
    alts_panel(c, t, C, ALT9, 860, 260, 860, 34, "26.ok", "C", 26)
    pause_timer(c, t, C["24.end"] - 1.9, 1560, 720)
    if sid == "27":
        pill(c, "+1 estaca daria 15: nem está nas alternativas", 1290, 790, AMBER, size=22, a=ep(t, C["27.xd"], 0.4),
             anchor="center", bounds=(0, 1920))
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


Q8 = ("O máximo divisor comum de dois números naturais é 6 e o mínimo múltiplo comum deles é 180. Sabendo que um dos "
      "números é 36, qual é o outro?")
ALT8 = [("A", "24", "28.c", "31.xa", "MDC(36, 24) = 12", RED),
        ("B", "30", "28.d", None, "", GREEN),
        ("C", "42", "28.e", "31.xc", "MMC(36, 42) = 252", RED),
        ("D", "60", "28.f", "31.xd", "MDC(36, 60) = 12", RED),
        ("E", "90", "28.g", "31.xe", "MDC(36, 90) = 18", RED)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8", "A RELAÇÃO MDC × MMC", BLUE)
    card(c, *CARD_R)
    a = ep(t, C["28.a"], 0.5)
    res = ep(t, C["29"], 0.5)
    para(c, Q8, 180, 240, 30, "bold", INK, a * (1 - res), 600, 40)
    if res > 0:
        pill(c, "dois números → vale a relação", 470, 220, PURPLE, size=22, a=res, anchor="center", bounds=(0, 1920))
        rows = [("29.a", "MDC · MMC = a · b", PURPLE, 34), ("29.b", "6 · 180 = 36 · b", INK, 34), ("29.c", "1 080 = 36 · b", INK, 34),
                ("29.d", "b = 1 080 ÷ 36 = 30", GREEN, 36)]
        for k, (cue, s, col, sz) in enumerate(rows):
            ftext(c, s, 190, 300 + k * 58, sz, "black", col, ep(t, C[cue], 0.4), align="left")
        if t >= C["30"] - 0.1:
            rows2 = [("30.a", "36 = 2^2 · 3^2"), ("30.b", "30 = 2 · 3 · 5"), ("30.c", "MDC = 2 · 3 = 6 ✓"), ("30.d", "MMC = 2^2 · 3^2 · 5 = 180 ✓")]
            for k, (cue, s) in enumerate(rows2):
                ftext(c, s, 190, 570 + k * 56, 30, "black", GREEN if k >= 2 else INK2, ep(t, C[cue], 0.4), align="left")
    alts_panel(c, t, C, ALT8, 860, 260, 860, 34, "30.ok", "B", 26)
    pause_timer(c, t, C["28.end"] - 1.9, 1560, 720)
    text(c, "Questão do material de estudo (seção 12)", 180, 860, 16, "medium", GRAY, a, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "ÚLTIMO EPISÓDIO DO ASSUNTO", "REVISÃO GERAL", PURPLE)
    rows = [("33.b", "juntamos tudo", GREEN), ("33.c", "caçamos as PEGADINHAS", AMBER), ("33.d", "QUESTÕES NOVAS", PURPLE)]
    for k, (cue, s, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 420, y - 16, a, 34, bg=col)
        text(c, s, 490, y, 56, "black", INK, a, align="left")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Quantas das seis você acertou no repete ou reparte?",
        canal="no Estudativo")


BLOCKS = dict(hook=b_hook, promessa=b_promessa, cenas=b_cenas, prereq=b_prereq, ancora=b_ancora, tabela=b_tabela, regua=b_regua,
              relacao=b_relacao, limite=b_limite, recap=b_recap, treino=b_treino, erros=b_erros, q9=b_q9, q8=b_q8,
              ponte=b_ponte, cta=b_cta)
