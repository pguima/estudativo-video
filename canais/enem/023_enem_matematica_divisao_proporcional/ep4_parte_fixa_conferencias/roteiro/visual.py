"""Visual — Divisão Proporcional, Episódio 4: parte fixa, o que não é divisão proporcional e as 3 conferências (tema claro).
Peças comuns da série em ../../comum.py (reexporta o 019/comum.py: expr com frações, alternativas, erro_cards, atalho...).
Peças deste episódio: montinho() (a parte fixa: maço de notas que é separado e depois devolvido), registradora() (a caixa
registradora que "fecha o caixa"), taximetro() (a bandeirada da série de Grandezas), pacote()/linha()/pessoa() (do episódio 2),
porta() (as duas portas do gancho) e cartao() (as situações da seção 09).
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
_s = importlib.util.spec_from_file_location("comum023", _p)
K = importlib.util.module_from_spec(_s); _s.loader.exec_module(K)
K.usar_tempos(Path(__file__).resolve().parents[1] / "audio" / "tempos.json")
motor.set_theme("claro")
expr, fr = K.expr, K.fr
frame, head_seq, which, para, boxed, regra, selo, pause_timer, chip = (K.frame, K.head_seq, K.which, K.para, K.boxed, K.regra,
                                                                        K.selo, K.pause_timer, K.chip)
fmid, ftext = K.fmid, K.ftext

MARCA = ""
ARQUIVO_FINAL = "enem_matematica_divisao_ep4_parte_fixa_conferencias.mp4"
CARD_R = K.CARD_R
CAIXA = "#C98B4B"
NOTA = "#5FAE7A"
NOTA_ESC = "#3E8A5A"
EQUIPES = [("Equipe 1", "1 ponto", BLUE), ("Equipe 2", "2 pontos", PURPLE), ("Equipe 3", "3 pontos", AMBER)]


# ======================================================================
# peças do episódio
# ======================================================================

def montinho(c, x, y, s, a, label="R$ 1 000", col=NOTA, lsize=26):
    """maço de notas (a parte fixa) centrado em (x, y), com o valor embaixo"""
    if a <= 0:
        return
    w, h = s, s * 0.5
    for k in range(3):
        dx, dy = -6 + 6 * k, 10 - 10 * k
        rrect(c, x - w / 2 + dx, y - h / 2 + dy, w, h, 8, mix(col, "#FFFFFF", 0.12 * (2 - k)), a, shadow=(k == 0))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2 + dx, y - h / 2 + dy, w, h), 8, 8),
                    paint(NOTA_ESC, a * 0.6, stroke=2))
    c.drawCircle(x + 6, y - 10, h * 0.22, paint("#FFFFFF", a * 0.7, stroke=3))
    rrect(c, x - w * 0.12 + 6, y - h / 2 - 10, w * 0.24, h + 4, 4, "#F3D9A4", a)
    if label:
        text(c, label, x, y + h / 2 + lsize + 14, lsize, "black", NOTA_ESC, a)


def registradora(c, cx, cy, s, a, visor="", estado=None, k_est=1.0):
    """caixa registradora; estado True = "FECHOU" (verde), False = "NÃO FECHA" (vermelho), None = sem selo"""
    if a <= 0:
        return
    w, h = s, s * 0.78
    # corpo
    rrect(c, cx - w / 2, cy - h * 0.15, w, h * 0.62, 18, "#5B6472", a, shadow=True)
    # visor
    vw, vh = w * 0.78, h * 0.3
    rrect(c, cx - vw / 2, cy - h * 0.5, vw, vh, 12, "#2F3540", a)
    vcol = "#9CF0B5" if estado is None else (mix("#9CF0B5", "#7CE29C", 0.5) if estado else "#FF9C9C")
    ftext(c, visor, cx, cy - h * 0.5 + vh * 0.68, int(vh * 0.52), "black", vcol, a)
    line(c, cx, cy - h * 0.2, cx, cy - h * 0.15, "#2F3540", a, 10)
    # teclas
    for i in range(3):
        for j in range(4):
            kx = cx - w * 0.33 + j * w * 0.22
            ky = cy - h * 0.02 + i * h * 0.12
            rrect(c, kx - w * 0.07, ky - h * 0.04, w * 0.14, h * 0.08, 5, "#E8E8EC", a * 0.95)
    # gaveta
    rrect(c, cx - w * 0.55, cy + h * 0.47, w * 1.1, h * 0.2, 10, "#454C57", a)
    rrect(c, cx - w * 0.1, cy + h * 0.55, w * 0.2, h * 0.05, 3, "#C9CDD4", a)
    if estado is not None and k_est > 0:
        col = GREEN if estado else RED
        s_ = "FECHOU" if estado else "NÃO FECHA"
        pill(c, s_, cx, cy - h * 0.5 - 44, col, size=max(22, int(s * 0.1)), a=a * k_est, anchor="center", bounds=(0, 1920))


def taximetro(c, cx, cy, s, a, valor="R$ 6,00", km="km 0"):
    if a <= 0:
        return
    w, h = s, s * 0.55
    rrect(c, cx - w / 2, cy - h / 2, w, h, 18, "#2F3540", a, shadow=True)
    rrect(c, cx - w * 0.42, cy - h * 0.36, w * 0.84, h * 0.46, 10, "#121417", a)
    ftext(c, valor, cx, cy - h * 0.04, int(h * 0.3), "black", "#FFCF5C", a)
    text(c, km, cx, cy + h * 0.38, int(h * 0.17), "black", "#C9CDD4", a)


def pacote(c, x, y, s, col, a, abre=0.0, valor=None, vsize=30):
    """pacotinho fechado (laço) centrado em (x, y); abre = 0..1 levanta a tampa e mostra o valor"""
    if a <= 0:
        return
    sc = 0.85 + 0.15 * ease_back(clamp(a))
    w, h = s * sc, s * 0.8 * sc
    rrect(c, x - w / 2, y - h / 2, w, h, 10, col, a, shadow=True)
    lid = h * 0.28
    dy = -abre * s * 0.45
    rrect(c, x - w / 2 - 6, y - h / 2 - lid * 0.5 + dy, w + 12, lid, 8, mix(col, "#000000", 0.12), a)
    line(c, x, y - h / 2 + 8, x, y + h / 2, "#FFFFFF", a * 0.85, 6)
    line(c, x, y - h / 2 - lid * 0.5 + dy, x, y - h / 2 + lid * 0.5 + dy, "#FFFFFF", a * 0.85, 6)
    if abre > 0 and valor:
        text_mid(c, valor, x, y - h / 2 - s * 0.1 + dy * 0.2, vsize, "black", GREEN, a * clamp(abre * 1.6))


def pacotes(c, t, x0, y, n, a, ins=None, abre=0.0, valor=None, col=CAIXA, s=66, gap=80):
    for i in range(n):
        ai = a * (ep(t, ins + 0.15 * i, 0.35) if ins is not None else 1.0)
        pacote(c, x0 + i * gap, y, s, col, ai, abre, valor)


def linha(c, partes, cx, cy, size, a, peso="black", align="center"):
    """texto numa linha com cor por trecho: partes = [(texto, cor)] (mantém os espaços dos milhares)"""
    if a <= 0:
        return
    ws = [text_w(s_, peso, size) for s_, _ in partes]
    x = cx - sum(ws) / 2 if align == "center" else (cx if align == "left" else cx - sum(ws))
    for (s_, col), w_ in zip(partes, ws):
        text(c, s_, x, cy + size * 0.36, size, peso, col or INK, a, align="left")
        x += w_


def pessoa(c, cx, cy, s, col, a):
    """bonequinho simples: cabeça e tronco (cy = centro do tronco)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - s * 0.62, s * 0.26, paint(col, a))
    p = skia.Path(); p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s * 0.4, cy - s * 0.3, s * 0.8, s * 0.7), s * 0.3, s * 0.3))
    c.drawPath(p, paint(col, a))


