"""Visual — Grandezas Proporcionais, Episódio 6: Revisão geral, pegadinhas e treino (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, pause_timer, selo...).
Índice visual da revisão: os 5 ícones dos episódios (icone()): etiqueta R$/kg · lupa de detetive · taxímetro ·
fração-guia · lanterna. Etiqueta, lupa e taxímetro copiados dos visual.py dos eps 1–3 para manter o traço.
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
"""
import importlib.util
import math
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum022", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, expr_w = K.expr, K.expr_w
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_grandezas_ep6_revisao.mp4"
CARD_R = K.CARD_R
DIR, INV = BLUE, PURPLE
LUZ = "#FFD84D"


# ======================================================================
# peças (mesmo traço dos episódios 1–3)
# ======================================================================

def etiqueta(c, x, y, a, linha1, linha2, rot=-4, w=300, h=140):
    """etiqueta de mercado (ep1), versão compacta; (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    c.save(); c.translate(x + w / 2, y + h / 2); c.rotate(rot); c.translate(-(x + w / 2), -(y + h / 2))
    p = skia.Path(); p.moveTo(x, y); p.lineTo(x + w - 60, y); p.lineTo(x + w, y + h / 2); p.lineTo(x + w - 60, y + h)
    p.lineTo(x, y + h); p.close()
    c.drawPath(p, paint(AMBER, a)); c.drawCircle(x + w - 58, y + h / 2, 11, paint("#FFFFFF", a))
    text(c, linha1, x + (w - 60) / 2, y + 44, 22, "black", "#FFFFFF", a)
    rrect(c, x + 18, y + 60, w - 96, 56, 14, GREEN, a * 0.9)
    text(c, linha2, x + (w - 60) / 2, y + 102, 36, "black", "#FFFFFF", a)
    c.restore()


def lupa(c, cx, cy, a, r=34, rot=-35):
    """lupa de detetive (ep2)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(rot)
    c.drawCircle(0, 0, r, paint("#FFFFFF", a * 0.35))
    c.drawCircle(0, 0, r, paint(INK, a, stroke=7))
    rrect(c, r - 2, -8, r * 1.35, 16, 8, AMBER, a)
    c.restore()


def taximetro(c, x, y, valor, a, w=250, h=96, size=44):
    """visor do taxímetro (ep3); (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    rrect(c, x, y, w, h, 16, "#1E2530", a, shadow=True)
    rrect(c, x + 10, y + 10, w - 20, h - 20, 10, "#0E1218", a)
    text_mid(c, valor, x + w / 2, y + h / 2, size, "black", "#3DE38A", a)


def guia(c, cx, cy, a, cima="direto", baixo="inverso", w=230, size=30):
    """a fração-guia (ep4): dois andares, o direto em cima e o inverso embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - 78, w, 62, 14, mix("#FFFFFF", DIR, 0.16), a)
    rrect(c, cx - w / 2, cy + 16, w, 62, 14, mix("#FFFFFF", INV, 0.16), a)
    line(c, cx - w / 2 - 12, cy, cx + w / 2 + 12, cy, INK, a, 7)
    text_mid(c, cima, cx, cy - 47, size, "black", DIR, a)
    text_mid(c, baixo, cx, cy + 47, size, "black", INV, a)


