"""Visual — Estudativo · FIS-OND-007: cordas, tubos e ressonância.
Linguagem visual da trilha Ondas e Som: docstring do visual.py da FIS-OND-001. Nesta aula: onda estacionária animada de
verdade (estacionaria(): y = A·sen(nπx/L)·cos ωt) em laranja, com nós em tinta e a envoltória tracejada; onda que vai em
laranja e a que volta em azul F.NEG; tubo desenhado com o ar (envoltória de deslocamento: ventre na ponta aberta, nó na
fechada); harmônicos em pílulas, o que não existe riscado em vermelho.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Ondas e Som")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-OND-007_cordas_tubos_e_ressonancia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("estaciona", "harmonicos", "tubos", "ressonancia", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula: corda e tubo aberto f = n·v/(2L); tubo fechado f = n·v/(4L), n ímpar
assert 2 * 0.5 == 1 and 1 * 200 / (2 * 0.5) == 200 and [n * 200 for n in (2, 3, 4)] == [400, 600, 800]
assert abs(2 * 0.85 - 1.7) < 1e-12 and abs(340 / (2 * 0.85) - 200) < 1e-9                 # tubo aberto de 85 cm
assert abs(4 * 0.85 - 3.4) < 1e-12 and abs(340 / (4 * 0.85) - 100) < 1e-9                 # o mesmo, fechado
assert [n * 100 for n in (1, 3, 5, 7)] == [100, 300, 500, 700] and 100 == 200 / 2           # ímpares; metade do aberto
assert abs(4 * 0.17 - 0.68) < 1e-12 and abs(340 / 0.68 - 500) < 1e-9 and 1000 / 500 == 2   # questão: 1000 Hz é par
assert [n * 500 for n in (3, 5)] == [1500, 2500]


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças (da FIS-OND-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def conta(c, t, linhas, x, y0, dy, size, align="left", escuro=False):
    tinta = BR if escuro else TINTA
    for i, ln in enumerate(linhas):
        ti, s = ln[0], ln[1]
        prox = linhas[i + 1][0] if i + 1 < len(linhas) else 1e9
        cor = ln[2] if len(ln) > 2 else ((CLARO if escuro else COR) if t < prox else tinta)
        E.formula_em(c, t, ti, s, x, y0 + i * dy, size, "g", cor, align)


def pilula(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def lembrete2(c, t, C, cena, itens, desenhos):
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


# ---------------- peças desta aula ----------------
def estacionaria(c, t, t0, x0, x1, y, A, n, cor=None, periodo=0.9, nos=True, envolt=True, largura=7, a=1.0):
    """corda presa em x0 e x1 vibrando no harmônico n: y = A·sen(nπx/L)·cos(2πt/T); nós em tinta, envoltória tracejada"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.5) * a
    cor = cor or E.COR
    k = math.cos(2 * math.pi * (t - t0) / periodo)
    N = 160
    pts = [(x0 + (x1 - x0) * i / N, y - A * k * math.sin(n * math.pi * i / N)) for i in range(N + 1)]
    if envolt:
        for s_ in (1, -1):
            env = [(x0 + (x1 - x0) * i / N, y - s_ * A * math.sin(n * math.pi * i / N)) for i in range(N + 1)]
            F.poli(c, env, 1.0, TINTA2, 0.35 * q, 3, E.TRACO)
    F.poli(c, pts, 1.0, cor, q, largura)
    if nos:
        for j in range(n + 1):
            c.drawCircle(x0 + (x1 - x0) * j / n, y, 11, M.paint(TINTA, q))


