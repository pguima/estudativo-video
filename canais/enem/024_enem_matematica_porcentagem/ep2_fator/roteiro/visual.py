"""Visual — Porcentagem, Episódio 2: o fator de multiplicação (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: maquina() (a máquina de fator com engrenagem: entra o preço antigo, sai o novo), etiqueta() (preço),
blocos() (o bloco "1" do que você já tinha + o pedaço que entra ou sai), linha() (texto com milhar e cor por trecho).
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
_s = importlib.util.spec_from_file_location("comum024", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext, WT = K.fmid, K.ftext, K.WT

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_porcentagem_ep2_fator.mp4"
CARD_R = K.CARD_R
METAL = "#8E9AAF"
BLOCO = "#5B7FD6"


# ======================================================================
# peças do episódio
# ======================================================================

def engrenagem(c, cx, cy, r, ang, col, a, dentes=10):
    """engrenagem simples: disco + dentes retangulares, girada de `ang` graus"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    p = paint(col, a)
    for k in range(dentes):
        c.save(); c.rotate(360 * k / dentes)
        c.drawRect(skia.Rect.MakeXYWH(-r * 0.16, -r * 1.22, r * 0.32, r * 0.4), p)
        c.restore()
    c.drawCircle(0, 0, r, p)
    c.drawCircle(0, 0, r * 0.38, paint("#FFFFFF", a))
    c.restore()


def maquina(c, cx, cy, fator, a, ang=0.0, col=PURPLE, w=330, h=250):
    """a máquina de fator: caixa com engrenagem girando e o rótulo '× fator'"""
    if a <= 0:
        return
    rrect(c, cx - w / 2, cy - h / 2, w, h, 28, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 28, 28), paint(col, a, stroke=6))
    engrenagem(c, cx - w * 0.22, cy - h * 0.12, h * 0.17, ang, mix(col, "#FFFFFF", 0.35), a)
    engrenagem(c, cx + w * 0.05, cy - h * 0.2, h * 0.11, -ang * 1.5 + 18, mix(METAL, "#FFFFFF", 0.2), a, 8)
    ftext(c, f"× {fator}", cx, cy + h * 0.3, 54, "black", col, a)
    # bocas de entrada e saída
    rrect(c, cx - w / 2 - 26, cy - 34, 30, 68, 8, col, a)
    rrect(c, cx + w / 2 - 4, cy - 34, 30, 68, 8, col, a)


def etiqueta(c, s, cx, cy, col, a, size=48, sub=None):
    """etiqueta de preço com furinho"""
    if a <= 0:
        return
    w = text_w(s, "black", size) + 70
    h = size * 1.7
    rrect(c, cx - w / 2, cy - h / 2, w, h, 16, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 16, 16), paint(col, a, stroke=4))
    c.drawCircle(cx - w / 2 + 20, cy, 7, paint(col, a))
    text_mid(c, s, cx + 10, cy, size, "black", col, a)
    if sub:
        text(c, sub, cx, cy + h / 2 + 36, 24, "bold", GRAY, a)


def esteira(c, t, t_in, cx, cy, antes, depois, fator, a, col=PURPLE, dist=430):
    """o preço entra na máquina pela esquerda e sai transformado pela direita"""
    if a <= 0:
        return
    u = ep(t, t_in, 1.4)
    ang = 220 * clamp((t - t_in) / 2.0)
    maquina(c, cx, cy, fator, a, ang, col)
    # entrada: desliza até a boca e some
    xin = lerp(cx - dist - 120, cx - 230, clamp(u * 1.6))
    etiqueta(c, antes, xin, cy, INK, a * (1 - clamp((u - 0.55) * 4)), 46)
    arrow(c, cx - dist + 40, cy + 120, cx - 200, cy + 120, GRAY, a * 0.6, 4, 14)
    arrow(c, cx + 200, cy + 120, cx + dist - 40, cy + 120, GRAY, a * 0.6, 4, 14)
    au = clamp((u - 0.6) * 3)
    etiqueta(c, depois, lerp(cx + 230, cx + dist + 100, au), cy, GREEN, a * au, 46)