def lanterna(c, cx, cy, a, s=1.0, n=2):
    """lanterna (ep5) iluminando uma grade n × n: a mesma luz em n² quadradinhos"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    rrect(c, -150, -22, 70, 44, 10, INK2, a)
    p = skia.Path(); p.moveTo(-82, -30); p.lineTo(-60, -40); p.lineTo(-60, 40); p.lineTo(-82, 30); p.close()
    c.drawPath(p, paint(INK, a))
    q = skia.Path(); q.moveTo(-60, -34); q.lineTo(90, -80); q.lineTo(90, 80); q.lineTo(-60, 34); q.close()
    c.drawPath(q, paint(LUZ, a * 0.35))
    cel = 160 / n
    for i in range(n):
        for j in range(n):
            rrect(c, 92 + i * cel * 0.55, -80 + j * cel, cel * 0.55 - 4, cel - 4, 4, LUZ, a * (0.95 / n + 0.2))
    c.restore()


def mini_tab(c, x, y, linhas, a, col_y=INK, rh=36, wc=(80, 90), size=26):
    """tabelinha de duas colunas (sem cabeçalho); (x, y) = canto superior esquerdo"""
    if a <= 0:
        return
    for r_, (u, v) in enumerate(linhas):
        for k, (s, w) in enumerate(((u, wc[0]), (v, wc[1]))):
            xx = x + (0 if k == 0 else wc[0] + 6)
            rrect(c, xx, y + r_ * (rh + 6), w, rh, 8, "#FFFFFF", a, stroke=2, stroke_color=INK2)
            text_mid(c, s, xx + w / 2, y + r_ * (rh + 6) + rh / 2, size, "black", INK if k == 0 else col_y, a)


def mini_graf(c, cx, cy, tipo, a, w=200, h=150, col=None):
    """eixos + curva: 'origem' (reta pela origem), 'fixa' (reta acima do zero), 'hiper' (hipérbole)"""
    if a <= 0:
        return
    x0, y0 = cx - w / 2, cy + h / 2
    arrow(c, x0, y0, x0 + w + 20, y0, INK, a, 3, 10)
    arrow(c, x0, y0, x0, y0 - h - 20, INK, a, 3, 10)
    col = col or BLUE
    p = skia.Path()
    if tipo == "origem":
        p.moveTo(x0, y0); p.lineTo(x0 + w, y0 - h)
    elif tipo == "fixa":
        p.moveTo(x0, y0 - h * 0.35); p.lineTo(x0 + w, y0 - h)
    else:
        for i in range(61):
            u = 0.12 + i / 60 * 0.88
            xx, yy = x0 + u * w, y0 - (0.11 / u) * h
            p.moveTo(xx, yy) if i == 0 else p.lineTo(xx, yy)
    c.drawPath(p, paint(col, a, stroke=6, cap_round=True))
    if tipo == "fixa":
        c.drawCircle(x0, y0 - h * 0.35, 9, paint(AMBER, a))
        text_mid(c, "5", x0 - 22, y0 - h * 0.35, 22, "black", AMBER, a, align="right")


def icone(c, k, cx, cy, s=1.0, a=1.0):
    """os 5 ícones da série (índice da revisão), desenhados em escala s em volta de (cx, cy)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.scale(s, s)
    if k == 0:      # ep1 a etiqueta R$/kg
        etiqueta(c, -150, -80, a, "PREÇO POR kg", "R$ 5", w=300, h=140)
        fmid(c, "k", 120, -70, 40, "black", GREEN, a)
    elif k == 1:    # ep2 o detetive da tabela
        mini_tab(c, -110, -80, [("1", "5"), ("2", "10"), ("3", "15")], a, BLUE)
        lupa(c, 80, -10, a, 36)
        fmid(c, "÷  ×", 70, 74, 28, "black", PURPLE, a)
    elif k == 2:    # ep3 o taxímetro da bandeirada
        taximetro(c, -125, -70, "R$ 6,00", a)
        text(c, "no km zero", 0, 66, 24, "black", AMBER, a)
    elif k == 3:    # ep4 a fração-guia
        guia(c, 0, -8, a)
    elif k == 4:    # ep5 a lanterna
        lanterna(c, 10, -6, a, 0.9, 2)
        fmid(c, "1/4", 80, 82, 28, "black", AMBER, a)
    c.restore()


def mtext(c, s, cx, cy, size, a, col=None, align="center"):
    """'$...' = matemática (expr); senão texto (ftext, aceita ²)"""
    if a <= 0:
        return
    if s.startswith("$"):
        expr(c, s[1:], cx, cy, size, a, cores={i: col or INK for i in range(30)} if col else None, align=align)
    else:
        fmid(c, s, cx, cy, size, "black", col or INK, a, align=align)


def mtext_w(s, size):
    return expr_w(s[1:], size) if s.startswith("$") else K.ftext_w(s, "black", size)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "REVISÃO FINAL", BLUE)
    aa, ab = ep(t, C["01.a"], 0.5), ep(t, C["01.b"], 0.5)
    for k, (a, tit, sub, col) in enumerate(((aa, "REGRA DE TRÊS", "resolver", PURPLE),
                                           (ab, "GRANDEZAS PROPORCIONAIS", "reconhecer", BLUE))):
        if a <= 0:
            continue
        x = 600 + k * 720
        rrect(c, x - 320, 200, 640, 210, 24, mix("#FFFFFF", col, 0.10), a, shadow=True)
        text(c, tit, x, 270, 34, "black", col, a)
        text(c, sub, x, 350, 54, "black", INK, a)
    pill(c, "o ENEM pergunta das DUAS formas", W / 2, 455, AMBER, size=30, a=ep(t, C["01.b"] + 1.2, 0.5), anchor="center")
    for k in range(5):
        icone(c, k, 400 + k * 280, 600, 0.72, ep(t, C["01.c"] + 0.2 * k, 0.4))
    ad = ep(t, C["01.d"], 0.5)
    chip(c, "TREINO", 640, 780, PURPLE, ad, 36)
    chip(c, "9 FRASES", 960, 780, AMBER, ep(t, C["01.d"] + 0.5, 0.4), 36)
    chip(c, "5 QUESTÕES", 1280, 780, GREEN, ep(t, C["01.d"] + 1.0, 0.4), 36)


def b_formatos(c, t, C, B):
    frame(c, t, B["start"], "COMO O ENEM PERGUNTA", "TRÊS FORMATOS", BLUE)
    itens = [("02.a", "TABELA", "que relação? qual valor falta?"), ("02.b", "GRÁFICO", "que situação o desenho mostra?"),
             ("02.c", "FÓRMULA", "o que acontece quando outra dobra?")]
    for k, (cue, tit, sub) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 460 + k * 500
        rrect(c, x - 220, 220 + d, 440, 520, 24, "#F7F7F5", a)
        badge_num(c, k + 1, x, 272 + d, a, 26, bg=BLUE)
        if k == 0:
            mini_tab(c, x - 90, 340 + d, [("2", "6"), ("4", "12"), ("6", "18")], a, BLUE, rh=42, size=28)
        elif k == 1:
            mini_graf(c, x, 440 + d, "origem", a, 220, 160)
        else:
            expr(c, "R = k · L/A", x, 440 + d, 58, a, cores={0: INK, 1: INK, 2: PURPLE, 3: INK, 4: DIR})
        text(c, tit, x, 600 + d, 38, "black", BLUE, a)
        para(c, sub, x, 650 + d, 26, "bold", INK2, a, 380, 32, align="center")


