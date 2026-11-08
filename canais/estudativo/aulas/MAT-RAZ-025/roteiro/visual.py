"""Visual — Estudativo · MAT-RAZ-025: unidades como guia (análise dimensional).
Peças locais: termo() escreve um número com unidade, em cima e embaixo, e risca a unidade (ou o número) que corta na hora da fala;
fila() alinha os termos com "×" no meio, sempre centrada pelo tamanho final, para nada pular de lugar quando um termo entra.
Todo instante vem de C[...]; o que cai entre dois cues usa lerp(C[a], C[b], f), que acompanha qualquer voz."""
from decimal import Decimal as D

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-025_unidades_como_guia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("corta", "torneira", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 80 * 3 == 240
assert 20 * D(1) / 20 == 1 and 1 * 60 == 60 and 60 * 24 == 1440 and 1440 * 30 == 43200 and D(43200) / 1000 == D("43.2") and D("43.2") > 40
assert D(1) / 60 < 1
assert 2 * 60 == 120
assert 9 * 10 == 90 and 90 * 30 == 2700 and D(2700) / 1000 == D("2.7")


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.formula_em(c, t, t0, s, cx, y, size, est, cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=130, size=80, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def _partes(p, size):
    """(número, unidade) → larguras"""
    n, u = p
    wn = E.larg(n, "g", size) if n else 0
    wu = E.larg(u, "b", size * 0.8) if u else 0
    gap = size * 0.2 if n and u else 0
    return wn, gap, wu


def larg_termo(cima, baixo, size):
    w = sum(_partes(cima, size))
    if baixo:
        w = max(w, sum(_partes(baixo, size)))
    return w + size * 0.3


def termo(c, t, t0, cx, cy, size, cima, baixo=None, cor=None, cortes=(), escuro=False, cor_corte=None):
    """número com unidade; baixo=None escreve numa linha só. cortes = [(onde 'c'|'b', qual 'n'|'u', instante)]"""
    cor = cor or (BR if escuro else TINTA)
    cu = E.mix(cor, "#FFFFFF" if not escuro else "#000000", 0.25)
    linhas = {"c": (cima, cy - size * 0.2 if baixo else cy + size * 0.35)}
    if baixo:
        linhas["b"] = (baixo, cy + size * 0.9)
    caixas = {}
    for k, (p, y) in linhas.items():
        wn, gap, wu = _partes(p, size)
        x = cx - (wn + gap + wu) / 2
        caixas[(k, "n")] = (x, y, wn)
        caixas[(k, "u")] = (x + wn + gap, y, wu)

    def desenha(a):
        for k, (p, y) in linhas.items():
            x, _, wn = caixas[(k, "n")]
            if p[0]:
                E.escreve(c, p[0], x, y, size, "g", cor, a)
            xu = caixas[(k, "u")][0]
            if p[1]:
                E.escreve(c, p[1], xu, y, size * 0.8, "b", cu, a)
        if baixo:
            lw = larg_termo(cima, baixo, size) - size * 0.15
            b = size * 0.075
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - lw / 2, cy - b / 2 + size * 0.03, lw, b), b / 2, b / 2), M.paint(cor, a))
    E.foco(c, t, t0, 0.5, desenha)
    for onde, qual, tc in cortes:
        p = ep(t, tc, 0.35)
        if p > 0 and (onde, qual) in caixas:
            x, y, w = caixas[(onde, qual)]
            M.line(c, x - 6, y + size * 0.08, x + w + 6, y - size * 0.72, cor_corte or (CLARO if escuro else E.COR), 1.0, max(5, size * 0.08), progress=p)
    return caixas


def fila(c, t, itens, cx, cy, size, escuro=False, gap=None):
    """itens = [dict(t0, cima, baixo=None, cortes=(), cor=None)]: termos com '×' entre eles, centrados pelo tamanho final.
    Devolve os centros e a borda direita."""
    gap = gap or size * 0.75
    ws = [larg_termo(i["cima"], i.get("baixo"), size) for i in itens]
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2
    xs = []
    for k, (it, w) in enumerate(zip(itens, ws)):
        xm = x + w / 2
        xs.append(xm)
        if k:
            E.foco(c, t, it["t0"], 0.5, lambda a, x=x: centro(c, "×", x - gap / 2, cy + size * 0.3, size * 0.8, "g", BR if escuro else TINTA2, a))
        termo(c, t, it["t0"], xm, cy, size, it["cima"], it.get("baixo"), it.get("cor"), it.get("cortes", ()), escuro)
        x += w + gap
    return xs, x - gap


