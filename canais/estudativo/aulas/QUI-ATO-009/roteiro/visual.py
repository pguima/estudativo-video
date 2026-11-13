"""Visual — Estudativo · QUI-ATO-009: famílias com nome, metais e ametais.
Segue a linguagem visual da Química (QUI-MIS-001), a da trilha (QUI-ATO-001) e a do módulo Tabela periódica (QUI-ATO-008):
família destacada em turquesa sobre Q.tabela; classes com cores fixas do módulo (metal azul-acinzentado claro, ametal
turquesa claro, gás nobre lilás claro; semimetais ficam brancos, sem rótulo, porque esta aula não os ensina).
Íon: Q.formula com a carga na cor da matéria (+) ou no azul do elétron (−).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-009_familias_metais_ametais.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("nobres", "metais_fam", "ametais_fam", "classes", "atalho", "questao", "fim"))
BR = "#FFFFFF"
C_METAL, C_AMETAL, C_NOBRE = "#C9D3E0", "#9FE3D6", "#D9CCF2"
AMETAIS = {"H", "C", "N", "O", "F", "P", "S", "Cl", "Se", "Br", "I"}
SEMI = {"B", "Si", "Ge", "As", "Sb", "Te", "At", "Po"}
TX, TY, TC = 330, 330, 70

assert [17 - 18, 16 - 18] == [-1, -2]
assert Q.distribuicao(13)[-2:] == [("3s", 2), ("3p", 1)] and 2 + 1 == 3
assert Q._posicoes()["Mg"][2] == 2 and Q._posicoes()["Br"][2] == 17


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


def classe(s, g):
    if g == 18:
        return "nobre"
    if s in AMETAIS:
        return "ametal"
    if s in SEMI:
        return "semi"
    return "metal"


def tabela_classes(c, t, t0, x, y, cel, mostra=(), d=0.9, a=1.0, hidrogenio=True):
    """tabela com as classes pintadas: mostra = classes que já ganharam cor ("metal", "ametal", "nobre")"""
    cores = dict(metal=C_METAL, ametal=C_AMETAL, nobre=C_NOBRE)
    for s, (z, per, g) in Q._posicoes().items():
        if g is None:
            continue
        q = ep(t, t0 + ((g - 1) + (per - 1)) * d / 22, 0.35) * a
        if q <= 0:
            continue
        k = classe(s, g)
        fundo = cores[k] if k in mostra else "#FFFFFF"
        cx, cy = x + (g - 1) * cel + cel / 2, y + (per - 1) * cel + cel / 2
        M.rrect(c, cx - cel / 2 + 2, cy - cel / 2 + 2, cel - 4, cel - 4, cel * 0.12, fundo, q)
        c.drawRoundRect(skia.Rect.MakeXYWH(cx - cel / 2 + 2, cy - cel / 2 + 2, cel - 4, cel - 4), cel * 0.12, cel * 0.12, M.paint(FIO, q, stroke=2))
        if s == "H" and hidrogenio and "ametal" in mostra:
            c.drawRoundRect(skia.Rect.MakeXYWH(cx - cel / 2 + 2, cy - cel / 2 + 2, cel - 4, cel - 4), cel * 0.12, cel * 0.12, M.paint(ERRADO, q, stroke=4))
        centro(c, s, cx, cy + cel * 0.15, cel * 0.4 if len(s) <= 2 else cel * 0.32, "b", TINTA, q)


def legenda(c, t, t0, x, y, itens):
    for k, (cor, txt) in enumerate(itens):
        E.foco(c, t, t0 + 0.3 * k, 0.4, lambda a, k=k, cor=cor, txt=txt: (M.rrect(c, x + k * 360, y - 34, 44, 44, 8, cor, a),
                                                                         E.escreve(c, txt, x + 60 + k * 360, y, 46, "g", TINTA, a)))


def ion(c, t, t0, s, x, y, size):
    neg = s.endswith("-")
    Q.formula_em(c, t, t0, s, x, y, size, cores={"carga": Q.ELETRON if neg else E.COR})


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], [("sódio", "g", 80, COR)] + ps("na água: reage com violência", "i", 66), XE, 260, passo=0.1)
        E.frase(c, t, C["s01.b"], [("neônio", "g", 80, "#7A5FC0")] + ps("quase não reage", "i", 66), XE, 430, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("a diferença:", "i", 66) + [("elétrons da última camada", "g", 62, COR)], XE, 640, passo=0.1)
        Q.bohr(c, t, C["s01.a"] + 0.3, 1450, 360, (2, 8, 1), r0=60, dr=46, s="Na", r_e=10)
        Q.bohr(c, t, C["s01.b"] + 0.3, 1450, 800, (2, 8), r0=70, dr=56, s="Ne", r_e=10)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("as famílias", "i", 70), ("com nome", "g", 66, COR)]),
                 (C["s02.b"], [("metal", "g", 66), ("ou", "i", 70), ("ametal", "g", 66)]),
                 (C["s02.c"], [("a", "i", 70), ("carga do íon", "g", 66, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("das aulas anteriores", "i", 70, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("família", "g", 70, COR)] + ps("= elétrons de valência", "i", 72), XE, 380, passo=0.12)
    E.frase(c, t, C["s03.b"], [("perder", "g", 66, COR)] + ps("elétrons: positivo", "i", 70), XE, 560, passo=0.12)
    ion(c, t, C["s03.b"] + 0.6, "Na^+", XE + 900, 570, 110)
    E.frase(c, t, C["s03.c"], [("ganhar", "g", 66, Q.ELETRON)] + ps("elétrons: negativo", "i", 70), XE, 720, passo=0.12)
    ion(c, t, C["s03.c"] + 0.6, "Cl^-", XE + 900, 730, 110)


# ---------------- gases nobres ----------------
def b_nobres(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("família 18:", "i", 66) + [("gases nobres", "g", 66, "#7A5FC0")], XE, 200, passo=0.12)
        Q.tabela(c, t, C["s04"] + 0.2, TX, 300, TC, numeros=True, destaque=("He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og"), cor="#9B84D9")
        E.frase(c, t, C["s04.c"], [("8", "g", 70, COR)] + ps("elétrons na valência", "i", 64), XE, 880, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("(o hélio,", "i", 56, TINTA2) + [("2", "g", 56, COR)] + ps("): um arranjo muito estável", "i", 56, TINTA2), XE + 720, 880, passo=0.08)
        E.foco(c, t, C["s04.e"], 0.4, lambda a: E.pilula(c, "quase não reagem", W / 2, 1000, 56, "g", fundo="#7A5FC0", a=a))
        return
    E.frase(c, t, C["s05.a"], ps("os outros átomos ganham ou perdem elétrons", "i", 60), XE, 260, passo=0.08)
    E.frase(c, t, C["s05.a"] + 2.4, ps("até ficar com a última camada", "i", 60), XE, 350, passo=0.08)
    E.frase(c, t, C["s05.a"] + 3.6, ps("igual à de um", "i", 60) + [("gás nobre", "g", 58, "#7A5FC0")], XE, 440, passo=0.08)
    Q.bohr(c, t, C["s05.a"] + 0.4, 600, 760, (2, 8, 1), r0=50, dr=40, s="Na", r_e=9)
    E.foco(c, t, C["s05.a"] + 2.0, 0.4, lambda a: M.arrow(c, 760, 760, 960, 760, E.COR, a, 6, 22))
    Q.bohr(c, t, C["s05.a"] + 2.2, 1140, 760, (2, 8), r0=50, dr=40, s="Na", r_e=9)
    E.foco(c, t, C["s05.a"] + 2.6, 0.4, lambda a: E.formula(c, "= Ne", 1280, 780, 64, "g", "#7A5FC0", a))
    pilula_em(c, t, C["s05.b"], "a base das ligações: outra aula", 1400, 590, 44, TINTA2, "b")


# ---------------- famílias de metais ----------------
def b_metais_fam(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("família 1:", "i", 66) + [("metais alcalinos", "g", 66, COR)], XE, 200, passo=0.12)
        Q.tabela(c, t, C["s06"] + 0.2, TX, 300, TC, numeros=True, destaque=("Li", "Na", "K", "Rb", "Cs", "Fr"))
        E.frase(c, t, C["s06.c"], [("1", "g", 70, COR)] + ps("elétron na valência, perdido com facilidade", "i", 58), XE, 880, passo=0.08)
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "reagem com violência na água", 1480, 180, 46, "b", fundo=TINTA, a=a))
        ion(c, t, C["s06.e"], "Na^+", 1500, 1010, 110)
        E.foco(c, t, C["s06.e"] + 0.3, 0.4, lambda a: E.escreve(c, "carga um mais", XE, 990, 60, "g", COR, a))
        return
    E.frase(c, t, C["s07.a"], ps("família 2:", "i", 66) + [("metais alcalinoterrosos", "g", 62, COR)], XE, 200, passo=0.12)
    Q.tabela(c, t, C["s07"] + 0.2, TX, 300, TC, numeros=True, familia=2)
    E.frase(c, t, C["s07.b"], ps("magnésio e cálcio, o dos ossos", "i", 56, TINTA2), XE, 880, passo=0.08)
    E.frase(c, t, C["s07.c"], [("2", "g", 70, COR)] + ps("elétrons na valência", "i", 58), XE, 990, passo=0.08)
    ion(c, t, C["s07.d"], "Mg^{2+}", 1450, 1010, 110)
    E.foco(c, t, C["s07.d"] + 0.3, 0.4, lambda a: E.escreve(c, "dois mais", 1130, 990, 56, "g", COR, a))


# ---------------- famílias de ametais ----------------
def b_ametais_fam(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("família 17:", "i", 66) + [("halogênios", "g", 66, COR)], XE, 200, passo=0.12)
        Q.tabela(c, t, C["s08"] + 0.2, TX, 300, TC, numeros=True, destaque=("F", "Cl", "Br", "I"))
        E.frase(c, t, C["s08.c"], ps("flúor na pasta de dente, cloro na água", "i", 54, TINTA2), XE + 640, 220, passo=0.08)
        E.frase(c, t, C["s08.d"], [("7", "g", 70, COR)] + ps("elétrons na valência:", "i", 58) + [("falta 1 para 8", "g", 56)], XE, 880, passo=0.08)
        ion(c, t, C["s08.f"], "Cl^-", 1500, 1010, 110)
        E.foco(c, t, C["s08.f"] + 0.3, 0.4, lambda a: E.escreve(c, "ganha 1: carga um menos", XE, 990, 60, "g", Q.ELETRON, a))
        return
    E.frase(c, t, C["s09.a"], ps("família 16:", "i", 66) + [("calcogênios", "g", 66, COR)], XE, 200, passo=0.12)
    Q.tabela(c, t, C["s09"] + 0.2, TX, 300, TC, numeros=True, destaque=("O", "S") if t >= C["s09.b"] else (), familia=16 if t < C["s09.b"] else None)
    E.frase(c, t, C["s09.c"], [("6", "g", 70, COR)] + ps("elétrons na valência: ganham 2", "i", 58), XE, 880, passo=0.08)
    ion(c, t, C["s09.d"], "O^{2-}", 1450, 1010, 110)
    E.foco(c, t, C["s09.d"] + 0.3, 0.4, lambda a: E.escreve(c, "dois menos", 1100, 990, 56, "g", Q.ELETRON, a))


# ---------------- metais e ametais ----------------
def b_classes(c, t, C, b):
    mostra = ()
    if t >= C["s10.b"]:
        mostra = ("metal",)
    if t >= C["s11.a"]:
        mostra = ("metal", "ametal", "nobre")
    tabela_classes(c, t, C["s10"] + 0.2, TX, 200, TC, mostra, hidrogenio=False)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("metais", "g", 66), ("e", "i", 70), ("ametais", "g", 66, COR)], XE, 120, passo=0.12)
        for k, (ck, s) in enumerate((("s10.c", "brilho"), ("s10.c", "conduzem calor e eletricidade"), ("s10.d", "viram fio ou chapa"))):
            pilula_em(c, t, C[ck] + 0.6 * (k % 2), s, [330, 790, 1440][k], 760, 44, "#5B6B80", "b")
        E.frase(c, t, C["s10.e"], ps("poucos elétrons na valência:", "i", 58) + [("perdem", "g", 56, COR)] + ps("e viram", "i", 58) + [("cátions", "g", 56, COR)], XE, 880, passo=0.08)
        legenda(c, t, C["s10.b"], XE, 1010, [(C_METAL, "metais")])
        return
    E.frase(c, t, C["s11.a"], [("ametais:", "g", 62, COR)] + ps("no canto de cima, à direita", "i", 62), XE, 120, passo=0.1)
    pilula_em(c, t, C["s11.b"], "sem brilho de metal, conduzem mal", 640, 760, 44, "#1F8A78", "b")
    E.frase(c, t, C["s11.c"], ps("muitos elétrons na valência:", "i", 58) + [("ganham", "g", 56, Q.ELETRON)] + ps("e viram", "i", 58) + [("ânions", "g", 56, Q.ELETRON)], XE, 880, passo=0.08)
    legenda(c, t, C["s11.a"], XE, 1010, [(C_METAL, "metais"), (C_AMETAL, "ametais"), (C_NOBRE, "gases nobres")])


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 170)
    E.frase(c, t, C["s12.a"], ps("hidrogênio é metal alcalino?", "i", 66), XE, 290, passo=0.1)
    if t >= C["s12.c"]:
        E.risco(c, XE, 305, XE + 820, 240, t, C["s12.c"], largura=12)
    Q.tabela(c, t, C["s12"] + 0.2, 1000, 380, 46, numeros=False, destaque=("H",), familia=None)
    E.frase(c, t, C["s12.b"], ps("tem 1 elétron na valência,", "i", 60), XE, 450, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("mas é um", "i", 60) + [("gás", "g", 58)] + ps("e", "i", 60) + [("não é metal", "g", 58, ERRADO)], XE, 560, passo=0.1)
    E.frase(c, t, C["s12.d"], ps("muitas tabelas o desenham", "i", 58, TINTA2) + [("separado", "g", 56)], XE, 760, passo=0.08)
    E.foco(c, t, C["s12.d"] + 1.0, 0.5, lambda a: (M.rrect(c, 1700, 760, 120, 120, 16, E.COR, a, shadow=True), centro(c, "H", 1760, 845, 70, "g", E.SOBRE, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o atalho para a carga do íon", "i", 70, CLARO), W / 2, 150, "center", 0.12)
        E.frase(c, t, C["s13.a"], [("metal", "g", 64, BR)] + ps("das famílias 1 e 2:", "i", 64, CLARO), XE, 290, passo=0.12)
        E.foco(c, t, C["s13.b"], 0.4, lambda a: E.pilula(c, "carga = + família", XE + 1180, 270, 56, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s13.c"], [("alumínio,", "g", 60, BR)] + ps("família 13, 3 na valência:", "i", 60, CLARO), XE, 410, passo=0.1)
        Q.formula_em(c, t, C["s13.c"] + 1.4, "Al^{3+}", XE + 1180, 420, 90, escuro=True)
        E.frase(c, t, C["s13.d"], [("ametal:", "g", 64, BR)], XE, 580)
        E.foco(c, t, C["s13.e"], 0.4, lambda a: E.pilula(c, "carga = família − 18", XE + 640, 560, 56, "g", fundo=E.COR, a=a))
        E.formula_em(c, t, C["s13.f"], "17 − 18 = −1", XE, 760, 96, "g", BR)
        Q.formula_em(c, t, C["s13.f"] + 0.6, "Cl^-", XE + 760, 760, 96, escuro=True)
        E.formula_em(c, t, C["s13.g"], "16 − 18 = −2", XE, 900, 96, "g", BR)
        Q.formula_em(c, t, C["s13.g"] + 0.6, "O^{2-}", XE + 760, 900, 96, escuro=True)
        return
    E.frase(c, t, C["s14.a"], [("metal", "g", 62, BR)] + ps("perde o que tem na valência", "i", 64, CLARO), W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("ametal", "g", 62, BR)] + ps("ganha o que falta para 8", "i", 64, CLARO), W / 2, 400, "center", 0.12)
    E.frase(c, t, C["s14.c"], [("não", "g", 62, ERRADO)] + ps("serve para os metais do meio da tabela:", "i", 62, CLARO), W / 2, 580, "center", 0.1)
    Q.formula_em(c, t, C["s14.d"], "Fe^{2+}", W / 2 - 300, 800, 130, escuro=True)
    E.foco(c, t, C["s14.d"] + 0.4, 0.4, lambda a: E.escreve(c, "e", W / 2 - 20, 790, 70, "i", CLARO, a))
    Q.formula_em(c, t, C["s14.d"] + 0.8, "Fe^{3+}", W / 2 + 100, 800, 130, escuro=True)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15.a"], [("magnésio:", "g", 66)] + ps("família 2", "i", 66), XE, 330, passo=0.12)
    E.frase(c, t, C["s15.b"], [("bromo:", "g", 66)] + ps("família 17", "i", 66), XE, 450, passo=0.12)
    E.frase(c, t, C["s15.c"], [("1", "g", 56, COR)] + ps("metal ou ametal?", "i", 60), XE, 640, passo=0.08)
    E.frase(c, t, C["s15.d"], [("2", "g", 56, COR)] + ps("qual é a carga do íon de cada um?", "i", 60), XE, 760, passo=0.08)
    if t < C["s16"]:
        Q.tabela(c, t, C["s15.a"], 1100, 300, 40, numeros=True, destaque=("Mg", "Br"))
    else:
        E.relogio(c, t, C["s16.a"], cx=1540, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    for k, (ka, kb, kc, el, fam, tipo, nome, conta, ion_s) in enumerate((
            ("s17.a", "s17.b", "s17.c", "magnésio", "família 2", "metal", "alcalinoterroso", "perde 2", "Mg^{2+}"),
            ("s17.d", "s17.e", "s17.f", "bromo", "família 17", "ametal", "halogênio", "17 − 18 = −1", "Br^-"))):
        x = XE + k * 860
        E.frase(c, t, C[ka], [(el, "g", 70), (fam, "i", 60, TINTA2)], x, 260, passo=0.15)
        E.foco(c, t, C[kb], 0.4, lambda a, x=x, tipo=tipo: E.pilula(c, tipo, x + 110, 380, 60, "g", fundo="#5B6B80" if tipo == "metal" else "#1F8A78", a=a))
        E.foco(c, t, C[kb] + 0.3, 0.4, lambda a, x=x, nome=nome: E.escreve(c, nome, x + 260, 400, 54, "i", TINTA, a))
        E.foco(c, t, C[kc], 0.4, lambda a, x=x, conta=conta: E.formula(c, conta, x, 560, 66, "g", TINTA2, a))
        ion(c, t, C[kc] + 0.5, ion_s, x, 800, 170)
    E.foco(c, t, C["s17.c"] + 0.8, 0.4, lambda a: E.escreve(c, "dois mais", XE, 900, 54, "g", COR, a))
    E.foco(c, t, C["s17.f"] + 0.8, 0.4, lambda a: E.escreve(c, "um menos", XE + 860, 900, 54, "g", Q.ELETRON, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        for k, (nome, n, cor) in enumerate((("alcalinos", "1", COR), ("halogênios", "7", COR), ("gases nobres", "8", "#7A5FC0"))):
            x = 360 + k * 600
            E.foco(c, t, C["s18.a"] + 0.6 * k, 0.4, lambda a, x=x, nome=nome, n=n, cor=cor: (E.bola(c, x, 370, 80, cor if cor != COR else None, a),
                                                                                         centro(c, n, x, 398, 80, "g", E.SOBRE, a), centro(c, nome, x, 510, 54, "g", TINTA, a)))
        E.frase(c, t, C["s18.b"], [("metal", "g", 66)] + ps("perde e vira", "i", 68) + [("cátion", "g", 66, COR)], XE, 720, passo=0.12)
        E.frase(c, t, C["s18.c"], [("ametal", "g", 66)] + ps("ganha e vira", "i", 68) + [("ânion", "g", 66, Q.ELETRON)], XE, 860, passo=0.12)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s19.a"], ps("qual átomo é", "i", 76) + [("maior?", "g", 76, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s19.b"], ps("só pela posição na tabela", "i", 64, TINTA2), XE, 510, passo=0.1)
    for k, r in enumerate((40, 60, 85)):
        E.foco(c, t, C["s19.b"] + 0.3 * k, 0.4, lambda a, k=k, r=r: E.bola(c, XE + 120 + k * 230, 760, r, a=a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nobres=b_nobres, metais_fam=b_metais_fam, ametais_fam=b_ametais_fam, classes=b_classes,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
