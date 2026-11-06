"""Visual — Estudativo · MAT-DIV-001: múltiplos e divisores.
Peças da aula: ovos em caixas (a divisão vira coisa concreta) e as 36 cadeiras que se rearrumam, uma multiplicação por vez, ao lado da tabela de pares.
Todo instante vem de C[...]: fala sem cue usa um ponto entre dois cues (lerp), para continuar certo com a voz real."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro, linha
import motor as M
import skia

E.usar("Matemática", "Divisibilidade, MMC e MDC")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-DIV-001_multiplos_divisores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("multiplo", "pares", "atalho", "questao", "fim"))
BR = "#FFFFFF"


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None, tinta=None):
    """número dentro da esfera"""
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a)


def bola_entra(c, t, t0, s, cx, cy, r, size, cor=None, tinta=None):
    """esfera com número que chega com salto em t0"""
    q = ease_back(prog(t, t0, 0.5))
    if q > 0.05:
        num_bola(c, s, cx, cy, r * q, max(2, round(size * q)), 1.0, cor, tinta)


def bloco(c, x, y, w, h, r, cor, a=1.0, stroke=None):
    """retângulo arredondado cheio ou só contorno"""
    if a > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), M.paint(cor, a, stroke=stroke))


def ovo(c, cx, cy, r, cor=None, a=1.0):
    """ovo com volume"""
    if a <= 0:
        return
    cor = cor or E.COR
    rx, ry = r * 0.8, r
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(
        skia.Point(cx - rx * 0.3, cy - ry * 0.4), r * 1.7,
        [M.hexc(M.mix(cor, BR, 0.4), a), M.hexc(cor, a), M.hexc(M.mix(cor, "#000000", 0.25), a)], [0.0, 0.5, 1.0]))
    c.drawOval(skia.Rect.MakeLTRB(cx - rx, cy - ry, cx + rx, cy + ry), p)


OX, OY, OW, OH, OG = 140, 215, 270, 190, 24  # as 9 caixas, 3 por linha


def caixas_ovos(c, t, t_ovos, t_caixas, cor):
    """os 54 ovos chegam soltos em t_ovos; t_caixas = instante do contorno de cada caixa"""
    for i in range(9):
        x, y = OX + (i % 3) * (OW + OG), OY + (i // 3) * (OH + OG)
        p = ep(t, t_caixas[i], 0.4)
        if p > 0:
            bloco(c, x, y, OW, OH, 22, BR, 0.75 * p)
            bloco(c, x, y, OW, OH, 22, cor, p, 4)
        for j in range(6):
            ex, ey = x + OW * ((j % 3) + 0.5) / 3, y + OH * ((j // 3) + 0.5) / 2
            ovo(c, ex, ey, 38, a=ep(t, t_ovos + (i * 6 + j) * 0.018, 0.3))


def fileiras_7(c, t, t0, t1, tr):
    """54 ÷ 7: sete bandejas de 7 ovos e os 5 que sobram, em vermelho"""
    for i in range(7):
        y = 215 + i * 84
        p = ep(t, lerp(t0, t1, i / 7), 0.35)
        bloco(c, 170, y, 610, 72, 18, BR, 0.75 * p)
        bloco(c, 170, y, 610, 72, 18, TINTA, p, 3)
        for j in range(7):
            ovo(c, 170 + 610 * (j + 0.5) / 7, y + 36, 28, a=p)
    for j in range(5):
        ovo(c, 205 + j * 87, 860, 32, ERRADO, ep(t, tr + j * 0.08, 0.35))


CX, CY, CW, CH = 130, 190, 1040, 640  # área das cadeiras


def arranjo(lin, col):
    """posição de cada uma das 36 cadeiras em lin × col, centradas na área"""
    lado = min(CW / col, CH / lin, 86)
    x0, y0 = CX + (CW - lado * col) / 2, CY + (CH - lado * lin) / 2
    return [(x0 + lado * (j + 0.5), y0 + lado * (i + 0.5)) for i in range(lin) for j in range(col)][:36], lado


def cadeira(c, cx, cy, s, cor, a=1.0):
    w = s * 0.72
    bloco(c, cx - w * 0.36, cy - w * 0.56, w * 0.72, w * 0.56, w * 0.14, cor, a)  # encosto
    bloco(c, cx - w / 2, cy + w * 0.08, w, w * 0.3, w * 0.1, cor, a)  # assento
    bloco(c, cx - w * 0.42, cy + w * 0.3, w * 0.12, w * 0.24, w * 0.04, cor, a)  # pés
    bloco(c, cx + w * 0.3, cy + w * 0.3, w * 0.12, w * 0.24, w * 0.04, cor, a)


def cadeiras(c, t, t0, etapas, ruim=None):
    """as mesmas 36 cadeiras: etapas = [(instante, linhas, colunas)]; ruim = (de, até): a 36ª fica vermelha"""
    pos, lado = arranjo(*etapas[0][1:])
    for ti, lin, col in etapas[1:]:
        if t < ti:
            break
        q, (dest, l2) = ease_io(prog(t, ti, 0.65)), arranjo(lin, col)
        pos = [(lerp(a, x, q), lerp(b, y, q)) for (a, b), (x, y) in zip(pos, dest)]
        lado = lerp(lado, l2, q)
    for i, (x, y) in enumerate(pos):
        fora = ruim and i == 35 and ruim[0] <= t < ruim[1]
        cadeira(c, x, y, lado, ERRADO if fora else E.COR, ep(t, t0 + i * 0.015, 0.3))


def par(c, t, t0, a, b, y, xs, s, cor=TINTA, cor2=None):
    """uma linha a × b da tabela de pares"""
    cor2 = cor2 or cor
    E.foco(c, t, t0, 0.4, lambda q: centro(c, str(a), xs[0], y, s, "g", cor, q))
    E.foco(c, t, t0 + 0.1, 0.4, lambda q: centro(c, "×", xs[1], y, s * 0.8, "b", CINZA, q))
    E.foco(c, t, t0 + 0.2, 0.4, lambda q: centro(c, str(b), xs[2], y, s, "g", cor2, q))


def sem_par(c, t, t0, tr, a, nota, y, xs, s):
    """linha que não serve: o número, o motivo e um risco"""
    E.foco(c, t, t0, 0.4, lambda q: centro(c, str(a), xs[0], y, s, "g", CINZA, q))
    E.foco(c, t, t0 + 0.1, 0.4, lambda q: E.escreve(c, nota, xs[1] - 30, y - 4, s * 0.72, "b", ERRADO, q))
    if t >= tr:
        E.risco(c, xs[0] - 50, y - s * 0.3, xs[1] + E.larg(nota, "b", s * 0.72) - 10, y - s * 0.3, t, tr, largura=8)


def relogio(c, t, t0):
    """relógio de pausa: enche em 3 segundos"""
    r = 210 * ease_back(prog(t, t0, 0.6))
    if r > 0:
        cx, cy = 1490, 440
        E.bola(c, cx, cy, r)
        f = M.clamp(prog(t, t0 + 0.8, 3.0))
        if f > 0:
            E.arco(c, cx, cy, r + 34, -90, 360 * f, TINTA, 10)
        for dx in (-44, 44):
            M.rrect(c, cx + dx - 22, cy - 80, 44, 160, 12, E.SOBRE, ep(t, t0 + 0.2, 0.4))
        E.foco(c, t, t0 + 0.2, 0.5, lambda a: centro(c, "pause o vídeo", cx, cy + r + 120, 64, "i", TINTA, a))


# ---------------- gancho ----------------
FALTA = ("?", 2, 3, 4, 6, 9, 12, "?", "?")


def b_gancho(c, t, C, b):
    def pergunta():
        s0 = C["s01"]
        E.frase(c, t, s0 + 0.3, [("quantos", "i", 100), ("divisores", "g", 92, COR), ("tem", "i", 100)], W / 2, 180, "center", passo=0.16)
        bola_entra(c, t, C["s01.a"], "36", W / 2, 420, 165, 170)
        E.frase(c, t, lerp(C["s01.a"], C["s01.b"], 0.45), [("contou", "i", 72), ("de", "i", 72), ("cabeça?", "i", 72)], W / 2, 690, "center", passo=0.14)
        for i, n in enumerate(FALTA):
            x, ti = W / 2 + (i - 4) * 170, C["s01.b"] + i * 0.07
            if n == "?":
                p = ep(t, ti, 0.4)
                E.caixa_pontilhada(c, x - 62, 760, 124, 136, p, ERRADO, prog_=p)
                E.foco(c, t, ti + 0.1, 0.4, lambda a, x=x: centro(c, "?", x, 860, 104, "g", ERRADO, a))
            else:
                E.foco(c, t, ti, 0.4, lambda a, x=x, n=n: centro(c, str(n), x, 860, 104, "g", TINTA, a))
        E.frase(c, t, C["s01.b"] + 0.7, [("esqueceu", "g", 62, ERRADO), ("algum", "g", 62, ERRADO)], W / 2, 980, "center")
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        s0 = C["s02"]
        q = ease_back(prog(t, C["s02.b"] - 0.2, 0.7))
        if q > 0:
            E.bola(c, 1480, 540, 290 * q)
        E.frase(c, t, s0 + 0.35, [("até", "i", 90), ("o", "i", 90), ("fim", "i", 90), ("da", "i", 90), ("aula", "i", 90)], XE, 350)
        E.frase(c, t, lerp(s0, C["s02.a"], 0.55), [("você", "i", 124), ("lista", "g", 124)], XE, 510)
        E.frase(c, t, C["s02.a"], [("todos", "g", 130, COR)], XE, 660)
        E.frase(c, t, C["s02.a"] + 0.5, [("sem", "i", 90), ("esquecer", "i", 90), ("nenhum", "i", 90)], XE, 800, passo=0.16)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1480, 525, 84, "g", E.SOBRE, a),
                                                      centro(c, "de prova", 1480, 610, 84, "i", E.SOBRE, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    s0 = C["s03"]
    E.frase(c, t, s0 + 0.35, [("para", "i", 84), ("acompanhar,", "i", 84)], XE, 290)
    E.frase(c, t, lerp(s0, C["s03.a"], 0.5), [("você", "i", 84), ("só", "i", 84), ("precisa", "i", 84), ("de", "i", 84)], XE, 400, passo=0.13)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 180, 705, 120, "i", TINTA, a))
    fim = lerp(C["s03.c"], C["s03.end"], 0.4)
    E.frase(c, t, fim, [("enferrujado?", "i", 62)], XE, 850)
    E.frase(c, t, fim + 0.5, [("procure", "i", 62), ("a", "i", 62), ("aula", "i", 62), ("no", "i", 62), ("canal", "i", 62)], XE, 930, passo=0.14)

    x = 900
    p = ep(t, C["s03.a"] + 0.2, 0.5)
    E.caixa_pontilhada(c, x, 150, 880, 180, p, prog_=p)
    E.frase(c, t, lerp(C["s03.a"], C["s03.b"], 0.2), [("faça", "i", 62), ("uma", "i", 62), ("divisão", "i", 62)], x + 44, 225, passo=0.14)
    E.frase(c, t, lerp(C["s03.a"], C["s03.b"], 0.5), [("e", "g", 60), ("veja", "g", 60), ("se", "g", 60), ("sobrou", "g", 60), ("resto", "g", 60, COR)], x + 44, 300, passo=0.14)
    # 17 bolinhas: três grupos de 5 e duas que sobram
    for i in range(3):
        y = 410 + i * 92
        p = ep(t, C["s03.b"] + i * 0.3, 0.35)
        for j in range(5):
            E.bola(c, 960 + j * 92, y, 36, a=p)
    for i in range(2):
        E.bola(c, 1520 + i * 92, 410, 36, ERRADO, ep(t, C["s03.c"] + i * 0.12, 0.35))
    linha(c, t, [("17", "g", 120, TINTA, C["s03.b"]), ("÷", "g", 100, CINZA, C["s03.b"] + 0.15), ("5", "g", 120, TINTA, C["s03.b"] + 0.3),
                 ("=", "g", 100, CINZA, C["s03.b"] + 0.45), ("3", "g", 120, COR, C["s03.b"] + 0.6)], x + 44, 800)
    E.frase(c, t, C["s03.c"], [("sobram", "i", 96), ("2", "g", 110, ERRADO)], x + 44, 950)


# ---------------- múltiplo ----------------
def b_multiplo(c, t, C, b):
    def ovos():
        fecha = [C["s05.a"] + i * 0.14 for i in range(9)]
        fecha[0] = C["s04.b"]  # a primeira caixa aparece na fala "caixas de seis"
        caixas_ovos(c, t, C["s04.a"], fecha, CERTO if t >= C["s05.c"] else TINTA)
    E.saida(c, t, C["s06"] - 0.1, ovos)

    X = 1090

    def cena():
        E.frase(c, t, C["s04"] + 0.3, [("uma", "i", 72), ("cena", "i", 72), ("do", "i", 72), ("dia", "i", 72), ("a", "i", 72), ("dia", "i", 72)], X, 230, passo=0.14)
        linha(c, t, [("54", "g", 170, COR, C["s04.a"]), ("ovos", "i", 130, TINTA, C["s04.a"] + 0.3)], X, 450)
        linha(c, t, [("caixas", "i", 110, TINTA, C["s04.b"]), ("de", "i", 110, TINTA, C["s04.b"] + 0.2), ("6", "g", 130, COR, C["s04.b"] + 0.35)], X, 620)
        q = lerp(C["s04.b"], C["s04.end"], 0.45)
        E.frase(c, t, q, [("dá", "i", 72), ("para", "i", 72), ("encher", "i", 72), ("as", "i", 72), ("caixas", "i", 72)], X, 780, passo=0.13)
        E.frase(c, t, q + 0.6, [("sem", "g", 68), ("sobrar", "g", 68), ("nenhum?", "g", 68, COR)], X, 870, passo=0.14)
    E.saida(c, t, C["s05"] - 0.1, cena)

    def conta():
        a_ = C["s05.a"]
        linha(c, t, [("54", "g", 130, TINTA, a_), ("÷", "g", 110, CINZA, a_ + 0.3), ("6", "g", 130, TINTA, a_ + 0.5), ("=", "g", 110, CINZA, a_ + 0.8), ("9", "g", 130, COR, a_ + 1.0)], X, 400)
        E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "resto 0", X + 240, 540, 84, estilo="g", fundo=CERTO, cor=BR, a=a))
        bola_entra(c, t, C["s05.c"], "9", X + 110, 780, 110, 130)
        E.frase(c, t, C["s05.c"] + 0.2, [("caixas", "g", 72, COR)], X + 250, 765)
        E.frase(c, t, C["s05.c"] + 0.4, [("cheias", "i", 76)], X + 250, 850)
    if t >= C["s05"]:
        E.saida(c, t, C["s06"] - 0.1, conta)

    # o nome
    def nome():
        s0 = C["s06"]
        E.frase(c, t, s0 + 0.3, [("quando", "i", 84), ("a", "i", 84), ("divisão", "i", 84), ("fecha", "g", 78, COR), ("assim", "i", 84)], W / 2, 190, "center", passo=0.16)
        a_ = C["s06.a"]
        linha(c, t, [("54", "g", 170, TINTA, a_), ("é", "i", 130, TINTA, a_ + 0.25), ("múltiplo", "g", 170, COR, a_ + 0.4), ("de", "i", 130, TINTA, a_ + 0.8), ("6", "g", 170, TINTA, a_ + 1.0)], W / 2, 430, "center")
        q0, q1 = lerp(a_, C["s06.b"], 0.3), lerp(a_, C["s06.b"], 0.72)
        E.frase(c, t, q0, [("o", "i", 76), ("resultado", "i", 76), ("de", "i", 76), ("multiplicar", "g", 70), ("o", "i", 76), ("número", "i", 76)], W / 2, 600, "center", passo=0.16)
        E.frase(c, t, q1, [("como", "i", 76), ("na", "i", 76), ("tabuada,", "i", 76), ("sem", "g", 70), ("parar", "g", 70), ("no", "g", 70), ("10", "g", 70, COR)], W / 2, 710, "center", passo=0.16)
        v = C["s06.b"]
        linha(c, t, [("6", "g", 150, TINTA, v), ("×", "g", 120, CINZA, v + 0.25), ("9", "g", 150, TINTA, v + 0.45), ("=", "g", 120, CINZA, v + 0.8), ("54", "g", 150, COR, v + 1.0)], W / 2, 920, "center")
    if t >= C["s06"]:
        E.saida(c, t, C["s07"] - 0.1, nome)

    # com sete
    def sete():
        s0 = C["s07"]
        fileiras_7(c, t, C["s07.a"], C["s07.b"], C["s07.b"])
        X7 = 900
        E.frase(c, t, s0 + 0.3, [("e", "i", 110), ("com", "i", 110), ("7?", "g", 120, COR)], X7, 280)
        a_ = C["s07.a"]
        linha(c, t, [("54", "g", 130, TINTA, a_), ("÷", "g", 110, CINZA, a_ + 0.3), ("7", "g", 130, TINTA, a_ + 0.5), ("=", "g", 110, CINZA, a_ + 0.8), ("7", "g", 130, COR, a_ + 1.0)], X7, 480)
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "sobram 5", X7 + 250, 620, 84, estilo="g", fundo=ERRADO, cor=BR, a=a))
        v = C["s07.c"]
        linha(c, t, [("54", "g", 96, TINTA, v), ("não", "g", 96, ERRADO, v + 0.2), ("é", "i", 96, TINTA, v + 0.35)], X7, 800)
        linha(c, t, [("múltiplo", "g", 96, TINTA, v + 0.5), ("de", "i", 96, TINTA, v + 0.7), ("7", "g", 96, TINTA, v + 0.85)], X7, 910)
    if t >= C["s07"]:
        E.saida(c, t, C["s08"] - 0.1, sete)

    # sem fim
    if t >= C["s08"]:
        s0 = C["s08"]
        E.frase(c, t, s0 + 0.3, [("a", "i", 96), ("lista", "i", 96), ("de", "i", 96), ("múltiplos", "g", 90, COR)], XE, 280, passo=0.14)
        E.frase(c, t, lerp(s0, C["s08.a"], 0.6), [("nunca", "i", 96), ("termina", "i", 96)], XE, 400)
        xs = (230, 450, 680, 910)
        for i, (n, x) in enumerate(zip((6, 12, 18, 24), xs)):
            E.foco(c, t, lerp(C["s08.a"], C["s08.b"], i * 0.16), 0.4, lambda a, n=n, x=x: centro(c, str(n), x, 660, 130, "g", TINTA, a))
        ti = lerp(C["s08.a"], C["s08.b"], 0.68)
        for n, x in ((30, 1110), (36, 1270)):
            E.foco(c, t, ti, 0.4, lambda a, n=n, x=x: centro(c, str(n), x, 660, 104, "b", CINZA, a))
        if t >= C["s08.b"] - 0.3:
            p = ep(t, C["s08.b"] - 0.3, 0.6)
            M.arrow(c, 1390, 625, 1780, 625, E.COR, p, 8, 30, p)
        E.frase(c, t, C["s08.b"], [("sem", "g", 120, COR), ("fim", "g", 120, COR)], W / 2, 870, "center")


# ---------------- divisor ----------------
def b_divisor(c, t, C, b):
    def lados():
        s0 = C["s09"]
        E.frase(c, t, s0 + 0.3, [("a", "i", 84), ("mesma", "i", 84), ("história", "i", 84), ("tem", "i", 84), ("outro", "i", 84), ("lado", "g", 78, COR)], W / 2, 190, "center", passo=0.14)
        t1 = lerp(s0, C["s09.a"], 0.5)
        bola_entra(c, t, t1, "54", 400, 520, 170, 170)
        bola_entra(c, t, t1 + 0.15, "6", 1520, 520, 120, 150)
        E.ponte(c, t, t1 + 0.35, 590, 1380, 430, "é múltiplo de", size=60)
        E.ponte(c, t, C["s09.a"], 1380, 590, 620, "é divisor de", TINTA, size=60)
        v = C["s09.b"]
        E.frase(c, t, lerp(C["s09.a"], v, 0.55), [("divisor:", "g", 84, COR), ("o", "i", 88), ("número", "i", 88), ("que", "i", 88), ("divide", "i", 88)], W / 2, 830, "center", passo=0.14)
        E.frase(c, t, v, [("sem", "g", 96), ("deixar", "g", 96), ("resto", "g", 96, CERTO)], W / 2, 950, "center")
    E.saida(c, t, C["s10"] - 0.1, lados)

    if t >= C["s10"]:
        a_ = C["s10.a"]
        E.frase(c, t, C["s10"] + 0.25, [("a", "i", 84), ("mesma", "i", 84), ("ideia,", "i", 84)], 330, 180, passo=0.14)
        E.frase(c, t, a_, [("dita", "i", 84), ("de", "i", 84), ("outro", "i", 84), ("jeito", "g", 78, COR)], 830, 180, passo=0.14)
        t1 = lerp(a_, C["s10.b"], 0.5)
        E.frase(c, t, t1, [("múltiplos", "g", 66, COR), ("de", "i", 72), ("6", "g", 66)], XE, 320, passo=0.12)
        for i, n in enumerate((6, 12, 18, 24)):
            E.foco(c, t, t1 + 0.2 + i * 0.12, 0.4, lambda a, i=i, n=n: centro(c, str(n), 250 + i * 230, 460, 120, "g", TINTA, a))
        if t >= t1 + 0.7:
            p = ep(t, t1 + 0.7, 0.5)
            M.arrow(c, 1110, 420, 1760, 420, CINZA, p, 7, 26, p)
        v = C["s10.b"]
        E.frase(c, t, v, [("divisores", "g", 66, COR), ("de", "i", 72), ("6", "g", 66)], XE, 600, passo=0.12)
        for i, n in enumerate((1, 2, 3, 6)):
            E.foco(c, t, v + 0.2 + i * 0.12, 0.4, lambda a, i=i, n=n: centro(c, str(n), 250 + i * 230, 740, 120, "g", TINTA, a))
        if t >= v + 0.7:
            p = ep(t, v + 0.7, 0.3)
            M.line(c, 1090, 620, 1090, 770, ERRADO, 1.0, 12, progress=p)
        E.foco(c, t, v + 0.8, 0.5, lambda a: E.pilula(c, "acabam aqui", 1420, 690, 72, estilo="g", fundo=ERRADO, cor=BR, a=a))
        q = lerp(v, C["s10.end"], 0.45)
        E.frase(c, t, q, [("nenhum", "i", 80), ("divisor", "i", 80), ("passa", "i", 80), ("do", "i", 80), ("próprio", "g", 74, COR), ("número", "g", 74, COR)], W / 2, 930, "center", passo=0.14)


# ---------------- divisores em pares ----------------
TX, TY, TD, TS = (1300, 1420, 1570), 262, 112, 92  # a tabela de pares


def b_pares(c, t, C, b):
    def tudo():
        etapas = [(None, 6, 6), (C["s12.a"], 1, 36), (C["s12.b"], 2, 18), (C["s12.c"], 3, 12), (C["s12.d"], 4, 9), (C["s13"] + 0.3, 6, 7), (C["s13.c"], 6, 6)]
        cadeiras(c, t, C["s11.a"], etapas, ruim=(C["s13.a"], C["s13.c"]))
        leg = [(C["s12.a"], "1 fileira de 36"), (C["s12.b"], "2 fileiras de 18"), (C["s12.c"], "3 fileiras de 12"), (C["s12.d"], "4 fileiras de 9"),
               (C["s13"] + 0.3, "5 fileiras?"), (C["s13.c"], "6 fileiras de 6")]
        for i, (ti, s) in enumerate(leg):
            fim = leg[i + 1][0] - 0.15 if i + 1 < len(leg) else C["s14"]
            if t < fim + 0.3:
                E.saida(c, t, fim, lambda ti=ti, s=s: E.foco(c, t, ti, 0.4, lambda a: centro(c, s, CX + CW / 2, 925, 90, "i", TINTA, a)), d=0.2)

        X = 1210

        def explica():
            linha(c, t, [("36", "g", 130, COR, C["s11.a"]), ("cadeiras", "i", 104, TINTA, C["s11.a"] + 0.3)], X, 300)
            E.frase(c, t, C["s11.a"] + 0.8, [("em", "i", 80), ("fileiras", "i", 80), ("iguais", "g", 74)], X, 410, passo=0.16)
            E.frase(c, t, lerp(C["s11.a"], C["s11.b"], 0.6), [("cada", "i", 76), ("arrumação", "i", 76)], X, 590, passo=0.16)
            E.frase(c, t, C["s11.b"], [("uma", "g", 62), ("multiplicação", "g", 62, COR)], X, 680, passo=0.16)
            E.frase(c, t, C["s11.c"] - 0.3, [("cada", "i", 76), ("multiplicação", "i", 70)], X, 800, passo=0.16)
            E.frase(c, t, C["s11.c"], [("um", "g", 62), ("par", "g", 62, COR), ("de", "g", 62), ("divisores", "g", 62)], X, 890, passo=0.16)
        E.saida(c, t, C["s12"] - 0.1, explica)

        if t >= C["s12"]:
            E.frase(c, t, C["s12"] + 0.3, [("do", "i", 76), ("1", "g", 76, COR), ("para", "i", 76), ("cima", "i", 76)], X, 150, passo=0.14)
            for i, (a_, b_, k) in enumerate(((1, 36, "s12.a"), (2, 18, "s12.b"), (3, 12, "s12.c"), (4, 9, "s12.d"))):
                par(c, t, C[k], a_, b_, TY + i * TD, TX, TS, COR, TINTA)
            sem_par(c, t, C["s13"] + 0.3, C["s13.b"], 5, "resto 1", TY + 4 * TD, TX, TS)
            par(c, t, C["s13.c"], 6, 6, TY + 5 * TD, TX, TS, COR, CINZA if t >= C["s13.d"] else TINTA)
            E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "o 6 conta 1 vez", TX[1], 935, 50, estilo="g", fundo=E.COR, cor=BR, a=a))
    E.saida(c, t, C["s14"] - 0.1, tudo)

    if t >= C["s14"]:
        E.frase(c, t, C["s14"] + 0.25, [("juntando", "i", 90), ("tudo,", "i", 90), ("em", "i", 90), ("ordem", "g", 84, COR)], W / 2, 210, "center", passo=0.14)
        v, nb, nc = C["s14.a"], C["s14.b"], C["s14.c"]
        for i, n in enumerate((1, 2, 3, 4, 6, 9, 12, 18, 36)):
            x, ti = 190 + i * 190, lerp(v, nb, i / 10)
            ponta = i in (0, 8)
            q = ep(t, nc, 0.5)
            cor = M.mix(E.COR, CINZA, 0 if ponta else q)
            bola_entra(c, t, ti, str(n), x, 450, 86, 72, cor)
            if ponta:
                E.caixa_pontilhada(c, x - 104, 346, 208, 208, q, ERRADO, prog_=q)
        linha(c, t, [("9", "g", 130, COR, nb), ("divisores", "g", 130, TINTA, nb + 0.2)], W / 2, 730, "center")
        E.frase(c, t, nc, [("o", "i", 78), ("1", "g", 78, COR), ("e", "i", 78), ("o", "i", 78), ("próprio", "i", 78), ("número", "i", 78), ("sempre", "i", 78), ("entram", "g", 72, COR)], W / 2, 860, "center", passo=0.13)
        E.frase(c, t, lerp(nc, C["s14.end"], 0.55), [("e", "i", 78), ("são", "i", 78), ("os", "i", 78), ("mais", "i", 78), ("esquecidos", "g", 72, ERRADO)], W / 2, 970, "center", passo=0.13)


# ---------------- erro ----------------
BX, BW = 420, 1080  # as barras: 54 tem 9 vezes a largura de 6


def b_erro(c, t, C, b):
    def troca():
        s0 = C["s15"]
        a_ = C["s15.a"]
        linha(c, t, [("o", "i", 80, TINTA, s0 + 0.3), ("erro", "g", 74, ERRADO, s0 + 0.45), ("mais", "i", 80, TINTA, s0 + 0.6), ("comum:", "i", 80, TINTA, s0 + 0.75),
                     ("trocar", "g", 74, ERRADO, a_), ("as", "g", 74, ERRADO, a_ + 0.15), ("palavras", "g", 74, ERRADO, a_ + 0.3)], W / 2, 180, "center")
        v = C["s15.b"]
        linha(c, t, [("54", "g", 130, TINTA, v), ("é", "i", 110, TINTA, v + 0.2), ("divisor", "g", 130, ERRADO, v + 0.35), ("de", "i", 110, TINTA, v + 0.6), ("6", "g", 130, TINTA, v + 0.75)], W / 2, 390, "center")
        n = C["s15.c"]
        if t >= n:
            E.risco(c, 500, 350, 1420, 350, t, n, largura=10)
        p = ep(t, n, 0.5)
        bloco(c, BX, 470, BW * p, 110, 16, E.COR, 1.0 if p > 0 else 0)
        if p > 0.6:
            E.escreve(c, "54", BX + 34, 548, 72, "g", BR, ep(t, n + 0.3, 0.3))
        q = ep(t, n + 0.3, 0.4)
        bloco(c, BX, 620, BW / 9, 110, 16, TINTA, q, 5)
        centro(c, "6", BX + BW / 18, 698, 72, "g", TINTA, q)
        E.frase(c, t, n + 0.3, [("54", "g", 84), ("não", "g", 84, ERRADO), ("cabe", "i", 90), ("dentro", "i", 90), ("de", "i", 90), ("6", "g", 84)], W / 2, 850, "center", passo=0.13)
        E.frase(c, t, lerp(n, C["s15.end"], 0.72), [("é", "i", 90), ("o", "i", 90), ("contrário", "g", 84, CERTO)], W / 2, 970, "center", passo=0.14)
    E.saida(c, t, C["s16"] - 0.1, troca)

    if t >= C["s16"]:
        E.frase(c, t, C["s16"] + 0.25, [("para", "i", 80), ("não", "i", 80), ("confundir", "g", 74, COR)], W / 2, 160, "center", passo=0.14)
        x, w, n = 740, 1044, 9
        a_ = C["s16.a"]
        linha(c, t, [("múltiplo", "g", 88, COR, a_)], XE, 330)
        E.frase(c, t, a_ + 0.3, [("é", "i", 72), ("o", "i", 72), ("grande", "g", 66)], XE, 415, passo=0.12)
        p = ep(t, a_ + 0.2, 0.5)
        E.chocolate(c, x, 270, w, 120, n, a=p, cortes=ep(t, C["s16.b"], 0.8))
        E.foco(c, t, a_ + 0.3, 0.4, lambda q: E.escreve(c, "54", x - 130, 356, 84, "g", TINTA, q))
        b_ = C["s16.b"]
        linha(c, t, [("divisor", "g", 88, COR, b_)], XE, 590)
        E.frase(c, t, b_ + 0.3, [("é", "i", 72), ("o", "i", 72), ("pequeno", "g", 66)], XE, 675, passo=0.12)
        # o pedaço de 6 passa pela barra do 54: cabe 9 vezes, certinho
        lp = w / n
        k = M.clamp(prog(t, b_ + 0.4, 1.5)) * n
        for i in range(n):
            p = M.clamp(k - i)
            if p > 0:
                E.tablete(c, x + i * lp, 270, lp, 120, E.COR, 1.0, lerp(0.6, 1.0, ease_back(p)))
        p = ep(t, b_ + 0.2, 0.4)
        if p > 0:
            E.tablete(c, x, 500, lp, 120, E.COR, p)
            centro(c, "6", x + lp / 2, 582, 72, "g", BR, p)
            E.chave(c, x, x + lp, 472, TINTA2, p, -20)
        E.frase(c, t, b_ + 0.7, [("cabe", "i", 72), ("certinho", "g", 66, CERTO)], x + lp + 40, 580, passo=0.14)
        for y, n1, mio, n2, ti in ((830, "6", "é divisor de", "54", C["s16.c"]), (945, "54", "é múltiplo de", "6", C["s16.d"])):
            linha(c, t, [(n1, "g", 96, TINTA, ti), (mio, "g", 96, COR, ti + 0.2), (n2, "g", 96, TINTA, ti + 0.6)], W / 2, y, "center")


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def parar():
        s0 = C["s17"]
        E.frase(c, t, s0 + 0.3, [("agora,", "i", 90, CLARO), ("o", "i", 90, CLARO), ("atalho", "i", 90, CLARO)], W / 2, 180, "center")
        E.frase(c, t, C["s17.a"], [("pare", "g", 84, BR), ("quando", "i", 90, BR), ("os", "i", 90, BR), ("pares", "g", 84, BR), ("se", "i", 90, BR), ("encontrarem", "i", 90, BR)], W / 2, 300, "center", passo=0.16)
        # uma tira com os números de 1 a 36: só os seis primeiros foram testados
        na, nb = lerp(C["s17.a"], C["s17.b"], 0.5), C["s17.b"]
        for i in range(36):
            x = 134 + i * 46
            ligado = i < 6 and t >= lerp(na, nb, i / 6)
            bloco(c, x, 470, 36, 110, 8, CLARO if ligado else E.COR, 1.0 if ligado else 0.5 * ep(t, na - 0.3, 0.4))
        E.foco(c, t, na - 0.2, 0.4, lambda a: (centro(c, "1", 152, 450, 60, "g", CLARO, a), centro(c, "36", 1762, 450, 60, "g", CLARO, a)))
        E.frase(c, t, na, [("você", "i", 72, CLARO), ("não", "i", 72, CLARO), ("precisou", "i", 72, CLARO), ("testar", "i", 72, CLARO), ("até", "i", 72, CLARO), ("36", "g", 66, BR)], W / 2, 710, "center", passo=0.13)
        if t >= nb:
            M.line(c, 400, 450, 400, 600, ERRADO, 1.0, 10, progress=ep(t, nb, 0.3))
            centro(c, "6", 382, 450, 60, "g", BR, ep(t, nb, 0.3))
        linha(c, t, [("parou", "g", 120, BR, nb), ("no", "i", 110, CLARO, nb + 0.2), ("6", "g", 130, CLARO, nb + 0.35)], W / 2, 880, "center")
    E.saida(c, t, C["s18"] - 0.1, parar)

    def porque():
        s0, xs, y0, dy = C["s18"], (240, 370, 520), 300, 128
        nomes = ((1, 36), (2, 18), (3, 12), (4, 9), (6, 6))
        a_, b_, c_ = C["s18.a"], C["s18.b"], C["s18.c"]
        for i, (u, v) in enumerate(nomes):
            y = y0 + i * dy
            cor = CLARO if t >= a_ + i * 0.2 else BR
            cor2 = CLARO if t >= b_ + i * 0.2 else BR
            E.foco(c, t, s0 + 0.2 + i * 0.1, 0.4, lambda q, u=u, y=y, cor=cor: centro(c, str(u), xs[0], y, 100, "g", cor, q))
            E.foco(c, t, s0 + 0.25 + i * 0.1, 0.4, lambda q, y=y: centro(c, "×", xs[1], y, 80, "b", CINZA, q))
            E.foco(c, t, s0 + 0.3 + i * 0.1, 0.4, lambda q, v=v, y=y, cor2=cor2: centro(c, str(v), xs[2], y, 100, "g", cor2, q))
        E.foco(c, t, a_, 0.4, lambda q: E.pilula(c, "sobe", xs[0], 165, 56, estilo="g", fundo=E.COR, cor=BR, a=q))
        E.foco(c, t, b_, 0.4, lambda q: E.pilula(c, "desce", xs[2], 165, 56, estilo="g", fundo=E.COR, cor=BR, a=q))
        p = ep(t, lerp(b_, c_, 0.5), 0.5)  # a última linha: onde as colunas se encontram
        E.caixa_pontilhada(c, 150, y0 + 4 * dy - 100, 470, 130, p, CLARO, prog_=p)
        X = 820
        E.frase(c, t, c_ - 0.4, [("todo", "i", 80, CLARO), ("divisor", "i", 80, CLARO), ("maior", "g", 74, BR)], X, 240, passo=0.14)
        E.frase(c, t, c_, [("já", "i", 80, CLARO), ("apareceu", "g", 74, BR), ("na", "i", 80, CLARO), ("direita", "g", 74, BR)], X, 340, passo=0.14)
        n = lerp(c_, C["s18.end"], 0.42)
        E.frase(c, t, n, [("testar", "i", 90, CLARO), ("o", "i", 90, CLARO), ("9?", "g", 96, BR)], X, 560, passo=0.14)
        E.frase(c, t, n + 0.7, [("só", "i", 80, CLARO), ("repetiria", "i", 80, CLARO), ("o", "i", 80, CLARO), ("par", "i", 80, CLARO)], X, 680, passo=0.14)
        E.foco(c, t, n + 1.2, 0.5, lambda q: E.pilula(c, "4 × 9", X + 190, 820, 96, estilo="g", fundo=E.COR, cor=BR, a=q))
        q = ep(t, n + 0.7, 0.4)  # marca o mesmo par na tabela
        E.caixa_pontilhada(c, 150, y0 + 3 * dy - 100, 470, 125, q, CLARO, prog_=q)
    if t >= C["s18"]:
        E.saida(c, t, C["s19"] - 0.1, porque)

    if t >= C["s19"]:
        s0 = C["s19"]
        E.frase(c, t, s0 + 0.25, [("quando", "i", 96, CLARO), ("não", "g", 90, BR), ("compensa?", "g", 90, BR)], W / 2, 200, "center", passo=0.14)
        a_, b_, c_ = C["s19.a"], C["s19.b"], C["s19.c"]
        E.foco(c, t, a_, 0.5, lambda q: num_bola(c, "1", 220, 390, 56, 64, q, E.COR, BR))
        E.frase(c, t, a_ + 0.1, [("a", "i", 76, CLARO), ("pergunta", "i", 76, CLARO), ("é", "i", 76, CLARO), ("só", "i", 76, CLARO), ("se", "i", 76, CLARO), ("um", "i", 76, CLARO), ("divide", "i", 76, CLARO), ("o", "i", 76, CLARO), ("outro?", "i", 76, CLARO)], 310, 400, passo=0.1)
        E.frase(c, t, b_, [("faça", "g", 72, BR), ("a", "g", 72, BR), ("divisão", "g", 72, BR), ("e", "g", 72, BR), ("pronto", "g", 72, BR)], 310, 500, passo=0.14)
        E.foco(c, t, c_, 0.5, lambda q: num_bola(c, "2", 220, 690, 56, 64, q, E.COR, BR))
        E.frase(c, t, c_ + 0.1, [("números", "i", 76, CLARO), ("muito", "i", 76, CLARO), ("grandes?", "i", 76, CLARO)], 310, 700, passo=0.14)
        E.frase(c, t, lerp(c_, C["s19.end"], 0.55), [("regras", "g", 72, BR), ("mais", "g", 72, BR), ("rápidas", "g", 72, BR)], 310, 800, passo=0.14)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    s0 = C["s20"]
    E.frase(c, t, s0 + 0.3, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 200)
    a_ = C["s20.a"]
    E.frase(c, t, a_, [("liste,", "i", 110), ("em", "i", 110), ("pares,", "g", 104, COR)], XE, 400, passo=0.15)
    E.frase(c, t, lerp(a_, C["s20.end"], 0.3), [("todos", "i", 110), ("os", "i", 110)], XE, 560, passo=0.15)
    E.frase(c, t, lerp(a_, C["s20.end"], 0.45), [("divisores", "g", 130, COR)], XE, 700)
    linha(c, t, [("de", "i", 130, TINTA, lerp(a_, C["s20.end"], 0.65)), ("28", "g", 170, TINTA, lerp(a_, C["s20.end"], 0.72))], XE, 890)
    relogio(c, t, C["s21.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    xs, y0, dy, s = (260, 370, 510), 225, 112, 84
    a_, b_, c_, d_ = C["s22.a"], C["s22.b"], C["s22.c"], C["s22.d"]
    a2, b2, c2, d2 = C["s23.a"], C["s23.b"], C["s23.c"], C["s23.d"]
    par(c, t, a_, 1, 28, y0, xs, s, COR, TINTA)
    par(c, t, b_, 2, 14, y0 + dy, xs, s, COR, TINTA)
    sem_par(c, t, lerp(b_, c_, 0.6), c_, 3, "resto", y0 + 2 * dy, xs, s)
    par(c, t, d_, 4, 7, y0 + 3 * dy, xs, s, COR, TINTA)
    sem_par(c, t, a2 - 0.5, a2, 5, "resto", y0 + 4 * dy, xs, s)
    sem_par(c, t, a2 - 0.3, a2 + 0.2, 6, "resto", y0 + 5 * dy, xs, s)
    # o 7 já está na coluna da direita: pare
    q = ep(t, b2, 0.4)
    E.caixa_pontilhada(c, xs[2] - 95, y0 + 3 * dy - 90, 190, 118, q, CERTO, prog_=q)
    E.foco(c, t, lerp(a2, b2, 0.55), 0.4, lambda q: centro(c, "7", xs[0], y0 + 6 * dy, s, "g", CERTO, q))
    E.foco(c, t, b2, 0.4, lambda q: E.escreve(c, "já apareceu: pare", xs[1] - 30, y0 + 6 * dy - 4, 62, "b", CERTO, q))

    X = 1050

    def subir():  # enquanto testa, a pista de que os pares vêm do 1 para cima
        E.frase(c, t, C["s22"] + 0.3, [("divisores", "i", 90), ("de", "i", 90), ("28", "g", 96, COR)], X, 340, passo=0.14)
        E.frase(c, t, C["s22"] + 0.9, [("do", "i", 90), ("1", "g", 96, COR), ("para", "i", 90), ("cima", "i", 90)], X, 470, passo=0.14)
        E.frase(c, t, lerp(b_, c_, 0.5), [("resto?", "i", 90), ("não", "g", 84, ERRADO), ("serve", "g", 84, ERRADO)], X, 680, passo=0.14)
    E.saida(c, t, c2 - 0.7, subir)
    E.frase(c, t, c2 - 0.5, [("em", "i", 84), ("ordem", "g", 78, COR)], X, 250, passo=0.14)
    for i, n in enumerate((1, 2, 4, 7, 14, 28)):
        bola_entra(c, t, lerp(c2, d2, i / 6.5), str(n), X + 90 + (i % 3) * 230, 400 + (i // 3) * 220, 96, 84)
    linha(c, t, [("6", "g", 150, COR, d2), ("divisores", "g", 130, TINTA, d2 + 0.2)], X, 880)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s24"] + 0.25, [("resumindo", "i", 96, COR)], W / 2, 200, "center")
        y = 390
        E.foco(c, t, C["s24.a"], 0.5, lambda a: num_bola(c, "1", 220, y - 28, 56, 64, a))
        E.frase(c, t, C["s24.a"] + 0.1, [("divisão", "i", 84), ("sem", "i", 84), ("resto:", "i", 84)], 310, y, passo=0.14)
        linha(c, t, [("um", "i", 84, TINTA, C["s24.b"] - 0.2), ("é", "i", 84, TINTA, C["s24.b"] - 0.1), ("múltiplo,", "g", 80, COR, C["s24.b"]),
                     ("o", "i", 84, TINTA, lerp(C["s24.b"], C["s24.c"], 0.6)), ("outro", "i", 84, TINTA, lerp(C["s24.b"], C["s24.c"], 0.8)), ("é", "i", 84, TINTA, lerp(C["s24.b"], C["s24.c"], 0.9)), ("divisor", "g", 80, COR, C["s24.c"])], 310, y + 120)
        y2 = 750
        v = C["s24.d"]
        E.foco(c, t, v - 0.3, 0.5, lambda a: num_bola(c, "2", 220, y2 - 28, 56, 64, a))
        E.frase(c, t, v - 0.2, [("para", "i", 84), ("listar", "i", 84), ("todos:", "i", 84)], 310, y2, passo=0.1)
        linha(c, t, [("use", "i", 84, TINTA, v), ("pares", "g", 80, COR, v + 0.15), ("e", "i", 84, TINTA, v + 0.4), ("pare", "g", 80, COR, v + 0.55), ("quando", "i", 84, TINTA, v + 0.75), ("se", "i", 84, TINTA, v + 0.95), ("encontrarem", "i", 84, TINTA, v + 1.05)], 310, y2 + 120)
    E.saida(c, t, C["s25"] - 0.1, resumo)
    if t < C["s25"]:
        return
    s0 = C["s25"]
    E.frase(c, t, s0 + 0.5, [("próxima", "i", 84), ("aula", "i", 84)], XE, 280)
    E.frase(c, t, C["s25.a"], [("regras", "g", 140, COR), ("de", "i", 130)], XE, 430)
    E.frase(c, t, C["s25.a"] + 0.5, [("divisibilidade", "g", 124, COR)], XE, 570)
    E.frase(c, t, lerp(C["s25.a"], C["s25.b"], 0.3), [("saber", "i", 76), ("sem", "i", 76), ("fazer", "i", 76), ("a", "i", 76), ("conta", "i", 76)], XE, 700, passo=0.16)
    E.foco(c, t, C["s25.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 330, 76, estilo="g", fundo=E.COR, cor=E.SOBRE, a=a))
    p = ease_io(prog(t, C["s25.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1740, 1600, p), lerp(650, 375, p), ep(t, C["s25.b"] + 0.2, 0.4), TINTA)
    E.frase(c, t, C["s25.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 900, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, multiplo=b_multiplo, divisor=b_divisor, pares=b_pares, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
