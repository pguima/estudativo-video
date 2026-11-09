"""Visual — Estudativo · FIS-MOD-005: relatividade restrita.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001. Na relatividade: a nave e quem
viaja nela em petróleo (F.VEL); quem vê de fora em tinta; γ sempre em laranja; tempo de fora = cronômetro em tinta, tempo
próprio = cronômetro petróleo. O relógio de luz é o pulso laranja entre dois espelhos. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-005_relatividade_restrita.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("postulados", "tempo", "comprimento", "erro", "atalho", "questao", "fim"))


def gama(b):
    return 1 / math.sqrt(1 - b * b)


# todas as contas da aula
assert abs(0.6 ** 2 - 0.36) < 1e-12 and abs(1 - 0.36 - 0.64) < 1e-12 and abs(math.sqrt(0.64) - 0.8) < 1e-12
assert abs(gama(0.6) - 1.25) < 1e-12 and abs(8 * 1.25 - 10) < 1e-12        # gêmeos: 8 anos → 10 anos
assert abs(100 / 1.25 - 80) < 1e-12                                          # nave de 100 m → 80 m
assert abs(8 / 1.25 - 6.4) < 1e-12                                           # o erro: 6,4 anos
assert abs(0.6 ** 2 + 0.8 ** 2 - 1) < 1e-12 and abs(gama(0.8) - 5 / 3) < 1e-12
assert abs(30 * 3 / 5 - 18) < 1e-12 and abs(50 * 3 / 5 - 30) < 1e-12         # questão: 18 anos e 30 m
assert gama(250 / 3e8) - 1 < 1e-12                                           # avião: γ praticamente 1
assert 0.5 + 1 == 1.5                                                        # "não uma vez e meia cê"


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
def nave(c, x, y, L, a=1.0, cor=None, k=1.0):
    """nave de lado, apontando para a direita; (x, y) = traseira no meio; L = comprimento; k encolhe na horizontal"""
    if a <= 0:
        return
    cor = cor or F.VEL
    L = L * k
    h = 0.28 * L / k if k else 0.28 * L
    h = min(h, 120)
    p = skia.Path()
    p.moveTo(x, y - h / 2); p.lineTo(x + L * 0.75, y - h / 2); p.quadTo(x + L, y, x + L * 0.75, y + h / 2); p.lineTo(x, y + h / 2); p.close()
    c.drawPath(p, M.paint(cor, a))
    for d in (-1, 1):
        q = skia.Path()
        q.moveTo(x + L * 0.05, y + d * h / 2); q.lineTo(x - L * 0.08, y + d * h * 0.95); q.lineTo(x + L * 0.25, y + d * h / 2); q.close()
        c.drawPath(q, M.paint(E.mix(cor, "#000000", 0.25), a))
    c.drawCircle(x + L * 0.62, y, h * 0.18, M.paint("#DDF4F6", a))


def pessoa(c, cx, yb, s, cor=TINTA, a=1.0):
    """bonequinho: cabeça e corpo, com os pés em yb"""
    if a <= 0:
        return
    c.drawCircle(cx, yb - s * 0.82, s * 0.16, M.paint(cor, a))
    M.rrect(c, cx - s * 0.17, yb - s * 0.62, s * 0.34, s * 0.62, s * 0.12, cor, a)


def relogio_luz(c, t, t0, cx, yb, alto, a=1.0, desloca=0.0, periodo=1.6, rastro=False):
    """dois espelhos e um pulso que sobe e desce; desloca = quanto o relógio anda por período (visto de fora)"""
    if a <= 0 or t < t0:
        return
    s = ((t - t0) / periodo) % 3 if desloca else (t - t0) / periodo
    x = cx + desloca * s
    for yy in (yb, yb - alto):
        M.rrect(c, x - 60, yy - 6, 120, 12, 4, TINTA, a)
    u = s % 1
    yp = yb - 12 - (alto - 24) * (1 - abs(1 - 2 * u))
    if rastro and desloca:
        n = int(s * 2) + 1
        pts = []
        for i in range(n + 1):
            xi = cx + desloca * min(s, i / 2)
            yi = yb - 12 if i % 2 == 0 else yb - alto + 12
            if i / 2 > s:
                xi, yi = x, yp
            pts.append((xi, yi))
        pts[-1] = (x, yp)
        F.poli(c, pts, 1.0, E.COR, a * 0.6, 4, E.TRACO)
    c.drawCircle(x, yp, 14, M.paint(E.COR, a))


def b_gancho(c, t, C, b):
    def um():
        E.frase(c, t, C["s01.a"], ps("uma astronauta numa", "i", 70) + [("nave muito rápida", "g", 66, F.VEL)], XE, 220, passo=0.12)
        if t >= C["s01.a"]:
            u = ease_io(prog(t, C["s01.a"] + 0.3, 2.4))
            nave(c, lerp(-300, 1500, u), 400, 300, ep(t, C["s01.a"], 0.3))
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (pessoa(c, 600, 880, 230, F.VEL, a), F.medida(c, "+8", "anos", 690, 760, 90, F.VEL, a)))
        E.foco(c, t, C["s01.c"], 0.5, lambda a: (pessoa(c, 1200, 880, 230, TINTA, a), E.escreve(c, "na Terra", 1110, 940, 46, "i", TINTA2, a)))
        E.foco(c, t, C["s01.d"], 0.5, lambda a: F.medida(c, "+10", "anos", 1290, 760, 90, COR, a))
        E.foco(c, t, C["s01.e"], 0.5, lambda a: E.pilula(c, "conta da relatividade", 1500, 560, 52, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s01.b"] + 0.2, 0.4, lambda a: E.escreve(c, "astronauta", 490, 940, 46, "i", TINTA2, a))
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        promessa(c, t, C, "s02", (("s02.a", "o tempo que dilata"), ("s02.b", "o comprimento que contrai")))


def b_lembrete(c, t, C, b):
    def f1(a, x, y):
        E.formula(c, "c = 3 × 10^8 m/s", x - 40, y + 20, 48, "g", TINTA, a, "center")

    def f2(a, x, y):
        E.formula(c, "r{0,64} = 0,8", x - 20, y + 20, 60, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "a velocidade da luz:", "a velocidade c"), ("s03.c", "a raiz quadrada:", "0,8 × 0,8 = 0,64")), (f1, f2))


# ---------------- as duas ideias ----------------
def aviao(c, x, y, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x, y - s * 0.12, s, s * 0.24, s * 0.12, "#C9CED4", a)
    for i in range(5):
        c.drawCircle(x + s * (0.3 + 0.12 * i), y - s * 0.03, s * 0.03, M.paint("#3B6E8F", a))


def b_postulados(c, t, C, b):
    def s04():
        E.frase(c, t, C["s04"] + 0.2, [("1905", "g", 130, TINTA), ("Einstein", "g", 90, COR)], XE, 260, passo=0.3)
        E.frase(c, t, C["s04.a"], ps("duas ideias", "i", 76), XE, 380)
        E.foco(c, t, C["s04.b"], 0.5, lambda a: (E.bola(c, XE + 40, 500, 38, a=a), centro(c, "1", XE + 40, 522, 48, "g", BR, a)))
        E.frase(c, t, C["s04.b"] + 0.1, ps("as leis da Física são", "i", 62) + [("as mesmas", "g", 62, COR)], XE + 110, 525, passo=0.1)
        E.frase(c, t, C["s04.b"] + 1.4, ps("parado ou em linha reta com velocidade constante", "i", 50, TINTA2), XE + 110, 610, passo=0.06)
        E.foco(c, t, C["s04.c"], 0.6, lambda a: aviao(c, 700, 820, 700, a))
        if t >= C["s04.c"] + 0.6:  # o copo cai reto dentro do avião
            u = ((t - C["s04.c"] - 0.6) / 1.2) % 1
            M.rrect(c, 1080 - 14, 790 + 60 * u * u - 20, 28, 40, 6, E.COR, 1.0)
        E.foco(c, t, C["s04.c"] + 0.8, 0.4, lambda a: E.escreve(c, "o copo cai igual ao de casa", 700, 1000, 50, "i", TINTA2, a))
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    E.foco(c, t, C["s05.a"], 0.5, lambda a: (E.bola(c, XE + 40, 220, 38, a=a), centro(c, "2", XE + 40, 242, 48, "g", BR, a)))
    E.frase(c, t, C["s05.a"] + 0.1, ps("a luz tem a", "i", 62) + [("mesma velocidade", "g", 62, COR)] + ps("para todos", "i", 62), XE + 110, 245, passo=0.1)
    E.foco(c, t, C["s05.b"], 0.5, lambda a: (nave(c, 300, 520, 360, a), F.medida(c, "0,5c", "", 420, 430, 60, F.VEL, a)))
    if t >= C["s05.b"] + 0.6:
        F.seta(c, 680, 520, 1500, 520, LUZ, 1.0, 8, None, ease_io(prog(t, C["s05.b"] + 0.6, 0.8)))
    E.foco(c, t, C["s05.c"], 0.5, lambda a: (pessoa(c, 440, 740, 130, F.VEL, a), E.escreve(c, "mede c", 520, 720, 54, "g", F.VEL, a)))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: (pessoa(c, 1300, 740, 130, TINTA, a), E.escreve(c, "mede c", 1380, 720, 54, "g", TINTA, a)))
    E.foco(c, t, C["s05.e"], 0.5, lambda a: (E.escreve(c, "1,5c", 1380, 820, 54, "g", ERRADO, a)))
    if t >= C["s05.e"] + 0.5:
        E.risco(c, 1370, 830, 1520, 780, t, C["s05.e"] + 0.5, largura=8)
    E.frase(c, t, C["s05.f"], ps("quem muda é", "i", 76) + [("o tempo", "g", 84, COR)], W / 2, 980, "center", 0.12)


# ---------------- dilatação do tempo ----------------
def b_tempo(c, t, C, b):
    def s06():
        E.frase(c, t, C["s06"], ps("relógio de luz", "i", 76), XE, 200)
        E.frase(c, t, C["s06.a"], ps("um pulso sobe e desce", "i", 56, TINTA2), XE, 290, passo=0.1)
        E.foco(c, t, C["s06.a"], 0.5, lambda a: relogio_luz(c, t, C["s06.a"], 420, 800, 360, a))
        E.foco(c, t, C["s06.b"], 0.4, lambda a: E.pilula(c, "na nave: reto", 420, 900, 46, "g", fundo=F.VEL, a=a))
        if t >= C["s06.c"]:
            relogio_luz(c, t, C["s06.c"], 900, 800, 360, ep(t, C["s06.c"], 0.4), desloca=260, periodo=2.2, rastro=True)
            E.foco(c, t, C["s06.c"] + 0.3, 0.4, lambda a: E.pilula(c, "de fora: inclinado, mais longo", 1300, 900, 46, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s06.d"], ps("mesma velocidade, caminho", "i", 56) + [("maior", "g", 56, COR)], 760, 200, passo=0.08)
        E.frase(c, t, C["s06.e"], ps("de fora, cada tique", "i", 56) + [("demora mais", "g", 56, COR)], 760, 290, passo=0.08)
    E.saida(c, t, C["s07"] - 0.1, s06)
    if C["s07"] <= t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], [("dilatação", "g", 84, COR), ("do tempo", "g", 84)], XE, 200, passo=0.15)
            E.formula_em(c, t, C["s07.b"], "Δt = γ · Δt₀", XE, 360, 120, "g", TINTA)
            E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.escreve(c, "Δt: o tempo de fora", 1000, 320, 52, "b", TINTA, a))
            E.foco(c, t, C["s07.c"], 0.4, lambda a: E.escreve(c, "Δt₀: tempo próprio, o da nave", 1000, 400, 52, "b", F.VEL, a))
            E.frase(c, t, C["s07.d"], [("γ", "g", 90, COR)] + ps("fator de Lorentz", "i", 66), XE, 600, passo=0.12)
            E.formula_em(c, t, C["s07.e"], "γ = f{1}{r{1 − f{v^2}{c^2}}}", XE, 830, 110, "g", COR)
            E.foco(c, t, C["s07.e"] + 1.6, 0.4, lambda a: E.escreve(c, "v: a velocidade da nave", 900, 830, 52, "i", TINTA2, a))
        E.saida(c, t, C["s08"] - 0.1, s07)
    if C["s08"] <= t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], [("v =", "g", 80), ("0,6c", "g", 80, F.VEL)], XE, 200, passo=0.15)
            linhas = [(C["s08.b"], "f{v}{c} = 0,6  →  0,6^2 = 0,36"), (C["s08.c"], "1 − 0,36 = 0,64"), (C["s08.d"], "r{0,64} = 0,8")]
            for i, (ti, s) in enumerate(linhas):
                E.formula_em(c, t, ti, s, XE, 360 + 150 * i, 84, "g", TINTA2 if i < 2 else TINTA)
            E.formula_em(c, t, C["s08.e"], "γ = f{1}{0,8}", XE, 860, 100, "g", COR)
            bola_txt(c, t, C["s08.e"] + 0.8, "1,25", "", 1400, 600, 170, 100)
            E.foco(c, t, C["s08.e"] + 1.1, 0.4, lambda a: centro(c, "γ", 1400, 420, 80, "g", COR, a))
        E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.foco(c, t, C["s09.a"], 0.5, lambda a: (F.cronometro(c, 380, 330, 110, 8, a, "8 anos", cor=F.VEL), E.escreve(c, "nave", 320, 170, 50, "i", F.VEL, a)))
    E.foco(c, t, C["s09.a"] + 0.5, 0.4, lambda a: E.escreve(c, "× 1,25 =", 560, 350, 70, "g", COR, a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: (F.cronometro(c, 1000, 330, 110, 10, a, "10 anos"), E.escreve(c, "Terra", 940, 170, 50, "i", TINTA, a)))
    E.frase(c, t, C["s09.c"], ps("a prova:", "i", 66) + [("o múon", "g", 66, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s09.c"] + 1.0, ps("nasce no alto da atmosfera e vive pouquíssimo", "i", 52, TINTA2), XE, 730, passo=0.06)
    E.frase(c, t, C["s09.d"], ps("chega ao chão: para nós, o tempo dele", "i", 56) + [("passa devagar", "g", 56, COR)], XE, 860, passo=0.08)
    if t >= C["s09.c"]:
        u = ((t - C["s09.c"]) / 2.2) % 1
        M.line(c, 1500, 560, 1500, 1000, TINTA2, 0.5, 4, dash=E.TRACO)
        E.bola(c, 1500, lerp(560, 990, u), 18, E.COR, 1.0)
        F.chao(c, 1380, 1620, 1010, ep(t, C["s09.c"], 0.4))


# ---------------- contração ----------------
def b_comprimento(c, t, C, b):
    def s10():
        E.frase(c, t, C["s10.a"], ps("o comprimento", "i", 76) + [("também muda", "g", 76, COR)], XE, 200, passo=0.12)
        k = 1 - 0.2 * ep(t, C["s10.b"] + 0.4, 0.8)
        E.foco(c, t, C["s10.a"] + 0.5, 0.5, lambda a: nave(c, 900, 420, 600, a, k=k))
        E.frase(c, t, C["s10.b"], ps("quem vê passar mede", "i", 56) + [("mais curta", "g", 56, COR)], XE, 330, passo=0.1)
        E.formula_em(c, t, C["s10.c"], "L = f{L₀}{γ}", XE, 680, 110, "g", TINTA)
        E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "L₀: medido parado junto da nave", XE + 420, 660, 50, "b", F.VEL, a))
        E.formula_em(c, t, C["s10.e"], "L₀ = 100 m,  v = 0,6c", XE, 860, 70, "g", TINTA2)
        bola_txt(c, t, C["s10.f"], "80", "m", 1500, 860, 110, 80)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    P = E.plano(c, t, C["s11"], 900, 260, 820, 560, 0, 1, 0, 6, passo=0.2, passo_y=1, marcas_x=[0, 0.6, 0.8, 1], marcas_y=[1, 2, 3, 4, 5],
                nomes=("v", ""), fmt=lambda v: {0.0: "0", 0.6: "0,6c", 0.8: "0,8c", 1.0: "c"}.get(round(v, 2), str(int(round(v)))))
    E.curva(c, t, C["s11.a"], P, lambda x: gama(x) if x < 0.985 else None, 0, 0.984, 1.4)
    E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: E.escreve(c, "γ", 860, 250, 64, "g", COR, a))
    E.frase(c, t, C["s11.a"], [("γ", "g", 80, COR)] + ps("sempre maior que 1", "i", 64), XE, 300, passo=0.12)
    E.frase(c, t, C["s11.a"] + 1.2, ps("e cresce sem limite perto de c", "i", 56, TINTA2), XE, 390, passo=0.08)
    E.frase(c, t, C["s11.b"], ps("nada com massa", "i", 60) + [("chega a c", "g", 60, COR)], XE, 540, passo=0.1)
    E.frase(c, t, C["s11.c"], [("avião:", "g", 60), ("γ", "g", 64, COR)] + ps("praticamente 1", "i", 60), XE, 700, passo=0.1)
    E.frase(c, t, C["s11.d"], ps("não aparece no dia a dia", "i", 56, TINTA2), XE, 800, passo=0.08)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s12.a"], ps("dividir em vez de multiplicar", "i", 70), XE + 480, 200, passo=0.1)
    E.formula_em(c, t, C["s12.b"], "8 ÷ 1,25 = 6,4 anos na Terra ?", W / 2, 380, 84, "g", ERRADO, "center")
    if t >= C["s12.c"]:
        E.risco(c, W / 2 - 600, 400, W / 2 + 600, 320, t, C["s12.c"], largura=12)
    E.frase(c, t, C["s12.c"], ps("de fora, o tempo tem que ser o", "i", 62) + [("maior", "g", 62, COR)], W / 2, 520, "center", 0.1)
    E.frase(c, t, C["s12.d"], ps("a regra:", "i", 70, COR), XE, 680)
    E.frase(c, t, C["s12.e"], [("de fora:", "g", 66), ("tempo", "i", 70), ("maior,", "g", 66, COR), ("comprimento", "i", 70), ("menor", "g", 66, COR)], XE, 790, passo=0.12)
    E.frase(c, t, C["s12.f"], [("γ", "g", 76, COR)] + ps("multiplica o tempo e divide o comprimento", "i", 62), XE, 920, passo=0.08)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("agora, o atalho", "i", 70, CLARO), XE, 160)
    if t < C["s14"]:
        E.frase(c, t, C["s13.a"], ps("quase sempre:", "i", 60, CLARO) + [("0,6c", "g", 70, BR)] + ps("ou", "i", 60, CLARO) + [("0,8c", "g", 70, BR)], XE, 290, passo=0.12)
        # triângulo 3-4-5 (0,6 · 0,8 · 1)
        A, B, Cc = (1100, 860), (1700, 860), (1100, 410)
        q = ep(t, C["s13.b"], 0.6)
        if q > 0:
            F.poli(c, [A, B, Cc, A], ease_io(q), BR, 1.0, 6)
            E.foco(c, t, C["s13.b"] + 0.5, 0.4, lambda a: (E.escreve(c, "0,8", 1360, 930, 60, "g", E.COR, a), E.escreve(c, "0,6", 980, 650, 60, "g", E.COR, a),
                                                          E.escreve(c, "1", 1440, 610, 60, "g", BR, a)))
        E.frase(c, t, C["s13.b"], ps("o triângulo", "i", 60, CLARO) + [("3, 4, 5", "g", 66, BR)], XE, 420, passo=0.12)
        E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "0,6^2 + 0,8^2 = 1", XE, 580, 76, "g", BR, a))
        E.frase(c, t, C["s13.d"], ps("a raiz é sempre", "i", 60, CLARO) + [("o outro número", "g", 60, E.COR)], XE, 740, passo=0.1)
        return
    for i, (v, r, g, gd, k) in enumerate((("0,6c", "0,8", "f{5}{4}", "1,25", "s14.a"), ("0,8c", "0,6", "f{5}{3}", "", "s14.b"))):
        y = 400 + 260 * i
        E.foco(c, t, C[k], 0.5, lambda a, v=v, y=y: E.escreve(c, "v = " + v, XE, y, 80, "g", BR, a))
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, r=r, y=y: (E.escreve(c, "→", 700, y, 60, "g", CLARO, a), E.escreve(c, "raiz", 780, y, 60, "i", CLARO, a), E.escreve(c, r, 920, y, 80, "g", BR, a)))
        E.foco(c, t, C[k] + 1.2, 0.5, lambda a, g=g, gd=gd, y=y: (E.formula(c, "→ γ = " + g, 1120, y, 84, "g", E.COR, a),
                                                                  E.escreve(c, ("= " + gd) if gd else "", 1520, y, 70, "g", E.COR, a)))
    E.frase(c, t, C["s14.c"], [("outra", "g", 56, ERRADO)] + ps("velocidade? faça a conta da raiz", "i", 58, CLARO), W / 2, 960, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s15.a"], [("nave de", "i", 70)], XE, 340)
    E.foco(c, t, C["s15.a"] + 0.4, 0.5, lambda a: (F.medida(c, "50", "m", XE + 260, 340, 80, F.VEL, a), E.escreve(c, "a", XE + 480, 340, 70, "i", TINTA, a),
                                                  E.escreve(c, "0,8c", XE + 540, 340, 80, "g", F.VEL, a)))
    E.frase(c, t, C["s15.b"], ps("na Terra:", "i", 70) + [("30 anos", "g", 70)], XE, 480, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("tempo", "i", 70) + [("na nave?", "g", 70, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("comprimento para quem", "i", 66) + [("vê passar?", "g", 66, COR)], XE, 780, passo=0.12)
    if t < C["s16"]:
        if t >= C["s15.a"]:
            u = ((t - C["s15.a"]) / 3.0) % 1
            nave(c, lerp(1050, 1800, u), 420, 260, ep(t, C["s15.a"], 0.4))
    else:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    def s17():
        E.foco(c, t, C["s17.a"], 0.5, lambda a: (E.escreve(c, "0,8c →", XE, 230, 80, "g", TINTA, a), E.formula(c, "γ = f{5}{3}", XE + 330, 230, 90, "g", COR, a)))
        E.formula_em(c, t, C["s17.b"], "Δt = γ · Δt₀", XE, 420, 90, "g", TINTA2)
        E.formula_em(c, t, C["s17.c"], "30 = f{5}{3} · Δt₀", XE, 580, 90, "g", TINTA)
        E.formula_em(c, t, C["s17.d"], "Δt₀ = 30 · f{3}{5}", XE, 760, 90, "g", TINTA)
        bola_txt(c, t, C["s17.e"], "18", "anos", 1400, 560, 170, 96)
    E.saida(c, t, C["s18"] - 0.1, s17)
    if t < C["s18"]:
        return
    E.formula_em(c, t, C["s18.a"], "L = f{50}{f{5}{3}}", XE, 280, 100, "g", TINTA)
    E.formula_em(c, t, C["s18.b"], "= 50 · f{3}{5}", XE + 430, 280, 100, "g", TINTA2)
    bola_txt(c, t, C["s18.c"], "30", "m", 1500, 280, 130, 90)
    E.frase(c, t, C["s18.d"], ps("confira a regra:", "i", 66, COR), XE, 520)
    E.frase(c, t, C["s18.d"] + 0.8, [("tempo de fora", "i", 64), ("maior:", "g", 64), ("30", "g", 64, COR), ("contra", "i", 64), ("18", "g", 64, F.VEL)], XE, 650, passo=0.12)
    E.frase(c, t, C["s18.d"] + 2.0, [("comprimento de fora", "i", 64), ("menor:", "g", 64), ("30", "g", 64, COR), ("contra", "i", 64), ("50", "g", 64, F.VEL)], XE, 780, passo=0.12)
    E.foco(c, t, C["s18.d"] + 3.2, 0.4, lambda a: E.selo(c, 1600, 720, 70, True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s19", (("s19.a", [("luz:", "g", 64), ("mesma velocidade", "i", 68), ("para todos", "i", 68)]),
                                ("s19.b", [("de fora:", "g", 64), ("tempo", "i", 68), ("× γ", "g", 64, COR)]),
                                ("s19.c", [("comprimento", "i", 68), ("÷ γ", "g", 64, COR)]),
                                ("s19.d", [("0,6", "g", 64), ("e", "i", 68), ("0,8:", "g", 64), ("triângulo 3, 4, 5", "i", 68)])), y0=350, dy=170)
    E.saida(c, t, C["s20"] - 0.1, tela_resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], ps("massa e energia:", "i", 80), XE, 400, passo=0.12)
    E.foco(c, t, C["s20.b"], 0.6, lambda a: E.formula(c, "E = m · c^2", XE, 620, 170, "g", COR, a))
    inscreva(c, t, C, "s20")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, postulados=b_postulados, tempo=b_tempo, comprimento=b_comprimento, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
