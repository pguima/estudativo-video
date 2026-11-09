"""Visual — Estudativo · FIS-ENE-003: energia cinética e teorema do trabalho.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001). Energia cinética = barra petróleo (F.VEL), a cor da velocidade (barras_energia).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-003_energia_cinetica_e_teorema_do_trabalho.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("cinetica", "quadrado", "teorema", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
EC = F.VEL

# todas as contas da aula
Ec = lambda m, v: m * v * v / 2
assert Ec(2, 3) == 9 and Ec(1000, 10) == 50000 and Ec(1000, 20) == 200000 and Ec(1000, 20) / Ec(1000, 10) == 4
assert 200000 / 40 == 5000 and Ec(2, 20) - Ec(2, 10) == 300 and Ec(2, 20 - 10) == 100 and 40 * 4 == 160
assert Ec(4, 3) == 18 and Ec(4, 5) == 50 and 50 - 18 == 32 and 32 / 8 == 4


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
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 56, COR)], x + 44, y + 160)
        if l3:
            E.foco(c, t, C[k] + 0.9, 0.5, lambda a, l3=l3, y=y: E.formula(c, l3, x + 44, y + 240, 46, "b", TINTA2, a))
        if i < len(desenhos) and desenhos[i]:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y, h=h: desenhos[i](a, x + w - 160, y + 105))
        y += h + gap
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.7), ps("faltou alguma?", "i", 54, COR) + ps("procure no canal", "i", 54),
            820, 1000, "left", 0.12)


# ---------------- desenhos desta aula ----------------
def caminho(c, t, t0, x0, x1, y, rot="d", modulo=None, lado=-1):
    """seta petróleo do deslocamento, logo abaixo do chão"""
    F.vetor(c, t, t0, (x0, y), (x1, y), rot, modulo, F.VEL, 8, lado=lado, size=50)


def boliche(c, t, t0, x, y):
    """bola rolando até os pinos, que tombam"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    F.chao(c, x - 80, x + 900, y, q)
    p = ease_io(prog(t, t0 + 0.3, 1.4))
    bx = lerp(x + 60, x + 600, p)
    E.bola(c, bx, y - 60, 60, TINTA2, q)
    tomba = ease_out(prog(t, t0 + 1.5, 0.6))
    for i in range(3):
        px = x + 680 + i * 70
        c.save(); c.translate(px, y); c.rotate(70 * tomba * (1 if i else 0.8))
        M.rrect(c, -16, -120, 32, 120, 14, BR, q)
        M.rrect(c, -16, -90, 32, 12, 4, ERRADO, q)
        c.restore()
    F.vetor(c, t, t0 + 0.3, (x + 40, y - 170), (x + 300, y - 170), "v", None, EC, 8, size=48)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for i, (v, tv) in enumerate(((40, C["s01.a"]), (80, C["s01.a"] + 0.6))):
            y = 470 + i * 330
            if t >= tv:
                F.chao(c, 170, 900, y, ep(t, tv, 0.4))
            E.foco(c, t, tv, 0.5, lambda a, y=y: F.carrinho(c, 500, y, 300, a=a))
            E.foco(c, t, tv + 0.3, 0.4, lambda a, y=y, v=v: F.medida(c, v, "km/h", 720, y - 150, 70, TINTA, a))
        fmt = lambda v: {1: "1×", 4: "4×"}[v]
        barras_energia(c, t, 1150, 860, 520, 4, [("40 km/h", 1, EC, C["s01.a"] + 1.0), ("80 km/h", 4, EC, C["s01.c"])], larg_=200, gap=120, size=56, fmt=fmt)
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.formula(c, "o dobro?", 1500, 280, 64, "g", ERRADO, a, "center")) if t < C["s01.c"] else None
        E.frase(c, t, C["s01.d"], ps("a velocidade pesa na batida", "i", 60, TINTA2), W / 2, 1010, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 320 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
        itens = (("s02.a", "energia cinética", 1.4, True), ("s02.b", "teorema do trabalho", 0, False), ("s02.b", "freio e distância", 1.2, False))
        for i, (k, s, dt, forte) in enumerate(itens):
            y = 450 + i * 160
            E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if forte else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o trabalho, em joule:", "τ = F · d · cos θ", None),
                              ("s03.c", "proporcional ao quadrado:", "dobra x → x² vezes 4", "2² = 4   ·   3² = 9")))


