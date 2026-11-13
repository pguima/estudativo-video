"""Visual — Estudativo · QUI-ELE-002: oxirredução, quem perde e quem ganha elétrons.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha Eletroquímica (cabeçalho da QUI-ELE-001): Nox em pílula sobre o
símbolo; oxidação em âmbar (OXI), seta para cima; redução em azul (RED, o do elétron), seta para baixo; agente = pílula com
contorno. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-002_oxirreducao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("troca", "nomes", "forno", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON
AZUL_CU = "#4F8FD8"

EQ1 = "Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)"
EQ2 = "Fe2O3 + 3 CO -> 2 Fe + 3 CO2"
EQ3 = "Mg + 2 HCl -> MgCl2 + H2"
# contas da aula
assert Q.lados("Zn + Cu^2+ -> Zn^2+ + Cu")[0] == Q.lados("Zn + Cu^2+ -> Zn^2+ + Cu")[1]
assert Q.lados(EQ2)[0] == Q.lados(EQ2)[1] and Q.lados(EQ3)[0] == Q.lados(EQ3)[1]
assert 2 * 3 + 3 * (-2) == 0 and 2 + (-2) == 0 and 4 + 2 * (-2) == 0   # Fe +3; C +2 no CO; C +4 no CO2
assert 2 + 2 * (-1) == 0                                              # Mg +2 no MgCl2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """palavras de uma frase; sinais (=, −, +, ×, →) vão na grotesca, porque a serifada itálica não tem esses glifos"""
    return [((w, "g", size * 0.9, cor) if w in ("=", "−", "+", "×", "→", "≠") else (w, "b", size * 0.9, cor) if ("-" in w and est == "i") else (w, est, size, cor)) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def tag(c, t, t0, g, nox, size, fundo=TINTA, dy=0):
    """Nox em pílula sobre um grupo da fórmula"""
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, nox, g["cx"], g["topo"] - size * 1.0 + dy, size, "g", fundo=fundo, a=a))


def arco(c, t, t0, x0, x1, y, cor, rotulo, cima=True, h=90, size=40):
    """arco com seta de x0 a x1 (acima ou abaixo da linha y) e o rótulo numa pílula: a troca do Nox"""
    p = ease_io(prog(t, t0, 0.7))
    if p <= 0:
        return
    s = -1 if cima else 1
    pth = skia.Path()
    pth.moveTo(x0, y); pth.cubicTo(x0, y + s * h, x1, y + s * h, x1, y)
    me = skia.PathMeasure(pth, False)
    L = me.getLength()
    parte = skia.Path(); me.getSegment(0, L * p, parte, True)
    c.drawPath(parte, M.paint(cor, 1, stroke=6))
    if p > 0.95:
        M.line(c, x1, y, x1 - 14, y + s * 26, cor, 1, 6)
        M.line(c, x1, y, x1 + 14, y + s * 26, cor, 1, 6)
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.pilula(c, rotulo, (x0 + x1) / 2, y + s * (h * 0.75 + size * 0.2), size, "g", fundo=cor, a=a))


def agente(c, t, t0, cx, cy, txt, cor, size=40):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, txt, cx, cy, size, "g", fundo=None, cor=cor, a=a, contorno=True))
    E.foco(c, t, t0, 0.4, lambda a: centro(c, txt, cx, cy + size * 0.36, size, "g", cor, a))


def eletron(c, x, y, r=14, a=1.0):
    E.bola(c, x, y, r, Q.ELETRON, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.16))


def voa(c, t, t0, A, B, d=1.0, alto=120, r=16):
    if t < t0 or t > t0 + d + 0.3:
        return
    p = ease_io(prog(t, t0, d))
    mx, my = (A[0] + B[0]) / 2, min(A[1], B[1]) - alto
    x = (1 - p) ** 2 * A[0] + 2 * (1 - p) * p * mx + p ** 2 * B[0]
    y = (1 - p) ** 2 * A[1] + 2 * (1 - p) * p * my + p ** 2 * B[1]
    eletron(c, x, y, r, 1 - ep(t, t0 + d, 0.3))


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def placa(c, x, y, w, h, cor, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 8, cor, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 8, 8), M.paint(M.mix(cor, "#000000", 0.35), a, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def s01():
        cx, yb = 1380, 900
        cor_sol = lambda tt: Q.muda_cor(tt, C["s01.c"], AZUL_CU, "#D9E6EE", 2.5)
        Q.bequer(c, t, C["s01.a"] - 0.3, cx, yb, 420, 460, 0.72, cor_sol, graduacao=False)
        cobre = ease_io(prog(t, C["s01.b"], 1.6))
        E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: placa(c, cx - 40, 360, 80, 470, M.mix("#8C96A8", "#B5532A", cobre), a))
        E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: centro(c, "zinco", cx, 330, 50, "g", TINTA, a))
        E.frase(c, t, C["s01.a"], ps("uma placa de", "i", 70) + [("zinco", "g", 66)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.2, ps("no sulfato de cobre,", "i", 70) + [("azul", "g", 66, AZUL_CU)], XE, 360, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("a placa fica", "i", 64) + [("coberta de cobre", "g", 60, "#B5532A")], XE, 540, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("o azul vai", "i", 64) + [("sumindo", "g", 60)], XE, 640, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("de onde veio o", "i", 76) + [("cobre?", "g", 70, COR)], XE, 860, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, s01)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 240, passo=0.14)
    lista(c, t, [(C["s02.b"], [("quem", "i", 70), ("se oxida,", "g", 64, OXI), ("quem", "i", 70), ("se reduz", "g", 64, RED)]),
                 (C["s02.c"], [("os", "i", 70), ("agentes", "g", 64, COR)]),
                 (C["s02.d"], [("o", "i", 70), ("alto-forno", "g", 64)]),
                 (C["s02.e"], [("atalho", "g", 64, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 400, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 190, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: (E.bola(c, XE + 40, 314, 40, a=a), centro(c, "1", XE + 40, 331, 48, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.a"] + 0.1, ps("calcular o", "i", 64) + [("Nox", "g", 60, COR)], XE + 120, 336, passo=0.1)
    for i, s in enumerate(("simples = 0", "íon = carga", "soma = 0")):
        pilula_em(c, t, C["s03.a"] + 0.8 + 0.7 * i, s, XE + 300 + 420 * i, 450, 50, TINTA)
    E.foco(c, t, C["s03.b"], 0.5, lambda a: (E.bola(c, XE + 40, 614, 40, a=a), centro(c, "2", XE + 40, 631, 48, "g", E.SOBRE, a)))
    E.frase(c, t, C["s03.b"] + 0.1, ps("a", "i", 64) + [("fila de reatividade", "g", 60, COR)], XE + 120, 636, passo=0.1)
    fila = ("K", "Mg", "Zn", "Fe", "H", "Cu", "Ag")
    x0, dx, y = XE + 180, 230, 820
    p = ep(t, C["s03.b"] + 0.5, 0.8)
    if p > 0:
        M.arrow(c, x0 - 90, y + 90, x0 + dx * 6 + 90, y + 90, TINTA2, p, 5, 22, p)
        E.foco(c, t, C["s03.b"] + 1.0, 0.4, lambda a: E.escreve(c, "mais reativo", x0 - 90, y + 150, 42, "i", TINTA2, a))
    for i, el in enumerate(fila):
        Q.atomo_em(c, t, C["s03.b"] + 0.5 + 0.1 * i, x0 + dx * i, y, 52, el)
    if t >= C["s03.c"]:
        for el, cor in (("Zn", E.COR), ("Cu", TINTA)):
            i = fila.index(el)
            q = ep(t, C["s03.c"], 0.4)
            c.drawCircle(x0 + dx * i, y, 74, M.paint(cor, q, stroke=6))
        E.foco(c, t, C["s03.c"] + 0.5, 0.4, lambda a: E.pilula(c, "zinco antes do cobre", x0 + dx * 3.5, y - 110, 44, "g", fundo=E.COR, a=a))


# ---------------- a troca: Zn + Cu2+ ----------------
EY, ES = 470, 112


def b_troca(c, t, C, b):
    G = Q.grupos(EQ1, W / 2, EY, ES, "center")
    cores = {1: RED, 3: RED} if C["s04.c"] <= t < C["s05"] else None
    Q.equacao(c, t, C["s04.a"], EQ1, W / 2, EY, ES, tl=[C["s04.a"], C["s04.a"] + 0.4, C["s04.a"] + 0.7, C["s04.b"], C["s04.b"] + 0.4, C["s04.b"] + 0.7], cores=cores)
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04"], ps("escreva o que aconteceu", "i", 64, TINTA2), XE, 200, passo=0.1)
            pilula_em(c, t, C["s04.c"], "estava dissolvido, como íon", G[1]["cx"], EY + 120, 42, TINTA)
            pilula_em(c, t, C["s04.d"], "virou metal", G[3]["cx"], EY + 120, 42, "#B5532A")
            E.foco(c, t, C["s04.d"] + 1.0, 0.4, lambda a: Q.formula(c, "SO4^2-", W / 2 - 160, 860, 90, TINTA2, a))
            E.frase(c, t, C["s04.d"] + 1.2, ps("o sulfato só assiste", "i", 60, TINTA2), W / 2 + 40, 860, passo=0.1)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    tag(c, t, C["s05.a"], G[0], "0", 46)
    tag(c, t, C["s05.a"] + 0.8, G[2], "+2", 46)
    arco(c, t, C["s05.b"], G[0]["cx"], G[2]["cx"], G[0]["topo"] - 110, OXI, "perde 2 e⁻", True, 100)
    tag(c, t, C["s05.c"], G[1], "+2", 46)
    tag(c, t, C["s05.c"] + 0.8, G[3], "0", 46)
    arco(c, t, C["s05.d"], G[1]["cx"], G[3]["cx"], G[1]["base"] + 50, RED, "ganha 2 e⁻", False, 110)
    if t >= C["s05.e"]:
        for k in range(2):
            voa(c, t, C["s05.e"] + 0.5 * k, (G[0]["cx"], G[0]["topo"] + 40), (G[1]["cx"], G[1]["topo"] + 40), 1.2, 200, 18)
        E.frase(c, t, C["s05.e"] + 0.4, ps("os elétrons do zinco", "i", 62) + [("foram para o cobre", "g", 58, RED)], W / 2, 930, "center", 0.1)


# ---------------- nomes ----------------
def coluna(c, t, t0, t1, x, nome, cor, l1, seta):
    E.frase(c, t, t0, [(nome, "g", 92, cor)], x, 330, "center")
    E.frase(c, t, t0 + 0.4, [(l1, "i", 66)], x, 450, "center")
    E.frase(c, t, t1, [("Nox", "g", 62), (seta, "g", 70, cor)], x, 580, "center")
    if t >= t1:
        p = ease_io(prog(t, t1 + 0.2, 0.6))
        y0, y1 = (760, 640) if seta == "sobe" else (640, 760)
        M.arrow(c, x, y0, x, lerp(y0, y1, p), cor, ep(t, t1 + 0.2, 0.3), 10, 30, p)


def b_nomes(c, t, C, b):
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06"], ps("cada metade da troca tem nome", "i", 60, TINTA2), W / 2, 180, "center", 0.1)
            coluna(c, t, C["s06.a"], C["s06.b"], 600, "oxidação", OXI, "perder elétrons", "sobe")
            coluna(c, t, C["s06.c"], C["s06.d"], 1320, "redução", RED, "ganhar elétrons", "desce")
            E.frase(c, t, C["s06.e"], ps("uma não acontece sem a outra:", "i", 58), W / 2, 880, "center", 0.1)
            E.frase(c, t, C["s06.f"], [("oxirredução", "g", 84, COR)], W / 2, 1000, "center")
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    G = Q.grupos(EQ1, W / 2, 360, 100, "center")
    Q.formula_em(c, t, C["s07"], EQ1, W / 2, 360, 100, align="center")
    E.frase(c, t, C["s07"] + 0.2, ps("o agente é quem provoca", "i", 64, TINTA2), W / 2, 170, "center", 0.1)
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.escreve(c, "provocou a redução do cobre", G[0]["cx"] - 120, 520, 44, "i", TINTA2, a))
    agente(c, t, C["s07.b"], G[0]["cx"] + 60, 610, "agente redutor", OXI, 46)
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.escreve(c, "provocou a oxidação do zinco", G[1]["cx"] - 60, 740, 44, "i", TINTA2, a))
    agente(c, t, C["s07.d"], G[1]["cx"] + 180, 830, "agente oxidante", RED, 46)
    E.frase(c, t, C["s07.e"], [("o redutor", "g", 58, OXI)] + ps("se oxida;", "i", 62) + [("o oxidante", "g", 58, RED)] + ps("se reduz", "i", 62), W / 2, 1000, "center", 0.1)


# ---------------- alto-forno ----------------
def forno(c, cx, yb, w, h, a=1.0, brilho=0.0):
    """alto-forno: torre escura que estreita no alto, com a boca brilhando"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - w * 0.32, yb - h); p.lineTo(cx + w * 0.32, yb - h); p.lineTo(cx + w * 0.5, yb - h * 0.35)
    p.lineTo(cx + w * 0.42, yb); p.lineTo(cx - w * 0.42, yb); p.lineTo(cx - w * 0.5, yb - h * 0.35); p.close()
    c.drawPath(p, M.paint("#3A3B42", a))
    g = skia.Paint(AntiAlias=True)
    g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, yb - h * 0.25), w * 0.5, [M.hexc("#FF8A1F", a * (0.6 + 0.4 * brilho)), M.hexc("#FF8A1F", 0)], [0, 1]))
    c.drawCircle(cx, yb - h * 0.25, w * 0.5, g)
    M.rrect(c, cx - w * 0.2, yb - h * 0.18, w * 0.4, h * 0.1, 10, "#FFB347", a)
    centro(c, "ferro", cx, yb - h * 0.1, 30, "g", "#3A3B42", a)


