"""Visual — Equações e Inequações do 1º Grau, Episódio 2: do texto à equação (idades, partes de um total e misturas).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: etiqueta() (a etiqueta do x, com unidade), boneco() e linha_tempo() (pai e filho ganhando "+4" ao
mesmo tempo), tanque() (álcool colorido embaixo, nível total subindo), barra_partes() (Bia = 1 parte, Ana = 3), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
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
fr = K.fr
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_equacoes_ep2_texto_equacao.mp4"
CARD_R = K.CARD_R
ALCOOL = "#F2B33D"
AGUA = "#BFDDF7"
PAI_C = "#3D6FD8"
FILHO_C = "#E07A2E"


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)]"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def etiqueta(c, s, x, y, a, size=30, col=BLUE):
    """a ETIQUETA do x: formato de etiqueta de preço (ponta à esquerda, furinho), com o texto 'x = ..., em ...'"""
    if a <= 0:
        return 0
    w = ftext_w(s, "black", size) + 90
    h = size * 1.9
    p = skia.Path()
    p.moveTo(x, y + h / 2); p.lineTo(x + 34, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h); p.lineTo(x + 34, y + h)
    p.close()
    c.drawPath(p, paint(mix("#FFFFFF", col, 0.12), a))
    c.drawPath(p, paint(col, a, stroke=4))
    c.drawCircle(x + 28, y + h / 2, 7, paint(col, a, stroke=3))
    fmid(c, s, x + 52 + (w - 52) / 2 - 6, y + h / 2, size, "black", col, a)
    return w


def boneco(c, cx, base, h, col, a, nome="", idade="", extra=0.0):
    """bonequinho simples (cabeça + corpo); idade embaixo; extra = alfa do selo '+4' na cabeça"""
    if a <= 0:
        return
    r = h * 0.17
    c.drawCircle(cx, base - h + r, r, paint(col, a))
    rrect(c, cx - h * 0.2, base - h + 2 * r + 6, h * 0.4, h - 2 * r - 6, h * 0.12, col, a)
    if nome:
        text(c, nome, cx, base + 38, 28, "black", col, a)
    if idade:
        text(c, idade, cx, base + 78, 30, "black", INK, a)
    if extra > 0:
        chip(c, "+4", cx + r * 2.2, base - h + r * 0.4, GREEN, a * extra, 30)


def tanque(c, x, y, w, h, vol, alc, cap, a, rot_vol="", rot_alc=""):
    """tanque visto de lado: vol = volume total (L), alc = litros de álcool, cap = capacidade desenhada (L).
    álcool (âmbar) embaixo, resto (azul-claro) em cima; o nível total acompanha o volume"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 18, "#FFFFFF", a, shadow=True)
    hv = h * min(1, vol / cap)
    ha = h * min(1, alc / cap)
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18))
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - hv, w, hv), paint(AGUA, a))
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - ha, w, ha), paint(ALCOOL, a))
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), paint(INK2, a, stroke=5))
    if rot_vol:
        line(c, x + w + 10, y + h - hv, x + w + 40, y + h - hv, INK2, a, 3)
        text(c, rot_vol, x + w + 50, y + h - hv + 12, 30, "black", INK, a, align="left")
    if rot_alc:
        text_mid(c, rot_alc, x + w / 2, y + h - ha / 2, 28, "black", INK, a if ha > 40 else 0)


def barra_partes(c, x, y, pw, h, n, col, a, rot="", sub=""):
    """n partes iguais lado a lado"""
    if a <= 0:
        return
    for k in range(n):
        rrect(c, x + k * (pw + 8), y, pw, h, 12, mix("#FFFFFF", col, 0.3), a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + k * (pw + 8), y, pw, h), 12, 12), paint(col, a, stroke=3))
        if sub:
            text_mid(c, sub, x + k * (pw + 8) + pw / 2, y + h / 2, 30, "black", col, a)
    if rot:
        text(c, rot, x - 20, y + h / 2 + 12, 34, "black", col, a, align="right")


