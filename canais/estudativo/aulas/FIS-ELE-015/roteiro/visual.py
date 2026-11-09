"""Visual — Estudativo · FIS-ELE-015: medidores e ponte de Wheatstone.

Segue a linguagem visual da Física (cabeçalho do visual.py da FIS-CIN-001) e a da Eletricidade (cabeçalho do visual.py da
FIS-ELE-001: circuito com F.fio, F.pilha, F.resistor; corrente = setinhas laranja; Ω e = só na fonte pesada).
Nesta aula: MEDIDOR = círculo branco com a letra laranja (A amperímetro, V voltímetro, G galvanômetro), peça `medidor`;
a leitura aparece numa pílula laranja ao lado dele. A PONTE é a peça `ponte` (losango: R1 em cima à esquerda, R2 embaixo
à esquerda, R3 em cima à direita, R4 embaixo à direita; G no meio; pilha à esquerda ligada ao vértice de cima e ao de
baixo). Os opostos ganham a mesma cor: R1 e R4 em laranja, R2 e R3 em azul (F.NEG).
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
ARQUIVO_FINAL = "estudativo_FIS-ELE-015_medidores_e_ponte_de_wheatstone.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("medidores", "erro", "ponte", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert 12 / (2 + 4) == 2 and 4 * 2 == 8
assert 8 * 3 / 2 == 12 and 2 * 12 == 8 * 3 == 24 and Fr(2, 8) == Fr(3, 12)
assert 2 + 8 == 10 and 3 + 12 == 15 and 10 * 15 == 150 and 10 + 15 == 25 and 150 / 25 == 6
assert 9 * 6 / 3 == 18 and 3 * 18 == 9 * 6 == 54 and Fr(3, 9) == Fr(6, 18) == Fr(1, 3)


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


def medidor(c, cx, cy, r, s, a=1.0, escuro=False, cor=None):
    """medidor: círculo com a letra (A, V ou G)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR if not escuro else "#14141C", a))
    c.drawCircle(cx, cy, r, M.paint(cor or (TINTA if not escuro else BR), a, stroke=6))
    E._meio(c, s, cx, cy, r * 1.0, "g", E.COR if not escuro else E.CLARO, a)


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: medidor(c, 1250, 420, 130, "A", a))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: medidor(c, 1600, 420, 130, "V", a))
        if t >= C["s01.b"]:
            q = ep(t, C["s01.b"], 0.3)
            for k in range(3):
                ang = -0.6 + 0.6 * k
                M.line(c, 1250 + math.sin(ang) * 150, 260 - math.cos(ang) * 10, 1250 + math.sin(ang) * 210, 230 - math.cos(ang) * 60, ERRADO, q, 10)
            E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "queima", 1250, 640, 50, "g", fundo=ERRADO, a=a))
        E.foco(c, t, C["s01.d"], 0.4, lambda a: E.pilula(c, "i ≈ 0", 1600, 640, 50, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s01.a"], [("amperímetro", "g", 76), ("errado:", "i", 80)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("pode queimar", "g", 66, ERRADO), XE, 400, passo=0.1)
        E.frase(c, t, C["s01.c"], [("voltímetro", "g", 76), ("errado:", "i", 80)], XE, 600, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("o circuito para", "g", 66, ERRADO), XE, 700, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate((("s02.a", "ligar os medidores", 1.2), ("s02.b", "a multiplicação cruzada", 0))):
        y = 480 + i * 170
        numero(c, t, C[k] + dt, i + 1, XE + 40, y - 30, 38)
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 74, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "em série, a corrente é a mesma;", "a tensão se divide", None),
                              ("s03.c", "em paralelo, a tensão é a mesma;", "menor R, maior corrente", None)))


# ---------------- medidores ----------------
MX0, MY0, MX1, MY1 = 1110, 470, 1760, 860
RA, RB = (1190, 1380), (1440, 1630)


