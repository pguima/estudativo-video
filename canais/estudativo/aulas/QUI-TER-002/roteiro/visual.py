"""Visual — Estudativo · QUI-TER-002: lei de Hess.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho da QUI-MIS-001) e a da trilha Termoquímica e Cinética (cabeçalho da QUI-TER-001):
ΔH < 0 em azul (Q.ELETRON), ΔH > 0 em âmbar; patamares de entalpia; conta de apoio em TINTA2 e resultado na esfera.
Nesta aula: cada equação dada é uma LINHA (equação à esquerda, ΔH alinhado à direita, na cor do sinal). Inverter = a linha
gira e o sinal troca de cor; multiplicar = pílula "× 2" ou "× ½" na frente; cancelar = risco cinza sobre a espécie repetida.
O alvo fica no alto, numa caixa pontilhada turquesa. Coeficiente fracionário que não é ½ (3/2) sai com eq_frac.
Peças candidatas ao kit: linha_eq (equação com ΔH à direita), eq_frac (coeficiente em fração), predio (Hess como altura).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Termoquímica e Cinética")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-TER-002_lei_de_hess.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "regras", "exemplo", "formacao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AZUL, AMBAR = Q.ELETRON, "#E8A317"

# as contas da aula
assert -394 + 283 == -111 and -394 - 283 == -677
assert -394 + 2 * (-286) == -966 and -966 - (-75) == -891
assert 198 // 2 == 99 and -297 - 99 == -396
for eq in ("C + O2 -> CO2", "CO + ½ O2 -> CO2", "CH4 + 2 O2 -> CO2 + 2 H2O", "S + O2 -> SO2", "2 SO3 -> 2 SO2 + O2"):
    if "½" not in eq:
        assert Q.lados(eq)[0] == Q.lados(eq)[1], eq


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
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def cor_dh(v):
    return AZUL if v < 0 else AMBAR


def txt_dh(v):
    return ("+" if v > 0 else "−") + str(abs(v))


def dh_txt(c, v, x, y, size, a=1.0, align="right", escuro=False, kj=True):
    """'ΔH = −394 kJ', alinhado pela direita em x"""
    tinta = BR if escuro else TINTA
    w1 = E.formula(None, "ΔH = ", 0, 0, size, a=0)
    num = txt_dh(v) + (" kJ" if kj else "")
    w2 = E.formula(None, num, 0, 0, size, a=0)
    x0 = x - w1 - w2 if align == "right" else x - (w1 + w2) / 2 if align == "center" else x
    E.formula(c, "ΔH = ", x0, y, size, "g", TINTA2 if not escuro else CLARO, a)
    E.formula(c, num, x0 + w1, y, size, "g", cor_dh(v), a)


def linha_eq(c, t, t0, s, v, x, y, size, xdh, cores=None, escuro=False, tdh=None):
    """equação à esquerda e ΔH à direita (alinhado em xdh)"""
    Q.formula_em(c, t, t0, s, x, y, size, cores=cores, escuro=escuro)
    E.foco(c, t, t0 + 0.3 if tdh is None else tdh, 0.4, lambda a: dh_txt(c, v, xdh, y, size * 0.9, a, escuro=escuro))


def eq_frac(c, partes, x, y, size, a=1.0, cor=None, escuro=False):
    """equação com coeficiente em fração: partes = [("q", "S"), ("t", "+"), ("f", "3", "2"), ("q", "O2 -> SO3")]"""
    cor = cor or (BR if escuro else TINTA)
    xx = x
    for p in partes:
        if p[0] == "q":
            xx += Q.formula(c, p[1], xx, y, size, cor, a, escuro=escuro) + size * 0.25
        elif p[0] == "t":
            xx += E.formula(c, p[1], xx, y, size, "g", cor, a) + size * 0.25
        else:
            xx += E.formula(c, "f{%s}{%s}" % (p[1], p[2]), xx, y, size * 0.9, "g", cor, a) + size * 0.12
    return xx - x


def risca(c, t, t0, g, cor=CINZA):
    """risco cinza de cancelamento sobre um grupo da fórmula"""
    if t >= t0:
        E.risco(c, g["x0"] - 8, g["base"] + 4, g["x1"] + 8, g["topo"] - 4, t, t0, cor=cor, largura=8)


def grupo_de(s, x, y, size, quero, k=0):
    """o k-ésimo grupo do símbolo 'quero' (com coeficiente, se houver) na fórmula"""
    G = [g for g in Q.grupos(s, x, y, size) if g["tipo"] != "coef"]
    alvo = [g for g in G if g["s"] == quero]
    return alvo[k]


def especie(s, x, y, size, k):
    """a caixa da k-ésima espécie (0, 1, 2...) de uma equação: x0, x1, topo, base"""
    cs = Q.centros(s, x, y, size, "left")
    G = Q.grupos(s, x, y, size)
    larg = [Q.formula(None, e, 0, 0, size) for e in _especies(s)]
    cx = cs[k]
    return dict(x0=cx - larg[k] / 2, x1=cx + larg[k] / 2, topo=G[0]["topo"], base=G[0]["base"])


def _especies(s):
    s = s.replace("->", "+")
    return [p.strip() for p in s.split(" + ")]


def predio(c, t, t0, x, yb, w, andares, h_andar, a=1.0):
    """prédio de frente com os andares numerados à direita"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, x, yb - andares * h_andar - 30, w, andares * h_andar + 30, 12, "#D9DCE1", q)
    for k in range(andares + 1):
        yy = yb - k * h_andar
        M.line(c, x, yy, x + w, yy, TINTA2, 0.5 * q, 3)
        centro(c, "térreo" if k == 0 else f"{k}º", x + w + 70, yy - 10, 36, "b", TINTA2, q)
        for j in range(3):
            if k < andares:
                M.rrect(c, x + 30 + j * (w - 60) / 3, yy - h_andar + 20, (w - 60) / 3 - 20, h_andar - 40, 6, "#AEB8C4", q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("carvão com pouco ar forma", "i", 66), XE, 230, passo=0.1)
        Q.formula_em(c, t, C["s01.a"] + 1.2, "CO", XE, 470, 220, cores={"CO": E.COR})
        Q.molecula(c, t, C["s01.a"] + 1.4, "CO", XE + 560, 400, 130, passo=0.2)
        E.foco(c, t, C["s01.a"] + 1.8, 0.4, lambda a: E.escreve(c, "monóxido de carbono", XE, 560, 52, "i", TINTA2, a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (E.formula(c, "ΔH = ?", 1260, 430, 150, "g", TINTA, a)))
        if t >= C["s01.b"] + 0.6:
            pilula_em(c, t, C["s01.b"] + 0.6, "não dá para medir direto", 1480, 540, 44, ERRADO, "b")
        E.frase(c, t, C["s01.c"], ps("junto, sempre sai um pouco de", "i", 60, TINTA2), XE, 740, passo=0.1)
        Q.formula_em(c, t, C["s01.c"] + 1.0, "CO2", XE + 900, 750, 100)
        Q.molecula(c, t, C["s01.c"] + 1.2, "CO2", XE + 1350, 720, 90, passo=0.15)
        E.frase(c, t, C["s01.d"], ps("mas o valor está em", "i", 64) + [("qualquer tabela", "g", 60, COR)], XE, 930, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 560, 290 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], [("lei", "g", 110, COR), ("de", "i", 110), ("Hess", "g", 110, COR)], XE, 300, passo=0.14)
    lista(c, t, [(C["s02.b"], [("somar", "g", 70), ("equações", "i", 74)]),
                 (C["s02.c"], [("inverter", "g", 70), ("e", "i", 74), ("multiplicar", "g", 70)]),
                 (C["s02.d"], [("entalpias", "g", 70), ("de", "i", 74), ("formação", "g", 70, COR)])], XE, 500, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 80, TINTA2), XE, 220, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.formula(c, "ΔH = chegada − partida", XE, 380, 90, "g", TINTA, a))
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.formula(c, "ΔH < 0", XE, 540, 90, "g", AZUL, a), E.escreve(c, "libera", XE + 380, 535, 64, "i", TINTA2, a)))
    E.foco(c, t, C["s03.b"] + 0.8, 0.5, lambda a: (E.formula(c, "ΔH > 0", XE + 760, 540, 90, "g", AMBAR, a), E.escreve(c, "absorve", XE + 1140, 535, 64, "i", TINTA2, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: E.formula(c, "f{1}{2} × 198 = 99", XE, 760, 90, "g", TINTA, a))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: E.formula(c, "−(−283) = +283", XE + 900, 760, 90, "g", TINTA, a))


# ---------------- a ideia: o caminho não importa ----------------
def b_ideia(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], ps("o", "i", 72) + [("ΔH", "g", 68, COR)] + ps("só depende do começo e do fim", "i", 72), XE, 200, passo=0.1)
        E.frase(c, t, C["s04.b"], [("não", "g", 66, ERRADO)] + ps("do caminho", "i", 72), XE, 300, passo=0.12)
        px, yb, hh = 760, 960, 105
        predio(c, t, C["s04.c"], px, yb, 380, 5, hh)
        if t >= C["s04.d"]:
            p = ease_io(prog(t, C["s04.d"], 1.6))
            pts = [(px - 60 - (60 if k % 2 else 0), yb - k * hh / 2) for k in range(11)]
            F.poli(c, pts, p, TINTA, 1, 7)
            M.line(c, px + 440 + 120, yb, px + 440 + 120, yb - (5 * hh) * p, E.COR, 1, 9)
            E.foco(c, t, C["s04.d"], 0.4, lambda a: (centro(c, "escada", px - 90, yb + 60, 44, "i", TINTA, a),
                                                     centro(c, "elevador", px + 560, yb + 60, 44, "i", COR, a)))
        if t >= C["s04.e"]:
            q = ep(t, C["s04.e"], 0.5)
            F.seta(c, 1500, yb, 1500, yb - 5 * hh, TINTA, q, 6, 24, ease_out(prog(t, C["s04.e"], 0.6)))
            E.foco(c, t, C["s04.e"] + 0.3, 0.4, lambda a: (E.escreve(c, "a mesma", 1540, 700, 66, "i", TINTA, a), E.escreve(c, "altura", 1540, 790, 70, "g", COR, a)))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    # o mesmo com a reação: três patamares
    x0 = 420
    ys = {"C": 330, "CO": 560, "CO2": 900}
    for k, (key, txt, tt) in enumerate((("C", "C + O2", C["s05"]), ("CO", "CO + ½ O2", C["s05.a"]), ("CO2", "CO2", C["s05.b"]))):
        p = ease_io(prog(t, tt, 0.6))
        if p > 0:
            M.line(c, x0, ys[key], x0 + 380 * p, ys[key], E.COR if key == "CO" else TINTA, 1, 10)
            E.foco(c, t, tt + 0.2, 0.4, lambda a, txt=txt, key=key: Q.formula(c, txt, x0 + 190, ys[key] - 26, 60, TINTA, a, "center"))
    if t >= C["s05.a"]:
        q = ep(t, C["s05.a"], 0.5)
        F.seta(c, x0 + 470, ys["C"], x0 + 470, ys["CO"] - 8, AZUL, q, 7, 26, ease_out(prog(t, C["s05.a"], 0.6)))
        E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: E.escreve(c, "direto", x0 + 500, (ys["C"] + ys["CO"]) / 2 + 16, 50, "i", TINTA, a))
    if t >= C["s05.b"]:
        q = ep(t, C["s05.b"], 0.5)
        F.seta(c, x0 + 760, ys["C"], x0 + 760, ys["CO2"] - 8, AZUL, q, 7, 26, ease_out(prog(t, C["s05.b"], 0.6)))
        F.seta(c, x0 + 900, ys["CO2"], x0 + 900, ys["CO"] + 8, AMBAR, ep(t, C["s05.b"] + 0.8, 0.5), 7, 26, ease_out(prog(t, C["s05.b"] + 0.8, 0.6)))
        E.foco(c, t, C["s05.b"] + 1.2, 0.4, lambda a: E.escreve(c, "pelo gás carbônico", x0 + 940, 760, 50, "i", TINTA, a))
    if t >= C["s05.c"]:
        pilula_em(c, t, C["s05.c"], "mesmo ΔH", 1560, 460, 60, E.COR)
    E.frase(c, t, C["s05.d"], ps("monte a reação com equações", "i", 60) + [("já medidas", "g", 56, COR)], W / 2, 1030, "center", 0.1)


