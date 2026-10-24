"""Visual — Função logarítmica e aplicações, Episódio 2: escalas logarítmicas e o pH (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, math_w, erro_cards, atalho, pause_timer...).
Peças deste episódio: fm() (fórmula com texto e potência), copo() (os três líquidos do concreto), regua_comum() e
regua_log() (o problema dos sons espremidos e a "régua de zeros"), pilha() (as bolinhas de H⁺, todas do mesmo tamanho:
1 · 10 · 100 · 1 000), regua_ph() (a régua de 0 a 14), tabela_ph() (a tabela da seção 06 com as duas parcelas),
alts() (alternativas com fórmulas).
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
_s = importlib.util.spec_from_file_location("comum043", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_logaritmica_ep2_escalas_ph.mp4"
CARD_R = K.CARD_R
LIMAO, CAFE, CHUVA = "#E8C547", "#7A4E2D", "#7FB6E0"


# ======================================================================
# tipografia: fórmula mista (texto + potência)
# ======================================================================

def _fm_w(p, size):
    kind = p[2] if len(p) > 2 else "t"
    if kind == "m":
        return K.math_w(p[0], size)
    return ftext_w(p[0], "black", size)


def fm_w(partes, size):
    return sum(_fm_w(p, size) for p in partes)


def fm(c, partes, cx, cy, size, a, align="center"):
    """partes = [(texto, cor[, tipo])]; tipo 't' texto (mantém espaços) ou 'm' expr (potência/fração: '10^{−3}',
    '(G₂/G₁)'). Centrada verticalmente em cy; devolve a largura"""
    tw = fm_w(partes, size)
    if a <= 0:
        return tw
    x = cx - tw / 2 if align == "center" else (cx - tw if align == "right" else cx)
    for p in partes:
        s_, col = p[0], p[1] or INK
        kind = p[2] if len(p) > 2 else "t"
        w_ = _fm_w(p, size)
        if kind == "m":
            K.expr(c, s_, x, cy, size, a, cores={i: col for i in range(12)}, align="left")
        else:
            ftext(c, s_, x, cy + size * 0.36, size, "black", col, a, align="left")
        x += w_
    return tw


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def defi(c, s, cx, cy, a, size=28, col=BLUE):
    """pílula de definição (azul)"""
    if a <= 0:
        return
    pill(c, s, cx, cy, col, size=size, a=a, anchor="center", bounds=(0, 1920))


# ======================================================================
# peças do episódio
# ======================================================================

def copo(c, cx, ybase, w, h, cor, a, nivel=0.72):
    """copo visto de frente: vidro claro com o líquido até `nivel` da altura"""
    if a <= 0:
        return
    x0 = cx - w / 2
    rrect(c, x0, ybase - h, w, h, 18, "#FFFFFF", a, shadow=True)
    hl = h * nivel
    rrect(c, x0 + 8, ybase - hl, w - 16, hl - 8, 12, cor, a * 0.85)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, ybase - h, w, h), 18, 18), paint(GRAY, a, stroke=4))
    line(c, x0 + 20, ybase - h + 24, x0 + 20, ybase - 30, "#FFFFFF", a * 0.7, 6)


def pilha(c, cx, ybase, n, a, col=RED, dot=6, gap=2):
    """n bolinhas de H⁺ (1, 10, 100 ou 1 000), todas do MESMO tamanho, empilhadas em grade a partir de ybase"""
    if a <= 0:
        return
    cols = {1: 1, 10: 5, 100: 10, 1000: 40}[n]
    rows = n // cols
    step = dot + gap
    w = cols * step - gap
    x0 = cx - w / 2
    for k in range(n):
        i, j = k % cols, k // cols
        c.drawCircle(x0 + i * step + dot / 2, ybase - j * step - dot / 2, dot / 2, paint(col, a))
    if n == 1:
        c.drawCircle(cx, ybase - dot / 2, dot * 2.2, paint(col, a, stroke=3))
    return w, rows * step


def regua_ph(c, x0, y, L, a, marcas=()):
    """régua de pH de 0 a 14 (passos iguais); marcas = [(pH, rótulo, cor)]"""
    if a <= 0:
        return
    u = L / 14
    rrect(c, x0 - 30, y - 34, L + 60, 68, 16, "#FFFFFF", a, shadow=True)
    for k in range(15):
        x = x0 + k * u
        line(c, x, y - 14, x, y + 14, INK, a, 3)
        text(c, str(k), x, y + 60, 26, "black", INK2, a)
    for v, rot, col in marcas:
        x = x0 + v * u
        c.drawCircle(x, y, 18, paint(col, a))
        pill(c, rot, x, y - 66, col, size=22, a=a, anchor="center", bounds=(0, 1920))


def regua_comum(c, x0, y, L, a, aperto=1.0):
    """régua comum de 0 a 1 W/m²: os sons do dia a dia (10⁻¹² a 10⁻²) caem todos colados no zero"""
    if a <= 0:
        return
    line(c, x0, y, x0 + L, y, INK, a, 5)
    for k in range(11):
        x = x0 + L * k / 10
        line(c, x, y - 12, x, y + 12, INK, a, 3)
    text(c, "0", x0, y + 56, 28, "black", INK2, a)
    text(c, "0,5", x0 + L / 2, y + 56, 28, "black", INK2, a)
    text(c, "1 W/m²", x0 + L, y + 56, 28, "black", INK2, a)
    if aperto > 0:
        for k in range(12):
            xx = x0 + 3 + (k % 3) * 4
            yy = y - 22 - (k // 3) * 16
            c.drawCircle(xx, yy, 7, paint(BLUE, a * aperto))
        c.drawCircle(x0 + L, y - 22, 9, paint(BLUE, a * aperto))


def regua_log(c, x0, y, L, a, arcos=0.0):
    """a "régua de zeros": 10⁻¹² ... 10⁰ = 1 em 13 passos iguais; arcos acende os "×10" entre os passos"""
    if a <= 0:
        return
    u = L / 12
    line(c, x0, y, x0 + L, y, INK, a, 5)
    sup = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    for k in range(13):
        x = x0 + k * u
        line(c, x, y - 14, x, y + 14, INK, a, 3)
        e = k - 12
        if k % 2 == 0:
            s_ = "1" if e == 0 else "10⁻" + "".join(sup[int(d)] for d in str(-e))
            text(c, s_, x, y + 60, 26, "black", INK2, a)
    if arcos > 0:
        for k in range(12):
            ak = a * clamp(arcos * 12 - k)
            if ak <= 0:
                continue
            xa, xb = x0 + k * u, x0 + (k + 1) * u
            p = skia.Path(); p.moveTo(xa, y - 20); p.quadTo((xa + xb) / 2, y - 70, xb, y - 20)
            c.drawPath(p, paint(GREEN, ak, stroke=4))
            text(c, "×10", (xa + xb) / 2, y - 64, 20, "black", GREEN, ak)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO LOGARÍTMICA · pH", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    for k, (s_, col, x) in enumerate((("pH 2", LIMAO, 560), ("pH 5", CAFE, 1360))):
        ak = ep(t, C["01.a"] + 1.0 * k, 0.4) * aa
        if ak > 0:
            rrect(c, x - 220, 230, 440, 200, 30, mix("#FFFFFF", col, 0.25), ak, shadow=True)
            text_mid(c, s_, x, 330, 110, "black", INK, ak)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        arrow(c, 800, 330, 1120, 330, GRAY, ab, 5, 16)
        pill(c, "diferença: 3", W / 2, 400, GRAY, size=30, a=ab, anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        text_mid(c, "3 vezes mais ácido?", 640, 580, 64, "black", AMBER, acc)
        strike(c, 330, 580, 950, 580, ep(t, C["01.c"] + 1.6, 0.4), RED, acc)
        selo(c, 640, 680, ep(t, C["01.c"] + 1.6, 0.4), "ERRA POR MUITO", RED, -4, 32)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        rrect(c, 1080, 490, 620, 300, 30, mix("#FFFFFF", GREEN, 0.10), ad, shadow=True)
        text(c, "concentração de H⁺", 1390, 550, 30, "black", GRAY, ad)
        text_mid(c, "1 000 ×", 1390, 650, 110, "black", GREEN, ad)
        text(c, "maior", 1390, 750, 34, "black", GREEN, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    aa, d = rise(t, C["02.a"])
    if aa > 0:
        text(c, "comparar duas leituras de uma escala logarítmica", W / 2, 320 + d, 44, "black", INK, aa)
        chip(c, "pH 2", 760, 420 + d, LIMAO, aa, 40)
        text_mid(c, "×", W / 2, 420 + d, 50, "black", GRAY, aa)
        chip(c, "pH 5", 1160, 420 + d, CAFE, aa, 40)
    ab, d = rise(t, C["02.b"])
    if ab > 0:
        text(c, "calcular o pH, mesmo com um número na frente", W / 2, 580 + d, 44, "black", INK, ab)
        for k, s_ in enumerate(("2 · 10⁻⁵", "5 · 10⁻⁴")):
            chip(c, s_, 760 + k * 400, 690 + d, PURPLE, ab, 40)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    itens = [("03.a", "série de Notação científica", ["quantas vezes maior = DIVISÃO", "2 ordens de grandeza = fator 100"]),
             ("03.b", "série de Logaritmos", ["log(M · N) = log M + log N"]),
             ("03.c", "série de Logaritmos", ["log 2 ≈ 0,30"])]
    for k, (cue, orig, linhas) in enumerate(itens):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 230 + k * 190 + d
        rrect(c, 260, y, 1400, 160, 22, "#FFFFFF", ak, shadow=True)
        text(c, orig, 300, y + 42, 24, "bold", GRAY, ak, align="left")
        for j, ln in enumerate(linhas):
            text(c, ln, 300 + j * 640, y + 112, 36, "black", PURPLE if k else BLUE, ak, align="left")


# ======================================================================
# concreto: três líquidos
# ======================================================================

def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS LÍQUIDOS", "QUEM É MAIS ÁCIDO?", BLUE)
    card(c, *CARD_R)
    itens = [("04.a", "limão", "pH ≈ 2", LIMAO, 520), ("04.b", "café", "pH ≈ 5", CAFE, 960),
             ("04.c", "água da chuva", "um pouco ácida", CHUVA, 1400)]
    for cue, nome, ph, cor, x in itens:
        ak = ep(t, C[cue], 0.5)
        copo(c, x, 620, 210, 290, cor, ak)
        if ak > 0:
            text(c, nome, x, 680, 36, "black", INK, ak)
            pill(c, ph, x, 740, PURPLE if "pH" in ph else GRAY, size=28, a=ak, anchor="center")
    ad = ep(t, C["04.d"], 0.5)
    defi(c, "ÁCIDO = no dia a dia, o que é azedo (como o limão)", W / 2, 240, ad, 28)
    ae = ep(t, C["04.e"], 0.5)
    if ae > 0:
        selo(c, W / 2, 815, ae, "QUANTAS VEZES MAIS ÁCIDO?", AMBER, -3, 32)


# ======================================================================
# bloco a — o problema da régua comum · a régua de zeros
# ======================================================================

def b_problema(c, t, C, B):
    head_seq(c, t, C, [("05", "POR QUE UMA ESCALA NOVA?", "O PROBLEMA DA RÉGUA COMUM", BLUE),
                       ("06", "A SOLUÇÃO", "A RÉGUA DE ZEROS", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            rrect(c, 300, 220, 1320, 130, 24, "#FFFFFF", aa, shadow=True)
            text(c, "o ouvido percebe sons de", W / 2, 262, 26, "bold", GRAY, aa)
            text_mid(c, "10⁻¹² W/m²   até   1 W/m²", W / 2, 312, 52, "black", INK, aa)
        ab = ep(t, C["05.b"], 0.5)
        if ab > 0:
            pill(c, "um fator de UM TRILHÃO: 1 000 000 000 000", W / 2, 410, PURPLE, size=30, a=ab, anchor="center",
                 bounds=(0, 1920))
        acc = ep(t, C["05.c"], 0.5)
        regua_comum(c, 320, 640, 1280, acc, ep(t, C["05.c"] + 1.2, 0.6))
        if acc > 0:
            pill(c, "quase todos os sons: ESPREMIDOS perto do zero", 330, 530, AMBER, size=26,
                 a=ep(t, C["05.c"] + 1.6, 0.4), anchor="left", bounds=(0, 1920))
            arrow(c, 360, 556, 330, 600, AMBER, ep(t, C["05.c"] + 1.6, 0.4), 4, 12)
        return
    aa = ep(t, C["06.a"], 0.5)
    defi(c, "ESCALA LOGARÍTMICA = cada fator 10 vira um PASSO IGUAL", W / 2, 240, aa, 28)
    ab = ep(t, C["06.b"], 0.5)
    regua_log(c, 330, 460, 1260, 1.0 if t >= C["06.a"] else 0, ab)
    if ab > 0:
        regra(c, "RÉGUA DE ZEROS: 1 passo = ×10 · 2 passos = ×100", W / 2, 600, ab, 34)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 680, 640, 120, 22, mix("#FFFFFF", BLUE, 0.10), acc)
        text(c, "LEITURA", 620, 722, 26, "black", BLUE, acc, tracking=2)
        text(c, "o número que você lê na régua", 620, 772, 28, "bold", INK, acc)
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        rrect(c, 980, 680, 640, 120, 22, mix("#FFFFFF", BLUE, 0.10), ad)
        text(c, "GRANDEZA", 1300, 722, 26, "black", BLUE, ad, tracking=2)
        text(c, "o que se mede de verdade (ex.: intensidade)", 1300, 772, 26, "bold", INK, ad)


# ======================================================================
# bloco b — a regra · bloco c — a tabela · atalho dos zeros
# ======================================================================

def b_regra(c, t, C, B):
    head(c, t, B["start"], "A REGRA QUE RESOLVE QUASE TUDO", "BASE 10", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    defi(c, "RAZÃO = resultado da divisão: QUANTAS VEZES uma grandeza é maior", W / 2, 240, aa, 26)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 360, 290, 1200, 230, 30, mix("#FFFFFF", PURPLE, 0.10), ab)
        fm(c, [("(G₂/G₁)", PURPLE, "m"), (" = ", PURPLE), ("10^{E₂−E₁}", PURPLE, "m")], W / 2, 405, 90, ab)
        text(c, "G = grandeza  ·  E = leitura", W / 2, 560, 26, "bold", GRAY, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        for k in range(4):
            ak = ep(t, C["07.c"] + 0.5 * k, 0.4) * acc
            x = 520 + k * 300
            chip(c, f"E₁ + {k}" if k else "E₁", x, 650, INK, ak, 32, fill=False)
            if k:
                arrow(c, x - 230, 650, x - 80, 650, GREEN, ak, 4, 12)
                text(c, "×10", x - 155, 630, 22, "black", GREEN, ak)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        regra(c, "a DIFERENÇA DE LEITURA vira o EXPOENTE DA RAZÃO", W / 2, 775, ad, 38)


TABELA = [("08.a", "1", "10", "10¹"), ("08.b", "2", "100", "10²"), ("08.c", "3", "1 000", "10³"),
          ("08.d", "0,3", "≈ 2", "log 2 ≈ 0,30"), ("08.e", "1,5", "≈ 32", "10 · √10 ≈ 31,6")]


def b_tabela(c, t, C, B):
    head(c, t, B["start"], "UMA TABELA QUE VALE OURO", "DIFERENÇA → RAZÃO", PURPLE)
    card(c, *CARD_R)
    x, y, rh = 330, 240, 96
    rrect(c, x, y, 1260, 60, 12, mix("#FFFFFF", PURPLE, 0.14), 1.0)
    for s_, xx in (("diferença na escala", x + 200), ("razão", x + 620), ("por quê", x + 1000)):
        text_mid(c, s_, xx, y + 30, 26, "black", PURPLE, 1.0)
    for k, (cue, dif, raz, pq) in enumerate(TABELA):
        ak, d = rise(t, C[cue])
        if ak <= 0:
            continue
        yy = y + 70 + k * rh + d
        rrect(c, x, yy, 1260, rh - 12, 12, "#FFFFFF", ak, shadow=True)
        text_mid(c, dif, x + 200, yy + (rh - 12) / 2, 46, "black", INK, ak)
        arrow(c, x + 360, yy + (rh - 12) / 2, x + 470, yy + (rh - 12) / 2, GRAY, ak, 4, 12)
        text_mid(c, raz, x + 620, yy + (rh - 12) / 2, 46, "black", GREEN, ak)
        text_mid(c, pq, x + 1000, yy + (rh - 12) / 2, 34, "black", INK2, ak)


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "UM SEGUIDO DE ZEROS", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5)
    K.atalho(c, 260, 210, 1400, 90, "DIFERENÇA INTEIRA = QUANTIDADE DE ZEROS", [""], aa, 30)
    if aa > 0:
        text_mid(c, "diferença 3", 560, 420, 54, "black", INK, aa)
        arrow(c, 760, 420, 900, 420, GREEN, aa, 5, 14)
        digs = ["1", "0", "0", "0"]
        for k, dg in enumerate(digs):
            ak = ep(t, C["09.a"] + 2.6 + 0.35 * k, 0.3)
            text_mid(c, dg, 990 + k * 80 + (40 if k == 1 else 0) * 0, 420, 110, "black", GREEN if k else INK, ak)
        text_mid(c, "= mil", 1430, 420, 54, "black", GREEN, ep(t, C["09.a"] + 4.2, 0.4))
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        boxed(c, 460, 560, 1000, 170, GREEN, ab, 0.08)
        text(c, "E O 0,3?", W / 2, 610, 26, "black", GREEN, ab, tracking=2)
        text_mid(c, "+ 0,3 na leitura  ≈  o DOBRO", W / 2, 670, 50, "black", INK, ab)


# ======================================================================
# bloco d — diferença não é razão
# ======================================================================

def b_armadilha(c, t, C, B):
    head(c, t, B["start"], "ARMADILHA", "DIFERENÇA NÃO É RAZÃO", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        chip(c, "pH 2", 780, 260, LIMAO, aa, 44)
        chip(c, "pH 5", 1140, 260, CAFE, aa, 44)
    cards = [("10.b", "DIVIDIR AS LEITURAS", "5 ÷ 2 = 2,5", RED, False),
             ("10.c", "SUBTRAIR E PARAR", "5 − 2 = 3", RED, False),
             ("10.e", "A DIFERENÇA É O EXPOENTE", "10³ = 1 000", GREEN, True)]
    for k, (cue, tit, conta, col, ok) in enumerate(cards):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 280 + k * 470
        rrect(c, x, 360, 430, 260, 24, mix("#FFFFFF", col, 0.08), ak, shadow=True)
        text(c, tit, x + 215, 410, 22, "black", col, ak, tracking=1)
        text_mid(c, conta, x + 215, 500, 54, "black", INK, ak)
        check_icon(c, x + 215, 575, 26, ep(t, C[cue] + 1.2, 0.4), col, "check" if ok else "x")
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        selo(c, 740, 720, ad, "OS 2 DISTRATORES CLÁSSICOS", AMBER, -3, 32)


# ======================================================================
# bloco e — o que é pH · bloco f — número na frente da potência
# ======================================================================

def b_ph(c, t, C, B):
    head_seq(c, t, C, [("11", "O QUE É pH?", "CONCENTRAÇÃO DE H⁺", BLUE),
                       ("12", "A MESMA FÓRMULA", "DE TRÁS PARA FRENTE", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        defs = [("11.a", "CONCENTRAÇÃO", "quanto de uma coisa está dissolvida num volume"),
                ("11.b", "ÍON HIDROGÊNIO · H⁺", "partícula minúscula que deixa a solução ácida"),
                ("11.c", "mol/L", "mol = unidade de quantidade (como a dúzia) por litro")]
        for k, (cue, tit, s_) in enumerate(defs):
            ak, d = rise(t, C[cue])
            if ak <= 0:
                continue
            y = 220 + k * 130 + d
            rrect(c, 280, y, 1360, 110, 20, mix("#FFFFFF", BLUE, 0.08), ak)
            text(c, tit, 320, y + 66, 32, "black", BLUE, ak, align="left")
            text(c, s_, 1600, y + 66, 28, "bold", INK, ak, align="right")
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            rrect(c, 460, 640, 1000, 160, 28, mix("#FFFFFF", PURPLE, 0.10), ad)
            fm(c, [("pH = −log [H⁺]", PURPLE)], W / 2, 720, 76, ad)
        return
    aa = ep(t, C["12"], 0.5)
    if aa > 0:
        rrect(c, 300, 220, 1320, 160, 28, mix("#FFFFFF", PURPLE, 0.10), aa)
        fm(c, [("pH = −log [H⁺]", PURPLE), ("   ⟺   ", INK), ("[H⁺] = ", PURPLE), ("10^{−pH}", PURPLE, "m"),
               (" mol/L", PURPLE)], W / 2, 300, 56, aa)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        rrect(c, 300, 420, 860, 220, 24, "#FFFFFF", acc, shadow=True)
        text(c, "POR QUE O MENOS?", 730, 462, 24, "black", AMBER, acc, tracking=2)
        fm(c, [("log ", INK), ("10^{−3}", INK, "m"), (" = ", INK), ("−3", RED)], 730, 525, 46, acc)
        fm(c, [("pH = −(−3) = ", INK), ("3", GREEN)], 730, 595, 46, ep(t, C["12.c"] + 3.2, 0.4))
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        rrect(c, 1200, 420, 420, 220, 24, mix("#FFFFFF", BLUE, 0.10), ad)
        text(c, "NEUTRA (25 °C)", 1410, 470, 24, "black", BLUE, ad, tracking=2)
        text_mid(c, "pH 7", 1410, 555, 80, "black", BLUE, ad)
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        pill(c, "pH + pOH = 14 · fica para a Química", W / 2, 720, GRAY, size=26, a=ae, anchor="center")


LINHAS_PH = [("13.a", [("10^{−3}", INK, "m")], [("−(−3)", INK)], "3"),
             ("13.b", [("2", BLUE), (" · ", INK), ("10^{−5}", PURPLE, "m")],
              [("−(", INK), ("0,30", BLUE), (" − 5", PURPLE), (")", INK)], "4,7"),
             ("14.a", [("5", BLUE), (" · ", INK), ("10^{−4}", PURPLE, "m")],
              [("−(", INK), ("0,70", BLUE), (" − 4", PURPLE), (")", INK)], "3,3")]
LINHAS_OK = {"13.a": "13.a", "13.b": "13.d", "14.a": "14.d"}


def tabela_ph(c, t, C, a, x=230, y=220, rh=96):
    if a <= 0:
        return
    rrect(c, x, y, 900, 56, 12, mix("#FFFFFF", PURPLE, 0.14), a)
    for s_, xx in (("[H⁺] (mol/L)", x + 160), ("conta", x + 500), ("pH", x + 800)):
        text_mid(c, s_, xx, y + 28, 26, "black", PURPLE, a)
    for k, (cue, conc, conta, ph) in enumerate(LINHAS_PH):
        ak, d = rise(t, C[cue])
        ak *= a
        if ak <= 0:
            continue
        yy = y + 66 + k * rh + d
        cy = yy + (rh - 12) / 2
        rrect(c, x, yy, 900, rh - 12, 12, "#FFFFFF", ak, shadow=True)
        fm(c, conc, x + 160, cy, 40, ak)
        fm(c, conta, x + 500, cy, 40, ak * ep(t, C[cue] + 1.0, 0.4))
        text_mid(c, ph, x + 800, cy, 48, "black", GREEN, ep(t, C[LINHAS_OK[cue]], 0.4) * a)


def b_contas(c, t, C, B):
    head_seq(c, t, C, [("13", "NÚMERO NA FRENTE?", "LOG DO PRODUTO É SOMA", PURPLE),
                       ("14", "MAIS UM", "O LOG DE 5 SAI DO LOG DE 2", PURPLE)])
    card(c, *CARD_R)
    tabela_ph(c, t, C, 1.0)
    sid = which(t, C, ["13", "14"])
    x0, y0 = 1180, 220
    if sid == "13":
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            rrect(c, x0, y0, 520, 400, 24, "#FFFFFF", acc, shadow=True)
            text(c, "DUAS PARCELAS", x0 + 260, y0 + 46, 24, "black", GRAY, acc, tracking=2)
            fm(c, [("log(2 · ", INK), ("10^{−5}", INK, "m"), (")", INK)], x0 + 260, y0 + 120, 40, acc)
            fm(c, [("= ", INK), ("log 2", BLUE), (" + ", INK), ("log ", PURPLE), ("10^{−5}", PURPLE, "m")], x0 + 260,
               y0 + 200, 40, ep(t, C["13.c"] + 1.0, 0.4))
            fm(c, [("= ", INK), ("0,30", BLUE), (" + ", INK), ("(−5)", PURPLE)], x0 + 260, y0 + 280, 40,
               ep(t, C["13.c"] + 3.0, 0.4))
            ad = ep(t, C["13.d"], 0.4)
            fm(c, [("= ", INK), ("−4,7", RED), ("  →  pH ", INK), ("4,7", GREEN)], x0 + 260, y0 + 355, 40, ad)
        return
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        rrect(c, x0, y0, 520, 300, 24, "#FFFFFF", ab, shadow=True)
        text(c, "E O LOG DE 5?", x0 + 260, y0 + 46, 24, "black", GRAY, ab, tracking=2)
        fm(c, [("5 = 10 ÷ 2", INK)], x0 + 260, y0 + 120, 42, ab)
        fm(c, [("log 5 = 1 − ", INK), ("0,30", BLUE)], x0 + 260, y0 + 190, 42, ep(t, C["14.b"] + 1.4, 0.4))
        fm(c, [("= ", INK), ("0,70", BLUE)], x0 + 260, y0 + 255, 46, ep(t, C["14.b"] + 3.0, 0.4))
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        fm(c, [("0,70", BLUE), (" − 4 = ", PURPLE), ("−3,3", RED)], x0 + 260, y0 + 380, 44, acc)


def b_atalho2(c, t, C, B):
    head(c, t, B["start"], "ATALHO DO pH", "ELIMINE ANTES DA CONTA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        boxed(c, 300, 210, 1320, 200, GREEN, aa, 0.08)
        fm(c, [("[H⁺] = k · ", INK), ("10^{−n}", INK, "m"), ("    com 1 < k < 10", GRAY)], W / 2, 270, 46, aa)
        ab = ep(t, C["15.b"], 0.5)
        fm(c, [("pH = n − log k   →   entre ", INK), ("n − 1", GREEN), (" e ", INK), ("n", GREEN)], W / 2, 355, 46, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        x0, x1, y = 460, 1460, 600
        line(c, x0 - 60, y, x1 + 60, y, INK, acc, 5)
        for x, s_ in ((x0, "4"), (x1, "5")):
            line(c, x, y - 18, x, y + 18, INK, acc, 4)
            text(c, s_, x, y + 66, 40, "black", INK, acc)
        rrect(c, x0, y - 12, x1 - x0, 24, 10, GREEN, acc * 0.3)
        fm(c, [("2 · ", INK), ("10^{−5}", INK, "m"), (": pH entre 4 e 5", INK)], W / 2, 490, 40, acc)
        a4 = ep(t, C["15.c"] + 2.4, 0.4)
        if a4 > 0:
            xm = x0 + 0.7 * (x1 - x0)
            c.drawCircle(xm, y, 18, paint(GREEN, a4))
            pill(c, "4,7", xm, y - 60, GREEN, size=28, a=a4, anchor="center")
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        selo(c, W / 2, 780, ad, "ELIMINA ALTERNATIVAS ANTES DE QUALQUER CONTA", GREEN, -2, 28)


# ======================================================================
# bloco h — a régua de pH e a pilha de H⁺
# ======================================================================

PILHAS = [(2, 1000, LIMAO, "limão"), (3, 100, None, ""), (4, 10, None, ""), (5, 1, CAFE, "café")]


def b_regua_ph(c, t, C, B):
    head(c, t, B["start"], "MENOR pH, MAIS ÁCIDO", "A ESCALA DE CABEÇA PARA BAIXO", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    ad = ep(t, C["16.d"], 0.5)
    marcas = [(2, "limão", mix(LIMAO, INK, 0.25)), (5, "café", CAFE)] if ad > 0 else []
    regua_ph(c, 380, 300, 1160, aa, marcas)
    ab = ep(t, C["16.b"], 0.5)
    for k, (ph, n, cor, nome) in enumerate(reversed(PILHAS)):
        ak = ep(t, C["16.b"] + 0.9 * k, 0.4) * ab
        if ak <= 0:
            continue
        x = 1460 - k * 370
        rrect(c, x - 150, 420, 300, 330, 22, "#FFFFFF", ak, shadow=True)
        text(c, f"pH {ph}", x, 462, 30, "black", INK, ak)
        pilha(c, x, 700, n, ak, dot=5, gap=2)
        text(c, f"{n:,}".replace(",", " ") + (" bolinha" if n == 1 else " bolinhas"), x, 738, 22, "bold", GRAY, ak)
        if k:
            arrow(c, x + 220, 600, x + 154, 600, GREEN, ak, 4, 10)
            text(c, "×10", x + 185, 575, 22, "black", GREEN, ak)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        selo(c, 600, 795, acc, "MENOR pH = MAIS H⁺", PURPLE, -3, 30)
    if ad > 0:
        rrect(c, 980, 762, 620, 66, 18, mix("#FFFFFF", GREEN, 0.14), ad)
        text_mid(c, "limão × café: 3 passos → 1 000 ×", 1290, 795, 30, "black", GREEN, ad)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("17", "SUA VEZ", "PAUSE E TENTE", GREEN), ("18", "VAMOS JUNTOS", "A DIFERENÇA VIRA EXPOENTE", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        chip(c, "solução 1 · pH 4", 680, 260, PURPLE, aa, 40)
        chip(c, "solução 2 · pH 6", 1240, 260, PURPLE, aa, 40)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        text(c, "quantas vezes mais H⁺ tem a solução 1?", W / 2, 370, 40, "black", INK, ab)
    pause_timer(c, t, C["17.end"] - 1.9, W / 2, 560)
    if t < C["18"]:
        return
    steps = [("18.a", [("diferença: 6 − 4 = ", INK), ("2", AMBER)]),
             ("18.b", [("10^{2}", GREEN, "m"), (" = ", INK), ("100 vezes", GREEN)])]
    for k, (cue, partes) in enumerate(steps):
        ak, d = rise(t, C[cue])
        fm(c, partes, W / 2, 470 + k * 110 + d, 54, ak)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        conferido(c, "a solução 1 tem o pH MENOR: é ela que tem mais H⁺", 420, 760, acc, True, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Numa escala de base 10, a diferença de leitura é o expoente da razão.",
          "Menor pH, mais ácido: cada unidade a menos é 10 vezes mais H⁺.",
          "Se [H⁺] = k · 10⁻ⁿ, o pH fica entre n − 1 e n."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["19", "32"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "19" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("pH 2 e pH 5: 3 vezes mais ácido", "os passos da régua são iguais e subtrair parece natural",
          "cada passo é ×10: diferença 3 → 10³ = 1 000 vezes"),
         ("pH MAIOR = mais ácido", "número maior costuma significar MAIS",
          "o MENOS da fórmula inverte: pH maior = MENOS H⁺"),
         ("log(2 · 10⁻⁵) = log 2 · (−5)", "tem um VEZES lá dentro",
          "log do produto é SOMA: 0,30 − 5 → pH 4,7 (o erro dá 1,5, fora de 4 a 5)")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["20", "21", "22"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _painel(c, y0, a, y1=830):
    rrect(c, 170, y0, 740, y1 - y0, 18, "#FFFFFF", a, shadow=True)


def alts(c, t, C, itens, x, y0, size, ok_cue, okL, cues_in, cues_x, gap=26):
    """alternativas com fórmula mista: itens = [(letra, partes_fm, motivo)]"""
    aok = ep(t, ok_cue, 0.5)
    y = y0
    hh = size * 1.7
    for L, partes, why in itens:
        a, d = rise(t, cues_in.get(L, 1e9))
        ok = L == okL
        ax = ep(t, cues_x.get(L, 1e9), 0.4) if not ok else 0
        if a > 0:
            if ok and aok > 0:
                rrect(c, x - 20, y - 10 + d, 720, hh + 20, 14, GREEN, 0.15 * aok)
            badge_num(c, L, x + 10, y + hh / 2 + d, a, 22, bg=GREEN if ok and aok > 0.5 else INK)
            cyy = y + d + hh / 2
            w_ = fm(c, partes, x + 50, cyy, size, a * (1 - 0.5 * ax), align="left")
            if ax > 0:
                strike(c, x + 46, cyy, x + 54 + w_, cyy, ax, RED, ax)
                if why:
                    pill(c, why, x + 700, cyy + size * 0.95, RED, size=18, a=ax, anchor="right", bounds=(0, 1920))
        y += hh + gap
    return y


def enunciado(c, s, a, y=240, size=26, maxw=700):
    for ln in K.wrap(s, "black", size, maxw):
        ftext(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 10
    return y


def fonte(c, t, a, fim):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a * (1 - ep(t, fim, 0.3)),
         align="left")


ALTS1 = [("A", [("2 vezes maior", INK)], "dividiu os pHs: 6 ÷ 3"), ("B", [("3 vezes maior", INK)], "parou na diferença"),
         ("C", [("30 vezes maior", INK)], "diferença × 10"), ("D", [("1 000 vezes maior", INK)], ""),
         ("E", [("1 000 000 vezes maior", INK)], "só o pH da chuva: 10⁶")]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · EU FAÇO", "COMPARAR ACIDEZ", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    y = enunciado(c, "O pH de uma solução é dado por pH = −log [H⁺], em que [H⁺] é a concentração de íons hidrogênio, "
                     "em mol/L. Um suco industrializado tem pH 3, e uma amostra de água de chuva tem pH 6. A concentração "
                     "de íons H⁺ no suco é, em relação à da água de chuva,", a0)
    fonte(c, t, a0, C["24"])
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABCE"}
    alts(c, t, C, ALTS1, 1000, 250, 40, C["24.ok"], "D", cues_in, cues_x)
    if t < C["24"]:
        return
    y0 = y + 14
    _painel(c, y0, ep(t, C["24"], 0.4))
    pill(c, "pergunta: COMPARAR duas leituras", 540, y0 + 45, PURPLE, size=22, a=ep(t, C["24"], 0.4), anchor="center")
    fm(c, [("diferença: 6 − 3 = ", INK), ("3", AMBER)], 540, y0 + 115, 36, ep(t, C["24.a"], 0.4))
    fm(c, [("(10^{−3}/10^{−6})", INK, "m"), (" = ", INK), ("10^{3}", GREEN, "m"), (" = 1 000", GREEN)], 540, y0 + 200,
       34, ep(t, C["24.b"], 0.4))
    acc = ep(t, C["24.c"], 0.4)
    if acc > 0:
        conferido(c, "suco: pH MENOR → mais H⁺", 250, y0 + 290, acc, True, 28)


ALTS2 = [("A", [("3,4", INK)], "descontou 2 · log 2"), ("B", [("3,7", INK)], ""), ("C", [("4,0", INK)], "ignorou o 2"),
         ("D", [("4,3", INK)], "somou o log 2: sinal"), ("E", [("4,6", INK)], "sinal errado e log 2 dobrado")]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · NÓS FAZEMOS", "pH DE UMA CHUVA ÁCIDA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    y = enunciado(c, "Uma estação de monitoramento coletou água de chuva com concentração de íons H⁺ igual a "
                     "2 · 10⁻⁴ mol/L. Sabendo que pH = −log [H⁺] e usando log 2 = 0,30, o pH dessa amostra é", a0)
    fonte(c, t, a0, C["27"])
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ACDE"}
    alts(c, t, C, ALTS2, 1000, 250, 44, C["27.ok"], "B", cues_in, cues_x)
    ap = ep(t, C["26.p"], 0.4) * (1 - ep(t, C["27"], 0.4))
    if ap > 0:
        fm(c, [("pH entre ", INK), ("?", AMBER), (" e ", INK), ("?", AMBER)], 540, y + 120, 54, ap)
    if t < C["27"]:
        return
    a1 = ep(t, C["27"], 0.4)
    # o atalho elimina C, D e E antes da conta
    for k, L in enumerate("CDE"):
        aL = ep(t, C["27"] + 1.4 + 0.2 * k, 0.3) * (1 - ep(t, C["28"], 0.3))
        if aL > 0:
            pill(c, "fora de 3 a 4", 1700, 250 + "ABCDE".index(L) * (44 * 1.7 + 26) + 37, AMBER, size=18, a=aL,
                 anchor="right", bounds=(0, 1920))
    y0 = y + 14
    _painel(c, y0, a1)
    fm(c, [("atalho: ", GREEN), ("2 · ", INK), ("10^{−4}", INK, "m"), (" → pH entre ", INK), ("3 e 4", GREEN)], 540,
       y0 + 50, 30, a1)
    fm(c, [("log(2 · ", INK), ("10^{−4}", INK, "m"), (") = ", INK), ("0,30", BLUE), (" − 4", PURPLE), (" = −3,7", RED)],
       540, y0 + 140, 32, ep(t, C["27.a"], 0.4))
    fm(c, [("pH = −(−3,7) = ", INK), ("3,7", GREEN)], 540, y0 + 225, 40, ep(t, C["27.b"], 0.4))
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        conferido(c, "mais perto de 4: o 2 é pequeno", 250, y0 + 305, acc, True, 26)


ALTS6 = [("A", [("10^{−7,8}", INK, "m")], "inverteu: maior pH"), ("B", [("10^{−7,2}", INK, "m")], ""),
         ("C", [("10^{−0,6}", INK, "m")], "largura da faixa"), ("D", [("10^{7,2}", INK, "m")], "sem o sinal: absurdo"),
         ("E", [("10^{7,8}", INK, "m")], "sem o sinal: absurdo")]


def b_q6(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 6 · VOCÊ FAZ", "A FAIXA DE pH DA PISCINA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["29.a"], 0.4)
    y = enunciado(c, "Para o conforto dos banhistas e a eficiência do cloro, recomenda-se que o pH da água de piscinas "
                     "fique entre 7,2 e 7,8. Sabendo que", a0)
    fm(c, [("[H⁺] = ", INK), ("10^{−pH}", INK, "m"), (" mol/L,", INK)], 190, y + 8, 28, a0, align="left")
    y = enunciado(c, "a maior concentração de íons H⁺ admitida nessa faixa, em mol/L, é", a0, y + 54)
    fonte(c, t, a0, C["30"])
    cues_in = {L: C[f"29.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"31.x{L.lower()}"] for L in "ACDE"}
    alts(c, t, C, ALTS6, 1000, 240, 44, C["30.ok"], "B", cues_in, cues_x)
    if t < C["30"]:
        pause_timer(c, t, C["29.end"] - 1.9, 540, 700)
        return
    y0 = y + 14
    _painel(c, y0, ep(t, C["30"], 0.4))
    fm(c, [("maior [H⁺]  →  ", INK), ("MENOR pH", GREEN), (": 7,2", INK)], 540, y0 + 60, 34, ep(t, C["30.a"], 0.4))
    fm(c, [("[H⁺] = ", INK), ("10^{−7,2}", GREEN, "m")], 540, y0 + 150, 44, ep(t, C["30.b"], 0.4))
    acc = ep(t, C["30.c"], 0.4)
    if acc > 0:
        conferido(c, "−7,2 > −7,8: mais perto do zero", 250, y0 + 245, acc, True, 26)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "TERREMOTOS", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    for k, (m, x) in enumerate(((7, 620), (5, 1300))):
        ak = ep(t, C["33.a"] + 1.2 * k, 0.4) * aa
        if ak <= 0:
            continue
        rrect(c, x - 250, 240, 500, 240, 30, "#FFFFFF", ak, shadow=True)
        text(c, "magnitude", x, 300, 30, "black", GRAY, ak)
        text_mid(c, str(m), x, 400, 120, "black", INK, ak)
    ab = ep(t, C["33.b"], 0.5)
    for k, s_ in enumerate(("2 ×?", "100 ×?", "1 000 ×?")):
        ak = ep(t, C["33.b"] + 1.0 * k, 0.4) * ab
        chip(c, s_, 560 + k * 400, 610, AMBER, ak, 46)
    if ab > 0:
        text(c, "a ENERGIA é quantas vezes maior?", W / 2, 540, 34, "black", INK, ab)
    pill(c, "ep. 3 · terremotos: amplitude, energia e magnitude", W / 2, 770, PURPLE, size=30,
         a=ep(t, C["33.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"],
        "Você já tinha caído no \"3 vezes mais ácido\"?", canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, problema=b_problema, regra=b_regra,
              tabela=b_tabela, atalho=b_atalho, armadilha=b_armadilha, ph=b_ph, contas=b_contas, atalho2=b_atalho2,
              regua_ph=b_regua_ph, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q2=b_q2, q6=b_q6,
              ponte=b_ponte, cta=b_cta)
