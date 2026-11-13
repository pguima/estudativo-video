"""Visual — Estudativo · QUI-INO-011: dupla troca (precipitado, gás ou água).
Linguagem visual: a da Química (QUI-MIS-001), a da trilha (QUI-INO-007) e a do módulo (QUI-INO-008). Peça nova: TROCA DE
PARES (troca_pares): quatro íons em dois pares que se cruzam. Precipitado = grãos brancos caindo no béquer (precipita);
gás = bolhas. Seta ↓ do precipitado e ↑ do gás desenhadas ao lado da fórmula (seta_estado), porque a fonte não tem a seta."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-011_dupla_troca.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('troca', 'jeitos', 'regras', 'atalho', 'questao', 'fim'))
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
for eq in ("AgNO3 + NaCl -> AgCl + NaNO3", "Na2CO3 + 2 HCl -> 2 NaCl + H2CO3", "H2CO3 -> H2O + CO2", "HCl + NaOH -> NaCl + H2O",
           "BaCl2 + Na2SO4 -> BaSO4 + 2 NaCl"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
NO3, SO4 = "#3E6FB0", "#C9A227"


def troca_pares(c, t, t0, cx, cy, p, ions, r=56):
    """ions = [(s, carga, cor)] x4: pares (0,1) e (2,3) viram (0,3) e (2,1) com p 0→1"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    e = ease_io(p)
    ini = [(-330, -90), (-150, -90), (150, -90), (330, -90)]
    fim_ = [(-330, -90), (330, 110), (150, -90), (-150, 110)]
    fim_ = [(-300, -90), (300, 110), (300, -90), (-300, 110)]
    fim_ = [(-330, -90), (-150, 110), (150, -90), (330, 110)]
    # 0 fica, 3 vai para baixo de 0; 2 fica, 1 vai para baixo de 2
    alvo = {0: (-240, -90), 1: (240, 110), 2: (240, -90), 3: (-240, 110)}
    for i, (s, carga, cor) in enumerate(ions):
        x0, y0 = ini[i]
        x1, y1 = alvo[i]
        x = cx + lerp(x0, x1, e)
        y = cy + lerp(y0, y1, e) + (-60 * math.sin(math.pi * e) if i in (1, 3) else 0)
        ion(c, x, y, r if len(s) <= 2 else r * 1.1, s, carga, q, cor=cor)


def precipita(c, t, t0, cx, yb, w, n=24, cor="#FFFFFF"):
    if t < t0:
        return
    for k in range(n):
        f = clampf(prog(t, t0 + 0.05 * k, 1.6))
        x = cx - w * 0.38 + (k * 37 % 100) / 100 * w * 0.76
        y = lerp(yb - 230, yb - 22 - (k % 3) * 10, ease_io(f))
        q = ep(t, t0 + 0.05 * k, 0.3)
        c.drawCircle(x, y, 9, M.paint(cor, q))
        c.drawCircle(x, y, 9, M.paint(CINZA, q, stroke=2))


def bolhas(c, t, t0, cx, yb, w, h, n=10):
    if t < t0:
        return
    for k in range(n):
        f = ((t - t0) * 0.5 + k / n) % 1
        x = cx - w * 0.32 + (k * 37 % 100) / 100 * w * 0.64 + 6 * math.sin(t * 3 + k)
        c.drawCircle(x, yb - 20 - f * h, 9 + 6 * f, M.paint(TINTA2, ep(t, t0, 0.4) * (1 - f * 0.6), stroke=3))


def seta_estado(c, t, t0, x, y, desce=True, cor=TINTA):
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    if desce:
        M.arrow(c, x, y - 70, x, y + 10, cor, q, 7, 22)
    else:
        M.arrow(c, x, y + 10, x, y - 70, cor, q, 7, 22)


