"""Visual — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 4: do texto à equação e o descarte de raízes (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: jardim() (o jardim 10 × 6 com a calçada crescendo dos DOIS lados de cada medida, setas "+x" e "+x",
até o retângulo 14 × 10), lixeira() (a raiz −10 caindo na lixeira; um "10" falso tenta sair com selo vermelho),
tabela_camp() (4 times, A × B e B × A destacados como o mesmo jogo), triangulo() (Pitágoras: a tela e a diagonal).
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
_s = importlib.util.spec_from_file_location("comum036", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_2grau_ep4_texto_equacao.mp4"
CARD_R = K.CARD_R
VERDE_J = "#7BBF6A"     # grama do jardim
VERDE_JE = "#5E9E4F"
CALC = "#C9C4BA"        # calçada
CALC_E = "#A9A398"


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


def seta_h(c, x0, x1, y, col, a, w=4):
    if a <= 0:
        return
    line(c, x0, y, x1, y, col, a, w)
    for xe, s in ((x0, 1), (x1, -1)):
        p = skia.Path()
        p.moveTo(xe, y); p.lineTo(xe + s * 14, y - 9); p.lineTo(xe + s * 14, y + 9); p.close()
        c.drawPath(p, paint(col, a))


def seta_v(c, x, y0, y1, col, a, w=4):
    if a <= 0:
        return
    line(c, x, y0, x, y1, col, a, w)
    for ye, s in ((y0, 1), (y1, -1)):
        p = skia.Path()
        p.moveTo(x, ye); p.lineTo(x - 9, ye + s * 14); p.lineTo(x + 9, ye + s * 14); p.close()
        c.drawPath(p, paint(col, a))


def jardim(c, cx, cy, u, xw, a, rot=True, setas=0.0, rot_ext=0.0):
    """jardim 10 m × 6 m (u px por metro) com calçada de largura xw (m) em volta; setas = alfa das setas '+x'"""
    if a <= 0:
        return
    gw, gh = 10 * u, 6 * u
    ew, eh = gw + 2 * xw * u, gh + 2 * xw * u
    if xw > 0:
        rrect(c, cx - ew / 2, cy - eh / 2, ew, eh, 10, CALC, a, shadow=True)
        for k in range(1, 40):
            xx = cx - ew / 2 + k * u * 0.8
            if xx < cx + ew / 2 - 4:
                line(c, xx, cy - eh / 2 + 3, xx, cy - gh / 2 - 3, CALC_E, a * 0.5, 2)
                line(c, xx, cy + gh / 2 + 3, xx, cy + eh / 2 - 3, CALC_E, a * 0.5, 2)
    rrect(c, cx - gw / 2, cy - gh / 2, gw, gh, 8, VERDE_J, a, shadow=xw <= 0)
    for k in range(6):
        for j in range(4):
            c.drawCircle(cx - gw / 2 + (k + 0.5) * gw / 6, cy - gh / 2 + (j + 0.5) * gh / 4, u * 0.18, paint(VERDE_JE, a))
    if rot:
        fmid(c, "10 m", cx, cy - gh / 2 + 34, 30, "black", "#FFFFFF", a)
        fmid(c, "6 m", cx - gw / 2 + 50, cy, 30, "black", "#FFFFFF", a)
    if setas > 0 and xw > 0:
        y = cy - eh / 2 - 26
        seta_h(c, cx - ew / 2, cx - gw / 2, y, BLUE, a * setas)
        seta_h(c, cx + gw / 2, cx + ew / 2, y, BLUE, a * setas)
        fmid(c, "+x", cx - gw / 2 - xw * u / 2, y - 30, 30, "black", BLUE, a * setas)
        fmid(c, "+x", cx + gw / 2 + xw * u / 2, y - 30, 30, "black", BLUE, a * setas)
        x = cx + ew / 2 + 26
        seta_v(c, x, cy - eh / 2, cy - gh / 2, BLUE, a * setas)
        seta_v(c, x, cy + gh / 2, cy + eh / 2, BLUE, a * setas)
        fmid(c, "+x", x + 36, cy - gh / 2 - xw * u / 2, 30, "black", BLUE, a * setas)
        fmid(c, "+x", x + 36, cy + gh / 2 + xw * u / 2, 30, "black", BLUE, a * setas)
    if rot_ext > 0:
        pill(c, "10 + 2x", cx, cy + eh / 2 + 40, PURPLE, size=28, a=a * rot_ext, anchor="center", bounds=(0, 1920))
        pill(c, "6 + 2x", cx - ew / 2 - 20, cy, PURPLE, size=28, a=a * rot_ext, anchor="right", bounds=(0, 1920))


def lixeira(c, cx, cy, s, a, tampa=0.0):
    """lixeira cinza com tampa (tampa = 0 fechada … 1 aberta)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - s * 0.55, cy - s * 0.5); p.lineTo(cx + s * 0.55, cy - s * 0.5)
    p.lineTo(cx + s * 0.44, cy + s * 0.7); p.lineTo(cx - s * 0.44, cy + s * 0.7); p.close()
    c.drawPath(p, paint("#8D949B", a))
    for k in (-0.22, 0, 0.22):
        line(c, cx + k * s, cy - s * 0.36, cx + k * s * 0.85, cy + s * 0.58, "#6E757C", a, max(3, s * 0.04))
    c.save()
    c.translate(cx + s * 0.6, cy - s * 0.56); c.rotate(55 * tampa)
    rrect(c, -s * 1.22, -s * 0.12, s * 1.24, s * 0.14, s * 0.05, "#6E757C", a)
    rrect(c, -s * 0.74, -s * 0.24, s * 0.28, s * 0.14, s * 0.04, "#6E757C", a)
    c.restore()


