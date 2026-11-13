"""Visual — Estudativo · QUI-LIG-004: qual é a ligação e o que ela explica.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha (QUI-LIG-001). Peça própria: o TESTE DE CONDUTIVIDADE
(teste()): lâmpada no alto, fios em tinta até dois eletrodos que mergulham na amostra; acesa = amarelo com brilho, apagada
= vidro cinza. As três ligações têm sempre o mesmo desenho: iônica = retículo de Na⁺/Cl⁻, covalente = moléculas
bola-vareta, metálica = íons + em fileiras com elétrons azuis. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-004_qual_e_a_ligacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("regra", "conduz", "fusao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMARELO = "#FFD23F"
PF = {"NaCl": 801, "Fe": 1538, "gelo": 0, "Hg": -39, "Al": 660, "KCl": 770, "etanol": -114}
assert PF["NaCl"] > PF["gelo"] and PF["Fe"] > PF["NaCl"] and PF["Al"] > 0 > PF["etanol"]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def ion(c, cx, cy, r, el, s, a=1.0, escuro=False):
    if a <= 0:
        return
    Q.atomo(c, cx, cy, r, el, a, rotulo=False, escuro=escuro)
    Q.formula(c, s, cx, cy + r * 0.3, r * 0.82, BR, a, "center")


def reticulo(c, t, t0, x, y, cols, rows, passo=80, r1=24, r2=34, onda=0.05, a=1.0, rotulo=True):
    for i in range(rows):
        for j in range(cols):
            q = ease_back(prog(t, t0 + (i + j) * onda, 0.35))
            if q > 0:
                na = (i + j) % 2 == 0
                ion(c, x + j * passo, y + i * passo, (r1 if na else r2) * q, "Na" if na else "Cl", ("Na^+" if na else "Cl^-") if rotulo else "", a)


def _h(k, s=1.0):
    v = math.sin(k * 12.9898 + s * 78.233) * 43758.5453
    return v - math.floor(v)


def metal(c, t, t0, x, y, cols, rows, p=80, r=26, el="Fe", fluxo=None, a=1.0, escuro=False):
    if t < t0:
        return
    for i in range(rows):
        for j in range(cols):
            q = ease_back(prog(t, t0 + (i + j) * 0.04, 0.35))
            if q > 0:
                Q.atomo(c, x + j * p, y + i * p, r * q, el, a, rotulo=False, escuro=escuro)
                centro(c, "+", x + j * p, y + i * p + r * 0.36 * q, r * q, "g", BR, a)
    qe = ep(t, t0 + 0.6, 0.5) * a
    w, h = cols * p, rows * p
    for k in range(int(cols * rows * 0.9)):
        bx, by = x - p / 2 + _h(k, 1) * w, y - p / 2 + _h(k, 2) * h
        if fluxo is not None and t > fluxo:
            ex = x - p / 2 + ((bx - (x - p / 2) + (t - fluxo) * 140) % w)
        else:
            ex = bx + 20 * math.sin(t * (1.1 + _h(k, 3)) + 6 * _h(k, 4))
        E.bola(c, ex, by + 16 * math.sin(t * 1.3 + 6 * _h(k, 6)), 7, Q.ELETRON, qe)


def lampada(c, cx, cy, luz=0.0, a=1.0):
    """lâmpada de teste; luz 0..1"""
    if a <= 0:
        return
    if luz > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), 180, [M.hexc(AMARELO, 0.55 * luz * a), M.hexc(AMARELO, 0)], [0, 1]))
        c.drawCircle(cx, cy, 180, g)
    c.drawCircle(cx, cy, 58, M.paint(M.mix("#E8ECEF", AMARELO, luz), a))
    c.drawCircle(cx, cy, 58, M.paint("#8A9099", a, stroke=4))
    M.rrect(c, cx - 28, cy + 50, 56, 46, 8, "#9AA0A8", a)
    pth = skia.Path(); pth.moveTo(cx - 18, cy + 40); pth.lineTo(cx - 8, cy - 10); pth.lineTo(cx + 8, cy - 10); pth.lineTo(cx + 18, cy + 40)
    c.drawPath(pth, M.paint("#5A5F66" if luz < 0.5 else "#B8860B", a, stroke=4))


def teste(c, t, t0, cx, ytopo, yamostra, luz=0.0, amostra=None, a=1.0):
    """circuito de teste: lâmpada em (cx, ytopo), eletrodos que descem até yamostra; amostra(a) desenha o material"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    if amostra:
        amostra(q)
    for s_ in (-1, 1):
        xe = cx + s_ * 110
        M.line(c, cx + s_ * 30, ytopo + 96, xe, ytopo + 150, TINTA, q, 6)
        M.line(c, xe, ytopo + 150, xe, yamostra, TINTA, q, 6)
        M.rrect(c, xe - 10, yamostra - 30, 20, 70, 5, "#5A5F66", q)
    M.rrect(c, cx - 150, ytopo + 130, 80, 40, 8, "#2A2B31", q)
    lampada(c, cx, ytopo, luz, q)


