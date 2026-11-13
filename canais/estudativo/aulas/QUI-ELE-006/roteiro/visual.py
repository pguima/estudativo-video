"""Visual — Estudativo · QUI-ELE-006: corrosão e proteção dos metais.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha Eletroquímica (cabeçalho da QUI-ELE-001). A ferrugem é a gota sobre a
chapa (peça local gota()): ânodo no meio (Fe²⁺ saindo), cátodo na borda (O₂ chegando), elétrons azuis andando na chapa. Navio
com blocos de zinco (peça local navio()). Escada de potenciais como na QUI-ELE-004 (escada(), candidata ao kit), com o ferro
destacado: o metal de sacrifício fica abaixo dele. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-006_corrosao_e_protecao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ferrugem", "sacrificio", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON
ACO, ZINCO, FERRUGEM, AGUA = "#7A7F88", "#B9C0CC", "#A0522D", "#9CCBE8"

POT = {"Ag": 0.80, "Cu": 0.34, "Pb": -0.13, "Sn": -0.14, "Fe": -0.44, "Zn": -0.76, "Mg": -2.37}
PAR = {"Ag": "Ag^+/Ag", "Cu": "Cu^2+/Cu", "Pb": "Pb^2+/Pb", "Sn": "Sn^2+/Sn", "Fe": "Fe^2+/Fe", "Zn": "Zn^2+/Zn", "Mg": "Mg^2+/Mg"}
assert POT["Zn"] < POT["Fe"] and POT["Mg"] < POT["Fe"] and POT["Sn"] > POT["Fe"] and POT["Pb"] > POT["Fe"]
assert [m for m in ("Cu", "Pb", "Mg", "Ag") if POT[m] < POT["Fe"]] == ["Mg"]


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


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def eletron(c, x, y, r=14, a=1.0):
    E.bola(c, x, y, r, Q.ELETRON, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.16))


def ion(c, x, y, r, txt, cor, a=1.0, size=None):
    E.bola(c, x, y, r, cor, a)
    centro(c, txt, x, y + r * 0.35, size or r * 0.9, "g", BR, a)


def navio(c, cx, cy, w, a=1.0, zinco=1.0, gasto=0.0):
    """casco de aço na água, com blocos de zinco presos embaixo; gasto 0..1 = os blocos diminuem"""
    if a <= 0:
        return
    h = w * 0.28
    p = skia.Path()
    p.moveTo(cx - w / 2, cy - h * 0.3); p.lineTo(cx + w / 2, cy - h * 0.3); p.lineTo(cx + w * 0.38, cy + h * 0.6)
    p.lineTo(cx - w * 0.42, cy + h * 0.6); p.close()
    c.drawPath(p, M.paint("#3D4350", a))
    M.rrect(c, cx - w * 0.3, cy - h * 0.8, w * 0.42, h * 0.5, 10, "#E8E8E2", a)
    M.rrect(c, cx + w * 0.12, cy - h * 0.62, w * 0.12, h * 0.32, 8, E.COR, a)
    M.rrect(c, cx - w * 0.6, cy + h * 0.15, w * 1.2, h * 0.9, 0, AGUA, 0.55 * a)
    if zinco > 0:
        for k in range(4):
            bw = w * 0.07 * (1 - 0.6 * gasto)
            M.rrect(c, cx - w * 0.3 + k * w * 0.18 - bw / 2, cy + h * 0.52, bw, h * 0.16, 4, ZINCO, a * zinco)


def gota(c, t, t0, cx, cy, w, te=None, tc=None, tf=None):
    """chapa de ferro com uma gota d'água: ânodo no meio, cátodo na borda; te = elétrons andam, tc = cátodo, tf = ferrugem"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, cx - w / 2, cy, w, 70, 8, ACO, q)
    p = skia.Path()
    gw, gh = w * 0.62, w * 0.2
    p.moveTo(cx - gw / 2, cy); p.cubicTo(cx - gw * 0.42, cy - gh * 1.3, cx + gw * 0.42, cy - gh * 1.3, cx + gw / 2, cy); p.close()
    c.drawPath(p, M.paint(AGUA, 0.75 * q))
    c.drawPath(p, M.paint("#4F8FBF", q, stroke=4))
    if tf is not None:
        f = ep(t, tf, 1.2)
        if f > 0:
            M.rrect(c, cx - gw * 0.22, cy - 12, gw * 0.44, 24, 10, FERRUGEM, f)
    if te is not None and t >= te:
        for lado in (-1, 1):
            Q.eletrons(c, t, te, [(cx, cy + 35), (cx + lado * gw * 0.46, cy + 35)], 110, 90, 12)
        for k in range(3):
            f = ((t - te) * 0.4 + k / 3) % 1.0
            ion(c, cx + (k - 1) * 50, cy - 20 - f * gh * 0.7, 20, "2+", "#D9732A", ep(t, te, 0.4) * (1 - f * 0.5), 18)
    if tc is not None and t >= tc:
        for lado in (-1, 1):
            f = ((t - tc) * 0.5) % 1.0
            x = cx + lado * gw * 0.44
            E.foco(c, t, tc, 0.4, lambda a, x=x: (Q.formula(c, "O2", x, cy - 170 + 0 * a, 44, "#2F64D6", a, "center")))
            if t >= tc + 0.3:
                M.arrow(c, x, cy - 150, x, cy - 50, "#2F64D6", ep(t, tc + 0.3, 0.3), 5, 18, ep(t, tc + 0.3, 0.4))


