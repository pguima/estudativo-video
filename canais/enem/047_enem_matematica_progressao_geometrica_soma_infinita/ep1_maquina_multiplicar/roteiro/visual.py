"""Visual — Progressão Geométrica, Episódio 1: a máquina de multiplicar (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: folha dobrada, contador, alternativas, erro_cards,
atalho, selo, regra...).
Peças deste episódio: maquina() (caixa roxa "×q": a ficha entra, sai multiplicada, com contador de quantas vezes a
máquina agiu), corrida() (a PA andando em passos iguais numa reta × a PG subindo por uma curva, com placar), fichas()
(fila de termos com setas ×q ou −r entre eles), linha() (texto com cor por trecho, mantém o espaço de milhar).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum047", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_pg_ep1_maquina_multiplicar.mp4"
CARD_R = K.CARD_R
TEAL = "#0E9384"
NB = " "   # espaço rígido de milhar


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


def ficha(c, s, cx, cy, a, col=INK, w=110, h=76, size=36, fill="#FFFFFF"):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, fill, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14), paint(col, a, stroke=3))
    fmid(c, s, cx, cy, size, "black", col, a)


def fichas(c, t, t0, vals, x0, y, passo, a, col=BLUE, op=None, op_col=PURPLE, dt=0.5, w=120, size=36):
    """fila de termos que entram um a um a partir de t0; op = texto entre eles ("×2", "−40"...)"""
    if a <= 0:
        return []
    xs = [x0 + k * passo for k in range(len(vals))]
    for k, (v, x) in enumerate(zip(vals, xs)):
        ak = a * ep(t, t0 + k * dt, 0.35)
        ficha(c, v, x, y, ak, col, w=w, size=size)
        if op and k > 0 and ak > 0:
            xm = (xs[k - 1] + x) / 2
            arrow(c, xs[k - 1] + w / 2 - 6, y - 60, x - w / 2 + 6, y - 60, op_col, ak, 4, 12)
            pill(c, op, xm, y - 96, op_col, size=22, a=ak, anchor="center", bounds=(0, 1920))
    return xs


def pessoa(c, cx, cy, r, a, col):
    """bonequinho: cabeça + ombros"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - r * 0.55, r * 0.55, paint(col, a))
    rrect(c, cx - r, cy + r * 0.1, 2 * r, r * 1.1, r * 0.55, col, a)


def maquina(c, cx, cy, rotulo, a, ent=None, sai=None, u=0.0, vezes=None, col=PURPLE, w=300, h=200):
    """a máquina ×q: caixa roxa com o rótulo; a ficha 'ent' entra pela esquerda e 'sai' sai pela direita (u = 0..1)"""
    if a <= 0:
        return
    # esteira
    line(c, cx - w / 2 - 260, cy + h / 2 - 10, cx + w / 2 + 260, cy + h / 2 - 10, INK2, a, 5)
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, col, a, shadow=True)
    rrect(c, cx - w / 2 + 16, cy - h / 2 + 16, w - 32, 44, 12, "#FFFFFF", a * 0.18)
    text(c, "MÁQUINA", cx, cy - h / 2 + 48, 22, "black", "#FFFFFF", a, tracking=3)
    fmid(c, rotulo, cx, cy + 22, max(80, h * 0.42), "black", "#FFFFFF", a)
    if ent is not None and u < 0.5:
        x = cx - w / 2 - 170 + (170 - 10) * (u / 0.5)
        ficha(c, ent, x, cy + h / 2 - 58, a * (1 - ep(u, 0.42, 0.08)), BLUE, w=130)
    if sai is not None and u >= 0.5:
        x = cx + w / 2 + 10 + 160 * ((u - 0.5) / 0.5)
        ficha(c, sai, x, cy + h / 2 - 58, a * ep(u, 0.5, 0.08), GREEN, w=130)
    if vezes is not None:
        pill(c, f"a máquina agiu: {vezes} {'vez' if vezes == 1 else 'vezes'}", cx, cy + h / 2 + 50, INK, size=26, a=a,
             anchor="center", bounds=(0, 1920))


PA6 = [2, 8, 14, 20, 26, 32]
PG6 = [2, 4, 8, 16, 32, 64]


