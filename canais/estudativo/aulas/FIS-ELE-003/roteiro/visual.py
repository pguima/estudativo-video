"""Visual — Estudativo · FIS-ELE-003: campo elétrico e linhas de força.

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001):
carga + laranja e − azul; força = seta laranja; CAMPO = seta em tinta (TINTA) e linhas de força em cinza-tinta (TINTA2) com
setas; campo uniforme = linhas paralelas igualmente espaçadas entre placas; atalho no palco. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-003_campo_eletrico_linhas_de_forca.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("campo", "carga", "linhas", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"

# todas as contas da aula
assert abs(8e-3 / 2e-6 - 4e3) < 1e-6 and 8 / 2 == 4 and -3 + 6 == 3
assert abs(9e9 * 4e-6 / 2 ** 2 - 9e3) < 1e-6 and 9 * 4 == 36 and 36 / 4 == 9
assert abs(9e9 * 2e-6 / 3 ** 2 - 2e3) < 1e-6 and 9 * 2 == 18 and 18 / 9 == 2 and abs(1e-6 * 2e3 - 2e-3) < 1e-15


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
    """vetor campo elétrico: seta em tinta com a letra-vetor E"""
    F.vetor(c, t, t0, A, B, rot, None, BR if escuro else TINTA, 8, size=56)


def dipolo(c, t, t0, x1, x2, y, n=2, d=1.2):
    """linhas de força de + (x1) para − (x2): curvas que saem da + e entram na −, com seta no meio"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    for k in range(-n, n + 1):
        h = k * 150
        pts = F._bezier((x1, y), (x1 + (x2 - x1) * 0.25, y - h * 1.35), (x1 + (x2 - x1) * 0.75, y - h * 1.35), (x2, y), 50)
        F.poli(c, pts, p, TINTA2, 1.0, 4)
        if p > 0.6:
            m = pts[25]
            F._cabeca(c, m[0] + 11, m[1], 1, 0, 22, TINTA2, ep(t, t0 + d * 0.6, 0.3))


def cota(c, t, t0, x1, x2, y, rot):
    q_ = ep(t, t0, 0.4)
    if q_ <= 0:
        return
    M.line(c, x1, y, x2, y, TINTA2, q_, 4, dash=E.TRACO)
    for x in (x1, x2):
        M.line(c, x, y - 18, x, y + 18, TINTA2, q_, 4)
    v, _, u = rot.partition(" ")
    F.medida(c, v, u, (x1 + x2) / 2, y + 70, 56, TINTA, q_, "center")


def placas(c, t, t0, x1, x2, y0, y1, n=6, a=1.0):
    """placas paralelas (+ à esquerda, − à direita) com linhas retas igualmente espaçadas"""
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


def linhas_retas(c, t, t0, x1, x2, y0, y1, n=6):
    for i in range(n):
        yy = lerp(y0, y1, i / (n - 1))
        p = ease_io(prog(t, t0 + 0.06 * i, 0.8))
        if p > 0:
            M.line(c, x1 + 30, yy, lerp(x1 + 30, x2 - 30, p), yy, TINTA2, 1.0, 4)
            if p > 0.6:
                F._cabeca(c, (x1 + x2) / 2 + 11, yy, 1, 0, 22, TINTA2, ep(t, t0 + 0.5 + 0.06 * i, 0.3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 600
        F.campo_carga(c, t, C["s01.c"], 860, y, 110, 360, n=12)
        F.carga(c, t, C["s01.a"], 860, y, 90, "+")
        F.carga(c, t, C["s01.a"] + 0.4, 1500, y, 40, "+")
        if t >= C["s01.a"] + 0.9:
            F.seta(c, 1550, y, 1720, y, E.COR, ep(t, C["s01.a"] + 0.9, 0.3), 9, None, ease_out(prog(t, C["s01.a"] + 0.9, 0.5)))
        E.foco(c, t, C["s01.a"] + 1.2, 0.4, lambda a: E.pilula(c, "sem encostar", 1200, 820, 46, "b", fundo=TINTA, a=a))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: E.escreve(c, "?", 1180, 500, 200, "g", COR, a) if t < C["s01.c"] else None)
        E.frase(c, t, C["s01.a"], ps("uma carga sente a outra", "i", 80), XE, 220, passo=0.12)
        E.frase(c, t, C["s01.c"], [("campo", "g", 110, COR), ("elétrico", "g", 110, COR)], XE, 1000)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "calcular o campo", 1.4), ("s02.b", "de dois jeitos", 0), ("s02.c", "ler as linhas de força", 0)), sz=70)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a lei de Coulomb:", "F = k · Q₁ · Q₂ ÷ d²"),),
             (lambda a, x, y: E.formula(c, "k = 9 × 10^9", x - 40, y + 10, 50, "g", TINTA, a, "center"),))


