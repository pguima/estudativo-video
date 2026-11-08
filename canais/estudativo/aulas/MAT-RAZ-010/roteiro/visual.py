"""Visual — Estudativo · MAT-RAZ-010: proporcional ao quadrado.
Peças locais: grade de quadradinhos de 1 m² (entra linha a linha; blocos em dois tons mostram os quadrados iguais ao
primeiro), cotas com fio e pontas, a foto ampliada e a tabela da trilha (nome em itálico com fio, valores, seta ao lado).
Todo instante vem de C[...]: sem voz, os tempos são provisórios e o visual segue os marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Razão e Proporção")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-RAZ-010_proporcional_ao_quadrado.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("area", "regra", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 3 * 3 == 9 and 6 * 6 == 36 == 4 * 9 and 9 * 9 == 81 and 3 * 2 == 6 and 6 * 4 == 24 == 4 * 6 and 6 * 2 == 12
assert 10 * 15 == 150 and 30 * 45 == 1350 == 9 * 150 and 150 * 3 == 450 and 16 * 9 == 144 == 12 * 12


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


CLARA = E.mix(E.COR, "#FFFFFF", 0.5)  # o segundo tom dos blocos


def grade_q(c, t, t0, cols, lins, x, y, s, cor_fn=None, dur=1.2, a=1.0):
    """quadradinhos de lado s (px) a partir do canto (x, y), entrando linha a linha em `dur` segundos"""
    if a <= 0:
        return
    n = cols * lins
    for r in range(lins):
        for k in range(cols):
            i = r * cols + k
            q = ep(t, t0 + dur * i / max(1, n), 0.3) * a
            if q <= 0:
                continue
            cor = cor_fn(r, k) if cor_fn else E.COR
            M.rrect(c, x + k * s + 2, y + r * s + 2, s - 4, s - 4, s * 0.12, cor, q)


def cota_h(c, t, t0, txt, x0, x1, y, cor=None, size=48):
    """medida embaixo de um lado: fio com pontas e o texto centrado"""
    def f(a):
        M.line(c, x0, y, x1, y, cor or TINTA2, a, 3)
        M.line(c, x0, y - 12, x0, y + 12, cor or TINTA2, a, 3)
        M.line(c, x1, y - 12, x1, y + 12, cor or TINTA2, a, 3)
        centro(c, txt, (x0 + x1) / 2, y + size + 8, size, "g", cor or TINTA2, a)
    E.foco(c, t, t0, 0.5, f)


def cota_v(c, t, t0, txt, x, y0, y1, cor=None, size=48):
    """medida à esquerda de um lado: fio com pontas e o texto à esquerda"""
    def f(a):
        M.line(c, x, y0, x, y1, cor or TINTA2, a, 3)
        M.line(c, x - 12, y0, x + 12, y0, cor or TINTA2, a, 3)
        M.line(c, x - 12, y1, x + 12, y1, cor or TINTA2, a, 3)
        E.escreve(c, txt, x - 24 - E.larg(txt, "g", size), (y0 + y1) / 2 + size * 0.36, size, "g", cor or TINTA2, a)
    E.foco(c, t, t0, 0.5, f)


def blocos(k):
    """cor por bloco k × k: tons alternados, para ver os quadrados iguais ao primeiro"""
    return lambda r, c_: E.COR if ((r // k) + (c_ // k)) % 2 == 0 else CLARA


def foto(c, x, y, w, h, a=1.0, cor=None):
    """foto: moldura clara, montanha e sol"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 10, "#FFFFFF", a)
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x + 8, y + 8, w - 16, h - 16))
    M.rrect(c, x + 8, y + 8, w - 16, h - 16, 4, CLARA, a)
    p = skia.Path(); p.moveTo(x + 8, y + h - 8); p.lineTo(x + w * 0.4, y + h * 0.5); p.lineTo(x + w * 0.62, y + h * 0.72)
    p.lineTo(x + w * 0.8, y + h * 0.58); p.lineTo(x + w - 8, y + h - 8); p.close()
    c.drawPath(p, M.paint(cor or E.COR, a))
    c.drawCircle(x + w * 0.72, y + h * 0.28, min(w, h) * 0.1, M.paint("#FFD500", a))
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 10, 10), M.paint(TINTA, a, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        grade_q(c, t, ka, 3, 3, 200, 420, 70)
        cota_h(c, t, ka + 0.6, "3 m", 200, 410, 660)
        E.foco(c, t, lerp(ka, kb, 0.6), 0.5, lambda a: centro(c, "9 m²", 305, 360, 72, "g", COR, a))
        grade_q(c, t, kb, 6, 6, 640, 230, 70, blocos(3) if t >= kd else None)
        cota_h(c, t, kb + 0.6, "6 m", 640, 1060, 680)
        E.frase(c, t, kb + 0.3, ps("o dobro", "i", 76) + ps("do lado", "g", 76, COR), 1180, 330, passo=0.12)
        E.foco(c, t, lerp(kb, kc, 0.5), 0.5, lambda a: E.escreve(c, "18 m²?", 1180, 520, 120, "g", ERRADO, a))
        if t >= kc:
            E.risco(c, 1170, 540, 1560, 420, t, kc, largura=14)
            E.foco(c, t, kd, 0.5, lambda a: E.escreve(c, "36 m²", 1180, 720, 150, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1500, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), ps("dobrar o lado", "i", 96) + [], XE, 450, passo=0.12)
        E.frase(c, t, lerp(ta, tb, 0.55), [("quadruplica", "g", 110, COR)], XE, 600)
        E.frase(c, t, lerp(ta, tb, 0.7), ps("a área", "i", 96), XE, 730, passo=0.12)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("lembre de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 880
    itens = (("s03.b", "1 metro quadrado é um quadradinho", "de 1 m de lado"), ("s03.c", "o teste", "do dobro"),
             ("s03.d", "potência de uma multiplicação", "(2 · L)² = 2² · L²"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 160)
    alvo = [C[k] for k, _, _ in itens]
    q1, q2 = ease_io(prog(t, alvo[1] - 0.35, 0.5)), ease_io(prog(t, alvo[2] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(340, 580, q1), 820, q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), 900, 1000, "left", 0.12)


# ---------------- área do quadrado ----------------
GX, GY, GS = 220, 300, 100  # canto da grade e lado do quadradinho


def b_area(c, t, C, b):
    a4, b4, c4, d4, e4 = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]
    a5, b5, c5, d5 = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7, d7 = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
    XR = 1360
    # a grade: 3 × 3 e depois 6 × 6, com os quatro blocos em tons alternados
    cores = blocos(3) if t >= c5 else (lambda r, k: E.COR if r < 3 and k < 3 else CLARA)
    if t < a5:
        grade_q(c, t, b4, 3, 3, GX, GY, GS)
    else:
        grade_q(c, t, b4, 3, 3, GX, GY, GS, cores)
        for r in range(6):
            for k in range(6):
                if r < 3 and k < 3:
                    continue
                q = ep(t, a5 + 0.04 * (r * 6 + k), 0.3)
                if q > 0:
                    M.rrect(c, GX + k * GS + 2, GY + r * GS + 2, GS - 4, GS - 4, GS * 0.12, cores(r, k), q)
    if t < a5:
        cota_h(c, t, b4, "3 m", GX, GX + 3 * GS, GY + 3 * GS + 30)
        cota_v(c, t, b4 + 0.3, "3 m", GX - 30, GY, GY + 3 * GS)
    else:
        cota_h(c, t, a5, "6 m", GX, GX + 6 * GS, GY + 6 * GS + 30)
        cota_v(c, t, a5 + 0.3, "6 m", GX - 30, GY, GY + 6 * GS)

    def textos4():
        E.frase(c, t, C["s04"] + 0.2, ps("área =", "i", 72) + ps("quantos quadradinhos cabem", "g", 64, COR), W / 2, 190, "center", 0.1)
        fcen(c, t, c4, "3 · 3 = 9 m²", XR, 470, 100, TINTA)
        fcen(c, t, d4, "lado · lado", XR, 650, 84, TINTA2)
        E.foco(c, t, e4, 0.5, lambda a: E.pilula(c, "área = lado²", XR, 800, 72, "g", cor=E.SOBRE, a=a))
    E.saida(c, t, a5 - 0.1, textos4)

    def textos5():
        E.frase(c, t, a5, ps("dobre o lado:", "i", 72) + ps("6 m", "g", 72, COR), XR, 190, "center", 0.12)
        fcen(c, t, b5, "6 · 6 = 36 m²", XR, 420, 100, TINTA)
        E.frase(c, t, c5, ps("cabem", "i", 64) + ps("4 quadrados", "g", 64, COR) + ps("iguais ao primeiro", "i", 64), XR, 580, "center", 0.1)
        fcen(c, t, d5, "36 = 4 · 9", XR, 760, 110, COR)
    if a5 <= t:
        E.saida(c, t, C["s06"] - 0.1, textos5)

    def textos6():
        E.frase(c, t, a6 - 0.6, ps("por que 4?", "i", 72), XR, 190, "center", 0.12)
        E.frase(c, t, a6, ps("o lado aparece", "i", 64) + ps("2 vezes", "g", 64, COR) + ps("na conta", "i", 64), XR, 380, "center", 0.1)
        E.frase(c, t, b6, ps("largura × 2", "g", 64) + ps("e", "i", 64) + ps("altura × 2", "g", 64), XR, 540, "center", 0.12)
        fcen(c, t, c6, "2 · 2 = 4", XR, 740, 120, COR)
    if C["s06"] <= t:
        E.saida(c, t, C["s07"] - 0.1, textos6)
    # as setas do dobro na largura e na altura
    p = ep(t, b6, 0.6) * (1 - ep(t, C["s07"] - 0.1, 0.4))
    if p > 0:
        M.arrow(c, GX, GY - 40, GX + 6 * GS * p, GY - 40, E.COR, 1.0, 7, 24, 1.0)
        M.arrow(c, GX + 6 * GS + 40, GY, GX + 6 * GS + 40, GY + 6 * GS * p, E.COR, 1.0, 7, 24, 1.0)
        centro(c, "× 2", GX + 3 * GS, GY - 64, 52, "g", COR, p)
        E.escreve(c, "× 2", GX + 6 * GS + 60, GY + 3 * GS + 18, 52, "g", COR, p)

    if t >= C["s07"]:
        E.frase(c, t, C["s07"] + 0.2, ps("com", "i", 72) + ps("potência", "g", 72, COR), XR, 190, "center", 0.12)
        fcen(c, t, a7, "lado novo = 2 · L", XR, 360, 80, TINTA)
        fcen(c, t, b7, "área nova = (2 · L)^2", XR, 520, 80, TINTA)
        fcen(c, t, c7, "= 2^2 · L^2", XR, 670, 90, TINTA)
        E.foco(c, t, d7, 0.5, lambda a: E.pilula(c, "= 4 · área antiga", XR, 830, 70, "g", cor=E.SOBRE, a=a))


# ---------------- a regra ----------------
def b_regra(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]

    def oito():
        E.frase(c, t, C["s08"] + 0.2, ps("teste do", "i", 72) + ps("dobro", "g", 72, COR), XE, 170, passo=0.12)
        xs = (400, 760, 1120)
        for i, (nome, v1, v2, t0, cor) in enumerate((("lado", "3", "6", a8, TINTA), ("área", "9", "36", a8 + 1.2, TINTA), ("lado · lado", "9", "36", c8, COR))):
            cabeca(c, t, t0, nome, xs[i], 330, 56, larg=260)
            coluna(c, t, xs[i], 330, [(v1, cor, t0 + 0.3), (v2, cor, t0 + 0.5)])
        for x, txt, t0 in ((xs[0], "× 2", a8 + 0.8), (xs[1], "× 4", a8 + 1.8), (xs[2], "× 4", c8 + 0.8)):
            seta(c, t, t0, x + 130, 330)
            E.foco(c, t, t0, 0.5, lambda a, x=x, txt=txt: E.escreve(c, txt, x + 150, 330 + DY3 * 1.5 + 18, 52, "g", COR, a))
        E.foco(c, t, b8, 0.5, lambda a: E.pilula(c, "não é proporcional ao lado", 1320, 150, 50, "g", fundo=ERRADO, cor=BR, a=a))
        E.frase(c, t, c8, ps("proporcional", "i", 80) + ps("ao quadrado do lado", "g", 80, COR), W / 2, 880, "center", 0.12)
    E.saida(c, t, C["s09"] - 0.1, oito)

    def nove():
        a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
        E.frase(c, t, a9, ps("lado", "i", 96) + ps("× k", "g", 96, TINTA), 500, 360, "center", 0.12)
        p = ep(t, b9 - 0.2, 0.5)
        if p > 0:
            M.arrow(c, 760, 330, 760 + 240 * p, 330, E.COR, 1.0, 7, 24, 1.0)
        E.foco(c, t, b9, 0.5, lambda a: E.formula(c, "área × k^2", 1100, 360, 96, "g", COR, a))
        fcen(c, t, c9, "lado × 3: área × 9", W / 2, 600, 90, TINTA)
        fcen(c, t, d9, "9 · 9 = 81 m²", W / 2, 800, 100, COR)
        E.foco(c, t, d9 + 0.8, 0.5, lambda a: centro(c, "9 vezes a área do começo", W / 2, 900, 56, "i", TINTA2, a))
    if C["s09"] <= t:
        E.saida(c, t, C["s10"] - 0.1, nove)

    def dez():
        a10, b10, c10 = C["s10.a"], C["s10.b"], C["s10.c"]
        E.frase(c, t, C["s10"] + 0.2, ps("e para", "i", 80) + ps("menos", "g", 80, COR), W / 2, 220, "center", 0.12)
        fcen(c, t, a10, "lado × f{1}{2}", 560, 470, 110, TINTA)
        fcen(c, t, b10, "(f{1}{2})^2 = f{1}{4}", 1300, 470, 110, TINTA)
        E.foco(c, t, c10, 0.5, lambda a: E.pilula(c, "área ÷ 4", 760, 760, 80, "g", cor=E.SOBRE, a=a))
        E.frase(c, t, c10 + 0.8, ps("não é", "i", 76) + ps("a metade", "g", 76, ERRADO), 1300, 785, "center", 0.12)
        # o quadrado e o quadradinho de lado pela metade: 1 de 4 partes
        q = ep(t, c10, 0.5)
        if q > 0:
            x0, y0, l = 1650, 640, 180
            M.rrect(c, x0, y0, l, l, 8, CLARA, q)
            M.rrect(c, x0, y0, l / 2, l / 2, 6, E.COR, q)
    if C["s10"] <= t:
        E.saida(c, t, C["s11"] - 0.1, dez)

    if t >= C["s11"]:
        a11, b11, c11, d11, e11 = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"]
        E.frase(c, t, a11, ps("qualquer figura", "i", 72) + ps("ampliada por inteiro", "g", 72, COR), W / 2, 170, "center", 0.12)
        s = 70
        grade_q(c, t, b11, 3, 2, 240, 330, s)
        cota_h(c, t, b11 + 0.3, "3 m", 240, 240 + 3 * s, 330 + 2 * s + 26, size=40)
        cota_v(c, t, b11 + 0.3, "2 m", 216, 330, 330 + 2 * s, size=40)
        fcen(c, t, b11 + 0.8, "3 · 2 = 6 m²", 345, 620, 64, TINTA)
        grade_q(c, t, c11, 6, 4, 700, 330, s, lambda r, k: E.COR if (r // 2 + k // 3) % 2 == 0 else CLARA)
        cota_h(c, t, c11 + 0.3, "6 m", 700, 700 + 6 * s, 330 + 4 * s + 26, size=40)
        cota_v(c, t, c11 + 0.3, "4 m", 676, 330, 330 + 4 * s, size=40)
        fcen(c, t, c11 + 0.8, "6 · 4 = 24 m²", 910, 760, 64, TINTA)
        E.foco(c, t, d11, 0.5, lambda a: E.pilula(c, "4 × a área", 1520, 480, 70, "g", cor=E.SOBRE, a=a))
        E.frase(c, t, e11 - 1.6, ps("na física: frenagem e", "i", 56), 1300, 920, "center", 0.1)
        E.foco(c, t, e11, 0.5, lambda a: E.formula(c, "velocidade^2", 1700, 920, 60, "g", COR, a, "center"))
        E.foco(c, t, e11 + 1.6, 0.5, lambda a: centro(c, "outra aula", 1700, 1000, 44, "i", TINTA2, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    a12, b12, c12 = C["s12.a"], C["s12.b"], C["s12.c"]
    a13, b13, c13 = C["s13.a"], C["s13.b"], C["s13.c"]
    E.frase(c, t, a12, ps("o erro:", "i", 66) + ps("área × o mesmo número do lado", "g", 62, ERRADO), XE, 160, passo=0.1)
    # 8,8 px por cm nas duas fotos: a grande tem 3 vezes cada lado
    E.foco(c, t, b12, 0.5, lambda a: foto(c, 200, 300, 88, 132, a))
    cota_h(c, t, b12 + 0.3, "10 cm", 200, 288, 460, size=34)
    cota_v(c, t, b12 + 0.3, "15 cm", 180, 300, 432, size=34)
    fcen(c, t, b12 + 0.9, "10 · 15 = 150 cm²", 1340, 340, 76, TINTA)
    def errado():
        fcen(c, t, c12, "150 · 3 = 450?", 1340, 500, 84, ERRADO)
        if t >= a13:
            E.risco(c, 1040, 520, 1640, 440, t, a13, largura=12)
    E.saida(c, t, a13 + 1.0, errado)
    # a foto ampliada: o triplo de cada lado
    E.foco(c, t, a13, 0.6, lambda a: foto(c, 420, 300, 264, 396, a))
    cota_h(c, t, a13 + 0.3, "30 cm", 420, 684, 730, size=40)

    E.foco(c, t, a13 + 0.3, 0.5, lambda a: E.escreve(c, "45 cm", 704, 520, 40, "g", TINTA2, a))
    fcen(c, t, b13, "30 · 45 = 1.350 cm²", 1340, 640, 76, TINTA)
    fcen(c, t, c13, "9 · 150 = 1.350", 1340, 800, 90, COR)
    E.foco(c, t, c13 + 0.6, 0.5, lambda a: E.formula(c, "porque 3^2 = 9", 1340, 920, 60, "g", TINTA2, a, "center"))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a14, b14, c14, d14, e14 = C["s14.a"], C["s14.b"], C["s14.c"], C["s14.d"], C["s14.e"]

    def tabela_():
        E.frase(c, t, C["s14"] + 0.2, ps("o atalho:", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, a14, ps("fator do lado,", "i", 80, CLARO) + ps("ao quadrado", "g", 80, BR), W / 2, 290, "center", 0.12)
        cabeca(c, t, b14 - 0.3, "lado", 640, 400, 54, CLARO, 300)
        cabeca(c, t, b14 - 0.3, "área", 1180, 400, 54, CLARO, 300)
        for i, (l, ar, t0) in enumerate((("× 2", "× 4", b14), ("× 3", "× 9", c14), ("× 10", "× 100", d14))):
            y = 520 + i * 130
            fcen(c, t, t0 - 0.5, l, 640, y, 90, BR)
            p = ep(t, t0 - 0.2, 0.4)
            if p > 0:
                M.arrow(c, 790, y - 30, 790 + 220 * p, y - 30, CLARO, 1.0, 5, 20, 1.0)
            fcen(c, t, t0, ar, 1180, y, 90, CLARO)
        E.frase(c, t, e14, ps("o fator entra", "i", 60, CLARO) + ps("2 vezes:", "g", 60, BR) + ps("largura e altura", "i", 60, CLARO), W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s15"] - 0.1, tabela_)

    if t >= C["s15"]:
        a15, b15, c15, d15 = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
        E.frase(c, t, a15, ps("só vale se", "i", 72, CLARO) + ps("todas as medidas", "g", 72, BR) + ps("mudam pelo mesmo fator", "i", 72, CLARO), W / 2, 200, "center", 0.1)
        s = 70
        grade_q(c, t, b15 - 0.6, 3, 2, 260, 420, s, lambda r, k: CLARO)
        grade_q(c, t, b15, 6, 2, 620, 420, s, lambda r, k: CLARO if k < 3 else BR)
        E.foco(c, t, b15 - 0.6, 0.5, lambda a: centro(c, "3 por 2", 365, 620, 48, "i", CLARO, a))
        E.foco(c, t, b15, 0.5, lambda a: centro(c, "6 por 2", 830, 620, 48, "i", CLARO, a))
        fcen(c, t, c15, "6 m² vira 12 m²", 1450, 520, 90, BR)
        E.foco(c, t, c15 + 0.6, 0.5, lambda a: centro(c, "só dobra", 1450, 620, 60, "g", ERRADO, a))
        E.frase(c, t, d15 - 2.0, ps("caixa ampliada: volume segue o", "i", 60, CLARO) + ps("cubo", "g", 60, BR), W / 2, 820, "center", 0.1)
        E.foco(c, t, d15, 0.5, lambda a: E.pilula(c, "outra aula", W / 2, 930, 52, "g", cor=BR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a16, b16, c16 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    grade_q(c, t, a16, 4, 4, 230, 300, 70)
    cota_h(c, t, a16 + 0.5, "4 m", 230, 510, 610, size=44)
    fcen(c, t, a16 + 1.4, "16 m²", 370, 770, 72, COR)
    E.frase(c, t, b16, ps("outro piso:", "i", 64) + ps("triplo do lado", "g", 64, COR), 640, 420, passo=0.1)
    E.frase(c, t, c16, ps("quantos", "i", 76) + ps("m²?", "g", 76, COR), 640, 560, passo=0.12)
    E.relogio(c, t, C["s17.a"], 1600, 470, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a18, b18, c18, d18 = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]
    XR = 1380
    fcen(c, t, a18 - 0.6, "lado × 3", XR, 230, 84, TINTA)
    fcen(c, t, a18, "área × 3^2 = 9", XR, 370, 84, COR)
    fcen(c, t, b18, "16 · 9 = 144 m²", XR, 540, 90, TINTA)
    fcen(c, t, c18, "lado novo: 12 m", XR, 720, 76, TINTA2)
    fcen(c, t, d18, "12 · 12 = 144", XR, 860, 90, TINTA)
    E.foco(c, t, d18 + 1.0, 0.5, lambda a: E.pilula(c, "bateu!", XR, 980, 64, "g", fundo=CERTO, cor=BR, a=a))
    # 12 × 12: nove blocos de 4 × 4, cada um igual ao piso antigo
    grade_q(c, t, a18, 12, 12, 200, 220, 54, blocos(4), dur=2.0)
    cota_h(c, t, c18, "12 m", 200, 200 + 12 * 54, 220 + 12 * 54 + 26, size=44)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s19.a", "área = lado · lado"), ("s19.b", "o fator entra 2 vezes"), ("s19.c", "lado × 2, área × 4"))
        for i, (k, s) in enumerate(itens):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 330, y - 30, 56, a=a),
                                                          centro(c, str(i + 1), 330, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 430, y)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a20, b20 = C["s20.a"], C["s20.b"]
    E.frase(c, t, C["s20"] + 0.2, ps("próxima aula", "i", 84), XE, 260)
    E.frase(c, t, a20, ps("ler uma", "i", 90) + [("fórmula", "g", 100, COR)], XE, 400, passo=0.12)
    E.foco(c, t, a20 + 1.0, 0.5, lambda a: E.formula(c, "R = k · f{L}{A}", XE, 600, 110, "g", TINTA, a))
    E.frase(c, t, b20, ps("L dobra,", "g", 64, COR) + ps("A cai pela metade", "g", 64, COR), XE, 760, passo=0.12)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1530, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1660, p), lerp(560, 360, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 960, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, area=b_area, regra=b_regra, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
