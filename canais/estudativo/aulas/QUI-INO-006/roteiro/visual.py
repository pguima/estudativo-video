"""Visual — Estudativo · QUI-INO-006: praticando ácidos, bases, sais e óxidos (aula de prática, cinco questões).
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007). Cada questão abre com o número na esfera
e o produto do dia a dia; a função entra como pílula na cor da escala de pH (gaveta)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-006_praticando_acidos_bases_sais_oxidos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('q1', 'q2', 'q3', 'q4', 'q5', 'fim'))
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
for eq in ("Al(OH)3 + 3 HCl -> AlCl3 + 3 H2O", "CO2 + H2O -> H2CO3", "CaO + H2O -> Ca(OH)2", "NH3 + HCl -> NH4^+ + Cl^-", "KOH + HNO3 -> KNO3 + H2O"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert 3 - 1 == 2 and 3 - 2 == 1
FUN = {"ácido": ACIDO, "base": BASE, "sal": E.COR, "óxido": TINTA2}


def cabeca(c, t, t0, n, txt):
    """número da questão na esfera + enunciado curto"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 56, a=a), centro(c, str(n), XE + 50, 194, 66, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, ps(txt, "i", 66, TINTA2), XE + 140, 192, passo=0.1)


def pausa(c, t, C, k):
    E.relogio(c, t, C[k + ".a"], cx=1500, cy=470, r=200)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    itens = (("ácido muriático", "HCl", "ácido"), ("soda cáustica", "NaOH", "base"), ("sal de cozinha", "NaCl", "sal"), ("cal viva", "CaO", "óxido"))
    for i, (nome, f, fun) in enumerate(itens):
        x = 300 + i * 440
        E.foco(c, t, C["s01.a"] + 0.5 * i, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 330, 50, "i", TINTA, a))
        Q.formula_em(c, t, C["s01.a"] + 0.5 * i + 0.2, f, x, 470, 110, align="center")
        pilula_em(c, t, C["s01.c"] + 0.4 * i, fun, x, 600, 54, FUN[fun])
    E.frase(c, t, C["s01.b"], ps("quatro gavetas", "i", 80), XE, 180, passo=0.12)
    E.frase(c, t, C["s01.d"], [("5", "g", 110, COR)] + ps("questões com coisas de casa", "i", 80), W / 2, 880, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as quatro pistas da fórmula", "i", 76, TINTA2), XE, 190, passo=0.12)
    linhas = (("s02.a", "HCl", "começa com H e solta H⁺", "ácido"), ("s02.b", "NaOH", "termina em OH", "base"),
              ("s02.c", "CaO", "dois elementos, um é O", "óxido"), ("s02.d", "NaCl", "metal + íon negativo de ácido", "sal"))
    for i, (k, f, txt, fun) in enumerate(linhas):
        y = 380 + i * 170
        Q.formula_em(c, t, C[k], f, XE, y, 100)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, txt=txt, y=y: E.escreve(c, txt, XE + 360, y - 8, 56, "b", TINTA, a))
        pilula_em(c, t, C[k] + 0.6, fun, 1560, y - 30, 54, FUN[fun])


# ---------------- questão 1 ----------------
ITENS1 = (("s03.a", "HCl", "ácido muriático", "ácido"), ("s03.b", "NaOH", "soda cáustica", "base"), ("s03.c", "NaCl", "sal de cozinha", "sal"), ("s03.d", "CaO", "cal viva", "óxido"))


def b_q1(c, t, C, b):
    cabeca(c, t, C["s03"], 1, "ácido, base, sal ou óxido?")
    for i, (k, f, nome, _) in enumerate(ITENS1):
        y = 380 + i * 170
        Q.formula_em(c, t, C[k], f, XE + 40, y, 110)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, XE + 400, y - 10, 56, "i", TINTA2, a))
    if t >= C["s04"]:
        pausa(c, t, C, "s04")


