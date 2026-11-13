"""Visual — Estudativo · QUI-INO-004: óxidos ácidos, básicos e neutros.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007). Classificação = três colunas com a
pílula da escala de pH: ÓXIDO ÁCIDO (ACIDO), BÁSICO (BASE), NEUTRO (NEUTRO). Óxido + água = os átomos se somam (soma_atomos)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-004_oxidos_acidos_basicos_neutros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('oxido', 'acido', 'neutro', 'atalho', 'questao', 'fim'))
BR = "#FFFFFF"
ACIDO, BASE, NEUTRO = "#E8602C", "#4B3FB5", TINTA2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns da trilha (as mesmas da QUI-INO-007; candidatas ao kit) ----------------
def clampf(v):
    return max(0.0, min(1.0, v))


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else BR, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, y=y, i=i: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def promessa(c, t, t0, itens, x=XE, y0=460, dy=170):
    """a promessa do gancho: 'até o fim da aula' + lista + hexágono da Química"""
    tb = t0 + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 540, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, t0, ps("até o fim da aula", "i", 88), x, 280, passo=0.14)
    lista(c, t, itens, x, y0, dy)


def lado(c, t, t0, x0, x1, y, rot, cor, sub=None, size=54):
    """chave embaixo de um trecho da equação, com o nome"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.chave(c, x0, x1, y, cor, p, 26)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, (x0 + x1) / 2, y + 90, size, "g", cor, a))
    if sub:
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: centro(c, sub, (x0 + x1) / 2, y + 150, 44, "i", TINTA2, a))


def selo_carga(c, cx, cy, r, carga, a=1.0):
    pos = "+" in carga
    E.bola(c, cx, cy, r, "#F2A516" if pos else Q.ELETRON, a)
    centro(c, carga.replace("-", "−"), cx, cy + r * 0.42, r * 1.15, "g", BR, a)


def ion(c, cx, cy, r, s, carga, a=1.0, escuro=False, cor=None):
    """íon: bolinha do elemento (ou esfera de grupo com a fórmula dentro) e a carga num selo no alto à direita"""
    if a <= 0 or r <= 0:
        return
    if s in Q.NOMES and cor is None:
        Q.atomo(c, cx, cy, r, s, a, escuro=escuro)
    else:
        E.bola(c, cx, cy, r, cor or "#6E6E76", a)
        sz = r * (0.95 if len(s) <= 2 else 0.75 if len(s) <= 3 else 0.6)
        Q.formula(c, s, cx, cy + sz * 0.36, sz, BR, a, "center")
    selo_carga(c, cx + r * 0.8, cy - r * 0.8, max(18, r * 0.38), carga, a)


def ion_em(c, t, t0, cx, cy, r, s, carga, cor=None, escuro=False):
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        ion(c, cx, cy, r * k, s, carga, min(1.0, prog(t, t0, 0.25)), escuro, cor)


def frasco_fechado(c, t, t0, cx, yb, w=220, h=260, particulas=None, cor=None):
    """erlenmeyer com rolha: o sistema fechado"""
    Q.erlenmeyer(c, t, t0, cx, yb, w, h, 0.0 if not cor else 0.3, cor or Q.AGUA, particulas=particulas)
    q = ep(t, t0 + 0.2, 0.4)
    if q > 0:
        M.rrect(c, cx - w * 0.16, yb - h - 34, w * 0.32, 52, 10, "#8B5E3C", q)


def caixa(c, t, t0, x, y, w, h, cor=None, t1=None):
    """caixa pontilhada que se desenha em volta de um trecho"""
    if t < t0 or (t1 is not None and t >= t1):
        return
    p = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)


def questao(c, t, C, sq, linhas, sp, desenho=None, titulo="hora de testar"):
    """tela da questão: texto à esquerda (linhas = [(instante, partes, y)]), desenho à direita até a pausa, e o relógio"""
    E.frase(c, t, C[sq], ps(titulo, "i", 72, COR), XE, 180)
    for ti, partes, y in linhas:
        E.frase(c, t, ti, partes, XE, y, passo=0.08)
    if t < C[sp]:
        if desenho:
            desenho()
    else:
        E.relogio(c, t, C[sp + ".a"], cx=1500, cy=470, r=200)


