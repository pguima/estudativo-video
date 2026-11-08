"""Visual — Estudativo · MAT-POR-001: o que é porcentagem, em fração e em decimal.
Peças desta aula: grade100() é a grade de 100 quadradinhos que se pinta um a um (o bloco de 25 vira um dos 4 blocos iguais);
pizza() é a pizza cortada em n fatias, com as pintadas saindo do centro (12,5% = 1 de 8); bateria() é a carga do celular.
A voz é real: os marcadores vêm de C[...] e, onde a tela precisa da palavra exata, fala(cena, palavra) lê o tempos.json."""
import json
import math
from pathlib import Path
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Matemática", "Porcentagem")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POR-001_o_que_e_porcentagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("grade", "meio", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert Fr(25, 100) == Fr(1, 4) and Fr(60, 100) == Fr(3, 5) and Fr(7, 100) == Fr("0.07")
assert Fr(25, 200) == Fr(1, 8) == Fr("0.125") and 25 // 25 == 1 and 200 // 25 == 8
assert Fr(5, 100) == Fr("0.05") and Fr("0.5") == Fr(50, 100) and Fr("0.5") / 10 == Fr("0.05")
assert Fr(75, 200) == Fr(3, 8) == Fr("0.375") and Fr("37.5") == 3 * Fr("12.5")
assert Fr(10, 100) == Fr(1, 10) and Fr(20, 100) == Fr(1, 5)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- tempo da palavra dita ----------------
_TEMPOS = json.loads((Path(__file__).resolve().parents[1] / "audio" / "tempos.json").read_text(encoding="utf-8"))
_CENAS = {s["id"]: s for s in _TEMPOS["scenes"]}


def fala(sid, palavra, k=1):
    """instante em que a k-ésima `palavra` da cena começa a ser dita"""
    s = _CENAS[sid]
    n = 0
    for tk in s["tokens"]:
        if tk["disp"].lower().strip(".,:;?!") == palavra:
            n += 1
            if n == k:
                return s["start"] + tk["t0"]
    raise KeyError((sid, palavra, k))


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, ti, s, x, y, size=64, cor=None, est="g"):
    E.foco(c, t, ti, 0.45, lambda a: centro(c, s, x, y, size, est, cor or TINTA, a))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else M.on(cor), a)


def frac_bola(c, t, t0, n, d, cx, cy, s, r, cor=None):
    E.resultado(c, t, t0, n, d, cx, cy, s, r, cor)


# ---------------- peças desta aula ----------------
def grade100(c, x, y, L, pint, a=1.0, blocos=0.0, cor=None, destaca=0.0):
    """grade 10 x 10. pint = quantos quadradinhos pintados (pode ser fracionário: o último entra aos poucos), na ordem do bloco
    de cima à esquerda (5 x 5). blocos = 0..1 traça as linhas dos 4 blocos iguais; destaca = 0..1 contorna o bloco pintado"""
    if a <= 0:
        return
    cor = cor or E.COR
    rr = E._casco(c, x, y, L, L, 14, a)
    cel = L / 10
    c.save(); c.clipRRect(rr, True)
    for k in range(25):
        f = M.clamp(pint - k)
        if f <= 0:
            break
        i, j = k % 5, k // 5
        c.drawRect(skia.Rect.MakeXYWH(x + i * cel, y + j * cel, cel, cel), M.paint(cor, a * f))
    for i in range(1, 10):
        M.line(c, x + cel * i, y, x + cel * i, y + L, FIO, a, 3)
        M.line(c, x, y + cel * i, x + L, y + cel * i, FIO, a, 3)
    for i in range(1, 5):  # dentro do bloco pintado, linhas brancas
        if pint >= 25:
            M.line(c, x + cel * i, y, x + cel * i, y + L / 2, BR, a, 3)
            M.line(c, x, y + cel * i, x + L / 2, y + cel * i, BR, a, 3)
    c.restore()
    if blocos > 0:
        M.line(c, x + L / 2, y, x + L / 2, y + L, TINTA, a, 9, progress=blocos)
        M.line(c, x, y + L / 2, x + L, y + L / 2, TINTA, a, 9, progress=blocos)
    c.drawRRect(rr, M.paint(TINTA, a, stroke=4))
    if destaca > 0:
        E.caixa_pontilhada(c, x - 14, y - 14, L / 2 + 28, L / 2 + 28, destaca, COR, prog_=destaca)


