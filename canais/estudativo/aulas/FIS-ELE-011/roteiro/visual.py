"""Visual — Estudativo · FIS-ELE-011: resistores em série.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: circuito com F.fio, F.pilha, F.resistor; corrente = setinhas laranja do + para o − por fora da pilha;
potencial = número numa pílula, nunca seta; Ω e = só na fonte pesada).
Nesta aula: o circuito é a peça `malha` (pilha no lado esquerdo, + em cima; resistores um atrás do outro no lado de cima).
A tensão de cada resistor aparece numa pílula cinza embaixo dele; a corrente, em laranja, em cima. "R eq" é escrito pela
peça `req` (R pesado com o índice "eq" menor), porque E.formula não tem índice.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-011_resistores_em_serie.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("serie", "equivalente", "exemplo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 2 + 4 == 6 and 12 / 6 == 2 and 2 * 2 == 4 and 4 * 2 == 8 and 4 + 8 == 12
assert 12 * 2 / 6 == 4 and 12 * 4 / 6 == 8 and 12 - 4 == 8
assert 3 + 5 + 12 == 20 and 40 / 20 == 2 and 12 * 2 == 24 and 40 * 12 / 20 == 24 and 3 * 2 == 6 and 5 * 2 == 10 and 6 + 10 + 24 == 40


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "2 A" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete(c, t, C, cena, itens, desenhos=()):
    """lembrete de 2 ou 3 coisas: itens = [(cue, linha fina, linha forte, linha de fórmula ou None)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hs = [200 + (70 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: E.formula(c, l3, x + 44, y + 240, 46, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


# ---------------- peças de circuito (copiadas nas aulas FIS-ELE-011 a 016) ----------------
def malha(c, t, t0, x0, y0, x1, y1, pecas, pilha=None, tp=None, d=0.8, escuro=False):
    """circuito em série: pilha no lado esquerdo (+ em cima), peças no lado de cima, fios no resto.
    pecas = [(tipo, rótulo, instante[, acesa])], tipo "R" (resistor) ou "L" (lâmpada). Devolve os (A, B) de cada peça"""
    n = len(pecas)
    xs = [x0 + (x1 - x0) * k / n for k in range(n + 1)]
    F.fio(c, t, t0, [(x0, y1), (x1, y1), (x1, y0)], d, escuro=escuro)
    F.pilha(c, t, tp if tp is not None else t0, (x0, y1), (x0, y0), pilha, escuro=escuro)
    ab = []
    for k, p in enumerate(pecas):
        A, B = (xs[k], y0), (xs[k + 1], y0)
        ab.append((A, B))
        if p[0] == "R":
            F.resistor(c, t, p[2], A, B, p[1], escuro=escuro)
        else:
            F.lampada(c, t, p[2], A, B, acesa=p[3] if len(p) > 3 else None, rotulo=p[1], escuro=escuro)
    return ab


def volta(x0, y0, x1, y1):
    """o caminho da corrente na malha: sai do + (canto de cima à esquerda) e volta pelo −"""
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def req(c, x, y, size, cor=None, a=1.0, align="left"):
    """"R eq": R pesado com o índice eq menor e mais baixo; devolve a largura"""
    w1, w2 = E.larg("R", "g", size), E.larg("eq", "b", size * 0.5)
    if a > 0 and c is not None:
        x0 = x - (w1 + w2) / 2 if align == "center" else x - w1 - w2 if align == "right" else x
        E.escreve(c, "R", x0, y, size, "g", cor or TINTA, a)
        E.escreve(c, "eq", x0 + w1 + size * 0.02, y + size * 0.16, size * 0.5, "b", cor or TINTA, a)
    return w1 + w2 + size * 0.02


def req_formula(c, t, t0, resto, x, y, size, cor=None, cor_r=None, align="left"):
    """linha "R eq = ..." que entra com foco: resto é escrito com E.formula logo depois do R eq"""
    def fn(a):
        w = req(None, 0, 0, size) + size * 0.2 + E.formula(None, resto, 0, 0, size, "g", a=0)
        x0 = x - w / 2 if align == "center" else x - w if align == "right" else x
        wr = req(c, x0, y, size, cor_r or cor or TINTA, a)
        E.formula(c, resto, x0 + wr + size * 0.2, y, size, "g", cor or TINTA, a)
    E.foco(c, t, t0, 0.5, fn)


def tag(c, t, t0, s, cx, cy, size=40, fundo=None, est="b"):
    """pílula pequena (tensão de um resistor, potencial de um ponto)"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo or TINTA2, a=a, cor=BR))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y, xs = 560, [180 + 260 * k for k in range(7)]
        F.fio(c, t, C["s01.a"], [(100, y), (180, y)], 0.4)
        F.fio(c, t, C["s01.a"] + 0.3, [(xs[-1], y), (xs[-1] + 80, y)], 0.4)
        off = C["s01.c"]
        cores = ("#FFC400", "#FF5A1F", "#2FA84F", "#0A93E0", "#E0009C", "#FFC400")
        for k in range(6):
            A, B = (xs[k], y), (xs[k + 1], y)
            acesa = C["s01.a"] + 0.4 + 0.1 * k if t < off else None
            F.lampada(c, t, C["s01.a"] + 0.1 * k, A, B, acesa=acesa, r=48)
            if t < off and t >= C["s01.a"] + 0.6:
                q = 0.5 + 0.5 * math.sin(t * 5 + k * 1.7)
                c.drawCircle((A[0] + B[0]) / 2, y, 48, M.paint(cores[k], 0.25 * q))
        # a lâmpada que queima: a quarta
        if t >= C["s01.b"]:
            cx = (xs[3] + xs[4]) / 2
            E.foco(c, t, C["s01.b"], 0.3, lambda a: (M.line(c, cx - 50, y - 50, cx + 50, y + 50, ERRADO, a, 10),
                                                     M.line(c, cx - 50, y + 50, cx + 50, y - 50, ERRADO, a, 10)))
            E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: E.pilula(c, "queimou", cx, y - 130, 46, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s01.a"], ps("o pisca-pisca antigo", "i", 84), XE, 250, passo=0.14)
        E.frase(c, t, C["s01.c"], [("a", "i", 76), ("fileira", "i", 76), ("inteira", "i", 76), ("apaga", "g", 76, ERRADO)], XE, 820, passo=0.14)
        E.frase(c, t, C["s01.d"], ps("culpa do jeito de ligar:", "i", 64, TINTA2) + [("em série", "g", 64, COR)], XE, 950, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate((("s02.b", "a equivalente"), ("s02.c", "a corrente"), ("s02.d", "a tensão em cada um"))):
        y = 450 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a primeira lei de Ohm:", "U = R · i", "volt = ohm × ampère"),
                              ("s03.c", "a tensão é uma", "diferença de potencial", None)))


# ---------------- série ----------------
X0, Y0, X1, Y1 = 900, 380, 1760, 800


def b_serie(c, t, C, b):
    E.saida(c, t, C["s04.b"] - 0.1, lambda: (F.resistor(c, t, C["s04.a"], (1050, 560), (1600, 560), "resistor"),
                                             E.frase(c, t, C["s04.a"] + 0.4, ps("a peça feita para ter resistência", "i", 50, TINTA2), 1325, 720, "center", 0.08)))
    if t < C["s04.b"]:
        E.frase(c, t, C["s04"], [("resistor", "g", 90, COR)], XE, 250)
        return
    rs = [("R", "R₁", C["s04.b"] + 0.4), ("R", "R₂", C["s04.b"] + 0.6), ("R", "R₃", C["s04.b"] + 0.8)]
    malha(c, t, C["s04.b"], X0, Y0, X1, Y1, rs, "U")
    F.corrente(c, t, C["s04.c"] + 0.4, volta(X0, Y0, X1, Y1))
    E.frase(c, t, C["s04.b"], [("em", "i", 90), ("série", "g", 90, COR)], XE, 250)
    E.frase(c, t, C["s04.b"] + 0.4, ps("um atrás do outro", "i", 60, TINTA2), XE, 350, passo=0.1)
    E.frase(c, t, C["s04.c"], ps("um só caminho", "g", 56, TINTA), XE, 450, passo=0.1)
    if t < C["s05"]:
        return
    # 1ª regra: a corrente é a mesma
    E.foco(c, t, C["s05.a"], 0.5, lambda a: (E.bola(c, XE + 30, 590, 30, a=a), centro(c, "1", XE + 30, 607, 40, "g", BR, a)))
    E.frase(c, t, C["s05.a"], [("i", "g", 64, COR), ("igual", "g", 64), ("em", "i", 66), ("todos", "i", 66)], XE + 80, 612, passo=0.12)
    for k in range(3):
        cx = X0 + (X1 - X0) * (k + 0.5) / 3
        tag(c, t, C["s05.a"] + 0.4 + 0.2 * k, "i", cx, Y0 - 175, 44, E.COR, "g")
    E.frase(c, t, C["s05.b"], ps("fila única, sem desvio", "i", 52, TINTA2), XE + 80, 690, passo=0.1)
    E.frase(c, t, C["s05.d"], ps("nenhuma carga se perde", "i", 52, TINTA2), XE + 80, 760, passo=0.1)
    if t < C["s06"]:
        return
    # 2ª regra: a tensão se divide
    E.foco(c, t, C["s06.a"], 0.5, lambda a: (E.bola(c, XE + 30, 870, 30, a=a), centro(c, "2", XE + 30, 887, 40, "g", BR, a)))
    E.frase(c, t, C["s06.a"], [("U", "g", 64, COR), ("se", "i", 66), ("divide", "g", 64)], XE + 80, 892, passo=0.12)
    for k, s in enumerate(("U₁", "U₂", "U₃")):
        cx = X0 + (X1 - X0) * (k + 0.5) / 3
        tag(c, t, C["s06.b"] + 0.2 * k, s, cx, Y0 + 100, 42)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "U = U₁ + U₂ + U₃", (X0 + X1) / 2, Y1 + 150, 70, "g", TINTA, a, "center"))


# ---------------- equivalente ----------------
def b_equivalente(c, t, C, b):
    E.frase(c, t, C["s07.a"], ps("resistência", "i", 84) + [("equivalente", "g", 84, COR)], XE, 210, passo=0.14)

    def s07():
        E.frase(c, t, C["s07.b"], ps("um só resistor no lugar de todos:", "i", 56, TINTA2), XE, 320, passo=0.08)
        E.frase(c, t, C["s07.b"] + 1.4, ps("mesma tensão, mesma corrente", "g", 52, TINTA2), XE, 400, passo=0.08)
        E.formula_em(c, t, C["s07.c"], "U = R₁ · i + R₂ · i", XE, 600, 100, "g", TINTA)
        E.formula_em(c, t, C["s07.d"], "U = (R₁ + R₂) · i", XE, 790, 100, "g", COR)
        E.foco(c, t, C["s07.d"] + 0.6, 0.4, lambda a: E.escreve(c, "o i em evidência", XE + 900, 780, 52, "i", TINTA2, a))
        # o desenho: dois resistores viram um
        y = 520
        E.saida(c, t, C["s07.d"] + 0.6, lambda: (F.resistor(c, t, C["s07.b"], (1250, y), (1500, y), "R₁"),
                                                 F.resistor(c, t, C["s07.b"] + 0.2, (1500, y), (1750, y), "R₂")))
        if t >= C["s07.d"] + 0.6:
            F.resistor(c, t, C["s07.d"] + 0.7, (1300, y), (1700, y))
            E.foco(c, t, C["s07.d"] + 0.9, 0.4, lambda a: req(c, 1500, y - 80, 64, COR, a, "center"))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], ps("em série, a equivalente é a", "i", 70) + [("soma", "g", 70, COR)], XE, 360, passo=0.12)
    req_formula(c, t, C["s08.b"], "= R₁ + R₂ + R₃ + ...", W / 2, 600, 120, TINTA, COR, "center")
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "sempre maior que o maior resistor", W / 2, 850, 52, "b", fundo=TINTA, a=a))


# ---------------- exemplo ----------------
EX = (760, 400, 1720, 820)


def b_exemplo(c, t, C, b):
    x0, y0, x1, y1 = EX
    malha(c, t, C["s09.a"], x0, y0, x1, y1, [("R", "2 Ω", C["s09.b"]), ("R", "4 Ω", C["s09.b"] + 0.4)], "12 V")
    F.corrente(c, t, C["s09.e"], volta(x0, y0, x1, y1))
    for k in range(2):
        cx = x0 + (x1 - x0) * (k + 0.5) / 2
        tag(c, t, C["s09.e"] + 0.3 + 0.2 * k, "2 A", cx, y0 - 175, 44, E.COR, "g")
    E.frase(c, t, C["s09"], ps("um exemplo", "i", 76, TINTA2), XE, 200)

    def s09():
        req_formula(c, t, C["s09.c"], "= 2 + 4 = 6 Ω", XE, 380, 84)
        E.formula_em(c, t, C["s09.d"], "i = 12 ÷ 6", XE, 560, 84, "g", TINTA)
        bola_txt(c, t, C["s09.e"], "2 A", XE + 140, 780, 110, 76)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.formula_em(c, t, C["s10"], "U = R · i", XE, 360, 84, "g", COR)
    E.formula_em(c, t, C["s10.a"], "2 × 2 = 4 V", XE, 520, 76, "g", TINTA)
    E.formula_em(c, t, C["s10.b"], "4 × 2 = 8 V", XE, 650, 76, "g", TINTA)
    for k, (s, tk) in enumerate((("4 V", "s10.a"), ("8 V", "s10.b"))):
        cx = x0 + (x1 - x0) * (k + 0.5) / 2
        tag(c, t, C[tk] + 0.4, s, cx, y0 + 110, 46)
    E.formula_em(c, t, C["s10.c"], "4 + 8 = 12 V", XE, 800, 76, "g", CERTO)
    E.frase(c, t, C["s10.d"], [("maior", "i", 60), ("R,", "g", 58, COR), ("maior", "i", 60), ("U", "g", 58, COR)], W / 2 + 200, 990, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    x0, y0, x1, y1 = 960, 420, 1760, 820

    def s11():
        malha(c, t, C["s11"] + 0.3, x0, y0, x1, y1, [("R", "2 Ω", C["s11"] + 0.5), ("R", "4 Ω", C["s11"] + 0.6)], "12 V")
        E.frase(c, t, C["s11.a"], ps("a corrente se gasta?", "i", 64), XE, 330, passo=0.12)
        # a ideia errada: 2 A entra, 1 A sai
        E.saida(c, t, C["s11.c"] - 0.05, lambda: (tag(c, t, C["s11.b"], "2 A", x0 + 120, y0 - 175, 46, E.COR, "g"),
                                                   tag(c, t, C["s11.b"] + 0.5, "1 A ?", x1 - 120, y0 - 175, 46, ERRADO, "g")))
        if t >= C["s11.c"]:
            F.corrente(c, t, C["s11.c"], volta(x0, y0, x1, y1))
            tag(c, t, C["s11.c"], "2 A", x0 + 120, y0 - 175, 46, CERTO, "g")
            tag(c, t, C["s11.c"] + 0.2, "2 A", x1 - 120, y0 - 175, 46, CERTO, "g")
            E.frase(c, t, C["s11.c"], ps("a mesma do começo ao fim", "g", 50, CERTO), XE, 440, passo=0.08)
        # o que cai é o potencial: pílulas nos pontos
        E.frase(c, t, C["s11.d"], ps("o que cai é o", "i", 60) + [("potencial", "g", 58, COR)], XE, 960, passo=0.12)
        for k, (s, P) in enumerate((("12 V", (x0, y0)), ("8 V", ((x0 + x1) / 2, y0)), ("0 V", (x1, y0)))):
            E.foco(c, t, C["s11.d"] + 0.8 + 0.5 * k, 0.4, lambda a, P=P: F.no(c, P, a))
            tag(c, t, C["s11.d"] + 0.8 + 0.5 * k, s, P[0] + (60 if k == 0 else 0), P[1] + 90, 44, TINTA)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    # lâmpada queimada = fio cortado
    malha(c, t, C["s12"], x0, y0, x1, y1, [("L", None, C["s12"] + 0.1), ("L", None, C["s12"] + 0.2), ("L", None, C["s12"] + 0.3)])
    cx = x0 + (x1 - x0) * 1.5 / 3
    E.foco(c, t, C["s12.a"], 0.3, lambda a: (M.line(c, cx - 48, y0 - 48, cx + 48, y0 + 48, ERRADO, a, 10),
                                             M.line(c, cx - 48, y0 + 48, cx + 48, y0 - 48, ERRADO, a, 10)))
    E.frase(c, t, C["s12.a"], ps("lâmpada queimada =", "i", 66) + [("fio cortado", "g", 62, ERRADO)], XE, 340, passo=0.12)
    E.frase(c, t, C["s12.b"], ps("sem caminho:", "i", 66) + [("i", "g", 66, COR), ("=", "g", 66, TINTA2), ("0", "g", 66, COR)], XE, 960, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def barra_partes(c, x, y, w, h, partes, cores, rotulos, a=1.0, cheio=1.0):
    """barra dividida em pedaços proporcionais: partes = [2, 4]; cada pedaço com a cor e o rótulo dele"""
    if a <= 0:
        return
    tot = sum(partes)
    xx = x
    for p, cor, rot in zip(partes, cores, rotulos):
        wp = w * p / tot
        M.rrect(c, xx + 4, y, (wp - 8) * cheio, h, 14, cor, a)
        for k in range(1, p):
            M.line(c, xx + wp * k / p, y + 10, xx + wp * k / p, y + h - 10, "#000000", a * 0.25, 3)
        if rot:
            E._meio(c, rot, xx + wp / 2, y + h / 2, h * 0.42, "g", BR, a)
        xx += wp


def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s13.a"], ps("a tensão se divide na", "i", 64, CLARO) + [("proporção", "g", 62, BR)] + ps("das resistências", "i", 64, CLARO),
                W / 2, 300, "center", 0.1)
        x, w = 360, 1200
        q = ease_io(prog(t, C["s13.b"], 0.8))
        E.foco(c, t, C["s13.b"], 0.5, lambda a: barra_partes(c, x, 470, w, 150, [2, 4], [E.mix(E.COR, BR, 0.35), E.COR], ["2 Ω", "4 Ω"], a, q))
        E.foco(c, t, C["s13.b"] + 0.8, 0.4, lambda a: centro(c, "6 partes", W / 2, 430, 52, "i", CLARO, a))
        E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "f{2}{6} = f{1}{3} de 12 V", x + w / 6, 760, 64, "g", BR, a, "center"))
        bola_txt(c, t, C["s13.d"], "4 V", x + w / 6, 900, 80, 58)
        E.foco(c, t, C["s13.e"], 0.5, lambda a: E.formula(c, "f{2}{3} de 12 V", x + w * 4 / 6, 760, 64, "g", BR, a, "center"))
        bola_txt(c, t, C["s13.e"] + 0.6, "8 V", x + w * 4 / 6, 900, 80, 58)
        E.frase(c, t, C["s13.f"], ps("sem calcular a corrente", "i", 56, CLARO), W / 2 + 560, 1010, "center", 0.1)
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("i", "g", 80, BR), ("igual", "i", 84, CLARO), ("→", "g", 80, CLARO), ("U", "g", 80, BR), ("proporcional", "i", 84, CLARO),
                               ("a", "i", 84, CLARO), ("R", "g", 80, BR)], W / 2, 400, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 68, CLARO)] + ps("a questão pede a corrente", "i", 68, CLARO),
            W / 2, 650, "center", 0.1)
    E.frase(c, t, C["s14.b"] + 2.0, ps("aí, lei de Ohm", "g", 60, BR), W / 2, 780, "center", 0.1)


# ---------------- questão ----------------
QX = (820, 430, 1780, 800)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: F.medida(c, 40, "V", XE, 360, 100, COR, a))
    E.frase(c, t, C["s15.b"], ps("em série:", "i", 64), XE, 480)
    E.frase(c, t, C["s15.b"] + 0.4, [("3,", "g", 64), ("5", "g", 64), ("e", "i", 64), ("12", "g", 64), ("Ω", "g", 50, F.UNID)], XE, 570, passo=0.15)
    E.frase(c, t, C["s15.c"], [("i", "g", 76, COR), ("=", "g", 76, TINTA2), ("?", "g", 76, COR)], XE, 730, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("tensão no de 12 Ω?", "g", 60), XE, 850, passo=0.1)
    if t < C["s16"]:
        x0, y0, x1, y1 = QX
        malha(c, t, C["s15.a"], x0, y0, x1, y1, [("R", "3 Ω", C["s15.b"]), ("R", "5 Ω", C["s15.b"] + 0.3), ("R", "12 Ω", C["s15.b"] + 0.6)], "40 V")
    else:
        E.relogio(c, t, C["s16.a"], cx=1400, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x0, y0, x1, y1 = 880, 560, 1780, 900

    def s17():
        malha(c, t, C["s17"], x0, y0, x1, y1, [("R", "3 Ω", C["s17"]), ("R", "5 Ω", C["s17"]), ("R", "12 Ω", C["s17"])], "40 V")
        req_formula(c, t, C["s17.a"], "= 3 + 5 + 12 = 20 Ω", XE, 230, 80)
        E.formula_em(c, t, C["s17.b"], "i = 40 ÷ 20", XE, 380, 80, "g", TINTA)
        bola_txt(c, t, C["s17.c"], "2 A", 1080, 350, 100, 70)
        F.corrente(c, t, C["s17.c"], volta(x0, y0, x1, y1))
        E.formula_em(c, t, C["s17.d"], "U = 12 × 2", XE, 560, 80, "g", TINTA)
        bola_txt(c, t, C["s17.e"], "24 V", XE + 180, 790, 120, 70, CERTO)
        tag(c, t, C["s17.e"], "24 V", x0 + (x1 - x0) * 5 / 6, y0 + 110, 46, CERTO)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], ps("pelo atalho:", "i", 70, TINTA2), XE, 240)
    E.foco(c, t, C["s18.a"] + 0.6, 0.5, lambda a: E.formula(c, "f{12}{20} = f{3}{5} de 40 V = 24 V", XE, 420, 96, "g", TINTA, a))
    x, w = 300, 1320
    E.foco(c, t, C["s18.b"], 0.5, lambda a: barra_partes(c, x, 620, w, 130, [3, 5, 12], [TINTA2, TINTA2, E.COR], ["6 V", "10 V", "24 V"], a))
    E.foco(c, t, C["s18.b"] + 0.3, 0.4, lambda a: [centro(c, s, x + w * cx / 20, 800, 46, "b", F.UNID, a) for s, cx in (("3 Ω", 1.5), ("5 Ω", 5.5), ("12 Ω", 14))])
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.formula(c, "6 + 10 + 24 = 40 V", W / 2, 960, 80, "g", CERTO, a, "center"))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo:", "i", 92, COR), ("em", "i", 92), ("série", "g", 88)], W / 2, 200, "center")
        itens = (("s19.a", [("i", "g", 76, COR), ("é", "i", 80), ("a", "i", 80), ("mesma", "g", 76)]),
                 ("s19.b", [("U", "g", 76, COR), ("se", "i", 80), ("divide", "g", 76)]),
                 ("s19.c", None))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y - 26, 52, a=a), centro(c, str(i + 1), 420, y - 4, 60, "g", BR, a)))
            if partes:
                E.frase(c, t, C[k] + 0.1, partes, 520, y, passo=0.12)
        req_formula(c, t, C["s19.c"] + 0.1, "= soma", 520, 800, 80, TINTA, COR)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("resistores", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.5, [("em", "i", 110), ("paralelo", "g", 110, COR)], XE, 540)
    # dois resistores lado a lado entre os mesmos dois nós
    xa, xb, ya, yb = 360, 900, 700, 860
    F.fio(c, t, C["s20.a"] + 0.6, [(260, (ya + yb) / 2), (xa, (ya + yb) / 2), (xa, ya), (xa + 60, ya)])
    F.fio(c, t, C["s20.a"] + 0.6, [(xa, (ya + yb) / 2), (xa, yb), (xa + 60, yb)])
    F.fio(c, t, C["s20.a"] + 0.6, [(1000, (ya + yb) / 2), (xb, (ya + yb) / 2), (xb, ya), (xb - 60, ya)])
    F.fio(c, t, C["s20.a"] + 0.6, [(xb, (ya + yb) / 2), (xb, yb), (xb - 60, yb)])
    F.resistor(c, t, C["s20.a"] + 0.9, (xa + 60, ya), (xb - 60, ya))
    F.resistor(c, t, C["s20.a"] + 1.1, (xa + 60, yb), (xb - 60, yb))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "a equivalente diminui", 640, 990, 44, "b", fundo=TINTA, a=a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, serie=b_serie, equivalente=b_equivalente, exemplo=b_exemplo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
