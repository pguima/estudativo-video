"""Visual — Estudativo · MAT-PLN-009: raízes complexas vêm em pares.
1 + 2i raiz de x³ − 3x² + 7x − 5 traz 1 − 2i; o porquê (trocar i por −i não muda os reais); grau 3 real tem uma raiz real;
o par vira x² − 2x + 5 (soma vezes diferença) e a chave dá x − 1; o erro de trocar o sinal da parte real; no palco, o atalho
do par pronto e o teste do 1; a questão com 2i.
Convenções da trilha em MAT-PLN-001; o i em âmbar (MAT-PLN-008); CHAVE de MAT-PLN-002, aqui com quatro colunas.
Instantes: só os marcadores C[...]; fala sem marcador usa entre()."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Polinômios")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-PLN-009_raizes_complexas_em_pares.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("par", "terceira", "erro", "atalho", "questao", "fim"))
IM = "#B86E00"


def _P(c, x):
    r = 0
    for k in c:
        r = r * x + k
    return r


# as contas da aula
_i = 1j
for _z in (1 + 2 * _i, 1 - 2 * _i, 1):
    assert abs(_P([1, -3, 7, -5], _z)) < 1e-12
assert all(abs((x - (1 + 2 * _i)) * (x - (1 - 2 * _i)) - (x * x - 2 * x + 5)) < 1e-12 for x in range(-4, 5))
assert all((x * x - 2 * x + 5) * (x - 1) == x ** 3 - 3 * x * x + 7 * x - 5 for x in range(-4, 5))
assert (2 * _i) ** 2 == -4 and 1 - 3 + 7 - 5 == 0
assert all(x ** 3 - x * x + 4 * x - 4 == (x * x + 4) * (x - 1) for x in range(-4, 5)) and _P([1, -1, 4, -4], 2 * _i) == 0


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
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.6)), cor, a),
                                     formula(c, s, cx, cy + size * 0.36, size, BR, a, "center")))


# chave de quatro colunas (x³, x², x, número): borda direita de cada coluna
CX4 = (420, 700, 950, 1160)
XB4 = 1250


def cols4(c, t, t0, partes, y, size, cor=None, dt=0.12):
    for k, s in enumerate(partes):
        if s:
            form(c, t, t0 + dt * k, s, CX4[k], y, size, cor, "right")


def risca4(c, t, t0, y, x0, x1):
    p = ep(t, t0, 0.5)
    if p > 0:
        M.line(c, x0, y + 34, x0 + (x1 - x0) * p, y + 34, TINTA, 1.0, 5)


def chave4(c, t, t0, dividendo, divisor, y0, size):
    a = ep(t, t0, 0.5)
    if a > 0:
        M.line(c, XB4, y0 - size, XB4, y0 + 36, TINTA, a, 6)
        M.line(c, XB4, y0 + 36, XB4 + 560 * a, y0 + 36, TINTA, a, 6)
    cols4(c, t, t0 + 0.2, dividendo, y0, size)
    form(c, t, t0, divisor, XB4 + 36, y0, size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        form(c, t, C["s01.a"], "x^3 − 3x^2 + 7x − 5", W / 2, 260, 120, align="center")
        raiz_bola(c, t, C["s01.a"] + 0.6, "1 + 2i", 480, 540, 150, 80)
        raiz_bola(c, t, C["s01.b"], "1 − 2i", 960, 540, 150, 80, COR)
        raiz_bola(c, t, C["s01.c"], "?", 1440, 540, 150, 100, TINTA2)
        nota(c, t, C["s01.b"] + 0.4, "sem conta nenhuma", 960, 770, 50, COR, "g", "center")
        nota(c, t, C["s01.c"] + 0.4, "em poucos passos", 1440, 860, 50, TINTA2, "g", "center")
    fase(c, t, C["s01"], C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        gancho_fim(c, t, C["s02.a"], C["s02.b"], [(ps("o par", "g", 120, COR), 1.0),
                                                 (ps("de uma raiz complexa", "i", 92), 1.6)])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", [
        (C["s03.b"], ps("conjugado:", "g", 60, COR) + ps("só o sinal do i muda", "i", 60), "2 + 3i   →   2 − 3i"),
        (C["s03.c"], ps("forma fatorada:", "g", 60, COR) + ps("um parêntese por raiz", "i", 60), None),
        (C["s03.d"], ps("divisão pela chave:", "g", 60, COR) + ps("dividir, multiplicar, subtrair", "i", 60), None),
    ])


# ---------------- o par ----------------
def b_par(c, t, C, b):
    def s04():
        form(c, t, C["s04.a"], "x = 2 + 3i   e   x = 2 − 3i", W / 2, 240, 100, align="center")
        form(c, t, C["s04.b"], "x = f{4 ± 6i}{2}", W / 2, 470, 120, align="center")
        pil(c, t, C["s04.b"] + 0.6, "o ± entrega o par", W / 2, 600, 54, IM)
        E.frase(c, t, C["s04.c"], ps("complexo é raiz", "i", 80) + ps("→", "g", 80, COR) + ps("o conjugado também", "g", 76, COR), W / 2, 760, "center", passo=0.12)
    fase(c, t, C["s04"], C["s05"] - 0.1, s04)

    def s05():
        E.frase(c, t, C["s05.a"], ps("trocar", "i", 76) + ps("i por −i", "g", 72, IM) + ps("não muda os reais", "i", 76), XE, 220, passo=0.1)
        form(c, t, C["s05.b"], "(−i)^2 = −1", XE, 380, 100, IM)
        form(c, t, C["s05.c"], "P(1 + 2i) = 0", XE, 560, 100)
        form(c, t, C["s05.d"], "→   P(1 − 2i) = 0", XE + fw("P(1 + 2i) = 0 ", 100), 560, 100, COR)
        pil(c, t, C["s05.e"], "condição: coeficientes reais", W / 2, 780, 60, TINTA)
    fase(c, t, C["s05"], C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06.a"], ps("grau 3:", "g", 84, COR) + ps("três raízes", "i", 88), XE, 260, passo=0.12)
    for k, (s, cor) in enumerate((("a + bi", IM), ("a − bi", IM), ("real", CERTO))):
        E.foco(c, t, C["s06.b"] + 0.4 * k, 0.5, lambda p, k=k, s=s, cor=cor: (E.bola(c, 520 + 420 * k, 520, 130 * ease_back(prog(t, C["s06.b"] + 0.4 * k, 0.6)), cor, p),
                                                                          formula(c, s, 520 + 420 * k, 550, 64, BR, p, "center")))
    nota(c, t, C["s06.b"] + 0.4, "as com i: de duas em duas", 730, 720, 54, IM, "g", "center")
    pil(c, t, C["s06.c"], "grau 3 com coeficientes reais: pelo menos uma raiz real", W / 2, 900, 54, CERTO)


# ---------------- a terceira raiz ----------------
def b_terceira(c, t, C, b):
    def s07_09():
        form(c, t, C["s07.b"], "[x − (1 + 2i)] · [x − (1 − 2i)]", W / 2, 220, 92, align="center")
        fase(c, t, C["s07.a"], C["s08"] - 0.1, lambda: pil(c, t, C["s07.a"], "cada raiz vira um parêntese: x − raiz", W / 2, 520, 56, TINTA))
        form(c, t, C["s08.b"], "= [(x − 1) − 2i] · [(x − 1) + 2i]", W / 2, 360, 92, TINTA2, "center")
        S = "= (x − 1)^2 − (2i)^2"
        form(c, t, C["s08.c"], S, W / 2, 510, 100, align="center")
        form(c, t, C["s09.a"], "(x − 1)^2 = x^2 − 2x + 1", XE, 680, 80, TINTA2)
        form(c, t, C["s09.b"], "(2i)^2 = 4 · (−1) = −4", 1060, 680, 80, IM)
        form(c, t, C["s09.c"], "x^2 − 2x + 1 + 4", W / 2, 850, 100, align="center")
        if t >= C["s09.d"]:
            E.foco(c, t, C["s09.d"], 0.45, lambda a: M.rrect(c, W / 2 - 400, 900, 800, 150, 36, CERTO, 0.14 * a))
        form(c, t, C["s09.d"], "= x^2 − 2x + 5", W / 2, 1000, 110, CERTO, "center")
        pil(c, t, C["s09.e"], "o i sumiu", 1600, 990, 54, CERTO)
    fase(c, t, C["s07"], C["s10"] - 0.1, s07_09)
    if t < C["s10"]:
        return
    sz, Y = 84, (300, 420, 540, 660, 780)
    chave4(c, t, C["s10"], ("x^3", "− 3x^2", "+ 7x", "− 5"), "x^2 − 2x + 5", Y[0], sz)
    form(c, t, C["s10.a"], "x", XB4 + 36, Y[0] + 120, sz, COR)
    if C["s10.b"] - 0.01 <= t < C["s10.c"] + 0.45:
        E.saida(c, t, C["s10.c"], lambda: cols4(c, t, C["s10.b"], ("x^3", "− 2x^2", "+ 5x", None), Y[1], sz, TINTA2))
    if t >= C["s10.c"]:
        cols4(c, t, C["s10.c"], ("−x^3", "+ 2x^2", "− 5x", None), Y[1], sz, COR, 0.05)
    risca4(c, t, C["s10.c"] + 0.4, Y[1], 180, CX4[3] + 20)
    cols4(c, t, C["s10.c"] + 0.8, (None, "−x^2", "+ 2x", "− 5"), Y[2], sz)
    form(c, t, C["s11.a"], "− 1", XB4 + 36 + fw("x ", sz), Y[0] + 120, sz, COR)
    cols4(c, t, C["s11.b"], (None, "x^2", "− 2x", "+ 5"), Y[3], sz, COR)
    risca4(c, t, C["s11.c"], Y[3], 460, CX4[3] + 20)
    cols4(c, t, C["s11.c"] + 0.4, (None, None, None, "0"), Y[4], sz, CERTO)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.caixa_pontilhada(c, XB4 + 16, Y[0] + 50, 260, 100, a, COR))
    E.foco(c, t, C["s11.e"], 0.5, lambda a: E.pilula(c, "terceira raiz: 1", 1560, 760, 64, estilo="g", fundo=CERTO, cor=BR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 110, ERRADO)] + ps("com o conjugado", "i", 100), W / 2, 190, "center")
    form(c, t, C["s12.a"] - 0.4, "1 + 2i", 560, 460, 140, align="center")
    form(c, t, C["s12.b"], "−1 − 2i", 1300, 460, 140, ERRADO, "center")
    if t > C["s12.b"] + 1.2:
        E.risco(c, 1080, 490, 1520, 350, t, C["s12.b"] + 1.2, largura=12)
    pil(c, t, C["s12.c"], "a parte real fica; só o sinal do i muda", W / 2, 680, 56, TINTA)
    form(c, t, C["s12.d"], "1 − 2i", W / 2, 900, 150, CERTO, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13.a"], ps("o par já sai", "i", 84, CLARO) + ps("pronto", "g", 80, BR), W / 2, 180, "center", passo=0.12)
        form(c, t, C["s13.b"], "raízes  1 ± 2i", W / 2, 340, 100, AM, "center")
        S = "x^2 − 2x + 5"
        form(c, t, C["s13.c"] - 0.3, S, W / 2, 560, 150, BR, "center")
        realce(c, t, C["s13.c"], S, "− 2x", W / 2, 560, 150, CLARO, "center")
        realce(c, t, C["s13.d"], S, "5", W / 2, 560, 150, AM, "center")
        form(c, t, C["s13.c"] + 0.4, "−2 · (parte real)", 300, 760, 70, CLARO)
        form(c, t, C["s13.d"] + 0.4, "1^2 + 2^2 = 5", 1140, 760, 70, AM)
        E.frase(c, t, C["s13.e"], ps("sem abrir parênteses", "i", 76, CLARO), W / 2, 930, "center")
    fase(c, t, C["s13"], C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("é a conta que você acabou de fazer,", "i", 72, CLARO) + ps("para qualquer par", "g", 66, BR), W / 2, 260, "center", passo=0.1)
    E.frase(c, t, C["s14.b"], ps("antes de dividir,", "i", 84, CLARO) + ps("teste o 1", "g", 84, BR), W / 2, 450, "center", passo=0.12)
    form(c, t, C["s14.c"], "1 − 3 + 7 − 5 = 0", W / 2, 620, 110, BR, "center")
    E.foco(c, t, C["s14.d"], 0.45, lambda a: E.pilula(c, "1 é raiz", W / 2, 750, 60, estilo="g", fundo=CERTO, cor=BR, a=a))
    nota(c, t, C["s14.d"] + 1.6, "se não for, divida pelo par", W / 2, 900, 60, CLARO, "i", "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    questao_ui(c, t, C, "s15", "s16", [
        (C["s15.a"], "2i  é raiz de", 400, 90),
        (C["s15.a"] + 0.8, "x^3 − x^2 + 4x − 4", 580, 110),
        (C["s15.b"], lambda a: E.escreve(c, "ache as outras duas raízes", XE, 800, 76, "g", COR, a), 0, 0),
    ], cx=1560, cy=470)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        form(c, t, C["s17.a"], "2i = 0 + 2i   →   conjugado: −2i", W / 2, 230, 96, align="center")
        form(c, t, C["s17.b"], "−2 · 0 = 0:  sem termo do meio", W / 2, 440, 84, TINTA2, "center")
        form(c, t, C["s17.c"], "0^2 + 2^2 = 4", W / 2, 600, 84, IM, "center")
        form(c, t, C["s17.d"], "par:  x^2 + 4", W / 2, 820, 130, CERTO, "center")
    fase(c, t, C["s17"], C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    sz, Y = 84, (260, 380, 500, 620, 740)
    chave4(c, t, C["s18"], ("x^3", "− x^2", "+ 4x", "− 4"), "x^2 + 4", Y[0], sz)
    form(c, t, C["s18.a"], "x", XB4 + 36, Y[0] + 120, sz, COR)
    cols4(c, t, C["s18.b"], ("−x^3", None, "− 4x", None), Y[1], sz, COR)
    risca4(c, t, C["s18.c"] - 0.3, Y[1], 180, CX4[3] + 20)
    cols4(c, t, C["s18.c"], (None, "−x^2", None, "− 4"), Y[2], sz)
    form(c, t, C["s18.d"], "− 1", XB4 + 36 + fw("x ", sz), Y[0] + 120, sz, COR)
    cols4(c, t, C["s18.d"] + 0.3, (None, "x^2", None, "+ 4"), Y[3], sz, COR)
    risca4(c, t, C["s18.d"] + 0.7, Y[3], 460, CX4[3] + 20)
    cols4(c, t, C["s18.d"] + 1.0, (None, None, None, "0"), Y[4], sz, CERTO)
    for k, s in enumerate(("2i", "−2i", "1")):
        raiz_bola(c, t, C["s18.e"] + 0.3 * k, s, 700 + 260 * k, 930, 76, 60, CERTO if s == "1" else IM)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = ((C["s19.a"], ps("raiz complexa vem com", "i", 72) + ps("o conjugado", "g", 72, COR)),
             (C["s19.b"], ps("o par vira", "i", 72) + ps("fator de grau 2", "g", 72, COR)),
             (C["s19.c"], ps("a divisão entrega", "i", 72) + ps("o resto das raízes", "g", 72, COR)))
    fim_padrao(c, t, C, "s19", "s20", itens, "próxima aula:", "prática de raízes complexas",
               extra=lambda: E.frase(c, t, C["s20.b"], ps("reais e complexas,", "i", 72) + ps("no estilo das provas", "g", 72, COR), XE, 540, passo=0.1),
               k_ins="c", k_bons="d")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, par=b_par, terceira=b_terceira, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
