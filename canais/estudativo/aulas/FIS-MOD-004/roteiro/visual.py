"""Visual — Estudativo · FIS-MOD-004: dualidade onda-partícula.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001. Aqui estreia a FENDA DUPLA
(placa em tinta com duas fendas; anteparo à direita: faixas claras e escuras = onda, dois montinhos = partícula) e o
quadro "ONDA x PARTÍCULA" (onda em laranja, partícula com o elétron azul). Todo instante vem de C[...]."""
import math
import random

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-004_dualidade_onda_particula.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("luz", "broglie", "bola", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
h_ = 6.6e-34
assert abs(9.1e-31 * 7.25e6 - 6.6e-24) < 0.01e-24                 # elétron a ~7 milhões de m/s: Q ≈ 6,6 × 10⁻²⁴
assert abs(h_ / 6.6e-24 - 1e-10) < 1e-22 and -34 - (-24) == -10   # λ = 10⁻¹⁰ m
assert abs(0.06 * 50 - 3) < 1e-12 and abs(h_ / 3 - 2.2e-34) < 1e-46   # bola de tênis: 2,2 × 10⁻³⁴ m
assert 60 * 50 == 3000 and abs((h_ / 3) / (h_ / 3000) - 1000) < 1e-6 # erro do grama: mil vezes menor
assert abs(h_ / 3.3e-24 - 2e-10) < 1e-22                           # questão: 2 × 10⁻¹⁰ m
assert abs(1.6726e-27 / 9.109e-31 - 1836) < 1                      # próton ≈ 1.836 elétrons ("quase mil oitocentas e quarenta")
assert abs(3.3e-24 / 9.1e-31 - 3.6e6) < 0.1e6                      # o elétron da questão anda a ~3,6 milhões de m/s


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- kit da trilha Física Moderna (o mesmo em todas as FIS-MOD; candidatas a fisica.py) ----------------
BR = "#FFFFFF"
LUZ = "#FFB000"   # brilho de fonte de luz (o mesmo da Óptica)
UV = "#8B3CF7"    # ultravioleta
VERM = "#D0202A"  # luz vermelha (não é o vermelho de "errado": vem sempre com a palavra "vermelha")


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def cor_luz(nm):
    """cor aproximada de uma luz visível pelo comprimento de onda em nanômetros (380 a 750)"""
    pts = ((380, (0.55, 0.0, 0.9)), (440, (0.25, 0.1, 1.0)), (490, (0.0, 0.65, 1.0)), (510, (0.0, 0.85, 0.35)),
           (580, (1.0, 0.9, 0.0)), (620, (1.0, 0.45, 0.0)), (660, (0.95, 0.1, 0.05)), (750, (0.6, 0.0, 0.0)))
    nm = max(380, min(750, nm))
    for (a, ca), (b, cb) in zip(pts, pts[1:]):
        if nm <= b:
            f = (nm - a) / (b - a)
            r, g, bb = (ca[i] + (cb[i] - ca[i]) * f for i in range(3))
            return "#%02X%02X%02X" % (int(r * 255), int(g * 255), int(bb * 255))
    return "#990000"


def pacote(c, x, y, ang, cor, a=1.0, n=3, amp=22, lam=34, largura=5):
    """um fóton parado: n ondas com envelope, centradas em (x, y), andando no ângulo ang (graus, 0 = direita, 90 = cima)"""
    if a <= 0:
        return
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    nx, ny = -uy, ux
    L = n * lam
    path = skia.Path()
    for i in range(61):
        s = -L / 2 + L * i / 60
        env = math.sin(math.pi * i / 60)
        d = amp * env * math.sin(2 * math.pi * s / lam)
        px, py = x + ux * s + nx * d, y + uy * s + ny * d
        path.moveTo(px, py) if i == 0 else path.lineTo(px, py)
    c.drawPath(path, M.paint(cor, a, stroke=largura, cap_round=True))
    F._cabeca(c, x + ux * (L / 2 + 16), y + uy * (L / 2 + 16), ux, uy, 20, cor, a)


def foton(c, t, t0, A, B, cor=None, d=1.0, n=3, amp=22, lam=34, largura=5, fica=False):
    """fóton que viaja de A até B entre t0 e t0 + d; some ao chegar (fica=True: para em B)"""
    if t < t0:
        return
    p = ease_io(prog(t, t0, d))
    if p >= 1 and not fica:
        return
    ang = math.degrees(math.atan2(-(B[1] - A[1]), B[0] - A[0]))
    a = min(1.0, prog(t, t0, 0.2)) * (1.0 if fica else 1 - max(0.0, (p - 0.85) / 0.15))
    pacote(c, lerp(A[0], B[0], p), lerp(A[1], B[1], p), ang, cor or E.COR, a, n, amp, lam, largura)


def jorro(c, t, t0, A, B, cor, periodo=0.5, d=1.1, t1=1e9, **kw):
    """fótons saindo de A para B um atrás do outro, de t0 até t1"""
    if t < t0:
        return
    k0 = int(max(0.0, t - t0 - d) // periodo)
    k = k0
    while t0 + k * periodo <= min(t, t1):
        foton(c, t, t0 + k * periodo, A, B, cor, d, **kw)
        k += 1


def eletron(c, cx, cy, r=26, a=1.0):
    """elétron: esferinha azul com o sinal de menos"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, F.NEG, a)
    M.line(c, cx - r * 0.42, cy, cx + r * 0.42, cy, BR, a, max(3, r * 0.2))


def lampada_fonte(c, cx, cy, r, cor=LUZ, a=1.0, t=0.0):
    """fonte de luz: esfera com brilho pulsando (a mesma linguagem da Óptica)"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    k = r * (2.3 + 0.12 * math.sin(t * 4))
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), k, [M.hexc(cor, 0.55 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, k, p)
    E.bola(c, cx, cy, r, cor, a)


def sol(c, cx, cy, r, a=1.0, t=0.0):
    """o Sol: fonte âmbar com raios em volta"""
    if a <= 0:
        return
    for i in range(12):
        g = math.radians(i * 30 + t * 8)
        M.line(c, cx + math.cos(g) * r * 1.25, cy + math.sin(g) * r * 1.25, cx + math.cos(g) * r * 1.6, cy + math.sin(g) * r * 1.6, LUZ, a, 8)
    lampada_fonte(c, cx, cy, r, LUZ, a, t)


def constante(c, t, t0, x, y, nome, simbolo, valor, size=64, w=None):
    """cartão de constante física: nome em itálico, símbolo laranja e valor em notação científica"""
    w = w or max(620, E.formula(None, valor, 0, 0, size, "g", a=0) + size * 2.4)
    hh = size * 3.1
    p = ep(t, t0, 0.5)
    if p <= 0:
        return
    E.caixa_pontilhada(c, x, y, w, hh, p, prog_=p)
    E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.escreve(c, nome, x + 34, y + size * 1.0, size * 0.62, "i", TINTA2, a))
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: (E.formula(c, simbolo, x + 34, y + size * 2.3, size, "g", COR, a),
                                            E.formula(c, valor, x + 34 + E.formula(None, simbolo + " ", 0, 0, size, "g", a=0), y + size * 2.3, size, "g", TINTA, a)))


