"""Visual — Estudativo · MAT-CON-009: praticando conjuntos e números reais (5 situações).
1) Venn 80 pessoas: 12, 33, 26 e 9 fora; 2) quadro ℕ ℤ ℚ irracional ℝ; 3) 0,2777… = 25/90 = 5/18; 4) 5 − 2x ≥ −3 → x ≤ 4 → ]−∞, 4]; 5) com ]1, 6[: ∩ = ]1, 4], ∪ = ]−∞, 6[.
Bolinha e pintura na mesma linguagem da MAT-EQU-015 (bolinha(), pinta()). A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_out, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-009_praticando_conjuntos_e_reais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "atalho", "fim"))
BR = "#FFFFFF"
# as contas da aula
import math
from fractions import Fraction as Fr
assert 45 - 12 == 33 and 38 - 12 == 26 and 12 + 33 + 26 == 71 == 45 + 38 - 12 and 80 - 71 == 9 and 6 * 6 == 36 and Fr(7, 4) == Fr("1.75") and 1 < 3 < 4
assert Fr(25, 90) == Fr(5, 18) and 27 - 2 == 25 and 100 * Fr(5, 18) - 10 * Fr(5, 18) == 25 and Fr(27, 99) != Fr(5, 18) and abs(5 / 18 - 0.27777) < 1e-4
assert (-3 - 5) / -2 == 4 and 5 - 2 * 0 >= -3 and max(1, -99) == 1 and min(4, 6) == 4 and 1 < 2 <= 4


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


MENOS = lambda v: (f"{v:g}" if isinstance(v, float) else str(v)).replace("-", "−").replace(".", ",")


def fm(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor or TINTA, align)


def bolinha(c, t, t0, x, y, fecha, cor=None, r=19, escuro=False):
    """bolinha da reta, como na MAT-EQU-015: cheia = o número entra; aberta = fica de fora"""
    cor = cor or COR
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0:
        return
    rr = r * k
    c.drawCircle(x, y, rr, M.paint(cor if fecha else ("#07070F" if escuro else E.PAPEL)))
    c.drawCircle(x, y, rr, M.paint(cor, 1.0, stroke=7))


def pinta(c, t, t0, x_ini, x_fim, y, cor=None, d=0.9, seta=None):
    """trecho pintado da reta, crescendo de x_ini para x_fim; seta=True põe a ponta de seta no fim (pedaço sem fim)"""
    p = ease_out(prog(t, t0, d))
    if p <= 0:
        return
    cor = cor or COR
    xm = lerp(x_ini, x_fim, p)
    M.line(c, x_ini, y, xm, y, cor, 1.0, 12, cap_round=False)
    if seta and p >= 0.99:
        lado = 1 if x_fim > x_ini else -1
        M.line(c, x_fim, y, x_fim - lado * 26, y - 18, cor, 1.0, 8)
        M.line(c, x_fim, y, x_fim - lado * 26, y + 18, cor, 1.0, 8)


def ponto(c, t, t0, x, y, cor, r=15):
    E.foco(c, t, t0, 0.4, lambda a: c.drawCircle(x, y, r, M.paint(cor, a)), blur=4)


def relacao(c, a, esq, sig, dir_, y, size, cor=None, xm=W / 2, cor_sig=None):
    """inequação alinhada pelo sinal em xm (mesma montagem da MAT-EQU-015)"""
    g = size * 0.5
    E.formula(c, esq, xm - g, y, size, "g", cor, a, "right")
    centro(c, sig, xm, y, size, "g", cor_sig or cor, a)
    E.formula(c, dir_, xm + g, y, size, "g", cor, a)


def pilha(c, t, linhas, ops, xm, y0, dy, size):
    g = size * 0.5
    for k, (t0, esq, sig, dir_) in enumerate(linhas):
        y = y0 + k * dy
        ult = k == len(linhas) - 1
        velha = not ult and t >= linhas[k + 1][0]
        cor = COR if ult else (CINZA if velha else TINTA)
        E.foco(c, t, t0, 0.5, lambda a, esq=esq, sig=sig, dir_=dir_, y=y, cor=cor: relacao(c, a, esq, sig, dir_, y, size, cor, xm))
        if k < len(ops):
            to, op = ops[k]
            we = E.formula(c, esq, 0, 0, size, a=0)
            wd = E.formula(c, dir_, 0, 0, size, a=0)
            cop = CINZA if velha else COR
            yo = y + size * 0.72
            for cx in (xm - g - we / 2, xm + g + wd / 2):
                E.foco(c, t, to, 0.45, lambda a, cx=cx, cop=cop: E.formula(c, op, cx, yo, size * 0.52, "b", cop, a, "center"), sobe=8)


def colchetes(c, t, t0, s, cx, y, size, cores=None, align="center"):
    """intervalo escrito grande; cores = {índice do caractere: cor} para acender um colchete"""
    w = E.larg(s, "g", size)
    x = cx - w / 2 if align == "center" else cx

    def desenha(a):
        xx = x
        f = E.fonte("g", size)
        for i, ch in enumerate(s):
            E.escreve(c, ch, xx, y, size, "g", (cores or {}).get(i, TINTA), a)
            xx += f.measureText(ch) + E.APERTO["g"] * size
    E.foco(c, t, t0, 0.5, desenha)
    return x


# ---------------- a pilha de retas ----------------
X0, X1 = 520, 1720  # todas as retas da pilha com os mesmos números alinhados


def vx_de(vmin, vmax):
    return lambda v: X0 + (v - vmin) / (vmax - vmin) * (X1 - X0)


def trecho(c, t, t0, vx, y, a, b, fa, fb, cor=None, tb=None):
    """intervalo na reta: pinta de a a b e põe as bolinhas (tb = instante das bolinhas, se vierem antes ou depois)"""
    pinta(c, t, t0 + 0.2, vx(a), vx(b), y, cor)
    tb = t0 if tb is None else tb
    bolinha(c, t, tb, vx(a), y, fa, cor)
    bolinha(c, t, tb, vx(b), y, fb, cor)


def faixa(c, t, t0, x0, x1, y0, y1, cor=None, alfa=0.14, t1=None):
    """régua vertical sobre a parte que interessa"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    if t1 is not None:
        p *= 1 - ep(t, t1, 0.4)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, y0, x1, y1), 14, 14), M.paint(cor or COR, alfa * p))


