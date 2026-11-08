"""Visual — Estudativo · MAT-POT-006: praticando potências.
Aula de prática: cinco contas, cada uma com selo de progresso e relógio de pausa, mais a dica final de testar com números pequenos.
Peças desta aula: selo de conta, cartões de dívida do kit e a pilha de folhas. Expoente sempre com E.formula."""
from fractions import Fraction as Fr

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, sinal, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-006_praticando_potencias.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao3", "questao5", "fim"))
BR = "#FFFFFF"
assert 8 ** 2 * 4 ** 3 / 2 ** 9 == 8 == 2 ** 3 and 64 * 64 == 2 ** 12 and -2 ** 4 + (-2) ** 3 * 3 == -40 and 16 + (-2) ** 3 * 3 == -8
assert Fr(1, 2) ** 3 * 2 ** 3 + 9 ** 0 == 2 and Fr(125, 1000) * 8 == 1 and 15 ** 2 * Fr(3) ** -2 == 25 == 5 ** 2 and 225 // 9 == 25
assert Fr(10) ** 4 * Fr(10) ** -1 == 1000 and 10000 * Fr(1, 10) == 1000 and (1 + 2) ** 2 == 9 and 1 ** 2 + 2 ** 2 == 5 and 42 ** 2 == 1764


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número ou fórmula dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    E.formula(c, s, cx, cy + size * 0.36, size, cor=tinta or E.SOBRE, a=a, align="center")


def fm(c, t, t0, s, x, y, size, cor=None, align="left"):
    E.formula_em(c, t, t0, s, x, y, size, cor=cor, align=align)


def fl(c, t, partes, x, y, size, align="left", gap=None):
    """linha de fórmulas em que cada parte entra no seu instante: partes = [(escrita, cor, t0), ...]; devolve o x e a largura de cada uma"""
    gap = size * 0.2 if gap is None else gap
    ws = [E.formula(None, p[0], 0, 0, size, a=0) for p in partes]
    tot = sum(ws) + gap * (len(ws) - 1)
    xx = x - tot / 2 if align == "center" else x
    xs = []
    for p, w in zip(partes, ws):
        fm(c, t, p[2], p[0], xx, y, size, p[1])
        xs.append(xx)
        xx += w + gap
    return xs, ws


def selo(c, t, t0, n, s=None):
    """conta n de 5, com cinco pontos de progresso"""
    s = s or f"conta {n} de 5"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", cor=E.SOBRE, a=a)
        for i in range(5):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pilha_folhas(c, t, ti, tf, x, base, w, n=26):
    """pilha de folhas vista de lado, folha a folha de ti a tf"""
    for i in range(n):
        q = ep(t, lerp(ti, tf, i / n), 0.3)
        if q > 0:
            M.rrect(c, x, base - i * 14 - 9, w, 9, 2, E.COR if i % 2 else TINTA2, q)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_ = C["s01.a"], C["s01.b"]
    E.frase(c, t, a_ + 0.1, ps("5", "g", 240, COR) + ps("contas", "g", 180, COR), XE, 340, passo=0.25)
    E.frase(c, t, a_ + 0.9, ps("criadas para esta aula", "i", 92), XE, 470, passo=0.15)
    E.frase(c, t, lerp(a_, b_, 0.55), ps("juntam o que você viu sobre potências", "i", 72), XE, 580, passo=0.11)
    for i, (s, cx) in enumerate((("pause", 520), ("resolva", 1140))):
        ti = b_ + i * 0.5
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 730, 56, 64, p), E.escreve(c, s, cx - 110, 762, 96, "g", TINTA, p)))
    E.frase(c, t, lerp(b_, C["s01.end"], 0.72), ps("errar aqui", "i", 88) + ps("não custa nada", "g", 80, COR), W / 2, 920, "center", 0.18)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("suas ferramentas", "i", 92, COR), XE, 160)
    itens = (("s02.a", "mesma base:", "vezes soma, dividido subtrai"), ("s02.b", "dentro e fora do parêntese:", "multiplica"),
             ("s02.c", "a potência vem", "antes do vezes"), ("s02.d", "expoente negativo", "vira fração"))
    for i, (k, s1, s2) in enumerate(itens):
        y = 210 + i * 170
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, XE, y, 1580, 142, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(s1, "i", 64) + ps(s2, "g", 60, COR), XE + 44, y + 92, passo=0.12)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.6), ps("travou?", "i", 60, COR) + ps("procure a aula no canal", "i", 60), W / 2, 1000, "center", 0.13)