INDICE = [("EP. 1", "o k não muda: quociente ou produto"), ("EP. 2", "divide e multiplica, em TODAS as linhas"),
          ("EP. 3", "a pergunta da origem"), ("EP. 4", "direto em cima, inverso embaixo"),
          ("EP. 5", "dobrou a distância: 1/4 da luz")]
IND_CUES = ["03.a", "03.b", "03.c", "04.a", "04.b"]
IND_POS = [(420, 195), (960, 195), (1500, 195), (690, 515), (1230, 515)]


def b_indice(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE COBRAR", "UMA FRASE POR EPISÓDIO", PURPLE)
    for k, (ep_, s) in enumerate(INDICE):
        a = ep(t, C[IND_CUES[k]], 0.5)
        if a <= 0:
            continue
        nxt = C[IND_CUES[k + 1]] if k + 1 < len(IND_CUES) else C["04.end"]
        on_ = 1.0 if C[IND_CUES[k]] - 0.05 <= t < nxt else 0.0
        x, y = IND_POS[k]
        rrect(c, x - 245, y, 490, 290, 22, mix("#F7F7F5", PURPLE, 0.10 * on_), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 245, y, 490, 290), 22, 22), paint(PURPLE, a, stroke=4))
        pill(c, ep_, x, y + 34, PURPLE if on_ else INK2, size=22, a=a, anchor="center", bounds=(0, 1920))
        icone(c, k, x, y + 145, 0.72, a)
        para(c, s, x, y + 258, 24, "black", INK if on_ else INK2, a, 450, 30, align="center")


def b_rendem(c, t, C, B):
    frame(c, t, B["start"], "SE TIVER TEMPO PARA DUAS", "AS QUE MAIS RENDEM", GREEN)
    aa, ab = ep(t, C["05.a"], 0.5), ep(t, C["05.b"], 0.5)
    for k, (a, tit, sub) in enumerate(((aa, "1 · O TESTE DA TABELA", "dividir e multiplicar"),
                                       (ab, "2 · A RETA FORA DA ORIGEM", "a armadilha mais cobrada"))):
        if a <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 340, 200, 680, 560, 24, "#F7F7F5", a)
        text(c, tit, x, 262, 34, "black", GREEN, a)
        text(c, sub, x, 312, 26, "bold", INK2, a)
        if k == 0:
            mini_tab(c, x - 180, 380, [("1", "5"), ("2", "10"), ("3", "15")], a, BLUE, rh=52, wc=(110, 110), size=32)
            for r_ in range(3):
                text_mid(c, "÷ = 5", x + 140, 406 + r_ * 58, 30, "black", GREEN, a)
            lupa(c, x + 230, 600, a, 34)
        else:
            mini_graf(c, x, 500, "fixa", a, 300, 220, AMBER)
            pill(c, "não nasce no zero: NÃO é proporção", x, 690, AMBER, size=24, a=a, anchor="center")


# treino: (cue da pergunta, cue da resposta, tipo, dado, decisão, cor, teste)
TREINO = [("06.b", "07.a", "tab", [("2", "9"), ("4", "18"), ("6", "27")], "DIRETA", DIR, "÷ = 4,5 sempre"),
          ("06.c", "07.b", "tab", [("1", "24"), ("3", "8"), ("6", "4")], "INVERSA", INV, "× = 24 sempre"),
          ("06.d", "07.c", "graf", "fixa", "NENHUMA", AMBER, "começa no 5, não no zero"),
          ("06.e", "07.d", "graf", "hiper", "INVERSA", INV, "hipérbole: nunca toca")]


def b_treino(c, t, C, B):
    head_seq(c, t, C, [("06", "TREINO-RELÂMPAGO", "DIRETA, INVERSA OU NENHUMA?", PURPLE),
                       ("07", "CONFERINDO", "OS DOIS TESTES E A ORIGEM", PURPLE)])
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    for k, (s, col) in enumerate((("DIRETA", DIR), ("INVERSA", INV), ("NENHUMA", AMBER))):
        pill(c, s, 640 + k * 320, 205, col, size=22, a=aa, anchor="center", bounds=(0, 1920))
    for k, (cq, cr, tipo, dado, dec, col, teste) in enumerate(TREINO):
        a, d = rise(t, C[cq])
        if a <= 0:
            continue
        x, y = 360 + k * 400, 260 + d
        ar = ep(t, C[cr], 0.4) if t >= C["07"] else 0
        on_ = ar > 0 and (k == 3 or t < C[TREINO[k + 1][1]])
        rrect(c, x - 180, y, 360, 440, 20, mix("#F7F7F5", col, 0.10 * ar), a)
        if on_:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 180, y, 360, 440), 20, 20), paint(col, a, stroke=4))
        badge_num(c, k + 1, x, y + 44, a, 24, bg=col if ar > 0 else INK2)
        if tipo == "tab":
            mini_tab(c, x - 88, y + 92, dado, a, BLUE, rh=44, wc=(80, 90), size=30)
        else:
            mini_graf(c, x, y + 180, dado, a, 210, 150, INV if dado == "hiper" else BLUE)
        if ar <= 0:
            fmid(c, "?", x, y + 350, 64, "black", AMBER, a)
        else:
            pill(c, dec, x, y + 330, col, size=28, a=ar, anchor="center", bounds=(0, 1920))
            ftext(c, teste, x, y + 400, 22, "black", INK2, ar)
    pause_timer(c, t, C["06.end"] - 1.9, W / 2, 770)


