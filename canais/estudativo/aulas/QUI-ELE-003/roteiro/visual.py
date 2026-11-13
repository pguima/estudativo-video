"""Visual — Estudativo · QUI-ELE-003: pilha de Daniell.
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha Eletroquímica (cabeçalho da QUI-ELE-001). A pilha é Q.pilha_daniell
e fica parada no centro da tela de "montagem" a "ponte"; o texto vai na faixa de cima e na de baixo. Elétrons azuis só no fio;
na ponte salina, íons negativos em cinza indo para o zinco e positivos em turquesa indo para o cobre (peça local ions_ponte,
candidata ao kit). Lâmpada no lugar do voltímetro (peça local lampada). Todo instante vem de C[...]."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Eletroquímica e Radioatividade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ELE-003_pilha_de_daniell.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("montagem", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OXI, RED = "#E08A00", Q.ELETRON
AZUL_CU, CLARO_ZN = "#6FA8DC", "#D6E4EE"

PX, PY, PW = W / 2, 590, 1100          # pilha: centro, largura
XA, XC = PX - PW * 0.32, PX + PW * 0.32
BW, BH = PW * 0.28, 300
YB = PY + 220
YTOP = YB - BH - 90
YF = YTOP - 130
assert Q.lados("Zn + Cu^2+ -> Zn^2+ + Cu")[0] == Q.lados("Zn + Cu^2+ -> Zn^2+ + Cu")[1]
assert Q.lados("Ni + 2 Ag^+ -> Ni^2+ + 2 Ag")[0] == Q.lados("Ni + 2 Ag^+ -> Ni^2+ + 2 Ag")[1]


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


def eletron(c, x, y, r=14, a=1.0):
    E.bola(c, x, y, r, Q.ELETRON, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.16))


def ion(c, x, y, r, sinal, cor, a=1.0):
    E.bola(c, x, y, r, cor, a)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(2.5, r * 0.18))
    if sinal == "+":
        M.line(c, x, y - r * 0.45, x, y + r * 0.45, BR, a, max(2.5, r * 0.18))


def lampada(c, t, cx, cy, acesa, a=1.0):
    """lâmpada pequena no lugar do voltímetro; acesa = 0..1"""
    if a <= 0:
        return
    if acesa > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), 150, [M.hexc("#FFD54A", 0.55 * acesa * a), M.hexc("#FFD54A", 0)], [0, 1]))
        c.drawCircle(cx, cy, 150, g)
    E.bola(c, cx, cy, 62, M.mix("#EDEDE8", "#FFE27A", acesa), a)
    M.rrect(c, cx - 30, cy + 52, 60, 34, 6, "#8A8D96", a)
    pth = skia.Path(); pth.moveTo(cx - 22, cy + 30); pth.lineTo(cx - 10, cy - 14); pth.lineTo(cx, cy + 10); pth.lineTo(cx + 10, cy - 14); pth.lineTo(cx + 22, cy + 30)
    c.drawPath(pth, M.paint("#6B5A2A" if acesa < 0.5 else "#C77700", a, stroke=4))


def pilha(c, t, t0, te=None, polos=False, cu=None, metais=("Zn", "Cu"), sol=("ZnSO4", "CuSO4"), cores=None, acesa=0.0):
    cor_cu = (lambda tt: Q.muda_cor(tt, cu, AZUL_CU, "#C9DCEA", 4.0)) if cu is not None else AZUL_CU
    cs = cores or (CLARO_ZN, cor_cu)
    Q.pilha_daniell(c, t, t0, PX, PY, metais, sol, te=te, ddp=" ", polos=polos, cores_sol=cs)
    if t >= t0 + 1.5:
        lampada(c, t, PX, YF, acesa, ep(t, t0 + 1.5, 0.4))


def ponte_pt(u):
    """ponto da ponte salina para u de 0 (lado do zinco) a 1 (lado do cobre), copiando a curva do kit"""
    x0, y0 = XA + BW * 0.25, YB - BH * 0.3
    x3, y3 = XC - BW * 0.25, YB - BH * 0.3
    yp = YB - BH * 0.62
    if u < 0.2:
        k = u / 0.2
        return x0, lerp(y0, yp, k)
    if u > 0.8:
        k = (u - 0.8) / 0.2
        return x3, lerp(yp, y3, k)
    k = (u - 0.2) / 0.6
    mx, my = PX, yp - 140
    return (1 - k) ** 2 * x0 + 2 * (1 - k) * k * mx + k ** 2 * x3, (1 - k) ** 2 * yp + 2 * (1 - k) * k * my + k ** 2 * yp


def ions_ponte(c, t, t0, n=4, vel=0.12):
    """negativos (cinza) andam para o zinco; positivos (turquesa) para o cobre"""
    if t < t0:
        return
    a = ep(t, t0, 0.4)
    for k in range(n):
        u = ((t - t0) * vel + k / n) % 1.0
        x, y = ponte_pt(1 - u)
        ion(c, x, y - 4, 13, "−", "#8A8D96", a)
        x, y = ponte_pt(u)
        ion(c, x, y + 4, 13, "+", E.COR, a)


def ions_saem(c, t, t0, cor, x, sinal, sobe=True, n=5):
    """íons saindo da placa para a solução (ou chegando nela)"""
    if t < t0:
        return
    for k in range(n):
        f = ((t - t0) * 0.35 + k / n) % 1.0
        dx = (40 + 150 * f) * (1 if k % 2 else -1)
        if not sobe:
            dx = (190 - 150 * f) * (1 if k % 2 else -1)
        y = YB - 60 - 45 * k
        ion(c, x + dx, y, 14, sinal, cor, ep(t, t0, 0.4) * (1 - abs(f - 0.5) * 0.6))


def topo(c, t, t0, partes, y=105):
    E.frase(c, t, t0, partes, W / 2, y, "center", 0.1)


def lista(c, t, itens, x, y0, dy, size=66, r=40):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + r, y - size * 0.38, r, a=a), centro(c, str(i + 1), x + r, y - size * 0.38 + r * 0.42, r * 1.2, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + r * 2 + 40, y, passo=0.1)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def copo():
            E.frase(c, t, C["s01.a"], ps("zinco no sulfato de cobre:", "i", 70), XE, 220, passo=0.12)
            Q.bequer(c, t, C["s01.a"], 700, 860, 380, 400, 0.72, AZUL_CU, graduacao=False)
            E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: M.rrect(c, 660, 440, 80, 400, 8, M.mix("#8C96A8", "#B5532A", ep(t, C["s01.a"] + 0.6, 2.0)), a))
            E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "a energia sai como calor", 1350, 600, 54, "g", fundo=OXI, a=a))
        E.saida(c, t, C["s01.c"] - 0.1, copo)
        if t < C["s01.c"]:
            return

        def separa():
            pilha(c, t, C["s01.c"], te=C["s01.d"], acesa=ep(t, C["s01.d"], 0.6))
            E.frase(c, t, C["s01.c"] + 0.2, ps("potes separados, ligados por um fio", "i", 62, TINTA2), W / 2, 120, "center", 0.1)
            E.frase(c, t, C["s01.d"], ps("a mesma reação", "i", 64) + [("acende uma lampadinha", "g", 60, COR)], W / 2, 1000, "center", 0.1)
        E.saida(c, t, C["s02"] - 0.1, separa)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 240, passo=0.14)
    lista(c, t, [(C["s02.b"], [("elétrons", "g", 64, RED), ("pelo", "i", 70), ("fio", "g", 64)]),
                 (C["s02.c"], [("íons", "g", 64, COR), ("pela", "i", 70), ("ponte", "g", 64)]),
                 (C["s02.d"], ps("qual placa", "i", 70) + [("se gasta", "g", 64)]),
                 (C["s02.e"], [("macete", "g", 64, COR)] + ps("do ânodo e cátodo", "i", 70))], XE, 400, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("você precisa de", "i", 76, TINTA2) + [("duas", "g", 70, COR), ("coisas", "i", 76, TINTA2)], XE, 200, passo=0.12)
    Q.formula_em(c, t, C["s03.a"], "Zn + Cu^2+ -> Zn^2+ + Cu", XE, 390, 100)
    E.foco(c, t, C["s03.a"] + 1.2, 0.4, lambda a: (E.pilula(c, "o zinco se oxida", 470, 490, 44, "g", fundo=OXI, a=a),
                                                  E.pilula(c, "o cobre se reduz", 1010, 490, 44, "g", fundo=RED, a=a)))
    E.frase(c, t, C["s03.b"], [("corrente", "g", 66, COR)] + ps("= carga andando num sentido só", "i", 66), XE, 690, passo=0.1)
    if t >= C["s03.b"] + 0.8:
        M.line(c, XE, 830, 1700, 830, TINTA, ep(t, C["s03.b"] + 0.8, 0.5), 8)
        Q.eletrons(c, t, C["s03.b"] + 1.0, [(XE, 830), (1700, 830)], 200, 150, 18)


# ---------------- montagem ----------------
def b_montagem(c, t, C, b):
    pilha(c, t, C["s04.b"])
    topo(c, t, C["s04.a"], [("pilha de Daniell,", "g", 64, COR)] + ps("de 1836", "i", 66))
    E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.pilula(c, "placa de zinco", XA, YB + 140, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s04.c"], 0.4, lambda a: E.pilula(c, "placa de cobre", XC, YB + 140, 44, "g", fundo="#B5532A", a=a))
    E.foco(c, t, C["s04.d"], 0.4, lambda a: E.pilula(c, "fio com lampadinha", PX + 330, YF, 42, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s04.e"], 0.4, lambda a: E.pilula(c, "ponte salina: água e sal", PX, YB - 20, 42, "g", fundo=E.COR, a=a))


# ---------------- elétrons ----------------
def b_eletrons(c, t, C, b):
    te = C["s05.c"]
    pilha(c, t, -10, te=te, acesa=ep(t, C["s06.e"], 0.6))
    if t < C["s06"]:
        topo(c, t, C["s05"], ps("siga os", "i", 66) + [("elétrons", "g", 62, RED)])
        ions_saem(c, t, C["s05.a"], "#8C96A8", XA, "+")
        E.foco(c, t, C["s05.a"] + 0.6, 0.4, lambda a: Q.formula(c, "Zn -> Zn^2+ + 2 e^-", XA - 60, 980, 64, TINTA, a, "center"))
        E.foco(c, t, C["s05.b"], 0.4, lambda a: (eletron(c, XA - 40, YTOP + 60, 14, a), eletron(c, XA - 40, YTOP + 110, 14, a)))
        E.frase(c, t, C["s05.c"], ps("e fogem pelo fio", "i", 60), PX + 400, 1000, "center", 0.1)
        return
    ions_saem(c, t, -10, "#8C96A8", XA, "+")
    ions_saem(c, t, C["s06.a"], AZUL_CU, XC, "+", sobe=False)
    E.foco(c, t, C["s06.a"], 0.4, lambda a: Q.formula(c, "Cu^2+ + 2 e^- -> Cu", XC + 60, 980, 64, TINTA, a, "center"))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.pilula(c, "cobre metálico na placa", XC + 320, YTOP + 70, 34, "g", fundo="#B5532A", a=a))
    topo(c, t, C["s06.c"], ps("elétrons no fio, num sentido só =", "i", 60) + [("corrente elétrica", "g", 56, COR)])


# ---------------- polos ----------------
def b_polos(c, t, C, b):
    pilha(c, t, -10, te=-10, acesa=1.0)
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "oxidação: ânodo", XA, YB + 140, 46, "g", fundo=OXI, a=a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "ânodo  −", XA - 250, YTOP + 40, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "redução: cátodo", XC, YB + 140, 46, "g", fundo=RED, a=a))
    E.foco(c, t, C["s07.d"], 0.4, lambda a: E.pilula(c, "cátodo  +", XC + 250, YTOP + 40, 44, "g", fundo=E.COR, a=a))
    if t < C["s08"]:
        topo(c, t, C["s07"], ps("cada placa tem nome", "i", 66, TINTA2))
        return
    topo(c, t, C["s08.a"], ps("elétrons: do", "i", 60) + [("ânodo", "g", 56)] + ps("para o", "i", 60) + [("cátodo", "g", 56)])
    p = ease_io(prog(t, C["s08.b"], 0.8))
    if p > 0:
        M.arrow(c, XC - 120, YF + 60, lerp(XC - 120, XA + 120, p), YF + 60, OXI, 1, 6, 22, p)
        E.foco(c, t, C["s08.b"] + 0.4, 0.4, lambda a: E.pilula(c, "corrente convencional: do + para o −", PX, YB + 225, 44, "g", fundo=OXI, a=a))


# ---------------- massa ----------------
def b_massa(c, t, C, b):
    pilha(c, t, -10, te=-10, acesa=1.0, cu=C["s09.e"])
    topo(c, t, C["s09"], ps("e as placas?", "i", 66, TINTA2))
    E.foco(c, t, C["s09.a"], 0.4, lambda a: E.pilula(c, "o zinco vira íon", XA, YB + 140, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "perde massa", XA - 260, YTOP + 160, 50, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "recebe metal", XC, YB + 140, 44, "g", fundo="#B5532A", a=a))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "ganha massa", XC + 260, YTOP + 160, 50, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s09.e"], ps("o azul clareia: o", "i", 58) + [("cobre dois mais", "g", 54, COR)] + ps("vira metal", "i", 58), W / 2, 1050, "center", 0.1)


# ---------------- ponte salina ----------------
def b_ponte(c, t, C, b):
    pilha(c, t, -10, te=-10 if t >= C["s11.d"] else None, acesa=ep(t, C["s11.d"], 0.5))
    if t < C["s11"]:
        topo(c, t, C["s10"], ps("sem a ponte, a pilha para em instantes", "i", 60, TINTA2))
        if t >= C["s10.a"]:
            for k in range(4):
                E.foco(c, t, C["s10.a"] + 0.2 * k, 0.3, lambda a, k=k: ion(c, XA - 90 + 60 * (k % 2) * 2, YB - 70 - 50 * (k // 2), 16, "+", E.COR, a))
            E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: E.pilula(c, "sobra +", XA, YB + 140, 50, "g", fundo=E.COR, a=a))
        if t >= C["s10.b"]:
            for k in range(4):
                E.foco(c, t, C["s10.b"] + 0.2 * k, 0.3, lambda a, k=k: ion(c, XC + 30 + 60 * (k % 2) * 2, YB - 70 - 50 * (k // 2), 16, "−", "#8A8D96", a))
            E.foco(c, t, C["s10.b"] + 0.6, 0.4, lambda a: E.pilula(c, "sobra −", XC, YB + 140, 50, "g", fundo="#6E6E76", a=a))
        return
    topo(c, t, C["s11.a"], ps("a ponte", "i", 64) + [("equilibra as cargas", "g", 60, COR)])
    ions_ponte(c, t, C["s11.b"])
    E.foco(c, t, C["s11.b"], 0.4, lambda a: E.pilula(c, "íons − vão ao zinco", XA, YB + 140, 44, "g", fundo="#6E6E76", a=a))
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "íons + vão ao cobre", XC, YB + 140, 44, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s11.d"], ps("soluções neutras: os elétrons", "i", 58) + [("continuam andando", "g", 54, RED)], W / 2, 1030, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    pilha(c, t, -10, te=-10, acesa=1.0)
    topo(c, t, C["s12"], [("cuidado:", "g", 66, ERRADO)] + ps("o elétron volta pela ponte?", "i", 64))

    def errado():
        if t >= C["s12.a"]:
            for k in range(3):
                u = ((t - C["s12.a"]) * 0.15 + k / 3) % 1
                x, y = ponte_pt(1 - u)
                eletron(c, x, y, 16, ep(t, C["s12.a"], 0.4))
            if t >= C["s12.a"] + 1.4:
                E.risco(c, PX - 260, YB - 240, PX + 260, YB - 140, t, C["s12.a"] + 1.4, largura=12)
        E.foco(c, t, C["s12.b"], 0.4, lambda a: E.pilula(c, "elétron não anda solto na água", PX, YB + 140, 46, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s12.c"] - 0.1, errado)
    if t < C["s12.c"]:
        return
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.pilula(c, "elétrons: só no fio", PX - 420, YF, 48, "g", fundo=RED, a=a))
    ions_ponte(c, t, C["s12.d"])
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "ponte: só íons", PX, YB + 140, 48, "g", fundo=E.COR, a=a))


# ---------------- macete (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o macete para não trocar", "i", 72, CLARO), W / 2, 190, "center", 0.12)
        for k, (tk, a1, a2, cor) in enumerate(((C["s13.a"], "Ânodo", "Oxidação", OXI), (C["s13.b"], "Cátodo", "Redução", RED))):
            y = 420 + 220 * k
            E.foco(c, t, tk, 0.4, lambda a, a1=a1, y=y, cor=cor: (E.escreve(c, a1[0], 380, y, 130, "g", cor, a), E.escreve(c, a1[1:], 380 + E.larg(a1[0], "g", 130) + 4, y, 130, "g", BR, a)))
            E.foco(c, t, tk + 0.6, 0.4, lambda a, a2=a2, y=y, cor=cor: (E.escreve(c, "e", 960, y, 90, "i", CLARO, a), E.escreve(c, a2[0], 1060, y, 130, "g", cor, a), E.escreve(c, a2[1:], 1060 + E.larg(a2[0], "g", 130) + 4, y, 130, "g", BR, a)))
        E.frase(c, t, C["s13.c"], [("vogal", "g", 70, OXI)] + ps("com vogal,", "i", 72, CLARO) + [("consoante", "g", 70, RED)] + ps("com consoante", "i", 72, CLARO), W / 2, 920, "center", 0.1)
        return
    E.frase(c, t, C["s14.a"], ps("o ânodo é sempre onde há", "i", 66, CLARO) + [("oxidação", "g", 62, BR)], W / 2, 260, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("não", "g", 62, ERRADO)] + ps("serve para o sinal:", "i", 66, CLARO), W / 2, 440, "center", 0.1)
    pilula_em(c, t, C["s14.b"] + 1.6, "na eletrólise, + e − se invertem (outra aula)", W / 2, 560, 46, "#3A3B46")
    E.frase(c, t, C["s14.c"], ps("na pilha, quem", "i", 66, CLARO) + [("manda elétrons", "g", 62, BR)] + ps("é o", "i", 66, CLARO) + [("negativo", "g", 62, CLARO)], W / 2, 760, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 150)
    if t < C["s16"]:
        pilha(c, t, C["s15.a"], metais=("Ni", "Ag"), sol=("Ni^2+", "Ag^+"), cores=("#CFE3CF", "#E4E4EA"))
        E.foco(c, t, C["s15.c"], 0.4, lambda a: E.pilula(c, "o níquel se oxida", XA - 230, YTOP + 40, 44, "g", fundo=OXI, a=a))
        perg = ((C["s15.d"], "quem é o ânodo?"), (C["s15.e"], "para onde vão os elétrons?"), (C["s15.f"], "qual placa perde massa?"), (C["s15.g"], "para onde vão os íons − da ponte?"))
        for k, (tk, s) in enumerate(perg):
            E.frase(c, t, tk, [(str(k + 1), "g", 44, COR)] + ps(s, "i", 46), 140 if k % 2 == 0 else 1000, 980 if k < 2 else 1045, passo=0.06)
        return
    E.relogio(c, t, C["s16.a"], cx=W / 2, cy=540, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    pilha(c, t, -10, te=C["s17.c"], polos=False, metais=("Ni", "Ag"), sol=("Ni^2+", "Ag^+"), cores=("#CFE3CF", "#E4E4EA"), acesa=ep(t, C["s17.c"], 0.5))
    topo(c, t, C["s17"], ps("vamos lá", "i", 64, TINTA2))
    E.foco(c, t, C["s17.a"], 0.4, lambda a: E.pilula(c, "oxidação: ânodo", XA, YB + 140, 46, "g", fundo=OXI, a=a))
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.pilula(c, "ânodo  −", XA - 250, YTOP + 40, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s17.c"] + 0.4, 0.4, lambda a: E.pilula(c, "cátodo  +", XC + 250, YTOP + 40, 44, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s17.d"], 0.4, lambda a: E.pilula(c, "perde massa", XA - 260, YTOP + 160, 48, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s17.e"], 0.4, lambda a: E.pilula(c, "ganha massa", XC + 260, YTOP + 160, 48, "g", fundo=CERTO, a=a))
    ions_ponte(c, t, C["s17.f"])
    E.foco(c, t, C["s17.f"] + 0.4, 0.4, lambda a: E.pilula(c, "íons − vão ao níquel", XC, YB + 140, 44, "g", fundo="#6E6E76", a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        lista(c, t, [(C["s18.a"], [("elétrons", "g", 66, RED)] + ps("pelo fio, do ânodo ao cátodo", "i", 70)),
                     (C["s18.b"], [("íons", "g", 66, COR)] + ps("pela ponte", "i", 70)),
                     (C["s18.c"], ps("o", "i", 70) + [("ânodo", "g", 66)] + ps("é a placa que se gasta", "i", 70))], 260, 390, 190, 66, 46)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], [("a", "i", 100), ("tensão", "g", 100, COR)], XE, 420)
    E.foco(c, t, C["s19.a"] + 0.5, 0.5, lambda a: E.escreve(c, "1,10 V", XE, 620, 170, "g", TINTA, a))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.b"] + 0.2, 0.4))
    E.frase(c, t, C["s19.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, montagem=b_montagem, eletrons=b_eletrons, polos=b_polos, massa=b_massa,
              ponte=b_ponte, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
