"""Visual — Estudativo · MAT-MTZ-006: sistema 3x3 por escalonamento. Primeira aula de sistemas 3x3 da trilha (sem matriz:
a ficha não traz MAT-MTZ-001 a 005). As próximas aulas de sistema copiam daqui:
- eq(): equação com os termos em colunas fixas (x | y | z | = | número), como no escalonamento feito à mão. A letra que vai
  sumir aparece em âmbar; o que sobra, em tinta; a resposta de cada letra, em verde.
- conta_eq(): duas equações empilhadas, "−" à esquerda, traço embaixo e o resultado, termo a termo.
- escada(): o contorno em degraus atrás do sistema escalonado.
Todo instante vem de C[...] (marcadores do roteiro)."""
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Matrizes e Sistemas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-MTZ-006_sistema_3x3_escalonamento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("sistema", "elimina", "subir", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
SOME = "#D98A00"
LETRAS = "xyz"


def vale(eq, sol):
    return sum(a * v for a, v in zip(eq[0], sol)) == eq[1]


S = [((1, 1, 1), 6), ((1, 2, 1), 8), ((1, 1, 2), 9)]
SOL = (1, 2, 3)
assert all(vale(e, SOL) for e in S)
assert (8 - 6, 9 - 6) == (2, 3) and 6 - 2 - 3 == 1 and 1 + 2 + 2 * 3 == 9
Q = [((1, 1, 1), 6), ((2, 3, 1), 14), ((1, 2, 3), 11)]
QS = (2, 3, 1)
assert all(vale(e, QS) for e in Q)
E2 = tuple(2 * a for a in Q[0][0]), 2 * Q[0][1]
R1 = tuple(a - b for a, b in zip(Q[1][0], E2[0])), Q[1][1] - E2[1]
R2 = tuple(a - b for a, b in zip(Q[2][0], Q[0][0])), Q[2][1] - Q[0][1]
R3 = tuple(a - b for a, b in zip(R2[0], R1[0])), R2[1] - R1[1]
assert E2 == ((2, 2, 2), 12) and R1 == ((0, 1, -1), 2) and R2 == ((0, 1, 2), 5) and R3 == ((0, 0, 3), 3)
ALTS = (("a)", (1, 2, 3)), ("b)", (2, 1, 3)), ("c)", (1, 3, 2)))
assert [all(vale(e, s) for e in S) for _, s in ALTS] == [True, False, False]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def termos(coefs, rhs):
    """[(sinal, termo)] por coluna; coluna vazia = None"""
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


def eq(c, coefs, rhs, x0, y, s, a=1.0, cores=None, cw=None, zero=False):
    """equação em colunas: x0 = borda do 1º termo; cores = {coluna (0..2) ou 'r': cor}; zero=True escreve 0 nas colunas vazias"""
    if a <= 0:
        return
    cw = cw or s * 2.2
    cores = cores or {}
    for k, tm in enumerate(termos(coefs, rhs)):
        cx = x0 + k * cw
        if tm is None:
            if zero:
                E.escreve(c, "0", cx, y, s, "g", cores.get(k, CINZA), a)
            continue
        sg, txt = tm
        cc = cores.get(k, TINTA)
        if sg:
            E.escreve(c, sg, cx - s * 0.75, y, s, "g", cc, a)
        E.escreve(c, txt, cx, y, s, "g", cc, a)
    E.escreve(c, "=", x0 + 3 * cw - s * 0.45, y, s, "g", TINTA, a)
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


def sistema3(c, t, ts, eqs, x0, y0, s, dy=None, cores=None):
    dy = dy or s * 1.5
    chave(c, t, ts[0], x0 - s * 0.9, y0 - s * 0.95, y0 + 2 * dy + s * 0.35, s)
    for i, (co, r) in enumerate(eqs):
        eq_em(c, t, ts[i], co, r, x0, y0 + i * dy, s, cores=(cores[i] if cores else None))


def conta_eq(c, t, t0, de, menos, res, x0, y, s, t_res, sinal_="−", cores_res=None, k_menos=None):
    """de − menos = res, empilhado; t_res = instante do resultado"""
    dy = s * 1.35
    cw = s * 2.2
    eq_em(c, t, t0, de[0], de[1], x0, y, s)
    eq_em(c, t, t0 + 0.3, menos[0], menos[1], x0, y + dy, s)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, sinal_, x0 - s * 1.7, y + dy, s, "g", COR, a))
    q = ep(t, t0 + 0.6, 0.5)
    if q > 0:
        M.line(c, x0 - s * 1.8, y + dy + s * 0.45, x0 - s * 1.8 + (3 * cw + s * 2.6) * q, y + dy + s * 0.45, TINTA, 1, 5)
    E.foco(c, t, t_res, 0.5, lambda a: eq(c, res[0], res[1], x0, y + 2 * dy + s * 0.25, s, a, cores=cores_res, zero=True))


