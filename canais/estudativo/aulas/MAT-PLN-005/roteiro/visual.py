"""Visual — Estudativo · MAT-PLN-005: multiplicidade, gráfico e sinal de um polinômio.
y = (x − 1)²(x + 2): raiz dupla 1 (toca e volta), raiz simples −2 (corta); o sinal na reta; a inequação > 0 (x > −2 e x ≠ 1);
o erro de trocar o sinal em toda raiz; no palco, o atalho do sinal (ímpar troca, par mantém); a questão (x + 1)(x − 3)² ≤ 0.
Convenções da trilha em MAT-PLN-001. Nova: SINAL = esfera pequena com + (cor da matéria) ou − (grafite) sobre cada pedaço da
reta; sinal errado em vermelho. Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-005_multiplicidade_grafico_sinal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("mult", "grafico", "erro", "atalho", "questao", "fim"))


def f(x):
    return (x - 1) ** 2 * (x + 2)


def g(x):
    return (x + 1) * (x - 3) ** 2


# as contas da aula
assert f(0) == 2 and f(-3) < 0 and f(-1) > 0 and f(2) > 0 and f(1) == 0 and f(-2) == 0
assert [s for s in (f(-3), f(0), f(2))] == [-16, 2, 4]
assert g(-2) < 0 and g(0) > 0 and g(4) > 0 and g(3) == 0 and g(-1) == 0


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



SG = "#3A3A48"  # o sinal de menos


def sinal_em(c, t, t0, x, y, s, cor=None, r=54):
    """esfera de sinal: + na cor da matéria, − em grafite (ou cor dada)"""
    cor = cor or (E.COR if s == "+" else SG)
    E.foco(c, t, t0, 0.4, lambda a: (E.bola(c, x, y, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, x, y + r * 0.38, r * 1.15, "g", BR, a)), sobe=8)


def reta_raizes(c, t, t0, raizes, y=640, x0=360, x1=1560, vmin=-4, vmax=3, escuro=False, tm=None):
    return E.reta(c, t, t0, x0, x1, y, vmin, vmax, raizes, fmt=E._num, escuro=escuro, size=54, tm=tm)


def grafico(c, t, t0, td, x=200, y=150, w=780, h=800):
    P = E.plano(c, t, t0, x, y, w, h, -3, 2.5, -7, 7, passo=1, passo_y=2, marcas_y=[-6, -4, -2, 2, 4, 6], size=36)
    E.curva(c, t, td, P, f, -2.5, 2.2, d=1.6, largura=8)
    return P


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        form(c, t, C["s01.a"], "y = (x − 1)^2(x + 2)", 1480, 230, 84, align="center")
        P = grafico(c, t, C["s01.a"] + 0.4, C["s01.a"] + 1.0)
        E.ponto(c, t, C["s01.b"], P, -2, 0, cor=COR, r=16)
        pil(c, t, C["s01.b"] + 0.2, "−2: atravessa", 1480, 450, 64)
        E.ponto(c, t, C["s01.c"], P, 1, 0, cor=CERTO, r=16)
        pil(c, t, C["s01.c"] + 0.2, "1: encosta e volta", 1480, 580, 64, CERTO)
        E.frase(c, t, C["s01.d"], ps("sem marcar", "i", 66) + ps("ponto nenhum", "g", 62, COR), 1480, 800, "center", passo=0.12)
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], C["s02.b"], [(ps("gráfico e sinal", "g", 110, COR), 1.0),
                                                 (ps("direto da", "i", 96), 1.6),
                                                 (ps("forma fatorada", "i", 96), 2.0)])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("forma fatorada:", "g", 60, COR) + ps("cada raiz vira um parêntese", "i", 60), "(x − 1)(x − 3)(x + 2)"),
        (C["s03.c"], ps("zeros do gráfico:", "g", 60, COR) + ps("onde ele encontra o eixo x", "i", 60), None),
        (C["s03.d"], ps("quadro de sinais:", "g", 60, COR) + ps("o sinal de cada fator, pedaço a pedaço", "i", 60), None),
    ])


# ---------------- multiplicidade ----------------
def b_mult(c, t, C, b):
    S, y, sz = "(x − 1)^2(x + 2)", 280, 130
    form(c, t, C["s04"] + 0.1, S, W / 2, y, sz, align="center")
    realce(c, t, C["s04.a"], S, "(x − 1)^2", W / 2, y, sz, CERTO, "center", t1=C["s04.d"])
    form(c, t, C["s04.a"] + 0.4, "= (x − 1)(x − 1)(x + 2)", W / 2, 440, 90, TINTA2, "center")
    num_bola(c, "1", 560, 640, 70 * ease_back(prog(t, C["s04.b"], 0.6)), 70, ep(t, C["s04.b"], 0.4), CERTO)
    E.frase(c, t, C["s04.b"] + 0.3, ps("raiz dupla", "g", 70, CERTO), 560, 790, "center")
    nota(c, t, C["s04.c"], "multiplicidade 2", 560, 880, 58, CERTO, "g", "center")
    realce(c, t, C["s04.d"], S, "(x + 2)", W / 2, y, sz, COR, "center")
    num_bola(c, "−2", 1360, 640, 70 * ease_back(prog(t, C["s04.d"], 0.6)), 64, ep(t, C["s04.d"], 0.4), COR)
    E.frase(c, t, C["s04.d"] + 0.3, ps("raiz simples", "g", 70, COR), 1360, 790, "center")
    nota(c, t, C["s04.d"] + 1.2, "multiplicidade 1", 1360, 880, 58, COR, "g", "center")
    if t >= C["s05"]:
        E.foco(c, t, C["s05.a"], 0.45, lambda a: M.rrect(c, 260, 940, 1400, 110, 30, COR, 0.1 * a))
        E.frase(c, t, C["s05.a"], ps("multiplicidade =", "i", 64) + ps("quantas vezes o parêntese aparece", "g", 58, COR), W / 2, 1012, "center", passo=0.1)
        if t >= C["s05.b"]:
            x0, w = trecho_x(S, "^2", W / 2, sz, "center")
            E.foco(c, t, C["s05.b"], 0.45, lambda a: E.caixa_pontilhada(c, x0 - 8, y - sz * 1.0, w + 32, sz * 0.68, a, CERTO))
            nota(c, t, C["s05.b"] + 0.2, "o expoente", x0 - 60, y - sz * 1.15, 54, CERTO, "g")


# ---------------- sinal ----------------
def b_sinal(c, t, C, b):
    E.frase(c, t, C["s06"] + 0.1, ps("o sinal", "g", 96, COR), XE, 190)
    form(c, t, C["s06.a"], "(x − 1)^2 ≥ 0", XE, 360, 100, CERTO)
    nota(c, t, C["s06.b"], "número ao quadrado: zero ou positivo", 900, 345, 58, TINTA2, "i")
    E.frase(c, t, C["s06.c"], ps("fora do 1: sinal do produto = sinal de", "i", 70) + ps("(x + 2)", "g", 66, COR), XE, 500, passo=0.08)
    vx = reta_raizes(c, t, C["s07"], [-2, 1], y=780, tm=[C["s07.a"] - 0.3, C["s07.c"] - 0.3])
    sinal_em(c, t, C["s07.a"], vx(-3.1), 690, "−")
    sinal_em(c, t, C["s07.b"], vx(-0.5), 690, "+")
    sinal_em(c, t, C["s07.b"] + 0.2, vx(2.1), 690, "+")
    E.foco(c, t, C["s07.c"], 0.4, lambda a: centro(c, "0", vx(1), 712, 64, "g", CERTO, a))
    pil(c, t, C["s07.d"], "positivo antes, positivo depois", vx(1), 960, 54, CERTO)


# ---------------- gráfico ----------------
def b_grafico(c, t, C, b):
    P = grafico(c, t, C["s08"], C["s08.a"])
    E.ponto(c, t, C["s08.b"], P, -2, 0, cor=COR, r=16)
    pil(c, t, C["s08.b"] + 0.3, "−2: troca de sinal, corta", 1460, 300, 50)
    E.ponto(c, t, C["s08.c"], P, 1, 0, cor=CERTO, r=16)
    pil(c, t, C["s08.c"] + 0.3, "1: não troca, toca e volta", 1460, 400, 50, CERTO)
    E.frase(c, t, C["s09.a"], ps("ímpar:", "i", 72) + ps("corta", "g", 68, COR), 1460, 590, "center", passo=0.1)
    E.frase(c, t, C["s09.b"], ps("par:", "i", 72) + ps("toca e volta", "g", 68, CERTO), 1460, 700, "center", passo=0.1)
    E.ponto(c, t, C["s09.c"], P, 0, 2, "(0, 2)", cor=TINTA, r=13, lado=(1, -1))
    form(c, t, C["s09.d"], "(−1)^2 · 2 = 2", 1460, 890, 80, TINTA2, "center")


# ---------------- inequação ----------------
def b_inequacao(c, t, C, b):
    form(c, t, C["s10.a"], "(x − 1)^2(x + 2) > 0", W / 2, 220, 110, align="center")
    E.frase(c, t, C["s10.b"], ps("gráfico", "i", 80) + ps("acima do eixo", "g", 74, COR), W / 2, 380, "center", passo=0.12)
    vx = reta_raizes(c, t, C["s10.b"] + 0.4, [-2, 1], y=640)
    sinal_em(c, t, C["s10.b"] + 0.8, vx(-3.1), 550, "−")
    sinal_em(c, t, C["s10.b"] + 0.9, vx(-0.5), 550, "+")
    sinal_em(c, t, C["s10.b"] + 1.0, vx(2.1), 550, "+")
    E.intervalo(c, t, C["s10.c"], vx, 640, -2, 1, False, False, CERTO)
    E.intervalo(c, t, C["s10.d"], vx, 640, 1, None, False, False, CERTO)
    nota(c, t, C["s10.d"] + 0.3, "no 1, vale zero: fica de fora", vx(1), 780, 52, CERTO, "g", "center")
    pil(c, t, C["s10.e"], "x > −2  e  x ≠ 1", W / 2, 930, 76, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 100, ERRADO)] + ps("com a raiz dupla", "i", 96), W / 2, 180, "center")
    nota(c, t, C["s11.a"], "trocar o sinal em toda raiz", W / 2, 300, 64, ERRADO, "i", "center")
    vx = reta_raizes(c, t, C["s11.a"], [-2, 1], y=560)
    sinal_em(c, t, C["s11.a"] + 0.6, vx(2.1), 470, "+")
    certo = t >= C["s11.e"]
    sinal_em(c, t, C["s11.b"], vx(-0.5), 470, "+" if certo else "−", CERTO if certo else ERRADO)
    sinal_em(c, t, C["s11.b"] + 0.9, vx(-3.1), 470, "+" if not certo else "−", ERRADO if not certo else SG)
    form(c, t, C["s11.c"], "x = 0:   (0 − 1)^2 · (0 + 2)", W / 2, 760, 84, align="center")
    form(c, t, C["s11.d"], "= 1 · 2 = 2,  positivo", W / 2, 880, 84, CERTO, "center")
    pil(c, t, C["s11.e"], "raiz dupla não troca o sinal", W / 2, 990, 56, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s12():
        E.frase(c, t, C["s12"] + 0.1, ps("agora, o atalho do sinal", "i", 80, CLARO), W / 2, 170, "center", passo=0.1)
        E.frase(c, t, C["s12.a"], ps("depois da maior raiz:", "i", 70, CLARO) + ps("+", "g", 70, BR), W / 2, 290, "center", passo=0.1)
        E.foco(c, t, C["s12.b"], 0.45, lambda a: E.pilula(c, "multiplicidade ímpar: troca", 540, 410, 48, estilo="g", fundo=CLARO, cor="#07070F", a=a))
        E.foco(c, t, C["s12.c"], 0.45, lambda a: E.pilula(c, "multiplicidade par: mantém", 1380, 410, 48, estilo="g", fundo=CERTO, cor=BR, a=a))
        vx = reta_raizes(c, t, C["s12.d"] - 0.6, [-2, 1], y=760, escuro=True)
        nota(c, t, C["s12.d"] - 0.4, "simples", vx(-2), 920, 46, CLARO, "g", "center")
        nota(c, t, C["s12.d"] - 0.4, "dupla", vx(1), 920, 46, CERTO, "g", "center")
        sinal_em(c, t, C["s12.d"], vx(2.1), 670, "+", CLARO)
        sinal_em(c, t, C["s12.e"], vx(-0.5), 670, "+", CLARO)
        sinal_em(c, t, C["s12.f"], vx(-3.1), 670, "−", "#5A5A70")
        flecha(c, t, C["s12.e"] - 0.3, vx(1.9), 600, vx(-0.3), 600, 50, CERTO, 0.5, 5)
        flecha(c, t, C["s12.f"] - 0.3, vx(-0.7), 600, vx(-2.9), 600, 50, CLARO, 0.5, 5)
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("depois da maior raiz,", "i", 76, CLARO) + ps("todo parêntese é +", "g", 70, BR), W / 2, 280, "center", passo=0.1)
    E.frase(c, t, C["s13.b"], ps("em cada raiz,", "i", 76, CLARO) + ps("só o parêntese dela muda", "g", 70, BR), W / 2, 440, "center", passo=0.1)
    nota(c, t, entre(C["s13.b"], C["s13.c"], 0.55), "uma vez para cada repetição", W / 2, 540, 58, CLARO, "i", "center")
    E.foco(c, t, C["s13.c"], 0.45, lambda a: E.pilula(c, "(3 − x) ou negativo na frente? faça o quadro", W / 2, 780, 56, estilo="g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s14", "s15", [
        (C["s14.a"] - 0.4, lambda a: E.escreve(c, "resolva", XE, 420, 76, "i", TINTA, a), 0, 0),
        (C["s14.a"], "(x + 1)(x − 3)^2 ≤ 0", 620, 110),
    ], cx=1550, cy=560)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    form(c, t, C["s16"] + 0.1, "(x + 1)(x − 3)^2 ≤ 0", W / 2, 190, 96, TINTA2, "center")
    vx = reta_raizes(c, t, C["s16.a"] - 0.3, [-1, 3], y=560, vmin=-3, vmax=5, tm=[C["s16.a"], C["s16.b"]])
    nota(c, t, C["s16.a"] + 0.2, "simples", vx(-1), 710, 46, COR, "g", "center")
    nota(c, t, C["s16.b"] + 0.2, "dupla", vx(3), 710, 46, CERTO, "g", "center")
    sinal_em(c, t, C["s16.c"], vx(4.2), 460, "+")
    sinal_em(c, t, C["s16.d"], vx(1), 460, "+")
    sinal_em(c, t, C["s16.e"], vx(-2.2), 460, "−")
    E.intervalo(c, t, C["s17.b"], vx, 560, None, -1, False, True, CERTO)
    if t >= C["s17.c"]:
        p = ep(t, C["s17.c"], 0.3)
        c.drawCircle(vx(3), 560, 17 * p, M.paint(CERTO))
    resp(c, t, C["s17.d"], "x ≤ −1  ou  x = 3", W / 2, 860, 76)
    nota(c, t, C["s17.e"], "o 3 é onde o gráfico só encosta", W / 2, 1010, 54, TINTA2, "i", "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s18.a"], ps("expoente do parêntese =", "i", 72) + ps("multiplicidade", "g", 72, COR)),
             (C["s18.b"], ps("ímpar", "g", 72, COR) + ps("corta,", "i", 72) + ps("par", "g", 72, CERTO) + ps("encosta", "i", 72)),
             (C["s18.c"], ps("o sinal só troca nas", "i", 72) + ps("ímpares", "g", 72, COR)))
    fim_padrao(c, t, C, "s18", "s19", itens, "próxima aula: sem resolver a equação", "soma e produto das raízes",
               extra=lambda: E.frase(c, t, C["s19.b"], ps("de um polinômio de", "i", 72) + ps("grau três", "g", 72, COR), XE, 540, passo=0.1),
               k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, mult=b_mult, sinal=b_sinal, grafico=b_grafico, inequacao=b_inequacao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
