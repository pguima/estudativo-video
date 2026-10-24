"""Visual — Potenciação e Radiciação, Episódio 6: racionalização e expoente fracionário (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (tipografia de potências/raízes no expr, atalho, selo_teste...).
Peças deste episódio: porão da fração, máscara do "1 disfarçado", binômios que se encaixam e o tradutor (o dígito de baixo
do expoente voa para a casinha da raiz; o de cima vira o expoente de dentro).
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
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_potenciacao_ep6_racionalizacao_expoente_fracionario.mp4"
CARD_R = K.CARD_R
PORAO = "#8A6A4B"


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


def curva(c, x1, y1, x2, y2, bend, col, a, w=5, rotulo=None, rsize=28, rcol=None):
    """seta curva (quadrática) de (x1,y1) a (x2,y2); bend > 0 sobe; rótulo no meio da curva"""
    if a <= 0:
        return
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - bend
    p = skia.Path(); p.moveTo(x1, y1); p.quadTo(mx, my, x2, y2)
    pe = paint(col, a, stroke=w, cap_round=True)
    c.drawPath(p, pe)
    ang = math.atan2(y2 - my, x2 - mx)
    for s_ in (-1, 1):
        c.drawLine(x2, y2, x2 - 18 * math.cos(ang + s_ * 0.5), y2 - 18 * math.sin(ang + s_ * 0.5), pe)
    if rotulo:
        ftext(c, rotulo, mx, (y1 + y2) / 2 - bend / 2 + (-14 if bend > 0 else 34), rsize, "black", rcol or col, a)


# ======================================================================
# peças do episódio
# ======================================================================

def porao_frac(c, cx, cy, num, den, size, a, ap=1.0, den_a=1.0, lbl=True):
    """fração grande com o denominador dentro do 'porão' (retângulo marrom claro abaixo do traço)"""
    if a <= 0:
        return
    wn, wd = K.math_w(num, size), K.math_w(den, size)
    w = max(wn, wd) + size * 0.5
    if ap > 0:
        rrect(c, cx - w / 2 - 30, cy + 12, w + 60, size * 1.35, 18, PORAO, 0.13 * a * ap)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 - 30, cy + 12, w + 60, size * 1.35), 18, 18),
                    paint(PORAO, 0.55 * a * ap, stroke=3))
        if lbl:
            text(c, "PORÃO", cx, cy + 12 + size * 1.35 + 34, 24, "black", PORAO, a * ap, tracking=2)
    expr(c, num, cx, cy - size * 0.62, size, a)
    line(c, cx - w / 2, cy, cx + w / 2, cy, INK, a, max(4, size * 0.07), cap_round=True)
    expr(c, den, cx, cy + size * 0.72, size, a * den_a)


def mascara(c, cx, cy, w, a, col=None):
    """máscara de baile (o '1 disfarçado'): faixa com dois furos para os olhos"""
    if a <= 0:
        return
    col = col or PURPLE
    h = w * 0.36
    p = skia.Path()
    p.moveTo(cx - w / 2, cy - h * 0.2)
    p.cubicTo(cx - w * 0.3, cy - h * 0.75, cx - w * 0.1, cy - h * 0.5, cx, cy - h * 0.35)
    p.cubicTo(cx + w * 0.1, cy - h * 0.5, cx + w * 0.3, cy - h * 0.75, cx + w / 2, cy - h * 0.2)
    p.cubicTo(cx + w * 0.45, cy + h * 0.6, cx + w * 0.15, cy + h * 0.55, cx, cy + h * 0.2)
    p.cubicTo(cx - w * 0.15, cy + h * 0.55, cx - w * 0.45, cy + h * 0.6, cx - w / 2, cy - h * 0.2)
    p.close()
    for ex in (-1, 1):
        p.addOval(skia.Rect.MakeXYWH(cx + ex * w * 0.22 - w * 0.11, cy - h * 0.12, w * 0.22, h * 0.32))
    p.setFillType(skia.PathFillType.kEvenOdd)
    c.drawPath(p, paint(col, a))
    for ex in (-1, 1):   # fitinhas
        line(c, cx + ex * w / 2, cy - h * 0.2, cx + ex * (w / 2 + 40), cy + h * 0.1, col, a, 5, cap_round=True)


def peca(c, x, cy, s, size, col, a, encaixe=0.0):
    """binômio como uma peça de quebra-cabeça (pill colorida com o binômio dentro). Devolve a largura."""
    w = K.math_w(s, size) + 70
    h = size * 1.7
    if a > 0:
        rrect(c, x, cy - h / 2, w, h, h / 2, col, 0.12 * a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - h / 2, w, h), h / 2, h / 2), paint(col, a, stroke=4))
        expr(c, s, x + w / 2, cy, size, a)
    return w


def tradutor_icone(c, cx, cy, s, a):
    """ícone do tradutor: dois balões de fala (raiz e potência) com setas de ida e volta"""
    if a <= 0:
        return
    for dx, col, txt in ((-0.55, BLUE, "√"), (0.55, PURPLE, "xⁿ")):
        bx = cx + dx * s
        rrect(c, bx - s * 0.42, cy - s * 0.38, s * 0.84, s * 0.62, s * 0.16, col, a)
        tail = skia.Path()
        tx = bx - s * 0.12 if dx < 0 else bx + s * 0.12
        tail.moveTo(tx - s * 0.08, cy + s * 0.2); tail.lineTo(tx, cy + s * 0.42); tail.lineTo(tx + s * 0.1, cy + s * 0.2)
        tail.close()
        c.drawPath(tail, paint(col, a))
        fmid(c, txt, bx, cy - s * 0.07, s * 0.36, "black", "#FFFFFF", a)
    arrow(c, cx - s * 0.1, cy - s * 0.62, cx + s * 0.3, cy - s * 0.62, GREEN, a, 4, 12)
    arrow(c, cx + s * 0.1, cy + s * 0.62, cx - s * 0.3, cy + s * 0.62, GREEN, a, 4, 12)


# ---------- tradutor: a^(m/n) → √[n]{a^m}, com os dígitos voando ----------

class _Rec:
    """embrulha um nó da tipografia: guarda onde ele foi desenhado e pode trocar a cor / esconder"""
    def __init__(self, node, key, store, col=None, vis=True):
        self.node, self.key, self.store, self.col, self.vis = node, key, store, col, vis
        self.w, self.asc, self.desc = node.w, node.asc, node.desc

    def draw(self, c, x, base, col, a):
        self.store[self.key] = (x, base)
        if self.vis and a > 0:
            self.node.draw(c, x, base, self.col or col, a)


def tradutor(c, cxl, cxr, cy, S, base, num, den, a, p_den, p_num, ar=1.0, col_den=None, col_num=None):
    """esquerda: base^{num/den}; direita: √[den]{base^num}. p_den/p_num (0..1) fazem o dígito voar da esquerda para a
    casinha (índice) / para o expoente de dentro. ar = alfa do resto da raiz (radical + base)."""
    if a <= 0:
        return
    col_den, col_num = col_den or AMBER, col_num or GREEN
    st = {}
    es = S * 0.6
    L = K.Sup(K.Txt(base, S, "black"), K.Frac(_Rec(K.Txt(num, es, "black"), "ln", st, col_num),
                                               _Rec(K.Txt(den, es, "black"), "ld", st, col_den), es), S)
    xl = cxl - L.w / 2
    bl = cy + S * 0.36
    L.draw(c, xl, bl, INK, a)
    ish = S * 0.5
    inner = K.Sup(K.Txt(base, S, "black"), _Rec(K.Txt(num, es, "black"), "rn", st, col_num, vis=p_num >= 1), S) \
        if num != "1" else K.Txt(base, S, "black")
    R = K.Rad(inner, _Rec(K.Txt(den, ish, "black"), "rd", st, col_den, vis=p_den >= 1), S)
    xr = cxr - R.w / 2
    R.draw(c, xr, bl, INK, a * ar)
    for key_l, key_r, p, s_, col, sz0, sz1 in (("ld", "rd", p_den, den, col_den, es, ish),
                                              ("ln", "rn", p_num, num, col_num, es, es)):
        if 0 < p < 1 and key_r in st:
            e = ease_io(p)
            (x0, b0), (x1, b1) = st[key_l], st[key_r]
            x = lerp(x0, x1, e); b = lerp(b0, b1, e) - 55 * math.sin(math.pi * e)
            K.Txt(s_, lerp(sz0, sz1, e), "black").draw(c, x, b, col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DOIS TRUQUES QUE A PROVA COBRA", BLUE)
    aa, ab = ep(t, C["01.a"], 0.5), ep(t, C["01.b"], 0.5)
    if aa > 0:
        card(c, 230, 220, 620, 330, aa)
        text(c, "a sua resposta", 540, 270, 28, "black", GRAY, aa)
        expr(c, "1/√{2}", 540, 405, 110, aa)
    if ab > 0:
        card(c, 1070, 220, 620, 330, ab)
        text(c, "nas alternativas", 1380, 270, 28, "black", GRAY, ab)
        expr(c, "√{2}/2", 1380, 405, 110, ab)
    acc, ad = ep(t, C["01.c"], 0.4), ep(t, C["01.d"], 0.5)
    fmid(c, "?", W / 2, 385, 110, "black", AMBER, acc * (1 - ad))
    fmid(c, "=", W / 2, 385, 120, "black", GREEN, ad)
    chip(c, "o MESMO número: ≈ 0,707", W / 2, 600, GREEN, ad, 32)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        expr(c, "√{2}", 700, 730, 90, ae)
        text_mid(c, "ou", W / 2, 730, 44, "black", GRAY, ae)
        expr(c, "√[3]{3}", 1220, 730, 90, ae)
        text(c, "qual é maior?", W / 2, 830, 30, "black", AMBER, ae)
    selo(c, 1560, 820, ep(t, C["01.f"], 0.5), "2 TRUQUES", PURPLE, -6, 40)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "tirar a raiz do DENOMINADOR", "racionalização"),
            ("02.b", "comparar e multiplicar raízes", "de índices diferentes: expoente fracionário"),
            ("02.c", "os dois truques que a prova cobra", "com as Questões 6 e 7 do material")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 280 + j * 165 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 52, 30, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EPISÓDIOS 2 E 4, E O MMC", GREEN)
    cols = [(400, "03.a", "EPISÓDIO 4", "(√{7})^2 = 7", "o quadrado desfaz a raiz"),
            (960, "03.b", "EPISÓDIO 2", "2^3 · 2^4 = 2^7", "mesma base: soma os expoentes"),
            (1520, "03.c", "SÉRIE DE DIVISIBILIDADE", "MMC(2,3) = 6", "o menor número da tabuada dos dois")]
    for x, cue, tag, e, sub in cols:
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        rrect(c, x - 250, 250, 500, 470, 24, "#F7F7F5", a)
        text(c, tag, x, 300, 22, "black", GRAY, a, tracking=1)
        expr(c, e, x, 450, 56, a, cores={len(e.split()) - 1: GREEN})
        para(c, sub, x - 210, 600, 28, "bold", INK2, a, 420, 36)
    ac = ep(t, C["03.c"] + 3.0, 0.5)
    if ac > 0:
        text(c, "2, 4, 6…   3, 6…", 1520, 540, 26, "black", BLUE, ac)


# ======================================================================
# bloco A — o porão e o 1 disfarçado
# ======================================================================

def b_porao(c, t, C, B):
    frame(c, t, B["start"], "POR QUE A PROVA COBRA?", "A RAIZ NO PORÃO", BLUE)
    aa, ab = ep(t, C["04.a"], 0.5), ep(t, C["04.b"], 0.5)
    porao_frac(c, 520, 420, "1", "√{2}", 120, ep(t, C["04"], 0.5), ab)
    if aa > 0:
        arrow(c, 760, 600, 640, 530, BLUE, aa, 5, 16, progress=aa)
        text(c, "DENOMINADOR", 860, 630, 30, "black", BLUE, aa)
        text(c, "o número de baixo", 860, 668, 24, "bold", INK2, aa)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        card(c, 1060, 210, 600, 290, acc)
        text(c, "ALTERNATIVAS DO ENEM", 1360, 255, 22, "black", GRAY, acc, tracking=1)
        expr(c, "√{2}/2", 1360, 345, 70, acc)
        text(c, "porão SEM raiz", 1360, 470, 26, "black", GREEN, acc)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        expr(c, "1/√{2} ≈ 0,707", 1360, 575, 44, ad, cores={2: GREEN})
        expr(c, "√{2}/2 ≈ 0,707", 1360, 680, 44, ad, cores={2: GREEN})
    pill(c, "RACIONALIZAR = tirar a raiz do porão SEM mudar o valor", W / 2, 790, BLUE, size=30, a=ep(t, C["04.e"], 0.5),
         anchor="center", bounds=(0, 1920))


def b_disfarce(c, t, C, B):
    frame(c, t, B["start"], "MUDAR SEM MUDAR", "O 1 DISFARÇADO", PURPLE)
    rows = [("05.a", "5 · 1 = 5", "vezes 1: nada muda"), ("05.b", "3/3 = 1", "um disfarçado"),
            ("05.c", "√{2}/√{2} = 1", "também é 1")]
    for k, (cue, e, sub) in enumerate(rows):
        a = ep(t, C[cue], 0.5)
        y = 290 + k * 180
        expr(c, e, 560, y, 72, a, cores={len(e.split()) - 1: GREEN})
        text(c, sub, 900, y + 12, 28, "bold", INK2, a, align="left")
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        card(c, 1260, 230, 400, 470, ad)
        text_mid(c, "1", 1460, 470, 260, "black", INK, ad)
        mascara(c, 1460, 395, 260, ep(t, C["05.d"] + 0.6, 0.5))
        text(c, "1 DISFARÇADO", 1460, 660, 32, "black", PURPLE, ad)
        chip(c, "muda a aparência, não o valor", 1460, 770, GREEN, ep(t, C["05.d"] + 1.6, 0.5), 28)


# ======================================================================
# bloco B — caso 1
# ======================================================================

def b_caso1(c, t, C, B):
    frame(c, t, B["start"], "CASO 1", "UMA RAIZ SOZINHA NO PORÃO", PURPLE)
    a0 = ep(t, C["06"], 0.5)
    aa, ab, acc, ad = (ep(t, C["06." + k], 0.5) for k in "abcd")
    s = "1/√{2} · √{2}/√{2} = √{2}/2"
    expr(c, s, W / 2, 330, 100, a0, alfas={1: aa, 2: aa, 3: ad, 4: ad}, cores={2: PURPLE, 4: GREEN})
    if aa > 0:
        x1 = W / 2 - K.math_w(s, 100) / 2 + K.math_w("1/√{2} · √{2}/√{2}", 100) - K.math_w("√{2}/√{2}", 100) / 2
        mascara(c, x1, 175, 120, aa)
        text(c, "1 disfarçado", x1 + 120, 185, 24, "black", PURPLE, aa, align="left")
    if ab > 0:
        text(c, "EM CIMA", 400, 545, 24, "black", GRAY, ab, tracking=1)
        expr(c, "1 · √{2} = √{2}", 400, 625, 54, ab, cores={4: GREEN})
    if acc > 0:
        text(c, "EMBAIXO", 1150, 545, 24, "black", GRAY, acc, tracking=1)
        expr(c, "√{2} · √{2} = (√{2})^2 = 2", 1150, 625, 54, acc, cores={6: GREEN})
        text(c, "o quadrado desfaz a raiz", 1150, 700, 26, "bold", INK2, acc)
    chip(c, "mesmo valor, porão limpo ✓", W / 2, 790, GREEN, ep(t, C["06.d"] + 1.5, 0.5), 32)


def b_caso1_atalho(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "RAIZ SOZINHA EMBAIXO", GREEN)
    aa = ep(t, C["07.a"], 0.5)
    K.atalho(c, 300, 210, 1320, 200, "ATALHO", ["raiz sozinha embaixo?", "multiplique em cima e embaixo por ELA MESMA"],
             aa, 38)
    ab, acc = ep(t, C["07.b"], 0.5), ep(t, C["07.c"], 0.5)
    expr(c, "4/√{2} · √{2}/√{2} = 4√{2}/2", 820, 560, 80, ab, cores={2: PURPLE})
    expr(c, "= 2√{2}", 1440, 560, 80, acc, cores={1: GREEN})
    if acc > 0:
        text(c, "4 ÷ 2 = 2", 1440, 670, 28, "black", GREEN, acc)
    chip(c, "depois, sempre veja se dá para simplificar", W / 2, 780, AMBER, ep(t, C["07.d"], 0.5), 30)


# ======================================================================
# bloco C — caso 2, conjugado e diferença de quadrados
# ======================================================================

def b_caso2(c, t, C, B):
    frame(c, t, B["start"], "CASO 2", "DUAS RAÍZES NO PORÃO", AMBER)
    porao_frac(c, 520, 400, "6", "√{5} - √{2}", 100, ep(t, C["08.a"], 0.5), 1.0)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        text(c, "o truque de antes?", 1300, 250, 28, "black", AMBER, ab)
        expr(c, "(√{5}-√{2}) · √{5}", 1300, 340, 64, ab, cores={2: AMBER})
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        expr(c, "= 5 - √{10}", 1300, 470, 72, acc, cores={3: RED})
        c.drawCircle(1300 + K.math_w("= 5 - √{10}", 72) / 2 - K.math_w("√{10}", 72) / 2, 470, 80, paint(RED, acc, stroke=4))
    selo(c, 1300, 640, ep(t, C["08.d"], 0.5), "A RAIZ CONTINUA LÁ!", RED, -4, 36)
    chip(c, "precisamos de OUTRO disfarce", W / 2, 790, PURPLE, ep(t, C["08.e"], 0.5), 32)


def b_conjugado(c, t, C, B):
    frame(c, t, B["start"], "DOIS NOMES", "BINÔMIO E CONJUGADO", BLUE)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        expr(c, "√{5} - √{2}", 560, 330, 100, aa)
        w = K.math_w("√{5} - √{2}", 100)
        text(c, "termo 1", 560 - w / 2 + 60, 440, 26, "black", BLUE, aa)
        text(c, "termo 2", 560 + w / 2 - 60, 440, 26, "black", BLUE, aa)
        pill(c, "BINÔMIO = dois termos ligados por + ou −", 560, 520, BLUE, size=26, a=aa, anchor="center",
             bounds=(0, 1920))
    ab, acc = ep(t, C["09.b"], 0.5), ep(t, C["09.c"], 0.5)
    if ab > 0:
        line(c, 960, 240, 960, 620, "#E6E6E2", ab, 3)
        expr(c, "√{5} + √{2}", 1360, 330, 100, acc, cores={1: GREEN})
        if acc > 0:
            c.drawCircle(1360, 330, 50, paint(GREEN, acc, stroke=4))
            text(c, "sinal do meio TROCADO", 1360, 440, 26, "black", GREEN, acc)
        pill(c, "CONJUGADO = o mesmo binômio, sinal do meio trocado", 1360, 520, BLUE, size=24, a=ab, anchor="center",
             bounds=(0, 1920))
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        w1 = K.math_w("(√{5}-√{2})", 56) + 70
        peca(c, W / 2 - w1 - 20, 700, "(√{5}-√{2})", 56, AMBER, ad)
        peca(c, W / 2 + 20, 700, "(√{5}+√{2})", 56, GREEN, ad)
        text(c, "PAR PERFEITO", W / 2, 810, 28, "black", PURPLE, ad, tracking=2)


def b_diferenca(c, t, C, B):
    head_seq(c, t, C, [("10", "POR QUE A RAIZ SOME?", "DIFERENÇA DE QUADRADOS", PURPLE),
                       ("11", "NA DÚVIDA", "TESTE COM NÚMEROS PEQUENOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        aa = ep(t, C["10.a"], 0.5)
        expr(c, "(x-y) · (x+y)", W / 2, 260, 80, aa)
        cells = [("10.b", "x · x = x^2", 560, 410, INK), ("10.c", "x · y", 1360, 410, AMBER),
                 ("10.c", "-y · x", 560, 540, AMBER), ("10.d", "-y · y = -y^2", 1360, 540, INK)]
        for cue, e, x, y, col in cells:
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            rrect(c, x - 300, y - 52, 600, 104, 18, mix("#FFFFFF", col, 0.08), a)
            expr(c, ("+ " + e) if e == "x · y" else e, x, y, 56, a)
        acc = ep(t, C["10.c"] + 1.6, 0.4)
        if acc > 0:
            strike(c, 1210, 410, 1510, 410, acc, GREEN, acc)
            strike(c, 410, 540, 710, 540, acc, GREEN, acc)
            chip(c, "+xy e −xy se cancelam", W / 2, 475, GREEN, acc, 26)
        ae = ep(t, C["10.e"], 0.5)
        if ae > 0:
            boxed(c, 500, 640, 920, 120, PURPLE, ae, 0.08)
            expr(c, "(x-y)(x+y) = x^2 - y^2", W / 2, 700, 64, ae, cores=mono("(x-y)(x+y) = x^2 - y^2", PURPLE))
            text(c, "um quadrado MENOS outro quadrado", W / 2, 800, 26, "black", PURPLE, ae)
        return
    aa, ab = ep(t, C["11.a"], 0.5), ep(t, C["11.b"], 0.5)
    expr(c, "(5-2) · (5+2) = 3 · 7 = 21", W / 2, 330, 72, aa, cores={8: GREEN})
    expr(c, "5^2 - 2^2 = 25 - 4 = 21", W / 2, 500, 72, ab, cores={8: GREEN})
    K.selo_teste(c, W / 2, 680, ep(t, C["11.b"] + 2.5, 0.4), ok=True, s="TESTE COM 5 E 2: CONFERE")


def b_encaixe(c, t, C, B):
    frame(c, t, B["start"], "O PAR PERFEITO", "A RAIZ SE DESMANCHA", GREEN)
    aa = ep(t, C["12.a"], 0.5)
    enc = ep(t, C["12.a"] + 0.6, 1.0)
    w1 = K.math_w("(√{5}-√{2})", 64) + 70
    gap = lerp(260, 10, enc)
    peca(c, W / 2 - w1 - gap / 2, 290, "(√{5}-√{2})", 64, AMBER, aa)
    peca(c, W / 2 + gap / 2, 290, "(√{5}+√{2})", 64, GREEN, aa)
    if enc >= 1 and aa > 0:
        fmid(c, "·", W / 2, 290, 60, "black", INK, aa)
    ab = ep(t, C["12.b"], 0.5)
    acc = ep(t, C["12.c"], 0.6)
    expr(c, "(√{5})^2 - (√{2})^2", 700, 470, 70, ab * (1 - 0.6 * acc), cores={0: AMBER, 2: GREEN})
    expr(c, "= 5 - 2 = 3", 1260, 470, 76, acc, cores={5: GREEN})
    chip(c, "o quadrado DESMANCHA a raiz", 700, 570, PURPLE, acc, 28)
    selo(c, 1300, 590, ep(t, C["12.d"], 0.5), "SEM RAIZ!", GREEN, -5, 40)
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        K.atalho(c, 300, 650, 1320, 170, "ATALHO",
                 ["com o conjugado, o porão vira direto: PRIMEIRO² − SEGUNDO²"], ae, 32)


# ======================================================================
# bloco D — o tradutor
# ======================================================================

def b_tradutor(c, t, C, B):
    frame(c, t, B["start"], "O SEGUNDO TRUQUE", "UM TRADUTOR", PURPLE)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        text(c, "IDIOMA RAIZ", 420, 215, 26, "black", BLUE, aa, tracking=1)
        text(c, "IDIOMA POTÊNCIA", 1500, 215, 26, "black", PURPLE, aa, tracking=1)
    tradutor_icone(c, W / 2, 290, 110, ep(t, C["13.b"], 0.5))
    acc = ep(t, C["13.c"], 0.5)
    af = ep(t, C["13.f"], 0.5)
    expr(c, "√{2}", 420, 350, 90, acc)
    expr(c, "2^{?}", 1500, 350, 90, acc * (1 - af), cores={0: AMBER})
    expr(c, "2^{1/2}", 1500, 350, 90, af, cores={0: GREEN})
    ad, ae = ep(t, C["13.d"], 0.5), ep(t, C["13.e"], 0.5)
    expr(c, "(√{2})^2 = 2", 420, 520, 60, ad, cores={2: GREEN})
    if ae > 0:
        expr(c, "(2^{1/2})^2 = 2^{(1/2)·2} = 2^1 = 2", 1290, 520, 54, ae, cores={6: GREEN})
        text(c, "potência de potência: multiplica os expoentes", 1290, 610, 24, "bold", INK2, ae)
    if af > 0:
        boxed(c, 660, 655, 600, 160, PURPLE, af, 0.08)
        expr(c, "√{2} = 2^{1/2}", W / 2, 750, 70, af, cores=mono("√{2} = 2^{1/2}", PURPLE))


def b_regra(c, t, C, B):
    frame(c, t, B["start"], "EXPOENTE FRACIONÁRIO", "EMBAIXO VIRA ÍNDICE", PURPLE)
    a0 = ep(t, C["14"], 0.5)
    pill(c, "EXPOENTE FRACIONÁRIO = expoente em forma de fração", W / 2, 225, BLUE, size=28, a=a0, anchor="center",
         bounds=(0, 1920))
    aa = ep(t, C["14.a"], 0.5)
    pb, pc = prog(t, C["14.b"], 1.4), prog(t, C["14.c"], 1.4)
    tradutor(c, 600, 1320, 470, 170, "a", "m", "n", aa, pb, pc, ar=ep(t, C["14.a"] + 0.8, 0.5))
    fmid(c, "=", W / 2, 470, 110, "black", INK, aa)
    if pb > 0:
        text(c, "EMBAIXO → índice (a casinha)", 1320, 620, 30, "black", AMBER, ep(t, C["14.b"], 0.4))
    if pc > 0:
        text(c, "EM CIMA → expoente de dentro", 1320, 670, 30, "black", GREEN, ep(t, C["14.c"], 0.4))
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 600, 560, 170, 22, "#F7F7F5", ad)
        expr(c, "√[3]{5} = 5^{1/3}", 540, 685, 64, ad, cores={2: GREEN})


def b_oito(c, t, C, B):
    frame(c, t, B["start"], "TRADUZINDO", "8 ELEVADO A 2/3", PURPLE)
    a0 = ep(t, C["15"], 0.5)
    pa, pb = prog(t, C["15.a"], 1.4), prog(t, C["15.b"], 1.4)
    tradutor(c, 560, 1180, 380, 160, "8", "2", "3", a0, pa, pb, ar=ep(t, C["15.a"], 0.5))
    fmid(c, "=", 870, 380, 100, "black", INK, a0)
    acc = ep(t, C["15.c"], 0.5)
    expr(c, "= √[3]{64} = 4", 1560, 380, 72, acc, cores={3: GREEN})
    if pa > 0:
        text(c, "o 3 de baixo → índice", 560, 560, 28, "black", AMBER, ep(t, C["15.a"], 0.4))
    if pb > 0:
        text(c, "o 2 de cima → expoente de dentro", 560, 610, 28, "black", GREEN, ep(t, C["15.b"], 0.4))
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        K.atalho(c, 980, 520, 720, 290, "ATALHO", ["faça a RAIZ primeiro", ("m", "√[3]{8} = 2 → 2^2 = 4")], ad, 40)


# ======================================================================
# blocos E/F/G — multiplicar e comparar índices diferentes
# ======================================================================

def b_multiplicar(c, t, C, B):
    frame(c, t, B["start"], "POR QUE É PODEROSO?", "AS 7 PROPRIEDADES VALEM", PURPLE)
    chip(c, "virando potência, as 7 propriedades do ep. 2 valem para raízes", W / 2, 230, BLUE, ep(t, C["16.a"], 0.5), 28)
    ab = ep(t, C["16.b"], 0.5)
    expr(c, "√{2} · √[3]{2} = ?", W / 2, 340, 84, ab)
    acc = ep(t, C["16.c"], 0.5)
    expr(c, "2^{1/2} · 2^{1/3}", 560, 490, 72, acc)
    chip(c, "mesma base: SOMA os expoentes", 560, 600, PURPLE, ep(t, C["16.d"], 0.5), 28)
    ae = ep(t, C["16.e"], 0.5)
    if ae > 0:
        text(c, "MMC(2, 3) = 6", 1340, 430, 26, "black", BLUE, ae)
        expr(c, "1/2 + 1/3 = 3/6 + 2/6 = 5/6", 1340, 520, 56, ae, cores={8: GREEN})
    af = ep(t, C["16.f"], 0.5)
    if af > 0:
        boxed(c, 560, 665, 800, 150, GREEN, af, 0.08)
        expr(c, "= 2^{5/6} = √[6]{2^5}", W / 2, 755, 64, af, cores={1: GREEN, 3: GREEN})


def b_comparar(c, t, C, B):
    frame(c, t, B["start"], "PARA COMPARAR", "MESMO ÍNDICE PRIMEIRO", PURPLE)
    a0 = ep(t, C["17"], 0.5)
    expr(c, "√{2}", 560, 260, 80, a0)
    expr(c, "√[3]{3}", 1360, 260, 80, a0)
    fmid(c, "?", W / 2, 260, 80, "black", AMBER, a0)
    chip(c, "índices diferentes: não dá direto", W / 2, 360, AMBER, ep(t, C["17.a"], 0.5), 26)
    ab = ep(t, C["17.b"], 0.5)
    chip(c, "MMC(2, 3) = 6", W / 2, 420, BLUE, ab, 26)
    for cue, x, e1, e2 in (("17.c", 560, "2^{1/2} = 2^{3/6}", "√[6]{2^3} = √[6]{8}"),
                           ("17.d", 1360, "3^{1/3} = 3^{2/6}", "√[6]{3^2} = √[6]{9}")):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        expr(c, e1, x, 520, 54, a)
        expr(c, e2, x, 640, 60, ep(t, C[cue] + 2.5, 0.5), cores={2: GREEN})
    ae = ep(t, C["17.e"], 0.5)
    if ae > 0:
        boxed(c, 560, 720, 800, 100, GREEN, ae, 0.08)
        expr(c, "8 < 9  →  √{2} < √[3]{3}", W / 2, 770, 56, ae, cores={1: GREEN, 4: GREEN})


def b_comparar_atalho(c, t, C, B):
    frame(c, t, B["start"], "ATALHO", "COMPARAR SEM SOFRER", GREEN)
    aa, ab = ep(t, C["18.a"], 0.5), ep(t, C["18.b"], 0.5)
    K.atalho(c, 260, 210, 1400, 160, "ATALHO 1", ["mesmo índice: compare só os números de dentro"], aa, 36)
    K.atalho(c, 260, 400, 1400, 160, "ATALHO 2", ["o índice multiplicou por k? eleve o número de dentro a k"], ab, 36)
    for cue, x, e1, k, e2 in (("18.c", 560, "√{2}", "índice × 3", "√[6]{2^3} = √[6]{8}"),
                              ("18.d", 1360, "√[3]{3}", "índice × 2", "√[6]{3^2} = √[6]{9}")):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        expr(c, e1, x - 250, 690, 60, a)
        arrow(c, x - 170, 690, x - 60, 690, AMBER, a, 4, 14, progress=a)
        text(c, k, x - 115, 650, 22, "black", AMBER, a)
        expr(c, e2, x + 140, 690, 54, a, cores={2: GREEN})


# ======================================================================
# nós fazemos
# ======================================================================

EXS = [("20.a", "3/√{3}", "= √{3}", "3√3/3 = √3"), ("20.c", "27^{1/3}", "= √[3]{27} = 3", "3³ = 27")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("20", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    labels = ["RACIONALIZE", "ESCREVA COMO RAIZ E CALCULE"]
    for k, (cue, q, r, why) in enumerate(EXS):
        a = ep(t, C["19." + "ab"[k]], 0.5)
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 330, 210, 660, 280, 24, "#F7F7F5", a)
        text(c, labels[k], x, 255, 22, "black", GRAY, a, tracking=1)
        expr(c, q, x, 370, 90, a)
        if t >= C["20"]:
            ra = ep(t, C[cue], 0.5)
            if k == 0:
                expr(c, "3/√{3} · √{3}/√{3} = 3√{3}/3", x, 590, 54, ra)
                expr(c, "= √{3}", x, 720, 72, ep(t, C["20.b"], 0.5), cores={1: GREEN})
            else:
                expr(c, "27^{1/3} = √[3]{27}", x, 590, 60, ra)
                expr(c, "= 3", x, 720, 80, ep(t, C["20.d"], 0.5), cores={1: GREEN})
                text(c, "porque 3³ = 27", x + 200, 730, 24, "bold", INK2, ep(t, C["20.d"], 0.5), align="left")
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 640)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Racionalizar é multiplicar por 1 disfarçado.", "Binômio com raiz? Multiplique pelo conjugado.",
          "Embaixo vira índice; em cima vira expoente."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("multiplicar SÓ o denominador: 1/√2 vira 1/2", "a raiz saiu do porão",
          "o valor mudou (0,5 ≠ 0,707): multiplique EM CIMA E EMBAIXO"),
         ("usar o MESMO sinal em vez do conjugado", "no caso 1 você multiplicou pelo próprio denominador",
          "(√5 − √2)² = 7 − 2√10: a raiz continua. Troque o sinal do meio"),
         ("comparar índices diferentes olhando o número de dentro", "com o mesmo índice funciona",
          "√3 = ⁶√27 e ³√4 = ⁶√16: o 4 é maior, mas √3 ganha")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24"], ERROS)


# ======================================================================
# Questão 6 do material
# ======================================================================

ALTS6 = [("A", "= 2√{5} + 2√{2}", "", GREEN), ("B", "= 6√{5} - 6√{2}", "sinal errado e não dividiu por 3", RED),
         ("C", "= √{5}+√{2}/3", "perdeu o 6", RED), ("D", "= 2√{3}", "fez √5 − √2 = √3", RED),
         ("E", "= √{5} + √{2}", "só trocou o sinal", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · RACIONALIZAÇÃO COM CONJUGADO", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    text(c, "Racionalizando o denominador de", 190, 250, 34, "black", INK, a0, align="left")
    expr(c, "6/√{5}-√{2}", 190, 340, 54, a0, align="left")
    text(c, ", obtém-se", 190 + K.math_w("6/√{5}-√{2}", 54) + 6, 352, 34, "black", INK, a0, align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"B": C["27.xb"], "C": C["27.xc"], "D": C["27.xd"], "E": C["27.xe"]}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS6, 960, 210, 720, 42, C["26.ok"], "A", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["25.end"] - 1.9, 470, 620)
    if t >= C["26"]:
        ra = ep(t, C["26"], 0.4)
        rrect(c, 170, 410, 740, 400, 18, "#FFFFFF", ra, shadow=True)
        chip(c, "binômio no porão → CONJUGADO", 540, 445, PURPLE, ra, 24)
        aa = ep(t, C["26.a"], 0.4)
        expr(c, "6/√{5}-√{2} · √{5}+√{2}/√{5}+√{2}", 540, 530, 36, aa, cores={2: GREEN})
        ab = ep(t, C["26.b"], 0.4)
        expr(c, "embaixo: 5 - 2 = 3", 540, 615, 32, ab, cores={5: GREEN})
        acc = ep(t, C["26.c"], 0.4)
        expr(c, "6(√{5}+√{2})/3 = 2(√{5}+√{2})", 540, 690, 34, acc, alfas={1: ep(t, C["26.d"], 0.4),
                                                                           2: ep(t, C["26.d"], 0.4)})
        expr(c, "= 2√{5} + 2√{2}", 540, 768, 38, ep(t, C["26.e"], 0.4), cores={1: GREEN, 2: GREEN, 3: GREEN})


# ======================================================================
# Questão 7 do material
# ======================================================================

ALTS7 = [("A", "= √{2} < √[3]{3} < √[6]{10}", "", GREEN),
         ("B", "= √[6]{10} < √[3]{3} < √{2}", "\"índice maior dá menor\"", RED),
         ("C", "= √[3]{3} < √{2} < √[6]{10}", "chute: 1,44 e 1,41", RED),
         ("D", "= √{2} < √[6]{10} < √[3]{3}", "fez 3³ em vez de 3²", RED),
         ("E", "= √[6]{10} < √{2} < √[3]{3}", "\"índice maior dá menor\"", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · COMPARAR ÍNDICES DIFERENTES", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    text(c, "Colocando os números", 190, 250, 34, "black", INK, a0, align="left")
    expr(c, "√{2} , √[3]{3} e √[6]{10}", 190, 330, 48, a0, align="left", gap=14)
    text(c, "em ordem crescente, obtém-se", 190, 415, 34, "black", INK, a0, align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"B": C["30.xb"], "C": C["30.xc"], "D": C["30.xd"], "E": C["30.xe"]}
    if t >= C["28.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS7, 960, 210, 720, 38, C["29.ok"], "A", cues_in, cues_x, gap=12)
    pause_timer(c, t, C["28.end"] - 1.9, 470, 640)
    if t >= C["29"]:
        ra = ep(t, C["29"], 0.4)
        rrect(c, 170, 460, 740, 350, 18, "#FFFFFF", ra, shadow=True)
        chip(c, "MMC(2, 3, 6) = 6", 540, 495, BLUE, ep(t, C["29.a"], 0.4), 24)
        expr(c, "√{2} = √[6]{2^3} = √[6]{8}", 540, 570, 40, ep(t, C["29.b"], 0.4), cores={4: GREEN})
        expr(c, "√[3]{3} = √[6]{3^2} = √[6]{9}", 540, 645, 40, ep(t, C["29.c"], 0.4), cores={4: GREEN})
        expr(c, "√[6]{10}", 540, 715, 40, ep(t, C["29.d"], 0.4), cores={0: GREEN})
        expr(c, "8 < 9 < 10", 540, 780, 40, ep(t, C["29.e"], 0.4), cores=mono("8 < 9 < 10", GREEN))
    if t >= C["30"]:
        aa = ep(t, C["30.a"], 0.5)
        selo(c, 1320, 700, aa, "SURPRESA: maior índice e MAIOR número", AMBER, -3, 30)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    for k, (cue, s, col) in enumerate((("32.a", "juntar TUDO", BLUE), ("32.b", "caçar as PEGADINHAS", AMBER),
                                       ("32.c", "treinar com QUESTÕES NOVAS", GREEN))):
        a = ep(t, C[cue], 0.5)
        x = 440 + k * 520
        if a > 0:
            card(c, x - 240, 280, 480, 260, a)
            badge_num(c, k + 1, x, 350, a, 34, bg=col)
            text(c, s, x, 470, 29, "black", col, a)
    pill(c, "ep. 7 · revisão geral e treino para o ENEM", W / 2, 700, PURPLE, size=32, a=ep(t, C["32.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Você achava que ⁶√10 era a menor?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, porao=b_porao, disfarce=b_disfarce, caso1=b_caso1,
              caso1_atalho=b_caso1_atalho, caso2=b_caso2, conjugado=b_conjugado, diferenca=b_diferenca, encaixe=b_encaixe,
              tradutor=b_tradutor, regra=b_regra, oito=b_oito, multiplicar=b_multiplicar, comparar=b_comparar,
              comparar_atalho=b_comparar_atalho, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q6=b_q6, q7=b_q7,
              ponte=b_ponte, cta=b_cta)