def escada(c, x, y, w, h, n, cor, a):
    """contorno em degraus: n degraus, cada um recuado à direita; (x, y) = canto de cima à esquerda"""
    if a <= 0:
        return
    p = skia.Path()
    dx = w / (n + 2)
    p.moveTo(x, y)
    for i in range(n):
        p.lineTo(x + i * dx, y + (i + 1) * h / n)
        if i < n - 1:
            p.lineTo(x + (i + 1) * dx, y + (i + 1) * h / n)
    p.lineTo(x + w, y + h); p.lineTo(x + w, y); p.close()
    c.drawPath(p, M.paint(cor, 0.1 * a))
    pt = M.paint(cor, a, stroke=5)
    pt.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
    c.drawPath(p, pt)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena():
        s = 92
        cores = None
        if t >= C["s01.c"]:
            cores = [None, {0: SOME}, {0: SOME}]
        sistema3(c, t, [C["s01.a"], C["s01.a"] + 0.4, C["s01.a"] + 0.8], S, 420, 360, s, cores=cores)
        E.frase(c, t, C["s01.b"], ps("não ataque tudo de uma vez", "i", 70, TINTA2), XE, 900)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "uma letra por vez", 1500, 300, 60, estilo="g", a=a))
        if t >= C["s01.d"]:
            q = ep(t, C["s01.d"], 0.6)
            escada(c, 1180, 470, 600, 330, 3, COR, q)
            E.foco(c, t, C["s01.d"] + 0.3, 0.5, lambda a: E.centro(c, "escada", 1480, 900, 80, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1450, 520, 300 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 360)
        E.frase(c, t, C["s02.a"] + 1.0, [("sistema", "g", 130, COR), ("3 × 3", "g", 130)], XE, 530)
        E.frase(c, t, C["s02.a"] + 2.0, ps("três equações, três letras", "i", 76, TINTA2), XE, 670)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1290, 505, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1310, 590, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 84), XE, 300)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE, 600, 320, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 210, 580, 120, "i", TINTA, a))
    x, w = 900, 880
    for i, (k, l1, l2) in enumerate((("s03.b", "a solução vale", "em todas as equações"), ("s03.c", "somar ou subtrair", "equações inteiras"))):
        y = 280 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 64)], x + 44, y + 95)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 64, COR)], x + 44, y + 180)


