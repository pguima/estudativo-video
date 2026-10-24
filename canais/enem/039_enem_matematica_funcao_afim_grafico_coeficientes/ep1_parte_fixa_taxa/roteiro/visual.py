"""Visual — Função Afim, Episódio 1: parte fixa + taxa, o que é função afim e onde você já a viu disfarçada (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: alternativas, erro_cards, atalho, selo, regra...).
Peças deste episódio: taximetro() (visor com a bandeirada acesa e o "+ a" a cada km), mola() (mola pendurada com régua:
o fixo em azul e o alongamento em roxo), fantasia() (cartão com o rótulo da série antiga e a estrutura ax + b por baixo),
linha() (texto com cor por trecho, mantém o espaço de milhar).
Cores com função: azul = b, o fixo / definição · roxo = a, a taxa / regra · âmbar = armadilha · verde = atalho · vermelho = erro.
"""
import importlib.util
from pathlib import Path
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_p = Path(__file__).resolve().parents[2] / "comum.py"
_s = importlib.util.spec_from_file_location("comum039", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
frame, head_seq, which, para, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.regra, K.selo,
                                                                K.pause_timer, K.chip)
fmid, ftext, ftext_w = K.fmid, K.ftext, K.ftext_w

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_funcao_afim_ep1_parte_fixa_taxa.mp4"
CARD_R = K.CARD_R
LCD = "#10141A"
CAIXA = "#2B2F37"


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


def lei(c, cx, cy, size, a, x="x", f="f(x)"):
    """f(x) = ax + b com a em roxo e b em azul"""
    return linha(c, [(f + " = ", INK), ("a", PURPLE), (x, INK), (" + ", INK), ("b", BLUE)], cx, cy, size, a)


def reais(v):
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + s


def taximetro(c, cx, cy, w, a, km=0.0, b_on=1.0, a_on=0.0):
    """visor de táxi: valor (5 + 2,5·km), km rodados e as luzes BANDEIRADA (azul) e + R$ 2,50 (roxo)"""
    if a <= 0:
        return
    h = w * 0.58
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, CAIXA, a, shadow=True)
    rrect(c, cx - w * 0.44, cy - h * 0.40, w * 0.88, h * 0.42, 14, LCD, a)
    text(c, "A PAGAR", cx - w * 0.40, cy - h * 0.29, w * 0.045, "black", "#9AA3B2", a, align="left")
    ftext(c, reais(5 + 2.5 * km), cx + w * 0.40, cy - h * 0.04, w * 0.12, "black", "#FFD166", a, align="right")
    ftext(c, f"{km:.0f} km", cx - w * 0.40, cy + h * 0.17, w * 0.065, "black", "#E6E6E2", a, align="left")
    # luzes
    for k, (s_, col, on) in enumerate((("BANDEIRADA", BLUE, b_on), ("+ R$ 2,50 / km", PURPLE, a_on))):
        x = cx - w * 0.42 + k * w * 0.44
        rrect(c, x, cy + h * 0.25, w * 0.40, h * 0.18, 12, mix(CAIXA, col, 0.25 + 0.75 * on), a)
        text_mid(c, s_, x + w * 0.20, cy + h * 0.34, w * 0.042, "black", "#FFFFFF", a * (0.45 + 0.55 * on))


def mola(c, x, ytop, a, comp, px=14.0, fixo=20, kg=None, regua=True, col_al=None):
    """mola pendurada no teto em (x, ytop); comp = comprimento em cm (px por cm). Régua à esquerda: 0–fixo em azul,
    fixo–comp em roxo (alongamento). kg = rótulo do peso pendurado."""
    if a <= 0:
        return
    col_al = col_al or PURPLE
    rrect(c, x - 110, ytop - 26, 220, 26, 6, "#8A909C", a)
    L = comp * px
    n = 14
    p = skia.Path()
    p.moveTo(x, ytop)
    p.lineTo(x, ytop + 14)
    for k in range(n):
        yy = ytop + 14 + (L - 28) * (k + 0.5) / n
        p.lineTo(x + (34 if k % 2 == 0 else -34), yy)
    p.lineTo(x, ytop + L - 14)
    p.lineTo(x, ytop + L)
    c.drawPath(p, paint("#5B6270", a, stroke=6))
    if kg:
        rrect(c, x - 60, ytop + L, 120, 96, 14, "#3A3F4A", a, shadow=True)
        text_mid(c, kg, x, ytop + L + 48, 34, "black", "#FFFFFF", a)
    if regua:
        rx = x - 140
        rrect(c, rx - 16, ytop, 32, fixo * px, 6, BLUE, a)
        if comp > fixo:
            rrect(c, rx - 16, ytop + fixo * px, 32, (comp - fixo) * px, 6, col_al, a)
        for cm in range(0, int(comp) + 1, 5):
            line(c, rx + 16, ytop + cm * px, rx + 30, ytop + cm * px, INK2, a, 3)
        ftext(c, f"{fixo} cm", rx - 30, ytop + fixo * px / 2 + 12, 28, "black", BLUE, a, align="right")
        if comp > fixo:
            ftext(c, f"+{comp - fixo:g} cm", rx - 30, ytop + (fixo + (comp - fixo) / 2) * px + 12, 28, "black", col_al, a,
                  align="right")


