"""Visual — Estudativo · MAT-PLN-002: divisão de polinômios pela chave e teorema do resto.
x² + 3x + 5 dividido por x − 1 na chave (quociente x + 4, resto 9), a conferência, o erro de não trocar os sinais,
o teorema do resto P(1) = 9 e, no palco, o atalho da divisibilidade (x³ − 8 por x − 2).
Convenções da trilha em MAT-PLN-001. Nova: CHAVE = dividendo em colunas por expoente, divisor à direita da barra,
quociente embaixo dela; o produto entra como se escreve (x² − x) e troca de sinal no lugar ao subtrair (−x² + x, na cor da matéria).
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-002_divisao_de_polinomios.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "chave", "teorema", "atalho", "questao", "fim"))


def _P(c, x):
    r = 0
    for k in c:
        r = r * x + k
    return r


# as contas da aula
assert _P([1, 3, 5], 1) == 9 and 17 == 5 * 3 + 2
assert all((x - 1) * (x + 4) + 9 == x * x + 3 * x + 5 for x in range(-5, 6))
assert all((x - 1) * (x + 2) + 3 == x * x + x + 1 for x in range(-5, 6))  # o erro de não trocar os sinais
assert _P([1, 0, 0, -8], 2) == 0
assert _P([1, 2, 0, -5], -2) == -5 and _P([1, 2, 0, -5], 2) == 11


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



# ---------------- a chave ----------------
CX = (500, 800, 1040)  # borda direita das colunas x², x e número
YR = (330, 460, 600, 730, 870)  # linhas: dividendo, produto, sobra, produto, resto
SZ = 110
XB = 1130  # barra da chave


def chave_base(c, t, t0, divisor="x − 1"):
    a = ep(t, t0, 0.5)
    if a > 0:
        M.line(c, XB, YR[0] - 110, XB, YR[0] + 40, TINTA, a, 6)
        M.line(c, XB, YR[0] + 40, XB + 440 * a, YR[0] + 40, TINTA, a, 6)
    form(c, t, t0, divisor, XB + 40, YR[0], SZ)


def cols(c, t, t0, partes, y, cor=None, dt=0.15, size=SZ):
    for k, s in enumerate(partes):
        if s:
            form(c, t, t0 + dt * k, s, CX[k], y, size, cor, "right")


def troca(c, t, t0, t1, antes, depois, y, cor_depois=None):
    """produto escrito como sai da conta (antes) e, em t1, com os sinais trocados (depois), no lugar"""
    if t < t0:
        return
    if t < t1 + 0.45:
        E.saida(c, t, t1, lambda: cols(c, t, t0, antes, y, TINTA2))
    if t >= t1:
        cols(c, t, t1, depois, y, cor_depois or COR, dt=0.05)


def risca(c, t, t0, y, x0=CX[0] - 330, x1=CX[2] + 20):
    p = ep(t, t0, 0.5)
    if p > 0:
        M.line(c, x0, y + 40, x0 + (x1 - x0) * p, y + 40, TINTA, 1.0, 5)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        form(c, t, C["s01.a"], "(x^2 + 3x + 5) ÷ (x − 1)", W / 2, 360, 130, align="center")
        form(c, t, C["s01.b"], "quociente  x + 4", 560, 600, 96, TINTA2, "center")
        form(c, t, C["s01.b"] + 0.8, "resto  9", 1300, 600, 96, COR, "center")
        E.frase(c, t, C["s01.c"], ps("o 9 sai em", "i", 84) + ps("3 segundos,", "g", 78, COR) + ps("sem dividir", "i", 84), W / 2, 860, "center", passo=0.12)
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], C["s02.b"], [(ps("dividir", "g", 120, COR), 1.0),
                                                 (ps("polinômios", "g", 120, COR), 1.3),
                                                 (ps("e achar o resto", "i", 96), 2.0)])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("valor numérico:", "g", 64, COR) + ps("troque o x pelo número", "i", 64), "P(1) = 1^2 + 3 · 1 + 5"),
        (C["s03.c"], ps("divisão com resto:", "g", 64, COR) + ps("17 ÷ 5 dá 3 e sobram 2", "i", 64), None),
    ])


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    def s04():
        form(c, t, C["s04.a"], "17 = 5 · 3 + 2", W / 2, 360, 150, align="center")
        S = "17 = 5 · 3 + 2"
        nomes = (("17", "dividendo"), ("5", "divisor"), ("3", "quociente"), ("2", "resto"))
        for k, (tr, nome) in enumerate(nomes):
            x0, w = trecho_x(S, tr, W / 2, 150, "center")
            nota(c, t, C["s04.b"] + 0.4 * k, nome, x0 + w / 2, 480 + 80 * (k % 2), 50, (COR, TINTA, TINTA, CERTO)[k], "g", "center")
        E.frase(c, t, C["s04.c"], ps("o resto é", "i", 80) + ps("menor que o divisor:", "g", 74, COR) + ps("2 < 5", "g", 74), W / 2, 760, "center", passo=0.12)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    form(c, t, C["s05.a"], "P(x) = divisor · quociente + resto", W / 2, 330, 96, align="center")
    E.frase(c, t, C["s05.b"], ps("resto de", "i", 80) + ps("grau menor", "g", 74, COR) + ps("que o divisor", "i", 80), W / 2, 520, "center", passo=0.12)
    form(c, t, C["s05.c"] - 1.6, "x − 1", 560, 740, 120, align="center")
    nota(c, t, C["s05.c"] - 1.2, "grau 1", 560, 840, 56, TINTA2, "g", "center")
    M.arrow(c, 760, 700, 1040, 700, FIO, ep(t, C["s05.c"], 0.5), 5, 16, ep(t, C["s05.c"], 0.5))
    pil(c, t, C["s05.c"] + 0.2, "resto: só um número", 1420, 715, 60)


# ---------------- a chave ----------------
def b_chave(c, t, C, b):
    chave_base(c, t, C["s06.a"])
    cols(c, t, C["s06.a"] + 0.3, ("x^2", "+ 3x", "+ 5"), YR[0])
    # os três passos, à direita
    passos = (("s06.c", "dividir"), ("s06.c", "multiplicar"), ("s06.c", "subtrair"))
    vez = [C["s07.a"], C["s07.c"], C["s08.a"], C["s09.a"], C["s09.b"], C["s09.c"]]
    k_vez = None
    for i, tv in enumerate(vez):
        if t >= tv - 0.1:
            k_vez = i % 3
    if t < C["s10"] - 0.1:
        for k, (cue, nome) in enumerate(passos):
            y = 640 + k * 120
            ativo = k_vez == k
            E.foco(c, t, C[cue] + 0.35 * k, 0.45, lambda p, k=k, y=y, ativo=ativo: num_bola(c, str(k + 1), 1240, y - 20, 36, 44, p, COR if ativo or k_vez is None else CINZA))
            E.frase(c, t, C[cue] + 0.35 * k + 0.1, [(nome, "g" if ativo else "i", 64, COR if ativo else TINTA)], 1300, y, passo=0.1)
    # 1ª rodada
    form(c, t, C["s07.b"], "x", XB + 40, YR[0] + 150, SZ, COR)
    realce(c, t, C["s07.a"], "x^2", "x^2", CX[0], YR[0], SZ, COR, "right", t1=C["s07.c"])
    realce(c, t, C["s07.a"], "x − 1", "x", XB + 40, YR[0], SZ, COR, t1=C["s07.c"])
    troca(c, t, C["s07.c"], C["s08.a"], ("x^2", "− x", None), ("−x^2", "+ x", None), YR[1])
    risca(c, t, C["s08.b"], YR[1])
    if t >= C["s08.b"]:
        x0, w = CX[0] - fw("x^2", SZ), fw("x^2", SZ)
        E.risco(c, x0 - 70, YR[1] + 15, x0 + w + 10, YR[0] - 95, t, C["s08.b"], COR, 7)
    cols(c, t, C["s08.c"], (None, "4x", None), YR[2])
    cols(c, t, C["s08.d"], (None, None, "+ 5"), YR[2])
    if t >= C["s08.d"]:
        flecha(c, t, C["s08.d"], CX[2] - 40, YR[0] + 20, CX[2] - 40, YR[2] - 90, 0.001, FIO, 0.4, 4)
    # 2ª rodada
    form(c, t, C["s09.a"], "+ 4", XB + 40 + fw("x ", SZ), YR[0] + 150, SZ, COR)
    troca(c, t, C["s09.b"], C["s09.c"], (None, "4x", "− 4"), (None, "−4x", "+ 4"), YR[3])
    risca(c, t, C["s09.c"] + 0.4, YR[3], CX[1] - 260)
    cols(c, t, C["s09.c"] + 0.8, (None, None, "9"), YR[4], CERTO)
    # fim da conta e conferência
    if t >= C["s10"]:
        pil(c, t, C["s10.a"], "9 não tem x: a conta para", 640, 1000, 50, TINTA)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.caixa_pontilhada(c, CX[2] - 120, YR[4] - 115, 150, 150, a, CERTO))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.caixa_pontilhada(c, XB + 20, YR[0] + 50, 300, 140, a, COR))
        form(c, t, C["s10.c"], "(x − 1)(x + 4)", 1210, 650, 70)
        form(c, t, C["s10.c"] + 0.7, "= x^2 + 3x − 4", 1210, 760, 70)
        form(c, t, C["s10.d"], "+ 9 = x^2 + 3x + 5", 1210, 880, 70, CERTO)
        E.foco(c, t, C["s10.d"] + 1.0, 0.45, lambda a: E.selo(c, 1560, 990, 46, True, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 110, ERRADO)] + ps("ao subtrair", "i", 100), W / 2, 190, "center")
    def s11():
        form(c, t, C["s11.a"], "3x − (−x)", 380, 420, 120)
        form(c, t, C["s11.b"], "= 2x", 380 + fw("3x − (−x) ", 120), 420, 120, ERRADO)
        if t > C["s11.b"] + 1.4:
            x0 = 380 + fw("3x − (−x) = ", 120)
            E.risco(c, x0 - 10, 440, x0 + fw("2x", 120) + 10, 320, t, C["s11.b"] + 1.4, largura=12)
        form(c, t, C["s11.b"] + 1.6, "= 4x", 1250, 420, 120, CERTO)
        form(c, t, C["s11.c"], "quociente x + 2,  resto 3", W / 2, 640, 96, ERRADO, "center")
    fase(c, t, C["s11"], 1e9, s11)
    form(c, t, C["s12.a"], "(x − 1)(x + 2) + 3 = x^2 + x + 1", W / 2, 820, 84, align="center")
    E.foco(c, t, C["s12.a"] + 1.2, 0.45, lambda a: E.selo(c, 1720, 790, 46, False, a))
    form(c, t, C["s12.a"] + 1.4, "e não x^2 + 3x + 5", 1500, 900, 56, ERRADO, "center")
    pil(c, t, C["s12.b"], "subtrair o parêntese = trocar todos os sinais", W / 2, 980, 50, TINTA)


# ---------------- teorema do resto ----------------
def b_teorema(c, t, C, b):
    def s13():
        E.frase(c, t, C["s13"] + 0.1, ps("e o resto", "i", 84) + ps("sem dividir?", "g", 78, COR), XE, 190, passo=0.12)
        S = "P(x) = (x − 1) · Q + R"
        form(c, t, C["s13.a"], S, W / 2, 400, 120, align="center")
        nota(c, t, C["s13.a"] + 1.0, "Q = quociente,  R = resto", W / 2, 500, 54, TINTA2, "i", "center")
        pil(c, t, C["s13.b"], "x = 1", 560, 650, 64)
        S2, X2 = "P(1) = (1 − 1) · Q + R", 780
        form(c, t, C["s13.c"] - 0.3, S2, X2, 800, 110, align="center")
        realce(c, t, C["s13.c"], S2, "(1 − 1) · Q", X2, 800, 110, COR, "center")
        x0, w = trecho_x(S2, "(1 − 1) · Q", X2, 110, "center")
        nota(c, t, C["s13.c"] + 0.4, "= 0", x0 + w / 2, 900, 64, COR, "g", "center")
        resp(c, t, C["s13.d"], "P(1) = R", 1560, 780, 76, COR)
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)

    def s14():
        form(c, t, C["s14.a"], "P(1) = 1 + 3 + 5 = 9", W / 2, 300, 120, CERTO, "center")
        E.frase(c, t, C["s14.b"], ps("teorema do resto", "g", 96, COR), W / 2, 520, "center", passo=0.12)
        E.foco(c, t, C["s14.c"], 0.5, lambda a: (M.rrect(c, 290, 610, 1360, 200, 40, COR, 0.1 * a),
                                                  E.escreve(c, "resto da divisão por", 340, 735, 64, "i", TINTA, a)))
        form(c, t, C["s14.c"] + 0.4, "(x − a)  →  P(a)", 960, 745, 100, COR)
    fase(c, t, C["s14"], C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"] + 0.1, ps("e com", "i", 84) + ps("mais", "g", 78, COR) + ps("no divisor?", "i", 84), XE, 200, passo=0.12)
    nota(c, t, C["s15.a"], "que número zera o divisor?", XE, 360, 66, TINTA, "i")
    form(c, t, C["s15.b"], "x + 2  zera com  x = −2", XE, 560, 110)
    pil(c, t, C["s15.c"], "resto = P(−2)", W / 2, 800, 84)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        E.frase(c, t, C["s16"] + 0.1, ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s16.a"], ps("divisível", "g", 110, BR) + ps("= resto zero", "i", 100, CLARO), W / 2, 340, "center", passo=0.12)
        form(c, t, C["s16.b"], "P(a) = 0 ?", W / 2, 500, 100, CLARO, "center")
        form(c, t, C["s16.c"], "(x^3 − 8) ÷ (x − 2)", W / 2, 680, 110, BR, "center")
        form(c, t, C["s16.d"], "P(2) = 2^3 − 8 = 0", W / 2, 840, 110, CLARO, "center")
        E.frase(c, t, C["s16.e"], ps("divisível,", "g", 76, BR) + ps("sem armar a conta", "i", 80, CLARO), W / 2, 990, "center", passo=0.12)
    fase(c, t, C["s16"], C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17.a"], ps("resto zero:", "g", 76, BR) + ps("divisão exata, como", "i", 80, CLARO) + ps("12 ÷ 3", "g", 76, BR), W / 2, 260, "center", passo=0.12)
    E.frase(c, t, C["s17.b"], ps("o atalho dá", "i", 84, CLARO) + ps("só o resto", "g", 78, BR), W / 2, 460, "center", passo=0.12)
    E.frase(c, t, C["s17.c"], ps("quer o quociente?", "i", 84, CLARO) + ps("arme a chave", "g", 78, BR), W / 2, 640, "center", passo=0.12)
    E.foco(c, t, C["s17.d"], 0.45, lambda a: E.pilula(c, "divisor do tipo x ± número", W / 2, 860, 64, estilo="g", fundo=CLARO, cor="#07070F", a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s18", "s19", [
        (C["s18.a"] - 0.6, lambda a: E.escreve(c, "resto da divisão de", XE, 380, 72, "i", TINTA, a), 0, 0),
        (C["s18.a"], "x^3 + 2x^2 − 5", 560, 120),
        (C["s18.b"] - 0.4, lambda a: E.escreve(c, "por", XE, 740, 72, "i", TINTA, a), 0, 0),
        (C["s18.b"], "x + 2 ?", 880, 120),
    ], cx=1500)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s20():
        form(c, t, C["s20.a"], "x + 2 zera com x = −2", XE, 220, 90)
        form(c, t, C["s20.a"] + 1.4, "resto = P(−2)", 1150, 220, 90, COR)
        S, y, sz = "(−2)^3 + 2 · (−2)^2 − 5", 430, 110
        form(c, t, C["s20.b"] - 0.4, S, W / 2, y, sz, align="center")
        realce(c, t, C["s20.b"], S, "(−2)^3", W / 2, y, sz, COR, "center", t1=C["s20.c"])
        form(c, t, C["s20.b"] + 0.3, "(−2)^3 = −8", 360, 600, 84, TINTA2)
        realce(c, t, C["s20.c"], S, "2 · (−2)^2", W / 2, y, sz, COR, "center", t1=C["s20.d"])
        form(c, t, C["s20.c"] + 0.3, "2 · 4 = 8", 1100, 600, 84, TINTA2)
        form(c, t, C["s20.d"], "−8 + 8 − 5", 600, 870, 110, align="center")
        resp(c, t, C["s20.d"] + 0.8, "resto −5", 1330, 840, 76)
    fase(c, t, C["s20"], C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    nota(c, t, C["s21.a"], "com +2 no lugar de −2:", XE, 300, 64, ERRADO)
    form(c, t, C["s21.b"], "8 + 8 − 5 = 11", XE, 470, 120, ERRADO)
    if t > C["s21.b"] + 1.6:
        E.risco(c, XE - 10, 490, XE + fw("8 + 8 − 5 = 11", 120) + 10, 370, t, C["s21.b"] + 1.6, largura=12)
    E.frase(c, t, C["s21.c"], ps("o número", "i", 80) + ps("zera o divisor:", "g", 74, COR) + ps("o sinal troca", "i", 80), W / 2, 760, "center", passo=0.12)
    form(c, t, C["s21.c"] + 1.2, "x + 2  →  −2", W / 2, 920, 100, COR, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s22.a"], ps("chave:", "i", 72) + ps("dividir, multiplicar, subtrair", "g", 64, COR)),
             (C["s22.a"] + 2.2, ps("ao subtrair,", "i", 72) + ps("troque os sinais", "g", 72, COR)),
             (C["s22.b"], ps("resto por (x − a) =", "i", 72) + [("P(a)", "g", 72, COR)]))
    fim_padrao(c, t, C, "s22", "s23", itens, "próxima aula: dividir só com os coeficientes", "Briot-Ruffini",
               k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, chave=b_chave, erro=b_erro, teorema=b_teorema,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
