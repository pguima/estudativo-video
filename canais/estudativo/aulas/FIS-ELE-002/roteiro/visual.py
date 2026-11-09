"""Visual — Estudativo · FIS-ELE-002: lei de Coulomb.

Segue a linguagem visual da Física (FIS-CIN-001) e a da trilha Eletricidade (docstring do visual.py da FIS-ELE-001):
carga + laranja e − azul, força elétrica = seta laranja saindo da carga, ao longo da linha que liga as cargas; distância
em cota tracejada; unidades em cinza-tinta; atalho no palco escuro. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Eletricidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ELE-002_lei_de_coulomb.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("forca", "formula", "proporcao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
METAL = "#A3AAB4"

# todas as contas da aula
assert abs(9e9 * 2e-6 * 3e-6 / 3 ** 2 - 6e-3) < 1e-15 and 9 * 2 * 3 == 54 and 9 - 6 - 6 == -3 and 54 / 9 == 6
assert 36 / 2 ** 2 == 9 and 36 / 2 == 18 and 2 ** 2 == 4 and 3 ** 2 == 9
assert 45 * 3 == 135 and 135 / 9 == 15 and 45 / 3 == 15


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



def par(c, t, t0, x1, x2, y, s1, s2, k, r=56, rot=None, escuro=False, d=0.5):
    """duas cargas com a força em cada uma: k = comprimento da seta (px); se atraem quando os sinais são opostos"""
    F.carga(c, t, t0, x1, y, r, s1)
    F.carga(c, t, t0 + 0.15, x2, y, r, s2)
    if t < t0 + 0.5 or k <= 0:
        return
    a, p = ep(t, t0 + 0.5, 0.3), ease_out(prog(t, t0 + 0.5, d))
    atrai = s1 != s2
    for xc, lado in ((x1, 1), (x2, -1)):
        s = lado if atrai else -lado
        x0 = xc + s * (r + 12)
        F.seta(c, x0, y, x0 + s * k, y, E.COR, a, 9, None, p)
    if rot:
        E.foco(c, t, t0 + 0.8, 0.4, lambda a_: centro(c, rot, (x1 + x2) / 2, y - r - 50, 56, "g", COR, a_))


def cota(c, t, t0, x1, x2, y, rot, a=1.0):
    """distância entre duas cargas: tracejado com o rótulo embaixo"""
    q_ = ep(t, t0, 0.4) * a
    if q_ <= 0:
        return
    M.line(c, x1, y, x2, y, TINTA2, q_, 4, dash=E.TRACO)
    for x in (x1, x2):
        M.line(c, x, y - 18, x, y + 18, TINTA2, q_, 4)
    E.formula(c, rot, (x1 + x2) / 2, y + 70, 60, "g", TINTA, q_, "center")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 560
        u = ease_io(prog(t, C["s01.b"], 1.0))
        x1, x2 = 420, lerp(760, 1100, u)
        k = lerp(170, 42, ease_io(prog(t, C["s01.b"] + 0.9, 0.6)))
        par(c, t, C["s01"] + 0.2, x1, x2, y, "+", "−", k)
        cota(c, t, C["s01"] + 0.6, x1, x2, y + 120, "d" if u < 0.5 else "2d")
        troca(c, t, [(C["s01.a"], "36 N"), (C["s01.d"], "9 N")],
              lambda s, a: F.medida(c, s.split()[0], "N", (x1 + x2) / 2, y - 120, 90, CERTO if s.startswith("9") else TINTA, a, "center"))
        E.frase(c, t, C["s01.b"], [("dobrou", "i", 84), ("a", "i", 84), ("distância", "g", 80, COR)], XE, 220)
        E.frase(c, t, C["s01.b"] + 1.6, [("e", "i", 84), ("a", "i", 84), ("força?", "g", 80)], XE, 330)
        E.foco(c, t, C["s01.c"], 0.5, lambda a: E.pilula(c, "18 N?", 1560, 420, 80, "g", fundo=ERRADO, a=a))
        if t >= C["s01.d"]:
            E.risco(c, 1400, 470, 1720, 370, t, C["s01.d"], largura=12)
        E.foco(c, t, C["s01.d"] + 0.3, 0.5, lambda a: E.pilula(c, "9 N", 1560, 640, 90, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "lei de Coulomb", 1.4), ("s02.b", "por proporção", 0), ("s02.c", "quase sem conta", 0)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def sinais(a, x, y):
        q(c, x - 110, y - 40, 26, "+", a); q(c, x - 40, y - 40, 26, "+", a)
        F.seta(c, x - 150, y - 40, x - 200, y - 40, E.COR, a, 6, 18); F.seta(c, x, y - 40, x + 50, y - 40, E.COR, a, 6, 18)
        q(c, x - 110, y + 40, 26, "+", a); q(c, x - 40, y + 40, 26, "−", a)
    lembrete(c, t, C, "s03", (("s03.b", "mesmo sinal repele,", "opostos atraem"), ("s03.c", "o prefixo micro:", "µ = dez elevado a −6")),
             (sinais, lambda a, x, y: E.formula(c, "1 µC = 10^{−6} C", x - 60, y + 20, 50, "g", TINTA, a, "center")))


# ---------------- a força ----------------
def b_forca(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("força:", "g", 100, COR)], XE, 260)
        E.frase(c, t, C["s04.a"] + 0.6, ps("um puxão ou um empurrão", "i", 70), XE, 370, passo=0.12)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.escreve(c, "N", XE, 640, 240, "g", COR, a))
        E.frase(c, t, C["s04.b"] + 0.3, [("newton", "g", 90)], XE + 220, 560)
        E.frase(c, t, C["s04.b"] + 0.7, ps("a unidade de força", "i", 60, TINTA2), XE + 220, 640, passo=0.1)
        y = 840
        if t >= C["s04.c"]:
            M.line(c, 760, y, 1760, y, TINTA2, ep(t, C["s04.c"], 0.4), 4, dash=E.TRACO)
        par(c, t, C["s04"] + 0.4, 1060, 1460, y, "+", "−", 130)
        E.foco(c, t, C["s04.c"] + 0.4, 0.4, lambda a: E.pilula(c, "na linha que liga as cargas", 1260, 980, 40, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], [("forças", "i", 84), ("iguais", "g", 84, COR), ("e", "i", 84), ("opostas", "g", 84, COR)], W / 2, 220, "center", 0.12)
    y = 560
    F.carga(c, t, C["s05.a"], 620, y, 110, "+")
    F.carga(c, t, C["s05.a"] + 0.2, 1300, y, 40, "−")
    if t >= C["s05.a"] + 0.6:
        a, p = ep(t, C["s05.a"] + 0.6, 0.3), ease_out(prog(t, C["s05.a"] + 0.6, 0.5))
        F.seta(c, 740, y, 960, y, E.COR, a, 10, None, p)
        F.seta(c, 1250, y, 1030, y, E.COR, a, 10, None, p)
    E.foco(c, t, C["s05.a"] + 1.0, 0.4, lambda a: (F.medida(c, "F", "", 850, y - 50, 60, COR, a, "center"), F.medida(c, "F", "", 1140, y - 50, 60, COR, a, "center")))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "sentidos opostos", 995, y + 170, 46, "b", fundo=TINTA, a=a))
    E.frase(c, t, C["s05.c"], [("na", "i", 72), ("pequena", "g", 68), ("=", "g", 68, TINTA2), ("na", "i", 72), ("grande", "g", 68)], W / 2, 930, "center", 0.12)


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    def s06():
        E.foco(c, t, C["s06"] + 0.5, 0.5, lambda a: E.escreve(c, "Charles Coulomb · século XVIII", XE, 200, 50, "i", TINTA2, a))
        F.formula_legenda(c, t, C["s06.a"], "F = k · f{Q₁ · Q₂}{d^2}", [("F", "força", "N"), ("Q₁, Q₂", "cargas", "C"), ("d", "distância", "m")],
                          XE + 40, 430, 150, tl=[C["s06.b"], C["s06.c"], C["s06.d"]], size_l=60)
        y = 520
        par(c, t, C["s06.a"] + 0.6, 1220, 1680, y, "+", "+", 70, r=50)
        cota(c, t, C["s06.d"], 1220, 1680, y + 110, "d")
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], [("k", "g", 120, COR), ("é", "i", 90), ("constante", "i", 90)], XE, 280)
            w = E.formula(None, "k = 9 × 10^9", 0, 0, 120, a=0)
            E.formula_em(c, t, C["s07.a"] + 1.4, "k = 9 × 10^9", XE, 480, 120, "g", TINTA)
            E.foco(c, t, C["s07.a"] + 2.4, 0.5, lambda a: E.formula(c, "N · m^2/C^2", XE + w + 30, 480, 66, "b", F.UNID, a))
            E.foco(c, t, C["s07.a"] + 1.0, 0.4, lambda a: E.escreve(c, "no vácuo e no ar", XE, 590, 54, "i", TINTA2, a))
            E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "na conta: cargas sem o sinal", 640, 680, 52, "g", fundo=TINTA, a=a))
            for i, (s1, s2, rot) in enumerate((("+", "−", "atrai"), ("+", "+", "repele"))):
                x0 = 1260 + i * 0
                y = 680 + i * 190 - 95
                E.foco(c, t, C["s07.c"] + 0.4 * i, 0.4, lambda a, y=y, s1=s1, s2=s2, rot=rot: (q(c, 1240, y, 36, s1, a), q(c, 1340, y, 36, s2, a),
                                                                                          E.escreve(c, rot, 1420, y + 18, 56, "g", COR, a)))
            E.frase(c, t, C["s07.c"] - 0.3, ps("o sinal diz se", "i", 56, TINTA2), 1200, 500, passo=0.1)
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    y = 250
    E.foco(c, t, C["s08.a"], 0.5, lambda a: (q(c, 640, y, 44, "+", a), F.medida(c, 2, "µC", 640, y - 70, 56, TINTA, a, "center")))
    E.foco(c, t, C["s08.a"] + 0.6, 0.5, lambda a: (q(c, 1280, y, 44, "+", a), F.medida(c, 3, "µC", 1280, y - 70, 56, TINTA, a, "center")))
    if t >= C["s08.b"]:
        M.line(c, 700, y, 1220, y, TINTA2, ep(t, C["s08.b"], 0.4), 4, dash=E.TRACO)
        E.foco(c, t, C["s08.b"], 0.4, lambda a: F.medida(c, 3, "m", 960, y + 70, 56, TINTA, a, "center"))
    E.formula_em(c, t, C["s08.b"] + 1.0, "F = f{9 × 10^9 · 2 × 10^{−6} · 3 × 10^{−6}}{3^2}", W / 2, 500, 80, "g", TINTA, "center")
    E.formula_em(c, t, C["s08.c"], "9 · 2 · 3 = 54", 480, 740, 72, "g", COR, "center")
    E.formula_em(c, t, C["s08.d"], "10^{9 − 6 − 6} = 10^{−3}", 1060, 740, 72, "g", COR, "center")
    E.formula_em(c, t, C["s08.e"], "3^2 = 9", 1580, 740, 72, "g", COR, "center")
    E.formula_em(c, t, C["s08.f"], "54 ÷ 9 = 6", 560, 930, 72, "g", TINTA, "center")
    E.foco(c, t, C["s08.g"], 0.5, lambda a: pilula_f(c, "F = 6 × 10^{−3} N", 1280, 905, 76, a=a))


# ---------------- proporção ----------------
def b_proporcao(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09.a"], [("a", "i", 96), ("proporção", "g", 96, COR)], XE, 240)
        E.frase(c, t, C["s09.b"], ps("direta com cada carga", "i", 70), XE, 470, passo=0.12)
        E.formula_em(c, t, C["s09.c"], "Q × 2  →  F × 2", XE + 60, 600, 90, "g", COR)
        E.frase(c, t, C["s09.d"], ps("inversa com o", "i", 70) + [("quadrado", "g", 66, COR)] + ps("da distância", "i", 70), XE, 800, passo=0.12)
        E.foco(c, t, C["s09.d"] + 1.0, 0.5, lambda a: (E.formula(c, "f{1}{d^2}", XE + 120, 900, 100, "g", COR, a, "center"),
                                                      E.escreve(c, "o d vai ao quadrado, embaixo", XE + 260, 910, 54, "i", TINTA2, a)))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], [("distância", "i", 80), ("muda", "i", 80), ("→", "g", 76, TINTA2), ("força", "g", 76, COR)], W / 2, 200, "center", 0.12)
            linhas = (("s10.a", "s10.b", "d × 2", "2^2 = 4", "F ÷ 4"), ("s10.c", "s10.d", "d × 3", "3^2 = 9", "F ÷ 9"), ("s10.e", "s10.f", "d ÷ 2", "2^2 = 4", "F × 4"))
            for i, (k1, k2, d_, qd, f_) in enumerate(linhas):
                y = 400 + i * 200
                E.formula_em(c, t, C[k1], d_, 420, y, 96, "g", TINTA, "center")
                E.formula_em(c, t, C[k1] + 0.6, qd, 960, y, 80, "g", TINTA2, "center")
                E.foco(c, t, C[k2], 0.5, lambda a, y=y, f_=f_, i=i: pilula_f(c, f_, 1500, y - 28, 80, fundo=E.COR if i < 2 else CERTO, a=a))
                if t >= C[k1] + 0.3:
                    F.seta(c, 600, y - 28, 760, y - 28, TINTA2, ep(t, C[k1] + 0.3, 0.3), 6, 20)
                    F.seta(c, 1140, y - 28, 1300, y - 28, TINTA2, ep(t, C[k2], 0.3), 6, 20)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11"], ps("no começo da aula", "i", 80, TINTA2), W / 2, 260, "center", 0.12)
    E.formula_em(c, t, C["s11.a"], "36 N", W / 2 - 420, 560, 150, "g", TINTA, "center")
    E.formula_em(c, t, C["s11.b"], "÷ 4", W / 2, 560, 150, "g", COR, "center")
    E.foco(c, t, C["s11.c"], 0.5, lambda a: pilula_f(c, "9 N", W / 2 + 430, 510, 120, fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("esquecer o", "i", 80) + [("quadrado", "g", 80, ERRADO)], XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s12.a"] + 1.4, "d × 2  →  F ÷ 2", XE, 420, 100, "g", TINTA)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: pilula_f(c, "18 N", 1500, 385, 90, fundo=ERRADO, a=a))
    if t >= C["s12.b"] + 0.6:
        E.risco(c, XE - 10, 440, 1650, 340, t, C["s12.b"] + 0.6, largura=12)
    E.formula_em(c, t, C["s12.c"], "F = k · f{Q₁ · Q₂}{d^2}", XE, 680, 96, "g", TINTA)
    xd = XE + E.formula(None, "F = k · f{Q₁ · Q₂}{d^2}", 0, 0, 96, a=0) - E.formula(None, "f{Q₁ · Q₂}{d^2}", 0, 0, 96, a=0) / 2
    E.foco(c, t, C["s12.c"] + 0.6, 0.5, lambda a: c.drawCircle(xd, 712, 56, M.paint(ERRADO, a, stroke=6)))
    E.formula_em(c, t, C["s12.d"], "d × 2  →  F ÷ 2^2 = F ÷ 4", XE, 920, 96, "g", CERTO)
    E.foco(c, t, C["s12.d"] + 1.0, 0.5, lambda a: E.selo(c, 1660, 890, 60, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s13():
        E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s13.a"], ps("não refaça a conta inteira", "i", 70, CLARO), W / 2, 280, "center", 0.12)
        E.formula_em(c, t, C["s13.b"], "nova F = F × (mudança da carga)", W / 2, 450, 70, "g", BR, "center")
        E.formula_em(c, t, C["s13.c"], "÷ (mudança da distância)^2", W / 2, 560, 70, "g", CLARO, "center")
        E.formula_em(c, t, C["s13.d"], "Q × 2,  d × 3", W / 2, 760, 84, "g", BR, "center")
        E.foco(c, t, C["s13.e"], 0.5, lambda a: pilula_f(c, "F × f{2}{9}", W / 2, 920, 84, a=a))
    E.saida(c, t, C["s14"] - 0.1, s13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("k", "g", 80, BR), ("não", "i", 80, CLARO), ("muda", "i", 80, CLARO)], W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s14.a"] + 1.0, ps("o resto é vezes e dividido", "i", 64, CLARO), W / 2, 390, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("não", "g", 66, ERRADO), ("compensa:", "i", 70, CLARO)], W / 2, 620, "center", 0.12)
    E.frase(c, t, C["s14.b"] + 0.8, ps("sem uma força de partida", "i", 70, BR), W / 2, 730, "center", 0.12)
    E.frase(c, t, C["s14.b"] + 2.0, [("→", "g", 64, CLARO), ("fórmula", "g", 64, BR), ("inteira", "g", 64, BR)], W / 2, 860, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"] - 0.6, [("se", "i", 80), ("repelem", "i", 80), ("com", "i", 80)], XE, 340)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: F.medida(c, 45, "N", XE + 560, 340, 100, COR, a))
    E.frase(c, t, C["s15.b"], [("uma", "i", 80), ("carga", "i", 80), ("×", "g", 80, COR), ("3", "g", 80, COR)], XE, 500, passo=0.15)
    E.frase(c, t, C["s15.c"], [("distância", "i", 80), ("×", "g", 80, COR), ("3", "g", 80, COR)], XE, 640, passo=0.15)
    E.frase(c, t, C["s15.d"], [("nova", "i", 84), ("força?", "g", 84, COR)], XE, 820, passo=0.15)

    def desenho():
        y = 470
        u = ease_io(prog(t, C["s15.c"], 0.9))
        x2 = lerp(1450, 1760, u)
        par(c, t, C["s15.a"], 1250, x2, y, "+", "+", 70, r=46)
        cota(c, t, C["s15.a"] + 0.5, 1250, x2, y + 120, "d" if u < 0.5 else "3d")
    questao_relogio(c, t, C, "s16", desenho)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17.a"], [("carga", "i", 76), ("×", "g", 76, COR), ("3", "g", 76, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s17.b"], [("distância", "i", 76), ("×", "g", 76, COR), ("3", "g", 76, COR), ("→", "g", 76, TINTA2), ("÷", "g", 76, COR), ("3²", "g", 76, COR),
                               ("=", "g", 76, TINTA2), ("÷", "g", 76, COR), ("9", "g", 76, COR)], XE, 340, passo=0.12)
    E.formula_em(c, t, C["s17.c"], "45 × 3 = 135", XE, 540, 96, "g", TINTA)
    E.formula_em(c, t, C["s17.d"], "135 ÷ 9 =", XE, 700, 96, "g", TINTA)
    E.foco(c, t, C["s17.e"], 0.5, lambda a: pilula_f(c, "15 N", XE + 700, 665, 96, fundo=CERTO, a=a))
    E.foco(c, t, C["s17.f"], 0.5, lambda a: (E.formula(c, "f{3}{9} = f{1}{3}", 1500, 520, 90, "g", COR, a, "center"),
                                            E.formula(c, "f{1}{3} de 45 = 15", 1500, 760, 80, "g", TINTA, a, "center")))
    E.foco(c, t, C["s17.f"] - 0.4, 0.4, lambda a: E.pilula(c, "mais rápido", 1500, 380, 44, "b", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela():
        resumo(c, t, C, "s18", (("s18.a", [("F = k · Q₁ · Q₂ ÷ d²", "g", 70)]),
                                ("s18.b", [("cargas", "i", 72), ("×", "g", 68, COR), ("2", "g", 68, COR), ("→", "g", 68, TINTA2), ("F", "g", 68), ("×", "g", 68, COR), ("2", "g", 68, COR)]),
                                ("s18.c", [("distância", "i", 72), ("×", "g", 68, COR), ("2", "g", 68, COR), ("→", "g", 68, TINTA2), ("F", "g", 68), ("÷", "g", 68, COR), ("4", "g", 68, COR)])))
    E.saida(c, t, C["s19"] - 0.1, tela)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("campo", "g", 120, COR), ("elétrico", "g", 120, COR)], XE, 410)
    F.campo_carga(c, t, C["s19.a"] + 0.6, 640, 760, 80, 230, n=10)
    F.carga(c, t, C["s19.a"] + 0.3, 640, 760, 60, "+")
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.escreve(c, "linhas de força", 940, 780, 56, "i", TINTA2, a))
    cta(c, t, C, "s19")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, forca=b_forca, formula=b_formula, proporcao=b_proporcao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
