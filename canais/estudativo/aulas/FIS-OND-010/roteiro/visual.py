"""Visual — Estudativo · FIS-OND-010: espectro eletromagnético em ordem.

Linguagem visual: a da trilha Ondas e Som, escrita na docstring do visual.py da FIS-OND-001 (que segue a da Física,
FIS-CIN-001). Peças próprias desta aula: espectro() (faixa das sete regiões, arco-íris só no visível, frequência
crescendo para a direita), chirp() (onda com lambda diminuindo), atomo() (núcleo, órbita e elétron que escapa) e ícones
simples dos aparelhos. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-010_espectro_eletromagnetico_em_ordem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("luz", "ordem", "ioniza", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula: c = λ·f
C_LUZ = 3e8
assert 300_000 * 1000 == C_LUZ
assert 100e6 == 1e8 and C_LUZ / 1e8 == 3                           # FM 100 MHz → 3 m
assert C_LUZ / 1e6 == 300 and 8 - 6 == 2 and 3 * 10 ** 2 == 300     # AM → 300 m
assert abs(C_LUZ / 1e-10 - 3e18) < 1e3 and 8 + 10 == 18            # raio X → 3 × 10^18 Hz
assert abs((C_LUZ / (10 * 1e8)) - 3 / 10) < 1e-12                   # frequência ×10, lambda ÷10


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (copiadas da FIS-OND-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "3 m" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def bola_formula(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera escrita como fórmula ("3 × 10^{18}")"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    """conta em pilha: linhas = [(instante, fórmula[, cor])]; a linha da vez fica laranja até a próxima chegar"""
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete3(c, t, C, cena, itens, desenhos):
    """lembrete de três coisas: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita da caixa"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w, hh = 820, 1000, 200
    for i, (k, l1, l2) in enumerate(itens):
        y = 150 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 44, y + 80)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 155)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + hh / 2))
    q = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    q2 = ease_io(prog(t, C[itens[2][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, 330 + 240 * q + 240 * q2, ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[2][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 960, "left", 0.12)


# ---------------- peças desta aula ----------------
FAIXAS = (("rádio", 300), ("micro-ondas", 240), ("infravermelho", 240), ("visível", 110), ("ultravioleta", 240), ("raios X", 220), ("gama", 250))
ARCO_IRIS = ["#E53935", "#FB8C00", "#FDD835", "#43A047", "#1E88E5", "#3949AB", "#8E24AA"]


def espectro(c, t, ts, x0, y, w=1600, h=100, rotulos=True, size=40, escuro=False, apaga=(), a=1.0):
    """faixa do espectro, rádio → gama, com a frequência crescendo para a direita. ts = instante de cada região
    (lista de 7) ou um só (entram em fila). apaga = índices que ficam apagados. Devolve [(x_ini, x_fim)] de cada região"""
    if not isinstance(ts, (list, tuple)):
        ts = [ts + 0.12 * i for i in range(7)]
    k = w / sum(L for _, L in FAIXAS)
    xs, x = [], x0
    tinta = BR if escuro else TINTA
    for i, (nome, L) in enumerate(FAIXAS):
        xa, xb = x, x + L * k
        xs.append((xa, xb))
        x = xb
        q = ep(t, ts[i], 0.5) * a * (0.25 if i in apaga else 1.0)
        if q <= 0:
            continue
        r = skia.Rect.MakeXYWH(xa, y + h * 0.5 * (1 - ease_back(min(1, q / max(a, 1e-6)))), xb - xa, h * ease_back(min(1, q / max(a, 1e-6))))
        if nome == "visível":
            p = skia.Paint(AntiAlias=True)
            p.setShader(skia.GradientShader.MakeLinear([skia.Point(xa, 0), skia.Point(xb, 0)], [M.hexc(cc, q) for cc in ARCO_IRIS]))
            c.drawRect(r, p)
        else:
            tom = E.mix(E.COR, "#FFFFFF", 0.85 - 0.1 * i) if not escuro else E.mix(E.COR, "#07070F", 0.75 - 0.08 * i)
            c.drawRect(r, M.paint(tom, q))
        M.line(c, xb, y, xb, y + h, tinta, 0.5 * q, 2)
        if rotulos:
            yy = y + h + 52 if i % 2 == 0 else y + h + 104
            if nome == "visível":
                yy = y - 26
            E.foco(c, t, ts[i] + 0.1, 0.4, lambda aa, nome=nome, xa=xa, xb=xb, yy=yy, q=q: centro(c, nome, (xa + xb) / 2, yy, size, "b", tinta, aa * q / max(a, 1e-6) * a), sobe=6)
    return xs


def chirp(c, t, t0, x0, x1, y, A, l0=330, l1=14, d=1.4, cor=None, largura=6):
    """onda com o lambda diminuindo da esquerda (l0) para a direita (l1), desenhada da esquerda para a direita"""
    if t < t0:
        return
    pts, fase = [], 0.0
    n = int(x1 - x0)
    for i in range(n + 1):
        u = i / n
        lam = l0 * (l1 / l0) ** u
        fase += 2 * math.pi / lam
        pts.append((x0 + i, y - A * math.sin(fase)))
    F.poli(c, pts, ease_io(prog(t, t0, d)), cor or E.COR, 1.0, largura)


def atomo(c, cx, cy, r, a=1.0, sai=0.0, cor_e=None):
    """núcleo laranja, órbita em tinta e um elétron azul; sai de 0 a 1 leva o elétron para fora, para cima e à direita"""
    if a <= 0:
        return
    pt = M.paint(TINTA2, 0.6 * a, stroke=4)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - r * 0.45, 2 * r, r * 0.9), pt)
    c.save(); c.translate(cx, cy); c.rotate(60)
    c.drawOval(skia.Rect.MakeXYWH(-r, -r * 0.45, 2 * r, r * 0.9), pt)
    c.restore()
    E.bola(c, cx, cy, r * 0.28, E.COR, a)
    for ang in (200, 330):
        g = math.radians(ang)
        E.bola(c, cx + r * math.cos(g), cy + r * 0.45 * math.sin(g), r * 0.1, cor_e or F.NEG, a)
    g = math.radians(20)
    ex, ey = cx + r * math.cos(g), cy + r * 0.45 * math.sin(g)
    s = ease_out(sai)
    E.bola(c, lerp(ex, ex + r * 1.3, s), lerp(ey, ey - r * 0.9, s), r * 0.1, cor_e or F.NEG, a)
    if s > 0.05:
        E._meio(c, "−", lerp(ex, ex + r * 1.3, s), lerp(ey, ey - r * 0.9, s) - r * 0.22, r * 0.18, "g", F.NEG, a * s)


def radio(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.line(c, cx + s * 0.6, cy - s * 0.55, cx + s * 1.0, cy - s * 1.25, TINTA, a, 6)
    M.rrect(c, cx - s, cy - s * 0.6, 2 * s, s * 1.2, s * 0.2, TINTA, a)
    c.drawCircle(cx - s * 0.45, cy, s * 0.35, M.paint(E.COR, a))
    c.drawCircle(cx - s * 0.45, cy, s * 0.12, M.paint(TINTA, a))
    for k in range(3):
        M.line(c, cx + s * 0.15, cy - s * 0.25 + k * s * 0.25, cx + s * 0.8, cy - s * 0.25 + k * s * 0.25, BR, a * 0.8, 4)


def forno(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 1.2, cy - s * 0.7, s * 2.4, s * 1.4, s * 0.12, TINTA, a)
    M.rrect(c, cx - s * 1.05, cy - s * 0.55, s * 1.55, s * 1.1, s * 0.08, "#3A3A44", a)
    for i in range(7):
        for j in range(5):
            c.drawCircle(cx - s * 0.95 + i * s * 0.22, cy - s * 0.43 + j * s * 0.22, s * 0.035, M.paint(E.COR, 0.7 * a))
    for k in range(3):
        c.drawCircle(cx + s * 0.85, cy - s * 0.35 + k * s * 0.3, s * 0.08, M.paint(BR, a))


def lampada(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy - s * 0.2), s * 1.6, [M.hexc("#FFD54F", 0.55 * a), M.hexc("#FFD54F", 0)], [0, 1]))
    c.drawCircle(cx, cy - s * 0.2, s * 1.6, p)
    c.drawCircle(cx, cy - s * 0.2, s * 0.7, M.paint("#FFC107", a))
    M.rrect(c, cx - s * 0.32, cy + s * 0.4, s * 0.64, s * 0.5, s * 0.08, TINTA2, a)
    for k in range(3):
        M.line(c, cx - s * 0.32, cy + s * 0.5 + k * s * 0.13, cx + s * 0.32, cy + s * 0.5 + k * s * 0.13, BR, a * 0.7, 3)


def raiox(c, cx, cy, s, a=1.0):
    """filme de radiografia com um osso claro"""
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.8, cy - s, s * 1.6, s * 2, s * 0.1, "#1C2430", a)
    for dy in (-1, 1):
        for dx in (-1, 1):
            c.drawCircle(cx + dx * s * 0.16, cy + dy * s * 0.62, s * 0.19, M.paint("#F2F2F2", a))
    M.rrect(c, cx - s * 0.13, cy - s * 0.62, s * 0.26, s * 1.24, s * 0.05, "#F2F2F2", a)