def _fatia(cx, cy, r, a0, varre):
    p = skia.Path()
    p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), a0, varre, False)
    p.close()
    return p


def pizza(c, cx, cy, r, n, pint=0, a=1.0, sai=0.0, escuro=False, cor=None, enche=1.0):
    """pizza de n fatias iguais; as `pint` primeiras (a partir do alto, no sentido horário) ficam na cor e saem `sai` px do centro"""
    if a <= 0 or r <= 0:
        return
    cor = cor or (CLARO if escuro else E.COR)
    borda = CLARO if escuro else TINTA
    if not escuro:
        s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
        s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
        c.drawCircle(cx + 4, cy + 12, r, s)
    c.drawCircle(cx, cy, r, M.paint(E.VAZIO, a * (0.08 if escuro else 1)))
    passo_ = 360 / n
    for i in range(n if n > 1 else 0):
        ang = math.radians(-90 + i * passo_)
        M.line(c, cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), CLARO if escuro else FIO, a * (0.5 if escuro else 1), 3)
    c.drawCircle(cx, cy, r, M.paint(borda, a, stroke=4))
    for i in range(min(int(pint), n)):
        a0 = -90 + i * passo_
        if n == 1:
            c.drawCircle(cx, cy, r * enche, M.paint(cor, a))
            continue
        meio = math.radians(a0 + passo_ / 2)
        p = _fatia(cx + sai * math.cos(meio), cy + sai * math.sin(meio), r, a0, passo_ * enche)
        c.drawPath(p, M.paint(cor, a))
        c.drawPath(p, M.paint("#07070F" if escuro else BR, a, stroke=4))


def bateria(c, cx, cy, w, h, f, a=1.0):
    """bateria de celular deitada, carregada até a fração f"""
    if a <= 0:
        return
    x, y = cx - w / 2, cy - h / 2
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.14 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 4, y + 12, w, h), 30, 30), s)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint(BR, a))
    pad = 18
    if f > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + pad, y + pad, (w - 2 * pad) * f, h - 2 * pad), 14, 14), M.paint(E.COR, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint(TINTA, a, stroke=8))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + w + 6, cy - h * 0.18, 26, h * 0.36), 8, 8), M.paint(TINTA, a))


def ponte_frac(c, t, x0, x1, cy, s, rot, tc, tb, cor=None):
    E.pontes(c, t, x0, x1, cy, s, rot, tc, tb, cor, 48)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "12,5%", XE, 520, 250, "g", COR, a))
        E.frase(c, t, fala("s01", "parece"), ps("parece um número", "i", 74), XE, 680, passo=0.12)
        E.frase(c, t, fala("s01", "quebrado"), [("quebrado", "g", 74, TINTA)], XE, 780)
        E.frase(c, t, fala("s01", "imaginar"), ps("difícil de imaginar", "i", 74), XE, 880, passo=0.12)
        sai = 46 * ease_back(prog(t, kc, 0.6))
        E.foco(c, t, kb, 0.6, lambda a: pizza(c, 1420, 470, 270, 8, 1 if t >= kc else 0, a, sai))
        cen(c, t, fala("s01", "oito"), "8 pedaços", 1420, 860, 64, TINTA, "i")
        E.foco(c, t, kc + 0.2, 0.45, lambda a: E.pilula(c, "1 de 8", 1420, 975, 60, "g", a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 330, passo=0.14)
        E.frase(c, t, fala("s02", "porcentagem"), [("porcentagem", "g", 110, COR)], XE, 500)
        E.frase(c, t, fala("s02", "fração"), ps("vira", "i", 90) + [("fração", "g", 100)], XE, 650, passo=0.12)
        E.frase(c, t, fala("s02", "decimal"), ps("e", "i", 90) + [("decimal", "g", 100)], XE, 800, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "Simplificar", "uma fração"), ("s03.c", "Trocar fração", "por decimal"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 270
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 66)], x + 44, y + 92)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 66, COR)], x + 44, y + 178)
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 690, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, fala("s03", "se"), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 900, "left", 0.12)