IONS1 = [("Ag", "+", None), ("NO3", "-", NO3), ("Na", "+", None), ("Cl", "-", None)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("nitrato de prata + cloreto de sódio", "i", 66), XE, 230, passo=0.1)
        E.frase(c, t, C["s01.b"], [("pó branco!", "g", 76, COR)], XE, 360)
        E.frase(c, t, C["s01.c"], ps("cloreto de sódio + nitrato de potássio", "i", 66), XE, 580, passo=0.1)
        E.frase(c, t, C["s01.d"], [("nada", "g", 76, TINTA2)] + ps("por quê?", "i", 76), XE, 710, passo=0.12)
        Q.bequer(c, t, C["s01.a"], 1350, 920, 300, 340, 0.7, Q.AGUA)
        precipita(c, t, C["s01.b"], 1350, 920, 300)
        Q.bequer(c, t, C["s01.c"], 1700, 920, 300, 340, 0.7, Q.AGUA)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("reconhecer", "g", 70), ("a", "i", 74), ("dupla troca", "g", 70, COR)]),
                              (C["s02.b"], [("prever", "g", 70), ("se", "i", 74), ("ela", "i", 74), ("acontece", "g", 70)]),
                              (C["s02.c"], [("sólido,", "g", 70, COR), ("gás", "g", 70, COR), ("ou", "i", 74), ("água", "g", 70, COR)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 80, TINTA2), XE, 200)
    E.frase(c, t, C["s03.a"], ps("sal dissolvido solta os seus íons", "i", 70), XE, 330, passo=0.1)
    Q.equacao(c, t, C["s03.b"], "AgNO3 -> Ag^+ + NO3^-", XE, 560, 100, align="left", passo=0.3)
    E.foco(c, t, C["s03.b"] + 0.6, 0.4, lambda a: E.escreve(c, "nitrato de prata", XE + 1100, 555, 50, "i", TINTA2, a))
    Q.equacao(c, t, C["s03.c"], "NaCl -> Na^+ + Cl^-", XE, 760, 100, align="left", passo=0.3)
    E.foco(c, t, C["s03.c"] + 0.6, 0.4, lambda a: E.escreve(c, "cloreto de sódio", XE + 1100, 755, 50, "i", TINTA2, a))


# ---------------- dupla troca ----------------
def b_troca(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("dupla troca:", "g", 80, COR)] + ps("dois compostos trocam de parceiros", "i", 66), XE, 230, passo=0.12)
        Q.equacao(c, t, C["s04.b"], "AB + CD -> AD + CB", W / 2, 520, 150, passo=0.3)
        E.frase(c, t, C["s04.c"], ps("o", "i", 66) + [("positivo", "g", 62)] + ps("de um fica com o", "i", 66) + [("negativo", "g", 62)] + ps("do outro", "i", 66), W / 2, 760, "center", 0.1)
        return
    if t < C["s06"]:
        p = prog(t, C["s05.b"], 1.6)
        troca_pares(c, t, C["s05.a"], W / 2, 420, p, IONS1)
        Q.formula_em(c, t, C["s05.b"], "AgNO3 + NaCl -> AgCl + NaNO3", W / 2, 800, 90, align="center")
        E.frase(c, t, C["s05.c"], ps("a prata ficou com o cloreto,", "i", 58), XE + 200, 950, passo=0.1)
        E.frase(c, t, C["s05.d"], ps("o sódio, com o nitrato", "i", 58), XE + 960, 950, passo=0.1)
        return
    E.frase(c, t, C["s06.a"], ps("só acontece se algum produto", "i", 70) + [("sair da solução", "g", 66, COR)], XE, 230, passo=0.12)
    Q.bequer(c, t, C["s06.b"], W / 2, 940, 420, 420, 0.72, Q.AGUA)
    for k, (s, carga, cor) in enumerate(IONS1 * 2):
        dx, dy = ((-150, 0), (60, -40), (140, 30), (-60, -150), (100, -140), (-130, -90), (10, 40), (150, -80))[k]
        x = W / 2 + dx + 20 * math.sin(t * 1.5 + k)
        y = 860 + dy + 14 * math.cos(t * 1.2 + k)
        if t >= C["s06.b"]:
            ion(c, x, y, 26 if len(s) <= 2 else 30, s, carga, ep(t, C["s06.b"] + 0.3, 0.4), cor=cor)
    E.frase(c, t, C["s06.c"], ps("íons soltos: é só uma", "i", 62, TINTA2) + [("mistura", "g", 58)], XE, 380, passo=0.1)