def conferido(c, s, x, y, a, ok=True, size=32):
    """linha de conferência com ✓ (verde) ou ✗ (vermelho)"""
    if a <= 0:
        return
    check_icon(c, x, y - size * 0.32, size * 0.62, a, GREEN if ok else RED, "check" if ok else "x")
    ftext(c, s, x + size * 0.95, y, size, "black", GREEN if ok else RED, a, align="left")


def porta(c, cx, cy, w, h, aberta, a, col, rotulo):
    """porta vista de frente; aberta = 1 (entreaberta, estreita) → 0 (fechada, com tranca verde)"""
    if a <= 0:
        return
    rrect(c, cx - w / 2 - 12, cy - h / 2 - 12, w + 24, h + 12, 12, "#E6E1D8", a)
    ww = w * (1 - 0.7 * aberta)
    rrect(c, cx - w / 2, cy - h / 2, ww, h, 8, col, a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 16, cy - h / 2 + 18, ww - 32, h * 0.38), 6, 6),
                paint("#FFFFFF", a * 0.35, stroke=4))
    c.drawCircle(cx - w / 2 + ww - 22, cy + 10, 9, paint("#F3D9A4", a))
    para(c, rotulo, cx, cy + h / 2 + 50, 28, "black", INK, a, 300, 34, align="center")


def cartao(c, x, y, w, h, titulo, a, col):
    if a <= 0:
        return
    rrect(c, x, y, w, h, 22, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), paint(col, a, stroke=4))
    size = 26
    while text_w(titulo, "black", size) > w - 30:
        size -= 1
    text(c, titulo, x + w / 2, y + 52, size, "black", col, a)


def mono(s, col):
    return {i: col for i in range(len(s.split()))}


# ======================================================================
# abertura
# ======================================================================

def b_hook(c, t, C, B):
    head(c, t, B["start"], "MATEMÁTICA ENEM", "PARTE FIXA E CONFERÊNCIAS", BLUE)
    aa = ep(t, C["01.a"], 0.5)
    if aa > 0:
        for k, s in enumerate(("parte 1", "parte 2", "parte 3")):
            ak = aa * ep(t, C["01.a"] + 0.3 * k, 0.4)
            conferido(c, s + " calculada", 330, 290 + k * 70, ak, True, 34)
    ab = ep(t, C["01.b"], 0.5)
    if ab > 0:
        check_icon(c, 450, 560, 60, ab, RED, "x")
        text(c, "e erra a questão", 450, 670, 44, "black", RED, ab)
    fecha = ep(t, C["01.e"] + 0.2, 0.9)
    acc = ep(t, C["01.c"], 0.5)
    porta(c, 1040, 450, 230, 330, 1 - fecha, acc, AMBER, "uma PARTE FIXA escondida")
    ad = ep(t, C["01.d"], 0.5)
    porta(c, 1440, 450, 230, 330, 1 - fecha, ad, RED, "respondeu a PARTE ERRADA")
    ae = ep(t, C["01.e"], 0.5)
    if ae > 0:
        selo(c, 1240, 230, ae, "HOJE: FECHE AS DUAS PORTAS", GREEN, -3, 34)


def b_promessa(c, t, C, B):
    frame(c, t, B["start"], "AO FINAL DESTA AULA", "VOCÊ VAI CONSEGUIR", GREEN)
    rows = [("02.a", "reconhecer quando a proporção NÃO vale sobre o total", "a parte fixa e outras pegadinhas"),
            ("02.b", "usar 3 conferências que pegam quase qualquer erro", "fechar o caixa · a ordem · o que foi pedido")]
    for j, (cue, s, sub) in enumerate(rows):
        a, d = rise(t, C[cue])
        y = 340 + j * 220 + d
        check_icon(c, 230, y - 14, 34, a, GREEN)
        text(c, s, 290, y, 48, "black", INK, a, align="left")
        text(c, sub, 290, y + 60, 34, "bold", GRAY, a, align="left")
    a0 = ep(t, C["02.b"] + 0.6, 0.5)
    registradora(c, 1600, 720, 200, a0 * 0.95, "OK", True, a0)