class Escada:
    def __init__(self, x, y0, y1, vmin, vmax):
        self.x, self.y0, self.y1, self.vmin, self.vmax = x, y0, y1, vmin, vmax

    def y(self, v):
        return lerp(self.y1, self.y0, (v - self.vmin) / (self.vmax - self.vmin))


def v_br(v):
    return ("+" if v > 0 else "−" if v < 0 else "") + f"{abs(v):.2f}".replace(".", ",")


def escada(c, t, t0, S, els, tl=None, destaque=(), riscar=(), escuro=False, size=52):
    tinta = BR if escuro else TINTA
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.arrow(c, S.x, S.y1 + 30, S.x, lerp(S.y1 + 30, S.y0 - 40, p), TINTA2 if not escuro else "#C8CAD2", 1, 5, 22, p)
    for k, el in enumerate(els):
        tk = tl[k] if tl else t0 + 0.4 + 0.2 * k
        v, y = POT[el], S.y(POT[el])
        cor = (E.CLARO if escuro else E.COR) if el in destaque else ("#A0522D" if el == "Fe" else tinta)

        def deg(a, y=y, el=el, v=v, cor=cor):
            M.line(c, S.x - 36, y, S.x + 36, y, cor, a, 7 if el in destaque or el == "Fe" else 5)
            Q.formula(c, PAR[el], S.x - 64, y + size * 0.34, size, cor, a, "right")
            E.escreve(c, v_br(v), S.x + 64, y + size * 0.34, size, "g", cor, a)
        E.foco(c, t, tk, 0.4, deg)
        if el in riscar and t >= tk + 0.5:
            E.risco(c, S.x - 330, y + 20, S.x + 260, y - 20, t, tk + 0.5, largura=8)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            navio(c, 1200, 560, 900, ep(t, C["s01.a"], 0.6), 1.0, ease_io(prog(t, C["s01.c"], 2.5)))
            E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "blocos de zinco", 1200, 820, 50, "g", fundo="#6E7686", a=a))
            E.frase(c, t, C["s01.a"], ps("navio de", "i", 70) + [("aço", "g", 66)], XE, 220, passo=0.12)
            E.foco(c, t, C["s01.a"] + 1.0, 0.4, lambda a: E.escreve(c, "ferro com um pouco de carbono", XE, 300, 46, "i", TINTA2, a))
            E.frase(c, t, C["s01.c"], ps("o zinco vai sendo comido", "i", 58), XE, 950, passo=0.1)
            E.frase(c, t, C["s01.d"], ps("por que o", "i", 70) + [("zinco", "g", 66, COR)] + ps("se gasta?", "i", 70), XE, 1040, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], ps("a", "i", 70) + [("ferrugem", "g", 64, FERRUGEM)] + ps("como uma pilha", "i", 70)),
                 (C["s02.c"], ps("o metal que", "i", 70) + [("se sacrifica", "g", 64, COR)]),
                 (C["s02.d"], [("atalho", "g", 64, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    lista(c, t, [(C["s03.a"], [("ânodo", "g", 62, OXI)] + ps("se oxida e se gasta", "i", 64)),
                 (C["s03.b"], ps("na escada, quem está", "i", 64) + [("mais embaixo", "g", 62, COR)] + ps("se oxida", "i", 64))], XE, 420, 200, 64, 42)


# ---------------- ferrugem ----------------
GX, GY, GW = 1250, 700, 900


def b_ferrugem(c, t, C, b):
    te = C["s04.c"]
    gota(c, t, C["s04"], GX, GY, GW, te=te, tc=C["s05.b"], tf=C["s06.b"])
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("uma gota d'água na chapa de ferro", "i", 58, TINTA2), XE, 200, passo=0.1)
        E.frase(c, t, C["s04.a"], ps("uma pilha que", "i", 64) + [("ninguém montou", "g", 60, COR)], XE, 300, passo=0.1)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: Q.formula(c, "Fe -> Fe^2+ + 2 e^-", XE, 440, 72, TINTA, a))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "meio da gota: ânodo", GX, GY + 140, 48, "g", fundo=OXI, a=a))
        return
    if t < C["s07"]:
        E.foco(c, t, -10, 0.4, lambda a: E.pilula(c, "meio da gota: ânodo", GX, GY + 140, 48, "g", fundo=OXI, a=a))
        E.frase(c, t, C["s05.a"], ps("os elétrons andam pela chapa até a", "i", 56) + [("borda", "g", 52)], XE, 200, passo=0.08)
        E.foco(c, t, C["s05.c"], 0.4, lambda a: Q.formula(c, "O2 + 2 H2O + 4 e^- -> 4 OH^-", XE, 330, 66, TINTA, a))
        E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "borda: cátodo", GX + GW * 0.3, GY + 230, 48, "g", fundo=RED, a=a))
        if t >= C["s06"]:
            E.foco(c, t, C["s06.a"], 0.4, lambda a: Q.formula(c, "Fe^2+ + OH^-", XE, 470, 66, TINTA, a))
            E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "com mais oxigênio, vira óxido de ferro", XE, 560, 44, "i", TINTA2, a))
            E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "ferrugem", GX, GY - 230, 56, "g", fundo=FERRUGEM, a=a))
        return
    E.frase(c, t, C["s07.a"], [("seco:", "g", 60)] + ps("não enferruja", "i", 62), XE, 220, passo=0.1)
    E.frase(c, t, C["s07.b"], [("sem oxigênio:", "g", 60)] + ps("também não", "i", 62), XE, 320, passo=0.1)
    E.frase(c, t, C["s07.c"], ps("precisa de", "i", 64) + [("água e oxigênio", "g", 60, COR)] + ps("juntos", "i", 64), XE, 440, passo=0.1)
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "na praia, mais rápido", 520, 560, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.e"], 0.4, lambda a: E.escreve(c, "o sal faz a água conduzir melhor", XE, 660, 50, "i", TINTA2, a))