def fim(c, t, C, sr, itens, sp, l1, l2, k_insc, k_bons, desenho=None, dy=180):
    """fechamento: resumo numerado, depois a próxima aula, inscreva-se e bons estudos"""
    def resumo():
        E.frase(c, t, C[sr], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * dy
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C[sp] - 0.1, resumo)
    if t < C[sp]:
        return
    E.frase(c, t, C[sp], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[sp] + 0.6, [(l1, "g", 110, COR)], XE, 400)
    if l2:
        E.frase(c, t, C[sp] + 1.0, [(l2, "g", 110, COR)], XE, 530)
    if desenho:
        desenho()
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


def palco_titulo(c, t, t0, txt):
    E.frase(c, t, t0, ps(txt, "i", 72, CLARO), W / 2, 150, "center", 0.12)


# ======================== desta aula ========================
for eq in ("SO3 + H2O -> H2SO4", "CO2 + H2O -> H2CO3", "CaO + H2O -> Ca(OH)2", "Na2O + H2O -> 2 NaOH", "SO2 + H2O -> H2SO3"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq


def bolhas(c, t, cx, yb, w, h, n=10, a=1.0, r=11):
    for k in range(n):
        f = (t * 0.5 + k / n) % 1
        x = cx - w * 0.32 + (k * 37 % 100) / 100 * w * 0.64 + 6 * math.sin(t * 3 + k)
        c.drawCircle(x, yb - 20 - f * h, r * (0.6 + 0.5 * f), M.paint(TINTA2, a * 0.8 * (1 - f * 0.6), stroke=3))


def classe(c, t, t0, cx, y, rot, cor, itens, size=96):
    """coluna de classificação: pílula + fórmulas embaixo"""
    pilula_em(c, t, t0, rot, cx, y, 52, cor)
    for i, (ti, f) in enumerate(itens):
        Q.formula_em(c, t, ti, f, cx, y + 160 + i * 130, size, align="center")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a água com gás é", "i", 84) + [("ácida", "g", 80, ACIDO)], XE, 260, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("ninguém colocou ácido", "i", 72, TINTA2), XE, 390, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("só", "i", 80) + [("gás carbônico", "g", 76, COR)], XE, 560, passo=0.14)
        Q.formula_em(c, t, C["s01.c"] + 0.8, "CO2 + H2O -> H2CO3", XE, 780, 100)
        E.frase(c, t, C["s01.d"], ps("um gás virou ácido", "i", 70), XE, 940, passo=0.12)
        Q.bequer(c, t, C["s01.a"], 1480, 900, 340, 440, 0.75, Q.AGUA)
        if t >= C["s01.c"]:
            bolhas(c, t, 1480, 900, 340, 300, a=ep(t, C["s01.c"], 0.4))
            for k in range(3):
                Q.molecula(c, t, C["s01.c"] + 0.2 * k, "CO2", 1400 + 80 * k, 600 + 60 * (k % 2), 40, passo=0.05, rotulos=False)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("reconhecer", "g", 70), ("um", "i", 74), ("óxido", "g", 70, COR)]),
                              (C["s02.b"], [("ácido,", "g", 70, ACIDO), ("básico", "g", 70, BASE), ("ou", "i", 74), ("neutro", "g", 70)]),
                              (C["s02.c"], [("o", "i", 74), ("que", "i", 74), ("forma", "g", 70), ("com", "i", 74), ("a", "i", 74), ("água", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 80, TINTA2), XE, 180)
    E.frase(c, t, C["s03.a"], [("ácido", "g", 70, ACIDO)] + ps("solta", "i", 66) + [("H⁺;", "g", 62)] + ps("fórmula com", "i", 66), XE, 320, passo=0.1)
    Q.formula_em(c, t, C["s03.a"] + 1.0, "H2SO4", XE + 830, 322, 70, cores={0: E.COR})
    E.frase(c, t, C["s03.b"], [("base", "g", 70, BASE)] + ps("solta", "i", 66) + [("OH⁻;", "g", 62)] + ps("fórmula termina em", "i", 66), XE, 440, passo=0.1)
    Q.formula_em(c, t, C["s03.b"] + 1.0, "NaOH", XE + 1000, 442, 70)
    P = Q.tabela(c, t, C["s03.c"] - 0.4, 560, 560, 44, numeros=False, d=1.0)
    amet = ("C", "N", "O", "F", "P", "S", "Cl", "Se", "Br", "I")
    fora = amet + ("H", "He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og", "B", "Si", "Ge", "As", "Sb", "Te", "Po", "At", "Ts")
    met = [s_ for s_ in Q._SIMBOLOS if s_ not in fora and Q._posicoes()[s_][2] is not None]
    for grupo, k, cor in ((met, "s03.c", BASE), (amet, "s03.d", ACIDO)):
        q = ep(t, C[k], 0.5)
        if q > 0:
            for s in grupo:
                x, y = P(s)
                M.rrect(c, x - 21, y - 21, 42, 42, 6, cor, 0.5 * q)
    E.foco(c, t, C["s03.c"] + 0.3, 0.4, lambda a: E.escreve(c, "metais", 560, 1000, 56, "g", BASE, a))
    E.foco(c, t, C["s03.d"] + 0.3, 0.4, lambda a: E.escreve(c, "ametais", 1150, 540, 56, "g", ACIDO, a))


# ---------------- óxido ----------------
def b_oxido(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("óxido", "g", 110, COR)] + [("=", "g", 76, TINTA2)] + ps("dois elementos só,", "i", 80), XE, 300, passo=0.14)
        E.frase(c, t, C["s04.b"], ps("e um deles é o", "i", 80) + [("oxigênio", "g", 76, ERRADO if False else TINTA)], XE, 420, passo=0.14)
        for i, k in enumerate(("s04.c", "s04.d", "s04.e", "s04.f")):
            f = ("CO2", "SO3", "CaO", "CO")[i]
            x = XE + 60 + i * 420
            Q.formula_em(c, t, C[k], f, x, 680, 130, cores={"O": E.COR})
            mol = {"CO2": "CO2", "CO": "CO"}.get(f)
            if mol:
                Q.molecula(c, t, C[k] + 0.2, mol, x + 110, 860, 70, passo=0.1)
            elif f == "SO3":
                Q.molecula(c, t, C[k] + 0.2, dict(atomos=[("S", 0, 0), ("O", 1.2, 0), ("O", -0.6, 1.0), ("O", -0.6, -1.0)], ligacoes=[(0, 1, 2), (0, 2, 2), (0, 3, 2)]), x + 110, 860, 60, passo=0.1)
            else:
                Q.atomo_em(c, t, C[k] + 0.2, x + 70, 860, 50, "Ca"), Q.atomo_em(c, t, C[k] + 0.3, x + 170, 860, 44, "O")
        return
    E.frase(c, t, C["s05"], ps("o nome conta os oxigênios", "i", 72, TINTA2), XE, 180, passo=0.12)
    E.frase(c, t, C["s05.a"], [("mono", "g", 66, COR), ("= 1,", "g", 66), ("di", "g", 66, COR), ("= 2,", "g", 66), ("tri", "g", 66, COR), ("= 3", "g", 66)], XE, 300, passo=0.15)
    for i, (k, f, a_, b_) in enumerate((("s05.b", "CO2", "di", "óxido de carbono (gás carbônico)"), ("s05.c", "SO3", "tri", "óxido de enxofre"),
                                        ("s05.d", "CO", "mon", "óxido de carbono"))):
        y = 450 + i * 130
        Q.formula_em(c, t, C[k], f, XE, y, 96)
        E.foco(c, t, C[k] + 0.3, 0.45, lambda a, a_=a_, b_=b_, y=y: (E.escreve(c, a_, XE + 300, y, 66, "g", COR, a),
                                                                  E.escreve(c, b_, XE + 300 + E.larg(a_, "g", 66), y, 66, "i", TINTA, a)))
    Q.formula_em(c, t, C["s05.e"], "CaO", XE, 900, 96)
    E.frase(c, t, C["s05.e"] + 0.5, ps("com metal: óxido de cálcio,", "i", 62) + [("a cal viva", "g", 58, COR)], XE + 300, 895, passo=0.1)