def bola_txt(c, t, t0, v, u, cx, cy, r, size, cor=None):
    """resposta na esfera: número pesado e unidade menor"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def promessa(c, t, C, cena, itens):
    """tela do "até o fim da aula": órbita à direita e três itens numerados. itens = [(cue, texto)]"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 450 + i * 160
        dt = 1.4 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 76, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas: itens = [(cue, linha fina, linha forte)]; desenhos[i](a, x, y) desenha à direita da caixa"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 190, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def resumo(c, t, C, cena, itens, y0=350, dy=170):
    """resumo numerado: itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)


def inscreva(c, t, C, cena):
    """inscreva-se com o cursor e "bons estudos!" (as duas últimas marcas da cena final)"""
    E.foco(c, t, C[cena + ".c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[cena + ".c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[cena + ".c"] + 0.2, 0.4))
    E.frase(c, t, C[cena + ".d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def placa_metal(c, x, y, w, h, a=1.0, rotulo=None):
    """placa de metal vista de lado: retângulo cinza com reflexo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 10, "#9AA0A8", a)
    M.rrect(c, x + 8, y + 8, w - 16, h * 0.18, 6, "#C9CED4", a)
    if rotulo:
        centro(c, rotulo, x + w / 2, y + h - 22, min(48, h * 0.4), "b", TINTA, a)