# ---------------- energia cinética ----------------
def b_cinetica(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("energia", "g", 90, COR), ("=", "g", 90), ("capacidade", "i", 90)], XE, 240, passo=0.12)
        E.frase(c, t, C["s04.a"] + 0.9, ps("de realizar trabalho", "i", 76), XE, 340, passo=0.12)
        boliche(c, t, C["s04.b"], 520, 760)
        E.frase(c, t, C["s04.c"], [("energia", "g", 84), ("cinética", "g", 84, EC)], XE, 960, passo=0.14)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], ps("massa × velocidade ao quadrado ÷ 2", "i", 62, TINTA2), XE, 220, passo=0.1)
            F.formula_legenda(c, t, C["s05.b"], "Ec = f{m · v^2}{2}", [("m", "massa", "kg"), ("v", "velocidade", "m/s"), ("Ec", "energia cinética", "J")],
                              XE, 470, 140, tl=[C["s05.c"], C["s05.d"], C["s05.e"]])
            q = ep(t, C["s05.b"] + 0.5, 0.5)
            if q > 0:
                E.formula(c, "v^2 = v · v", 1250, 470, 80, "g", EC, q)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], [("bola", "i", 76), ("2 kg", "g", 72), ("a", "i", 76), ("3 m/s", "g", 72, EC)], XE, 220, passo=0.12)
    E.foco(c, t, C["s06.a"] + 0.4, 0.5, lambda a: E.formula(c, "Ec = f{2 · 3^2}{2}", XE, 470, 120, "g", TINTA, a))
    troca(c, t, [(C["s06.b"], "3^2 = 9"), (C["s06.c"], "2 · 9 = 18"), (C["s06.d"], "18 ÷ 2 = 9")], lambda s, a: E.formula(c, s, XE, 700, 90, "g", TINTA2, a))
    bola_txt(c, t, C["s06.d"] + 0.4, "9 J", 1400, 520, 160, 90)


# ---------------- o quadrado ----------------
def b_quadrado(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07"], [("carro", "i", 70), ("1.000 kg", "g", 66)], XE, 200, passo=0.12)
        for i, (k, kr, v, conta) in enumerate((("s07.a", "s07.b", "10 m/s", "f{1.000 · 10^2}{2}"), ("s07.c", "s07.d", "20 m/s", "f{1.000 · 20^2}{2}"))):
            y = 400 + i * 300
            E.foco(c, t, C[k], 0.5, lambda a, v=v, y=y: F.medida(c, *v.split(" "), XE, y, 80, EC, a))
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, conta=conta, y=y: E.formula(c, conta, XE + 330, y, 70, "g", TINTA2, a))
        fmt = lambda v: milhar(v) + " J"
        barras_energia(c, t, 1180, 900, 560, 200000, [("10 m/s", 50000, EC, C["s07.b"]), ("20 m/s", 200000, EC, C["s07.d"])], larg_=200, gap=140, size=50, fmt=fmt)
        E.foco(c, t, C["s07.e"], 0.5, lambda a: E.pilula(c, "4× a energia", 1520, 200, 54, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s07.c"] - 0.4, 0.4, lambda a: E.escreve(c, "2× a velocidade", XE, 860, 54, "i", TINTA2, a))
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    linhas = (("s08.a", "velocidade × 2", "energia × 4", True), ("s08.b", "velocidade × 3", "energia × 9", True), ("s08.c", "massa × 2", "energia × 2", False))
    for i, (k, l1, l2, quad) in enumerate(linhas):
        y = 330 + i * 230
        E.foco(c, t, C[k], 0.5, lambda a, l1=l1, y=y: E.formula(c, l1, XE + 60, y, 90, "g", EC if i < 2 else TINTA, a))
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, y=y: F.seta(c, 900, y - 30, 1060, y - 30, TINTA2, a, 8))
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, l2=l2, y=y, quad=quad: E.formula(c, l2, 1110, y, 90, "g", COR if quad else TINTA, a))
    E.foco(c, t, C["s08.c"] + 1.0, 0.4, lambda a: E.pilula(c, "a massa entra sem quadrado", W / 2, 960, 46, "b", fundo=TINTA, a=a))


