"""Visual — Expressões Algébricas e Produtos Notáveis, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, selo_teste...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): caixinha com x · quadrado dividido em quatro (a², ab, ab, b²) ·
tesoura cortando um fator · gêmeos na reta numérica ao redor do número redondo.
Ícones de contexto nas questões (area_icone()): celular de aplicativo · terreno com calçada · praça ampliada · fração ·
gramado. O selo "TESTE: x = …" aparece quando o teste do número resolve a questão.
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
_s = importlib.util.spec_from_file_location("comum034", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_expressoes_algebricas_ep5_revisao.mp4"
CARD_R = K.CARD_R
GRAMA = "#7BBF6A"
GRAMA2 = "#4E9A3E"
TERRA = "#E9D8B4"
CALCADA = "#C9C9C4"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def mx(c, s, x, cy, size, col=INK, a=1.0, align="left"):
    """linha matemática de uma cor só (expr)"""
    return K.mdraw(c, s, x, cy, size, col, a, align=align)


# ======================================================================
# peças
# ======================================================================

def caixinha(c, a):
    """a letra como caixinha: caixa com x e um número entrando com parênteses"""
    rrect(c, -90, -70, 180, 140, 18, mix("#FFFFFF", BLUE, 0.15), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-90, -70, 180, 140), 18, 18), paint(BLUE, a, stroke=5))
    fmid(c, "x", 0, 0, 96, "black", BLUE, a)
    fmid(c, "(−2)", 0, -112, 44, "black", GREEN, a)
    arrow(c, 0, -86, 0, -70, GREEN, a, 4, 10)


def quadrado4(c, a, lado=200, k=0.62):
    """quadrado (a + b)² dividido em a², ab, ab, b² (os dois retângulos ab em âmbar)"""
    x0, y0 = -lado / 2, -lado / 2
    p = lado * k
    q = lado - p
    rrect(c, x0, y0, p, p, 0, mix("#FFFFFF", BLUE, 0.35), a)
    rrect(c, x0 + p, y0, q, p, 0, mix("#FFFFFF", AMBER, 0.55), a)
    rrect(c, x0, y0 + p, p, q, 0, mix("#FFFFFF", AMBER, 0.55), a)
    rrect(c, x0 + p, y0 + p, q, q, 0, mix("#FFFFFF", PURPLE, 0.35), a)
    for (xx, yy, ww, hh) in ((x0, y0, p, p), (x0 + p, y0, q, p), (x0, y0 + p, p, q), (x0 + p, y0 + p, q, q)):
        c.drawRect(skia.Rect.MakeXYWH(xx, yy, ww, hh), paint(INK2, a, stroke=3))
    fmid(c, "a²", x0 + p / 2, y0 + p / 2, lado * 0.2, "black", BLUE, a)
    fmid(c, "ab", x0 + p + q / 2, y0 + p / 2, lado * 0.14, "black", AMBER, a)
    fmid(c, "ab", x0 + p / 2, y0 + p + q / 2, lado * 0.14, "black", AMBER, a)
    fmid(c, "b²", x0 + p + q / 2, y0 + p + q / 2, lado * 0.13, "black", PURPLE, a)


def tesoura(c, cx, cy, s, a, col=INK):
    """tesoura estilizada (duas lâminas e dois anéis)"""
    c.save(); c.translate(cx, cy); c.scale(s, s)
    for sgn in (1, -1):
        pth = skia.Path(); pth.moveTo(-10, 0); pth.lineTo(90, sgn * 26); pth.lineTo(96, sgn * 14); pth.close()
        c.drawPath(pth, paint(col, a))
        c.drawCircle(-34, -sgn * 22, 18, paint(col, a, stroke=7))
    c.drawCircle(0, 0, 6, paint("#FFFFFF", a))
    c.restore()


def fracao_corte(c, a):
    """fração (x+2)(x−2)/(x−2)² com a tesoura cortando o fator (x − 2)"""
    mx(c, "{(x+2)(x−2)}/{(x−2)^2}", 0, 0, 52, INK, a, align="center")
    strike(c, 18, -40, 130, -40, a, RED, a)
    tesoura(c, -215, -10, 0.7, a, RED)
    text_mid(c, "FATOR", 0, 105, 26, "black", GREEN, a)


def gemeos(c, a, centro="300", passo="2"):
    """reta numérica com os gêmeos ao redor do número redondo"""
    line(c, -200, 30, 200, 30, INK2, a, 4)
    for x, s, col in ((-130, f"{int(centro) - int(passo)}", BLUE), (0, centro, GREEN), (130, f"{int(centro) + int(passo)}", BLUE)):
        line(c, x, 18, x, 42, INK2, a, 4)
        text_mid(c, s, x, 80, 34, "black", col, a)
    for x in (-130, 130):
        c.drawCircle(x, -30, 26, paint(mix("#FFFFFF", BLUE, 0.4), a))
        c.drawCircle(x, -30, 26, paint(BLUE, a, stroke=4))
        c.drawCircle(x - 8, -34, 4, paint(INK, a)); c.drawCircle(x + 8, -34, 4, paint(INK, a))
    p = skia.Path(); p.moveTo(-104, -60); p.quadTo(0, -120, 104, -60)
    c.drawPath(p, paint(GREEN, a, stroke=4))
    text_mid(c, "± 2", 0, -100, 30, "black", GREEN, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:
        caixinha(c, a)
    elif k == 1:
        quadrado4(c, a)
    elif k == 2:
        fracao_corte(c, a)
    elif k == 3:
        gemeos(c, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones de contexto: celular de corrida · terreno com calçada · praça ampliada · fração · gramado"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # celular com o mapa da corrida
        rrect(c, -60, -100, 120, 200, 18, INK, a, shadow=True)
        rrect(c, -50, -84, 100, 168, 8, mix("#FFFFFF", BLUE, 0.12), a)
        p = skia.Path(); p.moveTo(-30, 60); p.lineTo(-30, 10); p.lineTo(20, 10); p.lineTo(20, -50)
        c.drawPath(p, paint(BLUE, a, stroke=6))
        c.drawCircle(-30, 60, 9, paint(GREEN, a)); c.drawCircle(20, -50, 9, paint(RED, a))
    elif k == 1:    # terreno quadrado com a faixa de calçada
        rrect(c, -100, -100, 200, 200, 0, CALCADA, a)
        rrect(c, -70, -70, 140, 140, 0, TERRA, a)
        c.drawRect(skia.Rect.MakeXYWH(-100, -100, 200, 200), paint(INK2, a, stroke=3))
        c.drawRect(skia.Rect.MakeXYWH(-70, -70, 140, 140), paint(AMBER, a, stroke=4))
    elif k == 2:    # praça ampliada: quadrado antigo + faixa nova em L
        rrect(c, -100, -100, 200, 200, 0, mix("#FFFFFF", AMBER, 0.45), a)
        rrect(c, -100, -100, 150, 150, 0, GRAMA, a)
        c.drawRect(skia.Rect.MakeXYWH(-100, -100, 200, 200), paint(INK2, a, stroke=3))
        c.drawCircle(-25, -25, 22, paint(GRAMA2, a))
    elif k == 3:    # fração
        rrect(c, -110, -90, 220, 180, 18, "#FFFFFF", a, shadow=True)
        line(c, -70, 0, 70, 0, PURPLE, a, 6)
        text_mid(c, "x² − 4", 0, -40, 40, "black", INK, a)
        text_mid(c, "x − 2", 0, 42, 40, "black", INK, a)
    elif k == 4:    # gramado com régua
        rrect(c, -120, -70, 240, 140, 8, GRAMA, a, shadow=True)
        for j in range(9):
            line(c, -100 + j * 25, 60, -96 + j * 25, 40, GRAMA2, a, 4)
        line(c, -120, 92, 120, 92, INK2, a, 4)
        text_mid(c, "302 m", 0, 124, 30, "black", INK, a)
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def nb(s):
    """espaço rígido: não quebra 'R$ 5,00', '6 m' nem '90 000'"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(m²|m|km|reais|metros)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
    return s


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 300, 205, 600, 120, 18, "#FFFFFF", aa, shadow=True)
        text_mid(c, "“FATORE”", W / 2, 265, 64, "black", INK2, aa)
        strike(c, W / 2 - 200, 268, W / 2 + 200, 268, ep(t, C["01.a"] + 2.0, 0.4), RED, aa)
    itens = (("CORRIDA DE APLICATIVO", 0, BLUE), ("TERRENO AMPLIADO", 2, AMBER), ("CONTA SEM CALCULADORA", 4, GREEN))
    for k, (s, ic, col) in enumerate(itens):
        a = ep(t, C["01.b"] + 1.3 * k, 0.4)
        area_icone(c, ic, 480 + k * 480, 500, 0.85, a)
        text(c, s, 480 + k * 480, 660, 30, "black", col, a)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        pill(c, "tire o disfarce", W / 2, 735, PURPLE, size=34, a=ac, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 840, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 840, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


COBRA = [("02.a", "MODELAR", "escrever a expressão de um custo", BLUE, "custo = 5 + 2x"),
         ("02.b", "COMPARAR EXPRESSÕES", "qual alternativa é equivalente?", PURPLE, "(a + b)² = ?"),
         ("02.c", "CALCULAR SEM CALCULADORA", "produtos notáveis de cabeça", GREEN, "302 · 298"),
         ("02.d", "SIMPLIFICAR ANTES", "fatore e a conta vira uma linha", AMBER, "corte fatores")]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "AS QUATRO COBRANÇAS", "O QUE O ENEM COBRA", BLUE)
    for k, (cue, tit, sub, col, ex) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 440
        rrect(c, x - 200, 240 + d, 400, 500, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 300 + d, a, 28, bg=col)
        para(c, tit, x, 380 + d, 32, "black", col, a, 340, 40, align="center")
        sz = 40
        while ftw(ex, sz) > 340:
            sz -= 2
        fmid(c, ex, x, 540 + d, sz, "black", INK, a)
        para(c, sub, x, 620 + d, 25, "bold", INK2, a, 330, 32, align="center")


