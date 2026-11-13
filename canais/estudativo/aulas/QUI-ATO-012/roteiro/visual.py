"""Visual — Estudativo · QUI-ATO-012: praticando a tabela periódica. Última aula da trilha.
Segue a linguagem visual da Química (QUI-MIS-001), a da trilha (QUI-ATO-001) e a do módulo Tabela periódica (QUI-ATO-008):
cada questão abre com a pílula "questão N", o enunciado à esquerda e o recorte da tabela à direita; seta âmbar = raio,
seta turquesa = energia de ionização e eletronegatividade; a pausa é E.relogio no lugar da tabela.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-012_praticando_tabela_periodica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
AMBAR = "#F2A33A"
ESFERA = E.mix(E.COR, "#FFFFFF", 0.55)
RAIO = dict(F=64, Cl=99, S=104, Li=152, Cs=265)
assert RAIO["F"] < RAIO["Cl"] < RAIO["S"]
K19 = Q.distribuicao(19)
assert K19[-1] == ("4s", 1) and sum(n for _, n in K19) == 19
P = Q._posicoes()
assert P["K"][1:] == (4, 1) and P["S"][1:] == (3, 16) and P["Cl"][1:] == (3, 17) and P["F"][1:] == (2, 17) and P["Cs"][1:] == (6, 1)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


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


def cabeca(c, t, t0, n):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"questão {n}", XE + 140, 160, 50, "g", fundo=TINTA, a=a))


def esfera(c, t, t0, cx, cy, pm, rotulo, k=0.9):
    q = ease_back(prog(t, t0, 0.6))
    if q <= 0:
        return
    r = pm * k * q
    E.bola(c, cx, cy, r, ESFERA)
    Q.formula(c, rotulo, cx, cy + r * 0.2, max(28, r * 0.55), TINTA, min(1, q), "center")


def setas(c, t, x, y, cel, tr=None, te=None, escuro=False):
    if tr is not None and t >= tr:
        p = ease_io(prog(t, tr, 0.9))
        x0, y0, x1, y1 = x + 16.5 * cel, y + 0.6 * cel, x + 1.5 * cel, y + 6.4 * cel
        M.arrow(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), AMBAR, ep(t, tr, 0.3), max(10, cel * 0.25), max(30, cel * 0.8))
    if te is not None and t >= te:
        p = ease_io(prog(t, te, 0.9))
        x0, y0, x1, y1 = x + 2.5 * cel, y + 6.6 * cel, x + 16.4 * cel, y + 0.8 * cel
        M.arrow(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), E.CLARO if escuro else E.COR, ep(t, te, 0.3), max(10, cel * 0.25), max(30, cel * 0.8))


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 200, COR)] + ps("questões", "i", 120), XE, 360, passo=0.2)
    E.frase(c, t, C["s01.a"] + 0.8, ps("sobre a tabela periódica, criadas para esta aula", "i", 56, TINTA2), XE, 460, passo=0.08)
    E.frase(c, t, C["s01.b"], ps("não pede para decorar,", "i", 66) + [("pede para ler", "g", 62, COR)], XE, 640, passo=0.1)
    E.frase(c, t, C["s01.c"], [("pause", "g", 66, COR)] + ps("e resolva antes da resposta", "i", 66), XE, 800, passo=0.12)
    Q.tabela(c, t, C["s01.a"] + 0.4, 1150, 260, 38, numeros=False)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("quatro ferramentas", "i", 70, TINTA2), XE, 190, passo=0.12)
    itens = (("s02.a", "período e família pela distribuição"), ("s02.b", "as famílias com nome"), ("s02.c", "a seta do raio"),
             ("s02.d", "a seta da ionização e da eletronegatividade"))
    for i, (k, s) in enumerate(itens):
        y = 340 + i * 150
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 56)], XE + 110, y)
    E.frase(c, t, C["s02.d"] + 2.4, ps("travou? procure a aula no canal", "i", 54, TINTA2), XE, 960, passo=0.08)


# ---------------- questão 1 ----------------
def b_questao1(c, t, C, b):
    cabeca(c, t, C["s03.a"], 1)
    dist(c, t, K19, [C["s03.b"] + 0.5 * k for k in range(6)], XE, 340, 86)
    E.frase(c, t, C["s03.c"], [("1", "g", 56, COR)] + ps("período e família?", "i", 60), XE, 540, passo=0.08)
    E.frase(c, t, C["s03.d"], [("2", "g", 56, COR)] + ps("metal ou ametal?", "i", 60), XE, 650, passo=0.08)
    E.frase(c, t, C["s03.e"], [("3", "g", 56, COR)] + ps("a carga do íon?", "i", 60), XE, 760, passo=0.08)
    if t >= C["s04"]:
        E.relogio(c, t, C["s04.a"], cx=1540, cy=640, r=180)


def b_resposta1(c, t, C, b):
    cx = dist(c, t, K19, [C["s05"]] * 6, XE, 240, 86, cores={5: COR} if t >= C["s05.a"] else None)
    if t >= C["s05.a"]:
        E.chave(c, cx[5][0], cx[5][1], 270, E.COR, ep(t, C["s05.a"], 0.5), 26)
    E.frase(c, t, C["s05.a"], ps("maior número: 4 —", "i", 58) + [("4º período", "g", 56, COR)], XE, 420, passo=0.08)
    E.frase(c, t, C["s05.b"], ps("1 elétron na camada 4 —", "i", 58) + [("família 1", "g", 56, COR)], XE, 520, passo=0.08)
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "metal alcalino", XE + 220, 620, 54, "g", fundo="#5B6B80", a=a))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: Q.formula(c, "K^+", XE, 820, 150, cores={"carga": E.COR}, a=a))
    E.foco(c, t, C["s05.e"] + 0.3, 0.4, lambda a: E.escreve(c, "carga um mais", XE + 260, 800, 58, "g", COR, a))
    E.foco(c, t, C["s05.f"], 0.4, lambda a: E.pilula(c, "19 elétrons: potássio", XE + 330, 940, 50, "g", fundo=E.COR, a=a))
    Q.tabela(c, t, C["s05.a"], 1150, 420, 38, numeros=False, destaque=("K",) if t >= C["s05.b"] else ())


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    cabeca(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.b"], [("F", "g", 60), ("e", "i", 62), ("Cl", "g", 60)] + ps(": família 17", "i", 62), XE, 320, passo=0.1)
    E.frase(c, t, C["s06.c"], [("S", "g", 60)] + ps(": família 16, mesmo período do Cl", "i", 62), XE, 430, passo=0.1)
    E.frase(c, t, C["s06.d"], ps("dos três, qual tem o", "i", 64) + [("maior raio?", "g", 62, COR)], XE, 600, passo=0.1)
    if t < C["s07"]:
        Q.tabela(c, t, C["s06.b"], 1150, 300, 40, numeros=False, destaque=("F", "Cl", "S"))
    else:
        E.relogio(c, t, C["s07.a"], cx=1540, cy=520, r=190)


def b_resposta2(c, t, C, b):
    Q.tabela(c, t, C["s08"], XE, 220, 52, numeros=False, destaque=("F", "Cl", "S"))
    setas(c, t, XE, 220, 52, tr=C["s08.e"] + 0.6)
    E.frase(c, t, C["s08.a"], ps("Cl embaixo do F:", "i", 56), XE, 680, passo=0.08)
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.formula(c, "F < Cl", XE + 470, 680, 60, "g", COR, a))
    E.frase(c, t, C["s08.c"], ps("S à esquerda do Cl:", "i", 56), XE, 780, passo=0.08)
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.formula(c, "Cl < S", XE + 470, 780, 60, "g", COR, a))
    for k, el in enumerate(("F", "Cl", "S")):
        esfera(c, t, C["s08.e"] + 0.3 * k, [1350, 1520, 1730][k], 620 - RAIO[el] * 0.9, RAIO[el], el)
    E.foco(c, t, C["s08.e"] + 0.8, 0.4, lambda a: E.pilula(c, "o maior raio: enxofre", 1540, 760, 54, "g", fundo=AMBAR, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("o atalho da trilha", "i", 70, CLARO), W / 2, 150, "center", 0.12)
        E.frase(c, t, C["s09.a"], ps("duas setas no rascunho", "i", 64, CLARO), W / 2, 240, "center", 0.1)
        Q.tabela(c, t, C["s09.a"] + 0.2, 420, 320, 60, numeros=False, escuro=True)
        setas(c, t, 420, 320, 60, tr=C["s09.b"], te=C["s09.d"], escuro=True)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "raio", 560, 820, 54, "g", fundo=AMBAR, a=a))
        E.foco(c, t, C["s09.e"], 0.4, lambda a: E.pilula(c, "ionização e eletronegatividade", 1300, 820, 50, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s09.e"] + 2.4, 0.4, lambda a: E.escreve(c, "na eletronegatividade, o campeão é o flúor", 420, 960, 52, "i", CLARO, a))
        return
    E.frase(c, t, C["s10.a"], ps("as três dependem de quão perto do núcleo", "i", 60, CLARO), W / 2, 300, "center", 0.08)
    E.frase(c, t, C["s10.a"] + 2.4, ps("estão os", "i", 60, CLARO) + [("elétrons de fora", "g", 58, BR)], W / 2, 400, "center", 0.1)
    E.frase(c, t, C["s10.b"], [("não", "g", 60, ERRADO)] + ps("resolve as diagonais da eletronegatividade:", "i", 60, CLARO), W / 2, 580, "center", 0.08)
    E.frase(c, t, C["s10.c"], ps("para elas, use", "i", 64, CLARO) + [("a fila", "g", 62, BR)], W / 2, 700, "center", 0.12)
    for k, el in enumerate(("F", "O", "N", "Cl", "Br", "I", "S", "C", "P", "H")):
        E.foco(c, t, C["s10.c"] + 0.6 + 0.08 * k, 0.3, lambda a, k=k, el=el: (M.rrect(c, 230 + k * 150, 800, 124, 110, 16, "#22232B", a),
                                                                            centro(c, el, 292 + k * 150, 880, 60, "g", BR, a)))


# ---------------- questão 3 ----------------
def b_questao3(c, t, C, b):
    cabeca(c, t, C["s11.a"], 3)
    E.frase(c, t, C["s11.b"], ps("no ácido do estômago,", "i", 62), XE, 320, passo=0.1)
    E.frase(c, t, C["s11.b"] + 1.2, ps("um hidrogênio preso a um cloro", "i", 62), XE, 410, passo=0.1)
    E.frase(c, t, C["s11.c"], ps("quem puxa mais os elétrons?", "i", 64) , XE, 590, passo=0.1)
    if t < C["s12"]:
        Q.molecula(c, t, C["s11.b"] + 0.4, "HCl", 1500, 480, 180)
        Q.formula_em(c, t, C["s11.b"] + 0.8, "HCl", 1500, 760, 110, align="center")
    else:
        E.relogio(c, t, C["s12.a"], cx=1540, cy=520, r=190)


def b_resposta3(c, t, C, b):
    Q.tabela(c, t, C["s13"], XE, 220, 52, numeros=False, destaque=("H", "Cl"))
    if t >= C["s13.b"]:
        q = ep(t, C["s13.b"], 0.5)
        x0, y0 = XE + 26, 220 + 26
        x1, y1 = XE + 16 * 52 + 26, 220 + 2 * 52 + 26
        M.line(c, x0, y0, lerp(x0, x1, q), lerp(y0, y1, q), AMBAR, 1, 6, dash=[14, 10])
    E.frase(c, t, C["s13.a"], ps("H no alto à esquerda, Cl mais embaixo à direita", "i", 52), XE, 640, passo=0.06)
    E.foco(c, t, C["s13.b"], 0.4, lambda a: E.pilula(c, "diagonal: vale a fila", XE + 240, 730, 50, "g", fundo=AMBAR, a=a))
    for k, el in enumerate(("F", "O", "N", "Cl", "Br", "I", "S", "C", "P", "H")):
        E.foco(c, t, C["s13.c"] + 0.1 * k, 0.3, lambda a, k=k, el=el: (M.rrect(c, XE + k * 112, 820, 96, 90, 14, E.COR if el in ("Cl", "H") else "#E6E8EC", a),
                                                                      centro(c, el, XE + 48 + k * 112, 885, 50, "g", BR if el in ("Cl", "H") else TINTA, a)))
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.escreve(c, "Cl vem antes; H é o último", XE, 990, 52, "i", TINTA2, a))
    cabo_x, cabo_y = 1500, 470
    if t >= C["s13.e"]:
        u = ease_io(prog(t, C["s13.e"], 1.0))
        Q.atomo(c, cabo_x - 230, cabo_y, 60, "H")
        Q.atomo(c, cabo_x + 230, cabo_y, 90, "Cl")
        for dx in (-16, 16):
            E.bola(c, cabo_x + 110 * u + dx, cabo_y, 15, Q.ELETRON)
        E.foco(c, t, C["s13.e"] + 0.5, 0.4, lambda a: E.pilula(c, "o cloro puxa mais", cabo_x, cabo_y + 170, 54, "g", fundo=E.COR, a=a))


# ---------------- questão 4 ----------------
def b_questao4(c, t, C, b):
    cabeca(c, t, C["s14.a"], 4)
    E.frase(c, t, C["s14.b"], [("Li", "g", 60), ("e", "i", 62), ("Cs", "g", 60)] + ps(": metais alcalinos", "i", 62), XE, 320, passo=0.1)
    E.frase(c, t, C["s14.c"], ps("o césio, bem mais embaixo", "i", 60, TINTA2), XE, 420, passo=0.1)
    E.frase(c, t, C["s14.d"], [("1", "g", 56, COR)] + ps("maior energia de ionização?", "i", 60), XE, 600, passo=0.08)
    E.frase(c, t, C["s14.e"], [("2", "g", 56, COR)] + ps("reage com mais violência na água?", "i", 60), XE, 720, passo=0.08)
    if t < C["s15"]:
        Q.tabela(c, t, C["s14.b"], 1150, 300, 40, numeros=False, destaque=("Li", "Cs"))
    else:
        E.relogio(c, t, C["s15.a"], cx=1540, cy=520, r=190)


def b_resposta4(c, t, C, b):
    if t < C["s17"]:
        Q.tabela(c, t, C["s16"], XE, 220, 50, numeros=False, destaque=("Li", "Cs"))
        setas(c, t, XE, 220, 50, te=C["s16.a"])
        E.frase(c, t, C["s16.a"], ps("a ionização cresce para cima:", "i", 56), XE, 660, passo=0.08)
        E.foco(c, t, C["s16.b"], 0.4, lambda a: E.pilula(c, "maior: lítio", XE + 900, 640, 54, "g", fundo=E.COR, a=a))
        esfera(c, t, C["s16.c"], 1400, 560, RAIO["Li"], "Li", 0.6)
        esfera(c, t, C["s16.c"] + 0.3, 1650, 520, RAIO["Cs"], "Cs", 0.6)
        E.frase(c, t, C["s16.c"], ps("o césio é bem maior: o elétron de fora fica longe", "i", 52, TINTA2), XE, 780, passo=0.06)
        E.frase(c, t, C["s16.d"], ps("perde esse elétron fácil:", "i", 58), XE, 880, passo=0.08)
        E.foco(c, t, C["s16.e"], 0.4, lambda a: E.pilula(c, "o césio reage com mais violência", XE + 1050, 860, 50, "g", fundo=ERRADO, a=a))
        return
    E.frase(c, t, C["s17"], [("pegadinha", "g", 90, ERRADO)], XE, 280)
    E.frase(c, t, C["s17.a"], ps("ionização alta =", "i", 66) + [("segura bem o elétron", "g", 62, COR)], XE, 480, passo=0.1)
    E.frase(c, t, C["s17.b"], ps("quem segura bem", "i", 66) + [("reage menos", "g", 62)], XE, 620, passo=0.1)
    E.foco(c, t, C["s17.b"] + 0.6, 0.4, lambda a: Q.formula(c, "Li", 1500, 600, 140, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s18.a", [("período e família", "g", 64, COR), ("pela distribuição", "i", 68)]),
                 ("s18.b", [("as", "i", 68), ("duas setas", "g", 64, COR)]),
                 ("s18.c", [("nas diagonais,", "i", 68), ("a fila", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.12)
        Q.tabela(c, t, C["s18.b"], 1200, 360, 34, numeros=False)
        setas(c, t, 1200, 360, 34, tr=C["s18.b"] + 0.4, te=C["s18.b"] + 0.8)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("trilha", "i", 80)], XE, 220)
    E.frase(c, t, C["s19"] + 1.0, [("Ligações Químicas", "g", 80, COR)], XE, 340)
    E.frase(c, t, C["s19.a"], ps("a", "i", 62) + [("regra do octeto", "g", 60)] + ps(": sódio e cloro", "i", 62), XE, 480, passo=0.1)
    E.frase(c, t, C["s19.b"], ps("e a fórmula cruzando as cargas", "i", 62), XE, 590, passo=0.1)
    Q.formula_em(c, t, C["s19.b"] + 1.4, "Al2O3", XE + 60, 790, 150)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
