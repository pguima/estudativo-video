"""Visual — Potenciação e Radiciação, Episódio 5: Simplificar radicais e fazer contas com raízes (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (tipografia de potências/raízes no expr, atalho, selo_teste...).
Peças deste episódio: casa() = a "casinha" da raiz com a porta (os fatores saem em dupla/trio), maca()/laranja() = as frutas.
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
_s = importlib.util.spec_from_file_location("comum019", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, WT = K.fmid, K.ftext, K.WT

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_potenciacao_ep5_simplificar_radicais.mp4"
CARD_R = K.CARD_R
MACA, MACA_E = "#E5484D", "#B8323A"
LARANJA, LARANJA_E = "#F59E2B", "#D27A10"
FOLHA = "#3BA55C"
CASA = "#F4F1FA"


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# peças: ficha, casa da raiz, frutas
# ======================================================================

def ficha(c, cx, cy, s, rot, col, a, size=None):
    if a <= 0:
        return
    rrect(c, cx - s / 2, cy - s / 2, s, s, 16, mix("#FFFFFF", col, 0.16), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), 16, 16), paint(col, a, stroke=4))
    text_mid(c, rot, cx, cy, size or s * 0.56, "black", col, a)


def casa(c, x, y, w, h, a, indice=None, porta_a=0.0):
    """o sinal de raiz gigante: a 'casinha'. O traço da esquerda é a PORTA por onde os fatores saem."""
    if a <= 0:
        return
    rrect(c, x + 178, y + 16, w - 178, h - 16, 18, CASA, a)
    p = skia.Path()
    p.moveTo(x, y + h * 0.60); p.lineTo(x + 40, y + h * 0.48); p.lineTo(x + 96, y + h); p.lineTo(x + 172, y); p.lineTo(x + w, y)
    c.drawPath(p, paint(PURPLE, a, stroke=10, cap_round=True))
    if indice:
        text_mid(c, indice, x + 46, y + h * 0.26, 60, "black", PURPLE, a)
    if porta_a > 0:
        pill(c, "PORTA", x + 100, y + h + 36, PURPLE, size=24, a=a * porta_a, anchor="center", bounds=(0, 1920))


def porta_anim(c, t, x, y, w, h, fatores, grupos, a, size=100, gap=28, sobra=None, sobra_t=1e9):
    """fatores dentro da casa; grupos = [(índices, instante)] → no instante o grupo acende e UM fator sai pela porta."""
    cy = y + h * 0.56
    xin = [x + 220 + i * (size + gap) + size / 2 for i in range(len(fatores))]
    G = len(grupos)
    slots = [x - 70 - (G - k) * (size + 46) + size / 2 for k in range(G)]
    grupo_de = {}
    for g, (idx, ts) in enumerate(grupos):
        for i in idx:
            grupo_de[i] = (g, idx, ts)
    # moldura de cada grupo (antes de sair)
    for g, (idx, ts) in enumerate(grupos):
        hl, mv = ep(t, ts, 0.4), ep(t, ts + 0.9, 0.9)
        al = a * hl * (1 - mv)
        if al > 0:
            x0, x1 = xin[idx[0]] - size / 2 - 12, xin[idx[-1]] + size / 2 + 12
            boxed(c, x0, cy - size / 2 - 12, x1 - x0, size + 24, GREEN, al, 0.10, r=20)
            text(c, "DUPLA" if len(idx) == 2 else "TRIO", (x0 + x1) / 2, cy - size / 2 - 26, 26, "black", GREEN, al)
    for i, f_ in enumerate(fatores):
        if i in grupo_de:
            g, idx, ts = grupo_de[i]
            hl, mv = ep(t, ts, 0.4), ep(t, ts + 0.9, 0.9)
            col = mix(BLUE, GREEN, hl)
            if i == idx[0]:
                xx = lerp(xin[i], slots[g], mv)
                yy = cy - math.sin(math.pi * mv) * 120
                ficha(c, xx, yy, size, f_, col, a)
            else:
                xx = lerp(xin[i], xin[idx[0]], ep(t, ts + 0.5, 0.4))
                ficha(c, xx, cy, size, f_, col, a * (1 - ep(t, ts + 0.6, 0.4)))
        else:
            sa = ep(t, sobra_t, 0.4)
            ficha(c, xin[i], cy, size, f_, mix(BLUE, AMBER, sa), a)
            if sa > 0 and sobra:
                text(c, sobra, xin[i], cy + size / 2 + 44, 26, "black", AMBER, a * sa)
    # o "·" entre os que saíram
    for k in range(G - 1):
        aa = a * ep(t, grupos[k + 1][1] + 1.8, 0.3)
        fmid(c, "·", (slots[k] + slots[k + 1]) / 2, cy, 60, "black", INK, aa)
    return slots, cy


def maca(c, cx, cy, r, a, rot=None, rsize=None):
    if a <= 0:
        return
    c.drawCircle(cx - r * 0.28, cy, r * 0.78, paint(MACA, a))
    c.drawCircle(cx + r * 0.28, cy, r * 0.78, paint(MACA, a))
    c.drawCircle(cx, cy + r * 0.12, r * 0.86, paint(MACA, a))
    c.drawCircle(cx - r * 0.38, cy - r * 0.3, r * 0.18, paint("#FFFFFF", a * 0.45))
    line(c, cx, cy - r * 0.62, cx + r * 0.08, cy - r * 1.0, "#7A4B2A", a, max(3, r * 0.1))
    o = skia.Path(); o.addOval(skia.Rect.MakeXYWH(cx + r * 0.08, cy - r * 1.06, r * 0.5, r * 0.24))
    c.drawPath(o, paint(FOLHA, a))
    if rot:
        expr(c, rot, cx, cy + r * 0.08, rsize or r * 0.62, a, cores={0: "#FFFFFF"})


def laranja(c, cx, cy, r, a, rot=None, rsize=None):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r * 0.92, paint(LARANJA, a))
    for dx, dy in ((-0.4, -0.2), (0.3, 0.35), (0.45, -0.3), (-0.2, 0.45)):
        c.drawCircle(cx + dx * r, cy + dy * r, r * 0.05, paint(LARANJA_E, a * 0.7))
    c.drawCircle(cx - r * 0.35, cy - r * 0.35, r * 0.16, paint("#FFFFFF", a * 0.45))
    o = skia.Path(); o.addOval(skia.Rect.MakeXYWH(cx - r * 0.05, cy - r * 1.08, r * 0.46, r * 0.22))
    c.drawPath(o, paint(FOLHA, a))
    if rot:
        expr(c, rot, cx, cy + r * 0.04, rsize or r * 0.62, a, cores={0: "#FFFFFF"})


def frutas(c, fn, n, x, cy, r, a, t=None, t0=None, passo=0.18, rot=None, rsize=None):
    """n frutas lado a lado a partir de x; se t0, entram uma a uma"""
    for i in range(n):
        ai = a if t0 is None else a * ep(t, t0 + i * passo, 0.3)
        fn(c, x + i * r * 2.1, cy, r, ai, rot, rsize)
    return n * r * 2.1


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "CADÊ A MINHA RESPOSTA?", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    text(c, "SUA RESPOSTA", 520, 290, 28, "black", GRAY, aa)
    expr(c, "√{50}", 520, 440, 150, aa, cores={0: BLUE})
    ab = ep(t, C["01.b"], 0.5)
    alts = ["2√{5}", "5√{2}", "10√{5}", "25√{2}", "50"]
    ad = ep(t, C["01.d"], 0.5)
    for k, s in enumerate(alts):
        a = ab * ep(t, C["01.b"] + 0.15 * k, 0.3)
        y = 250 + k * 105
        if k == 1 and ad > 0:
            rrect(c, 1040, y - 44, 560, 88, 14, GREEN, 0.15 * ad)
        badge_num(c, "ABCDE"[k], 1090, y, a, 22, bg=GREEN if (k == 1 and ad > 0.5) else INK)
        expr(c, s, 1150, y, 54, a, align="left")
    acc = ep(t, C["01.c"], 0.5)
    if ab > 0:
        selo(c, 520, 620, ab * (1 - acc), "NÃO ESTÁ LÁ?", RED, -4, 40)
    if ad > 0:
        arrow(c, 700, 440, 1030, 355, GREEN, ad, 6, 18, progress=ad)
        text(c, "o MESMO número", 850, 330, 30, "black", GREEN, ad)
        expr(c, "√{50} = 5√{2}", 520, 640, 72, ad, cores={2: GREEN})
    pill(c, "hoje: SIMPLIFICAR RAÍZES", W / 2, 790, PURPLE, size=32, a=ep(t, C["01.e"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "SIMPLIFICAR qualquer raiz", "√50 = 5√2"), ("02.b", "quando dá (e quando NÃO dá) para somar", "maçã com maçã")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 52, "black", INK, a, align="left")
        text(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")
    maca(c, 1550, 470, 70, ep(t, C["02.b"] + 1.0, 0.4), "√{2}", 50)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    cols = [(460, "03.a", "FATORAR EM PRIMOS", "série de divisibilidade"), (960, "03.b", "QUADRADO PERFEITO", "um número ao quadrado"),
            (1460, "03.c", "RAIZ DE UM PRODUTO", "episódio 4")]
    for cx, cue, tit, sub in cols:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        card(c, cx - 230, 230, 460, 560, a)
        text(c, tit, cx, 290, 28, "black", BLUE, a)
        text(c, sub, cx, 330, 22, "bold", GRAY, a)
    a = ep(t, C["03.a"], 0.5)
    expr(c, "12 = 2 · 2 · 3", 460, 470, 52, a, cores={2: PURPLE, 4: PURPLE, 6: PURPLE})
    text(c, "só sobram primos", 460, 560, 26, "black", INK2, a)
    a = ep(t, C["03.b"], 0.5)
    for k, (n, b) in enumerate((("4", "2²"), ("9", "3²"), ("16", "4²"), ("25", "5²"), ("36", "6²"))):
        ak = a * ep(t, C["03.b"] + 2.6 + 0.35 * k, 0.3)
        y = 400 + k * 72
        text_mid(c, n, 900, y, 44, "black", INK, ak)
        text_mid(c, "= " + b, 1020, y, 36, "black", PURPLE, ak)
    a = ep(t, C["03.c"], 0.5)
    expr(c, "√{a·b} = √{a} · √{b}", 1460, 480, 46, a, cores=mono("√{a·b} = √{a} · √{b}", PURPLE))
    expr(c, "√{4·9} = 2 · 3", 1460, 600, 40, a, cores={2: GREEN, 4: GREEN})


# ======================================================================
# bloco A — método 1: o maior quadrado perfeito
# ======================================================================

def b_simplificar(c, t, C, B):
    frame(c, t, B["start"], "O QUE É SIMPLIFICAR?", "TIRAR DA RAIZ O QUE SAI", BLUE)
    aa = ep(t, C["04.a"], 0.5)
    pill(c, "SIMPLIFICAR = tirar de dentro da raiz tudo o que consegue sair", W / 2, 250, BLUE, size=30, a=aa,
         anchor="center", bounds=(0, 1920))
    acc = ep(t, C["04.c"], 0.5)
    expr(c, "√{50}", 640, 470, 150, ep(t, C["04"], 0.5), cores={0: INK})
    fmid(c, "=", W / 2, 470, 120, "black", GREEN, acc)
    expr(c, "5√{2}", 1280, 470, 150, acc, cores={0: GREEN})
    ab = ep(t, C["04.b"], 0.5)
    chip(c, "o VALOR não muda", 640, 660, PURPLE, ab, 32)
    chip(c, "só fica MAIS SIMPLES", 1280, 660, GREEN, acc, 32)
    text(c, "o mesmo número, dois jeitos de escrever", W / 2, 770, 30, "black", INK2, acc)


def b_metodo1(c, t, C, B):
    head_seq(c, t, C, [("05", "MÉTODO 1", "O QUADRADO PERFEITO QUE DIVIDE", PURPLE), ("06", "O NÚMERO DA FRENTE", "COEFICIENTE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        expr(c, "√{50}", 400, 470, 130, ep(t, C["05"], 0.5))
        chip(c, "quadrado perfeito que divide 50?", 1150, 250, AMBER, ep(t, C["05.a"], 0.5), 30)
        ab = ep(t, C["05.b"], 0.5)
        expr(c, "50 = 25 · 2", 1150, 350, 60, ab, cores={2: GREEN})
        acc = ep(t, C["05.c"], 0.5)
        expr(c, "√{50} = √{25} · √{2}", 1150, 480, 62, acc, cores={2: GREEN})
        ad = ep(t, C["05.d"], 0.5)
        expr(c, "√{25} = 5", 1150, 600, 54, ad, cores={2: GREEN})
        ae = ep(t, C["05.e"], 0.5)
        if ae > 0:
            boxed(c, 860, 660, 580, 130, GREEN, ae, 0.10)
            expr(c, "√{50} = 5√{2}", 1150, 725, 70, ae, cores={2: GREEN})
        return
    a0 = ep(t, C["06"], 0.5)
    expr(c, "5√{2}", 760, 460, 200, a0, cores={0: INK})
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 595, 370, 120, 180, 20, BLUE, 0.12 * aa)
        arrow(c, 470, 260, 610, 380, BLUE, aa, 5, 16, progress=aa)
        text(c, "COEFICIENTE", 420, 230, 34, "black", BLUE, aa)
        text(c, "o número de fora, multiplicando a raiz", 1350, 380, 30, "black", INK2, aa)
    ab = ep(t, C["06.b"], 0.5)
    expr(c, "5√{2} = 5 · √{2}", 1350, 520, 72, ab, cores={2: INK, 3: AMBER})
    chip(c, "o “vezes” fica escondido", 1350, 640, AMBER, ep(t, C["06.b"] + 1.6, 0.4), 30)


QUADS = ["100", "81", "64", "49", "36", "25", "16", "9", "4"]


def b_maior(c, t, C, B):
    head_seq(c, t, C, [("07", "E RAIZ DE 72?", "USE O MAIOR QUADRADO", PURPLE), ("08", "ATALHO", "DESÇA A LISTA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        expr(c, "√{72}", 400, 470, 130, ep(t, C["07"], 0.5))
        for k, (n, pal) in enumerate((("4", "quatro"), ("9", "nove"), ("36", "trinta"))):
            a = ep(t, WT(C, "07", pal, depois=C["07.a"]), 0.4)
            x = 900 + k * 220
            col = GREEN if n == "36" else INK2
            rrect(c, x - 80, 230, 160, 90, 18, mix("#FFFFFF", col, 0.12), a)
            text_mid(c, n, x, 275, 50, "black", col, a)
            text(c, "divide ✓", x, 360, 22, "black", col, a)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            text(c, "use sempre o MAIOR", 1120, 420, 32, "black", GREEN, ab)
        expr(c, "72 = 36 · 2", 1120, 495, 58, ab, cores={2: GREEN})
        acc = ep(t, C["07.c"], 0.5)
        expr(c, "√{36} = 6", 1120, 590, 52, acc, cores={2: GREEN})
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            boxed(c, 830, 655, 580, 125, GREEN, ad, 0.10)
            expr(c, "√{72} = 6√{2}", 1120, 718, 66, ad, cores={2: GREEN})
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        K.atalho(c, 900, 220, 800, 190, "ATALHO", ["desça a lista dos quadrados perfeitos:", "o 1º que DIVIDE é o MAIOR"], aa, 34)
    ab = ep(t, C["08.b"], 0.5)
    ad = ep(t, C["08.d"], 0.5)
    pals = ["cem", "oitenta", "sessenta", "quarenta", "trinta"]
    for k, n in enumerate(QUADS):
        a = ab * ep(t, C["08.b"] + 0.25 * k, 0.3)
        y = 225 + k * 66
        teste = ad > 0 and k < 5
        tk = WT(C, "08", pals[k], depois=C["08.d"]) if k < 5 else 1e9
        ok = ep(t, tk, 0.3) if teste else 0
        col = INK
        if ok > 0:
            col = GREEN if n == "36" else RED
        text_mid(c, n, 330, y, 44, "black", mix(INK, col, ok), a)
        text_mid(c, "= " + ["10²", "9²", "8²", "7²", "6²", "5²", "4²", "3²", "2²"][k], 450, y, 30, "black", PURPLE, a * 0.8)
        if ok > 0:
            if n == "36":
                check_icon(c, 560, y, 22, ok, GREEN)
            else:
                check_icon(c, 560, y, 22, ok, RED, "x")
    if ad > 0:
        text(c, "para 180:", 760, 470, 30, "black", GRAY, ad, align="left")
        text(c, "180 ÷ 36 = 5  ✓", 760, 530, 40, "black", GREEN, ep(t, WT(C, "08", "trinta", depois=C["08.d"]), 0.4),
             align="left")
    ae = ep(t, C["08.e"], 0.5)
    if ae > 0:
        boxed(c, 900, 620, 800, 140, GREEN, ae, 0.10)
        expr(c, "√{180} = √{36·5} = 6√{5}", 1300, 690, 62, ae, cores={4: GREEN})


def b_confere(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "CONFIRA ELEVANDO AO QUADRADO", GREEN)
    a0 = ep(t, C["09"], 0.5)
    boxed(c, 260, 210, 1400, 580, GREEN, a0, 0.06)
    text(c, "ATALHO", W / 2, 260, 24, "black", GREEN, a0, tracking=2)
    text(c, "eleve ao quadrado: tem de voltar o número de dentro", W / 2, 320, 40, "black", INK, a0)
    aa = ep(t, C["09.a"], 0.5)
    expr(c, "(5√{2})^2 = 5^2 · (√{2})^2", W / 2, 440, 72, aa)
    ab = ep(t, C["09.b"], 0.5)
    chip(c, "o expoente de fora pega OS DOIS fatores (ep. 2)", W / 2, 540, PURPLE, ab, 28)
    acc = ep(t, C["09.c"], 0.5)
    expr(c, "= 25 · 2", 760, 640, 64, acc, cores={1: INK, 3: INK})
    text(c, "o quadrado desfaz a raiz", 760, 710, 24, "black", INK2, acc)
    ad = ep(t, C["09.d"], 0.5)
    expr(c, "= 50", 1180, 640, 72, ad, cores={1: GREEN})
    check_icon(c, 1330, 630, 30, ad, GREEN)


# ======================================================================
# bloco B — método 2: a porta da raiz
# ======================================================================

ESCADA = [("180", "2", "10.b"), ("90", "2", "noventa"), ("45", "3", "quarenta"), ("15", "3", "quinze"), ("5", "", "cinco")]


def b_porta(c, t, C, B):
    head_seq(c, t, C, [("10", "MÉTODO 2", "FATORE EM PRIMOS", PURPLE), ("11", "A PORTA DA RAIZ", "SÓ SAI QUEM ESTÁ EM DUPLA", PURPLE),
                       ("12", "QUEM SAIU, MULTIPLICA", "QUEM SOBROU, FICA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11", "12"])
    if sid == "10":
        chip(c, "o quadrado perfeito não salta aos olhos?", W / 2, 230, AMBER, ep(t, C["10"], 0.5), 30)
        a0 = ep(t, C["10.a"], 0.5)
        line(c, 600, 290, 600, 700, INK2, a0, 4)
        tq = WT(C, "10", "quinze", depois=C["10.b"])
        for k, (n, p_, pal) in enumerate(ESCADA):
            if k == 0:
                tk = C["10.a"]
            elif pal == "cinco":
                tk = WT(C, "10", "cinco", depois=tq)
            else:
                tk = WT(C, "10", pal, depois=C["10.b"])
            a = ep(t, tk, 0.4)
            y = 330 + k * 85
            text(c, n, 570, y + 18, 54, "black", INK, a, align="right")
            if p_:
                ap = ep(t, C["10.b"] if k == 0 else tk + 0.6, 0.4)
                text(c, p_, 630, y + 18, 54, "black", PURPLE, ap, align="left")
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            card(c, 900, 380, 760, 200, acc)
            expr(c, "180 = 2 · 2 · 3 · 3 · 5", 1280, 480, 62, acc, cores={2: PURPLE, 4: PURPLE, 6: PURPLE, 8: PURPLE, 10: PURPLE})
            text(c, "tudo multiplicado", 1280, 620, 28, "black", INK2, acc)
        return
    x, y, w, h = 720, 300, 960, 250
    a0 = ep(t, C["11.a"], 0.5)
    casa(c, x, y, w, h, ep(t, C["11"], 0.5), porta_a=ep(t, C["11.b"], 0.4))
    pill(c, "só sai quem está em DUPLA · cada dupla sai como UM só", W / 2, 230, PURPLE, size=28, a=ep(t, C["11.b"], 0.5),
         anchor="center", bounds=(0, 1920))
    slots, cy = porta_anim(c, t, x, y, w, h, ["2", "2", "3", "3", "5"], [((0, 1), C["11.c"]), ((2, 3), C["11.d"])], a0,
                           sobra="sozinho: fica", sobra_t=C["11.e"])
    if sid == "11":
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        text(c, "2 · 3 = 6", (slots[0] + slots[1]) / 2, cy + 120, 40, "black", GREEN, aa)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        boxed(c, 300, 690, 560, 120, GREEN, acc, 0.10)
        expr(c, "√{180} = 6√{5}", 580, 750, 64, acc, cores={2: GREEN})
        text(c, "igual ao método 1", 580, 830, 22, "black", GREEN, acc)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        card(c, 960, 680, 720, 140, ad)
        expr(c, "√{2·2} = √{4} = 2", 1320, 730, 46, ad, cores={4: GREEN})
        text(c, "cada dupla é um quadrado perfeito escondido", 1320, 800, 24, "black", INK2, ad)


def b_porta72(c, t, C, B):
    frame(c, t, B["start"], "CONFERINDO COM O 72", "PELA PORTA", PURPLE)
    x, y, w, h = 720, 300, 960, 250
    a0 = ep(t, C["13.a"], 0.5)
    casa(c, x, y, w, h, ep(t, C["13"], 0.5), porta_a=1.0)
    expr(c, "72 = 2 · 2 · 2 · 3 · 3", W / 2, 230, 44, a0, cores={2: PURPLE, 4: PURPLE, 6: PURPLE, 8: PURPLE, 10: PURPLE})
    slots, cy = porta_anim(c, t, x, y, w, h, ["2", "2", "2", "3", "3"], [((0, 1), C["13.b"]), ((3, 4), C["13.c"])], a0,
                           sobra="sozinho: fica", sobra_t=C["13.d"])
    ae = ep(t, C["13.e"], 0.5)
    if ae > 0:
        text(c, "2 · 3 = 6", (slots[0] + slots[1]) / 2, cy + 120, 40, "black", GREEN, ae)
        boxed(c, 660, 680, 600, 120, GREEN, ae, 0.10)
        expr(c, "√{72} = 6√{2}", W / 2, 740, 64, ae, cores={2: GREEN})
        chip(c, "bate com o método 1", 1500, 740, GREEN, ep(t, C["13.e"] + 2.0, 0.4), 28)


# ======================================================================
# bloco C — raiz cúbica: saem em trio
# ======================================================================

def b_cubica(c, t, C, B):
    head_seq(c, t, C, [("14", "E NA RAIZ CÚBICA?", "SÓ SAI QUEM ESTÁ EM TRIO", PURPLE), ("15", "PELO MÉTODO 1", "CUBO PERFEITO", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15"])
    if sid == "14":
        x, y, w, h = 760, 300, 860, 250
        casa(c, x, y, w, h, ep(t, C["14"], 0.5), indice="3", porta_a=1.0)
        pill(c, "na raiz CÚBICA: só sai em TRIO", W / 2, 230, PURPLE, size=30, a=ep(t, C["14.a"], 0.5), anchor="center",
             bounds=(0, 1920))
        ab = ep(t, C["14.b"], 0.5)
        if ab > 0:
            expr(c, "54 = 2 · 3 · 3 · 3", 450, 700, 44, ab, cores={2: PURPLE, 4: PURPLE, 6: PURPLE, 8: PURPLE})
        porta_anim(c, t, x, y, w, h, ["2", "3", "3", "3"], [((1, 2, 3), C["14.c"])], ab, sobra="fica", sobra_t=C["14.d"])
        ae = ep(t, C["14.e"], 0.5)
        if ae > 0:
            boxed(c, 1000, 660, 600, 130, GREEN, ae, 0.10)
            expr(c, "√[3]{54} = 3√[3]{2}", 1300, 725, 64, ae, cores={2: GREEN})
        return
    a0 = ep(t, C["15"], 0.5)
    text(c, "CUBO PERFEITO = um número ao cubo", 560, 250, 30, "black", BLUE, a0)
    for k, (n, b) in enumerate((("8", "2³"), ("27", "3³"), ("64", "4³"))):
        ak = a0 * ep(t, C["15"] + 2.5 + 0.4 * k, 0.3)
        rrect(c, 300 + k * 180, 300, 150, 120, 18, mix("#FFFFFF", BLUE, 0.10), ak)
        text_mid(c, n, 375 + k * 180, 345, 50, "black", INK, ak)
        text_mid(c, "= " + b, 375 + k * 180, 395, 28, "black", PURPLE, ak)
    aa = ep(t, C["15.a"], 0.5)
    expr(c, "√[3]{54} = √[3]{27} · √[3]{2} = 3√[3]{2}", 1240, 360, 52, aa, cores={6: GREEN})
    text(c, "porque 3³ = 27", 1240, 450, 26, "black", INK2, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        K.atalho(c, 300, 520, 1320, 260, "ATALHO DA PORTA", ["raiz QUADRADA: sai em DUPLA", "raiz CÚBICA: sai em TRIO",
                                                              "quem sobra, fica dentro"], ab, 36)


# ======================================================================
# bloco D/E/F — somar só radicais semelhantes
# ======================================================================

def b_frutas(c, t, C, B):
    frame(c, t, B["start"], "SOMAR RAÍZES", "COMEÇA PELA FEIRA", BLUE)
    aa = ep(t, C["16.a"], 0.5)
    y1, y2 = 330, 590
    if aa > 0:
        frutas(c, maca, 2, 260, y1, 40, aa, t, C["16.a"])
        fmid(c, "+", 480, y1, 70, "black", INK, aa)
        frutas(c, maca, 5, 560, y1, 40, aa, t, C["16.a"] + 0.8)
        fmid(c, "=", 1030, y1, 70, "black", INK, aa)
        aa2 = ep(t, C["16.a"] + 2.0, 0.4)
        text(c, "7 maçãs", 1110, y1 + 18, 54, "black", GREEN, aa2, align="left")
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        frutas(c, maca, 2, 260, y2, 40, ab, t, C["16.b"])
        fmid(c, "+", 480, y2, 70, "black", INK, ab)
        frutas(c, laranja, 3, 560, y2, 40, ab, t, C["16.b"] + 0.6)
        fmid(c, "=", 1030, y2, 70, "black", INK, ab)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        text(c, "5 “maranjas”?", 1110, y2 + 18, 54, "black", RED, acc, align="left")
        strike(c, 1100, y2, 1460, y2, acc, RED, acc)
        text(c, "continuam 2 maçãs e 3 laranjas", 1110, y2 + 80, 26, "black", INK2, acc, align="left")
    pill(c, "só dá para juntar o que é IGUAL", W / 2, 790, GREEN, size=32, a=ep(t, C["16.d"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_semelhantes(c, t, C, B):
    frame(c, t, B["start"], "COM RAIZ É IGUALZINHO", "A RAIZ É A FRUTA", PURPLE)
    aa = ep(t, C["17.a"], 0.5)
    expr(c, "2√{3} + 5√{3}", 640, 280, 80, aa, cores={0: GREEN, 2: GREEN})
    if aa > 0:
        frutas(c, maca, 2, 260, 440, 44, aa, t, C["17.a"] + 1.0, rot="√{3}", rsize=30)
        fmid(c, "+", 520, 440, 64, "black", INK, aa)
        frutas(c, maca, 5, 600, 440, 44, aa, t, C["17.a"] + 1.8, rot="√{3}", rsize=30)
    ab = ep(t, C["17.b"], 0.5)
    expr(c, "= 7√{3}", 1440, 280, 90, ab, cores={1: GREEN})
    text(c, "2 + 5 = 7 frutas", 1440, 400, 30, "black", INK2, ab)
    acc = ep(t, C["17.c"], 0.5)
    pill(c, "RADICAIS SEMELHANTES = mesmo índice E mesmo radicando", W / 2, 570, BLUE, size=30, a=acc, anchor="center",
         bounds=(0, 1920))
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        K.atalho(c, 360, 640, 1200, 150, "ATALHO", ["some só os COEFICIENTES (os da frente): a fruta fica igual"], ad, 32)


def b_naosoma(c, t, C, B):
    frame(c, t, B["start"], "E FRUTAS DIFERENTES?", "NÃO TEM O QUE SOMAR", AMBER)
    a0 = ep(t, C["18"], 0.5)
    expr(c, "√{2} + √{3}", 420, 270, 70, a0)
    maca(c, 330, 400, 50, a0, "√{2}", 34)
    fmid(c, "+", 420, 400, 56, "black", INK, a0)
    laranja(c, 510, 400, 50, a0, "√{3}", 34)
    ab = ep(t, C["18.b"], 0.5)
    chip(c, "já é a FORMA FINAL", 420, 520, BLUE, ab, 30)
    text(c, "forma final = o jeito mais simples", 420, 580, 24, "black", INK2, ab)
    line(c, 760, 220, 760, 800, "#E6E6E2", ep(t, C["18.c"], 0.5), 3)
    acc = ep(t, C["18.c"], 0.5)
    expr(c, "2√{3} + 3√{2} ≠ 5√{5}", 1260, 270, 64, acc, cores={4: RED})
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        card(c, 880, 350, 760, 260, ad)
        text(c, "teste com raízes exatas", 1260, 395, 24, "black", GRAY, ad)
        expr(c, "2√{9} + 3√{4} = 6 + 6 = 12", 1260, 470, 52, ad, cores={8: GREEN})
    ae = ep(t, C["18.e"], 0.5)
    if ae > 0:
        expr(c, "5√{13} > 5 · 3 = 15", 1260, 560, 48, ae, cores={0: RED, 6: RED})
        K.selo_teste(c, 1260, 700, ae, ok=False, s="TESTE: NÃO CONFERE")


def b_antes(c, t, C, B):
    frame(c, t, B["start"], "PARECEM DIFERENTES...", "SIMPLIFIQUE ANTES", AMBER)
    aa = ep(t, C["19.a"], 0.5)
    expr(c, "√{12} + √{27}", 480, 280, 76, aa)
    ab, acc, ad = ep(t, C["19.b"], 0.5), ep(t, C["19.c"], 0.5), ep(t, C["19.d"], 0.5)
    maca(c, 360, 420, 56, aa * (1 - ad), "√{12}", 30)
    laranja(c, 600, 420, 56, aa * (1 - ad), "√{27}", 30)
    maca(c, 360, 420, 56, ad, "√{3}", 36)
    maca(c, 600, 420, 56, ad, "√{3}", 36)
    fmid(c, "+", 480, 420, 56, "black", INK, aa)
    text(c, "parece que não dá...", 480, 540, 28, "black", AMBER, aa * (1 - ad))
    text(c, "a MESMA fruta!", 480, 540, 28, "black", GREEN, ad)
    expr(c, "√{12} = √{4·3} = 2√{3}", 1300, 280, 54, ab, cores={4: GREEN})
    expr(c, "√{27} = √{9·3} = 3√{3}", 1300, 400, 54, acc, cores={4: GREEN})
    if ad > 0:
        boxed(c, 960, 470, 680, 130, GREEN, ad, 0.10)
        expr(c, "2√{3} + 3√{3} = 5√{3}", 1300, 535, 58, ad, cores={4: GREEN})
    pill(c, "simplifique ANTES de dizer que não dá", W / 2, 720, AMBER, size=34, a=ep(t, C["19.e"], 0.5), anchor="center",
         bounds=(0, 1920))


# ======================================================================
# bloco G — multiplicar e dividir com o mesmo índice
# ======================================================================

def b_multiplicar(c, t, C, B):
    frame(c, t, B["start"], "E MULTIPLICAR?", "MESMO ÍNDICE: UMA RAIZ SÓ", PURPLE)
    aa = ep(t, C["20.a"], 0.5)
    expr(c, "√{3} · √{12} = √{3·12}", 640, 290, 60, aa, cores={4: PURPLE})
    ab = ep(t, C["20.b"], 0.5)
    expr(c, "= √{36} = 6", 640, 400, 60, ab, cores={3: GREEN})
    acc = ep(t, C["20.c"], 0.5)
    expr(c, "√{18}/√{2} = √{18/2} = √{9} = 3", 1320, 340, 54, acc, cores={6: GREEN})
    if aa > 0:
        K.atalho(c, 300, 500, 1320, 140, "ATALHO", ["mesmo índice: junte tudo numa raiz só e faça a conta dentro"], aa, 32)
    ad = ep(t, C["20.d"], 0.5)
    if ad > 0:
        expr(c, "√{2} · √[3]{2} = ?", 760, 740, 52, ad, cores={0: AMBER, 2: AMBER})
        chip(c, "índices diferentes: truque do episódio 6", 1340, 740, AMBER, ad, 28)


# ======================================================================
# exercício
# ======================================================================

def b_exercicio(c, t, C, B):
    sid = which(t, C, ["21", "22"])
    head(c, t, C[sid], "SUA VEZ" if sid == "21" else "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)
    card(c, *CARD_R)
    for k, (cue, s) in enumerate((("21.a", "√{48} = ?"), ("21.b", "√{75} = ?"))):
        a = ep(t, C[cue], 0.5)
        cx = 560 + k * 800
        if a <= 0:
            continue
        rrect(c, cx - 300, 220, 600, 160, 18, "#F6F6F3", a)
        text(c, f"{k + 1}ª CONTA", cx, 252, 18, "black", GRAY, a, tracking=1)
        expr(c, s, cx, 320, 70, a)
    pause_timer(c, t, C["21.p"], W / 2, 480)
    if sid == "21":
        return
    aa = ep(t, C["22.a"], 0.5)
    expr(c, "48 = 16 · 3", 560, 450, 44, aa, cores={2: GREEN})
    expr(c, "= 4√{3}", 560, 540, 70, aa, cores={1: GREEN})
    ab = ep(t, C["22.b"], 0.5)
    expr(c, "75 = 25 · 3", 1360, 450, 44, ab, cores={2: GREEN})
    expr(c, "= 5√{3}", 1360, 540, 70, ab, cores={1: GREEN})
    acc = ep(t, C["22.c"], 0.5)
    if acc > 0:
        expr(c, "4√{3} + 5√{3}", 820, 700, 64, acc)
        maca(c, 1160, 700, 44, acc, "√{3}", 28)
        text(c, "a mesma fruta", 1160, 790, 22, "black", GREEN, acc)
    ad = ep(t, C["22.d"], 0.5)
    expr(c, "= 9√{3}", 1400, 700, 76, ad, cores={1: GREEN})


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Da raiz quadrada, os fatores saem em dupla.", "Só se somam raízes iguais: mesmo índice e mesmo radicando.",
          "Simplifique antes de dizer que não dá."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["23", "33"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "23" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("√12 + √27 = √39  (somar os radicandos)", "na multiplicação dá para juntar numa raiz só",
          "na soma, não: simplifique e some as frutas → 5√3"),
         ("2√3 + 3√2 = 5√5", "somar fora com fora e dentro com dentro parece organizado",
          "frutas diferentes: a conta já está pronta"),
         ("√72 = 2√18  (parar no meio)", "o valor até está certo",
          "o 18 ainda tem uma dupla de 3 dentro: forma final 6√2")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["24", "25", "26"], ERROS)


# ======================================================================
# Questões 4 e 5 do material
# ======================================================================

ALTS4 = [("A", "= 3√{20}", "valor certo, NÃO simplificada", AMBER), ("B", "= 6√{5}", "", GREEN),
         ("C", "= 9√{2}", "9² · 2 = 162, não 180", RED), ("D", "= 2√{45}", "valor certo, NÃO simplificada", AMBER),
         ("E", "= 18√{10}", "tirou o 18 sem tirar a raiz", RED)]
ALTS5 = [("A", "= √{40}", "somou os radicandos", RED), ("B", "= 2√{2}", "esqueceu o √8", RED), ("C", "= 4√{2}", "", GREEN),
         ("D", "= 10√{2}", "ignorou o sinal de menos", RED), ("E", "= 4√{10}", "trocou a fruta", RED)]


def _questao_base(c, t, C, B, sid0, titulo, enun, alts, ok_cue, okL, cues_x):
    head(c, t, B["start"], titulo, "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C[f"{sid0}.a"], 0.4)
    text(c, enun[0], 190, 250, 36, "black", INK, a0, align="left")
    expr(c, enun[1], 190, 330, 56, a0, align="left")
    text(c, "é", 190 + K.math_w(enun[1], 56) + 20, 342, 36, "black", INK, a0, align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"{sid0}.q{L.lower()}"] for L in "ABCDE"}
    if t >= C[f"{sid0}.qa"] - 0.3:
        K.alternativas(c, t, C, alts, 960, 210, 720, 42, ok_cue, okL, cues_in, cues_x, gap=14)
    pause_timer(c, t, C[f"{sid0}.end"] - 1.9, 470, 600)


def b_q4(c, t, C, B):
    cues_x = {"A": C["29.xa"], "D": C["29.xd"], "C": C["29.xc"], "E": C["29.xe"]}
    _questao_base(c, t, C, B, "27", "QUESTÃO · SIMPLIFICAÇÃO DE RADICAL", ("A forma simplificada de", "√{180}"), ALTS4,
                  C["28.ok"], "B", cues_x)
    if t >= C["28"]:
        ra = ep(t, C["28"], 0.4)
        rrect(c, 170, 410, 740, 390, 18, "#FFFFFF", ra, shadow=True)
        aa = ep(t, C["28.a"], 0.4)
        text(c, "desça a lista dos quadrados perfeitos", 540, 460, 24, "black", GREEN, aa)
        text(c, "100 ✗   81 ✗   64 ✗   49 ✗   36 ✓", 540, 515, 30, "black", INK, aa)
        expr(c, "180 = 36 · 5", 540, 600, 48, ep(t, C["28.b"], 0.4), cores={2: GREEN})
        expr(c, "√{180} = √{36} · √{5} = 6√{5}", 540, 700, 44, ep(t, C["28.c"], 0.4), cores={6: GREEN})
    if t >= C["29"]:
        ax = ep(t, C["29.xa"], 0.4)
        if ax > 0:
            card(c, 170, 410, 740, 390, ax)
            text(c, "A e D: o valor está certo, mas...", 540, 460, 26, "black", AMBER, ax)
            expr(c, "3√{20} = 3 · 2√{5} = 6√{5}", 540, 545, 40, ax, cores={6: GREEN})
            expr(c, "2√{45} = 2 · 3√{5} = 6√{5}", 540, 625, 40, ep(t, C["29.xd"], 0.4), cores={6: GREEN})
            text(c, "ainda tinham uma dupla dentro", 540, 690, 24, "black", INK2, ax)
            axc = ep(t, C["29.xc"], 0.4)
            if axc > 0:
                expr(c, "(9√{2})^2 = 81 · 2 = 162", 540, 760, 36, axc, cores={6: RED})


def b_q5(c, t, C, B):
    cues_x = {"A": C["32.xa"], "B": C["32.xb"], "D": C["32.xd"], "E": C["32.xe"]}
    _questao_base(c, t, C, B, "30", "QUESTÃO · SOMA DE RADICAIS", ("O valor de", "√{50} + √{8} - √{18}"), ALTS5,
                  C["31.ok"], "C", cues_x)
    if t >= C["31"]:
        ra = ep(t, C["31"], 0.4)
        rrect(c, 170, 410, 740, 390, 18, "#FFFFFF", ra, shadow=True)
        text(c, "simplifique ANTES", 540, 455, 24, "black", AMBER, ra)
        for k, (cue, s) in enumerate((("31.a", "√{50} = √{25·2} = 5√{2}"), ("31.b", "√{8} = √{4·2} = 2√{2}"),
                                      ("31.c", "√{18} = √{9·2} = 3√{2}"))):
            expr(c, s, 540, 520 + k * 70, 38, ep(t, C[cue], 0.4), cores={4: GREEN})
        ad = ep(t, C["31.d"], 0.4)
        if ad > 0:
            expr(c, "5√{2} + 2√{2} - 3√{2} = 4√{2}", 540, 745, 36, ad, cores={6: GREEN})
            maca(c, 850, 745, 26, ad, None)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "DOIS TRUQUES", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    if aa > 0:
        card(c, 300, 250, 560, 330, aa)
        expr(c, "1/√{2}", 580, 390, 110, aa)
        text(c, "raiz no DENOMINADOR", 580, 540, 28, "black", AMBER, aa)
    chip(c, "a prova quer SEM raiz embaixo", 580, 650, GREEN, ep(t, C["34.b"], 0.5), 30)
    acc = ep(t, C["34.c"], 0.5)
    if acc > 0:
        card(c, 1060, 250, 560, 330, acc)
        expr(c, "√{2} · √[3]{2}", 1340, 390, 90, acc)
        text(c, "índices DIFERENTES", 1340, 540, 28, "black", AMBER, acc)
    pill(c, "ep. 6 · racionalização e expoente fracionário", W / 2, 770, PURPLE, size=32, a=ep(t, C["34.d"], 0.5),
         anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Quanto deu √48 + √75 para você?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, simplificar=b_simplificar, metodo1=b_metodo1, maior=b_maior,
              confere=b_confere, porta=b_porta, porta72=b_porta72, cubica=b_cubica, frutas=b_frutas,
              semelhantes=b_semelhantes, naosoma=b_naosoma, antes=b_antes, multiplicar=b_multiplicar, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q4=b_q4, q5=b_q5, ponte=b_ponte, cta=b_cta)