def bola_txt_f(c, t, t0, v, u, cx, cy, h, size, cor=None):
    """resultado com potência de dez numa pílula larga laranja (a esfera não cabe a notação científica)"""
    w = E.formula(None, v + " " + u, 0, 0, size, "g", a=0) + size * 1.4

    def d(a):
        q = ease_back(prog(t, t0, 0.5))
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w * q / 2, cy - h / 2, w * q, h), h / 2, h / 2)
        c.drawRRect(rr, M.paint(cor or E.COR, a))
        wv = E.formula(None, v + " ", 0, 0, size, "g", a=0)
        x0 = cx - (wv + E.formula(None, u, 0, 0, size * 0.75, "b", a=0)) / 2
        E.formula(c, v, x0, cy + size * 0.36, size, "g", E.SOBRE, a)
        E.formula(c, u, x0 + wv, cy + size * 0.36, size * 0.75, "b", E.SOBRE, a)
    E.foco(c, t, t0, 0.5, d)


# ---------------- peças desta aula ----------------
def fendas(c, x, y0, y1, gap=110, a=1.0):
    """placa com duas fendas centradas em (y0 + y1) / 2"""
    if a <= 0:
        return
    ym = (y0 + y1) / 2
    for ya, yb in ((y0, ym - gap / 2 - 14), (ym - gap / 2 + 14, ym + gap / 2 - 14), (ym + gap / 2 + 14, y1)):
        M.rrect(c, x - 12, ya, 24, yb - ya, 4, TINTA, a)


def padrao(y, ym, h, onda=True):
    """intensidade no anteparo: faixas (onda) ou dois montinhos (partícula)"""
    u = (y - ym) / h
    if onda:
        return math.cos(u * 9.5) ** 2 * math.exp(-(u * 2.2) ** 2)
    return math.exp(-((u - 0.18) / 0.1) ** 2) + math.exp(-((u + 0.18) / 0.1) ** 2)


def anteparo(c, x, y0, y1, onda=True, a=1.0, w=60):
    """anteparo de frente: faixas claras e escuras, ou dois montinhos"""
    if a <= 0:
        return
    M.rrect(c, x, y0, w, y1 - y0, 6, "#16161C", a)
    ym, h = (y0 + y1) / 2, (y1 - y0)
    n = 160
    for i in range(n):
        y = y0 + h * i / n
        v = min(1.0, padrao(y, ym, h, onda))
        if v > 0.02:
            M.rrect(c, x, y, w, h / n + 1, 0, E.mix("#16161C", "#FFE7C2", v), a)


def pontos(c, t, t0, d, x, y0, y1, onda=True, n=260, seed=7):
    """elétrons chegando um a um ao anteparo e acumulando no padrão"""
    if t < t0:
        return
    rnd = random.Random(seed)
    ym, h = (y0 + y1) / 2, (y1 - y0)
    k = int(n * min(1.0, (t - t0) / d))
    feitos = 0
    while feitos < k:
        y = rnd.uniform(y0, y1)
        if rnd.random() < padrao(y, ym, h, onda):
            c.drawCircle(x + rnd.uniform(6, 54), y, 4.5, M.paint(F.NEG, 0.9))
            feitos += 1


def montagem(c, t, t0, x, y0, y1, a=1.0):
    """fonte à esquerda, placa com fendas e anteparo à direita"""
    E.foco(c, t, t0, 0.5, lambda a: fendas(c, x + 260, y0, y1, a=a))
    E.foco(c, t, t0 + 0.2, 0.5, lambda a: M.rrect(c, x + 60, (y0 + y1) / 2 - 50, 110, 100, 14, "#55565C", a))


