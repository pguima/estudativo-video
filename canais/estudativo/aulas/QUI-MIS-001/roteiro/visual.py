"""Visual — Estudativo · QUI-MIS-001: átomos, moléculas e fórmulas. Primeira aula de Química.

LINGUAGEM VISUAL DA QUÍMICA (todas as aulas QUI-* copiam daqui; peças em _ferramentas/quimica.py, importado como Q):
- Matéria: E.usar("Química", "<Trilha>"). Turquesa #00B8A0 (formas, esferas, cortina); texto na cor da matéria sai em
  E.COR_TEXTO (#005C50, turquesa escuro), porque o turquesa puro some sobre o papel. Forma-símbolo = hexágono com volume,
  como o anel do benzeno (E.simbolo / E.hexagono): na promessa do gancho, nas capas e na tira da matéria.
- FÓRMULA E EQUAÇÃO: sempre Q.formula / Q.formula_em / Q.equacao, na grotesca, em tinta. NUNCA em E.frase com itálico: a
  serifada não tem índice, carga, seta nem Δ. O pedaço que a fala explica vai na cor da matéria (cores={"H": COR},
  {"indice": COR}, {"coef": COR}); a caixa pontilhada (Q.grupos + E.caixa_pontilhada) marca um símbolo com o índice dele.
  Índice que "vale um" e não aparece = "1" em cinza, entre tracejados. Estados (s) (l) (g) (aq) pequenos e cinza.
- ÁTOMO = bolinha com volume na cor do elemento (modelo CPK, Q.atomo): H branco, C cinza-escuro, O vermelho, N azul, Cl verde,
  S amarelo, Na roxo... e o símbolo dentro. A cor é do ELEMENTO: mesma cor = mesmo elemento, em toda a matéria.
  MOLÉCULA = bola-vareta (Q.molecula): átomos pulam na fala, varetas cinza surgem quando as duas pontas existem; dupla =
  duas varetas. Desfazer a molécula = Q.molecula(..., separa=0..1). Fórmula nova vem com o modelo ao lado (fórmula à
  esquerda, modelo à direita) na primeira vez em que aparece.
- CONTAGEM DE ÁTOMOS: Q.inventario — bolinha do elemento, número em COR_TEXTO e o nome em itálico; o total fica embaixo do
  traço. Conta de apoio em cinza-tinta (TINTA2); resultado final na esfera turquesa (E.bola + E.SOBRE).
- ELÉTRON e par de elétrons: azul Q.ELETRON (o mesmo azul da carga negativa na Física); núcleo na cor da matéria (Q.bohr).
- FRASCO: vidro em cinza (Q.VIDRO) com véu branco; líquido incolor = Q.AGUA. O líquido só muda de cor para mostrar reação ou
  indicador (Q.muda_cor, Q.cor_ph). Partículas no frasco = Q.particulas (sólido em grade, líquido no fundo, gás voando).
- SETA DA REAÇÃO na cor da matéria; ΔH < 0 em azul, ΔH > 0 em âmbar; Ea na pílula turquesa (Q.energia).
- CERTO E ERRADO: como O é vermelho e Cl é verde, erro e acerto NUNCA ficam só na cor: erro leva E.risco, pílula com texto
  ou E.selo(False); acerto leva E.selo(True) ou a esfera. Leitura errada = texto vermelho + risco por cima.
- PALCO ESCURO (E.palco) só para atalho e macete: fórmulas em branco (escuro=True), destaque em E.CLARO, moléculas e átomos
  mantêm as cores dos elementos. Questão com E.relogio. Texto à esquerda (XE), desenho à direita; mínimo 40 px; fórmula
  principal com 160 px ou mais.
- Convenção dita na aula 1 ("aqui, cada átomo vira uma bolinha"): vale para o curso todo; não é preciso repetir.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-001_atomos_moleculas_formulas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("atomo", "elemento", "molecula", "formula", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula, conferidas pela contagem de verdade do kit
assert Q.contar("H2O") == {"H": 2, "O": 1} and sum(Q.contar("H2O").values()) == 3
assert Q.contar("C2H6O") == {"C": 2, "H": 6, "O": 1} and 2 + 6 + 1 == 9
assert Q.contar("2 H2O") == {"H": 4, "O": 2}
assert Q.contar("CO2") == {"C": 1, "O": 2}
assert Q.contar("2 C2H6O") == {"C": 4, "H": 12, "O": 2} and (2 + 6 + 1) * 2 == 18
assert Q.contar("CH3CH2OH") == Q.contar("C2H6O") and 3 + 2 + 1 == 6
assert sum(Q.contar("Al2(SO4)3").values()) == 17 and 2 + 1 + 4 + 3 == 10
assert Q.contar("H2SO4") == {"H": 2, "S": 1, "O": 4} and 2 + 1 + 4 == 7 and 2 + 4 == 6


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
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def caixa_grupo(c, t, t0, g, cor=None, pad=12, t1=None):
    """caixa pontilhada em volta de um grupo da fórmula (símbolo + índice)"""
    if t < t0 or (t1 is not None and t >= t1):
        return
    p = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, g["x0"] - pad, g["topo"] - pad, g["x1"] - g["x0"] + 2 * pad, g["base"] - g["topo"] + 2 * pad, p, cor, prog_=p)


def cabelo(c, x, y0, y1, w, a=1.0):
    """um fio de cabelo visto de perto: faixa vertical marrom com escamas"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x, 0), skia.Point(x + w, 0)],
                                               [M.hexc("#5A3A22", a), M.hexc("#8B5E3C", a), M.hexc("#4A2E1A", a)], [0, 0.45, 1]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x, y0, x + w, y1), w * 0.1, w * 0.1), p)
    for k in range(int((y1 - y0) / 70)):
        yy = y0 + 40 + k * 70
        pth = skia.Path(); pth.moveTo(x + 6, yy); pth.quadTo(x + w / 2, yy - 26, x + w - 6, yy)
        c.drawPath(pth, M.paint("#3A2414", 0.45 * a, stroke=3))


