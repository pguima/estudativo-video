"""Visual — Equações e Inequações do 1º Grau, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, selo_teste...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): balança equilibrada · linha do tempo com bonequinhos ·
reta no espelho · dois carrinhos na pista.
Ícones de contexto nas questões (area_icone()): carro da locadora · caixa d'água · mãe e filha · boletim · velocímetro.
Cada questão inédita tem a ETIQUETA "x = ..." (o que a incógnita significa), que entra na resolução.
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
_s = importlib.util.spec_from_file_location("comum035", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_equacoes_inequacoes_ep5_revisao.mp4"
CARD_R = K.CARD_R
AGUA = "#5AA9E6"
PELE = "#E8B98F"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def mx(c, s, x, cy, size, col=INK, a=1.0, align="left"):
    """linha matemática de uma cor só (expr)"""
    return K.mdraw(c, s, x, cy, size, col, a, align=align)


# ======================================================================
# peças
# ======================================================================

def balanca(c, a, ang=0.0):
    """balança de dois pratos, equilibrada (ang = inclinação do travessão em graus)"""
    rrect(c, -70, 110, 140, 22, 8, INK2, a)
    rrect(c, -10, -60, 20, 175, 6, INK2, a)
    c.save(); c.translate(0, -60); c.rotate(ang)
    rrect(c, -170, -9, 340, 18, 9, INK, a)
    for sx, col, s in ((-150, BLUE, "3x + 4"), (150, GREEN, "19")):
        line(c, sx, 0, sx - 40, 90, INK2, a, 3)
        line(c, sx, 0, sx + 40, 90, INK2, a, 3)
        p = skia.Path(); p.moveTo(sx - 70, 90); p.quadTo(sx, 140, sx + 70, 90); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", col, 0.35), a))
        c.drawPath(p, paint(col, a, stroke=4))
        fmid(c, s, sx, 62, 34, "black", col, a)
    c.restore()
    c.drawCircle(0, -60, 14, paint(AMBER, a))


def boneco(c, cx, by, s, col, a=1.0):
    """bonequinho simples de pé, com os pés em by"""
    c.save(); c.translate(cx, by); c.scale(s, s)
    c.drawCircle(0, -150, 24, paint(PELE, a))
    rrect(c, -26, -122, 52, 72, 18, col, a)
    line(c, -12, -52, -16, 0, INK, a, 9)
    line(c, 12, -52, 16, 0, INK, a, 9)
    c.restore()


def linha_tempo(c, a):
    """linha do tempo HOJE → +4: os dois bonequinhos andam juntos (o tempo passa para todos)"""
    line(c, -190, 70, 190, 70, INK2, a, 5)
    for x, s in ((-130, "hoje"), (130, "+ 4 anos")):
        line(c, x, 58, x, 82, INK2, a, 5)
        text_mid(c, s, x, 112, 26, "black", INK2, a)
    for x in (-130, 130):
        boneco(c, x - 26, 40, 0.62, BLUE, a)
        boneco(c, x + 24, 40, 0.42, AMBER, a)
    arrow(c, -70, -70, 70, -70, GREEN, a, 5, 14)
    text_mid(c, "+4 · +4", 0, -108, 28, "black", GREEN, a)


def reta_espelho(c, a):
    """reta numérica com o espelho no zero: 2 < 5 vira −2 > −5"""
    line(c, -200, 40, 200, 40, INK2, a, 4)
    for v in (-5, -2, 0, 2, 5):
        x = v * 34
        line(c, x, 28, x, 52, INK2, a, 4)
        text_mid(c, str(v).replace("-", "−"), x, 84, 24, "black", INK2, a)
    rrect(c, -6, -110, 12, 140, 4, mix("#FFFFFF", BLUE, 0.55), a)
    for v, col in ((2, GREEN), (5, BLUE), (-2, GREEN), (-5, BLUE)):
        c.drawCircle(v * 34, 40, 10, paint(col, a))
    p = skia.Path(); p.moveTo(68, -10); p.quadTo(0, -80, -68, -10)
    c.drawPath(p, paint(AMBER, a, stroke=4))
    fmid(c, "o sinal vira", 0, -120, 26, "black", AMBER, a)


def carrinho(c, x, y, col, a, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    rrect(c, -50, -30, 100, 34, 10, col, a)
    rrect(c, -28, -52, 56, 26, 8, mix("#FFFFFF", col, 0.5), a)
    c.drawCircle(-28, 6, 12, paint(INK, a)); c.drawCircle(28, 6, 12, paint(INK, a))
    c.restore()


def pista(c, a):
    """dois carrinhos numa pista: B larga na frente, A alcança no empate"""
    rrect(c, -210, -90, 420, 200, 20, mix("#FFFFFF", INK2, 0.12), a)
    line(c, -200, 10, 200, 10, "#FFFFFF", a, 5)
    line(c, 90, -90, 90, 110, AMBER, a, 5)
    text_mid(c, "empate", 90, -112, 24, "black", AMBER, a)
    carrinho(c, 20, -30, GREEN, a, 0.9)
    carrinho(c, -40, 70, BLUE, a, 0.9)
    text_mid(c, "B", 20, -42, 22, "black", "#FFFFFF", a)
    text_mid(c, "A", -40, 58, 22, "black", "#FFFFFF", a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:
        balanca(c, a)
    elif k == 1:
        linha_tempo(c, a)
    elif k == 2:
        reta_espelho(c, a)
    elif k == 3:
        pista(c, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones de contexto: carro da locadora · caixa d'água · mãe e filha · boletim · velocímetro"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # carro com a placa "km"
        carrinho(c, 0, 20, BLUE, a, 1.7)
        rrect(c, -50, -110, 100, 44, 10, AMBER, a)
        text_mid(c, "km", 0, -88, 30, "black", INK, a)
    elif k == 1:    # caixa d'água com nível
        rrect(c, -90, -90, 180, 190, 16, mix("#FFFFFF", INK2, 0.15), a, shadow=True)
        rrect(c, -80, 0, 160, 90, 10, AGUA, a)
        line(c, -95, 30, 95, 30, RED, a, 4)
        text_mid(c, "600 L", 0, -40, 30, "black", RED, a)
    elif k == 2:    # mãe e filha
        boneco(c, -40, 100, 0.95, BLUE, a)
        boneco(c, 50, 100, 0.62, AMBER, a)
    elif k == 3:    # boletim
        rrect(c, -90, -110, 180, 220, 14, "#FFFFFF", a, shadow=True)
        for j, (s, col) in enumerate((("prova  ×1", INK2), ("trab.  ×2", INK2), ("média ≥ 6", GREEN))):
            text_mid(c, s, 0, -60 + j * 60, 28, "black", col, a)
    elif k == 5:    # celular com a conta do plano
        rrect(c, -60, -100, 120, 200, 18, INK, a, shadow=True)
        rrect(c, -50, -84, 100, 168, 8, mix("#FFFFFF", BLUE, 0.12), a)
        text_mid(c, "R$", 0, -40, 34, "black", BLUE, a)
        line(c, -32, 10, 32, 10, INK2, a, 5); line(c, -32, 40, 20, 40, INK2, a, 5)
    elif k == 4:    # velocímetro
        p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(-100, -100, 200, 200), 180, 180)
        c.drawPath(p, paint(INK2, a, stroke=14))
        line(c, 0, 0, 62, -62, RED, a, 7)
        c.drawCircle(0, 0, 12, paint(INK, a))
        text_mid(c, "m/s", 0, 50, 30, "black", INK, a)
    c.restore()


def etiqueta(c, s, x, y, a, size=28):
    """a etiqueta do x: 'x = ...' num cartãozinho com furo"""
    if a <= 0:
        return
    w = ftw(s, size, "black") + 70
    rrect(c, x, y - size, w, size * 2, 10, mix("#FFFFFF", AMBER, 0.35), a, shadow=True)
    c.drawCircle(x + 20, y, 7, paint("#FFFFFF", a))
    c.drawCircle(x + 20, y, 7, paint(INK2, a, stroke=2))
    ftext(c, s, x + 40, y + size * 0.35, size, "black", INK, a, align="left")


def quebra(s, size, maxw, peso="black"):
    """quebra s em linhas de no máximo maxw (respeita os espaços rígidos)"""
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


def nb(s):
    """espaço rígido: não quebra 'R$ 80,00', '600 L' nem '2 000'"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(L|km|m/s|m/s²|s|h|anos|reais)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
    return s


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        rrect(c, W / 2 - 330, 205, 660, 120, 18, "#FFFFFF", aa, shadow=True)
        mx(c, "3x + 4 = 19", W / 2, 265, 64, INK2, aa, align="center")
        strike(c, W / 2 - 230, 268, W / 2 + 230, 268, ep(t, C["01.a"] + 2.0, 0.4), RED, aa)
    itens = (("PLANO DE CELULAR", 5, BLUE), ("NOTA DE ESCOLA", 3, AMBER), ("MISTURA", 1, GREEN))
    for k, (s, ic, col) in enumerate(itens):
        a = ep(t, C["01.b"] + 1.0 * k, 0.4)
        area_icone(c, ic, 480 + k * 480, 500, 0.85, a)
        text(c, s, 480 + k * 480, 660, 30, "black", col, a)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        pill(c, "desmonte o disfarce", W / 2, 735, PURPLE, size=34, a=ac, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 840, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 840, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


COBRA = [("02.a", "PLANOS E TARIFAS", "fixo + por unidade", BLUE, "80 + 0,5k"),
         ("02.b", "FRAÇÕES DE UM TOTAL", "salário, herança", PURPLE, "1/3 + 1/4"),
         ("02.c", "MÉDIAS E NOTAS", "a nota mínima", AMBER, "média ≥ 6"),
         ("02.d", "MISTURAS", "o volume também muda", GREEN, "(10 + x)/(40 + x)"),
         ("02.e", "FÓRMULAS", "isolar uma letra", RED, "v = v₀ + at")]


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
        sz = 36
        while ftw(ex, sz) > 290:
            sz -= 2
        fmid(c, ex, x, 560 + d, sz, "black", INK, a)
        para(c, sub, x, 640 + d, 24, "bold", INK2, a, 290, 30, align="center")


TRES = [("03.a", "1", "NOMEIE A INCÓGNITA", "x = número de minutos", BLUE),
        ("03.b", "2", "NEGATIVO? INVERTA O SINAL", "÷ (−2): < vira >", AMBER),
        ("03.c", "3", "LEIA O QUE SE PEDE", "o x nem sempre é a resposta", GREEN)]


def b_tres(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "TRÊS HÁBITOS DA SEÇÃO 01", GREEN)
    for k, (cue, n, tit, sub, col) in enumerate(TRES):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 250 + d, 500, 480, 24, mix("#F7F7F5", col, 0.10), a)
        badge_num(c, n, x, 320 + d, a, 34, bg=col)
        para(c, tit, x, 420 + d, 36, "black", col, a, 440, 44, align="center")
        para(c, sub, x, 590 + d, 30, "bold", INK, a, 440, 38, align="center")
    etiqueta(c, "x = minutos", 260, 790, ep(t, C["03.a"] + 0.6, 0.4))


