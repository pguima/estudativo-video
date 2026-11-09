"""Visual — Estudativo · FIS-ENE-004: energia potencial gravitacional e elástica.

Linguagem visual: a da Física (cabeçalho do visual.py da FIS-CIN-001) e a da trilha Energia e Colisões (cabeçalho do
visual.py da FIS-ENE-001). Energia potencial = laranja (E.COR); altura h = cota tracejada em tinta; deformação x da mola =
cota petróleo; gráfico F × x com a área (triângulo) pintada em laranja.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-004_energia_potencial_gravitacional_e_elastica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("gravitacional", "elastica", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"

# todas as contas da aula
ok = lambda a, b: abs(a - b) < 1e-9
assert 2 * 10 * 5 == 100 and ok(500 * 0.2 ** 2 / 2, 10) and ok(0.2 ** 2, 0.04) and 500 * 20 ** 2 / 2 == 100000 and 100000 / 10 == 10000
assert ok(100 * 0.2 / 2, 10) and ok(500 * 0.2, 100) and 0.5 * 10 * 2 == 10 and ok(1000 * 0.1 ** 2 / 2, 5) and ok(0.1 ** 2, 0.01)


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
def predio(c, x, yb, w, andares, a=1.0, janela=None):
    """prédio de frente com a base em yb; janela = andar (1 = térreo) onde fica o parapeito. Devolve o y do parapeito"""
    if a <= 0:
        return 0
    ha = 110
    M.rrect(c, x, yb - ha * andares, w, ha * andares, 8, "#D9D6CF", a)
    yj = 0
    for k in range(andares):
        y = yb - ha * (k + 1)
        for j in range(3):
            M.rrect(c, x + 30 + j * (w - 60) / 3 + 8, y + 22, (w - 60) / 3 - 16, 60, 6, "#9FB7C6", a)
        if janela == k + 1:
            yj = y + 82
            M.line(c, x + w - 20, yj, x + w + 50, yj, TINTA, a, 8)
    return yj


def vaso(c, cx, yb, s, a=1.0):
    """vaso de planta com a base em yb"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(cx - s * 0.5, yb - s); p.lineTo(cx + s * 0.5, yb - s); p.lineTo(cx + s * 0.35, yb); p.lineTo(cx - s * 0.35, yb); p.close()
    c.drawPath(p, M.paint(E.COR, a))
    for dx, h in ((-0.2, 0.7), (0, 0.95), (0.22, 0.6)):
        M.line(c, cx + dx * s, yb - s, cx + dx * s * 1.6, yb - s - h * s, "#2FA84F", a, max(4, s * 0.08))