def rotulo(c, t, t0, s, y, cor=None, cores=None):
    colchetes(c, t, t0, s, 280, y + 24, 76, cores)



def selo_numero(c, t, t0, n, x, y):
    """o número da situação numa esfera, no canto"""
    esfera(c, t, t0, x, y, 70, str(n), 90)


def vn(c, t, t0, cx, cy, r, nomes, numeros, tn, pinta=(), universo=None, size=58):
    p = [(it[0], it[1]) for it in pinta if len(it) < 3 or t < it[2]]
    return E.venn(c, t, t0, cx, cy, r, nomes, numeros=numeros, pinta=p, universo=universo, size=size, tn=tn)


def situacao(c, t, C, n, sid, titulo):
    """cabeçalho das telas de questão: esfera com o número + título"""
    selo_numero(c, t, C[sid + ".a"], n, 240, 190)
    E.frase(c, t, C[sid + ".a"] + 0.2, ps("situação", "i", 70, COR) + [(titulo, "g", 72)], 340, 215, "left", 0.1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb = C["s01.a"], C["s01.b"]
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "5", XE - 8, 640, 420, "g", COR, a))
    E.frase(c, t, ka + 0.2, [("situações", "i", 130)], XE + 300, 600)
    E.frase(c, t, ka + 0.8, ps("com tudo da trilha de", "i", 66) + [("conjuntos e reais", "g", 70, COR)], XE, 960, "left", 0.08)
    E.relogio(c, t, kb, 1520, 360, 140)
    E.frase(c, t, entre(C, "s01.b", "s01.end", 0.3), ps("resolva antes", "i", 66) + [("da resposta", "g", 70)], 1520, 720, "center", 0.1)
    E.frase(c, t, entre(C, "s01.b", "s01.end", 0.6), ps("errar aqui", "i", 58, TINTA2) + [("ensina", "g", 62, COR)], 1520, 810, "center", 0.1)


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.2, ps("você vai usar", "i", 80) + [("4 ferramentas", "g", 84, COR)], XE, 190, "left", 0.12)
    caixas = (("s02.a", 170, 280), ("s02.b", 990, 280), ("s02.c", 170, 640), ("s02.d", 990, 640))
    for k, x, y in caixas:
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, 760, 320, p, prog_=p)
    ka, kb, kc, kd = (C[f"s02.{k}"] for k in "abcd")
    vn(c, t, ka + 0.1, 550, 440, 70, ("A", "B"), {"AB": "12"}, {"AB": ka + 0.5}, size=32)
    E.frase(c, t, ka + 0.3, ps("Venn, de", "i", 50) + [("dentro para fora", "g", 52, COR)], 550, 570, "center", 0.06)
    txe(c, t, kb + 0.1, "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ", 1370, 440, 80, "g", COR, "center")
    E.frase(c, t, kb + 0.3, ps("a escada dos números", "i", 52), 1370, 540, "center", 0.06)
    fm(c, t, kc + 0.1, "0,444… = f{4}{9}", 550, 800, 96, COR, "center")
    E.frase(c, t, kc + 0.3, ps("fração geratriz", "i", 52), 550, 910, "center", 0.06)
    colchetes(c, t, kd + 0.1, "]2, 5]", 1370, 800, 110, {0: ERRADO, 5: CERTO})
    E.frase(c, t, kd + 0.3, ps("intervalos na reta", "i", 52), 1370, 910, "center", 0.06)


