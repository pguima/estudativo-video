"""Visual — Estudativo · FIS-ELE-016: praticando resistores e circuitos (prática, 5 questões).

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: circuito com F.fio, F.pilha, F.resistor, F.chave; corrente = setinhas laranja; Ω e = só na fonte pesada).
Reaproveita as peças das aulas do módulo, copiadas aqui: `fio_cobre` (FIS-ELE-010), `mista` (FIS-ELE-013), `curto` e
`apaga` (FIS-ELE-014), `medidor` e `ponte` (FIS-ELE-015). Cada questão: enunciado à esquerda, desenho à direita, relógio
na pausa; na resposta, a conta à esquerda e as leituras em pílulas no desenho.
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
ARQUIVO_FINAL = "estudativo_FIS-ELE-016_praticando_resistores_e_circuitos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
COBRE = "#C8743A"

# todas as contas da aula
par = lambda a, b: Fr(a * b, a + b)
assert 20 / 2 == 10 and 10 / 2 == 5 == 20 / 4
assert par(12, 6) == 4 and 12 * 6 == 72 and 12 + 6 == 18 and 4 + 4 == 8 and 24 / 8 == 3 and 4 * 3 == 12 and 24 - 12 == 12
assert 12 / 6 == 2 and 12 / 12 == 1 and 2 + 1 == 3
assert 3 * 10 == 30 and 30 / 30 == 1 and 30 / 20 == 1.5
assert 10 * 15 / 5 == 30 and 5 * 30 == 10 * 15 == 150 and Fr(5, 10) == Fr(15, 30)
assert 220 / 22 == 10 and 10 + 10 == 20 > 15 > 10


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


# (copiada de FIS-ELE-010)
def fio_cobre(c, x, cy, L, d, a=1.0, cor=COBRE, corte=True):
    """fio de comprimento L e espessura d, da esquerda (x) para a direita, com o corte (a bolinha) na ponta direita"""
    if a <= 0 or L <= 0:
        return
    rx = max(5, d * 0.22)
    escuro, claro = E.mix(cor, "#000000", 0.3), E.mix(cor, BR, 0.4)
    c.drawOval(skia.Rect.MakeXYWH(x - rx, cy - d / 2, 2 * rx, d), M.paint(escuro, a))
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, cy - d / 2), skia.Point(0, cy + d / 2)],
                                               [M.hexc(claro, a), M.hexc(cor, a), M.hexc(escuro, a)], [0.0, 0.45, 1.0]))
    c.drawRect(skia.Rect.MakeXYWH(x, cy - d / 2, L, d), p)
    if corte:
        c.drawOval(skia.Rect.MakeXYWH(x + L - rx, cy - d / 2, 2 * rx, d), M.paint(E.mix(cor, BR, 0.55), a))
        c.drawOval(skia.Rect.MakeXYWH(x + L - rx, cy - d / 2, 2 * rx, d), M.paint(escuro, a, stroke=3))

# (copiada de FIS-ELE-013)
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

# (copiada de FIS-ELE-014)
def curto(c, t, t0, A, B, fundo=110, d=0.6, cor=ERRADO):
    """fio do curto: sai de A, desce `fundo` px, passa por baixo e volta em B (vermelho)"""
    if t >= t0:
        F.poli(c, [A, (A[0], A[1] + fundo), (B[0], B[1] + fundo), B], ease_io(prog(t, t0, d)), cor, 1.0, 8)

# (copiada de FIS-ELE-014)
def apaga(c, t, t0, A, B, larg=150):
    """véu de papel sobre um resistor que saiu do circuito (fica cinza)"""
    q = ep(t, t0, 0.6)
    if q > 0:
        cx, cy = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        M.rrect(c, cx - larg / 2, cy - 40, larg, 80, 10, E.PAPEL if hasattr(E, "PAPEL") else "#F4F3EF", 0.7 * q)

# (copiada de FIS-ELE-015)
def medidor(c, cx, cy, r, s, a=1.0, escuro=False, cor=None):
    """medidor: círculo com a letra (A, V ou G)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR if not escuro else "#14141C", a))
    c.drawCircle(cx, cy, r, M.paint(cor or (TINTA if not escuro else BR), a, stroke=6))
    E._meio(c, s, cx, cy, r * 1.0, "g", E.COR if not escuro else E.CLARO, a)