def b_r1(c, t, C, b):
    E.frase(c, t, C["s05"], ps("questão 1", "i", 60, TINTA2), XE, 170)
    pistas = ("começa com H", "termina em OH", "metal + cloreto", "2 elementos, um é O")
    for i, ((_, f, nome, fun), k, pista) in enumerate(zip(ITENS1, ("s05.a", "s05.b", "s05.c", "s05.d"), pistas)):
        y = 330 + i * 170
        Q.formula_em(c, t, C["s05"], f, XE + 40, y, 100)
        E.foco(c, t, C[k], 0.4, lambda a, pista=pista, y=y: E.escreve(c, pista, XE + 380, y - 10, 54, "i", TINTA, a))
        pilula_em(c, t, C[k] + 0.4, fun, 1200, y - 34, 54, FUN[fun])
    pilula_em(c, t, C["s05.e"], "óxido básico: o cálcio é metal", 1200, 960, 44, BASE)


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    cabeca(c, t, C["s06"], 2, "o antiácido")
    Q.formula_em(c, t, C["s06.a"], "Al(OH)3", XE + 40, 420, 140)
    E.foco(c, t, C["s06.a"] + 0.4, 0.4, lambda a: E.escreve(c, "hidróxido de alumínio", XE + 40, 500, 52, "i", TINTA2, a))
    Q.formula_em(c, t, C["s06.b"], "+ HCl", XE + 40, 650, 120)
    E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: E.escreve(c, "do estômago", XE + 40, 720, 52, "i", TINTA2, a))
    E.frase(c, t, C["s06.c"], [("1", "g", 56, COR)] + ps("qual sal?", "i", 60), XE, 880, passo=0.1)
    E.frase(c, t, C["s06.d"], [("2", "g", 56, COR)] + ps("quantas águas?", "i", 60), XE + 520, 880, passo=0.1)
    if t >= C["s07"]:
        pausa(c, t, C, "s07")


def b_r2(c, t, C, b):
    E.frase(c, t, C["s08"], ps("questão 2", "i", 60, TINTA2), XE, 170)
    if t < C["s09"]:
        ion_em(c, t, C["s08.a"], 560, 420, 80, "Al", "3+")
        for k in range(3):
            ion_em(c, t, C["s08.b"] + 0.25 * k, 900 + 170 * k, 420, 60, "Cl", "-")
        E.formula_em(c, t, C["s08.c"], "+3 − 1 − 1 − 1 = 0", W / 2, 640, 70, "g", TINTA2, "center")
        Q.formula_em(c, t, C["s08.d"], "AlCl3", W / 2, 830, 150, align="center", cores={"indice": E.COR})
        E.foco(c, t, C["s08.d"] + 0.5, 0.4, lambda a: centro(c, "cloreto de alumínio", W / 2, 940, 56, "i", TINTA, a))
        return
    eq = "Al(OH)3 + 3 HCl -> AlCl3 + 3 H2O"
    Q.equacao(c, t, C["s09"], eq, W / 2, 400, 104, tl=[C["s09"], C["s09.b"] - 0.1, C["s09.b"], C["s09.c"] - 0.2, C["s09.c"], C["s09.d"] - 0.1, C["s09.d"]],
              cores={"coef": E.COR})
    E.frase(c, t, C["s09.a"], [("3 OH⁻", "g", 62, BASE)] + ps("pedem", "i", 66) + [("3 H⁺", "g", 62, ACIDO)], W / 2, 240, "center", 0.12)
    bola_txt(c, t, C["s09.d"] + 0.3, "3", 820, 640, 70, 80, CERTO)
    E.foco(c, t, C["s09.d"] + 0.5, 0.4, lambda a: E.escreve(c, "moléculas de água", 920, 665, 66, "i", TINTA, a))
    E.frase(c, t, C["s09.e"], [("ácido", "g", 64, ACIDO), ("+", "g", 64, TINTA2), ("base", "g", 64, BASE), ("→", "g", 64, COR), ("sal", "g", 64), ("+", "g", 64, TINTA2), ("água", "g", 64)],
            W / 2, 900, "center", 0.12)


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    cabeca(c, t, C["s10"], 3, "o sopro e a cal")
    E.frase(c, t, C["s10.a"], ps("sopre num copo com", "i", 60) + [("repolho roxo", "g", 56, "#7A3FA0")], XE, 360, passo=0.1)
    E.frase(c, t, C["s10.b"], ps("o ar do pulmão tem", "i", 60) + [("CO₂", "g", 56)], XE, 460, passo=0.1)
    E.frase(c, t, C["s10.c"], [("1", "g", 56, COR)] + ps("vermelho ou verde?", "i", 60), XE, 600, passo=0.1)
    E.frase(c, t, C["s10.d"], [("2", "g", 56, COR)] + ps("cal viva + água + fenolftaleína: cor?", "i", 60), XE, 760, passo=0.1)
    if t < C["s11"]:
        Q.bequer(c, t, C["s10.a"], 1520, 860, 300, 360, 0.7, "#7A3FA0")
        E.foco(c, t, C["s10.a"] + 0.4, 0.4, lambda a: M.line(c, 1560, 500, 1600, 820, "#E9E9E4", a, 14))
    else:
        pausa(c, t, C, "s11")