# ---------------- em cada cem ----------------
GX, GY, GL = 230, 200, 680


def b_grade(c, t, C, b):
    a4, b4, c4, d4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]

    def pergunta():
        E.frase(c, t, C["s04"] + 0.3, ps("o que quer dizer", "i", 84), W / 2, 220, "center", 0.12)
        E.foco(c, t, a4, 0.5, lambda a: centro(c, "25%", W / 2, 500, 240, "g", COR, a))
        E.frase(c, t, b4, [("por cento", "g", 92, TINTA)], 850, 700, "right")
        cen(c, t, b4 + 0.4, "=", 920, 700, 92, TINTA2)
        E.frase(c, t, c4, ps("em cada", "i", 96) + [("cem", "g", 96, COR)], 990, 700, "left", 0.15)
        E.frase(c, t, d4, [("25", "g", 96, COR)] + ps("em cada", "i", 96) + [("100", "g", 96)], W / 2, 900, "center", 0.18)
    E.saida(c, t, C["s05"] - 0.1, pergunta)
    if t < C["s05"]:
        return
    a5, b5 = C["s05.a"], C["s05.b"]
    pint = 25 * ease_io(prog(t, b5, 1.4))
    E.foco(c, t, a5, 0.6, lambda a: grade100(c, GX, GY, GL, pint, a))
    xr = 1060
    E.frase(c, t, fala("s05", "cem"), [("100", "g", 130)], xr, 380)
    E.frase(c, t, fala("s05", "quadradinhos"), ps("quadradinhos", "i", 72), xr + 250, 380)
    E.frase(c, t, b5, ps("pintados:", "i", 72), xr, 560)
    E.foco(c, t, b5, 0.4, lambda a: E.escreve(c, str(int(round(pint))), xr + 330, 560, 120, "g", COR, a))
    E.foco(c, t, fala("s05", "você"), 0.5, lambda a: E.escreve(c, "25%", xr, 820, 200, "g", COR, a))
    E.frase(c, t, fala("s05", "grade"), ps("da grade", "i", 72), xr + 470, 820)


