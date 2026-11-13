"""Visual — Estudativo · QUI-INO-010: simples troca e fila de reatividade.
Linguagem visual: a da Química (QUI-MIS-001), a da trilha (QUI-INO-007) e a do módulo (QUI-INO-008). Peça nova: a FILA DE
REATIVIDADE (fila): fichas dos metais em linha, o H no meio em destaque, seta "mais reativo" para a esquerda; os dois que
disputam o lugar acendem. Metal no ácido = béquer com a placa e bolhas quando reage (placa)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-010_simples_troca_fila_reatividade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('troca', 'fila', 'metais', 'atalho', 'questao', 'fim'))
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
for eq in ("Zn + 2 HCl -> ZnCl2 + H2", "Mg + 2 HCl -> MgCl2 + H2", "Fe + Cu^2+ -> Fe^2+ + Cu", "Cu + 2 Ag^+ -> Cu^2+ + 2 Ag", "Cl2 + 2 NaBr -> 2 NaCl + Br2"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
FILA = ("K", "Ca", "Na", "Mg", "Al", "Zn", "Fe", "H", "Cu", "Ag", "Au")
FX0, FDX = 170, 158


def fx(s):
    return FX0 + FILA.index(s) * FDX + 60


def fila(c, t, t0, y, acende=(), passo=0.08, r=52, escuro=False):
    """a fila dos metais, com o hidrogênio no meio"""
    for i, s in enumerate(FILA):
        x = FX0 + i * FDX + 60
        k = ease_back(prog(t, t0 + passo * i, 0.4))
        if k <= 0:
            continue
        if s == "H":
            E.bola(c, x, y, r * 1.1 * k, E.COR, 1)
            centro(c, "H", x, y + r * 0.4 * k, r * 1.1 * k, "g", BR, 1)
        else:
            Q.atomo(c, x, y, r * k, s, 1, escuro=escuro)
        if s in acende:
            c.drawCircle(x, y, r + 14 + 3 * math.sin(t * 5), M.paint(E.COR if not escuro else E.CLARO, 1, stroke=6))
    q = ep(t, t0 + passo * len(FILA), 0.4)
    if q > 0:
        M.arrow(c, FX0 + FDX * 6.8, y + r + 50, FX0 + 40, y + r + 50, CLARO if escuro else TINTA2, q, 4, 16)
        E.escreve(c, "mais reativo", FX0 + 60, y + r + 100, 40, "i", CLARO if escuro else TINTA2, q)


def placa(c, t, t0, cx, yb, metal, reage, te=None):
    """béquer com ácido e uma placa de metal; com reage, sobem bolhas de H₂"""
    Q.bequer(c, t, t0, cx, yb, 280, 320, 0.7, Q.AGUA)
    q = ep(t, t0 + 0.3, 0.4)
    if q <= 0:
        return
    cor = Q.cor_el(metal)
    M.rrect(c, cx - 30, yb - 330, 60, 280, 8, cor, q, shadow=True)
    centro(c, metal, cx, yb - 300, 40, "g", BR, q)
    if reage and t >= (te or t0):
        for k in range(10):
            f = ((t - (te or t0)) * 0.6 + k / 10) % 1
            x = cx + (-50 if k % 2 else 50) + 8 * math.sin(t * 3 + k)
            c.drawCircle(x, yb - 40 - f * 170, 8 + 6 * f, M.paint(TINTA2, q * (1 - f * 0.6), stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("zinco", "g", 80)] + ps("no ácido:", "i", 80), XE, 260, passo=0.14)
        E.frase(c, t, C["s01.b"], [("borbulha", "g", 76, COR)], XE, 370)
        E.frase(c, t, C["s01.c"], [("cobre", "g", 80)] + ps("no mesmo ácido:", "i", 80), XE, 540, passo=0.14)
        E.frase(c, t, C["s01.d"], [("nada", "g", 76, TINTA2)], XE, 650)
        E.frase(c, t, C["s01.e"], ps("os dois são metais.", "i", 70) + [("Por que só um?", "g", 66, COR)], XE, 860, passo=0.12)
        placa(c, t, C["s01.a"], 1400, 900, "Zn", True, C["s01.b"])
        placa(c, t, C["s01.c"], 1730, 900, "Cu", False)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("reconhecer", "g", 70), ("a", "i", 74), ("simples troca", "g", 70, COR)]),
                              (C["s02.b"], [("usar", "i", 74), ("a", "i", 74), ("fila", "g", 70, COR), ("de", "i", 74), ("reatividade", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 80, TINTA2), XE, 200)
    E.frase(c, t, C["s03.a"], [("metal", "g", 70)] + ps("perde elétrons e vira íon positivo", "i", 70), XE, 360, passo=0.1)
    Q.atomo_em(c, t, C["s03.a"] + 1.0, 640, 520, 60, "Zn")
    E.foco(c, t, C["s03.a"] + 1.4, 0.4, lambda a: M.arrow(c, 740, 520, 900, 520, TINTA2, a, 5, 18))
    ion_em(c, t, C["s03.a"] + 1.8, 1000, 520, 56, "Zn", "2+")
    Q.equacao(c, t, C["s03.b"], "HCl -> H^+ + Cl^-", W / 2, 820, 110, passo=0.3)
    E.foco(c, t, C["s03.b"] + 0.3, 0.4, lambda a: centro(c, "na água", W / 2 - 80, 700, 50, "i", TINTA2, a))


# ---------------- simples troca ----------------
def b_troca(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("duas palavras", "i", 76, TINTA2), XE, 200, passo=0.12)
        E.frase(c, t, C["s04.a"], [("simples:", "g", 76, COR)] + ps("um elemento só", "i", 76), XE, 380, passo=0.12)
        for i, f in enumerate(("Zn", "H2")):
            Q.formula_em(c, t, C["s04.a"] + 1.0 + 0.3 * i, f, 1250 + i * 300, 385, 100)
        E.frase(c, t, C["s04.b"], [("composta:", "g", 76, COR)] + ps("mais de um", "i", 76), XE, 620, passo=0.12)
        Q.formula_em(c, t, C["s04.b"] + 1.0, "HCl", 1250, 625, 100)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("simples troca:", "g", 80, COR)] + ps("o sozinho toma o lugar", "i", 74), XE, 230, passo=0.12)
        Q.equacao(c, t, C["s05.c"], "A + BC -> AC + B", W / 2, 560, 160, passo=0.3, cores={"A": E.COR})
        E.frase(c, t, C["s05.d"], [("A", "g", 66, COR)] + ps("entrou,", "i", 70) + [("B", "g", 66)] + ps("saiu sozinho", "i", 70), W / 2, 800, "center", 0.12)
        return
    E.frase(c, t, C["s06"], ps("veja o zinco", "i", 72, TINTA2), XE, 190, passo=0.12)
    cs = Q.equacao(c, t, C["s06.a"], "Zn + 2 HCl -> ZnCl2 + H2", W / 2, 420, 120, tl=[C["s06.a"], C["s06.a"] + 0.3, C["s06.a"] + 0.6, C["s06.b"] - 0.2, C["s06.b"], C["s06.b"] + 0.3, C["s06.b"] + 0.5],
                    cores={"Zn": E.COR})
    E.foco(c, t, C["s06.c"], 0.4, lambda a: centro(c, "o zinco tomou o lugar do H", W / 2, 580, 56, "i", TINTA, a))
    placa(c, t, C["s06.d"] - 0.4, W / 2, 1000, "Zn", True, C["s06.d"])
    E.foco(c, t, C["s06.d"] + 0.4, 0.4, lambda a: E.escreve(c, "bolhas de H₂", W / 2 + 200, 820, 54, "g", TINTA, a))


# ---------------- fila ----------------
def b_fila(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("só troca se quem entra for", "i", 70) + [("mais reativo", "g", 66, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s07.b"], [("mais reativo", "g", 62)] + ps("= perde elétrons com mais facilidade", "i", 64) if False else [("mais reativo:", "g", 62)] + ps("perde elétrons com mais facilidade", "i", 64), XE, 400, passo=0.1)
        Q.atomo_em(c, t, C["s07.c"], 600, 680, 70, "Zn")
        E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: centro(c, ">", 860, 710, 110, "g", COR, a))
        E.foco(c, t, C["s07.c"] + 0.5, 0.4, lambda a: (E.bola(c, 1100, 680, 60, E.COR, a), centro(c, "H", 1100, 704, 66, "g", BR, a)))
        E.frase(c, t, C["s07.c"] + 1.0, ps("o zinco empurra o hidrogênio para fora", "i", 60, TINTA2), W / 2, 900, "center", 0.1)
        return
    E.frase(c, t, C["s08.a"], [("a fila de reatividade", "g", 76, COR)], XE, 200)
    acende = ("Cu", "H") if t >= C["s09"] else ()
    fila(c, t, C["s08.b"], 520, acende)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: centro(c, "no meio, o hidrogênio", fx("H"), 420, 46, "b", COR, a))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: centro(c, "menos reativos", fx("Ag"), 650, 46, "b", TINTA2, a))
    if t >= C["s09"]:
        E.frase(c, t, C["s09.a"], [("Cu", "g", 64)] + ps("depois do", "i", 66) + [("H:", "g", 64, COR)] + ps("menos reativo", "i", 66), XE, 800, passo=0.12)
        E.frase(c, t, C["s09.c"], ps("o cobre", "i", 66) + [("não reage", "g", 62, ERRADO)] + ps("com o ácido", "i", 66), XE, 900, passo=0.12)
        pilula_em(c, t, C["s09.d"], "ouro e prata: joias por séculos", 1500, 900, 44, "#C9A227")


# ---------------- metal com metal ----------------
def prego(c, cx, y0, y1, cobre, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - 16, y0, 32, y1 - y0, 8, E.mix("#8A8F98", "#B4532A", cobre), a, shadow=True)
    M.rrect(c, cx - 40, y0 - 18, 80, 24, 8, E.mix("#8A8F98", "#B4532A", cobre * 0.5), a)


def b_metais(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("entre metais também", "i", 72, TINTA2), XE, 200, passo=0.12)
        Q.bequer(c, t, C["s10.a"], 1450, 920, 340, 400, 0.72, lambda tt: Q.muda_cor(tt, C["s10.d"], "#4A8FE0", "#A9C8EE", 2.0))
        cob = ease_io(prog(t, C["s10.d"], 2.0))
        E.foco(c, t, C["s10.a"] + 0.3, 0.4, lambda a: prego(c, 1450, 560, 880, cob, a))
        E.frase(c, t, C["s10.a"], ps("prego de", "i", 66) + [("ferro", "g", 62)] + ps("na solução azul de", "i", 66) + [("Cu²⁺", "g", 62, "#2B6CB0")], XE, 360, passo=0.1)
        E.frase(c, t, C["s10.b"], [("Fe", "g", 66)] + ps("é mais reativo que", "i", 66) + [("Cu", "g", 66)], XE, 500, passo=0.12)
        Q.equacao(c, t, C["s10.c"], "Fe + Cu^2+ -> Fe^2+ + Cu", XE, 700, 82, align="left", passo=0.3)
        E.frase(c, t, C["s10.d"], ps("o cobre se deposita,", "i", 62) + [("avermelhado", "g", 58, "#B4532A")], XE, 880, passo=0.1)
        return
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("e o contrário?", "i", 76, TINTA2) + [("Cu", "g", 70)] + ps("nos íons de", "i", 76, TINTA2) + [("Fe", "g", 70)], XE, 220, passo=0.12)
        fila(c, t, C["s11"], 520, ("Cu", "Fe"), passo=0.0)
        E.frase(c, t, C["s11.b"], ps("o cobre está à direita do ferro:", "i", 64) + [("menos reativo", "g", 60)], XE, 820, passo=0.1)
        E.frase(c, t, C["s11.d"], [("nada acontece", "g", 70, TINTA2)], XE, 950)
        return
    E.frase(c, t, C["s12.a"], ps("ametais: outra fila", "i", 76, TINTA2), XE, 220, passo=0.12)
    for i, s in enumerate(("F", "Cl", "Br", "I")):
        Q.atomo_em(c, t, C["s12.b"] + 0.3 * i, 460 + i * 300, 440, 66, s)
    E.foco(c, t, C["s12.b"] + 1.4, 0.4, lambda a: M.arrow(c, 1300, 560, 420, 560, TINTA2, a, 4, 16))
    Q.formula_em(c, t, C["s12.c"], "Cl2 + 2 NaBr -> 2 NaCl + Br2", XE, 720, 80)
    E.foco(c, t, C["s12.c"] + 0.5, 0.5, lambda a: E.selo(c, 1380, 695, 36, True, a))
    Q.formula_em(c, t, C["s12.d"], "I2 + NaCl", XE, 840, 80)
    E.foco(c, t, C["s12.d"] + 0.4, 0.4, lambda a: E.escreve(c, "não reage", XE + 420, 840, 60, "g", ERRADO, a))
    E.frase(c, t, C["s12.e"], ps("nos ametais, mais reativo", "i", 58, TINTA2) + [("ganha", "g", 54, COR)] + ps("elétron mais fácil", "i", 58, TINTA2), XE, 990, passo=0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("todo metal reage com ácido?", "i", 74), XE + 450, 190, passo=0.12)
    fila(c, t, C["s13.a"] + 0.5, 470, passo=0.05)
    lado(c, t, C["s13.b"], fx("K") - 50, fx("Fe") + 50, 660, "reagem com HCl", COR)
    lado(c, t, C["s13.c"], fx("Cu") - 50, fx("Au") + 50, 660, "ficam parados", ERRADO)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    palco_titulo(c, t, C["s14"], "o atalho de prova")
    if t < C["s15"]:
        E.frase(c, t, C["s14.a"], ps("ache os dois que disputam:", "i", 64, CLARO) + [("o sozinho", "g", 60, BR)] + ps("e", "i", 64, CLARO) + [("o preso", "g", 60, BR)], W / 2, 280, "center", 0.1)
        fila(c, t, C["s14.b"], 520, ("Zn", "H"), passo=0.03, escuro=True)
        E.frase(c, t, C["s14.c"], ps("o sozinho mais à esquerda?", "i", 64, CLARO) + [("reage", "g", 60, BR)], W / 2, 820, "center", 0.1)
        E.frase(c, t, C["s14.d"], ps("mais à direita?", "i", 64, CLARO) + [("não reage", "g", 60, ERRADO)], W / 2, 930, "center", 0.1)
        return
    E.frase(c, t, C["s15.a"], ps("o mais reativo sempre fica como", "i", 64, CLARO) + [("íon", "g", 60, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 60, ERRADO)] + ps("compensa decorar a fila inteira", "i", 64, CLARO), W / 2, 460, "center", 0.1)
    fila(c, t, C["s15.c"], 680, ("H", "Au"), passo=0.03, escuro=True)
    E.foco(c, t, C["s15.c"] + 1.0, 0.4, lambda a: centro(c, "guarde o H no meio e o ouro na ponta", W / 2, 940, 54, "b", CLARO, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar: use a fila", "i", 72, COR), XE, 180, passo=0.12)
    fila(c, t, C["s16"] + 0.5, 360, passo=0.03, r=44)
    E.frase(c, t, C["s16.a"], [("1", "g", 56, COR)] + ps("com HCl, reage o magnésio ou a prata?", "i", 60), XE, 640, passo=0.08)
    E.frase(c, t, C["s16.b"], [("2", "g", 56, COR)] + ps("fio de cobre numa solução de", "i", 60) + [("Ag⁺", "g", 56)], XE, 760, passo=0.08)
    E.frase(c, t, C["s16.c"], ps("há troca?", "i", 60), XE + 60, 850, passo=0.08)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1580, cy=740, r=140)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    acende = ("Mg", "H") if t < C["s18.c"] else ("Ag", "H") if t < C["s19"] else ("Cu", "Ag")
    fila(c, t, C["s18"], 330, acende, passo=0.0, r=46)
    if t < C["s19"]:
        Q.formula_em(c, t, C["s18.b"], "Mg + 2 HCl -> MgCl2 + H2", XE, 620, 90)
        E.foco(c, t, C["s18.b"] + 0.5, 0.5, lambda a: E.selo(c, 1560, 590, 40, True, a))
        Q.formula_em(c, t, C["s18.d"], "Ag + HCl", XE, 780, 90)
        E.foco(c, t, C["s18.d"] + 0.4, 0.4, lambda a: E.escreve(c, "não reage", XE + 470, 780, 66, "g", ERRADO, a))
        return
    E.frase(c, t, C["s19.a"], [("Cu", "g", 64)] + ps("antes da", "i", 66) + [("Ag:", "g", 64)] + ps("mais reativo", "i", 66), XE, 600, passo=0.12)
    Q.formula_em(c, t, C["s19.c"], "Cu + 2 Ag^+ -> Cu^2+ + 2 Ag", XE, 760, 90)
    E.foco(c, t, C["s19.c"] + 0.5, 0.5, lambda a: E.selo(c, 1620, 730, 40, True, a))
    E.frase(c, t, C["s19.d"], ps("a prata se deposita:", "i", 60) + [("árvore prateada", "g", 56, "#7D8590")], XE, 900, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        Q.equacao(c, t, C["s21.a"], "AB + CD -> AD + CB", 700, 760, 100, passo=0.3)
        E.frase(c, t, C["s21.b"], ps("sólido, gás ou água", "i", 62, TINTA2), XE, 900, passo=0.1)
    fim(c, t, C, "s20", [("s20.a", [("o", "i", 72), ("sozinho", "g", 66, COR), ("toma", "i", 72), ("o", "i", 72), ("lugar", "g", 66)]),
                         ("s20.b", [("só", "i", 72), ("se", "i", 72), ("for", "i", 72), ("mais reativo", "g", 66, COR)]),
                         ("s20.c", [("antes", "g", 66), ("do", "i", 72), ("H:", "g", 66, COR), ("reage", "i", 72), ("com", "i", 72), ("HCl", "g", 66)])],
        "s21", "Dupla troca", None, "s21.c", "s21.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, troca=b_troca, fila=b_fila, metais=b_metais, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