def bateria(c, cx, cy, w, h, a=1.0):
    """bateria de carro: caixa escura com os dois polos e a etiqueta na cor da matéria"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#2A2B31", a)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h * 0.2, 22, "#3A3B42", a)
    for dx, s in ((-0.3, "−"), (0.3, "+")):
        M.rrect(c, cx + dx * w - 26, cy - h / 2 - 34, 52, 40, 8, "#9AA0A8", a)
        centro(c, s, cx + dx * w, cy - h / 2 + h * 0.15, 56, "g", BR, a)
    M.rrect(c, cx - w * 0.36, cy - h * 0.05, w * 0.72, h * 0.38, 14, E.COR, a)
    Q.formula(c, "H2SO4", cx, cy + h * 0.21, h * 0.2, BR, a, "center")


def lista(c, t, itens, x, y0, dy, size=70):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def numeros_fora(c, t, t0, pts, raio, passo=0.15, ordem=None):
    """número de contagem (1, 2, 3...) em bolinha escura, do lado de fora de cada átomo, longe do centro da molécula"""
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    ordem = ordem or list(range(len(pts)))
    for k, i in enumerate(ordem):
        P = pts[i]
        ux, uy = E._uni(mx, my, P[0], P[1]) if math.dist(P, (mx, my)) > 1 else (0, -1)
        bx, by = P[0] + ux * (raio + 46), P[1] + uy * (raio + 46)
        E.foco(c, t, t0 + k * passo, 0.3, lambda a, bx=bx, by=by, k=k: (E.bola(c, bx, by, 34, TINTA, a), centro(c, str(k + 1), bx, by + 17, 44, "g", BR, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]

    def um():
        fx, fy, fs = XE + 40, 600, 300
        Q.formula_em(c, t, a1, "H2O", fx, fy, fs, cores={"indice": E.COR} if t >= b1 else None)
        E.foco(c, t, a1 + 0.5, 0.4, lambda a: E.escreve(c, "a fórmula da água", fx + 10, fy + 150, 60, "i", TINTA2, a))
        G = Q.grupos("H2O", fx, fy, fs)
        E.foco(c, t, b1 + 0.4, 0.4, lambda a: E.pilula(c, "um número só", G[0]["x1"] + 40, fy + 250, 46, "g", fundo=E.COR, a=a))
        # a molécula: três átomos que pulam e ganham número
        pts = Q.molecula(c, t, c1, "H2O", 1400, 500, 210, tl=[c1 + 0.7, c1, c1 + 0.35])
        numeros_fora(c, t, c1 + 0.3, pts, 85, 0.35, ordem=[1, 2, 0])
        E.frase(c, t, c1 + 1.1, [("3", "g", 90, COR), ("átomos", "i", 96)], 1400, 860, "center")
        if t >= d1:
            q = ep(t, d1, 0.4)
            c.drawCircle(pts[0][0], pts[0][1], 120 + 8 * math.sin(t * 5), M.paint(E.COR, q, stroke=7))
        E.frase(c, t, d1, ps("de onde vem o", "i", 76) + [("terceiro?", "g", 70, COR)], W / 2, 1000, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 540, 300 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("átomo,", "g", 70), ("elemento,", "g", 70), ("molécula", "g", 70, COR)]),
                 (C["s02.c"], [("contar", "g", 70), ("os", "i", 74), ("átomos", "g", 70)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)
    Q.formula_em(c, t, C["s02.c"] + 1.2, "C2H6O", XE + 680, 630, 96, cores={"indice": E.COR})


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("primeira aula de", "i", 84), XE, 300, passo=0.14)
    E.frase(c, t, C["s03"] + 0.8, [("Química", "g", 170, COR)], XE, 480)
    E.frase(c, t, C["s03.a"], ps("você não precisa de nada antes", "i", 70, TINTA2), XE, 620, passo=0.1)
    E.frase(c, t, C["s03.b"] - 0.5, ps("só", "i", 80), XE, 830)
    pilula_em(c, t, C["s03.b"], "contar", XE + 300, 805, 70, E.COR)
    E.frase(c, t, C["s03.b"] + 0.5, ps("e", "i", 80), XE + 520, 830)
    pilula_em(c, t, C["s03.b"] + 0.7, "multiplicar", XE + 850, 805, 70, TINTA)
    E.foco(c, t, C["s03.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1560, 380, 170 * a, giro=-6 * math.sin(t * 0.5)), blur=0)


# ---------------- átomo ----------------
def b_atomo(c, t, C, b):
    def s04():
        tc = C["s04.c"]
        E.frase(c, t, C["s04"] + 0.2, ps("comece pelo", "i", 76, TINTA2) + ps("menor pedaço", "i", 76, TINTA2), XE, 200, passo=0.12)
        E.frase(c, t, C["s04.a"], ps("tudo é feito de", "i", 84), XE, 340, passo=0.12)
        E.frase(c, t, C["s04.b"], [("átomos", "g", 170, COR)], XE, 520)
        for i, s in enumerate(("a água", "o ar", "a sua mão")):
            ti = lerp(C["s04.b"] + 0.6, tc - 0.4, i / 2.5)
            x = XE + [0, 260, 470][i]
            E.foco(c, t, ti, 0.4, lambda a, s=s, x=x: E.pilula(c, s, x + (E.larg(s, "i", 52) + 48) / 2, 640, 52, "i", fundo=TINTA, a=a))

        # nuvem de átomos que dá a ideia de "tudo"; sai quando o fio de cabelo entra
        def nuvem():
            for k, (el, dx, dy) in enumerate((("O", 0, 0), ("H", 90, -70), ("C", -120, 80), ("N", 150, 110), ("H", -60, -130), ("O", 40, 190))):
                Q.atomo_em(c, t, C["s04.b"] + 0.15 * k, 1450 + dx, 400 + dy, 56, el)
        E.saida(c, t, tc - 0.4, nuvem)
        # o fio de cabelo: a espessura dele tem centenas de milhares de átomos lado a lado
        if t >= tc - 0.2:
            hx, hw = 1230, 400
            E.foco(c, t, tc - 0.2, 0.5, lambda a: cabelo(c, hx, 330, 830, hw, a))
            E.foco(c, t, tc, 0.4, lambda a: E.escreve(c, "um fio de cabelo, de perto", hx - 10, 300, 46, "i", TINTA2, a))
            n = 30
            for k in range(n):
                q = ease_back(prog(t, tc + 0.4 + k * 0.05, 0.3))
                if q > 0:
                    E.bola(c, hx + 14 + k * (hw - 28) / (n - 1), 580, 6.2 * q, E.COR)
            p = ep(t, tc + 1.8, 0.5)
            if p > 0:
                M.line(c, hx, 890, hx + hw, 890, TINTA, p, 4)
                for xx in (hx, hx + hw):
                    M.line(c, xx, 870, xx, 910, TINTA, p, 4)
            E.foco(c, t, tc + 2.0, 0.4, lambda a: E.pilula(c, "centenas de milhares", hx + hw / 2, 960, 46, "g", fundo=E.COR, a=a))
            E.frase(c, t, tc + 0.3, ps("na espessura de um", "i", 64) + [("fio de cabelo", "g", 60)], XE, 820, passo=0.1)
            E.frase(c, t, tc + 1.6, ps("cabem", "i", 64) + [("centenas de milhares", "g", 60, COR)], XE, 920, passo=0.1)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05"], ps("ninguém enxerga um átomo", "i", 84), W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s05"] + 1.0, ps("a olho nu", "i", 84, TINTA2), W / 2, 380, "center", 0.12)
    E.frase(c, t, C["s05.a"], ps("aqui, cada átomo vira uma", "i", 76), W / 2, 560, "center", 0.12)
    for k, el in enumerate(("H", "O", "C")):
        Q.atomo_em(c, t, C["s05.a"] + 1.0 + 0.25 * k, 760 + 200 * k, 780, 80, el)
    E.frase(c, t, C["s05.a"] + 1.8, [("bolinha", "g", 84, COR)], 1440, 805)


# ---------------- elemento ----------------
def b_elemento(c, t, C, b):
    def s06a():
        E.frase(c, t, C["s06"], ps("só num copo de água", "i", 80), XE, 230, passo=0.12)
        E.frase(c, t, C["s06.a"], [("trilhões", "g", 90, COR), ("de", "i", 90), ("trilhões", "g", 90, COR)], XE, 360, passo=0.15)
        E.frase(c, t, C["s06.a"] + 0.8, ps("de átomos", "i", 84), XE, 460, passo=0.12)
        Q.bequer(c, t, C["s06"] + 0.3, 1430, 960, 380, 430, 0.75, Q.AGUA, te=C["s06"] + 0.5, d=1.0, graduacao=False,
                 particulas=dict(n=70, estado="liquido", tipos=[("H", 0.67), ("O", 0.33)], r=11, semente=4))
        E.frase(c, t, C["s06.b"], ps("mas tipos, só", "i", 80), XE, 680, passo=0.12)
        E.foco(c, t, C["s06.b"] + 0.7, 0.4, lambda a: E.escreve(c, "2", XE + 470, 700, 150, "g", COR, a))
        for k, el in enumerate(("H", "O")):
            Q.atomo_em(c, t, C["s06.b"] + 0.9 + 0.2 * k, XE + 170 + 170 * k, 850, 64, el)
            E.foco(c, t, C["s06.b"] + 1.2 + 0.2 * k, 0.4, lambda a, k=k, el=el: centro(c, Q.NOMES[el], XE + 170 + 170 * k, 960, 40, "i", TINTA2, a))
    E.saida(c, t, C["s06.c"] - 0.1, s06a)
    if C["s06.c"] <= t < C["s07"]:
        def s06b():
            E.frase(c, t, C["s06.c"], ps("cada tipo de átomo é um", "i", 76), XE, 260, passo=0.12)
            E.frase(c, t, C["s06.c"] + 1.0, [("elemento", "g", 130, COR)], XE, 410)
            E.frase(c, t, C["s06.c"] + 1.3, [("químico", "g", 130, COR)], XE, 540)
            E.foco(c, t, C["s06.d"], 0.5, lambda a: E.escreve(c, "118", XE, 800, 210, "g", TINTA, a))
            E.frase(c, t, C["s06.d"] + 0.4, ps("elementos", "i", 70), XE + 420, 730)
            E.frase(c, t, C["s06.d"] + 0.6, ps("conhecidos", "i", 70), XE + 420, 810)
            Q.tabela(c, t, C["s06.d"] - 0.2, 1010, 330, 46, numeros=False, d=1.2)
            pilula_em(c, t, C["s06.e"], "o que diferencia os tipos: outra aula", 1420, 760, 42, TINTA2, "b")
        E.saida(c, t, C["s07"] - 0.1, s06b)
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"] - 0.4, ps("cada elemento tem um", "i", 76), XE, 200, passo=0.12)
            E.frase(c, t, C["s07.a"] + 0.4, [("símbolo", "g", 76, COR)], XE + 760, 200)
            E.frase(c, t, C["s07.a"] + 0.9, ps("de uma ou duas letras", "i", 60, TINTA2), XE, 290, passo=0.1)
            linhas = (("s07.b", "H", "hidrogênio"), ("s07.c", "O", "oxigênio"), ("s07.d", "C", "carbono"), ("s07.e", "Na", "sódio"))
            for i, (k, el, nome) in enumerate(linhas):
                y = 440 + i * 165
                Q.atomo_em(c, t, C[k], XE + 70, y - 32, 62, el)
                Q.formula_em(c, t, C[k] + 0.1, el, XE + 190, y + 10, 110)
                E.frase(c, t, C[k] + 0.3, [(nome, "i", 76)], XE + 420, y)
            pilula_em(c, t, C["s07.e"] + 0.9, "do latim natrium", 1320, 905, 50, E.COR)
        E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return

    # s08: a regra das letras, Co × CO
    E.frase(c, t, C["s08"], ps("a regra das letras", "i", 76), XE, 180, passo=0.12)
    E.frase(c, t, C["s08.a"], [("1ª", "g", 64, COR), ("maiúscula,", "i", 70), ("2ª", "g", 64, COR), ("minúscula", "i", 70)], XE, 280, passo=0.15)
    def exemplos():
        for i, el in enumerate(("Na", "Cl", "Ca")):
            x = XE + 60 + i * 420
            E.foco(c, t, C["s08.a"] + 0.6 + 0.3 * i, 0.4, lambda a, x=x, el=el: (
                E.escreve(c, el[0], x, 640, 220, "g", COR, a),
                E.escreve(c, el[1], x + E.larg(el[0], "g", 220) + 6, 640, 220, "g", TINTA, a),
                centro(c, Q.NOMES[el], x + 110, 740, 50, "i", TINTA2, a)))
    if t < C["s08.b"]:
        E.saida(c, t, C["s08.b"] - 0.1, exemplos)
    x1, x2, w, y, h = 170, 1000, 750, 350, 540
    for x, k in ((x1, "s08.b"), (x2, "s08.c")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    # Co: um elemento só
    Q.formula_em(c, t, C["s08.b"] + 0.2, "Co", x1 + 60, y + 250, 200, cores={"Co": COR})
    Q.atomo_em(c, t, C["s08.b"] + 0.6, x1 + 560, y + 180, 95, "Co")
    E.frase(c, t, C["s08.b"] + 0.9, [("1", "g", 64, COR), ("elemento:", "i", 66), ("cobalto", "g", 62)], x1 + 60, y + 420, passo=0.12)
    # CO: dois elementos, o monóxido de carbono
    Q.formula_em(c, t, C["s08.c"] + 0.2, "CO", x2 + 60, y + 250, 200)
    Q.molecula(c, t, C["s08.c"] + 0.6, "CO", x2 + 560, y + 180, 150, passo=0.25)
    E.frase(c, t, C["s08.c"] + 0.9, [("2", "g", 64, COR), ("elementos:", "i", 66), ("C", "g", 62), ("e", "i", 66), ("O", "g", 62)], x2 + 60, y + 400, passo=0.12)
    E.foco(c, t, lerp(C["s08.c"], C["s08.d"], 0.6), 0.4, lambda a: E.pilula(c, "monóxido de carbono: gás tóxico", x2 + w / 2, y + 490, 38, "b", fundo=TINTA, a=a))
    if t >= C["s08.d"]:
        for g in Q.grupos("CO", x2 + 60, y + 250, 200):
            caixa_grupo(c, t, C["s08.d"] + 0.2 * g["i"], g, E.COR, 10)
        g = Q.grupos("Co", x1 + 60, y + 250, 200)[0]
        caixa_grupo(c, t, C["s08.d"], g, E.COR, 10)
        E.frase(c, t, C["s08.d"] + 0.4, ps("cada", "i", 64) + [("maiúscula", "g", 60, COR)] + ps("começa um elemento novo", "i", 64), W / 2, 990, "center", 0.1)


# ---------------- molécula ----------------
def b_molecula(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"] + 0.2, ps("os átomos se prendem", "i", 76), XE, 220, passo=0.12)
        E.frase(c, t, C["s09.a"], ps("um grupo de átomos presos:", "i", 70), XE, 360, passo=0.1)
        E.frase(c, t, C["s09.a"] + 1.4, [("molécula", "g", 140, COR)], XE, 520)
        E.frase(c, t, C["s09.b"], [("a", "i", 76), ("água", "g", 76)], XE, 700)
        E.frase(c, t, C["s09.c"], [("2", "g", 64, COR), ("hidrogênios", "i", 68)], XE, 800, passo=0.12)
        E.frase(c, t, C["s09.d"], [("+", "g", 64, TINTA2), ("1", "g", 64, COR), ("oxigênio", "i", 68)], XE, 890, passo=0.12)
        junta = 1 - ease_io(prog(t, C["s09"] + 1.4, 1.8))
        pts = Q.molecula(c, t, C["s09"] + 0.3, "H2O", 1400, 520, 230, passo=0.2, separa=junta)
        for i, (k, P) in enumerate((("s09.c", pts[1]), ("s09.c", pts[2]), ("s09.d", pts[0]))):
            q = ep(t, C[k] + 0.2 * (i % 2), 0.3) * (1 - ep(t, C["s09.e"], 0.4))
            if q > 0:
                c.drawCircle(P[0], P[1], (62 if i < 2 else 104), M.paint(E.COR, q, stroke=7))
        Q.formula_em(c, t, C["s09.d"] + 0.8, "H2O", 1400, 840, 120, align="center")
        pilula_em(c, t, C["s09.e"], "como se prendem: outra aula, a de ligações", 1400, 980, 38, TINTA2, "b")
    E.saida(c, t, C["s10"] - 0.1, s09)
    if C["s10"] <= t < C["s11"]:
        def s10():
            E.frase(c, t, C["s10.a"], ps("a menor parte da", "i", 76) + [("água", "g", 76, COR)], XE, 230, passo=0.12)
            E.frase(c, t, C["s10.a"] + 1.2, ps("que ainda é", "i", 76) + [("água", "g", 76, COR)], XE, 330, passo=0.12)
            sep = ease_io(prog(t, C["s10.b"], 1.2))
            Q.molecula(c, t, C["s10"], "H2O", W / 2, 620, 200, passo=0.0, separa=sep)
            if sep > 0.5:
                E.frase(c, t, C["s10.b"] + 1.0, ps("hidrogênio e oxigênio,", "i", 68), W / 2, 920, "center", 0.1)
                E.frase(c, t, C["s10.b"] + 1.8, [("não", "g", 64, ERRADO), ("água", "g", 64)], W / 2, 1010, "center")
                if t >= C["s10.b"] + 2.4:
                    E.risco(c, W / 2 - 30, 1025, W / 2 + 150, 960, t, C["s10.b"] + 2.4, largura=9)
        E.saida(c, t, C["s11"] - 0.1, s10)
    if C["s11"] <= t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11"], ps("pense na escrita", "i", 70, TINTA2), XE, 180, passo=0.12)
            defs = (("s11.a", "átomo", "cada letra escrita"), ("s11.b", "elemento", "o tipo de letra"), ("s11.c", "molécula", "a palavra"))
            for i, (k, a_, b_) in enumerate(defs):
                y = 290 + i * 105
                E.frase(c, t, C[k], [(a_, "g", 66, COR), ("=", "g", 66, TINTA2)], XE, y, passo=0.12)
                E.frase(c, t, C[k] + 0.3, [(b_, "i", 72)], XE + 430, y)
            # ARARA: 5 letras, 2 tipos
            tw, gap, y0 = 200, 26, 580
            x0 = W / 2 - (5 * tw + 4 * gap) / 2
            tipos = ep(t, C["s11.e"], 0.5)
            for i, ch in enumerate("ARARA"):
                ti = C["s11"] + 0.8 + 0.15 * i
                q = ease_back(prog(t, ti, 0.45))
                if q <= 0:
                    continue
                cx = x0 + i * (tw + gap) + tw / 2
                fundo = M.mix(TINTA, E.COR if ch == "A" else "#6E6E76", tipos)
                hh = 230 * q
                M.rrect(c, cx - tw / 2, y0 + 115 - hh / 2, tw, hh, 26, fundo, 1, shadow=True)
                centro(c, ch, cx, y0 + 115 + 62 * q, 180 * q, "g", BR, 1)
                E.foco(c, t, C["s11.d"] + 0.15 * i, 0.3, lambda a, i=i, cx=cx: centro(c, str(i + 1), cx, y0 + 300, 46, "b", TINTA2, a))
            E.frase(c, t, C["s11.d"] + 1.2, [("5", "g", 60, TINTA), ("letras", "i", 64)], x0, 1000, passo=0.12)
            E.frase(c, t, C["s11.e"], [("só", "i", 64), ("2", "g", 60, COR), ("tipos:", "i", 64)], W / 2 + 120, 1000, passo=0.12)
            E.foco(c, t, C["s11.e"] + 0.6, 0.4, lambda a: (E.pilula(c, "A", W / 2 + 560, 980, 50, "g", fundo=E.COR, a=a),
                                                          E.pilula(c, "R", W / 2 + 660, 980, 50, "g", fundo="#6E6E76", a=a)))
        E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    # s12: na água é igual
    E.frase(c, t, C["s12"], ps("na água é igual", "i", 76), XE, 200, passo=0.12)
    pts = Q.molecula(c, t, C["s12"], "H2O", 600, 600, 220, passo=0.0)
    if t >= C["s12.a"]:
        numeros_fora(c, t, C["s12.a"], pts, 85, 0.15, ordem=[1, 0, 2])
    if t >= C["s12.c"]:
        q = ep(t, C["s12.c"], 0.5)
        E.caixa_pontilhada(c, 250, 330, 700, 560, q, E.COR, prog_=q)
    for i, (k, n, s) in enumerate((("s12.a", "3", "átomos"), ("s12.b", "2", "elementos"), ("s12.c", "1", "molécula"))):
        y = 430 + i * 190
        E.foco(c, t, C[k], 0.5, lambda a, n=n, y=y: E.escreve(c, n, 1100, y + 30, 170, "g", COR, a))
        E.frase(c, t, C[k] + 0.2, [(s, "i", 96)], 1260, y)
    if t >= C["s12.b"]:
        for k, el in enumerate(("H", "O")):
            Q.atomo_em(c, t, C["s12.b"] + 0.3 + 0.15 * k, 1690 + 80 * k, 590, 32, el)


# ---------------- fórmula ----------------
FX, FY, FS = W / 2, 430, 260


def b_formula(c, t, C, b):
    if t < C["s15"]:
        cores = None
        if C["s13.c"] <= t < C["s14"]:
            cores = {"indice": E.COR}
        elif t >= C["s14.a"]:
            cores = {"H": E.COR}
        if t < C["s14.c"]:
            Q.formula_em(c, t, C["s13.a"], "H2O", FX, FY, FS, align="center", cores=cores)
            G = Q.grupos("H2O", FX, FY, FS, "center")
        else:
            G = Q.formula_um(c, t, C["s13.a"], "H2O", C["s14.c"], FX, FY, FS, align="center", cores=cores)

        def s13():
            E.frase(c, t, C["s13.a"], ps("a fórmula escreve a substância", "i", 70), W / 2, 150, "center", 0.1)
            for g in G:
                caixa_grupo(c, t, C["s13.b"] + 0.2 * g["i"], g, None, 14)
            E.frase(c, t, C["s13.b"] + 0.5, [("símbolos", "g", 64), ("=", "g", 64, TINTA2)] + ps("quais elementos", "i", 68), XE, 720, "left", 0.12)
            gx, gy = G[0]["x1"] - 30, FY + 95
            p = ep(t, C["s13.c"], 0.5)
            if p > 0:
                M.arrow(c, 1290, 790, gx + 12, gy + 20, E.COR, p, 6, 22, ease_io(prog(t, C["s13.c"], 0.5)))
            E.foco(c, t, C["s13.c"] + 0.3, 0.4, lambda a: E.pilula(c, "índice", 1400, 820, 58, "g", fundo=E.COR, a=a))
            E.frase(c, t, C["s13.c"] + 1.4, ps("quantos átomos daquele elemento", "i", 64), W / 2, 1000, "center", 0.1)
        E.saida(c, t, C["s14"] - 0.1, s13)
        if t < C["s14"]:
            return
        # s14: H₂ = 2 hidrogênios; O sem número = 1
        gH, gO = G[0], G[1]
        caixa_grupo(c, t, C["s14.a"], gH, E.COR, 14)
        for k in range(2):
            Q.atomo_em(c, t, C["s14.a"] + 0.6 + 0.25 * k, XE + 60 + 120 * k, 700, 50, "H")
        E.frase(c, t, C["s14.a"] + 0.9, [("2", "g", 66, COR), ("hidrogênios", "i", 70)], XE + 320, 722, passo=0.12)
        caixa_grupo(c, t, C["s14.b"], gO, TINTA2, 14)
        if C["s14.b"] <= t < C["s14.c"]:
            E.foco(c, t, C["s14.b"] + 0.3, 0.4, lambda a: centro(c, "?", gO["x1"] + 70, FY + 60, 110, "g", CINZA, a))
        Q.atomo_em(c, t, C["s14.c"] + 0.4, XE + 60, 850, 58, "O")
        E.frase(c, t, C["s14.c"] + 0.6, ps("sem número:", "i", 70) + [("1", "g", 66, COR), ("oxigênio", "i", 70)], XE + 320, 872, passo=0.12)
        E.formula_em(c, t, C["s14.d"], "2 + 1 =", 1420, 1000, 76, "g", TINTA2, "right")
        bola_txt(c, t, C["s14.d"] + 0.4, "3", 1510, 975, 62, 70)
        E.frase(c, t, C["s14.d"] + 0.6, [("átomos", "i", 76)], 1590, 1000)
        return

    # s15: o álcool, C₂H₆O
    fx, fy, fs = XE, 330, 200
    cores = {"C": E.COR} if C["s15.b"] <= t < C["s15.c"] else {"H": E.COR} if C["s15.c"] <= t < C["s15.d"] else {"O": E.COR} if C["s15.d"] <= t < C["s15.e"] else None
    E.frase(c, t, C["s15"], ps("o álcool comum", "i", 70, TINTA2), XE, 150, passo=0.12)
    Q.formula_um(c, t, C["s15.a"], "C2H6O", C["s15.d"], fx, fy, fs, cores=cores)
    Q.inventario(c, t, C["s15.b"], [("C", 2), ("H", 6), ("O", 1)], XE + 10, 540, 66, tl=[C["s15.b"], C["s15.c"], C["s15.d"]], total=C["s15.f"])
    pilula_em(c, t, C["s15.e"], "3 elementos", XE + 720, 640, 54, E.COR)
    Q.molecula(c, t, C["s15.a"] + 0.4, "C2H6O", 1500, 600, 140, passo=0.12)
    E.foco(c, t, C["s15.a"] + 1.6, 0.4, lambda a: centro(c, "etanol, o álcool comum", 1500, 900, 46, "i", TINTA2, a))


# ---------------- coeficiente ----------------
def b_coeficiente(c, t, C, b):
    E.frase(c, t, C["s16"] + 0.2, ps("um número na", "i", 76) + [("frente", "g", 76, COR)], XE, 190, passo=0.12)
    Q.formula_em(c, t, C["s16.a"], "2 H2O", W / 2, 400, 200, align="center", cores={"coef": E.COR})
    G = Q.grupos("2 H2O", W / 2, 400, 200, "center")
    p = ep(t, C["s16.b"], 0.5)
    if p > 0:
        gc = G[0]
        M.arrow(c, gc["cx"] - 170, 470, gc["cx"] - 40, 380, E.COR, p, 6, 22, ease_io(prog(t, C["s16.b"], 0.5)))
    E.foco(c, t, C["s16.b"] + 0.3, 0.4, lambda a: E.pilula(c, "coeficiente", G[0]["cx"] - 330, 500, 54, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s16.b"] + 1.2, ps("conta moléculas inteiras", "i", 60, TINTA2), W / 2 + 120, 530, "left", 0.1)
    # duas moléculas de água
    m1 = Q.molecula(c, t, C["s16.c"], "H2O", 640, 760, 150, passo=0.12)
    m2 = Q.molecula(c, t, C["s16.c"] + 0.5, "H2O", 1060, 760, 150, passo=0.12)
    for k, mm in enumerate((m1, m2)):
        E.foco(c, t, C["s16.c"] + 0.3 + 0.5 * k, 0.4, lambda a, mm=mm, k=k: E.pilula(c, f"molécula {k + 1}", mm[0][0], 620, 40, "b", fundo=TINTA, a=a))
    for i, P in enumerate((m1[1], m1[2], m2[1], m2[2])):
        q = ep(t, C["s16.d"] + 0.2 * i, 0.3)
        if q > 0:
            c.drawCircle(P[0], P[1], 46, M.paint(E.COR, q, stroke=6))
    for i, P in enumerate((m1[0], m2[0])):
        q = ep(t, C["s16.e"] + 0.2 * i, 0.3)
        if q > 0:
            c.drawCircle(P[0], P[1], 58, M.paint(TINTA, q, stroke=6))
    E.foco(c, t, C["s16.d"], 0.5, lambda a: (E.escreve(c, "4", 1400, 760, 120, "g", COR, a), E.escreve(c, "hidrogênios", 1490, 750, 64, "i", TINTA, a)))
    E.foco(c, t, C["s16.e"], 0.5, lambda a: (E.escreve(c, "2", 1400, 900, 120, "g", COR, a), E.escreve(c, "oxigênios", 1490, 890, 64, "i", TINTA, a)))


# ---------------- erro ----------------
EX, EY, ES = 560, 470, 230


def b_erro(c, t, C, b):
    E.frase(c, t, C["s17"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s17.a"], ps("o índice vale para tudo?", "i", 70), XE + 450, 190, passo=0.12)
    cores = {"indice": E.COR} if t >= C["s18.a"] else None
    if t < C["s18.c"]:
        Q.formula_em(c, t, C["s17.a"] + 0.8, "CO2", EX, EY, ES, cores=cores)
        G = Q.grupos("CO2", EX, EY, ES)
    else:
        G = Q.formula_um(c, t, C["s17.a"] + 0.8, "CO2", C["s18.c"], EX, EY, ES, cores=cores)
    gC, gO = G[0], G[1]
    E.frase(c, t, C["s17.b"] + 0.4, ps("gás carbônico", "i", 60, TINTA2), EX, EY + 160, passo=0.12)

    def errado():
        # a leitura errada: o 2 espalhado pela fórmula toda
        p = ep(t, C["s17.c"], 0.5)
        if p > 0:
            E.chave(c, gC["x0"], gO["x1"], gC["topo"] - 30, ERRADO, p, -26)
        E.frase(c, t, C["s17.c"], [("2", "g", 76, ERRADO), ("carbonos", "i", 80, ERRADO)], 1300, 400, passo=0.12)
        E.frase(c, t, C["s17.c"] + 0.8, [("2", "g", 76, ERRADO), ("oxigênios", "i", 80, ERRADO)], 1300, 520, passo=0.12)
        if t >= C["s17.c"] + 1.8:
            E.risco(c, 1280, 560, 1760, 340, t, C["s17.c"] + 1.8, largura=12)
    E.saida(c, t, C["s18.a"] - 0.1, errado)
    if t < C["s18.a"]:
        return
    # o certo: o 2 é só do O
    p = ep(t, C["s18.a"], 0.5)
    sub_x = gO["x1"] - 30
    if p > 0:
        M.arrow(c, sub_x + 50, EY + 150, sub_x + 4, EY + 70, E.COR, p, 6, 22, ease_io(prog(t, C["s18.a"], 0.5)))
    E.frase(c, t, C["s18.a"] + 0.4, ps("só vale para o símbolo de antes", "i", 56, TINTA2), EX, EY + 250, passo=0.1)
    caixa_grupo(c, t, C["s18.b"], gO, E.COR, 12)
    E.foco(c, t, C["s18.b"], 0.5, lambda a: (E.escreve(c, "2", 1300, 420, 100, "g", COR, a), E.escreve(c, "oxigênios", 1380, 410, 70, "i", TINTA, a)))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: (E.escreve(c, "1", 1300, 540, 100, "g", COR, a), E.escreve(c, "carbono", 1380, 530, 70, "i", TINTA, a)))
    Q.molecula(c, t, C["s18.d"], "CO2", 800, 900, 130, passo=0.15)
    E.foco(c, t, C["s18.d"] + 0.6, 0.5, lambda a: (E.escreve(c, "= 3", 1300, 660, 100, "g", TINTA, a), E.escreve(c, "átomos", 1520, 650, 70, "i", TINTA, a)))
    E.foco(c, t, C["s18.d"] + 1.0, 0.5, lambda a: E.selo(c, 1810, 630, 56, True, a))
    # o que vale para a fórmula toda é o coeficiente
    E.frase(c, t, C["s18.e"], ps("para a fórmula toda:", "i", 58, TINTA2), 1300, 840, passo=0.1)
    Q.formula_em(c, t, C["s18.e"] + 0.5, "2 CO2", 1300, 980, 100, cores={"coef": E.COR})
    E.foco(c, t, C["s18.e"] + 0.9, 0.4, lambda a: E.pilula(c, "coeficiente", 1700, 950, 44, "g", fundo=E.COR, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s20"]:
        def s19():
            E.frase(c, t, C["s19"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s19.a"], [("1", "g", 66, CLARO), ("some", "g", 70, BR), ("os", "i", 74, CLARO), ("índices", "g", 70, BR)], XE, 300, passo=0.12)
            E.frase(c, t, C["s19.a"] + 1.4, ps("(sem número = 1)", "i", 56, CLARO), XE + 720, 300, passo=0.1)
            E.frase(c, t, C["s19.b"], [("2", "g", 66, CLARO), ("vezes", "i", 74, CLARO), ("o", "i", 74, CLARO), ("coeficiente", "g", 70, BR)], XE, 410, passo=0.12)
            cores = {"indice": E.CLARO} if t >= C["s19.d"] - 0.8 else None
            if t >= C["s19.e"]:
                cores = {"coef": E.CLARO}
            Q.formula_um(c, t, C["s19.c"], "2 C2H6O", C["s19.d"] - 0.8, W / 2, 640, 190, align="center", cores=cores, escuro=True)
            E.formula_em(c, t, C["s19.d"] - 0.6, "2 + 6 + 1 =", W / 2 - 40, 880, 90, "g", BR, "right")
            E.foco(c, t, C["s19.d"], 0.5, lambda a: E.escreve(c, "9", W / 2 + 10, 880, 90, "g", CLARO, a))
            E.formula_em(c, t, C["s19.e"], "× 2 =", W / 2 + 110, 880, 90, "g", BR)
            wv = E.formula(None, "× 2 =", 0, 0, 90, a=0)
            bola_txt(c, t, C["s19.e"] + 0.6, "18", W / 2 + 110 + wv + 110, 850, 90, 84)
        E.saida(c, t, C["s20"] - 0.1, s19)
        return
    if t < C["s21"]:
        def s20():
            E.frase(c, t, C["s20.a"], ps("cada índice conta", "i", 70, CLARO) + [("um elemento", "g", 66, BR)], W / 2, 190, "center", 0.12)
            E.frase(c, t, C["s20.a"] + 1.6, ps("o coeficiente repete a molécula", "i", 64, CLARO), W / 2, 290, "center", 0.1)

            def porque():
                Q.formula_em(c, t, C["s20.a"] + 0.6, "C2H6O", W / 2, 560, 150, align="center", cores={"indice": E.CLARO}, escuro=True)
                for i, (n, el, x) in enumerate(((2, "C", -330), (6, "H", 0), (1, "O", 330))):
                    E.foco(c, t, C["s20.a"] + 1.2 + 0.3 * i, 0.4, lambda a, n=n, el=el, x=x: (
                        Q.atomo(c, W / 2 + x - 70, 740, 40, el, a, escuro=True),
                        E.escreve(c, f"× {n}", W / 2 + x - 10, 762, 64, "g", BR, a)))
            E.saida(c, t, C["s20.b"] - 0.1, porque)
            E.frase(c, t, C["s20.b"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("pediu cada elemento?", "i", 66, CLARO), W / 2, 450, "center", 0.12)
            E.frase(c, t, C["s20.b"] + 1.6, ps("leia", "i", 66, CLARO) + [("símbolo por símbolo", "g", 62, BR)], W / 2, 545, "center", 0.12)
            s = "CH3CH2OH"
            Q.formula_em(c, t, C["s20.c"] - 0.4, s, W / 2, 760, 150, align="center", cores={"H": E.CLARO} if t >= C["s20.c"] else None, escuro=True)
            E.formula_em(c, t, C["s20.c"] + 0.8, "H: 3 + 2 + 1 = 6", W / 2, 930, 80, "g", CLARO, "center")
            E.foco(c, t, C["s20.c"] + 1.4, 0.4, lambda a: E.pilula(c, "o mesmo álcool", 1560, 690, 40, "b", fundo=E.COR, a=a))
        E.saida(c, t, C["s21"] - 0.1, s20)
        return
    E.frase(c, t, C["s21.a"], ps("e se tiver", "i", 70, CLARO) + [("parênteses?", "g", 66, BR)], W / 2, 300, "center", 0.12)
    Q.formula_em(c, t, C["s21.a"] + 0.8, "Al2(SO4)3", W / 2, 600, 170, align="center", escuro=True)
    G = Q.grupos("Al2(SO4)3", W / 2, 600, 170, "center")
    par = [g for g in G if g["tipo"] == "par"]
    if par:
        caixa_grupo(c, t, C["s21.a"] + 1.4, dict(par[0], x1=G[-1]["x1"] + 70), E.CLARO, 14)
    E.frase(c, t, C["s21.a"] + 1.8, ps("a soma direta", "i", 66, CLARO) + [("pode errar", "g", 62, ERRADO)], W / 2, 820, "center", 0.12)
    pilula_em(c, t, C["s21.a"] + 2.6, "fica para outra aula", W / 2, 930, 46, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s22"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s22"] + 1.0, ps("o ácido da bateria de carro", "i", 66, TINTA2), XE, 290, passo=0.1)
    Q.formula_em(c, t, C["s22.a"], "H2SO4", XE, 470, 170)
    E.foco(c, t, C["s22.b"], 0.4, lambda a: Q.atomo(c, XE + 40, 560, 34, "S", a))
    E.frase(c, t, C["s22.b"] + 0.1, [("S", "g", 56), ("=", "g", 56, TINTA2), ("enxofre", "i", 62)], XE + 100, 580, passo=0.12)
    E.frase(c, t, C["s22.c"], [("1", "g", 56, COR)] + ps("quantos átomos de cada elemento?", "i", 60), XE, 720, passo=0.08)
    E.frase(c, t, C["s22.d"], [("2", "g", 56, COR)] + ps("quantos elementos?", "i", 60), XE, 820, passo=0.08)
    E.frase(c, t, C["s22.e"], [("3", "g", 56, COR)] + ps("quantos átomos no total?", "i", 60), XE, 920, passo=0.08)
    if t < C["s23"]:
        E.foco(c, t, C["s22"] + 1.2, 0.6, lambda a: bateria(c, 1460, 520, 520, 360, a))
    else:
        E.relogio(c, t, C["s23.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    fx, fy, fs = XE, 260, 170
    cores = {"H": E.COR} if C["s24.a"] <= t < C["s24.b"] else {"S": E.COR} if C["s24.b"] <= t < C["s24.c"] else {"O": E.COR} if C["s24.c"] <= t < C["s24.d"] else None
    Q.formula_um(c, t, C["s24"], "H2SO4", C["s24.b"] + 0.2, fx, fy, fs, cores=cores)
    Q.inventario(c, t, C["s24.a"], [("H", 2), ("S", 1), ("O", 4)], XE + 10, 460, 64, tl=[C["s24.a"], C["s24.b"], C["s24.c"]],
                 total=C["s25.b"] - 0.2)
    pilula_em(c, t, C["s24.d"], "3 elementos", XE + 700, 560, 54, E.COR)
    Q.molecula(c, t, C["s24"] + 0.4, "H2SO4", 1430, 470, 150, passo=0.1)
    E.formula_em(c, t, C["s25.a"], "2 + 1 + 4 =", 1280, 880, 84, "g", TINTA2, "right")
    bola_txt(c, t, C["s25.b"], "7", 1380, 852, 70, 84, CERTO)
    E.foco(c, t, C["s25.b"] + 0.3, 0.4, lambda a: E.escreve(c, "átomos", 1470, 880, 70, "i", TINTA, a))

    def erro():
        E.foco(c, t, C["s25.c"], 0.5, lambda a: (E.formula(c, "2 + 4 = 6", 1280, 1010, 64, "g", ERRADO, a, "right"),
                                                 E.escreve(c, "esqueceu o 1 do S", 1320, 1005, 50, "i", ERRADO, a)))
        if t >= C["s25.c"] + 0.7:
            E.risco(c, 990, 1025, 1290, 965, t, C["s25.c"] + 0.7, largura=9)
    if t >= C["s25.c"]:
        E.saida(c, t, C["s25.d"] - 0.1, erro)
    E.frase(c, t, C["s25.d"], [("7", "g", 60, COR), ("átomos,", "i", 64), ("3", "g", 60, COR), ("elementos,", "i", 64), ("1", "g", 60, COR), ("molécula", "i", 64)],
            1280, 1010, "center", 0.12)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s26"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s26.a", [("átomo", "g", 70), ("=", "g", 70, TINTA2), ("a", "i", 74), ("partícula", "i", 74)]),
                 ("s26.b", [("elemento", "g", 70), ("=", "g", 70, TINTA2), ("o", "i", 74), ("tipo", "i", 74), ("de", "i", 74), ("átomo", "i", 74)]),
                 ("s26.c", [("molécula", "g", 70), ("=", "g", 70, TINTA2), ("átomos", "i", 74), ("presos", "i", 74)]),
                 ("s26.d", [("índice", "g", 70), ("=", "g", 70, TINTA2), ("conta", "i", 74), ("o", "i", 74), ("símbolo", "i", 74), ("de", "i", 74), ("antes", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
        Q.formula_em(c, t, C["s26.d"] + 0.8, "H2O", 1560, 900, 150, cores={"indice": E.COR})
    E.saida(c, t, C["s27"] - 0.1, resumo)
    if t < C["s27"]:
        return
    E.frase(c, t, C["s27"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s27.a"], [("Substância", "g", 110, COR), ("pura", "g", 110, COR)], XE, 390)
    E.frase(c, t, C["s27.a"] + 0.5, [("ou", "i", 110), ("mistura", "g", 110, COR)], XE, 520)
    Q.molecula(c, t, C["s27.b"], "O2", 450, 740, 120, passo=0.2)
    Q.molecula(c, t, C["s27.b"] + 0.5, "O3", 900, 750, 120, passo=0.2)
    Q.formula_em(c, t, C["s27.b"] + 0.3, "O2", 450, 920, 90, align="center")
    Q.formula_em(c, t, C["s27.b"] + 0.8, "O3", 900, 920, 90, align="center")
    E.foco(c, t, C["s27.b"] + 1.2, 0.4, lambda a: centro(c, "≠", 675, 770, 120, "g", TINTA2, a))
    E.foco(c, t, C["s27.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s27.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s27.c"] + 0.2, 0.4))
    E.frase(c, t, C["s27.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, atomo=b_atomo, elemento=b_elemento, molecula=b_molecula, formula=b_formula,
              coeficiente=b_coeficiente, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