def tubo(c, t, t0, x0, x1, y, h, fechado, n=1, cor=None, a=1.0, periodo=1.0):
    """tubo de x0 a x1 (aberto em x0; fechado em x1 se fechado). Dentro, a envoltória do ar no harmônico n:
    aberto = ventre nas duas pontas; fechado = ventre na aberta e nó na fechada"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.5) * a
    cor = cor or E.COR
    for yy in (y - h / 2, y + h / 2):
        M.line(c, x0, yy, x1, yy, TINTA, q, 8)
    if fechado:
        M.line(c, x1, y - h / 2 - 4, x1, y + h / 2 + 4, TINTA, q, 14)
    L = x1 - x0
    kk = n * math.pi / L if not fechado else n * math.pi / (2 * L)
    A = h * 0.36
    s = math.cos(2 * math.pi * (t - t0) / periodo)
    N = 120
    for sg in (1, -1):  # envoltória parada, tracejada
        env = [(x0 + L * i / N, y - sg * A * math.cos(kk * L * i / N)) for i in range(N + 1)]
        F.poli(c, env, 1.0, TINTA2, 0.4 * q, 3, E.TRACO)
    for sg in (1, -1):
        pts = [(x0 + L * i / N, y - sg * A * s * math.cos(kk * L * i / N)) for i in range(N + 1)]
        F.poli(c, pts, 1.0, cor, q, 6)


def violao_cordas(c, x0, x1, y0, a=1.0, aperto=None):
    """seis cordas de espessuras diferentes; aperto = x do dedo na quarta corda"""
    if a <= 0:
        return
    M.rrect(c, x0 - 40, y0 - 60, x1 - x0 + 80, 420, 30, "#8B5E3C", 0.25 * a)
    for i in range(6):
        y = y0 + i * 60
        M.line(c, x0, y, x1, y, "#B98A3C" if i > 2 else TINTA2, a, 15 - 2.2 * i)
    if aperto:
        E.bola(c, aperto, y0 + 3 * 60, 30, a=a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        x0, x1, y0 = 880, 1680, 360
        E.foco(c, t, C["s01.a"], 0.5, lambda a: violao_cordas(c, x0, x1, y0, a, aperto=1100 if t >= C["s01.c"] else None))
        if t >= C["s01.a"]:
            cota_ = ep(t, C["s01.a"] + 0.5, 0.5)
            if cota_ > 0:
                F.seta(c, (x0 + x1) / 2, 820, x0, 820, TINTA2, cota_, 5, 20)
                F.seta(c, (x0 + x1) / 2, 820, x1, 820, TINTA2, cota_, 5, 20)
                E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: centro(c, "mesmo comprimento", (x0 + x1) / 2, 790, 46, "i", TINTA2, a))
        if t >= C["s01.b"]:
            for i in range(6):
                E.foco(c, t, C["s01.b"] + 0.25 * i, 0.4, lambda a, i=i: E.escreve(c, ("Mi", "Lá", "Ré", "Sol", "Si", "Mi")[i], 1720, y0 + i * 60 + 18, 40, "b", TINTA2, a))
        E.frase(c, t, C["s01.a"], ps("cordas do", "i", 76) + [("mesmo tamanho", "g", 70)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], [("notas", "g", 76, COR), ("diferentes", "g", 76, COR)], XE, 430, passo=0.15)
        E.frase(c, t, C["s01.c"], ps("apertou a corda:", "i", 70), XE, 620, passo=0.12)
        E.frase(c, t, C["s01.c"] + 1.2, [("a", "i", 70), ("nota", "i", 70), ("sobe", "g", 76, COR)], XE, 730, passo=0.12)
        E.frase(c, t, C["s01.end"] - 1.0, [("por quê?", "g", 96)], XE, 900)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate((("s02.b", "cordas e tubos"), ("s02.c", "ressonância"))):
        y = 500 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 84, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def soma(a, x, y):
        for j, (dy, cor) in enumerate(((-30, E.COR), (30, F.NEG))):
            pts = [(x - 40 + 170 * i / 60, y + dy - 16 * math.sin(2 * math.pi * i / 30)) for i in range(61)]
            F.poli(c, pts, 1.0, cor, a, 5)

    def agudo(a, x, y):
        pts = [(x - 40 + 170 * i / 120, y - 28 * math.sin(2 * math.pi * i / 20)) for i in range(121)]
        F.poli(c, pts, 1.0, E.COR, a, 5)
    lembrete2(c, t, C, "s03", (("s03.b", "duas ondas se somam:", "reforço ou cancelamento"), ("s03.c", "frequência maior:", "som mais agudo")), (soma, agudo))


# ---------------- onda estacionária ----------------
def b_estaciona(c, t, C, b):
    x0, x1 = 760, 1720
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("corda presa nas duas pontas", "i", 70), XE, 220, passo=0.1)
        for xx in (x0, x1):
            E.foco(c, t, C["s04"] + 0.6, 0.4, lambda a, xx=xx: (M.rrect(c, xx - 14, 330, 28, 520, 8, TINTA, a)))
        # a que vai (laranja) e a que volta (azul), correndo; a soma embaixo
        for k, (yy, cor, sent, t0) in enumerate(((420, E.COR, 1, C["s04.a"]), (560, F.NEG, -1, C["s04.b"]))):
            if t >= t0:
                q = ep(t, t0, 0.5)
                d_ = sent * 240 * (t - t0)
                pts = [(x0 + (x1 - x0) * i / 120, yy - 45 * math.sin(2 * math.pi * ((x1 - x0) * i / 120 - d_) / 320)) for i in range(121)]
                F.poli(c, pts, 1.0, cor, q, 6)
                F.seta(c, 540 - 70 * sent, yy - 22, 540 + 70 * sent, yy - 22, cor, q, 6)
        E.foco(c, t, C["s04.a"] + 0.3, 0.4, lambda a: E.escreve(c, "vai", XE, 440, 64, "g", COR, a))
        E.foco(c, t, C["s04.b"] + 0.3, 0.4, lambda a: E.escreve(c, "volta", XE, 580, 64, "g", F.NEG, a))
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "soma", XE, 760, 64, "g", TINTA, a))
        estacionaria(c, t, C["s04.c"] + 0.3, x0, x1, 740, 80, 3, envolt=False, nos=False)
        E.frase(c, t, C["s04.d"], ps("parece parada:", "i", 66) + [("onda", "g", 66, COR), ("estacionária", "g", 66, COR)], XE, 960, passo=0.12)
        return
    y = 560
    estacionaria(c, t, C["s05"], x0 - 400, x1, y, 150, 3)
    xs = [x0 - 400 + (x1 - x0 + 400) * j / 3 for j in range(4)]
    for j, xx in enumerate(xs):
        E.foco(c, t, C["s05.a"] + 0.2 * j, 0.4, lambda a, xx=xx: centro(c, "nó", xx, y + 90, 48, "g", TINTA, a))
    for j in range(3):
        xv = (xs[j] + xs[j + 1]) / 2
        E.foco(c, t, C["s05.b"] + 0.2 * j, 0.4, lambda a, xv=xv: centro(c, "ventre", xv, y - 190, 48, "g", COR, a))
    pilula(c, t, C["s05.c"], "pontas presas = nós", W / 2, 230, 56, TINTA)
    if t >= C["s05.d"]:
        q = ep(t, C["s05.d"], 0.5)
        yy = y + 210
        F.seta(c, (xs[1] + xs[2]) / 2, yy, xs[1], yy, TINTA, q, 5, 20)
        F.seta(c, (xs[1] + xs[2]) / 2, yy, xs[2], yy, TINTA, q, 5, 20)
        E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: E.formula(c, "fuso = f{λ}{2}", (xs[1] + xs[2]) / 2, yy + 120, 72, "g", COR, a, "center"))


# ---------------- harmônicos ----------------
def b_harmonicos(c, t, C, b):
    if t < C["s07"]:
        x0, x1 = 760, 1760
        for i, (k, n, s) in enumerate((("s06.a", 1, "1º: fundamental"), ("s06.c", 2, "2º harmônico"), ("s06.d", 3, "3º harmônico"))):
            y = 300 + i * 270
            estacionaria(c, t, C[k], x0, x1, y, 90, n, periodo=1.2 / n)
            E.foco(c, t, C[k], 0.4, lambda a, s=s, y=y, i=i: E.escreve(c, s, XE, y + 20, 60, "g", COR if i == 0 else TINTA, a))
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, n=n, y=y: E.escreve(c, f"{n} fuso" + ("s" if n > 1 else ""), XE, y + 90, 46, "i", TINTA2, a))
        pilula(c, t, C["s06.b"] + 0.6, "a nota mais grave", 1260, 160, 46, TINTA, "b")
        pilula(c, t, C["s06.e"], "nº do harmônico = nº de fusos", W / 2, 1000, 56, E.COR)
        return
    if t < C["s08"]:
        def s07():
            F.formula_legenda(c, t, C["s07.a"], "f = f{n · v}{2L}", [("n", "número do harmônico", None), ("L", "comprimento da corda", "m"),
                                                                    ("v", "velocidade na corda", "m/s")],
                              XE, 330, 150, tl=[C["s07.b"], C["s07.c"], C["s07.d"]], size_l=56)
            E.foco(c, t, C["s07.d"] + 1.0, 0.4, lambda a: E.formula(c, "f em Hz", XE + 700, 300, 64, "b", TINTA2, a))
            E.formula_em(c, t, C["s07.e"], "n fusos: λ = f{2L}{n}", 1150, 600, 80, "g", COR)
            estacionaria(c, t, C["s07.e"] + 0.4, 1150, 1780, 820, 70, 2)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    if t < C["s09"]:
        E.foco(c, t, C["s08"], 0.5, lambda a: E.formula(c, "f = f{n · v}{2L}", XE, 240, 90, "g", TINTA2, a))
        E.foco(c, t, C["s08.a"], 0.5, lambda a: (E.escreve(c, "L =", 1150, 200, 72, "g", TINTA, a), F.medida(c, "0,5", "m", 1290, 200, 72, COR, a)))
        E.foco(c, t, C["s08.b"], 0.5, lambda a: (E.escreve(c, "v =", 1150, 300, 72, "g", TINTA, a), F.medida(c, "200", "m/s", 1290, 300, 72, COR, a)))
        conta(c, t, [(C["s08.c"], "2L = 2 · 0,5 = 1 m"), (C["s08.c"] + 2.4, "f = f{200}{1} = 200 Hz")], XE, 470, 180, 90)
        for i, v in enumerate((200, 400, 600, 800)):
            ti = C["s08.c"] + 3.6 if i == 0 else C["s08.d"] + 0.5 * i
            pilula(c, t, ti, f"{v} Hz", XE + 170 + i * 400, 900, 60, E.COR if i == 0 else TINTA)
        return
    E.frase(c, t, C["s09"], ps("e o violão do começo?", "i", 76), XE, 220, passo=0.12)
    E.foco(c, t, C["s09.a"], 0.5, lambda a: violao_cordas(c, 1000, 1780, 380, a, aperto=1250))
    E.frase(c, t, C["s09.a"], [("apertou:", "i", 70), ("L", "g", 70, COR), ("menor", "g", 70)], XE, 420, passo=0.12)
    E.frase(c, t, C["s09.a"] + 1.4, [("→", "g", 70, TINTA2), ("f", "g", 70, COR), ("maior,", "g", 70), ("mais", "i", 70), ("aguda", "g", 70, COR)], XE, 530, passo=0.12)
    E.frase(c, t, C["s09.b"], [("corda", "i", 70), ("grossa:", "g", 70), ("v", "g", 70, F.NEG), ("menor", "g", 70)], XE, 760, passo=0.12)
    E.frase(c, t, C["s09.b"] + 1.4, [("→", "g", 70, TINTA2), ("mais", "i", 70), ("grave", "g", 70, F.NEG)], XE, 870, passo=0.12)


# ---------------- tubos ----------------
def b_tubos(c, t, C, b):
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("no tubo, vibra", "i", 70) + [("o ar", "g", 70, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s10.b"], [("aberto:", "g", 70), ("f", "g", 70, COR), ("=", "g", 70, TINTA2)], XE, 380, passo=0.12)
        E.formula_em(c, t, C["s10.b"] + 0.6, "f{n · v}{2L}", XE + 420, 395, 80, "g", COR)
        E.foco(c, t, C["s10.b"] + 1.0, 0.4, lambda a: E.escreve(c, "n = 1, 2, 3...", XE + 620, 380, 56, "b", TINTA2, a))
        tubo(c, t, C["s10.a"] + 0.3, 1000, 1760, 600, 140, False, 1)
        E.foco(c, t, C["s10.a"] + 0.6, 0.4, lambda a: (centro(c, "aberto", 1000, 720, 44, "i", TINTA2, a), centro(c, "aberto", 1760, 720, 44, "i", TINTA2, a)))
        conta(c, t, [(C["s10.c"], "L = 0,85 m → 2L = 1,7 m"), (C["s10.d"], "f = 340 ÷ 1,7 = 200 Hz")], XE, 830, 130, 76)
        return
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("fechado", "g", 76, COR)] + ps("numa ponta", "i", 76), XE, 220, passo=0.12)
        tubo(c, t, C["s11.a"] + 0.3, 900, 1700, 520, 160, True, 1)
        E.foco(c, t, C["s11.b"], 0.4, lambda a: (c.drawCircle(1700, 520, 14, M.paint(TINTA, a)), centro(c, "nó", 1700, 680, 56, "g", TINTA, a)))
        E.foco(c, t, C["s11.c"], 0.4, lambda a: centro(c, "ventre", 900, 680, 56, "g", COR, a))
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "1 fuso = f{λ}{4}", XE, 420, 72, "g", TINTA, a))
        E.foco(c, t, C["s11.d"] + 1.2, 0.5, lambda a: E.formula(c, "f = f{n · v}{4L}", XE, 840, 110, "g", COR, a))
        E.foco(c, t, C["s11.e"], 0.5, lambda a: E.pilula(c, "n = 1, 3, 5 (só ímpares)", 1300, 880, 60, "g", fundo=E.COR, a=a, cor=BR))
        return
    E.frase(c, t, C["s12.a"], ps("o mesmo tubo,", "i", 70) + [("fechado", "g", 70, COR)], XE, 220, passo=0.12)
    tubo(c, t, C["s12"], 1150, 1750, 220, 110, True, 1)
    conta(c, t, [(C["s12.b"], "4L = 3,4 m → f = 340 ÷ 3,4 = 100 Hz")], XE, 430, 0, 76)
    for i, v in enumerate((100, 300, 500, 700)):
        ti = C["s12.b"] + 1.5 if i == 0 else C["s12.c"] + 0.4 * i
        pilula(c, t, ti, f"{v} Hz", XE + 170 + i * 400, 640, 60, E.COR)
    for i, v in enumerate((200, 400)):
        x = XE + 370 + i * 800
        E.foco(c, t, C["s12.d"] + 0.3 * i, 0.4, lambda a, v=v, x=x: E.pilula(c, f"{v} Hz", x, 840, 60, "g", fundo=TINTA2, a=a, cor=BR))
        if t >= C["s12.d"] + 0.5 + 0.3 * i:
            E.risco(c, x - 130, 870, x + 130, 810, t, C["s12.d"] + 0.5 + 0.3 * i, largura=10)


# ---------------- ressonância ----------------
def taca(c, cx, cy, s, a=1.0, treme=0.0, quebra=False):
    """taça de vidro: bojo, haste e pé; treme desloca as bordas"""
    if a <= 0:
        return
    p = skia.Path()
    w = s * (1 + 0.04 * treme)
    p.moveTo(cx - w * 0.5, cy - s)
    p.cubicTo(cx - w * 0.55, cy - s * 0.2, cx - w * 0.1, cy, cx, cy)
    p.cubicTo(cx + w * 0.1, cy, cx + w * 0.55, cy - s * 0.2, cx + w * 0.5, cy - s)
    pt = M.paint("#7FC8E8", 0.35 * a)
    c.drawPath(p, pt)
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    M.line(c, cx, cy, cx, cy + s * 0.6, TINTA, a, 6)
    M.line(c, cx - s * 0.3, cy + s * 0.6, cx + s * 0.3, cy + s * 0.6, TINTA, a, 7)
    if quebra:
        for dx, dy in ((-0.2, -0.8), (0.15, -0.6), (0.05, -0.9)):
            M.line(c, cx + dx * s, cy + dy * s, cx + dx * s + 30, cy + dy * s + 40, ERRADO, a, 5)


def b_ressonancia(c, t, C, b):
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], [("ressonância", "g", 100, COR)], XE, 230)
        E.frase(c, t, C["s13.b"], ps("todo corpo tem", "i", 64) + [("frequências naturais", "g", 64)], XE, 360, passo=0.1)
        E.frase(c, t, C["s13.c"], ps("empurrão", "i", 64) + [("na frequência natural", "g", 64, COR)], XE, 480, passo=0.1)
        E.frase(c, t, C["s13.d"], [("amplitude", "g", 70, COR), ("cresce", "g", 70)], XE, 620, passo=0.12)
        # pêndulo empurrado no tempo certo: a amplitude cresce
        if t >= C["s13.c"]:
            amp = min(34, 6 + 10 * (t - C["s13.c"]))
            ang = amp * math.cos(2 * math.pi * (t - C["s13.c"]) / 1.6)
            F.pendulo(c, t, C["s13.c"] - 0.6, 1450, 200, 520, ang, r=50, amp=amp if t >= C["s13.d"] else None)
            if math.cos(2 * math.pi * (t - C["s13.c"]) / 1.6) > 0.9:
                g = math.radians(ang)
                bx, by = 1450 + 520 * math.sin(g), 200 + 520 * math.cos(g)
                F.seta(c, bx + 160, by, bx + 60, by, CERTO, 1.0, 9)
        return
    for i, (k, s) in enumerate((("s14.a", "balanço"), ("s14.b", "taça"), ("s14.c", "violão"))):
        x = 360 + i * 600
        pilula(c, t, C[k], s, x, 260, 64, E.COR if i == 1 else TINTA)
    if t >= C["s14.a"]:
        ang = 30 * math.cos(2 * math.pi * (t - C["s14.a"]) / 1.6)
        F.pendulo(c, t, C["s14.a"], 360, 380, 380, ang, r=46)
    if t >= C["s14.b"]:
        tr = math.sin(t * 60) * min(1.0, (t - C["s14.b"]) / 2)
        E.foco(c, t, C["s14.b"], 0.4, lambda a: taca(c, 960, 690, 200, a, tr, quebra=t >= C["s14.b"] + 2.2))
        for j in range(3):
            r = ((t - C["s14.b"]) * 120 + j * 60) % 180 + 40
            c.drawArc(skia.Rect.MakeXYWH(760 - r, 560 - r, 2 * r, 2 * r), -30, 60, False, M.paint(E.COR, 0.6 * (1 - r / 220), stroke=5))
        E.foco(c, t, C["s14.b"] + 0.4, 0.4, lambda a: centro(c, "a nota certa da voz", 960, 960, 46, "i", TINTA2, a))
    if t >= C["s14.c"]:
        q = ep(t, C["s14.c"], 0.5)
        c.drawOval(skia.Rect.MakeXYWH(1400, 420, 330, 440), M.paint("#B98A3C", 0.8 * q))
        c.drawCircle(1565, 600, 60, M.paint("#3A2A1A", q))
        for i in range(4):
            M.line(c, 1530 + i * 22, 380, 1530 + i * 22, 860, TINTA2, q, 3)
        E.foco(c, t, C["s14.c"] + 0.6, 0.4, lambda a: centro(c, "a caixa ressoa", 1565, 960, 46, "i", TINTA2, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s15.a"], [("fechado", "g", 70), ("não", "i", 76), ("tem", "i", 76), ("pares", "g", 70, COR)], XE + 480, 190, passo=0.12)
    tubo(c, t, C["s15.a"] + 0.4, 1150, 1750, 420, 130, True, 1)
    E.foco(c, t, C["s15.a"] + 1.0, 0.5, lambda a: F.medida(c, 100, "Hz", XE, 420, 100, COR, a))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: F.medida(c, "200 Hz?", "", XE + 420, 420, 100, ERRADO, a))
    if t >= C["s15.c"]:
        E.risco(c, XE + 400, 430, XE + 830, 340, t, C["s15.c"], largura=12)
    E.frase(c, t, C["s15.c"] + 0.6, [("nó", "g", 64), ("numa", "i", 64), ("ponta,", "i", 64), ("ventre", "g", 64, COR), ("na", "i", 64), ("outra", "i", 64)], XE, 620, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("só", "i", 64) + [("ímpares", "g", 64, COR)] + ps("de quartos de", "i", 64) + [("λ", "g", 64, COR)], XE, 740, passo=0.12)
    E.frase(c, t, C["s15.e"], [("100", "g", 90), ("→", "g", 90, TINTA2), ("300", "g", 90, CERTO), ("Hz", "b", 66, F.UNID)], XE, 920, passo=0.15)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s16"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
    E.frase(c, t, C["s16.a"], ps("ache o", "i", 76, CLARO) + [("fundamental", "g", 76, BR)] + ps("e multiplique", "i", 76, CLARO), W / 2, 290, "center", 0.12)
    for i, (k, s, mult) in enumerate((("s16.b", "corda e tubo aberto", ("×1", "×2", "×3")), ("s16.c", "tubo fechado", ("×1", "×3", "×5")))):
        y = 460 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, s=s, y=y: E.escreve(c, s, 260, y + 22, 64, "g", BR, a))
        for j, m in enumerate(mult):
            E.foco(c, t, C[k] + 0.6 + 0.3 * j, 0.4, lambda a, m=m, y=y, j=j: E.pilula(c, m, 1100 + j * 230, y, 64, "g", fundo=E.COR, a=a, cor=BR))
    E.frase(c, t, C["s16.d"], [("mesmo", "i", 60, CLARO), ("L:", "g", 60, BR), ("fundamental", "i", 60, CLARO), ("do", "i", 60, CLARO), ("fechado", "g", 60, BR), ("=", "g", 60, CLARO),
                               ("metade", "g", 60, BR), ("do", "i", 60, CLARO), ("aberto", "g", 60, BR)], W / 2, 830, "center", 0.1)
    E.frase(c, t, C["s16.e"], [("desenho", "g", 60, BR), ("da", "i", 60, CLARO), ("corda?", "i", 60, CLARO), ("conte", "i", 60, CLARO), ("os", "i", 60, CLARO), ("fusos", "g", 60, BR)],
            W / 2, 970, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("tubo", "i", 70), ("fechado", "g", 70, COR)], XE, 340, passo=0.12)
    E.foco(c, t, C["s17.a"] + 0.8, 0.5, lambda a: F.medida(c, 17, "cm", XE + 560, 340, 84, TINTA, a))
    E.frase(c, t, C["s17.b"], [("som:", "i", 70)], XE, 460)
    E.foco(c, t, C["s17.b"] + 0.3, 0.5, lambda a: F.medida(c, 340, "m/s", XE + 200, 460, 84, TINTA, a))
    E.frase(c, t, C["s17.c"], [("fundamental?", "g", 76, COR)], XE, 620)
    E.frase(c, t, C["s17.d"], ps("ressoa em", "i", 70) + [("1.000", "g", 70, COR), ("Hz?", "g", 70, COR)], XE, 760, passo=0.12)
    if t < C["s18"]:
        tubo(c, t, C["s17.a"], 1150, 1750, 480, 130, True, 1)
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s19"], [("vamos", "i", 70, COR), ("lá", "i", 70, COR)], XE, 190)
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "f = f{n · v}{4L}", 1250, 300, 90, "g", TINTA2, a))
    conta(c, t, [(C["s19.a"], "4L = 4 · 0,17"), (C["s19.b"], "= 0,68 m"), (C["s19.c"], "f = 340 ÷ 0,68")], XE, 370, 150, 90)
    bola_txt(c, t, C["s19.c"] + 1.4, "500 Hz", 1500, 600, 130, 64)
    E.frase(c, t, C["s19.d"], [("1.000", "g", 76), ("=", "g", 76, TINTA2), ("2", "g", 76, ERRADO), ("×", "g", 76, TINTA2), ("500:", "g", 76), ("par", "g", 76, ERRADO)], XE, 830, passo=0.12)
    pilula(c, t, C["s19.e"], "não ressoa", 1240, 805, 60, ERRADO)
    for i, v in enumerate(("1.500", "2.500")):
        pilula(c, t, C["s19.f"] + 0.4 * i, f"{v} Hz", XE + 220 + i * 420, 980, 56, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", "corda e tubo aberto:", "f = f{n · v}{2L}", "todos"), ("s20.b", "tubo fechado:", "f = f{n · v}{4L}", "só ímpares"),
                 ("s20.c", "ressonância:", "", "empurrar na frequência natural"))
        for i, (k, s1, f_, s2) in enumerate(itens):
            y = 380 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 52, a=a), centro(c, str(i + 1), 240, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s1, "g", 64)], 340, y)
            if f_:
                E.formula_em(c, t, C[k] + 0.4, f_, 1050, y + 10, 80, "g", COR)
                E.frase(c, t, C[k] + 0.9, ps(s2, "i", 60, TINTA2), 1450, y, passo=0.1)
            else:
                E.frase(c, t, C[k] + 0.5, ps(s2, "i", 60, COR), 820, y, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], ps("a fonte", "i", 100) + [("anda", "g", 110, COR)], XE, 400, passo=0.15)
    E.frase(c, t, C["s21.b"], [("efeito", "g", 90), ("Doppler", "g", 90, COR)], XE, 540, passo=0.15)
    if t >= C["s21.b"]:  # frentes de onda saindo de uma fonte que anda
        q = ep(t, C["s21.b"], 0.5)
        tau = (t - C["s21.b"]) % 3.0
        c.save(); c.clipRect(skia.Rect.MakeXYWH(0, 610, 1350, 470))
        e = 0.0
        while e < tau:  # uma crista a cada 0,4 s, centrada onde a fonte estava; a fonte anda mais devagar que o som
            r = 20 + 170 * (tau - e)
            c.drawCircle(420 + 110 * e, 840, r, M.paint(E.COR, q * 0.8 * max(0.0, 1 - (tau - e) / 3.0), stroke=5))
            e += 0.4
        c.restore()
        E.bola(c, 420 + 110 * tau, 840, 26, a=q)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, estaciona=b_estaciona, harmonicos=b_harmonicos, tubos=b_tubos,
              ressonancia=b_ressonancia, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
