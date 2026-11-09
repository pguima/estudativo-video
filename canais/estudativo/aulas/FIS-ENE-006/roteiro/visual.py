"""Visual — Estudativo · FIS-ENE-006: praticando trabalho e energia (cinco situações).

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001). Nas práticas, cada situação abre com o número numa esfera; a pausa usa E.relogio; o caminho
da energia aparece numa cadeia de pílulas (peça cadeia): elétrica = âmbar (ELET), potencial = laranja, cinética =
petróleo, calor = cinza.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-006_praticando_trabalho_e_energia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
EC, EPOT, ELET = F.VEL, E.COR, "#D9A400"

# todas as contas da aula
ok = lambda a, b: abs(a - b) < 1e-9
assert 4 * 30 + 2 * 30 / 2 == 150 and 500 * 10 * 12 == 60000 and 60000 / 20 == 3000 and 3000 / 4000 == 0.75
assert 108 / 72 == 1.5 and 1.5 ** 2 == 2.25 and 40 * 2.25 == 90 and 72 / 3.6 == 20 and 108 / 3.6 == 30 and (30 / 20) ** 2 == 2.25
assert ok(800 * 0.1 ** 2 / 2, 4) and 0.5 / 2 == 0.25 and 4 / 0.25 == 16 and math.sqrt(16) == 4
assert 2000 * 10 * 50 == 1_000_000 and 0.9 * 1_000_000 == 900_000


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
def situacao(c, t, t0, n, titulo):
    """cabeçalho da situação: número na esfera e o título"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 180, 56, a=a), centro(c, str(n), XE + 50, 206, 70, "g", BR, a)))
    E.frase(c, t, t0 + 0.2, [(titulo, "g", 72)], XE + 140, 205)


def cadeia(c, t, itens, x, y, size=46, gap=90):
    """caminho da energia: itens = [(texto, cor, instante)], pílulas ligadas por setas"""
    xx = x
    cs = []
    for i, (s, cor, ti) in enumerate(itens):
        w = E.larg(s, "g", size) + size * 1.1
        if i:
            E.foco(c, t, ti, 0.4, lambda a, xx=xx: F.seta(c, xx - gap + 12, y, xx - 12, y, TINTA2, a, 7))
        E.foco(c, t, ti, 0.4, lambda a, s=s, cor=cor, xx=xx, w=w: E.pilula(c, s, xx + w / 2, y, size, "g", fundo=cor, a=a))
        cs.append(xx + w / 2)
        xx += w + gap
    return cs


def pausa(c, t, C, cena):
    E.relogio(c, t, C[cena + ".a"], cx=1460, cy=520, r=200)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR), ("situações", "i", 110)], XE, 330, passo=0.2)
    nomes = ("gráfico", "guindaste", "freada", "mola", "usina")
    for i, s in enumerate(nomes):
        ti = lerp(C["s01.b"], C["s01.c"] - 0.3, i / 4)
        x = XE + i * 330
        E.foco(c, t, ti, 0.4, lambda a, i=i, x=x, s=s: (E.bola(c, x + 50, 520, 46, a=a), centro(c, str(i + 1), x + 50, 540, 54, "g", BR, a),
                                                        centro(c, s, x + 50, 640, 48, "g", TINTA, a)))
    E.frase(c, t, C["s01.c"], ps("pause e resolva antes da resposta", "i", 66), XE, 820, passo=0.1)
    E.frase(c, t, C["s01.d"], ps("e siga a", "i", 66) + [("energia", "g", 62, COR)], XE, 940, passo=0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 80), XE, 190, passo=0.12)
    linhas = (("s02.a", "τ = F · d · cos θ   ou   área do gráfico"), ("s02.b", "P = f{τ}{Δt}   ·   η = f{útil}{total}"),
              ("s02.c", "Ec = f{m · v^2}{2}   ·   Ep = m · g · h   ·   Ep = f{k · x^2}{2}"), ("s02.d", "sem atrito: E começo = E fim"))
    for i, (k, s) in enumerate(linhas):
        y = 360 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 38, a=a), centro(c, str(i + 1), XE + 40, y - 4, 48, "g", BR, a)))
        E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, XE + 110, y, 62, "g", TINTA, a))
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.6), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), XE, 1020, passo=0.1)


