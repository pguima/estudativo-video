"""Visual — Juros Compostos, Episódio 5: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, pause_timer, selo, chip...).
Índice visual da revisão: os 4 ícones dos episódios (icone()): bola de neve · reta e curva se cruzando · bloco 1,34 ao
quadrado · linha do tempo com seta para trás.
Ícones de contexto nas questões (area_icone()): cofrinho · cartão de crédito · relógio · linha do tempo com alvo · gráfico.
No gráfico (como no ep2): reta (simples) = AZUL e curva (compostos) = ROXO.
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
_s = importlib.util.spec_from_file_location("comum029", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_juros_compostos_ep5_revisao.mp4"
CARD_R = K.CARD_R
SIMP = BLUE
COMP = PURPLE
NEVE = "#EAF3FB"
MOEDA = "#F2B632"
MOEDA2 = "#C98E12"
CARTAO = "#3D5A80"


def ftw(s, size, peso="black"):
    return K.ftext_w(s, peso, size)


# ======================================================================
# peças
# ======================================================================

def moeda(c, cx, cy, r, a, s=""):
    if a <= 0:
        return
    c.drawCircle(cx, cy + 3, r, paint(MOEDA2, a))
    c.drawCircle(cx, cy, r, paint(MOEDA, a))
    c.drawCircle(cx, cy, r * 0.76, paint(MOEDA2, a, stroke=max(2, r * 0.08)))
    if s:
        text_mid(c, s, cx, cy, r * 0.8, "black", INK, a)


def bola_neve(c, a):
    """bola de neve rolando morro abaixo, com o rastro de bolinhas crescendo"""
    for k, (x, y, r) in enumerate(((-170, -40, 14), (-128, -14, 22), (-72, 18, 32))):
        c.drawCircle(x, y, r, paint(NEVE, a)); c.drawCircle(x, y, r, paint(SIMP, a, stroke=3))
    c.drawCircle(40, 30, 72, paint(NEVE, a)); c.drawCircle(40, 30, 72, paint(SIMP, a, stroke=4))
    for dx, dy in ((10, 0), (50, 40), (60, -10), (20, 60)):
        c.drawCircle(dx, dy, 6, paint(mix("#FFFFFF", SIMP, 0.35), a))
    line(c, -200, -60, 150, 110, LIGHT, a, 4)


def eixos_cruz(c, a, w=340, h=200):
    """eixos com reta (simples, azul) e curva (compostos, roxo) se cruzando em t = 1"""
    x0, y0 = -w / 2, h / 2
    line(c, x0, y0, x0 + w, y0, INK2, a, 3); line(c, x0, y0, x0, y0 - h, INK2, a, 3)
    sx, sy = w / 2.4, h / 2.2
    pr = skia.Path(); pr.moveTo(x0, y0 - 30)
    pr.lineTo(x0 + 2.3 * sx, y0 - 30 - (2.3 * 0.5) * sy)
    c.drawPath(pr, paint(SIMP, a, stroke=6))
    pc = skia.Path(); pc.moveTo(x0, y0 - 30)
    for k in range(1, 41):
        u = 2.3 * k / 40
        pc.lineTo(x0 + u * sx, y0 - 30 - (1.5 ** u - 1) * sy)
    c.drawPath(pc, paint(COMP, a, stroke=6))
    c.drawCircle(x0 + sx, y0 - 30 - 0.5 * sy, 10, paint(AMBER, a))
    line(c, x0 + sx, y0, x0 + sx, y0 - 30 - 0.5 * sy, AMBER, a * 0.6, 2)
    text_mid(c, "t = 1", x0 + sx, y0 + 26, 24, "black", AMBER, a)


def bloco_quadrado(c, a):
    """o bloco 1,34 elevado ao quadrado (dobrar o tempo)"""
    rrect(c, -120, -60, 200, 110, 18, mix("#FFFFFF", PURPLE, 0.16), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-120, -60, 200, 110), 18, 18), paint(PURPLE, a, stroke=4))
    fmid(c, "1,34", -20, -5, 60, "black", PURPLE, a)
    fmid(c, "2", 112, -58, 54, "black", GREEN, a)


def linha_tempo(c, a, seta=True):
    """linha do tempo hoje → futuro, com a seta voltando (÷ fator)"""
    line(c, -170, 40, 170, 40, INK2, a, 4)
    c.drawCircle(-150, 40, 14, paint(GREEN, a)); c.drawCircle(150, 40, 14, paint(BLUE, a))
    text_mid(c, "hoje", -150, 88, 26, "black", GREEN, a)
    text_mid(c, "futuro", 150, 88, 26, "black", BLUE, a)
    if seta:
        p = skia.Path(); p.moveTo(140, 10); p.quadTo(0, -90, -140, 10)
        c.drawPath(p, paint(PURPLE, a, stroke=5))
        q = skia.Path(); q.moveTo(-140, 10); q.lineTo(-146, -18); q.lineTo(-116, -6); q.close()
        c.drawPath(q, paint(PURPLE, a))
        fmid(c, "÷ fator", 0, -62, 30, "black", PURPLE, a)


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 4 ícones da série (índice da revisão), em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:
        bola_neve(c, a)
    elif k == 1:
        eixos_cruz(c, a)
    elif k == 2:
        bloco_quadrado(c, a)
    elif k == 3:
        linha_tempo(c, a)
    c.restore()


def area_icone(c, k, cx, cy, s, a):
    """ícones de contexto: cofrinho · cartão de crédito · relógio · alvo no futuro · gráfico reta × curva"""
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
    elif k == 1:    # cartão de crédito
        rrect(c, -110, -70, 220, 140, 16, CARTAO, a, shadow=True)
        rrect(c, -110, -40, 220, 26, 0, INK, a)
        rrect(c, -86, 0, 46, 34, 6, MOEDA, a)
        for j in range(4):
            rrect(c, -20 + j * 30, 12, 22, 10, 3, "#FFFFFF", a * 0.8)
    elif k == 2:    # relógio
        c.drawCircle(0, 0, 80, paint("#FFFFFF", a)); c.drawCircle(0, 0, 80, paint(INK2, a, stroke=6))
        for j in range(12):
            import math
            ang = j * math.pi / 6
            line(c, 64 * math.sin(ang), -64 * math.cos(ang), 72 * math.sin(ang), -72 * math.cos(ang), INK2, a, 4)
        line(c, 0, 0, 0, -52, INK, a, 7); line(c, 0, 0, 38, 14, AMBER, a, 6)
        c.drawCircle(0, 0, 8, paint(INK, a))
    elif k == 3:    # alvo no futuro + seta de volta
        linha_tempo(c, a, seta=False)
        for r_, col in ((40, RED), (27, "#FFFFFF"), (14, RED)):
            c.drawCircle(150, -20, r_, paint(col, a))
        p = skia.Path(); p.moveTo(110, -50); p.quadTo(0, -110, -140, 10)
        c.drawPath(p, paint(PURPLE, a, stroke=5))
    elif k == 4:    # gráfico reta × curva
        eixos_cruz(c, a, 260, 170)
    c.restore()


def conferido(c, s, x, y, a, ok=True, size=30):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def nb(s):
    """espaço rígido: não quebra 'R$ 6.000,00', '15 %' nem número + unidade"""
    s = s.replace("R$ ", "R$ ")
    s = re.sub(r"(?<=\d) (?=(%|meses|mês|anos|ano|reais)\b)", " ", s)
    return s


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    itens = (("POUPANÇA", 0, GREEN), ("CARTÃO", 1, RED), ("CHEQUE ESPECIAL", 2, AMBER), ("FINANCIAMENTO", 3, BLUE))
    for k, (s, ic, col) in enumerate(itens):
        a = ep(t, C["01.a"] + 0.7 * k, 0.4)
        area_icone(c, ic, 390 + k * 380, 330, 0.75, a)
        text(c, s, 390 + k * 380, 470, 30, "black", col, a)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, W / 2 - 330, 548, 70, 90, 10, INK2, ab)
        rrect(c, W / 2 - 320, 558, 50, 22, 4, mix("#FFFFFF", GREEN, 0.4), ab)
        for j in range(6):
            rrect(c, W / 2 - 320 + (j % 3) * 17, 590 + (j // 3) * 20, 13, 14, 3, "#FFFFFF", ab)
        line(c, W / 2 - 345, 640, W / 2 - 245, 545, RED, ab, 8)
        text(c, "SEM CALCULADORA", W / 2 - 220, 610, 46, "black", RED, ab, align="left")
    ac = ep(t, C["01.c"], 0.5)
    text(c, "o ENEM ENTREGA as potências e os logaritmos", W / 2, 690, 38, "black", PURPLE, ac)
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "9 FRASES V OU F", 760, 800, AMBER, ad, 34)
    chip(c, "5 QUESTÕES NOVAS", 1180, 800, GREEN, ep(t, C["01.d"] + 0.5, 0.4), 34)


COBRA = [("02.a", "MONTANTE", "com a potência dada", 0, BLUE),
         ("02.b", "O TEMPO", "tentativa ou logaritmo", 2, PURPLE),
         ("02.c", "TRAZER PARA HOJE", "valor presente", 3, GREEN),
         ("02.d", "SIMPLES × COMPOSTOS", "números ou gráfico", 4, AMBER),
         ("02.e", "TAXAS EM SEQUÊNCIA", "multiplique os fatores", 5, RED)]


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
            fmid(c, "1,1 · 1,2 · 0,75", x, 420 + d, 34, "black", RED, a)
        else:
            area_icone(c, ic, x, 420 + d, 0.8, a)
        para(c, tit, x, 590 + d, 28, "black", col, a, 300, 34, align="center")
        para(c, sub, x, 680 + d, 23, "bold", INK2, a, 290, 30, align="center")


INDICE = [("EP. 1", "bola de neve: juros sobre juros · fatores, não % somadas · o expoente conta as multiplicações"),
          ("EP. 2", "degraus iguais × degraus crescentes · cruzam em t = 1 · dobrar 3 vezes = × 8"),
          ("EP. 3", "× 1,1 = some a décima parte · dobrar o tempo = elevar ao quadrado · regra do 72 = radar"),
          ("EP. 4", "o filme ao contrário · para hoje, divida pelo mesmo fator")]
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
        yy = y + 360
        for ln in s.split(" · "):
            yy += para(c, ln, x, yy, 28, "black", INK if on_ else INK2, a, 370, 34, align="center") + 16


ONDE = [("05.a", "BIOLOGIA", "populações · bactérias"), ("05.b", "QUÍMICA", "meia-vida: × 1/2 por período"),
        ("05.c", "GEOGRAFIA", "projeções de população e PIB"), ("05.d", "ÁLGEBRA", "PG · exponencial · logaritmo"),
        ("05.e", "INFLAÇÃO", "série de Taxas equivalentes")]


def onde_icone(c, k, cx, cy, a):
    if a <= 0:
        return
    if k == 0:      # colônia de bactérias se multiplicando
        for j, (dx, dy) in enumerate(((-60, 20), (-20, -30), (20, 25), (60, -20), (0, 0), (-40, -60), (45, 55))):
            c.drawOval(skia.Rect.MakeXYWH(cx + dx - 24, cy + dy - 14, 48, 28), paint(mix("#FFFFFF", GREEN, 0.5), a))
            c.drawOval(skia.Rect.MakeXYWH(cx + dx - 24, cy + dy - 14, 48, 28), paint(GREEN, a, stroke=3))
    elif k == 1:    # barras caindo pela metade
        for j, h in enumerate((140, 70, 35, 17)):
            rrect(c, cx - 90 + j * 48, cy + 70 - h, 36, h, 4, mix("#FFFFFF", RED, 0.6), a)
        text_mid(c, "× 1/2", cx + 60, cy - 60, 30, "black", RED, a)
    elif k == 2:    # globo
        c.drawCircle(cx, cy, 70, paint(mix("#FFFFFF", BLUE, 0.3), a)); c.drawCircle(cx, cy, 70, paint(BLUE, a, stroke=4))
        c.drawOval(skia.Rect.MakeXYWH(cx - 30, cy - 70, 60, 140), paint(BLUE, a, stroke=3))
        line(c, cx - 70, cy, cx + 70, cy, BLUE, a, 3)
    elif k == 3:    # curva exponencial
        line(c, cx - 90, cy + 70, cx + 90, cy + 70, INK2, a, 3); line(c, cx - 90, cy + 70, cx - 90, cy - 80, INK2, a, 3)
        p = skia.Path(); p.moveTo(cx - 90, cy + 50)
        for j in range(1, 31):
            u = j / 30
            p.lineTo(cx - 90 + 170 * u, cy + 50 - 130 * (3 ** u - 1) / 2)
        c.drawPath(p, paint(COMP, a, stroke=6))
    else:           # etiqueta de preço subindo
        rrect(c, cx - 70, cy - 40, 140, 90, 12, "#FFFFFF", a, shadow=True)
        text_mid(c, "R$", cx, cy + 5, 44, "black", AMBER, a)
        arrow(c, cx + 60, cy + 60, cx + 100, cy - 70, RED, a, 6, 14)


def b_onde(c, t, C, B):
    frame(c, t, B["start"], "NÃO É SÓ MATEMÁTICA FINANCEIRA", "ONDE ISSO APARECE", BLUE)
    for k, (cue, tit, sub) in enumerate(ONDE):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 250 + k * 355
        rrect(c, x - 165, 240 + d, 330, 470, 24, mix("#F7F7F5", BLUE, 0.06), a)
        onde_icone(c, k, x, 390 + d, a)
        text(c, tit, x, 550 + d, 30, "black", BLUE, a)
        para(c, sub, x, 600 + d, 23, "bold", INK2, a, 290, 30, align="center")


HABITOS = [("06.a", "1", "PROCURE AS POTÊNCIAS", "elas mostram o caminho"),
           ("06.b", "2", "ELIMINE PELO SIMPLES", "depois de 1 período · composto > simples"),
           ("06.c", "3", "REGRA DO 72", "72 ÷ taxa · ≈ tempo para dobrar"),
           ("06.d", "4", "FATORES ATÉ O FIM", "reais só no final")]


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
    ("10% ao ano · 2 anos · compostos", "rende 20%", False, "10 + 10 = 20",
     "fatores se multiplicam · 1,1 × 1,1 = 1,21", "21%", 0),
    ("juros compostos", "M = C · (1 + i · t)", False, "é a fórmula da série anterior",
     "essa é a dos simples · a alternativa simples está sempre lá", "M = C · (1 + i)ᵗ", 1),
    ("aplicou R$ 1.000 · montante R$ 1.210", "juros = R$ 210", True, "a fórmula entrega o 1.210",
     "a fórmula dá o montante · J = M − C", "J = 210 · M = 1.210", 0),
    ("6 meses → × 1,34", "12 meses → × 2,68", False, "o tempo dobrou: dobrar o fator parece justo",
     "dobrar o tempo = elevar ao quadrado", "1,34² ≈ 1,80", 2),
    ("compostos", "12% a.a. = 1% a.m.", False, "nos juros simples era assim",
     "1% ao mês, 12 vezes, passa de 12% · a conversão usa potência (série própria)", "não divida por 12", 0),
    ("R$ 1.210 daqui a 2 anos · 10% a.a.", "valem R$ 1.000 hoje", True, "muita gente tiraria 10% duas vezes",
     "o filme ao contrário · divida pelo fator", "1.210 ÷ 1,21 = 1.000", 3),
    ("tabela do ano 0 ao ano 3", "expoente 4", False, "a tabela tem 4 linhas",
     "o expoente conta as multiplicações, não as linhas", "expoente 3", 0),
    ("tempo para dobrar a 10%", "log 2 ÷ log 1,1", True, "a tentação é dividir pela taxa (0,1)",
     "o denominador é o log do fator · radar: ≈ 7 anos", "≈ 7,3 anos", 2),
    ("mesma taxa", "compostos rendem SEMPRE mais", False, "na maioria das contas é assim",
     "as escadas se cruzam em 1 período · antes dele, o simples rende mais", "só depois de t = 1", 1),
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
        boxed(c, W / 2 - 330, 700, 660, 110, PURPLE, ab, 0.08)
        text_mid(c, "comece pelo fator: 1 + i", W / 2, 755, 40, "black", PURPLE, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · pad: a ideia · passos: (cue, texto) · confere: (cue, texto) ou None

Q = {
    "q1": dict(ids=("18", "19"), titulo="A APLICAÇÃO", area="POTÊNCIA FÁCIL · PEDE OS JUROS", ic=0, ok="D",
               enun=[("a", "Uma pessoa aplicou R$ 6.000,00 a juros compostos de 5% ao mês, por 2 meses.", False),
                     ("b", "Os JUROS recebidos foram de", True)],
               alts=[("A", "R$ 300,00", "um mês só", AMBER), ("B", "R$ 6.615,00", "é o montante", AMBER),
                     ("C", "R$ 600,00", "juros simples", RED), ("D", "R$ 615,00", "", GREEN),
                     ("E", "R$ 6.600,00", "montante simples", RED)],
               pad="fator de 1 mês: 1,05", passos=[("a", "2 meses: 1,05² = 1,1025"),
                                                   ("b", "M = R$ 6.615,00 · J = 6.615 − 6.000 = R$ 615,00")],
               confere=("v", "simples daria R$ 600: o composto passa disso")),
    "q2": dict(ids=("20", "21"), titulo="A DÍVIDA DO CARTÃO", area="POTÊNCIA DADA NO ENUNCIADO", ic=1, ok="A",
               enun=[("a", "Uma dívida de R$ 2.500,00 no cartão cresce 8% ao mês. Use 1,08⁶ ≈ 1,59.", False),
                     ("b", "Sem pagamentos, depois de 12 meses, a dívida será de", True)],
               alts=[("A", "R$ 6.320,25", "", GREEN), ("B", "R$ 3.975,00", "parou em 6 meses", AMBER),
                     ("C", "R$ 4.900,00", "juros simples", RED), ("D", "R$ 5.450,00", "somou os semestres", AMBER),
                     ("E", "R$ 7.950,00", "dobrou o fator", RED)],
               pad="12 meses = 2 × 6 meses: eleve ao quadrado", passos=[("a", "1,59² = 2,5281"),
                                                                       ("b", "2.500 × 2,5281 = R$ 6.320,25")],
               confere=None),
    "q3": dict(ids=("22", "23"), titulo="QUANDO TRIPLICA?", area="TEMPO COM LOGARITMOS", ic=2, ok="E",
               enun=[("a", "Um investimento rende 12% ao ano, a juros compostos. Use log 3 ≈ 0,48, log 2 ≈ 0,30 e "
                           "log 1,12 ≈ 0,05.", False),
                     ("b", "Em quanto tempo o capital triplica?", True)],
               alts=[("A", "4 anos", "dividiu pela taxa", RED), ("B", "6 anos", "log 2: é DOBRAR", AMBER),
                     ("C", "cerca de 16,7 anos", "simples (i·t = 2)", RED), ("D", "25 anos", "simples com J = 3C", RED),
                     ("E", "9,6 anos", "", GREEN)],
               pad="triplicar: log 3 ÷ log do fator", passos=[("a", "t = 0,48 ÷ 0,05 = 9,6 anos")],
               confere=("v", "radar: 72 ÷ 12 = 6 anos para dobrar")),
    "q4": dict(ids=("24", "25"), titulo="QUANTO APLICAR HOJE?", area="VALOR PRESENTE", ic=3, ok="C",
               enun=[("a", "Quanto aplicar hoje, a 10% ao ano, a juros compostos, para ter R$ 9.680,00 daqui a "
                           "2 anos?", True)],
               alts=[("A", "R$ 7.840,80", "tirou 10% duas vezes", AMBER), ("B", "≈ R$ 8.066,67", "fator simples (1,20)", RED),
                     ("C", "R$ 8.000,00", "", GREEN), ("D", "R$ 8.800,00", "voltou só 1 ano", AMBER),
                     ("E", "R$ 11.712,80", "multiplicou", RED)],
               pad="o filme ao contrário: ÷ fator", passos=[("a", "fator de 2 anos: 1,1² = 1,21"),
                                                            ("b", "9.680 ÷ 1,21 = R$ 8.000,00")],
               confere=("v", "volta: 8.000 × 1,21 = 9.680")),
    "q5": dict(ids=("26", "27"), titulo="QUAL PROPOSTA RENDE MAIS?", area="SIMPLES × COMPOSTOS", ic=4, ok="B",
               enun=[("a", "R$ 20.000,00 por 2 anos. Proposta I: juros simples de 16% ao ano. Proposta II: juros "
                           "compostos de 15% ao ano.", False),
                     ("b", "Rende mais, e quanto a mais:", True)],
               alts=[("A", "a I, R$ 400,00", "II como simples", RED), ("B", "a II, R$ 50,00", "", GREEN),
                     ("C", "a I, R$ 462,00", "I como composta", AMBER), ("D", "a II, R$ 4.017,50", "um ano a mais", AMBER),
                     ("E", "a II, R$ 19.600,00", "dobrou o fator", RED)],
               pad="taxas diferentes: faça a conta", passos=[("a", "I: 1 + 0,32 = 1,32 → R$ 26.400,00"),
                                                             ("b", "II: 1,15² = 1,3225 → R$ 26.450,00"),
                                                             ("c", "a II ganha por R$ 50,00")],
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

CHECK = [("28.b", "EP. 1", ["juros sobre juros: por que crescem", "M = C(1 + i)ᵗ e J = M − C", "taxas em sequência: fatores"]),
         ("28.c", "EP. 2", ["simples × compostos (antes e depois de t = 1)", "PG de razão 1 + i · exponencial",
                            "duplicações: × 2ⁿ"]),
         ("29.a", "EP. 3", ["potências de 1,1 · 1,05 · 1,02 à mão", "combinar potências dadas",
                            "dobrar o tempo = elevar ao quadrado", "tempo: tentativa · logaritmos · regra do 72"]),
         ("29.b", "EP. 4", ["valor presente: divida pelo fator"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["28.a"], 0.5) * (1 - ep(t, C["28.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    pos = [(170, 200), (170, 400), (990, 200), (990, 440)]
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
        area_icone(c, 2, 400, 660, 0.6, ac)
        area_icone(c, 4, 600, 660, 0.6, ac)
        text_mid(c, "inclua:", 1180, 620, 32, "bold", INK2, ac)
        text_mid(c, "logaritmos dados · comparação de regimes", 1180, 690, 38, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Descontos, acréscimos, lucro e prejuízo", W / 2, 330, 56, "black", PURPLE, aa)
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        rrect(c, W / 2 - 300, 420, 600, 120, 18, MOEDA, ab, shadow=True)
        rrect(c, W / 2 - 320, 520, 640, 30, 8, mix(MOEDA2, INK, 0.3), ab)
        text_mid(c, "o balcão · os mesmos fatores", W / 2, 478, 34, "black", INK, ab)
    ac = ep(t, C["31.c"], 0.5)
    ad = ep(t, C["31.d"], 0.5)
    text(c, "porcentagem DE QUÊ?", W / 2, 660, 50, "black", AMBER, ac)
    chip(c, "do CUSTO", 780, 770, BLUE, ad, 40)
    chip(c, "da VENDA", 1140, 770, GREEN, ep(t, C["31.d"] + 0.4, 0.4), 40)


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"], "Qual pegadinha te pegou?",
        canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, cobra=b_cobra, indice=b_indice, onde=b_onde, habitos=b_habitos,
              vf_intro=b_vf_intro, vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"),
              q3=faz_questao("q3"), q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta,
              ponte=b_ponte, cta=b_cta)