def b_duas(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "DUAS HABILIDADES", GREEN)
    aa, da = rise(t, C["03.a"])
    if aa > 0:
        boxed(c, 160, 240 + da, 760, 520, BLUE, aa, 0.06)
        badge_num(c, 1, 230, 300 + da, aa, 28, bg=BLUE)
        text(c, "TRADUZIR COM CUIDADO", 270, 312 + da, 34, "black", BLUE, aa, align="left")
        text(c, "o dobro da soma", 540, 440 + da, 36, "bold", INK2, aa)
        mx(c, "2(x+3)", 540, 510 + da, 56, GREEN, aa, align="center")
        text(c, "a soma do dobro", 540, 610 + da, 36, "bold", INK2, aa)
        mx(c, "2x+3", 540, 680 + da, 56, AMBER, aa, align="center")
    ab, db = rise(t, C["03.b"])
    if ab > 0:
        boxed(c, 1000, 240 + db, 760, 520, PURPLE, ab, 0.06)
        badge_num(c, 2, 1070, 300 + db, ab, 28, bg=PURPLE)
        text(c, "O TERMO DO MEIO", 1110, 312 + db, 34, "black", PURPLE, ab, align="left")
        c.save(); c.translate(1380, 500 + db); c.scale(0.95, 0.95); quadrado4(c, ab); c.restore()
        text(c, "(a + b)² = a² + 2ab + b²", 1380, 700 + db, 38, "black", INK, ab)