def b_prereq(c, t, C, B):
    frame(c, t, B["start"], "TRÊS LEMBRETES", "EM 30 SEGUNDOS", GREEN)
    aa = ep(t, C["03.a"], 0.5)
    if aa > 0:
        pill(c, "EPISÓDIO 1", 420, 250, GRAY, size=22, a=aa, anchor="center", bounds=(0, 1920))
        text(c, "PACOTINHOS", 420, 330, 40, "black", PURPLE, aa)
        pacotes(c, t, 340, 450, 3, aa, C["03.a"] + 0.3)
        text(c, "some · divida · multiplique", 420, 580, 30, "black", INK2, aa)
        text(c, "cada pacotinho vale k", 420, 640, 30, "black", GREEN, aa)
    ab = ep(t, C["03.b"], 0.5)
    if ab > 0:
        pill(c, "EPISÓDIO 2", 960, 250, GRAY, size=22, a=ab, anchor="center", bounds=(0, 1920))
        text(c, "INVERSA", 960, 330, 40, "black", BLUE, ab)
        alt = [180, 120, 90]
        for k, n in enumerate((2, 3, 4)):
            x = 860 + k * 100
            hh = alt[k] * ep(t, C["03.b"] + 0.3 * k, 0.5)
            rrect(c, x - 34, 560 - hh, 68, hh, 10, GREEN if k == 0 else mix(BLUE, "#FFFFFF", 0.3), ab)
            text(c, str(n), x, 600, 30, "black", INK, ab)
        text(c, "menor número, maior parte", 960, 660, 30, "black", INK2, ab)
    acc = ep(t, C["03.c"], 0.5)
    if acc > 0:
        pill(c, "SÉRIE DE GRANDEZAS", 1500, 250, GRAY, size=22, a=acc, anchor="center", bounds=(0, 1920))
        text(c, "BANDEIRADA", 1500, 330, 40, "black", AMBER, acc)
        taximetro(c, 1500, 460, 260, acc)
        text(c, "fixa: fica FORA", 1500, 600, 30, "black", INK2, acc)
        text(c, "da proporção", 1500, 645, 30, "black", INK2, acc)
    line(c, 690, 230, 690, 800, "#E6E6E2", aa, 3)
    line(c, 1230, 230, 1230, 800, "#E6E6E2", ab, 3)


# ======================================================================
# concreto — a gincana
# ======================================================================

def b_gincana(c, t, C, B):
    head_seq(c, t, C, [("04", "A GINCANA", "R$ 6 000 PARA 3 EQUIPES", BLUE), ("05", "DEFINIÇÃO", "PARTE FIXA E RESTANTE", BLUE)])
    card(c, *CARD_R)
    sid = which(t, C, ["04", "05"])
    if sid == "04":
        a0 = ep(t, C["04"], 0.5)
        chip(c, "prêmio: R$ 6 000", W / 2, 222, INK2, a0, 34)
        for k, (nome, pts, col) in enumerate(EQUIPES):
            x = 400 + k * 330
            ak = a0 * ep(t, C["04"] + 0.25 * k, 0.4)
            pessoa(c, x, 360, 120, col, ak)
            text(c, nome, x, 460, 32, "black", INK, ak)
            montinho(c, x, 560, 120, ep(t, C["04.a"] + 0.3 * k, 0.45), "R$ 1 000")
            ab = ep(t, C["04.b"] + 0.3 * k, 0.45)
            if ab > 0:
                chip(c, pts, x, 690, col, ab, 30)
        if ep(t, C["04.a"], 0.5) > 0:
            ap = ep(t, C["04.a"] + 1.0, 0.5)
            text(c, "só por", 1200, 550, 24, "bold", NOTA_ESC, ap)
            text(c, "participar", 1200, 580, 24, "bold", NOTA_ESC, ap)
        ab = ep(t, C["04.b"], 0.5)
        if ab > 0:
            text(c, "o RESTO conforme os pontos", 730, 760, 30, "black", PURPLE, ab)
        acc = ep(t, C["04.c"], 0.5) * (1 - ep(t, C["04.d"], 0.4))
        if acc > 0:
            boxed(c, 1300, 300, 420, 220, AMBER, acc, 0.08)
            text(c, "A TENTAÇÃO", 1510, 350, 26, "black", AMBER, acc)
            linha(c, [("6 000 em 1 : 2 : 3", INK)], 1510, 420, 38, acc)
            text(c, "direto?", 1510, 490, 30, "black", AMBER, acc)
        ad = ep(t, C["04.d"], 0.5)
        if ad > 0:
            boxed(c, 1300, 300, 420, 260, PURPLE, ad, 0.08)
            text(c, "a proporção vale", 1510, 360, 32, "black", PURPLE, ad)
            text(c, "SÓ SOBRE O RESTO", 1510, 420, 38, "black", PURPLE, ad)
            strike(c, 1360, 495, 1660, 495, ad, RED, ep(t, C["04.d"] + 0.3, 0.4))
            text(c, "não sobre o total", 1510, 505, 28, "bold", RED, ad)
        return
    a0 = ep(t, C["05"], 0.5)
    boxed(c, 220, 220, 700, 200, BLUE, a0, 0.08)
    text(c, "PARTE FIXA", 570, 280, 42, "black", BLUE, a0)
    aa = ep(t, C["05.a"], 0.5)
    text(c, "valor IGUAL para todos,", 570, 340, 30, "bold", INK2, aa)
    text(c, "ANTES de qualquer proporção", 570, 384, 30, "bold", INK2, aa)
    montinho(c, 570, 540, 150, a0, "R$ 1 000")
    ab = ep(t, C["05.b"], 0.5)
    boxed(c, 1000, 220, 700, 200, BLUE, ab, 0.08)
    text(c, "RESTANTE", 1350, 280, 42, "black", BLUE, ab)
    text(c, "o que SOBRA depois", 1350, 340, 30, "bold", INK2, ab)
    text(c, "de tirar os fixos", 1350, 384, 30, "bold", INK2, ab)
    if ab > 0:
        linha(c, [("6 000 − 3 000 = ", INK), ("3 000", PURPLE)], 1350, 520, 46, ab)
    acc = ep(t, C["05.c"], 0.5)
    if acc > 0:
        taximetro(c, 1350, 660, 220, acc)
        text(c, "bandeirada", 1530, 680, 28, "black", AMBER, acc, align="left")
    ad = ep(t, C["05.d"], 0.5)
    if ad > 0:
        regra(c, "a parte fixa fica FORA da divisão", 570, 760, ad, 34)


