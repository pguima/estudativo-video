"""Visual — Estudativo · FIS-ENE-010: praticando impulso e colisões (cinco situações). Última aula da trilha.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001): corpos = esferas laranja com a massa dentro (o segundo corpo em petróleo-claro), velocidade =
seta petróleo com o valor, painel "antes" | "depois", sentido_mais, Ec em barras_energia, coeficiente em pílula.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-010_praticando_impulso_e_colisoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
QC, EC = F.VEL, F.VEL
B2 = "#3FB8C4"

# todas as contas da aula
ok = lambda a, b: abs(a - b) < 1e-9
Ec = lambda m, v: m * v * v / 2
assert ok(0.45 * 30, 13.5) and ok(13.5 / 0.015, 900) and 13500 / 15 == 900 and 2 * 15 == 30 and -30 / 60 == -0.5 and 60 / 2 == 30 and 15 / 30 == 0.5
assert ok(0.02 * 300, 6) and ok(0.02 + 1.98, 2) and 6 / 2 == 3 and ok(Ec(0.02, 300), 900) and Ec(2, 3) == 9 and 900 - 9 == 891
assert 8 - 3 * 3 == -1 and (3 + 1) / 8 == 0.5 and Ec(1, 8) == 32 and Ec(1, -1) + Ec(3, 3) == 14
assert (6 - 12) / 3 == -2 and -2 + 6 == 4 and 1 * 6 == -2 + 2 * 4 and Ec(1, 6) == 18 and Ec(1, -2) + Ec(2, 4) == 18


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
    if a <= 0:
        return
    E.bola(c, cx, cy, r, cor or E.COR, a)
    if rot:
        centro(c, rot, cx, cy + r * 0.18, max(r * 0.5, 38), "g", BR, a)


def vel(c, t, t0, x, y, L, rot, lado=None):
    lado = lado if lado is not None else (1 if L > 0 else -1)
    F.vetor(c, t, t0, (x, y), (x + L, y), None, rot, QC, 9, lado=lado, size=46)


def painel(c, t, t0, x, y, w, h, titulo):
    p = ep(t, t0, 0.5)
    E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, titulo, x + 30, y + 64, 50, "i", TINTA2, a))


def situacao(c, t, t0, n, titulo):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 180, 56, a=a), centro(c, str(n), XE + 50, 206, 70, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [(titulo, "g", 72)], XE + 140, 205)


def pausa(c, t, C, cena):
    E.relogio(c, t, C[cena + ".a"], cx=1460, cy=520, r=200)


def bola_futebol(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(BR, a))
    c.drawCircle(cx, cy, r, M.paint(TINTA, a, stroke=max(3, r * 0.08)))
    for k in range(5):
        g = math.radians(90 + 72 * k)
        c.drawCircle(cx + math.cos(g) * r * 0.62, cy - math.sin(g) * r * 0.62, r * 0.17, M.paint(TINTA, a))
    c.drawCircle(cx, cy, r * 0.22, M.paint(TINTA, a))


def dois_carrinhos(c, t, t0, mA, mB, vA_txt, xA=380, xB=720, y=420):
    painel(c, t, t0, 120, 250, 820, 330, "antes")
    E.foco(c, t, t0, 0.5, lambda a: (corpo(c, xA, y + 40, 55 + 6 * mA, f"{mA} kg", a), corpo(c, xB, y + 40, 55 + 6 * mB, f"{mB} kg", a, B2)))
    E.foco(c, t, t0, 0.5, lambda a: (centro(c, "A", xA, y - 50, 40, "g", TINTA, a), centro(c, "B", xB, y - 60, 40, "g", TINTA, a)))
    vel(c, t, t0 + 0.4, xA + 60, y - 50, 160, vA_txt)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR), ("situações", "i", 110)], XE, 330, passo=0.2)
    nomes = ("chute", "gelo", "bala", "batida", "batida")
    for i, s in enumerate(nomes):
        ti = lerp(C["s01.b"], C["s01.c"] - 0.3, i / 4)
        x = XE + i * 330
        E.foco(c, t, ti, 0.4, lambda a, i=i, x=x, s=s: (E.bola(c, x + 50, 520, 46, a=a), centro(c, str(i + 1), x + 50, 540, 54, "g", BR, a),
                                                        centro(c, s, x + 50, 640, 48, "g", TINTA, a)))
    E.frase(c, t, C["s01.c"], ps("pause e resolva antes da resposta", "i", 66), XE, 840, passo=0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 80), XE, 200, passo=0.12)
    linhas = (("s02.a", "I = F · Δt = ΔQ"), ("s02.b", "nada de fora: Q antes = Q depois"), ("s02.c", "e = f{afastamento}{aproximação}"))
    for i, (k, s) in enumerate(linhas):
        y = 400 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, XE + 110, y, 70, "g", TINTA, a))
    E.frase(c, t, lerp(C["s02.c"], C["s02.end"], 0.6), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), XE, 1000, passo=0.1)


# ---------------- situação 1: chute ----------------
def chute(c, t, t0, x, y):
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    F.chao(c, x - 200, x + 700, y + 60, q)
    E.foco(c, t, t0, 0.4, lambda a: bola_futebol(c, x, y, 60, a))


def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1, "o chute")
    E.frase(c, t, C["s03.b"], [("bola", "i", 64), ("0,45 kg,", "g", 60), ("parada", "i", 64)], XE, 370, passo=0.12)
    E.frase(c, t, C["s03.c"], [("sai", "i", 64), ("a", "i", 64), ("30 m/s", "g", 60, QC)], XE, 480, passo=0.12)
    E.frase(c, t, C["s03.d"], [("contato:", "i", 64), ("15", "g", 60), ("milésimos", "i", 64), ("de", "i", 64), ("segundo", "i", 64)], XE, 590, passo=0.12)
    E.frase(c, t, C["s03.e"], [("força", "i", 66), ("média?", "g", 64, COR)], XE, 770, passo=0.12)
    if t < C["s04"]:
        chute(c, t, C["s03.b"], 1250, 640)
        vel(c, t, C["s03.c"], 1330, 520, 300, "30 m/s")
    else:
        pausa(c, t, C, "s04")


def b_resposta1(c, t, C, b):
    def s05():
        E.foco(c, t, C["s05.a"], 0.5, lambda a: E.formula(c, "I = ΔQ", XE, 270, 80, "g", E.COR_TEXTO, a))
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "ΔQ = 0,45 · 30 = 13,5", XE, 430, 80, "g", QC, a))
        E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, "Δt = 0,015 s", XE, 590, 80, "g", TINTA, a))
        E.foco(c, t, C["s05.d"], 0.5, lambda a: E.formula(c, "F = f{13,5}{0,015}", XE, 800, 96, "g", TINTA, a))
    E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06"], 0.4, lambda a: E.formula(c, "F = f{13,5}{0,015}", XE, 400, 96, "g", TINTA2, a))
    E.foco(c, t, C["s06.a"], 0.4, lambda a: E.pilula(c, "× 1.000 em cima e embaixo", 1150, 370, 46, "b", fundo=TINTA2, a=a))
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "= f{13.500}{15}", XE, 700, 96, "g", TINTA, a))
    bola_txt(c, t, C["s06.c"], "900 N", 1300, 700, 140, 70)


# ---------------- situação 2: gelo ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C["s07.a"], 2, "o arremesso no gelo")
    E.frase(c, t, C["s07.b"], [("patinadora", "i", 64), ("60 kg,", "g", 60), ("parada", "i", 64)], XE, 380, passo=0.12)
    E.frase(c, t, C["s07.c"], [("bola", "i", 64), ("2 kg", "g", 60), ("a", "i", 64), ("15 m/s", "g", 60, QC)], XE, 490, passo=0.12)
    E.frase(c, t, C["s07.d"], [("velocidade", "i", 66), ("de", "i", 66), ("recuo?", "g", 64, COR)], XE, 670, passo=0.12)
    if t < C["s08"]:
        E.foco(c, t, C["s07.b"], 0.5, lambda a: corpo(c, 1300, 600, 120, "60", a))
        E.foco(c, t, C["s07.c"], 0.5, lambda a: corpo(c, 1560, 620, 50, "2", a, B2))
        vel(c, t, C["s07.c"] + 0.3, 1560, 520, 220, "15 m/s")
        if t >= C["s07.b"]:
            M.line(c, 1050, 760, 1850, 760, "#9FC9DD", ep(t, C["s07.b"], 0.4), 8)
    else:
        pausa(c, t, C, "s08")


def b_resposta2(c, t, C, b):
    sentido_mais(c, t, C["s09"], 1560, 140)
    E.frase(c, t, C["s09.a"], ps("começou parado:", "i", 64) + [("razão", "g", 60, COR), ("inversa", "g", 60, COR)], XE, 250, passo=0.12)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.formula(c, "60 = 30 · 2", XE, 420, 84, "g", TINTA, a))
    E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "f{15}{30} = 0,5 m/s", XE, 600, 84, "g", TINTA, a))
    pilula_em(c, t, C["s09.d"], "para trás", XE + 760, 580, 50, F.NEG)
    E.foco(c, t, C["s09.e"], 0.5, lambda a: E.formula(c, "2 · 15 + 60 · v = 0  →  v = −0,5", XE, 860, 70, "g", QC, a))
    E.foco(c, t, C["s09.a"], 0.5, lambda a: (corpo(c, 1300, 520, 100, "60", a), corpo(c, 1600, 540, 45, "2", a, B2)))
    vel(c, t, C["s09.d"], 1300, 380, -150, "0,5 m/s")
    vel(c, t, C["s09.a"] + 0.4, 1600, 440, 200, "15 m/s")


# ---------------- situação 3: bala no bloco ----------------
def bala_bloco(c, t, t0, x, y, crava=None):
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    F.chao(c, x - 600, x + 400, y + 90, q)
    F.bloco(c, x, y, 220, 180, "1,98 kg", "#8B5E3C", q, size=40)
    bx = x - 520 if crava is None or t < crava else lerp(x - 520, x - 130, ease_out(prog(t, crava, 0.4)))
    M.rrect(c, bx, y - 12, 60, 24, 10, TINTA, q)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E.escreve(c, "20 g", x - 540, y - 40, 46, "g", TINTA, a)) if crava is None or t < crava else None


def b_questao3(c, t, C, b):
    situacao(c, t, C["s10.a"], 3, "a bala no bloco")
    E.frase(c, t, C["s10.b"], [("bala", "i", 64), ("20 g", "g", 60), ("a", "i", 64), ("300 m/s", "g", 60, QC)], XE, 370, passo=0.12)
    E.frase(c, t, C["s10.c"], [("bloco", "i", 64), ("1,98 kg,", "g", 60), ("parado,", "i", 64), ("superfície", "i", 64), ("lisa", "g", 60)], XE, 480, passo=0.12)
    E.frase(c, t, C["s10.d"], [("velocidade", "i", 66), ("do", "i", 66), ("conjunto?", "g", 64, COR)], XE, 660, passo=0.12)
    E.frase(c, t, C["s10.d"] + 1.6, [("energia", "i", 66), ("perdida?", "g", 64, COR)], XE, 770, passo=0.12)
    if t < C["s11"]:
        bala_bloco(c, t, C["s10.b"], 1500, 860)
        vel(c, t, C["s10.b"] + 0.3, 1000, 760, 200, "300 m/s")
    else:
        pausa(c, t, C, "s11")


def b_resposta3(c, t, C, b):
    def s12():
        E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "20 g = 0,02 kg", XE, 270, 70, "g", TINTA2, a))
        E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "antes: 0,02 · 300 = 6", XE, 420, 76, "g", QC, a))
        E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "depois: 2 · v", XE, 570, 76, "g", TINTA, a))
        bola_txt(c, t, C["s12.d"], "3 m/s", 1400, 480, 130, 64, QC)
        pilula_em(c, t, C["s12.e"], "grudaram: inelástica", 1400, 720, 50, F.NEG)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "antes: f{0,02 · 300^2}{2} = 900 J", XE, 330, 70, "g", EC, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "depois: f{2 · 3^2}{2} = 9 J", XE, 540, 70, "g", EC, a))
    bola_txt(c, t, C["s13.c"], "891 J", XE + 300, 790, 120, 60, TINTA2)
    E.frase(c, t, C["s13.c"] + 1.4, ps("calor e madeira rasgada", "i", 54, TINTA2), XE + 480, 810, passo=0.1)
    barras_energia(c, t, 1380, 900, 560, 900, [("antes", 900, EC, C["s13.a"]), ("depois", 9, EC, C["s13.b"]), ("perdeu", 891, CINZA, C["s13.c"])], larg_=120, gap=50, size=40)


# ---------------- situação 4: classificar ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C["s14.a"], 4, "a batida")
    dois_carrinhos(c, t, C["s14.b"], 1, 3, "8 m/s")
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.formula(c, "depois: B sai a 3 m/s", XE, 720, 70, "g", QC, a))
    E.frase(c, t, C["s14.e"], [("v", "g", 64, QC), ("de", "i", 66), ("A?", "g", 64, COR), ("tipo", "i", 66), ("de", "i", 66), ("colisão?", "g", 64, COR)], XE, 860, passo=0.12)
    if t >= C["s15"]:
        pausa(c, t, C, "s15")


def b_resposta4(c, t, C, b):
    sentido_mais(c, t, C["s16"], 1560, 140)
    painel(c, t, C["s16"], 120, 220, 820, 330, "antes")
    E.foco(c, t, C["s16"], 0.5, lambda a: (corpo(c, 380, 430, 61, "1 kg", a), corpo(c, 720, 430, 73, "3 kg", a, B2)))
    vel(c, t, C["s16"] + 0.3, 440, 320, 160, "8 m/s")
    painel(c, t, C["s16.b"], 980, 220, 820, 330, "depois")
    E.foco(c, t, C["s16.b"], 0.5, lambda a: (corpo(c, 1240, 430, 61, "1 kg", a), corpo(c, 1580, 430, 73, "3 kg", a, B2)))
    vel(c, t, C["s16.b"] + 0.3, 1580, 320, 120, "3 m/s")

    def s16():
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "antes: 1 · 8 = 8", XE, 680, 70, "g", QC, a))
        E.foco(c, t, C["s16.b"], 0.5, lambda a: E.formula(c, "depois: vA + 3 · 3", XE, 800, 70, "g", TINTA, a))
        E.foco(c, t, C["s16.c"], 0.5, lambda a: E.formula(c, "vA + 9 = 8  →  vA = −1", XE, 920, 70, "g", TINTA, a))
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t >= C["s16.d"]:
        vel(c, t, C["s16.d"], 1240, 320, -90, "1 m/s")
    if t < C["s17"]:
        return
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "afastamento: 3 + 1 = 4", XE, 680, 66, "g", TINTA, a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "aproximação: 8", XE, 790, 66, "g", TINTA, a))
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.formula(c, "e = f{4}{8} = 0,5", XE, 930, 76, "g", TINTA, a))
    pilula_em(c, t, C["s17.e"], "parcialmente elástica", 1350, 700, 50, TINTA2)
    E.foco(c, t, C["s17.e"] + 1.4, 0.5, lambda a: E.formula(c, "Ec: 32 J → 14 J", 1350, 860, 70, "g", EC, a, "center"))


# ---------------- situação 5: elástica ----------------
def b_questao5(c, t, C, b):
    situacao(c, t, C["s18.a"], 5, "a batida elástica")
    dois_carrinhos(c, t, C["s18.b"], 1, 2, "6 m/s")
    pilula_em(c, t, C["s18.d"], "elástica: e = 1", XE + 300, 720, 50, E.COR)
    E.frase(c, t, C["s18.e"], [("velocidades", "i", 66), ("depois?", "g", 64, COR)], XE, 880, passo=0.12)
    if t >= C["s19"]:
        pausa(c, t, C, "s19")


def b_resposta5(c, t, C, b):
    def s20():
        sentido_mais(c, t, C["s20"], 1560, 140)
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "6 = vA + 2 · vB", XE, 260, 80, "g", QC, a))
        E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "vB − vA = 6", XE, 400, 80, "g", TINTA, a))
        E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "vB = vA + 6", XE, 580, 76, "g", TINTA2, a))
        E.foco(c, t, C["s20.d"], 0.5, lambda a: E.formula(c, "6 = vA + 2 · vA + 12", XE, 720, 76, "g", TINTA, a))
        E.foco(c, t, C["s20.e"], 0.5, lambda a: E.formula(c, "3 · vA = −6  →  vA = −2", XE, 880, 80, "g", COR, a))
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    sentido_mais(c, t, C["s21"] - 0.4, 1560, 140)
    painel(c, t, C["s21"], 120, 220, 1680, 330, "depois")
    E.foco(c, t, C["s21"], 0.5, lambda a: (corpo(c, 700, 430, 61, "1 kg", a), corpo(c, 1100, 430, 67, "2 kg", a, B2)))
    vel(c, t, C["s21.a"], 1100, 320, 220, "4 m/s")
    vel(c, t, C["s21.b"], 700, 320, -140, "2 m/s")
    E.foco(c, t, C["s21.b"] + 0.4, 0.4, lambda a: E.escreve(c, "rebatido", 300, 340, 50, "i", TINTA2, a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.formula(c, "Ec antes: f{1 · 6^2}{2} = 18 J", XE, 700, 64, "g", EC, a))
    E.foco(c, t, C["s21.c"] + 1.4, 0.5, lambda a: E.formula(c, "Ec depois: f{1 · 2^2}{2} + f{2 · 4^2}{2} = 2 + 16 = 18 J", XE, 860, 64, "g", EC, a))
    E.foco(c, t, C["s21.d"], 0.4, lambda a: E.selo(c, 1720, 840, 60, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s22.a", "força média = f{I}{Δt}"), ("s22.b", "do repouso: razão inversa das massas"), ("s22.c", "grudou: inelástica, perde energia"),
                 ("s22.d", "elástica: duas equações e confira Ec"))
        for i, (k, s) in enumerate(itens):
            y = 340 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 66, "g", TINTA, a))
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], ps("trilha completa:", "i", 70, TINTA2), XE, 230, passo=0.1)
    E.frase(c, t, C["s23"] + 1.2, [("trabalho,", "g", 70), ("energia", "g", 70), ("e", "i", 70), ("colisões", "g", 70, COR)], XE, 330, passo=0.12)
    E.frase(c, t, C["s23.a"], ps("na sequência:", "i", 64, TINTA2), XE, 500, passo=0.1)
    E.frase(c, t, C["s23.a"] + 0.6, [("torque", "g", 110, COR), ("e", "i", 100), ("alavancas", "g", 110, COR)], XE, 640)
    E.frase(c, t, C["s23.b"], ps("a chave de roda comprida", "i", 60, TINTA2), XE, 760, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5,
              resposta5=b_resposta5, fim=b_fim)
