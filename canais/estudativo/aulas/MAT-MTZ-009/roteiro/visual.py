"""Visual — Estudativo · MAT-MTZ-009: prática de sistemas lineares (5 questões). Reúne as peças de MAT-MTZ-006 a 008:
eq() em colunas fixas e a letra que some em âmbar; "0 = n" com a cor do caso (índigo infinitas, vermelho nenhuma);
determinantes com barras e a coluna B em âmbar; planos() da aula 007; resultado em verde."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-009_praticando_sistemas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
SOME = "#D98A00"
LETRAS = "xyz"


def vale(eq, sol):
    return sum(a * v for a, v in zip(eq[0], sol)) == eq[1]


def menos(e1, e2, k=1):
    return tuple(a - k * b for a, b in zip(e1[0], e2[0])), e1[1] - k * e2[1]


def det(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


# questão 1
Q1 = [((1, 1, 1), 9), ((1, -1, 1), 3), ((2, 1, -1), 3)]
assert all(vale(e, (2, 3, 4)) for e in Q1) and menos(Q1[0], Q1[1]) == ((0, 2, 0), 6)
assert 9 - 3 == 6 and 3 - 3 == 0 and 3 * 2 == 6 and 6 - 2 == 4
# questão 2: suco x, sanduíche y, doce z
Q2 = [((1, 1, 1), 19), ((2, 1, 0), 18), ((0, 1, 3), 25)]
assert all(vale(e, (4, 10, 5)) for e in Q2)
R2 = menos(Q2[1], Q2[0], 2)
assert R2 == ((0, -1, -2), -20) and menos(Q2[2], ((0, 1, 2), 20)) == ((0, 0, 1), 5)
# questão 3: (k − 2)z = 2
for k in (2, 3, 4):
    s3 = [((1, 1, 1), 1), ((1, 2, 1), 2), ((2, 3, k), 5)]
    assert menos(s3[1], s3[0]) == ((0, 1, 0), 1) and menos(s3[2], s3[0], 2) == ((0, 1, k - 2), 3)
# questão 4
QA, QB = [[2, 3], [1, -2]], [13, -4]
assert det(QA) == -7 and det([[2, 13], [1, -4]]) == -21 and Fr(-21, -7) == 3 and 2 * 2 + 3 * 3 == 13 and 2 - 2 * 3 == -4


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def selo_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, f"questão {n}", XE + 150, 130, 52, estilo="g", a=a))


# ---------------- peças de sistema (como em MAT-MTZ-006/007) ----------------
def termos(coefs):
    out, primeiro = [], True
    for a, l in zip(coefs, LETRAS):
        if a == 0:
            out.append(None)
            continue
        k = "" if abs(a) == 1 else str(abs(a))
        sg = ("−" if a < 0 else "") if primeiro else ("−" if a < 0 else "+")
        out.append((sg, k + l))
        primeiro = False
    return out


def eq(c, coefs, rhs, x0, y, s, a=1.0, cores=None, cw=None, subs=None):
    if a <= 0:
        return
    cw = cw or s * 2.2
    cores = cores or {}
    tms = termos(coefs)
    for k, v in (subs or {}).items():
        tms[k] = v
    for k, tm in enumerate(tms):
        if tm is None:
            continue
        cx = x0 + k * cw
        sg, tx = tm
        cc = cores.get(k, TINTA)
        if sg:
            E.escreve(c, sg, cx - s * 0.75, y, s, "g", cc, a)
        E.escreve(c, tx, cx, y, s, "g", cc, a)
    E.escreve(c, "=", x0 + 3 * cw - s * 0.45, y, s, "g", cores.get("=", TINTA), a)
    E.escreve(c, E._num(rhs), x0 + 3 * cw + s * 0.35, y, s, "g", cores.get("r", TINTA), a)


def eq_em(c, t, t0, coefs, rhs, x0, y, s, **kw):
    E.foco(c, t, t0, 0.5, lambda a: eq(c, coefs, rhs, x0, y, s, a, **kw))


def chave(c, t, t0, x, y0, y1, s):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    meio, k = (y0 + y1) / 2, s * 0.32
    p = skia.Path()
    p.moveTo(x, y0); p.cubicTo(x - k, y0, x - k * 0.2, meio - k, x - k, meio)
    p.cubicTo(x - k * 0.2, meio + k, x - k, y1, x, y1)
    c.drawPath(p, M.paint(TINTA, q, stroke=max(5, s * 0.07), cap_round=True))


def sistema3(c, t, ts, eqs, x0, y0, s, dy=None, cores=None, subs=None):
    dy = dy or s * 1.5
    chave(c, t, ts[0], x0 - s * 0.9, y0 - s * 0.95, y0 + 2 * dy + s * 0.35, s)
    for i, (co, r) in enumerate(eqs):
        eq_em(c, t, ts[i], co, r, x0, y0 + i * dy, s, cores=(cores[i] if cores else None), subs=(subs[i] if subs else None))


def linha_em(c, t, t0, txt, x, y, size=70, cor=TINTA, rot=None):
    if rot:
        E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, rot, x - 300, y, 44, "b", COR, a))
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, txt, x, y, size, "g", cor, a))


# ---------------- planos (como em MAT-MTZ-007) ----------------
def proj(P, cx, cy, k):
    x, y, z = P
    return cx + (x + 0.55 * y * math.cos(math.radians(32))) * k, cy - (z + 0.55 * y * math.sin(math.radians(32))) * k


def face(c, pts, cx, cy, k, cor, a):
    if a <= 0:
        return
    pp = [proj(P, cx, cy, k) for P in pts]
    p = skia.Path(); p.addPoly(pp, True)
    c.drawPath(p, M.paint(cor, 0.22 * a))
    c.drawPath(p, M.paint(cor, 0.9 * a, stroke=4))


def livro(c, t, t0, cx, cy, k):
    cores = (COR, SOME, CERTO)
    for i, ang in enumerate((-20, 40, 100)):
        q = ep(t, t0 + 0.25 * i, 0.5)
        u = math.radians(ang)
        face(c, [(0, 0, 0), (2 * math.cos(u), 2 * math.sin(u), 0), (2 * math.cos(u), 2 * math.sin(u), 2), (0, 0, 2)], cx, cy, k, cores[i], q)
    if ep(t, t0 + 0.5, 0.5) > 0.9:
        M.line(c, *proj((0, 0, -0.3), cx, cy, k), *proj((0, 0, 2.3), cx, cy, k), TINTA, 1, 8)


# ---------------- abertura ----------------
def b_gancho(c, t, C, b):
    E.foco(c, t, C["s01.a"], 0.5, lambda a: E.escreve(c, "5", XE, 620, 420, "g", COR, a))
    E.frase(c, t, C["s01.a"] + 0.3, [("questões", "g", 120)], XE + 300, 470)
    E.frase(c, t, C["s01.a"] + 0.8, ps("de sistemas lineares", "i", 76, TINTA2), XE + 300, 580)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "pause e resolva antes", 1300, 850, 64, estilo="g", a=a))
    E.relogio(c, t, C["s01.b"] + 0.4, cx=1600, cy=330, r=150)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as ferramentas", "i", 84), XE, 190)
    itens = (("s02.a", "escalonar: uma letra por vez"), ("s02.b", "última linha: uma, infinitas, nenhuma"),
             ("s02.c", "Cramer: x = Dx / D"), ("s02.d", "conferir no fim"))
    for i, (k, txt) in enumerate(itens):
        y = 360 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 50, y - 25, 48, a=a), E.centro(c, str(i + 1), XE + 50, y - 3, 56, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, txt=txt, y=y: E.formula(c, txt, XE + 140, y, 72, "g", TINTA, a))


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    selo_q(c, t, C["s03.a"], 1)
    sistema3(c, t, [C["s03.b"], C["s03.c"], C["s03.d"]], Q1, 380, 400, 90)
    E.relogio(c, t, C["s04.a"], cx=1560, cy=520, r=180)


def b_resposta1(c, t, C, b):
    s = 70
    cores = [{1: SOME}, {1: SOME}, None] if t >= C["s05.a"] else None
    sistema3(c, t, [C["s05"]] * 3, Q1, 240, 260, s, dy=115, cores=cores)
    x = 1100
    linha_em(c, t, C["s05.b"], "1ª − 2ª:  2y = 6", x - 120, 300, 70, TINTA)
    E.foco(c, t, C["s05.b"] + 0.3, 0.5, lambda a: E.escreve(c, "x e z somem juntos", x - 120, 380, 50, "i", SOME, a))
    linha_em(c, t, C["s05.c"], "y = 3", x - 120, 490, 100, CERTO)
    linha_em(c, t, C["s06.a"], "x + z = 6", 240, 680, 70)
    linha_em(c, t, C["s06.b"], "2x − z = 0", 240, 790, 70)
    linha_em(c, t, C["s06.c"], "3x = 6  →  x = 2", 760, 735, 70, CERTO)
    linha_em(c, t, C["s06.d"], "z = 6 − 2 = 4", 760, 850, 70, CERTO)
    E.foco(c, t, C["s06.e"], 0.5, lambda a: (E.selo(c, 1360, 960, 50, True, a), E.formula(c, "(2, 3, 4)", 1440, 990, 100, "g", CERTO, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s07"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)
    E.frase(c, t, C["s07.a"], [("duas", "i", 84, BR), ("equações", "i", 84, BR), ("quase", "g", 78, CLARO), ("iguais", "g", 78, CLARO)], XE, 330)
    s, x0 = 84, 400
    cB = {0: BR, 2: BR, "r": BR, "=": BR, 1: "#FFB833"}
    E.foco(c, t, C["s07.b"], 0.5, lambda a: eq(c, (1, 1, 1), 9, x0, 520, s, a, cores=cB))
    E.foco(c, t, C["s07.b"] + 0.3, 0.5, lambda a: eq(c, (1, -1, 1), 3, x0, 640, s, a, cores=cB))
    E.foco(c, t, C["s07.b"] + 0.3, 0.5, lambda a: E.escreve(c, "−", x0 - 160, 640, s, "g", CLARO, a))
    q = ep(t, C["s07.b"] + 0.6, 0.5)
    if q > 0:
        M.line(c, x0 - 170, 680, x0 - 170 + 800 * q, 680, BR, 1, 5)
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "2y = 6", x0 + s * 2.2 - s * 0.6, 790, s, "g", "#FFB833", a))
    E.foco(c, t, C["s08.a"], 0.5, lambda a: E.escreve(c, "o que é igual se cancela", 1150, 560, 60, "b", CLARO, a))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.escreve(c, "nada parecido? tire o x", 1150, 680, 60, "b", "#FFB833", a))


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    selo_q(c, t, C["s09.a"], 2)
    itens = ((C["s09.b"], "1 suco + 1 sanduíche + 1 doce", "R$ 19"), (C["s09.c"], "2 sucos + 1 sanduíche", "R$ 18"),
             (C["s09.d"], "1 sanduíche + 3 doces", "R$ 25"))
    for i, (tt, l, v) in enumerate(itens):
        y = 340 + i * 150
        E.foco(c, t, tt, 0.5, lambda a, l=l, v=v, y=y: (E.escreve(c, l, XE, y, 66, "b", TINTA, a), E.escreve(c, v, XE + 1080, y, 70, "g", COR, a)))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: E.escreve(c, "quanto custa cada um?", XE, 860, 90, "g", COR, a))
    E.relogio(c, t, C["s10.a"], cx=1650, cy=820, r=140)


def b_resposta2(c, t, C, b):
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.escreve(c, "suco = x   sanduíche = y   doce = z", XE, 150, 56, "b", TINTA2, a))
    s = 64
    sistema3(c, t, [C["s11.b"], C["s11.c"], C["s11.d"]], Q2, 260, 300, s, dy=105)

    def contas():
        linha_em(c, t, C["s12.a"], "−y − 2z = −20", 1180, 300, 66, rot="2ª − 2·1ª")
        linha_em(c, t, C["s12.b"], "y + 2z = 20", 1180, 410, 66, rot="× (−1)")
        linha_em(c, t, C["s12.c"], "z = 5", 1180, 530, 90, CERTO, rot="3ª − essa")
        linha_em(c, t, C["s12.d"], "y + 10 = 20  →  y = 10", 1080, 680, 64, CERTO)
        linha_em(c, t, C["s12.e"], "x + 10 + 5 = 19  →  x = 4", 1080, 790, 64, CERTO)
    E.saida(c, t, C["s13"] - 0.1, contas)
    if t >= C["s13"]:
        for i, (l, v) in enumerate((("suco", "R$ 4"), ("sanduíche", "R$ 10"), ("doce", "R$ 5"))):
            E.foco(c, t, C["s13.a"] + 0.4 * i, 0.5, lambda a, l=l, v=v, i=i: (E.escreve(c, l, 1080, 360 + i * 130, 70, "i", TINTA, a),
                                                                            E.escreve(c, v, 1500, 360 + i * 130, 80, "g", CERTO, a)))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "2·4 + 10 = 18 ✓", 1080, 800, 70, "g", CERTO, a))


# ---------------- questão 3 ----------------
def b_questao3(c, t, C, b):
    selo_q(c, t, C["s14.a"], 3)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "qual k deixa sem solução?", XE, 290, 80, "g", ERRADO, a))
    eqs = [((1, 1, 1), 1), ((1, 2, 1), 2), ((2, 3, 1), 5)]
    sistema3(c, t, [C["s14.c"], C["s14.d"], C["s14.e"]], eqs, 380, 500, 90, cores=[None, None, {2: SOME}], subs=[None, None, {2: ("+", "kz")}])
    E.relogio(c, t, C["s15.a"], cx=1560, cy=600, r=180)


def b_resposta3(c, t, C, b):
    s = 64
    eqs = [((1, 1, 1), 1), ((1, 2, 1), 2), ((2, 3, 1), 5)]
    sistema3(c, t, [C["s16"]] * 3, eqs, 260, 260, s, dy=105, cores=[None, None, {2: SOME}], subs=[None, None, {2: ("+", "kz")}])
    linha_em(c, t, C["s16.a"], "y = 1", 1180, 300, 80, CERTO, rot="2ª − 1ª")
    linha_em(c, t, C["s16.b"], "y + (k − 2)·z = 3", 1180, 430, 70, TINTA, rot="3ª − 2·1ª")
    linha_em(c, t, C["s17.a"], "(k − 2)·z = 2", 1180, 560, 80, SOME)
    linha_em(c, t, C["s17.b"], "k = 2:  0 = 2", XE, 780, 100, ERRADO)
    E.foco(c, t, C["s17.b"] + 0.5, 0.5, lambda a: E.escreve(c, "impossível", XE + 760, 780, 80, "g", ERRADO, a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "k = 2", 1500, 960, 70, estilo="g", fundo=CERTO, a=a))


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    selo_q(c, t, C["s18.a"], 4)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "pela regra de Cramer: só o y", XE, 300, 76, "g", COR, a))
    E.sistema(c, t, C["s18.c"], ["2x + 3y = 13", "x − 2y = −4"], 330, 540, 110, tl=[C["s18.c"], C["s18.d"]])
    E.relogio(c, t, C["s19.a"], cx=1560, cy=600, r=180)


def b_resposta4(c, t, C, b):
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "só o y: D e Dy", XE, 190, 80, "g", COR, a))
    s, y = 110, 470
    G1 = E.matriz(c, t, C["s20.b"], QA, 450, y, s, barras=True)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "D", 450, G1.y0 - 30, 72, "g", TINTA, a, "center"))
    E.foco(c, t, C["s20.b"] + 1.2, 0.5, lambda a: E.centro(c, "2·(−2) − 3·1 = −7", 450, 760, 54, "b", TINTA, a))
    G2 = E.matriz(c, t, C["s20.c"], [[2, 13], [1, -4]], 1150, y, s, barras=True, cores={("c", 1): SOME})
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "Dy", 1150, G2.y0 - 30, 72, "g", TINTA, a, "center"))
    E.foco(c, t, C["s20.c"] + 1.8, 0.5, lambda a: E.centro(c, "2·(−4) − 13·1 = −21", 1150, 760, 54, "b", TINTA, a))
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.formula(c, "y = f{−21}{−7} = 3", 620, 960, 100, "g", CERTO, a))


# ---------------- questão 5 ----------------
def b_questao5(c, t, C, b):
    selo_q(c, t, C["s21.a"], 5)
    E.frase(c, t, C["s21.b"], ps("três planos, a mesma reta", "i", 80), XE, 320)
    livro(c, t, C["s21.b"] + 0.3, 1200, 760, 150)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.escreve(c, "quantas soluções?", XE, 520, 90, "g", COR, a))
    E.relogio(c, t, C["s22.a"], cx=500, cy=800, r=130)


def b_resposta5(c, t, C, b):
    E.foco(c, t, C["s23.a"], 0.5, lambda a: E.escreve(c, "infinitas", XE, 330, 150, "g", COR, a))
    livro(c, t, C["s23"], 1250, 780, 160)
    if t >= C["s23.c"]:
        for i in range(6):
            q = ep(t, C["s23.c"] + 0.15 * i, 0.3)
            x, y = proj((0, 0, 0.2 + 0.35 * i), 1250, 780, 160)
            c.drawCircle(x, y, 12 * q, M.paint(ERRADO))
    E.frase(c, t, C["s23.b"], ps("cada ponto da reta está nos três", "i", 60, TINTA2), XE, 470)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.escreve(c, "possível e indeterminado", XE, 700, 70, "g", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s24.a", "uma letra por vez"), ("s24.b", "equações quase iguais"), ("s24.c", "leia a última linha"), ("s24.d", "confira sempre"))
        for i, (k, s) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 430, y - 28, 52, a=a), E.centro(c, str(i + 1), 430, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 88)], 520, y)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    E.frase(c, t, C["s25"], ps("fim da trilha", "i", 84), XE, 300)
    E.frase(c, t, C["s25"] + 0.6, [("Matrizes", "g", 130, COR), ("e", "i", 120), ("Sistemas", "g", 130, COR)], XE, 470)
    E.frase(c, t, C["s25.a"], ps("volte às aulas das questões em que errou", "i", 64, TINTA2), XE, 620)
    E.foco(c, t, C["s25.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s25.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(1000, 845, p), ep(t, C["s25.b"] + 0.2, 0.4))
    E.frase(c, t, C["s25.c"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
