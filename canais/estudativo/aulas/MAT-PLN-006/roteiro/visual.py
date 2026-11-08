"""Visual — Estudativo · MAT-PLN-006: relações de Girard.
x³ − 6x² + 11x − 6 = 0 nasce de (x − 1)(x − 2)(x − 3): soma 6, duas a duas 11, produto 6; as fórmulas com a, b, c, d e os sinais
troca, mantém, troca; com a ≠ 1 (2x³ − 3x² − 11x + 6: soma 3/2, produto −3); o erro de não trocar o sinal do produto; no palco,
uma raiz conhecida mais Girard dá as outras de cabeça.
Convenções da trilha em MAT-PLN-001; raízes em esferas verdes (MAT-PLN-004). Nova: COEFICIENTES do grau três em cores fixas,
a na cor da matéria, b magenta, c âmbar, d verde-petróleo (as cores de a, b, c são as da trilha de equação do 2º grau).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-006_relacoes_de_girard.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "regra", "erro", "atalho", "questao", "fim"))
CA, CB, CC, CD = E.COR, "#C2187A", "#B86E00", "#0B7A6B"


def _mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


# as contas da aula
assert _mul(_mul([1, -1], [1, -2]), [1, -3]) == [1, -6, 11, -6] and 1 + 2 + 3 == 6 == 1 * 2 * 3 and 1 * 2 + 1 * 3 + 2 * 3 == 11
_r = [Fr(3), Fr(-2), Fr(1, 2)]
assert [2 * k for k in _mul(_mul([1, -3], [1, 2]), [1, Fr(-1, 2)])] == [2, -3, -11, 6]
assert sum(_r) == Fr(3, 2) == Fr(3, 2) and _r[0] * _r[1] * _r[2] == -3 == Fr(-6, 2)
assert _mul(_mul([1, 1], [1, -2]), [1, -3]) == [1, -4, 1, 6] and -1 + 2 + 3 == 4 and -1 * 2 * 3 == -6
assert 6 - 1 == 5 and 2 + 3 == 5 and 2 * 3 == 6


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta trilha (as mesmas em MAT-PLN-001 a 010) ----------------
# POLINÔMIO: fórmula na grotesca pesada; o que está em jogo na cor da matéria; certo em verde, errado em vermelho.
# DESTAQUE: retângulo claro atrás do trecho (realce). IDÊNTICO: três barras desenhadas (a fonte não tem o ≡).
BR = "#FFFFFF"
AM = "#FFD500"


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def entre(t0, t1, f):
    """instante na fração f do trecho entre dois marcadores: fala sem marcador própria"""
    return t0 + (t1 - t0) * f


def fw(s, size):
    """largura de uma fórmula (o ≡ ocupa o mesmo que um =)"""
    return E.formula(None, s.replace("≡", "="), 0, 0, size, a=0) if s else 0.0


def ident(c, cx, y, size, cor, a):
    """sinal de idêntico: três barras, centradas em cx, na altura do = da fórmula de linha de base y"""
    w, h, gap = size * 0.5, max(4, size * 0.065), size * 0.17
    for k in (-1, 0, 1):
        M.rrect(c, cx - w / 2, y - size * 0.33 + k * gap - h / 2, w, h, h / 2, cor, a)


def formula(c, s, x, y, size, cor=None, a=1.0, align="left"):
    """E.formula que aceita o ≡"""
    if a <= 0:
        return
    if "≡" not in s:
        E.formula(c, s, x, y, size, "g", cor, a, align)
        return
    xi = x - fw(s, size) / 2 if align == "center" else x - fw(s, size) if align == "right" else x
    esq, dir_ = s.split("≡", 1)
    E.formula(c, esq, xi, y, size, "g", cor, a)
    xm = xi + fw(esq, size)
    ident(c, xm + fw("=", size) / 2, y, size, cor or TINTA, a)
    E.formula(c, dir_, xm + fw("=", size), y, size, "g", cor, a)


def form(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: formula(c, s, x, y, size, cor, a, align))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def trecho_x(s, trecho, x, size, align="left", n=0):
    """(x inicial, largura) de um trecho da fórmula s"""
    xi = x - fw(s, size) / 2 if align == "center" else x - fw(s, size) if align == "right" else x
    i0 = -1
    for _ in range(n + 1):
        i0 = s.find(trecho, i0 + 1)
    assert i0 >= 0, (s, trecho)
    return xi + fw(s[:i0], size), fw(trecho, size) - size * 0.02


def realce(c, t, t0, s, trecho, x, y, size, cor=None, align="left", n=0, t1=None):
    a = ep(t, t0, 0.35) * (1 - ep(t, t1, 0.3) if t1 else 1)
    if a <= 0:
        return
    x0, w = trecho_x(s, trecho, x, size, align, n)
    pad = min(size * 0.14, 16)
    M.rrect(c, x0 - pad, y - size * 0.95, w + pad * 2, size * 1.25, size * 0.2, cor or COR, 0.16 * a)


def monta(c, t, pecas, x, y, size, align="left", cor=None):
    """fórmula que entra em pedaços: pecas = [(texto, t0[, cor]), ...]"""
    total = fw("".join(p[0] for p in pecas), size)
    x0 = x - total / 2 if align == "center" else x
    acc = ""
    for p in pecas:
        s, t0, cp = p[0], p[1], (p[2] if len(p) > 2 else cor)
        xo = x0 + fw(acc, size)
        E.foco(c, t, t0, 0.4, lambda a, s=s, xo=xo, cp=cp: formula(c, s, xo, y, size, cp, a))
        acc += s
    return x0


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def resp(c, t, t0, s, cx, cy, size, cor=CERTO, r=None):
    """resposta na esfera: fórmula branca sobre a bola"""
    r = r or max(fw(s, size) / 2 + size * 0.45, size * 0.95)
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), formula(c, s, cx, cy + size * 0.36, size, BR, a, "center")))


def pil(c, t, t0, s, cx, cy, size=50, fundo=None, cor=BR, estilo="g"):
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, cx, cy, size, estilo=estilo, fundo=fundo or E.COR, cor=cor, a=a), sobe=8)


def nota(c, t, t0, s, x, y, size=52, cor=None, est="i", align="left"):
    """texto de apoio parado que entra com foco"""
    if align == "center":
        E.foco(c, t, t0, 0.45, lambda p: centro(c, s, x, y, size, est, cor or TINTA2, p))
    else:
        E.foco(c, t, t0, 0.45, lambda p: E.escreve(c, s, x, y, size, est, cor or TINTA2, p))


def selo_em(c, t, t0, cx, cy, r, ok=True):
    E.foco(c, t, t0, 0.45, lambda p: E.selo(c, cx, cy, r, ok, p))


def flecha(c, t, t0, x0, y0, x1, y1, alto, cor, d=0.6, largura=6):
    """arco de (x0, y0) a (x1, y1) com ponta de seta; alto > 0 sobe, alto < 0 desce"""
    p = ep(t, t0, d)
    if p <= 0:
        return
    cx = (x0 + x1) / 2
    cy = (min(y0, y1) - alto) if alto > 0 else (max(y0, y1) - alto)
    pt = lambda u: ((1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u * u * x1, (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u * u * y1)
    n = max(2, int(30 * p))
    path = skia.Path()
    path.moveTo(*pt(0))
    for i in range(1, n + 1):
        path.lineTo(*pt(p * i / n))
    c.drawPath(path, M.paint(cor, 1.0, stroke=largura, cap_round=True))
    if p > 0.97:
        ang = math.atan2(y1 - cy, x1 - cx)
        for da in (2.6, -2.6):
            M.line(c, x1, y1, x1 + 24 * math.cos(ang + da), y1 + 24 * math.sin(ang + da), cor, 1.0, largura)


def gancho_fim(c, t, t0, tb, linhas, cx=1450, cy=520):
    """a promessa do gancho, no modelo do piloto: linhas à esquerda e a esfera com "+ atalho de prova" em tb"""
    if tb is not None:
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, cx, cy, 300 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", cx, cy - 15, 84, "g", BR, a),
                                              centro(c, "de prova", cx, cy + 70, 84, "i", BR, a)))
    E.frase(c, t, t0, ps("até o fim da aula", "i", 96), XE, 380)
    for k, (partes, dt) in enumerate(linhas):
        E.frase(c, t, t0 + dt, partes, XE, 530 + k * 140, passo=0.12)


def lembrete(c, t, C, sid, itens, x_f=1060):
    """lembrete numerado: itens = [(cue, partes do texto, fórmula de exemplo ou None)]"""
    E.frase(c, t, C[sid] + 0.2, ps("você vai usar", "i", 84), XE, 190)
    n = len(itens)
    y0, dy = (350, 230) if n == 3 else (380, 300) if n == 2 else (330, 170)
    for k, (tk, partes, fx) in enumerate(itens):
        y = y0 + k * dy
        E.foco(c, t, tk, 0.45, lambda p, k=k, y=y: num_bola(c, str(k + 1), XE + 40, y - 22, 42, 52, p))
        E.frase(c, t, tk, partes, XE + 120, y, passo=0.08)
        if fx:
            form(c, t, tk + 0.6, fx, XE + 120, y + 100, 70, TINTA2)
    nota(c, t, C[sid + ".end"] - 2.4, "faltou alguma? procure no canal", XE, 1010, 50)


def fim_padrao(c, t, C, resumo_id, prox_id, itens, prox_l1, prox_big, extra=None, k_ins="d", k_bons="e"):
    """resumo numerado (itens = [(cue, partes)]) e a ponte para a próxima aula com Inscreva-se"""
    def resumo():
        E.frase(c, t, C[resumo_id] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        for k, (tk, partes) in enumerate(itens):
            yy = 430 + k * 200
            E.foco(c, t, tk, 0.5, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), 230, yy - 30, 58, 66, p))
            E.frase(c, t, tk + 0.1, partes, 320, yy, passo=0.12)
    E.saida(c, t, C[prox_id] - 0.1, resumo)
    if t < C[prox_id]:
        return
    if prox_l1:
        E.frase(c, t, C[prox_id] + 0.2, ps(prox_l1, "i", 80), XE, 230, passo=0.1)
    E.frase(c, t, C[prox_id + ".a"], ps(prox_big, "g", 100, COR), XE, 390, passo=0.12)
    if extra:
        extra()
    ci = C[prox_id + "." + k_ins]
    E.foco(c, t, ci, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 640, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, ci + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(930, 685, p), ep(t, ci + 0.2, 0.4), TINTA)
    E.frase(c, t, C[prox_id + "." + k_bons], ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), W / 2, 960, "center")


def questao_ui(c, t, C, sid, pid, linhas, cx=1560, cy=470):
    """tela da questão: "hora de testar", linhas = [(t0, desenho(a) ou fórmula, y)], relógio de pausa na cena pid"""
    E.frase(c, t, C[sid] + 0.2, ps("hora de testar", "i", 72, COR), XE, 200)
    for t0, s, y, size in linhas:
        if callable(s):
            E.foco(c, t, t0, 0.5, s)
        else:
            form(c, t, t0, s, XE, y, size)
    E.relogio(c, t, C[pid + ".a"], cx, cy, 170)


def etiqueta(c, t, t0, n, rot=None):
    """etiqueta da questão (práticas): pílula "questão n" e o assunto em itálico ao lado"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"questão {n}", XE + 150, 150, 52, estilo="g", a=a), sobe=8)
    if rot:
        E.frase(c, t, t0 + 0.3, ps(rot, "i", 60, TINTA2), XE + 340, 168, passo=0.08)


