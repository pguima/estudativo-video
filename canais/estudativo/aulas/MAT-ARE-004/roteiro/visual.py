"""Visual — Estudativo · MAT-ARE-004: área do trapézio ((B + b) · h / 2) e do losango (D · d / 2).
Mesma linguagem da trilha (docstring de MAT-ARE-001) e o mesmo recorte que desliza de MAT-ARE-003 (peca, fantasma, mexe):
- trapézio + cópia girada 180° em volta do meio do lado = paralelogramo de base B + b;
- losango dentro do retângulo das diagonais: 4 triângulos dentro, 4 iguais fora;
- base do meio (atalho): as pontas que sobram embaixo giram e tapam as que faltam em cima.
B (base maior) na cor da matéria, b (base menor) em cinza escuro, como as duas famílias de MAT-ANG-001.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-004_area_trapezio_losango.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("trapezio", "losango", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert (10 + 6) * 4 // 2 == 32 and 10 * 4 // 2 + 6 * 4 // 2 == 32 and 8 * 6 // 2 == 24 and 10 * 4 == 40 and (10 + 6) // 2 * 4 == 32
assert (7 + 4) * (6 // 2) == 33 and (25 + 15) // 2 * 12 == 240 and 50 * 30 // 2 == 750


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo (palavra com ² ou ³ vai na grotesca: a serifada não tem o expoente)"""
    return [(w, "g" if any(ch in w for ch in "²³") else est, size * (0.92 if any(ch in w for ch in "²³") and est != "g" else 1), cor)
            for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    """desenha fn de t0 até t1 e some desfocando"""
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def cota_h(c, t, t0, txt, x0, x1, y, cor=None, size=50, a=1.0):
    def f(q):
        q *= a
        M.line(c, x0, y, x1, y, cor or TINTA2, q, 3)
        M.line(c, x0, y - 12, x0, y + 12, cor or TINTA2, q, 3)
        M.line(c, x1, y - 12, x1, y + 12, cor or TINTA2, q, 3)
        centro(c, txt, (x0 + x1) / 2, y - 22 if y >= 0 else y, size, "g", cor or COR, q)
    E.foco(c, t, t0, 0.5, f)


def cota_hb(c, t, t0, txt, x0, x1, y, cor=None, size=50, a=1.0):
    """cota com o texto embaixo da linha"""
    def f(q):
        q *= a
        M.line(c, x0, y, x1, y, cor or TINTA2, q, 3)
        M.line(c, x0, y - 12, x0, y + 12, cor or TINTA2, q, 3)
        M.line(c, x1, y - 12, x1, y + 12, cor or TINTA2, q, 3)
        centro(c, txt, (x0 + x1) / 2, y + 22 + size * 0.8, size, "g", cor or COR, q)
    E.foco(c, t, t0, 0.5, f)


def cota_v(c, t, t0, txt, x, y0, y1, cor=None, size=50, a=1.0, direita=False):
    def f(q):
        q *= a
        M.line(c, x, y0, x, y1, cor or TINTA2, q, 3)
        M.line(c, x - 12, y0, x + 12, y0, cor or TINTA2, q, 3)
        M.line(c, x - 12, y1, x + 12, y1, cor or TINTA2, q, 3)
        xt = x + 24 if direita else x - 24 - E.larg(txt, "g", size)
        E.escreve(c, txt, xt, (y0 + y1) / 2 + size * 0.36, size, "g", cor or COR, q)
    E.foco(c, t, t0, 0.5, f)


def ret_pts(x, y, w, h):
    """cantos do retângulo a partir do de cima à esquerda, no sentido horário"""
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


def no_caminho(pts, p, fecha=True):
    """ponto a uma fração p (0..1) do caminho pelos pontos"""
    lados = list(zip(pts, pts[1:] + (pts[:1] if fecha else [])))
    comp = [math.dist(a, b) for a, b in lados]
    alvo = sum(comp) * min(max(p, 0.0), 1.0)
    for (a, b), L in zip(lados, comp):
        if alvo <= L:
            f = alvo / L if L else 0
            return lerp(a[0], b[0], f), lerp(a[1], b[1], f)
        alvo -= L
    return pts[0] if fecha else pts[-1]


def cerca(c, pts, p, cor=None, fecha=True, largura=12, postes=True, a=1.0):
    """o PERÍMETRO: contorno grosso que se desenha em volta (p = 0..1 do caminho), com mourões a cada ~70 px"""
    if p <= 0 or a <= 0:
        return
    cor = cor or E.COR
    if a < 1:
        c.saveLayer(None, M.paint("#000000", a))
    E._contorno(c, pts, p, cor, largura, fecha)
    if postes:
        lados = list(zip(pts, pts[1:] + (pts[:1] if fecha else [])))
        total = sum(math.dist(u, v) for u, v in lados)
        n = max(2, int(total / 70))
        for k in range(n + (0 if fecha else 1)):
            f = k / n
            if f <= p + 1e-6:
                x_, y_ = no_caminho(pts, f, fecha)
                c.drawCircle(x_, y_, largura * 0.85, M.paint(cor))
                c.drawCircle(x_, y_, largura * 0.38, M.paint("#FFFFFF"))
    if a < 1:
        c.restore()


def tracejado(c, pts, cor=None, a=1.0, largura=6, fecha=False):
    if a <= 0:
        return
    path = skia.Path()
    path.addPoly([tuple(p_) for p_ in pts], fecha)
    pt = M.paint(cor or CINZA, a, stroke=largura, cap_round=True)
    pt.setPathEffect(skia.DashPathEffect.Make([18, 14], 0))
    c.drawPath(path, pt)


def num_lado(c, t, t0, n, x, y, cor=None, r=34):
    """número do lado numa bolinha (contar os lados)"""
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, x, y, r * ease_back(prog(t, t0, 0.4)), cor, a),
                                     centro(c, str(n), x, y + 13, 38, "g", E.SOBRE, a)))