def igual_pilula(c, s, cy, size, a, cor=None, bola=False):
    """"= resultado": a pílula (ou a esfera) centrada, com o "=" encostado à esquerda"""
    if not s:
        return
    if bola:
        r = E.larg(s, "g", size) / 2 + size * 0.5
        E.bola(c, W / 2, cy + 10, r, cor, a)
        centro(c, s, W / 2, cy + 10 + size * 0.36, size, "g", E.SOBRE, a)
        w = 2 * r
    else:
        E.pilula(c, s, W / 2, cy, size, "g", fundo=cor, a=a, cor=E.SOBRE)
        w = E.larg(s, "g", size) + size * 1.1
    centro(c, "=", W / 2 - w / 2 - 80, cy + 30, 110, "g", TINTA2, a)


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def torneira(c, x, y, s, a=1.0, escuro=False):
    """torneira com o bico em (x, y) apontando para baixo"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA2
    M.rrect(c, x - s * 1.6, y - s * 0.95, s * 1.75, s * 0.5, s * 0.12, tinta, a)
    M.rrect(c, x - s * 0.25, y - s * 0.95, s * 0.5, s * 0.95, s * 0.12, tinta, a)
    M.rrect(c, x - s * 0.95, y - s * 1.35, s * 0.18, s * 0.42, s * 0.06, tinta, a)
    M.rrect(c, x - s * 1.2, y - s * 1.45, s * 0.7, s * 0.16, s * 0.08, tinta, a)


def gota(c, cx, cy, r, a=1.0, cor=None):
    """gota d'água: círculo com bico para cima"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy - r * 2.1)
    p.cubicTo(cx + r * 0.3, cy - r * 1.3, cx + r, cy - r * 0.6, cx + r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, 180, False)
    p.cubicTo(cx - r, cy - r * 0.6, cx - r * 0.3, cy - r * 1.3, cx, cy - r * 2.1)
    c.drawPath(p, M.paint(cor or E.COR, a))


def pingando(c, t, t0, x, y0, y1, r=16, periodo=0.9):
    """gotas caindo do bico (x, y0) até y1, uma a cada `periodo` segundos, a partir de t0"""
    if t < t0:
        return
    for k in range(4):
        f = ((t - t0) / periodo - k * 0.33) % 1.0 if t - t0 >= k * periodo * 0.33 else None
        if f is None:
            continue
        yy = y0 + (y1 - y0) * f * f
        gota(c, x, yy + r * 2.1, r, 1 - ep(f, 0.85, 0.15))