def mola_parede(c, t, t0, x0, y, L0, x_along, cor_bloco=None, rot=None, k=1.0):
    """parede à esquerda em x0, mola até o bloco; x_along = quanto esticou (px). Devolve a borda do bloco"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return x0 + L0
    F.parede(c, x0, y - 110 * k, y + 60 * k, -1, q)
    F.chao(c, x0, x0 + L0 + 500 * k, y + 60 * k, q)
    xe = x0 + L0 + x_along
    F.mola(c, x0, y, xe, y, 9, 46 * k, TINTA2, q, 6)
    F.bloco(c, xe + 70 * k, y, 140 * k, 120 * k, rot, cor_bloco or E.COR, q)
    return xe


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        x, yb = 1150, 980
        E.foco(c, t, C["s01.a"], 0.5, lambda a: predio(c, x, yb, 420, 6, a, janela=5))
        yj = yb - 110 * 5 + 82
        cai = ease_io(prog(t, C["s01.b"], 1.0)) if t >= C["s01.b"] else 0
        yv = lerp(yj, yb, cai)
        E.foco(c, t, C["s01.a"] + 0.4, 0.4, lambda a: vaso(c, x + 470, yv, 70, a))
        if t >= C["s01.b"]:
            F.vetor(c, t, C["s01.b"] + 0.6, (x + 580, yj), (x + 580, yb - 120), "v", None, F.VEL, 9, lado=-1, size=50)
        F.chao(c, 1000, 1850, yb, 1.0) if t >= C["s01.a"] else None
        E.frase(c, t, C["s01.a"], [("parado", "i", 90), ("no", "i", 90), ("alto", "g", 90)], XE, 300)
        E.frase(c, t, C["s01.b"], [("se", "i", 80), ("cair:", "i", 80), ("velocidade", "g", 76, F.VEL)], XE, 440, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("a energia já estava lá,", "i", 70) + [("guardada", "g", 66)], XE, 620, passo=0.1)
        E.frase(c, t, C["s01.d"], [("energia", "g", 110), ("potencial", "g", 110, COR)], XE, 820)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 320 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
        itens = (("s02.b", "na altura"), ("s02.c", "numa mola"), ("s02.c", "de onde vem a fórmula"))
        for i, (k, s) in enumerate(itens):
            y = 450 + i * 160
            dt = 1.0 if i == 2 else 0
            E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i < 2 else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "o trabalho:", "τ = F · d", None),
                              ("s03.c", "o peso:", "P = m · g", "g = 10 m/s^2"),
                              ("s03.d", "a lei de Hooke:", "F = k · x", None)))


# ---------------- gravitacional ----------------
def subida(c, t, t0, x, yb, alto, tp=None, th=None, rot=True):
    """bloco erguido devagar do chão até a altura alto (px), com a força igual ao peso e a cota h"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    F.chao(c, x - 200, x + 260, yb, q)
    p = ease_io(prog(t, t0 + 0.4, 1.6))
    y = lerp(yb - 60, yb - 60 - alto, p)
    F.bloco(c, x, yb - 60, 140, 120, None, E.COR, 0.18 * q)
    F.bloco(c, x, y, 140, 120, "m" if rot else None, E.COR, q, size=56)
    if tp is not None:
        F.forca(c, t, tp, (x, y - 60), 90, 150, "F", None, None, size=50, lado=-1)
        E.foco(c, t, tp + 0.4, 0.4, lambda a: E.formula(c, "= m · g", x + 70, y - 150, 50, "g", COR, a))
    if th is not None and t >= th:
        M.line(c, x + 130, yb, x + 130, yb - alto, TINTA, ep(t, th, 0.4), 4, dash=E.TRACO)
        E.foco(c, t, th + 0.2, 0.4, lambda a: E.escreve(c, "h", x + 150, yb - alto / 2 + 20, 60, "g", TINTA, a))