def sol(c, cx, cy, r, a=1.0, giro=0.0):
    if a <= 0:
        return
    for k in range(12):
        g = math.radians(k * 30 + giro)
        M.line(c, cx + math.cos(g) * r * 1.25, cy + math.sin(g) * r * 1.25, cx + math.cos(g) * r * 1.6, cy + math.sin(g) * r * 1.6, "#FFB300", a, 7)
    E.bola(c, cx, cy, r, "#FFB300", a)


def setas_espectro(c, t, tf, tl, x0, x1, y, size=48, escuro=False):
    """frequência crescendo para a direita (laranja) e lambda crescendo para a esquerda (tinta)"""
    tinta = BR if escuro else TINTA
    q = ease_io(prog(t, tf, 0.6))
    if q > 0:
        F.seta(c, x0, y, lerp(x0, x1, q), y, E.COR if not escuro else CLARO, 1.0, 7, 28)
        E.foco(c, t, tf + 0.3, 0.4, lambda a: E.escreve(c, "frequência maior", x1 - 420, y - 22, size, "b", E.COR if not escuro else CLARO, a))
    q = ease_io(prog(t, tl, 0.6))
    if q > 0:
        F.seta(c, x1, y + 80, lerp(x1, x0, q), y + 80, tinta, 1.0, 7, 28)
        E.foco(c, t, tl + 0.3, 0.4, lambda a: E.formula(c, "λ maior", x0 + 30, y + 58, size, "b", tinta, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        itens = (("s01.a", "rádio", radio), ("s01.b", "micro-ondas", forno), ("s01.c", "lâmpada", lampada), ("s01.d", "raio X", raiox))
        for i, (k, nome, fn) in enumerate(itens):
            cx = 330 + i * 420
            E.foco(c, t, C[k], 0.5, lambda a, fn=fn, cx=cx: fn(c, cx, 430, 95, a))
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, nome=nome, cx=cx: centro(c, nome, cx, 640, 56, "i", TINTA, a))
        E.frase(c, t, C["s01.d"] + 1.2, ps("parecem muito diferentes", "i", 64, TINTA2), W / 2, 200, "center", 0.1)
        chirp(c, t, C["s01.e"], 160, 1760, 790, 50, d=1.6)
        E.frase(c, t, C["s01.e"], ps("o mesmo tipo de", "i", 76) + [("onda", "g", 76, COR)], W / 2, 960, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1520, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    itens = (("s02.a", "as ondas em ordem", "g", 1.2), ("s02.b", "c = λ · f", "g", 0), ("s02.c", "quem arranca elétrons", "g", 0))
    for i, (k, s, est, dt) in enumerate(itens):
        y = 450 + i * 170
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.formula_em(c, t, C[k] + dt + 0.1, s, XE + 110, y, 80, est, COR if i == 1 else TINTA)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def eq(a, x, y):
        F.onda(c, 99, 0, x - 130, x + 90, y, 28, 70, eixo=False) if a >= 0.99 else None

    def cient(a, x, y):
        E.formula(c, "3 × 10^{8}", x - 20, y + 22, 64, "g", TINTA, a, "center")

    def ion(a, x, y):
        atomo(c, x - 40, y, 62, a, 0.5)
    lembrete3(c, t, C, "s03", (("s03.b", "a equação da onda,", "v = λ · f"), ("s03.c", "contas em", "notação científica"),
                               ("s03.d", "átomo que perde elétron", "vira íon")), (eq, cient, ion))


# ---------------- a velocidade da luz ----------------
def b_luz(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("onda eletromagnética:", "i", 70), XE, 220, passo=0.1)
            E.frase(c, t, C["s04.a"], ps("anda até no", "i", 70) + [("vácuo", "g", 70, COR)], XE, 320, passo=0.1)
            E.foco(c, t, C["s04.b"], 0.6, lambda a: sol(c, 300, 620, 90, a, t * 8))
            E.foco(c, t, C["s04.b"] + 0.3, 0.6, lambda a: (E.bola(c, 1640, 620, 70, "#1E88E5", a), centro(c, "Terra", 1640, 760, 50, "i", TINTA, a)))
            F.onda(c, t, C["s04.b"] + 0.4, 450, 1540, 620, 40, 140, d=1.8, velocidade=120)
            E.foco(c, t, C["s04.b"] + 1.4, 0.4, lambda a: centro(c, "vácuo", 1000, 720, 50, "i", TINTA2, a))
        E.saida(c, t, C["s04.c"] - 0.1, s04)
        if t >= C["s04.c"]:  # três ondas, três lambdas, a mesma frente
            t0 = C["s04.c"]
            pilula(c, t, t0 + 0.3, "no vácuo, todas com a mesma velocidade", W / 2, 960, 56, E.COR)
            q = ease_io(prog(t, t0, 3.2))
            if q > 0:
                xf = lerp(520, 1700, q)
                M.line(c, xf, 220, xf, 860, COR, 0.8, 4, dash=E.TRACO)
            for i, (nome, lam, A) in enumerate((("rádio", 330, 60), ("luz", 90, 40), ("raio X", 26, 22))):
                y = 300 + i * 230
                F.onda(c, t, t0, 520, 1700, y, A, lam, d=3.2)
                E.foco(c, t, t0, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, XE, y + 18, 60, "b", TINTA, a))
        return
    if t < C["s06"]:
        def s05():
            E.foco(c, t, C["s05.a"], 0.5, lambda a: E.escreve(c, "c", XE, 470, 300, "g", COR, a))
            E.frase(c, t, C["s05.a"] + 0.2, ps("a velocidade da luz", "i", 76), XE + 260, 300, passo=0.12)
            E.foco(c, t, C["s05.b"], 0.5, lambda a: (E.escreve(c, "=", XE + 260, 470, 110, "g", TINTA2, a),
                                                     F.medida(c, "300.000", "km/s", XE + 380, 470, 120, TINTA, a)))
            E.foco(c, t, C["s05.c"], 0.5, lambda a: (E.escreve(c, "=", XE + 260, 680, 110, "g", TINTA2, a),
                                                     E.formula(c, "3 × 10^{8}", XE + 380, 680, 130, "g", COR, a)))
            E.foco(c, t, C["s05.c"] + 0.3, 0.5, lambda a: E.formula(c, "m/s", XE + 380 + E.formula(None, "3 × 10^{8}", 0, 0, 130, a=0) + 26, 680, 94, "b", F.UNID, a))
            pilula(c, t, C["s05.d"], "no ar: quase a mesma", XE + 600, 860, 56, TINTA, "b")
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    F.formula_legenda(c, t, C["s06.a"], "c = λ · f", [("c", "velocidade da luz", "m/s"), ("λ", "comprimento de onda", "m"), ("f", "frequência", "Hz")],
                      XE, 280, 150, size_l=54)
    E.frase(c, t, C["s06.b"], [("f", "g", 90, COR), ("sobe", "i", 90)], 1150, 330, passo=0.15)
    E.frase(c, t, C["s06.b"] + 1.0, [("λ", "g", 90), ("desce", "i", 90)], 1150, 470, passo=0.15)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: (E.pilula(c, "f × 10", 1300, 720, 70, "g", fundo=E.COR, a=a), F.seta(c, 1300, 790, 1300, 870, TINTA2, a, 7),
                                             E.pilula(c, "λ ÷ 10", 1300, 940, 70, "g", fundo=TINTA, a=a)))