# ---------------- o campo ----------------
def b_campo(c, t, C, b):
    def s04():
        y = 560
        E.frase(c, t, C["s04.a"], [("campo", "g", 100, COR), ("elétrico", "g", 100, COR)], XE, 260)
        E.frase(c, t, C["s04.a"] + 0.8, ps("o espaço modificado", "i", 66, TINTA2), XE, 360, passo=0.12)
        F.campo_carga(c, t, C["s04.a"], 1200, y, 110, 330, n=12)
        F.carga(c, t, C["s04"] + 0.5, 1200, y, 90, "+")
        E.foco(c, t, C["s04"] + 0.8, 0.4, lambda a: E.escreve(c, "Q", 1170, y + 170, 70, "g", TINTA, a))
        F.carga(c, t, C["s04.b"], 1640, y - 120, 36, "+")
        E.foco(c, t, C["s04.b"] + 0.3, 0.4, lambda a: E.escreve(c, "q", 1630, y - 190, 60, "g", COR, a))
        if t >= C["s04.c"]:
            ux, uy = E._uni(1200, y, 1640, y - 120)
            F.seta(c, 1640 + ux * 46, y - 120 + uy * 46, 1640 + ux * 210, y - 120 + uy * 210, E.COR, ep(t, C["s04.c"], 0.3), 9, None, ease_out(prog(t, C["s04.c"], 0.5)))
        E.frase(c, t, C["s04.b"], [("carga", "i", 72), ("de", "i", 72), ("teste", "i", 72), ("q", "g", 72, COR)], XE, 620, passo=0.12)
        E.frase(c, t, C["s04.c"], [("sente", "i", 72), ("uma", "i", 72), ("força", "g", 70, COR)], XE, 740, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("a força dividida pela carga de teste", "i", 64, TINTA2), XE, 200, passo=0.1)
            F.formula_legenda(c, t, C["s05.b"], "E = f{F}{q}", [("E", "campo", "N/C"), ("F", "força", "N"), ("q", "carga de teste", "C")],
                              XE + 60, 430, 160, tl=[C["s05.c"], C["s05.d"], C["s05.e"]], size_l=60)
            E.foco(c, t, C["s05.f"], 0.5, lambda a: E.pilula(c, "N/C: newtons em cada coulomb", 1340, 470, 46, "b", fundo=E.COR, a=a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"], 0.5, lambda a: (E.escreve(c, "q =", XE, 230, 70, "g", TINTA, a), F.medida(c, 2, "µC", XE + 140, 230, 70, COR, a)))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (E.escreve(c, "F =", XE + 640, 230, 70, "g", TINTA, a),
                                            E.formula(c, "8 × 10^{−3}", XE + 780, 230, 70, "g", COR, a),
                                            E.formula(c, "N", XE + 800 + E.formula(None, "8 × 10^{−3}", 0, 0, 70, a=0), 230, 50, "b", F.UNID, a)))
    E.formula_em(c, t, C["s06.b"] + 1.0, "E = f{8 × 10^{−3}}{2 × 10^{−6}}", W / 2, 450, 96, "g", TINTA, "center")
    E.formula_em(c, t, C["s06.c"], "8 ÷ 2 = 4", 560, 700, 84, "g", COR, "center")
    E.formula_em(c, t, C["s06.d"], "f{10^{−3}}{10^{−6}} = 10^3", 1300, 700, 84, "g", COR, "center")
    E.foco(c, t, C["s06.d"] + 1.6, 0.4, lambda a: centro(c, "−3 + 6 = 3", 1300, 820, 50, "b", TINTA2, a))
    E.foco(c, t, C["s06.e"], 0.5, lambda a: pilula_f(c, "E = 4 × 10^3 N/C", W / 2, 940, 76, a=a))