def briot(c, t, raiz, coefs, tc, tb, x, y, cw=210, size=96, tr=None, cor=None, escuro=False, mostra_conta=True, falta=(), cor_resto=None):
    """dispositivo de Briot-Ruffini (convenção da trilha). raiz à esquerda da barra, coeficientes em cima, resultados embaixo.
    tc = entrada da raiz e dos coeficientes, ou (raiz, coeficientes); tb[i] = instante do i-ésimo resultado (tb[0] = baixa o primeiro).
    Antes de cada resultado, uma seta diagonal leva o anterior até a coluna seguinte com "× raiz" (mostra_conta).
    tr = destaque do resto (caixa). falta = índices de coeficientes zero que entram pintados (termo que falta).
    Refaz a conta: os resultados são calculados aqui."""
    tinta = BR if escuro else TINTA
    forte = cor or (CLARO if escuro else COR)
    t_r, t_c = tc if isinstance(tc, tuple) else (tc, tc)
    res = [coefs[0]]
    for k in coefs[1:]:
        res.append(res[-1] * raiz + k)
    xs = [x + cw * (i + 0.5) for i in range(len(coefs))]
    yb = y + size * 1.55
    a = ep(t, t_r, 0.5)
    if a > 0:
        M.line(c, x - 10, y - size * 0.95, x - 10, yb + size * 0.35, tinta, a, 6)
        M.line(c, x - 10, y + size * 0.45, x + cw * len(coefs), y + size * 0.45, tinta, a, 6)
    E.foco(c, t, t_r, 0.5, lambda q: formula(c, E._num(raiz), x - 50, y, size, forte, q, "right"))
    for i, k in enumerate(coefs):
        E.foco(c, t, t_c + 0.15 * i, 0.5, lambda q, i=i, k=k: formula(c, E._num(k), xs[i], y, size, "#B86E00" if i in falta and not escuro else AM if i in falta else tinta, q, "center"))
    for i, r in enumerate(res):
        if i > 0 and mostra_conta:
            p = ep(t, tb[i] - 0.9, 0.5) * (1 - ep(t, tb[i] + 0.9, 0.4))
            if p > 0:
                M.arrow(c, xs[i - 1] + size * 0.35, yb - size * 0.45, xs[i] - size * 0.35, y + size * 0.62, forte, p, 5, 14, p)
                E.pilula(c, "× " + E._num(raiz), (xs[i - 1] + xs[i]) / 2 + 26, (y + yb) / 2 - 6, size * 0.36, estilo="g", fundo=forte, cor=BR if not escuro else "#07070F", a=p)
        last = i == len(res) - 1
        E.foco(c, t, tb[i], 0.45, lambda q, i=i, r=r, last=last: formula(c, E._num(r), xs[i], yb, size, (cor_resto or (CERTO if r == 0 else forte)) if last else tinta, q, "center"))
    if tr is not None:
        p = ep(t, tr, 0.5)
        E.caixa_pontilhada(c, xs[-1] - cw / 2 + 12, yb - size * 0.95, cw - 24, size * 1.3, p, cor_resto or (CERTO if res[-1] == 0 else forte), prog_=p)
    return res, xs, yb