def grade_q(c, t, t0, cols, lins, x, y, s, cor=None, dur=1.2, a=1.0, ti=None):
    """quadradinhos de lado s a partir do canto (x, y), entrando fileira a fileira em `dur` segundos"""
    if a <= 0:
        return
    for r in range(lins):
        for k in range(cols):
            i = r * cols + k
            t_ = (ti[r] + 0.12 * k) if ti else t0 + dur * i / max(1, cols * lins)
            q = ep(t, t_, 0.3) * a
            if q > 0:
                M.rrect(c, x + k * s + 3, y + r * s + 3, s - 6, s - 6, s * 0.1, cor or E.COR, q)


# ================= a ESCADA das unidades (mesma peça da trilha Medidas e Unidades) =================
class Escada:
    """degraus descendo da esquerda para a direita. (x, y) = canto de cima do 1º degrau; sw, sh = largura e altura do degrau.
    base = onde todos os degraus apoiam. meio = índice da unidade principal (degrau cheio da cor da matéria)."""

    def __init__(s, x=110, y=300, sw=186, sh=78, base=950, un=("m", "dm", "cm"), nomes=("metro", "decímetro", "centímetro"), meio=0, size=60):
        s.x, s.y, s.sw, s.sh, s.base, s.un, s.nomes, s.meio, s.size = x, y, sw, sh, base, un, nomes, meio, size
        s.n = len(un)

    def cx(s, i):
        return s.x + (i + 0.5) * s.sw

    def topo(s, i):
        return s.y + i * s.sh

    def ponto(s, i):
        k = min(max(i, 0), s.n - 1)
        return s.cx(k), s.y + k * s.sh - 34

    def degraus(s, c, t, td, a=1.0, acesos=(), ta=None):
        if a <= 0:
            return
        for i in range(s.n):
            ti = td + 0.09 * i
            q = ep(t, ti, 0.45)
            if q <= 0:
                continue
            top, x0 = s.topo(i), s.x + i * s.sw
            hh = (s.base - top) * ease_io(prog(t, ti, 0.45))
            meio = i == s.meio
            fundo, borda, tinta = (E.COR, E.COR, E.SOBRE) if meio else ("#FFFFFF", TINTA2, TINTA)
            acende = ep(t, ta, 0.4) if (i in acesos and ta is not None and not meio) else 0.0
            M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, fundo, q * a)
            if acende > 0:
                M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, E.COR, 0.16 * acende * q * a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 4, s.base - hh, s.sw - 8, hh), 12, 12), M.paint(borda, q * a, stroke=3))
            E.foco(c, t, ti + 0.2, 0.45, lambda b, i=i, top=top, tinta=tinta: centro(c, s.un[i], s.cx(i), top + s.size * 1.12, s.size, "g", tinta, b * a))
            cor_n = E.SOBRE if meio else TINTA2
            E.foco(c, t, ti + 0.3, 0.45, lambda b, i=i, top=top, cor_n=cor_n: centro(c, s.nomes[i], s.cx(i), top + s.size * 1.12 + 50, 38, "i", cor_n, b * a))

    def pulos(s, c, t, i0, hops, t0, a=1.0, cor=None, dur=0.7):
        """bolinha que pula de degrau em degrau; cada pulo deixa um arco numerado (1 degrau = 1 casa)"""
        if a <= 0 or t < t0:
            return
        cor = cor or E.COR
        atual, pulo, de = float(i0), 0.0, i0
        for k, (th, j) in enumerate(hops):
            q = prog(t, th, dur)
            if q <= 0:
                break
            s._arco(c, de, j, min(1.0, q * 1.25), k + 1, cor, a)
            if q < 1:
                atual, pulo = lerp(de, j, ease_io(q)), math.sin(math.pi * q) * 70
                break
            atual, de = float(j), j
        x0, y0 = s.ponto(math.floor(atual))
        x1, y1 = s.ponto(math.ceil(atual))
        f = atual - math.floor(atual)
        E.bola(c, lerp(x0, x1, f), lerp(y0, y1, f) - pulo, 30 * ease_back(prog(t, t0, 0.5)), cor, a)

    def _arco(s, c, i, j, p, k, cor, a):
        (xa, ya), (xb, yb) = s.ponto(i), s.ponto(j)
        ya, yb = ya - 36, yb - 36
        mx, my = (xa + xb) / 2, min(ya, yb) - 64
        pts = [(lerp(lerp(xa, mx, u), lerp(mx, xb, u), u), lerp(lerp(ya, my, u), lerp(my, yb, u), u)) for u in [p * n / 24 for n in range(25)]]
        path = skia.Path()
        path.moveTo(*pts[0])
        for x_, y_ in pts[1:]:
            path.lineTo(x_, y_)
        c.drawPath(path, M.paint(cor, 0.75 * a, stroke=5, cap_round=True))
        if p >= 1:
            (xp, yp), (xe, ye) = pts[-2], pts[-1]
            ang = math.atan2(ye - yp, xe - xp)
            h = skia.Path()
            h.moveTo(xe + math.cos(ang) * 3, ye + math.sin(ang) * 3)
            h.lineTo(xe - 18 * math.cos(ang - 0.5), ye - 18 * math.sin(ang - 0.5))
            h.lineTo(xe - 18 * math.cos(ang + 0.5), ye - 18 * math.sin(ang + 0.5))
            h.close()
            c.drawPath(h, M.paint(cor, 0.75 * a))
            xm, ym = pts[12]
            c.drawCircle(xm, ym - 4, 24, M.paint(cor, a))
            centro(c, str(k), xm, ym + 11, 32, "g", E.SOBRE, a)


