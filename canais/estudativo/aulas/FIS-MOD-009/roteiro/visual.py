"""Visual — Estudativo · FIS-MOD-009: Big Bang e expansão do Universo.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001 e, para o céu, o da FIS-MOD-008
(janela escura arredondada, ceu). Aqui: galáxia = elipse com brilho (galaxia); a onda de luz de uma galáxia é F.onda na cor
da luz, mais esticada (vermelha) quando se afasta e mais apertada (azul) quando se aproxima; balão com pontinhos para a
expansão; partículas: quark up em laranja, down em petróleo (F.VEL), elétron azul (eletron), fóton = pacote. Todo instante
vem de C[...]."""
import math
import random

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-009_big_bang_expansao_do_universo.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("doppler", "hubble", "expansao", "fundo", "particulas", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
from fractions import Fraction as Fr
assert Fr(2, 3) + Fr(2, 3) - Fr(1, 3) == 1             # próton: up, up, down
assert Fr(2, 3) - Fr(1, 3) - Fr(1, 3) == 0             # nêutron: up, down, down
assert 2000 * 3 == 6000 and 2000 * 2 == 4000           # Hubble por proporção
assert abs(70 / 3.26 * 100 - 2147) < 5                 # H₀ ≈ 70 km/s/Mpc → ~2.100 km/s a 100 milhões de anos-luz ("uns dois mil")
assert abs(2.725 - 273.15 + 270.4) < 0.1               # 2,7 K ≈ −270 °C


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


# ---------------- peças da astronomia (as mesmas em FIS-MOD-008 a 010) ----------------
AMBAR, GIGANTE, ANA, NEUTRON = "#FFB000", "#E2452B", "#DDEBFF", "#5AA9FF"
AZUL = "#2F6BFF"


def ceu(c, x, y, w, h, a=1.0, seed=3, n=70):
    """janela do céu: retângulo escuro arredondado com estrelas paradas"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 36, "#0B0B16", a)
    rnd = random.Random(seed)
    for _ in range(n):
        c.drawCircle(x + 20 + rnd.random() * (w - 40), y + 20 + rnd.random() * (h - 40), rnd.choice((1.5, 2, 2.5, 3.5)), M.paint(BR, a * rnd.uniform(0.4, 0.9)))


def estrela(c, cx, cy, r, cor=AMBAR, a=1.0):
    if a <= 0 or r <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.2, [M.hexc(cor, 0.55 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, r * 2.2, p)
    E.bola(c, cx, cy, r, cor, a)


def galaxia(c, cx, cy, r, cor="#E8D9FF", a=1.0, giro=-20):
    """galáxia: disco achatado com núcleo brilhante"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(giro); c.scale(1, 0.4)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(0, 0), r, [M.hexc(BR, 0.95 * a), M.hexc(cor, 0.6 * a), M.hexc(cor, 0.0)], [0.0, 0.35, 1.0]))
    c.drawCircle(0, 0, r, p)
    c.restore()


def faixa_cores(c, x, y, w, h, a=1.0):
    """faixa do visível: violeta à esquerda, vermelho à direita (comprimento de onda crescendo)"""
    if a <= 0:
        return
    for i in range(120):
        M.rrect(c, x + w * i / 120, y, w / 120 + 1, h, 0, cor_luz(400 + 300 * i / 120), a)


def quark(c, cx, cy, r, s, a=1.0):
    """quark: esfera com a letra u (up, laranja) ou d (down, petróleo)"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, E.COR if s == "u" else F.VEL, a)
    centro(c, s, cx, cy + r * 0.38, r * 1.1, "g", BR, a)


def b_gancho(c, t, C, b):
    def um():
        tv = (1240, 280, 540, 400)
        E.foco(c, t, C["s01.a"], 0.5, lambda a: M.rrect(c, tv[0] - 40, tv[1] - 40, tv[2] + 80, tv[3] + 80, 40, "#3A3A42", a))
        if t >= C["s01.a"]:
            rnd = random.Random(int(t * 12))
            q = ep(t, C["s01.a"], 0.5)
            M.rrect(c, *tv, 20, "#22222A", q)
            for _ in range(500):
                x, y = tv[0] + rnd.random() * tv[2], tv[1] + rnd.random() * tv[3]
                c.drawRect(skia.Rect.MakeXYWH(x, y, 6, 4), M.paint(rnd.choice(("#FFFFFF", "#9A9AA5", "#5A5A66")), q * 0.8))
            if t >= C["s01.b"]:
                for _ in range(8):
                    x, y = tv[0] + rnd.random() * tv[2], tv[1] + rnd.random() * tv[3]
                    c.drawRect(skia.Rect.MakeXYWH(x, y, 8, 6), M.paint(E.COR, ep(t, C["s01.b"], 0.4)))
        E.frase(c, t, C["s01.a"], ps("TV fora de sintonia:", "i", 66) + [("chuvisco", "g", 70)], XE, 300, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("um pedacinho era", "i", 66) + [("luz do começo", "g", 66, COR)], XE, 460, passo=0.12)
        E.frase(c, t, C["s01.b"] + 1.2, ps("do Universo", "i", 66), XE, 560, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("viajando há quase", "i", 62) + [("14 bilhões de anos", "g", 62, COR)], XE, 760, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "desvio para o vermelho"), ("s02.b", "radiação de fundo"), ("s02.c", "partículas do modelo padrão")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        F.poli(c, [(x - 130 + i * 3, y + 26 * math.sin(i * 0.12)) for i in range(80)], 1.0, E.COR, a, 5)

    def f2(a, x, y):
        estrela(c, x, y, 30, AMBAR, a)
    lembrete2(c, t, C, "s03", (("s03.b", "Doppler: fonte que se afasta", "frequência menor"), ("s03.c", "as estrelas fabricam", "elementos pela fusão")), (f1, f2))


# ---------------- o Doppler da luz ----------------
def b_doppler(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04.a"], ps("Doppler vale para a", "i", 70) + [("luz", "g", 70, COR)], XE, 220, passo=0.12)
        E.foco(c, t, C["s04.b"] - 0.6, 0.5, lambda a: faixa_cores(c, XE, 300, 1500, 90, a))
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.escreve(c, "vermelho: maior λ", XE + 1500 - E.larg("vermelho: maior λ", "g", 48), 450, 48, "g", VERM, a))
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.escreve(c, "violeta: menor λ", XE, 450, 48, "g", cor_luz(410), a))
        ceu(c, XE, 520, 1580, 460, ep(t, C["s04.d"] - 0.4, 0.5), seed=6, n=40)
        if t >= C["s04.d"]:
            u = (t - C["s04.d"]) * 30
            E.foco(c, t, C["s04.d"], 0.5, lambda a: galaxia(c, 480 + u, 750, 150, a=a))
            lam = lerp(110, 190, ep(t, C["s04.e"], 1.0))
            cor = E.mix(cor_luz(540), VERM, ep(t, C["s04.e"], 1.0))
            F.onda(c, t, C["s04.d"] + 0.4, 820, 1640, 750, 50, lam, cor, 0.8, velocidade=-80, eixo=False)
            F.seta(c, 650 + u, 900, 420 + u, 900, BR, ep(t, C["s04.d"] + 0.3, 0.4), 6)
            E.foco(c, t, C["s04.d"] + 0.5, 0.4, lambda a: E.escreve(c, "se afasta", 640 + u, 960, 44, "b", BR, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    for i, (k, kk, rot, cor, lam, sentido) in enumerate((("s05", "s05.a", "desvio para o vermelho", VERM, 190, -1), ("s05.b", "s05.c", "desvio para o azul", AZUL, 70, 1))):
        y = 300 + 340 * i
        ceu(c, XE, y - 130, 1580, 260, ep(t, C[k], 0.4), seed=7 + i, n=25)
        if t >= C[k]:
            E.foco(c, t, C[k], 0.5, lambda a, y=y: galaxia(c, 380, y, 110, a=a))
            F.onda(c, t, C[k] + 0.2, 620, 1300, y, 40, lam, cor, 0.8, velocidade=-60, eixo=False)
            F.seta(c, 380, y + 80, 380 + 160 * sentido, y + 80, BR, ep(t, C[k] + 0.3, 0.4), 6)
            E.foco(c, t, C[kk], 0.5, lambda a, y=y, rot=rot, cor=cor: E.pilula(c, rot, 1520, y, 42, "g", fundo=cor, a=a))
    E.frase(c, t, C["s05.d"] - 1.8, ps("medido pelas marcas dos elementos", "i", 54, TINTA2) + ps("(outra aula)", "i", 54, TINTA2), XE, 1000, passo=0.08)


# ---------------- Hubble ----------------
def b_hubble(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06"] + 0.2, [("1929", "g", 130, TINTA), ("Edwin Hubble", "g", 80, COR)], XE, 260, passo=0.3)
        E.frase(c, t, C["s06.b"], ps("quase todas:", "i", 62) + [("desvio para o vermelho", "g", 60, VERM)], XE, 400, passo=0.1)
        E.frase(c, t, C["s06.c"], ps("estão se", "i", 62) + [("afastando", "g", 62)], XE, 510, passo=0.12)
        E.frase(c, t, C["s06.d"], ps("mais longe,", "i", 66) + [("mais depressa", "g", 66, COR)], XE, 680, passo=0.12)
        E.frase(c, t, C["s06.e"], [("2×", "g", 80, COR)] + ps("distância", "i", 66) + [("→", "g", 70, TINTA2), ("2×", "g", 80, COR)] + ps("velocidade", "i", 66), XE, 820, passo=0.12)
        P = E.plano(c, t, C["s06.d"], 1180, 300, 580, 560, 0, 3, 0, 3, passo=1, nomes=("distância", "velocidade"), rotulos=False)
        E.curva(c, t, C["s06.d"] + 0.5, P, lambda x: x, 0, 2.9, 1.0)
        for k, (x, y) in enumerate(((0.6, 0.65), (1.2, 1.1), (1.7, 1.8), (2.3, 2.2), (2.7, 2.8))):
            E.ponto(c, t, C["s06.d"] + 0.6 + 0.2 * k, P, x, y, None, cor=VERM, r=11)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], ps("distâncias em", "i", 70) + [("anos-luz", "g", 76, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s07.b"], ps("a distância que a luz anda em", "i", 58) + [("1 ano", "g", 60)], XE, 320, passo=0.08)
    ceu(c, 170, 400, 520, 480, ep(t, C["s07.c"], 0.4), seed=21, n=30)
    for i, (k, d, v) in enumerate((("s07.c", "100 milhões de anos-luz", "~2.000 km/s"), ("s07.d", "200 milhões de anos-luz", "~4.000 km/s"))):
        y = 520 + 220 * i
        E.foco(c, t, C[k], 0.5, lambda a, y=y, i=i: galaxia(c, 300 + 300 * i, y, 90, a=a))
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, d=d, y=y: E.escreve(c, d, 760, y - 10, 56, "b", TINTA, a))
        q = ease_io(prog(t, C[k] + 0.6, 0.6))
        if q > 0:
            F.seta(c, 760, y + 50, 760 + (380 + 380 * i) * q, y + 50, VERM, 1.0, 10)
            E.foco(c, t, C[k] + 1.0, 0.4, lambda a, v=v, y=y, i=i: E.escreve(c, v, 780 + 380 + 380 * i, y + 66, 56, "g", VERM, a))


# ---------------- expansão ----------------
PONTOS = [(-0.5, -0.3), (0.1, -0.55), (0.55, -0.15), (-0.2, 0.3), (0.35, 0.45), (-0.6, 0.35), (0.0, 0.0)]


def balao(c, cx, cy, r, a=1.0, centro_=6):
    """balão com pontinhos; o de índice centro_ é o "nosso", em laranja"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx - r * 0.3, cy - r * 0.35), r * 1.3, [M.hexc("#FFE1D3", a), M.hexc("#F5A98A", a)], [0.0, 1.0]))
    c.drawCircle(cx, cy, r, p)
    M.line(c, cx, cy + r, cx - 10, cy + r + 30, "#C9714F", a, 8)
    for i, (dx, dy) in enumerate(PONTOS):
        c.drawCircle(cx + dx * r, cy + dy * r, max(6, r * 0.05), M.paint(E.COR if i == centro_ else TINTA, a))


def b_expansao(c, t, C, b):
    def s08():
        E.frase(c, t, C["s08.a"], ps("se expande o", "i", 70) + [("próprio espaço", "g", 70, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s08.b"], ps("um", "i", 66) + [("balão", "g", 66)] + ps("com pontinhos", "i", 66), XE, 340, passo=0.12)
        r = lerp(160, 300, ease_io(prog(t, C["s08.c"], 2.0)))
        E.foco(c, t, C["s08.b"], 0.5, lambda a: balao(c, 1350, 600, r, a))
        if t >= C["s08.d"]:
            q = ep(t, C["s08.d"], 0.5)
            for i, (dx, dy) in enumerate(PONTOS[:-1]):
                d = math.hypot(dx, dy)
                F.seta(c, 1350 + dx * r * 0.35, 600 + dy * r * 0.35, 1350 + dx * r * 0.95, 600 + dy * r * 0.95, TINTA2, q * 0.8, 5)
        E.frase(c, t, C["s08.c"], ps("encha o balão:", "i", 62), XE, 500, passo=0.1)
        E.frase(c, t, C["s08.d"], ps("todos se", "i", 62) + [("afastam", "g", 62)], XE, 610, passo=0.1)
        E.frase(c, t, C["s08.e"], ps("os mais longe,", "i", 62) + [("mais depressa", "g", 62, COR)], XE, 720, passo=0.1)
        E.foco(c, t, C["s08.f"], 0.5, lambda a: E.pilula(c, "nenhum pontinho é o centro", XE + 330, 870, 50, "g", fundo=TINTA, a=a))
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"], ps("rode o filme", "i", 70) + [("para trás", "g", 70, COR)], XE, 220, passo=0.12)
    k = 1 - ep(t, C["s09.b"], 2.0)
    for i in range(14):
        g = i * 2.4
        rr = 60 + 340 * k * ((i * 0.37) % 1 + 0.3)
        E.foco(c, t, C["s09.a"], 0.4, lambda a, g=g, rr=rr: galaxia(c, 1350 + math.cos(g) * rr, 560 + math.sin(g) * rr * 0.7, 50, a=a))
    if t >= C["s09.c"]:
        q = ep(t, C["s09.c"], 1.0)
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(1350, 560), 300, [M.hexc(BR, q), M.hexc(AMBAR, 0.8 * q), M.hexc(E.COR, 0.0)], [0.0, 0.4, 1.0]))
        c.drawCircle(1350, 560, 300, p)
    E.frase(c, t, C["s09.b"], ps("antes, tudo mais", "i", 62) + [("junto", "g", 62)], XE, 360, passo=0.1)
    E.frase(c, t, C["s09.c"], [("mais denso", "g", 62), ("e", "i", 62), ("mais quente", "g", 62, COR)], XE, 470, passo=0.12)
    E.frase(c, t, C["s09.d"], ps("há", "i", 66) + [("13,8 bilhões de anos", "g", 66, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s09.e"], ps("quentíssimo e apertado", "i", 58), XE, 750, passo=0.08)
    E.frase(c, t, C["s09.f"], [("Big Bang:", "g", 84, COR)] + ps("o começo da expansão", "i", 66), XE, 900, passo=0.12)


# ---------------- radiação de fundo ----------------
def b_fundo(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10.a"], ps("começo quente", "i", 70) + [("deixou luz", "g", 70, COR)], XE, 220, passo=0.12)
        E.frase(c, t, C["s10.b"], [("380 mil anos", "g", 64)] + ps("depois: a luz anda livre", "i", 60), XE, 340, passo=0.1)
        lam = lerp(60, 260, ep(t, C["s10.d"], 2.0))
        cor = E.mix(AMBAR, "#8C96A3", ep(t, C["s10.d"], 2.0))
        F.onda(c, t, C["s10.c"], 260, 1700, 640, 60, lam, cor, 1.0, velocidade=-90, eixo=False)
        E.frase(c, t, C["s10.c"], ps("viaja até hoje", "i", 60), XE, 840, passo=0.1)
        E.frase(c, t, C["s10.d"], ps("esticada até virar", "i", 60) + [("micro-ondas", "g", 64, COR)], XE, 950, passo=0.1)
        E.foco(c, t, C["s10.d"] + 2.0, 0.5, lambda a: E.pilula(c, "ondas bem mais compridas, como as do forno", 1300, 860, 40, "b", fundo=TINTA, a=a))
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.frase(c, t, C["s11.a"], [("1965:", "g", 80, COR)] + ps("um chiado de todas as direções", "i", 62), XE, 220, passo=0.12)
    ceu(c, 1100, 300, 640, 420, ep(t, C["s11.a"], 0.5), seed=12, n=30)
    if t >= C["s11.a"] + 0.5:
        for k in range(12):
            g = math.radians(30 * k)
            u = ((t - C["s11.a"]) * 0.6 + k * 0.08) % 1
            F.seta(c, 1420 + math.cos(g) * 300 * (1 - u), 510 + math.sin(g) * 190 * (1 - u), 1420 + math.cos(g) * 290 * (1 - u) * 0.8, 510 + math.sin(g) * 180 * (1 - u) * 0.8, "#C9C2B0", 0.8, 4)
    E.frase(c, t, C["s11.b"], [("radiação cósmica", "g", 70, COR)], XE, 380)
    E.frase(c, t, C["s11.b"] + 0.5, [("de fundo", "g", 70, COR)], XE, 470)
    E.frase(c, t, C["s11.c"], ps("como", "i", 62) + [("−270 °C", "g", 66)], XE, 610, passo=0.12)
    E.frase(c, t, C["s11.d"], ps("as duas", "i", 66) + [("grandes provas", "g", 66, COR)], XE, 800, passo=0.12)
    E.foco(c, t, C["s11.e"], 0.5, lambda a: (E.pilula(c, "desvio para o vermelho", XE + 280, 910, 46, "g", fundo=VERM, a=a),
                                             E.pilula(c, "radiação de fundo", XE + 820, 910, 46, "g", fundo=E.COR, a=a)))


# ---------------- partículas ----------------
def b_particulas(c, t, C, b):
    def s12():
        E.frase(c, t, C["s12.a"], ps("as partículas mais básicas:", "i", 62), XE, 220, passo=0.1)
        E.frase(c, t, C["s12.b"], [("modelo", "g", 90, COR), ("padrão", "g", 90, COR)], XE, 350, passo=0.15)
        E.frase(c, t, C["s12.c"], ps("matéria:", "i", 64) + [("quarks", "g", 64)] + ps("e", "i", 64) + [("léptons", "g", 64)], XE, 500, passo=0.12)
        E.foco(c, t, C["s12.d"], 0.5, lambda a: (eletron(c, XE + 40, 620, 30, a), E.escreve(c, "elétron: um lépton", XE + 100, 640, 56, "b", TINTA, a)))
        E.frase(c, t, C["s12.e"], [("próton", "g", 62, COR)] + ps("e", "i", 62) + [("nêutron:", "g", 62)] + ps("3 quarks cada", "i", 62), XE, 800, passo=0.12)
        for i in range(3):
            E.foco(c, t, C["s12.e"] + 0.8 + 0.2 * i, 0.4, lambda a, i=i: E.bola(c, 1350 + 110 * (i - 1), 560 + (40 if i == 1 else 0), 46, "#9AA0A8", a))
        c.drawCircle(1350, 580, 170, M.paint(TINTA2, ep(t, C["s12.e"] + 0.6, 0.4) * 0.6, stroke=4)) if t >= C["s12.e"] + 0.6 else None
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], ps("dois tipos de quark:", "i", 64), XE, 200, passo=0.1)
    E.foco(c, t, C["s13.b"], 0.5, lambda a: (quark(c, XE + 50, 300, 46, "u", a), E.escreve(c, "up:", XE + 120, 320, 60, "g", TINTA, a),
                                             E.formula(c, "+f{2}{3}", XE + 260, 320, 66, "g", COR, a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: (quark(c, XE + 650, 300, 46, "d", a), E.escreve(c, "down:", XE + 720, 320, 60, "g", TINTA, a),
                                             E.formula(c, "−f{1}{3}", XE + 920, 320, 66, "g", F.VEL, a)))
    for i, s in enumerate("uud"):
        E.foco(c, t, C["s13.d"] + 0.2 * i, 0.4, lambda a, i=i, s=s: quark(c, 1450 + 100 * (i - 1), 560 + (50 if i == 1 else 0), 46, s, a))
    if t >= C["s13.d"]:
        c.drawCircle(1450, 580, 160, M.paint(E.COR, ep(t, C["s13.d"], 0.4), stroke=5))
    E.frase(c, t, C["s13.d"], [("próton:", "g", 62, COR)] + ps("up, up, down", "i", 62), XE, 500, passo=0.1)
    E.formula_em(c, t, C["s13.e"], "f{2}{3} + f{2}{3} − f{1}{3} = 1", XE, 650, 84, "g", TINTA)
    E.frase(c, t, C["s13.f"], ps("as forças:", "i", 62) + [("bósons", "g", 64, COR)], XE, 830, passo=0.1)
    E.foco(c, t, C["s13.g"], 0.5, lambda a: (pacote(c, XE + 120, 940, 0, E.COR, a, n=3, amp=18, lam=30, largura=6),
                                             E.escreve(c, "fóton: força elétrica e magnética", XE + 260, 960, 50, "b", TINTA, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], ps("Big Bang", "i", 70) + [("não", "g", 70, ERRADO)] + ps("é bomba num ponto", "i", 70), XE + 480, 200, passo=0.12)
    E.foco(c, t, C["s14.a"] + 0.8, 0.5, lambda a: (ceu(c, 200, 300, 620, 420, a, seed=13, n=30), estrela(c, 510, 510, 40, AMBAR, a)))
    if t >= C["s14.a"] + 1.2:
        for k in range(8):
            g = math.radians(45 * k)
            F.seta(c, 510 + math.cos(g) * 60, 510 + math.sin(g) * 60, 510 + math.cos(g) * 170, 510 + math.sin(g) * 170, AMBAR, 1.0, 6)
    E.foco(c, t, C["s14.b"], 0.5, lambda a: E.selo(c, 760, 360, 50, False, a))
    E.frase(c, t, C["s14.b"], ps("sem centro, sem lado de fora", "i", 56), 960, 380, passo=0.08)
    E.frase(c, t, C["s14.c"], ps("o", "i", 62) + [("espaço inteiro", "g", 62, COR)] + ps("se estica", "i", 62), 960, 500, passo=0.1)
    r = lerp(150, 230, ep(t, C["s14.c"], 1.5))
    E.foco(c, t, C["s14.c"] + 0.3, 0.5, lambda a: balao(c, 1380, 780, r, a))
    E.frase(c, t, C["s14.d"], ps("de qualquer galáxia, as outras se afastam", "i", 52), XE, 1010, passo=0.06)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center")
    E.frase(c, t, C["s15.a"], [("Vermelho", "g", 90, "#FF5A4F"), ("=", "g", 90, CLARO), ("Vai embora", "g", 90, BR)], W / 2, 330, "center", 0.15)
    E.frase(c, t, C["s15.b"], [("Azul", "g", 90, "#6E9BFF"), ("=", "g", 90, CLARO), ("Aproxima", "g", 90, BR)], W / 2, 480, "center", 0.15)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: (E.risco(c, 790, 500, 850, 500, t, C["s15.c"], "#6E9BFF", 8), E.risco(c, 1110, 500, 1170, 500, t, C["s15.c"], "#6E9BFF", 8)))
    E.frase(c, t, C["s15.c"] + 0.3, ps("a mesma letra", "i", 56, CLARO), W / 2, 580, "center", 0.1)
    E.frase(c, t, C["s15.e"], [("afastou", "g", 60, BR), ("→", "g", 60, CLARO), ("f menor", "g", 60, BR), ("→", "g", 60, CLARO), ("λ maior", "g", 60, BR),
                               ("→", "g", 60, CLARO), ("vermelho", "g", 60, "#FF5A4F")], W / 2, 760, "center", 0.12)
    E.frase(c, t, C["s15.f"], [("radiação de fundo:", "g", 52, ERRADO)] + ps("esticada pela expansão, de todos os lados", "i", 54, CLARO), W / 2, 950, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], ps("galáxia se afasta a", "i", 62) + [("2.000 km/s", "g", 62)], XE, 330, passo=0.1)
    E.frase(c, t, C["s16.b"], ps("outra no", "i", 62) + [("triplo da distância", "g", 62, COR)], XE, 440, passo=0.1)
    E.frase(c, t, C["s16.c"], [("velocidade?", "g", 64, COR)], XE, 570)
    E.frase(c, t, C["s16.d"], ps("luz:", "i", 62) + [("vermelho", "g", 62, VERM)] + ps("ou", "i", 62) + [("azul?", "g", 62, AZUL)], XE, 680, passo=0.1)
    E.frase(c, t, C["s16.e"], [("nêutron", "g", 62)] + ps("(up, down, down):", "i", 58) + [("carga?", "g", 62, COR)], XE, 810, passo=0.1)
    if t < C["s17"]:
        E.foco(c, t, C["s16.a"], 0.5, lambda a: (ceu(c, 1250, 300, 560, 380, a, seed=15, n=25), galaxia(c, 1400, 430, 70, a=a), galaxia(c, 1680, 580, 70, a=a)))
    else:
        E.relogio(c, t, C["s17.a"], cx=1530, cy=470, r=180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.frase(c, t, C["s18.a"], ps("velocidade", "i", 70) + [("proporcional", "g", 70, COR)] + ps("à distância", "i", 70), XE, 240, passo=0.12)
        E.frase(c, t, C["s18.b"], [("3×", "g", 90, COR)] + ps("distância", "i", 70) + [("→", "g", 70, TINTA2), ("3×", "g", 90, COR)] + ps("velocidade", "i", 70), XE, 400, passo=0.12)
        E.formula_em(c, t, C["s18.c"] - 0.4, "3 × 2.000", XE, 580, 90, "g", TINTA2)
        bola_txt(c, t, C["s18.c"], "6.000", "km/s", 1450, 560, 180, 54)
        E.frase(c, t, C["s18.d"], ps("se afasta:", "i", 66), XE, 800, passo=0.1)
        E.foco(c, t, C["s18.e"], 0.5, lambda a: E.pilula(c, "desvio para o vermelho", XE + 680, 780, 54, "g", fundo=VERM, a=a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19.a"], [("nêutron:", "g", 76)] + ps("up, down, down", "i", 70), XE, 240, passo=0.12)
    for i, s in enumerate("udd"):
        E.foco(c, t, C["s19.a"] + 0.3 + 0.2 * i, 0.4, lambda a, i=i, s=s: quark(c, 1450 + 100 * (i - 1), 480 + (50 if i == 1 else 0), 46, s, a))
    E.formula_em(c, t, C["s19.b"], "f{2}{3} − f{1}{3} − f{1}{3}", XE, 470, 96, "g", TINTA)
    E.formula_em(c, t, C["s19.c"], "= f{2}{3} − f{2}{3}", XE, 660, 96, "g", TINTA2)
    bola_txt(c, t, C["s19.d"], "0", "", 1450, 800, 130, 110)
    E.foco(c, t, C["s19.d"] + 0.6, 0.4, lambda a: E.escreve(c, "carga zero: nêutron", XE, 860, 64, "g", COR, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s20", (("s20.a", [("galáxias se afastam:", "i", 66), ("mais longe, mais depressa", "g", 62, COR)]),
                                ("s20.b", [("provas:", "g", 62), ("vermelho", "g", 62, VERM), ("e", "i", 66), ("radiação de fundo", "g", 62, COR)]),
                                ("s20.c", [("matéria:", "g", 62), ("quarks e léptons", "i", 66)])), y0=380, dy=200)
    E.saida(c, t, C["s21"] - 0.1, tela_resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], [("Praticando:", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s21.a"] + 0.4, [("astronomia", "g", 100, COR)], XE, 520)
    for i, s in enumerate(("estrelas", "buracos negros", "expansão")):
        E.foco(c, t, C["s21.b"] + 0.4 * i, 0.4, lambda a, s=s, i=i: E.pilula(c, s, XE + 130 + 370 * i, 700, 44, "g", fundo=TINTA, a=a))
    inscreva(c, t, C, "s21")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, doppler=b_doppler, hubble=b_hubble, expansao=b_expansao, fundo=b_fundo,
              particulas=b_particulas, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
