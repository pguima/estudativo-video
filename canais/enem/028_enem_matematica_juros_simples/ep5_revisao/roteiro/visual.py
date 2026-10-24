"""Visual — Juros Simples, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): pilha de notas com moedinhas iguais · fichas de unidade com
bandeirinhas · escada de degraus iguais · mesa de quatro pernas.
Ícones de contexto nas questões (area_icone()): cofrinho · calendário · boleto (conta de água) · gráfico/tabela · ampulheta.
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
_s = importlib.util.spec_from_file_location("comum028", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_simples_ep5_revisao.mp4"
CARD_R = K.CARD_R
NOTA = "#7FBF8E"
NOTA2 = "#5FA371"
MOEDA = "#F2B632"
MOEDA2 = "#C98E12"
MADEIRA = "#C98F5A"
MADEIRA2 = "#9C6A3B"
AGUA = "#5FA8E8"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças
# ======================================================================

def nota(c, x, y, w, h, a):
    rrect(c, x, y, w, h, 8, NOTA, a, shadow=True)
    rrect(c, x + 8, y + 8, w - 16, h - 16, 6, NOTA2, a * 0.35)
    c.drawCircle(x + w / 2, y + h / 2, h * 0.28, paint("#FFFFFF", a * 0.6))
    text_mid(c, "R$", x + w / 2, y + h / 2, h * 0.32, "black", NOTA2, a)


def moeda(c, cx, cy, r, a, s=""):
    if a <= 0:
        return
    c.drawCircle(cx, cy + 3, r, paint(MOEDA2, a))
    c.drawCircle(cx, cy, r, paint(MOEDA, a))
    c.drawCircle(cx, cy, r * 0.76, paint(MOEDA2, a, stroke=max(2, r * 0.08)))
    if s:
        text_mid(c, s, cx, cy, r * 0.8, "black", INK, a)


def ficha(c, cx, cy, s, flag, a, w=170, h=96):
    """ficha de unidade com bandeirinha (cor da bandeira = a 'língua' da unidade)"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 14, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 14, 14), paint(INK2, a, stroke=2.5))
    line(c, cx + w / 2 - 26, cy - h / 2, cx + w / 2 - 26, cy - h / 2 - 54, INK2, a, 3)
    p = skia.Path(); p.moveTo(cx + w / 2 - 26, cy - h / 2 - 54); p.lineTo(cx + w / 2 + 22, cy - h / 2 - 42)
    p.lineTo(cx + w / 2 - 26, cy - h / 2 - 30); p.close()
    c.drawPath(p, paint(flag, a))
    fmid(c, s, cx, cy, h * 0.4, "black", INK, a)


def escada(c, x, base, n, dw, dh, a, col=GREEN, rot=True):
    """escada de n degraus iguais"""
    if a <= 0:
        return
    p = skia.Path(); p.moveTo(x, base)
    for k in range(n):
        p.lineTo(x + k * dw, base - (k + 1) * dh); p.lineTo(x + (k + 1) * dw, base - (k + 1) * dh)
    p.lineTo(x + n * dw, base); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.30), a))
    c.drawPath(p, paint(col, a, stroke=4))
    if rot:
        for k in range(1, n):
            text(c, "+", x + k * dw - 16, base - (k + 1) * dh + dh * 0.62, dh * 0.5, "black", col, a)


