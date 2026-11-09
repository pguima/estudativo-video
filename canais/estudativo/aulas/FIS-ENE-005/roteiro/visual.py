"""Visual — Estudativo · FIS-ENE-005: conservação da energia e energia dissipada.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001). Aqui as barras_energia acompanham o carrinho no trilho: potencial laranja, cinética petróleo,
dissipada cinza, e a linha tracejada do total fica parada enquanto não há atrito.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-005_conservacao_da_energia_e_energia_dissipada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("conserva", "conta", "atalho", "dissipada", "erro", "questao", "fim"))
BR = "#FFFFFF"
EC, EPOT, EDIS = F.VEL, E.COR, CINZA

# todas as contas da aula
ok = lambda a, b: abs(a - b) < 1e-9
assert math.sqrt(2 * 10 * 20) == 20 and 10 * 20 == 200 and 2 * 200 == 400 and ok(math.sqrt(2 * 10 * 0.45), 3) and 20 ** 2 / (2 * 10) == 20
assert 30 * 10 * 5 == 1500 and 30 * 36 / 2 == 540 and 1500 - 540 == 960
assert ok(math.sqrt(2 * 10 * 3.2), 8) and ok(20 * 3.2, 64) and ok(50 * 10 * 3.2, 1600) and 50 * 36 / 2 == 900 and 1600 - 900 == 700


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


# ---------------- desenhos desta aula ----------------
class Trilho:
    """descida suave de (x0, ytop) até (x1, ybot); u de 0 (alto) a 1 (embaixo); h(u) = fração da altura"""

    def __init__(s, x0, x1, ytop, ybot):
        s.x0, s.x1, s.ytop, s.ybot = x0, x1, ytop, ybot

    def ponto(s, u):
        return lerp(s.x0, s.x1, u), lerp(s.ytop, s.ybot, (1 - math.cos(math.pi * u)) / 2)

    def h(s, u):
        return 1 - (1 - math.cos(math.pi * u)) / 2


def trilho(c, t, t0, T, a=1.0, extra=180):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    pts = [T.ponto(i / 60) for i in range(61)] + [(T.x1 + extra, T.ybot)]
    F.poli(c, [(T.x0 - 120, T.ytop)] + pts, ease_io(prog(t, t0, 0.8)), TINTA, q, 8)
    for i in range(0, 61, 6):
        x, y = T.ponto(i / 60)
        M.line(c, x, y + 6, x, max(y + 6, T.ybot + 30), TINTA, 0.18 * q, 4)
    F.chao(c, T.x0 - 140, T.x1 + extra + 40, T.ybot + 30, q)


def carro_trilho(c, T, u, a=1.0, r=34, cor=None):
    x, y = T.ponto(u)
    E.bola(c, x, y - r - 4, r, cor or E.COR, a)


def escorregador(c, t, t0, x, yb, alto, base):
    """escada à esquerda e rampa reta descendo para a direita"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    F.chao(c, x - 120, x + base + 200, yb, q)
    M.line(c, x, yb, x, yb - alto, TINTA, q, 8)
    M.line(c, x - 70, yb, x - 70, yb - alto + 20, TINTA, q, 6)
    for k in range(1, 6):
        yy = yb - alto * k / 6
        M.line(c, x - 70, yy, x, yy, TINTA, q, 5)
    M.line(c, x, yb - alto, x + base, yb - 20, E.COR, q, 14)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    T = Trilho(300, 1100, 330, 860)

    def um():
        trilho(c, t, C["s01.a"], T)
        u = ease_io(prog(t, C["s01.a"] + 1.0, 2.6))
        E.foco(c, t, C["s01.a"] + 0.6, 0.4, lambda a: carro_trilho(c, T, u, a))
        if t >= C["s01.a"] + 0.6:
            M.line(c, 1340, 330, 1340, 860, TINTA, ep(t, C["s01.a"] + 0.6, 0.4), 4, dash=E.TRACO)
            M.line(c, 1180, 330, 1400, 330, TINTA2, 0.6 * ep(t, C["s01.a"] + 0.6, 0.4), 3, dash=E.TRACO)
        E.foco(c, t, C["s01.a"] + 0.9, 0.4, lambda a: F.medida(c, 20, "m", 1370, 460, 70, TINTA, a))
        E.frase(c, t, C["s01.a"], [("parte", "i", 64), ("do", "i", 64), ("repouso", "g", 60)], 1260, 220, passo=0.12)
        E.frase(c, t, C["s01.b"], [("v", "g", 90, EC), ("=", "g", 90), ("?", "g", 90, COR)], 1560, 920, passo=0.12)
        pilula_em(c, t, C["s01.c"], "não depende da massa", 1640, 620, 44, TINTA)
        pilula_em(c, t, C["s01.d"], "nem do formato do trilho", 1640, 720, 44, TINTA)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 320 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
        itens = (("s02.a", "começo = fim", 1.4, True), ("s02.b", "atalho da velocidade", 0, False), ("s02.c", "energia perdida", 0, False))
        for i, (k, s, dt, forte) in enumerate(itens):
            y = 450 + i * 160
            E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 70, COR if forte else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "a energia cinética:", "Ec = f{m · v^2}{2}", None),
                              ("s03.c", "a energia potencial:", "Ep = m · g · h", None),
                              ("s03.d", "raiz quadrada:", "r{400} = 20", None)))


