"""Visual — Estudativo · QUI-ATO-008: períodos e famílias. Primeira aula do módulo Tabela periódica.

Segue a linguagem visual da Química (QUI-MIS-001) e a da trilha (QUI-ATO-001). Acréscimos do MÓDULO TABELA PERIÓDICA
(as aulas QUI-ATO-009 a 012 copiam daqui):
- A TABELA é sempre Q.tabela: células brancas com fio cinza; o que a fala destaca fica na cor da matéria (familia=,
  periodo=, destaque=). Números das famílias em cima e dos períodos à esquerda, em cinza-tinta. Tabela inteira com
  cel ≈ 66 a 70; recorte (grupos_=, periodos=) quando só uma parte importa, com cel ≥ 90.
- A CASA de um elemento = casa(): cartão branco com o número atômico no alto à esquerda, o símbolo grande no meio, o nome
  embaixo e a massa atômica em cinza; cada parte com rótulo e seta na hora da fala. Candidata ao kit (Q.casa).
- PERÍODO = faixa deitada (linha); FAMÍLIA = faixa em pé (coluna). Nunca as duas na mesma cor ao mesmo tempo: a família
  em turquesa, o período em contorno tracejado turquesa (moldura_periodo()).
- NUMERAÇÃO ANTIGA (1A a 8A) em pílulas escuras acima das colunas, sob os números atuais.
- PROPRIEDADES PERIÓDICAS (010 a 012): seta grossa sobre a tabela, na direção em que a propriedade cresce: raio em âmbar
  (para baixo e para a esquerda), energia de ionização e eletronegatividade em turquesa (para cima e para a direita).
  Metais em azul-acinzentado claro, ametais em turquesa claro, gases nobres em lilás claro (cores fixas do módulo).
- DISTRIBUIÇÃO: E.formula("1s^{2} ..."), a camada de valência na cor da matéria com a chave embaixo (como na QUI-ATO-006).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-008_periodos_e_familias.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ordem", "periodo", "familia", "exemplo", "atalho", "questao", "fim"))
BR = "#FFFFFF"

TX, TY, TC = 330, 330, 70           # tabela inteira


def posicao(s):
    """(Z, período, família) pela tabela do kit"""
    return Q._posicoes()[s]


assert posicao("Na") == (11, 3, 1) and posicao("Cl")[1:] == (3, 17) and posicao("Fe")[1:] == (4, 8)
assert posicao("F")[1:] == (2, 17) and posicao("N")[1:] == (2, 15) and posicao("Ca")[1:] == (4, 2)
assert Q.distribuicao(9)[-1] == ("2p", 5) and 2 + 5 == 7 and Q.distribuicao(7)[-1] == ("2p", 3) and 2 + 2 + 3 == 7
assert Q.distribuicao(26)[-2:] == [("4s", 2), ("3d", 6)] and 2 + 6 == 8
assert Q.distribuicao(17)[-2:] == [("3s", 2), ("3p", 5)]


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


def casa(c, cx, cy, w, z, sim, nome, massa, a=1.0, cor=None):
    """a casa de um elemento na tabela (cartão branco): Z no alto à esquerda, símbolo, nome e massa atômica"""
    if a <= 0:
        return
    h = w * 1.18
    x, y = cx - w / 2, cy - h / 2
    M.rrect(c, x, y, w, h, w * 0.08, "#FFFFFF", a, shadow=True)
    c.drawRoundRect(skia.Rect.MakeXYWH(x, y, w, h), w * 0.08, w * 0.08, M.paint(cor or E.COR, a, stroke=max(3, w * 0.012)))
    E.escreve(c, str(z), x + w * 0.08, y + w * 0.2, w * 0.14, "g", COR, a)
    centro(c, sim, cx, y + h * 0.58, w * 0.42, "g", TINTA, a)
    centro(c, nome, cx, y + h * 0.76, w * 0.11, "m", TINTA, a)
    centro(c, massa, cx, y + h * 0.9, w * 0.1, "m", TINTA2, a)
    return x, y, w, h


def moldura_periodo(c, t, t0, per, x=TX, y=TY, cel=TC, cor=None):
    """contorno tracejado em volta de um período (linha) da tabela"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    yy = y + (per - 1) * cel
    pth = skia.Path(); pth.addRoundRect(skia.Rect.MakeXYWH(x - 6, yy - 4, 18 * cel + 12, cel + 8), 12, 12)
    p = M.paint(cor or E.COR, q, stroke=6)
    p.setPathEffect(skia.DashPathEffect.Make([18, 10], 0))
    c.drawPath(pth, p)