# ---------------- fração e decimal ----------------
def b_fracao(c, t, C, b):
    a6, b6, c6, d6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    gx, gy, gl = 1260, 230, 520

    def seis():
        E.frase(c, t, C["s06"] + 0.3, ps("virar fração é", "i", 80) + [("direto", "g", 80, COR)], XE, 150, "left", 0.12)
        y, s = 480, 120
        cen(c, t, a6 - 0.3, "25%", 270, y + 40, 110, TINTA)
        cen(c, t, a6 - 0.1, "=", 450, y + 30, 100, TINTA2)
        E.frac_q(c, t, a6, 25, 100, a6 + 0.1, fala("s06", "cem"), 620, y, s)
        E.frase(c, t, b6, ps("25 centésimos", "i", 54, TINTA2), 620, 700, "center", 0.12)
        ponte_frac(c, t, 760, 960, y, s, "÷ 25", c6, c6 + 0.35)
        E.foco(c, t, fala("s06", "quarto") - 0.3, 0.5, lambda a: E.fracao(c, 1, 4, 1060, y, s, COR, a))
        E.frase(c, t, fala("s06", "divisíveis"), ps("25 e 100: divisíveis por 25", "i", 50, TINTA2), XE, 870, "left", 0.08)
        E.foco(c, t, C["s06"], 0.5, lambda a: grade100(c, gx, gy, gl, 25, a, ep(t, d6, 0.8), destaca=ep(t, fala("s06", "pintou"), 0.5)))
        E.frase(c, t, d6, [("4", "g", 64, COR)] + ps("blocos iguais", "i", 60), gx + gl / 2, gy + gl + 110, "center", 0.12)
        E.frase(c, t, fala("s06", "pintou"), ps("pintou", "i", 60) + [("1", "g", 64, COR)], gx + gl / 2, gy + gl + 200, "center", 0.12)
    E.saida(c, t, C["s07"] - 0.15, seis)
    if t < C["s07"]:
        return

    def sete():
        E.frase(c, t, C["s07"] + 0.3, ps("e o", "i", 84) + [("decimal?", "g", 84, COR)], W / 2, 170, "center", 0.12)
        E.frase(c, t, fala("s07", "centésimos"), ps("centésimos:", "i", 66) + [("2 casas", "g", 66, COR)] + ps("depois da vírgula", "i", 66),
                W / 2, 300, "center", 0.12)
        s, y, xv = 210, 560, W / 2 + 120
        xs = E._centros("0,25", xv, s)
        E.foco(c, t, a7, 0.5, lambda a: E.numero(c, "0,", xv, y, s, a=a))
        for i in (2, 3):
            q = ep(t, a7 + 0.2, 0.5) * (1 - ep(t, b7, 0.3))
            if q > 0:
                E.caixa_pontilhada(c, xs[i] - s * 0.36, y - s * 0.78, s * 0.72, s * 0.92, q, COR, prog_=q)
        E.foco(c, t, b7 + 0.3, 0.45, lambda a: (E._digito(c, "2", xs[2], y, s, "g", COR, a), E._digito(c, "5", xs[3], y, s, "g", COR, a)))
        E.foco(c, t, fala("s07", "vinte", 1), 0.5, lambda a: E.fracao(c, 25, 100, 620, y - 70, 110, TINTA, a))
        cen(c, t, fala("s07", "é") - 0.1, "=", 810, y - 40, 100, TINTA2)
        yr = 820
        cen(c, t, fala("s07", "vinte", 3), "25%", 420, yr + 40, 110, TINTA)
        cen(c, t, fala("s07", "um"), "=", 600, yr + 30, 96, TINTA2)
        E.foco(c, t, fala("s07", "um"), 0.5, lambda a: E.fracao(c, 1, 4, 720, yr, 110, COR, a))
        cen(c, t, fala("s07", "zero", 2), "=", 840, yr + 30, 96, TINTA2)
        cen(c, t, fala("s07", "zero", 2), "0,25", 1030, yr + 40, 110, TINTA)
        E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "o mesmo número", 1520, yr + 2, 54, "g", a=a))
        E.frase(c, t, fala("s07", "três"), ps("3 jeitos", "i", 60, TINTA2), 1520, yr + 120, "center")
    E.saida(c, t, C["s08"] - 0.15, sete)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"] + 0.3, ps("a", "i", 84) + [("regra", "g", 84, COR)], W / 2, 170, "center", 0.12)
    y0 = 360
    cen(c, t, a8, "%", 700, y0 + 50, 150, COR)
    cen(c, t, fala("s08", "é") - 0.2, "=", 860, y0 + 35, 110, TINTA2)

    def molde(a):
        E.caixa_pontilhada(c, 1060 - 48, y0 - 125, 96, 100, a, COR)
        E.fracao(c, "", 100, 1060, y0, 110, TINTA, a)
    E.foco(c, t, fala("s08", "fração"), 0.5, molde)
    for k, (ti, pc, n, d, tf, res, tr, eh_frac) in enumerate((
            (b8, "7%", 7, 100, fala("s08", "sete", 2), "0,07", fala("s08", "zero"), False),
            (c8, "60%", 60, 100, fala("s08", "sessenta", 2), (3, 5), fala("s08", "três"), True))):
        y = 640 + k * 240
        cen(c, t, ti, pc, 600, y + 40, 110, TINTA)
        cen(c, t, tf - 0.2, "=", 780, y + 30, 96, TINTA2)
        E.foco(c, t, tf, 0.5, lambda a, n=n, d=d, y=y: E.fracao(c, n, d, 940, y, 100, TINTA, a))
        cen(c, t, tr - 0.2, "=", 1100, y + 30, 96, TINTA2)
        if eh_frac:
            E.foco(c, t, tr, 0.5, lambda a, y=y: E.fracao(c, 3, 5, 1260, y, 100, COR, a))
        else:
            cen(c, t, tr, res, 1320, y + 40, 110, COR)


