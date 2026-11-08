"""Visual — Estudativo · MAT-PLN-004: raízes e forma fatorada.
A raiz 1 de x³ − 2x² − 5x + 6 vira divisão exata, o Briot-Ruffini baixa o grau, Bhaskara acha 3 e −2 e sai
(x − 1)(x − 3)(x + 2), conferido com x = 10; o teorema fundamental da álgebra; o erro de esquecer a raiz dada e,
no palco, o atalho dos divisores do termo independente (começando pelo P(1)).
Convenções da trilha em MAT-PLN-001 e a TABELA de MAT-PLN-003. Nova: RAÍZES = esferas verdes com o número, uma por raiz.
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-004_raizes_forma_fatorada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("raiz", "fatorada", "teorema", "atalho", "questao", "fim"))


def _P(c, x):
    r = 0
    for k in c:
        r = r * x + k
    return r


# as contas da aula
assert [x for x in range(-10, 11) if _P([1, -2, -5, 6], x) == 0] == [-2, 1, 3]
assert 1 + 24 == 25 and (1 + 5) // 2 == 3 and (1 - 5) // 2 == -2
assert _P([1, -2, -5, 6], 10) == 756 == 9 * 7 * 12 and 1000 - 200 - 50 + 6 == 756
assert all(2 * x * x - 2 == 2 * (x - 1) * (x + 1) for x in range(-5, 6))
assert (-1) * (-3) * 2 == 6
assert [x for x in range(-10, 11) if _P([1, 0, -7, 6], x) == 0] == [-3, 1, 2] and 4 + 12 == 16
assert all((x - 2) * (x - 1) * (x + 3) == x ** 3 - 7 * x + 6 for x in range(-5, 6))


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



POLI = "x^3 − 2x^2 − 5x + 6"


def raiz_bola(c, t, t0, s, cx, cy, r=70, size=70, cor=CERTO):
    E.foco(c, t, t0, 0.5, lambda a: num_bola(c, s, cx, cy, r * ease_back(prog(t, t0, 0.6)), size, a, cor))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        form(c, t, C["s01.a"], POLI + " = 0", W / 2, 280, 120, align="center")
        pil(c, t, C["s01.b"], "Bhaskara: só grau 2", 620, 470, 60, ERRADO)
        pil(c, t, C["s01.c"], "1 é raiz", 1300, 470, 60)
        for k, s in enumerate(("1", "3", "−2")):
            raiz_bola(c, t, C["s01.d"] + 0.3 * k, s, 700 + 260 * k, 760, 90, 84)
        nota(c, t, C["s01.d"] + 1.2, "todas as raízes", W / 2, 940, 60, CERTO, "g", "center")
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], None, [(ps("baixar o grau", "g", 110, COR), 1.0),
                                           (ps("com uma raiz", "i", 96), 1.6)])
        form(c, t, C["s02.b"], "(x − 1)(x − 3)(x + 2)", 1880, 940, 96, COR, "right")


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("Briot-Ruffini:", "g", 64, COR) + ps("divide por x menos um número", "i", 64), None),
        (C["s03.c"], ps("Bhaskara:", "g", 64, COR) + ps("o delta primeiro", "i", 64), "Δ = b^2 − 4ac      x = f{−b ± r{Δ}}{2a}"),
    ])
    k = C["s03.b"] + 0.8
    briot(c, t, 1, [1, -2, -5, 6], k, [k + 0.4, k + 0.6, k + 0.8, k + 1.0], XE + 180, 495, 140, 56, mostra_conta=False)


# ---------------- raiz e divisão exata ----------------
def b_raiz(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], ps("raiz:", "g", 96, COR) + ps("o número que faz P dar zero", "i", 88), XE, 220, passo=0.12)
        form(c, t, C["s04.b"], "P(1) = 1 − 2 − 5 + 6 = 0", XE, 420, 110)
        E.frase(c, t, C["s04.c"], ps("P(1) =", "g", 72) + ps("resto da divisão por", "i", 78) + ps("x − 1", "g", 72, COR), XE, 620, passo=0.12)
        pil(c, t, C["s04.d"], "resto 0: divisão exata", 620, 800, 64, CERTO)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    form(c, t, C["s05.a"], "P(x) = (x − 1) · quociente", W / 2, 220, 100, align="center")
    k = C["s05.b"] - 0.6
    briot(c, t, 1, [1, -2, -5, 6], k, [k + 0.3, k + 0.5, k + 0.7, k + 0.9], 260, 450, 190, 90, tr=k + 1.1, mostra_conta=False)
    form(c, t, C["s05.b"], "quociente: x^2 − x − 6", 1080, 500, 72, COR)
    pil(c, t, C["s05.c"], "grau 3  →  grau 2", 1450, 660, 56, TINTA)
    E.frase(c, t, C["s05.d"], ps("isso é", "i", 96) + ps("baixar o grau", "g", 96, COR), W / 2, 930, "center", passo=0.12)


# ---------------- as outras raízes ----------------
def b_baixar(c, t, C, b):
    form(c, t, C["s06"] + 0.1, "(x − 1)(x^2 − x − 6) = 0", W / 2, 190, 100, align="center")
    E.foco(c, t, C["s06.a"], 0.45, lambda p: E.pilula(c, "produto = 0  →  algum fator = 0", W / 2, 300, 50, estilo="g", fundo=TINTA, cor=BR, a=p), sobe=8)
    form(c, t, C["s06.b"], "x − 1 = 0", XE, 470, 90)
    raiz_bola(c, t, C["s06.b"] + 0.6, "1", 690, 440, 56, 60)
    form(c, t, C["s06.c"], "x^2 − x − 6 = 0", 900, 470, 90, COR)
    pil(c, t, C["s07.a"], "a = 1   b = −1   c = −6", 1230, 580, 46, TINTA)
    form(c, t, C["s07.b"], "Δ = (−1)^2 − 4 · 1 · (−6) = 1 + 24 = 25", XE, 680, 72)
    form(c, t, C["s07.c"], "r{25} = 5      −b = 1", XE, 820, 72, TINTA2)
    form(c, t, C["s07.d"], "x = f{1 + 5}{2} = 3", 1250, 810, 72, CERTO)
    form(c, t, C["s07.e"], "x = f{1 − 5}{2} = −2", 1250, 960, 72, CERTO)


# ---------------- forma fatorada ----------------
def b_fatorada(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08.a"] - 0.6, ps("raízes", "i", 84), XE, 210)
        for k, s in enumerate(("1", "3", "−2")):
            raiz_bola(c, t, C["s08.a"] + 0.3 * k, s, 520 + 220 * k, 185, 66, 64)
        E.frase(c, t, C["s08.b"], ps("cada raiz vira", "i", 80) + ps("(x − raiz)", "g", 76, COR), XE, 400, passo=0.12)
        form(c, t, C["s08.c"], "x − (−2) = x + 2", XE, 540, 90, TINTA2)
        form(c, t, C["s08.d"], POLI + " = (x − 1)(x − 3)(x + 2)", W / 2, 760, 84, align="center")
        pil(c, t, C["s08.e"], "forma fatorada", 1300, 900, 60)
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)

    def s09():
        form(c, t, C["s09"] + 0.1, POLI + " = (x − 1)(x − 3)(x + 2)", W / 2, 220, 84, TINTA2, "center")
        nota(c, t, C["s09"] + 0.4, "teste com x = 10:", XE, 400, 64, TINTA2)
        form(c, t, C["s09.a"], "1000 − 200 − 50 + 6 = 756", XE, 560, 96)
        form(c, t, C["s09.b"], "9 · 7 · 12 = 756", XE, 720, 96, CERTO)
        E.foco(c, t, C["s09.b"] + 1.4, 0.45, lambda a: E.selo(c, 1100, 690, 50, True, a))
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], ps("número da frente", "i", 84) + ps("fica na frente", "g", 78, COR), XE, 260, passo=0.12)
    form(c, t, C["s10.b"], "2x^2 − 2", XE, 480, 110)
    nota(c, t, C["s10.b"] + 0.8, "raízes 1 e −1", 760, 470, 60, TINTA2)
    S = "2x^2 − 2 = 2(x − 1)(x + 1)"
    form(c, t, C["s10.c"], S, W / 2, 760, 110, align="center")
    realce(c, t, C["s10.c"] + 0.6, S, "2(", W / 2, 760, 110, COR, "center", n=0)


# ---------------- teorema fundamental ----------------
def b_teorema(c, t, C, b):
    E.frase(c, t, C["s11.a"], ps("teorema fundamental", "g", 84, COR) + ps("da álgebra", "i", 88), W / 2, 200, "center", passo=0.12)
    E.frase(c, t, C["s11.b"], ps("número de raízes =", "i", 96) + ps("grau", "g", 96, COR), W / 2, 380, "center", passo=0.12)
    nota(c, t, entre(C["s11.b"], C["s11.c"], 0.5), "grau 3, três raízes;  grau 4, quatro", W / 2, 470, 56, TINTA2, "i", "center")
    pil(c, t, C["s11.c"], "contando as repetidas", W / 2, 580, 52, TINTA)
    pil(c, t, C["s11.d"], "e as que não estão na reta (outra aula)", W / 2, 670, 52, TINTA)
    E.frase(c, t, C["s11.e"], ps("na reta:", "i", 84) + ps("no máximo o grau", "g", 80, COR), W / 2, 830, "center", passo=0.12)
    E.frase(c, t, C["s11.f"], ps("grau 3:", "g", 72) + ps("achou três raízes, acabou", "i", 78), W / 2, 980, "center", passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 110, ERRADO)] + ps("com a raiz dada", "i", 100), W / 2, 200, "center")
    form(c, t, C["s12.a"], "x^2 − x − 6 = 0", W / 2, 400, 100, TINTA2, "center")
    nota(c, t, C["s12.b"], "raízes:", 380, 600, 64, ERRADO, "i")
    for k, s in enumerate(("3", "−2")):
        raiz_bola(c, t, C["s12.b"] + 0.3 * k, s, 700 + 200 * k, 580, 64, 60)
    E.foco(c, t, C["s12.b"] + 0.9, 0.45, lambda a: E.selo(c, 1130, 580, 44, False, a))
    raiz_bola(c, t, C["s12.c"], "1", 1330, 580, 64, 60)
    nota(c, t, C["s12.c"] + 0.3, "faltou o 1", 1330, 700, 56, CERTO, "g", "center")
    pil(c, t, C["s12.d"], "grau 3: confira se estão as três", W / 2, 900, 62)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"] + 0.1, ps("e se ninguém der a raiz?", "i", 84, CLARO), W / 2, 200, "center", passo=0.1)
        nota(c, t, C["s13.a"], "primeiro coeficiente 1, todos inteiros:", W / 2, 360, 60, CLARO, "i", "center")
        E.frase(c, t, C["s13.b"], ps("raízes inteiras", "g", 84, BR) + ps("dividem o", "i", 88, CLARO) + ps("termo independente", "g", 84, BR), W / 2, 500, "center", passo=0.12)
        form(c, t, C["s13.c"], "divisores de 6:   ±1   ±2   ±3   ±6", W / 2, 720, 96, BR, "center")
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14"] + 0.1, ps("comece pelo 1:", "i", 84, CLARO) + ps("P(1) = soma dos coeficientes", "g", 76, BR), W / 2, 200, "center", passo=0.12)
    form(c, t, C["s14.b"], "1 − 2 − 5 + 6 = 0   →   1 é raiz", W / 2, 360, 84, CLARO, "center")
    S = "(x − 1)(x − 3)(x + 2)"
    form(c, t, C["s14.c"], S, W / 2, 560, 110, BR, "center")
    for tr in ("− 1", "− 3", "+ 2"):
        realce(c, t, C["s14.c"] + 0.8, S, tr, W / 2, 560, 110, CLARO, "center")
    form(c, t, C["s14.d"], "(−1) · (−3) · 2 = 6", W / 2, 720, 96, CLARO, "center")
    nota(c, t, entre(C["s14.d"], C["s14.e"], 0.6), "cada raiz divide o 6", W / 2, 820, 60, CLARO, "i", "center")
    E.foco(c, t, C["s14.e"], 0.45, lambda a: E.pilula(c, "raízes não inteiras: a questão precisa dar uma", W / 2, 960, 54, estilo="g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s15", "s16", [
        (C["s15.a"], "2 é raiz de", 420, 100),
        (C["s15.a"] + 0.6, "x^3 − 7x + 6", 600, 130),
        (C["s15.b"], lambda a: (E.escreve(c, "escreva a", XE, 820, 76, "i", TINTA, a), E.escreve(c, "forma fatorada", XE, 920, 80, "g", COR, a)), 0, 0),
    ], cx=1500)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        nota(c, t, C["s17.a"], "Briot-Ruffini com o 2, com o zero do x²", XE, 200, 56, TINTA2, "g")
        ks = "cdef"
        tb = [C["s17.c"] + 0.3] + [entre(C[f"s17.{ks[i]}"], C[f"s17.{ks[i + 1]}"] if i < 3 else C["s17.end"] - 0.3, 0.7) for i in range(1, 4)]
        briot(c, t, 2, [1, 0, -7, 6], (C["s17.a"], C["s17.b"]), tb, 330, 460, 230, 116, tr=tb[-1], falta=(1,))
    fase(c, t, C["s17"], C["s19"] - 0.1, s17)
    if C["s18"] <= t < C["s19"] + 0.4:
        def s18():
            form(c, t, C["s18.a"], "x^2 + 2x − 3 = 0", XE, 900, 84, COR)
            form(c, t, C["s18.b"], "Δ = 4 + 12 = 16,  r{16} = 4", 960, 900, 72, TINTA2)
            form(c, t, C["s18.c"], "x = f{−2 + 4}{2} = 1", 1370, 440, 66, CERTO)
            form(c, t, C["s18.d"], "x = f{−2 − 4}{2} = −3", 1370, 640, 66, CERTO)
        E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    form(c, t, C["s19.a"], "x^3 − 7x + 6 =", W / 2, 360, 100, align="center")
    form(c, t, C["s19.a"] + 0.5, "(x − 2)(x − 1)(x + 3)", W / 2, 540, 130, CERTO, "center")
    for k, s in enumerate(("2", "1", "−3")):
        raiz_bola(c, t, C["s19.b"] + 0.3 * k, s, 740 + 220 * k, 790, 70, 66)
    nota(c, t, C["s19.b"] + 1.2, "três raízes para grau três", W / 2, 960, 60, TINTA2, "i", "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s20.a"], ps("uma raiz dá", "i", 72) + ps("divisão exata", "g", 72, COR)),
             (C["s20.b"], ps("a divisão", "i", 72) + ps("baixa o grau", "g", 72, COR)),
             (C["s20.c"], ps("cada raiz vira", "i", 72) + ps("um parêntese", "g", 72, COR)))
    fim_padrao(c, t, C, "s20", "s21", itens, "próxima aula:", "raiz repetida e gráfico",
               extra=lambda: E.frase(c, t, C["s21.b"], ps("e o sinal de um polinômio", "i", 72) + ps("sem abrir nada", "g", 72, COR), XE, 540, passo=0.1),
               k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, raiz=b_raiz, baixar=b_baixar, fatorada=b_fatorada, teorema=b_teorema,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
