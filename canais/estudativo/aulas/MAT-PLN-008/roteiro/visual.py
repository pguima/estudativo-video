"""Visual — Estudativo · MAT-PLN-008: delta negativo, o número i.
x² − 4x + 13 = 0 com Δ = −36: i² = −1, √−36 = 6i, x = 2 ± 3i (conferido); números complexos (parte real e imaginária);
(2 + 3i)(2 − 3i) = 13 e o conjugado; o erro √−36 = −6; no palco, o atalho complexo vezes conjugado = a² + b².
Convenções da trilha em MAT-PLN-001. Nova: O NÚMERO i em âmbar (o que é imaginário), a parte real em tinta; conjugados lado a lado.
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-008_delta_negativo_numero_i.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("numero_i", "resolver", "multiplicar", "atalho", "questao", "fim"))
IM = "#B86E00"  # a parte com i

# as contas da aula
_i = 1j
assert 16 - 52 == -36 and (6 * _i) ** 2 == -36 and (-6) ** 2 == 36
for _z in (2 + 3 * _i, 2 - 3 * _i):
    assert _z * _z - 4 * _z + 13 == 0
assert (2 + 3 * _i) ** 2 == -5 + 12 * _i and -4 * (2 + 3 * _i) == -8 - 12 * _i
assert (2 + 3 * _i) * (2 - 3 * _i) == 13 == 4 + 9
assert 4 - 20 == -16 and (4 * _i) ** 2 == -16
for _z in (-1 + 2 * _i, -1 - 2 * _i):
    assert _z * _z + 2 * _z + 5 == 0


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


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        form(c, t, C["s01.a"], "x^2 − 4x + 13 = 0", W / 2, 300, 130, align="center")
        form(c, t, C["s01.b"], "Δ = 16 − 52 = −36", W / 2, 500, 110, ERRADO, "center")
        nota(c, t, C["s01.b"] + 0.9, "nenhum número da reta resolve", W / 2, 610, 60, TINTA2, "i", "center")
        resp(c, t, C["s01.c"], "x = 2 ± 3i", W / 2, 840, 110, COR)
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], C["s02.c"], [(ps("delta negativo", "g", 110, COR), 1.0),
                                                 (ps("com um número novo:", "i", 90), 1.8)])
        wl, _ = E._arranjo(ps("com um número novo:", "i", 90), XE, "left")
        form(c, t, C["s02.b"], "i", XE + wl + 40, 672, 130, IM)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("Bhaskara:", "g", 60, COR) + ps("o delta primeiro", "i", 60), "Δ = b^2 − 4ac      x = f{−b ± r{Δ}}{2a}"),
        (C["s03.c"], ps("delta negativo:", "g", 60, COR) + ps("nenhuma raiz real", "i", 60), None),
        (C["s03.d"], ps("raiz de uma multiplicação:", "g", 60, COR), "r{4 · 2} = r{4} · r{2}"),
    ])


# ---------------- o número i ----------------
def b_numero_i(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"] + 0.1, ps("e se existisse", "i", 90), XE, 230, passo=0.12)
        E.frase(c, t, C["s04.a"], ps("um número que, ao quadrado,", "i", 80) + ps("dá −1?", "g", 76, COR), XE, 380, passo=0.1)
        E.foco(c, t, C["s04.b"], 0.6, lambda a: E.bola(c, 560, 680, 150 * ease_back(prog(t, C["s04.b"], 0.6)), IM, a), blur=0)
        E.foco(c, t, C["s04.b"] + 0.2, 0.5, lambda a: centro(c, "i", 560, 750, 220, "g", BR, a))
        nota(c, t, C["s04.b"] + 0.6, "unidade imaginária", 560, 920, 56, IM, "g", "center")
        resp(c, t, C["s04.c"], "i^2 = −1", 1360, 690, 130, COR)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    def s05():
        form(c, t, C["s05.a"], "r{−1} = i", W / 2, 250, 120, IM, "center")
        form(c, t, C["s05.b"], "−36 = 36 · (−1)", W / 2, 470, 110, align="center")
        form(c, t, entre(C["s05.b"], C["s05.c"], 0.5), "r{36} = 6      r{−1} = i", W / 2, 640, 96, TINTA2, "center")
        E.foco(c, t, C["s05.c"], 0.45, lambda a: M.rrect(c, W / 2 - 330, 780, 660, 170, 40, COR, 0.12 * a))
        form(c, t, C["s05.c"], "r{−36} = 6i", W / 2, 905, 120, COR, "center")
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    S, y, sz = "2 + 3i", 420, 200
    form(c, t, C["s06.a"], S, W / 2, y, sz, align="center")
    E.frase(c, t, C["s06.b"], ps("número", "i", 84) + ps("complexo", "g", 84, COR), W / 2, 200, "center", passo=0.12)
    x2, w2 = trecho_x(S, "2", W / 2, sz, "center")
    x3, w3 = trecho_x(S, "3i", W / 2, sz, "center")
    realce(c, t, C["s06.c"], S, "2", W / 2, y, sz, TINTA, "center")
    nota(c, t, C["s06.c"] + 0.2, "parte real", x2 + w2 / 2, y + 130, 56, TINTA, "g", "center")
    realce(c, t, C["s06.d"], S, "3i", W / 2, y, sz, IM, "center")
    nota(c, t, C["s06.d"] + 0.2, "parte imaginária", x3 + w3 / 2, y + 130, 56, IM, "g", "center")
    form(c, t, C["s06.e"], "5 = 5 + 0i", W / 2, 850, 110, TINTA2, "center")
    nota(c, t, C["s06.e"] + 0.6, "os reais estão dentro dos complexos", W / 2, 960, 56, TINTA2, "i", "center")


# ---------------- resolver ----------------
def b_resolver(c, t, C, b):
    def s07():
        form(c, t, C["s07.a"], "x^2 − 4x + 13 = 0", W / 2, 220, 110, align="center")
        pil(c, t, C["s07.b"], "a = 1    b = −4    c = 13", W / 2, 360, 54, TINTA)
        form(c, t, C["s07.c"], "Δ = (−4)^2 − 4 · 1 · 13 = 16 − 52 = −36", W / 2, 560, 84, align="center")
        E.foco(c, t, C["s07.d"], 0.45, lambda a: M.rrect(c, W / 2 - 280, 720, 560, 170, 40, COR, 0.12 * a))
        form(c, t, C["s07.d"], "r{Δ} = 6i", W / 2, 845, 110, COR, "center")
    fase(c, t, C["s07"], C["s08"] - 0.1, s07)

    def s08():
        form(c, t, C["s08.a"], "x = f{4 ± 6i}{2}", XE, 330, 130)
        pil(c, t, C["s08.b"], "divida cada parte por 2", 1300, 290, 54)
        form(c, t, C["s08.c"], "4 ÷ 2 = 2", 1100, 470, 90, TINTA2)
        form(c, t, C["s08.d"], "6i ÷ 2 = 3i", 1100, 600, 90, IM)
        pil(c, t, C["s08.e"], "x = 2 + 3i", 600, 880, 84, CERTO)
        pil(c, t, C["s08.e"] + 0.8, "x = 2 − 3i", 1320, 880, 84, CERTO)
    fase(c, t, C["s08"], C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    nota(c, t, C["s09"] + 0.1, "conferindo x = 2 + 3i na equação:", XE, 190, 58, TINTA2)
    form(c, t, C["s09.a"], "(2 + 3i)^2 = 4 + 12i + 9i^2", XE, 360, 96)
    form(c, t, C["s09.b"], "= 4 + 12i − 9 = −5 + 12i", XE + 120, 500, 96, TINTA2)
    form(c, t, C["s09.c"], "−4(2 + 3i) = −8 − 12i", XE, 680, 96)
    form(c, t, C["s09.d"], "−5 + 12i − 8 − 12i + 13 = 0", XE, 880, 96, CERTO)
    E.foco(c, t, C["s09.d"] + 1.4, 0.45, lambda a: E.selo(c, 1660, 850, 50, True, a))


# ---------------- multiplicar ----------------
def b_multiplicar(c, t, C, b):
    E.frase(c, t, C["s10.a"], ps("chuveirinho, com", "i", 76) + ps("i² = −1", "g", 72, COR), XE, 150, passo=0.1)
    S = "(2 + 3i)(2 − 3i)"
    form(c, t, C["s10.b"], S, W / 2, 400, 130, align="center")
    pil(c, t, C["s10.c"], "soma vezes diferença", W / 2, 520, 54, TINTA)
    form(c, t, C["s10.d"], "= 2^2 − (3i)^2", W / 2, 680, 110, align="center")
    form(c, t, C["s11.a"], "(3i)^2 = 9i^2 = −9", XE, 880, 90, IM)
    form(c, t, C["s11.b"], "4 − (−9) = 13", 1060, 880, 90, CERTO)
    nota(c, t, C["s11.c"], "o i sumiu: resultado real", 1360, 980, 54, CERTO, "i", "center")
    if t >= C["s11.d"]:
        x1, w1 = trecho_x(S, "(2 − 3i)", W / 2, 130, "center")
        E.foco(c, t, C["s11.d"], 0.45, lambda a: E.caixa_pontilhada(c, x1 - 10, 260, w1 + 20, 170, a, IM))
        nota(c, t, C["s11.d"] + 0.2, "conjugado: só o sinal do i muda", x1 + w1 / 2 + 40, 245, 46, IM, "g", "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 110, ERRADO)] + ps("com o sinal", "i", 100), W / 2, 190, "center")
    certo = t >= C["s12.c"]
    form(c, t, C["s12.a"], "r{−36} = −6 ?", XE, 420, 120, ERRADO)
    if t > C["s12.b"] + 0.6:
        E.risco(c, XE - 10, 440, XE + fw("r{−36} = −6 ?", 120) + 10, 320, t, C["s12.b"] + 0.6, largura=12)
    form(c, t, C["s12.b"], "(−6)^2 = 36", 1100, 420, 100, ERRADO)
    form(c, t, C["s12.c"], "(6i)^2 = 36 · (−1) = −36", XE, 660, 110, CERTO)
    E.foco(c, t, C["s12.c"] + 1.6, 0.45, lambda a: E.selo(c, 1560, 630, 50, True, a))
    pil(c, t, C["s12.d"], "o menos de dentro da raiz vira i", W / 2, 900, 62)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"] + 0.1, ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s13.a"], ps("complexo × conjugado", "g", 84, BR), W / 2, 320, "center", passo=0.12)
        form(c, t, C["s13.b"], "(a + bi)(a − bi) = a^2 + b^2", W / 2, 500, 110, AM, "center")
        form(c, t, C["s13.c"], "(2 + 3i)(2 − 3i) = 4 + 9 = 13", W / 2, 720, 100, BR, "center")
        E.frase(c, t, C["s13.d"], ps("sem chuveirinho", "i", 80, CLARO), W / 2, 900, "center")
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("é", "i", 84, CLARO) + ps("soma vezes diferença", "g", 78, BR), W / 2, 280, "center", passo=0.12)
    E.frase(c, t, C["s14.b"], ps("e", "i", 84, CLARO) + ps("i² = −1", "g", 78, AM) + ps("vira o menos em mais", "i", 84, CLARO), W / 2, 440, "center", passo=0.12)
    form(c, t, C["s14.c"], "(2 + 3i)(1 − i)", W / 2, 700, 110, BR, "center")
    E.foco(c, t, C["s14.c"] + 1.5, 0.45, lambda a: E.pilula(c, "não são conjugados: chuveirinho", W / 2, 850, 58, estilo="g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s15", "s16", [
        (C["s15.a"] - 0.4, lambda a: E.escreve(c, "resolva", XE, 420, 76, "i", TINTA, a), 0, 0),
        (C["s15.a"], "x^2 + 2x + 5 = 0", 620, 120),
    ], cx=1550, cy=560)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        form(c, t, C["s17"] + 0.1, "x^2 + 2x + 5 = 0", W / 2, 200, 100, TINTA2, "center")
        pil(c, t, C["s17.a"], "a = 1    b = 2    c = 5", W / 2, 340, 54, TINTA)
        form(c, t, C["s17.b"], "Δ = 4 − 20 = −16", W / 2, 560, 110, align="center")
        E.foco(c, t, C["s17.c"], 0.45, lambda a: M.rrect(c, W / 2 - 320, 720, 640, 170, 40, COR, 0.12 * a))
        form(c, t, C["s17.c"], "r{−16} = 4i", W / 2, 845, 110, COR, "center")
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    form(c, t, C["s18.a"], "x = f{−2 ± 4i}{2}", XE, 330, 130)
    form(c, t, C["s18.b"], "−2 ÷ 2 = −1", 1100, 290, 90, TINTA2)
    form(c, t, C["s18.c"], "4i ÷ 2 = 2i", 1100, 420, 90, IM)
    pil(c, t, C["s18.d"], "x = −1 + 2i", 600, 760, 84, CERTO)
    pil(c, t, C["s18.d"] + 1.0, "x = −1 − 2i", 1320, 760, 84, CERTO)
    nota(c, t, C["s18.d"] + 2.0, "um par de conjugados", W / 2, 960, 56, TINTA2, "i", "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s19.a"], [("i² = −1", "g", 72, COR)]),
             (C["s19.b"], ps("raiz de negativo", "i", 72) + ps("vira i", "g", 72, COR)),
             (C["s19.c"], ps("Bhaskara", "g", 72, COR) + ps("continua funcionando", "i", 72)))
    fim_padrao(c, t, C, "s19", "s20", itens, "próxima aula:", "raízes complexas vêm em pares",
               extra=lambda: form(c, t, C["s20.b"], "1 + 2i   e   1 − 2i", XE, 560, 100, TINTA2), k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, numero_i=b_numero_i, resolver=b_resolver, multiplicar=b_multiplicar,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
