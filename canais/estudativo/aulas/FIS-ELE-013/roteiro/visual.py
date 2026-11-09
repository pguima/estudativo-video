"""Visual — Estudativo · FIS-ELE-013: associação mista de resistores.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: circuito com F.fio, F.pilha, F.resistor; corrente = setinhas laranja do + para o − por fora da pilha;
Ω e = só na fonte pesada).
Nesta aula: o circuito misto é a peça `mista` (pilha à esquerda, um resistor em série no fio de cima e, depois dele, os
ramos em paralelo como degraus entre o trilho de cima e o de baixo). Reduzir = o grupo some desfocando e o equivalente
entra no lugar. Na volta, a corrente de cada resistor numa pílula laranja e a tensão numa pílula cinza.
Atalho das letras: cada nó ganha uma pílula laranja com a letra; fio sem resistor leva a mesma letra.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia
from fractions import Fraction as Fr

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-013_associacao_mista_de_resistores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("reconhecer", "reduzir", "voltar", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
par = lambda a, b: Fr(a * b, a + b)
assert par(6, 3) == 2 and 6 * 3 == 18 and 6 + 3 == 9 and 4 + 2 == 6 and 18 / 6 == 3
assert 4 * 3 == 12 and 2 * 3 == 6 and 12 + 6 == 18 and 6 / 6 == 1 and 6 / 3 == 2 and 1 + 2 == 3
assert 18 / 6 == 3 and 18 / 3 == 6 and 3 + 6 == 9 != 3
assert par(12, 12) == 6 == 12 / 2 and 6 + 4 == 10 and 30 / 10 == 3 and 6 * 3 == 18 and 18 / 12 == 1.5 and 1.5 + 1.5 == 3


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
    hs = [200 + (80 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: fi(c, l3, x + 44, y + 245, 50, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


def tag(c, t, t0, s, cx, cy, size=40, fundo=None, est="b"):
    """pílula pequena (tensão de um resistor, corrente de um ramo, potencial de um ponto)"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo or TINTA2, a=a, cor=BR))


def numero(c, t, t0, i, cx, cy, r=30, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, str(i), cx, cy + r * 0.55, r * 1.3, "g", BR, a)))


# ---------------- fórmula com índice: cópia local de E.formula que aceita "_" (R_{eq}, R_1) ----------------
def _ler_i(s, i=0, fim=None):
    nos, txt = [], ""

    def solta():
        nonlocal txt
        if txt:
            nos.append(("t", txt))
            txt = ""

    while i < len(s):
        ch = s[i]
        if ch == fim:
            solta()
            return nos, i + 1
        if ch in "^_":
            solta()
            if s[i + 1] == "{":
                dentro, i = _ler_i(s, i + 2, "}")
            else:
                dentro, i = [("t", s[i + 1])], i + 2
            nos.append(("e" if ch == "^" else "i", dentro))
        elif ch == "f" and i + 1 < len(s) and s[i + 1] == "{":
            solta()
            cima, i = _ler_i(s, i + 2, "}")
            baixo, i = _ler_i(s, i + 1, "}")
            nos.append(("f", cima, baixo))
        else:
            txt += ch
            i += 1
    solta()
    return nos, i


