"""Visual — Matrizes e Operações, Episódio 4: o que muda em relação aos números e a matriz inversa (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com potências, alternativas, erro_cards, atalho,
selo, regra...).
Peças deste episódio: matriz() (matriz com colchetes, cor e alfa por casa), dims() (as fichas "2 × 3"), meia() e sapato()
(ícones da ordem), cadeado() (a chave da inversa), alt_mat() (alternativas que são matrizes), linha() (texto com cor
por trecho).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum048", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_matrizes_ep4_ordem_inversa.mp4"
CARD_R = K.CARD_R
CHAVE = "#C27A1F"    # a chave do cadeado (inversa)

A_ = [["1", "2"], ["0", "1"]]
B_ = [["1", "0"], ["3", "1"]]
AB = [["7", "2"], ["3", "1"]]
BA = [["1", "2"], ["3", "7"]]
U_ = [["1", "1"], ["1", "1"]]
V_ = [["1", "−1"], ["−1", "1"]]
Z_ = [["0", "0"], ["0", "0"]]
I_ = [["1", "0"], ["0", "1"]]
K_ = [["3", "1"], ["5", "2"]]
KI = [["2", "−1"], ["−5", "3"]]


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def mat_dims(rows, size, cw=None, rh=None):
    cw = cw or size * 1.75
    rh = rh or size * 1.35
    return len(rows[0]) * cw + size * 0.7, len(rows) * rh + size * 0.3, cw, rh


def mat_pos(cx, cy, rows, size, cw=None, rh=None):
    """centros das casas: lista de listas (x, y)"""
    w, h, cw, rh = mat_dims(rows, size, cw, rh)
    n, m = len(rows), len(rows[0])
    return [[(cx + (j - (m - 1) / 2) * cw, cy + (i - (n - 1) / 2) * rh) for j in range(m)] for i in range(n)]


def colchetes(c, cx, cy, w, h, a, col=INK2, sw=4):
    if a <= 0:
        return
    t = h * 0.12
    for s in (-1, 1):
        x = cx + s * w / 2
        p = skia.Path()
        p.moveTo(x - s * t, cy - h / 2); p.lineTo(x, cy - h / 2); p.lineTo(x, cy + h / 2); p.lineTo(x - s * t, cy + h / 2)
        c.drawPath(p, paint(col, a, stroke=sw))


def matriz(c, cx, cy, rows, size, a, col=INK, cores=None, alfas=None, cw=None, rh=None, br=INK2, peso="black"):
    """matriz com colchetes; cores/alfas = {(i, j): valor} por casa. Devolve a largura."""
    if a <= 0:
        return mat_dims(rows, size, cw, rh)[0]
    w, h, cw_, rh_ = mat_dims(rows, size, cw, rh)
    colchetes(c, cx, cy, w, h, a, br, max(3, size * 0.08))
    pos = mat_pos(cx, cy, rows, size, cw, rh)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            ak = a * (alfas or {}).get((i, j), 1.0)
            if ak > 0 and v:
                ftext(c, v, pos[i][j][0], pos[i][j][1] + size * 0.36, size, peso, (cores or {}).get((i, j), col), ak)
    return w


def dims(c, s, cx, cy, a, col=INK, meio=None, size=40):
    """ficha 'n × m'; meio = cor do número que encosta no vizinho ('esq' destaca o 1º, 'dir' o 2º)"""
    if a <= 0:
        return
    n, m = s.split("×")
    n, m = n.strip(), m.strip()
    w = 200
    rrect(c, cx - w / 2, cy - 44, w, 88, 18, mix("#FFFFFF", col, 0.10), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - 44, w, 88), 18, 18), paint(col, a, stroke=3))
    ftext(c, n, cx - 52, cy + size * 0.36, size, "black", meio[0] if meio and meio[0] else col, a)
    ftext(c, "×", cx, cy + size * 0.36, size * 0.8, "black", GRAY, a)
    ftext(c, m, cx + 52, cy + size * 0.36, size, "black", meio[1] if meio and meio[1] else col, a)


def meia(c, cx, cy, s, a, col=BLUE):
    """meia em L"""
    if a <= 0:
        return
    rrect(c, cx - 0.18 * s, cy - 0.5 * s, 0.36 * s, 0.8 * s, 0.12 * s, col, a)
    rrect(c, cx - 0.18 * s, cy + 0.12 * s, 0.62 * s, 0.32 * s, 0.16 * s, col, a)
    rrect(c, cx - 0.18 * s, cy - 0.5 * s, 0.36 * s, 0.12 * s, 0.04 * s, "#FFFFFF", a * 0.6)


def sapato(c, cx, cy, s, a, col=INK2):
    """sapato de perfil"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - 0.45 * s, cy + 0.25 * s); p.lineTo(cx - 0.45 * s, cy - 0.25 * s); p.lineTo(cx - 0.1 * s, cy - 0.25 * s)
    p.cubicTo(cx, cy - 0.05 * s, cx + 0.3 * s, cy - 0.05 * s, cx + 0.5 * s, cy + 0.08 * s)
    p.lineTo(cx + 0.5 * s, cy + 0.25 * s); p.close()
    c.drawPath(p, paint(col, a))
    rrect(c, cx - 0.5 * s, cy + 0.22 * s, 1.04 * s, 0.1 * s, 0.04 * s, INK, a)


