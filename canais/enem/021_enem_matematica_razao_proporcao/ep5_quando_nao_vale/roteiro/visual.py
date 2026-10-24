"""Visual — Razão, Proporção e Regra de Três, Episódio 5: Quando a regra de três NÃO funciona (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, pizza, alternativas, erro_cards...).
Peças deste episódio: gato(), rato(), crono() (cronômetro individual), selo_ouro() (PERGUNTA DE OURO), grade de área,
cubinhos isométricos, barras de juros, conta por faixa e músicos.
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
_s = importlib.util.spec_from_file_location("comum021", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_razao_ep5_quando_nao_vale.mp4"
CARD_R = K.CARD_R
OURO = "#C9930E"
GATO = "#E8743B"
GATO_ESC = "#B9531F"
RATO = "#9A9A96"
AGUA = "#7CC3EA"
CUBO = ("#8FB8FF", "#5F93F0", "#3E7BFA")   # topo, esquerda, direita


# ======================================================================
# peças do episódio
# ======================================================================

def gato(c, cx, cy, s, a=1.0, col=GATO):
    """gato sentado de frente; (cx, cy) = centro do corpo; s = altura total"""
    if a <= 0:
        return
    rabo = skia.Path(); rabo.moveTo(cx + s * 0.22, cy + s * 0.22)
    rabo.cubicTo(cx + s * 0.55, cy + s * 0.25, cx + s * 0.55, cy - s * 0.15, cx + s * 0.38, cy - s * 0.18)
    c.drawPath(rabo, paint(col, a, stroke=s * 0.07, cap_round=True))
    c.drawOval(skia.Rect.MakeXYWH(cx - s * 0.26, cy - s * 0.12, s * 0.52, s * 0.48), paint(col, a))
    hy = cy - s * 0.26
    for sx in (-1, 1):
        o = skia.Path(); o.moveTo(cx + sx * s * 0.20, hy - s * 0.04); o.lineTo(cx + sx * s * 0.17, hy - s * 0.30)
        o.lineTo(cx + sx * s * 0.04, hy - s * 0.14); o.close()
        c.drawPath(o, paint(col, a))
    c.drawCircle(cx, hy, s * 0.20, paint(col, a))
    for sx in (-1, 1):
        c.drawCircle(cx + sx * s * 0.075, hy - s * 0.02, s * 0.03, paint(INK, a))
    c.drawCircle(cx, hy + s * 0.05, s * 0.022, paint(GATO_ESC, a))


def rato(c, cx, cy, s, a=1.0):
    """ratinho de lado; (cx, cy) = centro; s = comprimento do corpo"""
    if a <= 0:
        return
    r = skia.Path(); r.moveTo(cx - s * 0.45, cy + s * 0.05)
    r.cubicTo(cx - s * 0.8, cy + s * 0.1, cx - s * 0.75, cy - s * 0.3, cx - s * 0.95, cy - s * 0.25)
    c.drawPath(r, paint(RATO, a, stroke=s * 0.05, cap_round=True))
    c.drawOval(skia.Rect.MakeXYWH(cx - s * 0.5, cy - s * 0.25, s * 0.85, s * 0.45), paint(RATO, a))
    c.drawCircle(cx + s * 0.18, cy - s * 0.27, s * 0.13, paint(RATO, a))
    c.drawCircle(cx + s * 0.18, cy - s * 0.27, s * 0.07, paint("#E9B8C2", a))
    c.drawCircle(cx + s * 0.28, cy - s * 0.06, s * 0.035, paint(INK, a))


def crono(c, cx, cy, r, frac, a=1.0, rotulo="2 min", col=GREEN):
    """cronômetro: arco que enche até frac (0–1), com o rótulo embaixo"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint("#D4D4CF", a, stroke=5))
    rrect(c, cx - r * 0.18, cy - r - r * 0.32, r * 0.36, r * 0.22, 4, INK2, a)
    if frac > 0:
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r * 0.82, cy - r * 0.82, r * 1.64, r * 1.64), -90, 360 * min(frac, 0.9999), False)
        p.close()
        c.drawPath(p, paint(col, a * 0.85))
    ang = -math.pi / 2 + 2 * math.pi * frac
    c.drawLine(cx, cy, cx + r * 0.7 * math.cos(ang), cy + r * 0.7 * math.sin(ang), paint(INK, a, stroke=4, cap_round=True))
    c.drawCircle(cx, cy, 5, paint(INK, a))
    if rotulo:
        text(c, rotulo, cx, cy + r + 40, 26, "black", INK2, a)