def circuito_medidores(c, t, t0, ta, tv, rot=False, tr=None):
    """pilha, dois resistores no fio de cima, o amperímetro no lado direito (em série) e o voltímetro sobre o 2º resistor"""
    ym = (MY0 + MY1) / 2
    F.pilha(c, t, t0, (MX0, MY1), (MX0, MY0), "12 V" if rot and t >= tr else None, lado=-1)
    F.fio(c, t, t0, [(MX0, MY0), (RA[0], MY0)], 0.4)
    F.resistor(c, t, t0 + 0.1, (RA[0], MY0), (RA[1], MY0))
    F.fio(c, t, t0 + 0.1, [(RA[1], MY0), (RB[0], MY0)], 0.3)
    F.resistor(c, t, t0 + 0.2, (RB[0], MY0), (RB[1], MY0))
    F.fio(c, t, t0 + 0.2, [(RB[1], MY0), (MX1, MY0), (MX1, ym - 70)], 0.4)
    F.fio(c, t, t0 + 0.2, [(MX1, ym + 70), (MX1, MY1), (MX0, MY1)], 0.5)
    if t < ta:
        F.fio(c, t, t0 + 0.2, [(MX1, ym - 70), (MX1, ym + 70)], 0.3)
    E.foco(c, t, ta, 0.5, lambda a: medidor(c, MX1, ym, 70, "A", a))
    if t >= tv:
        yv = MY0 - 190
        F.fio(c, t, tv, [(RB[0], MY0), (RB[0], yv), ((RB[0] + RB[1]) / 2 - 60, yv)], 0.5)
        F.fio(c, t, tv, [(RB[1], MY0), (RB[1], yv), ((RB[0] + RB[1]) / 2 + 60, yv)], 0.5)
        E.foco(c, t, tv + 0.3, 0.5, lambda a: medidor(c, (RB[0] + RB[1]) / 2, yv, 60, "V", a))
        E.foco(c, t, tv + 0.3, 0.4, lambda a: (F.no(c, (RB[0], MY0), a), F.no(c, (RB[1], MY0), a)))
    if rot and t >= tr:
        E.foco(c, t, tr, 0.4, lambda a: (E._cola(c, "2 Ω", (RA[0] + RA[1]) / 2, MY0, 0, 1, 50, 46, "b", TINTA, a),
                                         E._cola(c, "4 Ω", (RB[0] + RB[1]) / 2, MY0, 0, 1, 50, 46, "b", TINTA, a)))


