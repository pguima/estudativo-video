"""Visual — Taxas Equivalentes e Inflação, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): reta × curva · etiqueta de vitrine · carrinho de
supermercado · escada rolante.
Em cada questão inédita: a ficha do fator "(1 + i)" (area_icone()) + o contexto (calendário, banco, carteira, holerite,
gráfico de barras em queda).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum031", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_taxas_ep5_revisao.mp4"
CARD_R = K.CARD_R
ETIQ = "#FFF4D6"
DEGRAU = "#9AA5B1"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças
# ======================================================================

def reta_curva(c, a):
    """eixos com a reta da proporcional (azul) e a curva da equivalente (verde)"""
    line(c, -150, 90, 160, 90, INK2, a, 4); line(c, -150, 90, -150, -120, INK2, a, 4)
    line(c, -150, 90, 140, -40, BLUE, a, 6)
    p = skia.Path(); p.moveTo(-150, 90)
    p.cubicTo(-30, 80, 80, 20, 140, -110)
    c.drawPath(p, paint(GREEN, a, stroke=7))
    text_mid(c, "reta", 115, 5, 26, "black", BLUE, a)
    text_mid(c, "curva", 60, -110, 26, "black", GREEN, a)


def etiqueta(c, a, s="24% a.a.", col=AMBER, w=240, h=110):
    """etiqueta de preço com furo e barbante"""
    p = skia.Path(); p.moveTo(-w / 2, -h / 2); p.lineTo(w / 2 - 40, -h / 2); p.lineTo(w / 2, 0)
    p.lineTo(w / 2 - 40, h / 2); p.lineTo(-w / 2, h / 2); p.close()
    c.drawPath(p, paint(ETIQ, a)); c.drawPath(p, paint(col, a, stroke=5))
    c.drawCircle(w / 2 - 34, 0, 9, paint("#FFFFFF", a)); c.drawCircle(w / 2 - 34, 0, 9, paint(col, a, stroke=3))
    sz = 40
    while ftw(s, sz) > w - 70:
        sz -= 2
    fmid(c, s, -20, 2, sz, "black", col, a)


def vitrine(c, a):
    """etiqueta da vitrine (nominal) e o cupom do caixa (efetiva)"""
    c.save(); c.translate(-60, -50); c.rotate(-6); etiqueta(c, a, "24% a.a.", AMBER, 230, 96); c.restore()
    rrect(c, 10, 10, 170, 110, 8, "#FFFFFF", a, stroke=3, stroke_color=INK2)
    text_mid(c, "CAIXA", 95, 38, 22, "black", INK2, a)
    text_mid(c, "≈ 26,8%", 95, 85, 34, "black", GREEN, a)


def carrinho(c, a):
    """carrinho de supermercado com a etiqueta do fator dos preços"""
    line(c, -150, -70, -110, -70, INK2, a, 6)
    p = skia.Path(); p.moveTo(-110, -70); p.lineTo(-80, 40); p.lineTo(110, 40); p.lineTo(135, -40); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.15), a)); c.drawPath(p, paint(BLUE, a, stroke=5))
    for x in (-60, 85):
        c.drawCircle(x, 70, 16, paint(INK2, a))
    c.save(); c.translate(20, -105); c.rotate(-6)
    rrect(c, -80, -30, 160, 60, 10, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-80, -30, 160, 60), 10, 10), paint(RED, a, stroke=5))
    text_mid(c, "÷ 1,25", 0, 0, 30, "black", RED, a)
    c.restore()


def escada(c, a):
    """escada rolante de preços: degraus subindo, com a seta"""
    p = skia.Path(); p.moveTo(-170, 90)
    for k in range(6):
        p.lineTo(-170 + (k + 1) * 50, 90 - k * 34); p.lineTo(-170 + (k + 1) * 50, 90 - (k + 1) * 34)
    p.lineTo(150, 90 - 6 * 34); p.lineTo(150, 90); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", DEGRAU, 0.5), a)); c.drawPath(p, paint(INK2, a, stroke=4))
    line(c, -180, 50, 140, -170, INK2, a, 5)
    arrow(c, -120, 10, 60, -112, GREEN, a, 7, 20)
    text_mid(c, "R$", -40, -80, 30, "black", GREEN, a)


def fator(c, a, s="(1 + i)", col=PURPLE):
    """ficha do fator de cada questão inédita"""
    w = ftw(s, 44) + 60
    rrect(c, -w / 2, -40, w, 80, 18, mix("#FFFFFF", col, 0.12), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -40, w, 80), 18, 18), paint(col, a, stroke=5))
    fmid(c, s, 0, 2, 44, "black", col, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão) + a ficha do fator, em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (reta_curva, vitrine, carrinho, escada, fator)[k](c, a)
    c.restore()


def contexto(c, k, a):
    if k == 0:      # calendário de 3 meses
        for j in range(3):
            x = -110 + j * 80
            rrect(c, x - 34, -40, 68, 80, 8, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            rrect(c, x - 34, -40, 68, 22, 8, BLUE, a)
            text_mid(c, f"{j + 1}º", x, 14, 28, "black", INK, a)
        text_mid(c, "× 1,05", 0, 78, 30, "black", PURPLE, a)
    elif k == 1:    # banco
        p = skia.Path(); p.moveTo(-110, -40); p.lineTo(0, -95); p.lineTo(110, -40); p.close()
        c.drawPath(p, paint(INK2, a))
        for x in (-80, -27, 27, 80):
            rrect(c, x - 12, -30, 24, 90, 4, mix("#FFFFFF", INK2, 0.35), a)
        rrect(c, -120, 62, 240, 18, 4, INK2, a)
    elif k == 2:    # carteira
        rrect(c, -100, -55, 200, 120, 16, "#8D6E63", a)
        rrect(c, 20, -20, 100, 50, 12, "#6D4C41", a)
        c.drawCircle(60, 5, 9, paint(AMBER, a))
        rrect(c, -80, -80, 120, 40, 4, mix("#FFFFFF", GREEN, 0.5), a)
    elif k == 3:    # holerite
        rrect(c, -80, -80, 160, 170, 8, "#FFFFFF", a, stroke=3, stroke_color=INK2)
        text_mid(c, "SALÁRIO", 0, -52, 22, "black", INK2, a)
        for j in range(3):
            line(c, -55, -15 + j * 30, 55 - (j == 2) * 30, -15 + j * 30, LIGHT, a, 8)
        text_mid(c, "+8%", 0, 70, 30, "black", GREEN, a)
    elif k == 4:    # barras de inflação em queda
        line(c, -110, 70, 120, 70, INK2, a, 3)
        for j, (h, s) in enumerate(((120, "6%"), (80, "4%"), (40, "2%"))):
            x = -80 + j * 75
            rrect(c, x - 26, 70 - h, 52, h, 4, mix("#FFFFFF", RED, 0.45), a)
            text_mid(c, s, x, 50 - h, 24, "black", RED, a)


def area_icone(c, k, cx, cy, s, a):
    """a ficha do fator de cada questão inédita + o contexto dela"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    c.save(); c.translate(-160, 0); fator(c, a); c.restore()
    c.save(); c.translate(170, 0); contexto(c, k, a); c.restore()
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def nb(s):
    """espaço rígido: não quebra '26,8 %', 'a.a.' nem número + unidade"""
    s = re.sub(r"(?<=\d) (?=(%|a\.a\.|a\.m\.|a\.s\.|anos?|meses)\b)", " ", s)
    return s


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        text(c, "“equivalente”", W / 2, 300, 70, "black", GRAY, aa)
        w = text_w("“equivalente”", "black", 70)
        strike(c, W / 2 - w / 2 - 10, 280, W / 2 + w / 2 + 10, 280, aa, RED, aa)
    for k, s in enumerate(("qual rende mais?", "o salário ganhou da inflação?", "quanto custou de verdade?")):
        chip(c, s, [330, 900, 1560][k], 470, [BLUE, AMBER, RED][k], ep(t, C["01.b"] + 1.0 * k, 0.4), 30)
    ac = ep(t, C["01.c"], 0.6)
    if ac > 0:
        c.save(); c.translate(W / 2, 640); c.scale(1.6, 1.6); fator(c, ac, "FATORES", PURPLE); c.restore()
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 840, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 840, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