def b_gravitacional(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], [("energia", "g", 84), ("potencial", "g", 84, COR)], XE, 240, passo=0.12)
        E.frase(c, t, C["s04.a"] + 0.8, ps("= guardada pela posição", "i", 64) + ps("ou pela deformação", "i", 64), XE, 340, passo=0.1)
        E.frase(c, t, C["s04.b"], ps("não é movimento agora,", "i", 70), XE, 560, passo=0.1)
        E.frase(c, t, C["s04.c"], ps("pode virar", "i", 70) + [("movimento", "g", 66, F.VEL), ("depois", "i", 70)], XE, 660, passo=0.1)
        E.foco(c, t, C["s04.a"] + 1.5, 0.5, lambda a: vaso(c, 1450, 800, 110, a))
        E.foco(c, t, C["s04.a"] + 2.0, 0.5, lambda a: F.mola(c, 1250, 920, 1680, 920, 10, 50, TINTA2, a, 6))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05"], ps("comece pela", "i", 76) + [("altura", "g", 72, COR)], XE, 220, passo=0.12)
            subida(c, t, C["s05.a"], 1400, 900, 420, tp=C["s05.b"], th=C["s05.c"])
            E.frase(c, t, C["s05.b"], [("força", "i", 66), ("=", "g", 66), ("peso", "g", 66, COR), ("=", "g", 66), ("m · g", "g", 66)], XE, 420, passo=0.12)
            E.frase(c, t, C["s05.c"], [("ao", "i", 66), ("longo", "i", 66), ("de", "i", 66), ("h", "g", 66, COR)], XE, 540, passo=0.12)
            E.foco(c, t, C["s05.d"], 0.5, lambda a: E.formula(c, "τ = m · g · h", XE, 760, 120, "g", TINTA, a))
        E.saida(c, t, C["s06"] - 0.1, s05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], ps("o trabalho fica", "i", 76) + [("guardado", "g", 72, COR)], XE, 220, passo=0.12)
            F.formula_legenda(c, t, C["s06.b"], "Ep = m · g · h", [("m", "massa", "kg"), ("g", "gravidade, 10", "m/s^2"), ("h", "altura", "m"), ("Ep", "energia potencial", "J")],
                              XE, 480, 140, tl=[C["s06.c"], C["s06.c"] + 0.8, C["s06.c"] + 1.6, C["s06.d"]])
        E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        x, yb = 1200, 960
        E.foco(c, t, C["s07"], 0.5, lambda a: predio(c, x, yb, 340, 4, a, janela=0))
        E.foco(c, t, C["s07"] + 0.3, 0.5, lambda a: (M.line(c, x + 340, yb - 450, x + 460, yb - 450, TINTA, a, 8), vaso(c, x + 400, yb - 450, 70, a)))
        if t >= C["s07"] + 0.6:
            F.chao(c, 1050, 1850, yb, 1.0)
            M.line(c, x + 520, yb, x + 520, yb - 450, TINTA, ep(t, C["s07"] + 0.6, 0.4), 4, dash=E.TRACO)
        E.foco(c, t, C["s07"] + 0.8, 0.4, lambda a: F.medida(c, 5, "m", x + 545, yb - 205, 60, TINTA, a))
        E.frase(c, t, C["s07.a"], [("vaso", "i", 76), ("2 kg", "g", 72), ("a", "i", 76), ("5 m", "g", 72)], XE, 260, passo=0.12)
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "Ep = 2 · 10 · 5", XE, 480, 110, "g", TINTA, a))
        bola_txt(c, t, C["s07.b"] + 1.2, "100 J", XE + 300, 740, 130, 74)
    if t < C["s08"]:
        return
    E.frase(c, t, C["s08.a"], ps("altura medida", "i", 72) + [("a", "i", 72), ("partir", "i", 72), ("de", "i", 72), ("onde?", "g", 68, COR)], XE, 220, passo=0.12)
    x, yb = 1200, 960
    E.foco(c, t, C["s08"], 0.4, lambda a: predio(c, x, yb, 340, 4, a, janela=0))
    E.foco(c, t, C["s08"], 0.4, lambda a: (M.line(c, x + 340, yb - 450, x + 460, yb - 450, TINTA, a, 8), vaso(c, x + 400, yb - 450, 70, a)))
    if t >= C["s08"]:
        F.chao(c, 1050, 1850, yb, 1.0)
    E.frase(c, t, C["s08.b"], [("nível", "i", 66), ("zero:", "i", 66), ("você", "i", 66), ("escolhe", "g", 62)], XE, 400, passo=0.12)
    pilula_em(c, t, C["s08.b"] + 0.6, "zero no chão → 100 J", 1720, yb - 60, 40, TINTA)
    if t >= C["s08.c"]:
        M.line(c, 1000, yb - 450, 1800, yb - 450, E.COR, ep(t, C["s08.c"], 0.4), 4, dash=E.TRACO)
    pilula_em(c, t, C["s08.c"] + 0.4, "zero no vaso → 0 J", 1720, yb - 380, 40, E.COR)
    E.frase(c, t, C["s08.c"], ps("zero na altura do vaso:", "i", 60) + [("Ep = 0", "g", 58, COR)], XE, 560, passo=0.1)
    E.frase(c, t, C["s08.d"], [("a", "i", 64), ("diferença", "g", 60), ("entre", "i", 64), ("dois", "i", 64), ("pontos", "i", 64)], XE, 760, passo=0.12)
    E.frase(c, t, C["s08.d"] + 1.0, ps("nunca muda", "i", 64, COR), XE, 860, passo=0.12)


