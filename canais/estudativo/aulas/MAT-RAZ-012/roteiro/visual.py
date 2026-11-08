"""Visual — Estudativo · MAT-RAZ-012: praticando razão, proporção e regra de três (aula de prática, 5 situações).
Peças locais: cabeçalho de situação (número na esfera), a tabela da trilha (coluna com nome em itálico e fio, valores,
xis na cor da matéria, seta ao lado: mesmo sentido = direta, sentidos opostos = inversa; coluna inversa vira de cabeça para
baixo), faixa de linha para o "multiplique na linha" e a grade de m² da lona. Todo instante vem de C[...]: sem voz, os
tempos são provisórios e o visual segue os marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-012_praticando_razao_proporcao_regra_de_tres.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
assert 30 + 4 * 5 == 50 and 30 + 4 * 10 == 70 and 10 * 4 == 40
assert 4 * 216 == 96 * 9 == 864 and 96 / 4 == 24 and 24 * 9 == 216
assert 90 * 4 == 360 == 120 * 3
assert 6 * 8 * 20 == 960 == 8 * 10 * 12 and 8 * 10 == 80 and 80 * 3 == 48 * 5 and 20 * 3 == 5 * 12
assert 5 * 5 == 25 and 100 / 25 == 4 and 10 * 10 == 100 and 100 * 4 == 400


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


CLARA = E.mix(E.COR, "#FFFFFF", 0.5)


def tabela_n(c, t, nomes, tn, linhas, xs, y=300, larg=260, size=104, vira=None, escuro=False):
    """tabela da trilha com n colunas: linhas[i] = [(texto, cor, t0), (texto, cor, t0)] da coluna i; vira[i] = instante da virada"""
    vira = vira or [None] * len(nomes)
    for i, (nome, x) in enumerate(zip(nomes, xs)):
        cabeca(c, t, tn[i], nome, x, y, 54, CLARO if escuro else None, larg=larg)
        coluna(c, t, x, y, linhas[i], vira[i], size=size)


def sit(c, t, t0, n):
    """cabeçalho da situação: número na esfera e a palavra"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 40, 150, 46, a=a), centro(c, str(n), XE + 40, 172, 60, "g", E.SOBRE, a),
                                      E.escreve(c, "situação", XE + 110, 172, 64, "i", COR, a)))


def faixa(c, t, t0, x, y, w, a_fim=None, cor=None):
    """realce leve de uma linha da tabela"""
    p = ep(t, t0, 0.5) * (1 - (ep(t, a_fim, 0.4) if a_fim is not None else 0))
    if p > 0:
        M.rrect(c, x, y - 70, w, 140, 70, cor or E.COR, 0.10 * p)


def grade_q(c, t, t0, cols, lins, x, y, s, cor_fn=None, dur=1.2, a=1.0):
    n = cols * lins
    for r in range(lins):
        for k in range(cols):
            i = r * cols + k
            q = ep(t, t0 + dur * i / max(1, n), 0.3) * a
            if q > 0:
                M.rrect(c, x + k * s + 2, y + r * s + 2, s - 4, s - 4, s * 0.12, cor_fn(r, k) if cor_fn else E.COR, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    E.frase(c, t, ka, [("5", "g", 150, COR)] + ps("situações", "i", 120), W / 2, 330, "center", 0.14)
    for i in range(5):
        E.foco(c, t, ka + 0.6 + 0.25 * i, 0.5, lambda a, i=i: (E.bola(c, 560 + i * 200, 470, 60, a=a), centro(c, str(i + 1), 560 + i * 200, 496, 72, "g", E.SOBRE, a)))
    E.frase(c, t, kb, ps("que", "i", 96) + [("tipo de relação", "g", 96, COR)] + ps("é essa?", "i", 96), W / 2, 720, "center", 0.12)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "pause e resolva antes", W / 2, 900, 64, "g", cor=E.SOBRE, a=a))


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.2, ps("suas", "i", 84) + [("ferramentas", "g", 84, COR)], XE, 190, passo=0.12)
    itens = (("s02.a", "teste do dobro", "direta, inversa ou nenhuma"), ("s02.b", "direta", "produto cruzado"),
             ("s02.c", "inversa", "multiplique na linha"), ("s02.d", "composta", "cada coluna com a do x"),
             ("s02.e", "área", "lado × 2, área × 4"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 330 + i * 140
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 24, 42, a=a), centro(c, str(i + 1), XE + 40, y - 4, 52, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 64)], XE + 110, y)
        E.frase(c, t, C[k] + 0.3, ps(l2, "i", 60, COR), 820, y, passo=0.06)
    E.frase(c, t, C["s02.end"] - 2.4, ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), 1100, 1030, "left", 0.1)