def b_r3(c, t, C, b):
    E.frase(c, t, C["s12"], ps("questão 3", "i", 60, TINTA2), XE, 170)
    pilula_em(c, t, C["s12.a"], "CO₂: óxido ácido", 520, 320, 50, ACIDO)
    Q.formula_em(c, t, C["s12.b"], "CO2 + H2O -> H2CO3", 520, 480, 62, align="center")
    Q.bequer(c, t, C["s12.c"], 520, 860, 280, 300, 0.7, lambda tt: Q.muda_cor(tt, C["s12.c"] + 0.3, "#7A3FA0", "#C2457E", 1.0))
    E.foco(c, t, C["s12.c"] + 1.0, 0.4, lambda a: centro(c, "vai para o vermelho", 520, 960, 50, "g", "#C2457E", a))
    if t >= C["s13"]:
        pilula_em(c, t, C["s13.a"], "CaO: óxido básico", 1400, 320, 50, BASE)
        Q.formula_em(c, t, C["s13.b"], "CaO + H2O -> Ca(OH)2", 1400, 480, 62, align="center")
        Q.bequer(c, t, C["s13.c"], 1400, 860, 280, 300, 0.7, lambda tt: Q.muda_cor(tt, C["s13.c"] + 0.3, Q.AGUA, "#E85AA8", 1.0))
        E.foco(c, t, C["s13.c"] + 1.0, 0.4, lambda a: centro(c, "pH > 7: rosa", 1400, 960, 50, "g", "#E85AA8", a))


# ---------------- questão 4 ----------------
EQ4 = "NH3 + HCl -> NH4^+ + Cl^-"


def b_q4(c, t, C, b):
    cabeca(c, t, C["s14"], 4, "Brønsted-Lowry")
    Q.equacao(c, t, C["s14.a"], EQ4, XE, 460, 84, align="left", tl=[C["s14.a"], C["s14.a"] + 0.3, C["s14.a"] + 0.6, C["s14.b"] - 0.2, C["s14.b"], C["s14.b"] + 0.3, C["s14.b"] + 0.5])
    E.frase(c, t, C["s14.c"], [("1", "g", 56, COR)] + ps("quem é o ácido?", "i", 60), XE, 680, passo=0.1)
    E.frase(c, t, C["s14.c"] + 1.0, [("2", "g", 56, COR)] + ps("os dois pares conjugados?", "i", 60), XE, 790, passo=0.1)
    if t >= C["s15"]:
        pausa(c, t, C, "s15")