def mesa(c, cx, cy, s, a, letras=("C", "i", "t", "J"), falta=3):
    """mesa de quatro pernas: o tampo é J = C·i·t; a perna 'falta' é a que se descobre"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    rrect(c, -170, -70, 340, 46, 12, MADEIRA, a, shadow=True)
    xs = (-140, -60, 60, 140)
    cols = (BLUE, PURPLE, AMBER, GREEN)
    for k, (x, L) in enumerate(zip(xs, letras)):
        if k == falta:
            c.drawRect(skia.Rect.MakeXYWH(x - 14, -24, 28, 130), paint(cols[k], a, stroke=3))
            text_mid(c, "?", x, 140, 44, "black", cols[k], a)
        else:
            rrect(c, x - 14, -24, 28, 130, 4, MADEIRA2, a)
            text_mid(c, L, x, 140, 40, "black", cols[k], a)
    c.restore()


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 pilha de notas parada + moedinhas iguais
        for j in range(5):
            nota(c, -190 + (j % 2) * 6, 40 - j * 20, 180, 54, a)
        for j in range(3):
            moeda(c, 70 + j * 62, 64, 28, a, "30")
        arrow(c, 70, -60, 70, 18, MOEDA2, a, 4, 10)
    elif k == 1:    # ep2 fichas com bandeirinhas: mesma língua
        ficha(c, -100, 30, "a.m.", BLUE, a)
        ficha(c, 100, 30, "meses", BLUE, a)
        text_mid(c, "=", 0, 30, 50, "black", GREEN, a)
    elif k == 2:    # ep3 escada de degraus iguais
        escada(c, -170, 90, 4, 85, 46, a)
        c.drawCircle(-170, 90 - 46, 9, paint(BLUE, a))
    elif k == 3:    # ep4 mesa de quatro pernas
        mesa(c, 0, -10, 1.0, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones de contexto: cofrinho · calendário · boleto · tabela · ampulheta"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # cofrinho
        c.drawOval(skia.Rect.MakeXYWH(-90, -55, 180, 120), paint("#F4A7B9", a))
        c.drawOval(skia.Rect.MakeXYWH(-90, -55, 180, 120), paint("#C96A84", a, stroke=3))
        rrect(c, -30, -62, 60, 10, 5, INK, a)
        rrect(c, 78, -10, 26, 34, 10, "#F4A7B9", a)
        for x in (-55, 40):
            rrect(c, x, 55, 22, 26, 6, "#C96A84", a)
        moeda(c, 0, -92, 22, a)
    elif k == 1:    # calendário
        rrect(c, -80, -70, 160, 150, 14, "#FFFFFF", a, shadow=True)
        rrect(c, -80, -70, 160, 40, 14, RED, a)
        for i in range(4):
            for j in range(3):
                rrect(c, -64 + i * 34, -18 + j * 30, 26, 22, 4, mix("#FFFFFF", BLUE, 0.25), a)
        text_mid(c, "360", 0, -50, 24, "black", "#FFFFFF", a)
    elif k == 2:    # boleto da conta de água
        rrect(c, -75, -85, 150, 175, 10, "#FFFFFF", a, shadow=True)
        p = skia.Path(); p.moveTo(-35, -60); p.quadTo(-58, -25, -35, -15); p.quadTo(-12, -25, -35, -60); p.close()
        c.drawPath(p, paint(AGUA, a))
        for j in range(3):
            line(c, -5, -52 + j * 16, 55, -52 + j * 16, GRAY, a, 3)
        for j in range(14):
            line(c, -58 + j * 8.5, 30, -58 + j * 8.5, 70, INK, a, 2 + (j % 3))
        selo(c, 30, 0, a, "ATRASO", RED, -12, 18)
    elif k == 3:    # tabela + escadinha
        rrect(c, -90, -70, 180, 150, 10, "#FFFFFF", a, shadow=True)
        for j in range(1, 4):
            line(c, -90, -70 + j * 37.5, 90, -70 + j * 37.5, LIGHT, a, 2)
        line(c, -20, -70, -20, 80, LIGHT, a, 2)
        escada(c, 0, 66, 3, 26, 30, a, GREEN, rot=False)
    elif k == 4:    # ampulheta
        p = skia.Path(); p.moveTo(-55, -80); p.lineTo(55, -80); p.lineTo(6, 0); p.lineTo(55, 80); p.lineTo(-55, 80)
        p.lineTo(-6, 0); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", AGUA, 0.25), a)); c.drawPath(p, paint(INK2, a, stroke=4))
        q = skia.Path(); q.moveTo(-34, -48); q.lineTo(34, -48); q.lineTo(4, -4); q.lineTo(-4, -4); q.close()
        c.drawPath(q, paint(MOEDA, a))
        r = skia.Path(); r.moveTo(-48, 76); r.lineTo(48, 76); r.lineTo(0, 40); r.close()
        c.drawPath(r, paint(MOEDA, a))
        for y in (-84, 84):
            rrect(c, -66, y - 6, 132, 12, 6, MADEIRA2, a)
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def nb(s):
    """espaço rígido: não quebra 'R$ 6.000,00', '15 %' nem número + unidade"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(%|meses|mês|dias|anos|ano|reais)\b)", " ", s)
    return s


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    for k, (cue, s, col) in enumerate((("01.a", "BOLETO ATRASADO", RED), ("01.a", "COMPRA PARCELADA", AMBER),
                                       ("01.a", "EMPRÉSTIMO", BLUE))):
        a = ep(t, C[cue] + 0.9 * k, 0.4)
        area_icone(c, (2, 3, 0)[k], 520 + k * 440, 330, 0.9, a)
        text(c, s, 520 + k * 440, 480, 30, "black", col, a)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        fmid(c, "“calcule os juros simples”", W / 2, 580, 44, "black", INK2, ab)
        w = ftw("“calcule os juros simples”", 44)
        strike(c, W / 2 - w / 2 - 10, 584, W / 2 + w / 2 + 10, 584, ab, RED, ep(t, C["01.b"] + 1.2, 0.5))
    ac = ep(t, C["01.c"], 0.5)
    text(c, "a conversão está escondida na história", W / 2, 680, 40, "black", AMBER, ac)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 790, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 790, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


