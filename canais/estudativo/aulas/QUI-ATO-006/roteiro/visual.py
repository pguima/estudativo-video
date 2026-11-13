"""Visual — Estudativo · QUI-ATO-006: camada de valência e distribuição dos íons.
Segue a linguagem visual da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-ATO-001). Nesta aula:
- CAMADA DE VALÊNCIA = os termos da distribuição com o maior número de camada, na cor da matéria e com a chave turquesa
  embaixo; os de dentro ficam em cinza-tinta. No modelo de camadas (Q.bohr), a última camada ganha o anel turquesa.
- ELÉTRON QUE SAI = o termo risca e some; ELÉTRON QUE ENTRA = o expoente novo chega na cor da matéria.
- ORDEM DE CAMADA = o 4s desliza para depois do 3d (reordena()).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-006_camada_de_valencia_ions.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("valencia", "ions", "atalho", "questao", "fim"))
BR = "#FFFFFF"

S16 = Q.distribuicao(16)
FE = Q.distribuicao(26)
MN = Q.distribuicao(25)
S18 = Q.distribuicao(18)
assert S16 == [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 4)] and 2 + 4 == 6
assert FE[-2:] == [("4s", 2), ("3d", 6)] and sum(n for _, n in FE) - 2 == 24
assert MN[-2:] == [("4s", 2), ("3d", 5)] and sum(n for _, n in MN) - 2 == 23
assert S18[-1] == ("3p", 6) and 16 + 2 == 18
FE2 = FE[:5] + [("3d", 6)]
MN2 = MN[:5] + [("3d", 5)]


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


def termo(sub, n):
    return f"{sub}^{{{n}}}"


def larguras(itens, size):
    return [E.formula(None, termo(s, n), 0, 0, size, "g", a=0) for s, n in itens]


def dist(c, t, itens, t0, x, y, size, cores=None, passo=0.0, some=None, ordem=None, tm=None, escuro=False):
    """distribuição em linha. cores = {índice: cor}; some = {índice: instante em que risca e sai};
    ordem = nova ordem dos índices, para onde os termos deslizam a partir de tm. Devolve as caixas (x0, x1) finais."""
    tinta = BR if escuro else TINTA
    ws = larguras(itens, size)
    gap = size * 0.32

    def xs_de(idx):
        out, xx = {}, x
        for k in idx:
            out[k] = xx
            xx += ws[k] + gap
        return out
    x_a = xs_de(range(len(itens)))
    x_b = xs_de(ordem) if ordem else x_a
    u = ease_io(prog(t, tm, 0.9)) if (ordem and tm is not None) else 0
    caixas = {}
    for k, (s, n) in enumerate(itens):
        xx = lerp(x_a[k], x_b[k], u)
        dy = -size * 0.7 * math.sin(math.pi * u) if (ordem and x_b[k] != x_a[k]) else 0
        cor = (cores or {}).get(k, tinta)
        a_saida = 1.0
        if some and k in some and t >= some[k]:
            a_saida = 1 - ep(t, some[k] + 0.6, 0.5)
            if a_saida <= 0:
                continue
        E.foco(c, t, t0 + passo * k, 0.4, lambda a, s=termo(s, n), xx=xx, cor=cor, dy=dy, aa=a_saida: E.formula(c, s, xx, y + dy, size, "g", cor, a * aa))
        if some and k in some and t >= some[k]:
            E.risco(c, xx - 6, y + 6, xx + ws[k] + 6, y - size * 0.75, t, some[k], largura=8)
        caixas[k] = (xx, xx + ws[k])
    return caixas


def chave_sob(c, t, t0, caixas, idx, y, cor=None):
    xs = [caixas[k] for k in idx if k in caixas]
    if not xs:
        return
    E.chave(c, min(a for a, _ in xs), max(b for _, b in xs), y, cor or E.COR, ep(t, t0, 0.5), 26)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("o ferro termina em", "i", 70), XE, 240, passo=0.12)
        E.formula_em(c, t, C["s01.a"] + 0.6, "4s^2 3d^6", XE, 440, 170, "g", TINTA)
        E.frase(c, t, C["s01.a"] + 2.0, ps("seis na última camada?", "i", 66), XE, 600, passo=0.1)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (E.pilula(c, "não: tem dois", XE + 260, 720, 70, "g", fundo=E.COR, a=a)))
        E.frase(c, t, C["s01.c"], [("última camada", "g", 56, COR), ("≠", "g", 56, TINTA2), ("último subnível escrito", "g", 56, TINTA2)], XE, 900, passo=0.15)
        Q.bohr(c, t, C["s01.a"] + 0.3, 1480, 520, (2, 8, 14, 2), r0=80, dr=70, s="Fe")
        if t >= C["s01.b"]:
            q = ep(t, C["s01.b"], 0.5)
            c.drawCircle(1480, 520, 80 + 3 * 70, M.paint(E.COR, q, stroke=10))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("a", "i", 70), ("camada de valência", "g", 66, COR)]),
                 (C["s02.b"], [("a distribuição de um", "i", 70), ("íon", "g", 66)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das aulas anteriores", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("a distribuição segue as", "i", 70) + [("diagonais", "g", 66, COR)], XE, 340, passo=0.12)
    Q.pauling(c, t, C["s03.a"] + 0.3, 1320, 220, 48)
    E.frase(c, t, C["s03.b"], [("cátion:", "g", 66, COR)] + ps("perdeu elétrons", "i", 70), XE, 560, passo=0.12)
    E.frase(c, t, C["s03.c"], [("ânion:", "g", 66, Q.ELETRON)] + ps("ganhou elétrons", "i", 70), XE, 680, passo=0.12)


# ---------------- camada de valência ----------------
def b_valencia(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("camada de valência", "g", 90, COR)], XE, 240)
        E.frase(c, t, C["s04.a"] + 1.0, ps("a camada mais externa ocupada:", "i", 64), XE, 360, passo=0.1)
        E.frase(c, t, C["s04.b"], [("a de número maior", "g", 64)], XE, 460)
        E.frase(c, t, C["s04.c"], ps("é com ela que o átomo", "i", 60, TINTA2), XE, 620, passo=0.1)
        for k, s in enumerate(("cede", "recebe", "divide")):
            pilula_em(c, t, C["s04.c"] + 0.8 + 0.3 * k, s, XE + 100 + k * 240, 720, 54, TINTA)
        pilula_em(c, t, C["s04.d"], "como acontece: outra aula", XE + 330, 860, 46, TINTA2, "b")
        Q.bohr(c, t, C["s04.a"] + 0.3, 1480, 560, (2, 8, 6), r0=110, dr=95)
        q = ep(t, C["s04.b"], 0.5)
        if q > 0:
            c.drawCircle(1480, 560, 110 + 2 * 95, M.paint(E.COR, q, stroke=10))
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05"], [("enxofre:", "g", 66), ("16", "g", 66, COR)] + ps("elétrons", "i", 66), XE, 200, passo=0.12)
        cores = {3: COR, 4: COR, 0: TINTA2, 1: TINTA2, 2: TINTA2} if t >= C["s05.c"] else None
        cx = dist(c, t, S16, C["s05.b"], XE, 420, 100, cores=cores, passo=0.4)
        if t >= C["s05.c"]:
            chave_sob(c, t, C["s05.c"], cx, (3, 4), 450)
            E.frase(c, t, C["s05.c"] + 0.3, ps("maior número de camada:", "i", 60), XE, 620, passo=0.1)
            E.foco(c, t, C["s05.c"] + 1.2, 0.4, lambda a: E.escreve(c, "3", XE + 720, 630, 100, "g", COR, a))
        E.formula_em(c, t, C["s05.d"], "2 + 4 =", XE, 820, 90, "g", TINTA2)
        E.foco(c, t, C["s05.d"] + 0.6, 0.5, lambda a: (E.bola(c, XE + 420, 790, 64, a=a), centro(c, "6", XE + 420, 816, 70, "g", E.SOBRE, a)))
        E.foco(c, t, C["s05.d"] + 0.8, 0.4, lambda a: E.escreve(c, "elétrons na valência", XE + 520, 815, 56, "i", TINTA, a))
        return
    E.frase(c, t, C["s06"], [("ferro", "g", 66)] + ps("termina em", "i", 66), XE, 200, passo=0.12)
    cores = {5: COR, 6: TINTA2} if t >= C["s06.b"] else None
    cx = dist(c, t, FE, C["s06.a"], XE, 420, 96, cores=cores)
    if t >= C["s06.b"]:
        chave_sob(c, t, C["s06.c"], cx, (5,), 450)
        E.frase(c, t, C["s06.b"], ps("maior número de camada:", "i", 60), XE, 620, passo=0.1)
        E.foco(c, t, C["s06.b"] + 0.9, 0.4, lambda a: E.escreve(c, "4", XE + 720, 630, 100, "g", COR, a))
    E.foco(c, t, C["s06.d"], 0.5, lambda a: (E.bola(c, XE + 64, 790, 64, a=a), centro(c, "2", XE + 64, 816, 70, "g", E.SOBRE, a),
                                            E.escreve(c, "elétrons na valência", XE + 160, 815, 56, "i", TINTA, a)))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "o 3d é da camada 3, mais de dentro", XE, 960, 54, "i", TINTA2, a))


# ---------------- íons ----------------
def b_ions(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], [("ânion:", "g", 80, Q.ELETRON)] + ps("é fácil", "i", 80), XE, 220, passo=0.12)
        E.frase(c, t, C["s07.b"], ps("some os elétrons ganhos e distribua", "i", 62), XE, 340, passo=0.1)
        Q.formula_em(c, t, C["s07.c"], "S^{2-}", XE, 540, 150, cores={"carga": Q.ELETRON})
        E.formula_em(c, t, C["s07.c"] + 0.8, "16 + 2 = 18", XE + 380, 520, 90, "g", TINTA2)
        dist(c, t, S18, C["s07.d"], XE, 760, 96, cores={4: COR})
        return
    if t < C["s10"]:
        E.frase(c, t, C["s08.a"], [("cátion:", "g", 80, COR)] + ps("a armadilha", "i", 80), XE, 200, passo=0.12)
        E.frase(c, t, C["s08.b"], ps("saem da", "i", 62) + [("camada mais externa", "g", 60, COR)], XE, 320, passo=0.1)
        E.frase(c, t, C["s08.c"], ps("e não do último subnível escrito", "i", 58, TINTA2), XE, 410, passo=0.1)
        Q.formula_em(c, t, C["s08.d"], "Fe^{2+}", XE, 590, 140, cores={"carga": E.COR})
        E.frase(c, t, C["s08.d"] + 0.6, ps("perdeu 2 elétrons", "i", 58), XE + 340, 570, passo=0.1)
        some = {5: C["s08.e"] + 0.6}
        cx = dist(c, t, FE, C["s08.d"] + 0.4, XE, 800, 92, cores={5: COR} if t >= C["s08.e"] else None, some=some)
        if t >= C["s09"]:
            E.frase(c, t, C["s09.b"], [("24", "g", 64, COR)] + ps("elétrons, e o", "i", 64), XE, 960, passo=0.1)
            E.formula_em(c, t, C["s09.c"], "3d^6", XE + 520, 965, 70, "g", COR)
            E.foco(c, t, C["s09.c"] + 0.3, 0.4, lambda a: E.escreve(c, "ficou inteiro", XE + 700, 960, 60, "i", TINTA, a))
        return
    E.frase(c, t, C["s10"], ps("por que assim?", "i", 80), XE, 220, passo=0.12)
    E.frase(c, t, C["s10.a"], ps("o 4s entra primeiro:", "i", 64) + [("menos energia", "g", 60, COR)], XE, 380, passo=0.1)
    E.frase(c, t, C["s10.b"], ps("com o átomo pronto, está na", "i", 64) + [("camada de fora", "g", 60, COR)], XE, 500, passo=0.1)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.pilula(c, "entra pela energia, sai pela camada", W / 2, 720, 70, "g", fundo=E.COR, a=a))
    Q.bohr(c, t, C["s10"] + 0.3, 1600, 330, (2, 8, 14, 2), r0=50, dr=40, r_e=8)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("tirar os 2 elétrons do 3d, o último escrito", "i", 58), XE, 310, passo=0.08)
    ERR = FE[:5] + [("4s", 2), ("3d", 4)]
    dist(c, t, ERR, C["s11.b"], XE, 470, 86, cores={6: ERRADO})
    E.frase(c, t, C["s11.c"], ps("total: também 24, mas", "i", 60) + [("errado", "g", 58, ERRADO)], XE, 600, passo=0.1)
    if t >= C["s11.c"] + 1.6:
        E.risco(c, XE - 10, 490, XE + 1300, 400, t, C["s11.c"] + 1.6, largura=10)
    if t >= C["s11.d"]:
        dist(c, t, FE2, C["s11.d"], XE, 790, 86, cores={5: COR})
        E.foco(c, t, C["s11.d"] + 0.5, 0.4, lambda a: E.selo(c, 1500, 760, 40, True, a))
        E.frase(c, t, C["s11.d"] + 0.4, ps("os elétrons saem do 4s", "i", 58, TINTA2), XE, 940, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("reescreva em", "i", 70, CLARO) + [("ordem de camada", "g", 66, BR)], W / 2, 200, "center", 0.12)
        ordem = [0, 1, 2, 3, 4, 6, 5]
        some = {5: C["s12.c"] + 0.4} if t >= C["s12.c"] else None
        dist(c, t, FE, C["s12.a"] + 0.6, 230, 520, 96, cores={5: E.CLARO}, ordem=ordem, tm=C["s12.b"], some=some, escuro=True)
        E.frase(c, t, C["s12.b"] + 0.4, ps("o 3d antes, o 4s no fim", "i", 60, CLARO), W / 2, 700, "center", 0.1)
        E.frase(c, t, C["s12.c"], ps("aí, é só", "i", 66, CLARO) + [("tirar do final", "g", 62, BR)], W / 2, 860, "center", 0.12)
        return
    E.frase(c, t, C["s13.a"], ps("em ordem de camada, a de fora", "i", 66, CLARO) + [("fica no fim", "g", 62, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s13.b"], [("ânion?", "g", 64, "#8FB8FF")] + ps("não precisa:", "i", 66, CLARO), W / 2, 520, "center", 0.12)
    E.frase(c, t, C["s13.c"], ps("ganha elétrons e segue as", "i", 64, CLARO) + [("diagonais", "g", 60, BR)], W / 2, 640, "center", 0.1)
    Q.formula_em(c, t, C["s13.b"] + 0.6, "S^{2-}", W / 2 - 100, 860, 130, escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s14"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s14.a"], [("manganês:", "g", 70), ("25", "g", 80, COR)] + ps("elétrons", "i", 70), XE, 320, passo=0.12)
    E.frase(c, t, C["s14.b"] - 0.6, ps("termina em", "i", 62), XE, 450, passo=0.1)
    E.formula_em(c, t, C["s14.b"], "4s^2 3d^5", XE + 330, 460, 96, "g", TINTA)
    E.frase(c, t, C["s14.c"], [("1", "g", 56, COR)] + ps("quantos elétrons na valência?", "i", 60), XE, 640, passo=0.08)
    E.frase(c, t, C["s14.d"], [("2", "g", 56, COR)] + ps("e a distribuição do", "i", 60), XE, 760, passo=0.08)
    Q.formula_em(c, t, C["s14.d"] + 1.2, "Mn^{2+}", XE + 660, 770, 90)
    if t >= C["s15"]:
        E.relogio(c, t, C["s15.a"], cx=1540, cy=500, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s16"], [("manganês", "g", 60), ("25", "g", 60, COR)], XE, 180, passo=0.12)
    cx = dist(c, t, MN, C["s16"] + 0.3, XE, 330, 86, cores={5: COR} if t >= C["s16.a"] else None,
              some={5: C["s16.c"] + 0.5} if t >= C["s16.c"] else None)
    if t >= C["s16.a"]:
        chave_sob(c, t, C["s16.a"], cx, (5,), 360)
        E.foco(c, t, C["s16.b"], 0.5, lambda a: (E.bola(c, XE + 64, 480, 56, a=a), centro(c, "2", XE + 64, 502, 64, "g", E.SOBRE, a),
                                                E.escreve(c, "elétrons na valência", XE + 150, 500, 56, "i", TINTA, a)))
    if t >= C["s16.c"]:
        Q.formula_em(c, t, C["s16.c"], "Mn^{2+}", XE, 680, 110, cores={"carga": E.COR})
        E.frase(c, t, C["s16.c"] + 0.4, ps("saem 2, do 4s", "i", 58, TINTA2), XE + 320, 660, passo=0.1)
        dist(c, t, MN2, C["s16.d"], XE, 840, 86, cores={5: COR})
        E.foco(c, t, C["s16.e"], 0.4, lambda a: (E.formula(c, "25 − 2 = 23", XE, 990, 64, "g", TINTA2, a), E.selo(c, XE + 470, 968, 34, True, a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s17.a", [("valência:", "g", 66, COR), ("a camada de número maior", "i", 68)]),
                 ("s17.b", [("ânion:", "g", 66, Q.ELETRON), ("some e distribua", "i", 68)]),
                 ("s17.c", [("cátion:", "g", 66, COR), ("tire da camada mais externa", "i", 68)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s18.a"], [("praticando", "g", 90, COR)], XE, 400)
    E.frase(c, t, C["s18.a"] + 0.6, ps("dos modelos à distribuição", "i", 66), XE, 510, passo=0.1)
    E.frase(c, t, C["s18.b"], ps("questões no estilo da prova", "i", 60, TINTA2), XE, 620, passo=0.1)
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, valencia=b_valencia, ions=b_ions, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
