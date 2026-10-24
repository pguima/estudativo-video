"""Visual — Matrizes e Operações, Episódio 2: operações casa a casa (igualdade, soma e número vezes matriz) (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: matriz() (matriz com colchetes, casas coloridas e acesas uma a uma), folha() (a folha transparente
que desliza sobre a outra), carimbo() (o ×3 batendo em cada casa), planilha() (a tabela de notas com alunos e
disciplinas).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum048", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                          K.pause_timer)
ftext, ftext_w = K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_matrizes_ep2_casa_a_casa.mp4"
CARD_R = K.CARD_R


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


def mat_wh(vals, cw, ch):
    return len(vals[0]) * cw + 40, len(vals) * ch + 20


def matriz(c, cx, cy, vals, a, cw=110, ch=86, size=46, cores=None, alfas=None, hi=None, hi_col=None, br=None,
           colchete=1.0):
    """matriz centrada em (cx, cy): vals = linhas de strings ('' = casa vazia); cores/alfas = {(i, j): ...};
    hi = conjunto de casas acesas (fundo colorido). Devolve (largura, altura)."""
    w, h = mat_wh(vals, cw, ch)
    if a <= 0:
        return w, h
    x0, y0 = cx - w / 2, cy - h / 2
    bcol = br or INK
    for xx, sg in ((x0, 1), (x0 + w, -1)):
        if colchete <= 0:
            break
        line(c, xx, y0, xx, y0 + h, bcol, a * colchete, 5)
        line(c, xx, y0, xx + 18 * sg, y0, bcol, a * colchete, 5)
        line(c, xx, y0 + h, xx + 18 * sg, y0 + h, bcol, a * colchete, 5)
    for i, row in enumerate(vals):
        for j, s_ in enumerate(row):
            ccx = x0 + 20 + cw * (j + 0.5)
            ccy = y0 + 10 + ch * (i + 0.5)
            if hi and (i, j) in hi:
                rrect(c, ccx - cw / 2 + 6, ccy - ch / 2 + 6, cw - 12, ch - 12, 14, mix("#FFFFFF", hi_col or AMBER, 0.30),
                      a)
            if not s_:
                continue
            al = (alfas or {}).get((i, j), 1.0)
            if al <= 0:
                continue
            sz = size if ftext_w(s_, "black", size) < cw - 14 else size * (cw - 14) / ftext_w(s_, "black", size)
            ftext(c, s_, ccx, ccy + sz * 0.36, sz, "black", (cores or {}).get((i, j), INK), a * al)
    return w, h


def sub(c, base, s, cx, cy, size, col, a):
    """base com subscrito (a + ij), centrado em (cx, cy)"""
    if a <= 0:
        return
    wb, ws = ftext_w(base, "black", size), ftext_w(s, "black", size * 0.55)
    x = cx - (wb + ws) / 2
    ftext(c, base, x, cy + size * 0.36, size, "black", col, a, align="left")
    ftext(c, s, x + wb + 2, cy + size * 0.62, size * 0.55, "black", col, a, align="left")


def folha(c, cx, cy, w, h, a, col, rot=None):
    """a folha transparente (planilha) atrás de uma matriz"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 20, mix("#FFFFFF", col, 0.14), a * 0.85, shadow=True, stroke=4,
          stroke_color=mix("#FFFFFF", col, 0.6))
    if rot:
        pill(c, rot, cx, cy - h / 2, col, size=22, a=a, anchor="center", bounds=(0, 1920))


def carimbo(c, cx, cy, a, s="×3", col=None, r=34):
    """o carimbo que bate numa casa (aparece grande e encolhe até o tamanho final)"""
    if a <= 0:
        return
    col = col or PURPLE
    k = 1.0 + 0.6 * (1 - a)
    c.drawCircle(cx, cy, r * k, paint(mix("#FFFFFF", col, 0.25), a))
    c.drawCircle(cx, cy, r * k, paint(col, a, stroke=4))
    text_mid(c, s, cx, cy, 26 * k, "black", col, a)


