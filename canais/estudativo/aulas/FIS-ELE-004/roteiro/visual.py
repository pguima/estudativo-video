"""Visual — Estudativo · FIS-ELE-004: potencial elétrico e energia.

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001):
carga + laranja e − azul; campo em tinta, linhas de força em cinza-tinta; POTENCIAL é escalar: número com sinal numa
pílula, nunca seta; tensão = degrau de uma escada (desnível); trabalho positivo em verde. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-004_potencial_eletrico_energia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("potencial", "tensao", "trabalho", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"

# todas as contas da aula
assert abs(9e9 * 2e-6 / 3 - 6e3) < 1e-6 and 9 * 2 == 18 and 18 / 3 == 6 and abs(9e9 * 2e-6 / 3 ** 2 - 2e3) < 1e-6
assert abs(500 * 0.2 - 100) < 1e-9 and abs(3e-6 * 100 - 3e-4) < 1e-15 and 2000 + (-2000) == 0
assert abs(2000 * 0.05 - 100) < 1e-9 and abs(2e-6 * 100 - 2e-4) < 1e-15


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha Eletricidade (cópia das da FIS-ELE-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def q(c, x, y, r, s, a=1.0):
    """carga pequena: + laranja, − azul, com o sinal em branco"""
    if a <= 0:
        return
    cor = E.COR if s == "+" else NEG
    c.drawCircle(x + r * 0.08, y + r * 0.16, r, M.paint("#000000", 0.16 * a))
    c.drawCircle(x, y, r, M.paint(cor, a))
    k, lw = r * 0.52, max(3, r * 0.24)
    M.line(c, x - k, y, x + k, y, BR, a, lw)
    if s == "+":
        M.line(c, x, y - k, x, y + k, BR, a, lw)


def esfera_metal(c, cx, cy, R, a=1.0):
    E.bola(c, cx, cy, R, METAL, a)


def pilula_f(c, s, cx, cy, size, fundo=None, cor=BR, a=1.0):
    """pílula com fórmula (aceita potência de dez)"""
    if a <= 0:
        return
    w, h = E.formula(None, s, 0, 0, size, "g", a=0) + size * 1.2, size * 1.9
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), h / 2, h / 2), M.paint(fundo or E.COR, a))
    E.formula(c, s, cx, cy + size * 0.36, size, "g", cor, a, "center")


def _linha(c, partes, x, y, a, align="center"):
    """linha de tipografia mista parada (para a troca)"""
    w, xs = E._arranjo(partes, x, align)
    for p, xx in zip(partes, xs):
        E.escreve(c, p[0], xx, y, p[2], p[1], p[3] if len(p) > 3 else TINTA, a)


def terra(c, x, y, a=1.0, cor=TINTA):
    """símbolo de terra: três traços, o de cima em y"""
    for i, w in enumerate((90, 60, 30)):
        M.line(c, x - w / 2, y + i * 18, x + w / 2, y + i * 18, cor, a, 6)


def promessa(c, t, C, cena, itens, sz=74):
    """tela "até o fim da aula": órbita à direita e itens numerados. itens = [(cue, texto, atraso)]"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", sz, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, desenhos):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, cx, cy) desenha à direita da caixa"""
    if len(itens) == 2:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
        E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
        E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    else:
        E.frase(c, t, C[cena] + 0.2, ps("você precisa", "i", 84), XE, 470, passo=0.14)
        E.frase(c, t, C[cena] + 0.6, ps("de uma coisa", "i", 84), XE, 580, passo=0.14)
    x, w = 820, 1000
    y0 = 230 if len(itens) == 2 else 340
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    if len(itens) == 2:
        q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
        E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    else:
        E.cursor(c, x + w - 30, 560, ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, dy=190):
    """tela "resumindo": itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 380 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)


