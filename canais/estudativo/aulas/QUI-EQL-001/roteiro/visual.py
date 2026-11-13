"""Visual — Estudativo · QUI-EQL-001: equilíbrio químico e constante Kc. Primeira aula da trilha Equilíbrio Químico.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho da QUI-MIS-001; fórmula sempre com Q.formula).
LINGUAGEM VISUAL DA TRILHA "Equilíbrio Químico" (as aulas QUI-EQL-* copiam daqui):
- EQUAÇÃO DE EQUILÍBRIO com a seta dupla do kit ("<=>"), em turquesa. IDA = seta de cima, VOLTA = de baixo; quando a aula fala de
  uma delas, a pílula "ida" (tinta) ou "volta" (cinza) aparece em cima ou embaixo da seta.
- CONSTANTE em fração (kfrac): K grande com o índice pequeno (c, p, a, w, ps), "=" e a fração com produtos em cima e reagentes
  embaixo, cada concentração em Q.formula com o expoente na cor da matéria. Quem fica de fora (sólido, líquido puro) aparece na
  equação com risco cinza e nunca entra na fração.
- GRÁFICO DE VELOCIDADES × TEMPO: ida em tinta (desce), volta na cor da matéria (sobe); onde se encontram, linha tracejada e a
  pílula "equilíbrio". Equilíbrio = velocidades iguais, NUNCA concentrações iguais (as barras de concentração ficam diferentes).
- Estado físico (s) (l) (g) (aq) sempre escrito na equação quando decide quem entra na constante.
Peças candidatas ao kit (quimica.py): kfrac (expressão de K em fração), garrafa (refrigerante fechado), escada (escada rolante).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Equilíbrio Químico")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-EQL-001_equilibrio_quimico_kc.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("reversivel", "kc", "fora", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
MARROM = "#B5651D"

for eq in ("N2O4 -> 2 NO2", "N2 + 3 H2 -> 2 NH3", "CaCO3 -> CaO + CO2", "C + H2O -> CO + H2"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def _fq(c, s, x, y, size, cor, a=1.0, align="left", cores=None, escuro=False):
    """palavra comum sai em E.formula; espécie química, em Q.formula"""
    if s.replace(" ", "").isalpha() and s.islower():
        return E.formula(c, s, x, y, size, "g", cor, a, align)
    return Q.formula(c, s, x, y, size, cor, a, align, cores=cores, escuro=escuro)


def kfrac(c, t, t0, sub, num, den, x, y, size, tn=None, td=None, escuro=False, cor_exp=None):
    """K_sub = num / den. x = borda esquerda, y = linha da barra. num/den = textos Q.formula ("[NO2]^{2}"); den=None = sem fração"""
    tinta = BR if escuro else TINTA
    ce = cor_exp or (E.CLARO if escuro else E.COR)
    E.foco(c, t, t0, 0.4, lambda a: (E.escreve(c, "K", x, y + size * 0.36, size, "g", tinta, a),
                                     E.escreve(c, sub, x + E.larg("K", "g", size) + 4, y + size * 0.56, size * 0.55, "g", tinta, a),
                                     E.escreve(c, "=", x + E.larg("K", "g", size) + E.larg(sub, "g", size * 0.55) + size * 0.3, y + size * 0.36, size, "g", tinta, a)))
    x0 = x + E.larg("K", "g", size) + E.larg(sub, "g", size * 0.55) + size * 0.3 + E.larg("=", "g", size) + size * 0.35
    s_ = size * 0.85
    wn = _fq(None, num, 0, 0, s_, None, 0)
    if den is None:
        E.foco(c, t, tn if tn is not None else t0 + 0.3, 0.4, lambda a: _fq(c, num, x0, y + s_ * 0.36, s_, tinta, a, cores={"carga": ce}, escuro=escuro))
        return x0 + wn
    wd = _fq(None, den, 0, 0, s_, None, 0)
    w = max(wn, wd) + size * 0.3
    q = ep(t, tn if tn is not None else t0 + 0.3, 0.4)
    if q > 0:
        M.line(c, x0, y, x0 + w * ease_out(q), y, tinta, q, max(5, size * 0.07))
    E.foco(c, t, tn if tn is not None else t0 + 0.3, 0.4, lambda a: _fq(c, num, x0 + w / 2, y - size * 0.28, s_, tinta, a, "center", cores={"carga": ce}, escuro=escuro))
    E.foco(c, t, td if td is not None else t0 + 0.6, 0.4, lambda a: _fq(c, den, x0 + w / 2, y + size * 0.95, s_, tinta, a, "center", cores={"carga": ce}, escuro=escuro))
    return x0 + w


def garrafa(c, cx, yb, w, h, t, a=1.0):
    """garrafa fechada de refrigerante: bolhas subindo e voltando para o líquido"""
    if a <= 0:
        return
    pth = skia.Path()
    pth.moveTo(cx - w / 2, yb); pth.lineTo(cx - w / 2, yb - h * 0.6); pth.quadTo(cx - w / 2, yb - h * 0.78, cx - w * 0.18, yb - h * 0.86)
    pth.lineTo(cx - w * 0.18, yb - h); pth.lineTo(cx + w * 0.18, yb - h); pth.lineTo(cx + w * 0.18, yb - h * 0.86)
    pth.quadTo(cx + w / 2, yb - h * 0.78, cx + w / 2, yb - h * 0.6); pth.lineTo(cx + w / 2, yb); pth.close()
    c.save(); c.clipPath(pth, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeLTRB(cx - w, yb - h, cx + w, yb), M.paint("#EAF2F6", a))
    c.drawRect(skia.Rect.MakeLTRB(cx - w, yb - h * 0.62, cx + w, yb), M.paint("#5A3A22", a))
    for k in range(14):
        ph = (t * 0.45 + k * 0.29) % 1.0
        sobe = k % 2 == 0
        yy = lerp(yb - 20, yb - h * 0.75, ph if sobe else 1 - ph)
        xx = cx - w * 0.38 + (k * 37 % int(w * 0.76))
        c.drawCircle(xx, yy, 8, M.paint("#FFFFFF" if sobe else E.COR, 0.8 * a, stroke=3))
    c.restore()
    c.drawPath(pth, M.paint("#9DB3C2", a, stroke=6))
    M.rrect(c, cx - w * 0.22, yb - h - 30, w * 0.44, 40, 8, "#D62828", a)


def eixo_vel(c, t, t0, x, y, w, h):
    P = E.plano(c, t, t0, x, y, w, h, 0, 10, 0, 2.2, passo=10, passo_y=1, marcas_x=[], marcas_y=[], nomes=("", ""), size=40, grade=False)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.escreve(c, "velocidade", x + 20, y - 20, 46, "i", TINTA2, a), E.escreve(c, "tempo", x + w - 120, y + h - 18, 46, "i", TINTA2, a)))
    return P


V_IDA = lambda x: 0.7 + 1.3 * math.exp(-0.55 * x)
V_VOLTA = lambda x: 0.7 * (1 - math.exp(-0.55 * x))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: garrafa(c, 1450, 960, 340, 720, t, a))
        E.frase(c, t, C["s01.a"], ps("garrafa fechada:", "i", 70), XE, 260, passo=0.1)
        E.frase(c, t, C["s01.a"] + 0.8, ps("o gás", "i", 70) + [("sai", "g", 66, COR)] + ps("da bebida", "i", 70), XE, 380, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("e", "i", 70) + [("volta", "g", 66, COR)] + ps("para ela", "i", 70), XE, 490, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("a quantidade de gás", "i", 64, TINTA2) + [("não muda", "g", 60)], XE, 680, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("nada parou, e nada muda.", "i", 70) + [("como?", "g", 66, COR)], XE, 860, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1640, 640, 220 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"], [("equilíbrio", "g", 120, COR)], XE, 300)
    lista(c, t, [(C["s02.a"], [("por", "i", 74), ("que", "i", 74), ("é", "i", 74), ("dinâmico", "g", 70, COR)]),
                 (C["s02.b"], [("escrever", "i", 74), ("Kc", "g", 70), ("e", "i", 74), ("Kp", "g", 70)]),
                 (C["s02.c"], [("quem", "i", 74), ("fica", "i", 74), ("de", "i", 74), ("fora", "g", 70)])], XE, 500, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você vai usar", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: (Q.formula(c, "[NH3]", XE, 360, 90, TINTA, a), E.escreve(c, "concentração em mol/L", XE + 320, 350, 56, "i", TINTA2, a)))
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.formula(c, "v = f{Δ[ ]}{Δt}", XE, 540, 90, "g", TINTA, a), E.escreve(c, "velocidade média", XE + 420, 530, 56, "i", TINTA2, a)))
    E.foco(c, t, C["s03.c"], 0.5, lambda a: (Q.formula(c, "pO2", XE, 730, 90, TINTA, a), E.escreve(c, "pressão parcial: a parte de cada gás", XE + 320, 720, 56, "i", TINTA2, a)))
    E.foco(c, t, C["s03.d"], 0.5, lambda a: (E.formula(c, "2^3 = 8", XE, 900, 90, "g", TINTA, a), E.escreve(c, "potência", XE + 420, 890, 56, "i", TINTA2, a)))


# ---------------- reação reversível e equilíbrio dinâmico ----------------
EQN = "N2O4(g) <=> 2 NO2(g)"


def b_reversivel(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("reações que andam nos", "i", 70) + [("dois sentidos", "g", 66, COR)], XE, 220, passo=0.1)
            Q.formula_em(c, t, C["s04.b"], "A -> B", 620, 470, 120, align="center")
            E.foco(c, t, C["s04.c"], 0.4, lambda a: Q.formula(c, "B -> A", 1300, 470, 120, TINTA2, a, "center"))
            Q.formula_em(c, t, C["s04.d"], "A <=> B", W / 2, 720, 160, align="center")
            pilula_em(c, t, C["s04.e"], "ida →", W / 2, 590, 44, TINTA)
            pilula_em(c, t, C["s04.e"] + 0.6, "← volta", W / 2, 830, 44, CINZA)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    # s05-s07: N2O4 incolor → NO2 marrom; o gráfico das velocidades
    cor = M.mix("#F3EEE6", MARROM, 0.75 * ep(t, C["s05.b"], 5.0))
    Q.formula_em(c, t, C["s05"], EQN, 560, 220, 80, align="center")
    E.foco(c, t, C["s05"] + 0.4, 0.4, lambda a: (centro(c, "incolor", 330, 300, 42, "i", TINTA2, a), centro(c, "marrom", 820, 300, 42, "b", MARROM, a)))
    if t < C["s07"] + 1.0 or C["s07.d"] > t:
        E.saida(c, t, C["s07.d"] - 0.1, lambda: Q.erlenmeyer(c, t, C["s05"] + 0.2, 560, 900, 420, 460, nivel=0.85, cor=cor, graduacao=False))
    P = eixo_vel(c, t, C["s05.a"], 1080, 260, 700, 560)
    E.curva(c, t, C["s05.a"] + 0.2, P, V_IDA, 0, 10 if t >= C["s06.c"] else 3, d=1.6, cor=TINTA)
    if t >= C["s05.c"]:
        E.curva(c, t, C["s05.c"], P, V_VOLTA, 0, 10 if t >= C["s06.c"] else 3, d=1.6, cor=E.COR)
    E.foco(c, t, C["s05.a"] + 0.6, 0.4, lambda a: E.escreve(c, "ida", 1110, P.y(2.0) - 10, 44, "b", TINTA, a))
    E.foco(c, t, C["s05.c"] + 0.4, 0.4, lambda a: E.escreve(c, "volta", 1250, P.y(0.2) + 50, 44, "b", COR, a))
    if t >= C["s06.c"]:
        q = ep(t, C["s06.c"] + 1.0, 0.4)
        M.line(c, P.x(6.5), P.y(2.1), P.x(6.5), P.y(0), TINTA2, q, 3, dash=[10, 8])
        pilula_em(c, t, C["s06.d"], "equilíbrio", P.x(8.2), P.y(1.6), 44, E.COR)
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "a cor para de mudar", 1080, 960, 50, "i", TINTA, a))
    if t >= C["s07"]:
        def s07():
            M.rrect(c, 1060, 870, 760, 190, 24, "#FFFFFF", 1, shadow=True)
            E.escreve(c, "as reações não pararam", 1090, 930, 46, "g", TINTA, 1)
            E.escreve(c, "equilíbrio dinâmico", 1090, 1010, 54, "g", COR, 1)
        E.foco(c, t, C["s07.a"], 0.4, lambda a: s07())
        if t >= C["s07.d"]:
            # a escada rolante: a bolinha sobe enquanto a escada desce e fica no lugar
            q = ep(t, C["s07.d"], 0.5)
            M.line(c, 200, 960, 900, 560, TINTA2, q, 12)
            for k in range(5):
                f = ((t * 0.6 + k / 5) % 1)
                xx, yy = lerp(900, 200, f), lerp(560, 960, f)
                M.line(c, xx - 20, yy - 6, xx + 20, yy - 6, TINTA2, q * 0.8, 6)
            E.bola(c, 550, 720, 34 * q, E.COR)
            E.foco(c, t, C["s07.e"], 0.4, lambda a: E.escreve(c, "você sobe, a escada desce: fica no lugar", 200, 1030, 44, "b", TINTA, a))


# ---------------- Kc ----------------
def b_kc(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s08.a"], ps("no equilíbrio, uma conta sempre dá o mesmo número", "i", 60), XE, 190, passo=0.08)
        E.frase(c, t, C["s08.b"], [("constante de equilíbrio", "g", 76, COR)], XE, 310)
        kfrac(c, t, C["s08.b"] + 0.4, "c", "produtos", "reagentes", 560, 520, 110, tn=C["s08.c"], td=C["s08.d"])
        pilula_em(c, t, C["s08.e"], "cada concentração elevada ao seu coeficiente", 1380, 700, 40, TINTA)
        if t >= C["s09"]:
            Q.formula_em(c, t, C["s09.a"], EQN, XE, 860, 76, cores={"coef": E.COR})
            kfrac(c, t, C["s09.b"], "c", "[NO2]^{2}", "[N2O4]", 1100, 860, 90, tn=C["s09.b"], td=C["s09.c"])
            if t >= C["s09.d"]:
                pilula_em(c, t, C["s09.d"], "o 2 do coeficiente vira expoente", 1450, 1030, 40, E.COR)
        return
    Q.formula_em(c, t, C["s10.a"], "N2(g) + 3 H2(g) <=> 2 NH3(g)", W / 2, 240, 84, align="center", cores={"coef": E.COR})
    kfrac(c, t, C["s10.a"] + 0.8, "c", "[NH3]^{2}", "[N2] · [H2]^{3}", 560, 520, 120, tn=C["s10.b"], td=C["s10.c"])
    pilula_em(c, t, C["s10.d"], "Kc grande: muito produto", 600, 900, 50, E.COR)
    pilula_em(c, t, C["s10.e"], "Kc pequeno: pouco produto", 1320, 900, 50, TINTA)


# ---------------- quem fica de fora ----------------
EQC = "CaCO3(s) <=> CaO(s) + CO2(g)"


def b_fora(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("quem fica", "i", 80) + [("de fora?", "g", 76, COR)], XE, 230, passo=0.12)
        E.frase(c, t, C["s11.b"], [("sólidos", "g", 90), ("e", "i", 90), ("líquidos puros", "g", 90)], XE, 400, passo=0.14)
        for k, (s, x) in enumerate((("(s)", 300), ("(l)", 520))):
            pilula_em(c, t, C["s11.b"] + 0.4 + 0.3 * k, s, x, 520, 56, CINZA)
        E.frase(c, t, C["s11.c"], ps("a concentração deles não muda:", "i", 60, TINTA2), XE, 680, passo=0.1)
        E.frase(c, t, C["s11.c"] + 1.4, ps("carvão é carvão puro do começo ao fim", "i", 60, TINTA2), XE, 760, passo=0.1)
        E.frase(c, t, C["s11.d"], [("entram:", "i", 70), ("(g)", "g", 70, COR), ("e", "i", 70), ("(aq)", "g", 70, COR)], XE, 930, passo=0.14)
        return
    E.frase(c, t, C["s12.a"], ps("o calcário aquecido", "i", 64, TINTA2), XE, 180, passo=0.1)
    Q.formula_em(c, t, C["s12.a"] + 0.4, EQC, W / 2, 340, 96, align="center")
    if t >= C["s12.b"]:
        G = Q.grupos(EQC, W / 2, 340, 96, "center")
        sp = Q.centros(EQC, W / 2, 340, 96, "center")
        for k in (0, 1):
            wk = Q.formula(None, ("CaCO3(s)", "CaO(s)")[k], 0, 0, 96)
            E.risco(c, sp[k] - wk / 2, 360, sp[k] + wk / 2, 270, t, C["s12.b"] + 0.3 * k, cor=CINZA, largura=8)
    if t >= C["s12.c"]:
        kfrac(c, t, C["s12.c"], "c", "[CO2]", None, 640, 620, 130)
    if t >= C["s13"]:
        E.frase(c, t, C["s13.a"], [("Kp:", "g", 66, COR)] + ps("com as pressões parciais", "i", 66), XE, 820, passo=0.1)
        E.frase(c, t, C["s13.b"] + 1.0, ps("a parte da pressão total de cada gás", "i", 52, TINTA2), XE, 900, passo=0.08)
        E.frase(c, t, C["s13.d"], ps("mesma forma: produtos sobre reagentes", "b", 46, TINTA2), XE, 990, passo=0.08)
        kfrac(c, t, C["s13.e"], "p", "pCO2", None, 1200, 860, 110)


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("“no equilíbrio, as concentrações são iguais”", "i", 62, ERRADO), XE, 320, passo=0.08)
    if t >= C["s14.b"]:
        E.risco(c, XE - 10, 335, XE + 1200, 275, t, C["s14.b"], largura=9)
    E.frase(c, t, C["s14.b"], ps("o que fica igual são as", "i", 64) + [("velocidades", "g", 60, COR)], XE, 450, passo=0.1)
    for k, (nome, alt, cor) in enumerate((("N₂O₄", 330, TINTA), ("NO₂", 140, MARROM))):
        p = ease_out(prog(t, C["s14.c"] + 0.3 * k, 0.8))
        if p > 0:
            x = 560 + k * 300
            M.rrect(c, x, 960 - alt * p, 180, alt * p, 14, cor, 1)
            E.foco(c, t, C["s14.c"] + 0.3 * k, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x + 90, 1030, 50, "g", TINTA, a))
    E.foco(c, t, C["s14.c"], 0.4, lambda a: E.escreve(c, "concentrações no equilíbrio", 480, 580, 48, "b", TINTA2, a))
    E.frase(c, t, C["s14.d"], ps("constantes, mas", "i", 60) + [("diferentes", "g", 56, COR)], 1200, 820, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], ps("o atalho para escrever qualquer K", "i", 70, CLARO), W / 2, 160, "center", 0.1)
    for k, (tt, s) in enumerate(((C["s15.a"], "1  produtos sobre reagentes"), (C["s15.b"], "2  coeficiente vira expoente"), (C["s15.c"], "3  só entra (g) e (aq)"))):
        E.foco(c, t, tt, 0.5, lambda a, k=k, s=s: E.escreve(c, s, XE + 100, 320 + k * 130, 70, "g", BR if k != 2 else E.CLARO, a))
    E.frase(c, t, C["s15.d"], [("colchete:", "i", 60, CLARO), ("Kc", "g", 60, BR), ("·", "g", 60, CLARO), ("pressão:", "i", 60, CLARO), ("Kp,", "g", 60, BR)] +
            ps("só gás", "i", 60, CLARO), W / 2, 760, "center", 0.12)
    if t >= C["s16"]:
        E.frase(c, t, C["s16.a"], ps("cuidado com a água:", "i", 60, CLARO), XE, 920, passo=0.1)
        E.foco(c, t, C["s16.b"], 0.4, lambda a: Q.formula(c, "H2O(l): fora", 820, 920, 64, BR, a, escuro=True))
        E.foco(c, t, C["s16.c"], 0.4, lambda a: Q.formula(c, "H2O(g): entra", 1300, 920, 64, E.CLARO, a, escuro=True))


# ---------------- questão ----------------
EQQ = "C(s) + H2O(g) <=> CO(g) + H2(g)"


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s17.a"], ps("carvão em brasa e vapor de água", "i", 64, TINTA2), XE, 290, passo=0.1)
    Q.formula_em(c, t, C["s17.b"], EQQ, W / 2, 460, 96, align="center")
    E.frase(c, t, C["s17.c"], ps("escreva", "i", 72) + [("Kc", "g", 68, COR), ("e", "i", 72), ("Kp", "g", 68, COR)], XE, 660, passo=0.12)
    E.relogio(c, t, C["s18.a"], cx=1500, cy=760, r=110)


def b_resposta(c, t, C, b):
    Q.formula(c, EQQ, W / 2, 220, 90, align="center")
    sp = Q.centros(EQQ, W / 2, 220, 90, "center")
    if t >= C["s19.a"]:
        wk = Q.formula(None, "C(s)", 0, 0, 90)
        E.risco(c, sp[0] - wk / 2, 240, sp[0] + wk / 2, 150, t, C["s19.a"], cor=CINZA, largura=8)
        pilula_em(c, t, C["s19.a"] + 0.3, "sólido: fora", sp[0], 330, 40, CINZA)
    pilula_em(c, t, C["s19.b"], "vapor: entra", sp[1], 330, 40, E.COR)
    kfrac(c, t, C["s19.c"], "c", "[CO] · [H2]", "[H2O]", 420, 560, 110)
    kfrac(c, t, C["s19.d"], "p", "pCO · pH2", "pH2O", 420, 860, 110)
    pilula_em(c, t, C["s19.e"], "coeficientes 1: sem expoente", 1500, 1010, 44, TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s20.a"], ps("ida e volta com a", "i", 70) + [("mesma velocidade", "g", 66, COR)], W / 2, 360, "center", 0.12)
        kfrac(c, t, C["s20.b"], "", "produtos", "reagentes", 640, 600, 110)
        E.frase(c, t, C["s20.b"] + 1.2, ps("sem sólidos nem líquidos puros", "i", 60, TINTA2), W / 2, 900, "center", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("calcular", "g", 110, COR), ("o", "i", 110), ("Kc", "g", 110)], XE, 420)
    E.frase(c, t, C["s21.b"], ps("o quadro início, reage, equilíbrio", "i", 64, TINTA2), XE, 560, passo=0.1)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 820, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1020, 845, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 920)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, reversivel=b_reversivel, kc=b_kc, fora=b_fora, kp=b_fora, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