# ---------------- situação 1: gráfico ----------------
f1 = lambda x: 30 if x <= 4 else max(0.0, 30 - 15 * (x - 4))


def graf1(c, t, t0, tl1, tl2, ta1=None, ta2=None):
    P = F.grafico(c, t, t0, 960, 260, 820, 560, 0, 7, 0, 40, "d (m)", "F (N)", passo=1, passo_y=10)
    E.curva(c, t, tl1, P, f1, 0, 4, d=0.7)
    E.curva(c, t, tl2, P, f1, 4, 6, d=0.6)
    if ta1 is not None:
        E.area(c, t, ta1, P, f1, 0, 4)
        E.foco(c, t, ta1 + 0.5, 0.4, lambda a: F.medida(c, 120, "J", P.x(2), P.y(15) + 20, 56, COR, a, "center"))
    if ta2 is not None:
        E.area(c, t, ta2, P, f1, 4, 6, cor=F.VEL)
        E.foco(c, t, ta2 + 0.5, 0.4, lambda a: F.medida(c, 30, "J", P.x(4.6), P.y(8) + 20, 44, EC, a, "center"))
    return P


def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1, "o gráfico")
    E.frase(c, t, C["s03.a"] + 1.0, ps("força na direção do movimento", "i", 56, TINTA2), XE, 320, passo=0.1)
    E.frase(c, t, C["s03.b"], [("30 N", "g", 60, COR), ("nos", "i", 62), ("primeiros", "i", 62), ("4 m", "g", 60)], XE, 470, passo=0.12)
    E.frase(c, t, C["s03.c"], ps("depois cai a zero em", "i", 62) + [("2 m", "g", 60)], XE, 580, passo=0.12)
    E.frase(c, t, C["s03.d"], [("trabalho", "g", 66, COR), ("total?", "g", 66)], XE, 760, passo=0.12)
    if t < C["s04"]:
        graf1(c, t, C["s03.a"] + 0.4, C["s03.b"], C["s03.c"])
    else:
        pausa(c, t, C, "s04")


def b_resposta1(c, t, C, b):
    graf1(c, t, C["s05"] - 0.4, C["s05"] - 0.4, C["s05"] - 0.4, C["s05.b"], C["s05.c"])
    E.frase(c, t, C["s05.a"], [("trabalho", "i", 66), ("=", "g", 66), ("área", "g", 66, COR)], XE, 250, passo=0.12)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.formula(c, "retângulo: 4 · 30 = 120 J", XE, 430, 56, "g", COR, a))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: E.formula(c, "triângulo: f{2 · 30}{2} = 30 J", XE, 590, 56, "g", EC, a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.formula(c, "120 + 30 =", XE, 800, 76, "g", TINTA, a))
    bola_txt(c, t, C["s05.d"] + 0.5, "150 J", XE + 560, 775, 110, 62)


# ---------------- situação 2: guindaste ----------------
def guindaste(c, t, t0, x, yb, sobe=0.0):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    F.chao(c, x - 120, x + 620, yb, q)
    M.line(c, x, yb, x, yb - 640, TINTA, q, 16)
    M.line(c, x - 40, yb - 620, x + 520, yb - 620, TINTA, q, 14)
    M.rrect(c, x - 60, yb - 140, 120, 140, 12, ELET, q)
    yc = lerp(yb - 80, yb - 80 - 380, sobe)
    M.line(c, x + 460, yb - 620, x + 460, yc - 60, TINTA2, q, 4)
    F.bloco(c, x + 460, yc, 160, 120, "500 kg", E.COR, q, size=34)


def b_questao2(c, t, C, b):
    situacao(c, t, C["s06.a"], 2, "o guindaste")
    E.frase(c, t, C["s06.b"], [("500 kg", "g", 60), ("até", "i", 62), ("12 m", "g", 60, COR)], XE, 380, passo=0.12)
    E.frase(c, t, C["s06.c"], [("devagar,", "i", 62), ("em", "i", 62), ("20 s", "g", 60)], XE, 490, passo=0.12)
    E.frase(c, t, C["s06.d"], [("recebe", "i", 62), ("4 kW", "g", 60, ELET)], XE, 600, passo=0.12)
    E.frase(c, t, C["s06.e"], [("rendimento?", "g", 66, COR)], XE, 780)
    if t < C["s07"]:
        guindaste(c, t, C["s06.a"] + 0.4, 1250, 940, ease_io(prog(t, C["s06.b"] + 0.4, 2.0)))
    else:
        pausa(c, t, C, "s07")


