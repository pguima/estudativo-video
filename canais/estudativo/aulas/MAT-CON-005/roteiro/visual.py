"""Visual — Estudativo · MAT-CON-005: fração geratriz de uma dízima.
0,444… = 4/9; 0,1212… = 12/99 = 4/33; 0,2333… = 21/90 = 7/30. As contas ficam armadas (10x em cima, x embaixo, traço, 9x) e
as caudas iguais acendem na cor da matéria antes de sumir. A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-005_fracao_geratriz.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("equacao", "dois", "antes", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
from fractions import Fraction as Fr
assert 10 * Fr(4, 9) - Fr(4, 9) == 4 and Fr(12, 99) == Fr(4, 33) and 100 * Fr(4, 33) - Fr(4, 33) == 12
assert Fr(21, 90) == Fr(7, 30) and 100 * Fr(7, 30) - 10 * Fr(7, 30) == 21 and 23 - 2 == 21 and Fr(23, 99) != Fr(7, 30)
assert Fr(15, 90) == Fr(1, 6) and 16 - 1 == 15 and abs(1 / 6 - 0.16666) < 1e-4 and abs(4 / 9 - 0.4444) < 1e-4


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- símbolos de conjunto (a fonte da casa não tem ∈ ⊂ ∪ ∩ ℕ ℤ ℚ ℝ: desenhados aqui) ----------------
_TRACO = dict(g=0.15, b=0.1, m=0.075, i=0.052, s=0.052)
_DESENHA = "∈∉⊂⊄⊃∪∩∅"
_DUPLA = "ℕℤℚℝ"
_FM = skia.FontMgr()
_CM = _FM.makeFromFile("C:/Windows/Fonts/cambria.ttc", 1)


def _f2(size, est):
    f = skia.Font(_CM, size * 1.08)
    f.setSubpixel(True)
    f.setEdging(skia.Font.Edging.kAntiAlias)
    f.setEmbolden(est in "gb")
    return f


def _wsimb(ch, size, est):
    if ch in _DESENHA:
        return size * 0.78
    f = _f2(size, est)
    return f.measureText(ch) + size * 0.04


def _simb(c, ch, x, y, size, est, cor, a):
    sw = size * _TRACO[est]
    if ch in _DUPLA:
        f = _f2(size, est)
        p = M.paint(cor, a)
        if est in "gb":
            p.setStyle(skia.Paint.kStrokeAndFill_Style); p.setStrokeWidth(size * (0.025 if est == "g" else 0.012))
        c.drawString(ch, x + size * 0.02, y, f, p)
        return
    x0, x1 = x + size * 0.1 + sw / 2, x + size * 0.68 - sw / 2
    top, bot = y - size * 0.68 + sw / 2, y - size * 0.02 - sw / 2
    r = (bot - top) / 2
    pa = skia.Path()
    if ch in "∈∉⊂⊄":
        pa.moveTo(x1, top); pa.lineTo(x0 + r, top)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x0 + 2 * r, bot), -90, -180, False)
        pa.lineTo(x1, bot)
        if ch in "∈∉":
            pa.moveTo(x0, (top + bot) / 2); pa.lineTo(x1 - sw * 0.3, (top + bot) / 2)
    elif ch == "⊃":
        pa.moveTo(x0, top); pa.lineTo(x1 - r, top)
        pa.arcTo(skia.Rect.MakeLTRB(x1 - 2 * r, top, x1, bot), -90, 180, False)
        pa.lineTo(x0, bot)
    elif ch == "∪":
        rr = (x1 - x0) / 2
        pa.moveTo(x0, top); pa.lineTo(x0, bot - rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, bot - 2 * rr, x1, bot), 180, -180, False)
        pa.lineTo(x1, top)
    elif ch == "∩":
        rr = (x1 - x0) / 2
        pa.moveTo(x0, bot); pa.lineTo(x0, top + rr)
        pa.arcTo(skia.Rect.MakeLTRB(x0, top, x1, top + 2 * rr), 180, 180, False)
        pa.lineTo(x1, bot)
    elif ch == "∅":
        cx, cy, rr = (x0 + x1) / 2 + size * 0.02, (top + bot) / 2, (bot - top) / 2 + size * 0.02
        pa.addCircle(cx, cy, rr)
        pa.moveTo(cx + rr * 0.95, cy - rr * 1.25); pa.lineTo(cx - rr * 0.95, cy + rr * 1.25)
    if ch in "∉⊄":
        pa.moveTo(x0 + (x1 - x0) * 0.82, top - size * 0.1); pa.lineTo(x0 + (x1 - x0) * 0.18, bot + size * 0.1)
    p = M.paint(cor, a, stroke=sw)
    p.setStrokeCap(skia.Paint.kButt_Cap); p.setStrokeJoin(skia.Paint.kMiter_Join)
    c.drawPath(pa, p)


def _pedacos(s):
    out, cur = [], ""
    for ch in s:
        if ch in _DESENHA or ch in _DUPLA:
            if cur:
                out.append(cur); cur = ""
            out.append(ch)
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def tw(s, est, size):
    """largura de um texto que pode ter símbolos de conjunto"""
    return sum(_wsimb(p, size, est) if len(p) == 1 and (p in _DESENHA or p in _DUPLA) else E.larg(p, est, size) for p in _pedacos(s))


def tx(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """como E.escreve, com ∈ ∉ ⊂ ⊄ ∪ ∩ ℕ ℤ ℚ ℝ; align left/center/right"""
    if a <= 0:
        return
    cor = cor or TINTA
    w = tw(s, est, size)
    x = x - w / 2 if align == "center" else x - w if align == "right" else x
    for p in _pedacos(s):
        if len(p) == 1 and (p in _DESENHA or p in _DUPLA):
            _simb(c, p, x, y, size, est, cor, a)
            x += _wsimb(p, size, est)
        else:
            E.escreve(c, p, x, y, size, est, cor, a)
            x += E.larg(p, est, size)


def txe(c, t, t0, s, x, y, size, est="g", cor=None, align="left", d=0.5):
    E.foco(c, t, t0, d, lambda a: tx(c, s, x, y, size, est, cor, a, align))


def fz(c, t, t0, partes, x, y, align="left", passo=0.12):
    """como E.frase, aceitando os símbolos: partes = [(texto, estilo, tamanho[, cor])]"""
    esp = lambda p: p[2] * (0.24 if p[1] in "is" else 0.26)
    w = sum(tw(p[0], p[1], p[2]) for p in partes) + sum(esp(p) for p in partes[:-1])
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    for i, p in enumerate(partes):
        cor = p[3] if len(p) > 3 else TINTA
        E.foco(c, t, t0 + i * passo, 0.5, lambda a, p=p, xx=xx, cor=cor: tx(c, p[0], xx, y, p[2], p[1], cor, a))
        xx += tw(p[0], p[1], p[2]) + esp(p)
    return w
# ---------------- peças desta trilha ----------------
def ps(txt, est="i", size=84, cor=None):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor or TINTA) for w in txt.split()]


def entre(C, k1, k2, f):
    """instante entre dois marcadores (f = fração do trecho): acompanha a voz real sem segundos fixos"""
    return lerp(C[k1], C[k2], f)


def ln(c, t, partes, x, y, size, est="g", align="left"):
    """pedaços colados de um mesmo texto, cada um no seu instante: partes = [(texto, t0[, cor])]; devolve o x de cada pedaço"""
    ws = [tw(p[0], est, size) for p in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    xs = []
    for p, w in zip(partes, ws):
        cor = p[2] if len(p) > 2 else TINTA
        E.foco(c, t, p[1], 0.45, lambda a, p=p, xx=xx, cor=cor: tx(c, p[0], xx, y, size, est, cor, a))
        xs.append(xx)
        xx += w
    return xs


def esfera(c, t, t0, cx, cy, r, s, size, cor=None, est="g"):
    """esfera da matéria que cresce com um texto (ou símbolo) dentro"""
    k = ease_back(prog(t, t0, 0.6))
    if k <= 0:
        return
    E.bola(c, cx, cy, r * k, cor)
    E.foco(c, t, t0 + 0.15, 0.4, lambda a: tx(c, s, cx, cy + size * 0.36, size, est, E.SOBRE, a, "center"))


def fm(c, t, t0, s, x, y, size, cor=None, align="left"):
    """fórmula com fração (f{4}{9}) que entra com foco"""
    E.formula_em(c, t, t0, s, x, y, size, "g", cor or TINTA, align)


def lin(c, t, t0, esq, inteiro, cauda, xm, y, size, cor=None, tc=None, cor_c=None, ti=None, some=None):
    """linha armada pelo sinal de igual em xm: esq à esquerda; à direita, a parte inteira e a cauda (que acende em tc e apaga em some).
    ti = instante do lado direito, se ele entra depois"""
    cor = cor or TINTA
    g = size * 0.45
    E.foco(c, t, t0, 0.45, lambda a: (tx(c, esq, xm - g, y, size, "g", cor, a, "right"), centro(c, "=", xm, y, size, "g", cor, a)))
    td = t0 if ti is None else ti
    w = tw(inteiro, "g", size)
    E.foco(c, t, td, 0.45, lambda a: tx(c, inteiro, xm + g, y, size, "g", cor, a))
    if cauda:
        cc = (cor_c or COR) if tc is not None and t >= tc else cor
        a_c = 1.0 if some is None else 1 - 0.75 * ep(t, some, 0.5)
        E.foco(c, t, td, 0.45, lambda a: tx(c, cauda, xm + g + w, y, size, "g", cc, a * a_c))
        if tc is not None and t >= tc:
            wc = tw(cauda, "g", size)
            E.foco(c, t, tc, 0.4, lambda a: E.caixa_pontilhada(c, xm + g + w - 8, y - size * 0.86, wc + 16, size * 1.05, a, cc, prog_=a))


def traco(c, t, t0, x0, x1, y):
    p = ep(t, t0, 0.5)
    if p > 0:
        M.line(c, x0, y, x0 + (x1 - x0) * p, y, TINTA, 1.0, 6)


def menos(c, t, t0, x, y, size):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, "−", x, y, size, "g", ERRADO, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def dizima():
        fm(c, t, ka, "0,444…", W / 2, 330, 190, COR, "center")
        E.frase(c, t, ka + 0.6, ps("sem fim. que fração é essa?", "i", 66), W / 2, 450, "center", 0.08)
        for i, (f, d, x) in enumerate((("f{4}{10}", "= 0,4", 300), ("f{44}{100}", "= 0,44", 860))):
            t0 = entre(C, "s01.a", "s01.b", 0.45 + 0.2 * i)
            fm(c, t, t0, f + " " + d, x, 680, 110, TINTA2)
            if t >= t0 + 0.6:
                E.risco(c, x - 20, 720, x + 460, 600, t, t0 + 0.6, ERRADO, 12)
        E.foco(c, t, kb, 0.5, lambda a: (E.bola(c, 1660, 660, 140, CERTO, a), E.fracao(c, 4, 9, 1660, 650, 110, "#FFFFFF", a)))
        E.frase(c, t, kc, ps("e dá para descobrir em", "i", 70) + [("segundos", "g", 76, COR)], W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, dizima)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.25), ps("qualquer", "i", 90) + [("dízima", "g", 96, COR)], XE, 440, passo=0.12)
    fm(c, t, entre(C, "s02.a", "s02.b", 0.45), "0,444… → f{4}{9}", XE, 640, 110, COR)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.75), ps("com uma", "i", 80) + [("equação", "g", 84)], XE, 840, passo=0.12)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ macete", 1560, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    E.caixa_pontilhada(c, x, 220, w, 230, ep(t, C["s03.b"], 0.5), prog_=ep(t, C["s03.b"], 0.5))
    E.frase(c, t, C["s03.b"] + 0.1, [("dízima é", "i", 62), ("racional", "g", 64, COR)], x + 44, 300, "left", 0.1)
    fm(c, t, C["s03.b"] + 0.4, "0,4545… = f{5}{11}", x + 44, 400, 64, COR)
    E.caixa_pontilhada(c, x, 500, w, 230, ep(t, C["s03.c"], 0.5), prog_=ep(t, C["s03.c"], 0.5))
    E.frase(c, t, C["s03.c"] + 0.1, [("× 10 ou × 100:", "g", 64, COR), ("a vírgula anda", "i", 62)], x + 44, 590, "left", 0.1)
    E.formula_em(c, t, entre(C, "s03.c", "s03.end", 0.4), "0,5x = 1,2  →  5x = 12", x + 44, 680, 60, "g", TINTA2)
    py = lerp(430, 710, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.75), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 840, "left", 0.12)


# ---------------- a equação: um algarismo no período ----------------
XM = 560  # o igual das contas armadas


def b_equacao(c, t, C, b):
    a4, b4 = C["s04.a"], C["s04.b"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    E.frase(c, t, a4, ps("fração", "i", 84) + [("geratriz", "g", 90, COR)], XE, 170, "left", 0.12)
    E.frase(c, t, a4 + 0.6, ps("a fração que gera a dízima", "i", 54, TINTA2), XE + 560, 165, "left", 0.06)
    S = 110
    lin(c, t, b5, "10x", "4", ",444…", XM, 380, S, tc=c5, some=c6 + 0.5)
    lin(c, t, b4, "x", "0", ",444…", XM, 560, S, tc=c5, some=c6 + 0.5)
    def notas():
        E.foco(c, t, a5, 0.4, lambda a: E.pilula(c, "× 10 nos dois lados", XM + 760, 380 - 40, 46, "b", fundo=TINTA, a=a))
        if t < a6:
            E.foco(c, t, c5 + 0.3, 0.4, lambda a: E.escreve(c, "caudas iguais", XM + 620, 470, 54, "g", COR, a))
        E.foco(c, t, a6, 0.4, lambda a: E.pilula(c, "− x nos dois lados", XM + 760, 560 - 40, 46, "b", fundo=ERRADO, a=a))
        E.frase(c, t, c6 + 0.5, ps("a cauda some", "i", 56, TINTA2), XM + 380, 765, "left", 0.08)
    E.saida(c, t, a7, notas)
    menos(c, t, a6, 200, 560, S)
    traco(c, t, b6, 150, XM + 560, 620)
    lin(c, t, b6, "9x", "4", "", XM, 760, S, cor=COR, ti=d6)
    # resolve
    E.foco(c, t, b7, 0.5, lambda a: E.pilula(c, "÷ 9", 1460, 300, 52, "b", fundo=TINTA, a=a))
    fm(c, t, b7 + 0.2, "x = f{4}{9}", 1460, 520, 140, COR, "center")
    fm(c, t, c7, "4 ÷ 9 = 0,444…", 1460, 800, 76, CERTO, "center")
    E.foco(c, t, c7 + 0.6, 0.5, lambda a: E.selo(c, 1460, 900, 46, True, a))


# ---------------- dois algarismos no período ----------------
def b_dois(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    S = 104
    lin(c, t, d8, "100x", "12", ",1212…", XM, 380, S, tc=d8 + 0.8, some=a9 + 0.3)
    lin(c, t, a8, "x", "0", ",1212…", XM, 560, S, tc=d8 + 0.8, some=a9 + 0.3)
    E.foco(c, t, b8, 0.4, lambda a: E.pilula(c, "período: 12, dois algarismos", XM + 820, 470, 44, "b", a=a))
    E.foco(c, t, c8, 0.4, lambda a: E.pilula(c, "× 100: duas casas", XM + 720, 380 - 40, 46, "b", fundo=TINTA, a=a))
    menos(c, t, a9 - 0.3, 180, 560, S)
    traco(c, t, a9 - 0.2, 150, XM + 600, 620)
    lin(c, t, a9, "99x", "12", "", XM, 760, S, cor=COR)
    fm(c, t, b9, "x = f{12}{99}", 1000, 960, 100)
    E.foco(c, t, c9 - 0.5, 0.4, lambda a: E.pilula(c, "÷ 3", 1520, 790, 44, "b", fundo=TINTA, a=a))
    fm(c, t, c9, "= f{4}{33}", 1420, 960, 100, COR)


# ---------------- algarismo antes do período ----------------
def b_antes(c, t, C, b):
    def apresenta():
        ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
        E.frase(c, t, C["s10"] + 0.2, ps("e com algarismo", "i", 84) + [("antes do período?", "g", 88, COR)], W / 2, 220, "center", 0.12)
        ln(c, t, [("x = 0,", kb), ("2", kb, TINTA2), ("333…", kb, COR)], W / 2, 560, 180, "g", "center")
        E.frase(c, t, entre(C, "s10.b", "s10.c", 0.5), ps("o 2 aparece", "i", 60, TINTA2) + [("uma vez só", "g", 62, TINTA2)], W / 2, 720, "center", 0.08)
        E.frase(c, t, kc, ps("o período é o", "i", 64, COR) + [("3", "g", 72, COR)], W / 2, 830, "center", 0.08)
    E.saida(c, t, C["s11"] - 0.1, apresenta)
    if t < C["s11"]:
        return
    ka, kb, kc, kd, ke = (C[f"s11.{k}"] for k in "abcde")
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    S = 104
    E.frase(c, t, ka, ps("a vírgula vai até", "i", 60) + [("logo antes do período", "g", 62, COR)], XE, 160, "left", 0.08)
    lin(c, t, kb, "10x", "2", ",333…", XM, 560, S, tc=ke, some=c2)
    E.frase(c, t, kc, ps("depois, até o", "i", 60) + [("fim do 1º período", "g", 62, COR)], XE, 250, "left", 0.08)
    lin(c, t, kd, "100x", "23", ",333…", XM, 380, S, tc=ke, some=c2)
    if C["s11"] <= t < C["s12"]:
        E.foco(c, t, ke + 0.3, 0.4, lambda a: E.escreve(c, "caudas iguais", XM + 640, 470, 54, "g", COR, a))
    E.foco(c, t, a2, 0.4, lambda a: E.pilula(c, "− 10x nos dois lados", XM + 820, 560 - 40, 46, "b", fundo=ERRADO, a=a))
    menos(c, t, a2, 150, 560, S)
    traco(c, t, b2 - 0.2, 130, XM + 600, 620)
    lin(c, t, b2, "90x", "21", "", XM, 760, S, cor=COR, ti=c2)
    fm(c, t, d2, "x = f{21}{90}", 1000, 960, 100)
    E.foco(c, t, e2 - 0.5, 0.4, lambda a: E.pilula(c, "÷ 3", 1520, 790, 44, "b", fundo=TINTA, a=a))
    fm(c, t, e2, "= f{7}{30}", 1420, 960, 100, COR)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.2, [("cuidado:", "g", 80, ERRADO)] + ps("período de 2 algarismos", "i", 72) + [("× 10", "g", 80, ERRADO)], W / 2, 180, "center", 0.1)
    S = 110
    lin(c, t, kb, "10x", "1", ",2121…", XM + 200, 400, S, tc=kc, cor_c=ERRADO)
    lin(c, t, entre(C, "s13.a", "s13.b", 0.6), "x", "0", ",1212…", XM + 200, 580, S, tc=kc, cor_c=ERRADO)
    E.frase(c, t, kc + 0.3, ps("2121… contra 1212…", "b", 60, ERRADO), W / 2, 720, "center", 0.06)
    E.foco(c, t, kd, 0.5, lambda a: E.selo(c, 1640, 490, 56, False, a))
    E.frase(c, t, kd + 0.2, ps("não batem: nada some", "i", 66, ERRADO), W / 2, 810, "center", 0.08)
    E.frase(c, t, ke, ps("ande com a vírgula", "i", 76) + [("um período inteiro", "g", 80, CERTO)], W / 2, 920, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def noves():
        ka, kb, kc, kd = (C[f"s14.{k}"] for k in "abcd")
        E.frase(c, t, C["s14"] + 0.2, ps("agora, o", "i", 80, CLARO) + [("macete dos noves", "g", 84, BR)], W / 2, 170, "center", 0.11)
        E.foco(c, t, ka, 0.5, lambda a: E.fracao(c, "período", "9 para cada algarismo" if t >= kb else "", 640, 420, 76, BR, a))
        E.frase(c, t, ka + 0.2, ps("em cima", "i", 54, CLARO), 1180, 380, "left")
        E.frase(c, t, kb + 0.2, ps("embaixo", "i", 54, CLARO), 1180, 500, "left")
        fm(c, t, kc, "0,444… = f{4}{9}", 560, 820, 110, BR, "center")
        fm(c, t, kd, "0,1212… = f{12}{99}", 1360, 820, 110, BR, "center")
    E.saida(c, t, C["s15"] - 0.1, noves)
    if C["s15"] - 0.1 <= t:
        def porque():
            ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
            E.frase(c, t, ka - 0.3, ps("a equação", "i", 84, CLARO) + [("sempre deixa noves", "g", 88, BR)], W / 2, 300, "center", 0.11)
            fm(c, t, kb, "10x − x = 9x", W / 2, 560, 120, CLARO, "center")
            fm(c, t, kc, "100x − x = 99x", W / 2, 780, 120, CLARO, "center")
        E.saida(c, t, C["s16"] - 0.1, porque)
    if C["s16"] - 0.1 <= t:
        def antes():
            ka, kb, kc, kd, ke = (C[f"s16.{k}"] for k in "abcde")
            E.frase(c, t, C["s16"] + 0.2, ps("com algarismo antes do período:", "i", 70, CLARO), W / 2, 150, "center", 0.09)
            ln(c, t, [("0,", C["s16"] + 0.4, BR), ("2", C["s16"] + 0.4, CLARO), ("333…", C["s16"] + 0.4, BR)], 400, 420, 110, "g", "center")
            E.frase(c, t, ka, [("em cima:", "g", 58, BR)], 760, 280)
            E.frase(c, t, ka + 0.3, ps("até o fim do 1º período, menos o que não se repete", "i", 48, CLARO), 760, 345, "left", 0.04)
            fm(c, t, kb, "23 − 2 = 21", 760, 460, 96, BR)
            E.frase(c, t, kc, [("embaixo:", "g", 58, BR)], 760, 590)
            E.frase(c, t, kc + 0.3, ps("um 9 para o período, um 0 para o de antes", "i", 48, CLARO), 760, 655, "left", 0.04)
            fm(c, t, kd, "90", 760, 770, 96, BR)
            fm(c, t, ke, "f{23 − 2}{90} = f{21}{90} = f{7}{30}", 1260, 940, 90, CLARO, "center")
        E.saida(c, t, C["s17"] - 0.1, antes)
    if t < C["s17"]:
        return
    ka, kb, kc = C["s17.a"], C["s17.b"], C["s17.c"]
    E.frase(c, t, C["s17"] + 0.2, [("não compensa", "g", 84, BR)] + ps("o macete simples aqui", "i", 80, CLARO), W / 2, 220, "center", 0.11)
    fm(c, t, ka, "f{23}{99}", 600, 520, 140, ERRADO, "center")
    fm(c, t, kb, "= 0,2323…", 1050, 520, 120, ERRADO, "center")
    E.frase(c, t, kb + 0.6, ps("outro número", "i", 60, CLARO), 1050, 640, "center")
    E.frase(c, t, kc, ps("se esquecer, a", "i", 80, CLARO) + [("equação nunca falha", "g", 84, BR)], W / 2, 900, "center", 0.11)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb = C["s18.a"], C["s18.b"]
    E.frase(c, t, C["s18"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    E.frase(c, t, C["s18"] + 1.0, ps("a fração geratriz, na", "i", 70) + [("forma mais simples", "g", 72)], XE, 300, "left", 0.08)
    fm(c, t, ka, "0,777…", XE, 560, 150, COR)
    fm(c, t, kb, "0,1666…", XE, 820, 150, COR)
    E.relogio(c, t, C["s19.a"], 1520, 480, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    fm(c, t, C["s20"] + 0.3, "0,777…", XE, 260, 110)
    fm(c, t, a0, "= f{7}{9}", XE + 40 + E.formula(c, "0,777…", 0, 0, 110, a=0), 260, 110, CERTO)
    E.frase(c, t, entre(C, "s20", "s20.a", 0.6), ps("período 7: um nove", "i", 50, TINTA2), XE + 700, 240, "left", 0.06)
    ln(c, t, [("0,", C["s20"] + 0.5), ("1", C["s20"] + 0.5, TINTA2), ("666…", C["s20"] + 0.5, COR)], XE, 560, 110, "g")
    E.frase(c, t, b0, ps("1 antes do período", "i", 50, TINTA2) + ps("6", "g", 54, COR), XE, 650, "left", 0.06)
    E.frase(c, t, c0, [("em cima:", "g", 60, COR)], XE, 790)
    fm(c, t, c0 + 0.3, "16 − 1 = 15", XE + 300, 790, 76)
    E.frase(c, t, d0, [("embaixo:", "g", 60, COR)], XE, 900)
    fm(c, t, d0 + 0.3, "90", XE + 300, 900, 76)
    xa = XE + 40 + E.formula(c, "0,1666…", 0, 0, 110, a=0)
    fm(c, t, a1, "= f{15}{90}", xa, 560, 100)
    xb = xa + E.formula(c, "= f{15}{90}", 0, 0, 100, a=0) + 120
    E.foco(c, t, b1 - 0.4, 0.4, lambda a: E.pilula(c, "÷ 15", xb - 60, 400, 44, "b", fundo=TINTA, a=a))
    fm(c, t, b1, "= f{1}{6}", xb, 560, 100, CERTO)
    fm(c, t, c1, "1 ÷ 6 = 0,1666…", 1000, 850, 80, CERTO)
    E.foco(c, t, c1 + 0.8, 0.5, lambda a: E.selo(c, 1660, 820, 46, True, a))
    E.frase(c, t, c1 + 0.9, [("bateu", "g", 64, CERTO)], 1000, 950)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", "ande com a vírgula", "até as caudas ficarem iguais"), ("s22.b", "subtraia", "para a cauda sumir"),
                 ("s22.c", "com prática, os noves", "dão a resposta direto"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "g", 76), (l2, "i", 76)], 360, y, "left", 0.15)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    ka, kb, kc, kd = (C[f"s23.{k}"] for k in "abcd")
    E.frase(c, t, C["s23"] + 0.2, ps("toda dízima com período vira fração", "i", 70, TINTA2), XE, 220, passo=0.08)
    E.frase(c, t, ka - 1.0, ps("na próxima aula, os decimais que", "i", 72), XE, 340, passo=0.08)
    E.frase(c, t, ka, [("não acabam e não se repetem", "g", 84, COR)], XE, 460)
    fm(c, t, kb, "√7", XE, 640, 130, COR)
    fm(c, t, kb + 0.4, "π", XE + 260, 640, 130, COR)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 740, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(960, 765, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, equacao=b_equacao, dois=b_dois, antes=b_antes, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
