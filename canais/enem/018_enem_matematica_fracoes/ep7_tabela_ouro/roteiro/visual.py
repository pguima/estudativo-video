"""Visual — Frações, Decimais e Dízimas, Episódio 7: A tabela que vale ouro (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (pizza, expr com frações empilhadas, alternativas, erro_cards...).
Peças deste episódio: a tabela construída uma família por vez (pizza ou grade de 100 ao lado de cada linha), as três
CARTAS dos idiomas (fração · decimal · porcentagem) que viram no jogo, a vírgula que anda duas casas e a tabela completa
com o selo "tire um print".
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
_s = importlib.util.spec_from_file_location("comum018", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
fr, expr, expr_w, pizza = K.fr, K.expr, K.expr_w, K.pizza
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_fracoes_ep7_tabela_ouro.mp4"
CARD_R = K.CARD_R
GRADE_ON = "#2BA6A0"     # quadradinhos da grade de 100
CARTA_COSTAS = "#3D5AFE"

# as cinco famílias da tabela: (nome, cor, linhas); linha = (num, den, decimal, porcentagem, desenho)
FAMILIAS = [
    ("METADES E QUARTOS", BLUE, [("1", "2", "0,5", "50%", ("pz", 2, 1)), ("1", "4", "0,25", "25%", ("pz", 4, 1)),
                                 ("3", "4", "0,75", "75%", ("pz", 4, 3))]),
    ("TERÇOS E SEXTOS", AMBER, [("1", "3", "0,333…", "≈ 33,3%", ("pz", 3, 1)), ("2", "3", "0,666…", "≈ 66,7%", ("pz", 3, 2)),
                                ("1", "6", "0,1666…", "≈ 16,7%", ("pz", 6, 1))]),
    ("QUINTOS", PURPLE, [("1", "5", "0,2", "20%", ("pz", 5, 1)), ("2", "5", "0,4", "40%", ("pz", 5, 2)),
                         ("3", "5", "0,6", "60%", ("pz", 5, 3))]),
    ("OITAVOS", GREEN, [("1", "8", "0,125", "12,5%", ("pz", 8, 1)), ("3", "8", "0,375", "37,5%", ("pz", 8, 3)),
                        ("5", "8", "0,625", "62,5%", ("pz", 8, 5)), ("7", "8", "0,875", "87,5%", ("pz", 8, 7))]),
    ("DÉCIMOS, VIGÉSIMOS E CENTÉSIMOS", RED, [("1", "10", "0,1", "10%", ("gr", 10)), ("1", "20", "0,05", "5%", ("gr", 5)),
                                              ("1", "100", "0,01", "1%", ("gr", 1))]),
]


# ======================================================================
# peças do episódio
# ======================================================================

def grade100(c, x, y, s, n, a, col=GRADE_ON, u=1.0):
    """grade 10 × 10 (lado s) com os n primeiros quadradinhos pintados (u = progresso da pintura)."""
    if a <= 0:
        return
    g = max(1.0, s * 0.012)
    cw = (s - 9 * g) / 10
    rrect(c, x - 6, y - 6, s + 12, s + 12, 8, "#FFFFFF", a, shadow=True)
    lit = int(round(n * clamp(u)))
    for i in range(100):
        r_, k = divmod(i, 10)
        rrect(c, x + k * (cw + g), y + r_ * (cw + g), cw, cw, max(1, cw * 0.18), col if i < lit else "#E7E3DA", a)


def desenho(c, d, cx, cy, size, a):
    if d[0] == "pz":
        pizza(c, cx, cy, size, d[1], d[2], a, pull=0.3, sombra=False)
    else:
        grade100(c, cx - size, cy - size, size * 2, d[1], a)


def linha_tab(c, t, row, y, t0, xs, sizes=(54, 52, 52), pic=50, a=1.0):
    """uma linha da tabela: desenho · fração = decimal = porcentagem, entrando em sequência a partir de t0."""
    num, den, dec, pct, d = row
    xp, xf, xd, xc = xs
    a1, a2, a3 = (a * ep(t, t0 + k, 0.4) for k in (0, 0.9, 1.8))
    desenho(c, d, xp, y, pic, a1)
    fr(c, num, den, xf, y - sizes[0] * 0.38, sizes[0], INK, a1)
    fmid(c, "=", (xf + xd) / 2 - 20, y, sizes[1], "black", LIGHT, a2)
    fmid(c, dec, xd, y, sizes[1], "black", INK, a2)
    fmid(c, "=", (xd + xc) / 2 + 10, y, sizes[1], "black", LIGHT, a3)
    fmid(c, pct, xc, y, sizes[2], "black", GREEN if "≈" not in pct else AMBER, a3)


FAM_XS = (300, 520, 790, 1110)


def cabecalho(c, a, xs=FAM_XS, y=205):
    for x, s in zip(xs[1:], ("FRAÇÃO", "DECIMAL", "PORCENTAGEM")):
        text(c, s, x, y, 24, "black", GRAY, a)


def painel(c, x, y, w, h, col, titulo, linhas, a, size=34):
    """caixa lateral (padrão / atalho / aviso). linhas = [(texto, alfa)]; texto com 'a/b' isolado vira expr."""
    if a <= 0:
        return
    boxed(c, x, y, w, h, col, a, 0.08)
    pill(c, titulo, x + w / 2, y, col, size=24, a=a, anchor="center", bounds=(0, 1920))
    yy = y + 80
    for s, al in linhas:
        if any("/" in tok for tok in s.split()):
            expr(c, s, x + w / 2, yy + 6, size, a * al, cores={})
            yy += size * 2.3
        else:
            for ln in K.wrap(s, "black", size, w - 40):
                fmid(c, ln, x + w / 2, yy, size, "black", INK if col != GREEN else mix(GREEN, INK, 0.35), a * al)
                yy += size * 1.3
            yy += 12


def familia(c, t, C, k, cues, ys, pic=50):
    """as linhas da família k, cada uma entrando no seu cue."""
    rows = FAMILIAS[k][2]
    for row, cue, y in zip(rows, cues, ys):
        if cue is None:
            continue
        linha_tab(c, t, row, y, C[cue], FAM_XS, pic=pic)


def carta(c, cx, cy, w, h, titulo, val, virada, a, col=BLUE):
    """carta de idioma: virada = 0 (costas) → 1 (frente), com giro horizontal."""
    if a <= 0:
        return
    u = clamp(virada)
    sx = abs(math.cos(math.pi * u))
    sx = max(sx, 0.02)
    c.save(); c.translate(cx, cy); c.scale(sx, 1)
    if u < 0.5:
        rrect(c, -w / 2, -h / 2, w, h, 26, CARTA_COSTAS, a, shadow=True)
        rrect(c, -w / 2 + 16, -h / 2 + 16, w - 32, h - 32, 18, mix(CARTA_COSTAS, "#FFFFFF", 0.18), a)
        text_mid(c, "?", 0, 0, 110, "black", "#FFFFFF", a)
    else:
        rrect(c, -w / 2, -h / 2, w, h, 26, "#FFFFFF", a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 26, 26), paint(col, a, stroke=5))
        text(c, titulo, 0, -h / 2 + 44, 24, "black", col, a)
        if "/" in val:
            n_, d_ = val.split("/")
            fr(c, n_, d_, 0, 4, 72, INK, a)
        else:
            fmid(c, val, 0, 20, 78 if len(val) < 6 else 64, "black", INK, a)
    c.restore()


IDIOMAS = (("FRAÇÃO", BLUE), ("DECIMAL", PURPLE), ("PORCENTAGEM", GREEN))


def tres_cartas(c, vals, viradas, a, y=470, w=360, h=330, gap=420):
    for k, ((tit, col), v, vr) in enumerate(zip(IDIOMAS, vals, viradas)):
        carta(c, W / 2 + (k - 1) * gap, y, w, h, tit, v, vr, a, col)


def virgula_anda(c, cx, cy, digs, de, para_, u, a, size=90, col=None, suf=""):
    """algarismos espaçados; a vírgula pula da posição 'de' para 'para_' (posição = nº de algarismos à esquerda).
    Zeros à esquerda que sobram somem no fim."""
    if a <= 0:
        return
    col = col or INK
    step = size * 0.72
    n = len(digs)
    x0 = cx - (n - 1) * step / 2
    pos = lerp(de, para_, ease_io(clamp(u)))
    lead = 0
    while lead < para_ - 1 and digs[lead] == "0":
        lead += 1
    for i, ch in enumerate(digs):
        al = a * (1 - ep(u, 0.85, 0.15)) if i < lead else a
        fmid(c, ch, x0 + i * step, cy, size, "black", col, al)
    xv = x0 + (pos - 0.5) * step
    hop = -size * 0.5 * math.sin(math.pi * clamp(u)) if 0 < u < 1 else 0
    fmid(c, ",", xv, cy + size * 0.25 + hop, size, "black", RED, a * (1 - ep(u, 0.8, 0.2)))
    if suf:
        fmid(c, suf, x0 + (n - 1) * step + size * 0.75, cy, size, "black", GREEN, a * ep(u, 0.9, 0.1))


def bateria(c, x, y, w, h, frac, a):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(INK2, a, stroke=6))
    rrect(c, x + w + 4, y + h * 0.3, 16, h * 0.4, 5, INK2, a)
    rrect(c, x + 12, y + 12, (w - 24) * frac, h - 24, 10, AMBER, a)


# ======================================================================
# a tabela completa (também usada em miniatura no gancho)
# ======================================================================

def tabela_completa(c, a, t=None, t0=None):
    """as 16 linhas em duas colunas, agrupadas por família (faixa colorida à esquerda)."""
    if a <= 0:
        return
    card(c, *CARD_R, a=a)
    halves = (((0, 1, 2), (230, 380, 590, 810)), ((3, 4), (1030, 1190, 1400, 1620)))
    for fams, (xb, xf, xd, xc) in halves:
        for x, s in ((xf, "FRAÇÃO"), (xd, "DECIMAL"), (xc, "PORCENTAGEM")):
            text(c, s, x, 200, 22, "black", GRAY, a)
        y = 250
        for k in fams:
            nome, col, rows = FAMILIAS[k]
            y_ini = y
            for row in rows:
                num, den, dec, pct, _ = row
                fr(c, num, den, xf, y - 2, 28, INK, a)
                fmid(c, dec, xd, y + 10, 32, "black", INK, a)
                fmid(c, pct, xc, y + 10, 32, "black", GREEN if "≈" not in pct else AMBER, a)
                y += 64
            rrect(c, xb - 16, y_ini - 30, 10, y - y_ini - 6, 5, col, a)
            y += 10
    line(c, W / 2 + 50, 190, W / 2 + 50, 810, LINE, a, 3)
    text(c, "≈ = aproximado (terços e sextos são dízimas)", 1395, 790, 24, "bold", AMBER, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "A TABELA QUE VALE OURO", AMBER)
    aa = ep(t, C["01.a"], 0.5)
    fmid(c, "se você só pudesse decorar UMA coisa...", W / 2, 205, 44, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.6)
    if ab > 0:
        c.save(); c.translate(W / 2, 520); s = 0.52 + 0.04 * ep(t, C["01.b"], 1.2); c.scale(s, s); c.translate(-W / 2, -495)
        tabela_completa(c, ab)
        c.restore()
    for k, s_ in enumerate(("porcentagem", "probabilidade", "estatística")):
        a = ep(t, C["01.c"] + 0.5 * k, 0.4)
        chip(c, s_, W / 2 + (k - 1) * 420, 830, GREEN, a, 34, w=360)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "trocar de idioma DE CABEÇA", "fração ⇄ decimal ⇄ porcentagem"), ("02.b", "sem decorar tudo",
                                                                                      "usando padrões")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 330 + j * 200 + d
        check_icon(c, 260, y - 14, 34, a, GREEN)
        text(c, s, 320, y, 52, "black", INK, a, align="left")
        ftext(c, sub, 320, y + 58, 34, "bold", GRAY, a, align="left")
    aa = ep(t, C["02.a"], 0.5)
    for k, (v, col) in enumerate((("1/2", BLUE), ("0,5", PURPLE), ("50%", GREEN))):
        a = aa * ep(t, C["02.a"] + 0.4 * k, 0.4)
        x = 1260 + k * 170
        rrect(c, x - 72, 380, 144, 190, 18, "#FFFFFF", a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 72, 380, 144, 190), 18, 18), paint(col, a, stroke=4))
        if "/" in v:
            fr(c, "1", "2", x, 455, 54, INK, a)
        else:
            fmid(c, v, x, 475, 46, "black", INK, a)


# ======================================================================
# concreto, idiomas, por cento, pré-requisitos
# ======================================================================

def b_concreto(c, t, C, B):
    frame(c, t, B["start"], "VOCÊ JÁ USA ISSO", "TODO DIA", BLUE)
    itens = [("03.a", "metade de uma pizza"), ("03.b", "meio quilo"), ("03.c", "50% de desconto"), ("03.d", "0,5 na calculadora")]
    for k, (cue, s) in enumerate(itens):
        a, d = rise(t, C[cue])
        chip(c, s, 520, 250 + k * 118 + d, BLUE, a, 38, w=600)
    ae = ep(t, C["03.e"], 0.5)
    for k in range(4):
        arrow(c, 840, 250 + k * 118, 1010, 425, LIGHT, ae, 4, 14, progress=ae)
    pizza(c, 1110, 425, 80, 2, 1, ae, pull=0.4)
    text(c, "o MESMO número", 1110, 560, 34, "black", GREEN, ae)
    af = ep(t, C["03.f"], 0.5)
    bateria(c, 1330, 360, 260, 120, 0.25 * ep(t, C["03.f"] + 0.3, 0.8), af)
    fmid(c, "25%", 1460, 420, 40, "black", INK, af)
    expr(c, "= 1/4 da carga", 1460, 560, 40, ep(t, C["03.f"] + 1.8, 0.4), cores={1: AMBER})


def b_idiomas(c, t, C, B):
    frame(c, t, B["start"], "A ANALOGIA", "TRÊS IDIOMAS DO MESMO NÚMERO", PURPLE)
    aa = ep(t, C["04.a"], 0.5)
    chip(c, "meia dúzia", 760, 225, GRAY, aa, 34, w=300)
    fmid(c, "=", W / 2, 225, 44, "black", LIGHT, aa)
    chip(c, "seis", 1160, 225, GRAY, aa, 34, w=300)
    ab = ep(t, C["04.b"], 0.5)
    vr = [ep(t, C["04.b"] + 0.5 * k, 0.6) for k in range(3)]
    tres_cartas(c, ("1/2", "0,5", "50%"), vr, ab, y=450, w=320, h=270)
    acc = ep(t, C["04.c"], 0.5)
    ad = ep(t, C["04.d"], 0.5)
    text(c, "o ENEM troca de idioma no meio do enunciado", W / 2, 655, 34, "black", AMBER, acc * (1 - ad))
    text(c, "fluente nos três = ganha tempo", W / 2, 655, 36, "black", GREEN, ad)
    ae = ep(t, C["04.e"], 0.5)
    pill(c, "CONVERSÃO = traduzir de um idioma para outro", W / 2, 760, BLUE, size=32, a=ae, anchor="center",
         bounds=(0, 1920))


def b_porcento(c, t, C, B):
    frame(c, t, B["start"], "O QUE QUER DIZER", "“POR CENTO”?", BLUE)
    a0 = ep(t, C["05.t"], 0.5)
    grade100(c, 300, 230, 440, 50, a0, u=ep(t, C["05.a"], 1.4))
    text(c, "50 de cada 100", 520, 740, 34, "black", GRADE_ON, ep(t, C["05.a"] + 1.2, 0.4))
    fmid(c, "%", 1260, 300, 130, "black", BLUE, a0)
    fmid(c, "= “de cada 100”", 1260, 440, 52, "black", INK, ep(t, C["05.a"], 0.5))
    ac = ep(t, C["05.c"], 0.5)
    para(c, "PORCENTAGEM = fração com o 100 embaixo", 940, 540, 34, "black", BLUE, ac, 660, align="left")
    expr(c, "50% = 50/100", 1260, 680, 60, ep(t, C["05.d"], 0.5), cores={2: BLUE})


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        pill(c, "EPISÓDIO 1", 560, 230, GRAY, size=24, a=aa, anchor="center", bounds=(0, 1920))
        fmid(c, "FRAÇÃO = DIVISÃO", 560, 320, 50, "black", PURPLE, aa)
        expr(c, "1/2 = 1 ÷ 2 = 0,5", 560, 500, 66, ep(t, C["06.a"] + 0.8, 0.4), cores={4: GREEN})
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        line(c, W / 2, 220, W / 2, 780, LINE, ab, 3)
        pill(c, "EPISÓDIO 5", 1360, 230, GRAY, size=24, a=ab, anchor="center", bounds=(0, 1920))
        fmid(c, "× 100: VÍRGULA 2 CASAS →", 1360, 320, 44, "black", PURPLE, ab)
        virgula_anda(c, 1360, 500, "050", 1, 3, ep(t, C["06.c"], 1.0), ab, 100, suf="")
        fmid(c, "= 50%", 1360, 680, 60, "black", GREEN, ep(t, C["06.c"] + 1.4, 0.4))


# ======================================================================
# as famílias
# ======================================================================

def b_fam_quartos(c, t, C, B):
    head_seq(c, t, C, [("07", "FAMÍLIA 1 DE 5", "METADES E QUARTOS", BLUE), ("08", "FAMÍLIA 1 · O PADRÃO", "CADA QUARTO = 25%", GREEN)])
    card(c, *CARD_R)
    cabecalho(c, ep(t, C["07.t"], 0.5))
    familia(c, t, C, 0, ["07.a", "07.b", "07.c"], [310, 470, 630])
    aa = ep(t, C["08.a"], 0.5)
    painel(c, 1290, 250, 440, 330, GREEN, "ATALHO", [("cada quarto = 25%", 1), ("3 × 25% = 75%", ep(t, C["08.a"] + 1.2, 0.4))],
           aa, 34)
    ab = ep(t, C["08.b"], 0.5)
    expr(c, "1/4 + 3/4 = 1", 1510, 460, 40, ab)
    ac = ep(t, C["08.c"], 0.5)
    pill(c, "COMPLEMENTO = o que falta para 100% · 25% + 75% = 100%", W / 2, 780, BLUE, size=28, a=ac, anchor="center",
         bounds=(0, 1920))


def b_fam_tercos(c, t, C, B):
    head_seq(c, t, C, [("09", "FAMÍLIA 2 DE 5", "TERÇOS E SEXTOS", AMBER), ("10", "FAMÍLIA 2 · O ATALHO", "DOBRO E METADE", GREEN)])
    card(c, *CARD_R)
    cabecalho(c, ep(t, C["09.t"], 0.5))
    familia(c, t, C, 1, ["09.a", "09.d", "10.b"], [310, 470, 630])
    s10 = ep(t, C["10"], 0.4)
    ab = ep(t, C["09.b"], 0.5) * (1 - s10)
    painel(c, 1290, 250, 440, 160, BLUE, "DÍZIMA", [("repete sem fim: 0,333…", 1)], ab, 30)
    ac = ep(t, C["09.c"], 0.5) * (1 - s10)
    painel(c, 1290, 470, 440, 200, AMBER, "ATENÇÃO", [("≈ quer dizer", 1), ("APROXIMADO", 1)], ac, 32)
    aa = ep(t, C["10.a"], 0.5)
    painel(c, 1290, 250, 440, 420, GREEN, "ATALHO", [("2/3 = DOBRO de 1/3", 1), ("1/6 = METADE de 1/3", ep(t, C["10.b"], 0.4)),
                                                    ("33,3 ÷ 2 ≈ 16,7", ep(t, C["10.b"] + 1.5, 0.4))], aa, 30)
    regra(c, "viu “cerca de” na alternativa? pense em terços e sextos", W / 2, 780, ep(t, C["10.c"], 0.5), 30, AMBER)


def b_fam_quintos(c, t, C, B):
    frame(c, t, B["start"], "FAMÍLIA 3 DE 5", "QUINTOS", PURPLE)
    cabecalho(c, ep(t, C["11.t"], 0.5))
    familia(c, t, C, 2, ["11.a", "11.c", "11.d"], [310, 470, 630])
    ab = ep(t, C["11.b"], 0.5)
    painel(c, 1290, 250, 440, 440, GREEN, "ATALHO", [("5 quintos = 100%", 1), ("100 ÷ 5 = 20", ep(t, C["11.b"] + 1.0, 0.4)),
                                                    ("cada quinto = 20%", ep(t, C["11.b"] + 2.0, 0.4))], ab, 34)
    regra(c, "é só contar de 20 em 20", W / 2, 780, ep(t, C["11.d"] + 1.2, 0.5), 32, GREEN)


def b_fam_oitavos(c, t, C, B):
    frame(c, t, B["start"], "FAMÍLIA 4 DE 5 · A QUERIDINHA DO ENEM", "OITAVOS", GREEN)
    cabecalho(c, ep(t, C["12.t"], 0.5), y=195)
    familia(c, t, C, 3, ["12.a", "12.c", "12.d", "12.e"], [275, 420, 565, 710], pic=46)
    aa = ep(t, C["12.a"] + 1.0, 0.5)
    painel(c, 1290, 230, 440, 200, BLUE, "1/8 = METADE DE 1/4", [("25 ÷ 2 = 12,5", 1)], aa, 36)
    ab = ep(t, C["12.b"], 0.5)
    painel(c, 1290, 490, 440, 300, GREEN, "ATALHO", [("cada oitavo", 1), ("= 12,5%", 1)], ab, 44)


def b_fam_decimos(c, t, C, B):
    frame(c, t, B["start"], "FAMÍLIA 5 DE 5", "DÉCIMOS, VIGÉSIMOS E CENTÉSIMOS", RED)
    cabecalho(c, ep(t, C["13.t"], 0.5))
    familia(c, t, C, 4, ["13.a", "13.b", "13.c"], [310, 470, 630], pic=58)
    ab = ep(t, C["13.b"] + 0.6, 0.5)
    painel(c, 1290, 250, 440, 170, GREEN, "ATALHO", [("1/20 = METADE de 1/10", 1)], ab, 30)
    ad = ep(t, C["13.d"], 0.5)
    painel(c, 1290, 480, 440, 260, BLUE, "1/100 = 1%", [("literalmente:", 1), ("1 de cada 100", 1)], ad, 38)


# ======================================================================
# as quatro conversões
# ======================================================================

def b_conv(c, t, C, B):
    head_seq(c, t, C, [("14", "TRADUÇÃO 1 DE 4", "FRAÇÃO → DECIMAL", PURPLE), ("15", "TRADUÇÃO 2 DE 4", "DECIMAL → PORCENTAGEM", PURPLE),
                       ("16", "TRADUÇÃO 3 DE 4", "PORCENTAGEM → FRAÇÃO", PURPLE),
                       ("17", "TRADUÇÃO 4 DE 4", "DECIMAL EXATO → FRAÇÃO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["14", "15", "16", "17"])
    q = lambda x: C[f"{sid}.{x}"]
    if sid == "14":
        regra(c, "divida o de cima pelo de baixo", W / 2, 245, ep(t, q("a"), 0.5), 38)
        expr(c, "7/20 = 7 ÷ 20 = 0,35", W / 2, 420, 76, ep(t, q("b"), 0.5), cores={6: GREEN})
        ac = ep(t, q("c"), 0.5)
        if ac > 0:
            boxed(c, 360, 560, 1200, 240, GREEN, ac, 0.06)
            pill(c, "ATALHO: faça o de baixo virar 100", W / 2, 560, GREEN, size=28, a=ac, anchor="center", bounds=(0, 1920))
            expr(c, "7/20 = 35/100 = 0,35", W / 2, 680, 64, ac, cores={2: GREEN, 4: GREEN})
            text(c, "× 5 em cima e embaixo", W / 2, 775, 26, "black", GREEN, ac)
    elif sid == "15":
        regra(c, "multiplique por 100", W / 2, 245, ep(t, q("t"), 0.5), 38)
        expr(c, "0,35 × 100 = 35%", W / 2, 420, 76, ep(t, q("a"), 0.5), cores={4: GREEN})
        ab = ep(t, q("b"), 0.5)
        if ab > 0:
            boxed(c, 360, 560, 1200, 240, GREEN, ab, 0.06)
            pill(c, "ATALHO: vírgula 2 casas para a direita", W / 2, 560, GREEN, size=28, a=ab, anchor="center",
                 bounds=(0, 1920))
            virgula_anda(c, W / 2 - 40, 690, "035", 1, 3, ep(t, q("b") + 1.0, 1.0), ab, 90, suf="%")
    elif sid == "16":
        regra(c, "ponha sobre 100 e simplifique", W / 2, 245, ep(t, q("t"), 0.5), 38)
        expr(c, "37,5% = 37,5/100", 640, 420, 66, ep(t, q("a"), 0.5))
        ab = ep(t, q("b"), 0.5)
        expr(c, "= 375/1000", 1180, 420, 66, ab)
        text(c, "× 10 em cima e embaixo (sai a vírgula)", 1180, 530, 24, "black", GRAY, ab)
        ac = ep(t, q("c"), 0.5)
        expr(c, "= 3/8", 1540, 420, 66, ac, cores={1: GREEN})
        text(c, "÷ 125", 1540, 530, 26, "black", GREEN, ac)
        para(c, "simplificar = dividir em cima e embaixo pelo mesmo número", 260, 600, 30, "black", BLUE, ac, 1400)
        ad = ep(t, q("d"), 0.5)
        if ad > 0:
            boxed(c, 360, 670, 1200, 140, GREEN, ad, 0.06)
            fmid(c, "ATALHO: terminou em ,5? desconfie dos OITAVOS", W / 2, 715, 34, "black", GREEN, ad)
            fmid(c, "37,5 = 3 × 12,5 → 3/8", W / 2, 770, 32, "black", INK2, ad)
    else:
        regra(c, "sem vírgula, sobre 10, 100 ou 1000", W / 2, 245, ep(t, q("t"), 0.5), 38)
        ab = ep(t, q("b"), 0.5)
        expr(c, "0,24 = 24/100", 760, 430, 76, ab)
        ac = ep(t, q("c"), 0.5)
        expr(c, "= 6/25", 1240, 430, 76, ac, cores={1: GREEN})
        text(c, "÷ 4 em cima e embaixo", 1240, 560, 26, "black", GREEN, ac)
        ad = ep(t, q("d"), 0.5)
        if ad > 0:
            boxed(c, 360, 620, 1200, 180, GREEN, ad, 0.06)
            pill(c, "ATALHO: conte as casas depois da vírgula", W / 2, 620, GREEN, size=28, a=ad, anchor="center",
                 bounds=(0, 1920))
            fmid(c, "0,24 → 2 casas → 2 zeros → 100", W / 2, 720, 46, "black", INK, ad)


# ======================================================================
# nós fazemos: o jogo das cartas
# ======================================================================

RODADAS = {"18": [(0, ("3/4", "0,75", "75%")), (1, ("1/5", "0,2", "20%"))],
           "19": [(2, ("5/8", "0,625", "62,5%")), (0, ("1/20", "0,05", "5%"))]}


def b_jogo(c, t, C, B):
    head_seq(c, t, C, [("18", "NÓS FAZEMOS · O JOGO", "DIGA NOS OUTROS DOIS IDIOMAS", GREEN),
                       ("19", "NÓS FAZEMOS · O JOGO", "DIGA NOS OUTROS DOIS IDIOMAS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["18", "19"])
    q = lambda x: C[f"{sid}.{x}"]
    second = t >= q("b") - 0.05
    dada, vals = RODADAS[sid][1 if second else 0]
    cue, pc, rc = ("b", "p2", "r2") if second else ("a", "p1", "r1")
    n = (2 if sid == "19" else 0) + (2 if second else 1)
    for k in range(4):
        badge_num(c, k + 1, W / 2 - 120 + k * 80, 205, 1, 22, bg=GREEN if k + 1 == n else LIGHT)
    a0 = ep(t, C["18.t"], 0.5)
    outras = [k for k in range(3) if k != dada]
    viradas = [ep(t, q(cue), 0.6) if k == dada else ep(t, q(rc) + 0.6 * outras.index(k), 0.6) for k in range(3)]
    tres_cartas(c, vals, viradas, a0, y=480)
    pause_timer(c, t, q(pc), W / 2, 770)
    if sid == "19" and not second:
        pill(c, "terminou em ,5 → OITAVOS", W / 2, 780, GREEN, size=30, a=ep(t, q("r1"), 0.5), anchor="center",
             bounds=(0, 1920))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Fração, decimal e porcentagem: três idiomas do mesmo número.", "Cada quinto vale 20%; cada oitavo vale 12,5%.",
          "Para virar porcentagem, multiplique o decimal por 100."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["20", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "20" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=GREEN if k == 1 else PURPLE)
        para(c, s, 320, y, 44, "black", INK, a, 1340, 54)


ERROS = [("Ler 3/8 como 3,8% ou como 38%", "os algarismos são os mesmos: 3 e 8",
          "a barra da fração é divisão: 3 ÷ 8 = 0,375 = 37,5%"),
         ("Responder o complemento (quem NÃO escolheu) em vez do que foi pedido", "a conta estava certa",
          "a alternativa do complemento está lá, esperando: releia a pergunta no fim"),
         ("Voltar de porcentagem para fração e parar em 24/100", "24/100 é o mesmo número",
          "a alternativa vem simplificada: 24/100 = 6/25. Simplifique até o fim")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["21", "22", "23"], ERROS)


# ======================================================================
# questão 8
# ======================================================================

NOTA_Q = "Questão no estilo do ENEM, do material de estudo."
ALTS8 = [("A", "3,8%", "leu 3/8 como 3,8", RED), ("B", "24%", "fez 3 × 8", RED), ("C", "37,5%", "", GREEN),
         ("D", "38%", "leu 3/8 como 3,8", RED), ("E", "62,5%", "complemento: quem NÃO escolheu", AMBER)]


def b_q8(c, t, C, B):
    head_seq(c, t, C, [("24", "ESTILO ENEM · AGORA É COM VOCÊ", "A PESQUISA DE OPINIÃO", BLUE),
                       ("25", "VAMOS CONFERIR", "A PESQUISA DE OPINIÃO", GREEN),
                       ("26", "AS ARMADILHAS", "A PESQUISA DE OPINIÃO", AMBER)])
    card(c, *CARD_R)
    y = 240
    for cue, s, est in (("24.a", "Numa pesquisa de opinião, 3/8 dos entrevistados escolheram a opção A.", "t"),
                        ("24.b", "Esse valor corresponde a que porcentagem do total de entrevistados?", "q")):
        a = ep(t, C[cue], 0.4)
        y += para(c, s, 190, y, 32, "bold" if est == "q" else "black", BLUE if est == "q" else INK, a, 600, 42) + 16
    text(c, NOTA_Q, 190, 830, 18, "medium", GRAY, ep(t, C["24.a"], 0.5), align="left")
    cues_in = {L: C[f"24.{x}"] for L, x in zip("ABCDE", "cdefg")}
    cues_x = {"E": C["26.e"], "A": C["26.a"], "D": C["26.a"] + 0.4, "B": C["26.b"]}
    K.alternativas(c, t, C, ALTS8, 900, 215, 790, 44, C["25.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["24.end"] - 1.9, 480, 660)
    ra = ep(t, C["25.a"], 0.4)
    if ra > 0:
        rrect(c, 170, 560, 640, 250, 18, "#FFFFFF", ra, shadow=True)
        fmid(c, "3 ÷ 8 = 0,375", 490, 600, 40, "black", INK, ra)
        fmid(c, "× 100 = 37,5%", 490, 650, 40, "black", INK, ep(t, C["25.a"] + 2.2, 0.4))
        ab = ep(t, C["25.b"], 0.4)
        fmid(c, "ATALHO: 3 × 12,5% = 37,5%", 490, 706, 34, "black", GREEN, ab)
        result_box(c, "Letra C", 490, 762, 30, ep(t, C["25.ok"], 0.5), GREEN)


# ======================================================================
# a tabela completa, ponte e CTA
# ======================================================================

def b_tabela(c, t, C, B):
    head(c, t, B["start"], "A TABELA QUE VALE OURO", "COMPLETA", AMBER)
    aa = ep(t, C["28.a"], 0.6)
    tabela_completa(c, aa)
    selo(c, 1560, 92, ep(t, C["28.b"], 0.5), "TIRE UM PRINT", RED, -6, 34)
    pill(c, "revise uma família por dia", 360, 92, GREEN, size=30, a=ep(t, C["28.c"], 0.5), anchor="center",
         bounds=(0, 1920))


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "REVISÃO GERAL", PURPLE)
    ab = ep(t, C["29.b"], 0.5)
    pizza(c, 430, 380, 90, 4, 3, ab * ep(t, C["29.b"], 0.4), pull=0.4)
    fmid(c, "0,5", 760, 380, 80, "black", PURPLE, ab * ep(t, C["29.b"] + 0.3, 0.4))
    fmid(c, "0,333…", 1110, 380, 70, "black", AMBER, ab * ep(t, C["29.b"] + 0.6, 0.4))
    fmid(c, "37,5%", 1470, 380, 80, "black", GREEN, ab * ep(t, C["29.b"] + 0.9, 0.4))
    text(c, "juntamos tudo", W / 2, 520, 40, "black", INK2, ab)
    selo(c, 640, 640, ep(t, C["29.c"], 0.5), "PEGADINHAS", AMBER, -5, 40)
    chip(c, "questões novas", 1260, 640, GREEN, ep(t, C["29.d"], 0.5), 40, w=420)
    pill(c, "ep. 8 · revisão e questões inéditas", W / 2, 780, PURPLE, size=32, a=ep(t, C["29.e"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"], "Qual família da tabela você já sabia?",
        canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, concreto=b_concreto, idiomas=b_idiomas, porcento=b_porcento,
              prereq=b_prereq, fam_quartos=b_fam_quartos, fam_tercos=b_fam_tercos, fam_quintos=b_fam_quintos,
              fam_oitavos=b_fam_oitavos, fam_decimos=b_fam_decimos, conv=b_conv, jogo=b_jogo, recap=b_recap,
              erros=b_erros, q8=b_q8, tabela=b_tabela, ponte=b_ponte, cta=b_cta)