# ---------------- campo de uma carga ----------------
def b_carga(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07"], ps("direto da carga que cria", "i", 70, TINTA2), W / 2, 200, "center", 0.12)
        troca(c, t, [(C["s07.a"], "E = f{F}{q} = f{k · Q · q}{d^2 · q}"), (C["s07.c"], "E = f{k · Q}{d^2}")],
              lambda s, a: E.formula(c, s, W / 2, 470, 120 if "·" in s and "q}" not in s else 100, "g", TINTA, a, "center"))
        E.foco(c, t, C["s07.a"] + 1.0, 0.4, lambda a: E.pilula(c, "um dos Q da lei de Coulomb é o q de teste", W / 2, 640, 42, "b", fundo=TINTA2, a=a) if t < C["s07.c"] else None)
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "o q de cima corta com o de baixo", W / 2, 730, 46, "b", fundo=E.COR, a=a) if t < C["s07.c"] else None)
        for k, l, nome, y in (("s07.d", "Q", "a carga que cria o campo", 720), ("s07.e", "d", "a distância até o ponto", 840)):
            E.foco(c, t, C[k], 0.5, lambda a, l=l, nome=nome, y=y: (E.escreve(c, l, 560, y, 76, "g", COR, a), E.escreve(c, nome, 660, y, 60, "i", TINTA, a)))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if C["s08"] <= t < C["s09"]:
        def s08():
            y = 260
            F.carga(c, t, C["s08.a"], 600, y, 56, "+")
            E.foco(c, t, C["s08.a"] + 0.3, 0.4, lambda a: F.medida(c, 4, "µC", 600, y - 90, 56, TINTA, a, "center"))
            E.foco(c, t, C["s08.b"], 0.4, lambda a: (c.drawCircle(1300, y, 12, M.paint(TINTA, a)), E.escreve(c, "P", 1325, y - 20, 50, "g", TINTA, a)))
            cota(c, t, C["s08.b"], 660, 1300, y + 60, "2 m")
            campo_seta(c, t, C["s08.b"] + 0.4, (1300, y), (1500, y))
            E.formula_em(c, t, C["s08.b"] + 1.0, "E = f{9 × 10^9 · 4 × 10^{−6}}{2^2}", W / 2, 560, 90, "g", TINTA, "center")
            E.formula_em(c, t, C["s08.c"], "9 · 4 = 36   10^{9 − 6} = 10^3", W / 2, 760, 76, "g", COR, "center")
            E.formula_em(c, t, C["s08.d"], "36 ÷ 4 = 9", 520, 930, 76, "g", TINTA, "center")
            E.foco(c, t, C["s08.e"], 0.5, lambda a: pilula_f(c, "E = 9 × 10^3 N/C", 1250, 905, 76, a=a))
        E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], [("o", "i", 76), ("campo", "i", 76), ("é", "i", 76), ("vetor", "g", 76, COR)], W / 2, 170, "center", 0.12)
    y = 420
    for k, x, s, sai, rot in (("s09.a", 560, "+", True, "aponta para longe"), ("s09.b", 1360, "−", False, "aponta para ela")):
        F.campo_carga(c, t, C[k] + 0.2, x, y, 80, 210, n=8, sai=sai, cor=TINTA)
        F.carga(c, t, C[k], x, y, 60, s)
        E.foco(c, t, C[k] + 0.6, 0.4, lambda a, x=x, rot=rot: centro(c, rot, x, y + 270, 50, "i", TINTA2, a))
    y2 = 880
    for k, x, s, ok in (("s09.c", 200, "+", True), ("s09.d", 1100, "−", False)):
        campo_seta(c, t, C[k], (x, y2 - 90), (x + 260, y2 - 90))
        F.carga(c, t, C[k] + 0.3, x + 130, y2, 34, s)
        if t >= C[k] + 0.6:
            d_ = 1 if ok else -1
            F.seta(c, x + 130 + d_ * 46, y2, x + 130 + d_ * 230, y2, E.COR, ep(t, C[k] + 0.6, 0.3), 9, None, ease_out(prog(t, C[k] + 0.6, 0.5)))
            E.foco(c, t, C[k] + 0.9, 0.4, lambda a, x=x, d_=d_: E.escreve(c, "F", x + 130 + d_ * 150 - 18, y2 + 70, 56, "g", COR, a))
        E.foco(c, t, C[k] + 1.0, 0.4, lambda a, x=x, ok=ok: E.escreve(c, "mesmo sentido" if ok else "sentido oposto", x + (400 if ok else 330), y2 + 18, 50, "i", TINTA, a))


