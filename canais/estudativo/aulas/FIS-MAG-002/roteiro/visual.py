"""Visual — Estudativo · FIS-MAG-002: campo criado por corrente. Linguagem visual do Magnetismo: veja o visual.py da FIS-MAG-001.
Corrente = fio em tinta com setinhas laranja (F.corrente) e a letra i; campo B em tinta (linhas, símbolos saindo/entrando);
a mão direita em tom de pele com contorno em tinta. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-002_campo_criado_por_corrente.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fio", "simbolos", "valor", "espira", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
PELE, PELE2 = "#F4D3B8", "#E2B48F"

# todas as contas da aula (μ₀ = 4π·10⁻⁷; μ₀/2π = 2·10⁻⁷)
MU0 = 4 * math.pi * 1e-7
assert math.isclose(MU0 / (2 * math.pi), 2e-7)
assert math.isclose(MU0 * 10 / (2 * math.pi * 0.2), 1e-5)
assert math.isclose(2e-7 * 6 / 0.03, 4e-5) and math.isclose(2e-7 * 18 / 0.06, 6e-5)
assert 18 / 6 == 3 and 6 / 3 == 2 and 3 / 2 == 1.5 and math.isclose(4e-5 * 1.5, 6e-5)
# sentido: corrente para cima (+y); à direita (+x) o campo é ŷ × x̂ = −ẑ: entra na folha
assert (0 * 0 - 1 * 0, 0 * 1 - 0 * 0, 0 * 0 - 1 * 1)[2] == -1


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças do magnetismo (cópia da FIS-MAG-001 + novas) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def ang_tela(ux, uy):
    return math.degrees(math.atan2(-uy, ux))


def gira(t, t0, de, para, d=0.8):
    dif = (para - de + 180) % 360 - 180
    return de + dif * ease_io(prog(t, t0, d))


def bussola(c, cx, cy, r, ang, a=1.0, escuro=False):
    """bússola: caixa redonda e agulha; ang = para onde aponta o norte da agulha (graus da Física, 0 = direita)"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#1B1B22" if escuro else BR, a))
    c.drawCircle(cx, cy, r, M.paint(BR if escuro else TINTA, a, stroke=max(3, r * 0.08)))
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    nx, ny = -uy, ux
    L, wd = r * 0.8, r * 0.22
    for s, cor in ((1, E.COR), (-1, NEG)):
        p = skia.Path()
        p.moveTo(cx + ux * L * s, cy + uy * L * s); p.lineTo(cx + nx * wd, cy + ny * wd); p.lineTo(cx - nx * wd, cy - ny * wd); p.close()
        c.drawPath(p, M.paint(cor, a))
    c.drawCircle(cx, cy, r * 0.1, M.paint(TINTA if not escuro else BR, a))