def selo_ouro(c, x, y, a, size=30):
    """selo dourado da PERGUNTA DE OURO"""
    if a <= 0:
        return
    selo(c, x, y, a, "★ PERGUNTA DE OURO", OURO, -4, size)


def boneco(c, cx, cy, s, col, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy - s * 0.30, s * 0.17, paint(col, a))
    rrect(c, cx - s * 0.22, cy - s * 0.10, s * 0.44, s * 0.48, s * 0.18, col, a)


def grade(c, x, y, lado, n, a=1.0, cor=BLUE, prog_=1.0):
    """quadrado de lado `lado` px dividido em n × n quadradinhos; prog_ acende os quadradinhos um a um"""
    if a <= 0:
        return
    q = lado / n
    tot = n * n
    for i in range(tot):
        r_, k = divmod(i, n)
        ai = a * clamp(prog_ * tot - i, 0, 1)
        if ai > 0:
            rrect(c, x + k * q + 4, y + r_ * q + 4, q - 8, q - 8, 8, mix("#FFFFFF", cor, 0.35), ai)
    c.drawRect(skia.Rect.MakeXYWH(x, y, lado, lado), paint(INK, a, stroke=5))


def cubinho(c, x, y, s, a=1.0, cores=CUBO):
    """cubo isométrico; (x, y) = vértice de cima da face de topo; s = aresta na tela"""
    if a <= 0:
        return
    dx, dy = s * 0.866, s * 0.5
    top = skia.Path(); top.moveTo(x, y); top.lineTo(x + dx, y + dy); top.lineTo(x, y + 2 * dy); top.lineTo(x - dx, y + dy); top.close()
    lef = skia.Path(); lef.moveTo(x - dx, y + dy); lef.lineTo(x, y + 2 * dy); lef.lineTo(x, y + 2 * dy + s); lef.lineTo(x - dx, y + dy + s); lef.close()
    rig = skia.Path(); rig.moveTo(x + dx, y + dy); rig.lineTo(x, y + 2 * dy); rig.lineTo(x, y + 2 * dy + s); rig.lineTo(x + dx, y + dy + s); rig.close()
    for pth, col in ((top, cores[0]), (lef, cores[1]), (rig, cores[2])):
        c.drawPath(pth, paint(col, a))
        c.drawPath(pth, paint("#FFFFFF", a, stroke=2.5))


def cubo_n(c, x, y, s, n, a=1.0, vis=None):
    """n × n × n cubinhos isométricos; (x, y) = topo do bloco; vis = quantos aparecem (na ordem de baixo para cima)"""
    dx, dy = s * 0.866, s * 0.5
    cells = [(i, j, k) for k in range(n) for i in range(n) for j in range(n)]
    total = len(cells)
    vis = total if vis is None else vis
    # ordem de pintura: de trás para a frente, de baixo para cima
    order = sorted(range(total), key=lambda m: (cells[m][2], cells[m][0] + cells[m][1]))
    for rank, m in enumerate(order):
        i, j, k = cells[m]
        ai = a * clamp(vis - rank, 0, 1)
        if ai <= 0:
            continue
        px = x + (i - j) * dx
        py = y + (i + j) * dy + (n - 1 - k) * s
        cubinho(c, px, py, s, ai)


# ======================================================================
# abertura
# ======================================================================

