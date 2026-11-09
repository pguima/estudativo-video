"""Visual — Estudativo · FIS-MOD-010: praticando astronomia e cosmologia. Última aula da trilha.
Linguagem visual da trilha Física Moderna: veja o cabeçalho do visual.py da FIS-MOD-001 e, para o céu, o da FIS-MOD-008.
Prática no formato da FIS-MOD-007: número da questão na esfera, enunciado à esquerda, desenho à direita e relógio na pausa.
Todo instante vem de C[...]."""
import math
import random

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Física Moderna")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MOD-010_praticando_astronomia_cosmologia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "q1", "q2", "q3", "q4", "q5", "fim"))

# todas as contas da aula
assert 10 ** 2 == 100                                   # Q2: um décimo da distância → 100 vezes a força
assert 400 / 50 == 8 and 8 * 1000 == 8000               # Q4: 8.000 km/s
assert abs(1000 / 50 - 20) < 1e-12 and abs(70 / 3.26 - 21.5) < 0.1   # 20 km/s por milhão de anos-luz (real ≈ 21)


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


def buraco_negro(c, cx, cy, r, a=1.0, t=0.0):
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.2, [M.hexc(AMBAR, 0.0), M.hexc(AMBAR, 0.0), M.hexc(AMBAR, 0.55 * a), M.hexc(AMBAR, 0.0)], [0.0, 0.42, 0.55, 1.0]))
    c.drawCircle(cx, cy, r * 2.2, p)
    E.arco(c, cx, cy, r * 1.25, t * 40, 300, AMBAR, r * 0.18, a)
    c.drawCircle(cx, cy, r, M.paint("#000000", a))


def galaxia(c, cx, cy, r, cor="#E8D9FF", a=1.0, giro=-20):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(giro); c.scale(1, 0.4)
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(0, 0), r, [M.hexc(BR, 0.95 * a), M.hexc(cor, 0.6 * a), M.hexc(cor, 0.0)], [0.0, 0.35, 1.0]))
    c.drawCircle(0, 0, r, p)
    c.restore()


def numero_q(c, t, t0, n):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, XE + 50, 190, 50, a=a), centro(c, str(n), XE + 50, 214, 64, "g", BR, a)))
    E.frase(c, t, t0 + 0.1, ps("questão", "i", 72, COR), XE + 130, 214)


def pausa(c, t, t0, desenho):
    if t < t0:
        desenho()
    else:
        E.relogio(c, t, t0, cx=1500, cy=760, r=150)


def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], ps("questão de astronomia", "i", 76) + [("quase não tem conta", "g", 70, COR)], XE, 260, passo=0.1)
    E.frase(c, t, C["s01.b"], ps("cobra a", "i", 70) + [("ideia certa", "g", 70)] + ps("no lugar certo", "i", 70), XE, 400, passo=0.12)
    E.frase(c, t, C["s01.c"], ps("até o fim da aula:", "i", 66) + [("5 questões", "g", 70, COR)], XE, 580, passo=0.12)
    for i, s in enumerate(("estrelas", "buracos negros", "Big Bang", "expansão")):
        E.foco(c, t, C["s01.c"] + 1.2 + 0.35 * i, 0.4, lambda a, s=s, i=i: E.pilula(c, s, XE + 160 + 400 * (i % 2), 720 + 120 * (i // 2), 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s01.a"] + 0.3, 0.6, lambda a: (ceu(c, 1200, 600, 600, 380, a, seed=31, n=40), galaxia(c, 1380, 720, 100, a=a), buraco_negro(c, 1650, 860, 40, a, t)))


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 84), XE, 300, passo=0.14)
    for i, (k, l1, l2) in enumerate((("s02.a", "a vida das estrelas", "e os buracos negros"), ("s02.b", "o Big Bang", "e as provas dele"))):
        y = 400 + 260 * i
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, XE, y, 1000, 210, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "g", 64, COR)], XE + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "i", 60)], XE + 44, y + 170)
    E.foco(c, t, C["s02.a"] + 0.5, 0.5, lambda a: estrela(c, 1450, 500, 60, GIGANTE, a))
    E.foco(c, t, C["s02.b"] + 0.5, 0.5, lambda a: galaxia(c, 1450, 760, 120, "#B9A6E8", a))
    E.frase(c, t, lerp(C["s02.b"], C["s02.end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), XE, 980, "left", 0.12)


def b_metodo(c, t, C, b):
    def s03():
        E.frase(c, t, C["s03.a"], ps("ache a", "i", 72) + [("palavra-chave", "g", 70, COR)], XE, 220, passo=0.12)
        linhas = (("s03.b", "fim de estrela", "olhe a massa"), ("s03.c", "força da gravidade", "massas e distância"),
                  ("s03.d", "cor da galáxia", "vermelho vai, azul aproxima"), ("s03.e", "velocidade de afastamento", "proporcional à distância"))
        for i, (k, pal, regra) in enumerate(linhas):
            y = 380 + 160 * i
            E.foco(c, t, C[k], 0.5, lambda a, pal=pal, y=y: E.pilula(c, pal, XE + 330, y - 20, 48, "g", fundo=TINTA, a=a))
            E.foco(c, t, C[k] + 0.4, 0.5, lambda a, y=y: E.escreve(c, "→", XE + 700, y, 64, "g", TINTA2, a))
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, regra=regra, y=y: E.escreve(c, regra, XE + 790, y, 60, "g", COR, a))
    E.saida(c, t, C["s04"] - 0.1, s03)
    if t < C["s04"]:
        return
    E.frase(c, t, C["s04.a"], ps("duas", "i", 80) + [("pegadinhas", "g", 80, ERRADO)], XE, 220, passo=0.12)
    for i, (k, s1, s2) in enumerate((("s04.b", "o Sol não vira buraco negro", "pouca massa"), ("s04.c", "o Big Bang não explodiu num ponto", "o espaço inteiro se estica; não há centro"))):
        y = 360 + 300 * i
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, XE, y, 1580, 240, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s1, "g", 64)], XE + 50, y + 100)
        E.frase(c, t, C[k] + 1.2 if i == 0 else C["s04.d"], [(s2, "i", 60, COR)], XE + 50, y + 190)
    E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.selo(c, 1660, 440, 50, False, a))
    E.foco(c, t, C["s04.e"], 0.4, lambda a: E.selo(c, 1660, 740, 50, False, a))


