"""Visual — Estudativo · QUI-ELE-005: pilhas e baterias do dia a dia.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha Eletroquímica (cabeçalho da QUI-ELE-001). Pilha alcalina em corte
(peça local alcalina()), bateria de chumbo por fora (bateria(), a mesma da QUI-MIS-001) e por dentro (placas(); candidatas ao
kit). Nox em pílula sobre o símbolo; oxidação em âmbar, redução em azul. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-005_pilhas_e_baterias.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("alcalina", "chumbo", "descarte", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON
PB, PBO2 = "#7D838F", "#5A3A2A"

ALC = "Zn + 2 MnO2 -> ZnO + Mn2O3"
CHU = "Pb + PbO2 + 2 H2SO4 -> 2 PbSO4 + 2 H2O"
NICD = "Cd + 2 NiOOH + 2 H2O -> Cd(OH)2 + 2 Ni(OH)2"
assert Q.lados(ALC)[0] == Q.lados(ALC)[1] and Q.lados(CHU)[0] == Q.lados(CHU)[1] and Q.lados(NICD)[0] == Q.lados(NICD)[1]
assert 4 + 2 * (-2) == 0 and 2 * 3 + 3 * (-2) == 0           # Mn +4 no MnO2; +3 no Mn2O3
assert 4 + 2 * (-2) == 0 and 2 + (-2) == 0 and 6 * 2 == 12     # Pb +4 no PbO2; +2 no PbSO4 (SO4 −2); 12 V
assert 3 + (-2) + (-2) + 1 == 0 and 2 + 2 * (-1) == 0          # Ni +3 no NiOOH; +2 no Ni(OH)2


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


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def tag(c, t, t0, g, nox, size, fundo=TINTA, dy=0):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, nox, g["cx"], g["topo"] - size * 1.0 + dy, size, "g", fundo=fundo, a=a))


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def alcalina(c, cx, cy, w, h, a=1.0, corte=1.0):
    """pilha AA em pé; corte 0..1 abre o miolo: zinco em pó no centro, pasta de MnO2 em volta"""
    if a <= 0:
        return
    x0, y0 = cx - w / 2, cy - h / 2
    M.rrect(c, cx - w * 0.16, y0 - h * 0.05, w * 0.32, h * 0.07, 6, "#B8BCC4", a)
    M.rrect(c, x0, y0, w, h, w * 0.12, "#2A2B31", a)
    M.rrect(c, x0, y0 + h * 0.62, w, h * 0.38, w * 0.12, "#C9A227", a)
    centro(c, "+", cx, y0 + h * 0.14, w * 0.5, "g", BR, a)
    if corte > 0:
        q = a * corte
        M.rrect(c, x0 + w * 0.08, y0 + h * 0.08, w * 0.84, h * 0.86, w * 0.08, "#3B3034", q)       # MnO2
        M.rrect(c, x0 + w * 0.28, y0 + h * 0.12, w * 0.44, h * 0.76, w * 0.06, "#E9E3D0", q)       # separador
        M.rrect(c, x0 + w * 0.32, y0 + h * 0.14, w * 0.36, h * 0.72, w * 0.05, "#9AA0AA", q)       # zinco
        for k in range(18):
            px = cx + (((k * 37) % 23) / 23 - 0.5) * w * 0.28
            py = y0 + h * 0.18 + (k / 18) * h * 0.64
            c.drawCircle(px, py, w * 0.025, M.paint("#C8CDD6", q))
        M.line(c, cx, y0 + h * 0.2, cx, y0 + h * 0.86, "#C9A227", q, w * 0.03)


def bateria(c, cx, cy, w, h, a=1.0):
    """bateria de carro: caixa escura com os dois polos e a etiqueta na cor da matéria"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#2A2B31", a)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h * 0.2, 22, "#3A3B42", a)
    for dx, s in ((-0.3, "−"), (0.3, "+")):
        M.rrect(c, cx + dx * w - 26, cy - h / 2 - 34, 52, 40, 8, "#9AA0A8", a)
        centro(c, s, cx + dx * w, cy - h / 2 + h * 0.15, 56, "g", BR, a)
    M.rrect(c, cx - w * 0.36, cy - h * 0.05, w * 0.72, h * 0.38, 14, E.COR, a)
    centro(c, "12 V", cx, cy + h * 0.24, h * 0.2, "g", BR, a)