FY2, FS2 = 470, 104


def b_forno(c, t, C, b):
    G = Q.grupos(EQ2, W / 2, FY2, FS2, "center")
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], ps("o", "i", 70) + [("alto-forno", "g", 66, COR)], XE, 200, passo=0.12)
            E.foco(c, t, C["s08.a"] + 0.4, 0.6, lambda a: forno(c, 1620, 1000, 360, 520, a, 0.5 + 0.5 * math.sin(t * 2)))
            eq = "Fe2O3 + CO -> Fe + CO2"
            ex, ey, es = 680, 560, 100
            Q.equacao(c, t, C["s08.b"], eq, ex, ey, es, tl=[C["s08.b"], C["s08.c"] - 0.2, C["s08.c"], C["s08.d"] - 0.2, C["s08.d"], C["s08.d"] + 0.2, C["s08.d"] + 0.4])
            cs = Q.centros(eq, ex, ey, es)
            for k, (txt, tk) in enumerate((("minério", C["s08.b"]), ("monóxido de carbono", C["s08.c"]), ("ferro", C["s08.d"]), ("gás carbônico", C["s08.d"] + 0.4))):
                E.foco(c, t, tk + 0.3, 0.4, lambda a, k=k, txt=txt: centro(c, txt, cs[k], ey + (90 if k % 2 == 0 else 160), 44, "i", TINTA2, a))
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    Q.formula_em(c, t, C["s09"], EQ2, W / 2, FY2, FS2, align="center")
    if t < C["s11"]:
        def nox():
            tag(c, t, C["s09.b"], G[0], "+3", 42)
            tag(c, t, C["s09.c"], G[6], "0", 42)
            arco(c, t, C["s09.d"], G[0]["cx"], G[6]["cx"], G[0]["topo"] - 100, RED, "o ferro se reduz", True, 120)
            E.foco(c, t, C["s09.a"], 0.4, lambda a: E.formula(c, "2x + 3 · (−2) = 0", 300, 900, 56, "g", TINTA2, a))
            E.foco(c, t, C["s09.b"], 0.4, lambda a: E.formula(c, "x = +3", 300, 990, 56, "g", TINTA, a))
            tag(c, t, C["s10.a"], G[3], "+2", 42)
            tag(c, t, C["s10.b"], G[8], "+4", 42)
            arco(c, t, C["s10.c"], G[3]["cx"], G[8]["cx"], G[3]["base"] + 40, OXI, "o carbono se oxida", False, 130)
            E.foco(c, t, C["s10.d"], 0.4, lambda a: E.pilula(c, "O: −2 o tempo todo", 1400, 960, 48, "g", fundo=TINTA2, a=a))
        E.saida(c, t, C["s11"] - 0.1, nox)
        return
    agente(c, t, C["s11.b"], G[0]["cx"] + 20, FY2 + 140, "agente oxidante", RED, 44)
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.escreve(c, "o ferro do minério se reduziu", 200, 290, 48, "i", TINTA2, a))
    agente(c, t, C["s11.d"], G[3]["cx"] + 40, FY2 + 260, "agente redutor", OXI, 44)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.escreve(c, "o monóxido se oxidou", G[3]["cx"] - 80, FY2 + 360, 48, "i", TINTA2, a))
    E.frase(c, t, C["s11.e"], ps("o agente é a", "i", 64) + [("substância inteira", "g", 60, COR)] + ps("não só o átomo", "i", 64), W / 2, 1000, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("o oxidante é quem se oxida?", "i", 64), XE + 450, 190, passo=0.1)
    G = Q.grupos(EQ1, W / 2, 430, 100, "center")
    Q.formula_em(c, t, C["s12.a"] + 0.6, EQ1, W / 2, 430, 100, align="center")

    def errado():
        E.foco(c, t, C["s12.b"], 0.4, lambda a: (E.pilula(c, "agente oxidante?", G[0]["cx"] + 60, 580, 46, "g", fundo=ERRADO, a=a)))
        if t >= C["s12.b"] + 1.0:
            E.risco(c, G[0]["cx"] - 160, 610, G[0]["cx"] + 280, 550, t, C["s12.b"] + 1.0, largura=10)
        E.foco(c, t, C["s12.b"] + 0.6, 0.4, lambda a: E.escreve(c, "só pelo som da palavra", G[0]["cx"] - 100, 680, 46, "i", ERRADO, a))
    E.saida(c, t, C["s13.a"] - 0.1, errado)
    if t < C["s13.a"]:
        return
    E.frase(c, t, C["s13.a"], ps("o nome conta o que o agente faz", "i", 62) + [("no outro", "g", 58, COR)], W / 2, 620, "center", 0.1)
    E.frase(c, t, C["s13.b"], ps("o zinco", "i", 64) + [("se oxidou", "g", 60, OXI)], W / 2 - 320, 780, "center", 0.1)
    E.frase(c, t, C["s13.c"], ps("e", "i", 64) + [("reduziu o cobre", "g", 60, RED)], W / 2 + 320, 780, "center", 0.1)
    agente(c, t, C["s13.c"] + 0.8, W / 2, 920, "agente redutor", OXI, 54)
    E.foco(c, t, C["s13.c"] + 1.0, 0.4, lambda a: E.selo(c, W / 2 + 340, 920, 44, True, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
            for k, (tk, seta, txt1, txt2, cor, y) in enumerate(((C["s14.a"], "sobe", "se oxidou", "é o redutor", OXI, 400),
                                                                 (C["s14.b"], "desce", "se reduziu", "é o oxidante", RED, 620))):
                E.frase(c, t, tk, [("Nox", "g", 76, BR), (seta, "g", 76, cor)], XE + 120, y, passo=0.12)
                pp = ease_io(prog(t, tk + 0.2, 0.5))
                ya, yb_ = (y + 20, y - 80) if seta == "sobe" else (y - 80, y + 20)
                if pp > 0:
                    M.arrow(c, XE + 40, ya, XE + 40, lerp(ya, yb_, pp), cor, 1, 9, 26, pp)
                E.frase(c, t, tk + 0.8, ps("→", "g", 70, CLARO) + ps(txt1, "i", 72, CLARO), XE + 560, y, passo=0.1)
                E.frase(c, t, tk + 1.4, [(txt2, "g", 68, cor)], XE + 1080, y)
            E.frase(c, t, C["s14.c"], ps("os nomes sempre", "i", 72, CLARO) + [("se cruzam", "g", 68, BR)], W / 2, 900, "center", 0.12)
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15"], ps("para achar rápido quem muda:", "i", 64, CLARO), W / 2, 170, "center", 0.1)
    E.frase(c, t, C["s15.a"], ps("procure o elemento", "i", 64, CLARO) + [("sozinho", "g", 60, BR)] + ps("de um lado", "i", 64, CLARO), W / 2, 280, "center", 0.1)
    G = Q.grupos(EQ1, W / 2, 520, 110, "center")
    Q.formula_em(c, t, C["s15.a"] + 0.6, EQ1, W / 2, 520, 110, align="center", escuro=True)
    for i, (k, v) in enumerate(((0, "0"), (3, "0"))):
        if t >= C["s15.b"]:
            q = ep(t, C["s15.b"] + 0.3 * i, 0.4)
            g = G[k]
            E.caixa_pontilhada(c, g["x0"] - 14, g["topo"] - 14, g["x1"] - g["x0"] + 28, g["base"] - g["topo"] + 28, q, E.CLARO, prog_=q)
            E.foco(c, t, C["s15.b"] + 0.3 * i, 0.4, lambda a, g=g, v=v: E.pilula(c, v, g["cx"], g["topo"] - 60, 42, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s15.b"], ps("sozinho e sem carga:", "i", 58, CLARO) + [("zero", "g", 56, BR)], W / 2 - 300, 720, "center", 0.1)
    E.frase(c, t, C["s15.c"], ps("combinado:", "i", 58, CLARO) + [("quase nunca", "g", 56, BR)], W / 2 + 420, 720, "center", 0.1)
    E.frase(c, t, C["s15.d"], ps("no alto-forno, o carbono está combinado dos dois lados:", "i", 52, CLARO), W / 2, 880, "center", 0.08)
    pilula_em(c, t, C["s15.d"] + 2.5, "aí, não compensa: calcule", W / 2, 980, 46, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16.a"], ps("magnésio no ácido clorídrico solta", "i", 58, TINTA2) + [("gás hidrogênio", "g", 54)], XE, 290, passo=0.08)
    Q.formula_em(c, t, C["s16.b"], EQ3, XE, 480, 120)
    E.frase(c, t, C["s16.c"], [("1", "g", 56, COR)] + ps("quem se oxida? quem se reduz?", "i", 60), XE, 680, passo=0.08)
    E.frase(c, t, C["s16.d"], [("2", "g", 56, COR)] + ps("quais são os agentes?", "i", 60), XE, 790, passo=0.08)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1560, cy=700, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y, s = 470, 120
    G = Q.grupos(EQ3, W / 2, y, s, "center")
    Q.formula_em(c, t, C["s18"], EQ3, W / 2, y, s, align="center")
    tag(c, t, C["s18.a"], G[0], "0", 44)
    tag(c, t, C["s18.a"] + 0.6, G[4], "+2", 44)
    arco(c, t, C["s18.a"] + 1.4, G[0]["cx"], G[4]["cx"], G[0]["topo"] - 100, OXI, "se oxida", True, 110)
    E.foco(c, t, C["s18.a"] + 1.0, 0.4, lambda a: E.formula(c, "x + 2 · (−1) = 0", 1380, 860, 50, "g", TINTA2, a))
    agente(c, t, C["s18.b"], G[0]["cx"] + 30, 700, "agente redutor", OXI, 42)
    tag(c, t, C["s18.c"], G[2], "+1", 44)
    tag(c, t, C["s18.c"] + 0.6, G[6], "0", 44)
    arco(c, t, C["s18.c"] + 1.2, G[2]["cx"], G[6]["cx"], G[2]["base"] + 40, RED, "se reduz", False, 120)
    agente(c, t, C["s18.e"], G[2]["cx"] - 10, 820, "agente oxidante", RED, 42)
    if t >= C["s19.a"]:
        E.foco(c, t, C["s19.a"], 0.4, lambda a: E.pilula(c, "Cl: −1 dos dois lados", W / 2, 990, 46, "g", fundo=TINTA2, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s20.a"], [("oxidar", "g", 66, OXI)] + ps("= perder elétrons, Nox sobe", "i", 66)),
                     (C["s20.b"], [("reduzir", "g", 66, RED)] + ps("= ganhar, Nox desce", "i", 66)),
                     (C["s20.c"], [("o agente", "g", 66, COR)] + ps("faz no outro o contrário", "i", 66))], 240, 390, 190, 66, 46)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("balancear", "g", 100, COR)], XE, 420)
    E.frase(c, t, C["s21.a"] + 0.5, [("pelos", "i", 100), ("elétrons", "g", 100, RED)], XE, 560)
    for k in range(3):
        E.foco(c, t, C["s21.a"] + 0.8 + 0.2 * k, 0.4, lambda a, k=k: eletron(c, XE + 60 + 80 * k, 740, 24, a))
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, troca=b_troca, nomes=b_nomes, forno=b_forno, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