def chip_raiz(c, s, cx, cy, col, a, size=56):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 50
    rrect(c, cx - w / 2, cy - size * 0.75, w, size * 1.5, size * 0.4, col, a, shadow=True)
    fmid(c, s, cx, cy, size, "black", "#FFFFFF", a)


def descarte(c, t, t0, cx, cy, a, falso=None, s=120):
    """o chip −10 cai na lixeira (a partir de t0); falso = instante em que um '10' tenta sair, com selo vermelho"""
    if a <= 0:
        return
    k = ep(t, t0, 1.2)
    lixeira(c, cx, cy, s, a, tampa=min(1.0, k * 2.2) * (1 - ep(t, t0 + 1.4, 0.4)))
    if k < 1:
        yy = cy - s * 2.1 + k * s * 1.9
        chip_raiz(c, "−10", cx + (1 - k) * s * 0.8, yy, RED, a * (1 - ep(t, t0 + 1.0, 0.25)))
    if falso is not None:
        af = ep(t, falso, 0.5)
        if af > 0:
            chip_raiz(c, "10", cx + s * 0.25, cy - s * 0.95 - 30 * af, AMBER, a * af, 48)
            selo(c, cx + s * 2.1, cy - s * 0.2, a * af, "NÃO VIRA 10", RED, -8, 30)


TIMES = "ABCD"


def tabela_camp(c, t, x0, y0, cel, a, t_par=None):
    """tabela 4 × 4 de turno único; t_par = instante do destaque de A × B e B × A"""
    if a <= 0:
        return
    for i, L in enumerate(TIMES):
        fmid(c, L, x0 + (i + 1) * cel + cel / 2, y0 + cel / 2, 34, "black", BLUE, a)
        fmid(c, L, x0 + cel / 2, y0 + (i + 1) * cel + cel / 2, 34, "black", BLUE, a)
    ap = ep(t, t_par, 0.5) if t_par is not None else 0
    for i in range(4):
        for j in range(4):
            x, y = x0 + (j + 1) * cel, y0 + (i + 1) * cel
            if i == j:
                rrect(c, x + 4, y + 4, cel - 8, cel - 8, 10, "#E3E3DF", a)
                continue
            par = {i, j} == {0, 1}
            col = mix("#FFFFFF", AMBER, 0.45 * ap) if par else "#FFFFFF"
            rrect(c, x + 4, y + 4, cel - 8, cel - 8, 10, col, a, shadow=True)
            fmid(c, f"{TIMES[i]}×{TIMES[j]}", x + cel / 2, y + cel / 2, 24, "bold", INK2 if not par else INK, a)


def triangulo(c, x0, y0, w, h, a, lados=("x", "x + 2", "10"), col=None):
    """retângulo da tela com a diagonal (Pitágoras): base w, altura h, canto em (x0, y0) = canto superior esquerdo"""
    if a <= 0:
        return
    rrect(c, x0, y0, w, h, 8, mix("#FFFFFF", BLUE, 0.08), a)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, w, h), paint(INK2, a, stroke=4))
    line(c, x0, y0 + h, x0 + w, y0, col or PURPLE, a, 6)
    line(c, x0 + w - 28, y0 + h, x0 + w - 28, y0 + h - 28, INK2, a, 3)
    line(c, x0 + w - 28, y0 + h - 28, x0 + w, y0 + h - 28, INK2, a, 3)
    fmid(c, lados[1], x0 + w / 2, y0 + h + 34, 30, "black", INK, a)
    fmid(c, lados[0], x0 + w + 50, y0 + h / 2, 30, "black", INK, a, align="left")
    fmid(c, lados[2], x0 + w / 2 - 30, y0 + h / 2 - 34, 32, "black", col or PURPLE, a)