def placas(c, t, t0, x, y, w, h, n=6, a=1.0, vira=0.0):
    """corte da bateria: placas de Pb (cinza) e PbO2 (marrom) alternadas no ácido; vira 0..1 = ambas viram PbSO4 (branco)"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    M.rrect(c, x, y, w, h, 18, "#F2E9B8", 0.5 * q)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(Q.VIDRO, q, stroke=5))
    gap = w / (n + 1)
    for k in range(n):
        base = PB if k % 2 == 0 else PBO2
        cor = M.mix(base, "#E4E4DC", vira)
        qq = ep(t, t0 + 0.2 + 0.1 * k, 0.3) * a
        M.rrect(c, x + gap * (k + 1) - 18, y + h * 0.12, 36, h * 0.8, 6, cor, qq)


def lixo(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.5, cy - s * 0.45, s, s * 0.95, s * 0.08, "#5E636D", a)
    M.rrect(c, cx - s * 0.6, cy - s * 0.6, s * 1.2, s * 0.14, s * 0.05, "#3A3D45", a)
    for dx in (-0.22, 0, 0.22):
        M.line(c, cx + dx * s, cy - s * 0.3, cx + dx * s, cy + s * 0.38, "#3A3D45", a, s * 0.05)


def coleta(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.6, cy - s * 0.5, s * 1.2, s, s * 0.1, CERTO, a)
    M.rrect(c, cx - s * 0.3, cy - s * 0.42, s * 0.6, s * 0.1, s * 0.04, "#0D5E3D", a)
    centro(c, "pilhas", cx, cy + s * 0.12, s * 0.24, "g", BR, a)
    centro(c, "e baterias", cx, cy + s * 0.36, s * 0.18, "b", BR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            E.foco(c, t, C["s01.a"], 0.5, lambda a: alcalina(c, 480, 520, 150, 400, a, 0))
            p = ease_io(prog(t, C["s01.a"] + 1.2, 1.0))
            E.foco(c, t, C["s01.a"] + 0.8, 0.4, lambda a: lixo(c, 480, 880, 170, a))
            E.foco(c, t, C["s01.a"] + 1.4, 0.4, lambda a: E.pilula(c, "vai para o lixo", 480, 220, 50, "g", fundo=TINTA2, a=a))
            E.foco(c, t, C["s01.b"], 0.5, lambda a: bateria(c, 1380, 560, 560, 380, a))
            E.foco(c, t, C["s01.b"] + 1.0, 0.4, lambda a: E.pilula(c, "recarrega por anos", 1380, 220, 50, "g", fundo=E.COR, a=a))
            E.frase(c, t, C["s01.c"], ps("as duas são", "i", 70) + [("pilhas", "g", 66, COR)], W / 2, 960, "center", 0.12)
            E.frase(c, t, C["s01.d"], ps("o que muda por dentro?", "i", 64, TINTA2), W / 2, 1040, "center", 0.1)
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1580, 560, 230 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 230, passo=0.14)
    lista(c, t, [(C["s02.b"], [("se oxida", "g", 62, OXI), ("e", "i", 66), ("se reduz", "g", 62, RED)] + ps("nas duas", "i", 66)),
                 (C["s02.c"], ps("por que uma", "i", 66) + [("recarrega", "g", 62)]),
                 (C["s02.d"], ps("por que pilha", "i", 66) + [("não vai para o lixo", "g", 62, COR)]),
                 (C["s02.e"], [("atalho", "g", 62, COR), ("de", "i", 66), ("prova", "i", 66)])], XE, 390, 150, 62)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    lista(c, t, [(C["s03.a"], [("ânodo", "g", 62, OXI)] + ps("se oxida e manda elétrons", "i", 64)),
                 (C["s03.b"], [("cátodo", "g", 62, RED)] + ps("recebe e se reduz", "i", 64)),
                 (C["s03.c"], ps("Nox: a soma fecha em", "i", 64) + [("zero", "g", 62, COR)])], XE, 400, 190, 64, 42)


# ---------------- alcalina ----------------
def b_alcalina(c, t, C, b):
    cx, cy = 1500, 560
    corte = ease_io(prog(t, C["s04.a"] - 0.3, 0.8))
    k = ease_io(prog(t, C["s05"], 0.8))
    E.foco(c, t, C["s04"], 0.5, lambda a: alcalina(c, lerp(cx, 1760, k), lerp(cy, 300, k), lerp(250, 110, k), lerp(640, 280, k), a, corte))
    E.frase(c, t, C["s04"], ps("a pilha", "i", 70) + [("alcalina", "g", 66, COR)], XE, 190, passo=0.12)
    if t < C["s05"]:
        def s04():
            E.foco(c, t, C["s04.a"] + 0.3, 0.4, lambda a: E.pilula(c, "zinco em pó", cx - 330, cy - 120, 46, "g", fundo="#7D838F", a=a))
            E.foco(c, t, C["s04.b"], 0.4, lambda a: E.pilula(c, "pasta escura", cx - 330, cy + 40, 46, "g", fundo="#3B3034", a=a))
            Q.formula_em(c, t, C["s04.c"], "MnO2", XE, 470, 130, cores={"Mn": E.COR})
            E.foco(c, t, C["s04.c"] + 0.3, 0.4, lambda a: E.escreve(c, "dióxido de manganês", XE, 560, 52, "i", TINTA2, a))
            Q.formula_em(c, t, C["s04.d"], "KOH", XE, 740, 120)
            E.foco(c, t, C["s04.d"] + 0.3, 0.4, lambda a: E.escreve(c, "uma base forte: alcalina", XE, 830, 52, "i", TINTA2, a))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    y, s = 540, 92
    G = Q.grupos(ALC, 820, y, s, "center")
    Q.formula_em(c, t, C["s05"], ALC, 820, y, s, align="center")
    tag(c, t, C["s05.a"], G[0], "0", 40)
    tag(c, t, C["s05.b"], G[4], "+2", 40)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "o zinco se oxida: ânodo, polo −", 600, 700, 46, "g", fundo=OXI, a=a))
    if t >= C["s06"]:
        tag(c, t, C["s06.b"], G[2], "+4", 40, E.COR)
        E.foco(c, t, C["s06.a"], 0.4, lambda a: E.formula(c, "x + 2 · (−2) = 0", 300, 960, 52, "g", TINTA2, a))
        tag(c, t, C["s06.c"], G[6], "+3", 40, E.COR)
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "o manganês se reduz: cátodo, polo +", 720, 790, 46, "g", fundo=RED, a=a))
        E.foco(c, t, C["s06.e"], 0.5, lambda a: E.pilula(c, "1,5 V", 1760, 520, 60, "g", fundo=TINTA, a=a))


# ---------------- chumbo ----------------
def b_chumbo(c, t, C, b):
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07"], ps("a bateria do", "i", 70) + [("carro", "g", 66, COR)], XE, 190, passo=0.12)
            placas(c, t, C["s07.a"], 1000, 300, 760, 520)
            E.foco(c, t, C["s07.a"] + 0.5, 0.4, lambda a: E.pilula(c, "ácido sulfúrico", 1380, 870, 44, "g", fundo="#B39A1E", a=a))
            E.foco(c, t, C["s07.b"], 0.4, lambda a: (Q.formula(c, "Pb", XE, 470, 120, TINTA, a), E.pilula(c, "Nox 0", XE + 300, 440, 46, "g", fundo=PB, a=a)))
            E.foco(c, t, C["s07.c"], 0.4, lambda a: Q.formula(c, "PbO2", XE, 680, 120, TINTA, a))
            E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "Pb: +4", XE + 400, 650, 46, "g", fundo=PBO2, a=a))
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s09"]:
        y, s = 430, 86
        G = Q.grupos(CHU, W / 2, y, s, "center")
        Q.formula_em(c, t, C["s08"], CHU, W / 2, y, s, align="center")
        E.foco(c, t, C["s08.a"], 0.4, lambda a: E.pilula(c, "as duas placas viram o mesmo sal", W / 2, 600, 46, "g", fundo=TINTA, a=a))
        tag(c, t, C["s08.a"] + 0.8, G[8], "+2", 38)
        tag(c, t, C["s08.b"], G[0], "0", 38)
        E.foco(c, t, C["s08.b"] + 0.5, 0.4, lambda a: E.pilula(c, "0 → +2: se oxida, ânodo", 560, 760, 46, "g", fundo=OXI, a=a))
        tag(c, t, C["s08.c"], G[1], "+4", 38)
        E.foco(c, t, C["s08.c"] + 0.5, 0.4, lambda a: E.pilula(c, "+4 → +2: se reduz, cátodo, polo +", 1320, 870, 46, "g", fundo=RED, a=a))
        return
    E.frase(c, t, C["s09.a"], ps("cada célula dá cerca de", "i", 66) + [("2 V", "g", 66, COR)], XE, 220, passo=0.12)
    for k in range(6):
        E.foco(c, t, C["s09.b"] + 0.15 * k, 0.3, lambda a, k=k: (M.rrect(c, 260 + 240 * k, 400, 200, 260, 18, "#2A2B31", a), centro(c, "2 V", 360 + 240 * k, 560, 60, "g", BR, a)))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.formula(c, "6 × 2 = 12 V", W / 2, 850, 110, "g", COR, a, "center"))


# ---------------- recarga ----------------
def b_recarga(c, t, C, b):
    if t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10"], ps("por que essa", "i", 70) + [("recarrega?", "g", 66, COR)], XE, 190, passo=0.12)
            vira = ease_io(prog(t, C["s10.a"], 1.0)) * (1 - ease_io(prog(t, C["s10.d"], 1.2)))
            placas(c, t, C["s10"], 1120, 300, 660, 520, vira=vira)
            E.foco(c, t, C["s10.a"], 0.4, lambda a: E.pilula(c, "o sulfato de chumbo fica grudado", 1450, 880, 42, "g", fundo=TINTA, a=a))
            E.frase(c, t, C["s10.b"], ps("o alternador manda", "i", 56) + [("corrente ao contrário", "g", 52, COR)], XE, 420, passo=0.1)
            if t >= C["s10.c"]:
                p = ease_io(prog(t, C["s10.c"], 0.8))
                M.arrow(c, 820, 600, lerp(820, 300, p), 600, E.COR, 1, 10, 30, p)
                E.foco(c, t, C["s10.c"] + 0.4, 0.4, lambda a: E.escreve(c, "a reação anda para trás", XE, 700, 52, "i", TINTA, a))
            E.foco(c, t, C["s10.d"], 0.4, lambda a: Q.formula(c, "Pb + PbO2", XE, 790, 70, TINTA, a))
            pilula_em(c, t, C["s10.e"], "forçar com corrente: eletrólise (outra aula)", W / 2, 1000, 44, TINTA2)
        E.saida(c, t, C["s11"] - 0.1, s10)
        return
    E.foco(c, t, C["s11.a"], 0.5, lambda a: alcalina(c, 420, 520, 180, 460, a, 1.0))
    E.frase(c, t, C["s11.a"], ps("na alcalina, os produtos", "i", 58) + [("não voltam", "g", 54)], 640, 300, passo=0.1)
    E.frase(c, t, C["s11.b"], ps("forçar a recarga pode", "i", 58) + [("vazar ou esquentar", "g", 54, ERRADO)], 640, 400, passo=0.1)
    E.frase(c, t, C["s11.c"], ps("celular:", "i", 58) + [("íon-lítio", "g", 56, COR)] + ps("também recarrega", "i", 58), 640, 600, passo=0.1)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: (Q.atomo(c, 720, 780, 60, "Li", a), E.escreve(c, "o metal mais leve,", 820, 770, 52, "i", TINTA, a), E.escreve(c, "lá embaixo na escada", 820, 840, 52, "g", COR, a)))


# ---------------- descarte ----------------
def b_descarte(c, t, C, b):
    if t < C["s13"]:
        E.frase(c, t, C["s12"], ps("e o", "i", 70) + [("lixo?", "g", 66, COR)], XE, 190, passo=0.12)
        for k, el in enumerate(("Pb", "Hg", "Cd")):
            Q.atomo_em(c, t, C["s12.a"] + 0.3 * k, 360 + 230 * k, 420, 80, el)
            E.foco(c, t, C["s12.a"] + 0.3 * k + 0.2, 0.4, lambda a, k=k, el=el: centro(c, ("chumbo", "mercúrio", "cádmio")[k], 360 + 230 * k, 560, 46, "i", TINTA2, a))
        E.foco(c, t, C["s12.a"] + 1.2, 0.4, lambda a: E.pilula(c, "metais tóxicos", 590, 660, 50, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s12.b"], ps("e líquidos que", "i", 56) + [("corroem", "g", 54)], XE, 780, passo=0.1)
        E.foco(c, t, C["s12.c"], 0.5, lambda a: lixo(c, 1450, 520, 260, a))
        if t >= C["s12.d"]:
            for k in range(7):
                f = ((t - C["s12.d"]) * 0.5 + k / 7) % 1.0
                E.bola(c, 1450 + (k - 3) * 40, 700 + f * 260, 12, ("#575C66", "#B8B8C8", "#E070C0")[k % 3], ep(t, C["s12.d"], 0.4) * (1 - f))
            E.foco(c, t, C["s12.d"] + 0.3, 0.4, lambda a: E.pilula(c, "solo e água", 1450, 1010, 50, "g", fundo="#8B5E3C", a=a))
        return
    E.frase(c, t, C["s13.a"], ps("a lei brasileira obriga a", "i", 64) + [("logística reversa", "g", 60, COR)], XE, 240, passo=0.1)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: coleta(c, 560, 620, 320, a))
    E.foco(c, t, C["s13.b"] + 0.6, 0.4, lambda a: E.pilula(c, "em lojas e mercados", 560, 860, 46, "g", fundo=TINTA, a=a))
    if t >= C["s13.c"]:
        p = ease_io(prog(t, C["s13.c"], 0.8))
        M.arrow(c, 800, 620, lerp(800, 1150, p), 620, E.COR, 1, 10, 30, p)
        E.foco(c, t, C["s13.c"] + 0.6, 0.4, lambda a: (E.escreve(c, "fabricante:", 1200, 600, 60, "g", TINTA, a), E.escreve(c, "recicla ou dá o destino certo", 1200, 680, 50, "i", TINTA2, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("a bateria é um balde de elétrons?", "i", 64), XE + 450, 190, passo=0.1)

    def balde():
        x, y = 560, 560
        p = skia.Path(); p.moveTo(x - 160, y - 160); p.lineTo(x + 160, y - 160); p.lineTo(x + 120, y + 160); p.lineTo(x - 120, y + 160); p.close()
        c.drawPath(p, M.paint("#9AA0A8", 1))
        for k in range(12):
            c.drawCircle(x - 100 + (k % 4) * 66, y - 90 + (k // 4) * 70, 18, M.paint(Q.ELETRON, 1))
        if t >= C["s14.a"] + 1.6:
            E.risco(c, x - 220, y + 200, x + 220, y - 200, t, C["s14.a"] + 1.6, largura=12)
    E.foco(c, t, C["s14.a"] + 0.4, 0.5, lambda a: balde())
    E.frase(c, t, C["s14.b"], ps("ela guarda", "i", 62) + [("reagentes químicos", "g", 58, COR)], 1000, 430, passo=0.1)
    E.foco(c, t, C["s14.b"] + 0.8, 0.4, lambda a: Q.formula(c, "Pb + PbO2 + H2SO4", 1000, 560, 70, TINTA, a))
    E.frase(c, t, C["s14.c"], ps("a energia vira corrente", "i", 56), 1000, 690, passo=0.08)
    E.frase(c, t, C["s14.c"] + 0.8, ps("quando a", "i", 56) + [("reação acontece", "g", 52)], 1000, 760, passo=0.08)
    E.frase(c, t, C["s14.d"], ps("descarregada =", "i", 56) + [("sem reagente", "g", 54, COR)], 1000, 880, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s15.a"], ps("pilha de", "i", 64, CLARO) + [("metal e óxido:", "g", 60, BR)], W / 2, 290, "center", 0.1)
        E.frase(c, t, C["s15.b"], [("metal puro", "g", 64, OXI)] + ps("(Nox 0) = ânodo", "i", 66, CLARO), 520, 450, "center", 0.1)
        E.frase(c, t, C["s15.c"], [("óxido", "g", 64, "#7FB2FF")] + ps("(Nox alto) = cátodo", "i", 66, CLARO), 1400, 450, "center", 0.1)
        for k, (tk, m, o) in enumerate(((C["s15.d"], "Zn", "MnO2"), (C["s15.e"], "Pb", "PbO2"))):
            y = 640 + 160 * k
            E.foco(c, t, tk, 0.4, lambda a, m=m, o=o, y=y: (Q.formula(c, m, 520, y, 110, BR, a, "center", escuro=True), Q.formula(c, o, 1400, y, 110, BR, a, "center", escuro=True)))
        return
    E.frase(c, t, C["s16.a"], ps("o metal puro", "i", 64, CLARO) + [("só pode perder", "g", 60, BR)] + ps("elétrons", "i", 64, CLARO), W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s16.b"], ps("e o Nox alto do óxido", "i", 64, CLARO) + [("desce", "g", 60, BR)], W / 2, 420, "center", 0.1)
    E.frase(c, t, C["s16.c"], [("não", "g", 60, ERRADO), ("compensa", "i", 62, CLARO)] + ps("quando quem se reduz é um íon da solução", "i", 62, CLARO), W / 2, 640, "center", 0.1)
    pilula_em(c, t, C["s16.c"] + 2.4, "como na Daniell: use a escada de potenciais", W / 2, 780, 46, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s17.a"], ps("pilha recarregável de", "i", 58, TINTA2) + [("níquel e cádmio", "g", 54)], XE, 280, passo=0.08)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: (Q.formula(c, "Cd -> Cd(OH)2", XE, 430, 90, TINTA, a), E.pilula(c, "Cd: +2", XE + 780, 400, 44, "g", fundo=TINTA, a=a)))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: (Q.formula(c, "Ni: +3 -> +2", XE, 580, 90, TINTA, a)))
    E.frase(c, t, C["s17.d"], [("1", "g", 54, COR)] + ps("quem se oxida? quem é o cátodo?", "i", 58), XE, 760, passo=0.08)
    E.frase(c, t, C["s17.e"], [("2", "g", 54, COR)] + ps("por que não vai para o lixo comum?", "i", 58), XE, 870, passo=0.08)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1560, cy=560, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.foco(c, t, C["s19"], 0.4, lambda a: Q.formula(c, "Cd: 0 -> +2", XE, 330, 100, TINTA, a))
    E.foco(c, t, C["s19.a"], 0.4, lambda a: E.pilula(c, "subiu: se oxida, ânodo", 1250, 300, 50, "g", fundo=OXI, a=a))
    E.foco(c, t, C["s19"] + 0.3, 0.4, lambda a: Q.formula(c, "Ni: +3 -> +2", XE, 530, 100, TINTA, a))
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.pilula(c, "desceu: se reduz, cátodo", 1250, 500, 50, "g", fundo=RED, a=a))
    E.foco(c, t, C["s19.c"], 0.4, lambda a: (Q.atomo(c, XE + 60, 760, 60, "Cd", a), E.escreve(c, "cádmio: metal tóxico", XE + 160, 780, 60, "g", ERRADO, a)))
    E.foco(c, t, C["s19.d"], 0.5, lambda a: coleta(c, 1500, 820, 230, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s20.a"], [("metal puro", "g", 62, OXI)] + ps("se oxida,", "i", 66) + [("óxido", "g", 62, RED)] + ps("se reduz", "i", 66)),
                     (C["s20.b"], [("recarrega", "g", 62)] + ps("quando a corrente desfaz a reação", "i", 66)),
                     (C["s20.c"], ps("pilha vai para a", "i", 66) + [("coleta", "g", 62, COR)])], 200, 380, 190, 66, 46)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("a", "i", 100), ("ferrugem", "g", 100, "#A0522D")], XE, 420)
    E.frase(c, t, C["s21.b"], ps("e o", "i", 80) + [("zinco", "g", 76, COR)] + ps("que protege o navio", "i", 80), XE, 580, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, alcalina=b_alcalina, chumbo=b_chumbo, recarga=b_recarga, descarte=b_descarte,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