def _medir_i(nos, size, est):
    w = 0.0
    for n in nos:
        if n[0] == "t":
            w += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            w += _medir_i(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "i":
            w += _medir_i(n[1], size * 0.5, "b") + size * 0.04
        else:
            w += max(_medir_i(n[1], size * 0.78, est), _medir_i(n[2], size * 0.78, est)) + size * 0.22
    return w


def _desenhar_i(c, nos, x, y, size, est, cor, a):
    for n in nos:
        if n[0] == "t":
            E.escreve(c, n[1], x, y, size, est, cor, a)
            x += E.larg(n[1], est, size) + E.APERTO[est] * size + size * 0.02
        elif n[0] == "e":
            _desenhar_i(c, n[1], x + size * 0.02, y - size * 0.42, size * 0.58, est, cor, a)
            x += _medir_i(n[1], size * 0.58, est) + size * 0.04
        elif n[0] == "i":
            _desenhar_i(c, n[1], x + size * 0.01, y + size * 0.16, size * 0.5, "b", cor, a)
            x += _medir_i(n[1], size * 0.5, "b") + size * 0.04
        else:
            s_ = size * 0.78
            wc, wb = _medir_i(n[1], s_, est), _medir_i(n[2], s_, est)
            w = max(wc, wb) + size * 0.12
            _desenhar_i(c, n[1], x + (w - wc) / 2, y - size * 0.46, s_, est, cor, a)
            _desenhar_i(c, n[2], x + (w - wb) / 2, y + size * 0.46, s_, est, cor, a)
            b = max(4, size * 0.07)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(cor, a))
            x += w + size * 0.1
    return x


def fi(c, s, x, y, size, estilo="g", cor=None, a=1.0, align="left"):
    """como E.formula (expoente ^ e fração f{}{}), com índice: "R_{eq} = R_1 + R_2". Devolve a largura"""
    nos, _ = _ler_i(s)
    w = _medir_i(nos, size, estilo)
    if a > 0 and c is not None:
        xi = x - w / 2 if align == "center" else x - w if align == "right" else x
        _desenhar_i(c, nos, xi, y, size, estilo, cor or TINTA, a)
    return w


def fi_em(c, t, t0, s, x, y, size, estilo="g", cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: fi(c, s, x, y, size, estilo, cor, a, align))


# ---------------- peças de circuito (as mesmas nas aulas FIS-ELE-011 a 016) ----------------
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


def escada(c, t, t0, x0, y0, y1, xs, ramos, pilha=None, tp=None, d=0.8, escuro=False, nos=True):
    """circuito em paralelo: pilha no lado esquerdo (+ em cima), trilho de cima em y0 e de baixo em y1; cada ramo é uma peça
    vertical em xs[k] ligando os dois trilhos. ramos = [(tipo, rótulo, instante)] (tipo "R" ou "L")"""
    F.fio(c, t, t0, [(x0, y0), (xs[-1], y0)], d, escuro=escuro)
    F.fio(c, t, t0, [(x0, y1), (xs[-1], y1)], d, escuro=escuro)
    F.pilha(c, t, tp if tp is not None else t0, (x0, y1), (x0, y0), pilha, escuro=escuro)
    for k, p in enumerate(ramos):
        A, B = (xs[k], y0), (xs[k], y1)
        if p[0] == "R":
            F.resistor(c, t, p[2], A, B, p[1], escuro=escuro)
        else:
            F.lampada(c, t, p[2], A, B, rotulo=p[1], escuro=escuro)
        if nos and k < len(xs) - 1:
            E.foco(c, t, p[2], 0.4, lambda a, A=A, B=B: (F.no(c, A, a, escuro), F.no(c, B, a, escuro)))


def corrente_escada(c, t, t0, x0, y0, y1, xs, ramos=None, cor=None):
    """setinhas da corrente no circuito em escada: tronco pela pilha, uma descida por ramo (ramos = índices)"""
    F.corrente(c, t, t0, [(x0, y1), (x0, y0), (xs[-1], y0)], cor, fecha=False)
    F.corrente(c, t, t0, [(xs[-1], y1), (x0, y1)], cor, fecha=False)
    for k in (ramos if ramos is not None else range(len(xs))):
        F.corrente(c, t, t0, [(xs[k], y0), (xs[k], y1)], cor, fecha=False)


