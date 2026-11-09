"""Visual — Estudativo · FIS-MOD-008: vida das estrelas e buracos negros. Primeira aula de astronomia da trilha.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001. Astronomia: o CÉU é uma janela
escura arredondada no papel (ceu), com estrelas paradas; estrela = esfera com brilho na cor da sua fase (âmbar = como o
Sol, vermelho = gigante vermelha, branco-azulado = anã branca, azul = estrela de nêutrons); buraco negro = disco preto com
anel âmbar; gravidade = seta em tinta para dentro, fusão = seta laranja para fora. Relatividade geral = lençol de malha que
afunda (lencol). Todo instante vem de C[...]."""
import math
import random

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-008_vida_das_estrelas_buracos_negros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("nasce", "fim_estrela", "buraco", "erro", "atalho", "questao", "fim"))

# todas as contas da aula
assert 10 ** 2 == 100 and 100 ** 2 == 10000                 # raio 10× menor → 100×; 100× menor → 10.000×
assert abs(4.6 / 10 - 0.46) < 1e-12                         # 4,6 de ~10 bilhões de anos: "mais ou menos a metade"
assert 1915 < 1919 < 2019
G, Ms, d = 6.67e-11, 1.99e30, 1.5e11
assert G * Ms * 6e24 / d ** 2 == G * Ms * 6e24 / d ** 2     # mesma massa, mesma distância: mesma força (buraco negro no lugar do Sol)


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


def ceu(c, x, y, w, h, a=1.0, seed=3, n=70):
    """janela do céu: retângulo escuro arredondado com estrelas paradas"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 36, "#0B0B16", a)
    rnd = random.Random(seed)
    for _ in range(n):
        c.drawCircle(x + 20 + rnd.random() * (w - 40), y + 20 + rnd.random() * (h - 40), rnd.choice((1.5, 2, 2.5, 3.5)), M.paint(BR, a * rnd.uniform(0.4, 0.9)))


def estrela(c, cx, cy, r, cor=AMBAR, a=1.0):
    """estrela: esfera com brilho na cor da fase"""
    if a <= 0 or r <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.2, [M.hexc(cor, 0.55 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, r * 2.2, p)
    E.bola(c, cx, cy, r, cor, a)


def buraco_negro(c, cx, cy, r, a=1.0, t=0.0):
    """buraco negro: disco preto com anel âmbar girando"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.2, [M.hexc(AMBAR, 0.0), M.hexc(AMBAR, 0.0), M.hexc(AMBAR, 0.55 * a), M.hexc(AMBAR, 0.0)], [0.0, 0.42, 0.55, 1.0]))
    c.drawCircle(cx, cy, r * 2.2, p)
    E.arco(c, cx, cy, r * 1.25, t * 40, 300, AMBAR, r * 0.18, a)
    c.drawCircle(cx, cy, r, M.paint("#000000", a))


def nebulosa(c, cx, cy, s, a=1.0, encolhe=0.0):
    """nuvem de gás: manchas suaves que encolhem para o centro"""
    if a <= 0:
        return
    k = 1 - 0.7 * encolhe
    for i, (dx, dy, r, cor) in enumerate(((-0.4, -0.1, 0.55, "#C86BD8"), (0.35, 0.15, 0.5, "#5AA9FF"), (0.0, 0.3, 0.45, "#E2452B"), (0.1, -0.35, 0.4, "#C86BD8"))):
        p = skia.Paint(AntiAlias=True)
        x, y = cx + dx * s * k, cy + dy * s * k
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(x, y), r * s * k, [M.hexc(cor, 0.45 * a), M.hexc(cor, 0.0)], [0.0, 1.0]))
        c.drawCircle(x, y, r * s * k, p)


