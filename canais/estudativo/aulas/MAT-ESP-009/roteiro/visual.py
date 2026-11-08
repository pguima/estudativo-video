"""Visual — Estudativo · MAT-ESP-009: encher um recipiente, nível, vazão e tempo.
Mesma linguagem da trilha (MAT-ESP-001 a 008): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
resposta na esfera.
- ÁGUA = o prisma translúcido que sobe (agua(), de MAT-ESP-005) ou o cilindro translúcido (agua_cil()); o nível que a fala
  pergunta ganha a cota marca() à direita, com a altura escrita. O fundo pintado (piso()) é a área que divide.
- VAZÃO = a torneira() com o fio d'água caindo até a superfície e a vazão escrita numa pílula.
- Converter = a ESCADA da trilha Medidas (classe Escada e num_un, de MAT-MED-005 via MAT-ESP-005): cm → dm com a bolinha que pula;
  litros → m³ com a vírgula que anda três casas.
- Atalho (palco escuro): a caixa em contorno branco dividida em quartos iguais de tempo e de altura.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-009_encher_um_recipiente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("camada", "aquario", "caixa", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PI = 3
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))  # a inclinação de E.cilindro
assert 6 * 3 == 18 and 9 / 18 == 0.5 and 0.5 * 10 == 5 and 2 * 1.5 == 3 and 3 * 1 == 3 and 3 * 1000 == 3000 and 3000 / 25 == 120
assert 30 * 25 == 750 and 750 / 1000 == 0.75 and 0.75 / 3 == 0.25 and 750 / 3 == 250 and 30 / 120 == 0.25
assert PI * 1 ** 2 == 3 and 60 * 30 == 1800 and abs(1.8 / 3 - 0.6) < 1e-9 and 3 * 1.5 == 4.5 and 4500 / 30 == 150 and 150 / 60 == 2.5


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)



# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ² ou ³ vai na grotesca: a serifada não tem o expoente)"""
    return [(w, "g" if any(ch in w for ch in "²³√") else est, size * (0.92 if any(ch in w for ch in "²³√") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def face(c, pts, idx, a=1.0, cor=None, alfa_=0.42):
    if a <= 0:
        return
    p = skia.Path(); p.addPoly([pts[i] for i in idx], True)
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.5, tracejada=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def reto(c, P, A, B, k=34, a=1.0, cor=None):
    """quadradinho de ângulo reto no vértice P, nas direções de P→A e P→B"""
    if a <= 0:
        return
    def un(Q):
        dx, dy = Q[0] - P[0], Q[1] - P[1]
        n = math.hypot(dx, dy) or 1
        return dx / n * k, dy / n * k
    u, v = un(A), un(B)
    path = skia.Path()
    path.moveTo(P[0] + u[0], P[1] + u[1]); path.lineTo(P[0] + u[0] + v[0], P[1] + u[1] + v[1]); path.lineTo(P[0] + v[0], P[1] + v[1])
    c.drawPath(path, M.paint(cor or TINTA, a, stroke=4))


def rotulo(c, t, t0, s, P, Q, n, size=56, cor=None, gap=20):
    """rótulo de um segmento PQ, afastado na direção n"""
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, n[0], n[1], gap, size, "g", cor or COR, a))


# ---------------- cubinhos ----------------
KX, KY = 0.394, -0.308  # a profundidade na perspectiva cavaleira (a mesma de E.paralelepipedo)


def cubinho(c, x, y, s, a=1.0, cor=None):
    """cubinho cheio de aresta s: (x, y) = canto de baixo à esquerda da face da frente"""
    if a <= 0:
        return
    cor = cor or E.COR
    dx, dy = KX * s, KY * s
    br = M.paint("#FFFFFF", 0.9 * a, stroke=2)

    def poli(pts, tinta):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(tinta, a)); c.drawPath(p, br)
    poli([(x, y - s), (x + s, y - s), (x + s + dx, y - s + dy), (x + dx, y - s + dy)], E.mix(cor, "#FFFFFF", 0.35))
    poli([(x + s, y), (x + s + dx, y + dy), (x + s + dx, y - s + dy), (x + s, y - s)], E.mix(cor, "#000000", 0.25))
    poli([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], cor)


def enche(c, t, cols, fil, cam, x, y, s, tf, a=1.0, cor=None):
    """cubinhos de aresta s enchendo uma caixa cols x fil x cam: tf(camada, fileira) = instante da fileira (None = não entra).
    (x, y) = canto de baixo à esquerda da frente; a fileira 0 é a da FRENTE. cor(i, j, k) pode trocar a cor de um cubinho"""
    if a <= 0:
        return
    for k in range(cam):
        for j in reversed(range(fil)):  # do fundo para a frente
            t0 = tf(k, j)
            if t0 is None:
                continue
            for i in range(cols):
                q = ep(t, t0 + 0.08 * i, 0.35)
                if q <= 0:
                    continue
                cx = x + i * s + KX * s * j
                cy = y - k * s + KY * s * j - (1 - ease_io(q)) * 40
                cubinho(c, cx, cy, s, a * q, cor(i, j, k) if callable(cor) else cor)