def termo(sub, n):
    return f"{sub}^{{{n}}}"


def dist(c, t, itens, tl, x, y, size, cores=None):
    xx, caixas = x, []
    for k, ((s, n), ti) in enumerate(zip(itens, tl)):
        txt = termo(s, n)
        w = E.formula(None, txt, 0, 0, size, "g", a=0)
        cor = (cores or {}).get(k, TINTA)
        E.foco(c, t, ti, 0.4, lambda a, txt=txt, xx=xx, cor=cor: E.formula(c, txt, xx, y, size, "g", cor, a))
        caixas.append((xx, xx + w))
        xx += w + size * 0.32
    return caixas


def antiga(c, t, t0, x=TX, y=TY, cel=TC, dy=-60):
    """numeração antiga 1A a 8A acima das colunas representativas"""
    for k, g in enumerate((1, 2, 13, 14, 15, 16, 17, 18)):
        E.foco(c, t, t0 + 0.15 * k, 0.4, lambda a, g=g, k=k: E.pilula(c, f"{k + 1}A", x + (g - 1) * cel + cel / 2, y + dy, 34, "g", fundo=TINTA, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        Q.tabela(c, t, C["s01.a"], TX, 300, TC, numeros=False, d=1.4)
        E.frase(c, t, C["s01.a"] + 0.2, [("118", "g", 90, COR)] + ps("quadradinhos para decorar?", "i", 76), W / 2, 200, "center", 0.12)
        if t >= C["s01.b"]:
            E.risco(c, W / 2 - 120, 215, W / 2 + 560, 150, t, C["s01.b"], largura=12)
            E.foco(c, t, C["s01.b"] + 0.3, 0.4, lambda a: E.pilula(c, "não precisa", W / 2, 920, 70, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s01.c"], ps("o lugar sai da", "i", 66) + [("distribuição", "g", 62, COR)], W / 2, 1030, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("o", "i", 70), ("período", "g", 66, COR)]),
                 (C["s02.b"], [("a", "i", 70), ("família", "g", 66, COR)]),
                 (C["s02.c"], [("ler uma", "i", 70), ("casa", "g", 66)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das aulas anteriores", "i", 70, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("Z", "g", 70, COR)] + ps("= número de prótons", "i", 72), XE, 380, passo=0.12)
    E.frase(c, t, C["s03.b"], [("valência", "g", 70, COR)] + ps("= a camada de número maior", "i", 72), XE, 540, passo=0.12)
    E.formula_em(c, t, C["s03.b"] + 1.4, "1s^2 2s^2 2p^6 3s^1", XE, 720, 96, "g", TINTA)
    E.foco(c, t, C["s03.b"] + 2.0, 0.4, lambda a: E.formula(c, "3s^1", XE + E.formula(None, "1s^2 2s^2 2p^6 ", 0, 0, 96, "g", a=0), 720, 96, "g", COR, a))


# ---------------- a ordem da tabela ----------------
def b_ordem(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("em ordem de", "i", 64) + [("Z", "g", 64, COR)] + ps(": 1, 2, 3...", "i", 64), XE, 200, passo=0.1)
    fam = 1 if t >= C["s04.d"] else None
    Q.tabela(c, t, C["s04"] + 0.2, TX, TY, TC, z=True, familia=fam, d=1.2)
    if t >= C["s04.b"]:
        # o caminho da leitura: H → He, depois Li → Ne...
        p = ease_io(prog(t, C["s04.b"], 1.6))
        pts = [(TX + TC / 2, TY + TC / 2), (TX + 17.5 * TC, TY + TC / 2), (TX + TC / 2, TY + 1.5 * TC), (TX + 17.5 * TC, TY + 1.5 * TC)]
        for (x0, y0), (x1, y1), k in zip(pts, pts[1:], range(3)):
            u = min(1, max(0, p * 3 - k))
            if u > 0 and k != 1:
                M.arrow(c, x0, y0 - 2, lerp(x0, x1, u), y0 - 2, "#F2A33A", 0.9, 6, 20)
    if t >= C["s04.c"]:
        moldura_periodo(c, t, C["s04.c"], 3)
        E.foco(c, t, C["s04.c"] + 0.4, 0.4, lambda a: E.pilula(c, "período: linha deitada (são 7)", 600, 940, 46, "g", fundo=E.COR, a=a))
    if t >= C["s04.d"]:
        E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: E.pilula(c, "família: coluna em pé (são 18)", 1330, 1010, 46, "g", fundo=TINTA, a=a))


# ---------------- a casa ----------------
def b_casa(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("a casa de um elemento", "i", 70), XE, 200, passo=0.12)
        CX, CY, CW = 1300, 580, 440
        E.foco(c, t, C["s05.a"] + 0.3, 0.6, lambda a: casa(c, CX, CY, CW, 11, "Na", "sódio", "22,99", a))
        h = CW * 1.18
        x, y = CX - CW / 2, CY - h / 2
        rotulos = (("s05.b", "símbolo", CX - CW * 0.3, y + h * 0.5), ("s05.c", "nome", CX - CW * 0.2, y + h * 0.74),
                   ("s05.d", "número atômico", x + CW * 0.05, y + CW * 0.13), ("s05.e", "massa atômica", CX - CW * 0.2, y + h * 0.88))
        for k, (ck, txt, px, py) in enumerate(rotulos):
            yy = 340 + k * 140
            E.foco(c, t, C[ck], 0.4, lambda a, txt=txt, yy=yy, px=px, py=py: (E.escreve(c, txt, XE, yy, 58, "g", COR if txt != "massa atômica" else TINTA2, a),
                                                                            M.arrow(c, XE + E.larg(txt, "g", 58) + 20, yy - 18, px, py, E.COR, a, 4, 16)))
        pilula_em(c, t, C["s05.e"] + 1.4, "massa atômica: outra aula", XE + 300, 960, 44, TINTA2, "b")
        return
    E.frase(c, t, C["s06.a"], ps("o lugar de cada número", "i", 70) + [("muda", "g", 66, COR)], XE, 260, passo=0.12)
    E.frase(c, t, C["s06.a"] + 1.2, ps("de uma tabela para outra", "i", 70), XE, 360, passo=0.12)
    E.foco(c, t, C["s06.a"] + 0.4, 0.5, lambda a: casa(c, 1150, 700, 300, 11, "Na", "sódio", "22,99", a))
    E.foco(c, t, C["s06.a"] + 0.8, 0.5, lambda a: (M.rrect(c, 1400, 523, 300, 354, 24, "#FFFFFF", a, shadow=True),
                                                  centro(c, "22,99", 1550, 590, 40, "m", TINTA2, a), centro(c, "Na", 1550, 730, 126, "g", TINTA, a),
                                                  centro(c, "11", 1550, 820, 48, "g", COR, a)))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.pilula(c, "leia sempre a legenda", XE + 330, 560, 60, "g", fundo=E.COR, a=a))


# ---------------- período ----------------
def b_periodo(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("período", "g", 80, COR)] + ps("= número de camadas", "i", 70), XE, 190, passo=0.12)
    E.frase(c, t, C["s07.b"], ps("o maior número de camada da distribuição", "i", 56, TINTA2), XE, 280, passo=0.08)
    Q.tabela(c, t, C["s07"] + 0.2, TX, 420, TC, destaque=("Na",) if t >= C["s07.d"] else ())
    if t >= C["s07.c"]:
        dist(c, t, Q.distribuicao(11), [C["s07.c"]] * 4, XE, 1000, 84, cores={3: COR})
    if t >= C["s07.d"]:
        moldura_periodo(c, t, C["s07.d"], 3, TX, 420)
        E.foco(c, t, C["s07.d"] + 0.4, 0.4, lambda a: E.pilula(c, "3 camadas: 3º período", 1420, 980, 54, "g", fundo=E.COR, a=a))


# ---------------- família ----------------
def b_familia(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("família", "g", 80, COR)] + ps("= mesmo número de elétrons na valência", "i", 58), XE, 190, passo=0.1)
        Q.tabela(c, t, C["s08"] + 0.2, TX, 360, TC, familia=1 if t >= C["s08.c"] else None, destaque=("Na",))
        if t >= C["s08.b"]:
            dist(c, t, Q.distribuicao(11), [C["s08.b"]] * 4, XE, 940, 72, cores={3: COR})
            E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "1 elétron: família 1", 1450, 920, 50, "g", fundo=E.COR, a=a))
        if t >= C["s08.d"]:
            for k, (el, d_) in enumerate((("Li", "2s^1"), ("K", "4s^1"))):
                E.foco(c, t, C["s08.d"] + 0.4 * k, 0.4, lambda a, k=k, el=el, d_=d_: (E.formula(c, el, XE + k * 440, 1040, 60, "g", TINTA, a),
                                                                                      E.formula(c, "... " + d_, XE + 90 + k * 440, 1040, 60, "g", COR, a)))
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09.a"], ps("famílias 1 e 2:", "i", 60) + [("família = elétrons na valência", "g", 56, COR)], XE, 190, passo=0.1)
        E.frase(c, t, C["s09.b"], ps("famílias 13 a 18:", "i", 60), XE, 290, passo=0.1)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "tire 10", XE + 640, 270, 56, "g", fundo=E.COR, a=a))
        Q.tabela(c, t, C["s09"] + 0.2, TX, 420, TC, familia=17 if t >= C["s09.d"] else None)
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.formula(c, "17 − 10 = 7", 880, 340, 70, "g", TINTA, a))
        if t >= C["s09.e"]:
            E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "He: 2, a exceção", TX + 17.5 * TC, 420 - 40, 40, "g", fundo=ERRADO, a=a))
        return
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("a numeração antiga, com a letra", "i", 60) + [("A", "g", 60, COR)], XE, 190, passo=0.1)
        Q.tabela(c, t, C["s10"] + 0.2, TX, 420, TC, familia=17 if t >= C["s10.d"] else None)
        antiga(c, t, C["s10.b"], TX, 420, TC, -80)
        E.frase(c, t, C["s10.c"], ps("o número já é o de elétrons na valência", "i", 58, TINTA2), XE, 300, passo=0.08)
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.pilula(c, "7A = família 17", 1450, 960, 56, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s11.a"], ps("famílias 3 a 12:", "i", 60) + [("transição", "g", 58, COR)] + ps("(letra B na antiga)", "i", 52, TINTA2), XE, 190, passo=0.1)
    Q.tabela(c, t, C["s11"] + 0.2, TX, 360, TC, destaque=tuple(s for s, (z, per, g) in Q._posicoes().items() if g and 3 <= g <= 12 and per <= 7)
             if t < C["s11.e"] else ("Fe",))
    E.frase(c, t, C["s11.b"], ps("terminam em", "i", 58) + [("d", "g", 56, COR)], XE, 920, passo=0.1)
    E.frase(c, t, C["s11.c"], ps("família = último s + d", "i", 58), XE + 470, 920, passo=0.1)
    if t >= C["s11.d"]:
        E.formula_em(c, t, C["s11.d"], "Fe: ... 4s^2 3d^6", XE, 1030, 68, "g", TINTA)
        E.foco(c, t, C["s11.e"], 0.4, lambda a: E.pilula(c, "2 + 6 = família 8, período 4", 1380, 1010, 48, "g", fundo=E.COR, a=a))


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    E.frase(c, t, C["s12"], ps("um exemplo completo", "i", 70, TINTA2), XE, 190, passo=0.12)
    cx = dist(c, t, Q.distribuicao(9), [C["s12.a"]] * 3, XE, 380, 110, cores={1: COR, 2: COR} if t >= C["s12.c"] else None)
    if t >= C["s12.c"]:
        E.chave(c, cx[1][0], cx[2][1], 410, E.COR, ep(t, C["s12.c"], 0.5), 26)
    E.frase(c, t, C["s12.b"], ps("maior número:", "i", 62) + [("2", "g", 60)] + [("→", "g", 60, TINTA2)] + [("2º período", "g", 60, COR)], XE, 560, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("camada 2:", "i", 62) + [("2 + 5 = 7", "g", 60)] + [("→", "g", 60, TINTA2)] + [("família 17 (7A)", "g", 60, COR)], XE, 680, passo=0.1)
    E.frase(c, t, C["s12.e"], [("2 + 2 + 5 = 9", "g", 60)] + ps("elétrons:", "i", 62) + [("flúor", "g", 60)], XE, 800, passo=0.1)
    Q.tabela(c, t, C["s12.a"], 1200, 330, 36, numeros=False, destaque=("F",) if t >= C["s12.d"] else ())


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("tirar o período do", "i", 64) + [("último subnível escrito", "g", 60)], XE, 310, passo=0.1)
    FE = Q.distribuicao(26)
    cx = dist(c, t, FE, [C["s13.b"]] * 7, XE, 480, 84, cores={6: ERRADO} if t < C["s13.d"] else {5: COR})
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "3º período?", cx[6][1] + 210, 450, 50, "g", fundo=ERRADO, a=a))
    if t >= C["s13.d"]:
        E.risco(c, cx[6][1] + 90, 470, cx[6][1] + 340, 420, t, C["s13.d"], largura=9)
        E.chave(c, cx[5][0], cx[5][1], 510, E.COR, ep(t, C["s13.d"] + 0.3, 0.5), 26)
        E.frase(c, t, C["s13.d"] + 0.3, ps("o maior número de camada é o 4", "i", 60), XE, 660, passo=0.1)
    E.foco(c, t, C["s13.e"], 0.5, lambda a: E.pilula(c, "o ferro está no 4º período", XE + 380, 790, 60, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s13.f"], ps("o período vem da camada de fora", "i", 58, TINTA2), XE, 930, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho de prova", "i", 70, CLARO), W / 2, 160, "center", 0.12)
        E.frase(c, t, C["s14.a"], [("1", "g", 62, E.CLARO)] + ps("maior número de camada", "i", 64, CLARO) + [("= período", "g", 62, BR)], XE, 300, passo=0.1)
        E.frase(c, t, C["s14.c"], [("2", "g", 62, E.CLARO)] + ps("some os elétrons dessa camada", "i", 64, CLARO) + [("= família", "g", 62, BR)], XE, 420, passo=0.1)
        E.frase(c, t, C["s14.d"], ps("(na numeração antiga, com A)", "i", 54, CLARO), XE + 110, 500, passo=0.08)
        E.formula_em(c, t, C["s14.e"], "... 3s^2 3p^5", W / 2, 700, 120, "g", BR, "center")
        E.foco(c, t, C["s14.e"] + 1.2, 0.4, lambda a: E.pilula(c, "período 3", W / 2 - 260, 880, 60, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s14.e"] + 2.0, 0.4, lambda a: E.pilula(c, "2 + 5: família 7A", W / 2 + 240, 880, 60, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s15.a"], ps("período e família dependem só da", "i", 64, CLARO) + [("camada de fora", "g", 60, BR)], W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO), ("vale", "i", 66, CLARO)] + ps("para os de transição:", "i", 66, CLARO), W / 2, 480, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("some também os elétrons do", "i", 64, CLARO) + [("d", "g", 64, BR)], W / 2, 600, "center", 0.12)
    E.formula_em(c, t, C["s15.d"], "Fe: 4s^2 + 3d^6 → família 8", W / 2, 800, 84, "g", E.CLARO, "center")


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.formula_em(c, t, C["s16.a"], "1s^2 2s^2 2p^3", XE, 400, 140, "g", TINTA)
    E.frase(c, t, C["s16.b"], [("1", "g", 56, COR)] + ps("em que período e família?", "i", 60), XE, 600, passo=0.08)
    E.frase(c, t, C["s16.c"], [("2", "g", 56, COR)] + ps("qual é o Z?", "i", 60), XE, 720, passo=0.08)
    if t < C["s17"]:
        Q.tabela(c, t, C["s16.b"], 1150, 300, 38, numeros=True)
    else:
        E.relogio(c, t, C["s17.a"], cx=1540, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    cx = dist(c, t, Q.distribuicao(7), [C["s18"]] * 3, XE, 280, 110, cores={1: COR, 2: COR} if t >= C["s18.b"] else None)
    if t >= C["s18.b"]:
        E.chave(c, cx[1][0], cx[2][1], 310, E.COR, ep(t, C["s18.b"], 0.5), 26)
    E.frase(c, t, C["s18.a"], ps("maior número:", "i", 62) + [("2", "g", 60)] + [("→", "g", 60, TINTA2)] + [("2º período", "g", 60, COR)], XE, 460, passo=0.1)
    E.frase(c, t, C["s18.b"], ps("camada 2:", "i", 62) + [("2 + 3 = 5", "g", 60)] + [("→", "g", 60, TINTA2)] + [("família 15 (5A)", "g", 60, COR)], XE, 580, passo=0.1)
    E.frase(c, t, C["s18.d"], [("2 + 2 + 3 = 7", "g", 60)] + ps(":", "i", 62) + [("Z = 7", "g", 60)], XE, 700, passo=0.1)
    E.foco(c, t, C["s18.e"], 0.5, lambda a: E.pilula(c, "nitrogênio", XE + 690, 680, 54, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s18.f"], 0.4, lambda a: E.escreve(c, "Z 7, família 15: o Z não é a família", XE, 860, 58, "g", ERRADO, a))
    Q.tabela(c, t, C["s18"], 1200, 330, 36, numeros=False, familia=15 if t >= C["s18.c"] else None, destaque=("N",) if t >= C["s18.e"] else ())


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("período", "g", 66, COR), ("= número de camadas", "i", 68)]),
                 ("s19.b", [("família", "g", 66, COR), ("= elétrons de valência", "i", 68)]),
                 ("s19.c", [("a casa:", "g", 66), ("símbolo, nome, número atômico", "i", 64)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.12)
        E.foco(c, t, C["s19.c"] + 0.4, 0.5, lambda a: casa(c, 1560, 760, 260, 11, "Na", "sódio", "22,99", a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("as famílias", "i", 70) + [("com nome", "g", 70, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s20.b"], [("metais", "g", 70), ("e", "i", 74), ("ametais", "g", 70, COR)], XE, 530, passo=0.12)
    Q.tabela(c, t, C["s20.a"] + 0.4, XE + 20, 640, 40, numeros=False, familia=17)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ordem=b_ordem, casa=b_casa, periodo=b_periodo, familia=b_familia, exemplo=b_exemplo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