def lencol(c, cx, cy, w, h, fundo, a=1.0, s=None, cor=TINTA2):
    """malha esticada vista de frente e de cima, afundando fundo pixels perto do centro"""
    if a <= 0:
        return
    s = s or w * 0.18
    dz = lambda x, y: fundo * math.exp(-(((x - cx) / s) ** 2 + ((y - cy) / (s * 0.45)) ** 2))
    for j in range(9):
        y = cy - h / 2 + h * j / 8
        pts = [(cx - w / 2 + w * i / 60, y + dz(cx - w / 2 + w * i / 60, y)) for i in range(61)]
        F.poli(c, pts, 1.0, cor, a * 0.7, 3)
    for i in range(13):
        x = cx - w / 2 + w * i / 12
        pts = [(x, cy - h / 2 + h * j / 40 + dz(x, cy - h / 2 + h * j / 40)) for j in range(41)]
        F.poli(c, pts, 1.0, cor, a * 0.7, 3)
    return dz


def b_gancho(c, t, C, b):
    def um():
        ceu(c, 980, 140, 800, 560, ep(t, C["s01.a"], 0.5))
        E.foco(c, t, C["s01.a"] + 0.4, 0.6, lambda a: estrela(c, 1380, 420, 90, AMBAR, a))
        E.frase(c, t, C["s01.a"], ps("o", "i", 76) + [("ferro", "g", 80, COR)] + ps("do seu sangue", "i", 76), XE, 280, passo=0.12)
        E.frase(c, t, C["s01.a"] + 1.2, ps("foi fabricado numa", "i", 70) + [("estrela", "g", 70)], XE, 390, passo=0.12)
        E.frase(c, t, C["s01.b"], ps("antes de a Terra existir", "i", 60, TINTA2), XE, 500, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("e algumas terminam onde", "i", 66), XE, 720, passo=0.1)
        E.frase(c, t, C["s01.d"], ps("nem a", "i", 76) + [("luz", "g", 80, COR)] + ps("consegue sair", "i", 76), XE, 840, passo=0.12)
        E.foco(c, t, C["s01.c"] + 0.4, 0.6, lambda a: buraco_negro(c, 1380, 860, 80, a, t))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "a vida de uma estrela"), ("s02.b", "o fim decidido pela massa"), ("s02.c", "o buraco negro")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        E.formula(c, "F = f{G · M · m}{d^2}", x - 40, y + 20, 52, "g", TINTA, a, "center")

    def f2(a, x, y):
        for dx in (-70, 0):
            E.bola(c, x + dx, y, 20, E.COR, a)
        estrela(c, x + 90, y, 20, AMBAR, a)
    lembrete2(c, t, C, "s03", (("s03.b", "a gravidade depende de", "massas e distância²"), ("s03.c", "fusão: núcleos se juntam", "e liberam energia")), (f1, f2))


