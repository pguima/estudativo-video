"""Visual — Estudativo · MAT-PRO-004: progressão aritmética, razão e termo geral.

Linguagem visual da trilha Progressões (definida na MAT-PRO-001; esta aula acrescenta a razão, e as aulas de PA e PG copiam daqui):
- sequência = fila de caixas de borda índigo: o valor (termo) dentro, em preto; a posição (1º, 2º, 3º…) embaixo, em índigo (caixa(), fila()).
- posição n = índigo (ENT), termo aₙ = preto (SAI), como x e y na trilha Funções; a razão (o "+4" que pula de um termo
  para o próximo) = arco verde por cima das caixas (pula()), como os "+2,50" da tabela da MAT-FUN-009.
- índice sempre escrito como índice: a₁, aₙ, a₂₀, letra preta e índice índigo (fx() entende "a_1", "a_n", "a_{20}" e o resto de E.formula).
- gráfico na linguagem de Funções: E.plano com o eixo da posição (n) em índigo e o do termo (aₙ) em preto; E.ponto, E.curva tracejada.
- palco escuro só no atalho.
Peças locais: fx(), fx_em(), caixa(), fila(), pula(), resultado(), par(), eixos_pa()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Progressões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI, RAZ = COR, TINTA, CERTO  # posição n · termo aₙ · razão
ARQUIVO_FINAL = "estudativo_MAT-PRO-004_progressao_aritmetica_razao_e_termo_geral.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pa", "formula", "afim", "atalho", "questao", "fim"))
BR = "#FFFFFF"

a_ = lambda n: 5 + (n - 1) * 4
assert [a_(n) for n in (1, 2, 3, 4)] == [5, 9, 13, 17] and a_(20) == 81 and 19 * 4 == 76 and 4 * 20 + 1 == 81
assert 5 + 20 * 4 == 85 and 5 + 1 * 4 == 9 and 17 * 4 == 68 and 13 + 68 == 81
assert 7 + 29 * 5 == 152 and 29 * 5 == 145 and 5 * 30 + 2 == 152


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


# ---------------- gancho ----------------
GX = (300, 540, 780, 1020)


def b_gancho(c, t, C, b):
    def s01():
        cy = 420
        fila(c, t, [(x, v, f"{i + 1}º", C["s01.a"] + 0.48 * i) for i, (x, v) in enumerate(zip(GX, (5, 9, 13, 17)))], cy)
        fila(c, t, [(1260, "…", None, C["s01.b"] - 0.3)], cy)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: caixa(c, 1520, cy, 190, 150, "81" if t >= C["s01.d"] else "?", a, "20º", 80,
                                                     COR if t >= C["s01.d"] else CINZA, COR if t >= C["s01.d"] else None))
        if t >= C["s01.d"]:
            p = prog(t, C["s01.d"], 0.9)
            if p < 1:
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1520 - 95 - 40 * p, cy - 75 - 40 * p, 190 + 80 * p, 150 + 80 * p), 30, 30),
                            M.paint(COR, 1 - p, stroke=6))
        E.saida(c, t, C["s01.c"] - 0.2, lambda: E.frase(c, t, C["s01.b"] + 1.6, ps("escrever a lista inteira…", "i", 70, TINTA2), W / 2, 820, "center", passo=0.12))
        E.frase(c, t, C["s01.c"], [("ou", "i", 84), ("uma", "i", 84), ("conta", "g", 80, COR), ("só", "i", 84)], W / 2, 820, "center")
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 80), XE, 300)
    E.frase(c, t, C["s02.a"] + 1.0, [("a", "i", 110), ("razão", "g", 110, RAZ)], XE, 450)
    E.frase(c, t, C["s02.a"] + 1.6, [("e", "i", 110), ("qualquer", "i", 110), ("termo", "g", 110, COR)], XE, 600)
    # a velha conhecida: os pontos alinhados, sem dizer ainda o nome
    PG = E.Plano(1200, 250, 520, 480, 0, 5, 0, 21)
    if t >= C["s02.b"] - 0.2:
        E.plano(c, t, C["s02.b"] - 0.2, *PG.caixa, 0, 5, 0, 21, passo=1, passo_y=4, rotulos=False, nomes=("", ""), size=30)
        eixos_pa(c, t, C["s02.b"] - 0.2, PG)
        E.curva(c, t, C["s02.b"] + 0.6, PG, lambda x: 4 * x + 1, 0, 5, d=0.9, cor=TINTA2, largura=4, tracejada=True)
        for i in range(1, 5):
            E.ponto(c, t, C["s02.b"] + 0.2 + 0.2 * i, PG, i, a_(i), cor=COR, r=14)
        E.frase(c, t, C["s02.b"], [("uma", "i", 70), ("velha", "i", 70), ("conhecida", "g", 66, COR)], 1460, 880, "center")
    E.foco(c, t, C["s02.b"] + 1.6, 0.5, lambda a: E.pilula(c, "+ atalho de prova", XE + 300, 780, 56, "g", a=a))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você só precisa de", "i", 84), XE, 410)
    E.foco(c, t, C["s03"] + 0.6, 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03"] + 0.75, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.a", "posição e termo", [("a_n", SAI)]), ("s03.b", "função afim", [("vira reta", COR)]), ("s03.c", "equação com", [("parênteses", COR)]))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        fx_em(c, t, C[k] + 0.3, l2, x + 44, y + 162, 64)
    alvo = [(x + w - 30, 190 + i * 240 + 170) for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.b"] - 0.35, 0.5)), ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    py = lerp(lerp(alvo[0][1], alvo[1][1], q1), alvo[2][1], q2)
    E.cursor(c, alvo[0][0], py, ep(t, C["s03.a"], 0.4))


# ---------------- o que é PA ----------------
PX = (480, 760, 1040, 1320)


def b_pa(c, t, C, b):
    def lista():
        cy = 330
        dest = {}
        if C["s05.c"] <= t < C["s05.d"]:
            dest = {0: RAZ, 1: RAZ}
        elif C["s05.d"] <= t < C["s05.e"]:
            dest = {1: RAZ, 2: RAZ}
        fila(c, t, [(x, v, f"{i + 1}º", C["s04"] + 0.15 * i, None, dest.get(i)) for i, (x, v) in enumerate(zip(PX, (5, 9, 13, 17)))], cy)
        fila(c, t, [(1540, "…", None, C["s04"] + 0.6)], cy)
        for i in range(3):
            pula(c, t, C["s04.a"] + 0.45 * i, PX[i], PX[i + 1], cy - 75, "+4")

        def s04():
            E.frase(c, t, C["s04.b"], ps("soma sempre o mesmo número", "i", 76), W / 2, 640, "center")
            E.frase(c, t, C["s04.c"], [("progressão", "g", 104, COR), ("aritmética", "g", 104, COR)], W / 2, 810, "center")
            E.foco(c, t, C["s04.c"] + 0.8, 0.5, lambda a: E.pilula(c, "PA", W / 2, 920, 60, "g", a=a))
        E.saida(c, t, C["s05"] - 0.1, s04)
        if t < C["s05"]:
            return
        E.frase(c, t, C["s05.a"], [("a", "i", 90), ("razão", "g", 96, RAZ)], XE, 650)
        E.frase(c, t, C["s05.b"], [("letra", "i", 80), ("r", "g", 110, RAZ)], XE, 800)
        fx_em(c, t, C["s05.c"], [("9 − 5 = ", TINTA), ("4", RAZ)], 820, 640, 100)
        fx_em(c, t, C["s05.d"], [("13 − 9 = ", TINTA), ("4", RAZ)], 820, 800, 100)
        resultado(c, t, C["s05.e"], "r = 4", 1580, 710, 140, RAZ)
    E.saida(c, t, C["s06"] - 0.1, lista)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("a razão pode ser negativa", "i", 74), W / 2, 130, "center")
    y1, y2 = 420, 800
    XS = (420, 700, 980)
    fila(c, t, [(x, v, f"{i + 1}º", C["s06.a"] + 0.48 * i) for i, (x, v) in enumerate(zip(XS, (20, 17, 14)))], y1)
    for i in range(2):
        pula(c, t, C["s06.b"] + 0.3 * i, XS[i], XS[i + 1], y1 - 75, "−3")
    fx_em(c, t, C["s06.b"] + 0.4, [("r = ", TINTA), ("−3", RAZ)], 1220, y1 + 36, 100)
    E.foco(c, t, C["s06.b"] + 0.6, 0.5, lambda a: E.escreve(c, "a lista desce", 1230, y1 + 120, 52, "i", TINTA2, a))
    fila(c, t, [(x, 6, f"{i + 1}º", C["s06.c"] + 0.2 * i) for i, x in enumerate(XS)], y2)
    for i in range(2):
        pula(c, t, C["s06.c"] + 0.6 + 0.3 * i, XS[i], XS[i + 1], y2 - 75, "+0")
    fx_em(c, t, C["s06.c"] + 0.8, [("r = ", TINTA), ("0", RAZ)], 1220, y2 + 36, 100)
    E.foco(c, t, C["s06.c"] + 1.0, 0.5, lambda a: E.escreve(c, "só se repete", 1230, y2 + 120, 52, "i", TINTA2, a))


# ---------------- saltos ----------------
SX = (300, 540, 780, 1020)


def b_saltos(c, t, C, b):
    cy = 380
    E.saida(c, t, C["s07.c"] - 0.1, lambda: E.frase(c, t, C["s07"] + 1.0, [("quantas", "i", 74), ("vezes", "i", 74), ("soma", "i", 74), ("+4?", "g", 74, RAZ)],
                                                  W / 2, 150, "center"))
    fila(c, t, [(x, v, f"{i + 1}º", C["s07"] + 0.15 * i) for i, (x, v) in enumerate(zip(SX, (5, 9, 13, 17)))], cy, 180, 140, 76)
    fila(c, t, [(1270, "…", None, C["s07"] + 0.6), (1540, "?", "20º", C["s07"] + 0.7, CINZA)], cy, 180, 140, 76)
    pula(c, t, C["s07.a"], SX[0], SX[1], cy - 70, "+4")
    pula(c, t, C["s07.b"], SX[1], SX[2], cy - 70, "+4")
    if t >= C["s07.c"]:
        E.chave(c, SX[0] - 90, 1540 + 90, cy + 140, COR, ep(t, C["s07.c"], 0.6), 26, 6)
        E.foco(c, t, C["s07.c"] + 0.3, 0.5, lambda a: fx(c, [("19", COR), (" saltos de +4", TINTA)], W / 2 + 60, cy + 250, 64, a, "center"))
    rows = (("s07.a", "2º", "1 salto"), ("s07.b", "3º", "2 saltos"))
    for i, (k, pos, s) in enumerate(rows):
        E.frase(c, t, C[k] + 0.2, [(pos, "g", 66, ENT), ("→", "g", 66, TINTA2), (s, "i", 70)], XE + 60, 780 + i * 110)
    E.frase(c, t, C["s07.d"], [("saltos", "i", 84), ("=", "g", 80), ("posição", "g", 80, ENT), ("−", "g", 80), ("1", "g", 80)], 1000, 840)
    p = ep(t, C["s07.d"] + 0.8, 0.5)
    if p > 0:
        w = E.frase(c, t, 1e9, [("saltos", "i", 84), ("=", "g", 80), ("posição", "g", 80, ENT), ("−", "g", 80), ("1", "g", 80)], 1000, 840)
        E.caixa_pontilhada(c, 1000 - 30, 840 - 100, w + 60, 140, p, COR, p)


# ---------------- fórmula do termo geral ----------------
FORM = [("a_n", SAI), (" = ", TINTA), ("a_1", SAI), (" + ", TINTA), ("(", TINTA), ("n", ENT), (" − 1", TINTA), (")", TINTA), (" · ", TINTA), ("r", RAZ)]


def b_formula(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08.a"], ps("a fórmula do termo geral", "i", 80), W / 2, 190, "center")
        y, s = 500, 140
        pos = fx_em(c, t, C["s08.b"], FORM, W / 2, y, s, "center")
        x1, w1 = pos[2]
        caixa_em(c, t, C["s08.c"], x1, w1, y, s, SAI)
        E.foco(c, t, C["s08.c"] + 0.2, 0.4, lambda a: centro(c, "1º termo", x1 + w1 / 2, y + 140, 54, "i", TINTA, a))
        xn, wn = pos[5]
        caixa_em(c, t, C["s08.d"], xn, wn, y, s, ENT)
        E.foco(c, t, C["s08.d"] + 0.2, 0.4, lambda a: centro(c, "posição", xn + wn / 2, y - 170, 54, "i", ENT, a))
        xa, xb = pos[4][0], pos[7][0] + pos[7][1]
        if t >= C["s08.e"]:
            E.chave(c, xa, xb, y + 60, TINTA, ep(t, C["s08.e"], 0.5), 24, 5)
        E.foco(c, t, C["s08.e"] + 0.2, 0.4, lambda a: centro(c, "saltos", (xa + xb) / 2, y + 140, 54, "i", TINTA, a))
        xr, wr = pos[9]
        caixa_em(c, t, C["s08.f"], xr, wr, y, s, RAZ)
        E.foco(c, t, C["s08.f"] + 0.2, 0.4, lambda a: centro(c, "razão", xr + wr / 2 + 20, y + 140, 54, "i", RAZ, a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    fx_em(c, t, C["s09"], FORM, W / 2, 200, 90, "center")
    y1, y2, y3, s = 420, 560, 700, 100
    pos = fx_em(c, t, C["s09.a"], [("a_{20}", SAI), (" = 5 + ", TINTA), ("19", TINTA), (" · ", TINTA), ("4", RAZ)], 460, y1, s)
    xe = pos[1][0]
    fx_em(c, t, C["s09.b"], [(" = 5 + 76", TINTA)], xe, y2, s)
    fx_em(c, t, C["s09.c"], [(" = ", TINTA)], xe, y3, s)
    resultado(c, t, C["s09.c"], "81", xe + 220, y3 - 36, 80)
    fx_em(c, t, C["s09.d"], [("a_3", SAI), (" = 5 + 2 · ", TINTA), ("4", RAZ), (" = 13", TINTA)], 460, 900, 80)
    E.foco(c, t, C["s09.d"] + 4.0, 0.4, lambda a: E.selo(c, 1400, 872, 42, True, a))


# ---------------- PA como função afim ----------------
PL = E.Plano(1060, 190, 700, 700, 0, 5, 0, 21)


def b_afim(c, t, C, b):
    def s10():
        fx_em(c, t, C["s10"], [("a_n", SAI), (" = 5 + (", TINTA), ("n", ENT), (" − 1) · 4", TINTA)], W / 2, 200, 84, "center")
        fx_em(c, t, C["s10.a"], [("a_n", SAI), (" = 5 + 4", TINTA), ("n", ENT), (" − 4", TINTA)], W / 2, 360, 84, "center")
        pos = fx_em(c, t, C["s10.b"], [("a_n", SAI), (" = ", TINTA), ("4", RAZ), ("n", ENT), (" + ", TINTA), ("1", TINTA)], W / 2, 560, 130, "center")
        E.frase(c, t, C["s10.c"], [("função", "i", 70, COR), ("afim:", "i", 70, COR)], XE, 850)
        fx_em(c, t, C["s10.c"] + 0.4, [("f(", TINTA), ("x", ENT), (") = 4", TINTA), ("x", ENT), (" + 1", TINTA)], 1180, 850, 96, "center")
        E.foco(c, t, C["s10.c"] + 1.0, 0.4, lambda a: E.escreve(c, "n no papel do x", 1520, 850, 50, "i", ENT, a))
        x4, w4 = pos[2]
        caixa_em(c, t, C["s10.d"], x4, w4, 560, 130, RAZ)
        E.foco(c, t, C["s10.d"] + 0.2, 0.4, lambda a: centro(c, "razão", x4 + w4 / 2, 690, 52, "i", RAZ, a))
        x1, w1 = pos[5]
        caixa_em(c, t, C["s10.e"], x1, w1, 560, 130, TINTA)
        E.foco(c, t, C["s10.e"] + 0.2, 0.4, lambda a: fx(c, "5 − 4 = 1", x1 + w1 / 2, 690, 52, a, "center", "b", TINTA2))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    fx_em(c, t, C["s11"], [("a_n", SAI), (" = ", TINTA), ("4", RAZ), ("n", ENT), (" + 1", TINTA)], XE, 220, 90)
    E.plano(c, t, C["s11"], *PL.caixa, 0, 5, 0, 21, passo=1, passo_y=4, nomes=("", ""), size=38)
    eixos_pa(c, t, C["s11"], PL)
    for i, k in enumerate(("s11.a", "s11.b", "s11.c")):
        n = i + 1
        E.ponto(c, t, C[k], PL, n, a_(n), guias=True, cor=COR, r=16)
        E.foco(c, t, C[k], 0.4, lambda a, n=n, i=i: par(c, str(n), str(a_(n)), XE + 20, 360 + 100 * i, 72, a))
    if t >= C["s11.d"]:
        E.curva(c, t, C["s11.d"], PL, lambda x: 4 * x + 1, 0, 5, d=1.0, cor=TINTA2, largura=5, tracejada=True)
    E.frase(c, t, C["s11.d"], [("alinhados", "g", 72, COR)], XE, 700)
    t15 = C["s11.d"] + 2.4
    if t >= t15:
        k = ease_back(prog(t, t15, 0.4))
        X, Y = PL(1.5, 7)
        if k > 0:
            c.drawCircle(X, Y, 15 * k, M.paint(ERRADO, 0.9))
            E.risco(c, X - 22, Y - 22, X + 22, Y + 22, t, t15 + 0.5, largura=7)
        E.frase(c, t, t15, [("posição", "i", 64), ("1,5?", "g", 64, ERRADO), ("não", "i", 64), ("existe", "i", 64)], XE, 810)
    E.frase(c, t, C["s11.e"], [("pontos", "g", 66, COR), ("soltos", "i", 70), ("sobre", "i", 70), ("a", "i", 70), ("reta", "i", 70)], XE, 920)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("usar", "i", 80), ("n", "g", 80, ERRADO), ("no", "i", 80), ("lugar", "i", 80), ("de", "i", 80), ("n − 1", "g", 80, CERTO)],
            W / 2, 200, "center")
    pos = fx_em(c, t, C["s12.b"], [("a_{20} = 5 + 20 · 4", ERRADO)], 420, 430, 110)
    xe = pos[0][0] + pos[0][1]
    fx_em(c, t, C["s12.c"], [(" = 85", ERRADO)], xe, 430, 110)
    E.foco(c, t, C["s12.c"] + 0.5, 0.4, lambda a: E.selo(c, xe + 400, 393, 46, False, a))
    if t < C["s13"]:
        return
    pos = fx_em(c, t, C["s13.a"], [("a_1 = 5 + 1 · 4 = 9", ERRADO)], 420, 640, 90)
    xe = pos[0][0] + pos[0][1]
    E.foco(c, t, C["s13.a"] + 2.4, 0.5, lambda a: (fx(c, [("mas ", TINTA2), ("a_1 = 5", CERTO)], xe + 90, 640, 90, a, est="g")))
    E.frase(c, t, C["s13.b"], [("1º", "g", 72, ENT), ("termo:", "i", 74), ("nenhum", "g", 72), ("salto", "i", 74)], W / 2, 820, "center")
    E.frase(c, t, C["s13.c"], [("por", "i", 90), ("isso,", "i", 90), ("n − 1", "g", 96, CERTO)], W / 2, 970, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14.a"], [("pule", "g", 80, BR), ("de", "i", 80, CLARO), ("qualquer", "i", 80, CLARO), ("termo", "i", 80, CLARO)], W / 2, 140, "center")
        cy = 480
        E.foco(c, t, C["s14.b"], 0.5, lambda a: caixa(c, 520, cy, 200, 150, "13", a, "3º", 84, escuro=True))
        E.foco(c, t, C["s14.b"], 0.5, lambda a: fx(c, [("a_3", CLARO)], 300, cy + 30, 76, a, "right"))
        fila(c, t, [(960, "…", None, C["s14.c"] - 0.2)], cy, escuro=True)
        fim = t >= C["s14.e"] + 0.6
        E.foco(c, t, C["s14.c"] - 0.2, 0.5, lambda a: caixa(c, 1400, cy, 200, 150, "81" if fim else "?", a, "20º", 84,
                                                           BR if fim else CINZA, BR if fim else None, True))
        E.salto(c, t, C["s14.c"], 520, 1400, cy - 75 - 8, 150, CLARO, "17 saltos", d=0.9, size=56)
        E.foco(c, t, C["s14.c"] + 0.5, 0.4, lambda a: fx(c, "20 − 3 = 17", W / 2, 700, 64, a, "center", cor=CLARO))
        fx_em(c, t, C["s14.d"], [("17 · 4 = 68", BR)], 560, 860, 96, "center")
        fx_em(c, t, C["s14.e"], [("13 + 68 = ", BR), ("81", CLARO)], 1360, 860, 96, "center")
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("cada", "i", 84, CLARO), ("salto", "g", 80, BR), ("vale", "i", 84, CLARO), ("uma", "i", 84, CLARO), ("razão", "g", 80, BR)],
            W / 2, 220, "center")
    E.frase(c, t, C["s15.b"], [("saltos", "i", 84, CLARO), ("=", "g", 80, BR), ("chegada", "g", 80, BR), ("−", "g", 80, BR), ("partida", "g", 80, BR)],
            W / 2, 380, "center")
    E.foco(c, t, C["s15.c"], 0.5, lambda a: (E.pilula(c, "brilha", 400, 600, 56, "g", fundo=CERTO, a=a),
                                             fx(c, [("deu um termo solto, como ", CLARO), ("a_{10}", BR)], 580, 620, 70, a, est="i")))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: (E.pilula(c, "não compensa", 400, 800, 56, "g", fundo=ERRADO, a=a),
                                             fx(c, [("deu o ", CLARO), ("a_1", BR), (": a fórmula é a mesma conta", CLARO)], 640, 820, 70, a, est="i")))


# ---------------- questão ----------------
QX = (400, 700, 1000)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 150)
    cy = 370
    for i, (x, v, k) in enumerate(zip(QX, (7, 12, 17), ("s16.a", "s16.b", "s16.c"))):
        fila(c, t, [(x, f"R$ {v}", f"{i + 1}ª semana", C[k])], cy, 250, 140, 70, pos_size=40)
    fila(c, t, [(1220, "…", None, C["s16.c"] + 0.8)], cy)
    perg = (("s16.d", [("razão?", RAZ)]), ("s16.e", [("quanto na ", TINTA), ("30ª", ENT), (" semana?", TINTA)]), ("s16.f", [("lei: ", TINTA), ("a_n", SAI), (" = ?", TINTA)]))
    for i, (k, partes) in enumerate(perg):
        y = 630 + i * 135
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 52, "g", BR, a)))
        fx_em(c, t, C[k] + 0.1, partes, XE + 120, y, 70, est="g")
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], 1520, 650, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cy = 230
    RX = (360, 620, 880)
    fila(c, t, [(x, v, f"{i + 1}ª", C["s18"] + 0.1 * i) for i, (x, v) in enumerate(zip(RX, (7, 12, 17)))], cy, 170, 120, 66, pos_size=38)
    for i in range(2):
        pula(c, t, C["s18.a"] + 0.3 * i, RX[i], RX[i + 1], cy - 60, "+5", alto=60, size=46)

    def s18():
        fx_em(c, t, C["s18.a"], [("12 − 7 = 5", TINTA), ("   →   ", TINTA2), ("r = 5", RAZ)], XE, 470, 80)
        E.frase(c, t, C["s18.b"], [("30ª", "g", 74, ENT), ("semana:", "i", 76), ("29", "g", 74, COR), ("saltos", "i", 76)], XE, 600)
        fx_em(c, t, C["s18.c"], "29 · 5 = 145", XE, 730, 80)
        fx_em(c, t, C["s18.d"], [("a_{30}", SAI), (" = 7 + 145 = 152", TINTA)], XE, 860, 80)
        resultado(c, t, C["s18.d"] + 0.6, "R$ 152", 1500, 700, 170)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    fx_em(c, t, C["s19.a"], [("a_n", SAI), (" = 7 + 5", TINTA), ("n", ENT), (" − 5", TINTA)], XE, 480, 90)
    pos = fx_em(c, t, C["s19.b"], [("a_n", SAI), (" = 5", TINTA), ("n", ENT), (" + 2", TINTA)], XE, 640, 120)
    p = ep(t, C["s19.b"] + 0.5, 0.5)
    if p > 0:
        x0 = pos[0][0]
        x1 = pos[-1][0] + pos[-1][1]
        E.caixa_pontilhada(c, x0 - 24, 640 - 120, x1 - x0 + 48, 160, p, COR, p)
    fx_em(c, t, C["s19.c"], [("5 · ", TINTA), ("30", ENT), (" + 2 = 150 + 2 = 152", TINTA)], XE, 850, 84)
    E.foco(c, t, C["s19.c"] + 3.6, 0.4, lambda a: E.selo(c, 1560, 820, 46, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", [("r", RAZ), (" = termo − anterior", TINTA)]),
                 ("s20.b", [("até a posição ", TINTA), ("n", ENT), (": ", TINTA), ("n", ENT), (" − 1 saltos", TINTA)]),
                 ("s20.c", [("PA = função afim nas posições", TINTA)]))
        for i, (k, partes) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a), centro(c, str(i + 1), 330, y - 7, 64, "g", BR, a)))
            fx_em(c, t, C[k] + 0.1, partes, 430, y, 78)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("próxima aula", "i", 80), XE, 260)
    E.frase(c, t, C["s21"] + 0.6, [("Atalhos", "g", 140, COR)], XE, 420)
    E.frase(c, t, C["s21"] + 0.9, [("da", "i", 130), ("PA", "g", 140, COR)], XE, 570)
    fx_em(c, t, C["s21.a"], [("2, ", TINTA), ("x", COR), (", 10", TINTA)], 1150, 260, 84)
    fx_em(c, t, C["s21.b"], [("x − r, x, x + r", TINTA)], 1150, 400, 84)
    E.frase(c, t, C["s21.c"], [("múltiplos", "i", 66), ("de", "i", 66), ("7", "g", 64, COR)], 1150, 520)
    E.frase(c, t, C["s21.c"] + 0.5, [("com", "i", 66), ("3", "g", 64, COR), ("algarismos", "i", 66)], 1150, 600)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 560, 760, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(900, 700, p), lerp(1000, 785, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pa=b_pa, saltos=b_saltos, formula=b_formula, afim=b_afim, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
