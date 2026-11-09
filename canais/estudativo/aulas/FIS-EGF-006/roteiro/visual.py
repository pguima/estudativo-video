"""Visual — Estudativo · FIS-EGF-006: princípio de Pascal: prensa hidráulica.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-006_principio_de_pascal_prensa_hidraulica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("principio", "prensa", "preco", "atalho", "questao", "fim"))

# todas as contas da aula
assert 10_000 / 1_000 * 10 == 100 and 1_000 / 10 * 1 == 100  # F1 = 100 N; o pistão fino desce 100 cm
assert 1_000 / 20 == 50 and 12_000 / 50 == 240 and 4 * 50 == 200 and (10 / 1) ** 2 == 100 and (3 / 1) ** 2 == 9


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
PISTAO = "#2A2A30"


def prensa(c, x1, w1, x2, w2, yb, n1, n2, a=1.0, carro=None, canal=70):
    """prensa hidráulica: cilindro fino centrado em x1 (largura w1) e largo em x2 (w2), ligados no fundo yb.
    n1, n2 = altura do óleo (px acima do fundo) em cada cilindro; desenha os pistões no nível do óleo. Devolve (y1, y2) dos pistões"""
    if a <= 0:
        return yb - n1, yb - n2
    oleo = M.paint(OLEO, 0.6 * a)
    y1, y2 = yb - n1, yb - n2
    c.drawRect(skia.Rect.MakeLTRB(x1 - w1 / 2, y1, x1 + w1 / 2, yb), oleo)
    c.drawRect(skia.Rect.MakeLTRB(x2 - w2 / 2, y2, x2 + w2 / 2, yb), oleo)
    c.drawRect(skia.Rect.MakeLTRB(x1 + w1 / 2, yb - canal, x2 - w2 / 2, yb), oleo)
    top = yb - 560
    p = skia.Path()
    p.moveTo(x1 - w1 / 2, top); p.lineTo(x1 - w1 / 2, yb); p.lineTo(x2 + w2 / 2, yb); p.lineTo(x2 + w2 / 2, top)
    p.moveTo(x1 + w1 / 2, top); p.lineTo(x1 + w1 / 2, yb - canal); p.lineTo(x2 - w2 / 2, yb - canal); p.lineTo(x2 - w2 / 2, top)
    c.drawPath(p, M.paint(TINTA, a, stroke=6))
    M.rrect(c, x1 - w1 / 2 + 4, y1 - 22, w1 - 8, 22, 4, PISTAO, a)
    M.rrect(c, x2 - w2 / 2 + 4, y2 - 26, w2 - 8, 26, 4, PISTAO, a)
    if carro:
        F.bloco(c, x2, y2 - 26 - 70, w2 * 0.8, 140, carro, a=a, size=40)
    return y1, y2


def garrafa(c, cx, cy, a=1.0, aperto=0.0):
    if a <= 0:
        return
    w = 200 - 30 * aperto
    p = skia.Path()
    p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - 180, w, 400), 60, 60))
    c.drawPath(p, M.paint(AGUA, 0.5 * a))
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    M.rrect(c, cx - 40, cy - 250, 80, 80, 14, TINTA, a)


PX1, PW1, PX2, PW2, PYB = 900, 90, 1450, 420, 900


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            sobe = 60 * ease_io(prog(t, C["s01.a"] + 0.6, 1.6))
            q = ep(t, C["s01.a"], 0.5)
            prensa(c, PX1, PW1, PX2, PW2, PYB, 330 - sobe * 4, 230 + sobe, q, carro="carro" if t >= C["s01.a"] else None)
            F.forca(c, t, C["s01.b"], (PX1, PYB - 330 + sobe * 4 - 200), -90, 170, None)
            E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: E.pilula(c, "100 N", PX1 - 170, PYB - 330 + sobe * 4 - 120, 44, "g", fundo=E.COR, a=a))
            E.foco(c, t, C["s01.c"], 0.4, lambda a: E.pilula(c, "10.000 N", PX2, PYB - 230 - sobe - 220, 44, "g", fundo=TINTA, a=a))
            E.frase(c, t, C["s01.a"], ps("elevador de oficina:", "i", 62) + [("1 tonelada", "g", 62, COR)], XE, 190, passo=0.1)
            E.frase(c, t, C["s01.c"], [("100 vezes", "g", 70, COR)] + ps("menos força", "i", 70), XE, 300, passo=0.12)
            pilula_em(c, t, C["s01.d"], "um líquido preso num tubo", 1180, 1010, 48, E.COR)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "a força na prensa"), ("s02.b", "o preço do ganho")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "pressão:", "força ÷ área"), ("s03.c", "Stevin:", "mesma altura, mesma pressão")), 2)


# ---------------- o princípio ----------------
def b_principio(c, t, C, b):
    cx, cy = 1350, 600
    aperto = ease_io(prog(t, C["s04.b"] - 0.4, 0.6))
    E.foco(c, t, C["s04.a"], 0.5, lambda a: garrafa(c, cx, cy, a, aperto))
    if t >= C["s04.b"] - 0.4:
        F.seta(c, cx - 360, cy, cx - 125, cy, TINTA, ep(t, C["s04.b"] - 0.4, 0.4), 12)
        F.seta(c, cx + 360, cy, cx + 125, cy, TINTA, ep(t, C["s04.b"] - 0.4, 0.4), 12)
    q = ep(t, C["s04.c"], 0.6)
    if q > 0:
        for i in range(10):
            g = 2 * math.pi * i / 10
            ux, uy = math.cos(g) * 0.6, math.sin(g)
            n = math.hypot(ux, uy)
            ux, uy = ux / n, uy / n
            F.seta(c, cx + ux * 25, cy + 20 + uy * 40, cx + ux * 90, cy + 20 + uy * 150, E.COR, q, 7, cabeca=20, p=q)
    E.frase(c, t, C["s04.a"], ps("aperte uma garrafa", "i", 64) + [("fechada", "g", 64)], XE, 190, passo=0.12)
    E.frase(c, t, C["s04.c"], ps("o aumento de pressão chega", "i", 56) + [("a todo o líquido", "g", 56, COR)], XE, 300, passo=0.1)
    E.frase(c, t, C["s04.d"], [("princípio de Pascal:", "g", 62, COR)], XE, 820)
    E.frase(c, t, C["s04.e"], ps("o aumento de pressão se transmite", "i", 56) + [("inteiro", "g", 56, COR)], XE, 920, passo=0.1)


# ---------------- a prensa ----------------
def b_prensa(c, t, C, b):
    if t < C["s07"]:
        def s0506():
            q = ep(t, C["s05.a"], 0.5)
            prensa(c, PX1, PW1, PX2, PW2, PYB, 330, 230, q)
            E.foco(c, t, C["s05.b"], 0.4, lambda a: centro(c, "óleo", PX2, PYB - 60, 44, "b", "#9A6B10", a))
            E.foco(c, t, C["s05.c"], 0.4, lambda a: E.escreve(c, "pistão", PX2 + PW2 / 2 + 20, PYB - 240, 46, "i", TINTA, a))
            pilula_em(c, t, C["s05.d"], "fino: A₁", PX1, PYB + 60, 44, TINTA)
            pilula_em(c, t, C["s05.e"], "largo: A₂", PX2, PYB + 60, 44, TINTA)
            if t < C["s06"]:
                E.frase(c, t, C["s05.a"], [("prensa hidráulica", "g", 70, COR)], XE, 190)
                E.frase(c, t, C["s05.b"], ps("dois cilindros ligados,", "i", 58) + [("cheios de óleo", "g", 56)], XE, 290, passo=0.1)
                return
            F.forca(c, t, C["s06.a"], (PX1, PYB - 330 - 220), -90, 170, "F₁", lado=-1)
            E.foco(c, t, C["s06.b"], 0.4, lambda a: E.formula(c, "p = f{F₁}{A₁}", PX1 - 330, PYB - 200, 64, "g", COR, a))
            if t >= C["s06.c"]:
                for i in range(5):
                    x = lerp(PX1 + 80, PX2 - 160, i / 4)
                    F.seta(c, x, PYB - 35, x + 70, PYB - 35, E.COR, ep(t, C["s06.c"] + 0.1 * i, 0.4), 6, cabeca=16)
            F.forca(c, t, C["s06.d"], (PX2, PYB - 230 - 26), 90, 200, "F₂", lado=-1)
            E.foco(c, t, C["s06.d"], 0.4, lambda a: E.formula(c, "p = f{F₂}{A₂}", PX2 + 120, PYB - 420, 64, "g", COR, a))
            E.formula_em(c, t, C["s06.e"], "f{F₁}{A₁} = f{F₂}{A₂}", XE, 260, 120, "g", TINTA)
        E.saida(c, t, C["s07"] - 0.1, s0506)
        return
    if t < C["s08"]:
        def s07():
            E.formula_em(c, t, C["s07"], "f{F₁}{A₁} = f{F₂}{A₂}", XE, 260, 120, "g", TINTA)
            E.frase(c, t, C["s07.a"], [("F₁, F₂:", "g", 60, COR)] + ps("as forças, em newtons", "i", 62), XE, 470, passo=0.1)
            E.frase(c, t, C["s07.b"], [("A₁, A₂:", "g", 60, COR)] + ps("as áreas dos pistões", "i", 62), XE, 570, passo=0.1)
            E.frase(c, t, C["s07.c"], ps("igualdade de razões:", "i", 62), XE, 740, passo=0.1)
            E.frase(c, t, C["s07.d"], [("não converta a área:", "g", 60, CERTO)] + ps("mesma unidade dos dois lados", "i", 60), XE, 840, passo=0.1)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    q = ep(t, C["s08"], 0.5)
    prensa(c, PX1 + 380, PW1, PX2 + 250, PW2 - 60, PYB, 330, 230, q, carro="10.000 N")
    E.foco(c, t, C["s08.a"], 0.4, lambda a: E.pilula(c, "1.000 cm²", PX2 + 250, PYB + 50, 40, "b", fundo=TINTA, a=a))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "10 cm²", PX1 + 380, PYB + 50, 40, "b", fundo=TINTA, a=a))
    linhas(c, t, [(C["s08.c"], "f{F₁}{10} = f{10.000}{1.000}", TINTA), (C["s08.d"], "f{F₁}{10} = 10", TINTA)], XE, 260, 220, 84)
    bola_txt(c, t, C["s08.e"], "F₁ = 100 N", 420, 760, 150, 52, CERTO)
    E.frase(c, t, C["s08.f"], [("área × 100", "g", 60), ("→", "g", 56, TINTA2), ("força × 100", "g", 60, COR)], XE, 1010, passo=0.12)


# ---------------- o preço ----------------
def b_preco(c, t, C, b):
    desce = ease_io(prog(t, C["s09.b"], 2.0)) if t < C["s10"] else 1.0
    q = ep(t, C["s09"], 0.5)
    y1, y2 = prensa(c, PX1 + 300, PW1, PX2 + 150, PW2, PYB, 380 - 240 * desce, 230 + 240 * desce * (PW1 / PW2) ** 1, q, carro="carro")
    if t >= C["s09.b"]:
        pilula_em(c, t, C["s09.b"] + 1.6, "fino: desce muito", PX1 + 300, PYB + 60, 40, E.COR)
        pilula_em(c, t, C["s09.b"] + 1.8, "largo: sobe pouco", PX2 + 150, PYB + 60, 40, TINTA)
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("ninguém ganha força", "i", 64) + [("de graça", "g", 64, COR)], XE, 190, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("o óleo que sai do fino", "i", 54) + [("entra no largo", "g", 54)], XE, 290, passo=0.1)
        E.frase(c, t, C["s09.c"], [("mesmo volume", "g", 60, COR)], XE, 390)
        E.formula_em(c, t, C["s09.d"], "V = A · deslocamento", XE, 520, 64, "g", TINTA)
        E.frase(c, t, C["s09.e"], [("área × 100", "g", 56), ("→", "g", 54, TINTA2), ("desloc. ÷ 100", "g", 56, COR)], XE, 640, passo=0.12)
        return
    E.frase(c, t, C["s10.a"], ps("carro sobe", "i", 60) + [("1 cm", "g", 60, COR)], XE, 190, passo=0.12)
    E.frase(c, t, C["s10.b"], ps("pistão fino desce", "i", 60) + [("100 cm", "g", 60, COR)], XE, 290, passo=0.12)
    E.frase(c, t, C["s10.c"], [("força ganha", "g", 60)] + ps("cobra em", "i", 62) + [("distância", "g", 60, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s10.d"], [("força ÷ 100,", "g", 56), ("caminho × 100", "g", 56, COR)], XE, 550, passo=0.12)
    E.frase(c, t, C["s10.e"], ps("por isso, tantas bombadas", "i", 58, TINTA2), XE, 700, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("pressão maior no pistão largo?", "i", 62), XE + 480, 190, passo=0.1)
    if t >= C["s11.b"]:
        E.risco(c, XE + 470, 205, XE + 1300, 150, t, C["s11.b"], largura=10)
    q = ep(t, C["s11.a"], 0.5)
    prensa(c, PX1, PW1, PX2, PW2, PYB, 330, 230, q)
    for x, w, y in ((PX1, PW1, PYB - 330), (PX2, PW2, PYB - 230)):
        if t >= C["s11.b"]:
            n = 2 if w < 200 else 7
            for i in range(n):
                xx = x - w / 2 + (i + 0.5) * w / n
                F.seta(c, xx, y + 10, xx, y + 80, E.COR, ep(t, C["s11.b"], 0.4), 6, cabeca=16)
    E.foco(c, t, C["s11.b"], 0.4, lambda a: (E.pilula(c, "mesma p", PX1, PYB - 450, 40, "g", fundo=E.COR, a=a),
                                              E.pilula(c, "mesma p", PX2, PYB - 450, 40, "g", fundo=E.COR, a=a)))
    E.frase(c, t, C["s11.c"], ps("força maior porque a", "i", 56) + [("área é maior", "g", 56, COR)], XE, 330, passo=0.1)
    E.frase(c, t, C["s11.d"], ps("quem multiplica a força é a", "i", 56) + [("área", "g", 60, COR)], XE, 1010, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.formula_em(c, t, C["s12.a"], "ganho = f{A₂}{A₁}", W / 2, 360, 110, "g", BR, "center")
            E.frase(c, t, C["s12.b"], [("× a força,", "g", 64, BR), ("÷ o deslocamento", "g", 64, CLARO)], W / 2, 540, "center", 0.15)
            E.frase(c, t, C["s12.c"], ps("deu o", "i", 66, CLARO) + [("diâmetro?", "g", 66, BR)] + ps("eleve ao quadrado", "i", 66, CLARO), W / 2, 720, "center", 0.12)
            E.formula_em(c, t, C["s12.d"], "D × 10  →  A × 100", W / 2, 900, 96, "g", BR, "center")
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], ps("a área cresce com o", "i", 66, CLARO) + [("quadrado do diâmetro", "g", 64, BR)], W / 2, 300, "center", 0.1)
    for i, (r, s) in enumerate(((50, "D"), (150, "3D"))):
        x = 760 + i * 420
        q = ep(t, C["s13.a"] + 0.5 * i, 0.5)
        if q > 0:
            c.drawCircle(x, 560, r, M.paint(CLARO, 0.5 * q))
            c.drawCircle(x, 560, r, M.paint(BR, q, stroke=4))
            centro(c, s, x, 760, 50, "g", BR, q)
    E.foco(c, t, C["s13.a"] + 1.2, 0.4, lambda a: centro(c, "área × 9", 1500, 580, 64, "g", CLARO, a))
    E.frase(c, t, C["s13.b"], [("erro:", "g", 62, ERRADO)] + ps("usar 10 em vez de 100", "i", 64, CLARO), W / 2, 930, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s14")
    E.frase(c, t, C["s14.a"], [("pistão pequeno:", "i", 60), ("20 cm²", "g", 60, COR)], XE, 320, passo=0.12)
    E.frase(c, t, C["s14.b"], [("grande:", "i", 60), ("1.000 cm²", "g", 60, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s14.c"], [("carro", "i", 62), ("12.000 N:", "g", 62), ("força?", "g", 62, COR)], XE, 600, passo=0.12)
    E.frase(c, t, C["s14.d"], [("carro sobe", "i", 62), ("4 cm:", "g", 62), ("o pequeno desce?", "g", 60, COR)], XE, 740, passo=0.12)
    if t < C["s15"]:
        q = ep(t, C["s14.a"], 0.5)
        prensa(c, 1250, 80, 1600, 340, 940, 330, 230, q, carro="12.000 N")
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.formula_em(c, t, C["s16.a"], "ganho = 1.000 ÷ 20", XE, 240, 80, "g", TINTA)
    bola_txt(c, t, C["s16.b"], "50 ×", 1050, 210, 85, 52)
    E.formula_em(c, t, C["s16.c"], "F = 12.000 ÷ 50", XE, 470, 80, "g", TINTA)
    bola_txt(c, t, C["s16.d"], "240 N", 1050, 440, 110, 52, CERTO)
    E.formula_em(c, t, C["s16.e"], "desloc. = 4 cm × 50", XE, 720, 80, "g", TINTA)
    bola_txt(c, t, C["s16.f"], "200 cm", 1050, 690, 115, 50, CERTO)
    pilula_em(c, t, C["s16.f"] + 1.0, "2 metros", 1050, 860, 46, TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s18"]:
        E.saida(c, t, C["s18"] - 0.1, lambda: resumo(c, t, C, "s17", (
            ("s17.a", [("líquido preso:", "i", 70), ("transmite a pressão inteira", "g", 60, COR)]),
            ("s17.b", [("F₁ / A₁ = F₂ / A₂", "g", 66, COR)]),
            ("s17.c", [("ganha em força,", "i", 70), ("paga em distância", "g", 64, COR)]))))
        return

    def desenho():
        q = ep(t, C["s18.a"], 0.6)
        if q <= 0:
            return
        c.drawRect(skia.Rect.MakeLTRB(300, 700, 1150, 1000), M.paint(AGUA, 0.45 * q))
        M.line(c, 300, 700, 1150, 700, AGUA2, q, 5)
        F.bloco(c, 720, 820, 200, 160, None, a=q)
        F.forca(c, t, C["s18.b"], (720, 900), 90, 230, "E", cor=F.NEG, lado=1)
    proxima(c, t, C, "s18", [("Empuxo", "g", 120, COR)], [("princípio de Arquimedes", "i", 90)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, principio=b_principio, prensa=b_prensa, preco=b_preco, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