def posicao(t, pos, saltos, dur=0.7):
    atual, fim = float(pos), pos
    for t0, novo in saltos:
        q = ease_io(prog(t, t0, dur))
        if q <= 0:
            break
        if q >= 1:
            atual, fim = float(novo), novo
            continue
        return lerp(fim, novo, q)
    return atual


def num_un(c, t, dig, pos, saltos, x, y, size, unidades, cor=None, tv=None, some=False, t0=None):
    """número com a vírgula que anda (E.anda) e a unidade logo depois dele, que troca a cada salto. Devolve px (centro de cada casa)"""
    if t0 is not None and t < t0:
        return None
    a0 = ep(t, t0, 0.5) if t0 is not None else 1.0
    if a0 < 1:
        c.saveLayer(None, M.paint("#000000", a0))
    px = E.anda(c, t, dig, pos, saltos, x, y, size, cor=cor, tv=tv, some=some)
    cl = E.casa(size)
    ncas = max(len(dig), math.ceil(posicao(t, pos, saltos) - 1e-6))
    xu = x + ncas * cl + size * 0.3
    for k, (tu, u) in enumerate(unidades):
        prox = unidades[k + 1][0] if k + 1 < len(unidades) else None
        if t < tu:
            break
        if prox is not None and t >= prox + 0.35:
            continue
        sai = 1 - ep(t, prox, 0.35) if prox is not None else 1.0
        E.foco(c, t, tu, 0.4, lambda b, u=u: E.escreve(c, u, xu, y, size * 0.72, "g", COR, b * sai))
    if a0 < 1:
        c.restore()
    return px


def casas(c, t, t0, txt, cx, cy, cor=None, size=52):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, txt, cx, cy, size, "g", fundo=cor or E.COR, a=a, cor=E.SOBRE))


# ---------------- peças desta aula (recorte que desliza, igual a MAT-ARE-003) ----------------
def mexe(pts, dx=0.0, dy=0.0, ang=0.0, piv=None):
    """gira os pontos ang graus em volta de piv e depois anda (dx, dy)"""
    if ang and piv:
        co, si = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pts = [(piv[0] + (x - piv[0]) * co - (y - piv[1]) * si, piv[1] + (x - piv[0]) * si + (y - piv[1]) * co) for x, y in pts]
    return [(x + dx, y + dy) for x, y in pts]


def peca(c, pts, cor=None, alfa=0.14, a=1.0, borda=None, largura=6):
    if a <= 0:
        return
    path = skia.Path()
    path.addPoly([tuple(p_) for p_ in pts], True)
    c.drawPath(path, M.paint(cor or E.COR, alfa * a))
    pt = M.paint(borda or TINTA, a, stroke=largura)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pt)


def lado_cor(c, P0, P1, cor, q, largura=12):
    if q > 0:
        M.line(c, *P0, lerp(P0[0], P1[0], ease_io(q)), lerp(P0[1], P1[1], ease_io(q)), cor, 1.0, largura)


