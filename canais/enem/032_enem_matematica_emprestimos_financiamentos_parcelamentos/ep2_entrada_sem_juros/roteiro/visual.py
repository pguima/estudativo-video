"""Visual — Empréstimos, Financiamentos e Parcelamentos, Episódio 2: entrada mais uma parcela e o falso "sem juros" (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, mdraw...).
Peças deste episódio: eixo() (a LINHA DO TEMPO com HOJE e 30 DIAS), nota() (bloco de dinheiro com valor),
viagem() (o pedaço financiado sai de HOJE, viaja em arco até 30 DIAS e volta maior, com o "+juros" destacado),
etiqueta_parte() (a etiqueta da geladeira que se parte em duas), anuncio() (o cartaz "10× SEM JUROS" com a letra
pequena do à vista), fracao_card() (fração com resultado, vermelha ou verde), linha(), caixa(), conferido().
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
_s = importlib.util.spec_from_file_location("comum032", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                         K.pause_timer)

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_emprestimos_ep2_entrada_sem_juros.mp4"
CARD_R = K.CARD_R


# ======================================================================
# peças do episódio
# ======================================================================

def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha, com cor por trecho: partes = [(texto, cor)] (mantém espaços)"""
    if a <= 0:
        return 0
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else cx
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_
    return sum(ws)


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    text(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def caixa(c, cx, cy, tit, val, col, a, w=360, sub=None, h=140):
    """cartão de valor: título pequeno em cima, valor grande embaixo"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    rrect(c, cx - w / 2, cy - h / 2, w, 46, 22, col, a * 0.16)
    text(c, tit, cx, cy - h / 2 + 33, 24, "black", col, a)
    size = 44
    while text_w(val, "black", size) > w - 30:
        size -= 2
    text_mid(c, val, cx, cy + 22, size, "black", INK, a)
    if sub:
        text(c, sub, cx, cy + h / 2 + 34, 24, "bold", GRAY, a)


def nota(c, cx, cy, val, col, a, w=250, h=96, rot=None):
    """bloco de dinheiro: cédula estilizada com o valor"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 16, mix("#FFFFFF", col, 0.16), a, shadow=True)
    rrect(c, cx - w / 2 + 8, cy - h / 2 + 8, w - 16, h - 16, 12, mix("#FFFFFF", col, 0.16), a, stroke=3,
          stroke_color=col)
    size = 40
    while text_w(val, "black", size) > w - 40:
        size -= 2
    text_mid(c, val, cx, cy, size, "black", col, a)
    if rot:
        text(c, rot, cx, cy + h / 2 + 34, 24, "bold", GRAY, a)


def eixo(c, x0, x1, y, a, r0="HOJE", r1="30 DIAS"):
    """a LINHA DO TEMPO: duas datas"""
    if a <= 0:
        return
    line(c, x0 - 60, y, x1 + 80, y, INK2, a, 5)
    arrow(c, x1 + 40, y, x1 + 90, y, INK2, a, 5, 18)
    for x, r in ((x0, r0), (x1, r1)):
        line(c, x, y - 20, x, y + 20, INK2, a, 5)
        text(c, r, x, y + 64, 28, "black", INK2, a)


def viagem(c, t0, t, x0, x1, y, v0, v1, juros, a, sobe=170, dur=2.4):
    """o pedaço financiado viaja em arco de HOJE até 30 DIAS e chega maior (v0 → v1), com o '+juros' em destaque"""
    if a <= 0:
        return
    u = ease_io(clamp((t - t0) / dur)) if t >= t0 else 0.0
    if u <= 0:
        nota(c, x0, y, v0, AMBER, a)
        return
    pts = 40
    path = skia.Path()
    for k in range(pts + 1):
        s_ = u * k / pts
        xx = x0 + (x1 - x0) * s_
        yy = y - 70 - sobe * math.sin(math.pi * s_)
        path.moveTo(xx, yy) if k == 0 else path.lineTo(xx, yy)
    c.drawPath(path, paint(AMBER, a * 0.7, stroke=5, cap_round=True))
    xx = x0 + (x1 - x0) * u
    yy = y - sobe * math.sin(math.pi * u) * (1 if u < 1 else 0)
    chegou = u >= 0.999
    nota(c, xx, yy, v1 if chegou else v0, PURPLE if chegou else AMBER, a)
    if chegou and juros:
        aj = ep(t, t0 + dur, 0.4)
        pill(c, juros, x1, y - 110, RED, size=30, a=a * aj, anchor="center", bounds=(0, 1920))


def etiqueta_parte(c, cx, cy, a, parte=0.0, avista="R$ 1.900,00", prazo="2 × R$ 1.000,00", w=640, h=230):
    """a etiqueta da geladeira; com parte > 0 ela se divide em duas metades (entrada | 2ª parcela)"""
    if a <= 0:
        return
    if parte <= 0:
        rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#FFF7E0", a, shadow=True, stroke=4, stroke_color=AMBER)
        text(c, "GELADEIRA", cx, cy - h / 2 + 50, 28, "black", GRAY, a)
        text_mid(c, avista + " à vista", cx, cy, 44, "black", INK, a)
        text_mid(c, "ou " + prazo, cx, cy + 62, 36, "black", AMBER, a)
        return
    u = ease_io(clamp(parte))
    gap = 140 * u
    for k, (s1, s2, col) in enumerate((("ENTRADA", "R$ 1.000,00", BLUE), ("2ª PARCELA", "R$ 1.000,00", AMBER))):
        x = cx - w / 2 + k * w / 2 + (-gap if k == 0 else gap) / 2
        rrect(c, x, cy - h / 2, w / 2 - 8, h, 22, "#FFF7E0", a, shadow=True, stroke=4, stroke_color=col)
        text(c, s1, x + w / 4, cy - 30, 26, "black", col, a)
        text_mid(c, s2, x + w / 4, cy + 30, 40, "black", INK, a)


def anuncio(c, cx, cy, a, w=620, h=360, letra=1.0, carimbo=0.0):
    """o cartaz '10× SEM JUROS' com a letra pequena do à vista"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, RED, a, shadow=True)
    text(c, "10×", cx, cy - 40, 120, "black", "#FFFFFF", a)
    text(c, "SEM JUROS!", cx, cy + 50, 64, "black", "#FFE680", a)
    text(c, "R$ 100,00 por mês", cx, cy + 100, 30, "bold", "#FFFFFF", a)
    if letra > 0:
        text(c, "ou R$ 900,00 à vista", cx + w / 2 - 24, cy + h / 2 - 22, 22, "bold", "#FFFFFF", a * letra,
             align="right")
    if carimbo > 0:
        selo(c, cx + 40, cy - 10, a * carimbo, "PREÇO COM FANTASIA", AMBER, -10, 40)


def fracao_card(c, cx, cy, num, den, res, ok, a, rot="", w=400, h=300):
    if a <= 0:
        return
    col = GREEN if ok else RED
    rrect(c, cx - w / 2, cy - h / 2, w, h, 24, mix("#FFFFFF", col, 0.10), a, shadow=True)
    K.mdraw(c, f"{num}/{den}", cx, cy - 40, 60, col, a, align="center")
    text_mid(c, res, cx, cy + 80, 50, "black", col, a)
    if rot:
        text(c, rot, cx, cy + h / 2 + 40, 26, "bold", GRAY, a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "ENTRADA + 1 PARCELA", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    etiqueta_parte(c, 520, 420, aa, w=620)
    if aa > 0:
        rrect(c, 1010, 290, 700, 160, 26, "#FFFFFF", aa, shadow=True)
        linha(c, [("R$ 100 ÷ R$ 1.900 ≈ ", INK), ("5%", AMBER), (" ?", INK)], 1360, 370, 46, aa)
        text(c, "parece pouco...", 1360, 520, 32, "bold", GRAY, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        strike(c, 1050, 370, 1670, 370, ab, RED, ab)
        rrect(c, 230, 620, 620, 140, 22, mix("#FFFFFF", AMBER, 0.12), ab, shadow=True)
        text(c, "adiou só R$ 900,00", 540, 680, 40, "black", AMBER, ab)
        text(c, "por 1 mês", 540, 730, 32, "bold", INK2, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1010, 580, 700, 220, 26, mix("#FFFFFF", RED, 0.08), acc, shadow=True)
        K.mdraw(c, "100/900", 1180, 690, 64, RED, acc, align="center")
        text_mid(c, "≈ 11,1%", 1470, 670, 70, "black", RED, acc)
        text(c, "ao mês", 1470, 750, 32, "black", RED, acc)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    itens = [("02.a", "achar a taxa escondida em entrada + 1 parcela", GREEN),
             ("02.b", "desmascarar o \"sem juros\"", AMBER)]
    for k, (cue, s, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 330 + k * 220 + d
        rrect(c, 260, y, 1400, 160, 24, mix("#FFFFFF", col, 0.08), a, shadow=True)
        check_icon(c, 340, y + 80, 30, a, col)
        text_mid(c, s, 400, y + 80, 44, "black", INK, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "3 LEMBRETES", "RÁPIDOS", GREEN)
    cards = [("03.a", "PORCENTAGEM", "que % é a parte?", "parte/base", None),
             ("03.b", "EPISÓDIO 1", "a linha do tempo", None, "eixo"),
             ("03.c", "JUROS COMPOSTOS", "1 parcela, 1 período:", None, "igual")]
    for k, (cue, tag, s, fr, kind) in enumerate(cards):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 190 + k * 520
        rrect(c, x, 280 + d, 480, 460, 24, "#FFFFFF", a, shadow=True)
        pill(c, tag, x + 240, 330 + d, GREEN, size=24, a=a, anchor="center", bounds=(0, 1920))
        text(c, s, x + 240, 430 + d, 32, "black", INK2, a)
        if fr:
            K.mdraw(c, fr, x + 240, 570 + d, 64, PURPLE, a, align="center")
        elif kind == "eixo":
            eixo(c, x + 110, x + 330, 560 + d, a, "HOJE", "1 MÊS")
            nota(c, x + 110, 490 + d, "R$", BLUE, a, w=90, h=60)
            nota(c, x + 330, 490 + d, "R$", AMBER, a, w=90, h=60)
        else:
            text(c, "simples = compostos", x + 240, 540 + d, 36, "black", PURPLE, a)
            text(c, "(1 + i)¹ = 1 + i", x + 240, 610 + d, 32, "bold", INK2, a)


def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "O CARTAZ DA LOJA", "À VISTA OU 2 VEZES", BLUE),
                       ("05", "O OUTRO ANÚNCIO", "SERÁ SEM JUROS?", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        etiqueta_parte(c, 560, 420, ep(t, C["04.a"], 0.5), w=680)
        if ep(t, C["04.a"] + 2.6, 0.4) > 0:
            pill(c, "1ª no ato · 2ª em 30 dias", 560, 590, AMBER, size=30, a=ep(t, C["04.a"] + 2.6, 0.4),
                 anchor="center", bounds=(0, 1920))
        defs = [("04.b", "PREÇO À VISTA", "quitar tudo hoje"), ("04.c", "ENTRADA", "a parte paga no ato da compra")]
        for k, (cue, nome, sig) in enumerate(defs):
            a, d = rise(t, C[cue])
            if a <= 0:
                continue
            y = 300 + k * 200 + d
            rrect(c, 1000, y, 700, 160, 22, mix("#FFFFFF", BLUE, 0.06), a)
            text(c, nome, 1040, y + 66, 40, "black", BLUE, a, align="left")
            text(c, sig, 1040, y + 120, 30, "bold", INK2, a, align="left")
        return
    anuncio(c, 700, 470, ep(t, C["05.a"], 0.5), letra=ep(t, C["05.b"], 0.5))
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        arrow(c, 1400, 700, 1040, 640, AMBER, ab, 5, 20)
        text(c, "letra pequenininha", 1440, 730, 30, "black", AMBER, ab, align="left")
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        text_mid(c, "SEM JUROS?", 1440, 400, 64, "black", AMBER, acc)


# ======================================================================
# bloco a — o método em três linhas
# ======================================================================

def b_metodo(c, t, C, B):
    head(c, t, B["start"], "O MÉTODO", "EM TRÊS LINHAS", PURPLE)
    card(c, *CARD_R)
    itens = [("06.a", "A ENTRADA NÃO VIAJA", "paga hoje · não é emprestada · não paga aluguel", BLUE),
             ("06.b", "VALOR FINANCIADO", "o que a loja te empresta: só o que faltou pagar", BLUE),
             ("06.c", "TAXA EMBUTIDA", "a taxa que ninguém anuncia", PURPLE)]
    for k, (cue, nome, sig, col) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 220 + k * 200 + d
        badge_num(c, k + 1, 230, y + 70, a, 30, bg=col)
        rrect(c, 290, y, 1380, 150, 22, mix("#FFFFFF", col, 0.06), a)
        text(c, nome, 330, y + 62, 38, "black", col, a, align="left")
        text(c, sig, 330, y + 114, 28, "bold", INK2, a, align="left")
    ab = ep(t, C["06.b"] + 3.4, 0.5)
    if ab > 0:
        pill(c, "financiado = à vista − entrada", 1640, 482 + 30, PURPLE, size=28, a=ab, anchor="right",
             bounds=(0, 1920))
    acc = ep(t, C["06.c"] + 2.4, 0.5)
    if acc > 0:
        rrect(c, 1250, 640, 400, 140, 20, "#FFFFFF", acc, shadow=True)
        K.mdraw(c, "juros/financiado", 1450, 710, 44, PURPLE, acc, align="center")


# ======================================================================
# bloco b — a geladeira (eu faço)
# ======================================================================

X0, X1, YE = 520, 1360, 640


def b_geladeira(c, t, C, B):
    head_seq(c, t, C, [("07", "EU FAÇO · A GELADEIRA", "SÓ O QUE FICOU PARA DEPOIS", BLUE),
                       ("08", "ATALHO", "O FATOR", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["07", "08"])
    if sid == "07":
        a0 = ep(t, C["07.t"], 0.4)
        sp = ep(t, C["07.a"], 1.0)
        if t < C["07.b"]:
            etiqueta_parte(c, W / 2, 480, a0, parte=sp, w=760, h=260)
            return
        eixo(c, X0, X1, YE, 1.0)
        nota(c, X0 - 200, YE - 70, "R$ 1.000", BLUE, 1.0, w=220)
        selo(c, X0 - 200, YE - 170, 1.0, "NÃO VIAJA", BLUE, -6, 28)
        ab = ep(t, C["07.b"], 0.5)
        if ab > 0:
            rrect(c, 260, 220, 1400, 110, 22, mix("#FFFFFF", PURPLE, 0.08), ab)
            linha(c, [("financiado = ", PURPLE), ("1.900 − 1.000 = ", INK), ("R$ 900", AMBER)], W / 2, 275, 46, ab)
        viagem(c, C["07.c"], t, X0 + 20, X1, YE - 70, "R$ 900", "R$ 1.000", "+ R$ 100 de juros", ab)
        ad = ep(t, C["07.d"], 0.5)
        if ad > 0:
            rrect(c, 1180, 720, 520, 110, 22, "#FFFFFF", ad, shadow=True)
            K.mdraw(c, "100/900", 1300, 775, 40, PURPLE, ad, align="center")
            text_mid(c, "≈ 11,1% ao mês", 1540, 775, 36, "black", RED, ad)
        return
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        K.atalho(c, 300, 260, 1320, 220, "ATALHO · O FATOR",
                 ["parcela ÷ financiado, e tire o 1"], aa, 44)
        linha(c, [("1.000 ÷ 900 = ", INK), ("1,111", PURPLE)], W / 2, 600, 60, aa)
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        linha(c, [("1,111 − 1 = 0,111 = ", INK2), ("11,1%", GREEN)], W / 2, 720, 50, ab)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        pill(c, "o mesmo fator da série de Porcentagem", W / 2, 810, GREEN, size=26, a=acc, anchor="center",
             bounds=(0, 1920))


# ======================================================================
# bloco c — os denominadores errados
# ======================================================================

def b_denominador(c, t, C, B):
    head(c, t, B["start"], "OS DENOMINADORES ERRADOS", "DIVIDIR PELO QUÊ?", AMBER)
    card(c, *CARD_R)
    fr = [("09.a", "100", "2.000", "5%", False, "o total a prazo"),
          ("09.a", "100", "1.900", "≈ 5,3%", False, "o preço à vista"),
          ("09.b", "100", "900", "≈ 11,1%", True, "o que foi adiado")]
    for k, (cue, n, d_, r, ok, rot) in enumerate(fr):
        off = 2.4 * k if k < 2 else 1.6
        a = ep(t, C[cue] + off, 0.5)
        fracao_card(c, 400 + k * 560, 420, n, d_, r, ok, a, rot)
        if not ok and ep(t, C["09.b"], 0.5) > 0:
            strike(c, 400 + k * 560 - 150, 420, 400 + k * 560 + 150, 420, ep(t, C["09.b"], 0.5), RED,
                   ep(t, C["09.b"], 0.5))
    acc = ep(t, C["09.c"] + 1.5, 0.5)
    if acc > 0:
        K.atalho(c, 360, 650, 1200, 160, "CONFERÊNCIA",
                 ["a taxa certa é a MAIOR: o financiado é o menor denominador"], acc, 32)


# ======================================================================
# bloco d — o "sem juros"
# ======================================================================

def b_semjuros(c, t, C, B):
    head_seq(c, t, C, [("10", "O \"SEM JUROS\"", "QUEM PAGA HOJE PAGA O PREÇO REAL", AMBER),
                       ("11", "PREÇO COM FANTASIA", "QUANDO É MESMO SEM JUROS?", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["10", "11"])
    if sid == "10":
        anuncio(c, 560, 450, ep(t, C["10.t"], 0.5), w=560, h=340)
        aa = ep(t, C["10.a"], 0.5)
        caixa(c, 1300, 300, "PARCELADO", "10 × 100 = R$ 1.000", AMBER, aa, 560)
        caixa(c, 1300, 480, "À VISTA", "R$ 900", BLUE, ep(t, C["10.a"] + 1.8, 0.5), 560)
        ab = ep(t, C["10.b"], 0.5)
        if ab > 0:
            selo(c, 1520, 420, ab, "PREÇO REAL", BLUE, -6, 30)
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            rrect(c, 1020, 620, 560, 150, 22, mix("#FFFFFF", AMBER, 0.14), acc, shadow=True)
            text(c, "JUROS EMBUTIDOS", 1300, 675, 30, "black", AMBER, acc)
            text_mid(c, "R$ 100,00", 1300, 730, 50, "black", RED, acc)
        return
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        rrect(c, 230, 230, 700, 200, 22, mix("#FFFFFF", GREEN, 0.10), aa, shadow=True)
        text(c, "à vista = total parcelado", 580, 300, 38, "black", INK, aa)
        conferido(c, "sem juros de verdade", 380, 380, aa, True, 34)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        rrect(c, 990, 230, 700, 200, 22, mix("#FFFFFF", RED, 0.08), ab, shadow=True)
        text(c, "à vista < total parcelado", 1340, 300, 38, "black", INK, ab)
        conferido(c, "a diferença são juros", 1140, 380, ab, False, 34)
        anuncio(c, 1340, 640, ab, w=440, h=240, letra=0, carimbo=ep(t, C["11.b"] + 1.6, 0.5))
    acc = ep(t, C["11.c"], 0.5)
    if acc > 0:
        rrect(c, 230, 520, 700, 260, 22, "#FFFFFF", acc, shadow=True)
        text(c, "VÁRIAS PARCELAS?", 580, 590, 34, "black", PURPLE, acc)
        text(c, "o ENEM dá um fator pronto", 580, 650, 30, "bold", INK2, acc)
        text(c, "ou pede só a comparação", 580, 695, 30, "bold", INK2, acc)
        pill(c, "série: Comparação de propostas", 580, 745, PURPLE, size=22, a=acc, anchor="center",
             bounds=(0, 1920))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("12", "SUA VEZ", "PAUSE E TENTE", GREEN), ("13", "VAMOS JUNTOS", "SEPARE A ENTRADA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if t < C["13"]:
        if aa > 0:
            caixa(c, 660, 300, "À VISTA", "R$ 1.100", BLUE, aa, 460)
            caixa(c, 1260, 300, "A PRAZO", "2 × R$ 600", AMBER, aa, 460, sub="1ª no ato · 2ª em 30 dias")
        ab = ep(t, C["12.b"], 0.5)
        if ab > 0:
            text_mid(c, "qual é a taxa mensal embutida?", W / 2, 500, 44, "black", INK, ab)
        pause_timer(c, t, C["12.end"] - 1.9, W / 2, 660)
        return
    eixo(c, 620, 1300, 600, 1.0)
    a1 = ep(t, C["13.a"], 0.5)
    nota(c, 420, 530, "R$ 600", BLUE, a1, w=200)
    if a1 > 0:
        selo(c, 420, 440, a1, "NÃO VIAJA", BLUE, -6, 24)
        linha(c, [("financiado = 1.100 − 600 = ", INK), ("R$ 500", AMBER)], W / 2, 270, 42, a1)
    ab = ep(t, C["13.b"], 0.5)
    viagem(c, C["13.b"], t, 640, 1300, 530, "R$ 500", "R$ 600", "+ R$ 100", ab, sobe=120)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 1200, 690, 500, 120, 22, "#FFFFFF", acc, shadow=True)
        K.mdraw(c, "100/500", 1320, 750, 40, PURPLE, acc, align="center")
        text_mid(c, "= 20% ao mês", 1560, 750, 38, "black", GREEN, acc)
        text(c, "(100 ÷ 1.100 seria só ≈ 9%)", 600, 770, 28, "bold", GRAY, ep(t, C["13.c"] + 2.4, 0.4))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["A entrada não é financiada: divida os juros só pelo que ficou para depois.",
          "Taxa embutida = juros ÷ valor financiado.",
          "Se existe desconto à vista, o \"sem juros\" tem juros."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["14", "20"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "14" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Calcular a taxa sobre o preço total: 100 ÷ 2.000 = 5%", "R$ 2.000 é tudo o que você paga",
          "a entrada não foi emprestada: divida só pelo financiado (100 ÷ 900 ≈ 11,1%)"),
         ("Acreditar no \"sem juros\" com desconto à vista", "está escrito no anúncio, em letra grande",
          "compare os dois preços: se o à vista é menor, a diferença é juros")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["15", "16"], ERROS)


# ======================================================================
# questão 1 (você faz)
# ======================================================================

def _enunciado(c, s, a, y0=240, size=28, w=700):
    y = y0
    for ln in K.wrap(s, "black", size, w):
        text(c, ln, 190, y, size, "black", INK, a, align="left")
        y += size + 12
    return y + 8


ALTS1 = [("A", "0%, como diz o anúncio", "acreditou", RED), ("B", "10,0%", "100 ÷ 1.000 (total)", RED),
         ("C", "11,1%", "100 ÷ 900 (à vista)", RED), ("D", "20,0%", "100 ÷ 500 (parcela)", RED),
         ("E", "25,0%", "", GREEN)]


def b_q1(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 1 · VOCÊ FAZ", "O \"SEM JUROS\" DA LOJA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["17.a"], 0.4)
    yend = _enunciado(c, "Uma loja anuncia um aparelho por \"2 × R$ 500,00 sem juros, a primeira no ato da compra e a "
                      "segunda 30 dias depois\". Para pagamento à vista, o mesmo aparelho sai por R$ 900,00. A taxa "
                      "mensal de juros efetivamente cobrada de quem escolhe o parcelamento é de", a0)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY,
         a0 * (1 - ep(t, C["18"], 0.3)), align="left")
    cues_in = {L: C[f"17.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"19.x{L.lower()}"] for L in "ABCD"}
    K.alternativas(c, t, C, ALTS1, 1000, 250, 680, 36, C["18.ok"], "E", cues_in, cues_x, gap=34)
    if t < C["18"]:
        pause_timer(c, t, C["17.end"] - 2.4, 540, 720, dur=2.1)
        return
    y0 = yend + 4
    if t < C["19.c"]:
        rrect(c, 170, y0, 740, 830 - y0, 18, "#FFFFFF", ep(t, C["18"], 0.4), shadow=True)
        linha(c, [("entrada R$ 500: ", INK2), ("não viaja", BLUE)], 540, y0 + 55, 30, ep(t, C["18.a"], 0.4))
        linha(c, [("financiado = 900 − 500 = ", INK), ("400", AMBER)], 540, y0 + 115, 32, ep(t, C["18.b"], 0.4))
        linha(c, [("juros = 500 − 400 = ", INK), ("100", RED)], 540, y0 + 170, 32, ep(t, C["18.b"] + 3.4, 0.4))
        linha(c, [("100 ÷ 400 = ", INK), ("25% ao mês", GREEN)], 540, y0 + 235, 34, ep(t, C["18.c"], 0.4))
        return
    ac = ep(t, C["19.c"], 0.4)
    rrect(c, 170, y0, 740, 830 - y0, 18, mix("#FFFFFF", AMBER, 0.12), ac, shadow=True)
    text(c, "1.000, 900 e 500: todos MAIORES", 540, y0 + 70, 30, "black", AMBER, ac)
    text(c, "que os R$ 400 emprestados", 540, y0 + 115, 30, "black", AMBER, ac)
    text(c, "11,1% e 20%: respostas dos", 540, y0 + 190, 28, "bold", INK2, ac)
    text(c, "outros exemplos, aqui armadilhas", 540, y0 + 230, 28, "bold", INK2, ac)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "SAC", PURPLE)
    aa = ep(t, C["21.a"], 0.5)
    if aa > 0:
        text(c, "dívida de R$ 10.000 em 5 parcelas", W / 2, 290, 40, "black", INK, aa)
        for k in range(6):
            v = 10000 - 2000 * k
            h = 380 * v / 10000
            a = ep(t, C["21.a"] + 0.4 * k, 0.4)
            x = 430 + k * 210
            if h > 0:
                rrect(c, x - 60, 760 - h, 120, h, 12, BLUE, a * 0.85)
            text(c, f"{v // 1000}k" if v else "0", x, 740 - h, 30, "black", BLUE, a)
            text(c, f"mês {k}", x, 800, 24, "bold", GRAY, a)
        pill(c, "− R$ 2.000 por mês", 1500, 360, BLUE, size=28, a=ep(t, C["21.a"] + 2.6, 0.4), anchor="center",
             bounds=(0, 1920))
    ab = ep(t, C["21.b"], 0.5)
    if ab > 0:
        text_mid(c, "E OS JUROS?", 1540, 520, 48, "black", AMBER, ab)
    acc = ep(t, C["21.c"], 0.5)
    if acc > 0:
        pill(c, "ep. 3 · SAC", 1540, 640, PURPLE, size=36, a=acc, anchor="center", bounds=(0, 1920))


def b_cta(c, t, C, B):
    cta(c, t, C["22.like"], C["22.sub"], C["22.bell"], C["22.com"], C["22.bye"],
        "Qual \"sem juros\" você já viu com desconto à vista?", canal="no Estudativo", anki=C["22.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, metodo=b_metodo,
              geladeira=b_geladeira, denominador=b_denominador, semjuros=b_semjuros, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q1=b_q1, ponte=b_ponte, cta=b_cta)