def b_gancho(c, t, C, b):
    x, y0, y1 = 900, 260, 900
    def um():
        montagem(c, t, C["s01.a"], x, y0, y1)
        E.foco(c, t, C["s01.a"] + 0.4, 0.5, lambda a: M.rrect(c, x + 820, y0, 60, y1 - y0, 6, "#16161C", a))
        for k in range(6):
            tk = C["s01.a"] + 0.7 + 0.5 * k
            if tk <= t < tk + 0.6:
                u = (t - tk) / 0.6
                yy = lerp((y0 + y1) / 2, (y0 + y1) / 2 + (-1) ** k * 55, min(1, u * 2))
                eletron(c, lerp(x + 80, x + 820, u), yy, 16, 1.0)
        pontos(c, t, C["s01.a"] + 1.0, max(1.0, C["s01.d"] - C["s01.a"] - 1.0), x + 820, y0, y1, True)
        E.frase(c, t, C["s01.a"], ps("elétrons,", "i", 66) + [("um de cada vez", "g", 60, F.NEG)], XE, 200, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.2, ps("contra", "i", 60) + [("duas fendas", "g", 60)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("bolinhas fariam", "i", 56, TINTA2) + [("2 montinhos", "g", 56, TINTA2)], XE, 960, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("fazem", "i", 76) + [("faixas", "g", 76, COR)], XE, 520, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("a marca de uma", "i", 76) + [("onda", "g", 90, COR)], XE, 680, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "o λ de uma partícula"), ("s02.b", "o que mostra onda"), ("s02.c", "o que mostra partícula")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        E.formula(c, "Q = m · v", x - 40, y + 20, 60, "g", TINTA, a, "center")

    def f2(a, x, y):
        F.poli(c, [(x - 120 + i * 3, y - 10 + 22 * math.sin(i * 0.2)) for i in range(80)], 1.0, E.COR, a, 5)
    lembrete2(c, t, C, "s03", (("s03.b", "quantidade de movimento:", "massa × velocidade"), ("s03.c", "interferência:", "ondas se reforçam ou cancelam")), (f1, f2))


# ---------------- a luz ----------------
def b_luz(c, t, C, b):
    x, y0, y1 = 980, 260, 860
    def s04():
        montagem(c, t, C["s04.a"], x, y0, y1)
        if t >= C["s04.a"] + 0.6:
            F.poli(c, [(x + 170, (y0 + y1) / 2), (x + 250, (y0 + y1) / 2)], ease_io(prog(t, C["s04.a"] + 0.6, 0.4)), E.COR, 1.0, 8)
            for r in range(1, 9):  # frentes de onda saindo das duas fendas
                for yf in ((y0 + y1) / 2 - 55, (y0 + y1) / 2 + 55):
                    q = ep(t, C["s04.a"] + 0.8 + 0.12 * r, 0.3)
                    if q > 0:
                        c.drawArc(skia.Rect.MakeXYWH(x + 270 - 60 * r, yf - 60 * r, 120 * r, 120 * r), -60, 120, False, M.paint(E.COR, 0.35 * q, stroke=4))
        E.foco(c, t, C["s04.b"], 0.6, lambda a: anteparo(c, x + 760, y0, y1, True, a))
        E.frase(c, t, C["s04.a"], [("Young,", "g", 70), ("começo do século XIX", "i", 62, TINTA2)], XE, 220, passo=0.15)
        E.frase(c, t, C["s04.a"] + 1.0, ps("luz por", "i", 64) + [("duas fendas", "g", 62)], XE, 320, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("faixas claras e escuras", "i", 60), XE, 450, passo=0.1)
        E.frase(c, t, C["s04.c"], [("clara:", "g", 56)] + ps("se reforçam", "i", 60), XE, 560, passo=0.1)
        E.frase(c, t, C["s04.c"] + 1.0, [("escura:", "g", 56)] + ps("se cancelam", "i", 60), XE, 650, passo=0.1)
        E.frase(c, t, C["s04.d"], ps("interferência é coisa de onda", "i", 58), XE, 800, passo=0.08)
        E.foco(c, t, C["s04.e"], 0.5, lambda a: E.pilula(c, "a luz é ONDA", XE + 260, 910, 64, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if C["s05"] <= t < C["s06"]:
        def s05():
            placa_metal(c, 1100, 760, 600, 90, ep(t, C["s05"], 0.5), "metal")
            if t >= C["s05.a"]:
                k = int((t - C["s05.a"]) // 0.9)
                for j in range(max(0, k - 2), k + 1):
                    t0 = C["s05.a"] + 0.9 * j
                    foton(c, t, t0, (1100, 480), (1340 + 30 * (j % 3), 740), UV, 0.8, n=3, amp=12, lam=18, largura=4)
                    if t >= t0 + 0.8:
                        u = ease_out(prog(t, t0 + 0.8, 1.0))
                        eletron(c, lerp(1350 + 30 * (j % 3), 1600, u), lerp(750, 470, u), 22, min(1, u * 5) * (1 - prog(t, t0 + 2.2, 0.4)))
            E.frase(c, t, C["s05.a"], ps("fotoelétrico:", "i", 64) + [("1 fóton → 1 elétron", "g", 60)], XE, 260, passo=0.12)
            E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "PARTÍCULA", XE + 230, 400, 64, "g", fundo=F.NEG, a=a))
            E.frase(c, t, C["s05.c"], ps("a luz é", "i", 76) + [("as duas coisas", "g", 76, COR)], XE, 580, passo=0.12)
            E.frase(c, t, C["s05.d"], ps("cada experimento mostra um lado", "i", 58, TINTA2), XE, 690, passo=0.08)
            E.frase(c, t, C["s05.e"], [("dualidade", "g", 90, COR)], XE, 860)
            E.frase(c, t, C["s05.e"] + 0.5, [("onda-partícula", "g", 70, COR)], XE, 960)
        E.saida(c, t, C["s06"] - 0.1, s05)
    if t < C["s06"]:
        return
    E.frase(c, t, C["s06"], ps("a regra para a prova", "i", 70, COR), W / 2, 180, "center", 0.12)
    for i, (x, kk, kt, titulo, cor, itens) in enumerate(((180, "s06.a", "s06.b", "ONDA", E.COR, ("se espalha, contorna, interfere", "interferência · difração")),
                                                         (1000, "s06.c", "s06.d", "PARTÍCULA", F.NEG, ("troca energia num ponto", "efeito fotoelétrico")))):
        p = ep(t, C[kk], 0.5)
        E.caixa_pontilhada(c, x, 260, 740, 700, p, prog_=p)
        if t < C[kk]:
            continue
        E.foco(c, t, C[kt], 0.5, lambda a, x=x, titulo=titulo, cor=cor: E.pilula(c, titulo, x + 370, 340, 64, "g", fundo=cor, a=a))
        E.frase(c, t, C[kk] + 0.2, ps(itens[0], "i", 50), x + 370, 480, "center", 0.08)
        E.foco(c, t, C[kt] + 0.4, 0.5, lambda a, x=x, s=itens[1]: centro(c, s, x + 370, 880, 46, "g", TINTA, a))
        if i == 0:
            E.foco(c, t, C[kk] + 0.4, 0.5, lambda a, x=x: anteparo(c, x + 340, 560, 820, True, a))
        else:
            E.foco(c, t, C[kk] + 0.4, 0.5, lambda a, x=x: (placa_metal(c, x + 200, 760, 340, 60, a), eletron(c, x + 440, 620, 30, a)))
            foton(c, t, C[kk] + 0.5, (x + 150, 560), (x + 330, 740), UV, 0.8, n=3, amp=12, lam=18, largura=4, fica=True)


# ---------------- de Broglie ----------------
def b_broglie(c, t, C, b):
    def s07():
        E.frase(c, t, C["s07"] + 0.2, [("1924", "g", 140, TINTA)], XE, 270)
        E.frase(c, t, C["s07.a"], [("Louis", "g", 76), ("de Broglie", "g", 76, COR)], XE, 420, passo=0.15)
        E.frase(c, t, C["s07.a"] + 1.0, ps("a pergunta ao contrário", "i", 62, TINTA2), XE, 520, passo=0.1)
        E.frase(c, t, C["s07.b"], [("onda", "g", 70, E.COR), ("→", "g", 70, TINTA2)] + ps("age como partícula", "i", 70), XE, 680, passo=0.12)
        E.frase(c, t, C["s07.c"], [("partícula", "g", 70, F.NEG), ("→", "g", 70, TINTA2)] + ps("age como onda?", "i", 70), XE, 800, passo=0.12)
        E.foco(c, t, C["s07.d"], 0.5, lambda a: E.selo(c, 1500, 760, 70, True, a))
        E.foco(c, t, C["s07.c"] + 0.4, 0.5, lambda a: eletron(c, 1500, 420, 50, a))
        if t >= C["s07.d"]:
            F.onda(c, t, C["s07.d"], 1300, 1720, 420, 50, 105, E.COR, 1.0, velocidade=60, eixo=False)
            eletron(c, 1500, 420, 50, 1.0)
    E.saida(c, t, C["s08"] - 0.1, s07)
    if t < C["s08"]:
        return
    F.formula_legenda(c, t, C["s08.a"], "λ = f{h}{m · v}", [("λ", "comprimento de onda", "m"), ("h", "constante de Planck", "J·s"), ("m · v", "quantidade de movimento, Q", "kg·m/s")],
                      XE, 330, 150, tl=[C["s08.e"], C["s08.d"], C["s08.b"]], size_l=56, dy=96)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "= f{h}{Q}", XE + 660, 330, 150, "g", COR, a))
    constante(c, t, C["s08.d"] + 0.4, 1150, 690, "constante de Planck", "h =", "6,6 × 10^{−34} J·s", 60)