# o trapézio de bases 10 e 6 e altura 4 (60 px por unidade, isósceles)
U = 60
ZX, ZY = 200, 380
ZBL, ZBR, ZTR, ZTL = (ZX, ZY + 4 * U), (ZX + 10 * U, ZY + 4 * U), (ZX + 8 * U, ZY), (ZX + 2 * U, ZY)
TRAP = [ZBL, ZBR, ZTR, ZTL]
ZPE = (ZTL[0], ZBL[1])


def trap(c, t, t0, tB=None, tb=None, th=None, rB="10", rb="6", rh="4", alfa=0.12, a=1.0, escuro=False):
    """o trapézio com a base maior (cor da matéria), a menor (cinza escuro) e a altura tracejada"""
    if a <= 0:
        return
    if a < 1:
        c.saveLayer(None, M.paint("#000000", a))
    E.poligono(c, t, t0, TRAP, preenche=alfa, d=0.7, escuro=escuro)
    if tB is not None:
        lado_cor(c, ZBL, ZBR, E.COR, ep(t, tB, 0.5), 10)
        E.foco(c, t, tB + 0.2, 0.4, lambda q: centro(c, rB, (ZBL[0] + ZBR[0]) / 2, ZBL[1] + 72, 58, "g", CLARO if escuro else COR, q))
    if tb is not None:
        lado_cor(c, ZTL, ZTR, CLARO if escuro else TINTA2, ep(t, tb, 0.5), 10)
        E.foco(c, t, tb + 0.2, 0.4, lambda q: centro(c, rb, (ZTL[0] + ZTR[0]) / 2, ZTL[1] - 28, 58, "g", BR if escuro else TINTA2, q))
    if th is not None:
        E._altura(c, t, th, ZTL, ZPE, "", 1, 56)
        E.foco(c, t, th + 0.4, 0.4, lambda q: E.escreve(c, rh, ZTL[0] + 22, (ZTL[1] + ZPE[1]) / 2 + 20, 58, "g", BR if escuro else COR, q))
    if a < 1:
        c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        trap(c, t, ka, ka + 0.6, ka + 1.2, ka + 1.8)
        E.frase(c, t, kb, ps("duas bases", "i", 72) + [("diferentes", "g", 76, COR)], 1000, 330, "left", 0.1)
        E.frase(c, t, lerp(kb, kc, 0.5), ps("qual entra", "i", 70) + [("na conta?", "g", 74)], 1000, 460, "left", 0.1)
        E.frase(c, t, kc, [("as duas", "g", 100, COR)], 1000, 640, "left")
        if t >= kc:
            lado_cor(c, ZBL, ZBR, E.COR, ep(t, kc, 0.5), 14)
            lado_cor(c, ZTL, ZTR, TINTA2, ep(t, kc + 0.3, 0.5), 14)
        bola_res(c, t, kd, "32", 1480, 840, 120, 100)
        E.foco(c, t, kd + 0.3, 0.4, lambda a: E.escreve(c, "de área", 1630, 860, 60, "i", TINTA2, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 290, passo=0.12)
        E.frase(c, t, ta + 0.9, ps("a área do", "i", 78) + [("trapézio", "g", 96, COR)], XE, 440, passo=0.12)
        E.frase(c, t, ta + 1.6, ps("e do", "i", 78) + [("losango", "g", 96, COR)], XE, 570, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("e de onde vem", "i", 70) + [("cada fórmula", "g", 72)], XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "paralelogramo: b · h", "triângulo: a metade"), ("s03.c", "trapézio:", "os lados paralelos são as bases"),
             ("s03.d", "losango: diagonais", "em ângulo reto, cortadas ao meio"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, l2=l2, y=y: E.escreve(c, l2, x + 44, y + 160, 52, "g", COR, a))
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 590, q1), 840, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.7), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1010, "left", 0.12)


# ---------------- trapézio: duas cópias viram paralelogramo ----------------
ZM = ((ZBR[0] + ZTR[0]) / 2, (ZBR[1] + ZTR[1]) / 2)  # meio do lado direito: o giro de 180° em volta dele fecha o paralelogramo


