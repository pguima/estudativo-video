"""Visual — Estudativo · FIS-EGF-003: gravitação universal.

Segue a linguagem visual da Física (visual.py da FIS-CIN-001) e a da trilha Equilíbrio, Gravitação e Fluidos (cabeçalho do
visual.py da FIS-EGF-001): eixo e braço em cota, giro horário laranja e anti-horário azul, astros (Sol âmbar, Terra azul),
fluidos em azul translúcido, pressão em setinhas laranja, empuxo azul. O kit da trilha vem copiado logo abaixo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Equilíbrio, Gravitação e Fluidos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-EGF-003_gravitacao_universal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "proporcao", "gravidade", "atalho", "questao", "fim"))

# todas as contas da aula
assert 10 * 2 / 2 ** 2 == 5 and 3 / 2 ** 2 == 0.75 and 1 / 3 ** 2 == 1 / 9 and 1 / 0.5 ** 2 == 4
assert abs(10 * 0.1 / 0.5 ** 2 - 4) < 1e-9 and 70 * 4 == 280 and 70 * 10 == 700 and 6400 * 2 == 12800


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- kit da trilha (o mesmo em todas as aulas FIS-EGF) ----------------
BR = "#FFFFFF"
MADEIRA, MADEIRA2 = "#B07A4A", "#7E5432"
AGUA, AGUA2, OLEO = "#5AB4E6", "#2C86C2", "#E9B44C"
SOL, TERRA, LUA = "#FFB020", "#2F6FB0", "#A9A9B4"


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def linhas(c, t, itens, x, y0, dy, size=72, align="left", est="g"):
    """passo a passo: itens = [(instante, "fórmula", cor)], uma linha por etapa, de cima para baixo"""
    for i, it in enumerate(itens):
        t0, s, cor = it[0], it[1], (it[2] if len(it) > 2 else TINTA)
        E.formula_em(c, t, t0, s, x, y0 + i * dy, size, est, cor, align)


def cota(c, t, t0, A, B, rot, cor=TINTA2, size=46, lado=-1, d=0.5, cor_txt=None):
    """linha de medida de A até B, com tracinhos nas pontas e o rótulo no meio, do lado `lado` (−1 = acima/esquerda)"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    ux, uy = E._uni(*A, *B)
    nx, ny = -uy, ux
    M.line(c, *A, lerp(A[0], B[0], q), lerp(A[1], B[1], q), cor, 1.0, 4)
    for P_ in (A, B):
        M.line(c, P_[0] - nx * 16, P_[1] - ny * 16, P_[0] + nx * 16, P_[1] + ny * 16, cor, q, 4)
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    E.foco(c, t, t0 + d * 0.6, 0.4, lambda a: E._meio(c, rot, mx + nx * lado * (size * 0.8), my + ny * lado * (size * 0.8), size, "b", cor_txt or E.COR_TEXTO, a))


def seta_giro(c, cx, cy, r, ini, varre, cor, a=1.0, largura=9, p=1.0):
    """arco com ponta de seta: o sentido do giro. ini e varre em graus de tela (varre > 0 = horário)"""
    if a <= 0 or p <= 0:
        return
    v = varre * p
    E.arco(c, cx, cy, r, ini, v, cor, largura, a)
    g = math.radians(ini + v)
    x, y = cx + r * math.cos(g), cy + r * math.sin(g)
    s = 1 if v > 0 else -1
    ux, uy = -math.sin(g) * s, math.cos(g) * s
    F._cabeca(c, x + ux * largura * 1.6, y + uy * largura * 1.6, ux, uy, largura * 3.2, cor, a)


