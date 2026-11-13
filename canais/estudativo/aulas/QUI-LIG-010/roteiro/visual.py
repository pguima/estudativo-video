"""Visual — Estudativo · QUI-LIG-010: comparar pontos de ebulição.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), a da trilha (QUI-LIG-001) e a do módulo (QUI-LIG-006/009). Peça
própria: TERMÔMETRO (termometro()) = régua vertical de temperatura em °C, com 0 °C marcado; cada substância é uma bolinha
na sua temperatura, com a fórmula ao lado e o valor; a cor do ponto diz a força: ligação de hidrogênio = turquesa,
dipolo permanente = turquesa claro, dipolo induzido = cinza (a mesma escala de barras da QUI-LIG-009). A família do
oxigênio usa E.serie, com a tendência prolongada em tracejado. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-010_comparar_pontos_de_ebulicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ebulicao", "passo1", "agua", "atalho", "questao", "fim"))
BR = "#FFFFFF"
F_H, F_P, F_I = E.COR, M.mix(E.COR, "#FFFFFF", 0.4), "#A9AEB6"

PE = {"CH4": -161, "HCl": -85, "H2O": 100, "H2S": -60, "H2Se": -41, "H2Te": -2, "C3H8": -42, "C8H18": 126, "F2": -188, "HF": 20}
assert PE["CH4"] < PE["HCl"] < PE["H2O"] and PE["H2O"] - PE["H2S"] == 160
assert PE["CH4"] < PE["C3H8"] < PE["C8H18"] and PE["C8H18"] > PE["H2O"]
assert PE["H2S"] < PE["H2Se"] < PE["H2Te"] and PE["F2"] < PE["HCl"] < PE["HF"]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def termometro(c, t, t0, x, y0, y1, tmin, tmax, marcas=(-200, -100, 0, 100), escuro=False):
    """régua vertical: y0 = topo (tmax), y1 = base (tmin). Devolve T → y"""
    Y = lambda T: y1 - (T - tmin) / (tmax - tmin) * (y1 - y0)
    q = ep(t, t0, 0.5)
    if q > 0:
        tinta = BR if escuro else TINTA
        M.line(c, x, y1 + 10, x, lerp(y1 + 10, y0 - 10, ease_out(prog(t, t0, 0.6))), tinta, q, 6)
        for T in marcas:
            yy = Y(T)
            M.line(c, x - 16, yy, x + 16, yy, tinta, q, 4)
            E.formula(c, f"{T} °C".replace("-", "−"), x - 30, yy + 16, 40, "b", BR if escuro else TINTA2, q, "right")
        y0c = Y(0)
        M.line(c, x + 20, y0c, x + 1100, y0c, TINTA2 if not escuro else "#8A8D99", 0.35 * q, 3, dash=[12, 10])
    return Y


def ponto(c, t, t0, Y, x, T, f, cor, dx=40, escuro=False, rot=None):
    q = ease_back(prog(t, t0, 0.45))
    if q <= 0:
        return
    yy = Y(T)
    c.drawCircle(x, yy, 22 * q, M.paint(cor))
    c.drawCircle(x, yy, 22 * q, M.paint(TINTA if not escuro else BR, 0.6, stroke=3))
    a = min(1, prog(t, t0, 0.3))
    if f:
        Q.formula(c, f, x + dx, yy + 22, 62, None, a, escuro=escuro)
    E.escreve(c, (rot or f"{T} °C").replace("-", "−"), x + dx + 260, yy + 18, 52, "g", COR if not escuro else E.CLARO, a)


def legenda(c, t, t0, x, y, escuro=False):
    for k, (nome, cor) in enumerate((("ligação de hidrogênio", F_H), ("dipolo permanente", F_P), ("dipolo induzido", F_I))):
        E.foco(c, t, t0 + 0.15 * k, 0.4, lambda a, k=k, nome=nome, cor=cor: (c.drawCircle(x, y + k * 60, 16, M.paint(cor, a)),
                                                                          E.escreve(c, nome, x + 34, y + k * 60 + 14, 40, "b", BR if escuro else TINTA, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.formula_em(c, t, C["s01.a"], "H2S", XE, 220, 110)
        E.frase(c, t, C["s01.a"] + 0.4, ps("maior e quase 2× mais pesada", "i", 56, TINTA2), XE + 300, 210, passo=0.08)
        Q.molecula(c, t, C["s01.a"] + 0.6, dict(atomos=[("S", 0, -0.2), ("H", -0.85, 0.5), ("H", 0.85, 0.5)], ligacoes=[(0, 1, 1), (0, 2, 1)]), 1500, 220, 100)
        Y = termometro(c, t, C["s01.b"] - 0.4, 560, 380, 980, -100, 120, (-100, -50, 0, 50, 100))
        ponto(c, t, C["s01.b"], Y, 600, -60, "H2S", F_P)
        ponto(c, t, C["s01.c"], Y, 600, 100, "H2O", F_H)
        if t >= C["s01.d"]:
            q = ep(t, C["s01.d"], 0.5)
            M.line(c, 1400, Y(100), 1400, lerp(Y(100), Y(-60), ease_out(prog(t, C["s01.d"], 0.6))), COR, q, 6)
            for yy in (Y(100), Y(-60)):
                M.line(c, 1380, yy, 1420, yy, COR, q, 6)
            E.foco(c, t, C["s01.d"] + 0.4, 0.4, lambda a: E.escreve(c, "160 °C", 1450, (Y(100) + Y(-60)) / 2 + 20, 70, "g", COR, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 210 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    E.frase(c, t, C["s02.b"], [("ordenar", "g", 66)] + ps("pelo ponto de ebulição", "i", 70), XE, 420, passo=0.12)
    E.frase(c, t, C["s02.c"], [("1º", "g", 66, COR), ("a força,", "i", 70), ("2º", "g", 66, COR), ("o tamanho", "i", 70)], XE, 560, passo=0.12)
    E.frase(c, t, C["s02.d"], ps("e o caso da água", "i", 66, TINTA2), XE, 700, passo=0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 66, TINTA2), XE, 190, passo=0.12)
    barras = (("s03.a", "dipolo induzido", 0.25, F_I, "a mais fraca"), ("s03.b", "dipolo permanente", 0.55, F_P, "a do meio"), ("s03.c", "ligação de hidrogênio", 1.0, F_H, "a mais forte"))
    for k, (cue, nome, v, cor, nota) in enumerate(barras):
        y = 360 + k * 170
        p = ease_out(prog(t, C[cue], 0.7))
        if p > 0:
            M.rrect(c, XE + 620, y - 50, 800 * v * p, 90, 20, cor, 1)
        E.foco(c, t, C[cue], 0.4, lambda a, y=y, nome=nome, nota=nota: (E.escreve(c, nome, XE, y + 14, 52, "g", TINTA, a), E.escreve(c, nota, XE, y + 70, 42, "i", TINTA2, a)))
    E.foco(c, t, C["s03.c"] + 1.4, 0.4, lambda a: E.pilula(c, "H preso a F, O ou N", XE + 1100, 890, 48, "g", fundo=E.COR, a=a))


# ---------------- ponto de ebulição (s04) ----------------
def b_ebulicao(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("ponto de ebulição", "g", 76, COR)], XE, 200)
    E.frase(c, t, C["s04.a"] + 0.8, ps("a temperatura em que o líquido ferve e vira gás", "i", 54), XE, 290, passo=0.06)
    E.foco(c, t, C["s04.a"] + 0.4, 0.5, lambda a: Q.bequer(c, t, C["s04.a"] + 0.4, 560, 920, 360, 400, 0.7, Q.AGUA, graduacao=False))
    sep = ease_io(prog(t, C["s04.b"], 1.6))
    for k in range(6):
        x0, y0 = 480 + (k % 3) * 80, 830 - (k // 3) * 70
        x1, y1 = 380 + k * 70 + 30 * math.sin(t + k), 460 - (k % 2) * 60
        x, y = lerp(x0, x1, sep), lerp(y0, y1, sep)
        Q.molecula_desenho(c, "H2O", x, y, 36, 1.0, giro=40 * k + t * 20 * sep, rotulos=False)
    E.frase(c, t, C["s04.b"], ps("ferver: as moléculas se soltam umas das outras", "i", 52), 900, 460, passo=0.06)
    E.frase(c, t, C["s04.c"], [("força", "g", 62), ("mais forte", "i", 64), ("→", "g", 62, TINTA2)], 900, 640, passo=0.1)
    E.frase(c, t, C["s04.d"], [("mais calor,", "i", 64), ("ponto de ebulição", "g", 60, COR), ("mais alto", "g", 60, COR)], 900, 740, passo=0.1)


# ---------------- passo 1 (s05) ----------------
def b_passo1(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("1º passo:", "g", 66, COR)] + ps("compare o tipo de força", "i", 66), XE, 180, passo=0.1)
    Y = termometro(c, t, C["s05.a"] + 0.3, 400, 300, 980, -200, 120, (-200, -100, 0, 100))
    for cue, f, cor, forca in (("s05.b", "CH4", F_I, "dipolo induzido"), ("s05.c", "HCl", F_P, "dipolo permanente"), ("s05.d", "H2O", F_H, "ligação de hidrogênio")):
        ponto(c, t, C[cue] + 0.6, Y, 440, PE[f], f, cor)
        E.foco(c, t, C[cue], 0.4, lambda a, f=f, cor=cor, forca=forca: E.pilula(c, forca, 1560, Y(PE[f]) - 6, 42, "g", fundo=cor, a=a, cor=TINTA if cor != F_H else BR))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: E.pilula(c, "a ordem das temperaturas é a ordem das forças", W / 2 + 120, 1030, 44, "g", fundo=TINTA, a=a))


# ---------------- passo 2 (s06) ----------------
def b_passo2(c, t, C, b):
    E.frase(c, t, C["s06.a"], [("2º passo,", "g", 62, COR)] + ps("só se a força for a mesma:", "i", 60) + [("o tamanho", "g", 60)], XE, 170, passo=0.1)
    E.frase(c, t, C["s06.b"], ps("molécula maior, mais elétrons:", "i", 54, TINTA2), XE, 260, passo=0.08)
    E.frase(c, t, C["s06.c"], ps("dipolo induzido mais forte", "i", 54, TINTA2), XE + 720, 260, passo=0.08)
    Y = termometro(c, t, C["s06.a"] + 0.3, 400, 340, 990, -200, 150, (-200, -100, 0, 100))
    for cue, f, n, rot in (("s06.d", "CH4", 1, "metano"), ("s06.e", "C3H8", 3, "propano · gás de cozinha"), ("s06.f", "C8H18", 8, "octano · gasolina")):
        ponto(c, t, C[cue], Y, 440, PE[f], f, F_I)
        E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, f=f, rot=rot: E.escreve(c, rot, 1180, Y(PE[f]) + 16, 42, "i", TINTA2, a))
        if n > 1:
            Q.bastao(c, t, C[cue] + 0.4, Q.zigzag(n), 1650, Y(PE[f]) - 10, 46)
        else:
            E.foco(c, t, C[cue] + 0.4, 0.4, lambda a, f=f: E.bola(c, 1650, Y(PE[f]) - 10, 10, TINTA, a))


# ---------------- água (s07–s08) ----------------
def b_agua(c, t, C, b):
    E.frase(c, t, C["s07.a"], ps("a família do oxigênio", "i", 66), XE, 180, passo=0.1)
    x, y, w, h = 330, 300, 900, 640
    dados = [("H₂O", PE["H2O"]), ("H₂S", PE["H2S"]), ("H₂Se", PE["H2Se"]), ("H₂Te", PE["H2Te"])]
    vy = lambda v: y + h - (v + 120) / 240 * h
    xs = [x + w * (i + 0.5) / 4 for i in range(4)]
    q0 = ep(t, C["s07.b"], 0.5)
    if q0 > 0:
        M.line(c, x, y - 20, x, y + h, TINTA, q0, 5)
        M.line(c, x, y + h, x + w, y + h, TINTA, q0, 5)
        for v in (-100, -50, 0, 50, 100):
            M.line(c, x, vy(v), x + w, vy(v), FIO, q0, 2)
            E.formula(c, f"{v} °C".replace("-", "−"), x - 20, vy(v) + 14, 38, "b", TINTA2, q0, "right")
        for i, (rot, _) in enumerate(dados):
            E.formula(c, rot, xs[i], y + h + 56, 44, "b", TINTA, q0 * (1 if i else ep(t, C["s07.b"] + 0.3, 0.4)), "center")
    pts = [(xs[i], vy(v)) for i, (_, v) in enumerate(dados)]
    p = ease_io(prog(t, C["s07.c"], 1.2))
    if p > 0:
        for i in (1, 2):
            A, B = pts[i], pts[i + 1]
            u = max(0, min(1, p * 2 - (i - 1)))
            if u > 0:
                M.line(c, *A, lerp(A[0], B[0], u), lerp(A[1], B[1], u), TINTA2, 1, 7)
        for i in (1, 2, 3):
            k = ease_back(prog(t, C["s07.c"] + 0.3 * (i - 1), 0.4))
            if k > 0:
                c.drawCircle(*pts[i], 14 * k, M.paint(F_P))
                c.drawCircle(*pts[i], 14 * k, M.paint(TINTA, 0.6, stroke=3))
            E.foco(c, t, C["s07.c"] + 0.3 * (i - 1) + 0.2, 0.4, lambda a, i=i: E.formula(c, f"{dados[i][1]} °C".replace("-", "−"), pts[i][0], pts[i][1] - 30, 42, "g", COR, a, "center"))
    if t >= C["s07.d"]:
        q = ep(t, C["s07.d"], 0.5)
        (x1, y1), (x2, y2) = pts[2], pts[1]
        k = (y2 - y1) / (x2 - x1)
        yy = y2 + k * (xs[0] - x2)
        pp = ease_out(prog(t, C["s07.d"], 0.6))
        M.line(c, x2, y2, lerp(x2, xs[0], pp), lerp(y2, yy, pp), TINTA2, q, 5, dash=[14, 10])
        E.foco(c, t, C["s07.d"] + 0.5, 0.4, lambda a: (c.drawCircle(xs[0], yy, 14, M.paint(TINTA2, a, stroke=4)),
                                                      E.formula(c, "≈ −80 °C ?", xs[0], yy + 60, 44, "g", TINTA2, a, "center")))
    if t >= C["s08"]:
        q = ease_back(prog(t, C["s08.a"], 0.5))
        if q > 0:
            c.drawCircle(xs[0], vy(100), 20 * q, M.paint(F_H))
            c.drawCircle(xs[0], vy(100), 20 * q, M.paint(TINTA, 0.6, stroke=3))
        E.foco(c, t, C["s08.a"] + 0.2, 0.4, lambda a: E.formula(c, "100 °C", xs[0], vy(100) - 34, 56, "g", COR, a, "center"))
        E.frase(c, t, C["s08.b"], ps("S, Se, Te: dipolo permanente", "i", 48, TINTA2), 1300, 420, passo=0.06)
        E.frase(c, t, C["s08.c"], ps("só a água: H preso a O", "i", 52), 1300, 520, passo=0.06)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "ligação de hidrogênio", 1540, 620, 48, "g", fundo=F_H, a=a))
        E.frase(c, t, C["s08.e"], ps("mantém a água líquida", "i", 52, TINTA2), 1300, 740, passo=0.06)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s09"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s09.a"], ps("comparar só pelo tamanho?", "i", 66), XE + 460, 190, passo=0.1)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: (Q.formula(c, "H2S", XE + 100, 440, 120, ERRADO, a), E.escreve(c, "é maior...", XE + 420, 430, 60, "i", ERRADO, a),
                                            E.escreve(c, "então ferve acima da água?", XE + 100, 560, 66, "b", ERRADO, a)))
    if t >= C["s09.b"] + 1.6:
        E.risco(c, XE + 80, 590, XE + 1000, 380, t, C["s09.b"] + 1.6, largura=12)
    E.frase(c, t, C["s09.c"], ps("o tamanho só desempata quando a", "i", 62) + [("força é a mesma", "g", 60, COR)], W / 2, 800, "center", 0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], ps("o atalho cabe numa frase", "i", 66, CLARO), W / 2, 200, "center", 0.1)
            E.frase(c, t, C["s10.a"], [("força", "g", 110, BR), ("primeiro,", "i", 110, CLARO)], W / 2, 420, "center", 0.2)
            E.frase(c, t, C["s10.a"] + 0.8, [("tamanho", "g", 110, BR), ("no empate", "i", 110, CLARO)], W / 2, 560, "center", 0.2)
            E.frase(c, t, C["s10.b"], ps("a diferença entre as forças é grande;", "i", 56, CLARO), W / 2, 760, "center", 0.07)
            E.frase(c, t, C["s10.b"] + 2.0, ps("a de tamanho entre moléculas parecidas, pequena", "i", 56, CLARO), W / 2, 840, "center", 0.07)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11.a"], [("falha", "g", 62, ERRADO)] + ps("quando os tamanhos são muito diferentes", "i", 62, BR), W / 2, 200, "center", 0.1)
    Y = termometro(c, t, C["s11.a"] + 0.4, 520, 360, 860, 0, 150, (0, 50, 100, 150), escuro=True)
    ponto(c, t, C["s11.b"], Y, 560, 100, "H2O", F_H, escuro=True)
    ponto(c, t, C["s11.c"], Y, 560, 126, "C8H18", F_I, escuro=True)
    Q.bastao(c, t, C["s11.c"] + 0.3, Q.zigzag(8), 1480, 500, 60, escuro=True)
    E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: E.escreve(c, "octano: só dipolo induzido, mas enorme", 1100, 640, 44, "i", CLARO, a))
    E.frase(c, t, C["s11.d"], ps("na prova, as moléculas costumam ter tamanho parecido", "i", 52, CLARO), W / 2, 1000, "center", 0.06)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s12"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s12.a"], ps("do menor para o maior ponto de ebulição:", "i", 60), XE, 290, passo=0.08)
    for k, (cue, f, nome) in enumerate((("s12.b", "F2", "gás flúor"), ("s12.c", "HCl", ""), ("s12.d", "HF", "fluoreto de hidrogênio"))):
        y = 470 + k * 160
        Q.formula_em(c, t, C[cue], f, XE + 40, y, 110)
        if nome:
            E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, y=y, nome=nome: E.escreve(c, nome, XE + 340, y - 10, 52, "i", TINTA2, a))
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.pilula(c, "tamanhos parecidos", XE + 330, 960, 50, "g", fundo=TINTA, a=a))
    if t >= C["s13"]:
        E.relogio(c, t, C["s13.a"], cx=1480, cy=500, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("força primeiro", "i", 66, TINTA2), XE, 170)
            for k, (cue, f, motivo, forca, cor) in enumerate((("s14.a", "F2", "átomos iguais: apolar", "dipolo induzido", F_I),
                                                              ("s14.b", "HCl", "polar; H no Cl, que não é F, O nem N", "dipolo permanente", F_P),
                                                              ("s14.c", "HF", "H preso ao flúor", "ligação de hidrogênio", F_H))):
                y = 360 + k * 220
                Q.formula_em(c, t, C[cue], f, XE, y, 110)
                E.foco(c, t, C[cue] + 0.3, 0.4, lambda a, y=y, motivo=motivo: E.escreve(c, motivo, XE + 300, y - 10, 48, "i", TINTA, a))
                E.foco(c, t, C[cue] + 1.2, 0.4, lambda a, y=y, forca=forca, cor=cor: E.pilula(c, forca, 1560, y - 30, 48, "g", fundo=cor, a=a, cor=TINTA if cor != F_H else BR))
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], ps("a ordem:", "i", 66, TINTA2), XE, 180)
    Y = termometro(c, t, C["s15.a"], 400, 300, 940, -200, 50, (-200, -100, 0))
    for cue, f, cor in (("s15.b", "F2", F_I), ("s15.c", "HCl", F_P), ("s15.d", "HF", F_H)):
        ponto(c, t, C[cue], Y, 440, PE[f], f, cor)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "a mais leve ferve mais alto", 1450, 1010, 50, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s16.a", [("força mais forte,", "g", 62)] + ps("ponto de ebulição mais alto", "i", 64)),
                 ("s16.b", [("compare a força", "g", 62)] + ps("primeiro", "i", 64)),
                 ("s16.c", [("o tamanho", "g", 62)] + ps("só no empate", "i", 64)),
                 ("s16.d", [("a água", "g", 62)] + ps("ferve alto pelas ligações de hidrogênio", "i", 64)))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s17.a"], [("o gelo", "i", 90), ("boia", "g", 90, COR)], XE, 390, passo=0.15)
    E.frase(c, t, C["s17.b"], ps("o inseto anda sobre a água", "i", 66), XE, 520, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("a água sobe no tubo fino", "i", 66), XE, 630, passo=0.1)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s17.d"] + 0.2, 0.4))
    E.frase(c, t, C["s17.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ebulicao=b_ebulicao, passo1=b_passo1, passo2=b_passo2, agua=b_agua,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