def b_trapezio(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def ate_s06():
        trap(c, t, C["s04"] + 0.1, a4, b4, c4, "B = 10", "b = 6", "h = 4")
        if t < C["s05"]:
            E.frase(c, t, a4, [("B", "g", 80, COR)] + ps("= base maior", "i", 70), 1060, 330, "left", 0.1)
            E.frase(c, t, b4, [("b", "g", 80, TINTA2)] + ps("= base menor", "i", 70), 1060, 450, "left", 0.1)
            E.frase(c, t, c4, [("h", "g", 80, COR)] + ps("= altura, em ângulo reto", "i", 70), 1060, 570, "left", 0.1)
            return
        # a cópia: aparece ao lado, gira de cabeça para baixo e encosta no lado direito
        DX = 520
        gira = 180 * ease_io(prog(t, b5, 1.2))
        volta = DX * (1 - ease_io(prog(t, c5, 1.2)))
        copia = mexe(TRAP, volta, 0, gira, ZM)
        apaga = 1 - 0.65 * ep(t, b6, 0.5)
        E.foco(c, t, a5, 0.5, lambda a: peca(c, copia, CINZA, 0.45, a * apaga))
        if t >= d5:
            q = ep(t, d5, 0.6)
            path = skia.Path(); path.addPoly([ZBL, (ZBL[0] + 16 * U, ZBL[1]), (ZTL[0] + 16 * U, ZTL[1]), ZTL], True)
            c.drawPath(path, M.paint(E.COR, q * apaga, stroke=9))
        if t >= e5:
            # embaixo: B de um continua no b do outro
            yb = ZBL[1] + 150
            x0, x1, x2 = ZBL[0], ZBR[0], ZBL[0] + 16 * U
            q = ep(t, e5, 0.5)
            E.chave(c, x0, x1, yb - 30, E.COR, q, 26)
            E.chave(c, x1, x2, yb - 30, TINTA2, q, 26)
            E.foco(c, t, e5, 0.4, lambda a: (centro(c, "B", (x0 + x1) / 2, yb + 50, 60, "g", COR, a), centro(c, "b", (x1 + x2) / 2, yb + 50, 60, "g", TINTA2, a)))
            E.foco(c, t, e5 + 0.5, 0.4, lambda a: centro(c, "base = B + b", (x0 + x2) / 2, yb + 150, 64, "g", COR, a))
        if t < C["s06"]:
            E.frase(c, t, a5, ps("pegue uma", "i", 66) + [("cópia,", "g", 68, TINTA2)], 1400, 220, "left", 0.1)
            E.foco(c, t, b5, 0.4, lambda a: E.escreve(c, "gire e encoste", 1400, 310, 60, "i", TINTA, a))
            E.frase(c, t, d5, [("paralelogramo", "g", 66, COR)], 1400, 400, "left")
            return
        E.foco(c, t, a6, 0.5, lambda a: E.escreve(c, "(B + b) · h", 1340, 240, 76, "g", TINTA, a))
        E.frase(c, t, b6, ps("cada um:", "i", 62) + [("a metade", "g", 66, COR)], 1340, 340, "left", 0.1)
        fcen(c, t, c6, "A = f{(B + b) · h}{2}", 1580, 560, 96, COR)
    fase(c, t, C["s04"], C["s07"] - 0.1, ate_s06)
    if t < C["s07"] - 0.1:
        return
    # as contas, com o trapézio parado à esquerda
    trap(c, t, C["s07"] - 0.1, C["s07"], C["s07"] + 0.2, C["s07"] + 0.4)

    def sete():
        fcen(c, t, C["s07"] + 0.3, "A = f{(B + b) · h}{2}", 1360, 300, 76, COR)
        fcen(c, t, a7, "10 + 6 = 16", 1360, 480, 88)
        fcen(c, t, b7, "16 × 4 = 64", 1360, 620, 88)
        fcen(c, t, c7, "64 ÷ 2 = 32", 1360, 760, 88)
        bola_res(c, t, c7 + 1.0, "32", 1360, 920, 90, 80)
    fase(c, t, C["s07"], C["s08"] - 0.1, sete)
    if t < C["s08"]:
        return
    # outro caminho: a diagonal corta em dois triângulos de altura 4
    E.frase(c, t, C["s08"] + 0.2, ps("por outro", "i", 70) + [("caminho", "g", 74, COR)], 1000, 220, "left", 0.1)
    q = ep(t, a8, 0.6)
    if q > 0:
        lado_cor(c, ZBL, ZTR, TINTA, q, 6)
        c.drawPath(_path([ZBL, ZBR, ZTR]), M.paint(E.COR, 0.3 * ep(t, b8, 0.5)))
        c.drawPath(_path([ZBL, ZTR, ZTL]), M.paint(TINTA2, 0.3 * ep(t, c8, 0.5)))
    fcen(c, t, b8, "f{10 × 4}{2} = 20", 1300, 420, 80, COR)
    fcen(c, t, c8, "f{6 × 4}{2} = 12", 1300, 640, 80, TINTA2)
    fcen(c, t, d8, "20 + 12 = 32", 1300, 840, 88)
    E.foco(c, t, d8 + 1.0, 0.4, lambda a: E.selo(c, 1660, 815, 40, True, a))


def _path(pts):
    p = skia.Path(); p.addPoly([tuple(q) for q in pts], True); return p


# ---------------- losango ----------------
LC, LD, Ld = (560, 600), 8 * U, 6 * U
LE, LT, LR, LB = (LC[0] - LD / 2, LC[1]), (LC[0], LC[1] - Ld / 2), (LC[0] + LD / 2, LC[1]), (LC[0], LC[1] + Ld / 2)
LOS = [LE, LT, LR, LB]


def b_losango(c, t, C, b):
    a9, b9 = C["s09.a"], C["s09.b"]
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, C["s09"] + 0.1, ps("o", "i", 80) + [("losango", "g", 84, COR)], XE, 210, "left", 0.1)
    E.poligono(c, t, C["s09"] + 0.2, LOS, preenche=0.0, d=0.7)
    lado_cor(c, LE, LR, E.COR, ep(t, a9, 0.6), 7)
    lado_cor(c, LT, LB, TINTA2, ep(t, a9 + 0.8, 0.6), 7)
    E.angulo(c, t, a9 + 1.2, LC, LR, LT, r=34)
    rotD = "8" if t >= b1 else "D"
    rotd = "6" if t >= b1 else "d"
    E.foco(c, t, a9 + 0.4, 0.4, lambda a: centro(c, rotD, LC[0] + LD / 4, LC[1] - 18, 56, "g", COR, a))
    E.foco(c, t, a9 + 1.0, 0.4, lambda a: E.escreve(c, rotd, LC[0] + 16, LC[1] + Ld / 4 + 20, 56, "g", TINTA2, a))
    # 4 triângulos dentro
    dentro = [(LE, LT), (LT, LR), (LR, LB), (LB, LE)]
    for k, (P, Q) in enumerate(dentro):
        q = ep(t, b9 + 0.25 * k, 0.4)
        if q > 0:
            c.drawPath(_path([LC, P, Q]), M.paint(E.COR, 0.38 * q))
    # o retângulo das diagonais e os 4 de fora
    X0, Y0 = LE[0], LT[1]
    if t >= a0:
        c.drawRect(skia.Rect.MakeXYWH(X0, Y0, LD, Ld), M.paint(TINTA, ep(t, a0, 0.5), stroke=5))
    fora = [[LE, LT, (X0, Y0)], [LT, LR, (X0 + LD, Y0)], [LR, LB, (X0 + LD, Y0 + Ld)], [LB, LE, (X0, Y0 + Ld)]]
    for k, pts in enumerate(fora):
        q = ep(t, c0 + 0.25 * k, 0.4)
        if q > 0:
            c.drawPath(_path(pts), M.paint(CINZA, 0.4 * q))
    if t < C["s11"]:
        E.foco(c, t, a9, 0.4, lambda a: E.escreve(c, "D = diagonal maior", 1000, 360, 60, "g", COR, a))
        E.foco(c, t, a9 + 0.8, 0.4, lambda a: E.escreve(c, "d = diagonal menor", 1000, 450, 60, "g", TINTA2, a))
        E.foco(c, t, b9, 0.4, lambda a: E.escreve(c, "4 triângulos iguais", 1000, 560, 60, "i", TINTA, a * (1 - ep(t, a0, 0.3))))
        E.foco(c, t, a0, 0.4, lambda a: E.escreve(c, "retângulo D × d", 1000, 560, 60, "i", TINTA, a))
        E.foco(c, t, b0, 0.4, lambda a: E.escreve(c, "8 triângulos:", 1000, 670, 60, "g", TINTA, a))
        E.foco(c, t, c0, 0.4, lambda a: E.escreve(c, "4 dentro, 4 fora", 1000, 760, 60, "i", TINTA, a))
        E.frase(c, t, d0, ps("losango =", "i", 66) + [("metade do retângulo", "g", 66, COR)], 1000, 900, "left", 0.1)
        return
    fcen(c, t, a1, "A = f{D · d}{2}", 1360, 380, 110, COR)
    fcen(c, t, c1, "8 × 6 = 48", 1360, 620, 92)
    fcen(c, t, d1, "48 ÷ 2 = 24", 1360, 780, 92)
    bola_res(c, t, d1 + 1.0, "24", 1360, 940, 85, 80)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    E.frase(c, t, C["s12"] + 0.2, ps("o erro:", "i", 70) + [("esquecer o ÷ 2", "g", 70, ERRADO)], W / 2, 180, "center", 0.1)
    trap(c, t, C["s12"] + 0.3, C["s12"] + 0.6, C["s12"] + 0.8, C["s12"] + 1.0)
    E.foco(c, t, b2, 0.5, lambda a: E.escreve(c, "(10 + 6) × 4 = 64", 1000, 400, 76, "g", ERRADO, a))
    if t >= c2:
        q = ep(t, c2, 0.5)
        c.drawRect(skia.Rect.MakeXYWH(ZBL[0], ZTL[1], 10 * U, 4 * U), M.paint(CERTO, 0.12 * q))
        c.drawRect(skia.Rect.MakeXYWH(ZBL[0], ZTL[1], 10 * U, 4 * U), M.paint(CERTO, q, stroke=6))
    E.foco(c, t, c2 + 0.3, 0.5, lambda a: E.escreve(c, "retângulo 10 × 4 = 40", 1000, 560, 70, "g", CERTO, a))
    E.foco(c, t, c2 + 0.3, 0.4, lambda a: E.escreve(c, "cobre tudo", 1000, 640, 56, "i", TINTA2, a))
    if t >= d2:
        E.risco(c, 990, 420, 1720, 340, t, d2, largura=12)
    E.foco(c, t, d2 + 0.3, 0.5, lambda a: E.pilula(c, "a área não passa de 40", 1340, 790, 60, "g", fundo=ERRADO, a=a, cor=BR))
    E.foco(c, t, d2 + 0.9, 0.4, lambda a: E.escreve(c, "a certa: 32", 1000, 950, 70, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]

    def um():
        E.frase(c, t, a3, ps("o atalho:", "i", 80, CLARO) + [("a base do meio", "g", 86, BR)], W / 2, 210, "center", 0.1)
        trap(c, t, C["s13"] + 0.2, C["s13"] + 0.4, C["s13"] + 0.6, None, alfa=0.25, escuro=True)
        E._altura(c, t, C["s13"] + 0.8, ZTL, ZPE, "", 1, 56)
        E.foco(c, t, C["s13"] + 1.2, 0.4, lambda q: E.escreve(c, "4", ZTL[0] + 18, ZPE[1] - 22, 52, "g", BR, q))
        # a base do meio, na metade da altura
        ym = (ZTL[1] + ZBL[1]) / 2
        xa, xb = (ZBL[0] + ZTL[0]) / 2, (ZBR[0] + ZTR[0]) / 2
        lado_cor(c, (xa, ym), (xb, ym), BR, ep(t, b3, 0.6), 8)
        E.foco(c, t, b3 + 0.4, 0.4, lambda a: centro(c, "8", (xa + xb) / 2, ym - 22, 60, "g", BR, a))
        fcen(c, t, b3, "f{10 + 6}{2} = 8", 1320, 440, 88, BR)
        fcen(c, t, c3, "8 × 4 = 32", 1320, 640, 100, BR)
        # as pontas que sobram embaixo giram em volta do meio do lado e tapam as que faltam em cima
        gira = 180 * ease_io(prog(t, d3, 1.4))
        if t >= d3:
            for ponta, piv in (([ZBL, (xa, ZBL[1]), (xa, ym)], (xa, ym)), ([ZBR, (xb, ZBR[1]), (xb, ym)], (xb, ym))):
                peca(c, mexe(ponta, 0, 0, gira, piv), CLARO, 0.85, ep(t, d3, 0.3), BR, 3)
            if t >= d3 + 1.4:
                q = ep(t, d3 + 1.4, 0.4)
                c.drawRect(skia.Rect.MakeXYWH(xa, ZTL[1], xb - xa, ZBL[1] - ZTL[1]), M.paint(BR, q, stroke=7))
        E.frase(c, t, d3 + 0.4, ps("vale um", "i", 66, CLARO) + [("retângulo 8 × 4", "g", 70, BR)], 1000, 860, "left", 0.1)
    E.saida(c, t, C["s14"] - 0.1, um)
    if t < C["s14"]:
        return
    fcen(c, t, a4, "f{B + b}{2} = média das bases", W / 2, 300, 84, BR)
    E.foco(c, t, a4 + 1.5, 0.4, lambda a: centro(c, "a mesma conta, com a divisão antes", W / 2, 430, 56, "i", CLARO, a))
    E.frase(c, t, b4, ps("soma das bases", "i", 66, CLARO) + [("ímpar", "g", 70, BR)] + ps("e altura", "i", 66, CLARO) + [("par?", "g", 70, BR)],
            W / 2, 580, "center", 0.1)
    E.foco(c, t, b4 + 1.6, 0.4, lambda a: centro(c, "B = 7, b = 4, h = 6", W / 2, 690, 64, "g", CLARO, a))
    E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "tire a metade da altura", W / 2, 810, 60, "g", a=a, cor=E.SOBRE))
    fcen(c, t, c4 + 1.2, "(7 + 4) × 3 = 11 × 3 = 33", W / 2, 960, 84, BR)