def planilha(c, cx, cy, notas, a, titulo, col, alunos=("Ana", "Bia", "Caio"), discs=("MAT", "PORT"), hi=None,
             rotulos=1.0, num_col=None, fundo=1.0):
    """tabela de notas com alunos nas linhas e disciplinas nas colunas (rotulos = alfa de nomes e título)"""
    if a <= 0:
        return
    w, h = 420, 340
    folha(c, cx, cy, w, h, a * fundo, col, titulo if rotulos > 0.5 else None)
    x0, y0 = cx - w / 2, cy - h / 2
    for j, d in enumerate(discs):
        text(c, d, x0 + 200 + 120 * j, y0 + 70, 24, "black", col, a * rotulos)
    for i, nome in enumerate(alunos):
        yy = y0 + 130 + 80 * i
        text(c, nome, x0 + 40, yy + 10, 28, "bold", INK2, a * rotulos, align="left")
        for j in range(len(discs)):
            if hi and (i, j) in hi:
                rrect(c, x0 + 200 + 120 * j - 46, yy - 30, 110, 72, 12, mix("#FFFFFF", AMBER, 0.35), a)
            text_mid(c, notas[i][j], x0 + 200 + 120 * j, yy, 40, "black", num_col or INK, a)


def cartao(c, x, y, w, h, a, col=None, fill=False):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 24, mix("#FFFFFF", col, 0.10) if (fill and col) else "#FFFFFF", a, shadow=True)


def defin(c, termo, s, x, y, w, a, col=None, size=30):
    """faixa de definição: TERMO: frase"""
    if a <= 0:
        return
    col = col or BLUE
    rrect(c, x, y, w, 76, 18, mix("#FFFFFF", col, 0.12), a)
    linha(c, [(termo, col), (": " + s, INK)], x + 28, y + 38, size, a, align="left")


def sinal(c, s, x, y, a, col=None, size=60):
    if a > 0:
        ftext(c, s, x, y + size * 0.36, size, "black", col or INK, a)


# dados
A_SOMA = [["1", "4"], ["2", "0"]]
B_SOMA = [["3", "−1"], ["5", "2"]]
R_SOMA = [["4", "3"], ["7", "2"]]
R_3A = [["3", "12"], ["6", "0"]]
QA = [["5", "8"], ["7", "4"], ["6", "6"]]
QB = [["7", "5"], ["5", "8"], ["6", "5"]]
QM = [["6,2", "6,2"], ["5,8", "6,4"], ["6,0", "5,4"]]
CASAS = [(0, 0), (0, 1), (1, 0), (1, 1)]


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "MATRIZES · EPISÓDIO 2", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        planilha(c, 460, 400, QA, aa, "PROVA 1", BLUE, alunos=("aluno 1", "aluno 2", "aluno 3"))
        planilha(c, 1000, 400, QB, ep(t, C["01.a"] + 0.6, 0.4), "PROVA 2", PURPLE,
                 alunos=("aluno 1", "aluno 2", "aluno 3"))
        ak = ep(t, C["01.a"] + 2.6, 0.4)
        if ak > 0:
            rrect(c, 1290, 300, 400, 200, 26, mix("#FFFFFF", AMBER, 0.18), ak, shadow=True)
            text_mid(c, "6", 1400, 400, 120, "black", AMBER, ak)
            text(c, "médias", 1540, 390, 40, "black", INK, ak)
            text(c, "ponderadas", 1540, 440, 30, "bold", INK2, ak)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 620, 960, 130, 26, "#FFFFFF", ab, shadow=True)
        pill(c, "UMA CONTA SÓ", 340, 620, PURPLE, size=22, a=ab, bounds=(0, 1920))
        text_mid(c, "M = 0,4A + 0,6B", 780, 688, 70, "black", PURPLE, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        selo(c, 1490, 690, acc, "6,0 TAMBÉM APROVA?", AMBER, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "MATRIZES · EP. 2", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "2º episódio da série de MATRIZES", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "SOMAR", "casa com casa", BLUE, 0), ("02.a", "× NÚMERO", "todas as casas", PURPLE, 1.0),
             ("02.b", "IGUALDADE", "sem errar uma casa", GREEN, 0)]
    for k, (cue, tit, sub, col, dt) in enumerate(itens):
        ak = ep(t, C[cue] + dt, 0.5)
        if ak <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 220, 340, 440, 320, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 220, 340, 440, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 44, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    a, d = rise(t, C["03.a"])
    if a > 0:
        y = 300 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "episódio 1", 300, y - 75, BLUE, size=22, a=a)
        sub(c, "a", "ij", 560, y, 70, BLUE, a)
        text(c, "linha i · coluna j", 1050, y + 14, 40, "black", INK, a)
    a, d = rise(t, C["03.b"])
    if a > 0:
        y = 500 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "série de Sistemas", 300, y - 75, PURPLE, size=22, a=a)
        text_mid(c, "x + y = 7", 520, y - 22, 40, "black", INK, a)
        text_mid(c, "x − y = 1", 520, y + 28, 40, "black", INK, a)
        ak = ep(t, C["03.b"] + 4.0, 0.4)
        if ak > 0:
            arrow(c, 700, y, 820, y, PURPLE, ak, 5, 16)
            text_mid(c, "somando:  2x = 8", 1130, y, 48, "black", PURPLE, ak)
    a, d = rise(t, C["03.c"])
    if a > 0:
        y = 700 + d
        cartao(c, 260, y - 75, 1400, 150, a)
        pill(c, "decimal × inteiro", 300, y - 75, GREEN, size=22, a=a)
        text_mid(c, "0,4 · 5 = 2", 960, y, 60, "black", GREEN, a)