def blocos(c, x, y, unit, h, extra, a, col_extra, lbl1="1", lbl2=None, sai=False, sub1=None, sub2=None):
    """bloco '1' (o que você já tinha) + pedaço extra (aumento) ou pedaço retirado (desconto, sai=True)"""
    if a <= 0:
        return
    if not sai:
        rrect(c, x, y, unit, h, 14, BLOCO, a)
        text_mid(c, lbl1, x + unit / 2, y + h / 2, 54, "black", "#FFFFFF", a)
        if extra > 0:
            rrect(c, x + unit + 10, y, unit * extra, h, 14, col_extra, a)
            text_mid(c, lbl2 or "", x + unit + 10 + unit * extra / 2, y + h / 2, 40, "black", "#FFFFFF", a)
    else:
        fica = unit * (1 - extra)
        rrect(c, x, y, fica, h, 14, BLOCO, a)
        text_mid(c, lbl1, x + fica / 2, y + h / 2, 48, "black", "#FFFFFF", a)
        rrect(c, x + fica + 8, y, unit * extra - 8, h, 14, mix(RED, "#FFFFFF", 0.55), a * 0.9)
        text_mid(c, lbl2 or "", x + fica + 4 + unit * extra / 2, y + h / 2, 36, "black", RED, a)
    if sub1:
        text(c, sub1, x + (unit * (1 - extra) if sai else unit) / 2, y + h + 40, 26, "bold", INK2, a)
    if sub2:
        xx = x + unit * (1 - extra) + unit * extra / 2 if sai else x + unit + 10 + unit * extra / 2
        text(c, sub2, xx, y + h + 40, 26, "bold", RED if sai else col_extra, a)


