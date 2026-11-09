"""Visual — Estudativo · FIS-EGF-007: empuxo: princípio de Arquimedes.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-007_empuxo_principio_de_arquimedes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("origem", "formula", "atalho", "questao", "fim"))

# todas as contas da aula
assert abs(1000 * 0.002 * 10 - 20) < 1e-9 and abs(800 * 0.002 * 10 - 16) < 1e-9 and abs(7800 * 0.001 * 10 - 78) < 1e-9
assert abs(1000 * 0.001 * 10 - 10) < 1e-9 and abs(800 * 0.003 * 10 - 24) < 1e-9 and 3 * 8 == 24 and abs(1.5 * 8 - 12) < 1e-9


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
FERRO, ISOPOR = "#6E7380", "#F4F4F0"


def piscina(c, x, y, w, h, nivel=40, a=1.0):
    """recipiente com água até `nivel` px abaixo da borda; devolve a altura da superfície"""
    if a <= 0:
        return y + nivel
    c.drawRect(skia.Rect.MakeXYWH(x, y + nivel, w, h - nivel), M.paint(AGUA, 0.45 * a))
    M.line(c, x, y + nivel, x + w, y + nivel, AGUA2, a, 5)
    for X in (x, x + w):
        M.line(c, X, y, X, y + h, TINTA, a, 6)
    M.line(c, x - 3, y + h, x + w + 3, y + h, TINTA, a, 6)
    return y + nivel


def bola_cor(c, cx, cy, r, cor, a=1.0, contorno=False):
    E.bola(c, cx, cy, r, cor, a)
    if contorno:
        c.drawCircle(cx, cy, r, M.paint(TINTA2, a, stroke=3))


def empuxo(c, t, t0, P, comp, rot="E", modulo=None, lado=1):
    """o empuxo: seta azul para cima saindo de P"""
    F.forca(c, t, t0, P, 90, comp, rot, F.NEG, modulo, lado=lado)


def pressao_caixa(c, t, t0, cx, cy, w, h, k_cima, k_baixo, k_lado, d=0.5):
    """setinhas de pressão nas faces da caixa (comprimentos em px)"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    for i in range(3):
        x = cx - w / 2 + (i + 0.5) * w / 3
        F.seta(c, x, cy - h / 2 - 10 - k_cima, x, cy - h / 2 - 8, E.COR, q, 6, cabeca=16, p=q)
        F.seta(c, x, cy + h / 2 + 10 + k_baixo, x, cy + h / 2 + 8, E.COR, q, 7, cabeca=18, p=q)
    for j in range(2):
        y = cy - h / 2 + (j + 0.5) * h / 2
        kk = k_lado * (0.8 + 0.4 * j)
        F.seta(c, cx - w / 2 - 10 - kk, y, cx - w / 2 - 8, y, E.COR, q, 6, cabeca=16, p=q)
        F.seta(c, cx + w / 2 + 10 + kk, y, cx + w / 2 + 8, y, E.COR, q, 6, cabeca=16, p=q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            x, y, w, h = 900, 300, 860, 640
            q = ep(t, C["s01.a"], 0.5)
            ys = piscina(c, x, y, w, h, 60, q)
            if q > 0:
                for cx, cor in ((x + 230, FERRO), (x + 630, ISOPOR)):
                    M.line(c, cx, y + h, cx, y + h - 220, TINTA2, q, 3)
                    bola_cor(c, cx, y + h - 300, 90, cor, q, cor == ISOPOR)
            E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: (centro(c, "ferro", x + 230, y + h + 60, 44, "b", TINTA, a), centro(c, "isopor", x + 630, y + h + 60, 44, "b", TINTA, a)))
            for cx in (x + 230, x + 630):
                empuxo(c, t, C["s01.c"], (cx, y + h - 390), 150, "?" if t < C["s01.d"] else "E", lado=1)
            E.frase(c, t, C["s01.a"], ps("ferro e isopor,", "i", 64) + [("mesmo tamanho", "g", 62, COR)], XE, 190, passo=0.1)
            E.frase(c, t, C["s01.b"], ps("presas debaixo d'água", "i", 58, TINTA2), XE, 280, passo=0.1)
            E.frase(c, t, C["s01.c"], ps("quem recebe mais", "i", 60), XE, 450, passo=0.1)
            E.frase(c, t, C["s01.c"] + 0.5, [("força para cima?", "g", 58)], XE, 540)
            E.frase(c, t, C["s01.d"], [("nenhuma:", "g", 70, COR)] + ps("é a mesma", "i", 70), XE, 720, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "de onde vem o empuxo"), ("s02.b", "quanto ele vale")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "lei de Stevin:", "mais fundo, mais pressão"), ("s03.c", "densidade:", "água = 1.000 kg/m³")), 2)


