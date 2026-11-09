"""Visual — Estudativo · FIS-ENE-001: trabalho de uma força. Primeira aula da trilha Energia e Colisões.

Segue a LINGUAGEM VISUAL DA FÍSICA (cabeçalho do visual.py da FIS-CIN-001: grandeza, medida, fórmula com legenda, vetores,
certo/errado, palco no atalho). Peças em _ferramentas/fisica.py (F).

LINGUAGEM VISUAL DA TRILHA ENERGIA E COLISÕES (FIS-ENE-*; as aulas seguintes copiam daqui):
- FORÇA = seta laranja (F.forca / F.vetor, cor E.COR). DESLOCAMENTO d = seta petróleo (F.VEL) embaixo do chão, com o
  valor ("d = 10 m"). Ângulo θ entre força e deslocamento = arco laranja (E.angulo), com a reta do caminho tracejada.
- TRABALHO τ: fórmula nova com F.formula_legenda. Sinal do trabalho em pílula: positivo ("ajuda") = laranja (E.COR),
  negativo ("atrapalha") = azul (F.NEG), zero ("perpendicular") = cinza-tinta (TINTA2). Verde e vermelho seguem sendo
  só certo e errado.
- COMPONENTE que trabalha = seta laranja-clara ao longo do chão (E.mix(COR, branco, 0.35)); a que não trabalha = cinza.
- GRÁFICO F × d (F.grafico, eixos "d (m)" e "F (N)"): linha laranja e área pintada; o valor da área vai dentro dela, em J.
- ENERGIA: barras verticais (peça barras_energia, nas aulas de energia): cinética = petróleo (F.VEL, porque vem da
  velocidade), potencial = laranja (E.COR), dissipada/calor = cinza (TINTA2), elétrica = âmbar (ELET). O total fica numa
  linha tracejada em tinta acima das barras.
- QUANTIDADE DE MOVIMENTO Q = seta petróleo grossa (mesmo sentido de v); IMPULSO I = seta laranja (como a força).
  Convenção de sinal: seta "+" em tinta no alto da tela (peça sentido_mais), para a direita.
- COLISÕES: painel "antes" | "depois" separados por um fio; corpos = esferas ou blocos laranja com a massa dentro;
  velocidade = seta petróleo em cima de cada corpo, com o valor; Ec de cada momento em barras.
- Resposta final na esfera laranja (bola_txt), com a unidade. Contas que se resolvem: troca (uma linha sai quando a
  próxima chega).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Energia e Colisões")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-ENE-001_trabalho_de_uma_forca.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "inclinada", "sinais", "grafico", "atalho", "questao", "fim"))
BR = "#FFFFFF"
COMP = E.mix(E.COR, BR, 0.35)  # componente que trabalha

# todas as contas da aula
cos = lambda g: round(math.cos(math.radians(g)), 12)
assert 20 * 10 == 200 and 50 * 10 * cos(60) == 250 and 50 * 10 == 500 and -2000 * 20 == -40000
assert 5 * 40 / 2 == 100 and 100 * 8 * cos(60) == 400 and 100 * 8 * cos(90) == 0 and cos(180) == -1 and cos(0) == 1


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
def mochila(c, cx, cy, w, a=1.0):
    """mochila em pé, centrada em (cx, cy); alça em cima"""
    if a <= 0:
        return
    h = w * 1.2
    pt = M.paint(TINTA, a, stroke=max(6, w * 0.06))
    c.drawArc(skia.Rect.MakeXYWH(cx - w * 0.22, cy - h / 2 - w * 0.3, w * 0.44, w * 0.5), 180, 180, False, pt)
    F.bloco(c, cx, cy, w, h, None, E.COR, a)
    M.rrect(c, cx - w * 0.32, cy + h * 0.08, w * 0.64, h * 0.32, w * 0.08, E.mix(E.COR, "#000000", 0.18), a)
    M.line(c, cx - w * 0.2, cy + h * 0.16, cx + w * 0.2, cy + h * 0.16, BR, a * 0.7, 4)


def carrinho_mercado(c, x, y, s, a=1.0):
    """carrinho de supermercado de perfil: rodas tocando y, cesta acima, alça atrás (à esquerda). s = largura da cesta"""
    if a <= 0:
        return
    top, bot = y - s * 1.0, y - s * 0.32
    cesta = skia.Path()
    cesta.moveTo(x - s / 2, top); cesta.lineTo(x + s / 2, top); cesta.lineTo(x + s * 0.38, bot); cesta.lineTo(x - s * 0.42, bot); cesta.close()
    c.drawPath(cesta, M.paint(E.mix(E.COR, BR, 0.75), a))
    pt = M.paint(TINTA, a, stroke=max(5, s * 0.03)); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(cesta, pt)
    for k in range(1, 5):
        xx = lerp(x - s / 2, x + s / 2, k / 5)
        M.line(c, xx, top, lerp(x - s * 0.42, x + s * 0.38, k / 5), bot, TINTA, a * 0.5, 3)
    M.line(c, x - s / 2, top, x - s * 0.66, top - s * 0.16, TINTA, a, max(5, s * 0.03))
    M.line(c, x - s * 0.72, top - s * 0.16, x - s * 0.58, top - s * 0.16, E.COR, a, max(9, s * 0.06))
    M.line(c, x - s * 0.4, bot, x - s * 0.36, y - s * 0.08, TINTA, a, max(5, s * 0.03))
    M.line(c, x + s * 0.36, bot, x + s * 0.3, y - s * 0.08, TINTA, a, max(5, s * 0.03))
    for wx in (x - s * 0.36, x + s * 0.3):
        c.drawCircle(wx, y - s * 0.07, s * 0.07, M.paint("#1B1B20", a))


def mala(c, x, y, w, h, a=1.0):
    """mala de rodinhas: canto de baixo à esquerda em (x, y - rodas), rodas tocando y. Devolve o ponto de cima à direita"""
    r = w * 0.09
    if a > 0:
        F.bloco(c, x + w / 2, y - 2 * r - h / 2, w, h, None, E.COR, a)
        for k in (0.33, 0.66):
            M.line(c, x + w * k, y - 2 * r - h * 0.9, x + w * k, y - 2 * r - h * 0.1, E.mix(E.COR, "#000000", 0.25), a, 4)
        for wx in (x + w * 0.2, x + w * 0.8):
            c.drawCircle(wx, y - r, r, M.paint("#1B1B20", a))
    return x + w, y - 2 * r - h


def caminho(c, t, t0, x0, x1, y, rot="d", modulo=None, lado=-1):
    """seta petróleo do deslocamento, logo abaixo do chão"""
    F.vetor(c, t, t0, (x0, y), (x1, y), rot, modulo, F.VEL, 8, lado=lado, size=50)


def mala_forca(c, t, t0, x, y, k=1.0, comp=True, rotulos=True, t_comp=None, t_vert=None):
    """a mala puxada pela alça a 60°, com a força e as componentes. (x, y) = chão embaixo da mala"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    F.chao(c, x - 260 * k, x + 560 * k, y, q)
    P = mala(c, x, y, 180 * k, 230 * k, q)
    L = 340 * k
    B = (P[0] + L * cos(60), P[1] - L * math.sin(math.radians(60)))
    M.line(c, P[0], P[1], P[0] + 420 * k, P[1], TINTA2, 0.7 * q, 4, dash=E.TRACO)
    F.forca(c, t, t0 + 0.4, P, 60, L, "F" if rotulos else None, None, "50 N" if rotulos else None, size=54 * k, lado=-1)
    E.angulo(c, t, t0 + 0.9, P, (P[0] + 200, P[1]), B, "60°", r=95 * k, size=44 * k)
    if comp and t_comp is not None:
        F.vetor(c, t, t_comp, P, (B[0], P[1]), None, None, COMP, 9)
        M.line(c, *B, B[0], P[1], TINTA, 0.5 * ep(t, t_comp, 0.5), 4, dash=E.TRACO)
    if comp and t_vert is not None:
        F.vetor(c, t, t_vert, P, (P[0], B[1]), None, None, CINZA, 9)
        M.line(c, *B, P[0], B[1], TINTA, 0.5 * ep(t, t_vert, 0.5), 4, dash=E.TRACO)
    return P, B


