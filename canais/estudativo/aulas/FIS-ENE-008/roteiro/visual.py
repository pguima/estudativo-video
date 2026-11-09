"""Visual — Estudativo · FIS-ENE-008: conservação da quantidade de movimento.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001): corpos = esferas laranja com a massa dentro (peça corpo); velocidade = seta petróleo com o valor;
painel "antes" | "depois" (peça painel); sentido positivo com sentido_mais; forças internas = setas laranja opostas.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-008_conservacao_da_quantidade_de_movimento.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "empurrao", "recuo", "explosao", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
QC = F.VEL

# todas as contas da aula
ok = lambda a, b: abs(a - b) < 1e-9
assert 40 * 2 == 80 and -80 / 80 == -1 and ok(0.01 * 400, 4) and -4 / 4 == -1 and 3 * 10 == 30 and 2 * 20 == 40 and 30 - 40 == -10 and 0 - 40 == -40
assert ok(4 / 0.01, 400) and 400 / 400 == 1 and 80 / 40 == 2 and 3 * 6 == 18 and ok(-18 / 90, -0.2) and 90 / 3 == 30 and 6 / 30 == 0.2


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


def espingarda(c, x, y, s, a=1.0):
    """espingarda deitada, cano para a direita; (x, y) = meio da coronha"""
    if a <= 0:
        return
    M.rrect(c, x - s * 0.5, y - s * 0.12, s * 0.6, s * 0.24, s * 0.06, "#8B5E3C", a)
    M.rrect(c, x, y - s * 0.07, s * 1.3, s * 0.1, s * 0.03, TINTA, a)
    M.rrect(c, x + s * 0.1, y + s * 0.02, s * 0.18, s * 0.16, s * 0.03, TINTA2, a)


def explosao(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    for k in range(10):
        g = math.radians(k * 36 + 18)
        M.line(c, cx + math.cos(g) * r * 0.6, cy + math.sin(g) * r * 0.6, cx + math.cos(g) * r, cy + math.sin(g) * r, "#FFB020", a, 8)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        y = 560
        recua = ease_out(prog(t, C["s01.a"] + 0.8, 0.5))
        E.foco(c, t, C["s01.a"], 0.5, lambda a: espingarda(c, 760 - 90 * recua, y, 520, a))
        if t >= C["s01.a"] + 0.8:
            q = ep(t, C["s01.a"] + 0.8, 0.2)
            bx = lerp(1450, 1850, ease_out(prog(t, C["s01.a"] + 0.8, 0.6)))
            M.rrect(c, bx, y - 22, 50, 20, 8, TINTA, q)
            explosao(c, 1460, y - 12, 70, q * (1 - ep(t, C["s01.a"] + 1.2, 0.6)))
            vel(c, t, C["s01.a"] + 1.4, 600, y + 160, -260, None)
            E.foco(c, t, C["s01.a"] + 1.6, 0.4, lambda a: E.escreve(c, "coice", 380, y + 270, 64, "g", COR, a))
        E.frase(c, t, C["s01.b"], ps("nada de fora empurra para trás", "i", 62, TINTA2), XE, 250, passo=0.1)
        E.frase(c, t, C["s01.c"], [("de", "i", 90), ("onde", "i", 90), ("vem?", "g", 90, COR)], XE, 920, passo=0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 320 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula:", "i", 80, TINTA), XE, 250, passo=0.14)
        E.frase(c, t, C["s02.a"] + 1.2, [("Q antes = Q depois", "g", 76, COR)], XE, 360)
        itens = (("s02.b", "empurrões"), ("s02.c", "recuos"), ("s02.d", "explosões"))
        for i, (k, s) in enumerate(itens):
            y = 520 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "quantidade de movimento:", "Q = m · v", None),
                              ("s03.c", "o impulso:", "I = ΔQ", None),
                              ("s03.d", "equação do 1º grau:", "80 · v = −80 → v = −1", None)))


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    y = 620

    def s04_05():
        if t >= C["s04.a"]:
            M.line(c, 300, y + 90, 1620, y + 90, "#9FC9DD", ep(t, C["s04.a"], 0.4), 8)
        E.foco(c, t, C["s04.a"], 0.5, lambda a: corpo(c, 820, y, 90, "A", a))
        E.foco(c, t, C["s04.a"] + 0.2, 0.5, lambda a: corpo(c, 1100, y, 90, "B", a))
        F.vetor(c, t, C["s04.b"], (1100 - 90, y - 150), (1100 + 160, y - 150), "F", None, E.COR, 10, size=50)
        F.vetor(c, t, C["s04.c"], (820 + 90, y - 150), (820 - 160, y - 150), "F", None, E.COR, 10, size=50)
        E.frase(c, t, C["s04.a"], ps("patinadores parados no gelo", "i", 66), XE, 230, passo=0.1)
        pilula_em(c, t, C["s04.d"], "terceira lei de Newton (outra aula)", W / 2, 920, 46, TINTA2)
        if t >= C["s05"]:
            E.frase(c, t, C["s05.a"], ps("mesmo tempo,", "i", 64) + [("impulsos", "g", 60, COR), ("opostos", "g", 60, COR)], XE, 350, passo=0.1)
            F.vetor(c, t, C["s05.c"], (820, y + 170), (520, y + 170), "ΔQ", None, QC, 12, lado=1, size=46)
            F.vetor(c, t, C["s05.c"] + 0.3, (1100, y + 170), (1400, y + 170), "ΔQ", None, QC, 12, lado=1, size=46)
            pilula_em(c, t, C["s05.d"], "a soma não muda", 1600, 350, 50, QC)
    E.saida(c, t, C["s06"] - 0.1, s04_05)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"], 0.6, lambda a: E.pilula(c, "Q antes = Q depois", W / 2, 380, 96, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s06.b"], [("isolado:", "g", 60), ("nada", "i", 64), ("de", "i", 64), ("fora", "i", 64), ("empurra", "i", 64), ("para", "i", 64), ("os", "i", 64), ("lados", "i", 64)],
            W / 2, 720, "center", 0.1)
    sentido_mais(c, t, C["s07.a"], 760, 860)
    E.frase(c, t, C["s07.b"], [("direita:", "i", 60), ("+", "g", 60, COR)], 1100, 880, passo=0.1)
    E.frase(c, t, C["s07.c"], [("esquerda:", "i", 60), ("−", "g", 60, F.NEG)], 1100, 970, passo=0.1)


# ---------------- empurrão ----------------
def b_empurrao(c, t, C, b):
    sentido_mais(c, t, C["s08"], 1560, 140)
    painel(c, t, C["s08.a"], 120, 260, 820, 420, "antes")
    painel(c, t, C["s08.b"], 980, 260, 820, 420, "depois")
    E.foco(c, t, C["s08.a"], 0.5, lambda a: (corpo(c, 430, 520, 100, "80", a), corpo(c, 640, 540, 70, "40", a)))
    E.foco(c, t, C["s08.a"] + 0.6, 0.4, lambda a: E.escreve(c, "v = 0", 460, 380, 50, "g", TINTA2, a))
    E.foco(c, t, C["s08.b"], 0.5, lambda a: (corpo(c, 1240, 520, 100, "80", a), corpo(c, 1560, 540, 70, "40", a)))
    vel(c, t, C["s08.b"] + 0.3, 1560, 420, 200, "2 m/s")
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "Q antes = 0", XE, 820, 70, "g", QC, a))
    if t >= C["s09"]:
        vel(c, t, C["s09.d"] - 0.6, 1240, 400, -110, "1 m/s")
    E.foco(c, t, C["s09.a"], 0.5, lambda a: E.formula(c, "40 · 2 + 80 · v = 0", 900, 820, 70, "g", TINTA, a))
    troca(c, t, [(C["s09.b"], "80 · v = −80"), (C["s09.c"], "v = −1 m/s")], lambda s, a: E.formula(c, s, 900, 960, 70, "g", TINTA, a))
    pilula_em(c, t, C["s09.d"], "para a esquerda", 1600, 940, 46, F.NEG)


# ---------------- recuo ----------------
def b_recuo(c, t, C, b):
    sentido_mais(c, t, C["s10"], 1560, 140)
    E.frase(c, t, C["s10.a"], [("o", "i", 70), ("coice", "g", 66, COR), ("é", "i", 70), ("a", "i", 70), ("mesma", "i", 70), ("conta", "g", 66)], XE, 200, passo=0.12)
    y = 470
    rec = ease_out(prog(t, C["s11.a"], 0.6)) if t >= C["s11.a"] else 0
    E.foco(c, t, C["s10.b"], 0.5, lambda a: espingarda(c, 700 - 80 * rec, y, 500, a))
    E.foco(c, t, C["s10.b"] + 0.3, 0.4, lambda a: E.escreve(c, "4 kg", 420, y - 110, 56, "g", TINTA, a))
    if t >= C["s10.c"]:
        bx = lerp(1360, 1700, ease_out(prog(t, C["s10.c"], 0.6)))
        M.rrect(c, bx, y - 20, 50, 20, 8, TINTA, 1.0)
        E.foco(c, t, C["s10.c"] + 0.2, 0.4, lambda a: E.escreve(c, "10 g", 1600, y - 70, 50, "g", TINTA, a))
        vel(c, t, C["s10.c"] + 0.3, 1450, y + 90, 300, "400 m/s")
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.formula(c, "10 g = 0,01 kg", XE, 760, 64, "g", TINTA2, a))
    E.foco(c, t, C["s10.e"], 0.5, lambda a: E.formula(c, "Q bala = 0,01 · 400 = +4", XE, 880, 64, "g", QC, a))
    if t >= C["s11"]:
        vel(c, t, C["s11.a"], 500, y + 120, -200, "?")
    E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "4 · v = −4", 1050, 760, 70, "g", TINTA, a))
    bola_txt(c, t, C["s11.c"], "−1 m/s", 1600, 800, 110, 50, QC)
    E.frase(c, t, C["s11.d"], ps("pouca massa, rápida · muita massa, devagar", "i", 52, TINTA2), W / 2, 1020, "center", 0.08)


# ---------------- explosão ----------------
def b_explosao(c, t, C, b):
    sentido_mais(c, t, C["s12"], 1560, 140)
    painel(c, t, C["s12.a"], 120, 240, 760, 420, "antes")
    painel(c, t, C["s12.b"], 940, 240, 860, 420, "depois")
    E.foco(c, t, C["s12.a"], 0.5, lambda a: corpo(c, 420, 500, 100, "3", a))
    vel(c, t, C["s12.a"] + 0.3, 540, 500, 220, "10 m/s")
    E.foco(c, t, C["s12.b"], 0.4, lambda a: explosao(c, 1370, 500, 110, a * (1 - ep(t, C["s12.b"] + 0.8, 0.5))))
    E.foco(c, t, C["s12.b"] + 0.4, 0.5, lambda a: (corpo(c, 1530, 500, 85, "2", a), corpo(c, 1200, 520, 60, "1", a)))
    vel(c, t, C["s12.c"], 1630, 400, 140, "20 m/s")
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "v = ?", 1150, 400, 56, "g", COR, a, "center")) if t < C["s13.d"] else None
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "antes: 3 · 10 = 30", XE, 780, 64, "g", QC, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "depois: 2 · 20 + 1 · v", 900, 780, 64, "g", TINTA, a))
    troca(c, t, [(C["s13.c"], "40 + v = 30"), (C["s13.d"], "v = −10 m/s")], lambda s, a: E.formula(c, s, 900, 920, 70, "g", TINTA, a))
    if t >= C["s13.d"]:
        vel(c, t, C["s13.d"], 1150, 400, -150, "10 m/s")
    pilula_em(c, t, C["s13.e"], "para a esquerda", XE + 260, 920, 46, F.NEG)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], ps("explosão sempre do zero?", "i", 70), XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "40 + v = 0", 560, 470, 100, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "v = −40 m/s", 560, 660, 100, "g", ERRADO, a, "center"))
    if t >= C["s15.a"]:
        E.risco(c, 300, 690, 820, 560, t, C["s15.a"], largura=12)
    if t >= C["s15"]:
        M.line(c, 980, 300, 980, 950, FIO, ep(t, C["s15"], 0.4), 3)
    E.frase(c, t, C["s15.a"], ps("já andava antes", "i", 66), 1420, 380, "center", 0.12)
    E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "Q antes = 30", 1420, 560, 90, "g", CERTO, a, "center"))
    E.foco(c, t, C["s15.b"] + 0.8, 0.5, lambda a: E.formula(c, "40 + v = 30", 1420, 720, 90, "g", CERTO, a, "center"))
    E.frase(c, t, C["s15.c"], [("zero", "g", 60), ("só", "i", 64), ("se", "i", 64), ("começa", "i", 64), ("parado", "g", 60, COR)], 1420, 900, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        E.frase(c, t, C["s16"], ps("agora, o atalho: começou parado?", "i", 70, CLARO), W / 2, 160, "center", 0.1)
        E.frase(c, t, C["s16.a"], [("velocidades", "g", 70, BR), ("na", "i", 72, CLARO), ("razão", "i", 72, CLARO), ("inversa", "g", 70, BR), ("das", "i", 72, CLARO), ("massas", "g", 70, BR)],
                W / 2, 300, "center", 0.12)
        for i, (k, l1, l2) in enumerate((("s16.b", "massa × 2", "velocidade ÷ 2"), ("s16.c", "massa × 400", "velocidade ÷ 400"))):
            y = 520 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, l1=l1, y=y: E.formula(c, l1, 300, y, 76, "g", BR, a))
            E.foco(c, t, C[k] + 0.4, 0.4, lambda a, y=y: F.seta(c, 900, y - 26, 1060, y - 26, CLARO, a, 8))
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, l2=l2, y=y: E.formula(c, l2, 1110, y, 76, "g", CLARO, a))
        E.foco(c, t, C["s16.c"] + 2.4, 0.5, lambda a: E.formula(c, "f{400}{400} = 1 m/s", W / 2, 960, 70, "g", BR, a, "center"))
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17.a"], [("m · v", "g", 80, BR)] + ps("igual dos dois lados", "i", 72, CLARO), W / 2, 330, "center", 0.12)
    E.frase(c, t, C["s17.b"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("o sistema já andava antes", "i", 64, CLARO), W / 2, 620, "center", 0.1)
    E.frase(c, t, lerp(C["s17.b"], C["s17.end"], 0.6), ps("aí, monte a equação com os sinais", "i", 60, CLARO), W / 2, 740, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s18.a"], [("astronauta", "i", 70), ("90 kg,", "g", 66), ("parado", "i", 70)], XE, 360, passo=0.12)
    E.frase(c, t, C["s18.b"], [("ferramenta", "i", 70), ("3 kg", "g", 66), ("a", "i", 70), ("6 m/s", "g", 66, QC)], XE, 470, passo=0.12)
    E.frase(c, t, C["s18.c"], [("velocidade", "i", 70), ("e", "i", 70), ("sentido", "i", 70), ("do", "i", 70), ("astronauta?", "g", 66, COR)], XE, 650, passo=0.12)
    if t < C["s19"]:
        E.foco(c, t, C["s18.a"], 0.5, lambda a: corpo(c, 1300, 560, 120, "90", a))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: corpo(c, 1560, 560, 50, "3", a))
        vel(c, t, C["s18.b"] + 0.3, 1560, 460, 220, "6 m/s")
    else:
        E.relogio(c, t, C["s19.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    sentido_mais(c, t, C["s20"], 1560, 140)

    def s20():
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "antes: 0", XE, 300, 76, "g", QC, a))
        E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "3 · 6 + 90 · v = 0", XE, 470, 90, "g", TINTA, a))
        E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "90 · v = −18", XE, 640, 90, "g", TINTA, a))
        bola_txt(c, t, C["s20.d"], "−0,2 m/s", 1450, 560, 150, 58, QC)
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.foco(c, t, C["s21.a"], 0.5, lambda a: corpo(c, 900, 420, 120, "90", a))
    E.foco(c, t, C["s21.a"], 0.5, lambda a: corpo(c, 1250, 420, 50, "3", a))
    vel(c, t, C["s21.a"] + 0.3, 1250, 320, 240, "6 m/s")
    vel(c, t, C["s21.a"] + 0.6, 900, 280, -110, "0,2 m/s")
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.formula(c, "90 = 30 · 3", XE, 760, 80, "g", TINTA2, a))
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.formula(c, "f{6}{30} = 0,2 m/s", 900, 780, 90, "g", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s22.a", "nada de fora: Q antes = Q depois"), ("s22.b", "sentido positivo e sinal"), ("s22.c", "do repouso: razão inversa das massas"))
        for i, (k, s) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 68, "g", TINTA, a))
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], [("colisões", "g", 130, COR)], XE, 430)
    E.frase(c, t, C["s23.b"], ps("elástica, parcial ou inelástica", "i", 64, TINTA2), XE, 560, passo=0.1)
    E.foco(c, t, C["s23.a"], 0.5, lambda a: (corpo(c, 450, 800, 70, "", a), corpo(c, 640, 800, 70, "", a, F.VEL)))
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, empurrao=b_empurrao, recuo=b_recuo, explosao=b_explosao, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