# ======================================================================
# verdadeiro ou falso
# ======================================================================

def b_vf_intro(c, t, C, B):
    frame(c, t, B["start"], "PAUSE E RESPONDA", "VERDADEIRO OU FALSO?", AMBER)
    a0 = ep(t, C["08"], 0.5)
    chip(c, "V", 820, 360, GREEN, a0, 90)
    fmid(c, "ou", W / 2, 360, 50, "black", GRAY, a0)
    chip(c, "F", 1100, 360, RED, a0, 90)
    aa = ep(t, C["08.a"], 0.5)
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 90 + k * 90, 560, ep(t, C["08.a"] + 0.12 * k, 0.3), 30, bg=INK2)
    text(c, "os erros que mais custam pontos", W / 2, 650, 32, "bold", INK2, aa)
    pill(c, "pause ANTES da resposta", W / 2, 750, AMBER, size=30, a=ep(t, C["08.b"], 0.5), anchor="center")


# (contexto, afirmação, verdadeira?, por que engana, regra certa, versão certa, ícone, selo)
VF = [
    ("um gráfico em forma de reta", "$y = 2x + 10", False, "é uma reta, e a direta também é",
     "x = 0 dá y = 10, não zero: tem parcela fixa", "não é proporção", 2, "PERGUNTA DA ORIGEM"),
    ("táxi: R$ 6 + R$ 2,50 por km", "8 km → R$ 26 · 16 km → R$ 46", True, "dá vontade de dobrar: R$ 52",
     "a bandeirada é cobrada UMA vez só", "6 + 40 = 46", 2, "PERGUNTA DA ORIGEM"),
    ("um quadrado", "lado × 2 → área × 2", False, "lado e área crescem juntos",
     "os azulejos: 2 de largura × 2 de comprimento", "lado × 2 → área × 4", 4, None),
    ("uma lâmpada", "distância × 2 → luz ÷ 2", False, "parece uma inversa simples",
     "a mesma luz se espalha por uma área 4 vezes maior", "distância × 2 → luz ÷ 4", 4, None),
    ("uma criança", "idade e altura NÃO são proporcionais", True, "crescer junto parece proporção",
     "ninguém tem o dobro da altura ao dobrar de idade", "razão constante", 0, None),
    ("uma tabela", "a 1ª linha basta para achar o k", False, "uma linha sozinha sempre dá algum número",
     "é a CONSTÂNCIA que prova a relação", "teste TODAS as linhas", 1, None),
    ("horas decimais", "2,4 h = 2 h 24 min", True, "a gente lê 2 h 40",
     "décimo de hora não é minuto: 0,4 · 60 = 24", "2 h 24 min", 0, None),
    ("y = k · a/b, com a × 2 e b × 3", "y fica × 6", False, "o 2 e o 3 parecem se juntar",
     "o b está EMBAIXO: ele divide", "$y × 2/3", 3, None),
    ("a relação inversa", "a hipérbole toca os eixos", False, "a curva chega muito perto",
     "o tempo de viagem nunca chega a zero", "nunca toca", 1, None),
]
VF_IDS = [f"{9 + k:02d}" for k in range(9)]


def b_vf(c, t, C, B):
    sid = which(t, C, VF_IDS)
    n = VF_IDS.index(sid)
    ctx, conta, ver, engana, regra_, fix, ic, teste = VF[n]
    head(c, t, C[sid], f"VERDADEIRO OU FALSO? · {n + 1} DE 9", "PAUSE E RESPONDA", AMBER)
    card(c, *CARD_R)
    q = lambda x: C[f"{sid}.{x}"]
    for k in range(9):
        badge_num(c, k + 1, W / 2 - 4 * 66 + k * 66, 200, 1, 20, bg=AMBER if k == n else LIGHT)
    a0 = ep(t, q("t"), 0.5)
    if n == 8:
        mini_graf(c, 330, 400, "hiper", a0, 220, 160, INV)
    else:
        icone(c, ic, 330, 400, 0.85, a0)
    text(c, ctx, 960, 310, 32, "bold", INK2, a0)
    ar = ep(t, q("r"), 0.4)
    sz = 60
    while mtext_w(conta, sz) > 760:
        sz -= 2
    mtext(c, conta, 960, 410, sz, a0)
    if ar > 0 and not ver:
        w = mtext_w(conta, sz)
        strike(c, 960 - w / 2 - 10, 415, 960 + w / 2 + 10, 415, ar, RED, ar)
    pause_timer(c, t, q("p"), 1620, 400)
    selo(c, 1580, 400, ar, "VERDADEIRO" if ver else "FALSO", GREEN if ver else RED, -6, 40)
    ae = ep(t, q("e"), 0.5)
    if ae > 0:
        if ver:
            pill(c, "PARECE FALSO PORQUE...", 230, 540, AMBER, size=26, a=ae, bounds=(0, 1920))
        else:
            selo(c, 350, 540, ae, "PEGADINHA", AMBER, -5, 30)
        text(c, engana, 640 if ver else 520, 552, 34, "bold", INK2, ae, align="left")
    ag = ep(t, q("g"), 0.5)
    if ag > 0:
        boxed(c, 200, 630, 1520, 170, GREEN, ag, 0.07)
        para(c, regra_, 240, 700, 30, "black", GREEN, ag, 760)
        szf = 46
        while mtext_w(fix, szf) > 600:
            szf -= 2
        mtext(c, fix, 1340, 715, szf, ag, GREEN)
        if teste:
            selo(c, 1480, 600, ag, teste, AMBER, -5, 22)


