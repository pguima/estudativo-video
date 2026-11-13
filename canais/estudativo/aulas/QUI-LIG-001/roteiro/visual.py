"""Visual — Estudativo · QUI-LIG-001: regra do octeto e ligação iônica. Primeira aula da trilha Ligações Químicas.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho de QUI-MIS-001/roteiro/visual.py. Acrescenta, para a trilha de ligações:
- CAMADAS (atomo_camadas): núcleo na cor da matéria com o símbolo, camadas em fio cinza e elétrons azuis (Q.ELETRON) em
  posições fixas (8 vagas por camada a partir de 3; a vaga de 180° fica livre para o elétron que chega). O elétron que passa
  de um átomo ao outro anda em linha reta, com rastro, e a camada que esvazia some tracejada.
- ÍON = bolinha do elemento (cor CPK) com a fórmula do íon dentro (íon()): "Na^+" roxo, "Cl^-" verde. A carga aparece
  também como pílula "+1" / "−1" (TINTA para +, Q.ELETRON para −) quando a aula conta cargas.
- RETÍCULO (reticulo): grade de íons alternados, que entra em onda diagonal; ligação iônica nunca vira molécula bola-vareta.
- CRUZAR CARGAS: a carga de cima vira índice de baixo por uma seta curva na cor clara, no palco.
- COVALENTE: Q.lewis (pontos azuis para pares, traço em tinta para ligação). METÁLICA: íons em fileiras + elétrons soltos.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ligações Químicas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-LIG-001_regra_do_octeto_ligacao_ionica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("octeto", "troca", "cargas", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# as contas da aula, conferidas
assert Q.camadas(11) == [2, 8, 1] and Q.camadas(17) == [2, 8, 7] and Q.camadas(13) == [2, 8, 3] and Q.camadas(8) == [2, 6]
assert 11 - 10 == 1 and 17 - 18 == -1
assert 3 - 2 == 1 and 2 * 3 + 3 * (-2) == 0 and 3 * 3 + 2 * (-2) == 5
assert Q.contar("Al2O3") == {"Al": 2, "O": 3} and Q.contar("CaF2") == {"Ca": 1, "F": 2} and 2 + 2 * (-1) == 0


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def ion(c, cx, cy, r, el, s, a=1.0, escuro=False):
    """íon: bolinha na cor do elemento com a fórmula do íon dentro"""
    if a <= 0:
        return
    Q.atomo(c, cx, cy, r, el, a, rotulo=False, escuro=escuro)
    claro = el in ("H", "S", "F", "Al", "Ag", "Au", "Hg")
    Q.formula(c, s, cx, cy + r * 0.3, r * 0.82, TINTA if claro else BR, a, "center")


def ion_em(c, t, t0, cx, cy, r, el, s, d=0.45):
    q = ease_back(prog(t, t0, d))
    if q > 0:
        ion(c, cx, cy, r * q, el, s, min(1, prog(t, t0, 0.25)))


def atomo_camadas(c, cx, cy, s, nums, r0=62, dr=48, a=1.0, vazia=None, cor_camada=None, livre=None, rot=0.0):
    """modelo de camadas parado: núcleo com o símbolo, camadas e elétrons em vagas fixas.
    vazia = índice da camada que some (0..1 = quanto já sumiu); livre = ângulo (graus) deixado sem elétron na última camada"""
    if a <= 0:
        return
    rn = r0 * 0.5
    E.bola(c, cx, cy, rn, E.COR, a)
    centro(c, s, cx, cy + rn * 0.32, rn * (0.9 if len(s) == 1 else 0.72), "g", E.SOBRE, a)
    for i, n in enumerate(nums):
        R = r0 + i * dr
        aa = a
        if vazia is not None and vazia[0] == i:
            aa = a * (1 - vazia[1])
        if aa <= 0:
            continue
        cc = (cor_camada or {}).get(i, TINTA2)
        larg = 5 if i in (cor_camada or {}) else 3
        c.drawCircle(cx, cy, R, M.paint(cc, 0.75 * aa, stroke=larg))
        if n <= 2:
            angs = [90 + 180 * j for j in range(n)]
        else:
            vagas = [180 + 45 * j for j in range(8)]
            if livre is not None and i == len(nums) - 1:
                vagas = [v for v in vagas if abs(((v - livre) + 180) % 360 - 180) > 1]
            angs = vagas[:n] if n < 8 else vagas
        for g in angs:
            g = math.radians(g + rot * (i + 1))
            E.bola(c, cx + R * math.cos(g), cy - R * math.sin(g), 13, Q.ELETRON, aa)


def reticulo(c, t, t0, x, y, cols, rows, passo=96, r1=30, r2=42, d=0.35, onda=0.06, a=1.0, rotulo=True):
    """retículo de NaCl visto de frente: Na⁺ e Cl⁻ alternados, entrando em onda diagonal"""
    for i in range(rows):
        for j in range(cols):
            ti = t0 + (i + j) * onda
            q = ease_back(prog(t, ti, d))
            if q <= 0:
                continue
            cx, cy = x + j * passo, y + i * passo
            if (i + j) % 2 == 0:
                ion(c, cx, cy, r1 * q, "Na", "Na^+" if rotulo else "", a)
            else:
                ion(c, cx, cy, r2 * q, "Cl", "Cl^-" if rotulo else "", a)


def carga(c, t, t0, s, cx, cy, size=46, neg=False):
    pilula_em(c, t, t0, s, cx, cy, size, Q.ELETRON if neg else TINTA)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: Q.atomo(c, 470, 400, 120 * ease_back(prog(t, C["s01.a"], 0.5)), "Na", a))
        E.frase(c, t, C["s01.a"] + 0.3, [("sódio", "g", 76)], 470, 610, "center")
        E.frase(c, t, C["s01.a"] + 0.7, ps("metal que reage", "i", 52, TINTA2), 470, 690, "center", 0.1)
        E.frase(c, t, C["s01.a"] + 1.0, ps("com violência na água", "i", 52, TINTA2), 470, 755, "center", 0.1)
        Q.molecula(c, t, C["s01.b"], "Cl2", 1450, 400, 150, passo=0.2)
        E.frase(c, t, C["s01.b"] + 0.3, [("cloro", "g", 76)], 1450, 610, "center")
        E.frase(c, t, C["s01.b"] + 0.7, ps("gás venenoso", "i", 52, TINTA2), 1450, 690, "center", 0.1)
        p = ep(t, C["s01.c"], 0.6)
        if p > 0:
            M.arrow(c, 640, 470, 820, 760, E.COR, p, 6, 22, ease_io(prog(t, C["s01.c"], 0.6)))
            M.arrow(c, 1280, 470, 1100, 760, E.COR, p, 6, 22, ease_io(prog(t, C["s01.c"], 0.6)))
        Q.formula_em(c, t, C["s01.c"] + 0.4, "NaCl", W / 2, 870, 160, align="center")
        E.frase(c, t, C["s01.c"] + 0.8, ps("o sal do feijão", "i", 56, TINTA2), W / 2, 950, "center", 0.1)
        E.frase(c, t, C["s01.d"], ps("o que acontece entre eles?", "i", 66) , W / 2, 1040, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1660, 560, 210 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("por que o", "i", 70), ("sódio", "g", 66, COR), ("entrega", "i", 70), ("elétron", "i", 70)]),
                 (C["s02.c"], [("montar", "g", 66), ("fórmulas", "i", 70), ("como", "i", 70)]),
                 (C["s02.d"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 440, 170)
    Q.formula_em(c, t, C["s02.c"] + 0.8, "Al2O3", XE + 780, 612, 92, cores={"indice": E.COR})


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três ideias de antes", "i", 70, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("camada de valência", "g", 66, COR), ("=", "g", 66, TINTA2)] + ps("a última", "i", 72), XE, 330, passo=0.12)
    E.frase(c, t, C["s03.b"], [("gases nobres:", "g", 62), ("8", "g", 66, COR)] + ps("nela, quase não reagem", "i", 66), XE, 470, passo=0.12)
    E.frase(c, t, C["s03.b"] + 1.6, ps("(o hélio tem 2)", "i", 52, TINTA2), XE, 545, passo=0.1)
    E.frase(c, t, C["s03.c"], [("metal", "g", 62)] + ps("perde elétrons", "i", 66) + [("→", "g", 62, TINTA2), ("íon +", "g", 62, COR)], XE, 690, passo=0.12)
    E.frase(c, t, C["s03.d"], [("ametal", "g", 62)] + ps("ganha elétrons", "i", 66) + [("→", "g", 62, TINTA2), ("íon −", "g", 62, COR)], XE, 820, passo=0.12)
    tn = C["s03.b"] + 0.3
    E.foco(c, t, tn, 0.6, lambda a: atomo_camadas(c, 1560, 470, "Ne", [2, 8], 70, 70, a, cor_camada={1: E.COR}))
    E.foco(c, t, tn + 0.6, 0.4, lambda a: centro(c, "neônio: 2, 8", 1560, 720, 50, "i", TINTA2, a))


# ---------------- octeto ----------------
def b_octeto(c, t, C, b):
    E.frase(c, t, C["s04"], ps("por que os gases nobres ficam quietos?", "i", 62, TINTA2), XE, 180, passo=0.1)
    E.frase(c, t, C["s04.a"], [("8", "g", 90, COR)] + ps("na última camada = estável", "i", 76), XE, 320, passo=0.12)
    for i, s in enumerate(("perdendo", "ganhando", "dividindo")):
        pilula_em(c, t, C["s04.b"] + 0.35 * i, s, XE + 160 + i * 330, 430, 52, TINTA if i < 2 else TINTA2)
    E.frase(c, t, C["s04.b"] + 1.6, ps("dividir: próxima aula", "i", 44, TINTA2), XE + 840, 515, passo=0.08)
    E.frase(c, t, C["s04.c"], [("regra do", "i", 96)], XE, 610)
    E.frase(c, t, C["s04.c"] + 0.4, [("octeto", "g", 170, COR)], XE, 780)
    E.frase(c, t, C["s04.c"] + 1.2, ps("octeto = grupo de oito", "i", 54, TINTA2), XE, 870, passo=0.1)
    E.foco(c, t, C["s04.a"] + 0.4, 0.6, lambda a: atomo_camadas(c, 1600, 650, "Ar", [2, 8, 8], 60, 58, a, cor_camada={2: E.COR}))
    for k, el in enumerate(("H", "He")):
        Q.atomo_em(c, t, C["s04.d"] + 0.3 * k, XE + 50 + 130 * k, 985, 44, el)
    E.frase(c, t, C["s04.d"] + 0.7, [("hidrogênio:", "i", 56), ("2", "g", 56, COR)] + ps("como o hélio", "i", 56), XE + 260, 1005, passo=0.1)
    pilula_em(c, t, C["s04.e"], "a regra tem exceções: outra aula", 1530, 1010, 40, TINTA2, "b")


# ---------------- troca (s05–s07) ----------------
NX, CX_, AY = 560, 1360, 450
R3 = 62 + 2 * 48


def b_troca(c, t, C, b):
    te = C["s06.d"]                       # o elétron passa
    k = ease_io(prog(t, te, 1.4))         # 0..1 do caminho
    # sódio
    vazio = (2, ep(t, te + 1.2, 0.6)) if t >= te + 1.2 else None
    na_nums = [2, 8, 1] if k <= 0 else [2, 8, 0]
    E.foco(c, t, C["s05.a"], 0.6, lambda a: atomo_camadas(c, NX, AY, "Na", na_nums, a=a, vazia=vazio,
                                                         cor_camada={1: E.COR} if t >= C["s05.e"] else None, livre=None))
    E.foco(c, t, C["s05.a"] + 0.2, 0.4, lambda a: centro(c, "sódio · Z = 11", NX, 250, 52, "b", TINTA, a))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: (centro(c, "2, 8,", NX - 40, 700, 76, "g", TINTA, a),
                                            E.escreve(c, "1", NX + 95, 700, 76, "g", ERRADO if t >= C["s05.c"] else TINTA, a)))
    if C["s05.c"] <= t < te:
        q = ep(t, C["s05.c"], 0.4)
        c.drawCircle(NX + R3, AY, 30 + 4 * math.sin(t * 6), M.paint(E.COR, q, stroke=6))
    E.saida(c, t, C["s07"], lambda: pilula_em(c, t, C["s05.d"], "perder 1 é fácil", NX, 790, 46, E.COR))
    # cloro
    cl_nums = [2, 8, 7]
    E.foco(c, t, C["s06.a"], 0.6, lambda a: atomo_camadas(c, CX_, AY, "Cl", cl_nums, a=a, livre=180,
                                                          cor_camada={2: E.COR} if t >= C["s06.e"] else None))
    E.foco(c, t, C["s06.a"] + 0.2, 0.4, lambda a: centro(c, "cloro · Z = 17", CX_, 250, 52, "b", TINTA, a))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: centro(c, "2, 8, 7", CX_, 700, 76, "g", TINTA, a))
    if C["s06.c"] <= t < te + 1.4:
        q = ep(t, C["s06.c"], 0.4)
        c.drawCircle(CX_ - R3, AY, 30 + 4 * math.sin(t * 6), M.paint(E.COR, q, stroke=6))
    E.saida(c, t, C["s07"], lambda: pilula_em(c, t, C["s06.c"] + 0.3, "falta 1", CX_, 790, 46, E.COR))
    # o elétron que viaja
    if t >= C["s05.a"] + 0.3:
        x0, x1 = NX + R3, CX_ - R3
        if k > 0:
            for r_ in range(6):
                kk = max(0, k - r_ * 0.04)
                E.bola(c, lerp(x0, x1, kk), AY - 60 * math.sin(math.pi * kk), 13, Q.ELETRON, 0.18 * (6 - r_) / 6 if r_ else 1)
        else:
            E.foco(c, t, C["s05.a"] + 0.3, 0.3, lambda a: E.bola(c, x0, AY, 13, Q.ELETRON, a))
    E.foco(c, t, C["s06.e"], 0.5, lambda a: E.pilula(c, "os dois com 8", W / 2, 150, 46, "g", fundo=E.COR, a=a))
    # s07: as cargas
    E.foco(c, t, C["s07"] + 0.6, 0.4, lambda a: centro(c, "11 prótons, 10 elétrons", NX, 810, 50, "i", TINTA2, a))
    E.foco(c, t, C["s07.a"], 0.4, lambda a: centro(c, "sobra +1", NX, 880, 50, "b", TINTA, a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: Q.formula(c, "Na^+", NX, 1020, 120, None, a, "center", cores={"carga": E.COR}))
    E.foco(c, t, C["s07.b"] + 1.2, 0.4, lambda a: centro(c, "17 prótons, 18 elétrons", CX_, 810, 50, "i", TINTA2, a))
    E.foco(c, t, C["s07.c"], 0.4, lambda a: centro(c, "sobra −1", CX_, 880, 50, "b", TINTA, a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: Q.formula(c, "Cl^-", CX_, 1020, 120, None, a, "center", cores={"carga": E.COR}))


# ---------------- ligação iônica (s08–s09) ----------------
def b_ionica(c, t, C, b):
    def s08():
        aprox = ease_io(prog(t, C["s08.a"], 1.4))
        xa, xb = lerp(560, 820, aprox), lerp(1360, 1100, aprox)
        ion_em(c, t, C["s08"], xa, 470, 90, "Na", "Na^+")
        ion_em(c, t, C["s08"] + 0.2, xb, 470, 120, "Cl", "Cl^-")
        if t >= C["s08.a"]:
            q = ep(t, C["s08.a"], 0.4)
            for s_ in (-1, 1):
                M.arrow(c, W / 2 + s_ * 190, 300, W / 2 + s_ * 40, 300, E.COR, q, 6, 20)
        E.frase(c, t, C["s08.a"], ps("cargas opostas se atraem", "i", 70), W / 2, 210, "center", 0.12)
        E.frase(c, t, C["s08.b"], [("ligação", "g", 120), ("iônica", "g", 120, COR)], W / 2, 770, "center", 0.2)
        E.frase(c, t, C["s08.b"] + 0.9, ps("atração entre íons de cargas opostas", "i", 56, TINTA2), W / 2, 860, "center", 0.08)
        pilula_em(c, t, C["s08.c"], "metal: perde elétrons", 640, 980, 50, TINTA)
        pilula_em(c, t, C["s08.d"], "ametal: ganha elétrons", 1280, 980, 50, E.COR)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], ps("o sal não forma moléculas", "i", 70), XE, 200, passo=0.12)
    reticulo(c, t, C["s09.a"], 1080, 250, 7, 7, 100, 30, 42)
    E.frase(c, t, C["s09.b"], [("retículo", "g", 90, COR)], XE, 390)
    E.frase(c, t, C["s09.b"] + 0.5, [("cristalino", "g", 90, COR)], XE, 490)
    E.frase(c, t, C["s09.c"], ps("num grão de sal:", "i", 58, TINTA2), XE, 610, passo=0.1)
    E.frase(c, t, C["s09.c"] + 0.6, [("bilhões de bilhões", "g", 56)] + ps("de íons", "i", 58), XE, 690, passo=0.12)
    Q.formula_em(c, t, C["s09.d"], "NaCl", XE, 880, 150)
    E.foco(c, t, C["s09.d"] + 1.0, 0.4, lambda a: E.escreve(c, "1 molécula", XE + 430, 860, 60, "i", ERRADO, a))
    if t >= C["s09.d"] + 1.6:
        E.risco(c, XE + 415, 865, XE + 720, 815, t, C["s09.d"] + 1.6, largura=8)
    E.foco(c, t, C["s09.e"], 0.5, lambda a: E.pilula(c, "proporção 1 : 1", XE + 300, 980, 54, "g", fundo=E.COR, a=a))


# ---------------- cargas diferentes (s10–s11) ----------------
def fichas(c, t, itens, x, y, dx, r=56):
    """fileira de íons: itens = [(el, s, t0)]"""
    for i, (el, s, t0) in enumerate(itens):
        ion_em(c, t, t0, x + i * dx, y, r, el, s)


def b_cargas(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10"], ps("e se as cargas forem diferentes?", "i", 70, TINTA2), XE, 190, passo=0.1)
        for k, (cue, el, nome, fam, z, n, s, prox) in enumerate((("s10.a", "Al", "alumínio", "família 13", [2, 8, 3], "perde 3", "Al^{3+}", "s10.b"),
                                                                  ("s10.c", "O", "oxigênio", "família 16", [2, 6], "ganha 2", "O^{2-}", "s10.d"))):
            cx = 560 + 800 * k
            E.foco(c, t, C[cue], 0.6, lambda a, el=el, z=z, cx=cx: atomo_camadas(c, cx, 520, el, z, 62, 48, a, cor_camada={len(z) - 1: E.COR}))
            E.frase(c, t, C[cue] + 0.2, [(nome, "g", 60), (fam, "i", 56, TINTA2)], cx, 320, "center", 0.12)
            pilula_em(c, t, C[cue] + 1.2, n, cx, 760, 50, TINTA if k == 0 else Q.ELETRON)
            E.foco(c, t, C[prox], 0.5, lambda a, s=s, cx=cx: Q.formula(c, s, cx, 950, 150, None, a, "center", cores={"carga": E.COR}))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], ps("o composto tem carga total", "i", 70) + [("zero", "g", 70, COR)], XE, 190, passo=0.12)

    def tentativa():
        fichas(c, t, [("Al", "Al^{3+}", C["s11.b"]), ("O", "O^{2-}", C["s11.b"] + 0.3)], XE + 80, 400, 170)
        E.foco(c, t, C["s11.b"] + 0.8, 0.4, lambda a: E.formula(c, "+3 − 2 = +1", XE + 480, 420, 76, "g", TINTA, a))
        E.foco(c, t, C["s11.b"] + 1.6, 0.4, lambda a: E.selo(c, XE + 1050, 395, 48, False, a))
    E.saida(c, t, C["s11.c"] - 0.1, tentativa)
    if t < C["s11.c"]:
        return
    fichas(c, t, [("Al", "Al^{3+}", C["s11.c"]), ("Al", "Al^{3+}", C["s11.c"] + 0.3)], XE + 80, 420, 150)
    E.foco(c, t, C["s11.c"] + 0.8, 0.4, lambda a: E.formula(c, "+3 + 3 = +6", XE + 400, 445, 76, "g", TINTA, a))
    fichas(c, t, [("O", "O^{2-}", C["s11.d"] + 0.3 * i) for i in range(3)], XE + 80, 620, 150)
    E.foco(c, t, C["s11.d"] + 1.1, 0.4, lambda a: E.formula(c, "−2 − 2 − 2 = −6", XE + 550, 645, 76, "g", Q.ELETRON, a))
    E.foco(c, t, C["s11.e"], 0.5, lambda a: E.selo(c, 1560, 540, 60, True, a))
    Q.formula_em(c, t, C["s11.e"], "Al2O3", W / 2, 950, 180, align="center", cores={"indice": E.COR})


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("a carga vira o próprio índice?", "i", 64), XE + 460, 190, passo=0.1)
    E.foco(c, t, C["s12.a"] + 0.6, 0.4, lambda a: Q.formula(c, "Al^{3+}  O^{2-}", XE, 400, 110, None, a, cores={"carga": ERRADO}))
    E.foco(c, t, C["s12.a"] + 1.6, 0.5, lambda a: Q.formula(c, "Al3O2", XE + 760, 400, 150, ERRADO, a))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.formula(c, "3 alumínios: +3 + 3 + 3 = +9", XE, 600, 70, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.4, lambda a: E.formula(c, "2 oxigênios: −2 − 2 = −4", XE, 720, 70, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: E.formula(c, "sobra +5", XE, 870, 84, "g", ERRADO, a))
    E.foco(c, t, C["s12.d"] + 0.6, 0.4, lambda a: E.pilula(c, "não zerou", XE + 600, 845, 56, "g", fundo=ERRADO, a=a))
    if t >= C["s12.d"] + 1.0:
        E.risco(c, XE + 740, 420, XE + 1180, 300, t, C["s12.d"] + 1.0, largura=12)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s13.a"], [("cruze", "g", 84, BR), ("as", "i", 88, CLARO), ("cargas", "g", 84, BR)], W / 2, 270, "center", 0.12)
            E.frase(c, t, C["s13.b"], ps("a carga de um vira o índice do outro, sem o sinal", "i", 52, CLARO), W / 2, 350, "center", 0.07)
            ya, yb, fs = 560, 900, 190
            xa, xo = 640, 1120
            E.foco(c, t, C["s13"] + 1.0, 0.5, lambda a: (Q.formula(c, "Al^{3+}", xa, ya, fs, BR, a, "center", cores={"carga": E.CLARO}),
                                                         Q.formula(c, "O^{2-}", xo, ya, fs, BR, a, "center", cores={"carga": E.CLARO})))
            # setas cruzadas: carga do Al → índice do O e carga do O → índice do Al
            for k, (cue, x0, x1) in enumerate((("s13.c", xa + 120, xo + 120), ("s13.d", xo + 100, xa + 70))):
                p = ease_io(prog(t, C[cue], 0.8))
                if p > 0:
                    pth = skia.Path()
                    pth.moveTo(x0, ya - 150)
                    pth.cubicTo(x0 + (60 if k == 0 else -60), ya + 120, x1 + (-60 if k == 0 else 60), yb - 260, x1, yb - 10)
                    seg = skia.Path()
                    me = skia.PathMeasure(pth, False)
                    me.getSegment(0, me.getLength() * p, seg, True)
                    c.drawPath(seg, M.paint(E.CLARO, 1.0, stroke=6))
            Q.formula_em(c, t, C["s13.e"], "Al2O3", W / 2 - 20, yb + 60, 200, align="center", cores={"indice": E.CLARO}, escuro=True)
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], ps("por que funciona:", "i", 60, CLARO), XE, 180, passo=0.1)
    E.foco(c, t, C["s14.a"] + 0.6, 0.4, lambda a: E.formula(c, "2 alumínios: +3 + 3 = +6", XE, 290, 64, "g", BR, a))
    E.foco(c, t, C["s14.a"] + 1.4, 0.4, lambda a: E.formula(c, "3 oxigênios: −2 − 2 − 2 = −6", XE, 380, 64, "g", BR, a))
    E.frase(c, t, C["s14.b"], ps("depois de cruzar,", "i", 66, CLARO) + [("simplifique", "g", 62, BR)], XE, 540, passo=0.12)
    Q.formula_em(c, t, C["s14.c"], "Mg^{2+}  O^{2-}", XE, 720, 120, escuro=True, cores={"carga": E.CLARO})
    E.foco(c, t, C["s14.c"] + 1.2, 0.4, lambda a: E.formula(c, "→", XE + 640, 715, 100, "g", CLARO, a))
    Q.formula_em(c, t, C["s14.c"] + 1.5, "Mg2O2", XE + 780, 720, 130, escuro=True)
    if t >= C["s14.d"]:
        E.risco(c, XE + 770, 740, XE + 1170, 630, t, C["s14.d"], largura=10)
    Q.formula_em(c, t, C["s14.d"] + 0.4, "MgO", XE + 1250, 720, 150, escuro=True, cores={"Mg": E.CLARO, "O": E.CLARO})
    E.frase(c, t, C["s14.d"] + 1.0, ps("a menor proporção: 1 para 1", "i", 56, CLARO), XE + 780, 840, passo=0.1)
    pilula_em(c, t, C["s14.d"] + 2.4, "cargas do mesmo tamanho: nem precisa cruzar", W / 2, 980, 44, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.foco(c, t, C["s15.a"], 0.5, lambda a: (Q.atomo(c, XE + 50, 330, 44, "Ca", a), E.escreve(c, "cálcio: família 2", XE + 120, 350, 64, "b", TINTA, a)))
    E.foco(c, t, C["s15.b"], 0.5, lambda a: (Q.atomo(c, XE + 50, 460, 40, "F", a), E.escreve(c, "flúor: família 17", XE + 120, 480, 64, "b", TINTA, a)))
    E.frase(c, t, C["s15.c"], [("1", "g", 56, COR)] + ps("que íon cada um forma?", "i", 62), XE, 680, passo=0.08)
    E.frase(c, t, C["s15.d"], [("2", "g", 56, COR)] + ps("qual é a fórmula do composto?", "i", 62), XE, 790, passo=0.08)
    if t < C["s16"]:
        pos = Q.tabela(c, t, C["s15.a"] - 0.3, 1060, 300, 40, numeros=False, destaque=("Ca", "F"), d=1.0)
    else:
        E.relogio(c, t, C["s16.a"], cx=1480, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        E.frase(c, t, C["s17"], ps("vamos lá", "i", 66, TINTA2), XE, 170)
        E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "família 2: 2 na valência, perde", XE, 300, 56, "b", TINTA, a))
        Q.formula_em(c, t, C["s17.a"] + 1.0, "Ca^{2+}", XE + 1060, 310, 100, cores={"carga": E.COR})
        E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "família 17: 7 na valência, ganha 1", XE, 440, 56, "b", TINTA, a))
        Q.formula_em(c, t, C["s17.b"] + 1.0, "F^-", XE + 1060, 450, 100, cores={"carga": E.COR})
        ya, yb = 690, 960
        xa, xf = 620, 1000
        E.foco(c, t, C["s17.c"], 0.4, lambda a: (Q.formula(c, "Ca^{2+}", xa, ya, 140, None, a, "center", cores={"carga": E.COR}),
                                                 Q.formula(c, "F^-", xf, ya, 140, None, a, "center", cores={"carga": E.COR})))
        for k, (dt, x0, x1) in enumerate(((0.5, xa + 95, xf + 70), (1.4, xf + 60, xa + 40))):
            p = ease_io(prog(t, C["s17.c"] + dt, 0.7))
            if p > 0:
                M.arrow(c, x0, ya - 110, x1, yb - 60, E.COR, 1.0, 5, 18, p)
        Q.formula_em(c, t, C["s17.d"], "CaF2", 800, yb + 40, 170, align="center", cores={"indice": E.COR})
        E.foco(c, t, C["s17.c"] + 2.2, 0.4, lambda a: E.pilula(c, "o 1 não se escreve", 1400, 900, 46, "g", fundo=TINTA2, a=a))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    Q.formula_em(c, t, C["s18"], "CaF2", W / 2, 300, 190, align="center", cores={"indice": E.COR})
    E.foco(c, t, C["s18.a"], 0.4, lambda a: E.formula(c, "1 cálcio: +2", XE + 200, 480, 72, "g", TINTA, a))
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.formula(c, "2 flúores: −1 − 1 = −2", XE + 200, 590, 72, "g", TINTA, a))
    E.foco(c, t, C["s18.c"], 0.4, lambda a: E.formula(c, "total: 0", XE + 200, 720, 84, "g", COR, a))
    bola_txt(c, t, C["s18.c"] + 0.3, "CaF₂", 1500, 600, 120, 76, CERTO)
    E.foco(c, t, C["s18.d"], 0.4, lambda a: (Q.formula(c, "Ca2F", XE + 200, 900, 100, ERRADO, a),
                                            E.escreve(c, "usou as cargas sem cruzar", XE + 520, 890, 52, "i", ERRADO, a)))
    if t >= C["s18.d"] + 0.6:
        E.risco(c, XE + 190, 915, XE + 470, 830, t, C["s18.d"] + 0.6, largura=9)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("átomos", "g", 64)] + ps("buscam 8 na última camada", "i", 66)),
                 ("s19.b", [("metal", "g", 64)] + ps("perde,", "i", 66) + [("ametal", "g", 64)] + ps("ganha", "i", 66)),
                 ("s19.c", [("íons opostos", "g", 64)] + ps("se atraem", "i", 66)),
                 ("s19.d", ps("a fórmula sai", "i", 66) + [("cruzando as cargas", "g", 64, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 24, 50, a=a), centro(c, str(i + 1), 260, y - 2, 58, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 350, y, passo=0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 240)
    E.frase(c, t, C["s20.a"], ps("dois ametais: ambos querem ganhar", "i", 60, TINTA2), XE, 340, passo=0.1)
    E.frase(c, t, C["s20.b"], [("ligação", "g", 110, COR)], XE, 490)
    E.frase(c, t, C["s20.b"] + 0.4, [("covalente", "g", 110, COR)], XE, 610)
    E.frase(c, t, C["s20.c"], ps("e a estrutura de Lewis", "i", 64), XE, 720, passo=0.1)
    Q.lewis(c, t, C["s20.c"] + 0.4, [("Cl", -0.6, 0, [90, 180, 270]), ("Cl", 0.6, 0, [90, 0, 270])], [(0, 1, 1)], 600, 900, 160, 96, pontos=True)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, octeto=b_octeto, troca=b_troca, ionica=b_ionica, cargas=b_cargas,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