INDICE = [("EP. 1", "a balança equilibrada · passa dividindo com o próprio sinal · o traço da fração é um parêntese "
                    "disfarçado"),
          ("EP. 2", "a etiqueta do x · o tempo passa para todos · a raiz não é a resposta"),
          ("EP. 3", "a reta no espelho · bolinha aberta = porta fechada"),
          ("EP. 4", "a corrida dos dois planos · no empate ninguém é mais barato")]
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


ONDE = [("06.a", "FINANCEIRA", "2 000(1 + 0,02t) = 2 480", "1,24 = 1 + 0,02t", "t = 12 meses"),
        ("07.b", "FÍSICA · MUV", "30 = 10 + 4t", "20 = 4t", "t = 5 s"),
        ("07.c", "TERMÔMETRO", "86 = 1,8C + 32", "54 = 1,8C", "C = 30 °C")]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ ÁLGEBRA", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, l1, l2, res) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 250, 230 + d, 500, 440, 24, mix("#F7F7F5", BLUE, 0.06), a)
        text(c, tit, x, 300 + d, 32, "black", BLUE, a)
        for j, (s, col, sz0) in enumerate(((l1, INK, 40), (l2, INK2, 38), (res, GREEN, 48))):
            sz = sz0
            while ftw(s, sz) > 440:
                sz -= 2
            fmid(c, nb(s), x, 410 + j * 90 + d, sz, "black", col, a)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        boxed(c, 400, 720, 1120, 100, PURPLE, ad, 0.08)
        text_mid(c, "a fórmula vira equação do 1º grau: isole a incógnita", W / 2, 770, 34, "black", PURPLE, ad)


