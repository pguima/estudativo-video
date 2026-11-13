"""Visual — Estudativo · QUI-MIS-004: curva de aquecimento, pura ou mistura.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e as convenções da trilha (QUI-MIS-002).
Nesta aula, a CURVA DE AQUECIMENTO é desenhada trecho a trecho, no tempo da fala (curva_aq): cada trecho tem o seu
instante, o patamar fica na cor da matéria e ganha o rótulo embaixo; a temperatura do patamar é lida no eixo do lado,
com tracejado até o eixo e o número escrito nele. Trecho em rampa de mistura = mesma cor, sem patamar. A água pura
aparece em cinza por trás quando é preciso comparar.
Peça candidata ao kit: curva_aq (Q.aquecimento com um instante por trecho, marcas de tempo e valores escolhidos).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-004_curva_de_aquecimento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("curva", "misturas", "atalho", "erro", "questao", "fim"))
BR = "#FFFFFF"

# curvas (minuto, °C): 5 trechos de 2 minutos
AGUA = [(0, -20), (2, 0), (4, 0), (6, 100), (8, 100), (10, 120)]
SALGADA = [(0, -25), (2, -12), (4, -2), (6, 102), (8, 116), (10, 125)]
SOLDA = [(0, 110), (2, 183), (4, 183), (6, 250), (8, 290), (10, 320)]
ALCOOL = [(0, -40), (2, -24), (4, -12), (6, 78), (8, 78), (10, 100)]
QUESTAO = [(0, -5), (2, 10), (4, 18), (6, 78), (8, 78), (10, 95)]


def patamares(nos):
    """quais trechos são patamar: (fusão, ebulição)"""
    return (nos[1][1] == nos[2][1], nos[3][1] == nos[4][1])


def tipo(nos):
    return {(True, True): "pura", (False, False): "comum", (True, False): "eutética", (False, True): "azeotrópica"}[patamares(nos)]


assert tipo(AGUA) == "pura" and tipo(SALGADA) == "comum" and tipo(SOLDA) == "eutética" and tipo(ALCOOL) == "azeotrópica"
assert tipo(QUESTAO) == "azeotrópica" and QUESTAO[3][1] == 78 and (QUESTAO[1][1], QUESTAO[2][1]) == (10, 18)
assert AGUA[1][0] == 2 and AGUA[2][0] == 4  # "a fusão vai de dois a quatro minutos"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, r=44):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, r, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


class Graf:
    """caixa do gráfico: tempo (0 a 10 min) × temperatura (tmin a tmax)"""
    def __init__(self, x, y, w, h, tmin, tmax):
        self.x, self.y, self.w, self.h = x, y, w, h
        span = tmax - tmin
        self.lo, self.hi = tmin - span * 0.08, tmax + span * 0.06

    def X(self, m):
        return self.x + self.w * 0.04 + self.w * 0.9 * m / 10

    def Y(self, T):
        return self.y + self.h - self.h * (T - self.lo) / (self.hi - self.lo)


def eixos(c, t, t0, G, size=40, nomes=True, escuro=False, marcas_t=False):
    tinta = BR if escuro else TINTA
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    M.arrow(c, G.x, G.y + G.h, G.x, G.y - 20, tinta, p, 4, 18, ease_io(prog(t, t0, 0.6)))
    M.arrow(c, G.x, G.y + G.h, G.x + G.w + 20, G.y + G.h, tinta, p, 4, 18, ease_io(prog(t, t0, 0.6)))
    if nomes:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.escreve(c, "temperatura (°C)", G.x + 18, G.y - 10, size, "b", tinta, a),
                                              E.escreve(c, "tempo (min)", G.x + G.w - E.larg("tempo (min)", "b", size), G.y + G.h + size * (2.6 if marcas_t else 1.4), size, "b", tinta, a)))
    if marcas_t:
        for m in range(0, 11, 2):
            E.foco(c, t, t0 + 0.4, 0.4, lambda a, m=m: (M.line(c, G.X(m), G.y + G.h, G.X(m), G.y + G.h + 12, tinta, a, 3),
                                                       centro(c, str(m), G.X(m), G.y + G.h + 48, 36, "b", TINTA2 if not escuro else "#B8BCC8", a)))


def curva_aq(c, t, G, nos, tl, dur=None, cor=None, largura=8, valores=(), tv=None, rotulos=None, tr=None, size=44, escuro=False, a=1.0):
    """desenha a curva trecho a trecho: trecho k (de nos[k] a nos[k+1]) começa em tl[k] e leva dur[k] s.
    valores = temperaturas escritas no eixo (com tracejado até o primeiro ponto que as atinge), cada uma em tv[i].
    rotulos = textos dos 5 trechos (None pula), cada um em tr[k]."""
    cor = cor or E.COR
    dur = dur or [1.0] * 5
    tinta = BR if escuro else TINTA
    for k in range(5):
        if tl[k] is None or t < tl[k]:
            continue
        p = ease_io(prog(t, tl[k], dur[k]))
        (m0, T0), (m1, T1) = nos[k], nos[k + 1]
        x0, y0, x1, y1 = G.X(m0), G.Y(T0), G.X(m1), G.Y(T1)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, a, largura)
    for i, T in enumerate(valores):
        ti = tv[i] if tv else 0
        q = ep(t, ti, 0.4) * a
        if q <= 0:
            continue
        m = next(mm for mm, TT in nos if TT == T)
        M.line(c, G.x, G.Y(T), G.X(m), G.Y(T), TINTA2 if not escuro else "#8A8D99", 0.8 * q, 3, dash=[10, 8])
        s = E._num(T)
        E.foco(c, t, ti, 0.4, lambda aa, s=s, T=T: E.escreve(c, s, G.x - 16 - E.larg(s, "b", size), G.Y(T) + size * 0.36, size, "b", tinta, aa * a))
    if rotulos:
        for k, s in enumerate(rotulos):
            if not s or tr[k] is None:
                continue
            (m0, T0), (m1, T1) = nos[k], nos[k + 1]
            mx, my = (G.X(m0) + G.X(m1)) / 2, (G.Y(T0) + G.Y(T1)) / 2
            plat = T0 == T1
            dy = size * 1.4 if plat else -size * 0.8
            dx = 0 if plat else -size * 2.2
            E.foco(c, t, tr[k], 0.4, lambda aa, s=s, mx=mx, my=my, dx=dx, dy=dy, plat=plat: centro(
                c, s, mx + dx, my + dy, size, "b" if plat else "i", (E.CLARO if escuro else COR) if plat else tinta, aa * a))


def mini(c, t, t0, x, y, nos, titulo, nome, tnome, tl=None, size=36):
    """gráfico pequeno com título e o nome do tipo embaixo"""
    G = Graf(x, y, 480, 330, min(T for _, T in nos), max(T for _, T in nos))
    eixos(c, t, t0, G, nomes=False)
    tl = tl or [t0 + 0.3 + 0.35 * k for k in range(5)]
    curva_aq(c, t, G, nos, tl, [0.4] * 5, largura=7)
    pl = patamares(nos)
    for k, ok in ((1, pl[0]), (3, pl[1])):
        if ok and t >= tl[k]:
            (m0, T0), (m1, _) = nos[k], nos[k + 1]
            q = ep(t, tl[k] + 0.4, 0.4)
            c.drawCircle((G.X(m0) + G.X(m1)) / 2, G.Y(T0), 46 + 3 * math.sin(t * 5), M.paint(E.COR, q, stroke=5))
    E.frase(c, t, t0, [(titulo, "i", 46, TINTA2)], x + 240, y - 40, "center")
    pilula_em(c, t, tnome, nome, x + 240, y + 420, 50, E.COR)
    return G


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        G = Graf(760, 200, 1060, 700, -20, 20)
        eixos(c, t, C["s01.a"], G)
        tl = [C["s01.a"] + 0.6, C["s01.c"], None, None, None]
        curva_aq(c, t, G, AGUA, tl, [C["s01.c"] - C["s01.a"] - 0.6, 3.0], valores=(-20, 0), tv=(C["s01.a"] + 0.4, C["s01.c"]))
        E.frase(c, t, C["s01.a"], [("gelo", "g", 90), ("a", "i", 80)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 0.6, [("−20 °C", "g", 90, COR)], XE, 420)
        E.frase(c, t, C["s01.b"], ps("o termômetro sobe…", "i", 64, TINTA2), XE, 560, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("e trava no", "i", 70) + [("zero", "g", 70, COR)], XE, 680, passo=0.12)
        if t >= C["s01.c"] + 0.5:
            q = ep(t, C["s01.c"] + 0.5, 0.4)
            c.drawCircle((G.X(2) + G.X(4)) / 2, G.Y(0), 80 + 5 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
        E.frase(c, t, C["s01.d"], ps("para onde vai o calor?", "i", 66, TINTA2), XE, 900, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("ler", "i", 74), ("a", "i", 74), ("curva", "g", 70, COR)]),
                 (C["s02.c"], [("fusão", "g", 70), ("e", "i", 74), ("ebulição", "g", 70)]),
                 (C["s02.d"], [("pura", "g", 70), ("ou", "i", 74), ("mistura?", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("pura", "g", 70, COR), ("=", "g", 70, TINTA2)] + ps("um tipo de partícula;", "i", 68) + [("mistura", "g", 70, COR), ("=", "g", 70, TINTA2)] + ps("mais", "i", 68), XE, 400, passo=0.1)
    E.frase(c, t, C["s03.b"], [("fusão", "g", 70), ("e", "i", 68), ("ebulição", "g", 70)] + ps("absorvem calor", "i", 68), XE, 580, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("no gráfico, cada ponto junta", "i", 68) + [("dois", "g", 70, COR), ("valores", "i", 68)], XE, 760, passo=0.1)
    G = Graf(1350, 820, 380, 200, 0, 10)
    eixos(c, t, C["s03.c"] + 0.4, G, nomes=False)
    E.foco(c, t, C["s03.c"] + 1.4, 0.4, lambda a: (M.line(c, G.X(6), G.Y(6), G.X(6), G.y + G.h, TINTA2, a, 3, dash=[8, 6]),
                                                  M.line(c, G.x, G.Y(6), G.X(6), G.Y(6), TINTA2, a, 3, dash=[8, 6]),
                                                  E.bola(c, G.X(6), G.Y(6), 16, a=a)))


# ---------------- a curva da água ----------------
GA = Graf(330, 180, 1000, 720, -20, 120)


def b_curva(c, t, C, b):
    G = GA
    eixos(c, t, C["s04.a"], G, marcas_t=t >= C["s07"])
    if C["s04.b"] <= t < C["s05"]:
        q = ep(t, C["s04.b"], 0.4) * (1 - ep(t, C["s04.c"], 0.4))
        M.line(c, G.x, G.y + G.h, G.x + G.w, G.y + G.h, E.COR, q, 12)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.escreve(c, "tempo de fogo", G.x + G.w / 2 - 150, G.y + G.h - 30, 52, "g", COR, a * (1 - ep(t, C["s04.c"], 0.4))))
    if C["s04.c"] <= t < C["s05"]:
        q = ep(t, C["s04.c"], 0.4)
        M.line(c, G.x, G.y + G.h, G.x, G.y, E.COR, q, 12)
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "temperatura, em graus", G.x + 40, G.y + G.h / 2, 52, "g", COR, a))
    tl = [C["s05.a"], C["s05.b"], C["s06.a"], C["s06.b"], C["s06.c"]]
    rot = [None, "patamar", None, "patamar", None]
    curva_aq(c, t, G, AGUA, tl, [1.2, 1.2, 1.2, 1.2, 0.8], valores=(-20, 0, 100), tv=(C["s05.a"], C["s05.b"], C["s06.b"]),
             rotulos=rot, tr=[None, C["s05.c"], None, C["s06.b"] + 0.8, None])
    E.foco(c, t, C["s05.a"] + 0.3, 0.4, lambda a: E.escreve(c, "sólido", G.X(0.2), G.Y(-20) - 30, 44, "i", TINTA2, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "sólido + líquido", G.X(1.6), G.Y(0) - 30, 44, "b", COR, a))
    E.foco(c, t, C["s06.a"] + 0.5, 0.4, lambda a: E.escreve(c, "líquido", G.X(4.5), G.Y(50), 44, "i", TINTA2, a))
    E.foco(c, t, C["s06.b"] + 0.4, 0.4, lambda a: E.escreve(c, "fervendo", G.X(6.4), G.Y(100) - 30, 44, "b", COR, a))
    E.foco(c, t, C["s06.c"] + 0.4, 0.4, lambda a: E.escreve(c, "vapor", G.X(8.6), G.Y(118) - 26, 44, "i", TINTA2, a))
    xr = 1440
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], ps("o calor do patamar", "i", 56, TINTA2), xr, 300, passo=0.1)
            E.frase(c, t, C["s07.a"] + 0.8, [("não", "g", 66, COR), ("some", "g", 66)], xr, 400, passo=0.12)
            E.frase(c, t, C["s07.b"], ps("solta as partículas", "i", 56), xr, 540, passo=0.1)
            E.frase(c, t, C["s07.b"] + 1.0, ps("em vez de agitar", "i", 56), xr, 620, passo=0.1)
            pilula_em(c, t, C["s07.c"], "temperatura parada", xr + 200, 760, 44, E.COR)
            for k in (1, 3):
                (m0, T0), (m1, _) = AGUA[k], AGUA[k + 1]
                q = ep(t, C["s07.c"] + 0.3, 0.4)
                c.drawCircle((G.X(m0) + G.X(m1)) / 2, G.Y(T0), 70 + 4 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t >= C["s08"]:
        E.foco(c, t, C["s08.a"], 0.4, lambda a: (E.escreve(c, "ponto de fusão", xr, 560, 50, "i", TINTA2, a), E.escreve(c, "PF = 0 °C", xr, 650, 72, "g", COR, a)))
        E.foco(c, t, C["s08.b"], 0.4, lambda a: (E.escreve(c, "ponto de ebulição", xr, 300, 50, "i", TINTA2, a), E.escreve(c, "PE = 100 °C", xr, 390, 72, "g", COR, a)))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "ao nível do mar", xr, 760, 46, "i", TINTA2, a))
        pilula_em(c, t, C["s08.d"], "impressão digital", xr + 200, 900, 44, TINTA)


# ---------------- misturas ----------------
def b_misturas(c, t, C, b):
    if t >= C["s09"]:
        G = Graf(110, 330, 480, 330, -25, 125)
        eixos(c, t, C["s09"], G, nomes=False)
        curva_aq(c, t, G, AGUA, [C["s09"] + 0.2] * 5, [0.01] * 5, cor="#C9C9CE", largura=5)
        tl = [C["s09.a"] - 0.8, C["s09.a"] - 0.4, C["s09.a"], C["s09.b"], C["s09.b"] + 0.8]
        curva_aq(c, t, G, SALGADA, tl, [0.4, 0.4, 0.4, 1.2, 0.4], largura=7)
        E.frase(c, t, C["s09"], [("água com sal", "i", 46, TINTA2)], G.x + 240, G.y - 40, "center")
        E.foco(c, t, C["s09"] + 0.3, 0.4, lambda a: E.escreve(c, "cinza: água pura", G.x + 30, G.y + 40, 40, "i", CINZA, a))
        pilula_em(c, t, C["s09.d"], "mistura comum", G.x + 240, G.y + 420, 50, E.COR)
        if C["s09.c"] <= t < C["s10"]:
            E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "não deita: só inclina menos", 640, 980, 50, "i", COR, a))
    if t >= C["s10"]:
        mini(c, t, C["s10.a"], 720, 330, SOLDA, "solda de estanho e chumbo", "eutética", C["s10.d"],
             tl=[C["s10.b"] - 0.8, C["s10.b"], C["s10.c"] - 0.4, C["s10.c"], C["s10.c"] + 0.4])
        E.foco(c, t, C["s10.b"] + 0.6, 0.4, lambda a: E.escreve(c, "183 °C", 760, 430, 44, "b", COR, a))
    if t >= C["s11"]:
        mini(c, t, C["s11.a"], 1330, 330, ALCOOL, "álcool 96%", "azeotrópica", C["s11.d"],
             tl=[C["s11.a"] + 0.4, C["s11.c"] - 0.6, C["s11.c"], C["s11.b"], C["s11.b"] + 0.8])
        E.foco(c, t, C["s11.b"] + 0.6, 0.4, lambda a: E.escreve(c, "78 °C", 1430, 405, 44, "b", COR, a))
    E.frase(c, t, C["s09"], ps("e se for mistura?", "i", 70, TINTA2), W / 2, 150, "center", 0.12)


# ---------------- atalho (palco) ----------------
def icone(c, x, y, nos, a, escuro=True):
    G = Graf(x, y, 260, 150, min(T for _, T in nos), max(T for _, T in nos))
    M.line(c, G.x, G.y + G.h, G.x, G.y, "#8A8D99", a, 3)
    M.line(c, G.x, G.y + G.h, G.x + G.w, G.y + G.h, "#8A8D99", a, 3)
    pl = patamares(nos)
    for k in range(5):
        (m0, T0), (m1, T1) = nos[k], nos[k + 1]
        plat = (k == 1 and pl[0]) or (k == 3 and pl[1])
        cor = (E.CLARO if escuro else E.COR) if plat else (BR if escuro else TINTA)
        M.line(c, G.X(m0), G.Y(T0), G.X(m1), G.Y(T1), cor, a, 7 if plat else 5)


def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def quatro():
            E.frase(c, t, C["s12"], ps("o atalho:", "i", 66, CLARO) + [("conte", "g", 62, BR), ("os", "i", 66, CLARO), ("patamares", "g", 62, E.CLARO)], XE, 150, passo=0.12)
            linhas = ((C["s12.b"], AGUA, "2 patamares", "pura"), (C["s12.c"], SALGADA, "nenhum", "mistura comum"),
                      (C["s12.d"], SOLDA, "só o de baixo", "eutética"), (C["s12.e"], ALCOOL, "só o de cima", "azeotrópica"))
            for k, (ti, nos, n, nome) in enumerate(linhas):
                y = 250 + 200 * k
                E.foco(c, t, ti, 0.4, lambda a, nos=nos, y=y: icone(c, XE + 40, y, nos, a))
                E.frase(c, t, ti + 0.2, [(n, "g", 60, BR)], XE + 400, y + 110)
                E.frase(c, t, ti + 0.5, [("→", "g", 60, CLARO), (nome, "g", 64, E.CLARO)], XE + 960, y + 110, passo=0.12)
        E.saida(c, t, C["s13"] - 0.1, quatro)
        return
    if t < C["s14"]:
        def nomes():
            E.frase(c, t, C["s13"], ps("para não trocar os nomes:", "i", 64, CLARO), W / 2, 220, "center", 0.1)
            E.frase(c, t, C["s13.a"], [("eutético", "g", 96, E.CLARO)], W / 2, 420, "center")
            E.frase(c, t, C["s13.a"] + 0.8, ps("“que funde bem”: patamar na fusão", "i", 62, BR), W / 2, 520, "center", 0.1)
            E.frase(c, t, C["s13.b"], [("azeótropo", "g", 96, E.CLARO)], W / 2, 720, "center")
            E.frase(c, t, C["s13.b"] + 0.8, ps("“não muda ao ferver”: patamar na ebulição", "i", 62, BR), W / 2, 820, "center", 0.1)
            pilula_em(c, t, C["s13.c"], "o nome diz qual patamar fica", W / 2, 960, 46, E.COR)
        E.saida(c, t, C["s14"] - 0.1, nomes)
        return
    E.frase(c, t, C["s14.a"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("gráfico com um trecho só", "i", 66, CLARO), W / 2, 300, "center", 0.12)
    G = Graf(660, 420, 600, 360, 20, 110)
    E.foco(c, t, C["s14.a"] + 0.6, 0.4, lambda a: (M.line(c, G.x, G.y + G.h, G.x, G.y, "#8A8D99", a, 4), M.line(c, G.x, G.y + G.h, G.x + G.w, G.y + G.h, "#8A8D99", a, 4)))
    trecho = [(0, 40), (2, 70), (4, 100), (6, 100), (8, 100), (10, 100)]
    curva_aq(c, t, G, trecho, [C["s14.a"] + 1.0, C["s14.a"] + 1.4, C["s14.a"] + 1.8, None, None], [0.4] * 5, cor=E.CLARO, escuro=True)
    E.frase(c, t, C["s14.b"], ps("julgue só o patamar que aparece", "i", 60, BR), W / 2, 920, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    G = Graf(330, 240, 900, 640, -20, 120)
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 170)
    E.frase(c, t, C["s15.a"], ps("o patamar no eixo errado", "i", 64), XE + 430, 170, passo=0.1)
    eixos(c, t, C["s15"] + 0.2, G, marcas_t=True)
    curva_aq(c, t, G, AGUA, [C["s15"] + 0.4 + 0.2 * k for k in range(5)], [0.3] * 5)
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.chave(c, G.X(2), G.X(4), G.Y(0) - 40, ERRADO, a, -24))

    def errado():
        E.frase(c, t, C["s16.b"] + 0.5, [("de", "i", 60), ("2", "g", 66, ERRADO), ("a", "i", 60), ("4", "g", 66, ERRADO), ("min", "i", 60)], 1350, 400, passo=0.12)
        E.frase(c, t, C["s16.b"] + 1.6, [("PF", "g", 80, ERRADO), ("=", "g", 80, ERRADO), ("2?", "g", 80, ERRADO)], 1350, 540, passo=0.12)
        if t >= C["s17.a"]:
            E.risco(c, 1340, 560, 1680, 470, t, C["s17.a"], largura=10)
    E.saida(c, t, C["s17.b"] - 0.1, errado)
    E.frase(c, t, C["s17.a"], ps("PF é temperatura", "i", 60, TINTA2), 1350, 680, passo=0.1)
    if t >= C["s17.b"]:
        p = ease_io(prog(t, C["s17.b"], 0.8))
        M.arrow(c, G.X(3), G.Y(0), lerp(G.X(3), G.x + 6, p), G.Y(0), E.COR, 1, 6, 22)
    E.foco(c, t, C["s17.c"], 0.4, lambda a: E.escreve(c, "PF = 0 °C", 1350, 420, 80, "g", COR, a))
    E.foco(c, t, C["s17.c"] + 0.3, 0.4, lambda a: E.selo(c, 1800, 395, 46, True, a))
    E.frase(c, t, C["s17.d"], ps("eixo de baixo: quanto durou", "i", 54, TINTA2), 1350, 820, passo=0.1)


# ---------------- questão ----------------
GQ = Graf(1060, 200, 720, 720, -5, 95)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s17.a"], ps("um material é aquecido", "i", 60, TINTA2), XE, 290, passo=0.1)
    E.frase(c, t, C["s17.b"], ps("fusão: de 10 a 18 °C, subindo", "i", 58), XE, 400, passo=0.08)
    E.frase(c, t, C["s17.c"], ps("depois, deita nos 78 °C", "i", 58), XE, 490, passo=0.08)
    E.frase(c, t, C["s17.d"], [("1", "g", 60, COR)] + ps("ponto de ebulição?", "i", 64), XE, 660, passo=0.1)
    E.frase(c, t, C["s17.e"], [("2", "g", 60, COR)] + ps("pura ou mistura? de que tipo?", "i", 64), XE, 780, passo=0.1)
    if t < C["s18"]:
        eixos(c, t, C["s17.a"], GQ)
        tl = [C["s17.a"] + 0.4, C["s17.b"], C["s17.b"] + 0.6, C["s17.c"], C["s17.c"] + 0.8]
        curva_aq(c, t, GQ, QUESTAO, tl, [0.4, 0.8, 0.6, 1.0, 0.4], valores=(10, 18, 78), tv=(C["s17.b"], C["s17.b"] + 0.6, C["s17.c"]))
    else:
        E.relogio(c, t, C["s18.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    G = Graf(330, 220, 900, 640, -5, 95)
    eixos(c, t, C["s19"], G)
    curva_aq(c, t, G, QUESTAO, [C["s19"] + 0.2 * k for k in range(5)], [0.3] * 5, valores=(10, 18, 78), tv=(C["s19"],) * 3)
    if t >= C["s19.a"]:
        q = ep(t, C["s19.a"], 0.4)
        c.drawCircle((G.X(6) + G.X(8)) / 2, G.Y(78), 80 + 4 * math.sin(t * 5), M.paint(E.COR, q, stroke=6))
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.escreve(c, "PE = 78 °C", 1350, 330, 80, "g", COR, a))
    if t >= C["s19.c"]:
        E.chave(c, G.X(2), G.X(4), G.Y(18) - 50, TINTA2, ep(t, C["s19.c"], 0.5), -24)
        E.foco(c, t, C["s19.c"] + 0.3, 0.4, lambda a: E.escreve(c, "sem patamar", G.X(0.6), G.Y(18) - 100, 44, "b", TINTA2, a))
    E.frase(c, t, C["s20.a"], [("1", "g", 60, COR), ("patamar,", "i", 58), ("o", "i", 58), ("de", "i", 58), ("cima", "g", 56)], 1350, 480, passo=0.1)
    pilula_em(c, t, C["s20.b"], "azeotrópica", 1560, 620, 64, E.COR)

    def erro():
        E.foco(c, t, C["s20.c"], 0.4, lambda a: E.escreve(c, "substância pura", 1350, 800, 60, "i", ERRADO, a))
        if t >= C["s20.c"] + 0.8:
            E.risco(c, 1340, 815, 1780, 760, t, C["s20.c"] + 0.8, largura=8)
    erro()


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", [("patamar", "g", 66, COR), ("=", "g", 66, TINTA2), ("mudança", "i", 70), ("de", "i", 70), ("estado", "i", 70)]),
                 ("s21.b", [("PF", "g", 66), ("e", "i", 70), ("PE:", "g", 66), ("leia", "i", 70), ("no", "i", 70), ("eixo", "i", 70), ("do", "i", 70), ("lado", "g", 66, COR)]),
                 ("s21.c", [("conte", "i", 70), ("os", "i", 70), ("patamares", "g", 66, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("Praticando", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s22.a"] + 0.6, ps("questões de prova", "i", 80), XE, 520, passo=0.12)
    for k, nos in enumerate((AGUA, SOLDA, ALCOOL)):
        E.foco(c, t, C["s22.a"] + 0.8 + 0.3 * k, 0.4, lambda a, nos=nos, k=k: icone(c, XE + 20 + 320 * k, 650, nos, a, escuro=False))
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, curva=b_curva, misturas=b_misturas, atalho=b_atalho, erro=b_erro,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