# ---------------- as três regras ----------------
def b_regras(c, t, C, b):
    E.frase(c, t, C["s06.a"], ps("três regras", "i", 80, TINTA2), XE, 170, passo=0.12)
    linhas = ((C["s06.b"], "1", "inverteu", "troca o sinal"), (C["s07.a"], "2", "multiplicou", "multiplica o ΔH"),
              (C["s07.c"], "3", "somou", "soma os ΔH"))
    for k, (tt, n, v1, v2) in enumerate(linhas):
        y = 340 + k * 250
        E.foco(c, t, tt, 0.5, lambda a, y=y, n=n: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, n, XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, tt + 0.1, [(v1, "g", 58), ("→", "g", 58, TINTA2), (v2, "g", 56, COR)], XE + 110, y, passo=0.15)
    # os exemplos de cada regra, à direita
    xe = 1150
    E.foco(c, t, C["s06.c"], 0.5, lambda a: (E.formula(c, "A → B", xe, 320, 64, "g", TINTA, a), dh_txt(c, -100, 1790, 320, 58, a, kj=False)))
    E.foco(c, t, C["s06.c"] + 0.8, 0.5, lambda a: (E.formula(c, "B → A", xe, 400, 64, "g", TINTA, a), dh_txt(c, 100, 1790, 400, 58, a, kj=False)))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: (E.formula(c, "2 A → 2 B", xe, 600, 64, "g", TINTA, a), dh_txt(c, -200, 1790, 600, 58, a, kj=False)))
    pilula_em(c, t, C["s07.b"] + 0.4, "× 2", xe + 120, 520, 40, E.COR)
    if t >= C["s07.d"]:
        E.foco(c, t, C["s07.d"], 0.5, lambda a: (E.formula(c, "A → B", xe, 820, 60, "g", TINTA, a), E.formula(c, "B → C", xe + 330, 820, 60, "g", TINTA, a)))
        E.foco(c, t, C["s07.d"] + 0.8, 0.5, lambda a: E.formula(c, "A → C", xe + 160, 930, 70, "g", COR, a))
        wa = E.formula(None, "A → ", 0, 0, 60, a=0)
        wb = E.formula(None, "B", 0, 0, 60, a=0)
        for xx in (xe + wa, xe + 330):
            if t >= C["s07.d"] + 0.5:
                E.risco(c, xx - 8, 830, xx + wb + 8, 770, t, C["s07.d"] + 0.5, cor=CINZA, largura=7)