# ---------------- situação 1: Venn ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C, 1, "s03", "Venn")
    for i, (k, n, s) in enumerate((("s03.b", "80", "pessoas"), ("s03.c", "45", "filmes"), ("s03.d", "38", "música"), ("s03.e", "12", "ambos"))):
        y = 380 + i * 115
        E.foco(c, t, C[k], 0.45, lambda a, n=n, y=y: E.escreve(c, n, XE, y, 90, "g", COR, a))
        E.frase(c, t, C[k] + 0.1, ps(s, "i", 66), XE + 160, y, "left")
    E.frase(c, t, C["s03.f"], ps("quantas", "i", 64) + [("não assinam nenhum?", "g", 66, COR)], XE, 880, "left", 0.08)
    E.frase(c, t, C["s03.g"], ps("quantas assinam", "i", 64) + [("só filmes?", "g", 66, COR)], XE, 980, "left", 0.08)
    if t < C["s04"]:
        vn(c, t, C["s03.c"], 1330, 560, 190, ("filmes", "música"), {"": "?"}, {"": C["s03.f"]}, universo="80", size=52)
    E.relogio(c, t, C["s04.a"], 1400, 520, 170)


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    pin = [("AB", a5, b5), ("A", b5, c5), ("B", c5, d5), ("A", d5, e5), ("AB", d5, e5), ("B", d5, e5), ("", e5, C["s06"]), ("A", c6)]
    vn(c, t, C["s05"] + 0.1, 540, 600, 230, ("filmes", "música"), {"AB": "12", "A": "33", "B": "26", "": "9"},
       {"AB": a5, "A": b5 + 0.8, "B": c5 + 0.8, "": e5 + 0.6}, pin, universo="80 pessoas", size=58)
    XD = 1090

    def contas():
        E.frase(c, t, C["s05"] + 0.2, ps("de dentro para fora", "i", 66, TINTA2), XD, 220, "left", 0.08)
        fm(c, t, b5, "só filmes: 45 − 12 = 33", XD, 360, 64)
        fm(c, t, c5, "só música: 38 − 12 = 26", XD, 470, 64)
        fm(c, t, d5, "12 + 33 + 26 = 71", XD, 600, 76)
        fm(c, t, e5, "80 − 71 = 9", XD, 760, 100, CERTO)
        E.frase(c, t, e5 + 0.5, ps("não assinam nenhum", "i", 60, CERTO), XD, 850, "left", 0.08)
    E.saida(c, t, C["s06"] - 0.1, contas)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("pela fórmula, o mesmo", "i", 66, TINTA2), XD, 220, "left", 0.08)
    fm(c, t, a6, "45 + 38 = 83", XD, 380, 84)
    fm(c, t, b6, "83 − 12 = 71", XD, 520, 84, COR)
    E.frase(c, t, b6 + 0.5, ps("os 12 foram contados duas vezes", "i", 50, TINTA2), XD, 590, "left", 0.06)
    E.frase(c, t, c6, [("33", "g", 110, CERTO)], XD, 820)
    E.frase(c, t, c6 + 0.3, ps("assinam só filmes", "i", 66, CERTO), XD + 200, 805, "left", 0.08)