# ---------------- questão 1 ----------------
def b_q1(c, t, C, b):
    if t < C["s06"]:
        numero_q(c, t, C["s05"], 1)
        E.frase(c, t, C["s05.a"], ps("fim de uma estrela com", "i", 64) + [("a massa do Sol?", "g", 64, COR)], XE, 360, passo=0.1)
        E.frase(c, t, C["s05.b"], ps("e com", "i", 64) + [("30 massas solares?", "g", 64, COR)], XE, 490, passo=0.1)
        E.frase(c, t, C["s05.c"], ps("qual", "i", 64) + [("vive mais?", "g", 64, COR)], XE, 620, passo=0.1)
        pausa(c, t, C["s05.d"], lambda: (estrela(c, 1300, 520, 50, AMBAR, ep(t, C["s05.a"], 0.4)), estrela(c, 1620, 520, 130, NEUTRON, ep(t, C["s05.b"], 0.4))))
        return
    for i, (ti, nome, cor, r) in enumerate(((C["s06.a"], "Sol", AMBAR, 50), (C["s06.b"], "gigante vermelha", GIGANTE, 90), (C["s06.c"], "anã branca", ANA, 30))):
        x = 300 + 420 * i
        E.foco(c, t, ti, 0.5, lambda a, x=x, cor=cor, r=r: estrela(c, x, 300, r, cor, a))
        E.foco(c, t, ti + 0.2, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 440, 46, "g", TINTA, a))
    for i, (ti, nome, cor, r) in enumerate(((C["s06.d"], "30 massas solares", NEUTRON, 90), (C["s06.e"], "supernova", AMBAR, 70), (C["s06.f"], "buraco negro", None, 50))):
        x = 300 + 420 * i
        if cor:
            E.foco(c, t, ti, 0.5, lambda a, x=x, cor=cor, r=r: estrela(c, x, 640, r, cor, a))
        else:
            E.foco(c, t, ti, 0.5, lambda a, x=x, r=r: buraco_negro(c, x, 640, r, a, t))
        E.foco(c, t, ti + 0.2, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 790, 46, "g", TINTA, a))
    E.frase(c, t, C["s06.g"], ps("vive mais:", "i", 62) + [("a pequena", "g", 62, CERTO)], 1340, 400, passo=0.1)
    E.frase(c, t, C["s06.h"], ps("a grande queima", "i", 56) + [("muito mais depressa", "g", 54, COR)], XE, 950, passo=0.08)


