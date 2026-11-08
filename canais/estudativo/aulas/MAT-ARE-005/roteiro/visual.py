"""Visual — Estudativo · MAT-ARE-005: área do triângulo equilátero (ℓ²√3/4) e do hexágono regular (6 equiláteros).
Mesma linguagem da trilha (docstring de MAT-ARE-001) e da geometria plana (MAT-ANG-001, MAT-ANG-017 para √3):
- o equilátero com os tracinhos de lados iguais e a altura tracejada com o quadradinho do reto;
- o hexágono ligado ao centro: os seis triângulos acendem um a um, alternando a cor da matéria e um tom mais claro;
- ângulos com E.angulo (60° no centro; 120° no canto partido em 60° + 60°).
Raiz na tela com E.formula ("r{3}"); a aproximação √3 ≈ 1,7 é a de MAT-ANG-017.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-005_area_equilatero_hexagono.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("equilatero", "hexagono", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 6 * 3 == 18 and 18 // 2 == 9 and 6 ** 2 // 4 == 9 and 360 // 6 == 60 and 120 // 2 == 60 and 2 ** 2 // 4 == 1
assert abs(6 * 1.7 - 10.2) < 1e-9 and (6 // 2) ** 2 == 9 and (8 // 2) ** 2 == 16 and 5 ** 2 == 25 and (10 // 2) ** 2 == 25
assert 6 * 25 == 150 and abs(150 * 1.7 - 255) < 1e-9 and 18 * 1.7 > 30


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


# ---------------- peças desta aula ----------------
def _path(pts):
    p = skia.Path(); p.addPoly([tuple(q) for q in pts], True); return p


def hexa(cx, cy, r):
    """vértices do hexágono regular como em E.regular: 0 = embaixo à direita, 1 = embaixo à esquerda, depois no sentido horário da tela"""
    return [(cx + r * math.cos(math.radians(60 + 60 * k)), cy + r * math.sin(math.radians(60 + 60 * k))) for k in range(6)]


def fatias(c, t, ti, cx, cy, r, a=1.0, cores=None, alfa=0.42):
    """os seis triângulos do centro, acendendo um a um (ti = instante de cada um, ou do primeiro)"""
    V = hexa(cx, cy, r)
    for k in range(6):
        t_ = ti[k] if isinstance(ti, (list, tuple)) else ti + 0.25 * k
        q = ep(t, t_, 0.4) * a
        if q > 0:
            cor = (cores[k] if cores else (E.COR if k % 2 == 0 else CLARO))
            c.drawPath(_path([(cx, cy), V[k], V[(k + 1) % 6]]), M.paint(cor, alfa * q))


def raios(c, t, t0, cx, cy, r, a=1.0, cor=None, d=0.25):
    V = hexa(cx, cy, r)
    for k in range(6):
        q = ep(t, t0 + d * k, 0.4) * a
        if q > 0:
            M.line(c, cx, cy, lerp(cx, V[k][0], ease_io(q)), lerp(cy, V[k][1], ease_io(q)), cor or TINTA, 1.0, 5)


# o equilátero de lado 6 (80 px por unidade)
EA, EB = (220, 820), (700, 820)
EC = (460, 820 - 480 * math.sqrt(3) / 2)
EP = (460, 820)


def equi(c, t, t0, rot="6", tl=None, alfa=0.12, a=1.0):
    if a <= 0:
        return
    if a < 1:
        c.saveLayer(None, M.paint("#000000", a))
    E.triangulo(c, t, t0, EA, EB, EC, vertices=None, iguais=[1, 1, 1], lados=[rot, None, None], tl=tl, preenche=alfa, d=0.7, size=60)
    if a < 1:
        c.restore()


# ---------------- gancho ----------------
GX, GY, GR = 560, 560, 300


def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.regular(c, t, ka, 6, GX, GY, GR, lado="2", preenche=0.06, d=0.8, size=60)
        E.frase(c, t, ka + 0.6, ps("hexágono regular de", "i", 66) + [("lado 2", "g", 70, COR)], 1000, 300, "left", 0.1)
        E.frase(c, t, lerp(ka, kb, 0.4), ps("qual é a", "i", 76) + [("área?", "g", 84, COR)], 1000, 430, "left", 0.1)
        raios(c, t, kb, GX, GY, GR)
        fatias(c, t, kb + 0.4, GX, GY, GR)
        E.foco(c, t, kb + 0.4, 0.4, lambda a: E.escreve(c, "6 triângulos", 1000, 580, 76, "g", TINTA, a))
        bola_res(c, t, kc, "6r{3}", 1300, 800, 130, 90)
        E.foco(c, t, kc + 0.6, 0.4, lambda a: E.escreve(c, "≈ 10", 1460, 830, 76, "g", TINTA2, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 290, passo=0.12)
        E.frase(c, t, ta + 0.9, ps("a área do", "i", 78) + [("equilátero", "g", 96, COR)], XE, 440, passo=0.12)
        E.frase(c, t, ta + 1.6, ps("e do", "i", 78) + [("hexágono", "g", 96, COR)], XE, 570, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("de qualquer", "i", 70) + [("tamanho", "g", 72)], XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "área do triângulo", "f{b · h}{2}"), ("s03.c", "altura do equilátero", "h = f{ℓr{3}}{2}"),
             ("s03.d", "hexágono regular:", "lados iguais, 120° em cada canto"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 200, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 76)
        if i < 2:
            E.formula_em(c, t, C[k] + 0.4, l2, x + 520, y + 120, 64, "g", COR)
        else:
            E.foco(c, t, C[k] + 0.4, 0.5, lambda a, l2=l2, y=y: E.escreve(c, l2, x + 44, y + 160, 52, "g", COR, a))
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 590, q1), 840, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.7), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1010, "left", 0.12)


# ---------------- equilátero ----------------
def b_equilatero(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    geral = t >= a5  # do s05 em diante, o lado vira ℓ
    E.frase(c, t, C["s04"] + 0.1, ps("o", "i", 80) + [("equilátero", "g", 84, COR)], XE, 210, "left", 0.1)
    if not geral:
        equi(c, t, C["s04"] + 0.2, "6", [a4, a4, a4])
    else:
        equi(c, t, C["s04"] + 0.2, None)
        E.foco(c, t, a5, 0.4, lambda a: centro(c, "ℓ", (EA[0] + EB[0]) / 2, EA[1] + 76, 64, "g", COR, a))
    E._altura(c, t, b4, EC, EP, "", 1, 56)
    rot_h = "3r{3}" if not geral else ("f{ℓr{3}}{2}" if t >= b5 else "")
    if rot_h:
        E.foco(c, t, b4 + 0.3 if not geral else b5, 0.4, lambda a: E.formula(c, rot_h, EP[0] + 24, EP[1] - 90, 54, "g", COR, a))
    X = 1340
    if t < C["s05"]:
        fcen(c, t, a4, "base 6", X, 330, 76, TINTA2)
        fcen(c, t, b4, "altura 3r{3}", X, 450, 76, TINTA2)
        fcen(c, t, c4, "6 × 3r{3} = 18r{3}", X, 630, 84)
        fcen(c, t, d4, "f{18r{3}}{2} = 9r{3}", X, 830, 84, COR)
        return
    if t < C["s06"]:
        def cinco():
            fcen(c, t, c5, "ℓ · f{ℓr{3}}{2} = f{ℓ²r{3}}{2}", X, 420, 84)
            fcen(c, t, d5, "f{ℓ²r{3}}{2} ÷ 2 = f{ℓ²r{3}}{4}", X, 700, 84, COR)
            E.foco(c, t, c5 + 0.6, 0.4, lambda a: centro(c, "base × altura", X, 560, 50, "i", TINTA2, a))
            E.foco(c, t, d5 + 0.6, 0.4, lambda a: centro(c, "a metade", X, 840, 50, "i", TINTA2, a))
        E.saida(c, t, C["s06"] - 0.1, cinco)
        return
    fcen(c, t, a6, "A = f{ℓ²r{3}}{4}", X, 360, 120, COR)
    E.frase(c, t, b6, [("ℓ", "g", 66, COR)] + ps("= lado", "i", 62), X, 530, "center", 0.1)
    fcen(c, t, c6, "6² = 36", X - 220, 700, 84)
    fcen(c, t, d6, "36 ÷ 4 = 9", X + 220, 700, 84)
    bola_res(c, t, e6, "9r{3}", X, 880, 110, 84)


# ---------------- hexágono: seis equiláteros ----------------
HX, HY, HR = 560, 580, 300


def b_hexagono(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    V = hexa(HX, HY, HR)
    E.frase(c, t, C["s07"] + 0.1, ps("o", "i", 80) + [("hexágono regular", "g", 84, COR)], XE, 210, "left", 0.1)
    E.regular(c, t, C["s07"] + 0.2, 6, HX, HY, HR, preenche=0.0, d=0.8, size=58)
    E.foco(c, t, b9, 0.4, lambda a: centro(c, "2", HX, V[0][1] + 76, 60, "g", COR, a))
    raios(c, t, a7, HX, HY, HR)
    destaca = ep(t, c8, 0.5)  # o triângulo de baixo fica forte; os outros clareiam
    fatias(c, t, b7, HX, HY, HR, cores=[E.COR] + [CLARO if k % 2 else E.COR for k in range(1, 6)], alfa=0.42)
    if destaca > 0 and t < C["s09"]:
        c.drawPath(_path([(HX, HY), V[0], V[1]]), M.paint(E.COR, 0.5 * destaca))
    if t < C["s09"]:
        # 60° no centro
        E.angulo(c, t, c7, (HX, HY), V[0], V[1], "60°", r=70, size=46)
        E.foco(c, t, c7, 0.4, lambda a: E.formula(c, "360° ÷ 6 = 60°", 1000, 360, 70, "g", TINTA, a))
        # 120° no canto de baixo à esquerda, partido em 60° + 60°
        if t < b8:
            E.angulo(c, t, a8, V[1], V[0], V[2], "120°", r=60, size=46, dentro=True, cor=TINTA2)
        else:
            E.angulo(c, t, b8, V[1], V[0], (HX, HY), "60°", r=64, size=40)
            E.angulo(c, t, b8 + 0.3, V[1], (HX, HY), V[2], "60°", r=64, size=40, cor=TINTA2)
        E.angulo(c, t, c8 + 0.3, V[0], (HX, HY), V[1], "60°", r=64, size=40)
        E.foco(c, t, a8, 0.4, lambda a: E.formula(c, "canto: 120°", 1000, 480, 64, "g", TINTA2, a))
        E.foco(c, t, b8, 0.4, lambda a: E.formula(c, "120° ÷ 2 = 60°", 1000, 580, 64, "g", TINTA, a))
        E.frase(c, t, c8, ps("três ângulos de", "i", 62) + [("60°", "g", 64, COR)], 1000, 720, "left", 0.1)
        E.frase(c, t, d8, ps("cada um é", "i", 66) + [("equilátero", "g", 72, COR)], 1000, 840, "left", 0.1)
        E.foco(c, t, d8 + 0.6, 0.4, lambda a: E.escreve(c, "lado = lado do hexágono", 1000, 930, 52, "i", TINTA2, a))
        return
    X = 1340
    fcen(c, t, a9, "A = 6 × triângulo", X, 300, 76, COR)
    fcen(c, t, b9, "f{2²r{3}}{4} = f{4r{3}}{4} = r{3}", X, 470, 76)
    E.foco(c, t, c9, 0.4, lambda a: (centro(c, "cada triângulo:", X - 70, 590, 56, "i", TINTA2, a), E.formula(c, "r{3}", X + 140, 590, 60, "g", COR, a)))
    fcen(c, t, d9, "6 × r{3} = 6r{3}", X, 720, 84, COR)
    fcen(c, t, e9, "6 × 1,7 = 10,2", X, 870, 76)
    E.foco(c, t, e9 - 0.6, 0.4, lambda a: E.formula(c, "r{3} ≈ 1,7", 1000, 990, 52, "g", TINTA2, a))
    bola_res(c, t, e9 + 1.0, "≈ 10,2", 1700, 990, 80, 44)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"] + 0.2, ps("o erro:", "i", 70) + [("dividir por 2 em vez de 4", "g", 70, ERRADO)], W / 2, 180, "center", 0.1)
    equi(c, t, C["s10"] + 0.3, "6", [C["s10"] + 0.6] * 3, alfa=0.25)
    E._altura(c, t, C["s10"] + 0.8, EC, EP, "", 1, 56)
    E.foco(c, t, C["s10"] + 1.0, 0.4, lambda a: E.formula(c, "3r{3}", EP[0] + 24, EP[1] - 90, 54, "g", COR, a))
    E.foco(c, t, b0, 0.5, lambda a: E.formula(c, "f{6²r{3}}{2} = 18r{3} ≈ 30,6", 1000, 400, 70, "g", ERRADO, a))
    E.foco(c, t, b0 + 0.6, 0.4, lambda a: E.escreve(c, "mais de 30", 1000, 520, 56, "i", ERRADO, a))
    if t >= c0:
        q = ep(t, c0, 0.5)
        x0, y0 = EA[0], EC[1]
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, EB[0] - EA[0], EA[1] - y0), M.paint(ERRADO, 0.08 * q))
        c.drawRect(skia.Rect.MakeXYWH(x0, y0, EB[0] - EA[0], EA[1] - y0), M.paint(ERRADO, q, stroke=6))
    E.foco(c, t, c0 + 0.2, 0.5, lambda a: E.formula(c, "retângulo: 6 × 3r{3} = 18r{3}", 1000, 660, 62, "g", ERRADO, a))
    E.frase(c, t, d0, ps("o triângulo é", "i", 66) + [("a metade:", "g", 70, CERTO)], 1000, 820, "left", 0.1)
    E.foco(c, t, d0 + 0.8, 0.5, lambda a: E.formula(c, "9r{3}", 1700, 820, 80, "g", CERTO, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a1, ps("lado par:", "i", 80, CLARO) + [("use a metade do lado", "g", 84, BR)], W / 2, 210, "center", 0.1)
        fcen(c, t, b1, "f{ℓ²}{4} = (f{ℓ}{2})²", W / 2, 420, 110, BR)
        fcen(c, t, c1, "lado 6:  3² = 9  →  9r{3}", W / 2, 660, 84, CLARO)
        fcen(c, t, d1, "lado 8:  4² = 16  →  16r{3}", W / 2, 840, 84, CLARO)
    E.saida(c, t, C["s12"] - 0.1, um)
    if t < C["s12"]:
        return
    fcen(c, t, a2, "4 = 2²", W / 2, 260, 110, BR)
    E.foco(c, t, a2 + 0.8, 0.4, lambda a: centro(c, "dividir o quadrado por 4 = elevar a metade ao quadrado", W / 2, 370, 50, "i", CLARO, a))
    E.frase(c, t, b2, ps("lado", "i", 76, CLARO) + [("ímpar?", "g", 80, BR)], W / 2, 540, "center", 0.1)
    fcen(c, t, c2, "lado 5:  f{25r{3}}{4}", W / 2, 720, 92, CLARO)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "deixe o 4 embaixo", W / 2, 920, 64, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
LR_ = 120  # ladrilho: 10 cm de lado (12 px por cm)


def piso_hex(c, t, t0, cx, cy, r, a=1.0, destaque=True):
    """um pedaço de piso de ladrilhos hexagonais: o do meio e os vizinhos"""
    centros = [(cx, cy)] + [(cx + r * math.sqrt(3) * math.cos(math.radians(30 + 60 * k)), cy + r * math.sqrt(3) * math.sin(math.radians(30 + 60 * k))) for k in range(6)]
    for i, (x, y) in enumerate(centros):
        q = ep(t, t0 + 0.08 * i, 0.4) * a
        if q > 0:
            V = hexa(x, y, r)
            c.drawPath(_path(V), M.paint(E.COR if (i == 0 and destaque) else "#D8D6E8", (0.5 if i == 0 and destaque else 0.6) * q))
            pt = M.paint(TINTA, q, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
            c.drawPath(_path(V), pt)


def b_questao(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, lerp(C["s13"], a3, 0.5), ps("ladrilho em", "i", 64) + [("hexágono regular", "g", 64, COR)], XE, 360, passo=0.1)
    E.foco(c, t, a3, 0.5, lambda a: E.escreve(c, "lado 10 cm", XE, 470, 76, "g", TINTA, a))
    E.frase(c, t, b3, ps("qual é a", "i", 76) + [("área?", "g", 84, COR)], XE, 640, passo=0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.formula(c, "use r{3} = 1,7", XE, 800, 68, "g", TINTA2, a))
    cx, cy = 1420, 560
    V = hexa(cx, cy, LR_)

    def piso():
        piso_hex(c, t, a3 - 0.4, cx, cy, LR_)
        E.foco(c, t, a3 + 0.4, 0.4, lambda a: centro(c, "10 cm", (V[0][0] + V[1][0]) / 2, V[0][1] - 16, 40, "g", BR, a))
    E.saida(c, t, C["s14.a"] - 0.1, piso)  # na pausa, o relógio ocupa o lugar do piso
    E.relogio(c, t, C["s14.a"], 1450, 440, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    cx, cy, r = 480, 560, 280
    E.regular(c, t, C["s15"] + 0.1, 6, cx, cy, r, lado="10 cm", preenche=0.0, d=0.7, size=56)
    raios(c, t, a5, cx, cy, r, d=0.15)
    fatias(c, t, a5 + 0.3, cx, cy, r, alfa=0.35)
    X = 1300
    E.foco(c, t, a5, 0.4, lambda a: E.escreve(c, "6 equiláteros de lado 10", 960, 260, 60, "i", TINTA, a))
    fcen(c, t, b5, "10 ÷ 2 = 5,  5² = 25", X, 420, 80)
    fcen(c, t, c5, "cada um: 25r{3}", X, 560, 80, COR)
    fcen(c, t, a6, "6 × 25 = 150", X, 700, 80)
    fcen(c, t, b6, "150r{3} cm²", X, 830, 84, COR)
    fcen(c, t, c6, "150 × 1,7 = 255", X - 120, 970, 76)
    bola_res(c, t, c6 + 1.0, "255 cm²", 1720, 940, 115, 48)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s17.a", "equilátero:", "A = f{ℓ²r{3}}{4}"), ("s17.b", "hexágono:", "6 equiláteros"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 460 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 360, y - 30, 56, a=a), centro(c, str(i + 1), 360, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 84), 460, y, "left", 0.1)
            E.formula_em(c, t, C[k] + 0.4, l2, 920, y - 20 if i == 0 else y, 84, "g", COR)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a8, [("40 m de cerca:", "g", 90, COR)], XE, 390, passo=0.12)
    E.frase(c, t, a8 + 0.8, ps("qual retângulo guarda", "i", 70), XE, 500, passo=0.1)
    E.frase(c, t, a8 + 1.6, ps("a", "i", 70) + [("maior área?", "g", 76, COR)], XE, 600, passo=0.1)
    P = E.plano(c, t, b8, 1140, 220, 600, 380, 0, 20, 0, 110, passo=5, passo_y=50, rotulos=False, nomes=("x", "A"))
    E.curva(c, t, b8 + 0.4, P, lambda x: x * (20 - x), 0, 20, d=1.0)
    E.ponto(c, t, b8 + 1.4, P, 10, 100, "vértice", lado=(1, -1))
    E.foco(c, t, c8, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c8 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1580, p), lerp(970, 785, p), ep(t, c8 + 0.2, 0.4))
    E.frase(c, t, d8, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, equilatero=b_equilatero, hexagono=b_hexagono, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