def cadeado(c, cx, cy, s, a, aberto=0.0, col=PURPLE):
    """cadeado; aberto = 0 (fechado) a 1 (arco levantado)"""
    if a <= 0:
        return
    up = aberto * 0.22 * s
    arco = skia.Rect.MakeLTRB(cx - 0.28 * s, cy - 0.62 * s - up, cx + 0.28 * s, cy - 0.06 * s - up)
    c.drawArc(arco, 180, 180, False, paint(INK2, a, stroke=0.1 * s))
    line(c, cx - 0.28 * s, cy - 0.34 * s - up, cx - 0.28 * s, cy - 0.1 * s - up * (1 - aberto), INK2, a, 0.1 * s,
         cap_round=False)
    line(c, cx + 0.28 * s, cy - 0.34 * s - up, cx + 0.28 * s, cy - 0.1 * s, INK2, a, 0.1 * s, cap_round=False)
    rrect(c, cx - 0.42 * s, cy - 0.12 * s, 0.84 * s, 0.66 * s, 0.1 * s, col, a)
    c.drawCircle(cx, cy + 0.14 * s, 0.08 * s, paint("#FFFFFF", a))
    rrect(c, cx - 0.03 * s, cy + 0.16 * s, 0.06 * s, 0.18 * s, 0.02 * s, "#FFFFFF", a)


def chave(c, cx, cy, s, a, col=CHAVE):
    if a <= 0:
        return
    c.drawCircle(cx - 0.3 * s, cy, 0.18 * s, paint(col, a, stroke=0.08 * s))
    line(c, cx - 0.12 * s, cy, cx + 0.42 * s, cy, col, a, 0.08 * s)
    for dx in (0.22, 0.36):
        line(c, cx + dx * s, cy, cx + dx * s, cy + 0.14 * s, col, a, 0.07 * s)


def alt_mat(c, t, C, alts, x, y0, ok_cue, okL, cues_in, cues_x, size=34, gap=20, w=700):
    """alternativas A–E em que a resposta pode ser matriz: alts = [(L, texto_ou_linhas, motivo)]"""
    aok = ep(t, ok_cue, 0.5)
    y = y0
    for L, v, why in alts:
        a, d = rise(t, cues_in.get(L, 1e9))
        ok = L == okL
        is_m = isinstance(v, list)
        hh = (mat_dims(v, size)[1] + 8) if is_m else size * 1.6
        ax = ep(t, cues_x.get(L, 1e9), 0.4) if not ok else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - 6 + d, w + 30, hh + 12, 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + hh / 2 + d, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
            aa = a * (1 - 0.5 * ax)
            if is_m:
                mw = mat_dims(v, size)[0]
                matriz(c, x + 60 + mw / 2, y + hh / 2 + d, v, size, aa)
                if ax > 0:
                    strike(c, x + 52, y + hh / 2 + d, x + 68 + mw, y + hh / 2 + d, ax, RED, ax)
            else:
                text(c, v, x + 50, y + hh / 2 + d + size * 0.36, size, "bold", INK, aa, align="left")
                if ax > 0:
                    yy = y + hh / 2 + d
                    strike(c, x + 46, yy, x + 54 + text_w(v, "bold", size), yy, ax, RED, ax)
            if ax > 0 and why:
                pill(c, why, x + w, y + hh / 2 + d, RED, size=20, a=ax, anchor="right", bounds=(0, 1920))
        y += hh + gap
    return y