# ---------------- situação 1: nenhuma ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3, e3 = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"], C["s03.e"]
    sit(c, t, a3, 1)
    E.frase(c, t, b3, [("R$ 30", "g", 80, COR)] + ps("de despacho", "i", 76), XE, 340, passo=0.12)
    E.frase(c, t, c3, [("+ R$ 4", "g", 80, COR)] + ps("por quilo", "i", 76), XE, 480, passo=0.12)
    E.frase(c, t, d3, ps("5 kg:", "g", 80) + [("R$ 50", "g", 80, TINTA)], XE, 660, passo=0.12)
    E.frase(c, t, e3, ps("10 kg:", "g", 80) + [("?", "g", 80, CINZA)], XE, 800, passo=0.12)
    E.relogio(c, t, C["s04.a"], 1450, 470, 200)


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    sit(c, t, C["s05"], 1)
    fcen(c, t, a5, "10 kg: R$ 100?", 560, 380, 84, ERRADO)
    if t >= b5:
        E.risco(c, 290, 400, 830, 320, t, b5, largura=12)
    E.frase(c, t, b5, ps("o despacho", "i", 60) + ps("não dobra", "g", 60, ERRADO), 560, 490, "center", 0.1)
    fcen(c, t, c5, "10 · 4 = 40", 560, 640, 90, TINTA)
    fcen(c, t, d5 - 0.3, "40 + 30 =", 470, 800, 90, TINTA)
    E.foco(c, t, d5, 0.5, lambda a: E.pilula(c, "R$ 70", 800, 770, 76, "g", fundo=CERTO, cor=BR, a=a))
    if t < C["s06"]:
        return
    a6, b6, c6, d6, e6 = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
    M.line(c, 1040, 260, 1040, 900, FIO, ep(t, C["s06"], 0.4), 3)
    XR = 1460
    E.frase(c, t, a6, ps("peso × 2,", "g", 60) + ps("preço não", "i", 60), XR, 330, "center", 0.1)
    E.foco(c, t, b6, 0.5, lambda a: E.pilula(c, "não é proporcional", XR, 450, 60, "g", fundo=ERRADO, cor=BR, a=a))
    E.frase(c, t, c6, ps("regra de três", "i", 56) + ps("dá errado", "g", 56, ERRADO), XR, 570, "center", 0.1)
    fcen(c, t, d6, "0 kg: R$ 30", XR, 710, 76, TINTA)
    E.foco(c, t, d6 + 1.0, 0.5, lambda a: centro(c, "como a bandeirada do táxi", XR, 790, 46, "i", TINTA2, a))
    E.foco(c, t, e6, 0.5, lambda a: E.pilula(c, "primeiro, o tipo de relação", XR, 920, 54, "g", cor=E.SOBRE, a=a))


# ---------------- situação 2: direta ----------------
XS2 = (360, 720)
NOMES2 = ("farinha (kg)", "pães")