# ---------------- barreira ----------------
def b_barreira(c, t, C, b):
    E.frase(c, t, C["s08"], ps("como proteger?", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s08.a"], [("1", "g", 70, COR)] + ps("tapar", "i", 76), XE, 340, passo=0.1)
    for k, (s, cor) in enumerate((("tinta", "#C0392B"), ("graxa", "#3A3B42"), ("outro metal", ZINCO))):
        x = 300 + 460 * k
        E.foco(c, t, C["s08.b"] + 0.4 * k, 0.4, lambda a, x=x, s=s, cor=cor: (M.rrect(c, x, 560, 360, 60, 8, ACO, a), M.rrect(c, x, 530, 360, 34, 8, cor, a), centro(c, s, x + 180, 700, 50, "g", TINTA, a)))
    E.frase(c, t, C["s08.b"] + 1.4, ps("a água e o ar não chegam ao ferro", "i", 56, TINTA2), W / 2, 830, "center", 0.1)
    pilula_em(c, t, C["s08.c"], "funciona enquanto a camada estiver inteira", W / 2, 960, 46, TINTA)


# ---------------- sacrifício ----------------
S1 = Escada(1450, 300, 940, -2.6, 1.0)


def b_sacrificio(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s09"], [("2", "g", 70, COR)] + ps("o metal de", "i", 72) + [("sacrifício", "g", 66, COR)], XE, 200, passo=0.12)
        gota(c, t, C["s09"], 700, 640, 760)
        E.foco(c, t, C["s09.b"], 0.4, lambda a: (M.rrect(c, 1080, 640, 160, 70, 8, ZINCO, a), centro(c, "Zn", 1160, 690, 44, "g", TINTA, a)))
        E.frase(c, t, C["s09.b"], ps("ligue um metal que se oxide", "i", 56) + [("mais fácil", "g", 52)], XE, 320, passo=0.08)
        if t >= C["s09.d"]:
            Q.eletrons(c, t, C["s09.d"], [(1160, 720), (700, 720)], 130, 100, 12)
            E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "zinco: ânodo", 1160, 800, 46, "g", fundo=OXI, a=a))
            E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "se oxida no lugar do ferro", 1500, 560, 46, "g", fundo=OXI, a=a))
        E.foco(c, t, C["s10.a"], 0.4, lambda a: E.pilula(c, "ferro: cátodo, protegido", 600, 800, 46, "g", fundo=RED, a=a))
        E.foco(c, t, C["s10.c"], 0.4, lambda a: E.escreve(c, "o zinco se gasta e é trocado de tempos em tempos", XE, 960, 48, "i", TINTA2, a))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: navio(c, 1560, 960, 420, a))
        return
    E.frase(c, t, C["s11"], ps("como escolher?", "i", 64, TINTA2) + [("pela escada", "g", 60, COR)], XE, 200, passo=0.12)
    els = ("Ag", "Cu", "Fe", "Zn", "Mg")
    tl = (C["s11.e"], C["s11.e"] + 0.3, C["s11.a"], C["s11.b"], C["s11.c"])
    escada(c, t, C["s11"], S1, els, tl, destaque=("Zn", "Mg"), riscar=("Ag", "Cu"))
    if t >= C["s11.d"]:
        y = S1.y(POT["Fe"])
        M.line(c, 180, y, S1.x + 300, y, FERRUGEM, ep(t, C["s11.d"], 0.4), 3)
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "abaixo do ferro: servem", 560, S1.y(-1.6), 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s11.e"] + 0.6, 0.4, lambda a: E.pilula(c, "acima: não servem", 560, S1.y(0.5), 50, "g", fundo=ERRADO, a=a))