def corrida(c, x0, y0, w, h, nvis, a, placar=True, ymax=70):
    """eixos + PA (pontos azuis numa reta) e PG (pontos roxos numa curva) até o termo nvis (fracionário)"""
    if a <= 0:
        return
    line(c, x0, y0 + h, x0 + w, y0 + h, INK2, a, 3)
    line(c, x0, y0 + h, x0, y0, INK2, a, 3)
    X = lambda n: x0 + 60 + (n - 1) * (w - 120) / 5
    Y = lambda v: y0 + h - v / ymax * h
    for n in range(1, 7):
        text(c, f"{n}º", X(n), y0 + h + 40, 24, "bold", GRAY, a)
    # reta da PA e curva da PG
    nmax = max(1.0, min(6.0, nvis))
    p = skia.Path(); q = skia.Path()
    steps = 60
    for k in range(steps + 1):
        n = 1 + (nmax - 1) * k / steps
        ya = Y(2 + 6 * (n - 1)); yg = Y(2 * 2 ** (n - 1))
        (p.moveTo if k == 0 else p.lineTo)(X(n), ya)
        (q.moveTo if k == 0 else q.lineTo)(X(n), yg)
    c.drawPath(p, paint(BLUE, a * 0.6, stroke=4))
    c.drawPath(q, paint(PURPLE, a * 0.6, stroke=4))
    for n in range(1, 7):
        f = clamp(nvis - n + 1)
        if f <= 0:
            break
        c.drawCircle(X(n), Y(PA6[n - 1]), 14, paint(BLUE, a * f))
        c.drawCircle(X(n), Y(PG6[n - 1]), 14, paint(PURPLE, a * f))
    pill(c, "PA · +6", x0 + 20, y0 + 10, BLUE, size=24, a=a, bounds=(0, 1920))
    pill(c, "PG · ×2", x0 + 20, y0 + 60, PURPLE, size=24, a=a, bounds=(0, 1920))
    if placar:
        n = int(min(6, max(1, nvis)))
        rrect(c, x0 + w + 40, y0 + 40, 300, 230, 22, "#10141A", a)
        text(c, f"{n}º TERMO", x0 + w + 190, y0 + 90, 24, "black", "#9AA3B2", a)
        ftext(c, str(PA6[n - 1]), x0 + w + 110, y0 + 190, 64, "black", "#7FB2FF", a)
        ftext(c, "×", x0 + w + 190, y0 + 186, 40, "black", "#9AA3B2", a)
        ftext(c, str(PG6[n - 1]), x0 + w + 270, y0 + 190, 64, "black", "#C9A7FF", a)
        text(c, "PA        PG", x0 + w + 190, y0 + 245, 22, "bold", "#9AA3B2", a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PROGRESSÃO GEOMÉTRICA · EPISÓDIO 1", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        text(c, "DUAS SEQUÊNCIAS · O MESMO COMEÇO", W / 2, 230, 30, "black", INK2, aa, tracking=2)
    ab = ep(t, C["01.b"], 0.5)
    fichas(c, t, C["01.b"] + 0.6, ["2", "8", "14", "20", "26"], 560, 380, 200, ab, BLUE, "+6", BLUE, 0.6)
    acc = ep(t, C["01.c"], 0.5)
    fichas(c, t, C["01.c"] + 0.6, ["2", "4", "8", "16", "32"], 560, 600, 200, acc, PURPLE, "×2", PURPLE, 0.6)
    if ab > 0:
        pill(c, "SOMA 6", 300, 380, BLUE, size=26, a=ab, anchor="center", bounds=(0, 1920))
    if acc > 0:
        pill(c, "DOBRA", 300, 600, PURPLE, size=26, a=acc, anchor="center", bounds=(0, 1920))
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1290, 320, 140, 340), 20, 20), paint(GREEN, ad, stroke=5))
        pill(c, "5º termo: 32 > 26", 1360, 720, GREEN, size=28, a=ad, anchor="center", bounds=(0, 1920))
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, W / 2, 800, ae, "NUNCA MAIS É ALCANÇADA", PURPLE, -3, 36)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "PROGRESSÃO GEOMÉTRICA · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de PROGRESSÃO GEOMÉTRICA", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "RECONHECER", "uma PG", BLUE), ("02.b", "PORCENTAGEM", "vira razão", GREEN),
             ("02.c", "QUALQUER TERMO", "sem listar os anteriores", PURPLE)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "potência = multiplicação repetida", [("2⁶ = 2·2·2·2·2·2 = ", INK), ("64", GREEN)]),
             ("03.b", "série de Porcentagem", [("+5%  →  × ", INK), ("1,05", GREEN)]),
             ("03.c", "série de PA", [("do 1º ao termo n:  ", INK), ("n − 1", GREEN), (" passos", INK)])]
    for k, (cue, rot, partes) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 190 + d
        rrect(c, 260, y - 75, 1400, 150, 24, "#FFFFFF", a, shadow=True)
        pill(c, rot, 300, y - 75, BLUE, size=22, a=a, bounds=(0, 1920))
        linha(c, partes, W / 2, y + 8, 54, a)


