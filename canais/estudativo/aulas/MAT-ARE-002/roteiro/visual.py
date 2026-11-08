"""Visual — Estudativo · MAT-ARE-002: área do quadrado e do retângulo (base × altura, ℓ², contar pisos pelos lados).
Mesma linguagem da trilha (docstring de MAT-ARE-001): área = quadradinhos que entram fileira a fileira (grade_q), perímetro = cerca()
na cor da matéria, conversão pela escada do metro (Escada e num_un). Peças locais novas: pisos() desenha pisos que entram um a um,
metro_q() mostra um metro quadrado com os seus pisos, e quarto() é o chão de 4 m por 3 m (150 px por metro).
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-002_area_quadrado_retangulo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("contar", "quadrado", "pisos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 3 * 4 == 12 and 5 ** 2 == 25 and 2.5 * 0.4 == 1.0 and 8 * 6 == 48 and 12 * 4 == 48 and 12 * 2 == 24
assert 0.5 * 0.5 == 0.25 and 600 // 30 == 20 and 20 * 20 == 400 and 6 * 4 == 24


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
QX, QY, QS = 200, 330, 150  # o quarto: 4 m por 3 m, 150 px por metro
QW, QH = 4 * QS, 3 * QS


def chao(c, t, t0, base="4 m", altura="3 m", tl=None, a=1.0):
    """o chão do quarto, com a base embaixo e a altura à esquerda"""
    if a <= 0:
        return
    if a < 1:
        c.saveLayer(None, M.paint("#000000", a))
    E.retangulo(c, t, t0, QX, QY, QW, QH, base, altura, tl=tl, size=56, preenche=0.0)
    if a < 1:
        c.restore()


def pisos(c, t, x, y, cols, lins, s, t0, dur=1.2, cor=None, a=1.0, so=None, ti=None):
    """pisos de lado s, a partir de (x, y), entrando um a um em `dur` (ou fileira a fileira em ti).
    so = função (coluna, fileira) → True para só desenhar alguns"""
    if a <= 0:
        return
    n = cols * lins
    for r in range(lins):
        for k in range(cols):
            if so and not so(k, r):
                continue
            t_ = (ti[r] + 0.05 * k) if ti else t0 + dur * (r * cols + k) / max(1, n)
            q = ep(t, t_, 0.25) * a
            if q > 0:
                M.rrect(c, x + k * s + 2, y + r * s + 2, s - 4, s - 4, max(3, s * 0.08), cor or E.COR, q)


def linhas_m(c, x, y, cols, lins, s, a=1.0, cor=None):
    """linhas finas da grade (um metro em cada casa)"""
    if a <= 0:
        return
    for k in range(1, cols):
        M.line(c, x + k * s, y, x + k * s, y + lins * s, cor or FIO, a, 3)
    for r in range(1, lins):
        M.line(c, x, y + r * s, x + cols * s, y + r * s, cor or FIO, a, 3)


def metro_q(c, x, y, L, n, a=1.0, metade=False):
    """um metro quadrado de lado L com n x n pisos (metade=True: só a fileira de cima, a outra metade vazia em vermelho)"""
    if a <= 0:
        return
    M.rrect(c, x, y, L, L, 4, "#FFFFFF", a)
    s = L / n
    for r in range(n):
        for k in range(n):
            if metade and r >= n / 2:
                continue
            M.rrect(c, x + k * s + 3, y + r * s + 3, s - 6, s - 6, 6, E.COR, a)
    if metade:
        c.drawRect(skia.Rect.MakeXYWH(x, y + L / 2, L, L / 2), M.paint(ERRADO, 0.22 * a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(TINTA, a, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        chao(c, t, ka, tl=[ka + 0.6, None, None, ka + 1.0])
        E.foco(c, t, kb, 0.5, lambda a: (M.rrect(c, 1080, 300, 112, 112, 8, E.COR, a),
                                         E.escreve(c, "piso de", 1230, 345, 56, "i", TINTA, a),
                                         E.escreve(c, "0,5 m de lado", 1230, 410, 60, "g", COR, a)))
        E.frase(c, t, lerp(kb, kc, 0.45), ps("quantos", "i", 76) + [("pisos?", "g", 84, COR)], 1080, 560, "left", 0.1)
        E.foco(c, t, kc, 0.5, lambda a: E.escreve(c, "12 m² × 2 = 24", 1080, 720, 84, "g", ERRADO, a))
        # 24 pisos: dois em cada metro quadrado, e a metade de baixo de cada um fica vazia
        if t >= kd:
            linhas_m(c, QX, QY, 4, 3, QS, ep(t, kd, 0.4))
            pisos(c, t, QX, QY, 8, 6, QS / 2, kd, 1.4, so=lambda k, r: r % 2 == 0)
            for r in range(3):
                c.drawRect(skia.Rect.MakeXYWH(QX, QY + r * QS + QS / 2, QW, QS / 2), M.paint(ERRADO, 0.2 * ep(t, kd + 1.4, 0.5)))
        E.frase(c, t, kd + 1.0, [("metade", "g", 72, ERRADO)] + ps("do chão sem piso", "i", 66), 1080, 880, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 290, passo=0.12)
        E.frase(c, t, ta + 0.9, [("a área", "g", 120, COR)], XE, 450, passo=0.12)
        E.frase(c, t, ta + 1.4, ps("de retângulos e quadrados", "i", 78), XE, 570, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.6), [("contar pisos", "g", 80, COR)] + ps("sem errar", "i", 76), XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "área =", "quadradinhos que cobrem"), ("s03.c", "o metro quadrado:", "1 m² = quadrado de 1 m"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, l2=l2, y=y: E.escreve(c, l2, x + 44, y + 160, 56, "g", COR, a))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 700, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.6), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- contar quadradinhos: base × altura ----------------
def b_contar(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5, d5, e5, f5 = (C[f"s05.{k}"] for k in "abcdef")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    # o quarto fica o bloco inteiro: primeiro o contorno (perímetro), depois o que fica dentro (área)
    chao(c, t, C["s04"] + 0.1, tl=[C["s04"] + 0.6, None, None, C["s04"] + 0.8])
    q_cont = 1 - ep(t, a4, 0.5)
    cerca(c, ret_pts(QX, QY, QW, QH), ease_io(prog(t, C["s04"] + 0.3, 1.0)), postes=False, largura=10, a=q_cont)
    E.foco(c, t, C["s04"] + 0.4, 0.4, lambda a: E.escreve(c, "perímetro: o contorno", 1000, 300, 60, "i", TINTA2, a * q_cont))
    if t >= a4:
        c.drawRect(skia.Rect.MakeXYWH(QX, QY, QW, QH), M.paint(E.COR, 0.12 * ep(t, a4, 0.5)))
    grade_q(c, t, 0, 4, 3, QX, QY, QS, ti=[b4, c4, c4 + 0.5])

    if t < C["s05"]:
        E.frase(c, t, a4, [("área:", "g", 84, COR)] + ps("o que fica dentro", "i", 80), 1000, 300, "left", 0.1)
        E.foco(c, t, b4 + 0.2, 0.4, lambda a: E.escreve(c, "4 em cada fileira", 1000, 450, 64, "i", TINTA, a))
        E.foco(c, t, c4 + 0.2, 0.4, lambda a: E.escreve(c, "3 fileiras", 1000, 550, 64, "i", TINTA, a))
        fcen(c, t, d4, "3 × 4 = 12", 1300, 720, 100)
        bola_res(c, t, d4 + 1.0, "12 m²", 1300, 900, 120, 70)
        return

    def cinco():
        # a base (deitada) e a altura (em pé), sobre o quarto
        for (P0, P1), tk in ((((QX, QY + QH), (QX + QW, QY + QH)), a5), (((QX, QY + QH), (QX, QY)), b5)):
            q = ep(t, tk, 0.6)
            if q > 0:
                M.line(c, *P0, lerp(P0[0], P1[0], ease_io(q)), lerp(P0[1], P1[1], ease_io(q)), E.COR if tk == a5 else TINTA2, 1.0, 12)
        E.foco(c, t, a5 + 0.3, 0.4, lambda a: centro(c, "base", QX + QW / 2, QY + QH + 140, 60, "g", COR, a))
        E.foco(c, t, b5 + 0.3, 0.4, lambda a: E.escreve(c, "altura", QX - 20 - E.larg("altura", "g", 50), QY - 30, 50, "g", TINTA2, a))
        E.foco(c, t, a5 + 0.3, 0.4, lambda a: E.escreve(c, "base: quantos em cada fileira", 1000, 300, 52, "i", COR, a))
        E.foco(c, t, b5 + 0.3, 0.4, lambda a: E.escreve(c, "altura: quantas fileiras", 1000, 380, 52, "i", TINTA2, a))
        fcen(c, t, c5, "A = b · h", 1360, 600, 140, COR)
        for k, (tk, letra, nome, cor) in enumerate(((d5, "A", "área", COR), (e5, "b", "base", COR), (f5, "h", "altura", TINTA2))):
            y = 760 + k * 90
            E.foco(c, t, tk, 0.4, lambda a, letra=letra, nome=nome, cor=cor, y=y: (E.escreve(c, letra, 1150, y, 70, "g", cor, a),
                                                                                  E.escreve(c, "= " + nome, 1230, y, 64, "i", TINTA, a)))
    fase(c, t, C["s05"], C["s06"] - 0.1, cinco)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"] + 0.2, ps("e a", "i", 76) + [("unidade?", "g", 80, COR)], 1000, 300, "left", 0.1)
    fcen(c, t, a6, "m × m = m²", 1360, 480, 110)
    E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "² = 2 medidas multiplicadas", 1360, 620, 50, "g", a=a, cor=E.SOBRE))
    fcen(c, t, c6, "cm × cm = cm²", 1360, 800, 96, TINTA2)


# ---------------- quadrado e lados em unidades diferentes ----------------
ESC = Escada(x=1100, y=430, sw=190, sh=95, base=800)


def b_quadrado(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")

    def sete():
        x, y, L = 250, 300, 500
        E.quadrado(c, t, C["s07"] + 0.2, x, y, L, lado="5 m", tl=[C["s07"] + 0.8] * 4, size=58, preenche=0.0)
        grade_q(c, t, a7, 5, 5, x, y, L / 5, dur=1.6)
        E.frase(c, t, C["s07"] + 0.3, [("quadrado:", "g", 76, COR)] + ps("lado × lado", "i", 76), 1000, 300, "left", 0.1)
        fcen(c, t, b7, "A = ℓ²", 1360, 520, 150, COR)
        E.frase(c, t, c7, [("ℓ", "g", 70, COR)] + ps("= lado", "i", 66), 1360, 650, "center", 0.1)
        fcen(c, t, d7, "5² = 5 × 5 = 25", 1360, 800, 84)
        bola_res(c, t, d7 + 1.2, "25 m²", 1360, 960, 90, 54)
    fase(c, t, C["s07"], C["s08"] - 0.1, sete)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"] + 0.2, ps("unidades diferentes?", "i", 72), XE, 200, "left", 0.1)
    E.frase(c, t, a8, [("converta os lados antes", "g", 70, COR)], XE + 690, 200, "left")
    # a tábua: 2,5 m por 40 cm (300 px por metro)
    x, y, w, h = 170, 340, 600, 96  # 240 px por metro
    E.foco(c, t, b8, 0.5, lambda a: (M.rrect(c, x, y, w, h, 6, "#C9A27A", a),
                                     c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=4))))
    cota_hb(c, t, b8 + 0.3, "2,5 m", x, x + w, y + h + 40)
    troca = ep(t, c8 + 1.6, 0.4)
    cota_v(c, t, b8 + 0.8, "40 cm", x + w + 40, y, y + h, direita=True, a=1 - troca)
    if t >= c8 + 1.6:
        cota_v(c, t, c8 + 1.6, "0,4 m", x + w + 40, y, y + h, direita=True)
    # 40 cm → 0,4 m: dois degraus para cima
    ESC.degraus(c, t, c8 - 0.6, acesos=(0, 1), ta=c8)
    ESC.pulos(c, t, 2, [(c8, 1), (c8 + 0.7, 0)], c8 - 0.3)
    px = num_un(c, t, "40", 2, [(c8, 1), (c8 + 0.7, 0)], 1180, 970, 110, [(c8 - 0.3, "cm"), (c8 + 0.7, "dm"), (c8 + 1.4, "m")], t0=c8 - 0.3)
    if px and t >= c8 + 1.6:
        E.risco(c, px(1) - 40, 990, px(1) + 40, 880, t, c8 + 1.6, largura=10)
    fcen(c, t, d8, "2,5 × 0,4 = 1", 470, 680, 96)
    bola_res(c, t, d8 + 1.2, "1 m²", 470, 860, 110, 66)


# ---------------- os pisos do começo ----------------
def b_pisos(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    p = QS / 2
    chao(c, t, C["s09"] + 0.1, tl=[C["s09"] + 0.6, None, None, C["s09"] + 0.8])
    linhas_m(c, QX, QY, 4, 3, QS, ep(t, C["s09"] + 0.5, 0.4))
    # 1 m = 2 pisos: o primeiro metro da base ganha os dois pisos
    pisos(c, t, QX, QY + QH - p, 2, 1, p, a9, 0.5)
    E.foco(c, t, a9 + 0.3, 0.4, lambda a: E.escreve(c, "1 m = 2 pisos", 1000, 300, 64, "g", COR, a))
    # a fileira de baixo inteira: 8 pisos
    pisos(c, t, QX, QY + QH - p, 8, 1, p, b9, 0.9, so=lambda k, r: k >= 2)
    E.foco(c, t, b9 + 0.3, 0.4, lambda a: E.escreve(c, "8 em cada fileira", 1000, 400, 64, "i", TINTA, a))
    # a coluna da esquerda: 6 fileiras
    pisos(c, t, QX, QY, 1, 6, p, c9, 0.8, so=lambda k, r: r < 5)
    E.foco(c, t, c9 + 0.3, 0.4, lambda a: E.escreve(c, "6 fileiras", 1000, 500, 64, "i", TINTA, a))
    # o resto do chão
    pisos(c, t, QX + p, QY, 7, 5, p, a0, 1.2)
    fcen(c, t, a0, "8 × 6 = 48", 1300, 660, 96)
    E.foco(c, t, b0, 0.5, lambda a: metro_q(c, 1000, 760, 200, 2, a))
    E.foco(c, t, b0 + 0.3, 0.4, lambda a: E.escreve(c, "1 m² = 4 pisos", 1240, 880, 56, "g", COR, a))
    fcen(c, t, c0, "12 × 4 = 48", 1400, 1010, 70, TINTA2)
    bola_res(c, t, a0 + 1.0, "48", 1700, 640, 100, 70)
    E.foco(c, t, c0 + 1.4, 0.4, lambda a: E.selo(c, 1780, 990, 40, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    E.frase(c, t, C["s11"] + 0.2, ps("o erro:", "i", 70) + [("lado do piso não é área", "g", 70, ERRADO)], W / 2, 180, "center", 0.1)

    def um():
        # o piso: meio metro é o lado; a área é um quarto do metro quadrado
        x, y, L = 300, 330, 480
        E.foco(c, t, a1, 0.5, lambda a: (M.rrect(c, x, y, L, L, 4, "#FFFFFF", a), c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(TINTA, a, stroke=4))))
        cota_h(c, t, a1 + 0.3, "1 m", x, x + L, y - 30)
        E.foco(c, t, b1, 0.5, lambda a: M.rrect(c, x + 3, y + 3, L / 2 - 6, L / 2 - 6, 8, E.COR, a))
        cota_v(c, t, b1 + 0.2, "0,5 m", x - 30, y, y + L / 2)
        E.foco(c, t, b1 + 0.3, 0.4, lambda a: E.escreve(c, "0,5 m é o lado", 1000, 380, 66, "g", TINTA, a))
        fcen(c, t, c1, "0,5 × 0,5 = 0,25", 1300, 540, 90)
        E.foco(c, t, c1 + 0.8, 0.5, lambda a: E.pilula(c, "um quarto de m²", 1300, 670, 58, "g", a=a, cor=E.SOBRE))
        if t >= c1 + 0.8:
            for (dx, dy) in ((1, 0), (0, 1), (1, 1)):
                tracejado(c, ret_pts(x + dx * L / 2 + 6, y + dy * L / 2 + 6, L / 2 - 12, L / 2 - 12) + [(x + dx * L / 2 + 6, y + dy * L / 2 + 6)], CINZA, ep(t, c1 + 0.8, 0.4), 4)
    fase(c, t, C["s11"], d1 - 0.1, um)
    if t < d1 - 0.1:
        return
    chao(c, t, d1 - 0.1, tl=[d1, None, None, d1])
    linhas_m(c, QX, QY, 4, 3, QS, ep(t, d1, 0.4))
    pisos(c, t, QX, QY, 8, 6, QS / 2, d1, 1.0, so=lambda k, r: r % 2 == 0)
    for r in range(3):
        c.drawRect(skia.Rect.MakeXYWH(QX, QY + r * QS + QS / 2, QW, QS / 2), M.paint(ERRADO, 0.22 * ep(t, d1 + 1.0, 0.5)))
    E.frase(c, t, d1 + 0.3, ps("2 pisos por m²:", "i", 66) + [("metade vazia", "g", 66, ERRADO)], 1000, 400, "left", 0.1)
    fcen(c, t, e1, "24 pisos", 1300, 620, 110, ERRADO)
    E.frase(c, t, e1 + 0.6, ps("cobrem só", "i", 70) + [("metade do quarto", "g", 70, ERRADO)], 1000, 780, "left", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    x, y, s = 250, 380, 75  # o quarto de novo: 8 por 6 pisos

    def um():
        E.frase(c, t, a2, ps("trabalhe com os", "i", 80, CLARO) + [("lados,", "g", 86, BR)] + ps("não com a área", "i", 80, CLARO),
                W / 2, 210, "center", 0.1)
        E.foco(c, t, C["s12"] + 0.3, 0.5, lambda a: c.drawRect(skia.Rect.MakeXYWH(x, y, 8 * s, 6 * s), M.paint(CLARO, a, stroke=4)))
        pisos(c, t, x, y + 5 * s, 8, 1, s, b2, 0.8, cor=E.COR)
        pisos(c, t, x, y, 1, 5, s, c2, 0.6, cor=CLARO)
        if t >= a3:
            linhas_m(c, x, y, 8, 6, s, ep(t, a3, 0.6), CLARO)
        E.foco(c, t, b2, 0.4, lambda a: E.escreve(c, "comprimento: 4 m → 8 pisos", 960, 420, 56, "g", BR, a))
        E.foco(c, t, c2, 0.4, lambda a: E.escreve(c, "largura: 3 m → 6 pisos", 960, 530, 56, "g", CLARO, a))
        fcen(c, t, d2, "8 × 6 = 48", 1300, 700, 110, BR)
        E.frase(c, t, a3 + 0.3, ps("o chão vira uma", "i", 66, CLARO) + [("grade", "g", 70, BR)], 960, 860, "left", 0.1)
        E.frase(c, t, b3, ps("sem dividir por", "i", 60, CLARO) + [("número com vírgula", "g", 60, BR)], 960, 960, "left", 0.1)
    E.saida(c, t, c3 - 0.1, um)
    if t < c3 - 0.1:
        return
    # quando o piso não cabe exato: 3,2 m com piso de 0,5 m → 6 inteiros e um cortado
    E.frase(c, t, c3, ps("e quando o piso", "i", 76, CLARO) + [("não cabe exato?", "g", 80, BR)], W / 2, 260, "center", 0.1)
    y2, s2 = 480, 200
    E.foco(c, t, c3 + 0.2, 0.5, lambda a: c.drawRect(skia.Rect.MakeXYWH(200, y2, 6.4 * s2, s2), M.paint(CLARO, a, stroke=4)))
    pisos(c, t, 200, y2, 6, 1, s2, c3 + 0.6, 1.2, cor=E.COR)
    q = ep(t, d3, 0.5)
    if q > 0:
        M.rrect(c, 200 + 6 * s2 + 4, y2 + 4, 0.4 * s2 - 8, s2 - 8, 8, CLARO, q)
        tracejado(c, [(200 + 6.4 * s2, y2 - 20), (200 + 6.4 * s2, y2 + s2 + 20)], BR, q, 4)
    E.foco(c, t, d3 + 0.3, 0.5, lambda a: E.pilula(c, "piso cortado", 200 + 6.2 * s2, y2 + s2 + 110, 54, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, d3 + 0.6, ps("o pedaço que sobra", "i", 66, CLARO) + [("também leva piso", "g", 70, BR)], W / 2, 920, "center", 0.1)


# ---------------- questão ----------------
SX, SY, SL = 1200, 500, 440  # a sala quadrada: 6 m


def b_questao(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a4 - 0.6, ps("sala quadrada de", "i", 72), XE, 350, passo=0.1)
    E.foco(c, t, a4 + 0.2, 0.5, lambda a: E.escreve(c, "6 m", XE + 500, 350, 96, "g", COR, a))
    E.frase(c, t, b4, ps("quantas", "i", 72) + [("lajotas de 30 cm?", "g", 72, COR)], XE, 520, passo=0.1)
    E.frase(c, t, c4, ps("quantos metros de", "i", 72) + [("rodapé?", "g", 76, COR)], XE, 680, passo=0.1)
    E.quadrado(c, t, a4, SX, SY, SL, lado="6 m", tl=[a4 + 0.6] * 4, size=56, preenche=0.06)
    E.foco(c, t, b4 + 0.3, 0.5, lambda a: M.rrect(c, SX + 3, SY + 3, SL / 20 - 6, SL / 20 - 6, 4, E.COR, a))
    cerca(c, ret_pts(SX, SY, SL, SL), ease_io(prog(t, c4 + 0.3, 1.2)), postes=False, largura=10)
    E.relogio(c, t, C["s15.a"], 1420, 230, 120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    x, y, L = 200, 300, 600
    s = L / 20
    E.foco(c, t, C["s16"] + 0.1, 0.5, lambda a: (M.rrect(c, x, y, L, L, 4, "#FFFFFF", a), c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(TINTA, a, stroke=4))))
    cota_h(c, t, a6 + 0.6, "600 cm", x, x + L, y - 30)
    apaga = 1 - 0.75 * ep(t, C["s17"], 0.5)  # no rodapé, os pisos ficam claros para o contorno aparecer
    pisos(c, t, x, y, 20, 1, s, b6, 1.0, a=apaga)
    pisos(c, t, x, y + s, 1, 19, s, c6, 0.9, a=apaga)
    pisos(c, t, x + s, y + s, 19, 19, s, d6, 1.2, a=apaga)

    def um():
        E.foco(c, t, a6, 0.5, lambda a: E.pilula(c, "6 m = 600 cm", 1360, 300, 60, "g", fundo=TINTA, a=a, cor=BR))
        fcen(c, t, b6, "600 ÷ 30 = 20", 1360, 470, 92)
        E.foco(c, t, b6 + 0.6, 0.4, lambda a: centro(c, "lajotas por fileira", 1360, 545, 46, "i", TINTA2, a))
        E.foco(c, t, c6, 0.4, lambda a: centro(c, "20 fileiras", 1360, 650, 64, "g", TINTA, a))
        fcen(c, t, d6, "20 × 20 = 400", 1360, 790, 92)
        bola_res(c, t, d6 + 1.0, "400", 1300, 955, 95, 64)
        E.foco(c, t, d6 + 1.2, 0.4, lambda a: E.escreve(c, "lajotas", 1420, 978, 60, "i", TINTA, a))
    E.saida(c, t, C["s17"] - 0.1, um)
    if t < C["s17"]:
        return
    cerca(c, ret_pts(x, y, L, L), ease_io(prog(t, a7, 1.2)), largura=12)
    E.frase(c, t, a7, ps("rodapé =", "i", 70) + [("o contorno", "g", 76, COR)], 1000, 300, "left", 0.1)
    fcen(c, t, b7, "6 × 4 = 24", 1360, 480, 100)
    bola_res(c, t, b7 + 1.0, "24 m", 1360, 650, 110, 66)
    E.foco(c, t, c7, 0.5, lambda a: E.pilula(c, "piso → área", 1360, 830, 60, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, d7, 0.5, lambda a: E.pilula(c, "rodapé → perímetro", 1360, 950, 60, "g", fundo=TINTA, a=a, cor=BR))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s18.a", "retângulo:", "A = b · h"), ("s18.b", "quadrado:", "A = ℓ²"), ("s18.c", "pisos:", "quantos cabem em cada lado"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 410 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a), centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 80) + [(l2, "g", 80, COR)], 360, y, "left", 0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a9, [("paralelogramo", "g", 110, COR)], XE, 400, passo=0.12)
    E.frase(c, t, a9 + 1.0, ps("vira retângulo", "i", 84), XE, 520, passo=0.12)
    E.frase(c, t, b9, [("triângulo", "g", 96, COR)] + ps("= metade", "i", 84), XE, 680, passo=0.12)
    E.paralelogramo(c, t, a9 + 0.3, 1150, 240, 420, 260, 140, preenche=0.12)
    E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c9 + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1580, p), lerp(970, 785, p), ep(t, c9 + 0.2, 0.4))
    E.frase(c, t, d9, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, contar=b_contar, quadrado=b_quadrado, pisos=b_pisos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
