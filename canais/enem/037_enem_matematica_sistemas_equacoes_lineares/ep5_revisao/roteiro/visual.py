"""Visual — Sistemas de Equações Lineares, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, selo_teste...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): cercado de galinhas e coelhos · duas notas fiscais ·
trilhos paralelos · balança com duplas.
Ícones de contexto nas questões (area_icone()): cédulas · figurinhas · pipoca e refrigerante · plano cartesiano · irmãos.
Cada questão inédita tem as ETIQUETAS das duas incógnitas, que entram na resolução.
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
_s = importlib.util.spec_from_file_location("comum037", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, which, para, boxed, selo, pause_timer, chip = (K.frame, K.which, K.para, K.boxed, K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_sistemas_lineares_ep5_revisao.mp4"
CARD_R = K.CARD_R
PELE = "#E8B98F"
GRAMA = "#CFE8B5"
CERCA = "#B07B4A"
GALINHA = "#FFF4D6"
COELHO = "#D9D4CC"
PIPOCA = "#FFE9A8"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


def mx(c, s, x, cy, size, col=INK, a=1.0, align="left"):
    """linha matemática de uma cor só (expr)"""
    return K.mdraw(c, s, x, cy, size, col, a, align=align)


def nb(s):
    """espaço rígido: não quebra 'R$ 700', '30 cédulas' nem '2 000'"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(anos|cédulas|figurinhas|km|h)\b)", " ", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", " ", s)
    return s


def fit(c, s, x, y, size, maxw, peso, col, a, align="left"):
    """texto numa linha só, encolhendo até caber em maxw"""
    s = nb(s)
    while ftw(s, size, peso) > maxw and size > 18:
        size -= 1
    ftext(c, s, x, y, size, peso, col, a, align=align)
    return size


# ======================================================================
# peças
# ======================================================================

def boneco(c, cx, by, s, col, a=1.0):
    """bonequinho simples de pé, com os pés em by"""
    c.save(); c.translate(cx, by); c.scale(s, s)
    c.drawCircle(0, -150, 24, paint(PELE, a))
    rrect(c, -26, -122, 52, 72, 18, col, a)
    line(c, -12, -52, -16, 0, INK, a, 9)
    line(c, 12, -52, 16, 0, INK, a, 9)
    c.restore()


def galinha(c, cx, cy, s, a):
    c.drawCircle(cx, cy, s * 0.5, paint(GALINHA, a))
    c.drawCircle(cx, cy, s * 0.5, paint("#C9B48E", a, stroke=2))
    for k in (-1, 0, 1):
        c.drawCircle(cx + k * s * 0.12, cy - s * 0.52, s * 0.1, paint(RED, a))
    p = skia.Path(); p.moveTo(cx + s * 0.46, cy - s * 0.04); p.lineTo(cx + s * 0.68, cy + s * 0.04)
    p.lineTo(cx + s * 0.46, cy + s * 0.12); p.close()
    c.drawPath(p, paint(AMBER, a))
    c.drawCircle(cx + s * 0.18, cy - s * 0.1, s * 0.06, paint(INK, a))


def coelho(c, cx, cy, s, a):
    for k in (-1, 1):
        c.drawOval(skia.Rect.MakeXYWH(cx + k * s * 0.2 - s * 0.1, cy - s * 1.0, s * 0.2, s * 0.6), paint(COELHO, a))
    c.drawCircle(cx, cy, s * 0.5, paint(COELHO, a))
    c.drawCircle(cx, cy, s * 0.5, paint("#8E877E", a, stroke=2))
    for k in (-1, 1):
        c.drawCircle(cx + k * s * 0.17, cy - s * 0.08, s * 0.06, paint(INK, a))


def cercado(c, a):
    """ep1: o cercado com galinhas e coelhos"""
    rrect(c, -190, -110, 380, 220, 22, GRAMA, a)
    for k in range(7):
        x = -190 + k * 380 / 6
        rrect(c, x - 6, -130, 12, 40, 4, CERCA, a)
        rrect(c, x - 6, 90, 12, 40, 4, CERCA, a)
    line(c, -190, -112, 190, -112, CERCA, a, 6)
    line(c, -190, 112, 190, 112, CERCA, a, 6)
    for k, (x, y) in enumerate(((-120, -20), (-40, 50), (50, -20), (130, 50))):
        (galinha if k % 2 == 0 else coelho)(c, x, y, 70, a)