def b_vf_placar(c, t, C, B):
    frame(c, t, B["start"], "QUANTAS VOCÊ ACERTOU?", "O PLACAR", AMBER)
    aa = ep(t, C["18.a"], 0.5)
    for k, v in enumerate(VF):
        a = aa * ep(t, C["18.a"] + 0.12 * k, 0.3)
        x = W / 2 - 4 * 150 + k * 150
        badge_num(c, k + 1, x, 260, a, 26, bg=INK2)
        chip(c, "V" if v[2] else "F", x, 360, GREEN if v[2] else RED, a, 50)
    text(c, "6 falsas · 3 verdadeiras", W / 2, 490, 40, "black", INK, aa)
    ab = ep(t, C["18.b"], 0.5)
    chip(c, "AGORA: 5 QUESTÕES INÉDITAS", W / 2, 640, GREEN, ab, 44)
    text(c, "no estilo do ENEM", W / 2, 750, 30, "bold", INK2, ab)


# ======================================================================
# as 5 questões inéditas
# ======================================================================
# enun: (cue, texto, destaque?) · passos: (cue, texto ou '$expr') · selo1/selo2: (rótulo, texto curto, cor, cue)

CAMISETAS = [("10", "R$ 120"), ("20", "R$ 240"), ("30", "R$ 300"), ("40", "R$ 360")]

Q = {
    "q1": dict(ids=("19", "20"), titulo="A GRÁFICA", ok="E", icone=1,
               enun=[("a", "Uma gráfica registrou o preço total cobrado por lotes de camisetas:", False),
                     ("b", "Sobre o número de camisetas e o preço total, é correto afirmar que as duas grandezas são", True)],
               tabela=CAMISETAS,
               alts=[("A", "diretamente proporcionais, com k = 12", "só 2 linhas", AMBER),
                     ("B", "inversamente proporcionais, com k = 1 200", "1 linha só", RED),
                     ("C", "inversamente proporcionais, com k = 12", "trocou o teste", RED),
                     ("D", "diretamente proporcionais, com k = 9", "só a última", RED),
                     ("E", "nem diretamente nem inversamente proporcionais", "", GREEN)],
               selo1=("O DETETIVE", "divide e multiplica, em TODAS as linhas", PURPLE, "d"),
               plaus="lote maior costuma ter desconto ✓"),
    "q2": dict(ids=("21", "22"), titulo="A CONTA DE ÁGUA", ok="C", icone=2,
               enun=[("a", "Uma companhia de água cobra uma taxa fixa de R$ 30,00 por mês mais R$ 5,00 por metro cúbico "
                           "consumido.", False),
                     ("b", "Uma família consumiu 10 m³ e pagou R$ 80,00. No mês seguinte, consumiu o dobro. Quanto pagou?",
                      True)],
               alts=[("A", "R$ 100,00", "esqueceu a taxa", RED), ("B", "R$ 110,00", "dobrou a parte fixa", RED),
                     ("C", "R$ 130,00", "", GREEN), ("D", "R$ 160,00", "dobrou tudo, até a taxa", AMBER),
                     ("E", "R$ 190,00", "dobrou e somou outra taxa", RED)],
               selo1=("PERGUNTA DA ORIGEM", "consumo zero → conta de R$ 30: parcela fixa", AMBER, "g"),
               passos=[("a", "20 · 5 = 100  (o que varia)"), ("b", "30 + 100 = R$ 130")]),
    "q3": dict(ids=("23", "24"), titulo="AS MÁQUINAS", ok="B", icone=0,
               enun=[("a", "Três máquinas iguais embalam um lote de produtos em 6 horas.", False),
                     ("b", "Com 5 máquinas iguais a essas, no mesmo ritmo, o mesmo lote será embalado em", True)],
               alts=[("A", "3 h 6 min", "leu 0,6 h como 6 min", AMBER), ("B", "3 h 36 min", "", GREEN),
                     ("C", "4 h", "leu 0,6 h como 60 min", AMBER), ("D", "6 h", "achou que nada muda", RED),
                     ("E", "10 h", "usou direta", RED)],
               selo1=("INVERSA", "mais máquinas, menos tempo: o PRODUTO não muda", INV, "d"),
               passos=[("a", "3 · 6 = 18 = 5 · t"), ("b", "t = 18 ÷ 5 = 3,6 h"), ("c", "0,6 · 60 = 36 min")],
               relogio=True),
    "q4": dict(ids=("25", "26"), titulo="A PRESSÃO", ok="C", icone=3,
               enun=[("a", "A pressão que um objeto faz sobre o chão é diretamente proporcional à força e inversamente "
                           "proporcional à área de apoio.", False),
                     ("b", "Um objeto faz pressão de 600 pascals.", False),
                     ("c", "Se a força triplicar e a área de apoio dobrar, a pressão passará a ser de", True)],
               alts=[("A", "300 Pa", "ignorou a força", RED), ("B", "400 Pa", "trocou os andares", AMBER),
                     ("C", "900 Pa", "", GREEN), ("D", "1 800 Pa", "ignorou a área", RED),
                     ("E", "3 000 Pa", "SOMOU os efeitos (× 5)", AMBER)],
               selo1=("FRAÇÃO-GUIA", "força em cima, área embaixo", PURPLE, "d"),
               passos=[("a", "× 3  e  ÷ 2"), ("b", "600 · 3 ÷ 2 = 900 Pa")],
               guia=True),
    "q5": dict(ids=("27", "28"), titulo="A CAIXA DE SOM", ok="D", icone=4,
               enun=[("a", "A intensidade do som de uma caixa de som é inversamente proporcional ao quadrado da "
                           "distância até ela.", False),
                     ("b", "A 4 metros, um medidor marca 50 unidades.", False),
                     ("c", "A 2 metros da caixa, o medidor vai marcar", True)],
               alts=[("A", "12,5", "aplicou o 1/4 ao contrário", RED), ("B", "25", "tratou como direta", RED),
                     ("C", "100", "esqueceu o quadrado", AMBER), ("D", "200", "", GREEN),
                     ("E", "400", "usou o cubo", RED)],
               selo1=("A LANTERNA", "distância ÷ 2 → área ÷ 4 → som × 4", AMBER, "d"),
               passos=[("a", "distância ÷ 2 → intensidade × 4"), ("b", "50 · 4 = 200")],
               plaus="mais perto, mais alto ✓"),
}