def passo(c, n, s, x, y, a, col=PURPLE, size=36, w=640):
    if a <= 0:
        return
    badge_num(c, n, x + 24, y, a, 26, bg=col)
    para(c, s, x + 70, y + 12, size, "black", INK, a, w)


def pergunta(c, s, cx, cy, a, col=PURPLE, size=40):
    if a <= 0:
        return
    w = ftext_w(s, "black", size) + 80
    rrect(c, cx - w / 2, cy - 40, w, 80, 40, mix("#FFFFFF", col, 0.10), a)
    fmid(c, s, cx, cy, size, "black", col, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "DO TEXTO À EQUAÇÃO", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["01.a"], 0.5)
    ab = ep(t, C["01.b"], 0.5)
    ex = ep(t, C["01.b"] + 1.2, 0.5)
    boneco(c, 420, 620, 300, PAI_C, aa, "pai", "", ex)
    boneco(c, 640, 620, 190, FILHO_C, aa, "filho", "", ex)
    if aa > 0:
        pill(c, "pai + filho = 52 anos", 530, 250, INK, size=30, a=aa, anchor="center")
    if ab > 0:
        pill(c, "daqui a 4 anos: pai = 3 × filho", 530, 790, PURPLE, size=28, a=ab, anchor="center")
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        for k, (L, s) in enumerate((("A", "11"), ("B", "13"), ("C", "14"), ("D", "15"), ("E", "41"))):
            ak, d = rise(t, C["01.c"] + 0.25 * k)
            yy = 260 + k * 104 + d
            rrect(c, 960, yy, 560, 84, 16, "#F7F7F5", ak)
            badge_num(c, L, 1000, yy + 42, ak, 22, bg=GREEN if L == "A" else INK)
            text(c, s + " anos", 1050, yy + 54, 36, "black", INK, ak, align="left")
            if L != "A":
                pill(c, "certa para OUTRA pergunta", 1500, yy + 42, AMBER, size=20, a=ep(t, C["01.d"] + 0.3 * k, 0.4),
                     anchor="right", bounds=(0, 1920))


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "transformar texto em equação", "com um roteiro de 4 passos"),
            ("02.b", "não cair na resposta da pergunta errada", "achou o x? releia a pergunta")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        text(c, s, 360, y, 48, "black", INK, a, align="left")
        text(c, sub, 360, y + 60, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "RÁPIDOS", GREEN)
    cols = [("03.a", "EXPRESSÕES", ["o dobro da soma", "2 · (x + y)", "a soma do dobro", "2x + y"], BLUE),
            ("03.b", "FRAÇÕES", None, PURPLE),
            ("03.c", "EPISÓDIO 1", ["resolver: o roteiro", "hoje: MONTAR", "a equação"], GREEN)]
    for k, (cue, tit, lines, col) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 220 + k * 510
        rrect(c, x, 240, 460, 500, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x, 240, 460, 60, 24, col, a * 0.14)
        text(c, tit, x + 230, 282, 28, "black", col, a)
        if lines is None:
            fr(c, "1", "3", x + 70, 470, 64, INK, a)
            text_mid(c, "+", x + 140, 480, 52, "black", INK, a)
            fr(c, "1", "4", x + 210, 470, 64, INK, a)
            text_mid(c, "=", x + 280, 480, 52, "black", INK, a)
            fr(c, "7", "12", x + 370, 470, 64, GREEN, a)
            text(c, "MMC 12: 4/12 + 3/12", x + 230, 640, 28, "bold", GRAY, a)
        else:
            for j, s in enumerate(lines):
                big = j % 2 == 1 and k == 0
                text(c, s, x + 230, 380 + j * 80, 40 if big else 30, "black", INK if big else (col if j % 2 else INK2), a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA CONVERSA", "QUANTO TEM CADA UMA?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 220, 1400, 120, 24, "#F7F7F5", aa)
        linha(c, [("Ana tem o ", INK), ("TRIPLO", PURPLE), (" da Bia  ·  juntas: ", INK), ("R$ 96,00", GREEN)],
              W / 2, 280, 44, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        text(c, "?", W / 2, 470, 120, "black", AMBER, ab * (1 - ep(t, C["04.c"], 0.3)))
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        for k, (bia, ana, soma, ok) in enumerate(((10, 30, 40, False), (30, 90, 120, False))):
            ak = ep(t, C["04.c"] + 1.6 * k, 0.4)
            y = 420 + k * 120
            linha(c, [(f"Bia R$ {bia}  +  Ana R$ {ana}  =  ", INK), (f"R$ {soma}", RED)], W / 2, y, 44, ak)
            text(c, "pouco" if soma < 96 else "passou", 1500, y + 14, 30, "black", RED, ak)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "chutar cansa: a EQUAÇÃO resolve de uma vez", W / 2, 720, ad, 36, GREEN)