def lembrete2(c, t, C, cena, itens):
    """lembrete de duas coisas: itens = [(cue, linha fina, linha forte)]"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 930, 860
    for i, (k, l1, l2) in enumerate(itens):
        y = 260 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 690, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.55), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 930, 860, "left", 0.12)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]

    def um():
        tx, ty = 560, 330
        E.foco(c, t, C["s01"] + 0.2, 0.5, lambda a: torneira(c, tx, ty, 90, a))
        pingando(c, t, a1, tx, ty, 860, 22)
        E.frase(c, t, C["s01"] + 0.6, ps("parece não gastar", "i", 80) + [("nada", "g", 84)], 1000, 330, "left", 0.12)
        E.frase(c, t, a1, ps("uma gota aqui,", "i", 76, TINTA2), 1000, 470, "left", 0.12)
        E.frase(c, t, a1 + 1.0, ps("outra ali", "i", 76, TINTA2), 1000, 570, "left", 0.12)
        E.frase(c, t, b1 - 1.0, ps("em um mês:", "i", 80), 1000, 740, "left", 0.12)
        E.foco(c, t, b1, 0.5, lambda a: E.escreve(c, "+ de 40 L", 1000, 900, 150, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1450, 540, 290 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim da aula", "i", 92), XE, 330, passo=0.14)
        E.frase(c, t, ta + 0.8, [("fazer a conta", "g", 112, COR)], XE, 480)
        E.frase(c, t, ta + 1.4, ps("sem decorar", "i", 96), XE, 620, passo=0.12)
        E.frase(c, t, ta + 1.8, ps("nenhuma regra", "i", 96, COR), XE, 740, passo=0.12)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "as unidades", 1450, 525, 70, "i", E.SOBRE, a),
                                               centro(c, "montam", 1450, 615, 84, "g", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete2(c, t, C, "s03", (("s03.b", "multiplicar frações,", "cortando em cruz"), ("s03.c", "ler uma vazão,", "como L/min")))


# ---------------- a unidade corta ----------------
def b_corta(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")

    def conta():
        E.frase(c, t, C["s04"] + 0.2, ps("comece pelo", "i", 84) + [("conhecido", "g", 88, COR)], W / 2, 220, "center", 0.12)
        fcen(c, t, a4, "80 km/h", 500, 520, 120)
        fcen(c, t, b4, "× 3 h", 950, 520, 120)
        fcen(c, t, c4, "= 240 km", 1440, 520, 120, COR)
        E.foco(c, t, c4 + 0.3, 0.4, lambda a: centro(c, "80 × 3 = 240", W / 2, 760, 70, "b", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, conta)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"] + 0.2, ps("olhe as", "i", 84) + [("unidades", "g", 88, COR)], W / 2, 200, "center", 0.12)
    tc = c5
    xs, xd = fila(c, t, [dict(t0=a5, cima=("80", "km"), baixo=("1", "h"), cortes=[("b", "u", tc)]),
                        dict(t0=b5, cima=("3", "h"), cortes=[("c", "u", tc + 0.3)])], 820, 520, 130)
    E.foco(c, t, a5 + 0.4, 0.4, lambda a: (E.escreve(c, "km em cima", xs[0] - 520, 420, 50, "i", TINTA2, a),
                                            E.escreve(c, "hora embaixo", xs[0] - 520, 660, 50, "i", TINTA2, a)))
    E.foco(c, t, b5 + 0.3, 0.4, lambda a: E.escreve(c, "hora em cima", xs[1] - 120, 420, 50, "i", TINTA2, a))
    E.foco(c, t, c5 + 0.3, 0.4, lambda a: E.pilula(c, "se cortam", xs[1] - 90, 770, 54, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, d5 - 0.2, 0.5, lambda a: centro(c, "=", xd + 90, 565, 120, "g", TINTA, a))
    E.foco(c, t, d5, 0.5, lambda a: (E.escreve(c, "240", xd + 170, 565, 130, "g", TINTA, a),
                                     E.escreve(c, "km", xd + 170 + E.larg("240", "g", 130) + 26, 565, 130 * 0.8, "b", COR, a)))
    tq = lerp(d5, e5, 0.45)
    E.saida(c, t, e5 - 0.1, lambda: E.frase(c, t, tq, ps("a unidade do resultado", "i", 70) + [("saiu sozinha", "g", 70, COR)], W / 2, 900, "center", 0.1))
    if t >= e5 - 0.1:
        E.frase(c, t, e5, ps("aqui, ela vai", "i", 76) + [("montar a conta", "g", 80, COR)], W / 2, 900, "center", 0.12)


# ---------------- o fator que vale um ----------------
def b_fator(c, t, C, b):
    a6, b6 = C["s06.a"], C["s06.b"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    E.frase(c, t, a6, ps("o", "i", 90) + [("fator de conversão", "g", 96, COR)], W / 2, 220, "center", 0.12)
    fcen(c, t, lerp(a6, b6, 0.45), "1 h = 60 min", W / 2, 400, 90, TINTA2)
    termo(c, t, b6, 760, 620, 140, ("60", "min"), ("1", "h"))
    E.foco(c, t, b6 + 0.6, 0.4, lambda a: E.escreve(c, "a mesma quantidade", 1000, 600, 54, "i", TINTA2, a))
    E.foco(c, t, b6 + 0.8, 0.4, lambda a: E.escreve(c, "em cima e embaixo", 1000, 680, 54, "i", TINTA2, a))
    if t >= a7:
        E.foco(c, t, a7, 0.5, lambda a: (E.bola(c, 1640, 640, 110, a=a), centro(c, "= 1", 1640, 680, 100, "g", E.SOBRE, a)))
    E.frase(c, t, b7, ps("vezes 1:", "i", 66) + [("só troca a unidade", "g", 66, COR)], W / 2, 860, "center", 0.1)
    E.frase(c, t, c7, ps("a unidade que some vai", "i", 66) + [("do lado oposto", "g", 66, COR)], W / 2, 980, "center", 0.1)


# ---------------- a torneira ----------------
def b_torneira(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a10, b10 = C["s10.a"], C["s10.b"]
    a11, b11 = C["s11.a"], C["s11.b"]
    a12, b12 = C["s12.a"], C["s12.b"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]

    def dados():
        tx, ty = 330, 360
        E.foco(c, t, C["s08"] + 0.2, 0.5, lambda a: torneira(c, tx, ty, 80, a))
        pingando(c, t, C["s08"] + 0.5, tx, ty, 900, 20)
        fcen(c, t, a8, "20 gotas/min", 1100, 380, 110, COR)
        fcen(c, t, b8, "20 gotas = 1 mL", 1100, 590, 110)
        E.frase(c, t, c8, ps("quantos", "i", 84) + [("litros", "g", 88, COR)] + ps("em", "i", 84) + [("30 dias?", "g", 88)], 1100, 820, "center", 0.12)
    E.saida(c, t, C["s09"] - 0.1, dados)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"] + 0.1, ps("20 gotas/min →", "b", 54, TINTA2) + [("litros em 30 dias?", "g", 54, COR)], W / 2, 150, "center", 0.06)
    tg = c9
    tmin = lerp(a10, b10, 0.6)
    th = lerp(a11, b11, 0.45)
    tdia = lerp(a12, b12, 0.6)
    tml = lerp(a13, b13, 0.3)
    itens = [dict(t0=a9, cima=("20", "gotas"), baixo=("1", "min"), cortes=[("c", "u", tg), ("c", "n", tg + 0.4), ("b", "u", tmin)]),
             dict(t0=b9, cima=("1", "mL"), baixo=("20", "gotas"), cortes=[("b", "u", tg + 0.15), ("b", "n", tg + 0.55), ("c", "u", tml)]),
             dict(t0=a10, cima=("60", "min"), baixo=("1", "h"), cortes=[("c", "u", tmin + 0.15), ("b", "u", th)]),
             dict(t0=a11, cima=("24", "h"), baixo=("1", "dia"), cortes=[("c", "u", th + 0.15), ("b", "u", tdia)]),
             dict(t0=a12, cima=("30", "dias"), cortes=[("c", "u", tdia + 0.15)]),
             dict(t0=a13, cima=("1", "L"), baixo=("1.000", "mL"), cortes=[("b", "u", tml + 0.15)])]
    fila(c, t, itens, W / 2, 400, 66)
    # o que sobrou até agora
    y = 720
    res = [(d9, "1 mL/min"), (b10, "60 mL/h"), (b11, "1.440 mL/dia"), (b12, "43.200 mL"), (c13, "43,2 L")]
    troca(c, t, res, lambda s, a: igual_pilula(c, s, y, 96, a, bola=s == "43,2 L"))
    contas = [(b11, "60 × 24 = 1.440"), (b12, "1.440 × 30 = 43.200"), (b13, "43.200 ÷ 1.000: vírgula 3 casas para a esquerda"), (c13, "")]
    troca(c, t, contas, lambda s, a: centro(c, s, W / 2, 920, 58, "b", TINTA2, a))
    E.frase(c, t, c13 + 0.6, ps("jogados fora", "i", 64) + [("gota a gota", "g", 64, COR)], W / 2, 960, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a14, b14 = C["s14.a"], C["s14.b"]
    a15, b15, c15, d15 = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, C["s14"] + 0.2, [("cuidado:", "g", 90, ERRADO)] + ps("o fator", "i", 84) + [("de cabeça para baixo", "g", 84)], W / 2, 190, "center", 0.12)

    def errado():
        fcen(c, t, lerp(a14, b14, 0.4), "1 mL/min  →  mL/h", W / 2, 400, 96)
        fcen(c, t, b14, "1 ÷ 60", 700, 600, 110, ERRADO)
        fcen(c, t, a15, "= f{1}{60} mL/h", 1200, 600, 110, ERRADO)
        E.frase(c, t, lerp(a15, b15, 0.35), ps("em 1 hora pinga", "i", 70) + [("mais", "g", 74, ERRADO)] + ps("que em 1 minuto!", "i", 70), W / 2, 830, "center", 0.1)
    E.saida(c, t, b15 - 0.1, errado)
    if t < b15:
        return
    s = 120
    xs, xd = fila(c, t, [dict(t0=b15, cima=("1", "mL"), baixo=("1", "min"), cor=TINTA), dict(t0=b15 + 0.3, cima=("1", "h"), baixo=("60", "min"), cor=ERRADO)],
                  760, 480, s)
    if t >= c15:
        for x in xs:
            E.foco(c, t, c15, 0.4, lambda a, x=x: E.caixa_pontilhada(c, x - 150, 495, 300, 125, a, ERRADO))
        E.frase(c, t, c15 + 0.3, ps("min embaixo", "i", 64, ERRADO) + [("duas vezes", "g", 64, ERRADO)], 760, 810, "center", 0.1)
        E.frase(c, t, c15 + 0.9, ps("nada corta", "i", 64, ERRADO), 760, 900, "center", 0.1)
    if t >= d15:
        E.frase(c, t, d15, [("vire", "g", 80, CERTO)] + ps("o fator", "i", 76), 1500, 300, "center", 0.12)
        termo(c, t, d15 + 0.3, 1500, 500, s, ("60", "min"), ("1", "h"), CERTO)
        E.foco(c, t, d15 + 0.8, 0.4, lambda a: E.selo(c, 1500, 800, 56, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a16, b16 = C["s16.a"], C["s16.b"]
    a17 = C["s17.a"]
    a18, b18 = C["s18.a"], C["s18.b"]

    def fila_toda():
        E.frase(c, t, C["s16"] + 0.3, ps("o atalho de prova", "i", 70, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, a16, ps("monte a", "i", 92, CLARO) + [("fila inteira", "g", 100, BR)], W / 2, 300, "center", 0.12)
        tc = b16 + 0.2
        itens = [dict(t0=a16 + 0.6, cima=("20", "gotas"), baixo=("1", "min"), cortes=[("c", "u", tc), ("c", "n", a17), ("b", "u", tc + 0.3)]),
                 dict(t0=a16 + 0.8, cima=("1", "mL"), baixo=("20", "gotas"), cortes=[("b", "u", tc), ("b", "n", a17 + 0.2), ("c", "u", tc + 0.9)]),
                 dict(t0=a16 + 1.0, cima=("60", "min"), baixo=("1", "h"), cortes=[("c", "u", tc + 0.3), ("b", "u", tc + 0.5)]),
                 dict(t0=a16 + 1.2, cima=("24", "h"), baixo=("1", "dia"), cortes=[("c", "u", tc + 0.5), ("b", "u", tc + 0.7)]),
                 dict(t0=a16 + 1.4, cima=("30", "dias"), cortes=[("c", "u", tc + 0.7)]),
                 dict(t0=a16 + 1.6, cima=("1", "L"), baixo=("1.000", "mL"), cortes=[("b", "u", tc + 0.9)])]
        fila(c, t, itens, W / 2, 520, 62, escuro=True)
        E.frase(c, t, b16, ps("corte unidades", "i", 70, CLARO) + [("e números", "g", 74, BR)], W / 2, 800, "center", 0.12)
        E.frase(c, t, lerp(b16, C["s16.end"], 0.55), ps("e só multiplique", "i", 70, CLARO) + [("no fim", "g", 74, BR)], W / 2, 900, "center", 0.12)
        tf = lerp(C["s17"], a17, 0.5)
        E.foco(c, t, tf, 0.5, lambda a: E.formula(c, "f{20 × 1 × 60 × 24 × 30 × 1}{1 × 20 × 1 × 1 × 1.000}", W / 2, 1020, 50, "g", CLARO, a, "center"))
        if t >= a17:
            E.foco(c, t, a17, 0.4, lambda a: E.pilula(c, "o 20 de cima corta com o 20 de baixo", W / 2, 680, 40, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, a18 - 0.1, fila_toda)
    if t < a18:
        return
    E.frase(c, t, a18, ps("conversão de", "i", 84, CLARO) + [("um passo só", "g", 90, BR)], W / 2, 320, "center", 0.12)
    fcen(c, t, a18 + 1.0, "2 h → min", W / 2, 520, 110, CLARO)
    E.frase(c, t, b18, ps("multiplique", "i", 84, CLARO) + [("direto", "g", 90, BR)], W / 2, 720, "center", 0.12)
    fcen(c, t, b18 + 0.6, "2 × 60 = 120 min", W / 2, 900, 110, BR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s19.a"] - 1.0, ps("chuveiro:", "i", 84), XE, 380, passo=0.1)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.escreve(c, "9 L/min", XE + 380, 385, 100, "g", COR, a))
    E.frase(c, t, C["s19.b"] - 0.6, ps("banho:", "i", 84), XE, 540, passo=0.1)
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.escreve(c, "10 min/dia", XE + 300, 545, 100, "g", TINTA, a))
    E.frase(c, t, C["s19.c"], ps("quantos", "i", 92) + [("m³", "g", 100, COR)] + ps("em", "i", 92) + [("30 dias?", "g", 100)], XE, 790, passo=0.12)
    E.relogio(c, t, C["s20.a"], 1560, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a21, b21, c21 = C["s21.a"], C["s21.b"], C["s21.c"]
    a22, b22 = C["s22.a"], C["s22.b"]
    tmin = lerp(a21, b21, 0.6)
    tdia = lerp(b21, c21, 0.55)
    tl = lerp(a22, b22, 0.45)
    itens = [dict(t0=a21, cima=("9", "L"), baixo=("1", "min"), cortes=[("b", "u", tmin), ("c", "u", tl)]),
             dict(t0=a21 + 0.6, cima=("10", "min"), baixo=("1", "dia"), cortes=[("c", "u", tmin + 0.15), ("b", "u", tdia)]),
             dict(t0=lerp(b21, c21, 0.3), cima=("30", "dias"), cortes=[("c", "u", tdia + 0.15)]),
             dict(t0=a22, cima=("1", "m³"), baixo=("1.000", "L"), cortes=[("b", "u", tl + 0.15)])]
    E.frase(c, t, C["s21"] + 0.2, ps("vamos lá", "i", 76, COR), W / 2, 170, "center", 0.12)
    fila(c, t, itens, W / 2, 400, 80)
    y = 700
    res = [(b21, "90 L/dia"), (c21, "2.700 L"), (b22, "2,7 m³")]
    troca(c, t, res, lambda s, a: igual_pilula(c, s, y, 96, a, CERTO if s == "2,7 m³" else None, bola=s == "2,7 m³"))
    contas = [(b21, "9 × 10 = 90"), (c21, "90 × 30 = 2.700"), (lerp(a22, b22, 0.2), "1 m³ = 1.000 L"), (tl + 0.4, "2.700 ÷ 1.000: vírgula 3 casas para a esquerda"), (b22, "")]
    troca(c, t, contas, lambda s, a: centro(c, s, W / 2, 920, 58, "b", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s23.a", "escreva", "com as unidades"), ("s23.b", "multiplique por", "fatores que valem 1"),
                 ("s23.c", "pare quando sobrar", "a unidade pedida"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a), centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 76) + [(l2, "g", 76, COR if i == 0 else TINTA)], 320, y, "left", 0.1)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a0, b0 = C["s24.a"], C["s24.b"]
    E.frase(c, t, C["s24"] + 0.2, ps("na próxima aula", "i", 84), XE, 220, passo=0.14)
    E.frase(c, t, a0, [("praticando", "g", 130, COR)], XE, 380)
    E.frase(c, t, b0, ps("divisão proporcional,", "b", 64), XE, 500, passo=0.1)
    E.frase(c, t, b0 + 0.8, ps("velocidade, densidade", "b", 64), XE, 590, passo=0.1)
    E.frase(c, t, b0 + 1.4, ps("e", "i", 64) + [("vazão", "g", 64, COR)], XE, 680, passo=0.1)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 740, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(950, 765, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, corta=b_corta, fator=b_fator, torneira=b_torneira, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