def b_resposta2(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08"], [("útil", "g", 64, COR), ("=", "g", 64)] + ps("energia ganha em altura", "i", 64), XE, 220, passo=0.12)
        E.foco(c, t, C["s08.a"], 0.5, lambda a: E.formula(c, "Ep = 500 · 10 · 12 = 60.000 J", XE, 380, 70, "g", EPOT, a))
        E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "P útil = f{60.000}{20} = 3.000 W", XE, 560, 70, "g", TINTA, a))
        E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "4 kW = 4.000 W", XE, 720, 70, "g", ELET, a))
        E.foco(c, t, C["s08.d"], 0.5, lambda a: E.formula(c, "η = f{3.000}{4.000} =", XE, 900, 76, "g", TINTA, a))
        bola_txt(c, t, C["s08.d"] + 0.6, "75 %", XE + 720, 870, 110, 62)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], ps("siga a", "i", 80) + [("energia", "g", 76, COR)], XE, 260, passo=0.12)
    cs = cadeia(c, t, [("elétrica  4.000 W", ELET, C["s09.a"]), ("potencial  3.000 W", EPOT, C["s09.b"])], XE, 500, 62, 120)
    E.foco(c, t, C["s09.c"], 0.5, lambda a: (F.seta(c, cs[0], 560, cs[0], 760, TINTA2, a, 8), E.pilula(c, "calor  1.000 W", cs[0], 830, 62, "g", fundo=CINZA, a=a)))
    E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: centro(c, "3/4", cs[1], 410, 80, "g", EPOT, a))
    E.foco(c, t, C["s09.c"] + 0.4, 0.4, lambda a: E.escreve(c, "1/4", cs[0] + 260, 860, 80, "g", TINTA2, a))


# ---------------- situação 3: freada ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C["s10.a"], 3, "a freada")
    E.frase(c, t, C["s10.b"], [("72 km/h", "g", 62, EC), ("→", "g", 62, TINTA2), ("para", "i", 64), ("em", "i", 64), ("40 m", "g", 62)], XE, 400, passo=0.12)
    E.frase(c, t, C["s10.d"], [("mesmo", "i", 64), ("freio,", "i", 64), ("108 km/h:", "g", 62, EC)], XE, 560, passo=0.12)
    E.frase(c, t, C["s10.d"] + 1.4, [("quantos", "i", 66), ("metros?", "g", 64, COR)], XE, 680, passo=0.12)
    if t < C["s11"]:
        y = 900
        if t >= C["s10.b"]:
            F.chao(c, 170, 1750, y, ep(t, C["s10.b"], 0.4))
        p = ease_out(prog(t, C["s10.b"] + 0.3, 2.0))
        E.foco(c, t, C["s10.b"], 0.5, lambda a: F.carrinho(c, lerp(400, 1000, p), y, 260, a=a))
        caminho_ = C["s10.c"]
        F.vetor(c, t, caminho_, (400, y + 55), (1000, y + 55), "d", "40 m", EC, 8, lado=-1, size=46)
    else:
        pausa(c, t, C, "s11")


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s12.a"], [("energia", "i", 66), ("vai", "i", 66), ("com", "i", 66), ("v²", "g", 64, EC), ("→", "g", 64, TINTA2), ("distância", "i", 66), ("também", "i", 66)], XE, 220, passo=0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: E.formula(c, "f{108}{72} = 1,5", XE, 430, 90, "g", TINTA, a))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.formula(c, "1,5^2 = 2,25", XE, 620, 90, "g", TINTA, a))
    E.foco(c, t, C["s12.d"], 0.5, lambda a: E.formula(c, "40 · 2,25 =", XE, 820, 90, "g", TINTA, a))
    bola_txt(c, t, C["s12.d"] + 0.6, "90 m", XE + 680, 790, 120, 70)
    cadeia(c, t, [("cinética", EC, C["s12.e"]), ("calor nos freios", CINZA, C["s12.e"] + 0.5)], 1080, 480, 50)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("aqui cabe um atalho", "i", 76, CLARO), W / 2, 170, "center")
    E.frase(c, t, C["s13.a"], ps("numa comparação,", "i", 68, CLARO) + [("não", "g", 64, BR), ("converta", "g", 64, BR)], W / 2, 320, "center", 0.12)
    E.foco(c, t, C["s13.a"] + 1.4, 0.5, lambda a: E.formula(c, "f{108 km/h}{72 km/h} = 1,5", W / 2, 500, 84, "g", BR, a, "center"))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "f{30 m/s}{20 m/s} = 1,5", W / 2, 700, 84, "g", CLARO, a, "center"))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "a mesma razão", W / 2 + 560, 680, 46, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s13.d"], [("não", "g", 58, ERRADO), ("compensa:", "i", 62, CLARO)] + ps("pediu energia ou força? use m/s", "i", 62, CLARO), W / 2, 920, "center", 0.1)