def fantasia(c, cx, cy, w, a, rotulo, lei_partes, sub, col, tira=0.0):
    """cartão de 'disfarce': rótulo da série antiga em cima; tira = 0..1 levanta o rótulo e revela a estrutura ax + b"""
    if a <= 0:
        return
    h = 300
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#FFFFFF", a, shadow=True)
    linha(c, lei_partes, cx, cy - 20, 50, a)
    text(c, sub, cx, cy + 70, 28, "bold", INK2, a)
    # o rótulo cobre a estrutura e é levantado
    yy = cy - h / 2 + 10 - tira * 120
    rrect(c, cx - w / 2 + 10, yy, w - 20, 140, 22, col, a * (1 - 0.15 * tira), shadow=True)
    text_mid(c, rotulo, cx, yy + 70, 34, "black", "#FFFFFF", a)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "FUNÇÃO AFIM · EPISÓDIO 1", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        mola(c, 360, 260, aa, 20, 13, regua=False)
        text(c, "20 cm", 360, 580, 36, "black", BLUE, aa)
        ab0 = ep(t, C["01.a"] + 2.4, 0.5)
        mola(c, 680, 260, ab0, 26, 13, kg="2 kg", regua=False)
        text(c, "26 cm", 680, 760, 36, "black", INK, ab0)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        rrect(c, 1000, 250, 680, 170, 24, mix("#FFFFFF", AMBER, 0.25), ab)
        text(c, "REGRA DE TRÊS (5 kg)", 1340, 310, 32, "black", AMBER, ab)
        linha(c, [("26 · 5 ÷ 2 = ", INK), ("65 cm", AMBER)], 1340, 375, 50, ab)
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 450, 680, 170, 24, mix("#FFFFFF", GREEN, 0.18), acc)
        text(c, "A MOLA REAL (5 kg)", 1340, 510, 32, "black", GREEN, acc)
        linha(c, [("35 cm", GREEN)], 1340, 575, 60, acc)
        strike(c, 1180, 375, 1500, 375, ep(t, C["01.c"] + 0.6, 0.4), RED, 1)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1340, 720, ad, "ERROU POR QUASE O DOBRO", RED, -4, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "FUNÇÃO AFIM · EP. 1", "AO FINAL DESTA AULA", GREEN)
    a0 = ep(t, C["02"], 0.4)
    if a0 > 0:
        pill(c, "1º episódio da série de FUNÇÃO AFIM", W / 2, 240, BLUE, size=30, a=a0, anchor="center")
    itens = [("02.a", "RECONHECER", "em qualquer texto", BLUE), ("02.b", "DAR NOME", "aos 2 números: a e b", PURPLE),
             ("02.c", "REGRA DE TRÊS", "quando vale · quando engana", AMBER)]
    for k, (cue, tit, sub, col) in enumerate(itens):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 440 + k * 520
        rrect(c, x - 230, 330, 460, 330, 26, "#FFFFFF", ak, shadow=True)
        rrect(c, x - 230, 330, 460, 70, 26, col, ak * 0.16)
        badge_num(c, k + 1, x, 470, ak, 34, bg=col)
        text(c, tit, x, 570, 40, "black", col, ak)
        text(c, sub, x, 625, 28, "bold", INK2, ak)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    itens = [("03.a", "Conceito de Função", [("entra x  →  sai ", INK), ("f(x)", PURPLE)]),
             ("03.b", "Grandezas Proporcionais", [("y = k", INK), ("x", INK), ("   reta pela origem", INK2)]),
             ("03.c", "Juros Simples", [("M = C + C · i · t", INK)])]
    for k, (cue, serie, partes) in enumerate(itens):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        y = 300 + k * 170 + d
        rrect(c, 260, y - 70, 1400, 140, 24, "#FFFFFF", a, shadow=True)
        pill(c, "série de " + serie, 300, y - 70, BLUE, size=22, a=a)
        linha(c, partes, 960, y + 10, 52, a)


