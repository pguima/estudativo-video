"""Visual — Potenciação e Radiciação, Episódio 1: O que é potência e os casos especiais (iniciantes, tema claro).
Peças comuns da série em ../../comum.py (tipografia de potências/raízes no expr, folha dobrada, contador, escada, fila...).
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
_s = importlib.util.spec_from_file_location("comum019", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_potenciacao_ep1_o_que_e_potencia.mp4"
CARD_R = K.CARD_R
ZAP = "#25A35A"


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

TEMAS = [("juros", "C·(1+i)^t"), ("Pitágoras", "a^2=b^2+c^2"), ("áreas", "A=ℓ^2"), ("meia-vida", "m/2^n"), ("pH", "10^{-7}")]


def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "POTÊNCIA DO ZERO", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        boxed(c, 510, 190, 900, 110, AMBER, aa, 0.10)
        text_mid(c, "potência como TEMA da questão: quase nunca", W / 2, 245, 40, "black", INK, aa)
    ab = ep(t, C["01.b"], 0.5)
    text(c, "mas ela é a LÍNGUA das questões de…", W / 2, 380, 40, "black", BLUE, ab)
    for k, (nome, f_) in enumerate(TEMAS):
        a = ep(t, C["01.c"] + 0.4 * k, 0.4)
        if a <= 0:
            continue
        x = 300 + k * 330
        card(c, x - 145, 430, 290, 220, a)
        expr(c, f_, x, 520, 50, a, cores={0: PURPLE})
        text(c, nome, x, 620, 32, "black", INK, a)
    ad = ep(t, C["01.d"], 0.5)
    selo(c, W / 2, 760, ad, "QUEM NÃO LÊ, TRAVA ANTES DE COMEÇAR", RED, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI SABER", GREEN)
    rows = [("02.a", "o que é uma potência", "do zero, com papel dobrado"), ("02.b", "por que 2^0 dá 1", "sem decorar: com uma escada")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 300 + j * 170 + d
        check_icon(c, 300, y - 14, 34, a, GREEN)
        ftext(c, s, 360, y, 50, "black", INK, a, align="left")
        text(c, sub, 360, y + 54, 32, "bold", GRAY, a, align="left")
    ac = ep(t, C["02.c"], 0.5)
    if ac > 0:
        boxed(c, 300, 640, 1320, 130, AMBER, ac, 0.10)
        expr(c, "2^{-3} = 1/8", 560, 705, 60, ac, cores={0: INK, 1: INK, 2: GREEN})
        text_mid(c, "expoente negativo NÃO deixa negativo", 1170, 705, 38, "black", INK, ac)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "DOIS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        text(c, "MULTIPLICAR = somar parcelas iguais", 560, 250, 32, "black", BLUE, aa)
        for g in range(3):
            gx = 300 + g * 180
            rrect(c, gx, 300, 160, 130, 16, mix("#FFFFFF", BLUE, 0.08), aa * ep(t, C["03.a"] + 0.4 + 0.3 * g, 0.3))
            for k in range(2):
                c.drawCircle(gx + 50 + k * 60, 365, 18, paint(BLUE, aa * ep(t, C["03.a"] + 0.4 + 0.3 * g, 0.3)))
        expr(c, "3 · 2 = 2 + 2 + 2 = 6", 560, 520, 50, aa, cores={8: GREEN})
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        text(c, "INVERTER = virar de cabeça para baixo", 1340, 250, 32, "black", BLUE, ab)
        acc = ep(t, C["03.c"], 0.5)
        expr(c, "2 = 2/1 → 1/2", 1340, 390, 60, acc, cores={4: GREEN})
        ad = ep(t, C["03.d"], 0.5)
        expr(c, "2/3 → 3/2", 1340, 560, 60, ad, cores={2: GREEN})
    line(c, 960, 230, 960, 800, "#E6E6E2", aa, 3)


# ======================================================================
# bloco A — o papel dobrado
# ======================================================================

def _dobras(t, cues):
    """quantas dobras já aconteceram e o progresso da próxima (a dobra termina ~0,2 s antes do número ser dito)"""
    n = sum(1 for x in cues if t >= x - 0.2)
    if n >= len(cues):
        return n, 0.0
    nxt = cues[n]
    return n, clamp((t - (nxt - 1.1)) / 0.9)


def b_papel(c, t, C, B):
    head_seq(c, t, C, [("04", "DOBRE UMA FOLHA AO MEIO", "QUANTAS CAMADAS?", BLUE), ("05", "O NOME DISSO", "POTÊNCIA", BLUE),
                       ("06", "NO GERAL", "A ELEVADO A N", BLUE), ("07", "ATALHO", "VÁ DOBRANDO O RESULTADO", GREEN)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05", "06", "07"])
    if sid == "04":
        a0 = ep(t, C["04"], 0.5)
        ws = [K.WT(C, "04", "duas"), K.WT(C, "04", "quatro"), K.WT(C, "04", "oito")]
        n, pr = _dobras(t, ws)
        K.folha(c, 560, 500, 560, 400, n, a0, pr)
        K.contador(c, 1300, 420, 2 ** n, a0, "camadas")
        steps = ["1", "× 2 = 2", "× 2 = 4", "× 2 = 8"]
        for k in range(1, 4):
            a = ep(t, ws[k - 1], 0.4)
            text(c, f"{k}ª dobra  →  {2 ** k} camadas", 1300, 590 + k * 50 - 50, 30, "black", INK2 if k < n else BLUE, a)
        chip(c, "cada dobra: × 2", 1300, 760, AMBER, ep(t, C["04.d"], 0.5), 32)
        if t > C["04.e"] - 0.2:
            ae = ep(t, C["04.e"], 0.5)
            rrect(c, 330, 740, 460, 80, 18, "#FFFFFF", ae, shadow=True)
            expr(c, "2 · 2 · 2 = 8", 560, 780, 46, ae, cores={6: GREEN})
        return
    if sid == "05":
        K.folha(c, 380, 470, 280, 200, 3, ep(t, C["05"], 0.4) * 0.9)
        text(c, "3 dobras", 380, 690, 30, "black", INK2, ep(t, C["05"], 0.4))
        a0 = ep(t, C["05.t"], 0.5)
        cx, cy = 1050, 420
        ab, ac = ep(t, C["05.b"], 0.4), ep(t, C["05.c"], 0.4)
        expr(c, "2^3", cx, cy, 230, a0, cores={0: INK})
        if ab > 0:
            rrect(c, cx - 150, cy - 130, 170, 230, 24, BLUE, 0.12 * ab)
            arrow(c, cx - 70, cy + 230, cx - 70, cy + 120, BLUE, ab, 5, 16, progress=ab)
            text(c, "BASE", cx - 70, cy + 280, 34, "black", BLUE, ab)
            text(c, "o número que se repete", cx - 70, cy + 320, 26, "bold", INK2, ab)
        if ac > 0:
            rrect(c, cx + 25, cy - 190, 110, 140, 20, PURPLE, 0.14 * ac)
            arrow(c, cx + 330, cy - 120, cx + 150, cy - 120, PURPLE, ac, 5, 16, progress=ac)
            text(c, "EXPOENTE", cx + 470, cy - 135, 34, "black", PURPLE, ac)
            text(c, "quantas vezes a base aparece", cx + 470, cy - 95, 24, "bold", INK2, ac)
        aa = ep(t, C["05.a"], 0.5) * (1 - ep(t, C["05.b"], 0.4))
        pill(c, "POTÊNCIA = multiplicação de números iguais", cx + 200, 760, BLUE, size=30, a=aa, anchor="center", bounds=(0, 1920))
        ad = ep(t, C["05.d"], 0.5)
        if ad > 0:
            w = K.fila(c, 1290, 600, ["2", "2", "2"], ad, size=60)
            text(c, "cada 2 é um FATOR", 1290 + w / 2, 720, 30, "black", BLUE, ad)
        return
    if sid == "06":
        a0 = ep(t, C["06"], 0.5)
        expr(c, "a^n = a · a · … · a", W / 2, 240, 66, a0, cores={0: PURPLE})
        aa = ep(t, C["06.a"], 0.5)
        if aa > 0:
            x0, x1 = W / 2 - 80, W / 2 + 340
            line(c, x0, 300, x1, 300, PURPLE, aa, 4)
            line(c, x0, 300, x0, 285, PURPLE, aa, 4); line(c, x1, 300, x1, 285, PURPLE, aa, 4)
            text(c, "n fatores", (x0 + x1) / 2, 340, 28, "black", PURPLE, aa)
            text(c, "a = qualquer número", 420, 340, 28, "bold", INK2, aa)
        ab = ep(t, C["06.b"], 0.5)
        if ab > 0:
            text(c, "corrente de WhatsApp: cada pessoa manda para 2", W / 2, 410, 32, "black", ZAP, ab)
            for k in range(1, 6):
                ak = ab * ep(t, C["06.c"] + 0.45 * (k - 1), 0.3) if k > 1 else ab
                y = 460 + (k - 1) * 66
                n = 2 ** k
                sp = min(60, 1150 / n)
                x0 = W / 2 - (n - 1) * sp / 2 + 80
                text(c, f"{k}ª rodada", 300, y + 12, 26, "black", INK2, ak, align="left")
                for i in range(n):
                    c.drawCircle(x0 + i * sp, y, min(13, sp * 0.4), paint(ZAP, ak))
                text(c, str(n), 1700, y + 12, 30, "black", ZAP if k == 5 else INK2, ak, align="right")
        ad = ep(t, C["06.d"], 0.5)
        if ad > 0:
            rrect(c, 560, 770, 800, 64, 16, "#FFFFFF", ad, shadow=True)
            expr(c, "2^5 = 2 · 2 · 2 · 2 · 2 = 32", W / 2, 802, 36, ad, cores={12: GREEN}, alfas={12: ep(t, C["06.e"], 0.4)})
        return
    # 07 atalho
    a0 = ep(t, C["07.a"], 0.5)
    boxed(c, 220, 200, 1480, 560, GREEN, a0, 0.06)
    text(c, "ATALHO", W / 2, 250, 24, "black", GREEN, a0, tracking=2)
    text(c, "vá dobrando o resultado", W / 2, 310, 44, "black", INK, a0)
    vals = [2, 4, 8, 16, 32]
    for k, v in enumerate(vals):
        a = ep(t, C["07.b"] + 0.45 * k, 0.35)
        x = 380 + k * 290
        text_mid(c, str(v), x, 470, 90, "black", GREEN if k == 4 else INK, a)
        badge_num(c, k + 1, x, 570, ep(t, C["07.d"] + 0.25 * k, 0.3), 24, bg=GREEN)
        if k > 0:
            arrow(c, x - 220, 470, x - 80, 470, LIGHT, a, 5, 14, progress=a)
            fmid(c, "×2", x - 150, 415, 30, "black", AMBER, a)
    text(c, "cada passo = o anterior × a base", W / 2, 660, 34, "bold", INK2, ep(t, C["07.c"], 0.5))
    ad = ep(t, C["07.d"], 0.5)
    expr(c, "5 passos → 2^5 = 32", W / 2, 720, 44, ad, cores={3: GREEN, 4: GREEN, 5: GREEN})


# ======================================================================
# bloco B — o erro de partida
# ======================================================================

def b_erro_partida(c, t, C, B):
    frame(c, t, B["start"], "2 ELEVADO A 3 É…", "O ERRO DE PARTIDA", AMBER)
    a0 = ep(t, C["08"], 0.5)
    ac = ep(t, C["08.c"], 0.5)
    expr(c, "2^3 =", 520, 330, 130, a0)
    aa = ep(t, C["08.a"], 0.5)
    fmid(c, "6", 790, 330, 130, "black", RED, aa * (1 - 0.6 * ac))
    if ac > 0:
        strike(c, 740, 330, 845, 330, ac, RED, ac)
        fmid(c, "8", 940, 330, 130, "black", GREEN, ep(t, C["08.c"] + 0.8, 0.4))
    ab = ep(t, C["08.b"], 0.5)
    pill(c, "PARECE CERTO PORQUE...", 300, 520, AMBER, size=26, a=ab, bounds=(0, 1920))
    expr(c, "2 · 3 = 6", 470, 610, 54, ab * (1 - 0.6 * ac), cores={4: AMBER})
    K.folha(c, 1380, 420, 300, 220, 3, ac)
    text(c, "3 dobras = 8 camadas", 1380, 620, 34, "black", BLUE, ac)
    regra(c, "a base vezes ELA MESMA: 2 · 2 · 2 = 8", W / 2, 760, ep(t, C["08.d"], 0.5), 36)


# ======================================================================
# bloco C — expoente 1 e base 1
# ======================================================================

def b_um(c, t, C, B):
    head_seq(c, t, C, [("09", "EXPOENTE 1", "UM FATOR SÓ", BLUE), ("10", "BASE 1", "NÃO SAI DO LUGAR", BLUE)])
    card(c, *CARD_R)
    a0 = ep(t, C["09"], 0.5)
    text(c, "expoente 1", 560, 240, 30, "black", GRAY, a0)
    K.folha(c, 400, 400, 200, 150, 1, a0)
    K.fila(c, 600, 400, ["a"], ep(t, C["09.a"], 0.4), size=64)
    regra(c, "a^1 = a", 560, 580, ep(t, C["09.b"], 0.5), 50)
    expr(c, "7^1 = 7", 560, 720, 64, ep(t, C["09.c"], 0.5), cores={2: GREEN})
    line(c, 960, 220, 960, 800, "#E6E6E2", ep(t, C["10"], 0.4), 3)
    a1 = ep(t, C["10"], 0.5)
    text(c, "base 1", 1360, 240, 30, "black", GRAY, a1)
    K.fila(c, 1130, 400, ["1", "1", "1", "1", "1"], ep(t, C["10.a"], 0.4), size=56, alfas={i: ep(t, C["10.a"] + 0.3 * i, 0.3) for i in range(5)})
    text(c, "não sai do lugar", 1360, 520, 32, "bold", INK2, ep(t, C["10.b"], 0.4))
    regra(c, "1^n = 1", 1360, 600, ep(t, C["10.b"], 0.5), 50)
    expr(c, "1^{500} = 1", 1360, 730, 64, ep(t, C["10.c"], 0.5), cores={2: GREEN})


# ======================================================================
# blocos D e E — a escada que desce dividindo
# ======================================================================

DEGRAUS = [("2^3", "8"), ("2^2", "4"), ("2^1", "2"), ("2^0", "1"), ("2^{-1}", "1/2"), ("2^{-2}", "1/4"), ("2^{-3}", "1/8")]
EX0, EY0, EPX, EPY = 190, 200, 222, 60


def b_escada(c, t, C, B):
    head_seq(c, t, C, [("11", "2 ELEVADO A ZERO?", "ZERO FATORES…", AMBER), ("12", "A ESCADA", "CADA DEGRAU PARA BAIXO: ÷ 2", PURPLE),
                       ("13", "O PRÓXIMO DEGRAU", "EXPOENTE ZERO", PURPLE), ("14", "CONTINUANDO A DESCER", "EXPOENTE NEGATIVO", PURPLE)])
    card(c, *CARD_R)
    sid = which(t, C, ["11", "12", "13", "14"])
    if sid == "11":
        a0 = ep(t, C["11"], 0.5)
        expr(c, "2^0 = ?", W / 2, 400, 170, a0)
        aa = ep(t, C["11.a"], 0.5)
        selo(c, 1400, 300, aa, "dá zero?", AMBER, -8, 40)
        pill(c, "em vez de decorar: DESCOBRIR", W / 2, 680, GREEN, size=36, a=ep(t, C["11.b"], 0.5), anchor="center", bounds=(0, 1920))
        return
    ativos, setas = {}, {}
    if sid == "12":
        for i, cue in enumerate(["12.t", "12.a", "12.b"]):
            ativos[i] = ep(t, C[cue], 0.5)
        setas = {0: ep(t, C["12.c"], 0.5), 1: ep(t, C["12.c"] + 0.4, 0.5)}
    else:
        for i in range(3):
            ativos[i] = 1.0
        setas = {0: 1.0, 1: 1.0}
        if sid in ("13", "14"):
            ativos[3] = ep(t, C["13.a"], 0.5)
            setas[2] = ep(t, C["13.a"] - 0.3, 0.5)
        if sid == "14":
            for i, cue in ((4, "14.b"), (5, "14.c"), (6, "14.d")):
                ativos[i] = ep(t, C[cue], 0.5)
            setas[3] = ep(t, C["14.a"], 0.5)
            setas[4] = ep(t, C["14.c"] - 0.4, 0.5)
            setas[5] = ep(t, C["14.d"] - 0.4, 0.5)
    destaque = {}
    if sid == "13":
        destaque = {3: ep(t, C["13.b"], 0.4)}
    _escada(c, t, ativos, setas, destaque)
    if sid == "12":
        regra(c, "8 → 4 → 2: cada degrau para baixo DIVIDE por 2", 1240, 230, ep(t, C["12.d"], 0.5), 30)
    if sid == "13":
        ab = ep(t, C["13.b"], 0.5)
        regra(c, "2^0 = 1", 1430, 215, ab, 46)
        ac = ep(t, C["13.c"], 0.5)
        expr(c, "99^0 = 1", 1430, 315, 50, ac, cores={2: GREEN})
        text(c, "qualquer base, MENOS o zero", 1430, 385, 26, "black", INK2, ac)
        ad = ep(t, C["13.d"], 0.5)
        if ad > 0:
            boxed(c, 1180, 410, 500, 66, AMBER, ad, 0.10)
            ftext(c, "0^0: dividiria por zero ✗", 1430, 455, 30, "black", INK, ad)
        ae = ep(t, C["13.e"], 0.5)
        if ae > 0:
            boxed(c, 1180, 490, 500, 120, GREEN, ae, 0.10)
            text(c, "ATALHO", 1430, 525, 20, "black", GREEN, ae, tracking=2)
            text(c, "expoente zero → 1, sem conta", 1430, 580, 32, "black", INK, ae)
    if sid == "14":
        pill(c, "depois do zero: −1, −2, −3…", 1480, 230, PURPLE, size=28, a=ep(t, C["14.a"], 0.5), anchor="center", bounds=(0, 1920))


def _escada(c, t, ativos, setas, destaque):
    for i, (s, v) in enumerate(DEGRAUS):
        ai = ativos.get(i, 0.0)
        if ai <= 0:
            continue
        x, y = EX0 + i * EPX, EY0 + i * EPY + 120
        h = 130
        hl = destaque.get(i, 0.0)
        rrect(c, x, y, EPX - 14, h, 16, mix(K.DEGRAU, GREEN, 0.25 * hl), ai, shadow=True)
        rrect(c, x, y, EPX - 14, 10, 5, PURPLE if i < 3 else (GREEN if i == 3 else BLUE), ai * 0.9)
        expr(c, s, x + (EPX - 14) / 2, y + 42, 42, ai, cores={0: INK})
        expr(c, v, x + (EPX - 14) / 2, y + 96, 42 if "/" not in v else 36, ai,
             cores={0: PURPLE if i < 3 else (GREEN if i == 3 else BLUE)})
    for i, sa in setas.items():
        if sa <= 0:
            continue
        x1 = EX0 + i * EPX + (EPX - 14) * 0.7
        y1 = EY0 + i * EPY + 112
        x2 = EX0 + (i + 1) * EPX + (EPX - 14) * 0.3
        y2 = EY0 + (i + 1) * EPY + 112
        p = skia.Path(); p.moveTo(x1, y1); p.quadTo((x1 + x2) / 2, y1 - 50, x2, y2)
        pe = paint(AMBER, sa, stroke=5, cap_round=True)
        c.drawPath(p, pe)
        for s_ in (-1, 1):
            ang = math.atan2(y2 - (y1 - 50), x2 - (x1 + x2) / 2)
            c.drawLine(x2, y2, x2 - 16 * math.cos(ang + s_ * 0.5), y2 - 16 * math.sin(ang + s_ * 0.5), pe)
        fmid(c, "÷ 2", (x1 + x2) / 2, y1 - 56, 36, "black", AMBER, sa)


def b_negativo(c, t, C, B):
    frame(c, t, B["start"], "DOIS DEGRAUS LADO A LADO", "O MENOS MANDA INVERTER", PURPLE)
    aa = ep(t, C["15.a"], 0.5)
    expr(c, "2^3 = 8", 520, 290, 80, aa, cores={2: PURPLE})
    expr(c, "2^{-3} = 1/8", 1400, 290, 80, ep(t, C["15.a"] + 1.2, 0.5), cores={2: BLUE})
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        p = skia.Path(); p.moveTo(700, 360); p.quadTo(W / 2, 450, 1220, 360)
        c.drawPath(p, paint(GREEN, ab, stroke=5, cap_round=True))
        chip(c, "o INVERSO do 8", W / 2, 440, GREEN, ab, 32)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        boxed(c, 560, 510, 800, 150, PURPLE, acc, 0.08)
        expr(c, "a^{-n} = 1/a^n", W / 2, 585, 66, acc, cores={0: PURPLE, 1: PURPLE, 2: PURPLE})
    text(c, "a = a base · n = o expoente", W / 2, 700, 28, "bold", INK2, acc)
    ae = ep(t, C["15.e"], 0.5)
    if ae > 0:
        boxed(c, 470, 730, 980, 90, GREEN, ae, 0.10)
        text(c, "ATALHO", 600, 785, 20, "black", GREEN, ae, tracking=2)
        text(c, "inverta a base e tire o menos do expoente", 1010, 785, 32, "black", INK, ae)
    else:
        pill(c, "o menos no expoente = INVERTER", W / 2, 780, PURPLE, size=30, a=ep(t, C["15.d"], 0.5), anchor="center", bounds=(0, 1920))


def b_fracao(c, t, C, B):
    frame(c, t, B["start"], "E SE A BASE FOR FRAÇÃO?", "VIRA DE CABEÇA PARA BAIXO", PURPLE)
    a0 = ep(t, C["16.t"], 0.5)
    ab, ae = ep(t, C["16.b"], 0.5), ep(t, C["16.e"], 0.5)
    expr(c, "(2/3)^{-2} = (3/2)^2 = 9/4", W / 2, 290, 86, a0, cores={0: INK, 2: PURPLE, 4: GREEN},
         alfas={1: ab, 2: ab, 3: ae, 4: ae})
    # a fração virando
    u = ep(t, C["16.a"], 1.0)
    aa = ep(t, C["16.a"], 0.4)
    if aa > 0:
        cx, cy = 480, 590
        c.save(); c.translate(cx, cy)
        sc = math.cos(math.pi * u)
        c.scale(1, max(0.02, abs(sc)))
        if sc >= 0:
            fr(c, "2", "3", 0, -20, 110, INK, aa)
        else:
            fr(c, "3", "2", 0, -20, 110, BLUE, aa)
        c.restore()
        text(c, "inverter = de cabeça para baixo", cx, 800, 28, "black", BLUE, aa)
    acc = ep(t, C["16.c"], 0.5)
    if acc > 0:
        chip(c, "AO QUADRADO = vezes ela mesma", 1260, 470, BLUE, acc, 30)
        expr(c, "(3/2)^2 = 3/2 · 3/2", 1260, 570, 54, acc)
    ad = ep(t, C["16.d"], 0.5)
    expr(c, "3·3/2·2 = 9/4", 1260, 700, 54, ad, cores={2: GREEN})
    if ae > 0:
        boxed(c, 800, 770, 920, 56, GREEN, ae, 0.10)
        text_mid(c, "ATALHO: fração com expoente negativo → vire de cabeça para baixo", 1260, 798, 24, "black", GREEN, ae)


def b_nao_negativo(c, t, C, B):
    frame(c, t, B["start"], "E O RESULTADO, FICA NEGATIVO?", "NÃO: FICA PEQUENININHO", AMBER)
    a0 = ep(t, C["17"], 0.5)
    x0, x1, y = 260, 1660, 430
    val = lambda v: lerp(x0, x1, (v + 9) / 18)
    line(c, x0, y, x1, y, INK2, a0, 5)
    for v in range(-8, 9, 2):
        line(c, val(v), y - 14, val(v), y + 14, INK2, a0, 4)
        text(c, str(v).replace("-", "−"), val(v), y + 56, 28, "bold", INK2, a0)
    aa = ep(t, C["17.a"], 0.5)
    if aa > 0:
        xv = val(0.125)
        c.drawCircle(xv, y, 16, paint(GREEN, aa))
        arrow(c, xv + 120, y - 120, xv + 12, y - 18, GREEN, aa, 4, 14, progress=aa)
        expr(c, "2^{-3} = 1/8 = 0,125", xv + 330, y - 150, 46, aa, cores={0: GREEN, 1: GREEN, 2: GREEN, 3: GREEN, 4: GREEN})
        text(c, "positivo, pertinho do zero", xv + 330, y - 80, 28, "black", INK2, aa, align="center")
    ab = ep(t, C["17.b"], 0.5)
    if ab > 0:
        xv = val(-8)
        c.drawCircle(xv, y, 16, paint(RED, ab))
        check_icon(c, xv, y - 90, 30, ab, RED, "x")
        text(c, "−8? não!", xv + 20, y - 140, 34, "black", RED, ab)
    regra(c, "o menos do expoente NÃO mexe no sinal da resposta", W / 2, 640, ep(t, C["17.c"], 0.5), 36)
    chip(c, "ele só manda INVERTER", W / 2, 760, PURPLE, ep(t, C["17.d"], 0.5), 34)


def b_sinal(c, t, C, B):
    frame(c, t, B["start"], "REVISÃO RELÂMPAGO", "QUANDO A RESPOSTA FICA NEGATIVA", BLUE)
    aa = ep(t, C["18.a"], 0.5)
    expr(c, "(-2)^4 = 16", 520, 270, 64, aa, cores={2: GREEN})
    chip(c, "base negativa, expoente PAR → +", 520, 360, GREEN, aa, 26)
    ab = ep(t, C["18.b"], 0.5)
    expr(c, "(-2)^3 = -8", 1400, 270, 64, ab, cores={2: RED})
    chip(c, "expoente ÍMPAR → −  ·  3 = “ao cubo”", 1400, 360, RED, ab, 26)
    acc = ep(t, C["18.c"], 0.5)
    if acc > 0:
        boxed(c, 560, 420, 800, 80, GREEN, acc, 0.10)
        ftext(c, "ATALHO: os menos se cancelam em pares  (−)·(−) = +", W / 2, 472, 28, "black", GREEN, acc)
    line(c, 260, 540, 1660, 540, "#E6E6E2", acc, 3)
    ad = ep(t, C["18.d"], 0.5)
    expr(c, "-3^2 = -9", 520, 640, 70, ad, cores={2: RED})
    text(c, "sem parêntese: o expoente não pega o sinal", 520, 750, 26, "bold", INK2, ad)
    ae = ep(t, C["18.e"], 0.5)
    expr(c, "(-3)^2 = 9", 1400, 640, 70, ae, cores={2: GREEN})
    text(c, "com parêntese: (−3) · (−3)", 1400, 750, 26, "bold", INK2, ae)


# ======================================================================
# nós fazemos
# ======================================================================

EXS = [("19.a", "5^0", "1", "expoente zero"), ("19.b", "3^{-2}", "1/9", "inverte: 1/3²"), ("19.c", "(1/2)^{-1}", "2", "de cabeça para baixo"),
       ("19.d", "(-1)^7", "-1", "ímpar → negativo")]


def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("19", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("20", "VAMOS CONFERIR", "PAUSE E CALCULE", GREEN)])
    card(c, *CARD_R)
    for k, (cue, q, r, why) in enumerate(EXS):
        a = ep(t, C[cue], 0.5)
        if a <= 0:
            continue
        x = 330 + k * 420
        rrect(c, x - 185, 210, 370, 260, 24, "#F7F7F5", a)
        text(c, f"{k + 1}ª CONTA", x, 255, 22, "black", GRAY, a, tracking=1)
        expr(c, q + " = ?", x, 360, 60, a)
        if t >= C["20"]:
            ra = ep(t, C["20." + "abcd"[k]], 0.5)
            expr(c, r, x, 590, 80, ra, cores={0: GREEN})
            text(c, why, x, 700, 26, "bold", INK2, ra)
    pause_timer(c, t, C["19.end"] - 1.9, W / 2, 600)


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Potência é multiplicar a base por ela mesma.", "Qualquer número, menos o zero, elevado a zero dá 1.",
          "Expoente negativo inverte; não deixa negativo."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["21", "28"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "21" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 170 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 46, "black", INK, a, 1340, 56)


ERROS = [("2³ = 6", "2 · 3 dá 6, e os dois números estão ali", "são 3 fatores: 2 · 2 · 2 = 8"),
         ("a⁰ = 0", "o zero costuma zerar tudo", "a escada mostra: um degrau abaixo do 2 vem o 1"),
         ("2⁻³ = −8 (ou qualquer resultado negativo)", "o sinal de menos está ali, bem à vista",
          "o menos do expoente só inverte: 2⁻³ = 1/8, positivo")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["22", "23", "24"], ERROS)


# ======================================================================
# Questão 3 do material
# ======================================================================

ALTS = [("A", "= -{41/4}", "achou que o negativo deixa negativo", RED), ("B", "= 17/36", "menor que 1: impossível", RED),
        ("C", "= 25/4", "fez 2³ como 2 · 2", RED), ("D", "= 41/4", "", GREEN), ("E", "= 12", "não inverteu a fração", RED)]
ENUNCIADO = ("O valor da expressão", "(2/3)^{-2} + (1/2)^{-3}", "é")


def b_questao(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · EXPOENTES NEGATIVOS", "PAUSE E TENTE", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["25.a"], 0.4)
    text(c, ENUNCIADO[0], 190, 250, 36, "black", INK, a0, align="left")
    expr(c, ENUNCIADO[1], 190, 340, 60, a0, align="left")
    text(c, ENUNCIADO[2], 640, 352, 36, "black", INK, a0, align="left")
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"25.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {"A": C["27.xa"], "B": C["27.xb"], "C": C["27.xc"], "E": C["27.xe"]}
    if t >= C["25.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS, 890, 200, 800, 40, C["26.ok"], "D", cues_in, cues_x, gap=14)
    pause_timer(c, t, C["25.end"] - 1.9, 470, 640)
    if t >= C["26"]:
        ra = ep(t, C["26"], 0.4)
        rrect(c, 170, 420, 680, 380, 18, "#FFFFFF", ra, shadow=True)
        expr(c, "(2/3)^{-2} = (3/2)^2 = 9/4", 510, 480, 38, ep(t, C["26.a"], 0.4), cores={4: GREEN})
        expr(c, "(1/2)^{-3} = 2^3 = 8", 510, 580, 38, ep(t, C["26.b"], 0.4), cores={4: GREEN})
        expr(c, "8 = 32/4", 510, 670, 38, ep(t, C["26.c"], 0.4))
        expr(c, "9/4 + 32/4 = 41/4", 510, 755, 40, ep(t, C["26.d"], 0.4), cores={4: GREEN})


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "AS SETE PROPRIEDADES", PURPLE)
    aa = ep(t, C["29.a"], 0.5)
    expr(c, "(2^5·4^3)/8^2 = ?", W / 2, 340, 96, aa)
    ab = ep(t, C["29.b"], 0.5)
    for k in range(7):
        a = ab * ep(t, C["29.b"] + 0.2 * k, 0.3)
        x = 400 + k * 187
        card(c, x - 75, 520, 150, 170, a)
        badge_num(c, k + 1, x, 570, a, 26, bg=PURPLE)
        text_mid(c, "?", x, 640, 50, "black", PURPLE, a)
    pill(c, "ep. 2 · as sete propriedades da potenciação", W / 2, 780, PURPLE, size=32, a=ep(t, C["29.c"], 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["30.like"], C["30.sub"], C["30.bell"], C["30.com"], C["30.bye"], "Você também achava que 2⁰ dava zero?",
        canal="no Estudativo", anki=C["30.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, papel=b_papel, erro_partida=b_erro_partida, um=b_um,
              escada=b_escada, negativo=b_negativo, fracao=b_fracao, nao_negativo=b_nao_negativo, sinal=b_sinal,
              exercicio=b_exercicio, recap=b_recap, erros=b_erros, questao=b_questao, ponte=b_ponte, cta=b_cta)
