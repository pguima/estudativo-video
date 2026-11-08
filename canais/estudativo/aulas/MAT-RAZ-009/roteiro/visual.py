"""Visual — Estudativo · MAT-RAZ-009: regra de três composta com grandeza inversa.
Peças locais: a tabela da regra de três (a mesma da trilha: coluna com nome em itálico e fio, valores grandes, xis na cor
da matéria, seta ao lado de cada coluna: mesmo sentido = direta, sentidos opostos = inversa; a coluna inversa vira de cabeça
para baixo e a seta passa a descer), a corrente "uma de cada vez" e o muro de tijolos do atalho (mesma obra, mesmo total).
Todo instante vem de C[...]: sem voz, os tempos são provisórios e o visual segue os marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-009_regra_de_tres_composta_inversa.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "metodo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 12 * 15 == 180 and 180 / 18 == 10 and 10 * 8 == 80 and 80 / 10 == 8
assert 18 * 10 == 180 and 12 * 8 == 96 and 180 / 12 == 15 and 96 / 12 == 8 and 15 * 8 == 15 * 8
assert 15 * 180 / 96 == 28.125 and 12 * 8 * 15 == 1440 == 18 * 10 * 8
assert 4 * 6 * 15 == 360 == 5 * 8 * 9 and 5 * 8 == 40 and 4 * 6 == 24 and 15 * 3 == 5 * 9


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_res(c, t, t0, s, cx, cy, r=140, size=84, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


# --- tabela da regra de três (mesma linguagem em toda a trilha) ---
DY3 = 150  # distância entre as linhas da tabela


def cabeca(c, t, t0, nome, cx, y, size=56, cor=None, larg=300):
    """nome da grandeza, em itálico, com o fio embaixo"""
    E.foco(c, t, t0, 0.5, lambda a: (centro(c, nome, cx, y, size, "i", cor or TINTA2, a),
                                      M.line(c, cx - larg / 2, y + 34, cx + larg / 2, y + 34, FIO, a, 3)))


def coluna(c, t, cx, y, vals, vira=None, size=110, giro=1):
    """valores de uma coluna: vals = [(texto, cor, t0), ...], linha i na altura y + DY3*(i+1).
    vira = instante em que a coluna vira de cabeça para baixo (os dois valores trocam de linha, num arco)"""
    p = ease_io(prog(t, vira, 0.9)) if vira is not None else 0.0
    n = len(vals)
    for i, (s, cor, t0) in enumerate(vals):
        yi, yj = y + DY3 * (i + 1), y + DY3 * (n - i)
        yy = lerp(yi, yj, p)
        xx = cx + math.sin(math.pi * p) * 90 * (giro if i == 0 else -giro)
        fcen(c, t, t0, s, xx, yy + size * 0.36, size, cor)


def seta(c, t, t0, x, y, desce=True, cor=None, a=1.0, n=2):
    """seta vertical ao lado da coluna, da 1ª à última linha (desce) ou ao contrário (sobe)"""
    p = ep(t, t0, 0.6) * a
    if p <= 0:
        return
    ya, yb = y + DY3 - 40, y + DY3 * n + 40
    if not desce:
        ya, yb = yb, ya
    M.arrow(c, x, ya, x, yb, cor or COR, p, 7, 26, ease_io(prog(t, t0, 0.6)))


def cruz(c, t, t0, xa, xb, y, cor=None, fundo=None):
    """produto cruzado entre duas frações em xa e xb (barra em y): duas diagonais, com o = limpo no meio"""
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.line(c, xa + 60, y - 90, xb - 60, y + 110, cor or E.COR, 1.0, 7, progress=p)
    M.line(c, xa + 60, y + 110, xb - 60, y - 90, cor or E.COR, 1.0, 7, progress=p)
    c.drawCircle((xa + xb) / 2, y + 8, 46, M.paint(fundo or E.PAPEL))


def tipo(c, t, t0, s, cx, cy, cor=None, size=48, escuro=False):
    """pílula com o tipo da relação (direta / inversa)"""
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", fundo=cor or E.COR, cor=E.SOBRE, a=a))


def pessoa(c, cx, base, h, cor=None, a=1.0):
    """bonequinho: cabeça e corpo arredondado"""
    if a <= 0:
        return
    cor = cor or E.COR
    r = h * 0.18
    c.drawCircle(cx, base - h + r, r, M.paint(cor, a))
    w = h * 0.56
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, base - h * 0.58, w, h * 0.58), w * 0.42, w * 0.42), M.paint(cor, a))


def turma(c, t, t0, n, x, base, h=90, gap=22, cor=None, passo=0.08):
    """n bonecos lado a lado, a partir de x; entram um por um"""
    for i in range(n):
        E.foco(c, t, t0 + i * passo, 0.4, lambda a, i=i: pessoa(c, x + i * (h * 0.56 + gap) + h * 0.28, base, h, cor, a))
    return n * (h * 0.56 + gap) - gap


XS3 = (330, 650, 970)  # as três colunas da tabela
YT = 300
NOMES = ("operários", "horas/dia", "dias")


def tabela3(c, t, nomes, tn, linhas, xs=XS3, y=YT, larg=260, size=104, vira=(None, None, None), escuro=False):
    """tabela de três colunas: nomes com o instante tn[i]; linhas[i] = [(texto, cor, t0), (texto, cor, t0)]; vira[i] = instante em que a coluna vira"""
    for i, (nome, x) in enumerate(zip(nomes, xs)):
        cabeca(c, t, tn[i], nome, x, y, 54, CLARO if escuro else None, larg=larg)
        coluna(c, t, x, y, linhas[i], vira[i], size=size)


def elo(c, t, t0, rot, conta, x, y, cor_conta=None, tc=None, dx=330):
    """um elo da corrente: rótulo pesado à esquerda e a conta (com foco) à direita"""
    E.foco(c, t, t0, 0.5, lambda a: E.escreve(c, rot, x, y, 60, "g", TINTA, a))
    if conta:
        E.formula_em(c, t, tc if tc is not None else t0 + 0.3, conta, x + dx, y, 60, "g", cor_conta or COR)


def muro(c, x, base, cols, lins, s=44, cor=None, a=1.0):
    """muro de tijolos: cols tijolos por fiada, lins fiadas, a partir de (x, base) no canto de baixo à esquerda"""
    if a <= 0:
        return
    w, h = s * 2, s
    for r in range(lins):
        off = (w / 2) if r % 2 else 0
        for k in range(cols + (1 if r % 2 else 0)):
            x0 = x + k * w - off
            x1 = min(x0 + w, x + cols * w)
            x0 = max(x0, x)
            if x1 - x0 < 4:
                continue
            M.rrect(c, x0 + 3, base - (r + 1) * h + 3, x1 - x0 - 6, h - 6, 6, cor or E.COR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        xs = (520, 960, 1400)
        q = "28,1..." if t >= kc else "?"
        tabela3(c, t, NOMES, (ka, ka + 1.0, ka + 2.0),
                [[("12", TINTA, ka + 0.3), ("18", TINTA, kb)], [("8", TINTA, ka + 1.3), ("10", TINTA, kb + 1.2)],
                 [("15", TINTA, ka + 2.6), (q, ERRADO if t >= kc else CINZA, kc if t >= kc else kb + 2.2)]], xs, 220, 340, 120)
        E.frase(c, t, lerp(kb, kc, 0.75), ps("mais gente, mais horas", "i", 76) + [("e mais dias?", "g", 76, ERRADO)], W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("regra de três", "g", 104, COR)], XE, 450)
        E.frase(c, t, lerp(ta, tb, 0.45), [("composta", "g", 104, COR)], XE, 580)
        E.frase(c, t, lerp(ta, tb, 0.65), ps("com grandeza", "i", 84) + [("inversa", "g", 84, COR)], XE, 710, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de uma linha", 1500, 610, 66, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("lembre de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "na regra de três inversa", "linha × linha não muda"), ("s03.c", "na composta", "uma grandeza de cada vez"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 710, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- uma de cada vez ----------------
def b_ideia(c, t, C, b):
    a4, b4, c4 = C["s04.a"], C["s04.b"], C["s04.c"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    x1, x2 = 130, 1000
    E.frase(c, t, C["s04"] + 0.1, ps("só os operários", "g", 60, COR) + ps("(8 h/dia)", "i", 60), x1, 230, passo=0.1)
    elo(c, t, a4, "12 op.", "15 dias", x1, 400, TINTA)
    elo(c, t, b4, "1 op.", "12 · 15 = 180", x1, 560)
    elo(c, t, c4, "18 op.", "180 ÷ 18 = 10", x1, 720)
    if t >= C["s05"]:
        M.line(c, 960, 190, 960, 820, FIO, ep(t, C["s05"], 0.4), 3)
        E.frase(c, t, C["s05"] + 0.1, ps("agora as horas", "g", 60, COR) + ps("(18 op.)", "i", 60), x2, 230, passo=0.1)
    elo(c, t, a5, "8 h/dia", "10 · 8 = 80 h", x2, 400, dx=300)
    elo(c, t, b5, "10 h/dia", "80 ÷ 10 = 8", x2, 560, dx=300)
    E.foco(c, t, c5, 0.5, lambda a: E.pilula(c, "8 dias", 1430, 700, 80, "g", fundo=CERTO, cor=BR, a=a))
    E.frase(c, t, d5 - 1.6, ps("mais gente e mais horas:", "i", 66), W / 2, 930, "center", 0.12)
    E.frase(c, t, d5, [("menos dias", "g", 70, COR)], 1440, 930, "left")


# ---------------- colunas ----------------
def b_metodo(c, t, C, b):
    b6, c6, d6 = C["s06.b"], C["s06.c"], C["s06.d"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8 = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    E.frase(c, t, C["s06"] + 0.2, ps("as colunas,", "i", 72) + [("com um passo a mais", "g", 72, COR)], XE, 170, passo=0.12)
    tabela3(c, t, NOMES, (b6, c6, d6),
            [[("12", TINTA, b6 + 0.3), ("18", TINTA, b6 + 0.6)], [("8", TINTA, c6 + 0.4), ("10", TINTA, c6 + 0.7)],
             [("15", TINTA, d6 + 0.3), ("x", COR, d6 + 0.6)]], vira=(b8, c8, None))
    # setas: dias desce; operários e horas sobem (inversas) e, ao virar, descem
    seta(c, t, a7, XS3[2] + 125, YT)
    E.foco(c, t, a7, 0.5, lambda a: E.caixa_pontilhada(c, XS3[2] - 140, YT - 50, 280, 440, a * (1 - ep(t, C["s09"], 0.4)), E.COR))
    for i, (tt, tv) in enumerate(((b7, b8), (c7, c8))):
        v = ep(t, tv, 0.9)
        seta(c, t, tt, XS3[i] + 125, YT, desce=False, cor=TINTA, a=1 - v)
        seta(c, t, tv + 0.7, XS3[i] + 125, YT, cor=TINTA)
        tipo(c, t, tt + 0.6, "inversa", XS3[i], 780)
    E.saida(c, t, C["s09"] - 0.1, lambda: E.frase(c, t, a8, ps("vire as", "i", 64) + [("inversas", "g", 64, COR)], 1460, 420, "center", 0.12))
    tipo(c, t, d8, "não vira", XS3[2], 780, TINTA)

    def montagem():
        if t < C["s09"]:
            return
        a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
        fcen(c, t, a9, "f{15}{x} = f{18}{12} · f{10}{8}", 1480, 470, 96, TINTA)
        E.saida(c, t, d9, lambda: (fcen(c, t, b9, "18 · 10 = 180", 1480, 620, 64, TINTA2), fcen(c, t, c9, "12 · 8 = 96", 1480, 710, 64, TINTA2)))
        fcen(c, t, d9, "f{180}{96} = f{15}{8}", 1480, 670, 90, COR)
        fcen(c, t, d9 + 0.8, "f{15}{x} = f{15}{8}", 1480, 860, 80, TINTA)
        E.foco(c, t, e9, 0.5, lambda a: E.pilula(c, "x = 8", 1480, 990, 72, "g", cor=E.SOBRE, a=a))
    montagem()


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    E.saida(c, t, b11 - 0.1, lambda: E.frase(c, t, C["s10"] + 0.2, ps("e os", "i", 76) + [("28 dias?", "g", 76, ERRADO)], XE, 170, passo=0.12))
    t0 = C["s10"] + 0.4
    tabela3(c, t, NOMES, (t0, t0, t0), [[("12", TINTA, t0), ("18", TINTA, t0)], [("8", TINTA, t0), ("10", TINTA, t0)], [("15", TINTA, t0), ("x", COR, t0)]])
    for x in XS3:
        seta(c, t, a10, x + 125, YT, cor=ERRADO)
    E.saida(c, t, b11 - 0.1, lambda: tipo(c, t, a10 + 0.5, "tudo direto", XS3[1], 780, ERRADO))

    def conta():
        fcen(c, t, b10, "f{15}{x} = f{12}{18} · f{8}{10}", 1480, 430, 90, TINTA)
        fcen(c, t, c10, "x = 28,125", 1480, 610, 100, ERRADO)
        E.frase(c, t, a11, ps("mais operários e mais horas", "i", 52), 1480, 760, "center", 0.08)
        E.frase(c, t, a11 + 1.2, ps("dão", "i", 56) + [("mais dias?", "g", 60, ERRADO)], 1440, 840, "center", 0.1)
        E.foco(c, t, a11 + 2.0, 0.5, lambda a: E.selo(c, 1740, 820, 46, False, a))
    E.saida(c, t, b11 - 0.1, conta)
    # comparar só com a do x
    if t >= b11:
        y = YT + 470
        for i in (0, 1):
            p = ep(t, b11 + 0.4 * i, 0.6)
            if p > 0:
                x0, x1 = XS3[i], XS3[2]
                pth = skia.Path(); pth.moveTo(x0, y); pth.quadTo((x0 + x1) / 2, y + 150 - 40 * i, x1, y)
                pt = M.paint(CERTO, p, stroke=6); c.drawPath(pth, pt)
        E.frase(c, t, b11, ps("cada coluna", "i", 56) + [("só com a do x", "g", 56, CERTO)], 1480, 450, "center", 0.12)
        p = ep(t, c11, 0.6)
        if p > 0:
            yy = YT - 70
            pth = skia.Path(); pth.moveTo(XS3[0], yy); pth.quadTo((XS3[0] + XS3[1]) / 2, yy - 110, XS3[1], yy)
            c.drawPath(pth, M.paint(ERRADO, p, stroke=6))
            E.risco(c, 440, yy - 110, 540, yy - 10, t, c11 + 0.3, largura=10)
        E.frase(c, t, c11, ps("nunca", "i", 56) + [("uma com a outra", "g", 56, ERRADO)], 1480, 600, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    xs = (300, 560, 820)

    def linhas():
        E.frase(c, t, C["s12"] + 0.2, ps("o atalho:", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, a12, ps("multiplique", "g", 80, BR) + ps("tudo em cada linha", "i", 80, CLARO) + ps("e iguale", "g", 80, BR), W / 2, 290, "center", 0.12)
        for i, (nome, x) in enumerate(zip(NOMES, xs)):
            cabeca(c, t, b12 - 0.3, nome, x, 400, 46, CLARO, 220)
        for j, (vals, t0) in enumerate(((("12", "8", "15"), b12), (("18", "10", "x"), a13))):
            y = 400 + DY3 * (j + 1)
            p = ep(t, t0, 0.5)
            if p > 0:
                M.rrect(c, 190, y - 70, 740, 140, 70, CLARO, 0.16 * p)
            for k, (v, x) in enumerate(zip(vals, xs)):
                fcen(c, t, t0 + 0.2 * k, v, x, y + 36, 100, CLARO if v == "x" else BR)
            for k in (0, 1):
                E.foco(c, t, t0 + 0.4, 0.4, lambda a, k=k, y=y: centro(c, "·", (xs[k] + xs[k + 1]) / 2, y + 30, 90, "g", CLARO, a))
        fcen(c, t, b12 + 1.0, "12 · 8 · 15 = 1.440", 1440, 560, 76, BR)
        E.foco(c, t, c12, 0.5, lambda a: E.pilula(c, "homem-hora", 1440, 650, 50, "g", cor=BR, a=a))
        w1, w2 = E.formula(c, "18 · 10 · x", 0, 0, 76, a=0), E.formula(c, " = 180x", 0, 0, 76, a=0)
        x0 = 1440 - (w1 + w2) / 2
        E.formula_em(c, t, a13 + 0.8, "18 · 10 · x", x0, 790, 76, "g", BR)
        E.formula_em(c, t, b13, " = 180x", x0 + w1, 790, 76, "g", BR)
        fcen(c, t, c13, "180x = 1.440", 1440, 910, 76, BR)
        E.foco(c, t, d13, 0.5, lambda a: E.pilula(c, "x = 1.440 ÷ 180 = 8", 1440, 1010, 56, "g", cor=BR, a=a))
    E.saida(c, t, C["s14"] - 0.1, linhas)

    if t >= C["s14"]:
        a14, b14, c14, d14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"]
        E.frase(c, t, a14, ps("o muro é o mesmo:", "i", 72, CLARO) + ps("o total de horas também", "g", 72, BR), W / 2, 200, "center", 0.12)
        E.foco(c, t, a14 + 0.6, 0.5, lambda a: muro(c, 200, 560, 5, 4, 36, CLARO, a))
        E.frase(c, t, b14, ps("não vale se a obra", "i", 64, CLARO) + ps("mudar de tamanho", "g", 64, BR), 1340, 420, "center", 0.1)
        E.foco(c, t, c14, 0.5, lambda a: muro(c, 200, 900, 10, 4, 36, CLARO, a))
        E.foco(c, t, c14 + 0.3, 0.5, lambda a: centro(c, "2× maior: horas dobram", 1340, 640, 64, "g", ERRADO, a))
        E.foco(c, t, d14, 0.5, lambda a: E.pilula(c, "volte às colunas", 1340, 800, 66, "g", cor=BR, a=a))
        E.frase(c, t, d14 + 0.8, ps("+ uma coluna para o tamanho", "i", 54, CLARO), 1340, 920, "center", 0.1)


# ---------------- questão ----------------
NOMES_Q = ("jardineiros", "horas/dia", "dias")


def b_questao(c, t, C, b):
    a15, b15 = C["s15.a"], C["s15.b"]
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    xs = (300, 610, 920)
    tabela3(c, t, NOMES_Q, (a15, a15 + 1.0, a15 + 2.0),
            [[("4", TINTA, a15 + 0.4), ("5", TINTA, b15 + 0.4)], [("6", TINTA, a15 + 1.4), ("8", TINTA, b15 + 1.4)],
             [("15", TINTA, a15 + 2.6), ("?", CINZA, b15 + 2.6)]], xs, 300, 270)
    E.frase(c, t, b15 + 3.0, ps("o mesmo", "i", 60) + [("parque", "g", 60, COR)], XE, 860, passo=0.12)
    E.relogio(c, t, C["s16.a"], 1470, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs = (270, 560, 850)
    t0 = C["s17"]
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    vals = [[("4", TINTA, t0), ("5", TINTA, t0)], [("6", TINTA, t0), ("8", TINTA, t0)], [("15", TINTA, t0), ("x", COR, t0)]]
    tabela3(c, t, NOMES_Q, (t0, t0, t0), vals, xs, 300, 250, 96, vira=(b18 - 0.6, b18 - 0.6, None))
    for j, tt in enumerate((a17, b17)):
        p = ep(t, tt, 0.5) * (1 - ep(t, b18 - 1.0, 0.4))
        if p > 0:
            y = 300 + DY3 * (j + 1)
            M.rrect(c, 160, y - 70, 800, 140, 70, E.COR, 0.10 * p)

    def atalho():
        E.frase(c, t, t0 + 0.3, ps("pelo atalho", "i", 60, COR), 1440, 200, "center")
        fcen(c, t, a17, "4 · 6 · 15 = 360", 1440, 360, 84, TINTA)
        fcen(c, t, b17, "5 · 8 · x = 40x", 1440, 520, 84, TINTA)
        fcen(c, t, c17, "x = 360 ÷ 40", 1360, 680, 84, TINTA)
        E.foco(c, t, c17 + 0.8, 0.5, lambda a: E.pilula(c, "9 dias", 1440, 830, 76, "g", fundo=CERTO, cor=BR, a=a))
        E.frase(c, t, a18 - 1.0, ps("menos dias:", "i", 60), 1340, 970, "center", 0.1)
        E.foco(c, t, a18, 0.5, lambda a: E.selo(c, 1560, 950, 40, True, a))
    E.saida(c, t, b18 - 1.0, atalho)

    if t >= b18 - 1.0:
        E.frase(c, t, b18 - 0.9, ps("pelas colunas,", "i", 60, COR) + ps("viram as inversas", "g", 60, COR), 1400, 200, "center", 0.1)
        fcen(c, t, b18, "f{5}{4} · f{8}{6} = f{5}{3}", 1420, 420, 90, TINTA)
        fcen(c, t, c18, "f{15}{x} = f{5}{3}", 1420, 650, 90, TINTA)
        E.foco(c, t, d18, 0.5, lambda a: E.pilula(c, "x = 9", 1420, 850, 76, "g", fundo=CERTO, cor=BR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", "compare com a do x"), ("s19.b", "vire as inversas"), ("s19.c", "mesma obra: linha × linha"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                          centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20 = C["s20.a"], C["s20.b"]
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula:", "i", 84), XE, 260)
    E.frase(c, t, C["s20"] + 1.0, ps("nem direta, nem inversa", "g", 84, COR), XE, 380, passo=0.12)
    # o quadrado e o quadrado de lado dobrado
    E.foco(c, t, a20, 0.5, lambda a: M.rrect(c, XE, 520, 130, 130, 6, E.COR, a))
    q = ep(t, b20, 0.6)
    if q > 0:
        x0, y0, l = XE + 220, 520, 260
        for r in range(2):
            for k in range(2):
                M.rrect(c, x0 + k * l / 2 + 4, y0 + r * l / 2 + 4, l / 2 - 8, l / 2 - 8, 6, E.COR, q)
    E.foco(c, t, b20 + 0.4, 0.5, lambda a: E.escreve(c, "lado × 2: área × 4", XE + 540, 690, 64, "g", TINTA, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1530, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1660, p), lerp(560, 360, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, metodo=b_metodo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