def arame(c, x, y, w, d, h, a=1.0, cor=None):
    """contorno de uma caixa w x d x h (px) na mesma perspectiva, com as arestas de trás tracejadas"""
    if a <= 0:
        return
    dx, dy = KX * d, KY * d
    pt = M.paint(cor or TINTA, a, stroke=4)
    tr = M.paint(cor or TINTA2, 0.7 * a, stroke=3)
    tr.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
    c.drawLine(x, y, x + dx, y + dy, tr); c.drawLine(x + dx, y + dy, x + w + dx, y + dy, tr); c.drawLine(x + dx, y + dy, x + dx, y + dy - h, tr)
    for (x0, y0, x1, y1) in ((x, y, x + w, y), (x + w, y, x + w, y - h), (x + w, y - h, x, y - h), (x, y - h, x, y),
                             (x, y - h, x + dx, y - h + dy), (x + w, y - h, x + w + dx, y - h + dy), (x + w, y, x + w + dx, y + dy),
                             (x + dx, y - h + dy, x + w + dx, y - h + dy), (x + w + dx, y - h + dy, x + w + dx, y + dy)):
        c.drawLine(x0, y0, x1, y1, pt)


def piso(c, x, y, w, d, a=1.0, cor=None, grade=None):
    """o fundo da caixa pintado (a área da base); grade = (colunas, fileiras) desenha os quadradinhos de 1 m²"""
    if a <= 0:
        return
    dx, dy = KX * d, KY * d
    p = skia.Path(); p.addPoly([(x, y), (x + w, y), (x + w + dx, y + dy), (x + dx, y + dy)], True)
    c.drawPath(p, M.paint(cor or E.COR, 0.35 * a))
    if grade:
        n, m = grade
        for i in range(1, n):
            M.line(c, x + w * i / n, y, x + w * i / n + dx, y + dy, "#FFFFFF", a, 3)
        for j in range(1, m):
            M.line(c, x + dx * j / m, y + dy * j / m, x + w + dx * j / m, y + dy * j / m, "#FFFFFF", a, 3)


def agua(c, x, y, w, d, h, nivel, a=1.0):
    """água até a fração nivel da altura h, dentro da caixa"""
    if a <= 0 or nivel <= 0:
        return
    dx, dy = KX * d, KY * d
    hh = h * nivel
    cor = E.mix(E.COR, "#FFFFFF", 0.45)
    for pts, al in (([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + dy - hh), (x + w, y - hh)], 0.42),
                    ([(x, y - hh), (x + w, y - hh), (x + w + dx, y - hh + dy), (x + dx, y - hh + dy)], 0.55),
                    ([(x, y), (x + w, y), (x + w, y - hh), (x, y - hh)], 0.38)):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(cor, al * a))

# ================= a ESCADA das unidades (copiada de MAT-MED-005: a mesma peça da trilha Medidas e Unidades) =================
UN = ("km", "hm", "dam", "m", "dm", "cm", "mm")
NOMES = ("quilômetro", "hectômetro", "decâmetro", "metro", "decímetro", "centímetro", "milímetro")