def b_r4(c, t, C, b):
    E.frase(c, t, C["s16"], ps("questão 4", "i", 60, TINTA2), XE, 170)
    y = 420
    cs = Q.equacao(c, t, C["s16"], EQ4, W / 2, y, 120, tl=[C["s16"]] * 7)
    pilula_em(c, t, C["s16.a"], "ácido: doou", cs[1], 280, 44, ACIDO)
    pilula_em(c, t, C["s16.b"], "base: recebeu", cs[0], 280, 44, BASE)
    for k, xa, xb, yy, cor, rot in (("s16.c", cs[1], cs[3], y + 60, ACIDO, "par 1: HCl e Cl⁻"), ("s16.d", cs[0], cs[2], y + 200, BASE, "par 2: NH₃ e NH₄⁺")):
        p = ep(t, C[k], 0.5)
        if p > 0:
            pth = skia.Path(); pth.moveTo(xa, yy); pth.lineTo(xa, yy + 60); pth.lineTo(xb, yy + 60); pth.lineTo(xb, yy)
            c.drawPath(pth, M.paint(cor, p, stroke=6))
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, xa=xa, xb=xb, yy=yy, cor=cor, rot=rot: centro(c, rot, (xa + xb) / 2, yy + 120, 46, "b", cor, a))


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    cabeca(c, t, C["s17"], 5, "força e nome")
    Q.formula_em(c, t, C["s17.a"], "HNO3", XE + 40, 420, 120)
    Q.formula_em(c, t, C["s17.a"] + 1.0, "H2CO3", XE + 500, 420, 120)
    E.frase(c, t, C["s17.b"], [("1", "g", 56, COR)] + ps("forte, moderado ou fraco?", "i", 60), XE, 620, passo=0.1)
    E.frase(c, t, C["s17.c"], [("2", "g", 56, COR)] + [("HNO₃ + KOH:", "g", 56)] + ps("que sal? e o nome?", "i", 60), XE, 740, passo=0.1)
    if t >= C["s18"]:
        pausa(c, t, C, "s18")


def b_r5(c, t, C, b):
    E.frase(c, t, C["s19"], ps("questão 5", "i", 60, TINTA2), XE, 170)
    Q.formula_em(c, t, C["s19.a"], "HNO3", XE, 340, 100)
    E.formula_em(c, t, C["s19.a"] + 0.4, "3 − 1 = 2", XE + 360, 340, 80, "g", TINTA2)
    pilula_em(c, t, C["s19.a"] + 0.8, "forte", 1000, 310, 52, E.COR)
    Q.formula_em(c, t, C["s19.b"], "H2CO3", XE, 500, 100)
    E.foco(c, t, C["s19.b"] + 0.3, 0.4, lambda a: E.escreve(c, "a exceção", XE + 360, 490, 60, "i", TINTA2, a))
    pilula_em(c, t, C["s19.b"] + 0.6, "fraco", 1000, 470, 52, TINTA2)
    Q.formula_em(c, t, C["s19.c"], "K^+ + NO3^-", XE, 720, 100)
    Q.formula_em(c, t, C["s19.d"], "KNO3", XE + 700, 720, 110, cores={"indice": E.COR})
    E.foco(c, t, C["s19.d"] + 0.4, 0.4, lambda a: E.escreve(c, "nitrato de potássio", XE + 700, 820, 60, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        Q.formula_em(c, t, C["s21.a"], "C3H8 + 5 O2 -> 3 CO2 + 4 H2O", XE, 820, 80, cores={"coef": E.COR})
    fim(c, t, C, "s20", [("s20.a", [("a", "i", 72), ("fórmula", "g", 66, COR), ("diz", "i", 72), ("a", "i", 72), ("função", "g", 66)]),
                         ("s20.b", [("ácido", "g", 66, ACIDO), ("+", "g", 66, TINTA2), ("base", "g", 66, BASE), ("→", "g", 66, COR), ("sal", "g", 66), ("+", "g", 66, TINTA2), ("água", "g", 66)]),
                         ("s20.c", [("óxido", "i", 72), ("de", "i", 72), ("ametal:", "g", 66, ACIDO), ("ácido;", "i", 72), ("de", "i", 72), ("metal:", "g", 66, BASE), ("base", "i", 72)])],
        "s21", "Balancear", "por tentativas", "s21.c", "s21.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