# ======================================================================
# bloco A — separe, divida, devolva
# ======================================================================

ROW_Y = [340, 490, 640]
PARTES_G = ["500", "1 000", "1 500"]
TOTAIS_G = ["1 500", "2 000", "2 500"]


def _equipes_col(c, a):
    for k, (nome, pts, col) in enumerate(EQUIPES):
        y = ROW_Y[k]
        text(c, nome, 200, y + 2, 32, "black", col, a, align="left")
        text(c, f"peso {k + 1}", 200, y + 42, 24, "bold", GRAY, a, align="left")


def b_fixa(c, t, C, B):
    head_seq(c, t, C, [("06", "SEPARE E DIVIDA", "OS PASSOS 1 E 2", PURPLE), ("07", "DEVOLVA", "O PASSO 3", PURPLE),
                       ("08", "E SE ERRAR?", "OS DOIS CAMINHOS ERRADOS", RED)])
    card(c, *CARD_R)
    sid = which(t, C, ["06", "07", "08"])
    if sid in ("06", "07"):
        a0 = ep(t, C["06"], 0.5)
        _equipes_col(c, a0)
        # os 3 montinhos fixos: separados (canto direito) e, na cena 07, devolvidos para cada equipe
        sep = ep(t, C["06.a"], 0.6)
        dev = ep(t, C["07.a"] + 0.3, 0.9) if sid == "07" else 0
        for k in range(3):
            xs, ys = 1600, 300 + k * 110
            xd, yd = 420, ROW_Y[k]
            x = lerp(xs, xd, dev)
            y = lerp(ys, yd, dev) - 70 * math.sin(math.pi * dev)
            montinho(c, x, y, 110, sep * ep(t, C["06.a"] + 0.2 * k, 0.4), "R$ 1 000" if dev < 0.5 else "", lsize=22)
        if sid == "06" and sep > 0:
            text(c, "FIXOS SEPARADOS", 1600, 245, 24, "black", NOTA_ESC, sep)
            linha(c, [("3 × 1 000 = ", INK), ("3 000", NOTA_ESC)], 1600, 660, 32, ep(t, C["06.a"] + 0.6, 0.4))
            linha(c, [("6 000 − 3 000 = ", INK), ("3 000", PURPLE)], 1600, 720, 28, ep(t, C["06.a"] + 1.4, 0.4))
            text(c, "restante", 1600, 775, 24, "bold", PURPLE, ep(t, C["06.a"] + 1.4, 0.4))
        ab = ep(t, C["06.b"], 0.5)
        abre = ep(t, C["06.b"] + 2.2, 0.6)
        for k in range(3):
            pacotes(c, t, 560, ROW_Y[k], k + 1, ab, C["06.b"] + 0.3 * k, abre, "500", s=60, gap=74)
        if sid == "06" and ab > 0:
            rrect(c, 1010, 560, 400, 200, 22, "#FFFFFF", ab, shadow=True)
            text(c, "1 + 2 + 3 = 6", 1210, 620, 38, "black", INK, ab)
            linha(c, [("3 000 ÷ 6 = ", INK), ("500", GREEN)], 1210, 690, 38, ep(t, C["06.b"] + 1.4, 0.4))
            text(c, "k, o valor de 1 pacotinho", 1210, 745, 22, "bold", GREEN, ep(t, C["06.b"] + 1.4, 0.4))
        acc = ep(t, C["06.c"], 0.5)
        for k in range(3):
            linha(c, [("= ", INK2), (PARTES_G[k], PURPLE)], 900, ROW_Y[k], 38,
                  acc * ep(t, C["06.c"] + 0.6 * k, 0.4) * (1 if sid == "06" else 0))
        if sid == "07":
            for k in range(3):
                ab_ = ep(t, C["07.b"] + 0.9 * k, 0.5)
                linha(c, [("1 000 + ", NOTA_ESC), (PARTES_G[k], PURPLE), (" = ", INK2), (TOTAIS_G[k], GREEN)], 1150, ROW_Y[k], 38, ab_)
            acc2 = ep(t, C["07.c"], 0.5)
            registradora(c, 1600, 520, 200, acc2, "6 000", True if acc2 > 0.3 else None, ep(t, C["07.c"] + 0.6, 0.4))
            ad = ep(t, C["07.d"], 0.5)
            K.atalho(c, 300, 718, 1100, 110, "ATALHO", ["separe  ·  divida  ·  devolva"], ad, 38)
        return
    # 08 — os dois caminhos errados
    a0 = ep(t, C["08"], 0.5)
    pill(c, "ERRADO 1 · DIVIDIU O TOTAL", 540, 230, RED, size=24, a=a0, anchor="center", bounds=(0, 1920))
    aa = ep(t, C["08.a"], 0.5)
    if aa > 0:
        linha(c, [("6 000 ÷ 6 = 1 000", INK)], 540, 320, 40, aa)
        linha(c, [("1 000 · 2 000 · 3 000", RED)], 540, 400, 42, ep(t, C["08.a"] + 1.2, 0.4))
    ab = ep(t, C["08.b"], 0.5)
    if ab > 0:
        conferido(c, "a soma fecha: 6 000", 300, 500, ab, True, 30)
        conferido(c, "Equipe 1: 1 000, e não 1 500", 300, 570, ep(t, C["08.b"] + 0.6, 0.4), False, 30)
        text(c, "R$ 500 a menos do que manda o regulamento", 540, 650, 24, "bold", RED, ep(t, C["08.b"] + 0.6, 0.4))
    line(c, 960, 230, 960, 800, "#E6E6E2", a0, 3)
    acc = ep(t, C["08.c"], 0.5)
    if acc > 0:
        pill(c, "ERRADO 2 · NÃO DEVOLVEU O FIXO", 1370, 230, RED, size=24, a=acc, anchor="center", bounds=(0, 1920))
        linha(c, [("500 + 1 000 + 1 500", INK)], 1370, 320, 40, acc)
        linha(c, [("= 3 000", RED)], 1370, 390, 42, ep(t, C["08.c"] + 1.0, 0.4))
    ad = ep(t, C["08.d"], 0.5)
    registradora(c, 1370, 610, 210, ad, "3 000", False if ad > 0.3 else None, ep(t, C["08.d"] + 0.3, 0.4))