def raiz_bola(c, t, t0, s, cx, cy, r=70, size=70, cor=CERTO):
    E.foco(c, t, t0, 0.5, lambda a: num_bola(c, s, cx, cy, r * ease_back(prog(t, t0, 0.6)), size, a, cor))


def geral(c, t, t0, x, y, size, align="center"):
    """ax³ + bx² + cx + d = 0 com as letras nas cores fixas"""
    monta(c, t, [("a", t0, CA), ("x^3 + ", t0), ("b", t0 + 0.2, CB), ("x^2 + ", t0 + 0.2), ("c", t0 + 0.4, CC), ("x + ", t0 + 0.4),
                 ("d", t0 + 0.6, CD), (" = 0", t0 + 0.6)], x, y, size, align)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        form(c, t, C["s01.a"], "x^3 − 6x^2 + 11x − 6 = 0", W / 2, 260, 120, align="center")
        E.frase(c, t, C["s01.b"], ps("soma das raízes?", "g", 72, TINTA) + ps("produto?", "g", 72, TINTA), W / 2, 460, "center", passo=0.15)
        resp(c, t, C["s01.c"], "soma 6", 700, 700, 80, COR)
        resp(c, t, C["s01.c"] + 0.5, "produto 6", 1220, 700, 80, COR)
        nota(c, t, C["s01.c"] + 1.3, "sem achar as raízes", W / 2, 960, 64, TINTA2, "i", "center")
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], None, [(ps("soma e produto", "g", 110, COR), 1.0),
                                           (ps("direto dos coeficientes", "i", 96), 1.6)])
        E.frase(c, t, C["s02.b"], ps("relações de", "i", 90) + ps("Girard", "g", 100, COR), 1880, 960, "right", passo=0.15)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("soma e produto", "g", 60, COR) + ps("no grau dois:", "i", 60), "x^2 + bx + c = 0:   soma = −b,   produto = c"),
        (C["s03.c"], ps("forma fatorada:", "g", 60, COR) + ps("um parêntese por raiz", "i", 60), "(x − 1)(x − 2)(x − 3)"),
    ])