# ---------------- exemplo: o monóxido ----------------
EQ1, EQ2, EQ2I = "C + O2 -> CO2", "CO + ½ O2 -> CO2", "CO2 -> CO + ½ O2"
EX, XD, S1 = 330, 1780, 84


def b_exemplo(c, t, C, b):
    # o alvo
    q = ep(t, C["s08.a"], 0.5)
    if q > 0:
        E.caixa_pontilhada(c, EX - 30, 150, 1080, 120, q, E.COR, prog_=q)
    Q.formula_em(c, t, C["s08.a"], "C + ½ O2 -> CO", EX, 232, S1)
    E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: E.escreve(c, "alvo", EX + 1110, 230, 50, "i", COR, a))
    # equação 1
    linha_eq(c, t, C["s08.b"], EQ1, -394, EX, 420, S1, XD, cores={"C": E.COR} if C["s09.a"] <= t < C["s09.c"] else None)
    pilula_em(c, t, C["s09.b"], "fica", EX - 120, 395, 40, TINTA)
    # equação 2, depois invertida
    inv = t >= C["s09.d"]
    if not inv:
        linha_eq(c, t, C["s08.c"], EQ2, -283, EX, 570, S1, XD, cores={"CO": E.COR} if t >= C["s09.c"] else None)
    else:
        p = ease_io(prog(t, C["s09.d"], 0.6))
        k = abs(1 - 2 * p)
        c.save(); c.translate(0, 570 - 30); c.scale(1, max(0.05, k)); c.translate(0, -(570 - 30))
        Q.formula(c, EQ2 if p < 0.5 else EQ2I, EX, 570, S1, cores={"CO": E.COR})
        c.restore()
        E.foco(c, t, C["s09.e"], 0.4, lambda a: dh_txt(c, 283, XD, 570, S1 * 0.9, a))
        if t < C["s09.e"]:
            dh_txt(c, -283, XD, 570, S1 * 0.9, 1 - ep(t, C["s09.d"], 0.3))
        pilula_em(c, t, C["s09.d"] + 0.3, "invertida", EX - 150, 545, 40, AMBAR)
    # a soma
    if t >= C["s10.a"]:
        q = ep(t, C["s10.a"], 0.4)
        M.line(c, EX, 640, XD, 640, TINTA, q, 5)
        E.foco(c, t, C["s10.a"], 0.4, lambda a: centro(c, "+", EX - 60, 660, 70, "g", TINTA2, a))
    if t >= C["s10.b"]:
        g1 = especie(EQ1, EX, 420, S1, 2)
        g2 = especie(EQ2I, EX, 570, S1, 0)
        risca(c, t, C["s10.b"], g1)
        risca(c, t, C["s10.b"] + 0.3, g2)
    if t >= C["s10.c"]:
        E.frase(c, t, C["s10.c"], [("O₂:", "g", 52, TINTA2), ("1 − ½ = ½", "g", 52, TINTA2)], EX, 730, passo=0.15)
    if t >= C["s10.d"]:
        Q.formula_em(c, t, C["s10.d"], "C + ½ O2 -> CO", EX, 860, S1, cores={"CO": E.COR})
    E.formula_em(c, t, C["s10.e"], "−394 + 283 =", 1500, 990, 70, "g", TINTA2, "right")
    bola_txt(c, t, C["s10.f"], "−111", 1640, 965, 90, 62, AZUL)
    E.foco(c, t, C["s10.f"] + 0.3, 0.4, lambda a: E.escreve(c, "kJ", 1745, 990, 56, "g", TINTA, a))