# ---------------- situação 4: mola ----------------
def mola_carrinho(c, t, t0, solta=None):
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    x0, y = 260, 760
    F.parede(c, x0, y - 160, y + 40, -1, q)
    F.chao(c, x0, 1750, y + 40, q)
    s = ease_out(prog(t, solta, 0.6)) if solta is not None and t >= solta else 0
    xe = lerp(560, 660, s)
    F.mola(c, x0, y - 50, xe, y - 50, 8, 50, TINTA2, q, 6)
    cx = 660 + 150 + (900 * ease_io(prog(t, solta + 0.4, 1.5)) if s > 0 else 0) - (100 if s == 0 else 0)
    F.carrinho(c, cx, y + 40, 260, a=q)


def b_questao4(c, t, C, b):
    situacao(c, t, C["s14.a"], 4, "a mola")
    E.frase(c, t, C["s14.b"], [("k", "g", 60, COR), ("=", "g", 60), ("800 N/m", "g", 60)], XE, 360, passo=0.12)
    E.frase(c, t, C["s14.c"], [("comprimida", "i", 62), ("10 cm", "g", 60, F.VEL)], XE + 520, 360, passo=0.12)
    E.frase(c, t, C["s14.d"], [("carrinho", "i", 62), ("0,5 kg,", "g", 60), ("parado", "i", 62)], XE, 470, passo=0.12)
    E.frase(c, t, C["s14.e"], [("sem", "i", 62), ("atrito:", "i", 62), ("v", "g", 62, EC), ("=", "g", 62), ("?", "g", 62, COR)], XE, 580, passo=0.12)
    if t < C["s15"]:
        mola_carrinho(c, t, C["s14.b"])
    else:
        pausa(c, t, C, "s15")


def b_resposta4(c, t, C, b):
    def s16():
        E.foco(c, t, C["s16.a"], 0.5, lambda a: E.formula(c, "Ep = f{800 · 0,1^2}{2}", XE, 300, 84, "g", EPOT, a))
        troca(c, t, [(C["s16.b"], "0,1^2 = 0,01"), (C["s16.c"], "f{800 · 0,01}{2} = f{8}{2} = 4 J")], lambda s, a: E.formula(c, s, XE, 500, 76, "g", TINTA, a))
        cadeia(c, t, [("elástica  4 J", EPOT, C["s16.d"]), ("cinética  4 J", EC, C["s16.d"] + 0.6)], 1040, 300, 52)
        mola_carrinho(c, t, C["s16"], solta=C["s16.d"])
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.foco(c, t, C["s17.a"], 0.5, lambda a: E.formula(c, "f{0,5 · v^2}{2} = 4", XE, 300, 90, "g", EC, a))
    E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "0,25 · v^2 = 4", XE, 500, 90, "g", TINTA, a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.formula(c, "v^2 = f{4}{0,25} = 16", XE, 700, 90, "g", TINTA, a))
    bola_txt(c, t, C["s17.d"], "4 m/s", 1450, 560, 140, 70, EC)