# ---------------- questão ----------------
QZ = (1120, 300, 16)  # terreno: canto de cima à esquerda da base maior, px por metro
QL = (1330, 820, 5)   # pipa: centro, px por cm


def terreno_q(c, t, t0, tb, th, rot_h="12 m", a=1.0):
    x, y, k = QZ
    B, b, h = 25 * k, 15 * k, 12 * k
    pts = [(x, y + h), (x + B, y + h), (x + (B + b) / 2, y), (x + (B - b) / 2, y)]
    E.foco(c, t, t0, 0.5, lambda q: peca(c, pts, "#3FA45B", 0.18, q * a))
    E.foco(c, t, t0 + 0.2, 0.4, lambda q: centro(c, "25 m", x + B / 2, y + h + 64, 50, "g", COR, q * a))
    E.foco(c, t, t0 + 0.4, 0.4, lambda q: centro(c, "15 m", x + B / 2, y - 22, 50, "g", TINTA2, q * a))
    if t >= th:
        E._altura(c, t, th, pts[3], (pts[3][0], y + h), "", 1, 50)
        E.foco(c, t, th + 0.3, 0.4, lambda q: E.escreve(c, rot_h, pts[3][0] + 14, y + h / 2 + 18, 46, "g", COR, q * a))


def pipa(c, t, t0, td, a=1.0, cx=None, cy=None):
    x, y, k = QL
    x, y = cx or x, cy or y
    D, d = 50 * k, 30 * k
    pts = [(x - d / 2, y), (x, y - D * 0.3), (x + d / 2, y), (x, y + D * 0.7)]  # pipa em pé: a diagonal maior na vertical
    E.foco(c, t, t0, 0.5, lambda q: peca(c, pts, "#E2A23B", 0.5, q * a))
    if t >= td:
        q = ep(t, td, 0.5) * a
        M.line(c, pts[1][0], pts[1][1], pts[3][0], pts[3][1], COR, q, 5)
        M.line(c, pts[0][0], pts[0][1], pts[2][0], pts[2][1], TINTA2, q, 5)
        E.escreve(c, "50 cm", x + d / 2 + 4, y + D * 0.42, 46, "g", COR, q)
        centro(c, "30 cm", x - d / 2 - 90, y + 16, 46, "g", TINTA2, q)