# ---------------- linhas de força ----------------
def b_linhas(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10.a"], [("linhas", "i", 92), ("de", "i", 92), ("força", "g", 88, COR)], W / 2, 190, "center", 0.12)
        y, x1, x2 = 600, 640, 1280
        dipolo(c, t, C["s10.b"], x1, x2, y)
        F.carga(c, t, C["s10.a"] + 0.4, x1, y, 56, "+")
        F.carga(c, t, C["s10.a"] + 0.6, x2, y, 56, "−")
        E.foco(c, t, C["s10.b"] + 1.0, 0.4, lambda a: (E.escreve(c, "saem da +", 330, y + 130, 46, "i", TINTA2, a), E.escreve(c, "chegam na −", 1340, y + 130, 46, "i", TINTA2, a)))
        # campo num ponto: seta tangente à linha de cima
        pts = F._bezier((x1, y), (x1 + 160, y - 405), (x1 + 480, y - 405), (x2, y), 50)
        P0, P1 = pts[12], pts[14]
        ux, uy = E._uni(*P0, *P1)
        E.foco(c, t, C["s10.c"], 0.3, lambda a: c.drawCircle(*P0, 12, M.paint(TINTA, a)))
        campo_seta(c, t, C["s10.c"] + 0.3, P0, (P0[0] + ux * 170, P0[1] + uy * 170))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: (E.pilula(c, "juntas: campo forte", 960, 980, 44, "b", fundo=E.COR, a=a)))
        q_ = ep(t, C["s10.d"], 0.4) * (1 - ep(t, C["s10.e"], 0.4))
        if q_ > 0:
            c.drawCircle(x1 + 70, y, 110, M.paint(E.COR, q_, stroke=6))
        E.foco(c, t, C["s10.e"], 0.5, lambda a: E.pilula(c, "nunca se cruzam", 1640, 330, 44, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("um caso especial", "i", 70, TINTA2), W / 2, 180, "center", 0.12)
    x1, x2, y0, y1 = 520, 1220, 340, 820
    placas(c, t, C["s11.a"], x1, x2, y0, y1)
    linhas_retas(c, t, C["s11.b"], x1, x2, y0 + 20, y1 - 20)
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "CAMPO UNIFORME", W / 2 - 90, 960, 64, "g", fundo=E.COR, a=a))
    for i, (px, py) in enumerate(((1440, 400), (1520, 580), (1440, 760))):
        campo_seta(c, t, C["s11.d"] + 0.3 * i, (px, py), (px + 220, py), rot="E" if i == 0 else None)
    E.foco(c, t, C["s11.d"] + 1.2, 0.4, lambda a: E.escreve(c, "igual em todo ponto", 1400, 880, 46, "i", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("o campo depende de", "i", 76) + [("q?", "g", 76, ERRADO)], XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "q × 2", 420, 450, 110, "g", TINTA, "center")
    E.formula_em(c, t, C["s12.c"], "F × 2", 960, 450, 110, "g", TINTA, "center")
    E.formula_em(c, t, C["s12.d"], "E = f{2F}{2q} = f{F}{q}", 1460, 470, 100, "g", CERTO, "center")
    E.foco(c, t, C["s12.d"] + 0.8, 0.4, lambda a: E.pilula(c, "o campo continua o mesmo", 1460, 680, 46, "b", fundo=CERTO, a=a))
    E.frase(c, t, C["s12.e"], ps("depende só de", "i", 72) + [("Q", "g", 72, COR), ("e", "i", 72), ("d", "g", 72, COR)], W / 2, 900, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("a mesma proporção de Coulomb", "i", 66, CLARO), W / 2, 280, "center", 0.12)
        E.formula_em(c, t, C["s13.a"] + 1.4, "E = f{k · Q}{d^2}", W / 2, 440, 96, "g", BR, "center")
        E.formula_em(c, t, C["s13.b"], "d × 2  →  E ÷ 4", W / 2 - 380, 660, 76, "g", BR, "center")
        E.formula_em(c, t, C["s13.c"], "d × 3  →  E ÷ 9", W / 2 + 380, 660, 76, "g", BR, "center")
        E.foco(c, t, C["s13.d"], 0.5, lambda a: pilula_f(c, "F = q · E", W / 2, 880, 90, a=a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("d²", "g", 80, BR), ("embaixo,", "i", 80, CLARO), ("como", "i", 80, CLARO), ("em", "i", 80, CLARO), ("Coulomb", "g", 80, BR)], W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("não", "g", 66, ERRADO), ("vale", "g", 66, ERRADO), ("no", "i", 70, CLARO), ("campo", "i", 70, CLARO), ("uniforme", "g", 66, BR)], W / 2, 480, "center", 0.12)
    for i in range(5):
        yy = 620 + i * 70
        p = ease_io(prog(t, C["s14.b"] + 0.8 + 0.06 * i, 0.6))
        if p > 0:
            M.line(c, 700, yy, lerp(700, 1220, p), yy, CLARO, 1.0, 4)
            F._cabeca(c, lerp(700, 1220, p), yy, 1, 0, 20, CLARO, 1.0)
    E.foco(c, t, C["s14.b"] + 1.6, 0.4, lambda a: E.escreve(c, "E igual em todo ponto", 1300, 780, 50, "i", BR, a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"] - 0.5, [("carga", "i", 80)], XE, 340)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: F.medida(c, 2, "µC", XE + 260, 340, 96, COR, a))
    E.frase(c, t, C["s15.b"], [("campo", "i", 80), ("a", "i", 80), ("3", "g", 80, COR), ("m?", "g", 80, COR)], XE, 490, passo=0.15)
    E.frase(c, t, C["s15.c"], [("força", "i", 80), ("em", "i", 80), ("−1", "g", 80, NEG), ("µC?", "g", 80, NEG)], XE, 640, passo=0.15)
    E.frase(c, t, C["s15.d"], [("valor", "g", 76), ("e", "i", 80), ("sentido", "g", 76, COR)], XE, 790, passo=0.15)

    def desenho():
        y = 520
        F.carga(c, t, C["s15.a"], 1180, y, 60, "+")
        cota(c, t, C["s15.b"], 1240, 1700, y + 110, "3 m")
        F.carga(c, t, C["s15.c"], 1700, y, 34, "−")
    questao_relogio(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        E.formula_em(c, t, C["s17.a"], "E = f{k · Q}{d^2} = f{9 × 10^9 · 2 × 10^{−6}}{3^2}", W / 2, 330, 90, "g", TINTA, "center")
        E.formula_em(c, t, C["s17.b"], "9 · 2 = 18   10^{9 − 6} = 10^3", W / 2, 560, 80, "g", COR, "center")
        E.formula_em(c, t, C["s17.c"], "18 ÷ 9 = 2", 520, 790, 80, "g", TINTA, "center")
        E.foco(c, t, C["s17.d"], 0.5, lambda a: pilula_f(c, "E = 2 × 10^3 N/C", 1250, 765, 80, a=a))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.formula_em(c, t, C["s18.a"], "F = q · E", XE, 260, 100, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "= 1 × 10^{−6} · 2 × 10^3", XE + 470, 260, 80, "g", TINTA2)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: pilula_f(c, "F = 2 × 10^{−3} N", 640, 440, 76, a=a))
    y = 760
    F.carga(c, t, C["s18.d"] - 0.6, 760, y, 64, "+")
    F.carga(c, t, C["s18.d"] - 0.4, 1260, y, 36, "−")
    campo_seta(c, t, C["s18.d"], (1260, y - 110), (1520, y - 110))
    if t >= C["s18.e"]:
        F.seta(c, 1210, y, 1000, y, E.COR, ep(t, C["s18.e"], 0.3), 9, None, ease_out(prog(t, C["s18.e"], 0.5)))
        E.foco(c, t, C["s18.e"] + 0.3, 0.4, lambda a: E.escreve(c, "F", 1080, y + 80, 60, "g", COR, a))
    E.foco(c, t, C["s18.d"] + 0.3, 0.4, lambda a: E.pilula(c, "força contrária ao campo", 1400, 940, 44, "b", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s19", (("s19.a", [("E = F ÷ q", "g", 72)]),
                                ("s19.b", [("E = k · Q ÷ d²", "g", 72)]),
                                ("s19.c", [("linhas:", "i", 68), ("saem", "g", 64), ("da", "i", 68), ("+,", "g", 64, COR), ("entram", "g", 64), ("na", "i", 68), ("−", "g", 64, NEG)])))
        E.frase(c, t, C["s19.c"] + 1.6, ps("juntas = campo forte", "i", 64, TINTA2), 360, 900, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, tela)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("potencial", "g", 120, COR), ("elétrico", "g", 120, COR)], XE, 410)
    for i, r in enumerate((130, 210, 290)):
        q_ = ep(t, C["s20.a"] + 0.4 + 0.2 * i, 0.4)
        if q_ > 0:
            pt = M.paint(TINTA2, q_, stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
            c.drawCircle(560, 770, r, pt)
    F.carga(c, t, C["s20.a"] + 0.2, 560, 770, 56, "+")
    E.frase(c, t, C["s20.b"], [("e", "i", 66), ("o", "i", 66), ("trabalho", "g", 64)], 920, 800, passo=0.12)
    cta(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, campo=b_campo, carga=b_carga, linhas=b_linhas, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