def mini(c, t, t0, cx, cy, ang, escuro=False, rot=None):
    """bloco pequeno no chão com o caminho (petróleo, para a direita) e uma força no ângulo ang"""
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    F.chao(c, cx - 170, cx + 170, cy + 45, q, escuro)
    F.bloco(c, cx, cy, 110, 90, None, "#5A5A66" if escuro else TINTA2, q)
    F.vetor(c, t, t0, (cx - 130, cy + 95), (cx + 130, cy + 95), None, None, F.VEL, 7, escuro=escuro)
    P = (cx, cy - 45) if ang == 90 else ((cx + 55, cy) if ang == 0 else (cx - 55, cy))
    F.forca(c, t, t0 + 0.3, P, ang, 130, rot, escuro=escuro)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        cx, cy = 1400, 640
        E.foco(c, t, C["s01.a"] + 0.3, 0.6, lambda a: mochila(c, cx, cy, 250, a))
        F.forca(c, t, C["s01.a"] + 1.0, (cx, cy - 230), 90, 190, "F", size=60, lado=-1)
        E.foco(c, t, C["s01.a"] + 1.6, 0.5, lambda a: F.cronometro(c, 1740, 330, 95, 50, a, "10 min"))
        E.frase(c, t, C["s01.a"], [("segurar", "i", 90), ("parado", "g", 90)], XE, 290)
        E.frase(c, t, C["s01.a"] + 1.4, [("por", "i", 80), ("10", "g", 80, COR), ("minutos", "i", 80)], XE, 410)
        E.frase(c, t, C["s01.b"], [("o", "i", 84), ("braço", "i", 84), ("cansa", "g", 84)], XE, 560)
        E.frase(c, t, C["s01.c"] - 1.6, ps("para a Física:", "i", 70, TINTA2), XE, 720, passo=0.1)
        E.frase(c, t, C["s01.c"], [("trabalho", "g", 124), ("zero", "g", 124, COR)], XE, 870)
        pilula_em(c, t, C["s01.c"] + 0.3, "d = 0", cx, cy + 250, 52, TINTA)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        tb = C["s02.a"] + 0.4
        E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
        itens = (("s02.a", "calcular o trabalho", 1.4, True), ("s02.b", "zero ou negativo", 0, False), ("s02.c", "área do gráfico", 0, False))
        for i, (k, s, dt, forte) in enumerate(itens):
            y = 450 + i * 160
            E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a),
                                                            centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
            E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if forte else TINTA)], XE + 110, y)


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    def newton(a, x, y):
        F.medida(c, 10, "N", x - 70, y + 25, 80, COR, a)

    def comp(a, x, y):
        F.seta(c, x - 110, y + 60, x + 30, y - 70, E.COR, a, 8)
        F.seta(c, x - 110, y + 60, x + 30, y + 60, COMP, a, 8)
    lembrete(c, t, C, "s03", (("s03.b", "força se mede em", "newton (N)", None),
                              ("s03.c", "força inclinada, ao longo do chão:", "F · cos θ", "cos 0° = 1   ·   cos 90° = 0   ·   cos 180° = −1")),
             (newton, comp))


