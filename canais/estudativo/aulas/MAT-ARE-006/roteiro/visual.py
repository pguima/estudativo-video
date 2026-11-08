"""Visual — Estudativo · MAT-ARE-006: maior área com perímetro fixo (A(x) = x(20 − x), vértice em x = 10: o quadrado de 10 por 10).
Mesma linguagem da trilha (docstring de MAT-ARE-001): a cerca() é o perímetro, o retângulo do kit é a área.
Peças locais novas: cercado() desenha um retângulo de base x e altura 20 − x que muda de forma com a mesma cerca (a área acompanha);
muro() é o muro hachurado do cercado encostado. A parábola usa E.plano, E.curva e E.ponto (a linguagem de Funções, MAT-FUN-016 a 018).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-006_maior_area_perimetro_fixo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("funcao", "parabola", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

A_ = lambda x: x * (20 - x)
assert 19 * 1 == 19 and 15 * 5 == 75 and A_(10) == 100 and A_(5) == 75 and A_(19) == 19 and (0 + 20) / 2 == 10 and -20 / (2 * -1) == 10
assert 4 * 20 == 80 and 40 / 4 == 10 and 10 * (40 - 2 * 10) == 200 and 10 + 10 + 20 == 40 and max(A_(x / 10) for x in range(201)) == 100


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
def num(v):
    return str(int(round(v))) if abs(v - round(v)) < 0.05 else f"{v:.1f}".replace(".", ",")


def cercado(c, x0, yb, xb, k, a=1.0, cor_cerca=None, p=1.0, rot=True, size=50):
    """retângulo de base xb e altura 20 − xb (em metros), com o canto de baixo à esquerda em (x0, yb), k px por metro"""
    if a <= 0:
        return
    w, h = xb * k, (20 - xb) * k
    M.rrect(c, x0, yb - h, w, h, 4, E.mix(E.COR, "#FFFFFF", 0.86), a)
    cerca(c, [(x0, yb - h), (x0 + w, yb - h), (x0 + w, yb), (x0, yb)], p, cor_cerca, largura=9, a=a)
    if rot:
        centro(c, num(xb), x0 + w / 2, yb + 30 + size, size, "g", COR, a)
        E.escreve(c, num(20 - xb), x0 + w + 26, yb - h / 2 + size * 0.36, size, "g", TINTA2, a)


def muro(c, x0, x1, y, a=1.0, cima=True):
    """muro hachurado: a faixa fica acima de y (cima=True) ou abaixo"""
    if a <= 0:
        return
    hh = 36
    y0 = y - hh if cima else y
    M.rrect(c, x0, y0, x1 - x0, hh, 3, "#B9B4AA", a)
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x0, y0, x1 - x0, hh))
    for xx in range(int(x0) - 40, int(x1) + 40, 22):
        M.line(c, xx, y0 + hh, xx + hh, y0, "#8C877D", a, 3)
    c.restore()
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, x1 - x0, hh), M.paint(TINTA, a, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    k, yb = 30, 800

    def um():
        E.frase(c, t, ka, [("40 m", "g", 96, COR)] + ps("de cerca", "i", 84), W / 2, 230, "center", 0.1)
        for t0, x0, (bb, hh), area in ((kb, 120, (19, 1), "19 m²"), (kc, 800, (15, 5), "75 m²"), (kd, 1360, (10, 10), "?")):
            w, h = bb * k, hh * k
            q = ep(t, t0, 0.5)
            if q <= 0:
                continue
            if area == "?":
                tracejado(c, [(x0, yb - h), (x0 + w, yb - h), (x0 + w, yb), (x0, yb), (x0, yb - h)], TINTA2, q, 5)
            else:
                M.rrect(c, x0, yb - h, w, h, 3, E.mix(E.COR, "#FFFFFF", 0.86), q)
                cerca(c, [(x0, yb - h), (x0 + w, yb - h), (x0 + w, yb), (x0, yb)], ease_io(prog(t, t0, 1.0)), largura=8, postes=False)
            centro(c, f"{bb} × {hh}", x0 + w / 2, yb + 80, 54, "g", TINTA, q)
            centro(c, area, x0 + w / 2, yb - h - 40, 72 if area != "?" else 110, "g", COR, ep(t, t0 + 0.5, 0.4))
        E.frase(c, t, kd + 0.6, ps("mesma cerca,", "i", 70) + [("qual a maior área?", "g", 72, COR)], W / 2, 980, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 290, passo=0.12)
        E.frase(c, t, ta + 0.9, [("a maior área", "g", 110, COR)], XE, 440, passo=0.12)
        E.frase(c, t, ta + 1.6, ps("para uma cerca dada", "i", 80), XE, 560, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("pelo", "i", 72) + [("vértice", "g", 76, COR)] + ps("da parábola", "i", 72), XE, 720, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 900
    itens = (("s03.b", "área do retângulo", "A = b · h"), ("s03.c", "perímetro", "a volta inteira"),
             ("s03.d", "x do vértice", "média das raízes  ou  f{−b}{2a}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 250
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 200, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 80)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 160 if i < 2 else y + 150, 56, "g", COR)
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 590, q1), 840, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.7), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1010, "left", 0.12)


# ---------------- montar a função ----------------
def b_funcao(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    x0, y0, w, h = 320, 330, 560, 340
    pts = ret_pts(x0, y0, w, h)
    # a base muda com a mesma cerca durante "cada base dá uma área"
    if t >= b5:
        # a base anda de metro em metro (8, 9, ... 16 e volta), parando um pouco em cada valor; a cerca é sempre a mesma
        f = 0.5 - 0.5 * math.cos(2 * math.pi * min(t - b5, c5 - b5 + 0.8) / max(1.0, (c5 - b5 + 0.8)))
        xs = lerp(8, 16, f)
        i_ = math.floor(xs)
        xb = i_ + ease_io(M.clamp((xs - i_ - 0.7) / 0.3))
        k = 34
        E.foco(c, t, b5, 0.3, lambda a: cercado(c, x0 - 120, y0 + h + 80, xb, k, a, rot=False))
        xr = int(round(xb))
        E.foco(c, t, b5, 0.3, lambda a: (centro(c, str(xr), x0 - 120 + xb * k / 2, y0 + h + 150, 56, "g", COR, a),
                                         E.escreve(c, str(20 - xr), x0 - 120 + xb * k + 26, y0 + h + 80 - (20 - xb) * k / 2 + 20, 56, "g", TINTA2, a),
                                         E.escreve(c, f"A = {xr} × {20 - xr} = {xr * (20 - xr)}", 200, 1000, 60, "g", COR, a)))
    else:
        E.foco(c, t, C["s04"] + 0.1, 0.5, lambda a: M.rrect(c, x0, y0, w, h, 4, E.mix(E.COR, "#FFFFFF", 0.86), a * (1 - ep(t, b5, 0.3) if t < b5 + 1 else 1)))
        cerca(c, pts, ease_io(prog(t, C["s04"] + 0.3, 1.2)), TINTA2, largura=8, a=0.5 if t >= a4 else 1.0)
        if t >= a4:
            cerca(c, [pts[0], pts[3], pts[2]], ease_io(prog(t, a4, 1.0)), largura=10, fecha=False)
        E.foco(c, t, c4, 0.4, lambda a: centro(c, "x", x0 + w / 2, y0 + h + 90, 72, "g", COR, a))
        E.foco(c, t, d4, 0.4, lambda a: E.escreve(c, "20 − x", x0 - 30 - E.larg("20 − x", "g", 60), y0 + h / 2 + 22, 60, "g", TINTA2, a))
    if t < C["s05"]:
        fcen(c, t, a4, "volta: 40 m  →  meia volta: 20 m", 1340, 330, 60)
        fcen(c, t, b4, "base + altura = 20", 1340, 520, 80, COR)
        fcen(c, t, c4, "base = x", 1340, 680, 72)
        fcen(c, t, d4, "altura = 20 − x", 1340, 820, 72, TINTA2)
        return
    fcen(c, t, a5, "A(x) = x(20 − x)", 1340, 360, 96, COR)
    E.foco(c, t, b5, 0.4, lambda a: centro(c, "cada base dá uma área", 1340, 500, 56, "i", TINTA, a))
    fcen(c, t, c5, "A(x) = 20x − x²", 1340, 700, 96)


# ---------------- a parábola ----------------
def b_parabola(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7 = C["s07.a"], C["s07.b"]
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    P = E.plano(c, t, C["s06"] + 0.1, 200, 230, 760, 640, 0, 20, 0, 110, passo=5, passo_y=25, nomes=("x", "A"))
    E.curva(c, t, a6, P, A_, 0, 20, d=1.4)
    E.foco(c, t, a6 + 1.0, 0.4, lambda a: E.formula(c, "A(x) = 20x − x²", P.x(13.2), P.y(108), 50, "g", COR, a))
    if t >= d6:
        E.ponto(c, t, d6, P, 10, 100, None, r=16)
    E.ponto(c, t, a7, P, 0, 0, None)
    E.ponto(c, t, a7 + 0.5, P, 20, 0, None)
    if t >= a8 + 0.4:
        q = ep(t, a8 + 0.4, 0.6)
        M.line(c, P.x(10), P.y(0), P.x(10), P.y(100), TINTA2, q, 4, dash=[14, 10])
    X = 1400
    if t < C["s07"]:
        fcen(c, t, a6, "tem x²: parábola", X, 330, 72)
        E.foco(c, t, b6, 0.4, lambda a: E.formula(c, "−1x²", X, 480, 80, "g", ERRADO, a, "center"))
        E.foco(c, t, c6, 0.4, lambda a: centro(c, "abre para baixo", X, 590, 64, "g", TINTA, a))
        E.frase(c, t, d6, ps("vértice =", "i", 66) + [("ponto mais alto", "g", 68, COR)], X, 760, "center", 0.1)
        E.foco(c, t, d6 + 0.6, 0.4, lambda a: centro(c, "a maior área", X, 860, 56, "i", COR, a))
        return
    if t < C["s08"]:
        E.foco(c, t, a7, 0.4, lambda a: centro(c, "raízes:", X, 340, 60, "i", TINTA, a))
        fcen(c, t, a7 + 0.3, "x = 0  ou  x = 20", X, 450, 80, COR)
        E.foco(c, t, b7, 0.4, lambda a: centro(c, "base 0 ou altura 0:", X, 620, 58, "i", TINTA, a))
        E.foco(c, t, b7 + 0.5, 0.4, lambda a: centro(c, "sem área nenhuma", X, 710, 64, "g", TINTA2, a))
        # o retângulo achatado
        E.foco(c, t, b7 + 0.8, 0.4, lambda a: (M.rrect(c, X - 250, 800, 500, 10, 3, E.COR, a), centro(c, "20 × 0", X, 880, 48, "g", TINTA2, a)))
        return
    if t < C["s09"]:
        E.foco(c, t, a8, 0.4, lambda a: centro(c, "x do vértice = média das raízes", X, 300, 52, "i", TINTA, a))
        fcen(c, t, b8, "f{0 + 20}{2} = 10", X, 440, 84, COR)
        fcen(c, t, c8, "a = −1   b = 20", X, 640, 72, TINTA2)
        E.foco(c, t, c8 + 0.5, 0.4, lambda a: centro(c, "(este a não é a área)", X, 720, 46, "i", TINTA2, a))
        fcen(c, t, d8, "f{−20}{2 · (−1)} = 10", X, 880, 84, COR)
        return
    E.foco(c, t, C["s09"], 0.4, lambda a: centro(c, "base 10", X, 300, 70, "g", TINTA, a))
    fcen(c, t, a9, "altura: 20 − 10 = 10", X, 410, 70)
    E.foco(c, t, b9, 0.5, lambda a: (M.rrect(c, X - 240, 470, 150, 150, 4, E.mix(E.COR, "#FFFFFF", 0.8), a),
                                     c.drawRect(skia.Rect.MakeXYWH(X - 240, 470, 150, 150), M.paint(E.COR, a, stroke=7)),
                                     E.escreve(c, "quadrado!", X - 60, 570, 66, "g", COR, a)))
    fcen(c, t, c9, "10 × 10 = 100", X, 740, 84)
    bola_res(c, t, c9 + 1.0, "100 m²", X, 900, 110, 56)
    E.ponto(c, t, c9, P, 10, 100, "100", r=16, lado=(1, -1))
    E.ponto(c, t, d9, P, 5, 75, "75", cor=TINTA2, lado=(-1, -1))
    E.ponto(c, t, d9 + 0.4, P, 19, 19, "19", cor=TINTA2, lado=(1, -1))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    E.frase(c, t, C["s10"] + 0.2, ps("o erro:", "i", 70) + [("a volta inteira no lugar da meia", "g", 66, ERRADO)], W / 2, 180, "center", 0.1)
    E.foco(c, t, b0, 0.5, lambda a: E.formula(c, "A(x) = x(40 − x)", 200, 380, 84, "g", ERRADO, a))
    E.foco(c, t, c0, 0.5, lambda a: E.formula(c, "vértice em x = 20", 200, 520, 72, "g", ERRADO, a))
    E.foco(c, t, c0 + 0.6, 0.5, lambda a: E.formula(c, "quadrado 20 × 20?", 200, 640, 72, "g", ERRADO, a))
    # o quadrado de 20 por 20 e a volta dele
    x0, y0, L = 1180, 300, 480
    E.foco(c, t, c0 + 0.6, 0.5, lambda a: M.rrect(c, x0, y0, L, L, 4, E.mix(ERRADO, "#FFFFFF", 0.85), a))
    cerca(c, ret_pts(x0, y0, L, L), ease_io(prog(t, d0 - 0.4, 1.4)), ERRADO, largura=9)
    E.foco(c, t, c0 + 0.8, 0.4, lambda a: (centro(c, "20 m", x0 + L / 2, y0 + L + 70, 54, "g", ERRADO, a),
                                           E.escreve(c, "20 m", x0 + L + 26, y0 + L / 2 + 20, 54, "g", ERRADO, a)))
    fcen(c, t, d0, "volta: 4 × 20 = 80 m", 600, 800, 76, ERRADO)
    E.foco(c, t, d0 + 0.8, 0.4, lambda a: E.escreve(c, "o dobro da cerca", 330, 880, 56, "i", ERRADO, a))
    E.foco(c, t, e0, 0.5, lambda a: E.pilula(c, "confira o perímetro da resposta", W / 2, 990, 60, "g", a=a, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1 = C["s11.a"], C["s11.b"], C["s11.c"]
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a1, ps("cerca com a volta inteira:", "i", 76, CLARO), W / 2, 210, "center", 0.1)
        E.frase(c, t, a1 + 1.4, ps("o maior é o", "i", 84, CLARO) + [("quadrado", "g", 96, BR)], W / 2, 340, "center", 0.1)
        fcen(c, t, b1, "lado = f{perímetro}{4}", W / 2, 560, 96, BR)
        fcen(c, t, c1, "f{40}{4} = 10", W / 2, 820, 110, CLARO)
    E.saida(c, t, C["s12"] - 0.1, um)
    if t < C["s12"]:
        return
    P = E.plano(c, t, C["s12"] + 0.2, 160, 300, 560, 440, 0, 20, 0, 110, passo=5, passo_y=50, rotulos=False, escuro=True, nomes=("x", "A"))
    E.curva(c, t, C["s12"] + 0.4, P, A_, 0, 20, d=1.0, cor=CLARO)
    E.ponto(c, t, a2, P, 0, 0, "0", cor=BR, lado=(-1, 1))
    E.ponto(c, t, a2 + 0.4, P, 20, 0, "meia volta", cor=BR, lado=(1, -1))
    E.ponto(c, t, b2 - 0.3, P, 10, 100, "meio", cor=BR, lado=(1, -1))
    E.frase(c, t, a2, ps("raízes:", "i", 66, CLARO) + [("0 e a meia volta", "g", 66, BR)], 1000, 360, "left", 0.1)
    E.frase(c, t, b2, ps("vértice no meio:", "i", 66, CLARO) + [("base = altura", "g", 66, BR)], 1000, 480, "left", 0.1)
    E.frase(c, t, c2, ps("cercado", "i", 66, CLARO) + [("encostado no muro?", "g", 66, BR)], 1000, 680, "left", 0.1)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "monte a função", 1400, 820, 64, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
MX0, MX1, MY, MK = 1060, 1700, 420, 22  # o muro (em cima) e o cercado embaixo dele; MK px por metro


def b_questao(c, t, C, b):
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, C["s13"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a3 - 0.4, ps("cercado", "i", 72) + [("encostado no muro", "g", 72, COR)], XE, 350, passo=0.1)
    E.foco(c, t, b3, 0.5, lambda a: E.escreve(c, "40 m de cerca em 3 lados", XE, 470, 60, "g", TINTA, a))
    E.frase(c, t, c3, ps("quais medidas dão a", "i", 64), XE, 640, passo=0.1)
    E.frase(c, t, c3 + 0.8, [("maior área?", "g", 80, COR)], XE, 760, passo=0.1)
    E.foco(c, t, a3, 0.5, lambda a: muro(c, MX0, MX1, MY, a))
    E.foco(c, t, a3 + 0.3, 0.4, lambda a: centro(c, "muro", (MX0 + MX1) / 2, MY - 60, 50, "i", TINTA2, a))
    x0, w, h = MX0 + 80, 480, 280
    cerca(c, [(x0, MY), (x0, MY + h), (x0 + w, MY + h), (x0 + w, MY)], ease_io(prog(t, b3, 1.3)), fecha=False, largura=9)
    E.foco(c, t, b3 + 0.3, 0.3, lambda a: M.rrect(c, x0 + 6, MY + 4, w - 12, h - 10, 4, E.mix(E.COR, "#FFFFFF", 0.88), a))
    E.saida(c, t, C["s14.a"] - 0.1, lambda: E.foco(c, t, b3 + 0.8, 0.4, lambda a: centro(c, "?", x0 + w / 2, MY + h / 2 + 40, 110, "g", COR, a)))
    E.relogio(c, t, C["s14.a"], x0 + w / 2, MY + h / 2, 110)


# ---------------- resposta ----------------
RX, RY, RK = 260, 560, 26  # o muro na horizontal em RY; o cercado embaixo, o espelho em cima


def b_resposta(c, t, C, b):
    a5, b5, c5 = C["s15.a"], C["s15.b"], C["s15.c"]
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    a7, b7, c7, d7, e7 = (C[f"s17.{k}"] for k in "abcde")
    w, h = 20 * RK, 10 * RK
    fim = t >= d6  # os lados ganham os números
    E.foco(c, t, C["s15"] + 0.1, 0.5, lambda a: muro(c, RX - 60, RX + w + 60, RY, a))
    E.foco(c, t, C["s15"] + 0.4, 0.3, lambda a: M.rrect(c, RX + 6, RY + 4, w - 12, h - 10, 4, E.mix(E.COR, "#FFFFFF", 0.86), a))
    cerca(c, [(RX, RY), (RX, RY + h), (RX + w, RY + h), (RX + w, RY)], ease_io(prog(t, C["s15"] + 0.3, 1.0)), fecha=False, largura=9)
    E.foco(c, t, a5, 0.4, lambda a: (E.escreve(c, "10" if fim else "x", RX - 30 - E.larg("10" if fim else "x", "g", 56), RY + h / 2 + 20, 56, "g", COR, a),
                                     E.escreve(c, "10" if fim else "x", RX + w + 26, RY + h / 2 + 20, 56, "g", COR, a)))
    rot_f = "20" if t >= e6 else "40 − 2x"
    E.foco(c, t, b5, 0.4, lambda a: centro(c, rot_f, RX + w / 2, RY + h + 76, 56, "g", TINTA2, a))
    # o espelho do outro lado do muro: quadrado 20 × 20 com a volta inteira
    if t >= c7:
        q = ep(t, c7, 0.6)
        tracejado(c, [(RX, RY), (RX, RY - h), (RX + w, RY - h), (RX + w, RY)], CINZA, q, 6)
        E.foco(c, t, c7 + 0.6, 0.4, lambda a: centro(c, "espelho", RX + w / 2, RY - h / 2 + 18, 52, "i", TINTA2, a))
        E.foco(c, t, lerp(c7, d7, 0.45), 0.4, lambda a: centro(c, "quadrado 20 × 20, volta de 80 m", RX + w / 2, RY - h - 40, 46, "g", TINTA2, a))
    if t >= d7:
        c.drawRect(skia.Rect.MakeXYWH(RX, RY, w, h), M.paint(E.COR, ep(t, d7, 0.5), stroke=8))
    X = 1360
    if t < C["s16"]:
        E.foco(c, t, a5, 0.4, lambda a: centro(c, "x = cada lado que sai do muro", X, 320, 52, "i", TINTA, a))
        E.foco(c, t, b5, 0.4, lambda a: centro(c, "frente: 40 − 2x", X, 460, 70, "g", TINTA2, a))
        fcen(c, t, c5, "A(x) = x(40 − 2x)", X, 680, 88, COR)
        return
    if t < C["s17"]:
        fcen(c, t, C["s16"] + 0.1, "A(x) = x(40 − 2x)", X, 250, 64, COR)
        fcen(c, t, a6, "raízes: x = 0", X, 380, 70)
        fcen(c, t, b6, "40 − 2x = 0  →  x = 20", X, 500, 70)
        fcen(c, t, c6, "f{0 + 20}{2} = 10", X, 660, 80, COR)
        fcen(c, t, d6, "lados do muro: 10 m", X, 820, 64)
        fcen(c, t, e6, "frente: 40 − 20 = 20 m", X, 930, 64, TINTA2)
        return
    fcen(c, t, a7, "10 × 20 = 200", X - 140, 300, 88)
    bola_res(c, t, a7 + 1.0, "200 m²", 1730, 290, 110, 54)
    E.foco(c, t, b7, 0.5, lambda a: E.escreve(c, "não é um quadrado!", 1100, 480, 66, "g", ERRADO, a))
    E.frase(c, t, d7, ps("o seu cercado é", "i", 62) + [("a metade", "g", 66, COR)], 1100, 640, "left", 0.1)
    E.foco(c, t, d7 + 0.8, 0.4, lambda a: E.escreve(c, "10 × 20", 1100, 730, 66, "g", COR, a))
    fcen(c, t, e7, "10 + 10 + 20 = 40", X, 900, 80)
    E.foco(c, t, e7 + 1.0, 0.4, lambda a: E.selo(c, 1760, 875, 40, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s18.a", "a área em", "função de um lado"), ("s18.b", "ache o", "vértice"), ("s18.c", "volta inteira:", "o quadrado"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 410 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 84) + [(l2, "g", 88, COR)], 430, y, "left", 0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    E.frase(c, t, C["s19"] + 0.2, ps("na próxima aula,", "i", 80) + [("prática", "g", 90, COR)], XE, 260, passo=0.12)
    E.frase(c, t, a9, ps("a", "i", 72) + [("fórmula certa", "g", 76, COR)] + ps("para cada figura", "i", 72), XE, 420, passo=0.1)
    E.frase(c, t, b9, [("converter", "g", 76, COR)] + ps("unidades", "i", 72), XE, 540, passo=0.1)
    E.frase(c, t, c9, ps("o", "i", 72) + [("custo", "g", 76, COR)] + ps("de piso, cerca e pintura", "i", 72), XE, 660, passo=0.1)
    E.foco(c, t, d9, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d9 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1580, p), lerp(990, 815, p), ep(t, d9 + 0.2, 0.4))
    E.frase(c, t, e9, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, funcao=b_funcao, parabola=b_parabola, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
