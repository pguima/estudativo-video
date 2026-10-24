"""Visual — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 4: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 3 ícones dos episódios (icone()): pizza do preço · carimbos no carrinho · régua do custo
(e o prédio das faixas como ícone extra do V/F).
Em cada questão inédita: a etiqueta de preço com a pergunta "DE QUÊ?" (area_icone()) + o contexto (bolsa, bolo, caixas,
prédio, etiqueta remarcada).
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
import re
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum030", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_descontos_ep4_revisao.mp4"
CARD_R = K.CARD_R
MASSA = "#F6D27A"
MASSA2 = "#D9A441"
TOMATE = "#E2574C"
ETIQ = "#FFF4D6"
TINTA = "#7A4FB5"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças
# ======================================================================

def pizza(c, a, r=100):
    """a pizza do preço de venda: a fatia verde é o lucro, o resto paga o custo"""
    c.drawCircle(0, 0, r + 8, paint(MASSA2, a))
    c.drawCircle(0, 0, r, paint(MASSA, a))
    for ang, d in ((40, 0.5), (130, 0.6), (220, 0.45), (300, 0.62), (180, 0.2)):
        x, y = d * r * math.cos(math.radians(ang)), d * r * math.sin(math.radians(ang))
        c.drawCircle(x, y, r * 0.11, paint(TOMATE, a))
    p = skia.Path(); p.moveTo(0, 0)
    p.arcTo(skia.Rect.MakeXYWH(-r - 8, -r - 8, 2 * r + 16, 2 * r + 16), -90, 72, False); p.close()
    c.save(); c.translate(14, -10)
    c.drawPath(p, paint(GREEN, a))
    c.drawPath(p, paint("#FFFFFF", a, stroke=4))
    c.restore()
    text_mid(c, "lucro", r * 0.55, -r - 34, 26, "black", GREEN, a)


def carrinho(c, a):
    """carrinho com dois carimbos que se multiplicam"""
    line(c, -150, -70, -110, -70, INK2, a, 6)
    p = skia.Path(); p.moveTo(-110, -70); p.lineTo(-80, 40); p.lineTo(110, 40); p.lineTo(135, -40); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", BLUE, 0.15), a)); c.drawPath(p, paint(BLUE, a, stroke=5))
    for x in (-60, 85):
        c.drawCircle(x, 70, 16, paint(INK2, a))
    for k, (s, x, rot) in enumerate((("× 0,8", -40, -10), ("× 0,9", 70, 8))):
        c.save(); c.translate(x, -95); c.rotate(rot)
        rrect(c, -62, -30, 124, 60, 10, "#FFFFFF", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-62, -30, 124, 60), 10, 10), paint(TINTA, a, stroke=5))
        text_mid(c, s, 0, 0, 30, "black", TINTA, a)
        c.restore()


def regua(c, a, marcas=((0, "100"), (0.8, "180"), (0.08, "108"))):
    """a régua do custo: começa no custo (100) e mostra onde o preço final parou"""
    x0, x1, y = -180, 180, 20
    rrect(c, x0 - 20, y - 40, x1 - x0 + 40, 80, 10, "#FFF6DA", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 20, y - 40, x1 - x0 + 40, 80), 10, 10),
                paint(MASSA2, a, stroke=3))
    for k in range(19):
        h = 26 if k % 2 == 0 else 14
        line(c, x0 + k * 20, y - 40, x0 + k * 20, y - 40 + h, MASSA2, a, 3)
    sx = (x1 - x0) / 0.9
    cores = (BLUE, AMBER, GREEN)
    for j, (u, s) in enumerate(marcas):
        x = x0 + u * sx
        c.drawCircle(x, y + 18, 10, paint(cores[j], a))
        text_mid(c, s, x, y + 78 + (j == 2) * 34, 28, "black", cores[j], a)


def predio(c, a):
    """o prédio das faixas: cada andar com a sua taxa"""
    for k, (s, col) in enumerate((("0%", LIGHT), ("10%", mix("#FFFFFF", BLUE, 0.35)), ("20%", mix("#FFFFFF", PURPLE, 0.4)))):
        y = 60 - k * 70
        rrect(c, -90, y - 30, 180, 64, 6, col, a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-90, y - 30, 180, 64), 6, 6), paint(INK2, a, stroke=3))
        text_mid(c, s, 0, y + 2, 30, "black", INK, a)
    p = skia.Path(); p.moveTo(-104, -112); p.lineTo(0, -162); p.lineTo(104, -112); p.close()
    c.drawPath(p, paint(INK2, a))


def etiqueta(c, a, s="DE QUÊ?", col=AMBER, w=220, h=110):
    """etiqueta de preço com furo e barbante"""
    p = skia.Path(); p.moveTo(-w / 2, -h / 2); p.lineTo(w / 2 - 40, -h / 2); p.lineTo(w / 2, 0)
    p.lineTo(w / 2 - 40, h / 2); p.lineTo(-w / 2, h / 2); p.close()
    c.drawPath(p, paint(ETIQ, a)); c.drawPath(p, paint(col, a, stroke=5))
    c.drawCircle(w / 2 - 34, 0, 9, paint("#FFFFFF", a)); c.drawCircle(w / 2 - 34, 0, 9, paint(col, a, stroke=3))
    q = skia.Path(); q.moveTo(w / 2 - 34, 0); q.quadTo(w / 2 + 20, -h * 0.8, w / 2 + 60, -h * 0.5)
    c.drawPath(q, paint(INK2, a, stroke=3))
    sz = 40
    while ftw(s, sz) > w - 70:
        sz -= 2
    fmid(c, s, -20, 2, sz, "black", col, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 3 ícones da série (índice da revisão) + o prédio das faixas, em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:
        pizza(c, a)
    elif k == 1:
        carrinho(c, a)
    elif k == 2:
        regua(c, a)
    elif k == 3:
        predio(c, a)
    elif k == 4:
        etiqueta(c, a)
    c.restore()


def contexto(c, k, a):
    if k == 0:      # bolsa
        rrect(c, -70, -30, 140, 110, 14, mix("#FFFFFF", PURPLE, 0.45), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-70, -30, 140, 110), 14, 14), paint(PURPLE, a, stroke=4))
        p = skia.Path(); p.moveTo(-40, -30); p.quadTo(0, -110, 40, -30)
        c.drawPath(p, paint(PURPLE, a, stroke=7))
    elif k == 1:    # bolo
        rrect(c, -80, -10, 160, 90, 10, "#C98E62", a)
        rrect(c, -80, -30, 160, 34, 14, "#FFF0F4", a)
        for x in (-50, 0, 50):
            c.drawCircle(x, -40, 13, paint(TOMATE, a))
        line(c, 0, -60, 0, -100, AMBER, a, 6)
    elif k == 2:    # 4 caixas
        for j in range(4):
            x = -90 + j * 60
            rrect(c, x - 26, -10, 52, 60, 6, mix("#FFFFFF", BLUE, 0.3) if j < 3 else mix("#FFFFFF", GREEN, 0.45), a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 26, -10, 52, 60), 6, 6), paint(INK2, a, stroke=3))
        text_mid(c, "× 4", 0, -60, 34, "black", INK, a)
    elif k == 3:    # prédio
        c.save(); c.scale(0.7, 0.7); predio(c, a); c.restore()
    elif k == 4:    # etiqueta remarcada
        rrect(c, -80, -50, 160, 100, 10, "#FFFFFF", a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-80, -50, 160, 100), 10, 10), paint(RED, a, stroke=4))
        text_mid(c, "180", 0, -18, 36, "black", INK2, a)
        line(c, -40, -18, 40, -18, RED, a, 5)
        text_mid(c, "−40%", 0, 26, 30, "black", RED, a)


def area_icone(c, k, cx, cy, s, a):
    """a etiqueta "DE QUÊ?" de cada questão inédita + o contexto dela"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    c.save(); c.translate(-150, 0); etiqueta(c, a); c.restore()
    c.save(); c.translate(170, 0); contexto(c, k, a); c.restore()
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def nb(s):
    """espaço rígido: não quebra 'R$ 150,00', '25 %' nem número + unidade"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(%|reais|unidades)\b)", " ", s)
    return s


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 230, 620, 150, GREEN, aa, 0.08)
        check_icon(c, 340, 305, 34, aa, GREEN)
        text_mid(c, "CONTA CERTA", 600, 305, 52, "black", GREEN, aa)
    ab_ = ep(t, C["01.a"] + 1.4, 0.5)
    if ab_ > 0:
        boxed(c, 1040, 230, 620, 150, RED, ab_, 0.08)
        check_icon(c, 1120, 305, 34, ab_, RED, "x")
        text_mid(c, "BASE ERRADA", 1380, 305, 52, "black", RED, ab_)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "a única pergunta que importa:", W / 2, 460, 40, "bold", INK2, ab)
    ac = ep(t, C["01.c"], 0.6)
    if ac > 0:
        c.save(); c.translate(W / 2 - 60, 640); c.scale(1.7, 1.7); c.rotate(-3)
        etiqueta(c, ac, "DE QUÊ?", AMBER, 300, 110)
        c.restore()
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 820, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 820, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


COBRA = [("02.a", "LUCRO E PREJUÍZO", "em reais e em % · do custo ou da venda", 0, BLUE),
         ("02.b", "PREÇO PARA UMA MARGEM", "a fatia dentro da pizza", 0, PURPLE),
         ("02.c", "ENCADEADOS", "liquidação · caixa · frete", 1, GREEN),
         ("02.d", "PROMOÇÕES", "viram desconto efetivo", 5, AMBER),
         ("02.e", "POR FAIXA", "cada parte com a sua taxa", 3, RED)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "AS CINCO COBRANÇAS", "O QUE O ENEM COBRA", BLUE)
    for k, (cue, tit, sub, ic, col) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 230 + d, 330, 520, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 285 + d, a, 26, bg=col)
        if ic == 5:
            c.save(); c.translate(x, 430 + d); c.scale(0.8, 0.8); contexto(c, 2, a); c.restore()
        elif k == 1:
            c.save(); c.translate(x, 430 + d); c.scale(0.9, 0.9); etiqueta(c, a, "R$ ?", PURPLE, 200, 100); c.restore()
        else:
            icone(c, ic, x, 430 + d, 0.62, a)
        para(c, tit, x, 590 + d, 28, "black", col, a, 300, 34, align="center")
        para(c, sub, x, 680 + d, 23, "bold", INK2, a, 290, 30, align="center")


INDICE = [("EP. 1", "toda % tem dono · a pizza: o lucro é uma fatia · markup em cima, margem dentro"),
          ("EP. 2", "carimbos se multiplicam · desconto efetivo = conta do caixa · faixas = andares do prédio"),
          ("EP. 3", "a régua do custo: multiplique os fatores · só %? o custo vale 100")]
IND_CUES = ["03.a", "03.b", "04.a"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 380 + k * 580
        y = 200
        rrect(c, x - 260, y, 520, 610, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 260, y, 520, 610), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 235, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 200, 0.85, a)
        yy = y + 370
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 28, "black", INK if on_ else INK2, a, 460, 34, align="center") + 16


ONDE = [("05.a", "CIÊNCIAS HUMANAS", "imposto embutido: % de qual preço?"),
        ("05.b", "GRÁFICOS", "variação sobre qual valor?"),
        ("05.c", "MAT. FINANCEIRA", "à vista · “sem juros” (séries próprias)"),
        ("05.d", "FUNÇÕES POR PARTES", "as faixas (série própria)")]


def onde_icone(c, k, cx, cy, a):
    if a <= 0:
        return
    if k == 0:      # etiqueta com imposto
        c.save(); c.translate(cx, cy); etiqueta(c, a, "+ imposto", BLUE, 240, 100); c.restore()
    elif k == 1:    # barras com seta de variação
        for j, h in enumerate((70, 100, 130)):
            rrect(c, cx - 80 + j * 55, cy + 60 - h, 40, h, 4, mix("#FFFFFF", BLUE, 0.5), a)
        arrow(c, cx - 70, cy - 30, cx + 80, cy - 90, AMBER, a, 5, 14)
        text_mid(c, "+ ?%", cx + 70, cy - 120, 28, "black", AMBER, a)
    elif k == 2:    # cartão com parcelas
        rrect(c, cx - 100, cy - 60, 200, 124, 14, "#3D5A80", a, shadow=True)
        rrect(c, cx - 100, cy - 34, 200, 22, 0, INK, a)
        text_mid(c, "10 ×", cx, cy + 26, 36, "black", "#FFFFFF", a)
    else:           # escada de faixas (função por partes)
        line(c, cx - 100, cy + 70, cx + 100, cy + 70, INK2, a, 3); line(c, cx - 100, cy + 70, cx - 100, cy - 80, INK2, a, 3)
        p = skia.Path(); p.moveTo(cx - 100, cy + 50); p.lineTo(cx - 40, cy + 50); p.lineTo(cx - 40, cy)
        p.lineTo(cx + 20, cy); p.lineTo(cx + 20, cy - 60); p.lineTo(cx + 90, cy - 60)
        c.drawPath(p, paint(PURPLE, a, stroke=6))


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ NO BALCÃO", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, sub) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 240 + d, 380, 470, 24, mix("#F7F7F5", BLUE, 0.06), a)
        onde_icone(c, k, x, 390 + d, a)
        text(c, tit, x, 550 + d, 30, "black", BLUE, a)
        para(c, sub, x, 600 + d, 24, "bold", INK2, a, 330, 30, align="center")


HABITOS = [("06.a", "1", "A BASE AO LADO", "“25% do custo” · “10% da venda”"),
           ("06.b", "2", "PREÇO DE 100", "100 → 160 → 112"),
           ("06.c", "3", "DESCONFIE DA SOMA", "bases diferentes? · use fatores"),
           ("06.d", "4", "CONFIRA EM REAIS", "lucro ÷ base pedida")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "QUATRO HÁBITOS", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 250 + d, 380, 480, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=GREEN)
        para(c, tit, x, 430 + d, 36, "black", GREEN, a, 330, 44, align="center")
        for j, ln in enumerate(sub.split(" · ")):
            sz = 28
            while ftw(ln, sz, "bold") > 340:
                sz -= 1
            ftext(c, ln, x, 590 + d + j * 44, sz, "bold", INK, a)


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
    ("lucro R$ 20 · venda R$ 100", "25% da venda", False, "25% aparece mesmo: é do CUSTO",
     "toda % tem dono · lucro ÷ venda", "20% da venda", 0),
    ("custo R$ 90 · 25% sobre a VENDA", "preço R$ 120", True, "a mão vai para 90 × 1,25 = 112,50",
     "a margem é a fatia dentro da pizza · divida", "90 ÷ 0,75 = 120", 0),
    ("−20% e depois −10%", "= −30%", False, "20 + 10 = 30",
     "carimbos se multiplicam · 0,8 × 0,9 = 0,72", "−28%", 1),
    ("paguei R$ 72 depois de −20%", "o preço era R$ 90", True, "muitos fazem 72 × 1,2 = 86,40",
     "para voltar, divida pelo fator", "72 ÷ 0,8 = 90", 1),
    ("“2ª unidade com 50%”", "= 50% de desconto", False, "o cartaz grita 50",
     "a conta do caixa · leva 2, paga 1,5", "25% no par", 1),
    ("desconto por faixas", "a taxa mais alta vale para tudo", False, "“comprei na faixa dos 20%”",
     "cada andar com a sua taxa · só a parte dentro da faixa", "faixa por faixa", 3),
    ("2 peças a R$ 240 · +20% e −20%", "empatou", False, "+20 e −20 parecem se anular",
     "os custos são diferentes: 200 e 300 · pagou 500, recebeu 480", "prejuízo de R$ 20", 2),
    ("lucro 50% do custo · imposto 10% da venda", "sobra 40%", False, "50 − 10 = 40",
     "bases diferentes: calcule em reais · custo 100 → venda 150 → imposto 15", "sobra 35%", 2),
    ("margem sobre a VENDA", "nunca passa de 100%", True, "markup de 200% existe",
     "markup vai em cima do custo · a fatia nunca é a pizza inteira", "> 100%? elimine", 0),
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
        c.save(); c.translate(W / 2 - 20, 770); c.scale(1.1, 1.1); etiqueta(c, ab, "DE QUÊ?", AMBER, 300, 110); c.restore()


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · pad: a ideia · passos: (cue, texto) · confere: (cue, texto) ou None

Q = {
    "q1": dict(ids=("18", "19"), titulo="A BOLSA DA LOJA", area="LUCRO SOBRE A VENDA", ic=0, ok="B",
               enun=[("a", "Uma loja compra uma bolsa por R$ 150,00 e a vende por R$ 200,00.", False),
                     ("b", "O lucro, em porcentagem DO PREÇO DE VENDA, é de", True)],
               alts=[("A", "≈ 33,3%", "dividiu pelo custo", AMBER), ("B", "25%", "", GREEN),
                     ("C", "50%", "R$ 50 lido como 50%", RED), ("D", "75%", "custo ÷ venda", RED),
                     ("E", "≈ 133%", "venda ÷ custo", RED)],
               pad="de quê? DA VENDA", passos=[("a", "lucro: 200 − 150 = R$ 50,00"),
                                               ("b", "50 ÷ 200 = 0,25 = 25% da venda")],
               confere=None),
    "q2": dict(ids=("20", "21"), titulo="O BOLO NO APLICATIVO", area="PREÇO COM TAXA SOBRE A VENDA", ic=1, ok="E",
               enun=[("a", "Uma doceira quer receber R$ 45,00 líquidos por bolo. O aplicativo fica com 25% do preço "
                           "de venda.", False),
                     ("b", "O bolo deve custar", True)],
               alts=[("A", "R$ 56,25", "multiplicou por 1,25", AMBER), ("B", "R$ 70,00", "somou 25 reais", RED),
                     ("C", "R$ 33,75", "tirou 25% dos 45", RED), ("D", "R$ 180,00", "÷ 0,25: a fatia do app", RED),
                     ("E", "R$ 60,00", "", GREEN)],
               pad="a fatia do app está DENTRO do preço", passos=[("a", "sobra para ela: 100% − 25% = 75%"),
                                                                   ("b", "45 ÷ 0,75 = R$ 60,00")],
               confere=("v", "25% de 60 = 15 · 60 − 15 = 45")),
    "q3": dict(ids=("22", "23"), titulo="QUAL PROMOÇÃO?", area="DESCONTO EFETIVO", ic=2, ok="C",
               enun=[("a", "Você leva 4 unidades de R$ 20,00. I: leve 4, pague 3. II: 2ª unidade com 30%. "
                           "III: 20% em tudo.", False),
                     ("b", "O maior desconto efetivo é o da", True)],
               alts=[("A", "II, 30%", "30% sobre tudo", RED), ("B", "I, ≈ 33%", "grátis ÷ pagas", AMBER),
                     ("C", "I, 25%", "", GREEN), ("D", "II, 60%", "somou 30% + 30%", RED),
                     ("E", "I, 75%", "leu 3/4 como desconto", AMBER)],
               pad="conta do caixa: paga quanto pelos R$ 80?", passos=[("a", "I: paga R$ 60,00 → 25%"),
                                                                       ("b", "II: 2 × 34 = R$ 68,00 → 15%"),
                                                                       ("c", "III: paga R$ 64,00 → 20%")],
               confere=None),
    "q4": dict(ids=("24", "25"), titulo="O PRÉDIO DAS FAIXAS", area="DESCONTO POR FAIXA", ic=3, ok="A",
               enun=[("a", "Desconto por faixa: nada até R$ 100,00 · 10% de R$ 100,00 a R$ 300,00 · 20% acima de "
                           "R$ 300,00.", False),
                     ("b", "Numa compra de R$ 450,00, o cliente paga", True)],
               alts=[("A", "R$ 400,00", "", GREEN), ("B", "R$ 360,00", "20% sobre tudo", RED),
                     ("C", "R$ 315,00", "30%: somou as taxas", RED), ("D", "R$ 420,00", "só o último andar", AMBER),
                     ("E", "R$ 380,00", "20% de tudo acima de 100", AMBER)],
               pad="cada andar com a sua taxa", passos=[("a", "até 100: 0 · 100 a 300: 10% de 200 = 20"),
                                                         ("b", "acima de 300: 20% de 150 = 30"),
                                                         ("c", "desconto R$ 50,00 → paga R$ 400,00")],
               confere=None),
    "q5": dict(ids=("26", "27"), titulo="A LIQUIDAÇÃO", area="REMARCAÇÃO + LIQUIDAÇÃO", ic=4, ok="D",
               enun=[("a", "A etiqueta tem 80% sobre o custo. Na liquidação, 40% de desconto sobre a etiqueta.", False),
                     ("b", "Em relação ao custo, a loja teve", True)],
               alts=[("A", "lucro de 40%", "80 − 40", RED), ("B", "lucro de 48%", "descontou só a margem", AMBER),
                     ("C", "lucro de 108%", "leu o fator", AMBER), ("D", "lucro de 8%", "", GREEN),
                     ("E", "prejuízo de 8%", "“desconto grande = prejuízo”", RED)],
               pad="só porcentagens? o custo vale 100", passos=[("a", "etiqueta: 100 × 1,8 = 180"),
                                                                 ("b", "liquidação: 180 × 0,6 = 108"),
                                                                 ("c", "108 − 100 = lucro de 8% do custo")],
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
        area_icone(c, d["ic"], 700, 222, 0.44, a0)
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
                pill(c, "DE QUÊ?", 190, 260, PURPLE, size=18, a=ad, bounds=(0, 1920))
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

CHECK = [("28.b", "EP. 1", ["lucro e prejuízo: L = V − C", "% sobre o custo e sobre a venda", "sem aviso: sobre o custo",
                            "converter margem custo ↔ venda", "formar o preço (× ou ÷)", "imposto e comissão sobre a venda"]),
         ("28.c", "EP. 2", ["encadear fatores · desconto total", "preço original: ÷ fator",
                            "promoções → desconto efetivo", "faixas: cada taxa na sua parte"]),
         ("29.a", "EP. 3", ["remarcação + liquidação: sobrou lucro?", "lucro p% e prejuízo p%: prejuízo"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["28.a"], 0.5) * (1 - ep(t, C["28.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(170, 200), (990, 200), (990, 480)]
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
        boxed(c, 170, 640, 720, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 530, 690, 32, "black", INK, ae)


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
        icone(c, 0, 400, 660, 0.55, ac)
        c.save(); c.translate(620, 660); etiqueta(c, ac, "imposto", BLUE, 220, 90); c.restore()
        text_mid(c, "misture duas bases:", 1200, 620, 32, "bold", INK2, ac)
        text_mid(c, "lucro do CUSTO · imposto da VENDA", 1200, 690, 38, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Taxas equivalentes e inflação", W / 2, 330, 60, "black", PURPLE, aa)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        boxed(c, W / 2 - 420, 420, 840, 120, AMBER, ab, 0.10)
        text_mid(c, "10% ao mês ≠ 120% ao ano", W / 2, 480, 50, "black", INK, ab)
    ac = ep(t, C["31.c"], 0.5)
    chip(c, "rende 10%", 720, 660, GREEN, ac, 42)
    chip(c, "inflação 10%", 1200, 660, RED, ep(t, C["31.c"] + 0.6, 0.4), 42)
    ad = ep(t, C["31.d"], 0.5)
    text(c, "ficou mais rico?", W / 2, 800, 52, "black", AMBER, ad)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