# ======================================================================
# bloco B — o que parece divisão proporcional e não é
# ======================================================================

CARTOES = [("IMPOSTO POR FAIXAS", AMBER), ("RATEIO COM MÍNIMO", AMBER), ("HERANÇA COM LEGÍTIMA", AMBER),
           ("DESCONTO ESCALONADO", AMBER)]


def _cartoes(c, t, C, B):
    xs = [190, 590, 990, 1390]
    w, h = 360, 400
    y = 260
    cues = ["09.b", "09.c", "10.a", "10.b"]
    for k, (tit, col) in enumerate(CARTOES):
        if t < C[cues[k]] - 0.2:
            continue
        a = ep(t, C[cues[k]], 0.5)
        x = xs[k]
        cartao(c, x, y, w, h, tit, a, col)
        cx = x + w / 2
        if k == 0:   # degraus com alíquotas diferentes
            for j, (p, hh) in enumerate((("0%", 50), ("7%", 90), ("15%", 130), ("27%", 170))):
                bx = x + 40 + j * 72
                rrect(c, bx, 560 - hh, 60, hh, 8, mix(AMBER, "#FFFFFF", 0.5 - 0.12 * j), a)
                text(c, p, bx + 30, 550 - hh, 22, "black", INK, a)
            text(c, "cada faixa, uma alíquota", cx, 610, 22, "black", INK2, a)
            text(c, "sem k único", cx, 640, 24, "black", RED, a)
        elif k == 1:
            montinho(c, cx - 70, 420, 90, a, "")
            montinho(c, cx + 70, 420, 90, a, "")
            text(c, "parcela fixa de todos", cx, 540, 22, "black", INK2, a)
            text(c, "= a nossa parte fixa", cx, 600, 24, "black", NOTA_ESC, a)
        elif k == 2:
            K.pizza(c, cx, 440, 100, 4, 1, a, sel_col=mix(BLUE, "#FFFFFF", 0.2))
            text(c, "uma parte reservada", cx, 590, 22, "black", INK2, a)
            text(c, "por lei", cx, 625, 24, "black", BLUE, a)
        else:
            for j, (p, n) in enumerate((("5%", "1 a 10"), ("10%", "11 a 50"), ("15%", "51 +"))):
                bx = x + 40 + j * 100
                hh = 70 + 50 * j
                rrect(c, bx, 560 - hh, 84, hh, 8, mix(GREEN, "#FFFFFF", 0.4 - 0.12 * j), a)
                text(c, p, bx + 42, 550 - hh, 24, "black", INK, a)
                text(c, n, bx + 42, 590, 18, "bold", GRAY, a)
            text(c, "% muda em degraus", cx, 635, 24, "black", RED, a)


def b_parece(c, t, C, B):
    head_seq(c, t, C, [("09", "PARECE, MAS NÃO É", "SEÇÃO 09 DO MATERIAL", AMBER), ("10", "PARECE, MAS NÃO É", "MAIS DOIS CASOS", AMBER)])
    card(c, *CARD_R)
    aa = ep(t, C["09.a"], 0.5) * (1 - ep(t, C["09.b"], 0.4))
    if aa > 0:
        text(c, "cara de divisão proporcional...", W / 2, 420, 50, "black", INK, aa)
        text(c, "...mas não é", W / 2, 500, 50, "black", AMBER, aa)
    _cartoes(c, t, C, B)
    if t >= C["10"]:
        acc = ep(t, C["10.c"], 0.5)
        if acc > 0:
            regra(c, "leia a REGRA antes de dividir", W / 2, 750, acc, 40)


def b_iguais(c, t, C, B):
    head(c, t, B["start"], "PARTES IGUAIS", "UM CASO PARTICULAR", BLUE)
    card(c, *CARD_R)
    aa = ep(t, C["11.a"], 0.5)
    if aa > 0:
        text(c, "pesos", 400, 290, 34, "black", INK2, aa)
        ftext(c, "1 · 1 · 1", 400, 370, 70, "black", PURPLE, aa)
        text(c, "a MESMA regra", 400, 450, 30, "black", PURPLE, aa)
    ab = ep(t, C["11.b"], 0.5)
    if ab > 0:
        chip(c, "R$ 900 entre 3 amigos", 1150, 260, INK2, ab, 32)
        for k, col in enumerate((BLUE, PURPLE, AMBER)):
            x = 900 + k * 250
            pessoa(c, x, 430, 110, col, ab)
            pacote(c, x, 560, 76, CAIXA, ab, ep(t, C["11.b"] + 1.6, 0.5), "300")
        linha(c, [("900 ÷ 3 = ", INK), ("300", GREEN)], 1150, 690, 42, ep(t, C["11.b"] + 1.0, 0.4))
        text(c, "cada um leva um pacotinho", 1150, 760, 28, "bold", GREEN, ep(t, C["11.b"] + 1.6, 0.4))


# ======================================================================
# as três conferências
# ======================================================================

