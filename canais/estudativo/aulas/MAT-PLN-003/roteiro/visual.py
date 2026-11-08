"""Visual — Estudativo · MAT-PLN-003: dispositivo de Briot-Ruffini.
x³ − 2x² − 5x + 6 por x − 1 na tabela (quociente x² − x − 6, resto 0), o termo que falta entra com zero
(x³ − 4x + 5 por x + 2, resto 5), o erro de pular o zero (resto 17) e, no palco, a tabela calculando P(3) = 0.
Convenções da trilha em MAT-PLN-001. Nova: TABELA (briot) = número que zera o divisor à esquerda da barra, coeficientes em cima,
resultados embaixo; a seta "× número" leva cada resultado à coluna seguinte; o resto fica numa caixa (verde se for zero);
coeficiente zero do termo que falta em âmbar. Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-003_briot_ruffini.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("montar", "falta", "atalho", "questao", "fim"))


def _P(c, x):
    r = 0
    for k in c:
        r = r * x + k
    return r


def _briot(c, a):
    out = [c[0]]
    for k in c[1:]:
        out.append(out[-1] * a + k)
    return out


# as contas da aula (a tabela refaz cada uma; aqui, a conferência)
assert _briot([1, -2, -5, 6], 1) == [1, -1, -6, 0] and _P([1, -2, -5, 6], 1) == 0
assert _briot([1, 0, -4, 5], -2) == [1, -2, 0, 5] and _P([1, 0, -4, 5], -2) == 5
assert _briot([1, -4, 5], -2) == [1, -6, 17]
assert _briot([1, -2, -5, 6], 3) == [1, 1, -2, 0] and _P([1, -2, -5, 6], 3) == 0
assert _briot([2, 0, -3, 1], 1) == [2, 2, -1, 0] and _P([2, 0, -3, 1], 1) == 0


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



TX, TY, CW, TS = 430, 480, 230, 116  # a tabela principal


def tb_de(C, sid, ks, f=0.78):
    """instante de cada resultado: perto do fim da fala de cada marcador"""
    out = []
    for i, k in enumerate(ks):
        t0 = C[f"{sid}.{k}"]
        t1 = C[f"{sid}.{ks[i + 1]}"] if i + 1 < len(ks) else C[f"{sid}.end"] - 0.4
        out.append(t0 + 0.3 if i == 0 else entre(t0, t1, f))
    return out


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        form(c, t, C["s01.a"], "(x^3 − 2x^2 − 5x + 6) ÷ (x − 1)", W / 2, 240, 110, align="center")
        pil(c, t, C["s01.b"], "chave: 3 rodadas de dividir, multiplicar e subtrair", W / 2, 400, 50, TINTA)
        k = C["s01.c"]
        briot(c, t, 1, [1, -2, -5, 6], k, [k + 0.6, k + 1.0, k + 1.4, k + 1.8], 560, 640, 220, 104, tr=k + 2.2, mostra_conta=False)
        pil(c, t, k + 2.4, "vinte segundos", W / 2, 990, 60)
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], None, [(ps("dividir", "i", 96), 1.0),
                                           (ps("só com os", "i", 96) + ps("coeficientes", "g", 96, COR), 1.6),
                                           (ps("Briot-Ruffini", "g", 120, COR), 3.0)])
        E.foco(c, t, C["s02.b"], 0.6, lambda a: E.bola(c, 1520, 520, 240 * ease_back(prog(t, C["s02.b"], 0.6))), blur=0)
        E.foco(c, t, C["s02.b"] + 0.3, 0.5, lambda a: (centro(c, "a tabelinha", 1520, 500, 64, "i", BR, a),
                                                      centro(c, "da divisão", 1520, 580, 64, "g", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("divisão:", "g", 64, COR) + ps("polinômio = divisor · quociente + resto", "i", 64), "x^2 + 3x + 5 = (x − 1)(x + 4) + 9"),
        (C["s03.c"], ps("teorema do resto:", "g", 64, COR) + ps("resto por (x − a) é P(a)", "i", 64), "resto por (x − 1) = P(1) = 9"),
    ])


# ---------------- a tabela: montar, regra e leitura ----------------
def tabela(c, t, C, tb, tr=None):
    briot(c, t, 1, [1, -2, -5, 6], (C["s04.b"], C["s04.d"]), tb, TX, TY, CW, TS, tr=tr)


def topo(c, t, C):
    form(c, t, C["s04"] + 0.1, "(x^3 − 2x^2 − 5x + 6) ÷ (x − 1)", W / 2, 170, 90, TINTA2, "center")


def b_montar(c, t, C, b):
    topo(c, t, C)
    tabela(c, t, C, [1e9] * 4)
    nota(c, t, C["s04.a"], "o número que zera o divisor", 560, TY + 300, 54, COR, "g", "center")
    if t >= C["s04.a"]:
        p = ep(t, C["s04.a"] + 0.3, 0.5)
        M.arrow(c, 420, TY + 250, TX - 80, TY + 40, COR, p, 5, 16, p)
    E.foco(c, t, C["s04.c"], 0.5, lambda a: E.chave(c, TX + 20, TX + CW * 4 - 20, TY - TS - 30, COR, a, h=-24))
    nota(c, t, C["s04.c"], "coeficientes, do maior expoente para o menor", TX + CW * 2, TY - TS - 80, 50, COR, "g", "center")


def b_regra(c, t, C, b):
    topo(c, t, C)
    tb = tb_de(C, "s06", "abcd")
    tabela(c, t, C, tb)
    pil(c, t, C["s05.a"], "1. baixe o primeiro", 560, 890, 54)
    pil(c, t, C["s05.b"], "2. × número da esquerda, + o próximo", 1200, 990, 54, TINTA)
    contas = ((None, None), ("1 · 1 = 1", "−2 + 1 = −1"), ("−1 · 1 = −1", "−5 + (−1) = −6"), ("−6 · 1 = −6", "6 + (−6) = 0"))
    for i, k in enumerate("bcd"):
        t0, t1 = C[f"s06.{k}"], (C[f"s06.{'bcd'[i + 1]}"] if i < 2 else 1e9)
        a1, a2 = contas[i + 1]

        def mostra(a1=a1, a2=a2, t0=t0, i=i):
            form(c, t, t0, a1, 1420, TY + 40, 66, TINTA2)
            form(c, t, tb[i + 1] - 0.3, a2, 1420, TY + 160, 66, COR)
        fase(c, t, t0, t1 - 0.1, mostra)


def b_ler(c, t, C, b):
    topo(c, t, C)
    tabela(c, t, C, [0] * 4, tr=C["s07.a"])
    yb = TY + TS * 1.55
    nota(c, t, C["s07.a"] + 0.2, "resto", TX + CW * 3.5, yb + 130, 56, CERTO, "g", "center")
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.chave(c, TX + 20, TX + CW * 3 - 20, yb + 50, COR, a, h=24))
    nota(c, t, C["s07.b"] + 0.3, "coeficientes do quociente", TX + CW * 1.5, yb + 140, 56, COR, "g", "center")
    pil(c, t, C["s07.c"], "grau 3  →  grau 2", 360, 300, 50, TINTA)
    form(c, t, C["s07.d"], "quociente: x^2 − x − 6", W / 2, 1000, 90, COR, "center")
    if t >= C["s08"]:
        E.foco(c, t, C["s08.a"], 0.45, lambda a: M.rrect(c, 1350, 300, 520, 260, 30, CERTO, 0.1 * a))
        form(c, t, C["s08.a"], "P(1) = 1 − 2 − 5 + 6", 1380, 390, 56, TINTA)
        form(c, t, C["s08.a"] + 1.4, "= 0", 1380, 480, 64, CERTO)
        E.foco(c, t, C["s08.b"], 0.45, lambda a: E.selo(c, 1780, 470, 40, True, a))


# ---------------- termo que falta ----------------
def b_falta(c, t, C, b):
    form(c, t, C["s09.a"], "(x^3 − 4x + 5) ÷ (x + 2)", W / 2, 170, 96, align="center")
    tb = tb_de(C, "s10", "abcd")
    briot(c, t, -2, [1, 0, -4, 5], (C["s09.b"], C["s09.d"]), tb, TX, TY, CW, TS, tr=C["s11.c"], falta=(1,))
    pil(c, t, C["s09.c"], "falta x²: coeficiente zero", TX + CW * 1.5, 285, 50, "#B86E00")
    contas = (("1 · (−2) = −2", "0 + (−2) = −2"), ("−2 · (−2) = 4", "−4 + 4 = 0"), ("0 · (−2) = 0", "5 + 0 = 5"))
    for i, k in enumerate("bcd"):
        t0, t1 = C[f"s10.{k}"], (C[f"s10.{'bcd'[i + 1]}"] if i < 2 else C["s11"])
        a1, a2 = contas[i]

        def mostra(a1=a1, a2=a2, t0=t0, i=i):
            form(c, t, t0, a1, 1420, TY + 40, 66, TINTA2)
            form(c, t, tb[i + 1] - 0.3, a2, 1420, TY + 160, 66, COR)
        fase(c, t, t0, t1 - 0.1, mostra)
    if t >= C["s11"]:
        form(c, t, C["s11.a"], "x^2 − 2x + 0", XE + 60, 920, 90, TINTA2)
        form(c, t, C["s11.b"], "= x^2 − 2x", XE + 60 + fw("x^2 − 2x + 0 ", 90), 920, 90, COR)
        nota(c, t, C["s11.c"], "resto 5", 1600, 940, 64, COR, "g", "center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 100, ERRADO)] + ps("com o zero", "i", 96), W / 2, 170, "center")
    k = C["s12.b"]
    briot(c, t, -2, [1, -4, 5], k, [k + 0.8, k + 1.3, C["s12.c"]], 360, 420, 220, 104, tr=C["s12.c"], cor_resto=ERRADO, mostra_conta=False)
    nota(c, t, C["s12.a"], "pulou o zero do x²", 690, 760, 56, ERRADO, "g", "center")
    form(c, t, C["s12.d"], "P(−2) = −8 + 8 + 5 = 5", 1080, 450, 72, CERTO)
    E.foco(c, t, C["s12.d"] + 1.0, 0.45, lambda a: E.selo(c, 1400, 600, 44, True, a))
    pil(c, t, C["s12.e"], "termo que falta entra com zero, sempre", W / 2, 940, 58)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13.a"], ps("último número =", "i", 80, CLARO) + ps("P(número da esquerda)", "g", 74, BR), W / 2, 170, "center", passo=0.12)
        E.frase(c, t, C["s13.b"], ps("valor de polinômio", "i", 70, CLARO) + ps("só com × e +", "g", 66, BR), W / 2, 290, "center", passo=0.12)
        form(c, t, C["s13.c"], "P(3)  em  x^3 − 2x^2 − 5x + 6", W / 2, 430, 84, CLARO, "center")
        d, e = C["s13.d"], C["s13.e"]
        tb = [entre(d, e, f) for f in (0.08, 0.38, 0.68)] + [e]
        briot(c, t, 3, [1, -2, -5, 6], C["s13.c"] + 0.8, tb, 560, 650, 220, 104, tr=e, escuro=True)
        E.foco(c, t, e + 0.3, 0.45, lambda a: E.pilula(c, "P(3) = 0", 1690, 830, 64, estilo="g", fundo=CERTO, cor=BR, a=a))
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("porque o resto da divisão por", "i", 80, CLARO), W / 2, 330, "center", passo=0.1)
    form(c, t, C["s14.a"] + 0.6, "x − 3   é   P(3)", W / 2, 490, 120, BR, "center")
    E.frase(c, t, C["s14.b"], ps("não serve para", "i", 76, CLARO) + ps("2x − 1:", "g", 72, BR) + ps("use a chave", "i", 76, CLARO), W / 2, 780, "center", passo=0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s15", "s16", [
        (C["s15.a"] - 0.4, lambda a: E.escreve(c, "divida", XE, 400, 72, "i", TINTA, a), 0, 0),
        (C["s15.a"], "2x^3 − 3x + 1", 560, 130),
        (C["s15.b"] - 0.3, lambda a: E.escreve(c, "por", XE, 740, 72, "i", TINTA, a), 0, 0),
        (C["s15.b"], "x − 1", 900, 130),
    ], cx=1500)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    tb = tb_de(C, "s17", "cdef")
    briot(c, t, 1, [2, 0, -3, 1], (C["s17.a"], C["s17.b"]), tb, TX, 360, CW, TS, tr=C["s18.b"], falta=(1,))
    nota(c, t, C["s17.b"] - 0.6, "falta x²", TX + CW * 1.5, 170, 54, "#B86E00", "g", "center")
    form(c, t, C["s18.a"], "quociente: 2x^2 + 2x − 1", XE, 760, 96, COR)
    pil(c, t, C["s18.b"], "divisão exata", 1620, 560, 56, CERTO)
    form(c, t, C["s18.c"], "P(1) = 2 − 3 + 1 = 0", XE, 920, 90, CERTO)
    E.foco(c, t, C["s18.c"] + 1.2, 0.45, lambda a: E.selo(c, 1120, 890, 44, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s19.a"], ps("à esquerda,", "i", 72) + ps("o número que zera o divisor", "g", 64, COR)),
             (C["s19.b"], ps("coeficientes com", "i", 72) + ps("zero no que falta", "g", 72, COR)),
             (C["s19.c"], ps("baixe,", "g", 72, COR) + ps("multiplique e some", "i", 72)))
    fim_padrao(c, t, C, "s19", "s20", itens, "próxima aula: uma raiz quebra o polinômio", "raízes e forma fatorada",
               extra=lambda: form(c, t, C["s20.b"], "(x − 1)(x − 3)(x + 2)", XE, 580, 90, TINTA2), k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, montar=b_montar, regra=b_regra, ler=b_ler, falta=b_falta, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