HABITOS = [("08.a", "1", "SUBSTITUA AS ALTERNATIVAS", "montagem confusa? · teste cada opção no enunciado"),
           ("08.b", "2", "CONFIRA ANTES DE MARCAR", "na inequação: · um número de dentro e um de fora"),
           ("08.c", "3", "RELEIA A PERGUNTA", "achou o x? · é isso mesmo que se pede?")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "TRÊS HÁBITOS NA HORA H", GREEN)
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
        if k == 1:
            K.selo_teste(c, x + 170, 300 + d, a, True, "dentro e fora")


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


# (contexto, afirmação (expr ou “texto”), verdadeira?, por que engana, regra certa, versão certa em expr, ícone)
VF = [
    ("dividir por negativo", "−2x > −6 → x > 3", False, "a conta do número está certa",
     "dividiu por negativo: a reta vai para o espelho", "x < 3", 2),
    ("menos antes do parêntese", "−3(x−4) = −3x + 12", True, "muita gente escreve −12",
     "menos vezes menos dá mais", "−3 · (−4) = +12", 0),
    ("menos antes da fração", "−{x−4}/3 = {−x−4}/3", False, "o 4 parece longe do menos",
     "o traço é um parêntese disfarçado", "{−x+4}/3", 0),
    ("passar dividindo", "−2x = 10 → x = 5", False, "10 ÷ 2 é 5",
     "passa dividindo com o próprio sinal", "x = −5", 0),
    ("desigualdade estrita", "n > 800 → menor inteiro: 800", False, "o 800 apareceu na conta",
     "maior que é estrito: porta fechada no 800", "801", 2),
    ("idades", "“daqui a 4 anos, o pai terá o triplo do filho” → p + 4 = 3f", False, "o pai aparece primeiro",
     "o tempo passa para todos", "p+4 = 3(f+4)", 1),
    ("frações", "1/3 + 1/4 = 7/12", True, "a tentação é somar em cima e embaixo: 2/7",
     "frações se somam pelo MMC", "4/12 + 3/12", 0),
    ("mistura", "40 L com 10 L de álcool + 10 L de álcool → 20/40", False, "só lembramos do álcool que entrou",
     "o volume total também cresce", "20/50", 1),
    ("a pergunta", "“o valor de x costuma estar nas alternativas como armadilha”", True,
     "achar o x dá sensação de missão cumprida", "a raiz não é a resposta: releia a pergunta", "x ≠ resposta", 3),
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
    texto = conta.startswith("“") or "→" in conta and not conta.startswith("−2")
    if texto:
        sz = 46
        while ftw(nb(conta), sz) > 740 and sz > 38:
            sz -= 2
        lines = [nb(conta)] if ftw(nb(conta), sz) <= 740 else quebra(nb(conta), sz, 740)
        riscos = []
        for j, ln in enumerate(lines):
            yj = 410 + (j - (len(lines) - 1) / 2) * (sz + 12)
            fmid(c, ln, 960, yj, sz, "black", INK, a0)
            riscos.append((ftw(ln, sz), yj + 4))
    else:
        sz = 66
        while K.math_w(conta, sz) > 720:
            sz -= 2
        w = mx(c, conta, 960, 410, sz, INK, a0, align="center")
        riscos = [(w, 415)]
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
    etiqueta(c, "x = o que a letra significa", W / 2 - 300, 750, ab, 34)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto ou "=expr", destaque?) · etq: etiqueta do x · passos: (cue, texto ou "=expr") · confere: (cue, texto)