# ---------------- óxido ácido ----------------
def b_acido(c, t, C, b):
    E.frase(c, t, C["s06"], ps("ponha na água e veja o que se forma", "i", 66, TINTA2), XE, 180, passo=0.1)
    E.frase(c, t, C["s06.a"], ps("óxido de", "i", 76) + [("ametal", "g", 72, ACIDO), ("→", "g", 72, TINTA2), ("ácido", "g", 72, ACIDO)], XE, 320, passo=0.14)
    pilula_em(c, t, C["s06.b"], "óxido ácido", 1500, 300, 56, ACIDO)
    if t >= C["s07"]:
        cs = Q.equacao(c, t, C["s07.a"], "SO3 + H2O -> H2SO4", W / 2, 560, 140, tl=[C["s07.a"], C["s07.b"] - 0.1, C["s07.b"], C["s07.c"] - 0.2, C["s07.c"]])
        E.foco(c, t, C["s07.d"], 0.4, lambda a: centro(c, "ácido sulfúrico", cs[2], 680, 56, "g", ACIDO, a))
        if t < C["s08"]:
            pilula_em(c, t, C["s07.e"], "a chuva ácida: outra aula", W / 2, 860, 46, TINTA2)
    if t >= C["s08"]:
        Q.formula_em(c, t, C["s08.a"], "CO2 + H2O -> H2CO3", W / 2, 880, 110, align="center")
        E.foco(c, t, C["s08.b"], 0.4, lambda a: centro(c, "o ácido da água com gás", W / 2, 990, 54, "i", TINTA2, a))


