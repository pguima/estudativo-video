"""Visual — Estudativo · MAT-ARE-001: perímetro, o contorno de uma figura. Primeira aula de Áreas e Perímetros.

LINGUAGEM VISUAL DE ÁREAS E PERÍMETROS (as próximas aulas da trilha copiam daqui; segue a da geometria plana, MAT-ANG-001):
- Figuras do kit (E.retangulo, E.quadrado, E.triangulo, E.paralelogramo, E.trapezio, E.regular) em tinta preta, miolo claro da cor da matéria.
- PERÍMETRO = a volta: a cerca() é o contorno grosso na cor da matéria, com mourões, que se desenha em volta a partir de um canto.
  Cerca errada (que não fecha) em vermelho; o pedaço que falta fica tracejado em cinza.
- ÁREA = quadradinhos: grade_q() enche a figura fileira a fileira (mesma peça da trilha Medidas, MAT-MED-004).
- Medida que muda de unidade: cota_h()/cota_v() com o texto trocando; a conversão é a ESCADA do metro (Escada e num_un, iguais às
  de MAT-MED-001/004), aqui só com os degraus que a conta usa.
- Conta da vez em grotesca, resposta numa esfera (bola_res). Atalho no palco escuro.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-001_perimetro_contorno.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conceito", "retangulo", "unidades", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

assert 5 + 7 + 8 == 20 and 20 + 35 == 55 and 55 + 55 == 110 and 3 * 4 == 12
assert 120 + 80 == 200 and 200 * 2 == 400 and 400 / 100 == 4 and 6 * 100 == 600
assert 600 + 250 == 850 and 850 * 2 == 1700 and 1700 / 100 == 17 and 17 - 2 == 15


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
TX, TY, TW, TH = 230, 330, 700, 400  # o terreno de 35 m por 20 m (20 px por metro)
TER = ret_pts(TX, TY, TW, TH)


def terreno(c, t, t0, lados, tl, iguais=None):
    E.retangulo(c, t, t0, TX, TY, TW, TH, lados=lados, tl=tl, iguais=iguais, size=56, preenche=0.08)


def icone(c, x, y, w, h, nome, p, a, tipo):
    """os três usos do perímetro: cerca (terreno), rodapé (sala), fita (borda da mesa)"""
    if a <= 0:
        return
    if tipo == "cerca":
        M.rrect(c, x, y, w, h, 6, "#DDEFD9", a)
    elif tipo == "rodape":
        M.rrect(c, x, y, w, h, 4, "#F3EADB", a)
        for k in range(1, 6):
            M.line(c, x + w * k / 6, y, x + w * k / 6, y + h, "#E2D3BA", a, 2)
    else:
        M.rrect(c, x, y, w, h, 18, "#C9A27A", a)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(TINTA, a, stroke=3))
    cerca(c, ret_pts(x, y, w, h), p, largura=8 if tipo != "cerca" else 9, postes=tipo == "cerca", a=a)
    centro(c, nome, x + w / 2, y + h + 70, 58, "g", COR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        terreno(c, t, ka, ["35 m", None, None, "20 m"], [ka + 0.8, None, None, ka + 1.2])
        E.frase(c, t, ka + 0.8, ps("quantos metros de", "i", 70), 1080, 330, "left", 0.1)
        E.frase(c, t, ka + 1.4, [("cerca?", "g", 96, COR)], 1080, 450, "left")
        # a cerca de 55 m: só o lado de 20 e o de 35
        p = ease_io(prog(t, kb, 1.4))
        cerca(c, [TER[0], TER[3], TER[2]], p, ERRADO, fecha=False)
        E.foco(c, t, kb + 0.2, 0.5, lambda a: E.escreve(c, "20 + 35 = 55", 1080, 640, 90, "g", ERRADO, a))
        if t >= kc:
            tracejado(c, [TER[2], TER[1], TER[0]], CINZA, ep(t, kc, 0.5))
            E.foco(c, t, kc + 0.2, 0.5, lambda a: E.selo(c, TER[2][0], TER[2][1], 40, False, a))
        E.frase(c, t, kc + 0.3, ps("parou no", "i", 68) + [("meio do caminho", "g", 64, ERRADO)], 1080, 800, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 84), XE, 290, passo=0.12)
        E.frase(c, t, ta + 0.9, [("o contorno", "g", 110, COR)], XE, 440, passo=0.12)
        E.frase(c, t, ta + 1.4, ps("de qualquer figura", "i", 90), XE, 560, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("até com", "i", 70) + [("unidades diferentes", "g", 70, COR)], XE, 720, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "a escada do metro", "1 degrau = 1 casa"), ("s03.c", "no retângulo,", "lados opostos iguais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.foco(c, t, C[k] + 0.4, 0.5, lambda a, l2=l2, y=y: E.escreve(c, l2, x + 44, y + 160, 60, "g", COR, a))
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(420, 700, q), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.55), ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 1000, "left", 0.12)


# ---------------- o que é perímetro ----------------
FIG = [(330, 420), (720, 300), (1010, 470), (900, 840), (420, 800)]  # uma figura qualquer de lados retos


def b_conceito(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]

    def um():
        E.frase(c, t, a4, [("perímetro", "g", 110, COR)], 1120, 330, "left")
        E.frase(c, t, a4 + 0.6, ps("a medida do", "i", 72), 1120, 450, "left", 0.1)
        E.frase(c, t, a4 + 1.0, [("contorno", "g", 80)], 1120, 550, "left")
        E.poligono(c, t, a4 + 0.2, FIG, preenche=0.08, d=0.8)
        # quem anda pela borda: sai do canto, dá a volta e chega de novo ao começo
        p = ease_io(prog(t, b4, max(1.2, c4 - b4 + 0.4)))
        if t >= b4:
            cerca(c, FIG, p, postes=False, largura=12)
            E.foco(c, t, b4 - 0.3, 0.4, lambda a: (c.drawCircle(*FIG[0], 20, M.paint(TINTA, a)),
                                                   E.escreve(c, "partida", FIG[0][0] - 220, FIG[0][1] - 30, 46, "i", TINTA2, a)))
            x_, y_ = no_caminho(FIG, p)
            E.bola(c, x_, y_, 30 * ease_back(prog(t, b4, 0.4)))
        E.frase(c, t, c4 + 0.5, ps("deu a", "i", 72) + [("volta inteira", "g", 72, COR)], 1120, 720, "left", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, um)

    if C["s05"] <= t < C["s06"] + 0.4:
        a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")

        def dois():
            E.foco(c, t, a5, 0.5, lambda a: (E.escreve(c, "peri", 520 - E.larg("peri", "g", 150), 320, 150, "g", COR, a),
                                             centro(c, "em volta", 520 - E.larg("peri", "g", 150) / 2, 400, 52, "i", TINTA2, a)))
            E.foco(c, t, b5, 0.5, lambda a: (E.escreve(c, "metro", 530, 320, 150, "g", TINTA, a),
                                             centro(c, "medida", 530 + E.larg("metro", "g", 150) / 2, 400, 52, "i", TINTA2, a)))
            E.foco(c, t, b5 + 0.4, 0.5, lambda a: E.escreve(c, "= medir em volta", 1080, 300, 70, "i", TINTA, a))
            for k, (tk, nome, tipo, x, w) in enumerate(((c5, "cerca", "cerca", 200, 460), (d5, "rodapé", "rodape", 760, 400),
                                                        (e5, "fita", "fita", 1260, 460))):
                q = ep(t, tk, 0.5)
                icone(c, x, 560, w, 260, nome, ease_io(prog(t, tk + 0.3, 1.1)), q, tipo)
        E.saida(c, t, C["s06"] - 0.1, dois)

    if t >= C["s06"]:
        a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
        E.frase(c, t, C["s06"] + 0.2, ps("lados retos:", "i", 76), XE, 220, "left", 0.1)
        E.frase(c, t, a6, [("some todos os lados", "g", 84, COR)], XE + 430, 220, "left")
        A, B, Cc = (260, 880), (860, 880), (447.5, 555.2)  # AB = 8, BC = 7, CA = 5 (75 px por cm)
        E.triangulo(c, t, b6 - 0.3, A, B, Cc, vertices=None, lados=["8 cm", "7 cm", "5 cm"], tl=[b6 + 1.4, b6 + 0.8, b6 + 0.2], size=58)
        for k, (P0, P1, tk) in enumerate(((Cc, A, c6), (B, Cc, c6 + 0.5), (A, B, c6 + 1.0))):
            q = ep(t, tk, 0.5)
            if q > 0:
                M.line(c, *P0, *P1, E.COR, q, 12)
        fcen(c, t, c6, "5 + 7 + 8 = 20", 1380, 560, 110)
        bola_res(c, t, c6 + 1.6, "20 cm", 1380, 790, 140, 76)


# ---------------- o retângulo ----------------
def b_retangulo(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]

    def terra():
        # o terreno, depois os quatro lados, depois a meia volta e a volta inteira
        terreno(c, t, C["s07"], ["35 m", "20 m", "35 m", "20 m"], [a7, c7 + 0.4, lerp(c7, C["s07.end"], 0.6), a7 + 0.4],
                )
        if b7 <= t < C["s08"]:
            for k, (x_, y_) in enumerate(((TX + TW / 2, TY + TH - 60), (TX + TW - 60, TY + TH / 2), (TX + TW / 2, TY + 60), (TX + 60, TY + TH / 2))):
                num_lado(c, t, b7 + 0.25 * k, k + 1, x_, y_)
        if t >= a8:
            meia = ease_io(prog(t, a8, 1.0))
            volta = ease_io(prog(t, c8, 1.0))
            cerca(c, [TER[0], TER[3], TER[2], TER[1]], 0.5 * meia + 0.5 * volta, fecha=True)
    terra()
    E.frase(c, t, C["s07"] + 0.2, ps("o terreno:", "i", 70), 1080, 250, "left", 0.1)
    if t < C["s08"]:
        E.frase(c, t, a7, [("só 2 medidas", "g", 70, COR)], 1080, 360, "left")
        E.frase(c, t, b7, ps("mas são", "i", 70) + [("4 lados", "g", 76, COR)], 1080, 500, "left", 0.1)
        E.frase(c, t, c7, ps("opostos", "i", 70) + [("iguais", "g", 76, COR)], 1080, 640, "left", 0.1)
        return
    x0 = 1400
    fcen(c, t, a8, "20 + 35 = 55", x0, 420, 96)
    E.foco(c, t, b8, 0.5, lambda a: E.pilula(c, "meia volta", x0, 530, 54, "g", a=a, cor=E.SOBRE))
    fcen(c, t, c8, "55 + 55 = 110", x0, 700, 96)
    bola_res(c, t, d8, "110 m", x0, 880, 130, 70)


# ---------------- quadrado e equilátero (ainda no bloco retangulo) ----------------
def b_retangulo_total(c, t, C, b):
    if t < C["s09"]:
        E.saida(c, t, C["s09"] - 0.1, lambda: b_retangulo(c, t, C, b))
        return
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    E.frase(c, t, C["s09"] + 0.1, ps("no", "i", 76) + [("quadrado,", "g", 80, COR)], XE, 220, "left", 0.1)
    E.frase(c, t, a9, ps("4 lados iguais", "i", 76), XE + 520, 220, "left", 0.1)
    E.quadrado(c, t, a9 + 0.4, 250, 340, 420, lado="3 m", tl=[b9, b9 + 0.15, b9 + 0.3, b9 + 0.45], size=58)
    cerca(c, ret_pts(250, 340, 420, 420), ease_io(prog(t, c9, 1.2)))
    fcen(c, t, c9, "3 × 4 = 12", 1000, 560, 96)
    bola_res(c, t, c9 + 1.4, "12 m", 1000, 760, 120, 66)
    # o equilátero: lado vezes três
    A, B, Cc = (1380, 820), (1780, 820), (1580, 473.6)
    E.triangulo(c, t, d9 - 0.2, A, B, Cc, vertices=None, iguais=[1, 1, 1], tl=[d9 + 0.4] * 3)
    fcen(c, t, d9 + 0.6, "lado × 3", 1580, 960, 76, COR)
    E.foco(c, t, d9 - 0.2, 0.4, lambda a: centro(c, "equilátero", 1580, 400, 56, "i", TINTA2, a))


# ---------------- unidades diferentes ----------------
MX, MY, MW, MH = 330, 380, 600, 400  # a mesa: 1,2 m por 80 cm (5 px por cm)
ESC = Escada(x=150, y=420, sw=200, sh=110, base=900)


def b_unidades(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2 = C["s12.a"], C["s12.b"]

    def mesa(t1):
        def f():
            E.foco(c, t, C["s10"] + 0.2, 0.5, lambda a: M.rrect(c, MX, MY, MW, MH, 10, "#C9A27A", a))
            E.foco(c, t, C["s10"] + 0.2, 0.5, lambda a: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(MX, MY, MW, MH), 10, 10), M.paint(TINTA, a, stroke=4)))
            troca = ep(t, b1, 0.4) if t1 is None else 0
            cota_hb(c, t, b0, "1,2 m", MX, MX + MW, MY + MH + 40, a=1 - troca)
            if t1 is None:
                cota_hb(c, t, b1, "120 cm", MX, MX + MW, MY + MH + 40)
            cota_v(c, t, c0, "80 cm", MX - 40, MY, MY + MH)
        return f

    E.frase(c, t, a0, ps("unidades", "i", 76) + [("diferentes?", "g", 80, COR)], XE, 220, "left", 0.1)
    if t < C["s11"] + 0.5:
        E.saida(c, t, C["s11"], mesa(1))
        E.foco(c, t, b0, 0.5, lambda a: E.escreve(c, "1,2 m", 1080, 470, 110, "g", COR, a))
        E.foco(c, t, c0, 0.5, lambda a: E.escreve(c, "80 cm", 1500, 470, 110, "g", TINTA, a))
        E.foco(c, t, c0 + 0.5, 0.5, lambda a: E.escreve(c, "+", 1410, 465, 100, "g", TINTA2, a * (1 - ep(t, d0, 0.3))))
        if t >= d0:
            E.risco(c, 1060, 520, 1820, 380, t, d0 - 0.1, largura=12)
        E.foco(c, t, d0 + 0.2, 0.5, lambda a: E.pilula(c, "tudo na mesma unidade", 1450, 680, 62, "g", a=a, cor=E.SOBRE))
    if t < C["s11"]:
        return

    # a escada: do metro ao centímetro, dois degraus para baixo
    def escada():
        ESC.degraus(c, t, C["s11"] + 0.1, acesos=(1, 2), ta=a1)
        ESC.pulos(c, t, 0, [(a1, 1), (a1 + 0.7, 2)], C["s11"] + 0.4)
        num_un(c, t, "12", 1, [(a1, 2), (a1 + 0.7, 3)], 1000, 420, 130, [(C["s11"] + 0.4, "m"), (a1 + 0.7, "dm"), (a1 + 1.4, "cm")],
               t0=C["s11"] + 0.4, some=True)
        casas(c, t, a1 + 0.4, "2 casas →", 1300, 560)
        E.foco(c, t, b1, 0.5, lambda a: E.pilula(c, "1,2 m = 120 cm", 1300, 700, 66, "g", fundo=TINTA, a=a, cor=BR))
    fase(c, t, C["s11"], c1 - 0.1, escada)
    if t < c1 - 0.1:
        return

    def conta():
        mesa(None)()
        cota_hb(c, t, c1 - 0.2, "120 cm", MX, MX + MW, MY + MH + 40)
        fcen(c, t, c1, "120 + 80 = 200", 1360, 430, 92)
        cerca(c, [(MX, MY + MH), (MX, MY), (MX + MW, MY)], ease_io(prog(t, c1, 0.9)), fecha=False, postes=False, largura=10)
        fcen(c, t, d1, "200 × 2 = 400", 1360, 600, 92)
        cerca(c, ret_pts(MX, MY, MW, MH)[::-1], ease_io(prog(t, d1, 1.0)), postes=False, largura=10)
        bola_res(c, t, d1 + 1.0, "400 cm", 1360, 800, 130, 62)
    fase(c, t, c1 - 0.1, C["s12"] - 0.1, conta)
    if t < C["s12"]:
        return

    # de volta ao metro: dois degraus para cima
    ESC.degraus(c, t, C["s12"] + 0.1, acesos=(0, 1), ta=a2)
    ESC.pulos(c, t, 2, [(a2, 1), (a2 + 0.7, 0)], C["s12"] + 0.4)
    px = num_un(c, t, "400", 3, [(a2, 2), (a2 + 0.7, 1)], 1000, 420, 130, [(C["s12"] + 0.4, "cm"), (a2 + 0.7, "dm"), (a2 + 1.4, "m")],
                t0=C["s12"] + 0.4, tv=a2 - 0.4)
    casas(c, t, a2 + 0.4, "← 2 casas", 1300, 560, cor=TINTA)
    if px and t >= b2:
        E.risco(c, px(0) + 50, 440, px(2) + 50, 330, t, b2, largura=10)
    bola_res(c, t, b2 + 0.3, "4 m", 1320, 790, 130, 80)
    E.frase(c, t, b2 + 0.8, ps("de fita", "i", 64, TINTA2), 1520, 790, "left", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.2, ps("o erro:", "i", 70) + [("somar só o que aparece", "g", 70, ERRADO)], W / 2, 180, "center", 0.1)
    terreno(c, t, C["s13"] + 0.2, ["35 m", None, None, "20 m"], [a3, None, None, a3 + 0.3])
    cerca(c, [TER[0], TER[3], TER[2]], ease_io(prog(t, b3, 1.2)), ERRADO, fecha=False)
    E.foco(c, t, b3, 0.5, lambda a: E.escreve(c, "20 + 35 = 55", 1080, 400, 90, "g", ERRADO, a))
    if t >= c3:
        tracejado(c, [TER[2], TER[1], TER[0]], CINZA, ep(t, c3, 0.5))
        E.frase(c, t, c3 + 0.1, ps("cobre só", "i", 66) + [("2 lados", "g", 70, ERRADO)], 1080, 520, "left", 0.1)
    if t >= d3:
        for k, (x_, y_) in enumerate(((TX + TW / 2, TY + TH - 60), (TX + TW - 60, TY + TH / 2), (TX + TW / 2, TY + 60), (TX + 60, TY + TH / 2))):
            num_lado(c, t, d3 + 0.3 * k, k + 1, x_, y_)
        E.frase(c, t, d3 + 0.3, [("4 lados,", "g", 72, COR)] + ps("4 parcelas", "i", 72), 1080, 680, "left", 0.1)
        fcen(c, t, d3 + 1.4, "35 + 20 + 35 + 20", 1420, 780, 64)
    E.foco(c, t, e3, 0.5, lambda a: E.selo(c, TER[2][0], TER[2][1], 40, False, a))
    E.frase(c, t, e3 + 0.2, ps("a cerca tem de", "i", 54) + [("voltar ao começo", "g", 54, COR)], 1060, 920, "left", 0.1)
    if t >= e3:
        k = ease_back(prog(t, e3 + 0.4, 0.5))
        c.drawCircle(*TER[0], 24 * k, M.paint(CERTO))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4 = C["s14.a"], C["s14.b"], C["s14.c"]
    a5, b5, c5, d5 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]

    def um():
        E.frase(c, t, a4, ps("o atalho do", "i", 80, CLARO) + [("retângulo", "g", 86, BR)], W / 2, 220, "center", 0.12)
        E.frase(c, t, b4, ps("some comprimento e largura", "i", 76, CLARO), W / 2, 380, "center", 0.1)
        E.frase(c, t, b4 + 1.2, [("e dobre", "g", 110, BR)], W / 2, 520, "center")
        fcen(c, t, b4 + 2.0, "(35 + 20) × 2 = 110", 560, 720, 76, BR)
        fcen(c, t, b4 + 2.4, "(120 + 80) × 2 = 400", 1360, 720, 76, BR)
        E.foco(c, t, c4, 0.5, lambda a: E.pilula(c, "2 contas, não 4 parcelas", W / 2, 900, 64, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s15"] - 0.1, um)
    if t < C["s15"]:
        return
    # cada lado tem um gêmeo
    x, y, w, h = 160, 330, 480, 300
    E.frase(c, t, a5, ps("cada lado tem um", "i", 72, CLARO) + [("gêmeo", "g", 80, BR)], W / 2, 190, "center", 0.1)
    E.retangulo(c, t, C["s15"] + 0.2, x, y, w, h, iguais=[2, 1, 2, 1], tl=[a5 + 0.3] * 4, escuro=True, preenche=0.2)
    for (P0, P1), cr, tk in (((ret_pts(x, y, w, h)[0], ret_pts(x, y, w, h)[1]), E.COR, a5 + 0.5), ((ret_pts(x, y, w, h)[3], ret_pts(x, y, w, h)[2]), E.COR, a5 + 0.5),
                             ((ret_pts(x, y, w, h)[1], ret_pts(x, y, w, h)[2]), CLARO, a5 + 0.9), ((ret_pts(x, y, w, h)[0], ret_pts(x, y, w, h)[3]), CLARO, a5 + 0.9)):
        q = ep(t, tk, 0.5)
        if q > 0:
            M.line(c, *P0, *P1, cr, q, 12)
    E.foco(c, t, a5 + 0.4, 0.4, lambda a: centro(c, "retângulo", x + w / 2, y + h + 100, 52, "i", CLARO, a))
    E.foco(c, t, C["s15"] + 0.6, 0.4, lambda a: E.selo(c, x + w / 2, y + h + 190, 40, True, a))
    # paralelogramo: também tem
    E.paralelogramo(c, t, b5, 760, y + 20, 380, 280, 120, iguais=[2, 1, 2, 1], tl=[b5 + 0.6] * 4, escuro=True, preenche=0.2)
    E.foco(c, t, b5 + 0.4, 0.4, lambda a: centro(c, "paralelogramo", 1010, y + h + 100, 52, "i", CLARO, a))
    E.foco(c, t, b5 + 0.9, 0.4, lambda a: E.selo(c, 1010, y + h + 190, 40, True, a))
    # trapézio: não serve
    E.trapezio(c, t, c5, 1300, y + 20, 480, 240, 280, escuro=True, preenche=0.2)
    E.foco(c, t, c5 + 0.4, 0.4, lambda a: centro(c, "trapézio", 1540, y + h + 100, 52, "i", CLARO, a))
    E.foco(c, t, c5 + 0.9, 0.4, lambda a: E.selo(c, 1540, y + h + 190, 40, False, a))
    E.frase(c, t, d5, ps("aí,", "i", 70, CLARO) + [("some um por um", "g", 76, BR)], 1540, 960, "center", 0.1)


# ---------------- questão ----------------
HX, HY, HW, HH = 1250, 700, 540, 225  # a horta: 6 m por 250 cm (90 px por metro)


def horta(c, t, t0, tb, a=1.0):
    E.foco(c, t, t0, 0.5, lambda q: M.rrect(c, HX, HY, HW, HH, 6, "#DDEFD9", q * a))
    E.foco(c, t, t0, 0.5, lambda q: c.drawRect(skia.Rect.MakeXYWH(HX, HY, HW, HH), M.paint(TINTA, q * a, stroke=4)))
    cota_h(c, t, t0 + 0.3, "6 m", HX, HX + HW, HY - 30, a=a)
    cota_v(c, t, t0 + 0.6, "250 cm", HX - 30, HY, HY + HH, a=a, size=46)
    # o portão: 2 m sem tela, no lado de baixo
    q = ep(t, tb, 0.5) * a
    if q > 0:
        gx = HX + HW - 240
        c.drawRect(skia.Rect.MakeXYWH(gx, HY + HH - 6, 180, 12), M.paint("#FFFFFF", q))
        tracejado(c, [(gx, HY + HH), (gx + 180, HY + HH)], ERRADO, q, 6)
        centro(c, "portão 2 m", gx + 90, HY + HH + 70, 46, "g", ERRADO, q)


def b_questao(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a6 - 0.6, ps("horta retangular", "i", 72), XE, 350, passo=0.1)
    E.foco(c, t, a6 + 0.3, 0.5, lambda a: E.escreve(c, "6 m × 250 cm", XE, 470, 90, "g", COR, a))
    E.frase(c, t, b6, ps("menos um", "i", 72) + [("portão de 2 m", "g", 72, ERRADO)], XE, 620, passo=0.1)
    E.frase(c, t, c6, ps("quantos", "i", 72) + [("metros de tela?", "g", 74, COR)], XE, 800, passo=0.1)
    horta(c, t, a6, b6)
    E.relogio(c, t, C["s17.a"], 1480, 300, 140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    E.frase(c, t, a8, ps("a", "i", 70) + [("mesma unidade", "g", 74, COR)], XE, 200, "left", 0.1)

    def um():
        ESC.degraus(c, t, C["s18"] + 0.1, acesos=(1, 2), ta=b8)
        ESC.pulos(c, t, 0, [(b8, 1), (b8 + 0.7, 2)], a8 + 0.3)
        num_un(c, t, "6", 1, [(b8, 2), (b8 + 0.7, 3)], 900, 400, 110, [(a8 + 0.3, "m"), (b8 + 0.7, "dm"), (b8 + 1.4, "cm")], t0=a8 + 0.3, some=True)
        fcen(c, t, c8, "600 + 250 = 850", 1370, 600, 88)
        fcen(c, t, d8, "850 × 2 = 1.700", 1370, 760, 88)
        E.foco(c, t, d8 + 0.8, 0.4, lambda a: E.escreve(c, "cm", 1700, 760, 64, "g", COR, a))
    E.saida(c, t, C["s19"] - 0.1, um)
    if t < C["s19"]:
        return
    ESC.degraus(c, t, C["s19"] + 0.1, acesos=(0, 1), ta=lerp(C["s19"], a9, 0.25))
    ESC.pulos(c, t, 2, [(lerp(C["s19"], a9, 0.25), 1), (lerp(C["s19"], a9, 0.25) + 0.7, 0)], C["s19"] + 0.1)
    h1 = lerp(C["s19"], a9, 0.25)
    px = num_un(c, t, "1700", 4, [(h1, 3), (h1 + 0.7, 2)], 900, 400, 110, [(C["s19"] + 0.1, "cm"), (h1 + 0.7, "dm"), (h1 + 1.4, "m")],
                t0=C["s19"] + 0.1, tv=h1 - 0.3)
    if px and t >= a9:
        E.risco(c, px(1) + 45, 420, px(3) + 45, 310, t, a9, largura=10)
    fcen(c, t, b9, "17 − 2 = 15", 1300, 620, 96)
    E.foco(c, t, b9 - 0.3, 0.4, lambda a: E.escreve(c, "portão", 1580, 620, 52, "i", ERRADO, a))
    bola_res(c, t, b9 + 1.3, "15 m", 1300, 800, 125, 76)
    E.frase(c, t, c9, ps("esqueceu o portão?", "i", 54, ERRADO) + [("tela a mais", "g", 54, ERRADO)], 960, 1010, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        itens = (("s20.a", "perímetro =", "a volta inteira"), ("s20.b", "some", "todos os lados"), ("s20.c", "tudo na", "mesma unidade"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 410 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 84) + [(l2, "g", 88, COR)], 430, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1, e1 = (C[f"s21.{k}"] for k in "abcde")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 80), XE, 240, passo=0.12)
    E.frase(c, t, a1, ps("o que fica", "i", 84) + [("dentro:", "g", 96)], XE, 380, passo=0.12)
    E.frase(c, t, a1 + 1.0, [("a área", "g", 140, COR)], XE, 540, passo=0.12)
    E.frase(c, t, b1, [("base × altura", "g", 76)], XE, 680, passo=0.1)
    # o chão do quarto enchendo de pisos
    E.foco(c, t, b1, 0.5, lambda a: c.drawRect(skia.Rect.MakeXYWH(1150, 250, 540, 360), M.paint(TINTA, a, stroke=4)))
    grade_q(c, t, c1, 6, 4, 1150, 250, 90, dur=1.6)
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1420, 760, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d1 + 0.3, 0.8))
    E.cursor(c, lerp(1750, 1560, p), lerp(970, 785, p), ep(t, d1 + 0.2, 0.4))
    E.frase(c, t, e1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conceito=b_conceito, retangulo=b_retangulo_total, unidades=b_unidades,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
