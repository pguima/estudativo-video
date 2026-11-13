"""Visual — Estudativo · QUI-INO-003: neutralização e sais.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007). H⁺ e OH⁻ que se encontram viram a
molécula de água (encontro); íons que sobram ficam soltos e formam o sal. Cruzar cargas = seta curva da carga de um íon para o
índice do outro (cruza)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-003_neutralizacao_e_sais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('neutraliza', 'sal', 'nomes', 'atalho', 'questao', 'fim'))
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
OHC = "#B3343A"
SO4 = "#C9A227"
for eq in ("HCl + NaOH -> NaCl + H2O", "H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O", "Mg(OH)2 + 2 HCl -> MgCl2 + 2 H2O"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert 2 * 3 == 6 and 3 * 2 == 6 and 1 - 2 == -1


def encontro(c, t, t0, cx, cy, p, r=40):
    """um H⁺ e um OH⁻ se aproximam (p = 0..1) e viram H₂O"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    if p < 0.85:
        ion(c, lerp(cx - 260, cx - 40, ease_io(p)), cy, r * 0.75, "H", "+", q)
        ion(c, lerp(cx + 260, cx + 40, ease_io(p)), cy, r, "OH", "-", q, cor=OHC)
    else:
        Q.molecula(c, t, t0 + 0.0, "H2O", cx, cy, r * 2.2, passo=0, a=q * ep(t, 0, 0) if False else q)