# ---------------- o sistema ----------------
def b_sistema(c, t, C, b):
    def parte1():
        sistema3(c, t, [C["s04.a"], C["s04.b"], C["s04.c"]], S, 420, 300, 100)
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.formula(c, "(x, y, z) = ?", XE, 900, 110, "g", COR, a))
    E.saida(c, t, C["s05"] - 0.1, parte1)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], [("a", "i", 90), ("escada", "g", 84, COR)], XE, 200)
    s, x0, y0, dy = 92, 420, 400, 150
    escada(c, x0 - 80, y0 - 110, 980, 3 * dy, 3, COR, ep(t, C["s05.a"], 0.6))
    eq_em(c, t, C["s05.b"], (1, 1, 1), 6, x0, y0, s)
    eq_em(c, t, C["s05.c"], (0, 1, 1), 5, x0, y0 + dy, s)
    eq_em(c, t, C["s05.d"], (0, 0, 1), 3, x0, y0 + 2 * dy, s)
    for k, lab in (("s05.b", "3 letras"), ("s05.c", "2 letras"), ("s05.d", "1 letra")):
        i = ("s05.b", "s05.c", "s05.d").index(k)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, i=i, lab=lab: E.escreve(c, lab, 1460, y0 + i * dy, 56, "i", TINTA2, a))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: E.pilula(c, "escalonamento", 1530, 200, 56, estilo="g", a=a))
    if t >= C["s05.f"]:
        p = ep(t, C["s05.f"], 0.8)
        M.arrow(c, 1700, y0 + 2 * dy, 1700, lerp(y0 + 2 * dy, y0 - 60, p), CERTO, p, 7, 24, p)
        E.foco(c, t, C["s05.f"] + 0.4, 0.5, lambda a: E.escreve(c, "de baixo para cima", 1150, 980, 60, "b", CERTO, a))


# ---------------- eliminar ----------------
def b_elimina(c, t, C, b):
    s = 64
    # o sistema, pequeno, à esquerda
    cores = [None, {0: SOME}, {0: SOME}] if t >= C["s06.a"] else None
    sistema3(c, t, [C["s06"]] * 3, S, 240, 300, s, dy=110, cores=cores)
    E.foco(c, t, C["s06"], 0.5, lambda a: (E.escreve(c, "1ª", 70, 300, 44, "b", TINTA2, a), E.escreve(c, "2ª", 70, 410, 44, "b", TINTA2, a),
                                            E.escreve(c, "3ª", 70, 520, 44, "b", TINTA2, a)))
    E.foco(c, t, C["s06.a"], 0.5, lambda a: E.escreve(c, "tire o x das outras", XE, 700, 56, "i", SOME, a))
    xo, yo, so = 1060, 300, 80

    def op1():
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "2ª − 1ª", xo - 160, 190, 56, "b", COR, a))
        conta_eq(c, t, C["s06.b"], S[1], S[0], ((0, 1, 0), 2), xo, yo, so, C["s06.c"] - 0.6, cores_res={0: SOME, 2: SOME})
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "y = 2", xo, 850, 110, "g", CERTO, a))
    E.saida(c, t, C["s07"] - 0.1, op1)
    if C["s07"] <= t:
        def op2():
            E.foco(c, t, C["s07.a"], 0.4, lambda a: E.escreve(c, "3ª − 1ª", xo - 160, 190, 56, "b", COR, a))
            conta_eq(c, t, C["s07.a"], S[2], S[0], ((0, 0, 1), 3), xo, yo, so, C["s07.b"], cores_res={0: SOME, 1: SOME})
            E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "z = 3", xo, 850, 110, "g", CERTO, a))
        E.saida(c, t, C["s08"] - 0.1, op2)
    if C["s08"] <= t:
        E.foco(c, t, C["s08.a"], 0.5, lambda a: E.formula(c, "2x + ... ?", xo - 100, 400, 100, "g", SOME, a))
        E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "1ª × 2, depois subtraia", xo - 100, 560, 70, "b", COR, a))
        E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "o x precisa sumir", xo + 260, 760, 60, estilo="g", fundo=SOME, a=a))
    E.foco(c, t, C["s06.c"] + 0.4, 0.5, lambda a: E.formula(c, "y = 2", 240, 880, 70, "g", CERTO, a))
    E.foco(c, t, C["s07.c"] + 0.4, 0.5, lambda a: E.formula(c, "z = 3", 520, 880, 70, "g", CERTO, a))