# ---------------- o que é trabalho ----------------
def b_ideia(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"], [("trabalho", "g", 120, COR)], XE, 250)
        E.frase(c, t, C["s04.a"], ps("é o que uma força faz", "i", 70), XE, 370, passo=0.12)
        E.frase(c, t, C["s04.a"] + 1.0, ps("quando o corpo", "i", 70) + [("se desloca", "g", 66)], XE, 460, passo=0.12)
        # bloco empurrado que anda
        y = 560
        q = ease_io(prog(t, C["s04.a"] + 0.6, 1.6))
        if t >= C["s04.a"] + 0.2:
            F.chao(c, 1020, 1800, y, ep(t, C["s04.a"] + 0.2, 0.4))
            bx = lerp(1180, 1560, q)
            F.bloco(c, 1180, y - 75, 180, 150, None, TINTA2, 0.18 * ep(t, C["s04.a"] + 1.0, 0.4))
            F.bloco(c, bx, y - 75, 180, 150, None, TINTA2, ep(t, C["s04.a"] + 0.2, 0.4))
            F.seta(c, bx - 260, y - 75, bx - 95, y - 75, E.COR, ep(t, C["s04.a"] + 0.3, 0.3), 10)
            E.foco(c, t, C["s04.a"] + 0.5, 0.4, lambda a: E.escreve(c, "F", bx - 230, y - 105, 56, "g", COR, a))
            caminho(c, t, C["s04.a"] + 2.0, 1180, 1560, y + 60)
        E.frase(c, t, C["s04.b"], ps("sem deslocamento,", "i", 70) + [("sem", "g", 66), ("trabalho", "g", 66)], XE, 640, passo=0.12)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.formula(c, "d = 0  →  τ = 0", XE, 820, 104, "g", TINTA, a))
        E.foco(c, t, C["s04.c"] + 0.4, 0.5, lambda a: mochila(c, 1580, 860, 130, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("mesma", "i", 70), ("direção", "g", 66), ("e", "i", 70), ("mesmo", "i", 70), ("sentido", "g", 66)], XE, 220, passo=0.14)
            y = 470
            if t >= C["s05.a"] + 0.4:
                F.chao(c, 1080, 1780, y, ep(t, C["s05.a"] + 0.4, 0.4))
                E.foco(c, t, C["s05.a"] + 0.4, 0.5, lambda a: F.bloco(c, 1430, y - 70, 170, 140, None, TINTA2, a))
                F.forca(c, t, C["s05.a"] + 0.8, (1515, y - 70), 0, 220, "F", size=56)
                caminho(c, t, C["s05.a"] + 1.2, 1200, 1660, y + 55)
            F.formula_legenda(c, t, C["s05.c"], "τ = F · d", [("τ", "trabalho", "J"), ("F", "força", "N"), ("d", "deslocamento", "m")],
                              XE, 540, 140, tl=[C["s05.c"] + 1.2, C["s05.d"], C["s05.e"]])
            E.frase(c, t, C["s05.b"], [("força", "i", 64, TINTA2), ("×", "g", 60, TINTA2), ("distância", "i", 64, TINTA2)], XE, 320)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.foco(c, t, C["s06.a"], 0.5, lambda a: E.formula(c, "N · m", XE, 330, 130, "g", TINTA, a))
    wn = E.formula(None, "N · m", 0, 0, 130, "g", a=0)
    E.foco(c, t, C["s06.b"], 0.5, lambda a: E.formula(c, " = J", XE + wn, 330, 130, "g", COR, a))
    E.frase(c, t, C["s06.b"] + 0.4, [("joule", "i", 84)], XE + wn + 260, 330)
    y = 720
    if t >= C["s06.c"]:
        F.chao(c, 980, 1820, y, ep(t, C["s06.c"], 0.4))
    E.foco(c, t, C["s06.c"], 0.5, lambda a: carrinho_mercado(c, 1450, y, 300, a))
    F.forca(c, t, C["s06.c"] + 0.5, (1000, y - 330), 0, 220, "F", None, "20 N", size=52)
    caminho(c, t, C["s06.c"] + 1.2, 1080, 1700, y + 55, "d", "10 m")
    E.foco(c, t, C["s06.d"], 0.5, lambda a: E.formula(c, "τ = 20 · 10", XE, 640, 100, "g", TINTA, a))
    bola_txt(c, t, C["s06.d"] + 1.2, "200 J", XE + 300, 830, 120, 70)


