"""Visual — Estudativo · QUI-INO-008: balancear por tentativas. Primeira aula do módulo "Reações e balanceamento".
Linguagem visual: a da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-INO-007). Acréscimo do módulo (QUI-INO-008 a 012):
- BALANCEAMENTO = a equação no alto, com o coeficiente da vez na cor da matéria, e o PLACAR embaixo (placar): uma linha por
  elemento, átomos à esquerda e à direita, conferidos de verdade com Q.lados; igual = selo verde, diferente = número em vermelho.
- A ordem MACHO aparece como cinco fichas (macho); a ficha da vez acende.
- Mudar o índice é o erro: a fórmula errada sai em vermelho com risco."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Ácidos, bases e reações")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-INO-008_balancear_por_tentativas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ('regra', 'propano', 'atalho', 'questao', 'fim'))
BR = "#FFFFFF"
ACIDO, BASE, NEUTRO = "#E8602C", "#4B3FB5", TINTA2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns da trilha (as mesmas da QUI-INO-007; candidatas ao kit) ----------------
def clampf(v):
    return max(0.0, min(1.0, v))


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE if cor is None else BR, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, size=70):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, y=y, i=i: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def promessa(c, t, t0, itens, x=XE, y0=460, dy=170):
    """a promessa do gancho: 'até o fim da aula' + lista + hexágono da Química"""
    tb = t0 + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 540, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, t0, ps("até o fim da aula", "i", 88), x, 280, passo=0.14)
    lista(c, t, itens, x, y0, dy)


def lado(c, t, t0, x0, x1, y, rot, cor, sub=None, size=54):
    """chave embaixo de um trecho da equação, com o nome"""
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.chave(c, x0, x1, y, cor, p, 26)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rot, (x0 + x1) / 2, y + 90, size, "g", cor, a))
    if sub:
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: centro(c, sub, (x0 + x1) / 2, y + 150, 44, "i", TINTA2, a))


def selo_carga(c, cx, cy, r, carga, a=1.0):
    pos = "+" in carga
    E.bola(c, cx, cy, r, "#F2A516" if pos else Q.ELETRON, a)
    centro(c, carga.replace("-", "−"), cx, cy + r * 0.42, r * 1.15, "g", BR, a)


def ion(c, cx, cy, r, s, carga, a=1.0, escuro=False, cor=None):
    """íon: bolinha do elemento (ou esfera de grupo com a fórmula dentro) e a carga num selo no alto à direita"""
    if a <= 0 or r <= 0:
        return
    if s in Q.NOMES and cor is None:
        Q.atomo(c, cx, cy, r, s, a, escuro=escuro)
    else:
        E.bola(c, cx, cy, r, cor or "#6E6E76", a)
        sz = r * (0.95 if len(s) <= 2 else 0.75 if len(s) <= 3 else 0.6)
        Q.formula(c, s, cx, cy + sz * 0.36, sz, BR, a, "center")
    selo_carga(c, cx + r * 0.8, cy - r * 0.8, max(18, r * 0.38), carga, a)


def ion_em(c, t, t0, cx, cy, r, s, carga, cor=None, escuro=False):
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        ion(c, cx, cy, r * k, s, carga, min(1.0, prog(t, t0, 0.25)), escuro, cor)


def frasco_fechado(c, t, t0, cx, yb, w=220, h=260, particulas=None, cor=None):
    """erlenmeyer com rolha: o sistema fechado"""
    Q.erlenmeyer(c, t, t0, cx, yb, w, h, 0.0 if not cor else 0.3, cor or Q.AGUA, particulas=particulas)
    q = ep(t, t0 + 0.2, 0.4)
    if q > 0:
        M.rrect(c, cx - w * 0.16, yb - h - 34, w * 0.32, 52, 10, "#8B5E3C", q)


def caixa(c, t, t0, x, y, w, h, cor=None, t1=None):
    """caixa pontilhada que se desenha em volta de um trecho"""
    if t < t0 or (t1 is not None and t >= t1):
        return
    p = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)


def questao(c, t, C, sq, linhas, sp, desenho=None, titulo="hora de testar"):
    """tela da questão: texto à esquerda (linhas = [(instante, partes, y)]), desenho à direita até a pausa, e o relógio"""
    E.frase(c, t, C[sq], ps(titulo, "i", 72, COR), XE, 180)
    for ti, partes, y in linhas:
        E.frase(c, t, ti, partes, XE, y, passo=0.08)
    if t < C[sp]:
        if desenho:
            desenho()
    else:
        E.relogio(c, t, C[sp + ".a"], cx=1500, cy=470, r=200)


def fim(c, t, C, sr, itens, sp, l1, l2, k_insc, k_bons, desenho=None, dy=180):
    """fechamento: resumo numerado, depois a próxima aula, inscreva-se e bons estudos"""
    def resumo():
        E.frase(c, t, C[sr], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * dy
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C[sp] - 0.1, resumo)
    if t < C[sp]:
        return
    E.frase(c, t, C[sp], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[sp] + 0.6, [(l1, "g", 110, COR)], XE, 400)
    if l2:
        E.frase(c, t, C[sp] + 1.0, [(l2, "g", 110, COR)], XE, 530)
    if desenho:
        desenho()
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


def palco_titulo(c, t, t0, txt):
    E.frase(c, t, t0, ps(txt, "i", 72, CLARO), W / 2, 150, "center", 0.12)


# ======================== desta aula ========================
PROP = ["C3H8 + O2 -> CO2 + H2O", "C3H8 + O2 -> 3 CO2 + H2O", "C3H8 + O2 -> 3 CO2 + 4 H2O", "C3H8 + 5 O2 -> 3 CO2 + 4 H2O"]
MG = ["Mg + HCl -> MgCl2 + H2", "Mg + 2 HCl -> MgCl2 + H2"]
AL = ["Al + O2 -> Al2O3", "Al + O2 -> 2 Al2O3", "Al + 3 O2 -> 2 Al2O3", "4 Al + 3 O2 -> 2 Al2O3"]
ETA = ["C2H6O + O2 -> CO2 + H2O", "C2H6O + O2 -> 2 CO2 + H2O", "C2H6O + O2 -> 2 CO2 + 3 H2O", "C2H6O + 3 O2 -> 2 CO2 + 3 H2O"]
for fim_ in (PROP[-1], MG[-1], AL[-1], ETA[-1]):
    assert Q.lados(fim_)[0] == Q.lados(fim_)[1], fim_
assert 3 * 2 + 4 * 1 == 10 == 5 * 2 and 4 * 2 == 8 and 2 * 2 + 3 == 7 and 7 - 1 == 6 == 3 * 2 and 1 + 3 + 2 + 3 == 9


def estagio(t, lista, tempos):
    """a equação da vez: lista[k] a partir de tempos[k-1]"""
    k = sum(1 for x in tempos if t >= x)
    return lista[min(k, len(lista) - 1)]


def placar(c, t, t0, eq, x, y, els, size=60, escuro=False, dy=None):
    """placar do balanceamento: elemento | esquerda | direita, conferido com Q.lados"""
    esq, dir_ = Q.lados(eq)
    dy = dy or size * 1.5
    tinta = BR if escuro else TINTA
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    E.escreve(c, "esquerda", x + 150, y - size * 1.1, size * 0.6, "i", CLARO if escuro else TINTA2, q)
    E.escreve(c, "direita", x + 420, y - size * 1.1, size * 0.6, "i", CLARO if escuro else TINTA2, q)
    for i, el in enumerate(els):
        yy = y + i * dy
        Q.atomo(c, x + 40, yy - size * 0.33, size * 0.42, el, q, escuro=escuro)
        a_, b_ = esq.get(el, 0), dir_.get(el, 0)
        ok = a_ == b_
        centro(c, str(a_), x + 230, yy, size, "g", tinta if ok else ERRADO, q)
        centro(c, str(b_), x + 480, yy, size, "g", tinta if ok else ERRADO, q)
        if ok:
            E.selo(c, x + 620, yy - size * 0.33, size * 0.36, True, q)


def macho(c, t, t0, x, y, ativa=None, tl=None, escuro=False, dx=330, rr=64):
    """as cinco fichas da ordem: Metal, Ametal, Carbono, Hidrogênio, Oxigênio"""
    nomes = ("Metal", "Ametal", "Carbono", "Hidrogênio", "Oxigênio")
    for i, n in enumerate(nomes):
        ti = tl[i] if tl else t0 + 0.2 * i
        cx = x + i * dx
        on = ativa == i
        E.foco(c, t, ti, 0.4, lambda a, n=n, cx=cx, on=on: (E.bola(c, cx, y, rr, E.COR if on else ("#3A3B42" if escuro else TINTA), a),
                                                            centro(c, n[0], cx, y + rr * 0.4, rr * 1.2, "g", BR, a),
                                                            centro(c, n.lower(), cx, y + rr + 50, rr * 0.62, "b", (CLARO if escuro else TINTA2) if not on else E.COR, a)))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("a queima do propano, do botijão", "i", 72, TINTA2), XE, 200, passo=0.12)
        Q.equacao(c, t, C["s01.a"] + 0.4, PROP[0], W / 2, 430, 140, passo=0.25)
        placar(c, t, C["s01.b"], PROP[0], 640, 650, ["C"], 80)
        E.frase(c, t, C["s01.d"], ps("sumiram dois carbonos?", "i", 70), W / 2, 880, "center", 0.12)
        E.frase(c, t, C["s01.d"] + 1.6, ps("não: a equação está", "i", 66, TINTA2) + [("desequilibrada", "g", 62, COR)], W / 2, 980, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    promessa(c, t, C["s02"], [(C["s02.a"], [("balancear", "g", 70, COR), ("a", "i", 74), ("equação", "g", 70)]),
                              (C["s02.b"], [("a", "i", 74), ("ordem", "g", 70, COR), ("que", "i", 74), ("poupa", "i", 74), ("conta", "g", 70)]),
                              (C["s02.c"], [("conferir", "g", 70), ("em", "i", 74), ("segundos", "g", 70)])])


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre de duas coisas", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("nenhum átomo some, nenhum aparece:", "i", 66), XE, 360, passo=0.1)
    pilula_em(c, t, C["s03.a"] + 1.4, "Lavoisier", XE + 1180, 335, 50, E.COR)
    E.frase(c, t, C["s03.b"], ps("o", "i", 66) + [("coeficiente", "g", 62, COR)] + ps("multiplica a molécula inteira", "i", 66), XE, 520, passo=0.1)
    Q.formula_em(c, t, C["s03.c"], "3 CO2", XE, 760, 140, cores={"coef": E.COR})
    for k in range(3):
        Q.molecula(c, t, C["s03.c"] + 0.3 + 0.25 * k, "CO2", 900 + k * 260, 720, 70, passo=0.05)
    E.frase(c, t, C["s03.c"] + 1.2, [("3", "g", 64, COR)] + ps("carbonos e", "i", 66) + [("6", "g", 64, COR)] + ps("oxigênios", "i", 66), XE, 930, passo=0.12)


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("balancear", "g", 90, COR)] + ps("= escolher os coeficientes", "i", 76) if False else [("balancear:", "g", 90, COR)] + ps("escolher os coeficientes", "i", 76), XE, 250, passo=0.14)
        E.frase(c, t, C["s04.b"], ps("até cada elemento ter o mesmo número de átomos dos dois lados", "i", 56, TINTA2), XE, 360, passo=0.08)
        Q.formula_em(c, t, C["s04.c"], "4 H2O", W / 2, 680, 220, align="center", cores={"coef": E.COR})
        G = Q.grupos("4 H2O", W / 2, 680, 220, "center")
        pilula_em(c, t, C["s04.c"] + 0.3, "coeficiente: pode mudar", G[0]["cx"] - 150, 820, 46, E.COR)
        pilula_em(c, t, C["s04.d"], "índice: não muda", G[1]["x1"] + 150, 820, 46, TINTA)
        return
    E.frase(c, t, C["s05"], ps("uma ordem que funciona", "i", 76, TINTA2), XE, 200, passo=0.12)
    ativa = None
    for i, k in enumerate(("s05.a", "s05.b", "s05.c", "s05.d", "s05.e")):
        if t >= C[k]:
            ativa = i
    if t >= C["s05.f"]:
        ativa = None
    macho(c, t, 0, 300, 480, ativa, tl=[C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]])
    for k, txt, x in (("s05.a", "ferro, alumínio, magnésio", 300), ("s05.b", "enxofre, nitrogênio", 630)):
        if t < C["s05.f"]:
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, txt=txt, x=x: centro(c, txt, x, 680, 40, "i", TINTA2, a))
    E.frase(c, t, C["s05.f"], ps("as iniciais:", "i", 76, TINTA2) + [("MACHO", "g", 110, COR)], W / 2, 800, "center", 0.14)
    if t >= C["s06"]:
        E.frase(c, t, C["s06.a"], ps("o oxigênio por último: está em quase todas as substâncias", "i", 54), W / 2, 930, "center", 0.08)
        E.frase(c, t, C["s06.b"], ps("mexer nele cedo obriga a refazer tudo", "i", 54, TINTA2), W / 2, 1010, "center", 0.08)


# ---------------- exemplo com metal ----------------
def b_metal(c, t, C, b):
    E.frase(c, t, C["s07"], ps("um exemplo curto", "i", 70, TINTA2), XE, 180, passo=0.12)
    eq = estagio(t, MG, [C["s07.e"]])
    Q.equacao(c, t, C["s07.a"], eq, W / 2, 400, 130, passo=0.25, cores={"coef": E.COR})
    ativa = 0 if t < C["s07.c"] else 1 if t < C["s08.a"] else 3
    macho(c, t, C["s07.b"] - 0.4, 560, 560, ativa, dx=200, rr=44)
    els = ["Mg"] if t < C["s07.c"] else ["Mg", "Cl"] if t < C["s08.a"] else ["Mg", "Cl", "H"]
    placar(c, t, C["s07.b"], eq, 560, 780, els, 54, dy=76)
    if t >= C["s08.c"]:
        pilula_em(c, t, C["s08.c"], "balanceada", 1560, 830, 50, CERTO)
        E.foco(c, t, C["s08.d"], 0.4, lambda a: centro(c, "o coeficiente 1 não se escreve", 1560, 940, 44, "i", TINTA2, a))


# ---------------- propano ----------------
def b_propano(c, t, C, b):
    eq = estagio(t, PROP, [C["s09.c"], C["s10.d"], C["s11.f"]])
    if t >= C["s12"]:
        eq = PROP[-1]
    Q.equacao(c, t, C["s09"], eq, W / 2, 260, 108, tl=[C["s09"]] * 7, cores={"coef": E.COR})
    ativa = 2 if t < C["s10"] else 3 if t < C["s11"] else 4
    if t < C["s12"]:
        macho(c, t, C["s09.a"], 560, 430, ativa, dx=200, rr=44)
    els = ["C"] if t < C["s10"] else ["C", "H"] if t < C["s11"] else ["C", "H", "O"]
    if t < C["s12"]:
        placar(c, t, C["s09.b"], eq, 260, 690, els, 56, dy=86)
        # a conta de apoio, à direita
        if C["s10.b"] <= t < C["s11"]:
            E.formula_em(c, t, C["s10.c"], "4 × 2 = 8", 1450, 800, 80, "g", TINTA2, "center")
        if t >= C["s11.b"]:
            E.formula_em(c, t, C["s11.b"], "3 × 2 = 6", 1450, 720, 66, "g", TINTA2, "center")
            E.formula_em(c, t, C["s11.c"], "4 × 1 = 4", 1450, 800, 66, "g", TINTA2, "center")
            E.formula_em(c, t, C["s11.d"], "6 + 4 = 10", 1450, 880, 66, "g", TINTA, "center")
            E.formula_em(c, t, C["s11.e"], "5 × 2 = 10", 1450, 980, 66, "g", COR, "center")
        return
    placar(c, t, C["s12.b"], eq, 560, 540, ["C", "H", "O"], 66, dy=110)
    bola_txt(c, t, C["s12.c"], "ok", 1560, 640, 100, 70, CERTO)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("mexer no índice", "i", 74), XE + 450, 190, passo=0.12)
    Q.formula_em(c, t, C["s13.b"], "H2O", 520, 520, 200, align="center")
    E.foco(c, t, C["s13.b"] + 0.4, 0.4, lambda a: M.arrow(c, 760, 460, 960, 460, TINTA2, a, 6, 22))
    Q.formula_em(c, t, C["s13.b"] + 0.6, "H2O2", 1300, 520, 200, align="center", cor=ERRADO)
    Q.molecula(c, t, C["s13.c"], "H2O", 520, 720, 90, passo=0.1)
    Q.molecula(c, t, C["s13.c"] + 0.2, "H2O2", 1300, 720, 90, passo=0.1)
    E.foco(c, t, C["s13.d"], 0.4, lambda a: (centro(c, "água", 520, 860, 56, "i", TINTA, a), centro(c, "água oxigenada", 1300, 860, 56, "i", ERRADO, a)))
    if t >= C["s13.d"] + 0.6:
        E.risco(c, 1110, 560, 1490, 420, t, C["s13.d"] + 0.6, largura=10)
    E.frase(c, t, C["s13.e"], ps("o índice diz o que a substância é: só o", "i", 58) + [("coeficiente", "g", 54, COR)] + ps("muda", "i", 58), W / 2, 990, "center", 0.08)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    palco_titulo(c, t, C["s14"], "o atalho de prova")
    if t < C["s15"]:
        E.frase(c, t, C["s14.a"], [("O", "g", 62, BR)] + ps("ímpar de um lado, de dois em dois do outro?", "i", 62, CLARO), W / 2, 280, "center", 0.1)
        E.frase(c, t, C["s14.b"], [("dobre", "g", 66, BR)] + ps("quem deu ímpar", "i", 66, CLARO), W / 2, 380, "center", 0.12)
    eq = estagio(t, AL, [C["s15.a"], C["s15.b"], C["s15.d"]])
    Q.equacao(c, t, C["s14.c"], eq, W / 2, 580, 130, passo=0.25, escuro=True, cores={"coef": E.CLARO})
    placar(c, t, C["s14.d"], eq, 360, 790, ["Al", "O"], 60, escuro=True, dy=90)
    if t >= C["s15.e"]:
        E.frase(c, t, C["s15.e"], ps("ímpar × 2 = par", "i", 62, CLARO) if False else [("ímpar", "g", 60, BR), ("× 2", "g", 60, CLARO), ("= par", "g", 60, BR)], 1500, 820, "center", 0.12)
    if t >= C["s15.f"]:
        E.frase(c, t, C["s15.f"], [("não", "g", 54, ERRADO)] + ps("compensa se já der par", "i", 56, CLARO), 1500, 940, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    def desenho():
        pass
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s16.a"], ps("a queima do álcool comum", "i", 64, TINTA2), XE, 300, passo=0.1)
    Q.equacao(c, t, C["s16.b"], ETA[0], XE, 480, 110, align="left", tl=[C["s16.b"], C["s16.b"] + 0.3, C["s16.b"] + 0.6, C["s16.c"] - 0.2, C["s16.c"], C["s16.c"] + 0.3, C["s16.c"] + 0.5])
    E.frase(c, t, C["s16.d"], [("1", "g", 56, COR)] + ps("balanceie", "i", 60), XE, 680, passo=0.1)
    E.frase(c, t, C["s16.d"] + 0.6, [("2", "g", 56, COR)] + ps("qual é a soma dos coeficientes?", "i", 60), XE, 790, passo=0.1)
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1600, cy=760, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    eq = estagio(t, ETA, [C["s18.a"] + 0.4, C["s18.b"] + 0.4, C["s19.c"]])
    Q.equacao(c, t, C["s18"], eq, W / 2, 240, 110, tl=[C["s18"]] * 7, cores={"coef": E.COR})
    els = ["C"] if t < C["s18.b"] else ["C", "H"] if t < C["s18.c"] else ["C", "H", "O"]
    placar(c, t, C["s18.a"], eq, 220, 440, els, 56, dy=86)
    if t >= C["s18.c"]:
        E.formula_em(c, t, C["s18.c"], "2 × 2 + 3 = 7", 1450, 470, 66, "g", TINTA2, "center")
    if t >= C["s19"]:
        E.formula_em(c, t, C["s19.a"], "o álcool traz 1 O", 1450, 570, 56, "b", COR, "center")
        E.formula_em(c, t, C["s19.b"], "7 − 1 = 6", 1450, 660, 66, "g", TINTA2, "center")
        E.formula_em(c, t, C["s19.c"], "3 × 2 = 6", 1450, 750, 66, "g", TINTA2, "center")
        E.formula_em(c, t, C["s19.d"], "1 + 3 + 2 + 3 =", 960, 930, 84, "g", TINTA, "right")
        bola_txt(c, t, C["s19.e"], "9", 1070, 900, 70, 84, CERTO)
        E.foco(c, t, C["s19.e"] + 1.2, 0.4, lambda a: E.escreve(c, "esqueceu o 1? dá 8", 1200, 925, 52, "i", ERRADO, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def prox():
        for i, (f, rot) in enumerate((("2 H2 + O2 -> 2 H2O", "síntese"), ("2 H2O2 -> 2 H2O + O2", "análise"))):
            Q.formula_em(c, t, C["s21.a"] + 0.4 * i, f, XE, 720 + i * 130, 72)
            pilula_em(c, t, C["s21.a"] + 0.4 * i + 0.3, rot, XE + 1040, 700 + i * 130, 40, TINTA2)
    fim(c, t, C, "s20", [("s20.a", [("só", "i", 72), ("o", "i", 72), ("coeficiente", "g", 66, COR), ("muda", "i", 72)]),
                         ("s20.b", [("ordem", "i", 72), ("MACHO", "g", 66, COR)]),
                         ("s20.c", [("confira", "i", 72), ("elemento", "g", 66), ("por", "i", 72), ("elemento", "g", 66)])],
        "s21", "Síntese, análise", "e combustão", "s21.c", "s21.d", prox)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, regra=b_regra, metal=b_metal, propano=b_propano, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
