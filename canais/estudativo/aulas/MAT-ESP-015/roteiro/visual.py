"""Visual — Estudativo · MAT-ESP-015: partes da esfera: hemisfério, fuso e seção.
Mesma linguagem da trilha (MAT-ESP-001 a 014): E.esfera com a metade de trás do equador tracejada, o elemento da vez na cor
da matéria, a 2ª família em cinza, resposta na esfera. A esfera usa a inclinação 22°, como em MAT-ESP-014.
- HEMISFÉRIO: a própria E.esfera recortada (metade()): a de cima com o equador de trás tracejado; a de baixo (a tigela) com a
  tampa reta pintada e a borda inteira. As duas metades se afastam na vertical.
- FUSO: gomos de polo a polo (meridianos = meias elipses, meridiano()); o gomo da vez pintado (gomo()). Ao lado, a esfera
  vista de cima (pizza()): o ângulo do gomo como fatia. Regra de três numa tabela de duas colunas com a cruz (tabela()).
- CORTE (seção): uma faca reta (linha tracejada) com o círculo do corte (elipse pintada, secao()); o triângulo retângulo
  centro → centro do corte → borda, com a hipotenusa (o raio da esfera) em COR. O corte impossível sai em vermelho.
- ATALHO (palco): círculos contados em fila (4, 2, 3), cada um com a área πr².
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-015_partes_da_esfera.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("hemisferio", "fuso", "corte", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)
IN = 22
SEN, COS = math.sin(math.radians(IN)), math.cos(math.radians(IN))
assert 4 * 27 // 3 == 36 and 36 // 2 == 18 and 2 * 27 // 3 == 18 and 2 + 1 == 3 and 3 * 9 == 27
assert 6 ** 2 == 36 and 4 * 36 == 144 and 30 * 144 == 4320 and 4320 // 360 == 12 and 360 // 30 == 12 and 144 // 12 == 12
assert 5 ** 2 - 3 ** 2 == 16 and 4 ** 2 == 16 and 25 + 9 == 34 and 34 ** 0.5 > 5
assert 360 // 6 == 60 and 4 * 3 * 100 == 1200 and 1200 // 6 == 200 and 100 - 36 == 64 and 8 ** 2 == 64


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ², ³, √, π ou ° vai na grotesca)"""
    out = []
    for w in txt.split():
        g = any(ch in w for ch in "²³√π°")
        out.append((w, "g" if g else est, size * (0.92 if g and est != "g" else 1), cor))
    return out


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.5, tracejada=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def reto(c, P, A, B, k=30, a=1.0, cor=None):
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


def vertice(c, t, t0, P, r=15, cor=None, a=1.0):
    k = ease_back(prog(t, t0, 0.35))
    if k > 0 and a > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or E.COR, a))


def rot(c, t, t0, s, P, Q, n, size=56, cor=None, gap=14, a=1.0):
    """rótulo no meio do segmento PQ, afastado na direção n"""
    E.foco(c, t, t0, 0.4, lambda q: E._cola(c, s, (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2, n[0], n[1], gap, size, "g", cor or COR, q * a))


# ================= peças desta aula =================
def esfera(c, t, t0, cx, cy, r, raio=None, **kw):
    return E.esfera(c, t, t0, cx, cy, r, raio, inclina=IN, **kw)


def equador(c, cx, cy, r, a=1.0, cor=None, alfa_=0.45):
    if a <= 0:
        return
    ry = r * SEN
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, alfa_ * a))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, a, stroke=4))


def metade(c, t, t0, cx, cy, r, cima, a=1.0, tampa=0.0):
    """um hemisfério: a E.esfera recortada. cima = a metade de cima; a de baixo (tigela) mostra a tampa reta (tampa = 0..1 pinta)"""
    if a <= 0:
        return
    ry = r * SEN
    cr, el = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry)
    p = skia.Path()
    p.moveTo(cx - r, cy)
    if cima:
        p.arcTo(cr, 180, 180, False); p.arcTo(el, 0, 180, False)
    else:
        p.arcTo(cr, 180, -180, False); p.arcTo(el, 0, -180, False)
    p.close()

    def desenha():
        c.save(); c.clipPath(p, skia.ClipOp.kIntersect, True)
        esfera(c, t, t0, cx, cy, r)
        c.restore()
        if cima:
            c.drawArc(el, 0, 180, False, M.paint(TINTA, ep(t, t0, 0.5), stroke=5))
        else:
            c.drawOval(el, M.paint(E.mix(E.COR, "#FFFFFF", 0.55), 0.6 + 0.4 * tampa))
            if tampa > 0:
                c.drawOval(el, M.paint(E.COR, 0.45 * tampa))
            c.drawOval(el, M.paint(TINTA, ep(t, t0, 0.5), stroke=5))
    if a < 0.999:
        pa = skia.Paint(); pa.setAlphaf(a)
        c.saveLayer(None, pa); desenha(); c.restore()
    else:
        desenha()