# (copiada de FIS-ELE-015)
def ponte(c, t, t0, cx, cy, rx, ry, rots, g=True, xp=None, escuro=False, cores=None, tg=None, d=0.8):
    """ponte de Wheatstone em losango; rots = rótulos de R1..R4; g = desenha o galvanômetro no meio; xp = x da pilha.
    Devolve os quatro vértices (cima, esquerda, baixo, direita)"""
    T, L, B, R = (cx, cy - ry), (cx - rx, cy), (cx, cy + ry), (cx + rx, cy)
    xp = xp if xp is not None else cx - rx - 150
    F.fio(c, t, t0, [T, (cx, cy - ry - 90), (xp, cy - ry - 90), (xp, cy - 200)], d, escuro=escuro)
    F.pilha(c, t, t0, (xp, cy + 200), (xp, cy - 200), None, escuro=escuro)
    F.fio(c, t, t0, [(xp, cy + 200), (xp, cy + ry + 90), (cx, cy + ry + 90), B], d, escuro=escuro)
    cores = cores or [None] * 4
    for k, (A_, B_, lado) in enumerate(((T, L, -1), (L, B, -1), (T, R, 1), (R, B, 1))):
        F.resistor(c, t, t0 + 0.2 + 0.1 * k, A_, B_, rots[k], escuro=escuro, lado=lado, cor=cores[k])
    for P in (T, L, B, R):
        E.foco(c, t, t0 + 0.5, 0.4, lambda a, P=P: F.no(c, P, a, escuro))
    if g:
        tg_ = tg if tg is not None else t0 + 0.6
        F.fio(c, t, tg_, [L, (cx - 60, cy)], 0.4, escuro=escuro)
        F.fio(c, t, tg_, [R, (cx + 60, cy)], 0.4, escuro=escuro)
        E.foco(c, t, tg_ + 0.2, 0.4, lambda a: medidor(c, cx, cy, 60, "G", a, escuro))
    return T, L, B, R


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.foco(c, t, C["s01.a"], 0.6, lambda a: E.escreve(c, "5", XE - 10, 560, 420, "g", COR, a))
    E.frase(c, t, C["s01.a"] + 0.3, ps("questões", "i", 110), XE + 300, 420, passo=0.1)
    E.frase(c, t, C["s01.a"] + 0.6, ps("inéditas", "g", 90), XE + 300, 540, passo=0.1)
    temas = ("o fio", "circuito misto", "medidores", "curto", "ponte", "a casa")
    for i, s in enumerate(temas):
        x, y = 1150 + (i % 2) * 380, 300 + (i // 2) * 160
        E.foco(c, t, C["s01.b"] + 0.25 * i, 0.4, lambda a, s=s, x=x, y=y: E.pilula(c, s, x, y, 52, "g", fundo=TINTA if i % 2 else E.COR, a=a))
    E.frase(c, t, C["s01.c"], ps("pause e resolva antes da resposta", "i", 60, TINTA2), XE, 860, passo=0.1)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as ferramentas", "i", 84, COR), XE, 200)
    linhas = (("s02.a", "U = R · i", None),
              ("s02.b", "série:  i igual,  R_{eq} = R_1 + R_2", None),
              ("s02.c", "paralelo:  U igual,  f{R_1 · R_2}{R_1 + R_2}  ou  f{R}{n}", None),
              ("s02.d", "fio:  R = ρ · f{L}{A}", None))
    for i, (k, s, _) in enumerate(linhas):
        y = 380 + i * 180
        numero(c, t, C[k], i + 1, XE + 30, y - 24, 34)
        fi_em(c, t, C[k] + 0.1, s, XE + 100, y, 68, "g", TINTA)


# ---------------- questão 1: o fio cortado ----------------
def b_questao1(c, t, C, b):
    E.frase(c, t, C["s03.a"], [("questão", "i", 80), ("1", "g", 80, COR)], XE, 200, passo=0.12)
    E.frase(c, t, C["s03.b"], ps("fio de", "i", 64) + [("20", "g", 64), ("Ω", "g", 50, F.UNID)], XE, 360, passo=0.12)
    E.frase(c, t, C["s03.b"] + 1.0, ps("cortado em 2 pedaços iguais", "i", 56, TINTA2), XE, 450, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("ligados em", "i", 64) + [("paralelo", "g", 62, COR)], XE, 590, passo=0.12)
    E.frase(c, t, C["s03.d"], [("R", "g", 76), ("nova", "i", 80), ("=", "g", 76, TINTA2), ("?", "g", 80, COR)], XE, 760, passo=0.12)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=1400, cy=500, r=200)
        return
    q = ease_io(prog(t, C["s03.b"] + 0.8, 0.6))
    p = ease_io(prog(t, C["s03.c"], 0.8))
    x0, y = 1000, 400
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (fio_cobre(c, x0, lerp(y, 520, p), 360, 70, a), fio_cobre(c, x0 + 360 + 60 * q - 360 * p, lerp(y, 700, p), 360, 70, a)))
    if p > 0.95:
        F.fio(c, t, C["s03.c"] + 0.8, [(x0 - 80, 610), (x0 - 40, 610), (x0 - 40, 520), (x0 - 5, 520)], 0.4)
        F.fio(c, t, C["s03.c"] + 0.8, [(x0 - 40, 610), (x0 - 40, 700), (x0 - 5, 700)], 0.4)
        F.fio(c, t, C["s03.c"] + 0.8, [(x0 + 365, 520), (x0 + 420, 520), (x0 + 420, 700), (x0 + 365, 700)], 0.4)
        F.fio(c, t, C["s03.c"] + 0.8, [(x0 + 420, 610), (x0 + 480, 610)], 0.4)
    E.foco(c, t, C["s03.b"] + 1.2, 0.4, lambda a: E.pilula(c, "10 Ω" if p > 0.5 else "20 Ω", x0 + 180, 300 if p < 0.5 else 430, 44, "g", fundo=TINTA, a=a))


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("L", "g", 70, COR), ("÷ 2", "g", 70), ("→", "g", 70, TINTA2), ("R", "g", 70), ("÷ 2", "g", 70, F.NEG)], XE, 300, passo=0.12)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: F.medida(c, 10, "Ω", XE + 620, 300, 90, TINTA, a))
    E.formula_em(c, t, C["s05.c"], "2 iguais:  10 ÷ 2", XE, 500, 84, "g", TINTA)
    bola_txt(c, t, C["s05.d"], "5 Ω", 1150, 480, 110, 76, CERTO)
    E.frase(c, t, C["s05.e"], [("um", "i", 64), ("quarto", "g", 62, COR)] + ps("do fio inteiro", "i", 64), XE, 720, passo=0.12)
    E.formula_em(c, t, C["s05.e"] + 1.2, "20 ÷ 2 ÷ 2 = 5", XE, 860, 76, "g", TINTA2)