COBRA = [("02.a", "JUROS OU MONTANTE", "com conversão de unidade", 1, BLUE),
         ("02.b", "TAXA, CAPITAL OU PRAZO", "descobrir a letra que falta", 4, PURPLE),
         ("02.c", "MULTA E JUROS DE MORA", "a conta atrasada", 2, RED),
         ("02.d", "GRÁFICO OU TABELA", "crescimento em reta", 3, GREEN),
         ("02.e", "COMPRA COM ENTRADA", "a taxa escondida", 0, AMBER)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "AS HISTÓRIAS DA PROVA", "O QUE O ENEM COBRA", BLUE)
    for k, (cue, tit, sub, ic, col) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 230 + d, 330, 520, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 285 + d, a, 26, bg=col)
        if ic == 4:
            mesa(c, x, 420 + d, 0.62, a)
        else:
            area_icone(c, ic, x, 420 + d, 0.85, a)
        para(c, tit, x, 590 + d, 28, "black", col, a, 300, 34, align="center")
        para(c, sub, x, 680 + d, 23, "bold", INK2, a, 290, 30, align="center")


INDICE = [("EP. 1", "aluguel do dinheiro · sempre sobre o capital · a conta de um mês só · J acréscimo · M total"),
          ("EP. 2", "taxa e tempo: mesma língua · traduza só um · multa = ingresso · mora = taxímetro"),
          ("EP. 3", "escada de degraus iguais · a reta começa no capital · taxa = degrau ÷ capital"),
          ("EP. 4", "mesa de 4 pernas · M já tem o C dentro · a entrada não é empréstimo")]
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
        rrect(c, x - 210, y, 420, 610, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 210, y, 420, 610), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 185, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 200, 0.8, a)
        for j, ln in enumerate(s.split(" · ")):
            sz = 27
            while ftw(ln, sz) > 380:
                sz -= 1
            ftext(c, ln, x, y + 380 + j * 44, sz, "black", INK if on_ else INK2, a)


ONDE = [("05.a", "ÁLGEBRA", "função afim · PA (séries próprias)"), ("05.b", "FÍSICA", "movimento uniforme: s = s₀ + v·t"),
        ("05.c", "PORCENTAGEM", "e regra de três"), ("05.d", "HUMANAS", "endividamento · crédito · mora")]


def onde_icone(c, k, cx, cy, a):
    if a <= 0:
        return
    if k == 0:      # reta subindo de um ponto no eixo
        line(c, cx - 90, cy + 70, cx + 90, cy + 70, INK2, a, 3)
        line(c, cx - 90, cy + 70, cx - 90, cy - 80, INK2, a, 3)
        line(c, cx - 90, cy + 20, cx + 80, cy - 60, GREEN, a, 6)
        c.drawCircle(cx - 90, cy + 20, 10, paint(BLUE, a))
    elif k == 1:    # carrinho em movimento
        rrect(c, cx - 80, cy - 30, 160, 60, 14, BLUE, a, shadow=True)
        for x in (cx - 45, cx + 45):
            c.drawCircle(x, cy + 34, 18, paint(INK, a))
        for j in range(3):
            line(c, cx - 140, cy - 20 + j * 20, cx - 100, cy - 20 + j * 20, GRAY, a, 4)
    elif k == 2:
        fmid(c, "%", cx, cy, 120, "black", PURPLE, a)
    else:           # jornal / gráfico de endividamento
        rrect(c, cx - 80, cy - 80, 160, 160, 10, "#FFFFFF", a, shadow=True)
        for j in range(4):
            rrect(c, cx - 60 + j * 32, cy + 60 - (j + 1) * 26, 22, (j + 1) * 26, 3, RED, a)
        line(c, cx - 60, cy - 60, cx + 60, cy - 60, INK2, a, 5)


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ MATEMÁTICA FINANCEIRA", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, sub) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 190, 240 + d, 380, 470, 24, mix("#F7F7F5", BLUE, 0.06), a)
        onde_icone(c, k, x, 390 + d, a)
        text(c, tit, x, 550 + d, 32, "black", BLUE, a)
        para(c, sub, x, 600 + d, 24, "bold", INK2, a, 330, 30, align="center")