def cruza(c, t, t0, x0, y0, x1, y1, p=None):
    """seta curva: a carga de um íon vira o índice do outro"""
    p = ease_io(prog(t, t0, 0.6)) if p is None else p
    if p <= 0:
        return
    pth = skia.Path()
    pth.moveTo(x0, y0)
    pth.quadTo((x0 + x1) / 2 + (60 if x1 > x0 else -60), (y0 + y1) / 2, x1, y1)
    m = skia.PathMeasure(pth, False)
    seg = skia.Path()
    m.getSegment(0, m.getLength() * p, seg, True)
    c.drawPath(seg, M.paint(E.COR, 1, stroke=6))
    if p > 0.95:
        pos, tan = m.getPosTan(m.getLength())
        M.arrow(c, pos.x() - tan.x() * 30, pos.y() - tan.y() * 30, pos.x(), pos.y(), E.COR, 1, 6, 22)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("ácido", "g", 90, ACIDO)] + ps("que corrói", "i", 84), XE, 260, passo=0.14)
        E.frase(c, t, C["s01.b"], [("+", "g", 90, TINTA2), ("base", "g", 90, BASE)] + ps("que corrói", "i", 84), XE, 400, passo=0.14)
        E.frase(c, t, C["s01.b"] + 1.6, ps("na medida certa", "i", 60, TINTA2), XE, 480, passo=0.1)
        E.frase(c, t, C["s01.c"], [("=", "g", 90, TINTA2), ("água", "g", 90, COR), ("e", "i", 84), ("sal", "g", 90, COR)], XE, 680, passo=0.14)
        E.frase(c, t, C["s01.d"], ps("onde foi parar o perigo?", "i", 74), XE, 880, passo=0.12)
        Q.bequer(c, t, C["s01.a"], 1450, 920, 380, 420, 0.7, lambda tt: Q.muda_cor(tt, C["s01.c"], "#F6C9B8", Q.AGUA, 1.2),
                 particulas=dict(n=24, estado="liquido", tipos=[("Na", 0.5), ("Cl", 0.5)], r=12))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("ácido", "g", 70), ("+", "g", 70, TINTA2), ("base", "g", 70)]),
                              (C["s02.b"], [("a", "i", 74), ("fórmula", "g", 70, COR), ("do", "i", 74), ("sal", "g", 70)]),
                              (C["s02.c"], [("o", "i", 74), ("nome", "g", 70, COR), ("do", "i", 74), ("sal", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre das duas aulas anteriores", "i", 76, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("ácido", "g", 80, ACIDO)] + ps("solta", "i", 80), XE, 400, passo=0.14)
    ion_em(c, t, C["s03.a"] + 0.6, XE + 560, 375, 50, "H", "+")
    E.frase(c, t, C["s03.b"], [("base", "g", 80, BASE)] + ps("solta", "i", 80), XE, 560, passo=0.14)
    ion_em(c, t, C["s03.b"] + 0.6, XE + 560, 535, 56, "OH", "-", cor=OHC)
    Q.equacao(c, t, C["s03.c"], "HCl -> H^+ + Cl^-", XE, 820, 110, align="left", passo=0.3)
    E.foco(c, t, C["s03.c"] + 1.4, 0.4, lambda a: E.escreve(c, "o cloreto", XE + 900, 830, 60, "i", TINTA2, a))


# ---------------- neutralização ----------------
def b_neutraliza(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("junte ácido e base", "i", 80, TINTA2), XE, 200, passo=0.12)
        p = prog(t, C["s04.a"], C["s04.c"] - C["s04.a"] + 0.2)
        encontro(c, t, C["s04.a"], W / 2, 500, p, 60)
        Q.equacao(c, t, C["s04.c"], "H^+ + OH^- -> H2O", W / 2, 800, 130, passo=0.2)
        E.frase(c, t, C["s04.d"], [("+1", "g", 60, "#E09A10"), ("e", "i", 64), ("−1", "g", 60, Q.ELETRON)] + ps("se cancelam", "i", 64), W / 2, 960, "center", 0.12)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("neutralização", "g", 130, COR)], XE, 380)
        E.frase(c, t, C["s05.b"], ps("na medida certa, ácido e base deixam de agir", "i", 64), XE, 560, passo=0.1)
        E.foco(c, t, C["s05.c"], 0.4, lambda a: (E.pilula(c, "ácida", 520, 760, 56, "g", fundo=ACIDO, a=a * 0.35),
                                                E.pilula(c, "neutra", 900, 760, 64, "g", fundo=NEUTRO, a=a),
                                                E.pilula(c, "básica", 1280, 760, 56, "g", fundo=BASE, a=a * 0.35)))
        return
    eq = "HCl + NaOH -> NaCl + H2O"
    cs = Q.equacao(c, t, C["s06.a"], eq, W / 2, 330, 112, tl=[C["s06.a"], C["s06.b"] - 0.1, C["s06.b"], C["s06.c"] - 0.2, C["s06.c"], C["s06.d"] - 0.1, C["s06.d"]])
    if t >= C["s06.e"]:
        G = Q.grupos(eq, W / 2, 330, 112, "center")
        hs = [g for g in G if g["s"] == "H"]
        io = [k for k, g in enumerate(G) if g["s"] == "O"][0]
        caixa(c, t, C["s06.e"], hs[0]["x0"] - 8, hs[0]["topo"] - 8, hs[0]["x1"] - hs[0]["x0"] + 16, hs[0]["base"] - hs[0]["topo"] + 16, E.COR)
        caixa(c, t, C["s06.e"], G[io]["x0"] - 8, G[io]["topo"] - 8, G[io + 1]["x1"] - G[io]["x0"] + 16, G[io]["base"] - G[io]["topo"] + 16, E.COR)
        lado(c, t, C["s06.e"] + 0.4, cs[3] - 120, cs[3] + 120, 400, "água", COR)
    if t >= C["s07"]:
        lado(c, t, C["s07.a"], cs[2] - 150, cs[2] + 150, 400, "sal", COR)
        ion_em(c, t, C["s07.a"] + 0.2, 760, 700, 62, "Na", "+")
        E.foco(c, t, C["s07.a"] + 0.4, 0.4, lambda a: centro(c, "veio da base", 760, 810, 48, "i", TINTA2, a))
        ion_em(c, t, C["s07.b"], 1160, 700, 70, "Cl", "-")
        E.foco(c, t, C["s07.b"] + 0.2, 0.4, lambda a: centro(c, "veio do ácido", 1160, 810, 48, "i", TINTA2, a))
        pilula_em(c, t, C["s07.c"], "NaCl: cloreto de sódio, o sal de cozinha", W / 2, 950, 48, E.COR)


# ---------------- sal ----------------
def b_sal(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("ácido", "g", 84, ACIDO), ("+", "g", 84, TINTA2), ("base", "g", 84, BASE), ("→", "g", 84, COR),
                                    ("sal", "g", 84, COR), ("+", "g", 84, TINTA2), ("água", "g", 84)], W / 2, 330, "center", 0.15)
        E.frase(c, t, C["s08.b"], ps("sal: o", "i", 64) + [("íon positivo", "g", 60)] + ps("vem da base", "i", 64), W / 2, 560, "center", 0.1)
        E.frase(c, t, C["s08.c"], ps("e o", "i", 64) + [("íon negativo", "g", 60)] + ps("vem do ácido", "i", 64), W / 2, 670, "center", 0.1)
        ion_em(c, t, C["s08.b"] + 0.6, 800, 870, 56, "Na", "+")
        ion_em(c, t, C["s08.c"] + 0.6, 1120, 870, 62, "Cl", "-")
        return
    if t < C["s10"]:
        Q.equacao(c, t, C["s09.a"], "H2SO4 -> 2 H^+ + SO4^2-", W / 2, 260, 110, passo=0.3, cores={"carga": E.COR} if t >= C["s09.b"] else None)
        E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: centro(c, "sulfato: duas cargas negativas", W / 2, 370, 48, "i", TINTA2, a))
        ion_em(c, t, C["s09.b"] + 0.3, 1180, 620, 84, "SO4", "2-", cor=SO4)
        ion_em(c, t, C["s09.c"], 640, 620, 56, "Na", "+")
        if t >= C["s09.d"]:
            ion_em(c, t, C["s09.d"], 900, 620, 56, "Na", "+")
            E.formula_em(c, t, C["s09.d"] + 0.5, "+1 +1 −2 = 0", 900, 820, 70, "g", TINTA2, "center")
        Q.formula_em(c, t, C["s09.e"], "Na2SO4", W / 2, 990, 120, align="center", cores={"indice": E.COR})
        return
    eq = "H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O"
    Q.equacao(c, t, C["s10"], eq, W / 2, 380, 88, tl=[C["s10"], C["s10.b"] - 0.1, C["s10.b"], C["s10.c"] - 0.4, C["s10.c"] - 0.2, C["s10.c"] - 0.1, C["s10.c"]],
              cores={"coef": E.COR})
    E.frase(c, t, C["s10.a"], [("2 H⁺", "g", 70, ACIDO)] + ps("pedem", "i", 70) + [("2 OH⁻", "g", 70, BASE)], W / 2, 220, "center", 0.14)
    for k in range(2):
        encontro(c, t, C["s10.c"] + 0.3 * k, 760 + 420 * k, 640, prog(t, C["s10.c"] + 0.3 * k, 1.4), 44)
    E.frase(c, t, C["s10.d"], ps("cada", "i", 66) + [("H⁺", "g", 62, COR)] + ps("faz uma água", "i", 66), W / 2, 920, "center", 0.12)