# ---------------- questão 2: misto com medidores ----------------
Q2 = dict(x0=960, y0=420, y1=820, xr=(1040, 1260), xs=[1420, 1680])


def q2(c, t, t0, rots, ta, tv, ta_lido=None, tv_lido=None):
    x0, y0, y1, xr, xs = Q2["x0"], Q2["y0"], Q2["y1"], Q2["xr"], Q2["xs"]
    mista(c, t, t0, x0, y0, y1, xr, [xs[0], xs[1]], (rots[0], t0), [(rots[1], t0), (None, 1e9)], "24 V" if rots[0] else None)
    # o ramo de 6 Ω com o amperímetro embaixo
    ym = (y0 + y1) / 2 + 40
    F.resistor(c, t, t0, (xs[1], y0), (xs[1], ym - 70), rots[2])
    if t < ta:
        F.fio(c, t, t0, [(xs[1], ym - 70), (xs[1], y1)], 0.4)
    else:
        F.fio(c, t, t0, [(xs[1], ym - 70), (xs[1], ym - 50)], 0.1)
        F.fio(c, t, t0, [(xs[1], ym + 50), (xs[1], y1)], 0.1)
        E.foco(c, t, ta, 0.4, lambda a: medidor(c, xs[1], ym, 50, "A", a))
    if t >= tv:
        yv = y0 - 170
        xm = (xr[0] + xr[1]) / 2
        F.fio(c, t, tv, [(xr[0], y0), (xr[0], yv), (xm - 50, yv)], 0.4)
        F.fio(c, t, tv, [(xr[1], y0), (xr[1], yv), (xm + 50, yv)], 0.4)
        E.foco(c, t, tv + 0.2, 0.4, lambda a: (medidor(c, xm, yv, 50, "V", a), F.no(c, (xr[0], y0), a), F.no(c, (xr[1], y0), a)))
    if ta_lido is not None:
        tag(c, t, ta_lido, "2 A", xs[1] + 100, ym + 95, 46, E.COR, "g")
    if tv_lido is not None:
        tag(c, t, tv_lido, "12 V", (xr[0] + xr[1]) / 2 + 160, y0 - 170, 46, E.COR, "g")