def cta(c, t, C, cena):
    """inscreva-se (cue c) e bons estudos (cue d), à direita"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1580, 990, "center")


def questao_relogio(c, t, C, cena_pausa, desenho):
    """lado direito da questão: o desenho até a pausa, depois o relógio"""
    if t < C[cena_pausa]:
        desenho()
    else:
        E.relogio(c, t, C[cena_pausa + ".a"], cx=1460, cy=440, r=200)



def campo_seta(c, t, t0, A, B, rot="E", escuro=False):
    F.vetor(c, t, t0, A, B, rot, None, BR if escuro else TINTA, 8, size=56)


def placas(c, t, t0, x1, x2, y0, y1, a=1.0):
    """placas paralelas (+ à esquerda, − à direita)"""
    q_ = ep(t, t0, 0.5) * a
    if q_ <= 0:
        return
    M.rrect(c, x1 - 22, y0 - 30, 44, y1 - y0 + 60, 10, E.COR, q_)
    M.rrect(c, x2 - 22, y0 - 30, 44, y1 - y0 + 60, 10, NEG, q_)
    for i in range(5):
        yy = lerp(y0, y1, (i + 0.5) / 5)
        M.line(c, x1 - 10, yy, x1 + 10, yy, BR, q_, 5)
        M.line(c, x1, yy - 10, x1, yy + 10, BR, q_, 5)
        M.line(c, x2 - 10, yy, x2 + 10, yy, BR, q_, 5)


def linhas_retas(c, t, t0, x1, x2, y0, y1, n=5):
    for i in range(n):
        yy = lerp(y0, y1, i / (n - 1))
        p = ease_io(prog(t, t0 + 0.06 * i, 0.8))
        if p > 0:
            M.line(c, x1 + 30, yy, lerp(x1 + 30, x2 - 30, p), yy, TINTA2, 1.0, 4)
            if p > 0.6:
                F._cabeca(c, (x1 + x2) / 2 + 11, yy, 1, 0, 22, TINTA2, ep(t, t0 + 0.5 + 0.06 * i, 0.3))


def escada(c, x, y, degraus, w, h, a=1.0):
    """escada que desce para a direita: topo em (x, y)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y)
    for i in range(degraus):
        p.lineTo(x + (i + 1) * w, y + i * h)
        p.lineTo(x + (i + 1) * w, y + (i + 1) * h)
    p.lineTo(x, y + degraus * h)
    p.close()
    c.drawPath(p, M.paint("#E2E2DD", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))


def ponto(c, x, y, rot, a=1.0):
    if a <= 0:
        return
    c.drawCircle(x, y, 13, M.paint(TINTA, a))
    E.escreve(c, rot, x - 14, y - 30, 52, "g", TINTA, a)


# ---------------- gancho ----------------
def pilha_icone(c, cx, cy, a):
    M.rrect(c, cx - 60, cy - 120, 120, 240, 20, TINTA, a)
    M.rrect(c, cx - 60, cy - 120, 120, 80, 20, E.COR, a)
    M.rrect(c, cx - 22, cy - 140, 44, 24, 6, TINTA2, a)


def tomada_icone(c, cx, cy, a):
    M.rrect(c, cx - 110, cy - 110, 220, 220, 40, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 110, cy - 110, 220, 220), 40, 40), M.paint(TINTA2, a, stroke=4))
    for dx in (-38, 38):
        c.drawCircle(cx + dx, cy - 10, 18, M.paint(TINTA, a))
    c.drawCircle(cx, cy + 50, 14, M.paint(TINTA, a))


def raio_icone(c, cx, cy, a):
    p = skia.Path()
    for i, (dx, dy) in enumerate(((20, -130), (-60, 10), (0, 10), (-30, 130), (70, -20), (5, -20), (40, -130))):
        (p.moveTo if i == 0 else p.lineTo)(cx + dx, cy + dy)
    p.close()
    c.drawPath(p, M.paint("#FFC400", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))


def b_gancho(c, t, C, b):
    def um():
        for k, x, fn, val in (("s01.a", 400, pilha_icone, ("1,5", "V")), ("s01.b", 960, tomada_icone, ("127", "V")), ("s01.c", 1520, raio_icone, ("milhares de", "V"))):
            E.foco(c, t, C[k], 0.5, lambda a, x=x, fn=fn: fn(c, x, 430, a))
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x=x, val=val: F.medida(c, val[0], val[1], x, 680, 70 if len(val[0]) < 6 else 54, TINTA, a, "center"))
        E.frase(c, t, C["s01.d"], [("volt", "g", 96, COR), ("mede", "i", 96), ("o", "i", 96), ("quê?", "g", 96)], W / 2, 880, "center", 0.12)
    E.saida(c, t, C["s01.e"] - 0.1, um)
    if C["s01.e"] - 0.1 <= t < C["s02"]:
        E.frase(c, t, C["s01.e"], ps("energia por coulomb", "i", 100), W / 2, 420, "center", 0.12)
        E.foco(c, t, C["s01.e"] + 0.8, 0.5, lambda a: pilula_f(c, "1 V = 1 J/C", W / 2, 640, 110, a=a))
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "potencial de uma carga", 1.4), ("s02.b", "tensão no campo uniforme", 0), ("s02.c", "trabalho: q vezes U", 0)), sz=64)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o campo de uma carga:", "E = k · Q ÷ d²"), ("s03.c", "o trabalho:", "força × deslocamento")),
             (lambda a, x, y: (q(c, x - 60, y, 34, "+", a), F.seta(c, x - 15, y, x + 90, y, TINTA, a, 6, 20)),
              lambda a, x, y: E.formula(c, "τ = F · d", x - 40, y + 20, 56, "g", TINTA, a, "center")))