# ---------------- óxido básico ----------------
def b_basico(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("óxido de", "i", 76) + [("metal", "g", 72, BASE), ("→", "g", 72, TINTA2), ("base", "g", 72, BASE)], XE, 230, passo=0.14)
    pilula_em(c, t, C["s09.b"], "óxido básico", 1500, 210, 56, BASE)
    cs = Q.equacao(c, t, C["s09.c"], "CaO + H2O -> Ca(OH)2", W / 2, 460, 130, tl=[C["s09.c"], C["s09.c"] + 0.4, C["s09.c"] + 0.7, C["s09.d"] - 0.2, C["s09.d"]])
    E.foco(c, t, C["s09.e"], 0.4, lambda a: (centro(c, "cal viva", cs[0], 570, 50, "i", TINTA2, a), centro(c, "cal hidratada", cs[2], 570, 50, "i", TINTA2, a)))
    if t >= C["s10"]:
        cs2 = Q.equacao(c, t, C["s10.a"], "Na2O + H2O -> 2 NaOH", W / 2, 780, 120, tl=[C["s10.a"], C["s10.a"] + 0.4, C["s10.a"] + 0.7, C["s10.b"] - 0.2, C["s10.b"]],
                        cores={"coef": E.COR})
        E.foco(c, t, C["s10.b"] + 0.4, 0.4, lambda a: centro(c, "soda cáustica", cs2[2], 880, 50, "i", TINTA2, a))
        pilula_em(c, t, C["s10.c"], "metal no óxido, base na água (com poucas exceções)", W / 2, 1000, 42, BASE)