# ---------------- galvanizado ----------------
def b_camadas(c, t, C, b):
    E.frase(c, t, C["s12.a"], ps("aço", "i", 70) + [("galvanizado", "g", 66, COR)] + ps("= coberto de zinco", "i", 70), XE, 240, passo=0.12)
    E.foco(c, t, C["s12.a"] + 0.6, 0.4, lambda a: (M.rrect(c, 360, 520, 1200, 90, 8, ACO, a), M.rrect(c, 360, 490, 1200, 34, 8, ZINCO, a)))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.pilula(c, "1  tapa", 620, 760, 56, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s12.b"] + 1.4, 0.4, lambda a: E.pilula(c, "2  riscou: ainda se sacrifica", 1240, 760, 56, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("qualquer camada protege?", "i", 64), XE + 450, 190, passo=0.1)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (M.rrect(c, 300, 480, 820, 90, 8, ACO, a), M.rrect(c, 300, 450, 820, 34, 8, "#D8DCE2", a), centro(c, "lata: aço com estanho", 710, 640, 50, "g", TINTA, a)))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: (Q.formula(c, "Sn^2+/Sn", 1300, 420, 70, TINTA, a), E.escreve(c, "−0,14", 1640, 420, 70, "g", TINTA, a),
                                            Q.formula(c, "Fe^2+/Fe", 1300, 540, 70, FERRUGEM, a), E.escreve(c, "−0,44", 1640, 540, 70, "g", FERRUGEM, a)))
    E.foco(c, t, C["s13.c"] + 0.6, 0.4, lambda a: E.pilula(c, "estanho acima do ferro", 1530, 640, 44, "g", fundo=TINTA2, a=a))
    if t >= C["s13.d"]:
        q = ep(t, C["s13.d"], 0.4)
        M.rrect(c, 680, 450, 80, 34, 4, FERRUGEM, q)
        E.foco(c, t, C["s13.d"], 0.4, lambda a: E.pilula(c, "riscou: o ferro vira ânodo", 710, 780, 50, "g", fundo=OXI, a=a))
    E.frase(c, t, C["s13.e"], ps("enferruja", "i", 62) + [("mais rápido", "g", 58, ERRADO)] + ps("que sem estanho", "i", 62), W / 2, 960, "center", 0.1)


# ---------------- atalho (palco) ----------------
S2 = Escada(1500, 260, 880, -2.6, 0.5)