# ---------------- força inclinada ----------------
def b_inclinada(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07"], ps("e se a força for", "i", 76) + [("inclinada?", "g", 76, COR)], XE, 220, passo=0.12)
        mala_forca(c, t, C["s07.a"], 1020, 860, 1.0, t_comp=C["s07.c"], t_vert=C["s07.d"])
        E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "alça a 60° do chão", 1560, 760, 44, "b", fundo=TINTA, a=a))
        E.frase(c, t, C["s07.c"], [("só", "i", 64), ("a", "i", 64), ("parte", "i", 64), ("ao longo do chão", "g", 60, COR)], XE, 420, passo=0.12)
        E.frase(c, t, C["s07.c"] + 0.9, [("ajuda", "g", 60, COR), ("a", "i", 64), ("mala", "i", 64), ("a", "i", 64), ("andar", "i", 64)], XE, 510, passo=0.12)
        E.frase(c, t, C["s07.d"], [("a", "i", 60, TINTA2), ("parte", "i", 60, TINTA2), ("para", "i", 60, TINTA2), ("cima", "g", 56, TINTA2)], XE, 650, passo=0.12)
        E.frase(c, t, C["s07.d"] + 0.8, ps("não leva para a frente", "i", 60, TINTA2), XE, 730, passo=0.12)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if C["s08"] <= t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08"], ps("a parte ao longo do chão =", "i", 70), XE, 220, passo=0.12)
            wl = E._arranjo(ps("a parte ao longo do chão =", "i", 70), XE, "left")[0]
            E.formula_em(c, t, C["s08.a"], "F · cos θ", XE + wl + 30, 220, 80, "g", COR)
            F.formula_legenda(c, t, C["s08.b"], "τ = F · d · cos θ", [("τ", "trabalho", "J"), ("F", "força", "N"), ("d", "deslocamento", "m"),
                                                                  ("θ", "ângulo entre F e d", None)],
                              XE, 470, 140, tl=[C["s08.b"] + 0.8, C["s08.b"] + 1.2, C["s08.b"] + 1.6, C["s08.c"]], size_l=50)
            mala_forca(c, t, C["s08.c"] + 0.3, 1290, 900, 0.75, rotulos=False, t_comp=None)
        E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], [("a", "i", 70), ("mala,", "i", 70), ("andando", "i", 70), ("10 m", "g", 66, COR)], XE, 200, passo=0.12)
    E.formula_em(c, t, C["s09.a"], "τ = 50 · 10 · cos 60°", W / 2, 400, 110, "g", TINTA, "center")
    pilula_em(c, t, C["s09.b"], "cos 60° = 1/2", W / 2, 520, 52, E.COR)
    troca(c, t, [(C["s09.c"], "= 500 · f{1}{2}")], lambda s, a: E.formula(c, s, W / 2, 720, 100, "g", TINTA, a, "center"))
    bola_txt(c, t, C["s09.d"], "250 J", W / 2, 940, 100, 62)