# ---------------- o elétron ----------------
def cristal(c, x, y, n, m, passo, a=1.0):
    """átomos de um cristal enfileirados"""
    if a <= 0:
        return
    for i in range(n):
        for j in range(m):
            E.bola(c, x + i * passo, y + j * passo, passo * 0.28, "#8C96A3", a)


def b_exemplo(c, t, C, b):
    def s09():
        E.frase(c, t, C["s09"], [("elétron", "g", 76, F.NEG)], XE, 220)
        E.foco(c, t, C["s09.a"], 0.5, lambda a: (E.escreve(c, "v ≈", XE + 360, 220, 66, "g", TINTA2, a), F.medida(c, "7 milhões", "m/s", XE + 500, 220, 66, TINTA, a)))
        E.foco(c, t, C["s09.b"], 0.5, lambda a: (E.escreve(c, "Q =", XE, 360, 76, "g", TINTA2, a), E.formula(c, "6,6 × 10^{−24} kg·m/s", XE + 150, 360, 76, "g", TINTA, a)))
        E.formula_em(c, t, C["s09.b"] + 1.4, "λ = f{6,6 × 10^{−34}}{6,6 × 10^{−24}}", XE, 600, 100, "g", TINTA)
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "6,6 ÷ 6,6 = 1", 1200, 560, 60, "g", TINTA2, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: E.formula(c, "−34 − (−24) = −10", 1200, 660, 60, "g", TINTA2, a))
        bola_txt_f(c, t, C["s09.e"], "λ = 10^{−10}", "m", W / 2, 880, 110, 80)
    E.saida(c, t, C["s10"] - 0.1, s09)
    if t < C["s10"]:
        return
    E.frase(c, t, C["s10.a"], [("10⁻¹⁰ m", "g", 76, COR), ("=", "g", 76, TINTA2)] + ps("tamanho de um átomo", "i", 72), XE, 220, passo=0.12)
    E.frase(c, t, C["s10.a"] + 1.8, ps("difração: fresta do tamanho de", "i", 58) + [("λ", "g", 64, COR)], XE, 340, passo=0.1)
    E.foco(c, t, C["s10.b"], 0.6, lambda a: cristal(c, 1100, 520, 5, 5, 70, a))
    E.frase(c, t, C["s10.b"], ps("cristal: as frestas certas", "i", 58), XE, 470, passo=0.1)
    if t >= C["s10.c"]:
        for k in range(5):
            tk = C["s10.c"] + 0.25 * k
            if t >= tk:
                u = ease_out(prog(t, tk, 0.9))
                ang = math.radians(-30 + 15 * k)
                eletron(c, lerp(800, 1380, min(1, u * 1.6)) + (u > 0.62) * (u - 0.62) * 600 * math.cos(ang), 660 + (u > 0.62) * (u - 0.62) * 600 * math.sin(ang), 16, 1.0)
    E.frase(c, t, C["s10.c"], [("1927:", "g", 64, COR)] + ps("elétrons fazem", "i", 60) + [("difração", "g", 60)], XE, 700, passo=0.1)
    E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "de Broglie estava certo", XE + 360, 860, 54, "g", fundo=CERTO, a=a))


