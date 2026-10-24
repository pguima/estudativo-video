"""Visual — Equação do 2º Grau e Bhaskara, Episódio 1: forma geral, coeficientes com sinal e incompletas (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: tabela_abc() (a tabelinha a | b | c, com o sinal em âmbar), arruma() (os termos de 3x − x² = 2
andando para a esquerda e se arrumando na ordem x², x, número), caixas() (o produto nulo: duas caixinhas multiplicadas com
a placa "= 0"; cada uma acende quando vira zero), terreno() (o quadrado de 25 m²).
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
frame, head_seq, which, para, boxed, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                 K.selo, K.pause_timer)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_2grau_ep1_forma_incompletas.mp4"
CARD_R = K.CARD_R
TERRA = "#CDE7C1"
TERRA2 = "#7FB069"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)]"""
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        if a > 0:
            fmid(c, s_, x, cy, size, peso, col or INK, a, align="left")
        x += w_


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def tabela_abc(c, cx, y, vals, alfas, size=56, w=170, sinais=True):
    """tabelinha a | b | c: vals = ['−1', '3', '−2']; alfas = (a_a, a_b, a_c). Números negativos com o sinal em âmbar."""
    a0 = max(alfas)
    if a0 <= 0:
        return
    x0 = cx - 1.5 * w
    rrect(c, x0, y, 3 * w, 86, 16, mix("#FFFFFF", BLUE, 0.14), a0)
    rrect(c, x0, y + 86, 3 * w, 120, 16, "#FFFFFF", a0, shadow=True)
    for k, (L, v, al) in enumerate(zip("abc", vals, alfas)):
        xx = x0 + w * (k + 0.5)
        text_mid(c, L, xx, y + 43, 44, "black", BLUE, a0)
        if k:
            line(c, x0 + w * k, y + 10, x0 + w * k, y + 196, LIGHT, a0, 3)
        if al <= 0:
            continue
        neg = v.startswith("-") or v.startswith("−")
        if neg and sinais:
            body = v[1:]
            ww = ftext_w("−", "black", size) + ftext_w(body, "black", size)
            xs = xx - ww / 2
            fmid(c, "−", xs, y + 146, size, "black", AMBER, al, align="left")
            fmid(c, body, xs + ftext_w("−", "black", size), y + 146, size, "black", INK, al, align="left")
        else:
            fmid(c, v.replace("-", "−"), xx, y + 146, size, "black", INK, al)


def caixas(c, cx, cy, esq, dir_, a, acende_e=0.0, acende_d=0.0, size=64, placa=True):
    """produto nulo: [esq] · [dir_] = 0. acende_*: 0→1 a caixinha fica verde (virou zero)."""
    if a <= 0:
        return
    we = K.math_w(esq, size) + 70
    wd = K.math_w(dir_, size) + 70
    wdot = 70
    wplaca = 200 if placa else 0
    tot = we + wdot + wd + (40 + wplaca if placa else 0)
    x = cx - tot / 2
    for k, (s_, ww, lit) in enumerate(((esq, we, acende_e), (dir_, wd, acende_d))):
        col = mix("#FFFFFF", GREEN, 0.22 * lit)
        rrect(c, x, cy - size * 0.95, ww, size * 1.9, 22, col, a, shadow=True, stroke=4, stroke_color=mix(INK2, GREEN, lit))
        expr(c, s_, x + ww / 2, cy, size, a, cores={i: mix(INK, GREEN, lit) for i in range(9)})
        if lit > 0:
            pill(c, "= 0", x + ww / 2, cy + size * 1.35, GREEN, size=26, a=a * lit, anchor="center")
        x += ww
        if k == 0:
            fmid(c, "·", x + wdot / 2, cy, size * 1.2, "black", INK, a)
            x += wdot
    if placa:
        x += 40
        rrect(c, x, cy - 56, wplaca, 112, 18, INK, a)
        fmid(c, "= 0", x + wplaca / 2, cy, 58, "black", "#FFFFFF", a)