# ---------------- doze e meio ----------------
def b_meio(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    y, s = 430, 120

    def linha_():
        E.frase(c, t, C["s09"] + 0.3, ps("voltando ao gancho:", "i", 80), XE, 170, "left", 0.12)
        E.frase(c, t, fala("s09", "doze"), [("12,5%", "g", 90, COR)], XE + 780, 170)
        E.foco(c, t, a9, 0.5, lambda a: E.fracao(c, "12,5", 100, 300, y, s, TINTA, a))
        E.foco(c, t, fala("s09", "fração"), 0.5, lambda a: E.caixa_pontilhada(c, 300 - 150, y - 125, 300, 116, a, ERRADO))
        E.frase(c, t, fala("s09", "meio", 2), ps("meio em cima?", "i", 54, ERRADO), 300, y - 170, "center", 0.1)
        ponte_frac(c, t, 450, 625, y, s, "× 2", b9, b9 + 0.5)
        E.foco(c, t, c9, 0.5, lambda a: E.fracao(c, 25, 200, 760, y, s, TINTA, a))
        ponte_frac(c, t, 905, 1075, y, s, "÷ 25", fala("s10", "divisíveis"), fala("s10", "divisíveis") + 0.4)
        frac_bola(c, t, c10, 1, 8, 1210, y, s * 0.92, 120)
        sai = 34 * ease_back(prog(t, fala("s10", "fatia") + 0.2, 0.6))
        E.foco(c, t, fala("s10", "fatia"), 0.5, lambda a: pizza(c, 1640, y + 5, 160, 8, 1, a, sai))
    E.saida(c, t, C["s11"] - 0.15, linha_)
    if t < C["s10"] - 0.15:
        E.saida(c, t, C["s10"] - 0.2, lambda: E.frase(c, t, fala("s09", "como"), ps("dobrar em cima e embaixo", "i", 62) + [("não muda o valor", "g", 62, COR)],
                                                     W / 2, 800, "center", 0.1))
    if C["s10"] <= t < C["s11"]:
        E.frase(c, t, a10, [("25 ÷ 25", "g", 76), ("=", "g", 76, TINTA2), ("1", "g", 76, COR)], XE + 160, 770, "left", 0.3)
        E.frase(c, t, b10, [("200 ÷ 25", "g", 76), ("=", "g", 76, TINTA2), ("8", "g", 76, COR)], XE + 160, 900, "left", 0.3)
        E.frase(c, t, c10 + 0.4, ps("um oitavo", "i", 64, COR), 1210, 640, "center", 0.12)
    if t < C["s11"]:
        return
    a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
    E.frase(c, t, a11, ps("o decimal:", "i", 76) + [("1 ÷ 8", "g", 80, COR)], XE, 160, "left", 0.15)
    D = E.dividir("1", 8)
    assert D["quociente"] == "0,125"
    E.conta_div(c, t, D, [fala("s11", "zero"), fala("s11", "um", 3), fala("s11", "dois", 2), fala("s11", "cinco")],
                [b11, c11, d11, fala("s11", "não")], a11 + 0.3, 300, 380, 120, tv=fala("s11", "vírgula"),
                ts=[fala("s11", "zero") + 0.2, fala("s11", "dois", 1), fala("s11", "quatro")])
    E.frase(c, t, fala("s11", "um", 2), ps("1 é menor que 8:", "i", 56, TINTA2), 960, 690, "left", 0.08)
    E.frase(c, t, fala("s11", "escreva"), [("0 e vírgula", "g", 60, TINTA)], 960, 780, "left")
    E.foco(c, t, e11, 0.5, lambda a: num_bola(c, "0,125", 1600, 760, 150, 84, a))
    E.frase(c, t, e11 + 0.5, [("12,5% = 1/8 = 0,125", "g", 52, TINTA2)], 1560, 1000, "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13 = C["s13.a"], C["s13.b"]
    E.frase(c, t, fala("s12", "cuidado"), [("cuidado", "g", 100, ERRADO)] + ps("com um erro comum", "i", 90), W / 2, 180, "center", 0.12)

    def doze():
        y = 430
        cen(c, t, a12, "5%", 620, y, 170, TINTA)
        cen(c, t, b12 - 0.2, "=", 840, y, 140, TINTA2)
        cen(c, t, b12, "0,5", 1080, y, 170, ERRADO)
        if t >= c12 + 0.6:
            E.risco(c, 940, y + 10, 1220, y - 140, t, c12 + 0.6, largura=14)
        E.linha(c, t, [("0,5", "g", 84, TINTA, fala("s12", "zero", 2)), ("=", "g", 84, TINTA2, fala("s12", "é")),
                       ("5 décimos", "g", 84, TINTA, fala("s12", "cinco", 3))], W / 2, 640, "center")
        E.linha(c, t, [("=", "g", 84, TINTA2, fala("s12", "mesmo")), ("50 centésimos", "g", 84, TINTA, fala("s12", "cinquenta")),
                       ("=", "g", 84, TINTA2, c12 - 0.2), ("50%", "g", 84, ERRADO, c12)], W / 2, 790, "center")
        E.frase(c, t, fala("s12", "metade"), ps("a metade!", "i", 76, ERRADO), W / 2, 930, "center")
    E.saida(c, t, C["s13"] - 0.15, doze)
    if t < C["s13"]:
        return
    y = 400
    cen(c, t, C["s13"] + 0.3, "5%", 520, y + 50, 150, TINTA)
    cen(c, t, fala("s13", "são") - 0.1, "=", 720, y + 40, 120, TINTA2)
    E.foco(c, t, a13, 0.5, lambda a: E.fracao(c, 5, 100, 900, y, 120, TINTA, a))
    E.frase(c, t, fala("s13", "centésimo"), ps("centésimo pede", "i", 66) + [("2 casas", "g", 66, COR)], 1450, y + 20, "center", 0.12)
    s, xv, yv = 170, 1330, 790
    xs = E._centros("0,05", xv, s)
    E.foco(c, t, b13, 0.5, lambda a: E.numero(c, "0,05", xv, yv, s, a=a, cor=CERTO))
    E.chave(c, xs[2] - s * 0.34, xs[3] + s * 0.34, yv + 40, COR, ep(t, b13 + 0.5, 0.4), 24, 6)
    tm = fala("s13", "dez")
    E.foco(c, t, tm, 0.5, lambda a: centro(c, "0,5", 520, yv, 150, "g", ERRADO, a))
    if t >= tm + 0.4:
        E.risco(c, 400, yv + 10, 650, yv - 110, t, tm + 0.4, largura=12)
    if t >= fala("s13", "menor"):
        E.ponte(c, t, fala("s13", "menor"), 700, 1000, yv - 50, "10 vezes menor", TINTA, 44)


# ---------------- atalho (palco escuro) ----------------
COLS = (300, 740, 1180, 1620)


def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14, d14, e14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]
    a15, b15, c15, d15, e15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]

    def escada():
        E.saida(c, t, a15 - 0.1, lambda: E.frase(c, t, a14, ps("o caminho das", "i", 84, CLARO) + [("metades", "g", 84, BR)], W / 2, 150, "center", 0.14))
        E.frase(c, t, a15, ps("cada metade", "i", 76, CLARO) + [("dobra o de baixo", "g", 76, BR)], W / 2, 150, "center", 0.12)
        dados = ((b14, "100%", 1, 1, 1), (c14, "50%", 1, 2, 2), (d14, "25%", 1, 4, 4), (e14, "12,5%", 1, 8, 8))
        for i, (ti, pc, n, d, nf) in enumerate(dados):
            x = COLS[i]
            E.foco(c, t, ti, 0.6, lambda a, x=x, nf=nf, ti=ti: pizza(c, x, 420, 140, nf, 1, a, 16 * ease_back(prog(t, ti + 0.4, 0.5)) if nf > 1 else 0, True))
            cen(c, t, ti + 0.4, pc, x, 700, 84, BR)
            E.foco(c, t, ti + 0.8, 0.5, lambda a, x=x, n=n, d=d: E.fracao(c, n, d, x, 830, 92, CLARO, a))
            if i:
                ponte_frac_esc(c, t, ti, COLS[i - 1] + 160, x - 160, 420, "÷ 2")
                ti2 = fala("s15", "dobra") + 0.25 * (i - 1)
                E.ponte(c, t, ti2, COLS[i - 1] + 70, x - 70, 935, "× 2", CLARO, 40)
        if t < b14 + 0.8:
            pass
    E.saida(c, t, fala("s15", "guarde") - 0.1, escada)
    if t < fala("s15", "guarde"):
        return
    E.frase(c, t, fala("s15", "guarde"), ps("guarde também", "i", 84, CLARO), W / 2, 180, "center", 0.14)
    for x, ti, pc, n, d in ((560, b15, "10%", 1, 10), (1360, c15, "20%", 1, 5)):
        cen(c, t, ti, pc + " =", x - 80, 460, 110, BR)
        E.foco(c, t, ti + 0.6, 0.5, lambda a, x=x, n=n, d=d: E.fracao(c, n, d, x + 180, 420, 110, CLARO, a))
    y = 780
    cen(c, t, d15, "37%", 560, y, 120, BR)
    if t >= d15 + 1.0:
        E.foco(c, t, d15 + 1.0, 0.4, lambda a: centro(c, "não compensa", 560, y + 110, 54, "i", CLARO, a))
    E.ponte(c, t, e15 - 0.4, 740, 1060, y - 40, "direto", CLARO, 44)
    E.foco(c, t, e15, 0.5, lambda a: E.fracao(c, 37, 100, 1250, y - 40, 120, BR, a))


