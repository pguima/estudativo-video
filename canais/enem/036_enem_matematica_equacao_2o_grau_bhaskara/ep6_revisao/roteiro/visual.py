"""Visual — Equação do 2º Grau e Bhaskara, Episódio 6: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, selo_teste...).
Índice visual da revisão: os 5 ícones dos episódios (icone()): tabelinha a | b | c · porteiro Δ · duas cartas viradas ·
jardim com calçada · fantasia do y.
Ícones de contexto nas questões (area_icone()): quadro com moldura · porteiro Δ = 0 · cartas −3 e 7 · aperto de mão ·
bola lançada. A LIXEIRA recebe as raízes descartadas.
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
_s = importlib.util.spec_from_file_location("comum036", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_equacao_2o_grau_ep6_revisao.mp4"
CARD_R = K.CARD_R
GRAMA = "#7CC47F"
CALCADA = "#C9C4B6"
PELE = "#E8B98F"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def mx(c, s, x, cy, size, col=INK, a=1.0, align="left"):
    """linha matemática de uma cor só (expr)"""
    return K.mdraw(c, s, x, cy, size, col, a, align=align)


def nb(s):
    """espaço rígido: não quebra '1 200', '25 m' nem '30 cm'"""
    s = re.sub(r"(?<=\d) (?=(cm²|cm|m|s|L|km)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
    return s


def quebra(s, size, maxw, peso="black"):
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and ftw(tst, size, peso) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    return out + ([cur] if cur else [])


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# peças
# ======================================================================

def tabelinha(c, a):
    """ícone do ep1: a | b | c com sinal, e o '= 0' da equação arrumada"""
    for k, (L, v, col) in enumerate((("a", "1", BLUE), ("b", "−7", AMBER), ("c", "10", BLUE))):
        x = -165 + k * 110
        rrect(c, x, -90, 100, 70, 10, mix("#FFFFFF", col, 0.25), a)
        fmid(c, L, x + 50, -55, 34, "black", col, a)
        rrect(c, x, -14, 100, 70, 10, "#FFFFFF", a, stroke=3, stroke_color=col)
        fmid(c, v, x + 50, 21, 34, "black", INK, a)
    rrect(c, 175, -60, 100, 90, 14, GREEN, a)
    fmid(c, "= 0", 225, -15, 36, "black", "#FFFFFF", a)
    fmid(c, "o sinal é o sobrenome", 0, 110, 28, "black", AMBER, a)


def porteiro(c, a, n=None):
    """ícone do ep2: a porta com o Δ na placa (n = quantas raízes passam, opcional)"""
    rrect(c, -80, -120, 160, 230, 12, mix("#FFFFFF", PURPLE, 0.20), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-80, -120, 160, 230), 12, 12), paint(PURPLE, a, stroke=5))
    c.drawCircle(50, 0, 9, paint(PURPLE, a))
    rrect(c, -50, -100, 100, 70, 10, PURPLE, a)
    fmid(c, "Δ", 0, -65, 54, "black", "#FFFFFF", a)
    for k, (s, col) in enumerate((("> 0: 2", GREEN), ("= 0: 1", AMBER), ("< 0: 0", RED))):
        if n is None or n == k:
            fmid(c, s, 175, -60 + k * 60 if n is None else -10, 32, "black", col, a)


def cartas(c, a, vals=("?", "?")):
    """ícone do ep3: duas cartas viradas (soma e produto)"""
    for k, v in enumerate(vals):
        x = -70 + k * 140
        c.save(); c.translate(x, 0); c.rotate(-8 + 16 * k)
        rrect(c, -55, -80, 110, 160, 14, "#FFFFFF", a, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-55, -80, 110, 160), 14, 14), paint(BLUE, a, stroke=4))
        fmid(c, v, 0, 0, 58 if v == "?" else 50, "black", BLUE, a)
        c.restore()
    fmid(c, "S · P", 0, 125, 30, "black", PURPLE, a)


def jardim(c, a):
    """ícone do ep4: jardim com a calçada abraçando, e a lixeira com o −10"""
    rrect(c, -150, -100, 240, 180, 10, CALCADA, a)
    rrect(c, -120, -70, 180, 120, 6, GRAMA, a)
    fmid(c, "x", -30, -85, 26, "black", INK, a)
    fmid(c, "x", -30, 66, 26, "black", INK, a)
    lixeira(c, 160, 0, 0.8, a, "−10")


def lixeira(c, x, y, s, a, rot=None):
    """lixeira para as raízes descartadas (rot = a raiz que foi para o lixo)"""
    if a <= 0:
        return
    c.save(); c.translate(x, y); c.scale(s, s)
    if rot:
        fmid(c, rot, 0, -95, 34, "black", RED, a)
        strike(c, -40, -95, 40, -95, 1, RED, a)
    rrect(c, -50, -62, 100, 14, 6, INK2, a)
    rrect(c, -14, -74, 28, 14, 5, INK2, a)
    p = skia.Path(); p.moveTo(-42, -44); p.lineTo(42, -44); p.lineTo(32, 66); p.lineTo(-32, 66); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", INK2, 0.35), a))
    c.drawPath(p, paint(INK2, a, stroke=4))
    for xx in (-16, 0, 16):
        line(c, xx, -28, xx * 0.8, 52, INK2, a, 3)
    c.restore()


def fantasia(c, a, tirou=0.0):
    """ícone do ep5: o x² vestido de y (a máscara sai com tirou → 1)"""
    rrect(c, -110, -80, 220, 150, 22, mix("#FFFFFF", AMBER, 0.18), a)
    fmid(c, "x²", 0, -5, 72, "black", INK, a)
    am = a * (1 - tirou)
    if am > 0:
        c.save(); c.translate(0, -40 * tirou)
        rrect(c, -90, -60, 180, 90, 40, AMBER, am)
        c.drawCircle(-38, -20, 13, paint("#FFFFFF", am)); c.drawCircle(38, -20, 13, paint("#FFFFFF", am))
        fmid(c, "y", 0, 10, 40, "black", "#FFFFFF", am)
        c.restore()
    fmid(c, "a fantasia sai", 0, 115, 28, "black", AMBER, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 5 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (tabelinha, porteiro, cartas, jardim, fantasia)[k](c, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones de contexto: quadro com moldura · porteiro Δ = 0 · cartas −3 e 7 · aperto de mão · bola lançada"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # quadro com moldura
        rrect(c, -130, -95, 260, 190, 8, "#B07A3F", a, shadow=True)
        rrect(c, -100, -65, 200, 130, 4, mix("#FFFFFF", BLUE, 0.25), a)
        p = skia.Path(); p.moveTo(-90, 55); p.lineTo(-30, -10); p.lineTo(10, 30); p.lineTo(45, 0); p.lineTo(90, 55)
        p.close(); c.drawPath(p, paint(GRAMA, a))
        c.drawCircle(55, -35, 16, paint(AMBER, a))
    elif k == 1:    # porteiro com uma só
        porteiro(c, a, 1)
    elif k == 2:    # cartas −3 e 7
        cartas(c, a, ("−3", "7"))
    elif k == 3:    # aperto de mão (dois braços que se encontram)
        rrect(c, -170, -20, 140, 50, 22, BLUE, a)
        rrect(c, 30, -20, 140, 50, 22, GREEN, a)
        c.drawCircle(-30, 5, 36, paint(PELE, a)); c.drawCircle(30, 5, 36, paint(PELE, a))
        fmid(c, "28", 0, -85, 44, "black", INK, a)
    elif k == 4:    # bola lançada: a altura de 25 m cruzada duas vezes
        line(c, -150, 90, 150, 90, INK2, a, 4)
        p = skia.Path(); p.moveTo(-130, 90); p.quadTo(0, -170, 130, 90)
        c.drawPath(p, paint(INK2, a, stroke=3))
        line(c, -150, 0, 150, 0, AMBER, a, 3)
        fmid(c, "25 m", 165, -22, 26, "black", AMBER, a)
        for xx in (-86, 86):
            c.drawCircle(xx, 0, 14, paint(BLUE, a))
    c.restore()


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 380, 205, 760, 120, 18, "#FFFFFF", aa, shadow=True)
        mx(c, "x^2 - 5x + 4 = 0", W / 2, 265, 64, INK2, aa, align="center")
        strike(c, W / 2 - 300, 268, W / 2 + 300, 268, ep(t, C["01.a"] + 2.6, 0.4), RED, aa)
    itens = (("JARDIM", 0, GRAMA), ("BOLA", 4, BLUE), ("CAMPEONATO", 3, AMBER), ("LUCRO", None, GREEN))
    for k, (s, ic, col) in enumerate(itens):
        a = ep(t, C["01.b"] + 0.7 * k, 0.4)
        x = 360 + k * 400
        if ic is None:
            if a > 0:
                fmid(c, "R$", x, 500, 110, "black", GREEN, a)
        elif ic == 0:
            c.save(); c.translate(x, 500); c.scale(0.8, 0.8); jardim_simples(c, a); c.restore()
        else:
            area_icone(c, ic, x, 500, 0.75, a)
        text(c, s, x, 660, 30, "black", col, a)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        pill(c, "montar · resolver · escolher a raiz", W / 2, 735, PURPLE, size=34, a=ac, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 840, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 840, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


def jardim_simples(c, a):
    rrect(c, -130, -90, 260, 180, 10, CALCADA, a)
    rrect(c, -100, -60, 200, 120, 6, GRAMA, a)


COBRA = [("02.a", "ÁREAS", "moldura, calçada", BLUE, "(8+2x)(5+2x)"),
         ("02.b", "MOVIMENTO", "a altura da bola", PURPLE, "h = 25t - 5t^2"),
         ("02.c", "CONTAGEM", "jogos, apertos de mão", AMBER, "n(n-1)/2"),
         ("02.d", "ECONOMIA", "o lucro zero", GREEN, "L = 0"),
         ("02.e", "LEITURA DAS RAÍZES", "qual serve, qual vai pro lixo", RED, None)]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "AS CINCO FANTASIAS", "ONDE A EQUAÇÃO SE ESCONDE", BLUE)
    for k, (cue, tit, sub, col, ex) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 250 + d, 330, 480, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 28, "black", col, a, 290, 36, align="center")
        if ex:
            sz = 40
            while K.math_w(ex, sz) > 290:
                sz -= 2
            mx(c, ex, x, 560 + d, sz, INK, a, align="center")
        else:
            lixeira(c, x, 560 + d, 0.6, a, "−10")
        para(c, sub, x, 650 + d, 24, "bold", INK2, a, 290, 30, align="center")


TRES = [("03.a", "1", "IGUALE A ZERO", "ax² + bx + c = 0", BLUE),
        ("03.b", "2", "ESCOLHA O CAMINHO", "incompleta → fatoração · raízes inteiras → S e P · o resto → Bhaskara", PURPLE),
        ("03.c", "3", "VOLTE AO ENUNCIADO", "medida negativa não é resposta", GREEN)]


def b_tres(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "TRÊS HÁBITOS DA SEÇÃO 01", GREEN)
    for k, (cue, n, tit, sub, col) in enumerate(TRES):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 250 + d, 500, 520, 24, mix("#F7F7F5", col, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=col)
        para(c, tit, x, 420 + d, 36, "black", col, a, 440, 44, align="center")
        yy = 520 + d
        for ln in sub.split(" · "):
            yy += para(c, ln, x, yy, 28, "bold", INK, a, 440, 36, align="center") + 10
    lixeira(c, 1520, 650, 0.55, ep(t, C["03.c"] + 1.2, 0.4), "−10")


INDICE = [("EP. 1", "só conversa arrumada (= 0) · o sinal é o sobrenome · produto nulo · nunca divida por x"),
          ("EP. 2", "Bhaskara: a chave mestra · o Δ é o porteiro"),
          ("EP. 3", "o jogo dos dois números"),
          ("EP. 4", "a calçada abraça o jardim · descartar não é trocar o sinal"),
          ("EP. 5", "a fantasia do y tem de sair")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b", "05.c"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 220 + k * 370
        y = 200
        rrect(c, x - 170, y, 340, 620, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 170, y, 340, 620), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 150, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 220, 0.6, a)
        yy = y + 380
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 25, "black", INK if on_ else INK2, a, 300, 31, align="center") + 12


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ ÁLGEBRA", "ONDE ISSO APARECE", BLUE)
    a6 = ep(t, C["06.a"], 0.5) * (1 - ep(t, C["07.b"], 0.4))
    if a6 > 0:
        area_icone(c, 4, 520, 470, 1.25, a6)
        text(c, "FÍSICA · LANÇAMENTO", 1250, 280, 34, "black", BLUE, a6)
        mx(c, "25t - 5t^2 = 30", 1250, 380, 54, INK, a6, align="center")
        mx(c, "t^2 - 5t + 6 = 0", 1250, 470, 50, INK2, a6, align="center")
        fmid(c, "2 s subindo · 3 s descendo", 1250, 565, 40, "black", GREEN, a6)
        lixeira(c, 1250, 720, 0.6, ep(t, C["06.a"] + 7.0, 0.4) * a6, "t < 0")
        text_mid(c, "tempo negativo se descarta", 1250, 820, 26, "bold", INK2, ep(t, C["06.a"] + 7.0, 0.4) * a6)
    AREAS = [("07.b", "GEOMETRIA", "(x+2)^2 = x^2 + 4x + 4", "Pitágoras: x e x + 2"),
             ("07.c", "ECONOMIA", "-x^2 + 30x - 200 = 0", "lucro zero: 10 e 20 unidades"),
             ("07.d", "FUNÇÃO QUADRÁTICA", None, "raízes = cortes no eixo x")]
    for k, (cue, tit, ex, sub) in enumerate(AREAS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 260 + d, 500, 420, 24, mix("#F7F7F5", BLUE, 0.06), a)
        text(c, tit, x, 330 + d, 32, "black", BLUE, a)
        if ex:
            sz = 46
            while K.math_w(ex, sz) > 440:
                sz -= 2
            mx(c, ex, x, 460 + d, sz, INK, a, align="center")
        else:
            line(c, x - 180, 480 + d, x + 180, 480 + d, INK2, a, 4)
            p = skia.Path(); p.moveTo(x - 150, 380 + d); p.quadTo(x, 640 + d, x + 150, 380 + d)
            c.drawPath(p, paint(BLUE, a, stroke=5))
            for xx in (-104, 104):
                c.drawCircle(x + xx, 480 + d, 11, paint(GREEN, a))
        para(c, sub, x, 600 + d, 28, "bold", INK2, a, 440, 34, align="center")
        if k == 2:
            pill(c, "PRÓXIMA SÉRIE", x, 720 + d, PURPLE, size=24, a=a, anchor="center")


HABITOS = [("08.a", "1", "TESTE AS ALTERNATIVAS", "quem zerar é raiz"),
           ("08.b", "2", "SIMPLIFIQUE ANTES", "4x² + 32x − 80 = 0 · ÷ 4 · x² + 8x − 20 = 0"),
           ("08.c", "3", "SOMA E PRODUTO PRIMEIRO", "não saiu par inteiro? · Bhaskara"),
           ("08.d", "4", "RELEIA A PERGUNTA", "a raiz é o meio do caminho")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "QUATRO HÁBITOS NA HORA H", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 250 + d, 410, 500, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=GREEN)
        para(c, tit, x, 420 + d, 32, "black", GREEN, a, 360, 40, align="center")
        yy = 560 + d
        for ln in sub.split(" · "):
            yy += para(c, nb(ln), x, yy, 28, "bold", INK, a, 370, 36, align="center") + 10


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


# (contexto, afirmação (expr ou texto com "→"), verdadeira?, por que engana, regra certa, versão certa em expr, ícone)
VF = [
    ("o sinal do b", "x^2 - 7x + 10 = 0 → b = 7", False, "o 7 parece sozinho",
     "o sinal é o sobrenome do coeficiente", "b = -7", 0),
    ("o b² no Δ", "(-7)^2 = 49", True, "muita gente acha −49",
     "o menos entra no parêntese · b² nunca é negativo", "b^2 ≥ 0", 1),
    ("a divisão por 2a", "x = -b ± √{Δ}/2a", False, "a raiz parece a parte difícil",
     "o traço cobre o numerador inteiro", "x = {-b±√{Δ}}/2a", 1),
    ("dividir por x", "3x^2 = 12x → x = 4", False, "o 4 é mesmo uma raiz",
     "a divisão apaga o zero: fatore", "3x(x-4) = 0", 0),
    ("incompleta com b = 0", "x^2 = 25 → x = 5 ou x = -5", True, "a calculadora só mostra o 5",
     "(−5)² também dá 25 · só descarte se o contexto pedir", "x = ±5", 0),
    ("descartar a raiz", "largura: −10 não serve → resposta 10", False, "parece um conserto",
     "descartar não é trocar o sinal · a resposta é a outra raiz", "−10 → lixeira", 3),
    ("a soma das raízes", "x^2 - 7x + 10 = 0 → S = -7", False, "o −7 está ali na equação",
     "S = −b/a: o sinal do meio vem trocado", "S = 2 + 5 = 7", 2),
    ("a biquadrada", "x^4 - 5x^2 + 4 = 0 → x = 1 ou 4", False, "1 e 4 saem mesmo da conta",
     "esses são os valores do y · a fantasia tem de sair", "x = ±1 · x = ±2", 4),
    ("antes de Bhaskara", "x^2 + 4x = 140 → x^2 + 4x - 140 = 0", True, "dá vontade de usar c = 140",
     "a equação só conversa arrumada", "… = 0", 0),
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
    icone(c, ic, 330, 420, 0.5, a0)
    text(c, ctx.upper(), 960, 300, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    if ":" in conta:     # frase em texto
        sz = 44
        lines = quebra(nb(conta), sz, 740)
        riscos = []
        for j, ln in enumerate(lines):
            yj = 410 + (j - (len(lines) - 1) / 2) * (sz + 12)
            fmid(c, ln, 960, yj, sz, "black", INK, a0)
            riscos.append((ftw(ln, sz), yj + 4))
    else:
        sz = 62
        while K.math_w(conta, sz) > 720:
            sz -= 2
        w = mx(c, conta, 960, 410, sz, INK, a0, align="center")
        riscos = [(w, 415)]
    if ar > 0 and not ver:
        for w, yl in riscos:
            strike(c, 960 - w / 2 - 10, yl, 960 + w / 2 + 10, yl, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    if n == 5:
        lixeira(c, 1300, 560, 0.55, ep(t, q("g"), 0.5), "−10")
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        sze = 34
        while ftw(engana, sze, "bold") > (560 if ver else 680):
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
        if "→" in fix or "·" in fix:
            szf = 44
            while ftw(fix, szf) > 520:
                szf -= 2
            fmid(c, fix, 1420, 715, szf, "black", GREEN, ag)
        else:
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
    for k, (s, col) in enumerate((("= 0", BLUE), ("resolva", PURPLE), ("escolha a raiz", GREEN))):
        pill(c, s, W / 2 - 380 + k * 380, 760, col, size=32, a=ep(t, C["19.b"] + 0.5 + 0.3 * k, 0.4), anchor="center")


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · passos: (cue, texto ou "=expr") · confere: (cue, texto) · lixo: (cue, raiz descartada)

Q = {
    "q1": dict(ids=("20", "21"), titulo="A MOLDURA", area="ÁREA · RAIZ DESCARTADA", ic=0, ok="A",
               enun=[("a", "Um quadro de 30 cm por 20 cm ganha uma moldura de largura x em volta de todo o quadro. "
                           "Com a moldura, a área total passa a ser 1 200 cm².", False),
                     ("b", "A largura da moldura, em centímetros, é", True)],
               alts=[("A", "5", "", GREEN), ("B", "10", "moldura de um lado só", RED),
                     ("C", "30", "trocou o sinal do −30", AMBER), ("D", "35", "parou na √Δ", RED),
                     ("E", "600", "a área da moldura", AMBER)],
               intro="cada medida cresce 2x",
               passos=[("a", "=(30+2x)(20+2x) = 1 200"), ("b", "=x^2 + 25x - 150 = 0"),
                       ("c", "S = −25 · P = −150 → 5 e −30")],
               lixo=("c", "−30"), confere=("v", "40 · 30 = 1 200 cm²")),
    "q2": dict(ids=("22", "23"), titulo="UMA ÚNICA RAIZ", area="PARÂMETRO · Δ = 0", ic=1, ok="D",
               enun=[("a", "Na equação 2x² − 12x + k = 0, o número k foi escolhido para que exista uma única raiz "
                           "real.", False),
                     ("b", "O valor de k é", True)],
               alts=[("A", "−18", "−12² negativo", AMBER), ("B", "1,5", "não elevou o b", RED),
                     ("C", "3", "a raiz, não o k", AMBER), ("D", "18", "", GREEN),
                     ("E", "72", "esqueceu o 4", RED)],
               intro="uma só raiz: Δ = 0",
               passos=[("a", "=Δ = (-12)^2 - 4 · 2 · k"), ("b", "=144 - 8k = 0 → k = 18")],
               lixo=None, confere=("v", "raiz dupla: x = 3")),
    "q3": dict(ids=("24", "25"), titulo="A EQUAÇÃO PELAS RAÍZES", area="SOMA E PRODUTO", ic=2, ok="E",
               enun=[("a", "Uma equação do 2º grau, com a = 1, tem raízes −3 e 7.", False),
                     ("b", "Essa equação é", True)],
               alts=[("A", "=x^2 + 4x - 21 = 0", "não trocou o sinal do meio", AMBER),
                     ("B", "=x^2 - 4x + 21 = 0", "perdeu o sinal do produto", RED),
                     ("C", "=x^2 - 10x + 21 = 0", "ignorou o menos do 3", RED),
                     ("D", "=x^2 - 21x - 4 = 0", "trocou S e P de lugar", RED),
                     ("E", "=x^2 - 4x - 21 = 0", "", GREEN)],
               intro="o jogo, ao contrário",
               passos=[("a", "S = −3 + 7 = 4 · P = −21"), ("b", "=x^2 - Sx + P = 0"),
                       ("b", "=x^2 - 4x - 21 = 0")],
               lixo=None, confere=None),
    "q4": dict(ids=("26", "27"), titulo="OS APERTOS DE MÃO", area="CONTAGEM", ic=3, ok="B",
               enun=[("a", "Numa reunião, cada pessoa apertou a mão de cada uma das outras uma única vez. Foram 28 "
                           "apertos de mão.", False),
                     ("b", "O número de pessoas na reunião é", True)],
               alts=[("A", "7", "trocou o sinal do −7", AMBER), ("B", "8", "", GREEN),
                     ("C", "14", "dividiu 28 por 2", RED), ("D", "28", "respondeu os apertos", RED),
                     ("E", "56", "parou no 2 · 28", RED)],
               intro="cada aperto conta 2 vezes: ÷ 2",
               passos=[("a", "=n(n-1)/2 = 28"), ("b", "=n^2 - n - 56 = 0"), ("b", "S = 1 · P = −56 → 8 e −7")],
               lixo=("b", "−7"), confere=("v", "8 · 7 ÷ 2 = 28")),
    "q5": dict(ids=("28", "29"), titulo="A BOLA LANÇADA", area="LANÇAMENTO · INTERVALO", ic=4, ok="C",
               enun=[("a", "Uma bola é lançada para cima, e sua altura, em metros, é h = 30t − 5t², com t em segundos.",
                      False),
                     ("b", "Quanto tempo se passa entre o instante em que ela passa por 25 m subindo e o instante em "
                           "que passa descendo?", True)],
               alts=[("A", "1 s", "um instante só", AMBER), ("B", "3 s", "o topo: outra pergunta", RED),
                     ("C", "4 s", "", GREEN), ("D", "5 s", "um instante só", AMBER),
                     ("E", "8 s", "não dividiu por 2", RED)],
               intro="iguale a altura a 25",
               passos=[("a", "=30t - 5t^2 = 25"), ("a", "=t^2 - 6t + 5 = 0"), ("b", "S = 6 · P = 5 → 1 s e 5 s"),
                       ("c", "intervalo: 5 − 1 = 4 s")],
               lixo=None, confere=None),
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
    """um passo da resolução: '=conta' (expr) ou texto simples. Devolve a altura."""
    if ln.startswith("="):
        s = ln[1:]
        if "→" in s or re.search(r"\d \d{3}", s):
            sz = 42
            while ftw(nb(s), sz) > 640:
                sz -= 2
            ftext(c, nb(s), x, y + 14, sz, "black", col, a, align="left")
            return 60
        sz = 44
        while K.math_w(s, sz) > 640:
            sz -= 2
        _, up, dn = K.math_box(s, sz)
        mx(c, s, x, y, sz, col, a)
        return max(56, up + dn + 14)
    sz = 34
    while ftw(nb(ln), sz) > 640:
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
        area_icone(c, d["ic"], 770, 222, 0.32, a0)
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
            pill(c, d["intro"], 180, 320, PURPLE, size=28, a=ad, bounds=(0, 1920))
            yy = 400
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                yy += linha_passo(c, s, 180, yy, a, GREEN if last else INK) + 8
            if d["lixo"]:
                cue, r = d["lixo"]
                lixeira(c, 700, 680, 0.6, ep(t, C[f"{s2}.{cue}"] + 1.5, 0.4) * sol, r)
            if d["confere"]:
                cue, s = d["confere"]
                sz = 30
                while ftw(nb(s), sz) > 440:
                    sz -= 2
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, sz)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("30.b", "EP. 1", 0, ["forma geral e coeficientes com sinal", "incompletas: fator comum, sem dividir por x",
                               "b = 0: duas raízes simétricas · produto nulo"]),
         ("30.c", "EP. 2", 1, ["Bhaskara sem errar b², −b e o 2a", "de onde vem a fórmula", "o sinal do Δ e o parâmetro"]),
         ("31.a", "EP. 3", 2, ["soma e produto e os sinais das raízes", "montar a equação pelas raízes"]),
         ("31.b", "EP. 4", 3, ["modelar área, lançamento e campeonato", "descartar sem trocar o sinal"]),
         ("31.c", "EP. 5", 4, ["biquadradas: troca y = x² e volta para x"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["30.a"], 0.5) * (1 - ep(t, C["30.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(130, 200), (130, 400), (990, 200), (990, 340), (990, 480)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, ic, x + 40, y0 + 100, 0.2, a)
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 44
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            sz = 26
            while ftw(it, sz, "bold") > 640:
                sz -= 1
            K.ftext(c, it, x + 158, yy + 10, sz, "bold", INK, a, align="left")
    ae = ep(t, C["31.d"], 0.5)
    if ae > 0:
        boxed(c, 990, 640, 760, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1370, 690, 32, "black", INK, ae)


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
        icone(c, 3, 360, 670, 0.45, ac)
        text_mid(c, "PELO MENOS 10: você monta a equação", 1040, 640, 42, "black", BLUE, ac)
        text_mid(c, "a partir do texto do enunciado", 1040, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 260, 28, "black", GRAY, aa, tracking=2)
    text(c, "Sistemas de equações lineares", W / 2, 350, 62, "black", PURPLE, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        rrect(c, W / 2 - 420, 450, 840, 240, 24, mix("#FFFFFF", PURPLE, 0.10), ab, shadow=True)
        mx(c, "x + y = 10", W / 2, 530, 64, INK, ab, align="center")
        mx(c, "x - y = 2", W / 2, 620, 64, INK, ab, align="center")
        text(c, "duas incógnitas ao mesmo tempo", W / 2, 780, 38, "black", INK2, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, tres=b_tres, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