def b_questao2(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("questão", "i", 80), ("2", "g", 80, COR)], XE, 200, passo=0.12)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: F.medida(c, 24, "V", XE, 330, 84, COR, a))
    E.frase(c, t, C["s06.c"], [("4", "g", 58), ("Ω", "g", 46, F.UNID), ("em", "i", 60), ("série", "g", 56)], XE, 440, passo=0.1)
    E.frase(c, t, C["s06.d"], ps("com", "i", 60) + [("12", "g", 58), ("Ω", "g", 46, F.UNID), ("e", "i", 60), ("6", "g", 58), ("Ω", "g", 46, F.UNID)], XE, 530, passo=0.1)
    E.frase(c, t, C["s06.d"] + 0.8, ps("em paralelo", "g", 56), XE, 610, passo=0.1)
    E.frase(c, t, C["s06.e"], [("A", "g", 56, COR)] + ps("no ramo de", "i", 56) + [("6 Ω", "g", 52)], XE, 730, passo=0.1)
    E.frase(c, t, C["s06.f"], [("V", "g", 56, COR)] + ps("nas pontas do de", "i", 56) + [("4 Ω", "g", 52)], XE, 820, passo=0.1)
    E.frase(c, t, C["s06.g"], ps("o que cada um marca?", "g", 58, COR), XE, 950, passo=0.1)
    if t < C["s07"]:
        q2(c, t, C["s06.b"], ("4 Ω", "12 Ω", "6 Ω"), C["s06.e"], C["s06.f"])
    else:
        E.relogio(c, t, C["s07.a"], cx=1400, cy=500, r=200)


def b_resposta2(c, t, C, b):
    q2(c, t, C["s08"], ("4 Ω", "12 Ω", "6 Ω"), C["s08"], C["s08"], C["s09.e"], C["s09.b"])

    def s08():
        E.formula_em(c, t, C["s08.a"], "72 ÷ 18 = 4 Ω", XE, 300, 76, "g", TINTA)
        E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: E.escreve(c, "12 e 6 em paralelo", XE, 370, 46, "i", TINTA2, a))
        fi_em(c, t, C["s08.b"], "R_{eq} = 4 + 4 = 8 Ω", XE, 520, 76, "g", TINTA)
        E.formula_em(c, t, C["s08.c"], "i = 24 ÷ 8", XE, 700, 76, "g", TINTA)
        bola_txt(c, t, C["s08.c"] + 0.8, "3 A", 700, 680, 90, 64)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.formula_em(c, t, C["s09.a"], "V: 4 × 3 = 12 V", XE, 300, 76, "g", TINTA)
    E.formula_em(c, t, C["s09.c"], "paralelo: 24 − 12 = 12 V", XE, 450, 64, "g", TINTA2)
    E.formula_em(c, t, C["s09.d"], "A: 12 ÷ 6 = 2 A", XE, 600, 76, "g", TINTA)
    E.formula_em(c, t, C["s09.f"], "12 ÷ 12 = 1 A;  2 + 1 = 3", XE, 760, 60, "g", CERTO)


# ---------------- questão 3: o curto ----------------
Q3 = (900, 440, 1760, 820)


