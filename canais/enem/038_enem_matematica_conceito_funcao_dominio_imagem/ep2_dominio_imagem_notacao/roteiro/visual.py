"""Visual — Conceito de Função, Episódio 2: domínio, contradomínio, imagem e a notação f(x) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: maquina() (máquina de refrigerante: fenda de moedas R$ 1, 2 e 5, painel de 6 sabores com 2 esgotados e a
bandeja de saída), baloes() (A → B com flechas; o elemento que nunca sai fica apagado e a imagem é "recortada" de dentro de B),
cadeira() (a fórmula com o x trocado por um parêntese vazio onde a entrada "senta", com parênteses).
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
_s = importlib.util.spec_from_file_location("comum038", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_ep2_dominio_imagem_notacao.mp4"
CARD_R = K.CARD_R
CHAPA = "#D9473F"
CHAPA2 = "#B23A33"
SABORES = ["#E8A33D", "#7DBE5C", "#C0504D", "#8E6CC2", "#3C8DD6", "#E07BA6"]


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


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def moeda(c, cx, cy, r, s, a, col="#E2B23C", riscada=0.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(col, a))
    c.drawCircle(cx, cy, r * 0.82, paint("#FFFFFF", a * 0.35, stroke=3))
    fmid(c, s, cx, cy, r * 0.62, "black", INK, a)
    if riscada > 0:
        line(c, cx - r, cy - r, cx + r, cy + r, RED, a * riscada, 7)


def maquina(c, cx, cy, a, esgota=0.0, esc=1.0, moedas=True):
    """máquina de refrigerante vista de frente, centro (cx, cy). esgota (0→1): 2 botões ficam cinza com 'ESGOTADO'."""
    if a <= 0:
        return
    e = esc
    w, h = 520 * e, 760 * e
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(c, x0, y0, w, h, 36 * e, CHAPA, a, shadow=True)
    rrect(c, x0 + 24 * e, y0 + 24 * e, w - 48 * e, 90 * e, 20 * e, CHAPA2, a)
    text_mid(c, "REFRI", cx, y0 + 69 * e, 50 * e, "black", "#FFFFFF", a, tracking=6)
    # painel de 6 sabores (2 colunas × 3 linhas)
    for k in range(6):
        col_, row = k % 2, k // 2
        bx = x0 + 50 * e + col_ * 220 * e
        by = y0 + 150 * e + row * 140 * e
        off = k in (2, 5)
        fill = mix(SABORES[k], "#9AA0A6", 0.85 * esgota) if off else SABORES[k]
        rrect(c, bx, by, 200 * e, 116 * e, 20 * e, "#FFFFFF", a)
        rrect(c, bx + 14 * e, by + 14 * e, 60 * e, 88 * e, 14 * e, fill, a)
        text_mid(c, f"sabor {k + 1}", bx + 138 * e, by + 58 * e, 26 * e, "black", GRAY if off and esgota > 0.5 else INK, a)
        if off and esgota > 0:
            c.save(); c.translate(bx + 100 * e, by + 58 * e); c.rotate(-12)
            rrect(c, -92 * e, -22 * e, 184 * e, 44 * e, 10 * e, RED, a * esgota)
            text_mid(c, "ESGOTADO", 0, 0, 24 * e, "black", "#FFFFFF", a * esgota, tracking=2)
            c.restore()
    # fenda de moedas e bandeja
    rrect(c, x0 + w - 120 * e, y0 + 590 * e, 70 * e, 16 * e, 8 * e, INK, a)
    rrect(c, x0 + 60 * e, y0 + 640 * e, 300 * e, 80 * e, 18 * e, "#3B3F45", a)
    text_mid(c, "SAÍDA", x0 + 210 * e, y0 + 680 * e, 24 * e, "black", "#FFFFFF", a * 0.8, tracking=3)
    if moedas:
        for k, s in enumerate(("R$ 1", "R$ 2", "R$ 5")):
            moeda(c, x0 + w + 110 * e, y0 + 430 * e + k * 110 * e, 46 * e, s, a)


def balao(c, cx, cy, rx, ry, rot, col, a, dash=False):
    if a <= 0:
        return
    rect = skia.Rect.MakeLTRB(cx - rx, cy - ry, cx + rx, cy + ry)
    if not dash:
        c.drawOval(rect, paint(mix("#FFFFFF", col, 0.08), a))
    p = paint(col, a, stroke=5)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make([18, 12], 0))
    c.drawOval(rect, p)
    text(c, rot, cx, cy - ry - 22, 36, "black", col, a)


def baloes(c, t, cx, cy, a, A, B, f, t_fl, t_apaga=1e9, t_recorta=1e9, esc=1.0, rotA="A", rotB="B", t_x=None):
    """balão A (esquerda) e B (direita), flechas x → f(x) que entram nos instantes t_fl[k]; quem nunca sai apaga em t_apaga
    (etiqueta "no cardápio, mas nunca sai"); em t_recorta um balão menor tracejado (a imagem) contorna o que saiu."""
    if a <= 0:
        return
    e = esc
    xa, xb = cx - 380 * e, cx + 380 * e
    ra, rb = 150 * e, 170 * e
    ha = max(len(A), len(B)) * 78 * e / 2 + 50 * e
    balao(c, xa, cy, ra, ha, rotA, BLUE, a)
    balao(c, xb, cy, rb, ha, rotB, PURPLE, a)
    ya = {x: cy - (len(A) - 1) * 78 * e / 2 + k * 78 * e for k, x in enumerate(A)}
    yb = {y: cy - (len(B) - 1) * 78 * e / 2 + k * 78 * e for k, y in enumerate(B)}
    saem = {f(x) for x in A}
    ap = ep(t, t_apaga, 0.6)
    for x in A:
        fmid(c, str(x).replace("-", "−"), xa, ya[x], 46 * e, "black", INK, a)
    for y in B:
        nunca = y not in saem
        fmid(c, str(y).replace("-", "−"), xb, yb[y], 46 * e, "black", mix(INK, "#C8CCD0", ap) if nunca else INK, a)
    for k, x in enumerate(A):
        af = ep(t, t_fl[k], 0.6)
        if af > 0:
            arrow(c, xa + 40 * e, ya[x], xb - 44 * e, yb[f(x)], GREEN, a * af, 4, 14, progress=af)
    ar = ep(t, t_recorta, 0.8)
    an = ap * (1 - ar) if t_recorta > t_apaga else ap
    if an > 0:
        nunca = [str(y) for y in B if y not in saem]
        s_ = f"{', '.join(nunca)}: no cardápio, mas nunca sai" + ("m" if len(nunca) > 1 else "")
        pill(c, s_, xb, cy + ha + 34 * e, AMBER, size=int(24 * e), a=a * an, anchor="center", bounds=(0, 1920))
    if ar > 0:
        ys = sorted(yb[y] for y in saem)
        rect_h = (ys[-1] - ys[0]) / 2 + 52 * e
        balao(c, xb, (ys[0] + ys[-1]) / 2, 90 * e, rect_h, "", GREEN, a * ar, dash=True)
        yl = cy + ha + (84 if an > 0 else 34) * e
        pill(c, "IMAGEM", xb, yl, GREEN, size=int(26 * e), a=a * ar, anchor="center")


def slot(c, conteudo, x, cy, size, a, col, cheio=1.0):
    """o parêntese da cadeira vazia: '(' [caixa tracejada] ')'. Devolve a largura usada."""
    wc = max(size * 0.9, K.math_w(conteudo, size) + size * 0.3) if conteudo else size * 0.9
    wp = ftext_w("(", "black", size)
    fmid(c, "(", x, cy, size, "black", INK, a, align="left")
    bx = x + wp + 4
    r = skia.Rect.MakeXYWH(bx, cy - size * 0.55, wc, size * 1.1)
    p = paint(AMBER, a * (1 - cheio * 0.6), stroke=3)
    p.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    c.drawRoundRect(r, 10, 10, p)
    if conteudo and cheio > 0:
        expr(c, conteudo, bx + wc / 2, cy, size, a * cheio, cores={i: col for i in range(6)})
    fmid(c, ")", bx + wc + 4, cy, size, "black", INK, a, align="left")
    return wp + 8 + wc + wp


def cadeira(c, conteudo, cx, cy, size, a, col=AMBER, cheio=1.0):
    """f( ▢ ) = ( ▢ )² − 1, com o mesmo conteúdo nas duas cadeiras"""
    if a <= 0:
        return
    pecas_w = (ftext_w("f", "black", size) + ftext_w(" = ", "black", size) + ftext_w("² − 1", "black", size))
    wc = max(size * 0.9, K.math_w(conteudo, size) + size * 0.3) if conteudo else size * 0.9
    tot = pecas_w + 2 * (2 * ftext_w("(", "black", size) + 8 + wc)
    x = cx - tot / 2
    fmid(c, "f", x, cy, size, "black", PURPLE, a, align="left")
    x += ftext_w("f", "black", size)
    x += slot(c, conteudo, x, cy, size, a, col, cheio)
    fmid(c, " = ", x, cy, size, "black", INK, a, align="left")
    x += ftext_w(" = ", "black", size)
    x += slot(c, conteudo, x, cy, size, a, col, cheio)
    fmid(c, "² − 1", x, cy, size, "black", INK, a, align="left")


def passos(c, t, rows, x, y0, size, dy, xnota=1660):
    """linhas da conta: rows = [(instante, expr, nota, cor_da_nota)]"""
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
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÕES · EPISÓDIO 2", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    expr(c, "f(x) = x^2 - 1", W / 2, 300, 90, aa, cores={0: PURPLE})
    expr(c, "f(2+3) = ?", W / 2, 430, 80, ep(t, C["01.a"] + 2.6, 0.5), cores={2: AMBER})
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 200, 530, 700, 200, 26, mix("#FFFFFF", RED, 0.10), ab)
        expr(c, "f(2) + f(3) = 3 + 8", 550, 600, 52, ab)
        check_icon(c, 300, 680, 28, ab, RED, "x")
        fmid(c, "= 11 ?", 560, 680, 52, "black", RED, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 530, 700, 200, 26, mix("#FFFFFF", GREEN, 0.14), acc)
        expr(c, "f(2+3) = f(5)", 1370, 600, 52, acc)
        check_icon(c, 1120, 680, 28, acc, GREEN)
        fmid(c, "= 24", 1380, 680, 56, "black", GREEN, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        pill(c, "por que tão diferentes?", W / 2, 830, AMBER, size=34, a=ad, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "separar domínio, contradomínio e imagem", "o que entra · o cardápio · o que sai"),
            ("02.b", "calcular f de qualquer coisa", "a fórmula vira uma máquina"),
            ("02.c", "de um negativo, de 2x, de x + 1", "f(−2)  ·  f(2x)  ·  f(x + 1)")]
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
        text(c, "O PARÊNTESE DO NEGATIVO", 560, 280, 32, "black", PURPLE, aa)
        text(c, "série de Potenciação", 560, 324, 24, "bold", GRAY, aa)
        expr(c, "(-2)^2 = +4", 560, 470, 76, ep(t, C["03.a"] + 1.0, 0.4), cores={2: GREEN})
        expr(c, "-2^2 = -4", 560, 620, 76, ep(t, C["03.a"] + 4.6, 0.4), cores={2: RED})
        pill(c, "sem parênteses, o ² pega só o 2", 560, 710, AMBER, size=24, a=ep(t, C["03.a"] + 4.6, 0.4),
             anchor="center")
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "O QUADRADO DA SOMA", 1360, 280, 32, "black", BLUE, ab)
        text(c, "série de Expressões Algébricas", 1360, 324, 24, "bold", GRAY, ab)
        expr(c, "(x+1)^2", 1360, 460, 76, ab)
        expr(c, "= x^2 + 2x + 1", 1360, 580, 66, ep(t, C["03.b"] + 2.0, 0.4), cores={3: GREEN})
        ar = ep(t, C["03.b"] + 4.2, 0.4)
        if ar > 0:
            expr(c, "x^2 + 1", 1360, 690, 50, ar, cores={0: GRAY, 1: GRAY, 2: GRAY})
            strike(c, 1270, 690, 1450, 690, ar, RED)
    line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)


# ======================================================================
# concreto: a máquina de refrigerante
# ======================================================================

def b_maquina(c, t, C, B):
    head(c, t, B["start"], "UMA MÁQUINA DE REFRIGERANTE", "TRÊS LISTAS", BLUE)
    a0 = ep(t, C["04"], 0.5)
    maquina(c, 640, 560, a0, ep(t, C["04.c"], 0.8), esc=0.88)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        moeda(c, 1120, 760, 40, "50¢", aa, "#B8BCC2", ep(t, C["04.a"] + 2.6, 0.4))
        pill(c, "não entra", 1120, 830, RED, size=22, a=ep(t, C["04.a"] + 2.6, 0.4), anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    rows = [("O QUE PODE ENTRAR", "moedas de R$ 1, R$ 2 e R$ 5", BLUE),
            ("O QUE APARECE NO PAINEL", "os 6 sabores", PURPLE),
            ("O QUE REALMENTE SAI", "só 4 sabores", GREEN)]
    for k, (tit, s, col) in enumerate(rows):
        a = ad * ep(t, C["04.d"] + 1.4 + 1.1 * k, 0.4)
        if a <= 0:
            continue
        y = 300 + k * 170
        rrect(c, 1240, y, 520, 130, 22, mix("#FFFFFF", col, 0.10), a)
        rrect(c, 1240, y, 12, 130, 6, col, a)
        text(c, tit, 1275, y + 52, 26, "black", col, a, align="left", tracking=1)
        text(c, s, 1275, y + 100, 30, "bold", INK, a, align="left")


# ======================================================================
# bloco a — os três conjuntos
# ======================================================================

def b_conjuntos(c, t, C, B):
    head_seq(c, t, C, [("05", "OS TRÊS CONJUNTOS", "DE UMA FUNÇÃO f : A → B", BLUE),
                       ("06", "A IMAGEM CABE NO CARDÁPIO", "Im(f) ⊂ CD(f)", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            linha(c, [("f : A → B", PURPLE)], W / 2, 270, 70, aa)
            text(c, "cada elemento de A vai para um elemento de B", W / 2, 340, 28, "bold", GRAY, aa)
        rows = [("05.b", "DOMÍNIO", "D(f) = A", "tudo o que PODE entrar", BLUE),
                ("05.c", "CONTRADOMÍNIO", "CD(f) = B", "o cardápio: onde as saídas são procuradas", PURPLE),
                ("05.d", "IMAGEM", "Im(f)", "o que REALMENTE sai da cozinha", GREEN)]
        for k, (cue, tit, sym, s, col) in enumerate(rows):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 400 + k * 140 + d
            rrect(c, 240, y, 1440, 116, 22, mix("#FFFFFF", col, 0.08), a)
            rrect(c, 240, y, 12, 116, 6, col, a)
            text(c, tit, 290, y + 50, 34, "black", col, a, align="left")
            ftext(c, sym, 290, y + 94, 28, "bold", INK2, a, align="left")
            text(c, s, 1640, y + 72, 32, "bold", INK, a, align="right")
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        balao(c, W / 2, 470, 420, 220, "CONTRADOMÍNIO · o cardápio", PURPLE, aa)
        balao(c, W / 2 - 60, 490, 200, 120, "", GREEN, aa * ep(t, C["06.a"] + 0.8, 0.6), dash=True)
        text_mid(c, "IMAGEM", W / 2 - 60, 490, 40, "black", GREEN, aa * ep(t, C["06.a"] + 0.8, 0.6))
        pill(c, "a cozinha não inventa prato", W / 2 + 250, 620, AMBER, size=24, a=ep(t, C["06.a"] + 2.0, 0.4),
             anchor="center")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        linha(c, [("Im(f) ", GREEN), ("⊂", AMBER), (" CD(f)", PURPLE)], W / 2, 770, 64, ab)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        pill(c, "⊂  lê-se “está contido em”", 1500, 770, BLUE, size=28, a=acc, anchor="center")


# ======================================================================
# bloco b — o exemplo da seção 04
# ======================================================================

def b_exemplo(c, t, C, B):
    head_seq(c, t, C, [("07", "f(x) = x²", "A = {1, 2, 3} · B = {1, 4, 7, 9}", BLUE),
                       ("08", "A IMAGEM", "Im = {1, 4, 9}", GREEN)])
    card(c, *CARD_R)
    a0 = ep(t, C["07.a"], 0.5)
    sid = which(t, C, ["07", "08"])
    baloes(c, t, 760, 520, a0, [1, 2, 3], [1, 4, 7, 9], lambda x: x * x,
           [C["07.b"], C["07.c"], C["07.d"]], C["07.e"], C["08.b"], esc=0.95, rotA="A · domínio", rotB="B · cardápio")
    expr(c, "f(x) = x^2", 1560, 300, 60, a0, cores={0: PURPLE})
    for k, cue in enumerate(("07.b", "07.c", "07.d")):
        x = k + 1
        expr(c, f"f({x}) = {x * x}", 1560, 400 + k * 80, 46, ep(t, C[cue], 0.4), cores={2: GREEN})
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5) * (1 - ep(t, C["08.c"], 0.4))
        if aa > 0:
            rrect(c, 1360, 650, 400, 110, 22, mix("#FFFFFF", GREEN, 0.14), aa)
            fmid(c, "Im = {1, 4, 9}", 1560, 705, 44, "black", GREEN, aa)
        K.atalho(c, 1300, 620, 540, 190, "ATALHO · DOMÍNIO EM LISTA",
                 ["calcule cada entrada", "risque as repetidas"], ep(t, C["08.c"], 0.5), 30)


# ======================================================================
# bloco c — imagem e pré-imagem
# ======================================================================

def b_preimagem(c, t, C, B):
    head(c, t, B["start"], "IMAGEM E PRÉ-IMAGEM", "UMA FLECHA, DOIS NOMES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.5)
    if a0 <= 0:
        return
    c.drawCircle(560, 480, 90, paint(mix("#FFFFFF", BLUE, 0.12), a0))
    c.drawCircle(1360, 480, 90, paint(mix("#FFFFFF", PURPLE, 0.12), a0))
    fmid(c, "3", 560, 480, 90, "black", BLUE, a0)
    fmid(c, "9", 1360, 480, 90, "black", PURPLE, a0)
    af = ep(t, C["09.a"], 0.8)
    arrow(c, 670, 480, 1250, 480, GREEN, a0, 7, 24, progress=af)
    pill(c, "f", W / 2, 430, PURPLE, size=32, a=af, anchor="center")
    aa = ep(t, C["09.a"] + 0.6, 0.5)
    if aa > 0:
        rrect(c, 1160, 610, 400, 120, 22, mix("#FFFFFF", PURPLE, 0.10), aa)
        text(c, "9 é a IMAGEM de 3", 1360, 685, 32, "black", PURPLE, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 610, 400, 120, 22, mix("#FFFFFF", BLUE, 0.10), ab)
        text(c, "3 é a PRÉ-IMAGEM de 9", 560, 685, 30, "black", BLUE, ab)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        pill(c, "partida", 560, 330, BLUE, size=28, a=acc, anchor="center")
        pill(c, "chegada", 1360, 330, PURPLE, size=28, a=acc, anchor="center")


# ======================================================================
# bloco d — a notação f(x)
# ======================================================================

def b_notacao(c, t, C, B):
    head(c, t, B["start"], "A NOTAÇÃO f(x)", "LÊ-SE “f DE x”", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        fmid(c, "f", 560, 400, 200, "black", PURPLE, aa)
        pill(c, "o NOME da máquina", 560, 560, PURPLE, size=30, a=aa, anchor="center")
        pill(c, "não é número multiplicando", 560, 630, RED, size=24, a=ep(t, C["10.a"] + 1.6, 0.4), anchor="center")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        fmid(c, "( 3 )", 960, 400, 140, "black", BLUE, ab)
        pill(c, "o que ENTRA", 960, 560, BLUE, size=30, a=ab, anchor="center")
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        fmid(c, "= ?", 1350, 400, 140, "black", GREEN, acc)
        pill(c, "o que SAI · valor numérico", 1350, 560, GREEN, size=30, a=acc, anchor="center")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 690, 1200, 120, 24, mix("#FFFFFF", PURPLE, 0.08), ad)
        expr(c, "f(3) = (3)^2 - 1 = 9 - 1 = 8", W / 2, 750, 54, ad, cores={10: GREEN})


# ======================================================================
# bloco d — a cadeira vazia
# ======================================================================

def b_cadeira(c, t, C, B):
    head_seq(c, t, C, [("11", "A CADEIRA VAZIA", "f(−2)", AMBER), ("12", "A CADEIRA VAZIA", "f(3x)", AMBER),
                       ("13", "A CADEIRA VAZIA", "f(x + 1)", AMBER), ("14", "ATALHO", "TESTE COM x = 1", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13", "14"])
    expr(c, "f(x) = x^2 - 1", W / 2, 250, 56, ep(t, C["11"], 0.5), cores={0: PURPLE})
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        cheio = ep(t, C["11.b"] + 0.6, 0.6)
        cadeira(c, "-2", W / 2, 400, 92, aa, BLUE, cheio)
        if aa > 0 and cheio <= 0:
            pill(c, "o x sai: fica a cadeira vazia", W / 2, 500, AMBER, size=26, a=aa, anchor="center")
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            pill(c, "senta COM os parênteses", W / 2, 500, AMBER, size=28, a=ab, anchor="center")
        rows = [(C["11.c"], "f(-2) = (-2)^2 - 1", "", None),
                (C["11.d"], "= 4 - 1 = 3", "(−2)² = +4", GREEN)]
        passos(c, t, rows, 560, 610, 64, 110, xnota=1560)
        return
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        cadeira(c, "3x", W / 2, 400, 92, aa, BLUE, ep(t, C["12.a"] + 0.8, 0.6))
        rows = [(C["12.a"] + 2.0, "f(3x) = (3x)^2 - 1", "", None),
                (C["12.b"], "= 9x^2 - 1", "o ² pega o 3 e o x", PURPLE)]
        passos(c, t, rows, 560, 560, 64, 120, xnota=1600)
        acc = ep(t, C["12.c"], 0.5)
        if acc > 0:
            rrect(c, 560, 720, 800, 100, 22, mix("#FFFFFF", GREEN, 0.14), acc)
            expr(c, "f(3x) = 9x^2 - 1", W / 2, 770, 54, acc, cores={2: GREEN, 3: GREEN, 4: GREEN})
        return
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        cadeira(c, "x + 1", W / 2, 400, 92, aa, BLUE, ep(t, C["13.a"] + 0.8, 0.6))
        rows = [(C["13.b"], "= x^2 + 2x + 1 - 1", "quadrado da soma", BLUE),
                (C["13.c"], "= x^2 + 2x", "+1 − 1 = 0", GREEN)]
        passos(c, t, rows, 520, 560, 64, 130, xnota=1640)
        return
    aa = ep(t, C["14.a"], 0.5)
    K.atalho(c, 260, 300, 1400, 170, "ATALHO · CONFIRA A SUBSTITUIÇÃO", ["teste com x = 1"], aa, 40)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 510, 660, 200, 22, "#FFFFFF", ab, shadow=True)
        text(c, "NA FÓRMULA ORIGINAL", 590, 560, 22, "black", GRAY, ab, tracking=2)
        expr(c, "f(1+1) = f(2) = 3", 590, 640, 50, ab, cores={4: GREEN})
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 510, 660, 200, 22, "#FFFFFF", acc, shadow=True)
        text(c, "NA RESPOSTA", 1330, 560, 22, "black", GRAY, acc, tracking=2)
        expr(c, "1^2 + 2·1 = 3", 1330, 640, 50, acc, cores={4: GREEN})
        conferido(c, "bateu", 1210, 770, acc, True, 40)
    ad = ep(t, C["14.d"], 0.5)
    if ad > 0:
        pill(c, "não bateu? errou em algum lugar", 590, 770, AMBER, size=26, a=ad, anchor="center")


# ======================================================================
# bloco e — f(a + b) não é f(a) + f(b) · f(3x) não é 3·f(x)
# ======================================================================

def b_soma(c, t, C, B):
    head_seq(c, t, C, [("15", "A MÁQUINA NÃO DISTRIBUI", "f(a + b) ≠ f(a) + f(b)", PURPLE),
                       ("16", "O f NÃO É NÚMERO", "f(3x) ≠ 3 · f(x)", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            rrect(c, 220, 260, 700, 470, 26, mix("#FFFFFF", GREEN, 0.10), aa)
            text(c, "SOME PRIMEIRO", 570, 320, 26, "black", GREEN, aa, tracking=2)
            expr(c, "f(2+3)", 570, 410, 64, aa)
            expr(c, "= f(5)", 570, 510, 64, ep(t, C["15.a"] + 2.2, 0.4))
            expr(c, "= 25 - 1 = 24", 570, 610, 64, ep(t, C["15.a"] + 4.0, 0.4), cores={5: GREEN})
            pill(c, "a máquina trabalha 1 vez", 570, 690, GREEN, size=24, a=ep(t, C["15.a"] + 4.0, 0.4),
                 anchor="center")
        ab = ep(t, C["15.b"], 0.5)
        if ab > 0:
            rrect(c, 1000, 260, 700, 470, 26, mix("#FFFFFF", AMBER, 0.12), ab)
            text(c, "OUTRA PERGUNTA", 1350, 320, 26, "black", AMBER, ab, tracking=2)
            expr(c, "f(2) + f(3)", 1350, 410, 64, ab)
            expr(c, "= 3 + 8 = 11", 1350, 510, 64, ep(t, C["15.b"] + 2.0, 0.4), cores={5: AMBER})
            pill(c, "a máquina trabalha 2 vezes", 1350, 690, AMBER, size=24, a=ep(t, C["15.b"] + 2.0, 0.4),
                 anchor="center")
        acc = ep(t, C["15.c"], 0.5)
        if acc > 0:
            regra(c, "a máquina NÃO distribui: 24 ≠ 11", W / 2, 800, acc, 36)
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        fmid(c, "f", 400, 400, 170, "black", PURPLE, aa)
        pill(c, "nome da máquina", 400, 530, PURPLE, size=26, a=aa, anchor="center")
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        rrect(c, 700, 290, 960, 110, 22, mix("#FFFFFF", RED, 0.08), ab)
        expr(c, "3 · f(x) = 3x^2 - 3", 1180, 345, 54, ab, cores={0: RED})
        rrect(c, 700, 430, 960, 110, 22, mix("#FFFFFF", GREEN, 0.12), ab)
        expr(c, "f(3x) = 9x^2 - 1", 1180, 485, 54, ep(t, C["16.b"] + 2.0, 0.4), cores={2: GREEN, 3: GREEN, 4: GREEN})
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        pill(c, "TESTE COM x = 1", W / 2, 620, GREEN, size=28, a=acc, anchor="center")
        expr(c, "f(3) = 8", 700, 730, 60, acc, cores={2: GREEN})
        fmid(c, "≠", W / 2, 730, 70, "black", RED, acc)
        expr(c, "3 · f(1) = 0", 1220, 730, 60, acc, cores={4: RED})


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "IMAGEM DE g", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    expr(c, "g(x) = 2x + 1", 480, 270, 60, aa, cores={0: PURPLE})
    ftext(c, "D = {0, 1, 2}", 480, 360, 40, "black", BLUE, aa)
    ftext(c, "CD = {0, 1, 2, 3, 4, 5}", 480, 420, 40, "black", PURPLE, aa)
    ab = ep(t, C["17.b"], 0.5) * (1 - ep(t, C["18"], 0.3))
    if ab > 0:
        fmid(c, "Im = ?", 1300, 340, 80, "black", AMBER, ab)
    pause_timer(c, t, C["17.end"] - 1.9, 1300, 560)
    if t < C["18"]:
        return
    baloes(c, t, 1260, 560, ep(t, C["18"], 0.4), [0, 1, 2], [0, 1, 2, 3, 4, 5], lambda x: 2 * x + 1,
           [C["18.a"], C["18.b"], C["18.c"]], C["18.e"], C["18.d"], esc=0.62, rotA="D", rotB="CD")
    for k, (cue, s) in enumerate((("18.a", "g(0) = 2·0 + 1 = 1"), ("18.b", "g(1) = 2·1 + 1 = 3"),
                                  ("18.c", "g(2) = 2·2 + 1 = 5"))):
        expr(c, s, 480, 520 + k * 80, 42, ep(t, C[cue], 0.4), cores={6: GREEN})
    ad = ep(t, C["18.d"], 0.5)
    if ad > 0:
        rrect(c, 230, 760, 500, 80, 20, mix("#FFFFFF", GREEN, 0.14), ad)
        fmid(c, "Im = {1, 3, 5}", 480, 800, 40, "black", GREEN, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Domínio é o que entra; imagem é o que realmente sai.",
          "A imagem é parte do contradomínio, não necessariamente ele todo.",
          "Substitua o x pelo que estiver entre parênteses, com parênteses."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("imagem = contradomínio", "os dois ficam do lado da saída",
          "contradomínio é o cardápio inteiro; imagem é só o que sai (pode ser menor)"),
         ("f(3x) = 3 · f(x)", "o f parece um número multiplicando o parêntese",
          "o f é o nome da máquina: o 3x ENTRA nela → f(3x) = 9x² − 1"),
         ("f(a + b) = f(a) + f(b)", "lembra a propriedade distributiva",
          "a máquina não distribui: some primeiro, depois aplique → f(5) = 24"),
         ("f(−2) = −2² − 1 = −5", "os números são os mesmos",
          "ponha o parêntese ANTES de calcular: (−2)² − 1 = 3")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22", "23"], ERROS)


# ======================================================================
# questões 4 e 7 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=720):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS4 = [("A", "{0, 1, 2, 3, 4, 5}", "é o contradomínio", RED),
         ("B", "{0, 1, 4}", "", GREEN),
         ("C", "{−2, −1, 0, 1, 2}", "é o domínio", RED),
         ("D", "{1, 4}", "esqueceu g(0) = 0", RED),
         ("E", "{−4, −1, 0, 1, 4}", "−2² sem parênteses", RED)]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO, VOCÊ CONFERE", "IMAGEM NUM CONJUNTO FINITO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4) * (1 - ep(t, C["25"], 0.4))
    yend = _enunciado(c, [("Considere a função g: A → B, com A = {−2, −1, 0, 1, 2}, B = {0, 1, 2, 3, 4, 5} e g(x) = x². "
                           "A imagem de g é", INK)], a0, 270, 32)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS4, 1000, 270, 680, 34, C["25.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 120)
    if t >= C["25"]:
        ap = ep(t, C["25"], 0.4)
        _painel(c, ap)
        text(c, "calcule cada entrada", 550, 285, 28, "black", GRAY, ap)
        rows = [("25.a", "g(-2) = (-2)^2 = 4"), ("25.b", "g(-1) = 1"), ("25.b", "g(0) = 0"), ("25.c", "g(1) = 1"),
                ("25.c", "g(2) = 4")]
        for k, (cue, s) in enumerate(rows):
            off = 1.4 if k in (2, 4) else 0
            expr(c, s, 240, 360 + k * 70, 40, ep(t, C[cue] + off, 0.4), align="left")
        ad = ep(t, C["25.d"], 0.5)
        if ad > 0:
            text(c, "saíram: 4, 1, 0, 1, 4", 550, 730, 30, "black", INK2, ad)
            pill(c, "risque as repetidas", 550, 785, AMBER, size=24, a=ad, anchor="center")
        ae = ep(t, C["25.e"], 0.5)
        if ae > 0:
            rrect(c, 640, 330, 260, 90, 18, mix("#FFFFFF", GREEN, 0.16), ae)
            fmid(c, "{0, 1, 4}", 770, 375, 40, "black", GREEN, ae)
    ax = ep(t, C["26.xe"] + 2.6, 0.5)
    if ax > 0:
        pill(c, "−4 nem está em B: a cozinha não inventa prato", 1340, 820, AMBER, size=22, a=ax, anchor="center")


ALTS7 = [("A", "=2x^2 - 1", "o ² pegou só o x", RED),
         ("B", "=2x^2 - 2", "2 · f(x)", RED),
         ("C", "=4x^2 - 1", "", GREEN),
         ("D", "=4x^2 - 4", "4 · f(x)", RED),
         ("E", "=4x^2 - 4x + 1", "(2x − 1)²", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · VOCÊ FAZ", "SUBSTITUIR UMA EXPRESSÃO", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4) * (1 - ep(t, C["28"], 0.4))
    yend = _enunciado(c, [("Dada a função f(x) = x² − 1, a expressão de f(2x) é", INK)], a0, 290, 36)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    ap0 = ep(t, C["27.p"], 0.4) * (1 - ep(t, C["28"], 0.4))
    if ap0 > 0:
        cadeira(c, "", 540, yend + 60, 52, ap0)
        pill(c, "use a cadeira vazia", 540, yend + 140, AMBER, size=26, a=ap0, anchor="center")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS7, 1000, 270, 680, 36, C["28.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["27.end"] - 2.4, 540, yend + 300, dur=2.0)
    if t >= C["28"]:
        ap = ep(t, C["28"], 0.4)
        _painel(c, ap)
        cadeira(c, "2x", 550, 330, 56, ep(t, C["28.a"], 0.5), BLUE, ep(t, C["28.a"] + 0.6, 0.5))
        rows = [(C["28.a"] + 2.0, "f(2x) = (2x)^2 - 1", "", None),
                (C["28.b"], "= 4x^2 - 1", "", None)]
        passos(c, t, rows, 240, 450, 50, 90)
        acc = ep(t, C["28.c"], 0.5)
        if acc > 0:
            rrect(c, 200, 620, 700, 180, 18, mix("#FFFFFF", GREEN, 0.10), acc)
            text(c, "TESTE COM x = 1", 550, 665, 22, "black", GREEN, acc, tracking=2)
            expr(c, "f(2) = 4 - 1 = 3", 550, 720, 44, acc, cores={6: GREEN})
            text(c, "A = 1 · B = 0 · C = 3 · D = 0 · E = 1", 550, 780, 26, "black", INK2, acc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "O CAMINHO DE VOLTA", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 280, 620, 220, 26, "#FFFFFF", aa, shadow=True)
        text(c, "ATÉ AQUI", 530, 330, 24, "black", GRAY, aa, tracking=2)
        linha(c, [("entrada ", BLUE), ("→", INK), (" saída ?", GREEN)], 530, 420, 54, aa)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 280, 700, 220, 26, "#FFFFFF", ab, shadow=True)
        text(c, "“PAGUEI R$ 30,00 NO TÁXI”", 1350, 340, 30, "black", INK, ab)
        linha(c, [("? km ", AMBER), ("←", INK), (" R$ 30", GREEN)], 1350, 430, 54, ab)
    pill(c, "ep. 3 · o caminho de volta", W / 2, 680, PURPLE, size=34, a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Qual desses 4 erros você já cometeu?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, maquina=b_maquina, conjuntos=b_conjuntos,
              exemplo=b_exemplo, preimagem=b_preimagem, notacao=b_notacao, cadeira=b_cadeira, soma=b_soma,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q7=b_q7, ponte=b_ponte, cta=b_cta)