# ---------------- potencial ----------------
def b_potencial(c, t, C, b):
    def s04():
        sx, sy = 1100, 330

        def degraus():
            E.foco(c, t, C["s04.a"], 0.5, lambda a: escada(c, sx, sy, 4, 130, 110, a))
            kk = 3 * ease_io(prog(t, C["s04.b"], 1.6))
            i = min(2, int(kk))
            f = kk - i
            bx, by = sx + (i + 0.5 + f) * 130, sy + i * 110 - 38 + 110 * f ** 2
            E.foco(c, t, C["s04.a"] + 0.3, 0.4, lambda a: E.bola(c, bx, by, 38, a=a))
        E.saida(c, t, C["s04.c"] - 0.1, degraus)
        E.frase(c, t, C["s04.a"], ps("energia guardada pela", "i", 66) + [("posição", "g", 64, COR)], XE, 240, passo=0.1)
        E.frase(c, t, C["s04.b"], [("solta,", "i", 66), ("ela", "i", 66), ("desce", "g", 64)], XE, 360, passo=0.12)
        E.frase(c, t, C["s04.c"], ps("com cargas é igual", "i", 66), XE, 620, passo=0.12)
        F.campo_carga(c, t, C["s04.c"] + 0.2, 1380, 560, 80, 260, n=10)
        F.carga(c, t, C["s04.c"], 1380, 560, 64, "+")
        F.carga(c, t, C["s04.c"] + 0.4, 1700, 450, 30, "+")
        E.frase(c, t, C["s04.d"], [("energia", "g", 70, COR), ("potencial", "g", 70, COR), ("elétrica", "g", 70, COR)], XE, 780, passo=0.12)
        E.foco(c, t, C["s04.d"] + 0.8, 0.4, lambda a: E.escreve(c, "em joule (J)", XE, 880, 56, "i", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("potencial", "g", 100, COR), ("elétrico", "g", 100, COR)], XE, 260)
            E.frase(c, t, C["s05.a"] + 0.8, ps("energia ÷ carga", "i", 72), XE, 380, passo=0.12)
            E.foco(c, t, C["s05.b"], 0.5, lambda a: E.escreve(c, "V", XE, 700, 260, "g", COR, a))
            E.frase(c, t, C["s05.b"] + 0.3, [("volt", "g", 96)], XE + 230, 620)
            E.foco(c, t, C["s05.c"], 0.5, lambda a: pilula_f(c, "1 V = 1 J/C", XE + 440, 850, 76, fundo=TINTA, a=a))
            E.foco(c, t, C["s05.d"], 0.5, lambda a: pilha_icone(c, 1450, 520, a))
            E.foco(c, t, C["s05.d"] + 0.4, 0.4, lambda a: (F.medida(c, "1,5", "V", 1450, 780, 80, TINTA, a, "center"),
                                                          E.escreve(c, "1,5 J por coulomb", 1260, 870, 54, "i", TINTA2, a)))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            F.formula_legenda(c, t, C["s06.a"], "V = f{k · Q}{d}", [("V", "potencial", "V"), ("Q", "carga, com sinal", "C"), ("d", "distância", "m")],
                              XE + 40, 380, 150, tl=[C["s06.a"] + 0.6, C["s06.a"] + 0.9, C["s06.a"] + 1.2], size_l=58)
            E.foco(c, t, C["s06.b"], 0.5, lambda a: E.pilula(c, "d sem o quadrado", 1400, 300, 54, "g", fundo=E.COR, a=a))
            E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "Q < 0  →  V < 0", 1400, 520, 76, "g", NEG, a, "center"))
            E.foco(c, t, C["s06.d"], 0.5, lambda a: E.pilula(c, "ESCALAR: um número, sem seta", 1300, 880, 52, "g", fundo=TINTA, a=a))
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    y = 250
    F.carga(c, t, C["s07.a"], 600, y, 56, "+")
    E.foco(c, t, C["s07.a"] + 0.3, 0.4, lambda a: F.medida(c, 2, "µC", 600, y - 90, 56, TINTA, a, "center"))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: (c.drawCircle(1300, y, 12, M.paint(TINTA, a)), E.escreve(c, "P", 1325, y - 20, 50, "g", TINTA, a)))
    if t >= C["s07.b"]:
        q_ = ep(t, C["s07.b"], 0.4)
        M.line(c, 660, y + 60, 1300, y + 60, TINTA2, q_, 4, dash=E.TRACO)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: F.medida(c, 3, "m", 980, y + 130, 56, TINTA, a, "center"))
    E.formula_em(c, t, C["s07.b"] + 0.9, "V = f{9 × 10^9 · 2 × 10^{−6}}{3}", W / 2, 540, 90, "g", TINTA, "center")
    E.formula_em(c, t, C["s07.c"], "9 · 2 = 18   10^{9 − 6} = 10^3", W / 2, 740, 76, "g", COR, "center")
    E.formula_em(c, t, C["s07.d"], "18 ÷ 3 = 6", 520, 930, 76, "g", TINTA, "center")
    E.foco(c, t, C["s07.e"], 0.5, lambda a: pilula_f(c, "V = 6 × 10^3 V = 6.000 V", 1220, 905, 70, a=a))