# ---------------- situação 5: usina ----------------
def usina(c, t, t0, x, yb):
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    F.chao(c, x - 120, x + 700, yb, q)
    p = skia.Path(); p.moveTo(x, yb - 520); p.lineTo(x + 160, yb - 520); p.lineTo(x + 260, yb); p.lineTo(x, yb); p.close()
    c.drawPath(p, M.paint("#B9B6AE", q))
    c.drawRect(skia.Rect.MakeXYWH(x - 100, yb - 500, 100, 500), M.paint("#7FC8E8", 0.6 * q))
    M.line(c, x + 120, yb - 470, x + 420, yb - 60, "#3B8DB5", q, 22)
    c.drawCircle(x + 470, yb - 50, 50, M.paint(TINTA, q))
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: (M.line(c, x + 600, yb - 500, x + 600, yb - 50, TINTA, a, 4, dash=E.TRACO),
                                            M.line(c, x - 100, yb - 500, x + 620, yb - 500, TINTA2, a * 0.6, 3, dash=E.TRACO),
                                            E.escreve(c, "50 m", x + 620, yb - 260, 56, "g", TINTA, a),
                                            centro(c, "turbina", x + 470, yb + 70, 44, "i", TINTA2, a)))


def b_questao5(c, t, C, b):
    situacao(c, t, C["s18.a"], 5, "a usina")
    E.frase(c, t, C["s18.b"], [("a", "i", 62), ("cada", "i", 62), ("segundo:", "i", 62), ("2.000 kg", "g", 60), ("descem", "i", 62), ("50 m", "g", 60, COR)], XE, 370, passo=0.12)
    E.frase(c, t, C["s18.c"], [("90 %", "g", 60, ELET), ("vira", "i", 62), ("elétrica", "g", 60, ELET)], XE, 480, passo=0.12)
    E.frase(c, t, C["s18.d"], [("potência", "i", 66), ("elétrica?", "g", 64, COR)], XE, 660, passo=0.12)
    if t < C["s19"]:
        usina(c, t, C["s18.b"], 1150, 950)
    else:
        pausa(c, t, C, "s19")


def b_resposta5(c, t, C, b):
    def s20():
        E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "Ep = 2.000 · 10 · 50", XE, 300, 84, "g", EPOT, a))
        E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "= 1.000.000 J a cada segundo", XE, 440, 70, "g", TINTA, a))
        E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "= 1.000.000 W = 1 MW", XE, 580, 70, "g", TINTA, a))
        E.foco(c, t, C["s20.d"], 0.5, lambda a: E.formula(c, "90 % → 900.000 W", XE, 780, 76, "g", ELET, a))
        bola_txt(c, t, C["s20.d"] + 0.8, "900 kW", 1500, 750, 140, 64, ELET)
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], ps("siga a", "i", 80) + [("energia", "g", 76, COR)], XE, 260, passo=0.12)
    cs = cadeia(c, t, [("potencial", EPOT, C["s21.a"]), ("cinética", EC, C["s21.a"] + 0.7), ("elétrica  90 %", ELET, C["s21.b"])], XE, 500, 62, 120)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: (F.seta(c, cs[2], 560, cs[2], 760, TINTA2, a, 8), E.pilula(c, "calor  10 %", cs[2], 830, 62, "g", fundo=CINZA, a=a)))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        itens = (("s22.a", "força que muda: área do gráfico"), ("s22.b", "rendimento: útil ÷ total"), ("s22.c", "velocidade pesa ao quadrado"), ("s22.d", "sem atrito: só muda de forma"))
        for i, (k, s) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 68, "g", TINTA, a))
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], [("quantidade", "g", 100, COR), ("de", "i", 96)], XE, 400)
    E.frase(c, t, C["s23.a"] + 0.5, [("movimento", "g", 100, COR)], XE, 520)
    E.frase(c, t, C["s23.a"] + 0.9, [("e", "i", 96), ("impulso", "g", 100, COR)], XE, 640)
    E.frase(c, t, C["s23.b"], ps("por que o airbag protege", "i", 64, TINTA2), XE, 780, passo=0.1)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