# ---------------- de onde vem ----------------
def b_origem(c, t, C, b):
    x, y, w, h = 980, 220, 760, 800
    cx, cy, bw, bh = x + w / 2, y + 430, 240, 240
    if t < C["s05"]:
        def s04():
            q = ep(t, C["s04.a"], 0.5)
            piscina(c, x, y, w, h, 60, q)
            E.foco(c, t, C["s04.a"] + 0.2, 0.4, lambda a: F.bloco(c, cx, cy, bw, bh, None, a=a, cor=TINTA2))
            if t >= C["s04.b"]:
                for j in range(2):
                    yy = cy - bh / 2 + (j + 0.5) * bh / 2
                    kk = 50 * (0.8 + 0.4 * j)
                    F.seta(c, cx - bw / 2 - 18 - kk, yy, cx - bw / 2 - 8, yy, E.COR, ep(t, C["s04.b"], 0.4), 6, cabeca=16)
                    F.seta(c, cx + bw / 2 + 18 + kk, yy, cx + bw / 2 + 8, yy, E.COR, ep(t, C["s04.b"], 0.4), 6, cabeca=16)
            if t >= C["s04.c"]:
                for i in range(3):
                    xx = cx - bw / 2 + (i + 0.5) * bw / 3
                    F.seta(c, xx, cy - bh / 2 - 70, xx, cy - bh / 2 - 8, E.COR, ep(t, C["s04.c"], 0.4), 6, cabeca=16)
                    F.seta(c, xx, cy + bh / 2 + 130, xx, cy + bh / 2 + 8, E.COR, ep(t, C["s04.d"], 0.4), 8, cabeca=20)
            empuxo(c, t, C["s04.e"], (cx, cy - 20), 300, "E", lado=1)
            E.frase(c, t, C["s04.b"], [("laterais:", "g", 58)] + ps("se anulam", "i", 60), XE, 260, passo=0.1)
            E.frase(c, t, C["s04.c"], [("face de baixo:", "g", 58)] + ps("mais funda", "i", 60), XE, 380, passo=0.1)
            E.frase(c, t, C["s04.d"], [("pressão maior", "g", 60, COR)] + ps("embaixo", "i", 60), XE, 480, passo=0.1)
            E.frase(c, t, C["s04.e"], ps("a sobra:", "i", 70) + [("o empuxo", "g", 76, F.NEG)], XE, 680, passo=0.12)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    # s05: o líquido deslocado
    E.frase(c, t, C["s05.a"], [("Arquimedes:", "g", 64, COR)], XE, 190)
    E.frase(c, t, C["s05.b"], [("empuxo", "g", 60, F.NEG), ("=", "g", 60, TINTA2)] + ps("peso do líquido deslocado", "i", 62), XE, 300, passo=0.1)
    q = ep(t, C["s05.c"] - 0.6, 0.5)
    sobe = 70 * ease_io(prog(t, C["s05.c"], 1.0))
    if q > 0:
        x0, y0, w0, h0 = 760, 500, 700, 480
        c.drawRect(skia.Rect.MakeXYWH(x0, y0 + 120 - sobe, w0, h0 - 120 + sobe), M.paint(AGUA, 0.45 * q))
        M.line(c, x0, y0 + 120 - sobe, x0 + w0, y0 + 120 - sobe, AGUA2, q, 5)
        for X in (x0, x0 + w0):
            M.line(c, X, y0, X, y0 + h0, TINTA, q, 6)
        M.line(c, x0, y0 + h0, x0 + w0, y0 + h0, TINTA, q, 6)
        yb = lerp(y0 - 180, y0 + 260, ease_io(prog(t, C["s05.c"], 1.0)))
        F.bloco(c, x0 + w0 / 2, yb, 220, 220, None, a=q, cor=TINTA2)
    if t >= C["s05.d"]:
        qq = ep(t, C["s05.d"], 0.5)
        c.drawRect(skia.Rect.MakeXYWH(1560, 700, 220, 70 * 700 / 220 * 0 + 220), M.paint(AGUA2, 0.55 * qq))
        c.drawRect(skia.Rect.MakeXYWH(1560, 700, 220, 220), M.paint(TINTA, qq, stroke=4))
        F.forca(c, t, C["s05.d"] + 0.3, (1670, 810), -90, 200, "P", lado=1)
        E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: centro(c, "a água que saiu", 1670, 670, 42, "b", TINTA2, a))