# ---------------- a bola ----------------
def bola_tenis(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    E.bola(c, cx, cy, r, "#D7E33A", a)
    p = M.paint(BR, a, stroke=max(3, r * 0.08))
    c.drawArc(skia.Rect.MakeXYWH(cx - r * 1.5, cy - r * 0.8, r * 1.2, r * 1.6), -50, 100, False, p)
    c.drawArc(skia.Rect.MakeXYWH(cx + r * 0.3, cy - r * 0.8, r * 1.2, r * 1.6), 130, 100, False, p)


def b_bola(c, t, C, b):
    E.frase(c, t, C["s11"], ps("e uma", "i", 76) + [("bola?", "g", 76, COR)], XE, 200, passo=0.12)
    if t >= C["s11.a"]:
        u = (t - C["s11.a"]) * 0.5 % 1
        bola_tenis(c, lerp(1000, 1800, u), 250, 50, ep(t, C["s11.a"], 0.4))
    E.foco(c, t, C["s11.a"] + 0.4, 0.5, lambda a: (F.medida(c, "60", "g", XE, 330, 72, TINTA, a), E.escreve(c, "=", XE + 210, 330, 72, "g", TINTA2, a),
                                                  F.medida(c, "0,06", "kg", XE + 290, 330, 72, TINTA, a), E.escreve(c, "·", XE + 560, 330, 72, "g", TINTA2, a),
                                                  F.medida(c, "50", "m/s", XE + 620, 330, 72, TINTA, a)))
    E.foco(c, t, C["s11.b"], 0.5, lambda a: (E.escreve(c, "Q = 0,06 × 50 =", XE, 480, 76, "g", TINTA, a), E.escreve(c, "3", XE + 640, 480, 76, "g", COR, a)))
    E.formula_em(c, t, C["s11.c"], "λ = f{6,6 × 10^{−34}}{3}", XE, 660, 90, "g", TINTA)
    bola_txt_f(c, t, C["s11.d"], "2,2 × 10^{−34}", "m", 1350, 640, 100, 72)
    E.frase(c, t, C["s11.e"], ps("nenhuma fresta é tão pequena", "i", 64), XE, 880, passo=0.1)
    E.frase(c, t, C["s11.f"], ps("a onda existe, mas", "i", 64) + [("nunca aparece", "g", 64, COR)], XE, 990, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("massa em grama", "i", 76), XE + 480, 200, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "Q = 60 × 50 = 3.000 ?", W / 2, 400, 90, "g", ERRADO, "center")
    E.frase(c, t, C["s12.c"], [("λ", "g", 70, ERRADO)] + ps("sai", "i", 70) + [("mil vezes menor", "g", 70, ERRADO)], W / 2, 540, "center", 0.12)
    if t >= C["s12.c"] + 1.0:
        E.risco(c, W / 2 - 440, 420, W / 2 + 440, 330, t, C["s12.c"] + 1.0, largura=12)
    E.frase(c, t, C["s12.d"], [("h", "g", 76, COR)] + ps("em", "i", 76) + [("J·s", "g", 70)] + ps("é do SI:", "i", 76), XE, 720, passo=0.12)
    E.frase(c, t, C["s12.e"], [("massa", "i", 70), ("em kg,", "g", 70, CERTO), ("velocidade", "i", 70), ("em m/s", "g", 70, CERTO)], XE, 860, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center")
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], [("λ", "g", 90, E.COR)] + ps("inversamente proporcional a", "i", 66, CLARO) + [("Q", "g", 90, BR)], W / 2, 300, "center", 0.12)
        E.frase(c, t, C["s13.b"], [("2×", "g", 90, E.COR), ("v", "g", 90, BR), ("→", "g", 90, CLARO), ("λ", "g", 90, BR), ("÷ 2", "g", 90, E.COR)], W / 2, 460, "center", 0.15)
        # duas ondas: Q e 2Q
        F.onda(c, t, C["s13.b"] + 0.6, 460, 1460, 600, 40, 240, CLARO, 0.9, eixo=False)
        F.onda(c, t, C["s13.b"] + 1.2, 460, 1460, 720, 40, 120, E.COR, 0.9, eixo=False)
        E.foco(c, t, C["s13.b"] + 0.8, 0.4, lambda a: E.escreve(c, "Q", 330, 618, 56, "g", CLARO, a))
        E.foco(c, t, C["s13.b"] + 1.4, 0.4, lambda a: E.escreve(c, "2Q", 300, 738, 56, "g", E.COR, a))
        E.frase(c, t, C["s13.c"], ps("comparar? compare só", "i", 60, CLARO) + [("m · v", "g", 64, BR)], W / 2, 880, "center", 0.1)
        E.frase(c, t, C["s13.d"], [("maior Q", "g", 64, BR), ("→", "g", 64, CLARO), ("menor λ", "g", 64, E.COR)], W / 2, 990, "center", 0.12)
        return
    E.frase(c, t, C["s14.a"], [("próton", "g", 76, E.COR), ("≈", "g", 76, CLARO), ("1.840", "g", 76, BR), ("×", "g", 76, CLARO), ("elétron", "g", 76, "#7FB2FF")],
            W / 2, 320, "center", 0.12)
    E.foco(c, t, C["s14.a"] + 0.4, 0.5, lambda a: (E.bola(c, 700, 520, 80, E.COR, a), centro(c, "+", 700, 548, 80, "g", BR, a), eletron(c, 1220, 520, 22, a)))
    E.frase(c, t, C["s14.b"], ps("mesma velocidade:", "i", 60, CLARO) + [("λ", "g", 70, BR)] + ps("do próton", "i", 60, CLARO) + [("1.840× menor", "g", 64, E.COR)],
            W / 2, 740, "center", 0.1)
    E.frase(c, t, C["s14.c"], [("valor?", "g", 56, ERRADO)] + ps("aí, divida h por Q", "i", 60, CLARO), W / 2, 920, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("elétron:", "g", 70, F.NEG)], XE, 340)
    E.foco(c, t, C["s15.a"] + 0.6, 0.5, lambda a: (E.escreve(c, "Q =", XE, 470, 76, "g", TINTA2, a), E.formula(c, "3,3 × 10^{−24} kg·m/s", XE + 150, 470, 76, "g", TINTA, a)))
    E.frase(c, t, C["s15.b"], [("λ", "g", 80, COR)] + ps("do elétron?", "i", 70), XE, 640, passo=0.12)
    E.frase(c, t, C["s15.c"], [("próton,", "g", 66, E.COR)] + ps("mesma velocidade:", "i", 66), XE, 790, passo=0.1)
    E.frase(c, t, C["s15.c"] + 1.0, [("λ", "g", 70, COR), ("maior", "g", 64)] + ps("ou", "i", 66) + [("menor?", "g", 64)], XE, 900, passo=0.1)
    if t < C["s16"]:
        E.foco(c, t, C["s15.a"], 0.5, lambda a: eletron(c, 1500, 360, 46, a))
        if t >= C["s15.a"] + 0.4:
            F.onda(c, t, C["s15.a"] + 0.4, 1260, 1760, 360, 40, 140, E.COR, 1.0, velocidade=70, eixo=False)
            eletron(c, 1500, 360, 46, 1.0)
    else:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        E.frase(c, t, C["s17"], ps("pelo atalho:", "i", 72, COR), XE, 200)
        E.formula_em(c, t, C["s17.a"], "3,3 = f{6,6}{2}", XE, 360, 96, "g", TINTA)
        E.frase(c, t, C["s17.b"], [("Q ÷ 2", "g", 84), ("→", "g", 84, TINTA2), ("λ × 2", "g", 84, COR)], XE, 540, passo=0.15)
        bola_txt_f(c, t, C["s17.c"], "λ = 2 × 10^{−10}", "m", 1400, 450, 110, 76)
        E.formula_em(c, t, C["s17.d"], "f{6,6 × 10^{−34}}{3,3 × 10^{−24}} = 2 × 10^{−10}", XE, 820, 80, "g", TINTA2)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18.a"], [("próton:", "g", 80, E.COR)] + ps("mesma velocidade, massa muito maior", "i", 66), XE, 240, passo=0.1)
    E.frase(c, t, C["s18.b"], [("Q", "g", 90), ("maior", "g", 90, TINTA)], XE, 420, passo=0.15)
    E.frase(c, t, C["s18.c"], [("λ", "g", 90, COR), ("menor", "g", 90, COR)], XE, 580, passo=0.15)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "≈ 1.840 vezes menor", XE + 380, 740, 60, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s18.a"], 0.5, lambda a: (E.bola(c, 1450, 520, 110, E.COR, a), centro(c, "+", 1450, 556, 100, "g", BR, a)))
    if t >= C["s18.c"]:
        F.onda(c, t, C["s18.c"], 1200, 1700, 800, 30, 26, E.COR, 1.0, velocidade=40, eixo=False, largura=5)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s19", (("s19.a", [("luz e matéria:", "i", 70), ("onda", "g", 70, COR), ("e", "i", 70), ("partícula", "g", 70, F.NEG)]),
                                ("s19.b", [("interferência:", "g", 60, COR), ("onda;", "i", 64), ("fotoelétrico:", "g", 60, F.NEG), ("partícula", "i", 64)]),
                                ("s19.c", [("λ = h ÷ (m · v)", "g", 76)])), y0=380, dy=200)
    E.saida(c, t, C["s20"] - 0.1, tela_resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Relatividade", "g", 110, COR)], XE, 400)
    E.frase(c, t, C["s20.a"] + 0.4, [("restrita", "g", 110, COR)], XE, 530)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: F.cronometro(c, 560, 800, 120, 10 + 3 * math.sin(t), a, " "))
    E.foco(c, t, C["s20.b"] + 0.4, 0.4, lambda a: E.escreve(c, "o tempo passa mais devagar", 720, 820, 50, "i", TINTA, a))
    inscreva(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, luz=b_luz, broglie=b_broglie, exemplo=b_exemplo, bola=b_bola, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