def mista(c, t, t0, x0, y0, y1, xr, xs, r1, ramos, pilha=None, d=0.8, escuro=False):
    """pilha à esquerda (+ em cima); resistor r1 = (rótulo, instante) em série no fio de cima, entre xr[0] e xr[1];
    depois dele, os ramos (rótulo, instante) em paralelo, verticais em xs, entre o trilho de cima e o de baixo"""
    F.pilha(c, t, t0, (x0, y1), (x0, y0), pilha, escuro=escuro)
    F.fio(c, t, t0, [(x0, y0), (xr[0], y0)], d, escuro=escuro)
    F.resistor(c, t, r1[1], (xr[0], y0), (xr[1], y0), r1[0], escuro=escuro)
    F.fio(c, t, t0, [(xr[1], y0), (xs[-1], y0)], d, escuro=escuro)
    F.fio(c, t, t0, [(x0, y1), (xs[-1], y1)], d, escuro=escuro)
    for k, (rot, ti) in enumerate(ramos):
        F.resistor(c, t, ti, (xs[k], y0), (xs[k], y1), rot, escuro=escuro)
    if len(xs) > 1:
        E.foco(c, t, ramos[0][1], 0.4, lambda a: (F.no(c, (xs[0], y0), a, escuro), F.no(c, (xs[0], y1), a, escuro)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        x0, y0, y1, ym = 860, 300, 820, 560
        t0 = C["s01.a"]
        F.pilha(c, t, t0, (x0, y1), (x0, y0))
        F.fio(c, t, t0, [(x0, y0), (940, y0)])
        F.resistor(c, t, t0 + 0.2, (940, y0), (1180, y0))
        F.fio(c, t, t0 + 0.3, [(1180, y0), (1720, y0)])
        F.fio(c, t, t0 + 0.3, [(x0, y1), (1720, y1)])
        F.resistor(c, t, t0 + 0.4, (1380, y0), (1380, y1))
        F.resistor(c, t, t0 + 0.5, (1720, y0), (1720, ym))
        F.resistor(c, t, t0 + 0.6, (1720, ym), (1720, y1))
        E.foco(c, t, t0 + 0.6, 0.4, lambda a: (F.no(c, (1380, y0), a), F.no(c, (1380, y1), a)))
        E.frase(c, t, C["s01.a"], ps("parece um", "i", 84) + [("labirinto", "g", 84, COR)], XE, 260, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("duas peças que você já conhece", "i", 54, TINTA2), XE, 400, passo=0.1)
        if t >= C["s01.c"]:
            p = ep(t, C["s01.c"], 0.5)
            E.caixa_pontilhada(c, 1640, y0 + 40, 170, y1 - y0 - 80, p, cor=E.COR, prog_=p)
            pilula_em(c, t, C["s01.c"], "série", 1725, y1 + 70, 50, E.COR)
        if t >= C["s01.d"]:
            p = ep(t, C["s01.d"], 0.5)
            E.caixa_pontilhada(c, 1300, y0 - 40, 560, y1 - y0 + 80, p, cor=F.VEL, prog_=p)
            pilula_em(c, t, C["s01.d"], "paralelo", 1580, y0 - 90, 50, F.VEL)
        E.frase(c, t, C["s01.c"], [("série", "g", 80, COR)], XE, 600)
        E.frase(c, t, C["s01.d"], [("e", "i", 80), ("paralelo", "g", 80, F.VEL)], XE, 720, passo=0.15)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate((("s02.a", "reduzir a 1 resistor", 1.2), ("s02.b", "voltar: cada corrente", 0))):
        y = 480 + i * 170
        numero(c, t, C[k] + dt, i + 1, XE + 40, y - 30, 38)
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "em série, corrente igual:", "as resistências somam", "R_{eq} = R_1 + R_2"),
                              ("s03.c", "em paralelo, tensão igual:", "produto pela soma", "R_{eq} = f{R_1 · R_2}{R_1 + R_2}   ou   f{R}{n}")))