# ---------------- entalpia de formação ----------------
EQM = "CH4 + 2 O2 -> CO2 + 2 H2O(l)"


def b_formacao(c, t, C, b):
    if t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11.a"], [("entalpia", "g", 110, COR), ("de", "i", 110), ("formação", "g", 110, COR)], XE, 260, passo=0.14)
            E.frase(c, t, C["s11.b"], ps("o", "i", 64) + [("ΔH", "g", 60)] + ps("de formar uma substância, com coeficiente 1,", "i", 64), XE, 400, passo=0.08)
            E.frase(c, t, C["s11.b"] + 1.6, ps("a partir de substâncias simples", "i", 64), XE, 480, passo=0.1)
            E.frase(c, t, C["s11.c"], [("substância simples", "g", 60), ("=", "g", 60, TINTA2)] + ps("um elemento só", "i", 64), XE, 640, passo=0.12)
            for k, mol in enumerate(("O2", "H2")):
                Q.molecula(c, t, C["s11.c"] + 0.8 + 0.3 * k, mol, 1400 + 260 * k, 620, 90, passo=0.15)
            E.foco(c, t, C["s11.d"], 0.5, lambda a: (E.formula(c, "formação = 0", XE, 860, 110, "g", COR, a)))
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    if t < C["s13"]:
        def s12():
            E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "ΔH = produtos − reagentes", W / 2, 360, 100, "g", TINTA, a, "center"))
            E.frase(c, t, C["s12.b"], ps("somando as", "i", 64) + [("formações", "g", 60, COR)] + ps("de cada lado", "i", 64), W / 2, 500, "center", 0.1)
            pilula_em(c, t, C["s12.c"], "cada uma × o seu coeficiente", W / 2, 640, 56, E.COR)
            E.frase(c, t, C["s12.c"] + 1.4, ps("é o mesmo chegada menos partida", "i", 60, TINTA2), W / 2, 800, "center", 0.1)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], ps("a queima do metano", "i", 64, TINTA2), XE, 160, passo=0.1)
    cores = {"coef": E.COR} if t >= C["s14.a"] else None
    cs = Q.equacao(c, t, C["s13.a"], EQM, W / 2, 330, 96, tl=[C["s13.a"] + 0.2 * k for k in range(7)], cores=cores)
    vals = ((C["s13.b"], "−75"), (C["s13.e"], "0"), (C["s13.c"], "−394"), (C["s13.d"], "−286"))
    for k, (tt, v) in enumerate(vals):
        E.foco(c, t, tt, 0.4, lambda a, k=k, v=v: (E.pilula(c, v, cs[k], 450, 46, "g", fundo=TINTA if v != "0" else CINZA, a=a)))
    E.foco(c, t, C["s13.b"] + 0.2, 0.4, lambda a: E.escreve(c, "formação (kJ)", XE - 20, 530, 40, "i", TINTA2, a))
    # a conta
    E.foco(c, t, C["s14.a"], 0.5, lambda a: (E.escreve(c, "produtos", XE, 640, 56, "i", TINTA2, a),
                                            E.formula(c, "−394 + 2 · (−286)", XE + 330, 645, 74, "g", TINTA, a)))
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "= −966", XE + 1050, 645, 74, "g", TINTA, a))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.escreve(c, "reagentes", XE, 770, 56, "i", TINTA2, a),
                                            E.formula(c, "−75 + 2 · 0 = −75", XE + 330, 775, 74, "g", TINTA, a)))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "−966 − (−75) = −966 + 75 =", XE + 330, 935, 74, "g", TINTA2, a))
    wv = E.formula(None, "−966 − (−75) = −966 + 75 =", 0, 0, 74, a=0)
    bola_txt(c, t, C["s14.f"], "−891", XE + 330 + wv + 120, 910, 96, 60, AZUL)
    E.foco(c, t, C["s14.f"] + 0.3, 0.4, lambda a: E.escreve(c, "kJ", XE + 330 + wv + 230, 935, 56, "g", TINTA, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s15.a"], ps("inverteu e", "i", 70) + [("esqueceu", "g", 64, ERRADO)] + ps("de trocar o sinal", "i", 70), XE, 330, passo=0.1)
    Q.formula_em(c, t, C["s15.a"] + 0.8, EQ2I, XE, 480, 80)
    E.foco(c, t, C["s15.a"] + 1.2, 0.4, lambda a: dh_txt(c, -283, 1500, 480, 72, a))
    if t >= C["s15.b"] - 0.2:
        E.risco(c, 1130, 500, 1500, 430, t, C["s15.b"] - 0.2, largura=9)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "−394 − 283 =", XE, 660, 90, "g", ERRADO, a))
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "−677 kJ", XE + 620, 660, 90, "g", ERRADO, a))
    E.frase(c, t, C["s15.d"], ps("queimar só até o", "i", 60) + [("CO", "g", 56)] + ps("soltaria mais que queimar até o", "i", 60) + [("CO₂", "g", 56)],
            XE, 820, passo=0.08)
    E.foco(c, t, C["s15.d"] + 1.8, 0.4, lambda a: (E.formula(c, "677 > 394", XE, 940, 80, "g", TINTA, a)))
    pilula_em(c, t, C["s15.e"], "não faz sentido", XE + 720, 915, 54, ERRADO)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s17"]:
        def s16():
            E.frase(c, t, C["s16"], ps("o atalho para montar", "i", 72, CLARO), W / 2, 160, "center", 0.12)
            itens = ((C["s16.a"], "1", "comece pelo que aparece numa equação só"), (C["s16.b"], "2", "lado errado? inverta"),
                     (C["s16.c"], "3", "coeficiente diferente? multiplique"), (C["s16.d"], "4", "o O₂ por último: ele se acerta sozinho"))
            for k, (tt, n, s) in enumerate(itens):
                y = 330 + k * 170
                E.foco(c, t, tt, 0.4, lambda a, y=y, n=n: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, n, XE + 40, y - 4, 54, "g", E.SOBRE, a)))
                E.foco(c, t, tt + 0.1, 0.5, lambda a, y=y, s=s: E.escreve(c, s, XE + 110, y, 66, "b", BR, a))
        E.saida(c, t, C["s17"] - 0.1, s16)
        return
    E.frase(c, t, C["s17.a"], ps("cada substância que aparece", "i", 70, CLARO) + [("uma vez só", "g", 66, BR)], W / 2, 330, "center", 0.12)
    E.frase(c, t, C["s17.a"] + 1.6, ps("decide sozinha o que fazer com a equação", "i", 66, CLARO), W / 2, 430, "center", 0.1)
    E.frase(c, t, C["s17.b"], ps("deu a tabela de formação?", "i", 70, BR), W / 2, 640, "center", 0.12)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "ΔH = produtos − reagentes", W / 2, 820, 100, "g", CLARO, a, "center"))