def barra(c, cx, cy, w=360, h=110, a=1.0, ang=0.0, letras=True):
    """ímã em barra parado com o norte no sentido ang (graus da Física); letras sempre em pé"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(-ang)
    for lado, cor in ((1, E.COR), (-1, NEG)):
        x0 = 0 if lado > 0 else -w / 2
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, -h / 2), skia.Point(0, h / 2)],
                                                   [M.hexc(E.mix(cor, BR, 0.2), a), M.hexc(E.mix(cor, "#000000", 0.2), a)]))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, -h / 2, w / 2, h), 10, 10), p)
    c.restore()
    if letras:
        ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
        sz = min(h, w / 2) * 0.55
        E._meio(c, "N", cx + ux * w / 4, cy + uy * w / 4, sz, "g", BR, a)
        E._meio(c, "S", cx - ux * w / 4, cy - uy * w / 4, sz, "g", BR, a)


def simbolo_campo(c, cx, cy, r, sai=True, a=1.0, cor=None, escuro=False):
    """campo furando a folha: ponto no círculo = saindo; xis no círculo = entrando"""
    if a <= 0:
        return
    cor = cor or (BR if escuro else TINTA)
    c.drawCircle(cx, cy, r, M.paint(cor, a, stroke=max(3, r * 0.14)))
    if sai:
        c.drawCircle(cx, cy, r * 0.28, M.paint(cor, a))
    else:
        k = r * 0.62
        M.line(c, cx - k, cy - k, cx + k, cy + k, cor, a, max(3, r * 0.14))
        M.line(c, cx - k, cy + k, cx + k, cy - k, cor, a, max(3, r * 0.14))


def folha_campo(c, t, t0, x0, y0, cols, lins, passo, sai=True, r=20, cor=None, escuro=False, d=0.06):
    """grade de símbolos de campo que entram um a um a partir de t0"""
    for i in range(lins):
        for j in range(cols):
            k = i * cols + j
            E.foco(c, t, t0 + d * k, 0.35, lambda a, i=i, j=j: simbolo_campo(c, x0 + j * passo, y0 + i * passo, r, sai, a, cor, escuro), sobe=0)


def anel(c, cx, cy, rx, ry, a=1.0, cor=None, setas=True, frente=1, largura=5, t=0.0, gira_=0.0):
    """linha de campo circular vista em perspectiva (elipse) com setas; frente=1: a parte da frente (de baixo) aponta para a direita"""
    if a <= 0:
        return
    cor = cor or TINTA2
    c.drawOval(skia.Rect.MakeXYWH(cx - rx, cy - ry, 2 * rx, 2 * ry), M.paint(cor, a, stroke=largura))
    if setas:
        for k in range(2):
            g = math.pi / 2 + 0.75 + k * math.pi + gira_  # na frente, à esquerda, e atrás, à direita (longe do fio)
            x, y = cx + rx * math.cos(g), cy + ry * math.sin(g)
            tx, ty = -rx * math.sin(g) * -frente, ry * math.cos(g) * -frente
            n = math.hypot(tx, ty) or 1
            F._cabeca(c, x + tx / n * 12, y + ty / n * 12, tx / n, ty / n, 24, cor, a)


def punho(c, cx, cy, s, a=1.0, polegar=1):
    """mão direita fechada em volta de um fio vertical em cx; polegar=1 aponta para cima"""
    if a <= 0:
        return
    w, h = s * 1.0, s * 1.05
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, s * 0.28, PELE, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), s * 0.28, s * 0.28), M.paint(TINTA, a, stroke=4))
    for k in range(1, 4):  # vãos entre os dedos
        y = cy - h / 2 + h * k / 4
        M.line(c, cx - w / 2 + s * 0.12, y, cx + w / 2 - s * 0.3, y, PELE2, a, 4)
    # polegar
    tw, th = s * 0.3, s * 0.75
    x0 = cx + w / 2 - tw - s * 0.02
    y0 = cy - h / 2 - th * 0.75 if polegar > 0 else cy + h / 2 - th * 0.25
    M.rrect(c, x0, y0, tw, th, tw / 2, PELE, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, tw, th), tw / 2, tw / 2), M.paint(TINTA, a, stroke=4))


def bobina(c, x0, cy, w, ry, n, a=1.0, cor=None, frente_desce=True, t=0.0, t0=None):
    """solenoide de lado: n espiras (elipses) entre x0 e x0 + w; a parte da frente leva setinha para baixo"""
    if a <= 0:
        return
    cor = cor or TINTA
    passo = w / n
    for k in range(n):
        x = x0 + passo * (k + 0.5)
        c.drawOval(skia.Rect.MakeXYWH(x - passo * 0.32, cy - ry, passo * 0.64, 2 * ry), M.paint(cor, a * 0.45, stroke=5))
        p = skia.Path(); p.moveTo(x - passo * 0.32 + passo * 0.64 / 2 * 0, cy - ry)
        p.cubicTo(x + passo * 0.55, cy - ry * 0.6, x + passo * 0.55, cy + ry * 0.6, x, cy + ry)
        c.drawPath(p, M.paint(cor, a, stroke=7))
        if t0 is not None and t >= t0:
            q = ep(t, t0, 0.4)
            F._cabeca(c, x + passo * 0.4, cy + 8, 0, 1 if frente_desce else -1, 20, E.COR, q * a)


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas (o mesmo da FIS-CIN-001)"""
    E.frase(c, t, C[cena] + 0.2, ps("lembre", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def fio_v(c, t, t0, x, y0, y1, sobe=True, rot="i", a=1.0):
    """fio vertical em tinta com a corrente andando (para cima com sobe=True) e a letra i"""
    if t < t0:
        return
    M.line(c, x, y0, x, y1, TINTA, ep(t, t0, 0.4) * a, 8)
    pts = [(x, y1), (x, y0)] if sobe else [(x, y0), (x, y1)]
    F.corrente(c, t, t0 + 0.3, pts, fecha=False, a=a)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda a_: E.escreve(c, rot, x + 26, min(y0, y1) + 60, 64, "g", COR, a_ * a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        E.frase(c, t, C["s01.a"], [("1820", "g", 150, TINTA)], XE, 300)
        E.frase(c, t, C["s01.a"] + 0.6, ps("Oersted:", "i", 70) + ps("fio, bateria e bússola", "i", 70, TINTA2), XE, 420, passo=0.12)
        fx, by = 1350, 640
        ang = gira(t, C["s01.b"], 90, 180, 1.0)
        E.foco(c, t, C["s01.a"] + 0.5, 0.5, lambda a: bussola(c, fx, by, 170, ang, a))
        # o fio passa por cima da agulha; a pilha embaixo
        if t >= C["s01.a"] + 0.8:
            M.line(c, fx, 260, fx, 1000, TINTA, ep(t, C["s01.a"] + 0.8, 0.4), 9)
            F.corrente(c, t, C["s01.b"] - 0.3, [(fx, 1000), (fx, 260)], fecha=False)
        E.frase(c, t, C["s01.b"], ps("a agulha", "i", 80) + [("girou", "g", 80, COR)], XE, 600, passo=0.12)
        E.frase(c, t, C["s01.c"], [("corrente", "g", 90, COR), ("cria", "i", 90)], XE, 800)
        E.frase(c, t, C["s01.c"] + 0.5, [("campo", "g", 90, COR), ("magnético", "g", 90)], XE, 920)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.b", "sentido: mão direita"), ("s02.c", "fio, espira e bobina"))
    for i, (k, s) in enumerate(itens):
        y = 470 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def corr(a, x, y):
        E.formula(c, "i = f{Q}{Δt}", x - 30, y + 30, 70, "g", TINTA, a, "center")

    def bus(a, x, y):
        bussola(c, x - 80, y, 70, 0, a)
        F.seta(c, x + 10, y, x + 150, y, TINTA, a, 7)
        E.escreve(c, "B", x + 60, y - 30, 46, "g", TINTA, a)
    lembrete2(c, t, C, "s03", (("s03.b", "corrente:", "carga por segundo (A)"), ("s03.c", "N da bússola:", "sentido de B (T)")), (corr, bus))


# ---------------- o fio ----------------
def tabuleiro(c, cx, cy, fn, k=0.42):
    """desenha fn() num plano horizontal visto de cima e um pouco de frente"""
    c.save(); c.translate(cx, cy); c.scale(1, k)
    fn()
    c.restore()


def b_fio(c, t, C, b):
    cx, cy, R = 1260, 640, 330
    if t < C["s05"]:
        E.frase(c, t, C["s04"], ps("fio", "i", 90) + [("reto e comprido", "g", 84, COR)], XE, 220, passo=0.12)
        # o tabuleiro com as bússolas, visto de frente e de cima
        E.foco(c, t, C["s04.a"] - 0.6, 0.5, lambda a: tabuleiro(c, cx, cy, lambda: M.rrect(c, -560, -560, 1120, 1120, 40, "#ECE6DA", a)))
        n = 10
        for k in range(n):
            g = 2 * math.pi * k / n
            alvo = ang_tela(math.sin(g), -math.cos(g))  # tangente no sentido anti-horário (corrente subindo)
            ang = gira(t, C["s04.b"] + 0.06 * k, 90, alvo, 0.8)
            E.foco(c, t, C["s04.a"] + 0.08 * k, 0.4, lambda a, g=g, ang=ang: tabuleiro(c, cx, cy, lambda: bussola(c, R * math.cos(g), R * math.sin(g), 80, ang, a)), sobe=0)
        if t >= C["s04.c"]:
            for rr in (R * 0.55, R, R * 1.45):
                q = ep(t, C["s04.c"] + 0.2 * (rr / R), 0.5)
                anel(c, cx, cy, rr, rr * 0.42, q, TINTA2, rr != R)
        fio_v(c, t, C["s04.a"] - 0.6, cx, 300, 1040, True, None, 1.0) if t < C["s04.b"] else fio_v(c, t, C["s04.b"] - 0.3, cx, 300, 1040)
        E.frase(c, t, C["s04.b"], ps("as agulhas formam", "i", 60) + [("um círculo", "g", 60, COR)], XE, 340, passo=0.12)
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "linhas = círculos", XE + 230, 470, 50, "g", fundo=TINTA, a=a))
        return
    # a mão direita segura o fio
    E.frase(c, t, C["s05.a"], [("regra da", "i", 90), ("mão direita", "g", 90, COR)], XE, 220)
    fx, fy = 1300, 620
    fio_v(c, t, C["s05"], fx, 220, 1040, True, None)
    for rr, yy in ((300, fy - 260), (300, fy + 240)):
        E.foco(c, t, C["s05.c"], 0.6, lambda a, rr=rr, yy=yy: anel(c, fx, yy, rr, rr * 0.3, a, TINTA2))
    E.foco(c, t, C["s05.b"], 0.5, lambda a: punho(c, fx, fy, 190, a))
    E.foco(c, t, C["s05.b"] + 0.4, 0.4, lambda a: (F.seta(c, fx + 60, fy - 230, fx + 60, fy - 380, E.COR, a, 10),
                                                   E.pilula(c, "polegar = corrente", fx + 300, fy - 330, 42, "g", fundo=E.COR, a=a)))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "dedos = campo B", fx + 300, fy + 400, 42, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s05.b"], ps("polegar na", "i", 64) + [("corrente", "g", 64, COR)], XE, 420, passo=0.12)
    E.frase(c, t, C["s05.d"], ps("dedos no", "i", 64) + [("campo", "g", 64)], XE, 540, passo=0.12)


# ---------------- símbolos ----------------
def flecha(c, x, y, L, a, frente=True):
    """flecha de lado: ponta à direita (frente) ou cauda com penas"""
    M.line(c, x - L / 2, y, x + L / 2, y, TINTA, a, 7)
    F._cabeca(c, x + L / 2 + 20, y, 1, 0, 40, TINTA, a)
    for k in (-1, 1):
        M.line(c, x - L / 2, y, x - L / 2 - 30, y + k * 26, TINTA2, a, 6)


def b_simbolos(c, t, C, b):
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], ps("o campo", "i", 84) + [("fura a folha", "g", 84, COR)], XE, 220, passo=0.12)
        for i, (k, sai, nome, l2) in enumerate((("s06.b", True, "saindo", "ponta da flecha vindo"), ("s06.c", False, "entrando", "cauda da flecha indo"))):
            x = 560 + i * 800
            E.foco(c, t, C[k], 0.5, lambda a, x=x, sai=sai: simbolo_campo(c, x, 560, 130, sai, a))
            E.frase(c, t, C[k] + 0.3, [(nome, "g", 80, COR)], x, 800, "center")
            E.frase(c, t, C[k] + 0.7, ps(l2, "i", 50, TINTA2), x, 880, "center", 0.1)
        return
    E.frase(c, t, C["s07.a"], ps("fio na folha,", "i", 70) + [("corrente para cima", "g", 66, COR)], XE, 190, passo=0.12)
    fx = 1100
    fio_v(c, t, C["s07.a"], fx, 270, 1040)
    folha_campo(c, t, C["s07.b"], fx + 140, 360, 4, 4, 150, False, 26)
    folha_campo(c, t, C["s07.c"], fx - 140 - 3 * 150, 360, 4, 4, 150, True, 26)
    E.foco(c, t, C["s07.b"] + 0.6, 0.4, lambda a: E.pilula(c, "à direita: entra", fx + 370, 1010, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.c"] + 0.6, 0.4, lambda a: E.pilula(c, "à esquerda: sai", fx - 370, 1010, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: (punho(c, fx, 600, 150, a), anel(c, fx, 600, 260, 70, a, E.COR, largura=6)))


# ---------------- o valor ----------------
def b_valor(c, t, C, b):
    if t < C["s09"]:
        F.formula_legenda(c, t, C["s08.a"], "B = f{μ₀ · i}{2π · d}", [("i", "corrente", "A"), ("d", "distância até o fio", "m"),
                                                                  ("μ₀", "constante do vácuo", None)],
                          XE, 330, 130, tl=[C["s08.b"], C["s08.c"], C["s08.d"]])
        E.foco(c, t, C["s08.d"] + 1.0, 0.5, lambda a: E.formula(c, "μ₀ = 4π · 10^{−7}", 1150, 930, 70, "g", COR, a))
        fx = 1500
        fio_v(c, t, C["s08.a"], fx, 200, 760)
        E.foco(c, t, C["s08.c"], 0.4, lambda a: (M.line(c, fx, 480, fx + 260, 480, TINTA2, a, 4, dash=E.TRACO),
                                                 c.drawCircle(fx + 260, 480, 12, M.paint(TINTA, a)),
                                                 centro(c, "d", fx + 130, 455, 56, "g", TINTA, a)))
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("leia como", "i", 84) + [("proporção", "g", 84, COR)], XE, 220, passo=0.12)
        E.formula_em(c, t, C["s09"] + 0.4, "B = f{μ₀ · i}{2π · d}", 1180, 300, 110, "g", TINTA)
        for k, y, l1, l2, cor in (("s09.a", 560, "i × 2", "B × 2", CERTO), ("s09.b", 800, "d × 2", "B ÷ 2", ERRADO)):
            E.foco(c, t, C[k], 0.5, lambda a, y=y, l1=l1: E.formula(c, l1, XE + 60, y, 110, "g", TINTA, a))
            E.foco(c, t, C[k] + 0.4, 0.4, lambda a, y=y: F.seta(c, XE + 470, y - 36, XE + 640, y - 36, TINTA2, a, 8))
            E.foco(c, t, C[k] + 0.8, 0.5, lambda a, y=y, l2=l2, cor=cor: E.formula(c, l2, XE + 700, y, 110, "g", cor, a))
        E.frase(c, t, C["s09.a"] + 0.4, ps("em cima: junto", "i", 50, TINTA2), XE + 1150, 560, passo=0.1)
        E.frase(c, t, C["s09.b"] + 0.4, ps("embaixo: ao contrário", "i", 50, TINTA2), XE + 1150, 800, passo=0.1)
        return
    E.frase(c, t, C["s10.a"], [("i = 10", "g", 70), ("A", "b", 56, F.UNID)], XE, 200, passo=0.2)
    E.frase(c, t, C["s10.a"] + 0.5, [("d = 0,2", "g", 70), ("m", "b", 56, F.UNID)], XE + 480, 200, passo=0.2)
    x, y = 480, 470
    E.formula_em(c, t, C["s10.a"] + 0.8, "B = f{4π · 10^{−7} · 10}{2π · 0,2}", x - 300, y, 110, "g", TINTA)
    if t >= C["s10.b"]:  # o pi corta
        w0 = E.formula(None, "B = ", 0, 0, 110, a=0)
        w4 = E.formula(None, "4", 0, 0, 110 * 0.78, a=0)
        E.risco(c, x - 300 + w0 + w4 + 6, y - 40, x - 300 + w0 + w4 + 70, y - 110, t, C["s10.b"], E.COR, 8)
        w2 = E.formula(None, "2", 0, 0, 110 * 0.78, a=0)
        xb = x - 300 + w0 + (E.formula(None, "f{4π · 10^{−7} · 10}{2π · 0,2}", 0, 0, 110, a=0) - E.formula(None, "2π · 0,2", 0, 0, 110 * 0.78, a=0)) / 2 + w2 - 4
        E.risco(c, xb, y + 100, xb + 64, y + 30, t, C["s10.b"] + 0.2, E.COR, 8)
    E.foco(c, t, C["s10.c"], 0.5, lambda a: E.formula(c, "f{4}{2} = 2", 1420, 470, 90, "g", COR, a))
    E.formula_em(c, t, C["s10.d"], "= f{2 · 10^{−7} · 10}{0,2}", x - 300, 760, 100, "g", TINTA)
    E.foco(c, t, C["s10.e"], 0.5, lambda a: (E.bola(c, 1450, 760, 150, a=a), E.formula(c, "10^{−5} T", 1450, 790, 76, "g", E.SOBRE, a, "center")))


# ---------------- espira e solenoide ----------------
def b_espira(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("o fio num círculo:", "i", 76) + [("espira", "g", 76, COR)], XE, 200, passo=0.12)
        cx, cy, R = 1350, 600, 250
        if t >= C["s11.a"]:
            q = ease_io(prog(t, C["s11.a"], 0.8))
            c.drawArc(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), 90, 360 * q, False, M.paint(TINTA, 1, stroke=9))
            pts = [(cx + R * math.cos(-2 * math.pi * k / 40), cy + R * math.sin(-2 * math.pi * k / 40)) for k in range(40)]  # anti-horário
            F.corrente(c, t, C["s11.a"] + 0.8, pts, espaco=170)
        E.foco(c, t, C["s11.b"], 0.5, lambda a: simbolo_campo(c, cx, cy, 44, True, a))
        E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: E.escreve(c, "B", cx + 60, cy - 40, 60, "g", TINTA, a))
        E.foco(c, t, C["s11.c"], 0.4, lambda a: (M.line(c, cx, cy, cx + R * 0.71, cy + R * 0.71, TINTA2, a, 5, dash=E.TRACO),
                                                 E.escreve(c, "R", cx + 70, cy + 140, 60, "g", COR, a)))
        E.formula_em(c, t, C["s11.b"], "B = f{μ₀ · i}{2R}", XE, 450, 110, "g", TINTA)
        E.frase(c, t, C["s11.c"], [("R", "g", 56, COR), ("raio:", "i", 60), ("do centro ao fio", "i", 60, TINTA2)], XE, 650, passo=0.12)
        E.frase(c, t, C["s11.d"], [("i", "g", 60, COR), ("↑", "g", 60), ("B", "g", 60), ("↑", "g", 60), ("·", "g", 60, TINTA2), ("R", "g", 60, COR), ("↑", "g", 60), ("B", "g", 60), ("↓", "g", 60)],
                XE, 820, passo=0.12)
        return
    x0, cy, w, ry = 800, 640, 760, 150
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("muitas espiras:", "i", 76) + [("solenoide", "g", 76, COR)], XE, 200, passo=0.12)
        E.foco(c, t, C["s12.a"], 0.6, lambda a: bobina(c, x0, cy, w, ry, 9, a, t=t, t0=C["s12.a"] + 0.6))
        E.formula_em(c, t, C["s12.b"], "B = f{μ₀ · N · i}{L}", XE, 430, 100, "g", TINTA)
        E.frase(c, t, C["s12.c"], [("N:", "g", 56, COR), ("número de espiras", "i", 56)], XE, 560, passo=0.12)
        E.frase(c, t, C["s12.c"] + 0.8, [("L:", "g", 56, COR), ("comprimento", "i", 56)], XE, 650, passo=0.12)
        if t >= C["s12.c"] + 0.8:
            E.segmento(c, t, C["s12.c"] + 0.8, (x0, cy + ry + 70), (x0 + w, cy + ry + 70), "L", cor=TINTA2, largura=4, d=0.6)
        if t >= C["s12.d"]:
            for k in range(3):
                yy = cy - ry * 0.5 + k * ry * 0.5
                F.seta(c, x0 + 30, yy, x0 + w - 30, yy, TINTA2, ep(t, C["s12.d"] + 0.15 * k, 0.4), 6, p=ep(t, C["s12.d"] + 0.15 * k, 0.6))
            E.foco(c, t, C["s12.d"] + 0.6, 0.4, lambda a: E.pilula(c, "dentro: reto e igual", XE + 250, 820, 46, "g", fundo=TINTA, a=a))
        return
    # a bobina vira um ímã: linhas como as do ímã em barra, N à direita
    E.frase(c, t, C["s13.a"], ps("vira um", "i", 76) + [("ímã em barra", "g", 76, COR)], XE, 200, passo=0.12)
    F.linhas_campo(c, t, C["s13.a"] + 0.3, x0 + w / 2, cy, w, 2, d=1.2, h=150)
    bobina(c, x0, cy, w, ry, 9, 1, t=t, t0=C["s13"])
    for k in range(3):
        yy = cy - ry * 0.5 + k * ry * 0.5
        F.seta(c, x0 + 30, yy, x0 + w - 30, yy, TINTA2, 1, 6)
    E.foco(c, t, C["s13.a"] + 0.6, 0.4, lambda a: (E.pilula(c, "N", x0 + w + 80, cy - 90, 56, "g", fundo=E.COR, a=a), E.pilula(c, "S", x0 - 80, cy - 90, 56, "g", fundo=NEG, a=a)))
    E.frase(c, t, C["s13.b"], ps("dedos na corrente,", "i", 54), XE, 340, passo=0.1)
    E.frase(c, t, C["s13.c"], [("polegar", "g", 54), ("=", "g", 54, TINTA2), ("norte", "g", 54, COR)], XE, 420, passo=0.12)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.foco(c, t, C["s14.a"], 0.5, lambda a: E.formula(c, "d × 2  →  B ÷ 4 ?", XE, 400, 110, "g", ERRADO, a))
    if t >= C["s14.a"] + 1.0:
        E.risco(c, XE + 540, 420, XE + 900, 330, t, C["s14.a"] + 1.0, largura=12)
    E.frase(c, t, C["s14.b"], ps("isso é da", "i", 60) + [("força entre cargas", "g", 58)], XE, 560, passo=0.12)
    E.foco(c, t, C["s14.b"] + 0.6, 0.5, lambda a: E.formula(c, "F = f{k · Q · q}{d^2}", 1250, 580, 84, "g", TINTA2, a))
    E.foco(c, t, C["s14.c"], 0.5, lambda a: E.formula(c, "fio:  B = f{μ₀ · i}{2π · d}", XE, 800, 90, "g", TINTA, a))
    E.foco(c, t, C["s14.d"], 0.5, lambda a: E.pilula(c, "d × 2  →  B ÷ 2", 1400, 780, 70, "g", fundo=CERTO, a=a))


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 180, "center")
        E.formula_em(c, t, C["s15.a"], "f{μ₀}{2π} = f{4π · 10^{−7}}{2π} = 2 · 10^{−7}", W / 2, 400, 110, "g", BR, "center")
        E.formula_em(c, t, C["s15.b"], "B = 2 · 10^{−7} · f{i}{d}", W / 2, 700, 140, "g", CLARO, "center")
        E.foco(c, t, C["s15.c"], 0.5, lambda a: E.pilula(c, "sem pi na conta", W / 2, 900, 60, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s16.a"], ps("quantas vezes o campo", "i", 70, CLARO) + [("muda?", "g", 70, BR)], W / 2, 200, "center", 0.12)
    E.formula_em(c, t, C["s16.b"], "B × f{(o que mudou em cima)}{(o que mudou embaixo)}", W / 2, 470, 90, "g", BR, "center")
    E.foco(c, t, C["s16.b"] + 1.2, 0.5, lambda a: E.formula(c, "i × 3,  d × 2   →   B × f{3}{2}", W / 2, 700, 84, "g", CLARO, a, "center"))
    E.frase(c, t, C["s16.c"], [("vale para o", "i", 56, CLARO), ("fio longo", "g", 56, BR), ("e pontos perto dele", "i", 56, CLARO)], W / 2, 930, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    fx = 1350
    if t < C["s18"]:
        fio_v(c, t, C["s17.a"], fx, 240, 1000)
        E.foco(c, t, C["s17.a"] + 0.5, 0.4, lambda a: F.medida(c, 6, "A", fx - 60, 330, 64, COR, a, "right"))
        E.foco(c, t, C["s17.b"], 0.4, lambda a: (M.line(c, fx, 620, fx + 200, 620, TINTA2, a, 4, dash=E.TRACO), c.drawCircle(fx + 200, 620, 12, M.paint(TINTA, a)),
                                                 F.medida(c, 3, "cm", fx + 100, 590, 46, TINTA, a, "center")))
        E.foco(c, t, C["s17.b"], 0.5, lambda a: E.formula(c, "3 cm:  B = 4 · 10^{−5} T", XE, 360, 70, "g", TINTA, a))
        E.frase(c, t, C["s17.c"], [("6 cm", "g", 64, COR), ("e", "i", 66), ("18 A:", "g", 64, COR), ("B = ?", "g", 64)], XE, 520, passo=0.15)
        E.frase(c, t, C["s17.d"], ps("à direita do fio:", "i", 60) + [("entra ou sai?", "g", 60, COR)], XE, 680, passo=0.12)
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=500, r=200)
        E.frase(c, t, C["s18"], [("6 cm", "g", 64, COR), ("e", "i", 66), ("18 A:", "g", 64, COR), ("B = ?", "g", 64)], XE, 420, passo=0.12)
        E.frase(c, t, C["s18"] + 0.2, [("entra ou sai?", "g", 60, COR)], XE, 540)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s20"]:
        rows = (("s19.a", "s19.b", "i: 6 → 18", "× 3", "em cima"), ("s19.c", "s19.d", "d: 3 → 6", "× 2", "embaixo"))
        for i, (k1, k2, l1, l2, l3) in enumerate(rows):
            y = 330 + i * 200
            E.foco(c, t, C[k1], 0.5, lambda a, y=y, l1=l1: E.formula(c, l1, XE, y, 100, "g", TINTA, a))
            E.foco(c, t, C[k2], 0.5, lambda a, y=y, l2=l2: E.pilula(c, l2, 1000, y - 34, 70, "g", fundo=E.COR, a=a))
            E.foco(c, t, C[k2] + 0.3, 0.4, lambda a, y=y, l3=l3: E.escreve(c, l3, 1170, y - 10, 56, "i", TINTA2, a))
        E.foco(c, t, C["s19.e"], 0.5, lambda a: E.formula(c, "B × f{3}{2} = B × 1,5", XE, 820, 110, "g", COR, a))
        return
    E.formula_em(c, t, C["s20.a"], "4 · 10^{−5} × 1,5", XE, 300, 100, "g", TINTA)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: (E.bola(c, 560, 560, 170, a=a), E.formula(c, "6 · 10^{−5} T", 560, 590, 70, "g", E.SOBRE, a, "center")))
    fx = 1300
    fio_v(c, t, C["s20"], fx, 230, 1000)
    E.foco(c, t, C["s20.c"], 0.5, lambda a: punho(c, fx, 620, 150, a))
    E.foco(c, t, C["s20.c"] + 0.2, 0.5, lambda a: anel(c, fx, 620, 260, 70, a, E.COR, largura=6))
    folha_campo(c, t, C["s20.d"], fx + 160, 330, 3, 2, 150, False, 30)
    E.foco(c, t, C["s20.e"], 0.5, lambda a: E.pilula(c, "o campo entra", 1560, 900, 60, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", [("corrente", "g", 70), ("cria campo", "i", 74)]),
                 ("s21.b", [("sentido:", "g", 70), ("mão direita", "i", 74)]),
                 ("s21.c", [("B", "g", 70), ("cresce com", "i", 74), ("i,", "g", 70, COR), ("cai com", "i", 74), ("d", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
        E.frase(c, t, C["s21.d"], ps("próxima aula: a força numa", "i", 60, TINTA2) + [("carga em movimento", "g", 60, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.foco(c, t, C["s22.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s22.a"] + 0.2, 0.4))
    E.frase(c, t, C["s22.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fio=b_fio, simbolos=b_simbolos, valor=b_valor, espira=b_espira,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
