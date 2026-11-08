"""Visual — Estudativo · MAT-CON-002: união, interseção, diferença e complementar.
A = {1, 2, 3, 4}, B = {3, 4, 5}, U = {1, ..., 6}: A ∩ B = {3, 4}, A ∪ B = {1, ..., 5}, A − B = {1, 2}, B − A = {5}, Ā = {5, 6}. Cada operação pinta
sua região no Venn (E.venn). A fonte da casa não tem ∈, ⊂, ∪, ∩ nem ℕ ℤ ℚ ℝ: tx() desenha esses símbolos no peso do texto. Sem voz gravada ainda: todo instante
vem de um marcador C[...] ou de entre(), que divide o trecho entre dois marcadores e por isso acompanha a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Conjuntos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CON-002_uniao_intersecao_diferenca_complementar.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("venn", "complementar", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
# as contas da aula
A, B, U = {1, 2, 3, 4}, {3, 4, 5}, set(range(1, 7))
assert A & B == {3, 4} and A | B == {1, 2, 3, 4, 5} and A - B == {1, 2} and B - A == {5} and U - A == {5, 6}
Uq, Aq, Bq = {2, 4, 6, 8, 10, 12}, {2, 4, 6, 8}, {4, 8, 12}
assert Aq & Bq == {4, 8} and Bq - Aq == {12} and Aq | Bq == {2, 4, 6, 8, 12} and Uq - Bq == {2, 6, 10}


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


def barra_em(c, s, x, y, size, est="g", cor=None, a=1.0, align="left"):
    """letra com traço em cima (complementar): Ā"""
    w = tw(s, est, size)
    x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
    tx(c, s, x0, y, size, est, cor, a)
    M.line(c, x0 + size * 0.04, y - size * 0.86, x0 + tw(s[0], est, size) - size * 0.04, y - size * 0.86, cor or TINTA, a, size * 0.08)


# o Venn da aula: sempre no mesmo lugar, à esquerda; o texto fica à direita
VX, VY, VR = 560, 620, 230
NUM = {"A": "1   2", "AB": "3   4", "B": "5"}
XD = 1075  # coluna do texto


def vn(c, t, t0, pinta=(), numeros=None, tn=None, universo=None, cor=None, nomes=("A", "B"), cx=VX, cy=VY, r=VR, size=64):
    """pinta = [(região, t_entra[, t_sai])]: a pintura some quando a fala passa para outra operação"""
    p = [(it[0], it[1]) for it in pinta if len(it) < 3 or t < it[2]]
    return E.venn(c, t, t0, cx, cy, r, nomes, numeros=NUM if numeros is None else numeros, pinta=p, universo=universo, cor=cor, size=size, tn=tn)


def lugar(reg, cx=VX, cy=VY, r=VR):
    return E._venn_lugar(2, float(cx), float(cy), float(r), reg)


def resp(c, t, t0, esq, conj, y, size=96, cor=None, x=XD):
    """A ∩ B = {3, 4}: a operação entra antes, a resposta na fala"""
    txe(c, t, t0, esq + " = " + conj, x, y, size, "g", cor or COR)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def cafe():
        E.frase(c, t, ka, ps("quem toma", "i", 84) + [("café", "g", 90)] + [("ou", "g", 100, COR)] + [("chá?", "g", 90)], W / 2, 170, "center", 0.12)
        pin = [("AB", kb, kc), ("A", kc), ("AB", kc), ("B", kc)]
        vn(c, t, ka + 0.3, pin, numeros={}, nomes=("café", "chá"), cx=W / 2, cy=570, r=220)
        E.foco(c, t, kb, 0.4, lambda a: E.pilula(c, "café e chá", W / 2, 870, 50, "g", a=a))
        E.frase(c, t, entre(C, "s01.b", "s01.c", 0.3), ps("entra na conta?", "i", 70), 1500, 620, "left")
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 1560, 760, 56, True, a))
        E.frase(c, t, kc + 0.1, [("entra", "g", 84, CERTO)], 1640, 790)
        E.frase(c, t, entre(C, "s01.c", "s02", 0.5), [("ou", "g", 100, ERRADO)] + ps("derruba muita gente na prova", "i", 70), W / 2, 1010, "center", 0.15)
    E.saida(c, t, C["s02"] - 0.1, cafe)
    if t < C["s02"]:
        return
    ta, tb = C["s02.a"], C["s02.b"]
    E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 560, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
    E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
    fz(c, t, entre(C, "s02.a", "s02.b", 0.2), [("as", "i", 90), ("4 operações", "g", 90, COR)], XE, 440)
    fz(c, t, entre(C, "s02.a", "s02.b", 0.35), [("∪", "g", 110, COR), ("∩", "g", 110, COR), ("−", "g", 110, COR), ("complementar", "g", 80, COR)], XE, 580)
    fz(c, t, entre(C, "s02.a", "s02.b", 0.6), [("sem trocar", "i", 84), ("e", "g", 96), ("por", "i", 84), ("ou", "g", 96)], XE, 730)
    E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 545, 84, "g", E.SOBRE, a),
                                           centro(c, "de prova", 1560, 640, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    itens = (("s03.b", "{1, 2, 3}", "entre chaves"), ("s03.c", "∈", "pertence"), ("s03.d", "∅", "o conjunto vazio"))
    for i, (k, s, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        txe(c, t, C[k] + 0.1, s, x + 44, y + 128, 84, "g", COR)
        E.frase(c, t, C[k] + 0.3, [(l2, "i", 62)], x + 420, y + 120)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, entre(C, "s03.d", "s03.end", 0.4), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), x, 960, "left", 0.12)


# ---------------- o diagrama ----------------
def b_venn(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s04.{k}"] for k in "abcde")
    E.frase(c, t, C["s04"] + 0.2, ps("dois conjuntos", "i", 80, COR), XD, 200)
    txe(c, t, ka, "A = {1, 2, 3, 4}", XD, 340, 84)
    txe(c, t, kb, "B = {3, 4, 5}", XD, 470, 84)
    vn(c, t, kc, [("AB", kd)], tn={"A": kc + 0.8, "B": kc + 1.0, "AB": kd})
    E.frase(c, t, kd + 0.3, ps("3 e 4:", "g", 60, COR) + ps("a parte em comum", "i", 60), XD, 640, "left", 0.1)
    E.frase(c, t, ke, ps("diagrama de", "i", 84) + [("Venn", "g", 96, COR)], XD, 860, "left", 0.12)


# ---------------- interseção ----------------
def b_intersecao(c, t, C, b):
    ka, kb, kc, kd = (C[f"s05.{k}"] for k in "abcd")
    vn(c, t, C["s05"] - 9, [("AB", kc)])
    E.frase(c, t, ka, [("interseção", "g", 110, COR)], XD, 230)
    E.frase(c, t, kb, ps("em A", "g", 72) + [("e", "g", 90, COR)] + ps("em B", "g", 72), XD, 380, "left", 0.12)
    E.frase(c, t, kb + 0.6, ps("ao mesmo tempo", "i", 64), XD, 460, "left", 0.1)
    resp(c, t, kc, "A ∩ B", "{3, 4}", 640, 96)
    esfera(c, t, kd, XD + 110, 860, 100, "∩", 130)
    E.frase(c, t, kd + 0.3, ps("U de cabeça", "i", 60) + ps("para baixo", "i", 60), XD + 240, 880, "left", 0.1)


# ---------------- união ----------------
def b_uniao(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s06.{k}"] for k in "abcde")
    vn(c, t, C["s06"] - 9, [("AB", kc), ("A", kd), ("B", kd)])
    E.frase(c, t, ka, [("união", "g", 110, COR)], XD, 230)
    E.frase(c, t, kb, ps("em A", "g", 72) + [("ou", "g", 90, COR)] + ps("em B", "g", 72), XD, 380, "left", 0.12)
    E.frase(c, t, kc, [("ou", "g", 64, COR)] + ps("inclui quem está em", "i", 60) + [("ambos", "g", 64)], XD, 470, "left", 0.1)
    resp(c, t, kd, "A ∪ B", "{1, 2, 3, 4, 5}", 640, 72)
    E.frase(c, t, kd + 0.6, ps("sem repetir", "i", 56, TINTA2), XD, 715)
    esfera(c, t, ke, XD + 110, 880, 100, "∪", 130)
    E.frase(c, t, ke + 0.3, ps("um copo", "i", 60) + ps("que junta tudo", "i", 60), XD + 240, 900, "left", 0.1)


# ---------------- diferença ----------------
def b_diferenca(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s07.{k}"] for k in "abcde")
    vn(c, t, C["s07"] - 9, [("A", kd, ke), ("B", ke)])
    x, y = lugar("AB")
    for dx in (-48, 48):
        E.risco(c, x + dx - 30, y + 40, x + dx + 30, y - 40, t, kc + (0.3 if dx > 0 else 0), ERRADO, 10)
    E.frase(c, t, ka, [("diferença", "g", 110, COR)], XD, 230)
    E.frase(c, t, kb, ps("em A", "g", 72) + [("e não", "g", 80, COR)] + ps("em B", "g", 72), XD, 380, "left", 0.12)
    E.frase(c, t, kc, ps("risque o que", "i", 56) + [("também está em B", "g", 56, ERRADO)], XD, 480, "left", 0.1)
    resp(c, t, kd, "A − B", "{1, 2}", 650, 100)
    E.frase(c, t, ke, ps("a ordem", "i", 60) + [("importa:", "g", 64, COR)], XD, 790, "left", 0.1)
    resp(c, t, ke + 0.5, "B − A", "{5}", 910, 100, TINTA)


# ---------------- complementar ----------------
def b_complementar(c, t, C, b):
    t0 = C["s08.a"]
    pin = [("B", C["s09.b"] + 0.3), ("", C["s09.b"] + 0.3)]
    vn(c, t, t0, pin, numeros=dict(NUM, **{"": "6"}), tn={"": C["s08.b"] + 0.6, "A": t0 + 0.4, "B": t0 + 0.4, "AB": t0 + 0.4}, universo="U")
    if t < C["s09"]:
        E.frase(c, t, C["s08"] + 0.2, ps("falta o", "i", 76) + [("complementar", "g", 78, COR)], XD, 200, "left", 0.12)
        E.frase(c, t, t0, [("universo:", "g", 72, COR)], XD, 360)
        E.frase(c, t, t0 + 0.6, ps("tudo que está em jogo", "i", 64), XD, 440, "left", 0.1)
        E.frase(c, t, t0 + 1.2, ps("na questão", "i", 64), XD, 510, "left", 0.1)
        txe(c, t, C["s08.b"], "U = {1, 2, 3, 4, 5, 6}", XD, 680, 76)
        return
    ka, kb, kc, kd, ke = (C[f"s09.{k}"] for k in "abcde")
    E.frase(c, t, ka, ps("complementar de", "i", 80) + [("A", "g", 90, COR)], XD, 200, "left", 0.12)
    E.frase(c, t, kb, ps("no universo e", "i", 64) + [("fora de A", "g", 70, COR)], XD, 320, "left", 0.1)
    txe(c, t, entre(C, "s09.b", "s09.c", 0.3), "{1, 2, 3, 4, 5, 6} − {1, 2, 3, 4}", XD, 430, 50, "b", TINTA2)
    txe(c, t, kc, "= {5, 6}", XD, 560, 100, "g", COR)
    E.frase(c, t, kd, ps("na prova:", "i", 60, TINTA2), XD, 730)
    E.foco(c, t, kd + 0.2, 0.5, lambda a: barra_em(c, "A", XD + 60, 880, 140, "g", COR, a, "center"))
    E.frase(c, t, ke - 0.1, ps("ou", "i", 70, TINTA2), XD + 210, 870)
    E.formula_em(c, t, ke, "A^c", XD + 340, 880, 140, "g", COR)


# ---------------- o erro ----------------
def b_erro(c, t, C, b):
    def errado():
        ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
        E.frase(c, t, ka - 0.3, [("cuidado:", "g", 80, ERRADO)] + ps("tirar da união quem está em ambos", "i", 72), W / 2, 150, "center", 0.1)
        ok = t >= kc
        vn(c, t, ka + 0.2, [("A", ka + 0.6), ("B", ka + 0.6), ("AB", kc + 0.8)], cor=CERTO if ok else ERRADO)
        E.frase(c, t, entre(C, "s10.a", "s10.b", 0.4), ps("ou =", "i", 64) + [("um ou outro, só um", "g", 60, ERRADO)], XD, 330, "left", 0.1)
        txe(c, t, kb, "A ∪ B = {1, 2, 5}", XD, 470, 80, "g", ERRADO)
        E.risco(c, XD - 10, 490, XD + 680, 400, t, kc - 0.2, ERRADO, 12)
        txe(c, t, kc, "3 ∈ A", XD, 650, 76, "g", TINTA)
        txe(c, t, kc + 0.5, "→ 3 ∈ A ∪ B", XD + 235, 650, 76, "g", CERTO)
        E.frase(c, t, entre(C, "s10.c", "s11", 0.45), ps("o 4 também.", "i", 64), XD, 780, "left")
        E.frase(c, t, entre(C, "s10.c", "s11", 0.75), [("ambos entram", "g", 84, CERTO)], XD, 900)
    E.saida(c, t, C["s11"] - 0.1, errado)
    if t < C["s11"]:
        return
    ka, kb = C["s11.a"], C["s11.b"]
    E.frase(c, t, C["s11"] + 0.2, ps("guarde assim", "i", 80, COR), W / 2, 200, "center")
    for y, k, pal, s, txt, pin in ((470, ka, "e", "∩", "exige os dois ao mesmo tempo", ("AB",)), (800, kb, "ou", "∪", "aceita pelo menos um", ("A", "B", "AB"))):
        E.frase(c, t, k, [(pal, "g", 150, COR)], 260, y + 30, "center")
        esfera(c, t, k + 0.2, 500, y - 20, 80, s, 100)
        E.frase(c, t, k + 0.4, ps(txt, "i", 70), 640, y, "left", 0.08)
        vn(c, t, k + 0.4, [(p, k + 0.8) for p in pin], numeros={}, nomes=("", ""), cx=1600, cy=y - 10, r=80, size=30)


# ---------------- atalho (palco escuro) ----------------
def painel(c, a, x, y, w, h):
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint(E.PAPEL, a))


def b_atalho(c, t, C, b):
    palco(c, t)

    def caminho():
        ka, kb, kc, kd, ke = (C[f"s12.{k}"] for k in "abcde")
        painel(c, ep(t, C["s12"], 0.4), 120, 240, 920, 760)
        vn(c, t, C["s12"] + 0.1, [("AB", kb), ("A", kc), ("B", kd)], numeros={"AB": "3   4", "A": "1   2", "B": "5"},
           tn={"AB": kb, "A": kc + 0.3, "B": kd + 0.3}, cx=580, cy=640, r=210)
        E.frase(c, t, C["s12"] + 0.2, ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("comece pela", "i", 72, CLARO) + [("interseção", "g", 76, BR)], 1110, 330, "left", 0.11)
        txe(c, t, kb, "A ∩ B = {3, 4}", 1110, 460, 76, "g", BR)
        txe(c, t, kc, "A − B = {1, 2}", 1110, 610, 76, "g", CLARO)
        E.frase(c, t, kc + 0.4, ps("A sem a interseção", "i", 48, CLARO), 1110, 670, "left", 0.06)
        txe(c, t, kd, "B − A = {5}", 1110, 790, 76, "g", CLARO)
        txe(c, t, ke, "A ∪ B = {1, 2, 3, 4, 5}", 1110, 940, 66, "g", BR)
    E.saida(c, t, C["s13"] - 0.1, caminho)
    if t < C["s13"]:
        return
    ka, kb, kc, kd = (C[f"s13.{k}"] for k in "abcd")

    def pedacos():
        E.frase(c, t, ka - 0.3, ps("funciona porque são", "i", 72, CLARO) + [("pedaços que não se misturam", "g", 72, BR)], W / 2, 170, "center", 0.1)
        for i, s in enumerate(("só A", "em comum", "só B")):
            E.foco(c, t, ka + 0.6 + 0.4 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, 520 + i * 440, 330, 52, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, kb - 0.1, pedacos)
    if t < kb:
        return
    E.frase(c, t, kb, [("não compensa:", "g", 76, BR)] + ps("um conjunto inteiro dentro do outro", "i", 70, CLARO), W / 2, 170, "center", 0.1)
    painel(c, ep(t, kb + 0.2, 0.4), 160, 260, 760, 700)
    q = ease_io(prog(t, kb + 0.4, 0.8))
    if q > 0:
        c.drawArc(skia.Rect.MakeXYWH(240, 330, 560, 560), -90, 360 * q, False, M.paint(TINTA, 1.0, stroke=6, cap_round=True))
        c.drawArc(skia.Rect.MakeXYWH(420, 540, 220, 220), -90, 360 * q, False, M.paint(TINTA, 1.0, stroke=6, cap_round=True))
    if t >= kd:
        c.drawCircle(520, 610, 280, M.paint(COR, 0.3 * ep(t, kd, 0.5)))
    elif t >= kc:
        c.drawCircle(530, 650, 110, M.paint(COR, 0.32 * ep(t, kc, 0.5)))
    E.foco(c, t, kb + 0.8, 0.4, lambda a: (centro(c, "A", 530, 675, 70, "g", COR, a), centro(c, "B", 520, 440, 70, "g", COR, a)))
    txe(c, t, kc, "A ∩ B = A", 1060, 520, 100, "g", BR)
    E.frase(c, t, kc + 0.4, ps("o de dentro", "i", 60, CLARO), 1060, 600, "left", 0.1)
    txe(c, t, kd, "A ∪ B = B", 1060, 800, 100, "g", BR)
    E.frase(c, t, kd + 0.4, ps("o de fora", "i", 60, CLARO), 1060, 880, "left", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd, ke = (C[f"s14.{k}"] for k in "abcde")
    E.frase(c, t, C["s14"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    txe(c, t, ka, "U = {2, 4, 6, 8, 10, 12}", XE, 310, 80, "g", TINTA2)
    txe(c, t, kb, "A = {2, 4, 6, 8}", XE, 440, 96)
    txe(c, t, kc, "B = {4, 8, 12}", XE, 570, 96)
    fz(c, t, kd, [("A ∪ B", "g", 90, COR), ("·", "g", 90, CINZA), ("A ∩ B", "g", 90, COR), ("·", "g", 90, CINZA), ("B − A", "g", 90, COR)], XE, 760, "left", 0.3)
    E.frase(c, t, ke, ps("e o", "i", 76) + ps("complementar de B", "g", 76, COR), XE, 900, "left", 0.1)
    E.relogio(c, t, C["s15.a"], 1560, 420, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    num = {"A": "2   6", "AB": "4   8", "B": "12", "": "10"}
    a1, b1, c1 = C["s16.a"], C["s16.b"], C["s16.c"]
    a2, b2 = C["s17.a"], C["s17.b"]
    pin = [("AB", a1, b1), ("B", b1, c1), ("A", c1, C["s17"]), ("AB", c1, C["s17"]), ("B", c1, C["s17"]), ("A", a2), ("", a2)]
    vn(c, t, C["s16"] + 0.2, pin, numeros=num, universo="U", tn={k: C["s16"] + 0.6 for k in num})
    E.frase(c, t, C["s16"] + 0.3, ps("começando pela", "i", 70) + [("interseção", "g", 72, COR)], XD, 170, "left", 0.1)
    resp(c, t, a1, "A ∩ B", "{4, 8}", 320, 84)
    resp(c, t, b1, "B − A", "{12}", 470, 84)
    resp(c, t, c1, "A ∪ B", "{2, 4, 6, 8, 12}", 620, 76)
    E.foco(c, t, C["s17"] + 0.2, 0.5, lambda a: barra_em(c, "B", XD, 820, 100, "g", COR, a))
    txe(c, t, a2, "= {2, 6, 10}", XD + 90, 820, 100, "g", CERTO)
    if t >= b2:
        _, _, x1, y1 = E._venn_caixa(2, VX, VY, VR, 64)
        c.drawCircle(x1 - 64, y1 - 64 * 0.8, 64, M.paint(COR, ep(t, b2, 0.4), stroke=7))
    E.frase(c, t, b2, ps("o 10 não está em A nem em B,", "i", 56), XD, 940, "left", 0.07)
    E.frase(c, t, entre(C, "s17.b", "s17.end", 0.5), ps("mas está no universo:", "i", 56) + [("entra", "g", 60, CERTO)], XD, 1010, "left", 0.07)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.1, [("resumindo", "i", 88, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("e", "g", 80, COR), ("→", "g", 70), ("∩", "g", 90, COR), ("interseção: a parte em comum", "i", 70)]),
                 ("s18.b", [("ou", "g", 80, COR), ("→", "g", 70), ("∪", "g", 90, COR), ("união: tudo junto", "i", 70)]),
                 ("s18.c", [("−", "g", 90, COR), ("tira o que está no outro", "i", 70)]),
                 ("s18.d", [("complementar:", "g", 70, COR), ("o que falta para o universo", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 28, 52, a=a), centro(c, str(i + 1), 260, y - 6, 60, "g", E.SOBRE, a)))
            fz(c, t, C[k] + 0.1, partes, 350, y)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    ka, kb, kc, kd = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.2, ps("na próxima aula, o Venn resolve", "i", 72), XE, 230, passo=0.1)
    E.frase(c, t, C["s19"] + 0.9, [("problemas", "g", 110, COR)], XE, 370)
    E.frase(c, t, ka, ps("quantos alunos", "i", 66) + [("não praticam nenhum esporte?", "g", 66)], XE, 560, "left", 0.1)
    E.venn(c, t, kb, 1580, 290, 100, ("A", "B", "C"), size=40)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 640, 730, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, kc + 0.3, 0.8))
    E.cursor(c, lerp(970, 800, p), lerp(960, 755, p), ep(t, kc + 0.2, 0.4))
    E.frase(c, t, kd, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, venn=b_venn, intersecao=b_intersecao, uniao=b_uniao, diferenca=b_diferenca,
              complementar=b_complementar, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
