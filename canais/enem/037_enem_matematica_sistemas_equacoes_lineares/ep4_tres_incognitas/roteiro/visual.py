"""Visual — Sistemas de Equações Lineares, Episódio 4: três incógnitas, a escada e o atalho da soma (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: boneco() e balanca() (três amigos subindo em duplas na balança de farmácia), pilha() (as três
pesagens somadas: cada bonequinho aparece duas vezes e a pilha se divide ao meio), escada() própria (o sistema escalonado
em degraus, com z = 3 embaixo e setas subindo), fichas de combo com as letras A, B, C contadas.
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
_s = importlib.util.spec_from_file_location("comum037", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w, expr = K.fmid, K.ftext, K.ftext_w, K.expr

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_sistemas_ep4_tres_incognitas.mp4"
CARD_R = K.CARD_R

# cores das pessoas / lanches (identidade, não função)
P_COR = {"Ana": "#E0731F", "Beto": "#2A9D8F", "Caio": "#C2185B",
         "A": "#E0731F", "B": "#2A9D8F", "C": "#C2185B"}


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


def boneco(c, cx, base, s, col, a, nome=None):
    """bonequinho em pé: pés em (cx, base), altura ~ 2.6s"""
    if a <= 0:
        return
    rrect(c, cx - s * 0.55, base - s * 1.75, s * 1.1, s * 1.25, s * 0.45, col, a, shadow=True)
    c.drawCircle(cx, base - s * 2.15, s * 0.45, paint(col, a))
    c.drawCircle(cx, base - s * 2.15, s * 0.45, paint("#FFFFFF", a * 0.25))
    rrect(c, cx - s * 0.42, base - s * 0.55, s * 0.32, s * 0.55, s * 0.12, mix(col, INK, 0.35), a)
    rrect(c, cx + s * 0.1, base - s * 0.55, s * 0.32, s * 0.55, s * 0.12, mix(col, INK, 0.35), a)
    if nome:
        fmid(c, nome, cx, base - s * 1.15, s * 0.42, "black", "#FFFFFF", a)


def balanca(c, cx, base, a, valor=None, w=360, col_val=None):
    """balança de farmácia: plataforma em (cx, base) e visor ao lado"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, base, w, 26, 12, "#9AA3AD", a, shadow=True)
    rrect(c, cx + w / 2 - 40, base - 230, 24, 240, 10, "#9AA3AD", a)
    rrect(c, cx + w / 2 - 110, base - 320, 170, 96, 18, "#2F3640", a, shadow=True)
    if valor is not None:
        fmid(c, valor, cx + w / 2 - 25, base - 272, 34, "black", col_val or "#7CF29A", a)


def dupla(c, cx, base, nomes, a, valor=None, s=46, w=330, sobe=1.0):
    """dois bonequinhos na balança (sobe: 0 = fora, 1 = em cima)"""
    if a <= 0:
        return
    balanca(c, cx, base, a, valor if sobe > 0.95 else None, w)
    dy = (1 - sobe) * 60
    for k, n in enumerate(nomes):
        boneco(c, cx - 70 + k * 100 - 30, base - 2 + dy, s, P_COR[n], a * max(0.25, sobe), n[0])


def ficha(c, s, cx, cy, a, size=40, col=None):
    """letra de lanche/pessoa numa ficha colorida"""
    if a <= 0:
        return
    col = col or P_COR.get(s, INK)
    r = size * 0.85
    c.drawCircle(cx, cy, r, paint(col, a))
    fmid(c, s, cx, cy, size, "black", "#FFFFFF", a)


def escada(c, t, a, x0, y0, linhas, ativos, dx=150, dy=118, w=700, size=50):
    """sistema escalonado em degraus: linhas = [expr], o degrau de baixo é o último. ativos = [instante] por degrau."""
    if a <= 0:
        return
    n = len(linhas)
    for k, ex in enumerate(linhas):
        x = x0 + k * dx
        y = y0 + k * dy
        rrect(c, x, y, w - k * dx, dy - 10, 16, K.DEGRAU, a)
        on = ep(t, ativos[k], 0.4) if ativos[k] is not None else 0
        if on > 0:
            rrect(c, x, y, w - k * dx, dy - 10, 16, mix("#FFFFFF", GREEN, 0.22), a * on)
        expr(c, ex, x + 30, y + (dy - 10) / 2, size, a, align="left")
    return [(x0 + k * dx, y0 + k * dy) for k in range(n)]