# ---------------- conta 1: mesma base ----------------
def b_questao1(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s03.{k}"] for k in "abcd")
    selo(c, t, a_, 1)
    fl(c, t, [("8^2 · 4^3", COR, b_), ("÷ 2^9", COR, c_)], XE, 540, 150)
    E.frase(c, t, d_, ps("quanto", "i", 120) + ps("dá?", "g", 120, COR), XE, 800)
    E.relogio(c, t, C["s04.a"], 1520, 400, 190)


def b_resposta1(c, t, C, b):
    selo(c, t, C["s05"] - 0.5, 1)
    a_, b_, c_, d_ = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    X = 720
    fm(c, t, a_, "8 = 2^3", XE, 300, 110, COR)
    fm(c, t, b_, "4 = 2^2", XE, 470, 110, COR)
    fm(c, t, c_, "8^2 = (2^3)^2 = 2^6", X, 300, 110)
    fm(c, t, d_, "4^3 = (2^2)^3 = 2^6", X, 470, 110)
    M.line(c, XE, 540, W - XE, 540, FIO, ep(t, a6 - 0.4, 0.5), 3)
    y = 680
    xs, ws = fl(c, t, [("2^6 · 2^6 ÷ 2^9", None, C["s06"] + 0.1), ("= 2^{12} ÷ 2^9", None, a6), ("= 2^3", None, b6), ("=", None, c6 - 0.05)], XE, y, 100, gap=30)
    E.foco(c, t, c6, 0.5, lambda p: num_bola(c, "8", xs[-1] + ws[-1] + 120, y - 34, 84, 96, p, CERTO, BR))
    fm(c, t, a6 + 0.3, "6 + 6 = 12", xs[1] + 60, y + 100, 66, COR)
    fm(c, t, b6 + 0.3, "12 − 9 = 3", xs[2] + 50, y + 100, 66, COR)
    E.frase(c, t, d6 - 0.1, ps("pelo caminho longo:", "i", 66), XE, 950, passo=0.12)
    fm(c, t, d6 + 0.3, "64 × 64 ÷ 512", 770, 955, 84, TINTA2)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a, b_, c_, d = (C[f"s07.{k}"] for k in "abcd")
    E.frase(c, t, C["s07"] + 0.1, ps("o atalho da prática", "i", 88, CLARO), W / 2, 190, "center")
    E.frase(c, t, a, ps("ponha tudo na", "i", 110, BR) + ps("mesma base", "g", 104, BR), W / 2, 340, "center", 0.18)
    E.frase(c, t, b_, ps("somar e subtrair expoentes", "i", 76, CLARO) + ps("pede base igual", "g", 70, BR), W / 2, 500, "center", 0.13)
    E.frase(c, t, c_, ps("não compensa", "g", 80, ERRADO) + ps("sem a mesma base", "i", 84, CLARO), W / 2, 680, "center", 0.15)
    fl(c, t, [("8 = 2^3", BR, d), ("9 = 3^2", BR, d + 0.4)], W / 2, 850, 110, "center", gap=120)
    E.frase(c, t, lerp(d, C["s07.end"], 0.5), ps("calcule cada um", "g", 76, BR), W / 2, 980, "center")


# ---------------- conta 2: sinais e ordem ----------------
def b_questao2(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s08.{k}"] for k in "abcd")
    selo(c, t, a_, 2)
    fl(c, t, [("−2^4", COR, b_), ("+", None, c_), ("(−2)^3", COR, c_ + 0.3), ("× 3", COR, d_)], XE, 540, 140)
    E.foco(c, t, b_ + 0.6, 0.45, lambda q: E.pilula(c, "sem parênteses", 390, 690, 50, estilo="b", cor=E.SOBRE, a=q))
    E.relogio(c, t, C["s09.a"], 1550, 320, 170)


def b_resposta2(c, t, C, b):
    selo(c, t, C["s10"] - 0.5, 2)
    a_, b_, c_, d_, e_ = (C[f"s10.{k}"] for k in "abcde")

    def s10():
        fm(c, t, C["s10"] + 0.1, "−2^4 + (−2)^3 × 3", XE, 290, 120)
        E.frase(c, t, lerp(C["s10"], a_, 0.6), ps("as potências vêm primeiro", "i", 62), 1090, 270, passo=0.1)
        xa, xb = XE, 1000
        E.frase(c, t, a_, ps("sem parênteses:", "i", 66), xa, 450, passo=0.12)
        E.frase(c, t, a_ + 0.7, ps("o menos", "g", 62, ERRADO) + ps("fica de fora", "i", 66), xa, 540, passo=0.12)
        fm(c, t, b_, "2^4 = 16", xa, 680, 110)
        E.foco(c, t, c_, 0.5, lambda p: num_bola(c, "−16", xa + 170, 860, 110, 84, p))
        E.frase(c, t, d_ - 0.2, ps("com parênteses,", "i", 66) + ps("expoente ímpar:", "i", 66), xb, 450, passo=0.12)
        fm(c, t, d_ + 0.3, "(−2)^3 = −8", xb, 570, 110)
        fm(c, t, e_, "−8 × 3 = −24", xb, 700, 110)
        E.foco(c, t, e_ + 0.5, 0.5, lambda p: num_bola(c, "−24", xb + 170, 860, 110, 84, p))
    E.saida(c, t, C["s11"] - 0.1, s10)

    if t >= C["s11"]:
        a, b1, c1 = (C[f"s11.{k}"] for k in "abc")
        E.frase(c, t, C["s11"] + 0.1, ps("por último", "i", 80, COR), W / 2, 240, "center")
        E.foco(c, t, a, 0.5, lambda q: E.divida(c, 470, 450, 400, 220, "16", q))
        E.foco(c, t, a + 0.7, 0.5, lambda q: E.divida(c, 950, 450, 400, 220, "24", q))
        sinal(c, t, b1 - 0.1, "=", 1260, 445, 130)
        E.foco(c, t, b1, 0.5, lambda p: num_bola(c, "−40", 1520, 445, 140, 104, p, CERTO, BR))
        E.frase(c, t, c1 - 0.3, ps("quem achou", "i", 72) + ps("+16", "g", 72, ERRADO) + ps("no começo", "i", 72), XE, 760, passo=0.13)
        fm(c, t, c1, "16 − 24 = −8", XE, 880, 96, ERRADO)
        E.frase(c, t, c1 + 0.8, ps("um parêntese que não existia", "i", 68, ERRADO), 880, 860, passo=0.11)


# ---------------- conta 3: juntar bases e expoente zero ----------------
def b_questao3(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s12.{k}"] for k in "abcd")
    selo(c, t, a_, 3)
    fl(c, t, [("0,5^3", COR, b_), ("× 2^3", COR, c_), ("+ 9^0", COR, d_)], XE, 540, 140, gap=40)
    E.relogio(c, t, C["s13.a"], 1550, 320, 170)


def b_resposta3(c, t, C, b):
    selo(c, t, C["s14"] - 0.5, 3)
    a, b_, c_, d, e, f = (C[f"s14.{k}"] for k in "abcdef")
    E.frase(c, t, C["s14"] + 0.1, ps("expoentes iguais,", "i", 70) + ps("junte as bases", "g", 66, COR), XE, 240, passo=0.14)
    fm(c, t, a, "(0,5 × 2)^3", XE, 410, 124)
    fm(c, t, b_, "0,5 × 2 = 1", 1120, 300, 96, COR)
    fm(c, t, c_, "1^3 = 1", 1120, 440, 96, COR)
    M.line(c, XE, 500, W - XE, 500, FIO, ep(t, d - 0.3, 0.5), 3)
    fm(c, t, d, "9^0 = 1", XE, 640, 124)
    E.frase(c, t, d + 0.5, ps("e não zero", "g", 72, ERRADO), 660, 620)
    fl(c, t, [("1 + 1 =", None, e - 0.1)], XE, 830, 124)
    E.foco(c, t, e, 0.5, lambda p: num_bola(c, "2", XE + 510, 790, 96, 110, p, CERTO, BR))
    E.frase(c, t, f - 0.1, ps("confira:", "i", 66), 900, 740)
    fm(c, t, f + 0.2, "0,5^3 = 0,125", 900, 850, 88)
    fm(c, t, f + 1.2, "0,125 × 8 = 1", 900, 970, 88, CERTO)


# ---------------- conta 4: expoente negativo em fração ----------------
def b_questao4(c, t, C, b):
    a_, b_, c_ = (C[f"s15.{k}"] for k in "abc")
    selo(c, t, a_, 4)
    fl(c, t, [("15^2", COR, b_), ("×", None, c_), ("3^{−2}", COR, c_ + 0.1)], XE, 540, 170)
    E.relogio(c, t, C["s16.a"], 1500, 400, 190)


def b_resposta4(c, t, C, b):
    selo(c, t, C["s17"] - 0.5, 4)
    a, b_, c_, d, e, f = (C[f"s17.{k}"] for k in "abcdef")
    y = 300
    fm(c, t, a - 0.5, "15^2", XE, y, 120)
    fm(c, t, a, "= 225", XE + 270, y, 120, COR)
    fm(c, t, b_ - 0.5, "3^{−2}", 900, y, 120)
    fm(c, t, b_, "= f{1}{9}", 1190, y, 120, COR)
    fl(c, t, [("225 ÷ 9 =", None, c_)], XE, 510, 120)
    E.foco(c, t, c_ + 0.5, 0.5, lambda p: num_bola(c, "25", 830, 470, 96, 92, p, CERTO, BR))
    M.line(c, XE, 610, W - XE, 610, FIO, ep(t, d - 0.4, 0.5), 3)
    E.frase(c, t, lerp(c_, d, 0.65), ps("outro caminho", "i", 72, COR), XE, 700)
    fm(c, t, d, "15 = 3 × 5", 700, 705, 96)
    fm(c, t, e, "3^2 · 5^2 · f{1}{9}", XE, 900, 120)
    fm(c, t, lerp(e, f, 0.55), "9 × f{1}{9} = 1", 880, 900, 96, TINTA2)
    E.foco(c, t, f, 0.5, lambda p: num_bola(c, "5^2", 1560, 860, 110, 110, p, CERTO, BR))


# ---------------- conta 5: base dez ----------------
def b_questao5(c, t, C, b):
    a_, b_, c_, d_ = (C[f"s18.{k}"] for k in "abcd")
    selo(c, t, a_, 5, "última conta")
    E.frase(c, t, lerp(a_, b_, 0.4), ps("espessura de uma folha:", "i", 76), XE, 300, passo=0.13)
    fl(c, t, [("10^{−1}", COR, b_), ("mm", TINTA2, b_ + 0.1)], XE, 450, 130)
    E.frase(c, t, c_ - 0.3, ps("a gráfica empilha", "i", 76), XE, 610, passo=0.13)
    fl(c, t, [("10^4", COR, c_), ("folhas", TINTA2, c_ + 0.1)], XE, 750, 130)
    E.frase(c, t, d_, ps("altura da pilha,", "i", 88) + ps("em mm?", "g", 84, COR), XE, 930, passo=0.15)
    pilha_folhas(c, t, c_, d_, 1120, 980, 300)
    E.relogio(c, t, C["s19.a"], 1590, 300, 150)


def b_resposta5(c, t, C, b):
    selo(c, t, C["s20"] - 0.5, 5, "última conta")
    a, b_, c_, d, e, f = (C[f"s20.{k}"] for k in "abcdef")
    y = 300
    E.frase(c, t, lerp(C["s20"], a, 0.5), ps("folhas vezes espessura", "i", 66), XE, 220, passo=0.12)
    fm(c, t, a, "10^4 × 10^{−1}", XE, 370, 130)
    E.frase(c, t, lerp(a, b_, 0.65), ps("soma os expoentes", "i", 66), 1010, 240, passo=0.12)
    fm(c, t, b_, "4 − 1 = 3", 1010, 370, 110, COR)
    fm(c, t, c_, "= 10^3", XE, 590, 150)
    E.foco(c, t, d, 0.5, lambda p: num_bola(c, "1.000", 950, 535, 130, 76, p, CERTO, BR))
    E.foco(c, t, d + 0.1, 0.45, lambda p: E.escreve(c, "mm", 1110, 565, 84, "g", CERTO, p))
    E.frase(c, t, e - 0.1, ps("confira:", "i", 66), XE, 770)
    fm(c, t, e + 0.1, "10.000 × 0,1 = 1.000", 460, 780, 92)
    E.frase(c, t, lerp(e, f, 0.5), ps("o expoente é negativo,", "i", 64) + ps("a altura não", "g", 60, COR), XE, 900, passo=0.12)
    fm(c, t, f, "10^{−1} = f{1}{10}", 1100, 920, 90, COR)
    E.foco(c, t, f + 0.3, 0.45, lambda p: E.escreve(c, "de mm", 1500, 915, 60, "i", TINTA2, p))


# ---------------- última dica ----------------
def b_dica(c, t, C, b):
    a, b_, c_, d, e = (C[f"s21.{k}"] for k in "abcde")

    def s21():
        E.frase(c, t, C["s21"] + 0.1, ps("a regra existe?", "i", 88, COR), XE, 180)
        E.frase(c, t, a, ps("teste com", "i", 104) + ps("números pequenos", "g", 96, COR), XE, 320)
        fm(c, t, b_, "(1 + 2)^2  =?  1^2 + 2^2", W / 2, 520, 130, align="center")
        xa, xb = 500, 1420
        fm(c, t, c_, "3^2 = 9", xa, 760, 150, COR, "center")
        fm(c, t, d, "1 + 4 = 5", xb, 760, 150, COR, "center")
        sinal(c, t, d + 0.8, "≠", W / 2, 710, 130, ERRADO)
        E.frase(c, t, e, ps("não bateu:", "i", 88) + ps("a regra não existe", "g", 84, ERRADO), W / 2, 950, "center", 0.15)
    E.saida(c, t, C["s22"] - 0.1, s21)

    if t >= C["s22"]:
        a2, b2, c2 = (C[f"s22.{k}"] for k in "abc")
        E.foco(c, t, a2, 0.5, lambda q: E.selo(c, XE + 56, 280, 56, False, q))
        E.frase(c, t, a2 + 0.1, ps("um exemplo que falha", "i", 80) + ps("derruba a regra", "g", 76, ERRADO), XE + 150, 305, passo=0.14)
        E.foco(c, t, b2, 0.5, lambda q: E.selo(c, XE + 56, 500, 56, True, q))
        E.frase(c, t, b2 + 0.1, ps("um exemplo que bate", "i", 80) + ps("não prova nada", "g", 76, COR), XE + 150, 525, passo=0.14)
        fm(c, t, b2 + 1.2, "2^2 = 2 × 2", XE + 150, 680, 110)
        E.frase(c, t, b2 + 1.8, ps("coincidência", "g", 76, ERRADO), 860, 660)
        E.frase(c, t, c2, ps("bateu?", "i", 120) + ps("teste outro número", "g", 110, COR), W / 2, 900, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"] + 0.2, ps("resumindo", "i", 96, COR), W / 2, 200, "center")
        itens = ((400, "s23.a", ps("procure a", "i", 88) + ps("mesma base", "g", 82, COR)),
                 (600, "s23.b", ps("veja o que está", "i", 88) + ps("dentro do parêntese", "g", 82, COR)),
                 (800, "s23.c", ps("resolva a potência", "i", 88) + ps("antes do vezes", "g", 82, COR)))
        for i, (y, k, partes) in enumerate(itens):
            E.foco(c, t, C[k], 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), 220, y - 28, 56, 64, p))
            E.frase(c, t, C[k] + 0.1, partes, 310, y, passo=0.16)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    a, b_, c_, d, e = (C[f"s24.{k}"] for k in "abcde")
    E.frase(c, t, C["s24"] + 0.3, ps("próxima aula", "i", 84), XE, 200)
    E.frase(c, t, a, ps("o caminho de volta", "i", 104), XE, 330)
    E.frase(c, t, b_, ps("a", "i", 140) + ps("raiz quadrada", "g", 130, COR), XE, 500)
    fl(c, t, [("?^2", COR, c_), ("=", None, c_ + 0.5), ("1.764", None, c_ + 0.6)], XE, 680, 130)
    E.foco(c, t, d, 0.5, lambda p: E.pilula(c, "Inscreva-se", 1460, 640, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=p))
    p = ease_io(prog(t, d + 0.3, 0.8))
    E.cursor(c, lerp(1760, 1600, p), lerp(920, 680, p), ep(t, d + 0.2, 0.4), TINTA)
    E.frase(c, t, e, ps("bons", "i", 130) + ps("estudos!", "i", 130, COR), W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, dica=b_dica, fim=b_fim)