def b_questao2(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    sit(c, t, a7, 2)
    tabela_n(c, t, NOMES2, (b7, b7 + 0.3), [[("4", TINTA, b7 + 1.6), ("9", TINTA, c7 + 0.8)], [("96", TINTA, b7 + 0.8), ("?", CINZA, c7 + 0.3)]], XS2)
    E.frase(c, t, b7 + 3.0, ps("sempre a", "i", 60) + ps("mesma receita", "g", 60, COR), XE, 860, passo=0.1)
    E.relogio(c, t, C["s08.a"], 1450, 470, 200)


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9, e9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"], C["s09.e"]
    a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
    sit(c, t, C["s09"], 2)
    t0 = C["s09"]
    tabela_n(c, t, NOMES2, (t0, t0), [[("4", TINTA, t0), ("9", TINTA, t0)], [("96", TINTA, t0), ("x", COR, t0)]], XS2)
    seta(c, t, a9, XS2[0] + 140, 300)
    seta(c, t, a9 + 0.3, XS2[1] + 140, 300)
    tipo(c, t, b9, "direta", 540, 800)
    XR = 1400

    def colunas_():
        fcen(c, t, c9, "f{96}{x} = f{4}{9}", XR, 400, 100, TINTA)
        fcen(c, t, d9, "4 · x = 96 · 9 = 864", XR, 600, 80, TINTA)
        E.foco(c, t, e9, 0.5, lambda a: E.pilula(c, "x = 216 pães", XR, 760, 70, "g", fundo=CERTO, cor=BR, a=a))
    E.saida(c, t, a10 - 0.2, colunas_)
    if t >= a10 - 0.2:
        E.frase(c, t, a10 - 0.1, ps("pelo valor de", "i", 60) + ps("1 quilo", "g", 60, COR), XR, 300, "center", 0.1)
        fcen(c, t, a10, "96 ÷ 4 = 24", XR, 460, 90, TINTA)
        E.foco(c, t, a10 + 0.8, 0.5, lambda a: centro(c, "pães por quilo", XR, 530, 48, "i", TINTA2, a))
        fcen(c, t, b10, "24 · 9 = 216", XR, 680, 90, COR)
        E.foco(c, t, c10, 0.5, lambda a: E.pilula(c, "o mesmo lugar", XR, 840, 64, "g", fundo=CERTO, cor=BR, a=a))


# ---------------- situação 3: inversa ----------------
XS3 = (360, 720)
NOMES3 = ("km/h", "horas")


def b_questao3(c, t, C, b):
    a11, b11, c11, d11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
    sit(c, t, a11, 3)
    tabela_n(c, t, NOMES3, (b11 - 0.2, c11 - 0.2), [[("90", TINTA, b11), ("120", TINTA, d11)], [("4", TINTA, c11), ("?", CINZA, d11 + 1.2)]], XS3)
    E.frase(c, t, d11 + 2.0, ps("a", "i", 60) + ps("mesma viagem", "g", 60, COR), XE, 860, passo=0.1)
    E.relogio(c, t, C["s12.a"], 1450, 470, 200)


def b_resposta3(c, t, C, b):
    a13, b13, c13, d13, e13, f13 = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"], C["s13.f"]
    sit(c, t, C["s13"], 3)
    t0 = C["s13"]
    tabela_n(c, t, NOMES3, (t0, t0), [[("90", TINTA, t0), ("120", TINTA, t0)], [("4", TINTA, t0), ("x", COR, t0)]], XS3)
    seta(c, t, a13, XS3[0] + 140, 300, cor=TINTA)
    seta(c, t, a13 + 0.3, XS3[1] + 140, 300, desce=False)
    tipo(c, t, b13, "inversa", 540, 800)
    faixa(c, t, c13, 230, 300 + DY3, 620)
    faixa(c, t, d13, 230, 300 + 2 * DY3, 620)
    XR = 1400
    fcen(c, t, c13, "90 · 4 = 360", XR, 380, 90, TINTA)
    fcen(c, t, d13, "= 120 · x", XR, 520, 90, TINTA)
    E.foco(c, t, e13, 0.5, lambda a: E.pilula(c, "x = 3 horas", XR, 690, 70, "g", fundo=CERTO, cor=BR, a=a))
    E.frase(c, t, f13 - 1.4, ps("mais rápido,", "i", 60) + ps("menos tempo", "g", 60, COR), XR, 850, "center", 0.1)
    E.foco(c, t, f13, 0.5, lambda a: E.selo(c, XR, 950, 40, True, a))


# ---------------- situação 4: composta com inversas ----------------
XS4 = (300, 610, 920)
NOMES4 = ("pintores", "horas/dia", "dias")


def b_questao4(c, t, C, b):
    a14, b14, c14 = C["s14.a"], C["s14.b"], C["s14.c"]
    sit(c, t, a14, 4)
    tabela_n(c, t, NOMES4, (b14, b14 + 0.8, b14 + 1.8),
             [[("6", TINTA, b14 + 0.3), ("8", TINTA, c14 + 0.3)], [("8", TINTA, b14 + 1.2), ("10", TINTA, c14 + 1.3)],
              [("20", TINTA, b14 + 2.4), ("?", CINZA, c14 + 2.4)]], XS4, larg=250)
    E.frase(c, t, c14 + 3.0, ps("o", "i", 60) + ps("mesmo prédio", "g", 60, COR), XE, 860, passo=0.1)
    E.relogio(c, t, C["s15.a"], 1480, 470, 200)


def b_resposta4(c, t, C, b):
    a16, b16, c16, d16, e16, f16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"], C["s16.f"]
    sit(c, t, C["s16"], 4)
    t0 = C["s16"]
    xs = (270, 560, 850)
    tabela_n(c, t, NOMES4, (t0, t0, t0), [[("6", TINTA, t0), ("8", TINTA, t0)], [("8", TINTA, t0), ("10", TINTA, t0)], [("20", TINTA, t0), ("x", COR, t0)]],
             xs, larg=240, size=96, vira=(c16 - 0.4, c16 - 0.4, None))
    seta(c, t, t0 + 0.5, xs[2] + 120, 300)
    for i, tt in enumerate((a16, b16)):
        v = ep(t, c16 - 0.4, 0.9)
        seta(c, t, tt, xs[i] + 120, 300, desce=False, cor=TINTA, a=1 - v)
        seta(c, t, c16 + 0.3, xs[i] + 120, 300, cor=TINTA)
        tipo(c, t, tt + 0.4, "inversa", xs[i], 780)
    XR = 1440
    fcen(c, t, c16, "f{20}{x} = f{8}{6} · f{10}{8}", XR, 400, 90, TINTA)
    fcen(c, t, d16, "= f{80}{48} = f{5}{3}", XR, 600, 90, TINTA)
    E.foco(c, t, e16, 0.5, lambda a: E.pilula(c, "x = 12 dias", XR, 770, 70, "g", fundo=CERTO, cor=BR, a=a))
    E.frase(c, t, f16 - 1.2, ps("mais gente e mais horas,", "i", 54) + ps("menos dias", "g", 56, COR), XR, 920, "center", 0.08)


def b_atalho(c, t, C, b):
    palco(c, t)
    a17, b17, c17, d17 = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, C["s17"] + 0.2, ps("o atalho:", "i", 72, CLARO), W / 2, 170, "center", 0.12)
    E.frase(c, t, a17, ps("mesmo prédio,", "i", 72, CLARO) + ps("mesmas horas de trabalho", "g", 72, BR), W / 2, 290, "center", 0.12)
    xs = (300, 560, 820)
    for nome, x in zip(NOMES4, xs):
        cabeca(c, t, a17, nome, x, 400, 46, CLARO, 220)
    for j, (vals, t0) in enumerate(((("6", "8", "20"), b17), (("8", "10", "x"), c17))):
        y = 400 + DY3 * (j + 1)
        p = ep(t, t0, 0.5)
        if p > 0:
            M.rrect(c, 190, y - 70, 740, 140, 70, CLARO, 0.16 * p)
        for k, (v, x) in enumerate(zip(vals, xs)):
            fcen(c, t, t0 + 0.15 * k, v, x, y + 36, 100, CLARO if v == "x" else BR)
        for k in (0, 1):
            E.foco(c, t, t0 + 0.4, 0.4, lambda a, k=k, y=y: centro(c, "·", (xs[k] + xs[k + 1]) / 2, y + 30, 90, "g", CLARO, a))
    fcen(c, t, b17 + 0.6, "6 · 8 · 20 = 960", 1440, 560, 84, BR)
    fcen(c, t, c17 + 0.6, "8 · 10 · x = 80x", 1440, 720, 84, BR)
    E.foco(c, t, d17, 0.5, lambda a: E.pilula(c, "x = 960 ÷ 80 = 12", 1440, 880, 64, "g", cor=BR, a=a))