# ---------------- zero e negativo ----------------
def b_sinais(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10.a"], [("θ", "g", 110, COR), ("=", "g", 110), ("90°", "g", 110)], XE, 280)
        E.frase(c, t, C["s10.a"] + 0.8, ps("força em pé", "i", 64, TINTA2), XE, 380)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: E.formula(c, "cos 90° = 0", XE, 540, 96, "g", TINTA, a))
        sinal_tau(c, t, C["s10.c"], "0", XE + 170, 680, 60)
        y = 720
        cx = 1400
        if t >= C["s10.a"]:
            F.chao(c, cx - 380, cx + 380, y, ep(t, C["s10.a"], 0.4))
            caminho(c, t, C["s10.a"] + 0.3, cx - 260, cx + 260, y + 60, "d")
        troca_ = t < C["s10.d"]
        E.saida(c, t, C["s10.d"] - 0.1, lambda: (E.foco(c, t, C["s10.a"], 0.5, lambda a: F.bloco(c, cx, y - 80, 190, 160, None, TINTA2, a)),
                                                  F.forca(c, t, C["s10.a"] + 0.4, (cx, y - 160), 90, 260, "F", size=56, lado=-1),
                                                  E.angulo(c, t, C["s10.a"] + 0.9, (cx, y - 160), (cx + 150, y - 160), (cx, y - 400), None, r=60)))
        if not troca_:
            E.foco(c, t, C["s10.d"], 0.5, lambda a: mochila(c, cx, y - 130, 170, a))
            F.forca(c, t, C["s10.d"] + 0.3, (cx, y - 290), 90, 220, "F", size=56, lado=-1)
            E.frase(c, t, C["s10.d"] + 0.4, ps("andando no plano", "i", 56, TINTA2), XE, 830, passo=0.1)
            pilula_em(c, t, C["s10.e"], "não faz trabalho", cx, 960, 48, TINTA2)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if C["s11"] <= t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11.a"], [("θ", "g", 110, COR), ("=", "g", 110), ("180°", "g", 110)], XE, 280)
            E.frase(c, t, C["s11.a"] + 0.8, ps("força contra o movimento", "i", 60, TINTA2), XE, 380, passo=0.1)
            E.foco(c, t, C["s11.b"], 0.5, lambda a: E.formula(c, "cos 180° = −1", XE, 520, 90, "g", TINTA, a))
            sinal_tau(c, t, C["s11.c"], "-", XE + 170, 650, 56)
            y = 600
            cx = 1420
            if t >= C["s11.d"] - 0.6:
                F.chao(c, cx - 420, cx + 420, y, ep(t, C["s11.d"] - 0.6, 0.4))
                caminho(c, t, C["s11.d"] - 0.3, cx - 300, cx + 300, y + 60, "d", "20 m")
            E.foco(c, t, C["s11.d"] - 0.6, 0.5, lambda a: F.carrinho(c, cx, y, 320, a=a))
            F.forca(c, t, C["s11.d"], (cx + 60, y - 240), 180, 320, "F", None, "2.000 N", size=50, lado=-1)
            E.foco(c, t, C["s11.e"], 0.5, lambda a: E.formula(c, "τ = −2.000 · 20 = −40.000 J", W / 2 + 120, 860, 84, "g", TINTA, a, "center"))
            pilula_em(c, t, C["s11.f"], "atrapalha o movimento", W / 2 + 120, 980, 48, F.NEG)
        E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12"], ps("juntando os", "i", 80) + [("sinais", "g", 80, COR)], W / 2, 200, "center", 0.12)
    for i, (k, ang, tipo, nome) in enumerate((("s12.a", 0, "+", "ajuda"), ("s12.b", 180, "-", "atrapalha"), ("s12.c", 90, "0", "perpendicular"))):
        cx = 420 + i * 540
        mini(c, t, C[k], cx, 560, ang)
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, cx=cx, nome=nome: centro(c, nome, cx, 820, 64, "g", TINTA, a))
        sinal_tau(c, t, C[k] + 0.7, tipo, cx, 920, 52)