INDICE = [("EP. 1", "a letra é uma caixinha: o número entra com parênteses · frutas iguais · aperto de mão · o menos é "
                    "um espelho"),
          ("EP. 2", "o quadrado tem dois retângulos ab · expoente barrado na porta da soma · teste de 10 segundos"),
          ("EP. 3", "corta-se fator, nunca termo · o L que vira retângulo"),
          ("EP. 4", "os gêmeos ao redor do número redondo")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 285 + k * 450
        y = 200
        rrect(c, x - 210, y, 420, 610, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 210, y, 420, 610), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 185, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 210, 0.8, a)
        yy = y + 370
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 27, "black", INK if on_ else INK2, a, 370, 33, align="center") + 14


ONDE = [("06.a", "FINANCEIRA", "1,1² = 1,21", "21%, não 20% · o 1% a mais é o i²"),
        ("06.b", "FÍSICA", "(2v)² = 4v²", "dobrou a velocidade · energia × 4"),
        ("07.c", "GEOMETRIA", "(x + k)² − x²", "a área ganha 2kx + k²"),
        ("07.d", "2º GRAU", "Bhaskara", "nasce do quadrado da soma · próxima série do bloco")]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ ÁLGEBRA", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, conta, sub) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 440
        rrect(c, x - 200, 240 + d, 400, 480, 24, mix("#F7F7F5", BLUE, 0.06), a)
        text(c, tit, x, 310 + d, 32, "black", BLUE, a)
        sz = 52
        while ftw(conta, sz) > 340:
            sz -= 2
        fmid(c, conta, x, 450 + d, sz, "black", PURPLE, a)
        yy = 560 + d
        for ln in sub.split(" · "):
            yy += para(c, ln, x, yy, 25, "bold", INK2, a, 340, 32, align="center") + 8