# ---------------- nascimento e equilíbrio ----------------
def b_nasce(c, t, C, b):
    def s04():
        ceu(c, 1000, 160, 760, 760, ep(t, C["s04"], 0.5), seed=5)
        enc = ease_io(prog(t, C["s04.b"], 2.5))
        E.foco(c, t, C["s04.a"], 0.6, lambda a: nebulosa(c, 1380, 540, 320, a, enc))
        if t >= C["s04.b"]:
            for k in range(8):
                g = math.radians(45 * k)
                F.seta(c, 1380 + math.cos(g) * 330, 540 + math.sin(g) * 330, 1380 + math.cos(g) * 220, 540 + math.sin(g) * 220, BR, ep(t, C["s04.b"], 0.4) * (1 - ep(t, C["s04.e"], 0.4)), 5)
        E.foco(c, t, C["s04.e"], 0.6, lambda a: estrela(c, 1380, 540, 80 * ease_back(prog(t, C["s04.e"], 0.6)), AMBAR, a))
        E.frase(c, t, C["s04.a"], ps("nuvem de gás:", "i", 66) + [("nebulosa", "g", 70, COR)], XE, 240, passo=0.12)
        E.frase(c, t, C["s04.b"], ps("a gravidade puxa para o centro", "i", 58), XE, 380, passo=0.08)
        E.frase(c, t, C["s04.c"], ps("encolhe e", "i", 64) + [("esquenta", "g", 64, COR)], XE, 490, passo=0.12)
        E.frase(c, t, C["s04.d"], ps("centro a", "i", 64) + [("10 milhões de graus", "g", 62)], XE, 640, passo=0.12)
        E.frase(c, t, C["s04.e"], [("fusão:", "g", 64, COR)] + ps("hidrogênio em hélio", "i", 64), XE, 760, passo=0.12)
        E.frase(c, t, C["s04.f"], ps("nasceu uma", "i", 76) + [("estrela", "g", 76, COR)], XE, 900, passo=0.12)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    cx, cy = 1350, 560
    E.foco(c, t, C["s05.a"], 0.6, lambda a: estrela(c, cx, cy, 140, AMBAR, a))
    for k in range(8):
        g = math.radians(45 * k + 22.5)
        if t >= C["s05.b"]:
            F.seta(c, cx + math.cos(g) * 380, cy + math.sin(g) * 380, cx + math.cos(g) * 220, cy + math.sin(g) * 220, TINTA, 1.0, 9, None, ease_io(prog(t, C["s05.b"], 0.5)))
        g2 = math.radians(45 * k)
        if t >= C["s05.c"]:
            F.seta(c, cx + math.cos(g2) * 160, cy + math.sin(g2) * 160, cx + math.cos(g2) * 330, cy + math.sin(g2) * 330, E.COR, 1.0, 9, None, ease_io(prog(t, C["s05.c"], 0.5)))
    E.frase(c, t, C["s05.a"], ps("um", "i", 76) + [("cabo de guerra", "g", 76, COR)], XE, 240, passo=0.12)
    E.frase(c, t, C["s05.b"], [("gravidade:", "g", 62)] + ps("para dentro", "i", 62), XE, 380, passo=0.12)
    E.frase(c, t, C["s05.c"], [("fusão:", "g", 62, COR)] + ps("para fora", "i", 62), XE, 480, passo=0.12)
    E.frase(c, t, C["s05.d"], ps("equilibradas:", "i", 62) + [("estável", "g", 62, CERTO)], XE, 620, passo=0.12)
    E.frase(c, t, C["s05.e"], [("Sol:", "g", 62), ("4,6 bilhões de anos", "g", 62, COR)], XE, 780, passo=0.12)
    E.frase(c, t, C["s05.f"], ps("mais ou menos a metade da vida", "i", 56, TINTA2), XE, 880, passo=0.08)