# ---------------- teorema ----------------
def b_teorema(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09.a"], ps("ganha energia", "i", 76) + [("recebendo", "i", 76), ("trabalho", "g", 72, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s09.b"], [("força", "i", 60, TINTA2), ("resultante", "g", 56, TINTA2), ("=", "g", 56, TINTA2)] + ps("a soma de todas as forças", "i", 60, TINTA2),
                XE, 330, passo=0.1)
        E.formula_em(c, t, C["s09.c"], "τ = ΔEc", W / 2, 560, 170, "g", TINTA, "center")
        E.formula_em(c, t, C["s09.d"], "ΔEc = Ec fim − Ec começo", W / 2, 740, 76, "g", EC, "center")
        pilula_em(c, t, C["s09.e"], "teorema do trabalho e da energia cinética", W / 2, 900, 50, E.COR)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    for i, (k, sinal, txt, cor, ang) in enumerate((("s10.a", "τ > 0", "a energia aumenta: acelera", E.COR, 0), ("s10.b", "τ < 0", "a energia diminui: freia", F.NEG, 180))):
        y = 360 + i * 380
        pilula_em(c, t, C[k], sinal, XE + 140, y - 30, 64, cor)
        E.frase(c, t, C[k] + 0.3, ps(txt, "i", 64), XE + 330, y, passo=0.1)
        barras_energia(c, t, 1420, y + 110, 240, 4, [("antes", 2, EC, C[k] + 0.5), ("depois", 4 if i == 0 else 1, EC, C[k] + 1.0)], larg_=120, gap=60, size=40,
                       fmt=lambda v: "")