class Escada:
    """degraus descendo da esquerda para a direita. (x, y) = canto de cima do 1º degrau; sw, sh = largura e altura do degrau.
    base = onde todos os degraus apoiam. meio = índice da unidade principal (degrau cheio da cor da matéria)."""

    def __init__(s, x=110, y=300, sw=186, sh=78, base=950, un=UN, nomes=NOMES, meio=3, size=60):
        s.x, s.y, s.sw, s.sh, s.base, s.un, s.nomes, s.meio, s.size = x, y, sw, sh, base, un, nomes, meio, size
        s.n = len(un)

    def cx(s, i):
        return s.x + (i + 0.5) * s.sw

    def topo(s, i):
        return s.y + i * s.sh

    def ponto(s, i):
        """onde a bolinha fica em cima do degrau i (i pode ser fracionário)"""
        k = min(max(i, 0), s.n - 1)
        return s.cx(k), s.y + k * s.sh - 34

    def degraus(s, c, t, td, tl=None, a=1.0, acesos=(), ta=None, escuro=False, nomes=True):
        """td = instante de entrada de cada degrau (lista) ou do primeiro (número: entram em fila).
        tl = instante do rótulo de cada degrau (lista; padrão = o do degrau). acesos = degraus do caminho, em tom claro, a partir de ta."""
        if a <= 0:
            return
        for i in range(s.n):
            ti = td[i] if isinstance(td, (list, tuple)) else td + 0.09 * i
            q = ep(t, ti, 0.45)
            if q <= 0:
                continue
            top, x0 = s.topo(i), s.x + i * s.sw
            hh = (s.base - top) * ease_io(prog(t, ti, 0.45))
            meio = i == s.meio
            if s.un[i] == "":  # degrau sem nome: só o contorno tracejado
                r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 4, s.base - hh, s.sw - 8, hh), 12, 12)
                pt = M.paint(CLARO if escuro else TINTA2, 0.55 * q * a, stroke=3)
                pt.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
                c.drawRRect(r, pt)
                continue
            if escuro:
                fundo, borda, tinta = (E.COR, CLARO, BR) if meio else ("#FFFFFF", CLARO, BR)
                alfa = 1.0 if meio else 0.07
            else:
                fundo, borda, tinta = (E.COR, E.COR, E.SOBRE) if meio else ("#FFFFFF", TINTA2, TINTA)
                alfa = 1.0
            acende = ep(t, ta, 0.4) if (i in acesos and ta is not None and not meio) else 0.0
            M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, fundo, alfa * q * a)
            if acende > 0:
                M.rrect(c, x0 + 4, s.base - hh, s.sw - 8, hh, 12, E.COR, (0.32 if escuro else 0.16) * acende * q * a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 4, s.base - hh, s.sw - 8, hh), 12, 12), M.paint(borda, q * a, stroke=3))
            tli = tl[i] if tl else ti + 0.2
            E.foco(c, t, tli, 0.45, lambda b, i=i, top=top, tinta=tinta: centro(c, s.un[i], s.cx(i), top + s.size * 1.12, s.size, "g", tinta, b * a))
            if nomes:
                cor_n = (BR if meio else CLARO) if escuro else (E.SOBRE if meio else TINTA2)
                E.foco(c, t, tli + 0.1, 0.45, lambda b, i=i, top=top, cor_n=cor_n: centro(c, s.nomes[i], s.cx(i), top + s.size * 1.12 + 50, 40, "i", cor_n, b * a))

    def pulos(s, c, t, i0, hops, t0, a=1.0, cor=None, dur=0.7, rastro=True, escuro=False):
        """bolinha que aparece no degrau i0 em t0 e pula: hops = [(instante, degrau de destino), ...].
        Cada pulo deixa um arco com o número dele (1, 2, 3...): é a contagem de degraus = casas da vírgula."""
        if a <= 0 or t < t0:
            return
        cor = cor or E.COR
        atual, pulo = float(i0), 0.0
        de = i0
        for k, (th, j) in enumerate(hops):
            q = prog(t, th, dur)
            if q <= 0:
                break
            if rastro:
                s._arco(c, de, j, min(1.0, q * 1.25), k + 1, cor, a, escuro)
            if q < 1:
                e = ease_io(q)
                atual, pulo = lerp(de, j, e), math.sin(math.pi * q) * 70
                break
            atual, de = float(j), j
        x0, y0 = s.ponto(math.floor(atual))
        x1, y1 = s.ponto(math.ceil(atual))
        f = atual - math.floor(atual)
        E.bola(c, lerp(x0, x1, f), lerp(y0, y1, f) - pulo, 30 * ease_back(prog(t, t0, 0.5)), cor, a)

    def _arco(s, c, i, j, p, k, cor, a, escuro):
        (xa, ya), (xb, yb) = s.ponto(i), s.ponto(j)
        ya, yb = ya - 36, yb - 36
        alto = 64
        mx, my = (xa + xb) / 2, min(ya, yb) - alto
        pts = [(lerp(lerp(xa, mx, u), lerp(mx, xb, u), u), lerp(lerp(ya, my, u), lerp(my, yb, u), u)) for u in [p * n / 24 for n in range(25)]]
        path = skia.Path()
        path.moveTo(*pts[0])
        for x_, y_ in pts[1:]:
            path.lineTo(x_, y_)
        tinta = CLARO if escuro else cor
        c.drawPath(path, M.paint(tinta, 0.75 * a, stroke=5, cap_round=True))
        if p >= 1:
            (xp, yp), (xe, ye) = pts[-2], pts[-1]
            ang = math.atan2(ye - yp, xe - xp)
            h = skia.Path()
            h.moveTo(xe + math.cos(ang) * 3, ye + math.sin(ang) * 3)
            h.lineTo(xe - 18 * math.cos(ang - 0.5), ye - 18 * math.sin(ang - 0.5))
            h.lineTo(xe - 18 * math.cos(ang + 0.5), ye - 18 * math.sin(ang + 0.5))
            h.close()
            c.drawPath(h, M.paint(tinta, 0.75 * a))
            xm, ym = pts[12]
            c.drawCircle(xm, ym - 4, 24, M.paint(tinta, a))
            centro(c, str(k), xm, ym + 11, 32, "g", "#07070F" if escuro else E.SOBRE, a)


def posicao(t, pos, saltos, dur=0.7):
    """posição da vírgula no instante t (a mesma conta de E.anda)"""
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


def num_un(c, t, dig, pos, saltos, x, y, size, unidades, cor=None, tv=None, some=False, t0=None, cor_un=None, zero_esq=False, cor_novo=None):
    """número com a vírgula que anda (E.anda) e a unidade logo depois dele, que troca a cada salto.
    unidades = [(instante, "km"), ...]; a primeira entra em t0. Devolve px (centro de cada casa).
    zero_esq = o 0 antes da vírgula de "0,3" (dig "3", pos 0), que some quando a vírgula começa a andar."""
    if t0 is not None and t < t0:
        return None
    a0 = ep(t, t0, 0.5) if t0 is not None else 1.0
    c.saveLayer(None, M.paint("#000000", a0)) if a0 < 1 else None
    px = E.anda(c, t, dig, pos, saltos, x, y, size, cor=cor, tv=tv, some=some, cor_novo=cor_novo, cor_v=cor_novo)
    cl = E.casa(size)
    if zero_esq:
        z = 1 - ep(t, saltos[0][0], 0.3) if saltos else 1.0
        if z > 0:
            E.centro(c, "0", px(-1), y, size, "g", cor or TINTA, z)
    ncas = max(len(dig), math.ceil(posicao(t, pos, saltos) - 1e-6))
    xu = x + ncas * cl + size * 0.3
    for k, (tu, u) in enumerate(unidades):
        prox = unidades[k + 1][0] if k + 1 < len(unidades) else None
        if t < tu:
            break
        if prox is not None and t >= prox + 0.35:
            continue
        sai = 1 - ep(t, prox, 0.35) if prox is not None else 1.0
        E.foco(c, t, tu, 0.4, lambda b, u=u: E.escreve(c, u, xu, y, size * 0.72, "g", cor_un or COR, b * sai))
    if a0 < 1:
        c.restore()
    return px



