"""Visual — Estudativo · QUI-ELE-004: calcular a ddp e prever a reação.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha Eletroquímica (cabeçalho da QUI-ELE-001). ESCADA DE POTENCIAIS =
eixo vertical com o maior E° em cima e o hidrogênio no zero; cada degrau com o par (Q.formula) à esquerda e o valor à direita
(peça local escada(), candidata ao kit). A ddp é a cota vertical entre dois degraus (peça local cota()). Íon de cima reagindo
com o metal de baixo = seta turquesa descendo; o contrário = seta riscada. Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-004_ddp_e_prever_a_reacao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("volt", "potencial", "prever", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON

POT = {"Ag": 0.80, "Cu": 0.34, "H": 0.00, "Fe": -0.44, "Zn": -0.76, "Mg": -2.37}
PAR = {"Ag": "Ag^+/Ag", "Cu": "Cu^2+/Cu", "H": "H^+/H2", "Fe": "Fe^2+/Fe", "Zn": "Zn^2+/Zn", "Mg": "Mg^2+/Mg"}
r2 = lambda v: round(v, 2)
assert r2(POT["Cu"] - POT["Zn"]) == 1.10 and r2(POT["Ag"] - POT["Zn"]) == 1.56
assert r2(POT["Cu"] - POT["Fe"]) == 0.78 and r2(POT["Zn"] - POT["Cu"]) == -1.10
assert r2(POT["Zn"] + POT["Cu"]) == -0.42 and r2(POT["Cu"] - POT["Mg"]) == 2.71 and r2(POT["Cu"] - POT["Ag"]) == -0.46


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


def v_br(v, sinal=True):
    s = f"{abs(v):.2f}".replace(".", ",")
    return ("+" if v > 0 else "−" if v < 0 else "") + s if sinal else s


class Escada:
    def __init__(self, x, y0, y1, vmin, vmax):
        self.x, self.y0, self.y1, self.vmin, self.vmax = x, y0, y1, vmin, vmax

    def y(self, v):
        return lerp(self.y1, self.y0, (v - self.vmin) / (self.vmax - self.vmin))


def escada(c, t, t0, S, els, tl=None, destaque=(), escuro=False, size=56):
    """eixo vertical de E° com um degrau por elemento; destaque = elementos na cor da matéria"""
    tinta = BR if escuro else TINTA
    p = ep(t, t0, 0.6)
    if p <= 0:
        return
    M.arrow(c, S.x, S.y1 + 30, S.x, lerp(S.y1 + 30, S.y0 - 40, p), TINTA2 if not escuro else "#C8CAD2", 1, 5, 22, p)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, "E° (V)", S.x - 60, S.y0 - 70, 40, "b", TINTA2 if not escuro else CLARO, a))
    for k, el in enumerate(els):
        tk = (tl[k] if tl else t0 + 0.4 + 0.25 * k)
        v = POT[el]
        y = S.y(v)
        dest = el in destaque
        cor = (E.CLARO if escuro else E.COR) if dest else (tinta if el != "H" else TINTA2)

        def deg(a, y=y, el=el, v=v, cor=cor, dest=dest):
            M.line(c, S.x - 40, y, S.x + 40, y, cor, a, 8 if dest else 5)
            Q.formula(c, PAR[el], S.x - 70, y + size * 0.34, size, cor, a, "right")
            E.escreve(c, v_br(v) if v else "0,00", S.x + 70, y + size * 0.34, size, "g", cor, a)
        E.foco(c, t, tk, 0.4, deg)


def cota(c, t, t0, S, v_hi, v_lo, rot, dx=320, cor=None, size=60):
    """seta dupla vertical entre dois degraus com o valor ao lado: a ddp"""
    cor = cor or E.COR
    p = ease_io(prog(t, t0, 0.7))
    if p <= 0:
        return
    x = S.x + dx
    ya, yb = S.y(v_hi), S.y(v_lo)
    M.line(c, S.x + 250, ya, x + 20, ya, cor, 0.5, 3)
    M.line(c, S.x + 250, yb, x + 20, yb, cor, 0.5, 3)
    ym = (ya + yb) / 2
    M.arrow(c, x, ym, x, lerp(ym, ya, p), cor, 1, 7, 24, p)
    M.arrow(c, x, ym, x, lerp(ym, yb, p), cor, 1, 7, 24, p)
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.pilula(c, rot, x + 30 + E.larg(rot, "g", size) / 2 + size * 0.6, ym, size, "g", fundo=cor, a=a))


def seta_reage(c, t, t0, S, el_ion, el_met, x, ok=True):
    """seta curva do íon para o metal: reage (turquesa) ou não (riscada)"""
    p = ease_io(prog(t, t0, 0.7))
    if p <= 0:
        return
    ya, yb = S.y(POT[el_ion]), S.y(POT[el_met])
    pth = skia.Path(); pth.moveTo(x, ya); pth.cubicTo(x - 160, ya, x - 160, yb, x, yb)
    me = skia.PathMeasure(pth, False)
    parte = skia.Path(); me.getSegment(0, me.getLength() * p, parte, True)
    cor = E.COR if ok else ERRADO
    c.drawPath(parte, M.paint(cor, 1, stroke=7))
    if p > 0.95:
        d = 1 if yb > ya else -1
        M.line(c, x, yb, x - 26, yb - d * 14, cor, 1, 7)
        M.line(c, x, yb, x - 18, yb + d * 22, cor, 1, 7)
    if not ok and t >= t0 + 0.8:
        E.risco(c, x - 190, (ya + yb) / 2 + 60, x - 40, (ya + yb) / 2 - 60, t, t0 + 0.8, largura=10)


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


def conta(c, t, t0, s, x, y, size, cor=TINTA, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, "g", cor, align)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def s01():
            for k, (met, tk, v, x) in enumerate((("Cu", C["s01.a"], "1,10 V", 560), ("Ag", C["s01.c"], "1,56 V", 1360))):
                E.foco(c, t, tk, 0.5, lambda a, met=met, x=x: (Q.formula(c, "Zn | " + met, x, 330, 110, TINTA, a, "center")))
                tv = C["s01.b"] if k == 0 else C["s01.d"]
                E.foco(c, t, tv, 0.5, lambda a, x=x, v=v: (E.bola(c, x, 560, 150, "#22232B", a), c.drawCircle(x, 560, 150, M.paint(E.COR, a, stroke=8)), centro(c, v, x, 590, 84, "g", BR, a)))
            E.frase(c, t, C["s01.e"], ps("dá para prever", "i", 76) + [("sem montar nada?", "g", 70, COR)], W / 2, 900, "center", 0.12)
        E.saida(c, t, C["s02"] - 0.1, s01)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], ps("calcular a", "i", 70) + [("ddp", "g", 64, COR)] + ps("de uma pilha", "i", 70)),
                 (C["s02.c"], ps("prever se a reação", "i", 70) + [("acontece sozinha", "g", 64)]),
                 (C["s02.d"], [("atalho", "g", 64, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("três", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    lista(c, t, [(C["s03.a"], [("ânodo", "g", 62, OXI)] + ps("se oxida e manda elétrons ao", "i", 62) + [("cátodo", "g", 62, RED)]),
                 (C["s03.b"], [("volt", "g", 62, COR)] + ps("= joule por coulomb", "i", 62)),
                 (C["s03.c"], ps("subtrair negativo é somar:", "i", 62))], XE, 400, 190, 62, 42)
    E.foco(c, t, C["s03.c"] + 1.0, 0.4, lambda a: E.formula(c, "3 − (−2) = 3 + 2", 1110, 780, 64, "g", COR, a))


# ---------------- o volt ----------------
def b_volt(c, t, C, b):
    E.frase(c, t, C["s04"], ps("o número do aparelho", "i", 66, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s04.a"], [("ddp", "g", 90, COR)] + ps("= diferença de potencial, a tensão", "i", 64), XE, 340, passo=0.1)
    E.foco(c, t, C["s04.b"], 0.5, lambda a: E.escreve(c, "1,10 V", XE, 560, 160, "g", TINTA, a))
    E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.formula(c, "= 1,10 J por coulomb", XE + 620, 545, 70, "g", TINTA2, a))
    # um coulomb de carga levando energia pelo fio
    if t >= C["s04.c"]:
        M.line(c, XE, 820, 1750, 820, TINTA, ep(t, C["s04.c"], 0.4), 7)
        u = ease_io(prog(t, C["s04.c"] + 0.3, 3.0))
        x = lerp(XE + 60, 1690, u)
        E.foco(c, t, C["s04.c"] + 0.2, 0.4, lambda a: (E.bola(c, x, 820, 48, Q.ELETRON, a), centro(c, "1 C", x, 834, 34, "g", BR, a)))
        E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "+1,10 J", x, 730, 50, "g", fundo=OXI, a=a))
    E.frase(c, t, C["s04.d"] + 1.2, ps("mais ddp,", "i", 60) + [("mais energia por carga", "g", 56, COR)], W / 2, 980, "center", 0.1)


# ---------------- potencial ----------------
S1 = Escada(1300, 220, 900, -0.9, 0.9)


def b_potencial(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05"], ps("de onde vem o número?", "i", 66, TINTA2), XE, 200, passo=0.12)
        E.frase(c, t, C["s05.a"], ps("cada íon tem uma", "i", 66) + [("vontade", "g", 62, COR)] + ps("de receber elétrons", "i", 66), XE, 360, passo=0.1)
        Q.formula_em(c, t, C["s05.a"] + 1.4, "Cu^2+ + 2 e^- -> Cu", XE + 60, 540, 100)
        E.frase(c, t, C["s05.b"], ps("medida em volt:", "i", 66), XE, 740, passo=0.1)
        E.frase(c, t, C["s05.c"], [("potencial padrão de redução,", "g", 60, COR)], XE, 850)
        E.foco(c, t, C["s05.c"] + 1.2, 0.4, lambda a: E.formula(c, "E°", XE + 1120, 860, 110, "g", COR, a))
        E.foco(c, t, C["s05.c"] + 2.0, 0.4, lambda a: E.escreve(c, "medido nas condições fixas da tabela", XE, 940, 46, "i", TINTA2, a))
        return
    els = ("Ag", "Cu", "H", "Zn")
    tl = (C["s06.c"], C["s06.b"], C["s06.a"], C["s06.d"])
    escada(c, t, C["s06"], S1, els, tl, destaque=("Cu", "Zn") if t >= C["s07"] else ())
    if t < C["s07"]:
        E.frase(c, t, C["s06"], ps("pense numa", "i", 66) + [("escada", "g", 62, COR)], XE, 200, passo=0.12)
        p = ep(t, C["s06.e"], 0.5)
        if p > 0:
            M.arrow(c, 300, 820, 300, lerp(820, 330, ease_io(p)), E.COR, 1, 10, 32, ease_io(p))
            E.foco(c, t, C["s06.e"] + 0.5, 0.4, lambda a: (E.escreve(c, "mais alto:", 360, 450, 56, "i", TINTA, a), E.escreve(c, "mais vontade", 360, 530, 56, "g", COR, a), E.escreve(c, "de receber", 360, 600, 56, "i", TINTA, a)))
        return
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "maior: recebe, se reduz, cátodo", 520, S1.y(0.34), 44, "g", fundo=RED, a=a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "menor: se oxida, ânodo", 520, S1.y(-0.76), 44, "g", fundo=OXI, a=a))
    E.frase(c, t, C["s07.c"], ps("por isso o zinco se gastava", "i", 56, TINTA2), XE, 1020, passo=0.1)


# ---------------- ddp ----------------
def b_ddp(c, t, C, b):
    els = ("Ag", "Cu", "H", "Zn")
    escada(c, t, -10, S1, els, destaque=("Cu", "Zn") if t < C["s09"] else ("Ag", "Zn"))
    if t < C["s09"]:
        cota(c, t, C["s08.a"], S1, 0.34, -0.76, "1,10 V", 270)
        E.frase(c, t, C["s08.a"], ps("ddp = a distância na escada", "i", 60), XE, 200, passo=0.1)
        conta(c, t, C["s08.b"], "ddp = E°maior − E°menor", XE, 420, 56, TINTA)
        conta(c, t, C["s08.c"], "0,34 − (−0,76)", XE, 560, 66, TINTA2)
        conta(c, t, C["s08.e"], "= 0,34 + 0,76", XE, 680, 66, TINTA2)
        conta(c, t, C["s08.f"], "= 1,10 V", XE, 810, 80, COR)
        return
    cota(c, t, C["s09.a"], S1, 0.80, -0.76, "1,56 V", 270)
    E.frase(c, t, C["s09.a"], ps("com a prata no lugar do cobre", "i", 60), XE, 200, passo=0.1)
    conta(c, t, C["s09.b"], "0,80 + 0,76", XE, 560, 70, TINTA2)
    conta(c, t, C["s09.c"], "= 1,56 V", XE, 690, 80, COR)
    E.frase(c, t, C["s09.d"], ps("mais alto, mais distância", "i", 56, TINTA2), XE, 900, passo=0.1)


# ---------------- prever ----------------
S2 = Escada(1250, 260, 880, -0.9, 0.9)


def b_prever(c, t, C, b):
    els = ("Cu", "H", "Fe", "Zn")
    if t < C["s12"]:
        escada(c, t, C["s10"], S2, els, destaque=("Cu", "Fe"))
        E.frase(c, t, C["s10.a"], ps("acontece", "i", 66) + [("sozinha?", "g", 62, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s10.b"], ps("prego de ferro no", "i", 60) + [("sulfato de cobre", "g", 56)], XE, 320, passo=0.1)
        seta_reage(c, t, C["s10.e"], S2, "Cu", "Fe", S2.x - 330, True)
        E.foco(c, t, C["s10.f"], 0.4, lambda a: E.pilula(c, "o íon arranca elétrons do ferro", 560, 980, 46, "g", fundo=E.COR, a=a))
        if t >= C["s11"]:
            conta(c, t, C["s11.a"], "E°(recebe) − E°(perde)", XE, 480, 50, TINTA)
            conta(c, t, C["s11.b"], "0,34 + 0,44 = 0,78", XE, 590, 62, TINTA2)
            E.foco(c, t, C["s11.d"], 0.4, lambda a: (E.pilula(c, "positivo: acontece", 360, 700, 46, "g", fundo=CERTO, a=a)))
        return
    escada(c, t, -10, S2, els, destaque=("Cu", "Zn"))
    E.frase(c, t, C["s12.a"], ps("fio de cobre no", "i", 60) + [("sulfato de zinco", "g", 56)], XE, 200, passo=0.1)
    seta_reage(c, t, C["s12.b"], S2, "Zn", "Cu", S2.x - 330, False)
    conta(c, t, C["s12.c"], "−0,76 − 0,34", XE, 480, 62, TINTA2)
    conta(c, t, C["s12.d"], "= −1,10", XE, 590, 70, ERRADO)
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.pilula(c, "negativo: nada acontece", 380, 700, 46, "g", fundo=ERRADO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("somar como está na tabela", "i", 64), XE + 450, 190, passo=0.1)

    def errado():
        conta(c, t, C["s13.b"], "−0,76 + 0,34", W / 2, 420, 90, ERRADO, "center")
        conta(c, t, C["s13.c"], "= −0,42 V", W / 2, 560, 90, ERRADO, "center")
        if t >= C["s13.c"] + 1.0:
            E.risco(c, W / 2 - 330, 590, W / 2 + 330, 340, t, C["s13.c"] + 1.0, largura=12)
    E.saida(c, t, C["s13.e"] - 0.1, errado)
    E.frase(c, t, C["s13.d"], ps("pilha que funciona:", "i", 62) + [("ddp positiva", "g", 58, COR)], W / 2, 720, "center", 0.1)
    if t >= C["s13.e"]:
        conta(c, t, C["s13.e"], "0,34 − (−0,76) = 1,10 V", W / 2, 470, 90, TINTA, "center")
        E.foco(c, t, C["s13.e"] + 0.6, 0.4, lambda a: E.selo(c, W / 2 + 600, 440, 50, True, a))
    E.frase(c, t, C["s13.e"] + 1.4, ps("o negativo só aparece numa reação que", "i", 54, TINTA2) + [("não acontece", "g", 50)], W / 2, 860, "center", 0.08)


# ---------------- atalho (palco) ----------------
S3 = Escada(1520, 250, 880, -0.9, 0.9)


def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 72, CLARO), XE, 170, passo=0.12)
        escada(c, t, C["s14.a"], S3, ("Ag", "Cu", "H", "Fe", "Zn"), escuro=True, destaque=("Cu", "Zn"))
        E.frase(c, t, C["s14.b"], ps("o íon de", "i", 56, CLARO) + [("cima", "g", 52, BR)] + ps("reage com o metal de", "i", 56, CLARO) + [("baixo", "g", 52, BR)], XE, 330, passo=0.1)
        if t >= C["s14.b"]:
            p = ease_io(prog(t, C["s14.b"] + 0.4, 0.8))
            M.arrow(c, S3.x - 360, S3.y(0.34), S3.x - 360, lerp(S3.y(0.34), S3.y(-0.76), p), E.CLARO, 1, 9, 28, p)
        E.frase(c, t, C["s14.c"], ps("o contrário,", "i", 62, CLARO) + [("nunca", "g", 58, ERRADO)], XE, 450, passo=0.1)
        E.frase(c, t, C["s14.d"], ps("um positivo, um negativo:", "i", 56, CLARO), XE, 640, passo=0.1)
        E.frase(c, t, C["s14.d"] + 1.6, [("some os números", "g", 58, BR)] + ps("sem o sinal", "i", 60, CLARO), XE, 730, passo=0.1)
        E.foco(c, t, C["s14.d"] + 2.4, 0.4, lambda a: E.formula(c, "0,34 + 0,76 = 1,10", XE, 850, 62, "g", E.CLARO, a))
        return
    E.frase(c, t, C["s15.a"], ps("o íon de cima tem mais", "i", 62, CLARO) + [("vontade de receber", "g", 58, BR)], W / 2, 320, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 60, ERRADO), ("compensa", "i", 62, CLARO)] + ps("se a tabela der potenciais de oxidação:", "i", 62, CLARO), W / 2, 560, "center", 0.1)
    pilula_em(c, t, C["s15.c"], "troque o sinal de todos antes", W / 2, 700, 52, E.COR)


# ---------------- questão ----------------
S4 = Escada(1350, 230, 900, -2.6, 1.0)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: (Q.formula(c, "Mg^2+/Mg", XE, 330, 80, TINTA, a), E.escreve(c, "= −2,37 V", XE + 420, 330, 80, "g", COR, a)))
    E.frase(c, t, C["s16.b"], [("1", "g", 56, COR)] + ps("ddp da pilha de magnésio e cobre?", "i", 58), XE, 500, passo=0.08)
    E.frase(c, t, C["s16.b"] + 1.6, ps("quem é o ânodo?", "i", 58), XE + 60, 590, passo=0.08)
    E.frase(c, t, C["s16.c"], [("2", "g", 56, COR)] + ps("anel de prata reage com sulfato de cobre?", "i", 58), XE, 720, passo=0.08)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1500, cy=520, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s19"]:
        escada(c, t, C["s18"], S4, ("Cu", "H", "Mg"), destaque=("Cu", "Mg"), size=50)
        cota(c, t, C["s18.a"], S4, 0.34, -2.37, "2,71 V", 230, size=54)
        E.frase(c, t, C["s18.a"], ps("um positivo, um negativo:", "i", 58), XE, 220, passo=0.1)
        conta(c, t, C["s18.b"], "0,34 + 2,37", XE, 380, 70, TINTA2)
        conta(c, t, C["s18.c"], "= 2,71 V", XE, 500, 80, COR)
        E.foco(c, t, C["s18.d"], 0.4, lambda a: E.pilula(c, "magnésio embaixo: ânodo", 470, 640, 46, "g", fundo=OXI, a=a))
        return
    escada(c, t, -10, S2, ("Ag", "Cu", "H"), destaque=("Ag", "Cu"))
    E.frase(c, t, C["s19.a"], ps("a prata está", "i", 60) + [("acima", "g", 56, COR)] + ps("do cobre", "i", 60), XE, 220, passo=0.1)
    seta_reage(c, t, C["s19.b"], S2, "Cu", "Ag", S2.x - 330, False)
    conta(c, t, C["s19.c"], "0,34 − 0,80", XE, 420, 66, TINTA2)
    conta(c, t, C["s19.d"], "= −0,46", XE, 530, 74, ERRADO)
    E.foco(c, t, C["s19.e"], 0.4, lambda a: E.pilula(c, "o anel não reage", 420, 660, 50, "g", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s20.a"], [("ddp", "g", 66, COR)] + ps("= maior potencial − menor", "i", 70)),
                     (C["s20.b"], ps("o íon de", "i", 70) + [("cima", "g", 66)] + ps("reage com o metal de", "i", 70) + [("baixo", "g", 66)])], 260, 420, 200, 66, 46)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("pilha alcalina", "g", 96, COR)], XE, 420)
    E.frase(c, t, C["s21.a"] + 0.5, [("e", "i", 96), ("bateria do carro", "g", 96, COR)], XE, 550)
    E.frase(c, t, C["s21.b"], ps("por que uma recarrega?", "i", 70), XE, 700, passo=0.12)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, volt=b_volt, potencial=b_potencial, ddp=b_ddp, prever=b_prever,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