# ---------------- freada ----------------
def b_freio(c, t, C, b):
    y = 520
    if t >= C["s11.a"]:
        F.chao(c, 170, 1750, y, ep(t, C["s11.a"], 0.4))
    p = ease_out(prog(t, C["s11.a"] + 0.4, 2.4))
    E.foco(c, t, C["s11.a"], 0.5, lambda a: F.carrinho(c, lerp(380, 1250, p), y, 300, a=a))
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.formula(c, "1.000 kg · 20 m/s", 380, 300, 56, "g", TINTA, a, "center"))
    caminho(c, t, C["s12.a"], 380, 1250, y + 60, "d", "40 m")

    def s11():
        E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "Ec fim = 0", XE, 760, 76, "g", EC, a))
        E.foco(c, t, C["s11.c"], 0.5, lambda a: E.formula(c, "τ = 0 − 200.000", XE, 900, 86, "g", TINTA, a))
        bola_txt(c, t, C["s11.d"], "−200.000 J", 1400, 820, 170, 56, F.NEG)
    E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    F.forca(c, t, C["s12.b"] - 0.3, (1250, y - 230), 180, 300, "F", size=54, lado=-1)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "τ = −F · 40", XE, 760, 86, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "F · 40 = 200.000", XE, 900, 86, "g", TINTA, a))
    bola_txt(c, t, C["s12.d"], "5.000 N", 1400, 820, 150, 64)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("subtrair antes do quadrado", "i", 70), XE + 480, 200, passo=0.12)
    E.frase(c, t, C["s13.b"], [("2 kg:", "g", 66), ("10", "g", 66, EC), ("→", "g", 66, TINTA2), ("20 m/s", "g", 66, EC)], XE, 340, passo=0.12)

    def errado():
        E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "20 − 10 = 10", 520, 520, 84, "g", ERRADO, a, "center"))
        E.foco(c, t, C["s13.d"], 0.5, lambda a: E.formula(c, "f{2 · 10^2}{2} = 100 J", 520, 720, 84, "g", ERRADO, a, "center"))
        if t >= C["s13.d"] + 1.6:
            E.risco(c, 250, 760, 790, 640, t, C["s13.d"] + 1.6, largura=12)
    errado()
    if t < C["s14"]:
        return
    if t >= C["s14"]:
        M.line(c, 980, 300, 980, 950, FIO, ep(t, C["s14"], 0.4), 3)
    E.frase(c, t, C["s14.a"], [("Ec", "g", 60, EC), ("fim", "i", 64), ("−", "g", 60), ("Ec", "g", 60, EC), ("começo", "i", 64)], 1420, 340, "center", 0.12)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.formula(c, "fim: f{2 · 20^2}{2} = 400", 1420, 520, 70, "g", TINTA, a, "center"))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "começo: f{2 · 10^2}{2} = 100", 1420, 700, 70, "g", TINTA, a, "center"))
    bola_txt(c, t, C["s14.d"], "300 J", 1420, 880, 100, 60, CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s15.a"], ps("mesma força de freio:", "i", 64, CLARO) + [("distância", "g", 60, BR), ("vai", "i", 64, CLARO), ("com", "i", 64, CLARO),
                                                                                    ("v²", "g", 60, BR)], W / 2, 290, "center", 0.1)
        E.frase(c, t, C["s15.b"], [("v", "g", 76, BR), ("× 2", "g", 76, CLARO), ("→", "g", 76, CLARO), ("distância", "g", 76, BR), ("× 4", "g", 76, CLARO)], W / 2, 430, "center", 0.12)
        for i, (v, d, k) in enumerate(((20, 40, "s15.b"), (40, 160, "s15.c"))):
            y = 620 + i * 200
            x1 = 300 + d * 7.5
            E.foco(c, t, C[k] + 0.5, 0.4, lambda a, v=v, y=y: F.medida(c, v, "m/s", 280, y - 30, 56, BR, a, "right", escuro=True))
            if t >= C[k] + 0.5:
                M.line(c, 300, y, 300 + 1200 * 1.0, y, "#5A5A66", ep(t, C[k] + 0.5, 0.3), 4)
                F.vetor(c, t, C[k] + 0.8, (300, y), (x1, y), None, None, CLARO, 12, escuro=True)
            E.foco(c, t, C[k] + 1.4, 0.4, lambda a, d=d, x1=x1, y=y: F.medida(c, d, "m", x1 + 20, y + 18, 60, BR, a, escuro=True))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("F · d", "g", 76, BR)] + ps("= energia que o freio tira", "i", 70, CLARO), W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s16.b"], ps("e a energia vai com", "i", 70, CLARO) + [("v²", "g", 76, BR)], W / 2, 430, "center", 0.12)
    E.frase(c, t, C["s16.c"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("freio que muda, ou o carro não para", "i", 66, CLARO), W / 2, 700, "center", 0.1)
    E.frase(c, t, lerp(C["s16.c"], C["s16.end"], 0.7), ps("aí, faça a conta da energia", "i", 64, CLARO), W / 2, 820, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("carrinho", "i", 72), ("4 kg", "g", 68), ("a", "i", 72), ("3 m/s", "g", 68, EC)], XE, 360, passo=0.12)
    E.frase(c, t, C["s17.b"], [("chega", "i", 72), ("a", "i", 72), ("5 m/s", "g", 68, EC)], XE, 470, passo=0.12)
    E.frase(c, t, C["s17.c"], [("trabalho", "g", 68, COR), ("da", "i", 72), ("força?", "i", 72)], XE, 640, passo=0.12)
    E.frase(c, t, C["s17.d"], [("F", "g", 68, COR), ("=", "g", 68), ("8 N:", "g", 68), ("quantos", "i", 72), ("metros?", "g", 68)], XE, 760, passo=0.12)
    if t < C["s18"]:
        y = 720
        if t >= C["s17.a"]:
            F.chao(c, 1080, 1800, y, ep(t, C["s17.a"], 0.4))
        E.foco(c, t, C["s17.a"], 0.5, lambda a: F.bloco(c, 1300, y - 80, 200, 160, "4 kg", TINTA2, a))
        F.forca(c, t, C["s17.b"], (1400, y - 80), 0, 220, "F", size=54)
        F.vetor(c, t, C["s17.a"] + 0.4, (1200, y - 230), (1420, y - 230), "v", None, EC, 8, size=48)
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "começo: f{4 · 3^2}{2} = 18 J", XE, 330, 84, "g", TINTA, a))
        E.foco(c, t, C["s19.b"], 0.5, lambda a: E.formula(c, "fim: f{4 · 5^2}{2} = 50 J", XE, 560, 84, "g", TINTA, a))
        E.foco(c, t, C["s19.c"], 0.5, lambda a: E.formula(c, "τ = 50 − 18", XE, 800, 90, "g", TINTA, a))
        bola_txt(c, t, C["s19.c"] + 0.8, "32 J", 1450, 650, 150, 84)
        barras_energia(c, t, 1300, 470, 300, 50, [("antes", 18, EC, C["s19.a"]), ("depois", 50, EC, C["s19.b"])], larg_=110, gap=80, size=40) if t < C["s19.c"] + 0.8 else None
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20.a"], ps("a força ajuda:", "i", 70) + [("τ = F · d", "g", 70, COR)], XE, 280, passo=0.12)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "8 · d = 32", W / 2, 540, 120, "g", TINTA, a, "center"))
    bola_txt(c, t, C["s20.c"], "4 m", W / 2, 800, 130, 80)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", "Ec = f{m · v^2}{2}"), ("s21.b", "velocidade × 2  →  energia × 4"), ("s21.c", "τ resultante = Ec fim − Ec começo"))
        for i, (k, s) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 70, "g", TINTA, a))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22"] + 1.0, [("energia", "g", 120, COR), ("potencial", "g", 120, COR)], XE, 420)
    E.frase(c, t, C["s22.a"], ps("no alto", "i", 84), XE, 600)
    E.frase(c, t, C["s22.b"], ps("e numa mola", "i", 84), XE, 720)
    E.foco(c, t, C["s22.b"], 0.5, lambda a: F.mola(c, XE + 470, 690, XE + 820, 690, 7, 40, TINTA2, a))
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, cinetica=b_cinetica, quadrado=b_quadrado, teorema=b_teorema, freio=b_freio, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