def ponte_frac_esc(c, t, t0, x0, x1, y, rot):
    E.ponte(c, t, t0, x0, x1, y, rot, CLARO, 42)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.3, ps("hora de testar", "i", 72, COR), XE, 170)

    E.frase(c, t, fala("s16", "bateria"), ps("bateria do celular:", "i", 76), XE, 330, "left", 0.12)
    E.frase(c, t, a16, [("37,5%", "g", 110, COR)], XE, 460)
    f = 0.375 * ease_io(prog(t, a16, 1.2))
    E.saida(c, t, C["s17"] - 0.1, lambda: (E.foco(c, t, fala("s16", "bateria"), 0.5, lambda a: bateria(c, 1400, 480, 520, 230, f, a))))
    E.frase(c, t, b16, ps("que", "i", 92) + [("fração", "g", 92, COR)] + ps("é essa?", "i", 92), XE, 600, "left", 0.15)
    E.frase(c, t, fala("s16", "forma"), ps("na forma mais simples", "i", 62, TINTA2), XE, 700, "left", 0.1)
    E.frase(c, t, c16, ps("e o", "i", 92) + [("decimal?", "g", 92, COR)], XE, 880, "left", 0.15)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], 1420, 480, 190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18 = C["s18.a"], C["s18.b"], C["s18.c"]
    a19, b19, c19 = C["s19.a"], C["s19.b"], C["s19.c"]
    y, s = 470, 120

    def conta():
        E.frase(c, t, fala("s18", "são"), ps("37 e meio em cada 100", "i", 70), W / 2, 200, "center", 0.1)
        E.foco(c, t, fala("s18", "são") + 0.4, 0.5, lambda a: E.fracao(c, "37,5", 100, 300, y, s, TINTA, a))
        ponte_frac(c, t, 450, 625, y, s, "× 2", a18, a18 + 0.5)
        E.foco(c, t, fala("s18", "setenta"), 0.5, lambda a: E.fracao(c, 75, 200, 760, y, s, TINTA, a))
        ponte_frac(c, t, 905, 1075, y, s, "÷ 25", b18, b18 + 0.5)
        frac_bola(c, t, c18, 3, 8, 1210, y, s * 0.92, 120)
        E.frase(c, t, b18 + 0.6, [("75 ÷ 25 = 3", "g", 60, TINTA2)], XE + 120, 800, "left")
        E.frase(c, t, b18 + 1.0, [("200 ÷ 25 = 8", "g", 60, TINTA2)], XE + 120, 900, "left")
    E.saida(c, t, C["s19"] - 0.1, conta)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"] + 0.3, ps("pelo", "i", 84) + [("atalho", "g", 84, COR)], XE, 190, "left", 0.12)
    E.linha(c, t, [("37,5", "g", 100, TINTA, fala("s19", "trinta")), ("=", "g", 100, TINTA2, a19 - 0.2),
                   ("3 × 12,5", "g", 100, COR, a19)], XE, 390)
    sai = 30 * ease_back(prog(t, b19 + 0.3, 0.6))
    E.foco(c, t, b19, 0.5, lambda a: pizza(c, 1500, 610, 230, 8, 3, a, sai))
    E.frase(c, t, b19, [("3", "g", 92, COR)] + ps("fatias de", "i", 84), XE, 570, "left", 0.12)
    E.foco(c, t, fala("s19", "um"), 0.5, lambda a: E.fracao(c, 1, 8, XE + 480, 540, 92, TINTA, a))
    E.linha(c, t, [("=", "g", 100, TINTA2, fala("s19", "três", 2) - 0.2)], XE, 840)
    E.foco(c, t, fala("s19", "três", 2), 0.5, lambda a: E.fracao(c, 3, 8, XE + 170, 810, 110, COR, a))
    E.linha(c, t, [("=", "g", 100, TINTA2, c19 - 0.2)], XE + 270, 840)
    E.foco(c, t, c19, 0.5, lambda a: num_bola(c, "0,375", XE + 520, 810, 130, 76, a, CERTO))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s, e) in enumerate((("s20.a", "% = em cada 100", "g"), ("s20.b", "100 embaixo e simplifique", "g"),
                                       ("s20.c", "decimal: cima ÷ baixo", "g"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 330 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", "#FFFFFF", a)))
            E.frase(c, t, C[k] + 0.1, [(s, e, 90)], 430, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a21, b21, c21, d21, e21 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"], C["s21.e"]
    E.frase(c, t, C["s21"] + 0.3, [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, a21, [("Calcular", "g", 120, COR)], XE, 450)
    E.frase(c, t, a21 + 0.3, [("porcentagem", "g", 120, COR)], XE, 580)
    E.frase(c, t, b21, [("15% de 80", "g", 76)] + ps("de cabeça", "i", 76), XE, 740, "left", 0.2)
    E.frase(c, t, c21, ps("e contas maiores", "i", 76) + [("com decimal", "g", 76, COR)], XE, 850, "left", 0.15)
    E.foco(c, t, d21, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 72, estilo="g", a=a))
    p = ease_io(prog(t, d21 + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1640, p), lerp(620, 325, p), ep(t, d21 + 0.2, 0.4))
    E.frase(c, t, e21, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, grade=b_grade, fracao=b_fracao, meio=b_meio, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