COBRA = [("02.a", "TROCAR O PERÍODO", "sem × nem ÷ pelo nº de períodos", 0, BLUE),
         ("02.b", "INFLAÇÃO × GANHO REAL", "fatores se multiplicam e se dividem", 3, PURPLE),
         ("02.c", "POTÊNCIAS DADAS", "1,01¹² ≈ 1,1268: não calcule", 4, GREEN)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "AS TRÊS COBRANÇAS", "O QUE O ENEM COBRA", BLUE)
    for k, (cue, tit, sub, ic, col) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 230 + d, 500, 540, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 290 + d, a, 28, bg=col)
        if ic == 4:
            c.save(); c.translate(x, 450 + d); fator(c, a, "1,01¹²", GREEN); c.restore()
        else:
            icone(c, ic, x, 450 + d, 0.75, a)
        para(c, tit, x, 620 + d, 32, "black", col, a, 440, 38, align="center")
        para(c, sub, x, 700 + d, 25, "bold", INK2, a, 440, 32, align="center")


INDICE = [("EP. 1", "mesmo destino · fator primeiro, taxa depois · reta × curva"),
          ("EP. 2", "nominal = vitrine · efetiva = caixa"),
          ("EP. 3", "escada rolante · poder de compra é divisão"),
          ("EP. 4", "deflacionar = traduzir · taxa real: divida os fatores")]