def b_concreto(c, t, C, B):
    head(c, t, B["start"], "TRÊS CONTAS DO DIA A DIA", "O QUE ELAS TÊM EM COMUM?", BLUE)
    card(c, *CARD_R)
    cols = [("04.a", "TÁXI", "bandeirada", "por km"), ("04.b", "CELULAR", "mensalidade", "por minuto"),
            ("04.c", "SALÁRIO", "fixo", "comissão")]
    for k, (cue, tit, fixo, taxa) in enumerate(cols):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 450 + k * 510
        rrect(c, x - 230, 220, 460, 440, 24, "#FFFFFF", a, shadow=True)
        text(c, tit, x, 290, 44, "black", INK, a)
        rrect(c, x - 190, 340, 380, 110, 20, mix("#FFFFFF", BLUE, 0.16), a)
        text(c, "PARTE FIXA", x, 380, 22, "black", BLUE, a)
        text(c, fixo, x, 428, 36, "black", BLUE, a)
        ab = ep(t, C[cue] + 1.2, 0.4)
        rrect(c, x - 190, 480, 380, 110, 20, mix("#FFFFFF", PURPLE, 0.14), ab)
        text(c, "CRESCE NO RITMO", x, 520, 22, "black", PURPLE, ab)
        text(c, taxa, x, 568, 36, "black", PURPLE, ab)
    ad = ep(t, C["04.d"], 0.5)
    if ad > 0:
        regra(c, "PARTE FIXA + PARTE QUE CRESCE NO MESMO RITMO", W / 2, 750, ad, 38)


# ======================================================================
# bloco a — o táxi e a definição
# ======================================================================

def b_taxi(c, t, C, B):
    head(c, t, B["start"], "O TÁXI", "POR QUE COBRA ANTES DE SAIR?", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["05.a"], 0.5)
    tb = C["05.b"]
    km = clamp((t - tb - 0.6) / 3.0) * 2 if t >= tb else 0.0
    km = float(int(km))
    a_on = 1.0 if t >= tb + 0.6 and (t - tb - 0.6) % 1.5 < 0.5 and t < tb + 3.6 else 0.0
    taximetro(c, 560, 470, 640, aa, km, 1.0, a_on)
    if aa > 0:
        selo(c, 560, 760, ep(t, C["05.a"] + 1.6, 0.4), "b = R$ 5,00 · PARADO", BLUE, -4, 30)
    ab = ep(t, tb, 0.5)
    for j in range(2):
        aj = ep(t, tb + 0.9 + j * 1.5, 0.3)
        if aj <= 0:
            continue
        y = 300 + j * 110
        rrect(c, 1040, y - 42, 580, 84, 18, "#FFFFFF", aj, shadow=True)
        linha(c, [(f"{j + 1}º km:  ", INK2), ("+ R$ 2,50", PURPLE)], 1330, y, 38, aj)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        rrect(c, 1020, 560, 620, 170, 24, mix("#FFFFFF", PURPLE, 0.08), acc)
        text(c, "PREÇO", 1330, 610, 26, "black", INK2, acc)
        linha(c, [("P(d) = ", INK), ("5", BLUE), (" + ", INK), ("2,5", PURPLE), ("d", INK)], 1330, 675, 54, acc)
    if ab <= 0 and aa > 0:
        pass


