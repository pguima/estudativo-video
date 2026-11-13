"""Visual — Estudativo · QUI-INO-012: praticando reações e balanceamento (aula de prática, cinco questões; última da trilha).
Linguagem visual: a da Química (QUI-MIS-001), a da trilha (QUI-INO-007) e a do módulo (QUI-INO-008): placar do balanceamento,
fila de reatividade, pílulas dos tipos de reação (síntese azul, análise roxo, simples troca turquesa, dupla troca âmbar)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-012_praticando_reacoes_balanceamento.mp4"
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
BUT = ["C4H10 + O2 -> CO2 + H2O", "C4H10 + O2 -> 4 CO2 + 5 H2O", "2 C4H10 + O2 -> 8 CO2 + 10 H2O", "2 C4H10 + 13 O2 -> 8 CO2 + 10 H2O"]
for eq in (BUT[-1], "CaCO3 -> CaO + CO2", "2 H2 + O2 -> 2 H2O", "Zn + 2 HCl -> ZnCl2 + H2", "AgNO3 + NaCl -> AgCl + NaNO3",
           "Fe + 2 HCl -> FeCl2 + H2", "KCl + AgNO3 -> AgCl + KNO3", "Na2SO4 + 2 KNO3 -> 2 NaNO3 + K2SO4"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert 4 * 2 + 5 == 13 and 16 + 10 == 26 == 13 * 2 and 2 + 13 + 8 + 10 == 33 and 4 + 32 == 36
TIPO = {"síntese": "#2B8FD6", "análise": "#8E5BD0", "simples troca": E.COR, "dupla troca": "#E09A10"}
FILA = ("K", "Ca", "Na", "Mg", "Al", "Zn", "Fe", "H", "Cu", "Ag", "Au")


def estagio(t, lista, tempos):
    k = sum(1 for x in tempos if t >= x)
    return lista[min(k, len(lista) - 1)]


def placar(c, t, t0, eq, x, y, els, size=56, dy=84):
    esq, dir_ = Q.lados(eq)
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    E.escreve(c, "esquerda", x + 150, y - size * 1.1, size * 0.6, "i", TINTA2, q)
    E.escreve(c, "direita", x + 420, y - size * 1.1, size * 0.6, "i", TINTA2, q)
    for i, el in enumerate(els):
        yy = y + i * dy
        Q.atomo(c, x + 40, yy - size * 0.33, size * 0.42, el, q)
        a_, b_ = esq.get(el, 0), dir_.get(el, 0)
        ok = a_ == b_
        centro(c, str(a_), x + 230, yy, size, "g", TINTA if ok else ERRADO, q)
        centro(c, str(b_), x + 480, yy, size, "g", TINTA if ok else ERRADO, q)
        if ok:
            E.selo(c, x + 620, yy - size * 0.33, size * 0.36, True, q)


def fila(c, t, t0, y, acende=(), r=44):
    for i, s in enumerate(FILA):
        x = 230 + i * 150
        k = ease_back(prog(t, t0 + 0.03 * i, 0.4))
        if k <= 0:
            continue
        if s == "H":
            E.bola(c, x, y, r * 1.1 * k, E.COR, 1)
            centro(c, "H", x, y + r * 0.4 * k, r * 1.1 * k, "g", BR, 1)
        else:
            Q.atomo(c, x, y, r * k, s, 1)
        if s in acende:
            c.drawCircle(x, y, r + 12 + 3 * math.sin(t * 5), M.paint(E.COR, 1, stroke=6))
    q = ep(t, t0 + 0.4, 0.4)
    if q > 0:
        M.arrow(c, 230 + 150 * 6.6, y + r + 40, 200, y + r + 40, TINTA2, q, 4, 16)
        E.escreve(c, "mais reativo", 230, y + r + 90, 38, "i", TINTA2, q)


def cabeca(c, t, t0, n, txt):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 170, 56, a=a), centro(c, str(n), XE + 50, 194, 66, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, ps(txt, "i", 66, TINTA2), XE + 140, 192, passo=0.1)


def pausa(c, t, C, k, cx=1560, cy=640, r=170):
    E.relogio(c, t, C[k + ".a"], cx=cx, cy=cy, r=r)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    for i, (k, txt) in enumerate((("s01.a", "balancear"), ("s01.b", "classificar"), ("s01.c", "prever"))):
        pilula_em(c, t, C[k], txt, 420 + i * 540, 420, 76, E.COR)
    E.frase(c, t, C["s01.d"], [("5", "g", 110, COR)] + ps("questões que juntam o módulo", "i", 80), W / 2, 720, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("as ferramentas", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s02.a"], [("balancear:", "g", 66, COR), ("MACHO", "g", 66)] + ps("(metal, ametal, C, H, O)", "i", 60, TINTA2), XE, 380, passo=0.12)
    E.frase(c, t, C["s02.b"], [("simples troca:", "g", 66, COR)] + ps("a fila de reatividade", "i", 66), XE, 540, passo=0.12)
    E.frase(c, t, C["s02.c"], [("dupla troca:", "g", 66, COR)] + ps("sólido, gás ou água", "i", 66), XE, 700, passo=0.12)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    cabeca(c, t, C["s03"], 1, "o gás do isqueiro")
    E.frase(c, t, C["s03.a"], ps("balanceie a queima completa do butano", "i", 62), XE, 340, passo=0.1)
    Q.equacao(c, t, C["s03.b"], BUT[0], XE, 520, 104, align="left", passo=0.25)
    E.frase(c, t, C["s03.c"], ps("qual é a", "i", 64) + [("soma dos coeficientes?", "g", 60, COR)], XE, 700, passo=0.1)
    if t >= C["s04"]:
        pausa(c, t, C, "s04", cy=700, r=130)


def b_r1(c, t, C, b):
    eq = estagio(t, BUT, [C["s05.b"], C["s06.b"], C["s06.d"]])
    Q.equacao(c, t, C["s05"], eq, W / 2, 230, 100, tl=[C["s05"]] * 7, cores={"coef": E.COR})
    els = ["C"] if t < C["s05.b"] else ["C", "H"] if t < C["s05.c"] else ["C", "H", "O"]
    placar(c, t, C["s05.a"], eq, 220, 440, els)
    if C["s05.c"] <= t < C["s06"]:
        E.formula_em(c, t, C["s05.c"], "4 × 2 + 5 = 13", 1450, 470, 66, "g", TINTA2, "center")
        pilula_em(c, t, C["s05.d"], "13: ímpar", 1450, 580, 50, ERRADO)
    if t >= C["s06"]:
        E.formula_em(c, t, C["s06.a"], "5 águas × 2 = 10", 1450, 440, 60, "g", TINTA2, "center")
        E.formula_em(c, t, C["s06.c"], "16 + 10 = 26", 1450, 540, 60, "g", TINTA2, "center")
        E.formula_em(c, t, C["s06.d"], "13 × 2 = 26", 1450, 640, 60, "g", COR, "center")
        E.formula_em(c, t, C["s06.e"], "2 + 13 + 8 + 10 =", 980, 900, 80, "g", TINTA, "right")
        bola_txt(c, t, C["s06.e"] + 1.6, "33", 1100, 875, 76, 76, CERTO)


# ---------------- questão 2 ----------------
Q2 = (("s07.a", "CaCO3 ->{Δ} CaO + CO2", "análise", "s09.a"), ("s07.b", "2 H2 + O2 -> 2 H2O", "síntese", "s09.b"),
      ("s07.c", "Zn + 2 HCl -> ZnCl2 + H2", "simples troca", "s09.c"), ("s07.d", "AgNO3 + NaCl -> AgCl + NaNO3", "dupla troca", "s09.d"))


def b_q2(c, t, C, b):
    cabeca(c, t, C["s07"], 2, "classifique cada reação")
    for i, (k, eq, _, _) in enumerate(Q2):
        Q.formula_em(c, t, C[k], eq, XE + 40, 360 + i * 160, 76)
    if t >= C["s08"]:
        pausa(c, t, C, "s08", cx=1640, cy=380, r=120)


def b_r2(c, t, C, b):
    E.frase(c, t, C["s09"], ps("questão 2", "i", 60, TINTA2), XE, 170)
    for i, (k, eq, tipo, kr) in enumerate(Q2):
        y = 360 + i * 160
        Q.formula_em(c, t, C["s09"], eq, XE + 40, y, 72)
        pilula_em(c, t, C[kr], tipo, 1560, y - 24, 50, TIPO[tipo])
    E.foco(c, t, C["s09.b"] + 1.4, 0.4, lambda a: E.escreve(c, "e também uma queima", 1050, 512, 40, "i", TINTA2, a))


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    cabeca(c, t, C["s10"], 3, "use a fila da tela")
    fila(c, t, C["s10"] + 0.5, 380)
    E.frase(c, t, C["s10.a"], [("1", "g", 56, COR)] + ps("prego de ferro no ácido clorídrico: reage?", "i", 60), XE, 640, passo=0.08)
    E.frase(c, t, C["s10.b"], [("2", "g", 56, COR)] + ps("fio de cobre numa solução de", "i", 60) + [("Zn²⁺", "g", 56)] + ps(": reage?", "i", 60), XE, 760, passo=0.08)
    if t >= C["s11"]:
        pausa(c, t, C, "s11", cx=1640, cy=780, r=110)


def b_r3(c, t, C, b):
    acende = ("Fe", "H") if t < C["s12.c"] else ("Cu", "Zn")
    fila(c, t, C["s12"], 300, acende)
    Q.formula_em(c, t, C["s12.a"], "Fe + 2 HCl -> FeCl2 + H2", XE, 580, 86)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.selo(c, 1300, 555, 40, True, a))
    Q.formula_em(c, t, C["s12.c"], "Cu + Zn^2+", XE, 780, 86)
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "não reage: o cobre é menos reativo", XE + 500, 775, 54, "g", ERRADO, a))


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    cabeca(c, t, C["s13"], 4, "há reação?")
    Q.formula_em(c, t, C["s13.a"], "KCl + AgNO3", XE + 40, 420, 110)
    E.foco(c, t, C["s13.a"] + 0.4, 0.4, lambda a: E.escreve(c, "cloreto de potássio + nitrato de prata", XE + 40, 500, 48, "i", TINTA2, a))
    Q.formula_em(c, t, C["s13.b"], "Na2SO4 + KNO3", XE + 40, 680, 110)
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: E.escreve(c, "sulfato de sódio + nitrato de potássio", XE + 40, 760, 48, "i", TINTA2, a))
    if t >= C["s14"]:
        pausa(c, t, C, "s14", cx=1560, cy=560, r=160)


def b_r4(c, t, C, b):
    E.frase(c, t, C["s15"], ps("questão 4", "i", 60, TINTA2), XE, 170)
    Q.formula_em(c, t, C["s15.a"], "KCl + AgNO3 -> AgCl + KNO3", XE, 360, 84)
    pilula_em(c, t, C["s15.b"], "KNO₃: dissolve", 1050, 470, 44, TINTA2)
    pilula_em(c, t, C["s15.c"], "AgCl: precipita", 1460, 470, 44, E.COR)
    E.frase(c, t, C["s15.d"], [("há reação", "g", 62, CERTO)], XE, 480)
    if t >= C["s16"]:
        Q.formula_em(c, t, C["s16.a"], "Na2SO4 + 2 KNO3 -> 2 NaNO3 + K2SO4", XE, 680, 72)
        pilula_em(c, t, C["s16.b"], "sódio, potássio, nitrato", 1000, 790, 44, TINTA2)
        pilula_em(c, t, C["s16.c"], "tudo dissolve", 1480, 790, 44, TINTA2)
        E.frase(c, t, C["s16.d"], [("não", "g", 62, ERRADO), ("há", "g", 62), ("reação", "g", 62)], XE, 940, passo=0.12)


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    cabeca(c, t, C["s17"], 5, "Lavoisier e a queima")
    E.frase(c, t, C["s17.a"], ps("frasco fechado:", "i", 60, TINTA2) + [("4 g", "g", 58, COR)] + ps("de hidrogênio +", "i", 60) + [("32 g", "g", 58, COR)] + ps("de oxigênio", "i", 60), XE, 340, passo=0.08)
    E.frase(c, t, C["s17.b"], [("1", "g", 56, COR)] + ps("massa de água formada?", "i", 60), XE, 500, passo=0.08)
    E.frase(c, t, C["s17.c"], [("2", "g", 56, COR)] + ps("carvão com pouco oxigênio: que gás tóxico?", "i", 60), XE, 620, passo=0.08)
    if t >= C["s18"]:
        pausa(c, t, C, "s18", cx=1560, cy=760, r=120)


def b_r5(c, t, C, b):
    E.frase(c, t, C["s19"], ps("questão 5", "i", 60, TINTA2), XE, 170)
    Q.equacao(c, t, C["s19.a"], "2 H2 + O2 -> 2 H2O", W / 2, 360, 120, passo=0.3)
    Q.sob_termos(c, t, "2 H2 + O2 -> 2 H2O", W / 2, 360, 120, [["4 g", "32 g", "36 g" if t >= C["s19.b"] + 1.2 else "? g"]],
                 tl=[[C["s19.a"] + 0.6, C["s19.a"] + 0.9, C["s19.b"]]], size_l=64)
    E.formula_em(c, t, C["s19.b"], "4 + 32 =", 1000, 680, 84, "g", TINTA2, "right")
    bola_txt(c, t, C["s19.b"] + 1.2, "36 g", 1150, 650, 90, 64, CERTO)
    E.frase(c, t, C["s19.c"], ps("pouco oxigênio: queima", "i", 60) + [("incompleta", "g", 56, "#E09A10")], XE, 880, passo=0.1)
    pilula_em(c, t, C["s19.d"], "CO: monóxido de carbono", 1400, 860, 50, ERRADO)


# ---------------- fechamento (última da trilha) ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate((("s20.a", [("átomos", "g", 66, COR)] + ps("para balancear", "i", 72)),
                                         ("s20.b", [("substâncias", "g", 66, COR)] + ps("e quem troca, para classificar", "i", 72)),
                                         ("s20.c", [("fila", "g", 66, COR), ("ou", "i", 72), ("precipitado,", "g", 66, COR)] + ps("para prever", "i", 72)))):
            y = 360 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("trilha completa", "i", 80), XE, 250, passo=0.12)
    E.frase(c, t, C["s21"] + 0.8, [("Ácidos, bases,", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s21"] + 1.2, [("sais e reações", "g", 100, COR)], XE, 520)
    E.frase(c, t, C["s21.a"], ps("você já lê, balanceia e prevê uma reação", "i", 60, TINTA2), XE, 680, passo=0.1)
    E.foco(c, t, C["s21"] + 1.0, 0.6, lambda a: E.simbolo(c, 1560, 760, 170 * a, giro=6 * math.sin(t * 0.5)), blur=0)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE + 100, 960)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, q1=b_q1, r1=b_r1, q2=b_q2, r2=b_r2, q3=b_q3, r3=b_r3, q4=b_q4, r4=b_r4,
              q5=b_q5, r5=b_r5, fim=b_fim)
