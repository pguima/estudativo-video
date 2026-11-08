"""Visual — Estudativo · MAT-FUN-009: função afim, lei e gráfico.

Linguagem visual da trilha Funções (MAT-FUN-001 a 008): entrada / x (d, horas) em índigo (ENT), saída / y (P, preço, f(x)) em preto (SAI);
eixo x índigo, eixo y preto; par (x, y) com o x índigo e o y preto; plano na metade direita e texto à esquerda.
Nesta aula: a lei f(x) = ax + b com o x em índigo; o "a" (o que multiplica o x) e o "b" (o número sozinho) ganham caixas pontilhadas
(caixa_em(), a da MAT-FUN-003). Táxi: o taxímetro escuro da MAT-FUN-002 e a tabela de duas colunas com arcos "+2,50" entre as linhas.
Retas: E.reta_pontos (a reta de borda a borda), E.ponto para os pontos calculados; o ponto de conferência acende com anel verde.
Palco escuro só no atalho.
Peças locais: mista(), caixa_em(), tabela2(), salto_tab(), taximetro(), eixos(), par(), anel(), marca_eixo(), regua_desenho(), resultado()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-009_funcao_afim_lei_e_grafico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("taxi", "afim", "grafico", "atalho", "questao", "fim"))
BR = "#FFFFFF"

taxi = lambda d: 5 + 2.5 * d
f = lambda x: 2 * x - 1
enc = lambda x: 30 * x + 40
assert [taxi(d) for d in (0, 1, 2, 3, 6)] == [5, 7.5, 10, 12.5, 20] and 2.5 * 6 == 15
assert (f(0), f(2), f(1)) == (-1, 3, 1) and 5 * 6 + 2.5 == 32.5
assert enc(3) == 130 and 30 * 3 == 90 and (enc(0), enc(1)) == (40, 70)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fml(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


def mista(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """texto numa linha com uma cor por parte (MAT-FUN-003); devolve (centro x, largura) de cada parte"""
    ws = [E.larg(s, est, size) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x
    cs = []
    for (s, cor), w in zip(partes, ws):
        E.escreve(c, s, xx, y, size, est, cor, a)
        cs.append((xx + w / 2, w))
        xx += w
    return cs


def mista_em(c, t, t0, partes, x, y, size, align="left", est="g"):
    E.foco(c, t, t0, 0.5, lambda a: mista(c, partes, x, y, size, a, align, est))
    return mista(c, partes, x, y, size, 0, align, est)


def caixa_em(c, t, t0, cx, w, y, size, cor=None, d=0.5):
    """caixa pontilhada em volta de um trecho já escrito (MAT-FUN-003)"""
    p = ep(t, t0, d)
    if p > 0:
        E.caixa_pontilhada(c, cx - w / 2 - 16, y - size * 0.86, w + 32, size * 1.12, p, cor, p)


def par(c, xv, yv, x, y, size, a=1.0, align="left", est="g", cores=None, tinta=TINTA):
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", tinta), (xv, cx_), (", ", tinta), (yv, cy_), (")", tinta))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def tabela2(c, t, t0, linhas, x, y, cab=("d (km)", "P (R$)"), wc=230, hl=96, size=64, tl=None):
    """tabela de duas colunas, entrada (índigo) | saída (preto) (MAT-FUN-002)"""
    a = ep(t, t0, 0.5)
    n = len(linhas)
    if a > 0:
        centro(c, cab[0], x + wc / 2, y - 24, 48, "b", ENT, a)
        centro(c, cab[1], x + wc * 1.5, y - 24, 48, "b", SAI, a)
        M.line(c, x, y, x + 2 * wc, y, TINTA, a, 4)
        M.line(c, x + wc, y, x + wc, y + hl * n + 10, TINTA, a, 4)
    for i, (e, s) in enumerate(linhas):
        ry = y + 10 + hl * i
        ti = tl[i] if tl else t0 + 0.3 + 0.15 * i
        E.foco(c, t, ti, 0.4, lambda q, e=e, s=s, ry=ry: (
            centro(c, E._num(e), x + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ENT, q),
            centro(c, E._num(s), x + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", SAI, q)), sobe=6)


def salto_tab(c, t, t0, x, y0, y1, rot, cor=CERTO, d=0.5):
    """arco à direita da tabela, de uma linha para a seguinte, com o quanto subiu"""
    q = ease_out(prog(t, t0, d))
    if q > 0:
        r = (y1 - y0) / 2
        E.arco(c, x, (y0 + y1) / 2, r, -90, 180 * q, cor, 6)
        if q > 0.95:
            M.arrow(c, x + 4, y1 - 2, x - 4, y1, cor, 1.0, 6, 18)
        E.foco(c, t, t0 + 0.3, 0.3, lambda a: E.escreve(c, rot, x + r + 14, (y0 + y1) / 2 + 18, 48, "g", cor, a))


def taximetro(c, t, t0, t1, cx, cy):
    """o taxímetro escuro da MAT-FUN-002: R$ 5,00 no visor e "+ R$ 2,50 por km" embaixo"""
    a = ep(t, t0 - 0.2, 0.5)
    if a <= 0:
        return
    w, h = 560, 330
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 36, TINTA, a)
    M.rrect(c, cx - w / 2 + 34, cy - h / 2 + 40, w - 68, 150, 18, "#1E2A1E", a)
    centro(c, "TÁXI", cx, cy - h / 2 - 30, 56, "g", TINTA, a)
    E.foco(c, t, t0, 0.4, lambda q: centro(c, "R$ 5,00", cx, cy - h / 2 + 145, 96, "g", "#9BFF8A", q))
    E.foco(c, t, t1, 0.4, lambda q: centro(c, "+ R$ 2,50 por km", cx, cy + h / 2 - 50, 52, "b", BR, q))


def eixos(c, t, P, t0, mx, my, nx="x", ny="y", size=36, rot_y=True):
    """plano em etapas (MAT-FUN-001/006/007): grade, eixo x índigo, eixo y preto"""
    x, y, w, h = P.caixa
    if t < t0:
        return
    q = ep(t, t0, 0.8)
    for v in mx:
        M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
    for v in my:
        M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, nx, x + w + 10 - E.larg(nx, "i", 46), P.oy - 22, 46, "i", ENT, a))
    for i, v in enumerate(mx):
        if v == 0 and P.xmin < 0:
            continue
        X = P.x(v)
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
            M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
            centro(c, E._num(v), X + (14 if v == 0 else 0), P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, ny, P.ox + 22, y - 16, 46, "i", SAI, a))
    for i, v in enumerate(my):
        if v == 0:
            continue
        Y = P.y(v)
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
            M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
            rot_y and E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def anel(c, t, t0, P, xv, yv, cor=CERTO, r=26, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, *P(xv, yv), r, -90, 360 * q, cor, largura)


def marca_eixo(c, t, t0, P, v, cor=SAI, size=40):
    """o valor no eixo y numa pílula"""
    s = E._num(v)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, P.ox - 24 - E.larg(s, "g", size) / 2, P.y(v), size, "g", fundo=cor, a=a), sobe=0)


def resultado(c, t, t0, s, cx, cy, r=110):
    k = ease_back(prog(t, t0, 0.6))
    if k > 0:
        E.bola(c, cx, cy, r * k)
        size = r * (0.62 if len(s) <= 4 else 0.5 if len(s) <= 6 else 0.4)
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + size * 0.36, size, "g", BR, a), sobe=0)


def regua_desenho(c, P, A, B, a=1.0):
    """uma régua de verdade, encostada nos dois pontos"""
    if a <= 0:
        return
    (ax, ay), (bx, by) = P(*A), P(*B)
    ang = math.degrees(math.atan2(by - ay, bx - ax))
    L = math.hypot(bx - ax, by - ay) + 260
    c.save()
    c.translate((ax + bx) / 2, (ay + by) / 2)
    c.rotate(ang)
    M.rrect(c, -L / 2, 10, L, 64, 10, "#E8C46A", 0.85 * a)
    for i in range(int(L // 24)):
        hh = 22 if i % 5 == 0 else 12
        M.line(c, -L / 2 + 12 + i * 24, 10, -L / 2 + 12 + i * 24, 10 + hh, TINTA, 0.6 * a, 3)
    c.restore()


# ---------------- gancho ----------------
PG = E.Plano(1100, 200, 640, 620, -3, 3, -2, 5)


def b_gancho(c, t, C, b):
    def cena1():
        E.plano(c, t, C["s01.a"], *PG.caixa, PG.xmin, PG.xmax, PG.ymin, PG.ymax, rotulos=False, size=30)
        tabelinha = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
        for i, xv in enumerate(tabelinha):
            q = (1 - ep(t, C["s01.b"], 0.4))
            k = ease_back(prog(t, C["s01.a"] + 0.6 + 0.25 * i, 0.4)) * q
            if k > 0:
                c.drawCircle(*PG(xv, xv * xv - 1 + 0.5), 12 * k, M.paint(TINTA2))
        E.frase(c, t, C["s01.a"], [("tabela", "g", 72), ("com", "i", 72), ("vários", "g", 72, TINTA2), ("pontos", "i", 72)], XE, 300)
        if t >= C["s01.b"]:
            E.reta_pontos(c, t, C["s01.b"] + 0.3, PG, (-1, 0.5), (2, 3.5), d=0.8)
        E.frase(c, t, C["s01.b"], [("2", "g", 110, COR), ("pontos", "g", 90, COR), ("bastam", "i", 90)], XE, 470)
        E.frase(c, t, C["s01.c"], [("táxi,", "g", 60), ("conta", "i", 60), ("de", "i", 60), ("luz,", "g", 60)], XE, 620)
        E.frase(c, t, C["s01.c"] + 0.8, [("salário", "g", 60), ("com", "i", 60), ("comissão", "g", 60)], XE, 710)
    E.saida(c, t, C["s01.d"] - 0.1, cena1)
    E.saida(c, t, C["s02"] - 0.1, lambda: E.frase(c, t, C["s01.d"], [("função", "g", 200, COR), ("afim", "g", 200, COR)], W / 2, 620, "center"))
    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.4, [("escrever", "i", 90), ("a", "i", 90), ("lei", "g", 100, COR)], XE, 450)
        E.frase(c, t, C["s02.b"], [("traçar", "i", 90), ("a", "i", 90), ("reta", "g", 100, COR)], XE, 610)
        E.frase(c, t, C["s02.b"] + 1.0, [("com", "i", 72), ("2", "g", 80), ("pontos", "i", 72)], XE, 730)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, w, y = 900, 860, 360
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 340, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("o", "i", 64), ("gráfico", "g", 64, COR), ("de", "i", 64), ("uma", "i", 64), ("função", "i", 64)], x + 44, y + 100)
    E.frase(c, t, C["s03.b"] + 1.4, [("escolha", "i", 54), ("o", "i", 54), ("x,", "g", 58, ENT), ("calcule", "i", 54), ("o", "i", 54), ("y", "g", 58)], x + 44, y + 200)
    E.frase(c, t, C["s03.b"] + 2.6, [("marque", "i", 54)], x + 44, y + 290)
    E.foco(c, t, C["s03.b"] + 2.8, 0.5, lambda a: par(c, "x", "y", x + 260, y + 290, 58, a))
    E.cursor(c, x + w - 30, y + 300, ep(t, C["s03.b"], 0.4))


# ---------------- táxi ----------------
TABX, TABY = 260, 330
LINHAS = [(0, 5), (1, 7.5), (2, 10), (3, 12.5)]


def b_taxi(c, t, C, b):
    def s04():
        taximetro(c, t, C["s04.a"], C["s04.c"], 1350, 520)
        E.frase(c, t, C["s04.a"], [("R$", "g", 96, COR), ("5", "g", 96, COR)], XE, 330)
        E.frase(c, t, C["s04.a"] + 0.6, ps("só para começar", "i", 66), XE, 430)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.pilula(c, "bandeirada", XE + 200, 540, 52, "g", fundo=COR, a=a))
        E.frase(c, t, C["s04.c"], [("+", "g", 96, COR), ("R$", "g", 96, COR), ("2,50", "g", 96, COR)], XE, 720)
        E.frase(c, t, C["s04.c"] + 0.6, ps("por quilômetro", "i", 66), XE, 820)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return

    def s05():
        tl = [C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]]
        tabela2(c, t, C["s05"], [(0, "5"), (1, "7,50"), (2, "10"), (3, "12,50")], TABX, TABY, tl=tl)
        for i in range(3):
            y0 = TABY + 10 + 96 * i + 48
            salto_tab(c, t, C["s05.e"] + 0.4 * i, TABX + 2 * 230 + 30, y0, y0 + 96, "+2,50")
        E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: E.pilula(c, "só a bandeirada", 1340, TABY + 58, 44, "g", fundo=TINTA2, a=a))
        E.frase(c, t, C["s05.e"], [("sobe", "i", 66), ("sempre", "g", 66, CERTO), ("o", "i", 66), ("mesmo", "i", 66)], 1040, 640)
        E.frase(c, t, C["s05.e"] + 0.8, [("R$", "g", 72, CERTO), ("2,50", "g", 72, CERTO)], 1040, 750)
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], [("a", "i", 72), ("lei:", "g", 72, COR)], XE, 210)
    E.foco(c, t, C["s06.a"], 0.4, lambda a: mista(c, [("P = 5", SAI)], XE, 400, 120, a))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: mista(c, [(" + 2,5", TINTA), ("d", ENT)], XE + E.larg("P = 5", "g", 120), 400, 120, a))
    q = ep(t, C["s06.c"], 0.4)
    if q > 0:
        M.rrect(c, XE - 30, 270, E.larg("P = 5 + 2,5d", "g", 120) + 60, 175, 24, COR, 0.08 * q)
    E.frase(c, t, C["s06.d"], [("d", "g", 60, ENT), ("=", "g", 58), ("distância", "i", 58), ("(km)", "i", 54, TINTA2)], XE, 540)
    E.frase(c, t, C["s06.d"] + 0.8, [("P", "g", 60), ("=", "g", 58), ("preço", "i", 58), ("(R$)", "i", 54, TINTA2)], XE + 560, 540)
    E.frase(c, t, C["s06.e"], [("6", "g", 66, ENT), ("km:", "i", 62)], XE, 720)
    fml(c, t, C["s06.e"] + 0.3, "2,5 · 6 = 15", XE + 230, 720, 80)
    fml(c, t, C["s06.f"], "5 + 15 = 20", XE + 230, 860, 80)
    resultado(c, t, C["s06.f"] + 0.8, "R$ 20", 1500, 760, 140)


# ---------------- função afim ----------------
AFIM = [("f(", SAI), ("x", ENT), (") = ", SAI), ("a", TINTA), ("x", ENT), (" + ", TINTA), ("b", TINTA)]


def b_afim(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07.a"], [("função", "g", 110, COR), ("afim", "g", 110, COR)], W / 2, 250, "center")
        cs = mista_em(c, t, C["s07.b"], AFIM, W / 2, 480, 150, "center")
        (ca, wa), (cb, wb) = cs[3], cs[6]
        caixa_em(c, t, C["s07.c"], ca, wa, 480, 150, COR)
        E.foco(c, t, C["s07.c"] + 0.3, 0.4, lambda a: (centro(c, "multiplica", ca, 600, 46, "b", COR, a), centro(c, "o x", ca, 656, 46, "b", COR, a)))
        caixa_em(c, t, C["s07.d"], cb, wb, 480, 150, COR)
        E.foco(c, t, C["s07.d"] + 0.3, 0.4, lambda a: (centro(c, "o número", cb, 600, 46, "b", COR, a), centro(c, "sozinho", cb, 656, 46, "b", COR, a)))
        E.foco(c, t, C["s07.e"], 0.5, lambda a: mista(c, [("P = ", SAI), ("2,5", COR), ("d", ENT), (" + ", TINTA), ("5", COR)], W / 2, 800, 96, a, "center"))
        E.foco(c, t, C["s07.e"] + 0.8, 0.5, lambda a: centro(c, "a = 2,5   ·   b = 5", W / 2, 920, 64, "g", TINTA2, a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08"], [("outro", "i", 72), ("exemplo", "i", 72)], W / 2, 260, "center")
    cs = mista_em(c, t, C["s08.a"], [("f(", SAI), ("x", ENT), (") = ", SAI), ("2", TINTA), ("x", ENT), (" − 1", TINTA)], W / 2, 500, 150, "center")
    (ca, wa), (cb, wb) = cs[3], cs[5]
    caixa_em(c, t, C["s08.b"], ca, wa, 500, 150, COR)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: centro(c, "a = 2", ca, 640, 64, "g", COR, a))
    caixa_em(c, t, C["s08.b"] + 0.6, cb, wb, 500, 150, COR)
    E.foco(c, t, C["s08.b"] + 0.6, 0.4, lambda a: centro(c, "b = −1", cb, 640, 64, "g", COR, a))
    E.frase(c, t, C["s08.c"], [("o", "i", 64), ("b", "g", 66, COR), ("leva", "i", 64), ("o", "i", 64), ("sinal", "g", 66), ("da", "i", 64), ("frente", "i", 64)],
            W / 2, 860, "center")
    q = ep(t, C["s08.c"] + 0.4, 0.4)
    if q > 0:
        E.arco(c, cb - wb / 2 + E.larg(" ", "g", 150) + E.larg("−", "g", 150) / 2, 455, 46, -90, 360 * ease_out(prog(t, C["s08.c"] + 0.4, 0.5)), ERRADO, 6)


# ---------------- gráfico ----------------
PT = E.Plano(1080, 200, 700, 660, -0.6, 4.6, -1.2, 15.5)
TX, TY = [0, 1, 2, 3, 4], [0, 5, 10, 15]
PF = E.Plano(1080, 170, 700, 720, -2.6, 4.6, -3.6, 5.6)
FX, FY = list(range(-2, 5)), list(range(-3, 6))


def b_grafico(c, t, C, b):
    def taxi_plano():
        eixos(c, t, PT, C["s09"], TX, TY, "d (km)", "P (R$)")
        para = 1 - ep(t, C["s10.a"], 0.4)
        for i, (d, p) in enumerate(LINHAS):
            k = ease_back(prog(t, C["s09"] + 1.6 + 0.5 * i, 0.45))
            fica = 1.0 if d in (1, 3) else para
            if k > 0 and fica > 0:
                c.drawCircle(*PT(d, p), 15 * k, M.paint(TINTA, fica))
        if t >= C["s09.a"]:
            a = ep(t, C["s09.a"], 0.4) * (1 - ep(t, C["s09.b"], 0.3))
            if a > 0:
                (x0, y0), (x1, y1) = PT(-0.3, taxi(-0.3)), PT(4.3, taxi(4.3))
                M.line(c, x0, y0, x1, y1, TINTA2, a, 4, dash=[16, 12])
        if C["s09.b"] <= t < C["s10.a"] + 0.3:
            E.reta_pontos(c, t, C["s09.b"], PT, (0, 5), (3, 12.5), pontos=False)
        regua_desenho(c, PT, (1, 7.5), (3, 12.5), ep(t, C["s10.b"], 0.5))
        if t >= C["s10.b"] + 0.6:
            E.reta_pontos(c, t, C["s10.b"] + 0.6, PT, (1, 7.5), (3, 12.5), pontos=False)
        E.frase(c, t, C["s09"], [("os", "i", 70), ("pontos", "i", 70), ("do", "i", 70), ("táxi", "g", 70)], XE, 290)
        E.frase(c, t, C["s09.a"], [("ficam", "i", 70), ("alinhados", "g", 70, COR)], XE, 400)
        E.frase(c, t, C["s09.b"], [("gráfico:", "g", 70), ("uma", "i", 70), ("reta", "g", 76, COR)], XE, 540)
        E.frase(c, t, C["s10.a"], [("2", "g", 90, COR), ("pontos", "g", 76, COR), ("bastam", "i", 76)], XE, 700)
        E.frase(c, t, C["s10.b"], [("por", "i", 60), ("2", "g", 64), ("pontos,", "i", 60), ("uma", "i", 60), ("reta", "g", 64), ("só", "i", 60)], XE, 820)
    E.saida(c, t, C["s11"] - 0.1, taxi_plano)
    if t < C["s11"]:
        return
    eixos(c, t, PF, C["s11"], FX, FY)
    fml(c, t, C["s11.a"], "f(x) = 2x − 1", XE, 200, 96)

    def contas():
        fml(c, t, C["s11.b"], "x = 0:  2 · 0 − 1 = −1", XE, 360, 60)
        E.ponto(c, t, C["s11.c"], PF, 0, -1, cor=COR, r=16)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: par(c, "0", "−1", XE + 60, 460, 64, a))
        E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: par(c, "0", "−1", PF.x(0) + 24, PF.y(-1) + 50, 40, a))
        fml(c, t, C["s11.d"], "x = 2:  2 · 2 − 1 = 3", XE, 600, 60)
        E.ponto(c, t, C["s11.e"], PF, 2, 3, cor=COR, r=16)
        E.foco(c, t, C["s11.e"], 0.4, lambda a: par(c, "2", "3", XE + 60, 700, 64, a))
        E.foco(c, t, C["s11.e"] + 0.3, 0.4, lambda a: par(c, "2", "3", PF.x(2) + 26, PF.y(3) + 10, 40, a))
        E.frase(c, t, C["s11.f"], [("ligue", "g", 64, COR), ("e", "i", 62), ("prolongue", "g", 64, COR)], XE, 860)
    E.saida(c, t, C["s12"] - 0.1, contas)
    if t >= C["s11.f"]:
        E.reta_pontos(c, t, C["s11.f"], PF, (0, -1), (2, 3), pontos=False, d=1.0)
        if t >= C["s12"]:
            for xv, yv in ((0, -1), (2, 3)):
                c.drawCircle(*PF(xv, yv), 16, M.paint(COR))
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], [("conferir:", "g", 66, CERTO), ("um", "i", 64), ("3º", "g", 66), ("ponto", "i", 64)], XE, 360)
    fml(c, t, C["s12.a"], "x = 1:  2 · 1 − 1 = 1", XE, 500, 64)
    E.ponto(c, t, C["s12.b"], PF, 1, 1, cor=CERTO, r=16)
    anel(c, t, C["s12.b"] + 0.2, PF, 1, 1, CERTO, 30)
    E.foco(c, t, C["s12.b"], 0.4, lambda a: (par(c, "1", "1", XE + 60, 620, 64, a), E.selo(c, XE + 400, 600, 34, True, a)))
    E.frase(c, t, C["s12.c"], [("caiu", "i", 60), ("fora?", "g", 62, ERRADO), ("conta", "i", 60), ("errada", "g", 62, ERRADO)], XE, 800)
    if t >= C["s12.c"]:
        k = ease_back(prog(t, C["s12.c"] + 0.3, 0.4))
        X, Y = PF(1, 2.2)
        if k > 0:
            c.drawCircle(X, Y, 14 * k, M.paint(ERRADO, 0.85))
            E.risco(c, X - 18, Y - 18, X + 18, Y + 18, t, C["s12.c"] + 0.7, largura=6)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("trocar", "g", 76, ERRADO), ("os", "i", 72), ("números", "i", 72), ("de", "i", 72), ("lugar", "i", 72)], XE, 220)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: mista(c, [("P = 5", ERRADO), ("d", ENT), (" + 2,5", ERRADO)], XE, 400, 110, a))
    E.foco(c, t, C["s13.b"] + 0.5, 0.4, lambda a: E.selo(c, XE + 760, 365, 40, False, a))
    fml(c, t, C["s13.c"], "6 km:  5 · 6 + 2,5 = 32,50", XE, 560, 72, ERRADO)
    E.frase(c, t, C["s13.c"] + 1.4, [("e", "i", 62), ("não", "i", 62), ("R$", "g", 66, CERTO), ("20", "g", 66, CERTO)], XE + 1060, 560)
    E.frase(c, t, C["s13.d"], [("por", "i", 60), ("km", "g", 62), ("→", "g", 62, TINTA2), ("multiplica", "i", 60), ("o", "i", 60), ("d", "g", 66, ENT)], XE, 720)
    E.frase(c, t, C["s13.e"], [("fixo", "g", 62), ("→", "g", 62, TINTA2), ("sozinho", "i", 60)], XE, 820)
    E.foco(c, t, C["s13.e"] + 0.6, 0.5, lambda a: mista(c, [("P = 5 + 2,5", CERTO), ("d", ENT)], 1180, 780, 100, a))
    E.foco(c, t, C["s13.e"] + 0.9, 0.4, lambda a: E.selo(c, 1180 + E.larg("P = 5 + 2,5d", "g", 100) + 70, 745, 40, True, a))


# ---------------- atalho (palco escuro) ----------------
PA = E.Plano(1100, 260, 620, 600, -2.5, 3.5, -3, 5)


def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 66, CLARO), XE, 180)
        E.frase(c, t, C["s14.a"], [("o", "i", 76, CLARO), ("ponto", "i", 76, CLARO), ("do", "i", 76, CLARO), ("x", "g", 84, CLARO), ("=", "g", 80, BR),
                                   ("0", "g", 84, BR)], XE, 320)
        E.frase(c, t, C["s14.a"] + 1.0, [("sai", "i", 76, CLARO), ("de", "i", 76, CLARO), ("graça", "g", 80, BR)], XE, 420)
        E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "f(0) = a · 0 + b = b", XE, 580, 76, "g", BR, a))
        E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "2x − 1 → ", XE, 720, 70, "g", CLARO, a))
        E.foco(c, t, C["s14.c"] + 0.3, 0.5, lambda a: par(c, "0", "−1", XE + E.larg("2x − 1 → ", "g", 70) + 10, 720, 70, a, cores=(CLARO, BR), tinta=BR))
        E.frase(c, t, C["s14.d"], [("2º", "g", 60, BR), ("ponto:", "i", 60, CLARO), ("um", "i", 60, CLARO), ("x", "g", 64, CLARO), ("fácil", "g", 64, BR)], XE, 860)
        E.plano(c, t, C["s14.c"] - 0.3, *PA.caixa, PA.xmin, PA.xmax, PA.ymin, PA.ymax, grade=True, rotulos=False, size=30, escuro=True)
        E.ponto(c, t, C["s14.c"], PA, 0, -1, cor=BR, r=17)
        q = ease_out(prog(t, C["s14.c"] + 0.2, 0.5))
        if q > 0:
            E.arco(c, *PA(0, -1), 32, -90, 360 * q, "#FFE680", 6)
        E.ponto(c, t, C["s14.d"] + 0.3, PA, 1, 1, cor=CLARO, r=15)
        if t >= C["s14.d"] + 0.8:
            E.reta_pontos(c, t, C["s14.d"] + 0.8, PA, (0, -1), (1, 1), cor=CLARO, pontos=False)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15.a"], [("não", "g", 72, ERRADO), ("compensa:", "i", 72, CLARO)], XE, 230)
    E.frase(c, t, C["s15.a"] + 1.0, [("x", "g", 72, CLARO), ("de", "i", 68, CLARO), ("50", "g", 72, BR), ("a", "i", 68, CLARO), ("100", "g", 72, BR)], XE, 340)
    # plano que só mostra x de 50 a 100: o x = 0 fica fora da tela
    x0, y0, w, h = 1000, 300, 780, 520
    a = ep(t, C["s15.a"] + 0.6, 0.5)
    if a > 0:
        M.arrow(c, x0, y0 + h, x0 + w + 40, y0 + h, CLARO, a, 5, 22)
        for i, v in enumerate((50, 60, 70, 80, 90, 100)):
            X = x0 + 40 + i * (w - 80) / 5
            M.line(c, X, y0 + h - 10, X, y0 + h + 10, CLARO, a, 4)
            centro(c, str(v), X, y0 + h + 54, 36, "b", CLARO, a)
        M.line(c, x0 + 20, y0 + h - 60, x0 + w, y0 + 60, BR, a, 7)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (M.arrow(c, x0 + 60, y0 + 80, x0 - 120, y0 + 80, ERRADO, a, 8, 26),
                                             E.escreve(c, "x = 0: fora da tela", x0 + 80, y0 + 96, 44, "g", ERRADO, a)))
    E.frase(c, t, C["s15.b"], [("o", "i", 62, CLARO), ("x", "g", 66, CLARO), ("=", "g", 66, BR), ("0", "g", 66, BR), ("nem", "i", 62, CLARO), ("cabe", "g", 64, BR)],
            XE, 520)
    for i, (v, k) in enumerate(((60, 0.2), (90, 0.8))):
        X = x0 + 40 + (v - 50) / 10 * (w - 80) / 5
        Y = lerp(y0 + h - 60, y0 + 60, (X - x0 - 20) / (w - 20))
        kk = ease_back(prog(t, C["s15.c"] + 0.3 * i, 0.4))
        if kk > 0:
            c.drawCircle(X, Y, 16 * kk, M.paint("#FFE680"))
    E.frase(c, t, C["s15.c"], [("escolha", "i", 62, CLARO), ("2", "g", 66, BR), ("x", "g", 66, CLARO), ("do", "i", 62, CLARO), ("desenho", "g", 64, BR)], XE, 680)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 64, COR), XE, 170)
    E.frase(c, t, C["s16"] + 0.6, [("um", "i", 66), ("encanador", "g", 66)], XE, 280)
    E.frase(c, t, C["s16.a"], [("R$", "g", 70), ("40", "g", 70), ("a", "i", 64), ("visita", "i", 64)], XE, 400)
    E.frase(c, t, C["s16.b"], [("+", "g", 70, COR), ("R$", "g", 70), ("30", "g", 70), ("por", "i", 64), ("hora", "g", 64, ENT)], XE, 500)
    perguntas = (("s16.c", "1", [("a", "i", 60), ("lei", "g", 60, COR), ("do", "i", 60), ("preço?", "i", 60)]),
                 ("s16.d", "2", [("3", "g", 62, ENT), ("horas", "i", 60), ("custam?", "i", 60)]),
                 ("s16.e", "3", [("que", "i", 60), ("2", "g", 62), ("pontos", "g", 60), ("para", "i", 60), ("a", "i", 60), ("reta?", "g", 60, COR)]))
    for i, (k, n, partes) in enumerate(perguntas):
        yy = 660 + i * 120
        E.foco(c, t, C[k], 0.5, lambda a, n=n, yy=yy: (E.bola(c, XE + 34, yy - 20, 34, a=a), centro(c, n, XE + 34, yy - 4, 44, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 100, yy)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1440, cy=480, r=150)


# ---------------- resposta ----------------
PE = E.Plano(1120, 200, 660, 680, -0.4, 4.4, -8, 155)
EX, EY = [0, 1, 2, 3, 4], list(range(0, 151, 20))


def b_resposta(c, t, C, b):
    def s18():
        E.frase(c, t, C["s18.a"], [("multiplica", "i", 64), ("as", "i", 64), ("horas:", "g", 64, ENT), ("30", "g", 76, COR)], XE, 270)
        E.frase(c, t, C["s18.b"], [("fixo:", "g", 64), ("a", "i", 64), ("visita,", "i", 64), ("40", "g", 76, COR)], XE, 400)
        E.foco(c, t, C["s18.c"], 0.5, lambda a: mista(c, [("f(", SAI), ("x", ENT), (") = 30", SAI), ("x", ENT), (" + 40", SAI)], XE, 600, 120, a))
        E.frase(c, t, C["s18.d"], [("x", "g", 60, ENT), ("=", "g", 58), ("horas", "i", 58), ("·", "g", 58, TINTA2), ("f(x)", "g", 60), ("=", "g", 58), ("preço", "i", 58),
                                   ("(R$)", "i", 54, TINTA2)], XE, 760)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19"] - 0.4, 0.4, lambda a: mista(c, [("f(", SAI), ("x", ENT), (") = 30", SAI), ("x", ENT), (" + 40", SAI)], XE, 190, 80, a))
    fml(c, t, C["s19.a"], "30 · 3 = 90", XE, 330, 72)
    fml(c, t, C["s19.b"], "90 + 40 = 130", XE, 450, 72)
    E.foco(c, t, C["s19.b"] + 0.6, 0.4, lambda a: E.pilula(c, "R$ 130", XE + 680, 425, 56, "g", fundo=COR, a=a))
    eixos(c, t, PE, C["s19.c"] - 0.6, EX, EY, "horas", "R$", rot_y=False)
    pontos = (("s19.c", 0, 40, COR), ("s19.d", 1, 70, COR), ("s19.e", 3, 130, CERTO))
    for k, xv, yv, cor in pontos:
        E.ponto(c, t, C[k], PE, xv, yv, cor=cor, r=16)
        marca_eixo(c, t, C[k] + 0.3, PE, yv)
        if xv:
            M.line(c, *PE(xv, yv), PE.ox, PE.y(yv), TINTA, 0.6 * ep(t, C[k] + 0.1, 0.4), 4, dash=E.TRACO)
    E.foco(c, t, C["s19.c"], 0.4, lambda a: par(c, "0", "40", XE, 620, 66, a))
    E.foco(c, t, C["s19.d"], 0.4, lambda a: par(c, "1", "70", XE + 330, 620, 66, a))
    if t >= C["s19.d"] + 0.5:
        E.reta_pontos(c, t, C["s19.d"] + 0.5, PE, (0, 40), (1, 70), pontos=False)
    anel(c, t, C["s19.e"] + 0.2, PE, 3, 130, CERTO, 30)
    E.foco(c, t, C["s19.e"], 0.4, lambda a: (par(c, "3", "130", XE, 780, 66, a), E.escreve(c, "conferência", XE + 380, 780, 52, "i", CERTO, a)))


# ---------------- fechamento ----------------
PN = E.Plano(1160, 380, 560, 480, -1, 5, -1, 6)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("função", "g", 80), ("afim:", "g", 80), ("ax", "g", 84, COR), ("+", "g", 84, COR), ("b", "g", 84, COR)]),
                 ("s20.b", [("o", "i", 80), ("gráfico", "i", 80), ("é", "i", 80), ("uma", "i", 80), ("reta", "g", 84, COR)]),
                 ("s20.c", [("2", "g", 84, COR), ("pontos", "g", 80), ("bastam", "i", 80)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 28, 52, a=a),
                                                         E.escreve(c, str(i + 1), 230 - E.larg(str(i + 1), "g", 60) / 2, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 260)
    E.frase(c, t, C["s21.a"], [("o", "i", 90), ("que", "i", 90), ("o", "i", 90), ("a", "g", 110, COR), ("e", "i", 90), ("o", "i", 90), ("b", "g", 110, COR),
                               ("contam", "i", 90)], XE, 420)
    E.frase(c, t, C["s21.b"], [("de", "i", 60), ("onde", "i", 60), ("a", "i", 60), ("reta", "g", 62), ("parte", "g", 62, COR)], XE, 560)
    E.frase(c, t, C["s21.c"], [("quanto", "i", 60), ("sobe", "g", 62, COR), ("a", "i", 60), ("cada", "i", 60), ("passo", "g", 62)], XE, 660)
    if t >= C["s21.a"]:
        E.plano(c, t, C["s21.a"], *PN.caixa, PN.xmin, PN.xmax, PN.ymin, PN.ymax, grade=False, rotulos=False, size=30, d=0.5)
        E.reta_pontos(c, t, C["s21.a"] + 0.3, PN, (0, 1), (4, 5), pontos=False)
        E.ponto(c, t, C["s21.b"], PN, 0, 1, cor=COR, r=16)
        q = ep(t, C["s21.c"], 0.4)
        if q > 0:
            (x1, y1), (x2, y2) = PN(2, 3), PN(3, 3)
            M.line(c, x1, y1, x2, y2, CERTO, q, 6, dash=[12, 8])
            M.line(c, x2, y2, *PN(3, 4), CERTO, q, 6, dash=[12, 8])
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 260, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(520, 285, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 120), ("estudos!", "i", 120, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, taxi=b_taxi, afim=b_afim, grafico=b_grafico, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