# ---------------- neutro ----------------
def b_neutro(c, t, C, b):
    E.frase(c, t, C["s11.a"], ps("alguns óxidos de ametal", "i", 76) + [("não reagem", "g", 72)], XE, 230, passo=0.12)
    E.frase(c, t, C["s11.b"], ps("com a água: nem ácido, nem base", "i", 66, TINTA2), XE, 340, passo=0.1)
    pilula_em(c, t, C["s11.c"], "óxidos neutros", W / 2, 500, 60, NEUTRO)
    E.foco(c, t, C["s11.c"] + 0.6, 0.4, lambda a: E.escreve(c, "decore três:", XE, 700, 60, "i", TINTA2, a))
    for i, k in enumerate(("s11.d", "s11.e", "s11.f")):
        Q.formula_em(c, t, C[k], ("CO", "NO", "N2O")[i], 640 + i * 420, 760, 160, align="center")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("CO é ácido?", "i", 74), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s12.b"], "CO2", 560, 480, 170, align="center")
    Q.molecula(c, t, C["s12.b"] + 0.2, "CO2", 560, 620, 80, passo=0.1)
    pilula_em(c, t, C["s12.b"] + 0.5, "ácido", 560, 760, 56, ACIDO)
    Q.formula_em(c, t, C["s12.c"], "CO", 1360, 480, 170, align="center")
    Q.molecula(c, t, C["s12.c"] + 0.2, "CO", 1360, 620, 80, passo=0.1)
    pilula_em(c, t, C["s12.d"], "neutro", 1360, 760, 56, NEUTRO)
    E.frase(c, t, C["s12.e"], ps("neutro, mas", "i", 64) + [("muito tóxico", "g", 60, ERRADO)], W / 2, 940, "center", 0.12)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        palco_titulo(c, t, C["s13"], "o atalho de prova")
        E.frase(c, t, C["s13.a"], ps("junte os átomos do óxido com os da água,", "i", 62, CLARO), W / 2, 270, "center", 0.1)
        E.frase(c, t, C["s13.b"], ps("e ponha os", "i", 62, CLARO) + [("H", "g", 60, BR)] + ps("na frente", "i", 62, CLARO), W / 2, 360, "center", 0.12)
        Q.equacao(c, t, C["s13.c"], "SO3 + H2O", W / 2, 560, 140, passo=0.3, escuro=True)
        E.formula_em(c, t, C["s13.d"], "H: 2   S: 1   O: 3 + 1 = 4", W / 2, 720, 70, "g", CLARO, "center")
        Q.formula_em(c, t, C["s13.e"], "H2SO4", W / 2, 920, 170, align="center", escuro=True, cores={"indice": E.CLARO})
        return
    palco_titulo(c, t, C["s14"], "funciona porque")
    E.frase(c, t, C["s14.a"], ps("a água entra inteira:", "i", 66, CLARO) + [("nenhum átomo some", "g", 62, BR)], W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s14.b"], ps("no óxido básico, o", "i", 66, CLARO) + [("OH", "g", 62, BR)] + ps("vai para o fim:", "i", 66, CLARO), W / 2, 460, "center", 0.12)
    Q.formula_em(c, t, C["s14.c"], "CaO + H2O -> Ca(OH)2", W / 2, 620, 110, align="center", escuro=True)
    E.frase(c, t, C["s14.d"], [("não", "g", 62, ERRADO), ("compensa", "i", 66, CLARO)] + ps("com os neutros: eles não reagem", "i", 66, CLARO), W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        for i, (k, f) in enumerate((("s15.a", "K2O"), ("s15.b", "SO2"), ("s15.c", "NO"))):
            Q.formula_em(c, t, C[k], f, 1500, 330 + i * 190, 140, align="center")
    questao(c, t, C, "s15", [(C["s15"] + 0.6, ps("ácido, básico ou neutro?", "i", 64), 330),
                             (C["s15.a"], [("1", "g", 56, COR), ("K₂O", "g", 60)], 460),
                             (C["s15.b"], [("2", "g", 56, COR), ("SO₂", "g", 60)], 570),
                             (C["s15.c"], [("3", "g", 56, COR), ("NO", "g", 60)], 680),
                             (C["s15.d"], [("4", "g", 56, COR)] + ps("o ácido do", "i", 60) + [("SO₂", "g", 56)] + ps("com a água", "i", 60), 820)], "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs = (420, 960, 1500)
    for i, (k, f, rot, cor, sub) in enumerate((("s17.a", "K2O", "básico", BASE, "potássio: metal"), ("s17.b", "SO2", "ácido", ACIDO, "enxofre: ametal"),
                                                ("s17.c", "NO", "neutro", NEUTRO, "um dos três"))):
        Q.formula_em(c, t, C[k], f, xs[i], 300, 130, align="center")
        pilula_em(c, t, C[k] + 0.4, rot, xs[i], 400, 52, cor)
        E.foco(c, t, C[k] + 0.6, 0.4, lambda a, i=i, sub=sub: centro(c, sub, xs[i], 500, 46, "i", TINTA2, a))
    if t >= C["s18"]:
        Q.equacao(c, t, C["s18.a"], "SO2 + H2O -> H2SO3", W / 2, 720, 120, passo=0.3)
        E.formula_em(c, t, C["s18.b"], "H: 2   S: 1   O: 2 + 1 = 3", W / 2, 850, 64, "g", TINTA2, "center")
        pilula_em(c, t, C["s18.e"], "H₂SO₃", W / 2, 970, 72, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        def escala(a):
            for k in range(15):
                M.rrect(c, XE + k * 64, 760, 60, 60, 8, Q.cor_ph(k), a)
                centro(c, str(k), XE + k * 64 + 30, 800, 30, "g", BR, a)
        E.foco(c, t, C["s20.a"], 0.5, escala)
    fim(c, t, C, "s19", [("s19.a", [("ametal", "g", 66, ACIDO), ("→", "g", 66, TINTA2), ("óxido", "i", 72), ("ácido", "g", 66, ACIDO)]),
                         ("s19.b", [("metal", "g", 66, BASE), ("→", "g", 66, TINTA2), ("óxido", "i", 72), ("básico", "g", 66, BASE)]),
                         ("s19.c", [("CO,", "g", 66), ("NO,", "g", 66), ("N₂O:", "g", 66), ("neutros", "g", 66, COR)])],
        "s20", "Escala de pH", "e indicadores", "s20.c", "s20.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, oxido=b_oxido, acido=b_acido, basico=b_basico, neutro=b_neutro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