def prod(c, cx, cy, mats, size, a, sep="·", gap=34, cores=None):
    """sequência de matrizes e sinais: mats = [rows | 'texto'] centrada em cx; devolve as posições x dos itens"""
    ws = []
    for m in mats:
        ws.append(mat_dims(m, size)[0] if isinstance(m, list) else ftext_w(m, "black", size))
    tot = sum(ws) + gap * (len(mats) - 1)
    x = cx - tot / 2
    xs = []
    for k, (m, w_) in enumerate(zip(mats, ws)):
        xm = x + w_ / 2
        xs.append(xm)
        if isinstance(m, list):
            matriz(c, xm, cy, m, size, a, cores=(cores or {}).get(k))
        else:
            ftext(c, m, xm, cy + size * 0.36, size, "black", (cores or {}).get(k, INK2), a)
        x += w_ + gap
    return xs


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "MATRIZES · EPISÓDIO 4", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 200, 1320, 120, 22, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("NÚMEROS:  ", BLUE), ("a · b = 0  →  a = 0 ou b = 0", INK)], 960, 260, 44, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        text(c, "MATRIZES:", 960, 385, 32, "black", PURPLE, ab)
        u = clamp((t - C["01.c"]) / 0.6) if t >= C["01.c"] else 0
        mats = [U_, "·", V_, "=", Z_] if u > 0 else [U_, "·", V_]
        xs = prod(c, 960 if u > 0 else 760, 540, mats, 52, ab)
        if u > 0:
            K.boxed(c, xs[4] - 120, 440, 240, 200, GREEN, u, 0.10)
            text(c, "matriz NULA", xs[4], 690, 28, "black", GREEN, u)
        ad = ep(t, C["01.d"], 0.5)
        if ad > 0:
            for xk in (xs[0], xs[2]):
                selo(c, xk, 690, ad, "NÃO É NULA", RED, -4, 26)
    ad2 = ep(t, C["01.d"] + 1.2, 0.5)
    if ad2 > 0:
        pill(c, "produto zero SEM fator zero", W / 2, 790, AMBER, size=30, a=ad2, anchor="center")


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "MATRIZES · EP. 4", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "4º episódio da série de MATRIZES", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "QUAIS REGRAS VALEM", "dos números para as matrizes", BLUE),
             ("02.b", "A INVERSA 2 × 2", "para decifrar um código", PURPLE)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 640 + k * 640
        rrect(c, x - 290, 330, 580, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 290, 330, 580, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 26, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "episódio 3", PURPLE), ("03.b", "episódio 1", BLUE), ("03.c", "episódio 1", BLUE)]
    for k, (cue, tag, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 290 + k * 170 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, tag, 300, y - 70, col, size=22, a=a)
        if k == 0:
            linha(c, [("LINHA POR COLUNA: ", PURPLE), ("casa com casa, e soma", INK)], 780, y + 4, 38, a)
            matriz(c, 1300, y + 4, [["1", "2"], ["", ""]], 30, a, cores={(0, 0): PURPLE, (0, 1): PURPLE})
            matriz(c, 1460, y + 4, [["3", ""], ["4", ""]], 30, a, cores={(0, 0): PURPLE, (1, 0): PURPLE})
            text(c, "1·3 + 2·4", 1560, y + 14, 26, "black", PURPLE, a, align="left")
        elif k == 1:
            linha(c, [("IDENTIDADE I: ", BLUE), ("1 na diagonal, 0 no resto", INK)], 800, y + 4, 38, a)
            matriz(c, 1450, y + 4, I_, 34, a, cores={(0, 0): BLUE, (1, 1): BLUE})
        else:
            linha(c, [("TRANSPOSTA: ", BLUE), ("linhas viram colunas", INK)], 760, y + 4, 38, a)
            matriz(c, 1270, y + 4, [["1", "2"], ["3", "4"]], 32, a)
            arrow(c, 1350, y + 4, 1420, y + 4, GRAY, a, 3, 10)
            matriz(c, 1500, y + 4, [["1", "3"], ["2", "4"]], 32, a)
    ad = ep(t, C["03.d"], 0.5)
    if ad > 0:
        pill(c, "leitura: LINHA POR LINHA  ·  (1 2 / 3 4) = “um, dois; três, quatro”", W / 2, 810, INK2, size=26,
             a=ad, anchor="center")


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "DUAS CENAS DO DIA A DIA", "A ORDEM E A CHAVE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 220, 900, 560, 26, "#FFFFFF", aa, shadow=True)
        text(c, "1º MEIA, 2º SAPATO", 670, 290, 30, "black", BLUE, aa)
        meia(c, 520, 420, 150, aa)
        text(c, "+", 670, 440, 50, "black", GRAY, aa)
        sapato(c, 820, 440, 170, aa)
        a2 = ep(t, C["04.a"] + 2.4, 0.5)
        if a2 > 0:
            text(c, "1º SAPATO, 2º MEIA", 670, 580, 30, "black", AMBER, a2)
            sapato(c, 520, 670, 140, a2)
            meia(c, 600, 660, 110, a2 * 0.85)
            text(c, "?!", 820, 690, 50, "black", AMBER, a2)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        selo(c, 670, 760, ab, "A ORDEM MUDOU O RESULTADO", RED, -3, 26)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        rrect(c, 1180, 220, 520, 560, 26, "#FFFFFF", acc, shadow=True)
        text(c, "CADEADO DE SEGREDO", 1440, 290, 30, "black", PURPLE, acc)
        ab2 = clamp((t - C["04.c"] - 1.6) / 0.8)
        cadeado(c, 1440, 500, 220, acc, ab2)
        chave(c, 1440 - 160 + 120 * ab2, 680, 120, acc)
        text(c, "quem tranca precisa da chave", 1440, 750, 26, "bold", INK2, acc)


# ======================================================================
# bloco a — AB ≠ BA
# ======================================================================

