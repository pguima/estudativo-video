"""Visual — Estudativo · MAT-ANG-003: retas paralelas cortadas por uma transversal.
Linguagem da geometria plana (MAT-ANG-001/002): lados em tinta; ângulos iguais com a mesma cor — os AGUDOS em COR (índigo),
os OBTUSOS em TINTA2 (cinza escuro); medidas na grotesca; resposta na esfera. "Um cruzamento é cópia do outro": as quatro cunhas
do cruzamento de cima descem pela transversal com voa() e assentam no de baixo.
Peças locais: paral() desenha r, s e a transversal com os oito ângulos (1 a 4 em cima, 5 a 8 embaixo, na ordem do kit:
acima à direita, acima à esquerda, abaixo à esquerda, abaixo à direita), na versão clara ou no palco escuro, com inclinação que
pode variar; destaque() acende um ângulo. Todo instante vem de C[...]."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Ângulos e Triângulos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANG-003_paralelas_e_transversal.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("retas", "transversal", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 2 * 30 + 10 == 70 and (70 - 10) // 2 == 30
assert 2 * 50 + 10 == 110 and 2 * 30 + 10 + 110 == 180
assert 3 * 30 - 20 == 30 + 40 == 70 and 180 - 70 == 110


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     centro(c, s, cx, cy + size * 0.36, size, "g", BR, a)))


def operacao(c, t, t0, op, x, y, escuro=False):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, op, x, y - 30, 54, "g", a=a, cor=E.SOBRE))
    E.frase(c, t, t0 + 0.3, ps("nos dois lados", "i", 40, CLARO if escuro else TINTA2), x, y + 48, "center", 0.06)


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def rotulo(c, V, g, r, s, cor, size, a):
    if a <= 0 or not s:
        return
    w = E.formula(None, s, 0, 0, size, "b", a=0)
    ux, uy = math.cos(math.radians(g)), -math.sin(math.radians(g))
    k = r + 16 + abs(ux) * w / 2 + abs(uy) * size * 0.4
    E.formula(c, s, V[0] + ux * k, V[1] + uy * k + size * 0.36, size, "b", cor, a, "center")


def cunha_m(c, V, g1, g2, r, cor, a=1.0, alfa=0.3, borda=6):
    if a <= 0:
        return
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    path = skia.Path()
    path.moveTo(*V); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        p = M.paint(cor, a, stroke=borda, cap_round=True)
        p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


def voa(c, t, t0, d, V0, g1, g2, r, cor=None, V1=None, giro=0.0, fica=0.8):
    """o ângulo se move (ver MAT-ANG-002): a cunha sai de V0, gira e viaja até V1, deixando o contorno tracejado na origem"""
    if t < t0 or t > t0 + d + fica + 0.4:
        return
    cor = cor or E.COR
    V1 = V1 or V0
    p = ease_io(prog(t, t0, d))
    a = 1 - ep(t, t0 + d + fica, 0.4)
    ret = skia.Rect.MakeXYWH(V0[0] - r, V0[1] - r, 2 * r, 2 * r)
    tr = M.paint(cor, 0.8 * a, stroke=3)
    tr.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
    path = skia.Path(); path.moveTo(*V0); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    c.drawPath(path, tr)
    lift = 1 + 0.08 * math.sin(math.pi * p)
    c.save()
    c.translate(lerp(V0[0], V1[0], p), lerp(V0[1], V1[1], p))
    c.rotate(-giro * p)
    c.scale(lift, lift)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a * math.sin(math.pi * p)))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 10))
    path2 = skia.Path(); path2.moveTo(0, 0); path2.arcTo(skia.Rect.MakeXYWH(-r, -r, 2 * r, 2 * r), -g1, -(g2 - g1), False); path2.close()
    c.save(); c.translate(6, 12); c.drawPath(path2, s); c.restore()
    cunha_m(c, (0, 0), g1, g2, r, cor, a, alfa=0.55)
    c.restore()


def faixa(inc, k):
    """de que grau a que grau vai o ângulo k (1 a 8)"""
    j = (k - 1) % 4
    return ((0, inc), (inc, 180), (180, 180 + inc), (180 + inc, 360))[j]


def agudo(inc, k):
    return (k % 2 == 1) == (inc < 90)


class Fig:
    """posição da figura das paralelas"""

    def __init__(s, cx, cy, w=900, gap=330, inc=60, rt=None):
        s.cx, s.cy, s.w, s.gap, s.inc = cx, cy, w, gap, inc
        s.y1, s.y2 = cy - gap / 2, cy + gap / 2
        k = 1 / math.tan(math.radians(inc))
        s.P1, s.P2 = (cx + gap / 2 * k, s.y1), (cx - gap / 2 * k, s.y2)
        s.r_ag, s.r_ob = (rt or (90, 66))

    def V(s, k):
        return s.P1 if k <= 4 else s.P2

    def r(s, k):
        return s.r_ag if agudo(s.inc, k) else s.r_ob


def paral(c, t, t0, F, ang=None, escuro=False, nomes=True, d=0.7, tt=None):
    """r e s (com as setinhas de paralela) e a transversal t. ang = {k: (rótulo ou None, instante)}; tt = instante da transversal"""
    tinta = BR if escuro else TINTA
    tt = t0 + 0.4 if tt is None else tt
    if t >= t0:
        for i, yy in enumerate((F.y1, F.y2)):
            M.line(c, F.cx - F.w / 2, yy, F.cx + F.w / 2, yy, tinta, 1.0, 6, progress=ease_io(prog(t, t0 + 0.15 * i, d)))
            q = ep(t, t0 + d, 0.4)
            xm = F.cx + F.w * 0.4
            M.line(c, xm - 14, yy - 16, xm + 6, yy, tinta, q, 5)
            M.line(c, xm - 14, yy + 16, xm + 6, yy, tinta, q, 5)
        if nomes:
            E.foco(c, t, t0 + d * 0.8, 0.4, lambda a: (E.escreve(c, "r", F.cx + F.w / 2 + 20, F.y1 + 20, 64, "i", tinta, a),
                                                       E.escreve(c, "s", F.cx + F.w / 2 + 20, F.y2 + 20, 64, "i", tinta, a)))
    if t >= tt:
        ext = F.gap / 2 / math.sin(math.radians(F.inc)) + 150
        M.line(c, *pt((F.cx, F.cy), ext, F.inc + 180), *pt((F.cx, F.cy), ext, F.inc), CLARO if escuro else TINTA2, 1.0, 6,
               progress=ease_io(prog(t, tt, d)))
        if nomes:
            E.foco(c, t, tt + d, 0.4, lambda a: E.escreve(c, "t", pt((F.cx, F.cy), ext, F.inc)[0] + 16, pt((F.cx, F.cy), ext, F.inc)[1] + 20, 64, "i", CLARO if escuro else TINTA2, a))
        for P in (F.P1, F.P2):
            c.drawCircle(*P, 9 * ease_back(prog(t, tt + d * 0.8, 0.4)), M.paint(tinta))
    for k, (rot, ta) in sorted((ang or {}).items()):
        if t < ta:
            continue
        g1, g2 = faixa(F.inc, k)
        V = F.V(k)
        ag = agudo(F.inc, k)
        cor = (CLARO if ag else BR) if escuro else (E.COR if ag else TINTA2)
        E.angulo(c, t, ta, V, pt(V, 10, g1), pt(V, 10, g2), None, r=F.r(k), cor=cor, reto=abs(F.inc - 90) < 0.6)
        if rot:
            cr = (CLARO if ag else BR) if escuro else (COR if ag else TINTA2)
            E.foco(c, t, ta + 0.3, 0.4, lambda a, V=V, g=(g1 + g2) / 2, r=F.r(k), rot=rot, cr=cr: rotulo(c, V, g, r, rot, cr, 52, a))


def destaque(c, t, t0, F, k, t1=None, cor=None):
    """acende o ângulo k (cunha forte que pulsa ao entrar); some em t1"""
    if t < t0 or (t1 is not None and t > t1 + 0.4):
        return
    a = ep(t, t0, 0.4) * (1 - (ep(t, t1, 0.4) if t1 is not None else 0))
    g1, g2 = faixa(F.inc, k)
    pulsa = 1 + 0.12 * math.sin(math.pi * M.clamp(prog(t, t0, 0.6)))
    cunha_m(c, F.V(k), g1, g2, F.r(k) * pulsa, cor or (E.COR if agudo(F.inc, k) else TINTA2), a, alfa=0.6, borda=8)


TODOS = {k: (None, 0) for k in range(1, 9)}


def todos(t0, passo=0.12, rot=None):
    return {k: ((rot or {}).get(k), t0 + passo * (k - 1)) for k in range(1, 9)}


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    F = Fig(820, 540, 1000, 360, 60)

    def um():
        paral(c, t, ka, F, {k: (None, kb + 0.15 * (k - 1)) for k in range(1, 9)})
        for k in range(1, 9):
            g1, g2 = faixa(60, k)
            V = F.V(k)
            num = ep(t, kb + 0.15 * (k - 1) + 0.3, 0.4) * (1 - ep(t, kc, 0.4))
            rotulo(c, V, (g1 + g2) / 2, F.r(k), str(k), TINTA2, 50, num)
            med = ep(t, kc + 0.4 + (0 if agudo(60, k) else 0.6), 0.4)
            rotulo(c, V, (g1 + g2) / 2, F.r(k), "a" if agudo(60, k) else "b", COR if agudo(60, k) else TINTA2, 56, med)
        E.frase(c, t, kb, [("8", "g", 110, COR)] + ps("ângulos", "i", 90), 1500, 220, "center", 0.12)
        E.frase(c, t, kc, ps("só", "i", 90) + [("2", "g", 110, COR)] + ps("medidas", "i", 90), 1500, 960, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1500, 560, 250 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), [("reconhecer", "g", 96, COR)], XE, 440, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.55), ps("paralelas e concorrentes", "i", 72), XE, 550, passo=0.12)
        E.frase(c, t, tb, [("achar", "g", 96)] + ps("os 8 ângulos", "i", 84), XE, 720, passo=0.14)
        E.foco(c, t, tc + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1500, 535, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1500, 620, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 960, 820
    itens = (("s03.b", "opostos pelo vértice", "são iguais"), ("s03.c", "lado a lado", "somam 180°"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 280
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 60)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 60, COR)], x + 44, y + 160)
    py = lerp(420, 700, ease_io(prog(t, C["s03.c"] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, C["s03.end"] - 2.4, ps("faltou alguma?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 920, "left", 0.12)


# ---------------- posições de duas retas ----------------
def b_retas(c, t, C, b):
    a4, b4, a5, b5, a6, b6, c6 = C["s04.a"], C["s04.b"], C["s05.a"], C["s05.b"], C["s06.a"], C["s06.b"], C["s06.c"]
    E.frase(c, t, C["s04"], ps("duas retas no papel", "i", 76), W / 2, 160, "center", 0.12)
    cy = 520
    # concorrentes
    V = (330, cy)
    for i, g in enumerate((20, 115)):
        if t >= a4 + 0.25 * i:
            q = ease_io(prog(t, a4 + 0.25 * i, 0.6))
            M.line(c, *pt(V, 230 * q, g + 180), *pt(V, 230 * q, g), TINTA, 1.0, 6)
    E.foco(c, t, a4 + 0.4, 0.3, lambda a: c.drawCircle(*V, 11, M.paint(COR, a)))
    E.frase(c, t, a4 + 0.5, [("concorrentes", "g", 62, COR)], 330, 800, "center")
    E.frase(c, t, b4, ps("uma esquina", "i", 50, TINTA2), 330, 870, "center", 0.1)
    # perpendiculares
    V = (960, cy)
    for i, g in enumerate((0, 90)):
        if t >= a5 + 0.25 * i:
            q = ease_io(prog(t, a5 + 0.25 * i, 0.6))
            M.line(c, *pt(V, 220 * q, g + 180), *pt(V, 220 * q, g), TINTA, 1.0, 6)
    if t >= b5:
        E.angulo(c, t, b5, V, pt(V, 10, 0), pt(V, 10, 90), r=80)
    E.frase(c, t, a5 + 0.5, [("perpendiculares", "g", 62, COR)], 960, 800, "center")
    E.frase(c, t, b5, ps("cruz com 4 retos", "i", 50, TINTA2), 960, 870, "center", 0.1)
    # paralelas
    x0, x1 = 1380, 1820
    for i, yy in enumerate((cy - 90, cy + 90)):
        if t >= a6 + 0.25 * i:
            M.line(c, x0, yy, x1, yy, TINTA, 1.0, 6, progress=ease_io(prog(t, a6 + 0.25 * i, 0.7)))
    tril = ep(t, b6, 0.5) * (1 - ep(t, c6, 0.4))
    for i in range(7):
        xx = x0 + 30 + i * 64
        M.line(c, xx, cy - 90, xx, cy + 90, TINTA2, tril, 10)
    cad = ep(t, c6, 0.5)
    for yy in (cy - 270, cy - 180, cy, cy + 180):
        M.line(c, x0, yy, x1, yy, "#7FA7D9", cad * 0.8, 3)
    if t >= a6 + 1.0:
        q = ep(t, a6 + 1.0, 0.5)
        for xx in (x0 + 110, x1 - 110):
            M.arrow(c, xx, cy - 80, xx, cy + 80, COR, q, 4, 14, q)
            M.arrow(c, xx, cy + 80, xx, cy - 80, COR, q, 4, 14, q)
    E.frase(c, t, a6 + 0.5, [("paralelas", "g", 62, COR)], 1600, 800, "center")
    E.frase(c, t, a6 + 1.2, ps("nunca se cruzam", "i", 50, TINTA2), 1600, 870, "center", 0.1)
    E.frase(c, t, b6, ps("trilhos", "i", 50, TINTA2), 1600, 940, "center") if t < c6 else None
    E.frase(c, t, c6, ps("linhas do caderno", "i", 50, TINTA2), 1600, 940, "center", 0.1)


# ---------------- a transversal ----------------
def b_transversal(c, t, C, b):
    F = Fig(640, 560, 940, 360, 60)
    X = 1510
    a7, b7, c7, a8, b8 = C["s07.a"], C["s07.b"], C["s07.c"], C["s08.a"], C["s08.b"]
    ang = {k: (None, c7 + 0.15 * (k - 1)) for k in range(1, 5)}
    ang.update({k: (None, b8 + 1.6) for k in range(5, 9)})
    paral(c, t, C["s07"] + 0.2, F, ang, tt=a7)
    # a mesma inclinação: as duas paralelas com a transversal, em destaque
    if t >= a8:
        for V in (F.P1, F.P2):
            E.arco(c, V[0], V[1], 150, -F.inc, F.inc * ease_io(prog(t, a8, 0.5)), CERTO, 5, 1 - ep(t, b8, 0.4))
    # a cópia: as quatro cunhas de cima descem até o cruzamento de baixo
    for k in range(1, 5):
        g1, g2 = faixa(F.inc, k)
        voa(c, t, b8 + 0.1, 1.4, F.P1, g1, g2, F.r(k), E.COR if agudo(F.inc, k) else TINTA2, V1=F.P2, fica=0.3)
    E.foco(c, t, b7, 0.5, lambda a: E.pilula(c, "transversal", X, 300, 64, "g", fundo=TINTA2, a=a))

    def tesoura():
        E.frase(c, t, c7, ps("de frente:", "i", 66) + [("iguais", "g", 70, COR)], X, 480, "center", 0.12)
        E.frase(c, t, c7 + 1.2, ps("lado a lado:", "i", 66) + [("180°", "g", 70, TINTA2)], X, 590, "center", 0.12)
    E.saida(c, t, C["s08"] - 0.1, tesoura)
    if t >= C["s08"]:
        E.frase(c, t, a8, ps("mesma", "i", 76) + [("inclinação", "g", 76, CERTO)], X, 500, "center", 0.12)
        E.frase(c, t, b8, ps("o de baixo é", "i", 72), X, 700, "center", 0.12)
        E.frase(c, t, b8 + 0.6, [("cópia", "g", 110, COR)], X, 830, "center")
        E.frase(c, t, b8 + 1.0, ps("do de cima", "i", 72), X, 930, "center", 0.12)


# ---------------- correspondentes e alternos ----------------
def b_nomes(c, t, C, b):
    F = Fig(640, 560, 940, 360, 60)
    X = 1510
    a9, b9, c9, d9 = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
    a10, b10, c10, d10 = C["s10.a"], C["s10.b"], C["s10.c"], C["s10.d"]
    # a faixa entre as paralelas
    fx = ep(t, a10, 0.6)
    if fx > 0:
        c.drawRect(skia.Rect.MakeXYWH(F.cx - F.w / 2, F.y1, F.w * fx, F.gap), M.paint(E.COR, 0.07))
    paral(c, t, C["s09"] - 1, F, todos(C["s09"] - 1, 0))
    destaque(c, t, b9, F, 1, C["s10"])
    destaque(c, t, c9, F, 5, C["s10"])
    destaque(c, t, b10 - 1.2, F, 3)
    destaque(c, t, b10, F, 5)
    # o zê dos alternos
    if t >= d10:
        z = [(F.P1[0] - 300, F.y1), F.P1, F.P2, (F.P2[0] + 300, F.y2)]
        p = ease_io(prog(t, d10, 0.9))
        path = skia.Path(); path.moveTo(*z[0])
        L = [math.dist(z[i], z[i + 1]) for i in range(3)]
        alvo = sum(L) * p
        for i in range(3):
            if alvo >= L[i]:
                path.lineTo(*z[i + 1]); alvo -= L[i]
            else:
                f = alvo / L[i]
                path.lineTo(lerp(z[i][0], z[i + 1][0], f), lerp(z[i][1], z[i + 1][1], f)); break
        pz = M.paint(CERTO, 0.9, stroke=14, cap_round=True)
        pz.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, pz)

    def corr():
        E.frase(c, t, a9, ps("mesma posição", "i", 72), X, 300, "center", 0.12)
        E.frase(c, t, a9 + 0.8, [("correspondentes", "g", 70, COR)], X, 410, "center")
        E.frase(c, t, b9, ps("cima à direita", "i", 56, TINTA2), X, 540, "center", 0.1)
        E.frase(c, t, c9, ps("e cima à direita", "i", 56, TINTA2), X, 620, "center", 0.1)
        E.frase(c, t, d9, [("iguais", "g", 110, COR)], X, 820, "center")
    E.saida(c, t, C["s10"] - 0.1, corr)
    if t >= C["s10"]:
        E.frase(c, t, a10, ps("entre as paralelas:", "i", 66), X, 300, "center", 0.12)
        E.frase(c, t, b10, ps("lados opostos de t", "i", 56, TINTA2), X, 420, "center", 0.1)
        E.frase(c, t, c10, [("alternos internos", "g", 70, COR)], X, 560, "center")
        E.frase(c, t, d10, ps("desenham um", "i", 66) + [("Z", "g", 90, CERTO)], X, 700, "center", 0.12)
        E.frase(c, t, d10 + 0.8, [("iguais", "g", 110, COR)], X, 860, "center")


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    F = Fig(560, 560, 820, 360, 60)
    X, PX = 1350, 1760
    a11, b11, c11 = C["s11.a"], C["s11.b"], C["s11.c"]
    a12, b12, c12, d12 = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
    paral(c, t, C["s11"], F, {1: ("2x + 10", a11), 5: ("70°", b11)}, nomes=False)
    destaque(c, t, d12, F, 3)
    E.foco(c, t, d12 + 0.3, 0.4, lambda a: rotulo(c, F.P1, 210, F.r(3), "alterno", COR, 46, a))
    E.frase(c, t, a11, [("correspondentes", "g", 64, COR)] + ps("são iguais", "i", 64), X, 200, "center", 0.12)
    fcen(c, t, c11, "2x + 10 = 70", X, 360, 96)
    operacao(c, t, a12, "− 10", PX, 440)
    fcen(c, t, a12 + 0.4, "2x = 60", X, 500, 96)
    operacao(c, t, b12, "÷ 2", PX, 580)
    E.foco(c, t, b12 + 0.4, 0.5, lambda a: E.pilula(c, "x = 30", X, 610, 90, "g", a=a, cor=E.SOBRE))
    fcen(c, t, c12, "2 · 30 + 10 = 70", X, 800, 84, TINTA2)
    E.foco(c, t, c12 + 1.0, 0.4, lambda a: E.selo(c, X + 400, 772, 44, True, a))
    E.frase(c, t, d12, ps("alternos internos:", "i", 56) + [("mesma conta", "g", 56, COR)], X, 950, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    F = Fig(540, 680, 820, 360, 60)
    X = 1350
    a13, b13, a14, b14, c14, a15, b15, c15 = (C["s13.a"], C["s13.b"], C["s14.a"], C["s14.b"], C["s14.c"],
                                              C["s15.a"], C["s15.b"], C["s15.c"])
    E.frase(c, t, C["s13"], [("cuidado", "g", 90, ERRADO)] + ps("com este erro", "i", 84), W / 2, 150, "center", 0.12)
    paral(c, t, C["s13"] + 0.3, F, {1: ("2x + 10", a13 + 1.5), 6: ("110°", b13)}, nomes=False)
    E.foco(c, t, a13 + 2.2, 0.4, lambda a: rotulo(c, F.P1, 30, 210, "agudo", COR, 44, a))
    E.foco(c, t, b13 + 0.6, 0.4, lambda a: rotulo(c, F.P2, 120, 190, "obtuso", TINTA2, 44, a))
    E.frase(c, t, a13, ps("igualar", "i", 64) + [("agudo", "g", 64, COR)] + ps("com", "i", 64) + [("obtuso", "g", 64, TINTA2)], X, 290, "center", 0.12)
    fcen(c, t, a14, "2x + 10 = 110", X, 420, 80, ERRADO)
    fcen(c, t, b14, "x = 50", X, 530, 80, ERRADO)
    fcen(c, t, c14, "2 · 50 + 10 = 110", X, 640, 72, ERRADO)
    E.foco(c, t, c14 + 1.2, 0.4, lambda a: E.pilula(c, "obtuso!", X + 380, 610, 44, "g", fundo=ERRADO, a=a))
    if t >= a15:
        E.risco(c, X - 330, 660, X + 330, 380, t, a15, largura=12)
    E.frase(c, t, a15, [("agudo + obtuso = 180°", "g", 60, CERTO)], X, 780, "center")
    fcen(c, t, b15, "2x + 10 + 110 = 180", X, 880, 66)
    E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "x = 30  →  agudo = 70°", X, 980, 56, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a16, b16, c16, d16, e16 = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
    a17, b17, c17 = C["s17.a"], C["s17.b"], C["s17.c"]
    inc = 60 + 30 * ease_io(prog(t, c17 + 0.3, 1.2))
    F = Fig(600, 560, 860, 340, inc)
    ang = {k: (None, b16 + 0.1 * (k // 2)) for k in (1, 3, 5, 7)}
    ang.update({k: (None, c16 + 0.1 * (k // 2)) for k in (2, 4, 6, 8)})
    paral(c, t, C["s16"], F, ang, escuro=True)
    X = 1430

    def regras():
        E.frase(c, t, a16, ps("esqueça os nomes", "i", 66, CLARO), X, 200, "center", 0.12)
        E.frase(c, t, b16, [("agudos:", "g", 64, CLARO)] + ps("todos iguais", "i", 64, BR), X, 340, "center", 0.12)
        E.frase(c, t, c16, [("obtusos:", "g", 64, BR)] + ps("todos iguais", "i", 64, BR), X, 450, "center", 0.12)
        E.frase(c, t, d16, ps("agudo com agudo", "i", 60, CLARO), X, 610, "center", 0.1)
        E.foco(c, t, d16 + 0.6, 0.5, lambda a: E.pilula(c, "iguala", X, 680, 60, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, e16, ps("agudo com obtuso", "i", 60, CLARO), X, 820, "center", 0.1)
        E.foco(c, t, e16 + 0.6, 0.5, lambda a: E.pilula(c, "soma 180°", X, 890, 60, "g", fundo="#FFFFFF", cor="#07070F", a=a))
    E.saida(c, t, C["s17"] - 0.1, regras)
    if t >= C["s17"]:
        E.frase(c, t, a17, [("2 medidas", "g", 76, BR)] + ps("por cruzamento", "i", 66, CLARO), X, 280, "center", 0.12)
        E.frase(c, t, b17, ps("só vale com", "i", 66, CLARO) + [("paralelas", "g", 70, ERRADO)], X, 480, "center", 0.12)
        E.frase(c, t, c17, ps("transversal perpendicular:", "i", 60, CLARO), X, 680, "center", 0.1)
        E.frase(c, t, c17 + 1.0, [("todos 90°", "g", 90, BR)], X, 800, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    F = Fig(1380, 600, 760, 330, 60, rt=(80, 60))
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, C["s18"] + 1.5, ps("paralelas e transversal", "i", 70), XE, 330, passo=0.12)
    E.frase(c, t, C["s18.a"] - 1.4, [("alternos internos:", "g", 64, COR)], XE, 470)
    fcen(c, t, C["s18.a"], "3x − 20", XE + 170, 600, 88, COR)
    E.frase(c, t, C["s18.b"], ps("e", "i", 76), XE + 375, 600)
    fcen(c, t, C["s18.b"] + 0.3, "x + 40", XE + 560, 600, 88, COR)
    E.frase(c, t, C["s18.c"], ps("quanto vale", "i", 84) + [("x?", "g", 90, COR)], XE, 770, passo=0.14)
    E.frase(c, t, C["s18.c"] + 1.2, ps("e cada ângulo?", "i", 84), XE, 890, passo=0.14)
    E.saida(c, t, C["s19.a"] - 0.1, lambda: paral(c, t, C["s18"] + 1.5, F, {3: ("3x − 20", C["s18.a"]), 5: ("x + 40", C["s18.b"])}, nomes=False))
    E.relogio(c, t, C["s19.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    F = Fig(500, 600, 760, 330, 60, rt=(80, 60))
    X, PX = 1290, 1740
    a20, b20, c20, d20 = C["s20.a"], C["s20.b"], C["s20.c"], C["s20.d"]
    a21, b21, c21 = C["s21.a"], C["s21.b"], C["s21.c"]
    novo = ep(t, a21, 0.4)
    paral(c, t, C["s20"], F, {3: (None, C["s20"] + 0.3), 5: (None, C["s20"] + 0.3)}, nomes=False)
    for k, s in ((3, "3x − 20"), (5, "x + 40")):
        g1, g2 = faixa(60, k)
        E.foco(c, t, C["s20"] + 0.6, 0.4, lambda a, k=k, s=s, g=(g1 + g2) / 2: rotulo(c, F.V(k), g, F.r(k), s, COR, 48, a * (1 - novo)))
        E.foco(c, t, a21 + (0 if k == 3 else b21 - a21), 0.4, lambda a, k=k, g=(g1 + g2) / 2: rotulo(c, F.V(k), g, F.r(k), "70°", COR, 54, a))
    if t >= c21:
        for k in (2, 4, 6, 8):
            g1, g2 = faixa(60, k)
            E.angulo(c, t, c21 + 0.1 * k, F.V(k), pt(F.V(k), 10, g1), pt(F.V(k), 10, g2), r=F.r(k), cor=TINTA2)
            E.foco(c, t, c21 + 0.1 * k + 0.3, 0.4, lambda a, k=k, g=(g1 + g2) / 2: rotulo(c, F.V(k), g, F.r(k), "110°", TINTA2, 44, a))

    def contas():
        E.frase(c, t, C["s20"] + 0.5, [("alternos internos", "g", 60, COR)] + ps("são iguais", "i", 60), X, 200, "center", 0.12)
        fcen(c, t, a20, "3x − 20 = x + 40", X, 340, 84)
        operacao(c, t, b20, "− x", PX, 420)
        fcen(c, t, b20 + 0.4, "2x − 20 = 40", X, 480, 84)
        operacao(c, t, c20, "+ 20", PX, 560)
        fcen(c, t, c20 + 0.4, "2x = 60", X, 620, 84)
        E.foco(c, t, d20, 0.5, lambda a: E.pilula(c, "x = 30", X, 760, 90, "g", a=a, cor=E.SOBRE))
    E.saida(c, t, C["s21"] - 0.1, contas)
    if t >= C["s21"]:
        fcen(c, t, a21, "3 · 30 − 20 = 70°", X, 260, 84, COR)
        fcen(c, t, b21, "30 + 40 = 70°", X, 400, 84, COR)
        E.foco(c, t, b21 + 0.8, 0.4, lambda a: E.selo(c, X + 330, 372, 44, True, a))
        E.frase(c, t, c21, ps("os obtusos:", "i", 70, TINTA2), X, 600, "center", 0.12)
        fcen(c, t, c21 + 0.8, "180 − 70 = 110°", X, 740, 90, TINTA2)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", "paralelas nunca se cruzam"), ("s22.b", "o mesmo cruzamento, duas vezes"),
                 ("s22.c", "agudo e agudo: iguais"))
        for i, (k, s) in enumerate(itens):
            y = 380 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 360, y - 30, 56, a=a), centro(c, str(i + 1), 360, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76)], 460, y)
        E.frase(c, t, C["s22.c"] + 1.8, [("agudo e obtuso: somam 180°", "g", 76)], 460, 880)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23.a"] - 1.0, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s23.a"], [("Ângulos do", "g", 140, COR)], XE, 450)
    E.frase(c, t, C["s23.a"] + 0.3, [("triângulo", "g", 140, COR)], XE, 590)
    E.frase(c, t, C["s23.b"], ps("e o", "i", 76) + [("ângulo externo", "g", 76)], XE, 720, passo=0.12)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, retas=b_retas, transversal=b_transversal, nomes=b_nomes, exemplo=b_exemplo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