def b_questao3(c, t, C, b):
    E.frase(c, t, C["s10.a"], [("questão", "i", 80), ("3", "g", 80, COR)], XE, 200, passo=0.12)
    E.frase(c, t, C["s10.b"], ps("três de", "i", 62) + [("10", "g", 60), ("Ω", "g", 46, F.UNID)] + ps("em série", "g", 58), XE, 360, passo=0.1)
    E.foco(c, t, C["s10.b"] + 1.2, 0.5, lambda a: F.medida(c, 30, "V", XE, 470, 76, COR, a))
    E.frase(c, t, C["s10.c"], ps("um fio nas pontas de um", "i", 58, ERRADO), XE, 620, passo=0.1)
    E.frase(c, t, C["s10.d"], ps("e a corrente?", "g", 64, COR), XE, 780, passo=0.1)
    if t < C["s11"]:
        x0, y0, x1, y1 = Q3
        ab = malha(c, t, C["s10.b"], x0, y0, x1, y1, [("R", "10 Ω", C["s10.b"]), ("R", "10 Ω", C["s10.b"] + 0.2), ("R", "10 Ω", C["s10.b"] + 0.4)], "30 V")
        curto(c, t, C["s10.c"], *ab[1], 130)
    else:
        E.relogio(c, t, C["s11.a"], cx=1400, cy=500, r=200)