# ---------------- reconhecer ----------------
def b_reconhecer(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("primeiro:", "i", 76, TINTA2) + [("reconhecer", "g", 76, COR)] + ps("cada grupo", "i", 76), XE, 210, passo=0.12)
    # série
    y = 520
    F.fio(c, t, C["s04.b"], [(200, y), (260, y)], 0.3)
    F.resistor(c, t, C["s04.b"] + 0.1, (260, y), (520, y))
    F.resistor(c, t, C["s04.b"] + 0.2, (520, y), (780, y))
    F.fio(c, t, C["s04.b"] + 0.3, [(780, y), (840, y)], 0.3)
    E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: F.no(c, (520, y), a))
    if t >= C["s04.b"] + 0.8:
        r = 34 + 6 * math.sin(t * 5)
        c.drawCircle(520, y, r, M.paint(E.COR, ep(t, C["s04.b"] + 0.8, 0.4), stroke=5))
    E.foco(c, t, C["s04.b"] + 0.9, 0.4, lambda a: E.escreve(c, "nenhum fio sai daqui", 380, y + 110, 46, "i", TINTA2, a))
    pilula_em(c, t, C["s04.b"], "série", 520, 380, 54, E.COR)
    # paralelo
    xa, xb, ya, yb = 1100, 1700, 440, 640
    F.fio(c, t, C["s04.c"], [(1040, (ya + yb) / 2), (xa, (ya + yb) / 2), (xa, ya), (xa + 60, ya)], 0.5)
    F.fio(c, t, C["s04.c"], [(xa, (ya + yb) / 2), (xa, yb), (xa + 60, yb)], 0.5)
    F.fio(c, t, C["s04.c"], [(1760, (ya + yb) / 2), (xb, (ya + yb) / 2), (xb, ya), (xb - 60, ya)], 0.5)
    F.fio(c, t, C["s04.c"], [(xb, (ya + yb) / 2), (xb, yb), (xb - 60, yb)], 0.5)
    F.resistor(c, t, C["s04.c"] + 0.2, (xa + 60, ya), (xb - 60, ya))
    F.resistor(c, t, C["s04.c"] + 0.3, (xa + 60, yb), (xb - 60, yb))
    for P, s in (((xa, (ya + yb) / 2), "A"), ((xb, (ya + yb) / 2), "B")):
        E.foco(c, t, C["s04.c"] + 0.6, 0.4, lambda a, P=P: F.no(c, P, a))
        tag(c, t, C["s04.c"] + 0.8, s, P[0] + (-70 if s == "A" else 70), P[1], 44, E.COR, "g")
    pilula_em(c, t, C["s04.c"], "paralelo", 1400, 340, 54, F.VEL)
    E.foco(c, t, C["s04.c"] + 1.2, 0.4, lambda a: E.escreve(c, "os mesmos dois nós", 1220, 760, 46, "i", TINTA2, a))
    E.frase(c, t, lerp(C["s04.c"], C["s04.end"], 0.6), ps("nó = onde a corrente se divide", "i", 54, TINTA2), W / 2, 950, "center", 0.1)


# ---------------- reduzir ----------------
RX0, RY0, RY1, RXR, RXS = 900, 380, 800, (1000, 1260), [1440, 1720]


