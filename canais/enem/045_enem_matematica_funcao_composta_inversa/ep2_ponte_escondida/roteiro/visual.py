"""Visual — Função Composta e Função Inversa, Episódio 2: composição em contexto e a função escondida (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr, alternativas, erro_cards, atalho...).
Peças deste episódio: balao() (o balão meteorológico), cadeia3() (as três caixas TEM → PONTE → QUER, com a ponte que
brilha e some), caixa_q() (a caixa fechada com "?" que abre), relogio(), pilha(), linha().
Cores com função: azul = definição · roxo = regra/fórmula · âmbar = armadilha · verde = atalho/dica · vermelho = erro.
A função de DENTRO é AZUL e a de FORA é ROXA em todo o episódio (como no ep. 1); a PONTE é âmbar.
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
_s = importlib.util.spec_from_file_location("comum045", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                 K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_composta_inversa_ep2_ponte_escondida.mp4"
CARD_R = K.CARD_R
COL_IN, COL_OUT, COL_PONTE = BLUE, PURPLE, AMBER


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [ftext_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        ftext(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def balao(c, cx, cy, r, a):
    """balão meteorológico: bola branca com contorno, cordinha e a caixinha do sensor"""
    if a <= 0:
        return
    line(c, cx, cy + r * 0.98, cx, cy + r * 1.9, INK2, a, 3)
    rrect(c, cx - r * 0.22, cy + r * 1.9, r * 0.44, r * 0.32, 6, AMBER, a)
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(RED, a, stroke=6))
    c.drawCircle(cx - r * 0.35, cy - r * 0.35, r * 0.18, paint(mix("#FFFFFF", RED, 0.25), a))


def caixa(c, cx, cy, tit, sub, col, a, brilho=0.0, w=380, h=170):
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, mix("#FFFFFF", col, 0.10 + 0.30 * brilho), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26),
                paint(col, a, stroke=5 + 4 * brilho))
    sz = 44
    while ftext_w(tit, "black", sz) > w - 40 and sz > 20:
        sz -= 2
    fmid(c, tit, cx, cy - h * 0.13, sz, "black", col, a)
    if sub:
        text(c, sub, cx, cy + h * 0.30, 26, "bold", INK2, a)


def cadeia3(c, t, nomes, subs, cy, a, t_ponte=None, t_some=None, lei=None):
    """três caixas em fila; em t_ponte a do meio brilha (ponte), em t_some ela some e fica a seta direta com a lei"""
    if a <= 0:
        return
    xs = (420, 960, 1500)
    br = 0.0
    if t_ponte is not None:
        br = ep(t, t_ponte, 0.5) * (0.65 + 0.35 * math.sin(max(0.0, t - t_ponte) * 5))
    some = ep(t, t_some, 0.5) if t_some is not None else 0.0
    caixa(c, xs[0], cy, nomes[0], subs[0], COL_IN, a)
    caixa(c, xs[2], cy, nomes[2], subs[2], COL_OUT, a)
    caixa(c, xs[1], cy, nomes[1], subs[1], COL_PONTE, a * (1 - some), br)
    am = a * (1 - some)
    arrow(c, xs[0] + 195, cy, xs[1] - 200, cy, INK2, am, 5)
    arrow(c, xs[1] + 195, cy, xs[2] - 200, cy, INK2, am, 5)
    if br > 0 and some < 1:
        pill(c, "PONTE", xs[1], cy - 125, COL_PONTE, size=28, a=a * ep(t, t_ponte, 0.4) * (1 - some), anchor="center")
    if some > 0:
        y2 = cy - 30
        arrow(c, xs[0] + 195, y2, xs[2] - 200, y2, GREEN, a * some, 7, progress=some)
        if lei:
            al = a * ep(t, t_some + 0.5, 0.4)
            rrect(c, xs[1] - 230, y2 + 30, 460, 86, 20, "#FFFFFF", al, shadow=True)
            K.expr(c, lei, xs[1], y2 + 73, 40, al, cores={i: GREEN for i in range(8)})


def caixa_q(c, cx, cy, a, aberta=0.0, conteudo=None, w=230, h=120, col=None):
    """a caixa fechada com '?'; aberta (0..1) levanta a tampa e mostra o conteúdo"""
    if a <= 0:
        return
    col = col or COL_IN
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x, y, w, h, 16, mix("#FFFFFF", col, 0.12), a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 16, 16), paint(col, a, stroke=5))
    if conteudo and aberta > 0:
        sz = 40
        while K.math_w(conteudo, sz) > w - 24 and sz > 20:
            sz -= 2
        K.expr(c, conteudo, cx, cy + 4, sz, a * aberta, cores={i: GREEN for i in range(6)})
    fmid(c, "?", cx, cy, h * 0.62, "black", col, a * (1 - aberta))
    # tampa
    lift = 30 * aberta
    c.save()
    c.translate(x - 8, y - lift)
    c.rotate(-12 * aberta)
    rrect(c, 0, -22, w + 16, 26, 8, col, a * (1 - aberta))
    c.restore()


def relogio(c, cx, cy, r, a, ang=0.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint("#FFFFFF", a))
    c.drawCircle(cx, cy, r, paint(INK, a, stroke=6))
    for k in range(12):
        an = k * math.pi / 6
        line(c, cx + math.sin(an) * r * 0.80, cy - math.cos(an) * r * 0.80, cx + math.sin(an) * r * 0.92,
             cy - math.cos(an) * r * 0.92, INK2, a, 3)
    line(c, cx, cy, cx + math.sin(ang) * r * 0.70, cy - math.cos(ang) * r * 0.70, BLUE, a, 6)
    line(c, cx, cy, cx, cy - r * 0.45, INK, a, 7)


def pilha(c, cx, base, n, a, w=150):
    for k in range(n):
        rrect(c, cx - w / 2 + (k % 2) * 8, base - (k + 1) * 30, w, 26, 6, mix("#FFFFFF", PURPLE, 0.45), a)


def rotulo(c, s, cx, cy, col, a, size=26):
    pill(c, s, cx, cy, col, size=size, a=a, anchor="center")


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "COMPOSTA EM CONTEXTO", BLUE)
    a0 = ep(t, C["01.a"], 0.5)
    sobe = ep(t, C["01.a"], 6.0)
    balao(c, 520, lerp(700, 360, ease_io(sobe)), 80, a0)
    if a0 > 0:
        line(c, 260, 820, 260, 260, "#D5D8DE", a0, 4)
        for k in range(5):
            line(c, 248, 820 - k * 130, 272, 820 - k * 130, "#9AA0AA", a0, 3)
        rotulo(c, "0,2 km por minuto", 880, 330, BLUE, a0, 32)
    ab = ep(t, C["01.b"], 0.4)
    if ab > 0:
        rotulo(c, "−6 °C a cada km", 880, 430, PURPLE, ab, 32)
    acc = ep(t, C["01.c"], 0.4)
    if acc > 0:
        rrect(c, 1180, 300, 520, 200, 26, "#FFFFFF", acc, shadow=True)
        text(c, "aos 10 minutos", 1440, 360, 32, "black", GRAY, acc)
        fmid(c, "? °C", 1440, 440, 70, "black", AMBER, acc)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        regra(c, "1 fórmula só · a altitude nem aparece", W / 2, 770, ad, 40, GREEN)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    a, d = rise(t, C["02.a"])
    check_icon(c, 300, 346 + d, 34, a, GREEN)
    text(c, "juntar DUAS fórmulas numa só", 360, 360 + d, 50, "black", INK, a, align="left")
    ab, db = rise(t, C["02.b"])
    check_icon(c, 300, 486 + db, 34, ab, GREEN)
    text(c, "achar a FUNÇÃO ESCONDIDA", 360, 500 + db, 50, "black", INK, ab, align="left")
    if ab > 0:
        caixa_q(c, 1100, 680, ab, 0.0, w=200, h=110)
        K.expr(c, "f(?) = 8x - 1", 1430, 690, 44, ab, cores={0: COL_OUT})


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "RÁPIDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "episódio 1", 560, 280, 26, "bold", GRAY, aa)
        linha(c, [("f", COL_OUT), ("(", INK), ("g", COL_IN), ("(x)", INK), (")", INK)], 560, 400, 96, aa)
        pill(c, "de dentro para fora", 560, 520, GREEN, size=28, a=aa, anchor="center")
        arrow(c, 660, 600, 460, 600, GREEN, aa, 6)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "série de Função Afim", 1360, 280, 26, "bold", GRAY, ab)
        linha(c, [("custo", INK), (" = ", GRAY), ("fixo", AMBER)], 1360, 390, 56, ab)
        linha(c, [("+ ", GRAY), ("preço por unidade", BLUE), (" × ", GRAY), ("quantidade", PURPLE)], 1360, 480, 40, ab)
        text(c, "ex.: 500 + 3n", 1360, 580, 34, "black", INK2, ab)
    line(c, 960, 260, 960, 700, "#E6E6E2", ab, 3)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "UMA COISA PUXA A OUTRA", "BALÃO E FÁBRICA", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["04.a"], 0.5)
    if aa > 0:
        sobe = ep(t, C["04.a"], 3.0)
        balao(c, 600, lerp(520, 330, ease_io(sobe)), 62, aa)
        linha(c, [("tempo ↑", BLUE), ("  →  ", GRAY), ("altura ↑", AMBER), ("  →  ", GRAY), ("frio ↑", PURPLE)],
              600, 680, 30, aa)
    ab = ep(t, C["04.b"], 0.5)
    if ab > 0:
        relogio(c, 1240, 470, 90, ab, ep(t, C["04.b"], 3.0) * math.pi * 2)
        pilha(c, 1520, 600, 2 + int(5 * ep(t, C["04.b"], 3.0)), ab)
        linha(c, [("horas", BLUE), ("  →  ", GRAY), ("peças", AMBER), ("  →  ", GRAY), ("R$", PURPLE)], 1380, 680, 36, ab)
    line(c, 960, 260, 960, 700, "#E6E6E2", ab, 3)
    acc = ep(t, C["04.c"], 0.5)
    if acc > 0:
        regra(c, "GRANDEZA = tudo que dá para medir", W / 2, 770, acc, 40, BLUE)


# ======================================================================
# bloco a — a estratégia
# ======================================================================

def b_estrategia(c, t, C, B):
    head(c, t, B["start"], "A ESTRATÉGIA", "ACHE A PONTE", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    cadeia3(c, t, ("O QUE VOCÊ TEM", "INTERMEDIÁRIA", "O QUE VOCÊ QUER"), ("", "está nas DUAS fórmulas", ""),
            450, aa, C["05.b"], C["05.c"] + 1.0, None)
    if aa > 0:
        text(c, "GRANDEZA INTERMEDIÁRIA = a do meio, que liga as duas fórmulas", W / 2, 280, 30, "black", BLUE,
             aa * (1 - ep(t, C["05.c"], 0.4)))
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        regra(c, "SUBSTITUIR = trocar a letra da ponte pelo que ela vale", W / 2, 720, acc, 36)


# ======================================================================
# bloco b — o balão
# ======================================================================

def b_balao(c, t, C, B):
    head_seq(c, t, C, [("06", "O BALÃO", "DUAS FÓRMULAS", BLUE), ("07", "SUBSTITUA A PONTE", "ELA SOME", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            text(c, "altitude (km) depois de t minutos", 520, 280, 28, "bold", GRAY, aa)
            K.expr(c, "h(t) = 0,2t", 520, 370, 64, aa, cores={0: COL_IN})
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            text(c, "temperatura (°C) a h km de altura", 1400, 280, 28, "bold", GRAY, ab)
            K.expr(c, "T(h) = 25 - 6h", 1400, 370, 64, ab, cores={0: COL_OUT})
        acc = ep(t, C["06.c"], 0.5)
        if acc > 0:
            pill(c, "h", 655, 470, COL_PONTE, size=40, a=acc, anchor="center")
            pill(c, "h", 1590, 470, COL_PONTE, size=40, a=acc, anchor="center")
            rrect(c, 560, 570, 800, 120, 24, mix("#FFFFFF", COL_PONTE, 0.16), acc)
            text_mid(c, "a ALTITUDE está nas duas: é a ponte", W / 2, 630, 40, "black", COL_PONTE, acc)
        return
    a0 = ep(t, C["07"], 0.4)
    cadeia3(c, t, ("TEMPO", "ALTITUDE", "TEMPERATURA"), ("min", "km", "°C"), 330, a0, C["07"],
            C["07.b"], "T = 25 - 1,2t")
    aa = ep(t, C["07.a"], 0.5)
    if aa > 0:
        K.expr(c, "T = 25 - 6 · (0,2t)", 560, 560, 50, aa, cores={4: COL_IN, 5: COL_IN})
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        K.expr(c, "= 25 - 1,2t", 1260, 560, 50, ab, cores={3: GREEN})
        text(c, "6 · 0,2 = 1,2", 1260, 630, 28, "black", INK2, ab)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 520, 680, 880, 100, 22, "#FFFFFF", acc, shadow=True)
        linha(c, [("t = 10 min:  ", GRAY), ("25 − 12 = ", INK), ("13 °C", GREEN)], W / 2, 728, 42, acc)


def b_atalho(c, t, C, B):
    head(c, t, B["start"], "CONFIRA E ENCURTE", "O CAMINHO LONGO E O ATALHO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        text(c, "caminho longo", 520, 270, 28, "black", GRAY, aa)
        K.expr(c, "h(10) = 0,2 · 10 = 2", 520, 360, 44, aa, cores={0: COL_IN, 6: COL_PONTE})
        text(c, "km", 800, 360, 30, "black", COL_PONTE, aa)
        K.expr(c, "T(2) = 25 - 12 = 13", 520, 460, 44, ep(t, C["08.a"] + 2.0, 0.4), cores={0: COL_OUT, 6: GREEN})
        text(c, "°C", 800, 460, 30, "black", GREEN, ep(t, C["08.a"] + 2.0, 0.4))
        selo(c, 520, 570, ep(t, C["08.a"] + 3.4, 0.4), "BATEU", GREEN, -5, 32)
    line(c, 960, 260, 960, 720, "#E6E6E2", ep(t, C["08.b"], 0.4), 3)
    ab = ep(t, C["08.b"], 0.5)
    K.atalho(c, 1040, 260, 700, 120, "ATALHO", ["multiplique as taxas"], ab, 32)
    if ab > 0:
        linha(c, [("0,2 ", INK), ("km", COL_PONTE), ("/min", INK), ("  ×  ", GRAY), ("6 °C/", INK), ("km", COL_PONTE)],
              1400, 470, 40, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        line(c, 1300, 470, 1370, 450, RED, acc, 5)
        line(c, 1580, 470, 1650, 450, RED, acc, 5)
        rrect(c, 1100, 540, 600, 110, 22, mix("#FFFFFF", GREEN, 0.14), acc)
        text_mid(c, "= 1,2 °C por minuto", 1400, 595, 44, "black", GREEN, acc)


# ======================================================================
# bloco c — as cadeias
# ======================================================================

CADEIAS = [("tempo", "peças", "custo"), ("tempo", "altitude", "temperatura"), ("dólar", "real", "imposto")]


def b_cadeias(c, t, C, B):
    head(c, t, B["start"], "QUEM VAI DENTRO?", "TEM × QUER", BLUE)
    card(c, *CARD_R)
    for k, (a_, b_, c_) in enumerate(CADEIAS):
        a = ep(t, C["09.a"] + k * 1.4, 0.4)
        if a <= 0:
            continue
        y = 300 + k * 110
        rrect(c, 330, y - 44, 1260, 88, 20, "#FFFFFF", a, shadow=True)
        linha(c, [(a_, COL_IN), ("   →   ", GRAY), (b_, COL_PONTE), ("   →   ", GRAY), (c_, COL_OUT)], W / 2, y, 40, a)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        rotulo(c, "a DE DENTRO recebe o que você TEM", 560, 650, COL_IN, ab, 28)
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        rotulo(c, "a DE FORA entrega o que você QUER", 1360, 650, COL_OUT, acc, 28)
    ad = ep(t, C["09.d"], 0.5)
    if ad > 0:
        regra(c, "tem o tempo, quer o custo → dentro: peças(t) · fora: custo(peças)", W / 2, 770, ad, 32)


# ======================================================================
# bloco d — caso 1: conheço a de fora
# ======================================================================

def b_caso1(c, t, C, B):
    head_seq(c, t, C, [("10", "A FUNÇÃO ESCONDIDA", "CASO 1: CONHEÇO A DE FORA", PURPLE),
                       ("11", "ABRA A CAIXA", "ISOLE O g(x)", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        K.expr(c, "f(x) = 2x + 5", 560, 270, 46, aa, cores={0: COL_OUT})
        K.expr(c, "f(g(x)) = 8x - 1", 1360, 270, 46, aa, cores={0: COL_OUT, 2: COL_IN})
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0 and t < C["10.c"]:
        caixa_q(c, W / 2, 470, ab)
        text(c, "INCÓGNITA = o valor que você procura", W / 2, 600, 32, "black", BLUE, ab)
    acc = ep(t, C["10.c"], 0.5)
    sid = which(t, C, ["10", "11"])
    if acc > 0:
        # 2 · [?] + 5 = 8x − 1
        y = 440
        fmid(c, "2 ·", 600, y, 54, "black", INK, acc)
        aberta = ep(t, C["11.b"], 0.8) if sid == "11" else 0.0
        caixa_q(c, 790, y, acc, aberta, "4x - 3", 220, 110)
        passo = sid == "11" and t >= C["11.a"]
        ftext(c, "− 6" if passo else "+ 5", 920, y + 20, 54, "black", AMBER if passo else INK,
              acc if not (sid == "11" and t >= C["11.b"]) else acc * (1 - ep(t, C["11.b"], 0.4)), align="left")
        lado = "8x - 6" if passo else "8x - 1"
        K.expr(c, "= " + lado, 1260, y, 54, acc, cores={1: AMBER} if passo else {})
        if sid == "11":
            ab1 = ep(t, C["11.a"], 0.5)
            if ab1 > 0:
                pill(c, "+5 passa para o outro lado: TROCA O SINAL", W / 2, 570, AMBER, size=28, a=ab1 *
                     (1 - ep(t, C["11.b"], 0.4)), anchor="center")
            ab2 = ep(t, C["11.b"], 0.5)
            if ab2 > 0:
                pill(c, "divida TUDO por 2", W / 2, 570, GREEN, size=30, a=ab2, anchor="center")
    if sid == "11":
        acc2 = ep(t, C["11.c"], 0.5)
        if acc2 > 0:
            regra(c, "g(x) = 4x − 3", W / 2, 720, acc2, 56)


# ======================================================================
# bloco e — caso 2: conheço a de dentro
# ======================================================================

def b_caso2(c, t, C, B):
    head(c, t, B["start"], "CASO 2", "CONHEÇO A DE DENTRO", PURPLE)
    card(c, *CARD_R)
    X = 300
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        K.expr(c, "g(x) = x + 1", 560, 260, 44, aa, cores={0: COL_IN})
        K.expr(c, "f(g(x)) = x^2 + 2x", 1360, 260, 44, aa, cores={0: COL_OUT, 2: COL_IN})
    ab = ep(t, C["12.b"], 0.5)
    if ab > 0:
        linha(c, [("u = x + 1", COL_PONTE), ("     →     ", GRAY), ("x = u − 1", COL_PONTE)], W / 2, 370, 44, ab)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        K.expr(c, "f(u) = (u-1)^2 + 2(u-1)", X, 480, 50, acc, cores={0: COL_OUT}, align="left")
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        K.expr(c, "= u^2 - 2u + 1 + 2u - 2", X + 180, 580, 44, ad, cores={2: RED, 3: RED, 6: RED, 7: RED}, align="left")
        pill(c, "−2u e +2u se cancelam", 1420, 580, RED, size=24, a=ad, anchor="center")
        regra(c, "f(x) = x² − 1", W / 2, 730, ep(t, C["12.d"] + 1.6, 0.4), 52)


# ======================================================================
# bloco f — sempre confira
# ======================================================================

def b_confira(c, t, C, B):
    head(c, t, B["start"], "SEMPRE CONFIRA", "MONTE A COMPOSTA DE NOVO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    if aa > 0:
        text(c, "achou a função? ponha de volta na composta", W / 2, 260, 32, "black", INK2, aa)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        K.expr(c, "f(4x-3) = 8x - 6 + 5 = 8x - 1", W / 2, 370, 50, ab, cores={0: COL_OUT, 9: GREEN, 10: GREEN,
                                                                                11: GREEN})
        selo(c, 1620, 370, ep(t, C["13.b"] + 2.6, 0.4), "CONFERE", GREEN, -5, 30)
    acc = ep(t, C["13.c"], 0.5)
    K.atalho(c, 360, 470, 1200, 120, "ATALHO", ["teste com x = 1"], acc, 32)
    if acc > 0:
        linha(c, [("g(1) = 1", COL_IN), ("     f(1) = 7", COL_OUT), ("     8 · 1 − 1 = 7", GREEN)], W / 2, 690, 42,
              ep(t, C["13.c"] + 1.4, 0.4))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("14", "SUA VEZ", "PAUSE E TENTE", GREEN), ("15", "VAMOS JUNTOS", "A PONTE SÃO AS PÁGINAS", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    if aa > 0:
        K.expr(c, "p(t) = 50t", 560, 260, 46, aa, cores={0: COL_IN})
        text(c, "páginas em t minutos", 560, 320, 24, "bold", GRAY, aa)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        K.expr(c, "C(p) = 20 + 0,1p", 1360, 260, 46, ab, cores={0: COL_OUT})
        text(c, "reais por p páginas", 1360, 320, 24, "bold", GRAY, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0 and t < C["15"]:
        K.expr(c, "C(p(t)) = ?", 700, 440, 50, acc)
        linha(c, [("10 min = ", INK), ("R$ ?", AMBER)], 1260, 440, 50, acc)
    pause_timer(c, t, C["14.end"] - 1.9, W / 2, 600)
    if t < C["15"]:
        return
    a1 = ep(t, C["15.a"], 0.4)
    if a1 > 0:
        K.expr(c, "C = 20 + 0,1 · (50t)", W / 2, 420, 50, a1, cores={4: COL_IN, 5: COL_IN})
    a2 = ep(t, C["15.b"], 0.4)
    if a2 > 0:
        K.expr(c, "C(p(t)) = 20 + 5t", W / 2, 520, 56, a2, cores={0: GREEN})
    a3 = ep(t, C["15.c"], 0.4)
    if a3 > 0:
        linha(c, [("10 min:  ", GRAY), ("20 + 50 = ", INK), ("R$ 70,00", GREEN)], 560, 640, 40, a3)
    a4 = ep(t, C["15.d"], 0.4)
    if a4 > 0:
        linha(c, [("500 páginas:  ", GRAY), ("20 + 50 = ", INK), ("R$ 70,00", GREEN)], 1360, 640, 40, a4)
        selo(c, W / 2, 745, ep(t, C["15.d"] + 2.4, 0.4), "OS DOIS CAMINHOS BATEM", GREEN, -3, 30)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["A grandeza que aparece nas duas fórmulas é a ponte.",
          "Substitua a ponte e ela some da resposta.",
          "Achou a função escondida? Monte a composta de novo e confira."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["16", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "16" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Compor na ordem errada: o custo dentro das páginas", "qualquer encaixe das duas fórmulas dá uma fórmula",
          "a de dentro recebe o que você TEM (o tempo): 50 · (20 + 0,1t) = 1 000 + 5t está errado"),
         ("Somar os coeficientes: 50 + 0,1", "são dois números “por unidade”, lado a lado",
          "um encaixa no outro: 0,1 R$/página × 50 páginas/min = 5 R$/min"),
         ("Esquecer o custo fixo: só 5t", "a atenção toda vai para o termo do t",
          "os R$ 20 continuam lá: 10 min custam R$ 70, não R$ 50"),
         ("Parar em 2g(x) = 8x − 6, ou passar o +5 sem trocar o sinal", "a caixa já está quase sozinha",
          "divida tudo por 2 e confira: f(4x + 2) = 8x + 9, não 8x − 1")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["17", "18", "19", "20"], ERROS)


# ======================================================================
# questões
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


def _painel(c, y0, a):
    rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", a, shadow=True)


ALTS1 = [("A", "20 000 + 120t", "ordem errada: n(C(t))", RED), ("B", "500 + 43t", "somou 40 + 3", RED),
         ("C", "500 + 120t", "", GREEN), ("D", "500 + 3t", "t no lugar das peças", RED),
         ("E", "120t", "esqueceu o fixo", RED)]


def b_q1(c, t, C, B):
    head_seq(c, t, C, [("21", "QUESTÃO 1 · EU FAÇO", "CUSTO EM FUNÇÃO DO TEMPO", BLUE),
                       ("22", "RESOLVENDO", "A PONTE SÃO AS PEÇAS", BLUE), ("23", "AS ERRADAS", "CADA UMA, UM ERRO", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [("Uma pequena fábrica produz n(t) = 40t peças em t horas de funcionamento. O custo de "
                           "produção, em reais, de n peças é C(n) = 500 + 3n. O custo de produção, em reais, em função "
                           "do tempo t de funcionamento é dado por", INK)], a0, 240, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 40, C["22.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["21.end"] - 1.9, 540, yend + 130)
    if C["22"] <= t < C["23"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["22"], 0.4))
        pill(c, "tenho: TEMPO → ponte: PEÇAS → quero: CUSTO", 540, y0 + 46, COL_PONTE, size=20,
             a=ep(t, C["22"], 0.4), anchor="center")
        K.expr(c, "C = 500 + 3 · (40t)", 540, y0 + 130, 38, ep(t, C["22.a"], 0.4), cores={4: COL_IN, 5: COL_IN})
        K.expr(c, "= 500 + 120t", 540, y0 + 210, 40, ep(t, C["22.b"], 0.4), cores={3: GREEN})
        acc = ep(t, C["22.c"], 0.4)
        if acc > 0:
            text(c, "2 h:  80 peças  →  500 + 240 = 740", 540, y0 + 290, 26, "black", INK, acc)
            text(c, "fórmula:  500 + 120 · 2 = 740", 540, y0 + 335, 26, "black", GREEN, ep(t, C["22.c"] + 3.0, 0.4))
    if t >= C["23"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["23"], 0.4))
        axa = ep(t, C["23.xa"], 0.4)
        if axa > 0:
            text(c, "a ordem errada:", 540, y0 + 60, 26, "black", RED, axa)
            linha(c, [("40 · (500 + 3t)", RED), (" = 20 000 + 120t", INK)], 540, y0 + 130, 30, axa)


ALTS4 = [("A", "g(x) = 18x + 19", "aplicou f na composta", RED), ("B", "g(x) = 6x + 9", "não dividiu por 3", RED),
         ("C", "g(x) = 2x + 5/3", "−2 sem trocar o sinal", RED), ("D", "g(x) = 2x − 3", "sinal do 9 errado", RED),
         ("E", "g(x) = 2x + 3", "", GREEN)]


def b_q4(c, t, C, B):
    head_seq(c, t, C, [("24", "QUESTÃO 4 · VOCÊ FAZ", "A FUNÇÃO DE DENTRO", GREEN), ("25", "CONFERINDO", "ABRA A CAIXA", BLUE),
                       ("26", "AS ERRADAS", "CADA UMA, UM ERRO", AMBER)])
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Sejam f e g funções afins, dos reais nos reais, com f(x) = 3x − 2 e f(g(x)) = 6x + 7 para todo x real. "
                           "A lei de g é", INK)], a0, 240, 28)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS4, 1000, 250, 680, 38, C["25.ok"], "E", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 150)
    if t >= C["25"]:
        y0 = yend + 4
        _painel(c, y0, ep(t, C["25"], 0.4))
        aa = ep(t, C["25.a"], 0.4)
        if aa > 0:
            fmid(c, "3 ·", 290, y0 + 90, 40, "black", INK, aa)
            caixa_q(c, 420, y0 + 90, aa, ep(t, C["25.c"], 0.6), "2x + 3", 170, 86)
            K.expr(c, "- 2 = 6x + 7", 690, y0 + 90, 36, aa * (1 - ep(t, C["25.b"], 0.4)))
            K.expr(c, "= 6x + 9", 690, y0 + 90, 36, ep(t, C["25.b"], 0.4), cores={1: AMBER, 2: AMBER, 3: AMBER})
        ab = ep(t, C["25.b"], 0.4)
        if ab > 0:
            pill(c, "−2 passa trocando o sinal", 540, y0 + 190, AMBER, size=22, a=ab * (1 - ep(t, C["25.c"], 0.4)),
                 anchor="center")
        acc = ep(t, C["25.c"], 0.4)
        if acc > 0:
            pill(c, "divida tudo por 3", 540, y0 + 190, GREEN, size=24, a=acc, anchor="center")
        ad = ep(t, C["25.d"], 0.4)
        if ad > 0:
            K.expr(c, "f(2x+3) = 6x + 9 - 2 = 6x + 7", 540, y0 + 290, 30, ad, cores={0: COL_OUT})
            selo(c, 540, y0 + 380, ep(t, C["25.d"] + 2.4, 0.4), "CONFERE", GREEN, -4, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A FUNÇÃO QUE DESFAZ", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        rrect(c, 360, 280, 1200, 130, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("TÁXI:  ", GRAY), ("4,5 + 2,5x", PURPLE), ("  reais  (x em km)", GRAY)], W / 2, 345, 50, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        linha(c, [("tenho ", GRAY), ("R$ 37,00", GREEN), ("  →  quantos km?", AMBER)], W / 2, 500, 46, ab)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        rrect(c, 520, 580, 880, 100, 24, mix("#FFFFFF", AMBER, 0.16), acc)
        text_mid(c, "uma fórmula para QUALQUER valor?", W / 2, 630, 40, "black", AMBER, acc)
    pill(c, "ep. 3 · função inversa", W / 2, 790, PURPLE, size=30, a=ep(t, C["28.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Que duas grandezas se ligam por uma terceira?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, estrategia=b_estrategia,
              balao=b_balao, atalho=b_atalho, cadeias=b_cadeias, caso1=b_caso1, caso2=b_caso2, confira=b_confira,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, q1=b_q1, q4=b_q4, ponte=b_ponte, cta=b_cta)