# ---------------- de onde vem ----------------
P3 = "x^3 − 6x^2 + 11x − 6"


def b_origem(c, t, C, b):
    E.frase(c, t, C["s04.a"] - 0.6, ps("raízes", "i", 80), XE, 190)
    for k, s in enumerate("123"):
        raiz_bola(c, t, C["s04.a"] + 0.3 * k, s, 480 + 180 * k, 165, 56, 60)
    form(c, t, C["s04.b"], "(x − 1)(x − 2)(x − 3)", W / 2, 400, 110, align="center")
    form(c, t, C["s04.c"], "= " + P3, W / 2, 570, 110, align="center")
    S, X, Y, SZ = "= " + P3, W / 2, 570, 110
    realce(c, t, C["s05.a"], S, "6x^2", X, Y, SZ, CB, "center")
    form(c, t, C["s05.a"] + 0.4, "1 + 2 + 3 = 6", 240, 770, 80, CB)
    nota(c, t, C["s05.a"] + 0.8, "soma", 240, 850, 54, CB, "g")
    realce(c, t, C["s05.b"], S, "− 6", X, Y, SZ, CD, "center", n=1)
    form(c, t, C["s05.b"] + 0.4, "1 · 2 · 3 = 6", 1430, 770, 80, CD)
    nota(c, t, C["s05.b"] + 0.8, "produto", 1430, 850, 54, CD, "g")
    realce(c, t, C["s05.c"], S, "11x", X, Y, SZ, CC, "center")
    form(c, t, C["s05.d"], "1 · 2 + 1 · 3 + 2 · 3 = 11", W / 2, 990, 80, CC, "center")
    nota(c, t, C["s05.c"] + 0.6, "de duas em duas", 860, 850, 54, CC, "g")


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    geral(c, t, C["s06.a"], W / 2, 200, 110)
    linhas = (("s06.b", "soma", "f{−b}{a}", CB), ("s06.c", "duas a duas", "f{c}{a}", CC), ("s06.d", "produto", "f{−d}{a}", CD))
    for k, (cue, nome, fx, cor) in enumerate(linhas):
        x = 360 + 600 * k
        E.frase(c, t, C[cue], [(nome, "g", 64, cor)], x, 420, "center")
        form(c, t, C[cue] + 0.3, fx, x, 580, 120, cor, "center")
    for k, s in enumerate(("troca", "mantém", "troca")):
        pil(c, t, C["s07.a"] + 0.4 * k, s, 360 + 600 * k, 720, 50, (ERRADO, CERTO, ERRADO)[k])
    if t >= C["s07.b"]:
        pil(c, t, C["s07.b"], "a = 1: é só ler", W / 2, 840, 52, TINTA)
        for k, v in enumerate(("6", "11", "6")):
            resp(c, t, C["s07.c"] + 0.4 * k, v, 360 + 600 * k, 960, 66, (CB, CC, CD)[k], r=62)