def b_reduzir(c, t, C, b):
    t_red, t_ser = C["s06.d"], C["s06.e"]
    # estado 1: o circuito de verdade
    E.saida(c, t, t_red - 0.05, lambda: mista(c, t, C["s05.a"], RX0, RY0, RY1, RXR, RXS, ("4 Ω", C["s05.b"]),
                                               [("6 Ω", C["s05.c"]), ("3 Ω", C["s05.c"] + 0.3)], "18 V"))
    if t < C["s05.c"] + 0.5 or t >= t_red:
        pass
    else:
        p = ep(t, C["s06.a"], 0.5)
        if p > 0:
            E.caixa_pontilhada(c, RXS[0] - 70, RY0 + 30, RXS[1] - RXS[0] + 200, RY1 - RY0 - 60, p, cor=F.VEL, prog_=p)
    # estado 2: o paralelo vira 2 Ω
    if t_red - 0.05 <= t:
        xm = (RXS[0] + RXS[1]) / 2
        def dois():
            mista(c, t, t_red, RX0, RY0, RY1, RXR, [xm], ("4 Ω", -9), [("2 Ω", t_red)], "18 V", d=0.01)
            if t >= t_ser:
                p = ep(t, t_ser, 0.5)
                E.caixa_pontilhada(c, RXR[0] - 30, RY0 - 130, xm - RXR[0] + 170, 400, p, cor=E.COR, prog_=p)
        E.saida(c, t, t_ser + 0.6, dois)
    # estado 3: um só resistor de 6 Ω
    if t >= t_ser + 0.6:
        malha(c, t, t_ser + 0.6, RX0, RY0, 1600, RY1, [("R", "6 Ω", C["s06.f"])], "18 V", d=0.01)
        F.corrente(c, t, C["s07.a"], volta(RX0, RY0, 1600, RY1))
    E.frase(c, t, C["s05"], ps("reduzir", "i", 80) + [("passo", "g", 76, COR), ("a", "i", 80), ("passo", "g", 76, COR)], XE, 210, passo=0.12)
    E.frase(c, t, C["s06.a"], [("1.", "g", 56, COR)] + ps("o paralelo", "i", 60), XE, 360, passo=0.12)
    troca(c, t, [(C["s06.b"], "f{6 · 3}{6 + 3} = f{18}{9}"), (C["s06.c"], "= 2 Ω")], lambda s, a: fi(c, s, XE + 40, 500, 80, "g", TINTA, a))
    E.frase(c, t, C["s06.d"], ps("redesenhe", "i", 56, TINTA2), XE + 40, 620, passo=0.1)
    E.frase(c, t, C["s06.e"], [("2.", "g", 56, COR)] + ps("4 e 2 em série", "i", 60), XE, 740, passo=0.12)
    fi_em(c, t, C["s06.f"], "R_{eq} = 6 Ω", XE + 40, 860, 80, "g", COR)
    E.formula_em(c, t, C["s07.a"], "i = 18 ÷ 6", XE, 990, 70, "g", TINTA)
    bola_txt(c, t, C["s07.b"], "3 A", 1250, 590, 110, 76)


