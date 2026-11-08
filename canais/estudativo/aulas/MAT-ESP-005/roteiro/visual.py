"""Visual — Estudativo · MAT-ESP-005: volume do cubo e do bloco.
Mesma linguagem da MAT-ESP-001 (sólidos do kit, elemento da vez na cor da matéria, resposta na esfera) e da trilha Medidas:
- VOLUME = cubinhos que enchem a caixa. arame() é o contorno da caixa vazia (arestas de trás tracejadas) e enche() põe os cubinhos
  fileira a fileira, camada a camada, na mesma perspectiva cavaleira de E.paralelepipedo (cubinho() e arame() são os de MAT-MED-005).
  A fileira da vez entra caindo; a coluna que a fala aponta ganha outra cor (TINTA2).
- Fundo da caixa = área (m²): o piso pintado na cor da matéria (piso()). Água = prisma translúcido que sobe (agua()).
- Converter unidades = a ESCADA da trilha Medidas (classe Escada e num_un, copiadas de MAT-MED-005): bolinha que pula de degrau
  e a vírgula que anda no número. Aqui, a escada do comprimento com m, dm e cm.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-005_volume_do_cubo_e_do_bloco.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("camadas", "formula", "caixa", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 4 * 3 == 12 and 12 * 2 == 24 and 3 ** 3 == 27 and 2 * 1.5 == 3 and 3 * 1 * 1000 == 3000
assert 2 * 1.5 * 50 == 150 and 3 * 0.5 == 1.5 and 1.5 * 1000 == 1500 and 20 * 15 == 300 and 300 * 10 == 3000
assert 6 * 3 == 18 and 18 * 4 == 72 and 2 ** 3 == 8 and 8 * 1000 == 8000


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ² ou ³ vai na grotesca: a serifada não tem o expoente)"""
    return [(w, "g" if any(ch in w for ch in "²³") else est, size * (0.92 if any(ch in w for ch in "²³") and est != "g" else 1), cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)




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


# ---------------- gancho ----------------
GX, GY, GA, GB, GH = 260, 820, 440, 330, 220   # a caixa-d'água: 2 m x 1,5 m x 1 m (220 px por metro)


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        E.paralelepipedo(c, t, a1, GX, GY, GA, GB, GH, ("2 m", "1,5 m", "1 m"), size=54, tm=a1 + 1.2)
        E.frase(c, t, a1 + 0.2, [("caixa-d'água", "g", 76, COR)], 1080, 260, "left", 0.1)
        E.frase(c, t, lerp(a1, b1, 0.6), ps("quantos", "i", 76) + [("litros?", "g", 80, COR)], 1080, 380, "left", 0.1)
        E.frase(c, t, b1, [("2 + 1,5 + 1 = 4,5", "g", 70, ERRADO)], 1080, 540, "left", 0.1)
        if t >= b1 + 0.6:
            E.risco(c, 1070, 560, 1640, 480, t, b1 + 0.6, largura=10)
        E.frase(c, t, b1 + 0.8, ps("somar não diz nada", "i", 56, TINTA2), 1080, 630, "left", 0.1)
        bola_txt(c, t, c1, "3.000 L", 1300, 830, 150, 72)
        E.frase(c, t, c1 + 0.8, ps("com uma", "i", 56) + [("multiplicação", "g", 56, COR)], 1300, 1030, "center", 0.1)
        agua(c, GX, GY, GA, GB, GH, ease_io(prog(t, c1, 2.5)))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("o volume", "g", 104, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.4), ps("de cubo e bloco", "i", 90), XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("e em", "i", 90) + [("litros", "g", 104, COR)], XE, 740, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "área do retângulo:", "base × altura"), ("s03.c", "1 m³:", "cubo de 1 m de lado"), ("s03.d", "1 m³ guarda", "1.000 litros"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 60), x + 44, y + 84, "left", 0.1)
        E.frase(c, t, C[k] + 0.4, [(l2, "g", 60, COR)], x + 44, y + 160)
    alvo = [(C[k], 190 + i * 240 + 170) for i, (k, _, _) in enumerate(itens)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.7), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- volume em camadas ----------------
BX, BY, BS = 230, 880, 120   # o bloco 4 x 3 x 2 da aula: cubinhos de 120 px


