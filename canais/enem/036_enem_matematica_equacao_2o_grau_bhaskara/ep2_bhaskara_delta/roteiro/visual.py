"""Visual — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 2: a fórmula de Bhaskara e o que o Δ revela (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: chave() (a chave mestra), porta() (o porteiro Δ: aberta para 2, para 1, trancada), mini_parabola()
(miniatura ilustrativa, sem vértice nem concavidade), tabelinha() (a | b | c com sinal), m().
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
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_2grau_ep2_bhaskara_delta.mp4"
CARD_R = K.CARD_R
FORMULA = "x = -b±√{Δ}/2a"


def m(c, s, cx, cy, size, a=1.0, hl=None, align="center", col=None):
    """linha matemática (expr) de uma cor, com destaques por token: hl = {índice: cor}"""
    n = len(s.split())
    cores = {i: col or INK for i in range(n)}
    cores.update(hl or {})
    return K.expr(c, s, cx, cy, size, a, cores=cores, align=align)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def defin(c, termo, s, y, a, w=1400):
    """faixa azul de definição: TERMO + frase"""
    if a <= 0:
        return
    x = W / 2 - w / 2
    boxed(c, x, y - 50, w, 100, BLUE, a, 0.08)
    pill(c, termo, x + 24, y, BLUE, size=26, a=a)
    tw = text_w(termo, "bold", 26) + 70
    para(c, s, x + 24 + tw, y + 12, 32, "bold", INK, a, w - tw - 60)


def flash(c, x, y, w, h, t, t0, a=1.0):
    """flash âmbar em volta de um pedaço da fórmula"""
    f = ep(t, t0, 0.25) * (1 - ep(t, t0 + 1.2, 0.6)) * a
    if f > 0:
        rrect(c, x - w / 2, y - h / 2, w, h, 14, AMBER, 0.28 * f)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, y - h / 2, w, h), 14, 14), paint(AMBER, f, stroke=4))


# ======================================================================
# peças do episódio
# ======================================================================

def chave(c, x, y, s, a, col=PURPLE):
    """chave mestra: argola à esquerda, haste e dentes; (x, y) = centro da argola"""
    if a <= 0:
        return
    c.drawCircle(x, y, s * 0.42, paint(col, a, stroke=s * 0.16))
    c.drawCircle(x, y, s * 0.14, paint(col, a * 0.3))
    rrect(c, x + s * 0.40, y - s * 0.08, s * 1.5, s * 0.16, s * 0.05, col, a)
    for k, (dx, hh) in enumerate(((1.25, 0.34), (1.55, 0.24), (1.78, 0.34))):
        rrect(c, x + s * dx, y + s * 0.04, s * 0.13, s * hh, s * 0.03, col, a)


def cadeado(c, x, y, s, a, col=AMBER):
    if a <= 0:
        return
    rrect(c, x - s / 2, y - s * 0.1, s, s * 0.8, s * 0.12, col, a)
    p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(x - s * 0.32, y - s * 0.62, s * 0.64, s * 0.9), 180, 180)
    c.drawPath(p, paint(col, a, stroke=s * 0.12))
    c.drawCircle(x, y + s * 0.25, s * 0.09, paint("#FFFFFF", a))


def tabelinha(c, cx, cy, vals, a, size=46, ws=150, alfas=None):
    """a | b | c com sinal, em três fichas"""
    if a <= 0:
        return
    for k, (L, v) in enumerate(zip("abc", vals)):
        ak = a * (alfas[k] if alfas else 1.0)
        if ak <= 0:
            continue
        x = cx + (k - 1) * (ws + 24)
        rrect(c, x - ws / 2, cy - 70, ws, 140, 18, "#FFFFFF", ak, shadow=True)
        text(c, L, x, cy - 30, 30, "black", PURPLE, ak)
        m(c, v, x, cy + 26, size, ak, col=AMBER if v.startswith("-") else INK)


def mini_parabola(c, cx, cy, w, h, k, a, col=BLUE, raizes=(), selo_fq=True):
    """miniatura ilustrativa: eixo x e uma curva que corta (k > 0, raízes em ±√k), toca (k = 0) ou não toca (k < 0)"""
    if a <= 0:
        return
    line(c, cx - w / 2, cy, cx + w / 2, cy, INK2, a, 3)
    p = skia.Path()
    for i in range(41):
        u = -1 + i / 20
        x = cx + u * w * 0.38
        y = cy - h * (u * u - k) * 1.6
        (p.moveTo if i == 0 else p.lineTo)(x, y)
    c.drawPath(p, paint(col, a, stroke=5, cap_round=True))
    for u in raizes:
        c.drawCircle(cx + u * w * 0.38, cy, 9, paint(RED, a))
    if selo_fq:
        text(c, "série de Função Quadrática", cx, cy + h * 0.55 + 34, 18, "bold", GRAY, a)


def porta(c, cx, cy, titulo, n, a, aberta_u, col, eq, delta):
    """porta do porteiro Δ: n raízes passam (bolinhas saindo); n = 0 → trancada"""
    if a <= 0:
        return
    w, h = 400, 470
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 22, mix("#FFFFFF", col, 0.08), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), paint(col, a, stroke=4))
    chip(c, titulo, cx, y + 4, col, a, 34, True, 220)
    m(c, eq, cx, y + 80, 30, a)
    m(c, delta, cx, y + 130, 34, a, col=col)
    # a porta
    px, py, pw, ph = cx - 70, y + 170, 140, 170
    rrect(c, px, py, pw, ph, 10, "#F1EEE6", a)
    if n == 0:
        rrect(c, px, py, pw, ph, 10, mix("#FFFFFF", RED, 0.25), a)
        cadeado(c, cx, py + ph / 2, 56, a * aberta_u, RED)
    else:
        ang = 70 * aberta_u
        fw = pw * math.cos(math.radians(ang))
        rrect(c, px, py, max(6, fw), ph, 8, mix("#FFFFFF", col, 0.35), a)
        c.drawCircle(px + max(6, fw) - 16, py + ph / 2, 6, paint(INK, a))
        for k in range(n):
            u = clamp(aberta_u * 1.4 - 0.4 - 0.25 * k)
            bx = cx + 10 + 90 * u + 0 * k
            by = py + ph / 2 - 40 + 70 * k if n == 2 else py + ph / 2
            c.drawCircle(bx + 60 * u, by, 18, paint(GREEN, a * u))
    text(c, ("passam 2 raízes" if n == 2 else "passa 1 raiz" if n == 1 else "nenhuma raiz real"), cx, y + 385, 28,
         "black", col, a * aberta_u)
    text(c, ("raízes 1 e 4" if n == 2 else "raiz dupla: 2" if n == 1 else "√−16 não existe nos reais"), cx, y + 430, 24,
         "bold", INK2, a * aberta_u)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FÓRMULA DE BHASKARA", PURPLE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 380, 220, 1160, 170, 30, "#FFFFFF", aa, shadow=True)
        m(c, FORMULA, W / 2, 305, 76, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        chip(c, "b = −7", 480, 500, AMBER, ab, 56)
        text(c, "o sinal do b", 480, 600, 30, "black", AMBER, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 760, 450, 440, 110, 20, mix("#FFFFFF", GREEN, 0.10), acc)
        m(c, "b^2 = (-7)^2 = +49", 980, 505, 42, acc, hl={4: GREEN})
        flash(c, 980, 505, 440, 110, t, C["01.c"] + 0.6)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 1260, 450, 380, 110, 20, mix("#FFFFFF", GREEN, 0.10), ad)
        m(c, "-b = +7", 1450, 505, 46, ad, hl={2: GREEN})
        flash(c, 1450, 505, 380, 110, t, C["01.d"] + 0.4)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        rrect(c, 560, 640, 800, 150, 22, mix("#FFFFFF", RED, 0.08), ae)
        m(c, "-3 e -1/2", 760, 715, 46, ae, col=RED)
        strike(c, 650, 715, 870, 715, ae, RED, ae)
        text_mid(c, "→", 960, 715, 54, "black", INK2, ae)
        m(c, "3 e 1/2", 1150, 715, 46, ae, col=GREEN)
        selo(c, 1360, 650, ae, "RAÍZES TROCADAS", RED, 6, 26)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "aplicar Bhaskara sem errar sinal", "Δ = b^2 - 4ac   ·   " + FORMULA),
            ("02.b", "saber quantas raízes só olhando o Δ", "Δ>0 → 2   ·   Δ=0 → 1   ·   Δ<0 → 0")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 240 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        m(c, sub, 360, y + 90, 40, a, align="left", col=PURPLE)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    cols = [("03.a", "A | B | C COM SINAL", "episódio 1", 380), ("03.b", "PARÊNTESES NO NEGATIVO", "série de Operações", 960),
            ("03.c", "QUADRADO DA SOMA", "série de Expressões Algébricas", 1540)]
    for cue, tit, src, x in cols:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        rrect(c, x - 270, 250, 540, 520, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x, 310, 28, "black", BLUE, a)
        text(c, src, x, 352, 22, "bold", GRAY, a)
        if cue == "03.a":
            m(c, "2x^2 - 7x + 3 = 0", x, 440, 40, a)
            tabelinha(c, x, 610, ["2", "-7", "3"], a, 38, 130)
        elif cue == "03.b":
            m(c, "(-7)^2 = 49", x, 470, 50, a, hl={2: GREEN})
            check_icon(c, x - 210, 470, 20, a, GREEN)
            m(c, "-7^2 = -49", x, 600, 50, a, hl={2: RED})
            text(c, "sem parênteses: outra conta", x, 690, 24, "bold", INK2, a)
        else:
            m(c, "(a+b)^2", x, 470, 56, a)
            m(c, "= a^2 + 2ab + b^2", x, 580, 40, a, hl={3: PURPLE})


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA EQUAÇÃO COMPLETA", "OS TRUQUES FUNCIONAM?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["04"], 0.5)
    if a0 > 0:
        rrect(c, 510, 210, 900, 130, 24, "#F7F7F5", a0)
        m(c, "2x^2 - 7x + 3 = 0", W / 2, 275, 70, a0)
    tent = [("04.a", "x em evidência?", "o 3 não tem x", 560), ("04.b", "isolar o x²?", "o −7x atrapalha", 1360)]
    for cue, s, why, x in tent:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        rrect(c, x - 330, 390, 660, 200, 22, mix("#FFFFFF", RED, 0.06), a)
        text(c, s, x, 460, 40, "black", INK, a)
        ax = ep(t, C[cue] + 2.2, 0.4)
        check_icon(c, x - 250, 535, 22, ax, RED, "x")
        text(c, why, x + 20, 548, 32, "bold", RED, ax)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 400, acc, "TRAVOU", RED, -6, 34)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        chave(c, 700, 720, 90, ad)
        text(c, "CHAVE MESTRA", 1200, 700, 50, "black", PURPLE, ad)
        text(c, "abre qualquer equação do 2º grau", 1200, 760, 30, "bold", INK2, ad)


# ======================================================================
# bloco a — a fórmula
# ======================================================================

def b_formula(c, t, C, B):
    head_seq(c, t, C, [("05", "A FÓRMULA DE BHASKARA", "PRIMEIRA ETAPA: O Δ", PURPLE),
                       ("06", "A FÓRMULA DE BHASKARA", "SEGUNDA ETAPA: AS RAÍZES", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        defin(c, "FÓRMULA DE BHASKARA", "a receita que dá as raízes de qualquer equação do 2º grau", 240,
              ep(t, C["05.a"], 0.5))
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            defin(c, "DISCRIMINANTE (Δ)", "a primeira conta da fórmula · Δ = “delta”, letra grega", 370, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            boxed(c, 560, 450, 800, 170, PURPLE, acc, 0.10)
            m(c, "Δ = b^2 - 4ac", W / 2, 535, 84, acc, col=PURPLE)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            chave(c, 520, 730, 60, ad)
            cadeado(c, 760, 730, 60, ad)
            text(c, "só abre a equação arrumada:", 1150, 712, 34, "black", AMBER, ad)
            m(c, "ax^2 + bx + c = 0", 1150, 775, 40, ad, hl={6: AMBER})
        return
    a0 = ep(t, C["06.a"], 0.5)
    if a0 > 0:
        boxed(c, 460, 240, 1000, 240, PURPLE, a0, 0.10)
        m(c, FORMULA, W / 2, 360, 96, a0, col=PURPLE)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        text(c, "± = duas contas", W / 2, 560, 40, "black", AMBER, ab)
        m(c, "x₁ = -b+√{Δ}/2a", 640, 680, 56, ep(t, C["06.b"] + 1.4, 0.4))
        m(c, "x₂ = -b-√{Δ}/2a", 1280, 680, 56, ep(t, C["06.b"] + 2.2, 0.4))
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        pill(c, "por isso costumam sair DUAS raízes", W / 2, 800, PURPLE, size=28, a=acc, anchor="center")


# ======================================================================
# bloco b — exemplo completo (a fórmula preenchida peça por peça)
# ======================================================================

def b_exemplo(c, t, C, B):
    head_seq(c, t, C, [("07", "EXEMPLO COMPLETO", "PRIMEIRO A, B, C; DEPOIS O Δ", PURPLE),
                       ("08", "EXEMPLO COMPLETO", "AS DUAS RAÍZES", PURPLE),
                       ("09", "ATALHO", "A CONFERÊNCIA DE 10 SEGUNDOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09"])
    m(c, "2x^2 - 7x + 3 = 0", W / 2, 215, 46, ep(t, C["07"], 0.5))
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        tabelinha(c, 400, 400, ["2", "-7", "3"], aa, 48, 140,
                  alfas=[ep(t, C["07.a"] + 0.9 * k, 0.4) for k in range(3)])
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            m(c, "Δ = (-7)^2 - 4·2·3", 1240, 340, 58, ab, hl={2: AMBER})
            flash(c, 1150, 340, 210, 100, t, C["07.b"] + 0.4)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            m(c, "(-7)^2 = 49", 1000, 500, 48, acc, hl={2: GREEN})
            m(c, "4·2·3 = 24", 1480, 500, 48, ep(t, C["07.c"] + 1.6, 0.4))
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            rrect(c, 900, 600, 680, 140, 24, mix("#FFFFFF", PURPLE, 0.10), ad)
            m(c, "Δ = 49 - 24 = 25", 1240, 670, 62, ad, hl={6: PURPLE})
        return
    if sid == "08":
        pill(c, "Δ = 25", 260, 300, PURPLE, size=30, a=1)
        pill(c, "b = −7", 260, 370, AMBER, size=30, a=1)
        pill(c, "a = 2", 260, 440, BLUE, size=30, a=1)
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            m(c, "-b = -(-7) = +7", 1060, 300, 50, aa, hl={4: GREEN})
            flash(c, 1250, 300, 140, 90, t, C["08.a"] + 0.8)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            m(c, "√{25} = 5", 820, 410, 46, ab)
            m(c, "2a = 4", 1300, 410, 46, ep(t, C["08.b"] + 1.2, 0.4))
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            rrect(c, 760, 470, 600, 170, 24, "#FFFFFF", acc, shadow=True)
            # o traço se estica para cobrir o numerador inteiro
            m(c, "x =", 900, 555, 64, acc)
            u = ep(t, C["08.c"] + 0.4, 0.9)
            ftext(c, "7 ± 5", 1110, 528, 60, "black", INK, acc)
            line(c, 1110 - 90 * u, 553, 1110 + 90 * u, 553, INK, acc, 6)
            text(c, "4", 1110, 625, 60, "black", INK, acc * u)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            m(c, "x₁ = 7+5/4 = 12/4 = 3", 700, 740, 46, ad, hl={4: GREEN})
        ae = ep(t, C["08.e"], 0.5)
        if ae > 0:
            m(c, "x₂ = 7-5/4 = 2/4 = 1/2", 1340, 740, 46, ae, hl={4: GREEN})
        return
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 260, 250, 1400, 170, "ATALHO · CONFERÊNCIA DE 10 SEGUNDOS", ["coloque uma raiz de volta na equação"], aa, 40)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        m(c, "x = 3:", 420, 540, 50, ab, col=PURPLE)
        m(c, "2·9 - 21 + 3 = 0", 1000, 540, 60, ab, hl={4: GREEN})
        conferido(c, "bateu", 1420, 560, ep(t, C["09.ok"], 0.4), True, 40)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        pill(c, "não deu zero? o erro quase sempre está num SINAL", W / 2, 720, AMBER, size=30, a=acc, anchor="center")


# ======================================================================
# bloco c — os três tropeços
# ======================================================================

def b_tropecos(c, t, C, B):
    head(c, t, B["start"], "OS TRÊS TROPEÇOS", "ONDE A MAIORIA ERRA", AMBER)
    card(c, *CARD_R)
    cards = [("10.a", "1 · o b²", "(-7)^2 = +49", "ao quadrado nunca fica negativo"),
             ("10.b", "2 · o −b", "-(-7) = +7", "o oposto de −7"),
             ("10.c", "3 · o 2a", "7+5/4", "divide o numerador INTEIRO")]
    for k, (cue, tit, s, nota) in enumerate(cards):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 230 + k * 500
        rrect(c, x, 250, 460, 470, 24, mix("#FFFFFF", AMBER, 0.08), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 250, 460, 470), 24, 24), paint(AMBER, a, stroke=3))
        badge_num(c, k + 1, x + 230, 250, a, 26, bg=AMBER)
        text(c, tit, x + 230, 330, 38, "black", AMBER, a)
        m(c, s, x + 230, 460, 60, a)
        para(c, nota, x + 40, 600, 30, "bold", INK2, a, 380, align="left")
    ac = ep(t, C["10.c"] + 2.5, 0.5)
    if ac > 0:
        m(c, "≠  7 + 5/4", 1460, 785, 34, ac, col=RED)


# ======================================================================
# bloco d — de onde vem a fórmula
# ======================================================================

def b_origem(c, t, C, B):
    head_seq(c, t, C, [("11", "DE ONDE VEM A FÓRMULA", "O QUADRADO DA SOMA AO CONTRÁRIO", PURPLE),
                       ("12", "DE ONDE VEM O ±", "DOIS NÚMEROS, O MESMO QUADRADO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        pill(c, "quadrado da soma ao contrário", W / 2, 220, PURPLE, size=28, a=ep(t, C["11.a"], 0.5), anchor="center")
        rows = [("11.b", "ax^2 + bx + c = 0", "× 4a", None),
                ("11.b", "4a^2x^2 + 4abx + 4ac = 0", "", None),
                ("11.c", "4a^2x^2 + 4abx + b^2 = b^2 - 4ac", "+ b² − 4ac", None),
                ("11.d", "(2ax+b)^2 = b^2 - 4ac", "quadrado perfeito", {0: PURPLE}),
                ("11.e", "(2ax+b)^2 = Δ", "o próprio Δ", {2: PURPLE})]
        for k, (cue, s, nota, hl) in enumerate(rows):
            a = ep(t, C[cue] + (1.2 if k == 1 else 0), 0.5)
            if a <= 0:
                continue
            y = 310 + k * 100
            m(c, s, 900, y, 48, a, hl=hl)
            if nota:
                text(c, nota, 1420, y + 12, 30, "black", AMBER if k < 3 else PURPLE, a, align="left")
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        m(c, "(2ax+b)^2 = Δ", W / 2, 260, 60, aa)
        arrow(c, 760, 320, 600, 410, PURPLE, aa, 5, 18)
        arrow(c, 1160, 320, 1320, 410, PURPLE, aa, 5, 18)
        m(c, "2ax+b = +√{Δ}", 560, 470, 50, aa, col=GREEN)
        m(c, "2ax+b = -√{Δ}", 1360, 470, 50, aa, col=BLUE)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        m(c, "5^2 = 25", 700, 610, 54, ab)
        m(c, "(-5)^2 = 25", 1220, 610, 54, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 560, 690, 800, 120, 24, mix("#FFFFFF", PURPLE, 0.10), acc)
        m(c, FORMULA, W / 2, 750, 56, acc, col=PURPLE)


# ======================================================================
# bloco e — o porteiro Δ
# ======================================================================

def b_porteiro(c, t, C, B):
    head_seq(c, t, C, [("13", "O Δ É O PORTEIRO", "QUANTAS RAÍZES PASSAM?", BLUE), ("14", "O Δ É O PORTEIRO", "Δ = 0", BLUE),
                       ("15", "O Δ É O PORTEIRO", "Δ NEGATIVO", BLUE), ("16", "ATALHO", "O SINAL DE a E c", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14", "15", "16"])
    if sid == "16":
        aa = ep(t, C["16.a"], 0.5)
        K.atalho(c, 260, 220, 1400, 160, "ATALHO · SINAIS OPOSTOS EM a E c", ["−4ac vira SOMA"], aa, 40)
        ab = ep(t, C["16.b"], 0.5)
        if ab > 0:
            m(c, "3x^2 - 5x - 2 = 0", 600, 480, 52, ab, hl={0: BLUE, 4: BLUE})
            text(c, "a = 3 (+)   c = −2 (−)", 600, 560, 30, "black", INK2, ab)
            m(c, "Δ = 25 + 24", 1300, 480, 56, ab, hl={3: GREEN, 4: GREEN})
            text(c, "b² + positivo = positivo", 1300, 560, 30, "black", GREEN, ab)
        acc = ep(t, C["16.c"], 0.5)
        if acc > 0:
            pill(c, "duas raízes garantidas, sem fazer conta", W / 2, 700, GREEN, size=32, a=acc, anchor="center")
        return
    if sid == "13":
        defin(c, "RAIZ REAL", "solução que existe entre os números do dia a dia", 790,
              ep(t, C["13.b"], 0.5) * (1 - ep(t, C["13.c"], 0.4)), 1300)
    portas = [("13.c", "Δ > 0", 2, GREEN, "x^2 - 5x + 4", "Δ = 9", 0.49, (-0.7, 0.7), 420),
              ("14", "Δ = 0", 1, BLUE, "x^2 - 4x + 4", "Δ = 0", 0.0, (0.0,), 960),
              ("15", "Δ < 0", 0, RED, "x^2 + 2x + 5", "Δ = -16", -0.35, (), 1500)]
    for cue, tit, n, col, eq, dl, k, rz, x in portas:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        u = ep(t, C[cue] + 1.5, 1.0)
        porta(c, x, 470, tit, n, a, u, col, eq, dl)
        mini_parabola(c, x, 790, 260, 30, k, a * u, col, rz, selo_fq=False)
    if sid == "14":
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            pill(c, "RAIZ DUPLA: as duas contas caem no mesmo número", W / 2, 840, BLUE, size=24, a=acc, anchor="center")
    if sid == "15":
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            pill(c, "Δ negativo: pode parar a conta aqui", W / 2, 840, RED, size=24, a=acc, anchor="center")


# ======================================================================
# bloco f — a parábola (só ilustração)
# ======================================================================

def b_parabola(c, t, C, B):
    head(c, t, B["start"], "O MESMO PORTEIRO, DESENHADO", "A PARÁBOLA (SÓ ILUSTRAÇÃO)", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        m(c, "y = ax^2 + bx + c", 520, 260, 50, aa)
        defin(c, "PARÁBOLA", "a curva que esse desenho forma", 370, aa, 1100)
    ab = ep(t, C["17.b"], 0.5)
    casos = [(0.49, (-0.7, 0.7), GREEN, "corta 2 vezes"), (0.0, (0.0,), BLUE, "toca 1 vez"),
             (-0.35, (), RED, "não toca")]
    for k, (kk, rz, col, s) in enumerate(casos):
        ak = ep(t, C["17.b"] + 0.9 * k, 0.5)
        if ak <= 0:
            continue
        x = 400 + k * 560
        mini_parabola(c, x, 640, 420, 80, kk, ak, col, rz, selo_fq=False)
        text(c, s, x, 790, 30, "black", col, ak)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        selo(c, 1380, 250, acc, "SÉRIE DE FUNÇÃO QUADRÁTICA", PURPLE, -4, 28)


# ======================================================================
# bloco g — parâmetro
# ======================================================================

def b_parametro(c, t, C, B):
    head(c, t, B["start"], "QUESTÕES DE PARÂMETRO", "UMA LETRA NO LUGAR DO NÚMERO", PURPLE)
    card(c, *CARD_R)
    defin(c, "PARÂMETRO", "um valor que você escolhe e que muda a equação", 240, ep(t, C["18.a"], 0.5))
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        m(c, "x^2 - 8x + k = 0", 560, 380, 56, ab, hl={4: AMBER})
        text(c, "uma única raiz?", 560, 460, 34, "black", INK2, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        arrow(c, 860, 400, 1040, 400, BLUE, acc, 5, 18)
        chip(c, "Δ = 0", 1220, 400, BLUE, acc, 52)
        text(c, "segunda porta", 1220, 480, 26, "bold", BLUE, acc)
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        rrect(c, 400, 560, 1120, 110, 22, mix("#FFFFFF", PURPLE, 0.10), ad)
        m(c, "64 - 4k = 0   →   k = 16", W / 2, 615, 54, ad, hl={6: PURPLE, 7: PURPLE, 8: PURPLE})
    ae = ep(t, C["18.e"], 0.5)
    if ae > 0:
        m(c, "x^2 - 8x + 16 = (x-4)^2", W / 2, 750, 46, ae, hl={6: GREEN})
        conferido(c, "confere", 1480, 770, ae, True, 30)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E TENTE", GREEN), ("20", "VAMOS JUNTOS", "A, B, C · Δ · RAÍZES", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["19.a"], 0.5)
    if aa > 0:
        rrect(c, 480, 210, 960, 130, 24, "#F7F7F5", aa)
        m(c, "3x^2 - 5x - 2 = 0", W / 2, 275, 66, aa)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 560)
    if t < C["20"]:
        return
    tabelinha(c, 420, 470, ["3", "-5", "-2"], ep(t, C["20.a"], 0.5), 44, 130)
    ab = ep(t, C["20.b"], 0.5)
    if ab > 0:
        m(c, "Δ = (-5)^2 - 4·3·(-2)", 1230, 420, 44, ab)
        m(c, "= 25 + 24 = 49", 1230, 500, 48, ep(t, C["20.b"] + 2.5, 0.4), hl={5: PURPLE})
    acc = ep(t, C["20.c"], 0.5)
    if acc > 0:
        m(c, "x = 5±7/6", 560, 680, 56, acc)
        m(c, "→   2   ou   -1/3", 1000, 680, 52, ep(t, C["20.c"] + 1.6, 0.4), hl={1: GREEN, 3: GREEN})
    ad = ep(t, C["20.d"], 0.5)
    if ad > 0:
        m(c, "x = 2:  12 - 10 - 2 = 0", 1480, 640, 32, ad)
        conferido(c, "bateu", 1380, 720, ep(t, C["20.ok"], 0.4), True, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Primeiro a, b e c com sinal; depois o Δ.",
          "Δ positivo, duas raízes; zero, uma; negativo, nenhuma real.",
          "O 2a divide o numerador inteiro."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Δ com −7² = −49", "na calculadora, −7² sem parênteses dá mesmo −49",
          "b SEMPRE entre parênteses: (−7)² = 49 · senão Δ = −73 e você jura que não há raiz"),
         ("dividir só a raiz por 2a: 7 + 5 ÷ 4 = 8,25", "a raiz de Δ fica bem em cima do 2a",
          "o traço cobre o numerador inteiro: (7 + 5) ÷ 4 = 3"),
         ("x² − 5x = −6 com c = −6 → 6 e −1", "os três números estão ali, prontos",
          "arrume primeiro: x² − 5x + 6 = 0 → raízes 2 e 3")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24"], ERROS)


# ======================================================================
# questão 2 do material (eu começo, você termina)
# ======================================================================

ALTS2 = [("A", "3", "a própria raiz dupla", RED), ("B", "6", "copiou o b sem sinal", RED), ("C", "9", "", GREEN),
         ("D", "36", "esqueceu o 4 de 4ac", RED), ("E", "−9", "Δ = 72: dois pontos", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU COMEÇO, VOCÊ TERMINA", "UM ÚNICO PONTO DE CONTATO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    y = 230
    for ln in K.wrap("Um programa de desenho traça a curva y = x² − 6x + k, em que k é escolhido pelo usuário. Para uma "
                     "vinheta, o designer quer que a curva toque o eixo horizontal em exatamente um ponto. O valor de k "
                     "deve ser", "black", 26, 700):
        ftext(c, ln, 190, y, 26, "black", INK, a0, align="left")
        y += 38
    yend = y
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["26"], 0.3)),
         align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 40, C["26.ok"], "C", cues_in, cues_x, gap=34)
    if t >= C["26"]:
        y0 = yend + 10
        rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["26"], 0.4), shadow=True)
        aa = ep(t, C["26.a"], 0.4)
        if aa > 0:
            text(c, "1 ponto  =  1 raiz", 540, y0 + 50, 30, "black", BLUE, aa)
            m(c, "Δ = 0", 540, y0 + 100, 40, aa, col=BLUE)
        ab = ep(t, C["26.b"], 0.4)
        if ab > 0:
            m(c, "a = 1   b = -6   c = k", 540, y0 + 160, 34, ab, hl={3: AMBER, 5: AMBER})
        pause_timer(c, t, C["26.p"] + 0.1, 540, y0 + 250)
        ad = ep(t, C["26.d"], 0.4)
        if ad > 0:
            m(c, "36 - 4k = 0  →  k = 9", 540, y0 + 230, 36, ad, hl={6: GREEN, 7: GREEN, 8: GREEN})
        ae = ep(t, C["26.e"], 0.4)
        if ae > 0:
            m(c, "x^2 - 6x + 9 = (x-3)^2", 540, y0 + 300, 30, ae)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "RAÍZES EM 3 SEGUNDOS", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    if aa > 0:
        m(c, "x^2 - 7x + 10 = 0", W / 2, 330, 80, aa)
        text(c, "sem fórmula nenhuma", W / 2, 440, 34, "black", GREEN, aa)
    ab = ep(t, C["29.b"], 0.5)
    if ab > 0:
        chip(c, "? + ? = 7", 700, 570, PURPLE, ab, 50)
        chip(c, "? · ? = 10", 1220, 570, PURPLE, ab, 50)
    pill(c, "ep. 3 · soma e produto", W / 2, 720, PURPLE, size=32, a=ep(t, C["29.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"],
        "Qual dos três tropeços já te pegou?", canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, formula=b_formula, exemplo=b_exemplo,
              tropecos=b_tropecos, origem=b_origem, porteiro=b_porteiro, parabola=b_parabola, parametro=b_parametro,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, ponte=b_ponte, cta=b_cta)