# ---------------- elástica ----------------
def b_elastica(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], ps("passe para a", "i", 76) + [("mola", "g", 72, COR)], XE, 200, passo=0.12)
        stretch = 260 * ease_io(prog(t, C["s09.a"], 2.2))
        xe = mola_parede(c, t, C["s09"] + 0.4, 300, 500, 520, stretch)
        if t >= C["s09.b"]:
            F.vetor(c, t, C["s09.b"], (xe + 140, 500), (xe + 140 + 60 + stretch * 0.9, 500), "F", None, E.COR, 9, lado=-1, size=50)
        if t >= C["s09.c"]:
            M.line(c, 820, 420, 820, 600, TINTA2, ep(t, C["s09.c"], 0.4), 3, dash=E.TRACO)
            F.vetor(c, t, C["s09.c"], (820, 650), (820 + stretch, 650), "x", None, F.VEL, 7, lado=-1, size=48)
        E.frase(c, t, C["s09.a"], [("a", "i", 64), ("força", "i", 64), ("não", "g", 60), ("é", "i", 64), ("constante", "g", 60)], XE, 770, passo=0.12)
        E.frase(c, t, C["s09.b"], [("de", "i", 64), ("0", "g", 60), ("até", "i", 64), ("k · x", "g", 60, COR)], XE + 1000, 770, passo=0.12)
        E.foco(c, t, C["s09.c"], 0.5, lambda a: E.formula(c, "x = deformação (m)", XE, 900, 58, "b", F.VEL, a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.formula(c, "k = constante da mola (N/m)", XE + 760, 900, 58, "b", TINTA, a))
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    P = F.grafico(c, t, C["s10.a"], 960, 220, 820, 560, 0, 0.3, 0, 150, "x (m)", "F (N)", passo=0.1, passo_y=50)
    f = lambda x: 500 * x
    E.curva(c, t, C["s10.b"], P, f, 0, 0.2, d=0.8)
    E.area(c, t, C["s10.c"], P, f, 0, 0.2)
    E.foco(c, t, C["s10.c"] + 0.4, 0.4, lambda a: (E.formula(c, "k · x", P.x(0.2) + 20, P.y(100) - 10, 52, "g", COR, a),
                                                   E.formula(c, "x", P.x(0.1), P.y(0) - 30, 52, "g", F.VEL, a, "center")))

    def s10():
        E.frase(c, t, C["s10.a"], ps("força que muda:", "i", 64) + [("gráfico", "g", 60)], XE, 280, passo=0.12)
        E.frase(c, t, C["s10.b"], ps("reta que sai do zero", "i", 60, TINTA2), XE, 380, passo=0.1)
        E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "área = f{x · k · x}{2}", XE, 560, 76, "g", TINTA, a))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if C["s11"] <= t < C["s12"]:
        def s11():
            E.foco(c, t, C["s11.a"], 0.5, lambda a: E.formula(c, "Ep = f{k · x^2}{2}", XE, 400, 120, "g", COR, a))
            E.frase(c, t, C["s11.b"], [("k", "g", 56, COR), ("=", "g", 56), ("500 N/m", "g", 56)], XE, 560, passo=0.1)
            E.frase(c, t, C["s11.c"], [("x", "g", 56, F.VEL), ("=", "g", 56), ("20 cm", "g", 56)], XE, 650, passo=0.1)
            E.foco(c, t, C["s11.d"], 0.5, lambda a: E.formula(c, "= 0,2 m", XE + 380, 650, 56, "g", F.VEL, a))
            troca(c, t, [(C["s11.e"], "0,2^2 = 0,04"), (C["s11.f"], "f{500 · 0,04}{2} = f{20}{2}")], lambda s, a: E.formula(c, s, XE, 840, 76, "g", TINTA, a))
            bola_txt(c, t, C["s11.f"] + 1.4, "10 J", P.x(0.1), P.y(30) + 10, 80, 48)
        E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.formula(c, "x × 2  →  Ep × 4", XE, 500, 90, "g", COR, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("x em centímetro", "i", 76), XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "f{500 · 20^2}{2}", 560, 470, 100, "g", ERRADO, a, "center"))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "= 100.000 J", 560, 700, 100, "g", ERRADO, a, "center"))
    if t >= C["s14.a"]:
        E.risco(c, 270, 720, 860, 600, t, C["s14.a"], largura=12)
    if t >= C["s14"]:
        M.line(c, 980, 300, 980, 950, FIO, ep(t, C["s14"], 0.4), 3)
    E.frase(c, t, C["s14.a"], [("k", "g", 64, COR), ("em", "i", 66), ("N/m", "g", 64), ("→", "g", 64, TINTA2), ("x", "g", 64, F.VEL), ("em", "i", 66), ("metro", "g", 64)],
            1420, 400, "center", 0.12)
    E.foco(c, t, C["s14.a"] + 1.4, 0.5, lambda a: E.formula(c, "f{500 · 0,2^2}{2} = 10 J", 1420, 600, 84, "g", CERTO, a, "center"))
    E.frase(c, t, C["s14.b"], ps("com centímetro:", "i", 60) + [("10.000×", "g", 60, ERRADO), ("maior", "i", 60)], 1420, 800, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s15.a"], ps("sem o k? com a", "i", 66, CLARO) + [("força", "g", 62, BR), ("final", "g", 62, BR)], W / 2, 290, "center", 0.12)
        E.foco(c, t, C["s15.b"], 0.6, lambda a: (E.bola(c, W / 2, 500, 200 * ease_back(prog(t, C["s15.b"], 0.6)), a=a),
                                                 E.formula(c, "Ep = f{F · x}{2}", W / 2, 520, 72, "g", BR, a, "center")))
        E.frase(c, t, C["s15.c"], [("F", "g", 62, BR), ("=", "g", 62, CLARO), ("100 N,", "g", 62, BR), ("x", "g", 62, BR), ("=", "g", 62, CLARO), ("20 cm", "g", 62, BR)],
                W / 2, 800, "center", 0.12)
        E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "f{100 · 0,2}{2} = f{20}{2} = 10 J", W / 2, 950, 70, "g", CLARO, a, "center"))
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("F", "g", 76, BR), ("final", "i", 80, CLARO), ("=", "g", 76, CLARO), ("k · x", "g", 76, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s16.b"], ps("a mesma mola: 500 · 0,2 = 100 N", "i", 64, CLARO), W / 2, 440, "center", 0.1)
    E.frase(c, t, C["s16.c"], [("não", "g", 62, ERRADO), ("compensa:", "i", 66, CLARO)] + ps("deu k e x? use a fórmula", "i", 66, CLARO), W / 2, 720, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s17.a"], [("livro", "i", 72), ("0,5 kg", "g", 68), ("a", "i", 72), ("2 m", "g", 68)], XE, 360, passo=0.12)
    E.frase(c, t, C["s17.b"], [("Ep", "g", 68, COR), ("em", "i", 72), ("relação", "i", 72), ("ao", "i", 72), ("chão?", "g", 68)], XE, 470, passo=0.12)
    E.frase(c, t, C["s17.c"], [("mola", "i", 72), ("1.000 N/m,", "g", 68), ("comprimida", "i", 72), ("10 cm", "g", 68)], XE, 650, passo=0.12)
    E.frase(c, t, C["s17.d"], [("energia", "i", 72), ("guardada?", "g", 68, COR)], XE, 760, passo=0.12)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s19():
        E.foco(c, t, C["s19.a"], 0.5, lambda a: E.formula(c, "Ep = 0,5 · 10 · 2", W / 2, 460, 120, "g", TINTA, a, "center"))
        bola_txt(c, t, C["s19.b"], "10 J", W / 2, 760, 140, 84)
    E.saida(c, t, C["s20"] - 0.1, s19)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.formula(c, "x = 10 cm = 0,1 m", XE, 260, 80, "g", F.VEL, a))
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.formula(c, "0,1^2 = 0,01", XE, 440, 80, "g", TINTA2, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "Ep = f{1.000 · 0,01}{2} = f{10}{2}", XE, 660, 90, "g", TINTA, a))
    bola_txt(c, t, C["s20.d"], "5 J", 1500, 560, 140, 84)
    E.frase(c, t, C["s20.d"] + 1.0, ps("comprimida ou esticada: a mesma conta", "i", 58, TINTA2), W / 2, 950, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", "altura:  Ep = m · g · h"), ("s21.b", "mola:  Ep = f{k · x^2}{2}"), ("s21.c", "as duas: trabalho guardado"))
        for i, (k, s) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.foco(c, t, C[k] + 0.1, 0.5, lambda a, s=s, y=y: E.formula(c, s, 400, y, 70, "g", TINTA, a))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("energia", "g", 110), ("guardada", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s22.a"] + 0.7, [("vira", "i", 100), ("movimento", "g", 110, F.VEL)], XE, 560)
    E.frase(c, t, C["s22.b"], ps("montanha-russa e pêndulo", "i", 70, TINTA2), XE, 720, passo=0.1)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, gravitacional=b_gravitacional, elastica=b_elastica, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