# ---------------- questão 2 ----------------
def b_q2(c, t, C, b):
    if t < C["s08"]:
        numero_q(c, t, C["s07"], 2)
        E.frase(c, t, C["s07.a"], ps("o Sol vira", "i", 62) + [("buraco negro", "g", 62)] + ps("de mesma massa", "i", 62), XE, 360, passo=0.1)
        E.frase(c, t, C["s07.b"], ps("a força na Terra:", "i", 62) + [("aumenta, diminui ou fica igual?", "g", 56, COR)], XE, 490, passo=0.1)
        E.frase(c, t, C["s07.c"], ps("e a", "i", 62) + [("1/10 da distância?", "g", 62, COR)], XE, 620, passo=0.1)
        pausa(c, t, C["s07.d"], lambda: (estrela(c, 1500, 500, 80, AMBAR, ep(t, C["s07.a"], 0.4) * (1 - ep(t, C["s07.a"] + 1.0, 0.6))),
                                         buraco_negro(c, 1500, 500, 50, ep(t, C["s07.a"] + 1.0, 0.6), t)))
        return
    E.formula_em(c, t, C["s08.a"], "F = f{G · M · m}{d^2}", XE, 260, 100, "g", TINTA)
    E.frase(c, t, C["s08.b"], ps("mesmas massas, mesma distância:", "i", 60), XE, 430, passo=0.08)
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.pilula(c, "a força fica igual", XE + 260, 530, 54, "g", fundo=CERTO, a=a))
    cx, cy = 1350, 420
    E.foco(c, t, C["s08.d"], 0.5, lambda a: buraco_negro(c, cx, cy, 36, a, t))
    if t >= C["s08.d"]:
        pt = M.paint(TINTA2, ep(t, C["s08.d"], 0.4) * 0.6, stroke=3)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawOval(skia.Rect.MakeXYWH(cx - 360, cy - 130, 720, 260), pt)
        g = (t - C["s08.d"]) * 0.8
        E.bola(c, cx + 360 * math.cos(g), cy + 130 * math.sin(g), 24, "#2F7FD0", 1.0)
    E.frase(c, t, C["s08.e"], ps("sem luz e sem calor:", "i", 56) + [("não é aspirador", "g", 56)], XE, 660, passo=0.08)
    E.frase(c, t, C["s08.f"], [("1/10 da distância:", "g", 62, COR)], XE, 800)
    E.formula_em(c, t, C["s08.h"], "10^2 = 100", XE + 600, 800, 76, "g", TINTA)
    E.foco(c, t, C["s08.h"] + 0.6, 0.5, lambda a: E.pilula(c, "100 vezes mais força", XE + 300, 910, 54, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s08.i"], ps("igual com o Sol", "i", 54, TINTA2), XE + 720, 920, passo=0.08)


# ---------------- questão 3 ----------------
def b_q3(c, t, C, b):
    if t < C["s10"]:
        numero_q(c, t, C["s09"], 3)
        E.frase(c, t, C["s09.a"], [("Andrômeda:", "g", 64)] + ps("desvio para o", "i", 62) + [("azul", "g", 64, AZUL)], XE, 360, passo=0.1)
        E.frase(c, t, C["s09.b"], ps("se", "i", 64) + [("afasta", "g", 62)] + ps("ou se", "i", 64) + [("aproxima?", "g", 62)], XE, 490, passo=0.1)
        E.frase(c, t, C["s09.c"], ps("contradiz a", "i", 64) + [("expansão?", "g", 64, COR)], XE, 620, passo=0.1)

        def des():
            ceu(c, 1150, 300, 650, 420, ep(t, C["s09.a"], 0.4), seed=41, n=30)
            if t >= C["s09.a"]:
                galaxia(c, 1320, 500, 130, a=ep(t, C["s09.a"], 0.4))
                F.onda(c, t, C["s09.a"] + 0.3, 1450, 1760, 500, 30, 50, AZUL, 0.6, velocidade=-60, eixo=False)
        pausa(c, t, C["s09.d"], des)
        return
    E.frase(c, t, C["s10.a"], [("azul", "g", 80, AZUL), ("=", "g", 80, TINTA2), ("aproxima", "g", 80)], XE, 260, passo=0.12)
    E.frase(c, t, C["s10.b"], ps("Andrômeda vem na", "i", 62) + [("nossa direção", "g", 62)], XE, 380, passo=0.1)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.pilula(c, "não contradiz", XE + 200, 520, 54, "g", fundo=CERTO, a=a))
    E.frase(c, t, C["s10.c"] + 0.8, ps("é nossa vizinha", "i", 60), XE + 470, 540, passo=0.1)
    E.frase(c, t, C["s10.d"], ps("perto, a", "i", 60) + [("gravidade vence", "g", 60, COR)] + ps("a expansão", "i", 60), XE, 690, passo=0.1)
    E.frase(c, t, C["s10.e"], ps("as distantes, quase todas,", "i", 58) + [("se afastam", "g", 58, VERM)], XE, 830, passo=0.08)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: (ceu(c, 1250, 180, 560, 300, a, seed=42, n=25), galaxia(c, 1400, 320, 90, a=a), galaxia(c, 1640, 360, 60, "#B9A6E8", a)))
    if t >= C["s10.b"]:
        F.seta(c, 1460, 410, 1580, 410, BR, ep(t, C["s10.b"], 0.4), 6)