def b_definicao(c, t, C, B):
    head(c, t, B["start"], "DEFINIÇÃO", "FUNÇÃO AFIM", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["06.a"], 0.5)
    if aa > 0:
        rrect(c, 560, 200, 800, 130, 26, mix("#FFFFFF", BLUE, 0.10), aa)
        lei(c, W / 2, 265, 72, aa)
    ab = ep(t, C["06.b"], 0.5)
    if ab > 0:
        rrect(c, 220, 380, 700, 300, 24, "#FFFFFF", ab, shadow=True)
        text(c, "a", 290, 470, 80, "black", PURPLE, ab)
        para(c, "COEFICIENTE ANGULAR ou TAXA DE VARIAÇÃO", 350, 435, 28, "black", PURPLE, ab, 540, 34)
        text(c, "quanto muda a cada unidade de x", 570, 540, 28, "bold", INK2, ab)
        pill(c, "táxi: R$ 2,50 POR km", 570, 620, PURPLE, size=26, a=ep(t, C["06.b"] + 2.4, 0.4), anchor="center")
    acc = ep(t, C["06.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 380, 700, 300, 24, "#FFFFFF", acc, shadow=True)
        text(c, "b", 1070, 470, 80, "black", BLUE, acc)
        para(c, "COEFICIENTE LINEAR ou VALOR INICIAL", 1130, 435, 28, "black", BLUE, acc, 540, 34)
        text(c, "quanto vale quando x = 0", 1350, 540, 28, "bold", INK2, acc)
        pill(c, "táxi: R$ 5,00 FIXOS", 1350, 620, BLUE, size=26, a=ep(t, C["06.c"] + 2.4, 0.4), anchor="center")
    ad = ep(t, C["06.d"], 0.5)
    if ad > 0:
        line(c, 780, 765, 1140, 715, PURPLE, ad, 7, progress=ep(t, C["06.d"], 1.0))
        linha(c, [("gráfico: sempre uma RETA", INK), ("  ·  ep. 3", GRAY)], 960, 805, 30, ad)


def b_nomes(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "ACHE O a E O b PELOS NOMES", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["07.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 140, "ATALHO", ["ache o a e o b pelos NOMES"], aa, 42)
    ab = ep(t, C["07.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 380, 680, 300, 24, mix("#FFFFFF", BLUE, 0.10), ab)
        text(c, "b  (o fixo)", 600, 440, 40, "black", BLUE, ab)
        for k, s_ in enumerate(("fixo", "inicial", "mensalidade", "sem carga")):
            chip(c, s_, 430 + (k % 2) * 340, 520 + (k // 2) * 90, BLUE, ep(t, C["07.b"] + 0.6 + k * 0.5, 0.3), 30)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 380, 680, 300, 24, mix("#FFFFFF", PURPLE, 0.10), acc)
        text(c, "a  (a taxa) · “POR”", 1320, 440, 40, "black", PURPLE, acc)
        for k, s_ in enumerate(("por km", "por minuto", "por kg")):
            chip(c, s_, 1320, 515 + k * 60, PURPLE, ep(t, C["07.c"] + 0.8 + k * 0.5, 0.3), 28)
    ad = ep(t, C["07.d"], 0.5)
    if ad > 0:
        linha(c, [("b = ", INK), ("R$ 40 fixos", BLUE), ("     a = ", INK), ("R$ 0,50 por minuto", PURPLE)], W / 2, 760,
              38, ad)


# ======================================================================
# bloco b — os casos particulares
# ======================================================================

CASOS = [("08.a", "AFIM GERAL", [("5", BLUE), (" + ", INK), ("2,5", PURPLE), ("d", INK)], "táxi", INK),
         ("08.b", "LINEAR (b = 0)", [("6", PURPLE), ("L", INK)], "combustível · nada fixo", PURPLE),
         ("08.c", "IDENTIDADE", [("f(x) = x", INK)], "sai o que entrou", BLUE),
         ("09.a", "CONSTANTE (a = 0)", [("99,90", BLUE)], "mensalidade fixa", AMBER)]


def b_casos(c, t, C, B):
    head_seq(c, t, C, [("08", "E SE UM DELES FOR ZERO?", "OS CASOS PARTICULARES", BLUE),
                       ("09", "E SE O a FOR ZERO?", "FUNÇÃO CONSTANTE", BLUE)])
    card(c, *CARD_R)
    for k, (cue, nome, partes, sub, col) in enumerate(CASOS):
        a, d = rise(t, C[cue])
        if a <= 0:
            continue
        x = 300 + k * 440
        y = 230 + d
        rrect(c, x - 200, y, 400, 380, 24, "#FFFFFF", a, shadow=True)
        rrect(c, x - 200, y, 400, 74, 24, col, a * 0.16)
        text(c, nome, x, y + 50, 28, "black", col, a)
        linha(c, partes, x, y + 170, 56, a)
        text(c, sub, x, y + 270, 26, "bold", INK2, a)
        # mini gráfico (só a forma)
        gx, gy = x - 80, y + 350
        line(c, gx, gy, gx + 160, gy, LIGHT, a, 3)
        line(c, gx, gy, gx, gy - 70, LIGHT, a, 3)
        if k == 0:
            line(c, gx, gy - 22, gx + 150, gy - 70, col, a, 5)
        elif k in (1, 2):
            line(c, gx, gy, gx + 150, gy - 70, col, a, 5)
        else:
            line(c, gx, gy - 40, gx + 150, gy - 40, col, a, 5)
    ab = ep(t, C["09.b"], 0.5)
    if ab > 0:
        pill(c, "usou pouco ou muito: paga o mesmo", 1620, 690, AMBER, size=24, a=ab, anchor="right", bounds=(0, 1920))
    acc = ep(t, C["09.c"], 0.5)
    if acc > 0:
        regra(c, "PARTE FIXA + PARTE PROPORCIONAL A x", W / 2, 775, acc, 38)


# ======================================================================
# blocos c e d — os disfarces
# ======================================================================

def b_disfarce(c, t, C, B):
    head_seq(c, t, C, [("10", "VOCÊ JÁ VIU ISSO", "DISFARÇADO (1)", PURPLE),
                       ("11", "VOCÊ JÁ VIU ISSO", "DISFARÇADO (2)", PURPLE)])
    card(c, *CARD_R)
    a1 = ep(t, C["10.a"], 0.5)
    tira1 = ep(t, C["10.a"] + 2.6, 0.8)
    fantasia(c, 560, 420, 720, a1, "GRANDEZAS PROPORCIONAIS",
             [("y = ", INK), ("k", PURPLE), ("x", INK), (" + ", INK), ("0", BLUE)], "a bandeirada é ZERO (b = 0)", BLUE,
             tira1)
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0 and t < C["11"]:
        rrect(c, 1040, 280, 600, 280, 24, "#FFFFFF", ab, shadow=True)
        text(c, "a reta que NÃO passa", 1340, 340, 30, "black", INK, ab)
        text(c, "pela origem?", 1340, 385, 30, "black", INK, ab)
        line(c, 1140, 520, 1540, 520, LIGHT, ab, 3); line(c, 1140, 520, 1140, 410, LIGHT, ab, 3)
        line(c, 1140, 480, 1520, 420, PURPLE, ab, 5)
        c.drawCircle(1140, 480, 9, paint(BLUE, ab))
    acc = ep(t, C["10.c"], 0.5)
    if acc > 0 and t < C["11"]:
        selo(c, 1340, 640, acc, "AFIM COM PARTE FIXA", BLUE, -4, 32)
    ad = ep(t, C["10.d"], 0.5)
    if ad > 0 and t < C["11"]:
        pill(c, "proporção direta = CASO ESPECIAL da afim", 560, 700, PURPLE, size=26, a=ad, anchor="center")
    if t < C["11"]:
        return
    a2 = ep(t, C["11.a"], 0.5)
    tira2 = ep(t, C["11.b"], 0.8)
    fantasia(c, 1340, 420, 720, a2, "JUROS SIMPLES",
             [("M(t) = ", INK), ("1 000", BLUE), (" + ", INK), ("50", PURPLE), ("t", INK)], "R$ 1.000,00 a 5% ao mês",
             GREEN, tira2)
    ab2 = ep(t, C["11.b"], 0.5)
    if ab2 > 0:
        pill(c, "b = 1 000: o CAPITAL = a bandeirada", 1340, 640, BLUE, size=24, a=ab2, anchor="center")
    ac2 = ep(t, C["11.c"], 0.5)
    if ac2 > 0:
        pill(c, "a = 50: JUROS DE CADA MÊS = o taxímetro", 1340, 700, PURPLE, size=24, a=ac2, anchor="center")
    ad2 = ep(t, C["11.d"], 0.5)
    if ad2 > 0:
        regra(c, "a mesma estrutura, com outra roupa", 960, 785, ad2, 32)


# ======================================================================
# bloco e — proporcional só quando b = 0
# ======================================================================

def b_dobro(c, t, C, B):
    head(c, t, B["start"], "DOBRAR O x DOBRA O y?", "PROPORCIONAL SÓ QUANDO b = 0", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["12.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 200, 1480, 100, 22, mix("#FFFFFF", BLUE, 0.08), aa)
        text(c, "PROPORCIONAIS: dobrou um, dobra o outro", 960, 262, 34, "black", BLUE, aa)
    a1 = ep(t, C["12.a"] + 4.5, 0.5)
    if a1 > 0:
        linha(c, [("C(m) = ", INK), ("40", BLUE), (" + ", INK), ("0,50", PURPLE), ("m", INK)], 960, 360, 50, a1)
    for k, (cue, mins, conta, res) in enumerate((("12.b", "100 min", "40 + 50", "R$ 90,00"),
                                                 ("12.c", "200 min", "40 + 100", "R$ 140,00"))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 330, 430, 660, 200, 24, "#FFFFFF", ak, shadow=True)
        text(c, mins, x, 490, 40, "black", INK, ak)
        linha(c, [(conta + " = ", INK2), (res, GREEN)], x, 570, 44, ak)
    ad = ep(t, C["12.d"], 0.5)
    if ad > 0:
        linha(c, [("2 · 90 = ", INK2), ("180", RED), ("  ≠  140", INK)], 960, 700, 46, ad)
        selo(c, 960, 790, ep(t, C["12.d"] + 2.6, 0.4), "A BANDEIRADA NÃO DOBRA", AMBER, -3, 34)


def b_zero(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "O TESTE DO ZERO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    K.atalho(c, 260, 200, 1400, 150, "ATALHO · REGRA DE TRÊS VALE?", ["com x = 0, o resultado dá ZERO?"], aa, 42)
    ab = ep(t, C["13.b"], 0.5)
    if ab > 0:
        rrect(c, 260, 400, 680, 260, 24, mix("#FFFFFF", GREEN, 0.12), ab)
        text(c, "COMBUSTÍVEL", 600, 455, 32, "black", INK, ab)
        linha(c, [("0 L  →  ", INK2), ("R$ 0", GREEN)], 600, 535, 48, ab)
        selo(c, 600, 615, ep(t, C["13.b"] + 2.5, 0.4), "PODE REGRA DE TRÊS", GREEN, -3, 26)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        rrect(c, 980, 400, 680, 260, 24, mix("#FFFFFF", RED, 0.08), acc)
        text(c, "CELULAR", 1320, 455, 32, "black", INK, acc)
        linha(c, [("0 min  →  ", INK2), ("R$ 40", BLUE)], 1320, 535, 48, acc)
        selo(c, 1320, 615, ep(t, C["13.c"] + 2.0, 0.4), "NÃO PODE", RED, -3, 26)
    ad = ep(t, C["13.d"], 0.5)
    if ad > 0:
        pill(c, "10 segundos de teste", W / 2, 750, GREEN, size=30, a=ad, anchor="center")


# ======================================================================
# bloco f — a mola
# ======================================================================

def b_mola(c, t, C, B):
    head(c, t, B["start"], "A MOLA DO COMEÇO", "O QUE É PROPORCIONAL?", PURPLE)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    t_b, t_d = C["14.b"], C["14.d"]
    comp = 20 + 6 * ep(t, t_b, 1.0) + 9 * ep(t, t_d, 1.4)
    kg = "5 kg" if t >= t_d else ("2 kg" if t >= t_b else None)
    mola(c, 560, 230, aa, comp, 13, kg=kg)
    if aa > 0:
        pill(c, "sem carga: o FIXO", 680, 300, BLUE, size=24, a=aa)
    ab = ep(t, t_b, 0.5)
    if ab > 0:
        rrect(c, 1000, 230, 660, 150, 22, "#FFFFFF", ab, shadow=True)
        text(c, "ALONGAMENTO", 1330, 280, 30, "black", PURPLE, ab)
        text(c, "quanto esticou além do tamanho dela", 1330, 335, 26, "bold", INK2, ab)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        rrect(c, 1000, 410, 660, 120, 22, mix("#FFFFFF", PURPLE, 0.10), acc)
        linha(c, [("6 cm ÷ 2 kg = ", INK), ("3 cm por kg", PURPLE)], 1330, 470, 40, acc)
    ad = ep(t, t_d, 0.5)
    if ad > 0:
        rrect(c, 1000, 560, 660, 200, 22, "#FFFFFF", ad, shadow=True)
        linha(c, [("5 kg · 3 = ", INK), ("15 cm", PURPLE)], 1330, 615, 40, ad)
        linha(c, [("20", BLUE), (" + ", INK), ("15", PURPLE), (" = ", INK), ("35 cm", GREEN)], 1330, 700, 52,
              ep(t, t_d + 2.4, 0.4))


def b_tirefixo(c, t, C, B):
    head(c, t, B["start"], "ATALHO", "A RECEITA DA PARTE FIXA", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["15.a"], 0.5)
    passos = [("1", "TIRE O FIXO", "26 − 20 = 6 cm", BLUE), ("2", "PROPORÇÃO NO RESTO", "6 cm → 2 kg · 15 cm → 5 kg", PURPLE),
              ("3", "DEVOLVA O FIXO", "20 + 15 = 35 cm", GREEN)]
    for k, (n_, tit, ex, col) in enumerate(passos):
        ak = aa * ep(t, C["15.a"] + 0.4 + k * 1.1, 0.4)
        if ak <= 0:
            continue
        x = 450 + k * 510
        K.boxed(c, x - 230, 230, 460, 300, GREEN, ak, 0.08)
        badge_num(c, n_, x, 300, ak, 34, bg=col)
        text(c, tit, x, 400, 34, "black", INK, ak)
        text(c, ex, x, 470, 26, "bold", INK2, ak)
        if k < 2:
            arrow(c, x + 240, 380, x + 270, 380, GREEN, ak, 5, 14)
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        pill(c, "regra de três SÓ na parte que cresce", W / 2, 620, PURPLE, size=30, a=ab, anchor="center")
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 740, acc, "A REGRA DE TRÊS QUE O ENEM QUER", GREEN, -3, 34)


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E TENTE", GREEN), ("17", "VAMOS JUNTOS", "O FIXO NÃO DOBRA", GREEN)])
    card(c, *CARD_R)
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        rrect(c, 220, 200, 1480, 110, 22, "#FFFFFF", aa, shadow=True)
        linha(c, [("S(v) = ", INK), ("1 500", BLUE), (" + ", INK), ("0,04", PURPLE), ("v", INK)], 960, 255, 54, aa)
        pill(c, "R$ fixos", 640, 330, BLUE, size=22, a=ep(t, C["16.a"] + 1.4, 0.4), anchor="center")
        pill(c, "4% das vendas", 1150, 330, PURPLE, size=22, a=ep(t, C["16.a"] + 2.4, 0.4), anchor="center")
    for k, (cue, venda) in enumerate((("16.b", "R$ 10.000,00"), ("16.c", "R$ 20.000,00"))):
        ak = ep(t, C[cue], 0.5)
        if ak <= 0:
            continue
        x = 560 + k * 800
        rrect(c, x - 330, 400, 660, 320, 24, "#FFFFFF", ak, shadow=True)
        text(c, "vendas: " + venda, x, 460, 36, "black", INK, ak)
        if t < C["17"]:
            text_mid(c, "S = ?" if k == 0 else "o DOBRO?", x, 580, 56, "black", AMBER, ak)
    if t < C["17"]:
        pause_timer(c, t, C["16.end"] - 1.9, 960, 790)
        return
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        linha(c, [("0,04 · 10 000 = ", INK2), ("400", PURPLE)], 560, 545, 38, ab)
        linha(c, [("1 500", BLUE), (" + ", INK), ("400", PURPLE), (" = ", INK), ("1 900", GREEN)], 560, 630, 46,
              ep(t, C["17.b"] + 2.4, 0.4))
    acc = ep(t, C["17.c"], 0.5)
    if acc > 0:
        linha(c, [("0,04 · 20 000 = ", INK2), ("800", PURPLE)], 1360, 545, 38, acc)
        linha(c, [("1 500", BLUE), (" + ", INK), ("800", PURPLE), (" = ", INK), ("2 300", GREEN)], 1360, 630, 46,
              ep(t, C["17.c"] + 1.8, 0.4))
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        linha(c, [("o dobro seria ", INK2), ("3 800", RED), ("  →  NÃO DOBROU", INK)], 960, 790, 38, ad)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["a é quanto muda por unidade; b é quanto vale no início.",
          "Proporcional é o caso especial com b = 0.",
          "Com parte fixa, dobrar o x não dobra o y."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "27"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Regra de três com parte fixa: táxi 10 km = R$ 30, logo 20 km = R$ 60", "mais km é mais dinheiro, e isso lembra proporção",
          "a bandeirada não dobra: 5 + 2,5 · 20 = R$ 55,00"),
         ("Proporção com o comprimento TOTAL: 26 cm para 2 kg, logo 65 cm para 5 kg", "o enunciado só mostra o comprimento",
          "proporcional é o ALONGAMENTO: tire os 20, faça a proporção, devolva os 20")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20"], ERROS)


# ======================================================================
# questões do material
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


ALTS2 = [("A", "R$ 100,00.", "esqueceu a mensalidade", RED), ("B", "R$ 130,00.", "90 + 40: mensalidade de novo", RED),
         ("C", "R$ 140,00.", "", GREEN), ("D", "R$ 180,00.", "regra de três: 2 · 90", RED),
         ("E", "R$ 220,00.", "2 · 90 + 40", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 2 · EU FAÇO", "DOBRAR O CONSUMO NÃO DOBRA A CONTA", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["21.a"], 0.4)
    yend = _enunciado(c, [("Um plano de celular cobra uma mensalidade fixa mais um valor constante por minuto de ligação. "
                           "Em um mês com 100 minutos, a conta foi de R$ 90,00; a mensalidade fixa é de R$ 40,00. "
                           "Em um mês com 200 minutos, a conta será de", INK)], a0, 236, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["22"], 0.3)),
         align="left")
    cues_in = {L: C[f"21.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"23.x{L.lower()}"] for L in "ABDE"}
    K.alternativas(c, t, C, ALTS2, 1000, 260, 680, 38, C["22.ok"], "C", cues_in, cues_x, gap=34)
    pause_timer(c, t, C["21.end"] - 1.9, 540, yend + 120)
    if t >= C["22"]:
        y0 = 236 - 30
        _painel(c, y0, ep(t, C["22"], 0.4))
        aa = ep(t, C["22.a"], 0.4)
        if aa > 0:
            linha(c, [("b = ", INK), ("R$ 40", BLUE), (" (fixa)", INK2)], 540, y0 + 60, 34, aa)
            linha(c, [("a = ", INK), ("?", PURPLE), (" (por minuto)", INK2)], 540, y0 + 115, 34, ep(t, C["22.a"] + 2.2, 0.4))
        ab = ep(t, C["22.b"], 0.4)
        if ab > 0:
            linha(c, [("90 − 40 = ", INK2), ("50", INK), (" em 100 min", INK2)], 540, y0 + 195, 32, ab)
            linha(c, [("a = 50 ÷ 100 = ", INK), ("R$ 0,50/min", PURPLE)], 540, y0 + 250, 32, ep(t, C["22.b"] + 2.0, 0.4))
        acc = ep(t, C["22.c"], 0.4)
        if acc > 0:
            linha(c, [("C(200) = ", INK), ("40", BLUE), (" + ", INK), ("0,5", PURPLE), (" · 200", INK)], 540, y0 + 340, 34, acc)
            linha(c, [("= 40 + 100 = ", INK), ("R$ 140", GREEN)], 540, y0 + 400, 38, ep(t, C["22.c"] + 2.4, 0.4))
        ad = ep(t, C["22.d"], 0.4)
        if ad > 0:
            check_icon(c, 250, y0 + 480, 20, ad, GREEN)
            linha(c, [("C(100) = 40 + 50 = 90 · bate", GREEN)], 290, y0 + 482, 28, ad, align="left")


ALTS9 = [("A", "cerca de 2,5 kg.", "regra de três com o total", RED), ("B", "4 kg.", "", GREEN),
         ("C", "6 kg.", "12 ÷ 2: massa como taxa", RED), ("D", "cerca de 10,7 kg.", "32 ÷ 3: esqueceu os 20", RED),
         ("E", "16 kg.", "32 ÷ 2", RED)]


def b_q9(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO 9 · VOCÊ FAZ", "A MOLA QUE ALONGA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["24.a"], 0.4)
    yend = _enunciado(c, [("Uma mola tem 20 cm de comprimento sem carga. Pendurando-se nela um objeto de 2 kg, seu "
                           "comprimento passa a 26 cm. Admitindo que o alongamento seja proporcional à massa pendurada, "
                           "a massa que deixa a mola com 32 cm de comprimento é", INK)], a0, 236, 27)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0 * (1 - ep(t, C["25"], 0.3)),
         align="left")
    cues_in = {L: C[f"24.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"26.x{L.lower()}"] for L in "ACDE"}
    K.alternativas(c, t, C, ALTS9, 1000, 260, 680, 38, C["25.ok"], "B", cues_in, cues_x, gap=34)
    if t < C["25"]:
        pause_timer(c, t, C["24.end"] - 1.9, 540, yend + 120)
        return
    y0 = 236 - 30
    _painel(c, y0, ep(t, C["25"], 0.4))
    aa = ep(t, C["25.a"], 0.4)
    if aa > 0:
        linha(c, [("b = ", INK), ("20 cm", BLUE), (" (sem carga)", INK2)], 540, y0 + 60, 32, aa)
        linha(c, [("a = 6 ÷ 2 = ", INK), ("3 cm por kg", PURPLE)], 540, y0 + 115, 32, ep(t, C["25.a"] + 2.4, 0.4))
    ab = ep(t, C["25.b"], 0.4)
    if ab > 0:
        linha(c, [("20", BLUE), (" + ", INK), ("3", PURPLE), ("m", INK), (" = 32", INK)], 540, y0 + 205, 44, ab)
    acc = ep(t, C["25.c"], 0.4)
    if acc > 0:
        linha(c, [("32 − 20 = ", INK2), ("12 cm", PURPLE)], 540, y0 + 290, 34, acc)
        linha(c, [("m = 12 ÷ 3 = ", INK), ("4 kg", GREEN)], 540, y0 + 355, 40, ep(t, C["25.c"] + 1.8, 0.4))
    ad = ep(t, C["25.d"], 0.4)
    if ad > 0:
        mola(c, 760, y0 + 420, ad, 32, 6, kg=None, regua=False)
        check_icon(c, 250, y0 + 460, 20, ad, GREEN)
        linha(c, [("20 + 12 = 32 · bate", GREEN)], 290, y0 + 462, 28, ad, align="left")


# ======================================================================
# ponte e CTA
# ======================================================================

def _vela(c, x, ybase, a, alt_cm, px=22):
    if a <= 0:
        return
    h = alt_cm * px
    rrect(c, x - 45, ybase - h, 90, h, 12, "#F6E7C8", a, shadow=True)
    c.drawRect(skia.Rect.MakeXYWH(x - 45, ybase - h, 90, h), paint("#D9C59A", a, stroke=3))
    line(c, x, ybase - h, x, ybase - h - 22, INK, a, 4)
    p = skia.Path()
    p.moveTo(x, ybase - h - 70); p.quadTo(x + 22, ybase - h - 36, x, ybase - h - 24); p.quadTo(x - 22, ybase - h - 36, x,
                                                                                                ybase - h - 70)
    c.drawPath(p, paint("#FFB020", a))
    text(c, f"{alt_cm} cm", x, ybase + 50, 34, "black", INK, a)


def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A TAXA QUE O ENUNCIADO NÃO DÁ", PURPLE)
    aa = ep(t, C["28.a"], 0.5)
    if aa > 0:
        linha(c, [("a = ", PURPLE), ("?", AMBER)], 1340, 300, 90, aa)
    ab = ep(t, C["28.b"], 0.5)
    if ab > 0:
        _vela(c, 420, 720, ab, 17)
        text(c, "aos 10 min", 420, 820, 28, "bold", INK2, ab)
        ab2 = ep(t, C["28.b"] + 2.0, 0.5)
        _vela(c, 760, 720, ab2, 13)
        text(c, "aos 30 min", 760, 820, 28, "bold", INK2, ab2)
    acc = ep(t, C["28.c"], 0.5)
    if acc > 0:
        rrect(c, 1080, 420, 520, 200, 24, mix("#FFFFFF", AMBER, 0.25), acc)
        text(c, "derrete quanto POR minuto?", 1340, 500, 32, "black", AMBER, acc)
        text(c, "e quando acaba?", 1340, 570, 32, "black", AMBER, acc)
    pill(c, "ep. 2 · coeficiente angular, linear e o zero", 1340, 720, PURPLE, size=26, a=ep(t, C["28.d"], 0.5),
         anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["29.like"], C["29.sub"], C["29.bell"], C["29.com"], C["29.bye"],
        "Qual conta da sua vida tem uma bandeirada escondida?", canal="no Estudativo", anki=C["29.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, taxi=b_taxi, definicao=b_definicao,
              nomes=b_nomes, casos=b_casos, disfarce=b_disfarce, dobro=b_dobro, zero=b_zero, mola=b_mola,
              tirefixo=b_tirefixo, exercicio=b_exercicio, recap=b_recap, erros=b_erros, q2=b_q2, q9=b_q9, ponte=b_ponte,
              cta=b_cta)