IND_CUES = ["03.a", "03.b", "04.a", "04.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 285 + k * 450
        y = 200
        rrect(c, x - 205, y, 410, 610, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 205, y, 410, 610), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 180, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 210, 0.8, a)
        yy = y + 380
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 28, "black", INK if on_ else INK2, a, 360, 34, align="center") + 16


ONDE = [("05.a", "ROTATIVO DO CARTÃO", "1 dígito ao mês · 3 dígitos ao ano"),
        ("05.b", "IPCA · IBGE", "gráficos de inflação em Humanas"),
        ("05.c", "SALÁRIO", "reajuste e poder de compra"),
        ("05.d", "PRÓXIMAS SÉRIES", "Empréstimos · Comparação de propostas")]


def onde_icone(c, k, cx, cy, a):
    if a <= 0:
        return
    if k == 0:      # cartão
        rrect(c, cx - 100, cy - 60, 200, 124, 14, "#3D5A80", a, shadow=True)
        rrect(c, cx - 100, cy - 34, 200, 22, 0, INK, a)
        text_mid(c, "10% a.m.", cx, cy + 26, 30, "black", "#FFFFFF", a)
    elif k == 1:    # gráfico de linha
        line(c, cx - 100, cy + 60, cx + 100, cy + 60, INK2, a, 3); line(c, cx - 100, cy + 60, cx - 100, cy - 70, INK2, a, 3)
        p = skia.Path(); p.moveTo(cx - 90, cy - 40); p.lineTo(cx - 40, cy - 10); p.lineTo(cx + 10, cy - 30)
        p.lineTo(cx + 50, cy + 10); p.lineTo(cx + 90, cy + 20)
        c.drawPath(p, paint(RED, a, stroke=6))
        text_mid(c, "inflação %", cx + 20, cy - 80, 24, "black", RED, a)
    elif k == 2:    # holerite
        c.save(); c.translate(cx, cy); c.scale(0.8, 0.8); contexto(c, 3, a); c.restore()
    else:           # contrato com parcelas
        rrect(c, cx - 80, cy - 75, 160, 150, 8, "#FFFFFF", a, stroke=3, stroke_color=INK2)
        for j in range(4):
            line(c, cx - 55, cy - 40 + j * 28, cx + 55, cy - 40 + j * 28, LIGHT, a, 8)
        text_mid(c, "12 ×", cx + 120, cy - 50, 30, "black", PURPLE, a)


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ NO BANCO", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, sub) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 240 + d, 380, 470, 24, mix("#F7F7F5", BLUE, 0.06), a)
        onde_icone(c, k, x, 390 + d, a)
        para(c, tit, x, 550 + d, 30, "black", BLUE, a, 340, 36, align="center")
        para(c, sub, x, 620 + d, 24, "bold", INK2, a, 330, 30, align="center")