# ---------------- três jeitos ----------------
def b_jeitos(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("1", "g", 80, COR), ("precipitado", "g", 80)], XE, 230, passo=0.14)
        E.frase(c, t, C["s07.b"], ps("um sólido que não se dissolve e cai", "i", 64), XE, 340, passo=0.1)
        Q.bequer(c, t, C["s07.a"], 1500, 920, 320, 360, 0.7, Q.AGUA)
        precipita(c, t, C["s07.b"], 1500, 920, 320)
        Q.formula_em(c, t, C["s07.c"], "AgCl", XE, 600, 140)
        E.foco(c, t, C["s07.c"] + 0.4, 0.4, lambda a: E.escreve(c, "cloreto de prata: o pó branco", XE, 700, 52, "i", TINTA2, a))
        seta_estado(c, t, C["s07.d"], XE + 360, 590, True)
        E.foco(c, t, C["s07.d"] + 0.3, 0.4, lambda a: E.escreve(c, "setinha para baixo", XE + 420, 600, 50, "b", TINTA, a))
        return
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("com os estados", "i", 70, TINTA2), XE, 230, passo=0.12)
        eq = "AgNO3(aq) + NaCl(aq) -> AgCl(s) + NaNO3(aq)"
        Q.formula_em(c, t, C["s08.a"] + 0.4, eq, W / 2, 520, 76, align="center", cores={"AgCl": ERRADO} if False else None)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: centro(c, "(aq) = dissolvido em água", W / 2, 680, 56, "b", TINTA2, a))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: centro(c, "(s) = sólido: o precipitado", W / 2, 790, 56, "b", COR, a))
        E.frase(c, t, C["s08.d"], ps("um", "i", 64) + [("(s)", "g", 60, COR)] + ps("no meio dos", "i", 64) + [("(aq)", "g", 60)] + ps("é a pista", "i", 64), W / 2, 950, "center", 0.12)
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], [("2", "g", 80, COR), ("gás", "g", 80)] + ps("que escapa em bolhas", "i", 70), XE, 230, passo=0.14)
        Q.formula_em(c, t, C["s09.b"], "Na2CO3 + 2 HCl -> 2 NaCl + H2CO3", XE, 440, 72)
        Q.formula_em(c, t, C["s09.c"], "H2CO3 -> H2O + CO2", XE + 300, 600, 90)
        seta_estado(c, t, C["s09.d"], Q.grupos("H2CO3 -> H2O + CO2", XE + 300, 600, 90)[-1]["x1"] + 40, 590, False)
        Q.bequer(c, t, C["s09.a"], 1600, 940, 300, 300, 0.7, Q.AGUA)
        bolhas(c, t, C["s09.c"], 1600, 940, 300, 200)
        E.foco(c, t, C["s09.d"] + 0.3, 0.4, lambda a: E.escreve(c, "setinha para cima", XE + 300, 760, 50, "b", TINTA, a))
        return
    E.frase(c, t, C["s10.a"], [("3", "g", 80, COR), ("água", "g", 80)] + ps("quase não forma íons", "i", 70), XE, 230, passo=0.14)
    Q.equacao(c, t, C["s10.b"], "HCl + NaOH -> NaCl + H2O", W / 2, 520, 120, passo=0.3)
    pilula_em(c, t, C["s10.c"], "a neutralização é uma dupla troca", W / 2, 760, 56, E.COR)