def linha(c, partes, cx, cy, size, a, peso="black"):
    """texto numa linha, centrado em cx, com cor por trecho: partes = [(texto, cor)] (mantém os espaços dos milhares)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def conferido(c, s, x, y, a, ok=True, size=32):
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def lado_a_lado(c, a_l, a_c, titulo_l, linhas_l, titulo_c, linhas_c, y0=250):
    """caminho longo (esquerda, cinza) × caminho curto (direita, verde)"""
    if a_l > 0:
        pill(c, titulo_l, 520, y0, GRAY, size=24, a=a_l, anchor="center", bounds=(0, 1920))
    for k, (s, col, aa) in enumerate(linhas_l):
        linha(c, [(s, col)], 520, y0 + 90 + k * 80, 42, aa)
    line(c, 960, y0 - 20, 960, y0 + 330, "#E6E6E2", max(a_l, a_c), 3)
    if a_c > 0:
        pill(c, titulo_c, 1400, y0, GREEN, size=24, a=a_c, anchor="center", bounds=(0, 1920))
    for k, (s, col, aa) in enumerate(linhas_c):
        linha(c, [(s, col)], 1400, y0 + 90 + k * 80, 42, aa)


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "O FATOR DE MULTIPLICAÇÃO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        text(c, "AUMENTAR 200%", 620, 300, 64, "black", INK, aa)
        ftext(c, "= DOBRAR ?", 620, 390, 54, "black", AMBER, aa)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        strike(c, 500, 372, 770, 372, ab, RED, ep(t, C["01.b"] + 0.3, 0.4))
        # 1 bloco do que tinha + 2 blocos novos = 3
        for k in range(3):
            ak = ab * ep(t, C["01.b"] + 0.3 * k, 0.4)
            rrect(c, 1000 + k * 200, 250, 170, 170, 18, BLUE if k == 0 else GREEN, ak)
            text_mid(c, "100%", 1085 + k * 200, 335, 36, "black", "#FFFFFF", ak)
        text(c, "o que tinha", 1085, 460, 24, "bold", BLUE, ab)
        text(c, "+ 200%", 1385, 460, 24, "bold", GREEN, ab)
        text(c, "= TRIPLICAR", 1300, 540, 60, "black", GREEN, ep(t, C["01.b"] + 0.9, 0.5))
    acc = ep(t, C["01.c"], 0.5)
    if acc > 0:
        maquina(c, W / 2, 720, "3", acc, 200 * clamp((t - C["01.c"]) / 3), PURPLE, 260, 200)
    ad = ep(t, C["01.d"], 0.5)
    if ad > 0:
        selo(c, 1420, 730, ad, "UMA ÚNICA MULTIPLICAÇÃO", GREEN, -4, 32)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "escrever o FATOR de qualquer aumento ou desconto", "sem pensar"),
            ("02.b", "ler um fator ao contrário", "0,65  →  desconto de quanto?")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 360 + j * 220 + d
        check_icon(c, 280, y - 14, 34, a, GREEN)
        text(c, s, 340, y, 48, "black", INK, a, align="left")
        ftext(c, sub, 340, y + 62, 34, "bold", GRAY, a, align="left")


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "UM LEMBRETE", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "EPISÓDIO 1", W / 2, 240, GRAY, size=22, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "PORCENTAGEM = POR CEM", W / 2, 320, 46, "black", BLUE, aa)
        expr(c, "25% = 25/100 = 0,25", W / 2, 440, 72, aa, cores={4: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        ftext(c, "10% = 0,1", 660, 580, 56, "black", INK, ab)
        ftext(c, "5% = 0,05", 1260, 580, 56, "black", INK, ep(t, C["03.b"] + 1.0, 0.5))
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        pill(c, "FORMA DECIMAL", W / 2, 700, BLUE, size=34, a=acc, anchor="center", bounds=(0, 1920))


# ======================================================================
# concreto — as placas e o caminho longo
# ======================================================================

def b_concreto(c, t, C, B):
    head_seq(c, t, C, [("04", "VOCÊ JÁ VIU ESSAS PLACAS", "QUANTO FICA O VALOR NOVO?", BLUE),
                       ("05", "O CAMINHO DE SEMPRE", "DUAS CONTAS", INK2)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        placas = [("04.a", "+25%", "REAJUSTE", AMBER, 500), ("04.b", "−40%", "DESCONTO", RED, 960), ("04.c", "×2", "SALÁRIO DOBROU", GREEN, 1420)]
        for cue, big, small, col, x in placas:
            a = ep(t, C[cue], 0.5)
            if a <= 0:
                continue
            rrect(c, x - 190, 250, 380, 300, 26, col, a, shadow=True)
            text_mid(c, big, x, 370, 96, "black", "#FFFFFF", a)
            text_mid(c, small, x, 480, 30, "black", "#FFFFFF", a)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            selo(c, W / 2, 700, ad, "QUANTO FICA O VALOR NOVO?", BLUE, -2, 40)
        return
    a0 = ep(t, C["05"], 0.5)
    etiqueta(c, "R$ 60", 420, 330, INK, a0, 54, "reajuste de 25%")
    aa = ep(t, C["05.a"], 0.5)
    if aa > 0:
        badge_num(c, 1, 760, 320, aa, 26, bg=GRAY)
        linha(c, [("25% de 60 = ", INK), ("15", AMBER)], 1100, 320, 50, aa)
        text(c, "primeiro, a parte", 1100, 400, 28, "bold", GRAY, aa)
    ab = ep(t, C["05.b"], 0.5)
    if ab > 0:
        badge_num(c, 2, 760, 500, ab, 26, bg=GRAY)
        linha(c, [("60 + 15 = ", INK), ("75", GREEN)], 1100, 500, 50, ab)
        text(c, "depois, soma", 1100, 580, 28, "bold", GRAY, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 730, acc, "E SE FOSSE NUMA CONTA SÓ?", AMBER, -3, 38)


# ======================================================================
# bloco A — o fator de aumento (a máquina)
# ======================================================================

def b_aumento(c, t, C, B):
    head_seq(c, t, C, [("06", "O FATOR DE MULTIPLICAÇÃO", "UMA MÁQUINA", BLUE), ("07", "POR QUE 1,25?", "O 1 É O QUE VOCÊ JÁ TINHA", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07"])
    if sid == "06":
        a0 = ep(t, C["06"], 0.5)
        if a0 > 0:
            boxed(c, 360, 200, 1200, 100, BLUE, a0, 0.08)
            text_mid(c, "FATOR: o número que, × o valor antigo, já dá o valor novo", W / 2, 250, 34, "black", BLUE, a0)
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            u_in = C["06.b"]
            esteira(c, t, u_in, W / 2, 520, "R$ 60", "R$ 75", "1,25", aa)
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            linha(c, [("60 × 1,25 = ", INK), ("75", GREEN)], W / 2, 770, 46, ad)
        return
    aa = ep(t, C["07.a"], 0.5)
    ab = ep(t, C["07.b"], 0.5)
    blocos(c, 420, 250, 600, 170, 0.25 * ab, aa, GREEN, "1", "0,25", sub1="os R$ 60 que você JÁ TINHA",
           sub2="+ 1/4 que ENTRA" if ab > 0.5 else None)
    acc = ep(t, C["07.c"], 0.5)
    if acc > 0:
        boxed(c, 460, 560, 1000, 220, PURPLE, acc, 0.08)
        text(c, "AUMENTO DE x%", W / 2, 615, 30, "black", PURPLE, acc)
        expr(c, "fator = 1 + x/100", W / 2, 700, 70, acc, cores={2: BLUE, 4: GREEN})
        text(c, "x/100 = a taxa em decimal", W / 2, 765, 24, "bold", INK2, ep(t, C["07.c"] + 2.0, 0.5))


# ======================================================================
# bloco B — o fator de desconto
# ======================================================================

def b_desconto(c, t, C, B):
    head_seq(c, t, C, [("08", "E NO DESCONTO?", "LONGO × CURTO", BLUE), ("09", "DESCONTO", "O FATOR É O QUE SOBRA", PURPLE),
                       ("10", "CUIDADO", "5% NÃO É 0,5", AMBER)])
    card(c, *CARD_R)
    sid = which(t, C, ["08", "09", "10"])
    if sid == "08":
        aa = ep(t, C["08.a"], 0.5)
        etiqueta(c, "tênis R$ 200 · −40%", W / 2, 230, INK, aa, 34)
        ab = ep(t, C["08.b"], 0.5)
        acc = ep(t, C["08.c"], 0.5)
        lado_a_lado(c, ab, acc, "CAMINHO LONGO", [("40% de 200 = 80", INK, ab), ("200 − 80 = 120", INK, ep(t, C["08.b"] + 2.2, 0.5))],
                    "CAMINHO CURTO: O FATOR", [("1 − 0,4 = 0,6", PURPLE, acc), ("200 × 0,6 = 120", GREEN, ep(t, C["08.c"] + 2.4, 0.5))],
                    y0=330)
        if acc > 0:
            selo(c, W / 2, 770, ep(t, C["08.c"] + 4.2, 0.5), "BATEU!", GREEN, -4, 40)
        return
    if sid == "09":
        aa = ep(t, C["09.a"], 0.5)
        blocos(c, 520, 240, 880, 160, 0.4, aa, RED, "0,6", "0,4", sai=True, sub1="FICAM 60%", sub2="SAEM 40%")
        ab = ep(t, C["09.b"], 0.5)
        if ab > 0:
            boxed(c, 300, 480, 620, 170, PURPLE, ab, 0.08)
            text(c, "DESCONTO DE x%", 610, 530, 28, "black", PURPLE, ab)
            expr(c, "fator = 1 − x/100", 610, 605, 56, ab, cores={2: BLUE, 4: RED})
        acc = ep(t, C["09.c"], 0.5)
        K.atalho(c, 1000, 480, 640, 300, "ATALHO", ["desconto: o fator", "é o que SOBRA", "100 − 40 = 60 → 0,6"], acc, 32)
        return
    aa = ep(t, C["10.a"], 0.5)
    if aa > 0:
        ftext(c, "+5%", 520, 330, 80, "black", INK, aa)
        ftext(c, "→  1,5", 820, 330, 70, "black", RED, aa)
        strike(c, 720, 330, 930, 330, aa, RED, ep(t, C["10.a"] + 0.8, 0.4))
        text(c, "isso seria +50%!", 820, 410, 26, "bold", RED, ep(t, C["10.a"] + 0.8, 0.4))
    ab = ep(t, C["10.b"], 0.5)
    if ab > 0:
        ftext(c, "5% = 0,05", 1320, 300, 56, "black", INK, ab)
        ftext(c, "fator 1,05", 1320, 390, 64, "black", GREEN, ep(t, C["10.b"] + 1.8, 0.5))
    acc = ep(t, C["10.c"], 0.5)
    K.atalho(c, 420, 500, 1080, 260, "ATALHO", ["a taxa ocupa DUAS casas depois da vírgula", "5% → 0,05   ·   8% → 0,08   ·   25% → 0,25"],
             acc, 34)


# ======================================================================
# bloco C — a tabela em ritmo de jogo
# ======================================================================

def _jogo(c, t, C, sid, itens, primeira):
    for k, (cue, var, fat) in enumerate(itens):
        a = ep(t, C[f"{sid}.{cue}"], 0.4)
        if a <= 0:
            continue
        col, row = k % 3, k // 3
        x, y = 470 + col * 490, 300 + row * 250
        rrect(c, x - 200, y - 75, 400, 190, 22, "#FFFFFF", a, shadow=True)
        ftext(c, var, x, y - 10, 54, "black", INK, a)
        ta = WT(C, sid, primeira, 1, C[f"{sid}.{cue}"])
        ar = ep(t, ta, 0.4)
        if ar > 0:
            ftext(c, f"× {fat}", x, y + 70, 54, "black", GREEN if not var.startswith("−") else RED, ar)
        else:
            pause_timer(c, t, C[f"{sid}.{cue}"] + 0.6, x, y + 64, a, 0.8, 26)


def b_jogo(c, t, C, B):
    head_seq(c, t, C, [("11", "RITMO DE JOGO", "OS AUMENTOS", GREEN), ("12", "RITMO DE JOGO", "OS DESCONTOS", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12"])
    if sid == "11":
        _jogo(c, t, C, "11", [("a", "+5%", "1,05"), ("b", "+10%", "1,10"), ("c", "+20%", "1,20"), ("d", "+25%", "1,25"),
                              ("e", "+50%", "1,50")], "um")
        return
    _jogo(c, t, C, "12", [("a", "−5%", "0,95"), ("b", "−10%", "0,90"), ("c", "−25%", "0,75"), ("d", "−40%", "0,60")], "zero")
    ae = ep(t, C["12.e"], 0.5)
    if ae > 0:
        blocos(c, 1240, 560, 360, 110, 0.25, ae, RED, "0,75", "¼", sai=True)
        text(c, "o que tinha, menos ¼", 1420, 720, 26, "bold", INK2, ae)


# ======================================================================
# bloco D — 100% dobra, 200% triplica
# ======================================================================

def b_dobra(c, t, C, B):
    head_seq(c, t, C, [("13", "AUMENTO DE 100%", "DOBRAR", BLUE), ("14", "AUMENTO DE 200%", "TRIPLICAR", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["13", "14"])
    n_extra = 1 if sid == "13" else 2
    aa = ep(t, C[f"{sid}.a"], 0.5)
    etiqueta(c, "salário R$ 1 500", 400, 240, INK, aa, 36)
    for k in range(1 + n_extra):
        ak = aa * (1 if k == 0 else ep(t, C[f"{sid}.a"] + 0.5 * k, 0.4))
        rrect(c, 300 + k * 290, 340, 260, 190, 18, BLOCO if k == 0 else GREEN, ak)
        text_mid(c, "1 500", 430 + k * 290, 420, 42, "black", "#FFFFFF", ak)
        text(c, "o que tinha" if k == 0 else "+ 100%", 430 + k * 290, 565, 24, "bold", BLOCO if k == 0 else GREEN, ak)
    ab = ep(t, C[f"{sid}.b"], 0.5)
    if ab > 0:
        if sid == "13":
            expr(c, "fator = 1 + 1 = 2", 1350, 360, 56, ab, cores={6: GREEN})
            linha(c, [("1 500 × 2 = ", INK), ("3 000", GREEN)], 1350, 470, 46, ep(t, C["13.b"] + 1.6, 0.5))
        else:
            expr(c, "fator = 1 + 2 = 3", 1400, 360, 56, ab, cores={6: GREEN})
            linha(c, [("1 500 × 3 = ", INK), ("4 500", GREEN)], 1400, 470, 46, ab)
            text(c, "o que tinha + duas vezes ele", 1400, 545, 28, "bold", INK2, ep(t, C["14.b"], 0.5))
    acc = ep(t, C[f"{sid}.c"], 0.5)
    if acc > 0:
        selo(c, W / 2, 700, acc, "AUMENTAR 100% = DOBRAR" if sid == "13" else "AUMENTAR 200% = TRIPLICAR", GREEN, -3, 44)
    if sid == "14":
        ad = ep(t, C["14.d"], 0.5)
        if ad > 0:
            chip(c, "+300% → fator 4", 1400, 790, PURPLE, ad, 30)


# ======================================================================
# bloco E — o caminho de volta
# ======================================================================

def b_volta(c, t, C, B):
    head_seq(c, t, C, [("15", "O CAMINHO DE VOLTA", "LER O FATOR AO CONTRÁRIO", PURPLE), ("16", "A REGRA DA VOLTA", "MAIOR OU MENOR QUE 1?", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["15", "16"])
    if sid == "15":
        aa = ep(t, C["15.a"], 0.5)
        if aa > 0:
            ftext(c, "× 1,5", 520, 270, 64, "black", INK, aa)
            blocos(c, 300, 340, 300, 130, 0.5, aa, GREEN, "1", "0,5", sub1="o que tinha", sub2="passou 0,5")
            text(c, "AUMENTO DE 50%", 520, 600, 40, "black", GREEN, ep(t, C["15.a"] + 2.6, 0.5))
        ab = ep(t, C["15.b"], 0.5)
        if ab > 0:
            line(c, 960, 240, 960, 760, "#E6E6E2", ab, 3)
            ftext(c, "× 0,65", 1380, 270, 64, "black", INK, ab)
            blocos(c, 1180, 340, 400, 130, 0.35, ab, RED, "0,65", "0,35", sai=True, sub1="fica", sub2="falta p/ o 1")
            text(c, "DESCONTO DE 35%", 1380, 600, 40, "black", RED, ep(t, C["15.b"] + 3.0, 0.5))
        return
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        boxed(c, 260, 260, 640, 300, GREEN, aa, 0.08)
        text(c, "FATOR MAIOR QUE 1", 580, 330, 34, "black", GREEN, aa)
        text(c, "AUMENTO", 580, 410, 50, "black", INK, aa)
        text(c, "o que passa do 1", 580, 480, 30, "bold", GREEN, aa)
        ftext(c, "1,08 → +8%", 580, 530, 30, "black", INK2, aa)
    ab = ep(t, C["16.b"], 0.5)
    if ab > 0:
        boxed(c, 1020, 260, 640, 300, RED, ab, 0.08)
        text(c, "FATOR MENOR QUE 1", 1340, 330, 34, "black", RED, ab)
        text(c, "DESCONTO", 1340, 410, 50, "black", INK, ab)
        text(c, "o que falta para o 1", 1340, 480, 30, "bold", RED, ab)
        ftext(c, "0,9 → −10%", 1340, 530, 30, "black", INK2, ab)
    K.atalho(c, 460, 620, 1000, 170, "ATALHO", ["compare com o 1: passou é aumento, faltou é desconto"],
             ep(t, C["16.b"] + 2.4, 0.5), 32)


# ======================================================================
# bloco F — por que o fator é melhor
# ======================================================================

def b_melhor(c, t, C, B):
    head(c, t, B["start"], "POR QUE O FATOR?", "UMA CONTA E MÁQUINAS EM SÉRIE", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        text(c, "caminho longo: 2 contas", 560, 280, 36, "black", GRAY, aa)
        text(c, "fator: 1 conta", 1360, 280, 36, "black", GREEN, aa)
        check_icon(c, 1190, 268, 24, aa, GREEN)
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        ang = 200 * clamp((t - C["17.b"]) / 3)
        cols = [GREEN, RED, GREEN]
        fats = ["1,1", "0,8", "1,2"]
        n_on = 1 + int(ep(t, C["17.c"], 0.3) * 2 + 0.001) if t >= C["17.c"] else 1
        for k in range(3):
            ak = ab * (1 if k < n_on else ep(t, C["17.c"] + 0.8 * k, 0.4))
            maquina(c, 520 + k * 440, 560, fats[k], ak, ang * (1 if k % 2 == 0 else -1), cols[k], 280, 210)
            if k < 2:
                arrow(c, 680 + k * 440, 560, 795 + k * 440, 560, GRAY, ak * ep(t, C["17.c"] + 0.8 * (k + 1), 0.4), 5, 18)
        text(c, "aumento · desconto · aumento", W / 2, 760, 30, "bold", INK2, ep(t, C["17.c"], 0.5))


# ======================================================================
# nós fazemos
# ======================================================================

def _cartas(c, t, C, sid_q, sid_r, itens, respostas, cor_resp):
    for k, s in enumerate(itens):
        a = ep(t, C[f"{sid_q}.a"] + 0.6 * k, 0.4)
        x = 470 + k * 490
        rrect(c, x - 210, 260, 420, 300, 24, "#FFFFFF", a, shadow=True)
        ftext(c, s, x, 380, 60, "black", INK, a)
        if t >= C[sid_r]:
            ar = ep(t, C[f"{sid_r}.{'abc'[k]}"], 0.4)
            ftext(c, respostas[k], x, 490, 50, "black", cor_resp[k], ar)


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("18", "SUA VEZ", "DIGA O FATOR", GREEN), ("19", "VAMOS CONFERIR", "DIGA O FATOR", GREEN)])
    card(c, *CARD_R)
    _cartas(c, t, C, "18", "19", ["+15%", "−30%", "+150%"], ["× 1,15", "× 0,70", "× 2,5"], [GREEN, RED, GREEN])
    if t < C["19"]:
        pause_timer(c, t, C["18.end"] - 1.9, W / 2, 690)
    else:
        aa = ep(t, C["19.b"], 0.5)
        if aa > 0:
            text(c, "sobram 70%", 960, 640, 28, "bold", INK2, aa)
        acc = ep(t, C["19.c"], 0.5)
        if acc > 0:
            text(c, "1 + 1,5", 1450, 640, 28, "bold", INK2, acc)


def b_exercicio2(c, t, C, B):
    head_seq(c, t, C, [("20", "AO CONTRÁRIO", "DIGA A VARIAÇÃO", GREEN), ("21", "CONFERINDO", "DIGA A VARIAÇÃO", GREEN)])
    card(c, *CARD_R)
    _cartas(c, t, C, "20", "21", ["× 1,08", "× 0,85", "× 2,5"], ["+8%", "−15%", "+150%"], [GREEN, RED, GREEN])
    if t < C["21"]:
        pause_timer(c, t, C["20.end"] - 1.9, W / 2, 690)
    else:
        for k, s in enumerate(["passou 0,08", "faltam 0,15", "passou 1,5"]):
            text(c, s, 470 + k * 490, 640, 28, "bold", INK2, ep(t, C[f"21.{'abc'[k]}"] + 1.0, 0.5))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Aumento: 1 + a taxa. Desconto: 1 − a taxa.", "O 1 é o que você já tinha.", "Aumentar 200% é triplicar."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["22", "29"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "22" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Achar que aumentar 200% é dobrar", "200 lembra \"duas vezes\"",
          "o fator é 1 + 2 = 3: triplica. Dobrar é aumentar 100%"),
         ("Usar 0,25 como fator de um aumento de 25%", "0,25 é mesmo 25%",
          "60 × 0,25 = 15: o preço despencaria. Faltou o 1: o fator é 1,25"),
         ("Ler o fator 0,65 como desconto de 65%", "o 65 está ali, bem à vista",
          "65% é o que FICA; o desconto é o que SAI: 1 − 0,65 = 35%")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["23", "24", "25"], ERROS)


# ======================================================================
# Questão 2 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=32, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS2 = [("A", "R$ 85,00", "não sai de conta certa", RED), ("B", "R$ 96,00", "usou 20%", RED),
         ("C", "R$ 100,00", "", GREEN), ("D", "R$ 105,00", "somou R$ 25, não 25%", RED),
         ("E", "R$ 120,00", "usou 50%", RED)]


def b_q2(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · PAUSE E TENTE", "FATOR DE AUMENTO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["26.a"], 0.4)
    _enunciado(c, [("Um produto que custava R$ 80,00 sofreu reajuste de 25%.", INK),
                   ("O novo preço do produto é", BLUE)], a0, 250)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"26.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"28.x{L.lower()}"] for L in "ABDE"}
    if t >= C["26.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS2, 1000, 250, 680, 44, C["27.ok"], "C", cues_in, cues_x, gap=34)
    if t < C["27"]:
        pause_timer(c, t, C["26.end"] - 1.9, 540, 600)
        return
    ra = ep(t, C["27"], 0.4)
    rrect(c, 170, 420, 740, 390, 18, "#FFFFFF", ra, shadow=True)
    aa = ep(t, C["27.a"], 0.4)
    if aa > 0:
        pill(c, "FATOR", 250, 470, PURPLE, size=20, a=aa, anchor="left", bounds=(0, 1920))
        linha(c, [("80 × 1,25 = ", INK), ("100", GREEN)], 600, 475, 40, aa)
    ab = ep(t, C["27.b"], 0.4)
    if ab > 0:
        pill(c, "LONGO", 250, 570, GRAY, size=20, a=ab, anchor="left", bounds=(0, 1920))
        linha(c, [("20 + 80 = ", INK), ("100", GREEN)], 600, 575, 40, ab)
    acc = ep(t, C["27.c"], 0.4)
    if acc > 0:
        pill(c, "ATALHO ¼", 250, 670, GREEN, size=20, a=acc, anchor="left", bounds=(0, 1920))
        linha(c, [("80 ÷ 4 = 20", INK)], 600, 675, 40, acc)
    ach = ep(t, C["28.chk"], 0.4)
    if ach > 0:
        conferido(c, "¼ de 80 = 20 → só pode ser 100", 210, 770, ach, True, 28)


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "VARIAÇÕES SUCESSIVAS", PURPLE)
    aa = ep(t, C["30.a"], 0.5)
    ang = 200 * clamp((t - C["30.a"]) / 4)
    maquina(c, 660, 400, "1,1", aa, ang, GREEN, 280, 210)
    maquina(c, 1260, 400, "1,2", aa * ep(t, C["30.a"] + 1.0, 0.4), -ang, GREEN, 280, 210)
    arrow(c, 820, 400, 1100, 400, GRAY, aa * ep(t, C["30.a"] + 1.2, 0.4), 5, 18)
    ab = ep(t, C["30.b"], 0.5)
    if ab > 0:
        ftext(c, "+10% e +20% = +30% ?", W / 2, 640, 56, "black", AMBER, ab)
    acc = ep(t, C["30.c"], 0.5)
    if acc > 0:
        strike(c, 680, 622, 1240, 622, acc, RED, acc)
        selo(c, 1500, 600, acc, "NÃO!", RED, -6, 50)
    pill(c, "ep. 3 · variações sucessivas", W / 2, 770, PURPLE, size=32, a=ep(t, C["30.d"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["31.like"], C["31.sub"], C["31.bell"], C["31.com"], C["31.bye"], "Achava que +200% era dobrar?",
        canal="no Estudativo", anki=C["31.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, concreto=b_concreto, aumento=b_aumento, desconto=b_desconto,
              jogo=b_jogo, dobra=b_dobra, volta=b_volta, melhor=b_melhor, exercicio=b_exercicio, exercicio2=b_exercicio2,
              recap=b_recap, erros=b_erros, q2=b_q2, ponte=b_ponte, cta=b_cta)