def b_conf1(c, t, C, B):
    head(c, t, B["start"], "CONFERÊNCIA 1", "FECHAR O CAIXA", GREEN)
    card(c, *CARD_R)
    a0 = ep(t, C["12"], 0.5)
    boxed(c, 220, 210, 720, 100, BLUE, a0, 0.08)
    text(c, "CONFERIR = checar antes de marcar", 580, 272, 32, "black", BLUE, a0)
    aa = ep(t, C["12.a"], 0.5)
    ab = ep(t, C["12.b"], 0.5)
    fecha = ep(t, C["12.b"] + 1.6, 0.4)
    registradora(c, 1380, 520, 300, aa, "6 000" if ab > 0.3 else "", True if fecha > 0 else None, fecha)
    if aa > 0:
        text(c, "como numa loja, no fim do dia", 1380, 800, 26, "bold", GRAY, aa)
    if ab > 0:
        for k, s in enumerate(("1 500", "+ 2 000", "+ 2 500")):
            ftext(c, s, 760, 400 + k * 70, 48, "black", INK, ab * ep(t, C["12.b"] + 0.3 * k, 0.4), align="right")
        line(c, 480, 600, 780, 600, INK, ab, 4)
        ftext(c, "6 000", 760, 665, 52, "black", GREEN, fecha, align="right")
        text(c, "= o total?", 880, 665, 30, "black", GREEN, fecha)
    acc = ep(t, C["12.c"], 0.5)
    if acc > 0:
        conferido(c, "não deu? erro no k ou nos pesos", 300, 760, acc, False, 30)


def b_conf2(c, t, C, B):
    head(c, t, B["start"], "CONFERÊNCIA 2", "A ORDEM FAZ SENTIDO?", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["13.a"], 0.5)
    pill(c, "DIRETA", 540, 230, PURPLE, size=26, a=aa, anchor="center", bounds=(0, 1920))
    if aa > 0:
        text(c, "maior PESO → maior parte", 540, 300, 30, "black", INK2, aa)
        for k, (v, hh) in enumerate(zip(TOTAIS_G, (150, 200, 250))):
            x = 380 + k * 160
            h_ = hh * ep(t, C["13.a"] + 0.3 * k, 0.5)
            rrect(c, x - 55, 660 - h_, 110, h_, 12, EQUIPES[k][2], aa * 0.85)
            text(c, v, x, 645 - h_, 28, "black", INK, aa)
            text(c, f"peso {k + 1}", x, 705, 24, "black", EQUIPES[k][2], aa)
        check_icon(c, 790, 400, 32, ep(t, C["13.a"] + 1.6, 0.4), GREEN)
    line(c, 960, 230, 960, 760, "#E6E6E2", aa, 3)
    ab = ep(t, C["13.b"], 0.5)
    pill(c, "INVERSA", 1380, 230, BLUE, size=26, a=ab, anchor="center", bounds=(0, 1920))
    if ab > 0:
        text(c, "MENOR número → maior parte", 1380, 300, 30, "black", INK2, ab)
        for k, (n, v, hh) in enumerate(((2, "1 200", 250), (3, "800", 170), (4, "600", 130))):
            x = 1220 + k * 160
            h_ = hh * ep(t, C["13.b"] + 0.3 * k, 0.5)
            rrect(c, x - 55, 660 - h_, 110, h_, 12, GREEN if k == 0 else mix(BLUE, "#FFFFFF", 0.3), ab * 0.85)
            text(c, v, x, 645 - h_, 28, "black", INK, ab)
            text(c, f"{n} faltas", x, 705, 24, "black", INK2, ab)
        text(c, "o bônus do episódio 2", 1380, 740, 22, "bold", GRAY, ab)
    acc = ep(t, C["13.c"], 0.5)
    if acc > 0:
        selo(c, 760, 800, acc, "ORDEM AO CONTRÁRIO? VOCÊ TROCOU O MÉTODO", AMBER, -2, 28)


def b_conf3(c, t, C, B):
    head(c, t, B["start"], "CONFERÊNCIA 3", "RELEIA O QUE FOI PEDIDO", GREEN)
    card(c, *CARD_R)
    aa = ep(t, C["14.a"], 0.5)
    for k, s in enumerate(("a MENOR parte?", "a do SEGUNDO?", "a DIFERENÇA?")):
        chip(c, s, 420 + k * 420, 260, AMBER, aa * ep(t, C["14.a"] + 0.5 * k, 0.4), 34)
    ab = ep(t, C["14.b"], 0.5)
    if ab > 0:
        text(c, "quanto a Equipe 3 recebeu A MAIS que a Equipe 1?", W / 2, 370, 34, "black", INK, ab)
        for k, (v, hh, col) in enumerate((("1 500", 150, BLUE), ("2 500", 250, AMBER))):
            x = 640 + k * 260
            rrect(c, x - 70, 700 - hh, 140, hh, 12, col, ab * 0.85)
            text(c, v, x, 685 - hh, 30, "black", INK, ab)
            text(c, f"Equipe {1 + 2 * k}", x, 740, 24, "black", col, ab)
        dif = ep(t, C["14.b"] + 1.4, 0.5)
        if dif > 0:
            rrect(c, 830, 450, 140, 100, 12, GREEN, 0.25 * dif)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(830, 450, 140, 100), 12, 12), paint(GREEN, dif, stroke=4))
            linha(c, [("2 500 − 1 500 = ", INK), ("1 000", GREEN)], 1360, 520, 46, dif)
            text(c, "a diferença, não uma parte", 1360, 590, 26, "bold", GREEN, dif)
    acc = ep(t, C["14.c"], 0.5)
    if acc > 0:
        boxed(c, 1080, 640, 600, 160, GREEN, acc, 0.08)
        text(c, "ATALHO", 1380, 680, 22, "black", GREEN, acc, tracking=2)
        text(c, "sublinhe o que foi pedido", 1380, 730, 32, "black", INK, acc)
        line(c, 1210, 745, 1550, 745, GREEN, acc * ep(t, C["14.c"] + 0.5, 0.4), 5)
        text(c, "antes de calcular", 1380, 780, 28, "black", INK, acc)