# ---------------- subir ----------------
def b_subir(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("suba", "g", 84, CERTO), ("a", "i", 90), ("escada", "i", 90)], XE, 190)
    s, x0, y0, dy = 92, 420, 390, 150
    escada(c, x0 - 80, y0 - 110, 980, 3 * dy, 3, COR, ep(t, C["s09"], 0.6))
    eq_em(c, t, C["s09"], (1, 1, 1), 6, x0, y0, s, cores={1: CERTO if t >= C["s09.b"] else TINTA, 2: CERTO if t >= C["s09.b"] else TINTA})
    eq_em(c, t, C["s09"] + 0.2, (0, 1, 0), 2, x0, y0 + dy, s, cores={1: CERTO, "r": CERTO})
    eq_em(c, t, C["s09"] + 0.4, (0, 0, 1), 3, x0, y0 + 2 * dy, s, cores={2: CERTO, "r": CERTO})
    if t >= C["s09"]:
        p = ep(t, C["s09.a"], 0.8)
        M.arrow(c, 1460, y0 + 2 * dy, 1460, lerp(y0 + 2 * dy, y0 - 40, p), CERTO, p, 7, 24, p)
    x = 1560
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "x + 2 + 3 = 6", x - 60, 360, 64, "b", TINTA, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "x + 5 = 6", x - 60, 450, 64, "b", TINTA, a))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "x = 1", x - 60, 560, 90, "g", CERTO, a))
    E.foco(c, t, C["s10.a"], 0.5, lambda a: (E.selo(c, 960, 925, 60, True, a), E.formula(c, "(1, 2, 3)", 1050, 955, 100, "g", CERTO, a)))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "3ª: 1 + 2 + 2·3 = 9", XE, 955, 64, "b", TINTA, a))
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.escreve(c, "bateu", 1560, 955, 80, "g", CERTO, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 104, ERRADO), ("com", "i", 96), ("isto", "i", 96)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("subtrair só o lado das letras", "i", 70, ERRADO), XE, 300)
    xo, yo, so = 520, 470, 88
    conta_eq(c, t, C["s11.a"] + 0.4, S[1], S[0], ((0, 1, 0), 8), xo, yo, so, C["s11.b"], cores_res={1: ERRADO, "r": ERRADO, 0: CINZA, 2: CINZA})
    if t >= C["s11.c"]:
        E.risco(c, xo - 40, yo + 2 * so * 1.35 + 40, xo + 3 * so * 2.2 + 160, yo + 2 * so * 1.35 - 60, t, C["s11.c"], largura=12)
        E.foco(c, t, C["s11.c"], 0.5, lambda a: E.escreve(c, "8 − 6 = 2", 1300, 760, 90, "g", CERTO, a))
    E.frase(c, t, C["s11.d"], [("sai", "i", 84), ("de", "i", 84), ("um", "i", 84), ("lado,", "i", 84), ("sai", "i", 84), ("do", "i", 84), ("outro", "g", 78, COR)], W / 2, 980, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12"], [("o", "i", 84, CLARO), ("atalho", "i", 84, CLARO)], XE, 190)
    E.frase(c, t, C["s12.a"], [("teste", "g", 84, BR), ("os", "i", 90, BR), ("trios", "g", 84, CLARO)], XE, 330)
    for n, (l, sol) in enumerate(ALTS):
        y = 520 + n * 150
        ok = all(vale(e, sol) for e in S)
        E.foco(c, t, C["s12.b"] + 0.3 * n, 0.5, lambda a, l=l, sol=sol, y=y: E.formula(c, f"{l}  ({sol[0]}, {sol[1]}, {sol[2]})", XE, y, 90, "g", BR, a))
        E.foco(c, t, C["s12.c"] + 0.4 * n, 0.5, lambda a, ok=ok, y=y: E.selo(c, 900, y - 30, 48, ok, a))
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.escreve(c, "vale em todas?", 1080, 560, 70, "i", CLARO, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.escreve(c, "comece pela mais diferente", 1080, 680, 56, "b", "#FFB833", a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.escreve(c, "sem alternativas: escalone", 1080, 800, 56, "b", E.ERRADO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    sistema3(c, t, [C["s14.a"], C["s14.b"], C["s14.c"]], Q, 380, 400, 96)
    E.relogio(c, t, C["s15.a"], cx=1560, cy=520, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    s = 56
    sistema3(c, t, [C["s16"]] * 3, Q, 200, 220, s, dy=90)
    xo, yo, so = 1000, 260, 70

    def op1():
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.escreve(c, "1ª × 2", xo - 150, 170, 52, "b", COR, a))
        conta_eq(c, t, C["s16.b"] - 0.6, Q[1], E2, R1, xo, yo, so, C["s16.c"], cores_res={0: SOME, "r": TINTA})
    E.saida(c, t, C["s17"] - 0.1, op1)
    if C["s17"] <= t < C["s18"]:
        def op2():
            E.foco(c, t, C["s17.a"], 0.4, lambda a: E.escreve(c, "3ª − 1ª", xo - 150, 170, 52, "b", COR, a))
            eq_em(c, t, C["s17.a"] + 0.2, R2[0], R2[1], xo, yo, so)
            eq_em(c, t, C["s17.b"] - 0.2, R1[0], R1[1], xo, yo + so * 1.35, so)
            E.foco(c, t, C["s17.b"], 0.4, lambda a: E.escreve(c, "−", xo - so * 1.7, yo + so * 1.35, so, "g", COR, a))
            q = ep(t, C["s17.b"] + 0.2, 0.5)
            if q > 0:
                M.line(c, xo - so * 1.8, yo + so * 1.8, xo - so * 1.8 + (3 * so * 2.2 + so * 2.6) * q, yo + so * 1.8, TINTA, 1, 5)
            E.foco(c, t, C["s17.c"], 0.5, lambda a: eq(c, R3[0], R3[1], xo, yo + 2 * so * 1.35 + so * 0.25, so, a, cores={1: SOME}, zero=True))
            E.foco(c, t, C["s17.d"], 0.5, lambda a: E.formula(c, "z = 1", xo, 760, 100, "g", CERTO, a))
        E.saida(c, t, C["s18"] - 0.1, op2)
    # a escada que vai se formando à esquerda
    y0, dy, se = 560, 120, 70
    if t >= C["s16.c"]:
        escada(c, 120, y0 - 85, 820, 3 * dy, 3, COR, ep(t, C["s16.c"], 0.6))
        eq_em(c, t, C["s16.c"], Q[0][0], Q[0][1], 220, y0, se)
        eq_em(c, t, C["s16.c"] + 0.3, R1[0], R1[1], 220, y0 + dy, se)
    eq_em(c, t, C["s17.d"], (0, 0, 1), 1, 220, y0 + 2 * dy, se, cores={2: CERTO, "r": CERTO})
    if t >= C["s18"]:
        x = 1080
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "y − 1 = 2  →  y = 3", x, 420, 70, "g", TINTA, a))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "x + 3 + 1 = 6  →  x = 2", x, 560, 70, "g", TINTA, a))
        E.foco(c, t, C["s18.c"], 0.5, lambda a: (E.selo(c, x + 30, 895, 60, True, a), E.formula(c, "(2, 3, 1)", x + 130, 930, 110, "g", CERTO, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (k, s) in enumerate((("s19.a", "tire o x das outras"), ("s19.b", "repita até a escada"), ("s19.c", "suba e confira"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 430, y - 30, 56, a=a), E.centro(c, str(i + 1), 430, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 96)], 530, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s20.a"], [("infinitas", "g", 140, COR)], XE, 470)
    E.frase(c, t, C["s20.b"], [("ou", "i", 120), ("nenhuma", "g", 140, COR)], XE, 630)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1560, p), lerp(1000, 845, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, sistema=b_sistema, elimina=b_elimina, subir=b_subir, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