# ---------------- questão ----------------
QX = 300


def alvo_so3(c, x, y, size, a=1.0):
    eq_frac(c, [("q", "S"), ("t", "+"), ("f", "3", "2"), ("q", "O2 -> SO3")], x, y, size, a)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 150)
    E.foco(c, t, C["s18.a"], 0.4, lambda a: (Q.atomo(c, XE + 40, 230, 30, "S", a), E.escreve(c, "S = enxofre", XE + 90, 245, 44, "b", TINTA2, a)))
    q = ep(t, C["s18.a"] + 0.6, 0.5)
    if q > 0:
        E.caixa_pontilhada(c, QX - 30, 300, 900, 130, q, E.COR, prog_=q)
    E.foco(c, t, C["s18.a"] + 0.6, 0.5, lambda a: alvo_so3(c, QX, 390, 84, a))
    E.foco(c, t, C["s18.a"] + 1.0, 0.4, lambda a: E.escreve(c, "alvo: ΔH = ?", QX + 920, 385, 56, "b", COR, a))
    linha_eq(c, t, C["s18.b"], "S + O2 -> SO2", -297, QX, 580, 80, 1780)
    linha_eq(c, t, C["s18.c"], "2 SO3 -> 2 SO2 + O2", 198, QX, 720, 80, 1780)
    E.relogio(c, t, C["s19.a"], cx=W / 2, cy=860, r=70)