# ---------------- situação 2: classificar ----------------
NUM2 = (("s07.b", "r{36}"), ("s07.c", "−5"), ("s07.d", "f{7}{4}"), ("s07.e", "r{3}"))


def b_questao2(c, t, C, b):
    situacao(c, t, C, 2, "s07", "classificar")
    for i, (k, s) in enumerate(NUM2):
        fm(c, t, C[k], s, 300 + i * 300, 470, 120, COR, "center")
    f = C["s07.f"]
    for i, (s1, s2) in enumerate((("qual é", "natural?"), ("inteiro,", "mas não natural?"), ("racional,", "mas não inteiro?"), ("e qual é", "irracional?"))):
        E.frase(c, t, f + 1.0 * i, ps(s1, "i", 60) + [(s2, "g", 62)], XE, 680 + i * 95, "left", 0.08)
    E.relogio(c, t, C["s08.a"], 1560, 760, 150)


COLS2 = (("ℕ", 900), ("ℤ", 1120), ("ℚ", 1340), ("irrac.", 1580), ("ℝ", 1800))


def b_resposta2(c, t, C, b):
    t0 = C["s09"] + 0.2
    for s, x in COLS2:
        txe(c, t, t0, s, x, 200, 90 if len(s) == 1 else 54, "g", COR, "center")
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    linhas = ((a9, "r{36} = 6", "natural", (True, True, True, False)),
              (b9, "−5", "inteiro", (False, True, True, False)),
              (c9, "f{7}{4} = 1,75", "racional", (False, False, True, False)),
              (a0, "r{3}", "irracional", (False, False, False, True)))
    for i, (k, s, rot, marcas) in enumerate(linhas):
        y = 370 + i * 175
        fm(c, t, k, s, XE, y, 90)
        tm = b0 if i == 3 else k + 0.8
        for j, ok in enumerate(marcas):
            E.foco(c, t, tm + 0.15 * j, 0.4, lambda a, x=COLS2[j][1], y=y, ok=ok: E.selo(c, x, y - 30, 40, ok, a))
        E.foco(c, t, c0 + 0.15 * i, 0.4, lambda a, y=y: E.selo(c, COLS2[4][1], y - 30, 40, True, a))
    E.frase(c, t, entre(C, "s10.a", "s10.b", 0.3), ps("1 < 3 < 4: não é quadrado", "i", 46, TINTA2), XE, 970, "left", 0.05)
    E.frase(c, t, c0 + 0.6, ps("todos têm ponto na reta", "i", 50, COR), 1600, 1010, "center", 0.06)


# ---------------- situação 3: geratriz ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C, 3, "s11", "geratriz")
    fm(c, t, C["s11.b"], "0,2777…", XE, 560, 200, COR)
    E.frase(c, t, C["s11.c"], ps("na forma", "i", 72) + [("mais simples", "g", 76)], XE, 760, "left", 0.1)
    E.relogio(c, t, C["s12.a"], 1500, 480, 170)


