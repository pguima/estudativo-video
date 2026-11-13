"""Visual — Estudativo · QUI-SOL-002: solubilidade e curvas de solubilidade.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a da trilha Soluções (cabeçalho de
QUI-SOL-001/roteiro/visual.py): soluto = bolinhas/grãos; corpo de fundo = grãos brancos empilhados no fundo; curva com Q.solubilidade
e as duas guias tracejadas da leitura; valor lido na pílula turquesa. Todo instante vem de C[...]."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Soluções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-SOL-002_solubilidade_curvas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("limite", "curva", "gas", "atalho", "questao", "fim"))
BR = "#FFFFFF"
SAL = "#FFFFFF"

KNO3 = [(0, 13), (10, 21), (20, 32), (30, 46), (40, 64), (50, 85), (60, 110), (70, 138), (80, 169)]
NACL = [(0, 35.7), (20, 36), (40, 36.6), (60, 37.3), (80, 38.4)]
S = dict(KNO3)
# as contas da aula
assert 50 - 36 == 14 and 80 - S[40] == 16
assert S[40] / 2 == 32 and 40 - 32 == 8
assert 100 < S[60] and 100 - S[40] == 36


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


def rotulo(c, t, t0, s, cx, y, size=48, cor=TINTA2):
    E.foco(c, t, t0, 0.4, lambda a: centro(c, s, cx, y, size, "i", cor, a))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def fundo_sal(c, t, t0, cx, yb, w, n, r=10, a=1.0, semente=2):
    """corpo de fundo: grãos brancos que caem e se empilham no fundo do béquer"""
    if t < t0:
        return
    rnd = random.Random(semente)
    por = max(1, int((w - 30) / (2.05 * r)))
    for i in range(n):
        ti = t0 + 0.02 * i
        u = ease_out(prog(t, ti, 0.6))
        if u <= 0:
            continue
        fx = cx - (w - 30) / 2 + r + (i % por) * 2.05 * r + (r if (i // por) % 2 else 0) * 0.5
        fy = yb - 10 - r - (i // por) * 1.75 * r
        y = lerp(yb - 240 - rnd.random() * 60, fy, u)
        c.drawCircle(fx, y, r, M.paint(SAL, a))
        c.drawCircle(fx, y, r, M.paint("#B9BCC2", 0.8 * a, stroke=1.5))


def dissolvido(c, t, t0, cx, yb, w, h, n, a=1.0, semente=4, nivel=0.7):
    """soluto dissolvido: pontinhos turquesa espalhados no líquido"""
    if t < t0:
        return
    q = ep(t, t0, 0.8) * a
    rnd = random.Random(semente)
    for i in range(n):
        x = cx - w / 2 + 20 + rnd.random() * (w - 40)
        y = yb - 20 - rnd.random() * (h * nivel - 40)
        ph = rnd.random() * 6.3
        c.drawCircle(x + 3 * math.sin(t * 1.2 + ph), y + 3 * math.cos(t + ph), 3.2, M.paint(E.COR, 0.85 * q))


def guias(c, t, t0, P, x, y, cor=None, d=0.5):
    """as duas guias de leitura: sobe da temperatura até a curva, depois anda até o eixo do lado"""
    cor = cor or E.COR
    p1, p2 = ease_io(prog(t, t0, d)), ease_io(prog(t, t0 + d, d))
    if p1 > 0:
        M.line(c, P.x(x), P.y(0), P.x(x), lerp(P.y(0), P.y(y), p1), cor, 1, 5, dash=[16, 12])
    if p2 > 0:
        M.line(c, P.x(x), P.y(y), lerp(P.x(x), P.x(0), p2), P.y(y), cor, 1, 5, dash=[16, 12])
    if p1 >= 1:
        c.drawCircle(P.x(x), P.y(y), 13, M.paint(cor))


def ponto(c, t, t0, P, x, y, cor, r=15):
    q = ease_back(prog(t, t0, 0.4))
    if q > 0:
        c.drawCircle(P.x(x), P.y(y), r * q, M.paint(cor))
        c.drawCircle(P.x(x), P.y(y), r * q, M.paint(BR, 1, stroke=3))


def curva(c, t, t0, x=200, y=230, w=820, h=640, sal=False, d=1.2):
    curvas = [dict(nome="KNO3", pts=KNO3, t=t0 + 0.6)]
    if sal:
        curvas.append(dict(nome="NaCl", pts=NACL, t=sal, cor=TINTA2))
    return Q.solubilidade(c, t, t0, x, y, w, h, curvas, tmax=80, smax=180, d=d, passo=20, passo_y=20, size=34)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cx, yb, w, h = 1360, 880, 440, 480
        Q.bequer(c, t, C["s01.a"], cx, yb, w, h, 0.7, Q.AGUA, graduacao=False)
        E.frase(c, t, C["s01.a"] + 0.2, [("50 g", "g", 80, COR), ("de", "i", 80), ("sal", "i", 80)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.4, [("100 g", "g", 80, COR), ("de", "i", 80), ("água", "i", 80)], XE, 420, passo=0.12)
        rotulo(c, t, C["s01.a"] + 2.4, "a 20 °C", XE + 90, 510, 56)
        dissolvido(c, t, C["s01.a"] + 1.2, cx, yb, w, h, 80)
        # colher mexendo
        if t >= C["s01.b"] - 0.2:
            q = ep(t, C["s01.b"] - 0.2, 0.4) * (1 - ep(t, C["s01.d"], 0.4))
            ang = 0.35 * math.sin(t * 6)
            c.save(); c.translate(cx, yb - h * 0.95); c.rotate(math.degrees(ang))
            M.rrect(c, -8, -40, 16, 380, 8, "#9AA0A8", q)
            c.restore()
            E.frase(c, t, C["s01.b"], ps("mexa um minuto, mexa uma hora", "i", 56, TINTA2), XE, 640, passo=0.1)
        fundo_sal(c, t, C["s01.c"] - 0.4, cx, yb, w, 38, 11)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (E.escreve(c, "14 g", XE, 820, 120, "g", COR, a), E.escreve(c, "no fundo", XE + 300, 815, 70, "i", TINTA, a)))
        pilula_em(c, t, C["s01.d"], "a água tem um limite", cx, 330, 54, E.COR)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("ler", "i", 74), ("o", "i", 74), ("limite", "g", 70, COR), ("no", "i", 74), ("gráfico", "i", 74)]),
                 (C["s02.c"], [("quanto", "i", 74), ("sobra", "g", 70, COR), ("no", "i", 74), ("fundo", "i", 74)]),
                 (C["s02.d"], [("o", "i", 74), ("refrigerante", "g", 70), ("quente", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre", "i", 76, TINTA2), XE, 170)
    E.frase(c, t, C["s03.a"], [("soluto", "g", 76, COR), ("=", "g", 70, TINTA2)] + ps("o que se dissolve", "i", 70), XE, 300, passo=0.12)
    E.frase(c, t, C["s03.b"], [("solvente", "g", 76, COR), ("=", "g", 70, TINTA2)] + ps("o que dissolve: a água", "i", 70), XE, 400, passo=0.12)
    E.serie(c, t, C["s03.c"], [("seg", 2), ("ter", 3), ("qua", 5), ("qui", 4), ("sex", 6)], XE, 560, 640, 330, vmin=0, vmax=7, valores=False, size=34)
    rotulo(c, t, C["s03.c"] + 0.6, "gráfico de linha", XE + 320, 1010, 48)
    E.frase(c, t, C["s03.d"], [("regra", "g", 70, COR), ("de", "i", 74), ("três", "g", 70, COR)], 1180, 620, passo=0.12)
    E.frase(c, t, C["s03.d"] + 1.0, [("dobra", "i", 70), ("um,", "i", 70), ("dobra", "i", 70), ("o", "i", 70), ("outro", "g", 66)], 1180, 730, passo=0.12)
    E.formula_em(c, t, C["s03.d"] + 2.0, "100 g → 36 g", 1180, 860, 64, "g", TINTA2)
    E.formula_em(c, t, C["s03.d"] + 2.6, "200 g → 72 g", 1180, 950, 64, "g", COR)


# ---------------- o limite ----------------
def b_limite(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("o máximo de soluto que se dissolve", "i", 66), XE, 230, passo=0.1)
            E.frase(c, t, C["s04.a"] + 1.8, ps("numa quantidade de água, numa temperatura", "i", 56, TINTA2), XE, 320, passo=0.08)
            E.frase(c, t, C["s04.b"], [("coeficiente", "g", 110, COR)], XE, 520)
            E.frase(c, t, C["s04.b"] + 0.5, [("de", "i", 110), ("solubilidade", "g", 110, COR)], XE, 660)
            E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "gramas em 100 g de água", XE + 360, 820, 56, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    cx, yb, w, h = 1400, 860, 420, 460
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("sal", "g", 70), ("de", "i", 74), ("cozinha,", "i", 74), ("20 °C", "g", 70, TINTA2)], XE, 220, passo=0.12)
            E.foco(c, t, C["s05.a"] + 1.2, 0.5, lambda a: (E.escreve(c, "36 g", XE, 400, 150, "g", COR, a),
                                                           E.escreve(c, "em 100 g de água", XE + 370, 390, 60, "i", TINTA, a)))
            Q.bequer(c, t, C["s05"], cx, yb, w, h, 0.7, Q.AGUA, graduacao=False)
            dissolvido(c, t, C["s05.b"], cx, yb, w, h, 80)
            E.frase(c, t, C["s05.b"], [("36", "g", 66, COR), ("dissolvem", "i", 70)], XE, 600, passo=0.12)
            fundo_sal(c, t, C["s05.c"] - 0.2, cx, yb, w, 38, 11)
            E.formula_em(c, t, C["s05.c"], "50 − 36 = 14 g", XE, 760, 90, "g", TINTA)
            rotulo(c, t, C["s05.c"] + 0.8, "ficam no fundo", XE + 280, 850, 54)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06"], ps("cada situação tem um nome", "i", 66, TINTA2), XE, 170, passo=0.1)
            xs = (380, 960, 1540)
            dados = ((C["s06.a"], "insaturada", "abaixo do limite", 40, 0), (C["s06.b"], "saturada", "no limite", 80, 0),
                     (C["s06.c"], "corpo de fundo", "passou do limite", 80, 30))
            for k, (ti, nome, sub, n, nf) in enumerate(dados):
                Q.bequer(c, t, ti, xs[k], 760, 300, 330, 0.72, Q.AGUA, graduacao=False)
                dissolvido(c, t, ti + 0.2, xs[k], 760, 300, 330, n, semente=6 + k)
                if nf:
                    fundo_sal(c, t, ti + 0.4, xs[k], 760, 300, nf, 10)
                E.frase(c, t, ti, [(nome, "g", 62, COR)], xs[k], 340, "center")
                rotulo(c, t, ti + 0.4, sub, xs[k], 840, 46, TINTA)
            pilula_em(c, t, C["s06.d"], "corpo de fundo = o sólido que ficou embaixo", 1300, 950, 40, E.COR, "b")
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    E.frase(c, t, C["s07.a"], ps("caso raro:", "i", 70, TINTA2), XE, 230)
    E.frase(c, t, C["s07.a"] + 0.6, [("supersaturada", "g", 110, COR)], XE, 380)
    E.frase(c, t, C["s07.a"] + 1.6, ps("mais que o limite, sem nada no fundo", "i", 60), XE, 480, passo=0.1)
    Q.bequer(c, t, C["s07"], cx, yb, w, h, 0.7, Q.AGUA, graduacao=False)
    cai = C["s07.b"] + 1.6
    dissolvido(c, t, C["s07"], cx, yb, w, h, int(130 - 50 * ep(t, cai, 0.6)))
    E.frase(c, t, C["s07.b"], [("instável", "g", 90, ERRADO)], XE, 680)
    # o grão que cai e dispara a cristalização
    u = prog(t, C["s07.b"] + 0.8, 0.8)
    if 0 < u < 1:
        c.drawCircle(cx, lerp(yb - h - 60, yb - 40, u * u), 11, M.paint(SAL))
    fundo_sal(c, t, cai, cx, yb, w, 40, 11)
    rotulo(c, t, cai + 0.4, "o excesso cai de uma vez", cx, yb + 80, 48)


# ---------------- a curva ----------------
def b_curva(c, t, C, b):
    t0 = C["s08.a"]
    tsal = C["s11.b"]
    P = curva(c, t, t0 - 0.2, sal=tsal)
    E.saida(c, t, C["s09"] - 0.1, lambda: E.frase(c, t, C["s08"], ps("o limite muda com a temperatura", "i", 56, TINTA2), 1190, 320, passo=0.1))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "temperatura", P.x(25), P.y(0) + 110, 42, "b", fundo=E.COR, a=a))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "gramas em 100 g de água", 880, 175, 40, "b", fundo=E.COR, a=a))
    E.frase(c, t, C["s09.a"], [("nitrato", "g", 58), ("de", "i", 62), ("potássio", "g", 58)], 1190, 320, passo=0.12)
    E.foco(c, t, C["s09.a"] + 0.8, 0.4, lambda a: Q.formula(c, "KNO3", 1190, 420, 70, COR, a))
    rotulo(c, t, C["s09.a"] + 1.2, "usado em adubo", 1530, 410, 44)
    if t >= C["s09.b"]:
        guias(c, t, C["s09.b"], P, 40, 64)
        E.frase(c, t, C["s09.b"], [("1", "g", 52, COR)] + ps("suba da temperatura", "i", 54), 1190, 520, passo=0.1)
        E.frase(c, t, C["s09.c"], [("2", "g", 52, COR)] + ps("ande até o eixo do lado", "i", 54), 1190, 600, passo=0.1)
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "64 g", P.x(0) - 90, P.y(64), 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "40 °C", P.x(40), P.y(0) + 50, 36, "g", fundo=TINTA, a=a))
    if C["s10"] <= t < C["s11"]:
        def s10():
            ponto(c, t, C["s10"] + 0.5, P, 40, 80, ERRADO)
            E.formula_em(c, t, C["s10"] + 0.3, "80 g a 40 °C", 1190, 730, 58, "g", TINTA)
            E.frase(c, t, C["s10.a"], [("80", "g", 58, ERRADO), (">", "g", 58, TINTA2), ("64", "g", 58, COR)], 1190, 820, passo=0.12)
            E.frase(c, t, C["s10.b"], ps("saturada com corpo de fundo", "i", 54), 1190, 900, passo=0.1)
            E.formula_em(c, t, C["s10.c"], "80 − 64 = 16 g no fundo", 1190, 990, 58, "g", COR)
            p = ep(t, C["s10.c"], 0.5)
            if p > 0:
                M.line(c, P.x(40) + 30, P.y(80), P.x(40) + 30, lerp(P.y(80), P.y(64), p), ERRADO, 1, 5)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t >= C["s11"]:
        E.frase(c, t, C["s11.a"], [("nitrato:", "g", 58), ("sobe", "i", 62), ("rápido", "g", 58, COR)], 1190, 760, passo=0.12)
        rotulo(c, t, C["s11.a"] + 1.0, "água quente dissolve muito mais", 1510, 840, 46, TINTA)
        E.frase(c, t, C["s11.b"] + 0.3, [("sal", "g", 58), ("de", "i", 62), ("cozinha:", "i", 62), ("quase", "i", 62), ("deitada", "g", 58, COR)], 1190, 960, passo=0.12)


# ---------------- gás ----------------
def bolhas(c, t, t0, cx, yb, w, h, n, vel=1.0, a=1.0, semente=3, nivel=0.72):
    """bolhas de gás subindo e escapando pela superfície"""
    if t < t0:
        return
    rnd = random.Random(semente)
    top = yb - h * nivel
    for i in range(n):
        x = cx - w / 2 + 24 + rnd.random() * (w - 48)
        per = 1.6 + rnd.random() * 1.2
        fase = rnd.random() * per
        u = (((t - t0) * vel + fase) % per) / per
        y = lerp(yb - 20, top - 60, u)
        r = 5 + 6 * u
        al = a * ep(t, t0, 0.5) * (1 if y > top else 1 - (top - y) / 60)
        if al > 0:
            c.drawCircle(x + 4 * math.sin(u * 9 + i), y, r, M.paint("#FFFFFF", 0.55 * al))
            c.drawCircle(x + 4 * math.sin(u * 9 + i), y, r, M.paint(TINTA2, 0.6 * al, stroke=2))


def termometro(c, x, y, h, nivel, cor, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - 14, y - h, 28, h, 14, "#FFFFFF", a, stroke=3, stroke_color=TINTA2)
    M.rrect(c, x - 7, y - 10 - (h - 30) * nivel, 14, (h - 30) * nivel + 10, 7, cor, a)
    c.drawCircle(x, y + 6, 24, M.paint(cor, a))
    c.drawCircle(x, y + 6, 24, M.paint(TINTA2, a, stroke=3))


def b_gas(c, t, C, b):
    E.frase(c, t, C["s12"], ps("com gás, é o", "i", 76) + [("contrário", "g", 76, COR)], XE, 200, passo=0.12)
    xs = (560, 1320)
    for k, (cor, nome, nb, nd, tn) in enumerate((("#CFE7F7", "gelado", 4, 110, 0.15), ("#F7E3CF", "quente", 22, 40, 0.85))):
        ti = C["s12.a"] + 0.3 * k
        Q.bequer(c, t, ti, xs[k], 850, 380, 420, 0.72, cor, graduacao=False)
        dissolvido(c, t, ti + 0.2, xs[k], 850, 380, 420, nd, semente=8 + k)
        bolhas(c, t, ti + 0.4, xs[k], 850, 380, 420, nb, 1.0 + k)
        E.foco(c, t, ti, 0.4, lambda a, k=k, tn=tn: termometro(c, xs[k] + 260, 820, 300, tn, "#2E86AB" if k == 0 else ERRADO, a))
        rotulo(c, t, ti + 0.3, nome, xs[k], 930, 54, TINTA)
    E.frase(c, t, C["s12.a"], ps("mais quente, menos gás dissolvido", "i", 60), XE, 300, passo=0.1)
    pilula_em(c, t, C["s12.b"], "gelada: quase o dobro de gás carbônico", W / 2, 1010, 44, E.COR, "b")
    if t >= C["s13"]:
        def s13():
            c.drawRect(skia.Rect.MakeWH(W, H), M.paint("#F4F2EC", ep(t, C["s13"], 0.4)))
            E.frase(c, t, C["s13.a"], ps("refrigerante quente", "i", 76) + [("perde o gás", "g", 72, COR)], XE, 240, passo=0.12)
            Q.bequer(c, t, C["s13.a"], 1320, 900, 380, 460, 0.75, "#5A2E1A", graduacao=False)
            bolhas(c, t, C["s13.b"], 1320, 900, 380, 460, 30, 1.8, nivel=0.75)
            E.frase(c, t, C["s13.a"] + 1.2, ps("o calor baixa o limite", "i", 64), XE, 400, passo=0.1)
            E.frase(c, t, C["s13.b"], ps("o gás que passou do limite", "i", 64), XE, 540, passo=0.1)
            E.frase(c, t, C["s13.b"] + 1.0, [("escapa", "g", 90, COR), ("em", "i", 80), ("bolhas", "i", 80)], XE, 660, passo=0.12)
            pilula_em(c, t, C["s13.c"], "gelado, segura o gás por mais tempo", XE + 450, 840, 46, TINTA, "b")
        s13()


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("o limite é para 100 g de água", "i", 64), XE + 440, 190, passo=0.1)
    cx, yb, w, h = 1540, 900, 360, 420
    Q.bequer(c, t, C["s14.b"], cx, yb, w, h, 0.4, Q.AGUA, graduacao=False)
    E.frase(c, t, C["s14.b"], [("40 g", "g", 70, COR), ("de", "i", 72), ("nitrato", "i", 72)], XE, 360, passo=0.12)
    E.frase(c, t, C["s14.b"] + 1.0, [("50 g", "g", 70, COR), ("de", "i", 72), ("água,", "i", 72), ("40 °C", "g", 66, TINTA2)], XE, 460, passo=0.12)
    rotulo(c, t, C["s14.b"] + 0.4, "50 g de água", cx, yb + 80, 48)

    def errado():
        E.frase(c, t, C["s14.c"], [("40", "g", 70, ERRADO), ("<", "g", 70, ERRADO), ("64", "g", 70, ERRADO), ("insaturada", "i", 72, ERRADO)], XE, 640, passo=0.12)
        if t >= C["s14.c"] + 1.6:
            E.risco(c, XE - 10, 655, XE + 720, 585, t, C["s14.c"] + 1.6, largura=12)
    E.saida(c, t, C["s15.a"] + 0.6, errado)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], ps("a água é a", "i", 70) + [("metade", "g", 66, COR)], XE, 640, passo=0.12)
    E.formula_em(c, t, C["s15.b"], "64 ÷ 2 = 32 g", XE, 760, 86, "g", TINTA)
    rotulo(c, t, C["s15.b"] + 0.8, "metade da água, metade do sal", XE + 300, 840, 46)
    E.frase(c, t, C["s15.c"], [("40", "g", 64, COR), (">", "g", 64, TINTA2), ("32", "g", 64, COR)], XE, 950, passo=0.12)
    fundo_sal(c, t, C["s15.d"] - 0.2, cx, yb, w, 22, 10)
    E.formula_em(c, t, C["s15.d"], "40 − 32 =", XE + 420, 950, 64, "g", TINTA2)
    bola_txt(c, t, C["s15.d"] + 0.5, "8 g", XE + 860, 928, 66, 56)
    E.foco(c, t, C["s15.d"] + 0.8, 0.4, lambda a: E.escreve(c, "no fundo", XE + 950, 950, 56, "i", TINTA, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    P = Q.solubilidade(c, t, C["s16"] - 0.3, 200, 230, 760, 620, [dict(nome="KNO3", pts=KNO3, t=C["s16"])], tmax=80, smax=180, d=0.8,
                       escuro=True, passo=20, passo_y=20, size=32)
    E.frase(c, t, C["s16.a"], ps("marque a solução como um", "i", 60, CLARO) + [("ponto", "g", 60, BR)], 1100, 230, passo=0.1)
    linhas = ((C["s16.b"], (40, 40), "#7FC8F8", "abaixo da linha:", "insaturada"),
              (C["s16.c"], (40, 64), E.CLARO, "sobre a linha:", "saturada"),
              (C["s16.d"], (40, 100), ERRADO, "acima da linha:", "sobra no fundo"))
    for k, (ti, (x, y), cor, l1, l2) in enumerate(linhas):
        ponto(c, t, ti, P, x + 8 * (k - 1), y, cor)
        yy = 380 + k * 140
        E.foco(c, t, ti, 0.4, lambda a, cor=cor, yy=yy: c.drawCircle(1120, yy - 18, 16, M.paint(cor, a)))
        E.frase(c, t, ti + 0.1, ps(l1, "i", 56, CLARO) + [(l2, "g", 54, BR)], 1160, yy, passo=0.1)
    p = ep(t, C["s16.d"] + 1.2, 0.5)
    if p > 0:
        M.line(c, P.x(40) + 40, P.y(100), P.x(40) + 40, lerp(P.y(100), P.y(64), p), ERRADO, 1, 5)
        E.foco(c, t, C["s16.d"] + 1.4, 0.4, lambda a: E.escreve(c, "sobra", P.x(40) - 140, P.y(82) + 12, 40, "b", ERRADO, a))
    if t >= C["s17"]:
        E.frase(c, t, C["s17.a"], ps("funciona porque", "i", 54, CLARO) + [("a curva é o limite", "g", 52, BR)], 1100, 820, passo=0.1)
        E.frase(c, t, C["s17.b"], [("não", "g", 50, ERRADO), ("compensa:", "i", 54, CLARO)] + ps("água ≠ 100 g", "b", 50, BR), 1100, 910, passo=0.1)
        E.frase(c, t, C["s17.b"] + 1.6, ps("passe antes para 100 g de água", "i", 52, CLARO), 1100, 990, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s18"] + 1.0, ps("curva do nitrato de potássio", "i", 56, TINTA2), XE, 260, passo=0.1)
    E.frase(c, t, C["s18.a"], [("100 g", "g", 62, COR)] + ps("de sal em", "i", 66) + [("100 g", "g", 62, COR)] + ps("de água,", "i", 66), XE, 380, passo=0.1)
    E.frase(c, t, C["s18.a"] + 1.6, ps("a", "i", 66) + [("60 °C", "g", 62)], XE, 460, passo=0.1)
    E.frase(c, t, C["s18.b"], [("1", "g", 56, COR)] + ps("a solução é saturada?", "i", 62), XE, 540, passo=0.1)
    E.frase(c, t, C["s18.c"], [("2", "g", 56, COR)] + ps("esfria até", "i", 62) + [("40 °C:", "g", 58)], XE, 660, passo=0.1)
    E.frase(c, t, C["s18.d"], ps("quantos gramas ficam no fundo?", "i", 62), XE + 60, 750, passo=0.1)
    if t < C["s19"]:
        P = Q.solubilidade(c, t, C["s18"] + 0.5, 1180, 300, 560, 500, [dict(nome="", pts=KNO3)], tmax=80, smax=180, d=0.8, passo=20, passo_y=40, size=28)
    else:
        E.relogio(c, t, C["s19.a"], cx=1470, cy=520, r=220)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    P = curva(c, t, C["s20"] - 0.3, x=200, y=230, w=820, h=640, d=0.6)
    guias(c, t, C["s20.a"], P, 60, 110)
    E.foco(c, t, C["s20.a"] + 0.9, 0.4, lambda a: E.pilula(c, "110 g", P.x(0) - 90, P.y(110), 40, "g", fundo=E.COR, a=a))
    ponto(c, t, C["s20.b"], P, 60, 100, "#2E86AB")
    E.frase(c, t, C["s20.b"], [("100", "g", 62, COR), ("<", "g", 62, TINTA2), ("110", "g", 62, COR)], 1190, 300, passo=0.12)
    E.frase(c, t, C["s20.c"], [("insaturada:", "g", 56), ("tudo", "i", 62), ("se", "i", 62), ("dissolve", "i", 62)], 1190, 400, passo=0.1)
    if t >= C["s20.d"]:
        guias(c, t, C["s20.d"], P, 40, 64, TINTA2)
        E.foco(c, t, C["s20.d"] + 0.9, 0.4, lambda a: E.pilula(c, "64 g", P.x(0) - 90, P.y(64), 40, "g", fundo=TINTA, a=a))
        ponto(c, t, C["s20.d"] + 0.4, P, 40, 100, ERRADO)
        E.frase(c, t, C["s20.d"], [("a", "i", 62), ("40 °C:", "g", 56), ("limite", "i", 62), ("64", "g", 58, COR)], 1190, 560, passo=0.1)
        p = ep(t, C["s20.e"], 0.5)
        if p > 0:
            M.line(c, P.x(40) + 30, P.y(100), P.x(40) + 30, lerp(P.y(100), P.y(64), p), ERRADO, 1, 5)
    E.formula_em(c, t, C["s20.e"], "100 − 64 =", 1190, 760, 76, "g", TINTA2)
    bola_txt(c, t, C["s20.e"] + 0.6, "36 g", 1290, 900, 78, 62, CERTO)
    E.foco(c, t, C["s20.e"] + 0.9, 0.4, lambda a: E.escreve(c, "no fundo", 1400, 922, 64, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", [("a", "i", 70), ("curva", "g", 66), ("é", "i", 70), ("o", "i", 70), ("limite", "g", 66, COR)]),
                 ("s21.b", [("abaixo:", "i", 70), ("insaturada;", "g", 62), ("sobre:", "i", 70), ("saturada", "g", 62)]),
                 ("s21.c", [("a", "i", 70), ("sobra", "g", 66), ("fica", "i", 70), ("no", "i", 70), ("fundo", "i", 70)]),
                 ("s21.d", [("gás:", "g", 66), ("menos", "i", 70), ("no", "i", 70), ("quente", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("concentração", "g", 110, COR)], XE, 400)
    for k, s in enumerate(("g/L", "%", "ppm")):
        pilula_em(c, t, C["s22.b"] + 0.4 * k, s, XE + 110 + 230 * k, 560, 70, TINTA)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 460, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(760, 485, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, limite=b_limite, curva=b_curva, gas=b_gas, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
