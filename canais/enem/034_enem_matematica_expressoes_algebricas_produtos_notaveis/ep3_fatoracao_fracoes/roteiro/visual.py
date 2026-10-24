"""Visual — Expressões Algébricas e Produtos Notáveis, Episódio 3: fatoração, frações algébricas e o produto notável ao
contrário (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações empilhadas e potências, alternativas,
erro_cards, atalho...).
Peças deste episódio: tesoura() (a tesoura que só corta fator), lpeca() (o L que vira retângulo), passo() (linha de conta
com rótulo à esquerda).
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
_s = importlib.util.spec_from_file_location("comum034", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w
expr, mdraw, math_w = K.expr, K.mdraw, K.math_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_algebra_ep3_fatoracao_fracoes.mp4"
CARD_R = K.CARD_R


# ======================================================================
# peças do episódio
# ======================================================================

def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def tesoura(c, cx, cy, s, a, abre=0.5, col=None):
    """tesoura com a ponta para a ESQUERDA; abre = 0 (fechada) a 1 (aberta)"""
    if a <= 0:
        return
    col = col or GREEN
    ang = 6 + 16 * clamp(abre)
    for sg in (-1, 1):
        c.save(); c.translate(cx, cy); c.rotate(sg * ang)
        p = skia.Path()
        p.moveTo(0, -s * 0.07); p.quadTo(-s * 0.55, -s * 0.09, -s * 0.95, 0); p.quadTo(-s * 0.55, s * 0.03, 0, s * 0.05)
        p.close()
        c.drawPath(p, paint("#C9CED6", a))
        c.drawPath(p, paint("#7D8590", a, stroke=2))
        c.drawCircle(s * 0.42, sg * s * 0.10, s * 0.17, paint(col, a, stroke=s * 0.07))
        line(c, 0, 0, s * 0.27, sg * s * 0.07, col, a, s * 0.07)
        c.restore()
    c.drawCircle(cx, cy, s * 0.05, paint(INK, a))


def passo(c, rot, s, x, y, a, size=46, col=None, rcol=GRAY):
    """linha de conta: rótulo curto à esquerda (cinza) e a expressão alinhada à esquerda"""
    if a <= 0:
        return
    if rot:
        text(c, rot, x - 30, y + 10, 26, "black", rcol, a, align="right")
    n = len(s.split())
    expr(c, s, x, y, size, a, cores={i: col or INK for i in range(n)}, align="left")


def fcorta(c, num, den, cx, cy, size, a, cortes=(), u=0.0, col=None, cores=None):
    """fração montada por peças (listas de tokens do expr, desenhados colados) com corte preciso das peças em `cortes`
    = {("n", i), ("d", j)}; u = progresso do risco (0 → 1). Devolve a largura."""
    if a <= 0:
        return 0
    col = col or GREEN
    wn = [math_w(p_, size) for p_ in num]
    wd = [math_w(p_, size) for p_ in den]
    w = max(sum(wn), sum(wd)) + size * 0.4
    line(c, cx - w / 2, cy, cx + w / 2, cy, INK, a, size * 0.07)
    for lado, parts, ws, yy in (("n", num, wn, cy - size * 0.62), ("d", den, wd, cy + size * 0.62)):
        x = cx - sum(ws) / 2
        for i, (p_, w_) in enumerate(zip(parts, ws)):
            k = (cores or {}).get((lado, i), INK)
            expr(c, p_, x, yy, size, a, cores={j: k for j in range(9)}, align="left")
            if (lado, i) in cortes and u > 0:
                strike(c, x - 4, yy + size * 0.30, x + w_ + 4, yy - size * 0.30, u, col, a * u)
            x += w_
    return w


def pergunta(c, s, cx, cy, a, col=PURPLE, size=38):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 38, w, 76, 38, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


def defin(c, termo, s, x, y, w, a, col=BLUE, size=30):
    """caixa de definição: TERMO em negrito colorido + explicação"""
    if a <= 0:
        return
    boxed(c, x, y, w, 110, col, a, 0.08)
    text(c, termo, x + 30, y + 46, 26, "black", col, a, align="left", tracking=1)
    text(c, s, x + 30, y + 88, size, "bold", INK, a, align="left")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FATORAÇÃO E FRAÇÕES ALGÉBRICAS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 230, 680, 420, 26, "#FFFFFF", aa, shadow=True)
        expr(c, "{x+3}/3", 570, 400, 110, aa)
        u = ep(t, C["01.a"] + 2.2, 1.2)
        if u > 0:
            # a tesoura passa pelos dois 3
            tesoura(c, lerp(760, 620, u), lerp(360, 470, u), 120, aa * (1 - ep(t, C["01.a"] + 3.6, 0.3)),
                    abs(math.sin(u * 6)), RED)
            strike(c, 600, 380, 680, 340, u, RED, aa * u)
            strike(c, 535, 495, 600, 455, u, RED, aa * u)
        expr(c, "= x ?", 820, 400, 80, ep(t, C["01.a"] + 3.4, 0.4), cores={0: RED, 1: RED, 2: RED})
        text(c, "o corte \"óbvio\"", 570, 610, 30, "black", RED, ep(t, C["01.a"] + 3.4, 0.4))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 230, 700, 420, 26, "#FFFFFF", ab, shadow=True)
        pill(c, "teste: x = 6", 1350, 290, BLUE, size=30, a=ab, anchor="center")
        expr(c, "{6+3}/3 = 9/3 = 3", 1350, 430, 70, ab, cores={6: GREEN})
        aw = ep(t, C["01.b"] + 3.5, 0.4)
        if aw > 0:
            linha = "x = 6"
            expr(c, linha, 1350, 580, 60, aw, cores={0: RED, 1: RED, 2: RED})
            check_icon(c, 1500, 572, 24, aw, RED, "x")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 760, acc, "ERROU O DOBRO", RED, -3, 50)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "fatorar pelos 5 casos", "fator comum · agrupamento · diferença de quadrados · 2 trinômios"),
            ("02.b", "simplificar frações algébricas", "sem cortar o que não pode"),
            ("02.c", None, "sem descobrir a e b")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        if s:
            text(c, s, 360, y, 48, "black", INK, a, align="left")
        else:
            text(c, "tirar", 360, y, 48, "black", INK, a, align="left")
            expr(c, "a^2+b^2", 360 + text_w("tirar ", "black", 48), y - 14, 54, a, align="left")
            xw = 360 + text_w("tirar ", "black", 48) + math_w("a^2+b^2", 54) + 16
            text(c, "de  a + b  e  ab", xw, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "OS 3 PRODUTOS NOTÁVEIS (ep. 2)", 540, 290, 30, "black", PURPLE, aa)
        for k, s in enumerate(["(a+b)^2 = a^2+2ab+b^2", "(a-b)^2 = a^2-2ab+b^2", "(a+b)(a-b) = a^2-b^2"]):
            expr(c, s, 540, 400 + k * 120, 48, ep(t, C["03.a"] + 0.8 + 1.2 * k, 0.4))
    line(c, 960, 240, 960, 760, "#E6E6E2", ep(t, C["03.b"], 0.4), 3)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "SÓ SE CORTA O QUE MULTIPLICA", 1400, 290, 30, "black", GREEN, ab)
        text(c, "série de Frações", 1400, 336, 24, "bold", GRAY, ab)
        expr(c, "12/18 = {6·2}/{6·3} = 2/3", 1400, 500, 64, ab, cores={4: GREEN})
        pill(c, "o 6 multiplica em cima E embaixo", 1400, 650, GREEN, size=28, a=ep(t, C["03.b"] + 3.0, 0.4),
             anchor="center")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "COMECE COM UM NÚMERO", "O QUE É FATORAR?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        expr(c, "12 = 3 · 4", 560, 330, 100, aa, cores={2: BLUE, 4: BLUE})
        al = ep(t, C["04.a"] + 1.4, 0.4)
        pill(c, "fator", 610, 430, BLUE, size=26, a=al, anchor="center")
        pill(c, "fator", 780, 430, BLUE, size=26, a=al, anchor="center")
        text(c, "o 12 FATORADO", 560, 520, 34, "black", INK2, al)
    ab = ep(t, C["04.b"], 0.5)
    defin(c, "FATORAR", "escrever como MULTIPLICAÇÃO", 1040, 250, 640, ab)
    defin(c, "FATOR", "cada pedaço que multiplica", 1040, 390, 640, ep(t, C["04.b"] + 2.5, 0.4))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        expr(c, "(x+5)(x-5)", 520, 680, 52, acc)
        arrow(c, 700, 680, 1180, 680, PURPLE, acc, 6, 20)
        text(c, "produto notável MONTA", 940, 650, 28, "black", PURPLE, acc)
        expr(c, "x^2-25", 1320, 680, 52, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        arrow(c, 1180, 760, 700, 760, GREEN, ad, 6, 20)
        text(c, "fatoração DESMONTA", 940, 806, 28, "black", GREEN, ad)


# ======================================================================
# bloco a — fator comum
# ======================================================================

def b_comum(c, t, C, B):
    head_seq(c, t, C, [("05", "CASO 1", "FATOR COMUM", PURPLE), ("06", "ATALHO", "CONFIRA DESENVOLVENDO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    a0 = ep(t, C["05.a"], 0.5)
    defin(c, "FATOR COMUM", "o que se repete em TODOS os termos", 260, 210, 1400, a0 if sid == "05" else 0)
    ab = ep(t, C["05.b"], 0.5)
    yb = 440
    if ab > 0 and sid == "05":
        hl = ep(t, C["05.b"] + 1.0, 0.4)
        x0 = W / 2 - math_w("6x^2 + 9x", 90) / 2
        expr(c, "6x^2 + 9x", W / 2, yb, 90, ab)
        if sid == "05" and hl > 0:
            pill(c, "6 = 3·2", x0 + 60, yb + 100, AMBER, size=26, a=hl, anchor="center")
            pill(c, "9 = 3·3", x0 + math_w("6x^2 + 9x", 90) - 60, yb + 100, AMBER, size=26, a=hl, anchor="center")
            text(c, "os dois têm o 3 e um x", W / 2, yb + 180, 30, "black", AMBER, ep(t, C["05.b"] + 2.5, 0.4))
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0 and sid == "05":
        text(c, "3x sai para fora; dentro, o que sobrou", W / 2, 690, 30, "bold", GRAY, acc)
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0 and sid == "05":
        expr(c, "6x^2 + 9x = 3x(2x+3)", W / 2, 780, 70, ad, cores={4: GREEN})
    if sid == "06":
        expr(c, "6x^2 + 9x = 3x(2x+3)", W / 2, 300, 80, 1.0, cores={4: GREEN})
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            passo(c, "ida:", "3x · 2x = 6x^2", 760, 440, ep(t, C["06.a"] + 0.3, 0.4), 52)
            passo(c, "", "3x · 3 = 9x", 760, 530, ep(t, C["06.a"] + 2.4, 0.4), 52)
            conferido(c, "voltou ao começo", 760, 620, ep(t, C["06.a"] + 4.0, 0.4), True, 34)
        abb = ep(t, C["06.b"], 0.5)
        K.atalho(c, 300, 660, 1320, 150, "ATALHO DE CONFERÊNCIA", ["fatorou? DESENVOLVA DE VOLTA: tem que voltar ao começo"],
                 abb, 34)


# ======================================================================
# bloco b — agrupamento
# ======================================================================

def b_agrupa(c, t, C, B):
    head(c, t, B["start"], "CASO 2", "AGRUPAMENTO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        g = ep(t, C["07.a"] + 2.0, 0.4)
        if g > 0:
            w = math_w("ax + 3a + 2x + 6", 80)
            x0 = W / 2 - w / 2
            wa = math_w("ax + 3a", 80)
            rrect(c, x0 - 14, 230, wa + 28, 120, 20, None, g, stroke=4, stroke_color=BLUE)
            rrect(c, x0 + w - math_w("2x + 6", 80) - 14, 230, math_w("2x + 6", 80) + 28, 120, 20, None, g, stroke=4,
                  stroke_color=AMBER)
        expr(c, "ax + 3a + 2x + 6", W / 2, 290, 80, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        expr(c, "a(x+3)", 700, 470, 70, ab, cores={0: BLUE})
        expr(c, "+", W / 2, 470, 70, ep(t, C["07.b"] + 2.5, 0.4))
        expr(c, "2(x+3)", 1220, 470, 70, ep(t, C["07.b"] + 2.5, 0.4), cores={0: AMBER})
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        for cx in (700, 1220):
            rrect(c, cx - 30, 420, 180, 100, 18, GREEN, 0.14 * acc)
        pill(c, "o MESMO parêntese: ele vira o fator comum", W / 2, 580, GREEN, size=28, a=acc, anchor="center")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 520, 650, 880, 140, 24, mix("#FFFFFF", PURPLE, 0.08), ad)
        expr(c, "= (a+2)(x+3)", W / 2, 720, 80, ad, cores={1: GREEN})


# ======================================================================
# bloco c — diferença de quadrados e o L
# ======================================================================

def b_difquad(c, t, C, B):
    head(c, t, B["start"], "CASO 3", "DIFERENÇA DE QUADRADOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        expr(c, "x^2 - 25", 560, 320, 96, aa)
        a2 = ep(t, C["08.a"] + 1.8, 0.4)
        expr(c, "x^2 - 5^2", 560, 460, 70, a2, cores={0: BLUE, 2: BLUE})
        text(c, "dois quadrados", 560, 560, 28, "black", BLUE, a2)
    defin(c, "DIFERENÇA DE QUADRADOS", "um quadrado MENOS outro quadrado", 960, 250, 720, ep(t, C["08.b"], 0.5))
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 960, 420, 720, 140, 24, mix("#FFFFFF", PURPLE, 0.08), acc)
        expr(c, "= (x+5)(x-5)", 1320, 490, 72, acc, cores={1: GREEN})
        text(c, "soma × diferença", 1320, 590, 28, "black", PURPLE, acc)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        expr(c, "x^2 - 5x + 5x - 25", W / 2, 720, 56, ad, cores={2: GRAY, 3: GRAY, 4: GRAY, 5: GRAY})
        strike(c, W / 2 - 150, 720, W / 2 + 120, 720, ep(t, C["08.d"] + 1.2, 0.4), RED, ad)
        conferido(c, "voltou", 1460, 740, ep(t, C["08.d"] + 2.4, 0.4), True, 32)


def _ret(c, x, y, w, h, col, a, rot=0.0, cx=None, cy=None):
    if a <= 0:
        return
    c.save()
    if rot:
        c.translate(cx, cy); c.rotate(rot); c.translate(-cx, -cy)
    rrect(c, x, y, w, h, 4, mix("#FFFFFF", col, 0.30), a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), paint(col, a, stroke=4))
    c.restore()


def b_lshape(c, t, C, B):
    head(c, t, B["start"], "POR QUE VALE?", "O L QUE VIRA RETÂNGULO", PURPLE)
    card(c, *CARD_R)
    A, Bq = 400.0, 160.0
    x0, y0 = 300.0, 290.0
    aa = ep(t, C["09.a"], 0.5)
    if aa <= 0:
        return
    tira = ep(t, C["09.a"] + 2.2, 0.8)          # o quadrado b × b sai do canto
    corta = ep(t, C["09.c"], 0.6)               # o L se divide em dois retângulos
    move = ep(t, C["09.c"] + 1.6, 1.4)          # a peça de baixo gira e sobe
    if tira < 1:
        _ret(c, x0, y0, A, A, BLUE, aa)
    else:
        # o L: retângulo esquerdo (A − B) × A e peça de baixo à direita B × (A − B)
        _ret(c, x0, y0, A - Bq, A, BLUE, aa)
        # peça direita: começa em (x0 + A − B, y0 + B), B × (A − B); vai para cima do retângulo esquerdo, girada:
        # (A − B) de largura × B de altura, em (x0, y0 − B)
        px = lerp(x0 + A - Bq, x0, move)
        py = lerp(y0 + Bq, y0 - Bq, move)
        pw = lerp(Bq, A - Bq, move)
        ph = lerp(A - Bq, Bq, move)
        _ret(c, px + (corta * 8 if move == 0 else 0), py, pw, ph, AMBER if corta > 0 else BLUE, aa)
    if tira > 0:
        bx = lerp(x0 + A - Bq, x0 + A + 120, tira)
        by = lerp(y0, y0 - 40, tira)
        _ret(c, bx, by, Bq, Bq, RED, aa * (1 - 0.6 * tira))
        text(c, "b × b", bx + Bq / 2, by + Bq / 2 + 10, 30, "black", RED, aa * tira)
    # cotas
    al = aa * (1 - move)
    text(c, "a", x0 - 30, y0 + A / 2 + 10, 36, "black", BLUE, al)
    text(c, "a", x0 + A / 2, y0 + A + 46, 36, "black", BLUE, al)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        expr(c, "área do L = a^2 - b^2", 1300, 300, 54, ab)
    if corta > 0:
        text(c, "recorte e remonte", 1300, 420, 32, "black", AMBER, corta)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        text(c, "a + b", x0 - 70, y0 + (A - 2 * Bq) / 2 + 10 + Bq / 2, 34, "black", GREEN, ad)
        text(c, "a − b", x0 + (A - Bq) / 2, y0 + A + 46, 34, "black", GREEN, ad)
        expr(c, "= (a+b)(a-b)", 1300, 520, 60, ad, cores={1: GREEN})
    ae = ep(t, C["09.e"], 0.5)
    if ae > 0:
        regra(c, "mesma área, agora como MULTIPLICAÇÃO", 1300, 700, ae, 34)


# ======================================================================
# bloco d — trinômio quadrado perfeito
# ======================================================================

def b_tqp(c, t, C, B):
    head_seq(c, t, C, [("10", "CASO 4", "TRINÔMIO QUADRADO PERFEITO", PURPLE), ("11", "ATALHO", "RAIZ DAS PONTAS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        defin(c, "TRINÔMIO QUADRADO PERFEITO", "3 termos que nasceram de um quadrado", 260, 210, 1400, ep(t, C["10.a"], 0.5))
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            s = "x^2 - 6x + 9"
            expr(c, s, W / 2, 440, 90, ab, cores={0: BLUE, 4: BLUE})
            w = math_w(s, 90); x0 = W / 2 - w / 2
            ar = ep(t, C["10.b"] + 2.0, 0.4)
            pill(c, "√ → x", x0 + 40, 545, BLUE, size=30, a=ar, anchor="center")
            pill(c, "√ → 3", x0 + w - 30, 545, BLUE, size=30, a=ar, anchor="center")
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            expr(c, "2 · x · 3 = 6x", W / 2, 650, 56, acc, cores={6: GREEN})
            conferido(c, "confere", 1300, 668, ep(t, C["10.c"] + 2.5, 0.4), True, 32)
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            rrect(c, 620, 720, 680, 110, 22, mix("#FFFFFF", PURPLE, 0.08), ad)
            expr(c, "= (x-3)^2", W / 2, 775, 70, ad, cores={1: GREEN})
        return
    aa = ep(t, C["11.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 150, "ATALHO DE RECONHECIMENTO", ["raiz das PONTAS  ·  2 × produto delas = termo do MEIO?"],
             aa, 36)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        s = "4x^2 + 12x + 9"
        expr(c, s, W / 2, 450, 84, ab, cores={0: BLUE, 4: BLUE})
        w = math_w(s, 84); x0 = W / 2 - w / 2
        ar = ep(t, C["11.b"] + 2.0, 0.4)
        pill(c, "√ → 2x", x0 + 60, 555, BLUE, size=30, a=ar, anchor="center")
        pill(c, "√ → 3", x0 + w - 30, 555, BLUE, size=30, a=ar, anchor="center")
        am = ep(t, C["11.b"] + 4.0, 0.4)
        expr(c, "2 · 2x · 3 = 12x", W / 2, 650, 56, am, cores={6: GREEN})
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 620, 715, 680, 110, 22, mix("#FFFFFF", PURPLE, 0.08), acc)
        expr(c, "= (2x+3)^2", W / 2, 770, 70, acc, cores={1: GREEN})


# ======================================================================
# bloco e — soma e produto · bloco f — combinado
# ======================================================================

def b_somaprod(c, t, C, B):
    head(c, t, B["start"], "CASO 5", "TRINÔMIO SOMA E PRODUTO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        expr(c, "x^2 + 5x + 6", W / 2, 290, 86, aa, cores={2: BLUE, 4: AMBER})
        fill = ep(t, C["12.b"], 0.5)
        for k, (op, res, col) in enumerate((("+", "5", BLUE), ("·", "6", AMBER))):
            y = 440 + k * 110
            a2 = ep(t, C["12.a"] + 2.0 + k * 1.0, 0.4)
            if a2 <= 0:
                continue
            text(c, "SOMA" if k == 0 else "PRODUTO", 520, y + 12, 28, "black", col, a2, align="right")
            for j, xx in enumerate((640, 860)):
                rrect(c, xx - 55, y - 50, 110, 100, 16, "#FFFFFF", a2, stroke=4, stroke_color=col)
                text_mid(c, "23"[j], xx, y, 60, "black", INK, a2 * fill)
            text_mid(c, op, 750, y, 56, "black", INK, a2)
            text_mid(c, "= " + res, 1040, y, 56, "black", col, a2)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 1180, 430, 500, 220, 24, mix("#FFFFFF", PURPLE, 0.08), acc)
        expr(c, "(x+2)(x+3)", 1430, 540, 64, acc, cores={0: GREEN, 1: GREEN})
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "aqui é só FATORAÇÃO  ·  resolver equação: série do 2º grau", W / 2, 760, AMBER, size=28, a=ad,
             anchor="center")


def b_combo(c, t, C, B):
    head(c, t, B["start"], "CASOS JUNTOS", "A ORDEM DE ATAQUE", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        passo(c, "", "x^3 - 4x", 300, 280, aa, 70)
        passo(c, "", "= x(x^2-4)", 760, 280, ep(t, C["13.a"] + 1.8, 0.4), 70)
        pill(c, "fator comum: x", 920, 370, BLUE, size=26, a=ep(t, C["13.a"] + 1.8, 0.4), anchor="center")
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        pill(c, "x² − 4: diferença de quadrados!", 1350, 370, AMBER, size=28, a=ab, anchor="center")
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 640, 430, 900, 120, 22, mix("#FFFFFF", PURPLE, 0.08), acc)
        expr(c, "= x(x+2)(x-2)", 1090, 490, 72, acc, cores={1: GREEN})
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        boxed(c, 260, 600, 1400, 200, GREEN, ad, 0.08)
        text(c, "ORDEM DE ATAQUE", W / 2, 646, 22, "black", GREEN, ad, tracking=2)
        steps = ["1  fator comum", "2  produto notável", "3  soma e produto"]
        for k, s in enumerate(steps):
            ak = ep(t, C["13.d"] + 0.6 + 0.9 * k, 0.4)
            chip(c, s, 520 + k * 440, 730, GREEN, ak, 36)
            if k < 2:
                arrow(c, 700 + k * 440, 730, 780 + k * 440, 730, GREEN, ak, 5, 14)


# ======================================================================
# bloco g — frações algébricas
# ======================================================================

def b_tesoura(c, t, C, B):
    head(c, t, B["start"], "FRAÇÕES ALGÉBRICAS", "O QUE PODE SER CORTADO?", BLUE)
    card(c, *CARD_R)
    defin(c, "FRAÇÃO ALGÉBRICA", "uma fração com letras", 260, 200, 640, ep(t, C["14.a"], 0.5))
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        boxed(c, 960, 200, 700, 110, PURPLE, ab, 0.08)
        text_mid(c, "corta-se FATOR, nunca TERMO", 1310, 255, 38, "black", PURPLE, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 360, 640, 430, 24, "#FFFFFF", acc, shadow=True)
        expr(c, "{x+3}/3", 580, 520, 100, acc, cores={0: INK})
        u = ep(t, C["14.c"] + 1.0, 1.4)
        tesoura(c, lerp(840, 560, u), 480, 110, acc * (1 - ep(t, C["14.c"] + 2.6, 0.3)), abs(math.sin(u * 5)), RED)
        sa = ep(t, C["14.c"] + 2.4, 0.4)
        selo(c, 580, 690, sa, "TERMO: NÃO CORTA", RED, -4, 32)
        text(c, "um pedaço do bolo", 580, 760, 26, "bold", GRAY, sa)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 960, 360, 700, 430, 24, "#FFFFFF", ad, shadow=True)
        u = ep(t, C["14.d"] + 1.0, 1.2)
        s1 = ep(t, C["14.d"] + 2.0, 0.4)
        fcorta(c, ["(x+3)", "(x-3)"], ["x", "(x+3)"], 1310, 520, 72, ad, {("n", 0), ("d", 1)}, s1,
               cores={("n", 0): GREEN, ("d", 1): GREEN})
        tesoura(c, lerp(1640, 1480, u), 415, 90, ad * (1 - ep(t, C["14.d"] + 2.4, 0.3)), abs(math.sin(u * 5)), GREEN)
        selo(c, 1310, 690, s1, "FATOR: CORTA", GREEN, -4, 32)


def b_fracao(c, t, C, B):
    head_seq(c, t, C, [("15", "SIMPLIFICAR", "FATORE PRIMEIRO", PURPLE), ("16", "E O −3?", "CONTINUA PROIBIDO", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        expr(c, "{x^2-9}/{x^2+3x}", 420, 330, 76, aa)
        ab = ep(t, C["15.b"], 0.5)
        if ab > 0:
            boxed(c, 760, 230, 900, 200, AMBER, ab, 0.08)
            text(c, "CONDIÇÃO DE EXISTÊNCIA: denominador ≠ 0", 1210, 280, 26, "black", AMBER, ab)
            expr(c, "x(x+3) ≠ 0", 1210, 340, 52, ep(t, C["15.b"] + 2.0, 0.4))
            text(c, "proibidos:  x = 0   e   x = −3", 1210, 410, 32, "black", RED, ep(t, C["15.b"] + 3.4, 0.4))
        acc = ep(t, C["15.c"], 0.5)
        ad = ep(t, C["15.d"], 0.5)
        if acc > 0:
            expr(c, "=", 330, 590, 70, acc)
            fcorta(c, ["(x+3)", "(x-3)"], ["x", "(x+3)"], 620, 590, 70, acc, {("n", 0), ("d", 1)}, ad,
                   cores={("n", 0): GREEN, ("d", 1): GREEN} if ad > 0 else None)
        if ad > 0:
            pill(c, "fator: corta", 620, 730, GREEN, size=26, a=ad, anchor="center")
        ae = ep(t, C["15.e"], 0.5)
        if ae > 0:
            rrect(c, 1010, 500, 650, 260, 24, mix("#FFFFFF", PURPLE, 0.08), ae)
            expr(c, "= {x-3}/x", 1335, 590, 76, ae, cores={1: GREEN})
            text(c, "x ≠ 0  e  x ≠ −3", 1335, 720, 36, "black", AMBER, ae)
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        pill(c, "x = −3 na conta ORIGINAL", W / 2, 260, BLUE, size=30, a=aa, anchor="center")
        expr(c, "{(-3)^2-9}/{(-3)^2+3·(-3)} = {9-9}/{9-9} = 0/0", W / 2, 420, 64, aa, cores={4: RED})
        selo(c, 1560, 520, ep(t, C["16.a"] + 2.5, 0.4), "NÃO EXISTE", RED, -5, 34)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        text(c, "simplificar não pode CRIAR um valor", W / 2, 600, 40, "black", INK2, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        regra(c, "o que era PROIBIDO continua PROIBIDO", W / 2, 730, acc, 42, AMBER)


# ======================================================================
# bloco h — o produto notável ao contrário
# ======================================================================

def b_contrario(c, t, C, B):
    head(c, t, B["start"], "AO CONTRÁRIO", "A SOMA DOS QUADRADOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        expr(c, "(a+b)^2 = a^2 + 2ab + b^2", W / 2, 270, 66, aa, cores={4: AMBER})
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        boxed(c, 340, 350, 1240, 140, PURPLE, ab, 0.08)
        expr(c, "a^2 + b^2 = (a+b)^2 - 2ab", W / 2, 420, 72, ab, cores={6: AMBER})
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        text(c, "soma 5  ·  produto 6", 560, 570, 40, "black", BLUE, acc)
        expr(c, "5^2 - 2·6 = 25 - 12 = 13", 1220, 570, 58, ep(t, C["17.c"] + 1.6, 0.4), cores={6: GREEN})
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        expr(c, "2 e 3:  2^2 + 3^2 = 4 + 9 = 13", W / 2, 690, 50, ad)
        conferido(c, "sem descobrir os números!", 700, 790, ep(t, C["17.d"] + 2.4, 0.4), True, 34)


# ======================================================================
# nós fazemos, recap, erros
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "FATORE EM CIMA E EMBAIXO", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    expr(c, "{x^2-25}/{x^2-10x+25}", 420 if t >= C["19"] else W / 2, 330, 80, aa)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 600)
    if t < C["19"]:
        return
    a1 = ep(t, C["19.a"], 0.5)
    if a1 > 0:
        text(c, "em cima", 900, 240, 26, "black", BLUE, a1, align="left")
        mdraw(c, "(x+5)(x-5)", 900, 300, 54, BLUE, a1)
    a2 = ep(t, C["19.b"], 0.5)
    if a2 > 0:
        text(c, "embaixo (pontas x e 5 · meio 10x)", 900, 380, 26, "black", PURPLE, a2, align="left")
        mdraw(c, "(x-5)^2", 900, 440, 54, PURPLE, a2)
        pill(c, "proibido: x = 5", 1340, 440, AMBER, size=26, a=ep(t, C["19.b"] + 3.0, 0.4))
    a3 = ep(t, C["19.c"], 0.5)
    if a3 > 0:
        rrect(c, 260, 520, 700, 150, 22, mix("#FFFFFF", PURPLE, 0.08), a3)
        expr(c, "= {x+5}/{x-5}", 610, 595, 66, a3, cores={1: GREEN})
    a4 = ep(t, C["19.d"], 0.5)
    if a4 > 0:
        pill(c, "teste: x = 0", 1300, 560, BLUE, size=28, a=a4, anchor="center")
        expr(c, "{-25}/25 = -1", 1180, 680, 46, a4)
        expr(c, "5/{-5} = -1", 1460, 680, 46, ep(t, C["19.d"] + 3.0, 0.4))
        conferido(c, "bateu", 1240, 790, ep(t, C["19.d"] + 4.5, 0.4), True, 32)


FRASES = ["Fatorar é o caminho de volta do produto notável.",
          "Comece sempre pelo fator comum.",
          "Corta-se fator, nunca termo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 320 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 62)


ERROS = [("Cortar o 3 em (x + 3)/3", "o 3 está em cima e embaixo, como nas frações de número",
          "em cima o 3 é TERMO: fatore antes; se não virou multiplicação, não corta"),
         ("x² − 16 = (x − 4)²", "tem quadrado, tem 4, tem sinal de menos",
          "(x − 4)² teria o termo −8x. O certo: (x + 4)(x − 4)"),
         ("Simplificar e esquecer a condição de existência", "(x − 3)/x aceita o −3 sem reclamar",
          "na original, −3 dá 0/0: escreva os proibidos ANTES de cortar")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _painel(c, y0, a, x=170, w=760):
    rrect(c, x, y0, w, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS4 = [("A", "={-2}/{x+2}", "cortou o x² (termo)", RED), ("B", "={x-4}/{x+4}", "", GREEN),
         ("C", "={x+4}/{x-4}", "inverteu", RED), ("D", "=x-4", "esqueceu o quadrado", RED),
         ("E", "={(x-4)^2}/{(x+4)^2}", "x² − 16 = (x − 4)²", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "SIMPLIFICAR FATORANDO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    text(c, "Para x ≠ −4, a expressão", 190, 250, 34, "black", INK, a0, align="left")
    expr(c, "{x^2-16}/{x^2+8x+16}", 420, 345, 62, a0)
    text(c, "é igual a", 680, 358, 34, "black", INK, a0, align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 210, 680, 42, C["25.ok"], "B", cues_in, cues_x, gap=12)
    if t >= C["25"]:
        y0 = 420
        _painel(c, y0, ep(t, C["25"], 0.4))
        passo(c, "", "x^2-16 = (x+4)(x-4)", 210, y0 + 60, ep(t, C["25.a"], 0.4), 40, BLUE)
        passo(c, "", "x^2+8x+16 = (x+4)^2", 210, y0 + 140, ep(t, C["25.b"], 0.4), 40, PURPLE)
        text(c, "2 · x · 4 = 8x ✓", 820, y0 + 150, 24, "black", GREEN, ep(t, C["25.b"] + 2.5, 0.4), align="right")
        ac = ep(t, C["25.c"], 0.4)
        if ac > 0:
            expr(c, "{(x+4)(x-4)}/{(x+4)^2} = {x-4}/{x+4}", 540, y0 + 250, 40, ac, cores={2: GREEN})
        conferido(c, "x = 0:  −16/16 = −1  e  −4/4 = −1", 210, y0 + 370, ep(t, C["25.d"], 0.4), True, 26)


ALTS5 = [("A", "53", "", GREEN), ("B", "67", "81 − 14: tirou só ab", RED), ("C", "81", "(a + b)² direto", RED),
         ("D", "95", "81 + 14: somou", RED), ("E", "109", "81 + 28: somou", RED)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "O PRODUTO NOTÁVEL AO CONTRÁRIO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    ap = ep(t, C["27"], 0.4) * (1 - a0)
    if ap > 0:
        pill(c, "retângulo:  diagonal² = lado² + lado²  (Pitágoras)", W / 2, 300, PURPLE, size=30, a=ap, anchor="center")
    if a0 > 0:
        y = 250
        for ln in K.wrap("Um retângulo tem perímetro de 18 cm e área de 14 cm². O quadrado da medida da diagonal desse "
                         "retângulo, em centímetros quadrados, é", "black", 28, 720):
            text(c, ln, 190, y, 28, "black", INK, a0, align="left"); y += 40
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["28"], 0.3)),
             align="left")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 40, C["28.ok"], "A", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["27.end"] - 1.9, 540, 560)
    if t >= C["28"]:
        y0 = 430
        _painel(c, y0, ep(t, C["28"], 0.4))
        passo(c, "", "a+b = 9   ·   ab = 14", 210, y0 + 60, ep(t, C["28.a"], 0.4), 40, BLUE)
        ab = ep(t, C["28.b"], 0.4)
        if ab > 0:
            mdraw(c, "a^2+b^2 = (a+b)^2 - 2ab", 210, y0 + 150, 40, PURPLE, ab)
            mdraw(c, "= 81 - 28 = 53", 300, y0 + 230, 44, GREEN, ep(t, C["28.b"] + 2.5, 0.4))
        conferido(c, "lados 2 e 7:  4 + 49 = 53", 210, y0 + 330, ep(t, C["28.c"], 0.4), True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "ATALHO DE CONTA", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        expr(c, "1003 · 997 = ?", W / 2, 400, 120, aa, cores={4: AMBER})
        pill(c, "sem calculadora  ·  em 5 segundos", W / 2, 560, AMBER, size=34, a=ep(t, C["30.a"] + 2.0, 0.4),
             anchor="center")
    pill(c, "ep. 4 · produtos notáveis como atalho de conta", W / 2, 720, PURPLE, size=32, a=ep(t, C["30.b"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Já cortou um termo achando que era fator?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, comum=b_comum, agrupa=b_agrupa,
              difquad=b_difquad, lshape=b_lshape, tqp=b_tqp, somaprod=b_somaprod, combo=b_combo, tesoura=b_tesoura,
              fracao=b_fracao, contrario=b_contrario, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4,
              q5=b_q5, ponte=b_ponte, cta=b_cta)