def _gatos_ratos(c, x0, y, n, a, s=90, gap=150):
    for k in range(n):
        gato(c, x0 + k * gap, y, s, a)
        rato(c, x0 + k * gap + 10, y + 110, 52, a)


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "QUANDO A REGRA DE TRÊS ENGANA", RED)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    _gatos_ratos(c, 300, 340, 2, aa)
    crono(c, 650, 370, 58, ep(t, C["01.a"] + 0.6, 1.2), aa)
    text(c, "2 gatos · 2 ratos · 2 min", 480, 600, 34, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        _gatos_ratos(c, 1000, 340, 4, ab, 80, 130)
        fmid(c, "?", 1690, 380, 120, "black", AMBER, ab)
        text(c, "4 gatos · 4 ratos · ? min", 1250, 600, 34, "black", INK, ab)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        chip(c, "4 minutos?", 760, 700, RED, ac, 34)
        chip(c, "1 minuto?", 1160, 700, RED, ep(t, C["01.c"] + 0.8, 0.4), 34)
    ad = ep(t, C["01.d"], 0.5)
    selo(c, W / 2, 790, ad, "A REGRA DE TRÊS TE ENGANOU", RED, -2, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "reconhecer a regra de três-armadilha", "quando dobrar a causa NÃO dobra o efeito"),
            ("02.b", "usar 3 hábitos de prova", "que pegam a maioria dos erros")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "LEMBRETE DO EPISÓDIO 3", "O TESTE DO DOBRO", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        for j, (lab, op, nome, col) in enumerate((("×2", "×2", "DIRETA", BLUE), ("×2", "÷2", "INVERSA", PURPLE))):
            x = 560 + j * 800
            card(c, x - 300, 250, 600, 260, aa)
            text(c, "uma grandeza", x - 140, 320, 26, "bold", INK2, aa)
            text(c, "a outra", x + 140, 320, 26, "bold", INK2, aa)
            text(c, lab, x - 140, 400, 60, "black", INK, aa)
            text(c, op, x + 140, 400, 60, "black", col, aa)
            arrow(c, x - 70, 382, x + 70, 382, GRAY, aa, 4, 12)
            pill(c, nome, x, 465, col, size=28, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        boxed(c, 260, 560, 1400, 130, BLUE, ab, 0.08)
        text(c, "PROPORCIONAIS", W / 2, 612, 34, "black", BLUE, ab)
        text(c, "dobrar uma dobra EXATAMENTE a outra (ou corta exatamente pela metade)", W / 2, 662, 28, "bold", INK2, ab)
    ac = ep(t, C["03.c"], 0.5)
    text(c, "só aí a regra de três funciona", W / 2, 760, 38, "black", GREEN, ac)


# ======================================================================
# a pergunta de ouro
# ======================================================================

def _pizza_dupla(c, x_peq, x_gr, cy, r, a, a4=0.0):
    """pizza pequena (raio r) e a grande (raio 2r); a4 = 4 pequenas em 2×2 ao lado"""
    K.pizza(c, x_peq, cy, r, 6, 0, a)
    K.pizza(c, x_gr, cy, 2 * r, 8, 0, a)


def b_cotidiano(c, t, C, B):
    frame(c, t, B["start"], "NEM TUDO É PROPORCIONAL", "TRÊS CENAS DO DIA A DIA", AMBER)
    for k, (cue, titulo, linha) in enumerate((("04.a", "pizza", "diâmetro ×2 → pizza ×4"),
                                               ("04.b", "conta de luz", "consumo ×2 → conta ≠ ×2"),
                                               ("04.c", "bebê", "9 pessoas ≠ 1 mês"))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        card(c, x - 240, 240 + d, 480, 470, a)
        text(c, titulo, x, 310 + d, 40, "black", INK, a)
        if k == 0:
            K.pizza(c, x - 120, 470 + d, 45, 6, 0, a)
            K.pizza(c, x + 70, 470 + d, 90, 8, 0, a)
        elif k == 1:
            rrect(c, x - 80, 380 + d, 160, 200, 14, "#FFFFFF", a, shadow=True)
            for j in range(4):
                line(c, x - 55, 420 + d + j * 30, x + 55 - (j % 2) * 40, 420 + d + j * 30, "#D4D4CF", a, 6)
            ftext(c, "R$ ?", x, 560 + d, 40, "black", AMBER, a)
        else:
            for j in range(9):
                r_, q = divmod(j, 3)
                boneco(c, x - 90 + q * 60, 410 + d + r_ * 70, 56, [BLUE, PURPLE, GREEN][q], a)
            fmid(c, "≠", x + 90, 480 + d, 60, "black", RED, a)
            text(c, "1 mês", x + 160, 495 + d, 30, "black", RED, a)
        text(c, linha, x, 670 + d, 28, "black", AMBER if k else PURPLE, a)


def b_ouro(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE QUALQUER REGRA DE TRÊS", "A PERGUNTA DE OURO", OURO)
    a0 = ep(t, C["05"], 0.5)
    selo_ouro(c, W / 2, 270, a0, 38)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 360, 340, 1200, 140, OURO, aa, 0.10)
        text_mid(c, "Dobrar a CAUSA dobra MESMO o EFEITO?", W / 2, 410, 52, "black", INK, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        card(c, 360, 540, 560, 220, ab)
        check_icon(c, 430, 625, 40, ab, GREEN)
        text(c, "SIM", 500, 640, 56, "black", GREEN, ab, align="left")
        text(c, "pode usar a regra de três", 640, 720, 28, "bold", INK2, ab)
    ac = ep(t, C["05.c"], 0.5)
    if ac > 0:
        card(c, 1000, 540, 560, 220, ac)
        check_icon(c, 1070, 625, 40, ac, RED, "x")
        text(c, "NÃO ou DEPENDE", 1140, 640, 48, "black", RED, ac, align="left")
        text(c, "regra de três FORA", 1280, 720, 28, "bold", INK2, ac)


# ======================================================================
# bloco A — os gatos
# ======================================================================

def b_gatos(c, t, C, B):
    head_seq(c, t, C, [("06", "OS GATOS", "O RITMO DE UM GATO SÓ", BLUE), ("07", "QUATRO GATOS", "QUATRO CRONÔMETROS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            gato(c, 400, 400, 150, aa)
            text(c, "UM gato", 400, 600, 34, "black", INK, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            for k in range(2):
                x = 800 + k * 300
                gato(c, x, 380, 120, ab)
                rato(c, x + 10, 510, 64, ab)
                arrow(c, x, 455, x + 5, 478, GATO_ESC, ab, 4, 10)
            text(c, "cada gato → UM rato", 950, 610, 32, "black", INK, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            boxed(c, 690, 650, 520, 100, BLUE, acc, 0.08)
            text_mid(c, "EM PARALELO = ao mesmo tempo", 950, 700, 30, "black", BLUE, acc)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            crono(c, 1480, 420, 100, ep(t, C["06.d"], 2.0), ad)
            text(c, "cada um: 2 minutos", 1480, 640, 32, "black", GREEN, ad)
        return
    a0 = ep(t, C["07"], 0.5)
    run = prog(t, C["07.c"], 2.2)
    for k in range(4):
        x = 330 + k * 300
        ak = a0 * ep(t, C["07"] + 0.2 * k, 0.4)
        gato(c, x, 330, 110, ak)
        rato(c, x + 10, 450, 58, ep(t, C["07.a"], 0.5) * ak)
        crono(c, x, 600, 52, run if t >= C["07.c"] else 0, ep(t, C["07.b"], 0.5) * ak, "2 min" if run >= 1 else "")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        text(c, "gatos ×2 e ratos ×2 → o RITMO não muda", 760, 770, 34, "black", PURPLE, ad)
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1360, 610, 330, 200, "ATALHO", ["reduza a UM:", "quanto UM faz?"], ae, 30)


# ======================================================================
# bloco B — área e lado
# ======================================================================

def b_area(c, t, C, B):
    head_seq(c, t, C, [("08", "LADO DOBROU", "E A ÁREA?", BLUE), ("09", "A PIZZA", "RELAÇÃO QUADRÁTICA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        if aa > 0:
            boxed(c, 220, 230, 760, 100, BLUE, aa, 0.08)
            text_mid(c, "ÁREA = quantos quadradinhos cabem", 600, 280, 32, "black", BLUE, aa)
        ab = ep(t, C["08.b"], 0.5)
        grade(c, 330, 420, 150, 1, ab, BLUE, ep(t, C["08.b"], 0.6))
        text(c, "lado 1", 405, 630, 30, "black", INK2, ab)
        text(c, "1 quadradinho", 405, 690, 30, "black", BLUE, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            arrow(c, 540, 495, 720, 495, GRAY, acc, 4, 12)
            text(c, "lado ×2", 630, 470, 28, "black", INK2, acc)
            grade(c, 780, 350, 300, 2, acc, PURPLE, prog(t, C["08.c"] + 0.4, 1.4))
            text(c, "lado 2", 930, 700, 30, "black", INK2, acc)
            text(c, "4 quadradinhos", 1450, 470, 44, "black", PURPLE, ep(t, C["08.c"] + 1.6, 0.5))
            expr(c, "2 · 2 = 4", 1450, 560, 60, ep(t, C["08.c"] + 1.6, 0.5), cores={4: PURPLE})
        return
    aa = ep(t, C["09.a"], 0.5)
    K.pizza(c, 470, 470, 180, 8, 0, ep(t, C["09"], 0.5))
    text(c, "diâmetro ×2", 470, 700, 30, "black", INK2, ep(t, C["09"], 0.5))
    if aa > 0:
        fmid(c, "=", 760, 470, 90, "black", PURPLE, aa)
        for k in range(4):
            r_, q = divmod(k, 2)
            ak = aa * ep(t, C["09.a"] + 0.25 * k, 0.4)
            K.pizza(c, 900 + q * 190, 375 + r_ * 190, 88, 6, 0, ak)
        text(c, "4 pizzas pequenas", 995, 700, 30, "black", PURPLE, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        boxed(c, 1240, 240, 450, 180, PURPLE, ab, 0.08)
        text(c, "QUADRÁTICA", 1465, 305, 34, "black", PURPLE, ab)
        text(c, "o lado vezes ele mesmo", 1465, 360, 26, "bold", INK2, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        K.atalho(c, 1240, 470, 450, 300, "ATALHO", ["lado ×2 → área ×4", "lado ×3 → área ×9"], acc, 34)


# ======================================================================
# bloco C — volume e aresta
# ======================================================================

def b_volume(c, t, C, B):
    frame(c, t, B["start"], "E COM UMA CAIXA?", "VOLUME E ARESTA", BLUE)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        boxed(c, 1080, 240, 600, 100, BLUE, aa, 0.08)
        text_mid(c, "VOLUME = quantos cubinhos enchem", 1380, 290, 30, "black", BLUE, aa)
    ab = ep(t, C["10.b"], 0.5)
    cubinho(c, 380, 330, 110, ab)
    if ab > 0:
        line(c, 380 + 95, 330 + 55 + 5, 380 + 95, 330 + 55 + 110, RED, ab, 6)
        text(c, "ARESTA", 560, 460, 30, "black", RED, ab, align="left")
        text(c, "cada lado do cubo", 560, 500, 24, "bold", INK2, ab, align="left")
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        vis = 8 * prog(t, C["10.c"] + 0.3, 2.4)
        cubo_n(c, 960, 380, 90, 2, acc, vis)
        expr(c, "2 · 2 · 2 = 8", 1380, 470, 64, ep(t, C["10.c"] + 2.0, 0.5), cores={6: PURPLE})
        text(c, "largura · altura · fundo", 1380, 560, 28, "bold", INK2, ep(t, C["10.c"] + 2.0, 0.5))
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1100, 620, 560, 170, "ATALHO", ["aresta ×2 → volume ×8"], ad, 36)


# ======================================================================
# bloco D — juros
# ======================================================================

SIMPLES = [100, 110, 120, 130, 140]
COMPOSTOS = [100, 110, 121, 133.1, 146.41]


def _barras(c, x0, y_base, vals, col, a, t, t0, escala=2.6, larg=80, gap=34):
    """barras do saldo mês a mês, entrando uma a uma a partir de t0"""
    for k, v in enumerate(vals):
        ak = a * ep(t, t0 + 0.25 * k, 0.4)
        h = (v - 60) * escala
        x = x0 + k * (larg + gap)
        rrect(c, x, y_base - h, larg, h, 10, col, ak)
        s = f"{v:.2f}".replace(".", ",") if v % 1 else f"{int(v)}"
        text(c, s, x + larg / 2, y_base - h - 16, 22, "black", INK, ak)
        text(c, f"{k}", x + larg / 2, y_base + 34, 22, "bold", GRAY, ak)



def b_juros(c, t, C, B):
    frame(c, t, B["start"], "E O DINHEIRO GUARDADO?", "JUROS SIMPLES × COMPOSTOS", BLUE)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        text(c, "SIMPLES", 450, 250, 34, "black", BLUE, aa)
        text(c, "sempre sobre os R$ 100 iniciais", 450, 290, 24, "bold", INK2, aa)
        _barras(c, 190, 700, SIMPLES, BLUE, aa, t, C["11.a"])
        text(c, "mês", 450, 780, 22, "bold", GRAY, aa)
        chip(c, "+10 todo mês", 450, 345, BLUE, aa, 26)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        line(c, 960, 230, 960, 800, "#E6E6E2", ab, 3)
        text(c, "COMPOSTOS", 1430, 250, 34, "black", PURPLE, ab)
        text(c, "juros sobre juros", 1430, 290, 24, "bold", INK2, ab)
        _barras(c, 1170, 700, COMPOSTOS, PURPLE, ab, t, C["11.b"])
        text(c, "mês", 1430, 780, 22, "bold", GRAY, ab)
    acc = ep(t, C["11.c"], 0.5)
    chip(c, "EXPONENCIAL: cada vez mais rápido", 1430, 345, PURPLE, acc, 24)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 860, ad, "REGRA DE TRÊS: SÓ NOS SIMPLES", GREEN, -2, 28)


# ======================================================================
# bloco E — tarifa por faixa
# ======================================================================

def b_faixa(c, t, C, B):
    frame(c, t, B["start"], "A CONTA DE ÁGUA", "TARIFA POR FAIXA", AMBER)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        boxed(c, 220, 230, 780, 100, BLUE, aa, 0.08)
        text_mid(c, "POR FAIXA: o preço muda com o consumo", 610, 280, 30, "black", BLUE, aa)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        # régua de consumo 0–20 m³ com as duas faixas
        x0, x1, y = 240, 1000, 450
        xm = (x0 + x1) / 2
        rrect(c, x0, y - 30, xm - x0, 60, 10, mix("#FFFFFF", GREEN, 0.4), ab)
        rrect(c, xm, y - 30, x1 - xm, 60, 10, mix("#FFFFFF", RED, 0.35), ab)
        text(c, "até 10 m³: R$ 3 cada", (x0 + xm) / 2, y + 10, 26, "black", INK, ab)
        text(c, "acima: R$ 6 cada", (xm + x1) / 2, y + 10, 26, "black", INK, ab)
        for v, x in ((0, x0), (10, xm), (20, x1)):
            text(c, f"{v}", x, y + 70, 24, "bold", GRAY, ab)
        text(c, "m³", x1 + 40, y + 70, 24, "bold", GRAY, ab)
        text(c, "(valores hipotéticos)", 610, 560, 22, "medium", GRAY, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        card(c, 1120, 240, 560, 170, acc)
        ftext(c, "10 m³ → R$ 30", 1400, 340, 48, "black", INK, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        card(c, 1120, 440, 560, 200, ad)
        ftext(c, "20 m³ → R$ 90", 1400, 525, 48, "black", RED, ad)
        ftext(c, "30 + 10 × 6", 1400, 590, 32, "black", INK2, ad)
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        text(c, "consumo ×2 → conta ×3", 1400, 720, 40, "black", AMBER, ae)
        text(c, "não existe UMA razão única", 610, 700, 34, "black", AMBER, ae)


# ======================================================================
# bloco F — tarefas indivisíveis
# ======================================================================

def _nota(c, x, y, a, col=PURPLE):
    c.drawOval(skia.Rect.MakeXYWH(x - 14, y - 10, 28, 20), paint(col, a))
    c.drawLine(x + 12, y, x + 12, y - 46, paint(col, a, stroke=5))
    c.drawLine(x + 12, y - 46, x + 30, y - 34, paint(col, a, stroke=5, cap_round=True))


def b_indivisivel(c, t, C, B):
    frame(c, t, B["start"], "TRABALHO QUE NÃO SE DIVIDE", "TAREFAS INDIVISÍVEIS", BLUE)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        for k in range(4):
            boneco(c, 260 + k * 90, 420, 110, BLUE, aa)
        _nota(c, 330, 300, aa); _nota(c, 470, 280, aa)
        crono(c, 700, 400, 60, 1.0, aa, "5 min", BLUE)
        text(c, "4 músicos", 400, 560, 32, "black", INK, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        for k in range(8):
            boneco(c, 1000 + k * 80, 420, 100, PURPLE, ab)
        _nota(c, 1100, 300, ab); _nota(c, 1400, 280, ab)
        text(c, "8 músicos", 1280, 560, 32, "black", INK, ab)
        ftext(c, "2,5 min?", 1700, 420, 40, "black", RED, ab * (1 - ep(t, C["13.c"], 0.4)))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        ftext(c, "5 min ✓", 1700, 420, 40, "black", GREEN, acc)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        boxed(c, 360, 630, 1200, 130, BLUE, ad, 0.08)
        text(c, "TAREFA INDIVISÍVEL", W / 2, 685, 34, "black", BLUE, ad)
        text(c, "mais gente NÃO deixa mais rápido (como os 9 meses do bebê)", W / 2, 732, 26, "bold", INK2, ad)


# ======================================================================
# bloco G — os 3 hábitos
# ======================================================================

HABITOS = [("14", "1", "PLAUSIBILIDADE", "o resultado faz sentido?"),
           ("15", "2", "VALOR UNITÁRIO", "o preço de UMA unidade"),
           ("16", "3", "UNIDADES", "converta primeiro")]


def b_habitos(c, t, C, B):
    head_seq(c, t, C, [("14", "HÁBITO 1", "CONFIRA O SENTIDO", GREEN), ("15", "HÁBITO 2", "REDUZA A UM", GREEN),
                       ("16", "HÁBITO 3", "PADRONIZE AS UNIDADES", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16"])
    n = ["14", "15", "16"].index(sid)
    # trilho dos 3 hábitos
    for k, (s_, num, nome, sub) in enumerate(HABITOS):
        a = ep(t, C[s_], 0.4) if k <= n else 0
        col = GREEN if k == n else GRAY
        x = 380 + k * 580
        badge_num(c, k + 1, x - 130, 250, a, 26, bg=col)
        text(c, nome, x - 95, 262, 28, "black", col, a, align="left")
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        if aa > 0:
            boxed(c, 300, 320, 1320, 90, BLUE, aa, 0.08)
            text_mid(c, "PLAUSIBILIDADE = o resultado faz sentido?", W / 2, 365, 32, "black", BLUE, aa)
        for j, (cue, s1, s2) in enumerate((("14.b", "mais operários", "MAIS dias?"), ("14.c", "mais velocidade", "MAIS tempo?"))):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            x = 560 + j * 800
            card(c, x - 330, 440, 660, 230, a)
            text(c, s1, x, 530, 36, "black", INK, a)
            arrow(c, x - 40, 560, x + 40, 560, GRAY, a, 4, 12)
            text(c, s2, x, 625, 40, "black", RED, a)
            selo(c, x, 745, a, "INVERTEU!", RED, -4, 26)
        return
    if sid == "15":
        for j, (cue, peso, preco, uni, rc, col) in enumerate((("15.a", "500 g", "R$ 8", "R$ 16/kg", "15.c", RED),
                                                                ("15.b", "1 kg", "R$ 14", "R$ 14/kg", "15.d", GREEN))):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            x = 450 + j * 520
            rrect(c, x - 110, 340, 220, 260, 20, mix("#FFFFFF", AMBER, 0.25 + 0.15 * j), a, shadow=True)
            text(c, "CAFÉ", x, 410, 30, "black", INK, a)
            text(c, peso, x, 480, 44, "black", INK, a)
            ftext(c, preco, x, 560, 40, "black", INK2, a)
            ra = ep(t, C[rc], 0.5)
            ftext(c, uni, x, 670, 40, "black", col, ra)
        ae = ep(t, C["15.e"], 0.5)
        if ae > 0:
            K.atalho(c, 1230, 340, 460, 300, "ATALHO", ["preço ÷ quantidade", "= preço de UMA", "unidade"], ae, 30)
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        ftext(c, "1 h 30 min", 520, 440, 64, "black", INK, aa)
        ftext(c, "≠ 1,30 h", 520, 540, 56, "black", RED, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        ftext(c, "= 90 min", 1000, 440, 64, "black", GREEN, ab, align="left")
        text(c, "60 + 30", 1100, 520, 30, "bold", INK2, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        boxed(c, 300, 610, 760, 150, AMBER, acc, 0.10)
        text(c, "unidades misturadas:", 680, 670, 30, "black", INK, acc)
        text(c, "a conta fecha… e sai ERRADA", 680, 718, 30, "black", AMBER, acc)
    ad = ep(t, C["16.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1140, 600, 520, 180, "ATALHO", ["converta primeiro, monte depois"], ad, 30)


# ======================================================================
# nós fazemos
# ======================================================================

EXERC = [("17.a", "18.a", "receita: 4 → 8 pessoas", "DÁ", "ingredientes ×2"),
         ("17.b", "18.b", "lado do terreno dobrou: e a área?", "NÃO DÁ", "área ×4"),
         ("17.c", "18.c", "conta de água por faixa", "NÃO DÁ", "o preço muda"),
         ("17.d", "18.d", "carro a velocidade constante", "DÁ", "tempo ×2, distância ×2")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "DÁ REGRA DE TRÊS?", GREEN), ("18", "VAMOS CONFERIR", "COM A PERGUNTA DE OURO", GREEN)])
    card(c, *CARD_R)
    for k, (cue, rc, s, resp, why) in enumerate(EXERC):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 135 + d
        badge_num(c, k + 1, 240, y - 6, a, 26, bg=BLUE)
        text(c, s, 290, y + 6, 36, "black", INK, a, align="left")
        if t >= C["18"]:
            ra = ep(t, C[rc], 0.5)
            ok = resp == "DÁ"
            pill(c, resp, 1250, y - 20, GREEN if ok else RED, size=30, a=ra, bounds=(0, 1920))
            text(c, why, 1450, y + 6, 26, "bold", INK2, ra, align="left")
    if t < C["18"]:
        pause_timer(c, t, C["17.end"] - 1.9, 1500, 420)
    else:
        selo_ouro(c, W / 2, 790, ep(t, C["18"], 0.5), 26)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Dobrar a causa dobra mesmo o efeito? Se não, nada de regra de três.", "Área vai ao quadrado; volume, ao cubo.",
          "Resultado estranho? Confira o sentido."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 48, "black", INK, a, 1340, 58)


ERROS = [("Dobrar gatos e ratos… e dobrar o tempo", "mais ratos parecem dar mais trabalho",
          "os gatos também dobraram: cada um com um rato, no mesmo tempo"),
         ("Regra de três na ÁREA a partir do lado", "o terreno ficou maior, então a área cresceria igual",
          "área vai ao quadrado: lado ×2 → área ×4"),
         ("Regra de três em JUROS COMPOSTOS", "mais tempo dá mais juros",
          "os juros crescem sobre os juros: regra de três só nos simples"),
         ("Não conferir se o resultado faz sentido", "a conta fechou sem erro",
          "uma conta perfeita pode resolver o problema trocado: confira o sentido")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22", "23"], ERROS)


# ======================================================================
# Questão 8 do material
# ======================================================================

ALTS8 = [("A", "1 minuto", "inversa só com os gatos", RED), ("B", "2 minutos", "", GREEN),
         ("C", "4 minutos", "direta só com os ratos", RED), ("D", "8 minutos", "dobrou o tempo duas vezes", RED),
         ("E", "16 minutos", "4 gatos × 4 ratos", RED)]


def _enunciado(c, linhas, a, y0=250, size=34, w=640):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · A PROVA OFICIAL DO GANCHO", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    _enunciado(c, [("Dois gatos caçam dois ratos em dois minutos.", INK),
                   ("Mantido esse mesmo ritmo de caça, quatro gatos caçarão quatro ratos em", BLUE)], a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    if t >= C["24.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS8, 980, 200, 700, 40, C["25.ok"], "B", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["24.end"] - 1.9, 470, 640)
    if t >= C["25"]:
        ra = ep(t, C["25"], 0.4)
        rrect(c, 170, 470, 720, 330, 18, "#FFFFFF", ra, shadow=True)
        selo_ouro(c, 530, 510, ra, 22)
        text(c, "dobrar os gatos dobra o tempo? NÃO", 530, 575, 26, "black", INK, ra)
        aa = ep(t, C["25.a"], 0.4)
        for k in range(4):
            x = 280 + k * 165
            gato(c, x, 650, 70, aa)
            rato(c, x + 6, 712, 36, aa)
            crono(c, x + 60, 640, 22, prog(t, C["25.b"], 1.2) if t >= C["25.b"] else 0, aa, "")
        ftext(c, "cada um: 2 min", 530, 785, 28, "black", GREEN, ep(t, C["25.b"], 0.4))
    am = ep(t, C["26.m"], 0.5) if t >= C["26"] else 0
    if am > 0:
        selo(c, 1330, 805, am, "A e C: AS DUAS REGRAS DE TRÊS", AMBER, -2, 22)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    itens = [("28.b", "juntamos tudo", BLUE), ("28.c", "caçamos as pegadinhas", AMBER), ("28.d", "questões novas", GREEN)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        x = 400 + k * 560
        card(c, x - 240, 320 + d, 480, 260, a)
        badge_num(c, k + 1, x, 390 + d, a, 34, bg=col)
        text(c, s, x, 500 + d, 38, "black", INK, a)
    pill(c, "ep. 6 · revisão e treino para o ENEM", W / 2, 720, PURPLE, size=32, a=ep(t, C["28.a"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"], "Você tinha respondido 4 minutos para os gatos?",
        canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, cotidiano=b_cotidiano, ouro=b_ouro, gatos=b_gatos,
              area=b_area, volume=b_volume, juros=b_juros, faixa=b_faixa, indivisivel=b_indivisivel, habitos=b_habitos,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q8=b_q8, ponte=b_ponte, cta=b_cta)