# ======================================================================
# bloco a — o que é PG
# ======================================================================

def b_folha(c, t, C, B):
    head(c, t, B["start"], "DOBRE UMA FOLHA AO MEIO", "O QUE É UMA PG?", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, B["start"], 0.5) * (1 - ep(t, C["04.c"], 0.4))
    if a0 > 0:
        tt = (t - C["04.a"]) / 1.0           # uma dobra por segundo, a partir da fala "duas camadas"
        if tt < 0:
            K.folha(c, 640, 490, 760, 540, 0, a0)
            K.contador(c, 1360, 470, 1, a0 * 0.5, "camada", INK2)
        else:
            dob = int(min(tt, 4))
            prog = tt - dob if tt < 4 else 0
            K.folha(c, 640, 490, 760, 540, dob, a0, prog)
            K.contador(c, 1360, 470, 2 ** (dob + (1 if prog > 0.5 else 0)), a0, "camadas", PURPLE)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0 and t < C["04.c"]:
        regra(c, "cada número = o anterior × 2", W / 2, 790, ab, 36)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        vals = ["10" + NB + "000", "10" + NB + "500", "11" + NB + "025", "11" + NB + "576"]
        text(c, "população de uma cidade que cresce 5% ao ano", W / 2, 260, 32, "black", INK2, acc)
        fichas(c, t, C["04.c"] + 0.5, vals, 470, 430, 330, acc, BLUE, "×1,05", PURPLE, 0.5, w=210, size=34)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 600, 1320, 170, 24, mix("#FFFFFF", BLUE, 0.10), ad)
        text(c, "PROGRESSÃO GEOMÉTRICA (PG)", W / 2, 655, 34, "black", BLUE, ad)
        text(c, "cada termo = o anterior × o MESMO número", W / 2, 725, 36, "bold", INK, ad)


TIPOS = [("05.b", "(3, 6, 12, 24, …)", "q = 2", "CRESCENTE", GREEN),
         ("05.c", "(80, 40, 20, 10, …)", "q = 1/2", "DECRESCENTE", BLUE),
         ("05.d", "(2, −6, 18, −54, …)", "q = −3", "ALTERNANTE", AMBER),
         ("05.e", "(5, 5, 5, …)", "q = 1", "CONSTANTE", INK2)]