def cristal(c, cx, cy, a=1.0, n=4, p=60):
    reticulo(c, 99, 0, cx - (n - 1) * p / 2, cy - (n - 1) * p / 2, n, n, p, 18, 25, rotulo=False, a=a)


def gelo(c, cx, cy, s=160, a=1.0):
    if a <= 0:
        return
    pp = skia.Paint(AntiAlias=True)
    pp.setShader(skia.GradientShader.MakeLinear([skia.Point(cx - s, cy - s), skia.Point(cx + s, cy + s)], [M.hexc("#EAF7FD", a), M.hexc("#A9D8EE", a)], [0, 1]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), 24, 24), pp)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), 24, 24), M.paint("#7FB8D6", a, stroke=4))
    M.line(c, cx - s * 0.3, cy - s * 0.3, cx - s * 0.05, cy - s * 0.3, BR, 0.8 * a, 8)


def panela(c, cx, cy, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - 130, cy - 60, 260, 130, 30, "#3A3B40", a, shadow=True)
    M.rrect(c, cx - 150, cy - 74, 300, 30, 14, "#55575E", a)
    M.rrect(c, cx + 140, cy - 70, 160, 26, 13, "#2A2B31", a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("três materiais da cozinha", "i", 66, TINTA2), W / 2, 170, "center", 0.1)
        objs = ((420, "sal", lambda a: cristal(c, 420, 420, a)), (960, "gelo", lambda a: gelo(c, 960, 420, 190, a)), (1480, "panela de ferro", lambda a: panela(c, 1440, 430, a)))
        for k, (x, nome, fn) in enumerate(objs):
            E.foco(c, t, C["s01.a"] + 0.4 + 0.4 * k, 0.5, fn)
            E.foco(c, t, C["s01.a"] + 0.6 + 0.4 * k, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 620, 56, "b", TINTA, a))
        for k, (cue, s_) in enumerate((("s01.b", "conduz sólido?"), ("s01.c", "só conduz derretido?"), ("s01.d", "derrete mais fácil?"))):
            pilula_em(c, t, C[cue], s_, W / 2, 740 + k * 90, 50, TINTA if k % 2 == 0 else TINTA2)
        E.frase(c, t, C["s01.e"], ps("a resposta está no", "i", 62) + [("tipo de ligação", "g", 60, COR)], W / 2, 1030, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 220 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("a", "i", 70), ("ligação", "g", 66, COR), ("pelos", "i", 70), ("elementos", "i", 70)]),
                 (C["s02.c"], [("quem", "i", 70), ("conduz", "g", 66), ("e", "i", 70), ("quem", "i", 70), ("aguenta calor", "g", 66)]),
                 (C["s02.d"], [("o", "i", 70), ("atalho", "g", 66, COR), ("que", "i", 70), ("a prova", "i", 70), ("cobra", "i", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("as três ligações", "i", 70, TINTA2), XE, 180, passo=0.12)
    linhas = (("s03.a", "iônica", "metal entrega elétrons ao ametal; íons se atraem"),
              ("s03.b", "covalente", "ametais dividem pares; formam moléculas"),
              ("s03.c", "metálica", "íons + num mar de elétrons"))
    for k, (cue, nome, desc) in enumerate(linhas):
        y = 360 + k * 230
        E.frase(c, t, C[cue], [(nome, "g", 76, COR)], XE, y)
        E.frase(c, t, C[cue] + 0.4, ps(desc, "i", 52, TINTA2), XE, y + 70, passo=0.06)
    reticulo(c, t, C["s03.a"] + 0.3, 1450, 290, 4, 2, 70, 22, 30)
    Q.molecula(c, t, C["s03.b"] + 0.3, "H2O", 1560, 560, 110)
    metal(c, t, C["s03.c"] + 0.3, 1450, 790, 4, 2, 70, 24)


# ---------------- regra (s04–s05) ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s04"], ps("qual é a ligação? olhe", "i", 66, TINTA2) + [("os elementos", "g", 62, COR)], XE, 180, passo=0.1)
    linhas = (("s04.b", "metal + ametal", "iônica"), ("s04.c", "ametal + ametal", "covalente"), ("s04.d", "metal (+ metal)", "metálica"))
    for k, (cue, par, lig) in enumerate(linhas):
        y = 330 + k * 130
        E.frase(c, t, C[cue], [(par, "g", 64), ("→", "g", 64, TINTA2), (lig, "g", 64, COR)], XE, y, passo=0.15)
    pilula_em(c, t, C["s04.e"], "o hidrogênio entra como ametal", XE + 360, 700, 46, TINTA2, "b")
    exemplos = (("s05.a", "NaCl", "iônica", lambda a: reticulo(c, 99, 0, 330, 870, 4, 1, 64, 20, 27, a=a)),
                ("s05.b", "H2O", "covalente", lambda a: Q.molecula_desenho(c, "H2O", 960, 880, 80, a)),
                ("s05.c", "Fe", "metálica", lambda a: metal(c, t, -9, 1500, 860, 4, 1, 62, 22, a=a)))
    for k, (cue, f, lig, fn) in enumerate(exemplos):
        x = 420 + 540 * k
        Q.formula_em(c, t, C[cue], f, x, 830, 96, align="center")
        E.foco(c, t, C[cue] + 0.8, 0.4, lambda a, x=x, lig=lig: E.pilula(c, lig, x, 980, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: (centro(c, "metal + ametal", 420, 900, 44, "i", TINTA2, a)))
    E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: (centro(c, "ametal + ametal", 960, 900, 44, "i", TINTA2, a)))
    E.foco(c, t, C["s05.c"] + 0.3, 0.4, lambda a: (centro(c, "metal sozinho", 1500, 900, 44, "i", TINTA2, a)))


# ---------------- condução (s06–s08) ----------------
def b_conduz(c, t, C, b):
    E.frase(c, t, C["s06"], ps("para conduzir:", "i", 66, TINTA2) + [("carga que anda", "g", 62, COR)], XE, 170, passo=0.1)
    if t < C["s07"]:
        E.saida(c, t, C["s07"] - 0.1, lambda: (
            teste(c, t, C["s06.b"] - 0.4, 1350, 330, 800, ep(t, C["s06.b"] + 0.4, 0.4),
                  lambda a: metal(c, t, C["s06.b"] - 0.4, 1150, 800, 6, 2, 80, 26, fluxo=C["s06.b"] + 0.4, a=a)),
            E.frase(c, t, C["s06.b"], [("ferro:", "g", 64)] + ps("elétrons soltos andam sempre", "i", 62), XE, 400, passo=0.1),
            E.frase(c, t, C["s06.c"], [("conduz", "g", 62, CERTO)] + ps("sólido e derretido", "i", 64), XE, 520, passo=0.1)))
        return
    if t < C["s08"]:
        def s07():
            sol = t < C["s07.d"]
            luz = 0 if sol else ep(t, C["s07.f"], 0.5)
            if sol:
                am = lambda a: cristal(c, 1350, 800, a, 5, 56)
            else:
                am = lambda a: Q.bequer(c, t, C["s07.d"], 1350, 960, 420, 300, 0.75, Q.AGUA, graduacao=False,
                                        particulas=dict(n=26, estado="gas", tipos=[("Na", 0.5), ("Cl", 0.5)], r=14, semente=7))
            teste(c, t, C["s07"], 1350, 300, 800 if sol else 760, luz, am)
            E.frase(c, t, C["s07.a"], [("sal:", "g", 64)] + ps("tem cargas, os íons", "i", 62), XE, 330, passo=0.1)
            E.frase(c, t, C["s07.b"], ps("no sólido, cada íon está preso", "i", 58, TINTA2), XE, 430, passo=0.08)
            E.frase(c, t, C["s07.c"], [("sólido:", "g", 60), ("não conduz", "g", 60, ERRADO)], XE, 540, passo=0.12)
            E.frase(c, t, C["s07.d"], ps("derretido ou na água:", "i", 60), XE, 680, passo=0.1)
            E.frase(c, t, C["s07.e"], ps("os íons ficam livres para andar", "i", 56, TINTA2), XE, 770, passo=0.08)
            E.frase(c, t, C["s07.f"], [("aí", "i", 62), ("conduz", "g", 60, CERTO)], XE, 880, passo=0.1)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    torneira = t >= C["s08.c"]
    luz = ep(t, C["s08.c"] + 0.6, 0.5) if torneira else 0
    am = lambda a: (Q.bequer(c, t, C["s08"], 1350, 960, 420, 300, 0.75, Q.AGUA, graduacao=False),
                    [Q.molecula(c, t, None, "H2O", 1220 + 90 * k, 870 + 40 * (k % 2), 34, a=a) for k in range(4)],
                    [Q.particulas(c, t, 1180, 820, 340, 120, 8, "gas", [("Na", 0.5), ("Cl", 0.5)], 12, 9, a * ep(t, C["s08.c"], 0.4))] if torneira else None)
    teste(c, t, C["s08"], 1350, 300, 760, luz, am)
    E.frase(c, t, C["s08.a"], [("água pura:", "g", 64)] + ps("só moléculas inteiras", "i", 62), XE, 330, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("quase", "i", 62) + [("não conduz", "g", 60, ERRADO)], XE, 440, passo=0.1)
    E.frase(c, t, C["s08.c"], [("da torneira:", "g", 60)] + ps("leva sais dissolvidos", "i", 62), XE, 600, passo=0.1)
    E.frase(c, t, C["s08.c"] + 1.4, ps("os íons dos sais andam:", "i", 58, TINTA2) + [("conduz", "g", 56, CERTO)], XE, 700, passo=0.08)


# ---------------- ponto de fusão (s09–s11) ----------------
def tabela_final(c, t, C):
    cols = ("", "ponto de fusão", "conduz sólido?", "conduz derretido?")
    linhas = (("s11.b", "iônico", ("alto", "não", "sim")), ("s11.c", "molecular", ("baixo", "não", "não")), ("s11.d", "metálico", ("alto*", "sim", "sim")))
    xs = (XE, 640, 1060, 1500)
    for j, h in enumerate(cols):
        E.foco(c, t, C["s11.a"] + 0.1 * j, 0.4, lambda a, j=j, h=h: E.escreve(c, h, xs[j], 300, 46, "b", TINTA2, a))
    for i, (cue, nome, vals) in enumerate(linhas):
        y = 450 + i * 160
        E.foco(c, t, C[cue], 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, XE, y, 66, "g", COR, a))
        for j, v in enumerate(vals):
            cor = CERTO if v == "sim" else ERRADO if v == "não" else TINTA
            E.foco(c, t, C[cue] + 0.4 + 0.3 * j, 0.4, lambda a, j=j, v=v, y=y, cor=cor: E.escreve(c, v, xs[j + 1], y, 62, "g", cor, a))
    q = ep(t, C["s11.a"], 0.4)
    if q > 0:
        M.line(c, XE, 340, 1800, 340, TINTA2, q, 3)
    E.foco(c, t, C["s11.d"] + 1.6, 0.4, lambda a: E.escreve(c, "* quase sempre", 640, 900, 42, "i", TINTA2, a))
    E.foco(c, t, C["s11.c"] + 0.2, 0.4, lambda a: E.escreve(c, "molecular = covalente feito de moléculas", XE, 1000, 46, "i", TINTA2, a))


def b_fusao(c, t, C, b):
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09"], [("ponto de fusão", "g", 66, COR)], XE, 180)
            E.frase(c, t, C["s09.a"], ps("a temperatura em que o sólido derrete", "i", 58, TINTA2), XE, 270, passo=0.08)
            reticulo(c, t, C["s09.b"], 1240, 330, 6, 4, 80, 24, 32)
            E.frase(c, t, C["s09.b"], ps("sal: desmontar o retículo", "i", 60), XE, 420, passo=0.1)
            E.foco(c, t, C["s09.c"], 0.5, lambda a: (E.escreve(c, "801 °C", XE, 560, 120, "g", TINTA, a)))
            E.frase(c, t, C["s09.d"], ps("metais: em geral, alto", "i", 60), XE, 720, passo=0.1)
            E.foco(c, t, C["s09.e"], 0.5, lambda a: (E.escreve(c, "ferro: 1538 °C", XE, 820, 76, "g", TINTA, a)))
            E.foco(c, t, C["s09.f"], 0.5, lambda a: E.pilula(c, "exceção: mercúrio, líquido", 1450, 820, 50, "g", fundo=TINTA2, a=a))
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], [("gelo:", "g", 66)] + ps("derrete a", "i", 70) + [("0 °C", "g", 66, COR)], XE, 200, passo=0.1)
            sep = ease_io(prog(t, C["s10.c"], 1.4))
            for i in range(2):
                for j in range(4):
                    k = i * 4 + j
                    dx = (j - 1.5) * (190 + 90 * sep)
                    dy = (i - 0.5) * (170 + 80 * sep) + 20 * sep * math.sin(t * 2 + k)
                    Q.molecula(c, t, C["s10.a"] + 0.1 * k, "H2O", 1220 + dx, 640 + dy, 70, passo=0.05, giro=15 * k * sep)
            E.frase(c, t, C["s10.b"], ps("a ligação H–O não quebra", "i", 58), XE, 380, passo=0.1)
            E.frase(c, t, C["s10.c"], ps("só afasta uma molécula da outra", "i", 58, TINTA2), XE, 480, passo=0.08)
            pilula_em(c, t, C["s10.d"], "forças entre moléculas: outra aula", XE + 420, 900, 44, TINTA2, "b")
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11.a"], [("juntando", "i", 70, TINTA2), ("tudo", "i", 70, TINTA2)], XE, 190)
    tabela_final(c, t, C)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("tem íons, então conduz sempre?", "i", 62), XE + 460, 190, passo=0.1)
    teste(c, t, C["s12.b"], 640, 340, 780, 0, lambda a: cristal(c, 640, 780, a, 5, 56))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "não acende", 640, 1000, 50, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "íon preso não leva corrente", XE, 290, 52, "i", TINTA2, a))
    teste(c, t, C["s12.e"], 1450, 340, 740, ep(t, C["s12.e"] + 0.6, 0.5),
          lambda a: Q.bequer(c, t, C["s12.e"], 1450, 960, 380, 280, 0.75, Q.AGUA, graduacao=False,
                             particulas=dict(n=22, estado="gas", tipos=[("Na", 0.5), ("Cl", 0.5)], r=13, semente=5)))
    E.foco(c, t, C["s12.e"] + 0.8, 0.4, lambda a: E.pilula(c, "acende", 1450, 1030, 50, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o caminho inverso", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s13.a"], ps("a prova descreve o comportamento", "i", 58, CLARO), W / 2, 240, "center", 0.08)
            linhas = (("s13.b", "conduz sólido?", "metálica"), ("s13.c", "não conduz sólido, conduz derretido?", "iônica"),
                      ("s13.d", "não conduz e derrete fácil?", "molecular"))
            for k, (cue, perg, resp) in enumerate(linhas):
                y = 420 + k * 190
                E.frase(c, t, C[cue], ps(perg, "i", 62, BR), XE, y, passo=0.08)
                E.foco(c, t, C[cue] + 1.2, 0.4, lambda a, y=y, resp=resp: E.pilula(c, resp, 1600, y - 20, 60, "g", fundo=E.COR, a=a))
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], ps("elétron solto: quase só no metal", "i", 62, BR), XE, 220, passo=0.1)
    E.frase(c, t, C["s14.b"], ps("íon preso: só se solta quando o sólido se desfaz", "i", 56, CLARO), XE, 320, passo=0.08)
    E.frase(c, t, C["s14.c"], [("cuidado:", "g", 58, ERRADO)] + ps("conduzir na água não serve de prova", "i", 60, BR), XE, 500, passo=0.08)
    E.frase(c, t, C["s14.c"] + 2.4, ps("certos ácidos, moleculares, também conduzem: outra aula", "i", 50, CLARO), XE, 590, passo=0.06)
    E.frase(c, t, C["s14.d"], [("grafite", "g", 62, BR)] + ps("(ponta do lápis): carbono que conduz", "i", 58, CLARO), XE, 780, passo=0.08)
    pilula_em(c, t, C["s14.d"] + 2.0, "caso especial", XE + 300, 880, 46, E.COR)


