"""Visual — Estudativo · MAT-ARE-003: área do paralelogramo (recorta e vira retângulo) e do triângulo (metade do paralelogramo).
Mesma linguagem da trilha (docstring de MAT-ARE-001). Peças locais novas, que as próximas aulas copiam:
- peca(): um pedaço de figura (polígono com miolo e contorno) que pode andar (dx, dy) e girar em volta de um ponto;
- fantasma(): o contorno tracejado que fica no lugar de onde o pedaço saiu (como o voa() de MAT-ANG-002);
- o RECORTE: o pedaço da vez fica cheio da cor da matéria, desliza em ease_io e assenta no destino; a cópia girada fica em cinza.
A altura é sempre tracejada com o quadradinho do ângulo reto (E._altura); lado inclinado usado no lugar dela = vermelho.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-003_area_paralelogramo_triangulo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("paralelogramo", "triangulo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 10 * 6 == 60 and 60 // 2 == 30 and 8 * 4 == 32 and 3 ** 2 + 4 ** 2 == 5 ** 2 and 6 * 8 // 2 == 24 and 8 * 5 == 40
assert 10 // 2 * 6 == 30 and 7 * 5 == 35 and 35 / 2 == 17.5 and 30 // 2 == 15 and 15 * 45 == 675 and 675 * 20 == 13500
assert 13500 / 10000 == 1.35


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


# ---------------- peças desta aula: recorte que desliza ----------------
def mexe(pts, dx=0.0, dy=0.0, ang=0.0, piv=None):
    """gira os pontos ang graus em volta de piv e depois anda (dx, dy)"""
    if ang and piv:
        co, si = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        pts = [(piv[0] + (x - piv[0]) * co - (y - piv[1]) * si, piv[1] + (x - piv[0]) * si + (y - piv[1]) * co) for x, y in pts]
    return [(x + dx, y + dy) for x, y in pts]


def peca(c, pts, cor=None, alfa=0.14, a=1.0, borda=None, largura=6):
    """pedaço de figura: miolo claro e contorno"""
    if a <= 0:
        return
    path = skia.Path()
    path.addPoly([tuple(p_) for p_ in pts], True)
    c.drawPath(path, M.paint(cor or E.COR, alfa * a))
    pt = M.paint(borda or TINTA, a, stroke=largura)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pt)


def fantasma(c, pts, a=1.0, cor=None):
    if a > 0:
        tracejado(c, list(pts) + [pts[0]], cor or TINTA2, 0.7 * a, 4)


def lado_cor(c, P0, P1, cor, q, largura=12):
    if q > 0:
        M.line(c, *P0, lerp(P0[0], P1[0], ease_io(q)), lerp(P0[1], P1[1], ease_io(q)), cor, 1.0, largura)


# o paralelogramo de base 8, lado 5 e altura 4 (80 px por cm, desloca 3)
PX, PY, PW_, PH, PD = 300, 400, 640, 320, 240
PBL, PBR, PTR, PTL = (PX, PY + PH), (PX + PW_, PY + PH), (PX + PW_ + PD, PY), (PX + PD, PY)
PE = (PX + PD, PY + PH)  # o pé da altura
TRI = [PBL, PE, PTL]  # o triângulo da ponta que é recortado
RESTO = [PE, PBR, PTR, PTL]


# ---------------- gancho ----------------
GX, GY, GW, GH = 230, 380, 600, 360  # retângulo 10 × 6 (60 px por unidade)
GA, GB, GC = (GX, GY + GH), (GX + GW, GY + GH), (GX + 240, GY)


def gancho_fig(c, t, t0, tr=None, tm=None, alfa_tri=0.14):
    """triângulo de base 10 e altura 6; tr = instante do retângulo em volta; tm = as sobras em cinza"""
    E.foco(c, t, t0, 0.5, lambda a: peca(c, [GA, GB, GC], alfa=alfa_tri, a=a))
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, "10", (GA[0] + GB[0]) / 2, GA[1] + 70, 56, "g", COR, a))
    E._altura(c, t, t0 + 0.6, GC, (GC[0], GA[1]), "6", 1, 56)
    if tr is not None and t >= tr:
        q = ep(t, tr, 0.6)
        c.drawRect(skia.Rect.MakeXYWH(GX, GY, GW, GH), M.paint(TINTA2, q, stroke=5))
    if tm is not None and t >= tm:
        q = ep(t, tm, 0.6)
        for pts in ([(GX, GY), GC, GA], [GC, (GX + GW, GY), GB]):
            path = skia.Path(); path.addPoly(pts, True)
            c.drawPath(path, M.paint(CINZA, 0.35 * q))
        c.drawPath(_tri_path([GA, GB, GC]), M.paint(E.COR, 0.45 * q))


def _tri_path(pts):
    p = skia.Path(); p.addPoly(pts, True); return p


def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        gancho_fig(c, t, ka, kc, kd)
        E.frase(c, t, ka + 0.6, ps("base 10, altura 6", "i", 70), 1000, 300, "left", 0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.escreve(c, "10 × 6 = 60?", 1000, 470, 96, "g", ERRADO, a))
        E.frase(c, t, kc, [("60", "g", 76, TINTA2)] + ps("é o retângulo inteiro", "i", 66), 1000, 600, "left", 0.1)
        fcen(c, t, kd + 0.3, "60 ÷ 2 = 30", 1300, 780, 96, COR)
        E.foco(c, t, kd, 0.4, lambda a: E.escreve(c, "o triângulo é a metade", 1000, 900, 60, "i", COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 290, passo=0.12)
        E.frase(c, t, ta + 0.9, ps("a área do", "i", 78) + [("paralelogramo", "g", 92, COR)], XE, 440, passo=0.12)
        E.frase(c, t, ta + 1.6, ps("e do", "i", 78) + [("triângulo", "g", 92, COR)], XE, 570, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("e de onde vem", "i", 70) + [("cada fórmula", "g", 72)], XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, 200, w, 196, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("área do retângulo", "i", 60)], x + 44, 284)
    E.foco(c, t, C["s03.b"] + 0.4, 0.5, lambda a: E.escreve(c, "A = b · h", x + 44, 360, 60, "g", COR, a))
    p = ep(t, C["s03.c"], 0.5)
    E.caixa_pontilhada(c, x, 450, w, 420, p, prog_=p)
    E.frase(c, t, C["s03.c"] + 0.1, [("altura: em ângulo reto", "i", 60)], x + 44, 534)
    # a altura do obtusângulo cai fora, no lado prolongado
    A, B, V = (x + 90, 800), (x + 380, 800), (x + 560, 600)
    E.triangulo(c, t, C["s03.c"] + 0.4, A, B, V, vertices=None, preenche=0.1, d=0.6)
    if t >= C["s03.c"] + 1.4:
        tracejado(c, [B, (V[0] + 40, 800)], TINTA2, ep(t, C["s03.c"] + 1.4, 0.4), 4)
    E._altura(c, t, C["s03.c"] + 1.6, V, (V[0], 800), "h", 1, 52)
    E.foco(c, t, C["s03.c"] + 2.2, 0.4, lambda a: E.escreve(c, "pode cair fora", x + 44, 640, 50, "i", COR, a))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(370, 840, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.7), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- paralelogramo: recorta e vira retângulo ----------------
def b_paralelogramo(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    if t < C["s05"]:
        E.frase(c, t, C["s04"] + 0.2, [("paralelogramo", "g", 84, COR)], XE, 210, "left")
        E.paralelogramo(c, t, C["s04"] + 0.3, PX, PY, PW_, PH, PD, iguais=[2, 1, 2, 1], tl=[a4 + 0.3] * 4, size=58)
        for (P0, P1) in ((PBL, PBR), (PTL, PTR)):
            lado_cor(c, P0, P1, E.COR, ep(t, a4, 0.6), 10)
        E.foco(c, t, a4, 0.4, lambda a: E.escreve(c, "lados opostos paralelos", 1260, 330, 54, "i", TINTA2, a))
        E.foco(c, t, b4, 0.4, lambda a: centro(c, "8 cm", (PBL[0] + PBR[0]) / 2, PBL[1] + 80, 58, "g", COR, a))
        E._altura(c, t, c4, PTL, PE, "", 1, 58)
        E.foco(c, t, d4, 0.4, lambda a: E.escreve(c, "4 cm", PE[0] + 22, (PTL[1] + PE[1]) / 2 + 20, 58, "g", COR, a))
        E.foco(c, t, c4 + 0.2, 0.4, lambda a: E.escreve(c, "altura: em ângulo reto", 1260, 430, 54, "g", COR, a))
        return
    # o recorte: o triângulo da ponta fica cheio, desliza 8 cm para a direita e assenta
    E.frase(c, t, C["s05"] + 0.1, [("recorte", "g", 84, COR)] + ps("e encaixe", "i", 80), XE, 210, "left", 0.1)
    anda = ease_io(prog(t, b5, 1.6))
    peca(c, RESTO)
    if t >= b5:
        fantasma(c, TRI, ep(t, b5, 0.3))
    cheio = ep(t, a5, 0.5)
    peca(c, mexe(TRI, PW_ * anda), alfa=0.14 + 0.5 * cheio)
    if t < b5 + 0.2:
        E._altura(c, t, C["s05"], PTL, PE, "", 1, 58)
    if a5 <= t < b5 + 1.6:  # a tesoura: o corte pela altura
        q = ep(t, a5, 0.4)
        tracejado(c, [PTL, PE], ERRADO, q, 6)
    E.foco(c, t, C["s05"], 0.4, lambda a: centro(c, "8 cm", (PBL[0] + PBR[0]) / 2 + PD * anda, PBL[1] + 80, 58, "g", COR, a))
    # virou retângulo 8 × 4
    if t >= c5:
        q = ep(t, c5, 0.5)
        c.drawRect(skia.Rect.MakeXYWH(PTL[0], PTL[1], PW_, PH), M.paint(E.COR, q, stroke=8))
        E.foco(c, t, c5, 0.4, lambda a: E.escreve(c, "4 cm", PTL[0] + 24, (PY + PH / 2) + 20, 58, "g", COR, a))
    if t >= d5:
        lado_cor(c, PBR, PTR, CERTO, ep(t, d5, 0.6), 12)
        E.foco(c, t, d5 + 0.3, 0.4, lambda a: E.escreve(c, "lados opostos iguais:", 1260, 380, 50, "i", TINTA, a))
        E.foco(c, t, d5 + 0.5, 0.4, lambda a: E.escreve(c, "encaixe perfeito", 1260, 450, 56, "g", CERTO, a))
    if C["s05"] <= t < C["s06"]:
        E.frase(c, t, c5, ps("virou", "i", 70) + [("retângulo", "g", 76, COR)], 1260, 660, "left", 0.1)
        E.frase(c, t, c5 + 0.6, [("8 × 4", "g", 76)], 1260, 770, "left", 0.1)
        return
    E.foco(c, t, a6, 0.5, lambda a: E.pilula(c, "A = b · h", 1520, 620, 76, "g", a=a, cor=E.SOBRE))
    fcen(c, t, b6, "8 × 4 = 32", 1520, 790, 96)
    bola_res(c, t, b6 + 1.0, "32 cm²", 1520, 950, 112, 48)
    # altura = distância entre os lados paralelos
    if t >= c6:
        q = ep(t, c6, 0.5)
        for xx in (PTL[0] + 160, PTL[0] + 400):
            M.arrow(c, xx, PY + 10, xx, PY + PH - 10, TINTA2, q, 4, 16, q)
            M.arrow(c, xx, PY + PH - 10, xx, PY + 10, TINTA2, q, 4, 16, q)
        E.foco(c, t, c6 + 0.2, 0.4, lambda a: centro(c, "distância entre os paralelos", (PTL[0] + PTR[0]) / 2, PY + PH + 160, 50, "i", TINTA, a))


# ---------------- triângulo: metade do paralelogramo ----------------
TA, TB, TC = (160, 760), (640, 760), (280, 440)  # base 480, altura 320
TM = ((TB[0] + TC[0]) / 2, (TB[1] + TC[1]) / 2)  # meio do lado BC: o giro de 180° em volta dele fecha o paralelogramo
TD = (TB[0] + TC[0] - TA[0], TB[1] + TC[1] - TA[1])


def b_triangulo(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9 = C["s09.a"], C["s09.b"]

    def sete_oito():
        E.frase(c, t, C["s07"] + 0.1, ps("o", "i", 80) + [("triângulo", "g", 84, COR)], XE, 210, "left", 0.1)
        tri = [TA, TB, TC]
        E.foco(c, t, a7, 0.5, lambda a: peca(c, tri, alfa=0.35, a=a))
        # a cópia: aparece ao lado, gira de cabeça para baixo e encosta no lado BC
        DX = 480
        gira = 180 * ease_io(prog(t, b7, 1.2))
        volta = DX * (1 - ease_io(prog(t, c7, 1.2)))
        copia = mexe(tri, volta, 0, gira, TM)
        apaga = 1 - 0.6 * ep(t, a8, 0.5)
        E.foco(c, t, a7 + 0.4, 0.5, lambda a: peca(c, copia, CINZA, 0.45, a * apaga))
        if t >= d7:
            q = ep(t, d7, 0.6)
            path = skia.Path(); path.addPoly([TA, TB, TD, TC], True)
            c.drawPath(path, M.paint(E.COR, q, stroke=9))
            E.foco(c, t, d7 + 0.2, 0.4, lambda a: centro(c, "paralelogramo", (TC[0] + TD[0]) / 2, TC[1] - 30, 54, "i", COR, a))
        E.foco(c, t, d7 + 0.3, 0.4, lambda a: centro(c, "b", (TA[0] + TB[0]) / 2, TA[1] + 70, 60, "g", COR, a))
        E._altura(c, t, d7 + 0.5, TC, (TC[0], TA[1]), "h", 1, 60)
        if C["s07"] <= t < C["s08"]:
            E.frase(c, t, a7, [("+ uma cópia", "g", 64, TINTA2)], 1320, 360, "left", 0.1)
            E.foco(c, t, b7, 0.4, lambda a: E.escreve(c, "gira de cabeça", 1320, 470, 56, "i", TINTA, a))
            E.foco(c, t, b7 + 0.2, 0.4, lambda a: E.escreve(c, "para baixo", 1320, 540, 56, "i", TINTA, a))
            E.foco(c, t, c7, 0.4, lambda a: E.escreve(c, "e encosta no lado", 1320, 640, 56, "i", TINTA, a))
            E.frase(c, t, d7, ps("mesma", "i", 60) + [("base e altura", "g", 62, COR)], 1320, 780, "left", 0.1)
            return
        E.frase(c, t, a8, ps("cada triângulo é", "i", 64) + [("metade", "g", 70, COR)], 1060, 330, "left", 0.1)
        fcen(c, t, b8, "A = f{b · h}{2}", 1360, 560, 120, COR)
        E.frase(c, t, c8, [("b", "g", 66, COR)] + ps("= base", "i", 62), 1180, 800, "left", 0.1)
        E.frase(c, t, d8, [("h", "g", 66, COR)] + ps("= altura, em ângulo reto", "i", 62), 1180, 900, "left", 0.1)
    fase(c, t, C["s07"], C["s09"] - 0.1, sete_oito)
    if C["s09"] <= t < C["s10"] + 0.4:
        def nove():
            gancho_fig(c, t, C["s09"] + 0.1, C["s09"] + 0.3, a9, 0.14)
            E.frase(c, t, C["s09"] + 0.2, ps("base 10, altura 6", "i", 70), 1000, 300, "left", 0.1)
            fcen(c, t, a9, "10 × 6 = 60", 1300, 480, 96)
            fcen(c, t, b9, "60 ÷ 2 = 30", 1300, 640, 96)
            bola_res(c, t, b9 + 1.0, "30", 1300, 830, 110, 90)
            E.foco(c, t, b9 + 1.6, 0.4, lambda a: E.escreve(c, "o 30 do começo", 1450, 850, 52, "i", TINTA2, a))
        E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"]:
        return
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    E.frase(c, t, a0, ps("vale para", "i", 76) + [("qualquer triângulo", "g", 80, COR)], W / 2, 200, "center", 0.1)
    # obtusângulo: a altura cai fora, no lado prolongado
    A, B, V = (200, 760), (560, 760), (780, 440)
    E.triangulo(c, t, b0 - 0.4, A, B, V, vertices=None, preenche=0.12, d=0.6)
    if t >= b0:
        tracejado(c, [B, (V[0] + 50, 760)], TINTA2, ep(t, b0, 0.4), 4)
    E._altura(c, t, b0 + 0.3, V, (V[0], 760), "h", 1, 56)
    E.foco(c, t, b0 - 0.1, 0.4, lambda a: centro(c, "b", (A[0] + B[0]) / 2, 830, 56, "g", COR, a))
    E.foco(c, t, b0 + 0.5, 0.4, lambda a: centro(c, "a altura cai fora", 500, 940, 56, "i", COR, a))
    # triângulo retângulo de lados 6 e 8: os lados do reto já são base e altura
    R, P8, P6 = (1100, 760), (1500, 760), (1100, 460)  # 50 px por unidade
    E.triangulo(c, t, c0 - 0.4, R, P8, P6, vertices=None, lados=["8", None, "6"], retos=(0,), tl=[c0 + 0.2, None, c0 + 0.4], preenche=0.12, d=0.6, size=58)
    fcen(c, t, d0, "6 × 8 = 48", 1560, 470, 80)
    fcen(c, t, d0 + 1.2, "48 ÷ 2 = 24", 1560, 590, 80)
    bola_res(c, t, d0 + 2.0, "24", 1690, 760, 80, 70)


# ---------------- erro: lado inclinado no lugar da altura ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1, e1, f1 = (C[f"s11.{k}"] for k in "abcdef")
    E.frase(c, t, C["s11"] + 0.2, ps("o erro:", "i", 70) + [("lado inclinado no lugar da altura", "g", 66, ERRADO)], W / 2, 180, "center", 0.1)
    E.paralelogramo(c, t, C["s11"] + 0.3, PX, PY, PW_, PH, PD, base="8", size=58)
    lado_cor(c, PBR, PTR, ERRADO, ep(t, b1, 0.6), 12)
    E.foco(c, t, b1 + 0.3, 0.4, lambda a: E.escreve(c, "5", (PBR[0] + PTR[0]) / 2 + 30, (PBR[1] + PTR[1]) / 2 + 20, 64, "g", ERRADO, a))
    E.foco(c, t, c1, 0.5, lambda a: E.escreve(c, "8 × 5 = 40", 1250, 420, 90, "g", ERRADO, a))
    if t >= e1:
        E.risco(c, 1240, 440, 1720, 350, t, e1, largura=12)
    E._altura(c, t, d1 - 0.2, PTL, PE, "", 1, 58)
    lado_cor(c, PTL, PE, CERTO, ep(t, d1, 0.6), 10)
    E.foco(c, t, d1 + 0.3, 0.4, lambda a: E.escreve(c, "4", PE[0] + 22, (PTL[1] + PE[1]) / 2 + 20, 64, "g", CERTO, a))
    E.foco(c, t, d1 + 0.5, 0.4, lambda a: E.escreve(c, "5 é maior que 4", 1250, 560, 60, "i", TINTA, a))
    fcen(c, t, e1, "8 × 4 = 32", 1480, 720, 90, CERTO)
    E.foco(c, t, e1 + 0.5, 0.4, lambda a: E.selo(c, 1790, 690, 40, True, a))
    E.foco(c, t, f1, 0.5, lambda a: E.pilula(c, "altura = medida em ângulo reto", W / 2, 960, 58, "g", fundo=CERTO, a=a, cor=BR))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")

    def um():
        E.frase(c, t, a2, ps("divida por 2", "i", 84, CLARO) + [("antes", "g", 90, BR)] + ps("de multiplicar", "i", 84, CLARO), W / 2, 230, "center", 0.1)
        fcen(c, t, C["s12"] + 2.2, "f{10 × 6}{2}", 520, 560, 110, CLARO)
        E.foco(c, t, b2, 0.4, lambda a: E.risco(c, 400, 520, 520, 430, t, b2, CLARO, 8))
        E.foco(c, t, b2, 0.4, lambda a: E.escreve(c, "5", 420, 430, 80, "g", BR, a))
        fcen(c, t, b2, "10 ÷ 2 = 5", 1240, 470, 90, CLARO)
        fcen(c, t, c2, "5 × 6 = 30", 1240, 640, 110, BR)
        E.foco(c, t, c2 + 1.0, 0.4, lambda a: E.pilula(c, "números menores, conta de cabeça", W / 2, 880, 54, "g", a=a, cor=E.SOBRE))
        if t >= a3:
            E.frase(c, t, a3, ps("metade de um fator =", "i", 62, CLARO) + [("metade do produto", "g", 64, BR)], W / 2, 1000, "center", 0.1)
    E.saida(c, t, b3 - 0.1, um)
    if t < b3 - 0.1:
        return
    E.foco(c, t, b3, 0.5, lambda a: E.pilula(c, "divida o número par", W / 2, 240, 70, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, c3, ps("base e altura", "i", 76, CLARO) + [("ímpares?", "g", 80, BR)], W / 2, 420, "center", 0.1)
    E.foco(c, t, c3 + 0.8, 0.4, lambda a: centro(c, "7 e 5", W / 2, 540, 80, "g", CLARO, a))
    E.frase(c, t, d3, ps("aí,", "i", 72, CLARO) + [("multiplique primeiro", "g", 76, BR)], W / 2, 680, "center", 0.1)
    fcen(c, t, d3 + 1.0, "7 × 5 = 35", 640, 860, 96, BR)
    fcen(c, t, e3 - 0.3, "35 ÷ 2 = 17,5", 1300, 860, 96, CLARO)


# ---------------- questão ----------------
def bandeira(c, t, t0, x, y, base, alt, a=1.0, varal=True):
    """bandeirinha de festa: triângulo de ponta para baixo pendurado no varal"""
    if a <= 0:
        return
    pts = [(x, y), (x + base, y), (x + base / 2, y + alt)]
    if varal:
        E.foco(c, t, t0, 0.5, lambda q: M.line(c, x - 160, y - 8, x + base + 160, y - 8, TINTA2, q * a, 4))
    E.foco(c, t, t0 + 0.2, 0.5, lambda q: peca(c, pts, E.COR, 0.3, q * a))
    return pts


def b_questao(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s14"] + 1.0, ps("bandeirinha de festa", "i", 72), XE, 340, passo=0.1)
    E.foco(c, t, a4, 0.5, lambda a: E.escreve(c, "base 30 cm, altura 45 cm", XE, 460, 64, "g", COR, a))
    E.frase(c, t, b4, ps("quantos", "i", 70) + [("cm² de tecido?", "g", 72, COR)], XE, 620, passo=0.1)
    E.frase(c, t, c4, ps("e", "i", 70) + [("20 bandeirinhas,", "g", 72)] + ps("em", "i", 70) + [("m²?", "g", 72, COR)], XE, 760, passo=0.1)
    x, y, bs, al = 1080, 340, 300, 450  # 10 px por cm
    bandeira(c, t, C["s14"] + 0.4, x, y, bs, al)
    cota_h(c, t, a4, "30 cm", x, x + bs, y - 40)
    E._altura(c, t, a4 + 0.4, (x + bs / 2, y + al), (x + bs / 2, y), "", -1, 52)
    E.foco(c, t, a4 + 0.6, 0.4, lambda a: E.escreve(c, "45 cm", x + bs + 20, y + al / 2, 52, "g", COR, a))
    E.relogio(c, t, C["s15.a"], 1700, 720, 110)


# ---------------- resposta ----------------
ESC_A = Escada(x=150, y=420, sw=210, sh=110, base=900, un=("m²", "dm²", "cm²"), nomes=("", "", ""))


def b_resposta(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    a7, b7, c7 = C["s17.a"], C["s17.b"], C["s17.c"]

    def um():
        x, y, bs, al = 250, 300, 300, 450
        bandeira(c, t, C["s16"] + 0.1, x, y, bs, al)
        cota_h(c, t, C["s16"] + 0.3, "30 cm", x, x + bs, y - 40)
        E._altura(c, t, C["s16"] + 0.5, (x + bs / 2, y + al), (x + bs / 2, y), "", -1, 52)
        E.foco(c, t, C["s16"] + 0.7, 0.4, lambda a: E.escreve(c, "45 cm", x + bs + 20, y + al / 2, 52, "g", COR, a))
        E.frase(c, t, C["s16"] + 0.3, ps("pelo", "i", 66) + [("atalho", "g", 70, COR)], 900, 260, "left", 0.1)
        fcen(c, t, a6, "30 ÷ 2 = 15", 1300, 420, 92)
        fcen(c, t, b6, "15 × 45 = 675", 1300, 580, 92)
        E.foco(c, t, b6 + 0.8, 0.4, lambda a: E.escreve(c, "cm²", 1640, 580, 60, "g", COR, a))
        fcen(c, t, c6, "675 × 20 = 13.500", 1300, 760, 88)
        E.foco(c, t, c6 + 0.8, 0.4, lambda a: E.escreve(c, "cm²", 1700, 760, 60, "g", COR, a))
    E.saida(c, t, C["s17"] - 0.1, um)
    if t < C["s17"]:
        return
    if t < c7:
        def dois():
            ESC_A.degraus(c, t, C["s17"] + 0.1, acesos=(0, 1), ta=a7)
            ESC_A.pulos(c, t, 2, [(a7, 1), (a7 + 0.7, 0)], C["s17"] + 0.4)
            px = num_un(c, t, "13500", 5, [(a7, 3), (a7 + 0.7, 1)], 900, 420, 110, [(C["s17"] + 0.4, "cm²"), (a7 + 0.7, "dm²"), (a7 + 1.4, "m²")],
                        t0=C["s17"] + 0.4, tv=a7 - 0.4)
            casas(c, t, a7 + 0.3, "← 4 casas", 1300, 570, cor=TINTA)
            if px and t >= b7:
                E.risco(c, px(3) - 40, 440, px(4) + 40, 340, t, b7, largura=10)
            bola_res(c, t, b7 + 0.4, "1,35 m²", 1300, 780, 130, 64)
        E.saida(c, t, c7 - 0.1, dois)
        return
    x, y, bs, al = 760, 300, 300, 450
    bandeira(c, t, c7, x, y, bs, al)
    lado_cor(c, (x + bs, y), (x + bs / 2, y + al), ERRADO, ep(t, c7 + 0.6, 0.6), 10)
    E._altura(c, t, c7 + 0.3, (x + bs / 2, y + al), (x + bs / 2, y), "", -1, 52)
    lado_cor(c, (x + bs / 2, y + al), (x + bs / 2, y), CERTO, ep(t, c7 + 0.3, 0.6), 10)
    E.foco(c, t, c7 + 0.6, 0.4, lambda a: E.escreve(c, "45 cm: do bico até a base", 1160, 520, 58, "g", CERTO, a))
    E.foco(c, t, c7 + 1.2, 0.4, lambda a: E.escreve(c, "não é o lado", 1160, 640, 58, "i", ERRADO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s18.a", "paralelogramo:", "A = b · h"), ("s18.b", "triângulo:", "a metade"), ("s18.c", "altura:", "em ângulo reto"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 410 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 84) + [(l2, "g", 88, COR)], 430, y, "left", 0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a9, [("trapézio", "g", 130, COR)], XE, 430, passo=0.12)
    E.frase(c, t, b9, ps("e", "i", 100) + [("losango", "g", 130, COR)], XE, 590, passo=0.12)
    E.trapezio(c, t, a9, 1060, 240, 400, 220, 200, preenche=0.12, d=0.7)
    E.poligono(c, t, b9, [(1540, 340), (1680, 220), (1820, 340), (1680, 460)], preenche=0.12, d=0.7)
    E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c9 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1580, p), lerp(970, 785, p), ep(t, c9 + 0.2, 0.4))
    E.frase(c, t, d9, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, paralelogramo=b_paralelogramo, triangulo=b_triangulo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