def apoio(c, x, y, s=70, a=1.0, escuro=False):
    """apoio triangular com o vértice (o eixo) em (x, y)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(x - s * 0.7, y + s); p.lineTo(x + s * 0.7, y + s); p.close()
    c.drawPath(p, M.paint(BR if escuro else TINTA, a))
    c.drawCircle(x, y, s * 0.13, M.paint(E.COR, a))


def lembrete(c, t, C, cena, itens, numero, palavra="coisas"):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)], uma caixa por item"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de" if palavra == "coisas" else "você vai usar", "i", 80), XE, 410, passo=0.14)
    t1 = C.get(cena + ".a", C[cena] + 0.6) if hasattr(C, "get") else C[cena] + 0.6
    E.foco(c, t, t1, 0.5, lambda a: E.escreve(c, str(numero), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, t1 + 0.15, 0.5, lambda a: E.escreve(c, palavra, XE + 215, 700, 110 if palavra == "coisas" else 84, "i", TINTA, a))
    x, w = 820, 1000
    h = {2: 230, 3: 190, 4: 150}[n]
    gap = {2: 290, 3: 230, 4: 180}[n]
    y0 = {2: 230, 3: 150, 4: 140}[n]
    s1, s2 = {2: (58, 58), 3: (50, 52), 4: (44, 46)}[n]
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s2, COR)], x + 44, y + h * 0.4 + s2 * 1.3)
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 50, COR) + ps("procure no canal", "i", 50), 820, 1010, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """até o fim da aula: itens = [(cue, texto)] numerados, com a órbita à direita"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 450 + i * 160
        dt = 1.2 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, cena, itens):
    """itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 26, 52, a=a), centro(c, str(i + 1), 230, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.1)


def proxima(c, t, C, cena, l1, l2, desenho=None, k=("a", "c", "d")):
    """próxima aula + inscreva-se + bons estudos; desenho(a) ilustra a próxima aula na metade de baixo"""
    E.frase(c, t, C[cena], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[f"{cena}.{k[0]}"], l1, XE, 400)
    if l2:
        E.frase(c, t, C[f"{cena}.{k[0]}"] + 0.5, l2, XE, 540)
    if desenho:
        desenho()
    E.foco(c, t, C[f"{cena}.{k[1]}"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[f"{cena}.{k[1]}"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[f"{cena}.{k[1]}"] + 0.2, 0.4))
    E.frase(c, t, C[f"{cena}.{k[2]}"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def hora_testar(c, t, C, cena):
    E.frase(c, t, C[cena], ps("hora de testar", "i", 72, COR), XE, 180)




def empurra(c, t, t0, P, ang, comp, rot=None, modulo=None, cor=None):
    """força que CHEGA ao ponto P vindo da direção oposta a ang (graus da Física): a ponta encosta no corpo"""
    dx, dy = F._dir(ang)
    F.vetor(c, t, t0, (P[0] - dx * comp, P[1] - dy * comp), P, rot, modulo, cor, 10, em=0.4)


# ---------------- peças desta aula ----------------
MARTE = "#C4512A"


def par(c, t, t0, A, B, rA, rB, comp, corA=TERRA, corB=LUA, rot=("F", "F"), d=0.5, a=1.0):
    """dois corpos que se atraem: setas iguais, uma em cada um, apontando para o outro"""
    q = ep(t, t0, d) * a
    if q <= 0:
        return
    E.bola(c, *A, rA, corA, q)
    E.bola(c, *B, rB, corB, q)
    ux, uy = E._uni(*A, *B)
    if comp > 4:
        F.vetor(c, t, t0 + 0.3, (A[0] + ux * (rA + 8), A[1] + uy * (rA + 8)), (A[0] + ux * (rA + 8 + comp), A[1] + uy * (rA + 8 + comp)), rot[0], None, E.COR, 9, lado=-1)
        F.vetor(c, t, t0 + 0.3, (B[0] - ux * (rB + 8), B[1] - uy * (rB + 8)), (B[0] - ux * (rB + 8 + comp), B[1] - uy * (rB + 8 + comp)), rot[1], None, E.COR, 9, lado=1)


def maca(c, x, y, r, a=1.0):
    if a <= 0:
        return
    E.bola(c, x, y, r, "#D8342C", a)
    M.line(c, x, y - r * 0.9, x + r * 0.15, y - r * 1.4, "#5A3A1E", a, max(3, r * 0.12))
    p = skia.Path(); p.addOval(skia.Rect.MakeXYWH(x + r * 0.15, y - r * 1.45, r * 0.6, r * 0.3))
    c.drawPath(p, M.paint("#3E9B3E", a))


def corpo_cai(c, x, y, s, a=1.0, cor=None):
    F.bloco(c, x, y, s, s, None, cor=cor, a=a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            # a maçã cai; a Lua gira; a mesma força
            ya = lerp(330, 760, ease_io(prog(t, C["s01.a"] + 0.6, 1.0)) ** 2)
            E.foco(c, t, C["s01.a"], 0.5, lambda a: maca(c, 520, ya, 40, a))
            if t >= C["s01.a"]:
                F.chao(c, 300, 760, 806, ep(t, C["s01.a"], 0.4))
            F.vetor(c, t, C["s01.a"] + 0.4, (600, 380), (600, 520), None, None, E.COR, 9)
            q = ep(t, C["s01.b"], 0.6)
            if q > 0:
                E.bola(c, 1350, 560, 150, TERRA, q)
                pt = M.paint(TINTA, 0.6 * q, stroke=4); pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
                c.drawCircle(1350, 560, 360, pt)
                g = 0.4 * (t - C["s01.b"]) + 2.2
                L = (1350 + 360 * math.cos(g), 560 - 360 * math.sin(g))
                E.bola(c, *L, 44, LUA, q)
                ux, uy = E._uni(*L, 1350, 560)
                F.seta(c, L[0] + ux * 54, L[1] + uy * 54, L[0] + ux * 170, L[1] + uy * 170, E.COR, q, 9)
            E.frase(c, t, C["s01.a"], ps("a força que derruba a maçã", "i", 60), XE, 180, passo=0.1)
            E.frase(c, t, C["s01.b"], [("=", "g", 60, TINTA2)] + ps("a que segura a Lua", "i", 60), XE, 270, passo=0.1)
            E.frase(c, t, C["s01.c"], [("Isaac", "i", 76), ("Newton", "g", 76, COR)], XE, 960, passo=0.15)
            pilula_em(c, t, C["s01.d"], "uma fórmula só", 1350, 1000, 50, E.COR)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "a fórmula por proporção"), ("s02.b", "sem decorar número"), ("s02.c", "a gravidade de um planeta")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o peso:", "P = m · g"), ("s03.c", "as leis de Kepler:", "planetas em órbita do Sol")), 2)


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("todo corpo com massa", "i", 70) + [("atrai", "g", 70, COR)] + ps("todo outro", "i", 70), XE, 200, passo=0.12)
            E.foco(c, t, C["s04.b"], 0.5, lambda a: (E.bola(c, 1350, 800, 230, TERRA, a)))
            E.foco(c, t, C["s04.b"], 0.5, lambda a: F.bloco(c, 1350, 515, 80, 110, None, a=a))
            F.vetor(c, t, C["s04.b"] + 0.4, (1350, 515), (1350, 620), None, None, E.COR, 10, lado=-1)
            F.vetor(c, t, C["s04.b"] + 1.0, (1350, 800), (1350, 695), None, None, E.COR, 10, lado=-1)
            c.drawCircle(1350, 800, 8, M.paint(BR, ep(t, C["s04.b"] + 1.0, 0.3)))
            E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.escreve(c, "a Terra puxa você", 1420, 560, 46, "i", TINTA, a))
            E.foco(c, t, C["s04.b"] + 1.0, 0.4, lambda a: E.escreve(c, "você puxa a Terra", 1420, 1080 - 30, 46, "i", TINTA, a))
            E.frase(c, t, C["s04.c"], [("3ª lei:", "g", 60)] + ps("mesmo valor,", "i", 62) + [("sentidos opostos", "g", 60, COR)], XE, 360, passo=0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            F.formula_legenda(c, t, C["s05.a"], "F = f{G · M · m}{d^2}",
                              [("M, m", "as massas", "kg"), ("d", "distância entre os centros", "m"), ("G", "a constante da gravitação", None)],
                              XE, 330, 130, tl=[C["s05.b"], C["s05.c"], C["s05.d"]], size_l=50)
            A, B = (1150, 520), (1700, 520)
            par(c, t, C["s05.a"] + 0.6, A, B, 120, 60, 110, rot=(None, None))
            E.foco(c, t, C["s05.b"], 0.4, lambda a: (centro(c, "M", A[0], A[1] + 20, 70, "g", BR, a), centro(c, "m", B[0], B[1] + 20, 56, "g", TINTA, a)))
            if t >= C["s05.c"]:
                for P_ in (A, B):
                    c.drawCircle(*P_, 8, M.paint(TINTA, ep(t, C["s05.c"], 0.3)))
            cota(c, t, C["s05.c"] + 0.2, (A[0], A[1] + 200), (B[0], B[1] + 200), "d", lado=1, size=60)
            if t >= C["s05.c"] + 0.2:
                for P_ in (A, B):
                    M.line(c, P_[0], P_[1], P_[0], P_[1] + 220, TINTA2, 0.5 * ep(t, C["s05.c"] + 0.2, 0.4), 3, dash=E.TRACO)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    E.formula_em(c, t, C["s06.a"], "G ≈ 6,7 × 10^{−11}", XE, 330, 120, "g", TINTA)
    E.frase(c, t, C["s06.a"] + 0.8, ps("no Sistema Internacional", "i", 52, TINTA2), XE, 430, passo=0.1)
    E.frase(c, t, C["s06.b"], ps("um número", "i", 76) + [("minúsculo", "g", 76, COR)], XE, 570, passo=0.12)
    for i, x in enumerate((1250, 1550)):
        E.foco(c, t, C["s06.c"] + 0.2 * i, 0.5, lambda a, x=x: F.bloco(c, x, 760, 110, 170, None, a=a, cor=TINTA2))
    E.foco(c, t, C["s06.c"] + 0.6, 0.4, lambda a: centro(c, "força quase zero", 1400, 920, 50, "b", ERRADO, a))
    E.frase(c, t, C["s06.d"], ps("só massa enorme:", "i", 62) + [("planeta", "g", 62, COR)], XE, 760, passo=0.12)


# ---------------- proporção ----------------
def b_proporcao(c, t, C, b):
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07"], ps("leia como", "i", 70) + [("proporção", "g", 70, COR)], XE, 180, passo=0.12)
            E.formula_em(c, t, C["s07"] + 0.4, "F = f{G · M · m}{d^2}", 1250, 230, 90, "g", TINTA)
            linhas(c, t, [(C["s07.b"], "massa × 2  →  F × 2", TINTA), (C["s07.d"], "d × 2  →  F ÷ 2^2", TINTA)], XE, 420, 160, 84)
            E.foco(c, t, C["s07.e"], 0.4, lambda a: E.formula(c, "= F ÷ 4", XE + E.formula(None, "d × 2  →  F ÷ 2^2 ", 0, 0, 84, a=0), 580, 84, "g", COR, a))
            # a distância dobra e as setas encolhem para 1/4
            k = ease_io(prog(t, C["s07.d"], 1.2))
            dist = lerp(380, 760, k)
            comp = 200 / (dist / 380) ** 2
            A = (1050, 870)
            par(c, t, C["s07.c"], A, (A[0] + dist, A[1]), 70, 50, comp, rot=(None, None))
            cota(c, t, C["s07.c"] + 0.3, (A[0], A[1] + 110), (A[0] + dist, A[1] + 110), "d" if k < 0.5 else "2d", lado=1, size=48)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    linhas(c, t, [(C["s08.a"], "d × 3  →", TINTA), (C["s08.c"], "d ÷ 2  →", TINTA)], XE, 260, 170, 84)
    E.formula_em(c, t, C["s08.b"], "F ÷ 9", XE + 470, 260, 84, "g", COR)
    E.formula_em(c, t, C["s08.d"], "F × 4", XE + 470, 430, 84, "g", COR)
    P = F.grafico(c, t, C["s08.e"] - 0.4, 1000, 230, 780, 560, 0, 6, 0, 6, eixo_x="d", eixo_y="F", passo=1, passo_y=1)
    E.curva(c, t, C["s08.e"], P, lambda x: 4 / x ** 2, 0.82, 6, d=1.5)
    E.frase(c, t, C["s08.e"], ps("enfraquece rápido", "i", 62), XE, 700, passo=0.1)
    E.frase(c, t, C["s08.f"], ps("mas", "i", 62) + [("nunca chega a zero", "g", 62, COR)], XE, 820, passo=0.1)


# ---------------- gravidade de um planeta ----------------
def b_gravidade(c, t, C, b):
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09"], ps("de onde vem o", "i", 66) + [("g = 10 m/s²?", "g", 64, COR)], XE, 180, passo=0.12)
            cx, cy, R = 1450, 760, 300
            q = ep(t, C["s09.a"], 0.5)
            if q > 0:
                E.bola(c, cx, cy, R, TERRA, q)
                F.bloco(c, cx, cy - R - 55, 70, 110, None, a=q)
            F.vetor(c, t, C["s09.a"] + 0.3, (cx + 80, cy - R - 110), (cx + 80, cy - R + 20), "P", None, E.COR, 9, lado=-1)
            if t >= C["s09.b"]:
                M.line(c, cx, cy, cx, cy - R, BR, ep(t, C["s09.b"], 0.5), 6)
                c.drawCircle(cx, cy, 9, M.paint(BR, ep(t, C["s09.b"], 0.3)))
            E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.escreve(c, "R", cx + 22, cy - R / 2 + 20, 64, "g", BR, a))
            E.formula_em(c, t, C["s09.c"], "m · g = f{G · M · m}{R^2}", XE, 480, 110, "g", TINTA)
            if t >= C["s09.d"]:
                x0 = XE
                xm2 = XE + E.formula(None, "m · g = f{G · M · ", 0, 0, 110, a=0) - 4
                E.risco(c, x0 - 6, 500, x0 + 80, 410, t, C["s09.d"], cor=E.COR, largura=9)
                E.risco(c, xm2, 440, xm2 + 72, 370, t, C["s09.d"] + 0.25, cor=E.COR, largura=9)
            E.frase(c, t, C["s09.d"] + 0.6, ps("a sua massa", "i", 60) + [("corta", "g", 60, COR)], XE, 700, passo=0.12)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    if t < C["s11"]:
        def s10():
            F.formula_legenda(c, t, C["s10.a"], "g = f{G · M}{R^2}", [("M", "massa do planeta", "kg"), ("R", "raio do planeta", "m")],
                              XE, 340, 140, tl=[C["s10.b"], C["s10.b"] + 0.6], size_l=52)
            E.frase(c, t, C["s10.c"], ps("não depende da", "i", 62) + [("sua massa", "g", 62, COR)], XE, 820, passo=0.12)
            for i, (x, s) in enumerate(((1300, 60), (1550, 140))):
                y = lerp(330, 820, ease_io(prog(t, C["s10.c"] + 0.6, 1.4)) ** 2)
                E.foco(c, t, C["s10.c"], 0.4, lambda a, x=x, s=s, y=y: F.bloco(c, x, y, s, s, None, a=a, cor=TINTA2 if i else None))
            if t >= C["s10.c"]:
                F.chao(c, 1150, 1720, 900, ep(t, C["s10.c"], 0.4))
            E.foco(c, t, C["s10.c"] + 2.0, 0.4, lambda a: centro(c, "chegam juntos (sem ar)", 1430, 990, 46, "i", TINTA2, a))
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.frase(c, t, C["s11.a"], [("massa", "i", 64), ("× 2", "g", 64, COR), ("raio", "i", 64), ("× 2", "g", 64, COR)], XE, 200, passo=0.14)
    q = ep(t, C["s11.a"], 0.6)
    if q > 0:
        E.bola(c, 1250, 620, 110, TERRA, q)
        E.bola(c, 1600, 620, 220, LUA, q)
        centro(c, "Terra", 1250, 790, 44, "i", TINTA2, q)
        centro(c, "2M, 2R", 1600, 900, 48, "b", TINTA, q)
    linhas(c, t, [(C["s11.b"], "massa × 2  →  g × 2", TINTA), (C["s11.c"], "raio × 2  →  g ÷ 4", TINTA), (C["s11.d"], "g × f{2}{4} = f{g}{2}", COR)], XE, 380, 170, 76)
    bola_txt(c, t, C["s11.e"], "5 m/s²", 560, 930, 110, 50)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    if t < C["s12.c"]:
        def s12a():
            E.formula_em(c, t, C["s12.a"], "d × 2  →  F ÷ 2", XE, 420, 100, "g", ERRADO)
            if t >= C["s12.b"]:
                E.risco(c, XE - 10, 440, XE + 760, 350, t, C["s12.b"], largura=12)
            E.formula_em(c, t, C["s12.b"] + 0.8, "d × 2  →  F ÷ 2^2 = F ÷ 4", XE, 640, 100, "g", CERTO)
        E.saida(c, t, C["s12.c"] - 0.1, s12a)
        return
    cx, cy, R = 760, 640, 190
    q = ep(t, C["s12.c"], 0.5)
    if q > 0:
        E.bola(c, cx, cy, R, TERRA, q)
        c.drawCircle(cx, cy, 8, M.paint(BR, q))
    E.frase(c, t, C["s12.c"], ps("de", "i", 66) + [("centro a centro", "g", 66, COR)], XE + 480, 190, passo=0.12)
    sx = cx + 2 * R
    E.foco(c, t, C["s12.d"], 0.5, lambda a: F.bloco(c, sx + 20, cy, 50, 50, None, a=a))
    cota(c, t, C["s12.d"] + 0.3, (cx + R, cy - 230), (sx, cy - 230), "6.400 km de altura", lado=-1, size=40)
    cota(c, t, C["s12.e"], (cx, cy + 260), (sx, cy + 260), "12.800 km = 2R", lado=1, size=48)
    E.frase(c, t, C["s12.f"], ps("distância × 2", "i", 58) + [("→", "g", 56, TINTA2), ("peso ÷ 4", "g", 58, COR)], 1120, 1010, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.frase(c, t, C["s13.a"], ps("não substitua números:", "i", 70, CLARO) + [("monte o fator", "g", 70, BR)], W / 2, 320, "center", 0.12)
            E.formula_em(c, t, C["s13.b"], "F × f{fator da massa}{(fator da distância)^2}", W / 2, 540, 92, "g", BR, "center")
            E.formula_em(c, t, C["s13.e"], "massa × 3,  d × 2  →  F × f{3}{2^2} =", W / 2 - 110, 820, 84, "g", CLARO, "center")
            bola_txt(c, t, C["s13.f"], "¾ F", W / 2 + 640, 790, 95, 60)
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], [("G", "g", 76, BR)] + ps("e o que não mudou", "i", 76, CLARO) + [("cortam", "g", 76, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s14.b"], ps("G só é preciso", "i", 66, CLARO) + ps("sem caso conhecido para comparar", "g", 60, BR), W / 2, 620, "center", 0.1)
    E.frase(c, t, C["s14.b"] + 3.0, ps("aí: notação científica", "i", 62, CLARO), W / 2, 780, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s15")
    E.frase(c, t, C["s15.a"], [("Marte:", "g", 66, MARTE), ("massa", "i", 66), ("≈ 1/10", "g", 66)], XE, 330, passo=0.12)
    E.frase(c, t, C["s15.b"], [("raio", "i", 66), ("≈ 1/2", "g", 66)], XE + 238, 440, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("g em Marte?", "i", 72), XE, 620, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("peso de", "i", 72) + [("70 kg", "g", 72, COR)] + ps("lá?", "i", 72), XE, 760, passo=0.12)
    if t < C["s16"]:
        q = ep(t, C["s15.a"], 0.6)
        if q > 0:
            E.bola(c, 1300, 600, 200, TERRA, q)
            E.bola(c, 1680, 640, 100, MARTE, q)
            centro(c, "Terra", 1300, 880, 46, "i", TINTA2, q)
            centro(c, "Marte", 1680, 820, 46, "i", TINTA2, q)
    else:
        E.relogio(c, t, C["s16.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s18"]:
        def s17():
            linhas(c, t, [(C["s17.a"], "massa ÷ 10  →  g ÷ 10", TINTA), (C["s17.b"], "raio × f{1}{2}  →  (f{1}{2})^2 = f{1}{4} embaixo", TINTA),
                          (C["s17.c"], "÷ f{1}{4}  =  × 4", COR), (C["s17.d"], "10 ÷ 10 × 4", TINTA)], XE, 250, 180, 76)
            bola_txt(c, t, C["s17.e"], "4 m/s²", 1450, 850, 130, 56, CERTO)
            pilula_em(c, t, lerp(C["s17.e"], C["s17.end"], 0.4), "medido: 3,7 m/s²", 1450, 1020, 44, TINTA)
        E.saida(c, t, C["s18"] - 0.1, s17)
        return
    E.formula_em(c, t, C["s18.a"], "P = 70 · 4", XE, 330, 110, "g", TINTA)
    bola_txt(c, t, C["s18.b"], "280 N", XE + 820, 300, 120, 60, CERTO)
    E.frase(c, t, C["s18.b"] + 1.0, ps("na Terra:", "i", 64) + [("700 N", "g", 64)], XE, 500, passo=0.12)
    E.frase(c, t, C["s18.c"], [("massa:", "i", 72), ("70 kg", "g", 72, COR)] + ps("nos dois", "i", 72), XE, 720, passo=0.12)
    E.frase(c, t, C["s18.d"], ps("o que muda é o", "i", 72) + [("peso", "g", 76, COR)], XE, 880, passo=0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s20"]:
        E.saida(c, t, C["s20"] - 0.1, lambda: resumo(c, t, C, "s19", (
            ("s19.a", [("F = G · M · m / d²", "g", 64, COR)]),
            ("s19.b", [("distância × 2", "i", 70), ("→", "g", 64, TINTA2), ("força ÷ 4", "g", 64, COR)]),
            ("s19.c", [("g", "g", 66, COR), ("depende da massa e do", "i", 70), ("raio²", "g", 66)]))))
        return

    def desenho():
        q = ep(t, C["s20.a"], 0.6)
        if q <= 0:
            return
        cx, cy = 760, 820
        E.bola(c, cx, cy, 110 * q, TERRA, q)
        pt = M.paint(TINTA, 0.6 * q, stroke=4); pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawCircle(cx, cy, 190, pt)
        g = t * 0.9
        F.bloco(c, cx + 190 * math.cos(g), cy - 190 * math.sin(g), 36, 36, None, a=q)
        E.foco(c, t, C["s20.b"], 0.5, lambda a: E.bola(c, cx + 480, cy - 40, 50, LUA, a))
    proxima(c, t, C, "s20", [("Satélites", "g", 120, COR), ("e", "i", 110), ("marés", "g", 120, COR)], None, desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, proporcao=b_proporcao, gravidade=b_gravidade, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
