"""Visual — Logaritmos, Episódio 2: as três propriedades e o kit log 2 e log 3 (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, math_w, erro_cards, atalho, pause_timer...).
Peças deste episódio: fm() (fórmula com texto, potência e índice: "log_b (M · N)"), regua() (a régua de cálculo com o
trecho de 1 a 2 emendado ao de 1 a 3), virar() (o cartão da potência girando e virando a regra do log), porta() (a porta
trancada da soma), caixinhas()/tabela_kit() (o kit 2, 3 e 10 montando cada número), faixas() (a conferência dos inteiros),
alts() (alternativas com fórmulas).
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
_s = importlib.util.spec_from_file_location("comum042", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_logaritmos_ep2_propriedades_kit.mp4"
CARD_R = K.CARD_R
PAPEL = K.PAPEL
LOG2, LOG3 = math.log10(2), math.log10(3)


# ======================================================================
# tipografia: fórmula mista (texto + potência + índice)
# ======================================================================

def _fm_w(p, size):
    kind = p[2] if len(p) > 2 else "t"
    if kind == "m":
        return K.math_w(p[0], size)
    if kind == "sub":
        return text_w(p[0], "black", size * 0.56)
    return ftext_w(p[0], "black", size)


def fm_w(partes, size):
    return sum(_fm_w(p, size) for p in partes)


def fm(c, partes, cx, cy, size, a, align="center"):
    """partes = [(texto, cor[, tipo])]; tipo 't' texto (mantém espaços), 'm' expr (potência/fração: '2^3', '(M/N)'),
    'sub' índice (a base do log). Centrada verticalmente em cy; devolve a largura"""
    tw = fm_w(partes, size)
    if a <= 0:
        return tw
    x = cx - tw / 2 if align == "center" else (cx - tw if align == "right" else cx)
    for p in partes:
        s_, col = p[0], p[1] or INK
        kind = p[2] if len(p) > 2 else "t"
        w_ = _fm_w(p, size)
        if kind == "m":
            K.expr(c, s_, x, cy, size, a, cores={i: col for i in range(12)}, align="left")
        elif kind == "sub":
            text(c, s_, x, cy + size * 0.36 + size * 0.16, size * 0.56, "black", col, a, align="left")
        else:
            ftext(c, s_, x, cy + size * 0.36, size, "black", col, a, align="left")
        x += w_
    return tw


def LB(col=PURPLE):
    """'log' com a base b em índice"""
    return [("log", col), ("b", col, "sub")]


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def defi(c, s, cx, cy, a, size=28, col=BLUE):
    """pílula de definição (azul)"""
    if a <= 0:
        return
    pill(c, s, cx, cy, col, size=size, a=a, anchor="center", bounds=(0, 1920))


# ======================================================================
# peças do episódio
# ======================================================================

def regua(c, x0, y, L, a, shift=0.0, top_seg=0.0, bot_seg=0.0, bot=1.0, fim=0.0):
    """régua de cálculo: escala de cima fixa (1 a 10, cada n a L·log n de x0) e escala de baixo deslizando (shift = 1 põe
    o 1 de baixo sobre o 2 de cima). top_seg/bot_seg acendem os trechos de 1 a 2 (cima) e de 1 a 3 (baixo); fim marca o 6."""
    if a <= 0:
        return
    nums = range(1, 11)
    rrect(c, x0 - 40, y, L + 80, 92, 12, PAPEL, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 40, y, L + 80, 92), 12, 12), paint(PAPEL_B, a, stroke=2))
    for n in nums:
        x = x0 + L * math.log10(n)
        line(c, x, y + 92, x, y + 52, INK, a, 3)
        text(c, str(n), x, y + 40, 28, "black", INK, a)
        if n < 10:
            xm = x0 + L * math.log10(n + 0.5)
            line(c, xm, y + 92, xm, y + 70, INK2, a, 2)
    if top_seg > 0:
        rrect(c, x0, y + 58, L * LOG2 * top_seg, 26, 8, BLUE, a * 0.85)
    if bot <= 0:
        return
    bx0 = x0 + L * LOG2 * shift
    ab = a * bot
    rrect(c, bx0 - 40, y + 104, L + 80, 92, 12, "#FFFFFF", ab, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx0 - 40, y + 104, L + 80, 92), 12, 12), paint(PAPEL_B, ab, stroke=2))
    for n in nums:
        x = bx0 + L * math.log10(n)
        line(c, x, y + 104, x, y + 144, INK, ab, 3)
        text(c, str(n), x, y + 182, 28, "black", INK, ab)
        if n < 10:
            xm = bx0 + L * math.log10(n + 0.5)
            line(c, xm, y + 104, xm, y + 126, INK2, ab, 2)
    if bot_seg > 0:
        rrect(c, bx0, y + 112, L * LOG3 * bot_seg, 26, 8, GREEN, ab * 0.85)
    if fim > 0:
        x6 = x0 + L * math.log10(6)
        line(c, x6, y - 30, x6, y + 230, RED, a * fim, 4, dash=(12, 8))
        c.drawCircle(x6, y + 30, 30, paint(RED, a * fim, stroke=5))


PAPEL_B = getattr(K, "PAPEL_BORDA", "#D8D2C2")


def virar(c, cx, cy, w, h, u, a, frente, verso):
    """cartão que gira em torno do eixo vertical: u 0 → 0,5 mostra a frente encolhendo; 0,5 → 1 mostra o verso crescendo.
    frente/verso: funções (c) que desenham o conteúdo centrado em (0, 0)"""
    if a <= 0:
        return
    k = math.cos(math.pi * clamp(u))
    sx = max(0.02, abs(k))
    c.save(); c.translate(cx, cy); c.scale(sx, 1)
    lado = frente if k >= 0 else verso
    col = BLUE if k >= 0 else PURPLE
    rrect(c, -w / 2, -h / 2, w, h, 30, mix("#FFFFFF", col, 0.10), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 30, 30), paint(col, a, stroke=4))
    lado(c)
    c.restore()


def porta(c, cx, cy, s, a, cad=1.0):
    """porta trancada com cadeado (cad: alfa do cadeado)"""
    if a <= 0:
        return
    w, h = s * 0.62, s
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, mix("#FFFFFF", AMBER, 0.55), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14),
                paint(mix(AMBER, INK, 0.35), a, stroke=5))
    for k in range(2):
        rrect(c, cx - w / 2 + 22, cy - h / 2 + 24 + k * h * 0.48, w - 44, h * 0.4, 8, mix("#FFFFFF", AMBER, 0.35), a)
    c.drawCircle(cx + w * 0.32, cy + 8, 9, paint(INK, a))
    if cad > 0:
        bx, by = cx + w * 0.32, cy + 70
        p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(bx - 26, by - 52, 52, 60), 180, 180)
        c.drawPath(p, paint(INK2, a * cad, stroke=9))
        rrect(c, bx - 38, by - 22, 76, 64, 10, RED, a * cad, shadow=True)
        c.drawCircle(bx, by + 6, 8, paint("#FFFFFF", a * cad))


KITBOX = [("log 2", "0,301", BLUE), ("log 3", "0,477", GREEN), ("log 10", "1", PURPLE)]


def caixinhas(c, x, y, a, alfas=(1, 1, 1), w=340, h=150, gap=34, vertical=True, size=44):
    """as três caixinhas do kit"""
    for k, (s_, v, col) in enumerate(KITBOX):
        ak = a * alfas[k]
        if ak <= 0:
            continue
        xx, yy = (x, y + k * (h + gap)) if vertical else (x + k * (w + gap), y)
        rrect(c, xx, yy, w, h, 22, mix("#FFFFFF", col, 0.12), ak, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, yy, w, h), 22, 22), paint(col, ak, stroke=4))
        text(c, s_, xx + w / 2, yy + h * 0.36, size * 0.62, "black", col, ak)
        text_mid(c, ("≈ " if v != "1" else "= ") + v, xx + w / 2, yy + h * 0.68, size, "black", INK, ak)


KIT = [("4", "2^2", [("2 · ", INK), ("0,301", BLUE), (" = 0,602", INK)]),
       ("6", "2·3", [("0,301", BLUE), (" + ", INK), ("0,477", GREEN), (" = 0,778", INK)]),
       ("9", "3^2", [("2 · ", INK), ("0,477", GREEN), (" = 0,954", INK)]),
       ("12", "2^2·3", [("0,602 + ", INK), ("0,477", GREEN), (" = 1,079", INK)]),
       ("5", "10/2", [("1", PURPLE), (" − ", INK), ("0,301", BLUE), (" = 0,699", INK)]),
       ("1,5", "3/2", [("0,477", GREEN), (" − ", INK), ("0,301", BLUE), (" = 0,176", INK)]),
       ("0,9", "9/10", [("0,954 − ", INK), ("1", PURPLE), (" = −0,046", RED)]),
       ("0,2", "2/10", [("0,301", BLUE), (" − ", INK), ("1", PURPLE), (" = −0,699", RED)])]
KIT_CUES = ["15.a", "15.b", "15.c", "15.d", "16.a", "16.b", "17.a", "17.b"]


def tabela_kit(c, t, C, a, x=200, y=272, rh=64, destaca_neg=0.0):
    """a tabela do kit montada linha a linha (número · decomposição · log)"""
    if a <= 0:
        return
    cols = (x, x + 200, x + 500)
    rrect(c, x - 20, y, 1080, 52, 12, mix("#FFFFFF", PURPLE, 0.14), a)
    for s_, xx in zip(("número", "decomposição", "logaritmo"), (cols[0] + 80, cols[1] + 130, cols[2] + 280)):
        text_mid(c, s_, xx, y + 26, 26, "black", PURPLE, a)
    for k, (n, dec, partes) in enumerate(KIT):
        ak, d = rise(t, C[KIT_CUES[k]])
        ak *= a
        if ak <= 0:
            continue
        yy = y + 52 + k * rh
        neg = k >= 6
        bg = mix("#FFFFFF", RED, 0.10 * destaca_neg) if neg else "#FFFFFF"
        rrect(c, x - 20, yy + 4 + d, 1080, rh - 8, 10, bg, ak, shadow=True)
        text_mid(c, n, cols[0] + 80, yy + rh / 2 + d, 36, "black", RED if neg and destaca_neg > 0.5 else INK, ak)
        K.expr(c, dec, cols[1] + 130, yy + rh / 2 + d, 30 if "/" not in dec else 26, ak, cores={0: INK2})
        fm(c, partes, cols[2] + 280, yy + rh / 2 + d, 32, ak)


def faixas(c, t, C, y, a):
    """a conferência dos inteiros: três faixas (0 a 1 · 1 a 10 · 10 a 100)"""
    rows = [("17", "a", "entre 1 e 10", "log entre 0 e 1", BLUE), ("18", "b", "entre 10 e 100", "log entre 1 e 2", PURPLE),
            ("18", "c", "entre 0 e 1", "log NEGATIVO", RED)]
    for k, (sid, cue, n, lg, col) in enumerate(rows):
        ak = ep(t, C[f"18.{cue}"], 0.5) * a
        if ak <= 0:
            continue
        x = 220 + k * 500
        rrect(c, x, y, 460, 250, 24, "#FFFFFF", ak, shadow=True)
        rrect(c, x, y, 460, 60, 24, col, ak * 0.14)
        text(c, "NÚMERO", x + 230, y + 42, 22, "black", col, ak, tracking=2)
        text_mid(c, n, x + 230, y + 105, 40, "black", INK, ak)
        arrow(c, x + 230, y + 138, x + 230, y + 178, GRAY, ak, 4, 12)
        text_mid(c, lg, x + 230, y + 212, 38, "black", col, ak)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "LOGARITMOS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 170, 28, mix("#FFFFFF", AMBER, 0.12), aa, shadow=True)
        fm(c, [("log(10 + 10)", INK), ("  =  ", AMBER), ("log 10 + log 10", INK), ("  ?", AMBER)], W / 2, 305, 72, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 450, 660, 180, 24, "#FFFFFF", ab, shadow=True)
        text(c, "TESTE: o lado esquerdo", 590, 500, 24, "black", GRAY, ab, tracking=1)
        fm(c, [("log 20 ≈ ", INK), ("1,30", BLUE)], 590, 570, 60, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 450, 660, 180, 24, "#FFFFFF", acc, shadow=True)
        text(c, "o lado direito", 1330, 500, 24, "black", GRAY, acc, tracking=1)
        fm(c, [("1 + 1 = ", INK), ("2", PURPLE)], 1330, 570, 60, acc)
        text_mid(c, "≠", W / 2 - 0, 540, 90, "black", RED, ep(t, C["01.c"] + 1.0, 0.4))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        strike(c, 300, 305, 1620, 305, ad, RED, ad)
        selo(c, 600, 745, ad, "PARECE ÓBVIA · ESTÁ ERRADA", RED, -4, 34)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        pill(c, "a alternativa com ela SEMPRE aparece", 1360, 775, AMBER, size=30, a=ae, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    aa, d = rise(t, C["02.a"])
    if aa > 0:
        text(c, "usar as 3 propriedades", W / 2, 300 + d, 46, "black", INK, aa)
    props = [("produto", "soma"), ("quociente", "diferença"), ("expoente", "desce ×")]
    for k, (p_, q_) in enumerate(props):
        ak = ep(t, C["02.a"] + 1.4 + 0.6 * k, 0.4)
        x = 480 + k * 480
        chip(c, p_, x, 390, PURPLE, ak, 36)
        arrow(c, x, 435, x, 480, GRAY, ak, 4, 12)
        chip(c, q_, x, 525, PURPLE, ak, 36, fill=False)
    ab = ep(t, C["02.b"], 0.5)
    if ab > 0:
        text(c, "e calcular muitos logs só com", W / 2, 640, 36, "black", INK, ab)
        chip(c, "log 2", 820, 730, BLUE, ab, 40)
        chip(c, "log 3", 1100, 730, GREEN, ab, 40)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "série de Potenciação", 520, 270, 26, "bold", GRAY, aa)
        rrect(c, 200, 300, 640, 420, 22, "#FFFFFF", aa, shadow=True)
        for k, (s_, why) in enumerate((("a^m · a^n = a^{m+n}", "multiplicou: SOMA"), ("a^m ÷ a^n = a^{m-n}", "dividiu: SUBTRAI"),
                                       ("(a^m)^n = a^{m·n}", "potência de potência: MULTIPLICA"))):
            ak = ep(t, C["03.a"] + 1.6 * k, 0.4) * aa
            K.expr(c, s_, 520, 380 + k * 125, 50, ak, cores={i: PURPLE for i in range(8)})
            text(c, why, 520, 432 + k * 125, 22, "bold", GRAY, ak)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "série de Divisibilidade", 1260, 270, 26, "bold", GRAY, ab)
        rrect(c, 960, 300, 600, 170, 22, "#FFFFFF", ab, shadow=True)
        K.expr(c, "72 = 2^3 · 3^2", 1260, 385, 60, ab, cores={0: INK, 1: INK, 2: BLUE, 3: INK, 4: GREEN})
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        text(c, "episódio 1", 1260, 520, 26, "bold", GRAY, acc)
        rrect(c, 960, 550, 600, 170, 22, mix("#FFFFFF", BLUE, 0.10), acc)
        text_mid(c, "log  =  EXPOENTE", 1260, 605, 44, "black", BLUE, acc)
        fm(c, [("log 100 = 2  ⟺  ", INK), ("10^2", INK, "m"), (" = 100", INK)], 1260, 670, 34, acc)


# ======================================================================
# concreto: a régua de cálculo
# ======================================================================

def b_regua(c, t, C, B):
    head_seq(c, t, C, [("04", "ANTES DA CALCULADORA", "A RÉGUA DE CÁLCULO", BLUE),
                       ("05", "POR QUE FUNCIONA?", "COMPRIMENTO = LOG", BLUE)])
    card(c, *CARD_R)
    x0, y, L = 300, 330, 1200
    a0 = ep(t, C["04.a"], 0.5)
    if a0 > 0:
        defi(c, "RÉGUA DE CÁLCULO = multiplica somando comprimentos", W / 2, 230, a0 * (1 - ep(t, C["05"], 0.3)), 28)
    tb = ep(t, C["04.b"], 1.0)
    sh = ep(t, C["04.c"], 1.2)
    bs = ep(t, C["04.c"] + 1.2, 0.9)
    fim = ep(t, C["04.d"], 0.5)
    regua(c, x0, y, L, a0, sh, tb, bs, a0, fim)
    if tb > 0:
        pill(c, "de 1 até 2", x0 + L * LOG2 / 2, y - 40, BLUE, size=22, a=tb, anchor="center")
    if bs > 0:
        bx0 = x0 + L * LOG2 * sh
        pill(c, "de 1 até 3", bx0 + L * LOG3 / 2, y + 250, GREEN, size=22, a=bs, anchor="center")
    if fim > 0:
        text_mid(c, "2 × 3 = 6", W / 2, 680, 64, "black", RED, fim)
    sid = which(t, C, ["04", "05"])
    if sid != "05":
        return
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        pill(c, "cada número fica a uma distância = SEU LOG", W / 2, 230, BLUE, size=28, a=aa, anchor="center",
             bounds=(0, 1920))
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 610, 1200, 140, 26, mix("#FFFFFF", PURPLE, 0.10), ab)
        fm(c, [("log 2", BLUE), (" + ", INK), ("log 3", GREEN), (" = ", INK), ("log 6", RED)], W / 2, 680,
           70, ab)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        selo(c, 1540, 780, ad, "1ª PROPRIEDADE", PURPLE, -4, 30)


# ======================================================================
# bloco a — produto vira soma
# ======================================================================

def b_produto(c, t, C, B):
    head_seq(c, t, C, [("06", "PROPRIEDADE 1", "PRODUTO VIRA SOMA", PURPLE),
                       ("07", "DE ONDE VEM?", "A POTÊNCIA LIDA DE TRÁS PARA FRENTE", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        defi(c, "PROPRIEDADE OPERATÓRIA = regra que transforma uma conta em outra", W / 2, 235, aa, 26)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            rrect(c, 300, 300, 1320, 170, 28, mix("#FFFFFF", PURPLE, 0.10), ab)
            fm(c, LB() + [("(M · N) = ", PURPLE)] + LB() + [(" M + ", PURPLE)] + LB() + [(" N", PURPLE)], W / 2, 385, 74, ab)
            defi(c, "PRODUTO = resultado de uma multiplicação", W / 2, 510, ep(t, C["06.b"] + 2.4, 0.4), 24)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 580, 680, 160, 22, "#FFFFFF", acc, shadow=True)
            text(c, "TESTE", 600, 618, 22, "black", GRAY, acc, tracking=2)
            fm(c, [("log(10 · 100) = log 1000 = ", INK), ("3", GREEN)], 600, 680, 36, acc)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            rrect(c, 980, 580, 680, 160, 22, "#FFFFFF", ad, shadow=True)
            text(c, "E A SOMA", 1320, 618, 22, "black", GRAY, ad, tracking=2)
            fm(c, [("log 10 + log 100 = 1 + 2 = ", INK), ("3", GREEN)], 1320, 680, 36, ad)
            conferido(c, "bateu", 1240, 790, ep(t, C["06.d"] + 2.0, 0.4), True, 30)
        return
    # cena 07: o cartão da potência gira e vira a regra do log
    u = ep(t, C["07.c"], 1.4)

    def frente(cc):
        fm(cc, [("b^x", INK, "m"), (" · ", INK), ("b^y", INK, "m"), (" = ", INK), ("b^{x+y}", BLUE, "m")], 0, -10, 80, 1.0)
        text(cc, "potências: multiplicar SOMA os expoentes", 0, 90, 26, "bold", GRAY, 1.0)

    def verso(cc):
        fm(cc, [("log(M · N) = log M + log N", PURPLE)], 0, -10, 62, 1.0)
        text(cc, "log é expoente: o produto vira SOMA", 0, 90, 26, "bold", GRAY, 1.0)

    aa = ep(t, C["07.a"], 0.5)
    virar(c, W / 2, 440, 1240, 300, u, aa, frente, verso)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0 and u < 0.5:
        pill(c, "x + y: os expoentes se SOMAM", 1400, 640, BLUE, size=26, a=ab * (1 - 2 * u), anchor="center")
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        chip(c, "log = expoente", 560, 650, BLUE, acc, 34)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        regra(c, "as regras de potência LIDAS DE TRÁS PARA FRENTE", W / 2, 760, ad, 38)


# ======================================================================
# bloco b — quociente vira diferença
# ======================================================================

def b_quociente(c, t, C, B):
    head(c, t, B["start"], "PROPRIEDADE 2", "QUOCIENTE VIRA DIFERENÇA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    defi(c, "QUOCIENTE = resultado de uma divisão", W / 2, 235, aa, 28)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 300, 1320, 200, 28, mix("#FFFFFF", PURPLE, 0.10), ab)
        fm(c, LB() + [("(M/N)", PURPLE, "m"), (" = ", PURPLE)] + LB() + [(" M − ", PURPLE)] + LB() + [(" N", PURPLE)],
           W / 2, 400, 74, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 580, 680, 160, 22, "#FFFFFF", acc, shadow=True)
        text(c, "TESTE", 600, 618, 22, "black", GRAY, acc, tracking=2)
        fm(c, [("log(1000 ÷ 10) = log 100 = ", INK), ("2", GREEN)], 600, 680, 34, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 980, 580, 680, 160, 22, "#FFFFFF", ad, shadow=True)
        text(c, "E A DIFERENÇA", 1320, 618, 22, "black", GRAY, ad, tracking=2)
        fm(c, [("log 1000 − log 10 = 3 − 1 = ", INK), ("2", GREEN)], 1320, 680, 34, ad)
        conferido(c, "bateu", 1240, 790, ep(t, C["08.d"] + 1.2, 0.4), True, 30)


# ======================================================================
# bloco c — expoente desce multiplicando
# ======================================================================

def b_potencia(c, t, C, B):
    head_seq(c, t, C, [("09", "PROPRIEDADE 3", "O EXPOENTE DESCE MULTIPLICANDO", PURPLE),
                       ("10", "VALE PARA RAIZ?", "RAIZ É EXPOENTE 1/2", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        if aa > 0:
            defi(c, "POTÊNCIA = número multiplicado por ele mesmo", 760, 235, aa, 26)
            K.expr(c, "10^3 = 10 · 10 · 10", 1480, 235, 40, aa, cores={0: BLUE})
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            rrect(c, 300, 310, 1320, 220, 28, mix("#FFFFFF", PURPLE, 0.10), ab)
            u = ep(t, C["09.b"] + 1.6, 1.2)
            # o k sai do expoente e desce para a frente
            cx, cy = W / 2, 420
            wl = fm_w(LB() + [(" M", PURPLE)], 74)
            xr = cx - 70                                     # fim do lado esquerdo
            fm(c, LB() + [(" M", PURPLE)], xr - wl, cy, 74, ab, align="left")
            kx0, ky0 = xr + 22, cy - 46
            kx1, ky1 = cx + 90, cy
            uu = ease_io(u)
            kx, ky = lerp(kx0, kx1, uu), lerp(ky0, ky1, uu)
            text_mid(c, "k", kx, ky, lerp(44, 74, uu), "black", AMBER, ab)
            fm(c, [("=", PURPLE)], cx, cy, 74, ab)
            fm(c, [(" · ", PURPLE)] + LB() + [(" M", PURPLE)], cx + 125, cy, 74, ab * ep(t, C["09.b"] + 1.6, 0.6), align="left")
            if 0.05 < u < 0.95:
                pill(c, "o expoente DESCE", cx - 240, cy + 80, AMBER, size=22, a=ab, anchor="center")
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            rrect(c, 260, 600, 1400, 150, 22, "#FFFFFF", acc, shadow=True)
            fm(c, [("log ", INK), ("10^3", INK, "m"), (" = log 1000 = ", INK), ("3", GREEN), ("        3 · log 10 = 3 · 1 = ", INK),
                   ("3", GREEN)], W / 2, 675, 40, acc)
            conferido(c, "bateu", 1240, 800, ep(t, C["09.c"] + 2.4, 0.4), True, 30)
        return
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 240, 1320, 160, 26, "#FFFFFF", aa, shadow=True)
        fm(c, [("√{2}", INK, "m"), (" = ", INK), ("2^{1/2}", BLUE, "m")], W / 2, 320, 80, aa)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 450, 1320, 160, 26, mix("#FFFFFF", PURPLE, 0.10), ab)
        fm(c, [("log ", PURPLE), ("√{2}", PURPLE, "m"), (" = ", PURPLE), ("1/2", AMBER, "m"), (" · log 2", PURPLE)],
           W / 2, 530, 72, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        fm(c, [("≈ 0,301 ÷ 2 ≈ ", INK), ("0,15", GREEN)], W / 2, 700, 56, acc)


# ======================================================================
# atalho: as três numa linha
# ======================================================================

def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DENTRO DO LOG → FORA DO LOG", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 90, "TRADUÇÃO DIRETA", [""], aa, 30)
    rows = [("×", "+", "vezes vira MAIS"), ("÷", "−", "dividir vira MENOS"), ("expoente", "frente", "o expoente vai para a FRENTE")]
    for k, (dentro, fora, s_) in enumerate(rows):
        ak = ep(t, C["11.a"] + 0.9 * k, 0.4)
        if ak <= 0:
            continue
        x = 300 + k * 450
        rrect(c, x, 310, 420, 230, 22, "#FFFFFF", ak, shadow=True)
        text(c, "dentro", x + 105, 350, 22, "bold", GRAY, ak)
        text(c, "fora", x + 315, 350, 22, "bold", GRAY, ak)
        text_mid(c, dentro, x + 105, 420, 44 if len(dentro) < 3 else 30, "black", INK, ak)
        arrow(c, x + 175, 420, x + 245, 420, GREEN, ak, 4, 12)
        text_mid(c, fora, x + 315, 420, 44 if len(fora) < 3 else 30, "black", GREEN, ak)
        text(c, s_, x + 210, 510, 22, "black", GREEN, ak)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        boxed(c, 300, 590, 1320, 170, GREEN, ab, 0.08)
        text(c, "NA DÚVIDA, TESTE COM 10 E 100", W / 2, 640, 26, "black", GREEN, ab, tracking=2)
        fm(c, [("log 10 = ", INK), ("1", GREEN), ("        log 100 = ", INK), ("2", GREEN)], W / 2, 705, 46, ab)


# ======================================================================
# bloco d — o que as propriedades não dizem
# ======================================================================

def b_naodizem(c, t, C, B):
    head_seq(c, t, C, [("12", "O QUE ELAS NÃO DIZEM", "SOMA DENTRO DO LOG", AMBER),
                       ("13", "O QUE ELAS NÃO DIZEM", "UM LOG DIVIDIDO PELO OUTRO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            fm(c, [("log(M + N) = ", INK), ("???", RED)], 1080, 300, 72, aa)
            pill(c, "NÃO TEM REGRA", 1080, 390, RED, size=30, a=aa, anchor="center")
        ab = ep(t, C["12.b"], 0.5)
        porta(c, 430, 500, 480, ab, ep(t, C["12.b"] + 0.6, 0.4))
        if ab > 0:
            text(c, "PORTA TRANCADA", 430, 800, 30, "black", AMBER, ab, tracking=2)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            rrect(c, 760, 480, 860, 240, 24, "#FFFFFF", acc, shadow=True)
            text(c, "O TESTE DO COMEÇO", 1190, 525, 22, "black", GRAY, acc, tracking=2)
            fm(c, [("log 20 ≈ ", INK), ("1,30", BLUE)], 1190, 600, 48, acc)
            fm(c, [("log 10 + log 10 = ", INK), ("2", PURPLE)], 1190, 670, 48, acc)
            text_mid(c, "≠", 1560, 635, 80, "black", RED, ep(t, C["12.c"] + 1.4, 0.4))
        return
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 240, 1320, 200, 26, mix("#FFFFFF", AMBER, 0.10), aa)
        fm(c, [("log M ÷ log N", INK), ("   ≠   ", RED), ("log M − log N", INK)], W / 2, 340, 66, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 500, 680, 200, 22, "#FFFFFF", ab, shadow=True)
        text(c, "COM 1000 E 10", 600, 545, 22, "black", GRAY, ab, tracking=2)
        fm(c, [("log 1000 ÷ log 10 = 3 ÷ 1 = ", INK), ("3", BLUE)], 600, 620, 32, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 500, 680, 200, 22, "#FFFFFF", acc, shadow=True)
        text(c, "E A DIFERENÇA", 1320, 545, 22, "black", GRAY, acc, tracking=2)
        fm(c, [("log 1000 − log 10 = 3 − 1 = ", INK), ("2", PURPLE)], 1320, 620, 32, acc)
        selo(c, W / 2, 780, ep(t, C["13.c"] + 1.6, 0.4), "NÃO BATE", RED, -4, 36)


# ======================================================================
# bloco e — o kit · bloco f — menor que 1, log negativo
# ======================================================================

def b_kit(c, t, C, B):
    head_seq(c, t, C, [("14", "O KIT", "2, 3 E 10", GREEN), ("15", "O KIT", "MONTANDO AS PEÇAS", GREEN),
                       ("16", "O KIT", "E COM DIVISÃO?", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16"])
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        alf = [ep(t, C["14.a"] + 1.6 * k, 0.4) for k in range(3)]
        caixinhas(c, 220, 205, aa, alf, 360, 180, 30)
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            rrect(c, 680, 220, 1000, 220, 24, mix("#FFFFFF", BLUE, 0.08), ab)
            text(c, "DECOMPOSIÇÃO EM FATORES PRIMOS", 1180, 270, 26, "black", BLUE, ab, tracking=2)
            text(c, "escrever o número como produto de primos", 1180, 320, 28, "bold", INK2, ab)
            K.expr(c, "12 = 2 · 2 · 3 = 2^2 · 3", 1180, 390, 46, ab, cores={0: INK})
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            rrect(c, 680, 490, 1000, 290, 24, "#FFFFFF", acc, shadow=True)
            text(c, "SAI DO KIT: todo número feito de", 1180, 545, 28, "black", INK, acc)
            for k, (n, col) in enumerate((("2", BLUE), ("3", GREEN), ("5", AMBER))):
                chip(c, n, 1020 + k * 160, 620, col, acc, 46)
            a5 = ep(t, C["14.c"] + 3.2, 0.5)
            if a5 > 0:
                fm(c, [("5 = 10 ÷ 2", AMBER)], 1180, 720, 46, a5)
                pill(c, "1 − 0,301", 1520, 720, PURPLE, size=24, a=a5, anchor="center")
        return
    caixinhas(c, 1400, 250, 1.0, (1, 1, 1), 320, 150, 26, True, 40)
    tabela_kit(c, t, C, 1.0, 230, 232, 64)


def b_negativo(c, t, C, B):
    head(c, t, B["start"], "MENOR QUE 1?", "LOG NEGATIVO", RED)
    card(c, *CARD_R)
    hl = ep(t, C["17.a"], 0.5)
    tabela_kit(c, t, C, 1.0, 230, 232, 64, destaca_neg=hl)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        rrect(c, 1380, 300, 360, 220, 22, mix("#FFFFFF", RED, 0.10), acc, shadow=True)
        fm(c, [("10^{negativo}", RED, "m")], 1560, 380, 48, acc)
        text(c, "dá MENOS que 1", 1560, 470, 28, "black", RED, acc)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        rrect(c, 1380, 570, 360, 220, 22, mix("#FFFFFF", AMBER, 0.12), ad, shadow=True)
        text(c, "log 0,9 > 0 ?", 1560, 640, 34, "black", INK, ad)
        text(c, "ERRO DE SINAL", 1560, 700, 30, "black", AMBER, ad)
        text(c, "(decisivo no ep. 3)", 1560, 750, 22, "bold", GRAY, ad)


def b_atalho2(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "CONFIRA PELOS INTEIROS", GREEN)
    card(c, *CARD_R)
    K.atalho(c, 260, 200, 1400, 90, "ONDE O LOG TEM QUE CAIR", [""], ep(t, C["18"], 0.5), 30)
    faixas(c, t, C, 330, 1.0)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 640, 1000, 120, 24, mix("#FFFFFF", GREEN, 0.10), ad)
        fm(c, [("12 está entre 10 e 100  →  log 12 = ", INK), ("1,079", GREEN)], W / 2, 700, 40, ad)
        conferido(c, "bateu", 1500, 800, ep(t, C["18.d"] + 1.6, 0.4), True, 30)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "DECOMPONHA E USE O KIT", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 210, 1460, 130, 24, "#F7F7F5", aa)
        fm(c, [("log 2 = ", INK), ("0,30", BLUE), ("      log 3 = ", INK), ("0,48", GREEN)], W / 2, 250, 40, aa)
        text(c, "log 18 = ?", W / 2, 320, 36, "black", PURPLE, aa)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 560)
    if t < C["20"]:
        return
    steps = [("20.a", [("18 = 2 · 9 = 2 · ", INK), ("3^2", GREEN, "m")]),
             ("20.b", [("log 18 = ", INK), ("log 2", BLUE), (" + 2 · ", INK), ("log 3", GREEN)]),
             ("20.c", [("= ", INK), ("0,30", BLUE), (" + 2 · ", INK), ("0,48", GREEN), (" = 0,30 + 0,96 = ", INK),
                       ("1,26", GREEN)])]
    for k, (cue, partes) in enumerate(steps):
        ak, d = rise(t, C[cue])
        fm(c, partes, W / 2, 420 + k * 105 + d, 48, ak)
    ad = ep(t, C["20.d"], 0.5)
    if ad > 0:
        conferido(c, "entre 10 e 100 → log entre 1 e 2", 600, 760, ad, True, 34)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Produto vira soma, quociente vira diferença, expoente desce multiplicando.",
          "Soma dentro do log não tem regra.",
          "Número entre 0 e 1 tem log negativo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "35"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("log(M + N)  =  log M + log N", "lembra a regra do produto",
          "a soma de fora só aparece quando DENTRO tem VEZES: log(M · N)"),
         ("log M ÷ log N  =  log M − log N", "tem divisão e diferença",
          "a diferença é log(M ÷ N) · teste: 3 ÷ 2 = 1,5, e não 1"),
         ("log 72  =  log 8 · log 9", "72 é 8 · 9",
          "o vezes de dentro vira MAIS fora: log 8 + log 9"),
         ("log 0,9  >  0", "log 9 é positivo",
          "0,9 = 9 ÷ 10: 0,954 − 1 = −0,046 (negativo)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24", "25"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


def alts(c, t, C, itens, x, y0, size, ok_cue, okL, cues_in, cues_x, gap=26):
    """alternativas com fórmula mista: itens = [(letra, partes_fm, motivo)]"""
    aok = ep(t, ok_cue, 0.5)
    y = y0
    hh = size * 1.7
    for L, partes, why in itens:
        a, d = rise(t, cues_in.get(L, 1e9))
        ok = L == okL
        ax = ep(t, cues_x.get(L, 1e9), 0.4) if not ok else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - 10 + d, 720, hh + 20, 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + hh / 2 + d, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
            cyy = y + d + hh / 2
            w_ = fm(c, partes, x + 50, cyy, size, a * (1 - 0.5 * ax), align="left")
            if ax > 0:
                strike(c, x + 46, cyy, x + 54 + w_, cyy, ax, RED, ax)
                if why:
                    pill(c, why, x + 700, cyy + size * 0.95, RED, size=18, a=ax, anchor="right", bounds=(0, 1920))
        y += hh + gap
    return y


def enunciado(c, s, a, y=240, size=26, maxw=700):
    for ln in K.wrap(s, "black", size, maxw):
        ftext(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 10
    return y


ALTS2 = [("A", [("0,78", INK)], "log 2 + log 3 = log 6"), ("B", [("0,864", INK)], "log 8 · log 9: multiplicou"),
         ("C", [("0,96", INK)], "só log 9"), ("D", [("1,38", INK)], "log 24: esqueceu o 2 do 3²"),
         ("E", [("1,86", INK)], "")]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "LOGARITMO POR DECOMPOSIÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    y = enunciado(c, "Um técnico precisa do valor de log 72, mas dispõe apenas das aproximações log 2 = 0,30 e "
                     "log 3 = 0,48. Usando corretamente as propriedades dos logaritmos, ele obtém para log 72 o valor",
                  a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["27"], 0.3)),
         align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABCD"}
    alts(c, t, C, ALTS2, 1000, 250, 44, C["27.ok"], "E", cues_in, cues_x)
    if t < C["27"]:
        return
    y0 = y + 14
    _painel(c, y0, ep(t, C["27"], 0.4))
    fm(c, [("72 = 8 · 9 = ", INK), ("2^3", BLUE, "m"), (" · ", INK), ("3^2", GREEN, "m")], 540, y0 + 55, 36,
       ep(t, C["27.a"], 0.4))
    fm(c, [("3 · ", BLUE), ("0,30", BLUE), (" = 0,90", INK)], 540, y0 + 135, 36, ep(t, C["27.b"], 0.4))
    fm(c, [("+ 2 · ", GREEN), ("0,48", GREEN), (" = 0,96", INK)], 540, y0 + 205, 36, ep(t, C["27.c"], 0.4))
    ad = ep(t, C["27.d"], 0.4)
    if ad > 0:
        fm(c, [("log 72 = ", INK), ("1,86", GREEN)], 540, y0 + 280, 42, ad)
        pill(c, "10 < 72 < 100 → entre 1 e 2", 540, y0 + 345, GREEN, size=22, a=ad, anchor="center")


ALTS9 = [("A", [("b − a", INK)], ""), ("B", [("a − b", INK)], "log(2/3): negativo"),
         ("C", [("a + b", INK)], "log 6"), ("D", [("b/a", INK, "m")], "log de 3 na base 2"),
         ("E", [("1 + b − a", INK)], "log 15: 1,5 virou 15")]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · NÓS FAZEMOS", "UM LOGARITMO EM LETRAS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    y = enunciado(c, "Em uma tabela antiga, os valores de log 2 e log 3 aparecem indicados por a e b, respectivamente. "
                     "Em função de a e b, o valor de log 1,5 é", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["30"], 0.3)),
         align="left")
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "BCDE"}
    alts(c, t, C, ALTS9, 1000, 250, 44, C["30.ok"], "A", cues_in, cues_x)
    ap = ep(t, C["29.p"], 0.4) * (1 - ep(t, C["30"], 0.4))
    if ap > 0:
        fm(c, [("1,5 = ", INK), ("?", AMBER), (" ÷ ", INK), ("?", AMBER)], 540, y + 120, 60, ap)
    if t < C["30"]:
        return
    y0 = y + 14
    _painel(c, y0, ep(t, C["30"], 0.4))
    fm(c, [("1,5 = 3 ÷ 2", INK)], 540, y0 + 55, 40, ep(t, C["30"], 0.4))
    fm(c, [("log 1,5 = ", INK), ("log 3", GREEN), (" − ", INK), ("log 2", BLUE)], 540, y0 + 135, 36,
       ep(t, C["30.a"], 0.4))
    fm(c, [("= ", INK), ("b", GREEN), (" − ", INK), ("a", BLUE)], 540, y0 + 210, 44, ep(t, C["30.b"], 0.4))
    acc = ep(t, C["30.c"], 0.4)
    if acc > 0:
        conferido(c, "0,477 − 0,301 = 0,176 > 0", 250, y0 + 295, acc, True, 28)


ALTS7 = [("A", [("I e II", INK)], "aceita a I (falsa)"), ("B", [("II e IV", INK)], ""),
         ("C", [("II e III", INK)], "aceita a III (falsa)"), ("D", [("I, II e IV", INK)], "aceita a I (falsa)"),
         ("E", [("III e IV", INK)], "aceita a III e tira a II")]
AFIRM = [("I", [("I.  log(a + b) = log a + log b", INK)]), ("II", [("II.  log ", INK), ("a^3", INK, "m"), (" = 3 log a", INK)]),
         ("III", [("III.  log(a ÷ b) = log a ÷ log b", INK)]), ("IV", [("IV.  log 1 = 0", INK)])]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · VOCÊ FAZ", "VERDADEIRAS OU FALSAS?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["32.a"], 0.4)
    y = enunciado(c, "Um estudante escreveu as igualdades abaixo, com a e b reais positivos e logaritmos decimais.", a0)
    ab = ep(t, C["32.b"], 0.4)
    marcas = {"II": (C["33.a"], True), "IV": (C["33.b"], True), "I": (C["33.c"], False), "III": (C["33.d"], False)}
    yy = y + 20
    for k, (rot, partes) in enumerate(AFIRM):
        ak = ab * ep(t, C["32.b"] + 2.6 * k, 0.4)
        if ak > 0:
            rrect(c, 180, yy - 30, 720, 64, 12, "#F7F7F5", ak)
            fm(c, partes, 200, yy, 30, ak, align="left")
            tm, ok = marcas[rot]
            am = ep(t, tm, 0.4)
            if am > 0:
                check_icon(c, 860, yy, 22, am, GREEN if ok else RED, "check" if ok else "x")
        yy += 82
    acc = ep(t, C["32.c"], 0.4)
    if acc > 0:
        text(c, "São verdadeiras para todos os valores positivos apenas:", 190, yy + 10, 24, "black", INK, acc,
             align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["33"], 0.3)),
         align="left")
    cues_in = {L: C[f"32.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"34.x{L.lower()}"] for L in "ACDE"}
    alts(c, t, C, ALTS7, 1000, 250, 44, C["33.ok"], "B", cues_in, cues_x)
    if t < C["33"]:
        pause_timer(c, t, C["32.end"] - 1.9, 760, 770)
        return
    for cue, s_, yv in (("33.c", "I: com a = b = 10 → 1,30 ≠ 2", 760), ("33.d", "III: com a = 100, b = 10 → 1 ≠ 2", 800)):
        ak = ep(t, C[cue], 0.4) * (1 - ep(t, C["34"], 0.4))
        if ak > 0:
            pill(c, s_, 190, yv, RED, size=20, a=ak, bounds=(0, 1920))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TIRANDO O t DO EXPOENTE", PURPLE)
    aa = ep(t, C["36.a"], 0.5)
    if aa > 0:
        rrect(c, 460, 250, 1000, 230, 30, "#FFFFFF", aa, shadow=True)
        fm(c, [("1,08^t", INK, "m"), (" = 2", INK)], W / 2, 365, 120, aa)
    ab = ep(t, C["36.b"], 0.5)
    if ab > 0:
        pill(c, "o t está PRESO no expoente", 760, 560, AMBER, size=30, a=ab, anchor="center")
        pill(c, "2 não é potência de 1,08", 1240, 560, AMBER, size=30, a=ab, anchor="center")
    acc = ep(t, C["36.c"], 0.5)
    if acc > 0:
        text_mid(c, "como derrubar esse t?", W / 2, 680, 60, "black", PURPLE, acc)
    pill(c, "ep. 3 · equações com log e mudança de base", W / 2, 790, PURPLE, size=30, a=ep(t, C["36.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["37.like"], C["37.sub"], C["37.bell"], C["37.com"], C["37.bye"],
        "Você já tinha caído no log(10 + 10)?", canal="no Estudativo", anki=C["37.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, regua=b_regua, produto=b_produto, quociente=b_quociente,
              potencia=b_potencia, atalho=b_atalho, naodizem=b_naodizem, kit=b_kit, negativo=b_negativo,
              atalho2=b_atalho2, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q9=b_q9, q7=b_q7,
              ponte=b_ponte, cta=b_cta)
