"""Visual — Estudativo · QUI-LIG-006: geometria molecular. Primeira aula do módulo Polaridade e forças intermoleculares.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001) e a da trilha (QUI-LIG-001). Acrescenta, para este módulo:
- FORMA DA MOLÉCULA (forma()): bola-vareta com o átomo central maior, ligantes nas direções de cada geometria; dupla e
  tripla = varetas paralelas. PAR LIVRE = lobo translúcido turquesa (lobo()) com dois pontos azuis na ponta: ocupa
  espaço, mas não entra no nome da forma. Ângulo = arco fino em TINTA2 com o valor em grotesca ("104,5°").
- REGIÃO DE ELÉTRONS: número em bolinha escura sobre cada ligação e cada par livre ao contar; dupla e tripla valem 1.
- BALÕES (baloes()): a analogia da repulsão, em cores suaves, amarrados no centro.
- POLARIDADE (próximas aulas): δ+ e δ− em grotesca (E.escreve "g"), nunca na serifada; seta do dipolo na cor da matéria,
  apontando para o átomo mais eletronegativo; nuvem do par puxada para um lado = gradiente.
- FORÇAS ENTRE MOLÉCULAS: linha tracejada turquesa entre as moléculas; ligação de hidrogênio = tracejado mais grosso.
Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-006_geometria_molecular.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("repulsao", "formas", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# regiões = ligações (dupla e tripla valem 1) + pares livres
REG = {"CO2": (2, 0), "CH4": (4, 0), "NH3": (3, 1), "H2O": (2, 2), "H2S": (2, 2), "HCN": (2, 0)}
NOME = {(2, 0): "linear", (2, 1): "angular", (2, 2): "angular", (3, 0): "trigonal plana", (3, 1): "piramidal", (4, 0): "tetraédrica"}
assert NOME[REG["CO2"]] == "linear" and NOME[REG["CH4"]] == "tetraédrica" and NOME[REG["NH3"]] == "piramidal"
assert NOME[REG["H2O"]] == "angular" and NOME[REG["H2S"]] == "angular" and NOME[REG["HCN"]] == "linear"
assert 6 - 2 == 4 and 4 // 2 == 2   # H₂S: 6 de valência, 2 nas ligações, 2 pares livres


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


def lobo(c, cx, cy, ux, uy, L, a=1.0, escuro=False):
    """par livre: lobo translúcido saindo do centro na direção (ux, uy), com o par de elétrons na ponta"""
    if a <= 0:
        return
    ang = math.degrees(math.atan2(uy, ux))
    c.save()
    c.translate(cx, cy)
    c.rotate(ang)
    r = skia.Rect.MakeLTRB(L * 0.15, -L * 0.34, L * 1.05, L * 0.34)
    pf = skia.Paint(AntiAlias=True)
    pf.setShader(skia.GradientShader.MakeLinear([skia.Point(0, 0), skia.Point(L, 0)], [M.hexc(E.COR, 0.05 * a), M.hexc(E.COR, 0.32 * a)], [0, 1]))
    c.drawOval(r, pf)
    c.drawOval(r, M.paint(E.COR, 0.6 * a, stroke=3))
    for s_ in (-1, 1):
        c.drawCircle(L * 0.75, s_ * L * 0.09, L * 0.055, M.paint(Q.ELETRON, a))
    c.restore()


DIRS = {
    "linear": [(-1, 0), (1, 0)],
    "trigonal": [(0, -1), (-0.87, 0.5), (0.87, 0.5)],
    "tetra": [(0, -1), (-0.94, 0.33), (0.47, 0.6), (0.6, -0.12)],
    "angular": [(-0.78, 0.62), (0.78, 0.62)],
}


def forma(c, t, t0, central, ligantes, dirs, cx, cy, L=210, lobos=(), ordem=None, a=1.0, passo=0.2, tl=None, escuro=False, r_c=70, r_l=50):
    """molécula com geometria: central em (cx, cy); ligantes nas direções dirs (unidades); lobos = direções dos pares livres.
    ordem = ordem de ligação de cada ligante (2 = dupla). tl = instante de cada ligante. Varetas por baixo, átomos por cima"""
    if t < t0:
        return
    ordem = ordem or [1] * len(ligantes)
    for k, (ux, uy) in enumerate(lobos):
        lobo(c, cx, cy, ux, uy, L * 0.95, a * ep(t, t0 + 0.3 + 0.2 * k, 0.4), escuro)
    ts = tl or [t0 + 0.3 + passo * k for k in range(len(ligantes))]
    atras = [3] if dirs is DIRS["tetra"] and len(ligantes) == 4 else []
    pos = []
    for k in range(len(ligantes)):
        ux, uy = dirs[k]
        n = math.hypot(ux, uy)
        ux, uy = ux / n, uy / n
        q = ease_back(prog(t, ts[k], 0.45))
        pos.append((cx + ux * L, cy + uy * L, q))
        if q <= 0:
            continue
        nx, ny = -uy, ux
        offs = {1: (0,), 2: (-1, 1), 3: (-1.4, 0, 1.4)}[ordem[k]]
        for o in offs:
            M.line(c, cx + nx * o * 9, cy + ny * o * 9, cx + ux * L + nx * o * 9, cy + uy * L + ny * o * 9, Q.LIGA, a * min(1, q), 12 if ordem[k] == 1 else 8)
    for k in atras:
        x2, y2, q = pos[k]
        if q > 0:
            Q.atomo(c, x2, y2, r_l * q * 0.85, ligantes[k], a * 0.8, escuro=escuro)
    E.foco(c, t, t0, 0.4, lambda aa: Q.atomo(c, cx, cy, r_c, central, a * aa, escuro=escuro))
    for k in range(len(ligantes)):
        x2, y2, q = pos[k]
        if k not in atras and q > 0:
            Q.atomo(c, x2, y2, r_l * q, ligantes[k], a, escuro=escuro)


def angulo(c, t, t0, cx, cy, d1, d2, R, rot, a=1.0, cor=TINTA2):
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    a1 = math.degrees(math.atan2(d1[1], d1[0]))
    a2 = math.degrees(math.atan2(d2[1], d2[0]))
    sw = (a2 - a1) % 360
    if sw > 180:
        a1, sw = a2, 360 - sw
    c.drawArc(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), a1, sw * ease_out(prog(t, t0, 0.5)), False, M.paint(cor, q, stroke=4))
    am = math.radians(a1 + sw / 2)
    E.formula(c, rot, cx + (R + 70) * math.cos(am), cy + (R + 70) * math.sin(am) + 18, 50, "g", cor, q, "center")


def baloes(c, t, t0, n, cx, cy, L=150, a=1.0):
    cores = ("#FF8FA3", "#FFC857", "#7FD1E8", "#B39DDB")
    dirs = {2: [(-1, 0), (1, 0)], 3: DIRS["trigonal"], 4: DIRS["tetra"]}[n]
    q = ease_back(prog(t, t0, 0.6))
    if q <= 0:
        return
    for k, (ux, uy) in enumerate(dirs):
        nn = math.hypot(ux, uy)
        ux, uy = ux / nn, uy / nn
        bx, by = cx + ux * L * q, cy + uy * L * q
        M.line(c, cx, cy, bx - ux * 40, by - uy * 40, TINTA2, a, 3)
        c.save(); c.translate(bx, by); c.rotate(math.degrees(math.atan2(uy, ux)))
        pp = skia.Paint(AntiAlias=True)
        pp.setShader(skia.GradientShader.MakeRadial(skia.Point(10, -12), 60, [M.hexc("#FFFFFF", 0.9 * a), M.hexc(cores[k], a)], [0, 1]))
        c.drawOval(skia.Rect.MakeLTRB(-40, -34, 44, 34), pp)
        c.restore()
    E.bola(c, cx, cy, 12, TINTA, a)


def regiao_n(c, t, t0, x, y, n, a=1.0):
    E.foco(c, t, t0, 0.3, lambda aa: (E.bola(c, x, y, 26, TINTA, a * aa), centro(c, str(n), x, y + 13, 34, "g", BR, a * aa)))


# formas das quatro moléculas
def _r(L):
    return dict(r_c=min(70, L * 0.34), r_l=min(50, L * 0.25))


def co2(c, t, t0, cx, cy, L=220, a=1.0, escuro=False):
    forma(c, t, t0, "C", ["O", "O"], DIRS["linear"], cx, cy, L, ordem=[2, 2], a=a, escuro=escuro, **_r(L))


def ch4(c, t, t0, cx, cy, L=200, a=1.0, escuro=False):
    forma(c, t, t0, "C", ["H"] * 4, DIRS["tetra"], cx, cy, L, a=a, escuro=escuro, **_r(L))


PIR = [(-0.92, 0.42), (0.92, 0.42), (0.2, 0.72)]


def nh3(c, t, t0, cx, cy, L=200, a=1.0, escuro=False):
    forma(c, t, t0, "N", ["H"] * 3, PIR, cx, cy, L, lobos=[(0, -1)], a=a, escuro=escuro, **_r(L))


def h2o(c, t, t0, cx, cy, L=210, a=1.0, escuro=False, lobos=True):
    forma(c, t, t0, "O", ["H", "H"], DIRS["angular"], cx, cy, L, lobos=[(-0.6, -0.8), (0.6, -0.8)] if lobos else (), a=a, escuro=escuro, **_r(L))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.formula_em(c, t, C["s01.a"], "H2O", 520, 250, 110, align="center")
        Q.formula_em(c, t, C["s01.a"] + 0.6, "CO2", 1400, 250, 110, align="center")
        E.frase(c, t, C["s01.b"], ps("um átomo no meio, preso a dois outros", "i", 56, TINTA2), W / 2, 360, "center", 0.08)
        h2o(c, t, C["s01.c"], 520, 600, 190, lobos=t >= C["s01.e"])
        pilula_em(c, t, C["s01.c"] + 0.6, "dobrada", 520, 860, 56, E.COR)
        co2(c, t, C["s01.d"], 1400, 640, 200)
        pilula_em(c, t, C["s01.d"] + 0.6, "reta", 1400, 860, 56, TINTA)
        E.frase(c, t, C["s01.e"], ps("quem dobra a água não aparece na fórmula", "i", 58), W / 2, 1010, "center", 0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    for k, s_ in enumerate(("linear", "angular", "piramidal", "tetraédrica")):
        pilula_em(c, t, C["s02.b"] + 0.35 * k, s_, XE + 150 + k * 380, 380, 60, E.COR if k % 2 == 0 else TINTA)
    E.frase(c, t, C["s02.c"], ps("contando os pares em volta do átomo do meio", "i", 60), XE, 540, passo=0.08)
    E.frase(c, t, C["s02.d"], [("+", "g", 66, COR), ("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)], XE, 660, passo=0.12)
    nh3(c, t, C["s02.c"] + 0.4, 1500, 870, 150)


# ---------------- lembrete ----------------
AGUA_LEWIS = [("H", -1, 0), ("O", 0, 0, [90, 0]), ("H", 0, 1)]


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 66, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("estrutura", "g", 76), ("de", "i", 80), ("Lewis", "g", 76, COR)], XE, 320, passo=0.12)
    E.frase(c, t, C["s03.b"], [("traço", "g", 60), ("=", "g", 60, TINTA2)] + ps("par compartilhado (simples, dupla, tripla)", "i", 58), XE, 460, passo=0.08)
    E.frase(c, t, C["s03.c"], [("par livre", "g", 60, COR), ("=", "g", 60, TINTA2)] + ps("o que sobra, fora das ligações", "i", 58), XE, 580, passo=0.08)
    pts = Q.lewis(c, t, C["s03.a"] + 0.4, AGUA_LEWIS, [(0, 1, 1), (1, 2, 1)], 1450, 760, 190, 130, tl=[C["s03.a"] + 0.4] * 3, tp=C["s03.c"])
    if t >= C["s03.c"]:
        q = ep(t, C["s03.c"], 0.4)
        E.caixa_pontilhada(c, 1450 - 70, 760 - 150, 140, 70, q, E.COR, prog_=q)
        E.caixa_pontilhada(c, 1450 + 70, 760 - 65, 80, 130, q, E.COR, prog_=q)


# ---------------- repulsão (s04–s06) ----------------
def b_repulsao(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("átomo", "g", 90), ("central", "g", 90, COR)], XE, 230, passo=0.15)
            E.frase(c, t, C["s04.a"] + 0.8, ps("o que se liga aos outros", "i", 62, TINTA2), XE, 320, passo=0.1)
            Q.lewis(c, t, C["s04.b"], AGUA_LEWIS, [(0, 1, 1), (1, 2, 1)], 560, 620, 180, 120, tl=[C["s04.b"]] * 3)
            Q.lewis(c, t, C["s04.c"], [("O", -1.1, 0, [90, 270]), ("C", 0, 0), ("O", 1.1, 0, [90, 270])], [(0, 1, 2), (1, 2, 2)], 1380, 640, 200, 120, tl=[C["s04.c"]] * 3)
            for cue, x, y in (("s04.b", 560, 620), ("s04.c", 1380, 640)):
                if t >= C[cue] + 0.5:
                    c.drawCircle(x, y, 80 + 4 * math.sin(t * 6), M.paint(E.COR, ep(t, C[cue] + 0.5, 0.4), stroke=6))
            E.frase(c, t, C["s04.d"], ps("a forma depende do que está em volta dele", "i", 60), W / 2, 960, "center", 0.08)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("pares de elétrons: negativos", "i", 64) + [("se repelem", "g", 60, COR)], XE, 200, passo=0.1)
            E.frase(c, t, C["s05.b"], ps("e se afastam o máximo que podem", "i", 58, TINTA2), XE, 290, passo=0.08)
            E.frase(c, t, C["s05.c"], ps("pense em balões amarrados pelo nó", "i", 58), XE, 400, passo=0.08)
            for k, (cue, n, nome) in enumerate((("s05.d", 2, "opostos"), ("s05.e", 3, "triângulo"), ("s05.f", 4, "tetraedro"))):
                x = 400 + 560 * k
                baloes(c, t, C[cue], n, x, 680, 150)
                E.foco(c, t, C[cue] + 0.4, 0.4, lambda a, x=x, n=n, nome=nome: (centro(c, f"{n} balões", x, 930, 54, "g", TINTA, a), centro(c, nome, x, 1000, 50, "i", TINTA2, a)))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    E.frase(c, t, C["s06"], [("região", "g", 76, COR), ("=", "g", 76, TINTA2)] + ps("direção com elétrons", "i", 76), XE, 220, passo=0.12)
    E.frase(c, t, C["s06.a"], ps("cada ligação vale uma", "i", 60), XE, 340, passo=0.1)
    E.frase(c, t, C["s06.b"], [("simples,", "i", 60), ("dupla", "g", 58, COR), ("ou", "i", 60), ("tripla", "g", 58, COR), ("vale 1", "g", 58)], XE, 430, passo=0.1)
    E.frase(c, t, C["s06.c"], ps("cada par livre também vale uma", "i", 60), XE, 520, passo=0.1)
    Q.lewis(c, t, C["s06.a"], [("O", -1.1, 0, [90, 270]), ("C", 0, 0), ("O", 1.1, 0, [90, 270])], [(0, 1, 2), (1, 2, 2)], 560, 790, 200, 110, tl=[C["s06.a"]] * 3)
    regiao_n(c, t, C["s06.b"], 450, 720, 1)
    regiao_n(c, t, C["s06.b"] + 0.3, 670, 720, 2)
    E.foco(c, t, C["s06.b"] + 0.7, 0.4, lambda a: centro(c, "C: 2 regiões", 560, 960, 56, "g", COR, a))
    Q.lewis(c, t, C["s06.c"], AGUA_LEWIS, [(0, 1, 1), (1, 2, 1)], 1400, 760, 180, 110, tl=[C["s06.c"]] * 3)
    for k, (x, y) in enumerate(((1310, 700), (1460, 850), (1400, 590), (1560, 760))):
        regiao_n(c, t, C["s06.c"] + 0.5 + 0.25 * k, x, y, k + 1)
    E.foco(c, t, C["s06.c"] + 1.8, 0.4, lambda a: centro(c, "O: 4 regiões", 1400, 1030, 56, "g", COR, a))


# ---------------- as quatro formas (s07–s10) ----------------
def painel(c, t, C, k, cues, desenha, titulo, linhas, nome, ang):
    E.frase(c, t, C[cues[0]] - 0.2, titulo, XE, 210, passo=0.12)
    for i, (cue, partes) in enumerate(linhas):
        E.frase(c, t, C[cue], partes, XE, 340 + i * 110, passo=0.1)
    desenha()
    E.foco(c, t, C[cues[-1]], 0.5, lambda a: E.pilula(c, nome, XE + 260, 860, 76, "g", fundo=E.COR, a=a))
    if ang:
        E.foco(c, t, C[cues[-1]] + 0.4, 0.4, lambda a: E.escreve(c, ang, XE + 30, 990, 60, "g", TINTA2, a))


def b_formas(c, t, C, b):
    MX, MY = 1350, 560
    if t < C["s08"]:
        E.saida(c, t, C["s08"] - 0.1, lambda: painel(c, t, C, 0, ("s07.a", "s07.c"),
            lambda: (co2(c, t, C["s07.a"], MX, MY, 260), angulo(c, t, C["s07.c"] + 0.3, MX, MY, (1, 0), (-1, 0.0001), 90, "180°")),
            [("gás carbônico", "g", 70, COR)], [("s07.a", ps("2 duplas, nenhum par livre", "i", 58)), ("s07.b", [("2 regiões:", "g", 58)] + ps("lados opostos", "i", 60))],
            "linear", "ângulo de 180°"))
        return
    if t < C["s09"]:
        E.saida(c, t, C["s09"] - 0.1, lambda: painel(c, t, C, 1, ("s08.a", "s08.c"),
            lambda: (ch4(c, t, C["s08.a"], MX, MY + 40, 230), angulo(c, t, C["s08.c"] + 0.3, MX, MY + 40, (0, -1), (-0.94, 0.33), 80, "109,5°")),
            [("metano", "g", 70, COR)], [("s08.a", ps("4 ligações simples", "i", 58)), ("s08.b", [("4 regiões:", "g", 58)] + ps("cantos do tetraedro", "i", 60))],
            "tetraédrica", "ângulos de 109,5°"))
        return
    if t < C["s10"]:
        E.saida(c, t, C["s10"] - 0.1, lambda: painel(c, t, C, 2, ("s09.a", "s09.f"),
            lambda: (nh3(c, t, C["s09.a"], MX, MY + 60, 230)),
            [("amônia", "g", 70, COR)], [("s09.a", ps("3 ligações + 1 par livre", "i", 58)), ("s09.c", [("4 regiões", "g", 58)] + ps("como no tetraedro", "i", 60)),
                                         ("s09.d", ps("o nome só olha os átomos", "i", 58, TINTA2)), ("s09.f", ps("N no topo, 3 H na base", "i", 58))],
            "piramidal", None))
        return
    painel(c, t, C, 3, ("s10.a", "s10.d"),
           lambda: (h2o(c, t, C["s10.a"], MX, MY + 20, 230), angulo(c, t, C["s10.d"] + 0.3, MX, MY + 20, DIRS["angular"][0], DIRS["angular"][1], 90, "104,5°")),
           [("água", "g", 70, COR)], [("s10.a", ps("2 ligações + 2 pares livres", "i", 58)), ("s10.b", [("4 regiões", "g", 58)] + ps("outra vez", "i", 60)),
                                     ("s10.c", ps("sem os pares: três átomos em V", "i", 58, TINTA2))],
           "angular", "cerca de 104,5°")


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("a água reta, como o gás carbônico?", "i", 62), XE + 460, 190, passo=0.1)
    forma(c, t, C["s11.a"] + 0.4, "O", ["H", "H"], DIRS["linear"], 560, 520, 200)
    if t >= C["s11.a"] + 1.4:
        E.risco(c, 300, 580, 820, 460, t, C["s11.a"] + 1.4, largura=12)
    E.foco(c, t, C["s11.a"] + 1.2, 0.4, lambda a: centro(c, "errado", 560, 700, 56, "g", ERRADO, a))
    E.frase(c, t, C["s11.b"], ps("o que muda são os pares livres", "i", 60), XE, 860, passo=0.1)
    co2(c, t, C["s11.c"], 1400, 340, 150)
    E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: centro(c, "C: nenhum par livre", 1400, 470, 50, "b", TINTA, a))
    h2o(c, t, C["s11.d"], 1400, 680, 140)
    E.foco(c, t, C["s11.d"] + 0.5, 0.4, lambda a: centro(c, "O: dois, empurram os H", 1400, 860, 50, "b", COR, a))
    E.frase(c, t, C["s11.e"], ps("sem desenhar Lewis, você erra a forma", "i", 60, TINTA2), XE, 980, passo=0.08)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 66, CLARO), W / 2, 120, "center", 0.12)
            E.frase(c, t, C["s12.a"], ps("no átomo central, conte", "i", 58, CLARO) + [("ligantes", "g", 56, BR)] + ps("e", "i", 58, CLARO) + [("pares livres", "g", 56, E.CLARO)], W / 2, 210, "center", 0.08)
            linhas = (("s12.d", "2 ligantes, 0 pares", "linear"), ("s12.e", "2 ligantes + par livre", "angular"),
                      ("s12.f", "3 ligantes, 0 pares", "trigonal plana"), ("s12.g", "3 ligantes + 1 par", "piramidal"),
                      ("s12.h", "4 ligantes", "tetraédrica"))
            for k, (cue, regra, nome) in enumerate(linhas):
                y = 340 + k * 140
                E.foco(c, t, C[cue], 0.4, lambda a, y=y, regra=regra, nome=nome: (E.escreve(c, regra, XE + 40, y, 54, "b", BR, a),
                                                                               E.escreve(c, "→", XE + 740, y, 54, "g", CLARO, a),
                                                                               E.escreve(c, nome, XE + 840, y, 58, "g", E.CLARO, a)))
            mini = {"s12.d": lambda: co2(c, t, C["s12.d"], 1640, 330, 80, escuro=True),
                    "s12.e": lambda: h2o(c, t, C["s12.e"], 1640, 470, 70, escuro=True),
                    "s12.f": lambda: forma(c, t, C["s12.f"], "C", ["H", "H", "O"], [(-0.87, 0.5), (0.87, 0.5), (0, -1)], 1640, 620, 70, ordem=[1, 1, 2], escuro=True, r_c=24, r_l=18),
                    "s12.g": lambda: nh3(c, t, C["s12.g"], 1640, 760, 70, escuro=True),
                    "s12.h": lambda: ch4(c, t, C["s12.h"], 1640, 920, 60, escuro=True)}
            for k, fn in mini.items():
                if t >= C[k]:
                    fn()
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], ps("par livre ocupa espaço, mas o nome só conta os átomos", "i", 58, BR), W / 2, 300, "center", 0.07)
    E.frase(c, t, C["s13.b"], ps("molécula de dois átomos:", "i", 62, CLARO) + [("sempre linear", "g", 60, E.CLARO)], W / 2, 520, "center", 0.1)
    Q.molecula(c, t, C["s13.b"] + 0.8, "HCl", 700, 720, 150, escuro=True)
    Q.molecula(c, t, C["s13.b"] + 1.2, "O2", 1220, 720, 150, escuro=True)
    E.frase(c, t, C["s13.c"], ps("nem precisa contar", "i", 60, CLARO), W / 2, 930, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14.a"], [("1", "g", 56, COR)] + ps("a geometria do", "i", 62), XE, 320, passo=0.08)
    Q.formula_em(c, t, C["s14.a"] + 0.6, "H2S", XE + 560, 330, 100)
    E.frase(c, t, C["s14.a"] + 1.0, ps("(cheiro de ovo podre)", "i", 50, TINTA2), XE + 60, 410, passo=0.08)
    E.frase(c, t, C["s14.b"], ps("o enxofre é da família do oxigênio", "i", 56, TINTA2), XE + 60, 500, passo=0.08)
    E.frase(c, t, C["s14.c"], [("2", "g", 56, COR)] + ps("a geometria do", "i", 62), XE, 680, passo=0.08)
    Q.formula_em(c, t, C["s14.c"] + 0.6, "HCN", XE + 560, 690, 100)
    E.frase(c, t, C["s14.c"] + 1.0, ps("(ácido cianídrico)", "i", 50, TINTA2), XE + 60, 770, passo=0.08)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s17"]:
        def s16():
            E.frase(c, t, C["s16"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
            Q.formula_em(c, t, C["s16"] + 0.4, "H2S", XE, 330, 120)
            E.frase(c, t, C["s16.a"], [("S:", "g", 58), ("6", "g", 58, COR)] + ps("de valência, como o O", "i", 60), XE, 470, passo=0.1)
            E.frase(c, t, C["s16.b"], ps("2 ligações usam 2; sobram 4:", "i", 58), XE, 580, passo=0.08)
            E.frase(c, t, C["s16.b"] + 1.6, [("2 pares livres", "g", 58, COR)], XE, 670, passo=0.1)
            forma(c, t, C["s16.b"], "S", ["H", "H"], DIRS["angular"], 1400, 560, 220, lobos=[(-0.6, -0.8), (0.6, -0.8)])
            E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "angular, como a água", XE + 330, 860, 64, "g", fundo=CERTO, a=a))
        E.saida(c, t, C["s17"] - 0.1, s16)
        return
    Q.formula_em(c, t, C["s17"], "HCN", XE, 260, 120)
    E.frase(c, t, C["s17.a"], ps("central: o carbono", "i", 60), XE + 420, 250, passo=0.1)
    Q.lewis(c, t, C["s17.b"], [("H", -1.1, 0), ("C", 0, 0), ("N", 1.1, 0, [0])], [(0, 1, 1), (1, 2, 3)], 700, 470, 200, 110, tl=[C["s17.b"]] * 3)
    E.foco(c, t, C["s17.c"], 0.4, lambda a: centro(c, "nenhum par livre no C", 700, 600, 50, "b", TINTA, a))
    regiao_n(c, t, C["s17.d"], 590, 400, 1)
    regiao_n(c, t, C["s17.d"] + 0.3, 810, 400, 2)
    forma(c, t, C["s17.d"], "C", ["H", "N"], DIRS["linear"], 1450, 470, 200, ordem=[1, 3])
    E.foco(c, t, C["s17.d"] + 0.5, 0.4, lambda a: E.pilula(c, "linear", 1450, 640, 64, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s17.e"], 0.4, lambda a: E.escreve(c, "cada traço da tripla = 1 região? → 4 regiões, tetraédrica", XE, 820, 50, "b", ERRADO, a))
    if t >= C["s17.e"] + 1.2:
        E.risco(c, XE - 10, 830, XE + 1480, 790, t, C["s17.e"] + 1.2, largura=8)
    E.frase(c, t, C["s17.e"] + 1.6, [("a tripla vale", "i", 62), ("1 região", "g", 60, COR)], XE, 940, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s18.a", ps("os pares em volta do central", "i", 64) + [("se afastam", "g", 62)]),
                 ("s18.b", [("ligação ou par livre", "g", 62)] + ps("= 1 região", "i", 64)),
                 ("s18.c", ps("o nome da forma", "i", 64) + [("só olha os átomos", "g", 62, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s19.a"], [("polaridade", "g", 120, COR)], XE, 400)
    E.frase(c, t, C["s19.b"], [("gás carbônico", "g", 58), ("apolar,", "i", 62), ("água", "g", 58), ("polar", "i", 62)], XE, 540, passo=0.1)
    co2(c, t, C["s19.b"] + 0.4, 520, 780, 130)
    h2o(c, t, C["s19.b"] + 0.8, 1060, 800, 120)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, repulsao=b_repulsao, formas=b_formas, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