HABITOS = [("06.a", "1", "SUBLINHE AS UNIDADES", "a.m.? a.a.? · dias? meses?"),
           ("06.b", "2", "JUROS OU MONTANTE?", "circule o que pedem"),
           ("06.c", "3", "UM PERÍODO", "calcule C·i · e multiplique"),
           ("06.d", "4", "ORDEM DE GRANDEZA", "poucos meses · poucos %")]


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
            ftext(c, ln, x, 590 + d + j * 44, 28, "bold", INK, a)


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
    ("18% ao ano · 8 meses", "J = C · 0,18 · 8", False, "os números estão no enunciado",
     "taxa anual não conversa com meses", "C · 0,015 · 8", 1),
    ("2% a.m. · 2 anos", "24% a.a. e 24 meses", False, "parece capricho: converteu tudo",
     "converta só um · os dois: 12 vezes errado (para + ou para −)", "2% e 24 meses", 1),
    ("pegou R$ 1.000 · devolveu R$ 1.120", "juros = R$ 120", True, "o número que aparece é 1.120",
     "juros é só o acréscimo · M é o total", "J = 120 · M = 1.120", 0),
    ("taxa de 1,5%", "entra como 0,15", False, "os algarismos são os mesmos",
     "0,15 é 15% · ande duas casas", "1,5% = 0,015", 0),
    ("achar a taxa", "i = J ÷ (M · t)", False, "o montante é o número maior",
     "o aluguel é sobre o capital", "i = J ÷ (C · t)", 3),
    ("triplicar o capital", "juros = 2 × capital", True, "triplicar lembra o 3",
     "M já tem o C dentro · i·t = k − 1", "M = C + 2C", 3),
    ("1 ano e 3 meses", "= 1,3 ano", False, "é assim que se escreve",
     "mês não é décimo de ano", "15 meses = 1,25 ano", 1),
    ("conta paga com atraso", "multa + juros de mora", True, "parece cobrar duas vezes",
     "multa = ingresso (uma vez) · mora = taxímetro (por dia)", "as duas", 1),
    ("2% ao mês", "= 2 ÷ 12 ao ano", False, "o ano tem 12 meses",
     "em um ano cabem 12 aluguéis · período maior, taxa maior", "24% ao ano", 1),
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
    text(c, nb(ctx).upper(), 960, 310, 30, "black", INK2, a0)
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
        ftext(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        lns = regra_.split(" · ")
        for j, ln in enumerate(lns):
            szr = 30
            while ftw(ln, szr) > 860:
                szr -= 1
            ftext(c, ln, 240, 705 + (j - (len(lns) - 1) / 2) * 44, szr, "black", GREEN, ag, align="left")
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
        ficha(c, 820, 760, "taxa", BLUE, ab, 170, 80)
        ficha(c, 1100, 760, "tempo", BLUE, ab, 170, 80)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · pad: a ideia · passos: (cue, texto) · confere: (cue, texto) ou None

Q = {
    "q1": dict(ids=("18", "19"), titulo="A APLICAÇÃO", area="TAXA ANUAL, PRAZO EM MESES", ic=0, ok="E",
               enun=[("a", "Uma pessoa aplicou R$ 6.000,00 a juros simples de 15% ao ano, por 10 meses.", False),
                     ("b", "Os juros recebidos foram de", True)],
               alts=[("A", "R$ 75,00", "um mês só", AMBER), ("B", "R$ 6.750,00", "é o montante", AMBER),
                     ("C", "R$ 900,00", "um ano inteiro", AMBER), ("D", "R$ 9.000,00", "taxa anual × meses", RED),
                     ("E", "R$ 750,00", "", GREEN)],
               pad="ao ANO × MESES: traduza a taxa", passos=[("a", "15% ÷ 12 = 1,25% a.m. · 1 mês: R$ 75,00"),
                                                             ("b", "10 meses: R$ 750,00")],
               confere=("v", "1 ano daria R$ 900: 10 meses, menos")),
    "q2": dict(ids=("20", "21"), titulo="O PRAZO EM DIAS", area="ANO COMERCIAL", ic=1, ok="B",
               enun=[("a", "Um empréstimo de R$ 3.600,00, a 30% ao ano, foi pago em 40 dias. Use o ano comercial.", False),
                     ("b", "Os juros foram de", True)],
               alts=[("A", "R$ 43.200,00", "dias como anos", RED), ("B", "R$ 120,00", "", GREEN),
                     ("C", "R$ 3.720,00", "é o montante", AMBER), ("D", "R$ 3.600,00", "dias como meses", RED),
                     ("E", "R$ 118,36", "ano de 365 dias", AMBER)],
               pad="ano comercial: 360 dias", passos=[("a", "1 ano: R$ 1.080,00 · ÷ 360 = R$ 3,00 por dia"),
                                                      ("b", "40 dias: R$ 120,00")],
               confere=None),
    "q3": dict(ids=("22", "23"), titulo="A CONTA DE ÁGUA", area="MULTA E JUROS DE MORA", ic=2, ok="D",
               enun=[("a", "Uma conta de água de R$ 180,00 foi paga com 20 dias de atraso. Multa de 2% e juros de mora "
                           "de 1% ao mês, proporcionais aos dias.", False),
                     ("b", "O valor pago foi", True)],
               alts=[("A", "R$ 181,20", "esqueceu a multa", RED), ("B", "R$ 183,60", "esqueceu os juros", RED),
                     ("C", "R$ 185,40", "mês inteiro de juros", AMBER), ("D", "R$ 184,80", "", GREEN),
                     ("E", "R$ 219,60", "1% por DIA", AMBER)],
               pad="ingresso + taxímetro", passos=[("a", "multa: 2% de 180 = R$ 3,60"),
                                                   ("b", "mora: 1 mês = R$ 1,80 · 20 dias = 2/3 → R$ 1,20"),
                                                   ("c", "180 + 3,60 + 1,20 = R$ 184,80")],
               confere=None),
    "q4": dict(ids=("24", "25"), titulo="A TABELA DE MONTANTES", area="GRÁFICO E TABELA", ic=3, ok="A",
               enun=[("a", "O montante de uma aplicação, mês a mês:", False),
                     ("b", "A taxa mensal é de", True)],
               tabela=[("mês 0", "2.500"), ("mês 1", "2.575"), ("mês 2", "2.650"), ("mês 3", "2.725")],
               alts=[("A", "3%", "", GREEN), ("B", "0,3%", "a vírgula", AMBER),
                     ("C", "cerca de 2,75%", "dividiu pelo montante", RED), ("D", "9%", "não dividiu pelos 3 meses", RED),
                     ("E", "75%", "leu o degrau como taxa", AMBER)],
               pad="degraus iguais: juros simples", passos=[("a", "degrau: R$ 75,00 por mês"),
                                                            ("b", "75 ÷ 2.500 = 0,03 = 3% a.m.")],
               confere=None),
    "q5": dict(ids=("26", "27"), titulo="QUANDO TRIPLICA?", area="DOBRAR E TRIPLICAR", ic=4, ok="C",
               enun=[("a", "A juros simples de 5% ao mês, em quanto tempo um capital triplica?", True)],
               alts=[("A", "5 anos", "J = 3C", RED), ("B", "1 ano e 8 meses", "só dobrou", AMBER),
                     ("C", "3 anos e 4 meses", "", GREEN), ("D", "3 anos e 3 meses", "3,33 ≠ 3 anos e 3 meses", AMBER),
                     ("E", "40 anos", "a taxa é AO MÊS", RED)],
               pad="M já tem o C dentro: J = 2C", passos=[("a", "0,05·t = 2 → t = 2 ÷ 0,05 = 40 meses"),
                                                          ("b", "40 meses = 3 anos e 4 meses")],
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


def tabela(c, linhas, x, y, a):
    """tabelinha mês × montante (R$), com os degraus aparecendo"""
    if a <= 0:
        return
    rrect(c, x, y, 560, 56 * len(linhas) + 56, 12, "#FFFFFF", a, shadow=True)
    rrect(c, x, y, 560, 56, 12, mix("#FFFFFF", BLUE, 0.2), a)
    text(c, "mês", x + 90, y + 38, 26, "black", BLUE, a)
    text(c, "montante (R$)", x + 360, y + 38, 26, "black", BLUE, a)
    for k, (m, v) in enumerate(linhas):
        yy = y + 56 + k * 56
        line(c, x + 10, yy, x + 550, yy, LIGHT, a, 2)
        text(c, m, x + 90, yy + 38, 28, "bold", INK2, a)
        text(c, v, x + 360, yy + 38, 30, "black", INK, a)


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
        area_icone(c, d["ic"], 760, 235, 0.5, a0)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
            if cue == "a" and d.get("tabela"):
                tabela(c, d["tabela"], 180, y, a)
                y += 56 * len(d["tabela"]) + 80
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            if ad > 0:
                boxed(c, 170, 260, 650, 84, PURPLE, ad, 0.08)
                pill(c, "PENSE", 190, 260, PURPLE, size=18, a=ad, bounds=(0, 1920))
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

CHECK = [("28.b", "EP. 1", ["C, i, t, J e M no enunciado", "J = C·i·t e M = C(1 + i·t)", "taxa na forma decimal"]),
         ("28.c", "EP. 2", ["taxa e tempo na mesma unidade", "taxas proporcionais (só nos simples)", "ano de 360 · mês de 30",
                            "“1 ano e 3 meses” = 15 meses", "multa e juros de mora"]),
         ("29.a", "EP. 3", ["montante = reta (função afim)", "PA de razão C · i"]),
         ("29.b", "EP. 4", ["isolar: divida pelo capital", "dobrar e triplicar: i·t = k − 1", "taxa com entrada"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["28.a"], 0.5) * (1 - ep(t, C["28.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(170, 200), (170, 400), (990, 200), (990, 360)]
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x + 40, y0 + 100, 0.22, a)
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 44
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            sz = 26
            while ftw(it, sz, "bold") > 640:
                sz -= 1
            K.ftext(c, it, x + 158, yy + 10, sz, "bold", INK, a, align="left")
    ae = ep(t, C["29.c"], 0.5)
    if ae > 0:
        boxed(c, 990, 640, 720, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1350, 690, 32, "black", INK, ae)


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
        for k, ic in enumerate((1, 2, 3)):
            area_icone(c, ic, 420 + k * 170, 660, 0.55, ac)
        text_mid(c, "de preferência:", 1250, 620, 32, "bold", INK2, ac)
        text_mid(c, "conversão · boleto · gráfico", 1250, 690, 40, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Juros compostos e montante", W / 2, 330, 62, "black", PURPLE, aa)
    ab = ep(t, C["31.b"], 0.5)
    chip(c, "JUROS SOBRE JUROS", W / 2, 440, AMBER, ab, 36)
    ac = ep(t, C["31.c"], 0.5)
    if ac > 0:
        x0, y0 = 520, 760
        line(c, x0, y0, x0 + 360, y0, INK2, ac, 3); line(c, x0, y0, x0, y0 - 220, INK2, ac, 3)
        line(c, x0, y0 - 40, x0 + 340, y0 - 150, GRAY, ac, 5)
        p = skia.Path(); p.moveTo(x0, y0 - 40)
        for k in range(1, 35):
            u = k / 34
            p.lineTo(x0 + 340 * u, y0 - 40 - 160 * (2.6 ** (u * 1.6) - 1) / (2.6 ** 1.6 - 1))
        c.drawPath(p, paint(PURPLE, ac, stroke=6))
        text(c, "reta → curva", x0 + 180, y0 + 50, 30, "black", PURPLE, ac)
    ad = ep(t, C["31.d"], 0.5)
    if ad > 0:
        text(c, "PA", 1180, 640, 64, "black", GRAY, ad)
        arrow(c, 1250, 620, 1340, 620, PURPLE, ad, 5, 14)
        text(c, "PG", 1410, 640, 64, "black", PURPLE, ad)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