def b_medidores(c, t, C, b):
    ym = (MY0 + MY1) / 2
    circuito_medidores(c, t, C["s04"], C["s04.c"], C["s05.b"], True, C["s06.c"])
    F.corrente(c, t, C["s04.b"], [(MX0, MY0), (MX1, MY0), (MX1, MY1), (MX0, MY1)])
    E.frase(c, t, C["s04.a"], [("amperímetro", "g", 66, COR), ("mede", "i", 70), ("a", "i", 70), ("corrente", "g", 66)], XE, 220, passo=0.12)
    E.frase(c, t, C["s04.c"], [("em", "i", 62), ("série:", "g", 60), ("no", "i", 62), ("caminho", "i", 62)], XE, 320, passo=0.12)
    E.frase(c, t, C["s04.d"], [("ideal:", "i", 56, TINTA2), ("R", "g", 54), ("=", "g", 54, TINTA2), ("0", "g", 54, COR)], XE, 410, passo=0.12)
    E.frase(c, t, C["s05.a"], [("voltímetro", "g", 66, COR), ("mede", "i", 70), ("a", "i", 70), ("tensão", "g", 66)], XE, 560, passo=0.12)
    E.frase(c, t, C["s05.b"], [("em", "i", 62), ("paralelo:", "g", 56), ("uma", "i", 58), ("ponta", "i", 58), ("de", "i", 58), ("cada", "i", 58),
                               ("lado", "i", 58)], XE, 660, passo=0.1)
    E.frase(c, t, C["s05.d"], [("ideal:", "i", 56, TINTA2), ("R", "g", 54), ("enorme", "g", 54, COR)], XE, 750, passo=0.12)
    E.frase(c, t, C["s06.a"], [("A:", "g", 54, COR)] + ps("catraca no caminho", "i", 56), XE, 880, passo=0.1)
    E.frase(c, t, C["s06.b"], [("V:", "g", 54, COR)] + ps("régua por fora", "i", 56), XE, 970, passo=0.1)
    tag(c, t, C["s06.d"], "2 A", MX1 + 0, ym + 130, 46, E.COR, "g")
    tag(c, t, C["s06.e"], "8 V", (RB[0] + RB[1]) / 2 - 150, MY0 - 190, 46, E.COR, "g")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s07"], [("cuidado:", "g", 90, ERRADO)] + ps("trocar as ligações", "i", 80), XE, 200, passo=0.14)
    # amperímetro em paralelo
    x0, y0, x1, y1 = 200, 460, 840, 820
    F.pilha(c, t, C["s07.b"], (x0, y1), (x0, y0))
    F.fio(c, t, C["s07.b"], [(x0, y0), (360, y0)], 0.3)
    F.resistor(c, t, C["s07.b"], (360, y0), (680, y0))
    F.fio(c, t, C["s07.b"], [(680, y0), (x1, y0), (x1, y1), (x0, y1)], 0.5)
    F.fio(c, t, C["s07.b"] + 0.3, [(360, y0), (360, y0 + 150), (460, y0 + 150)], 0.4, cor=ERRADO)
    F.fio(c, t, C["s07.b"] + 0.3, [(680, y0), (680, y0 + 150), (580, y0 + 150)], 0.4, cor=ERRADO)
    E.foco(c, t, C["s07.b"] + 0.5, 0.4, lambda a: medidor(c, 520, y0 + 150, 58, "A", a, cor=ERRADO))
    F.corrente(c, t, C["s07.c"], [(x0, y0), (360, y0), (360, y0 + 150), (680, y0 + 150), (680, y0), (x1, y0), (x1, y1), (x0, y1)], vel=260, espaco=80)
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "queima", 520, y1 + 90, 50, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s07.b"], [("A", "g", 60, COR), ("em", "i", 62), ("paralelo", "g", 58, ERRADO)], x0, 380, passo=0.12)
    # voltímetro em série
    x0, x1 = 1080, 1720
    F.pilha(c, t, C["s08.a"], (x0, y1), (x0, y0))
    F.fio(c, t, C["s08.a"], [(x0, y0), (1180, y0)], 0.3)
    F.resistor(c, t, C["s08.a"], (1180, y0), (1440, y0))
    F.fio(c, t, C["s08.a"], [(1440, y0), (x1, y0), (x1, (y0 + y1) / 2 - 60)], 0.4)
    F.fio(c, t, C["s08.a"], [(x1, (y0 + y1) / 2 + 60), (x1, y1), (x0, y1)], 0.4)
    E.foco(c, t, C["s08.a"] + 0.3, 0.4, lambda a: medidor(c, x1, (y0 + y1) / 2, 58, "V", a, cor=ERRADO))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "i ≈ 0: o circuito para", 1400, y1 + 90, 46, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s08.a"], [("V", "g", 60, COR), ("em", "i", 62), ("série", "g", 58, ERRADO)], x0, 380, passo=0.12)


# ---------------- ponte ----------------
PCX, PCY, PRX, PRY = 1520, 560, 250, 270