# ---------------- voltar ----------------
def b_voltar(c, t, C, b):
    mista(c, t, C["s08"], RX0, RY0, RY1, RXR, RXS, ("4 Ω", C["s08"]), [("6 Ω", C["s08"]), ("3 Ω", C["s08"])], "18 V")
    F.corrente(c, t, C["s08.b"], [(RX0, RY1), (RX0, RY0), (RXS[0], RY0)], fecha=False)
    E.frase(c, t, C["s08.a"], ps("o caminho de", "i", 76) + [("volta", "g", 76, COR)], XE, 210, passo=0.12)

    def s08():
        tag(c, t, C["s08.b"], "3 A", sum(RXR) / 2, RY0 - 170, 46, E.COR, "g")
        E.formula_em(c, t, C["s08.c"], "4 × 3 = 12 V", XE, 400, 84, "g", TINTA)
        tag(c, t, C["s08.c"] + 0.4, "12 V", sum(RXR) / 2, RY0 + 80, 44)
        E.frase(c, t, C["s08.d"], ps("o paralelo vale", "i", 54, TINTA2) + [("2 Ω", "g", 50, TINTA2)], XE, 520, passo=0.1)
        E.formula_em(c, t, C["s08.e"], "2 × 3 = 6 V", XE, 640, 84, "g", TINTA)
        E.formula_em(c, t, C["s08.e"] + 1.2, "12 + 6 = 18 V", XE, 790, 70, "g", CERTO)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    tag(c, t, -9, "3 A", sum(RXR) / 2, RY0 - 170, 46, E.COR, "g")
    tag(c, t, -9, "12 V", sum(RXR) / 2, RY0 + 80, 44)
    for k in range(2):
        tag(c, t, C["s09.a"] + 0.2 * k, "6 V", RXS[k] - 90, (RY0 + RY1) / 2 + 70, 42)
    E.frase(c, t, C["s09.a"], [("6 V", "g", 64, TINTA), ("nos", "i", 66), ("dois", "i", 66), ("ramos", "i", 66)], XE, 380, passo=0.12)
    E.formula_em(c, t, C["s09.b"], "6 ÷ 6 = 1 A", XE, 520, 80, "g", TINTA)
    E.formula_em(c, t, C["s09.c"], "6 ÷ 3 = 2 A", XE, 650, 80, "g", TINTA)
    tag(c, t, C["s09.b"] + 0.4, "1 A", RXS[0] - 90, (RY0 + RY1) / 2 - 40, 44, E.COR, "g")
    tag(c, t, C["s09.c"] + 0.4, "2 A", RXS[1] - 90, (RY0 + RY1) / 2 - 40, 44, E.COR, "g")
    for k in range(2):
        F.corrente(c, t, C["s09.b"] + 0.4 * k, [(RXS[k], RY0), (RXS[k], RY1)], fecha=False)
    E.formula_em(c, t, C["s09.d"], "1 + 2 = 3 A", XE, 800, 84, "g", CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    RX0, RXR, RXS = 1060, (1140, 1380), [1520, 1760]
    mista(c, t, C["s10"], RX0, RY0, RY1, RXR, RXS, ("4 Ω", C["s10"]), [("6 Ω", C["s10"]), ("3 Ω", C["s10"])], "18 V")
    E.frase(c, t, C["s10.a"], ps("a tensão da pilha no paralelo", "i", 56), XE, 330, passo=0.1)
    for k in range(2):
        tag(c, t, C["s10.a"] + 0.8 + 0.2 * k, "18 V ?", RXS[k] - 110, (RY0 + RY1) / 2 + 70, 42, ERRADO)
    E.formula_em(c, t, C["s10.b"], "18 ÷ 6 = 3 A", XE, 480, 76, "g", ERRADO)
    E.formula_em(c, t, C["s10.c"], "18 ÷ 3 = 6 A", XE, 600, 76, "g", ERRADO)
    E.formula_em(c, t, C["s11.a"], "3 + 6 = 9 A", XE, 740, 76, "g", ERRADO)
    E.foco(c, t, C["s11.a"] + 0.8, 0.4, lambda a: E.formula(c, "≠ 3 A", XE + 500, 740, 76, "g", TINTA, a))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.selo(c, 750, 600, 60, False, a))
    tag(c, t, C["s11.c"], "12 V", sum(RXR) / 2, RY0 + 80, 46, E.COR, "g")
    E.frase(c, t, C["s11.c"], [("12", "g", 60, COR), ("dos", "i", 62), ("18 V", "g", 60), ("ficaram", "i", 62), ("no", "i", 62), ("de", "i", 62),
                               ("4 Ω", "g", 60, COR)], XE, 920, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("o atalho:", "i", 76, CLARO) + [("uma", "g", 72, BR), ("letra", "g", 72, BR), ("em", "g", 72, BR), ("cada", "g", 72, BR),
                                                                  ("nó", "g", 72, BR)], W / 2, 170, "center", 0.12)
        A, B = (560, 400), (1360, 400)
        Cc, D = (760, 760), (1560, 760)
        F.fio(c, t, C["s12"], [(400, 400), A], 0.3, escuro=True)
        F.resistor(c, t, C["s12"] + 0.2, A, B, "R1", escuro=True)
        F.fio(c, t, C["s12"] + 0.3, [B, (1520, 400)], 0.3, escuro=True)
        F.fio(c, t, C["s12"] + 0.4, [A, (A[0], 580), (Cc[0], 580), Cc], 0.6, escuro=True)
        F.fio(c, t, C["s12"] + 0.4, [B, (B[0], 640), (D[0], 640), D], 0.6, escuro=True)
        F.resistor(c, t, C["s12"] + 0.6, Cc, D, "R2", escuro=True, lado=-1)
        for P in (A, B, Cc, D):
            E.foco(c, t, C["s12"] + 0.7, 0.4, lambda a, P=P: F.no(c, P, a, True))
        tag(c, t, C["s12.a"], "A", A[0] - 60, A[1] - 60, 50, E.COR, "g")
        tag(c, t, C["s12.a"] + 0.3, "B", B[0] + 60, B[1] - 60, 50, E.COR, "g")
        # o fio sem resistor não muda a letra
        if t >= C["s12.b"]:
            q = ep(t, C["s12.b"], 0.5)
            F.poli(c, [A, (A[0], 580), (Cc[0], 580), Cc], q, CLARO, 1.0, 10)
            F.poli(c, [B, (B[0], 640), (D[0], 640), D], ep(t, C["s12.b"] + 0.6, 0.5), CLARO, 1.0, 10)
        tag(c, t, C["s12.b"] + 0.6, "A", Cc[0] - 60, Cc[1] + 60, 50, E.COR, "g")
        tag(c, t, C["s12.b"] + 1.2, "B", D[0] + 60, D[1] + 60, 50, E.COR, "g")
        E.frase(c, t, C["s12.c"], [("R1:", "g", 56, BR), ("A–B", "g", 56, CLARO), ("·", "g", 56, CLARO), ("R2:", "g", 56, BR), ("A–B", "g", 56, CLARO),
                                   ("→", "g", 56, CLARO), ("paralelo", "g", 56, BR)], W / 2, 950, "center", 0.1)
        E.frase(c, t, C["s12.d"], ps("não importa o desenho", "i", 50, CLARO), W / 2, 1035, "center", 0.1)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("por quê? o fio tem", "i", 70, CLARO) + [("R", "g", 66, BR), ("≈", "g", 66, CLARO), ("0", "g", 66, BR)], W / 2, 300, "center", 0.12)
    E.formula_em(c, t, C["s13.a"] + 1.4, "U = 0 · i = 0", W / 2, 470, 100, "g", BR, "center")
    E.frase(c, t, C["s13.b"], ps("as duas pontas são o mesmo ponto", "g", 60, BR), W / 2, 640, "center", 0.1)
    E.frase(c, t, C["s13.c"], [("não", "g", 58, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("circuito pequeno, tudo à vista", "i", 62, CLARO),
            W / 2, 860, "center", 0.1)


# ---------------- questão ----------------
QX0, QY0, QY1, QXR, QXS = 960, 400, 800, (1030, 1250), [1400, 1730]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: F.medida(c, 30, "V", XE, 360, 100, COR, a))
    E.frase(c, t, C["s14.b"], [("4", "g", 64), ("Ω", "g", 50, F.UNID), ("em", "i", 64), ("série", "g", 64)], XE, 490, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("com", "i", 64) + [("12", "g", 64), ("Ω", "g", 50, F.UNID), ("e", "i", 64), ("12", "g", 64), ("Ω", "g", 50, F.UNID)],
            XE, 590, passo=0.1)
    E.frase(c, t, C["s14.c"] + 0.8, ps("em paralelo", "g", 60), XE, 680, passo=0.1)
    E.frase(c, t, C["s14.d"], ps("corrente em cada 12 Ω?", "g", 62, COR), XE, 840, passo=0.1)
    if t < C["s15"]:
        mista(c, t, C["s14.a"], QX0, QY0, QY1, QXR, QXS, ("4 Ω", C["s14.b"]), [("12 Ω", C["s14.c"]), ("12 Ω", C["s14.c"] + 0.3)], "30 V")
    else:
        E.relogio(c, t, C["s15.a"], cx=1400, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    mista(c, t, C["s16"], QX0, QY0, QY1, QXR, QXS, ("4 Ω", C["s16"]), [("12 Ω", C["s16"]), ("12 Ω", C["s16"])], "30 V")

    def s16():
        E.formula_em(c, t, C["s16.a"], "12 ÷ 2 = 6 Ω", XE, 300, 80, "g", TINTA)
        E.foco(c, t, C["s16.a"] + 0.4, 0.4, lambda a: E.escreve(c, "dois iguais em paralelo", XE, 380, 46, "i", TINTA2, a))
        fi_em(c, t, C["s16.b"], "R_{eq} = 6 + 4 = 10 Ω", XE, 530, 80, "g", TINTA)
        E.formula_em(c, t, C["s16.c"], "i = 30 ÷ 10", XE, 700, 80, "g", TINTA)
        bola_txt(c, t, C["s16.c"] + 0.8, "3 A", 700, 680, 90, 64)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    F.corrente(c, t, C["s17"], [(QX0, QY1), (QX0, QY0), (QXS[0], QY0)], fecha=False)
    tag(c, t, C["s17"], "3 A", sum(QXR) / 2, QY0 - 170, 44, E.COR, "g")
    E.formula_em(c, t, C["s17.a"], "6 × 3 = 18 V", XE, 320, 80, "g", TINTA)
    for k in range(2):
        tag(c, t, C["s17.a"] + 0.4 + 0.2 * k, "18 V", QXS[k] - 100, (QY0 + QY1) / 2 + 70, 42)
    E.formula_em(c, t, C["s17.b"], "18 ÷ 12", XE, 480, 80, "g", TINTA)
    bola_txt(c, t, C["s17.c"], "1,5 A", 620, 460, 100, 60, CERTO)
    for k in range(2):
        tag(c, t, C["s17.c"] + 0.3 + 0.2 * k, "1,5 A", QXS[k] - 100, (QY0 + QY1) / 2 - 40, 42, E.COR, "g")
        F.corrente(c, t, C["s17.c"] + 0.3, [(QXS[k], QY0), (QXS[k], QY1)], fecha=False)
    E.formula_em(c, t, C["s17.d"], "1,5 + 1,5 = 3 A", XE, 700, 80, "g", CERTO)
    E.frase(c, t, C["s17.d"] + 0.4, ps("ramos iguais, correntes iguais", "i", 50, TINTA2), XE, 800, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        itens = (("s18.a", [("reduza", "g", 66), ("um", "i", 70), ("grupo", "i", 70), ("de", "i", 70), ("cada", "i", 70), ("vez", "i", 70)]),
                 ("s18.b", [("ache", "g", 66), ("a", "i", 70), ("corrente", "i", 70), ("total", "g", 66, COR)]),
                 ("s18.c", [("volte:", "g", 66), ("série,", "i", 70), ("i", "g", 66, COR), ("inteira;", "i", 70), ("paralelo,", "i", 70),
                            ("U", "g", 66, COR), ("igual", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 190
            numero(c, t, C[k], i + 1, 300, y - 26, 48)
            E.frase(c, t, C[k] + 0.1, partes, 390, y, passo=0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.b"], [("curto-circuito", "g", 110, COR)], XE, 420)
    # um resistor com um fio por fora: o curto
    y = 700
    F.fio(c, t, C["s19.a"], [(240, y), (320, y)], 0.3)
    F.resistor(c, t, C["s19.a"] + 0.1, (320, y), (700, y))
    F.fio(c, t, C["s19.a"] + 0.2, [(700, y), (780, y)], 0.3)
    if t >= C["s19.a"] + 0.5:
        F.poli(c, [(320, y), (320, y + 130), (700, y + 130), (700, y)], ep(t, C["s19.a"] + 0.5, 0.6), ERRADO, 1.0, 8)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "o disjuntor", 510, 960, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.d"] + 0.2, 0.4))
    E.frase(c, t, C["s19.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, reconhecer=b_reconhecer, reduzir=b_reduzir, voltar=b_voltar, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