# ---------------- a fórmula ----------------
def b_formula(c, t, C, b):
    if t < C["s07"]:
        def s06():
            F.formula_legenda(c, t, C["s06.a"], "E = d · V · g", [("d", "densidade do LÍQUIDO", "kg/m^3"), ("V", "volume deslocado (a parte dentro)", "m^3"),
                                                                 ("g", "gravidade, 10", "m/s^2")], XE, 330, 140, tl=[C["s06.b"], C["s06.c"], C["s06.d"]], size_l=50, cor=F.NEG)
            E.frase(c, t, C["s06.e"], [("d · V", "g", 60, F.NEG), ("=", "g", 60, TINTA2)] + ps("massa de líquido;", "i", 60) + [("× g", "g", 60, F.NEG), ("=", "g", 60, TINTA2)] + ps("o peso dela", "i", 60),
                    XE, 900, passo=0.08)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    if t < C["s08"]:
        def s07():
            x, y, w, h = 1150, 330, 560, 560
            q = ep(t, C["s07.a"], 0.5)
            piscina(c, x, y, w, h, 60, q)
            E.foco(c, t, C["s07.a"] + 0.2, 0.4, lambda a: F.bloco(c, x + w / 2, y + 330, 200, 160, "2 L", a=a, cor=TINTA2))
            empuxo(c, t, C["s07.d"], (x + w / 2, y + 300), 200, "E", "20 N", lado=1)
            linhas(c, t, [(C["s07.b"], "2 L = 0,002 m^3", TINTA2), (C["s07.c"], "E = 1.000 · 0,002 · 10", TINTA)], XE, 260, 150, 72)
            bola_txt(c, t, C["s07.d"], "20 N", 420, 600, 110, 56)
            E.formula_em(c, t, C["s07.e"], "no óleo: 800 · 0,002 · 10", XE, 820, 66, "g", "#9A6B10")
            bola_txt(c, t, C["s07.f"], "16 N", 420, 960, 85, 48, OLEO)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s09"]:
        def s08():
            x, y, w, h = 900, 300, 860, 640
            q = ep(t, C["s08.a"], 0.5)
            piscina(c, x, y, w, h, 60, q)
            if q > 0:
                for cx, cor in ((x + 230, FERRO), (x + 630, ISOPOR)):
                    M.line(c, cx, y + h, cx, y + h - 220, TINTA2, q, 3)
                    bola_cor(c, cx, y + h - 300, 90, cor, q, cor == ISOPOR)
            for cx in (x + 230, x + 630):
                empuxo(c, t, C["s08.d"], (cx, y + h - 390), 150, "E", lado=1)
            E.frase(c, t, C["s08.b"], ps("mesmo tamanho:", "i", 60) + [("mesmo V", "g", 60, F.NEG)], XE, 220, passo=0.1)
            E.frase(c, t, C["s08.d"], [("mesmo d,", "g", 58), ("mesmo V,", "g", 58), ("mesmo E", "g", 58, F.NEG)], XE, 340, passo=0.12)
            E.frase(c, t, C["s08.e"], ps("o que muda:", "i", 60) + [("o peso", "g", 60, COR)], XE, 520, passo=0.1)
            E.frase(c, t, C["s08.f"], ps("peso × empuxo: próxima aula", "i", 50, TINTA2), XE, 620, passo=0.08)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    if t < C["s10"]:
        def s09():
            x, y, w, h = 900, 380, 860, 560
            q = ep(t, C["s09.a"], 0.5)
            ys = piscina(c, x, y, w, h, 100, q)
            afunda = lerp(40, 110, ease_io(prog(t, C["s09.c"], 1.0)))
            if q > 0:
                bx, by = x + w / 2, ys + afunda - 70
                p = skia.Path(); p.moveTo(bx - 260, by); p.lineTo(bx + 260, by); p.lineTo(bx + 200, by + 140); p.lineTo(bx - 200, by + 140); p.close()
                c.drawPath(p, M.paint(MADEIRA, q))
                c.save(); c.clipRect(skia.Rect.MakeLTRB(x, ys, x + w, y + h))
                c.drawPath(p, M.paint(AGUA2, 0.35 * q))
                c.restore()
                if t >= C["s09.c"]:
                    F.bloco(c, bx, by - 50, 200, 100, "carga", a=ep(t, C["s09.c"], 0.4), size=36)
            empuxo(c, t, C["s09.d"], (x + w / 2 + 120, ys + afunda + 140), 130, "E", lado=1)
            E.frase(c, t, C["s09.a"], ps("só uma parte dentro?", "i", 64), XE, 220, passo=0.1)
            E.frase(c, t, C["s09.b"], [("conta só essa parte", "g", 62, F.NEG)], XE, 330)
            E.frase(c, t, C["s09.c"], ps("barco carregado:", "i", 58) + [("afunda mais", "g", 58)], XE, 520, passo=0.1)
            E.frase(c, t, C["s09.d"], [("mais empuxo", "g", 62, F.NEG)], XE, 620)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    x, y, w, h = 1100, 200, 600, 820
    q = ep(t, C["s10"], 0.5)
    piscina(c, x, y, w, h, 40, q)
    desce = 260 * ease_io(prog(t, C["s10.b"], 1.4))
    cx, cy = x + w / 2, y + 260 + desce
    if q > 0:
        F.bloco(c, cx, cy, 180, 160, None, a=q, cor=TINTA2)
    pressao_caixa(c, t, C["s10.c"], cx, cy, 180, 160, 40 + desce * 0.25, 90 + desce * 0.25, 30)
    E.frase(c, t, C["s10.a"], ps("mais fundo,", "i", 64) + [("muda o empuxo?", "g", 62)], XE, 220, passo=0.1)
    E.frase(c, t, C["s10.b"], [("não,", "g", 64, CERTO)] + ps("depois de todo dentro", "i", 62), XE, 330, passo=0.1)
    E.frase(c, t, C["s10.c"], ps("pressão sobe", "i", 58) + [("em cima e embaixo", "g", 56)], XE, 520, passo=0.1)
    E.frase(c, t, C["s10.d"], [("mesma diferença,", "g", 58, COR), ("mesmo empuxo", "g", 58, F.NEG)], XE, 620, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("densidade do corpo na fórmula", "i", 62), XE + 480, 190, passo=0.1)
    E.frase(c, t, C["s11.b"], [("ferro:", "g", 60), ("1 L,", "g", 60), ("7.800 kg/m³", "g", 60, TINTA2)], XE, 330, passo=0.12)
    E.formula_em(c, t, C["s11.c"], "7.800 · 0,001 · 10 = 78 N", XE, 480, 80, "g", ERRADO)
    if t >= C["s11.d"]:
        E.risco(c, XE - 10, 500, XE + 1010, 420, t, C["s11.d"], largura=10)
    E.frase(c, t, C["s11.d"], ps("quem empurra é a", "i", 64) + [("água", "g", 64, F.NEG)], XE, 640, passo=0.12)
    E.formula_em(c, t, C["s11.e"], "1.000 · 0,001 · 10 = 10 N", XE, 800, 80, "g", CERTO)
    pilula_em(c, t, C["s11.f"], "78 N é o peso da bola", 1500, 960, 48, TINTA)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.frase(c, t, C["s12.a"], ps("na água:", "i", 76, CLARO) + [("1 litro", "g", 76, BR), ("→", "g", 70, CLARO), ("10 N", "g", 76, BR)], W / 2, 340, "center", 0.12)
            E.frase(c, t, C["s12.b"], [("1 L de água", "g", 62, BR), ("=", "g", 60, CLARO), ("1 kg", "g", 62, BR)], W / 2 - 330, 520, "center", 0.12)
            E.frase(c, t, C["s12.c"], [("1 kg", "g", 62, BR), ("pesa", "i", 64, CLARO), ("10 N", "g", 62, BR)], W / 2 + 380, 520, "center", 0.12)
            E.formula_em(c, t, C["s12.d"], "3 L  →  30 N", W / 2 - 330, 720, 92, "g", CLARO, "center")
            E.formula_em(c, t, C["s12.e"], "0,5 L  →  5 N", W / 2 + 380, 720, 92, "g", CLARO, "center")
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], ps("outro líquido:", "i", 72, CLARO) + [("ajuste", "g", 72, BR)], W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("× a densidade", "g", 68, BR), ("em", "i", 70, CLARO), ("g/cm³", "g", 64, CLARO)], W / 2, 450, "center", 0.12)
    E.formula_em(c, t, C["s13.c"], "800 kg/m^3 = 0,8 g/cm^3", W / 2, 640, 84, "g", CLARO, "center")
    E.formula_em(c, t, C["s13.c"] + 1.6, "óleo: 1 L  →  8 N", W / 2, 820, 96, "g", BR, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s14")
    E.frase(c, t, C["s14.a"], [("objeto de", "i", 64), ("3 L", "g", 64, COR)] + ps("todo no óleo", "i", 64), XE, 330, passo=0.12)
    E.frase(c, t, C["s14.b"], [("d =", "g", 60), ("800 kg/m³", "g", 60, "#9A6B10")], XE, 440, passo=0.12)
    E.frase(c, t, C["s14.c"], ps("qual é o", "i", 70) + [("empuxo?", "g", 70, F.NEG)], XE, 620, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("e com", "i", 70) + [("metade dentro?", "g", 70, COR)], XE, 760, passo=0.12)
    if t < C["s15"]:
        x, y, w, h = 1200, 330, 520, 600
        q = ep(t, C["s14.a"], 0.5)
        if q > 0:
            c.drawRect(skia.Rect.MakeXYWH(x, y + 60, w, h - 60), M.paint(OLEO, 0.55 * q))
            M.line(c, x, y + 60, x + w, y + 60, "#B98A2A", q, 5)
            for X in (x, x + w):
                M.line(c, X, y, X, y + h, TINTA, q, 6)
            M.line(c, x, y + h, x + w, y + h, TINTA, q, 6)
            F.bloco(c, x + w / 2, y + 340, 200, 160, "3 L", a=q, cor=TINTA2)
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    linhas(c, t, [(C["s16.a"], "3 L = 0,003 m^3", TINTA2), (C["s16.b"], "E = 800 · 0,003 · 10", TINTA)], XE, 230, 150, 80)
    bola_txt(c, t, C["s16.c"], "24 N", 1450, 340, 120, 60, CERTO)
    E.formula_em(c, t, C["s16.d"], "atalho: 3 L × 8 N = 24 N", XE, 560, 72, "g", TINTA2)
    E.formula_em(c, t, C["s16.e"], "metade: 1,5 L × 8 N", XE, 760, 80, "g", TINTA)
    bola_txt(c, t, C["s16.f"], "12 N", 1450, 740, 120, 60, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s18"]:
        E.saida(c, t, C["s18"] - 0.1, lambda: resumo(c, t, C, "s17", (
            ("s17.a", [("empuxo:", "g", 66, F.NEG), ("pressão maior", "i", 70), ("embaixo", "g", 66)]),
            ("s17.b", [("E = d · V · g:", "g", 64, F.NEG), ("o peso do líquido deslocado", "i", 66)]),
            ("s17.c", [("d do líquido,", "g", 64), ("V só a parte dentro", "g", 64, COR)]))))
        return

    def desenho():
        q = ep(t, C["s18.b"], 0.6)
        if q <= 0:
            return
        c.drawRect(skia.Rect.MakeLTRB(250, 760, 1200, 1040), M.paint(AGUA, 0.45 * q))
        M.line(c, 250, 760, 1200, 760, AGUA2, q, 5)
        p = skia.Path(); p.moveTo(560, 700); p.lineTo(660, 640); p.lineTo(760, 700); p.lineTo(800, 760); p.lineTo(780, 1000); p.lineTo(540, 1000); p.lineTo(520, 760); p.close()
        c.drawPath(p, M.paint("#EAF6FF", q))
        c.drawPath(p, M.paint(AGUA2, q, stroke=4))
    proxima(c, t, C, "s18", [("Flutuar", "g", 120, COR), ("ou", "i", 110), ("afundar", "g", 120, COR)], None, desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, origem=b_origem, formula=b_formula, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