# ======================================================================
# concreto — as duas planilhas e as folhas transparentes
# ======================================================================

P1 = [["6", "7"], ["5", "8"], ["9", "4"]]
P2 = [["8", "5"], ["7", "6"], ["7", "8"]]


def b_planilhas(c, t, C, B):
    head(c, t, B["start"], "DUAS PLANILHAS", "A MESMA TURMA, DUAS PROVAS", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    ab = ep(t, C["04.b"], 0.5)
    v = ease_io(clamp((t - C["04.c"] - 0.6) / 1.6))
    x2 = 1240 + (764 - 1240) * v
    hi = {(1, 0)} if v > 0.95 else None
    planilha(c, 720, 470, P1, aa, "PROVA 1", BLUE, hi=hi)
    planilha(c, x2, 470 + 26 * v, P2, ep(t, C["04.a"] + 1.2, 0.4), "PROVA 2", PURPLE, rotulos=1 - v, num_col=PURPLE,
             fundo=1 - 0.6 * v)
    if ab > 0:
        pill(c, "mesmos ALUNOS nas linhas", 480, 230, BLUE, size=24, a=ab * (1 - v), anchor="center")
        pill(c, "mesmas DISCIPLINAS nas colunas", 1240, 230, PURPLE, size=24, a=ab * (1 - v), anchor="center")
    acc = ep(t, C["04.c"] + 2.4, 0.5)
    if acc > 0:
        rrect(c, 1180, 380, 520, 180, 24, mix("#FFFFFF", AMBER, 0.16), acc, shadow=True)
        para(c, "cada casa só conversa com a casa de baixo", 1210, 440, 34, "black", INK, acc, 470, 44)


def b_definicoes(c, t, C, B):
    head(c, t, B["start"], "DOIS NOMES", "ANTES DAS CONTAS", BLUE)
    card(c, *CARD_R)
    aa, d = rise(t, C["05.a"])
    defin(c, "MESMA ORDEM", "o mesmo número de linhas e de colunas", 260, 230 + d, 1400, aa, BLUE, 34)
    ab, d2 = rise(t, C["05.b"])
    vals = [["", "", ""], ["", "", ""]]
    hi = {(1, 2)} if ab > 0 else None
    if aa > 0:
        for cx in (620, 1300):
            matriz(c, cx, 470 + d, vals, aa, 90, 76, 32, hi=hi, hi_col=AMBER)
            if ab > 0:
                sub(c, "a", "23", cx - 155 + 20 + 90 * 2.5, 470 + d - 86 + 10 + 76 * 1.5, 34, AMBER, ab)
            text(c, "2 × 3", cx, 610 + d, 34, "black", BLUE, aa)
        text_mid(c, "e", 960, 470 + d, 50, "black", BLUE, aa)
    defin(c, "ELEMENTOS CORRESPONDENTES", "moram no mesmo endereço", 260, 690 + d2, 1400, ab, AMBER, 34)


# ======================================================================
# bloco a — igualdade
# ======================================================================

def b_igualdade(c, t, C, B):
    head(c, t, B["start"], "IGUALDADE DE MATRIZES", "UM SISTEMA DISFARÇADO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    defin(c, "IGUALDADE", "mesma ordem e casa por casa igual", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["06.b"], 0.5)
    acc = ep(t, C["06.c"], 0.5)
    hi = {(0, 0), (1, 1)} if acc > 0 else None
    matriz(c, 620, 440, [["x + y", "3"], ["2", "x − y"]], ab, 170, 100, 44, hi=hi, hi_col=PURPLE)
    sinal(c, "=", 860, 440, ab)
    matriz(c, 1040, 440, [["7", "3"], ["2", "1"]], ab, 110, 100, 48, hi=hi, hi_col=PURPLE)
    if acc > 0:
        rrect(c, 1240, 330, 420, 220, 22, mix("#FFFFFF", PURPLE, 0.12), acc, shadow=True)
        text_mid(c, "x + y = 7", 1450, 395, 48, "black", PURPLE, acc)
        text_mid(c, "x − y = 1", 1450, 480, 48, "black", PURPLE, ep(t, C["06.c"] + 0.8, 0.4))
        pill(c, "cada casa vira uma equação", 840, 620, PURPLE, size=26, a=acc, anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 690, 1000, 110, 22, mix("#FFFFFF", GREEN, 0.14), ad)
        linha(c, [("somando:  2x = 8   →   ", INK), ("x = 4", GREEN), ("   ·   ", INK2),
                  ("y = 3", GREEN)], 960, 745, 46, ad)


# ======================================================================
# bloco b — soma (folhas transparentes) · bloco c — número × matriz (carimbo)
# ======================================================================

def b_soma(c, t, C, B):
    head(c, t, B["start"], "SOMA DE MATRIZES", "FOLHA SOBRE FOLHA", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    v = ease_io(clamp((t - C["07.a"] - 1.6) / 1.4))
    # A fica; B desliza para cima de A e para deslocada, com os pares lado a lado
    xa, xb = 500, 1000 - (1000 - 542) * v
    on = [C["07.b"], C["07.b"] + 2.6, C["07.c"], C["07.c"] + 2.0]
    lit = {CASAS[k] for k in range(4) if t >= on[k]}
    cur = {CASAS[k] for k in range(4) if on[k] <= t < (on[k + 1] if k < 3 else C["07.d"])}
    folha(c, xa, 430, 360, 320, aa, BLUE, "A")
    matriz(c, xa, 430, A_SOMA, aa, 130, 110, 46, hi=cur, hi_col=AMBER, br=BLUE)
    folha(c, xb, 430 + 28 * v, 360, 320, aa * (0.9 - 0.5 * v), PURPLE, "B" if v < 0.5 else None)
    matriz(c, xb, 430 + 28 * v, B_SOMA, aa, 130, 110, 46 - 12 * v, cores={k: PURPLE for k in CASAS}, br=PURPLE,
           colchete=1 - v)
    if aa > 0:
        pill(c, "+", (xa + xb) / 2, 640, PURPLE, size=40, a=aa * (1 - v), anchor="center")
    if lit:
        sinal(c, "=", 900, 440, 1.0)
        folha(c, 1300, 440, 330, 300, 1.0, GREEN, "A + B")
        matriz(c, 1300, 440, R_SOMA, 1.0, 110, 86, 46, alfas={k: (1.0 if k in lit else 0) for k in CASAS},
               cores={k: GREEN for k in CASAS}, br=GREEN)
        contas = {(0, 0): "1 + 3", (0, 1): "4 + (−1)", (1, 0): "2 + 5", (1, 1): "0 + 2"}
        for k in cur:
            pill(c, contas[k] + " = " + R_SOMA[k[0]][k[1]], 900, 660, AMBER, size=30, a=1.0, anchor="center")
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        rrect(c, 360, 720, 1200, 90, 20, mix("#FFFFFF", PURPLE, 0.12), ad)
        linha(c, [("subtração: casa − casa  ·  só na ", INK), ("MESMA ORDEM", PURPLE)], 960, 765, 38, ad)


def b_numero(c, t, C, B):
    head(c, t, B["start"], "NÚMERO × MATRIZ", "AUMENTO GERAL", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    sinal(c, "3 ·", 420, 450, aa, PURPLE, 80)
    matriz(c, 640, 450, A_SOMA, aa, 120, 100, 52)
    sinal(c, "=", 900, 450, aa, INK, 70)
    batidas = [C["08.b"], C["08.b"] + 2.2, C["08.c"], C["08.c"] + 2.2]
    for k, (i, j) in enumerate(CASAS):
        ak = ep(t, batidas[k], 0.35) * (1 - ep(t, batidas[k] + 1.2, 0.4))
        ccx = 640 - 140 + 20 + 120 * (j + 0.5)
        ccy = 450 - 110 + 10 + 100 * (i + 0.5)
        carimbo(c, ccx + 40, ccy - 30, ak)
    alf = {CASAS[k]: ep(t, batidas[k] + 0.3, 0.3) for k in range(4)}
    matriz(c, 1160, 450, R_3A, aa, 130, 100, 52, alfas=alf, cores={k: PURPLE for k in CASAS}, br=PURPLE)
    if aa > 0:
        pill(c, "TODO MUNDO recebe", 960, 640, PURPLE, size=30, a=aa, anchor="center")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        selo(c, 960, 750, ad, "O ×3 BATE EM TODAS AS CASAS", GREEN, -3, 40)


def b_atalho_ordem(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ANTES DE QUALQUER CONTA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · CASA A CASA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        text(c, "1 · CONFIRA A ORDEM", 960, 340, 44, "black", INK, aa)
        matriz(c, 700, 460, [["•", "•"], ["•", "•"]], aa, 70, 60, 40)
        text_mid(c, "+", 840, 460, 50, "black", INK, aa)
        matriz(c, 1000, 460, [["•", "•", "•"], ["•", "•", "•"]], aa, 70, 60, 40)
        text(c, "2 × 2  e  2 × 3:  a soma NÃO EXISTE", 960, 590, 32, "bold", RED, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        text(c, "2 · IGUALDADE: SOME AS EQUAÇÕES", 960, 680, 40, "black", INK, ab)
        text(c, "(x + y) + (x − y) = 2x  ·  o y some", 960, 745, 34, "bold", GREEN, ab)


# ======================================================================
# bloco d — média ponderada
# ======================================================================

def b_media(c, t, C, B):
    head(c, t, B["start"], "MÉDIA PONDERADA", "CADA NOTA TEM UM PESO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    defin(c, "MÉDIA PONDERADA", "cada nota pesa diferente", 260, 200, 1400, aa, BLUE, 32)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        rrect(c, 460, 320, 1000, 120, 24, "#FFFFFF", ab, shadow=True)
        text_mid(c, "M = 0,4A + 0,6B", 960, 380, 64, "black", PURPLE, ab)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        for k, (rot, n, col) in enumerate((("prova 1", "5", BLUE), ("prova 2", "8", PURPLE))):
            x = 560 + k * 300
            rrect(c, x - 110, 480, 220, 150, 22, mix("#FFFFFF", col, 0.14), acc)
            text(c, rot, x, 520, 26, "bold", col, acc)
            text_mid(c, n, x, 585, 70, "black", INK, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        text_mid(c, "0,4 · 5 = 2", 1330, 500, 44, "black", INK, ad)
        text_mid(c, "0,6 · 8 = 4,8", 1330, 570, 44, "black", INK, ep(t, C["10.d"] + 2.0, 0.4))
        a2 = ep(t, C["10.d"] + 4.4, 0.4)
        if a2 > 0:
            rrect(c, 1150, 610, 360, 80, 18, mix("#FFFFFF", GREEN, 0.16), a2)
            text_mid(c, "M = 6,8", 1330, 650, 48, "black", GREEN, a2)
    ae = ep(t, C["10.e"], 0.5)
    if ae > 0:
        pill(c, "na matriz: POSIÇÃO POR POSIÇÃO", 960, 760, PURPLE, size=30, a=ae, anchor="center")


def b_atalho_media(c, t, C, B):
    head(c, t, B["start"], "ATALHO PARA CONFERIR", "A MÉDIA FICA ENTRE AS NOTAS", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["11"], 0.4)
    if a0 > 0:
        K.boxed(c, 260, 200, 1400, 600, GREEN, a0, 0.08)
        text(c, "ATALHO · CONFERÊNCIA DA MÉDIA", 960, 250, 24, "black", GREEN, a0, tracking=2)
    aa = ep(t, C["11.a"], 0.5)
    x0, x1, y = 420, 1500, 520
    if aa > 0:
        line(c, x0, y, x1, y, INK, aa, 6)
        for n in range(5, 9):
            xx = x0 + (x1 - x0) * (n - 5) / 3
            line(c, xx, y - 18, xx, y + 18, INK, aa, 5)
            text(c, str(n), xx, y + 70, 40, "black", INK, aa)
        rrect(c, x0 - 10, y - 14, x1 - x0 + 20, 28, 14, mix("#FFFFFF", GREEN, 0.4), aa * 0.6)
        text(c, "ENTRE as duas notas", 960, 400, 40, "black", INK, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        xm = x0 + (x1 - x0) * (6.8 - 5) / 3
        c.drawCircle(xm, y, 22, paint(GREEN, ab))
        text(c, "6,8", xm, y - 50, 46, "black", GREEN, ab)
        pill(c, "mais perto da nota de PESO MAIOR", 960, 680, GREEN, size=32, a=ab, anchor="center")
        text(c, "peso 0,4", x0, y + 120, 26, "bold", INK2, ab)
        text(c, "peso 0,6", x1, y + 120, 26, "bold", PURPLE, ab)


# ======================================================================
# bloco e — propriedades e 2X + A = B
# ======================================================================

def b_propriedades(c, t, C, B):
    head(c, t, B["start"], "COMO NOS NÚMEROS", "AS REGRAS DA SOMA", PURPLE)
    card(c, *CARD_R)
    itens = [("12.a", "A + B = B + A", "a ordem não importa", PURPLE),
             ("12.b", "A + 0 = A", "matriz nula: elemento neutro", BLUE),
             ("12.b", "−A", "a oposta: troca o sinal de cada casa", BLUE)]
    dts = [0, 0, 3.6]
    for k, (cue, f, sub, col) in enumerate(itens):
        ak = ep(t, C[cue] + dts[k], 0.5) * (1 - ep(t, C["12.c"], 0.4))
        if ak <= 0:
            continue
        y = 270 + k * 150
        rrect(c, 300, y - 50, 1320, 110, 22, "#FFFFFF", ak, shadow=True)
        text(c, f, 560, y + 20, 52, "black", col, ak)
        text(c, sub, 1580, y + 16, 30, "bold", INK2, ak, align="right")
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 200, 1320, 120, 24, mix("#FFFFFF", PURPLE, 0.12), acc)
        linha(c, [("2X + A = B   →   ", INK), ("X = (B − A) ÷ 2", PURPLE)], 960, 260, 54, acc)
        pill(c, "como no 1º grau, casa a casa", 960, 340, PURPLE, size=24, a=acc, anchor="center")
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        matriz(c, 420, 560, [["5", "6"], ["8", "2"]], ad, 90, 80, 40)
        sinal(c, "−", 560, 560, ad, INK, 54)
        matriz(c, 700, 560, A_SOMA, ad, 90, 80, 40)
        sinal(c, "=", 840, 560, ad, INK, 54)
        matriz(c, 980, 560, [["4", "2"], ["6", "2"]], ad, 90, 80, 40)
        a2 = ep(t, C["12.d"] + 4.2, 0.4)
        if a2 > 0:
            sinal(c, "÷ 2 =", 1180, 560, a2, PURPLE, 50)
            matriz(c, 1400, 560, [["2", "1"], ["3", "1"]], a2, 90, 80, 44, cores={k: GREEN for k in CASAS}, br=GREEN)
            text(c, "X", 1400, 700, 40, "black", GREEN, a2)
        text(c, "B", 420, 700, 34, "black", INK2, ad)
        text(c, "A", 700, 700, 34, "black", INK2, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("13", "SUA VEZ", "PAUSE E TENTE", GREEN), ("14", "VAMOS JUNTOS", "CARIMBO, DEPOIS CASA − CASA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    MA, MB = [["2", "5"], ["1", "3"]], [["4", "1"], ["3", "7"]]
    if t < C["14"]:
        text(c, "A =", 520, 420, 56, "black", BLUE, aa, align="right")
        matriz(c, 640, 400, MA, aa, 100, 86, 46)
        text(c, "B =", 1110, 420, 56, "black", PURPLE, aa, align="right")
        matriz(c, 1230, 400, MB, aa, 100, 86, 46)
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            rrect(c, 710, 540, 500, 100, 22, mix("#FFFFFF", GREEN, 0.14), ab)
            text_mid(c, "2A − B = ?", 960, 590, 56, "black", GREEN, ab)
        pause_timer(c, t, C["13.end"] - 1.9, 960, 730)
        return
    a1 = ep(t, C["14.a"], 0.5)
    sinal(c, "2A =", 320, 330, a1, PURPLE, 50)
    matriz(c, 520, 330, [["4", "10"], ["2", "6"]], a1, 100, 80, 42, cores={k: PURPLE for k in CASAS}, br=PURPLE)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        on = [C["14.b"], C["14.b"] + 2.2, C["14.c"], C["14.c"] + 2.0]
        lit = {CASAS[k] for k in range(4) if t >= on[k]}
        matriz(c, 520, 600, [["4", "10"], ["2", "6"]], ab, 100, 80, 42, cores={k: PURPLE for k in CASAS})
        sinal(c, "−", 700, 600, ab, INK, 54)
        matriz(c, 880, 600, MB, ab, 100, 80, 42)
        sinal(c, "=", 1060, 600, ab, INK, 54)
        matriz(c, 1260, 600, [["0", "9"], ["−1", "−1"]], ab, 110, 80, 42,
               alfas={k: (1.0 if k in lit else 0) for k in CASAS}, cores={k: GREEN for k in CASAS}, br=GREEN)
        text(c, "2A − B", 1260, 740, 30, "black", GREEN, ab)


# ======================================================================
# recap e erros
# ======================================================================

FRASES = ["Soma e igualdade: casa com casa, na mesma ordem.",
          "Número vezes matriz atinge todas as casas.",
          "Igualdade de matrizes vira um sistema."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["15", "24"])
    frame(c, t, B["start"] if sid == "15" else C["24"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "15" else "PARA FECHAR",
          PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Em 3 · A, multiplicar só a primeira linha",
          "na conta de números, o 3 aparece uma vez só",
          "é aumento geral: o ×3 bate em TODAS as casas."),
         ("Somar uma 2 × 2 com uma 2 × 3",
          "números sempre dá para somar",
          "uma casa sem par não tem com quem somar: a soma NÃO EXISTE.")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["16", "17"], ERROS)


# ======================================================================
# questão 8 em três tempos
# ======================================================================

ALTS8 = [("A", "1", "alunos aprovados nas duas", RED), ("B", "2", "contou as abaixo de 6", RED),
         ("C", "3", "trocou os pesos", RED), ("D", "4", "", GREEN), ("E", "5", "média simples", RED)]
ORDEM = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


def b_q8(c, t, C, B):
    sid = which(t, C, ["18", "19", "20", "21", "22", "23"])
    heads = {"18": "A MÉDIA DA TURMA", "19": "EU FAÇO", "20": "NÓS FAZEMOS", "21": "VOCÊ FAZ", "22": "A CONTAGEM",
             "23": "AS ARMADILHAS"}
    head(c, t, B["start"] if sid == "18" else C[sid], "QUESTÃO 8 · ESTILO ENEM", heads[sid],
         GREEN if sid in ("21", "22") else PURPLE)
    card(c, *CARD_R)
    cues_in = {L: C[f"18.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABCE"}
    K.alternativas(c, t, C, ALTS8, 1300, 260, 420, 40, C["22.ok"], "D", cues_in, cues_x, gap=34)
    a0 = ep(t, C["18.a"], 0.4)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    # quais casas de M já apareceram
    tm = {(0, 0): C["19.c"], (0, 1): C["20.a"] + 2.0, (1, 0): C["20.b"] + 2.0, (1, 1): C["22.a"] + 2.2,
          (2, 0): C["22.b"], (2, 1): C["22.c"]}
    alf = {k: ep(t, v, 0.4) for k, v in tm.items()}
    # casa em foco (acesa em A, B e M)
    foco = None
    if sid == "19":
        foco = {(0, 0)}
    elif sid == "20":
        foco = {(0, 1)} if t < C["20.b"] else {(1, 0)}
    elif sid == "21":
        foco = {(1, 1), (2, 0), (2, 1)}
    elif sid == "22" and t < C["22.d"]:
        foco = {(1, 1)} if t < C["22.b"] else ({(2, 0)} if t < C["22.c"] else {(2, 1)})
    text(c, "A =", 250, 330, 40, "black", BLUE, a0, align="right")
    matriz(c, 360, 310, QA, a0, 90, 66, 38, hi=foco, br=BLUE)
    text(c, "B =", 590, 330, 40, "black", PURPLE, a0, align="right")
    matriz(c, 700, 310, QB, a0, 90, 66, 38, hi=foco, br=PURPLE)
    if sid == "18":
        ab = ep(t, C["18.b"], 0.5)
        if ab > 0:
            rrect(c, 190, 470, 1020, 100, 20, mix("#FFFFFF", PURPLE, 0.12), ab)
            linha(c, [("M = 0,4A + 0,6B", PURPLE), ("   ·   aprova: ", INK), ("≥ 6,0", AMBER)], 700, 520, 40, ab)
        acc = ep(t, C["18.c"], 0.5)
        if acc > 0:
            para(c, "Quantos dos seis elementos de M são maiores ou iguais a 6,0?", 190, 640, 38, "black", INK, acc,
                 1000, 48)
        return
    # a matriz M sendo preenchida
    am = ep(t, C["19"], 0.4)
    cores = {}
    if sid in ("22", "23") and t >= C["22.d"]:
        cores = {k: (GREEN if float(QM[k[0]][k[1]].replace(",", ".")) >= 6 else RED) for k in ORDEM}
    vals = [[QM[i][j] if alf[(i, j)] > 0 else ("?" if sid == "21" and (i, j) in foco else "") for j in range(2)]
            for i in range(3)]
    alf2 = {k: (alf[k] if alf[k] > 0 else 1.0) for k in ORDEM}
    text(c, "M =", 950, 330, 40, "black", GREEN, am, align="right")
    matriz(c, 1080, 310, vals, am, 110, 66, 38, cores=cores or {k: (AMBER if vals[k[0]][k[1]] == "?" else INK)
                                                               for k in ORDEM}, alfas=alf2, hi=foco, br=GREEN)
    # a conta da casa em foco
    contas = {(0, 0): ("0,4 · 5 + 0,6 · 7", "2 + 4,2 = 6,2"), (0, 1): ("0,4 · 8 + 0,6 · 5", "3,2 + 3 = 6,2"),
              (1, 0): ("0,4 · 7 + 0,6 · 5", "2,8 + 3 = 5,8"), (1, 1): ("0,4 · 4 + 0,6 · 8", "1,6 + 4,8 = 6,4"),
              (2, 0): ("0,4 · 6 + 0,6 · 6", "2,4 + 3,6 = 6,0"), (2, 1): ("0,4 · 6 + 0,6 · 5", "2,4 + 3 = 5,4")}
    if sid in ("19", "20", "22") and foco and len(foco) == 1 and not (sid == "22" and t >= C["22.d"]):
        k = next(iter(foco))
        t0 = {"19": C["19.b"], "20": C["20.a"] if k == (0, 1) else C["20.b"]}.get(sid, C[sid])
        if sid == "22":
            t0 = {(1, 1): C["22.a"], (2, 0): C["22.b"], (2, 1): C["22.c"]}[k]
        ak = ep(t, t0, 0.4)
        if ak > 0:
            rrect(c, 190, 520, 1020, 230, 22, "#FFFFFF", ak, shadow=True)
            text_mid(c, contas[k][0], 700, 590, 46, "black", INK, ak)
            text_mid(c, contas[k][1], 700, 652, 50, "black", GREEN, ep(t, t0 + 1.2, 0.4))
        if sid == "19":
            pill(c, "entre 5 e 7, perto do 7: confere", 700, 734, GREEN, size=24, a=ep(t, C["19.c"] + 1.0, 0.4),
                 anchor="center", bounds=(160, 1270))
    if sid == "21":
        pause_timer(c, t, C["21.end"] - 1.9, 700, 640)
        return
    if sid in ("22", "23") and t >= C["22.d"]:
        ad = ep(t, C["22.d"], 0.5)
        rrect(c, 190, 520, 1020, 230, 22, "#FFFFFF", ad, shadow=True)
        linha(c, [("≥ 6,0: ", INK), ("6,2 · 6,2 · 6,4 · 6,0", GREEN)], 700, 580, 40, ad)
        linha(c, [("< 6,0: ", INK), ("5,8 · 5,4", RED)], 700, 650, 40, ad)
        if sid == "22":
            selo(c, 1080, 468, ep(t, C["22.d"] + 1.6, 0.4), "6,0 CONTA!", AMBER, -5, 30)
        ae = ep(t, C["22.e"], 0.5)
        if ae > 0:
            text_mid(c, "4 médias", 700, 715, 40, "black", GREEN, ae)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "MULTIPLICAÇÃO DE MATRIZES", PURPLE)
    aa = ep(t, C["25.a"], 0.5)
    if aa > 0:
        cartao(c, 260, 220, 640, 380, aa)
        text(c, "A FILIAL COMPRA", 580, 280, 26, "black", BLUE, aa, tracking=2)
        for k, s_ in enumerate(("10 kg de arroz", "5 kg de feijão", "4 L de óleo")):
            text(c, s_, 580, 370 + k * 70, 40, "black", INK, aa)
        ak = ep(t, C["25.a"] + 4.0, 0.4)
        cartao(c, 1020, 220, 640, 380, ak)
        text(c, "O FORNECEDOR COBRA", 1340, 280, 26, "black", PURPLE, ak, tracking=2)
        for k, s_ in enumerate(("R$ 5 o kg", "R$ 9 o kg", "R$ 8 o litro")):
            text(c, s_, 1340, 370 + k * 70, 40, "black", INK, ak)
    ab = ep(t, C["25.b"], 0.5)
    if ab > 0:
        pill(c, "várias filiais × vários fornecedores, DE UMA VEZ?", W / 2, 680, BLUE, size=32, a=ab, anchor="center")
    acc = ep(t, C["25.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 780, acc, "NÃO É CASA COM CASA", RED, -3, 44)


def b_cta(c, t, C, B):
    cta(c, t, C["26.like"], C["26.sub"], C["26.bell"], C["26.com"], C["26.bye"],
        "Você contaria o 6,0 como aprovado?", canal="no Estudativo", anki=C["26.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, planilhas=b_planilhas, definicoes=b_definicoes,
              igualdade=b_igualdade, soma=b_soma, numero=b_numero, atalho_ordem=b_atalho_ordem, media=b_media,
              atalho_media=b_atalho_media, propriedades=b_propriedades, exercicio=b_exercicio, recap=b_recap,
              erros=b_erros, q8=b_q8, ponte=b_ponte, cta=b_cta)