def b_arred(c, t, C, B):
    head(c, t, B["start"], "UM CUIDADO EXTRA", "NÃO ARREDONDE O k", AMBER)
    card(c, *CARD_R)
    a0 = ep(t, C["15"], 0.5)
    aa = ep(t, C["15.a"], 0.5)
    if aa > 0:
        linha(c, [("R$ 2 000 em 1, 2 e 4  →  soma 7", INK)], W / 2, 230, 38, aa)
        linha(c, [("k = 2 000 ÷ 7 = ", INK), ("285,714…", AMBER)], W / 2, 300, 44, ep(t, C["15.a"] + 1.2, 0.4))
    ab = ep(t, C["15.b"], 0.5)
    if ab > 0:
        pill(c, "k ARREDONDADO: 286", 540, 390, RED, size=24, a=ab, anchor="center", bounds=(0, 1920))
        for k, s in enumerate(("286", "+ 572", "+ 1 144")):
            ftext(c, s, 640, 470 + k * 60, 40, "black", INK, ab * ep(t, C["15.b"] + 0.3 * k, 0.4), align="right")
        line(c, 400, 640, 660, 640, INK, ab, 3)
        ftext(c, "2 002", 640, 695, 44, "black", RED, ep(t, C["15.b"] + 1.2, 0.4), align="right")
        registradora(c, 820, 590, 150, ep(t, C["15.b"] + 1.4, 0.4), "2 002", False, ep(t, C["15.b"] + 1.6, 0.4))
    line(c, 960, 360, 960, 790, "#E6E6E2", ab, 3)
    acc = ep(t, C["15.c"], 0.5)
    if acc > 0:
        pill(c, "k EXATO: 2 000/7", 1380, 390, GREEN, size=24, a=acc, anchor="center", bounds=(0, 1920))
        for k, s in enumerate(("285,71", "+ 571,43", "+ 1 142,86")):
            ftext(c, s, 1500, 470 + k * 60, 40, "black", INK, acc * ep(t, C["15.c"] + 0.3 * k, 0.4), align="right")
        line(c, 1240, 640, 1520, 640, INK, acc, 3)
        ftext(c, "2 000,00", 1500, 695, 44, "black", GREEN, ep(t, C["15.c"] + 1.2, 0.4), align="right")
        registradora(c, 1660, 590, 150, ep(t, C["15.c"] + 1.4, 0.4), "2 000", True, ep(t, C["15.c"] + 1.6, 0.4))
        text(c, "arredonde só as partes, no fim", 1380, 780, 26, "black", GREEN, ep(t, C["15.c"] + 1.8, 0.4))


# ======================================================================
# nós fazemos
# ======================================================================

def b_exercicio(c, t, C, B):
    head_seq(c, t, C, [("16", "SUA VEZ", "PAUSE E CALCULE", GREEN), ("17", "VAMOS CONFERIR", "SEPARE · DIVIDA · DEVOLVA", GREEN)])
    card(c, *CARD_R)
    conf = t >= C["17"]
    aa = ep(t, C["16.a"], 0.5)
    if aa > 0:
        y0 = 260 if not conf else 230
        linha(c, [("R$ 5 000", INK), (" entre 2 pessoas", INK2)], W / 2, y0, 44 if not conf else 34, aa)
        linha(c, [("R$ 500 fixos", NOTA_ESC), (" para cada  ·  resto em ", INK2), ("1 : 3", PURPLE)], W / 2, y0 + 70 if not conf else y0 + 52,
              40 if not conf else 30, aa)
    ab = ep(t, C["16.b"], 0.5) * (1 - (ep(t, C["17"], 0.3) if conf else 0))
    if ab > 0:
        text(c, "quanto recebe cada uma?", W / 2, 440, 40, "black", BLUE, ab)
        for k, col in enumerate((BLUE, AMBER)):
            pessoa(c, 820 + k * 280, 580, 110, col, ab)
    pause_timer(c, t, C["16.end"] - 1.9, W / 2, 720)
    if not conf:
        return
    rows = [("17.a", [("1  SEPARE   ", PURPLE), ("5 000 − 1 000 = ", INK), ("4 000", PURPLE)]),
            ("17.b", [("2  DIVIDA   ", PURPLE), ("4 000 ÷ 4 = ", INK), ("1 000", GREEN), ("  (k)", GREEN)]),
            ("17.c", [("3  DEVOLVA   ", PURPLE), ("500 + 1 000 = ", INK), ("1 500", GREEN), ("   ·   500 + 3 000 = ", INK),
                      ("3 500", GREEN)])]
    for k, (cue, partes) in enumerate(rows):
        linha(c, partes, 220, 370 + k * 105, 38, ep(t, C[cue], 0.5), align="left")
    ad = ep(t, C["17.d"], 0.5)
    if ad > 0:
        linha(c, [("1 500 + 3 500 = ", INK), ("5 000", GREEN)], 640, 720, 44, ad)
        registradora(c, 1500, 620, 190, ad, "5 000", True, ep(t, C["17.d"] + 0.6, 0.4))


# ======================================================================
# recap, erros
# ======================================================================

FRASES = ["Parte fixa? Separe antes, devolva depois.", "A soma das partes tem que fechar o caixa.",
          "Releia o que foi pedido antes de marcar."]


def b_recap(c, t, C, B):
    sid = which(t, C, ["18", "26"])
    frame(c, t, B["start"], "3 FRASES-CHAVE", "PARA GUARDAR" if sid == "18" else "PARA FECHAR", PURPLE)
    for k, s in enumerate(FRASES):
        a, d = rise(t, C[f"{sid}.{'abc'[k]}"])
        y = 300 + k * 180 + d
        badge_num(c, k + 1, 260, y - 16, a, 36, bg=PURPLE)
        para(c, s, 320, y, 50, "black", INK, a, 1360, 60)


ERROS = [("Aplicar a proporção sobre o TOTAL quando há parte fixa", "a soma das partes até fecha",
          "o regulamento manda dividir só o RESTO: separe o fixo primeiro"),
         ("Esquecer de DEVOLVER a parte fixa no fim", "as contas da proporção estão perfeitas",
          "a soma dá só o restante: o caixa denuncia, some o fixo de volta"),
         ("Arredondar o k no meio do caminho", "a diferença é de centavos",
          "os centavos se multiplicam e a soma não fecha: arredonde só no fim"),
         ("Calcular tudo certo e responder a PARTE ERRADA", "o número achado está lá, nas alternativas",
          "ele responde OUTRA pergunta: releia o que foi pedido")]