# ---------------- o fim pela massa ----------------
def b_fim_estrela(c, t, C, b):
    def s06():
        q = ep(t, C["s06.b"], 1.2)
        E.foco(c, t, C["s06.a"], 0.5, lambda a: estrela(c, 1350, 560, lerp(110, 260, q), E.mix(AMBAR, GIGANTE, q), a))
        E.frase(c, t, C["s06.a"], ps("acaba o hidrogênio do centro", "i", 62), XE, 260, passo=0.08)
        E.frase(c, t, C["s06.b"], ps("incha e esfria por fora", "i", 62), XE, 380, passo=0.08)
        E.frase(c, t, C["s06.c"], [("gigante", "g", 84, GIGANTE), ("vermelha", "g", 84, GIGANTE)], XE, 520, passo=0.15)
        E.frase(c, t, C["s06.d"], ps("daqui em diante, quem decide é a", "i", 58) + [("massa", "g", 66, COR)], XE, 720, passo=0.08)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], ps("como o Sol:", "i", 66) + [("até 8 massas solares", "g", 62)], XE, 240, passo=0.12)
            E.frase(c, t, C["s07.b"], ps("solta as camadas de fora", "i", 62), XE, 380, passo=0.08)
            q = ep(t, C["s07.b"], 1.0)
            E.foco(c, t, C["s07.a"], 0.5, lambda a: estrela(c, 1400, 560, lerp(220, 50, ep(t, C["s07.c"], 0.6)), E.mix(GIGANTE, ANA, ep(t, C["s07.c"], 0.6)), a))
            if q > 0:
                for r in (300, 360):
                    c.drawCircle(1400, 560, r * (0.8 + 0.3 * q), M.paint("#C86BD8", 0.5 * (1 - 0.5 * q), stroke=14))
            E.frase(c, t, C["s07.c"], [("anã", "g", 84, TINTA), ("branca", "g", 84, TINTA)], XE, 540, passo=0.15)
            E.frase(c, t, C["s07.d"], ps("do tamanho da", "i", 62) + [("Terra", "g", 62)], XE, 660, passo=0.12)
            E.foco(c, t, C["s07.d"] + 0.6, 0.5, lambda a: (E.bola(c, 1650, 860, 50, "#2F7FD0", a), E.escreve(c, "Terra", 1610, 950, 44, "i", TINTA2, a)))
        E.saida(c, t, C["s08"] - 0.1, s07)
    if C["s08"] <= t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], [("mais de 8", "g", 70, COR)] + ps("massas solares", "i", 64), XE, 240, passo=0.12)
            E.frase(c, t, C["s08.b"], ps("fusão até o", "i", 62) + [("ferro;", "g", 62)] + ps("aí, para", "i", 62), XE, 360, passo=0.1)
            E.frase(c, t, C["s08.c"], ps("o centro desaba e", "i", 62), XE, 480, passo=0.1)
            E.frase(c, t, C["s08.d"], [("supernova", "g", 96, COR)], XE, 610)
            E.frase(c, t, C["s08.e"], ps("espalha os elementos fabricados", "i", 56), XE, 740, passo=0.08)
            E.foco(c, t, C["s08.e"] + 1.6, 0.5, lambda a: E.pilula(c, "o ferro do seu sangue", XE + 330, 860, 50, "g", fundo=TINTA, a=a))
            E.foco(c, t, C["s08.a"], 0.5, lambda a: estrela(c, 1400, 540, 180 * (1 - 0.6 * ep(t, C["s08.c"], 0.5)), GIGANTE, a))
            if t >= C["s08.d"]:
                q = ease_out(prog(t, C["s08.d"], 1.4))
                p = skia.Paint(AntiAlias=True)
                p.setShader(skia.GradientShader.MakeRadial(skia.Point(1400, 540), 80 + 360 * q, [M.hexc(BR, 0.9 * (1 - q * 0.6)), M.hexc(AMBAR, 0.6 * (1 - q * 0.5)), M.hexc(GIGANTE, 0.0)], [0.0, 0.5, 1.0]))
                c.drawCircle(1400, 540, 80 + 360 * q, p)
                rnd = random.Random(9)
                for k in range(26):
                    g = rnd.random() * 2 * math.pi
                    rr = (120 + 300 * q) * rnd.uniform(0.7, 1.1)
                    c.drawCircle(1400 + math.cos(g) * rr, 540 + math.sin(g) * rr, rnd.uniform(5, 10), M.paint(rnd.choice((E.COR, "#8C96A3", AMBAR, NEUTRON)), 1 - 0.5 * q))
        E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09.a"], ps("o que sobra:", "i", 62) + [("estrela de nêutrons", "g", 66, NEUTRON)], XE, 240, passo=0.12)
    E.foco(c, t, C["s09.a"] + 0.4, 0.5, lambda a: estrela(c, 1450, 330, 50, NEUTRON, a))
    E.frase(c, t, C["s09.b"], ps("mais massa que o Sol em", "i", 58) + [("~20 km", "g", 62)], XE, 360, passo=0.1)
    E.frase(c, t, C["s09.c"], ps("1 colher de chá:", "i", 58) + [("bilhões de toneladas", "g", 60, COR)], XE, 480, passo=0.1)
    E.frase(c, t, C["s09.d"], ps("sobra com mais de", "i", 62) + [("3 massas solares", "g", 62)], XE, 680, passo=0.1)
    E.frase(c, t, C["s09.e"], ps("nada segura o desabamento", "i", 58), XE, 790, passo=0.08)
    E.frase(c, t, C["s09.f"], [("buraco negro", "g", 96, TINTA)], XE, 930)
    E.foco(c, t, C["s09.f"], 0.6, lambda a: buraco_negro(c, 1450, 760, 110, a, t))