# ---------------- conservação ----------------
def b_conserva(c, t, C, b):
    T = Trilho(250, 1000, 330, 860)
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], [("Ec", "g", 84, EC), ("+", "g", 84), ("Ep", "g", 84, EPOT), ("=", "g", 84), ("energia", "i", 90), ("mecânica", "g", 84)], XE, 260, passo=0.14)
        E.frase(c, t, C["s04.b"], ps("sem atrito e sem resistência do ar:", "i", 66), XE, 460, passo=0.1)
        E.frase(c, t, C["s04.c"], [("ela", "i", 84), ("se", "i", 84), ("conserva", "g", 84, COR)], XE, 600, passo=0.12)
        E.frase(c, t, C["s04.d"], ps("muda de forma; o", "i", 66) + [("total", "g", 62), ("não", "g", 62), ("muda", "g", 62)], XE, 760, passo=0.1)
        return
    trilho(c, t, C["s05"], T)
    k1, k2 = C["s05.b"], C["s05.c"]
    u = 0 if t < k1 else (0.5 * ease_io(prog(t, k1, 1.6)) if t < k2 else 0.5 + 0.5 * ease_io(prog(t, k2, 1.4)))
    E.foco(c, t, C["s05"] + 0.4, 0.4, lambda a: carro_trilho(c, T, u, a))
    h = T.h(u)
    barras_energia(c, t, 1350, 860, 520, 1, [("Ep", h, EPOT, C["s05.a"]), ("Ec", 1 - h, EC, C["s05.a"])], larg_=170, gap=90, size=56,
                   total=1, t_total=C["s05.d"], fmt=lambda v: "")
    E.foco(c, t, C["s05.d"] + 0.3, 0.4, lambda a: E.escreve(c, "total", 1700, 320, 50, "i", TINTA, a))


