"""Visual — Estudativo · MAT-TRI-010: relação fundamental (sen²x + cos²x = 1; sen x = 3/5 → cos x = 4/5, tg x = 3/4).
Linguagem da trigonometria (MAT-TRI-001) no ciclo (MAT-TRI-007): figuras em tinta; o ângulo da vez é o arco na cor da matéria.
O triângulo dentro do ciclo leva as cores fixas dos lados: hipotenusa = raio 1 em índigo (HIP), o lado deitado = cos x em
petróleo (ADJ, o adjacente) e o lado em pé = sen x em âmbar (OPO, o oposto). As mesmas cores pintam "sen x" e "cos x" nas contas.
Resposta na esfera ou na pílula; erro em vermelho, certo em verde; atalho no palco escuro (lá, ADJ_ESC e CLARO).
A figura não mente: o ponto do exemplo está em 36,87° (cos 4/5, sen 3/5) e o da questão em 298,07° (cos 8/17, sen −15/17).
Peças locais: cf() (conta com partes coloridas), tri_ciclo() (o triângulo dentro do ciclo), tri() e rot() (de MAT-TRI-001), resp().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-010_relacao_fundamental_da_trigonometria.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ciclo", "exemplo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"
ADJ_ESC = "#3CC7D3"
X35 = math.degrees(math.asin(3 / 5))          # 36,87°: cos 4/5, sen 3/5
X4Q = 360 - math.degrees(math.acos(8 / 17))   # 298,07°: cos 8/17, sen −15/17
assert abs(math.cos(math.radians(X35)) - 0.8) < 1e-12 and abs(math.sin(math.radians(X4Q)) + 15 / 17) < 1e-12
assert 9 + 16 == 25 and 25 - 9 == 16 and 1 + 3 == 4 and 9 + 4 == 13 and 17 ** 2 == 289 and 8 ** 2 == 64 and 289 - 64 == 225 == 15 ** 2
assert abs((3 / 5) / (4 / 5) - 3 / 4) < 1e-12 and 1 - 3 / 5 == 2 / 5 and 225 + 64 == 289


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """conta numa linha com partes coloridas: [(texto, cor), ...]; y = linha de base. Devolve a largura"""
    w = sum(_w(s, size, est) for s, _ in partes)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for s, cor in partes:
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += _w(s, size, est)
    return w


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def resp(c, t, t0, partes, cx, cy, size=76, alto=1.75, cor=None):
    """resposta na pílula da cor da matéria; partes = texto ou [(texto, cor)]"""
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size, 0) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def grosso(c, P, Q, cor, a, larg=12, p=1.0):
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, progress=p)


def rotulo_lado(c, P, Q, s, G, size, cor, a, gap=26, fundo=False):
    """fórmula centrada ao lado do segmento PQ, do lado oposto ao ponto G"""
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    w = _w(s, size)
    hh = size * (0.95 if s.startswith(("f{", "−f{")) else 0.5)
    # afasta o centro do rótulo o bastante para a caixa (w x 2hh) não tocar o segmento
    d = gap + abs(nx) * w / 2 + abs(ny) * hh
    X, Y = mx + nx * d, my + ny * d
    if fundo:  # papel por trás: o rótulo pode cruzar a circunferência sem sujar
        M.rrect(c, X - w / 2 - 10, Y - hh - 8, w + 20, 2 * hh + 16, 14, E.PAPEL, 0.92 * a)
    E.formula(c, s, X, Y + size * 0.36, size, "g", cor, a, "center")


def tri_ciclo(c, t, cx, cy, r, ang, td=None, tf=None, th=None, tc=None, ts=None, rh=None, rc=None, rs=None,
              size=56, escuro=False, a=1.0, cc=None, cs=None):
    """o triângulo retângulo dentro do ciclo: O, o pé no eixo horizontal e o ponto P do arco.
    td = tracejado que desce de P; tf = triângulo aceso com o ângulo reto; th/tc/ts = hipotenusa, cos e sen pintados;
    rh/rc/rs = rótulos (texto ou função t → texto)"""
    if a <= 0:
        return
    co, se = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    O, P, F = (cx, cy), (cx + r * co, cy - r * se), (cx + r * co, cy)
    G = ((O[0] + P[0] + F[0]) / 3, (O[1] + P[1] + F[1]) / 3)
    tinta = BR if escuro else TINTA
    if tf is not None and t >= tf:
        q = ep(t, tf, 0.6) * a
        path = skia.Path(); path.moveTo(*O); path.lineTo(*F); path.lineTo(*P); path.close()
        c.drawPath(path, M.paint(E.COR, (0.22 if escuro else 0.13) * q))
        k = 26
        sx, sy = (-1 if co > 0 else 1), (-1 if se > 0 else 1)
        sq = skia.Path(); sq.moveTo(F[0] + sx * k, F[1]); sq.lineTo(F[0] + sx * k, F[1] + sy * k); sq.lineTo(F[0], F[1] + sy * k)
        c.drawPath(sq, M.paint(tinta, q, stroke=4))
    if td is not None and t >= td:
        M.line(c, *P, *F, tinta, 0.8 * a, 5, dash=E.TRACO, progress=ep(t, td, 0.6))
    for t_, P1, Q1, cor, rot_ in ((th, O, P, HIP if not escuro else CLARO, rh), (tc, O, F, cc or (ADJ if not escuro else ADJ_ESC), rc),
                                  (ts, F, P, cs or OPO, rs)):
        if t_ is None or t < t_:
            continue
        grosso(c, P1, Q1, cor, a, 12, ease_io(prog(t, t_, 0.5)))
        s = rot_(t) if callable(rot_) else rot_
        if s:
            E.foco(c, t, t_ + 0.3, 0.4, lambda b, P1=P1, Q1=Q1, s=s, cor=cor: rotulo_lado(c, P1, Q1, s, G, size * (1.25 if s.startswith(("f{", "−f{")) else 1), cor, b * a, fundo=not escuro))
    return P


def base_ciclo(c, t, t0, cx, cy, r, ang, ta, escuro=False, a=1.0):
    """o ciclo do kit (eixos, 1 e −1, o arco x e o ponto P), sem o seno e o cosseno do kit: o triângulo vem de tri_ciclo"""
    if a <= 0 or t < t0:
        return
    if a < 1:
        pt = skia.Paint(); pt.setAlphaf(a); c.saveLayer(None, pt)
    E.trigono(c, t, t0, cx, cy, r, ang, rotulo="x", seno=False, cosseno=False, ponto_="P", ts={"circulo": t0, "raio": ta},
              size=50, escuro=escuro)
    if a < 1:
        c.restore()


def rot(c, P, Q, s, G, size=60, cor=None, a=1.0, gap=20, est="b"):
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, est, cor or TINTA, a)


def tri(c, t, t0, A, R, T, med, tm, cores, escuro=False, size=70, alfa=None):
    """triângulo retângulo da MAT-TRI-001: A = vértice do ângulo x, R = reto, T = o outro. Lados "adj" A–R, "opo" R–T, "hip" A–T.
    med = {lado: texto ou função t → texto}; tm = {lado: instante}; cores = {lado: (instante, cor)}"""
    G = ((A[0] + R[0] + T[0]) / 3, (A[1] + R[1] + T[1]) / 3)
    E.triangulo(c, t, t0, A, R, T, vertices=None, retos=(1,), preenche=0.07, d=0.9, escuro=escuro)
    seg = {"adj": (A, R), "opo": (R, T), "hip": (A, T)}
    for k, (P, Q) in seg.items():
        cor_k = None
        if k in cores and t >= cores[k][0]:
            cor_k = cores[k][1]
            grosso(c, P, Q, cor_k, 1.0, 12, ease_io(prog(t, cores[k][0], 0.5)))
        if k in tm and k in med:
            s = med[k](t) if callable(med[k]) else med[k]
            cor_t = cor_k or (BR if escuro else TINTA)
            E.foco(c, t, tm[k], 0.4, lambda a, P=P, Q=Q, s=s, cor_t=cor_t: rot(c, P, Q, s, G, size, cor_t, a, 22, "g"))
    if alfa is not None:
        E.angulo(c, t, alfa, A, R, T, "x", r=95, size=54)
    return G


def sen_x(cor=OPO):
    return ("sen x", cor)


def cos_x(cor=ADJ):
    return ("cos x", cor)


def relacao(c, x, y, size, a=1.0, align="center", escuro=False):
    """sen²x + cos²x = 1, com o seno em âmbar e o cosseno em petróleo"""
    tinta = BR if escuro else TINTA
    return cf(c, [("sen²x", OPO), (" + ", tinta), ("cos²x", ADJ_ESC if escuro else ADJ), (" = 1", tinta)], x, y, size, a, align)


# ---------------- gancho ----------------
GX, GY_, GR = 1420, 600, 300


def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    tq = lerp(a1, b1, 0.55)  # "Quanto vale o cosseno?"

    def um():
        cf_em(c, t, a1, [sen_x(), (" = f{3}{5}", TINTA)], XE, 300, 110)
        E.foco(c, t, a1 + 0.8, 0.5, lambda a: E.pilula(c, "1º quadrante", XE + 680, 268, 50, "g", a=a, cor=E.SOBRE))
        cf_em(c, t, tq, [cos_x(), (" = ?", TINTA)], XE, 540, 110)
        cf_em(c, t, b1, [("1 − f{3}{5} = f{2}{5}", ERRADO)], XE, 760, 96)
        if t >= b1 + 1.2:
            E.risco(c, XE - 10, 800, XE + _w("1 − f{3}{5} = f{2}{5}", 96) + 10, 700, t, b1 + 1.2, ERRADO, 10)
        cf_em(c, t, c1, [cos_x(), (" = f{4}{5}", CERTO)], XE, 960, 110)
        E.foco(c, t, c1 + 0.4, 0.5, lambda a: E.selo(c, XE + _w("cos x = f{4}{5}", 110) + 80, 925, 44, True, a))
        base_ciclo(c, t, a1 + 0.2, GX, GY_, GR, X35, a1 + 1.0)
        tri_ciclo(c, t, GX, GY_, GR, X35, td=a1 + 1.6, tf=a1 + 1.6, ts=a1 + 2.0, rs="f{3}{5}", tc=tq,
                  rc=lambda tt: "f{4}{5}" if tt >= c1 else "?", size=58)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 640, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 260, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.15), [("cos", "g", 100, ADJ)] + ps("pelo", "i", 90) + [("sen", "g", 100, OPO)], XE, 420, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.35), [("sen", "g", 100, OPO)] + ps("pelo", "i", 90) + [("cos", "g", 100, ADJ)], XE, 570, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("com a relação", "i", 70) + [("mais usada", "g", 76, COR)], XE, 720, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 625, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 710, 80, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 860, 940
    itens = (("s03.b", "no ciclo de raio 1",
              lambda a, y: cf(c, [("cos", ADJ), (" no horizontal, ", TINTA), ("sen", OPO), (" no vertical", TINTA)], x + 44, y, 56, a)),
             ("s03.c", "o teorema de",
              lambda a, y: cf(c, [("Pitágoras:  a² + b² = c²", COR)], x + 44, y, 60, a)),
             ("s03.d", "se um número ao quadrado dá 9",
              lambda a, y: cf(c, [("ele vale 3 ou −3", COR)], x + 44, y, 60, a)))
    for i, (k, l1, fn) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 80)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, fn=fn, y=y: fn(a, y + 162))
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 580, q1), 820, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 860, 1000, "left", 0.12)


# ---------------- de onde vem ----------------
CX, CY, CR = 560, 560, 330
ANG = 40


def b_ciclo(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6 = C["s06.a"], C["s06.b"]
    X = 1400
    base_ciclo(c, t, a4, CX, CY, CR, ANG, a4 + 0.9)
    tri_ciclo(c, t, CX, CY, CR, ANG, td=b4, tf=c4, th=a5, tc=b5, ts=c5, rh="1", rc="cos x", rs="sen x", size=56)

    def quatro_cinco():
        E.frase(c, t, a4, ps("marque", "i", 64) + [("x", "g", 70, COR)] + ps("no 1º quadrante", "i", 64), X, 200, "center", 0.1)
        E.frase(c, t, b4, ps("desça até o", "i", 60) + [("eixo horizontal", "g", 64)], X, 320, "center", 0.1)
        E.frase(c, t, c4, ps("um", "i", 64) + [("triângulo retângulo", "g", 70, COR)], X, 440, "center", 0.1)
        cf_em(c, t, a5, [("hipotenusa = raio = 1", HIP)], X, 640, 64, "center")
        cf_em(c, t, b5, [("deitado: ", TINTA), ("cos x", ADJ)], X, 780, 70, "center")
        cf_em(c, t, c5, [("em pé: ", TINTA), ("sen x", OPO)], X, 920, 70, "center")
    E.saida(c, t, C["s06"] - 0.1, quatro_cinco)
    if t < C["s06"] - 0.1:
        return
    E.frase(c, t, C["s06"] + 0.2, [("Pitágoras", "g", 70, COR)], X, 200, "center", 0.1)
    E.foco(c, t, C["s06"] + 0.8, 0.5, lambda a: cf(c, [("cateto² + cateto² = hip²", TINTA2)], X, 310, 56, a, "center"))
    cf_em(c, t, a6, [("(sen x)²", OPO), (" + ", TINTA), ("(cos x)²", ADJ), (" = 1²", HIP)], X, 480, 74, "center")
    E.foco(c, t, a6 + 1.6, 0.5, lambda a: cf(c, [("1² = 1", TINTA2)], X, 590, 56, a, "center"))
    E.foco(c, t, b6, 0.5, lambda a: E.caixa_pontilhada(c, X - 400, 680, 800, 200, a, COR, prog_=ep(t, b6, 0.6)))
    E.foco(c, t, b6 + 0.1, 0.5, lambda a: relacao(c, X, 810, 92, a))
    E.frase(c, t, b6 + 0.5, ps("relação fundamental", "i", 50, COR), X, 950, "center", 0.08)


# ---------------- notação ----------------
def b_notacao(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")

    def sete():
        E.frase(c, t, C["s07"] + 0.2, ps("na prova, ela vem assim:", "i", 64), W / 2, 190, "center", 0.1)
        E.foco(c, t, a7, 0.5, lambda a: relacao(c, W / 2, 400, 140, a))
        cf_em(c, t, b7, [("sen²x", OPO), (" = ", TINTA), ("(sen x)²", OPO)], W / 2, 610, 100, "center")
        E.frase(c, t, b7 + 0.8, ps("calcule o seno e eleve o resultado ao quadrado", "i", 50, TINTA2), W / 2, 710, "center", 0.06)
        cf_em(c, t, c7, [("sen²x  ≠  sen(x²)", ERRADO)], W / 2, 890, 90, "center")
        E.foco(c, t, c7 + 0.4, 0.5, lambda a: E.selo(c, W / 2 + _w("sen²x  ≠  sen(x²)", 90) / 2 + 90, 858, 42, False, a))
        E.frase(c, t, c7 + 1.0, ps("o ângulo não vai ao quadrado", "i", 46, TINTA2), W / 2, 985, "center", 0.06)
    E.saida(c, t, C["s08"] - 0.1, sete)
    if t < C["s08"] - 0.1:
        return
    E.frase(c, t, a8, ps("vale em", "i", 66) + [("qualquer quadrante", "g", 72, COR)], W / 2, 190, "center", 0.1)
    E.frase(c, t, b8, ps("ao quadrado,", "i", 56, TINTA2) + [("o sinal some", "g", 60)], W / 2, 300, "center", 0.1)
    E.foco(c, t, c8 - 0.3, 0.5, lambda a: centro(c, "teste: 30°", 330, 525, 56, "i", COR, a * (1 if t < c8 + 999 else 0)))
    x0 = 600
    cf_em(c, t, c8, [("sen 30°", OPO), (" = f{1}{2}  →  (f{1}{2})^2 = f{1}{4}", TINTA)], x0, 540, 80)
    cf_em(c, t, d8, [("cos 30°", ADJ), (" = f{r{3}}{2}  →  (f{r{3}}{2})^2 = f{3}{4}", TINTA)], x0, 740, 80)
    cf_em(c, t, e8, [("f{1}{4} + f{3}{4} = f{4}{4} = 1", CERTO)], x0, 950, 86)
    E.foco(c, t, e8 + 1.4, 0.5, lambda a: E.selo(c, x0 + _w("f{1}{4} + f{3}{4} = f{4}{4} = 1", 86) + 80, 920, 42, True, a))


# ---------------- exemplo ----------------
EX, EY, ER = 470, 580, 290


def b_exemplo(c, t, C, b):
    a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    X0, XC = 940, 1390
    base_ciclo(c, t, C["s09"], EX, EY, ER, X35, C["s09"] + 0.8)
    # o 1º quadrante aceso quando o quadrante decide
    if t >= c1:
        k = ep(t, c1, 0.5)
        path = skia.Path(); path.moveTo(EX, EY); path.arcTo(skia.Rect.MakeXYWH(EX - ER, EY - ER, 2 * ER, 2 * ER), 0, -90, False); path.close()
        c.drawPath(path, M.paint(E.COR, 0.10 * k))
    # o outro candidato: −4/5, no 2º quadrante, que some quando o quadrante decide
    if t >= a1:
        k = ep(t, a1 + 0.4, 0.5) * (1 - 0.5 * ep(t, c1 + 0.6, 0.5))
        tri_ciclo(c, t, EX, EY, ER, 180 - X35, td=a1 + 0.4, tc=a1 + 0.6, rc="−f{4}{5}", size=54, a=k, cc=TINTA2)
        if t >= c1 + 0.2:
            Xg = EX - ER * 0.4
            E.risco(c, Xg - 60, EY + 150, Xg + 60, EY + 40, t, c1 + 0.2, ERRADO, 8)
    tri_ciclo(c, t, EX, EY, ER, X35, td=a9 + 0.2, tf=a9 + 0.2, ts=a9 + 0.4, rs="f{3}{5}", tc=a9 + 0.6,
              rc=lambda tt: "f{4}{5}" if tt >= d1 else "?", size=54)

    cf_em(c, t, a9, [sen_x(), (" = f{3}{5}", TINTA)], X0, 200, 84)
    E.foco(c, t, a9 + 0.8, 0.5, lambda a: E.pilula(c, "1º quadrante", X0 + 640, 172, 44, "g", a=a, cor=E.SOBRE))

    def nove():
        cf_em(c, t, b9, [("(f{3}{5})^2 = f{3 · 3}{5 · 5}", TINTA)], X0, 470, 84)
        cf_em(c, t, c9, [(" = f{9}{25}", COR)], X0 + _w("(f{3}{5})^2 = f{3 · 3}{5 · 5}", 84), 470, 84)
        E.frase(c, t, c9 + 0.3, ps("o seno ao quadrado", "i", 50, TINTA2), XC, 640, "center", 0.08)
    E.saida(c, t, C["s10"] - 0.1, nove)

    def dez():
        cf_em(c, t, a0, [("cos²x", ADJ), (" = 1 − f{9}{25}", TINTA)], X0, 400, 84)
        E.frase(c, t, b0 - 1.6, ps("o 1 com o mesmo denominador:", "i", 48, TINTA2), X0, 540, "left", 0.06)
        cf_em(c, t, b0, [("1 = f{25}{25}", TINTA)], X0, 650, 80)
        cf_em(c, t, c0, [("25 − 9 = 16", TINTA)], X0 + 520, 650, 80)
        resp(c, t, d0, [("cos²x = f{16}{25}", BR)], XC, 860, 72, 2.3)
    if C["s10"] - 0.1 <= t:
        E.saida(c, t, C["s11"] - 0.1, dez)

    def onze():
        cf_em(c, t, a1, [("cos x = f{4}{5}  ou  −f{4}{5}", TINTA)], XC, 400, 80, "center")
        E.frase(c, t, b1, ps("quem decide:", "i", 60) + [("o quadrante", "g", 66, COR)], XC, 560, "center", 0.1)
        E.frase(c, t, c1, ps("no 1º, à direita:", "i", 56) + [("cos positivo", "g", 60, CERTO)], XC, 680, "center", 0.1)
        resp(c, t, d1, [("cos x = f{4}{5}", BR)], XC, 870, 76, 2.3)
    if C["s11"] - 0.1 <= t:
        E.saida(c, t, C["s12"] - 0.1, onze)
    if t < C["s12"] - 0.1:
        return
    cf_em(c, t, a2, [("tg x = ", TINTA), ("f{sen x}{cos x}", TINTA)], X0, 420, 84)
    if t >= a2:  # numerador e denominador nas cores
        pass
    y = 640
    s = 90
    E.foco(c, t, b2, 0.5, lambda a: cf(c, [("f{3}{5}", OPO), (" ÷ ", TINTA), ("f{4}{5}", ADJ)], X0, y, s, a))
    d1x = X0 + _w("f{3}{5}", s) / 2
    d2x = X0 + _w("f{3}{5} ÷ ", s) + _w("f{4}{5}", s) / 2
    if t >= b2 + 1.6:
        for xx in (d1x, d2x):
            E.risco(c, xx - 30, y + 72, xx + 30, y + 10, t, b2 + 1.6, ERRADO, 8)
    x1 = X0 + _w("f{3}{5} ÷ f{4}{5}", s)
    E.foco(c, t, c2, 0.5, lambda a: cf(c, [(" = ", TINTA), ("f{3}{4}", COR)], x1, y, s, a))
    E.foco(c, t, c2 + 0.3, 0.5, lambda a: E.selo(c, x1 + _w(" = f{3}{4}", s) + 70, y - 30, 38, True, a))
    E.frase(c, t, d2, ps("não existe se", "i", 54, TINTA2) + [("cos x = 0", "g", 58, ERRADO)] + ps("(90°)", "i", 54, TINTA2), XC, 900, "center", 0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a3, b3, c3, d3, e3, f3 = (C[f"s13.{k}"] for k in "abcdef")
    x = 300

    def tudo():
        E.frase(c, t, a3, ps("o erro:", "i", 66) + [("esquecer os quadrados", "g", 70, ERRADO)], x, 190, "left", 0.1)
        cf_em(c, t, b3, [("cos x = 1 − sen x", ERRADO)], x, 360, 90)
        cf_em(c, t, c3, [("1 − f{3}{5} = f{2}{5}", ERRADO)], x, 540, 86)
        E.frase(c, t, d3, [("teste:", "i", 60, TINTA2)], x, 740)
        cf_em(c, t, d3 + 0.3, [("(f{2}{5})^2 = f{4}{25}", TINTA)], x + 220, 740, 86)
        cf_em(c, t, e3, [("f{9}{25} + f{4}{25} = f{13}{25}", TINTA)], x, 940, 86)
        xe = x + _w("f{9}{25} + f{4}{25} = f{13}{25}", 86)
        E.foco(c, t, e3 + 2.0, 0.5, lambda a: cf(c, [("  ≠ 1", ERRADO)], xe, 940, 86, a))
        E.foco(c, t, e3 + 2.4, 0.5, lambda a: E.selo(c, xe + _w("  ≠ 1", 86) + 80, 910, 46, False, a))
        E.foco(c, t, c3 + 0.6, 0.5, lambda a: E.selo(c, x + _w("1 − f{3}{5} = f{2}{5}", 86) + 80, 510, 46, False, a))
    E.saida(c, t, f3 - 0.3, tudo)
    if t < f3 - 0.3:
        return
    E.frase(c, t, f3, ps("a relação é entre", "i", 76) + [("os quadrados", "g", 84, CERTO)], W / 2, 400, "center", 0.1)
    E.foco(c, t, f3 + 0.6, 0.5, lambda a: relacao(c, W / 2, 640, 130, a))
    E.foco(c, t, f3 + 1.0, 0.5, lambda a: E.selo(c, W / 2 + relacao(None, 0, 0, 130, 0) / 2 + 90, 600, 46, True, a))


# ---------------- atalho (palco escuro) ----------------
K = 110
TA, TR, TT = (230, 860), (230 + 4 * K, 860), (230 + 4 * K, 860 - 3 * K)


def b_atalho(c, t, C, b):
    palco(c, t)
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    X = 1300
    tri(c, t, a4, TA, TR, TT, med={"opo": "3", "hip": "5", "adj": lambda tt: "4" if tt >= c4 else "?"},
        tm={"opo": b4 + 0.3, "hip": b4 + 1.0, "adj": a4 + 1.0},
        cores={"opo": (b4 + 0.3, OPO), "hip": (b4 + 1.0, CLARO), "adj": (c4, ADJ_ESC)}, escuro=True, size=80, alfa=a4 + 0.8)

    def quatorze():
        E.frase(c, t, C["s14"] + 0.1, ps("o atalho:", "i", 62, CLARO) + [("desenhe o triângulo", "g", 66, BR)], X, 180, "center", 0.1)
        cf_em(c, t, b4, [("sen x", OPO), (" = f{3}{5}", BR)], X, 360, 90, "center")
        E.frase(c, t, b4 + 1.0, [("oposto 3,", "g", 54, OPO), ("hipotenusa 5", "g", 54, CLARO)], X, 480, "center", 0.1)
        E.frase(c, t, c4 - 1.6, ps("o trio", "i", 60, CLARO) + [("3, 4 e 5", "g", 72, BR)], X, 610, "center", 0.1)
        cf_em(c, t, d4, [("cos x", ADJ_ESC), (" = f{4}{5}", BR)], X - 250, 800, 90, "center")
        cf_em(c, t, e4, [("tg x", BR), (" = f{3}{4}", BR)], X + 250, 800, 90, "center")
        E.frase(c, t, e4 + 1.2, ps("sem conta de fração", "i", 56, CLARO), X, 970, "center", 0.08)
    E.saida(c, t, C["s15"] - 0.1, quatorze)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, a5, ps("a relação fundamental é o próprio", "i", 52, CLARO), X, 190, "center", 0.08)
    E.frase(c, t, a5 + 1.2, [("Pitágoras", "g", 76, BR)], X, 290, "center", 0.1)
    E.foco(c, t, a5 + 1.8, 0.5, lambda a: cf(c, [("3²", OPO), (" + ", BR), ("4²", ADJ_ESC), (" = ", BR), ("5²", CLARO)], X, 400, 72, a, "center"))
    E.frase(c, t, b5, ps("o triângulo dá", "i", 56, CLARO) + [("o tamanho,", "g", 62, BR)] + ps("nunca o sinal", "i", 56, CLARO), X, 560, "center", 0.1)
    E.frase(c, t, c5, ps("fora do 1º quadrante:", "i", 54, CLARO) + [("sinal pelo quadrante", "g", 58, BR)], X, 700, "center", 0.1)
    E.frase(c, t, d5, ps("trio desconhecido?", "i", 54, CLARO) + [("Pitágoras no papel", "g", 58, AMBAR)], X, 870, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    cf_em(c, t, a6, [cos_x(), (" = f{8}{17}", TINTA)], XE, 420, 110)
    E.frase(c, t, b6, ps("no", "i", 70) + [("4º quadrante", "g", 78, COR)], XE, 600, "left", 0.1)
    E.frase(c, t, c6, ps("calcule", "i", 70) + [("sen x", "g", 78, OPO)] + ps("e", "i", 70) + [("tg x", "g", 78)], XE, 790, "left", 0.1)
    E.relogio(c, t, C["s17.a"], 1520, 440, 170)


# ---------------- resposta ----------------
K2 = 34
RA, RR_, RT = (220, 950), (220 + 8 * K2, 950), (220 + 8 * K2, 950 - 15 * K2)
QX, QY, QR = 520, 520, 300


def b_resposta(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    a9, b9, c9, d9 = (C[f"s19.{k}"] for k in "abcd")
    X = 1100

    def dezoito():
        E.frase(c, t, C["s18"] + 0.1, ps("pelo triângulo", "i", 64, COR), 330, 200, "center", 0.1)
        tri(c, t, C["s18"] + 0.3, RA, RR_, RT, med={"adj": "8", "hip": "17", "opo": lambda tt: "15" if tt >= e8 else "?"},
            tm={"adj": a8, "hip": a8 + 0.5, "opo": a8 + 1.0},
            cores={"adj": (a8, ADJ), "hip": (a8 + 0.5, HIP), "opo": (e8, OPO)}, size=64, alfa=C["s18"] + 1.0)
        cf_em(c, t, b8, [("17² = 289", HIP)], X, 280, 90)
        cf_em(c, t, c8, [("8² = 64", ADJ)], X, 460, 90)
        cf_em(c, t, d8, [("289 − 64 = 225", TINTA)], X, 640, 90)
        resp(c, t, e8, [("r{225} = 15", BR)], X + 300, 850, 84, 2.0, OPO)
    E.saida(c, t, C["s19"] - 0.1, dezoito)
    if t < C["s19"] - 0.1:
        return
    base_ciclo(c, t, C["s19"], QX, QY, QR, X4Q, C["s19"] + 0.8)
    if t >= a9:  # o 4º quadrante aceso
        k = ep(t, a9, 0.5)
        path = skia.Path(); path.moveTo(QX, QY); path.arcTo(skia.Rect.MakeXYWH(QX - QR, QY - QR, 2 * QR, 2 * QR), 0, 90, False); path.close()
        c.drawPath(path, M.paint(E.COR, 0.10 * k))
    tri_ciclo(c, t, QX, QY, QR, X4Q, td=C["s19"] + 1.2, tf=C["s19"] + 1.2, tc=C["s19"] + 1.4, rc="f{8}{17}", ts=a9, rs="−f{15}{17}", size=50)
    E.frase(c, t, a9, ps("abaixo do eixo:", "i", 60) + [("sen negativo", "g", 66, ERRADO)], X + 300, 220, "center", 0.1)
    resp(c, t, b9, [("sen x = −f{15}{17}", BR)], X + 300, 420, 76, 2.3)
    cf_em(c, t, c9, [("tg x = f{−15}{8} = −f{15}{8}", TINTA)], X + 300, 650, 84, "center")
    cf_em(c, t, d9, [("225 + 64 = 289", CERTO)], X + 300, 880, 84, "center")
    E.foco(c, t, d9 + 1.0, 0.5, lambda a: E.selo(c, X + 300 + _w("225 + 64 = 289", 84) / 2 + 80, 850, 40, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", lambda a, y: relacao(c, 320, y, 76, a, "left")),
                 ("s20.b", lambda a, y: E.frase(c, t, C["s20.b"] + 0.1, ps("a conta dá", "i", 68) + [("o tamanho", "g", 72, COR)], 320, y)),
                 ("s20.c", lambda a, y: E.frase(c, t, C["s20.c"] + 0.1, ps("o quadrante dá", "i", 68) + [("o sinal", "g", 72, COR)], 320, y)))
        for i, (k, fn) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            if i == 0:
                E.foco(c, t, C[k] + 0.1, 0.5, lambda a, fn=fn, y=y: fn(a, y))
            else:
                fn(1, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula, seno e cosseno viram", "i", 66), XE, 200, passo=0.1)
    E.frase(c, t, a1, [("desenho", "g", 84, COR)], XE, 310, passo=0.1)
    E.frase(c, t, b1, ps("a", "i", 60) + [("onda", "g", 66, COR)] + ps("de cada um", "i", 60), XE, 440, passo=0.1)
    if t >= b1:  # uma onda pequena que corre
        p = ease_io(prog(t, b1, 1.4))
        path = skia.Path()
        x0, y0, w, h = 1080, 430, 640, 70
        n = 120
        for i in range(int(n * p) + 1):
            xx = x0 + w * i / n
            yy = y0 - h * math.sin(2 * math.pi * 2 * i / n)
            (path.moveTo if i == 0 else path.lineTo)(xx, yy)
        c.drawPath(path, M.paint(E.COR, 1.0, stroke=8, cap_round=True))
    E.foco(c, t, c1, 0.5, lambda a: E.formula(c, "y = 3 · sen x", XE, 580, 80, "g", COR, a))
    E.frase(c, t, c1 + 0.8, ps("período e imagem", "i", 56, TINTA2), XE + 560, 580, passo=0.08)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ciclo=b_ciclo, notacao=b_notacao, exemplo=b_exemplo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