# ---------------- tensão ----------------
def b_tensao(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08.a"], ps("diferença de potencial", "i", 80), XE, 240, passo=0.12)
        E.foco(c, t, C["s08.b"], 0.5, lambda a: E.pilula(c, "ddp", XE + 120, 380, 70, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s08.c"], [("=", "g", 76, TINTA2), ("tensão,", "i", 82), ("U", "g", 90, COR)], XE + 300, 404)
        E.formula_em(c, t, C["s08.d"], "U = V₁ − V₂", XE, 620, 120, "g", TINTA)
        E.foco(c, t, C["s08.e"], 0.5, lambda a: escada(c, 1150, 480, 2, 260, 200, a))
        if t >= C["s08.e"] + 0.4:
            a = ep(t, C["s08.e"] + 0.4, 0.4)
            M.line(c, 1700, 480, 1700, 680, COR, a, 6)
            F._cabeca(c, 1700, 680, 0, 1, 22, E.COR, a)
            E.foco(c, t, C["s08.e"] + 0.5, 0.4, lambda a_: (E.escreve(c, "U", 1730, 600, 76, "g", COR, a_), E.escreve(c, "V₁", 1180, 450, 50, "g", TINTA, a_),
                                                          E.escreve(c, "V₂", 1440, 650, 50, "g", TINTA, a_)))
        E.frase(c, t, C["s08.e"] + 1.0, ps("o que conta é quanto se desce", "i", 56, TINTA2), XE, 820, passo=0.1)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    x1, x2, y0, y1 = 1080, 1720, 300, 760
    placas(c, t, C["s09"], x1, x2, y0, y1)
    linhas_retas(c, t, C["s09"] + 0.3, x1, x2, y0 + 30, y1 - 30)
    E.formula_em(c, t, C["s09.a"], "U = E · d", XE, 330, 120, "g", TINTA)
    E.foco(c, t, C["s09.a"] + 0.9, 0.4, lambda a: E.escreve(c, "campo × distância", XE, 420, 54, "i", TINTA2, a))
    p1, p2 = (1240, 530), (1560, 530)
    E.foco(c, t, C["s09.a"] + 0.5, 0.4, lambda a: (ponto(c, *p1, "1", a), ponto(c, *p2, "2", a)))
    if t >= C["s09.a"] + 0.8:
        q_ = ep(t, C["s09.a"] + 0.8, 0.4)
        M.line(c, p1[0], 830, p2[0], 830, TINTA2, q_, 4, dash=E.TRACO)
        E.escreve(c, "d", (p1[0] + p2[0]) / 2 - 15, 900, 60, "g", TINTA, q_)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "no sentido das linhas, o potencial cai", 1400, 200, 40, "b", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: (E.escreve(c, "E =", XE, 600, 66, "g", TINTA, a), F.medida(c, 500, "N/C", XE + 140, 600, 66, COR, a)))
    E.foco(c, t, C["s09.d"], 0.5, lambda a: (E.escreve(c, "d =", XE, 710, 66, "g", TINTA, a), F.medida(c, 20, "cm", XE + 140, 710, 66, COR, a),
                                            E.escreve(c, "= 0,2 m", XE + 390, 710, 66, "g", TINTA2, a)))
    E.foco(c, t, C["s09.e"], 0.5, lambda a: pilula_f(c, "U = 500 · 0,2 = 100 V", XE + 380, 880, 64, a=a))


# ---------------- trabalho ----------------
def b_trabalho(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10"], ps("o trabalho da força elétrica", "i", 66, TINTA2), XE, 200, passo=0.1)
        F.formula_legenda(c, t, C["s10.a"], "τ = q · U", [("τ", "trabalho", "J"), ("q", "carga", "C"), ("U", "tensão entre os pontos", "V")],
                          XE + 40, 430, 160, tl=[C["s10.b"], C["s10.c"], C["s10.d"]], size_l=60)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    x1, x2, y0, y1 = 1080, 1720, 300, 760
    placas(c, t, C["s11"], x1, x2, y0, y1)
    p1, p2 = (1220, 530), (1580, 530)
    E.foco(c, t, C["s11"] + 0.3, 0.4, lambda a: (ponto(c, *p1, "1", a), ponto(c, *p2, "2", a)))
    u = ease_io(prog(t, C["s11.a"] + 0.4, 1.6))
    F.carga(c, t, C["s11.a"], lerp(p1[0], p2[0], u), p1[1] + 80, 32, "+")
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "1 está 100 V acima de 2", 1400, 870, 44, "b", fundo=TINTA, a=a))
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (E.escreve(c, "q =", XE, 300, 70, "g", TINTA, a), F.medida(c, 3, "µC", XE + 140, 300, 70, COR, a)))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (E.escreve(c, "U =", XE, 420, 70, "g", TINTA, a), F.medida(c, 100, "V", XE + 150, 420, 70, COR, a)))
    E.formula_em(c, t, C["s11.c"], "τ = 3 × 10^{−6} · 100", XE, 600, 84, "g", TINTA)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: pilula_f(c, "τ = 3 × 10^{−4} J", XE + 360, 760, 76, fundo=CERTO, a=a))
    E.frase(c, t, C["s11.e"], [("positivo:", "g", 56, CERTO), ("a", "i", 60), ("força", "i", 60), ("ajudou", "i", 60)], XE, 940, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], [("d²", "g", 80, ERRADO), ("no", "i", 80), ("potencial", "i", 80)], XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (E.escreve(c, "campo", 420, 400, 56, "i", TINTA2, a), E.formula(c, "E = f{k · Q}{d^2}", 420, 520, 100, "g", TINTA, a)))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: (E.escreve(c, "potencial", 1180, 400, 56, "i", TINTA2, a), E.formula(c, "V = f{k · Q}{d}", 1180, 520, 100, "g", COR, a)))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: pilula_f(c, "com d²: 2.000 V", 640, 800, 66, fundo=ERRADO, a=a))
    if t >= C["s12.d"] + 0.6:
        E.risco(c, 360, 840, 920, 760, t, C["s12.d"] + 0.6, largura=10)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: pilula_f(c, "certo: 6.000 V", 1320, 800, 66, fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    y = 640

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], [("o", "i", 76, CLARO), ("potencial", "i", 76, CLARO), ("é", "i", 76, CLARO), ("escalar", "g", 76, BR)], W / 2, 280, "center", 0.12)
        E.frase(c, t, C["s13.b"], ps("some com o sinal, sem seta", "i", 64, CLARO), W / 2, 390, "center", 0.12)
        F.carga(c, t, C["s13.c"], 500, y, 60, "+", escuro=True)
        F.carga(c, t, C["s13.c"] + 0.2, 1420, y, 60, "−", escuro=True)
        E.foco(c, t, C["s13.c"] + 0.3, 0.3, lambda a: c.drawCircle(960, y, 12, M.paint(BR, a)))
        E.foco(c, t, C["s13.c"] + 0.4, 0.4, lambda a: (E.pilula(c, "+2.000 V", 730, y - 120, 48, "g", fundo=E.COR, a=a),
                                                      E.pilula(c, "−2.000 V", 1190, y - 120, 48, "g", fundo=NEG, a=a)))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: pilula_f(c, "V = 0", 960, 860, 90, fundo=TINTA2, a=a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], ps("energia não tem direção", "i", 76, CLARO), W / 2, 250, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("não", "g", 66, ERRADO), ("vale", "g", 66, ERRADO), ("para", "i", 70, CLARO), ("o", "i", 70, CLARO), ("campo:", "i", 70, CLARO),
                               ("vetor", "g", 66, BR)], W / 2, 380, "center", 0.12)
    F.carga(c, t, C["s14.b"], 500, y, 60, "+", escuro=True)
    F.carga(c, t, C["s14.b"] + 0.2, 1420, y, 60, "−", escuro=True)
    E.foco(c, t, C["s14.b"] + 0.3, 0.3, lambda a: c.drawCircle(960, y, 12, M.paint(BR, a)))
    campo_seta(c, t, C["s14.c"], (960, y), (1180, y), escuro=True)
    E.foco(c, t, C["s14.c"] + 0.6, 0.4, lambda a: E.pilula(c, "V = 0, mas o campo é forte", 960, 860, 50, "g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"] - 0.4, [("campo", "i", 76), ("uniforme:", "i", 76)], XE, 330)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: F.medida(c, "2.000", "N/C", XE + 600, 330, 80, COR, a))
    E.frase(c, t, C["s15.b"], [("tensão", "g", 76), ("a", "i", 80), ("5", "g", 76, COR), ("cm?", "g", 76, COR)], XE, 490, passo=0.15)
    E.frase(c, t, C["s15.c"], [("trabalho", "g", 76), ("em", "i", 80), ("+2", "g", 76, COR), ("µC?", "g", 76, COR)], XE, 640, passo=0.15)
    E.frase(c, t, C["s15.d"], ps("do potencial maior para o menor", "i", 60, TINTA2), XE, 760, passo=0.1)

    def desenho():
        x1, x2, y0, y1 = 1230, 1760, 320, 760
        placas(c, t, C["s15.a"], x1, x2, y0, y1)
        linhas_retas(c, t, C["s15.a"] + 0.3, x1, x2, y0 + 30, y1 - 30)
        E.foco(c, t, C["s15.b"], 0.4, lambda a: (ponto(c, 1370, 540, "1", a), ponto(c, 1620, 540, "2", a),
                                                 F.medida(c, 5, "cm", 1495, 880, 60, TINTA, a, "center")))
    questao_relogio(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s17.a"], "5 cm = 0,05 m", XE, 250, 84, "g", TINTA2)
    E.formula_em(c, t, C["s17.b"], "U = E · d = 2.000 · 0,05", XE, 420, 84, "g", TINTA)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: pilula_f(c, "U = 100 V", 1500, 395, 80, a=a))
    E.formula_em(c, t, C["s18.a"], "τ = q · U", XE, 630, 84, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "= 2 × 10^{−6} · 100", XE + 420, 630, 84, "g", TINTA)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: pilula_f(c, "τ = 2 × 10^{−4} J", 1500, 605, 80, fundo=CERTO, a=a))
    E.frase(c, t, C["s18.d"], [("positivo:", "g", 60, CERTO)] + ps("foi do potencial maior para o menor", "i", 62), XE, 860, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s19", (("s19.a", [("V = k · Q ÷ d", "g", 72), ("sem", "i", 72), ("quadrado,", "i", 72), ("com", "i", 72), ("sinal", "g", 68, COR)]),
                                ("s19.b", [("U = E · d", "g", 72), ("no", "i", 72), ("campo", "i", 72), ("uniforme", "i", 72)]),
                                ("s19.c", [("τ = q · U", "g", 72)])))
    E.saida(c, t, C["s20"] - 0.1, tela)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("condutores", "g", 120, COR)], XE, 410)
    E.foco(c, t, C["s20.a"] + 0.4, 0.5, lambda a: E.bola(c, 560, 760, 180, METAL, a))
    for i in range(10):
        g = 2 * math.pi * i / 10
        E.foco(c, t, C["s20.a"] + 0.8 + 0.05 * i, 0.3, lambda a, g=g: q(c, 560 + 150 * math.cos(g), 760 + 150 * math.sin(g), 22, "+", a), blur=0)
    E.frase(c, t, C["s20.b"], [("para-raios", "g", 70), ("e", "i", 72), ("carro", "g", 70)], 860, 790, passo=0.12)
    cta(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, potencial=b_potencial, tensao=b_tensao, trabalho=b_trabalho, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