def b_camadas(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]

    def ideia():
        E.frase(c, t, a4, [("volume", "g", 84, COR)] + ps("= quantos cubinhos", "i", 72), 160, 220, "left", 0.1)
        E.frase(c, t, a4 + 0.9, ps("enchem o espaço", "i", 72), 160, 310, "left", 0.1)
        arame(c, 200, 840, 3 * 100, 2 * 100, 2 * 100, ep(t, a4 + 0.2, 0.5))
        enche(c, t, 3, 2, 2, 200, 840, 100, lambda k, j: a4 + 0.6 + k * 0.6 + (1 - j) * 0.3)
        E.frase(c, t, a4 + 1.5, ps("cubinho de 1 m³", "i", 46, TINTA2), 380, 1000, "center", 0.08)
        E.paralelepipedo(c, t, b4, 800, 840, 330, 200, 200)
        E.foco(c, t, b4 + 0.3, 0.4, lambda q: (centro(c, "bloco", 1000, 960, 56, "g", COR, q), centro(c, "(paralelepípedo)", 1000, 1020, 44, "i", TINTA2, q)))
        E.cubo(c, t, c4, 1430, 840, 240, "a", todas=True, size=50)
        E.foco(c, t, c4 + 0.3, 0.4, lambda q: (centro(c, "cubo", 1600, 1000, 56, "g", COR, q), centro(c, "arestas iguais", 1600, 1050, 44, "i", TINTA2, q)))
    fase(c, t, C["s04"], C["s05"] - 0.1, ideia)
    if t < C["s05"] - 0.1:
        return

    # o bloco 4 x 3 x 2, camada a camada
    w, d, h = 4 * BS, 3 * BS, 2 * BS
    arame(c, BX, BY, w, d, h, ep(t, a5, 0.5))
    E.foco(c, t, a5 + 0.4, 0.4, lambda q: centro(c, "4 m", BX + w / 2, BY + 70, 54, "g", TINTA2, q))
    E.foco(c, t, a5 + 0.7, 0.4, lambda q: E.escreve(c, "3 m", BX + w + KX * d + 20, BY + KY * d / 2 + 30, 54, "g", TINTA2, q))
    E.foco(c, t, a5 + 1.0, 0.4, lambda q: E.escreve(c, "2 m", BX - 120, BY - h / 2 + 20, 54, "g", TINTA2, q))
    piso(c, BX, BY, w, d, ep(t, d5, 0.5) * (1 - ep(t, a6, 0.4)), grade=(4, 3))
    tfil = lambda k, j: (lerp(b5, c5, 0.25 * (2 - j)) if k == 0 else a6 + 0.35 * (2 - j))
    col = lambda i, j, k: TINTA2 if (t >= c6 and i == 0 and j == 0) else None
    enche(c, t, 4, 3, 2, BX, BY, BS, tfil, cor=col)
    X = 1300
    E.frase(c, t, b5, [("4", "g", 70, COR)] + ps("por fileira,", "i", 62) + [("3", "g", 70, COR)] + ps("fileiras", "i", 62), X, 260, "center", 0.1)
    fcen(c, t, c5, "4 × 3 = 12 cubinhos", X, 380, 70)
    E.frase(c, t, d5, ps("= a área do fundo:", "i", 56, TINTA2) + [("12 m²", "g", 60, COR)], X, 470, "center", 0.1)
    E.frase(c, t, a6, [("2 camadas", "g", 66, COR)] + ps("de 12", "i", 62), X, 620, "center", 0.1)
    fcen(c, t, b6, "12 × 2 = 24", X, 740, 76)
    bola_txt(c, t, b6 + 0.7, "24 m³", X, 870, 100, 60)
    E.frase(c, t, c6, ps("cada m² do fundo segura", "i", 50, TINTA2) + [("uma coluna", "g", 52, TINTA2)], X, 1035, "center", 0.08)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")

    def bloco():
        E.frase(c, t, a7, [("volume", "g", 80, COR)] + ps("= área da base × altura", "i", 72), W / 2, 210, "center", 0.1)
        E.paralelepipedo(c, t, b7 - 0.3, 260, 860, 520, 300, 320, ("a", "b", "c"), size=64, tm=d7)
        piso(c, 260, 860, 520, 300, ep(t, a7 + 0.8, 0.5) * (1 - ep(t, b7, 0.4)))
        fcen(c, t, b7, "V = a × b × c", 1380, 480, 120, COR)
        E.foco(c, t, c7, 0.4, lambda q: centro(c, "volume", 1380 - E.formula(None, "V = a × b × c", 0, 0, 120, "g", a=0) / 2 + 40, 560, 46, "i", COR, q))
        E.frase(c, t, d7, ps("comprimento, largura e altura", "i", 56, TINTA2), 1380, 700, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, bloco)
    if t < C["s08"] - 0.1:
        return
    fcen(c, t, a8, "a × a × a", 1380, 300, 100)
    fcen(c, t, b8, "V = a³", 1380, 470, 140, COR)
    if t >= c8:
        p = ep(t, c8, 0.5)
        x3 = 1380 + E.formula(None, "V = a³", 0, 0, 140, "g", a=0) / 2 - 22
        E.caixa_pontilhada(c, x3 - 44, 330, 80, 90, p, COR, prog_=p)
        E.foco(c, t, c8 + 0.2, 0.4, lambda q: centro(c, "ao cubo", x3, 580, 54, "i", COR, q))
    # o cubo de 3 m: 27 cubinhos
    s = 120
    arame(c, 260, 900, 3 * s, 3 * s, 3 * s, ep(t, C["s08"], 0.5))
    E.foco(c, t, d8, 0.4, lambda q: centro(c, "3 m", 260 + 1.5 * s, 970, 56, "g", TINTA2, q))
    enche(c, t, 3, 3, 3, 260, 900, s, lambda k, j: e8 + 0.3 * k + 0.12 * (2 - j))
    fcen(c, t, e8, "3³ = 3 × 3 × 3", 1380, 720, 76)
    bola_txt(c, t, e8 + 1.0, "27 m³", 1380, 880, 120, 70)