def _passos(c, t, rows, x, y0, size, dy, xnota=1660):
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

PES = [(("Ana", "Beto"), "125 kg"), (("Beto", "Caio"), "145 kg"), (("Ana", "Caio"), "140 kg")]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "QUANTO PESA O BETO?", BLUE)
    for k, cue in enumerate(("01.a", "01.b", "01.c")):
        a = ep(t, C[cue], 0.5)
        dupla(c, 380 + k * 580, 560, PES[k][0], a, PES[k][1], sobe=ep(t, C[cue] + 0.3, 0.6))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 640, 1000, 110, 24, mix("#FFFFFF", RED, 0.08), ad)
        linha(c, [("125 ÷ 2 = ", INK), ("62,5 kg", RED)], W / 2, 695, 52, ad)
        strike(c, 560, 695, 1360, 695, ep(t, C["01.e"], 0.4), RED)
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, W / 2, 840, ae, "BETO: 65 kg", GREEN, -4, 52)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "resolver sistemas com três incógnitas", "três letras, três equações"),
            ("02.b", "pela escada e pelo atalho da soma", "de baixo para cima · some e divida")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 200 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 58, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "SUBSTITUIÇÃO", 560, 290, 34, "black", PURPLE, aa)
        text(c, "episódio 1", 560, 334, 24, "bold", GRAY, aa)
        expr(c, "x + y = 10", 560, 450, 64, aa)
        expr(c, "y = 3", 560, 550, 64, ep(t, C["03.a"] + 2.2, 0.4))
        expr(c, "x = 7", 560, 670, 70, ep(t, C["03.a"] + 4.6, 0.4), cores={2: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "SUBTRAIR EQUAÇÕES", 1360, 290, 34, "black", BLUE, ab)
        text(c, "episódio 2", 1360, 334, 24, "bold", GRAY, ab)
        expr(c, "x + y + z = 6", 1360, 450, 56, ab)
        fmid(c, "− (y + z = 5)", 1360, 550, 56, "black", INK, ab)
        line(c, 1130, 610, 1590, 610, INK, ab, 4)
        expr(c, "x = 1", 1360, 680, 64, ep(t, C["03.b"] + 2.4, 0.4), cores={2: GREEN})
        pill(c, "o que é igual some", 1360, 770, BLUE, size=26, a=ep(t, C["03.b"] + 2.4, 0.4), anchor="center")
    line(c, 960, 250, 960, 780, "#E6E6E2", ab, 3)


# ======================================================================
# concreto: a balança
# ======================================================================

def b_balanca(c, t, C, B):
    head(c, t, B["start"], "A BALANÇA DE FARMÁCIA", "TRÊS AMIGOS, EM DUPLAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    for k in range(3):
        t0 = C["04.a"] + k * 1.4
        dupla(c, 380 + k * 580, 600, PES[k][0], aa * ep(t, t0, 0.4), PES[k][1], sobe=ep(t, t0 + 0.3, 0.6))
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        pill(c, "ninguém subiu sozinho", W / 2, 690, AMBER, size=30, a=ab, anchor="center")
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        linha(c, [("3 ", BLUE), ("valores escondidos  →  ", INK), ("3 ", BLUE), ("pistas", INK)], W / 2, 780, 44, acc)


# ======================================================================
# bloco a — três equações independentes
# ======================================================================

def b_tres(c, t, C, B):
    head(c, t, B["start"], "BLOCO A · QUANTAS EQUAÇÕES?", "TRÊS LETRAS, TRÊS PISTAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        boxed(c, 240, 240, 1440, 150, BLUE, aa, 0.08)
        linha(c, [("SISTEMA 3 × 3", BLUE), (": 3 equações e 3 incógnitas", INK)], W / 2, 315, 44, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        boxed(c, 240, 420, 1440, 150, BLUE, ab, 0.08)
        linha(c, [("INDEPENDENTES", BLUE), (": cada uma traz uma informação nova", INK)], W / 2, 478, 40, ab)
        ftext(c, "não é cópia nem mistura das outras", W / 2, 540, 30, "bold", GRAY, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, 240, 610, 1440, 170, 22, mix("#FFFFFF", AMBER, 0.12), acc)
        for k, s in enumerate(("A = ?", "B = ?", "C = ?")):
            chip(c, s, 640 + k * 320, 660, AMBER, acc, size=36)
        text(c, "2 pistas para 3 números: sobra dúvida", W / 2, 750, 32, "black", INK, acc)


# ======================================================================
# bloco b — a escada
# ======================================================================

ESC = ["x + y + z = 6", "y + z = 5", "z = 3"]


def b_escada(c, t, C, B):
    head_seq(c, t, C, [("06", "BLOCO B · SISTEMA ESCALONADO", "UMA ESCADA", BLUE),
                       ("07", "DE BAIXO PARA CIMA", "SUBA SUBSTITUINDO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    aa = ep(t, C["06.a"], 0.5)
    if sid == "06":
        escada(c, t, aa, 260, 250, ESC, [None, None, None])
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            for k, s in enumerate(("3 letras", "2 letras", "1 letra")):
                pill(c, s, 1660, 250 + k * 118 + 54, BLUE, size=26, a=ab, anchor="right")
            boxed(c, 240, 640, 1440, 80, BLUE, ab, 0.08)
            linha(c, [("SISTEMA ESCALONADO", BLUE), (": cada linha tem uma letra a menos", INK)], W / 2, 680, 34, ab)
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            boxed(c, 240, 735, 1440, 80, BLUE, acc, 0.08)
            linha(c, [("ESCALONAR", BLUE), (": arrumar o sistema nesse formato", INK)], W / 2, 775, 34, acc)
        return
    tz, ty, tx = C["07.a"], C["07.b"], C["07.c"]
    escada(c, t, 1.0, 260, 250, ESC, [tx, ty, tz])
    # respostas ao lado dos degraus, subindo
    for k, (t0, s) in enumerate(((tx, "x = 1"), (ty, "y = 2"), (tz, "z = 3"))):
        a = ep(t, t0, 0.4)
        if a > 0:
            chip(c, s, 1430, 250 + k * 118 + 54, GREEN, a, size=40)
    ab = ep(t, ty, 0.4)
    if ab > 0:
        arrow(c, 1270, 250 + 2 * 118 + 40, 1270, 250 + 118 + 70, GREEN, ab, 5, 16, ab)
        ftext(c, "y + 3 = 5", 1090, 250 + 118 + 66, 30, "black", GRAY, ab)
    acc = ep(t, tx, 0.4)
    if acc > 0:
        arrow(c, 1270, 250 + 118 + 40, 1270, 250 + 70, GREEN, acc, 5, 16, acc)
        ftext(c, "x + 2 + 3 = 6", 1090, 250 + 66, 30, "black", GRAY, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        boxed(c, 240, 640, 1440, 150, BLUE, ad, 0.08)
        linha(c, [("SUBSTITUIÇÃO DE BAIXO PARA CIMA", BLUE)], W / 2, 685, 34, ad)
        linha(c, [("conferência: ", GRAY), ("1 + 2 + 3 = 6", GREEN)], W / 2, 745, 40, ep(t, C["07.d"] + 2.4, 0.4))


def b_atalho_escada(c, t, C, B):
    head(c, t, B["start"], "ATALHO NA ESCADA", "SUBTRAIA O DEGRAU DE BAIXO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        expr(c, "x + y + z = 6", 560, 330, 60, aa, cores={2: GREEN, 4: GREEN})
        expr(c, "y + z = 5", 560, 450, 60, aa)
        rrect(c, 520, 290, 300, 80, 16, GREEN, 0.10 * aa)
        pill(c, "já vale 5", 900, 330, GREEN, size=26, a=ep(t, C["08.a"] + 2.5, 0.4), anchor="left")
    ab = ep(t, C["08.b"], 0.5)
    K.atalho(c, 1060, 260, 600, 360, "ATALHO", [("m", "6 − 5 = 1"), "x = 1, sem achar o y"], ab, size=40)


# ======================================================================
# bloco c — o atalho da soma · bloco d — total menos a dupla
# ======================================================================

COMBOS = [("A", "B", "R$ 13,00"), ("B", "C", "R$ 15,00"), ("A", "C", "R$ 14,00")]


def _combos(c, t, a, y=300, hl=None):
    for k, (p, q, v) in enumerate(COMBOS):
        cx = 440 + k * 520
        al = a if hl is None else a * (1.0 if hl == k else 0.35)
        if al <= 0:
            continue
        rrect(c, cx - 210, y - 70, 420, 150, 22, "#FFFFFF", al, shadow=True)
        ficha(c, p, cx - 140, y - 5, al, 34)
        fmid(c, "+", cx - 85, y - 5, 40, "black", INK, al)
        ficha(c, q, cx - 30, y - 5, al, 34)
        fmid(c, v, cx + 110, y - 5, 38, "black", INK, al)


def b_soma(c, t, C, B):
    head(c, t, B["start"], "BLOCO C · O ATALHO DA SOMA", "CONTE AS LETRAS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    _combos(c, t, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        text(c, "somando as três: quantas vezes aparece cada letra?", W / 2, 450, 32, "black", INK2, ab)
    for k, L in enumerate("ABC"):
        al = ep(t, C["09.c"] + k * 1.3, 0.4)
        if al > 0:
            x = 560 + k * 400
            ficha(c, L, x - 50, 540, al, 34)
            ficha(c, L, x + 50, 540, al, 34)
            text(c, "2 vezes", x, 620, 28, "black", P_COR[L], al)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 670, 1320, 140, 22, mix("#FFFFFF", PURPLE, 0.10), ad)
        fmid(c, "13 + 15 + 14 = 42 = 2 · (A + B + C)", W / 2, 715, 44, "black", INK, ad)
        linha(c, [("A + B + C = 42 ÷ 2 = ", INK), ("21", GREEN)], W / 2, 775, 40, ep(t, C["09.d"] + 4.0, 0.4))


def b_regra(c, t, C, B):
    head(c, t, B["start"], "BLOCO D · CADA UM", "O TOTAL MENOS A DUPLA EM QUE ELE NÃO ESTÁ", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["10"], 0.4)
    cues = [C["10.a"], C["10.b"], C["10.c"]]
    hl = None
    for k, t0 in enumerate(cues):
        if t >= t0:
            hl = (0, 1, 2)[k]
    _combos(c, t, a0, 290, hl=hl if t < C["10.d"] else None)
    pill(c, "total: R$ 21,00", W / 2, 420, GREEN, size=30, a=a0, anchor="center")
    rows = [(C["10.a"], "C", "21 − 13 = 8", "sem C: A + B"), (C["10.b"], "A", "21 − 15 = 6", "sem A: B + C"),
            (C["10.c"], "B", "21 − 14 = 7", "sem B: A + C")]
    for k, (t0, L, ex, nota) in enumerate(rows):
        a, d = rise(t, t0)
        if a <= 0:
            continue
        y = 510 + k * 92 + d
        ficha(c, L, 420, y, a, 32)
        expr(c, ex, 500, y, 50, a, align="left")
        pill(c, nota, 1480, y, PURPLE, size=24, a=a, anchor="center")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        pill(c, "confira: 6 + 7 = 13 ✓", 1060, 790, GREEN, size=28, a=ad, anchor="center")


def b_atalho_soma(c, t, C, B):
    head(c, t, B["start"], "ATALHO DA SOMA", "TRÊS PASSOS", GREEN)
    card(c, *CARD_R)
    passos = [("11.a", "SOME as três duplas"), ("11.b", "DIVIDA POR 2: cada um apareceu 2 vezes"),
              ("11.c", "TIRE do total a dupla sem quem você procura")]
    boxed(c, 240, 230, 1440, 580, GREEN, ep(t, C["11"], 0.4), 0.06)
    for k, (cue, s) in enumerate(passos):
        a, d = rise(t, C[cue])
        y = 340 + k * 160 + d
        badge_num(c, k + 1, 330, y - 14, a, 36, bg=GREEN)
        text(c, s, 400, y, 46, "black", INK, a, align="left")


# ======================================================================
# bloco e — quando usar
# ======================================================================

def _cidades(c, cx, cy, a):
    pts = [(cx - 110, cy + 70), (cx + 110, cy + 70), (cx, cy - 90)]
    for i in range(3):
        x0, y0 = pts[i]; x1, y1 = pts[(i + 1) % 3]
        line(c, x0, y0, x1, y1, GRAY, a, 5)
    for (x, y), L in zip(pts, "ABC"):
        ficha(c, L, x, y, a, 26)


def b_quando(c, t, C, B):
    head(c, t, B["start"], "BLOCO E · QUANDO USAR", "CADA LETRA, O MESMO NÚMERO DE VEZES", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        regra(c, "cada incógnita aparece o mesmo número de vezes", W / 2, 290, aa, 38, BLUE)
    for k, (s, dt) in enumerate((("pesagens em dupla", 0.0), ("combos de lanchonete", 1.6), ("distâncias entre 3 cidades", 3.4))):
        a = ep(t, C["12.b"] + dt, 0.4)
        if a <= 0:
            continue
        cx = 460 + k * 500
        rrect(c, cx - 210, 380, 420, 300, 24, "#FFFFFF", a, shadow=True)
        if k == 0:
            rrect(c, cx - 130, 590, 260, 20, 10, "#9AA3AD", a, shadow=True)
            boneco(c, cx - 50, 588, 34, P_COR["Ana"], a, "A")
            boneco(c, cx + 50, 588, 34, P_COR["Beto"], a, "B")
        elif k == 1:
            for j, L in enumerate("ABC"):
                ficha(c, L, cx - 90 + j * 90, 520, a, 34)
        else:
            _cidades(c, cx, 520, a)
        text(c, s, cx, 650, 28, "black", INK, a)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        pill(c, "outros 3 × 3: escalonamento completo → série de Determinantes", W / 2, 760, PURPLE, size=26, a=acc,
             anchor="center")


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("13", "SUA VEZ", "PAUSE E TENTE", GREEN), ("14", "VAMOS JUNTOS", "PELO ATALHO DA SOMA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        for k, ex in enumerate(("A + B = 9", "B + C = 11", "A + C = 10")):
            rrect(c, 260 + k * 480, 240, 440, 110, 20, "#FFFFFF", aa, shadow=True)
            expr(c, ex, 480 + k * 480, 295, 50, aa)
    ab = ep(t, C["13.b"], 0.5) * (1 - ep(t, C["14"], 0.3))
    if ab > 0:
        text(c, "quanto vale cada um?", W / 2, 440, 40, "black", INK, ab)
    pause_timer(c, t, C["13.end"] - 1.9, W / 2, 600)
    if t < C["14"]:
        return
    rows = [(C["14.a"], "9 + 11 + 10 = 30", "cada letra 2 vezes", GREEN),
            (C["14.a"] + 4.5, "30 ÷ 2 = 15", "total", GREEN)]
    _passos(c, t, rows, 300, 430, 50, 90)
    for k, (dt, L, ex) in enumerate(((0.0, "A", "15 − 11 = 4"), (2.6, "B", "15 − 10 = 5"), (5.2, "C", "15 − 9 = 6"))):
        a = ep(t, C["14.b"] + dt, 0.4)
        if a <= 0:
            continue
        y = 640
        x = 340 + k * 480
        ficha(c, L, x, y, a, 30)
        expr(c, ex, x + 50, y, 42, a, align="left")
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        pill(c, "confira: 4 + 5 = 9 ✓", W / 2, 760, GREEN, size=30, a=acc, anchor="center")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Sistema escalonado: resolva de baixo para cima.",
          "Em duplas, cada um aparece duas vezes: some e divida por 2.",
          "Cada um é o total menos a dupla em que ele não está."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["15", "25"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "15" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 52, "black", INK, a, 1360, 62)


ERROS = [("somou 42 e não dividiu: C = 42 − 13 = 29", "a soma das três duplas foi feita direitinho",
          "C sozinho custaria mais que o combo B + C (R$ 15). Cada um apareceu 2 vezes: 42 ÷ 2 = 21 → C = 8"),
         ("A + B = 13 → cada um R$ 6,50", "são dois lanches e treze reais: metade para cada",
          "isso supõe que os dois custam o mesmo. Ninguém disse isso: A = 6 e B = 7"),
         ("perguntam y e a pessoa responde 5", "o 5 é o número que está na tela",
          "5 é y + z, um resultado do meio do caminho. y = 2. Releia a pergunta antes de marcar")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["16", "17", "18"], ERROS)


# ======================================================================
# questões 2 e 8 do material
# ======================================================================

def _enunciado(c, s, a, y0=250, size=29, w=720):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y


def _painel(c, a, y0=230):
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS2 = [("A", "60", "massa da Ana", RED),
         ("B", "62,5", "125 ÷ 2", RED),
         ("C", "65", "", GREEN),
         ("D", "72,5", "145 ÷ 2", RED),
         ("E", "80", "massa do Caio", RED)]


def pilha(c, t, t0, t_div, cx, base, a):
    """as três pesagens somadas: Ana, Beto e Caio aparecem duas vezes cada; depois a pilha se divide ao meio"""
    if a <= 0:
        return
    nomes = ["Ana", "Beto", "Beto", "Caio", "Ana", "Caio"]
    u = ep(t, t_div, 0.8)
    for k, n in enumerate(nomes):
        ak = a * ep(t, t0 + k * 0.25, 0.3)
        grupo = 0 if n in ("Ana", "Beto", "Caio") and k in (0, 1, 3) else 1
        x = cx - 250 + k * 100
        if u > 0:
            # reorganiza em dois grupos de três: Ana, Beto, Caio | Ana, Beto, Caio
            ordem = {"Ana": 0, "Beto": 1, "Caio": 2}
            g = 0 if k in (0, 1, 3) else 1
            xf = cx - 330 + g * 380 + ordem[n] * 100
            x = x + (xf - x) * u
        boneco(c, x, base, 30, P_COR[n], ak, n[0])
    if u > 0:
        line(c, cx + 5, base - 120, cx + 5, base + 10, INK, a * u, 4)
        text(c, "÷ 2", cx + 5, base - 135, 30, "black", PURPLE, a * u)


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "PESAGENS EM DUPLA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["19.a"], 0.4) * (1 - ep(t, C["20"], 0.4))
    yend = _enunciado(c, "Três amigos, Ana, Beto e Caio, subiram em duplas numa balança. Ana e Beto juntos marcaram 125 kg; "
                         "Beto e Caio, 145 kg; Ana e Caio, 140 kg. A massa de Beto, em quilogramas, é", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"19.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"21.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 260, 680, 34, C["20.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["19.end"] - 1.9, 540, yend + 100)
    if t >= C["20"]:
        ap = ep(t, C["20"], 0.4)
        _painel(c, ap)
        text(c, "duplas → atalho da soma", 550, 285, 26, "black", GREEN, ap)
        pilha(c, t, C["20.a"], C["20.a"] + 4.5, 550, 470, ap * (1 - ep(t, C["20.b"], 0.4)))
        rows = [(C["20.a"], "125 + 145 + 140 = 410 kg", "", None), (C["20.a"] + 4.5, "410 ÷ 2 = 205 kg", "", None)]
        _passos(c, t, rows, 220, 560, 38, 64)
        ab = ep(t, C["20.b"], 0.4)
        if ab > 0:
            rrect(c, 200, 290, 700, 130, 18, mix("#FFFFFF", PURPLE, 0.10), ab)
            text(c, "Beto: tire a dupla SEM ele (Ana + Caio)", 550, 335, 24, "black", PURPLE, ab)
            text(c, "205 − 140 = 65 kg", 550, 395, 44, "black", GREEN, ab)
        acc = ep(t, C["20.c"], 0.4)
        if acc > 0:
            rrect(c, 200, 700, 700, 110, 18, mix("#FFFFFF", GREEN, 0.10), acc)
            text(c, "Ana 60 kg · Caio 80 kg", 550, 740, 28, "black", INK2, acc)
            text(c, "confira: 60 + 65 = 125 kg ✓", 550, 788, 28, "black", GREEN, acc)


ALTS8 = [("A", "5", "difíceis", RED),
         ("B", "7", "", GREEN),
         ("C", "8", "fáceis", RED),
         ("D", "15", "pontos das difíceis", RED),
         ("E", "17", "m + 2d (meio do caminho)", AMBER)]


def b_q8(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 8 · VOCÊ FAZ", "PROVA COM TRÊS NÍVEIS", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4) * (1 - ep(t, C["23"], 0.4))
    yend = _enunciado(c, "Uma prova tem 20 questões: as fáceis valem 1 ponto, as médias valem 2 e as difíceis valem 3, num "
                         "total de 37 pontos. O número de questões médias é 2 a mais que o de difíceis. O número de "
                         "questões médias é", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS8, 1000, 260, 680, 34, C["23.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["22.end"] - 1.9, 540, yend + 100)
    if t >= C["23"]:
        ap = ep(t, C["23"], 0.4)
        _painel(c, ap)
        text(c, "f fáceis · m médias · d difíceis", 550, 280, 26, "black", BLUE, ap)
        rows = [(C["23.a"], "f + m + d = 20", "", None),
                (C["23.a"] + 3.2, "f + 2m + 3d = 37", "", None),
                (C["23.a"] + 6.6, "m = d + 2", "", None),
                (C["23.b"], "m + 2d = 17", "", None),
                (C["23.c"], "3d + 2 = 17 → d = 5", "", None),
                (C["23.c"] + 5.0, "m = 7 · f = 8", "", None)]
        _passos(c, t, rows, 220, 345, 38, 62)
        ab = ep(t, C["23.b"], 0.4)
        if ab > 0:
            pill(c, "2ª − 1ª", 880, 345 + 3 * 62, PURPLE, size=22, a=ab, anchor="right")
        ad = ep(t, C["23.d"], 0.4)
        if ad > 0:
            rrect(c, 200, 715, 700, 100, 18, mix("#FFFFFF", GREEN, 0.10), ad)
            text(c, "8 + 7 + 5 = 20 questões", 550, 755, 26, "black", INK2, ad)
            text(c, "8 + 14 + 15 = 37 pontos ✓", 550, 798, 26, "black", GREEN, ad)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO", PURPLE)
    itens = [("26.a", "juntamos tudo", BLUE), ("26.b", "caçamos as pegadinhas", AMBER),
             ("26.c", "sistemas na Física, na Química e na Geometria", PURPLE)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        y = 330 + k * 150 + d
        badge_num(c, k + 1, 360, y - 14, a, 32, bg=col)
        text(c, s, 420, y, 50, "black", INK, a, align="left")


def b_cta(c, t, C, B):
    cta(c, t, C["27.like"], C["27.sub"], C["27.bell"], C["27.com"], C["27.bye"],
        "Você já tinha dividido uma pesagem em dupla por 2?", canal="no Estudativo", anki=C["27.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, balanca=b_balanca, tres=b_tres, escada=b_escada,
              atalho_escada=b_atalho_escada, soma=b_soma, regra=b_regra, atalho_soma=b_atalho_soma, quando=b_quando,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q8=b_q8, ponte=b_ponte, cta=b_cta)