def selo_linha(c, x, y, w, rotulo, s, col, a):
    """caixa com rótulo (PERGUNTA DA ORIGEM, FRAÇÃO-GUIA...) e uma linha curta"""
    if a <= 0:
        return
    boxed(c, x, y, w, 84, col, a, 0.08)
    pill(c, rotulo, x + 20, y, col, size=18, a=a, bounds=(0, 1920))
    sz = 26
    while K.ftext_w(s, "black", sz) > w - 40:
        sz -= 1
    ftext(c, s, x + 20, y + 54, sz, "black", INK, a, align="left")


def tab_q1(c, t, C, x, y, a, sol):
    """a tabela da questão 1; na resolução nascem as colunas ÷ e ×"""
    if a <= 0:
        return
    cab = ["camisetas", "preço"]
    ws = [150, 170]
    for k, (s, w) in enumerate(zip(cab, ws)):
        xx = x + sum(ws[:k]) + 8 * k
        text(c, s, xx + w / 2, y - 12, 22, "black", INK2, a)
    rh = 52
    quoc = ["12", "12", "10", "9"]
    prod = ["1 200", "4 800", "9 000", "14 400"]
    ad_, ac_ = ep(t, C["20.a"], 0.4) * sol, ep(t, C["20.c"], 0.4) * sol
    ab_ = ep(t, C["20.b"], 0.4)
    for r_, (u, v) in enumerate(CAMISETAS):
        yy = y + r_ * (rh + 8)
        for k, (s, w) in enumerate(((u, ws[0]), (v, ws[1]))):
            xx = x + sum(ws[:k]) + 8 * k
            rrect(c, xx, yy, w, rh, 10, "#FFFFFF", a, stroke=2, stroke_color=INK2)
            text_mid(c, s, xx + w / 2, yy + rh / 2, 30, "black", INK if k == 0 else BLUE, a)
        if sol > 0:
            xq = x + 350
            aq = ad_ if r_ < 2 else ab_ * sol
            cq = GREEN if r_ < 2 and ab_ <= 0 else (RED if ab_ > 0 else GREEN)
            text_mid(c, quoc[r_], xq + 50, yy + rh / 2, 30, "black", cq, aq)
            ap = ac_ * ep(t, C["20.c"] + 0.35 * r_, 0.3)
            text_mid(c, prod[r_], xq + 170, yy + rh / 2, 28, "black", RED, ap)
    if sol > 0:
        text(c, "÷", x + 400, y - 12, 26, "black", PURPLE, ad_)
        text(c, "×", x + 520, y - 12, 26, "black", PURPLE, ac_)