# ---------------- a conta ----------------
def b_conta(c, t, C, b):
    def s06_07():
        E.frase(c, t, C["s06"], ps("o carrinho, de", "i", 66) + [("20 m", "g", 62)], XE, 200, passo=0.1)
        E.foco(c, t, C["s06.a"], 0.5, lambda a: E.formula(c, "alto:  m · 10 · 20", XE, 360, 80, "g", EPOT, a))
        E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, "embaixo:  f{m · v^2}{2}", XE + 900, 360, 80, "g", EC, a))
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.formula(c, "m · 10 · 20 = f{m · v^2}{2}", W / 2, 620, 110, "g", TINTA, a, "center"))
        if t >= C["s07.a"]:
            for x0, x1 in ((W / 2 - 430, W / 2 - 350), (W / 2 + 205, W / 2 + 285)):
                M.line(c, x0, 640, x1, 540, E.COR, 1.0, 8, progress=ep(t, C["s07.a"], 0.35))
        troca(c, t, [(C["s07.b"], "f{v^2}{2} = 200"), (C["s07.c"], "v^2 = 400")], lambda s, a: E.formula(c, s, W / 2 - 300, 880, 96, "g", TINTA, a, "center"))
        bola_txt(c, t, C["s07.d"], "20 m/s", W / 2 + 350, 860, 120, 58, EC)
    E.saida(c, t, C["s08"] - 0.1, s06_07)
    if t < C["s08"]:
        return
    T = Trilho(250, 900, 360, 760)
    trilho(c, t, C["s08"], T)
    u = 0.42
    x, y = T.ponto(u)
    E.foco(c, t, C["s08"] + 0.3, 0.4, lambda a: carro_trilho(c, T, u, a))
    dx, dy = T.ponto(u + 0.01)[0] - x, T.ponto(u + 0.01)[1] - y
    ang = math.degrees(math.atan2(-dy, dx))
    F.forca(c, t, C["s08.a"], (x, y - 38), ang + 90, 170, "N", size=50)
    F.vetor(c, t, C["s08.a"] + 0.3, (x + 50, y + 30), (x + 50 + 160 * math.cos(math.radians(ang)), y + 30 - 160 * math.sin(math.radians(ang))), "v", None, EC, 7, lado=-1, size=44)
    E.frase(c, t, C["s08.a"], [("normal", "g", 64), ("perpendicular", "g", 60, COR), ("ao", "i", 68), ("caminho", "i", 68)], 1050, 360, passo=0.12)
    pilula_em(c, t, C["s08.b"], "τ = 0", 1250, 470, 52, TINTA2)
    E.frase(c, t, C["s08.c"], ps("só conta a", "i", 64) + [("diferença", "g", 60), ("de", "i", 64), ("altura", "g", 60, COR)], 1050, 620, passo=0.1)
    if t >= C["s08.d"]:
        F.pendulo(c, t, C["s08.d"], 1500, 720, 230, F.oscila(t, C["s08.d"], 35, 2.2), r=30, amp=35)
        E.frase(c, t, C["s08.d"] + 0.4, ps("o fio também:", "i", 58) + [("τ = 0", "g", 54, TINTA2)], 1050, 1000, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s09():
        E.frase(c, t, C["s09"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s09"] + 1.0, ps("saindo do repouso, sem atrito", "i", 56, CLARO), W / 2, 270, "center", 0.1)
        E.foco(c, t, C["s09.a"], 0.6, lambda a: (E.bola(c, 620, 540, 240 * ease_back(prog(t, C["s09.a"], 0.6)), a=a),
                                                 E.formula(c, "v = r{2 · g · h}", 620, 565, 70, "g", BR, a, "center")))
        if t >= C["s09.b"]:
            F.pendulo(c, t, C["s09.b"], 1350, 380, 330, F.oscila(t, C["s09.b"], 40, 2.4), r=34, amp=40, escuro=True)
        E.foco(c, t, C["s09.b"] + 0.6, 0.4, lambda a: E.formula(c, "h = 45 cm = 0,45 m", 1350, 870, 50, "b", CLARO, a, "center"))
        E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "v = r{2 · 10 · 0,45} = r{9}", 620, 880, 70, "g", BR, a, "center"))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "= 3 m/s", 620, 1000, 76, "g", CLARO, a, "center"))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("a", "i", 76, CLARO), ("massa", "g", 76, BR), ("sempre", "i", 76, CLARO), ("corta", "g", 76, BR)], W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s10.b"], ps("ao contrário:", "i", 66, CLARO), W / 2, 420, "center", 0.12)
    E.foco(c, t, C["s10.b"] + 0.6, 0.5, lambda a: E.formula(c, "h = f{v^2}{2 · g} = f{20^2}{20} = 20 m", W / 2, 560, 80, "g", BR, a, "center"))
    E.frase(c, t, C["s10.c"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("já começa andando, ou tem atrito", "i", 64, CLARO), W / 2, 820, "center", 0.1)
    E.frase(c, t, lerp(C["s10.c"], C["s10.end"], 0.6), ps("aí, iguale as energias com todos os termos", "i", 58, CLARO), W / 2, 930, "center", 0.1)


# ---------------- dissipada ----------------
def b_dissipada(c, t, C, b):
    def s11():
        E.frase(c, t, C["s11"], [("e", "i", 84), ("com", "i", 84), ("atrito?", "g", 84, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s11.a"], ps("a força do esfregar", "i", 64) + ps("(outra aula)", "i", 54, TINTA2), XE, 360, passo=0.1)
        E.frase(c, t, C["s11.b"], ps("transforma energia em", "i", 64) + [("calor", "g", 60, TINTA2)], XE, 470, passo=0.1)
        E.frase(c, t, C["s11.c"], [("energia", "g", 76), ("dissipada", "g", 76, TINTA2)], XE, 660, passo=0.12)
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "E dissipada = E começo − E fim", XE, 820, 70, "g", TINTA, a))
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    x, yb = 220, 900
    escorregador(c, t, C["s12"], x, yb, 420, 560)
    p = ease_io(prog(t, C["s12.a"] + 0.5, 2.0))
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.bola(c, lerp(x + 30, x + 560, p), lerp(yb - 450, yb - 50, p), 34, TINTA2, a))
    E.foco(c, t, C["s12.a"] + 0.3, 0.4, lambda a: E.formula(c, "30 kg · 5 m", x + 120, yb - 470, 50, "g", TINTA, a))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: F.medida(c, 6, "m/s", x + 560, yb - 120, 56, EC, a, "center"))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "alto: 30 · 10 · 5 = 1.500 J", 960, 230, 60, "g", EPOT, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "embaixo: f{30 · 36}{2} = 540 J", 960, 360, 60, "g", EC, a))
    itens = [("alto", 1500, EPOT, C["s12.c"]), ("embaixo", 540, EC, C["s12.d"])]
    if t >= C["s13.b"]:
        itens.append(("calor", 960, EDIS, C["s13.b"]))
    barras_energia(c, t, 1000, 900, 400, 1500, itens, larg_=170, gap=70, size=46, total=1500, t_total=C["s13.a"])
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "1.500 − 540 = 960 J", XE, 1010, 60, "g", TINTA, a))
    pilula_em(c, t, C["s13.c"], "a energia não sumiu: virou calor", 1350, 1010, 42, TINTA2)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], ps("o mais pesado chega antes?", "i", 70), XE + 480, 200, passo=0.12)
    for i, (m, r, k) in enumerate(((100, 34, "s14.b"), (500, 52, "s14.b"))):
        T = Trilho(250 + i * 840, 850 + i * 840, 380, 760)
        trilho(c, t, C[k] + 0.3 * i, T, extra=60)
        u = ease_io(prog(t, C["s15.a"] - 0.2, 2.0)) if t >= C["s15.a"] - 0.2 else 0
        E.foco(c, t, C[k] + 0.3 * i, 0.4, lambda a, T=T, r=r, u=u: carro_trilho(c, T, u, a, r))
        E.foco(c, t, C[k] + 0.6 + 0.3 * i, 0.4, lambda a, m=m, i=i: F.medida(c, m, "kg", 250 + i * 840, 320, 60, TINTA, a))
        bola_txt(c, t, C["s15.b"] + 0.2 * i, "20 m/s", 760 + i * 840, 920, 90, 46, EC)
    pilula_em(c, t, C["s14.c"], "500 kg mais veloz?", 1620, 300, 44, ERRADO) if t < C["s15"] else None
    E.frase(c, t, C["s15.a"], ps("a massa", "i", 64) + [("cortou", "g", 60, COR)], W / 2, 1050, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], [("skatista", "i", 72), ("50 kg,", "g", 68), ("do", "i", 72), ("repouso", "i", 72)], XE, 360, passo=0.12)
    E.frase(c, t, C["s16.b"], [("rampa", "i", 72), ("de", "i", 72), ("3,2 m", "g", 68, COR), ("de", "i", 72), ("altura", "i", 72)], XE, 470, passo=0.12)
    E.frase(c, t, C["s16.c"], [("sem", "i", 70), ("atrito:", "i", 70), ("v", "g", 66, EC), ("=", "g", 66), ("?", "g", 66, COR)], XE, 650, passo=0.12)
    E.frase(c, t, C["s16.d"], [("chega", "i", 70), ("a", "i", 70), ("6 m/s:", "g", 66, EC), ("dissipada?", "g", 66, TINTA2)], XE, 770, passo=0.12)
    if t < C["s17"]:
        T = Trilho(1150, 1700, 400, 800)
        trilho(c, t, C["s16.a"], T, extra=100)
        E.foco(c, t, C["s16.a"] + 0.4, 0.4, lambda a: carro_trilho(c, T, 0, a, 34))
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "v = r{2 · 10 · 3,2}", W / 2, 360, 120, "g", TINTA, a, "center"))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "= r{64}", W / 2, 600, 120, "g", TINTA, a, "center"))
        bola_txt(c, t, C["s18.c"], "8 m/s", W / 2, 850, 130, 70, EC)
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "alto: 50 · 10 · 3,2 = 1.600 J", XE, 280, 64, "g", EPOT, a))
    E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "embaixo: f{50 · 36}{2} = 900 J", XE, 450, 64, "g", EC, a))
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "1.600 − 900 =", XE, 680, 80, "g", TINTA, a))
    bola_txt(c, t, C["s19.c"] + 0.6, "700 J", XE + 700, 650, 110, 64, TINTA2)
    itens = [("alto", 1600, EPOT, C["s19.a"]), ("embaixo", 900, EC, C["s19.b"])]
    if t >= C["s19.c"]:
        itens.append(("calor", 700, EDIS, C["s19.c"]))
    barras_energia(c, t, 1180, 900, 480, 1600, itens, larg_=150, gap=60, size=44, total=1600, t_total=C["s19.c"])


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", "sem atrito: E começo = E fim"), ("s20.b", "do repouso: v = r{2 · g · h}"), ("s20.c", "dissipada = E começo − E fim"))
        for i, (k, s) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 70, "g", TINTA, a))
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("praticando", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s21.a"] + 0.7, ps("trabalho, potência, rendimento e energia", "i", 60, TINTA2), XE, 540, passo=0.1)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, conserva=b_conserva, conta=b_conta, atalho=b_atalho, dissipada=b_dissipada,
              erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
