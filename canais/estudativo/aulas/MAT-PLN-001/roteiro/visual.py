"""Visual — Estudativo · MAT-PLN-001: o que é polinômio, grau, valor numérico P(2) = 19, soma, multiplicação e identidade.
Abre a trilha de Polinômios e cria as convenções dela (peças comuns abaixo, iguais de MAT-PLN-001 a 010): fórmula na grotesca
pesada, destaque claro atrás do trecho da vez, resultado na esfera verde, sinal de idêntico desenhado em três barras.
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-001_o_que_e_polinomio.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("oque", "somar", "identidade", "atalho", "questao", "fim"))


def _P(c, x):
    r = 0
    for k in c:
        r = r * x + k
    return r


def _mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


# as contas da aula
assert _P([2, 0, -1, 5], 2) == 19 and _P([2, 0, -1, 5], 1) == 6
assert [a + b for a, b in zip([2, 0, -1, 5], [1, 0, 4, -1])] == [3, 0, 3, 4]
assert _mul([1, 2], [1, 0, -3]) == [1, 2, -3, -6] and _P([1, 2, -3, -6], 1) == -6 == 3 * -2
assert 8 + 8 == 16 and 2 * 2 ** 6 == 128
assert _P([3, -5, 1], -1) == 9 and _P([3, -5, 1], 1) == -1 and 3 * (-1) + 5 + 1 == 3


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



def chuveiro(c, t, ts, s, y, size, cor, align="center", x=W / 2, alto=90):
    """as quatro setas do chuveirinho (convenção de MAT-EQU-005), em ts = (1º·1º, 1º·2º, 2º·1º, 2º·2º)"""
    i2 = s.index(")(") + 1
    p1, p2 = s[1:i2 - 1], s[i2 + 1:-1]
    a1, b1 = p1.split(" ", 1)[0], p1.split(" ", 2)[2]
    a2, b2 = p2.split(" ", 1)[0], p2.split(" ", 2)[2]
    pos = lambda tr, n=0: trecho_x(s, tr, x, size, align, n)
    xa1, wa1 = pos(a1)
    xb1, wb1 = pos(b1)
    xa2, wa2 = pos(a2, 1 if a2 == a1 else 0)
    xb2, wb2 = pos(b2, 1 if b2 == b1 else 0)
    topo, base = y - size * 0.95, y + size * 0.2
    flecha(c, t, ts[0], xa1 + wa1 / 2, topo, xa2 + wa2 / 2, topo, alto * 1.4, cor)
    flecha(c, t, ts[1], xa1 + wa1 / 2, topo, xb2 + wb2 / 2, topo, alto * 2.2, cor)
    flecha(c, t, ts[2], xb1 + wb1 / 2, base, xa2 + wa2 / 2, base, -alto * 1.4, cor)
    flecha(c, t, ts[3], xb1 + wb1 / 2, base, xb2 + wb2 / 2, base, -alto * 2.2, cor)


POLI = "2x^3 − x + 5"


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")
    S, y, sz = "5x^2 + x^3", 470, 170

    def conta():
        form(c, t, a1, S, W / 2, y, sz, align="center")
        realce(c, t, b1, S, "x^2", W / 2, y, sz, ERRADO, "center", t1=c1)
        pil(c, t, b1 + 0.1, "grau 2?", 620, 700, 64, ERRADO)
        realce(c, t, c1, S, "5", W / 2, y, sz, ERRADO, "center", t1=d1)
        pil(c, t, c1 + 0.1, "grau 5?", 960, 700, 64, ERRADO)
        realce(c, t, d1, S, "x^3", W / 2, y, sz, CERTO, "center")
        resp(c, t, d1 + 0.2, "grau 3", 1340, 720, 70)
        if t > b1 + 0.6:
            E.risco(c, 510, 740, 730, 660, t, c1 - 0.2, TINTA, largura=9)
        if t > c1 + 0.6:
            E.risco(c, 850, 740, 1070, 660, t, d1 - 0.2, TINTA, largura=9)
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], C["s02.b"], [(ps("polinômio:", "g", 120, COR), 1.0),
                                                 (ps("grau, valor,", "i", 96), 1.6),
                                                 (ps("soma e produto", "i", 96), 2.2)])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("trocar a letra", "g", 60, COR) + ps("por um número entre parênteses", "i", 60), "2 · (−3)^2"),
        (C["s03.c"], ps("juntar", "i", 60) + ps("semelhantes", "g", 60, COR) + ps("(mesma letra e expoente)", "i", 60), "3x + 5x = 8x"),
        (C["s03.d"], ps("chuveirinho:", "g", 60, COR) + ps("cada termo multiplica cada termo", "i", 60), "(x + 1)(x + 2)"),
    ])


# ---------------- o que é ----------------
def b_oque(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"] + 0.1, ps("polinômio", "g", 110, COR) + ps("é uma soma de termos", "i", 96), XE, 220, passo=0.12)
        S = "3x^4"
        form(c, t, C["s04.b"], S, 520, 560, 200, align="center")
        nota(c, t, C["s04.b"] + 0.5, "número", 410, 680, 54, COR, "g", "center")
        nota(c, t, C["s04.b"] + 0.9, "potência de x", 610, 760, 54, TINTA, "g", "center")
        pil(c, t, C["s04.c"], "expoente inteiro, sem sinal de menos", 600, 900, 50)
        form(c, t, C["s04.d"], "+ 7", 1200, 560, 200)
        nota(c, t, C["s04.d"] + 0.4, "número sozinho", 1310, 700, 54, TINTA, "g", "center")
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    def s05():
        y, sz = 400, 150
        form(c, t, C["s05.a"], POLI, W / 2, y, sz, align="center")
        realce(c, t, C["s05.b"], POLI, "2", W / 2, y, sz, COR, "center")
        x2, _ = trecho_x(POLI, "2", W / 2, sz, "center")
        nota(c, t, C["s05.b"] + 0.3, "coeficiente 2", x2 - 60, 560, 54, COR, "g")
        realce(c, t, C["s05.c"], POLI, "− x", W / 2, y, sz, COR, "center")
        x3, w3 = trecho_x(POLI, "− x", W / 2, sz, "center")
        nota(c, t, C["s05.c"] + 0.3, "coeficiente −1", x3 + w3 / 2, 640, 54, COR, "g", "center")
        realce(c, t, C["s05.d"], POLI, "5", W / 2, y, sz, AM, "center")
        x4, _ = trecho_x(POLI, "5", W / 2, sz, "center")
        nota(c, t, C["s05.d"] + 0.3, "termo independente", min(x4 + 40, 1580), 730, 54, TINTA, "g", "center")
        if t >= C["s06"]:
            form(c, t, C["s06.a"], "f{1}{x}", 700, 880, 110, ERRADO, "center")
            if t > C["s06.a"] + 0.6:
                E.risco(c, 640, 930, 760, 790, t, C["s06.a"] + 0.6, largura=10)
            E.frase(c, t, C["s06.b"], ps("x embaixo da fração:", "i", 64) + ps("não é polinômio", "g", 60, ERRADO), 820, 890, passo=0.1)
    fase(c, t, C["s05"], 1e9, s05)


# ---------------- grau ----------------
def b_grau(c, t, C, b):
    E.frase(c, t, C["s07.a"], ps("grau", "g", 110, COR) + ps("= o maior expoente do x", "i", 90), XE, 220, passo=0.12)
    y1, sz = 450, 130
    form(c, t, C["s07.a"] + 0.8, POLI, XE, y1, sz)
    realce(c, t, C["s07.b"], POLI, "x^3", XE, y1, sz, CERTO)
    resp(c, t, C["s07.b"] + 0.2, "3", 1450, y1 - 45, 90, r=90)
    S2, y2 = "5x^2 + x^3", 720
    form(c, t, C["s07.c"], S2, XE, y2, sz)
    realce(c, t, C["s07.c"] + 0.6, S2, "x^3", XE, y2, sz, CERTO)
    resp(c, t, C["s07.c"] + 0.8, "3", 1450, y2 - 45, 90, r=90)
    pil(c, t, C["s07.d"], "a ordem não importa", 470, 900, 52, TINTA)
    pil(c, t, C["s07.e"], "o número da frente não conta", 1270, 900, 52, TINTA)


# ---------------- valor numérico ----------------
def b_valor(c, t, C, b):
    y0 = 240
    form(c, t, C["s08.a"], "P(x) = " + POLI, W / 2, y0, 120, align="center")
    def s08():
        nota(c, t, C["s08.a"] + 1.0, "P de polinômio; o x avisa a letra", W / 2, 380, 58, TINTA2, "i", "center")
        form(c, t, C["s08.b"], "P(2)", 640, 620, 140, COR, "center")
        E.frase(c, t, C["s08.b"] + 0.5, ps("= valor quando", "i", 76) + ps("x = 2", "g", 70, COR), 780, 620, passo=0.12)
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    S = "P(2) = 2 · (2)^3 − (2) + 5"
    y = 470
    form(c, t, C["s09.a"], S, W / 2, y, 110, align="center")
    for n in (1, 2):
        realce(c, t, C["s09.a"] + 0.5, S, "(2)", W / 2, y, 110, COR, "center", n=n)
    form(c, t, C["s09.b"], "2 · 8 = 16", W / 2, 640, 96, TINTA2, "center")
    form(c, t, C["s09.c"], "16 − 2 + 5", 640, 850, 110, align="center")
    resp(c, t, C["s09.d"], "P(2) = 19", 1300, 815, 84)


# ---------------- somar ----------------
COLS = (760, 1120, 1420)  # borda direita das colunas x³, x e número


def linha_cols(c, t, t0, partes, y, size, cor=None, dt=0.15):
    for k, s in enumerate(partes):
        if s:
            form(c, t, t0 + dt * k, s, COLS[k], y, size, cor, "right")


def b_somar(c, t, C, b):
    E.frase(c, t, C["s10.a"], ps("somar", "g", 96, COR) + ps("= juntar os semelhantes", "i", 84), XE, 200, passo=0.12)
    sz = 120
    ys = (420, 580, 800)
    linha_cols(c, t, C["s10.b"], ("2x^3", "− x", "+ 5"), ys[0], sz)
    linha_cols(c, t, C["s10.c"], ("x^3", "+ 4x", "− 1"), ys[1], sz)
    form(c, t, C["s10.c"], "+", 380, ys[1], sz, COR)
    p = ep(t, C["s10.c"] + 0.6, 0.5)
    if p > 0:
        M.line(c, 400, ys[1] + 60, 400 + 1080 * p, ys[1] + 60, TINTA, 1.0, 6)
    for k, (cue, s) in enumerate((("s11.a", "3x^3"), ("s11.b", "+ 3x"), ("s11.c", "+ 4"))):
        x1 = COLS[k]
        w = 300 if k < 2 else 220
        a = ep(t, C[cue], 0.35) * (1 - ep(t, C["s11.d"], 0.3))
        if a > 0:
            M.rrect(c, x1 - w + 10, ys[0] - 130, w, ys[2] - ys[0] + 170, 24, COR, 0.1 * a)
        form(c, t, C[cue] + 0.2, s, x1, ys[2], sz, CERTO if t >= C["s11.d"] else COR, "right")
    nota(c, t, C["s11.d"] + 0.3, "o expoente não muda", 1500, ys[2] + 120, 54, CERTO, "i", "center")


# ---------------- multiplicar ----------------
def b_multiplicar(c, t, C, b):
    S, y, sz = "(x + 2)(x^2 − 3)", 450, 130
    def s12():
        E.frase(c, t, C["s12.a"], ps("multiplicar:", "g", 80, COR) + ps("chuveirinho", "i", 84), XE, 150, passo=0.12)
        form(c, t, C["s12.b"], S, W / 2, y, sz, align="center")
        ts = tuple(C[f"s12.{k}"] for k in "cdef")
        chuveiro(c, t, ts, S, y, sz, COR, alto=55)
        prods = (("x · x^2 = x^3", "s12.c"), ("x · (−3) = −3x", "s12.d"), ("2 · x^2 = 2x^2", "s12.e"), ("2 · (−3) = −6", "s12.f"))
        for k, (s, cue) in enumerate(prods):
            xx, yy = (330 if k % 2 == 0 else 1030), (760 if k < 2 else 920)
            form(c, t, C[cue] + 0.1, s, xx, yy, 92, TINTA)
    fase(c, t, C["s12"], C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    R = "x^3 + 2x^2 − 3x − 6"
    form(c, t, C["s13"] + 0.1, S, W / 2, 300, sz, align="center")
    form(c, t, C["s13.a"], "= " + R, W / 2, 520, 120, CERTO, "center")
    x1, w1 = trecho_x(S, "(x + 2)", W / 2, sz, "center")
    x2, w2 = trecho_x(S, "(x^2 − 3)", W / 2, sz, "center")
    pil(c, t, C["s13.b"], "grau 1", x1 + w1 / 2, 130, 52, TINTA)
    pil(c, t, C["s13.b"] + 0.6, "grau 2", x2 + w2 / 2, 130, 52, TINTA)
    pil(c, t, C["s13.b"] + 1.6, "grau 3", W / 2, 650, 52, CERTO)
    E.frase(c, t, C["s13.c"], ps("na multiplicação,", "i", 84) + ps("os graus somam:", "g", 76, COR) + ps("1 + 2 = 3", "g", 76), W / 2, 880, "center", passo=0.12)


# ---------------- identidade ----------------
def b_identidade(c, t, C, b):
    def s14():
        E.frase(c, t, C["s14.a"], ps("idênticos:", "g", 100, COR) + ps("mesmo valor para qualquer x", "i", 84), XE, 280, passo=0.12)
        E.frase(c, t, C["s14.b"], ps("coeficientes iguais,", "i", 84) + ps("termo a termo", "g", 76, COR), XE, 450, passo=0.12)
        E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.bola(c, W / 2, 720, 150, a=a), ident(c, W / 2, 720 + 60, 230, BR, a)))
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)

    def s15():
        S, y, sz = "ax + b ≡ 3x − 2", 330, 140
        form(c, t, C["s15.a"], S, W / 2, y, sz, align="center")
        realce(c, t, C["s15.b"], S, "ax", W / 2, y, sz, COR, "center")
        realce(c, t, C["s15.b"], S, "3x", W / 2, y, sz, COR, "center")
        realce(c, t, C["s15.c"], S, "b", W / 2, y, sz, AM, "center")
        realce(c, t, C["s15.c"], S, "− 2", W / 2, y, sz, AM, "center")
        resp(c, t, C["s15.b"] + 0.4, "a = 3", 700, 560, 84, COR)
        resp(c, t, C["s15.c"] + 0.4, "b = −2", 1220, 560, 84, COR)
    fase(c, t, C["s15"], C["s16"] - 0.1, s15)

    if t < C["s16"]:
        return
    S, y, sz = "ax^2 + bx + c ≡ 4x^2 − 7", 300, 120
    form(c, t, C["s16.a"], S, W / 2, y, sz, align="center")
    form(c, t, C["s16.b"], "a = 4", 560, 480, 90, COR, "center")
    form(c, t, C["s16.b"] + 0.4, "c = −7", 1360, 480, 90, COR, "center")
    S2 = "4x^2 + 0x − 7"
    form(c, t, C["s16.c"], S2, 760, 720, 120, align="center")
    realce(c, t, C["s16.c"] + 0.5, S2, "0x", 760, 720, 120, AM, "center")
    nota(c, t, C["s16.c"] + 0.4, "nenhum x é zero x", 760, 840, 56, TINTA2, "i", "center")
    resp(c, t, C["s16.d"], "b = 0", 1440, 690, 80, COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s17"], [("cuidado", "g", 110, ERRADO)] + ps("na soma", "i", 100), W / 2, 190, "center")
    S, y = "x^3 + x^3 = 2x^6", 400
    certo = t >= C["s18.a"]
    if not certo:
        form(c, t, C["s17.a"], "x^3 + x^3 =", 560, y, 130)
        form(c, t, C["s17.b"], "2x^6", 560 + fw("x^3 + x^3 = ", 130), y, 130, ERRADO)
        if t > C["s17.d"] + 1.0:
            x0 = 560 + fw("x^3 + x^3 = ", 130)
            E.risco(c, x0 - 10, y + 30, x0 + fw("2x^6", 130) + 10, y - 120, t, C["s17.d"] + 1.0, largura=12)
    else:
        form(c, t, C["s18.a"], "x^3 + x^3 = 2x^3", 560, y, 130, CERTO)
    def teste():
        nota(c, t, C["s17.c"] - 0.6, "teste com x = 2:", XE, 580, 60, TINTA2)
        form(c, t, C["s17.c"], "8 + 8 = 16", XE, 720, 100, CERTO)
        form(c, t, C["s17.d"], "2 · 2^6 = 2 · 64 = 128", 900, 720, 100, ERRADO)
    fase(c, t, C["s17.c"] - 0.6, C["s18.b"] - 0.1, teste)
    if t >= C["s18.b"]:
        nota(c, t, C["s18.b"], "na multiplicação, sim:", 480, 690, 64, TINTA2)
        form(c, t, C["s18.b"] + 0.5, "x^3 · x^3 = x^6", 480, 850, 120, COR)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s19():
        E.frase(c, t, C["s19"] + 0.1, ps("agora, o atalho", "i", 80, CLARO), W / 2, 180, "center")
        form(c, t, C["s19.a"], "P(1)", 560, 380, 160, BR, "center")
        E.frase(c, t, C["s19.a"] + 0.6, ps("= soma dos", "i", 90, CLARO) + ps("coeficientes", "g", 84, BR), 720, 380, passo=0.12)
        form(c, t, C["s19.b"] - 0.4, POLI, W / 2, 580, 110, CLARO, "center")
        form(c, t, C["s19.b"], "2 − 1 + 5 = 6", W / 2, 740, 110, BR, "center")
        E.frase(c, t, C["s19.c"], ps("porque", "i", 70, CLARO) + ps("1 elevado a qualquer expoente = 1", "g", 64, BR), W / 2, 930, "center", passo=0.08)
    fase(c, t, C["s19"], C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"], ps("sem abrir o produto:", "i", 80, CLARO), W / 2, 190, "center")
    form(c, t, C["s20.b"], "(x + 2)(x^2 − 3)", W / 2, 370, 120, BR, "center")
    form(c, t, C["s20.c"], "(1 + 2)(1 − 3) = 3 · (−2) = −6", W / 2, 540, 100, CLARO, "center")
    nota(c, t, C["s20.d"] - 0.3, "aberto:", 360, 720, 64, CLARO)
    form(c, t, C["s20.d"], "1 + 2 − 3 − 6 = −6", 600, 720, 100, BR)
    E.foco(c, t, C["s20.d"] + 1.5, 0.45, lambda a: E.selo(c, 1660, 690, 56, True, a))
    E.frase(c, t, C["s20.e"], ps("outro valor de x:", "i", 64, CLARO) + ps("conta inteira", "g", 60, BR), W / 2, 920, "center", passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s21", "s22", [
        (C["s21.a"], "P(x) = 3x^2 − 5x + 1", 420, 110),
        (C["s21.b"], "P(−1) = ?", 640, 110),
        (C["s21.c"], lambda a: (E.escreve(c, "soma dos", XE, 810, 76, "i", TINTA, a), E.escreve(c, "coeficientes = ?", XE, 900, 76, "g", COR, a)), 0, 0),
    ])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s23():
        S, y, sz = "3 · (−1)^2 − 5 · (−1) + 1", 300, 110
        form(c, t, C["s23.a"], S, W / 2, y, sz, align="center")
        realce(c, t, C["s23.b"], S, "3 · (−1)^2", W / 2, y, sz, COR, "center", t1=C["s23.c"])
        form(c, t, C["s23.b"] + 0.3, "(−1)^2 = 1   →   3 · 1 = 3", W / 2, 460, 86, TINTA2, "center")
        realce(c, t, C["s23.c"], S, "− 5 · (−1)", W / 2, y, sz, COR, "center", t1=C["s23.d"])
        form(c, t, C["s23.c"] + 0.3, "−5 · (−1) = +5", W / 2, 590, 86, TINTA2, "center")
        form(c, t, C["s23.d"], "3 + 5 + 1", 600, 860, 110, align="center")
        resp(c, t, C["s23.d"] + 0.6, "P(−1) = 9", 1340, 830, 84)
    fase(c, t, C["s23"], C["s24"] - 0.1, s23)
    if t < C["s24"]:
        return
    form(c, t, C["s24.a"], "soma dos coeficientes = P(1)", W / 2, 230, 90, align="center")
    form(c, t, C["s24.b"], "3 − 5 + 1", 640, 420, 110, align="center")
    resp(c, t, C["s24.b"] + 0.6, "−1", 1180, 385, 90, r=90)
    nota(c, t, C["s24.c"] - 0.2, "sem parênteses no quadrado:", XE, 640, 58, ERRADO)
    form(c, t, C["s24.c"], "−1^2 = −1", XE, 780, 96, ERRADO)
    form(c, t, C["s24.d"], "3 · (−1) + 5 + 1 = 3", 860, 780, 96, ERRADO)
    if t > C["s24.d"] + 0.9:
        E.risco(c, 1500, 800, 1640, 700, t, C["s24.d"] + 0.9, largura=10)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s25.a"], ps("grau =", "i", 72) + ps("maior expoente", "g", 72, COR)),
             (C["s25.b"], [("P(a):", "g", 72, COR)] + ps("troque o x por a", "i", 72)),
             (C["s25.c"], ps("somar e multiplicar:", "i", 72) + ps("como com letras", "g", 72, COR)))
    fim_padrao(c, t, C, "s25", "s26", itens, "próxima aula:", "dividir polinômios",
               extra=lambda: E.frase(c, t, C["s26.b"], ps("e achar", "i", 72) + ps("o resto sem dividir", "g", 72, COR), XE, 540, passo=0.1),
               k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, oque=b_oque, grau=b_grau, valor=b_valor, somar=b_somar,
              multiplicar=b_multiplicar, identidade=b_identidade, erro=b_erro, atalho=b_atalho, questao=b_questao,
              resposta=b_resposta, fim=b_fim)
