"""Visual — Estudativo · QUI-INO-001: ácidos (ionização, nomes e força).
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007): íon = bolinha com selo de carga,
equação termo a termo, pílula ÁCIDO na cor da escala de pH. Peça nova: teste da lâmpada (lampada/teste_lampada)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-001_acidos_ionizacao_nomes_forca.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('ionizacao', 'nomes', 'forca', 'atalho', 'questao', 'fim'))
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
# as contas da aula
assert Q.lados("HCl -> H^+ + Cl^-")[0] == Q.lados("HCl -> H^+ + Cl^-")[1]
assert 4 - 2 == 2 and 3 - 1 == 2 and 3 - 2 == 1 and 4 - 3 == 1
assert Q.contar("H3PO4") == {"H": 3, "P": 1, "O": 4}


def lampada(c, cx, cy, r, acesa, a=1.0):
    """lâmpada: bulbo, rosca e brilho quando acesa (0..1)"""
    if a <= 0:
        return
    if acesa > 0:
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.6, [M.hexc("#FFD34D", 0.55 * acesa * a), M.hexc("#FFD34D", 0)], [0, 1]))
        c.drawCircle(cx, cy, r * 2.6, p)
    c.drawCircle(cx, cy, r, M.paint(E.mix("#F4F4F2", "#FFE27A", acesa), a))
    c.drawCircle(cx, cy, r, M.paint(TINTA2, a, stroke=4))
    M.rrect(c, cx - r * 0.45, cy + r * 0.85, r * 0.9, r * 0.6, 6, "#9AA0A8", a)
    M.line(c, cx - r * 0.25, cy + r * 0.2, cx, cy - r * 0.25, "#C9A227" if acesa else CINZA, a, 3)
    M.line(c, cx + r * 0.25, cy + r * 0.2, cx, cy - r * 0.25, "#C9A227" if acesa else CINZA, a, 3)


def teste_lampada(c, t, t0, cx, yb, cor_liq, acesa, n_ion=0, a_ion=1.0):
    """béquer com dois fios e a lâmpada em cima: acende quando há íons"""
    Q.bequer(c, t, t0, cx, yb, 300, 300, 0.7, cor_liq)
    q = ep(t, t0 + 0.2, 0.4)
    if q <= 0:
        return
    for dx in (-60, 60):
        M.line(c, cx + dx, yb - 150, cx + dx, yb - 420, TINTA, q, 5)
        M.rrect(c, cx + dx - 8, yb - 150, 16, 100, 4, "#5B6470", q)
    M.line(c, cx - 60, yb - 420, cx - 30, yb - 420, TINTA, q, 5)
    M.line(c, cx + 60, yb - 420, cx + 30, yb - 420, TINTA, q, 5)
    lampada(c, cx, yb - 470, 58, acesa, q)
    for k in range(n_ion):
        x = cx - 110 + (k * 53 % 220) + 10 * math.sin(t * 2 + k)
        y = yb - 40 - (k * 37 % 140) + 6 * math.cos(t * 2.4 + k)
        ion(c, x, y, 17, "H" if k % 2 == 0 else "Cl", "+" if k % 2 == 0 else "-", a_ion * q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("ácido clorídrico", "i", 84) + [("puro", "g", 80, COR)], XE, 260, passo=0.14)
        E.frase(c, t, C["s01.b"], [("não", "g", 74, ERRADO)] + ps("conduz eletricidade", "i", 78), XE, 380, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("na água:", "i", 78, TINTA2) + [("acende", "g", 74, COR)], XE, 620, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("o que a água fez com ele?", "i", 74), XE, 860, passo=0.12)
        ac = ep(t, C["s01.c"] + 0.8, 0.5)
        teste_lampada(c, t, C["s01.a"], 1450, 960, lambda tt: E.mix("#EEF2EE", Q.AGUA, ep(tt, C["s01.c"], 0.6)), ac, 8 if t >= C["s01.c"] else 0,
                      ep(t, C["s01.c"] + 0.4, 0.5))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("reconhecer", "g", 70), ("um", "i", 74), ("ácido", "g", 70, COR)]),
                              (C["s02.b"], [("o", "i", 74), ("que", "i", 74), ("acontece", "g", 70), ("na", "i", 74), ("água", "g", 70)]),
                              (C["s02.c"], [("dar", "i", 74), ("nome", "g", 70, COR)]),
                              (C["s02.d"], [("forte", "g", 70, COR), ("ou", "i", 74), ("fraco", "g", 70)])], y0=440, dy=150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre de duas coisas", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("íon", "g", 90, COR), ("=", "g", 90, TINTA2)] + ps("átomo com carga", "i", 90), XE, 380, passo=0.14)
    ion_em(c, t, C["s03.a"] + 1.2, XE + 120, 560, 70, "Na", "+")
    E.foco(c, t, C["s03.a"] + 1.4, 0.4, lambda a: E.escreve(c, "perdeu elétron", XE + 240, 580, 56, "i", TINTA, a))
    ion_em(c, t, C["s03.a"] + 2.4, XE + 820, 560, 70, "Cl", "-")
    E.foco(c, t, C["s03.a"] + 2.6, 0.4, lambda a: E.escreve(c, "ganhou elétron", XE + 940, 580, 56, "i", TINTA, a))
    E.frase(c, t, C["s03.b"], ps("conduz eletricidade", "i", 70) + [("=", "g", 66, TINTA2)] + [("íons soltos", "g", 66, COR)] + ps("que andam", "i", 70), XE, 820, passo=0.12)
    for k in range(6):
        x = XE + 300 + ((t - C["s03.b"]) * 120 + k * 200) % 1200
        if t >= C["s03.b"] + 0.5:
            ion(c, x, 940, 26, "Na" if k % 2 else "Cl", "+" if k % 2 else "-", ep(t, C["s03.b"] + 0.5, 0.4))


# ---------------- ionização ----------------
def b_ionizacao(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("o ácido clorídrico", "i", 76, TINTA2), XE, 200, passo=0.12)
        Q.formula_em(c, t, C["s04.a"], "HCl", XE, 420, 200)
        Q.lewis(c, t, C["s04.b"], [("H", -1.0, 0, []), ("Cl", 0.4, 0, [90, 0, 270])], [(0, 1, 1)], 1400, 400, escala=170, size=110, pontos=True)
        E.frase(c, t, C["s04.b"] + 0.6, ps("um par de elétrons", "i", 64) + [("dividido", "g", 60, COR)], 1400, 600, "center", 0.1)
        pilula_em(c, t, C["s04.b"] + 1.4, "ligação covalente", 1400, 690, 46, TINTA)
        E.frase(c, t, C["s04.c"], [("sem", "g", 80, ERRADO), ("íons", "g", 80)], XE, 620, passo=0.14)
        E.frase(c, t, C["s04.c"] + 1.0, ps("puro, não conduz", "i", 70, TINTA2), XE, 730, passo=0.12)
        E.foco(c, t, C["s04.c"] + 1.2, 0.5, lambda a: lampada(c, XE + 120, 900, 60, 0, a))
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05"], ps("na água, a molécula se parte", "i", 76), XE, 200, passo=0.12)
        sep = ease_io(prog(t, C["s05.a"], 1.4))
        xh, xc = lerp(860, 560, sep), lerp(1060, 1360, sep)
        Q.atomo_em(c, t, C["s05"], xc, 520, 110, "Cl")
        if sep < 0.6:
            M.line(c, xh + 50, 520, xc - 100, 520, Q.LIGA, 1 - sep / 0.6, 14)
        # o par de elétrons vai com o cloro
        for dy in (-18, 18):
            c.drawCircle(lerp(960, xc - 135, sep), 520 + dy, 12, M.paint(Q.ELETRON, ep(t, C["s05"], 0.4)))
        Q.atomo_em(c, t, C["s05"], xh, 520, 70, "H")
        if t >= C["s05.b"]:
            selo_carga(c, xc + 90, 430, 34, "-", ep(t, C["s05.b"], 0.4))
            E.foco(c, t, C["s05.b"] + 0.2, 0.4, lambda a: (Q.formula(c, "Cl^-", xc, 760, 110, TINTA, a, "center"),
                                                          centro(c, "cloreto", xc, 840, 52, "i", TINTA2, a)))
        if t >= C["s05.c"]:
            selo_carga(c, xh + 58, 462, 30, "+", ep(t, C["s05.c"], 0.4))
            E.foco(c, t, C["s05.c"] + 0.2, 0.4, lambda a: (Q.formula(c, "H^+", xh, 760, 110, TINTA, a, "center"),
                                                          centro(c, "sem elétron", xh, 840, 52, "i", TINTA2, a)))
        pilula_em(c, t, C["s05.d"], "H⁺ = só um próton", xh, 950, 50, E.COR)
        return
    if t < C["s07"]:
        cs = Q.equacao(c, t, C["s06.a"], "HCl -> H^+ + Cl^-", W / 2, 330, 160, tl=[C["s06.a"], C["s06.b"] - 0.3, C["s06.b"], C["s06.c"] - 0.2, C["s06.c"]])
        E.foco(c, t, C["s06.a"] + 0.6, 0.4, lambda a: centro(c, "na água", (cs[0] + cs[1]) / 2 + 40, 190, 50, "i", COR, a))
        E.frase(c, t, C["s06.d"], ps("os íons nascem na água:", "i", 66), XE, 560, passo=0.12)
        E.frase(c, t, C["s06.e"], [("ionização", "g", 110, COR)], XE, 700)
        teste_lampada(c, t, C["s06.d"], 1480, 1000, Q.AGUA, ep(t, C["s06.e"] + 1.2, 0.5), 10)
        return
    # s07: o hidrônio
    E.frase(c, t, C["s07.a"], ps("o", "i", 76) + [("H⁺", "g", 72, COR)] + ps("se prende a uma água", "i", 76), XE, 200, passo=0.12)
    cs = Q.equacao(c, t, C["s07.a"] + 0.6, "H^+ + H2O -> H3O^+", W / 2, 470, 150, passo=0.35)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: centro(c, "hidrônio", cs[2], 600, 60, "g", COR, a))
    Q.molecula(c, t, C["s07.a"] + 1.0, "H2O", cs[1], 760, 90, passo=0.1)
    E.frase(c, t, C["s07.c"], ps("nas provas:", "i", 60, TINTA2), XE, 960, passo=0.1)
    Q.formula_em(c, t, C["s07.c"] + 0.4, "H^+", XE + 400, 960, 80, cores={"H": E.COR})
    E.foco(c, t, C["s07.c"] + 0.7, 0.4, lambda a: E.escreve(c, "ou", XE + 570, 960, 66, "i", TINTA2, a))
    Q.formula_em(c, t, C["s07.c"] + 0.9, "H3O^+", XE + 680, 960, 80, cores={"H": E.COR})
    E.foco(c, t, C["s07.c"] + 1.3, 0.5, lambda a: E.selo(c, XE + 1000, 935, 42, True, a))


# ---------------- definição ----------------
def b_definicao(c, t, C, b):
    E.frase(c, t, C["s08"], ps("o químico sueco", "i", 66, TINTA2) + [("Arrhenius", "g", 66)], XE, 190, passo=0.12)
    E.frase(c, t, C["s08.a"], [("ácido", "g", 100, COR)] + ps("na água, solta", "i", 84) + [("H⁺", "g", 100, COR)], XE, 340, passo=0.14)
    E.frase(c, t, C["s08.a"] + 1.6, ps("como único íon positivo", "i", 64, TINTA2), XE, 430, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("na fórmula, o", "i", 66) + [("H", "g", 66, COR)] + ps("vem na frente", "i", 66), XE, 580, passo=0.12)
    for i, (k, f) in enumerate((("s08.c", "HCl"), ("s08.d", "H2SO4"), ("s08.e", "HNO3"))):
        Q.formula_em(c, t, C[k], f, XE + 20 + i * 520, 780, 130, cores={0: E.COR})
    if t >= C["s08.e"] + 1.0:
        Q.formula_em(c, t, C["s08.e"] + 1.0, "H2O", XE + 20, 990, 90)
        E.foco(c, t, C["s08.e"] + 1.4, 0.4, lambda a: E.escreve(c, "quase não solta íons: não é ácido", XE + 260, 980, 54, "i", TINTA2, a))


# ---------------- nomes ----------------
def palavra(c, t, t0, raiz, fim_, x, y, size):
    """palavra com a terminação na cor da matéria (ácido clor|ídrico)"""
    E.foco(c, t, t0, 0.45, lambda a: (E.escreve(c, "ácido", x, y, size * 1.05, "i", TINTA, a),
                                      E.escreve(c, raiz, x + E.larg("ácido ", "i", size * 1.05), y, size, "g", TINTA, a),
                                      E.escreve(c, fim_, x + E.larg("ácido ", "i", size * 1.05) + E.larg(raiz, "g", size), y, size, "g", COR, a)))


def b_nomes(c, t, C, b):
    E.frase(c, t, C["s09"], ps("os nomes", "i", 76, TINTA2), XE, 170, passo=0.12)
    E.frase(c, t, C["s09.a"], ps("sem oxigênio:", "i", 66), XE, 290, passo=0.12)
    E.frase(c, t, C["s09.a"] + 0.6, [("-ídrico", "g", 70, COR)], XE + 440, 290)
    Q.formula_em(c, t, C["s09.b"], "HCl", XE, 420, 96)
    palavra(c, t, C["s09.b"] + 0.3, "clor", "ídrico", XE + 240, 415, 62)
    pilula_em(c, t, C["s09.c"], "o ácido muriático", XE + 1110, 395, 44, TINTA2, "b")
    if t >= C["s10"]:
        E.frase(c, t, C["s10.a"], ps("com oxigênio, os comuns:", "i", 66), XE, 570, passo=0.12)
        E.frase(c, t, C["s10.a"] + 1.0, [("-ico", "g", 70, COR)], XE + 790, 570)
        for i, (k, f, raiz, extra) in enumerate((("s10.b", "H2SO4", "sulfúr", "bateria de carro"), ("s10.c", "HNO3", "nítr", None),
                                                 ("s10.d", "H2CO3", "carbôn", "refrigerante"))):
            y = 700 + i * 120
            Q.formula_em(c, t, C[k], f, XE, y, 90)
            palavra(c, t, C[k] + 0.3, raiz, "ico", XE + 340, y - 5, 58)
            if extra:
                pilula_em(c, t, C[k] + 1.2, extra, XE + 1110, y - 25, 40, TINTA2, "b")


# ---------------- força ----------------
def moleculas_ionizando(c, t, t0, x, y, w, frac, rotulo, cor):
    """dez moléculas de HA: as ionizadas viram dois íons separados"""
    for k in range(10):
        cx = x + (k % 5) * w / 5 + 40
        cy = y + (k // 5) * 130
        q = ep(t, t0 + 0.05 * k, 0.4)
        if q <= 0:
            continue
        sep = ease_io(prog(t, t0 + 0.6 + 0.08 * k, 0.8)) if k < frac else 0
        ion(c, cx - 22 - 12 * sep, cy, 20, "H", "+", q) if sep > 0.5 else Q.atomo(c, cx - 22 - 12 * sep, cy, 20, "H", q)
        ion(c, cx + 22 + 12 * sep, cy, 28, "Cl", "-", q) if sep > 0.5 else Q.atomo(c, cx + 22 + 12 * sep, cy, 28, "Cl", q)
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: centro(c, rotulo, x + w / 2, y + 330, 62, "g", cor, a))


def b_forca(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11"], ps("e a força?", "i", 80, TINTA2), XE, 200, passo=0.12)
        E.frase(c, t, C["s11.a"], [("forte:", "g", 66, COR)] + ps("quase todas viram íons", "i", 66), XE, 330, passo=0.12)
        moleculas_ionizando(c, t, C["s11.a"] + 0.5, 140, 520, 760, 9, "forte", COR)
        E.frase(c, t, C["s11.b"], [("fraco:", "g", 66)] + ps("só umas poucas", "i", 66), 1040, 330, passo=0.12)
        moleculas_ionizando(c, t, C["s11.b"] + 0.4, 1040, 520, 760, 1, "fraco", TINTA2)
        return
    E.frase(c, t, C["s12"], ps("sem oxigênio, decore", "i", 76, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s12"] + 1.2, [("3", "g", 76, COR), ("fortes", "g", 76, COR)], XE + 760, 200, passo=0.12)
    for i, f in enumerate(("HCl", "HBr", "HI")):
        Q.formula_em(c, t, C["s12.a"] + 0.5 * i, f, XE + i * 420, 420, 150)
    pilula_em(c, t, C["s12.a"] + 1.6, "fortes", XE + 1400, 370, 56, E.COR)
    Q.formula_em(c, t, C["s12.b"], "HF", XE, 640, 120)
    pilula_em(c, t, C["s12.b"] + 0.4, "moderado", XE + 400, 600, 50, TINTA2)
    E.frase(c, t, C["s12.c"], ps("os outros:", "i", 70) + [("fracos", "g", 66)], XE, 860, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("mais", "i", 70) + [("H", "g", 66)] + [("=", "g", 66, TINTA2)] + ps("mais forte?", "i", 70), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s13.b"], "HNO3", 520, 520, 170, align="center", cores={0: E.COR})
    E.foco(c, t, C["s13.b"] + 0.5, 0.4, lambda a: centro(c, "1 H", 520, 640, 60, "g", TINTA2, a))
    pilula_em(c, t, C["s13.c"], "forte", 520, 740, 60, E.COR)
    Q.formula_em(c, t, C["s13.d"], "H2CO3", 1400, 520, 170, align="center", cores={0: E.COR})
    E.foco(c, t, C["s13.d"] + 0.5, 0.4, lambda a: centro(c, "2 H", 1400, 640, 60, "g", TINTA2, a))
    pilula_em(c, t, C["s13.e"], "fraco", 1400, 740, 60, TINTA2)
    if t >= C["s13.e"] + 0.8:
        E.frase(c, t, C["s13.e"] + 0.8, ps("o número de H não decide", "i", 66), W / 2, 950, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        palco_titulo(c, t, C["s14"], "o atalho de prova")
        E.frase(c, t, C["s14.a"], [("O", "g", 90, BR), ("−", "g", 90, CLARO), ("H", "g", 90, BR)], 420, 380, "center", 0.2)
        E.foco(c, t, C["s14.a"] + 0.8, 0.4, lambda a: centro(c, "oxigênios menos hidrogênios", 420, 460, 46, "i", CLARO, a))
        for i, (k, s, rot, cor) in enumerate((("s14.b", "≥ 2", "forte", E.COR), ("s14.c", "1", "moderado", "#6E6E76"), ("s14.d", "0", "fraco", "#3A3B42"))):
            y = 610 + i * 120
            E.foco(c, t, C[k], 0.4, lambda a, s=s, y=y: E.formula(c, s, 300, y, 80, "g", BR, a, "center"))
            pilula_em(c, t, C[k] + 0.2, rot, 560, y - 28, 50, cor)
        if t >= C["s15"]:
            for i, (k, f, conta, kk) in enumerate((("s15.a", "H2SO4", "4 − 2 = 2", "s15.b"), ("s15.c", "HNO3", "3 − 1 = 2", "s15.d"))):
                y = 420 + i * 300
                Q.formula_em(c, t, C[k], f, 1080, y, 130, escuro=True, cores={"O": E.CLARO})
                E.formula_em(c, t, C[k] + 0.6, conta, 1080, y + 120, 76, "g", CLARO)
                pilula_em(c, t, C[kk], "forte", 1660, y + 90, 50, E.COR)
        return
    palco_titulo(c, t, C["s16"], "funciona porque")
    E.frase(c, t, C["s16.a"], ps("oxigênios que sobram facilitam a saída do", "i", 62, CLARO) + [("H⁺", "g", 62, BR)], W / 2, 270, "center", 0.1)
    E.frase(c, t, C["s16.b"], [("exceção:", "g", 66, ERRADO)], W / 2, 430, "center")
    Q.formula_em(c, t, C["s16.b"] + 0.4, "H2CO3", W / 2, 600, 150, align="center", escuro=True)
    E.formula_em(c, t, C["s16.c"], "3 − 2 = 1", 560, 780, 76, "g", CLARO, "center")
    E.foco(c, t, C["s16.c"] + 0.6, 0.4, lambda a: E.escreve(c, "moderado?", 820, 780, 66, "i", CLARO, a))
    if t >= C["s16.c"] + 1.2:
        E.risco(c, 800, 790, 1120, 735, t, C["s16.c"] + 1.2, largura=8)
    pilula_em(c, t, C["s16.d"], "fraco: vira CO₂ + água", W / 2, 900, 50, E.COR)
    E.frase(c, t, C["s16.e"], ps("o gás do refrigerante", "i", 62, CLARO), W / 2, 1020, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        Q.formula_em(c, t, C["s17.a"], "H3PO4", 1500, 440, 140, align="center")
        Q.formula_em(c, t, C["s17.c"], "HBr", 1500, 720, 140, align="center")
    questao(c, t, C, "s17", [(C["s17.a"], ps("ácido fosfórico (refrigerante de cola)", "i", 58, TINTA2), 300),
                             (C["s17.b"], [("1", "g", 56, COR)] + ps("forte, moderado ou fraco?", "i", 60), 420),
                             (C["s17.c"], [("2", "g", 56, COR)] + ps("ionização do ácido bromídrico", "i", 60), 600),
                             (C["s17.d"], [("3", "g", 56, COR)] + ps("ele é forte ou fraco?", "i", 60), 720)], "s18", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.formula_em(c, t, C["s19"], "H3PO4", XE, 300, 130, cores={"O": E.COR} if t >= C["s19.b"] else None)
    E.frase(c, t, C["s19.a"], ps("tem oxigênio: atalho", "i", 60, TINTA2), XE + 520, 290, passo=0.1)
    E.formula_em(c, t, C["s19.b"], "4 − 3 = 1", XE, 430, 90, "g", TINTA2)
    pilula_em(c, t, C["s19.c"], "moderado", XE + 600, 400, 56, TINTA2)
    if t >= C["s20"]:
        cs = Q.equacao(c, t, C["s20.a"], "HBr -> H^+ + Br^-", W / 2, 690, 140, tl=[C["s20.a"], C["s20.b"] - 0.3, C["s20.b"], C["s20.c"] - 0.2, C["s20.c"]])
        E.foco(c, t, C["s20.c"] + 0.4, 0.4, lambda a: centro(c, "brometo", cs[2], 800, 52, "i", TINTA2, a))
        E.frase(c, t, C["s20.d"], ps("um dos três fortes sem oxigênio:", "i", 60), XE, 960, passo=0.1)
        bola_txt(c, t, C["s20.e"], "forte", 1560, 940, 110, 64, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        E.frase(c, t, C["s22.b"], ps("o que soltam na água", "i", 64, TINTA2), XE, 530, passo=0.1)
        Q.equacao(c, t, C["s22.b"] + 0.4, "NaOH -> Na^+ + OH^-", 700, 820, 110, passo=0.3)
    fim(c, t, C, "s21", [("s21.a", [("ácido", "g", 66, COR), ("solta", "i", 72), ("H⁺", "g", 66), ("na", "i", 72), ("água", "i", 72)]),
                         ("s21.b", [("ídrico", "g", 66), ("sem", "i", 72), ("O,", "g", 66), ("ico", "g", 66), ("com", "i", 72), ("O", "g", 66)]),
                         ("s21.c", [("força:", "g", 66, COR), ("O", "g", 66), ("−", "g", 66, TINTA2), ("H", "g", 66)])],
        "s22", "Bases", None, "s22.c", "s22.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ionizacao=b_ionizacao, definicao=b_definicao, nomes=b_nomes, forca=b_forca,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
