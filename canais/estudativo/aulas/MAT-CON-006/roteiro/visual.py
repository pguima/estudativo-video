"""Visual — Estudativo · MAT-CON-006: irracionais e números reais.
√16 = 4 e √7 = 2,6457… (entre 2 e 3); π = 3,14159…; ℝ = retângulo com ℕ ⊂ ℤ ⊂ ℚ dentro e os irracionais na faixa de fora de ℚ;
1,4 < √2 < 1,5 na reta de 1 a 2 (1,4² = 1,96 e 1,5² = 2,25). A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-006_irracionais_e_reais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("raizes", "irracional", "reais", "ordem", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
import math
assert 4 * 4 == 16 and 2 ** 2 < 7 < 3 ** 2 and abs(math.sqrt(7) - 2.6457) < 1e-4 and abs(1.4 ** 2 - 1.96) < 1e-9 and abs(1.5 ** 2 - 2.25) < 1e-9
assert 1.4 < math.sqrt(2) < 1.5 and 3 / 2 == 1.5 and (-3) ** 2 == 9 > 4 == (-2) ** 2 and 5 * 5 == 25 and 9 < 10 < 16 and abs(3.2 ** 2 - 10.24) < 1e-9


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
    """fórmula (r{7}, f{3}{2}, 1,4^2) que entra com foco"""
    E.formula_em(c, t, t0, s, x, y, size, "g", cor or TINTA, align)


def reais(c, t, t0, x, y, w, h, tq, ti, irr=(), tr=None):
    """o retângulo ℝ com ℕ ⊂ ℤ ⊂ ℚ à esquerda e os irracionais na faixa de fora de ℚ. irr = [(fórmula, x, y, t0)]"""
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), M.paint(COR, 0.06 * q))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), M.paint(TINTA, q, stroke=5))
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: tx(c, "ℝ", x + 24, y + 96, 90, "g", COR, a))
    R = h * 0.38
    cx, cy = x + w * 0.36, y + h * 0.54
    for i, (t1, xx, yy, r, s) in enumerate(((tq, cx, cy, R, "ℚ"), (tq + 0.2, cx, cy + R * 0.22, R * 0.68, "ℤ"), (tq + 0.4, cx, cy + R * 0.42, R * 0.38, "ℕ"))):
        p = ease_io(prog(t, t1, 0.7))
        if p <= 0:
            continue
        c.drawCircle(xx, yy, r, M.paint(COR, 0.08 + 0.06 * i * p))
        c.drawArc(skia.Rect.MakeXYWH(xx - r, yy - r, 2 * r, 2 * r), -90, 360 * p, False, M.paint(TINTA, 1.0, stroke=5, cap_round=True))
        E.foco(c, t, t1 + 0.3, 0.4, lambda a, xx=xx, yy=yy, r=r, s=s: tx(c, s, xx, yy - r + R * 0.24, R * 0.2, "g", COR, a, "center"))
    E.foco(c, t, ti, 0.4, lambda a: E.escreve(c, "irracionais", x + w * 0.72 - E.larg("irracionais", "i", 52) / 2, y + 90, 52, "i", TINTA2, a))
    for s, xx, yy, t1 in irr:
        E.formula_em(c, t, t1, s, xx, yy, 70, "g", COR, "center")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def duas():
        fm(c, t, ka, "r{16}", 560, 440, 220, TINTA, "center")
        fm(c, t, ka + 0.5, "r{7}", 1360, 440, 220, TINTA, "center")
        E.frase(c, t, entre(C, "s01.a", "s01.b", 0.6), ps("parecem da mesma família", "i", 70, TINTA2), W / 2, 620, "center", 0.08)
        fm(c, t, kb, "= 4", 560, 800, 120, CERTO, "center")
        E.frase(c, t, kb + 0.4, [("natural", "g", 70, CERTO)], 560, 920, "center")
        E.frase(c, t, kc, ps("não vira", "i", 70, ERRADO) + [("fração", "g", 74, ERRADO)], 1360, 800, "center", 0.1)
        E.frase(c, t, kc + 0.4, ps("de jeito nenhum", "i", 70, ERRADO), 1360, 900, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, duas)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.2), ps("separar", "i", 84), XE, 450, passo=0.12)
    fm(c, t, entre(C, "s02.a", "s02.b", 0.3), "r{16}  e  r{7}", XE + 330, 450, 96, COR)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.55), ps("pôr raízes", "i", 84) + [("em ordem na reta", "g", 84, COR)], XE, 640, passo=0.12)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    E.caixa_pontilhada(c, x, 220, w, 230, ep(t, C["s03.b"], 0.5), prog_=ep(t, C["s03.b"], 0.5))
    E.frase(c, t, C["s03.b"] + 0.1, [("dízima com período", "i", 62), ("vira fração", "g", 64, COR)], x + 44, 300, "left", 0.1)
    fm(c, t, C["s03.b"] + 0.4, "0,444… = f{4}{9}", x + 44, 400, 64, COR)
    E.caixa_pontilhada(c, x, 500, w, 230, ep(t, C["s03.c"], 0.5), prog_=ep(t, C["s03.c"], 0.5))
    E.frase(c, t, C["s03.c"] + 0.1, [("raiz quadrada", "g", 64, COR)], x + 44, 590, "left", 0.1)
    fm(c, t, entre(C, "s03.c", "s03.end", 0.35), "r{9} = 3, porque 3 × 3 = 9", x + 44, 685, 60, TINTA2)
    py = lerp(430, 710, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.75), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 840, "left", 0.12)


# ---------------- √16 e √7 ----------------
def b_raizes(c, t, C, b):
    def quatro():
        ka, kb, kc = C["s04.a"], C["s04.b"], C["s04.c"]
        fm(c, t, ka, "r{16} = 4", XE, 300, 140, CERTO)
        fm(c, t, ka + 0.6, "4 × 4 = 16", XE + 620, 290, 76, TINTA2)
        E.frase(c, t, entre(C, "s04.a", "s04.b", 0.5), ps("natural, inteiro e racional", "i", 64, CERTO), XE, 410, "left", 0.08)
        fm(c, t, kb, "r{7}", XE, 640, 140)
        E.frase(c, t, kb + 0.3, ps("não é", "i", 72) + [("exata", "g", 76, ERRADO)], XE + 300, 630, "left", 0.1)
        fm(c, t, kc, "2 < r{7} < 3", XE, 880, 120, COR)
        fm(c, t, entre(C, "s04.c", "s05", 0.5), "2^2 = 4  e  3^2 = 9", XE + 820, 870, 76, TINTA2)
    E.saida(c, t, C["s05"] - 0.1, quatro)
    if t < C["s05"]:
        return
    ka, kb, kc = C["s05.a"], C["s05.b"], C["s05.c"]
    fm(c, t, ka, "r{7} = 2,6457…", W / 2, 330, 150, COR, "center")
    E.frase(c, t, ka + 0.6, ps("na calculadora, e muito mais", "i", 56, TINTA2), W / 2, 430, "center", 0.06)
    E.frase(c, t, kb, ps("não acaba", "g", 74) + ps("e", "i", 70) + ps("não tem período", "g", 74), W / 2, 590, "center", 0.12)
    E.frase(c, t, entre(C, "s05.b", "s05.c", 0.6), ps("como saber, se ninguém vê o fim?", "i", 60, TINTA2), W / 2, 690, "center", 0.06)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "já provado: não vira fração", W / 2, 820, 60, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, entre(C, "s05.c", "s05.end", 0.8), ps("aqui, você usa o fato", "i", 60, TINTA2), W / 2, 960, "center", 0.08)


# ---------------- irracional ----------------
def b_irracional(c, t, C, b):
    def regra():
        ka, kb, kc, kd = (C[f"s06.{k}"] for k in "abcd")
        E.frase(c, t, ka, [("irracional", "g", 140, COR)], W / 2, 240, "center")
        for i, s in enumerate(("não acaba", "não se repete", "não vira fração")):
            E.foco(c, t, kb + 0.5 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, 440 + i * 520, 400, 52, "g", fundo=TINTA, a=a))
        E.frase(c, t, kc, ps("raiz de natural que", "i", 66) + [("não é quadrado", "g", 70, COR)] + ps("de nenhum natural", "i", 66), W / 2, 600, "center", 0.08)
        for i, s in enumerate(("r{2}", "r{3}", "r{5}", "r{7}")):
            fm(c, t, entre(C, "s06.c", "s06.d", 0.4) + 0.2 * i, s, 560 + i * 270, 790, 110, COR, "center")
        E.frase(c, t, kd, [("sempre irracional", "g", 80, COR)], W / 2, 960, "center")
    E.saida(c, t, C["s07"] - 0.1, regra)
    if t < C["s07"]:
        return
    ka, kb, kc, kd = (C[f"s07.{k}"] for k in "abcd")
    E.frase(c, t, C["s07"] + 0.2, ps("o irracional mais", "i", 76) + [("famoso", "g", 80)], XE, 220, "left", 0.12)
    esfera(c, t, ka, 400, 560, 190, "π", 260)
    fm(c, t, kb, "3,14159…", 700, 520, 150, COR)
    E.frase(c, t, kb + 0.6, ps("sem fim e sem repetir", "i", 60, TINTA2), 700, 620, "left", 0.08)
    E.foco(c, t, kc, 0.4, lambda a: E.pilula(c, "de onde vem: aula de circunferência", 1160, 760, 46, "b", fundo=TINTA, a=a))
    fm(c, t, kd, "3,14", 700, 940, 100)
    E.frase(c, t, kd + 0.4, ps("é só um", "i", 66) + [("valor aproximado", "g", 70, COR)] + ps("de", "i", 66) + [("π", "g", 70, COR)], 960, 930, "left", 0.1)


# ---------------- os reais ----------------
RX, RY, RW, RH = 980, 170, 870, 780


def b_reais(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    irr = (("r{2}", RX + RW * 0.8, RY + 260, e8 + 0.2), ("r{7}", RX + RW * 0.86, RY + 450, e8 + 0.4), ("π", RX + RW * 0.8, RY + 640, e8 + 0.6))
    reais(c, t, b8, RX, RY, RW, RH, d8, e8, irr)

    def texto():
        E.frase(c, t, C["s08"] + 0.2, ps("racionais", "g", 58) + ps("+", "g", 58, COR) + ps("irracionais", "g", 58), XE, 230, "left", 0.15)
        E.frase(c, t, a8, ps("os números", "i", 80) + [("reais", "g", 90, COR)], XE, 360, "left", 0.12)
        E.frase(c, t, c8, ps("todos os pontos", "i", 64) + [("da reta", "g", 66, COR)], XE, 500, "left", 0.1)
        vx = E.reta(c, t, c8 + 0.2, 200, 720, 640, -2, 2, range(-2, 3), lambda v: str(v).replace("-", "−"), size=40)
        q = ep(t, c8 + 0.6, 0.8)
        if q > 0:
            M.line(c, 150, 640, 150 + 630 * q, 640, COR, 1.0, 10, cap_round=False)
        txe(c, t, d8, "ℚ ⊂ ℝ", XE, 830, 110, "g", COR)
    E.saida(c, t, C["s09"] - 0.1, texto)
    if t < C["s09"]:
        return
    ka, kb, kc = C["s09.a"], C["s09.b"], C["s09.c"]
    fm(c, t, ka, "r{−4}", 420, 360, 140, ERRADO, "center")
    E.frase(c, t, kb, ps("não dá", "i", 66) + [("número da reta", "g", 70, ERRADO)], 460, 560, "center", 0.1)
    wq = E.formula(c, "r{−4}", 0, 0, 110, a=0)
    E.foco(c, t, kc, 0.5, lambda a: (E.formula(c, "r{−4}", 200, 780, 110, "g", ERRADO, a), tx(c, "∉ ℝ", 230 + wq, 780, 110, "g", ERRADO, a)))


# ---------------- ordem na reta ----------------
def b_ordem(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"] + 0.2, ps("ponha em ordem", "i", 70, COR), XE, 150)
    for i, (k, s) in enumerate(((a0, "1,4"), (b0, "r{2}"), (c0, "f{3}{2}"))):
        fm(c, t, k, s, 330 + i * 300, 290, 100, TINTA, "center")
    fm(c, t, a1, "= 1,5", 1050, 290, 90, TINTA2)
    fm(c, t, b1, "1,4^2 = 1,96 < 2", XE, 470, 80)
    fm(c, t, c1, "1,5^2 = 2,25 > 2", XE, 590, 80)
    E.frase(c, t, d1, ps("então", "i", 64) + ps("√2", "g", 70, COR) + ps("fica no meio", "i", 64), 1000, 530, "left", 0.1)
    y = 820
    vx = E.reta(c, t, C["s12"], 260, 1660, y, 1.3, 1.6, (1.3, 1.4, 1.5, 1.6), lambda v: f"{v:.1f}".replace(".", ","), size=52)
    for k, v, s, dy in ((a2, 1.4, "1,4", 60), (b2, 2 ** 0.5, "r{2}", 170), (c2, 1.5, "f{3}{2}", 60)):
        E.foco(c, t, k, 0.4, lambda a, v=v: c.drawCircle(vx(v), y, 16, M.paint(COR, a)), blur=4)
        if dy > 100:
            E.foco(c, t, k + 0.1, 0.4, lambda a, v=v: M.line(c, vx(v), y - 26, vx(v) + 60, y - 110, COR, a, 4))
        fm(c, t, k + 0.1, s, vx(v) + (90 if dy > 100 else 0), y - dy, 64, COR, "center")
    E.frase(c, t, d2, ps("cada número tem o", "i", 58) + [("seu ponto", "g", 62, COR)], W / 2, 1000, "center", 0.08)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = (C[f"s13.{k}"] for k in "abcd")
    E.frase(c, t, C["s13"] + 0.2, [("cuidado", "g", 90, ERRADO)], W / 2, 180, "center")
    E.frase(c, t, ka, ps("todo decimal sem fim", "i", 76) + [("é irracional?", "g", 80, ERRADO)], W / 2, 330, "center", 0.1)
    w0 = E.formula(c, "0,444…", 0, 0, 150, a=0)
    fm(c, t, kb, "0,444…", 360, 560, 150)
    E.frase(c, t, entre(C, "s13.b", "s13.c", 0.5), ps("não acaba, mas tem período", "i", 60, TINTA2), 360 + w0 / 2, 680, "center", 0.06)
    fm(c, t, kc, "= f{4}{9}", 400 + w0, 560, 140, CERTO)
    E.frase(c, t, kc + 0.4, [("racional", "g", 76, CERTO)], 400 + w0 + E.formula(c, "= f{4}{9}", 0, 0, 140, a=0) + 50, 545)
    E.frase(c, t, kd, [("irracional:", "g", 76, COR)] + ps("não acaba", "i", 72) + [("e", "g", 76)] + ps("não se repete", "i", 72), W / 2, 880, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def quadrado():
        ka, kb = C["s14.a"], C["s14.b"]
        E.frase(c, t, C["s14"] + 0.2, ps("agora, o atalho para comparar raiz com decimal", "i", 64, CLARO), W / 2, 170, "center", 0.07)
        E.frase(c, t, ka, ps("eleve tudo", "i", 96, CLARO) + [("ao quadrado", "g", 104, BR)], W / 2, 400, "center", 0.12)
        fm(c, t, kb, "(r{2})^2 = 2", W / 2, 640, 140, BR, "center")
        E.frase(c, t, kb + 0.5, ps("a raiz", "i", 70, CLARO) + [("desaparece", "g", 76, BR)], W / 2, 830, "center", 0.1)
    E.saida(c, t, C["s15"] - 0.1, quadrado)
    if t < C["s15"]:
        return
    ka, kb, kc, kd = (C[f"s15.{k}"] for k in "abcd")
    E.frase(c, t, ka, ps("entre positivos, o maior tem o", "i", 70, CLARO) + [("quadrado maior", "g", 74, BR)], W / 2, 220, "center", 0.08)
    E.frase(c, t, kb, [("não compensa", "g", 84, BR)] + ps("com negativos", "i", 80, CLARO), W / 2, 420, "center", 0.1)
    fm(c, t, kc, "−3 < −2", 600, 650, 130, BR, "center")
    fm(c, t, entre(C, "s15.c", "s15.d", 0.4), "(−3)^2 = 9", 1300, 620, 90, CLARO, "center")
    fm(c, t, entre(C, "s15.c", "s15.d", 0.7), "(−2)^2 = 4", 1300, 740, 90, CLARO, "center")
    fm(c, t, kd, "9 > 4", 1300, 920, 130, ERRADO, "center")
    E.frase(c, t, kd + 0.4, ps("a ordem virou", "i", 60, CLARO), 600, 900, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd, ke, kf = (C[f"s16.{k}"] for k in "abcdef")
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    for i, (k, s) in enumerate(((ka, "r{25}"), (kb, "r{10}"), (kc, "0,1212…"), (kd, "−4"))):
        fm(c, t, k, s, (260, 580, 990, 1360)[i], 380, 96, COR, "center")
    E.frase(c, t, ke, ps("qual é", "i", 80) + [("irracional?", "g", 84, COR)], XE, 560, "left", 0.1)
    E.frase(c, t, kf, ps("ponha em ordem:", "i", 76), XE, 760, "left", 0.1)
    fm(c, t, kf + 0.5, "3,   r{10},   3,2", XE, 900, 100, COR)
    E.relogio(c, t, C["s17.a"], 1560, 660, 160)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def classifica():
        ka, kb, kc, kd, ke = (C[f"s18.{k}"] for k in "abcde")
        linhas = ((ka, "r{25} = 5", "natural", TINTA), (kb, "0,1212… = f{4}{33}", "racional", TINTA), (kc, "−4", "inteiro", TINTA))
        for i, (k, s, rot, cor) in enumerate(linhas):
            y = 240 + i * 170
            fm(c, t, k, s, XE, y, 84, cor)
            E.frase(c, t, k + 0.4, [(rot, "i", 64, TINTA2)], 1000, y - 10)
        fm(c, t, kd, "9 < 10 < 16", XE, 820, 90)
        E.frase(c, t, kd + 0.4, ps("10 não é quadrado de natural", "i", 56, TINTA2), XE + 620, 810, "left", 0.06)
        fm(c, t, ke, "r{10}", XE, 990, 110, COR)
        E.frase(c, t, ke + 0.3, [("é a irracional", "g", 80, COR)], XE + 240, 980)
    E.saida(c, t, C["s19"] - 0.1, classifica)
    if t < C["s19"]:
        return
    ka, kb, kc, kd = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.2, ps("para a ordem,", "i", 70) + [("eleve ao quadrado", "g", 74, COR)], XE, 200, "left", 0.1)
    fm(c, t, ka, "3^2 = 9", XE, 380, 96)
    fm(c, t, kb, "(r{10})^2 = 10", XE, 530, 96)
    fm(c, t, kc, "3,2^2 = 10,24", XE, 680, 96)
    fm(c, t, kd, "3 < r{10} < 3,2", W / 2, 900, 130, CERTO, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("ℚ", "g", 96, COR), ("racional", "g", 80), ("vira fração", "i", 80)]),
                 ("s20.b", [("irracional", "g", 80), ("não acaba e não se repete", "i", 80)]),
                 ("s20.c", [("ℝ", "g", 96, COR), ("reais:", "g", 80), ("todos os pontos da reta", "i", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            fz(c, t, C[k] + 0.1, partes, 360, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    ka, kb, kc, kd = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula,", "i", 76), XE, 240, passo=0.1)
    E.frase(c, t, ka, [("pedaços inteiros da reta", "g", 90, COR)], XE, 380)
    E.frase(c, t, entre(C, "s21.a", "s21.b", 0.4), ps("todos os reais entre 2 e 5", "i", 66), XE, 490, "left", 0.08)
    E.frase(c, t, kb, ps("com", "i", 80) + [("colchetes", "g", 90, COR)], XE, 640, "left", 0.12)
    E.foco(c, t, kb + 0.3, 0.5, lambda a: E.escreve(c, "[2, 5]", XE + 620, 650, 120, "g", COR, a))
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(980, 785, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, raizes=b_raizes, irracional=b_irracional, reais=b_reais, ordem=b_ordem,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
