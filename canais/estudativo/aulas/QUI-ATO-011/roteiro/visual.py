"""Visual — Estudativo · QUI-ATO-011: energia de ionização e eletronegatividade.
Segue a linguagem visual da Química (QUI-MIS-001), a da trilha (QUI-ATO-001) e a do módulo Tabela periódica (QUI-ATO-008):
seta turquesa para cima e para a direita (energia de ionização e eletronegatividade), seta âmbar do raio quando ela volta
para comparar; cabo de guerra = dois átomos puxando o par de elétrons azul; a fila de eletronegatividade em pílulas.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-011_ionizacao_eletronegatividade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ionizacao", "eneg", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#F2A33A"
FILA = ["F", "O", "N", "Cl", "Br", "I", "S", "C", "P", "H"]
FRASE = ["Fui", "Ontem", "No", "Clube,", "Briguei,", "I", "Saí", "Correndo", "Para o", "Hospital"]
assert FILA.index("O") < FILA.index("Cl") and FILA.index("Cl") < FILA.index("H") and FILA.index("O") < FILA.index("S")
P = Q._posicoes()
assert P["O"][1:] == (2, 16) and P["F"][1:] == (2, 17) and P["Cl"][1:] == (3, 17) and P["S"][1:] == (3, 16)
assert P["K"][1:] == (4, 1) and P["Br"][1:] == (4, 17)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def ima(c, cx, cy, s, a=1.0):
    """ímã em U, de lado: polos para a direita"""
    if a <= 0:
        return
    w = s * 0.32
    pth = skia.Path()
    pth.addArc(skia.Rect.MakeXYWH(cx - s, cy - s, 2 * s, 2 * s), 90, 180)
    c.drawPath(pth, M.paint("#D9483B", a, stroke=w))
    M.line(c, cx, cy - s, cx + s * 0.6, cy - s, "#D9483B", a, w)
    M.line(c, cx, cy + s, cx + s * 0.6, cy + s, "#5B6470", a, w)
    M.rrect(c, cx + s * 0.6, cy - s - w / 2, s * 0.35, w, 4, "#C9CCD2", a)
    M.rrect(c, cx + s * 0.6, cy + s - w / 2, s * 0.35, w, 4, "#C9CCD2", a)


def clipe(c, x, y, a=1.0):
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - 22, 90, 44), 22, 22)
    c.drawRRect(r, M.paint("#8A8D96", a, stroke=7))
    r2 = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 14, y - 11, 60, 22), 11, 11)
    c.drawRRect(r2, M.paint("#8A8D96", a, stroke=6))


def tabela_seta(c, t, t0, x, y, cel, ts, destaque=(), cor=None, escuro=False, de=None, ate=None):
    Q.tabela(c, t, t0, x, y, cel, numeros=False, destaque=destaque, escuro=escuro)
    if ts is not None and t >= ts:
        p = ease_io(prog(t, ts, 0.9))
        x0, y0 = de or (x + 2 * cel, y + 6.5 * cel)
        x1, y1 = ate or (x + 16.5 * cel, y + 0.6 * cel)
        M.arrow(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor or E.COR, ep(t, ts, 0.3), max(10, cel * 0.25), max(30, cel * 0.8))


def cabo(c, t, t0, cx, cy, esq, dir_, puxa=0.0, a=1.0):
    """cabo de guerra: dois átomos e o par de elétrons entre eles; puxa < 0 vai para a esquerda, > 0 para a direita"""
    if t < t0:
        return
    q = ep(t, t0, 0.5) * a
    Q.atomo(c, cx - 260, cy, 80, esq, q)
    Q.atomo(c, cx + 260, cy, 80, dir_, q)
    M.line(c, cx - 180, cy, cx + 180, cy, TINTA2, 0.5 * q, 6)
    u = ease_io(prog(t, t0 + 0.6, 1.2)) * puxa
    px = cx + 120 * u
    E.bola(c, px - 16, cy, 15, Q.ELETRON, q)
    E.bola(c, px + 16, cy, 15, Q.ELETRON, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("sódio", "g", 70), ("+", "g", 70, TINTA2), ("cloro", "g", 70)] + ps("= sal de cozinha", "i", 70), XE, 260, passo=0.15)
        Q.atomo_em(c, t, C["s01.a"] + 0.5, 1250, 560, 100, "Na")
        Q.atomo_em(c, t, C["s01.a"] + 0.8, 1650, 560, 80, "Cl")
        if t >= C["s01.b"]:
            u = ease_io(prog(t, C["s01.b"] + 0.5, 1.4))
            E.bola(c, lerp(1360, 1560, u), 560 - 140 * math.sin(math.pi * u), 18, Q.ELETRON)
        E.frase(c, t, C["s01.b"], ps("um entrega um elétron, o outro recebe", "i", 60), XE, 400, passo=0.08)
        E.frase(c, t, C["s01.c"], [("quem entrega?", "g", 80, COR)], XE, 820)
        E.frase(c, t, C["s01.d"], ps("a tabela responde com", "i", 60) + [("duas setas", "g", 58)], XE, 940, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("quem", "i", 70), ("perde elétron", "g", 66, COR), ("fácil", "i", 70)]),
                 (C["s02.b"], [("quem", "i", 70), ("puxa mais", "g", 66, COR), ("os elétrons", "i", 70)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("o raio cresce", "i", 66) + [("para baixo e para a esquerda", "g", 60, AMBAR)], XE, 320, passo=0.12)
    tabela_seta(c, t, C["s03.a"] + 0.2, 500, 420, 50, C["s03.a"] + 1.0, cor=AMBAR, de=(500 + 16.5 * 50, 420 + 0.6 * 50), ate=(500 + 1.5 * 50, 420 + 6.4 * 50))
    E.frase(c, t, C["s03.b"], ps("átomo menor: elétrons de fora", "i", 60) + [("mais perto do núcleo", "g", 56)], XE, 860, passo=0.1)


# ---------------- energia de ionização ----------------
def b_ionizacao(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("energia de ionização", "g", 80, COR)], XE, 200)
        E.frase(c, t, C["s04.a"] + 1.0, ps("a energia para arrancar um elétron", "i", 60), XE, 300, passo=0.08)
        E.frase(c, t, C["s04.a"] + 2.6, ps("do átomo sozinho, no estado gasoso", "i", 52, TINTA2), XE, 380, passo=0.08)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: ima(c, 600, 720, 120, a))
        perto = t < C["s04.d"]
        xc = 700 + 20 if perto else 1100
        if t >= C["s04.b"] + 0.4:
            xr = lerp(740, 1130, ease_io(prog(t, C["s04.d"], 0.8)))
            clipe(c, xr, 610, ep(t, C["s04.b"] + 0.4, 0.4))
        E.frase(c, t, C["s04.c"], ps("perto: difícil de puxar", "i", 58), 1350, 520, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("longe: sai fácil", "i", 58), 1350, 760, passo=0.1)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("átomo pequeno: elétron de fora", "i", 62) + [("perto do núcleo", "g", 58)], XE, 200, passo=0.1)
        E.frase(c, t, C["s05.b"], ps("anda ao contrário do raio:", "i", 62), XE, 310, passo=0.1)
        tabela_seta(c, t, C["s05"] + 0.2, 380, 420, 64, C["s05.c"])
        E.foco(c, t, C["s05.c"] + 0.5, 0.4, lambda a: E.pilula(c, "cresce para cima e para a direita", 1250, 330, 50, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s06.a"], [("Na", "g", 66), ("e", "i", 70), ("Cl", "g", 66)] + ps("no 3º período", "i", 70), XE, 200, passo=0.12)
    Q.tabela(c, t, C["s06"] + 0.2, XE, 290, 50, numeros=False, destaque=("Na", "Cl"))
    Q.atomo_em(c, t, C["s06.b"], 1300, 560, 120, "Na")
    E.foco(c, t, C["s06.c"], 0.4, lambda a: E.pilula(c, "ionização baixa: perde fácil", 1300, 760, 44, "g", fundo=E.COR, a=a))
    Q.atomo_em(c, t, C["s06.d"], 1680, 560, 80, "Cl")
    E.foco(c, t, C["s06.d"] + 0.3, 0.4, lambda a: E.pilula(c, "segura os seus", 1680, 860, 44, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s06.e"], ps("quem entrega:", "i", 66) + [("o sódio", "g", 66, COR)], XE, 760, passo=0.12)
    pilula_em(c, t, C["s06.f"], "como se juntam depois: outra aula", XE + 400, 900, 44, TINTA2, "b")


# ---------------- eletronegatividade ----------------
def b_eneg(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("eletronegatividade", "g", 90, COR)], XE, 220)
        E.frase(c, t, C["s07.b"], ps("a força com que o átomo puxa os elétrons", "i", 58), XE, 330, passo=0.08)
        E.frase(c, t, C["s07.b"] + 2.4, ps("quando está preso a outro átomo", "i", 58), XE, 410, passo=0.08)
        E.frase(c, t, C["s07.c"], ps("um", "i", 62) + [("cabo de guerra", "g", 60)] + ps("pelos elétrons", "i", 62), XE, 560, passo=0.1)
        cabo(c, t, C["s07.c"] + 0.4, W / 2, 800, "H", "Cl", puxa=1.0 if t >= C["s07.d"] else 0.0)
        E.foco(c, t, C["s07.d"] + 1.0, 0.4, lambda a: E.pilula(c, "puxa mais: mais eletronegativo", W / 2 + 260, 950, 44, "g", fundo=E.COR, a=a))
        return
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("também cresce", "i", 62) + [("para cima e para a direita", "g", 58, COR)], XE, 200, passo=0.1)
        tabela_seta(c, t, C["s08"] + 0.2, 380, 330, 64, C["s08.a"] + 0.4, destaque=("F",) if t >= C["s08.c"] else (),
                    ate=(380 + 16.4 * 64, 330 + 1.3 * 64))
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "flúor, o campeão", 380 + 16.5 * 64, 330 + 1.5 * 64 - 110, 50, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s08.d"], ps("o elemento mais eletronegativo de todos", "i", 58, TINTA2), XE, 900, passo=0.08)
        return
    E.frase(c, t, C["s09.a"], [("F,", "g", 66), ("O", "g", 66), ("e", "i", 70), ("Cl", "g", 66)], XE, 190, passo=0.15)
    Q.tabela(c, t, C["s09"] + 0.2, 1000, 260, 44, numeros=False, destaque=("F", "O", "Cl"))
    E.frase(c, t, C["s09.b"], ps("O e F: 2º período", "i", 58), XE, 360, passo=0.08)
    E.frase(c, t, C["s09.c"], [("F", "g", 60, COR)] + ps(", à direita, ganha", "i", 60), XE, 460, passo=0.08)
    E.frase(c, t, C["s09.d"], ps("F e Cl: família 17", "i", 58), XE, 600, passo=0.08)
    E.frase(c, t, C["s09.e"], [("F", "g", 60, COR)] + ps(", em cima, ganha", "i", 60), XE, 700, passo=0.08)
    E.foco(c, t, C["s09.f"], 0.5, lambda a: E.pilula(c, "F é o mais eletronegativo dos três", W / 2, 900, 60, "g", fundo=E.COR, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("gases nobres, os mais eletronegativos?", "i", 62), XE, 310, passo=0.1)
    if t >= C["s10.b"]:
        E.risco(c, XE, 325, XE + 1080, 260, t, C["s10.b"], largura=12)
    Q.tabela(c, t, C["s10.a"] + 0.4, 500, 420, 54, numeros=False, familia=18, cor="#9B84D9")
    E.frase(c, t, C["s10.b"], ps("quase não se prendem a outros átomos", "i", 58), XE, 880, passo=0.08)
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "ficam fora da escala", 1450, 980, 56, "g", fundo="#7A5FC0", a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], [("O", "g", 66, BR)] + ps("contra", "i", 66, CLARO) + [("Cl?", "g", 66, BR)], W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s11.b"], ps("em diagonal: as setas brigam", "i", 60, CLARO), W / 2, 270, "center", 0.1)
        E.frase(c, t, C["s11.c"], ps("a fila de prova, com uma frase:", "i", 60, CLARO), W / 2, 400, "center", 0.1)
        for k, (w_, el) in enumerate(zip(FRASE, FILA)):
            x = 170 + k * 162
            ti = C["s11.d"] + 0.3 * k
            E.foco(c, t, ti, 0.35, lambda a, x=x, w_=w_: centro(c, w_, x + 60, 560, 40, "i", CLARO, a))
            E.foco(c, t, ti + 0.1, 0.35, lambda a, x=x, el=el, k=k: (M.rrect(c, x, 600, 120, 110, 18, E.COR if el in ("O", "Cl") else "#22232B", a),
                                                                    centro(c, el, x + 60, 680, 64, "g", BR, a)))
        E.frase(c, t, C["s11.d"] + 3.4, ps("do mais para o menos eletronegativo", "i", 54, CLARO), W / 2, 820, "center", 0.08)
        return
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("cada inicial é um elemento, na ordem que as provas usam", "i", 52, CLARO), W / 2, 200, "center", 0.06)
        for k, el in enumerate(FILA):
            x = 170 + k * 162
            E.foco(c, t, C["s12.b"] + 0.35 * k, 0.35, lambda a, x=x, el=el: (M.rrect(c, x, 380, 120, 110, 18, E.COR if el in ("O", "Cl") else "#22232B", a),
                                                                            centro(c, el, x + 60, 460, 64, "g", BR, a),
                                                                            centro(c, Q.NOMES[el], x + 60, 540, 30, "m", CLARO, a)))
        if t >= C["s12.c"]:
            E.foco(c, t, C["s12.c"], 0.4, lambda a: (M.arrow(c, 170 + 162 + 60, 640, 170 + 3 * 162 + 60, 640, E.CLARO, a, 6, 22)))
        E.frase(c, t, C["s12.d"], [("O", "g", 66, BR), (">", "g", 66, E.CLARO), ("Cl", "g", 66, BR)] + ps(": oxigênio mais eletronegativo", "i", 60, CLARO), W / 2, 820, "center", 0.12)
        return
    E.frase(c, t, C["s13.a"], ps("a fila resolve as diagonais", "i", 64, CLARO) + [("desses 10", "g", 60, BR)], W / 2, 330, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("não", "g", 62, ERRADO)] + ps("serve para a energia de ionização:", "i", 62, CLARO), W / 2, 520, "center", 0.1)
    E.frase(c, t, C["s13.c"], ps("para ela, use as", "i", 64, CLARO) + [("setas", "g", 62, BR)], W / 2, 640, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14.a"], [("1", "g", 56, COR)] + ps("do mais para o menos eletronegativo:", "i", 58), XE, 320, passo=0.08)
    E.foco(c, t, C["s14.a"] + 2.4, 0.4, lambda a: E.formula(c, "F, O, S", XE + 60, 430, 84, "g", TINTA, a))
    E.frase(c, t, C["s14.b"], [("2", "g", 56, COR)] + ps("potássio ou bromo, do 4º período:", "i", 58), XE, 600, passo=0.08)
    E.frase(c, t, C["s14.c"], ps("quem perde elétron mais fácil?", "i", 58), XE + 60, 700, passo=0.08)
    if t < C["s15"]:
        Q.tabela(c, t, C["s14.a"], 1080, 300, 40, numeros=False, destaque=("F", "O", "S", "K", "Br"))
    else:
        E.relogio(c, t, C["s15.a"], cx=1540, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    Q.tabela(c, t, C["s16"], 1020, 250, 44, numeros=False, destaque=("F", "O", "S") if t < C["s16.d"] else ("K", "Br"))
    E.frase(c, t, C["s16.a"], ps("F à direita do O:", "i", 58) + [("F ganha", "g", 56, COR)], XE, 230, passo=0.08)
    E.frase(c, t, C["s16.b"], ps("O em cima do S:", "i", 58) + [("O ganha", "g", 56, COR)], XE, 340, passo=0.08)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.formula(c, "F > O > S", XE, 480, 96, "g", TINTA, a))
    E.foco(c, t, C["s16.c"] + 0.3, 0.4, lambda a: E.selo(c, XE + 560, 450, 40, True, a))
    E.frase(c, t, C["s16.d"], ps("K, à esquerda: maior,", "i", 58), XE, 680, passo=0.08)
    E.frase(c, t, C["s16.d"] + 1.6, ps("energia de ionização mais baixa", "i", 58), XE, 770, passo=0.08)
    E.foco(c, t, C["s16.e"], 0.5, lambda a: E.pilula(c, "o potássio perde mais fácil", XE + 380, 900, 60, "g", fundo=E.COR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        tabela_seta(c, t, C["s17.a"], 1100, 560, 38, C["s17.a"] + 0.4)
        E.frase(c, t, C["s17.a"], [("ionização", "g", 60, COR), ("e", "i", 64), ("eletronegatividade:", "g", 60, COR)], XE, 340, passo=0.1)
        E.frase(c, t, C["s17.a"] + 1.4, ps("para cima e para a direita", "i", 62), XE, 430, passo=0.1)
        E.frase(c, t, C["s17.b"], ps("ao contrário do raio", "i", 58, TINTA2), XE, 520, passo=0.1)
        E.frase(c, t, C["s17.c"], [("flúor:", "g", 62, COR)] + ps("o mais eletronegativo", "i", 62), XE, 700, passo=0.1)
        E.frase(c, t, C["s17.d"], ps("metais da esquerda:", "i", 62) + [("perdem fácil", "g", 60)], XE, 820, passo=0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("praticando:", "g", 80, COR)], XE, 400)
    E.frase(c, t, C["s18.a"] + 0.6, ps("a tabela inteira", "i", 72), XE, 510, passo=0.12)
    E.frase(c, t, C["s18.b"], ps("questões no estilo da prova", "i", 60, TINTA2), XE, 620, passo=0.1)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ionizacao=b_ionizacao, eneg=b_eneg, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
