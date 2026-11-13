"""Visual — Estudativo · QUI-ATO-005: distribuição eletrônica pelo diagrama de Pauling.
Segue a linguagem visual da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-ATO-001). Nesta aula:
- SUBNÍVEL = "1s^2" com E.formula na grotesca: número da camada e letra em tinta, expoente (elétrons) menor no alto.
  O subnível da vez fica na cor da matéria; o que já foi escrito volta para a tinta. Capacidades s 2, p 6, d 10, f 14 em
  pílulas turquesa. Prédio = camada é o andar, subnível é o apartamento (predio()).
- DIAGRAMA = Q.pauling, com as diagonais na cor da matéria; o contador "sobram N" em cinza-tinta à direita.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-005_diagrama_de_pauling.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("subniveis", "diagrama", "ferro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

FE = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2), ("3d", 6)]
BR35 = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2), ("3d", 10), ("4p", 5)]
assert Q.distribuicao(26) == FE and sum(n for _, n in FE) == 26
assert Q.distribuicao(35) == BR35 and 20 + 10 + 5 == 35 and sum(n for _, n in BR35[:6]) == 20
assert 2 + 2 + 6 + 2 + 6 + 8 == 26          # o erro (3d⁸ no lugar de 4s² 3d⁶) também fecha 26
SOBRAM = [26 - sum(n for _, n in FE[:k + 1]) for k in range(7)]
assert SOBRAM == [24, 22, 16, 14, 8, 6, 0]


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


def dist(c, t, itens, tl, x, y, size, ate=None, cor_vez=True, escuro=False, cores=None):
    """distribuição termo a termo: itens = [("1s", 2), ...], tl = instante de cada termo; devolve [x0, x1] de cada termo"""
    tinta = BR if escuro else TINTA
    xs, xx = [], x
    vez = None
    for k, ti in enumerate(tl):
        if t >= ti:
            vez = k
    for k, ((sub, n), ti) in enumerate(zip(itens, tl)):
        s = f"{sub}^{{{n}}}"
        w = E.formula(None, s, 0, 0, size, "g", a=0)
        cor = (cores or {}).get(k) or ((E.CLARO if escuro else COR) if (cor_vez and k == vez and (ate is None or t < ate)) else tinta)
        E.foco(c, t, ti, 0.4, lambda a, s=s, xx=xx, cor=cor: E.formula(c, s, xx, y, size, "g", cor, a))
        xs.append((xx, xx + w))
        xx += w + size * 0.32
    return xs


def predio(c, t, t0, x, yb, a=1.0):
    """o prédio: andar 1 com s; andar 2 com s e p; andar 3 com s, p e d; andar 4 com s, p, d e f"""
    caps = dict(s=2, p=6, d=10, f=14)
    for i in range(4):
        q = ep(t, t0 + 0.25 * i, 0.4) * a
        if q <= 0:
            continue
        y = yb - (i + 1) * 120
        M.rrect(c, x - 20, y - 10, 4 * 150 + 40, 116, 10, "#E6E8EC", q)
        E.escreve(c, str(i + 1), x - 90, y + 72, 64, "g", TINTA2, q)
        for j, L in enumerate("spdf"[:i + 1]):
            M.rrect(c, x + j * 150, y + 6, 130, 84, 12, E.COR if L == "s" else E.mix(E.COR, "#FFFFFF", 0.25 * j), q, shadow=True)
            E.formula(c, f"{i + 1}{L}", x + j * 150 + 65, y + 66, 46, "g", E.SOBRE, q, "center")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("ferro:", "g", 80), ("26", "g", 100, COR)] + ps("elétrons", "i", 80), XE, 260, passo=0.15)
        Q.bohr(c, t, C["s01.a"] + 0.3, 1450, 560, (2, 8, 14, 2), r0=90, dr=75, s="Fe")
        E.frase(c, t, C["s01.b"], ps("onde fica cada um?", "i", 80), XE, 420, passo=0.12)
        E.frase(c, t, C["s01.c"] - 2.2, ps("um desenho simples responde:", "i", 60, TINTA2), XE, 600, passo=0.1)
        E.frase(c, t, C["s01.c"], [("diagrama de Pauling", "g", 76, COR)], XE, 720)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("desenhar o", "i", 70), ("diagrama", "g", 66)]),
                 (C["s02.b"], [("seguir as", "i", 70), ("diagonais", "g", 66, COR)]),
                 (C["s02.c"], [("os elétrons do", "i", 70), ("ferro", "g", 66)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das aulas anteriores", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("camadas numeradas de", "i", 66) + [("1 a 7", "g", 64, COR)], XE, 340, passo=0.12)
    E.frase(c, t, C["s03.a"] + 1.6, [("1", "g", 60, COR)] + ps("é a K,", "i", 62) + [("2", "g", 60, COR)] + ps("é a L...", "i", 62), XE, 440, passo=0.12)
    Q.bohr(c, t, C["s03.a"] + 0.2, 1460, 560, (2, 8, 8), r0=100, dr=90, nomes=True)
    E.frase(c, t, C["s03.b"], ps("átomo neutro:", "i", 66) + [("elétrons = Z", "g", 64, COR)], XE, 680, passo=0.12)


# ---------------- subníveis ----------------
def b_subniveis(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("cada camada se divide em", "i", 64) + [("subníveis", "g", 62, COR)], XE, 200, passo=0.1)
        E.frase(c, t, C["s04.b"], [("camada", "g", 60), ("=", "g", 60, TINTA2)] + ps("o andar", "i", 64), XE, 340, passo=0.12)
        E.frase(c, t, C["s04.c"], [("subnível", "g", 60, COR), ("=", "g", 60, TINTA2)] + ps("o apartamento", "i", 64), XE, 440, passo=0.12)
        predio(c, t, C["s04.b"] + 0.3, 1100, 900)
        for k, L in enumerate("spdf"):
            pilula_em(c, t, C["s04.d"] + 0.3 * k, L, XE + 60 + 120 * k, 620, 72, TINTA)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("cada subnível tem um", "i", 66) + [("limite", "g", 62, COR)], XE, 220, passo=0.12)
        for k, (ck, L, n) in enumerate((("s05.b", "s", 2), ("s05.c", "p", 6), ("s05.d", "d", 10), ("s05.e", "f", 14))):
            x = 360 + k * 400
            E.foco(c, t, C[ck], 0.5, lambda a, x=x, L=L, n=n: (E.bola(c, x, 520, 130 * ease_back(prog(t, C[ck], 0.5)), E.COR, a),
                                                               centro(c, L, x, 545, 120, "g", E.SOBRE, a)))
            E.foco(c, t, C[ck] + 0.2, 0.4, lambda a, x=x, n=n: centro(c, f"{n} elétrons", x, 760, 56, "g", TINTA, a))
        E.frase(c, t, C["s05.e"] + 1.0, ps("os únicos números para decorar", "i", 60, TINTA2), W / 2, 930, "center", 0.1)
        return
    E.frase(c, t, C["s06"], ps("como escrever", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.formula_em(c, t, C["s06.a"], "2s^2", 760, 650, 340, "g", TINTA)
    for ck, txt, x0, y0, x1, y1 in (("s06.a", "número da camada", 560, 840, 820, 700), ("s06.b", "letra do subnível", 1000, 900, 1020, 720),
                                    ("s06.c", "elétrons, no alto", 1300, 300, 1210, 380)):
        E.foco(c, t, C[ck] + 0.3, 0.4, lambda a, txt=txt, x0=x0, y0=y0, x1=x1, y1=y1: (M.arrow(c, x0, y0, x1, y1, E.COR, a, 5, 18),
                                                                                    E.escreve(c, txt, x0 - (E.larg(txt, "g", 50) if x0 < 900 else 0), y0 + 50 if y0 > 600 else y0 - 20, 50, "g", COR, a)))
    E.frase(c, t, C["s06.d"], ps("camada 2, subnível s, com 2 elétrons", "i", 56, TINTA2), W / 2, 1010, "center", 0.08)


# ---------------- o diagrama ----------------
PX, PY, PS = 980, 170, 64


def b_diagrama(c, t, C, b):
    if t < C["s08"]:
        E.frase(c, t, C["s07.a"], ps("primeiro, os de", "i", 70) + [("menor energia", "g", 66, COR)], XE, 260, passo=0.12)
        E.frase(c, t, C["s07.b"], ps("essa ordem", "i", 70) + [("não é", "g", 66, ERRADO)] + ps("a das camadas", "i", 70), XE, 400, passo=0.12)
        E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "4s", XE + 100, 680, 200, "g", COR, a))
        E.foco(c, t, C["s07.c"] + 0.5, 0.4, lambda a: E.escreve(c, "enche antes do", XE + 420, 660, 66, "i", TINTA, a))
        E.foco(c, t, C["s07.c"] + 1.0, 0.5, lambda a: E.formula(c, "3d", XE + 900, 680, 200, "g", TINTA, a))
        return
    # o diagrama: linhas escritas em s08, diagonais em s09
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("uma linha por camada", "i", 64), XE, 220, passo=0.1)
        Q.pauling(c, t, C["s08.b"] - 0.6, PX, PY, PS, setas=False)
        E.frase(c, t, C["s08.e"], ps("até a sétima linha", "i", 56, TINTA2), XE, 360, passo=0.1)
        return
    Q.pauling(c, t, C["s09"] - 1.0, PX, PY, PS, setas=False)
    Q.pauling(c, t, C["s09.a"] - 0.8, PX, PY, PS, setas=True, passo=(C["s09.c"] + 2.0 - C["s09.a"]) / 8)
    E.frase(c, t, C["s09.a"], ps("diagonais paralelas", "i", 64), XE, 220, passo=0.1)
    E.frase(c, t, C["s09.a"] + 1.0, ps("de cima à direita", "i", 58, TINTA2), XE, 310, passo=0.1)
    E.frase(c, t, C["s09.a"] + 1.8, ps("para baixo à esquerda", "i", 58, TINTA2), XE, 390, passo=0.1)
    ordem = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p"]
    tl = [lerp(C["s09.b"], C["s09.c"], k / 5) if k < 5 else C["s09.c"] + 0.6 * (k - 5) for k in range(8)]
    for k, (sub, ti) in enumerate(zip(ordem, tl)):
        x = XE + (k % 4) * 180
        y = 560 + (k // 4) * 120
        E.foco(c, t, ti, 0.35, lambda a, sub=sub, x=x, y=y, k=k: E.formula(c, sub, x, y, 70, "g", COR if sub in ("4s", "3d") else TINTA, a))
    E.frase(c, t, C["s09.d"], ps("a ordem de", "i", 64) + [("encher", "g", 62, COR)], XE, 900, passo=0.1)


# ---------------- o ferro ----------------
def b_ferro(c, t, C, b):
    E.frase(c, t, C["s10"], [("ferro:", "g", 66), ("26", "g", 66, COR)] + ps("elétrons", "i", 66), XE, 180, passo=0.12)
    tl = [C["s10.b"], C["s10.c"], C["s10.d"], C["s11.a"], C["s11.b"], C["s11.c"], C["s11.e"]]
    xs = dist(c, t, FE, tl, XE, 420, 96, ate=C["s12"])
    Q.pauling(c, t, C["s10"] - 2.0, 1340, 520, 40, Z=26, passo=(C["s11.e"] - C["s10.b"] + 0.4) / 7)
    # sobram
    vez = max([k for k, ti in enumerate(tl) if t >= ti] or [-1])
    if vez >= 0 and t < C["s12"]:
        n = SOBRAM[vez]
        E.foco(c, t, tl[vez], 0.3, lambda a: (E.escreve(c, "sobram", XE, 600, 60, "i", TINTA2, a), E.escreve(c, str(n), XE + 230, 610, 90, "g", COR, a)))
    if C["s11.d"] <= t < C["s11.e"] + 0.8:
        E.foco(c, t, C["s11.d"], 0.4, lambda a: E.pilula(c, "no 3d cabem 10, só sobraram 6", XE + 450, 760, 48, "g", fundo=TINTA, a=a))
    if t >= C["s12"]:
        x0, x1 = xs[5][0], xs[6][1]
        E.chave(c, x0, x1, 470, E.COR, ep(t, C["s12.a"], 0.5), 26)
        E.frase(c, t, C["s12.a"] + 0.3, ps("termina em", "i", 60), XE, 640, passo=0.1)
        E.formula_em(c, t, C["s12.a"] + 0.6, "4s^2 3d^6", XE + 330, 650, 90, "g", COR)
        E.frase(c, t, C["s12.b"], ps("o último ficou", "i", 60) + [("incompleto:", "g", 58)] + ps("normal", "i", 60), XE, 800, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("seguir as camadas e encher o 3d antes do 4s", "i", 56), XE, 310, passo=0.08)
    ERR = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("3d", 8)]
    xs = dist(c, t, ERR, [C["s13.b"]] * 6, XE, 480, 84, cor_vez=False, cores={5: ERRADO})
    if t >= C["s13.b"] + 0.6:
        E.foco(c, t, C["s13.b"] + 0.6, 0.4, lambda a: E.escreve(c, "e o 4s vazio?", xs[5][1] + 40, 470, 54, "i", ERRADO, a))
    if t >= C["s13.c"]:
        E.risco(c, XE - 10, 500, xs[5][1] + 10, 400, t, C["s13.c"], largura=10)
        dist(c, t, FE, [C["s13.c"] + 0.5] * 7, XE, 720, 84, cor_vez=False, cores={5: COR})
        E.foco(c, t, C["s13.c"] + 1.0, 0.4, lambda a: E.selo(c, 1780, 690, 40, True, a))
        E.frase(c, t, C["s13.c"] + 1.2, ps("pelas diagonais, o 4s vem antes", "i", 58, TINTA2), XE, 880, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("o atalho para conferir", "i", 70, CLARO), W / 2, 170, "center", 0.12)
        E.foco(c, t, C["s14.a"], 0.5, lambda a: E.pilula(c, "some os números do alto", W / 2, 320, 70, "g", fundo=E.COR, a=a))
        xs = dist(c, t, FE, [C["s14.a"] + 0.4] * 7, 250, 540, 92, cor_vez=False, escuro=True, cores={k: E.CLARO for k in range(7)} if t >= C["s14.b"] else None)
        E.formula_em(c, t, C["s14.b"], "2 + 2 + 6 + 2 + 6 + 2 + 6", W / 2, 740, 84, "g", BR, "center")
        E.foco(c, t, C["s14.c"], 0.5, lambda a: (E.bola(c, W / 2, 900, 70, a=a), centro(c, "26", W / 2, 926, 72, "g", E.SOBRE, a)))
        E.foco(c, t, C["s14.d"], 0.4, lambda a: E.escreve(c, "= elétrons do ferro", W / 2 + 110, 924, 56, "i", CLARO, a))
        return
    E.frase(c, t, C["s15.a"], ps("cada número do alto conta elétrons:", "i", 62, CLARO), W / 2, 260, "center", 0.1)
    E.frase(c, t, C["s15.a"] + 1.8, ps("o total tem que", "i", 62, CLARO) + [("fechar", "g", 60, BR)], W / 2, 350, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("não", "g", 62, ERRADO)] + ps("pega a troca de ordem:", "i", 64, CLARO), W / 2, 520, "center", 0.1)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "... 3p^6 3d^8", W / 2 - 40, 680, 90, "g", "#FF8A80", a, "right"))
    E.foco(c, t, C["s15.c"] + 0.4, 0.4, lambda a: E.formula(c, "também = 26", W / 2 + 40, 680, 72, "g", CLARO, a))
    E.frase(c, t, C["s15.d"], ps("para a ordem:", "i", 64, CLARO) + [("as diagonais", "g", 62, BR)], W / 2, 880, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16.a"], [("bromo:", "g", 76), ("35", "g", 90, COR)] + ps("elétrons", "i", 76), XE, 340, passo=0.12)
    E.frase(c, t, C["s16.b"], [("1", "g", 56, COR)] + ps("distribua pelo diagrama de Pauling", "i", 60), XE, 520, passo=0.08)
    E.frase(c, t, C["s16.c"], [("2", "g", 56, COR)] + ps("qual é o último subnível?", "i", 60), XE, 640, passo=0.08)
    if t < C["s17"]:
        Q.pauling(c, t, C["s16.b"], 1300, 300, 46, setas=False)
    else:
        E.relogio(c, t, C["s17.a"], cx=1540, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18"], ps("bromo, 35 elétrons", "i", 64, TINTA2), XE, 180, passo=0.1)
    tl = [C["s18.a"]] * 6 + [C["s18.c"], C["s18.d"]]
    xs = dist(c, t, BR35, tl, XE, 380, 84, ate=C["s19"])
    if t >= C["s18.a"] + 0.4:
        E.chave(c, xs[0][0], xs[5][1], 410, TINTA2, ep(t, C["s18.a"] + 0.4, 0.5), 26)
        E.foco(c, t, C["s18.a"] + 0.6, 0.4, lambda a: E.escreve(c, "igual ao ferro: 20", XE + 200, 500, 52, "i", TINTA2, a))
    for ck, n in (("s18.b", 15), ("s18.c", 5)):
        if C[ck] <= t < (C["s18.c"] if ck == "s18.b" else C["s18.d"] + 0.6):
            E.foco(c, t, C[ck], 0.3, lambda a, n=n: (E.escreve(c, "sobram", XE, 640, 60, "i", TINTA2, a), E.escreve(c, str(n), XE + 230, 650, 90, "g", COR, a)))
    if t >= C["s18.e"]:
        E.frase(c, t, C["s18.e"], ps("último subnível:", "i", 64), XE, 680, passo=0.1)
        E.foco(c, t, C["s18.e"] + 0.4, 0.5, lambda a: (E.bola(c, XE + 640, 660, 76, a=a), E.formula(c, "4p^5", XE + 640, 684, 64, "g", E.SOBRE, a, "center")))
    if t >= C["s19"]:
        E.formula_em(c, t, C["s19.a"], "20 + 10 + 5 = 35", XE, 900, 84, "g", TINTA2)
        E.foco(c, t, C["s19.b"], 0.4, lambda a: E.selo(c, XE + 840, 870, 40, True, a))
    Q.pauling(c, t, C["s18"], 1380, 470, 40, Z=35, passo=0.25)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        for k, (L, n) in enumerate((("s", 2), ("p", 6), ("d", 10), ("f", 14))):
            x = 380 + k * 380
            E.foco(c, t, C["s20.a"] + 0.4 * k, 0.4, lambda a, x=x, L=L, n=n: (E.bola(c, x, 380, 80, a=a), centro(c, L, x, 404, 80, "g", E.SOBRE, a),
                                                                           centro(c, str(n), x, 540, 76, "g", COR, a)))
        E.frase(c, t, C["s20.b"], [("1", "g", 60, COR)] + ps("encha pelas", "i", 66) + [("diagonais", "g", 62)], XE, 720, passo=0.1)
        E.frase(c, t, C["s20.c"], [("2", "g", 60, COR)] + ps("some os números do alto para", "i", 66) + [("conferir", "g", 62)], XE, 860, passo=0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], ps("elétrons na", "i", 70) + [("última camada", "g", 70, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s21.b"], ps("e a distribuição de um", "i", 70) + [("íon", "g", 70, COR)], XE, 530, passo=0.12)
    Q.formula_em(c, t, C["s21.b"] + 0.8, "Fe^{2+}", XE + 60, 760, 150)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, subniveis=b_subniveis, diagrama=b_diagrama, ferro=b_ferro, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