# ================= peças desta aula =================
def agua_cil(c, cx, cy, r, h, nivel, a=1.0):
    """água até a fração nivel da altura h (px) dentro de um E.cilindro de base em (cx, cy)"""
    if a <= 0 or nivel <= 0:
        return
    ry, ct = r * SEN, cy - h * nivel * COS
    cor = E.mix(E.COR, "#FFFFFF", 0.45)
    p = skia.Path()
    p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, ct)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    c.drawPath(p, M.paint(cor, 0.45 * a))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), M.paint(cor, 0.6 * a))


def marca(c, t, t0, x, y0, y1, rot, cor=None, size=52, a=1.0):
    """cota vertical de y0 (embaixo) até y1 (em cima), com a medida à direita"""
    p = ease_io(prog(t, t0, 0.5))
    if p <= 0 or a <= 0:
        return
    cor = cor or E.COR
    yy = lerp(y0, y1, p)
    M.line(c, x, y0, x, yy, cor, a, 5)
    for y_ in (y0, yy):
        M.line(c, x - 14, y_, x + 14, y_, cor, a, 5)
    E.foco(c, t, t0 + 0.3, 0.4, lambda q: E.escreve(c, rot, x + 26, (y0 + y1) / 2 + size * 0.36, size, "g", cor, q * a))


def torneira(c, t, t0, x, y, y_fim, vazao=None, a=1.0, cor=None, escuro=False):
    """a torneira com a boca em (x, y) e o fio d'água caindo até y_fim; vazao = texto da pílula"""
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    tinta = BR if escuro else TINTA
    M.rrect(c, x - 150, y - 46, 160, 30, 8, E.mix(TINTA2, "#FFFFFF", 0.3), q)
    M.rrect(c, x - 16, y - 46, 32, 46, 6, E.mix(TINTA2, "#FFFFFF", 0.3), q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 150, y - 46, 160, 30), 8, 8), M.paint(tinta, q, stroke=3))
    f = ease_io(prog(t, t0 + 0.3, 0.5))
    if f > 0:
        c.drawRect(skia.Rect.MakeXYWH(x - 7, y, 14, (y_fim - y) * f), M.paint(cor or E.mix(E.COR, "#FFFFFF", 0.35), 0.8 * q))
    if vazao:
        E.foco(c, t, t0 + 0.4, 0.4, lambda b: E.pilula(c, vazao, x - 330, y - 30, 50, "g", a=b * a, cor=E.SOBRE))


def caixa(c, t, t0, x, y, w, d, h, medidas=(None, None, None), tm=None, size=54):
    return E.paralelepipedo(c, t, t0, x, y, w, d, h, medidas, size=size, tm=tm)


AX, AY, AW, AD, AH = 200, 880, 600, 300, 400   # o aquário: 60 x 30 cm de fundo (10 px por cm), 40 cm de altura
GX, GY, GA, GB, GH = 260, 880, 440, 330, 220   # a caixa-d'água: 2 m x 1,5 m x 1 m (220 px por metro)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        caixa(c, t, a1, AX, AY, AW, AD, AH, ("60 cm", "30 cm", None), tm=a1 + 0.8)
        agua(c, AX, AY, AW, AD, AH, 0.125 * ease_io(prog(t, b1 + 0.5, 1.5)))
        torneira(c, t, b1, AX + AW / 2 + 60, 250, AY - 60, "9 L", a=1 - ep(t, b1 + 2.2, 0.4))
        E.frase(c, t, a1 + 0.3, [("aquário", "g", 76, COR)], 1080, 260, "left", 0.1)
        E.frase(c, t, a1 + 1.0, ps("fundo de 60 por 30 cm", "i", 60), 1080, 350, "left", 0.1)
        E.frase(c, t, b1, ps("um balde de", "i", 66) + [("9 litros", "g", 70, COR)], 1080, 490, "left", 0.1)
        E.frase(c, t, c1, ps("quanto o", "i", 70) + [("nível sobe?", "g", 74, COR)], 1080, 630, "left", 0.1)
        marca(c, t, c1 + 0.4, AX + AW + KX * AD + 40, AY + KY * AD, AY + KY * AD - 0.125 * AH, "?" if t < d1 else "5 cm", size=50)
        bola_txt(c, t, d1, "5 cm", 1300, 840, 110, 60)
        E.frase(c, t, d1 + 0.8, ps("uma", "i", 60) + [("divisão", "g", 62, COR)] + ps("só", "i", 60), 1300, 1020, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.2), ps("quanto o", "i", 90) + [("nível sobe", "g", 100, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("e em quanto", "i", 90) + [("tempo", "g", 100, COR)], XE, 600, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.65), ps("o recipiente enche", "i", 90), XE, 740, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "prisma e cilindro: volume =", "área da base × altura"), ("s03.c", "1 dm³ = 1 L", "1 m³ = 1.000 L"),
             ("s03.d", "tempo =", "volume ÷ vazão"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 80, "left", 0.1)
        E.frase(c, t, C[k] + 0.6, [(l2, "g", 60, COR)], x + 44, y + 162)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- a camada de água ----------------
