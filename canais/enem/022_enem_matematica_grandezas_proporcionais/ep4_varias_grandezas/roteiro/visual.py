"""Visual — Grandezas Proporcionais, Episódio 4: várias grandezas ao mesmo tempo (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: andares() (a fração-guia de dois andares), mangueira(), fio() (cresce e engrossa, com a seta da
resistência) e seringa() (o êmbolo de Boyle comprimindo o gás).
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
_s = importlib.util.spec_from_file_location("comum022", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_grandezas_ep4_varias_grandezas.mp4"
CARD_R = K.CARD_R
COBRE = "#C8742B"
COBRE_ESC = "#8E4F1A"
AGUA = "#4FA3F7"
MANG = "#2E9E5B"
GAS = "#7CB7F5"


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# peças do episódio
# ======================================================================

def andares(c, cx, cy, a, cima=(), baixo=(), w=620, pre="y = k ·", size=44, lado=True):
    """a fração-guia de dois andares. cima/baixo = [(texto, alfa)] — fichas que 'sobem' e 'descem' para o seu andar"""
    if a <= 0:
        return
    pw = text_w(pre, "black", size + 16) if pre else 0
    if pre:
        text(c, pre, cx - w / 2 - 30, cy + 20, size + 16, "black", PURPLE, a, align="right")
    rrect(c, cx - w / 2, cy - 150, w, 130, 22, "#EAF7EF", a)
    rrect(c, cx - w / 2, cy + 20, w, 130, 22, "#EEF3FE", a)
    line(c, cx - w / 2 - 10, cy, cx + w / 2 + 10, cy, INK, a, 8)
    if lado:
        text(c, "EM CIMA: DIRETO", cx + w / 2 + 30, cy - 75, 26, "black", GREEN, a, align="left")
        text(c, "EMBAIXO: INVERSO", cx + w / 2 + 30, cy + 95, 26, "black", BLUE, a, align="left")
    for lst, y0, d in ((cima, cy - 85, -1), (baixo, cy + 85, 1)):
        n = len(lst)
        for k, (s, ak) in enumerate(lst):
            if ak <= 0:
                continue
            x = cx - w / 2 + w * (k + 0.5) / max(n, 1)
            off = (1 - ease_io(clamp(ak, 0, 1))) * 60 * (-d)
            chip(c, s, x, y0 + off, GREEN if d < 0 else BLUE, a * ak, size - 6)


def mangueira(c, x, y, comp, grossura, a, fluxo=0.0, rotulo=None, col=MANG):
    """mangueira horizontal de comprimento `comp` px e espessura `grossura` px; fluxo = 0..1 (gotas andando)"""
    if a <= 0:
        return
    h = grossura
    rrect(c, x, y - h / 2, comp, h, h / 2, col, a)
    rrect(c, x + 6, y - h / 2 + 6, comp - 12, h - 12, (h - 12) / 2, AGUA, a * 0.55)
    n = max(3, int(comp / 70))
    for k in range(n):
        px = x + ((k / n + fluxo) % 1.0) * comp
        c.drawCircle(px, y, max(4, h * 0.16), paint("#FFFFFF", a * 0.85))
    if rotulo:
        text(c, rotulo, x + comp / 2, y + h / 2 + 46, 28, "black", INK2, a)


def fio(c, x, y, comp, grossura, a, rotulo=None, seta=0, seta_a=0.0):
    """fio de cobre (cilindro deitado) com a 'boca' (seção transversal) à direita; seta = +1 sobe, -1 desce (resistência)"""
    if a <= 0:
        return
    h = grossura
    rrect(c, x, y - h / 2, comp, h, h / 2.4, COBRE, a, shadow=True)
    rrect(c, x + 8, y - h / 2 + 5, comp - 16, h * 0.22, h * 0.1, "#F2B27A", a * 0.8)
    c.drawOval(skia.Rect.MakeXYWH(x + comp - h * 0.35, y - h / 2, h * 0.7, h), paint(COBRE_ESC, a))
    c.drawOval(skia.Rect.MakeXYWH(x + comp - h * 0.27, y - h / 2 + h * 0.12, h * 0.54, h * 0.76), paint("#E39A5A", a))
    if rotulo:
        text(c, rotulo, x + comp / 2, y + h / 2 + 46, 28, "black", INK2, a)
    if seta and seta_a > 0:
        ax = x + comp + h * 0.5 + 60
        col = RED if seta > 0 else GREEN
        if seta > 0:
            arrow(c, ax, y + 60, ax, y - 60, col, seta_a, 8, 22, progress=seta_a)
        else:
            arrow(c, ax, y - 60, ax, y + 60, col, seta_a, 8, 22, progress=seta_a)
        text(c, "R", ax + 34, y + 12, 34, "black", col, seta_a)


def seringa(c, x, y, frac, a, w=560, h=150, rot_p=None, rot_v=None):
    """seringa tampada deitada: o êmbolo entra da direita; frac = fração do cilindro ocupada pelo gás (1 = cheio)"""
    if a <= 0:
        return
    rrect(c, x - 30, y + 14, 34, h - 28, 8, INK2, a)                      # tampa
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(INK, a, stroke=6))
    gw = w * frac
    rrect(c, x + 6, y + 6, gw - 12, h - 12, 12, GAS, a * 0.35)
    rnd = [(0.12, 0.3), (0.3, 0.7), (0.5, 0.25), (0.7, 0.62), (0.86, 0.35), (0.22, 0.55), (0.62, 0.42), (0.42, 0.8)]
    for fx, fy in rnd:
        c.drawCircle(x + 10 + fx * (gw - 20), y + 12 + fy * (h - 24), 9, paint(BLUE, a * 0.8))
    px = x + gw
    rrect(c, px, y + 8, 22, h - 16, 6, INK, a)                           # êmbolo
    rrect(c, px + 22, y + h / 2 - 12, w * (1 - frac) + 140, 24, 8, INK2, a)  # haste
    rrect(c, px + w * (1 - frac) + 150, y + h / 2 - 50, 26, 100, 8, INK, a)  # cabo
    if rot_v:
        text(c, rot_v, x + gw / 2, y + h + 50, 32, "black", BLUE, a)
    if rot_p:
        text(c, rot_p, px + w * (1 - frac) + 160, y - 26, 30, "black", RED, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "VÁRIAS GRANDEZAS", BLUE)
    forms = [("v = d/t", 330, 330), ("R = k · L/A", 960, 300), ("P · V = k", 1590, 330), ("F = m · a", 520, 560),
             ("d = m/V", 1400, 560)]
    for k, (s, x, y) in enumerate(forms):
        a = ep(t, C["01.a"] + 0.25 * k, 0.5)
        expr(c, s, x, y, 64, a, cores=mono(s, INK))
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        regra(c, "cada fórmula = uma FRASE sobre proporção", W / 2, 700, ab, 36)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        ftext(c, "decorar  ✗", 640, 800, 40, "black", RED, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        ftext(c, "raciocinar  ✓", 1280, 800, 40, "black", GREEN, ad)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "montar a fórmula a partir do enunciado", "direto em cima, inverso embaixo"),
            ("02.b", "saber o efeito de várias mudanças juntas", "a dobra, b triplica… e o y?"),
            ("02.c", "ler qualquer fórmula sem medo", "v = d/t, F = m · a, P · V = k…")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 360, y + 56, 32, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "EPISÓDIO 1", 560, 250, GRAY, size=22, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "O k: o número que não muda", 560, 330, 36, "black", PURPLE, aa)
        expr(c, "direta:  y = k · x", 560, 450, 50, aa, cores={2: PURPLE})
        expr(c, "inversa:  y = k/x", 560, 570, 50, aa, cores={2: PURPLE})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "SÉRIE DE FRAÇÕES", 1360, 250, GRAY, size=22, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "× 2/3  =  × 2  e  ÷ 3", 1360, 330, 36, "black", PURPLE, ab)
        expr(c, "12 × 2/3 = 24 ÷ 3 = 8", 1360, 490, 58, ab, cores={6: GREEN})
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)


# ======================================================================
# concreto — a mangueira
# ======================================================================

def b_mangueira(c, t, C, B):
    frame(c, t, B["start"], "DUAS CAUSAS", "AO MESMO TEMPO", BLUE)
    fl = (t * 0.35) % 1.0
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        mangueira(c, 260, 320, 700, 44, aa, fl * 0.5, "mais comprida")
        ftext(c, "comprimento ATRAPALHA ↓ fluxo", 1340, 330, 38, "black", RED, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        mangueira(c, 260, 530, 400, 100, ab, fl, "mais grossa")
        ftext(c, "grossura FACILITA ↑ fluxo", 1340, 540, 38, "black", GREEN, ab)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        regra(c, "duas causas, lados contrários… numa conta só?", W / 2, 760, acc, 36)


# ======================================================================
# bloco A — a fração-guia
# ======================================================================

def b_guia(c, t, C, B):
    head_seq(c, t, C, [("05", "A FRAÇÃO-GUIA", "DOIS ANDARES", PURPLE), ("06", "POR QUE FUNCIONA", "DOBRE E VEJA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        if aa > 0:
            andares(c, 860, 470, aa, lado=False, pre=None)
            text(c, "NUMERADOR", 860, 300, 28, "black", INK2, aa)
            text(c, "DENOMINADOR", 860, 670, 28, "black", INK2, aa)
        ab, acc = ep(t, C["05.b"], 0.5), ep(t, C["05.c"], 0.5)
        if ab > 0:
            andares(c, 860, 470, ab, cima=[("a: direto", ab)], baixo=[("b: inverso", acc)], pre=None, w=620)
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            rrect(c, 300, 720, 1320, 100, 20, "#F4F0FE", ad)
            expr(c, "y = k · a/b", W / 2, 770, 64, ad, cores={2: PURPLE, 4: GREEN})
        return
    expr(c, "y = k · a/b", 500, 330, 90, 1.0, cores={2: PURPLE})
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        ftext(c, "a × 2  (em cima)", 1160, 290, 40, "black", GREEN, aa, align="left")
        ftext(c, "→ y × 2 · DIRETA", 1160, 350, 40, "black", GREEN, aa, align="left")
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        ftext(c, "b × 2  (embaixo)", 1160, 460, 40, "black", BLUE, ab, align="left")
        ftext(c, "→ y ÷ 2 · INVERSA", 1160, 520, 40, "black", BLUE, ab, align="left")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        K.atalho(c, 260, 560, 760, 230, "ATALHO", ["AUMENTA o resultado? → em cima", "DIMINUI o resultado? → embaixo"], acc, 34)


# ======================================================================
# bloco B — o fio condutor
# ======================================================================

def b_fio(c, t, C, B):
    head_seq(c, t, C, [("07", "O FIO ELÉTRICO", "O QUE ATRAPALHA", BLUE), ("08", "A FÓRMULA DA FÍSICA", "R = ρ · L/A", PURPLE),
                       ("09", "1º CAMINHO", "ACHANDO O k", PURPLE), ("10", "2º CAMINHO", "PELOS EFEITOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08", "09", "10"])
    if sid == "07":
        aa = ep(t, C["07.a"], 0.5)
        if aa > 0:
            boxed(c, 220, 200, 1480, 110, BLUE, aa, 0.08)
            text(c, "RESISTÊNCIA ELÉTRICA = o quanto o fio ATRAPALHA a eletricidade", W / 2, 268, 34, "black", BLUE, aa)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            grow = ep(t, C["07.b"], 1.0)
            fio(c, 260, 430, 300 + 400 * grow, 50, ab, "mais comprido", +1, ep(t, C["07.b"] + 0.6, 0.4))
            text(c, "DIRETO", 1500, 440, 36, "black", GREEN, ab)
        acc = ep(t, C["07.c"], 0.5)
        if acc > 0:
            thick = ep(t, C["07.c"], 1.0)
            fio(c, 260, 640, 500, 50 + 60 * thick, acc, "mais grosso", -1, ep(t, C["07.c"] + 0.6, 0.4))
            text(c, "INVERSO", 1500, 650, 36, "black", BLUE, ep(t, C["07.d"], 0.4))
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            pill(c, "SEÇÃO TRANSVERSAL = a área da 'boca' do fio", 1140, 790, BLUE, size=24, a=ad, anchor="center",
                 bounds=(0, 1920))
        return
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        andares(c, 860, 400, aa, cima=[("L: comprimento", aa)], baixo=[("A: área", aa)], pre="R = k ·", w=560, size=40)
        ab = ep(t, C["08.b"], 0.5)
        if ab > 0:
            rrect(c, 300, 600, 640, 160, 20, "#F4F0FE", ab)
            text(c, "NA FÍSICA", 620, 640, 24, "black", INK2, ab)
            ftext(c, "R = ρ · L ÷ A", 620, 715, 56, "black", PURPLE, ab)
        acc = ep(t, C["08.c"], 0.5)
        if acc > 0:
            boxed(c, 1010, 600, 620, 160, BLUE, acc, 0.08)
            ftext(c, "ρ (rô) = RESISTIVIDADE", 1320, 655, 32, "black", BLUE, acc)
            text(c, "o quanto o MATERIAL atrapalha", 1320, 710, 26, "bold", INK2, acc)
        ad = ep(t, C["08.d"], 0.5)
        if ad > 0:
            selo(c, 1320, 805, ad, "ρ É O NOSSO k", GREEN, -3, 28)
        return
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        fio(c, 240, 290, 360, 50, aa, "6 m · 2 mm² · 6 Ω")
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            expr(c, "6 = k · 6/2 = k · 3", 1220, 280, 52, ab, cores=mono("6 = k · 6/2 = k · 3", INK))
            ftext(c, "k = 2", 1220, 380, 56, "black", PURPLE, ab)
        acc = ep(t, C["09.c"], 0.5)
        fio(c, 240, 560, 720, 66, acc, "12 m · 3 mm² · ? Ω")
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            expr(c, "R = 2 · 12/3 = 2 · 4 = 8", 1260, 560, 52, ad, cores={8: GREEN})
            ftext(c, "8 Ω", 1260, 690, 64, "black", GREEN, ad)
        return
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        ftext(c, "comprimento: 6 → 12", 300, 290, 40, "black", INK, aa, align="left")
        ftext(c, "em cima: × 2", 1000, 290, 40, "black", GREEN, aa, align="left")
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        ftext(c, "área: 2 → 3", 300, 400, 40, "black", INK, ab, align="left")
        ftext(c, "embaixo: ÷ 1,5", 1000, 400, 40, "black", BLUE, ab, align="left")
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0:
        ftext(c, "6 × 2 = 12      12 ÷ 1,5 = 8 Ω", 660, 540, 46, "black", PURPLE, acc)
        text(c, "o mesmo resultado ✓", 660, 610, 30, "black", GREEN, acc)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1180, 470, 500, 250, "ATALHO", ["cada mudança vira", "um FATOR:", "multiplique os fatores"], ad, 32)


# ======================================================================
# bloco C — várias mudanças: efeitos se multiplicam
# ======================================================================

def b_efeitos(c, t, C, B):
    head_seq(c, t, C, [("11", "VÁRIAS MUDANÇAS", "UMA DE CADA VEZ", PURPLE), ("12", "EFEITOS", "SE MULTIPLICAM", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        aa = ep(t, C["11.a"], 0.5)
        expr(c, "y = k · a/b", 500, 330, 90, aa, cores={2: PURPLE})
        if aa > 0:
            ftext(c, "a × 2     b × 3", 1300, 330, 48, "black", INK, aa)
        ab = ep(t, C["11.b"], 0.5)
        if ab > 0:
            ftext(c, "a em cima: × 2", 500, 490, 40, "black", GREEN, ab)
            ftext(c, "b embaixo: ÷ 3", 1300, 490, 40, "black", BLUE, ep(t, C["11.b"] + 1.8, 0.4))
        acc = ep(t, C["11.c"], 0.5)
        if acc > 0:
            expr(c, "y × 2/3", W / 2, 620, 72, acc, cores={1: PURPLE})
        ad = ep(t, C["11.d"], 0.5)
        if ad > 0:
            expr(c, "12 × 2/3 = 8", W / 2, 760, 56, ad, cores={4: GREEN})
        return
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        regra(c, "os efeitos se MULTIPLICAM, não se somam", W / 2, 290, aa, 40)
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        ftext(c, "× 2  e  ÷ 3", 560, 470, 60, "black", GREEN, ab)
        ftext(c, "≠  2 − 3", 1340, 470, 60, "black", RED, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        ftext(c, "receita × 2  →  depois ÷ 3 potes", W / 2, 660, 44, "black", PURPLE, acc)
        text(c, "uma ação depois da outra, sobre o mesmo número", W / 2, 730, 30, "bold", INK2, acc)


# ======================================================================
# bloco D — as fórmulas lidas em voz alta
# ======================================================================

def _linha_formula(c, y, s, txt, a, col_t=INK2, cores=None):
    expr(c, s, 520, y, 64, a, cores=cores if cores is not None else mono(s, INK))
    ftext(c, txt, 900, y + 10, 34, "black", col_t, a, align="left")


def b_formulas(c, t, C, B):
    head_seq(c, t, C, [("13", "FÓRMULAS EM VOZ ALTA", "VELOCIDADE", PURPLE), ("14", "FÓRMULAS EM VOZ ALTA", "TUDO EM CIMA", PURPLE),
                       ("16", "FÓRMULAS EM VOZ ALTA", "DENSIDADE E ENERGIA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14", "16"])
    if sid == "13":
        aa = ep(t, C["13.a"], 0.5)
        expr(c, "v = d/t", 560, 440, 130, aa, cores={2: INK})
        ab = ep(t, C["13.b"], 0.5)
        if ab > 0:
            ftext(c, "d em cima → DIRETA", 1060, 360, 44, "black", GREEN, ab, align="left")
            text(c, "mais distância, mesmo tempo: mais velocidade", 1060, 410, 26, "bold", INK2, ab, align="left")
        acc = ep(t, C["13.c"], 0.5)
        if acc > 0:
            ftext(c, "t embaixo → INVERSA", 1060, 540, 44, "black", BLUE, acc, align="left")
            text(c, "mais tempo, mesma distância: menos velocidade", 1060, 590, 26, "bold", INK2, acc, align="left")
        return
    if sid == "14":
        aa = ep(t, C["14.a"], 0.5)
        _linha_formula(c, 330, "F = m · a", "força: DIRETA à massa e à aceleração", aa, GREEN)
        ab = ep(t, C["14.b"], 0.5)
        _linha_formula(c, 530, "P = U · i", "potência: DIRETA à tensão e à corrente", ab, GREEN)
        if ab > 0:
            text(c, "U = tensão (o empurrão da tomada) · i = corrente (quanto passa)", 900, 590, 24, "bold", INK2, ab,
                 align="left")
        acc = ep(t, C["14.c"], 0.5)
        if acc > 0:
            regra(c, "tudo em cima = tudo direto", W / 2, 740, acc, 36)
        return
    aa = ep(t, C["16.a"], 0.5)
    _linha_formula(c, 330, "d = m/V", "mesmo material: m e V DIRETAS; o k é a densidade", aa, GREEN)
    ab = ep(t, C["16.b"], 0.5)
    _linha_formula(c, 560, "E = m·v^2/2", "energia do movimento (cinética)", ab, INK2)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        selo(c, 1350, 680, acc, "TEM QUADRADO: PRÓXIMO EPISÓDIO", AMBER, -3, 28)


def b_boyle(c, t, C, B):
    frame(c, t, B["start"], "QUÍMICA · LEI DE BOYLE", "P · V = k", PURPLE)
    aa = ep(t, C["15.a"], 0.5)
    frac = 1.0 - 0.4 * ep(t, C["15.b"], 1.6)
    seringa(c, 280, 280, frac, aa, rot_v="volume do gás")
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        boxed(c, 300, 520, 640, 120, BLUE, ab, 0.08)
        text(c, "PRESSÃO = força apertando", 620, 572, 30, "black", BLUE, ab)
        text(c, "cada pedacinho do gás", 620, 615, 26, "bold", INK2, ab)
        ftext(c, "P ↑", 1380, 330, 60, "black", RED, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        ftext(c, "V ↓", 1580, 330, 60, "black", BLUE, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        expr(c, "P · V = k", 1380, 560, 80, ad, cores={4: PURPLE})
        text(c, "temperatura constante", 1380, 640, 26, "bold", INK2, ad)
        regra(c, "produto constante → INVERSA", W / 2, 760, ad, 36)


# ======================================================================
# bloco E — leitura rápida
# ======================================================================

def b_leitura(c, t, C, B):
    frame(c, t, B["start"], "PERCEBEU O PADRÃO?", "A LEITURA RÁPIDA", GREEN)
    aa, ab = ep(t, C["17.a"], 0.5), ep(t, C["17.b"], 0.5)
    andares(c, 820, 440, max(aa, ab), cima=[("DIRETO", aa)], baixo=[("INVERSO", ab)], pre=None, w=560, size=48, lado=False)
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        K.atalho(c, 300, 650, 1320, 140, "SEM DECORAR NADA", ["grandeza dobrou? olhe o andar dela"], acc, 34)
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        selo(c, 1560, 330, ad, "É ISSO QUE O ENEM PERGUNTA", BLUE, -6, 26)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "PAUSE E PENSE", GREEN), ("19", "VAMOS CONFERIR", "UM ANDAR DE CADA VEZ", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["18.a"], 0.5)
    expr(c, "y = k · a/b", 560, 340, 100, aa, cores={2: PURPLE})
    ab = ep(t, C["18.b"], 0.5)
    if ab > 0:
        ftext(c, "a × 3", 1240, 300, 56, "black", INK, ab)
        ftext(c, "b × 2", 1240, 400, 56, "black", INK, ab)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0 and t < C["19"]:
        ftext(c, "y × ?", W / 2, 590, 72, "black", PURPLE, acc)
    pause_timer(c, t, C["18.end"] - 1.9, W / 2, 740)
    if t >= C["19"]:
        a1 = ep(t, C["19.a"], 0.4)
        ftext(c, "em cima: × 3", 1500, 300, 40, "black", GREEN, a1, align="left")
        a2 = ep(t, C["19.b"], 0.4)
        ftext(c, "embaixo: ÷ 2", 1500, 400, 40, "black", BLUE, a2, align="left")
        a3 = ep(t, C["19.c"], 0.4)
        if a3 > 0:
            expr(c, "y × 3/2", 760, 620, 80, a3, cores={1: PURPLE})
            ftext(c, "= 1,5 vez maior", 1200, 630, 52, "black", GREEN, a3, align="left")


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Direto em cima, inverso embaixo.", "Várias mudanças? Multiplique os efeitos.",
          "Toda fórmula é uma frase sobre proporção."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "31"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 290 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Somar os efeitos em vez de multiplicar", "são várias mudanças, e somar parece juntar tudo",
          "cada mudança age sobre a anterior: × um fator, ÷ o outro"),
         ("Pôr a grandeza inversa no numerador", "a gente escreve na ordem em que lê o enunciado",
          "o que DIMINUI o resultado vai EMBAIXO. Sempre."),
         ("Boyle: mais pressão, mais volume", "em muita fórmula os números crescem juntos",
          "comprimir um gás diminui o espaço dele: mais pressão, MENOS volume")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# Questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS7 = [("A", "5 Ω", "achou que os efeitos se anulam", RED), ("B", "7,5 Ω", "somou: 5 × (3 − 1,5)", RED),
         ("C", "10 Ω", "", GREEN), ("D", "15 Ω", "esqueceu a área", RED), ("E", "45 Ω", "área em cima: 5 × 3 × 3", RED)]


def b_q7(c, t, C, B):
    head_seq(c, t, C, [("24", "QUESTÃO · PROPORÇÃO COMPOSTA", "PAUSE E TENTE", BLUE), ("25", "1º CAMINHO", "ACHANDO O k", PURPLE),
                       ("26", "2º CAMINHO", "PELOS EFEITOS", GREEN), ("27", "E AS OUTRAS?", "CADA ERRO, UMA LETRA", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    _enunciado(c, [("A resistência elétrica de um fio é diretamente proporcional ao seu comprimento e inversamente "
                    "proporcional à área de sua seção transversal. Um fio de 10 m de comprimento e 2 mm² de seção tem "
                    "resistência de 5 Ω.", INK),
                   ("Outro fio, do mesmo material, com 30 m de comprimento e 3 mm² de seção, terá resistência de", BLUE)],
               a0, 230, 27, 720)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"27.x{L.lower()}"] for L in "ABDE"}
    if t >= C["24.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS7, 1000, 230, 680, 40, C["25.ok"], "C", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["24.end"] - 1.9, 470, 700)
    if C["25"] <= t < C["27"]:
        ra = ep(t, C["25"], 0.4)
        rrect(c, 170, 530, 760, 290, 18, "#FFFFFF", ra, shadow=True)
        if t < C["26"]:
            expr(c, "R = k · L/A", 550, 590, 44, ep(t, C["25.a"], 0.4), cores={2: PURPLE})
            expr(c, "5 = k · 10/2 = 5k", 550, 680, 40, ep(t, C["25.b"], 0.4), cores=mono("5 = k · 10/2 = 5k", INK))
            ftext(c, "k = 1  →  30 ÷ 3 = 10 Ω", 550, 775, 38, "black", GREEN, ep(t, C["25.c"], 0.4))
        else:
            ftext(c, "L: 10 → 30   em cima: × 3", 550, 590, 34, "black", GREEN, ep(t, C["26.a"], 0.4))
            ftext(c, "A: 2 → 3   embaixo: ÷ 1,5", 550, 650, 34, "black", BLUE, ep(t, C["26.b"], 0.4))
            ftext(c, "5 × 3 = 15  ÷ 1,5 = 10 Ω", 550, 720, 38, "black", PURPLE, ep(t, C["26.c"], 0.4))
            ftext(c, "mais comprido, pouco mais grosso: sobe ✓", 550, 785, 24, "black", AMBER, ep(t, C["26.d"], 0.4))


ALTS9 = [("A", "2 litros", "6 ÷ nova pressão", RED), ("B", "3 litros", "6 ÷ pressão antiga", RED),
         ("C", "4 litros", "", GREEN), ("D", "9 litros", "tratou como direta", RED), ("E", "12 litros", "parou no k", RED)]


def b_q9(c, t, C, B):
    head_seq(c, t, C, [("28", "QUESTÃO · LEI DE BOYLE", "PAUSE E TENTE", BLUE), ("29", "VAMOS RESOLVER", "BOM SENSO PRIMEIRO", GREEN),
                       ("30", "E AS OUTRAS?", "CADA ERRO, UMA LETRA", RED)])
    card(c, *CARD_R)
    a0 = ep(t, C["28.a"], 0.4)
    _enunciado(c, [("A uma temperatura constante, o volume ocupado por certa massa de gás é inversamente proporcional à "
                    "pressão exercida sobre ele. Um gás ocupa 6 litros sob pressão de 2 atm.", INK),
                   ("Ao ser comprimido até a pressão de 3 atm, mantida a temperatura, esse gás passará a ocupar", BLUE)],
               a0, 230, 28, 720)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"28.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"30.x{L.lower()}"] for L in "ABDE"}
    if t >= C["28.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS9, 1000, 230, 680, 40, C["29.ok"], "C", cues_in, cues_x, gap=22)
    pause_timer(c, t, C["28.end"] - 1.9, 470, 700)
    if C["29"] <= t < C["30"]:
        ra = ep(t, C["29"], 0.4)
        rrect(c, 170, 500, 760, 320, 18, "#FFFFFF", ra, shadow=True)
        ftext(c, "comprimiu → V tem que DIMINUIR", 550, 550, 32, "black", AMBER, ep(t, C["29.a"], 0.4))
        ftext(c, "D e E caem: 9 e 12 > 6", 550, 600, 28, "black", RED, ep(t, C["29.b"], 0.4))
        ftext(c, "k = 2 × 6 = 12", 550, 670, 38, "black", PURPLE, ep(t, C["29.c"], 0.4))
        ftext(c, "3 × V = 12  →  V = 4 L", 550, 735, 38, "black", GREEN, ep(t, C["29.d"], 0.4))
        ftext(c, "efeitos: 6 ÷ 1,5 = 4 ✓", 550, 795, 28, "black", GREEN, ep(t, C["29.e"], 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "QUANDO DOBRAR NÃO DOBRA", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    items = [("área", "A = L^2", 460), ("energia", "E = m·v^2/2", 960), ("luz", "I = k/d^2", 1460)]
    for k, (nm, s, x) in enumerate(items):
        a = aa * ep(t, C["32.a"] + 0.6 * k, 0.4)
        if a <= 0:
            continue
        card(c, x - 220, 260, 440, 300, a)
        text(c, nm.upper(), x, 320, 30, "black", INK2, a)
        expr(c, s, x, 440, 64, a, cores=mono(s, PURPLE))
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        regra(c, "tem QUADRADO: dobrar NÃO dobra", W / 2, 660, ab, 38)
    pill(c, "ep. 5 · quadrado, cubo e inverso do quadrado", W / 2, 790, PURPLE, size=30, a=ep(t, C["32.c"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Qual fórmula você vai ler primeiro?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, mangueira=b_mangueira, guia=b_guia, fio=b_fio,
              efeitos=b_efeitos, formulas=b_formulas, boyle=b_boyle, leitura=b_leitura, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q7=b_q7, q9=b_q9, ponte=b_ponte, cta=b_cta)