def b_resposta3(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    cor2 = TINTA2 if t >= a3 else TINTA
    cor7 = COR if t >= b3 else TINTA
    ln(c, t, [("0,", C["s13"] + 0.2), ("2", C["s13"] + 0.2, cor2), ("777…", C["s13"] + 0.2, cor7)], XE, 230, 120, "g")
    E.frase(c, t, a3 + 0.3, ps("o 2 fica fora do período", "i", 50, TINTA2), XE + 640, 200, "left", 0.06)
    E.frase(c, t, b3, ps("período:", "i", 50, COR) + [("7", "g", 56, COR)], XE + 640, 260, "left", 0.06)

    def macete():
        E.frase(c, t, c3, [("em cima:", "g", 60, COR)], XE, 420)
        fm(c, t, c3 + 0.3, "27 − 2 = 25", XE + 300, 420, 76)
        E.frase(c, t, d3, [("embaixo:", "g", 60, COR)], XE, 540)
        fm(c, t, d3 + 0.3, "90", XE + 300, 540, 76)
        E.frase(c, t, d3 + 0.6, ps("um 9 pelo período, um 0 pelo 2", "i", 48, TINTA2), XE + 460, 535, "left", 0.05)
        fm(c, t, a4, "f{25}{90}", 1400, 470, 110)
        E.foco(c, t, b4 - 0.4, 0.4, lambda a: E.pilula(c, "÷ 5", 1590, 330, 44, "b", fundo=TINTA, a=a))
        fm(c, t, b4, "= f{5}{18}", 1530, 470, 110, CERTO)
        E.frase(c, t, c4 - 0.3, ps("pela equação:", "i", 56, TINTA2), XE, 720, "left", 0.06)
        fm(c, t, c4, "100x − 10x = 90x", XE, 830, 76)
        fm(c, t, entre(C, "s14.c", "s14.d", 0.4), "27,777… − 2,777…", XE + 700, 830, 64, TINTA2)
        fm(c, t, d4, "90x = 25", XE, 960, 90, COR)
    E.saida(c, t, C["s15"] - 0.1, macete)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"] + 0.2, ps("o macete simples daria", "i", 66), XE, 440, "left", 0.08)
    fm(c, t, a5, "f{27}{99}", 520, 640, 140, ERRADO, "center")
    fm(c, t, b5, "= 0,2727…", 940, 640, 120, ERRADO, "center")
    E.frase(c, t, b5 + 0.6, [("outro número", "g", 66, ERRADO)], 1400, 620)
    E.frase(c, t, c5, ps("na dízima, olhe primeiro", "i", 70) + [("o que fica fora do período", "g", 74, COR)], W / 2, 900, "center", 0.08)


# ---------------- situação 4: inequação ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C, 4, "s16", "inequação")
    fm(c, t, C["s16.b"], "5 − 2x ≥ −3", XE, 540, 160, COR)
    E.frase(c, t, C["s16.c"], ps("escreva como", "i", 76) + [("intervalo", "g", 80, COR)], XE, 760, "left", 0.1)
    E.relogio(c, t, C["s17.a"], 1520, 480, 170)


def b_resposta4(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    linhas = ((C["s18"] + 0.2, "5 − 2x", "≥", "−3"), (a8, "−2x", "≥", "−8"), (d8, "x", "≤", "4"))
    pilha(c, t, linhas, ((a8, "− 5"), (b8, "÷ (−2)")), 520, 220, 190, 100)
    if C["s18"] <= t < C["s19"] + 0.4:
        E.saida(c, t, C["s19"], lambda: E.foco(c, t, c8, 0.5, lambda a: E.pilula(c, "negativo: vira o sinal", 1260, 420, 52, "g", fundo=ERRADO, a=a)))
    if t >= d8:
        E.foco(c, t, d8, 0.4, lambda a: centro(c, "≤", 520, 600, 100, "g", ERRADO, a))
    y = 880
    vx = E.reta(c, t, a9 - 0.3, 260, 1660, y, -2, 6, range(-2, 7), MENOS, size=50)
    bolinha(c, t, a9, vx(4), y, True)
    pinta(c, t, b9, vx(4), 90, y, seta=True)
    colchetes(c, t, b9 + 0.3, "]−∞, 4]", 1420, 330, 120, {0: ERRADO, 6: CERTO})
    E.frase(c, t, b9 + 0.6, ps("tem tracinho: fechado no 4", "i", 48, TINTA2), 1420, 410, "center", 0.05)
    fm(c, t, c9, "5 − 2 · 0 = 5 ≥ −3", 1160, 620, 64)
    E.foco(c, t, c9 + 0.6, 0.4, lambda a: E.selo(c, 1790, 600, 36, True, a))
    ponto(c, t, d9, vx(0), y, CERTO, 16)
    E.foco(c, t, d9, 0.4, lambda a: c.drawCircle(vx(0), y, 40, M.paint(CERTO, a, stroke=6)), blur=4)
    E.frase(c, t, d9 + 0.3, [("bateu", "g", 64, CERTO)], vx(0), y - 70, "center")


# ---------------- situação 5: ∩ e ∪ ----------------
def b_questao5(c, t, C, b):
    situacao(c, t, C, 5, "s20", "junta tudo")
    colchetes(c, t, C["s20.b"], "]−∞, 4]", XE, 470, 130, align="left")
    E.frase(c, t, C["s20.b"] + 0.4, ps("a resposta da situação 4", "i", 50, TINTA2), XE, 540, "left", 0.06)
    colchetes(c, t, C["s20.c"], "]1, 6[", XE + 640, 470, 130, align="left")
    fz(c, t, C["s20.d"], [("ache", "i", 76), ("∩", "g", 96, COR), ("e", "i", 76), ("∪", "g", 96, COR)], XE, 760, "left", 0.15)
    E.relogio(c, t, C["s21.a"], 1560, 600, 150)


V5 = vx_de(-2, 8)


def b_resposta5(c, t, C, b):
    t0 = C["s22"] + 0.2
    ya, yb, yr = 240, 440, 730
    for y in (ya, yb):
        E.reta(c, t, t0 - 0.2, X0, X1, y, -2, 8, range(-2, 9), MENOS, size=42)
    colchetes(c, t, t0, "]−∞, 4]", 260, ya + 24, 66)
    pinta(c, t, t0 + 0.2, V5(4), X0 - 30, ya, TINTA, seta=True)
    bolinha(c, t, t0 + 0.2, V5(4), ya, True, TINTA)
    colchetes(c, t, t0 + 0.3, "]1, 6[", 260, yb + 24, 66)
    trecho(c, t, t0 + 0.5, V5, yb, 1, 6, False, False, TINTA)
    a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
    a3, b3, c3, d3 = (C[f"s23.{k}"] for k in "abcd")

    def inter():
        E.frase(c, t, a2, ps("maior começo:", "i", 48, TINTA2) + [("1", "g", 54)], 260, yr + 170, "center", 0.06)
        E.frase(c, t, b2, ps("menor fim:", "i", 48, TINTA2) + [("4", "g", 54)], 260, yr + 240, "center", 0.06)
        faixa(c, t, a2, V5(1), V5(4), ya - 60, yb + 60)
        if t >= c2:
            c.drawCircle(V5(1), yb, 38, M.paint(ERRADO, ep(t, c2, 0.4), stroke=6))
        if t >= d2:
            for y in (ya, yb):
                c.drawCircle(V5(4), y, 38, M.paint(CERTO, ep(t, d2, 0.4), stroke=6))
        E.foco(c, t, a3 - 0.3, 0.4, lambda a: M.line(c, X0 - 40, yr, X1 + 60, yr, TINTA, a, 5))
        trecho(c, t, a3, V5, yr, 1, 4, False, True)
        fz(c, t, a3 + 0.3, [("∩ = ]1, 4]", "g", 80, COR)], W / 2 + 200, yr + 200, "center")
    E.saida(c, t, b3 - 0.1, inter)
    if t < b3:
        return
    faixa(c, t, b3, X0 - 30, V5(6), ya - 60, yb + 60)
    if t >= c3:
        c.drawCircle(V5(6), yb, 38, M.paint(ERRADO, ep(t, c3, 0.4), stroke=6))
    E.foco(c, t, b3, 0.4, lambda a: M.line(c, X0 - 40, yr, X1 + 60, yr, TINTA, a, 5))
    pinta(c, t, d3, V5(6), X0 - 30, yr, seta=True)
    bolinha(c, t, d3, V5(6), yr, False)
    fz(c, t, d3 + 0.3, [("∪ = ]−∞, 6[", "g", 80, COR)], W / 2, yr + 200, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    ka, kb, kc, kd = (C[f"s24.{k}"] for k in "abcd")
    E.frase(c, t, C["s24"] + 0.3, ps("daqui sai um atalho de prova", "i", 66, CLARO), W / 2, 150, "center", 0.08)
    E.frase(c, t, ka, ps("teste", "i", 84, CLARO) + [("um número", "g", 90, BR)] + ps("em cada resposta", "i", 84, CLARO), W / 2, 290, "center", 0.12)
    vb = lambda v: 520 + (v + 2) / 10 * 1200
    for i, (y, s) in enumerate(((450, "]−∞, 4]"), (560, "]1, 6["), (700, "]1, 4]"))):
        t1 = entre(C, "s24.a", "s24.b", 0.3) + 0.3 * i
        E.foco(c, t, t1, 0.4, lambda a, y=y, s=s, i=i: (M.line(c, 480, y, 1760, y, CLARO, a, 4),
                                                        E.escreve(c, s, 160, y + 22, 64, "g", BR if i == 2 else CLARO, a)))
        a_, b_ = ((-2.6, 4), (1, 6), (1, 4))[i]
        pinta(c, t, t1 + 0.2, vb(max(a_, -2)) if a_ > -2 else 480, vb(b_), y, CLARO if i < 2 else BR)
    q = ep(t, entre(C, "s24.a", "s24.b", 0.6), 0.4)
    if q > 0:
        M.line(c, vb(2), 410, vb(2), 740, "#FFD500", q, 5)
        E.foco(c, t, entre(C, "s24.a", "s24.b", 0.6), 0.4, lambda a: centro(c, "2", vb(2), 400, 70, "g", "#FFD500", a))
    E.foco(c, t, kb, 0.5, lambda a: E.selo(c, vb(2) + 70, 690, 34, True, a))
    E.frase(c, t, kc, ps("a resposta é", "i", 66, CLARO) + [("o grupo de números que servem", "g", 70, BR)], W / 2, 870, "center", 0.08)
    E.frase(c, t, kd, [("pontas:", "g", 70, BR)] + ps("confira na pilha, uma por uma", "i", 66, CLARO), W / 2, 990, "center", 0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s25"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s25.a", [("Venn:", "g", 76, COR), ("de dentro para fora", "i", 74)]),
                 ("s25.b", [("classificar:", "g", 76, COR), ("suba a escada", "i", 74)]),
                 ("s25.c", [("dízima:", "g", 76, COR), ("olhe o que fica fora do período", "i", 74)]),
                 ("s25.d", [("intervalos:", "g", 76, COR), ("confira as pontas, uma por uma", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 28, 52, a=a), centro(c, str(i + 1), 260, y - 6, 60, "g", E.SOBRE, a)))
            fz(c, t, C[k] + 0.1, partes, 350, y)
    E.saida(c, t, C["s26"] - 0.1, resumo)
    if t < C["s26"]:
        return
    ka, kb, kc, kd = (C[f"s26.{k}"] for k in "abcd")
    E.frase(c, t, C["s26"] + 0.3, ps("trilha de conjuntos e reais", "i", 66, TINTA2) + [("fechada", "g", 70, CERTO)], XE, 210, "left", 0.08)
    E.frase(c, t, ka - 0.8, ps("a próxima trilha:", "i", 76), XE, 340, "left", 0.1)
    E.frase(c, t, ka, [("produtos notáveis", "g", 110, COR)], XE, 480)
    fm(c, t, kb, "(x + 3)^2", XE, 660, 120, COR)
    E.frase(c, t, kb + 0.4, ps("sem multiplicar tudo", "i", 62), XE + 470, 650, "left", 0.08)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 780, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(990, 805, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 970, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, atalho=b_atalho, fim=b_fim)
