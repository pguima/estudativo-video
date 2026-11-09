"""Visual — Estudativo · FIS-CIN-010: praticando vetores e movimentos (aula de prática, cinco questões).

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001 (peças em _ferramentas/fisica.py, importado como F).
Nesta aula: cada questão tem o número no alto, o enunciado à esquerda e o desenho à direita; na pausa, o relógio entra no
lugar do desenho. O MÉTODO (a grandeza que falta escolhe a ferramenta) fica no palco escuro, em quadro de quatro linhas.
Na resolução, os dados aparecem como lista (dados()): o que a questão dá em tinta, o que ela pede em laranja com "?",
e o que não aparece em cinza riscado. Velocidade em petróleo (F.VEL), aceleração em violeta (F.ACEL).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-010_praticando_vetores_e_movimentos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
assert math.isqrt(30 ** 2 + 40 ** 2) == 50 and 30 + 40 == 70
assert 20 + 10 == 30 and 600 / 30 == 20 and 20 * 20 == 400 and 600 - 10 * 20 == 400
assert (0 + 6) / 2 == 3 and 3 * 4 == 12 and 6 / 4 * 4 ** 2 / 2 == 12
assert 60 ** 2 == 3600 and 3600 / (2 * 3) == 600
assert -10 + (-2) * 3 == -16 and (-2) * 3 == -6


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais (copiadas entre as aulas FIS-CIN) ----------------
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


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete(c, t, C, cena, itens, desenhos=None):
    """'você precisa de N coisas': itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) à direita de cada caixa"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    h, gap, s1 = (230, 290, 58) if n == 2 else (196, 236, 52)
    y0 = 520 - (h + gap * (n - 1)) / 2
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s1, COR)], x + 44, y + h * 0.74)
        if desenhos:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 150, y + h / 2))
    ult = itens[-1][0]
    E.frase(c, t, lerp(C[ult], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 990, "left", 0.12)


def promessa(c, t, C, cena, itens, titulo="até o fim da aula"):
    """gancho: a órbita à direita e a lista numerada; itens = [(cue, texto, atraso)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps(titulo, "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a),
                                                        centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def fim_inscreva(c, t, C, cena, k_insc, k_bons):
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def resumo(c, t, C, cena, itens):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 190
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


# ---------------- peças desta aula ----------------
def titulo_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 190, 50, a=a), centro(c, str(n), XE + 50, 214, 64, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [("questão", "i", 72)], XE + 130, 214)


def dados(c, t, itens, x, y0, dy=96, size=64):
    """itens = [(instante, símbolo, valor, tipo)] com tipo "da" (tinta), "pede" (laranja, "?") ou "fora" (cinza riscado)"""
    for i, (ti, s, v, tipo) in enumerate(itens):
        y = y0 + i * dy
        cor = {"da": TINTA, "pede": COR, "fora": CINZA}[tipo]

        def lin(a, s=s, v=v, y=y, cor=cor, tipo=tipo):
            E.formula(c, s, x, y, size, "g", cor, a)
            E.formula(c, "= " + v if v else "", x + size * 1.5, y, size, "g", cor, a)
            if tipo == "fora":
                M.line(c, x - 10, y - size * 0.3, x + size * 4.2, y - size * 0.3, ERRADO, a, 6)
        E.foco(c, t, ti, 0.4, lin)


def aviao(c, x, y, s=1.0, a=1.0, cor=None, giro=0.0):
    """avião visto de cima apontando para cima (giro em graus)"""
    if a <= 0:
        return
    cor = cor or E.COR
    c.save(); c.translate(x, y); c.rotate(giro); c.scale(s, s)
    M.rrect(c, -14, -70, 28, 140, 14, cor, a)
    p = skia.Path(); p.moveTo(-90, 10); p.lineTo(90, 10); p.lineTo(14, -20); p.lineTo(-14, -20); p.close()
    c.drawPath(p, M.paint(cor, a))
    p2 = skia.Path(); p2.moveTo(-36, 66); p2.lineTo(36, 66); p2.lineTo(10, 46); p2.lineTo(-10, 46); p2.close()
    c.drawPath(p2, M.paint(cor, a))
    c.restore()


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], ps("a dificuldade quase nunca é", "i", 70) + [("a conta", "g", 70)], XE, 300, passo=0.1)
    E.frase(c, t, C["s01.b"], [("é", "i", 90), ("escolher", "g", 96, COR), ("a", "i", 90), ("fórmula", "g", 96, COR)], XE, 450, passo=0.14)
    for i in range(5):
        E.foco(c, t, C["s01.c"] + 0.8 + 0.15 * i, 0.4, lambda a, i=i: (M.rrect(c, XE + i * 190, 600, 160, 190, 20, E.COR if i % 2 == 0 else TINTA, a),
                                                                      centro(c, str(i + 1), XE + i * 190 + 80, 725, 90, "g", BR, a)))
    E.frase(c, t, C["s01.d"], [("em", "i", 80), ("segundos", "g", 80, COR)], XE, 940, passo=0.14)
    E.foco(c, t, C["s01.d"], 0.5, lambda a: F.cronometro(c, 1550, 700, 140, 15 * ease_io(prog(t, C["s01.d"], 1.5)), a, ""))


# ---------------- o que vai usar ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s02", (("s02.a", "soma de", "vetores"), ("s02.b", "movimento uniforme", "e encontro"), ("s02.c", "movimento com", "aceleração")))


# ---------------- o método (palco escuro) ----------------
FERR = (("v = v₀ + a · t", "Δs"), ("s = s₀ + v₀ · t + f{a · t^2}{2}", "v"), ("v^2 = v₀^2 + 2 · a · Δs", "t"), ("Δs = f{v₀ + v}{2} · t", "a"))


def b_metodo(c, t, C, b):
    palco(c, t)

    def s03():
        E.frase(c, t, C["s03"], ps("primeiro, o método", "i", 76, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s03.a"], [("v", "g", 76, BR), ("constante?", "i", 76, CLARO)], XE, 380, passo=0.12)
        E.formula_em(c, t, C["s03.b"], "s = s₀ + v · t", 1000, 380, 90, "g", BR)
        E.frase(c, t, C["s03.c"], [("v", "g", 76, BR), ("muda?", "i", 76, CLARO)], XE, 620, passo=0.12)
        E.frase(c, t, C["s03.c"] + 0.8, [("4", "g", 90, E.CLARO), ("ferramentas", "g", 80, BR)], 1000, 620, passo=0.12)
        E.frase(c, t, C["s03.d"], ps("cada uma deixa uma grandeza de fora", "i", 64, CLARO), W / 2, 880, "center", 0.1)
    E.saida(c, t, C["s04"] - 0.1, s03)
    if t < C["s04"]:
        return
    E.foco(c, t, C["s04"], 0.4, lambda a: (E.escreve(c, "ferramenta", XE, 200, 50, "b", CLARO, a), E.escreve(c, "não tem", 1460, 200, 50, "b", CLARO, a)))
    for i, (f_, sem) in enumerate(FERR):
        y = 330 + i * 140
        ti = C["s04." + "abcd"[i]]
        E.foco(c, t, ti, 0.5, lambda a, f_=f_, y=y: E.formula(c, f_, XE, y, 72, "g", BR, a))
        E.foco(c, t, ti + 0.5, 0.4, lambda a, sem=sem, y=y: (E.pilula(c, sem, 1560, y - 24, 56, "g", fundo=E.COR, a=a)))
    for i, s in enumerate(("v₀", "v", "a", "t", "Δs")):
        E.foco(c, t, C["s04.e"] + 0.2 * i, 0.4, lambda a, i=i, s=s: (M.rrect(c, 360 + i * 230, 880, 180, 110, 26, BR, 0.12 * a),
                                                                     E.formula(c, s, 450 + i * 230, 960, 70, "g", BR, a, "center")))
    E.frase(c, t, C["s04.f"], ps("a que não aparece em nada escolhe a ferramenta", "i", 54, CLARO), W / 2, 1050, "center", 0.08)


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    titulo_q(c, t, C["s05"], 1)
    O = (1440, 700)
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], [("avião:", "i", 66), ("norte,", "g", 64), ("40", "g", 64, COR), ("m/s", "b", 48, F.UNID)], XE, 400, passo=0.12)
        E.frase(c, t, C["s05.b"], [("vento:", "i", 66), ("leste,", "g", 64), ("30", "g", 64, COR), ("m/s", "b", 48, F.UNID)], XE, 520, passo=0.12)
        E.frase(c, t, C["s05.c"], ps("velocidade para quem está no chão?", "g", 56), XE, 700, passo=0.1)
        if t < C["s05.d"]:
            E.foco(c, t, C["s05.a"], 0.5, lambda a: aviao(c, *O, 0.9, a))
            F.vetor(c, t, C["s05.a"] + 0.4, (O[0], O[1] - 90), (O[0], O[1] - 400), None, "40 m/s", F.VEL, 11, size=50)
            F.vetor(c, t, C["s05.b"] + 0.3, (O[0] + 110, O[1]), (O[0] + 340, O[1]), None, "30 m/s", F.VEL, 11, lado=-1, size=50)
        else:
            E.relogio(c, t, C["s05.d"], cx=1460, cy=500, r=190)
        return
    u = 9
    P0 = (1300, 950)
    Q = (P0[0], P0[1] - 40 * u)
    R = (Q[0] + 30 * u, Q[1])
    F.vetor(c, t, C["s06"] + 0.2, P0, Q, None, "40", F.VEL, 11, size=52)
    F.vetor(c, t, C["s06"] + 0.6, Q, R, None, "30", F.VEL, 11, size=52)
    F.vetor(c, t, C["s06.c"], P0, R, "R", None, E.COR, 12, lado=-1, size=60)
    E.frase(c, t, C["s06.a"], [("ângulo", "g", 70), ("reto:", "g", 70), ("Pitágoras", "i", 74, COR)], XE, 400, passo=0.12)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: (M.rrect(c, XE, 470, 560, 140, 30, E.COR, 0.9 * a), centro(c, "30 · 40 · 50", XE + 280, 565, 76, "g", BR, a)))
    bola_txt(c, t, C["s06.c"], "50 m/s", XE + 800, 540, 115, 56)
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E.escreve(c, "70?", XE, 850, 110, "g", ERRADO, a))
    if t >= C["s06.d"] + 0.4:
        E.risco(c, XE - 10, 860, XE + 220, 760, t, C["s06.d"] + 0.4, largura=10)
    E.frase(c, t, C["s06.d"] + 0.6, ps("só com as setas em fila", "i", 56, TINTA2), XE + 280, 830, "left", 0.1)


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    titulo_q(c, t, C["s07"], 2)
    y = 820
    vx = F.pista(c, t, C["s07.a"], 300, 1620, y, 0, 600, list(range(0, 601, 100)), "m", size=36)
    q = ease_io(prog(t, C["s08.d"], 1.4))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: F.carrinho(c, vx(lerp(0, 400, q)), y, 160, a=a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: F.carrinho(c, vx(lerp(600, 400, q)), y, 160, a=a, sentido=-1))
    if t < C["s08"]:
        F.vetor(c, t, C["s07.b"] + 0.3, (vx(0), y - 150), (vx(0) + 200, y - 150), None, "20 m/s", F.VEL, 10, size=46)
        F.vetor(c, t, C["s07.c"] + 0.3, (vx(600), y - 150), (vx(600) - 100, y - 150), None, "10 m/s", F.VEL, 10, lado=-1, size=46)
        E.frase(c, t, C["s07.a"], ps("um em direção ao outro", "i", 64), XE, 360, passo=0.1)
        E.frase(c, t, C["s07.d"], [("quando", "g", 66, COR), ("e", "i", 66), ("onde", "g", 66, COR)] + ps("se cruzam?", "i", 66), XE, 480, passo=0.12)
        if t >= C["s07.e"]:
            E.relogio(c, t, C["s07.e"], cx=1500, cy=330, r=120)
        return
    E.frase(c, t, C["s08.a"], [("v", "g", 60, F.VEL), ("constante,", "i", 60), ("opostos:", "i", 60), ("atalho", "g", 60, COR)], XE, 360, passo=0.1)
    E.formula_em(c, t, C["s08.b"], "20 + 10 = 30", XE, 500, 80, "g", TINTA)
    E.formula_em(c, t, C["s08.c"], "600 ÷ 30 = 20 s", XE, 620, 80, "g", TINTA)
    E.formula_em(c, t, C["s08.d"], "20 · 20 = 400 m", 1000, 500, 80, "g", COR)
    bola_txt(c, t, C["s08.d"] + 1.4, "400 m", vx(400), y - 215, 70, 36)


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    titulo_q(c, t, C["s09"], 3)
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("bicicleta: parte do repouso,", "i", 60), XE, 380, passo=0.1)
        E.frase(c, t, C["s09.a"] + 1.4, [("6", "g", 64, COR), ("m/s", "b", 48, F.UNID), ("em", "i", 60), ("4", "g", 64, COR), ("s", "b", 48, F.UNID)], XE, 480, passo=0.12)
        E.frase(c, t, C["s09.b"], ps("quanto ela andou?", "g", 64), XE, 640, passo=0.1)
        if t >= C["s09.c"]:
            E.relogio(c, t, C["s09.c"], cx=1460, cy=500, r=190)
        return
    dados(c, t, [(C["s10.a"], "v₀", "0", "da"), (C["s10.a"] + 0.5, "v", "6", "da"), (C["s10.a"] + 1.0, "t", "4", "da"),
                 (C["s10.b"], "Δs", "?", "pede"), (C["s10.c"], "a", "", "fora")], XE, 380, 110, 70)
    E.formula_em(c, t, C["s10.c"] + 1.0, "Δs = f{v₀ + v}{2} · t", 900, 420, 84, "g", TINTA2)
    E.formula_em(c, t, C["s10.d"], "f{0 + 6}{2} = 3", 900, 640, 84, "g", TINTA)
    E.formula_em(c, t, C["s10.e"], "3 · 4", 900, 850, 84, "g", TINTA)
    bola_txt(c, t, C["s10.e"] + 0.8, "12 m", 1450, 820, 110, 64)


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    titulo_q(c, t, C["s11"], 4)
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("decolar:", "i", 60) + [("60", "g", 64, COR), ("m/s", "b", 48, F.UNID)], XE, 380, passo=0.1)
        E.frase(c, t, C["s11.b"], ps("do repouso, com", "i", 60) + [("3", "g", 64, F.ACEL), ("m/s²", "b", 48, F.UNID)], XE, 480, passo=0.1)
        E.frase(c, t, C["s11.c"], ps("comprimento mínimo da pista?", "g", 60), XE, 640, passo=0.1)
        if t < C["s11.d"]:
            E.foco(c, t, C["s11.a"], 0.5, lambda a: (M.rrect(c, 1100, 820, 700, 70, 10, "#3A3A40", a), aviao(c, 1200, 800, 0.9, a, giro=90)))
            for k in range(6):
                E.foco(c, t, C["s11.a"] + 0.2, 0.4, lambda a, k=k: M.line(c, 1140 + k * 110, 855, 1200 + k * 110, 855, BR, a, 5))
        else:
            E.relogio(c, t, C["s11.d"], cx=1460, cy=500, r=190)
        return
    dados(c, t, [(C["s12.a"], "v₀", "0", "da"), (C["s12.a"] + 0.4, "v", "60", "da"), (C["s12.a"] + 0.8, "a", "3", "da"),
                 (C["s12.b"], "Δs", "?", "pede"), (C["s12.c"], "t", "", "fora")], XE, 380, 110, 70)
    E.foco(c, t, C["s12.c"] + 0.4, 0.4, lambda a: E.pilula(c, "Torricelli", 1100, 360, 56, "g", fundo=E.COR, a=a))
    E.formula_em(c, t, C["s12.d"], "60^2 = 0 + 2 · 3 · Δs", 760, 560, 76, "g", TINTA)
    E.formula_em(c, t, C["s12.e"], "Δs = 3600 ÷ 6", 760, 760, 84, "g", TINTA)
    bola_txt(c, t, C["s12.e"] + 0.9, "600 m", 1520, 760, 110, 56)


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    titulo_q(c, t, C["s13"], 5)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], [("de", "i", 60), ("ré:", "i", 60), ("v₀", "g", 60, F.VEL), ("= −10", "g", 60), ("m/s", "b", 46, F.UNID)], XE, 380, passo=0.1)
        E.frase(c, t, C["s13.a"] + 1.8, [("a", "g", 60, F.ACEL), ("= −2", "g", 60), ("m/s²", "b", 46, F.UNID)], XE, 480, passo=0.1)
        E.frase(c, t, C["s13.b"], [("v", "g", 60, COR)] + ps("depois de 3 s?", "g", 60), XE, 640, passo=0.1)
        E.frase(c, t, C["s13.c"], ps("acelerado ou retardado?", "g", 60), XE, 750, passo=0.1)
        if t < C["s13.d"]:
            x, y = 1450, 860
            E.foco(c, t, C["s13.a"], 0.4, lambda a: F.carrinho(c, x, y, 220, a=a))
            F.vetor(c, t, C["s13.a"] + 0.4, (x, y - 170), (x - 300, y - 170), "v", None, F.VEL, 10, lado=-1, size=46)
            F.vetor(c, t, C["s13.a"] + 1.8, (x, y - 290), (x - 200, y - 290), "a", None, F.ACEL, 10, lado=-1, size=46)
        else:
            E.relogio(c, t, C["s13.d"], cx=1460, cy=500, r=190)
        return
    dados(c, t, [(C["s14"] + 0.3, "v₀", "−10", "da"), (C["s14"] + 0.6, "a", "−2", "da"), (C["s14"] + 0.9, "t", "3", "da"),
                 (C["s14.a"], "v", "?", "pede"), (C["s14.a"] + 0.8, "Δs", "", "fora")], XE, 380, 110, 70)
    E.formula_em(c, t, C["s14.b"], "v = v₀ + a · t", 860, 400, 84, "g", TINTA2)
    E.formula_em(c, t, C["s14.c"], "v = −10 + (−2) · 3", 860, 580, 84, "g", TINTA)
    bola_txt(c, t, C["s14.d"], "−16 m/s", 1500, 770, 120, 52, F.VEL)
    E.frase(c, t, C["s14.e"], ps("sinais iguais:", "i", 60) + [("acelerado", "g", 60, COR)], 860, 980, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.frase(c, t, C["s15"], [("resumindo", "i", 84, COR)], XE, 200)
    E.frase(c, t, C["s15.a"], [("v", "g", 66), ("constante:", "i", 66), ("sorvete", "g", 66, COR)], XE, 330, passo=0.12)
    E.frase(c, t, C["s15.b"], [("v", "g", 66), ("mudando:", "i", 66)] + ps("a grandeza que falta", "g", 62, COR), XE, 440, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("próxima aula:", "i", 64) + [("gráfico", "g", 72, COR), ("s × t", "g", 72, COR)], XE, 620, passo=0.12)
    P = E.plano(c, t, C["s15.c"] + 0.3, 300, 700, 640, 300, 0, 8, 0, 80, 1, 20, grade=False, rotulos=False, nomes=("t", "s"))
    E.curva(c, t, C["s15.c"] + 0.8, P, lambda x: 10 * x, 0, 8, d=1.0)
    fim_inscreva(c, t, C, "s15", "s15.d", "s15.e")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