Q = {
    "q1": dict(ids=("20", "21"), titulo="A LOCADORA", area="PONTO DE EQUILÍBRIO", ic=0, ok="B",
               enun=[("a", "Uma locadora tem dois planos por dia. Plano A: R$ 80,00 + R$ 0,50 por km. "
                           "Plano B: R$ 50,00 + R$ 0,80 por km.", False),
                     ("b", "Os planos empatam em quantos km, e qual compensa num passeio de 150 km?", True)],
               alts=[("A", "30 km; o plano A", "parou no 30 = 0,3k", AMBER), ("B", "100 km; o plano A", "", GREEN),
                     ("C", "100 km; o plano B", "inverteu o vencedor", RED),
                     ("D", "130 km; o plano B", "preço no lugar de km", RED),
                     ("E", "155 km; o plano A", "preço no lugar de km", RED)],
               etq="k = distância, em km",
               passos=[("a", "=80 + 0,5k = 50 + 0,8k"), ("b", "=30 = 0,3k → k = 100"),
                       ("c", "150 km: A R$ 155 · B R$ 170")],
               confere=("b", "em 100 km: R$ 130 nos dois")),
    "q2": dict(ids=("22", "23"), titulo="A CAIXA D'ÁGUA", area="INEQUAÇÃO · RESPOSTA INTEIRA", ic=1, ok="D",
               enun=[("a", "Uma caixa d'água tem 2 000 L e perde 70 L por hora. Um alarme toca quando ela tiver MENOS "
                           "de 600 L.", False),
                     ("b", "Depois de quantas horas completas, no mínimo, o alarme já estará tocando?", True)],
               alts=[("A", "9", "usou só os 600 L", RED), ("B", "19", "não inverteu o sinal", AMBER),
                     ("C", "20", "o empate", AMBER), ("D", "21", "", GREEN), ("E", "29", "esvaziou a caixa", RED)],
               etq="t = tempo, em horas",
               passos=[("a", "=2 000 − 70t < 600"), ("b", "=−70t < −1 400 → t > 20"),
                       ("c", "20 h: 600 L (ainda não é menos)")],
               confere=("v", "21 h: 530 L · toca")),
    "q3": dict(ids=("24", "25"), titulo="MÃE E FILHA", area="IDADES · HÁ 5 ANOS", ic=2, ok="C",
               enun=[("a", "Hoje, a soma das idades de uma mãe e de sua filha é 50 anos. Há 5 anos, a mãe tinha o "
                           "quádruplo da idade da filha.", False),
                     ("b", "Hoje, a idade da MÃE é", True)],
               alts=[("A", "13 anos", "respondeu o x", AMBER), ("B", "32 anos", "a mãe há 5 anos", RED),
                     ("C", "37 anos", "", GREEN), ("D", "40 anos", "ignorou os 5 anos", RED),
                     ("E", "41 anos", "−5 só na mãe", RED)],
               etq="f = idade da filha hoje",
               passos=[("a", "=(50−f) − 5 = 4(f−5)"), ("b", "=65 = 5f → f = 13"),
                       ("c", "mãe: 50 − 13 = 37 anos")],
               confere=("v", "há 5 anos: 32 = 4 · 8")),
    "q4": dict(ids=("26", "27"), titulo="A NOTA MÍNIMA", area="MÉDIA PONDERADA", ic=3, ok="B",
               enun=[("a", "A prova tem peso 1 e o trabalho tem peso 2. Para passar, a média tem que ser no mínimo 6,0. "
                           "Um aluno tirou 4,0 na prova.", False),
                     ("b", "A menor nota que ele precisa no trabalho é", True)],
               alts=[("A", "6,0", "a própria média", AMBER), ("B", "7,0", "", GREEN),
                     ("C", "8,0", "média simples", RED), ("D", "10,0", "trocou os pesos", RED),
                     ("E", "14,0", "não dividiu por 2", RED)],
               etq="T = nota do trabalho",
               passos=[("a", "={4+2T}/3 ≥ 6"), ("b", "=4 + 2T ≥ 18 → T ≥ 7")],
               confere=("v", "T = 7: (4 + 14) ÷ 3 = 6")),
    "q5": dict(ids=("28", "29"), titulo="O CARRO ACELERANDO", area="ISOLAR A INCÓGNITA", ic=4, ok="A",
               enun=[("a", "Na Física, v = v₀ + at. Um carro está a 12 m/s e acelera 1,5 m/s² até chegar a 30 m/s.",
                      False),
                     ("b", "O tempo, em segundos, é", True)],
               alts=[("A", "12", "", GREEN), ("B", "18", "parou na variação", AMBER),
                     ("C", "20", "esqueceu o v₀", RED), ("D", "27", "multiplicou", RED),
                     ("E", "28", "somou o 12", RED)],
               etq="t = tempo, em segundos",
               passos=[("a", "=30 = 12 + 1,5t"), ("b", "=18 = 1,5t → t = 12")],
               confere=("v", "12 + 1,5 · 12 = 30 m/s")),
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
    """um passo da resolução: '=conta' (expr, com os milhares protegidos) ou texto simples. Devolve a altura."""
    if ln.startswith("="):
        s = ln[1:]
        if re.search(r"\d \d{3}", s) or "→" in s:
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
        area_icone(c, d["ic"], 770, 222, 0.42, a0)
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
            etiqueta(c, d["etq"], 180, 315, ad, 30)
            yy = 410
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4) * sol
                last = j == len(d["passos"]) - 1
                yy += linha_passo(c, s, 180, yy, a, GREEN if last else INK) + 8
            if d["confere"]:
                cue, s = d["confere"]
                sz = 30
                while ftw(nb(s), sz) > 580:
                    sz -= 2
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, sz)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("30.b", "EP. 1", 0, ["resolver: a mesma operação nos dois pratos", "menos antes do parêntese, sem errar sinal",
                               "denominadores pelo MMC (o traço é parêntese)", "0x = k: nenhuma solução · 0x = 0: infinitas"]),
         ("30.c", "EP. 2", 1, ["montar a equação, com a etiqueta do x", "idades: o tempo passa para todos",
                               "misturas: o volume total também muda"]),
         ("31.a", "EP. 3", 2, ["inverter o sinal com negativo", "reta, intervalo e inequação dupla",
                               "o menor inteiro de uma desigualdade estrita"]),
         ("31.b", "EP. 4", 3, ["ponto de equilíbrio entre dois planos"]),
         ("31.c", "EP. 5", None, ["conferir substituindo e reler a pergunta"])]


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
            K.selo_teste(c, x + 40, y0 + 62, a, True, "confira")
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
        if ac > 0 and i < 15:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 4, y - 4, 74, 80), 14, 14), paint(BLUE, ac, stroke=4))
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 300, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 400, 46, "black", GREEN, ab)
    if ac > 0:
        boxed(c, 200, 580, 1520, 180, BLUE, ac, 0.08)
        icone(c, 3, 360, 670, 0.5, ac)
        text_mid(c, "METADE: planos e inequações", 1020, 640, 44, "black", BLUE, ac)
        text_mid(c, "com resposta inteira (n > 800 → 801)", 1020, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["33.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 260, 28, "black", GRAY, aa, tracking=2)
    text(c, "Equação do 2º grau e Bhaskara", W / 2, 350, 62, "black", PURPLE, aa)
    ab = ep(t, C["33.b"], 0.5)
    if ab > 0:
        rrect(c, W / 2 - 420, 470, 840, 200, 24, mix("#FFFFFF", PURPLE, 0.10), ab, shadow=True)
        mx(c, "x^2 = 9", W / 2 - 150, 570, 70, INK, ab, align="center")
        arrow(c, W / 2 + 10, 570, W / 2 + 110, 570, GREEN, ab, 6, 16)
        mx(c, "x = ±3", W / 2 + 250, 570, 70, GREEN, ab, align="center")
        text(c, "o x ao quadrado · duas respostas", W / 2, 760, 38, "black", INK2, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["34.like"], C["34.sub"], C["34.bell"], C["34.com"], C["34.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["34.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, tres=b_tres, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