def b_resposta3(c, t, C, b):
    x0, y0, x1, y1 = Q3
    ab = malha(c, t, C["s12"], x0, y0, x1, y1, [("R", "10 Ω", C["s12"]), ("R", "10 Ω", C["s12"]), ("R", "10 Ω", C["s12"])], "30 V")
    curto(c, t, C["s12"], *ab[1], 130)
    apaga(c, t, C["s12.c"], *ab[1], 180)
    F.corrente(c, t, C["s12.a"], volta(x0, y0, x1, y1), vel=90 if t < C["s12.e"] else 150)
    troca(c, t, [(C["s12.a"], "1 A"), (C["s12.e"], "1,5 A")], lambda s, a: E.pilula(c, s, (x0 + x1) / 2, y0 - 180, 50, "g", fundo=E.COR, a=a))
    E.formula_em(c, t, C["s12.a"], "antes: 30 ÷ 30 = 1 A", XE, 330, 66, "g", TINTA2)
    E.frase(c, t, C["s12.b"], ps("o do meio fica em curto:", "i", 54), XE, 470, passo=0.1)
    E.frase(c, t, C["s12.c"], [("sai", "g", 60, ERRADO), ("do", "i", 62), ("circuito", "i", 62)], XE, 560, passo=0.12)
    E.formula_em(c, t, C["s12.d"], "30 ÷ 20 =", XE, 720, 80, "g", TINTA)
    bola_txt(c, t, C["s12.e"], "1,5 A", 620, 695, 90, 54, CERTO)
    E.formula_em(c, t, C["s12.f"], "1 A → 1,5 A", XE, 900, 76, "g", COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho que mais salva tempo:", "i", 70, CLARO), W / 2, 200, "center", 0.1)
    E.frase(c, t, C["s13.a"], [("estime", "g", 110, BR)], W / 2, 360, "center")
    fi_em(c, t, C["s13.b"], "série:  R_{eq} > o maior", W / 2, 540, 84, "g", BR, "center")
    fi_em(c, t, C["s13.c"], "paralelo:  R_{eq} < o menor", W / 2, 690, 84, "g", CLARO, "center")
    E.frase(c, t, C["s13.d"], ps("fora disso? há um erro", "i", 62, CLARO), W / 2, 860, "center", 0.1)
    E.frase(c, t, C["s13.e"], ps("e alternativas caem sem conta", "g", 58, BR), W / 2, 970, "center", 0.1)


# ---------------- questão 4: a ponte ----------------
PCX, PCY, PRX, PRY = 1520, 560, 250, 270


def b_questao4(c, t, C, b):
    E.frase(c, t, C["s14.a"], [("questão", "i", 80), ("4", "g", 80, COR)], XE, 200, passo=0.12)
    E.frase(c, t, C["s14.b"], [("G", "g", 62, COR), ("=", "g", 62, TINTA2), ("0", "g", 62, COR)], XE, 340, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("um lado:", "i", 58) + [("5", "g", 56), ("e", "i", 58), ("10", "g", 56), ("Ω", "g", 44, F.UNID)], XE, 470, passo=0.1)
    E.frase(c, t, C["s14.d"], ps("outro:", "i", 58) + [("15", "g", 56), ("Ω", "g", 44, F.UNID), ("e", "i", 58), ("Rx", "g", 56, COR)], XE, 570, passo=0.1)
    E.frase(c, t, C["s14.e"], [("Rx", "g", 80, COR), ("=", "g", 80, TINTA2), ("?", "g", 80, COR)], XE, 760, passo=0.12)
    if t < C["s15"]:
        ponte(c, t, C["s14.b"], PCX, PCY, PRX, PRY, ["5 Ω" if t >= C["s14.c"] else None, "10 Ω" if t >= C["s14.c"] else None,
                                                    "15 Ω" if t >= C["s14.d"] else None, "Rx" if t >= C["s14.d"] else None], tg=C["s14.b"])
    else:
        E.relogio(c, t, C["s15.a"], cx=1400, cy=500, r=200)


def b_resposta4(c, t, C, b):
    cores = [E.COR, F.NEG, F.NEG, E.COR] if t >= C["s16.b"] else None
    ponte(c, t, C["s16"], PCX, PCY, PRX, PRY, ["5 Ω", "10 Ω", "15 Ω", "Rx" if t < C["s16.d"] else "30 Ω"], cores=cores, tg=C["s16"])
    E.frase(c, t, C["s16.a"], ps("G em zero:", "i", 58) + [("equilíbrio", "g", 56)], XE, 260, passo=0.1)
    E.frase(c, t, C["s16.b"], ps("opostos:", "i", 58) + [("5", "g", 56, COR), ("e", "i", 58), ("Rx,", "g", 56, COR), ("10", "g", 56, F.NEG), ("e", "i", 58),
                                                         ("15", "g", 56, F.NEG)], XE, 370, passo=0.1)
    E.formula_em(c, t, C["s16.c"], "5 · Rx = 10 · 15 = 150", XE, 520, 72, "g", TINTA)
    bola_txt(c, t, C["s16.d"], "30 Ω", XE + 180, 720, 110, 64, CERTO)
    fi_em(c, t, C["s16.e"], "f{5}{10} = f{15}{30}", XE, 940, 72, "g", TINTA)


# ---------------- questão 5: a casa ----------------
HX0, HY0, HY1, HXS = 920, 440, 820, [1300, 1660]


def casa2(c, t, t0, aberta, ligados, um=None, rot=True):
    """rede de 220 V, disjuntor no fio de cima e dois aquecedores de 22 Ω em paralelo"""
    F.fio(c, t, t0, [(HX0, HY0), (1000, HY0)], 0.3)
    F.chave(c, t, t0, (1000, HY0), (1180, HY0), fechada=1 - aberta, rotulo="15 A" if rot else None)
    F.fio(c, t, t0, [(1180, HY0), (HXS[-1], HY0)], 0.5)
    F.fio(c, t, t0, [(HX0, HY1), (HXS[-1], HY1)], 0.5)
    E.foco(c, t, t0, 0.4, lambda a: (E.pilula(c, "220 V", HX0, (HY0 + HY1) / 2, 42, "g", fundo=TINTA, a=a),
                                     M.line(c, HX0, HY0, HX0, (HY0 + HY1) / 2 - 40, TINTA, a, 6),
                                     M.line(c, HX0, (HY0 + HY1) / 2 + 40, HX0, HY1, TINTA, a, 6)))
    for k, x in enumerate(HXS):
        F.resistor(c, t, t0 + 0.2 * k, (x, HY0), (x, HY1), "22 Ω")
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: (F.no(c, (HXS[0], HY0), a), F.no(c, (HXS[0], HY1), a)))
    if ligados is not None and aberta < 0.5:
        F.corrente(c, t, ligados, [(HX0, HY0), (HXS[-1], HY0)], fecha=False)
        for k, x in enumerate(HXS):
            if um is None or k == 0:
                F.corrente(c, t, ligados, [(x, HY0), (x, HY1)], fecha=False)


