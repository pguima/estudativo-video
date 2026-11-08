"""Visual — Estudativo · MAT-CON-001: conjuntos, pertence, está contido e vazio.
V = {a, e, i, o, u}; ∈ liga elemento a conjunto, ⊂ liga conjunto a conjunto; {1, 2, 3} tem 8 subconjuntos (2³); P = {2, 5, 7, 9} tem 16.
A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-001_conjuntos_pertence_contido_vazio.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conjunto", "pertence", "contar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
assert 3 + 3 + 1 + 1 == 8 == 2 ** 3 and 2 ** 5 == 32 and 2 ** 4 == 16


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


# ---------------- gancho ----------------
SEIS = ("{1}", "{2}", "{3}", "{1, 2}", "{1, 3}", "{2, 3}")


def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def lista():
        E.frase(c, t, ka, ps("quantos subconjuntos tem", "i", 84), W / 2, 190, "center", 0.1)
        txe(c, t, ka + 0.6, "{1, 2, 3}", W / 2, 360, 150, "g", COR, "center")
        for i, s in enumerate(SEIS):
            x, y = 330 + (i % 3) * 400, 560 + (i // 3) * 150
            txe(c, t, entre(C, "s01.a", "s01.b", 0.55) + 0.15 * i, s, x, y, 96, "g", TINTA, "center")
        E.foco(c, t, kb, 0.5, lambda a: tx(c, "= 6 ?", 1360, 635, 130, "g", ERRADO, a))
        if t >= kb + 0.6:
            E.risco(c, 1320, 680, 1680, 520, t, entre(C, "s01.b", "s01.c", 0.25), ERRADO, 14)
        txe(c, t, entre(C, "s01.b", "s01.c", 0.4), "∅", 330, 950, 110, "g", CERTO, "center")
        E.frase(c, t, entre(C, "s01.b", "s01.c", 0.4) + 0.2, ps("o vazio", "i", 60, CERTO), 420, 940, "left")
        txe(c, t, entre(C, "s01.b", "s01.c", 0.65), "{1, 2, 3}", 1000, 950, 96, "g", CERTO, "center")
        E.frase(c, t, entre(C, "s01.b", "s01.c", 0.65) + 0.2, ps("o próprio", "i", 60, CERTO), 1230, 940, "left")
        esfera(c, t, kc, 1660, 920, 120, "8", 150, CERTO)
    E.saida(c, t, C["s02"] - 0.1, lista)
    if t < C["s02"]:
        return
    ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
    E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1520, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.5), ps("escrever", "i", 90) + [("qualquer conjunto", "g", 90, COR)], XE, 450, passo=0.14)
    fz(c, t, tb, [("usar", "i", 90), ("∈", "g", 110, COR), ("e", "i", 90), ("⊂", "g", 110, COR), ("sem trocar", "g", 84)], XE, 600)
    E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1520, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1520, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    E.caixa_pontilhada(c, x, 240, w, 196, ep(t, C["s03.b"], 0.5), prog_=ep(t, C["s03.b"], 0.5))
    E.frase(c, t, C["s03.b"] + 0.1, [("comparar números", "i", 62)], x + 44, 324)
    E.frase(c, t, C["s03.b"] + 0.3, [("com", "i", 62), (">", "g", 66, COR), ("e", "i", 62), ("<", "g", 66, COR)], x + 44, 404)
    E.caixa_pontilhada(c, x, 500, w, 196, ep(t, C["s03.c"], 0.5), prog_=ep(t, C["s03.c"], 0.5))
    E.frase(c, t, C["s03.c"] + 0.1, [("potência", "i", 62)], x + 44, 584)
    E.formula_em(c, t, entre(C, "s03.c", "s03.end", 0.25), "2^3 = 2 × 2 × 2", x + 44, 668, 66, "g", COR)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.72), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 820, "left", 0.12)


# ---------------- o que é conjunto ----------------
def b_conjunto(c, t, C, b):
    def oque():
        ka, kb, kc = C["s04.a"], C["s04.b"], C["s04.c"]
        E.frase(c, t, C["s04"] + 0.2, ps("o que é um", "i", 90) + [("conjunto?", "g", 120, COR)], W / 2, 220, "center", 0.12)
        E.frase(c, t, ka, ps("um", "i", 76) + [("grupo de coisas", "g", 76)], W / 2, 380, "center", 0.12)
        E.frase(c, t, entre(C, "s04.a", "s04.b", 0.45), ps("com uma", "i", 76) + [("regra clara", "g", 76, COR)] + ps("de quem está dentro", "i", 76),
                W / 2, 490, "center", 0.12)
        E.frase(c, t, kb, ps("cada coisa é um", "i", 76) + [("elemento", "g", 84, COR)], W / 2, 640, "center", 0.12)
        for i, s in enumerate("aeiou"):
            esfera(c, t, kc + 0.25 + 0.3 * i, 560 + i * 200, 850, 80, s, 110)
    E.saida(c, t, C["s05"] - 0.1, oque)
    if t < C["s05"]:
        return
    ka, kb, kc, kd, ke = (C[f"s05.{k}"] for k in "abcde")
    y, s = 330, 150
    # V = {a, e, i, o, u}: o nome, as chaves, depois os elementos
    partes = [("V", ka, COR), (" = {", kb), ("a", kc), (", e", kc + 0.25), (", i", kc + 0.5), (", o", kc + 0.75), (", u", kc + 1.0), ("}", kb)]
    xs = ln(c, t, partes, W / 2, y, s, "g", "center")
    E.foco(c, t, ka + 0.2, 0.45, lambda a: E.pilula(c, "nome: letra maiúscula", xs[0] + 40, y + 90, 44, a=a))
    E.foco(c, t, kb + 0.2, 0.45, lambda a: E.pilula(c, "entre chaves, separados por vírgula", W / 2 + 170, y + 90, 44, fundo=TINTA, a=a))
    # ordem e repetidos
    txe(c, t, kd, "{a, e, i, o, u} = {u, o, i, e, a}", W / 2, 640, 96, "g", TINTA, "center")
    E.frase(c, t, kd + 0.3, ps("a ordem", "i", 64) + [("não importa", "g", 64, COR)], W / 2, 730, "center", 0.12)
    txe(c, t, ke, "{a, a, e} = {a, e}", W / 2, 890, 96, "g", TINTA, "center")
    E.frase(c, t, ke + 0.3, ps("repetido conta", "i", 64) + [("uma vez só", "g", 64, COR)], W / 2, 980, "center", 0.12)


# ---------------- pela regra; o vazio ----------------
def b_regra(c, t, C, b):
    def regra():
        ka, kb, kc = C["s06.a"], C["s06.b"], C["s06.c"]
        E.frase(c, t, C["s06"] + 0.2, ps("também dá para descrever pela", "i", 80) + [("regra", "g", 90, COR)], W / 2, 200, "center", 0.11)
        E.frase(c, t, ka, ps("algarismos", "i", 76) + [("maiores que 6", "g", 76)], 860, 430, "right", 0.12)
        txe(c, t, kb, "= {7, 8, 9}", 920, 430, 110, "g", COR)
        E.frase(c, t, kc, ps("algarismos", "i", 76) + [("maiores que 9", "g", 76)], 860, 680, "right", 0.12)
        txe(c, t, entre(C, "s06.c", "s07", 0.7), "= nenhum", 920, 680, 110, "g", ERRADO)
    E.saida(c, t, C["s07"] - 0.1, regra)
    if t < C["s07"]:
        return
    ka, kb, kc = C["s07.a"], C["s07.b"], C["s07.c"]
    E.frase(c, t, ka, ps("o conjunto", "i", 110) + [("vazio", "g", 130, COR)], W / 2, 260, "center", 0.14)
    txe(c, t, kb, "{ }", 620, 690, 300, "g", TINTA, "center")
    E.frase(c, t, kb + 0.3, ps("chaves", "i", 64) + [("sem nada dentro", "g", 64)], 620, 860, "center", 0.1)
    E.frase(c, t, kc - 0.1, ps("ou", "i", 90, TINTA2), W / 2, 640, "center")
    txe(c, t, kc, "∅", 1300, 690, 300, "g", COR, "center")
    E.frase(c, t, kc + 0.3, ps("zero", "i", 64) + [("cortado", "g", 64, COR)], 1300, 860, "center", 0.1)


# ---------------- pertence ----------------
def b_pertence(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s08.{k}"] for k in "abcde")
    E.frase(c, t, C["s08"] + 0.2, ps("os símbolos", "i", 80, COR), XE, 170)
    E.frase(c, t, ka, ps("de", "i", 80) + [("elemento", "g", 84, COR)] + ps("para", "i", 80) + [("conjunto", "g", 84)], XE, 320, "left", 0.12)
    esfera(c, t, kb, 1500, 560, 200, "∈", 230)
    E.frase(c, t, kb + 0.3, [("pertence", "g", 84, COR)], 1500, 880, "center")
    txe(c, t, kc, "a ∈ V", XE, 580, 160)
    txe(c, t, kc + 0.4, "V = {a, e, i, o, u}", XE + 520, 570, 56, "b", TINTA2)
    E.frase(c, t, kc + 0.6, ps("a", "g", 56, CERTO) + ps("está lá dentro", "i", 56, CERTO), XE + 520, 640, "left", 0.1)
    txe(c, t, kd, "b ∈ V", XE, 860, 160)
    E.frase(c, t, kd + 0.4, ps("b", "g", 56, ERRADO) + ps("não está", "i", 56, ERRADO), XE + 520, 850, "left", 0.1)
    xb = XE + tw("b ", "g", 160)
    E.risco(c, xb + 120 * 0.92, 860 - 160 * 0.78, xb + 160 * 0.12, 860 + 22, t, ke, COR, 14)
    E.frase(c, t, ke + 0.4, ps("símbolo", "i", 56) + [("cortado", "g", 56, COR)], XE + 520, 920, "left", 0.1)


# ---------------- está contido ----------------
LETRAS = dict(a=(1300, 470), e=(1420, 600), i=(1610, 420), o=(1660, 640), u=(1480, 790))


def b_contido(c, t, C, b):
    def contido():
        ka, kb, kc, kd, ke = (C[f"s09.{k}"] for k in "abcde")
        E.frase(c, t, ka, ps("de", "i", 80) + [("conjunto", "g", 84)] + ps("para", "i", 80) + [("conjunto", "g", 84, COR)], XE, 170, "left", 0.12)
        esfera(c, t, kb, 330, 440, 130, "⊂", 170)
        E.frase(c, t, kb + 0.3, [("está contido", "g", 90, COR)], 500, 470)
        txe(c, t, kc, "{a, e} ⊂ V", XE, 720, 140)
        E.frase(c, t, kd, ps("cada elemento dele", "i", 64) + [("está em V", "g", 64, CERTO)], XE, 820, "left", 0.1)
        E.frase(c, t, ke, [("subconjunto:", "g", 72, COR)] + ps("um pedaço do conjunto", "i", 72), XE, 960, "left", 0.12)
        # V como região, com a e e cercados
        q = ease_io(prog(t, kc, 0.8))
        if q > 0:
            c.drawArc(skia.Rect.MakeXYWH(1160, 280, 640, 640), -90, 360 * q, False, M.paint(TINTA, 1.0, stroke=6, cap_round=True))
        E.foco(c, t, kc + 0.3, 0.4, lambda a: tx(c, "V", 1790, 320, 80, "g", TINTA, a))
        for i, (s, (x, y)) in enumerate(LETRAS.items()):
            cor = COR if s in "ae" and t >= kd else TINTA
            E.foco(c, t, kc + 0.3 + 0.12 * i, 0.4, lambda a, s=s, x=x, y=y, cor=cor: tx(c, s, x, y + 30, 90, "g", cor, a, "center"))
        p = ease_io(prog(t, kd, 0.7))
        if p > 0:
            c.drawArc(skia.Rect.MakeXYWH(1215, 395, 300, 280), 200, 360 * p, False, M.paint(COR, 1.0, stroke=7, cap_round=True))
        if t >= ke:
            c.drawOval(skia.Rect.MakeXYWH(1215, 395, 300, 280), M.paint(COR, 0.16 * ep(t, ke, 0.5)))
    E.saida(c, t, C["s10"] - 0.1, contido)
    if t < C["s10"]:
        return
    ka, kb = C["s10.a"], C["s10.b"]
    E.frase(c, t, C["s10"] + 0.2, ps("dois casos que", "i", 80) + [("surpreendem", "g", 84, COR)], W / 2, 180, "center", 0.12)
    for x, k, s, l1, l2 in ((520, ka, "V ⊂ V", "todo conjunto está", "contido nele mesmo"), (1400, kb, "∅ ⊂ V", "o vazio está contido", "em qualquer conjunto")):
        E.foco(c, t, k, 0.5, lambda a, x=x: E.caixa_pontilhada(c, x - 400, 290, 800, 640, a, prog_=a))
        txe(c, t, k + 0.2, s, x, 580, 190, "g", COR, "center")
        E.frase(c, t, k + 0.6, ps(l1, "i", 62), x, 770, "center", 0.08)
        E.frase(c, t, k + 0.9, ps(l2, "i", 62), x, 850, "center", 0.08)


# ---------------- contando os subconjuntos ----------------
def b_contar(c, t, C, b):
    ka, kb, kc, kd, ke, kf = (C[f"s11.{k}"] for k in "abcdef")
    E.frase(c, t, C["s11"] + 0.2, ps("os subconjuntos de", "i", 76), 820, 190, "right")
    txe(c, t, ka, "{1, 2, 3}", 860, 195, 110, "g", COR)
    linhas = ((kb, "1 elemento", ("{1}", "{2}", "{3}"), TINTA), (kc, "2 elementos", ("{1, 2}", "{1, 3}", "{2, 3}"), TINTA),
              (kd, "o próprio", ("{1, 2, 3}",), CERTO), (ke, "o vazio", ("∅",), CERTO))
    for i, (k, rot, sets, cor) in enumerate(linhas):
        y = 380 + i * 165
        E.frase(c, t, k, ps(rot, "i", 64, cor), 560, y, "right", 0.08)
        for j, s in enumerate(sets):
            txe(c, t, k + 0.2 + 0.18 * j, s, 620 + j * 330, y, 84, "g", cor)
    E.frase(c, t, entre(C, "s11.c", "s11.d", 0.45), ps("os que costumam", "i", 52, CERTO) + [("faltar", "g", 52, CERTO)], 1000, 800, "left", 0.1)
    E.frase(c, t, kf, ps("total", "i", 72), 1640, 330, "center")
    esfera(c, t, kf + 0.1, 1640, 520, 130, "8", 170)
    E.frase(c, t, kf + 0.5, ps("3 + 3 + 1 + 1", "b", 52, TINTA2), 1640, 730, "center", 0.05)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    def troca():
        ka, kb, kc, kd = (C[f"s12.{k}"] for k in "abcd")
        E.frase(c, t, ka - 0.3, [("cuidado:", "g", 84, ERRADO)] + ps("trocar os símbolos", "i", 84), W / 2, 170, "center", 0.12)
        txe(c, t, kb, "a ⊂ V", 560, 440, 170, "g", ERRADO, "center")
        E.risco(c, 360, 470, 760, 300, t, entre(C, "s12.b", "s12.c", 0.75), ERRADO, 14)
        txe(c, t, kc, "a ∈ V", 1360, 440, 170, "g", CERTO, "center")
        E.frase(c, t, kc + 0.4, ps("a sozinho é", "i", 60) + [("elemento:", "g", 60, CERTO)] + ps("pertence", "i", 60), 1360, 540, "center", 0.1)
        txe(c, t, entre(C, "s12.c", "s12.d", 0.55), "{a} ⊂ V", W / 2, 800, 170, "g", CERTO, "center")
        E.frase(c, t, kd, ps("entre chaves é", "i", 60) + [("conjunto:", "g", 60, CERTO)] + ps("está contido", "i", 60), W / 2, 910, "center", 0.1)
    E.saida(c, t, C["s13"] - 0.1, troca)
    if t < C["s13"]:
        return
    ka, kb, kc, kd = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.2, ps("antes de escrever, pergunte:", "i", 70, TINTA2), W / 2, 160, "center", 0.1)
    E.frase(c, t, ka, ps("o que está à esquerda é", "i", 76) + [("elemento", "g", 80, COR)] + ps("ou", "i", 76) + [("conjunto?", "g", 80, COR)],
            W / 2, 270, "center", 0.1)
    for x, k, nome, s in ((520, kb, "elemento", "∈"), (1400, kc, "conjunto", "⊂")):
        E.foco(c, t, k, 0.5, lambda a, x=x: E.caixa_pontilhada(c, x - 330, 360, 660, 400, a, prog_=a))
        E.frase(c, t, k + 0.1, [(nome, "g", 80)], x, 470, "center")
        txe(c, t, k + 0.3, s, x, 680, 190, "g", COR, "center")
    E.frase(c, t, entre(C, "s13.c", "s13.d", 0.3), ps("o vazio também é", "i", 70) + [("conjunto:", "g", 72)], 900, 920, "right", 0.1)
    txe(c, t, kd, "∅ ⊂ V", 960, 935, 130, "g", COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def escolhas():
        ka, kb, kc, kd = (C[f"s14.{k}"] for k in "abcd")
        E.frase(c, t, C["s14"] + 0.2, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("contar subconjuntos", "i", 90, CLARO) + [("sem listar", "g", 96, BR)], W / 2, 280, "center", 0.12)
        for i, n in enumerate("123"):
            x = 560 + i * 400
            esfera(c, t, kb + 0.2 * i, x, 450, 70, n, 90)
            E.foco(c, t, kb + 0.4 + 0.2 * i, 0.4, lambda a, x=x: (centro(c, "entra", x, 590, 52, "g", BR, a),
                                                                 centro(c, "ou fica fora", x, 650, 46, "i", CLARO, a)))
            E.foco(c, t, kc + 0.3 * i, 0.4, lambda a, x=x: centro(c, "2", x, 790, 110, "g", CLARO, a))
            if i:
                E.foco(c, t, kc + 0.3 * i - 0.15, 0.4, lambda a, x=x: centro(c, "×", x - 200, 780, 90, "g", CLARO, a))
        E.foco(c, t, kd, 0.5, lambda a: E.formula(c, "= 2^3 = 8", W / 2, 960, 110, "g", BR, a, "center"))
    E.saida(c, t, C["s15"] - 0.1, escolhas)

    def arvore():
        ka, kb, kc, kd = (C[f"s15.{k}"] for k in "abcd")
        E.frase(c, t, C["s15"] + 0.2, ps("cada escolha forma", "i", 72, CLARO) + [("um subconjunto diferente", "g", 72, BR)], W / 2, 140, "center", 0.1)
        q = ep(t, ka - 0.2, 0.5)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(260, 200, 1400, 820), 30, 30)
        c.drawRRect(r, M.paint(E.PAPEL, q))
        if q <= 0:
            return
        for i, n in enumerate("123"):
            E.foco(c, t, ka + 0.7 * i, 0.4, lambda a, i=i, n=n: centro(c, f"o {n} entra?", 700 + i * 355, 270, 46, "i", TINTA2, a))
        fim = lambda cam: "{" + ", ".join(str(i + 1) for i, s in enumerate(cam) if s == "sim") + "}" if "sim" in cam else "∅"
        dest = []
        if t >= kb:
            dest.append(("não",) * 3)
        if t >= kc:
            dest.append(("sim",) * 3)
        E.arvore(c, t, ka, [["sim", "não"]] * 3, 300, 300, 1300, 700, folha=fim, tn=[ka, ka + 0.7, ka + 1.4], tf=ka + 2.1,
                 destaque=tuple(dest), size=44)
    if t >= C["s15"] - 0.1:
        E.saida(c, t, C["s15.d"] - 0.1, arvore)
    if C["s15.d"] <= t < C["s16"]:
        kd = C["s15.d"]
        E.frase(c, t, kd, ps("nas vogais,", "i", 90, CLARO) + [("5 elementos", "g", 96, BR)], W / 2, 380, "center", 0.12)
        E.foco(c, t, kd + 0.6, 0.5, lambda a: E.formula(c, "2^5 = 32", W / 2, 640, 220, "g", BR, a, "center"))
        E.frase(c, t, entre(C, "s15.d", "s16", 0.7), [("subconjuntos", "i", 90, CLARO)], W / 2, 820, "center")
    if t < C["s16"]:
        return
    ka, kb = C["s16.a"], C["s16.b"]
    E.frase(c, t, C["s16"] + 0.2, [("não compensa", "g", 90, BR)] + ps("quando a questão pede", "i", 80, CLARO), W / 2, 200, "center", 0.12)
    E.frase(c, t, ka, [("quais são", "g", 120, CLARO)] + ps("os subconjuntos:", "i", 90, CLARO), W / 2, 360, "center", 0.12)
    E.frase(c, t, entre(C, "s16.a", "s16.b", 0.6), ps("aí, você", "i", 80, CLARO) + [("lista", "g", 90, BR)], W / 2, 480, "center", 0.12)
    E.frase(c, t, kb, ps("conte só os", "i", 80, CLARO) + [("diferentes", "g", 90, BR)], W / 2, 690, "center", 0.12)
    txe(c, t, kb + 0.6, "{a, a, e}", 800, 870, 110, "g", BR, "right")
    E.foco(c, t, kb + 0.9, 0.4, lambda a: centro(c, "→", 900, 860, 100, "g", CLARO, a))
    E.frase(c, t, kb + 1.1, [("2", "g", 110, CLARO)] + ps("elementos", "i", 80, CLARO), 1010, 870, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd = (C[f"s17.{k}"] for k in "abcd")
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    txe(c, t, ka, "P = {2, 5, 7, 9}", XE, 330, 120, "g", COR)
    fz(c, t, kb, [("5", "g", 100), ("pertence", "i", 80), ("ou", "i", 80), ("está contido", "i", 80), ("em P?", "g", 84)], XE, 520, "left", 0.1)
    fz(c, t, kc, [("e", "i", 80), ("{5, 7}", "g", 100), ("?", "g", 100)], XE, 690, "left", 0.1)
    fz(c, t, kd, [("quantos", "i", 84), ("subconjuntos", "g", 90, COR), ("P tem?", "i", 84)], XE, 870, "left", 0.1)
    E.relogio(c, t, C["s18.a"], 1560, 400, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def simbolos():
        ka, kb = C["s19.a"], C["s19.b"]
        txe(c, t, C["s19"] + 0.3, "P = {2, 5, 7, 9}", W / 2, 200, 96, "g", TINTA2, "center")
        E.frase(c, t, entre(C, "s19", "s19.a", 0.5), ps("o 5 sozinho é", "i", 66) + [("elemento", "g", 70, COR)], 520, 400, "center", 0.1)
        txe(c, t, ka, "5 ∈ P", 520, 620, 190, "g", CERTO, "center")
        E.frase(c, t, entre(C, "s19.a", "s19.b", 0.4), ps("{5, 7} é", "i", 66) + [("conjunto", "g", 70, COR)], 1400, 400, "center", 0.1)
        txe(c, t, kb, "{5, 7} ⊂ P", 1400, 620, 160, "g", CERTO, "center")
        E.foco(c, t, ka + 0.4, 0.5, lambda a: E.selo(c, 520, 800, 56, True, a))
        E.foco(c, t, kb + 0.4, 0.5, lambda a: E.selo(c, 1400, 800, 56, True, a))
    E.saida(c, t, C["s20"] - 0.1, simbolos)
    if t < C["s20"]:
        return
    ka, kb, kc = C["s20.a"], C["s20.b"], C["s20.c"]
    E.frase(c, t, C["s20"] + 0.2, ps("P tem", "i", 80) + [("4 elementos", "g", 84, COR)], XE, 220, "left", 0.12)
    E.formula_em(c, t, ka, "2^4", XE, 470, 200, "g", COR)
    for i, n in enumerate(("2", "4", "8", "16")):
        x = 640 + i * 280
        E.foco(c, t, kb + 0.35 * i, 0.4, lambda a, x=x, n=n: centro(c, n, x, 450, 110, "g", TINTA if n != "16" else COR, a))
        if i:
            E.foco(c, t, kb + 0.35 * i - 0.15, 0.4, lambda a, x=x: (centro(c, "→", x - 140, 440, 70, "g", TINTA2, a),
                                                                   centro(c, "× 2", x - 140, 360, 44, "b", TINTA2, a)))
    esfera(c, t, kc, 1560, 760, 150, "16", 160, CERTO)
    E.frase(c, t, kc + 0.2, [("subconjuntos", "g", 80)], XE, 760)
    fz(c, t, entre(C, "s20.c", "s20.end", 0.4), [("contando", "i", 64), ("∅", "g", 80, COR), ("e", "i", 64), ("P", "g", 80, COR)], XE, 880)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s21.a", [("elemento", "g", 84), ("∈", "g", 96, COR), ("pertence", "i", 84)]),
                 ("s21.b", [("conjunto", "g", 84), ("⊂", "g", 96, COR), ("está contido", "i", 84)]),
                 ("s21.c", None))
        for i, (k, partes) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            if partes:
                fz(c, t, C[k] + 0.1, partes, 400, y)
            else:
                E.formula_em(c, t, C[k] + 0.1, "2^n", 400, y, 96, "g", COR)
                E.frase(c, t, C[k] + 0.3, ps("conta os subconjuntos", "i", 84), 560, y, "left", 0.1)
                E.frase(c, t, C[k] + 0.6, ps("n = número de elementos", "i", 52, TINTA2), 560, y + 70, "left", 0.06)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    ka, kb, kc, kd = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula, juntar e separar conjuntos", "i", 72), XE, 230, passo=0.1)
    E.frase(c, t, ka, [("união, interseção,", "g", 88, COR)], XE, 360)
    E.frase(c, t, ka + 0.5, [("diferença e complementar", "g", 88, COR)], XE, 470)
    E.frase(c, t, kb, ps("sem confundir", "i", 72) + [("e", "g", 80, COR)] + ps("com", "i", 72) + [("ou", "g", 80, COR)], XE, 600, passo=0.1)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 740, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(960, 765, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conjunto=b_conjunto, regra=b_regra, pertence=b_pertence, contido=b_contido,
              contar=b_contar, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