HABITOS = [("08.a", "1", "TESTE COM UM NÚMERO", "x = 2 no enunciado e nas alternativas · duas bateram? outro valor"),
           ("08.b", "2", "UMA FRASE DE CADA VEZ", "cada informação vira uma expressão · só depois junte"),
           ("08.c", "3", "CACE O TERMO DO MEIO", "sem 2ab ou com ab pela metade · é o sonho do calouro")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 250 + d, 500, 480, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=GREEN)
        para(c, tit, x, 420 + d, 36, "black", GREEN, a, 440, 44, align="center")
        yy = 560 + d
        for ln in sub.split(" · "):
            yy += para(c, ln, x, yy, 28, "bold", INK, a, 440, 36, align="center") + 12
        if k == 0:
            K.selo_teste(c, x + 170, 300 + d, a, True, "x = 2")


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["09.t"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["09.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["09.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["09.b"], 0.5), anchor="center")


# (contexto, afirmação em expr, verdadeira?, por que engana, regra certa, versão certa em expr, ícone)
VF = [
    ("quadrado da soma", "(a+b)^2 = a^2 + b^2", False, "parece que o expoente entra nas duas parcelas",
     "faltam os dois retângulos ab", "a^2 + 2ab + b^2", 1),
    ("quadrado da diferença", "(a−b)^2 = a^2 − b^2", False, "parece que o menos só se copia",
     "o b² continua positivo", "a^2 − 2ab + b^2", 1),
    ("sem parênteses", "−2^2 = −4", True, "2² é 4, e o sinal parece ir junto",
     "o expoente pega só o 2 · negativo na caixinha: use parênteses", "(−2)^2 = 4", 0),
    ("o menos antes do parêntese", "5 − (x−3) = 8 − x", True, "muita gente escreve 5 − x − 3",
     "o menos é um espelho: troca todos os sinais", "5 − x + 3", 0),
    ("somar termos", "2x + 3x^2 = 5x^3", False, "2 + 3 dá 5",
     "frutas diferentes não se juntam · só termos semelhantes", "2x + 3x^2", 0),
    ("o expoente na multiplicação", "(3x)^2 = 3x^2", False, "o quadrado parece ser só do x",
     "na multiplicação, o expoente entra", "9x^2", 1),
    ("simplificar", "{x+3}/3 = x", False, "tem 3 em cima e embaixo",
     "o 3 de cima é termo · corta-se fator, nunca termo", "{x+3}/3", 2),
    ("traduzir", "“o dobro da soma de x com 3” = 2x + 3", False, "a palavra dobro vem primeiro, colada no x",
     "primeiro a soma, depois o dobro", "2(x+3)", 0),
    ("diferença de quadrados", "x^2 − 16 = (x+4)(x−4)", True, "(x − 4)² parece a mesma coisa",
     "soma pela diferença · o L que vira retângulo", "≠ (x−4)^2", 2),
]
VF_IDS = [f"{10 + k:02d}" for k in range(9)]


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
    text(c, ctx.upper(), 960, 300, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    if conta.startswith("“"):
        sz = 48
        while ftw(conta, sz) > 760:
            sz -= 2
        fmid(c, conta, 960, 410, sz, "black", INK, a0)
        w = ftw(conta, sz)
    else:
        sz = 66
        while K.math_w(conta, sz) > 720:
            sz -= 2
        w = mx(c, conta, 960, 410, sz, INK, a0, align="center")
    if ar > 0 and not ver:
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
        ftext(c, engana, 640 if ver else 520, 552, sze, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        lns = regra_.split(" · ")
        for j, ln in enumerate(lns):
            szr = 30
            while ftw(ln, szr) > 820:
                szr -= 1
            ftext(c, ln, 240, 705 + (j - (len(lns) - 1) / 2) * 44, szr, "black", GREEN, ag, align="left")
        szf = 52
        while K.math_w(fix, szf) > 520:
            szf -= 2
        mx(c, fix, 1420, 715, szf, GREEN, ag, align="center")


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["19.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["19.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 140 + k * 140
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["19.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    if ab > 0:
        boxed(c, W / 2 - 360, 700, 720, 110, GREEN, ab, 0.08)
        text_mid(c, "confira trocando x por um número", W / 2, 755, 38, "black", GREEN, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto ou "=expr", destaque?) · pad: a ideia · passos: (cue, texto ou "=expr") · confere: (cue, texto) ou None
# teste: (cue, rótulo) do selo "TESTE: x = …" quando o teste do número decide

Q = {
    "q1": dict(ids=("20", "21"), titulo="AS DUAS CORRIDAS", area="MODELAGEM", ic=0, ok="D",
               enun=[("a", "Um aplicativo cobra R$ 5,00 de bandeirada em cada corrida, mais R$ 2,00 por km. Uma "
                           "pessoa fez duas corridas: a 1ª com x km e a 2ª com 3 km a mais que a 1ª.", False),
                     ("b", "O valor total das duas corridas, em reais, é", True)],
               alts=[("A", "=4x+13", "2x + 3: sem parênteses", AMBER), ("B", "=4x+11", "1 bandeirada só", RED),
                     ("C", "=4x+10", "esqueceu os 3 km", RED), ("D", "=4x+16", "", GREEN),
                     ("E", "=20x", "juntou frutas diferentes", RED)],
               pad="uma frase de cada vez",
               passos=[("a", "=corrida 1: 5+2x"), ("b", "=corrida 2: 5+2(x+3) = 5+2x+6"),
                       ("c", "=total: 4x+16")],
               confere=("v", "x = 4: 13 + 19 = 32 reais"), teste=None),
    "q2": dict(ids=("22", "23"), titulo="O TERRENO E A CALÇADA", area="EQUIVALÊNCIA", ic=1, ok="B",
               enun=[("a", "Um terreno quadrado tem lado de x metros. Para a calçada, perdeu 6 m em cada lado e "
                           "continuou quadrado.", False),
                     ("b", "A área que sobrou, em m², é", True)],
               alts=[("A", "=x^2−36", "sonho do calouro", RED), ("B", "=x^2−12x+36", "", GREEN),
                     ("C", "=x^2−6x+36", "meio pela metade", AMBER), ("D", "=x^2−12x−36", "b² negativo", RED),
                     ("E", "=x^2+12x+36", "sinal trocado", RED)],
               pad="lado novo: x − 6 · área: (x − 6)²",
               passos=[("a", "x = 10 → lado 4 → área 16 m²"), ("b", "só a B dá 16")],
               confere=("v", "meio: 2 · x · 6 = 12x"), teste=("a", "TESTE: x = 10")),
    "q3": dict(ids=("24", "25"), titulo="A PRAÇA AMPLIADA", area="ÁREA · TERMO DO MEIO", ic=2, ok="E",
               enun=[("a", "Uma praça quadrada tem lado de x metros. A prefeitura vai aumentar cada lado em 4 m.", False),
                     ("b", "O AUMENTO da área da praça, em m², é", True)],
               alts=[("A", "=16", "sonho do calouro", RED), ("B", "=8x", "sem o quadradinho", AMBER),
                     ("C", "=4x+16", "um retângulo só", AMBER), ("D", "=x^2+8x+16", "área nova inteira", RED),
                     ("E", "=8x+16", "", GREEN)],
               pad="desenhe o quadrado novo",
               passos=[("a", "2 retângulos x · 4 + quadradinho 4 · 4"), ("b", "=aumento: 8x+16")],
               confere=("v", "x = 10: 196 − 100 = 96 m²"), teste=None),
    "q4": dict(ids=("26", "27"), titulo="A FRAÇÃO ALGÉBRICA", area="SIMPLIFICAÇÃO", ic=3, ok="A",
               enun=[("a", "Para x ≠ 2, a fração", False), ("a", "={3x^2−12}/{x^2−4x+4}", False),
                     ("b", "é igual a", True)],
               alts=[("A", "={3(x+2)}/{x−2}", "", GREEN), ("B", "=3", "fatorou como quadrado", RED),
                     ("C", "=9/{4x−4}", "cortou termo", RED), ("D", "={x+2}/{x−2}", "perdeu o 3", AMBER),
                     ("E", "={3(x−2)}/{x+2}", "inverteu", AMBER)],
               pad="fatore em cima e embaixo · fator comum primeiro",
               passos=[("a", "=em cima: 3(x+2)(x−2)"), ("b", "=embaixo: (x−2)^2"),
                       ("c", "={3(x+2)}/{x−2}")],
               confere=("v", "x = 3: 15/1 = 15"), teste=("v", "TESTE: x = 3")),
    "q5": dict(ids=("28", "29"), titulo="O GRAMADO", area="CONTA SEM CALCULADORA", ic=4, ok="C",
               enun=[("a", "Um condomínio vai cobrir com grama um terreno retangular de 302 m por 298 m.", False),
                     ("b", "Sem calculadora, a área do terreno, em m², é", True)],
               alts=[("A", "90 004", "somou o 2²", RED), ("B", "90 000", "ignorou o 2²", AMBER),
                     ("C", "89 996", "", GREEN), ("D", "89 998", "tirou 2, não 2²", AMBER),
                     ("E", "88 804", "fez 298²", RED)],
               pad="gêmeos ao redor de 300",
               passos=[("a", "=(300+2)(300−2)"), ("b", "=300^2 − 2^2 = 90 000 − 4"), ("b", "89 996 m²")],
               confere=("v", "um pouco menos que 90 000"), teste=None),
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


def linha_passo(c, ln, x, y, a, col):
    """um passo da resolução: '=rótulo: expr' (rótulo em texto, conta em expr) ou texto simples. Devolve a altura."""
    if ln.startswith("="):
        s = ln[1:]
        rot = ""
        if ": " in s:
            rot, s = s.split(": ", 1)
            rot += ":"
        xx = x
        if rot:
            ftext(c, rot, x, y + 12, 32, "bold", INK2, a, align="left")
            xx = x + ftw(rot, 32, "bold") + 16
        sz = 44
        while K.math_w(s, sz) > 640 - (xx - x):
            sz -= 2
        _, up, dn = K.math_box(s, sz)
        mx(c, s, xx, y, sz, col, a)
        return max(56, up + dn + 14)
    sz = 34
    while ftw(ln, sz) > 640:
        sz -= 2
    ftext(c, nb(ln), x, y + 12, sz, "black", col, a, align="left")
    return 56


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
        area_icone(c, d["ic"], 770, 222, 0.42, a0)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            if s.startswith("="):
                _, up, dn = K.math_box(s[1:], 50)
                mx(c, s[1:], 180, y + up, 50, INK, a)
                y += up + dn + 24
                continue
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
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
            yy = 410
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                yy += linha_passo(c, s, 180, yy, a, GREEN if last else INK) + 8
            if d["confere"]:
                cue, s = d["confere"]
                sz = 30
                while ftw(s, sz) > 580:
                    sz -= 2
                conferido(c, s, 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, sz)
            if d["teste"]:
                cue, s = d["teste"]
                K.selo_teste(c, 660, 785, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, s)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("30.b", "EP. 1", 0, ["traduzir: “o dobro da soma” × “a soma do dobro”", "valor numérico com negativos entre ( )",
                               "termos semelhantes e distributiva completa", "menos antes do parêntese: troque os sinais"]),
         ("30.c", "EP. 2", 1, ["quadrado da soma e da diferença de cabeça", "soma pela diferença, nos dois sentidos",
                               "o desenho: (a + b)² ≠ a² + b²", "o cubo da soma, no volume"]),
         ("31.a", "EP. 3", 2, ["fatorar: fator comum, agrupamento, a² − b², trinômio", "frações: corte só fatores",
                               "a² + b² a partir de a + b e ab"]),
         ("31.b", "EP. 4", 3, ["49 · 51 e 87² − 13² sem calculadora"]),
         ("31.c", "EP. 5", None, ["testar alternativas com um número"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["30.a"], 0.5) * (1 - ep(t, C["30.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 200), (150, 440), (990, 200), (990, 400), (990, 520)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        if ic is not None:
            icone(c, ic, x + 40, y0 + 100, 0.22, a)
        else:
            K.selo_teste(c, x + 40, y0 + 90, a, True, "x = 2")
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 44
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            sz = 26
            while ftw(it, sz, "bold") > 600:
                sz -= 1
            K.ftext(c, it, x + 158, yy + 10, sz, "bold", INK, a, align="left")
    ae = ep(t, C["31.d"], 0.5)
    if ae > 0:
        boxed(c, 990, 680, 760, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1370, 730, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["32.a"], 0.5)
    ab = ep(t, C["32.b"], 0.5)
    ac = ep(t, C["32.c"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["32.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 200 + k * 82, 230 + r_ * 90
        col = mix("#E6E6E2", GREEN, ab if ok else 0)
        rrect(c, x, y, 66, 72, 12, col, a)
        if ac > 0 and i < 10:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 74, 80), 14, 14), paint(BLUE, ac, stroke=4))
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 400, 46, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 200, 580, 1520, 180, BLUE, ac, 0.08)
        area_icone(c, 0, 360, 670, 0.6, ac)
        text_mid(c, "pelo menos 10 de MODELAGEM", 1000, 640, 44, "black", BLUE, ac)
        text_mid(c, "escrever a expressão a partir de um texto", 1000, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 260, 28, "black", GRAY, aa, tracking=2)
    text(c, "Equações e inequações do 1º grau", W / 2, 350, 62, "black", PURPLE, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        rrect(c, W / 2 - 420, 470, 840, 200, 24, mix("#FFFFFF", PURPLE, 0.10), ab, shadow=True)
        mx(c, "2x+3 = 11", W / 2 - 120, 570, 70, INK, ab, align="center")
        arrow(c, W / 2 + 90, 570, W / 2 + 190, 570, GREEN, ab, 6, 16)
        mx(c, "x = 4", W / 2 + 290, 570, 70, GREEN, ab, align="center")
        text(c, "encontrar o valor desconhecido", W / 2, 760, 38, "black", INK2, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, duas=b_duas, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