def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), XE, 170, passo=0.12)
        escada(c, t, C["s14"] + 0.3, S2, ("Cu", "Fe", "Zn", "Mg"), escuro=True, destaque=("Zn", "Mg"))
        E.frase(c, t, C["s14.a"], ps("sacrifício =", "i", 60, CLARO) + [("abaixo do ferro", "g", 58, BR)], XE, 340, passo=0.1)
        E.frase(c, t, C["s14.b"], ps("o mais embaixo se oxida", "i", 58, CLARO), XE, 450, passo=0.1)
        E.frase(c, t, C["s14.c"], ps("não precisa da ddp:", "i", 58, CLARO), XE, 620, passo=0.1)
        E.foco(c, t, C["s14.d"], 0.4, lambda a: E.pilula(c, "compare com −0,44", 450, 730, 54, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s15.a"], ps("o mais embaixo", "i", 64, CLARO) + [("perde elétrons com mais facilidade", "g", 58, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 60, ERRADO), ("compensa", "i", 62, CLARO)] + ps("ir até o fim da escada:", "i", 62, CLARO), W / 2, 520, "center", 0.1)
    for k, el in enumerate(("Na", "K")):
        Q.atomo_em(c, t, C["s15.c"] + 0.2 * k, 800 + 300 * k, 680, 70, el, escuro=True)
    pilula_em(c, t, C["s15.d"], "reagem com a própria água e somem", W / 2, 850, 50, ERRADO)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s16.a"], ps("tubulação de ferro", "i", 62) + [("enterrada", "g", 58)] + ps("em solo úmido", "i", 62), XE, 290, passo=0.08)
    E.frase(c, t, C["s16.b"], ps("candidatos a metal de sacrifício:", "i", 58, TINTA2), XE, 400, passo=0.08)
    for k, el in enumerate(("Cu", "Pb", "Mg", "Ag")):
        Q.atomo_em(c, t, C["s16.c"] + 0.3 * k, 300 + 240 * k, 540, 70, el)
        E.foco(c, t, C["s16.c"] + 0.3 * k + 0.2, 0.4, lambda a, k=k, el=el: centro(c, Q.NOMES[el], 300 + 240 * k, 660, 44, "i", TINTA2, a))
    E.foco(c, t, C["s16.d"], 0.4, lambda a: (Q.formula(c, "Pb^2+/Pb", XE, 800, 66, TINTA, a), E.escreve(c, "= −0,13 V", XE + 340, 800, 66, "g", TINTA, a)))
    E.frase(c, t, C["s16.e"], ps("qual protege? quem se oxida?", "i", 62), XE, 930, passo=0.08)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1560, cy=520, r=170)


# ---------------- resposta ----------------
S3 = Escada(1500, 230, 990, -2.6, 1.0)


def b_resposta(c, t, C, b):
    els = ("Ag", "Cu", "Pb", "Fe", "Mg")
    tl = (C["s18.b"], C["s18.b"] + 0.2, C["s18.c"], C["s18.a"], C["s18.d"])
    escada(c, t, C["s18"], S3, els, tl, destaque=("Mg",), riscar=("Ag", "Cu", "Pb"), size=46)
    E.frase(c, t, C["s18.a"], ps("compare com o ferro:", "i", 60) + [("−0,44", "g", 58, FERRUGEM)], XE, 220, passo=0.1)
    E.foco(c, t, C["s18.c"] + 0.4, 0.4, lambda a: E.escreve(c, "o chumbo é menos negativo: fica acima", XE, 380, 52, "i", TINTA2, a))
    E.foco(c, t, C["s18.d"], 0.4, lambda a: E.pilula(c, "só o magnésio está abaixo", 560, 560, 52, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s18.e"], 0.4, lambda a: E.pilula(c, "ele se oxida; o ferro fica protegido", 560, 680, 46, "g", fundo=OXI, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s19.a"], ps("a", "i", 70) + [("ferrugem", "g", 66, FERRUGEM)] + ps("é uma pilha; o ferro é o ânodo", "i", 70)),
                     (C["s19.b"], [("sacrifício", "g", 66, COR)] + ps("= abaixo do ferro, se oxida no lugar dele", "i", 66))], 200, 420, 200, 66, 46)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("praticando", "g", 100, COR)], XE, 420)
    E.frase(c, t, C["s20.b"], [("ddp,", "g", 70), ("polos", "g", 70), ("e", "i", 74), ("proteção", "g", 70)], XE, 560, passo=0.12)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ferrugem=b_ferrugem, barreira=b_barreira, sacrificio=b_sacrificio,
              camadas=b_camadas, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