# ---------------- buraco negro e relatividade geral ----------------
def b_buraco(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10.a"], ps("gravidade de", "i", 66) + [("Einstein,", "g", 66), ("1915", "g", 66, COR)], XE, 220, passo=0.12)
        fundo = 220 * ease_io(prog(t, C["s10.c"], 1.0))
        dz = lencol(c, 1200, 620, 1100, 360, fundo, ep(t, C["s10.b"], 0.5))
        E.frase(c, t, C["s10.b"], ps("um", "i", 66) + [("lençol esticado", "g", 66)], XE, 340, passo=0.12)
        if t >= C["s10.c"]:
            E.bola(c, 1200, 620 + fundo - 60, 60, "#55565C", ep(t, C["s10.c"], 0.4))
        if t >= C["s10.d"]:
            u = prog(t, C["s10.d"], 2.2)
            ang = 3.3 * u
            rr = 420 * (1 - 0.8 * u)
            x, y = 1200 - math.cos(ang) * rr, 620 - math.sin(ang) * rr * 0.4
            E.bola(c, x, y + (dz(x, y) if dz else 0) - 20, 20, E.COR, 1.0)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if C["s11"] <= t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11.a"], ps("a", "i", 66) + [("massa curva o espaço", "g", 66, COR)], XE, 220, passo=0.12)
            E.frase(c, t, C["s11.b"], ps("gravidade = movimento na curva", "i", 58), XE, 330, passo=0.08)
            dz = lencol(c, 1150, 640, 1000, 340, 160, ep(t, C["s11"], 0.4))
            E.foco(c, t, C["s11"], 0.4, lambda a: estrela(c, 1150, 700, 70, AMBAR, a))
            if t >= C["s11.c"]:
                pts = [(650 + i * 10, 520 + 0.0 * i) for i in range(101)]
                pts = [(x, 470 + 140 * math.exp(-((x - 1150) / 230) ** 2) * 0.6 + 0.12 * (x - 650)) for x, _ in pts]
                F.poli(c, pts, ease_io(prog(t, C["s11.c"], 1.0)), E.COR, 1.0, 6)
            E.frase(c, t, C["s11.c"], ps("até a", "i", 66) + [("luz", "g", 66, COR)] + ps("faz a curva", "i", 66), XE, 900, passo=0.12)
            E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "eclipse de 1919", 1450, 980, 46, "g", fundo=TINTA, a=a))
            E.foco(c, t, C["s11.e"], 0.5, lambda a: E.pilula(c, "Sobral, Ceará", 1800 - 140, 900, 46, "g", fundo=E.COR, a=a))
        E.saida(c, t, C["s12"] - 0.1, s11)
    if t < C["s12"]:
        return
    lencol(c, 1250, 560, 1000, 340, 420, ep(t, C["s12"], 0.4), s=150)
    E.foco(c, t, C["s12.a"], 0.5, lambda a: buraco_negro(c, 1250, 900, 60, a, t))
    E.frase(c, t, C["s12.a"], ps("massa tão concentrada:", "i", 58) + [("poço sem fundo", "g", 60, COR)], XE, 220, passo=0.1)
    E.frase(c, t, C["s12.b"], [("horizonte de eventos", "g", 62)], XE, 360)
    E.frase(c, t, C["s12.c"], ps("passou, não sai mais", "i", 60), XE, 480, passo=0.1)
    E.frase(c, t, C["s12.d"], ps("nem a luz, a", "i", 56) + [("300 mil km/s", "g", 58, COR)], XE, 600, passo=0.1)
    E.foco(c, t, C["s12.e"], 0.5, lambda a: E.pilula(c, "2019: a primeira imagem", XE + 300, 760, 50, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("buraco negro não é", "i", 70) + [("aspirador", "g", 70, ERRADO)], XE + 480, 200, passo=0.12)
    E.frase(c, t, C["s13.b"], ps("longe dele: a gravidade de", "i", 58) + [("qualquer corpo de mesma massa", "g", 54)], XE, 340, passo=0.08)
    E.formula_em(c, t, C["s13.c"], "F = f{G · M · m}{d^2}", XE, 520, 100, "g", TINTA)
    E.frase(c, t, C["s13.d"], ps("só massas e distância", "i", 58, TINTA2), XE + 560, 500, passo=0.08)
    cx, cy = 1250, 820
    E.foco(c, t, C["s13.e"], 0.5, lambda a: (estrela(c, cx, cy, 60, AMBAR, a * (1 - ep(t, C["s13.e"] + 1.0, 0.6))), buraco_negro(c, cx, cy, 40, a * ep(t, C["s13.e"] + 1.0, 0.6), t)))
    if t >= C["s13.e"]:
        pt = M.paint(TINTA2, ep(t, C["s13.e"], 0.4) * 0.6, stroke=3)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawOval(skia.Rect.MakeXYWH(cx - 420, cy - 150, 840, 300), pt)
        g = (t - C["s13.e"]) * 0.8
        E.bola(c, cx + 420 * math.cos(g), cy + 150 * math.sin(g), 26, "#2F7FD0", ep(t, C["s13.e"], 0.4))
    E.frase(c, t, C["s13.f"], ps("a Terra:", "i", 60) + [("mesma órbita", "g", 60, CERTO)], XE, 760, passo=0.1)
    E.frase(c, t, C["s13.g"], ps("só que escura e gelada", "i", 56, TINTA2), XE, 870, passo=0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 70, CLARO), XE, 150)
    if t < C["s15"]:
        E.frase(c, t, C["s14.a"], ps("a", "i", 70, CLARO) + [("massa decide tudo", "g", 70, BR)], XE, 260, passo=0.12)
        linhas = (("s14.b", "pouca, como o Sol", (("gigante vermelha", GIGANTE, 70), ("anã branca", ANA, 34)), None),
                  ("s14.c", "muita", (("supernova", AMBAR, 60), ("estrela de nêutrons", NEUTRON, 30)), None),
                  ("s14.d", "enorme", (("supernova", AMBAR, 60), ("buraco negro", None, 40)), None))
        for i, (k, rot, fases, _) in enumerate(linhas):
            y = 430 + 190 * i
            E.foco(c, t, C[k], 0.4, lambda a, rot=rot, y=y: E.escreve(c, rot, XE, y + 16, 54, "g", BR, a))
            for j, (nome, cor, r) in enumerate(fases):
                x = 820 + 540 * j
                if cor:
                    E.foco(c, t, C[k] + 0.3 + 0.4 * j, 0.4, lambda a, x=x, y=y, cor=cor, r=r: estrela(c, x, y, r, cor, a))
                else:
                    E.foco(c, t, C[k] + 0.3 + 0.4 * j, 0.4, lambda a, x=x, y=y, r=r: buraco_negro(c, x, y, r, a, t))
                E.foco(c, t, C[k] + 0.4 + 0.4 * j, 0.4, lambda a, x=x, y=y, nome=nome: E.escreve(c, nome, x + 90, y + 14, 40, "b", CLARO, a))
                if j == 1:
                    E.foco(c, t, C[k] + 0.6, 0.4, lambda a, y=y: E.escreve(c, "→", 1275, y + 18, 54, "g", CLARO, a))
        E.frase(c, t, C["s14.e"], ps("mais massa,", "i", 60, CLARO) + [("vida mais curta", "g", 62, E.COR)], XE, 1000, passo=0.1)
        return
    E.frase(c, t, C["s15.a"], ps("gravidade na superfície:", "i", 66, CLARO) + [("proporção", "g", 66, BR)], W / 2, 300, "center", 0.12)
    E.frase(c, t, C["s15.b"], [("raio ÷ 10", "g", 84, BR), ("→", "g", 84, CLARO), ("gravidade × 100", "g", 84, E.COR)], W / 2, 500, "center", 0.12)
    E.frase(c, t, C["s15.c"], ps("a gravidade vai com", "i", 64, CLARO), W / 2 - 160, 720, "right", 0.1)
    E.formula_em(c, t, C["s15.c"] + 0.6, "f{M}{R^2}", W / 2 - 100, 720, 110, "g", E.COR, "left")
    E.frase(c, t, C["s15.d"], [("massa mudou?", "g", 56, ERRADO)] + ps("faça as duas proporções", "i", 60, CLARO), W / 2, 950, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s16.a"], ps("como termina uma estrela", "i", 66) + [("com a massa do Sol?", "g", 62, COR)], XE, 350, passo=0.1)
    E.frase(c, t, C["s16.b"], ps("raio", "i", 66) + [("100 vezes menor,", "g", 66)] + ps("mesma massa:", "i", 66), XE, 520, passo=0.1)
    E.frase(c, t, C["s16.c"], [("gravidade", "g", 66, COR)] + ps("quantas vezes maior?", "i", 66), XE, 640, passo=0.1)
    if t < C["s17"]:
        ceu(c, 1200, 760, 600, 260, ep(t, C["s16.a"], 0.4), seed=8, n=30)
        E.foco(c, t, C["s16.a"] + 0.3, 0.5, lambda a: estrela(c, 1500, 890, 70, AMBAR, a))
    else:
        E.relogio(c, t, C["s17.a"], cx=1550, cy=730, r=150)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s18():
        E.frase(c, t, C["s18.a"], ps("massa do Sol:", "i", 66) + [("pouca massa", "g", 66, COR)], XE, 240, passo=0.12)
        fases = ((C["s18.a"] + 0.5, "Sol", AMBAR, 70), (C["s18.b"], "gigante vermelha", GIGANTE, 120), (C["s18.c"], "anã branca", ANA, 40))
        for i, (ti, nome, cor, r) in enumerate(fases):
            x = 300 + 560 * i
            E.foco(c, t, ti, 0.5, lambda a, x=x, cor=cor, r=r: estrela(c, x, 560, r, cor, a))
            E.foco(c, t, ti + 0.2, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 760, 50, "g", TINTA, a))
            if i:
                E.foco(c, t, ti - 0.2, 0.4, lambda a, x=x: centro(c, "→", x - 280, 580, 70, "g", TINTA2, a))
        E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "nada de buraco negro", W / 2, 900, 56, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s19"] - 0.1, s18)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19.a"], ps("cai com o", "i", 70) + [("quadrado da distância", "g", 70, COR)], XE, 240, passo=0.12)
    E.formula_em(c, t, C["s19.b"], "R ÷ 100", XE, 420, 100, "g", TINTA)
    E.formula_em(c, t, C["s19.c"], "100^2 = 10.000", XE, 600, 100, "g", TINTA)
    bola_txt(c, t, C["s19.d"], "10.000×", "", 1400, 480, 190, 66)
    E.frase(c, t, C["s19.e"], ps("é mais ou menos o que vira uma", "i", 58) + [("anã branca", "g", 58)], XE, 860, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s20", (("s20.a", [("equilíbrio:", "g", 64), ("gravidade", "i", 68), ("×", "g", 64, TINTA2), ("fusão", "i", 68, COR)]),
                                ("s20.b", [("a massa decide o fim", "g", 64, COR)]),
                                ("s20.c", [("massa curva o espaço;", "i", 66), ("buraco negro:", "g", 62), ("nem a luz sai", "i", 66)])), y0=380, dy=200)
    E.saida(c, t, C["s21"] - 0.1, tela_resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s21.a"], ps("de volta ao começo de tudo", "i", 62), XE, 360, passo=0.1)
    E.frase(c, t, C["s21.b"], [("Big Bang", "g", 120, COR)], XE, 520)
    E.foco(c, t, C["s21.b"] + 0.3, 0.6, lambda a: (ceu(c, 300, 620, 700, 360, a, seed=11),
                                                  estrela(c, 650, 800, 40 + 20 * math.sin(t * 2), AMBAR, a)))
    inscreva(c, t, C, "s21")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, nasce=b_nasce, fim_estrela=b_fim_estrela, buraco=b_buraco, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