# ---------------- situação 5: quadrado ----------------
def b_questao5(c, t, C, b):
    a18, b18, c18, d18, e18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"], C["s18.e"]
    sit(c, t, a18, 5)
    grade_q(c, t, b18, 5, 5, 240, 300, 64)
    E.foco(c, t, b18 + 0.5, 0.5, lambda a: centro(c, "5 m", 400, 680, 56, "g", TINTA2, a))
    E.foco(c, t, c18, 0.5, lambda a: E.pilula(c, "R$ 100", 400, 780, 70, "g", cor=E.SOBRE, a=a))
    E.frase(c, t, d18, ps("preço", "i", 64) + ps("pela área", "g", 64, COR), 680, 420, passo=0.1)
    E.frase(c, t, e18, ps("lado × 2:", "g", 70) + ps("quanto custa?", "i", 70, COR), 680, 580, passo=0.1)
    E.relogio(c, t, C["s19.a"], 1560, 470, 180)


def b_resposta5(c, t, C, b):
    a20, b20, c20 = C["s20.a"], C["s20.b"], C["s20.c"]
    a21, b21, c21 = C["s21.a"], C["s21.b"], C["s21.c"]
    sit(c, t, C["s20"], 5)
    XR = 1360

    def raciocinio():
        fcen(c, t, a20, "R$ 200?", XR, 380, 90, ERRADO)
        if t >= b20:
            E.risco(c, XR - 200, 400, XR + 200, 320, t, b20, largura=12)
        fcen(c, t, b20, "lado × 2: área × 4", XR, 560, 80, COR)
        fcen(c, t, c20 - 0.3, "100 · 4 =", XR - 130, 740, 90, TINTA)
        E.foco(c, t, c20, 0.5, lambda a: E.pilula(c, "R$ 400", XR + 230, 710, 72, "g", fundo=CERTO, cor=BR, a=a))
    E.saida(c, t, C["s21"] - 0.1, raciocinio)
    # a lona grande: 10 × 10, com os quatro blocos de 5 × 5
    k = 5
    grade_q(c, t, C["s20"] + 0.2, 5, 5, 200, 290, 54)
    if t >= b20:
        for r in range(10):
            for j in range(10):
                if r < 5 and j < 5:
                    continue
                q = ep(t, b20 + 0.012 * (r * 10 + j), 0.3)
                if q > 0:
                    cor = E.COR if ((r // k) + (j // k)) % 2 == 0 else CLARA
                    M.rrect(c, 200 + j * 54 + 2, 290 + r * 54 + 2, 50, 50, 6, cor, q)
    if t >= C["s21"]:
        fcen(c, t, a21, "5 · 5 = 25 m²", XR, 340, 80, TINTA)
        E.foco(c, t, a21 + 1.0, 0.5, lambda a: centro(c, "R$ 100 ÷ 25 = R$ 4 por m²", XR, 420, 48, "g", TINTA2, a))
        fcen(c, t, b21, "10 · 10 = 100 m²", XR, 580, 80, TINTA)
        fcen(c, t, c21, "100 · 4 = R$ 400", XR, 760, 90, COR)
        E.foco(c, t, c21 + 1.0, 0.5, lambda a: E.pilula(c, "bateu!", XR, 900, 64, "g", fundo=CERTO, cor=BR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", "primeiro, o tipo de relação"), ("s22.b", "depois, a conta"), ("s22.c", "faz sentido?"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                          centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.2, ps("próxima aula", "i", 84), XE, 280)
    E.frase(c, t, C["s23.a"], [("divisão proporcional", "g", 120, COR)], XE, 430)
    E.frase(c, t, C["s23.b"], ps("R$ 1.200", "g", 70) + ps("na razão", "i", 70) + ps("3 para 5", "g", 70), XE, 570, passo=0.12)
    E.frase(c, t, C["s23.c"], ps("o lucro entre sócios", "i", 70), XE, 680, passo=0.12)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1580, 190, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1710, p), lerp(430, 220, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              atalho=b_atalho, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