def terreno(c, cx, cy, lado, a, rot="25 m²", lado_txt=None):
    if a <= 0:
        return
    x0, y0 = cx - lado / 2, cy - lado / 2
    rrect(c, x0, y0, lado, lado, 10, TERRA, a, shadow=True, stroke=5, stroke_color=TERRA2)
    for k in range(1, 5):
        line(c, x0 + lado * k / 5, y0 + 6, x0 + lado * k / 5, y0 + lado - 6, "#FFFFFF", a * 0.7, 2)
        line(c, x0 + 6, y0 + lado * k / 5, x0 + lado - 6, y0 + lado * k / 5, "#FFFFFF", a * 0.7, 2)
    fmid(c, rot, cx, cy, lado * 0.17, "black", "#2F5D24", a)
    if lado_txt:
        pill(c, lado_txt, cx, y0 + lado + 44, INK, size=28, a=a, anchor="center")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "EQUAÇÃO DO 2º GRAU", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "3x^2 = 12x", W / 2, 320, 120, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        pill(c, "÷ x", 1340, 320, AMBER, size=40, a=ab, anchor="center")
        arrow(c, W / 2, 420, W / 2, 500, INK2, ab, 5, 16)
        expr(c, "3x = 12   →   x = 4", W / 2, 580, 84, ab, cores={4: GREEN, 5: GREEN, 6: GREEN})
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        check_icon(c, 1470, 560, 34, acc, GREEN)
        pill(c, "CERTO, MAS INCOMPLETO", W / 2, 700, AMBER, size=34, a=acc, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 760, 770, 400, 120, 24, mix("#FFFFFF", RED, 0.10), ad)
        fmid(c, "x = ?", W / 2, 830, 64, "black", RED, ad)
    ae = ep(t, C["01.e"], 0.4)
    if ae > 0:
        selo(c, 1360, 840, ae, "QUAL RESPOSTA SUMIU?", RED, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "arrumar qualquer equação do 2º grau", "tudo de um lado, zero do outro"),
            ("02.b", "ler os coeficientes sem errar o sinal", "x² − 7x + 10  →  b = −7"),
            ("02.c", "resolver as incompletas sem fórmula", "fator comum · raiz com ± · produto nulo")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 320 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "EXPRESSÕES ALGÉBRICAS", 560, 280, 30, "black", PURPLE, aa)
        text(c, "fator comum", 560, 330, 26, "bold", GRAY, aa)
        expr(c, "5x + 10 = 5(x+2)", 560, 420, 60, aa, cores={4: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "quadrado da soma", 560, 540, 26, "bold", GRAY, ab)
        expr(c, "(x+1)^2 = x^2 + 2x + 1", 560, 630, 56, ab)
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        text(c, "EQUAÇÕES DO 1º GRAU", 1360, 280, 30, "black", BLUE, ac)
        text(c, "a balança", 1360, 330, 26, "bold", GRAY, ac)
        # balança simples
        rrect(c, 1352, 440, 16, 230, 6, "#7A5A3A", ac)
        rrect(c, 1250, 660, 220, 24, 8, "#7A5A3A", ac)
        rrect(c, 1160, 430, 400, 16, 8, "#7A5A3A", ac)
        for sx in (-1, 1):
            c.drawOval(skia.Rect.MakeXYWH(1360 + sx * 190 - 80, 500, 160, 26), paint(GREEN, ac))
            line(c, 1360 + sx * 190, 438, 1360 + sx * 190 - 60, 506, INK2, ac, 2)
            line(c, 1360 + sx * 190, 438, 1360 + sx * 190 + 60, 506, INK2, ac, 2)
        pill(c, "o mesmo dos dois lados", 1360, 740, PURPLE, size=28, a=ac, anchor="center")
    line(c, 960, 240, 960, 780, "#E6E6E2", max(ab, ac), 3)


# ======================================================================
# concreto: o terreno de 25 m²
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UM TERRENO QUADRADO", "QUANTO MEDE O LADO?", BLUE)
    a0 = ep(t, C["04"], 0.5)
    aa = ep(t, C["04.a"], 0.5)
    terreno(c, 520, 470, 400, a0, "25 m²", "lado = 5 m" if aa > 0.5 else "lado = ?")
    if aa > 0:
        expr(c, "5 · 5 = 25", 520, 790, 46, aa, cores={4: GREEN})
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        rrect(c, 960, 250, 760, 120, 24, mix("#FFFFFF", BLUE, 0.10), ab)
        fmid(c, "? · ? = 25", 1340, 310, 60, "black", INK, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        expr(c, "5 · 5 = 25", 1340, 450, 56, acc, cores={0: GREEN, 2: GREEN})
        expr(c, "(-5) · (-5) = 25", 1340, 540, 56, acc, cores={0: AMBER, 2: AMBER})
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        expr(c, "x^2 = 25", 1340, 670, 80, ad, cores={0: BLUE})
        pill(c, "x = 5  ou  x = −5", 1340, 770, PURPLE, size=32, a=ad, anchor="center")
        ad2 = ep(t, C["04.d"] + 3.6, 0.5)
        if ad2 > 0:
            strike(c, 1420, 770, 1510, 770, ad2, RED)
            pill(c, "lado não é negativo", 1340, 840, AMBER, size=24, a=ad2, anchor="center")


# ======================================================================
# bloco a — definição
# ======================================================================

def b_definicao(c, t, C, B):
    head_seq(c, t, C, [("05", "EQUAÇÃO DO 2º GRAU", "A FORMA GERAL", BLUE), ("06", "POR QUE a ≠ 0?", "SEM x², VIRA 1º GRAU", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    aa = ep(t, C["05.a"], 0.5)
    expr(c, "ax^2 + bx + c = 0", W / 2, 290, 110, aa, cores={0: PURPLE, 2: PURPLE, 4: PURPLE})
    if sid == "05":
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            for k, (L, s) in enumerate((("a", "acompanha o x²"), ("b", "acompanha o x"), ("c", "termo independente"))):
                ak = ep(t, C["05.b"] + 2.5 + k * 2.2, 0.4)
                x = 400 + k * 560
                rrect(c, x - 240, 420, 480, 170, 22, mix("#FFFFFF", BLUE, 0.10), ak)
                text_mid(c, L, x, 470, 56, "black", BLUE, ak)
                text_mid(c, s, x, 545, 30, "bold", INK2, ak)
            text(c, "COEFICIENTES: os números da equação", W / 2, 400, 26, "black", BLUE, ab)
        acc = ep(t, C["05.c"], 0.5)
        if acc > 0:
            rrect(c, 460, 660, 1000, 110, 22, mix("#FFFFFF", GREEN, 0.14), acc)
            linha(c, [("RAÍZES", BLUE), (": os valores de x que resolvem a equação", INK)], W / 2, 715, 32, acc)
        return
    a6 = ep(t, C["06.a"], 0.5)
    if a6 > 0:
        pill(c, "a = 0", 1500, 290, AMBER, size=36, a=a6, anchor="center")
        expr(c, "0x^2 + 3x - 6", 760, 470, 80, a6, cores={0: RED})
        strike(c, 560, 470, 700, 470, ep(t, C["06.a"] + 1.4, 0.4), RED)
        arrow(c, 1080, 470, 1180, 470, INK, a6, 5, 16)
        expr(c, "3x - 6", 1400, 470, 80, ep(t, C["06.a"] + 1.8, 0.4), cores={0: BLUE})
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        pill(c, "isso é do 1º grau", 1400, 570, BLUE, size=28, a=ab, anchor="center")
        regra(c, "regra: a ≠ 0", W / 2, 720, ab, 44)


# ======================================================================
# bloco b — arrumar e ler os coeficientes
# ======================================================================

def arruma(c, t, t0, cy, size, a):
    """3x − x² = 2  →  −x² + 3x − 2 = 0. Os termos andam (0→1 em ~2,4 s a partir de t0)."""
    if a <= 0:
        return
    m = ease_io(clamp((t - t0) / 2.4))
    # posições iniciais e finais (centros)
    ini = {"3x": 620, "-x^2": 860, "=": 1080, "2": 1240}
    fim = {"-x^2": 560, "3x": 830, "2": 1080, "=": 1290, "0": 1460}
    depois = {"3x": "+ 3x", "2": "- 2"}
    for tok in ("3x", "-x^2", "=", "2"):
        x = ini[tok] + (fim[tok] - ini[tok]) * m
        s = depois[tok] if (tok in depois and m > 0.5) else tok
        col = AMBER if (tok == "2" and m > 0.5) else (BLUE if tok == "-x^2" else INK)
        lift = -50 * (1 - abs(2 * m - 1)) if tok in ("2", "-x^2") and 0 < m < 1 else 0
        expr(c, s, x, cy + lift, size, a, cores={0: col, 1: col})
    expr(c, "0", fim["0"], cy, size, a * clamp((m - 0.6) / 0.4), cores={0: GREEN})


def b_arrumar(c, t, C, B):
    head_seq(c, t, C, [("07", "PRIMEIRO, ARRUME", "TUDO DE UM LADO · ZERO DO OUTRO", PURPLE),
                       ("08", "A TABELINHA", "O SINAL FAZ PARTE DO COEFICIENTE", PURPLE),
                       ("09", "TREINE O OLHO", "TABELA DA SEÇÃO 02", PURPLE),
                       ("10", "ATALHO", "a NEGATIVO? VEZES −1", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09", "10"])
    if sid in ("07", "08"):
        a0 = ep(t, C["07"], 0.5)
        if t < C["07.c"]:
            expr(c, "3x - x^2 = 2", W / 2, 300, 96, a0)
            if t >= C["07.t"] + 2.0:
                pill(c, "a = ?", 1500, 300, AMBER, size=34, a=ep(t, C["07.t"] + 2.0, 0.4), anchor="center")
        else:
            arruma(c, t, C["07.c"] + 1.0, 300, 96, a0)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0 and sid == "07":
            for k, s in enumerate(("x²", "x", "número")):
                badge_num(c, k + 1, 640 + k * 320, 520, ep(t, C["07.b"] + 2.0 + 0.6 * k, 0.3), 30, bg=PURPLE)
                text(c, s, 640 + k * 320, 600, 36, "black", PURPLE, ep(t, C["07.b"] + 2.0 + 0.6 * k, 0.3))
            regra(c, "tudo de um lado · zero do outro", W / 2, 720, ab, 36)
        if sid == "08":
            al = (ep(t, C["08.a"], 0.4), ep(t, C["08.b"], 0.4), ep(t, C["08.c"], 0.4))
            tabela_abc(c, W / 2, 440, ["-1", "3", "-2"], al)
            ad = ep(t, C["08.d"], 0.5)
            if ad > 0:
                rrect(c, 360, 690, 1200, 110, 22, mix("#FFFFFF", AMBER, 0.14), ad)
                linha(c, [("o sinal é o ", INK), ("SOBRENOME", AMBER), (": o c se chama ", INK), ("−2", AMBER)],
                      W / 2, 745, 36, ad)
        return
    if sid == "09":
        rows = [("09.a", "2x^2 - 7x + 3 = 0", "já está", ["2", "-7", "3"]),
                ("09.b", "x^2 = 5x", "x^2 - 5x = 0", ["1", "-5", "0"]),
                ("09.c", "(x+1)^2 = 9", "x^2 + 2x - 8 = 0", ["1", "2", "-8"])]
        for k, (cue, dada, geral, vals) in enumerate(rows):
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            y = 270 + k * 190
            rrect(c, 180, y - 70, 1560, 160, 20, "#FFFFFF", a, shadow=True)
            expr(c, dada, 420, y + 10, 44, a)
            arrow(c, 640, y + 10, 700, y + 10, GRAY, a, 4, 12)
            if geral == "já está":
                text_mid(c, "já está arrumada", 900, y + 10, 30, "bold", GRAY, a)
            else:
                expr(c, geral, 920, y + 10, 44, ep(t, C[cue] + 2.5, 0.4), cores={0: PURPLE})
            for j, v in enumerate(vals):
                xx = 1300 + j * 150
                aj = ep(t, C[cue] + 3.5 + 0.4 * j, 0.3)
                text_mid(c, "abc"[j], xx, y - 34, 24, "black", BLUE, a)
                neg = v.startswith("-")
                fmid(c, v.replace("-", "−"), xx, y + 24, 46, "black", AMBER if neg else INK, aj)
        return
    # 10 — vezes −1
    a0 = ep(t, C["10"], 0.5)
    expr(c, "-x^2 + 3x - 2 = 0", W / 2, 290, 80, a0, cores={0: AMBER})
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        pill(c, "× (−1)  nos dois lados", W / 2, 400, PURPLE, size=32, a=aa, anchor="center")
    ab = ep(t, C["10.b"], 0.5)
    expr(c, "x^2 - 3x + 2 = 0", W / 2, 520, 80, ab, cores={0: GREEN, 2: GREEN, 4: GREEN})
    acc = ep(t, C["10.c"], 0.5)
    K.atalho(c, 360, 620, 1200, 200, "ATALHO · a NEGATIVO? VEZES −1", ["todos os sinais viram · as raízes NÃO mudam",
                                                                         "0 · (−1) = 0"], acc, 32)


# ======================================================================
# bloco c — produto nulo e c = 0
# ======================================================================

def b_nulo(c, t, C, B):
    head_seq(c, t, C, [("11", "EQUAÇÃO INCOMPLETA", "O PRODUTO NULO", PURPLE), ("12", "c = 0", "x EM EVIDÊNCIA", PURPLE),
                       ("13", "ATALHO", "c = 0", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        if aa > 0:
            rrect(c, 360, 230, 1200, 110, 22, mix("#FFFFFF", BLUE, 0.10), aa)
            linha(c, [("INCOMPLETA", BLUE), (": falta o b ou falta o c (vale zero)", INK)], W / 2, 285, 34, aa)
        ab = ep(t, C["11.b"], 0.5)
        caixas(c, W / 2, 520, "?", "?", ab, ep(t, C["11.c"] + 1.0, 0.6), 0, 80)
        if ab > 0:
            regra(c, "se uma multiplicação deu zero, alguém ali é zero", W / 2, 740, ab, 36)
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        expr(c, "2x^2 - 10x = 0", W / 2, 270, 84, aa)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            pill(c, "2x nos dois termos", 1500, 270, PURPLE, size=26, a=ab, anchor="center")
        caixas(c, W / 2, 470, "2x", "(x-5)", ab, ep(t, C["12.c"] + 1.4, 0.5), ep(t, C["12.d"], 0.5), 70)
        acc = ep(t, C["12.c"] + 1.4, 0.5)
        if acc > 0:
            expr(c, "2x = 0  →  x = 0", 620, 680, 50, acc, cores={4: GREEN, 5: GREEN, 6: GREEN})
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            expr(c, "x - 5 = 0  →  x = 5", 1300, 680, 50, ad, cores={6: GREEN, 7: GREEN, 8: GREEN})
        conferido(c, "2 · 25 − 10 · 5 = 0", 700, 790, ep(t, C["12.e"], 0.5), True, 34)
        return
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 360, 250, 1200, 300, "ATALHO · QUANDO O c É ZERO", ["uma raiz é SEMPRE 0", ("m", "a outra: x = -b/a")], aa,
             40)
    ab = ep(t, C["13.b"], 0.5)
    expr(c, "x = -(-10)/2 = 5", W / 2, 680, 70, ab, cores={4: GREEN})


# ======================================================================
# bloco d — nunca divida por x
# ======================================================================

def b_dividir(c, t, C, B):
    head(c, t, B["start"], "NUNCA DIVIDA POR x", "A RAIZ QUE SOME", RED)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    expr(c, "2x^2 = 10x", 560, 290, 80, aa)
    if aa > 0:
        pill(c, "÷ x", 840, 290, AMBER, size=32, a=aa, anchor="center")
        expr(c, "→  2x = 10  →  x = 5", 1260, 290, 60, ep(t, C["14.a"] + 2.2, 0.4))
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        selo(c, 1500, 420, ab, "CADÊ O ZERO?", RED, -5, 36)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 470, 1000, 110, 22, mix("#FFFFFF", AMBER, 0.14), acc)
        linha(c, [("dividir por x supõe ", INK), ("x ≠ 0", AMBER)], 760, 525, 38, acc)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        regra(c, "jogou fora, sem perceber, a raiz zero", W / 2, 650, ad, 34, RED)
        ad2 = ep(t, C["14.d"] + 4.5, 0.5)
        expr(c, "2x^2 - 10x = 0  →  2x(x-5) = 0  →  x = 0  ou  x = 5", W / 2, 770, 42, ad2,
             cores={9: GREEN, 10: GREEN, 11: GREEN, 13: GREEN, 14: GREEN, 15: GREEN})


# ======================================================================
# bloco e — b = 0
# ======================================================================

def b_bzero(c, t, C, B):
    head_seq(c, t, C, [("15", "b = 0", "ISOLE O x² E USE ±", PURPLE), ("16", "x² NEGATIVO?", "SEM RAIZ REAL", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        rows = [(C["15.a"], "2x^2 - 50 = 0", ""),
                (C["15.b"], "2x^2 = 50", "+ 50 nos dois lados"),
                (C["15.b"] + 3.4, "x^2 = 25", "÷ 2 nos dois lados")]
        for k, (t0, ex, nota) in enumerate(rows):
            a, d = rise(t, t0)
            if a <= 0:
                continue
            y = 270 + k * 120 + d
            expr(c, ex, 300, y, 64, a, align="left")
            if nota:
                pill(c, nota, 1120, y, PURPLE, size=24, a=a, anchor="right")
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            terreno(c, 1440, 420, 220, acc, "25")
            rrect(c, 300, 600, 820, 110, 22, mix("#FFFFFF", GREEN, 0.14), acc)
            expr(c, "x = 5  ou  x = -5", 710, 655, 60, acc, cores={2: GREEN, 6: GREEN})
        ad = ep(t, C["15.d"], 0.5)
        if ad > 0:
            pill(c, "RAÍZES SIMÉTRICAS: mesmo número, sinais trocados", W / 2, 790, BLUE, size=28, a=ad, anchor="center")
        return
    aa = ep(t, C["16"], 0.5)
    expr(c, "x^2 + 9 = 0", 560, 290, 80, aa)
    expr(c, "→  x^2 = -9", 1200, 290, 80, ep(t, C["16.a"], 0.5), cores={2: RED})
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        expr(c, "3^2 = 9", 600, 450, 54, ab, cores={2: GREEN})
        expr(c, "(-3)^2 = 9", 1000, 450, 54, ab, cores={2: GREEN})
        fmid(c, "? ² = −9", 1400, 450, 54, "black", RED, ab)
    acc = ep(t, C["16.c"], 0.5) * (1 - ep(t, C["16.d"], 0.4))
    if acc > 0:
        selo(c, W / 2, 620, acc, "NÃO TEM RAIZ REAL", RED, -3, 44)
    ad = ep(t, C["16.d"], 0.5)
    K.atalho(c, 360, 540, 1200, 260, "ATALHO · QUANDO O b É ZERO", ["isole o x² e tire a raiz com ±",
                                                                     "deu negativo?  SEM RAIZ REAL"], ad, 34)


# ======================================================================
# bloco f — já vem fatorada
# ======================================================================

def b_fatorada(c, t, C, B):
    head(c, t, B["start"], "JÁ VEIO MULTIPLICADA?", "LEIA AS RAÍZES", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    caixas(c, W / 2, 330, "(x-2)", "(x+7)", aa, ep(t, C["17.b"] + 1.0, 0.5), ep(t, C["17.b"] + 4.2, 0.5), 70)
    a1 = ep(t, C["17.b"] + 1.0, 0.5)
    if a1 > 0:
        expr(c, "x = 2", 700, 560, 64, a1, cores={2: GREEN})
    a2 = ep(t, C["17.b"] + 4.2, 0.5)
    if a2 > 0:
        expr(c, "x = -7", 1220, 560, 64, a2, cores={2: GREEN})
    acc = ep(t, C["17.c"], 0.5) * (1 - ep(t, C["17.d"], 0.4))
    if acc > 0:
        pill(c, "sem conta nenhuma", W / 2, 680, GREEN, size=34, a=acc, anchor="center")
    ad = ep(t, C["17.d"], 0.5)
    K.atalho(c, 360, 640, 1200, 190, "ATALHO · LEIA COM O SINAL TROCADO", ["(x − 2) → 2  ·  (x + 7) → −7  ·  não desenvolva"],
             ad, 32)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E TENTE", GREEN), ("19", "VAMOS JUNTOS", "QUEM É ZERO: O b OU O c?", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    ab = ep(t, C["18.b"], 0.5)
    badge_num(c, 1, 300, 280, aa, 28, bg=PURPLE)
    expr(c, "x^2 - 49 = 0", 360, 280, 64, aa, align="left")
    badge_num(c, 2, 1000, 280, ab, 28, bg=PURPLE)
    expr(c, "2x^2 + 6x = 0", 1060, 280, 64, ab, align="left")
    if t < C["19"]:
        pause_timer(c, t, C["18.end"] - 1.9, W / 2, 560)
        return
    a1 = ep(t, C["19.a"], 0.5)
    if a1 > 0:
        pill(c, "b = 0", 600, 380, PURPLE, size=26, a=a1, anchor="center")
        expr(c, "x^2 = 49", 600, 480, 56, a1)
        expr(c, "x = 7  ou  x = -7", 600, 590, 52, ep(t, C["19.a"] + 3.0, 0.4), cores={2: GREEN, 6: GREEN})
    b1 = ep(t, C["19.b"], 0.5)
    if b1 > 0:
        pill(c, "c = 0", 1320, 380, PURPLE, size=26, a=b1, anchor="center")
        caixas(c, 1320, 480, "2x", "(x+3)", b1, ep(t, C["19.c"], 0.5), ep(t, C["19.c"] + 1.6, 0.5), 44, placa=False)
        expr(c, "x = 0  ou  x = -3", 1320, 610, 52, ep(t, C["19.c"], 0.4), cores={2: GREEN, 6: GREEN})
    conferido(c, "2 · 9 + 6 · (−3) = 18 − 18 = 0", 960, 760, ep(t, C["19.d"], 0.5), True, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Primeiro arrume: tudo de um lado, zero do outro.",
          "O sinal faz parte do coeficiente.",
          "Nunca divida por x: coloque x em evidência."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("x² − 7x + 10  →  b = 7", "o número que aparece escrito é o 7",
          "o sinal faz parte do coeficiente: b = −7"),
         ("2x² = 10x  →  ÷ x  →  só x = 5", "o 5 funciona na equação",
          "ao dividir por x, o zero sumiu: arrume e use a evidência → 0 e 5"),
         ("x² = 25  →  só x = 5", "a raiz de 25 é 5",
          "são duas respostas: 5 e −5 (só descarte o −5 se o contexto pedir)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questão 5 do material (você faz)
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS5 = [("A", "está correta, pois a única solução é 4.", "ignora a raiz perdida", RED),
         ("B", "está errada, pois as soluções são 2 e −2.", "resolveu 3x² = 12", RED),
         ("C", "está errada, pois as soluções são 4 e −4.", "± é do b = 0", RED),
         ("D", "está incompleta, pois faltou a solução −4.", "−4 não satisfaz", RED),
         ("E", "está incompleta, pois faltou a solução 0.", "", GREEN)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · VOCÊ FAZ", "A RAIZ QUE SUMIU", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4) * (1 - ep(t, C["25"], 0.4))
    yend = _enunciado(c, [("Para resolver a equação 3x² = 12x, um estudante dividiu os dois lados por 3x e concluiu que a "
                           "solução é x = 4. Sobre essa resolução, é correto afirmar que ela", INK)], a0, 250, 30)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["26.xa"], "B": C["26.xb"], "C": C["26.xc"], "D": C["26.xc"] + 1.2}
    K.alternativas(c, t, C, ALTS5, 1000, 240, 680, 28, C["25.ok"], "E", cues_in, cues_x, gap=26)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 110)
    if t >= C["25"]:
        ap = ep(t, C["25"], 0.4)
        rrect(c, 170, 230, 760, 600, 18, "#FFFFFF", ap, shadow=True)
        text(c, "ARRUME E COLOQUE x EM EVIDÊNCIA", 550, 285, 22, "black", PURPLE, ap, tracking=1)
        rows = [(C["25.a"], "3x^2 - 12x = 0"), (C["25.b"], "3x(x-4) = 0"), (C["25.c"], "x = 0  ou  x = 4")]
        for k, (t0, ex) in enumerate(rows):
            a, d = rise(t, t0)
            expr(c, ex, 550, 370 + k * 100 + d, 52, a, cores={2: GREEN, 6: GREEN} if k == 2 else None)
        ad = ep(t, C["25.d"], 0.5)
        if ad > 0:
            pill(c, "o ÷ 3x jogou fora o ZERO", 550, 680, RED, size=26, a=ad, anchor="center")
        af = ep(t, C["26.f"], 0.5)
        if af > 0:
            rrect(c, 200, 720, 700, 90, 18, mix("#FFFFFF", RED, 0.08), af)
            text(c, "x = −4:  3 · 16 = 48  ≠  12 · (−4) = −48", 550, 776, 26, "black", RED, af)
    axd = ep(t, C["26.xd"], 0.5)
    if axd > 0:
        pill(c, "aqui quem é zero é o c", 1340, 720, AMBER, size=24, a=axd, anchor="center")


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A FÓRMULA DE BHASKARA", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    expr(c, "2x^2 - 7x + 3 = 0", W / 2, 340, 100, aa)
    if aa > 0:
        pill(c, "completa · sem fator comum à vista", W / 2, 460, AMBER, size=30, a=aa, anchor="center")
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        rrect(c, 610, 540, 700, 130, 26, mix("#FFFFFF", PURPLE, 0.12), ab)
        fmid(c, "x = ?", W / 2, 605, 70, "black", PURPLE, ab)
    pill(c, "ep. 2 · uma fórmula que resolve todas", W / 2, 760, PURPLE, size=32, a=ep(t, C["28.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Você já tinha dividido por x alguma vez?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, definicao=b_definicao,
              arrumar=b_arrumar, nulo=b_nulo, dividir=b_dividir, bzero=b_bzero, fatorada=b_fatorada,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q5=b_q5, ponte=b_ponte, cta=b_cta)