def b_questao5(c, t, C, b):
    E.frase(c, t, C["s17.a"], [("questão", "i", 80), ("5", "g", 80, COR)] + ps("a casa", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: F.medida(c, 220, "V", XE, 340, 84, COR, a))
    E.frase(c, t, C["s17.c"], ps("disjuntor de", "i", 58) + [("15", "g", 56), ("A", "g", 44, F.UNID)], XE, 470, passo=0.1)
    E.frase(c, t, C["s17.d"], ps("2 aquecedores de", "i", 58) + [("22", "g", 56), ("Ω", "g", 44, F.UNID)], XE, 580, passo=0.1)
    E.frase(c, t, C["s17.d"] + 1.2, ps("em paralelo", "g", 56), XE, 670, passo=0.1)
    E.frase(c, t, C["s17.e"], ps("o disjuntor desarma?", "g", 62, COR), XE, 830, passo=0.1)
    if t < C["s18"]:
        casa2(c, t, C["s17.b"], 0, None)
    else:
        E.relogio(c, t, C["s18.a"], cx=1400, cy=500, r=200)


def b_resposta5(c, t, C, b):
    aberta = ease_io(prog(t, C["s19.e"] + 0.3, 0.4))
    casa2(c, t, C["s19"], aberta, C["s19.c"], um=(None if t >= C["s19.d"] else 0))
    for k in range(2):
        tag(c, t, C["s19.a"] + 0.2 * k, "220 V", HXS[k] - 110, (HY0 + HY1) / 2 + 60, 40)
    tag(c, t, C["s19.b"], "10 A", HXS[0] - 110, (HY0 + HY1) / 2 - 30, 44, E.COR, "g")
    tag(c, t, C["s19.d"], "10 A", HXS[1] - 110, (HY0 + HY1) / 2 - 30, 44, E.COR, "g")
    E.frase(c, t, C["s19.a"], ps("cada um com", "i", 58) + [("220", "g", 56), ("V", "g", 44, F.UNID)], XE, 280, passo=0.1)
    E.formula_em(c, t, C["s19.b"], "220 ÷ 22 = 10 A", XE, 420, 76, "g", TINTA)
    E.frase(c, t, C["s19.c"], ps("um só:", "i", 58) + [("10", "g", 56), ("A", "g", 44, F.UNID), ("aguenta", "g", 56, CERTO)], XE, 570, passo=0.1)
    E.formula_em(c, t, C["s19.d"], "10 + 10 = 20 A", XE, 720, 76, "g", TINTA)
    E.frase(c, t, C["s19.e"], [("20", "g", 70, ERRADO), (">", "g", 70, TINTA2), ("15:", "g", 70), ("desarma", "g", 70, ERRADO)], XE, 880, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", [("reduza", "g", 62), ("por", "i", 66), ("partes", "i", 66)]),
                 ("s20.b", [("corrente", "g", 62), ("total,", "i", 66), ("depois", "i", 66), ("volte", "g", 62, COR)]),
                 ("s20.c", [("fio", "i", 66), ("sem", "i", 66), ("resistor:", "i", 66), ("curto", "g", 62, ERRADO)]),
                 ("s20.d", [("ponte", "g", 62), ("em", "i", 66), ("equilíbrio:", "i", 66), ("produto", "g", 62, COR), ("cruzado", "g", 62, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 165
            numero(c, t, C[k], i + 1, 380, y - 24, 46)
            E.frase(c, t, C[k] + 0.1, partes, 470, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("potência", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s21.a"] + 0.5, [("elétrica", "g", 110, COR)], XE, 540)
    # o resistor que esquenta
    y = 760
    F.fio(c, t, C["s21.b"], [(260, y), (340, y)], 0.3)
    F.resistor(c, t, C["s21.b"], (340, y), (700, y))
    F.fio(c, t, C["s21.b"], [(700, y), (780, y)], 0.3)
    if t >= C["s21.b"] + 0.4:
        q = ep(t, C["s21.b"] + 0.4, 0.8)
        for k in range(3):
            x = 450 + 70 * k
            pts = [(x + 12 * math.sin(t * 3 + k + j * 0.9), y - 70 - 24 * j) for j in range(6)]
            F.poli(c, pts, 1.0, E.COR, q * 0.8, 6)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