# ---------------- a caixa-d'água ----------------
def b_caixa(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    E.paralelepipedo(c, t, C["s09"], GX, GY, GA, GB, GH, ("2 m", "1,5 m", "1 m"), size=54)
    piso(c, GX, GY, GA, GB, ep(t, a9, 0.5) * (1 - ep(t, c9, 0.4)))
    agua(c, GX, GY, GA, GB, GH, ease_io(prog(t, c9, 2.5)))
    X = 1360
    E.frase(c, t, C["s09"] + 0.2, ps("de volta à", "i", 66) + [("caixa-d'água", "g", 70, COR)], X, 220, "center", 0.1)
    E.frase(c, t, a9, ps("fundo:", "i", 62), X - 360, 370, "left", 0.1)
    fcen(c, t, a9 + 0.3, "2 × 1,5 = 3 m²", X + 130, 370, 78)
    E.frase(c, t, b9, ps("× altura:", "i", 62), X - 360, 510, "left", 0.1)
    fcen(c, t, b9 + 0.3, "3 × 1 = 3 m³", X + 130, 510, 78)
    E.frase(c, t, c9, ps("1 m³ = 1.000 L:", "i", 56, TINTA2), X, 640, "center", 0.1)
    fcen(c, t, c9 + 0.6, "3 × 1.000", X, 740, 80)
    bola_txt(c, t, c9 + 1.4, "3.000 L", X, 900, 125, 64)


# ---------------- erro ----------------
TX, TY, TA, TB, TH = 230, 860, 440, 330, 110   # o tanque: 2 m x 1,5 m x 50 cm


def b_erro(c, t, C, b):
    a0, b0, c0 = C["s10.a"], C["s10.b"], C["s10.c"]
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    E.frase(c, t, C["s10"] + 0.2, [("cuidado:", "g", 76, ERRADO)] + ps("unidades diferentes", "i", 76), W / 2, 180, "center", 0.12)
    E.paralelepipedo(c, t, b0, TX, TY, TA, TB, TH, ("2 m", "1,5 m", None), size=54)
    E.foco(c, t, b0 + 0.8, 0.4, lambda q: E.escreve(c, "50 cm", TX - 190, TY - TH / 2 + 20, 56, "g", ERRADO, q))
    X = 1350

    def errado():
        fcen(c, t, c0, "2 × 1,5 × 50 = 150", X, 400, 84, ERRADO)
        E.frase(c, t, a1, [("150 m³", "g", 66, ERRADO)] + ps("seriam", "i", 60) + [("150.000 L", "g", 66, ERRADO)], X, 530, "center", 0.1)
        E.frase(c, t, a1 + 1.2, ps("num tanque mais baixo que a caixa de 3.000 L!", "i", 48, TINTA2), X, 610, "center", 0.08)
    fase(c, t, c0, b1 - 0.1, errado)
    if t >= b1 - 0.1:
        fcen(c, t, b1, "50 cm = 0,5 m", X, 400, 84, COR)
        fcen(c, t, c1, "3 × 0,5 = 1,5 m³", X, 560, 84)
        bola_txt(c, t, d1, "1.500 L", X, 760, 130, 66)
    agua(c, TX, TY, TA, TB, TH, ease_io(prog(t, d1, 1.5)))


# ---------------- atalho (palco escuro) ----------------
ESC = Escada(x=120, y=330, sw=230, sh=110, base=700, un=("m", "dm", "cm"), nomes=("metro", "decímetro", "centímetro"), meio=0, size=70)


def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")

    def um():
        E.frase(c, t, a2, ps("meça em", "i", 70, CLARO) + [("decímetros:", "g", 74, BR)] + ps("sai em", "i", 70, CLARO) + [("litros", "g", 74, BR)],
                W / 2, 170, "center", 0.1)
        ESC.degraus(c, t, a2 + 0.4, escuro=True)
        ESC.pulos(c, t, 0, [(b2, 1)], b2 - 0.4, escuro=True)
        E.foco(c, t, b2 + 0.4, 0.4, lambda q: centro(c, "1 casa →", ESC.cx(0.5), 830, 56, "g", BR, q))
        x0, y0, sz = 1000, 390, 100
        for k, (dig, ts, un0) in enumerate((("2", c2, "m"), ("15", c2 + 0.5, "m"), ("1", c2 + 1.0, "m"))):
            y = y0 + 150 * k
            num_un(c, t, dig, 1, [(ts + 0.5, 2)], x0, y, sz, [(ts, "m"), (ts + 1.0, "dm")], cor=BR, t0=ts, some=True, cor_un=CLARO, cor_novo=CLARO)
        fcen(c, t, d2, "20 × 15 = 300", 1180, 880, 84, BR)
        fcen(c, t, e2, "300 × 10 = 3.000 L", 1180, 1000, 84, CLARO)
    fase(c, t, C["s12"], C["s13"] - 0.1, um)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, C["s13"] + 0.2, ps("funciona porque", "i", 70, CLARO), W / 2, 220, "center", 0.1)
    fcen(c, t, a3, "1 dm³ = 1 L", W / 2, 400, 130, BR)
    E.frase(c, t, b3, ps("e", "i", 66, CLARO) + [("tudo vai para a mesma unidade", "g", 62, BR)], W / 2, 540, "center", 0.1)
    E.foco(c, t, c3, 0.5, lambda a: E.selo(c, 440, 700, 50, False, a))
    E.frase(c, t, c3 + 0.1, ps("não compensa se a prova pede", "i", 62, CLARO) + [("m³", "g", 66, BR)], 520, 725, "left", 0.1)
    E.foco(c, t, d3, 0.5, lambda a: E.pilula(c, "fique em metros", W / 2, 880, 84, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    E.frase(c, t, C["s14"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a4, ps("aquário:", "i", 70) + [("60 × 30 × 40 cm", "g", 70, COR)], XE, 360, passo=0.1)
    E.frase(c, t, b4, ps("quantos", "i", 76) + [("litros?", "g", 80, COR)], XE, 480, passo=0.1)
    E.frase(c, t, c4, ps("caixa cúbica de", "i", 70) + [("2 m", "g", 70, COR)] + ps("de aresta:", "i", 70), XE, 680, passo=0.1)
    E.frase(c, t, c4 + 1.2, ps("quantos", "i", 76) + [("litros?", "g", 80, COR)], XE, 800, passo=0.1)

    def desenhos():
        E.paralelepipedo(c, t, a4, 1250, 560, 360, 180, 240, ("60 cm", "30 cm", "40 cm"), size=44)
        E.cubo(c, t, c4, 1330, 1000, 230, "2 m", size=48)
    E.saida(c, t, C["s15.a"] - 0.1, desenhos)
    E.relogio(c, t, C["s15.a"])


# ---------------- resposta ----------------
ESC_R = Escada(x=120, y=360, sw=220, sh=120, base=820, un=("m", "dm", "cm"), nomes=("metro", "decímetro", "centímetro"), meio=1, size=64)


def b_resposta(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")

    def aquario():
        E.frase(c, t, C["s16"] + 0.2, ps("aquário:", "i", 66) + [("tudo em decímetros", "g", 66, COR)], W / 2, 180, "center", 0.1)
        ESC_R.degraus(c, t, a6 - 0.2, acesos=(1, 2), ta=a6 + 0.4)
        ESC_R.pulos(c, t, 2, [(lerp(a6, b6, 0.2), 1)], a6 + 0.2)
        E.foco(c, t, lerp(a6, b6, 0.2) + 0.5, 0.4, lambda q: centro(c, "← 1 casa", ESC_R.cx(1.5), 900, 56, "g", COR, q))
        for k, (de, para) in enumerate((("60", "6"), ("30", "3"), ("40", "4"))):
            tk = lerp(a6, b6, 0.4 + 0.18 * k)
            y = 380 + 130 * k
            E.saida(c, t, tk + 0.6, lambda de=de, tk=tk, y=y: E.foco(c, t, tk - 0.4, 0.4, lambda q: E.escreve(c, de + " cm", 900, y, 80, "g", TINTA2, q)))
            E.foco(c, t, tk + 0.6, 0.4, lambda q, para=para, y=y: E.escreve(c, para + " dm", 900, y, 80, "g", COR, q))
        fcen(c, t, b6, "6 × 3 = 18", 1500, 520, 84)
        fcen(c, t, c6, "18 × 4 = 72", 1500, 680, 84)
        bola_txt(c, t, c6 + 0.8, "72 L", 1500, 870, 120, 76)
    fase(c, t, C["s16"], C["s17"] - 0.1, aquario)
    if t < C["s17"] - 0.1:
        return
    E.frase(c, t, C["s17"] + 0.2, ps("caixa cúbica de", "i", 66) + [("2 m", "g", 70, COR)], W / 2, 180, "center", 0.1)
    fcen(c, t, a7, "2³ = 2 × 2 × 2 = 8 m³", 1380, 360, 76)
    fcen(c, t, b7, "8 × 1.000", 1380, 500, 76)
    bola_txt(c, t, b7 + 0.8, "8.000 L", 1380, 670, 145, 60)
    # o cubo de 1 m e o de 2 m, lado a lado
    s = 110
    E.foco(c, t, c7, 0.5, lambda q: cubinho(c, 200, 900, s, q, TINTA2))
    E.foco(c, t, c7, 0.4, lambda q: centro(c, "1 m", 200 + s / 2, 960, 48, "g", TINTA2, q))
    arame(c, 470, 900, 2 * s, 2 * s, 2 * s, ep(t, c7 + 0.3, 0.4))
    enche(c, t, 2, 2, 2, 470, 900, s, lambda k, j: d7 + 0.4 * k + 0.15 * (1 - j))
    E.foco(c, t, c7 + 0.4, 0.4, lambda q: centro(c, "2 m", 470 + s, 960, 48, "g", COR, q))
    E.frase(c, t, d7, [("8 vezes", "g", 66, COR)] + ps("maior", "i", 62), 1380, 880, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s18.a", ps("volume =", "i", 66) + [("área da base × altura", "g", 64, COR)]),
                 ("s18.b", ps("bloco:", "i", 66) + [("V = a × b × c", "g", 70, COR)]),
                 ("s18.c", ps("cubo:", "i", 66) + [("V = a³", "g", 70, COR)]),
                 ("s18.d", [("1 m³ = 1.000 L", "g", 70, COR)]))
        for i, (k, l1) in enumerate(itens):
            y = 360 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 350, y, "left", 0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    E.frase(c, t, C["s19"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a9, [("Área", "g", 130, COR)] + ps("da caixa", "i", 100), XE, 420)
    E.frase(c, t, a9 + 0.6, ps("quanta tinta para pintar por fora", "i", 64), XE, 530, passo=0.1)
    E.frase(c, t, b9, ps("e a", "i", 72) + [("diagonal", "g", 76, COR)] + ps("do cubo", "i", 72), XE, 680, passo=0.1)
    E.foco(c, t, c9, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c9 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c9 + 0.2, 0.4))
    E.frase(c, t, d9, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, camadas=b_camadas, formula=b_formula, caixa=b_caixa, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
