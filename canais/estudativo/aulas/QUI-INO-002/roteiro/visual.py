"""Visual — Estudativo · QUI-INO-002: bases (dissociação, nomes e força).
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007). O hidróxido OH⁻ é uma esfera de grupo
vermelho-escura com "OH" dentro e o selo azul de carga (ion(..., cor=OHC)): ele anda sempre inteiro.
Peça nova: rede iônica que se desfaz na água (rede)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-002_bases_dissociacao_nomes_forca.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('hidroxido', 'nomes', 'forca', 'atalho', 'questao', 'fim'))
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
assert Q.contar("Ca(OH)2") == {"Ca": 1, "O": 2, "H": 2}
assert Q.lados("NaOH -> Na^+ + OH^-")[0] == Q.lados("NaOH -> Na^+ + OH^-")[1]
assert Q.lados("Ca(OH)2 -> Ca^2+ + 2 OH^-")[0] == Q.lados("Ca(OH)2 -> Ca^2+ + 2 OH^-")[1]
assert Q.lados("Ba(OH)2 -> Ba^2+ + 2 OH^-")[0] == Q.lados("Ba(OH)2 -> Ba^2+ + 2 OH^-")[1]


def rede(c, t, t0, cx, cy, sep, n=4, r=34, metal="Na", carga="+"):
    """composto iônico: grade de metal e OH⁻ alternados; sep = 0..1 espalha os íons pela água"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    for i in range(n):
        for j in range(n):
            x0, y0 = cx + (i - (n - 1) / 2) * r * 2.3, cy + (j - (n - 1) / 2) * r * 2.3
            k = i * n + j
            ang = k * 2.4
            x = x0 + sep * (math.cos(ang) * 260 + 40 * math.sin(t * 1.5 + k))
            y = y0 + sep * (math.sin(ang) * 150 + 30 * math.cos(t * 1.3 + k))
            if (i + j) % 2 == 0:
                ion(c, x, y, r, metal, carga, q)
            else:
                ion(c, x, y, r * 0.9, "OH", "-", q, cor=OHC)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a soda cáustica", "i", 88), XE, 260, passo=0.14)
        E.frase(c, t, C["s01.a"] + 0.9, [("desentope", "g", 84, COR)] + ps("a pia", "i", 88), XE, 380, passo=0.14)
        E.frase(c, t, C["s01.b"], ps("dissolve gordura e cabelo", "i", 66, TINTA2), XE, 480, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("na água, ela solta", "i", 70), XE, 680, passo=0.12)
        ion_em(c, t, C["s01.c"] + 1.0, XE + 680, 655, 62, "OH", "-", cor=OHC)
        E.frase(c, t, C["s01.d"], ps("é o íon que faz uma", "i", 70) + [("base", "g", 70, COR)], XE, 880, passo=0.12)
        Q.molecula(c, t, C["s01.c"] + 0.6, dict(atomos=[("O", 0, 0), ("H", 1.0, -0.2)], ligacoes=[(0, 1, 1)]), 1500, 560, 150, passo=0.2)
        if t >= C["s01.c"] + 1.4:
            selo_carga(c, 1560, 430, 40, "-", ep(t, C["s01.c"] + 1.4, 0.4))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("o", "i", 74), ("que", "i", 74), ("a", "i", 74), ("base", "g", 70, COR), ("faz", "i", 74), ("na", "i", 74), ("água", "g", 70)]),
                              (C["s02.b"], [("dar", "i", 74), ("nome", "g", 70, COR)]),
                              (C["s02.c"], [("forte", "g", 70, COR), ("pela", "i", 74), ("família", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre da", "i", 80, TINTA2) + [("ligação iônica", "g", 76)], XE, 200, passo=0.12)
    for i, (k, el, carga, txt) in enumerate((("s03.a", "Na", "+", "família 1: perde 1 elétron"), ("s03.b", "Ca", "2+", "família 2: perde 2 elétrons"))):
        y = 390 + i * 200
        ion_em(c, t, C[k], XE + 80, y - 30, 66, el, carga)
        Q.formula_em(c, t, C[k] + 0.2, f"{el}^{carga}", XE + 200, y + 10, 100)
        E.frase(c, t, C[k] + 0.4, ps(txt, "i", 64, TINTA2), XE + 460, y, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("composto iônico: os íons", "i", 62) + [("já existem", "g", 58, COR)], XE, 880, passo=0.1)
    rede(c, t, C["s03.c"] + 0.4, 1550, 860, 0, n=3, r=28, metal="Na")


# ---------------- hidróxido ----------------
def b_hidroxido(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("um íon diferente", "i", 80, TINTA2), XE, 200, passo=0.12)
        Q.molecula(c, t, C["s04.a"], dict(atomos=[("O", 0, 0), ("H", 1.0, -0.2)], ligacoes=[(0, 1, 1)]), 1400, 480, 190, passo=0.3)
        E.frase(c, t, C["s04.a"], ps("um oxigênio preso a um hidrogênio", "i", 62), XE, 340, passo=0.1)
        E.frase(c, t, C["s04.b"], [("+ 1", "g", 62, Q.ELETRON)] + ps("elétron", "i", 62), XE, 440, passo=0.12)
        if t >= C["s04.b"]:
            E.foco(c, t, C["s04.b"], 0.4, lambda a: c.drawCircle(1290, 400, 16, M.paint(Q.ELETRON, a)))
            selo_carga(c, 1520, 330, 44, "-", ep(t, C["s04.b"] + 0.5, 0.4))
        Q.formula_em(c, t, C["s04.c"], "OH^-", XE, 680, 180, cores={"carga": Q.ELETRON})
        E.frase(c, t, C["s04.c"] + 0.4, [("hidróxido", "g", 80, COR)], XE + 420, 660)
        pilula_em(c, t, C["s04.d"], "dois átomos que andam sempre juntos", W / 2, 900, 48, TINTA)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05"], ps("a soda cáustica", "i", 76, TINTA2), XE, 180, passo=0.12)
        Q.formula_em(c, t, C["s05.a"], "NaOH", XE, 340, 130)
        E.frase(c, t, C["s05.b"], ps("íons", "i", 62) + [("Na⁺", "g", 58)] + ps("e", "i", 62) + [("OH⁻", "g", 58, COR)] + ps("presos", "i", 62), XE + 420, 320, passo=0.12)
        sep = ease_io(prog(t, C["s05.c"] + 0.4, 1.6))
        Q.bequer(c, t, C["s05.c"], 1480, 900, 560, 460, 0.78, Q.AGUA)
        rede(c, t, C["s05.a"] + 0.4, 1480, 760, sep * 0.42, n=4, r=26)
        E.frase(c, t, C["s05.c"], ps("na água, só se", "i", 66) + [("separam", "g", 62, COR)], XE, 540, passo=0.12)
        Q.equacao(c, t, C["s05.d"], "NaOH -> Na^+ + OH^-", XE, 800, 96, align="left", tl=[C["s05.d"], C["s05.d"] + 0.5, C["s05.d"] + 0.9, C["s05.e"] - 0.2, C["s05.e"]])
        return
    E.frase(c, t, C["s06"], ps("separar íons que já existiam:", "i", 66, TINTA2), XE, 200, passo=0.1)
    E.frase(c, t, C["s06.a"], [("dissociação", "g", 110, COR)], XE, 340)
    E.frase(c, t, C["s06.b"], ps("Arrhenius:", "i", 62, TINTA2) + [("base", "g", 74, COR)] + ps("na água solta", "i", 70), XE, 520, passo=0.12)
    Q.formula_em(c, t, C["s06.b"] + 1.4, "OH^-", XE + 1000, 525, 90, cores={"carga": Q.ELETRON})
    E.frase(c, t, C["s06.b"] + 1.8, ps("como único íon negativo", "i", 60, TINTA2), XE, 610, passo=0.1)
    for i, f in enumerate(("NaOH", "KOH", "Ca(OH)2")):
        Q.formula_em(c, t, C["s06.c"] + 0.4 * i, f, XE + 20 + i * 470, 850, 120, cores={"OH": E.COR} if False else None)
    E.foco(c, t, C["s06.c"] + 1.4, 0.4, lambda a: centro(c, "o OH vem no fim, depois do metal", W / 2, 990, 52, "i", TINTA2, a))


# ---------------- nomes ----------------
def b_nomes(c, t, C, b):
    E.frase(c, t, C["s07"], ps("o nome é fácil", "i", 76, TINTA2), XE, 180, passo=0.12)
    E.frase(c, t, C["s07.a"], [("hidróxido de", "g", 90, COR)] + ps("+ metal", "i", 90), XE, 330, passo=0.14)
    for i, (k, f, nome) in enumerate((("s07.b", "NaOH", "hidróxido de sódio"), ("s07.c", "KOH", "hidróxido de potássio"))):
        y = 500 + i * 140
        Q.formula_em(c, t, C[k], f, XE, y, 100)
        E.frase(c, t, C[k] + 0.3, ps(nome, "i", 70), XE + 380, y - 5, passo=0.1)
    E.frase(c, t, C["s07.d"], ps("carga variável:", "i", 62, TINTA2) + [("algarismo romano", "g", 58, COR)], XE, 830, passo=0.1)
    for i, (f, nome) in enumerate((("Fe(OH)2", "hidróxido de ferro II"), ("Fe(OH)3", "hidróxido de ferro III"))):
        x = XE + i * 860
        Q.formula_em(c, t, C["s07.d"] + 1.2 + 0.4 * i, f, x, 960, 80)
        E.foco(c, t, C["s07.d"] + 1.5 + 0.4 * i, 0.4, lambda a, x=x, nome=nome: E.escreve(c, nome, x + 345, 955, 48, "i", TINTA2, a))


# ---------------- parênteses ----------------
def b_parenteses(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08"], ps("e com carga", "i", 76, TINTA2) + [("2+", "g", 72, COR)] + ps("?", "i", 76, TINTA2), XE, 200, passo=0.12)
        ion_em(c, t, C["s08.a"], 560, 520, 90, "Ca", "2+")
        ion_em(c, t, C["s08.a"] + 0.8, 330, 520, 60, "OH", "-", cor=OHC)
        ion_em(c, t, C["s08.a"] + 1.1, 790, 520, 60, "OH", "-", cor=OHC)
        E.formula_em(c, t, C["s08.a"] + 1.6, "+2 − 1 − 1 = 0", 560, 720, 70, "g", TINTA2, "center")
        Q.formula_em(c, t, C["s08.b"], "Ca(OH)2", 1380, 560, 170, align="center")
        G = Q.grupos("Ca(OH)2", 1380, 560, 170, "center")
        par = [g for g in G if g["tipo"] == "par"]
        if par and t >= C["s08.b"] + 0.8:
            g = par[0]
            caixa(c, t, C["s08.b"] + 0.8, g["x0"] - 10, g["topo"] - 14, G[-1]["x1"] - g["x0"] + 40, g["base"] - g["topo"] + 40, E.COR)
        E.foco(c, t, C["s08.b"] + 1.2, 0.4, lambda a: centro(c, "o OH entre parênteses, o 2 fora", 1380, 720, 48, "i", TINTA2, a))
        return
    Q.formula_em(c, t, C["s09"], "Ca(OH)2", W / 2, 300, 170, align="center", cores={"indice": E.COR} if t >= C["s09.a"] else None)
    E.frase(c, t, C["s09.a"], ps("o índice fora vale para o", "i", 64) + [("grupo inteiro", "g", 60, COR)], W / 2, 440, "center", 0.1)
    Q.inventario(c, t, C["s09.b"], [("O", 2), ("H", 2), ("Ca", 1)], XE + 40, 600, 60, tl=[C["s09.b"], C["s09.b"] + 0.5, C["s09.c"]])
    Q.equacao(c, t, C["s09.d"], "Ca(OH)2 -> Ca^2+ + 2 OH^-", W / 2, 940, 100, tl=[C["s09.d"], C["s09.d"] + 0.4, C["s09.d"] + 0.8, C["s09.e"] - 0.2, C["s09.e"]],
              cores={"coef": E.COR})
    ion_em(c, t, C["s09.d"] + 0.9, 1100, 680, 64, "Ca", "2+")
    ion_em(c, t, C["s09.e"] + 0.2, 1400, 680, 50, "OH", "-", cor=OHC)
    ion_em(c, t, C["s09.e"] + 0.4, 1560, 680, 50, "OH", "-", cor=OHC)


# ---------------- força ----------------
def b_forca(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10"], ps("e a força?", "i", 76, TINTA2), XE, 180, passo=0.12)
        E.frase(c, t, C["s10.a"], [("forte", "g", 66, COR)] + [("=", "g", 60, TINTA2)] + ps("se dissocia quase toda", "i", 64), XE, 290, passo=0.1)
        P = Q.tabela(c, t, C["s10.a"] + 0.8, 560, 680, 46, numeros=False, d=1.0, familia=1 if C["s10.b"] <= t < C["s10.c"] else None)
        if t >= C["s10.c"]:
            for s in ("Be", "Mg", "Ca", "Sr", "Ba", "Ra", "Li", "Na", "K", "Rb", "Cs", "Fr"):
                x, y = P(s)
                M.rrect(c, x - 22, y - 22, 44, 44, 6, E.COR, 0.85 * ep(t, C["s10.c"], 0.4))
        E.frase(c, t, C["s10.b"], [("família 1", "g", 62, COR)] + ps("(alcalinos): forte", "i", 64), XE, 410, passo=0.1)
        E.frase(c, t, C["s10.c"], [("família 2", "g", 62, COR)] + ps("(alcalinoterrosos): forte", "i", 64), XE, 510, passo=0.1)
        E.frase(c, t, C["s10.d"], ps("outros metais:", "i", 64) + [("fracas", "g", 60)], XE, 610, passo=0.1)
        return
    E.frase(c, t, C["s11"], ps("guarde uma", "i", 76, TINTA2) + [("exceção", "g", 72, ERRADO)], XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s11.a"], "Mg(OH)2", XE, 420, 160)
    E.frase(c, t, C["s11.a"] + 0.5, ps("família 2, mas", "i", 62, TINTA2), XE, 530, passo=0.1)
    pilula_em(c, t, C["s11.b"], "fraca e quase insolúvel", XE + 760, 515, 46, TINTA2)
    E.frase(c, t, C["s11.c"], ps("é o", "i", 66) + [("leite de magnésia", "g", 62, COR)], XE, 700, passo=0.12)
    E.frase(c, t, C["s11.d"], ps("a soda, forte, feriria a boca", "i", 60, TINTA2), XE, 800, passo=0.1)
    E.foco(c, t, C["s11.d"] + 1.6, 0.4, lambda a: E.escreve(c, "o berílio também é exceção", XE, 920, 52, "i", TINTA2, a))
    # frasco de leite de magnésia
    def frasco(a):
        M.rrect(c, 1430, 360, 260, 520, 60, "#F4F4F2", a, shadow=True)
        M.rrect(c, 1500, 300, 120, 80, 14, "#2B6CB0", a)
        M.rrect(c, 1450, 520, 220, 200, 20, E.COR, a)
        centro(c, "Mg(OH)₂", 1560, 640, 44, "g", BR, a)
    E.foco(c, t, C["s11.c"] + 0.3, 0.5, frasco)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("desmontar o", "i", 74) + [("OH", "g", 70)], XE + 450, 190, passo=0.12)
    def errado():
        Q.formula_em(c, t, C["s12.b"], "NaOH -> Na^+ + O^2- + H^+", W / 2, 430, 110, align="center", cor=ERRADO)
        if t >= C["s12.c"] + 0.8:
            E.risco(c, 380, 450, 1540, 360, t, C["s12.c"] + 0.8, largura=10)
    E.saida(c, t, C["s12.d"] + 1.2, errado)
    E.frase(c, t, C["s12.d"], ps("o OH", "i", 70) + [("não se parte", "g", 66, COR)], W / 2, 600, "center", 0.12)
    Q.formula_em(c, t, C["s12.e"], "NaOH -> Na^+ + OH^-", W / 2, 800, 120, align="center")
    E.foco(c, t, C["s12.e"] + 0.5, 0.5, lambda a: E.selo(c, 1660, 760, 50, True, a))
    ion_em(c, t, C["s12.e"] + 0.8, W / 2 + 330, 950, 46, "OH", "-", cor=OHC)
    E.foco(c, t, C["s12.e"] + 1.0, 0.4, lambda a: E.escreve(c, "inteiro, uma carga negativa", W / 2 - 400, 965, 52, "i", TINTA2, a))


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        palco_titulo(c, t, C["s13"], "o atalho de prova")
        E.frase(c, t, C["s13.a"], ps("número de", "i", 70, CLARO) + [("OH", "g", 66, BR), ("=", "g", 66, CLARO), ("carga do metal", "g", 66, BR)], W / 2, 280, "center", 0.12)
        for i, (k, f, rot) in enumerate((("s13.b", "NaOH", "família 1: Na⁺"), ("s13.c", "Ca(OH)2", "família 2: Ca²⁺"), ("s13.d", "Al(OH)3", "família 13: Al³⁺"))):
            y = 480 + i * 190
            E.foco(c, t, C[k], 0.4, lambda a, rot=rot, y=y: E.escreve(c, rot, 300, y, 64, "b", CLARO, a))
            Q.formula_em(c, t, C[k] + 0.4, f, 1000, y + 10, 110, escuro=True, cores={"indice": E.CLARO})
        return
    palco_titulo(c, t, C["s14"], "funciona porque")
    E.frase(c, t, C["s14.a"], ps("cada", "i", 66, CLARO) + [("OH⁻", "g", 62, BR)] + ps("cancela uma carga positiva", "i", 66, CLARO), W / 2, 280, "center", 0.12)
    ion_em(c, t, C["s14.a"] + 0.6, 960, 450, 70, "Al", "3+", escuro=True)
    for k, dx in enumerate((-230, 0, 230)):
        ion_em(c, t, C["s14.a"] + 1.0 + 0.2 * k, 960 + dx, 600 if dx else 620, 40, "OH", "-", cor=OHC)
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("carga variável, como o ferro", "i", 66, CLARO), W / 2, 820, "center", 0.12)
    E.frase(c, t, C["s14.c"], ps("a carga vem no nome:", "i", 62, CLARO) + [("ferro III", "g", 58, BR)], W / 2, 920, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        Q.formula_em(c, t, C["s15.a"], "Ba(OH)2", 1500, 500, 160, align="center")
        E.foco(c, t, C["s15.b"], 0.4, lambda a: centro(c, "bário: família 2", 1500, 640, 56, "i", TINTA2, a))
    questao(c, t, C, "s15", [(C["s15.a"], ps("o hidróxido de bário", "i", 64), 330),
                             (C["s15.c"], [("1", "g", 56, COR)] + ps("o que ele produz na água?", "i", 60), 520),
                             (C["s15.d"], [("2", "g", 56, COR)] + ps("base forte ou fraca?", "i", 60), 640)], "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.formula_em(c, t, C["s17"], "Ba(OH)2", XE, 260, 130, cores={"indice": E.COR} if t >= C["s17.c"] else None)
    E.frase(c, t, C["s17.a"], ps("família 2:", "i", 64, TINTA2) + [("carga 2+", "g", 60, COR)], XE + 600, 250, passo=0.12)
    Q.equacao(c, t, C["s17.b"], "Ba(OH)2 -> Ba^2+ + 2 OH^-", W / 2, 500, 130, tl=[C["s17.b"] - 0.3, C["s17.b"] - 0.1, C["s17.b"], C["s17.d"] - 0.2, C["s17.d"]],
              cores={"coef": E.COR})
    E.frase(c, t, C["s17.c"], ps("o 2 fora dos parênteses:", "i", 60, TINTA2) + [("2 hidróxidos", "g", 56)], W / 2, 660, "center", 0.1)
    E.frase(c, t, C["s17.e"], ps("não é magnésio nem berílio:", "i", 62), XE + 100, 900, passo=0.1)
    bola_txt(c, t, C["s17.f"], "forte", 1500, 880, 110, 64, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        E.frase(c, t, C["s19.b"], [("ácido", "g", 64), ("+", "g", 64, TINTA2), ("base", "g", 64), ("→", "g", 64, COR), ("sal", "g", 64, COR), ("+", "g", 64, TINTA2), ("água", "g", 64)], XE, 560, passo=0.12)
        Q.equacao(c, t, C["s19.a"], "H^+ + OH^- -> H2O", 600, 820, 110, passo=0.3)
    fim(c, t, C, "s18", [("s18.a", [("base", "g", 66, COR), ("solta", "i", 72), ("OH⁻", "g", 66), ("na", "i", 72), ("água", "i", 72)]),
                         ("s18.b", [("hidróxido", "g", 66), ("de", "i", 72), ("+", "g", 66, TINTA2), ("metal", "i", 72)]),
                         ("s18.c", [("famílias", "i", 72), ("1", "g", 66, COR), ("e", "i", 72), ("2:", "g", 66, COR), ("fortes", "g", 66), ("(menos", "i", 72), ("Mg", "g", 66), ("e", "i", 72), ("Be)", "g", 66)])],
        "s19", "Neutralização", None, "s19.c", "s19.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, hidroxido=b_hidroxido, nomes=b_nomes, parenteses=b_parenteses, forca=b_forca,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
