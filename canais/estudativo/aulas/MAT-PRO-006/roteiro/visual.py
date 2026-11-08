"""Visual — Estudativo · MAT-PRO-006: soma dos termos de uma PA.

Linguagem visual da trilha Progressões (MAT-PRO-001 e MAT-PRO-004): fila de caixas de borda índigo com o termo dentro (preto) e a
posição embaixo (índigo); a razão é o arco verde por cima das caixas; índice como índice, letra preta e índice índigo (a₁, aₙ, Sₙ) com fx().
Nesta aula: 1 + 2 + … + 100 com arcos ligando as pontas (liga()), cada um "101"; a soma escrita duas vezes, na ordem e de trás para
frente, com as colunas em caixa pontilhada; Sₙ = (a₁ + aₙ) · n / 2 com fração de verdade (frac_fx()); no atalho, as 30 colunas
dos depósitos (E.colunas) com a linha da média 34, o que falta embaixo da linha em vermelho e o que sobra em cima em verde.
Palco escuro só no atalho.
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), caixa_em() (as da MAT-PRO-004), liga(), frac_fx()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-006_soma_dos_termos_de_uma_pa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("gauss", "formula", "dias", "atalho", "questao", "fim"))
BR = "#FFFFFF"

DIAS = [5 + 2 * i for i in range(30)]
assert sum(range(1, 101)) == 5050 == 50 * 101 and sum(range(1, 6)) == 15 == (1 + 5) * 5 // 2
assert DIAS[-1] == 63 == 5 + 29 * 2 and 29 * 2 == 58 and sum(DIAS) == 1020 == 68 * 15 and (5 + 30) * 15 == 525
assert 68 / 2 == 34 and 34 * 30 == 1020 and 101 / 2 == 50.5 and 101 * 50 == 5050
assert 12 + 19 * 2 == 50 and 19 * 2 == 38 and sum(12 + 2 * i for i in range(20)) == 620 == 62 * 10


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _pedacos(s):
    """separa "a_{20} = 5" em [(0, "a"), (1, "20"), (0, " = 5")]: 1 = índice"""
    out, buf, i = [], "", 0
    while i < len(s):
        if s[i] == "_":
            if buf:
                out.append((0, buf))
                buf = ""
            if s[i + 1] == "{":
                j = s.index("}", i)
                out.append((1, s[i + 2:j]))
                i = j + 1
            else:
                out.append((1, s[i + 1]))
                i += 2
        else:
            buf += s[i]
            i += 1
    if buf:
        out.append((0, buf))
    return out


def _w(s, size, est):
    return sum(E.formula(None, p, 0, 0, size * (0.6 if k else 1), est, a=0) + (size * 0.03 if k else 0) for k, p in _pedacos(s))


def fx(c, partes, x, y, size, a=1.0, align="left", est="g", cor=None):
    """fórmula com índice de verdade (a_n, a_1, a_{20}); partes = texto ou [(texto, cor)]. Devolve [(x0, largura)] de cada parte.
    Como na MAT-PRO-001: em pedaço preto (SAI), a letra fica preta e o índice (a posição) sai em índigo"""
    if isinstance(partes, str):
        partes = [(partes, cor or TINTA)]
    ws = [_w(s, size, est) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    out = []
    for (s, cr), w in zip(partes, ws):
        out.append((xx, w))
        if a > 0:
            px = xx
            for k, p in _pedacos(s):
                sz = size * (0.6 if k else 1)
                E.formula(c, p, px + (size * 0.01 if k else 0), y + (size * 0.2 if k else 0), sz, est, ENT if (k and cr == SAI) else cr, a)
                px += E.formula(None, p, 0, 0, sz, est, a=0) + (size * 0.03 if k else 0)
        xx += w
    return out


def fx_em(c, t, t0, partes, x, y, size, align="left", est="g", cor=None):
    E.foco(c, t, t0, 0.5, lambda a: fx(c, partes, x, y, size, a, align, est, cor))
    return fx(c, partes, x, y, size, 0, align, est, cor)


def caixa(c, cx, cy, w, h, val, a=1.0, pos=None, size=80, cor=None, borda=None, escuro=False, pos_size=44):
    """um termo: caixa de borda índigo com o valor dentro (preto) e a posição embaixo (índigo), como casa() da MAT-PRO-001"""
    if a <= 0:
        return
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 20, 20)
    c.drawRRect(rr, M.paint("#1A1830" if escuro else "#FFFFFF", a))
    c.drawRRect(rr, M.paint(borda or (CLARO if escuro else COR), a, stroke=5))
    if val is not None and val != "":
        fx(c, [(str(val), cor or (BR if escuro else SAI))], cx, cy + size * 0.36, size, a, "center")
    if pos:
        centro(c, pos, cx, cy + h / 2 + pos_size + 14, pos_size, "b", CLARO if escuro else ENT, a)


def fila(c, t, itens, cy, w=190, h=150, size=80, escuro=False, pos_size=44):
    """itens = [(cx, valor, posição, t0[, cor[, borda]])]; valor "…" = reticências sem caixa"""
    for it in itens:
        cx, val, pos, t0 = it[:4]
        cor = it[4] if len(it) > 4 else None
        borda = it[5] if len(it) > 5 else None
        if val == "…":
            E.foco(c, t, t0, 0.5, lambda a, cx=cx: centro(c, "…", cx, cy + 20, 90, "g", BR if escuro else TINTA2, a))
        else:
            E.foco(c, t, t0, 0.5, lambda a, cx=cx, val=val, pos=pos, cor=cor, borda=borda: caixa(
                c, cx, cy, w, h, val, a, pos, size, cor, borda, escuro, pos_size))


def pula(c, t, t0, x0, x1, ytopo, rot, cor=RAZ, alto=80, size=52):
    """a razão: arco por cima das caixas, de um termo para o seguinte"""
    E.salto(c, t, t0, x0, x1, ytopo - 8, alto, cor, rot, size=size)


def resultado(c, t, t0, s, cx, cy, r=110, cor=None):
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k, cor)
        size = r * (0.62 if len(s) <= 3 else 0.5 if len(s) <= 5 else 0.4)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g"):
    """par (posição, termo): posição em índigo, termo em preto"""
    partes = (("(", TINTA), (xv, ENT), (", ", TINTA), (yv, SAI), (")", TINTA))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def caixa_em(c, t, t0, x0, w, y, size, cor=None, d=0.5):
    """caixa pontilhada em volta de um trecho já escrito (x0 = início, y = linha de base)"""
    p = ep(t, t0, d)
    if p > 0:
        E.caixa_pontilhada(c, x0 - 16, y - size * 0.9, w + 32, size * 1.25, p, cor, p)


def eixos_pa(c, t, t0, P, nome_y="a_n"):
    """depois de E.plano: o eixo das posições em índigo e os nomes n (índigo) e aₙ (preto)"""
    x, y, w, h = P.caixa
    if t >= t0:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 22, ep(t, t0, 0.6))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (fx(c, [("n", ENT)], x + w + 30, P.oy + 70, 56, a),
                                          fx(c, [(nome_y, SAI)], P.ox + 24, y - 20, 56, a)))


def liga(c, t, t0, x0, x1, y, alto, rot=None, cor=None, d=0.7, size=52, a=1.0):
    """arco que liga duas pontas da soma (sem seta), com o rótulo no alto"""
    cor = cor or COR
    p = ease_out(prog(t, t0, d))
    if p <= 0 or a <= 0:
        return
    path = skia.Path()
    n = 40
    for i in range(n + 1):
        u = p * i / n
        X, Y = lerp(x0, x1, u), y - alto * math.sin(u * math.pi)
        path.lineTo(X, Y) if i else path.moveTo(X, Y)
    c.drawPath(path, M.paint(cor, a, stroke=6, cap_round=True))
    for X in (x0, x1):
        c.drawCircle(X, y, 8, M.paint(cor, a))
    if rot:
        E.foco(c, t, t0 + d * 0.7, 0.4, lambda q: centro(c, rot, (x0 + x1) / 2, y - alto - 22, size, "g", cor, q * a), sobe=6)


def frac_fx(c, num, den, x, y, size, a=1.0, cor=TINTA):
    """fração com índices no numerador: num = partes de fx, den = texto. x = borda esquerda, y = linha de base da conta.
    Devolve (largura, posições das partes do numerador)"""
    s_ = size * 0.78
    pos = fx(c, num, 0, 0, s_, 0)
    wn = pos[-1][0] + pos[-1][1]
    wd = E.formula(None, den, 0, 0, s_, "g", a=0)
    w = max(wn, wd) + size * 0.12
    pos = fx(c, num, x + (w - wn) / 2, y - size * 0.46, s_, a)
    if a > 0:
        E.formula(c, den, x + (w - wd) / 2, y + size * 0.46, s_, "g", cor, a)
        b = max(4, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(cor, a))
    return w, pos


def formula_s(c, x, y, size, a=1.0, cor_res=TINTA):
    """Sₙ = (a₁ + aₙ) · n / 2, com a fração de verdade; devolve as posições de Sₙ, a₁, aₙ e n"""
    p1 = fx(c, [("S_n", SAI), (" = ", TINTA)], x, y, size, a)
    w, pn = frac_fx(c, [("(", TINTA), ("a_1", SAI), (" + ", TINTA), ("a_n", SAI), (") · ", TINTA), ("n", ENT)], "2", p1[1][0] + p1[1][1], y, size, a)
    return dict(S=p1[0], a1=pn[1], an=pn[3], n=pn[5], fim=p1[1][0] + p1[1][1] + w)


def larg_s(size):
    d = formula_s(None, 0, 0, size, 0)
    return d["fim"]


# ---------------- gancho ----------------
GAUSS = [("1", TINTA), (" + ", TINTA), ("2", TINTA), (" + ", TINTA), ("3", TINTA), (" + … + ", TINTA), ("98", TINTA), (" + ", TINTA),
         ("99", TINTA), (" + ", TINTA), ("100", TINTA)]


def b_gancho(c, t, C, b):
    def s01():
        fx_em(c, t, C["s01.a"], GAUSS, W / 2, 380, 100, "center")
        E.saida(c, t, C["s01.b"] - 0.2, lambda: E.frase(c, t, C["s01.a"] + 5.0, ps("uma hora de sossego?", "i", 70, TINTA2), W / 2, 560, "center"))
        resultado(c, t, C["s01.b"], "5.050", W / 2, 600, 130)
        E.frase(c, t, C["s01.c"], [("o", "i", 90), ("menino:", "i", 90), ("Gauss", "g", 120, COR)], W / 2, 900, "center")
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 260)
    E.frase(c, t, C["s02.a"] + 2.6, [("a", "i", 100), ("ideia", "i", 100), ("de", "i", 100), ("Gauss", "g", 104, COR)], XE, 430)
    E.frase(c, t, C["s02.a"] + 4.8, [("a", "i", 100), ("fórmula", "g", 104, COR), ("da", "i", 100), ("soma", "i", 100)], XE, 590)
    E.foco(c, t, C["s02.a"] + 7.0, 0.5, lambda a: E.pilula(c, "+ atalho de prova", XE + 300, 780, 58, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03"] + 0.6, 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03"] + 0.75, 0.5, lambda a: E.escreve(c, "coisa", XE + 170, 700, 120, "i", TINTA, a))
    x, w, y = 860, 920, 330
    p = ep(t, C["s03.a"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 300, p, prog_=p)
    E.frase(c, t, C["s03.a"] + 0.1, [("termo geral:", "i", 62), ("o", "i", 62), ("último", "g", 60, COR), ("termo", "i", 62)], x + 44, y + 90)
    fx_em(c, t, C["s03.a"] + 0.4, [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" + (", TINTA), ("n", ENT), (" − 1) · ", TINTA), ("r", RAZ)], x + 44, y + 220, 84)
    E.cursor(c, x + w - 30, y + 270, ep(t, C["s03.a"], 0.4))


# ---------------- a ideia de Gauss ----------------
def b_gauss(c, t, C, b):
    y = 640
    pos = fx_em(c, t, C["s04"], GAUSS, W / 2, y, 96, "center")
    cx = lambda i: pos[i][0] + pos[i][1] / 2
    pares = ((0, 10, "s04.b", 250), (2, 8, "s04.c", 180), (4, 6, "s04.d", 110))
    E.frase(c, t, C["s04.a"], [("junte", "i", 84), ("as", "i", 84), ("pontas", "g", 80, COR)], W / 2, 170, "center")
    for i, j, k, alto in pares:
        liga(c, t, C[k], cx(i), cx(j), y - 90, alto, "101", COR)
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, i=i, j=j: (c.drawCircle(cx(i), y - 30, 62, M.paint(COR, 0.12 * a)),
                                                           c.drawCircle(cx(j), y - 30, 62 + 14 * (j == 10), M.paint(COR, 0.12 * a))))

    def s04():
        E.frase(c, t, C["s04.e"] - 2.6, [("um", "i", 64), ("sobe", "g", 60, CERTO), ("1,", "g", 60, CERTO), ("o", "i", 64), ("outro", "i", 64),
                                          ("desce", "g", 60, ERRADO), ("1", "g", 60, ERRADO)], W / 2, 800, "center")
        E.frase(c, t, C["s04.e"], [("a", "i", 76), ("soma", "i", 76), ("do", "i", 76), ("par", "i", 76), ("não", "g", 72, COR), ("muda", "g", 72, COR)],
                W / 2, 920, "center")
    E.saida(c, t, C["s05"] - 0.1, s04)
    E.frase(c, t, C["s05.a"], [("100", "g", 80), ("números", "i", 84), ("→", "g", 80, TINTA2), ("50", "g", 84, COR), ("pares", "i", 84)], XE + 40, 830)
    fx_em(c, t, C["s05.b"], "50 · 101 = ", XE + 40, 975, 84)
    resultado(c, t, C["s05.b"] + 0.4, "5.050", XE + 40 + E.formula(None, "50 · 101 = ", 0, 0, 84, "g", a=0) + 100, 945, 80)


# ---------------- a soma em dobro ----------------
DX = (620, 820, 1020, 1220, 1420)


def b_dobro(c, t, C, b):
    E.frase(c, t, C["s06"], [("e", "i", 80), ("se", "i", 80), ("for", "i", 80), ("ímpar?", "g", 76, COR)], W / 2, 160, "center")
    y1, y2, s = 400, 560, 96

    def linha(y, nums, a):
        fx(c, [("S", SAI), (" =", TINTA)], 300, y, s, a)
        for i, (x, v) in enumerate(zip(DX, nums)):
            centro(c, str(v), x, y, s, "g", TINTA, a)
            if i < 4:
                centro(c, "+", x + 100, y - 4, s * 0.8, "g", TINTA2, a)
    E.foco(c, t, C["s06"] + 0.8, 0.5, lambda a: linha(y1, (1, 2, 3, 4, 5), a))

    def sem_par():
        liga(c, t, C["s06"] + 2.2, DX[0], DX[4], y1 - 90, 150, None, COR)
        liga(c, t, C["s06"] + 2.4, DX[1], DX[3], y1 - 90, 90, None, COR)
        E.foco(c, t, C["s06"] + 2.8, 0.4, lambda a: (c.drawCircle(DX[2], y1 - 34, 64, M.paint(ERRADO, a, stroke=6)),
                                                     centro(c, "sem par", DX[2], y1 + 90, 50, "i", ERRADO, a)))
    E.saida(c, t, C["s06.a"] - 0.1, sem_par)
    E.foco(c, t, C["s06.a"] + 0.4, 0.5, lambda a: linha(y2, (5, 4, 3, 2, 1), a))
    E.foco(c, t, C["s06.a"] + 0.6, 0.4, lambda a: E.escreve(c, "de trás para frente", 1560, y2 - 20, 44, "i", TINTA2, a))
    for i, x in enumerate(DX):
        t0 = C["s06.b"] + 0.15 * i
        p = ep(t, t0, 0.4)
        if p > 0:
            E.caixa_pontilhada(c, x - 70, y1 - 100, 140, y2 - y1 + 140, p, COR, p)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a, x=x: centro(c, "6", x, y2 + 120, 84, "g", COR, a))
    E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: E.escreve(c, "1º + último", 300, y2 + 112, 48, "i", COR, a))
    E.frase(c, t, C["s06.c"], [("5", "g", 76, COR), ("colunas", "i", 80), ("de", "i", 80), ("6", "g", 76, COR)], W / 2, 860, "center")
    E.frase(c, t, C["s06.d"], [("é", "i", 76), ("a", "i", 76), ("soma", "i", 76), ("em", "i", 76), ("dobro:", "g", 72), ("÷", "g", 80, COR), ("2", "g", 80, COR)],
            W / 2, 980, "center")


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s07():
        size, y = 150, 520
        x = W / 2 - larg_s(size) / 2
        E.foco(c, t, C["s07.a"], 0.5, lambda a: formula_s(c, x, y, size, a))
        d = formula_s(None, x, y, size, 0)
        x0, w0 = d["S"]
        caixa_em(c, t, C["s07.b"], x0, w0, y, size, SAI)
        E.foco(c, t, C["s07.b"] + 0.2, 0.4, lambda a: centro(c, "a soma", x0 + w0 / 2, y + 160, 54, "i", TINTA, a))
        s_ = size * 0.78
        yn = y - size * 0.46
        for k, ck, rot, cor in (("a1", "s07.c", "primeiro", SAI), ("an", "s07.d", "último", SAI)):
            xa, wa = d[k]
            caixa_em(c, t, C[ck], xa, wa, yn, s_, ENT)
            E.foco(c, t, C[ck] + 0.2, 0.4, lambda a, xa=xa, wa=wa, rot=rot: centro(c, rot, xa + wa / 2, yn - s_ - 50, 54, "i", TINTA, a))
        xn, wn = d["n"]
        caixa_em(c, t, C["s07.e"], xn, wn, yn, s_, ENT)
        E.foco(c, t, C["s07.e"] + 0.2, 0.4, lambda a: centro(c, "quantos termos", xn + wn / 2, y + 160, 54, "i", ENT, a))
        E.frase(c, t, C["s07.f"], [("(primeiro", "g", 60), ("+", "g", 60), ("último)", "g", 60), ("×", "g", 60, COR), ("quantidade", "g", 60),
                                   ("÷", "g", 60, COR), ("2", "g", 60)], W / 2, 900, "center", passo=0.25)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    size = 90
    E.foco(c, t, C["s08"], 0.5, lambda a: formula_s(c, W / 2 - larg_s(size) / 2, 230, size, a))
    fx_em(c, t, C["s08.a"], "1 + 2 + 3 + 4 + 5 = 15", XE + 40, 470, 84)
    fx_em(c, t, C["s08.b"], [("1 + 5", TINTA), (" = 6", TINTA)], XE + 40, 620, 84)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.escreve(c, "primeiro + último", 700, 620, 50, "i", TINTA2, a))
    fx_em(c, t, C["s08.c"], [("6 · ", TINTA), ("5", ENT), (" = 30", TINTA)], XE + 40, 770, 84)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "5 termos", 700, 770, 50, "i", ENT, a))
    fx_em(c, t, C["s08.d"], "30 ÷ 2 = 15", XE + 40, 920, 84)
    E.foco(c, t, C["s08.d"] + 1.6, 0.4, lambda a: (E.selo(c, 1300, 690, 70, True, a),
                                                   centro(c, "bateu, mesmo ímpar", 1300, 830, 56, "i", CERTO, a)))


# ---------------- 30 dias ----------------
FX_ = (330, 590, 850)


def b_dias(c, t, C, b):
    cy = 250
    fim = t >= C["s10.c"]
    fila(c, t, [(FX_[0], "R$ 5", "1º dia", C["s09.a"])], cy, 220, 130, 66, pos_size=40)
    fila(c, t, [(x, f"R$ {v}", f"{i + 2}º dia", C["s09.b"] + 0.5 + 0.3 * i) for i, (x, v) in enumerate(zip(FX_[1:], (7, 9)))], cy, 220, 130, 66, pos_size=40)
    for i in range(2):
        pula(c, t, C["s09.b"] + 0.3 * i, FX_[i], FX_[i + 1], cy - 65, "+2", alto=60, size=46)
    fila(c, t, [(1090, "…", None, C["s09.c"])], cy)
    E.foco(c, t, C["s09.c"], 0.5, lambda a: caixa(c, 1340, cy, 220, 130, "R$ 63" if fim else "?", a, "30º dia", 66, COR if fim else CINZA, pos_size=40))
    E.frase(c, t, C["s09.c"] + 0.3, [("total", "g", 70, COR), ("em", "i", 74), ("30", "g", 70), ("dias?", "i", 74)], 1340, 480, "center")

    def s10():
        E.frase(c, t, C["s10"], [("primeiro,", "i", 70), ("o", "i", 70), ("último", "g", 66, COR), ("termo", "i", 70)], XE, 520)
        E.frase(c, t, C["s10.a"], [("1º", "g", 70, ENT), ("→", "g", 70, TINTA2), ("30º:", "g", 70, ENT), ("29", "g", 70, COR), ("saltos", "i", 74)], XE, 660)
        fx_em(c, t, C["s10.b"], [("29 · ", TINTA), ("2", RAZ), (" = 58", TINTA)], XE, 790, 80)
        fx_em(c, t, C["s10.c"], [("a_{30}", SAI), (" = 5 + 58 = 63", TINTA)], XE, 920, 80)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    fx_em(c, t, C["s11.a"], "5 + 63 = 68", XE, 560, 84)
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.escreve(c, "primeiro + último", XE + 560, 560, 50, "i", TINTA2, a))
    pos = fx_em(c, t, C["s11.b"], [("S_{30}", SAI), (" = ", TINTA)], XE, 760, 96)
    xs = pos[1][0] + pos[1][1]
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "f{68 · 30}{2}", xs, 760, 96, "g", TINTA, a))
    w = E.formula(None, "f{68 · 30}{2}", 0, 0, 96, "g", a=0)
    E.foco(c, t, C["s11.b"] + 1.8, 0.5, lambda a: E.formula(c, " = 68 · 15", xs + w, 760, 96, "g", TINTA, a))
    E.foco(c, t, C["s11.b"] + 1.8, 0.4, lambda a: E.escreve(c, "30 ÷ 2 = 15 primeiro", xs + 40, 900, 50, "i", TINTA2, a))
    resultado(c, t, C["s11.c"], "R$ 1.020", 1600, 700, 150)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("dias", "g", 72, ERRADO), ("no", "i", 76), ("lugar", "i", 76), ("do", "i", 76), ("último", "g", 72, CERTO), ("termo", "i", 76)],
            W / 2, 170, "center")
    x0 = 480
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "f{(5 + 30) · 30}{2}", x0, 400, 110, "g", ERRADO, a))
    w = E.formula(None, "f{(5 + 30) · 30}{2}", 0, 0, 110, "g", a=0)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: (E.formula(c, " = 525", x0 + w, 400, 110, "g", ERRADO, a), E.selo(c, x0 + w + 470, 365, 46, False, a)))
    if t < C["s13"]:
        return
    cx, cy = 560, 720
    E.foco(c, t, C["s13.a"], 0.5, lambda a: caixa(c, cx, cy, 260, 170, "63" if t >= C["s13.b"] else "", a, "30º", 96, COR, pos_size=60))
    E.frase(c, t, C["s13.a"] + 0.3, [("30", "g", 76, ENT), ("é", "i", 80), ("a", "i", 80), ("posição", "g", 76, ENT)], 820, 680)
    E.frase(c, t, C["s13.b"], [("R$", "g", 76), ("63", "g", 76, COR), ("é", "i", 80), ("o", "i", 80), ("valor", "g", 76)], 820, 800)
    E.frase(c, t, C["s13.c"], [("1º", "g", 66, COR), ("o", "i", 70), ("último", "g", 66), ("termo,", "i", 70), ("depois", "i", 70), ("some", "g", 66, COR)],
            W / 2, 990, "center")


# ---------------- atalho (palco escuro) ----------------
GX, GY, GW, GH, GMAX = 940, 300, 780, 560, 70


def grafico(c, t, t0, falta=0.0):
    E.colunas(c, t, t0, [("", v) for v in DIAS], GX, GY, GW, GH, vmax=GMAX, cor=CLARO, valores=False, escuro=True, passo=0.03, d=0.4)
    vy = lambda v: GY + GH - v / GMAX * GH
    slot = GW / 30
    bw = slot * 0.62
    if falta > 0:
        for i, v in enumerate(DIAS):
            x = GX + slot * (i + 0.5) - bw / 2
            y0, y1 = sorted((vy(v), vy(34)))
            c.drawRect(skia.Rect.MakeLTRB(x, y0, x + bw, y1), M.paint(ERRADO if v < 34 else CERTO, 0.75 * falta))
    return vy


def b_atalho(c, t, C, b):
    palco(c, t)
    vy = None
    if t < C["s15.b"] + 0.5:
        def g():
            vy = grafico(c, t, C["s14.c"] - 0.6, ep(t, C["s15.a"], 0.6))
            p = ep(t, C["s14.c"] + 0.4, 0.6)
            if p > 0:
                M.line(c, GX - 10, vy(34), GX - 10 + (GW + 20) * p, vy(34), BR, 1.0, 5, dash=[18, 12])
            E.foco(c, t, C["s14.c"] + 0.8, 0.4, lambda a: E.escreve(c, "34", GX + GW + 24, vy(34) + 22, 60, "g", BR, a))
            E.foco(c, t, C["s15.a"] + 0.4, 0.4, lambda a: (E.escreve(c, "falta", GX + 10, GY + GH + 70, 56, "g", ERRADO, a),
                                                           E.escreve(c, "sobra", GX + GW - 190, GY - 10, 56, "g", CERTO, a)))
        E.saida(c, t, C["s15.b"] - 0.1, g)

    def s14():
        E.frase(c, t, C["s14.a"], [("soma", "g", 80, BR), ("=", "g", 80, BR), ("média", "g", 80, CLARO), ("×", "g", 80, BR), ("quantidade", "g", 80, BR)],
                W / 2, 180, "center")
        E.foco(c, t, C["s14.b"], 0.5, lambda a: (E.escreve(c, "média =", XE, 430, 70, "i", CLARO, a),
                                                 E.formula(c, "f{1º + último}{2}", XE + 280, 430, 84, "g", BR, a)))
        fx_em(c, t, C["s14.c"], [("f{68}{2} = 34", BR)], XE, 640, 90)
        fx_em(c, t, C["s14.d"], [("34 · 30 = ", BR), ("1.020", CLARO)], XE, 830, 90)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.saida(c, t, C["s15.b"] - 0.1, lambda: (
        E.frase(c, t, C["s15.a"], [("o", "i", 70, CLARO), ("que", "i", 70, CLARO), ("falta", "g", 66, ERRADO), ("no", "i", 70, CLARO), ("começo", "i", 70, CLARO)], XE, 400),
        E.frase(c, t, C["s15.a"] + 1.2, [("sobra", "g", 66, CERTO), ("no", "i", 70, CLARO), ("fim", "i", 70, CLARO)], XE, 510),
        E.frase(c, t, C["s15.a"] + 3.4, [("34", "g", 66, BR), ("todo", "i", 70, CLARO), ("dia", "i", 70, CLARO)], XE, 640)))
    if t < C["s15.b"]:
        return

    def s15b():
        E.foco(c, t, C["s15.b"] + 0.3, 0.5, lambda a: (E.pilula(c, "não compensa", 470, 300, 56, "g", fundo=ERRADO, a=a),
                                                      fx(c, [("1 + 100 = 101", BR), (", ímpar", CLARO)], 720, 320, 76, a)))
        fx_em(c, t, C["s15.c"], [("101 ÷ 2 = 50,5", CLARO)], XE + 100, 560, 90)
        fx_em(c, t, C["s15.d"], [("100 ÷ 2 = 50", BR), ("   →   ", CLARO), ("101 · 50", BR)], XE + 100, 780, 90)
    s15b()


# ---------------- questão ----------------
def auditorio(c, t, t0, cx, y0, a_ext=1.0):
    """fileiras de cadeiras que crescem: 12, 14, 16, … (as 4 primeiras)"""
    for i in range(4):
        n = 12 + 2 * i
        y = y0 + i * 70
        for k in range(n):
            x = cx + (k - (n - 1) / 2) * 30
            q = ease_back(prog(t, t0 + 0.4 * i + 0.01 * k, 0.3))
            if q > 0:
                M.rrect(c, x - 11 * q, y - 11 * q, 22 * q, 22 * q, 6, COR if i == 0 else TINTA2, a_ext)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 150)
    linhas = (("s16.a", [("20", "g", 80, COR), ("fileiras", "i", 84)]), ("s16.b", [("1ª:", "g", 80, ENT), ("12", "g", 80), ("cadeiras", "i", 84)]),
              ("s16.c", [("cada", "i", 84), ("uma:", "i", 84), ("+2", "g", 80, RAZ), ("cadeiras", "i", 84)]),
              ("s16.d", [("quantas", "i", 84), ("ao", "i", 84), ("todo?", "g", 80, COR)]))
    for i, (k, partes) in enumerate(linhas):
        E.frase(c, t, C[k], partes, XE, 330 + 160 * i)
    E.saida(c, t, C["s17"] - 0.1, lambda: (auditorio(c, t, C["s16.b"], 1400, 380),
                                           E.foco(c, t, C["s16.c"] + 0.6, 0.4, lambda a: (E.escreve(c, "12", 1630, 392, 44, "b", COR, a),
                                                                                         E.escreve(c, "14", 1660, 462, 44, "b", TINTA2, a),
                                                                                         E.escreve(c, "16", 1690, 532, 44, "b", TINTA2, a)))))
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], 1440, 520, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18"] + 1.0, [("a", "i", 70), ("última", "g", 66, COR), ("fileira", "i", 70)], XE, 200)
    fx_em(c, t, C["s18.a"], [("19 · ", TINTA), ("2", RAZ), (" = 38", TINTA)], XE, 340, 84)
    fx_em(c, t, C["s18.b"], [("a_{20}", SAI), (" = 12 + 38 = 50", TINTA)], XE, 480, 84)
    E.frase(c, t, C["s18.c"] - 1.4, [("a", "i", 70), ("soma", "g", 66, COR)], XE, 660)
    fx_em(c, t, C["s18.c"], "12 + 50 = 62", XE, 790, 84)
    fx_em(c, t, C["s18.d"], [("20", ENT), (" ÷ 2 = 10", TINTA)], XE + 620, 790, 84)
    fx_em(c, t, C["s18.e"], "62 · 10 = ", XE, 960, 96)
    bx = XE + E.formula(None, "62 · 10 = ", 0, 0, 96, "g", a=0) + 100
    resultado(c, t, C["s18.e"] + 0.4, "620", bx, 925, 90)
    E.foco(c, t, C["s18.e"] + 1.0, 0.4, lambda a: E.escreve(c, "cadeiras", bx + 120, 960, 70, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s19.a", "ache o último termo"), ("s19.b", "some as pontas"), ("s19.c", "× quantidade ÷ 2"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 90)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s20.a"], [("Hora", "g", 140, COR), ("de", "i", 130)], XE, 420)
    E.frase(c, t, C["s20.a"] + 0.3, [("praticar", "g", 140, COR)], XE, 570)
    E.frase(c, t, C["s20.a"] + 1.0, [("figuras", "i", 70)], 1250, 320)
    E.frase(c, t, C["s20.a"] + 1.6, [("calendários", "i", 70)], 1250, 430)
    E.frase(c, t, C["s20.a"] + 2.2, [("pagamentos", "i", 70)], 1250, 540)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, gauss=b_gauss, dobro=b_dobro, formula=b_formula, dias=b_dias, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