# ---------------- com á diferente de um ----------------
def b_coef_a(c, t, C, b):
    def s08():
        pil(c, t, C["s08.a"], "a ≠ 1: divida pelo a", W / 2, 180, 56)
        form(c, t, C["s08.b"], "2x^3 − 3x^2 − 11x + 6 = 0", W / 2, 380, 110, align="center")
        form(c, t, C["s08.c"], "soma = f{3}{2}", 520, 640, 110, CB, "center")
        nota(c, t, C["s08.c"] + 0.3, "o b com o sinal trocado, dividido por 2", 520, 800, 46, TINTA2, "i", "center")
        form(c, t, C["s08.d"], "produto = f{−6}{2} = −3", 1350, 640, 110, CD, "center")
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"] - 0.6, ps("as raízes:", "i", 80), XE, 220)
    for k, s in enumerate(("3", "−2", "f{1}{2}")):
        E.foco(c, t, C["s09.a"] + 0.3 * k, 0.5, lambda a, k=k, s=s: (E.bola(c, 700 + 240 * k, 195, 80 * ease_back(prog(t, C["s09.a"] + 0.3 * k, 0.6)), CERTO, a),
                                                                    formula(c, s, 700 + 240 * k, 195 + (30 if k < 2 else 0), 76 if k < 2 else 62, BR, a, "center")))
    form(c, t, C["s09.b"], "3 − 2 = 1,    1 + f{1}{2} = f{3}{2}", XE, 520, 96, CB)
    form(c, t, C["s09.c"], "3 · (−2) = −6,    −6 · f{1}{2} = −3", XE, 760, 96, CD)
    E.foco(c, t, C["s09.c"] + 2.0, 0.45, lambda a: E.selo(c, 1700, 730, 50, True, a))
    E.foco(c, t, C["s09.b"] + 1.8, 0.45, lambda a: E.selo(c, 1700, 490, 50, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 110, ERRADO)] + ps("com o produto", "i", 100), W / 2, 190, "center")
    nota(c, t, C["s10.a"], "o sinal do produto:", XE, 360, 64, TINTA2)
    pil(c, t, C["s10.a"] + 1.6, "grau 2: mantém (é o c)", 620, 480, 54, TINTA)
    pil(c, t, C["s10.b"], "grau 3: troca", 1280, 480, 54, COR)
    form(c, t, C["s10.c"], P3 + " = 0", XE, 680, 84, TINTA2)
    form(c, t, C["s10.c"] + 0.6, "produto = −6 ?", XE, 830, 96, ERRADO)
    if t > C["s10.d"]:
        E.risco(c, XE - 10, 850, XE + fw("produto = −6 ?", 96) + 10, 760, t, C["s10.d"], largura=12)
    form(c, t, C["s10.d"], "1 · 2 · 3 = 6", 1100, 830, 110, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s11():
        E.frase(c, t, C["s11.a"], ps("uma raiz conhecida", "g", 74, BR) + ps("+ Girard =", "i", 80, CLARO) + ps("as outras duas", "g", 74, BR), W / 2, 200, "center", passo=0.1)
        form(c, t, C["s11.b"], P3 + " = 0", W / 2, 370, 90, CLARO, "center")
        E.foco(c, t, C["s11.b"] + 1.5, 0.45, lambda a: E.pilula(c, "1 é raiz", W / 2, 470, 54, estilo="g", fundo=CERTO, cor=BR, a=a))
        form(c, t, C["s11.c"], "soma das outras:  6 − 1 = 5", 300, 640, 84, BR)
        form(c, t, C["s11.d"], "produto das outras:  f{6}{1} = 6", 300, 800, 84, BR)
        resp(c, t, C["s11.e"], "2 e 3", 1550, 900, 90)
    fase(c, t, C["s11"], C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], ps("soma e produto valem para", "i", 80, CLARO) + ps("as três juntas", "g", 74, BR), W / 2, 330, "center", passo=0.1)
    nota(c, t, entre(C["s12.a"], C["s12.b"], 0.6), "tirando a conhecida, sobra o que falta", W / 2, 450, 60, CLARO, "i", "center")
    E.foco(c, t, C["s12.b"], 0.45, lambda a: E.pilula(c, "raízes não inteiras: Briot-Ruffini + Bhaskara", W / 2, 720, 56, estilo="g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s13", "s14", [
        (C["s13.a"], lambda a: (E.escreve(c, "sem resolver,", XE, 380, 72, "i", TINTA, a), E.escreve(c, "soma e produto das raízes", XE, 480, 72, "g", COR, a)), 0, 0),
        (C["s13.b"], "x^3 − 4x^2 + x + 6 = 0", 700, 100),
    ], cx=1560, cy=470)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s15():
        form(c, t, C["s15"] + 0.1, "x^3 − 4x^2 + x + 6 = 0", W / 2, 200, 100, TINTA2, "center")
        for k, (l, v, cor) in enumerate((("a", "1", CA), ("b", "−4", CB), ("c", "1", CC), ("d", "6", CD))):
            E.foco(c, t, C["s15.a"] + 0.4 * k, 0.45, lambda p, k=k, l=l, v=v, cor=cor: E.pilula(c, f"{l} = {v}", 480 + 320 * k, 340, 54, estilo="g", fundo=cor, cor=BR, a=p), sobe=8)
        form(c, t, C["s15.b"], "soma = −(−4) = 4", 520, 600, 90, CB, "center")
        form(c, t, C["s15.c"], "produto = −6", 1420, 600, 90, CD, "center")
        resp(c, t, C["s15.b"] + 1.2, "4", 520, 820, 90, CB, r=90)
        resp(c, t, C["s15.c"] + 1.0, "−6", 1420, 820, 90, CD, r=90)
    fase(c, t, C["s15"], C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16"] + 0.1, ps("conferindo: as raízes são", "i", 76), XE, 220, passo=0.1)
    for k, s in enumerate(("−1", "2", "3")):
        raiz_bola(c, t, C["s16.a"] + 0.3 * k, s, 1150 + 190 * k, 195, 66, 60)
    form(c, t, C["s16.b"], "−1 + 2 + 3 = 4", XE, 520, 110, CB)
    form(c, t, C["s16.c"], "(−1) · 2 · 3 = −6", XE, 760, 110, CD)
    E.foco(c, t, C["s16.b"] + 1.2, 0.45, lambda a: E.selo(c, 1300, 480, 50, True, a))
    E.foco(c, t, C["s16.c"] + 1.4, 0.45, lambda a: E.selo(c, 1300, 720, 50, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def item(nome, fx, cor):
        return [(nome, "i", 72, TINTA), (fx, "g", 72, cor)]
    itens = ((C["s17.a"], item("soma:", "−b ÷ a", CB)), (C["s17.b"], item("duas a duas:", "c ÷ a", CC)), (C["s17.c"], item("produto:", "−d ÷ a", CD)))
    fim_padrao(c, t, C, "s17", "s18", itens, "próxima aula:", "prática de polinômios",
               extra=lambda: E.frase(c, t, C["s18.b"], ps("divisão, raízes, gráfico e", "i", 72) + ps("Girard", "g", 72, COR), XE, 540, passo=0.1),
               k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, regra=b_regra, coef_a=b_coef_a, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