# ---------------- questão ----------------
CARDS = (("X", "660 °C", "conduz sólido", "metálico", "alumínio"), ("Y", "770 °C", "só conduz derretido", "iônico", "cloreto de potássio"),
         ("Z", "−114 °C", "não conduz", "molecular", "álcool comum"))


def card(c, x, y, k, a=1.0, resposta=0.0):
    nome, pf, cond, lig, quem = CARDS[k]
    if a <= 0:
        return
    M.rrect(c, x, y, 500, 380, 30, "#FFFFFF", 0.95 * a, shadow=True)
    E.escreve(c, nome, x + 40, y + 110, 100, "g", COR, a)
    E.escreve(c, "derrete a", x + 40, y + 190, 44, "i", TINTA2, a)
    E.escreve(c, pf, x + 240, y + 190, 50, "g", TINTA, a)
    E.escreve(c, cond, x + 40, y + 260, 46, "b", TINTA, a)
    if resposta > 0:
        E.pilula(c, lig, x + 250, y + 330, 50, "g", fundo=CERTO, a=a * resposta)
        E.escreve(c, quem, x + 160, y + 112, 40, "i", TINTA2, a * resposta)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    for k, cue in enumerate(("s15.a", "s15.b", "s15.c")):
        E.foco(c, t, C[cue], 0.5, lambda a, k=k: card(c, XE + k * 560, 290, k, a))
    E.frase(c, t, C["s15.d"], ps("qual é a ligação de cada um?", "i", 66), XE, 850, passo=0.1)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1640, cy=860, r=120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], ps("pela condução", "i", 66, TINTA2), XE, 170)
    for k, cue in enumerate(("s17.a", "s17.b", "s17.c")):
        card(c, XE + k * 560, 290, k, 1.0, ep(t, C[cue], 0.5))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", [("metal + ametal:", "g", 58), ("iônica", "i", 62)]),
                 ("s18.a", [("ametal + ametal:", "g", 58), ("covalente", "i", 62)]),
                 ("s18.a", [("metal + metal:", "g", 58), ("metálica", "i", 62)]),
                 ("s18.b", ps("a ligação diz quem conduz e quem aguenta calor", "i", 60)))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 160
            ti = C[k] + (0.9 * i if i < 3 else 0)
            E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, ti + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s19.a"], [("praticando:", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s19.a"] + 0.5, [("tipos de ligação", "g", 90, COR)], XE, 520)
    E.frase(c, t, C["s19.b"], ps("fórmulas e propriedades em questões", "i", 60), XE, 650, passo=0.1)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regra=b_regra, conduz=b_conduz, fusao=b_fusao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
