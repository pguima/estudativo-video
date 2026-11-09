"""Visual — Estudativo · FIS-ELE-012: resistores em paralelo.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: circuito com F.fio, F.pilha, F.resistor; corrente = setinhas laranja do + para o − por fora da pilha;
Ω e = só na fonte pesada).
Nesta aula: o paralelo é a peça `escada` (pilha à esquerda, trilho de cima e de baixo, cada resistor um degrau vertical
entre os trilhos: todos ligam os mesmos dois pontos). Corrente de cada ramo numa pílula laranja ao lado dele; a tensão,
em cinza. Índices (R_1, R_{eq}) com `fi`, cópia local de E.formula que aceita "_".
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
ARQUIVO_FINAL = "estudativo_FIS-ELE-012_resistores_em_paralelo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("paralelo", "conta", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
par = lambda a, b: Fr(a * b, a + b)
assert par(6, 6) == 3 and Fr(1, 3) + Fr(1, 6) == Fr(3, 6) == Fr(1, 2) and par(3, 6) == 2
assert 12 / 3 == 4 and 12 / 6 == 2 and 4 + 2 == 6 == 12 / 2 and 3 * 6 == 18 and 3 + 6 == 9 and 18 / 9 == 2
assert Fr(12, 3) == 4 and par(6, 3) == 2 and par(2, 2) == 1
assert par(4, 12) == 3 and 4 * 12 == 48 and 4 + 12 == 16 and 12 / 3 == 4 and 12 / 4 == 3 and 12 / 12 == 1 and 3 + 1 == 4


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


# ---------------- pedágio ----------------
def pedagio(c, t, x, y, faixas, a=1.0, t_nova=None):
    """pedágio visto de cima: faixas horizontais com cabine no meio e carros passando; a 2ª faixa abre em t_nova"""
    if a <= 0:
        return
    for k in range(faixas):
        q = a * (ep(t, t_nova, 0.6) if k == 1 and t_nova is not None else 1.0)
        if q <= 0:
            continue
        yy = y + k * 170
        c.drawRect(skia.Rect.MakeXYWH(x, yy, 900, 130), M.paint("#D9D6CF", q))
        for b in (yy, yy + 130):
            M.line(c, x, b, x + 900, b, TINTA2, q, 4)
        M.rrect(c, x + 420, yy - 30, 60, 50, 8, TINTA, q)
        M.line(c, x + 450, yy + 20, x + 450, yy + 65, E.COR, q, 8)
        for j in range(4):
            cx = x + ((t * 160 + j * 240 + k * 90) % 960) - 40
            if x <= cx <= x + 860:
                M.rrect(c, cx, yy + 40, 90, 50, 14, E.COR if j % 2 else F.VEL, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        x0, y0, y1 = 900, 360, 780
        escada(c, t, C["s01"], x0, y0, y1, [1250], [("R", "6 Ω", C["s01"] + 0.3)], "12 V")
        if t >= C["s01.a"]:
            F.fio(c, t, C["s01.a"], [(1250, y0), (1580, y0)], 0.5)
            F.fio(c, t, C["s01.a"], [(1250, y1), (1580, y1)], 0.5)
            F.resistor(c, t, C["s01.a"] + 0.4, (1580, y0), (1580, y1), "6 Ω")
            E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: (F.no(c, (1250, y0), a), F.no(c, (1250, y1), a)))
        E.frase(c, t, C["s01"], ps("mais um resistor", "i", 80), XE, 260, passo=0.14)
        E.frase(c, t, C["s01"] + 0.6, ps("resistência total:", "i", 60, TINTA2), XE, 470, passo=0.12)
        troca(c, t, [(C["s01"] + 1.0, ("6", TINTA)), (C["s01.b"], ("3", CERTO))],
              lambda s, a: F.medida(c, s[0], "Ω", XE, 650, 170, s[1], a))
        E.frase(c, t, C["s01.b"] + 0.5, [("diminui", "g", 72, CERTO)], XE, 800)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "em paralelo", XE + 220, 930, 56, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    E.frase(c, t, C["s02.a"] + 1.0, [("a", "i", 80), ("equivalente", "g", 80, COR)], XE, 420, passo=0.14)
    for i, s in enumerate(("produto pela soma", "iguais: R ÷ n")):
        y = 600 + i * 150
        numero(c, t, C["s02.b"] + 0.4 * i, i + 1, XE + 40, y - 30, 38)
        E.frase(c, t, C["s02.b"] + 0.4 * i + 0.1, [(s, "g", 72, TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "em série, corrente igual e", "a equivalente é a soma", "R_{eq} = R_1 + R_2"),
                              ("s03.c", "frações com o mínimo múltiplo comum:", "denominadores diferentes", "f{1}{3} + f{1}{6} = f{2}{6} + f{1}{6}")))


# ---------------- o que é paralelo ----------------
PX0, PY0, PY1, PXS = 900, 340, 760, [1200, 1460, 1720]


def b_paralelo(c, t, C, b):
    def circuito():
        escada(c, t, C["s04"], PX0, PY0, PY1, PXS, [("R", "R_1", 1e9), ("R", "R_2", 1e9), ("R", "R_3", 1e9)], "U")
        for k in range(3):
            F.resistor(c, t, C["s04.a"] + 0.3 * k, (PXS[k], PY0), (PXS[k], PY1))
            E.foco(c, t, C["s04.a"] + 0.3 * k + 0.2, 0.4, lambda a, k=k: fi(c, f"R_{k + 1}", PXS[k] + 50, (PY0 + PY1) / 2 + 18, 50, "b", TINTA, a))
        for k in range(2):
            E.foco(c, t, C["s04.b"], 0.4, lambda a, k=k: (F.no(c, (PXS[k], PY0), a), F.no(c, (PXS[k], PY1), a)))
        if t >= C["s04.c"]:
            r = 30 + 8 * math.sin(t * 5)
            c.drawCircle(PXS[0], PY0, r, M.paint(E.COR, ep(t, C["s04.c"], 0.4) * (1 - ep(t, C["s04.d"], 0.4)), stroke=5))
        tag(c, t, C["s04.b"], "A", PXS[0], PY0 - 70, 46, E.COR, "g")
        tag(c, t, C["s04.b"] + 0.3, "B", PXS[0], PY1 + 70, 46, E.COR, "g")
        if t >= C["s04.d"]:
            p = ep(t, C["s04.d"], 0.5)
            E.caixa_pontilhada(c, PXS[1] - 70, PY0 + 20, 190, PY1 - PY0 - 40, p, prog_=p)
            E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: E.pilula(c, "ramo", PXS[1] + 25, PY1 + 70, 44, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s04.a"], ps("cada um num", "i", 62) + [("caminho", "g", 60, COR)], XE, 340, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("os mesmos", "i", 62) + [("2", "g", 60, COR)] + ps("pontos", "i", 62), XE, 440, passo=0.12)
        E.frase(c, t, C["s04.c"], [("nó:", "g", 60, COR)] + ps("onde a corrente se divide", "i", 52, TINTA2), XE, 540, passo=0.1)
        E.frase(c, t, C["s04.d"], [("ramo:", "g", 60, COR)] + ps("cada caminho", "i", 52, TINTA2), XE, 630, passo=0.1)
    E.frase(c, t, C["s04"], [("em", "i", 90), ("paralelo", "g", 90, COR)], XE, 220)
    if t < C["s05"]:
        circuito()
        return
    if t < C["s06"]:
        escada(c, t, -9, PX0, PY0, PY1, PXS, [("R", None, -9)] * 3, "U")
        for k in range(3):
            fi(c, f"R_{k + 1}", PXS[k] + 50, (PY0 + PY1) / 2 + 18, 50, "b", TINTA, 1.0)
        numero(c, t, C["s05.a"], 1, XE + 30, 370)
        E.frase(c, t, C["s05.a"], [("U", "g", 64, COR), ("igual", "g", 64), ("em", "i", 66), ("todos", "i", 66)], XE + 80, 392, passo=0.12)
        for k in range(3):
            tag(c, t, C["s05.a"] + 0.6 + 0.2 * k, "U", PXS[k] - 88, (PY0 + PY1) / 2, 42)
        numero(c, t, C["s05.b"], 2, XE + 30, 570)
        E.frase(c, t, C["s05.b"], [("i", "g", 64, COR), ("total", "i", 66), ("=", "g", 64, TINTA2), ("soma", "g", 64)], XE + 80, 592, passo=0.12)
        fi_em(c, t, C["s05.b"] + 1.0, "i = i_1 + i_2 + i_3", XE + 80, 720, 70, "g", TINTA)
        corrente_escada(c, t, C["s05.b"] + 0.5, PX0, PY0, PY1, PXS)
        return
    # s06: o pedágio
    E.frase(c, t, C["s06"], ps("por que a equivalente", "i", 64) + [("diminui?", "g", 62, COR)], XE, 340, passo=0.12)
    E.foco(c, t, C["s06.a"], 0.5, lambda a: pedagio(c, t, 880, 420, 2, a, C["s06.b"]))
    E.frase(c, t, C["s06.a"], [("pedágio", "g", 64)], XE, 480)
    E.frase(c, t, C["s06.b"], ps("mais uma cabine", "i", 56, TINTA2), XE, 580, passo=0.1)
    E.frase(c, t, C["s06.c"], ps("passa mais carro", "g", 56, CERTO), XE, 670, passo=0.1)
    E.frase(c, t, C["s06.d"], ps("cada ramo novo =", "i", 64) + [("mais", "g", 62, COR), ("um", "g", 62, COR), ("caminho", "g", 62, COR)],
            XE, 900, passo=0.12)


# ---------------- a conta ----------------
CX0, CY0, CY1, CXS = 1000, 330, 720, [1300, 1630]


def b_conta(c, t, C, b):
    def s07():
        fi_em(c, t, C["s07.a"], "i_1 = f{U}{R_1}", XE, 380, 110, "g", TINTA)
        fi_em(c, t, C["s07.a"] + 0.6, "i_2 = f{U}{R_2}", XE + 600, 380, 110, "g", TINTA)
        E.foco(c, t, C["s07.a"] + 1.2, 0.4, lambda a: E.escreve(c, "a lei de Ohm em cada ramo", XE, 520, 50, "i", TINTA2, a))
        fi_em(c, t, C["s07.b"], "f{1}{R_{eq}} = f{1}{R_1} + f{1}{R_2} + ...", W / 2, 800, 130, "g", COR, "center")
    E.frase(c, t, C["s07"], ps("a conta sai da", "i", 70) + [("lei", "g", 66), ("de", "g", 66), ("Ohm", "g", 66)], XE, 200, passo=0.12)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    # circuito do exemplo, que fica até o fim do bloco
    escada(c, t, C["s08.a"], CX0, CY0, CY1, CXS, [("R", "3 Ω", C["s08.a"] + 0.3), ("R", "6 Ω", C["s08.a"] + 0.5)], None)
    fi(c, "f{1}{R_{eq}} = f{1}{R_1} + f{1}{R_2}", 1440, 950, 60, "g", TINTA2, ep(t, C["s08.a"], 0.5)) if t >= C["s08.a"] else None

    def s08():
        y = 520
        troca(c, t, [(C["s08.b"], "f{1}{3} + f{1}{6}"), (C["s08.c"], "f{2}{6} + f{1}{6}"), (C["s08.d"], "f{3}{6}"), (C["s08.e"], "f{1}{2}")],
              lambda s, a: fi(c, s, XE, y, 120, "g", TINTA, a))
        E.foco(c, t, C["s08.c"] + 0.3, 0.4, lambda a: E.escreve(c, "mínimo múltiplo comum: 6", XE, y + 170, 48, "i", TINTA2, a))
        fi_em(c, t, C["s08.f"] - 0.8, "f{1}{R_{eq}} = f{1}{2}", XE, 840, 90, "g", TINTA)
        bola_txt(c, t, C["s08.f"], "2 Ω", 820, 800, 110, 76, CERTO)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if C["s09"] <= t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("2", "g", 120, CERTO), ("Ω", "g", 90, F.UNID), ("<", "g", 110, TINTA2), ("3", "g", 120), ("Ω", "g", 90, F.UNID)], XE, 520, passo=0.15)
            E.frase(c, t, C["s09.a"] + 1.0, ps("menor que o menor", "i", 62, TINTA2), XE, 640, passo=0.12)
            E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "em paralelo: R eq < o menor", XE + 400, 820, 50, "b", fundo=TINTA, a=a))
        E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    # s10: as correntes
    E.foco(c, t, C["s10.a"], 0.4, lambda a: E._cola(c, "12 V", CX0, (CY0 + CY1) / 2, -1, 0, 70, 50, "b", TINTA, a))
    corrente_escada(c, t, C["s10.b"], CX0, CY0, CY1, CXS)
    tag(c, t, C["s10.b"] + 0.4, "4 A", CXS[0] - 90, (CY0 + CY1) / 2, 44, E.COR, "g")
    tag(c, t, C["s10.c"], "2 A", CXS[1] - 90, (CY0 + CY1) / 2, 44, E.COR, "g")
    tag(c, t, C["s10.e"], "6 A", (CX0 + CXS[0]) / 2, CY0 - 60, 44, E.COR, "g")
    E.formula_em(c, t, C["s10.b"], "12 ÷ 3 = 4 A", XE, 380, 80, "g", TINTA)
    E.formula_em(c, t, C["s10.c"], "12 ÷ 6 = 2 A", XE, 520, 80, "g", TINTA)
    E.frase(c, t, C["s10.d"], [("menor", "i", 60), ("R,", "g", 58, COR), ("maior", "i", 60), ("i", "g", 58, COR)], XE, 660, passo=0.12)
    E.formula_em(c, t, C["s10.e"], "4 + 2 = 6 = 12 ÷ 2", XE, 800, 76, "g", CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s11.a"], ps("parar no", "i", 70) + [("um", "g", 66), ("meio", "g", 66)], XE, 360, passo=0.12)
    E.foco(c, t, C["s11.a"] + 0.8, 0.5, lambda a: F.medida(c, "0,5", "Ω", 1150, 380, 130, ERRADO, a))
    if t >= C["s11.c"]:
        E.risco(c, 1130, 400, 1480, 280, t, C["s11.c"], largura=12)
    fi_em(c, t, C["s11.b"], "f{1}{R_{eq}} = f{1}{2}", XE, 640, 110, "g", TINTA)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "vire a fração", XE + 680, 600, 48, "g", fundo=E.COR, a=a))
    fi_em(c, t, C["s11.d"], "R_{eq} = 2 Ω", XE + 1000, 640, 110, "g", CERTO)
    E.frase(c, t, C["s11.e"], ps("na prova, o meio ohm é a", "i", 58, TINTA2) + [("armadilha", "g", 56, ERRADO)], XE, 900, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"], ps("agora, os atalhos", "i", 76, CLARO), W / 2, 170, "center")
        numero(c, t, C["s12.a"], 1, 420, 330, 36)
        E.frase(c, t, C["s12.a"], ps("dois resistores:", "i", 70, CLARO) + [("produto", "g", 66, BR), ("pela", "g", 66, BR), ("soma", "g", 66, BR)], 480, 355, passo=0.12)
        fi_em(c, t, C["s12.a"] + 1.6, "R_{eq} = f{R_1 · R_2}{R_1 + R_2}", W / 2, 560, 110, "g", BR, "center")
        troca(c, t, [(C["s12.b"], "f{3 · 6}{3 + 6}"), (C["s12.c"], "f{18}{9}")], lambda s, a: fi(c, s, W / 2 - 120, 830, 110, "g", CLARO, a, "right"))
        E.foco(c, t, C["s12.c"] + 0.4, 0.4, lambda a: E.formula(c, "=", W / 2 - 60, 830, 110, "g", CLARO, a))
        bola_txt(c, t, C["s12.d"], "2 Ω", W / 2 + 130, 800, 100, 70)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    numero(c, t, C["s13.a"], 2, 420, 220, 36)
    E.frase(c, t, C["s13.a"], ps("iguais:", "i", 70, CLARO), 480, 245)
    fi_em(c, t, C["s13.a"] + 0.6, "R_{eq} = f{R}{n}", 760, 245, 80, "g", BR)
    E.formula_em(c, t, C["s13.b"], "3 de 12 Ω: f{12}{3} =", 480, 440, 80, "g", CLARO)
    bola_txt(c, t, C["s13.c"], "4 Ω", 1370, 410, 85, 62)
    E.frase(c, t, C["s13.d"], ps("é a soma de frações, já pronta", "i", 58, CLARO), W / 2, 610, "center", 0.1)
    E.frase(c, t, C["s13.e"], [("três", "g", 58, BR), ("diferentes?", "i", 62, CLARO)] + ps("junte dois, depois o terceiro", "i", 62, CLARO), W / 2, 750, "center", 0.1)
    E.formula_em(c, t, C["s13.f"], "6 e 3 → 2 Ω", W / 2 - 300, 900, 72, "g", BR, "center")
    E.formula_em(c, t, C["s13.g"], "2 e 2 → 1 Ω", W / 2 + 300, 900, 72, "g", BR, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: F.medida(c, 12, "V", XE, 360, 100, COR, a))
    E.frase(c, t, C["s14.b"], ps("em paralelo:", "i", 64), XE, 480)
    E.frase(c, t, C["s14.b"] + 0.4, [("4", "g", 64), ("e", "i", 64), ("12", "g", 64), ("Ω", "g", 50, F.UNID)], XE, 570, passo=0.15)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: fi(c, "R_{eq} = ?", XE, 730, 76, "g", TINTA, a))
    E.frase(c, t, C["s14.d"], ps("corrente da pilha?", "g", 60), XE, 860, passo=0.1)
    if t < C["s15"]:
        escada(c, t, C["s14.a"], 960, 360, 780, [1290, 1620], [("R", "4 Ω", C["s14.b"]), ("R", "12 Ω", C["s14.b"] + 0.3)], "12 V")
    else:
        E.relogio(c, t, C["s15.a"], cx=1400, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    x0, y0, y1, xs = 1000, 360, 760, [1300, 1630]
    escada(c, t, C["s16"], x0, y0, y1, xs, [("R", "4 Ω", C["s16"]), ("R", "12 Ω", C["s16"])], "12 V")

    def s16():
        troca(c, t, [(C["s16.a"], "f{4 · 12}{4 + 12}"), (C["s16.b"], "f{48}{16}")], lambda s, a: fi(c, s, XE, 420, 100, "g", TINTA, a))
        bola_txt(c, t, C["s16.c"], "3 Ω", 640, 390, 100, 70, CERTO)
        E.foco(c, t, C["s16.c"] + 0.8, 0.4, lambda a: E.escreve(c, "menor que 4: confere", XE, 570, 50, "i", TINTA2, a))
        E.formula_em(c, t, C["s16.d"], "i = 12 ÷ 3", XE, 760, 90, "g", TINTA)
        bola_txt(c, t, C["s16.e"], "4 A", 760, 730, 100, 70, CERTO)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    corrente_escada(c, t, C["s17.a"], x0, y0, y1, xs)
    E.frase(c, t, C["s17.a"], ps("conferindo pelos ramos", "i", 70, TINTA2), XE, 300, passo=0.12)
    E.formula_em(c, t, C["s17.b"], "12 ÷ 4 = 3 A", XE, 470, 84, "g", TINTA)
    E.formula_em(c, t, C["s17.c"], "12 ÷ 12 = 1 A", XE, 610, 84, "g", TINTA)
    tag(c, t, C["s17.b"] + 0.4, "3 A", xs[0] - 90, (y0 + y1) / 2, 44, E.COR, "g")
    tag(c, t, C["s17.c"] + 0.4, "1 A", xs[1] - 90, (y0 + y1) / 2, 44, E.COR, "g")
    E.formula_em(c, t, C["s17.d"], "3 + 1 = 4 A", XE, 790, 90, "g", CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo:", "i", 92, COR), ("em", "i", 92), ("paralelo", "g", 88)], W / 2, 190, "center")
        itens = (("s18.a", [("U", "g", 70, COR), ("é", "i", 74), ("a", "i", 74), ("mesma", "g", 70)]),
                 ("s18.b", [("i", "g", 70, COR), ("se", "i", 74), ("divide", "g", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 160
            numero(c, t, C[k], i + 1, 420, y - 26, 48)
            E.frase(c, t, C[k] + 0.1, partes, 510, y, passo=0.12)
        numero(c, t, C["s18.c"], 3, 420, 674, 48)
        fi_em(c, t, C["s18.c"] + 0.1, "R_{eq} < o menor", 510, 700, 70, "g", TINTA)
        numero(c, t, C["s18.d"], 4, 420, 850, 48)
        fi_em(c, t, C["s18.d"] + 0.1, "f{R_1 · R_2}{R_1 + R_2}   e   f{R}{n}", 510, 880, 70, "g", COR)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("série", "g", 110, COR), ("e", "i", 110), ("paralelo", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s19.a"] + 0.5, [("juntos", "i", 110)], XE, 540)
    # um resistor em série com dois em paralelo
    y0, y1 = 680, 900
    F.fio(c, t, C["s19.b"], [(200, (y0 + y1) / 2), (260, (y0 + y1) / 2)], 0.3)
    F.resistor(c, t, C["s19.b"] + 0.2, (260, (y0 + y1) / 2), (520, (y0 + y1) / 2))
    F.fio(c, t, C["s19.b"] + 0.3, [(520, (y0 + y1) / 2), (580, (y0 + y1) / 2), (580, y0), (620, y0)], 0.4)
    F.fio(c, t, C["s19.b"] + 0.3, [(580, (y0 + y1) / 2), (580, y1), (620, y1)], 0.4)
    F.resistor(c, t, C["s19.b"] + 0.5, (620, y0), (880, y0))
    F.resistor(c, t, C["s19.b"] + 0.6, (620, y1), (880, y1))
    F.fio(c, t, C["s19.b"] + 0.7, [(880, y0), (940, y0), (940, y1), (880, y1)], 0.4)
    F.fio(c, t, C["s19.b"] + 0.7, [(940, (y0 + y1) / 2), (1000, (y0 + y1) / 2)], 0.3)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, paralelo=b_paralelo, conta=b_conta, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
