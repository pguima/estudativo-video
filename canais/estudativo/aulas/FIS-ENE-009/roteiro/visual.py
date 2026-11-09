"""Visual — Estudativo · FIS-ENE-009: colisões e coeficiente de restituição.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001): painel "antes" | "depois", corpos = esferas laranja com a massa dentro (a segunda bola em
petróleo-claro quando precisa distinguir), velocidades petróleo com o valor, Ec em barras_energia. O coeficiente e
aparece como pílula: e = 1 laranja, 0 < e < 1 cinza-tinta, e = 0 azul.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-009_colisoes_e_coeficiente_de_restituicao.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "tipos", "inelastica", "elastica", "parcial", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
QC, EC = F.VEL, F.VEL
B2 = "#3FB8C4"  # a segunda bola

# todas as contas da aula
Ec = lambda m, v: m * v * v / 2
assert 1000 * 20 / 2000 == 10 and Ec(1000, 20) == 200000 and Ec(2000, 10) == 100000
v_err = math.sqrt(200000 * 2 / 2000); assert abs(v_err - 14.14) < 0.01 and round(2000 * v_err) == 28284
assert (4 + 4) / 2 == 4 and 4 - 4 == 0
assert (12 - 3) / 3 == 3 and 3 + 3 == 6 and 0.5 * 6 == 3 and Ec(2, 6) == 36 and Ec(2, 3) + Ec(1, 6) == 27
assert 3 * 4 / 4 == 3 and Ec(3, 4) == 24 and Ec(4, 3) == 18 and 24 - 18 == 6


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "250 J" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g"):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=BR))


def sinal_tau(c, t, t0, tipo, cx, cy, size=48):
    """pílula do sinal do trabalho: + ajuda (laranja), − atrapalha (azul), 0 perpendicular (cinza)"""
    txt, fundo = {"+": ("τ > 0", E.COR), "-": ("τ < 0", F.NEG), "0": ("τ = 0", TINTA2)}[tipo]
    pilula_em(c, t, t0, txt, cx, cy, size, fundo)


def milhar(v):
    """número com ponto de milhar: 200000 vira 200.000"""
    return f"{int(v):,}".replace(",", ".") if float(v).is_integer() else E._num(v)


def barras_energia(c, t, x, yb, h, vmax, itens, larg_=150, gap=60, size=44, total=None, t_total=None, fmt=None):
    """barras verticais de energia na base yb: itens = [(rótulo, valor, cor, instante)]; h = altura de vmax.
    total = valor da linha tracejada do total (aparece em t_total). O valor (fmt) vai em cima de cada barra"""
    fmt = fmt or (lambda v: milhar(v) + " J")
    for i, (rot, v, cor, ti) in enumerate(itens):
        bx = x + i * (larg_ + gap)
        q = ep(t, ti, 0.4)
        if q <= 0:
            continue
        hh = h * v / vmax * ease_io(prog(t, ti, 0.7))
        if hh > 0.5:
            M.rrect(c, bx, yb - hh, larg_, hh, 10, cor, q)
        E.foco(c, t, ti + 0.4, 0.4, lambda a, bx=bx, v=v, hh=hh: F.medida(c, *(fmt(v).split(" ", 1) + [""])[:2], bx + larg_ / 2, yb - h * v / vmax - 18, size, TINTA, a, "center"))
        E.foco(c, t, ti, 0.4, lambda a, bx=bx, rot=rot, cor=cor: centro(c, rot, bx + larg_ / 2, yb + size + 14, size, "g", cor, a))
    if total is not None and t_total is not None and t >= t_total:
        n = len(itens)
        yt = yb - h * total / vmax
        M.line(c, x - 30, yt, x + n * larg_ + (n - 1) * gap + 30, yt, TINTA, ep(t, t_total, 0.4), 4, dash=E.TRACO)
    if t >= min(it[3] for it in itens):
        n = len(itens)
        M.line(c, x - 30, yb, x + n * larg_ + (n - 1) * gap + 30, yb, TINTA, ep(t, min(it[3] for it in itens), 0.4), 5)


def sentido_mais(c, t, t0, x, y, escuro=False):
    """convenção de sinal: seta curta para a direita com "+" (sentido positivo)"""
    tinta = BR if escuro else TINTA
    E.foco(c, t, t0, 0.4, lambda a: (F.seta(c, x, y, x + 150, y, tinta, a, 7), E.escreve(c, "+", x + 165, y + 18, 56, "g", tinta, a),
                                      E.escreve(c, "sentido positivo", x, y + 56, 36, "i", tinta, a)))


def lembrete(c, t, C, cena, itens, desenhos=()):
    """lembrete de 2 ou 3 coisas: itens = [(cue, linha fina, linha forte, linha de fórmula ou None)]"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, str(n), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    hs = [200 + (70 if it[3] else 0) for it in itens]
    gap = 40 if n == 2 else 30
    y = 120 + (800 - sum(hs) - gap * (n - 1)) / 2
    for i, (k, l1, l2, l3) in enumerate(itens):
        h = hs[i]
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 56)], x + 44, y + 82)
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, x + 44, y + 160, 56, "g", COR, a))
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: E.formula(c, l3, x + 44, y + 240, 46, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


# ---------------- peças desta aula ----------------
def corpo(c, cx, cy, r, rot, a=1.0, cor=None):
    """corpo = esfera laranja com a massa dentro"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, cor or E.COR, a)
    if rot:
        centro(c, rot, cx, cy + r * 0.18, r * 0.5, "g", BR, a)


def painel(c, t, t0, x, y, w, h, titulo):
    p = ep(t, t0, 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, titulo, x + 30, y + 64, 50, "i", TINTA2, a))


def vel(c, t, t0, x, y, L, rot, lado=None):
    """velocidade (petróleo) de comprimento L (negativo = para a esquerda); o valor fica em cima"""
    lado = lado if lado is not None else (1 if L > 0 else -1)
    F.vetor(c, t, t0, (x, y), (x + L, y), None, rot, QC, 9, lado=lado, size=46)


def coef(c, t, t0, s, cx, cy, size=50):
    fundo = {"e = 1": E.COR, "e = 0": F.NEG}.get(s, TINTA2)
    pilula_em(c, t, t0, s, cx, cy, size, fundo)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 420
        E.frase(c, t, C["s01.a"], [("sinuca", "g", 70, COR)], XE, 220)
        if t >= C["s01.a"]:
            c.drawRect(skia.Rect.MakeXYWH(150, y - 120, 1620, 240), M.paint("#2E7D4F", 0.25 * ep(t, C["s01.a"], 0.4)))
        p = ease_io(prog(t, C["s01.a"] + 0.5, 1.2))
        xa = lerp(400, 900, p)
        q2 = ease_out(prog(t, C["s01.c"], 1.2))
        xb = lerp(1010, 1600, q2) if t >= C["s01.c"] else 1010
        E.foco(c, t, C["s01.a"], 0.4, lambda a: corpo(c, xa, y, 55, "", a, BR))
        E.foco(c, t, C["s01.a"], 0.4, lambda a: corpo(c, xb, y, 55, "", a))
        pilula_em(c, t, C["s01.b"], "a branca para", 900, y + 170, 42, TINTA)
        pilula_em(c, t, C["s01.c"] + 0.4, "a outra sai", 1550, y + 170, 42, E.COR)

    def dois():
        y2 = 820
        if t >= C["s01.d"]:
            F.chao(c, 170, 1750, y2, ep(t, C["s01.d"], 0.4))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: (F.carrinho(c, 820, y2, 300, a=a), F.carrinho(c, 1120, y2, 300, a=a, cor=B2)))
        E.foco(c, t, C["s01.d"] + 0.4, 0.4, lambda a: E.pilula(c, "grudados", 970, y2 - 230, 42, "g", fundo=F.NEG, a=a))
    E.saida(c, t, C["s01.d"] - 0.1, um)
    if t >= C["s01.d"] - 0.1:
        E.saida(c, t, C["s02"] - 0.1, dois)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 320 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
        itens = (("s02.b", "elástica, parcial ou inelástica", True), ("s02.c", "velocidades depois", False))
        for i, (k, s, forte) in enumerate(itens):
            y = 470 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 56, COR if forte else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "com sinal:", "Q antes = Q depois", None),
                              ("s03.c", "energia cinética:", "Ec = f{m · v^2}{2}", None),
                              ("s03.d", "sistemas:", "some as equações", None)))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], ps("forças enormes, tempo curtíssimo", "i", 64), XE, 220, passo=0.1)
        E.frase(c, t, C["s04.a"], ps("forças internas:", "i", 66) + [("de", "i", 66), ("um", "i", 66), ("no", "i", 66), ("outro", "i", 66)], XE, 360, passo=0.1)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: E.pilula(c, "Q se conserva em toda colisão", W / 2, 560, 60, "g", fundo=QC, a=a))
        E.frase(c, t, C["s04.c"], [("Ec:", "g", 66, EC), ("nem", "i", 70), ("sempre", "g", 66)], XE, 760, passo=0.12)
        cadeia_ = ("calor", "som", "deformação")
        for i, s in enumerate(cadeia_):
            E.foco(c, t, C["s04.d"] + 0.3 * i, 0.4, lambda a, i=i, s=s: E.pilula(c, s, (880, 1110, 1400)[i], 740, 46, "g", fundo=CINZA, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.frase(c, t, C["s05.a"], [("coeficiente", "g", 70, COR), ("de", "i", 72), ("restituição", "g", 70, COR)], XE, 200, passo=0.12)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "e = f{afastamento}{aproximação}", XE, 380, 90, "g", TINTA, a))
    if t < C["s06"]:
        return
    y = 720
    E.foco(c, t, C["s06.a"], 0.4, lambda a: E.escreve(c, "antes", XE, y - 110, 50, "i", TINTA2, a))
    E.foco(c, t, C["s06.a"], 0.4, lambda a: (corpo(c, 360, y, 50, "", a), corpo(c, 640, y, 50, "", a, B2)))
    vel(c, t, C["s06.a"] + 0.3, 360, y - 80, 140, None)
    E.foco(c, t, C["s06.a"] + 0.6, 0.4, lambda a: centro(c, "aproximação", 500, y + 100, 46, "g", TINTA, a))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "depois", 900, y - 110, 50, "i", TINTA2, a))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: (corpo(c, 1020, y, 50, "", a), corpo(c, 1400, y, 50, "", a, B2)))
    vel(c, t, C["s06.b"] + 0.3, 1400, y - 80, 140, None)
    E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: centro(c, "afastamento", 1210, y + 100, 46, "g", TINTA, a))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "sentidos opostos: some  ·  mesmo sentido: subtraia", W / 2, 960, 52, "b", TINTA, a, "center"))
    E.foco(c, t, C["s06.c"], 0.4, lambda a: (F.seta(c, 1500, 880, 1600, 880, QC, a, 7), F.seta(c, 1740, 880, 1640, 880, B2, a, 7)))


# ---------------- tipos ----------------
def b_tipos(c, t, C, b):
    cards = (("s07.a", "e = 1", "elástica", "Ec se conserva", 1.0), ("s07.c", "0 < e < 1", "parcialmente elástica", "perde parte", 0.6),
             ("s08.a", "e = 0", "inelástica", "saem grudados", 0.3))
    E.frase(c, t, C["s07"], ps("o coeficiente vai de 0 a 1", "i", 70), W / 2, 180, "center", 0.12)
    for i, (k, e, nome, obs, frac) in enumerate(cards):
        x = 160 + i * 560
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 500, 680, p, prog_=p)
        coef(c, t, C[k] + 0.1, e, x + 250, 380, 54)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, nome=nome, x=x: centro(c, nome, x + 250, 500, 46 if len(nome) > 12 else 60, "g", TINTA, a))
        barras_energia(c, t, x + 110, 880, 260, 1, [("antes", 1, EC, C[k] + 0.5), ("depois", frac, EC, C[k] + 0.9)], larg_=110, gap=60, size=36, fmt=lambda v: "")
        kk = {0: "s07.b", 1: "s07.d", 2: "s08.b"}[i]
        E.foco(c, t, C[kk], 0.4, lambda a, obs=obs, x=x: centro(c, obs, x + 250, 580, 46, "i", TINTA2, a))
    pilula_em(c, t, C["s08.c"], "a que mais perde energia", 1400, 1030, 40, F.NEG)


# ---------------- inelástica ----------------
def b_inelastica(c, t, C, b):
    painel(c, t, C["s09.a"], 120, 150, 820, 360, "antes")
    painel(c, t, C["s09.b"], 980, 150, 820, 360, "depois")
    y = 400
    E.foco(c, t, C["s09.a"], 0.5, lambda a: (corpo(c, 340, y, 75, "1.000", a), corpo(c, 680, y, 75, "1.000", a, B2)))
    vel(c, t, C["s09.a"] + 0.3, 340, y - 110, 200, "20 m/s")
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (corpo(c, 1270, y, 75, "1.000", a), corpo(c, 1420, y, 75, "1.000", a, B2)))
    vel(c, t, C["s09.e"], 1345, y - 110, 120, "10 m/s")

    def s09():
        E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "antes: 1.000 · 20 = 20.000", XE, 680, 64, "g", QC, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "depois: 2.000 · v", XE, 820, 64, "g", TINTA, a))
        bola_txt(c, t, C["s09.e"], "10 m/s", 1350, 760, 120, 56, QC)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: E.formula(c, "Ec antes: f{1.000 · 20^2}{2} = 200.000 J", XE, 680, 56, "g", EC, a))
    E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "Ec depois: f{2.000 · 10^2}{2} = 100.000 J", XE, 860, 56, "g", EC, a))
    barras_energia(c, t, 1350, 990, 360, 200000, [("antes", 200000, EC, C["s10.a"]), ("depois", 100000, EC, C["s10.b"])], larg_=150, gap=80, size=40)
    pilula_em(c, t, C["s10.c"], "metade virou deformação e calor", XE + 520, 1010, 42, CINZA)


# ---------------- elástica ----------------
def b_elastica(c, t, C, b):
    painel(c, t, C["s11.a"], 120, 150, 820, 330, "antes")
    painel(c, t, C["s12.d"] - 0.6, 980, 150, 820, 330, "depois") if t >= C["s12.d"] - 0.6 else None
    y = 380
    E.foco(c, t, C["s11.a"], 0.5, lambda a: (corpo(c, 340, y, 60, "A", a, BR), corpo(c, 680, y, 60, "B", a)))
    E.foco(c, t, C["s11.a"], 0.5, lambda a: centro(c, "A", 340, y + 12, 34, "g", TINTA, a))
    vel(c, t, C["s11.b"], 340, y - 100, 200, "4 m/s")
    if t >= C["s12.d"] - 0.6:
        E.foco(c, t, C["s12.d"] - 0.6, 0.5, lambda a: (corpo(c, 1240, y, 60, "A", a, BR), corpo(c, 1560, y, 60, "B", a)))
        E.foco(c, t, C["s12.d"] - 0.6, 0.5, lambda a: centro(c, "A", 1240, y + 12, 34, "g", TINTA, a))
        vel(c, t, C["s12.d"] - 0.3, 1560, y - 100, 200, "4 m/s")
        E.foco(c, t, C["s12.d"], 0.4, lambda a: E.escreve(c, "parada", 1170, y - 90, 44, "i", TINTA2, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "4 = vA + vB", XE, 640, 76, "g", QC, a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "vB − vA = 4", XE, 760, 76, "g", TINTA, a))
    if t >= C["s12.a"]:
        M.line(c, XE, 800, XE + 520, 800, TINTA, ep(t, C["s12.a"], 0.4), 4)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "2 · vB = 8", XE, 890, 76, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "vB = 4  ·  vA = 0", XE + 600, 890, 76, "g", COR, a))
    pilula_em(c, t, C["s12.e"], "massas iguais, elástica: trocam de velocidade", W / 2, 1010, 44, E.COR)


# ---------------- parcial ----------------
def b_parcial(c, t, C, b):
    y = 330
    painel(c, t, C["s13.a"], 120, 120, 820, 320, "antes")
    E.foco(c, t, C["s13.a"], 0.5, lambda a: (corpo(c, 360, y, 75, "2", a), corpo(c, 660, y, 55, "1", a, B2)))
    vel(c, t, C["s13.a"] + 0.3, 360, y - 110, 200, "6 m/s")
    coef(c, t, C["s13.b"], "e = 0,5", 1560, 580, 54)

    def eqs():
        E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "12 = 2 · vA + vB", XE, 600, 70, "g", QC, a))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "vB − vA = 0,5 · 6 = 3", XE, 720, 70, "g", TINTA, a))
        troca(c, t, [(C["s14.a"], "vB = vA + 3"), (C["s14.b"], "12 = 2 · vA + vA + 3"), (C["s14.c"], "3 · vA = 9  →  vA = 3")],
              lambda s, a: E.formula(c, s, XE, 860, 70, "g", TINTA, a))
    eqs()
    if t >= C["s14.d"]:
        painel(c, t, C["s14.d"] - 0.3, 980, 120, 820, 320, "depois")
        E.foco(c, t, C["s14.d"], 0.5, lambda a: (corpo(c, 1250, y, 75, "2", a), corpo(c, 1600, y, 55, "1", a, B2)))
        vel(c, t, C["s14.d"] + 0.2, 1250, y - 110, 100, "3 m/s")
        vel(c, t, C["s14.d"] + 0.4, 1600, y - 110, 200, "6 m/s")
    barras_energia(c, t, 1350, 1000, 300, 36, [("antes", 36, EC, C["s14.e"]), ("depois", 27, EC, C["s14.e"] + 0.5)], larg_=140, gap=70, size=40)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s15.a"], ps("energia conservada sempre?", "i", 70), XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "200.000 = f{2.000 · v^2}{2}", 560, 440, 76, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s15.b"] + 0.8, 0.5, lambda a: E.formula(c, "v ≈ 14 m/s", 560, 620, 90, "g", ERRADO, a, "center"))
    if t >= C["s16.b"]:
        E.risco(c, 330, 640, 790, 540, t, C["s16.b"], largura=12)
    E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "Q = 2.000 · 14 ≈ 28.000", 560, 800, 66, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "> 20.000 de antes", 560, 920, 66, "g", ERRADO, a, "center"))
    if t >= C["s16.c"]:
        M.line(c, 1080, 300, 1080, 950, FIO, ep(t, C["s16.c"], 0.4), 3)
    E.frase(c, t, C["s16.c"], [("Q:", "g", 70, QC), ("sempre", "g", 70)], 1480, 480, "center", 0.12)
    E.frase(c, t, C["s16.d"], [("Ec:", "g", 70, EC), ("só", "i", 76), ("na", "i", 76), ("elástica", "g", 70, COR)], 1480, 640, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s17():
        E.frase(c, t, C["s17"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s17.a"], [("massas", "g", 64, BR), ("iguais,", "g", 64, BR)] + ps("elástica, uma parada:", "i", 66, CLARO), W / 2, 300, "center", 0.1)
        E.foco(c, t, C["s17.a"] + 1.4, 0.5, lambda a: E.pilula(c, "trocam de velocidade", W / 2, 420, 60, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s17.b"], [("inelástica,", "g", 64, BR)] + ps("um parado:", "i", 66, CLARO), W / 2, 640, "center", 0.1)
        E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "v final = f{Q antes}{massa total}", W / 2, 820, 84, "g", BR, a, "center"))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], ps("na troca: a única saída que conserva Q", "i", 62, CLARO), W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s18.a"] + 1.8, ps("e afasta na mesma rapidez", "i", 62, CLARO), W / 2, 390, "center", 0.1)
    E.frase(c, t, C["s18.b"], ps("na inelástica: uma velocidade só, a do conjunto", "i", 62, CLARO), W / 2, 540, "center", 0.1)
    E.frase(c, t, C["s18.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("elástica com massas diferentes", "i", 64, CLARO), W / 2, 760, "center", 0.1)
    E.frase(c, t, lerp(C["s18.c"], C["s18.end"], 0.6), ps("aí, monte o sistema", "i", 60, CLARO), W / 2, 870, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s19.a"], [("3 kg", "g", 66), ("a", "i", 70), ("4 m/s", "g", 66, QC), ("bate", "i", 70), ("em", "i", 70), ("1 kg", "g", 66), ("parado", "i", 70)], XE, 350, passo=0.12)
    E.frase(c, t, C["s19.b"], [("seguem", "i", 70), ("grudados", "g", 66, F.NEG)], XE, 460, passo=0.12)
    E.frase(c, t, C["s19.c"], [("velocidade", "i", 70), ("final?", "g", 66, COR)], XE, 620, passo=0.12)
    E.frase(c, t, C["s19.d"], [("tipo", "i", 70), ("de", "i", 70), ("colisão?", "g", 66, COR)], XE, 730, passo=0.12)
    E.frase(c, t, C["s19.e"], [("energia", "i", 70), ("perdida?", "g", 66, COR)], XE, 840, passo=0.12)
    if t < C["s20"]:
        E.foco(c, t, C["s19.a"], 0.5, lambda a: (corpo(c, 1300, 640, 90, "3", a), corpo(c, 1620, 655, 60, "1", a, B2)))
        vel(c, t, C["s19.a"] + 0.3, 1300, 510, 200, "4 m/s")
    else:
        E.relogio(c, t, C["s20.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s21():
        E.foco(c, t, C["s21.a"], 0.5, lambda a: E.formula(c, "antes: 3 · 4 = 12", XE, 300, 76, "g", QC, a))
        E.foco(c, t, C["s21.b"], 0.5, lambda a: E.formula(c, "depois: 4 · v", XE, 460, 76, "g", TINTA, a))
        bola_txt(c, t, C["s21.c"], "3 m/s", 1400, 420, 130, 64, QC)
        coef(c, t, C["s21.d"], "e = 0", 1400, 700, 60)
        E.foco(c, t, C["s21.d"] + 0.3, 0.4, lambda a: centro(c, "inelástica", 1400, 820, 56, "g", TINTA, a))
    E.saida(c, t, C["s22"] - 0.1, s21)
    if t < C["s22"]:
        return
    E.foco(c, t, C["s22.a"], 0.5, lambda a: E.formula(c, "antes: f{3 · 4^2}{2} = 24 J", XE, 330, 76, "g", EC, a))
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.formula(c, "depois: f{4 · 3^2}{2} = 18 J", XE, 560, 76, "g", EC, a))
    bola_txt(c, t, C["s22.c"], "6 J", XE + 300, 820, 110, 64, TINTA2)
    barras_energia(c, t, 1300, 900, 480, 24, [("antes", 24, EC, C["s22.a"]), ("depois", 18, EC, C["s22.b"]), ("perdeu", 6, CINZA, C["s22.c"])], larg_=130, gap=60, size=40)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s23.a", "toda colisão: Q se conserva"), ("s23.b", "e = f{afastamento}{aproximação}"), ("s23.c", "Ec se conserva só com e = 1"))
        for i, (k, s) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 68, "g", TINTA, a))
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s24.a"], [("praticando", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s24.a"] + 0.7, ps("impulso, recuo e colisões", "i", 64, TINTA2), XE, 540, passo=0.1)
    E.foco(c, t, C["s24.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s24.b"] + 0.2, 0.4))
    E.frase(c, t, C["s24.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, tipos=b_tipos, inelastica=b_inelastica, elastica=b_elastica,
              parcial=b_parcial, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