# ---------------- a ordem ----------------
def b_ordem(c, t, C, b):
    if t < C["s08"]:
        ks = [C["s07." + k] for k in "abcdefg"]
        chirp(c, t, C["s07.a"], 160, 1760, 280, 60, d=lerp(1.2, C["s07.g"] - C["s07.a"] + 0.6, 1.0))
        E.frase(c, t, C["s07"], ps("da menor para a maior frequência", "i", 60, TINTA2), W / 2, 150, "center", 0.1)
        espectro(c, t, ks, 160, 420, size=42)
        setas_espectro(c, t, C["s07.a"] + 0.2, C["s07.h"], 260, 1660, 780, 50)
        E.frase(c, t, C["s07.h"] + 0.8, [("rádio:", "b", 54), ("o", "i", 58), ("maior", "g", 54), ("λ;", "g", 54), ("gama:", "b", 54), ("o", "i", 58), ("menor", "g", 54, COR)],
                W / 2, 1000, "center", 0.1)
        return
    if t < C["s09"]:
        def s08():
            xs = espectro(c, t, C["s08"] - 0.5, 160, 170, h=70, rotulos=False, apaga=(0, 1, 2, 4, 5, 6))
            xa, xb = xs[3]
            q = ep(t, C["s08.a"], 0.6)
            if q > 0:  # a fatia do visível se abre embaixo
                X0, X1, Y = 460, 1460, 430
                pt = M.paint(TINTA2, 0.5 * q, stroke=3)
                c.drawLine(xa, 240, X0, Y, pt); c.drawLine(xb, 240, X1, Y, pt)
                p = skia.Paint(AntiAlias=True)
                p.setShader(skia.GradientShader.MakeLinear([skia.Point(X0, 0), skia.Point(X1, 0)], [M.hexc(cc, q) for cc in ARCO_IRIS]))
                c.drawRect(skia.Rect.MakeXYWH(X0, Y, X1 - X0, 170 * q), p)
            E.frase(c, t, C["s08.a"], ps("uma faixa estreita no meio", "i", 56, TINTA2), W / 2, 120, "center", 0.1)
            E.frase(c, t, C["s08.b"], [("vermelho", "g", 64, "#E53935")], 460, 690)
            E.frase(c, t, C["s08.b"] + 0.6, ps("f menor", "b", 48, TINTA2), 460, 760)
            E.frase(c, t, C["s08.c"], [("violeta", "g", 64, "#8E24AA")], 1460, 690, "right")
            E.frase(c, t, C["s08.c"] + 0.6, ps("f maior", "b", 48, TINTA2), 1460, 760, "right")
            E.frase(c, t, C["s08.d"], [("infra", "g", 70, COR), ("=", "g", 70, TINTA2), ("abaixo", "i", 74)], XE, 900, passo=0.15)
            E.foco(c, t, C["s08.d"] + 0.8, 0.4, lambda a: E.escreve(c, "do vermelho", XE, 980, 50, "i", TINTA2, a))
            E.frase(c, t, C["s08.e"], [("ultra", "g", 70, COR), ("=", "g", 70, TINTA2), ("além", "i", 74)], 1750, 900, "right", 0.15)
            E.foco(c, t, C["s08.e"] + 0.8, 0.4, lambda a: E.escreve(c, "do violeta", 1500, 980, 50, "i", TINTA2, a))
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    E.frase(c, t, C["s09"], ps("rádio FM", "i", 80), XE, 220, passo=0.12)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: (E.escreve(c, "f =", XE, 380, 90, "g", TINTA, a), F.medida(c, "100", "MHz", XE + 190, 380, 90, COR, a)))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "= 1 × 10^{8} Hz", XE + 600, 380, 90, "g", TINTA, a))
    conta(c, t, [(C["s09.c"], "λ = f{c}{f} = f{3 × 10^{8}}{1 × 10^{8}}")], XE, 640, 0, 100)
    bola_txt(c, t, C["s09.d"], "3 m", 1500, 640, 150, 96)
    E.foco(c, t, C["s09.d"] + 0.5, 0.4, lambda a: centro(c, "a altura de um teto", 1500, 870, 50, "i", TINTA2, a))
    radio(c, 1500, 330, 70, ep(t, C["s09"], 0.5))