# ---------------- regras ----------------
def b_regras(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("o sal precipita? duas regras", "i", 72, TINTA2), XE, 200, passo=0.12)
        E.foco(c, t, C["s11.a"], 0.4, lambda a: (E.bola(c, XE + 40, 344, 40, a=a), centro(c, "1", XE + 40, 362, 48, "g", BR, a)))
        E.frase(c, t, C["s11.a"], [("sódio,", "g", 66), ("potássio", "g", 66), ("e", "i", 70), ("nitrato:", "g", 66)] + ps("sempre se dissolvem", "i", 70), XE + 110, 370, passo=0.12)
        E.foco(c, t, C["s11.b"], 0.4, lambda a: (E.bola(c, XE + 40, 504, 40, a=a), centro(c, "2", XE + 40, 522, 48, "g", BR, a)))
        E.frase(c, t, C["s11.b"], [("cloreto", "g", 66)] + ps("se dissolve, menos o de", "i", 70) + [("prata", "g", 66, ERRADO), ("e", "i", 70), ("chumbo", "g", 66, ERRADO)], XE + 110, 530, passo=0.12)
        pilula_em(c, t, C["s11.c"], "os outros: a prova dá a tabela", W / 2, 760, 50, TINTA2)
        return
    E.frase(c, t, C["s12"], ps("a mistura que não deu nada", "i", 70, TINTA2), XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s12.a"], "NaCl + KNO3", XE, 380, 100)
    Q.formula_em(c, t, C["s12.b"], "-> NaNO3 + KCl", XE + 640, 380, 100)
    pilula_em(c, t, C["s12.c"], "dissolve", XE + 960, 480, 44, TINTA2)
    pilula_em(c, t, C["s12.c"] + 0.4, "dissolve", XE + 1380, 480, 44, TINTA2)
    for i, (k, txt) in enumerate((("s12.d", "sem precipitado"), ("s12.d", "sem gás"), ("s12.d", "sem água"))):
        E.foco(c, t, C[k] + 0.4 * i, 0.4, lambda a, i=i, txt=txt: E.escreve(c, txt, XE + i * 520, 680, 60, "g", TINTA2, a))
    E.frase(c, t, C["s12.e"], [("não", "g", 90, ERRADO), ("há", "g", 90), ("reação", "g", 90)], W / 2, 880, "center", 0.14)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("parar no ácido carbônico", "i", 74), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s13.b"], "H2CO3", XE, 420, 120)
    def errado():
        E.frase(c, t, C["s13.c"], ps("“nada sai da solução”", "i", 66, ERRADO), XE + 700, 410, passo=0.1)
        if t >= C["s13.c"] + 1.2:
            E.risco(c, XE + 690, 420, XE + 1300, 360, t, C["s13.c"] + 1.2, largura=8)
    E.saida(c, t, C["s13.d"] + 1.0, errado)
    Q.equacao(c, t, C["s13.d"], "H2CO3 -> H2O + CO2", W / 2, 640, 120, passo=0.3)
    seta_estado(c, t, C["s13.d"] + 1.2, Q.grupos("H2CO3 -> H2O + CO2", W / 2, 640, 120, "center")[-1]["x1"] + 40, 630, False)
    pilula_em(c, t, C["s13.e"], "tem gás: a reação acontece", W / 2, 840, 56, E.COR)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    palco_titulo(c, t, C["s14"], "o atalho de prova")
    if t < C["s15"]:
        E.frase(c, t, C["s14.a"], ps("olhe só os", "i", 66, CLARO) + [("dois produtos novos", "g", 62, BR)], W / 2, 290, "center", 0.12)
        Q.formula_em(c, t, C["s14.a"] + 0.8, "AgCl + NaNO3", W / 2, 520, 150, align="center", escuro=True)
        G = Q.grupos("AgCl + NaNO3", W / 2, 520, 150, "center")
        pilula_em(c, t, C["s14.b"], "sódio ou nitrato: dissolve", (G[2]["x0"] + G[-1]["x1"]) / 2, 660, 44, "#3A3B42")
        pilula_em(c, t, C["s14.c"], "o precipitado está aqui", (G[0]["x0"] + G[1]["x1"]) / 2, 660, 44, E.COR)
        return
    E.frase(c, t, C["s15.a"], ps("sais de", "i", 66, CLARO) + [("sódio, potássio", "g", 62, BR)] + ps("e", "i", 66, CLARO) + [("nitratos", "g", 62, BR)] + ps("nunca precipitam", "i", 66, CLARO), W / 2, 330, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO)] + ps("compensa se os dois produtos forem de outros tipos", "i", 62, CLARO), W / 2, 520, "center", 0.1)
    pilula_em(c, t, C["s15.c"], "aí, consulte a tabela de solubilidade", W / 2, 680, 50, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    Q.formula_em(c, t, C["s16.a"], "BaCl2 + Na2SO4", XE, 380, 110)
    E.foco(c, t, C["s16.a"] + 0.4, 0.4, lambda a: E.escreve(c, "cloreto de bário + sulfato de sódio", XE, 470, 50, "i", TINTA2, a))
    pilula_em(c, t, C["s16.b"], "o sulfato de bário não se dissolve", 640, 590, 44, TINTA)
    E.frase(c, t, C["s16.c"], [("1", "g", 56, COR)] + ps("quais são os produtos?", "i", 60), XE, 760, passo=0.08)
    E.frase(c, t, C["s16.d"], [("2", "g", 56, COR)] + ps("a reação acontece? por quê?", "i", 60), XE, 870, passo=0.08)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1560, cy=470, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ions = [("Ba", "2+", None), ("Cl", "-", None), ("Na", "+", None), ("SO4", "2-", SO4)]
    if t < C["s19"]:
        troca_pares(c, t, C["s18"], W / 2, 400, prog(t, C["s18.a"], 1.6), ions)
        Q.formula_em(c, t, C["s18.b"], "BaSO4", 560, 780, 110, align="center")
        Q.formula_em(c, t, C["s18.d"], "2 NaCl", 1360, 780, 110, align="center", cores={"coef": E.COR})
        E.foco(c, t, C["s18.b"] + 0.3, 0.4, lambda a: centro(c, "sulfato de bário", 560, 880, 50, "i", TINTA2, a))
        E.foco(c, t, C["s18.d"] + 0.3, 0.4, lambda a: centro(c, "cloreto de sódio", 1360, 880, 50, "i", TINTA2, a))
        return
    Q.formula_em(c, t, C["s19"], "BaCl2 + Na2SO4 -> BaSO4 + 2 NaCl", XE, 300, 84)
    seta_estado(c, t, C["s19.c"], [g for g in Q.grupos("BaCl2 + Na2SO4 -> BaSO4 + 2 NaCl", XE, 300, 84) if g["s"] == "O"][1]["x1"] + 30, 290, True)
    pilula_em(c, t, C["s19.a"], "NaCl: dissolve", 1300, 430, 44, TINTA2)
    Q.bequer(c, t, C["s19.b"], 560, 900, 320, 360, 0.7, Q.AGUA)
    precipita(c, t, C["s19.c"], 560, 900, 320)
    E.frase(c, t, C["s19.d"], ps("há reação:", "i", 66) + [("forma precipitado", "g", 62, COR)], 1000, 640, passo=0.12)
    E.frase(c, t, C["s19.e"], ps("é o contraste do", "i", 58, TINTA2) + [("raio X do estômago", "g", 54)], 1000, 760, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        for i, rot in enumerate(("balancear", "classificar", "prever")):
            pilula_em(c, t, C["s21.b"] + 0.3 * i, rot, XE + 160 + i * 380, 760, 54, E.COR)
    fim(c, t, C, "s20", [("s20.a", [("os", "i", 72), ("íons", "g", 66), ("trocam", "i", 72), ("de", "i", 72), ("parceiros", "g", 66, COR)]),
                         ("s20.b", [("só", "i", 72), ("com", "i", 72), ("sólido,", "g", 66, COR), ("gás", "g", 66, COR), ("ou", "i", 72), ("água", "g", 66, COR)]),
                         ("s20.c", [("sódio,", "g", 66), ("potássio,", "g", 66), ("nitrato:", "g", 66), ("dissolvem", "i", 72)])],
        "s21", "Praticando", "reações", "s21.c", "s21.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, troca=b_troca, jeitos=b_jeitos, regras=b_regras, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
