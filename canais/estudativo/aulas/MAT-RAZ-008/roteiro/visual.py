"""Visual — Estudativo · MAT-RAZ-008: regra de três composta com grandezas diretas.
Peças locais: a tabela da regra de três (a mesma da trilha: coluna com nome em itálico e fio, valores grandes, xis na cor
da matéria, seta ao lado de cada coluna, setas no mesmo sentido = direta), a corrente "uma mudança de cada vez" e a grade de
horas de máquina do atalho (3 × 4 = 12 quadradinhos com 10 peças cada; depois 5 × 6 = 30).
Todo instante vem de C[...]: sem voz, os tempos são provisórios e o visual segue os marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-008_regra_de_tres_composta_diretas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "metodo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 120 / 3 == 40 and 40 * 5 == 200 and 200 / 4 == 50 and 50 * 6 == 300
assert 3 * 4 == 12 and 5 * 6 == 30 and 120 * 5 == 600 and 600 / 2 == 300 and 120 / 12 == 10 and 30 * 10 == 300
assert 4 * 6 == 24 and 72 / 24 == 3 and 6 * 5 == 30 and 30 * 3 == 90 and 72 * 5 == 4 * 90


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


def quadradinhos(c, t, t0, lin, col, cx, cy, st, tn=None, n="10", cor=None, tinta="#07070F"):
    """lin × col quadradinhos (horas de máquina), entram linha a linha; tn = instante do número dentro de cada um"""
    x0, y0 = cx - col * st / 2, cy - lin * st / 2
    s = st * 0.86
    for r in range(lin):
        for k in range(col):
            q = ep(t, t0 + (r * col + k) * 0.04, 0.3)
            if q <= 0:
                continue
            x, y = x0 + k * st + st / 2, y0 + r * st + st / 2
            M.rrect(c, x - s / 2, y - s / 2, s, s, s * 0.16, cor or CLARO, q)
            if tn is not None:
                qa = ep(t, tn + (r * col + k) * 0.03, 0.3)
                if qa > 0:
                    centro(c, n, x, y + s * 0.17, s * 0.46, "g", tinta, qa)


XS3 = (330, 650, 970)  # as três colunas da tabela
YT = 300


def tabela3(c, t, nomes, tn, linhas, xs=XS3, y=YT, larg=260, size=104):
    """tabela de três colunas: nomes com o instante tn[i]; linhas[i] = [(texto, cor, t0), (texto, cor, t0)]"""
    for i, (nome, x) in enumerate(zip(nomes, xs)):
        cabeca(c, t, tn[i], nome, x, y, 54, larg=larg)
        coluna(c, t, x, y, linhas[i], size=size)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        xs = (520, 960, 1400)
        q = "200" if t >= kc else "?"
        tabela3(c, t, ("máquinas", "horas", "peças"), (ka, ka + 0.6, ka + 1.2),
                [[("3", TINTA, ka + 0.3), ("5", TINTA, kb)], [("4", TINTA, ka + 0.9), ("6", TINTA, kb + 0.8)],
                 [("120", TINTA, ka + 1.6), (q, ERRADO if t >= kc else CINZA, kc if t >= kc else kb + 1.6)]], xs, 220, 340, 120)
        E.frase(c, t, kc + 1.4, ps("faltou", "i", 84) + [("uma grandeza", "g", 84, ERRADO)] + ps("na conta", "i", 84), W / 2, 900, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("regra de três", "g", 104, COR)], XE, 450)
        E.frase(c, t, lerp(ta, tb, 0.5), ps("com", "i", 90) + [("3 grandezas", "g", 96, COR)], XE, 590, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("ou mais", "i", 90), XE, 710, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("lembre de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 800
    itens = (("s03.b", "grandezas diretas", "dobra uma, dobra a outra"), ("s03.c", "a regra de três direta", "tabela e produto cruzado"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 280 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    q1 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(450, 710, q1), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 960, 960, "left", 0.12)


# ---------------- uma mudança de cada vez ----------------
def elo(c, t, t0, rot, conta, x, y, cor_conta=None, tc=None):
    """um elo da corrente: rótulo pesado à esquerda e a conta (com foco) à direita"""
    E.foco(c, t, t0, 0.5, lambda a: E.escreve(c, rot, x, y, 60, "g", TINTA, a))
    if conta:
        E.formula_em(c, t, tc if tc is not None else t0 + 0.3, conta, x + 330, y, 60, "g", cor_conta or COR)


def b_ideia(c, t, C, b):
    def titulo():
        E.frase(c, t, C["s04"] + 0.3, ps("três grandezas mudam juntas", "i", 76), W / 2, 330, "center", 0.12)
        E.frase(c, t, C["s04.a"], ps("mude", "i", 120) + [("uma de cada vez", "g", 120, COR)], W / 2, 560, "center", 0.14)
        E.frase(c, t, C["s04.a"] + 2.2, ps("primeiro, só as máquinas:", "i", 66), W / 2, 780, "center", 0.12)
        E.foco(c, t, C["s04.a"] + 4.0, 0.5, lambda a: E.pilula(c, "horas paradas em 4", W / 2, 900, 60, "g", cor=E.SOBRE, a=a))
    E.saida(c, t, C["s05"] - 0.1, titulo)

    def correntes():
        a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
        a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
        x1, x2 = 130, 1000
        E.frase(c, t, C["s05"] + 0.1, ps("só as máquinas", "g", 60, COR) + ps("(4 h)", "i", 60), x1, 230, passo=0.1)
        elo(c, t, a5, "3 máq.", "120", x1, 400, TINTA)
        elo(c, t, b5, "1 máq.", "120 ÷ 3 = 40", x1, 560)
        elo(c, t, c5, "5 máq.", "40 · 5 = 200", x1, 720)
        if t >= C["s06"]:
            M.line(c, 960, 190, 960, 820, FIO, ep(t, C["s06"], 0.4), 3)
            E.frase(c, t, C["s06"] + 0.1, ps("agora as horas", "g", 60, COR) + ps("(5 máq.)", "i", 60), x2, 230, passo=0.1)
        elo(c, t, a6, "4 h", "200", x2, 400, TINTA)
        elo(c, t, b6, "1 h", "200 ÷ 4 = 50", x2, 560)
        elo(c, t, c6, "6 h", "50 · 6 = 300", x2, 720)
        if C["s05.end"] - 3.0 <= t < C["s06"]:
            E.frase(c, t, C["s05.end"] - 3.0, ps("o erro", "i", 64) + ps("parava aqui", "g", 64, ERRADO), x1, 900, passo=0.12)
        E.foco(c, t, c5 + 0.8, 0.5, lambda a: E.caixa_pontilhada(c, x1 + 310, 640, 470, 110, a * (1 - ep(t, C["s06"], 0.4)), ERRADO))
    if C["s05"] <= t:
        E.saida(c, t, C["s07"] - 0.1, correntes)

    if t >= C["s07"]:
        a7, b7 = C["s07.a"], C["s07.b"]
        E.foco(c, t, a7, 0.6, lambda a: (E.bola(c, 1420, 520, 230 * ease_back(prog(t, a7, 0.6)), a=a),
                                          centro(c, "300", 1420, 540, 150, "g", E.SOBRE, a), centro(c, "peças", 1420, 630, 64, "i", E.SOBRE, a)), blur=0)
        for i, (txt, t0) in enumerate((("mais máquinas,", lerp(a7, b7, 0.35)), ("mais horas,", lerp(a7, b7, 0.7)))):
            y = 380 + i * 200
            E.frase(c, t, t0, ps(txt, "i", 76) + [("mais peças", "g", 76, COR)], XE, y, passo=0.12)
        p = ep(t, b7, 0.6)
        if p > 0:
            for x in (330, 560, 790):
                M.arrow(c, x, 900, x, 900 - 140 * p, E.COR, p, 9, 30, 1.0)
        E.frase(c, t, b7 + 0.3, ps("as duas", "i", 66) + [("empurram para cima", "g", 66, COR)], 900, 870, passo=0.12)


# ---------------- método das colunas ----------------
def tabela_maquinas(c, t, C, cor_x=None):
    b8, c8, d8 = C["s08.b"], C["s08.c"], C["s08.d"]
    tabela3(c, t, ("máquinas", "horas", "peças"), (b8, c8, d8),
            [[("3", TINTA, b8 + 0.3), ("5", TINTA, b8 + 0.6)], [("4", TINTA, c8 + 0.3), ("6", TINTA, c8 + 0.6)],
             [("120", TINTA, d8 + 0.3), ("x", cor_x or COR, d8 + 0.6)]])


def b_metodo(c, t, C, b):
    def tudo():
        E.frase(c, t, C["s08"] + 0.2, ps("uma coluna para", "i", 72) + [("cada grandeza", "g", 72, COR)], XE, 170, passo=0.12)
        tabela_maquinas(c, t, C)
        a9, b9, c9 = C["s09.a"], C["s09.b"], C["s09.c"]
        seta(c, t, a9, XS3[2] + 125, YT)
        E.foco(c, t, a9, 0.5, lambda a: E.caixa_pontilhada(c, XS3[2] - 140, YT - 50, 280, 440, a, E.COR))
        seta(c, t, b9, XS3[0] + 125, YT)
        tipo(c, t, b9 + 0.6, "direta", XS3[0], 780)
        seta(c, t, c9, XS3[1] + 125, YT)
        tipo(c, t, c9 + 0.6, "direta", XS3[1], 780)
        if t < C["s10"]:
            E.frase(c, t, a9 + 0.3, ps("cada uma", "i", 64) + ps("contra a do x", "g", 64, COR), 1460, 420, "center", 0.12)
            E.frase(c, t, a9 + 1.5, ps("uma de cada vez", "i", 64), 1460, 520, "center", 0.12)
        # a montagem e a conta, à direita
        a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
        E.frase(c, t, a10, ps("fração do x = produto das outras", "i", 50, TINTA2), 1480, 300, "center", 0.08)
        E.formula_em(c, t, b10, "f{120}{x}", 1230, 470, 96, "g", TINTA)
        E.formula_em(c, t, c10, "= f{3}{5} · f{4}{6}", 1370, 470, 96, "g", TINTA)
        a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
        E.saida(c, t, c11, lambda: (fcen(c, t, a11, "3 · 4 = 12", 1480, 620, 64, TINTA2), fcen(c, t, b11, "5 · 6 = 30", 1480, 710, 64, TINTA2)))
        fcen(c, t, c11, "f{12}{30} = f{2}{5}", 1480, 670, 90, COR)
        fcen(c, t, d11, "2 · x = 120 · 5 = 600", 1440, 850, 72, TINTA)
        E.foco(c, t, e11, 0.5, lambda a: E.pilula(c, "x = 300", 1480, 985, 72, "g", cor=E.SOBRE, a=a))
    E.saida(c, t, C["s12"] - 0.1, tudo)
    if t < C["s12"]:
        return
    # por que multiplicar as frações
    a12, b12, fim = C["s12.a"], C["s12.b"], C["s12.end"]
    E.frase(c, t, C["s12"] + 0.2, ps("por que", "i", 80) + [("multiplicar", "g", 80, COR)] + ps("as frações?", "i", 80), W / 2, 180, "center", 0.12)
    for i, (op, f, ff, t0) in enumerate((("÷ 3 e · 5", "f{5}{3}", "f{3}{5}", a12), ("÷ 4 e · 6", "f{6}{4}", "f{4}{6}", lerp(a12, b12, 0.5)))):
        y = 420 + i * 230
        fcen(c, t, t0, op, 470, y, 84, TINTA)
        fcen(c, t, t0 + 0.8, "= · " + f, 860, y, 84, TINTA)
        fcen(c, t, b12 + 0.6 * i, ff, 1430, y, 96, COR)
        p = ep(t, b12 + 0.6 * i, 0.6)
        if p > 0:
            M.arrow(c, 1030, y - 28, 1030 + 280 * p, y - 28, E.COR, p, 6, 22, 1.0)
    E.frase(c, t, b12 + 1.4, ps("de cabeça para baixo", "i", 56, COR), 1430, 300, "center", 0.1)
    E.frase(c, t, lerp(b12, fim, 0.3), ps("o antigo fica em cima, como em", "i", 56), 900, 850, "center", 0.1)
    fcen(c, t, lerp(b12, fim, 0.3) + 0.8, "f{120}{x}", 1520, 850, 80, COR)
    E.foco(c, t, lerp(b12, fim, 0.75), 0.5, lambda a: E.pilula(c, "as mudanças se acumulam: multiplica", W / 2, 990, 56, "g", cor=E.SOBRE, a=a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a13, b13, c13, d13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    E.frase(c, t, C["s13"] + 0.2, ps("o erro", "i", 80) + [("comum", "g", 80, ERRADO)], XE, 170, passo=0.12)
    t0 = C["s13"] + 0.4
    tabela3(c, t, ("máquinas", "horas", "peças"), (t0, t0, t0),
            [[("3", TINTA, t0), ("5", TINTA, t0)], [("4", TINTA, t0), ("6", TINTA, t0)], [("120", TINTA, t0), ("x", COR, t0)]])
    # esquecer a coluna das horas
    p = ep(t, a13, 0.5) * (1 - ep(t, c13, 0.4))
    if p > 0:
        M.rrect(c, XS3[1] - 150, YT - 60, 300, 450, 24, E.PAPEL, 0.75 * p)
        E.risco(c, XS3[1] - 120, YT + 380, XS3[1] + 120, YT - 20, t, a13, largura=14)
    E.frase(c, t, a13 + 0.3, ps("esqueceu", "i", 64) + ps("uma coluna", "g", 64, ERRADO), 1460, 400, "center", 0.12)
    fcen(c, t, b13, "x = 200", 1460, 560, 110, ERRADO)
    E.foco(c, t, c13, 0.5, lambda a: E.caixa_pontilhada(c, XS3[1] - 110, YT + 2 * DY3 - 75, 220, 150, a, E.COR))
    E.frase(c, t, c13 + 0.2, ps("mas foram", "i", 64) + ps("6 horas", "g", 64, COR), 1460, 720, "center", 0.12)
    for i, x in enumerate(XS3):
        E.foco(c, t, d13 + 0.3 * i, 0.4, lambda a, x=x, i=i: (E.bola(c, x, YT + 470, 44, a=a), centro(c, str(i + 1), x, YT + 489, 54, "g", E.SOBRE, a)))
    E.foco(c, t, d13 + 0.4, 0.5, lambda a: E.pilula(c, "conte as colunas", 1460, 900, 64, "g", cor=E.SOBRE, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    a15, b15, c15 = C["s15.a"], C["s15.b"], C["s15.c"]

    def parte1():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, a14, ps("1 máquina", "g", 80, BR) + ps("em", "i", 80, CLARO) + ps("1 hora", "g", 80, BR), W / 2, 290, "center", 0.12)
        quadradinhos(c, t, b14, 3, 4, 560, 640, 110, tn=c14 + 0.6)
        E.foco(c, t, b14, 0.5, lambda a: (centro(c, "3 máquinas", 560, 470, 46, "i", CLARO, a)))
        E.foco(c, t, b14 + 0.3, 0.5, lambda a: (centro(c, "4 horas", 560, 850, 46, "i", CLARO, a)))
        fcen(c, t, b14 + 0.6, "3 · 4 = 12", 1380, 520, 96, BR)
        E.foco(c, t, b14 + 1.2, 0.5, lambda a: centro(c, "horas de máquina", 1380, 600, 52, "i", CLARO, a))
        fcen(c, t, c14, "120 ÷ 12 = 10", 1380, 760, 96, BR)
        E.foco(c, t, c14 + 0.6, 0.5, lambda a: centro(c, "peças por hora de máquina", 1380, 840, 52, "i", CLARO, a))
    E.saida(c, t, a15 - 0.1, parte1)

    def parte2():
        E.frase(c, t, a15, ps("nova situação", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        quadradinhos(c, t, a15, 5, 6, 560, 600, 96, tn=b15)
        E.foco(c, t, a15, 0.5, lambda a: centro(c, "5 máquinas × 6 horas", 560, 380, 46, "i", CLARO, a))
        fcen(c, t, a15 + 0.6, "5 · 6 = 30", 1380, 420, 96, BR)
        fcen(c, t, b15, "30 · 10 =", 1300, 620, 96, BR)
        E.foco(c, t, b15 + 0.5, 0.5, lambda a: (E.bola(c, 1640, 590, 110, a=a), centro(c, "300", 1640, 620, 84, "g", BR, a)))
        E.frase(c, t, c15, ps("cada máquina, cada hora:", "i", 60, CLARO), 1380, 820, "center", 0.1)
        E.frase(c, t, c15 + 0.8, ps("o mesmo tanto", "g", 64, BR), 1380, 910, "center", 0.1)
    if a15 <= t:
        E.saida(c, t, C["s16"] - 0.1, parte2)

    if t >= C["s16"]:
        a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
        E.frase(c, t, a16, ps("não compensa se a divisão", "i", 80, CLARO) + ps("não for exata", "g", 80, BR), W / 2, 300, "center", 0.12)
        fcen(c, t, b16, "100 ÷ 12 = 8,333...", W / 2, 540, 110, BR)
        E.foco(c, t, b16 + 1.6, 0.5, lambda a: centro(c, "número quebrado", W / 2, 660, 60, "i", ERRADO, a))
        E.foco(c, t, c16, 0.5, lambda a: E.pilula(c, "vá pelas colunas", W / 2, 850, 80, "g", cor=BR, a=a))


# ---------------- questão ----------------
NOMES_Q = ("costureiras", "horas", "camisetas")


def b_questao(c, t, C, b):
    a17, b17 = C["s17.a"], C["s17.b"]
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    xs = (300, 610, 920)
    tabela3(c, t, NOMES_Q, (a17, a17 + 0.8, a17 + 1.6),
            [[("4", TINTA, a17 + 0.4), ("6", TINTA, b17 + 0.8)], [("6", TINTA, a17 + 1.2), ("5", TINTA, b17 + 1.8)],
             [("72", TINTA, a17 + 2.0), ("?", CINZA, b17 + 0.3)]], xs, 300, 270)
    E.frase(c, t, b17 + 2.6, ps("no", "i", 60) + [("mesmo ritmo", "g", 60, COR)], XE, 860, passo=0.12)
    E.relogio(c, t, C["s18.a"], 1470, 470, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs = (270, 560, 850)
    t0 = C["s19"]
    vals = [[("4", TINTA, t0), ("6", TINTA, t0)], [("6", TINTA, t0), ("5", TINTA, t0)], [("72", TINTA, t0), ("x", COR, t0)]]
    tabela3(c, t, NOMES_Q, (t0, t0, t0), vals, xs, 300, 250, 96)
    a19, b19 = C["s19.a"], C["s19.b"]
    a20, b20, c20, d20, e20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"], C["s20.e"]

    def atalho():
        E.frase(c, t, t0 + 0.3, ps("pelo atalho", "i", 60, COR), 1420, 200, "center")
        fcen(c, t, a19, "4 · 6 = 24", 1420, 330, 80, TINTA)
        E.foco(c, t, a19 + 0.8, 0.5, lambda a: centro(c, "horas de trabalho", 1420, 400, 46, "i", TINTA2, a))
        fcen(c, t, b19, "72 ÷ 24 = 3", 1420, 520, 80, TINTA)
        E.foco(c, t, b19 + 0.8, 0.5, lambda a: centro(c, "camisetas por hora", 1420, 590, 46, "i", TINTA2, a))
        fcen(c, t, a20, "6 · 5 = 30", 1420, 720, 80, TINTA)
        fcen(c, t, b20, "30 · 3 =", 1340, 880, 80, TINTA)
        E.foco(c, t, b20 + 0.4, 0.5, lambda a: (E.bola(c, 1600, 852, 80, CERTO, a), centro(c, "90", 1600, 880, 72, "g", BR, a)))
    E.saida(c, t, c20 - 0.1, atalho)

    def colunas_():
        E.frase(c, t, c20, ps("pelas colunas", "i", 60, COR), 1420, 200, "center")
        fcen(c, t, c20 + 0.4, "f{72}{x} = f{4}{6} · f{6}{5}", 1420, 420, 90, TINTA)
        fcen(c, t, d20, "f{72}{x} = f{4}{5}", 1420, 650, 90, TINTA)
        E.foco(c, t, e20, 0.5, lambda a: (E.bola(c, 1420, 850, 90, CERTO, a), E.formula(c, "x = 90", 1420, 870, 56, "g", BR, a, "center")))
    if t >= c20:
        E.saida(c, t, C["s21"] - 0.1, colunas_)

    if t >= C["s21"]:
        a21, b21, c21 = C["s21.a"], C["s21.b"], C["s21.c"]
        # costureiras sobem, horas descem
        for x, sobe, rot in ((xs[0], True, "subiu"), (xs[1], False, "desceu")):
            q = ep(t, a21 + (0 if sobe else 1.2), 0.5)
            if q > 0:
                y = 300 + DY3 * 2 - 30
                M.arrow(c, x + 80, y + (30 if sobe else -50), x + 80, y + (-50 if sobe else 30), CERTO if sobe else ERRADO, q, 6, 20, q)
                centro(c, rot, x, 300 + DY3 * 2 + 110, 46, "i", TINTA2, q)
        E.frase(c, t, b21, ps("mesmo assim,", "i", 60), 1420, 300, "center", 0.1)
        E.frase(c, t, b21 + 0.5, ps("as duas são diretas", "g", 64, COR), 1420, 380, "center", 0.1)
        E.frase(c, t, lerp(b21, c21, 0.45), ps("direta não quer dizer", "i", 56), 1420, 520, "center", 0.1)
        E.frase(c, t, lerp(b21, c21, 0.45) + 0.6, ps("tudo sobe", "g", 60, ERRADO), 1420, 595, "center", 0.1)
        E.frase(c, t, c21, ps("cada uma, sozinha, puxa as peças", "i", 56), 1420, 740, "center", 0.1)
        E.frase(c, t, c21 + 1.0, ps("para o lado dela", "g", 60, COR), 1420, 815, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", "uma coluna por grandeza"), ("s22.b", "compare com a do x"), ("s22.c", "multiplique as frações"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                          centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s23.a"], [("grandeza inversa", "g", 130, COR)], XE, 460)
    E.frase(c, t, C["s23.b"], ps("operários · horas por dia · dias", "i", 72), XE, 590, passo=0.14)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1530, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1660, p), lerp(560, 360, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, metodo=b_metodo, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
