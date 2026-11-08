"""Visual — Estudativo · MAT-CON-003: problemas com diagrama de Venn.
Turma de 40 (futebol 22, vôlei 17, ambos 7 → 15, 7, 10 e 8 fora); turma de 50 com três esportes (2 no centro; 4, 3, 5; 10, 9, 6; 11 fora);
questão 35 + 30 − x = 50 → x = 15. O Venn se preenche de dentro para fora. A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-003_problemas_diagrama_de_venn.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("dois", "formula", "tres", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
assert 22 - 7 == 15 and 17 - 7 == 10 and 15 + 7 + 10 == 32 and 40 - 32 == 8 and 22 + 17 - 7 == 32 and 40 - 22 - 17 == 1 and 1 + 7 == 8
assert (6 - 2, 5 - 2, 7 - 2) == (4, 3, 5) and 19 - 4 - 3 - 2 == 10 and 20 - 4 - 5 - 2 == 9 and 16 - 3 - 5 - 2 == 6
assert 10 + 9 + 6 + 4 + 3 + 5 + 2 == 39 and 50 - 39 == 11 and 60 - 10 == 50 and 35 + 30 - 15 == 50 and 35 - 15 == 20


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


def vn(c, t, t0, cx, cy, r, nomes, numeros, tn, pinta=(), universo=None, cor=None, size=60):
    """Venn da aula; pinta = [(região, t_entra[, t_sai])]: a pintura some quando a conta passa para outra região"""
    p = [(it[0], it[1]) for it in pinta if len(it) < 3 or t < it[2]]
    return E.venn(c, t, t0, cx, cy, r, nomes, numeros=numeros, pinta=p, universo=universo, cor=cor, size=size, tn=tn)


def conta(c, t, t0, s, x, y, size=80, cor=None, est="g"):
    E.formula_em(c, t, t0, s, x, y, size, est, cor or TINTA)


XD = 1090  # coluna do texto, à direita do diagrama


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd, ke, kf = (C[f"s01.{k}"] for k in "abcdef")

    def problema():
        for i, (k, rot, n) in enumerate(((ka, "turma", "40"), (kb, "futebol", "22"), (kc, "vôlei", "17"), (kd, "jogam ambos", "7"))):
            y = 230 + i * 120
            E.frase(c, t, k, [(rot, "i", 70)], 560, y, "right")
            E.foco(c, t, k + 0.1, 0.45, lambda a, n=n, y=y: E.escreve(c, n, 600, y, 96, "g", COR, a))
        E.frase(c, t, entre(C, "s01.d", "s01.e", 0.25), ps("quantos não jogam", "i", 76) + [("nenhum?", "g", 84, COR)], 170, 800, "left", 0.12)
        vn(c, t, ka + 0.3, 1400, 420, 190, ("futebol", "vôlei"), {"": "?"}, {"": entre(C, "s01.d", "s01.e", 0.3)}, size=52, universo="")
        conta(c, t, ke, "40 − 22 − 17 = 1", 170, 960, 84, ERRADO)
        if t >= kf - 0.3:
            E.risco(c, 160, 980, 860, 890, t, kf - 0.3, ERRADO, 12)
        esfera(c, t, kf, 1400, 900, 110, "8", 140, CERTO)
    E.saida(c, t, C["s02"] - 0.1, problema)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.25), ps("resolver problemas com", "i", 84), XE, 440, passo=0.12)
    E.frase(c, t, entre(C, "s02.a", "s02.b", 0.55), [("2 e com 3", "g", 100, COR)] + ps("esportes", "i", 90), XE, 580, passo=0.12)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    E.caixa_pontilhada(c, x, 240, w, 196, ep(t, C["s03.b"], 0.5), prog_=ep(t, C["s03.b"], 0.5))
    fz(c, t, C["s03.b"] + 0.1, [("interseção", "i", 62), ("∩", "g", 70, COR), ("e união", "i", 62), ("∪", "g", 70, COR)], x + 44, 324)
    E.frase(c, t, C["s03.b"] + 0.3, [("no diagrama de Venn", "g", 60, COR)], x + 44, 404)
    E.caixa_pontilhada(c, x, 500, w, 196, ep(t, C["s03.c"], 0.5), prog_=ep(t, C["s03.c"], 0.5))
    E.frase(c, t, C["s03.c"] + 0.1, [("equação:", "i", 62)], x + 44, 584)
    E.frase(c, t, C["s03.c"] + 0.3, [("o mesmo nos dois lados", "g", 60, COR)], x + 44, 664)
    py = lerp(410, 670, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.c", "s03.end", 0.72), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), x, 820, "left", 0.12)


# ---------------- dois conjuntos ----------------
def b_dois(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5 = C["s05.a"], C["s05.b"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    pin = [("AB", b4, a5), ("A", a5, b5), ("B", b5, a6), ("A", a6, b6), ("AB", a6, b6), ("B", a6, b6), ("", b6)]
    vn(c, t, C["s04"] + 0.2, 540, 600, 230, ("futebol", "vôlei"), {"AB": "7", "A": "15", "B": "10", "": "8"},
       {"AB": d4, "A": a5 + 0.8, "B": b5 + 0.8, "": c6 + 0.6}, pin, universo="turma de 40", size=60)

    def s04():
        E.frase(c, t, a4, ps("de", "i", 80) + [("dentro", "g", 84, COR)] + ps("para", "i", 80) + [("fora", "g", 84, COR)], XD, 260, "left", 0.12)
        E.frase(c, t, b4, ps("comece pela", "i", 70) + [("interseção", "g", 74)], XD, 420, "left", 0.12)
        E.frase(c, t, c4, [("7", "g", 110, COR)] + ps("jogam ambos", "i", 70), XD, 580, "left", 0.12)
        E.frase(c, t, d4, ps("vai no", "i", 70) + [("meio", "g", 74, COR)], XD, 700, "left", 0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] - 0.1 <= t:
        def s05():
            E.frase(c, t, C["s05"] + 0.2, ps("o 7 já está no meio", "i", 66, TINTA2), XD, 260, "left", 0.1)
            E.frase(c, t, a5, [("só futebol", "g", 70, COR)], XD, 420)
            conta(c, t, a5 + 0.5, "22 − 7 = 15", XD, 530, 96)
            E.frase(c, t, b5, [("só vôlei", "g", 70, COR)], XD, 700)
            conta(c, t, b5 + 0.5, "17 − 7 = 10", XD, 810, 96)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("some os pedaços", "i", 70, TINTA2), XD, 260)
    conta(c, t, a6, "15 + 7 + 10 = 32", XD, 380, 90)
    E.frase(c, t, a6 + 0.8, ps("jogam pelo menos um", "i", 58), XD, 460, "left", 0.08)
    E.frase(c, t, b6, [("fora", "g", 70, COR)] + ps("dos círculos", "i", 66), XD, 640, "left", 0.12)
    conta(c, t, c6, "40 − 32 = 8", XD, 760, 96, CERTO)
    E.frase(c, t, c6 + 0.6, ps("não jogam nenhum", "i", 60, CERTO), XD, 840, "left", 0.1)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    y_f = lerp(560, 200, ease_io(prog(t, C["s08"] - 0.2, 0.7)))
    k_f = lerp(1.0, 0.8, ease_io(prog(t, C["s08"] - 0.2, 0.7)))

    def nota():
        E.frase(c, t, C["s07"] + 0.2, ps("na prova:", "i", 76, TINTA2), W / 2, 200, "center")
        txe(c, t, a7, "n(A)", 700, 370, 120, "g", COR, "center")
        E.frase(c, t, a7 + 0.4, ps("= número de elementos de A", "i", 70), 800, 360, "left", 0.08)
    E.saida(c, t, b7, nota)
    if t < C["s08"] - 0.2:
        E.frase(c, t, entre(C, "s07.a", "s07.b", 0.55), ps("e a fórmula da união:", "i", 70, COR), W / 2, 450, "center", 0.1)
    c.save(); c.translate(W / 2, y_f); c.scale(k_f, k_f); c.translate(-W / 2, -y_f)
    ln(c, t, [("n(A ∪ B)", b7, COR), (" = n(A) + n(B) ", b7 + 1.0), ("− n(A ∩ B)", b7 + 2.0, ERRADO if t >= a8 else TINTA)], W / 2, y_f, 92, "g", "center")
    c.restore()
    if t < C["s08"]:
        return
    E.frase(c, t, a8, ps("quem joga ambos foi contado", "i", 70) + [("2 vezes", "g", 76, ERRADO)], W / 2, 360, "center", 0.1)
    conta(c, t, b8, "22 = 15 + 7", 380, 520, 90)
    conta(c, t, b8 + 0.6, "17 = 10 + 7", 1140, 520, 90)
    for x in (380 + E.formula(c, "22 = 15 + ", 0, 0, 90, a=0), 1140 + E.formula(c, "17 = 10 + ", 0, 0, 90, a=0)):
        E.foco(c, t, b8 + 1.0, 0.4, lambda a, x=x: c.drawCircle(x + 26, 488, 58, M.paint(ERRADO, a, stroke=6)), blur=4)
    E.frase(c, t, entre(C, "s08.b", "s08.c", 0.6), ps("então tira", "i", 66) + [("uma vez", "g", 70, COR)], W / 2, 660, "center", 0.1)
    conta(c, t, c8, "22 + 17 = 39", 380, 820, 96)
    conta(c, t, d8, "39 − 7 = 32", 1140, 820, 96, COR)
    E.foco(c, t, entre(C, "s08.d", "s08.end", 0.6), 0.5, lambda a: E.selo(c, 1700, 785, 50, True, a))
    E.frase(c, t, entre(C, "s08.d", "s08.end", 0.6), ps("igual ao diagrama", "i", 60, CERTO), W / 2, 960, "center", 0.1)


# ---------------- três conjuntos ----------------
TC = dict(cx=520, cy=620, r=205)
NUM3 = {"ABC": "2", "AB": "4", "AC": "3", "BC": "5", "A": "10", "B": "9", "C": "6", "": "11"}


def b_tres(c, t, C, b):
    k = lambda s: C[s]
    tn = {"ABC": k("s11.a"), "AB": k("s11.b") + 0.9, "AC": k("s11.c") + 0.9, "BC": k("s11.d") + 0.9,
          "A": k("s12.b"), "B": k("s12.d"), "C": k("s12.f"), "": k("s13.c")}
    pin = [("ABC", k("s11.a"), k("s11.b")), ("AB", k("s11.b"), k("s11.c")), ("AC", k("s11.c"), k("s11.d")), ("BC", k("s11.d"), k("s12")),
           ("A", k("s12.a"), k("s12.c")), ("B", k("s12.c"), k("s12.e")), ("C", k("s12.e"), k("s13")), ("", k("s13.b"))]
    vn(c, t, k("s09.a"), TC["cx"], TC["cy"], TC["r"], ("F", "V", "B"), NUM3, tn, pin, universo="turma de 50", size=58)

    def dados():
        E.frase(c, t, C["s09"] + 0.2, ps("três esportes,", "i", 62) + [("mesmo método", "g", 64, COR)], XD, 220, "left", 0.1)
        for i, (kk, l, nome, n) in enumerate((("s09.b", "F", "futebol", "19"), ("s09.c", "V", "vôlei", "20"), ("s09.d", "B", "basquete", "16"))):
            y = 420 + i * 150
            E.foco(c, t, C[kk], 0.45, lambda a, l=l, y=y: E.escreve(c, l, XD, y, 96, "g", COR, a))
            E.frase(c, t, C[kk] + 0.1, ps(nome, "i", 70), XD + 100, y, "left")
            E.foco(c, t, C[kk] + 0.2, 0.45, lambda a, n=n, y=y: E.escreve(c, n, XD + 440, y, 96, "g", TINTA, a))
    E.saida(c, t, C["s10"] - 0.1, dados)
    if C["s10"] - 0.1 <= t:
        def pares():
            for i, (kk, s, n) in enumerate((("s10.a", "F e V", "6"), ("s10.b", "F e B", "5"), ("s10.c", "V e B", "7"), ("s10.d", "os três", "2"))):
                y = 240 + i * 130
                pp = [(s, "g", 76, TINTA)] if i == 3 else [(s[0], "g", 80, COR), ("e", "i", 76), (s[-1], "g", 80, COR)]
                E.frase(c, t, C[kk], pp, XD, y, "left", 0.1)
                E.foco(c, t, C[kk] + 0.2, 0.45, lambda a, n=n, y=y: E.escreve(c, n, XD + 400, y, 96, "g", TINTA, a))
            E.frase(c, t, C["s10.e"], ps("atenção: o", "i", 58) + [("6", "g", 62, ERRADO)] + ps("já inclui quem", "i", 58), XD, 820, "left", 0.08)
            E.frase(c, t, C["s10.e"] + 0.8, ps("joga os três", "i", 58), XD, 890, "left", 0.08)
        E.saida(c, t, C["s11"] - 0.1, pares)
    if C["s11"] - 0.1 <= t:
        def duplas():
            E.frase(c, t, C["s11"] + 0.2, ps("de dentro para fora", "i", 70, TINTA2), XD, 220, "left", 0.1)
            E.frase(c, t, k("s11.a"), ps("no centro, o", "i", 70) + [("2", "g", 90, COR)], XD, 350, "left", 0.1)
            for i, (kk, s, cc) in enumerate((("s11.b", "F e V", "6 − 2 = 4"), ("s11.c", "F e B", "5 − 2 = 3"), ("s11.d", "V e B", "7 − 2 = 5"))):
                y = 520 + i * 150
                E.frase(c, t, C[kk], [(s[0], "g", 70, COR), ("e", "i", 66), (s[-1], "g", 70, COR)], XD, y, "left", 0.1)
                conta(c, t, C[kk] + 0.4, cc, XD + 260, y, 84)
        E.saida(c, t, C["s12"] - 0.1, duplas)
    if C["s12"] - 0.1 <= t:
        def sozinhos():
            E.frase(c, t, C["s12"] + 0.2, ps("só um esporte", "i", 70, TINTA2), XD, 220, "left", 0.1)
            for i, (ka, kr, s, cc, r_) in enumerate((("s12.a", "s12.b", "F", "19 − 4 − 3 − 2", "10"), ("s12.c", "s12.d", "V", "20 − 4 − 5 − 2", "9"),
                                                    ("s12.e", "s12.f", "B", "16 − 3 − 5 − 2", "6"))):
                y = 400 + i * 170
                E.foco(c, t, C[ka], 0.45, lambda a, s=s, y=y: E.escreve(c, s, XD, y, 84, "g", COR, a))
                conta(c, t, C[ka] + 0.3, cc, XD + 90, y, 72)
                conta(c, t, C[kr], "= " + r_, XD + 90 + E.formula(c, cc + " ", 0, 0, 72, a=0), y, 72, COR)
        E.saida(c, t, C["s13"] - 0.1, sozinhos)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13"] + 0.2, ps("some as 7 partes", "i", 70, TINTA2), XD, 220, "left", 0.1)
    conta(c, t, k("s13.a"), "10 + 9 + 6 + 4 + 3 + 5 + 2", XD, 380, 62)
    conta(c, t, k("s13.a") + 0.6, "= 39", XD, 490, 96, COR)
    E.frase(c, t, k("s13.a") + 0.9, ps("jogam alguma coisa", "i", 58), XD + 260, 480, "left", 0.08)
    conta(c, t, k("s13.b"), "50 − 39 = 11", XD, 700, 100, CERTO)
    E.frase(c, t, k("s13.c"), ps("não jogam nenhum", "i", 64, CERTO), XD, 800, "left", 0.1)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd = (C[f"s14.{k}"] for k in "abcd")
    E.frase(c, t, C["s14"] + 0.2, ps("o erro do começo", "i", 80, ERRADO), W / 2, 190, "center")
    conta(c, t, ka, "40 − 22 − 17 = 1", 260, 400, 120, ERRADO)
    E.frase(c, t, kb, ps("os", "i", 70) + [("7", "g", 84, ERRADO)] + ps("de ambos", "i", 70) + [("saíram 2 vezes", "g", 74, ERRADO)], W / 2, 560, "center", 0.1)
    E.frase(c, t, entre(C, "s14.b", "s14.c", 0.5), ps("uma no 22, outra no 17", "i", 60, TINTA2), W / 2, 650, "center", 0.08)
    E.frase(c, t, kc, ps("devolva os 7:", "i", 76), 560, 830, "right", 0.1)
    conta(c, t, kc + 0.5, "1 + 7 = 8", 620, 840, 120, CERTO)
    E.foco(c, t, kd, 0.5, lambda a: E.selo(c, 1420, 800, 62, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def contrario():
        ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
        E.frase(c, t, C["s15"] + 0.2, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("a fórmula também roda", "i", 84, CLARO) + [("ao contrário", "g", 90, BR)], W / 2, 290, "center", 0.12)
        E.frase(c, t, kb, ps("a questão dá", "i", 70, CLARO) + [("quem não joga nenhum", "g", 72, BR)], W / 2, 450, "center", 0.1)
        E.frase(c, t, entre(C, "s15.b", "s15.c", 0.5), ps("e esconde", "i", 70, CLARO) + [("quem joga ambos", "g", 72, BR)], W / 2, 560, "center", 0.1)
        E.frase(c, t, kc, ps("chame a interseção de", "i", 76, CLARO) + [("x", "g", 100, BR)], W / 2, 720, "center", 0.1)
        E.foco(c, t, entre(C, "s15.c", "s15.end", 0.5), 0.5, lambda a: tx(c, "n(A ∪ B) = n(A) + n(B) − x", W / 2, 900, 84, "g", CLARO, a, "center"))
    E.saida(c, t, C["s16"] - 0.1, contrario)
    if t < C["s16"]:
        return
    ka, kb, kc = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, ka, ps("é", "i", 80, CLARO) + [("uma igualdade:", "g", 84, BR)], W / 2, 220, "center", 0.12)
    E.frase(c, t, entre(C, "s16.a", "s16.b", 0.4), ps("sabendo 3 números, a equação dá o", "i", 66, CLARO) + [("4º", "g", 74, BR)], W / 2, 330, "center", 0.08)
    E.frase(c, t, kb, [("não compensa", "g", 80, BR)] + ps("com 3 conjuntos:", "i", 76, CLARO), W / 2, 530, "center", 0.12)
    E.frase(c, t, entre(C, "s16.b", "s16.c", 0.5), ps("a fórmula fica comprida demais", "i", 64, CLARO), W / 2, 630, "center", 0.08)
    E.frase(c, t, kc, ps("preencha de", "i", 84, CLARO) + [("dentro para fora", "g", 92, BR)], W / 2, 840, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd, ke, kf = (C[f"s17.{k}"] for k in "abcdef")
    E.frase(c, t, C["s17"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 160, passo=0.12)
    for i, (k, n, s) in enumerate(((ka, "60", "pessoas"), (kb, "35", "usam mapas"), (kc, "30", "usam música"), (kd, "10", "não usam nenhum"))):
        y = 300 + i * 120
        E.foco(c, t, k, 0.45, lambda a, n=n, y=y: E.escreve(c, n, XE, y, 96, "g", COR, a))
        E.frase(c, t, k + 0.1, ps(s, "i", 70), XE + 170, y, "left", 0.08)
    E.frase(c, t, ke, ps("quantas usam", "i", 80) + [("ambos?", "g", 88, COR)], XE, 820, "left", 0.1)
    E.frase(c, t, kf, ps("e", "i", 80) + [("só mapas?", "g", 88, COR)], XE, 940, "left", 0.1)
    E.relogio(c, t, C["s18.a"], 1520, 420, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    vn(c, t, C["s19"] + 0.2, 1560, 600, 160, ("mapas", "música"), {"": "10", "AB": "15", "A": "20"}, {"": a9, "AB": c0, "A": d0},
       [("AB", c0, d0), ("A", d0)], universo="60", size=50)
    linhas = ((a9, "união = 60 − 10 = 50"), (b9, "35 + 30 − x = 50"), (c9, "65 − x = 50"), (a0, "65 = 50 + x"), (b0, "x = 15"))
    for i, (k, s) in enumerate(linhas):
        y = 200 + i * 125
        ult = i == len(linhas) - 1
        velha = not ult and t >= linhas[i + 1][0]
        conta(c, t, k, s, XE, y, 86, COR if ult else (CINZA if velha else TINTA))
    E.foco(c, t, a0 + 0.3, 0.4, lambda a: E.pilula(c, "+ x nos dois lados", 860, 555, 40, "b", fundo=TINTA, a=a))
    E.foco(c, t, b0 + 0.3, 0.4, lambda a: E.pilula(c, "− 50", 640, 680, 40, "b", fundo=TINTA, a=a))
    E.frase(c, t, c0, [("15", "g", 96, CERTO)] + ps("usam ambos", "i", 72), XE, 850, "left", 0.1)
    conta(c, t, d0, "só mapas: 35 − 15 = 20", XE, 980, 76, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 260, "center")
        for i, (k, l1, l2) in enumerate((("s21.a", "preencha de", "dentro para fora"), ("s21.b", "tire uma vez", "a interseção"))):
            y = 470 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(l1, "i", 84), (l2, "g", 84)], 400, y, "left", 0.15)
        E.frase(c, t, C["s21.b"] + 1.0, ps("ela foi contada duas vezes", "i", 56, TINTA2), 400, 760, "left", 0.08)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    ka, kb, kc, kd = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula, os conjuntos mais famosos", "i", 70), XE, 230, passo=0.1)
    fz(c, t, ka, [("ℕ", "g", 130, COR), ("ℤ", "g", 130, COR), ("ℚ", "g", 130, COR)], XE, 420, "left", 0.3)
    E.frase(c, t, ka + 0.3, ps("naturais, inteiros e racionais", "i", 66), XE + 560, 400, "left", 0.08)
    E.frase(c, t, kb, ps("uma dízima", "i", 72) + [("também é fração", "g", 76, COR)], XE, 570, "left", 0.1)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 740, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(960, 765, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 950, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, dois=b_dois, formula=b_formula, tres=b_tres, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
