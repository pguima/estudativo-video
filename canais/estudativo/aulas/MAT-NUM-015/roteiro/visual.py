"""Visual — Estudativo · MAT-NUM-015: números negativos e reta numérica.
Identidade em _ferramentas/editorial.py. Peças locais: termometro, passos (saltos de um em um sobre a reta), ponto e camara."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco
import motor as M
import skia

E.usar("Matemática", "Números e Contas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-NUM-015_numeros_negativos_reta_numerica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("termometro", "comparar", "modulo", "atalho", "questao", "fim"))
BR = "#FFFFFF"
sn = lambda v: str(v).replace("-", "−")  # o menos da tela


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


def pal(s, estilo="i", size=84, cor=TINTA):
    """frase em palavras, para entrar uma a uma"""
    return [(p, estilo, size, cor) for p in s.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=CERTO):
    """o resultado na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r, cor, a), E.centro(c, s, cx, cy + size * 0.35, size, "g", M.on(cor), a)))


def ponto(c, t, t0, x, y, cor=None, r=24):
    """ponto marcado na reta"""
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        E.bola(c, x, y, r * k, cor)


def passos(c, t, t0, t1, de, ate, vx, y, cor=None, alto=64):
    """os passos sobre a reta, um a um, de t0 a t1 (peça local)"""
    n, lado = abs(ate - de), 1 if ate > de else -1
    d = (t1 - t0) / max(1, n)
    for i in range(n):
        v = de + i * lado
        E.salto(c, t, t0 + i * d, vx(v), vx(v + lado), y, alto, cor, d=max(0.2, d), largura=6)


def termometro(c, cx, y0, px, vmin, vmax, valor, a=1.0, marcas=(), size=48):
    """termômetro de pé: y0 = altura do zero, px = pixels por grau, valor = onde está o líquido (peça local)"""
    if a <= 0:
        return
    w, topo, base = 46, y0 - vmax * px - 26, y0 - vmin * px + 26
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, topo, w, base - topo + 30), w / 2, w / 2)
    c.drawRRect(r, M.paint(E.VAZIO, a))
    c.drawCircle(cx, base + 46, 56, M.paint(E.VAZIO, a))
    yv = y0 - valor * px
    M.rrect(c, cx - 12, yv, 24, base + 46 - yv, 6, E.COR, a)
    c.drawCircle(cx, base + 46, 42, M.paint(E.COR, a))
    c.drawRRect(r, M.paint(TINTA, a, stroke=4))
    for v in range(vmin, vmax + 1):
        yy = y0 - v * px
        M.line(c, cx + 34, yy, cx + (58 if v == 0 else 46), yy, TINTA, a, 5 if v == 0 else 3)
    for v in marcas:
        yy = y0 - v * px
        E.escreve(c, sn(v), cx + 70, yy + size * 0.35, size, "b", TINTA, a)