QR = 400


def b_resposta(c, t, C, b):
    q = 1.0
    E.caixa_pontilhada(c, QR - 30, 120, 900, 130, q, E.COR, prog_=q)
    alvo_so3(c, QR, 210, 84)
    linha_eq(c, t, C["s20"] - 0.6, "S + O2 -> SO2", -297, QR, 390, 80, 1780, cores={"S": E.COR} if t >= C["s20.a"] else None)
    pilula_em(c, t, C["s20.a"] + 0.4, "fica", 190, 365, 40, TINTA)
    if t < C["s20.c"]:
        linha_eq(c, t, C["s20"] - 0.6, "2 SO3 -> 2 SO2 + O2", 198, QR, 530, 80, 1780, cores={"SO3": E.COR} if t >= C["s20.b"] else None)
    else:
        E.foco(c, t, C["s20.c"], 0.5, lambda a: eq_frac(c, [("q", "SO2"), ("t", "+"), ("q", "½ O2 -> SO3")], QR, 530, 80, a))
        pilula_em(c, t, C["s20.c"] + 0.2, "invertida, × ½", 190, 505, 34, AMBAR)
        E.foco(c, t, C["s20.d"], 0.4, lambda a: (E.formula(c, "+198 → −198 → −99", 1780, 455, 46, "g", TINTA2, a, "right"), dh_txt(c, -99, 1780, 530, 72, a)))
    if t >= C["s21.a"]:
        q = ep(t, C["s21.a"], 0.4)
        M.line(c, QR, 600, 1780, 600, TINTA, q, 5)
        g1 = especie("S + O2 -> SO2", QR, 390, 80, 2)
        risca(c, t, C["s21.a"] + 0.2, g1)
        wso2 = Q.formula(None, "SO2", 0, 0, 80)
        risca(c, t, C["s21.a"] + 0.4, dict(x0=QR, x1=QR + wso2, topo=470, base=545))
    if t >= C["s21.b"]:
        E.frase(c, t, C["s21.b"], [("O₂:", "g", 52, TINTA2), ("1 + ½ =", "g", 52, TINTA2)], QR, 690, passo=0.15)
        E.foco(c, t, C["s21.b"] + 0.4, 0.4, lambda a: E.formula(c, "f{3}{2}", QR + 330, 690, 52, "g", COR, a))
        E.foco(c, t, C["s21.b"] + 0.8, 0.5, lambda a: alvo_so3(c, QR, 820, 84, a))
    E.formula_em(c, t, C["s21.c"], "−297 − 99 =", 1480, 980, 72, "g", TINTA2, "right")
    bola_txt(c, t, C["s21.d"], "−396", 1620, 955, 90, 60, AZUL)
    E.foco(c, t, C["s21.d"] + 0.3, 0.4, lambda a: E.escreve(c, "kJ", 1725, 980, 56, "g", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s22.a"], ps("o", "i", 74) + [("ΔH", "g", 70, COR)] + ps("não depende do caminho", "i", 74), W / 2, 340, "center", 0.12)
        for k, (tt, a1, a2) in enumerate(((C["s22.b"], "inverteu", "troca o sinal"), (C["s22.c"], "multiplicou", "multiplica"), (C["s22.d"], "somou", "soma"))):
            y = 520 + k * 150
            E.frase(c, t, tt, [(a1, "g", 76), ("→", "g", 76, TINTA2), (a2, "g", 76, COR)], W / 2, y, "center", 0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], [("energia", "g", 120, COR), ("de", "i", 120), ("ligação", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s23.b"], ps("quebrar gasta, formar libera", "i", 64, TINTA2), XE, 560, passo=0.1)
    Q.molecula(c, t, C["s23.b"] + 0.5, "H2", 450, 760, 120, separa=0.6 * ep(t, C["s23.b"] + 1.2, 1.0))
    Q.molecula(c, t, C["s23.b"] + 0.8, "Cl2", 850, 760, 120, separa=0.6 * ep(t, C["s23.b"] + 1.4, 1.0))
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, regras=b_regras, exemplo=b_exemplo, formacao=b_formacao,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