def b_tipos(c, t, C, B):
    head(c, t, B["start"], "A RAZÃO q", "A MÁQUINA DE MULTIPLICAR", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0 and t < C["05.b"] + 0.4:
        u = clamp((t - C["05.a"] - 1.6) / 2.2)
        maquina(c, W / 2, 460, "×q", aa * (1 - ep(t, C["05.b"], 0.4)), "termo", "seguinte", u)
        rrect(c, 300, 690, 1320, 100, 20, mix("#FFFFFF", BLUE, 0.10), aa * (1 - ep(t, C["05.b"], 0.4)))
        text(c, "RAZÃO q: o número fixo que multiplica cada termo", W / 2, 752, 32, "black", BLUE,
             aa * (1 - ep(t, C["05.b"], 0.4)))
    for k, (cue, seq, q, nome, col) in enumerate(TIPOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 145 + d
        rrect(c, 240, y - 55, 1440, 110, 20, "#FFFFFF", a, shadow=True)
        ftext(c, seq, 290, y + 14, 40, "black", INK, a, align="left")
        chip(c, q, 1150, y, PURPLE, a, 36)
        pill(c, nome, 1620, y, col, size=26, a=a, anchor="right", bounds=(0, 1920))
    a5 = ep(t, C["05.e"] + 2.0, 0.5)
    if a5 > 0:
        pill(c, "e (1 000; 1 050; 1 102,5; …) tem q = 1,05: cresce 5% por período", W / 2, 830, GREEN, size=24, a=a5,
             anchor="center", bounds=(0, 1920))


# ======================================================================
# bloco b — quociente, não diferença
# ======================================================================

def b_quociente(c, t, C, B):
    head(c, t, B["start"], "COMO ACHAR A RAZÃO?", "QUOCIENTE, NÃO DIFERENÇA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 200, 1320, 110, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        linha(c, [("q = ", PURPLE), ("termo ÷ anterior", INK), ("   ·   QUOCIENTE = resultado da divisão", BLUE)], W / 2, 255,
              34, aa)
    ab = ep(t, C["06.b"], 0.5)
    fichas(c, t, C["06.b"], ["80", "40", "20"], 640, 500, 320, ab, BLUE, "÷ 2 → q = 0,5", PURPLE, 0.4, w=140, size=44)
    if ab > 0:
        linha(c, [("40 ÷ 80 = ", INK), ("0,5", GREEN)], W / 2, 640, 56, ep(t, C["06.b"] + 1.6, 0.4))
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        check_icon(c, 600, 730, 24, acc, RED, "x")
        linha(c, [("40 − 80 = −40 ", RED), ("→ diferença: coisa de PA", INK2)], 640, 732, 34, acc, align="left")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        regra(c, "na PG, o que se repete é a DIVISÃO", W / 2, 810, ad, 32)


# ======================================================================
# bloco c — porcentagem vira razão
# ======================================================================

def b_fator(c, t, C, B):
    head(c, t, B["start"], "E A PORCENTAGEM?", "ELA VIRA RAZÃO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        rrect(c, 300, 200, 1320, 100, 20, mix("#FFFFFF", BLUE, 0.10), aa)
        text(c, "FATOR: o número que multiplica", W / 2, 262, 36, "black", BLUE, aa)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        K.atalho(c, 260, 340, 680, 300, "ATALHO · CRESCER", [("m", "q = 1 + i"), "+5%  →  × 1,05"], ab, 44)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        K.atalho(c, 980, 340, 680, 300, "ATALHO · CAIR", [("m", "q = 1 − i"), "−15%  →  × 0,85"], acc, 44)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        regra(c, "multiplique pelo que FICA, não pela porcentagem", W / 2, 750, ad, 34)


# ======================================================================
# bloco d — termo geral · instante zero
# ======================================================================

def b_termo(c, t, C, B):
    head(c, t, B["start"], "O 20º SEM LISTAR TODOS?", "O TERMO GERAL", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0 and t < C["08.c"]:
        xs = fichas(c, t, C["08.a"], ["a₁", "a₂", "a₃", "…", "aₙ"], 420, 400, 270, aa, BLUE, "×q", PURPLE, 0.6, w=130)
        cont = 1 + int(clamp((t - C["08.a"] - 1.2) / 2.6) * 2.999)
        pill(c, ["a₂: 1 vez", "a₃: 2 vezes", "aₙ: n − 1 vezes"][min(cont, 3) - 1], W / 2, 520, INK, size=30, a=aa,
             anchor="center", bounds=(0, 1920))
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        y = 650 if t < C["08.c"] else 280
        K.boxed(c, 460, y - 90, 1000, 180, PURPLE, ab, 0.08)
        pill(c, "TERMO GERAL", 500, y - 90, PURPLE, size=22, a=ab, bounds=(0, 1920))
        K.expr(c, "aₙ = a₁ · q^{n−1}", W / 2, y + 10, 78, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 430, 1320, 170, 24, "#FFFFFF", acc, shadow=True)
        text(c, "(3, 6, 12, …) · o 5º termo", W / 2, 480, 30, "black", BLUE, acc)
        linha(c, [("a₅ = 3 · 2⁴ = 3 · 16 = ", INK), ("48", GREEN)], W / 2, 555, 52, ep(t, C["08.c"] + 1.6, 0.4))
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        rrect(c, 460, 640, 1000, 140, 22, mix("#FFFFFF", PURPLE, 0.08), ad)
        K.expr(c, "aₙ = aₖ · q^{n−k}", W / 2, 712, 60, ad)
        pill(c, "partindo do termo de posição k", W / 2, 640, PURPLE, size=22, a=ad, anchor="center", bounds=(0, 1920))


def b_zero(c, t, C, B):
    head(c, t, B["start"], "E QUANDO FALA EM TEMPO?", "CONTE DO INSTANTE ZERO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    if aa > 0:
        K.boxed(c, 300, 200, 1320, 150, PURPLE, aa, 0.08)
        linha(c, [("TERMO ZERO a₀", BLUE), (" = o valor inicial   →   ", INK2)], 760, 275, 34, aa)
        K.expr(c, "a₀ · q^t", 1420, 275, 60, aa)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rrect(c, 300, 390, 1320, 230, 24, "#FFFFFF", ab, shadow=True)
        pill(c, "você já viu isso · série de Função Exponencial", 340, 390, INK2, size=22, a=ab, bounds=(0, 1920))
        text(c, "500 bactérias · dobram a cada 20 min · 2 h", W / 2, 460, 32, "black", INK, ab)
        linha(c, [("120 ÷ 20 = ", INK), ("6 vezes", PURPLE), ("   ·   500 · 2⁶ = 500 · 64 = ", INK),
                  ("32" + NB + "000", GREEN)], W / 2, 545, 40, ep(t, C["09.b"] + 2.0, 0.4))
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        pill(c, "aₙ com n − 1  ou  a₀ com t: a mesma conta, só muda quem é o primeiro", W / 2, 660, INK, size=26, a=acc,
             anchor="center", bounds=(0, 1920))
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        K.atalho(c, 360, 700, 1200, 120, "ATALHO · ANTES DA POTÊNCIA", ["escreva:  fator = …   ·   quantas vezes age = …"],
                 ad, 34)


# ======================================================================
# bloco e — razão por dois termos
# ======================================================================

def b_doistermos(c, t, C, B):
    head(c, t, B["start"], "DOIS TERMOS SOLTOS?", "A RAZÃO A PARTIR DE DOIS TERMOS", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        xs = [460, 760, 1060, 1360]
        for k, (lab, v) in enumerate((("a₂", "3"), ("a₃", "?"), ("a₄", "?"), ("a₅", "24"))):
            ficha(c, v, xs[k], 330, aa, BLUE if v != "?" else GRAY, w=150, size=48)
            ftext(c, lab, xs[k], 410, 28, "bold", GRAY, aa)
        ab = ep(t, C["10.b"], 0.5)
        for k in range(3):
            ak = ab * ep(t, C["10.b"] + 1.0 + k * 0.5, 0.3)
            if ak > 0:
                arrow(c, xs[k] + 80, 260, xs[k + 1] - 80, 260, PURPLE, ak, 4, 12)
                pill(c, "×q", (xs[k] + xs[k + 1]) / 2, 225, PURPLE, size=22, a=ak, anchor="center", bounds=(0, 1920))
        if ab > 0:
            K.atalho(c, 300, 460, 620, 150, "ATALHO · CONTE PELOS ÍNDICES", ["5 − 2 = 3 vezes"], ab, 38)
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 460, 640, 150, 24, "#FFFFFF", acc, shadow=True)
        K.expr(c, "q^3 = 24 ÷ 3 = 8", 1300, 515, 46, acc)
        linha(c, [("q = ", INK), ("2", GREEN)], 1300, 580, 46, ep(t, C["10.c"] + 2.8, 0.4))
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        rrect(c, 300, 660, 640, 140, 22, mix("#FFFFFF", BLUE, 0.10), ad)
        text(c, "PA: a distância SE DIVIDE", 620, 742, 34, "black", BLUE, ad)
        rrect(c, 980, 660, 640, 140, 22, mix("#FFFFFF", PURPLE, 0.10), ad)
        text(c, "PG: SE TIRA A RAIZ", 1300, 742, 34, "black", PURPLE, ad)


# ======================================================================
# bloco f — PG é exponencial · teste da tabela
# ======================================================================

def b_corrida(c, t, C, B):
    head(c, t, B["start"], "QUEM DOBRA NUNCA É ALCANÇADA?", "A CORRIDA: PA × PG", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if t < C["11.b"]:
        nv = 1 + 5 * clamp((t - C["11.a"]) / 3.0) * 0.6
    elif t < C["11.c"]:
        nv = 4
    elif t < C["11.c"] + 3.4:
        nv = 5
    else:
        nv = 6
    corrida(c, 260, 200, 1000, 480, nv, aa)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        regra(c, "PG = função exponencial nos naturais 1, 2, 3, …", W / 2, 810, ad, 32)


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "PA OU PG?", "O TESTE DA TABELA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    K.atalho(c, 360, 190, 1200, 120, "ATALHO · TESTE DA TABELA", ["divida cada valor pelo anterior"], aa, 36)
    ab = ep(t, C["12.b"], 0.5)
    fichas(c, t, C["12.b"] + 0.4, ["200", "300", "450", "675"], 360, 450, 260, ab, PURPLE, "÷ → 1,5", PURPLE, 0.4, w=150)
    if ab > 0:
        pill(c, "PG", 1500, 450, PURPLE, size=40, a=ep(t, C["12.b"] + 3.2, 0.4), anchor="center", bounds=(0, 1920))
    acc = ep(t, C["12.c"], 0.5)
    fichas(c, t, C["12.c"] + 0.4, ["200", "300", "400", "500"], 360, 650, 260, acc, BLUE, "− → 100", BLUE, 0.4, w=150)
    if acc > 0:
        pill(c, "PA", 1500, 650, BLUE, size=40, a=ep(t, C["12.c"] + 2.6, 0.4), anchor="center", bounds=(0, 1920))
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        pill(c, "quociente constante → EXPONENCIAL   ·   diferença constante → AFIM", W / 2, 800, INK, size=26, a=ad,
             anchor="center", bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("13", "SUA VEZ", "PAUSE E TENTE", GREEN), ("14", "VAMOS JUNTOS", "FATOR E QUANTAS VEZES", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 200, 1400, 150, 24, "#FFFFFF", aa, shadow=True)
        linha(c, [("app: 2" + NB + "000 usuários", BLUE), ("   ·   +10% ao mês   ·   ", INK2), ("q = ?", AMBER),
                  ("   ·   em 3 meses = ?", AMBER)], W / 2, 275, 42, aa)
    if t < C["14"]:
        pause_timer(c, t, C["13.end"] - 1.9, 960, 560)
        return
    ab = ep(t, C["14.a"], 0.5)
    if ab > 0:
        rrect(c, 260, 400, 680, 200, 24, "#FFFFFF", ab, shadow=True)
        text(c, "FATOR", 600, 450, 26, "black", AMBER, ab)
        linha(c, [("1 + 0,1 = ", INK), ("1,1", PURPLE)], 600, 535, 52, ab)
    acc = ep(t, C["14.b"], 0.5)
    if acc > 0:
        rrect(c, 980, 400, 680, 200, 24, "#FFFFFF", acc, shadow=True)
        text(c, "QUANTAS VEZES AGE", 1320, 450, 26, "black", AMBER, acc)
        linha(c, [("3 vezes", PURPLE), (" (1 por mês)", INK2)], 1320, 535, 48, acc)
    ad = ep(t, C["14.c"], 0.5)
    if ad > 0:
        rrect(c, 360, 640, 1200, 150, 24, mix("#FFFFFF", GREEN, 0.12), ad)
        linha(c, [("2" + NB + "000 · 1,1³ = 2" + NB + "000 · 1,331 = ", INK), ("2" + NB + "662", GREEN)], W / 2, 715, 50, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Na PG, o que se repete é a divisão de um termo pelo anterior.",
          "Crescer i% é multiplicar por 1 + i.",
          "O expoente é o número de vezes que o fator age."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["15", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "15" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("aₙ = a₁ · qⁿ: o 5º termo de (3, 6, 12, …) = 3 · 2⁵ = 96", "é o 5º termo, então parece expoente 5",
          "o 1º termo já está lá: a máquina age 4 vezes. 3 · 2⁴ = 48"),
         ("razão de (80, 40, 20, …) = −40", "na PA era assim: um menos o outro",
          "na PG você DIVIDE: 40 ÷ 80 = 0,5"),
         ("“dobra 6 vezes” = 500 · 2 · 6 = 6 000", "tem um 2 e tem um 6 no enunciado",
          "6 vezes é o EXPOENTE: 500 · 2⁶ = 32 000"),
         ("5% ao ano com q = 0,05: 1 000 pessoas viram 50", "0,05 é mesmo 5%",
          "0,05 é só o aumento: o fator é 1,05")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["16", "17", "18", "19"], ERROS)


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


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _questao(c, t, C, sid_q, sid_r, sid_x, alts, okL, xs, txt, fonte="Questão do material de estudo (seção 12)", size=27,
             asz=36, gap=30, pausa_y=None):
    a0 = ep(t, C[f"{sid_q}.a"], 0.4)
    yend = _enunciado(c, [(txt, INK)], a0, 236, size)
    text(c, fonte, 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[sid_r], 0.3)), align="left")
    cues_in = {L: C[f"{sid_q}.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"{sid_x}.x{L.lower()}"] for L in xs}
    K.alternativas(c, t, C, alts, 1000, 260, 680, asz, C[f"{sid_r}.ok"], okL, cues_in, cues_x, gap=gap)
    if t < C[sid_r]:
        pause_timer(c, t, C[f"{sid_q}.end"] - 1.9, 540, pausa_y or min(yend + 120, 740))
        return None
    y0 = 236 - 30
    _painel(c, y0, ep(t, C[sid_r], 0.4))
    return y0


ALTS7 = [("A", "8" + NB + "000", "só o aumento linear", RED), ("B", "42" + NB + "000", "1 ano só", RED),
         ("C", "48" + NB + "000", "linear: + 2 000/ano", RED), ("D", "48" + NB + "620", "", GREEN),
         ("E", "168" + NB + "000", "× 1,05 × 4", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 7 · EU FAÇO", "CRESCIMENTO PERCENTUAL", BLUE)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "20", "21", "22", ALTS7, "D", "ABCE",
                  "A população de um município é de 40 000 habitantes e, segundo uma projeção, deve crescer 5% ao ano. "
                  "Use 1,05⁴ ≈ 1,2155. Daqui a 4 anos, a população projetada será de aproximadamente")
    if y0 is None:
        return
    aa = ep(t, C["21.a"], 0.4)
    if aa > 0:
        linha(c, [("fator = ", INK), ("1,05", PURPLE)], 540, y0 + 60, 38, aa)
        linha(c, [("quantas vezes age = ", INK), ("4", PURPLE)], 540, y0 + 130, 38, aa)
    ab = ep(t, C["21.b"], 0.4)
    if ab > 0:
        linha(c, [("1,05⁴ ≈ 1,2155 ", INK), ("(dado)", GRAY)], 540, y0 + 230, 38, ab)
    acc = ep(t, C["21.c"], 0.4)
    if acc > 0:
        linha(c, [("40" + NB + "000 · 1,2155", INK)], 540, y0 + 320, 40, acc)
        linha(c, [("= ", INK), ("48" + NB + "620", GREEN)], 540, y0 + 400, 52, ep(t, C["21.c"] + 1.8, 0.4))
    ad = ep(t, C["21.d"], 0.4)
    if ad > 0:
        check_icon(c, 250, y0 + 500, 20, ad, GREEN)
        linha(c, [("pouco mais de 20% em 4 anos · bate", GREEN)], 290, y0 + 502, 26, ad, align="left")


ALTS_ALG = [("A", "266 g", "tratou como PA", RED), ("B", "486 g", "1 vez: 6ª semana", RED),
            ("C", "972 g", "162 · 3 · 2", RED), ("D", "1" + NB + "458 g", "", GREEN), ("E", "4" + NB + "374 g", "3 vezes: 8ª semana", RED)]


def b_algas(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO NOVA · NÓS FAZEMOS", "AS ALGAS DO TANQUE", PURPLE)
    card(c, *CARD_R)
    y0 = _questao(c, t, C, "23", "24", "25", ALTS_ALG, "D", "ABCE",
                  "Em um tanque de cultivo, a massa de algas é medida ao fim de cada semana, e os valores formam uma "
                  "progressão geométrica. Ao fim da 2ª semana havia 6 g de algas e, ao fim da 5ª semana, 162 g. Mantido "
                  "esse padrão, ao fim da 7ª semana a massa de algas será de", fonte="Questão inédita", size=25, asz=34)
    if y0 is None:
        return
    aa = ep(t, C["24.a"], 0.4)
    if aa > 0:
        linha(c, [("2ª → 5ª: o fator age ", INK), ("3 vezes", PURPLE)], 540, y0 + 60, 32, aa)
        K.expr(c, "q^3 = 162 ÷ 6 = 27", 540, y0 + 150, 42, ep(t, C["24.a"] + 1.6, 0.4))
        linha(c, [("q = ", INK), ("3", GREEN)], 540, y0 + 230, 42, ep(t, C["24.a"] + 3.6, 0.4))
    ab = ep(t, C["24.b"], 0.4)
    if ab > 0:
        linha(c, [("5ª → 7ª: mais ", INK), ("2 vezes", PURPLE)], 540, y0 + 320, 32, ab)
        K.expr(c, "162 · 3^2 = 162 · 9", 540, y0 + 400, 40, ab)
    acc = ep(t, C["24.c"], 0.4)
    if acc > 0:
        linha(c, [("= ", INK), ("1" + NB + "458 g", GREEN)], 540, y0 + 490, 54, acc)


ALTS9 = [("A", "=P(n)=1 000+200n", "linear: ano 2 → 1 400", RED), ("B", "=P(n)=1 000·1,2n", "ano 0 → 0", RED),
         ("C", "=P(n)=1 000·0,2^n", "taxa no lugar do fator", RED), ("D", "=P(n)=1 200^n", "sem valor inicial", RED),
         ("E", "=P(n)=1 000·1,2^n", "", GREEN)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "O MODELO DA TABELA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    if a0 > 0 and t < C["27"]:
        tab = [("ano n", "0", "1", "2", "3"), ("clientes", "1 000", "1 200", "1 440", "1 728")]
        for r, row in enumerate(tab):
            for j, v in enumerate(row):
                x = 230 + (0 if j == 0 else 150 + (j - 1) * 150)
                ftext(c, v, x, 500 + r * 60, 28, "black" if r == 0 or j == 0 else "bold", BLUE if r == 0 else INK, a0,
                      align="left")
    y0 = _questao(c, t, C, "26", "27", "28", ALTS9, "E", "ABCD",
                  "Uma loja virtual registrou o número de clientes cadastrados no início de cada ano, a partir do ano "
                  "de lançamento (ano 0). Mantido o padrão, a expressão que fornece o número de clientes P(n) no ano n é",
                  size=25, asz=30, gap=26, pausa_y=700)
    if y0 is None:
        return
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        linha(c, [("1 200 ÷ 1 000 = 1 440 ÷ 1 200 = ", INK), ("1,2", PURPLE)], 540, y0 + 60, 28, aa)
        pill(c, "quociente constante → PG", 540, y0 + 115, PURPLE, size=22, a=aa, anchor="center", bounds=(0, 1920))
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        linha(c, [("ano 0 → ", INK), ("1 000", BLUE), ("   ·   age ", INK), ("n vezes", PURPLE)], 540, y0 + 200, 32, ab)
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        K.expr(c, "P(n) = 1 000 · 1,2^n", 540, y0 + 290, 44, acc)
        linha(c, [("ano 2: 1 000 · 1,44 = ", INK), ("1 440", GREEN), (" ✓", GREEN)], 540, y0 + 380, 32,
              ep(t, C["27.c"] + 2.4, 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "PROPRIEDADES E SOMA", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    if aa > 0:
        # árvore da mensagem: 1 → 3 → 9
        pessoa(c, W / 2, 260, 30, aa, PURPLE)
        for k in range(3):
            x = W / 2 - 300 + k * 300
            ak = aa * ep(t, C["30.a"] + 0.8, 0.4)
            line(c, W / 2, 300, x, 380, INK2, ak, 3)
            pessoa(c, x, 410, 26, ak, BLUE)
            for j in range(3):
                xx = x - 80 + j * 80
                aj = aa * ep(t, C["30.a"] + 2.2, 0.4)
                line(c, x, 450, xx, 510, INK2, aj, 2)
                pessoa(c, xx, 535, 18, aj, TEAL)
        pill(c, "dia 1: 3 pessoas · dia 2: 9 novas …", W / 2, 620, INK2, size=26, a=aa, anchor="center")
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        linha(c, [("em 6 dias, AO TODO = ", INK), ("?", AMBER)], W / 2, 700, 50, ab)
    acc = ep(t, C["30.c"], 0.5)
    if acc > 0:
        selo(c, 1450, 700, acc, "NÃO É 3⁶", RED, -6, 34)
    pill(c, "ep. 2 · propriedades e soma finita", W / 2, 800, PURPLE, size=30, a=ep(t, C["30.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"],
        "Quantas vezes você consegue dobrar uma folha de papel?", canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, folha=b_folha, tipos=b_tipos, quociente=b_quociente,
              fator=b_fator, termo=b_termo, zero=b_zero, doistermos=b_doistermos, corrida=b_corrida, tabela=b_tabela,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q7=b_q7, algas=b_algas, q9=b_q9, ponte=b_ponte,
              cta=b_cta)