def b_erros(c, t, C, B):
    K.erro_cards(c, t, C, ["19", "20", "21", "22"], ERROS)


# ======================================================================
# Questão 7 do material
# ======================================================================

def _enunciado(c, linhas, a, y0=250, size=30, w=700):
    y = y0
    for s, col in linhas:
        for ln in K.wrap(s, "black", size, w):
            text(c, ln, 190, y, size, "black", col, a, align="left")
            y += size + 12
        y += 8
    return y


ALTS7 = [("A", "R$ 3.500,00", "esqueceu de devolver o fixo", RED), ("B", "R$ 4.000,00", "não segue o regulamento", RED),
         ("C", "R$ 4.500,00", "", GREEN), ("D", "R$ 5.000,00", "proporção sobre os 10 000", RED),
         ("E", "R$ 6.000,00", "sobre o total e + o fixo", RED)]


def b_q7(c, t, C, B):
    head(c, t, B["start"], "QUESTÃO · PAUSE E TENTE", "PARTE FIXA ANTES DA PROPORÇÃO", BLUE)
    card(c, *CARD_R)
    a0 = ep(t, C["23.a"], 0.4)
    _enunciado(c, [("Uma quantia de R$ 10.000,00 será distribuída entre três pessoas da seguinte forma: cada uma recebe "
                    "inicialmente R$ 1.000,00 e o restante é dividido em partes diretamente proporcionais a 2, 3 e 5.", INK),
                   ("A terceira pessoa receberá, no total,", BLUE)], a0, 240)
    text(c, "Questão do material de estudo (seção 12)", 190, 822, 18, "medium", GRAY, a0, align="left")
    cues_in = {L: C[f"23.q{L.lower()}"] for L in "ABCDE"}
    cues_x = {L: C[f"25.x{L.lower()}"] for L in "ABDE"}
    if t >= C["23.qa"] - 0.3:
        K.alternativas(c, t, C, ALTS7, 1000, 240, 680, 42, C["24.ok"], "C", cues_in, cues_x, gap=30)
    pause_timer(c, t, C["23.end"] - 1.9, 540, 690)
    if t >= C["24"]:
        ra = ep(t, C["24"], 0.4)
        rrect(c, 170, 500, 740, 310, 18, "#FFFFFF", ra, shadow=True)
        if t < C["25"]:
            linha(c, [("1 ", PURPLE), ("10 000 − 3 000 = ", INK), ("7 000", PURPLE)], 540, 560, 36, ep(t, C["24.a"], 0.4))
            linha(c, [("2 ", PURPLE), ("7 000 ÷ 10 = ", INK), ("700", GREEN), (" (k)", GREEN)], 540, 625, 36, ep(t, C["24.b"], 0.4))
            linha(c, [("5 × 700 = ", INK), ("3 500", PURPLE)], 540, 690, 36, ep(t, C["24.c"], 0.4))
            linha(c, [("3 ", PURPLE), ("1 000 + 3 500 = ", INK), ("4 500", GREEN)], 540, 760, 38, ep(t, C["24.d"], 0.4))
        else:
            ab = ep(t, C["25"], 0.4)
            text(c, "FECHANDO O CAIXA", 400, 560, 26, "black", PURPLE, ab)
            linha(c, [("2 400 + 3 100 + 4 500", INK)], 400, 640, 34, ep(t, C["25.a"], 0.4))
            linha(c, [("= 10 000", GREEN)], 400, 710, 38, ep(t, C["25.a"] + 0.8, 0.4))
            registradora(c, 780, 680, 150, ep(t, C["25.a"] + 0.8, 0.4), "10 000", True, ep(t, C["25.a"] + 1.2, 0.4))


# ======================================================================
# ponte e CTA
# ======================================================================

def b_ponte(c, t, C, B):
    frame(c, t, B["start"], "PRÓXIMO EPISÓDIO", "A REVISÃO", PURPLE)
    aa = ep(t, C["27.a"], 0.5)
    if aa > 0:
        # os 4 ícones dos episódios
        pacotes(c, t, 390, 400, 3, aa, C["27.a"], s=60, gap=74)
        text(c, "pacotinhos", 464, 500, 26, "black", INK2, aa)
        expr(c, "1/2", 820, 400, 80, aa, cores={0: GREEN})
        text(c, "fração virando", 820, 500, 26, "black", INK2, aa)
        for i in range(2):
            for j in range(5):
                rrect(c, 1080 + j * 42, 360 + i * 42, 38, 38, 6, mix(BLUE, "#FFFFFF", 0.3), aa)
        text(c, "pessoa-dia", 1180, 500, 26, "black", INK2, aa)
        montinho(c, 1540, 400, 110, aa, "")
        text(c, "parte fixa", 1540, 500, 26, "black", INK2, aa)
    ab = ep(t, C["27.b"], 0.5)
    if ab > 0:
        selo(c, 700, 640, ab, "PEGADINHAS", AMBER, -4, 40)
    acc = ep(t, C["27.c"], 0.5)
    if acc > 0:
        chip(c, "questões novas", 1240, 640, GREEN, acc, 40)
    pill(c, "ep. 5 · revisão geral", W / 2, 780, PURPLE, size=32, a=ep(t, C["27.c"] + 0.6, 0.5), anchor="center")


def b_cta(c, t, C, B):
    cta(c, t, C["28.like"], C["28.sub"], C["28.bell"], C["28.com"], C["28.bye"], "Já esqueceu de devolver a parte fixa?",
        canal="no Estudativo", anki=C["28.anki"])


BLOCKS = dict(hook=b_hook, promessa=b_promessa, prereq=b_prereq, gincana=b_gincana, fixa=b_fixa, parece=b_parece,
              iguais=b_iguais, conf1=b_conf1, conf2=b_conf2, conf3=b_conf3, arred=b_arred, exercicio=b_exercicio,
              recap=b_recap, erros=b_erros, q7=b_q7, ponte=b_ponte, cta=b_cta)