def _passos(c, t, rows, x, y0, size, dy, xnota=1700):
    for k, (t0, ex, nota, col) in enumerate(rows):
        a, d = rise(t, t0)
        if a <= 0:
            continue
        y = y0 + k * dy + d
        expr(c, ex, x, y, size, a, align="left")
        if nota:
            pill(c, nota, xnota, y, col or PURPLE, size=24, a=a, anchor="right", bounds=(0, 1920))


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A RAIZ QUE VAI PARA O LIXO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        chip_raiz(c, "−10", 760, 330, RED, aa, 64)
        chip_raiz(c, "2", 1160, 330, GREEN, aa, 64)
        text(c, "as raízes da equação", W / 2, 440, 30, "bold", GRAY, aa)
    ab = ep(t, C["01.b"], 0.5) * (1 - ep(t, C["01.c"], 0.4))
    if ab > 0:
        pill(c, "largura não pode ser negativa…  então 10 m?", W / 2, 540, AMBER, size=34, a=ab, anchor="center")
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        text(c, "a calçada mede 2 m", W / 2, 560, 52, "black", GREEN, ac)
    descarte(c, t, C["01.d"], W / 2 - 200, 760, ep(t, C["01.d"] - 0.3, 0.3), falso=C["01.d"] + 1.6, s=90)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "transformar áreas, campeonatos e lucros em equação", "largura × comprimento · times × adversários"),
            ("02.b", "escolher a raiz que faz sentido", "a que não serve vai para o lixo, inteira")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 260, y - 14, 34, a, GREEN)
        text(c, s, 320, y, 46, "black", INK, a, align="left")
        ftext(c, sub, 320, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    cols = [("03.a", "1º GRAU", BLUE, ["etiqueta: x = ?", "a raiz nem sempre", "é a resposta"]),
            ("03.b", "EXPRESSÕES", PURPLE, None),
            ("03.c", "EPISÓDIO 3", GREEN, ["soma e produto", "raízes de cabeça"])]
    for k, (cue, tit, col, linhas_) in enumerate(cols):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        cx = 420 + k * 540
        rrect(c, cx - 240, 290 + d, 480, 420, 26, "#FFFFFF", a, shadow=True)
        rrect(c, cx - 240, 290 + d, 480, 70, 26, col, a)
        rrect(c, cx - 240, 330 + d, 480, 30, 0, col, a)
        fmid(c, tit, cx, 326 + d, 30, "black", "#FFFFFF", a)
        if linhas_:
            for j, s in enumerate(linhas_):
                fmid(c, s, cx, 450 + j * 70 + d, 36, "black", INK, a)
        else:
            expr(c, "(x+2)^2", cx, 450 + d, 54, a)
            expr(c, "= x^2 + 4x + 4", cx, 560 + d, 46, a, cores={2: PURPLE})
            fmid(c, "o termo do meio", cx, 650 + d, 28, "bold", PURPLE, a)


# ======================================================================
# concreto · bloco a
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS SITUAÇÕES", "DO DIA A DIA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    jardim(c, 560, 470, 46, 1.2 * ep(t, C["04.a"] + 1.0, 1.0), aa)
    if aa > 0:
        text(c, "jardim com calçada em volta", 560, 760, 30, "black", INK2, aa)
    ab = ep(t, C["04.b"], 0.5)
    tabela_camp(c, t, 1080, 250, 100, ab)
    if ab > 0:
        text(c, "todo time enfrenta todo time", 1380, 760, 30, "black", INK2, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        linha(c, [("MODELAR", BLUE), (": transformar a situação em equação", INK)], W / 2, 810, 34, acc)


def b_nasce(c, t, C, B):
    head(c, t, B["start"], "BLOCO A · DE ONDE NASCE O x²", "DUAS MEDIDAS DESCONHECIDAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        text(c, "duas medidas desconhecidas se MULTIPLICAM", W / 2, 260, 40, "black", BLUE, aa)
    itens = [("05.b", "largura", "comprimento", "área"), ("05.c", "times", "adversários", "jogos"),
             ("05.d", "preço", "quantidade", "receita")]
    for k, (cue, s1, s2, res) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 370 + k * 120 + d
        chip(c, s1, 520, y, BLUE, a, 38, w=320)
        fmid(c, "×", 760, y, 56, "black", INK, a)
        chip(c, s2, 1000, y, BLUE, a, 38, w=320)
        fmid(c, "=  " + res, 1220, y, 40, "black", INK2, a, align="left")
    ae = ep(t, C["05.e"], 0.5)
    if ae > 0:
        rrect(c, 560, 720, 800, 100, 22, mix("#FFFFFF", PURPLE, 0.12), ae)
        expr(c, "x · x = x^2", W / 2, 770, 60, ae, cores={4: PURPLE})


# ======================================================================
# bloco b — a calçada
# ======================================================================

def b_calcada(c, t, C, B):
    head_seq(c, t, C, [("06", "BLOCO B · A CALÇADA", "ELA ABRAÇA O JARDIM", BLUE),
                       ("07", "BLOCO B · ARRUMAR", "IGUALE A ZERO E SIMPLIFIQUE", PURPLE),
                       ("08", "BLOCO B · QUAL RAIZ SERVE?", "VOLTE AO TEXTO", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid == "06":
        aa = ep(t, C["06"], 0.4)
        xw = 2.0 * ep(t, C["06.b"], 2.2)
        jardim(c, 640, 500, 40, xw, aa, setas=ep(t, C["06.b"] + 1.0, 0.5), rot_ext=ep(t, C["06.c"], 0.5))
        a1 = ep(t, C["06.a"], 0.5)
        if a1 > 0:
            rrect(c, 1130, 250, 560, 110, 20, mix("#FFFFFF", BLUE, 0.10), a1)
            text(c, "ETIQUETA", 1410, 285, 20, "black", BLUE, a1, tracking=2)
            text(c, "x = largura da calçada (m)", 1410, 332, 30, "black", INK, a1)
        a2 = ep(t, C["06.b"], 0.5)
        if a2 > 0:
            text(c, "dos DOIS lados de cada medida", 1410, 430, 30, "black", BLUE, a2)
            text(c, "cada medida cresce 2x", 1410, 480, 30, "bold", INK2, a2)
        a4 = ep(t, C["06.d"], 0.5)
        if a4 > 0:
            rrect(c, 1130, 560, 560, 220, 22, "#FFFFFF", a4, shadow=True)
            text(c, "ÁREA = comprimento × largura", 1410, 610, 24, "black", PURPLE, a4)
            expr(c, "(10+2x)(6+2x)", 1410, 680, 44, a4)
            expr(c, "= 140", 1410, 745, 44, a4)
        return
    if sid == "07":
        rows = [(C["07.a"], "4x^2 + 32x + 60 = 140", "distributiva", BLUE),
                (C["07.b"], "4x^2 + 32x − 80 = 0", "− 140 nos dois lados", PURPLE),
                (C["07.c"], "x^2 + 8x − 20 = 0", "÷ 4", GREEN)]
        _passos(c, t, rows, 240, 280, 62, 115)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            rrect(c, 240, 640, 1440, 160, 22, mix("#FFFFFF", GREEN, 0.10), ad)
            linha(c, [("soma ", INK2), ("−8", PURPLE), ("   ·   produto ", INK2), ("−20", PURPLE)], 700, 720, 40, ad)
            chip_raiz(c, "2", 1280, 720, GREEN, ad, 52)
            chip_raiz(c, "−10", 1480, 720, RED, ad, 52)
        return
    a0 = ep(t, C["08"], 0.4)
    jardim(c, 560, 470, 30, 2.0, a0, rot=False)
    if a0 > 0:
        pill(c, "14 m", 560, 640, PURPLE, size=28, a=a0, anchor="center")
        pill(c, "10 m", 330, 470, PURPLE, size=28, a=a0, anchor="right")
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text(c, "x é uma LARGURA: não existe negativa", 1280, 270, 30, "black", INK, aa)
    descarte(c, t, C["08.b"], 1150, 520, ep(t, C["08.b"] - 0.3, 0.3), s=90)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        chip_raiz(c, "x = 2 m", 1470, 470, GREEN, acc, 52)
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 1000, 680, 680, 110, 20, mix("#FFFFFF", GREEN, 0.10), ad)
        text(c, "14 · 10 = 140 m²  ✓", 1340, 750, 44, "black", GREEN, ad)


def b_atalho1(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ANTES DA FÓRMULA", GREEN)
    card(c, *CARD_R)
    passos = [("09.a", "1", "IGUALE A ZERO", "tudo de um lado, zero do outro"),
              ("09.b", "2", "DIVIDA POR UM FATOR COMUM", "4x² + 32x − 80 = 0  →  ÷ 4"),
              ("09.c", "3", "AS RAÍZES NÃO MUDAM", "números pequenos: soma e produto")]
    for k, (cue, n, tit, sub) in enumerate(passos):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 170 + d
        boxed(c, 260, y - 60, 1400, 140, GREEN, a, 0.08)
        badge_num(c, n, 340, y + 10, a, 34, bg=GREEN)
        text(c, tit, 420, y, 44, "black", INK, a, align="left")
        ftext(c, sub, 420, y + 50, 30, "bold", GRAY, a, align="left")


# ======================================================================
# bloco c — o campeonato
# ======================================================================

def b_campeonato(c, t, C, B):
    head_seq(c, t, C, [("10", "BLOCO C · O CAMPEONATO", "CADA JOGO CONTADO DUAS VEZES", BLUE),
                       ("11", "BLOCO C · 45 JOGOS", "QUANTOS TIMES?", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        if aa > 0:
            rrect(c, 240, 240, 720, 100, 20, mix("#FFFFFF", BLUE, 0.10), aa)
            linha(c, [("TURNO ÚNICO", BLUE), (": cada par joga UMA vez", INK)], 600, 290, 30, aa)
        tabela_camp(c, t, 1060, 220, 118, ep(t, C["10"], 0.4), t_par=C["10.c"])
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            text(c, "4 times × 3 adversários = 12", 600, 450, 40, "black", INK2, ab)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            pill(c, "A × B  e  B × A: o MESMO jogo", 600, 560, AMBER, size=32, a=acc, anchor="center")
        ad = ep(t, C["10.d"], 0.5)
        if ad > 0:
            rrect(c, 240, 640, 720, 160, 22, mix("#FFFFFF", GREEN, 0.12), ad)
            text(c, "12 ÷ 2 = 6 jogos", 600, 700, 48, "black", GREEN, ad)
            text(c, "cada jogo foi contado 2 vezes", 600, 760, 28, "bold", GRAY, ad)
        return
    a0 = ep(t, C["11"], 0.4)
    if a0 > 0:
        rrect(c, 1180, 240, 500, 150, 22, mix("#FFFFFF", PURPLE, 0.10), a0)
        text(c, "JOGOS (turno único)", 1430, 280, 22, "black", PURPLE, a0, tracking=2)
        expr(c, "{n(n−1)}/2", 1430, 335, 46, a0)
    rows = [(C["11.a"], "n^2 − n − 90 = 0", "45 jogos · × 2", BLUE),
            (C["11.b"], "Δ = 1 + 360 = 361 = 19^2", "", PURPLE),
            (C["11.c"], "n = {1+19}/2 = 10 times", "", GREEN)]
    _passos(c, t, rows, 240, 300, 52, 130, xnota=1120)
    acc = ep(t, C["11.c"] + 2.5, 0.4)
    if acc > 0:
        chip_raiz(c, "−9", 1440, 520, RED, acc * (1 - ep(t, C["11.c"] + 4.0, 0.6)), 44)
        lixeira(c, 1440, 560, 60, acc * ep(t, C["11.c"] + 3.6, 0.4))
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        rrect(c, 240, 700, 1440, 100, 20, mix("#FFFFFF", AMBER, 0.14), ad)
        linha(c, [("TURNO E RETURNO", AMBER), (": cada par joga 2 vezes  →  n(n − 1), sem ÷ 2", INK)], W / 2, 750, 32, ad)


def b_atalho2(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "DOIS NÚMEROS SEGUIDOS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        expr(c, "n·(n−1)", W / 2, 300, 70, aa)
        text(c, "um número vezes o anterior", W / 2, 380, 32, "bold", GRAY, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        linha(c, [("45 jogos  →  dobro ", INK2), ("90", PURPLE), ("  =  ", INK), ("10", GREEN), (" × 9", INK)],
              W / 2, 510, 56, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        boxed(c, 460, 620, 1000, 150, GREEN, acc, 0.10)
        text(c, "O MAIOR = NÚMERO DE TIMES", W / 2, 668, 24, "black", GREEN, acc, tracking=2)
        text(c, "10 times", W / 2, 735, 56, "black", INK, acc)


# ======================================================================
# blocos d e e
# ======================================================================

def b_descartar(c, t, C, B):
    head(c, t, B["start"], "BLOCO D · DESCARTAR", "NÃO É TROCAR O SINAL", RED)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 240, 240, 1440, 100, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("DESCARTAR", BLUE), (": jogar fora a raiz que não faz sentido", INK)], W / 2, 290, 34, aa)
        for k, s in enumerate(("medida negativa", "tempo negativo", "nº de times negativo")):
            chip(c, s, 520 + k * 440, 420, RED, aa * ep(t, C["13.a"] + 0.6 * k, 0.4), 30, w=380)
    descarte(c, t, C["13.b"], 760, 650, ep(t, C["13.b"] - 0.3, 0.3), falso=C["13.c"], s=110)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        text(c, "vai INTEIRA para o lixo", 1380, 620, 40, "black", INK, acc)
        text(c, "−10  ≠  10", 1380, 700, 52, "black", RED, acc)


def b_releia(c, t, C, B):
    head(c, t, B["start"], "BLOCO E · RELEIA A PERGUNTA", "UMA EQUAÇÃO, TRÊS RESPOSTAS", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    jardim(c, 520, 500, 28, 2.0, aa, rot=False)
    if aa > 0:
        text(c, "x = 2", 520, 720, 40, "black", GREEN, aa)
    perg = [("14.b", "largura da calçada?", "2 m"), ("14.b", "lado maior do conjunto?", "14 m"),
            ("14.c", "área só da calçada?", "140 − 60 = 80 m²")]
    for k, (cue, q, r) in enumerate(perg):
        a, d = rise(t, C[cue] + (1.8 if k == 1 else 0))
        if a <= 0:
            continue
        y = 290 + k * 150 + d
        rrect(c, 920, y - 50, 760, 120, 20, "#FFFFFF", a, shadow=True)
        text(c, q, 950, y, 28, "bold", GRAY, a, align="left")
        text(c, r, 950, y + 50, 40, "black", PURPLE, a, align="left")
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        selo(c, 1300, 780, ad, "RELEIA A PERGUNTA", AMBER, -3, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("15", "SUA VEZ", "PAUSE E TENTE", GREEN), ("16", "VAMOS JUNTOS", "ETIQUETA, ZERO, RAÍZES", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 260, 520, 300, 8, mix("#FFFFFF", "#D9B26B", 0.35), aa, shadow=True)
        fmid(c, "40 m²", 520, 410, 50, "black", INK, aa)
        fmid(c, "x", 520, 600, 36, "black", BLUE, aa)
        fmid(c, "x + 3", 860, 410, 36, "black", BLUE, aa, align="left")
    ab = ep(t, C["15.b"], 0.5) * (1 - ep(t, C["16"], 0.3))
    if ab > 0:
        text(c, "Quanto mede o LADO MENOR?", 1300, 330, 40, "black", INK, ab)
    pause_timer(c, t, C["15.end"] - 1.9, 1300, 520)
    if t < C["16"]:
        return
    rows = [(C["16.a"], "x(x+3) = 40", "x = lado menor (m)", BLUE),
            (C["16.b"] + 1.6, "x^2 + 3x − 40 = 0", "iguale a zero", PURPLE)]
    _passos(c, t, rows, 1000, 270, 48, 100, xnota=1700)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        linha(c, [("soma ", INK2), ("−3", PURPLE), (" · produto ", INK2), ("−40", PURPLE)], 1300, 500, 34, acc)
        chip_raiz(c, "5", 1200, 590, GREEN, acc, 44)
        chip_raiz(c, "−8", 1400, 590, RED, acc * (1 - ep(t, C["16.d"], 0.5)), 44)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        rrect(c, 1000, 680, 680, 120, 22, mix("#FFFFFF", GREEN, 0.12), ad)
        text(c, "lado menor: 5 m", 1340, 725, 38, "black", GREEN, ad)
        text(c, "5 · 8 = 40 m²  ✓", 1340, 778, 30, "black", INK2, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Duas medidas desconhecidas multiplicadas: equação do 2º grau.",
          "Iguale a zero e simplifique antes da fórmula.",
          "Raiz sem sentido se descarta, não se troca o sinal."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["17", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "17" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 62)


ERROS = [("raízes 2 e −10  →  “10 m”", "o 10 apareceu na conta, e largura tem que ser positiva",
          "o −10 vai INTEIRO para o lixo: a resposta é a outra raiz, 2 m"),
         ("Bhaskara direto em (10 + 2x)(6 + 2x) = 140", "os números estão todos ali",
          "a fórmula só vale com ZERO do outro lado: 4x² + 32x − 80 = 0 · c = −80, não 60"),
         ("(x + 1)² = x² + 1  em  x² + (x + 1)² = 25", "parece só elevar cada pedaço",
          "falta o termo do meio, 2x: x² + x − 12 = 0 → lados 3 e 4 (9 + 16 = 25)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["18", "19", "20"], ERROS)
    if which(t, C, ["18", "19", "20"]) == "20":
        a = ep(t, C["20"], 0.4) * (1 - ep(t, C["20.a"], 0.4))
        if a > 0:
            rrect(c, 300, 300, 1320, 380, 22, "#FFFFFF", a, shadow=True)
            text(c, "TEOREMA DE PITÁGORAS", W / 2, 360, 26, "black", BLUE, a, tracking=2)
            text(c, "num triângulo retângulo:", W / 2, 430, 32, "bold", GRAY, a)
            text(c, "lado maior² = soma dos quadrados dos outros dois", W / 2, 510, 38, "black", INK, a)
            expr(c, "a^2 + b^2 = c^2", W / 2, 610, 56, a, cores={4: PURPLE})


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, s, a, y0=250, size=29, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _questao(c, t, C, sid_q, sid_r, sid_x, enun, alts, okL, xs, fonte=True, ok_sid=None):
    a0 = ep(t, C[f"{sid_q}.a"], 0.4) * (1 - ep(t, C[sid_r], 0.4))
    yend = _enunciado(c, enun, a0)
    if fonte:
        text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"{sid_q}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in xs}
    K.alternativas(c, t, C, alts, 1000, 260, 680, 32, C[f"{ok_sid or sid_r}.ok"], okL, cues_in, cues_x, gap=30)
    pause_timer(c, t, C[f"{sid_q}.end"] - 1.9, 540, min(yend + 100, 760))
    return t >= C[sid_r]


ALTS1 = [("A", "2 m", "", GREEN),
         ("B", "2,5 m", "esqueceu o 4x²", RED),
         ("C", "4 m", "calçada num lado só", RED),
         ("D", "cerca de 4,5 m", "esqueceu o termo do meio", RED),
         ("E", "10 m", "trocou o sinal do −10", RED)]


def b_q1(c, t, C, B):
    head_seq(c, t, C, [("21", "QUESTÃO 1 · EU FAÇO", "A CALÇADA", BLUE), ("23", "QUESTÃO 1", "AS ERRADAS", RED)])
    card(c, *CARD_R)
    enun = ("Um jardim retangular de 10 m por 6 m será contornado por uma calçada de largura constante, em todos os "
            "lados. Com a calçada, o conjunto formará um retângulo de 140 m² de área. A largura da calçada será de")
    if not _questao(c, t, C, "21", "22", "23", enun, ALTS1, "A", "BCDE"):
        return
    ap = ep(t, C["22"], 0.4)
    _painel(c, ap)
    rows = [(C["22.a"], "(10+2x)(6+2x) = 140", "", None), (C["22.b"], "4x^2 + 32x − 80 = 0", "", None),
            (C["22.b"] + 2.2, "x^2 + 8x − 20 = 0", "", None)]
    _passos(c, t, rows, 220, 300, 44, 80)
    acc = ep(t, C["22.c"], 0.4)
    if acc > 0:
        chip_raiz(c, "2", 380, 580, GREEN, acc, 44)
        chip_raiz(c, "−10", 560, 580, RED, acc * (1 - ep(t, C["22.c"] + 2.0, 0.5)), 44)
        lixeira(c, 560, 600, 50, acc * ep(t, C["22.c"] + 1.8, 0.4))
    ad = ep(t, C["22.d"], 0.4)
    if ad > 0:
        rrect(c, 200, 680, 700, 110, 18, mix("#FFFFFF", GREEN, 0.12), ad)
        text(c, "14 · 10 = 140 m²  ✓", 550, 750, 38, "black", GREEN, ad)


ALTS6 = [("A", "8", "n² = 66", RED),
         ("B", "11", "n − 1  ou  |−11|", RED),
         ("C", "12", "", GREEN),
         ("D", "23", "parou em √Δ", RED),
         ("E", "33", "66 ÷ 2", RED)]


def b_q6(c, t, C, B):
    head_seq(c, t, C, [("24", "QUESTÃO 6 · NÓS FAZEMOS", "O CAMPEONATO", BLUE), ("26", "QUESTÃO 6", "AS ERRADAS", RED)])
    card(c, *CARD_R)
    enun = ("Em um campeonato de futebol de bairro disputado em turno único, cada time enfrenta cada um dos outros "
            "exatamente uma vez. A tabela completa tem 66 jogos. O número de times participantes é")
    if not _questao(c, t, C, "24", "25", "26", enun, ALTS6, "C", "ABDE"):
        return
    ap = ep(t, C["25"], 0.4)
    _painel(c, ap)
    rows = [(C["25"] + 0.3, "{n(n−1)}/2 = 66", "", None), (C["25.a"], "n^2 − n − 132 = 0", "", None),
            (C["25.b"], "Δ = 529 = 23^2", "", None), (C["25.c"], "n = {1+23}/2 = 12", "", None)]
    _passos(c, t, rows, 220, 300, 42, 95)
    acc = ep(t, C["25.c"] + 2.4, 0.4)
    if acc > 0:
        chip_raiz(c, "−11", 760, 585, RED, acc * (1 - ep(t, C["25.c"] + 3.6, 0.5)), 36)
        lixeira(c, 760, 610, 44, acc * ep(t, C["25.c"] + 3.4, 0.4))
    ad = ep(t, C["25.d"], 0.4)
    if ad > 0:
        rrect(c, 200, 690, 700, 110, 18, mix("#FFFFFF", GREEN, 0.12), ad)
        text(c, "12 · 11 ÷ 2 = 66 jogos  ✓", 550, 760, 36, "black", GREEN, ad)


ALTS9 = [("A", "5", "metade da diagonal", RED),
         ("B", "6", "é o lado MENOR", AMBER),
         ("C", "cerca de 7,1", "supôs tela quadrada", RED),
         ("D", "8", "", GREEN),
         ("E", "cerca de 8,9", "(x + 2)² = x² + 4", RED)]


def b_q9(c, t, C, B):
    head_seq(c, t, C, [("27", "QUESTÃO 9 · VOCÊ FAZ", "PITÁGORAS NA TELA", BLUE), ("29", "QUESTÃO 9", "AS ERRADAS", RED)])
    card(c, *CARD_R)
    enun = ("A diagonal de uma tela retangular mede 10 polegadas, e um dos lados da tela mede 2 polegadas a mais que o "
            "outro. A medida do lado maior, em polegadas, é")
    if not _questao(c, t, C, "27", "28", "29", enun, ALTS9, "D", "ABCE"):
        return
    ap = ep(t, C["28"], 0.4)
    _painel(c, ap)
    triangulo(c, 260, 260, 300, 190, ap)
    rows = [(C["28.a"], "x^2 + (x+2)^2 = 100", "", None), (C["28.b"], "x^2 + 2x − 48 = 0", "", None)]
    _passos(c, t, rows, 220, 530, 40, 80)
    acc = ep(t, C["28.c"], 0.4)
    if acc > 0:
        chip_raiz(c, "6", 330, 690, BLUE, acc, 36)
        chip_raiz(c, "−8", 470, 690, RED, acc * (1 - ep(t, C["28.c"] + 1.5, 0.5)), 36)
        text(c, "maior: 6 + 2 = 8", 720, 700, 32, "black", GREEN, acc)
    ad = ep(t, C["28.d"], 0.4)
    if ad > 0:
        text(c, "36 + 64 = 100  ✓", 550, 790, 34, "black", GREEN, ad)


ALTS7 = [("A", "10", "", GREEN),
         ("B", "20", "lucro máximo (Função quadrática)", AMBER),
         ("C", "30", "a outra raiz: o prejuízo volta", RED),
         ("D", "40", "soma das raízes", RED),
         ("E", "300", "produto das raízes", RED)]


def b_q7(c, t, C, B):
    head_seq(c, t, C, [("30", "DESAFIO FINAL", "QUANDO O PREJUÍZO ACABA", PURPLE),
                       ("31", "DESAFIO FINAL", "RECEITA − CUSTO", PURPLE),
                       ("32", "DESAFIO FINAL", "TESTE VALORES", GREEN)])
    card(c, *CARD_R)
    enun = ("Uma pequena fábrica vende x unidades de um produto por semana ao preço unitário de (50 − x) reais. O custo "
            "semanal de produção é 10x + 300 reais. A menor quantidade semanal vendida a partir da qual a fábrica deixa "
            "de ter prejuízo é")
    if not _questao(c, t, C, "30", "31", "32", enun, ALTS7, "A", "BCDE", ok_sid="32"):
        return
    ap = ep(t, C["31"], 0.4)
    _painel(c, ap)
    aa = ep(t, C["31.a"], 0.4)
    if aa > 0:
        defs = [("RECEITA", "preço × quantidade", BLUE), ("CUSTO", "o que sai", BLUE),
                ("LUCRO", "receita − custo", BLUE), ("PREJUÍZO", "lucro negativo", RED)]
        for k, (n, s, col) in enumerate(defs):
            a = aa * ep(t, C["31.a"] + 1.2 * k, 0.4)
            text(c, n, 210, 285 + k * 46, 26, "black", col, a, align="left")
            text(c, s, 420, 285 + k * 46, 26, "bold", INK2, a, align="left")
    rows = [(C["31.b"], "L = x(50−x) − (10x+300)", "", None), (C["31.b"] + 2.2, "L = −x^2 + 40x − 300", "", None),
            (C["31.c"], "x^2 − 40x + 300 = 0", "", None)]
    _passos(c, t, rows, 210, 490, 34, 64)
    acc = ep(t, C["31.c"] + 2.0, 0.4)
    if acc > 0:
        text(c, "Δ = 400   →   10  e  30", 550, 700, 34, "black", PURPLE, acc)
    a1 = ep(t, C["32.a"], 0.4)
    if a1 > 0:
        rrect(c, 200, 730, 700, 80, 16, mix("#FFFFFF", AMBER, 0.12), a1)
        text(c, "L(5) = −125: prejuízo", 380, 780, 26, "black", RED, a1)
        text(c, "L(20) = 100: lucro", 720, 780, 26, "black", GREEN, ep(t, C["32.b"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A EQUAÇÃO DISFARÇADA", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        expr(c, "x^4 − 13x^2 + 36 = 0", W / 2, 430, 96, aa)
        pill(c, "expoente 4", 720, 300, AMBER, size=30, a=aa, anchor="center")
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        selo(c, W / 2, 620, ab, "2º GRAU DISFARÇADA", PURPLE, -4, 46)
    acc = ep(t, C["34.c"], 0.5)
    if acc > 0:
        text(c, "biquadradas e x no denominador", W / 2, 780, 40, "black", INK2, acc)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"],
        "Você já marcou uma raiz com o sinal trocado?", canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, nasce=b_nasce, calcada=b_calcada,
              atalho1=b_atalho1, campeonato=b_campeonato, atalho2=b_atalho2, descartar=b_descartar, releia=b_releia,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q6=b_q6, q9=b_q9, q7=b_q7, ponte=b_ponte,
              cta=b_cta)
