"""Visual — Estudativo · QUI-CAL-005: estequiometria de massa a massa.

Segue a linguagem da estequiometria (cabeçalho da QUI-CAL-004), a da trilha (QUI-CAL-001) e a da Química (QUI-MIS-001).
Os quatro passos ficam numa fila de pílulas no alto (passos_fila): a pílula do passo da vez acende na cor da matéria.
A equação fica embaixo dela, com as linhas de Q.sob_termos; a regra de três (Q.regra_tres) entra embaixo das linhas.
No atalho, o dado e o xis ficam EM CIMA da equação (linha_cima), e a massa da equação embaixo: a regra de três sai da coluna.
Peça candidata ao kit quimica.py: passos_fila() e linha_cima() (valores em cima de cada substância da equação)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Cálculos Químicos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-CAL-005_estequiometria_massa_a_massa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "ar", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EQ = "C2H6O + 3 O2 -> 2 CO2 + 3 H2O"
EX, EY, ES = W / 2, 330, 92

# todas as contas da aula
assert Q.lados(EQ)[0] == Q.lados(EQ)[1]
assert 2 * 44 == 88 and 23 * 88 / 46 == 44 and 176 / 88 == 2 and 2 * 46 == 92
assert 3 * 32 == 96 and 3 * 18 == 54 and 46 + 96 == 142 == 88 + 54
assert 230 / 46 == 5 and 5 * 88 == 440


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    tinta = E.SOBRE if cor is None else BR
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", tinta, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def conta(c, t, t0, el, txt, res, x, y, size=72, tr=None, cor_res=None, escuro=False):
    """linha de massa: bolinha do elemento + "6 × 12 =" + parcial na cor da matéria (tr = instante do parcial)"""
    r = size * 0.42
    if el:
        Q.atomo_em(c, t, t0, x + r, y - size * 0.34, r, el, escuro=escuro)
        x += 2 * r + size * 0.4
    E.formula_em(c, t, t0 + 0.1, txt, x, y, size, "g", BR if escuro else TINTA)
    w = E.formula(None, txt, 0, 0, size, a=0)
    if res:
        E.formula_em(c, t, tr if tr is not None else t0 + 0.6, res, x + w + size * 0.3, y, size, "g", cor_res or (E.CLARO if escuro else COR))
    return x + w


def casa(c, cx, cy, s, el, z, m, a=1.0, cor_m=None):
    """casa do elemento na tabela periódica: Z no canto, símbolo, nome e a massa atômica embaixo"""
    if a <= 0:
        return
    w, h = s, s * 1.15
    x, y = cx - w / 2, cy - h / 2
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), s * 0.08, s * 0.08)
    c.drawRRect(rr, M.paint("#FFFFFF", a))
    c.drawRRect(rr, M.paint(E.COR, a, stroke=max(3, s * 0.025)))
    E.escreve(c, str(z), x + s * 0.09, y + s * 0.19, s * 0.14, "b", TINTA2, a)
    centro(c, el, cx, cy + s * 0.1, s * 0.42, "g", TINTA, a)
    centro(c, Q.NOMES[el], cx, cy + s * 0.28, s * 0.12, "i", TINTA2, a)
    centro(c, m, cx, cy + s * 0.5, s * 0.17, "g", cor_m or COR, a)


def casa_em(c, t, t0, cx, cy, s, el, z, m, cor_m=None):
    E.foco(c, t, t0, 0.5, lambda a: casa(c, cx, cy, s, el, z, m, a, cor_m))


def soma_vertical(c, t, tl, nums, tot, xd, y0, size, tt, cor_tot=None):
    """conta armada de somar, alinhada à direita em xd; tt = instante do traço e do total"""
    dy = size * 1.15
    for i, (n, ti) in enumerate(zip(nums, tl)):
        E.foco(c, t, ti, 0.4, lambda a, n=n, i=i: E.formula(c, n, xd, y0 + i * dy, size, "g", TINTA, a, "right"))
    E.foco(c, t, tl[1] if len(tl) > 1 else tl[0], 0.4, lambda a: E.formula(c, "+", xd - size * 2.6, y0 + dy * (len(nums) - 1), size, "g", TINTA2, a))
    p = ep(t, tt, 0.4)
    yl = y0 + (len(nums) - 1) * dy + size * 0.35
    if p > 0:
        M.line(c, xd - size * 2.8, yl, xd + size * 0.2, yl, TINTA, p, 5, progress=ease_out(prog(t, tt, 0.4)))
    return yl


def ponte_mol(c, t, t0, y, esq, meio, dir_, rot_e="", rot_d="", te=None, td=None, xs=(420, 960, 1500), size=58, escuro=False):
    """a ponte do mol: gramas ← → mol ← → moléculas. esq/meio/dir_ = texto de cada margem (ou (texto, instante));
    rot_e / rot_d = operação na pílula de cada vão; te / td = instante de cada vão"""
    tinta = BR if escuro else TINTA
    x0, xm, x1 = xs

    def txt(v):
        return v if isinstance(v, tuple) else (v, t0)
    for k, (v, x) in enumerate(((esq, x0), (dir_, x1))):
        s, ti = txt(v)
        if s:
            E.foco(c, t, ti, 0.45, lambda a, s=s, x=x: E.formula(c, s, x, y + size * 0.36, size, "g", tinta, a, "center"))
    s, ti = txt(meio)
    k = ease_back(prog(t, ti, 0.5))
    if k > 0:
        r = max(size * 1.25, E.formula(None, s, 0, 0, size * 0.8, a=0) * 0.62)
        E.bola(c, xm, y, r * k)
        E.foco(c, t, ti + 0.1, 0.4, lambda a: E.formula(c, s, xm, y + size * 0.29, size * 0.8, "g", E.SOBRE, a, "center"))
    rb = max(size * 1.25, E.formula(None, s, 0, 0, size * 0.8, a=0) * 0.62)
    we = E.formula(None, txt(esq)[0], 0, 0, size, a=0) / 2 if txt(esq)[0] else 60
    wd = E.formula(None, txt(dir_)[0], 0, 0, size, a=0) / 2 if txt(dir_)[0] else 60
    for (xa, xb, rot, tv) in ((x0 + we + 36, xm - rb - 30, rot_e, te), (xm + rb + 30, x1 - wd - 36, rot_d, td)):
        if tv is None:
            continue
        p = ease_io(prog(t, tv, 0.6))
        if p > 0:
            M.arrow(c, xa, y, lerp(xa, xb, p), y, E.CLARO if escuro else E.COR, 1.0, 7, 24, 1.0)
        if rot:
            pilula_em(c, t, tv + 0.3, rot, (xa + xb) / 2, y - 80, 42, TINTA if not escuro else "#24303A")


def pacotes(c, t, t0, n, x, y, w, h, rot, cor=None, passo=0.35, escuro=False):
    """barra cortada em n pacotes iguais que entram um a um, com o rótulo de cada um (quantas vezes cabe)"""
    wk = w / n
    for k in range(n):
        q = ease_back(prog(t, t0 + k * passo, 0.45))
        if q <= 0:
            continue
        xx = x + k * wk
        M.rrect(c, xx + 4, y + h * (1 - q) / 2, wk - 8, h * q, 14, cor or E.COR, 1.0)
        centro(c, rot, xx + wk / 2, y + h / 2 + h * 0.18, h * 0.5, "g", E.SOBRE, min(1, q))


def chip(c, s, cx, cy, size, fundo=None, a=1.0, escuro=True):
    """fórmula química dentro de uma pílula do tamanho dela"""
    if a <= 0:
        return
    w = Q.formula(None, s, 0, 0, size) + size * 0.9
    M.rrect(c, cx - w / 2, cy - size * 0.8, w, size * 1.6, size * 0.8, fundo or E.COR, a)
    Q.formula(c, s, cx, cy + size * 0.36, size, BR, a, "center", escuro=escuro)


def passos_fila(c, t, tl, nomes, y=160, atual=None):
    """os passos do método numa fila de pílulas; tl = instante de cada uma; a última que entrou fica na cor da matéria"""
    xs, x = [], 0
    ws = [E.larg(f"{i + 1}  {n}", "b", 40) + 70 for i, n in enumerate(nomes)]
    x0 = W / 2 - (sum(ws) + 24 * (len(ws) - 1)) / 2
    k_at = max([i for i, ti in enumerate(tl) if t >= ti], default=-1) if atual is None else atual
    for i, (n, ti, w) in enumerate(zip(nomes, tl, ws)):
        cx = x0 + w / 2
        E.foco(c, t, ti, 0.4, lambda a, i=i, n=n, cx=cx: E.pilula(c, f"{i + 1}  {n}", cx, y, 40, "b", fundo=E.COR if i == k_at else "#5A5F66", a=a))
        x0 += w + 24


def linha_cima(c, t, s, x, y, size, vals, tl, cor=None, escuro=False):
    """valores em cima de cada substância da equação (o dado e o xis)"""
    cs = Q.centros(s, x, y, size)
    for cx, v, ti in zip(cs, vals, tl):
        if v:
            E.foco(c, t, ti, 0.4, lambda a, cx=cx, v=v: E.formula(c, v, cx, y - size * 1.05, size * 0.7, "g", cor or (E.CLARO if escuro else COR), a, "center"))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.formula_em(c, t, C["s01.a"], "C2H6O", XE, 330, 150)
        E.frase(c, t, C["s01.a"] + 0.8, [("46 g", "g", 110, TINTA)], XE, 500)
        E.frase(c, t, C["s01.a"] + 1.4, ps("de etanol queimados", "i", 56, TINTA2), XE, 580, passo=0.1)
        p = ep(t, C["s01.b"] - 0.3, 0.6)
        if p > 0:
            M.arrow(c, 760, 420, lerp(760, 1040, ease_io(p)), 420, E.COR, 1.0, 8, 26)
        Q.formula_em(c, t, C["s01.b"], "CO2", 1120, 330, 150)
        E.frase(c, t, C["s01.b"] + 0.5, [("88 g", "g", 110, COR)], 1120, 500)
        E.frase(c, t, C["s01.b"] + 1.1, ps("de gás carbônico", "i", 56, TINTA2), 1120, 580, passo=0.1)
        pilula_em(c, t, C["s01.c"], "quase o dobro", 1560, 470, 50, TINTA)
        E.frase(c, t, C["s01.d"], ps("de onde vem a massa a mais?", "i", 76), XE, 800, passo=0.12)
        E.frase(c, t, C["s01.e"], ps("e a conta em", "i", 66, TINTA2) + [("uma linha", "g", 62, COR)], XE, 930, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("massa", "g", 70), ("→", "g", 70, TINTA2), ("massa", "g", 70, COR)]),
                 (C["s02.c"], [("o", "i", 74), ("atalho", "g", 70, COR), ("das", "i", 74), ("massas", "g", 70)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 80) + [("duas coisas", "g", 76, COR)], XE, 200, passo=0.12)
    y = [430, 760]
    for i, k in enumerate(("s03.b", "s03.c")):
        E.foco(c, t, C[k], 0.5, lambda a, i=i: (E.bola(c, XE + 40, y[i] - 30, 44, a=a), centro(c, str(i + 1), XE + 40, y[i] - 8, 54, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("equação em mols, mol em grama", "i", 66), XE + 110, y[0])
    Q.formula_em(c, t, C["s03.b"] + 1.0, "2 H2 + O2 → 2 H2O", XE + 110, y[0] + 130, 80, cores={"coef": E.COR})
    E.formula_em(c, t, C["s03.b"] + 1.6, "1 mol = 32 g", XE + 1060, y[0] + 130, 64, "g", COR)
    E.frase(c, t, C["s03.c"] + 0.1, ps("regra de três", "i", 66), XE + 110, y[1])
    E.formula_em(c, t, C["s03.c"] + 0.6, "f{3}{7} = f{18}{x}", XE + 600, y[1] + 10, 70, "g", TINTA)


# ---------------- o método ----------------
NOMES = ("equação", "mols", "gramas", "regra de três")


def b_metodo(c, t, C, b):
    if t < C["s04.b"]:
        E.frase(c, t, C["s04.a"], [("estequiometria", "g", 110, COR)], XE, 420)
        E.frase(c, t, C["s04.a"] + 1.2, ps("a conta das quantidades numa reação", "i", 70, TINTA2), XE, 540, passo=0.1)
        return
    passos_fila(c, t, [C["s04.b"], C["s05.a"], C["s06.a"], C["s07.a"]], NOMES)
    tc = C["s04.c"]
    Q.equacao(c, t, tc, EQ, EX, EY, ES, tl=[tc + 0.3 * k for k in range(7)], cores={"coef": E.COR})
    E.saida(c, t, C["s05"], lambda: E.foco(c, t, tc + 2.4, 0.4, lambda a: centro(c, "a queima do etanol", EX, EY + 90, 44, "i", TINTA2, a)))
    if t >= C["s05"]:
        Q.sob_termos(c, t, EQ, EX, EY, ES, [["1 mol", "", "2 mol", ""]], tl=[[C["s05.b"], 0, C["s05.c"], 0]], size_l=70, cores_l=[COR], dy=100)
    if t >= C["s06"]:
        Q.sob_termos(c, t, EQ, EX, EY + 100, ES, [["46 g", "", "2 × 44 = 88 g", ""]], tl=[[C["s06.b"], 0, C["s06.c"], 0]], size_l=64, dy=100)
    if C["s07"] <= t < C["s08"]:
        Q.regra_tres(c, t, C["s07.b"] - 0.3, ("etanol", "gás carbônico"), [("46 g", "88 g"), ("23 g", "x")], 700, 700, 74,
                     tl=[C["s07.b"], C["s07.c"]], res="44 g", tres=C["s07.d"], dx=520, x_res=1500)
    if t >= C["s08"]:
        def volta():
            E.frase(c, t, C["s08.a"], ps("a conta anda", "i", 66) + [("ao contrário", "g", 62, COR)], XE, 680, passo=0.12)
            E.formula_em(c, t, C["s08.b"], "? g de etanol → 176 g de gás carbônico", XE, 800, 66, "g", TINTA)
            E.formula_em(c, t, C["s08.c"], "176 = 2 × 88", XE, 930, 74, "g", TINTA2)
            E.formula_em(c, t, C["s08.d"], "→ 2 × 46 =", XE + 620, 930, 74, "g", TINTA2)
            bola_txt(c, t, C["s08.e"], "92 g", XE + 1130, 905, 82, 56)
        volta()


# ---------------- a massa a mais ----------------
def b_ar(c, t, C, b):
    Q.equacao(c, t, C["s09"], EQ, EX, 280, ES, tl=[C["s09"]] * 7, cores={"coef": E.COR})
    Q.sob_termos(c, t, EQ, EX, 280, ES, [["46 g", "96 g", "88 g", "54 g"]], tl=[[C["s09"], C["s09.b"], C["s09"], C["s09.d"]]], size_l=66, dy=100)
    pilula_em(c, t, C["s09.a"], "veio do ar", Q.centros(EQ, EX, 280, ES)[1], 150, 44, E.COR)
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: centro(c, "3 × 32", Q.centros(EQ, EX, 280, ES)[1], 470, 44, "b", TINTA2, a))
    E.foco(c, t, C["s09.d"] + 0.3, 0.4, lambda a: centro(c, "3 × 18", Q.centros(EQ, EX, 280, ES)[3], 470, 44, "b", TINTA2, a))
    E.foco(c, t, C["s09.c"], 0.6, lambda a: E.balanca(c, W / 2, 800, "46 + 96" if t < C["s09.d"] else "46 + 96", "88 + 54" if t >= C["s09.d"] else "", 0.0, a, 72, larg_braco=820))
    E.foco(c, t, C["s09.c"] + 1.0, 0.4, lambda a: centro(c, "142 g", W / 2 - 410, 1000, 60, "g", COR, a))
    E.foco(c, t, C["s09.d"] + 1.0, 0.4, lambda a: centro(c, "142 g", W / 2 + 410, 1000, 60, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("esquecer o coeficiente", "i", 72), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s10.a"] + 0.4, EQ, EX, 420, ES, align="center", cores={"coef": E.COR} if t >= C["s10.d"] else None)
    cs = Q.centros(EQ, EX, 420, ES)

    def errado():
        E.foco(c, t, C["s10.b"], 0.4, lambda a: E.formula(c, "44 g", cs[2], 560, 76, "g", ERRADO, a, "center"))
        E.foco(c, t, C["s10.b"] + 0.4, 0.4, lambda a: centro(c, "de um mol só", cs[2], 630, 44, "i", ERRADO, a))
        if t >= C["s10.c"]:
            E.risco(c, cs[2] - 110, 575, cs[2] + 110, 500, t, C["s10.c"], largura=10)
            pilula_em(c, t, C["s10.c"] + 0.2, "a metade do certo", cs[2] + 400, 540, 46, ERRADO)
    E.saida(c, t, C["s10.d"] - 0.1, errado)
    if t >= C["s10.d"]:
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.formula(c, "2 × 44 = 88 g", cs[2], 570, 76, "g", COR, a, "center"))
        E.frase(c, t, C["s10.d"] + 0.6, [("massa", "g", 66), ("=", "g", 66, TINTA2), ("coeficiente", "g", 66, COR), ("×", "g", 66, TINTA2), ("massa molar", "g", 66)], W / 2, 820, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    y = 480
    E.frase(c, t, C["s11"], ps("o atalho:", "i", 72, CLARO) + [("massas embaixo da equação", "g", 64, BR)], W / 2, 160, "center", 0.12)
    apaga = ep(t, C["s12.b"], 0.5)
    cs = Q.centros(EQ, EX, y, ES)
    Q.equacao(c, t, C["s11.a"], EQ, EX, y, ES, tl=[C["s11.a"]] * 7, escuro=True, cores={"coef": E.CLARO})
    if apaga > 0:
        for k in (1, 3):
            M.rrect(c, cs[k] - 150, y - 110, 300, 160, 20, "#0B0E14", 0.75 * apaga)
    Q.sob_termos(c, t, EQ, EX, y, ES, [["46 g", "", "88 g", ""]], tl=[[C["s11.c"], 0, C["s11.d"], 0]], size_l=74, escuro=True)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: centro(c, "coeficiente × massa molar", W / 2, 700, 50, "i", CLARO, a))
    linha_cima(c, t, EQ, EX, y, ES, ["23 g", "", "x", ""], [C["s11.e"], 0, C["s11.e"] + 0.4, 0], escuro=True)
    E.foco(c, t, C["s11.f"], 0.5, lambda a: E.formula(c, "x = f{23 × 88}{46} = 44 g", W / 2, 880, 76, "g", BR, a, "center"))
    E.frase(c, t, C["s12.a"], ps("a proporção das massas é", "i", 60, CLARO) + [("fixa", "g", 58, BR)], W / 2, 1010, "center", 0.1) if t < C["s12.d"] else None
    pilula_em(c, t, C["s12.c"], "pule o oxigênio e a água", W / 2, 1010, 44, "#24303A") if C["s12.c"] <= t < C["s12.d"] else None
    if t >= C["s12.d"]:
        E.frase(c, t, C["s12.d"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("pediu mols? pare na linha dos mols", "i", 64, CLARO), W / 2, 1010, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s13.a"], ps("um fogareiro queima", "i", 70) + [("230 g", "g", 66, COR)] + ps("de etanol", "i", 70), XE, 330, passo=0.1)
    Q.formula_em(c, t, C["s13.a"] + 0.5, EQ, XE, 520, 76, cores={"coef": E.COR})
    E.frase(c, t, C["s13.b"], ps("quantos gramas de", "i", 66) + [("gás carbônico?", "g", 62, COR)], XE, 720, passo=0.1)
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1520, cy=780, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.equacao(c, t, C["s15"], EQ, EX, 300, ES, tl=[C["s15"]] * 7, cores={"coef": E.COR})
    linha_cima(c, t, EQ, EX, 300, ES, ["230 g", "", "x", ""], [C["s15"] + 0.4, 0, C["s15"] + 0.6, 0])
    Q.sob_termos(c, t, EQ, EX, 300, ES, [["46 g", "", "88 g", ""]], tl=[[C["s15.a"], 0, C["s15.a"] + 0.6, 0]], size_l=72)
    E.formula_em(c, t, C["s15.b"], "230 ÷ 46 = 5", XE, 680, 90, "g", TINTA)
    pilula_em(c, t, C["s15.c"], "5 vezes mais etanol", XE + 1000, 650, 46, E.COR)
    E.formula_em(c, t, C["s15.d"], "5 × 88 =", XE, 880, 90, "g", TINTA2)
    bola_txt(c, t, C["s15.d"] + 0.8, "440 g", XE + 620, 850, 100, 64, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for i, (k, n) in enumerate(zip(("s16.a", "s16.b", "s16.c", "s16.d"), ("equação balanceada", "mols da pergunta", "mols em gramas", "regra de três"))):
            y = 340 + i * 130
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 24, 46, a=a), centro(c, str(i + 1), 300, y - 4, 54, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(n, "g", 64)], 390, y)
        E.frase(c, t, C["s16.e"], ps("ou, pelo atalho:", "i", 66, TINTA2) + [("massas embaixo da equação", "g", 60, COR)], 300, 900, passo=0.1)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s17.a"], ps("reagentes", "i", 80) + [("fora da proporção", "g", 76, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s17.b"], ps("quem acaba primeiro?", "i", 76) + [("quanto sobra?", "g", 70)], XE, 600, passo=0.12)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 780, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 805, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, ar=b_ar, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
