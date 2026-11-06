"""Visual — Estudativo · MAT-FRA-001: o que é uma fração.
Identidade em _ferramentas/editorial.py. A barra de chocolate é o fio da aula: corta em 4, pinta 3 e vira 3/4. Todos os
instantes vêm dos cues da voz; nada de segundos absolutos.
Peças só desta aula: P, fica, pessoa, relogio."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, fr, sinal, palco, chocolate, chave, centro
import motor as M

E.usar("Matemática", "Frações e Decimais")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-FRA-001_o_que_e_uma_fracao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("barra", "nomes", "leitura", "traco", "atalho"))
BR = E.SOBRE


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def P(s, est="i", size=84, cor=None):
    """palavras de uma frase, todas no mesmo estilo"""
    return [(w, est, size, cor or TINTA) for w in s.split()]


def fica(c, t, t0, t1, partes, x, y, align="left", passo=0.15):
    """frase que entra em t0 e sai em t1"""
    E.saida(c, t, t1, lambda: E.frase(c, t, t0, partes, x, y, align, passo))


def pessoa(c, cx, y, r, cor, a=1.0):
    """pessoa simples, cabeça e ombros; y = base"""
    M.rrect(c, cx - r, y - r * 1.25, 2 * r, r * 1.25, r * 0.6, cor, a)
    E.bola(c, cx, y - r * 1.85, r * 0.62, cor, a)


def relogio(c, t, t0, cx, cy):
    """relógio de pausa: enche nos 3 segundos da pausa"""
    r = 190 * ease_back(prog(t, t0, 0.6))
    if r <= 0:
        return
    E.bola(c, cx, cy, r)
    f = M.clamp(prog(t, t0 + 0.8, 3.0))
    if f > 0:
        E.arco(c, cx, cy, r + 30, -90, 360 * f, TINTA, 10)
    for dx in (-40, 40):
        M.rrect(c, cx + dx - 20, cy - 72, 40, 144, 11, BR, ep(t, t0 + 0.2, 0.4))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + 300, 60, "i", TINTA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    s2 = C["s02"]

    def codigo():
        y, s = 380, 220
        for t0, n, d, x, nome in ((C["s01.a"], 3, 4, 430, "três quartos"), (C["s01.b"], 5, 12, 960, "cinco doze avos"), (C["s01.c"], 12, 4, 1490, "doze quartos")):
            fr(c, t, t0, n, d, x, y, s, COR if d == 12 else None)
            E.foco(c, t, t0 + 0.2, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 690, 72, "i", TINTA2, a))
        E.frase(c, t, C["s01.c"] + 1.0, P("se essas palavras te travam,") + P("calma", "g", 76, COR), W / 2, 840, "center", passo=0.17)
        E.frase(c, t, lerp(C["s01.c"], s2, 0.6), P("é") + P("bem mais simples", "g", 76, COR) + P("do que parece"), W / 2, 960, "center", passo=0.17)
    E.saida(c, t, s2 - 0.1, codigo)
    if t < s2:
        return

    E.frase(c, t, s2 + 0.2, P("até o fim desta aula, você vai", size=80, cor=COR), XE, 170, passo=0.13)
    ta, tb, tc, td = C["s02.a"], C["s02.b"], C["s02.c"], C["s02.d"]
    # 1: pintar
    E.foco(c, t, ta, 0.5, lambda a: chocolate(c, XE, 240, 270, 96, 4, [(i, COR, 1) for i in range(3)], a))
    E.frase(c, t, ta + 0.1, P("pintar", "g", 88) + P("uma fração", "i", 96), 500, 320, passo=0.15)
    # 2: ler
    E.foco(c, t, tb, 0.5, lambda a: E.fracao(c, 5, 12, XE + 135, 462, 72, COR, a))
    E.frase(c, t, tb + 0.1, P("ler", "g", 88) + P("qualquer fração", "i", 96), 500, 510, passo=0.15)
    # 3: 12/4 = 3
    E.foco(c, t, tc, 0.5, lambda a: E.fracao(c, 12, 4, XE + 135, 652, 72, COR, a))
    E.frase(c, t, tc + 0.1, P("é só o número", "i", 96) + P("3", "g", 92, COR), 500, 700, passo=0.15)
    # 4: atalho
    p = ease_back(prog(t, td - 0.1, 0.5))
    if p > 0:
        E.mais(c, XE + 135, 852, 62 * p, giro=(1 - p) * 90)
    E.frase(c, t, td, P("atalho", "g", 88) + P("de prova", "i", 96), 500, 890, passo=0.15)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, P("para acompanhar,"), XE, 300)
    E.frase(c, t, C["s03.a"] - 1.2, P("você só precisa de"), XE, 400, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 710, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 215, 690, 130, "i", TINTA, a))
    x, y, w, h = 960, 330, 760, 300
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("saber", "i", 100)], x + 60, y + 125)
    E.frase(c, t, C["s03.b"] + 0.3, [("dividir", "g", 124, COR)], x + 60, y + 245)
    E.cursor(c, x + w - 34, y + h - 30, ep(t, C["s03.b"] + 0.4, 0.4))
    E.frase(c, t, C["s03.b"] + 1.1, P("se faltar isso, procure a aula", size=62) + P("no canal", "g", 56, COR), XE, 860, passo=0.14)


# ---------------- a barra ----------------
BX, BW, BY, BH = 260, 1400, 300, 210


def b_barra(c, t, C, b):
    lp = BW / 4
    s4a, s4b, s5a, s5b, s6, s6a, s6b, s6c, s7 = C["s04.a"], C["s04.b"], C["s05.a"], C["s05.b"], C["s06"], C["s06.a"], C["s06.b"], C["s06.c"], C["s07"]

    def tela():
        # o título de cada momento
        fica(c, t, s4a, s5b - 0.2, P("imagine uma barra de") + P("chocolate", "g", 76, COR), W / 2, 190, "center")
        fica(c, t, s5b, s6a - 0.15, P("fração:", "g", 76, COR) + P("que parte do inteiro você tem"), W / 2, 190, "center", 0.13)
        fica(c, t, s6a, s6b - 0.1, P("pinte um pedaço"), W / 2, 190, "center")
        fica(c, t, s6b, s6c - 0.1, P("pinte mais") + P("dois", "g", 76, COR), W / 2, 190, "center")
        E.frase(c, t, s6c, P("três quartos", "g", 76, COR) + P("da barra"), W / 2, 190, "center")

        # a barra
        ped = [(0, COR, prog(t, s6a, 0.4))] + [(i, COR, prog(t, s6b + (i - 1) * 0.2, 0.4)) for i in (1, 2)]
        chocolate(c, BX, BY, BW, BH, 4, ped, ep(t, s4a, 0.5), ep(t, s4b, 0.9))
        for i in range(3):
            t0 = s6a if i == 0 else s6b + (i - 1) * 0.2
            E.foco(c, t, t0 + 0.1, 0.3, lambda a, i=i: centro(c, str(i + 1), BX + lp * (i + 0.5), BY + 142, 110, "g", BR, a), sobe=0, blur=6)

        # você e três amigos: 4 pessoas, 4 pedaços
        def gente():
            for i in range(4):
                E.foco(c, t, s4a + 1.7 + i * 0.14, 0.4, lambda a, i=i: pessoa(c, BX + lp * (i + 0.5), 770, 50, COR if i == 0 else TINTA2, a))
            E.foco(c, t, s4a + 2.3, 0.4, lambda a: centro(c, "você e três amigos", W / 2, 860, 64, "i", TINTA, a))
            E.frase(c, t, s4b, P("quatro pedaços iguais", "g", 76, COR), W / 2, 975, "center")
        E.saida(c, t, s5a - 0.15, gente)

        # um pedaço = um quarto
        def um():
            chave(c, BX + 8, BX + lp - 8, BY + BH + 16, COR, ep(t, s5a, 0.4))
            E.foco(c, t, s5a + 0.1, 0.5, lambda a: E.fracao(c, 1, 4, BX + lp / 2, 690, 120, COR, a))
            E.frase(c, t, s5a + 0.3, P("cada pedaço é") + P("um quarto", "g", 76, COR) + P("da barra"), BX + lp + 30, 720, passo=0.14)
        E.saida(c, t, s6b - 0.1, um)

        # o inteiro
        def inteiro():
            chave(c, BX, BX + BW, BY - 14, TINTA, ep(t, s6 - 2.0, 0.5), h=-20)
            E.frase(c, t, s6 - 2.0, P("inteiro:", "g", 76, COR) + P("a barra completa"), W / 2, 880, "center", passo=0.17)
        E.saida(c, t, s6a - 0.1, inteiro)

        # três de quatro
        chave(c, BX + 8, BX + lp * 3 - 8, BY + BH + 16, COR, ep(t, s6b + 0.6, 0.4))
        E.foco(c, t, s6b + 0.7, 0.4, lambda a: centro(c, "3 dos 4 pedaços", BX + lp * 1.5, BY + BH + 104, 70, "g", COR, a))
        E.resultado(c, t, s6c, 3, 4, 1360, 790, 124, 165)
        E.frase(c, t, s6c + 0.2, P("você pintou", "i", 92), 420, 800, passo=0.15)
    E.saida(c, t, s7 - 0.1, tela)
    if t < s7:
        return

    # só vale com pedaços iguais
    E.frase(c, t, s7 + 0.2, P("só tem uma") + P("exigência", "g", 76, COR), W / 2, 170, "center")
    x, w, y1, y2, h = 500, 1120, 250, 500, 150
    E.foco(c, t, C["s07.a"], 0.5, lambda a: (chocolate(c, x, y1, w, h, 4, [(0, COR, 1)], a), E.fracao(c, 1, 4, 290, y1 + h / 2, 84, CERTO, a)))
    E.foco(c, t, C["s07.a"] + 0.1, 0.4, lambda a: centro(c, "pedaços iguais", x + w / 2, y1 + h + 66, 60, "b", CERTO, a))
    q = C["s07.a"] + 0.7
    E.foco(c, t, q, 0.5, lambda a: (E.barra(c, x, y2, w, h, 0.64, [(0.64, 1), (0.8, 1), (0.9, 1)], a), E.fracao(c, 1, 4, 290, y2 + h / 2, 84, ERRADO, a)))
    chave(c, x + 8, x + w * 0.64 - 8, y2 + h + 14, TINTA2, ep(t, q + 0.5, 0.4))
    E.foco(c, t, q + 0.6, 0.4, lambda a: centro(c, "enorme", x + w * 0.32, y2 + h + 96, 58, "i", TINTA, a))
    chave(c, x + w * 0.9 + 6, x + w - 6, y2 + h + 14, TINTA2, ep(t, q + 1.0, 0.4))
    E.foco(c, t, q + 1.1, 0.4, lambda a: centro(c, "minúsculo", x + w * 0.95, y2 + h + 96, 58, "i", TINTA, a))
    if t >= C["s07.b"]:
        E.risco(c, 225, y2 + 150, 355, y2, t, C["s07.b"], largura=12)
    E.frase(c, t, C["s07.b"], P("aquilo") + P("não é um quarto", "g", 76, ERRADO) + P("da barra"), W / 2, 880, "center")


# ---------------- numerador e denominador ----------------
def b_nomes(c, t, C, b):
    s9, s10, s11 = C["s09"], C["s10"], C["s11"]
    t10c, t10d = C["s10.c"], C["s10.d"]

    def ficha():
        cx, cy, s = 430, 450, 300
        lw = E.larg("4", "g", s) + s * 0.2
        p = ep(t, C["s08.a"], 0.5)
        M.rrect(c, cx - lw / 2 * p, cy - 12, lw * p, 25, 12, TINTA, 1.0 if p > 0 else 0)
        cn = E.mix(TINTA, COR, ep(t, C["s10.a"], 0.4))
        cd = E.mix(TINTA, COR, ep(t, C["s09.a"], 0.4) * (1 - ep(t, C["s10.a"], 0.4)))
        E.foco(c, t, C["s08.b"], 0.5, lambda a: centro(c, "3", cx, cy - s * 0.2, s, "g", cn, a))
        E.foco(c, t, C["s08.c"], 0.5, lambda a: centro(c, "4", cx, cy + s * 0.9, s, "g", cd, a))

        # s08: as três partes, com nome simples
        def partes():
            E.frase(c, t, C["s08"] + 0.2, P("na escrita, a fração tem", cor=COR), 660, 190, passo=0.14)
            E.frase(c, t, C["s08.b"], P("um número em cima", size=76), 660, 300, passo=0.14)
            E.frase(c, t, C["s08.a"], P("um traço", size=76), 660, 462, passo=0.14)
            E.frase(c, t, C["s08.c"], P("outro embaixo", size=76), 660, 640, passo=0.14)
        E.saida(c, t, s9 - 0.1, partes)

        # denominador: em quantas partes o inteiro foi dividido
        bx, by, bw, bh = 830, 640, 880, 150
        q = ep(t, C["s09.a"], 0.5)
        if q > 0:
            M.arrow(c, 620, 640, 790, 520, COR if t < C["s10.a"] else FIO, q, 4, 16, q)
        E.frase(c, t, C["s09.a"], [("denominador", "g", 88, COR)], 830, 520)
        E.frase(c, t, C["s09.b"], P("as partes iguais do inteiro", size=62), 830, 590, passo=0.1)
        ped = [(i, COR, prog(t, C["s10.b"] + i * 0.2, 0.4)) for i in range(3)]
        chocolate(c, bx, by, bw, bh, 4, ped, ep(t, C["s09.b"], 0.5), ep(t, C["s09.b"] + 0.1, 0.8))
        E.frase(c, t, C["s09.c"] - 1.7, P("denominar", "g", 60, COR) + P("é dar nome", size=66), XE, 880, passo=0.14)

        def quarto():
            chave(c, bx + 6, bx + bw / 4 - 6, by + bh + 14, COR, ep(t, C["s09.c"], 0.4))
            E.foco(c, t, C["s09.c"] + 0.1, 0.4, lambda a: centro(c, "quarto", bx + bw / 8, by + bh + 104, 76, "g", COR, a))
        E.saida(c, t, C["s10.a"] - 0.1, quarto)

        # numerador: quantas você pegou
        q = ep(t, C["s10.a"], 0.5)
        if q > 0:
            M.arrow(c, 620, 280, 790, 260, COR, q, 4, 16, q)
        E.frase(c, t, C["s10.a"], [("numerador", "g", 88, COR)], 830, 280)
        E.frase(c, t, C["s10.b"], P("conta as partes que você pegou", size=62), 830, 350, passo=0.1)
    E.saida(c, t, t10c - 0.1, ficha)
    if t < t10c - 0.1:
        return

    def duas():
        x, w, h = 500, 1200, 150
        # mudou o de cima: mais pedaços, do mesmo tamanho
        y = 210
        n = 3 if t >= t10c + 1.0 else 2
        E.frase(c, t, t10c, P("mudou o de cima:", size=72) + P("muda a quantidade", "g", 64, COR), XE, y - 30, passo=0.13)
        E.foco(c, t, t10c + 0.1, 0.4, lambda a: E.fracao(c, n, 4, 300, y + 90, 92, COR, a))
        ped = [(i, COR, prog(t, t10c + 0.2 + i * 0.15, 0.3)) for i in (0, 1)] + [(2, COR, prog(t, t10c + 1.0, 0.4))]
        E.foco(c, t, t10c + 0.1, 0.4, lambda a: chocolate(c, x, y + 20, w, h, 4, ped, a))
        # mudou o de baixo: pedaços de outro tamanho
        y = 610
        vira = t10d + 0.8
        E.frase(c, t, t10d, P("mudou o de baixo:", size=72) + P("muda o tamanho", "g", 64, COR), XE, y - 30, passo=0.13)
        E.foco(c, t, t10d + 0.1, 0.4, lambda a: E.fracao(c, 3, 8 if t >= vira else 4, 300, y + 90, 92, COR, a))
        E.saida(c, t, vira - 0.15, lambda: E.foco(c, t, t10d + 0.1, 0.4, lambda a: chocolate(c, x, y + 20, w, h, 4, [(i, COR, 1) for i in range(3)], a)), d=0.3)
        E.foco(c, t, vira, 0.5, lambda a: chocolate(c, x, y + 20, w, h, 8, [(i, COR, 1) for i in range(3)], a))
    E.saida(c, t, s11 - 0.1, duas)
    if t < s11 - 0.1:
        return

    # pintar 2/5 lendo a fração
    ta, tb, tc = C["s11.a"], C["s11.b"], C["s11.c"]
    E.frase(c, t, s11 + 0.2, P("com esses nomes,") + P("pintar", "g", 76, COR) + P("fica automático"), W / 2, 190, "center", passo=0.14)
    cx, cy, s = 410, 500, 250
    cd, cn = E.mix(TINTA, COR, ep(t, tb, 0.4) * (1 - ep(t, tc, 0.4))), E.mix(TINTA, COR, ep(t, tc, 0.4))

    def dois_quintos(a):
        E.fracao(c, 2, 5, cx, cy, s, TINTA, a)
        centro(c, "2", cx, cy - s * 0.2, s, "g", cn, a)
        centro(c, "5", cx, cy + s * 0.9, s, "g", cd, a)
    E.foco(c, t, ta, 0.5, dois_quintos)
    x, y, w, h = 720, 370, 1000, 220
    ped = [(i, COR, prog(t, tc + 0.2 + i * 0.25, 0.4)) for i in range(2)]
    chocolate(c, x, y, w, h, 5, ped, ep(t, ta + 0.1, 0.5), ep(t, tb, 0.9))
    E.frase(c, t, tb, P("o de baixo:", size=72) + P("cortar em 5", "g", 66) + P("partes iguais", size=72), x, 710, passo=0.13)
    E.frase(c, t, tc, P("o de cima:", size=72) + P("pintar 2", "g", 66, COR), x, 830, passo=0.13)


# ---------------- como se lê ----------------
NOMES = ((2, "meio"), (3, "terço"), (4, "quarto"), (5, "quinto"), (6, "sexto"), (7, "sétimo"), (8, "oitavo"), (9, "nono"), (10, "décimo"))


def b_leitura(c, t, C, b):
    s13, s15, s16 = C["s13"], C["s15"], C["s16"]

    def regra():
        E.frase(c, t, C["s12"] + 0.3, P("como se lê", size=100) + P("uma fração?", "g", 90, COR), W / 2, 190, "center")
        cx, cy, s = 440, 560, 270
        cn, cd = E.mix(TINTA, COR, ep(t, C["s12.a"], 0.4) * (1 - ep(t, C["s12.b"], 0.4))), E.mix(TINTA, COR, ep(t, C["s12.b"], 0.4))

        def tres_q(a):
            E.fracao(c, 3, 4, cx, cy, s, TINTA, a)
            centro(c, "3", cx, cy - s * 0.2, s, "g", cn, a)
            centro(c, "4", cx, cy + s * 0.9, s, "g", cd, a)
        E.foco(c, t, C["s12"] + 0.5, 0.5, tres_q)
        for t0, y0, y1 in ((C["s12.a"], 460, 430), (C["s12.b"], 700, 730)):
            q = ep(t, t0, 0.5)
            if q > 0:
                M.arrow(c, 620, y0, 800, y1, COR, q, 4, 16, q)
        E.frase(c, t, C["s12.a"], [("três", "g", 150, COR)], 840, 470)
        E.frase(c, t, C["s12.a"] + 0.3, P("como um número normal", size=64), 840, 550, passo=0.12)
        E.frase(c, t, C["s12.b"], [("quartos", "g", 150, COR)], 840, 750)
        E.frase(c, t, C["s12.b"] + 0.3, P("o nome do pedaço", size=64), 840, 830, passo=0.12)
    E.saida(c, t, s13 - 0.1, regra)
    if t < s13 - 0.1:
        return

    def grade():
        E.frase(c, t, s13 + 0.1, P("são") + P("nove nomes", "g", 76, COR), W / 2, 150, "center")
        ts = [C["s13." + k] for k in "abcde"] + [C["s14." + k] for k in "abcd"]
        for i, ((n, nome), t0) in enumerate(zip(NOMES, ts)):
            x, y = XE + (i % 3) * 530, 275 + (i // 3) * 255

            def cel(a, i=i, n=n, nome=nome, x=x, y=y):
                E.escreve(c, str(n), x, y, 76, "g", COR, a)
                E.escreve(c, nome, x + (130 if n == 10 else 80), y, 80, "g", TINTA, a)
                chocolate(c, x, y + 26, 480, 86, n, [(0, COR, 1)], a)
            E.foco(c, t, t0, 0.45, cel)
    E.saida(c, t, s15 - 0.1, grade)
    if t < s15 - 0.1:
        return

    def plural():
        E.frase(c, t, s15 + 0.1, P("com mais de um pedaço,") + P("plural", "g", 76, COR), W / 2, 170, "center")
        for i, (t0, n, d, s1, s2) in enumerate(((C["s15.a"], 1, 5, "um quinto", ""), (C["s15.b"], 2, 5, "dois quinto", "s"), (C["s15.c"], 7, 8, "sete oitavo", "s"))):
            y = 340 + i * 240
            E.foco(c, t, t0, 0.5, lambda a, n=n, d=d, y=y: E.fracao(c, n, d, 280, y, 100, COR, a))

            def le(a, s1=s1, s2=s2, y=y):
                E.escreve(c, s1, 420, y + 30, 96, "g", TINTA, a)
                E.escreve(c, s2, 420 + E.larg(s1, "g", 96) + 2, y + 30, 96, "g", COR, a)
            E.foco(c, t, t0 + 0.1, 0.5, le)
            E.foco(c, t, t0 + 0.2, 0.5, lambda a, n=n, d=d, y=y: chocolate(c, 1040, y - 60, 680, 120, d, [(j, COR, 1) for j in range(n)], a))
    E.saida(c, t, s16 - 0.1, plural)
    if t < s16 - 0.1:
        return

    E.frase(c, t, s16 + 0.2, P("de") + P("11", "g", 76, COR) + P("em diante, a regra fica mais fácil"), W / 2, 170, "center", passo=0.14)
    E.frase(c, t, C["s16.a"] - 2.0, P("fale o de baixo e acrescente", size=72), W / 2 - 130, 290, "center", passo=0.13)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.pilula(c, "avos", 1460, 268, 76, estilo="g", cor=BR, a=a))
    y = 520
    for t0, n, d, x, nome in ((C["s16.b"], 1, 11, 400, "um onze"), (C["s16.c"], 5, 12, 960, "cinco doze"), (C["s16.d"], 3, 20, 1520, "três vinte")):
        fr(c, t, t0, n, d, x, y, 170, COR)
        E.foco(c, t, t0 + 0.15, 0.45, lambda a, x=x, nome=nome: (centro(c, nome, x - 60, 780, 76, "i", TINTA, a),
                                                                E.escreve(c, "avos", x - 60 + E.larg(nome, "i", 76) / 2 + 18, 780, 72, "g", COR, a)))
    E.frase(c, t, C["s16.d"] + 1.4, P("cem e mil têm nome próprio:", size=62) + P("centésimo e milésimo,", "b", 54, TINTA2) + P("em outra aula", size=62), W / 2, 930, "center", passo=0.13)


# ---------------- o traço é uma divisão ----------------
def b_traco(c, t, C, b):
    s18, s19 = C["s18"], C["s19"]
    ta, tb, tc, td = C["s18.a"], C["s18.b"], C["s18.c"], C["s18.d"]

    def divide():
        E.frase(c, t, C["s17"] + 0.3, P("aquele") + P("traço", "g", 76, COR) + P("também tem significado"), W / 2, 190, "center")
        cx, cy, s = 520, 540, 290
        lb = E.mix(TINTA, COR, ep(t, C["s17.a"], 0.4))
        E.foco(c, t, C["s17"] + 0.4, 0.5, lambda a: E.fracao(c, 12, 4, cx, cy, s, TINTA, a, barra=lb))
        sinal(c, t, C["s17.b"] - 0.1, "=", 960, cy, 170)
        E.frase(c, t, C["s17.b"], [("12 ÷ 4", "g", 200, COR)], 1090, cy + 72)
        E.frase(c, t, C["s17.a"], P("o traço da fração é uma") + P("divisão", "g", 76, COR), W / 2, 880, "center", passo=0.14)
    E.saida(c, t, s18 - 0.1, divide)
    if t < s18 - 0.1:
        return

    def barras():
        E.linha(c, t, [("12", "g", 84, COR, ta), ("barras inteiras", "i", 92, TINTA, ta + 0.1), ("para", "i", 92, TINTA, tb), ("4 pessoas", "g", 84, COR, tb + 0.1)], W / 2, 150, "center")
        w, h, px = 205, 64, 255
        q = ease_io(prog(t, tc, 0.9))
        for k in range(12):
            x0, y0 = XE + (k % 6) * px, 300 + (k // 6) * 95   # 12 juntas, em 2 fileiras
            x1, y1 = XE + (k % 4) * px, 220 + (k // 4) * 88   # uma coluna para cada pessoa
            p = prog(t, ta + k * 0.06, 0.35)
            chocolate(c, lerp(x0, x1, q), lerp(y0, y1, q), w, h, 4, [(i, COR, 1) for i in range(4)], M.clamp(p * 1.6))
        for i in range(4):
            cx = XE + i * px + w / 2
            E.foco(c, t, tb + 0.2 + i * 0.12, 0.4, lambda a, cx=cx: pessoa(c, cx, 640, 50, TINTA2, a))
            E.foco(c, t, tc + 0.7, 0.4, lambda a, cx=cx: centro(c, "3 barras", cx, 725, 60, "b", COR, a))
        y = 400
        fr(c, t, td, 12, 4, 1270, y, 130, COR)
        sinal(c, t, td + 0.2, "=", 1425, y, 110)
        E.foco(c, t, td + 0.3, 0.5, lambda a: (E.bola(c, 1600, y + 3, 125, a=a), centro(c, "3", 1600, y + 52, 150, "g", BR, a)))
        E.frase(c, t, td + 1.3, P("um número comum,", "g", 66) + P("escrito em forma de fração", size=74), W / 2, 880, "center", passo=0.13)
    E.saida(c, t, s19 - 0.1, barras)
    if t < s19 - 0.1:
        return

    E.frase(c, t, s19 + 0.2, P("de cima maior que o de baixo?", size=74) + P("outra aula", "g", 66, COR), W / 2, 280, "center", passo=0.12)
    E.frase(c, t, C["s19.a"] - 1.0, P("por enquanto, guarde", size=74, cor=COR), W / 2, 460, "center", passo=0.13)
    E.frase(c, t, C["s19.a"], P("traço", "g", 180, COR) + P("é", "i", 190) + P("divisão", "g", 180, COR), W / 2, 680, "center", passo=0.2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    x, y, w, h = 260, 215, 1400, 170
    lp = w / 4
    ta, tb, tc = C["s20.a"], C["s20.b"], C["s20.c"]
    s21, xa, xb, xc = C["s21"], C["s21.a"], C["s21.b"], C["s21.c"]
    yc = y + h + 14
    E.frase(c, t, C["s20"] + 0.2, P("cuidado", "g", 92, ERRADO) + P("com o erro mais comum", size=88), W / 2, 150, "center")
    ped = [(i, COR, prog(t, ta + i * 0.15, 0.35)) for i in range(3)]
    chocolate(c, x, y, w, h, 4, ped, ep(t, C["s20"] + 0.5, 0.5), 1.0)

    def rotulos():
        chave(c, x + 8, x + lp * 3 - 8, yc, COR, ep(t, ta, 0.4))
        E.foco(c, t, ta + 0.1, 0.4, lambda a: centro(c, "3 pintados", x + lp * 1.5, yc + 88, 66, "g", COR, a))
        chave(c, x + lp * 3 + 8, x + w - 8, yc, TINTA2, ep(t, tb, 0.4))
        E.foco(c, t, tb + 0.1, 0.4, lambda a: centro(c, "1 sem pintar", x + lp * 3.5, yc + 88, 66, "g", TINTA2, a))
    E.saida(c, t, xc - 0.15, rotulos, d=0.3)

    # a resposta errada: 3/1
    cy, s = 720, 160

    fr(c, t, tc, 3, 1, 330, cy, s, ERRADO)
    if t >= xc - 0.6:
        E.risco(c, 245, cy + 150, 415, cy - 150, t, xc - 0.6, largura=14)
    fica(c, t, tc + 0.2, s21 - 0.1, P("três", "g", 72) + P("em cima,", size=78) + P("um", "g", 72) + P("embaixo", size=78), 520, cy + 30, passo=0.14)

    # 3 ÷ 1 = 3 barras inteiras
    def seriam():
        E.frase(c, t, s21 + 0.2, P("mas o traço é divisão", size=72), 520, 640, passo=0.14)
        E.frase(c, t, xa, [("3 ÷ 1 = 3", "g", 84, ERRADO)], 520, 740)
        for i in range(3):
            E.foco(c, t, xb + i * 0.15, 0.4, lambda a, i=i: chocolate(c, 980 + i * 245, 660, 220, 90, 4, [(j, ERRADO, 1) for j in range(4)], a))
        E.frase(c, t, xb + 0.5, P("seriam") + P("3 barras", "g", 76, ERRADO), 980, 840, passo=0.14)
        E.frase(c, t, xb + 1.2, P("você tem", size=72) + P("menos de uma", "g", 66, COR), 520, 930, passo=0.14)
    E.saida(c, t, xc - 0.15, seriam, d=0.3)

    # o de baixo conta todos
    chave(c, x + 8, x + w - 8, yc, CERTO, ep(t, xc, 0.5))
    E.foco(c, t, xc + 0.1, 0.4, lambda a: centro(c, "4 pedaços no total", W / 2, yc + 88, 66, "g", CERTO, a))
    E.resultado(c, t, xc + 0.3, 3, 4, 1000, cy + 10, 116, 158, CERTO)
    E.frase(c, t, xc + 0.2, P("o de baixo conta", size=76), 1200, cy - 10, passo=0.12)
    E.frase(c, t, xc + 0.5, P("todos", "g", 76, CERTO) + P("os pedaços", size=76), 1200, cy + 80, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    s23 = C["s23"]
    ta, tb, tc, td = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]

    def tabuada():
        E.frase(c, t, C["s22"] + 0.3, P("e o atalho prometido", cor=CLARO), W / 2, 150, "center")
        E.frase(c, t, ta, P("a tabuada", "i", 124, CLARO) + P("ao contrário", "g", 112, BR), W / 2, 310, "center")
        cx, cy, s = 420, 620, 200
        fr(c, t, tb, 24, 6, cx, cy, s, BR)
        E.frase(c, t, tb + 1.3, P("não arme a conta", "i", 66, CLARO), cx, 910, "center", passo=0.12)
        y = cy + 52
        E.foco(c, t, tc, 0.5, lambda a: E.escreve(c, "6 ×", 740, y, 150, "g", BR, a))
        E.foco(c, t, tc + 0.3, 0.4, lambda a: E.escreve(c, "= 24", 1215, y, 150, "g", BR, a))
        E.saida(c, t, td - 0.1, lambda: E.foco(c, t, tc + 0.2, 0.4, lambda a: (E.caixa_pontilhada(c, 1000, cy - 90, 170, 180, a, CLARO),
                                                                                centro(c, "?", 1085, y, 150, "g", CLARO, a))), d=0.2)
        E.foco(c, t, td, 0.5, lambda a: (E.bola(c, 1085, cy + 3, 105, CERTO, a), centro(c, "4", 1085, y - 6, 140, "g", BR, a)))
    E.saida(c, t, s23 - 0.1, tabuada)
    if t < s23 - 0.1:
        return

    xa, xb, xc = C["s23.a"], C["s23.b"], C["s23.c"]
    E.frase(c, t, xa, P("dividir é o", cor=CLARO) + P("caminho de volta", "g", 76, BR) + P("de multiplicar", cor=CLARO), W / 2, 170, "center", passo=0.14)
    y = 350
    E.foco(c, t, xa + 0.2, 0.5, lambda a: centro(c, "6 × 4 = 24", 520, y, 110, "g", BR, a))
    p = ep(t, xa + 0.7, 0.6)
    if p > 0:
        M.arrow(c, 830, y - 52, 1090, y - 52, CLARO, p, 5, 18, p)
        M.arrow(c, 1090, y + 8, 830, y + 8, CLARO, p, 5, 18, p)
    E.foco(c, t, xa + 1.0, 0.5, lambda a: centro(c, "24 ÷ 6 = 4", 1400, y, 110, "g", CLARO, a))
    E.frase(c, t, xb - 2.8, P("quando não compensa?", "i", 86, CLARO), W / 2, 540, "center", passo=0.17)
    fr(c, t, xb, 612, 3, 420, 780, 130, BR)
    E.frase(c, t, xb - 1.0, P("fora da tabuada", "g", 66, BR), 640, 800, passo=0.15)
    # a conta armada
    gx, gy = 1250, 780
    E.foco(c, t, xc, 0.5, lambda a: (E.escreve(c, "612", gx, gy, 130, "g", BR, a), M.line(c, gx + 260, gy - 110, gx + 260, gy + 30, CLARO, a, 7),
                                     M.line(c, gx + 260, gy + 30, gx + 430, gy + 30, CLARO, a, 7), E.escreve(c, "3", gx + 300, gy, 130, "g", BR, a)))
    E.foco(c, t, xc + 0.3, 0.4, lambda a: E.pilula(c, "arme a conta", gx + 215, 920, 60, estilo="g", fundo=E.COR, cor=BR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ta, tb, tc = C["s24.a"], C["s24.b"], C["s24.c"]
    E.frase(c, t, C["s24"] + 0.3, P("hora de testar", size=72, cor=COR), XE, 170)
    E.frase(c, t, ta - 0.6, P("uma barra tem", size=80) + P("12", "g", 92, COR) + P("pedaços iguais", size=80), XE, 320, passo=0.14)
    E.foco(c, t, ta + 0.1, 0.5, lambda a: chocolate(c, XE, 370, 1100, 140, 12, [(i, COR, prog(t, tb + 0.1 + i * 0.12, 0.3)) for i in range(5)], a))
    E.frase(c, t, tb - 0.4, P("você comeu", size=80) + P("5", "g", 92, COR), XE, 640, passo=0.17)
    E.frase(c, t, tc, P("que fração da barra", size=100) + P("você comeu?", "g", 90, COR), XE, 820, passo=0.15)
    E.frase(c, t, tc + 1.3, P("e como ela", size=100) + P("se lê?", "g", 90, COR), XE, 950, passo=0.15)
    relogio(c, t, C["s25.a"], 1520, 340)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ta, tb, tc = C["s26.a"], C["s26.b"], C["s26.c"]
    x, y, w, h = 260, 230, 1400, 170
    lp = w / 12
    ped = [(i, COR, prog(t, C["s26"] + 0.3 + i * 0.1, 0.3)) for i in range(5)]
    chocolate(c, x, y, w, h, 12, ped, ep(t, C["s26"] + 0.2, 0.5), 1.0)
    yc = y + h + 14
    chave(c, x, x + w, y - 14, TINTA, ep(t, ta, 0.4), h=-20)
    E.foco(c, t, ta + 0.1, 0.4, lambda a: centro(c, "12 no total", W / 2, y - 54, 66, "b", TINTA, a))
    chave(c, x + 8, x + lp * 5 - 8, yc, COR, ep(t, tb, 0.4))
    E.foco(c, t, tb + 0.1, 0.4, lambda a: centro(c, "5 você pegou", x + lp * 2.5, yc + 80, 66, "b", COR, a))
    cx, cy, s = 500, 720, 190
    E.frac_q(c, t, C["s26"] + 0.5, 5, 12, tb, ta, cx, cy, s)
    E.frase(c, t, tc - 1.0, P("de onze em diante,", size=72) + P("avos", "g", 66, COR), 800, 650, passo=0.14)
    E.foco(c, t, tc, 0.5, lambda a: (M.rrect(c, 790, 700, 880, 170, 85, CERTO, a), centro(c, "cinco doze avos", 1230, 815, 96, "g", BR, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    s28 = C["s28"]

    def resumo():
        E.frase(c, t, C["s27"] + 0.3, P("resumindo", size=92, cor=COR), W / 2, 170, "center")
        for i, (t0, n, d, l1, l2) in enumerate(((C["s27.a"], "", 4, "o de baixo:", "em quantas partes"), (C["s27.b"], 3, "", "o de cima:", "quantas você pegou"), (C["s27.c"], None, None, "o traço:", "uma divisão"))):
            y = 370 + i * 215
            E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, 250, y - 30, 58, a=a), centro(c, str(i + 1), 250, y - 7, 64, "g", BR, a)))
            E.frase(c, t, t0 + 0.1, P(l1, size=88), 350, y - 8, passo=0.1)
            E.frase(c, t, t0 + 0.3, [(l2, "g", 88, COR)], 830, y - 8)
    E.saida(c, t, s28 - 0.1, resumo)
    if t < s28 - 0.1:
        return

    ta, tb, tc, td = C["s28.a"], C["s28.b"], C["s28.c"], C["s28.d"]
    E.frase(c, t, s28 + 0.2, P("próxima aula"), XE, 190)
    E.frase(c, t, s28 + 0.8, P("Fração de uma", "g", 112, COR), XE, 320, passo=0.13)
    E.frase(c, t, s28 + 1.2, P("quantidade", "g", 112, COR), XE, 440)
    y = 640
    fr(c, t, ta, 3, 4, 250, y, 96)
    E.frase(c, t, ta + 0.3, P("de", size=92) + P("20", "g", 88, COR), 345, y + 30, passo=0.15)
    E.frase(c, t, tb, P("o salário inteiro,", size=84), 720, y - 20, passo=0.15)
    E.frase(c, t, tb + 0.5, [("sabendo só uma parte", "g", 66, COR)], 720, y + 70)
    E.foco(c, t, tc, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1430, 300, 84, estilo="g", cor=BR, a=a))
    p = ease_io(prog(t, tc + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1620, p), lerp(560, 340, p), ep(t, tc + 0.2, 0.4), cor=TINTA)
    E.frase(c, t, td, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, barra=b_barra, nomes=b_nomes, leitura=b_leitura, traco=b_traco, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
