"""Visual — Estudativo · MAT-MTZ-007: discutir um sistema (uma, infinitas ou nenhuma solução). Segue a linguagem de MAT-MTZ-006:
eq() em colunas fixas, conta_eq() empilhada, a letra que some em âmbar. A última linha da escada ganha o selo do caso:
verde = uma solução (SPD), índigo = infinitas (SPI), vermelho = nenhuma (SI). planos() desenha os três planos em perspectiva
cavaleira: canto da sala (um ponto), livro aberto (uma reta), chão e teto (nenhum ponto)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-007_discutir_sistema.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("casos", "exemplo", "valork", "planos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
SOME = "#D98A00"
LETRAS = "xyz"


def vale(eq, sol):
    return sum(a * v for a, v in zip(eq[0], sol)) == eq[1]


def menos(e1, e2, k=1):
    return tuple(a - k * b for a, b in zip(e1[0], e2[0])), e1[1] - k * e2[1]


EX = [((1, 1, 1), 3), ((1, 2, 2), 5), ((2, 3, 3), 10)]
A1, A2 = menos(EX[1], EX[0]), menos(EX[2], EX[0], 2)
assert A1 == ((0, 1, 1), 2) and A2 == ((0, 1, 1), 4) and menos(A2, A1) == ((0, 0, 0), 2)
EX8 = [EX[0], EX[1], ((2, 3, 3), 8)]
assert menos(EX8[2], EX[0], 2) == ((0, 1, 1), 2)
assert all(vale(e, (1, 1, 1)) for e in EX8) and all(vale(e, (1, 2, 0)) for e in EX8)
# o k: x + y + z = 6, x + 2y + z = 8, x + y + kz = 9  ->  y = 2 e (k − 1)z = 3
for k in (1, 2, 4):
    sis = [((1, 1, 1), 6), ((1, 2, 1), 8), ((1, 1, k), 9)]
    assert menos(sis[1], sis[0]) == ((0, 1, 0), 2) and menos(sis[2], sis[0]) == ((0, 0, k - 1), 3)
assert 2 * 3 != 7
Q = [((1, 1, 1), 2), ((1, -1, 1), 0), ((2, 0, 2), 2)]
Q1, Q2 = menos(Q[1], Q[0]), menos(Q[2], Q[0], 2)
assert Q1 == ((0, -2, 0), -2) and Q2 == ((0, -2, 0), -2) and menos(Q2, Q1) == ((0, 0, 0), 0)
assert all(vale(e, (1, 1, 0)) for e in Q) and all(vale(e, (0, 1, 1)) for e in Q)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


# ---------------- peças de sistema (como em MAT-MTZ-006) ----------------
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


def eq(c, coefs, rhs, x0, y, s, a=1.0, cores=None, cw=None, zero=False, txt=None, subs=None):
    """subs = {coluna: (sinal, termo)} troca o termo de uma coluna (ex.: kz)"""
    if a <= 0:
        return
    cw = cw or s * 2.2
    cores = cores or {}
    tms = termos(coefs)
    for k, v in (subs or {}).items():
        tms[k] = v
    for k, tm in enumerate(tms):
        cx = x0 + k * cw
        if tm is None:
            if zero:
                E.escreve(c, "0", cx, y, s, "g", cores.get(k, CINZA), a)
            continue
        sg, tx = tm
        cc = cores.get(k, TINTA)
        if sg:
            E.escreve(c, sg, cx - s * 0.75, y, s, "g", cc, a)
        E.escreve(c, tx, cx, y, s, "g", cc, a)
    E.escreve(c, "=", x0 + 3 * cw - s * 0.45, y, s, "g", cores.get("=", TINTA), a)
    E.escreve(c, txt if txt else E._num(rhs), x0 + 3 * cw + s * 0.35, y, s, "g", cores.get("r", TINTA), a)


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


def zero_igual(c, t, t0, n, x, y, s, cor):
    """a linha "0 = n" da escada"""
    E.foco(c, t, t0, 0.5, lambda a: E.formula(c, f"0 = {E._num(n)}", x, y, s, "g", cor, a))


# ---------------- planos ----------------
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


def planos(c, t, caso, cx, cy, k, t0):
    cores = (COR, SOME, CERTO)
    q = [ep(t, t0 + 0.25 * i, 0.5) for i in range(3)]
    if caso == "ponto":
        face(c, [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)], cx, cy, k, cores[0], q[0])
        face(c, [(0, 0, 0), (0, 2, 0), (0, 2, 2), (0, 0, 2)], cx, cy, k, cores[1], q[1])
        face(c, [(0, 0, 0), (2, 0, 0), (2, 0, 2), (0, 0, 2)], cx, cy, k, cores[2], q[2])
        if q[2] > 0.9:
            x, y = proj((0, 0, 0), cx, cy, k)
            c.drawCircle(x, y, 14, M.paint(TINTA))
    elif caso == "reta":
        for i, ang in enumerate((-20, 40, 100)):
            u = math.radians(ang)
            face(c, [(0, 0, 0), (2 * math.cos(u), 2 * math.sin(u), 0), (2 * math.cos(u), 2 * math.sin(u), 2), (0, 0, 2)], cx, cy, k, cores[i], q[i])
        if q[2] > 0.9:
            M.line(c, *proj((0, 0, -0.3), cx, cy, k), *proj((0, 0, 2.3), cx, cy, k), TINTA, 1, 8)
    else:
        face(c, [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)], cx, cy, k, cores[0], q[0])
        face(c, [(0, 0, 1.8), (2, 0, 1.8), (2, 2, 1.8), (0, 2, 1.8)], cx, cy, k, cores[1], q[1])
        face(c, [(1, -0.2, -0.3), (1, 2.2, -0.3), (1, 2.2, 2.1), (1, -0.2, 2.1)], cx, cy, k, cores[2], q[2])


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        sistema3(c, t, [C["s01"] + 0.5] * 3, EX, 380, 300, 80)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: E.pilula(c, "uma resposta só?", 1450, 300, 56, estilo="g", fundo=TINTA2, a=a))
        zero_igual(c, t, C["s01.b"], 2, 1250, 640, 170, ERRADO)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.escreve(c, "nenhuma solução", 1100, 860, 90, "g", ERRADO, a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        for i, (w, cor) in enumerate((("uma,", CERTO), ("infinitas", COR), ("ou nenhuma", ERRADO))):
            E.frase(c, t, C["s02.a"] + 1.0 + 0.5 * i, [(w, "g", 110, cor)], XE, 490 + i * 140)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 84), XE, 300)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE, 600, 320, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 210, 580, 120, "i", TINTA, a))
    x, w = 900, 880
    for i, (k, l1, l2) in enumerate((("s03.b", "escalonar =", "uma letra por vez"), ("s03.c", "plano =", "folha sem bordas"))):
        y = 280 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 64)], x + 44, y + 95)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 64, COR)], x + 44, y + 180)


# ---------------- os três casos ----------------
def b_casos(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("a", "i", 84), ("última", "g", 78, COR), ("linha", "i", 84), ("da", "i", 84), ("escada", "i", 84)], XE, 190)
    casos = ((C["s04.b"], C["s04.c"], "3z = 6", "uma solução", "possível e determinado", CERTO),
             (C["s05.a"], C["s05.c"], "0 = 0", "infinitas", "possível e indeterminado", COR),
             (C["s06.a"], C["s06.c"], "0 = 2", "nenhuma", "impossível", ERRADO))
    for i, (t1, t2, f, l1, l2, cor) in enumerate(casos):
        y = 380 + i * 230
        E.foco(c, t, t1, 0.5, lambda a, f=f, y=y, cor=cor: E.formula(c, f, XE, y, 120, "g", cor, a))
        E.foco(c, t, t1 + 0.6, 0.5, lambda a, l1=l1, y=y, cor=cor: E.escreve(c, l1, 760, y - 30, 70, "g", cor, a))
        E.foco(c, t, t2, 0.5, lambda a, l2=l2, y=y: E.escreve(c, l2, 760, y + 50, 56, "i", TINTA2, a))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "sempre verdade", 1600, 590, 46, estilo="b", fundo=TINTA2, a=a))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.pilula(c, "mentira", 1600, 820, 46, estilo="b", fundo=ERRADO, a=a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    s = 64
    oito = t >= C["s09.a"]
    eqs = EX8 if oito else EX
    sistema3(c, t, [C["s07.a"], C["s07.b"], C["s07.c"]], eqs, 240, 260, s, dy=110,
             cores=[None, None, {"r": COR} if oito else None])
    xo, so = 1060, 76

    def caso_dez():
        eq_em(c, t, C["s08.a"], A1[0], A1[1], xo, 280, so)
        E.foco(c, t, C["s08.a"], 0.4, lambda a: E.escreve(c, "2ª − 1ª", xo - 220, 280, 44, "b", COR, a))
        eq_em(c, t, C["s08.b"], A2[0], A2[1], xo, 400, so)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: E.escreve(c, "3ª − 2·1ª", xo - 260, 400, 44, "b", COR, a))
        q = ep(t, C["s08.c"], 0.5)
        if q > 0:
            M.line(c, xo - 60, 440, xo - 60 + 700 * q, 440, TINTA, 1, 5)
        zero_igual(c, t, C["s08.c"], 2, xo + 300, 560, 110, ERRADO)
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.escreve(c, "impossível", xo, 720, 90, "g", ERRADO, a))
    E.saida(c, t, C["s09"] - 0.1, caso_dez)
    if t >= C["s09"]:
        E.foco(c, t, C["s09.a"], 0.5, lambda a: E.escreve(c, "10 → 8", 240, 680, 80, "g", COR, a))
        eq_em(c, t, C["s09.b"] - 0.3, A1[0], A1[1], xo, 280, so)
        eq_em(c, t, C["s09.b"], A1[0], A1[1], xo, 400, so)
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.escreve(c, "3ª − 2·1ª", xo - 260, 400, 44, "b", COR, a))
        q = ep(t, C["s09.c"], 0.5)
        if q > 0:
            M.line(c, xo - 60, 440, xo - 60 + 700 * q, 440, TINTA, 1, 5)
        zero_igual(c, t, C["s09.c"], 0, xo + 300, 560, 110, COR)
        E.foco(c, t, C["s09.c"] + 0.4, 0.5, lambda a: E.escreve(c, "infinitas", xo, 720, 90, "g", COR, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "(1, 1, 1)", 240, 900, 90, "g", CERTO, a))
        E.foco(c, t, C["s09.e"], 0.5, lambda a: E.formula(c, "(1, 2, 0)", 760, 900, 90, "g", CERTO, a))


# ---------------- o valor de k ----------------
def b_valork(c, t, C, b):
    E.frase(c, t, C["s10.a"], [("qual", "i", 84), ("k", "g", 80, SOME), ("deixa", "i", 84), ("sem", "i", 84), ("solução?", "g", 78, ERRADO)], XE, 180)
    s = 70
    eqs = [((1, 1, 1), 6), ((1, 2, 1), 8), ((1, 1, 1), 9)]
    sistema3(c, t, [C["s10.b"]] * 3, eqs, 240, 330, s, dy=115, cores=[None, None, {2: SOME}], subs=[None, None, {2: ("+", "kz")}])
    xo = 1080
    E.foco(c, t, C["s10.c"], 0.5, lambda a: (E.escreve(c, "2ª − 1ª:", xo, 350, 56, "b", COR, a), E.formula(c, "y = 2", xo + 280, 350, 70, "g", TINTA, a)))
    E.foco(c, t, C["s10.d"], 0.5, lambda a: (E.escreve(c, "3ª − 1ª:", xo, 470, 56, "b", COR, a), E.formula(c, "kz − z = 3", xo + 280, 470, 70, "g", TINTA, a)))
    E.foco(c, t, C["s11.a"], 0.5, lambda a: E.formula(c, "(k − 1) · z = 3", xo, 620, 90, "g", SOME, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "k = 1:  0 · z = 3", XE, 820, 90, "g", TINTA, a))
    zero_igual(c, t, C["s11.c"], 3, XE, 960, 100, ERRADO)
    E.foco(c, t, C["s11.c"] + 0.3, 0.5, lambda a: E.escreve(c, "impossível", XE + 400, 960, 80, "g", ERRADO, a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.escreve(c, "k ≠ 1: uma solução", 1100, 900, 70, "g", CERTO, a))


# ---------------- planos ----------------
def b_planos(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("cada", "i", 84), ("equação", "i", 84), ("=", "g", 78), ("um", "i", 84), ("plano", "g", 78, COR)], XE, 180)
    E.frase(c, t, C["s12.b"], ps("a solução está nos três ao mesmo tempo", "i", 60, TINTA2), XE, 280)
    k = 120
    planos(c, t, "ponto", 300, 720, k, C["s13.a"])
    planos(c, t, "reta", 960, 720, k, C["s13.b"])
    planos(c, t, "nada", 1500, 720, k, C["s13.c"])
    for x, tt, l1, l2, cor in ((300, C["s13.a"], "um ponto", "uma solução", CERTO), (960, C["s13.b"], "uma reta", "infinitas", COR),
                               (1500, C["s13.c"], "nenhum ponto", "nenhuma", ERRADO)):
        E.foco(c, t, tt + 0.8, 0.5, lambda a, x=x, l1=l1, l2=l2, cor=cor: (E.escreve(c, l1, x - 60, 900, 60, "g", cor, a),
                                                                           E.escreve(c, l2, x - 60, 970, 48, "i", TINTA2, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 104, ERRADO), ("com", "i", 96), ("isto", "i", 96)], XE, 200)
    zero_igual(c, t, C["s14.a"], 0, XE, 520, 200, TINTA)
    E.foco(c, t, C["s14.a"] + 0.5, 0.5, lambda a: E.escreve(c, "→ resposta 0?", XE + 620, 500, 100, "g", ERRADO, a))
    if t >= C["s14.b"]:
        E.risco(c, XE + 600, 530, XE + 1350, 430, t, C["s14.b"], largura=14)
        E.frase(c, t, C["s14.b"], ps("não dá valor para letra nenhuma", "i", 70, TINTA), XE, 740)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.escreve(c, "infinitas soluções", XE, 900, 110, "g", COR, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)
    E.frase(c, t, C["s15.a"], [("as", "i", 76, BR), ("letras", "g", 70, CLARO), ("dobraram?", "i", 76, BR)], XE, 320)
    s, x0 = 84, 330
    E.foco(c, t, C["s15.b"], 0.5, lambda a: eq(c, (1, 1, 1), 3, x0, 500, s, a, cores={i: BR for i in (0, 1, 2, "=", "r")}))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: eq(c, (2, 2, 2), 7, x0, 640, s, a, cores={0: "#FFB833", 1: "#FFB833", 2: "#FFB833", "=": BR, "r": BR}))
    E.foco(c, t, C["s15.c"] + 0.6, 0.5, lambda a: E.escreve(c, "× 2", 120, 640, 64, "b", "#FFB833", a))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.escreve(c, "3 × 2 = 6 ≠ 7", 1150, 640, 84, "g", E.ERRADO, a))
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.escreve(c, "impossível", 1150, 520, 90, "g", BR, a))
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.escreve(c, "letras dobram → número dobra junto", XE, 850, 60, "b", CLARO, a))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.escreve(c, "dobrou também? escalone", XE, 960, 60, "b", "#FFB833", a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.escreve(c, "uma, infinitas ou nenhuma?", XE, 320, 64, "g", COR, a))
    sistema3(c, t, [C["s17.b"], C["s17.c"], C["s17.d"]], Q, 380, 500, 90)
    E.relogio(c, t, C["s18.a"], cx=1560, cy=560, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s = 60
    sistema3(c, t, [C["s19"]] * 3, Q, 220, 240, s, dy=100)
    xo, so = 1100, 76
    E.foco(c, t, C["s19.a"], 0.4, lambda a: E.escreve(c, "2ª − 1ª", xo - 280, 300, 44, "b", COR, a))
    eq_em(c, t, C["s19.a"], Q1[0], Q1[1], xo, 300, so)
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.escreve(c, "3ª − 2·1ª", xo - 280, 420, 44, "b", COR, a))
    eq_em(c, t, C["s19.b"], Q2[0], Q2[1], xo, 420, so)
    q = ep(t, C["s19.c"], 0.5)
    if q > 0:
        M.line(c, xo - 60, 460, xo - 60 + 700 * q, 460, TINTA, 1, 5)
    zero_igual(c, t, C["s19.d"], 0, xo + 300, 580, 110, COR)
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.escreve(c, "possível e indeterminado", XE, 700, 70, "g", COR, a))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "(1, 1, 0)", XE, 840, 80, "g", CERTO, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "(0, 1, 1)", XE + 420, 840, 80, "g", CERTO, a))
    planos(c, t, "reta", 1450, 920, 100, C["s20.d"])


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("a", "i", 92, COR), ("última", "i", 92, COR), ("linha", "i", 92, COR)], W / 2, 190, "center")
        for i, (k, f, s, cor) in enumerate((("s21.a", "3z = 6", "uma solução", CERTO), ("s21.b", "0 = 0", "infinitas", COR), ("s21.c", "0 = 2", "nenhuma", ERRADO))):
            y = 400 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, f=f, y=y, cor=cor: E.formula(c, f, 380, y, 100, "g", cor, a))
            E.frase(c, t, C[k] + 0.2, [(s, "g", 90, cor)], 900, y)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("sistema", "i", 110), ("como", "i", 110), ("matriz", "g", 120, COR)], XE, 470)
    E.frase(c, t, C["s22.b"], [("regra", "i", 110), ("de", "i", 110), ("Cramer", "g", 120, COR)], XE, 630)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(1000, 845, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, casos=b_casos, exemplo=b_exemplo, valork=b_valork, planos=b_planos,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
