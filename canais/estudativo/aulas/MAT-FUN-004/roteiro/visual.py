"""Visual — Estudativo · MAT-FUN-004: domínio, contradomínio e imagem.

Linguagem visual da trilha Funções (MAT-FUN-001 a 003): entrada em índigo (ENT), saída em preto (SAI).
- domínio (D) = o oval A pintado de índigo claro, com o rótulo "D" em índigo; na reta, trecho índigo (E.intervalo).
- contradomínio (CD) = o contorno grosso do oval B, rótulo "CD" em preto.
- imagem (Im) = um disco cinza-escuro atrás de cada elemento de B que recebe flecha, rótulo "Im" em preto.
  O elemento do CD que fica fora da imagem ganha um anel cinza; no erro, o que foi posto errado na imagem fica vermelho.
Peças locais: ovais(), flecha(), dominio(), imagem(), tabela2(), mista()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-004_dominio_contradominio_imagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("diagrama", "tabela", "contexto", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert [2 * x for x in (1, 2, 3, 4)] == [2, 4, 6, 8] and 20 * 2.5 == 50
assert sorted({x * x for x in (-1, 0, 1, 2)}) == [0, 1, 4]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- símbolos de conjunto (a fonte da casa não tem ∈ ⊂ ∪ ∩ ℕ ℤ ℚ ℝ; mesma solução da MAT-CON-004) ----------------
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


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def mista(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [tw(s, est, size) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x
    for (s, cor), w in zip(partes, ws):
        tx(c, s, xx, y, size, est, cor, a)
        xx += w
    return sum(ws)


def pilula_tx(c, s, cx, cy, size, fundo, a=1.0):
    """pílula com texto que pode ter símbolos de conjunto"""
    if a <= 0:
        return
    w, h = tw(s, "g", size) + size * 1.1, size * 1.6
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, fundo, a)
    tx(c, s, cx, cy + size * 0.33, size, "g", BR, a, "center")


def mista_em(c, t, t0, partes, x, y, size, align="left", est="g"):
    E.foco(c, t, t0, 0.5, lambda a: mista(c, partes, x, y, size, a, align, est))


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


class Dg:
    """geometria de um diagrama de flechas: centros dos ovais, raios e lugar de cada elemento"""

    def __init__(s, cxa, cxb, cy, A, B, dy=100, rw=130):
        s.cxa, s.cxb, s.cy, s.A, s.B, s.dy, s.rw = cxa, cxb, cy, A, B, dy, rw
        s.rh = (max(len(A), len(B)) * dy + 70) / 2
        s.pa = {v: (cxa, cy + (i - (len(A) - 1) / 2) * dy) for i, v in enumerate(A)}
        s.pb = {v: (cxb, cy + (i - (len(B) - 1) / 2) * dy) for i, v in enumerate(B)}


def ovais(c, t, g, ta, tb, size=60, nomes=("A", "B"), escuro=False):
    """desenha os dois ovais (A índigo, B preto) e os elementos; ta/tb = instante de cada conjunto"""
    tinta = BR if escuro else TINTA
    ca = CLARO if escuro else ENT
    for cx, els, cor, tt, nome, pos in ((g.cxa, g.A, ca, ta, nomes[0], g.pa), (g.cxb, g.B, tinta, tb, nomes[1], g.pb)):
        q = ease_io(prog(t, tt, 0.6))
        if q > 0:
            r = skia.Rect.MakeXYWH(cx - g.rw, g.cy - g.rh, 2 * g.rw, 2 * g.rh)
            if not escuro:
                c.drawOval(r, M.paint(BR, 0.75 * q))
            c.drawArc(r, -90, 360 * q, False, M.paint(cor, 1.0, stroke=6, cap_round=True))
        if nome:
            E.foco(c, t, tt + 0.3, 0.4, lambda a, cx=cx, nome=nome, cor=cor: centro(c, nome, cx, g.cy - g.rh - 26, 64, "g", cor, a))
        for i, v in enumerate(els):
            X, Y = pos[v]
            E.foco(c, t, tt + 0.3 + 0.1 * i, 0.4, lambda a, v=v, X=X, Y=Y, cor=cor: centro(c, E._num(v), X, Y + size * 0.36, size, "g", cor, a), sobe=6)


def flecha(c, t, t0, p0, p1, cor=None, d=0.6, folga=(46, 52), largura=6):
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    M.arrow(c, x0 + ux * folga[0], y0 + uy * folga[0], x1 - ux * folga[1], y1 - uy * folga[1], cor or ENT, 1.0, largura, 22, p)


def dominio(c, g, a, cor=None):
    """o domínio: o oval A inteiro pintado de índigo claro"""
    if a > 0:
        c.drawOval(skia.Rect.MakeXYWH(g.cxa - g.rw, g.cy - g.rh, 2 * g.rw, 2 * g.rh), M.paint(cor or ENT, 0.16 * a))


def contra(c, g, a, cor=None):
    """o contradomínio: contorno grosso do oval B"""
    if a > 0:
        c.drawOval(skia.Rect.MakeXYWH(g.cxb - g.rw, g.cy - g.rh, 2 * g.rw, 2 * g.rh), M.paint(cor or SAI, a, stroke=14))


def imagem(c, g, els, a, cor=None, r=44):
    """a imagem: um disco escuro e suave atrás de cada elemento de B que recebe flecha"""
    if a > 0:
        for v in els:
            X, Y = g.pb[v]
            c.drawCircle(X, Y, r, M.paint(cor or SAI, 0.16 * a))


def anel(c, t, t0, X, Y, r=46, cor=ERRADO, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, X, Y, r, -90, 360 * q, cor, largura)


def tabela2(c, t, t0, linhas, x, y, cab=("entrada", "saída"), wc=260, hl=92, size=64, tl=None):
    a = ep(t, t0, 0.5)
    n = len(linhas)
    if a > 0:
        centro(c, cab[0], x + wc / 2, y - 24, 46, "b", ENT, a)
        centro(c, cab[1], x + wc * 1.5, y - 24, 46, "b", SAI, a)
        M.line(c, x, y, x + 2 * wc, y, TINTA, a, 4)
        M.line(c, x + wc, y, x + wc, y + hl * n + 10, TINTA, a, 4)
    caixas = []
    for i, (e, s) in enumerate(linhas):
        ry = y + 10 + hl * i
        caixas.append((x - 10, ry, 2 * wc + 20, hl))
        ti = tl[i] if tl else t0 + 0.3 + 0.15 * i
        E.foco(c, t, ti, 0.4, lambda q, e=e, s=s, ry=ry: (
            centro(c, E._num(e), x + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ENT, q),
            centro(c, E._num(s), x + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", SAI, q)), sobe=6)
    return caixas


def rotulo(c, t, t0, s, x, y, cor, sub=None, align="left"):
    E.frase(c, t, t0, [(s, "g", 72, cor)], x, y, align)
    if sub:
        E.frase(c, t, t0 + 0.4, ps(sub, "i", 48, TINTA2), x, y + 62, align, 0.06)


# ---------------- gancho ----------------
def pessoa(c, X, Y, cor, a, meia=False):
    """bonequinho simples: cabeça e corpo; meia=True corta a metade direita"""
    if a <= 0:
        return
    c.save()
    if meia:
        c.clipRect(skia.Rect.MakeLTRB(X - 80, Y - 200, X, Y + 80))
    c.drawCircle(X, Y - 120, 40, M.paint(cor, a))
    M.rrect(c, X - 60, Y - 66, 120, 140, 50, cor, a)
    c.restore()
    if meia:
        M.line(c, X, Y - 175, X, Y + 90, ERRADO, a, 5, dash=[12, 10])


def b_gancho(c, t, C, b):
    def cena1():
        E.frase(c, t, C["s01.a"], [("R$", "g", 96, COR), ("20", "g", 96, COR), ("por", "i", 80), ("pessoa", "i", 80)], XE, 300)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (pessoa(c, 1180, 520, ENT, a), pessoa(c, 1360, 520, ENT, a)))
        E.foco(c, t, C["s01.b"] + 0.4, 0.5, lambda a: pessoa(c, 1540, 520, ERRADO if t > C["s01.c"] else ENT, a, meia=True))
        E.frase(c, t, C["s01.b"], [("2,5", "g", 96), ("pessoas", "i", 80)], XE, 460)
        E.frase(c, t, C["s01.b"] + 2.4, [("20", "g", 72, TINTA2), ("×", "g", 72, TINTA2), ("2,5", "g", 72, TINTA2), ("=", "g", 72, TINTA2), ("50", "g", 80)],
                XE, 580)
        E.frase(c, t, C["s01.c"], [("meia", "i", 80), ("pessoa", "i", 80), ("não", "g", 76, ERRADO), ("existe", "g", 76, ERRADO)], XE, 760)
        E.frase(c, t, C["s01.d"], ps("o que pode entrar numa função?", "i", 64, TINTA2), XE, 900, passo=0.1)
    E.saida(c, t, C["s01.e"] - 0.1, cena1)
    E.saida(c, t, C["s02"] - 0.1, lambda: E.frase(c, t, C["s01.e"], [("domínio", "g", 250, COR)], W / 2, 620, "center"))
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("domínio", "g", 120, ENT), ("e", "i", 110)], XE, 450)
        E.frase(c, t, C["s02.a"] + 2.2, [("imagem", "g", 120)], XE, 580)
        E.frase(c, t, C["s02.a"] + 4.4, [("como", "i", 90), ("intervalo", "g", 90, COR)], XE, 730)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "a saída quando entra x:", "f(x)"), ("s03.c", "naturais e inteiros:", "ℕ e ℤ"), ("s03.d", "um pedaço da reta:", "intervalo"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 80)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: tx(c, l2, x + 44, y + 160, 64, "g", COR, a))
    E.foco(c, t, C["s03.d"] + 0.6, 0.5, lambda a: E.escreve(c, "[0, 5]", x + 560, 190 + 2 * 240 + 160, 64, "g", TINTA2, a))
    alvo = [x + w - 30, 190 + 170, 430 + 170, 670 + 170]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, alvo[0], lerp(lerp(alvo[1], alvo[2], q1), alvo[3], q2), ep(t, C["s03.b"], 0.4))


# ---------------- diagrama ----------------
G = Dg(760, 1160, 590, [1, 2, 3, 4], [2, 4, 6, 8, 10])
FL = [(1, 2), (2, 4), (3, 6), (4, 8)]


def diagrama(c, t, ta, tb, tf, passo=0.5):
    ovais(c, t, G, ta, tb)
    for i, (e, s) in enumerate(FL):
        flecha(c, t, tf + passo * i, G.pa[e], G.pb[s])


def b_diagrama(c, t, C, b):
    mista_em(c, t, C["s04.a"], [("f(", TINTA), ("x", ENT), (") = 2", TINTA), ("x", ENT)], W / 2, 190, 100, "center")
    diagrama(c, t, C["s04.b"], C["s04.c"], C["s04.d"])
    q = pulso(t, C["s05.a"], 2.4)
    if q > 0:
        M.arrow(c, G.cxa - 40, G.cy + G.rh + 70, G.cxb + 40, G.cy + G.rh + 70, ENT, q, 8, 26)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: mista(c, [("f: ", TINTA), ("A", ENT), (" → ", TINTA2), ("B", SAI)], W / 2, 1000, 90, a, "center"))


def b_nomes(c, t, C, b):
    mista(c, [("f(", TINTA), ("x", ENT), (") = 2", TINTA), ("x", ENT)], W / 2, 190, 100, 1.0, "center")
    dominio(c, G, ep(t, C["s06.a"], 0.5))
    contra(c, G, ep(t, C["s06.c"], 0.5))
    imagem(c, G, [2, 4, 6, 8], ep(t, C["s07.b"], 0.6))
    diagrama(c, t, -10, -10, -10)
    anel(c, t, C["s07.d"], *G.pb[10], 46, TINTA2)
    rotulo(c, t, C["s06.a"], "domínio", XE, 420, ENT, "todas as entradas")
    E.foco(c, t, C["s06.b"] + 1.2, 0.5, lambda a: mista(c, [("D = A", ENT)], XE, 600, 64, a))
    rotulo(c, t, C["s06.c"], "contradomínio", 1330, 360, SAI, "onde as saídas podem cair")
    E.foco(c, t, C["s06.d"] + 1.0, 0.5, lambda a: mista(c, [("CD = B", SAI)], 1330, 520, 64, a))
    rotulo(c, t, C["s07.a"], "imagem", 1330, 680, SAI, "o que sai de verdade")
    E.foco(c, t, C["s07.c"], 0.5, lambda a: mista(c, [("Im = {2, 4, 6, 8}", SAI)], 1330, 840, 60, a))
    E.frase(c, t, C["s07.d"], [("10:", "g", 46, TINTA2), ("ninguém", "i", 46, TINTA2), ("tem", "i", 46, TINTA2), ("dobro", "i", 46, TINTA2),
                               ("10", "g", 46, TINTA2)], XE, 880)
    E.foco(c, t, C["s07.e"], 0.5, lambda a: pilula_tx(c, "Im ⊂ CD", W / 2, 1000, 60, SAI, a))


# ---------------- tabela ----------------
def b_tabela(c, t, C, b):
    E.frase(c, t, C["s08.a"], [("numa", "i", 84), ("tabela", "g", 80, COR)], W / 2, 160, "center")
    x, y, wc = 300, 310, 260
    linhas = [(1, 5), (2, 8), (3, 8), (4, 10)]
    tl = [C["s08.b"] + k for k in (0, 1.6, 3.0, 4.3)]
    cx = tabela2(c, t, C["s08.b"] - 0.4, linhas, x, y, ("horas", "preço (R$)"), wc=wc, tl=tl)
    yb = y + 10
    hh = 92 * 4
    q = ep(t, C["s08.c"], 0.5)
    if q > 0:
        M.rrect(c, x + 10, yb, wc - 20, hh, 20, ENT, 0.14 * q)
    q = ep(t, C["s08.d"], 0.5)
    if q > 0:
        M.rrect(c, x + wc + 10, yb, wc - 20, hh, 20, SAI, 0.12 * q)
    for i in (1, 2):
        anel(c, t, C["s08.e"] + 0.3 * (i - 1), x + wc * 1.5, cx[i][1] + 46, 42, TINTA2)
    mista_em(c, t, C["s08.c"], [("D = {1, 2, 3, 4}", ENT)], 1000, 430, 72)
    mista_em(c, t, C["s08.d"], [("Im = {5, 8, 10}", SAI)], 1000, 600, 72)
    E.frase(c, t, C["s08.e"], [("o", "i", 60), ("8", "g", 64), ("aparece", "i", 60), ("2", "g", 64), ("vezes,", "i", 60)], 1000, 780)
    E.frase(c, t, C["s08.e"] + 1.6, [("entra", "i", 60), ("uma", "g", 60), ("vez", "g", 60), ("só", "i", 60)], 1000, 860)


# ---------------- contexto ----------------
def b_contexto(c, t, C, b):
    def churras():
        E.frase(c, t, C["s09.a"], ps("o domínio vem da vida real", "i", 76), W / 2, 190, "center", 0.12)
        E.frase(c, t, C["s09.b"], [("entrada:", "i", 64), ("número", "g", 64, ENT), ("de", "i", 64), ("pessoas", "g", 64, ENT)], W / 2, 330, "center")
        vx = E.reta(c, t, C["s09.c"] - 0.3, 300, 1620, 640, 0, 6, list(range(0, 7)), E._num, size=50)
        for i in range(0, 7):
            k = ease_back(prog(t, C["s09.c"] + 0.2 * min(i, 4), 0.4))
            if k > 0:
                c.drawCircle(vx(i), 640, 18 * k, M.paint(ENT))
        E.foco(c, t, C["s09.c"] + 1.2, 0.4, lambda a: centro(c, "…", 1720, 655, 80, "g", ENT, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: mista(c, [("D = ℕ", ENT)], W / 2, 880, 110, a, "center"))
        if t >= C["s09.e"]:
            X = vx(2.5)
            E.foco(c, t, C["s09.e"], 0.4, lambda a: (centro(c, "2,5", X, 560, 52, "g", ERRADO, a),))
            E.risco(c, X - 26, 614, X + 26, 666, t, C["s09.e"] + 0.2, largura=8)
            E.risco(c, X + 26, 614, X - 26, 666, t, C["s09.e"] + 0.35, largura=8)
    E.saida(c, t, C["s10"] - 0.1, churras)
    if t < C["s10"]:
        return

    def carro():
        mista_em(c, t, C["s10.a"], [("d(", TINTA), ("t", ENT), (") = 80", TINTA), ("t", ENT)], W / 2, 220, 110, "center")
        E.frase(c, t, C["s10.a"] + 0.6, ps("80 km por hora", "i", 54, TINTA2), W / 2, 310, "center", 0.08)
        E.frase(c, t, C["s10.b"], [("t", "g", 76, ENT), ("=", "g", 72), ("tempo", "i", 72), ("de", "i", 72), ("viagem", "i", 72), ("(h)", "i", 64, TINTA2)],
                W / 2, 450, "center")
        E.frase(c, t, C["s10.c"], [("2,5", "g", 72, ENT), ("horas:", "i", 70), ("existe", "g", 70, CERTO)], 330, 620)
        E.foco(c, t, C["s10.c"] + 0.6, 0.4, lambda a: E.selo(c, 1120, 598, 34, True, a))
        E.frase(c, t, C["s10.d"], [("tempo", "i", 70), ("negativo:", "g", 70, ERRADO), ("não", "i", 70)], 330, 760)
        E.foco(c, t, C["s10.d"] + 0.6, 0.4, lambda a: E.selo(c, 1120, 738, 34, False, a))
        E.foco(c, t, C["s10.e"], 0.5, lambda a: mista(c, [("D: ", TINTA), ("t ≥ 0", ENT)], W / 2, 940, 110, a, "center"))
    E.saida(c, t, C["s11"] - 0.1, carro)
    if t < C["s11"]:
        return
    mista(c, [("D: ", TINTA), ("t ≥ 0", ENT)], W / 2, 260, 96, ep(t, C["s11"], 0.3), "center")
    vx = E.reta(c, t, C["s11"], 300, 1600, 560, -2, 6, list(range(-2, 7)), E._num, size=48)
    E.intervalo(c, t, C["s11.a"], vx, 560, 0, None, fecha_ini=True, fecha_fim=False)
    E.foco(c, t, C["s11.a"] + 0.4, 0.5, lambda a: mista(c, [("[0, +∞[", ENT)], W / 2, 820, 140, a, "center"))
    E.foco(c, t, C["s11.b"], 0.4, lambda a: (centro(c, "fechado no 0", vx(0), 470, 50, "b", ENT, a),))
    anel(c, t, C["s11.b"], vx(0), 560, 34, ENT)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: centro(c, "aberto no +∞", 1600, 470, 50, "b", ENT, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("trocar", "i", 72), ("contradomínio", "g", 68), ("por", "i", 72), ("imagem", "g", 68, ERRADO)], W / 2, 170, "center")
    diagrama(c, t, C["s12"] - 0.6, C["s12"] - 0.4, C["s12"] - 0.2, 0.1)
    errado = 1 - ep(t, C["s12.d"], 0.5)
    imagem(c, G, [2, 4, 6, 8, 10], ep(t, C["s12.b"], 0.5) * errado, ERRADO)
    if C["s12.b"] <= t < C["s12.d"] + 0.5:
        E.foco(c, t, C["s12.b"], 0.5, lambda a: mista(c, [("Im = {2, 4, 6, 8, 10}", ERRADO)], XE, 450, 52, a * errado))
        if t > C["s12.b"] + 0.6:
            E.risco(c, XE, 470, XE + 520, 400, t, C["s12.b"] + 1.2, largura=8)
    anel(c, t, C["s12.c"], *G.pb[10], 48)
    E.frase(c, t, C["s12.c"], [("10:", "g", 56, ERRADO), ("sem", "i", 56), ("flecha", "i", 56)], 1360, 880)
    contra(c, G, pulso(t, C["s12.d"], 1.6))
    imagem(c, G, [2, 4, 6, 8], ep(t, C["s12.e"], 0.5))
    rotulo(c, t, C["s12.d"], "CD", 1360, 420, SAI, "onde pode chegar")
    rotulo(c, t, C["s12.e"], "Im", 1360, 620, SAI, "onde chega de fato")
    E.foco(c, t, C["s12.e"] + 0.5, 0.5, lambda a: mista(c, [("Im = {2, 4, 6, 8}", SAI)], XE, 640, 52, a))


# ---------------- atalho (palco escuro) ----------------
GA = Dg(1420, 1730, 600, [1, 2, 3], [2, 4, 6, 8], dy=96, rw=100)


def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 72, CLARO), XE, 180)
        E.frase(c, t, C["s13.a"], [("domínio:", "g", 72, CLARO), ("de", "i", 72, BR), ("onde", "i", 72, BR), ("SAI", "g", 72, BR), ("flecha", "i", 72, BR)], XE, 330)
        E.frase(c, t, C["s13.b"], [("imagem:", "g", 72, BR), ("onde", "i", 72, CLARO), ("CHEGA", "g", 72, BR), ("flecha", "i", 72, CLARO)], XE, 460)
        E.frase(c, t, C["s13.c"], [("tabela:", "g", 54, BR), ("domínio", "i", 54, CLARO), ("=", "i", 54, CLARO), ("coluna", "i", 54, CLARO), ("de", "i", 54, CLARO),
                                   ("entrada", "g", 54, CLARO)], XE, 680)
        E.frase(c, t, C["s13.d"], [("imagem", "i", 54, CLARO), ("=", "i", 54, CLARO), ("coluna", "i", 54, CLARO), ("de", "i", 54, CLARO), ("saída,", "g", 54, BR),
                                   ("sem", "i", 54, CLARO), ("repetir", "g", 54, BR)], XE, 770)
        a = ep(t, C["s13.a"], 0.5)
        if a > 0:
            dominio(c, GA, a * 1.6, CLARO)
            ovais(c, t, GA, C["s13.a"], C["s13.a"] + 0.2, size=52, escuro=True)
            for i, (e, s) in enumerate([(1, 2), (2, 4), (3, 6)]):
                flecha(c, t, C["s13.a"] + 0.4 + 0.2 * i, GA.pa[e], GA.pb[s], CLARO, folga=(40, 46))
            imagem(c, GA, [2, 4, 6], ep(t, C["s13.b"], 0.5) * 2.2, BR, 38)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("cada", "i", 76, CLARO), ("flecha:", "i", 76, CLARO), ("entrada", "g", 76, CLARO), ("→", "g", 76, BR), ("saída", "g", 76, BR)],
            W / 2, 280, "center")
    E.frase(c, t, C["s14.b"], [("não", "g", 72, ERRADO), ("compensa:", "i", 72, CLARO), ("função", "i", 72, CLARO), ("de", "i", 72, CLARO), ("uma", "i", 72, CLARO),
                               ("história", "g", 72, BR)], W / 2, 520, "center")
    E.frase(c, t, C["s14.b"] + 2.6, ps("sem desenho nem tabela", "i", 56, CLARO), W / 2, 610, "center", 0.08)
    E.frase(c, t, C["s14.c"], [("o", "i", 76, CLARO), ("que", "i", 76, CLARO), ("a", "i", 76, CLARO), ("situação", "i", 76, CLARO), ("deixa", "i", 76, CLARO),
                               ("entrar?", "g", 76, BR)], W / 2, 830, "center")


# ---------------- questão ----------------
GQ = Dg(1240, 1600, 560, [-1, 0, 1, 2], [0, 1, 2, 3, 4], dy=96, rw=110)
FQ = [(-1, 1), (0, 0), (1, 1), (2, 4)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 190)
    mista_em(c, t, C["s15.a"], [("f(", TINTA), ("x", ENT), (") = ", TINTA), ("x", ENT), ("²", TINTA)], XE, 320, 96)
    mista_em(c, t, C["s15.a"] + 1.4, [("f: ", TINTA), ("A", ENT), (" → ", TINTA2), ("B", SAI)], XE + 420, 320, 72)
    ovais(c, t, GQ, C["s15.b"], C["s15.c"], size=54)
    E.frase(c, t, C["s15.d"], [("D?", "g", 70, ENT), ("CD?", "g", 70), ("Im?", "g", 70)], XE, 480)
    E.frase(c, t, C["s15.e"], [("loja:", "g", 60), ("entrada", "i", 60), ("=", "i", 60), ("nº", "i", 60), ("de", "i", 60), ("camisetas", "g", 60, ENT)], XE, 700)
    E.frase(c, t, C["s15.f"], [("que", "i", 64), ("números", "i", 64), ("entram?", "g", 64, COR)], XE, 800)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=860, cy=420, r=56)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    G2 = GQ
    dominio(c, G2, ep(t, C["s17.e"], 0.5))
    contra(c, G2, ep(t, C["s17.f"], 0.5) * (1 - 0.6 * ep(t, C["s18"], 0.5)))
    imagem(c, G2, [0, 1, 4], ep(t, C["s18.a"], 0.5))
    ovais(c, t, G2, C["s17"] - 2, C["s17"] - 2, size=54)
    for e, s in FQ:
        k = {-1: "s17.a", 0: "s17.b", 1: "s17.c", 2: "s17.d"}[e]
        flecha(c, t, C[k], G2.pa[e], G2.pb[s], folga=(44, 48))
    for k, (e, s) in zip(("s17.a", "s17.b", "s17.c", "s17.d"), FQ):
        y = 260 + 90 * FQ.index((e, s))
        E.foco(c, t, C[k], 0.4, lambda a, e=e, s=s, y=y: mista(c, [("(", TINTA), (E._num(e), ENT), (")² = ", TINTA), (str(s), SAI)], XE, y, 64, a))
    E.foco(c, t, C["s17.e"], 0.5, lambda a: mista(c, [("D = A", ENT)], XE, 690, 64, a))
    E.foco(c, t, C["s17.f"], 0.5, lambda a: mista(c, [("CD = B", SAI)], XE + 330, 690, 64, a))
    E.foco(c, t, C["s18.a"], 0.5, lambda a: mista(c, [("Im = {0, 1, 4}", SAI)], XE, 800, 72, a))
    for v in (2, 3):
        anel(c, t, C["s18.b"] + 0.2 * (v - 2), *G2.pb[v], 40, TINTA2)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: pilula_tx(c, "camisetas: ℕ", XE + 260, 930, 60, ENT, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", [("domínio:", "g", 84, ENT), ("o", "i", 84), ("que", "i", 84), ("entra", "i", 84)]),
                 ("s19.b", [("contradomínio:", "g", 84), ("onde", "i", 84), ("pode", "i", 84), ("chegar", "i", 84)]),
                 ("s19.c", [("imagem:", "g", 84), ("o", "i", 84), ("que", "i", 84), ("sai", "i", 84), ("de", "i", 84), ("verdade", "i", 84)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s20.a"], [("domínio", "g", 130, COR)], XE, 460)
    E.frase(c, t, C["s20.a"] + 0.4, [("pela", "i", 120), ("fórmula", "g", 130, COR)], XE, 600)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: (E.formula(c, "f{1}{x − 2}", XE, 790, 76, "g", TINTA, a),
                                             E.formula(c, "r{x − 3}", XE + 300, 790, 76, "g", TINTA, a)))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, diagrama=b_diagrama, nomes=b_nomes, tabela=b_tabela, contexto=b_contexto,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
