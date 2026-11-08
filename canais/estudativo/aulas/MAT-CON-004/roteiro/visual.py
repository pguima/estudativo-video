"""Visual — Estudativo · MAT-CON-004: naturais, inteiros e racionais.
−3 ∈ ℤ e ∉ ℕ; 0,75 = 75/100 = 3/4 e 0,4545… = 5/11 são racionais; 5 = 5/1; ℕ ⊂ ℤ ⊂ ℚ em círculos um dentro do outro (familias()), com
números nas faixas. A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-004_naturais_inteiros_racionais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("naturais", "racionais", "escada", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
from fractions import Fraction as Fr
assert Fr(75, 100) == Fr(3, 4) == Fr("0.75") and abs(5 / 11 - 0.454545) < 1e-6 and Fr(12, 4) == 3 and Fr(18, 6) == 3
assert Fr(6, 10) == Fr(3, 5) and abs(1 / 3 - 0.3333) < 1e-3 and Fr(-1, 2) == Fr("-0.5")


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
    """fórmula com fração (f{3}{4}) que entra com foco"""
    E.formula_em(c, t, t0, s, x, y, size, "g", cor or TINTA, align)


def familias(c, t, cx, cy, R, tq, tz, tn, tnum=None, escuro=False):
    """ℕ dentro de ℤ dentro de ℚ: três círculos, cada um com o símbolo no alto da sua faixa e números de exemplo"""
    tinta = BR if escuro else TINTA
    circ = ((tq, cx, cy, R, "ℚ"), (tz, cx, cy + R * 0.22, R * 0.7, "ℤ"), (tn, cx, cy + R * 0.42, R * 0.4, "ℕ"))
    for i, (t0, x, y, r, s) in enumerate(circ):
        q = ease_io(prog(t, t0, 0.8))
        if q <= 0:
            continue
        c.drawCircle(x, y, r, M.paint(COR, 0.07 + 0.07 * i * q))
        c.drawArc(skia.Rect.MakeXYWH(x - r, y - r, 2 * r, 2 * r), -90, 360 * q, False, M.paint(tinta, 1.0, stroke=6, cap_round=True))
        E.foco(c, t, t0 + 0.3, 0.4, lambda a, x=x, y=y, r=r, s=s: tx(c, s, x, y - r + R * 0.2, R * 0.16, "g", COR if not escuro else CLARO, a, "center"))
    if tnum is None:
        return
    nums = (("0", cx - R * 0.1, cy + R * 0.52, tnum[0]), ("1", cx + R * 0.1, cy + R * 0.52, tnum[0]), ("2", cx, cy + R * 0.68, tnum[0]),
            ("−1", cx - R * 0.45, cy + R * 0.08, tnum[1]), ("−3", cx + R * 0.45, cy + R * 0.08, tnum[1]),
            ("f{3}{4}", cx - R * 0.82, cy - R * 0.1, tnum[2]), ("0,4545…", cx, cy - R * 0.55, tnum[2]), ("−0,5", cx + R * 0.8, cy - R * 0.12, tnum[2]))
    for s, x, y, t0 in nums:
        E.formula_em(c, t, t0, s, x, y, R * 0.125, "g", tinta, "center")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = (C[f"s01.{k}"] for k in "abcd")

    def perguntas():
        txe(c, t, ka, "−3 ∈ ℕ ?", 520, 430, 150, "g", TINTA, "center")
        E.frase(c, t, ka + 0.4, ps("é natural?", "i", 70), 520, 560, "center")
        txe(c, t, kb, "0,4545…", 1400, 400, 130, "g", TINTA, "center")
        E.frase(c, t, entre(C, "s01.b", "s01.c", 0.4), ps("não acaba nunca.", "i", 62), 1400, 510, "center", 0.08)
        E.frase(c, t, entre(C, "s01.b", "s01.c", 0.6), ps("pode ser", "i", 70) + [("fração?", "g", 76, COR)], 1400, 600, "center", 0.1)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 400, 780, 70, False, a))
        E.frase(c, t, kc + 0.1, [("não", "g", 110, ERRADO)], 500, 820)
        E.foco(c, t, kd, 0.5, lambda a: E.selo(c, 1280, 780, 70, True, a))
        E.frase(c, t, kd + 0.1, [("sim", "g", 110, CERTO)], 1380, 820)
    E.saida(c, t, C["s02"] - 0.1, perguntas)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.3), ps("cada número na", "i", 84) + [("sua família", "g", 90, COR)], XE, 450, passo=0.12)
    fz(c, t, entre(C, "s02.a", "s02.b", 0.6), [("ℕ", "g", 150, COR), ("ℤ", "g", 150, COR), ("ℚ", "g", 150, COR)], XE, 680, "left", 0.25)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "∈  ⊂", "pertence e contido"), ("s03.c", "−3", "negativos na reta"), ("s03.d", "0,4545…", "dízima"))
    for i, (k, s, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        txe(c, t, C[k] + 0.1, s, x + 44, y + 128, 80, "g", COR)
        E.frase(c, t, C[k] + 0.3, [(l2, "i", 58)], x + 450, y + 120)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.d", "s03.end", 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), x, 960, "left", 0.12)


# ---------------- naturais ----------------
def b_naturais(c, t, C, b):
    ka, kb, kc = C["s04.a"], C["s04.b"], C["s04.c"]
    E.frase(c, t, C["s04"] + 0.2, ps("os números de", "i", 84) + [("contar", "g", 90, COR)], XE, 220, "left", 0.12)
    ln(c, t, [("0", ka, COR), (", 1", ka + 0.3), (", 2", ka + 0.6), (", 3", ka + 0.9), (", …", ka + 1.4)], XE, 440, 150, "g")
    E.frase(c, t, entre(C, "s04.a", "s04.b", 0.45), ps("o", "i", 66) + [("zero entra:", "g", 70, COR)] + ps("quem não tem nada", "i", 66), XE, 570, "left", 0.1)
    E.frase(c, t, kb, ps("são os", "i", 90) + [("naturais", "g", 110, COR)], XE, 790, "left", 0.12)
    esfera(c, t, kc, 1520, 640, 230, "ℕ", 260)
    E.frase(c, t, kc + 0.4, ps("N maiúsculo, traço duplo", "i", 52, TINTA2), 1520, 960, "center", 0.06)


# ---------------- inteiros ----------------
def b_inteiros(c, t, C, b):
    def junta():
        ka, kb, kc = C["s05.a"], C["s05.b"], C["s05.c"]
        E.frase(c, t, C["s05"] + 0.2, ps("junte os", "i", 84) + [("negativos", "g", 90)], XE, 200, "left", 0.12)
        E.frase(c, t, ka, ps("são os", "i", 84) + [("inteiros", "g", 100, COR)], XE, 340, "left", 0.12)
        vx = E.reta(c, t, kb, 260, 1660, 620, -4, 4, range(-4, 5), lambda v: str(v).replace("-", "−"), size=56)
        for v in range(-4, 5):
            tv = kb + 0.3 + (0 if v >= 0 else 0.9 + 0.25 * (-v))
            E.foco(c, t, tv, 0.4, lambda a, v=v: c.drawCircle(vx(v), 620, 16, M.paint(COR if v < 0 else TINTA2, a)), blur=4)
        E.frase(c, t, kb + 0.5, ps("naturais", "i", 56, TINTA2), vx(2), 540, "center")
        E.frase(c, t, kb + 1.4, ps("e os negativos", "i", 56, COR), vx(-2), 540, "center", 0.08)
        txe(c, t, kc, "ℤ", 600, 920, 170, "g", COR, "center")
        E.frase(c, t, kc + 0.3, ps("Z de", "i", 70) + [("Zahl,", "g", 72)] + ps("número em alemão", "i", 70), 720, 900, "left", 0.1)
    E.saida(c, t, C["s06"] - 0.1, junta)
    if t < C["s06"]:
        return
    ka, kb, kc, kd = (C[f"s06.{k}"] for k in "abcd")
    E.frase(c, t, C["s06"] + 0.1, [("−3", "g", 150, COR)], W / 2, 260, "center")
    E.frase(c, t, ka, ps("pertence aos", "i", 76) + [("inteiros", "g", 80, CERTO)], 520, 460, "center", 0.1)
    E.frase(c, t, kb, ps("não pertence aos", "i", 76) + [("naturais", "g", 80, ERRADO)], 1400, 460, "center", 0.1)
    E.frase(c, t, entre(C, "s06.b", "s06.c", 0.45), ps("ninguém conta −3 objetos", "i", 60, TINTA2), 1400, 550, "center", 0.08)
    txe(c, t, kc, "−3 ∈ ℤ", 520, 780, 170, "g", CERTO, "center")
    txe(c, t, kd, "−3 ∉ ℕ", 1400, 780, 170, "g", ERRADO, "center")
    E.frase(c, t, kd + 0.6, ps("símbolo cortado", "i", 56, TINTA2), 1400, 900, "center", 0.08)


# ---------------- racionais ----------------
def b_racionais(c, t, C, b):
    def regra():
        ka, kb, kc, kd = (C[f"s07.{k}"] for k in "abcd")
        E.frase(c, t, C["s07"] + 0.2, ps("e os números", "i", 80) + [("quebrados?", "g", 84)], XE, 200, "left", 0.12)
        E.frase(c, t, ka, [("racional:", "g", 90, COR)] + ps("pode ser escrito como fração", "i", 76), XE, 350, "left", 0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.fracao(c, "inteiro", "inteiro", 620, 640, 96, TINTA, a))
        E.foco(c, t, kc, 0.5, lambda a: (E.escreve(c, "≠ 0", 860, 735, 96, "g", ERRADO, a)))
        E.frase(c, t, kc + 0.3, ps("o de baixo nunca é zero", "i", 56, ERRADO), 860, 820, "left", 0.08)
        esfera(c, t, kd, 1580, 600, 200, "ℚ", 230)
        E.frase(c, t, kd + 0.4, ps("Q de", "i", 60) + [("quociente", "g", 62, COR)], 1580, 900, "center", 0.1)
    E.saida(c, t, C["s08"] - 0.1, regra)

    def exato():
        ka, kb, kc, kd = (C[f"s08.{k}"] for k in "abcd")
        fm(c, t, ka, "0,75 = f{75}{100}", 260, 400, 130)
        E.foco(c, t, kb - 0.6, 0.4, lambda a: E.pilula(c, "÷ 25 em cima e embaixo", 1100, 240, 44, "b", fundo=TINTA, a=a))
        fm(c, t, kb, "= f{3}{4}", 940, 400, 130, COR)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 1440, 360, 56, True, a))
        E.frase(c, t, kc + 0.1, [("racional", "g", 84, CERTO)], 1520, 390)
        E.frase(c, t, entre(C, "s08.c", "s08.d", 0.3), ps("decimal que acaba: embaixo", "i", 62) + [("10, 100, 1000…", "g", 64)], XE, 680, "left", 0.08)
        E.frase(c, t, kd, ps("todo", "i", 84) + [("decimal exato", "g", 90, COR)] + ps("é racional", "i", 84), XE, 860, "left", 0.12)
    if C["s08"] - 0.1 <= t:
        E.saida(c, t, C["s09"] - 0.1, exato)

    def dizima():
        ka, kb, kc = C["s09.a"], C["s09.b"], C["s09.c"]
        E.frase(c, t, C["s09"] + 0.2, ps("e a", "i", 84) + [("dízima?", "g", 90, COR)], XE, 220, "left", 0.12)
        fm(c, t, ka, "5 ÷ 11 = 0,4545…", XE, 480, 140)
        E.frase(c, t, kb, ps("nasceu de uma fração:", "i", 76), XE, 700, "left", 0.1)
        fm(c, t, kb + 0.4, "f{5}{11}", 1000, 730, 120, COR)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, XE + 50, 870, 52, True, a))
        E.frase(c, t, kc + 0.1, [("racional,", "g", 84, CERTO)] + ps("mesmo sem acabar", "i", 76), XE + 130, 900, "left", 0.1)
    if C["s09"] - 0.1 <= t:
        E.saida(c, t, C["s10"] - 0.1, dizima)
    if t < C["s10"]:
        return
    ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
    E.frase(c, t, C["s10"] + 0.2, ps("e os", "i", 84) + [("inteiros?", "g", 90, COR)], XE, 220, "left", 0.12)
    fm(c, t, ka, "5 = f{5}{1}", 300, 480, 150)
    E.frase(c, t, ka + 0.6, ps("5 ÷ 1 = 5", "b", 54, TINTA2), 300, 640, "left", 0.05)
    fm(c, t, kb, "−3 = f{−3}{1}", 1050, 480, 150)
    E.frase(c, t, entre(C, "s10.b", "s10.c", 0.4), ps("em cima pode ser negativo; dividir por 1 não muda nada", "i", 52, TINTA2), W / 2, 760, "center", 0.05)
    E.frase(c, t, kc, ps("todo", "i", 84) + [("inteiro", "g", 90, COR)] + ps("também é", "i", 84) + [("racional", "g", 90, COR)], W / 2, 920, "center", 0.12)


# ---------------- na reta ----------------
def b_reta(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s11.{k}"] for k in "abcde")
    fmt = lambda v: str(v).replace("-", "−")
    E.frase(c, t, C["s11"] + 0.2, ps("na", "i", 84) + [("reta", "g", 90, COR)], XE, 200, "left", 0.12)
    y = 560
    vx = E.reta(c, t, C["s11"] + 0.3, 260, 1660, y, -2, 2, range(-2, 3), fmt, size=60)
    for v in range(-2, 3):
        E.foco(c, t, ka + 0.15 * (v + 2), 0.4, lambda a, v=v: c.drawCircle(vx(v), y, 18, M.paint(TINTA, a)), blur=4)
    E.frase(c, t, ka + 0.2, ps("passo inteiro", "i", 56, TINTA2), vx(1.5), 760, "center")
    q = ep(t, kb, 0.8)
    if q > 0:
        for v in range(-2, 2):
            M.line(c, vx(v) + 24, y, vx(v) + 24 + (vx(v + 1) - vx(v) - 48) * q, y, COR, 0.35, 14, cap_round=False)
    E.frase(c, t, kb + 0.3, ps("e os espaços entre eles", "i", 56, COR), vx(-1.5), 760, "center", 0.08)
    for k, v, s in ((kc, 0.75, "f{3}{4}"), (kd, -0.5, "−f{1}{2}")):
        E.foco(c, t, k, 0.4, lambda a, v=v: c.drawCircle(vx(v), y, 20, M.paint(COR, a)), blur=4)
        E.foco(c, t, k + 0.1, 0.4, lambda a, v=v: M.line(c, vx(v), y - 30, vx(v), y - 110, COR, a, 5))
        fm(c, t, k + 0.2, s, vx(v), y - 160, 80, COR, "center")
    E.frase(c, t, entre(C, "s11.d", "s11.e", 0.2), ps("= −0,5", "g", 60, TINTA2), vx(-0.5) + 90, 400, "left")
    E.frase(c, t, ke, ps("não são inteiros, mas", "i", 76) + [("ambos são racionais", "g", 80, CERTO)], W / 2, 920, "center", 0.1)


# ---------------- a escada ----------------
def b_escada(c, t, C, b):
    ka, kb, kc, kd = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s12"] + 0.2, ps("daí sai uma", "i", 80) + [("escada", "g", 84, COR)], XE, 200, "left", 0.12)
    fz(c, t, ka, [("todo", "i", 70), ("natural", "g", 74), ("é", "i", 70), ("inteiro", "g", 74, COR)], XE, 360)
    fz(c, t, kb, [("todo", "i", 70), ("inteiro", "g", 74), ("é", "i", 70), ("racional", "g", 74, COR)], XE, 470)
    txe(c, t, kc, "ℕ ⊂ ℤ ⊂ ℚ", XE, 720, 150, "g", COR)
    familias(c, t, 1450, 590, 380, kd - 0.2, kd, kd + 0.2, (kd + 0.5, kd + 0.8, kd + 1.1))


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.2, [("cuidado", "g", 90, ERRADO)], W / 2, 180, "center")
    E.frase(c, t, ka, ps("decimal que não acaba", "i", 76) + [("não pode ser fração?", "g", 76, ERRADO)], W / 2, 320, "center", 0.1)
    fm(c, t, kb, "0,4545… = f{5}{11}", W / 2, 560, 150, COR, "center")
    E.frase(c, t, entre(C, "s13.b", "s13.c", 0.45), ps("divida e confira: 5 ÷ 11", "i", 60, TINTA2), W / 2, 720, "center", 0.08)
    E.frase(c, t, kc, ps("não acabar", "i", 76) + [("não tira", "g", 80, CERTO)] + ps("ninguém dos racionais", "i", 76), W / 2, 850, "center", 0.1)
    E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "números que não viram fração: outra aula", W / 2, 980, 46, "b", fundo=TINTA, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def degraus():
        ka, kb, kc, kd, ke = (C[f"s14.{k}"] for k in "abcde")
        E.frase(c, t, C["s14"] + 0.2, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("suba a escada", "i", 84, CLARO) + [("de baixo para cima", "g", 84, BR)], W / 2, 280, "center", 0.12)
        for i, (k, s, sim) in enumerate(((kb, "é natural?", "ℕ"), (kc, "é inteiro?", "ℤ"), (kd, "vira fração?", "ℚ"))):
            x, y = 200 + i * 540, 920 - i * 170
            q = ep(t, k, 0.5)
            if q > 0:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - 90, 500, 120), 18, 18), M.paint(COR, 0.55 * q))
            E.frase(c, t, k, [(s, "g", 58, BR)], x + 30, y - 10)
            E.foco(c, t, k + 0.1, 0.4, lambda a, x=x, y=y, sim=sim: tx(c, sim, x + 450, y - 6, 72, "g", CLARO, a, "center"))
            if i < 2:
                E.foco(c, t, k + 0.4, 0.4, lambda a, x=x, y=y: centro(c, "não: sobe", x + 470, y - 120, 44, "i", CLARO, a))
        E.frase(c, t, ke, [("no primeiro sim, pare:", "g", 66, BR)], 170, 470)
        E.frase(c, t, ke + 0.6, ps("ele já está em todos de fora", "i", 58, CLARO), 170, 550, "left", 0.08)
    E.saida(c, t, C["s15"] - 0.1, degraus)
    if t < C["s15"]:
        return
    ka, kb, kc, kd = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, C["s15"] + 0.2, ps("cada um", "i", 76, CLARO) + [("está contido no seguinte", "g", 76, BR)], W / 2, 200, "center", 0.1)
    txe(c, t, ka, "ℕ ⊂ ℤ ⊂ ℚ", W / 2, 360, 120, "g", CLARO, "center")
    E.frase(c, t, kb, [("não compensa", "g", 80, BR)] + ps("julgar pela aparência", "i", 76, CLARO), W / 2, 540, "center", 0.1)
    fm(c, t, kc, "f{12}{4} = 3", 760, 760, 140, BR, "center")
    txe(c, t, kc + 0.8, "∈ ℕ", 1180, 790, 120, "g", CLARO, "center")
    E.frase(c, t, kd, ps("simplifique", "i", 84, CLARO) + [("antes de classificar", "g", 84, BR)], W / 2, 980, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    E.frase(c, t, C["s16"] + 1.0, ps("a que conjuntos pertence cada um?", "i", 70), XE, 290, "left", 0.08)
    for i, (k, s) in enumerate((("s16.a", "−7"), ("s16.b", "0,6"), ("s16.c", "0,333…"), ("s16.d", "f{18}{6}"))):
        x = 440 + (i % 2) * 600
        y = 520 + (i // 2) * 300
        fm(c, t, C[k], s, x, y, 140, COR, "center")
    E.relogio(c, t, C["s17.a"], 1560, 480, 170)


# ---------------- resposta ----------------
COLS = {"ℕ": 1230, "ℤ": 1460, "ℚ": 1690}


def b_resposta(c, t, C, b):
    k = lambda s: C[s]
    for s, x in COLS.items():
        txe(c, t, C["s18"] + 0.2, s, x, 200, 110, "g", COR, "center")
    linhas = ((k("s18.a"), "−7", "", (("ℕ", False, k("s18.a")), ("ℤ", True, k("s18.a") + 1.0), ("ℚ", True, k("s18.b")))),
              (k("s18.c"), "0,6", "= f{6}{10} = f{3}{5}", (("ℕ", False, k("s18.c") + 0.8), ("ℤ", False, k("s18.c") + 1.0), ("ℚ", True, k("s18.d")))),
              (k("s19.a"), "0,333…", "= f{1}{3}", (("ℕ", False, k("s19.b")), ("ℤ", False, k("s19.b")), ("ℚ", True, k("s19.b")))),
              (k("s19.c"), "f{18}{6}", "= 3", (("ℕ", True, k("s19.d")), ("ℤ", True, k("s19.d") + 0.2), ("ℚ", True, k("s19.d") + 0.4))))
    for i, (t0, s, conv, marcas) in enumerate(linhas):
        y = 380 + i * 180
        fm(c, t, t0, s, 170, y, 100)
        if conv:
            fm(c, t, t0 + (0.6 if i != 1 else entre(C, "s18.c", "s18.d", 0.6) - t0), conv, 640, y, 76, TINTA2)
        for col, ok, tm in marcas:
            E.foco(c, t, tm, 0.4, lambda a, x=COLS[col], y=y, ok=ok: E.selo(c, x, y - 30, 44, ok, a))
    E.frase(c, t, k("s19.c") - 0.1, [("pegadinha", "g", 52, ERRADO)], 900, 900)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("ℕ", "g", 96, COR), ("natural", "g", 80), ("conta", "i", 80)]),
                 ("s20.b", [("ℤ", "g", 96, COR), ("inteiro", "g", 80), ("ganha os negativos", "i", 80)]),
                 ("s20.c", [("ℚ", "g", 96, COR), ("racional", "g", 80), ("vira fração, até a dízima", "i", 80)]))
        for i, (kk, partes) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, C[kk], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            fz(c, t, C[kk] + 0.1, partes, 360, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    ka, kb, kc, kd = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula, o caminho de volta", "i", 76), XE, 240, passo=0.1)
    fm(c, t, ka, "0,4545… → f{5}{11}", XE, 440, 120, COR)
    E.frase(c, t, kb, ps("a", "i", 90) + [("fração geratriz", "g", 100, COR)], XE, 640, "left", 0.12)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(980, 785, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, naturais=b_naturais, inteiros=b_inteiros, racionais=b_racionais, reta=b_reta,
              escada=b_escada, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
