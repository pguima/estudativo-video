"""Visual — Função Composta e Função Inversa, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): duas máquinas em fila · a ponte que some · a esteira rodando
ao contrário · o espelho na diagonal.
Ícones de área (area_icone()): termômetro · frasco · moeda · cadeado · máquinas · espelho · tabela.
"∘" e "ℝ" só existem na fonte do ftext: todo texto com eles passa por ftext/fmid/fit (nunca text, pill, chip, head).
Cores com função: azul = definição · roxo = regra, fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
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
_s = importlib.util.spec_from_file_location("comum045", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_composta_inversa_ep5_revisao.mp4"
CARD_R = K.CARD_R
COL_G, COL_F = BLUE, PURPLE


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def nb(s):
    """espaço rígido: não quebra 'R$ 30', 'US$ 50', '40 °C' nem '1 000'"""
    s = re.sub(r"(?<=\$) (?=\d)", " ", s)
    s = re.sub(r"(?<=\d) (?=(°F|°C|reais|vezes|%)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
    return s


def fit(c, s, x, y, size, maxw, peso, col, a, align="left"):
    """texto numa linha só (ftext), encolhendo até caber em maxw"""
    s = nb(s)
    while ftw(s, size, peso) > maxw and size > 18:
        size -= 1
    ftext(c, s, x, y, size, peso, col, a, align=align)
    return size


def _quebra(s, size, maxw, peso="black"):
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and ftw(tst, size, peso) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    return out + ([cur] if cur else [])


def para_nb(c, s, x, y, size, peso, color, a, maxw, lh=None, align="left"):
    """quebra de linha (ftext) que respeita os espaços rígidos de nb()"""
    s = nb(s)
    lh = lh or size * 1.32
    out = _quebra(s, size, maxw, peso)
    if a > 0:
        for k, ln in enumerate(out):
            ftext(c, ln, x, y + k * lh, size, peso, color, a, align=align)
    return len(out) * lh


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


# ======================================================================
# peças: os 4 ícones dos episódios
# ======================================================================

def caixa_maq(c, cx, cy, nome, col, a, w=150, h=120):
    """mini máquina: funil à esquerda, corpo com o nome"""
    p = skia.Path(); p.moveTo(cx - w / 2 - 34, cy - 34); p.lineTo(cx - w / 2, cy - 16); p.lineTo(cx - w / 2, cy + 16)
    p.lineTo(cx - w / 2 - 34, cy + 34); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.4), a))
    rrect(c, cx - w / 2, cy - h / 2, w, h, 18, mix("#FFFFFF", col, 0.18), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 18, 18), paint(col, a, stroke=5))
    fmid(c, nome, cx, cy, h * 0.5, "black", col, a)


def maquinas_ic(c, a):
    """ep1: duas máquinas em fila (g primeiro, f depois)"""
    caixa_maq(c, -110, 0, "g", COL_G, a)
    arrow(c, -25, 0, 25, 0, INK2, a, 6, 16)
    caixa_maq(c, 140, 0, "f", COL_F, a)
    for x, s in ((-110, "1º"), (140, "2º")):
        ftext(c, s, x, 110, 32, "black", INK2, a, align="center")


def ponte_ic(c, a):
    """ep2: a ponte (a grandeza intermediária) entre duas margens, sumindo"""
    rrect(c, -220, 20, 120, 120, 10, mix("#FFFFFF", GREEN, 0.5), a)
    rrect(c, 100, 20, 120, 120, 10, mix("#FFFFFF", GREEN, 0.5), a)
    p = skia.Path(); p.moveTo(-100, 40); p.quadTo(0, -60, 100, 40)
    c.drawPath(p, paint(AMBER, a * 0.55, stroke=14))
    for x in (-60, 0, 60):
        line(c, x, 25 if x else -12, x, 40, AMBER, a * (0.9 if x else 0.45), 6)
    ftext(c, "t", -160, 0, 44, "black", INK, a, align="center")
    ftext(c, "R$", 160, 0, 40, "black", INK, a, align="center")
    ftext(c, "peças", 0, -40, 30, "black", AMBER, a * 0.6, align="center")


def esteira_ic(c, a):
    """ep3: a esteira rodando ao contrário (o caminho de volta)"""
    rrect(c, -200, -10, 400, 70, 35, mix("#FFFFFF", INK2, 0.35), a, shadow=True)
    for x in (-160, -55, 55, 160):
        c.drawCircle(x, 25, 24, paint("#FFFFFF", a)); c.drawCircle(x, 25, 24, paint(INK2, a, stroke=5))
    arrow(c, 150, -60, -150, -60, GREEN, a, 8, 24)
    rrect(c, -40, -150, 80, 70, 12, AMBER, a)
    ftext(c, "f⁻¹", 0, 130, 50, "black", GREEN, a, align="center")


def espelho_ic(c, a):
    """ep4: o espelho na diagonal y = x, com (1, 3) e (3, 1)"""
    rrect(c, -180, -180, 360, 360, 22, "#FFFFFF", a, shadow=True)
    line(c, -150, 150, -150, -150, INK2, a, 4)
    line(c, -150, 150, 150, 150, INK2, a, 4)
    line(c, -150, 150, 150, -150, GREEN, a, 6, dash=[16, 10])
    for (x, y), col in (((-90, -60), COL_F), ((60, 90), COL_G)):
        c.drawCircle(x, y, 18, paint(col, a))
    line(c, -90, -60, 60, 90, AMBER, a * 0.7, 4, dash=[8, 8])


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (maquinas_ic, ponte_ic, esteira_ic, espelho_ic)[k](c, a)
    c.restore()


# ======================================================================
# ícones de área
# ======================================================================

def termometro(c, a):
    rrect(c, -35, -170, 70, 260, 35, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-35, -170, 70, 260), 35, 35), paint(INK2, a, stroke=6))
    c.drawCircle(0, 115, 60, paint(RED, a))
    rrect(c, -14, -60, 28, 160, 14, RED, a)
    for k in range(4):
        line(c, 40, -130 + k * 45, 70, -130 + k * 45, INK2, a, 5)


def frasco(c, a):
    p = skia.Path(); p.moveTo(-40, -170); p.lineTo(40, -170); p.lineTo(40, -60); p.lineTo(130, 140); p.lineTo(-130, 140)
    p.lineTo(-40, -60); p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    q = skia.Path(); q.moveTo(-85, 40); q.lineTo(85, 40); q.lineTo(130, 140); q.lineTo(-130, 140); q.close()
    c.drawPath(q, paint(mix("#FFFFFF", PURPLE, 0.55), a))
    c.drawPath(p, paint(INK2, a, stroke=7))
    ftext(c, "pH", 0, 115, 56, "black", "#FFFFFF", a, align="center")


def moeda(c, a):
    c.drawCircle(0, 0, 140, paint(AMBER, a))
    c.drawCircle(0, 0, 112, paint(mix(AMBER, INK, 0.25), a, stroke=8))
    ftext(c, "US$", 0, 26, 76, "black", "#FFFFFF", a, align="center")


def cadeado(c, a):
    p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(-80, -170, 160, 180), 180, 180)
    c.drawPath(p, paint(INK2, a, stroke=24))
    line(c, -80, -80, -80, -20, INK2, a, 24); line(c, 80, -80, 80, -20, INK2, a, 24)
    rrect(c, -130, -30, 260, 190, 24, BLUE, a, shadow=True)
    c.drawCircle(0, 50, 22, paint("#FFFFFF", a))
    rrect(c, -8, 50, 16, 60, 6, "#FFFFFF", a)


def maquinas_area(c, a):
    maquinas_ic(c, a)


def espelho_area(c, a):
    espelho_ic(c, a)


def tabela_ic(c, a):
    rrect(c, -190, -130, 380, 260, 16, "#FFFFFF", a, shadow=True)
    for k in range(1, 3):
        line(c, -190, -130 + k * 87, 190, -130 + k * 87, INK2, a, 4)
    for k in range(1, 5):
        line(c, -190 + k * 76, -130, -190 + k * 76, 130, INK2, a, 4)
    rrect(c, -190, -43, 380, 87, 0, mix("#FFFFFF", PURPLE, 0.3), a * 0.6)


AREA_F = (termometro, frasco, moeda, cadeado, maquinas_area, espelho_area, tabela_ic)


def area_icone(c, k, cx, cy, s, a):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    AREA_F[k](c, a)
    c.restore()


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    a0 = ep(t, C["01.a"], 0.5)
    if a0 > 0:
        rrect(c, 760, 190, 400, 130, 65, "#FFFFFF", a0, shadow=True)
        fmid(c, "f ∘ g", W / 2, 255, 80, "black", INK2, a0)
        strike(c, W / 2 - 120, 258, W / 2 + 120, 258, ep(t, C["01.a"] + 1.2, 0.4), RED)
    for k, (s, ic, col) in enumerate((("“o custo depende das peças, que dependem do tempo”", 4, BLUE),
                                      ("“quanto ele andou, se pagou R$ 37,00?”", 6, PURPLE))):
        a, d = rise(t, C["01.b"] + 1.6 * k)
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 360, 360 + d, 720, 290, 26, mix("#F7F7F5", col, 0.12), a)
        if k == 0:
            icone(c, 0, x, 450 + d, 0.42, a)
        else:
            esteira_ic_s(c, x, 450 + d, 0.42, a)
        para_nb(c, s, x, 575 + d, 32, "black", col, a, 640, 40, align="center")
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        rrect(c, 410, 690, 1100, 100, 50, mix("#FFFFFF", GREEN, 0.16), ac, shadow=True)
        text_mid(c, "COMPOSTA E INVERSA SEM O SÍMBOLO", W / 2, 740, 44, "black", GREEN, ac)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        chip(c, "9 V OU F", 330, 860, AMBER, ad, 26)
        chip(c, "5 QUESTÕES NOVAS", 1590, 860, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 26)


def esteira_ic_s(c, cx, cy, s, a):
    c.save(); c.translate(cx, cy); c.scale(s, s)
    esteira_ic(c, a)
    c.restore()


COBRA = [("02.a", "ENCADEAR MODELOS", "tempo → peças → custo", BLUE, 0, "icone"),
         ("02.b", "INVERTER UMA FÓRMULA", "°F → °C", PURPLE, 0, "termo"),
         ("02.c", "TABELAS E CÓDIGOS", "de uma tabela para a outra", AMBER, 6, "area"),
         ("02.d", "GRÁFICO DA INVERSA", "o espelho em y = x", GREEN, 3, "icone")]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "O QUE A PROVA PEDE", "QUATRO FORMAS", BLUE)
    for k, (cue, tit, sub, col, ic, tipo) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 250 + d, 380, 500, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 30, "black", col, a, 340, 38, align="center")
        if tipo == "icone":
            icone(c, ic, x, 560 + d, 0.48, a)
        elif tipo == "termo":
            area_icone(c, 0, x, 560 + d, 0.48, a)
        else:
            area_icone(c, ic, x, 560 + d, 0.42, a)
        fit(c, sub, x, 710 + d, 30, 340, "black", INK2, a, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "DUAS HABILIDADES", BLUE)
    for k, (cue, tit, sub, col, ic) in enumerate((("03.a", "A ORDEM: A DE DENTRO AGE PRIMEIRO", "f(g(x)): primeiro g, depois f", PURPLE, 0),
                                                  ("03.b", "INVERTER = TROCAR ENTRADA E SAÍDA", "a inversa não é “um sobre”", GREEN, 2))):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 250 + k * 290
        rrect(c, 200, y + d, 1520, 250, 26, mix("#F7F7F5", col, 0.10), a, shadow=True)
        badge_num(c, k + 1, 280, y + 125 + d, a, 36, bg=col)
        icone(c, ic, 480, y + 125 + d, 0.48, a)
        fit(c, tit, 680, y + 115 + d, 50, 1000, "black", col, a)
        fit(c, sub, 680, y + 180 + d, 36, 1000, "bold", INK2, a)


INDICE = [("EP. 1", "máquinas em fila · de dentro para fora · meia e sapato"),
          ("EP. 2", "a grandeza-ponte some · a de dentro recebe o que você tem"),
          ("EP. 3", "o caminho de volta · na ordem contrária · f⁻¹ desfaz, 1/f vira"),
          ("EP. 4", "cada saída com um dono · o espelho em y = x · procure nas saídas")]
IND_CUES = ["04.a", "04.b", "05.a", "05.b"]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "RELEMBRE CADA EPISÓDIO", PURPLE)
    aq = ep(t, C["04.t"], 0.5) * (1 - ep(t, C["04.a"], 0.4))
    if aq > 0:
        rrect(c, 360, 380, 1200, 160, 30, "#FFFFFF", aq, shadow=True)
        fmid(c, "f(g(x)): quem trabalha primeiro?", W / 2, 460, 54, "black", INK, aq)
        pause_timer(c, t, C["04.t"] + 2.2, 1500, 640, a=aq)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["05.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x = 358 + k * 400
        y = 210
        rrect(c, x - 190, y, 380, 620, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 190, y, 380, 620), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x - 170, y + 34, PURPLE if on_ else INK2, size=20, a=a, bounds=(0, 1920))
        icone(c, k, x, y + 210, 0.62, a)
        yy = y + 380
        for ln in s.split(" · "):
            yy += para_nb(c, ln, x, yy, 26, "black", INK if on_ else INK2, a, 330, 32, align="center") + 10


ONDE = [("06.a", "FÍSICA", 0, "C = (F − 32) ÷ 1,8", "a volta de F = 1,8C + 32 · energia(velocidade(t)) é composta", BLUE),
        ("06.b", "QUÍMICA", 1, "pH = −log[H⁺]", "[H⁺] = 10 elevado a −pH: um desfaz o outro", PURPLE),
        ("07.c", "FINANCEIRA", 2, "câmbio → imposto", "compor; voltar ao preço inicial é inverter", GREEN),
        ("07.d", "LINGUAGENS E TIC", 3, "codificar → decodificar", "decodificar é aplicar a inversa", AMBER)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "AS OUTRAS PROVAS", "A MESMA IDEIA, OUTRA ROUPA", BLUE)
    for k, (cue, tit, ic, lei_, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 358 + k * 400
        rrect(c, x - 190, 220 + d, 380, 600, 24, mix("#F7F7F5", col, 0.08), a)
        para(c, tit, x, 280 + d, 30, "black", col, a, 360, 36, align="center")
        area_icone(c, ic, x, 450 + d, 0.42, a)
        fit(c, lei_, x, 630 + d, 32, 340, "black", INK, a, align="center")
        para_nb(c, res, x, 680 + d, 25, "bold", INK2, a, 340, 31, align="center")


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS NA HORA H", GREEN)
    a, d = rise(t, C["08.a"])
    if a > 0:
        rrect(c, 120, 230 + d, 1000, 600, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, 1, 190, 300 + d, a, 34, bg=GREEN)
        fit(c, "ACHE A GRANDEZA INTERMEDIÁRIA", 250, 315 + d, 40, 840, "black", GREEN, a)
        rrect(c, 170, 380 + d, 900, 260, 18, "#FFFFFF", a, shadow=True)
        sub = ep(t, C["08.a"] + 2.5, 0.4)
        for j, (ante, ponte, depois) in enumerate((("n = 40t   ", "peças", " por hora"),
                                                    ("C = 500 + 3n   ", "peças", " custam"))):
            yy = 450 + j * 90 + d
            ftext(c, ante, 210, yy, 36, "black", INK, a, align="left")
            x2 = 210 + ftw(ante, 36)
            ftext(c, ponte, x2, yy, 36, "black", AMBER if sub > 0 else INK2, a, align="left")
            if sub > 0:
                line(c, x2, yy + 10, x2 + ftw(ponte, 36), yy + 10, AMBER, sub * a, 6)
        a2 = ep(t, C["08.a2"], 0.4) * a
        if a2 > 0:
            fit(c, "C(n(t)) = 500 + 120t", 620, 690 + d, 44, 820, "black", PURPLE, a2, align="center")
            selo(c, 620, 785 + d, a2, "A PONTE SOME", AMBER, -2, 32)
    for k, (cue, n, tit, sub) in enumerate((("09.b", "2", "TESTE COM UM PONTO", "f(1) = 3 → a inversa certa leva o 3 ao 1"),
                                            ("09.c", "3", "TABELA: DE DENTRO PARA FORA", "composta: g, depois f | inversa: procure nas saídas"))):
        ak, dk = rise(t, C[cue])
        if ak <= 0:
            continue
        y = 230 + k * 310
        rrect(c, 1160, y + dk, 600, 290, 24, mix("#F7F7F5", GREEN, 0.10), ak)
        badge_num(c, n, 1230, y + 60 + dk, ak, 30, bg=GREEN)
        fit(c, tit, 1285, y + 74 + dk, 34, 450, "black", GREEN, ak)
        yy = y + 150 + dk
        for ln in sub.split(" | "):
            yy += para_nb(c, ln, 1460, yy, 28, "bold", INK, ak, 540, 34, align="center") + 8


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["10.t"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["10.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["10.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["10.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone do episódio)
VF = [
    ("de dentro para fora", "em f(g(x)), f age primeiro", False, "a gente lê da esquerda para a direita",
     "primeiro g, depois f", "f(g(2)) = f(6) = 7", 0),
    ("meia e sapato", "f(x) = x + 1, g(x) = 3x: f(g(2)) ≠ g(f(2))", True, "soma e produto aceitam qualquer ordem",
     "f(g(2)) = f(6) = 7 · g(f(2)) = g(3) = 9", "7 ≠ 9", 0),
    ("compor não é multiplicar", "f(g(x)) = f(x) · g(x)", False, "os parênteses lembram multiplicação",
     "compor é pôr uma dentro da outra", "7 ≠ 3 · 6 = 18", 0),
    ("a expressão inteira", "f(x) = x² + 1 ⇒ f(x + 2) = x² + 3", False, "dá vontade de elevar só o x",
     "substitua entre parênteses: (x + 2)² + 1", "x = 1: 10, não 4", 0),
    ("o ⁻¹ não é expoente", "f⁻¹(x) = 1/f(x)", False, "o −1 parece expoente",
     "f(x) = 2x: f⁻¹(8) = 4, mas 1/f(8) = 1/16", "f⁻¹ desfaz", 2),
    ("sapato antes da meia", "a inversa de 3x + 2 é (x − 2)/3", True, "dá vontade de dividir primeiro",
     "o último passo sai primeiro · f(1) = 5 → (5 − 2)/3 = 1", "(x − 2)/3", 2),
    ("cada saída com um dono", "x² tem inversa √x em todos os reais", False, "a raiz parece desfazer o quadrado",
     "3 e −3 dão o mesmo 9: dois donos", "só com x ≥ 0", 3),
    ("o espelho certo", "o gráfico da inversa reflete no eixo y", False, "o eixo y é o espelho mais famoso",
     "o espelho é a diagonal y = x", "(2, 5) → (5, 2)", 3),
    ("de baixo para cima", "tabela: f⁻¹(b) se procura nas saídas de f", True, "o costume é olhar a linha de cima",
     "ache o b nas saídas e leia a entrada", "saídas → entrada", 3),
]
VF_IDS = [f"{11 + k:02d}" for k in range(9)]


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
    icone(c, ic, 330, 410, 0.5, a0)
    fmid(c, ctx.upper(), 960, 290, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    s = nb(conta)
    sz = 50
    while ftw(s, sz) > 760 and sz > 38:
        sz -= 2
    lines = [s] if ftw(s, sz) <= 760 else _quebra(s, sz, 760)
    riscos = []
    for j, ln in enumerate(lines):
        yj = 410 + (j - (len(lines) - 1) / 2) * (sz + 12)
        fmid(c, ln, 960, yj, sz, "black", INK, a0)
        riscos.append((ftw(ln, sz), yj + 4))
    if ar > 0 and not ver:
        for w, yl in riscos:
            strike(c, 960 - w / 2 - 10, yl, 960 + w / 2 + 10, yl, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 410, a=1 - ar)
    selo(c, 1580, 410, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        fit(c, engana, 640 if ver else 520, 552, 34, 1020 if ver else 1140, "bold", INK2, ae)
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        lns = _quebra(nb(regra_), 30, 820)
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 725 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        fit(c, fix, 1420, 735, 44, 520, "black", GREEN, ag, align="center")


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["20.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["20.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 140 + k * 140
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["20.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 620, GREEN, ab, 44)
    if ab > 0:
        rrect(c, W / 2 - 520, 700, 1040, 100, 14, mix("#FFFFFF", AMBER, 0.30), ab, shadow=True)
        text_mid(c, "a ordem ou o caminho de volta · resolva · teste", W / 2, 750, 36, "black", INK, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================

Q = {
    "q1": dict(ids=("21", "22"), titulo="QUANTO CHEGA EM REAIS?", area="CÂMBIO E IMPOSTO", ic=2, ok="E",
               enun=[("a", "Um produto custa US$ 50,00. O dólar está a R$ 5,00, e sobre o valor em reais incide imposto "
                           "de 60%.", False),
                     ("b", "Quanto a pessoa paga, em reais?", True)],
               alts=[("A", "R$ 80,00", "imposto sem converter", RED), ("B", "R$ 250,00", "esqueceu o imposto", AMBER),
                     ("C", "R$ 280,00", "imposto em dólar + reais", AMBER), ("D", "R$ 330,00", "somou 5 + 1,6", RED),
                     ("E", "R$ 400,00", "", GREEN)],
               passos=[("d", "r(d) = 5d   ·   F(r) = 1,6r"), ("a", "F(r(d)) = 1,6 · 5d = 8d"), ("a", "8 · 50 = R$ 400")],
               confere=("v", "US$ 1 → R$ 5 → R$ 8")),
    "q2": dict(ids=("23", "24"), titulo="DE DENTRO PARA FORA", area="COMPOSTA EM UM PONTO", ic=4, ok="B",
               enun=[("a", "Sejam f(x) = x + 5 e g(x) = x².", False),
                     ("b", "Quanto vale f(g(3))?", True)],
               alts=[("A", "9", "parou em g(3)", AMBER), ("B", "14", "", GREEN), ("C", "17", "somou f(3) + g(3)", RED),
                     ("D", "64", "ordem trocada: g(f(3))", RED), ("E", "72", "multiplicou f(3) · g(3)", RED)],
               passos=[("d", "1º  g(3) = 3² = 9"), ("a", "2º  f(9) = 9 + 5 = 14")],
               confere=None),
    "q3": dict(ids=("25", "26"), titulo="O CAMINHO DE VOLTA", area="CONVERSÃO DE TEMPERATURA", ic=0, ok="D",
               enun=[("a", "F = 1,8C + 32. Um termômetro marca 104 °F.", False),
                     ("b", "Quanto é, em Celsius?", True)],
               alts=[("A", "219,2 °C", "aplicou a fórmula de ida", RED), ("B", "≈ 75,6 °C", "somou o 32", RED),
                     ("C", "72 °C", "esqueceu de dividir", AMBER), ("D", "40 °C", "", GREEN),
                     ("E", "≈ 25,8 °C", "dividiu antes de subtrair", AMBER)],
               passos=[("d", "ida: × 1,8, depois + 32"), ("a", "volta: 104 − 32 = 72"), ("a", "72 ÷ 1,8 = 40 °C")],
               confere=("v", "1,8 · 40 + 32 = 104")),
    "q4": dict(ids=("27", "28"), titulo="O PONTO DA INVERSA", area="GRÁFICO DA INVERSA", ic=5, ok="C",
               enun=[("a", "O gráfico de uma função invertível f passa pelo ponto (−2, 5).", False),
                     ("b", "Por qual ponto passa o gráfico de f⁻¹?", True)],
               alts=[("A", "(−2, 5)", "o ponto do próprio f", AMBER), ("B", "(2, −5)", "mexeu nos sinais", RED),
                     ("C", "(5, −2)", "", GREEN), ("D", "(−5, 2)", "espelho errado", RED),
                     ("E", "(5, −1/2)", "usou 1/f", RED)],
               passos=[("d", "f: −2 → 5"), ("d", "f⁻¹: 5 → −2"), ("a", "(a, b) vira (b, a): (5, −2)")],
               confere=None),
    "q5": dict(ids=("29", "30"), titulo="A INVERSA NA TABELA", area="TABELAS ENCADEADAS", ic=6, ok="A",
               enun=[("b", "Calcule f⁻¹(g(4)).", True)],
               alts=[("A", "1", "", GREEN), ("B", "2", "parou em g(4)", AMBER), ("C", "3", "ignorou g: f(4)", RED),
                     ("D", "4", "usou f, não f⁻¹", RED), ("E", "não é possível: f não tem inversa", "cada saída de f é única", RED)],
               passos=[("d", "g(4) = 2"), ("a", "o 2 nas saídas de f → x = 1")],
               confere=None),
}

TAB_X = (1, 2, 3, 4)
TAB_F = (2, 4, 1, 3)
TAB_G = (3, 1, 4, 2)


def tabela_q5(c, x0, y0, a, hl_g=0.0, hl_f=0.0):
    """a tabela da Q5: linhas x, f(x), g(x); hl_g acende g(4) = 2 e hl_f acende o 2 nas saídas de f e o x = 1"""
    if a <= 0:
        return
    cw, rh = 110, 74
    rrect(c, x0, y0, cw * 5, rh * 3, 14, "#FFFFFF", a, shadow=True)
    for j, (nome, vals, col) in enumerate((("x", TAB_X, INK2), ("f(x)", TAB_F, COL_F), ("g(x)", TAB_G, COL_G))):
        y = y0 + j * rh
        if j:
            line(c, x0, y, x0 + cw * 5, y, LIGHT, a, 3)
        fmid(c, nome, x0 + cw / 2, y + rh / 2, 32, "black", col, a)
        for k, v in enumerate(vals):
            cx = x0 + cw * (k + 1.5)
            acesa = (j == 2 and k == 3 and hl_g > 0) or (j == 1 and k == 0 and hl_f > 0) or (j == 0 and k == 0 and hl_f > 0)
            if acesa:
                aa = hl_g if j == 2 else hl_f
                rrect(c, cx - 40, y + 8, 80, rh - 16, 12, GREEN, a * 0.25 * aa)
            fmid(c, str(v), cx, y + rh / 2, 36, "black", GREEN if acesa else INK, a)
    line(c, x0 + cw, y0, x0 + cw, y0 + rh * 3, LIGHT, a, 3)


def espelho_q4(c, x0, y0, s, a, prog):
    """plano com a diagonal y = x, o ponto (−2, 5) e o reflexo (5, −2)"""
    if a <= 0:
        return
    X = lambda v: x0 + s * (v + 6) / 12
    Y = lambda v: y0 + s - s * (v + 6) / 12
    rrect(c, x0 - 10, y0 - 10, s + 20, s + 20, 14, "#FFFFFF", a, shadow=True)
    line(c, X(-6), Y(0), X(6), Y(0), LIGHT, a, 3)
    line(c, X(0), Y(-6), X(0), Y(6), LIGHT, a, 3)
    line(c, X(-6), Y(-6), X(6), Y(6), GREEN, a, 4, dash=[12, 8])
    c.drawCircle(X(-2), Y(5), 11, paint(COL_F, a))
    ftext(c, "(−2, 5)", X(-2), Y(5) - 18, 22, "black", COL_F, a, align="center")
    if prog > 0:
        line(c, X(-2), Y(5), X(-2) + (X(5) - X(-2)) * prog, Y(5) + (Y(-2) - Y(5)) * prog, AMBER, a, 3, dash=[6, 6])
        if prog > 0.95:
            c.drawCircle(X(5), Y(-2), 11, paint(COL_G, a))
            ftext(c, "(5, −2)", X(5), Y(-2) + 34, 22, "black", COL_G, a, align="center")
    ftext(c, "y = x", X(5.2), Y(5.8), 20, "black", GREEN, a, align="center")


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
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        K.alternativas(c, t, C, [(L, nb(s), w, col) for L, s, w, col in d["alts"]],
                       880, 230, 820, 30, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        area_icone(c, d["ic"], 770, 222, 0.24, a0 * (1 - sol))
        if nome == "q5":
            at = ep(t, C[f"{s1}.a"], 0.4)
            hg = ep(t, C[f"{s2}.d"] + 1.0, 0.4)
            hf = ep(t, C[f"{s2}.a"] + 1.2, 0.4)
            tabela_q5(c, 190, 270 if sol <= 0 else 260, at, hg, hf)
            ab = ep(t, C[f"{s1}.b"], 0.4) * (1 - sol)
            fit(c, "Calcule f⁻¹(g(4)).", 190, 560, 40, 600, "black", BLUE, ab)
        else:
            y = 280
            for cue, s, dest in d["enun"]:
                a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
                h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
                y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 720, 760)
        if sol > 0:
            yy = 290 if nome != "q5" else 530
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.9 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 34, 640, "black", GREEN if last else INK, a)
                yy += 66
            if nome == "q4":
                espelho_q4(c, 300, yy + 10, 300, sol, ep(t, C[f"{s2}.a"], 1.0))
                yy += 330
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"] + 0.4, 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 790, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["g age primeiro em f(g(x))", "composta num ponto e a lei", "f ∘ g ≠ g ∘ f"]),
         ("31.c", "EP. 2", 1, ["eliminar a grandeza-ponte", "achar a função escondida"]),
         ("32.a", "EP. 3", 2, ["isolar x e trocar os nomes", "inversa de função racional", "f⁻¹(x) ≠ 1/f(x)"]),
         ("32.b", "EP. 4", 3, ["só bijetora tem inversa", "espelho em y = x · exp e log", "inversa em tabela"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 210), (150, 480), (990, 210), (990, 480)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, ic, x + 60, y0 + 140, 0.26, a)
        for j, it in enumerate(itens):
            yy = y0 + 40 + j * 62
            rrect(c, x + 150, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            fit(c, it, x + 198, yy + 10, 28, 580, "bold", INK, a)
    ac = ep(t, C["32.c"], 0.5)
    if ac > 0:
        boxed(c, 560, 760, 800, 90, AMBER, ac, 0.10)
        text_mid(c, "não marcou? reveja o episódio", W / 2, 805, 34, "black", INK, ac)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["33.a"], 0.5)
    ab = ep(t, C["33.b"], 0.5)
    ac = ep(t, C["33.c"], 0.5)
    for i in range(25):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["33.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 18
        x, y = 200 + k * 82, 230 + r_ * 90
        col = mix("#E6E6E2", GREEN, ab if ok else 0)
        rrect(c, x, y, 66, 72, 12, col, a)
        if ac > 0 and i < 8:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 74, 80), 14, 14), paint(BLUE, ac, stroke=4))
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "25 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "18 acertos", 1450, 400, 46, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 200, 580, 1520, 180, BLUE, ac, 0.08)
        for k, ic in enumerate((2, 0, 4)):
            area_icone(c, ic, 290 + k * 110, 670, 0.2, ac)
        text_mid(c, "8 DE CONTEXTO", 1100, 640, 46, "black", BLUE, ac)
        text_mid(c, "fórmulas encadeadas · conversões para inverter", 1100, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 260, 28, "black", GRAY, aa, tracking=2)
    text(c, "Progressão aritmética", W / 2, 350, 76, "black", PURPLE, aa)
    ab = ep(t, C["34.b"], 0.6)
    if ab > 0:
        fit(c, "uma função afim só nos números naturais", W / 2, 440, 38, 1300, "bold", INK2, ab, align="center")
    ac = ep(t, C["34.c"], 0.5)
    for k, v in enumerate((3, 7, 11, 15, 19)):
        a = ac * ep(t, C["34.c"] + 0.35 * k, 0.3)
        if a <= 0:
            continue
        x = 560 + k * 200
        c.drawCircle(x, 600, 62, paint(mix("#FFFFFF", PURPLE, 0.18), a))
        c.drawCircle(x, 600, 62, paint(PURPLE, a, stroke=5))
        fmid(c, str(v), x, 600, 52, "black", PURPLE, a)
        if k < 4:
            arrow(c, x + 66, 600, x + 134, 600, GREEN, a, 4, 12)
            ftext(c, "+4", x + 100, 560, 28, "black", GREEN, a, align="center")
    if ac > 0:
        selo(c, W / 2, 770, ac, "SEMPRE O MESMO TANTO", GREEN, -3, 34)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