def nota_fiscal(c, x, y, a, linhas, total, col):
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + 150, y); p.lineTo(x + 150, y + 190)
    for k in range(6):
        p.lineTo(x + 150 - 12.5 - k * 25, y + 200); p.lineTo(x + 150 - 25 - k * 25, y + 190)
    p.close()
    c.drawPath(p, paint("#FFFFFF", a))
    c.drawPath(p, paint(col, a, stroke=4))
    for j, s in enumerate(linhas):
        ftext(c, s, x + 16, y + 44 + j * 38, 26, "black", INK2, a, align="left")
    line(c, x + 14, y + 128, x + 136, y + 128, INK2, a, 2)
    ftext(c, total, x + 16, y + 168, 28, "black", col, a, align="left")


def notas(c, a):
    """ep2: juntar as duas notas fiscais"""
    nota_fiscal(c, -200, -110, a, ["2 S", "1 J"], "R$ 31", BLUE)
    fmid(c, "+", 0, -10, 70, "black", GREEN, a)
    nota_fiscal(c, 50, -110, a, ["1 S", "2 J"], "R$ 26", PURPLE)


def trilhos(c, a):
    """ep3: trilhos paralelos que nunca se encontram"""
    for k in range(9):
        x = -180 + k * 45
        rrect(c, x - 9, -100, 18, 200, 4, CERCA, a)
    for y in (-60, 60):
        line(c, -210, y, 210, y, INK2, a, 12)
    fmid(c, "0 = 2", 0, 150, 40, "black", RED, a)