def mini_relogio(c, cx, cy, r, minutos, a):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r + 6, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r + 6, paint(INK, a, stroke=6))
    p = skia.Path(); p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, minutos / 60 * 360, False); p.close()
    c.drawPath(p, paint(GREEN, a * 0.3))
    for k in range(12):
        ang = -math.pi / 2 + k * math.pi / 6
        c.drawLine(cx + (r - 12) * math.cos(ang), cy + (r - 12) * math.sin(ang), cx + r * math.cos(ang),
                   cy + r * math.sin(ang), paint(INK, a, stroke=3))
    ang = -math.pi / 2 + minutos / 60 * 2 * math.pi
    c.drawLine(cx, cy, cx + (r - 16) * math.cos(ang), cy + (r - 16) * math.sin(ang), paint(GREEN, a, stroke=7, cap_round=True))
    c.drawCircle(cx, cy, 7, paint(INK, a))


def faz_questao(nome):
    d = Q[nome]
    s1, s2 = d["ids"]
    num = int(nome[1])

    def bloco(c, t, C, B):
        head(c, t, B["start"], f"QUESTÃO {num} DE 5 · ESTILO ENEM", d["titulo"], BLUE)
        card(c, *CARD_R)
        a0 = ep(t, C[s1], 0.5)
        pill(c, "QUESTÃO EXTRA DA SÉRIE (ESTILO ENEM)", 180, 200, BLUE, size=20, a=a0, bounds=(0, 1920))
        text(c, "Situação hipotética, elaborada para fins didáticos.", 180, 828, 18, "medium", GRAY, a0, align="left")
        sol = ep(t, C[s2], 0.5)
        cues_in = {L: C[f"{s1}.l{L.lower()}"] for L in "ABCDE"}
        cues_x = {L: C[f"{s2}.x{L.lower()}"] for L in "ABCDE" if L != d["ok"]}
        if nome == "q1":
            # enunciado curto em cima, a tabela no meio, a pergunta embaixo; alternativas longas à direita
            a = ep(t, C[f"{s1}.a"], 0.4)
            para(c, d["enun"][0][1], 180, 280, 28, "bold", INK, a * (1 - sol), 640, 36)
            selo_linha(c, 170, 250, 640, *d["selo1"][:3], ep(t, C[f"{s2}.{d['selo1'][3]}"], 0.4) * sol)
            tab_q1(c, t, C, 190, 400, a, sol)
            ab = ep(t, C[f"{s1}.b"], 0.4) * (1 - sol)
            para(c, d["enun"][1][1], 180, 680, 28, "black", BLUE, ab, 640, 36)
            pause_timer(c, t, C[f"{s1}.end"] - 1.9, 740, 640)
            if sol > 0:
                pill(c, "nenhum dos dois é constante", 480, 690, RED, size=24, a=ep(t, C["20.c"] + 1.6, 0.4),
                     anchor="center", bounds=(0, 1920))
                pill(c, d["plaus"], 480, 760, GREEN, size=22, a=ep(t, C[f"{s2}.v"], 0.4), anchor="center",
                     bounds=(0, 1920))
            K.alternativas(c, t, C, d["alts"], 860, 230, 840, 28, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=16)
            result_box(c, f"Letra {d['ok']}", 1290, 790, 34, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
            return
        y = 270
        for cue, s, dest in d["enun"]:
            a = ep(t, C[f"{s1}.{cue}"], 0.4) * (1 - sol)
            h = para(c, s, 180, y + 22, 30, "black" if dest else "bold", BLUE if dest else INK, a, 620, 40)
            y += h + 18
        icone(c, d["icone"], 380, 715, 0.7, a0 * (1 - sol))
        pause_timer(c, t, C[f"{s1}.end"] - 1.9, 680, 715)
        K.alternativas(c, t, C, d["alts"], 880, 230, 820, 34, C[f"{s2}.ok"], d["ok"], cues_in, cues_x, gap=14)
        if sol > 0:
            rot, s_, col, cue = d["selo1"]
            selo_linha(c, 170, 250, 620, rot, s_, col, ep(t, C[f"{s2}.{cue}"], 0.4) * sol)
            yy = 410
            if d.get("guia"):
                guia(c, 300, 470, ep(t, C[f"{s2}.d"] + 1.0, 0.4) * sol, "força", "área", w=200, size=28)
                yy = 590
            for j, (cue, s) in enumerate(d["passos"]):
                a = ep(t, C[f"{s2}.{cue}"], 0.4)
                last = j == len(d["passos"]) - 1
                sz = 38
                while mtext_w(s, sz) > 560:
                    sz -= 2
                mtext(c, s, 480 if not d.get("guia") else 600, yy, sz, a, GREEN if last else None)
                yy += 66
            if d.get("relogio"):
                mini_relogio(c, 680, 640, 60, 36, ep(t, C[f"{s2}.c"], 0.4))
            if d.get("plaus"):
                pill(c, d["plaus"], 480, 700, GREEN, size=22, a=ep(t, C[f"{s2}.v"], 0.4), anchor="center",
                     bounds=(0, 1920))
            result_box(c, f"Letra {d['ok']}", 480, 775, 38, ep(t, C[f"{s2}.ok"], 0.5), GREEN)
    return bloco


# ======================================================================
# checklist, meta, ponte e CTA
# ======================================================================

CHECK = [("29.b", "EP. 1", ["quociente e produto", "achar o k e o que ele significa", "décimo de hora em minutos"]),
         ("29.c", "EP. 2", ["tabela: dividir e multiplicar", "testar todas as linhas"]),
         ("29.d", "EP. 3", ["o desenho de cada gráfico", "reta fora da origem e parcela fixa"]),
         ("30.a", "EP. 4", ["direto em cima, inverso embaixo", "ler fórmulas de Física"]),
         ("30.b", "EP. 5", ["quadrado, cubo e inverso do quadrado"]),
         ("30.c", "TODOS", ["conferir se o resultado faz sentido"])]


def b_checklist(c, t, C, B):
    frame(c, t, B["start"], "CHECKLIST DE DOMÍNIO", "MARQUE SÓ O QUE EXPLICA EM VOZ ALTA", GREEN)
    aa = ep(t, C["29.a"], 0.5) * (1 - ep(t, C["29.b"], 0.4))
    pill(c, "explicar em voz alta, sem consultar nada", W / 2, 470, GREEN, size=34, a=aa, anchor="center")
    for k, (cue, ep_, itens) in enumerate(CHECK):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        col_ = 0 if k < 3 else 1
        x = 190 if col_ == 0 else 1000
        y0 = 200 + sum(len(CHECK[j][2]) * 52 + 34 for j in range(0 if col_ == 0 else 3, k))
        pill(c, ep_, x, y0 + 20, PURPLE if k < 5 else GREEN, size=20, a=a, bounds=(0, 1920))
        for j, it in enumerate(itens):
            yy = y0 + 20 + j * 52
            rrect(c, x + 110, yy - 16, 32, 32, 7, "#FFFFFF", a, stroke=3, stroke_color=INK2)
            ftext(c, it, x + 160, yy + 11, 28, "bold", INK, a, align="left")
    ae = ep(t, C["30.d"], 0.5)
    if ae > 0:
        boxed(c, 1000, 640, 700, 110, AMBER, ae, 0.10)
        text_mid(c, "não marcou? reveja o episódio", 1350, 695, 32, "black", INK, ae)


def b_meta(c, t, C, B):
    frame(c, t, B["start"], "ANTES DE DIZER “DOMINADO”", "A META", GREEN)
    aa = ep(t, C["31.a"], 0.5)
    ab = ep(t, C["31.b"], 0.5)
    for i in range(30):
        r_, k = divmod(i, 10)
        a = aa * ep(t, C["31.a"] + 0.03 * i, 0.2)
        ok = ab > 0 and i < 21
        x, y = 250 + k * 82, 250 + r_ * 92
        rrect(c, x, y, 66, 72, 12, mix("#E6E6E2", GREEN, ab if ok else 0), a)
        if ok:
            check_icon(c, x + 33, y + 36, 18, ab, "#FFFFFF")
        else:
            text_mid(c, str(i + 1), x + 33, y + 36, 24, "black", INK2, a)
    text(c, "30 questões", 1450, 320, 52, "black", INK, aa)
    text(c, "21 acertos = 70%", 1450, 420, 46, "black", GREEN, ab)
    ac = ep(t, C["31.c"], 0.5)
    if ac > 0:
        boxed(c, 250, 600, 1420, 160, AMBER, ac, 0.10)
        mini_tab(c, 300, 625, [("1", "5"), ("2", "10")], ac, BLUE, rh=46, wc=(70, 80), size=26)
        mini_graf(c, 1540, 690, "fixa", ac, 140, 90, AMBER)
        text_mid(c, "priorize: TABELA e PARCELA FIXA", W / 2, 680, 38, "black", INK, ac)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "SÉRIE COMPLETA", "PRÓXIMO ASSUNTO", PURPLE)
    aa = ep(t, C["32.a"], 0.5)
    text(c, "PRÓXIMO ASSUNTO", W / 2, 250, 28, "black", GRAY, aa, tracking=2)
    text(c, "Divisão proporcional", W / 2, 330, 62, "black", PURPLE, aa)
    ab = ep(t, C["32.b"], 0.5)
    if ab > 0:
        for k, (n, col) in enumerate(((2, BLUE), (3, PURPLE), (5, GREEN))):
            x0 = 520 + k * 300
            for j in range(n):
                xx = x0 + (j % 3) * 70
                yy = 450 + (j // 3) * 80
                rrect(c, xx, yy, 60, 56, 10, col, ab * ep(t, C["32.b"] + 0.1 * j, 0.3), shadow=True)
                text_mid(c, "k", xx + 30, yy + 28, 28, "black", "#FFFFFF", ab)
        text(c, "os pacotinhos de k viram a ferramenta principal", W / 2, 700, 34, "black", INK, ab)


def b_cta(c, t, C, B):
    cta(c, t, C["33.like"], C["33.sub"], C["33.bell"], C["33.com"], C["33.bye"], "Qual questão te pegou?",
        canal="no Estudativo", anki=C["33.anki"])


BLOCKS = dict(hook=b_hook, formatos=b_formatos, indice=b_indice, rendem=b_rendem, treino=b_treino, vf_intro=b_vf_intro,
              vf=b_vf, vf_placar=b_vf_placar, q1=faz_questao("q1"), q2=faz_questao("q2"), q3=faz_questao("q3"),
              q4=faz_questao("q4"), q5=faz_questao("q5"), checklist=b_checklist, meta=b_meta, ponte=b_ponte, cta=b_cta)
