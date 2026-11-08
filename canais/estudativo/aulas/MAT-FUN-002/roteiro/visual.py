"""Visual — Estudativo · MAT-FUN-002: o que é função, cada entrada com uma saída.

Linguagem visual da trilha Funções (a mesma da MAT-FUN-001):
- entrada (x, d, m...) = índigo da matéria (ENT); saída (y, P, C...) = tinta preta (SAI). Toda letra e número de entrada sai em índigo.
- máquina: caixa escura com a regra em branco; a entrada entra pela esquerda numa esfera índigo e a saída sai pela direita numa esfera preta.
- diagrama de flechas: oval A (entradas) com contorno índigo à esquerda, oval B (saídas) com contorno preto à direita; flecha índigo.
  Flecha que derruba a função fica vermelha; o elemento culpado ganha um anel vermelho.
- tabela de duas colunas: cabeçalho "entrada" em índigo e "saída" em preto; a linha culpada ganha faixa vermelha.
Peças locais: mista() (fórmula com cores por parte), maquina(), passa(), ovais(), flecha(), tabela2(), faixa()."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA
ARQUIVO_FINAL = "estudativo_MAT-FUN-002_o_que_e_funcao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("formula", "maquina", "flechas", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 5 + 2.5 * 4 == 15 and 5 + 2.5 * 10 == 30 and 40 + 90 * 3 == 310


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def mista(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """texto numa linha com uma cor por parte: partes = [(texto, cor)]; devolve o centro x de cada parte"""
    ws = [E.larg(s, est, size) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x
    cs = []
    for (s, cor), w in zip(partes, ws):
        E.escreve(c, s, xx, y, size, est, cor, a)
        cs.append(xx + w / 2)
        xx += w
    return cs


def mista_em(c, t, t0, partes, x, y, size, align="left", est="g"):
    E.foco(c, t, t0, 0.5, lambda a: mista(c, partes, x, y, size, a, align, est))
    return mista(c, partes, x, y, size, 0, align, est)


def bolinha(c, X, Y, s, cor, a=1.0, r=62, size=None):
    if a <= 0:
        return
    size = size or (r * 0.95 if len(s) < 3 else r * 0.7)
    E.bola(c, X, Y, r, cor, a)
    centro(c, s, X, Y + size * 0.36, size, "g", BR, a)


def maquina(c, cx, cy, regra, a=1.0, w=560, h=300, size=76, rotulos=True):
    """a máquina da função: caixa escura com a regra; boca de entrada à esquerda (índigo) e de saída à direita"""
    if a <= 0:
        return
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.25 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2 + 10, cy - h / 2 + 18, w, h), 40, 40), s)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 40, TINTA, a)
    M.rrect(c, cx - w / 2 - 22, cy - 70, 44, 140, 14, ENT, a)
    M.rrect(c, cx + w / 2 - 22, cy - 70, 44, 140, 14, TINTA2, a)
    for i in range(3):  # luzinhas
        c.drawCircle(cx - 60 + 60 * i, cy - h / 2 + 40, 9, M.paint(CLARO if i == 1 else "#3C3C46", a))
    if regra:
        E.formula(c, regra, cx, cy + size * 0.36 + 10, size, "g", BR, a, "center")
    if rotulos:
        centro(c, "entrada", cx - w / 2 - 170, cy + 130, 46, "i", ENT, a)
        centro(c, "saída", cx + w / 2 + 170, cy + 130, 46, "i", SAI, a)


def passa(c, t, cx, cy, ent, sai, t_in, t_out, w=560, some=None, r=62):
    """a entrada rola até a boca e some; a saída nasce na outra boca e anda para fora. some = instante em que a saída vai embora"""
    p = ease_io(prog(t, t_in, 0.8))
    if 0 < p < 1:
        X = lerp(cx - w / 2 - 300, cx - w / 2 - 10, p)
        bolinha(c, X, cy, ent, ENT, 1 - ep(t, t_in + 0.55, 0.25), r)
    elif p <= 0 and t >= t_in - 0.6:
        bolinha(c, cx - w / 2 - 300, cy, ent, ENT, ep(t, t_in - 0.6, 0.4), r)
    q = ease_out(prog(t, t_out, 0.8))
    if q > 0:
        a = 1.0 if some is None else 1 - ep(t, some, 0.4)
        bolinha(c, lerp(cx + w / 2, cx + w / 2 + 280, q), cy, sai, SAI, min(1, q * 3) * a, r)


def ovais(c, t, t0, cxa, cxb, cy, A, B, ta=None, tb=None, tB=None, size=60, dy=110, rw=150, nomes=("A", "B"), sub=("entradas", "saídas"), escuro=False):
    """dois conjuntos em ovais: A (entradas, índigo) e B (saídas, preto). ta/tb = instantes dos elementos; tB = instante do oval B.
    Devolve os centros: (pa, pb), dicionários elemento → (x, y)"""
    n = max(len(A), len(B))
    rh = (n * dy + 70) / 2
    tinta = BR if escuro else TINTA
    ca = CLARO if escuro else ENT
    tB = t0 + 0.3 if tB is None else tB
    sub = sub or (None, None)
    pa, pb = {}, {}
    for cx, els, cor, tt, tov, nome, sb, d in ((cxa, A, ca, ta, t0, nomes[0], sub[0], pa), (cxb, B, tinta, tb, tB, nomes[1], sub[1], pb)):
        q = ease_io(prog(t, tov, 0.6))
        if q > 0:
            r = skia.Rect.MakeXYWH(cx - rw, cy - rh, 2 * rw, 2 * rh)
            if not escuro:
                c.drawOval(r, M.paint(BR, 0.75 * q))
            c.drawArc(r, -90, 360 * q, False, M.paint(cor, 1.0, stroke=6, cap_round=True))
        if nome:
            E.foco(c, t, tov + 0.3, 0.4, lambda a, cx=cx, nome=nome, cor=cor: centro(c, nome, cx, cy - rh - 26, 64, "g", cor, a))
        if sb:
            E.foco(c, t, tov + 0.4, 0.4, lambda a, cx=cx, sb=sb, cor=cor: centro(c, sb, cx, cy + rh + 66, 46, "i", cor, a))
        m = len(els)
        for i, v in enumerate(els):
            y = cy + (i - (m - 1) / 2) * dy
            d[v] = (cx, y)
            ti = (tt if tt is not None else tov + 0.4) + 0.12 * i
            E.foco(c, t, ti, 0.4, lambda a, v=v, cx=cx, y=y, cor=cor: centro(c, str(v), cx, y + size * 0.36, size, "g", cor, a), sobe=6)
    return pa, pb


def flecha(c, t, t0, p0, p1, cor=None, d=0.6, folga=(52, 62), largura=6):
    """flecha de um elemento de A até um de B"""
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    (x0, y0), (x1, y1) = p0, p1
    import math
    L = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    a0x, a0y = x0 + ux * folga[0], y0 + uy * folga[0]
    a1x, a1y = x1 - ux * folga[1], y1 - uy * folga[1]
    M.arrow(c, a0x, a0y, a1x, a1y, cor or ENT, 1.0, largura, 22, p)


def anel(c, t, t0, X, Y, r=48, cor=ERRADO, largura=6):
    q = ease_out(prog(t, t0, 0.5))
    if q > 0:
        E.arco(c, X, Y, r, -90, 360 * q, cor, largura)


def faixa(c, x, y, w, h, cor, a):
    if a > 0:
        M.rrect(c, x, y, w, h, 14, cor, 0.16 * a)


def tabela2(c, t, t0, linhas, x, y, cab=("entrada", "saída"), wc=240, hl=92, size=64, tl=None, escuro=False):
    """tabela de duas colunas, entrada (índigo) | saída (preto); devolve a caixa de cada linha (x, y, w, h)"""
    tinta = BR if escuro else TINTA
    ca = CLARO if escuro else ENT
    a = ep(t, t0, 0.5)
    n = len(linhas)
    if a > 0:
        centro(c, cab[0], x + wc / 2, y - 24, 46, "b", ca, a)
        centro(c, cab[1], x + wc * 1.5, y - 24, 46, "b", tinta, a)
        M.line(c, x, y, x + 2 * wc, y, tinta, a, 4)
        M.line(c, x + wc, y, x + wc, y + hl * n + 10, tinta, a, 4)
    caixas = []
    for i, (e, s) in enumerate(linhas):
        ry = y + 10 + hl * i
        caixas.append((x - 10, ry, 2 * wc + 20, hl))
        ti = tl[i] if tl else t0 + 0.3 + 0.15 * i
        E.foco(c, t, ti, 0.4, lambda q, e=e, s=s, ry=ry: (
            centro(c, E._num(e), x + wc / 2, ry + hl / 2 + size * 0.36, size, "g", ca, q),
            centro(c, E._num(s), x + wc * 1.5, ry + hl / 2 + size * 0.36, size, "g", tinta, q)), sobe=6)
    return caixas


# ---------------- gancho ----------------
def taximetro(c, t, C, cx, cy):
    a = ep(t, C["s01.a"] - 0.2, 0.5)
    if a <= 0:
        return
    w, h = 560, 330
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 36, TINTA, a)
    M.rrect(c, cx - w / 2 + 34, cy - h / 2 + 40, w - 68, 150, 18, "#1E2A1E", a)
    centro(c, "TÁXI", cx, cy - h / 2 - 30, 56, "g", TINTA, a)
    E.foco(c, t, C["s01.a"], 0.4, lambda q: centro(c, "R$ 5,00", cx, cy - h / 2 + 145, 96, "g", "#9BFF8A", q))
    E.foco(c, t, C["s01.b"], 0.4, lambda q: centro(c, "+ R$ 2,50 por km", cx, cy + h / 2 - 50, 52, "b", BR, q))


def b_gancho(c, t, C, b):
    def cena1():
        taximetro(c, t, C, 1400, 470)
        E.frase(c, t, C["s01.a"], [("R$", "g", 96, COR), ("5", "g", 96, COR)], XE, 330)
        E.frase(c, t, C["s01.a"] + 0.6, ps("só para começar", "i", 70), XE, 430)
        E.frase(c, t, C["s01.b"], [("+", "g", 96, COR), ("R$", "g", 96, COR), ("2,50", "g", 96, COR)], XE, 600)
        E.frase(c, t, C["s01.b"] + 0.6, ps("por quilômetro", "i", 70), XE, 700)
        E.frase(c, t, C["s01.c"], [("cada", "i", 72), ("distância,", "i", 72, ENT), ("um", "i", 72), ("preço", "g", 72), ("só", "i", 72)],
                W / 2, 900, "center")
    E.saida(c, t, C["s01.d"] - 0.1, cena1)
    E.saida(c, t, C["s02"] - 0.1, lambda: E.frase(c, t, C["s01.d"], [("função", "g", 260, COR)], W / 2, 620, "center"))

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("entrada", "g", 120, ENT), ("e", "i", 110), ("saída", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 3.6, [("tabela", "i", 90), ("ou", "i", 90), ("flechas:", "i", 90)], XE, 620)
        E.frase(c, t, C["s02.a"] + 4.6, [("é", "i", 100), ("função?", "g", 110, COR)], XE, 750)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 410)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 900, 860
    itens = (("s03.b", "trocar a letra", "por um número"), ("s03.c", "conjunto:", "{1, 2, 3}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 250 + i * 300
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 68)], x + 44, y + 96)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 68, COR)], x + 44, y + 190)
    E.foco(c, t, C["s03.b"] + 1.6, 0.5, lambda a: E.escreve(c, "d = 4 → 2,5·(4)", x + 420, 346, 46, "m", TINTA2, a))
    px = x + w - 30
    q = ease_io(prog(t, C["s03.c"] - 0.35, 0.5))
    E.cursor(c, px, lerp(250 + 210, 550 + 210, q), ep(t, C["s03.b"], 0.4))


# ---------------- fórmula ----------------
FORM = [("P", SAI), (" = ", TINTA), ("5", TINTA), (" + ", TINTA), ("2,5", TINTA), ("d", ENT)]


def b_formula(c, t, C, b):
    sobe = ease_io(prog(t, C["s05"] - 0.2, 0.8))
    y, size = lerp(430, 220, sobe), lerp(170, 110, sobe)
    E.foco(c, t, C["s04.a"], 0.6, lambda a: mista(c, FORM, W / 2, y, size, a, "center"))
    xs = mista(c, FORM, W / 2, y, size, 0, "center")
    # legendas: P, d, 5, 2,5
    leg = (("s04.b", 0, "preço (R$)", SAI), ("s04.c", 5, "distância (km)", ENT), ("s04.d", 2, "parte fixa", TINTA2), ("s04.e", 4, "por km", TINTA2))

    def legendas():
        for k, i, txt, cor in leg:
            X = xs[i]
            p = ep(t, C[k], 0.5)
            if p > 0:
                yl = 610 + (110 if i in (2, 4) else 0)
                M.arrow(c, X, yl - 60, X, y + 58, cor, p, 5, 18, p)
                E.foco(c, t, C[k], 0.4, lambda a, X=X, txt=txt, cor=cor, yl=yl: centro(c, txt, X, yl, 56, "b", cor, a))
    E.saida(c, t, C["s05"] - 0.3, legendas)
    if t < C["s05"]:
        return
    for cx, km, mul, tot, ks in ((560, "4", "10", "15", ("s05.a", "s05.b", "s05.c")), (1360, "10", "25", "30", ("s05.d", "s05.e", "s05.f"))):
        E.foco(c, t, C[ks[0]], 0.5, lambda a, cx=cx, km=km: mista(c, [("d", ENT), (" = ", TINTA), (km, ENT)], cx, 400, 90, a, "center"))
        E.foco(c, t, C[ks[1]], 0.5, lambda a, cx=cx, km=km, mul=mul: mista(c, [("2,5 × ", TINTA), (km, ENT), (" = " + mul, TINTA)], cx, 560, 76, a, "center"))
        E.foco(c, t, C[ks[2]], 0.5, lambda a, cx=cx, mul=mul, tot=tot: mista(c, [("5 + " + mul + " = ", TINTA), (tot, SAI)], cx, 700, 76, a, "center"))
        E.foco(c, t, C[ks[2]] + 0.6, 0.5, lambda a, cx=cx, tot=tot: E.pilula(c, f"P = R$ {tot}", cx, 850, 64, "g", fundo=SAI, a=a))


# ---------------- máquina ----------------
MX, MY = W / 2, 470


def b_maquina(c, t, C, b):
    def s06():
        E.foco(c, t, C["s06.a"], 0.5, lambda a: bolinha(c, 360, MY, "d", ENT, a, 80))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: (E.caixa_pontilhada(c, MX - 280, MY - 150, 560, 300, a),
                                                 E.formula(c, "5 + 2,5d", MX, MY + 30, 84, "g", TINTA, a, "center")))
        for x0, x1, k in ((460, MX - 300, "s06.a"), (MX + 300, 1460, "s06.b")):
            p = ep(t, C[k] + 0.4, 0.5)
            M.arrow(c, x0, MY, x1, MY, TINTA2, p, 6, 22, p)
        E.foco(c, t, C["s06.b"] + 0.4, 0.5, lambda a: bolinha(c, 1560, MY, "P", SAI, a, 80))
        E.frase(c, t, C["s06.a"], ps("você escolhe", "i", 52, ENT), 360, 640, "center", 0.1)
        E.frase(c, t, C["s06.b"], ps("a fórmula devolve", "i", 52), 1560, 640, "center", 0.1)
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "entrada", 360, 300, 60, "g", fundo=ENT, a=a))
        E.foco(c, t, C["s06.d"], 0.5, lambda a: E.pilula(c, "saída", 1560, 300, 60, "g", fundo=SAI, a=a))
        E.frase(c, t, C["s06.e"], [("o", "i", 84), ("preço", "g", 80), ("depende", "i", 84), ("da", "i", 84), ("distância", "g", 80, ENT)], W / 2, 880, "center")
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return

    def s07():
        E.foco(c, t, C["s07.a"], 0.6, lambda a: maquina(c, MX, MY, "5 + 2,5d", a))
        passa(c, t, MX, MY, "4", "15", C["s07.a"] + 1.0, C["s07.b"], some=C["s07.c"] - 0.9)
        passa(c, t, MX, MY, "10", "30", C["s07.c"] - 0.9, C["s07.c"])
        E.foco(c, t, C["s07.b"] + 0.4, 0.4, lambda a: mista(c, [("4", ENT), ("  →  ", TINTA2), ("15", SAI)], 760, 860, 72, a, "center"))
        E.foco(c, t, C["s07.c"] + 0.4, 0.4, lambda a: mista(c, [("10", ENT), ("  →  ", TINTA2), ("30", SAI)], 1160, 860, 72, a, "center"))
    E.saida(c, t, C["s07.d"] - 0.1, s07)
    if t < C["s07.d"]:
        return

    def regra():
        E.frase(c, t, C["s07.d"], [("cada", "i", 110), ("entrada", "g", 110, ENT)], W / 2, 330, "center")
        E.frase(c, t, C["s07.d"] + 0.7, [("dá", "i", 110), ("exatamente", "i", 110), ("uma", "g", 110), ("saída", "g", 110)], W / 2, 470, "center")
        t1 = C["s07.d"] + 2.6
        E.frase(c, t, t1, [("nenhuma", "i", 70), ("entrada", "g", 66, ENT), ("sem", "i", 70), ("saída", "g", 66)], 300, 690)
        E.frase(c, t, C["s07.e"], [("nenhuma", "i", 70), ("entrada", "g", 66, ENT), ("com", "i", 70), ("duas", "g", 66, ERRADO)], 300, 860)
        # desenhinhos: entrada sem flecha; entrada com duas flechas
        E.foco(c, t, t1 + 0.4, 0.4, lambda a: (bolinha(c, 1260, 668, "x", ENT, a, 44), E.selo(c, 1440, 668, 36, False, a)))
        if t >= C["s07.e"] + 0.4:
            a = ep(t, C["s07.e"] + 0.4, 0.4)
            bolinha(c, 1260, 840, "x", ENT, a, 44)
            M.arrow(c, 1310, 830, 1460, 790, ERRADO, a, 5, 18, a)
            M.arrow(c, 1310, 850, 1460, 890, ERRADO, a, 5, 18, a)
            E.selo(c, 1540, 840, 36, False, a)
    E.saida(c, t, C["s08"] - 0.1, regra)
    if t < C["s08"]:
        return
    y = 430
    E.foco(c, t, C["s08"], 0.5, lambda a: mista(c, FORM, W / 2, y, 170, a, "center"))
    xs = mista(c, FORM, W / 2, y, 170, 0, "center")
    wP, wd = E.larg("P", "g", 170), E.larg("d", "g", 170)
    pa = ep(t, C["s08.a"], 0.5)
    E.caixa_pontilhada(c, xs[0] - wP / 2 - 24, y - 150, wP + 48, 190, pa, SAI, pa)
    E.frase(c, t, C["s08.a"] + 0.3, [("sozinha:", "i", 58), ("saída", "g", 58)], xs[0], 590, "center", 0.12)
    pb = ep(t, C["s08.b"], 0.5)
    E.caixa_pontilhada(c, xs[5] - wd / 2 - 24, y - 150, wd + 48, 190, pb, ENT, pb)
    E.frase(c, t, C["s08.b"] + 0.3, [("na", "i", 58, ENT), ("conta:", "i", 58, ENT), ("entrada", "g", 58, ENT)], xs[5], 590, "center", 0.12)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "é pista, não é regra", W / 2, 720, 50, "b", fundo=TINTA2, a=a))
    E.frase(c, t, C["s08.d"], [("quem", "i", 96), ("depende", "g", 92, COR), ("de", "i", 96), ("quem?", "i", 96)], W / 2, 930, "center")


# ---------------- tabela ----------------
def b_tabela(c, t, C, b):
    E.frase(c, t, C["s09.a"], [("numa", "i", 84), ("tabela", "g", 80, COR)], W / 2, 170, "center")
    x1, x2, y = 260, 1100, 330
    caixas1 = tabela2(c, t, C["s09.a"], [(1, 3), (2, 5), (3, 7), (4, 9)], x1, y)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "é função", x1 + 240, 820, 56, "g", fundo=CERTO, a=a))
    for i in range(4):
        q = ep(t, C["s09.b"] + 0.15 * i, 0.3) * (1 - ep(t, C["s09.c"], 0.4))
        if q > 0:
            E.selo(c, x1 + 540, caixas1[i][1] + caixas1[i][3] / 2, 26, True, q)
    caixas2 = tabela2(c, t, C["s09.c"] - 0.4, [(1, 2), (2, 4), (2, 6), (3, 8)], x2, y)
    q = ep(t, C["s09.c"], 0.4)
    for i in (1, 2):
        faixa(c, *caixas2[i], ERRADO, q)
    for i in (1, 2):
        xx, yy, ww, hh = caixas2[i]
        anel(c, t, C["s09.d"] + 0.4 * (i - 1), x2 + 360, yy + hh / 2, 46)
    E.frase(c, t, C["s09.e"], [("a", "i", 64), ("entrada", "i", 64), ("2", "g", 66, ENT), ("deu", "i", 64), ("duas", "g", 64, ERRADO), ("saídas", "i", 64)], W / 2, 980, "center")
    E.foco(c, t, C["s09.f"], 0.5, lambda a: E.pilula(c, "não é função", x2 + 240, 820, 56, "g", fundo=ERRADO, a=a))


# ---------------- flechas ----------------
D1 = [(1, 2), (2, 4), (3, 6)]


def b_flechas(c, t, C, b):
    def d1():
        E.frase(c, t, C["s10.a"], [("diagrama", "i", 84), ("de", "i", 84), ("flechas", "g", 80, COR)], W / 2, 150, "center")
        pa, pb = ovais(c, t, C["s10.b"], 700, 1220, 570, [1, 2, 3], [2, 4, 6, 8], ta=C["s10.d"], tb=C["s10.e"], tB=C["s10.c"])
        q = pulso(t, C["s11.a"], 2.0)
        if q > 0:
            c.drawOval(skia.Rect.MakeXYWH(700 - 150, 570 - 255, 300, 510), M.paint(ENT, 0.12 * q))
        for i, (e, s) in enumerate(D1):
            flecha(c, t, C["s11.b"] + 1.5 * i, pa[e], pb[s])
        E.foco(c, t, C["s11.c"], 0.5, lambda a: E.pilula(c, "é função", W / 2, 960, 56, "g", fundo=CERTO, a=a))
        anel(c, t, C["s11.d"], *pb[8], 50, TINTA2)
        E.frase(c, t, C["s11.d"] + 0.3, [("em", "i", 50), ("B,", "g", 50), ("pode", "i", 50), ("sobrar", "g", 50)], 1410, 790)
    E.saida(c, t, C["s12"] - 0.1, d1)
    if t < C["s12"]:
        return
    for cx, fl, t0, tn, ruim in ((520, [(1, 2), (2, 4), (2, 6), (3, 8)], C["s12.a"], C["s12.b"], 2),
                                 (1400, [(1, 2), (2, 4)], C["s12.c"], C["s12.d"], 3)):
        pa, pb = ovais(c, t, t0 - 0.6, cx - 200, cx + 200, 520, [1, 2, 3], [2, 4, 6, 8], dy=100, rw=110, size=54, nomes=("A", "B"), sub=None)
        for i, (e, s) in enumerate(fl):
            flecha(c, t, t0 + 0.15 * i, pa[e], pb[s], ERRADO if e == ruim else None, folga=(40, 48))
        anel(c, t, t0 + 0.7, *pa[ruim], 42)
        E.foco(c, t, tn, 0.5, lambda a, cx=cx: E.pilula(c, "não é função", cx, 900, 54, "g", fundo=ERRADO, a=a))
        E.foco(c, t, t0 + 0.8, 0.4, lambda a, cx=cx, ruim=ruim: centro(c, "2 flechas saem do 2" if ruim == 2 else "o 3 fica sem flecha",
                                                                          cx, 800, 50, "i", ERRADO, a))


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13.a"], [("duas", "i", 72), ("flechas", "i", 72), ("chegando", "g", 68, ERRADO), ("no", "i", 72), ("mesmo?", "i", 72)],
            W / 2, 170, "center")
    pa, pb = ovais(c, t, C["s13.b"], 960, 1460, 560, ["Ana", "Bruno"], ["abril", "maio", "junho"], ta=C["s13.c"], tb=C["s13.b"] + 0.6,
                   size=56, dy=130, rw=170, sub=("pessoas", "mês do aniversário"), nomes=(None, None))
    flecha(c, t, C["s13.d"], pa["Ana"], pb["maio"], folga=(84, 90))
    flecha(c, t, C["s13.d"] + 0.4, pa["Bruno"], pb["maio"], folga=(90, 90))
    if t >= C["s13.d"] + 0.8:
        anel(c, t, C["s13.d"] + 0.8, *pb["maio"], 70, TINTA2)
    E.frase(c, t, C["s13.e"], [("cada", "i", 56), ("pessoa,", "i", 56, ENT), ("um", "g", 56), ("mês", "i", 56)], XE, 480)
    E.foco(c, t, C["s13.f"], 0.5, lambda a: E.pilula(c, "é função", XE + 160, 610, 56, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s13.g"], [("o", "i", 72), ("problema", "i", 72), ("é", "i", 72), ("SAIR", "g", 72, ERRADO), ("2", "g", 72, ERRADO),
                               ("flechas,", "i", 72), ("não", "i", 72), ("chegar", "g", 72)], W / 2, 980, "center")


# ---------------- atalho (palco escuro) ----------------
def mini_tabela(c, x, y, linhas, a, ruins=(), cor_ruim=ERRADO, wc=130, hl=64, size=46):
    for i in ruins:
        M.rrect(c, x - 8, y + 6 + hl * i, 2 * wc + 16, hl, 12, cor_ruim, 0.3 * a)
    M.line(c, x + wc, y - 6, x + wc, y + hl * len(linhas) + 8, BR, a, 3)
    centro(c, "entrada", x + wc / 2, y - 20, 34, "b", CLARO, a)
    centro(c, "saída", x + wc * 1.5, y - 20, 34, "b", BR, a)
    M.line(c, x, y, x + 2 * wc, y, BR, a, 3)
    for i, (e, s) in enumerate(linhas):
        yy = y + 6 + hl * i + hl / 2 + size * 0.36
        centro(c, E._num(e), x + wc / 2, yy, size, "g", CLARO, a)
        centro(c, E._num(s), x + wc * 1.5, yy, size, "g", BR, a)


def b_atalho(c, t, C, b):
    palco(c, t)

    def s14():
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 72, CLARO), W / 2, 150, "center")
        E.frase(c, t, C["s14.a"], [("olhe", "i", 96, CLARO), ("só", "i", 96, CLARO), ("as", "i", 96, CLARO), ("entradas", "g", 96, BR)], W / 2, 290, "center")
        E.frase(c, t, C["s14.b"], [("tabela:", "g", 64, BR)], 260, 470)
        E.frase(c, t, C["s14.b"] + 0.5, ps("entrada repetida com saídas diferentes?", "i", 60, CLARO), 260, 550, passo=0.1)
        E.frase(c, t, C["s14.c"], [("diagrama:", "g", 64, BR)], 260, 690)
        E.frase(c, t, C["s14.c"] + 0.5, ps("quantas flechas saem de cada elemento de A?", "i", 60, CLARO), 260, 770, passo=0.1)
        E.frase(c, t, C["s14.d"], [("nenhuma", "i", 64, CLARO), ("com", "i", 64, CLARO), ("duas,", "g", 64, BR), ("nenhuma", "i", 64, CLARO),
                                   ("esquecida:", "g", 64, BR), ("função", "g", 64, CERTO)], W / 2, 950, "center", 0.14)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], ps("só duas coisas derrubam", "i", 72, CLARO), W / 2, 160, "center")
    # 1) uma entrada, duas respostas
    a = ep(t, C["s15.a"], 0.5)
    if a > 0:
        bolinha(c, 380, 340, "x", COR, a, 46)
        M.arrow(c, 434, 326, 600, 280, ERRADO, a, 6, 20, a)
        M.arrow(c, 434, 354, 600, 400, ERRADO, a, 6, 20, a)
        centro(c, "duas respostas", 500, 490, 52, "i", BR, a)
    a = ep(t, C["s15.b"], 0.5)
    if a > 0:
        bolinha(c, 1140, 340, "x", COR, a, 46)
        E.selo(c, 1320, 340, 40, False, a)
        centro(c, "nenhuma resposta", 1230, 490, 52, "i", BR, a)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: mini_tabela(c, 380, 640, [(1, 3), (2, 4), (2, 4)], a, (1, 2), "#FFFFFF"))
    E.frase(c, t, C["s15.c"] + 0.5, ps("linha inteira repetida:", "i", 60, CLARO), 840, 720)
    E.frase(c, t, C["s15.c"] + 1.6, ps("a mesma informação", "i", 60, CLARO), 840, 800)
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.pilula(c, "ainda é função", 1090, 910, 56, "g", fundo=CERTO, a=a))


# ---------------- questão ----------------
FC = [("C", SAI), (" = ", TINTA), ("40 + 90", TINTA), ("m", ENT)]
TQ = [(-1, 2), (0, 1), (1, 2), (-1, 3)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s16.a"], [("academia:", "g", 60), ("R$", "i", 60), ("40", "g", 60), ("de", "i", 60), ("matrícula", "i", 60)], XE, 300)
    E.frase(c, t, C["s16.a"] + 1.4, [("+", "g", 60), ("R$", "i", 60), ("90", "g", 60), ("por", "i", 60), ("mês", "i", 60)], XE, 380)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: mista(c, FC, XE, 530, 110, a))
    E.frase(c, t, C["s16.c"], [("entrada?", "g", 60, ENT), ("saída?", "g", 60)], XE, 650)
    E.frase(c, t, C["s16.d"], [("3", "g", 60, ENT), ("meses:", "i", 60), ("quanto?", "g", 60)], XE, 740)
    tabela2(c, t, C["s16.e"], TQ, 1200, 250, ("x", "y"))
    E.foco(c, t, C["s16.e"] + 0.3, 0.4, lambda a: centro(c, "é função?", 1440, 710, 64, "g", COR, a))
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1440, cy=850, r=56)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.foco(c, t, C["s18"], 0.5, lambda a: mista(c, FC, W / 2, 300, 150, a, "center"))
        xs = mista(c, FC, W / 2, 300, 150, 0, "center")
        E.foco(c, t, C["s18.a"], 0.5, lambda a: centro(c, "entrada: meses", xs[3], 420, 56, "b", ENT, a))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: centro(c, "saída: custo", xs[0], 420, 56, "b", SAI, a))
        E.foco(c, t, C["s18.c"], 0.5, lambda a: mista(c, [("90 × ", TINTA), ("3", ENT), (" = 270", TINTA)], W / 2, 600, 96, a, "center"))
        E.foco(c, t, C["s18.d"], 0.5, lambda a: mista(c, [("40 + 270 = ", TINTA), ("310", SAI)], W / 2, 740, 96, a, "center"))
        E.foco(c, t, C["s18.d"] + 0.6, 0.5, lambda a: E.pilula(c, "R$ 310", W / 2, 880, 72, "g", fundo=CERTO, a=a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    cx = tabela2(c, t, C["s19"], TQ, 1100, 280, ("x", "y"))
    q = ep(t, C["s19.a"], 0.4)
    for i in (0, 3):
        faixa(c, *cx[i], ERRADO, q)
    for i in (0, 3):
        anel(c, t, C["s19.b"] + 0.4 * (i == 3), 1100 + 360, cx[i][1] + cx[i][3] / 2, 44)
    q = ep(t, C["s19.d"], 0.4)
    for i in (0, 2):
        xx, yy, ww, hh = cx[i]
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1100 + 250, yy + 6, 220, hh - 12), 14, 14), M.paint(TINTA2, q, stroke=5))
    E.frase(c, t, C["s19.a"], [("−1", "g", 76, ENT), ("aparece", "i", 70), ("2", "g", 76), ("vezes", "i", 70)], XE, 340)
    E.frase(c, t, C["s19.b"], [("saídas", "i", 70), ("2", "g", 76), ("e", "i", 70), ("3", "g", 76)], XE, 450)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "não é função", XE + 230, 580, 56, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s19.d"], [("saída", "i", 64), ("2", "g", 70), ("repetida:", "i", 64)], XE, 760)
    E.frase(c, t, C["s19.e"], [("sozinha,", "i", 64), ("não", "g", 64), ("atrapalha", "g", 64)], XE, 850)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("entrada:", "g", 84, ENT), ("você", "i", 84), ("escolhe", "i", 84)]),
                 ("s20.a", [("saída:", "g", 84), ("depende", "i", 84), ("dela", "i", 84)]),
                 ("s20.b", [("função:", "g", 84, COR), ("cada", "i", 84), ("entrada,", "i", 84), ("uma", "g", 84), ("saída", "i", 84)]))
        for i, (k, partes) in enumerate(itens):
            y = 420 + i * 190
            t0 = C[k] + (2.4 if i == 1 else 0)
            E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                       E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, t0 + 0.1, partes, 400, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.foco(c, t, C["s21.a"], 0.5, lambda a: mista(c, [("f(", COR), ("x", COR), (")", COR)], XE, 480, 170, a))
    E.frase(c, t, C["s21.b"], [("calcular", "g", 72), ("a", "i", 76), ("saída", "i", 76)], XE, 620)
    E.frase(c, t, C["s21.c"], [("e", "i", 76), ("o", "i", 76), ("caminho", "g", 72, COR), ("de", "i", 76), ("volta", "g", 72, COR)], XE, 730)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, formula=b_formula, maquina=b_maquina, tabela=b_tabela, flechas=b_flechas,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