def b_camada(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s04.{k}"] for k in "abcde")
    a5, b5 = C["s05.a"], C["s05.b"]
    x, y, w, d, h = 200, 900, 560, 340, 380
    arame(c, x, y, w, d, h, ep(t, C["s04"], 0.5))
    piso(c, x, y, w, d, ep(t, b4, 0.5))
    nv = 0.22
    agua(c, x, y, w, d, h, nv * ease_io(prog(t, a4, 1.2)))
    xm = x + w + KX * d + 40
    if e4 <= t < C["s05"] + 0.4:
        marca(c, t, e4, xm, y + KY * d, y + KY * d - nv * h, "?", size=56)
    X = 1350

    def ideia():
        E.frase(c, t, a4, ps("a água forma uma", "i", 62) + [("camada", "g", 66, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b4, ps("com a", "i", 62) + [("forma do fundo", "g", 66, COR)], X, 340, "center", 0.1)
        fcen(c, t, c4, "V = área do fundo × altura", X, 500, 60)
        E.frase(c, t, d4, [("V:", "g", 62, COR)] + ps("conhecido", "i", 62), X - 220, 660, "center", 0.1)
        E.frase(c, t, e4, [("altura:", "g", 62, COR)] + ps("o que falta", "i", 62), X + 180, 660, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, ideia)
    if t < C["s05"] - 0.1:
        return
    E.frase(c, t, C["s05"] + 0.2, ps("isolando a altura", "i", 62), X, 230, "center", 0.1)
    fcen(c, t, a5, "nível sobe = f{volume}{área do fundo}", X, 440, 70, COR)
    E.foco(c, t, b5, 0.5, lambda q: E.pilula(c, "tudo na mesma unidade", X, 720, 62, "g", a=q, cor=E.SOBRE))
    E.frase(c, t, b5 + 0.6, ps("antes de dividir", "i", 56, TINTA2), X, 850, "center", 0.1)


# ---------------- o aquário ----------------
ESC_A = Escada(x=120, y=360, sw=220, sh=120, base=820, un=("m", "dm", "cm"), nomes=("metro", "decímetro", "centímetro"), meio=1, size=64)
QX, QY, QW, QD, QH = 170, 900, 480, 240, 320   # o aquário menor (8 px por cm)


def b_aquario(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]

    def fundo():
        E.frase(c, t, C["s06"] + 0.2, ps("no aquário:", "i", 66) + [("tudo em decímetros", "g", 66, COR)], W / 2, 180, "center", 0.1)
        ESC_A.degraus(c, t, a6 - 0.2, acesos=(1, 2), ta=a6 + 0.4)
        ESC_A.pulos(c, t, 2, [(b6 - 0.2, 1)], a6 + 0.4)
        E.foco(c, t, b6 + 0.5, 0.4, lambda q: centro(c, "← 1 casa", ESC_A.cx(1.5), 900, 56, "g", COR, q))
        for k, (de, para, tk) in enumerate((("60", "6", b6), ("30", "3", c6))):
            y = 420 + 140 * k
            E.saida(c, t, tk + 0.6, lambda de=de, tk=tk, y=y: E.foco(c, t, tk - 0.2, 0.4, lambda q: E.escreve(c, de + " cm", 900, y, 80, "g", TINTA2, q)))
            E.foco(c, t, tk + 0.6, 0.4, lambda q, para=para, y=y: E.escreve(c, para + " dm", 900, y, 80, "g", COR, q))
        fcen(c, t, d6, "6 × 3 = 18 dm²", 1520, 640, 84)
        E.frase(c, t, d6 + 0.8, ps("de fundo", "i", 56, TINTA2), 1520, 730, "center", 0.1)
    fase(c, t, C["s06"], C["s07"] - 0.1, fundo)
    if t < C["s07"] - 0.1:
        return
    caixa(c, t, C["s07"], QX, QY, QW, QD, QH, ("6 dm", "3 dm", None), tm=C["s07"] + 0.3)
    piso(c, QX, QY, QW, QD, ep(t, C["s07"] + 0.4, 0.5) * (1 - ep(t, b7 + 0.8, 0.4)))
    agua(c, QX, QY, QW, QD, QH, 0.125 * ease_io(prog(t, a7 + 0.4, max(0.8, b7 - a7))))
    if t >= c7:
        marca(c, t, c7, QX + QW + KX * QD + 36, QY + KY * QD, QY + KY * QD - 0.125 * QH, "5 cm", size=48)
    X = 1330
    fcen(c, t, a7, "9 L = 9 dm³", X, 260, 80)
    fcen(c, t, b7, "f{9}{18} = 0,5 dm", X, 460, 84, COR)
    fcen(c, t, c7, "0,5 dm = 5 cm", X - 150, 720, 70)
    E.frase(c, t, c7 + 0.5, ps("meio decímetro", "i", 50, TINTA2), X - 150, 800, "center", 0.1)
    bola_txt(c, t, c7 + 0.9, "5 cm", X + 290, 720, 110, 60)


# ---------------- a caixa-d'água: tempo para encher ----------------
def b_caixa(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    caixa(c, t, C["s08"], GX, GY, GA, GB, GH)
    E.foco(c, t, a8, 0.4, lambda q: centro(c, "2 m", GX + GA / 2, GY + 64, 52, "g", COR, q))
    E.foco(c, t, a8 + 0.5, 0.4, lambda q: E.escreve(c, "1,5 m", GX + GA + KX * GB / 2 + 24, GY + KY * GB / 2 + 30, 52, "g", COR, q))
    E.foco(c, t, b8, 0.4, lambda q: E.escreve(c, "1 m", GX - 120, GY - GH / 2 + 18, 52, "g", COR, q))
    piso(c, GX, GY, GB * 0 + GA, GB, ep(t, a9, 0.5) * (1 - ep(t, b9, 0.4)))
    nivel = ease_io(prog(t, d9, max(1.0, e9 - d9)))
    agua(c, GX, GY, GA, GB, GH, nivel)
    sup = GY + KY * GB / 2 - GH * nivel
    torneira(c, t, c8, GX + GA / 2 + KX * GB / 2, 200, sup, "25 L/min")
    X = 1360

    def pergunta():
        E.frase(c, t, C["s08"] + 0.2, ps("a", "i", 66) + [("caixa-d'água", "g", 70, COR)] + ps("vazia", "i", 66), X, 260, "center", 0.1)
        E.frase(c, t, d8, ps("em quanto", "i", 70) + [("tempo", "g", 74, COR)] + ps("enche?", "i", 70), X, 640, "center", 0.1)
    fase(c, t, C["s08"], C["s09"] - 0.1, pergunta)
    if t < C["s09"] - 0.1:
        return
    fcen(c, t, a9, "2 × 1,5 = 3 m²", X, 220, 66)
    fcen(c, t, b9, "3 × 1 = 3 m³", X, 340, 66)
    fcen(c, t, c9, "= 3.000 L", X, 450, 66, TINTA2)
    E.frase(c, t, d9, ps("tempo =", "i", 56) + [("volume ÷ vazão", "g", 56)], X, 600, "center", 0.1)
    fcen(c, t, d9 + 0.4, "3.000 ÷ 25 = 120 min", X, 720, 70, COR)
    bola_txt(c, t, e9, "2 h", X, 900, 100, 70)


# ---------------- o nível depois de meia hora ----------------
def b_nivel(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    caixa(c, t, C["s10"] - 1, GX, GY, GA, GB, GH)
    E.foco(c, t, C["s10"] - 1, 0.1, lambda q: (centro(c, "2 m", GX + GA / 2, GY + 64, 52, "g", COR, q),
                                              E.escreve(c, "1,5 m", GX + GA + KX * GB / 2 + 24, GY + KY * GB / 2 + 30, 52, "g", COR, q),
                                              E.escreve(c, "1 m", GX - 120, GY - GH / 2 + 18, 52, "g", COR, q)))
    nv = 1 - ep(t, C["s10"], 0.6) if t < a0 else 0.25 * ease_io(prog(t, a0 + 0.3, max(1.0, b0 - a0)))
    agua(c, GX, GY, GA, GB, GH, nv)
    if t >= e0:
        marca(c, t, e0, GX + GA + KX * GB + 40, GY + KY * GB, GY + KY * GB - 0.25 * GH, "25 cm", size=50)
    X = 1360
    E.frase(c, t, a0, ps("depois de", "i", 66) + [("meia hora?", "g", 70, COR)], X, 230, "center", 0.1)
    fcen(c, t, b0, "30 × 25 = 750 L", X, 380, 74)
    fcen(c, t, c0, "= 0,75 m³", X, 500, 74, TINTA2)
    fcen(c, t, d0, "0,75 ÷ 3 = 0,25 m", X, 660, 74, COR)
    bola_txt(c, t, e0, "25 cm", X, 860, 115, 56)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    x, y, w, d, h = 200, 900, 330, 250, 165   # a caixa de 1 m, menor
    caixa(c, t, C["s11"], x, y, w, d, h)
    E.foco(c, t, C["s11"] + 0.5, 0.4, lambda q: E.escreve(c, "1 m", x - 100, y - h / 2 + 18, 48, "g", TINTA2, q))
    if t >= c1:
        p = ease_io(prog(t, c1, 0.9))
        xs = x + w / 2 + KX * d / 2
        y0 = y - h + KY * d / 2
        M.line(c, xs, y0, xs, lerp(y0, 150, p), ERRADO, 1, 8)
        if p >= 1:
            h_ = skia.Path(); h_.moveTo(xs, 120); h_.lineTo(xs - 22, 160); h_.lineTo(xs + 22, 160); h_.close()
            c.drawPath(h_, M.paint(ERRADO))
        E.foco(c, t, c1 + 0.6, 0.4, lambda q: E.escreve(c, "250 m?!", xs + 30, 250, 66, "g", ERRADO, q))
    X = 1250
    E.frase(c, t, C["s11"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 180, "center", 0.1)
    E.frase(c, t, a1, ps("dividir", "i", 62) + [("litros", "g", 66, ERRADO)] + ps("por", "i", 62) + [("m²", "g", 66, ERRADO)], X, 280, "center", 0.1)

    def errado():
        fcen(c, t, b1, "750 ÷ 3 = 250", X, 430, 80, ERRADO)
        E.frase(c, t, c1, ps("numa caixa de", "i", 58) + [("1 m", "g", 62)] + ps("de altura!", "i", 58), X, 550, "center", 0.1)
    fase(c, t, b1, d1 - 0.1, errado)
    if t >= d1 - 0.1:
        E.frase(c, t, d1, ps("passe para", "i", 60) + [("m³", "g", 64, COR)] + ps("antes:", "i", 60), X, 450, "center", 0.1)
        num_un(c, t, "750", 3, [(d1 + 1.6, 0)], X - 260, 650, 120, [(d1 + 0.6, "L"), (d1 + 2.4, "m³")], t0=d1 + 0.6, cor_novo=COR)
        E.foco(c, t, d1 + 2.4, 0.4, lambda q: centro(c, "3 casas para a esquerda", X, 800, 56, "g", COR, q))
        E.frase(c, t, d1 + 3.0, ps("750 L =", "i", 56) + [("0,75 m³", "g", 60, COR)], X, 920, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def quartos(c, t, t0, x, y, w, h, nivel, rot=None, a=1.0):
    """a caixa de frente em contorno branco, com as marcas dos quartos e a água até nivel"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    if nivel > 0:
        c.drawRect(skia.Rect.MakeXYWH(x, y - h * nivel, w, h * nivel), M.paint(E.COR, 0.75 * q))
        c.drawRect(skia.Rect.MakeXYWH(x, y - h * nivel, w, 6), M.paint(CLARO, q))
    c.drawRect(skia.Rect.MakeXYWH(x, y - h, w, h), M.paint(BR, q, stroke=5))
    for k in range(1, 4):
        pt = M.paint(CLARO, 0.7 * q, stroke=3)
        pt.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
        c.drawLine(x, y - h * k / 4, x + w, y - h * k / 4, pt)
        if rot:
            E.centro(c, rot[k - 1], x - 90, y - h * k / 4 + 16, 40, "g", CLARO, q)
    if rot:
        E.centro(c, rot[3], x - 90, y - h + 16, 40, "g", BR, q)


def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]

    def um():
        E.frase(c, t, C["s12"] + 0.2, ps("o", "i", 70, CLARO) + [("atalho", "g", 74, BR)], W / 2, 180, "center", 0.1)
        E.frase(c, t, a2, ps("paredes retas e", "i", 58, CLARO) + [("vazão constante", "g", 62, BR)], W / 2, 280, "center", 0.1)
        x, y, w, h = 400, 960, 300, 560
        if t < c2:  # vazão constante: o nível sobe em linha reta até cheio
            nivel = prog(t, b2, max(1.0, c2 - b2 - 0.3))
        else:  # e volta ao primeiro quarto: meia hora
            nivel = lerp(1.0, 0.25, ease_io(prog(t, c2, 0.8)))
        quartos(c, t, a2 + 0.3, x, y, w, h, nivel, ("30 min", "1 h", "1h30", "2 h"))
        E.frase(c, t, b2, ps("o nível sobe", "i", 58, CLARO) + [("o mesmo tanto", "g", 62, BR)] + ps("a cada minuto", "i", 58, CLARO), 1250, 440, "center", 0.1)
        fcen(c, t, c2, "30 min = f{1}{4} de 2 h", 1250, 620, 76, BR)
        fcen(c, t, d2, "f{1}{4} de 1 m = 25 cm", 1250, 820, 76, CLARO)
        E.frase(c, t, d2 + 1.2, ps("sem converter nada", "i", 56, CLARO), 1250, 960, "center", 0.1)
    fase(c, t, C["s12"], C["s13"] - 0.1, um)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, C["s13"] + 0.2, ps("funciona porque", "i", 66, CLARO), W / 2, 180, "center", 0.1)
    E.frase(c, t, a3, ps("cada cm de altura guarda o", "i", 58, CLARO) + [("mesmo volume", "g", 62, BR)], W / 2, 280, "center", 0.1)
    x, y, w, h = 300, 900, 300, 440
    q = ep(t, a3, 0.5)
    if q > 0:
        for k in range(5):
            qk = ep(t, a3 + 0.25 * k, 0.4)
            c.drawRect(skia.Rect.MakeXYWH(x, y - h * (k + 1) / 5 + 6, w, h / 5 - 12), M.paint(E.COR, 0.7 * qk))
        c.drawRect(skia.Rect.MakeXYWH(x, y - h, w, h), M.paint(BR, q, stroke=5))
        E.foco(c, t, a3 + 1.2, 0.4, lambda b_: centro(c, "fundo igual", x + w / 2, y + 70, 48, "g", CLARO, b_))
    # o funil: alarga para cima
    fx, fy = 1300, 900
    qf = ep(t, b3, 0.5)
    if qf > 0:
        nv = ease_io(prog(t, b3 + 0.5, 2.0))
        hh = 440
        top = 300
        ytop = fy - hh
        yl = fy - hh * 0.35 * nv
        wl = lerp(30, top, 0.35 * nv)
        p = skia.Path(); p.moveTo(fx - 30, fy); p.lineTo(fx + 30, fy); p.lineTo(fx + wl, yl); p.lineTo(fx - wl, yl); p.close()
        c.drawPath(p, M.paint(E.COR, 0.75 * qf))
        g = skia.Path(); g.moveTo(fx - top, ytop); g.lineTo(fx - 30, fy); g.lineTo(fx + 30, fy); g.lineTo(fx + top, ytop)
        c.drawPath(g, M.paint(BR, qf, stroke=5))
        E.selo(c, fx + top + 60, ytop + 40, 40, False, qf)
        E.foco(c, t, b3 + 0.4, 0.4, lambda b_: centro(c, "funil, garrafa: não", fx, fy + 70, 48, "g", CLARO, b_))
    E.frase(c, t, c3, ps("na parte estreita, o nível sobe", "i", 56, CLARO) + [("mais rápido", "g", 60, BR)], W / 2, 1050, "center", 0.1)


# ---------------- questão ----------------
CX_, CY_, CR_, CH_ = 1450, 920, 200, 300   # a caixa cilíndrica: raio 1 m, altura 1,5 m (200 px por metro)


def b_questao(c, t, C, b):
    a4, b4, c4, d4, e4, f4 = (C[f"s14.{k}"] for k in "abcdef")
    E.frase(c, t, C["s14"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a4, ps("caixa cilíndrica:", "i", 62) + [("raio 1 m", "g", 64, COR)], XE, 330, passo=0.1)
    E.frase(c, t, b4, ps("altura", "i", 62) + [("1,5 m", "g", 64, COR)], XE, 430, passo=0.1)
    E.frase(c, t, c4, ps("torneira de", "i", 62) + [("30 L/min", "g", 64, COR)], XE, 530, passo=0.1)
    E.frase(c, t, d4, [("π = 3", "g", 64, COR)], XE, 630, passo=0.1)
    E.frase(c, t, e4, [("1)", "g", 64, COR)] + ps("quanto o nível sobe em 1 hora?", "i", 60), XE, 790, passo=0.1)
    E.frase(c, t, f4, [("2)", "g", 64, COR)] + ps("em quanto tempo enche?", "i", 60), XE, 900, passo=0.1)

    def desenho():
        E.cilindro(c, t, a4, CX_, CY_, CR_, CH_)
        E.cilindro(c, t, 1e9, CX_, CY_, CR_, CH_, "1 m", None, size=52, tm=a4 + 0.4)
        E.cilindro(c, t, 1e9, CX_, CY_, CR_, CH_, None, "1,5 m", size=52, tm=b4)
        torneira(c, t, c4, CX_, 300, CY_ - 40, "30 L/min")
    E.saida(c, t, C["s15.a"] - 0.1, desenho)
    E.relogio(c, t, C["s15.a"])


# ---------------- resposta ----------------
RX_, RY_, RR_, RH_ = 380, 940, 200, 300


def b_resposta(c, t, C, b):
    a6, b6, c6, d6, e6 = (C[f"s16.{k}"] for k in "abcde")
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    X = 1260
    E.cilindro(c, t, C["s16"], RX_, RY_, RR_, RH_, "1 m", "1,5 m", size=50)
    if t < C["s17"]:
        nv = 0.4 * ease_io(prog(t, b6, max(1.0, e6 - b6)))
    elif t < C["s18"]:
        nv = lerp(0.4, 1.0, ease_io(prog(t, b7, max(1.0, d7 - b7))))
    else:
        nv = 1.0
    agua_cil(c, RX_, RY_, RR_, RH_, nv)
    if C["s16"] <= t < C["s17"] and t >= e6:
        marca(c, t, e6, RX_ + RR_ + 130, RY_, RY_ - 0.4 * RH_ * COS, "60 cm", size=48)

    def hora():
        E.frase(c, t, C["s16"] + 0.2, [("1)", "g", 64, COR)] + ps("em 1 hora", "i", 66), X, 200, "center", 0.1)
        fcen(c, t, a6, "3 × 1² = 3 m²", X, 330, 70)
        fcen(c, t, b6, "60 × 30 = 1.800 L", X, 460, 70)
        fcen(c, t, c6, "= 1,8 m³", X, 570, 70, TINTA2)
        fcen(c, t, d6, "1,8 ÷ 3 = 0,6 m", X, 700, 74, COR)
        bola_txt(c, t, e6, "60 cm", X, 890, 120, 58)
    fase(c, t, C["s16"], C["s17"] - 0.1, hora)

    def encher():
        E.frase(c, t, C["s17"] + 0.2, [("2)", "g", 64, COR)] + ps("para encher", "i", 66), X, 200, "center", 0.1)
        fcen(c, t, a7, "3 × 1,5 = 4,5 m³", X, 340, 72)
        fcen(c, t, b7, "= 4.500 L", X, 460, 72, TINTA2)
        fcen(c, t, c7, "4.500 ÷ 30 = 150 min", X, 600, 72, COR)
        bola_txt(c, t, d7, "2 h e meia", X, 830, 140, 50)
    fase(c, t, C["s17"], C["s18"] - 0.1, encher)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.2, ps("pelo", "i", 66) + [("atalho,", "g", 70, COR)] + ps("confira", "i", 66), X, 200, "center", 0.1)
    fcen(c, t, a8, "sobe 60 cm por hora", X, 350, 66)
    fcen(c, t, b8, "caixa: 150 cm", X, 480, 66, TINTA2)
    fcen(c, t, c8, "150 ÷ 60 = 2,5 h", X, 640, 80, COR)
    E.foco(c, t, c8 + 1.2, 0.5, lambda a: E.selo(c, X - 120, 820, 60, True, a))
    E.frase(c, t, c8 + 1.4, [("bateu", "g", 72, CERTO)], X - 30, 845, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", ps("nível sobe =", "i", 62) + [("volume ÷ área do fundo", "g", 62, COR)]),
                 ("s19.b", ps("tempo =", "i", 62) + [("volume ÷ vazão", "g", 62, COR)]),
                 ("s19.c", [("tudo na mesma unidade", "g", 62, COR)] + ps("antes de dividir", "i", 62)))
        for i, (k, l1) in enumerate(itens):
            y = 400 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 350, y, "left", 0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a0, b0, c0, d0 = (C[f"s20.{k}"] for k in "abcd")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, C["s20"] + 0.8, [("Praticando", "g", 130, COR)], XE, 420)
    E.frase(c, t, a0, ps("moldes e vistas", "i", 64), XE, 540, passo=0.1)
    E.frase(c, t, b0, [("volume, capacidade e área", "g", 60, COR)], XE, 640, passo=0.1)
    E.frase(c, t, b0 + 1.0, ps("em caixas, latas e reservatórios", "i", 58), XE, 730, passo=0.1)
    E.foco(c, t, c0, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c0 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c0 + 0.2, 0.4))
    E.frase(c, t, d0, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, camada=b_camada, aquario=b_aquario, caixa=b_caixa, nivel=b_nivel, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