def camara(c, x, y, w, h, n, v, a=1.0, cor=None):
    """câmara fria: cartão com número e temperatura (peça local)"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 18, E.VAZIO, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 18, 18), M.paint(cor or TINTA, a, stroke=4))
    E.centro(c, f"câmara {n}", x + w / 2, y + 70, 54, "i", TINTA2, a)
    E.centro(c, f"{sn(v)}°", x + w / 2, y + h - 44, 110, "g", cor or COR, a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def conta():
        ka, kb, kc, kd = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
        y, s = 380, 190
        E.frase(c, t, ka + 0.5, pal("maior ou menor?", size=84), W / 2, 170, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: (E.centro(c, "−7", 620, y, s, "g", TINTA, a), E.centro(c, "−2", 1300, y, s, "g", TINTA, a)))
        E.saida(c, t, kb - 0.1, lambda: E.foco(c, t, ka + 0.3, 0.4, lambda a: E.centro(c, "?", 960, y, s, "g", COR, a)))
        E.foco(c, t, kb, 0.4, lambda a: E.centro(c, ">", 960, y, s, "g", ERRADO, a))
        E.frase(c, t, lerp(ka, kb, 0.55), [("7 > 2", "g", 84, TINTA2)] + pal("então...", size=80), W / 2, 540, "center", passo=0.1)
        E.risco(c, 880, y + 10, 1040, y - 130, t, kc, largura=16)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 1640, y - 60, 84, False, a))
        E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "−7 < −2", 780, 800, 170, "g", CERTO, a))
        E.frase(c, t, kd, pal("é", size=110) + [("menor", "g", 110, CERTO)], 1140, 800, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, conta)
    if t >= C["s02"]:
        ta, tb, tc = C["s02.a"], C["s02.b"], C["s02.c"]
        E.foco(c, t, tc - 0.2, 0.7, lambda a: E.bola(c, 1490, 520, 280 * ease_back(prog(t, tc - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, pal("até o fim desta aula", size=90), XE, 330)
        E.frase(c, t, lerp(ta, tb, 0.55), [("negativos", "g", 124, COR)], XE, 490)
        E.frase(c, t, lerp(ta, tb, 0.8), pal("na", size=110) + [("reta", "g", 124)], XE, 640, passo=0.12)
        E.frase(c, t, tb, pal("e o que é", size=110) + [("módulo", "g", 124, COR)], XE, 790, passo=0.12)
        E.foco(c, t, tc + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1490, 505, 84, "g", E.SOBRE, a),
                                               E.centro(c, "de prova", 1490, 590, 84, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    ka, kb, kc = C["s03.a"], C["s03.b"], C["s03.c"]
    E.frase(c, t, C["s03"] + 0.1, pal("você só precisa de"), XE, 410)
    E.foco(c, t, ka, 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, ka + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 960, 780
    for y, k, l1, l2 in ((230, kb, "saber", "subtrair"), (510, kc, "usar os sinais", "de > e de <")):
        p = ep(t, k, 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, k + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, k + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    E.frase(c, t, lerp(kc, C["s03.end"], 0.4), pal("abertura virada para o maior", size=62), x + 44, 800, passo=0.08)
    py = lerp(400, 680, ease_io(prog(t, kc - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, kb, 0.4))


# ---------------- o que é ----------------
def b_termometro(c, t, C, b):
    ka, kb, kc, kd, ke = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"], C["s04.e"]
    E.frase(c, t, C["s04"] + 0.1, pal("o que existe", size=92) + pal("abaixo", "g", 92, COR) + pal("do zero?", size=92), W / 2, 170, "center", passo=0.12)
    v = lerp(0, -3, ease_io(prog(t, kb + 0.3, 1.0)))
    E.foco(c, t, ka, 0.5, lambda a: termometro(c, 340, 400, 62, -4, 2, v, a, marcas=(2, 0, -2, -3)))
    x = 620
    E.frase(c, t, ka, [("0°", "g", 96, TINTA)] + pal("zero grau", size=78), x, 380, passo=0.1)
    E.frase(c, t, kb, pal("esfria", size=78) + [("3", "g", 88), ("graus", "i", 78)], x, 520, passo=0.1)
    E.frase(c, t, kc, pal("3 abaixo de zero", size=78), x, 660, passo=0.1)
    E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "−3", 1450, 480, 280, "g", COR, a))
    E.frase(c, t, ke - 0.3, pal("no banco:", size=78), x, 860, passo=0.1)
    E.frase(c, t, ke, pal("saldo", size=78) + [("−3", "g", 88, COR)], x + 300, 860, passo=0.1)
    E.foco(c, t, ke + 0.2, 0.5, lambda a: E.divida(c, 1450, 790, 380, 220, "R$ 3", a, topo="deve"))


# ---------------- reta ----------------
XR0, XR1, YR = 270, 1650, 500


def b_reta(c, t, C, b):
    ka, kb, kc, kd = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
    tm = [kd + 0.05 * (8 + v) for v in range(-8, 0)] + [kb] + [kc + 0.05 * v for v in range(1, 9)]
    if t < C["s06"]:
        E.frase(c, t, C["s05"] + 0.1, pal("deite o termômetro:", size=88) + [("a", "g", 88, COR), ("reta", "g", 88, COR), ("numérica", "g", 88, COR)], W / 2, 190, "center", passo=0.12)
    vx = E.reta(c, t, ka, XR0, XR1, YR, -8, 8, range(-8, 9), fmt=sn, size=46, tm=tm)

    def rotulos():
        for k, x0, x1, s in ((kc, vx(1), vx(8), "positivos"), (kd, vx(-8), vx(-1), "negativos")):
            E.chave(c, x0, x1, YR - 56, COR, ep(t, k, 0.5), h=-22)
            E.foco(c, t, k, 0.5, lambda a, x0=x0, x1=x1, s=s: E.centro(c, s, (x0 + x1) / 2, YR - 110, 70, "g", COR, a))
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "zero no meio", vx(0), YR - 170, 62, "i", TINTA, a))
        E.frase(c, t, lerp(kd, C["s05.end"], 0.55), pal("todo passo tem o", size=88) + [("mesmo", "g", 88, COR), ("tamanho", "g", 88, COR)], W / 2, 780, "center", passo=0.12)
    E.saida(c, t, C["s06"] - 0.1, rotulos)

    if C["s06"] <= t < C["s07"]:
        ka, kb, kc, kd, ke = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]
        fim = C["s06.end"]
        E.frase(c, t, C["s06"] + 0.1, pal("vamos marcar", size=88), W / 2, 190, "center")
        ponto(c, t, ka, vx(0), YR, TINTA)
        passos(c, t, kb + 0.2, kc - 0.5, 0, 4, vx, YR)
        passos(c, t, kc + 0.2, kd - 0.5, 0, -3, vx, YR)
        ponto(c, t, kc - 0.5, vx(4), YR)
        ponto(c, t, kd - 0.5, vx(-3), YR)
        E.foco(c, t, kc - 0.5, 0.4, lambda a: E.centro(c, "4", vx(4), YR - 110, 96, "g", COR, a))
        E.foco(c, t, kd - 0.5, 0.4, lambda a: E.centro(c, "−3", vx(-3), YR - 110, 96, "g", COR, a))
        E.frase(c, t, kd, pal("o", size=92) + [("sinal", "g", 92, COR)] + pal("diz o lado", size=92), W / 2, 730, "center", passo=0.12)
        E.frase(c, t, ke, pal("o", size=92) + [("número", "g", 92, COR)] + pal("diz quantos passos", size=92), W / 2, 850, "center", passo=0.12)
        E.frase(c, t, lerp(ke, fim, 0.6), [("4", "g", 76)] + pal("é o mesmo que", size=72) + [("+4", "g", 76)], W / 2, 970, "center", passo=0.12)

    if t >= C["s07"]:
        ka, kb, kc = C["s07.a"], C["s07.b"], C["s07.c"]
        fim = C["s07.end"]
        E.frase(c, t, C["s07"] + 0.1, pal("positivos, negativos e zero:", size=84), W / 2, 170, "center", passo=0.1)
        E.frase(c, t, ka, [("números", "g", 104, COR), ("inteiros", "g", 104, COR)], W / 2, 300, "center", passo=0.14)
        for v, ti in ((-2, kb), (0, kb + 0.8), (7, kb + 1.1)):
            ponto(c, t, ti, vx(v), YR)
        E.frase(c, t, lerp(ka, kb, 0.6), pal("sem nenhuma parte quebrada", size=72), W / 2, 720, "center", passo=0.1)
        E.frase(c, t, kc, [("zero", "g", 92, COR)] + pal("não é positivo nem negativo", size=88), W / 2, 830, "center", passo=0.12)
        E.frase(c, t, lerp(kc, fim, 0.6), pal("ele separa os lados", size=80), W / 2, 950, "center", passo=0.1)


# ---------------- comparar ----------------
def b_comparar(c, t, C, b):
    def regra():
        ka, kb, kc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
        E.frase(c, t, ka, pal("mais à", size=92) + [("direita", "g", 92, COR)] + pal("é", size=92) + [("maior", "g", 92, COR)], W / 2, 190, "center", passo=0.12)
        y = 470
        vx = E.reta(c, t, C["s08"] + 0.1, 300, 1620, y, -8, 3, range(-8, 4), fmt=sn, size=46)
        if t >= ka:
            p = ep(t, ka + 0.3, 0.8)
            M.arrow(c, 420, 310, 1500, 310, COR, p, 6, 20, p)
        ponto(c, t, kb, vx(-7), y)
        ponto(c, t, kc, vx(-2), y, TINTA)
        E.foco(c, t, kb, 0.4, lambda a: E.centro(c, "−7", vx(-7), y - 60, 84, "g", COR, a))
        E.foco(c, t, kc, 0.4, lambda a: E.centro(c, "−2", vx(-2), y - 60, 84, "g", TINTA, a))
        E.foco(c, t, kd, 0.5, lambda a: E.centro(c, "−7 < −2", W / 2, 820, 150, "g", CERTO, a))
    E.saida(c, t, C["s09"] - 0.1, regra)

    def dia():
        ka, kb = C["s09.a"], C["s09.b"]
        E.frase(c, t, C["s09"] + 0.1, pal("no dia a dia", size=88), W / 2, 170, "center")
        E.foco(c, t, ka, 0.5, lambda a: termometro(c, 310, 340, 40, -8, 1, -7, a, marcas=(0, -7)))
        E.foco(c, t, ka + 0.5, 0.5, lambda a: termometro(c, 620, 340, 40, -8, 1, -2, a, marcas=(0, -2)))
        E.frase(c, t, lerp(ka, kb, 0.45), [("−7", "g", 72, COR)] + pal("é mais frio", size=72), 500, 920, "center", passo=0.1)
        E.foco(c, t, kb, 0.5, lambda a: E.divida(c, 1190, 460, 370, 240, "R$ 7", a, topo="deve"))
        E.foco(c, t, kb + 0.5, 0.5, lambda a: E.divida(c, 1590, 460, 280, 180, "R$ 2", a, topo="deve"))
        E.frase(c, t, kb + 0.5, pal("dever", size=72) + [("7", "g", 72, ERRADO)] + pal("é pior que dever", size=72) + [("2", "g", 72)], 1370, 720, "center", passo=0.1)
    if C["s09"] - 0.1 <= t:
        E.saida(c, t, C["s10"] - 0.1, dia)

    if t >= C["s10"]:
        ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
        E.frase(c, t, C["s10"] + 0.1, pal("a regra vale para", size=84) + [("qualquer", "g", 84, COR)] + pal("comparação", size=84), W / 2, 190, "center", passo=0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.centro(c, "4 > −3", 560, 440, 170, "g", TINTA, a))
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "0 > −1", 1360, 440, 170, "g", TINTA, a))
        E.frase(c, t, lerp(kb, kc, 0.5), pal("todo negativo fica à", size=80) + [("esquerda", "g", 80, COR)] + pal("do zero", size=80), W / 2, 640, "center", passo=0.1)
        E.frase(c, t, kc, pal("todo negativo é", size=92) + [("menor", "g", 92, COR)] + pal("que zero", size=92), W / 2, 790, "center", passo=0.1)
        E.frase(c, t, kc + 1.4, pal("e menor que qualquer", size=92) + [("positivo", "g", 92, COR)], W / 2, 920, "center", passo=0.1)


# ---------------- módulo ----------------
def b_modulo(c, t, C, b):
    y = 500

    def primeira():
        ka, kb, kc, kd, ke, kf, kg = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"], C["s11.e"], C["s11.f"], C["s11.g"]
        E.frase(c, t, ka, [("módulo", "g", 92, COR)] + pal("é a distância até o zero", size=92), W / 2, 170, "center", passo=0.12)
        E.frase(c, t, kb, pal("duas barrinhas em pé:", size=76) + [("|   |", "g", 96, COR)], W / 2, 300, "center", passo=0.1)
        vx = E.reta(c, t, ka + 0.3, XR0, XR1, y, -8, 8, range(-8, 9), fmt=sn, size=46)
        ponto(c, t, kc, vx(-8), y)
        passos(c, t, lerp(kc, kd, 0.3), kd, -8, 0, vx, y)
        x0, x1 = vx(-8), vx(0)
        E.foco(c, t, kd, 0.4, lambda a: E.centro(c, "8 passos", (x0 + x1) / 2, y - 100, 66, "b", COR, a))
        yy = 790
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "|−8|", 560, yy, 150, "g", TINTA, a))
        E.foco(c, t, ke, 0.4, lambda a: E.escreve(c, "= 8", 745, yy, 150, "g", CERTO, a))
        E.foco(c, t, kf, 0.5, lambda a: E.centro(c, "|5| = 5", 1350, yy - 50, 100, "g", TINTA, a))
        E.foco(c, t, kg, 0.5, lambda a: E.centro(c, "|0| = 0", 1350, yy + 80, 100, "g", TINTA, a))
    E.saida(c, t, C["s12"] - 0.1, primeira)

    if t >= C["s12"]:
        ka, kb, kc = C["s12.a"], C["s12.b"], C["s12.c"]
        t0 = C["s12"]
        E.frase(c, t, ka, [("opostos:", "g", 92, COR)] + pal("mesma distância, lados contrários", size=84), W / 2, 170, "center", passo=0.1)
        vx = E.reta(c, t, t0, XR0, XR1, y, -8, 8, range(-8, 9), fmt=sn, size=46)
        ponto(c, t, t0, vx(-8), y)
        ponto(c, t, t0 + 0.1, vx(8), y)
        passos(c, t, t0 + 0.3, lerp(t0, ka, 0.45), 0, 8, vx, y)
        E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "oposto de 8 é −8", W / 2, 770, 110, "g", TINTA, a))
        ponto(c, t, kc, vx(-3), y, TINTA)
        ponto(c, t, kc, vx(3), y, TINTA)
        E.foco(c, t, kc, 0.5, lambda a: E.centro(c, "oposto de −3 é 3", W / 2, 920, 110, "g", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"]
    E.frase(c, t, C["s13"] + 0.1, [("cuidado:", "g", 92, ERRADO)] + pal("módulo não", size=92) + [("troca", "g", 92, ERRADO), ("o", "g", 92, ERRADO), ("sinal", "g", 92, ERRADO)], W / 2, 190, "center", passo=0.12)
    E.foco(c, t, kb, 0.5, lambda a: E.centro(c, "|8| = −8", 500, 420, 140, "g", ERRADO, a))
    E.foco(c, t, kb + 0.5, 0.5, lambda a: E.selo(c, 900, 370, 70, False, a))
    E.frase(c, t, kc, pal("ninguém anda", size=80) + [("−8", "g", 88, ERRADO)] + pal("passos", size=80), 1400, 400, "center", passo=0.1)
    y = 660
    vx = E.reta(c, t, kd, 400, 1500, y, 0, 8, range(0, 9), fmt=sn, size=46)
    ponto(c, t, kd, vx(8), y)
    passos(c, t, kd + 0.2, ke - 0.2, 8, 0, vx, y)
    E.foco(c, t, ke - 0.3, 0.4, lambda a: E.centro(c, "8 passos", vx(4), y - 94, 66, "b", COR, a))
    E.frase(c, t, ke, [("módulo", "g", 96, COR)] + pal("nunca dá", size=96) + [("negativo", "g", 96, COR)], W / 2, 930, "center", passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def vira():
        ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
        E.frase(c, t, C["s14"] + 0.1, pal("agora, o atalho:", size=80, cor=CLARO), W / 2, 210, "center", passo=0.1)
        E.frase(c, t, ka, pal("entre negativos,", size=100, cor=BR) + [("vira", "g", 100, BR)] + pal("ao contrário", size=100, cor=BR), W / 2, 350, "center", passo=0.1)
        E.frase(c, t, kb, pal("compare sem o sinal", size=76, cor=CLARO), 520, 560, "center", passo=0.1)
        E.foco(c, t, kb + 0.4, 0.5, lambda a: E.centro(c, "7 > 2", 520, 760, 170, "g", BR, a))
        E.frase(c, t, kc, pal("ponha o menos e inverta", size=76, cor=CLARO), 1400, 560, "center", passo=0.1)
        E.foco(c, t, kc + 0.4, 0.5, lambda a: E.centro(c, "−7 < −2", 1400, 760, 170, "g", CLARO, a))
        if t >= kc:
            p = ep(t, kc + 0.2, 0.6)
            M.arrow(c, 800, 710, 1040, 710, CLARO, p, 6, 20, p)
    E.saida(c, t, C["s15"] - 0.1, vira)

    if t >= C["s15"]:
        ka, kb, kc = C["s15.a"], C["s15.b"], C["s15.c"]
        y = 410
        vx = E.reta(c, t, C["s15"] + 0.1, 330, 1500, y, -9, 0, range(-9, 1), fmt=sn, escuro=True, size=46)
        E.frase(c, t, ka, pal("mais longe do zero,", size=80, cor=CLARO) + [("mais", "g", 80, BR), ("à", "g", 80, BR), ("esquerda", "g", 80, BR)], W / 2, 200, "center", passo=0.1)
        if t >= ka:
            p = ep(t, ka + 0.3, 1.0)
            M.arrow(c, vx(0), y - 60, vx(-9), y - 60, CLARO, p, 6, 20, p)
        E.foco(c, t, lerp(ka, kb, 0.72), 0.5, lambda a: E.centro(c, "e mais à esquerda é menor", W / 2, 610, 76, "i", BR, a))
        E.foco(c, t, kb, 0.5, lambda a: E.selo(c, 340, 740, 62, False, a))
        E.frase(c, t, kb, pal("só vale com", size=76, cor=CLARO) + [("dois", "g", 76, BR), ("negativos", "g", 76, BR)], 440, 765, passo=0.1)
        E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 340, 890, 62, True, a))
        E.frase(c, t, kc, pal("negativo contra positivo:", size=76, cor=CLARO) + [("o", "g", 76, BR), ("positivo", "g", 76, BR), ("ganha", "g", 76, BR)], 440, 915, passo=0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    ka, kb, kc, kd, ke = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
    E.frase(c, t, C["s16"], pal("hora de testar", size=72, cor=COR), XE, 170)
    for x, k, n, v in ((XE, ka, 1, -9), (XE + 355, kb, 2, 2), (XE + 710, kc, 3, -4)):
        E.foco(c, t, k, 0.5, lambda a, x=x, n=n, v=v: camara(c, x, 220, 330, 240, n, v, a))
    E.frase(c, t, kd, pal("em ordem, da", size=84) + [("mais", "g", 84, COR), ("fria", "g", 84, COR)], XE, 610, passo=0.1)
    E.frase(c, t, kd + 0.8, pal("para a", size=84) + [("mais", "g", 84, COR), ("quente", "g", 84, COR)], XE, 720, passo=0.1)
    E.frase(c, t, ke, pal("qual está mais", size=92) + [("perto", "g", 92, COR)] + pal("do zero?", size=92), XE, 900, passo=0.1)
    E.relogio(c, t, C["s17.a"], 1520, 400, 180)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    y = 340
    t0 = C["s18"]
    E.frase(c, t, t0 + 0.1, pal("na reta", size=80), W / 2, 150, "center")
    vx = E.reta(c, t, t0 + 0.1, 260, 1640, y, -10, 3, range(-10, 4), fmt=sn, size=46)

    def rot(v, n, s_, ti, cor=None):
        ponto(c, t, ti, vx(v), y, cor)
        E.foco(c, t, ti, 0.4, lambda a: (E.centro(c, n, vx(v), y - 60, 66, "g", cor or COR, a)))

    def ordem():
        ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
        rot(-9, "câmara 1", "", ka)
        rot(-4, "câmara 3", "", kb)
        rot(2, "câmara 2", "", kc)
        for x, s_, k, l in ((420, "−9°", ka, "câmara 1"), (960, "−4°", kb, "câmara 3"), (1500, "2°", kc, "câmara 2")):
            E.foco(c, t, k, 0.5, lambda a, x=x, s_=s_, l=l: (E.centro(c, s_, x, 660, 150, "g", COR, a), E.centro(c, l, x, 760, 66, "i", TINTA, a)))
        E.foco(c, t, ka + 0.3, 0.5, lambda a: E.centro(c, "a mais fria", 420, 860, 62, "b", COR, a))
        for x, k in ((690, kb), (1230, kc)):
            E.foco(c, t, k, 0.4, lambda a, x=x: E.centro(c, "<", x, 650, 110, "g", TINTA, a))
    E.saida(c, t, C["s19"] - 0.1, ordem)

    if t >= C["s19"]:
        ka, kb, kc, kd = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
        for v, n in ((-9, "1"), (-4, "3"), (2, "2")):
            ponto(c, t, t0, vx(v), y)
        for k, de, x, s_ in ((ka, -9, 380, "|−9| = 9"), (kb, -4, 960, "|−4| = 4"), (kc, 2, 1540, "|2| = 2")):
            if t >= k:
                passos(c, t, k, k + 0.6, de, 0, vx, y, alto=42)
            E.foco(c, t, k, 0.5, lambda a, s_=s_, x=x: E.centro(c, s_, x, 690, 104, "g", TINTA, a))
        E.frase(c, t, C["s19"] + 0.1, pal("compare as", size=76) + [("distâncias", "g", 76, COR)], W / 2, 540, "center", passo=0.1)
        E.frase(c, t, kd - 0.4, pal("a menor distância:", size=84), 620, 900, "center", passo=0.1)
        E.foco(c, t, kd, 0.5, lambda a: E.pilula(c, "câmara 2", 1240, 875, 92, estilo="g", fundo=CERTO, cor=BR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s20.a", "o sinal diz o lado"), ("s20.b", "mais à direita é maior"), ("s20.c", "módulo: distância até o zero"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a), E.centro(c, str(i + 1), 300, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 84)], 400, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"] + 0.1, pal("próxima aula"), XE, 270)
    E.frase(c, t, C["s21.a"], pal("conta com esses números:", size=92), XE, 400, passo=0.1)
    E.frase(c, t, C["s21.b"], [("somar", "g", 110, COR)] + pal("e", size=100) + [("subtrair", "g", 110, COR), ("inteiros", "g", 110, COR)], XE, 540, passo=0.12)
    E.frase(c, t, C["s21.c"], pal("pensando em", size=96) + [("dívida", "g", 96)] + pal("e", size=96) + [("pagamento", "g", 96)], XE, 680, passo=0.12)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1800, 1630, p), lerp(990, 815, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], 700, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, termometro=b_termometro, reta=b_reta, comparar=b_comparar, modulo=b_modulo,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