def balanca_duplas(c, a):
    """ep4: a balança das pesagens em dupla"""
    rrect(c, -70, 110, 140, 22, 8, INK2, a)
    rrect(c, -10, -60, 20, 175, 6, INK2, a)
    rrect(c, -170, -69, 340, 18, 9, INK, a)
    for sx, col in ((-130, BLUE), (130, GREEN)):
        line(c, sx, -60, sx - 40, 30, INK2, a, 3)
        line(c, sx, -60, sx + 40, 30, INK2, a, 3)
        p = skia.Path(); p.moveTo(sx - 70, 30); p.quadTo(sx, 80, sx + 70, 30); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", col, 0.35), a))
        c.drawPath(p, paint(col, a, stroke=4))
    boneco(c, -150, 30, 0.42, BLUE, a); boneco(c, -110, 30, 0.42, AMBER, a)
    boneco(c, 110, 30, 0.42, AMBER, a); boneco(c, 150, 30, 0.42, GREEN, a)
    c.drawCircle(0, -60, 14, paint(AMBER, a))
    fmid(c, "÷ 2", 0, -115, 36, "black", GREEN, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    (cercado, notas, trilhos, balanca_duplas)[k](c, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones de contexto: cédulas · figurinhas · pipoca e refrigerante · plano cartesiano · três irmãos"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # cédulas de 10 e de 50
        for j, (v, col) in enumerate((("10", "#E29A6B"), ("50", "#C9A54A"))):
            x, y = -150 + j * 90, -70 + j * 50
            rrect(c, x, y, 220, 110, 10, mix("#FFFFFF", col, 0.55), a, shadow=True)
            rrect(c, x + 10, y + 10, 200, 90, 8, mix("#FFFFFF", col, 0.25), a)
            fmid(c, v, x + 110, y + 55, 50, "black", INK, a)
    elif k == 1:    # figurinhas
        for j in range(3):
            c.save(); c.rotate(-12 + j * 12)
            rrect(c, -60, -90, 120, 170, 12, "#FFFFFF", a, shadow=True)
            rrect(c, -48, -78, 96, 110, 8, mix("#FFFFFF", (BLUE, GREEN, AMBER)[j], 0.45), a)
            c.restore()
        boneco(c, 0, 20, 0.42, AMBER, a)
    elif k == 2:    # pipoca e refrigerante
        p = skia.Path(); p.moveTo(-170, -40); p.lineTo(-30, -40); p.lineTo(-50, 110); p.lineTo(-150, 110); p.close()
        c.drawPath(p, paint(RED, a))
        for j in range(4):
            line(c, -150 + j * 33, -40, -140 + j * 28, 110, "#FFFFFF", a, 8)
        for j, (x, y) in enumerate(((-140, -60), (-100, -75), (-60, -60), (-120, -90), (-80, -95))):
            c.drawCircle(x, y, 26, paint(PIPOCA, a))
        rrect(c, 40, -60, 110, 170, 12, BLUE, a)
        rrect(c, 40, -10, 110, 50, 0, "#FFFFFF", a)
        line(c, 110, -60, 130, -120, INK2, a, 6)
    elif k == 3:    # plano cartesiano (sem as retas da resposta)
        rrect(c, -150, -130, 300, 260, 14, "#FFFFFF", a, shadow=True)
        for j in range(-4, 5):
            line(c, j * 30, -115, j * 30, 115, mix("#FFFFFF", INK2, 0.2), a, 1)
            line(c, -135, j * 26, 135, j * 26, mix("#FFFFFF", INK2, 0.2), a, 1)
        arrow(c, -135, 0, 140, 0, INK2, a, 4, 12)
        arrow(c, 0, 115, 0, -125, INK2, a, 4, 12)
        fmid(c, "r · s ?", 70, -80, 30, "black", PURPLE, a)
    elif k == 4:    # três irmãos
        boneco(c, -90, 110, 0.72, BLUE, a)
        boneco(c, 0, 110, 0.9, GREEN, a)
        boneco(c, 90, 110, 0.62, AMBER, a)
    c.restore()


def etiqueta(c, s, x, y, a, size=28):
    """a etiqueta de uma incógnita: 'd = ...' num cartãozinho com furo"""
    if a <= 0:
        return 0
    w = ftw(s, size, "black") + 70
    rrect(c, x, y - size, w, size * 2, 10, mix("#FFFFFF", AMBER, 0.35), a, shadow=True)
    c.drawCircle(x + 20, y, 7, paint("#FFFFFF", a))
    c.drawCircle(x + 20, y, 7, paint(INK2, a, stroke=2))
    ftext(c, s, x + 40, y + size * 0.35, size, "black", INK, a, align="left")
    return w


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


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


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    itens = (("INTEIRAS E MEIAS", BLUE), ("CARROS E MOTOS", GREEN), ("CAFÉ CARO E BARATO", AMBER))
    for k, (s, col) in enumerate(itens):
        a, d = rise(t, C["01.a"] + 0.9 * k)
        if a <= 0:
            continue
        x = 400 + k * 560
        rrect(c, x - 240, 220 + d, 480, 130, 22, mix("#FFFFFF", col, 0.14), a, shadow=True)
        text_mid(c, s, x, 285 + d, 36, "black", col, a)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, W / 2 - 360, 410, 720, 210, 24, "#FFFFFF", ab, shadow=True)
        mx(c, "i + m = 300", W / 2, 470, 54, BLUE, ab, align="center")
        mx(c, "40i + 20m = 8400", W / 2, 560, 54, PURPLE, ab, align="center")
        text_mid(c, "DUAS CONDIÇÕES AO MESMO TEMPO", W / 2, 655, 28, "black", INK2, ab)
    ac = ep(t, C["01.c"], 0.5)
    if ac > 0:
        pill(c, "a conta é curta · o que decide é a TRADUÇÃO", W / 2, 740, PURPLE, size=32, a=ac, anchor="center")
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 850, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 850, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


COBRA = [("02.a", "QUANTIDADE E VALOR", "ingressos de dois preços", BLUE, "i + m = 300"),
         ("02.b", "CABEÇAS E PATAS", "animais, veículos, rodas", GREEN, "2g + 4c = 28"),
         ("02.c", "MISTURAS", "dois cafés, duas soluções", AMBER, "10a + 20b = ?"),
         ("02.d", "COMBOS DE COMPRAS", "2 sanduíches + 1 suco", PURPLE, "2S + J = ?"),
         ("02.e", "GRÁFICOS", "onde duas retas se cruzam", RED, "(2, 3)")]


def b_cobra(c, t, C, B):
    frame(c, t, B["start"], "AS CINCO FANTASIAS", "COMO O SISTEMA APARECE", BLUE)
    for k, (cue, tit, sub, col, ex) in enumerate(COBRA):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 250 + d, 330, 480, 24, mix("#F7F7F5", col, 0.08), a)
        badge_num(c, k + 1, x, 310 + d, a, 28, bg=col)
        para(c, tit, x, 390 + d, 28, "black", col, a, 290, 36, align="center")
        sz = 40
        while ftw(ex, sz) > 290:
            sz -= 2
        fmid(c, nb(ex), x, 560 + d, sz, "black", INK, a)
        para(c, sub, x, 640 + d, 24, "bold", INK2, a, 290, 30, align="center")