def b_ponte(c, t, C, b):
    E.frase(c, t, C["s09"], ps("a ponte de", "i", 76) + [("Wheatstone", "g", 72, COR)], XE, 200, passo=0.12)
    if t < C["s12"]:
        cores = None
        if t >= C["s10.c"]:
            cores = [E.COR, F.NEG, F.NEG, E.COR]
        ponte(c, t, C["s09.a"], PCX, PCY, PRX, PRY, ["R₁", "R₂", "R₃", "R₄"], tg=C["s09.e"], cores=cores)
        if t >= C["s09.b"]:
            q = 0.5 + 0.5 * math.sin(t * 5)
            for P in ((PCX, PCY - PRY), (PCX, PCY + PRY)):
                c.drawCircle(*P, 26 + 6 * q, M.paint(E.COR, ep(t, C["s09.b"], 0.4) * (1 - ep(t, C["s09.c"], 0.4)), stroke=5))
        E.frase(c, t, C["s09.a"], ps("4 resistores num", "i", 58) + [("losango", "g", 56)], XE, 330, passo=0.1)
        E.frase(c, t, C["s09.e"], [("G:", "g", 56, COR)] + ps("o galvanômetro, no meio", "i", 56), XE, 430, passo=0.1)
        if C["s10"] <= t:
            E.frase(c, t, C["s10.a"], [("G", "g", 64, COR), ("=", "g", 64, TINTA2), ("0", "g", 64, COR), ("→", "g", 64, TINTA2), ("equilíbrio", "g", 60)], XE, 540, passo=0.12)
            fi_em(c, t, C["s10.d"], "R_1 · R_4 = R_2 · R_3", XE, 650, 76, "g", TINTA)
            E.frase(c, t, C["s10.c"], ps("opostos, na diagonal", "i", 52, TINTA2), XE, 730, passo=0.1)
        if t >= C["s11"]:
            def s11():
                E.frase(c, t, C["s11.a"], ps("sem corrente no meio,", "i", 50, TINTA2), XE, 840, passo=0.08)
                E.frase(c, t, C["s11.b"], [("U", "g", 48), ("=", "g", 48, TINTA2), ("0", "g", 48, COR)] + ps("nas pontas do G:", "i", 50, TINTA2), XE, 910, passo=0.08)
                fi_em(c, t, C["s11.d"], "f{R_1}{R_2} = f{R_3}{R_4}", XE + 60, 1010, 60, "g", COR)
            s11()
        return
    # s12: exemplo
    ponte(c, t, C["s12"], PCX, PCY, PRX, PRY, ["2 Ω", "8 Ω", "3 Ω", "R₄ = ?" if t < C["s12.f"] else "12 Ω"],
          cores=[E.COR, F.NEG, F.NEG, E.COR], tg=C["s12"])
    E.formula_em(c, t, C["s12.e"], "2 · R₄ = 8 · 3", XE, 450, 84, "g", TINTA)
    E.formula_em(c, t, C["s12.e"] + 1.2, "2 · R₄ = 24", XE, 600, 84, "g", TINTA)
    bola_txt(c, t, C["s12.f"], "12 Ω", XE + 180, 800, 120, 70, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    cx, cy = 1530, 600
    g = t < C["s13.a"] + 0.6
    ponte(c, t, C["s13"], cx, cy, 250, 250, ["2 Ω", "8 Ω", "3 Ω", "12 Ω"], g=False, escuro=True)
    if g:
        E.saida(c, t, C["s13.a"] + 0.2, lambda: (M.line(c, cx - 250, cy, cx + 250, cy, BR, 1.0, 6), medidor(c, cx, cy, 56, "G", 1.0, True)))
    else:
        E.foco(c, t, C["s13.a"] + 0.6, 0.4, lambda a: E.pilula(c, "meio apagado", cx, cy, 40, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s13"], ps("o atalho:", "i", 72, CLARO), XE, 200)
    E.frase(c, t, C["s13.a"], ps("equilíbrio?", "i", 62, CLARO) + [("apague", "g", 60, BR), ("o", "g", 60, BR), ("meio", "g", 60, BR)], XE, 310, passo=0.12)
    E.frase(c, t, C["s13.b"], ps("galvanômetro, resistor ou nada:", "i", 50, CLARO) + [("tanto", "g", 48, BR), ("faz", "g", 48, BR)], XE, 400, passo=0.08)
    E.frase(c, t, C["s13.c"], ps("2 lados em série, em paralelo", "g", 52, BR), XE, 520, passo=0.08)
    E.formula_em(c, t, C["s13.d"], "2 + 8 = 10    3 + 12 = 15", XE, 640, 60, "g", CLARO)
    fi_em(c, t, C["s13.e"], "f{10 · 15}{10 + 15} = f{150}{25}", XE, 800, 70, "g", BR)
    bola_txt(c, t, C["s13.e"] + 1.2, "6 Ω", XE + 560, 780, 80, 58)
    E.frase(c, t, C["s14.a"], ps("antes, confira o", "i", 54, CLARO) + [("produto", "g", 52, BR), ("cruzado", "g", 52, BR)], XE, 960, passo=0.1)
    E.frase(c, t, C["s14.b"], [("não", "g", 50, ERRADO), ("fechou?", "i", 54, CLARO)] + ps("o meio fica", "i", 54, CLARO), XE, 1040, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15"] + 0.5, ps("ponte em equilíbrio", "i", 60, TINTA2), XE, 300)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: fi(c, "R_1 = 3 Ω", XE, 450, 76, "g", TINTA, a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: fi(c, "R_2 = 9 Ω", XE, 570, 76, "g", TINTA, a))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: fi(c, "R_3 = 6 Ω", XE, 690, 76, "g", TINTA, a))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: fi(c, "R_4 = ?", XE, 830, 90, "g", COR, a))
    if t < C["s16"]:
        ponte(c, t, C["s15.a"], PCX, PCY, PRX, PRY, ["3 Ω", "9 Ω", "6 Ω", "?"], tg=C["s15.a"])
    else:
        E.relogio(c, t, C["s16.a"], cx=1400, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ponte(c, t, C["s17"], PCX, PCY, PRX, PRY, ["3 Ω", "9 Ω", "6 Ω", "?" if t < C["s17.c"] else "18 Ω"], cores=[E.COR, F.NEG, F.NEG, E.COR], tg=C["s17"])
    E.frase(c, t, C["s17.a"], ps("opostos:", "i", 58) + [("R1", "g", 56, COR), ("e", "i", 58), ("R4,", "g", 56, COR), ("R2", "g", 56, F.NEG), ("e", "i", 58),
                                                         ("R3", "g", 56, F.NEG)], XE, 280, passo=0.1)
    E.formula_em(c, t, C["s17.b"], "3 · R₄ = 9 · 6 = 54", XE, 450, 80, "g", TINTA)
    bola_txt(c, t, C["s17.c"], "18 Ω", XE + 180, 650, 110, 64, CERTO)
    fi_em(c, t, C["s17.d"], "f{3}{9} = f{6}{18}", XE, 900, 76, "g", TINTA)
    E.frase(c, t, C["s17.e"], ps("um terço dos dois lados", "i", 52, TINTA2), XE + 350, 890, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        E.foco(c, t, C["s18.a"], 0.5, lambda a: medidor(c, 360, 380, 60, "A", a))
        E.frase(c, t, C["s18.a"] + 0.1, [("em", "i", 66), ("série,", "g", 62), ("R", "g", 62), ("≈", "g", 62, TINTA2), ("0", "g", 62, COR)], 460, 404, passo=0.1)
        E.foco(c, t, C["s18.b"], 0.5, lambda a: medidor(c, 360, 560, 60, "V", a))
        E.frase(c, t, C["s18.b"] + 0.1, [("em", "i", 66), ("paralelo,", "g", 62), ("R", "g", 62), ("enorme", "g", 62, COR)], 460, 584, passo=0.1)
        E.foco(c, t, C["s18.c"], 0.5, lambda a: medidor(c, 360, 740, 60, "G", a))
        fi_em(c, t, C["s18.c"] + 0.1, "= 0:  R_1 · R_4 = R_2 · R_3", 460, 764, 62, "g", TINTA)
        E.frase(c, t, C["s18.c"] + 1.0, ps("e o meio pode ser apagado", "i", 56, TINTA2), 460, 870, passo=0.1)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("praticar", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s19.a"] + 0.5, [("o", "i", 110), ("módulo", "g", 110, COR)], XE, 540)
    for i, s in enumerate(("fio", "série", "paralelo", "misto", "curto", "medidores")):
        x, y = XE + 20 + (i % 3) * 260, 700 + (i // 3) * 110
        E.foco(c, t, C["s19.b"] + 0.25 * i, 0.4, lambda a, s=s, x=x, y=y: E.pilula(c, s, x + 110, y, 42, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, medidores=b_medidores, erro=b_erro, ponte=b_ponte, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