def b_questao(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    E.frase(c, t, C["s15"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s15"] + 1.2, ps("terreno em", "i", 66) + [("trapézio", "g", 68, COR)], XE, 330, passo=0.1)
    E.foco(c, t, a5, 0.5, lambda a: E.escreve(c, "bases 25 m e 15 m", XE, 430, 64, "g", TINTA, a))
    E.foco(c, t, b5, 0.5, lambda a: E.escreve(c, "12 m entre elas", XE, 520, 64, "g", TINTA, a))
    E.frase(c, t, c5, ps("qual é a", "i", 66) + [("área?", "g", 70, COR)], XE, 620, passo=0.1)
    E.frase(c, t, lerp(c5, d5, 0.4), ps("pipa em", "i", 66) + [("losango", "g", 68, COR)], XE, 760, passo=0.1)
    E.foco(c, t, d5, 0.5, lambda a: E.escreve(c, "diagonais 50 cm e 30 cm", XE, 860, 60, "g", TINTA, a))
    E.frase(c, t, e5, ps("quanto", "i", 66) + [("papel?", "g", 70, COR)], XE, 960, passo=0.1)
    terreno_q(c, t, a5, a5, b5)
    pipa(c, t, lerp(c5, d5, 0.4), d5)
    E.relogio(c, t, C["s16.a"], 1700, 720, 110)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]
    a8, b8 = C["s18.a"], C["s18.b"]

    def um():
        terreno_q(c, t, C["s17"] + 0.1, C["s17"] + 0.1, a7)
        E.foco(c, t, a7 + 0.4, 0.4, lambda a: E.escreve(c, "12 m = a altura", 160, 460, 64, "g", COR, a))
        fcen(c, t, b7, "f{25 + 15}{2} = 20", 560, 680, 88)
        E.foco(c, t, b7 + 0.4, 0.4, lambda a: centro(c, "base do meio", 560, 820, 50, "i", TINTA2, a))
        fcen(c, t, c7, "20 × 12 = 240", 1360, 680, 92)
        bola_res(c, t, c7 + 1.0, "240 m²", 1360, 880, 125, 52)
    E.saida(c, t, C["s18"] - 0.1, um)
    if t < C["s18"]:
        return
    pipa(c, t, C["s18"] + 0.1, C["s18"] + 0.3, cx=520, cy=420)
    fcen(c, t, a8, "50 × 30 = 1.500", 1300, 420, 92)
    fcen(c, t, b8, "1.500 ÷ 2 = 750", 1300, 600, 92)
    bola_res(c, t, b8 + 1.0, "750 cm²", 1300, 800, 130, 50)
    E.foco(c, t, b8 + 1.4, 0.4, lambda a: E.escreve(c, "de papel", 1460, 820, 56, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s19.a", "trapézio:", "A = f{(B + b) · h}{2}"), ("s19.b", "losango:", "A = f{D · d}{2}"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 460 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 360, y - 30, 56, a=a), centro(c, str(i + 1), 360, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 84), 460, y, "left", 0.1)
            E.formula_em(c, t, C[k] + 0.4, l2, 900, y - 20, 84, "g", COR)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a0, [("equilátero", "g", 120, COR)], XE, 420, passo=0.12)
    E.frase(c, t, b0, ps("e", "i", 100) + [("hexágono", "g", 120, COR)], XE, 580, passo=0.12)
    E.regular(c, t, a0, 3, 1250, 380, 150, preenche=0.12, d=0.7, iguais=[1, 1, 1])
    E.regular(c, t, b0, 6, 1640, 360, 150, preenche=0.12, d=0.7)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1580, p), lerp(970, 785, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, trapezio=b_trapezio, losango=b_losango, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
