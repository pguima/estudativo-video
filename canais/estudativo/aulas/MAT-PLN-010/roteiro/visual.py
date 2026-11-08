"""Visual — Estudativo · MAT-PLN-010: praticando raízes complexas (prática, quatro questões inéditas).
1) x² − 6x + 10 = 0 (3 ± i, conferido pelo atalho do par); 2) x³ − 1 = 0 (Briot-Ruffini com o 1 e Bhaskara: (−1 ± i√3)/2);
3) 2 + i raiz de x³ − 5x² + 9x − 5 (par x² − 4x + 5 e o teste do 1); 4) x⁴ − 16 = 0 (±2 e ±2i); no palco, contar as raízes.
Convenções da trilha em MAT-PLN-001 a 009 (tabela, esferas de raiz, o i em âmbar). Práticas: etiqueta "questão n" e relógio.
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-010_praticando_raizes_complexas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "atalho", "fim"))
IM = "#B86E00"


def _P(c, x):
    r = 0
    for k in c:
        r = r * x + k
    return r


# as contas da aula
_i = 1j
assert 36 - 40 == -4 and all(abs(_P([1, -6, 10], z)) < 1e-12 for z in (3 + _i, 3 - _i)) and 3 ** 2 + 1 ** 2 == 10
assert 1 - 4 == -3 and all(abs(_P([1, 0, 0, -1], z)) < 1e-12 for z in (1, (-1 + _i * 3 ** 0.5) / 2, (-1 - _i * 3 ** 0.5) / 2))
assert all(abs(_P([1, -5, 9, -5], z)) < 1e-12 for z in (2 + _i, 2 - _i, 1)) and 1 - 5 + 9 - 5 == 0 and 2 ** 2 + 1 == 5
assert all((x * x - 4 * x + 5) * (x - 1) == x ** 3 - 5 * x * x + 9 * x - 5 for x in range(-4, 5))
assert all(abs(_P([1, 0, 0, 0, -16], z)) < 1e-12 for z in (2, -2, 2 * _i, -2 * _i))


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



def raiz_bola(c, t, t0, s, cx, cy, r=70, size=60, cor=CERTO):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.6)), cor, a),
                                     formula(c, s, cx, cy + size * 0.36, size, BR, a, "center")))


def enunciado(c, t, C, sid, pid, n, rot, linhas):
    etiqueta(c, t, C[sid + ".a"], n, rot)
    for t0, s, y, size in linhas:
        if callable(s):
            E.foco(c, t, t0, 0.5, s)
        else:
            form(c, t, t0, s, XE, y, size)
    E.relogio(c, t, C[pid + ".a"], 1560, 560, 170)


# ---------------- abertura ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], ps("quatro questões", "g", 120, COR), XE, 360)
    E.frase(c, t, C["s01.a"] + 1.0, ps("raízes reais e complexas", "i", 90), XE, 500, passo=0.12)
    for k, s in enumerate(("2", "−2", "2i", "−2i")):
        raiz_bola(c, t, C["s01.a"] + 1.8 + 0.2 * k, s, XE + 70 + 200 * k, 680, 70, 54, IM if "i" in s else CERTO)
    E.foco(c, t, C["s01.b"], 0.6, lambda a: E.bola(c, 1520, 520, 230 * ease_back(prog(t, C["s01.b"], 0.6))), blur=0)
    E.foco(c, t, C["s01.b"] + 0.3, 0.5, lambda a: (centro(c, "pause e", 1520, 500, 70, "i", BR, a), centro(c, "resolva", 1520, 580, 70, "g", BR, a)))


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 84), XE, 190)
    itens = (("s02.a", "i² = −1", None), ("s02.b", "conjugado:", "só o sinal do i muda"),
             ("s02.c", "Briot-Ruffini:", "baixa o grau"), ("s02.d", "o par:", "vira um fator de grau 2"))
    for k, (cue, nome, desc) in enumerate(itens):
        y = 340 + 150 * k
        E.foco(c, t, C[cue], 0.45, lambda p, k=k, y=y: num_bola(c, str(k + 1), XE + 40, y - 22, 40, 50, p))
        E.frase(c, t, C[cue], ps(nome, "g", 62, COR) + (ps(desc, "i", 62) if desc else []), XE + 110, y, passo=0.08)
    form(c, t, C["s02.d"] + 1.6, "a ± bi   →   x^2 − 2ax + (a^2 + b^2)", XE + 110, 1000 - 60, 64, TINTA2)


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    enunciado(c, t, C, "s03", "s04", 1, "delta negativo", [
        (C["s03.a"] + 0.6, lambda a: E.escreve(c, "resolva", XE, 400, 76, "i", TINTA, a), 0, 0),
        (C["s03.b"], "x^2 − 6x + 10 = 0", 600, 110),
    ])


def b_resposta1(c, t, C, b):
    def s05():
        form(c, t, C["s05"] + 0.1, "x^2 − 6x + 10 = 0", W / 2, 190, 96, TINTA2, "center")
        form(c, t, C["s05.a"], "Δ = 36 − 40 = −4", XE, 380, 100)
        form(c, t, C["s05.b"], "r{−4} = 2i", 1100, 380, 100, IM)
        form(c, t, C["s05.c"], "x = f{6 ± 2i}{2}", XE, 620, 120)
        pil(c, t, C["s05.d"], "x = 3 + i", 1000, 600, 76, CERTO)
        pil(c, t, C["s05.d"] + 0.6, "x = 3 − i", 1500, 600, 76, CERTO)
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    nota(c, t, C["s06"] + 0.1, "confira pelo atalho do par", XE, 220, 64, TINTA2)
    form(c, t, C["s06"] + 0.4, "3 ± i", XE + 640, 222, 76, IM)
    form(c, t, C["s06.a"], "−2 · 3 = −6   →   −6x", XE, 420, 100)
    form(c, t, C["s06.b"], "3^2 + 1^2 = 10", XE, 600, 100, IM)
    form(c, t, C["s06.c"], "x^2 − 6x + 10", W / 2, 840, 130, CERTO, "center")
    E.foco(c, t, C["s06.c"] + 1.0, 0.45, lambda a: E.selo(c, 1560, 800, 50, True, a))


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    enunciado(c, t, C, "s07", "s08", 2, "grau três", [
        (C["s07.a"] + 0.6, lambda a: E.escreve(c, "ache todas as raízes de", XE, 400, 72, "i", TINTA, a), 0, 0),
        (C["s07.b"], "x^3 − 1 = 0", 600, 130),
    ])


def b_resposta2(c, t, C, b):
    def s09():
        form(c, t, C["s09.a"], "1^3 − 1 = 0:  1 é raiz", XE, 200, 80, CERTO)
        ks = "cdef"
        tb = [C["s09.c"] + 0.3] + [entre(C[f"s09.{ks[i]}"], C[f"s09.{ks[i + 1]}"] if i < 3 else C["s09.end"] - 0.3, 0.7) for i in range(1, 4)]
        briot(c, t, 1, [1, 0, 0, -1], C["s09.b"], tb, 520, 480, 230, 116, tr=tb[-1], falta=(1, 2))
    fase(c, t, C["s09"], C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    form(c, t, C["s10.a"], "x^2 + x + 1 = 0", XE, 220, 100, COR)
    form(c, t, C["s10.b"], "Δ = 1 − 4 = −3", XE, 400, 96)
    form(c, t, C["s10.c"], "r{−3} = i r{3}", 1050, 400, 96, IM)
    form(c, t, C["s10.d"], "x = f{−1 ± i r{3}}{2}", XE, 660, 120)
    raiz_bola(c, t, C["s10.e"], "1", 1050, 640, 80, 70)
    E.foco(c, t, C["s10.e"] + 0.3, 0.5, lambda a: E.pilula(c, "+ um par de complexas", 1460, 640, 56, estilo="g", fundo=IM, cor=BR, a=a), sobe=8)
    nota(c, t, C["s10.e"] + 0.6, "1 real + 2 complexas = 3 raízes", W / 2, 920, 60, TINTA2, "i", "center")


# ---------------- questão 3 ----------------
def b_questao3(c, t, C, b):
    enunciado(c, t, C, "s11", "s12", 3, "raiz complexa dada", [
        (C["s11.b"], "2 + i  é raiz de", 400, 90),
        (C["s11.b"] + 0.8, "x^3 − 5x^2 + 9x − 5", 580, 110),
        (C["s11.c"], lambda a: E.escreve(c, "ache as outras raízes", XE, 780, 76, "g", COR, a), 0, 0),
    ])


def b_resposta3(c, t, C, b):
    def s13():
        form(c, t, C["s13.a"], "conjugado:  2 − i", XE, 220, 100, IM)
        form(c, t, C["s13.b"], "−2 · 2 = −4   →   −4x", XE, 420, 96)
        form(c, t, C["s13.c"], "2^2 + 1^2 = 5", XE, 580, 96, IM)
        form(c, t, C["s13.d"], "par:  x^2 − 4x + 5", W / 2, 820, 130, CERTO, "center")
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    form(c, t, C["s14.a"], "P(1) = 1 − 5 + 9 − 5 = 0", XE, 220, 100)
    E.foco(c, t, C["s14.b"], 0.45, lambda a: E.pilula(c, "1 é raiz", 1500, 190, 60, estilo="g", fundo=CERTO, cor=BR, a=a), sobe=8)
    for k, (s, cor) in enumerate((("2 + i", IM), ("2 − i", IM), ("1", CERTO))):
        raiz_bola(c, t, C["s14.c"] + 0.4 * k, s, 560 + 400 * k, 480, 110, 64, cor)
    nota(c, t, entre(C["s14.c"], C["s14.d"], 0.7), "se o 1 não fosse raiz: divida pelo par", W / 2, 700, 56, TINTA2, "i", "center")
    form(c, t, C["s14.d"], "(x^2 − 4x + 5)(x − 1) = x^3 − 5x^2 + 9x − 5", W / 2, 900, 80, CERTO, "center")


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    enunciado(c, t, C, "s15", "s16", 4, "grau quatro", [
        (C["s15.a"] + 0.6, lambda a: E.escreve(c, "ache todas as raízes de", XE, 400, 72, "i", TINTA, a), 0, 0),
        (C["s15.b"], "x^4 − 16 = 0", 600, 130),
    ])


def b_resposta4(c, t, C, b):
    def s17():
        form(c, t, C["s17"] + 0.1, "x^4 − 16 = 0", W / 2, 190, 100, TINTA2, "center")
        form(c, t, C["s17.a"], "x^4 = (x^2)^2      16 = 4^2", W / 2, 420, 100, align="center")
        pil(c, t, C["s17.b"], "diferença de dois quadrados", W / 2, 580, 56, TINTA)
        form(c, t, C["s17.b"] + 0.6, "(x^2 + 4)(x^2 − 4) = 0", W / 2, 800, 120, COR, "center")
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    form(c, t, C["s18"] + 0.1, "(x^2 + 4)(x^2 − 4) = 0", W / 2, 180, 96, TINTA2, "center")
    form(c, t, C["s18.a"], "x^2 − 4 = 0:   x = 2  ou  x = −2", XE, 380, 90)
    form(c, t, C["s18.b"], "x^2 + 4 = 0:   x^2 = −4", XE, 560, 90)
    form(c, t, C["s18.c"], "x = 2i  ou  x = −2i", XE + 420, 700, 90, IM)
    for k, (s, cor) in enumerate((("2", CERTO), ("−2", CERTO), ("2i", IM), ("−2i", IM))):
        raiz_bola(c, t, C["s18.c"] + 1.0 + 0.3 * k, s, 520 + 300 * k, 900, 80, 60, cor)
    nota(c, t, C["s18.d"], "só 2 e −2? faltaram as complexas", 1500, 1020, 50, ERRADO, "i", "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s19.a"], ps("conte as raízes", "g", 96, BR) + ps("antes de começar", "i", 90, CLARO), W / 2, 210, "center", passo=0.12)
    nota(c, t, C["s19.a"] + 1.4, "grau = número de raízes;  as com i vêm em pares", W / 2, 320, 56, CLARO, "i", "center")
    E.frase(c, t, C["s19.b"], ps("grau 4:", "g", 84, BR) + ps("quatro raízes", "i", 88, CLARO), W / 2, 480, "center", passo=0.12)
    for k, (s, cor) in enumerate((("2", CERTO), ("−2", CERTO), ("2i", IM), ("−2i", IM))):
        raiz_bola(c, t, C["s19.c"] + 0.3 * k, s, 520 + 300 * k, 680, 80, 60, cor)
    E.foco(c, t, C["s19.d"], 0.45, lambda a: E.pilula(c, "a contagem não fechou? falta raiz", W / 2, 900, 62, estilo="g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 220, "center")
        itens = ((C["s20.a"], ps("delta negativo", "i", 72) + ps("pede i", "g", 72, COR)),
                 (C["s20.b"], ps("raiz complexa traz", "i", 72) + ps("o conjugado", "g", 72, COR)),
                 (C["s20.c"], ps("o grau diz", "i", 72) + ps("quantas raízes há", "g", 72, COR)))
        for k, (tk, partes) in enumerate(itens):
            yy = 430 + k * 200
            E.foco(c, t, tk, 0.5, lambda p, k=k, yy=yy: num_bola(c, str(k + 1), 230, yy - 30, 58, 66, p))
            E.frase(c, t, tk + 0.1, partes, 320, yy, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.2, ps("você fecha", "i", 84), XE, 300, passo=0.1)
    E.frase(c, t, C["s21.a"], ps("a trilha de polinômios", "g", 100, COR), XE, 450, passo=0.12)
    ci = C["s21.b"]
    E.foco(c, t, ci, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1500, 640, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, ci + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1640, p), lerp(930, 685, p), ep(t, ci + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s21.c"], ps("bons", "i", 120) + ps("estudos!", "i", 120, COR), W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              atalho=b_atalho, fim=b_fim)