def b_ordem(c, t, C, B):
    head(c, t, B["start"], "A ORDEM IMPORTA?", "AB ≠ BA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        linha(c, [("2 · 3 = 3 · 2", INK), ("   COMUTATIVA: ", BLUE), ("trocar a ordem não muda", INK)], 960, 215, 34,
              aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        linha(c, [("A = ", INK)], 560, 330, 44, ab)
        matriz(c, 700, 330, A_, 44, ab)
        linha(c, [("B = ", INK)], 1160, 330, 44, ab)
        matriz(c, 1300, 330, B_, 44, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, 230, 440, 700, 260, 24, mix("#FFFFFF", PURPLE, 0.08), acc)
        text(c, "A · B", 580, 495, 34, "black", PURPLE, acc)
        matriz(c, 580, 610, AB, 52, acc, cores={(0, 0): PURPLE})
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        rrect(c, 990, 440, 700, 260, 24, mix("#FFFFFF", AMBER, 0.10), ad)
        text(c, "B · A", 1340, 495, 34, "black", AMBER, ad)
        matriz(c, 1340, 610, BA, 52, ad, cores={(0, 0): AMBER})
        text_mid(c, "≠", 960, 600, 70, "black", RED, ep(t, C["05.e"], 0.4))
    ae = ep(t, C["05.e"], 0.5)
    if ae > 0:
        meia(c, 760, 780, 60, ae)
        sapato(c, 850, 790, 70, ae)
        text(c, "como meia e sapato: a ordem muda o resultado", 920, 795, 28, "black", PURPLE, ae, align="left")


def b_nem_existe(c, t, C, B):
    head(c, t, B["start"], "ÀS VEZES NEM EXISTE", "CONFIRA O MEIO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        linha(c, [("A: ", INK), ("2 × 3", PURPLE), ("      B: ", INK), ("3 × 4", PURPLE)], 960, 240, 44, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 320, 1320, 180, 24, mix("#FFFFFF", GREEN, 0.10), ab)
        text(c, "A · B", 420, 425, 36, "black", INK, ab)
        dims(c, "2 × 3", 650, 410, ab, meio=(None, GREEN))
        text(c, "·", 775, 425, 40, "black", GRAY, ab)
        dims(c, "3 × 4", 900, 410, ab, meio=(GREEN, None))
        arrow(c, 1020, 410, 1110, 410, GRAY, ab, 3, 10)
        linha(c, [("existe: ", GREEN), ("2 × 4", GREEN)], 1300, 410, 40, ab)
        check_icon(c, 1520, 410, 26, ab, GREEN)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 540, 1320, 180, 24, mix("#FFFFFF", RED, 0.08), acc)
        text(c, "B · A", 420, 645, 36, "black", INK, acc)
        dims(c, "3 × 4", 650, 630, acc, meio=(None, RED))
        text(c, "·", 775, 645, 40, "black", GRAY, acc)
        dims(c, "2 × 3", 900, 630, acc, meio=(RED, None))
        text(c, "4 ≠ 2", 1150, 645, 40, "black", RED, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        selo(c, 1420, 630, ad, "NÃO EXISTE", RED, -5, 32)


def b_atalho_ordem(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "MULTIPLICAÇÃO DE MATRIZES", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["07"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · ANTES DE QUALQUER CONTA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        text(c, "O PRODUTO EXISTE?  CONFIRA O MEIO", 960, 340, 38, "black", GREEN, aa)
        dims(c, "m × n", 820, 420, aa, meio=(None, GREEN), size=36)
        dims(c, "n × p", 1100, 420, aa, meio=(GREEN, None), size=36)
        text(c, "colunas da 1ª = linhas da 2ª", 960, 510, 28, "bold", INK2, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        text(c, "AB ≠ BA?  BASTA UMA CASA DIFERENTE", 960, 600, 38, "black", GREEN, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        linha(c, [("1ª casa de AB: ", INK), ("7", PURPLE), ("    1ª casa de BA: ", INK), ("1", AMBER)], 960, 690, 40,
              acc)
        check_icon(c, 1420, 690, 24, acc, GREEN)


# ======================================================================
# bloco b — produto nulo
# ======================================================================

def b_nulo(c, t, C, B):
    head(c, t, B["start"], "PRODUTO ZERO", "SEM NENHUM FATOR ZERO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        ub = clamp((t - C["08.b"]) / 2.0) * 4 if t >= C["08.b"] else 0
        al = {(i, j): clamp(ub - (2 * i + j)) for i in range(2) for j in range(2)}
        xs = prod(c, 820, 330, [U_, "·", V_, "="], 46, aa)
        w = mat_dims(Z_, 46)[0]
        matriz(c, xs[-1] + 60 + w / 2, 330, Z_, 46, aa, col=GREEN, alfas=al)
        if 0 < ub < 4.5:
            k = min(3, int(ub))
            i, j = divmod(k, 2)
            par = lambda v: f"({v})" if v.startswith("−") else v
            s_ = f"linha {i + 1} × coluna {j + 1}:  1·{par(V_[0][j])} + 1·{par(V_[1][j])} = 0"
            text(c, s_, 960, 470, 30, "black", PURPLE, aa)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        pill(c, "MATRIZ NULA = só zeros", 560, 540, BLUE, size=28, a=acc, anchor="center")
        pill(c, "nenhum fator é nulo", 1360, 540, AMBER, size=28, a=acc, anchor="center")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 600, 1400, 210, 24, mix("#FFFFFF", RED, 0.07), ad)
        linha(c, [("AB = AC", INK), ("  não dá  ", RED), ("B = C", INK), ("   (não se “corta” o A)", RED)], 960, 645,
              36, ad)
        xs = prod(c, 700, 735, [U_, "·", Z_, "="], 30, ad, gap=20)
        xs2 = prod(c, 1240, 735, [U_, "·", V_, "="], 30, ad, gap=20)
        text(c, "0", xs[-1] + 50, 746, 36, "black", GREEN, ad)
        text(c, "0", xs2[-1] + 50, 746, 36, "black", GREEN, ad)
        text(c, "mesmo resultado, matrizes da direita DIFERENTES", 960, 800, 22, "bold", INK2, ad)


# ======================================================================
# bloco c — as propriedades
# ======================================================================

def _prop(c, y, s_, vale, obs, a, col_obs=INK2, size=42):
    rrect(c, 260, y - 60, 1400, 120, 22, "#FFFFFF", a, shadow=True)
    K.expr(c, s_, 640, y, size, a, cores={i: INK for i in range(60)})
    check_icon(c, 1060, y, 28, a, GREEN if vale else RED, "check" if vale else "x")
    text(c, obs, 1110, y + 12, 30, "black", col_obs, a, align="left")


def b_props(c, t, C, B):
    head(c, t, B["start"], "O QUE CONTINUA VALENDO", "AS PROPRIEDADES BOAS", BLUE)
    card(c, *CARD_R)
    rows = [("09.a", "A · I = I · A = A", "IDENTIDADE = o número 1", BLUE),
            ("09.b", "(AB)C = A(BC)", "ASSOCIATIVA: agrupe como quiser", BLUE),
            ("09.c", "A(B+C) = AB + AC", "DISTRIBUTIVA: mantendo o lado", BLUE)]
    for k, (cue, s_, obs, col) in enumerate(rows):
        a, d = rise(t, C[cue])
        if a > 0:
            _prop(c, 300 + k * 190 + d, s_, True, obs, a, col)


def b_props2(c, t, C, B):
    head(c, t, B["start"], "ONDE MORA A PEGADINHA", "A ORDEM SE INVERTE", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 140, 22, "#FFFFFF", aa, shadow=True)
        K.expr(c, "(AB)^{t} = B^{t} · A^{t}", 620, 290, 50, aa, cores={i: INK for i in range(60)})
        check_icon(c, 960, 290, 28, aa, GREEN)
        text(c, "a ordem SE INVERTE", 1010, 302, 30, "black", AMBER, aa, align="left")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 520, 380, 880, 100, 22, mix("#FFFFFF", AMBER, 0.10), ab)
        text(c, "tirar a roupa:", 700, 442, 28, "black", INK2, ab)
        sapato(c, 900, 432, 70, ab)
        text(c, "→", 990, 442, 36, "black", GRAY, ab)
        meia(c, 1060, 430, 60, ab)
        text(c, "1º sapato, 2º meia", 1240, 442, 26, "bold", INK2, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 510, 1400, 130, 22, mix("#FFFFFF", RED, 0.07), acc)
        K.expr(c, "(A+B)^{2} = A^{2} + 2AB + B^{2}", 760, 575, 46, acc * 0.8, cores={i: INK for i in range(60)})
        check_icon(c, 1300, 575, 28, acc, RED, "x")
        text(c, "não em geral", 1350, 587, 30, "black", RED, acc, align="left")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 670, 1400, 130, 22, mix("#FFFFFF", GREEN, 0.10), ad)
        K.expr(c, "(A+B)^{2} = A^{2} + AB + BA + B^{2}", 760, 735, 46, ad, cores={i: INK for i in range(60)})
        check_icon(c, 1300, 735, 28, ad, GREEN)
        text(c, "AB + BA vira 2AB só se comutarem", 1340, 790, 22, "bold", INK2, ad, align="left")


# ======================================================================
# blocos d, e — a inversa e a receita
# ======================================================================

def b_inversa(c, t, C, B):
    head(c, t, B["start"], "DIVISÃO DE MATRIZES?", "A MATRIZ INVERSA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        text(c, "números:", 560, 256, 44, "black", BLUE, aa, align="right")
        K.expr(c, "5 · 1/5 = 1", 600, 240, 48, aa, cores={i: INK for i in range(20)}, align="left")
        text(c, "o 1/5 desfaz o 5", 1000, 256, 36, "bold", INK2, aa, align="left")
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 320, 1400, 150, 24, mix("#FFFFFF", BLUE, 0.10), ab)
        text(c, "MATRIZ INVERSA", 460, 355, 24, "black", BLUE, ab, tracking=2)
        K.expr(c, "A · A^{-1} = A^{-1} · A = I", 960, 415, 52, ab, cores={i: BLUE for i in range(60)})
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        u = clamp((t - C["11.c"] - 1.2) / 1.2)
        rrect(c, 260, 500, 860, 300, 24, "#FFFFFF", acc, shadow=True)
        text(c, "A tranca", 450, 560, 32, "black", PURPLE, acc)
        cadeado(c, 450, 690, 150, acc, 0)
        text(c, "→", 690, 700, 50, "black", GRAY, acc * u)
        K.expr(c, "A^{-1}", 820, 552, 40, acc * u, cores={i: CHAVE for i in range(10)}, align="right")
        text(c, "destranca", 840, 562, 32, "black", CHAVE, acc * u, align="left")
        cadeado(c, 900, 720, 150, acc * u, u)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        rrect(c, 1170, 500, 490, 300, 24, mix("#FFFFFF", AMBER, 0.10), ad)
        text(c, "SÓ PARA QUADRADAS", 1415, 590, 30, "black", AMBER, ad)
        text(c, "2 × 3: não tem", 1415, 650, 28, "bold", INK2, ad)
        a2 = ep(t, C["11.d"] + 1.8, 0.4)
        text(c, "e nem toda quadrada tem", 1415, 730, 28, "black", RED, a2)


def b_receita(c, t, C, B):
    head(c, t, B["start"], "A CHAVE DE UMA 2 × 2", "A RECEITA EM 3 MOVIMENTOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        linha(c, [("A = ", INK)], 380, 330, 48, aa)
        matriz(c, 540, 330, K_, 48, aa)
        al = ep(t, C["12.a"] + 2.2, 0.4)
        if al > 0:
            matriz(c, 860, 330, [["a", "b"], ["c", "d"]], 40, al, col=GRAY)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        rrect(c, 1040, 250, 620, 160, 22, mix("#FFFFFF", PURPLE, 0.10), ab)
        text(c, "ad − bc", 1350, 300, 34, "black", PURPLE, ab)
        linha(c, [("3·2 − 1·5 = 6 − 5 = ", INK), ("1", GREEN)], 1350, 360, 36, ab)
    # a animação principal: o resultado sendo montado
    if t < C["12.c"]:
        return
    cx, cy, size = 760, 620, 70
    pos = mat_pos(cx, cy, K_, size)
    u1 = ease_io(clamp((t - C["12.c"] - 0.6) / 1.2))       # troca da diagonal
    u2 = ep(t, C["12.d"] + 0.5, 0.5)                    # sinais
    u3 = ep(t, C["12.e"] + 0.5, 0.5)                    # ÷ 1
    a0 = ep(t, C["12.c"], 0.5)
    w, h, _, _ = mat_dims(K_, size)
    colchetes(c, cx, cy, w, h, a0, INK2, 5)
    (x00, y00), (x11, y11) = pos[0][0], pos[1][1]
    # 3 e 2 trocam por um arco
    for v, (xa, ya), (xb, yb), sgn in (("3", (x00, y00), (x11, y11), 1), ("2", (x11, y11), (x00, y00), -1)):
        x = xa + (xb - xa) * u1
        y = ya + (yb - ya) * u1 - sgn * 90 * math.sin(math.pi * u1)
        ftext(c, v, x, y + size * 0.36, size, "black", PURPLE if 0 < u1 < 1 or u1 >= 1 else INK, a0)
    for (i, j), v in (((0, 1), "1"), ((1, 0), "5")):
        x, y = pos[i][j]
        s_ = ("−" + v) if u2 > 0.5 else v
        ftext(c, s_, x, y + size * 0.36, size, "black", RED if u2 > 0 else INK, a0)
    if u1 > 0:
        pill(c, "1 · TROCA a diagonal principal", 1350, 520, PURPLE, size=26, a=a0, anchor="center")
    if u2 > 0:
        pill(c, "2 · SINAL na secundária", 1350, 600, RED, size=26, a=u2, anchor="center")
    if u3 > 0:
        pill(c, "3 · DIVIDE por ad − bc = 1", 1350, 680, GREEN, size=26, a=u3, anchor="center")
        K.expr(c, "1/1 ·", cx - w / 2 - 80, cy, 44, u3, cores={i: GREEN for i in range(10)})
    af = ep(t, C["12.f"], 0.5)
    if af > 0:
        rrect(c, 1080, 730, 560, 90, 20, mix("#FFFFFF", GREEN, 0.14), af)
        K.expr(c, "A^{-1} =", 1250, 775, 36, af, cores={i: GREEN for i in range(10)})
        matriz(c, 1450, 775, KI, 30, af, col=GREEN)


def b_confere(c, t, C, B):
    head(c, t, B["start"], "SERÁ QUE ESTÁ CERTA?", "MULTIPLIQUE PELA ORIGINAL", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["13.a"], 0.5)
    if a0 > 0:
        al = {(0, 0): ep(t, C["13.a"] + 1.4, 0.4), (0, 1): ep(t, C["13.b"] + 1.4, 0.4),
              (1, 0): ep(t, C["13.c"] + 0.2, 0.4), (1, 1): ep(t, C["13.c"] + 0.6, 0.4)}
        xs = prod(c, 820, 340, [K_, "·", KI, "="], 50, a0)
        w = mat_dims(I_, 50)[0]
        matriz(c, xs[-1] + 60 + w / 2, 340, I_, 50, a0, col=GREEN, alfas=al)
        lin = None
        if t < C["13.b"]:
            lin = "3·2 + 1·(−5) = 1"
        elif t < C["13.c"]:
            lin = "3·(−1) + 1·3 = 0"
        if lin:
            text(c, lin, 960, 480, 36, "black", PURPLE, a0)
        acc = ep(t, C["13.c"] + 0.8, 0.4)
        if acc > 0:
            selo(c, 1500, 470, acc, "CONFERE: É A IDENTIDADE", GREEN, -4, 30)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 560, 1400, 120, 22, mix("#FFFFFF", RED, 0.08), ad)
        linha(c, [("ad − bc = 0", RED), ("  →  não dá para dividir  →  ", INK), ("SEM INVERSA", RED)], 960, 620, 38,
              ad)
    ae = ep(t, C["13.e"], 0.5)
    if ae > 0:
        pill(c, "esse número tem nome e série própria: DETERMINANTE", W / 2, 760, BLUE, size=30, a=ae,
             anchor="center")


def b_atalho_receita(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "A RECEITA DA INVERSA 2 × 2", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["14"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · NUNCA ESQUEÇA UM MOVIMENTO", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["14.a"], 0.5)
    for k, (s_, col) in enumerate((("TROCA", PURPLE), ("SINAL", RED), ("DIVIDE", GREEN))):
        ak = aa * ep(t, C["14.a"] + 0.5 + 0.5 * k, 0.3)
        if ak > 0:
            chip(c, s_, 560 + k * 400, 360, col, ak, size=50, w=320)
            if k < 2:
                text(c, "→", 760 + k * 400, 376, 44, "black", GRAY, ak)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "troca na diagonal PRINCIPAL  ·  sinal na SECUNDÁRIA", 960, 500, 36, "black", INK, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 420, 580, 1080, 150, 22, "#FFFFFF", acc, shadow=True)
        text(c, "CONFERÊNCIA", 960, 625, 24, "black", GREEN, acc, tracking=2)
        K.expr(c, "A · A^{-1} = I", 960, 685, 46, acc, cores={i: GREEN for i in range(20)})


# ======================================================================
# bloco f — códigos
# ======================================================================

def b_codigo(c, t, C, B):
    head(c, t, B["start"], "PARA QUE SERVE?", "MENSAGENS CODIFICADAS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        text(c, "“O I”", 330, 320, 50, "black", INK, aa)
        arrow(c, 420, 305, 500, 305, GRAY, aa, 3, 10)
        matriz(c, 570, 305, [["15"], ["9"]], 40, aa, col=BLUE)
        text(c, "letra → número → COLUNA", 450, 420, 24, "bold", INK2, aa)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        cadeado(c, 860, 320, 110, ab, 0)
        text(c, "CODIFICAR = trancar", 860, 430, 26, "black", PURPLE, ab)
        K.expr(c, "A · M = E", 1180, 305, 44, ab, cores={i: PURPLE for i in range(20)})
        text(c, "A = matriz-chave", 1180, 380, 24, "bold", INK2, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        rrect(c, 260, 480, 1400, 140, 22, mix("#FFFFFF", GREEN, 0.10), acc)
        cadeado(c, 380, 560, 90, acc, clamp((t - C["15.c"] - 1.0) / 0.8))
        text(c, "DECODIFICAR = destrancar:", 470, 562, 32, "black", GREEN, acc, align="left")
        K.expr(c, "A^{-1} · E = M", 1250, 552, 44, acc, cores={i: GREEN for i in range(20)})
        text(c, "“O I” de volta", 1560, 562, 26, "black", GREEN, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        rrect(c, 260, 650, 1400, 140, 22, mix("#FFFFFF", RED, 0.08), ad)
        text(c, "inversa com um SINAL errado:", 300, 732, 32, "black", RED, ad, align="left")
        lixo = "#&%  ¿Q*" if int(t * 6) % 2 else "%Q#  *&¿"
        text(c, lixo, 1060, 736, 50, "black", RED, ad)
        selo(c, 1450, 720, ad, "SAI LIXO", RED, -5, 30)


# ======================================================================
# nós fazemos
# ======================================================================

N_ = [["2", "1"], ["3", "2"]]
NI = [["2", "−1"], ["−3", "2"]]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "TROCA, SINAL, DIVIDE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        linha(c, [("inversa de  ", INK)], 640, 290, 44, aa)
        matriz(c, 870, 290, N_, 44, aa)
        linha(c, [("  e confira", AMBER)], 1100, 290, 44, aa)
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, 960, 560)
        return
    a1 = ep(t, C["17.a"], 0.5)
    if a1 > 0:
        linha(c, [("ad − bc = 2·2 − 1·3 = 4 − 3 = ", INK), ("1", GREEN)], 960, 420, 40, a1)
    a2 = ep(t, C["17.b"], 0.5)
    if a2 > 0:
        for k, (s_, col) in enumerate((("TROCA", PURPLE), ("SINAL", RED), ("÷ 1", GREEN))):
            chip(c, s_, 660 + k * 300, 520, col, a2 * ep(t, C["17.b"] + 0.6 * k, 0.3), size=32, w=220)
    a3 = ep(t, C["17.c"], 0.5)
    if a3 > 0:
        K.expr(c, "A^{-1} =", 680, 660, 44, a3, cores={i: GREEN for i in range(10)})
        matriz(c, 880, 660, NI, 40, a3, col=GREEN)
    a4 = ep(t, C["17.d"], 0.5)
    if a4 > 0:
        xs = prod(c, 1360, 660, [N_, "·", NI, "="], 26, a4, gap=14)
        w = mat_dims(I_, 26)[0]
        matriz(c, xs[-1] + 34 + w / 2, 660, I_, 26, a4, col=GREEN)
        check_icon(c, 1730, 660, 22, a4, GREEN)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["A ordem dos fatores altera o produto.",
          "Produto zero não exige fator zero.",
          "Inversa 2 × 2: troca a diagonal, muda o sinal da secundária, divide por ad − bc."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Supor que A · B = B · A", "nos números, a ordem nunca importou",
          "com as matrizes do começo, a 1ª casa dá 7 numa ordem e 1 na outra"),
         ("De A · B = 0, concluir que A = 0 ou B = 0", "nos números, essa regra vale sempre",
          "o exemplo do gancho derruba: o produto é nulo e nenhum fator é"),
         ("Inversa só TROCANDO a diagonal", "a troca é o movimento que mais aparece",
          "em (2 1 / 3 2), trocar devolve a própria matriz; o produto dá (7 4 / 12 7), não é I")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALT4 = [("A", "a matriz nula, pois AB = BA", "supôs AB = BA"), ("B", [["6", "0"], ["0", "−6"]], ""),
        ("C", [["−6", "0"], ["0", "6"]], "fez BA − AB"), ("D", [["0", "2"], ["−3", "0"]], "A − B, sem multiplicar"),
        ("E", I_, "identidade, sem relação")]


def b_q4(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 4 · EU FAÇO", "A ORDEM DOS FATORES", PURPLE)
    card(c, *CARD_R)
    a0 = ep(t, C["22.a"], 0.4)
    if a0 > 0:
        text(c, "Considere as matrizes", 190, 250, 30, "black", INK, a0, align="left")
        linha(c, [("A = ", INK)], 230, 340, 36, a0, align="left")
        matriz(c, 400, 340, A_, 36, a0)
        linha(c, [("B = ", INK)], 530, 340, 36, a0, align="left")
        matriz(c, 700, 340, B_, 36, a0)
        text(c, "A matriz A · B − B · A é", 190, 450, 30, "black", INK, a0, align="left")
    cues_in = {L: C[f"22.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"24.x{L.lower()}"] for L in "ACDE"}
    alt_mat(c, t, C, ALT4, 960, 220, C["23.ok"], "B", cues_in, cues_x, size=26, gap=14, w=720)
    a1 = ep(t, C["23.a"], 0.5)
    if a1 > 0:
        rrect(c, 170, 500, 740, 320, 18, "#FFFFFF", a1, shadow=True)
        text(c, "AB", 300, 560, 30, "black", PURPLE, a1)
        matriz(c, 300, 640, AB, 34, a1, cores={(0, 0): PURPLE, (1, 1): PURPLE})
        text(c, "−", 450, 650, 44, "black", GRAY, a1)
        text(c, "BA", 600, 560, 30, "black", AMBER, a1)
        matriz(c, 600, 640, BA, 34, a1, cores={(0, 0): AMBER, (1, 1): AMBER})
    a2 = ep(t, C["23.b"], 0.5)
    if a2 > 0:
        text(c, "=", 730, 650, 44, "black", GRAY, a2)
        al = {(0, 0): ep(t, C["23.b"] + 0.8, 0.3), (0, 1): ep(t, C["23.b"] + 2.0, 0.3),
              (1, 0): ep(t, C["23.b"] + 3.2, 0.3), (1, 1): ep(t, C["23.b"] + 4.4, 0.3)}
        matriz(c, 830, 640, [["6", "0"], ["0", "−6"]], 30, a2, col=GREEN, alfas=al)
        text(c, "casa a casa", 540, 790, 24, "bold", INK2, a2)


ALT9 = [("A", "=A · I = I · A = A", "", GREEN), ("B", "=A · B = B · A", "a ordem importa", RED),
        ("C", "=(A+B)^{2} = A^{2} + 2AB + B^{2}", "AB e BA podem diferir", RED),
        ("D", "=(A·B)^{t} = A^{t} · B^{t}", "a ordem se inverte", RED),
        ("E", "se A · B = 0, então A = 0 ou B = 0", "o gancho derruba", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · NÓS FAZEMOS", "A ÚNICA VERDADEIRA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    yend = _enunciado(c, [("Um estudante listou afirmações sobre matrizes quadradas A e B de mesma ordem, sendo I a "
                           "identidade e 0 a matriz nula. A única afirmação verdadeira para quaisquer A e B é", INK)],
                      a0, 250, 30)
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALT9, 960, 230, 720, 28, C["26.ok"], "A", cues_in, cues_x, gap=22)
    if t < C["26"]:
        pause_timer(c, t, C["25.end"] - 1.9, 540, yend + 120)
        return
    a1 = ep(t, C["26.a"], 0.5)
    if a1 > 0:
        rrect(c, 170, yend + 30, 740, 200, 18, "#FFFFFF", a1, shadow=True)
        text(c, "a identidade é o número 1", 540, yend + 100, 32, "black", BLUE, a1)
        text(c, "DOS DOIS LADOS", 540, yend + 160, 36, "black", GREEN, a1)


ALT6 = [("A", "2 e 5.", "inverteu a ordem", RED), ("B", "−5 e −2.", "sinais na diagonal principal", RED),
        ("C", "63 e 172.", "só trocou a diagonal", RED), ("D", "5 e 2.", "", GREEN),
        ("E", "80 e 143.", "multiplicou de novo por A", RED)]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · VOCÊ FAZ", "DECIFRAR COM A INVERSA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    if a0 > 0:
        yy = _enunciado(c, [("Um sistema de mensagens converte cada par de letras em uma matriz coluna M com dois "
                             "números e envia E = A · M, em que", INK)], a0, 245, 28, 720)
        linha(c, [("A = ", INK)], 230, yy + 30, 32, a0, align="left")
        matriz(c, 370, yy + 30, K_, 32, a0)
        linha(c, [("E = ", INK)], 520, yy + 30, 32, a0, align="left")
        matriz(c, 640, yy + 30, [["17"], ["29"]], 32, a0)
        yend = _enunciado(c, [("Os dois números originais, de cima para baixo, eram", INK)], a0, yy + 130, 28, 720)
    else:
        yend = 600
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALT6, 1000, 260, 680, 32, C["28.ok"], "D", cues_in, cues_x, gap=30)
    if t < C["28"]:
        pause_timer(c, t, C["27.end"] - 1.9, 540, min(yend + 90, 780))
        return
    y0 = 206
    a1 = ep(t, C["28"], 0.4)
    rrect(c, 170, y0, 760, 830 - y0, 18, "#FFFFFF", a1, shadow=True)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        K.expr(c, "A^{-1} =", 400, y0 + 80, 36, aa, cores={i: CHAVE for i in range(10)})
        matriz(c, 580, y0 + 80, KI, 32, aa, col=CHAVE)
        chave(c, 790, y0 + 80, 90, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        K.expr(c, "M = A^{-1} · E", 550, y0 + 200, 36, ab, cores={i: GREEN for i in range(20)})
        text(c, "2·17 − 29 = 5", 550, y0 + 280, 32, "black", INK, ep(t, C["28.b"] + 1.5, 0.4))
        text(c, "−5·17 + 3·29 = 2", 550, y0 + 340, 32, "black", INK, ep(t, C["28.b"] + 3.5, 0.4))
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        rrect(c, 220, y0 + 400, 660, 170, 18, mix("#FFFFFF", GREEN, 0.12), acc)
        text(c, "CONFERÊNCIA", 550, y0 + 445, 22, "black", GREEN, acc, tracking=2)
        text(c, "3·5 + 1·2 = 17  ✓", 550, y0 + 500, 30, "black", INK, acc)
        text(c, "5·5 + 2·2 = 29  ✓", 550, y0 + 548, 30, "black", INK, acc)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO DE MATRIZES", PURPLE)
    itens = [("31.a", "JUNTAMOS TUDO", PURPLE), ("31.b", "CAÇAMOS AS PEGADINHAS", AMBER),
             ("31.c", "QUESTÕES INÉDITAS", GREEN)]
    for k, (cue, s_, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 300, 460, 260, 26, mix("#FFFFFF", col, 0.12), ak)
        badge_num(c, k + 1, x, 380, ak, 34, bg=col)
        text(c, s_, x, 490, 32, "black", col, ak)
    ac = ep(t, C["31.c"] + 1.2, 0.5)
    if ac > 0:
        selo(c, W / 2, 700, ac, "ÚLTIMO EPISÓDIO DO ASSUNTO", AMBER, -3, 38)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Qual regra dos números você mais se surpreendeu ao ver falhar nas matrizes?", canal="no Estudativo",
        anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, ordem=b_ordem,
              nem_existe=b_nem_existe, atalho_ordem=b_atalho_ordem, nulo=b_nulo, props=b_props, props2=b_props2,
              inversa=b_inversa, receita=b_receita, confere=b_confere, atalho_receita=b_atalho_receita,
              codigo=b_codigo, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q4=b_q4, q9=b_q9, q6=b_q6,
              ponte=b_ponte, cta=b_cta)