HABITOS = [("06.a", "1", "TUDO EM FATORES", "20% → 1,2 · −10% → 0,9"),
           ("06.b", "2", "REGIME E TIPO", "“capitalizado” = nominal"),
           ("06.c", "3", "USE O DADO · CONFIRA", "real ≈ diferença, um pouco menor")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 250 + d, 500, 480, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=GREEN)
        para(c, tit, x, 430 + d, 38, "black", GREEN, a, 440, 46, align="center")
        for j, ln in enumerate(sub.split(" · ")):
            sz = 32
            while ftw(ln, sz, "bold") > 440:
                sz -= 1
            ftext(c, ln, x, 600 + d + j * 50, sz, "bold", INK, a)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["07"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["07.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["07.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["07.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("juros compostos · 2% ao mês", "= 24% ao ano", False, "12 × 2 = 24",
     "isso é a reta (juros simples) · compostos: 1,02¹² ≈ 1,268", "≈ 26,8% a.a.", 0),
    ("21% em 2 anos", "= 10,5% ao ano", False, "dividir por 2 parece justo",
     "encurtar o período: raiz do fator · 1,1² = 1,21", "10% a.a.", 0),
    ("12% a.a. capitalizados mensalmente", "custam 12% ao ano", False, "o 12 está escrito ali",
     "é a vitrine: ÷ 12 = 1% a.m. · capitalize: 1,01¹² ≈ 1,1268", "≈ 12,68% a.a.", 1),
    ("fator acumulado 1,268", "= aumento de 26,8%", True, "o 126,8% está sempre nas alternativas",
     "fator primeiro, taxa depois · tire o 1", "1,268 − 1 = 0,268", 0),
    ("inflação de 5% e depois de 10%", "acumulam 15%", False, "5 + 10 = 15",
     "a 2ª incide sobre preços já aumentados · 1,05 × 1,10 = 1,155", "15,5%", 2),
    ("inflação de 100%", "tira metade do poder de compra", True, "espera-se perder os mesmos 100%",
     "poder de compra é divisão · 1 ÷ 2 = 0,5", "compra a metade", 2),
    ("rendeu 17,6% · inflação 12%", "ganho real de 5,6%", False, "a subtração é rápida",
     "divida os fatores · 1,176 ÷ 1,12 = 1,05", "5% real", 3),
    ("rendeu 8% · inflação 10%", "perdeu poder de compra", True, "o saldo do extrato subiu",
     "mais devagar que a escada · 1,08 ÷ 1,10 ≈ 0,982", "< 1: perda", 3),
    ("a inflação caiu de 8% para 4%", "os preços caíram", False, "“caiu” está na manchete",
     "caiu a velocidade: a escada continua subindo · preço caindo = deflação", "subiram 4%", 3),
]
VF_IDS = [f"{8 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 62 + k * 62, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    icone(c, ic, 330, 420, 0.55, a0)
    szc = 30
    while ftw(nb(ctx).upper(), szc) > 760:
        szc -= 1
    text(c, nb(ctx).upper(), 960, 310, szc, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 60
    while ftw(conta, sz) > 680:
        sz -= 2
    fmid(c, nb(conta), 960, 410, sz, "black", INK, a0)
    if ar > 0 and not ver:
        w = ftw(conta, sz)
        strike(c, 960 - w / 2 - 10, 415, 960 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        sze = 34
        while ftw(engana, sze, "bold") > (1020 if ver else 1140):
            sze -= 1
        ftext(c, nb(engana), 640 if ver else 520, 552, sze, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        lns = regra_.split(" · ")
        for j, ln in enumerate(lns):
            szr = 30
            while ftw(ln, szr) > 860:
                szr -= 1
            ftext(c, nb(ln), 240, 705 + (j - (len(lns) - 1) / 2) * 44, szr, "black", GREEN, ag, align="left")
        szf = 44
        while ftw(fix, szf) > 520:
            szf -= 2
        fmid(c, nb(fix), 1420, 715, szf, "black", GREEN, ag)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["17.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["17.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 140 + k * 140
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["17.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    if ab > 0:
        c.save(); c.translate(W / 2, 760); c.scale(1.3, 1.3); fator(c, ab, "fatores primeiro", PURPLE); c.restore()


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · pad: a ideia · passos: (cue, texto) · confere: (cue, texto) ou None

Q = {
    "q1": dict(ids=("18", "19"), titulo="O TRIMESTRE", area="TAXA EQUIVALENTE", ic=0, ok="C",
               enun=[("a", "Uma aplicação rende 5% ao mês, em juros compostos. Considere 1,05³ ≈ 1,158.", False),
                     ("b", "A taxa TRIMESTRAL equivalente é de", True)],
               alts=[("A", "15%", "proporcional: a reta", AMBER), ("B", "115,8%", "não tirou o 1", RED),
                     ("C", "15,8%", "", GREEN), ("D", "1,58%", "vírgula deslocada", RED),
                     ("E", "5%", "repetiu a do mês", RED)],
               pad="fator primeiro: 1,05", passos=[("a", "3 meses: 1,05³ ≈ 1,158"),
                                                   ("b", "tire o 1: 0,158 = 15,8% ao trimestre")],
               confere=("v", "um pouco acima dos 15% da reta")),
    "q2": dict(ids=("20", "21"), titulo="A VITRINE DO BANCO", area="NOMINAL → EFETIVA", ic=1, ok="A",
               enun=[("a", "Um banco anuncia 30% ao ano, capitalizados semestralmente. Considere 1,15² = 1,3225.", False),
                     ("b", "A taxa EFETIVA anual é de", True)],
               alts=[("A", "32,25%", "", GREEN), ("B", "30%", "a vitrine", AMBER),
                     ("C", "15%", "só o semestre", AMBER), ("D", "132,25%", "não tirou o 1", RED),
                     ("E", "60%", "somou 30% duas vezes", RED)],
               pad="“capitalizados” = vitrine (nominal)", passos=[("a", "÷ 2 semestres: 15% ao semestre"),
                                                                  ("b", "1,15² = 1,3225 → 32,25% ao ano")],
               confere=("v", "atalho: 30 + 15² ÷ 100 = 32,25")),
    "q3": dict(ids=("22", "23"), titulo="A RENDA PARADA", area="PODER DE COMPRA", ic=2, ok="D",
               enun=[("a", "Num ano de inflação de 50%, uma pessoa ficou com a renda parada.", False),
                     ("b", "O poder de compra dela caiu cerca de", True)],
               alts=[("A", "50%", "= a inflação", RED), ("B", "66,7%", "o que sobrou", AMBER),
                     ("C", "25%", "metade da inflação", RED), ("D", "33,3%", "", GREEN),
                     ("E", "150%", "o fator", RED)],
               pad="poder de compra é divisão", passos=[("a", "1 ÷ 1,5 ≈ 0,667: sobram 2/3"),
                                                        ("b", "perdeu 1/3 ≈ 33,3%")],
               confere=("v", "a perda é menor que a inflação")),
    "q4": dict(ids=("24", "25"), titulo="O REAJUSTE", area="REAJUSTE × INFLAÇÃO", ic=3, ok="B",
               enun=[("a", "Uma categoria teve reajuste de 8% num ano de inflação de 20%.", False),
                     ("b", "Em termos reais, o salário", True)],
               alts=[("A", "perdeu 12%", "subtraiu 8 − 20", AMBER), ("B", "perdeu 10%", "", GREEN),
                     ("C", "ganhou 8%", "esqueceu a inflação", RED), ("D", "perdeu 28%", "somou as taxas", RED),
                     ("E", "ganhou 10%", "sinal trocado", RED)],
               pad="taxa real: divida os fatores", passos=[("a", "1,08 ÷ 1,20 = 0,90"),
                                                           ("b", "< 1: perda real de 10%")],
               confere=("v", "um pouco menor que os 12 da subtração")),
    "q5": dict(ids=("26", "27"), titulo="A INFLAÇÃO EM QUEDA", area="GRÁFICO DE INFLAÇÃO", ic=4, ok="E",
               enun=[("a", "Inflação em 3 anos seguidos: 6%, 4% e 2%. Considere 1,06 · 1,04 · 1,02 ≈ 1,124.", False),
                     ("b", "Nesses três anos, os preços", True)],
               alts=[("A", "caíram", "inflação caindo ≠ preço caindo", RED),
                     ("B", "voltaram ao início", "inflação caindo ≠ preço caindo", RED),
                     ("C", "subiram 12%", "somou as taxas", AMBER), ("D", "subiram 2%", "só o último ano", AMBER),
                     ("E", "subiram ≈ 12,4%", "", GREEN)],
               pad="escada mais lenta, mas subindo", passos=[("a", "todo ano: fator maior que 1"),
                                                             ("b", "1,124 − 1 → subiram ≈ 12,4%")],
               confere=None),
}


def para_nb(c, s, x, y, size, peso, color, a, maxw, lh=None):
    """quebra de linha que respeita os espaços rígidos de nb()"""
    s = nb(s)
    lh = lh or size * 1.32
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and text_w(tst, peso, size) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    if cur:
        out.append(cur)
    if a > 0:
        for k, ln in enumerate(out):
            text(c, ln, x, y + k * lh, size, peso, color, a, align="left")
    return len(out) * lh


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · {d['area']}", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        area_icone(c, d["ic"], 770, 222, 0.40, a0)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            if ad > 0:
                boxed(c, 170, 260, 650, 84, PURPLE, ad, 0.08)
                pill(c, "A IDEIA", 190, 260, PURPLE, size=18, a=ad, bounds=(0, 1920))
                szp = 30
                while ftw(d["pad"], szp) > 600:
                    szp -= 1
                ftext(c, d["pad"], 190, 316, szp, "black", INK, ad, align="left")
            yy = 420
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                for ln in s.split(" · "):
                    sz = 34
                    while ftw(ln, sz) > 640:
                        sz -= 2
                    ftext(c, nb(ln), 180, yy, sz, "black", GREEN if last else INK, a, align="left")
                    yy += 56
                yy += 6
            if d["confere"]:
                cue, s = d["confere"]
                sz = 30
                while ftw(s, sz) > 580:
                    sz -= 2
                conferido(c, s, 190, yy + 10, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, sz)
            result_box(c, f"Letra {d['ok']}", 1290, 700, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("28.b", "EP. 1", ["proporcional × equivalente", "mensal → anual: fator ^ 12", "período curto: raiz do fator",
                            "1,1² = 1,21 · 1,1³ = 1,331 · 1,2² = 1,44"]),
         ("28.c", "EP. 2", ["nominal → efetiva: ÷ e capitalize", "acumuladas: multiplique (até negativas)"]),
         ("29.a", "EP. 3", ["inflação e inflação acumulada", "poder de compra: 1 − 1/(1 + π)",
                            "inflação em queda ≠ deflação"]),
         ("29.b", "EP. 4", ["deflacionar um valor", "(1 + n) = (1 + r)(1 + π)", "quando “n − π” falha"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["28.a"], 0.5) * (1 - ep(t, C["28.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(170, 200), (990, 200), (170, 500), (990, 500)]
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x + 40, y0 + 100, 0.22, a)
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 46
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            sz = 26
            while ftw(it, sz, "bold") > 600:
                sz -= 1
            K.ftext(c, it, x + 158, yy + 10, sz, "bold", INK, a, align="left")
    ae = ep(t, C["29.c"], 0.5)
    if ae > 0:
        boxed(c, W / 2 - 360, 730, 720, 90, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", W / 2, 775, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["30.a"], 0.5)
    ab = ep(t, C["30.b"], 0.5)
    for i in range(20):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["30.a"] + 0.04 * i, 0.2)
        ok = ab > 0 and i < 14
        x, y = 230 + k * 82, 250 + r_ * 90
        rrect(c, x, y, 66, 72, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "20 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "14 acertos = 70%", 1450, 400, 46, "black", GREEN, ab)
    ac = ep(t, C["30.c"], 0.5)
    if ac > 0:
        boxed(c, 230, 560, 1460, 200, AMBER, ac, 0.10)
        icone(c, 3, 400, 670, 0.5, ac)
        text_mid(c, "priorize:", 1150, 610, 32, "bold", INK2, ac)
        text_mid(c, "taxa real e reajuste de salário", 1150, 670, 38, "black", INK, ac)
        text_mid(c, "taxas de períodos diferentes", 1150, 725, 38, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Empréstimos, financiamentos e parcelamentos", W / 2, 330, 56, "black", PURPLE, aa)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        boxed(c, W / 2 - 420, 420, 840, 120, AMBER, ab, 0.10)
        text_mid(c, "os juros do “sem juros”", W / 2, 480, 50, "black", INK, ab)
    chip(c, "tabela SAC", 720, 660, BLUE, ep(t, C["31.c"], 0.5), 46)
    chip(c, "tabela Price", 1200, 660, GREEN, ep(t, C["31.d"], 0.5), 46)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