def b_rende(c, t, C, B):
    frame(c, t, B["start"], "O QUE MAIS RENDE", "ANTES DE QUALQUER CONTA", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        boxed(c, 200, 240, 1520, 170, AMBER, aa, 0.08)
        text(c, "1 · NOMEIE AS INCÓGNITAS, COM UNIDADE", 260, 300, 36, "black", AMBER, aa, align="left")
        etiqueta(c, "i = nº de ingressos inteiros", 260, 360, ep(t, C["03.a"] + 0.8, 0.4), 28)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        boxed(c, 200, 440, 1520, 150, BLUE, ab, 0.08)
        text(c, "2 · UMA EQUAÇÃO PARA CADA INFORMAÇÃO", 260, 500, 36, "black", BLUE, ab, align="left")
        text(c, "“ao todo” · “o dobro” · “a mesma quantia”", 260, 555, 28, "bold", INK2, ab, align="left")
    ac = ep(t, C["03.c"], 0.5)
    if ac > 0:
        boxed(c, 200, 620, 1520, 170, GREEN, ac, 0.08)
        text(c, "3 · OLHE A PERGUNTA ANTES DE RESOLVER", 260, 680, 36, "black", GREEN, ac, align="left")
        mx(c, "x + y = ?", 1400, 705, 60, GREEN, ac, align="center")
        text(c, "às vezes ela já é uma combinação", 260, 740, 28, "bold", INK2, ac, align="left")


INDICE = [("EP. 1", "duas incógnitas, duas pistas · trocar a peça, com parênteses · tudo de um tipo"),
          ("EP. 2", "juntar as notas fiscais · comprar o mesmo pedido 3 vezes"),
          ("EP. 3", "estrada de soluções e o cruzamento · 0 = 2: trilhos que nunca se encontram"),
          ("EP. 4", "a escada do escalonado · cada um sobe 2 vezes na balança")]
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


ONDE = [("06.a", "FÍSICA", ["sA = 20 + 80t", "sB = 200 − 100t", "180t = 180"], "t = 1 h · km 100", BLUE),
        ("07.b", "QUÍMICA", ["soluto antes", "= soluto depois"], "a equação dos valores", PURPLE),
        ("07.c", "GEOMETRIA", ["duas retas", "um ponto comum"], "o cruzamento", AMBER),
        ("07.d", "FUNÇÃO AFIM", ["custo A = custo B"], "próximas séries", GREEN)]


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ MATEMÁTICA", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, ls, res, col) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 220 + d, 410, 470, 24, mix("#F7F7F5", col, 0.08), a)
        text(c, tit, x, 290 + d, 32, "black", col, a)
        for j, s in enumerate(ls):
            fit(c, s, x, 390 + j * 70 + d, 36, 360, "black", INK, a, align="center")
        fit(c, res, x, 640 + d, 32, 360, "black", col, a, align="center")
    ad = ep(t, C["07.d"] + 2.2, 0.5)
    if ad > 0:
        boxed(c, 400, 730, 1120, 90, INK2, ad, 0.06)
        text_mid(c, "determinante e Cramer: série de Determinantes", W / 2, 775, 32, "black", INK2, ad)


HABITOS = [("08.a", "1", "UMA EQUAÇÃO POR INFORMAÇÃO", "só achou uma? · releia: “ao todo”, “o dobro”"),
           ("08.b", "2", "MÉTODO PELO FORMATO", "coeficiente 1: substituição · opostos: adição · total: some tudo"),
           ("09.c", "3", "CONFIRA NA OUTRA EQUAÇÃO", "a que você não usou · por último"),
           ("09.d", "4", "RESPONDA A PERGUNTA", "não a incógnita · a outra está nas alternativas")]


def b_habitos(c, t, C, B):
    frame(c, t, B["start"], "ESTRATÉGIA DE PROVA", "QUATRO HÁBITOS NA HORA H", GREEN)
    for k, (cue, n, tit, sub) in enumerate(HABITOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 285 + k * 450
        rrect(c, x - 205, 240 + d, 410, 520, 24, mix("#F7F7F5", GREEN, 0.10), a)
        badge_num(c, n, x, 310 + d, a, 34, bg=GREEN)
        para(c, tit, x, 400 + d, 32, "black", GREEN, a, 360, 40, align="center")
        yy = 560 + d
        for ln in sub.split(" · "):
            yy += para(c, ln, x, yy, 26, "bold", INK, a, 360, 34, align="center") + 10
        if k == 2:
            K.selo_teste(c, x + 140, 300 + d, a, True, "nas duas")


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


# (contexto, afirmação (texto), verdadeira?, por que engana, regra certa, versão certa, ícone)
VF = [
    ("tradução", "“Rita tem o dobro de Léo” → 2R = L", False, "o 2 aparece perto da Rita",
     "teste: Léo 5, Rita 10", "R = 2L", 0),
    ("substituição", "m = 20 − c em 3c + 2m → 3c + 40 − c", False, "o 40 saiu certo",
     "a peça entra com parênteses: o 2 multiplica tudo", "3c + 40 − 2c", 0),
    ("multiplicar", "(x + 2y = 7) × 3 → 3x + 6y = 21", True, "muita gente esquece o 7",
     "comprar o mesmo pedido 3 vezes: o valor também triplica", "7 × 3 = 21", 1),
    ("a pergunta", "achei c = 12 carros; pediram motos → marco 12", False, "achar a incógnita parece o fim",
     "responda a pergunta, não a incógnita", "motos = ?", 0),
    ("“se der k”", "“se Ana der 4 balas a Bia, ficam iguais” → A − 4 = B + 4", True, "muita gente só tira de quem dá",
     "quem recebe também muda", "−4 e +4", 0),
    ("a combinação", "pediram x + y → tenho que achar x e y", False, "parece que sempre se resolve tudo",
     "junte as notas fiscais: some as equações", "some!", 1),
    ("0 = 5", "a conta deu 0 = 5 → errei a conta", False, "0 = 5 parece um absurdo",
     "o absurdo é a resposta: trilhos que nunca se encontram", "impossível", 2),
    ("0 = 0", "a conta deu 0 = 0 → a solução é (0, 0)", False, "o zero parece a resposta",
     "a mesma estrada desenhada duas vezes", "infinitas", 2),
    ("duplas", "A + B, B + C e A + C somam 60 → A + B + C = 30", True, "a tentação é dizer 60",
     "cada um sobe duas vezes na balança: ÷ 2", "60 ÷ 2 = 30", 3),
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
    icone(c, ic, 330, 400, 0.5, a0)
    text(c, ctx.upper(), 960, 300, 30, "black", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    s = nb(conta)
    sz = 46
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
        lns = _quebra(regra_, 30, 820)
        for j, ln in enumerate(lns):
            ftext(c, ln, 240, 725 + (j - (len(lns) - 1) / 2) * 44, 30, "black", GREEN, ag, align="left")
        fit(c, fix, 1420, 735, 52, 500, "black", GREEN, ag, align="center")


def _quebra(s, size, maxw, peso="black"):
    out, cur = [], ""
    for w in s.split(" "):
        tst = (cur + " " + w).strip(" ")
        if cur and ftw(tst, size, peso) > maxw:
            out.append(cur); cur = w
        else:
            cur = tst
    return out + ([cur] if cur else [])


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
    w1 = ftw("x = o que a letra é", 32) + 70
    etiqueta(c, "x = o que a letra é", W / 2 - w1 - 20, 750, ab, 32)
    etiqueta(c, "y = a outra", W / 2 + 20, 750, ab, 32)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · etqs: etiquetas das incógnitas · passos: (cue, texto) · confere: (cue, texto)

Q = {
    "q1": dict(ids=("21", "22"), titulo="AS CÉDULAS", area="QUANTIDADE E VALOR", ic=0, ok="B",
               enun=[("a", "Um caixa tem 30 cédulas, umas de R$ 10 e outras de R$ 50, somando R$ 700.", False),
                     ("b", "Quantas são as cédulas de R$ 10?", True)],
               alts=[("A", "10", "a outra incógnita", AMBER), ("B", "20", "", GREEN), ("C", "30", "o total", RED),
                     ("D", "40", "400 ÷ 10, não ÷ 40", RED), ("E", "70", "como se todas fossem de 10", RED)],
               etqs=["d = cédulas de R$ 10", "c = cédulas de R$ 50"],
               passos=[("a", "d + c = 30 · 10d + 50c = 700"), ("b", "30 de R$ 10 = 300 · faltam 400"),
                       ("b", "cada troca soma 40 → c = 10"), ("c", "d = 30 − 10 = 20")],
               confere=("v", "200 + 500 = 700")),
    "q2": dict(ids=("23", "24"), titulo="AS FIGURINHAS", area="O TRIPLO E “SE DER 10”", ic=1, ok="D",
               enun=[("a", "Ana tem o triplo das figurinhas de Bruno. Se Ana der 10 figurinhas a Bruno, os dois ficam "
                           "com a mesma quantidade.", False),
                     ("b", "Quantas figurinhas Ana tem?", True)],
               alts=[("A", "10", "é o Bruno", AMBER), ("B", "15", "quem recebe não mudou", RED),
                     ("C", "20", "depois da troca", AMBER), ("D", "30", "", GREEN), ("E", "40", "o total", RED)],
               etqs=["a = figurinhas de Ana", "b = figurinhas de Bruno"],
               passos=[("a", "a = 3b   (teste: 2 e 6)"), ("b", "a − 10 = b + 10"),
                       ("c", "3b − 10 = b + 10 → b = 10"), ("c", "a = 30")],
               confere=("v", "depois: 20 e 20")),
    "q3": dict(ids=("25", "26"), titulo="O COMBO DO CINEMA", area="A PERGUNTA JÁ É A SOMA", ic=2, ok="C",
               enun=[("a", "No cinema, 3 pipocas e 1 refrigerante custam R$ 50; 1 pipoca e 3 refrigerantes custam "
                           "R$ 38.", False),
                     ("b", "Quanto custam, juntos, 1 pipoca e 1 refrigerante?", True)],
               alts=[("A", "R$ 8", "só o refrigerante", AMBER), ("B", "R$ 14", "só a pipoca", AMBER),
                     ("C", "R$ 22", "", GREEN), ("D", "R$ 44", "÷ 2: são 4 de cada", RED),
                     ("E", "R$ 88", "as duas compras", RED)],
               etqs=["p = pipoca (R$)", "r = refrigerante (R$)"],
               passos=[("a", "pedem p + r: some as notas"), ("a", "4p + 4r = 88"), ("b", "p + r = 88 ÷ 4 = 22")],
               confere=("v", "p = 14, r = 8: 50 e 38")),
    "q4": dict(ids=("27", "28"), titulo="DUAS RETAS", area="CLASSIFICAR O SISTEMA", ic=3, ok="E",
               enun=[("a", "Num aplicativo, alguém desenhou as retas r: 3x − y = 4 e s: 6x − 2y = 5.", False),
                     ("b", "Sobre as retas e o sistema, é correto dizer:", True)],
               alts=[("A", "concorrentes, em (1, −1)", "testou só em r", AMBER),
                     ("B", "coincidentes, infinitas soluções", "só o lado esquerdo", RED),
                     ("C", "0 = 3: houve erro de cálculo", "o absurdo é a resposta", RED),
                     ("D", "concorrentes, em (0, 0)", "zero não é resposta", RED),
                     ("E", "paralelas, sem solução", "", GREEN)],
               etqs=[],
               passos=[("a", "esquerda: 6 e −2 = o dobro de 3 e −1"), ("b", "direita: o dobro de 4 seria 8 ≠ 5"),
                       ("c", "2r − s:  0 = 3 → trilhos")],
               confere=None),
    "q5": dict(ids=("29", "30"), titulo="OS TRÊS IRMÃOS", area="TRÊS INCÓGNITAS · DUPLAS", ic=4, ok="A",
               enun=[("a", "Três irmãos: Ana e Bia somam 31 anos; Bia e Caio, 37; Ana e Caio, 28.", False),
                     ("b", "Qual é a idade de Ana?", True)],
               alts=[("A", "11 anos", "", GREEN), ("B", "14 anos", "dividiu uma dupla", RED),
                     ("C", "17 anos", "é o Caio", AMBER), ("D", "20 anos", "é a Bia", AMBER),
                     ("E", "59 anos", "não dividiu por 2", RED)],
               etqs=["A, B, C = idades"],
               passos=[("a", "31 + 37 + 28 = 96"), ("a", "96 ÷ 2 = 48 (os três)"), ("b", "Ana = 48 − 37 = 11")],
               confere=("v", "Bia 20 · Caio 17 · 11 + 20 = 31")),
}


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
        area_icone(c, d["ic"], 770, 222, 0.42, a0 * (1 - sol))
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        y = 280
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para_nb(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 600, 40)
            y += h + 18
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 500, 760)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 32, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            ad = ep(t, C[f"{s2}.d"], 0.4) * sol
            yy = 300
            if d["etqs"]:
                xx = 180
                for e in d["etqs"]:
                    w = ftw(e, 24) + 70
                    if xx + w > 800:
                        xx = 180; yy += 62
                    etiqueta(c, e, xx, yy, ad, 24)
                    xx += w + 16
                yy += 70
            else:
                fit(c, "compare os números das duas retas", 180, yy + 10, 30, 600, "black", PURPLE, ad)
                yy += 70
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"] + 0.6 * sum(1 for p in d["passos"][:j] if p[0] == cue), 0.4) * sol
                last = j == len(d["passos"]) - 1
                fit(c, s, 180, yy + 14, 38, 620, "black", GREEN if last else INK, a)
                yy += 62
            if d["confere"]:
                cue, s = d["confere"]
                conferido(c, nb(s), 190, yy + 30, ep(t, C[f"{s2}.{cue}"], 0.4) * sol, True, 28)
            result_box(c, f"Letra {d['ok']}", 1290, 720, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("31.b", "EP. 1", 0, ["testar a solução nas duas equações", "montar: quantidade e valor",
                               "traduzir “o dobro”, “se der k” sem inverter", "substituir com parênteses",
                               "tudo de um tipo · encontro de móveis"]),
         ("31.c", "EP. 2", 1, ["adição: multiplicar a equação inteira", "pediram x + y? some as equações"]),
         ("32.a", "EP. 3", 2, ["concorrentes, paralelas, coincidentes", "classificar pelas razões",
                               "ler 0 = 2 e 0 = 0"]),
         ("32.b", "EP. 4", 3, ["3 × 3 escalonado: a escada", "duplas: some tudo e divida por 2"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["31.a"], 0.5) * (1 - ep(t, C["31.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(150, 200), (150, 520), (990, 200), (990, 400)]
    for k, (cue, ep_, ic, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x, y0 = pos[k]
        pill(c, ep_, x, y0 + 18, PURPLE, size=20, a=a, bounds=(0, 1920))
        icone(c, ic, x + 40, y0 + 100, 0.22, a)
        for j, it in enumerate(itens):
            yy = y0 + 18 + j * 44
            rrect(c, x + 110, yy - 15, 30, 30, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            fit(c, it, x + 158, yy + 10, 26, 600, "bold", INK, a)
    ae = ep(t, C["32.d"], 0.5)
    if ae > 0:
        boxed(c, 990, 640, 760, 100, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1370, 690, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["33.a"], 0.5)
    ab = ep(t, C["33.b"], 0.5)
    ac = ep(t, C["33.c"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["33.a"] + 0.03 * i, 0.2)
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
        icone(c, 0, 360, 670, 0.38, ac)
        text_mid(c, "15 DE MONTAGEM A PARTIR DE TEXTO", 1030, 640, 44, "black", BLUE, ac)
        text_mid(c, "ingressos · misturas · combos", 1030, 710, 32, "bold", INK2, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["34.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Conceito de função", W / 2, 330, 62, "black", PURPLE, aa)
    text(c, "domínio · contradomínio · imagem", W / 2, 400, 36, "bold", INK2, aa)
    ab = ep(t, C["34.b"], 0.5)
    if ab > 0:
        rrect(c, W / 2 - 460, 470, 920, 200, 24, mix("#FFFFFF", PURPLE, 0.10), ab, shadow=True)
        mx(c, "x + y = 5", W / 2 - 250, 570, 60, INK2, ab, align="center")
        arrow(c, W / 2 - 60, 570, W / 2 + 40, 570, GREEN, ab, 6, 16)
        mx(c, "y = 5 − x", W / 2 + 230, 570, 60, GREEN, ab, align="center")
    ac = ep(t, C["34.c"], 0.5)
    text(c, "uma coisa que determina a outra", W / 2, 760, 40, "black", PURPLE, ac)


def b_cta(c, t, C, B):
    cta(c, t, C["35.like"], C["35.sub"], C["35.bell"], C["35.com"], C["35.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["35.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, rende=b_rende, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
