"""Visual — Estudativo · MAT-POT-015: praticando notação científica.
Aula de prática: quatro situações, com selo de progresso e relógio de pausa. Peças locais: Sol e Terra (desenho abstrato), raio de luz
com cronômetro, fio com fila de bactérias, pílula com fórmula. Todo instante vem de C[...]: entre dois cues, lerp(C[a], C[b], f)."""
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-015_praticando_notacao_cientifica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "fim"))
BR = "#FFFFFF"
AMARELO = "#F7B500"
assert 150000000 / 300000 == 500 and 1.5 / 3 == 0.5 and 8 - 5 == 3 and 8 * 60 == 480 and 500 - 480 == 20
assert 8 / 2 == 4 and -5 - (-6) == 1 and 4 * 10 == 40 and 8 * 10 ** -5 < 1 * 10 ** -4
assert 2.4 * 10 ** 6 + 6 * 10 ** 5 == 3 * 10 ** 6 and 15 / 3 == 5 and 7 - 5 == 2
assert 365 * 24 * 3600 == 31536000 and 3.15 < 3.1536 < 3.16


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def cen(c, t, t0, s, cx, y, size, cor=None, est="g"):
    E.foco(c, t, t0, 0.5, lambda a: centro(c, s, cx, y, size, est, cor or TINTA, a))


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def selo(c, t, t0, n):
    """situação n de 4, com quatro pontos de progresso"""
    s = f"situação {n} de 4"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 100, 46, estilo="b", a=a, cor=E.SOBRE)
        for i in range(4):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 100, 15, a=a)
            else:
                c.drawCircle(x, 100, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def sol(c, cx, cy, r, a=1.0):
    """o Sol, abstrato: esfera amarela com halo"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 1.7, [M.hexc(AMARELO, 0.45 * a), M.hexc(AMARELO, 0.0)], [0.0, 1.0]))
    c.drawCircle(cx, cy, r * 1.7, p)
    E.bola(c, cx, cy, r, AMARELO, a)


def terrinha(c, cx, cy, r, a=1.0):
    """a Terra, abstrata: esfera da cor da matéria com manchas claras"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, E.COR, a)
    for dx, dy, q in ((-0.3, -0.25, 0.3), (0.32, 0.22, 0.24)):
        c.drawCircle(cx + dx * r, cy + dy * r, q * r, M.paint(E.CLARO, 0.55 * a))


def raio(c, x0, x1, y, p, a=1.0):
    """o raio de luz: um traço amarelo que sai do Sol e avança até p (0..1)"""
    if a <= 0 or p <= 0:
        return
    xp = lerp(x0, x1, p)
    M.line(c, x0, y, xp, y, AMARELO, a, 10)
    c.drawCircle(xp, y, 14, M.paint(AMARELO, a))


def cronometro(c, cx, cy, r, f, s, a=1.0, size=None):
    """cronômetro: aro que enche (f = 0..1) e o tempo no meio"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint(E.VAZIO, a))
    c.drawCircle(cx, cy, r, M.paint(FIO, a, stroke=10))
    E.arco(c, cx, cy, r, -90, 360 * f, E.COR, 10, a)
    M.rrect(c, cx - 14, cy - r - 30, 28, 22, 5, TINTA, a)
    size = size or r * 0.5
    centro(c, s, cx, cy + size * 0.35, size, "g", TINTA, a)


def bacteria(c, x, y, w, h, a=1.0):
    """bactéria: cápsula verde deitada"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, h / 2, CERTO, a)
    M.line(c, x + h / 2, y + h * 0.32, x + w - h / 2, y + h * 0.32, "#FFFFFF", 0.4 * a, 3)


def fio(c, x, y, w, h, a=1.0):
    """o fio de cabelo: uma faixa escura. A largura do fio é a medida que as bactérias cobrem"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 8, TINTA, a)


def conserta2(c, t, x, y, s, ta, tj, tc, e0, e1):
    """0,5 × 10^e0: a vírgula salta em tj, o zero à esquerda some, e o expoente desce em tc"""
    cl = E.casa(s)
    k = s / 170
    tl = tj + 0.8
    dx = cl * ease_io(prog(t, tl + 0.1, 0.5))
    xf = x + 2 * cl + 44 * k - dx
    wf = E.formula(c, "× 10", 0, 0, s, a=0)
    xe = xf + wf
    if t < tl:
        E.foco(c, t, ta, 0.5, lambda a: E.anda(c, t, "05", 1, [(tj, 2)], x, y, s))
    else:
        E._digito(c, "5", x + 1.5 * cl - dx, y, s, "g", TINTA, 1.0)
        E.saida(c, t, tl, lambda: (E._digito(c, "0", x + 0.5 * cl, y, s, "g", TINTA, 1.0), E._virgula(c, x + 2 * cl, y, s, COR, 1.0)))
    E.foco(c, t, ta, 0.5, lambda a: (E.formula(c, "× 10", xf, y, s, a=a), E.formula(c, f"^{e0}", xe, y, s, a=a)))
    E.corta(c, t, tc, xe + 30 * k, y - 106 * k, 76 * k)
    E.foco(c, t, tc + 0.3, 0.4, lambda a: E.formula(c, f"^{e1}", xe + 66 * k, y, s, cor=COR, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]
    E.frase(c, t, ka, ps("quantos minutos a", "i", 88) + [("luz do Sol", "g", 88, COR)] + ps("leva até você?", "i", 88), W / 2, 170, "center", 0.11)
    E.foco(c, t, ka, 0.6, lambda a: sol(c, 300, 390, 110, a))
    E.foco(c, t, ka + 0.5, 0.6, lambda a: terrinha(c, 1600, 390, 44, a))
    raio(c, 410, 1556, 390, ease_io(prog(t, ka + 0.8, kb - ka - 0.8)), ep(t, ka + 0.8, 0.3))
    E.frase(c, t, kb, [("4", "g", 170, COR), ("situações", "g", 130, COR)] + ps("criadas para esta aula", "i", 72), W / 2, 700, "center", 0.16)
    for i, (s, cx) in enumerate((("pause", 620), ("resolva", 1160))):
        E.foco(c, t, kc + i * 0.5, 0.5, lambda p, i=i, s=s, cx=cx: (E.bola(c, cx - 170, 870, 52, a=p), centro(c, str(i + 1), cx - 170, 893, 60, "g", E.SOBRE, p),
                                                                    E.escreve(c, s, cx - 100, 898, 88, "g", TINTA, p)))
    E.frase(c, t, lerp(kc, C["s01.end"], 0.55), ps("antes de ver a resposta", "i", 72), W / 2, 1000, "center", 0.11)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 100), XE, 340, passo=0.14)
    E.frase(c, t, C["s02"] + 0.9, [("quatro", "g", 130, COR)], XE, 490)
    E.frase(c, t, C["s02"] + 1.2, ps("ferramentas", "i", 100), XE, 610)
    x, w = 830, 900
    for i, (k, s) in enumerate((("s02.a", "escrever em notação científica"), ("s02.b", "multiplicar e dividir"), ("s02.c", "somar com expoente igual"), ("s02.d", "achar a ordem de grandeza"))):
        y = 170 + i * 165
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 134, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(s, "g", 58, COR)], x + 40, y + 88)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.45), ps("travou?", "i", 62, COR), XE, 730, passo=0.13)
    E.frase(c, t, lerp(C["s02.d"], C["s02.end"], 0.6), ps("procure a aula no canal", "i", 60), XE, 810, passo=0.1)


# ---------------- situação 1 ----------------
def b_questao1(c, t, C, b):
    ka, kb, kc, kd = C["s03.a"], C["s03.b"], C["s03.c"], C["s03.d"]
    selo(c, t, ka, 1)
    E.frase(c, t, kb - 0.4, ps("o Sol está a cerca de", "i", 76), XE, 240, passo=0.1)
    E.frase(c, t, kb + 0.2, [("150 milhões de km", "g", 96, COR)], XE, 350)
    E.frase(c, t, kc - 0.5, ps("a luz percorre cerca de", "i", 76), XE, 480, passo=0.1)
    E.frase(c, t, kc + 0.2, [("300 mil km", "g", 96, COR)] + ps("por segundo", "i", 76), XE, 590, passo=0.12)
    E.frase(c, t, kd, ps("em quantos segundos a luz do Sol", "i", 80) + [("chega aqui?", "g", 80, COR)], W / 2, 740, "center", 0.1)
    E.foco(c, t, kb, 0.6, lambda a: sol(c, 300, 910, 72, a))
    E.foco(c, t, kb + 0.4, 0.6, lambda a: terrinha(c, 1600, 910, 30, a))
    if t >= kc:
        q = ep(t, kc, 0.5)
        p = M.paint(TINTA2, q, stroke=4)
        p.setPathEffect(skia.DashPathEffect.Make([16, 14], 0))
        c.drawLine(390, 910, 1560, 910, p)
    E.relogio(c, t, C["s04.a"], 1540, 330, 150)


def b_resposta1(c, t, C, b):
    selo(c, t, C["s05"], 1)

    def monta():
        ka, kb, kc = C["s05.a"], C["s05.b"], C["s05.c"]
        E.frase(c, t, C["s05"] + 0.3, ps("quantas vezes 300 mil cabe na distância?", "i", 80), W / 2, 280, "center", 0.1)
        E.foco(c, t, ka, 0.5, lambda a: E.pilula(c, "é uma divisão", W / 2, 440, 96, "g", a=a, cor=E.SOBRE))
        E.cientifica(c, t, kb, "1,5", 8, 520, 730, 140, align="center")
        fcen(c, t, kc - 0.1, "÷", 960, 730, 130, COR)
        E.cientifica(c, t, kc, "3", 5, 1370, 730, 140, align="center")
    E.saida(c, t, C["s06"] - 0.1, monta)

    def conta():
        ka, kb, kc, kd = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        fcen(c, t, ka, "1,5 ÷ 3 = 0,5", 540, 310, 120)
        fcen(c, t, kb, "8 − 5 = 3", 1360, 310, 120)
        fcen(c, t, lerp(kb, kc, 0.6), "10^3", 1360, 470, 120, COR)
        fcen(c, t, kc, "0,5 × 10^3", W / 2 - 60, 690, 170)
        E.foco(c, t, kd + 0.2, 0.5, lambda a: E.selo(c, 1420, 640, 62, False, a))
        E.frase(c, t, kd, [("0,5", "g", 92, ERRADO)] + ps("fica abaixo de", "i", 88) + [("1", "g", 92, ERRADO)], W / 2, 900, "center", 0.14)
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, conta)

    if t >= C["s07"]:
        ka, kb, kc, kd = C["s07.a"], C["s07.b"], C["s07.c"], C["s07.d"]
        tm = lerp(kc, kd, 0.42)

        def forma():
            conserta2(c, t, 470, 400, 170, C["s07"], lerp(C["s07"], ka, 0.45), kb + 0.9, 3, 2)
            E.frase(c, t, lerp(C["s07"], ka, 0.1), ps("a vírgula anda uma casa para a", "i", 70) + [("direita", "g", 70, COR)], W / 2, 190, "center", 0.09)
            E.frase(c, t, kb, ps("frente 10 vezes maior,", "i", 80) + [("o expoente desce", "g", 76, COR)], W / 2, 580, "center", 0.11)
        E.saida(c, t, kc - 0.1, forma)
        E.cientifica(c, t, kc, "5", 2, 660, 330, 150, cor=COR, align="center")
        E.frase(c, t, kc + 0.7, [("= 500 segundos", "g", 92, COR)], 1300, 330, "center")
        E.frase(c, t, tm, ps("1 minuto tem 60 segundos,", "i", 70) + [("8 × 60 = 480", "g", 72)], W / 2, 480, "center", 0.1)
        x0, x1, y = 400, 1540, 620
        E.foco(c, t, kc, 0.6, lambda a: sol(c, 300, y, 90, a))
        E.foco(c, t, kc + 0.2, 0.6, lambda a: terrinha(c, 1610, y, 42, a))
        raio(c, x0, x1, y, ease_io(prog(t, kc + 0.3, kd - kc)), ep(t, kc + 0.3, 0.3))
        E.foco(c, t, kd, 0.5, lambda a: cronometro(c, 960, 850, 150, ease_io(prog(t, kd, 0.8)), "8 min 20 s", a, 52))


# ---------------- situação 2 ----------------
def b_questao2(c, t, C, b):
    ka, kb, kc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
    a9, b9 = C["s09.a"], C["s09.b"]
    selo(c, t, ka, 2)
    E.frase(c, t, ka + 0.2, ps("com duas perguntas", "i", 66), 800, 122, "left", 0.1)
    E.frase(c, t, kb - 0.6, ps("folha de papel:", "i", 72), XE, 280, passo=0.1)
    E.formula_em(c, t, kb, "1 × 10^{−4} m", XE + 480, 280, 96, cor=COR)
    E.frase(c, t, kc - 0.6, ps("fio de cabelo:", "i", 72), XE, 400, passo=0.1)
    E.formula_em(c, t, kc, "8 × 10^{−5} m", XE + 480, 400, 96, cor=COR)
    E.frase(c, t, kd, [("1.", "g", 84, COR)] + ps("qual é o", "i", 84) + [("mais fino?", "g", 84, COR)], XE, 530, passo=0.12)
    E.frase(c, t, a9 - 0.6, ps("bactéria comum:", "i", 72), XE, 680, passo=0.1)
    E.formula_em(c, t, a9, "2 × 10^{−6} m", XE + 480, 680, 96, cor=COR)
    E.frase(c, t, b9, [("2.", "g", 76, COR)] + ps("quantas", "i", 76) + [("bactérias em fila", "g", 76, COR)] + ps("cobrem a largura do fio?", "i", 76), XE, 810, passo=0.09)
    E.foco(c, t, b9 + 0.3, 0.5, lambda a: (fio(c, XE, 870, 1400, 44, a), bacteria(c, XE + 8, 926, 62, 28, a)))
    E.relogio(c, t, C["s10.a"], 1540, 340, 150)


def b_resposta2(c, t, C, b):
    selo(c, t, C["s11"], 2)
    fm = lambda v: str(v).replace("-", "−")

    def fino():
        ka, kb, kc, kd = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        E.frase(c, t, C["s11"] + 0.3, ps("8 parece maior que 1, mas", "i", 76), W / 2, 240, "center", 0.1)
        E.frase(c, t, ka, ps("quem decide primeiro é o", "i", 84) + [("expoente", "g", 84, COR)], W / 2, 350, "center", 0.11)
        vx = E.reta(c, t, kb, 440, 1480, 500, -6, -3, (-5, -4), fm, size=76, tm=(kb, kb + 0.2))
        E.frase(c, t, lerp(kb, kc, 0.3), ps("−4 está à direita:", "i", 72) + [("a folha é mais grossa", "g", 72, COR)], W / 2, 690, "center", 0.1)
        E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "o mais fino é o fio de cabelo", W / 2, 810, 80, "g", a=a, cor=E.SOBRE))
        E.frase(c, t, kd, ps("só compare a frente com", "i", 72) + [("expoentes iguais", "g", 72, COR)], W / 2, 960, "center", 0.1)
    E.saida(c, t, C["s12"] - 0.1, fino)
    if t >= C["s12"]:
        ka, kb, kc, kd, ke = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"], C["s12.e"]
        E.frase(c, t, C["s12"] + 0.2, ps("agora a divisão", "i", 66), 800, 122, "left", 0.1)
        fcen(c, t, ka, "8 ÷ 2 = 4", 460, 310, 110)
        fcen(c, t, kb, "−5 − (−6)", 1300, 310, 110)
        E.frase(c, t, lerp(kb, kc, 0.55), ps("tirar um negativo é somar", "i", 66), 1300, 420, "center", 0.1)
        fcen(c, t, kc, "−5 + 6 = 1", 1300, 540, 110, COR)
        E.cientifica(c, t, kd, "4", 1, 460, 540, 130, cor=COR, align="center")
        fx, fw = XE, 1500
        E.foco(c, t, kd, 0.5, lambda a: fio(c, fx, 650, fw, 40, a))
        n = 40
        w = fw / n
        for i in range(n):
            E.foco(c, t, ke + i * 0.03, 0.2, lambda a, i=i: bacteria(c, fx + i * w + 2, 700, w - 4, 30, a), blur=4, sobe=-10)
        E.frase(c, t, ke, ps("cerca de", "i", 84) + [("40 bactérias", "g", 96, CERTO)], W / 2, 880, "center", 0.12)


# ---------------- situação 3 ----------------
def b_questao3(c, t, C, b):
    ka, kb, kc, kd = C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"]
    selo(c, t, ka, 3)
    E.frase(c, t, kb - 0.5, ps("uma cidade tem", "i", 76), XE, 280, passo=0.1)
    E.formula_em(c, t, kb, "2,4 × 10^6", XE, 400, 110, cor=COR)
    E.frase(c, t, kb + 1.1, ps("habitantes", "i", 72), XE + 520, 400, passo=0.1)
    E.frase(c, t, kc - 0.5, ps("a vizinha tem", "i", 76), XE, 540, passo=0.1)
    E.formula_em(c, t, kc, "6 × 10^5", XE, 660, 110, cor=COR)
    E.frase(c, t, kd, ps("quantos habitantes têm", "i", 84) + [("juntas?", "g", 84, COR)], XE, 830, passo=0.11)
    E.frase(c, t, lerp(kd, C["s13.end"], 0.55), ps("em notação científica", "i", 76), XE, 940, passo=0.1)
    E.relogio(c, t, C["s14.a"], 1520, 340, 170)


def b_resposta3(c, t, C, b):
    ka, kb, kc, kd = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"]
    selo(c, t, C["s15"], 3)
    te = lerp(ka, kb, 0.22)
    E.frase(c, t, C["s15"] + 0.4, ps("soma pede o", "i", 72) + [("mesmo expoente", "g", 68, COR)], 800, 122, "left", 0.1)
    fcen(c, t, ka, "6 × 10^5", 500, 300, 110)
    if t >= te:
        q = ep(t, te, 0.5)
        M.arrow(c, 780, 262, 900, 262, COR, q, 7, 22, q)
    fcen(c, t, te + 0.3, "0,6 × 10^6", 1240, 300, 110, COR)
    fcen(c, t, kb, "2,4 + 0,6 = 3", W / 2, 470, 110)

    def certo():
        E.cientifica(c, t, kc, "3", 6, 590, 690, 150, cor=CERTO, align="center")
        E.foco(c, t, kc + 0.8, 0.5, lambda a: E.selo(c, 900, 640, 54, True, a))
        E.frase(c, t, lerp(kc, kd, 0.6), [("3 milhões", "g", 84, CERTO)] + ps("de habitantes", "i", 72), 990, 680, "left", 0.11)
    certo()
    E.cientifica(c, t, kd, "8,4", 6, 500, 880, 110, cor=ERRADO, align="center")
    E.foco(c, t, kd + 0.4, 0.5, lambda a: E.selo(c, 860, 845, 46, False, a))
    E.frase(c, t, lerp(kd, C["s15.end"], 0.3), ps("mais de 8 milhões?", "i", 70, ERRADO), 930, 860, "left", 0.1)
    E.frase(c, t, lerp(kd, C["s15.end"], 0.6), ps("nenhuma cidade chega a 2 milhões e meio", "i", 66), W / 2, 985, "center", 0.09)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    ka, kb, kc = C["s16.a"], C["s16.b"], C["s16.c"]
    f = lambda q: lerp(kb, kc, q)
    E.frase(c, t, C["s16"] + 0.1, ps("o atalho da divisão da luz do Sol", "i", 72, CLARO), W / 2, 130, "center", 0.1)
    E.frase(c, t, ka, ps("ande a vírgula", "g", 100, BR) + ps("antes de dividir", "i", 100, CLARO), W / 2, 260, "center", 0.14)
    fcen(c, t, lerp(ka, kb, 0.5), "1,5 × 10^8 =", 660, 430, 120, BR)
    fcen(c, t, kb, "15 × 10^7", 1270, 430, 120, CLARO)
    fcen(c, t, f(0.14), "15 ÷ 3 = 5", 540, 590, 100, BR)
    fcen(c, t, f(0.28), "7 − 5 = 2", 1380, 590, 100, BR)
    E.frase(c, t, f(0.44), [("=", "g", 110, CLARO)], 550, 750)
    E.cientifica(c, t, f(0.45), "5", 2, 870, 750, 130, cor=CLARO, align="center")
    E.frase(c, t, f(0.56), ps("sem ajuste no fim", "i", 76, CLARO), 1140, 745, "left", 0.1)
    if t < kc + 0.5:
        E.saida(c, t, kc - 0.1, lambda: E.frase(c, t, f(0.69), ps("a frente ficou", "i", 66, CLARO) + [("10 vezes maior,", "b", 62, BR)] + ps("a potência,", "i", 66, CLARO) + [("10 vezes menor", "b", 62, BR)], W / 2, 900, "center", 0.09))
    E.foco(c, t, kc, 0.5, lambda a: E.selo(c, 260, 900, 56, False, a))
    E.frase(c, t, kc + 0.1, ps("não compensa se o primeiro da frente", "i", 62, CLARO), 340, 870, "left", 0.07)
    E.frase(c, t, lerp(kc, C["s16.end"], 0.4), ps("já é", "i", 62, CLARO) + [("maior que o segundo", "g", 60, BR)], 340, 960, "left", 0.08)
    E.frase(c, t, lerp(kc, C["s16.end"], 0.75), ps("aí,", "i", 72, CLARO) + [("divida direto", "g", 68, BR)], 1230, 960, "left", 0.1)


# ---------------- situação 4 ----------------
def b_questao4(c, t, C, b):
    ka, kb, kc, kd = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    selo(c, t, ka, 4)
    E.frase(c, t, ka + 0.2, ps("a última", "i", 66), 800, 122, "left", 0.1)
    E.frase(c, t, kb - 0.3, ps("um ano de", "i", 80) + [("365 dias", "g", 100, COR)] + ps("tem", "i", 80), XE, 320, passo=0.12)
    E.frase(c, t, kc, [("31.536.000", "g", 140, COR)], XE, 500)
    E.frase(c, t, lerp(kc, kd, 0.55), ps("segundos", "i", 90), XE, 620, passo=0.1)
    E.frase(c, t, kd, ps("qual é a", "i", 84) + [("ordem de grandeza", "g", 84, COR)] + ps("desse número?", "i", 84), W / 2, 830, "center", 0.11)
    E.relogio(c, t, C["s18.a"], 1520, 330, 170)


def b_resposta4(c, t, C, b):
    ka, kb, kc, kd = C["s19.a"], C["s19.b"], C["s19.c"], C["s19.d"]
    selo(c, t, C["s19"], 4)
    fcen(c, t, ka, "≈ 3,15 × 10^7", W / 2, 300, 130)
    E.frase(c, t, kb, ps("começa com 3,1:", "i", 80) + [("compare com calma", "g", 80, COR)], W / 2, 440, "center", 0.11)
    fmt = lambda v: f"{v:.2f}".replace(".", ",")
    vx = E.reta(c, t, kc - 0.3, 500, 1420, 620, 3.12, 3.18, (3.15, 3.16), fmt, size=64, tm=(kc, kc + 0.2))
    E.foco(c, t, kc + 0.2, 0.5, lambda a: (c.drawCircle(vx(3.15), 620, 16, M.paint(E.COR, a)),))
    E.frase(c, t, lerp(kc, kd, 0.55), ps("não passa: o expoente fica", "i", 76), 620, 880, "center", 0.1)
    E.foco(c, t, kd, 0.5, lambda a: (E.bola(c, 1480, 840, 130, a=a), E.formula(c, "10^7", 1480, 885, 110, "g", E.SOBRE, a, "center")))
    E.frase(c, t, lerp(kd, C["s19.end"], 0.72), [("foi por pouco!", "g", 76, CERTO)], 620, 985, "center")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        for i, (k, s) in enumerate((("s20.a", "nas contas, cuide dos expoentes"), ("s20.b", "na soma, iguale antes"), ("s20.c", "confira a frente: de 1 até menos de 10"))):
            y = 390 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 74)], 350, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21.a"], ps("com esta prática, você", "i", 90), XE, 280, passo=0.12)
    E.frase(c, t, lerp(C["s21.a"], C["s21.b"], 0.35), [("fecha a trilha", "g", 140, COR)], XE, 440)
    E.frase(c, t, lerp(C["s21.a"], C["s21.b"], 0.6), ps("de potências e raízes", "i", 100), XE, 570, passo=0.14)
    E.foco(c, t, C["s21.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 720, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(970, 745, p), ep(t, C["s21.b"] + 0.2, 0.4))
    E.frase(c, t, C["s21.c"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