# ---------------- gráfico F × d ----------------
def b_grafico(c, t, C, b):
    P = F.grafico(c, t, C["s13.a"], 860, 230, 900, 600, 0, 12, 0, 50, "d (m)", "F (N)", passo=2, passo_y=10)
    f1 = lambda x: 20
    f2 = lambda x: 8 * x

    def ret():
        E.curva(c, t, C["s13.c"], P, f1, 0, 10, d=0.8)
        E.area(c, t, C["s13.d"], P, f1, 0, 10)
        E.foco(c, t, C["s13.e"], 0.4, lambda a: F.medida(c, 200, "J", P.x(5), P.y(10) + 20, 64, COR, a, "center"))
    E.saida(c, t, C["s14.b"] - 0.1, ret)
    E.frase(c, t, C["s13.a"], ps("força no eixo vertical", "i", 56), XE, 260, passo=0.1)
    E.frase(c, t, C["s13.b"], ps("deslocamento no horizontal", "i", 56), XE, 340, passo=0.1)

    def txt13():
        E.frase(c, t, C["s13.c"], [("F", "g", 64, COR), ("constante:", "i", 64), ("20 N", "g", 60)], XE, 500, passo=0.12)
        E.frase(c, t, C["s13.d"], [("retângulo", "i", 64), ("20", "g", 60), ("×", "g", 60, TINTA2), ("10", "g", 60)], XE, 610, passo=0.12)
        E.foco(c, t, C["s13.e"], 0.4, lambda a: E.formula(c, "= 200 J", XE, 720, 80, "g", COR, a))
    E.saida(c, t, C["s14"] - 0.1, txt13)
    if t < C["s14"]:
        return
    E.frase(c, t, C["s14.a"], [("área", "g", 70, COR), ("=", "g", 70), ("trabalho", "g", 70)], XE, 500, passo=0.14)
    E.curva(c, t, C["s14.b"], P, f2, 0, 5, d=0.9)
    E.foco(c, t, C["s14.b"] + 0.8, 0.4, lambda a: E.formula(c, "40", P.x(5) + 20, P.y(40) - 10, 50, "g", COR, a))
    E.area(c, t, C["s14.c"], P, f2, 0, 5)
    E.foco(c, t, C["s14.c"], 0.4, lambda a: E.formula(c, "triângulo:  f{base · altura}{2}", XE, 640, 56, "b", TINTA, a))
    E.foco(c, t, C["s14.d"], 0.4, lambda a: E.formula(c, "f{5 · 40}{2} = f{200}{2}", XE, 820, 70, "g", TINTA, a))
    E.foco(c, t, C["s14.e"], 0.4, lambda a: F.medida(c, 100, "J", P.x(3.5), P.y(10) + 20, 64, COR, a, "center"))
    bola_txt(c, t, C["s14.e"], "100 J", XE + 220, 960, 90, 54)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s15.a"], ps("esquecer o cosseno", "i", 76), XE + 480, 200, passo=0.12)

    def s15():
        E.foco(c, t, C["s15.b"], 0.5, lambda a: E.formula(c, "τ = 50 · 10", W / 2, 480, 120, "g", TINTA, a, "center"))
        E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "= 500 J ?", W / 2, 700, 130, "g", ERRADO, a, "center"))
        if t >= C["s15.c"] + 0.8:
            E.risco(c, W / 2 - 300, 720, W / 2 + 300, 600, t, C["s15.c"] + 0.8, largura=12)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    P, B = mala_forca(c, t, C["s16"], 340, 840, 0.95, t_comp=C["s16.b"] - 0.2, t_vert=C["s16.a"])
    E.frase(c, t, C["s16.a"], ps("a parte para cima", "i", 60, TINTA2) + [("não", "g", 56, TINTA2), ("ajuda", "g", 56, TINTA2)], 1000, 380, passo=0.1)
    E.frase(c, t, C["s16.b"], [("só", "i", 64), ("metade", "g", 60, COR), ("trabalha:", "i", 64), ("25 N", "g", 60, COR)], 1000, 500, passo=0.12)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.formula(c, "25 · 10 =", 1000, 660, 90, "g", TINTA, a))
    bola_txt(c, t, C["s16.c"] + 0.4, "250 J", 1560, 630, 110, 64, CERTO)
    E.frase(c, t, C["s16.d"], ps("sem cosseno: só força", "i", 54) + [("no mesmo sentido", "g", 50, COR)] + ps("do caminho", "i", 54),
            W / 2, 1000, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s17():
        E.frase(c, t, C["s17"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 150, "center")
        E.frase(c, t, C["s17.a"], ps("antes da conta:", "i", 70, CLARO) + [("força", "g", 66, BR), ("×", "g", 66, CLARO), ("caminho", "g", 66, BR)],
                W / 2, 280, "center", 0.12)
        mini(c, t, C["s17.b"], 400, 520, 90, True)
        E.foco(c, t, C["s17.b"] + 0.5, 0.4, lambda a: centro(c, "perpendicular", 400, 740, 56, "g", BR, a))
        E.foco(c, t, C["s17.b"] + 0.9, 0.4, lambda a: E.pilula(c, "τ = 0", 400, 840, 52, "g", fundo=TINTA2, a=a))
        mini(c, t, C["s17.c"], 960, 520, 180, True)
        E.foco(c, t, C["s17.c"] + 0.5, 0.4, lambda a: centro(c, "contra", 960, 740, 56, "g", BR, a))
        E.foco(c, t, C["s17.c"] + 0.9, 0.4, lambda a: E.pilula(c, "sinal −", 960, 840, 52, "g", fundo=F.NEG, a=a))
        # o carro e a força do chão
        x, y = 1520, 600
        if t >= C["s17.d"]:
            F.chao(c, x - 230, x + 230, y, ep(t, C["s17.d"], 0.4), True)
        E.foco(c, t, C["s17.d"], 0.5, lambda a: F.carrinho(c, x, y, 260, a=a))
        F.forca(c, t, C["s17.d"] + 0.6, (x, y - 140), 90, 160, None, escuro=True)
        F.vetor(c, t, C["s17.d"] + 0.3, (x - 170, y + 55), (x + 170, y + 55), None, None, F.VEL, 7, escuro=True)
        E.foco(c, t, C["s17.d"] + 1.0, 0.4, lambda a: centro(c, "força do chão", x, 740, 56, "g", BR, a))
        E.foco(c, t, C["s17.e"], 0.4, lambda a: E.pilula(c, "τ = 0", x, 840, 52, "g", fundo=TINTA2, a=a))
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], [("cos 90°", "g", 84, BR), ("=", "g", 84, CLARO), ("0", "g", 84, BR)], W / 2, 320, "center", 0.14)
    E.frase(c, t, C["s18.a"] + 1.0, ps("zera a conta inteira", "i", 76, CLARO), W / 2, 450, "center", 0.12)
    E.frase(c, t, C["s18.b"], [("não", "g", 64, ERRADO), ("compensa:", "i", 70, CLARO)] + ps("força inclinada", "i", 70, CLARO), W / 2, 680, "center", 0.12)
    E.frase(c, t, C["s18.b"] + 1.2, ps("e a questão pede o", "i", 70, CLARO) + [("valor", "g", 66, BR)], W / 2, 780, "center", 0.12)
    E.frase(c, t, lerp(C["s18.b"], C["s18.end"], 0.7), ps("aí, faça a conta com o cosseno", "i", 64, CLARO), W / 2, 920, "center", 0.1)