# ---------------- ionizante ----------------
def b_ioniza(c, t, C, b):
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], [("o", "i", 84), ("risco", "g", 84, ERRADO)], XE, 200)
            espectro(c, t, C["s10.a"] - 0.4, 160, 270, h=60, rotulos=False)
            q = ease_io(prog(t, C["s10.a"], 1.0))
            if q > 0:
                F.seta(c, 200, 390, lerp(200, 1720, q), 390, E.COR, 1.0, 10, 34)
                E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: E.escreve(c, "mais energia em cada átomo", 980, 460, 50, "b", COR, a))
            cx, cy = 1400, 720
            E.foco(c, t, C["s10.b"] - 0.6, 0.5, lambda a: atomo(c, cx, cy, 170, a, ep(t, C["s10.b"] + 0.8, 0.9)))
            # a radiação chega: onda curta vinda da esquerda
            F.onda(c, t, C["s10.b"], 700, 1170, 760, 26, 34, d=0.8, eixo=False)
            E.frase(c, t, C["s10.b"], ps("ultravioleta forte:", "i", 56), XE, 600, passo=0.1)
            E.frase(c, t, C["s10.b"] + 1.0, [("arranca", "g", 60, COR), ("elétrons", "g", 60)], XE, 680, passo=0.12)
            E.foco(c, t, C["s10.c"], 0.5, lambda a: (E.pilula(c, "íon", cx + 300, cy + 60, 60, "g", fundo=TINTA, a=a)))
            pilula(c, t, C["s10.d"], "IONIZANTE", 500, 960, 66, ERRADO)
            E.foco(c, t, C["s10.d"] + 0.8, 0.4, lambda a: E.escreve(c, "pode danificar as células", 860, 980, 52, "i", TINTA2, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    xs = espectro(c, t, C["s11"], 160, 380, size=42)
    xu = (xs[4][0] + xs[4][1]) / 2  # ultravioleta mais forte: da metade do UV em diante
    q = ep(t, C["s11.a"], 0.5)
    if q > 0:
        E.chave(c, 165, xs[3][1] - 5, 320, CERTO, q, -26, 6)
        E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: centro(c, "não ionizam", (165 + xs[3][1]) / 2, 260, 60, "g", CERTO, a))
    q = ep(t, C["s11.b"], 0.5)
    if q > 0:
        E.chave(c, xu, 1755, 320, ERRADO, q, -26, 6)
        E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: centro(c, "ionizam", (xu + 1755) / 2, 260, 60, "g", ERRADO, a))
        M.line(c, xu, 330, xu, 480, ERRADO, q, 5, dash=E.TRACO)
        E.foco(c, t, C["s11.b"] + 0.8, 0.4, lambda a: centro(c, "UV forte", xu, 640, 48, "b", ERRADO, a))
    E.frase(c, t, C["s11.c"], ps("usos e cuidados:", "i", 64) + [("próxima aula", "g", 64, COR)], W / 2, 900, "center", 0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)

    def s12a():
        E.frase(c, t, C["s12.a"], [("raio", "g", 90), ("X", "g", 90, COR), ("mais", "i", 96), ("rápido?", "g", 90, ERRADO)], XE, 370, passo=0.15)
        if t >= C["s12.a"] + 1.6:
            E.risco(c, XE - 10, 380, XE + 880, 280, t, C["s12.a"] + 1.6, largura=12)
    E.saida(c, t, C["s12.b"] - 0.1, s12a)
    if t < C["s12.b"]:
        return
    t0 = C["s12.b"]
    for i, (nome, lam, A) in enumerate((("rádio", 330, 60), ("raio X", 24, 24))):
        y = 400 + i * 230
        F.onda(c, t, t0, 520, 1700, y, A, lam, d=2.6)
        E.foco(c, t, t0, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, XE, y + 18, 60, "b", TINTA, a))
    q = ease_io(prog(t, t0, 2.6))
    if q > 0:
        xf = lerp(520, 1700, q)
        M.line(c, xf, 300, xf, 720, COR, 0.8, 4, dash=E.TRACO)
    E.foco(c, t, t0 + 2.0, 0.5, lambda a: (E.formula(c, "3 × 10^{8}", 1100, 800, 72, "g", CERTO, a),
                                           E.formula(c, "m/s", 1100 + E.formula(None, "3 × 10^{8}", 0, 0, 72, a=0) + 18, 800, 54, "b", F.UNID, a),
                                           E.escreve(c, "as duas:", 760, 800, 60, "i", TINTA, a)))
    E.frase(c, t, C["s12.c"], [("muda:", "i", 66), ("f", "g", 66, COR), ("e", "i", 66), ("λ.", "g", 66, COR), ("Nunca", "g", 62), ("a", "i", 66), ("velocidade", "g", 62)],
            W / 2, 960, "center", 0.12)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center")
    palavras = ("Rita", "Mandou", "Isabel", "Ver", "Uma", "Xícara", "Grande")
    nomes = ("rádio", "micro", "infra", "visível", "ultra", "X", "gama")
    size = 74
    ws = [E.larg(p, "g", size) for p in palavras]
    gap = 30
    x = W / 2 - (sum(ws) + gap * 6) / 2
    for i, (p, n, w_) in enumerate(zip(palavras, nomes, ws)):
        ti = C["s13.a"] + 0.25 * i
        cx = x + w_ / 2
        E.foco(c, t, ti, 0.4, lambda a, p=p, x=x: (E.escreve(c, p[0], x, 380, size, "g", CLARO, a),
                                                    E.escreve(c, p[1:], x + E.larg(p[0], "g", size) + E.APERTO["g"] * size, 380, size, "g", BR, a)))
        tn = C["s13.b"] + 0.3 * i
        E.foco(c, t, tn, 0.4, lambda a, n=n, cx=cx: centro(c, n, cx, 470, 44, "b", CLARO, a))
        x += w_ + gap
    if t < C["s13.d"]:
        setas_espectro(c, t, C["s13.c"], C["s13.c"] + 1.6, 260, 1660, 650, 50, escuro=True)
        E.foco(c, t, C["s13.c"] + 0.8, 0.4, lambda a: E.escreve(c, "e o risco", 1400, 720, 46, "i", CLARO, a))
        E.frase(c, t, C["s13.c"] + 3.6, ps("a ordem é sempre a mesma", "i", 56, CLARO), W / 2, 900, "center", 0.1)
    else:
        X0, X1, Y = 460, 1460, 640
        p = skia.Paint(AntiAlias=True)
        q = ep(t, C["s13.d"], 0.5)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(X0, 0), skia.Point(X1, 0)], [M.hexc(cc, q) for cc in ARCO_IRIS]))
        c.drawRect(skia.Rect.MakeXYWH(X0, Y, X1 - X0, 110), p)
        E.foco(c, t, C["s13.d"] + 0.8, 0.4, lambda a: (E.escreve(c, "vermelho: f menor", X0, Y + 190, 54, "b", BR, a)))
        E.foco(c, t, C["s13.d"] + 1.4, 0.4, lambda a: (E.formula(c, "violeta: f maior", X1, Y + 190, 54, "b", BR, a, "right")))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s14.a"], ps("rádio AM:", "i", 70), XE, 340, passo=0.1)
    E.foco(c, t, C["s14.a"] + 0.6, 0.5, lambda a: E.formula(c, "f = 1 × 10^{6} Hz", XE + 330, 340, 76, "g", COR, a))
    E.frase(c, t, C["s14.b"], ps("raio X:", "i", 70), XE, 480, passo=0.1)
    E.foco(c, t, C["s14.b"] + 0.6, 0.5, lambda a: E.formula(c, "λ = 1 × 10^{−10} m", XE + 330, 480, 76, "g", COR, a))
    E.frase(c, t, C["s14.c"], [("λ", "g", 70), ("da", "i", 70), ("rádio?", "g", 70, COR)], XE, 660, passo=0.12)
    E.frase(c, t, C["s14.c"] + 1.2, [("f", "g", 70), ("do", "i", 70), ("raio X?", "g", 70, COR)], XE, 770, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("qual é", "i", 70) + [("ionizante?", "g", 70, ERRADO)], XE, 900, passo=0.12)
    if t < C["s15"]:
        E.foco(c, t, C["s14.a"], 0.5, lambda a: radio(c, 1500, 350, 90, a))
        E.foco(c, t, C["s14.b"], 0.5, lambda a: raiox(c, 1500, 720, 120, a))
    else:
        E.relogio(c, t, C["s15.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s16():
        E.frase(c, t, C["s16"], ps("rádio AM", "i", 76), XE, 220, passo=0.12)
        conta(c, t, [(C["s16.a"], "λ = f{3 × 10^{8}}{10^{6}}"), (C["s16.b"], "= 3 × 10^{8 − 6} = 3 × 10^{2}")], XE, 430, 230, 96)
        bola_txt(c, t, C["s16.c"], "300 m", 1560, 600, 160, 90)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], ps("raio X", "i", 76), XE, 220, passo=0.12)
    conta(c, t, [(C["s17.a"], "f = f{3 × 10^{8}}{10^{−10}}"), (C["s17.b"], "= 3 × 10^{8} × 10^{10}")], XE, 430, 230, 96)
    E.foco(c, t, C["s17.b"] + 1.4, 0.4, lambda a: E.formula(c, "8 + 10 = 18", XE + 900, 660, 60, "b", TINTA2, a))
    bola_formula(c, t, C["s17.c"], "3 × 10^{18}", 1560, 470, 180, 66)
    E.foco(c, t, C["s17.c"] + 0.3, 0.4, lambda a: centro(c, "Hz", 1560, 740, 64, "b", F.UNID, a))
    pilula(c, t, C["s17.d"], "IONIZANTE: o raio X", XE + 330, 900, 60, ERRADO)
    E.frase(c, t, C["s17.e"], [("f", "g", 54, COR), ("muito", "i", 58), ("maior,", "i", 58), ("λ", "g", 54, COR), ("muito", "i", 58), ("menor", "i", 58)], 1400, 1000, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s18.a", "no vácuo, todas a c"), ("s18.b", "c = λ · f"), ("s18.c", "rádio → gama: f sobe, λ desce"), ("s18.d", "UV forte, X e gama: ionizam"))
        for i, (k, s) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.formula_em(c, t, C[k] + 0.1, s, 400, y, 70, "g", TINTA)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19"] + 0.8, [("cada", "i", 90), ("faixa,", "i", 90), ("seu", "i", 90), ("uso", "g", 96, COR)], XE, 380, passo=0.12)
    usos = ("celular", "forno", "controle remoto", "protetor solar", "radiografia")
    x, y = XE, 580
    for i, s in enumerate(usos):
        wp = E.larg(s, "g", 54) + 54 * 1.1
        if x + wp > 1250:
            x, y = XE, y + 130
        E.foco(c, t, C["s19.a"] + 0.3 * i, 0.4, lambda a, s=s, x=x, y=y, i=i, wp=wp: E.pilula(c, s, x + wp / 2, y, 54, "g", fundo=TINTA if i % 2 else E.COR, a=a))
        x += wp + 30
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.b"] + 0.2, 0.4))
    E.frase(c, t, C["s19.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, luz=b_luz, ordem=b_ordem, ioniza=b_ioniza, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