# ---------------- questão 4 ----------------
def b_q4(c, t, C, b):
    if t < C["s12"]:
        numero_q(c, t, C["s11"], 4)
        E.frase(c, t, C["s11.a"], [("50 milhões de anos-luz", "g", 60)] + ps("→", "g", 60, TINTA2) + [("1.000 km/s", "g", 60, VERM)], XE, 360, passo=0.1)
        E.frase(c, t, C["s11.b"], [("400 milhões", "g", 64, COR)] + ps("de anos-luz", "i", 62) + [("→ ?", "g", 70, COR)], XE, 500, passo=0.1)
        pausa(c, t, C["s11.c"], lambda: (ceu(c, 1150, 600, 650, 320, ep(t, C["s11.a"], 0.4), seed=43, n=25),
                                         galaxia(c, 1300, 760, 70, a=ep(t, C["s11.a"], 0.4)), galaxia(c, 1680, 760, 50, a=ep(t, C["s11.b"], 0.4))))
        return
    E.frase(c, t, C["s12.a"], ps("velocidade", "i", 70) + [("proporcional", "g", 70, COR)] + ps("à distância", "i", 70), XE, 240, passo=0.12)
    E.formula_em(c, t, C["s12.b"], "400 ÷ 50 = 8", XE, 420, 100, "g", TINTA)
    E.frase(c, t, C["s12.c"], [("8×", "g", 90, COR)] + ps("a distância", "i", 70), XE, 600, passo=0.12)
    E.frase(c, t, C["s12.d"], [("8×", "g", 90, COR)] + ps("a velocidade", "i", 70), XE, 740, passo=0.12)
    bola_txt(c, t, C["s12.e"], "8.000", "km/s", 1450, 560, 190, 60)


# ---------------- questão 5 ----------------
def b_q5(c, t, C, b):
    if t < C["s14"]:
        numero_q(c, t, C["s13"], 5)
        E.frase(c, t, C["s13.a"], [("radiação cósmica de fundo:", "g", 58)] + ps("saiu como luz quente", "i", 58), XE, 360, passo=0.1)
        E.frase(c, t, C["s13.b"], ps("por que chega como", "i", 64) + [("micro-ondas?", "g", 64, COR)], XE, 500, passo=0.1)
        E.frase(c, t, C["s13.c"], ps("por que é", "i", 64) + [("prova do Big Bang?", "g", 64, COR)], XE, 630, passo=0.1)
        pausa(c, t, C["s13.d"], lambda: F.onda(c, t, C["s13.a"], 1150, 1780, 800, 40, 60, AMBAR, 0.8, velocidade=-60, eixo=False) if t >= C["s13.a"] else None)
        return
    lam = lerp(60, 260, ep(t, C["s14.a"], 2.0))
    F.onda(c, t, C["s14"], 260, 1700, 300, 60, lam, E.mix(AMBAR, "#8C96A3", ep(t, C["s14.a"], 2.0)), 0.8, velocidade=-80, eixo=False)
    E.frase(c, t, C["s14.a"], ps("o espaço se esticou,", "i", 62) + [("e as ondas junto", "g", 62)], XE, 520, passo=0.1)
    E.frase(c, t, C["s14.c"], [("λ muito maior:", "g", 64), ("micro-ondas", "g", 64, COR)], XE, 640, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("um começo quente", "i", 60) + [("tinha que deixar essa luz", "g", 58)], XE, 790, passo=0.08)
    E.frase(c, t, C["s14.e"], ps("igual de", "i", 60) + [("todas as direções", "g", 60, COR)] + ps("· achada em 1965", "i", 60, TINTA2), XE, 910, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def tela_resumo():
        resumo(c, t, C, "s15", (("s15.a", [("a massa", "g", 66, COR), ("decide o fim da estrela", "i", 68)]),
                                ("s15.b", [("gravidade:", "g", 64), ("só massa e distância", "i", 68)]),
                                ("s15.c", [("vermelho", "g", 64, VERM), ("e", "i", 68), ("radiação de fundo:", "g", 64, COR), ("o Big Bang", "i", 68)])), y0=380, dy=190)
    E.saida(c, t, C["s15.d"] - 0.1, tela_resumo)
    if t < C["s15.d"]:
        return
    E.frase(c, t, C["s15.d"], ps("você fechou a", "i", 84), XE, 300, passo=0.12)
    E.frase(c, t, C["s15.d"] + 0.6, [("Física Moderna", "g", 120, COR)], XE, 470)
    E.foco(c, t, C["s15.d"] + 0.8, 0.8, lambda a: E.simbolo(c, 600, 780, 180 * ease_back(prog(t, C["s15.d"] + 0.8, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.foco(c, t, C["s15.e"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s15.e"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s15.e"] + 0.2, 0.4))
    E.frase(c, t, C["s15.f"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, q1=b_q1, q2=b_q2, q3=b_q3, q4=b_q4, q5=b_q5, fim=b_fim)