# ---------------- questão ----------------
def caixote_corda(c, t, t0, x, y, k=1.0, t_chao=None):
    """caixote puxado por corda a 60°, com F = 100 N e d = 8 m. (x, y) = chão no meio do caixote"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    F.chao(c, x - 300 * k, x + 520 * k, y, q)
    w, h = 220 * k, 170 * k
    F.bloco(c, x, y - h / 2, w, h, None, E.COR, q)
    P = (x + w / 2, y - h * 0.55)
    L = 300 * k
    B = (P[0] + L * cos(60), P[1] - L * math.sin(math.radians(60)))
    M.line(c, P[0], P[1], P[0] + 380 * k, P[1], TINTA2, 0.7 * q, 4, dash=E.TRACO)
    F.forca(c, t, t0 + 0.4, P, 60, L, "F", None, "100 N", size=50 * k, lado=1)
    E.angulo(c, t, t0 + 0.9, P, (P[0] + 200, P[1]), B, "60°", r=90 * k, size=42 * k)
    caminho(c, t, t0 + 0.7, x - 200 * k, x + 300 * k, y + 55, "d", "8 m")
    if t_chao is not None:
        F.forca(c, t, t_chao, (x - 40 * k, y - h), 90, 190 * k, None, TINTA2)
        E.foco(c, t, t_chao + 0.4, 0.4, lambda a: E.escreve(c, "do chão", x - 240 * k, y - h - 120 * k, 44, "i", TINTA2, a))


def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s19.a"], ps("corda a", "i", 70) + [("60°", "g", 66, COR)] + ps("do chão", "i", 70), XE, 330, passo=0.12)
    E.frase(c, t, C["s19.b"], [("F", "g", 66, COR), ("=", "g", 66), ("100 N", "g", 66)], XE, 440, passo=0.12)
    E.frase(c, t, C["s19.c"], [("anda", "i", 70), ("8 m", "g", 66)], XE, 540, passo=0.12)
    E.frase(c, t, C["s19.d"], [("τ", "g", 72, COR), ("da", "i", 72), ("corda?", "g", 68)], XE, 700, passo=0.12)
    E.frase(c, t, C["s19.e"], [("τ", "g", 72, COR), ("da", "i", 72), ("força", "i", 72), ("do", "i", 72), ("chão?", "g", 68)], XE, 820, passo=0.12)
    if t < C["s20"]:
        caixote_corda(c, t, C["s19.a"], 1260, 800, 1.0, t_chao=C["s19.e"])
    else:
        E.relogio(c, t, C["s20.a"], cx=1460, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s21():
        E.formula_em(c, t, C["s21.a"], "τ = F · d · cos θ", W / 2, 260, 100, "g", TINTA2, "center")
        E.formula_em(c, t, C["s21.b"], "τ = 100 · 8 · cos 60°", W / 2, 450, 110, "g", TINTA, "center")
        troca(c, t, [(C["s21.c"], "= 800 · f{1}{2}")], lambda s, a: E.formula(c, s, W / 2, 660, 110, "g", TINTA, a, "center"))
        bola_txt(c, t, C["s21.d"], "400 J", W / 2, 880, 125, 72)
    E.saida(c, t, C["s22"] - 0.1, s21)
    if t < C["s22"]:
        return
    caixote_corda(c, t, C["s22"], 640, 820, 0.9, t_chao=C["s22.a"])
    E.frase(c, t, C["s22.a"], [("força", "i", 70), ("do", "i", 70), ("chão:", "i", 70), ("para", "g", 64), ("cima", "g", 64)], 1100, 330, passo=0.12)
    E.frase(c, t, C["s22.b"], [("θ", "g", 80, COR), ("=", "g", 80), ("90°", "g", 80)], 1100, 470, passo=0.12)
    bola_txt(c, t, C["s22.c"], "0 J", 1350, 680, 120, 74, TINTA2)
    E.frase(c, t, C["s22.c"] + 0.6, ps("sem conta nenhuma", "i", 60, TINTA2), 1350, 880, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s23.a", [("τ = F · d · cos θ", "g", 70), ("em", "i", 70), ("joule", "g", 70, COR)]),
                 ("s23.b", [("perpendicular:", "i", 70), ("0", "g", 70), ("·", "g", 70, TINTA2), ("contra:", "i", 70), ("negativo", "g", 70, F.NEG)]),
                 ("s23.c", [("no", "i", 70), ("gráfico,", "i", 70), ("área", "g", 70, COR), ("=", "g", 70), ("trabalho", "g", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s24.a"], [("potência", "g", 130, COR)], XE, 420)
    E.frase(c, t, C["s24.a"] + 0.6, ps("a rapidez do trabalho", "i", 64, TINTA2), XE, 520, passo=0.1)
    E.frase(c, t, C["s24.b"], [("e", "i", 110), ("rendimento", "g", 120, COR)], XE, 700)
    E.foco(c, t, C["s24.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s24.c"] + 0.2, 0.4))
    E.frase(c, t, C["s24.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, inclinada=b_inclinada, sinais=b_sinais, grafico=b_grafico,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