# ---------------- nomes ----------------
def b_nomes(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("o nome do sal vem do ácido", "i", 76, TINTA2), XE, 200, passo=0.12)
        linhas = (("s11.a", "clorídrico", "ídrico", "cloreto", "eto"), ("s11.c", "sulfúrico", "ico", "sulfato", "ato"),
                  ("s11.d", "nítrico", "ico", "nitrato", "ato"), ("s11.e", "carbônico", "ico", "carbonato", "ato"))
        for i, (k, a_, ta, b_, tb) in enumerate(linhas):
            y = 360 + i * 150
            E.foco(c, t, C[k], 0.45, lambda a, a_=a_, ta=ta, y=y: (E.escreve(c, a_[:-len(ta)], XE + 40, y, 74, "g", TINTA, a),
                                                                E.escreve(c, ta, XE + 40 + E.larg(a_[:-len(ta)], "g", 74), y, 74, "g", ACIDO, a)))
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, y=y: M.arrow(c, XE + 560, y - 24, XE + 700, y - 24, COR, a, 6, 20))
            E.foco(c, t, C[k] + 0.5, 0.45, lambda a, b_=b_, tb=tb, y=y: (E.escreve(c, b_[:-len(tb)], XE + 760, y, 74, "g", TINTA, a),
                                                                      E.escreve(c, tb, XE + 760 + E.larg(b_[:-len(tb)], "g", 74), y, 74, "g", COR, a)))
        pilula_em(c, t, C["s11.a"] + 0.8, "ídrico → eto", 1560, 340, 50, ACIDO)
        pilula_em(c, t, C["s11.b"] + 0.4, "ico → ato", 1560, 490, 50, ACIDO)
        return
    E.frase(c, t, C["s12.a"], ps("nome do íon negativo +", "i", 70) + [("de", "g", 66, COR)] + ps("+ metal", "i", 70), XE, 200, passo=0.12)
    for i, (k, f, nome) in enumerate((("s12.b", "Na2SO4", "sulfato de sódio"), ("s12.c", "KNO3", "nitrato de potássio"), ("s12.d", "CaCO3", "carbonato de cálcio"))):
        y = 400 + i * 170
        Q.formula_em(c, t, C[k], f, XE, y, 110)
        E.frase(c, t, C[k] + 0.3, ps(nome, "i", 72), XE + 480, y - 5, passo=0.1)
    pilula_em(c, t, C["s12.d"] + 1.2, "calcário, mármore, casca de ovo", W / 2 + 300, 930, 46, TINTA2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("um sódio só?", "i", 74), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s13.b"], "NaSO4", 520, 480, 170, align="center", cor=ERRADO)
    if t >= C["s13.d"]:
        E.risco(c, 300, 500, 760, 380, t, C["s13.d"], largura=10)
    E.formula_em(c, t, C["s13.c"], "+1 − 2 = −1", 1360, 470, 100, "g", TINTA, "center")
    pilula_em(c, t, C["s13.d"], "sobrou carga", 1360, 600, 50, ERRADO)
    E.frase(c, t, C["s13.e"], ps("num sal, as cargas somam", "i", 70) + [("zero", "g", 66, COR)], W / 2, 820, "center", 0.12)
    Q.formula_em(c, t, C["s13.e"] + 0.8, "Na2SO4", W / 2 - 60, 990, 110, align="center", cores={"indice": E.COR})
    E.foco(c, t, C["s13.e"] + 1.2, 0.5, lambda a: E.selo(c, W / 2 + 260, 955, 44, True, a))


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        palco_titulo(c, t, C["s14"], "o atalho de prova")
        E.frase(c, t, C["s14.a"], [("cruze", "g", 70, BR)] + ps("as cargas: a carga de um vira o índice do outro", "i", 62, CLARO), W / 2, 270, "center", 0.1)
        Q.formula_em(c, t, C["s14.b"], "Al^3+", 640, 520, 150, align="center", escuro=True, cores={"carga": E.CLARO})
        Q.formula_em(c, t, C["s14.b"] + 0.4, "SO4^2-", 1240, 520, 150, align="center", escuro=True, cores={"carga": E.CLARO})
        G = Q.grupos("Al2(SO4)3", W / 2, 900, 150, "center")
        cruza(c, t, C["s14.c"], 745, 400, G[-1]["x1"] - 22, 860)
        cruza(c, t, C["s14.c"] + 0.4, 1370, 400, G[0]["x1"] - 22, 860)
        Q.formula_em(c, t, C["s14.d"], "Al2(SO4)3", W / 2, 900, 150, align="center", escuro=True, cores={"indice": E.CLARO})
        return
    palco_titulo(c, t, C["s15"], "funciona porque")
    E.formula_em(c, t, C["s15.a"], "+3 +3 = +6", W / 2, 330, 90, "g", BR, "center")
    E.formula_em(c, t, C["s15.b"], "−2 −2 −2 = −6", W / 2, 460, 90, "g", BR, "center")
    E.frase(c, t, C["s15.c"], [("cuidado:", "g", 62, ERRADO)] + ps("cargas iguais", "i", 66, CLARO), W / 2, 640, "center", 0.12)
    Q.formula_em(c, t, C["s15.c"] + 1.0, "Ca^2+ + SO4^2-", W / 2, 780, 100, align="center", escuro=True)
    E.frase(c, t, C["s15.d"], ps("um de cada já zera:", "i", 62, CLARO), W / 2 - 160, 960, "right", 0.1)
    Q.formula_em(c, t, C["s15.e"], "CaSO4", W / 2 - 100, 970, 110, escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        Q.formula_em(c, t, C["s16.a"], "Mg(OH)2", 1500, 420, 130, align="center")
        E.foco(c, t, C["s16.b"], 0.4, lambda a: E.escreve(c, "+", 1480, 560, 90, "g", TINTA2, a))
        Q.formula_em(c, t, C["s16.b"] + 0.2, "HCl", 1500, 720, 130, align="center")
    questao(c, t, C, "s16", [(C["s16.a"], ps("leite de magnésia (hidróxido de magnésio)", "i", 56, TINTA2), 300),
                             (C["s16.b"], ps("com o ácido clorídrico do estômago", "i", 56, TINTA2), 390),
                             (C["s16.c"], [("1", "g", 56, COR)] + ps("qual sal se forma? fórmula e nome", "i", 60), 560),
                             (C["s16.d"], [("2", "g", 56, COR)] + ps("quantas moléculas de água?", "i", 60), 680)], "s17", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ion_em(c, t, C["s18.a"], 440, 300, 70, "Mg", "2+")
    E.foco(c, t, C["s18.a"] + 0.3, 0.4, lambda a: centro(c, "da base", 440, 410, 48, "i", TINTA2, a))
    ion_em(c, t, C["s18.b"], 760, 300, 62, "Cl", "-")
    ion_em(c, t, C["s18.c"], 940, 300, 62, "Cl", "-")
    E.foco(c, t, C["s18.b"] + 0.3, 0.4, lambda a: centro(c, "do ácido", 850, 410, 48, "i", TINTA2, a))
    Q.formula_em(c, t, C["s18.d"], "MgCl2", 1180, 330, 120, cores={"indice": E.COR})
    E.foco(c, t, C["s18.d"] + 0.5, 0.4, lambda a: E.escreve(c, "cloreto de magnésio", 1180, 420, 52, "i", TINTA, a))
    if t >= C["s19"]:
        eq = "Mg(OH)2 + 2 HCl -> MgCl2 + 2 H2O"
        Q.equacao(c, t, C["s19.a"], eq, W / 2, 680, 100, tl=[C["s19.a"], C["s19.b"] - 0.1, C["s19.b"], C["s19.c"] - 0.2, C["s19.c"], C["s19.d"] - 0.1, C["s19.d"]],
                  cores={"coef": E.COR})
        E.frase(c, t, C["s19.a"], [("2 OH⁻", "g", 62, BASE)] + ps("pedem", "i", 66) + [("2 H⁺", "g", 62, ACIDO)], W / 2, 540, "center", 0.12)
        bola_txt(c, t, C["s19.d"] + 0.4, "2", 820, 900, 70, 80, CERTO)
        E.foco(c, t, C["s19.d"] + 0.6, 0.4, lambda a: E.escreve(c, "moléculas de água", 920, 925, 66, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        for i, f in enumerate(("CO2", "SO3", "CaO")):
            Q.formula_em(c, t, C["s21.b"] + 0.3 * i, f, XE + i * 300, 800, 110)
    fim(c, t, C, "s20", [("s20.a", [("ácido", "g", 66, ACIDO), ("+", "g", 66, TINTA2), ("base", "g", 66, BASE), ("→", "g", 66, COR), ("sal", "g", 66), ("+", "g", 66, TINTA2), ("água", "g", 66)]),
                         ("s20.b", [("H⁺", "g", 66), ("+", "g", 66, TINTA2), ("OH⁻", "g", 66), ("→", "g", 66, COR), ("água", "g", 66)]),
                         ("s20.c", [("ídrico", "g", 66), ("→", "g", 66, COR), ("eto,", "g", 66), ("ico", "g", 66), ("→", "g", 66, COR), ("ato", "g", 66)])],
        "s21", "Óxidos", None, "s21.c", "s21.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, neutraliza=b_neutraliza, sal=b_sal, nomes=b_nomes, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