def casca_baixo(c, cx, cy, r, a=1.0, cor=None, alfa_=0.4):
    """a casca curva da tigela pintada (meia esfera de baixo)"""
    if a <= 0:
        return
    ry = r * SEN
    p = skia.Path()
    p.moveTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 180, -180, False)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    c.drawPath(p, M.paint(cor or TINTA2, alfa_ * a))


def _mer(cx, cy, r, f):
    rx = max(abs(f) * r, 0.5)
    return skia.Rect.MakeXYWH(cx - rx, cy - r, 2 * rx, 2 * r)


def meridiano(c, cx, cy, r, f, a=1.0, cor=None, largura=4):
    """o meridiano da frente com abertura f = seno do ângulo (−1 a 1): meia elipse de polo a polo"""
    if a <= 0:
        return
    if abs(f) < 0.01:
        M.line(c, cx, cy - r, cx, cy + r, cor or TINTA, a, largura)
        return
    c.drawArc(_mer(cx, cy, r, f), -90, 180 if f > 0 else -180, False, M.paint(cor or TINTA, a, stroke=largura))


def gomo(c, cx, cy, r, f1, f2, a=1.0, cor=None, alfa_=0.55):
    """o gomo (fuso) entre os meridianos f1 < f2, pintado"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx, cy - r)
    p.arcTo(_mer(cx, cy, r, f2), -90, 180 if f2 >= 0 else -180, False)
    p.arcTo(_mer(cx, cy, r, f1), 90, -180 if f1 >= 0 else 180, False)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))
    c.drawPath(p, M.paint(cor or E.COR, a, stroke=5))


def gomos(c, cx, cy, r, n, a=1.0):
    """os meridianos da frente de uma bola com n gomos iguais (n par)"""
    for k in range(1, n // 2):
        meridiano(c, cx, cy, r, math.sin(math.radians(-90 + 360 / n * k)), a, TINTA2, 3)


def pizza(c, cx, cy, r, varre, a=1.0, cor=None, rotulo=None, size=56, ini=-90, cheia=0.55, raios=0):
    """a esfera vista de cima: círculo com a fatia de varre graus a partir de ini (graus da tela); raios = nº de divisões tracejadas"""
    if a <= 0:
        return
    rc = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    c.drawCircle(cx, cy, r, M.paint(E.mix(E.COR, "#FFFFFF", 0.9), a))
    for k in range(raios):
        an = math.radians(ini + 360 / raios * k)
        M.line(c, cx, cy, cx + r * math.cos(an), cy + r * math.sin(an), TINTA2, a * 0.7, 3, dash=E.TRACO)
    if varre > 0:
        p = skia.Path()
        if varre >= 359.9:
            p.addCircle(cx, cy, r)
        else:
            p.moveTo(cx, cy); p.arcTo(rc, ini, varre, False); p.close()
        c.drawPath(p, M.paint(cor or E.COR, cheia * a))
        pt = M.paint(cor or E.COR, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(p, pt)
        if rotulo and varre < 359:
            am = math.radians(ini + varre / 2)
            centro(c, rotulo, cx + r * 0.62 * math.cos(am), cy + r * 0.62 * math.sin(am) + size * 0.36, size, "g", TINTA, a)
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=5))
    c.drawCircle(cx, cy, 7, M.paint(TINTA, a))


def secao(c, cx, cy, r, k, a=1.0, cor=None, faca=True, w_faca=1.25):
    """o corte a k·r acima do centro (k pode ser negativo): a faca tracejada e o círculo do corte. Devolve (centro do corte, borda)"""
    k = max(-0.999, min(0.999, k))
    rr = r * math.sqrt(1 - k * k)
    ry, y = rr * SEN, cy - k * r * COS
    if a > 0:
        if faca:
            M.line(c, cx - r * w_faca, y, cx + r * w_faca, y, TINTA2, a * 0.8, 4, dash=E.TRACO)
        el = skia.Rect.MakeXYWH(cx - rr, y - ry, 2 * rr, 2 * ry)
        c.drawOval(el, M.paint(cor or E.COR, 0.5 * a))
        c.drawOval(el, M.paint(cor or E.COR, a, stroke=4))
    return (cx, y), (cx + rr, y)


def triangulo_corte(c, t, t0, O, Oc, P, a=1.0, t1=None, t2=None, t3=None, rots=(None, None, None), size=58, cor_h=None):
    """o triângulo do corte: O → Oc (distância ao centro) em t1, Oc → P (raio do corte) em t2, O → P (raio da esfera) em t3"""
    q = ep(t, t0, 0.5) * a
    if q > 0:
        p = skia.Path(); p.addPoly([O, Oc, P], True)
        c.drawPath(p, M.paint(E.COR, 0.22 * q))
        reto(c, Oc, O, P, 26, q)
    vertice(c, t, t0 if t1 is None else t1, O, 10, TINTA, a)
    for ti, (A, B), cor, larg, n, s in ((t1, (O, Oc), TINTA2, 9, (-1, 0), rots[0]), (t2, (Oc, P), TINTA, 9, (0, -1), rots[1]),
                                        (t3, (O, P), cor_h or E.COR, 11, (0.5, 0.8), rots[2])):
        if ti is not None:
            aresta(c, t, ti, A, B, cor, larg, a=a)
            if s:
                rot(c, t, ti + 0.3, s, A, B, n, size, cor if cor != TINTA2 else TINTA, a=a)


def circulos(c, t, ts, x0, y, r, gap, cor=None, borda=BR, a=1.0):
    """fila de círculos (o círculo do meio, de área πr²), cada um entra no seu instante"""
    for k, tk in enumerate(ts):
        q = ease_back(prog(t, tk, 0.4))
        if q > 0:
            cx = x0 + k * (2 * r + gap)
            c.drawCircle(cx, y, r * q, M.paint(cor or E.COR, 0.9 * a))
            c.drawCircle(cx, y, r * q, M.paint(borda, a, stroke=5))


def tabela(c, t, xa, xb, y, cabecas, linhas, tc=None, cor=None):
    """regra de três: cabecas = (t0, nome_a, nome_b); linhas = [(t0, a, b, cor_b)]; a cruz em tc"""
    t0, na, nb = cabecas
    E.foco(c, t, t0, 0.5, lambda q: (centro(c, na, xa, y, 54, "i", TINTA2, q), centro(c, nb, xb, y, 54, "i", TINTA2, q),
                                      M.line(c, xa - 150, y + 30, xb + 150, y + 30, FIO, q, 3)))
    for i, (ti, va, vb, cb) in enumerate(linhas):
        yy = y + 140 + i * 130
        fcen(c, t, ti, va, xa, yy, 84)
        fcen(c, t, ti + 0.3, vb, xb, yy, 84, cb)
    if tc is not None:
        p = ep(t, tc, 0.6)
        if p > 0:
            y1, y2 = y + 140 - 30, y + 270 - 30
            M.line(c, xa + 90, y1, xb - 90, y2, cor or E.COR, p, 6, progress=p)
            M.line(c, xa + 90, y2, xb - 90, y1, cor or E.COR, p, 6, progress=p)


# ---------------- gancho ----------------
GX, GY, GR = 500, 600, 300   # a laranja de raio 5 (60 px por cm)


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        esfera(c, t, a1, GX, GY, GR)
        E.frase(c, t, a1 + 0.2, ps("uma", "i", 64) + [("laranja", "g", 68, COR)] + ps("de raio 5 cm", "i", 64), 1050, 220, "left", 0.1)
        if t >= b1:
            k = lerp(0.95, 0.6, ease_io(prog(t, b1, 0.9)))
            Oc, P = secao(c, GX, GY, GR, k, ep(t, b1, 0.4))
            if t >= b1 + 1.0:
                triangulo_corte(c, t, b1 + 1.0, (GX, GY), Oc, P, t1=b1 + 1.0, t2=b1 + 1.4, t3=b1 + 1.8,
                                rots=("3", "?" if t < c1 else "4", "5"))
        E.frase(c, t, b1, ps("corte", "i", 64) + [("reto", "g", 68, COR)] + ps("a 3 cm do centro", "i", 64), 1050, 360, "left", 0.1)
        E.frase(c, t, b1 + 1.6, ps("raio do círculo do corte?", "i", 64), 1050, 500, "left", 0.1)
        bola_txt(c, t, c1, "4 cm", 1300, 720, 120, 70)
        E.foco(c, t, c1 + 0.8, 0.5, lambda q: E.pilula(c, "Pitágoras", 1620, 720, 64, "g", a=q, cor=E.SOBRE, fundo=TINTA))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("as partes", "g", 104, COR)] + ps("da esfera", "i", 90), XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("a metade, o gomo", "i", 80), XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("e o corte", "i", 80), XE, 700, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "esfera:", "A = 4πr^2    V = f{4πr³}{3}"), ("s03.c", "Pitágoras:", "a^2 = b^2 + c^2"),
             ("s03.d", "regra de três direta:", "a tabela e a cruz"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 72, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 166, 56, "g", COR)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- hemisfério ----------------
HX, HY, HR = 480, 600, 250


def b_hemisferio(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    sep = 70 * ease_io(prog(t, b4, 0.8))
    cima = 1 - ep(t, C["s05"], 0.5)          # a metade de cima sai; a tigela fica
    if t < b4:
        esfera(c, t, a4, HX, HY, HR)
        if t >= a4 + 0.6:
            secao(c, HX, HY, HR, 0.0, ep(t, a4 + 0.6, 0.4), faca=True, w_faca=1.3)
    else:
        metade(c, t, a4, HX, HY - sep, HR, True, cima)
        metade(c, t, a4, HX, HY + sep * (1 - ep(t, C["s05"], 0.6)), HR, False, 1.0, tampa=ep(t, c6, 0.5))
        casca_baixo(c, HX, HY + sep * (1 - ep(t, C["s05"], 0.6)), HR, ep(t, a6, 0.5) * (1 - ep(t, d6, 0.4)), E.COR, 0.35)
    if t >= a5:
        Y = HY + sep * (1 - ep(t, C["s05"], 0.6))
        aresta(c, t, a5, (HX, Y), (HX + HR, Y), TINTA, 6)
        E.foco(c, t, a5 + 0.3, 0.4, lambda q: E._cola(c, "3", HX + HR / 2, Y, 0, -1, 8, 56, "g", TINTA, q))
    X = 1320

    def corta():
        E.frase(c, t, a4, ps("corte bem no", "i", 64) + [("meio", "g", 68, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b4, [("2 hemisférios", "g", 72, COR)], X, 400, "center", 0.1)
        E.frase(c, t, b4 + 0.8, ps("duas metades iguais", "i", 56, TINTA2), X, 480, "center", 0.1)
        E.frase(c, t, lerp(b4, c4, 0.5), ps("uma tigela com tampa reta", "i", 56), X, 600, "center", 0.1)
        E.frase(c, t, c4, ps("volume =", "i", 64) + [("metade", "g", 70, COR)] + ps("da esfera", "i", 64), X, 780, "center", 0.1)
    fase(c, t, C["s04"], C["s05"] - 0.1, corta)

    def volume():
        E.frase(c, t, a5, ps("raio 3: esfera", "i", 62) + [("36π", "g", 66, COR)], X, 240, "center", 0.1)
        fcen(c, t, b5, "36π ÷ 2", X - 180, 460, 84)
        bola_txt(c, t, b5 + 0.6, "18π", X + 220, 435, 105, 72)
        E.frase(c, t, c5, ps("na fórmula:", "i", 58), X, 700, "center", 0.1)
        fcen(c, t, c5 + 0.5, "V = f{2πr³}{3}", X, 860, 110, COR)
    fase(c, t, C["s05"], C["s06"] - 0.1, volume)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, C["s06"] + 0.1, ps("e a área?", "i", 64), X, 200, "center", 0.1)
    E.frase(c, t, a6, ps("metade da", "i", 58) + [("casca", "g", 62, COR)], X - 230, 330, "center", 0.1)
    E.frase(c, t, b6, ps("=", "i", 58) + [("2 círculos", "g", 62, COR)], X + 200, 330, "center", 0.1)
    E.frase(c, t, c6, ps("+ a", "i", 58) + [("tampa", "g", 62, COR)] + ps("= 1 círculo", "i", 58), X, 450, "center", 0.1)
    circulos(c, t, (b6, b6 + 0.3, c6 + 0.3), X - 220, 600, 70, 80, E.COR, TINTA)
    fcen(c, t, d6, "A = 3πr^2", X, 820, 110, COR)
    fcen(c, t, e6, "3 × 9 = 27", X - 180, 990, 70)
    bola_txt(c, t, e6 + 0.6, "27π", X + 200, 965, 85, 60)


# ---------------- fuso ----------------
FX, FY, FR = 430, 600, 290
F30, F60 = math.sin(math.radians(30)), math.sin(math.radians(60))


def b_fuso(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    PX, PY, PR = 1060, 640, 190     # a vista de cima, ao lado da bola (s07-s08)

    def bola():
        esfera(c, t, a7, FX, FY, FR)
        gomos(c, FX, FY, FR, 12, ep(t, a7 + 0.6, 0.5))
        dobra = ease_io(prog(t, a8, 0.8))
        f2 = lerp(F30, F60, dobra)
        gomo(c, FX, FY, FR, 0.0, f2, ep(t, b7, 0.5))
        E.foco(c, t, b7 + 0.5, 0.4, lambda q: centro(c, "bola de praia", FX, FY + FR + 80, 50, "i", TINTA2, q))
        q = ep(t, c7, 0.5)
        if q > 0:
            varre = lerp(30, 60, dobra) if t < c8 else lerp(60, 360, ease_io(prog(t, c8, 1.0)))
            pizza(c, PX, PY, PR, varre, q, rotulo=f"{round(varre)}°" if varre < 359 else None, size=46, raios=12)
            E.foco(c, t, c7 + 0.3, 0.4, lambda q2: centro(c, "vista de cima", PX, PY + PR + 70, 46, "i", TINTA2, q2))
    fase(c, t, C["s07"], C["s09"] - 0.1, bola)
    X = 1560

    def texto():
        E.frase(c, t, a7, [("fuso", "g", 92, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b7, ps("a casca de", "i", 58) + [("um gomo", "g", 62, COR)], X, 350, "center", 0.1)
        E.frase(c, t, lerp(b7, c7, 0.6), ps("de polo a polo", "i", 54, TINTA2), X, 440, "center", 0.1)
        E.frase(c, t, c7, ps("abre num", "i", 58) + [("ângulo", "g", 62, COR)], X, 560, "center", 0.1)
    fase(c, t, C["s07"], C["s08"] - 0.1, texto)

    def prop():
        E.frase(c, t, a8, ps("ângulo", "i", 58) + [("× 2", "g", 64, COR)], X, 240, "center", 0.1)
        E.frase(c, t, a8 + 0.7, ps("gomo", "i", 58) + [("× 2", "g", 64, COR)], X, 330, "center", 0.1)
        E.foco(c, t, b8, 0.5, lambda q: E.pilula(c, "diretamente", X, 470, 54, "g", a=q, cor=E.SOBRE))
        E.foco(c, t, b8 + 0.3, 0.5, lambda q: E.pilula(c, "proporcionais", X, 550, 54, "g", a=q, cor=E.SOBRE))
        E.frase(c, t, c8, [("360°", "g", 66, COR)] + ps("= a esfera inteira", "i", 56), X, 700, "center", 0.1)
        E.frase(c, t, d8, ps("então,", "i", 60) + [("regra de três", "g", 66, COR)], X, 860, "center", 0.1)
    fase(c, t, C["s08"], C["s09"] - 0.1, prop)
    if t < C["s09"] - 0.1:
        return
    # s09-s10: a vista de cima à esquerda, a tabela à direita
    qx, qy, qr = 400, 620, 230
    cunha = ep(t, c0, 0.5)
    pizza(c, qx, qy, qr, 30, ep(t, C["s09"], 0.5), rotulo="30°", size=52, raios=12, cheia=0.55 + 0.4 * cunha)
    E.foco(c, t, a9 + 0.4, 0.4, lambda q: centro(c, "raio 6", qx, qy + qr + 80, 54, "g", TINTA, q))
    X = 1300

    def conta():
        E.frase(c, t, a9, ps("fuso de", "i", 58) + [("30°", "g", 64, COR)] + ps("numa esfera de", "i", 58) + [("raio 6", "g", 64, COR)],
                X, 200, "center", 0.1)
        fcen(c, t, b9, "esfera: 4π · 6² = 4π · 36 = 144π", X, 320, 60)
        tabela(c, t, X - 220, X + 220, 450, (c9 - 0.3, "ângulo", "área"),
               [(c9, "360°", "144π", TINTA), (d9, "30°", "x", COR)], tc=a0)
        fcen(c, t, a0 + 0.4, "360x = 30 · 144π = 4.320π", X, 860, 64)
        fcen(c, t, b0, "x = 4.320π ÷ 360", X - 170, 990, 64)
        bola_txt(c, t, b0 + 0.7, "12π", X + 300, 960, 85, 64)
    fase(c, t, C["s09"], c0 - 0.1, conta)
    if t < c0 - 0.1:
        return
    E.frase(c, t, c0, ps("gomo inteiro, casca e dentro:", "i", 58), X, 260, "center", 0.1)
    E.frase(c, t, c0 + 0.8, [("cunha", "g", 96, COR)], X, 400, "center", 0.1)
    fcen(c, t, d0, "30° = f{1}{12} da volta", X, 600, 80)
    fcen(c, t, d0 + 1.2, "cunha = f{1}{12} da esfera", X, 820, 80, COR)


# ---------------- o corte (seção) ----------------
def b_corte(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2 = C["s12.a"], C["s12.b"], C["s12.c"]
    a3, b3, c3, d3, e3, f3 = (C[f"s13.{k}"] for k in "abcdef")
    esfera(c, t, C["s11"], GX, GY, GR)
    # a faca desce: aparece um círculo; no meio é o maior; longe do centro, menor
    if t >= b1:
        if t < c1:
            k = lerp(0.9, 0.45, ease_io(prog(t, b1, 1.4)))
        elif t < d1:
            k = lerp(0.45, 0.0, ease_io(prog(t, c1, 0.9)))
        elif t < C["s12"]:
            k = lerp(0.0, 0.6, ease_io(prog(t, d1, 0.9)))
        else:
            k = 0.6
        Oc, P = secao(c, GX, GY, GR, k, ep(t, b1, 0.4))
        if t >= C["s12"]:
            triangulo_corte(c, t, a3, (GX, GY), Oc, P, t1=a2, t2=b2, t3=c2, rots=("3", "?" if t < f3 else "4", "5"))
    X = 1360

    def sempre():
        E.frase(c, t, a1, [("o corte", "g", 88, COR)], X, 240, "center", 0.1)
        E.frase(c, t, lerp(a1, b1, 0.4), ps("uma faca reta, em qualquer lugar", "i", 54, TINTA2), X, 340, "center", 0.08)
        E.frase(c, t, b1, ps("aparece sempre um", "i", 60) + [("círculo", "g", 64, COR)], X, 480, "center", 0.1)
        E.frase(c, t, c1, ps("pelo centro: o", "i", 58) + [("maior", "g", 62, COR)], X, 640, "center", 0.1)
        E.frase(c, t, d1, ps("longe do centro:", "i", 58) + [("menor", "g", 62, COR)], X, 760, "center", 0.1)
    fase(c, t, C["s11"], C["s12"] - 0.1, sempre)

    def lados():
        E.frase(c, t, C["s12"] + 0.1, ps("laranja de raio 5, corte a 3 do centro", "i", 52, TINTA2), X, 220, "center", 0.08)
        E.frase(c, t, a2, ps("do centro ao centro do corte:", "i", 56) + [("3", "g", 62, COR)], X, 380, "center", 0.1)
        E.frase(c, t, b2, ps("do centro do corte à borda:", "i", 56) + [("?", "g", 62, COR)], X, 500, "center", 0.1)
        E.frase(c, t, c2, ps("do centro à borda:", "i", 56) + [("5", "g", 62, COR)], X, 620, "center", 0.1)
        E.frase(c, t, c2 + 0.8, ps("o raio da esfera", "i", 50, TINTA2), X, 700, "center", 0.1)
    fase(c, t, C["s12"], C["s13"] - 0.1, lados)
    if t < C["s13"] - 0.1:
        return
    E.frase(c, t, a3, [("triângulo retângulo", "g", 64, COR)], X, 220, "center", 0.1)
    E.frase(c, t, a3 + 0.8, ps("hipotenusa = o raio da esfera", "i", 52, TINTA2), X, 300, "center", 0.1)
    fcen(c, t, b3, "5² = 25", X - 200, 440, 78)
    fcen(c, t, c3, "3² = 9", X + 200, 440, 78)
    fcen(c, t, d3, "25 − 9 = 16", X, 590, 84)
    fcen(c, t, e3, "r{16} = 4", X - 160, 790, 90, COR)
    bola_txt(c, t, f3, "4 cm", X + 230, 760, 100, 60)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    esfera(c, t, C["s14"], GX, GY, GR)
    Oc, P = secao(c, GX, GY, GR, 0.6, 1.0)
    triangulo_corte(c, t, C["s14"], (GX, GY), Oc, P, t1=C["s14"], t2=C["s14"], t3=C["s14"], rots=("3", None, "5"))
    # o corte impossível: maior que o círculo do meio
    q = ep(t, c4, 0.5)
    if q > 0:
        rr = GR * math.sqrt(34) / 5
        el = skia.Rect.MakeXYWH(GX - rr, Oc[1] - rr * SEN, 2 * rr, 2 * rr * SEN)
        pt = M.paint(ERRADO, q, stroke=6); pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawOval(el, M.paint(ERRADO, 0.12 * q)); c.drawOval(el, pt)
        E.foco(c, t, c4 + 0.3, 0.4, lambda q2: E.selo(c, GX + rr + 10, Oc[1] - 80, 44, False, q2))
    X = 1360
    E.frase(c, t, C["s14"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 200, "center", 0.1)
    E.frase(c, t, a4, [("somar", "g", 64, ERRADO)] + ps("os quadrados", "i", 60), X, 300, "center", 0.1)
    fcen(c, t, a4 + 0.8, "25 + 9 = 34", X, 450, 84, ERRADO)
    fcen(c, t, b4, "r{34} > 5", X, 600, 84, ERRADO)
    E.frase(c, t, c4, ps("corte maior que o do meio?", "i", 56), X, 740, "center", 0.1)
    E.frase(c, t, c4 + 0.8, [("impossível", "g", 66, ERRADO)], X, 830, "center", 0.1)
    E.foco(c, t, d4, 0.5, lambda q: E.pilula(c, "hipotenusa é o maior: subtraia", X, 970, 52, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]

    def um():
        E.frase(c, t, C["s15"] + 0.2, ps("atalho da área do hemisfério:", "i", 64, CLARO), W / 2, 180, "center", 0.1)
        E.frase(c, t, a5, [("conte círculos", "g", 84, BR)], W / 2, 290, "center", 0.1)
        x0 = 940
        for y, rotl, n, tk in ((430, "esfera inteira", 4, b5), (600, "meia casca", 2, c5), (770, "com a tampa", 3, d5)):
            E.frase(c, t, tk, ps(rotl, "i", 56, CLARO), x0 - 100, y + 18, "right", 0.1)
            circulos(c, t, [tk + 0.2 + 0.15 * k for k in range(n)], x0, y, 62, 36)
            E.foco(c, t, tk + 0.3 + 0.15 * n, 0.4, lambda q, n=n, y=y: E.escreve(c, f"= {n}", x0 + n * 160 - 10, y + 26, 70, "g", BR, q))
        fcen(c, t, e5, "A = 3πr^2", W / 2, 960, 110, BR)
    fase(c, t, C["s15"], C["s16"] - 0.1, um)
    if t < C["s16"] - 0.1:
        return
    E.frase(c, t, C["s16"] + 0.1, ps("funciona porque", "i", 64, CLARO), W / 2, 200, "center", 0.1)
    E.frase(c, t, a6, ps("tudo no mesmo círculo, de área", "i", 60, CLARO) + [("πr²", "g", 66, BR)], W / 2, 330, "center", 0.1)
    circulos(c, t, (a6 + 0.6,), W / 2, 480, 70, 0)
    E.foco(c, t, b6, 0.5, lambda a: E.selo(c, 420, 680, 44, False, a))
    E.frase(c, t, b6 + 0.1, ps("cuidado: tigela aberta, cúpula sem piso", "i", 56, CLARO), 490, 702, "left", 0.1)
    E.frase(c, t, lerp(b6, c6, 0.6), ps("não tem tampa", "i", 56, CLARO), 490, 800, "left", 0.1)
    E.foco(c, t, c6, 0.5, lambda a: E.pilula(c, "só 2 círculos: 2πr²", W / 2, 960, 62, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
QX, QY, QR = 1460, 600, 260


def b_questao(c, t, C, b):
    a7, b7, c7, d7, e7, f7 = (C[f"s17.{k}"] for k in "abcdef")
    E.frase(c, t, C["s17"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 180, passo=0.12)
    E.frase(c, t, a7, ps("bola de plástico de", "i", 58) + [("raio 10 cm", "g", 62, COR)], XE, 300, passo=0.1)
    E.frase(c, t, b7, [("6 gomos", "g", 62, COR)] + ps("iguais", "i", 58), XE, 400, passo=0.1)
    E.frase(c, t, c7, [("π = 3", "g", 62, COR)], XE, 500, passo=0.1)
    E.frase(c, t, d7, [("1)", "g", 60, COR)] + ps("quanto plástico tem um gomo?", "i", 58), XE, 660, passo=0.1)
    E.frase(c, t, e7, [("2)", "g", 60, COR)] + ps("corte reto a", "i", 58) + [("6 cm", "g", 62, COR)] + ps("do centro:", "i", 58), XE, 770, passo=0.1)
    E.frase(c, t, f7, ps("qual o raio do círculo do corte?", "i", 58), XE + 70, 860, passo=0.1)

    def bola():
        esfera(c, t, a7, QX, QY, QR)
        an = math.radians(35)
        Q = (QX + QR * math.cos(an), QY + QR * math.sin(an))
        if t >= a7 + 0.5:
            vertice(c, t, a7 + 0.5, (QX, QY), 9, TINTA)
            aresta(c, t, a7 + 0.5, (QX, QY), Q, TINTA, 6)
            rot(c, t, a7 + 0.8, "10 cm", (QX, QY), Q, (0.6, -0.8), 50, COR)
        gomos(c, QX, QY, QR, 6, ep(t, b7, 0.5))
        gomo(c, QX, QY, QR, -0.5, 0.5, ep(t, d7, 0.5))
        if t >= e7:
            secao(c, QX, QY, QR, 0.6, ep(t, e7, 0.5))
    E.saida(c, t, C["s18.a"] - 0.1, bola)
    E.relogio(c, t, C["s18.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    X = 1300

    def gomo1():
        pizza(c, 420, 600, 240, 60 * ease_io(prog(t, a9, 0.8)), ep(t, C["s19"], 0.5), rotulo="60°", size=54, raios=6)
        E.foco(c, t, C["s19"] + 0.3, 0.4, lambda q: centro(c, "vista de cima", 420, 920, 50, "i", TINTA2, q))
        E.frase(c, t, C["s19"] + 0.2, [("1)", "g", 64, COR)] + ps("um gomo", "i", 62), X, 200, "center", 0.1)
        fcen(c, t, a9, "360° ÷ 6 = 60°", X, 360, 80)
        fcen(c, t, b9, "= f{1}{6} da bola", X, 500, 76, COR)
        fcen(c, t, c9, "4 × 3 × 100 = 1.200 cm²", X, 680, 74)
        fcen(c, t, d9, "1.200 ÷ 6", X - 200, 900, 80)
        bola_txt(c, t, d9 + 0.6, "200 cm²", X + 210, 875, 125, 54)
    fase(c, t, C["s19"], C["s20"] - 0.1, gomo1)
    if t < C["s20"] - 0.1:
        return
    cx, cy, r = 450, 600, 280
    esfera(c, t, C["s20"], cx, cy, r)
    Oc, P = secao(c, cx, cy, r, 0.6, ep(t, C["s20"] + 0.3, 0.4))
    triangulo_corte(c, t, C["s20"] + 0.5, (cx, cy), Oc, P, t1=C["s20"] + 0.5, t2=C["s20"] + 0.7, t3=C["s20"] + 0.9,
                    rots=("6", "?" if t < e0 else "8", "10"))
    E.frase(c, t, C["s20"] + 0.2, [("2)", "g", 64, COR)] + ps("o corte", "i", 62), X, 200, "center", 0.1)
    fcen(c, t, a0, "10² = 100", X - 200, 360, 78)
    fcen(c, t, b0, "6² = 36", X + 200, 360, 78)
    fcen(c, t, c0, "100 − 36 = 64", X, 520, 84)
    fcen(c, t, d0, "r{64} = 8", X, 690, 90, COR)
    bola_txt(c, t, e0, "8 cm", X - 150, 890, 100, 60)
    E.foco(c, t, e0 + 0.6, 0.5, lambda q: E.selo(c, X + 70, 890, 44, True, q))
    E.frase(c, t, e0 + 0.8, ps("menor que 10", "i", 56, CERTO), X + 130, 910, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s21.a", "hemisfério:", "metade do volume, 3 círculos de área"), ("s21.b", "fuso:", "a fração do ângulo"),
                 ("s21.c", "corte:", "Pitágoras, raio da esfera na hipotenusa"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 430 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 25, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", E.SOBRE, a)))
            wl = E.frase(c, t, C[k] + 0.1, ps(l1, "i", 64), 390, y, "left", 0.12)
            E.frase(c, t, C[k] + 0.5, [(l2, "g", 56, COR)], 390 + wl + 24, y, "left", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    a2, b2, c2, d2 = (C[f"s22.{k}"] for k in "abcd")
    E.frase(c, t, C["s22"] + 0.2, ps("na próxima aula", "i", 80), XE, 230, passo=0.12)
    E.frase(c, t, C["s22"] + 0.8, [("praticar", "g", 110, COR)] + ps("tudo isso", "i", 92), XE, 380)
    E.frase(c, t, a2, ps("a fórmula de cada sólido", "i", 58), XE, 500, passo=0.1)
    E.frase(c, t, b2, ps("casquinha, tenda, bola, reservatório", "i", 54, TINTA2), XE, 600, passo=0.1)
    E.piramide(c, t, a2, 1240, 840, 4, 110, 220)
    E.cone(c, t, a2 + 0.3, 1520, 840, 95, 250)
    esfera(c, t, a2 + 0.6, 1740, 750, 95)
    E.foco(c, t, c2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(620, 355, p), ep(t, c2 + 0.2, 0.4))
    E.frase(c, t, d2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1010, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, hemisferio=b_hemisferio, fuso=b_fuso, corte=b_corte, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