# ======================================================================
# bloco a — o roteiro de 4 passos
# ======================================================================

def b_roteiro(c, t, C, B):
    head_seq(c, t, C, [("05", "O ROTEIRO", "4 PASSOS", PURPLE), ("06", "O PASSO 3", "A FRASE DE IGUALDADE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["05", "06"])
    if sid == "05":
        aa = ep(t, C["05.a"], 0.5)
        passo(c, 1, "a INCÓGNITA (o valor escondido), com unidade", 220, 270, aa, BLUE, 34, 760)
        etiqueta(c, "x = dinheiro da Bia, em R$", 1080, 225, ep(t, C["05.a"] + 2.6, 0.4), 32)
        ab = ep(t, C["05.b"], 0.5)
        passo(c, 2, "o resto EM FUNÇÃO dela", 220, 410, ab, PURPLE, 34, 760)
        if ab > 0:
            linha(c, [("Ana = ", INK), ("3x", PURPLE)], 1300, 410, 48, ab)
        passo(c, 3, "a FRASE DE IGUALDADE", 220, 550, ep(t, C["05.c"], 0.5), PURPLE, 34, 760)
        passo(c, 4, "resolver e responder O QUE FOI PEDIDO", 220, 690, ep(t, C["05.d"], 0.5), PURPLE, 34, 760)
        return
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        text(c, "o pedaço do texto que vira o  =", W / 2, 280, 44, "black", BLUE, aa)
    for k, s in enumerate(("“é igual a”", "“custam o mesmo”", "“totaliza”", "“sobrou”")):
        chip(c, s, 360 + k * 400, 420, BLUE, ep(t, C["06.b"] + 0.6 * k, 0.4), 34)
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        linha(c, [("“as duas juntas ", INK2), ("têm", BLUE), (" 96”", INK2)], W / 2, 560, 40, acc)
        arrow(c, W / 2, 600, W / 2, 650, AMBER, acc, 5, 16)
        linha(c, [("x + 3x ", INK), ("=", BLUE), (" 96", INK)], W / 2, 710, 64, ep(t, C["06.c"] + 1.4, 0.4))


# ======================================================================
# blocos b, c — consecutivos e partes
# ======================================================================

def b_consecutivos(c, t, C, B):
    head(c, t, B["start"], "NÚMEROS CONSECUTIVOS", "SOMAM 84", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        text(c, "CONSECUTIVOS = seguidos, um depois do outro", W / 2, 250, 34, "black", BLUE, aa)
        for k, s in enumerate(("7", "8", "9")):
            chip(c, s, 820 + k * 140, 330, BLUE, aa, 40)
    ab = ep(t, C["07.b"], 0.5)
    etiqueta(c, "x = o menor número", 220, 400, ab, 28)
    if ab > 0:
        for k, s in enumerate(("x", "x + 1", "x + 2")):
            chip(c, s, 820 + k * 240, 430, PURPLE, ep(t, C["07.b"] + 0.5 * k, 0.4), 40, w=210)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        linha(c, [("3x + 3 = 84  →  3x = 81  →  ", INK), ("x = 27", GREEN)], W / 2, 545, 46, acc)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        linha(c, [("resposta: ", INK2), ("27, 28 e 29", GREEN)], 560, 650, 44, ad)
        pill(c, "a resposta NÃO é só o x", 560, 720, AMBER, size=24, a=ad, anchor="center")
    ae = ep(t, C["07.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1000, 600, 640, 200, "ATALHO", ["o do MEIO = soma ÷ 3", "84 ÷ 3 = 28"], ae, 34)


def b_partes(c, t, C, B):
    head(c, t, B["start"], "PARTES DE UM TOTAL", "ANA = 3 × BIA · JUNTAS 96", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["08"], 0.5)
    etiqueta(c, "x = dinheiro da Bia, em R$", 220, 200, a0, 28)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha(c, [("x + 3x = 96  →  4x = 96  →  ", INK), ("x = 24", GREEN)], W / 2, 340, 48, aa)
    ab = ep(t, C["08.b"], 0.5)
    barra_partes(c, 520, 420, 200, 80, 1, FILHO_C, ab, "Bia", "R$ 24")
    barra_partes(c, 520, 530, 200, 80, 3, PAI_C, ab, "Ana", "R$ 24")
    if ab > 0:
        text(c, "= R$ 72", 1220, 584, 40, "black", PAI_C, ab, align="left")
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        linha(c, [("se x fosse a Ana:  ", INK2), ("Bia = x/3", RED), ("  → fração", INK2)], W / 2 - 300, 690, 32, acc)
        pill(c, "x = a MENOR parte", W / 2 - 300, 760, BLUE, size=26, a=ep(t, C["08.c"] + 2.0, 0.4), anchor="center")
    ad = ep(t, C["08.d"], 0.5)
    if ad > 0:
        K.atalho(c, 1120, 640, 540, 180, "ATALHO", ["96 ÷ 4 partes = 24"], ad, 34)


# ======================================================================
# bloco d — idades
# ======================================================================

def b_idades(c, t, C, B):
    head_seq(c, t, C, [("09", "IDADES", "O TEMPO PASSA PARA TODOS", PURPLE), ("10", "ATALHO DE OURO", "A DIFERENÇA NÃO MUDA", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["09", "10"])
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        # linha do tempo
        if aa > 0:
            line(c, 260, 720, 1660, 720, INK2, aa, 4)
            for xx, s in ((560, "HOJE"), (1300, "DAQUI A 4 ANOS")):
                line(c, xx, 705, xx, 735, INK2, aa, 4)
                text(c, s, xx, 780, 28, "black", INK2, aa)
        boneco(c, 480, 640, 260, PAI_C, aa, "", "")
        boneco(c, 640, 640, 170, FILHO_C, aa, "", "")
        if aa > 0:
            pill(c, "pai: p", 480, 300, PAI_C, size=28, a=aa, anchor="center")
            pill(c, "filho: f", 650, 380, FILHO_C, size=28, a=aa, anchor="center")
        ab = ep(t, C["09.b"], 0.5)
        ex = ep(t, C["09.b"] + 0.4, 0.5)
        boneco(c, 1220, 640, 270, PAI_C, ab, "", "", ex if t >= C["09.b"] + 1.6 else 0)
        boneco(c, 1390, 640, 180, FILHO_C, ab, "", "", ex)
        if ab > 0:
            pill(c, "f + 4", 1440, 250, FILHO_C, size=28, a=ab, anchor="center")
            pill(c, "p + 4", 1200, 250, PAI_C, size=28, a=ep(t, C["09.b"] + 1.6, 0.4), anchor="center")
        acc = ep(t, C["09.c"], 0.5)
        if acc > 0:
            selo(c, 930, 520, acc, "+4 PARA OS DOIS", GREEN, -4, 34)
        ad = ep(t, C["09.d"], 0.5)
        if ad > 0:
            pill(c, "há 3 anos:  f − 3  e  p − 3", 930, 620, PURPLE, size=26, a=ad, anchor="center")
        return
    aa = ep(t, C["10.a"], 0.5)
    for k, (lab, p_, f_) in enumerate((("hoje", 41, 11), ("daqui a 4", 45, 15), ("daqui a 100", 141, 111))):
        ak = ep(t, C["10.a"] + 0.9 * k, 0.4) * aa
        if ak <= 0:
            continue
        x = 330 + k * 470
        rrect(c, x - 190, 250, 380, 300, 22, "#FFFFFF", ak, shadow=True)
        text(c, lab, x, 300, 30, "black", GRAY, ak)
        linha(c, [(f"pai {p_}", PAI_C), ("  ·  ", INK2), (f"filho {f_}", FILHO_C)], x, 380, 34, ak)
        linha(c, [("diferença: ", INK2), ("30", GREEN)], x, 470, 40, ak)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        K.atalho(c, 360, 610, 1200, 170, "ATALHO DE OURO", ["a DIFERENÇA de idade nunca muda"], ab, 44)


# ======================================================================
# bloco e — frações de um total
# ======================================================================

def b_fracoes(c, t, C, B):
    head(c, t, B["start"], "FRAÇÕES DE UM TOTAL", "“DO SALÁRIO” × “DO RESTANTE”", AMBER)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    x0, w0, y0 = 260, 1400, 250
    if aa > 0:
        text(c, "salário: R$ 1.200", x0, y0 - 14, 32, "black", INK, aa, align="left")
        rrect(c, x0, y0, w0, 90, 12, "#F7F7F5", aa)
        rrect(c, x0, y0, w0 / 2, 90, 12, mix("#FFFFFF", GRAY, 0.35), aa)
        text_mid(c, "aluguel: R$ 600", x0 + w0 / 4, y0 + 45, 30, "black", INK2, aa)
        text_mid(c, "sobram R$ 600", x0 + 3 * w0 / 4, y0 + 45, 30, "black", INK, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        y = 430
        text(c, "1/4 DO SALÁRIO", x0, y - 14, 30, "black", BLUE, ab, align="left")
        rrect(c, x0, y, w0, 70, 12, "#F7F7F5", ab)
        rrect(c, x0, y, w0 / 4, 70, 12, mix("#FFFFFF", BLUE, 0.4), ab)
        text_mid(c, "R$ 300", x0 + w0 / 8, y + 35, 32, "black", BLUE, ab)
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        y = 580
        text(c, "1/4 DO RESTANTE", x0 + w0 / 2, y - 14, 30, "black", AMBER, acc, align="left")
        rrect(c, x0 + w0 / 2, y, w0 / 2, 70, 12, "#F7F7F5", acc)
        rrect(c, x0 + w0 / 2, y, w0 / 8, 70, 12, mix("#FFFFFF", AMBER, 0.5), acc)
        text_mid(c, "R$ 150", x0 + w0 / 2 + w0 / 16, y + 35, 28, "black", INK, acc)
    ad = ep(t, C["11.d"], 0.5)
    if ad > 0:
        regra(c, "SUBLINHE de quem é a fração", W / 2, 750, ad, 36, AMBER)


# ======================================================================
# bloco f — misturas
# ======================================================================

def b_mistura(c, t, C, B):
    head_seq(c, t, C, [("12", "MISTURAS", "CONCENTRAÇÃO", BLUE), ("13", "CHEGAR A 20%", "E O ATALHO DA ÁGUA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["12", "13"])
    if sid == "12":
        aa = ep(t, C["12.a"], 0.5)
        if aa > 0:
            chip(c, "SOLUTO = o álcool", 560, 260, ALCOOL, aa, 32)
            chip(c, "VOLUME TOTAL = o tanque inteiro", 1260, 260, BLUE, ep(t, C["12.a"] + 2.0, 0.4), 32)
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            text_mid(c, "concentração =", 1250, 440, 44, "black", PURPLE, ab, align="right")
            fr(c, "soluto", "volume total", 1460, 430, 48, INK, ab, num_col=ALCOOL, den_col=BLUE)
        acc = ep(t, C["12.c"], 0.5)
        u = ep(t, C["12.d"] + 0.3, 2.0)
        vol, alc = 20 + 2.5 * u, 2 + 2.5 * u
        tanque(c, 300, 340, 300, 420, vol, alc, 30, acc, f"{vol:.1f} L".replace(".", ",").replace(",0 ", " "),
               f"{alc:.1f} L álcool".replace(".", ",").replace(",0 ", " "))
        if acc > 0:
            text(c, "20 L com 10% de álcool", 450, 815, 28, "black", INK, acc)
        ad = ep(t, C["12.d"], 0.5)
        if ad > 0:
            linha(c, [("sobe EM CIMA ", ALCOOL), ("e ", INK), ("sobe EMBAIXO", BLUE)], 1180, 610, 44, ad)
            pill(c, "o álcool que entra também aumenta o tanque", 1180, 700, AMBER, size=26, a=ad, anchor="center")
        return
    a0 = ep(t, C["13"], 0.5)
    etiqueta(c, "x = litros de álcool puro que entram", 220, 200, a0, 26)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        fr(c, "2 + x", "20 + x", 520, 380, 56, INK, aa, num_col=ALCOOL, den_col=BLUE)
        text_mid(c, "= 0,2", 760, 395, 56, "black", INK, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        text(c, "2 + x = 4 + 0,2x", 560, 540, 40, "black", INK2, ab)
        linha(c, [("0,8x = 2  →  ", INK2), ("x = 2,5 L", GREEN)], 560, 620, 44, ep(t, C["13.b"] + 2.0, 0.4))
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        K.atalho(c, 1010, 300, 680, 360, "ATALHO · CONTE A ÁGUA", ["água: 18 L (não muda)", "no fim, 18 L = 80%",
                                                                    "18 ÷ 0,8 = 22,5 L", "22,5 − 20 = 2,5 L"], acc, 32)
        conferido(c, "os dois caminhos batem", 1110, 730, ep(t, C["13.c"] + 4.0, 0.4), True, 30)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "MÃE E FILHA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 200, 1480, 130, 24, "#F7F7F5", aa)
        linha(c, [("mãe ", INK), ("30", PAI_C), (" · filha ", INK), ("6", FILHO_C), (" · daqui a quantos anos mãe = 3 × filha?", INK)],
              W / 2, 265, 40, aa)
    pause_timer(c, t, C["14.end"] - 1.9, W / 2, 560)
    if t < C["15"]:
        return
    a1 = ep(t, C["15.a"], 0.4)
    etiqueta(c, "k = anos que vão passar", 220, 360, a1, 28)
    if a1 > 0:
        linha(c, [("mãe: 30 + k", PAI_C), ("   ·   ", INK2), ("filha: 6 + k", FILHO_C)], 1240, 400, 36, a1)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        linha(c, [("30 + k ", INK), ("=", BLUE), (" 3 · (6 + k)", INK)], 560, 510, 46, ab)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        linha(c, [("30 + k = 18 + 3k  →  12 = 2k  →  ", INK2), ("k = 6", GREEN)], 560, 600, 34, acc)
    ad = ep(t, C["15.d"], 0.5)
    if ad > 0:
        conferido(c, "36 = 3 × 12", 300, 700, ad, True, 34)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        K.atalho(c, 1060, 470, 640, 300, "ATALHO DA DIFERENÇA", ["diferença: 30 − 6 = 24", "no triplo: 24 = 2 filhas",
                                                                  "filha 12 → k = 6"], ae, 32)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Primeiro a etiqueta do x, com unidade.", "O tempo passa para todos.", "Achou o x? Releia a pergunta."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "30"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 54, "black", INK, a, 1360, 64)


ERROS = [("Somar os 4 anos a uma pessoa só", "o texto fala dos anos junto com o nome de UMA pessoa",
          "o tempo passa para TODOS: f + 4 e p + 4"),
         ("Mistura: esquecer que o volume total cresce", "a gente só pensa no álcool que entrou",
          "o álcool entra NO TANQUE: mexe em cima e embaixo da fração"),
         ("Responder o x quando pedem outra coisa", "o x deu um número bonito, e ele está nas alternativas",
          "a raiz não é a resposta: volte e leia a pergunta"),
         ("Somar frações sem MMC: 1/3 + 1/4 = 2/7", "é só somar em cima e somar embaixo",
          "terço e quarto são pedaços diferentes: MMC 12 → 7/12")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19", "20"], ERROS)


# ======================================================================
# questões do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=28, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


def _fonte(c, t, C, a0, prox):
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C[prox], 0.3)),
         align="left")


ALTS5 = [("A", "11 anos.", "", GREEN), ("B", "13 anos.", "triplo HOJE: ignorou os 4", RED),
         ("C", "14 anos.", "+4 só no pai", RED), ("D", "15 anos.", "filho daqui a 4 anos", AMBER),
         ("E", "41 anos.", "é o pai, hoje", AMBER)]


def b_q5(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 5 · EU FAÇO", "PROBLEMA DE IDADES", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [("Hoje, a soma das idades de um pai e de seu filho é 52 anos. Daqui a 4 anos, a idade do pai "
                           "será o triplo da idade do filho. A idade atual do filho é", INK)], a0, 240)
    _fonte(c, t, C, a0, "22")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "BCDE"}
    K.alternativas(c, t, C, ALTS5, 1000, 250, 680, 44, C["22.ok"], "A", cues_in, cues_x, gap=34)
    if t >= C["22"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["22"], 0.4))
        etiqueta(c, "f = idade do filho HOJE, em anos", 190, y0 + 16, ep(t, C["22"], 0.4), 22)
        linha(c, [("pai hoje: ", INK2), ("52 − f", PAI_C)], 540, y0 + 110, 30, ep(t, C["22.a"], 0.4))
        linha(c, [("(52 − f) + 4 = 3 · (f + 4)", INK)], 540, y0 + 165, 30, ep(t, C["22.b"], 0.4))
        linha(c, [("56 − f = 3f + 12  →  44 = 4f  →  ", INK2), ("f = 11", GREEN)], 540, y0 + 220, 24, ep(t, C["22.c"], 0.4))
        conferido(c, "pai 41 · daqui a 4: 45 = 3 × 15", 200, y0 + 275, ep(t, C["22.d"], 0.4), True, 24)
        pill(c, "pede o filho HOJE", 540, y0 + 330, AMBER, size=22, a=ep(t, C["22.e"], 0.4), anchor="center")
    af = ep(t, C["23.f"], 0.5)
    if af > 0:
        K.atalho(c, 1000, 700, 680, 130, "ATALHO", ["diferença 30 = 2 filhos → 15 no futuro → 11 hoje"], af, 26)


ALTS3 = [("A", "R$ 1.750,00", "1/3 + 1/4 = 2/7", RED), ("B", "R$ 1.979,17", "frações sobre os 1.250", RED),
         ("C", "R$ 2.142,86", "trocou sobra por gasto", RED), ("D", "R$ 2.500,00", "“do restante”", AMBER),
         ("E", "R$ 3.000,00", "", GREEN)]


def b_q3(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 3 · NÓS FAZEMOS", "FRAÇÕES DE UM TOTAL", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Uma pessoa gasta 1/3 do seu salário com aluguel e 1/4 do salário com alimentação. Depois "
                           "desses dois gastos, sobram R$ 1.250,00. O salário dessa pessoa é", INK)], a0, 240)
    _fonte(c, t, C, a0, "25")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS3, 1000, 250, 680, 44, C["25.ok"], "E", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 140)
    if t >= C["25"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        etiqueta(c, "x = salário, em R$", 190, y0 + 16, ep(t, C["25"], 0.4), 24)
        aa = ep(t, C["25.a"], 0.4)
        if aa > 0:
            pill(c, "as duas: DO SALÁRIO", 720, y0 + 52, BLUE, size=20, a=aa, anchor="center")
            fr(c, "1", "3", 300, y0 + 130, 40, INK, aa)
            text_mid(c, "+", 360, y0 + 140, 36, "black", INK, aa)
            fr(c, "1", "4", 420, y0 + 130, 40, INK, aa)
            text_mid(c, "=", 480, y0 + 140, 36, "black", INK, aa)
            fr(c, "7", "12", 550, y0 + 130, 40, INK, aa)
            text(c, "gastos", 700, y0 + 152, 26, "bold", GRAY, aa, align="left")
        ab = ep(t, C["25.b"], 0.4)
        if ab > 0:
            text(c, "sobram", 200, y0 + 247, 26, "bold", GRAY, ab, align="left")
            fr(c, "5", "12", 340, y0 + 225, 40, GREEN, ab)
            text(c, "x = 1 250", 400, y0 + 247, 32, "black", INK, ab, align="left")
        acc = ep(t, C["25.c"], 0.4)
        if acc > 0:
            linha(c, [("1 250 ÷ 5 × 12 = ", GREEN), ("3 000", GREEN)], 540, y0 + 315, 30, acc)
        conferido(c, "1 000 + 750 + 1 250 = 3 000", 200, y0 + 370, ep(t, C["25.d"], 0.4), True, 24)


ALTS9 = [("A", "6", "esqueceu que o tanque cresce", RED), ("B", "10", "", GREEN), ("C", "15", "6 ÷ 0,4", RED),
         ("D", "16", "40% dos 40 L antigos", RED), ("E", "50", "volume FINAL", AMBER)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "MISTURA E CONCENTRAÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["27.a"], 0.4)
    yend = _enunciado(c, [("Um tanque contém 40 litros de uma mistura com 25% de álcool, em volume. Deseja-se acrescentar "
                           "álcool puro para que a concentração passe a ser de 40%. A quantidade de álcool puro a "
                           "acrescentar, em litros, é", INK)], a0, 240)
    _fonte(c, t, C, a0, "28")
    cues_in = {L: C[f"27.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"29.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS9, 1000, 250, 680, 44, C["28.ok"], "B", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["27.end"] - 1.9, 540, yend + 120)
    if t >= C["28"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["28"], 0.4))
        etiqueta(c, "x = litros de álcool puro", 190, y0 + 16, ep(t, C["28"], 0.4), 24)
        linha(c, [("álcool: 25% de 40 L = ", INK2), ("10 L", ALCOOL)], 540, y0 + 110, 28, ep(t, C["28.a"], 0.4))
        ab = ep(t, C["28.b"], 0.4)
        if ab > 0:
            fr(c, "10 + x", "40 + x", 330, y0 + 170, 32, INK, ab, num_col=ALCOOL, den_col=BLUE)
            text(c, "= 0,4  →", 430, y0 + 182, 30, "black", INK, ab, align="left")
            linha(c, [("x = 10", GREEN)], 720, y0 + 172, 34, ep(t, C["28.b"] + 3.0, 0.4))
        linha(c, [("água 30 L = 60% → total 50 L → ", GREEN), ("+10", GREEN)], 540, y0 + 250, 24, ep(t, C["28.c"], 0.4))
        conferido(c, "20 L em 50 L = 40%", 200, y0 + 305, ep(t, C["28.d"], 0.4), True, 24)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "INEQUAÇÕES", PURPLE)
    aa = ep(t, C["31.a"], 0.5)
    if aa > 0:
        rrect(c, 260, 250, 520, 400, 30, "#4A4F57", aa, shadow=True)
        rrect(c, 310, 320, 420, 230, 16, "#2A2E33", aa)
        c.drawCircle(520, 435, 70, paint("#E8743B", aa * 0.5))
        text(c, "FORNO", 520, 610, 30, "black", "#FFFFFF", aa)
        linha(c, [("T = 220 − 8t", INK)], 1260, 330, 60, aa)
        linha(c, [("NO MÁXIMO", AMBER), (" 60 °C?", INK)], 1260, 440, 52, ep(t, C["31.a"] + 2.0, 0.4))
    ab = ep(t, C["31.b"], 0.5)
    if ab > 0:
        text(c, "“no máximo 20 minutos”", 1260, 560, 40, "black", RED, ab)
        strike(c, 1010, 548, 1510, 548, ab, RED, ab)
    pill(c, "ep. 3 · inequações: a regra do sinal", W / 2, 780, PURPLE, size=30, a=ep(t, C["31.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["32.like"], C["32.sub"], C["32.bell"], C["32.com"], C["32.bye"],
        "Você já tinha caído na pegadinha dos 4 anos?", canal="no Estudativo", anki=C["32.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, roteiro=b_roteiro,
              consecutivos=b_consecutivos, partes=b_partes, idades=b_idades, fracoes=b_fracoes, mistura=b_mistura,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q5=b_q5, q3=b_q3, q9=b_q9, ponte=b_ponte, cta=b_cta)
