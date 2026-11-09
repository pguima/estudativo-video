"""Visual — Estudativo · FIS-MAG-006: lei de Lenz. Linguagem visual do Magnetismo: veja o visual.py da FIS-MAG-001.
Cada cena mostra o ímã e a espira de lado (a face que a espira cria vira uma pílula N laranja ou S azul) e, à direita, a espira
vista do lado do ímã (vista_do_ima), com a corrente andando no sentido certo. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-006_lei_de_lenz.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("lei", "aproxima", "afasta", "porque", "freio", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
COBRE = "#C27A44"

# a regra da aula, conferida: corrente anti-horária vista de frente → campo saindo para quem olha (z+) → face norte
cruz = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
# no ponto de baixo da espira (r = −y), a corrente anti-horária anda para +x; dl × r̂ aponta o campo no centro
assert cruz((1, 0, 0), (0, 1, 0))[2] > 0
# os quatro casos: (polo que se move, chega?) → face que a espira cria do lado do ímã
CASOS = {("N", True): "N", ("N", False): "S", ("S", True): "S", ("S", False): "N"}
assert CASOS[("S", False)] == "N"  # a questão: sul se afastando → face norte → anti-horário


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças do magnetismo ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def barra(c, cx, cy, w=360, h=110, a=1.0, ang=0.0):
    """ímã em barra com o norte no sentido ang (graus da Física); letras em pé"""
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
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    sz = min(h, w / 2) * 0.55
    E._meio(c, "N", cx + ux * w / 4, cy + uy * w / 4, sz, "g", BR, a)
    E._meio(c, "S", cx - ux * w / 4, cy - uy * w / 4, sz, "g", BR, a)


def espira_lado(c, x, cy, ry, a=1.0, face=None, lado_face=-1, af=1.0):
    """espira vista de lado (elipse fina) e, se face, a pílula da face que ela cria do lado lado_face"""
    if a <= 0:
        return
    c.drawOval(skia.Rect.MakeXYWH(x - 34, cy - ry, 68, 2 * ry), M.paint(TINTA, a, stroke=9))
    if face and af > 0:
        E.pilula(c, face, x + lado_face * 90, cy, 60, "g", fundo=E.COR if face == "N" else NEG, a=a * af)


def vista_do_ima(c, t, t0, cx, cy, R, face, a=1.0, rot=True):
    """a espira vista do lado do ímã: face N = corrente anti-horária; S = horária"""
    if a <= 0 or t < t0:
        return
    q = ep(t, t0, 0.4) * a
    c.drawCircle(cx, cy, R, M.paint(TINTA, q, stroke=9))
    n = 40
    sinal = -1 if face == "N" else 1  # anti-horário na tela: ângulo da tela diminuindo
    pts = [(cx + R * math.cos(sinal * 2 * math.pi * k / n), cy + R * math.sin(sinal * 2 * math.pi * k / n)) for k in range(n)]
    F.corrente(c, t, t0 + 0.3, pts, espaco=150, a=a)
    E._meio(c, face, cx, cy, R * 0.75, "g", E.COR if face == "N" else NEG, q)
    if rot:
        E.foco(c, t, t0 + 0.4, 0.4, lambda a_: centro(c, "anti-horário" if face == "N" else "horário", cx, cy + R + 80, 50, "g", TINTA, a_ * a))
        E.foco(c, t, t0 + 0.6, 0.4, lambda a_: centro(c, "visto do lado do ímã", cx, cy - R - 40, 42, "i", TINTA2, a_ * a))


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


def cena_lado(c, t, t0, chega, polo_frente="N", face=None, tf=None, x_esp=1050, cy=620):
    """ímã à esquerda, com polo_frente virado para a espira, chegando ou saindo; a face da espira aparece em tf"""
    d = max(0.0, t - t0)
    q = min(1.0, d / 3.0)
    xm = lerp(380, 640, q) if chega else lerp(640, 380, q)
    ang = 0 if polo_frente == "N" else 180
    barra(c, xm, cy, 380, 110, ep(t, t0 - 0.4, 0.4), ang)
    F.seta(c, xm - 110 if chega else xm + 110, cy - 110, xm + 110 if chega else xm - 110, cy - 110, TINTA2, ep(t, t0, 0.3), 7)
    af = ep(t, tf, 0.4) if tf is not None else 0
    espira_lado(c, x_esp, cy, 190, ep(t, t0 - 0.4, 0.4), face, -1, af)
    if face and tf is not None and t >= tf + 0.5:  # a força da espira no ímã
        repele = face == polo_frente
        x0 = xm + 190
        F.seta(c, x0 + 30, cy + 110, x0 - 150 if repele else x0 + 160, cy + 110, E.COR, ep(t, tf + 0.5, 0.3), 10)
    return xm


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        cx = 1350
        E.foco(c, t, C["s01.a"], 0.5, lambda a: (M.rrect(c, cx - 130, 150, 260, 860, 30, E.mix(COBRE, BR, 0.55), a),
                                                 c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 130, 150, 260, 860), 30, 30), M.paint(COBRE, a, stroke=10))))
        v = 0.0
        if t >= C["s01.c"]:
            v = 70 * (t - C["s01.c"])
        y = 280 + min(v, 560)
        E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: barra(c, cx, y, 220, 90, a, -90))
        E.foco(c, t, C["s01.b"], 0.4, lambda a: E.pilula(c, "o cobre não gruda", cx + 330, 300, 46, "g", fundo=TINTA, a=a))
        if t >= C["s01.d"]:
            for k in (-1, 1):
                F.seta(c, cx + k * 70, y + 90, cx + k * 70, y - 40, E.COR, ep(t, C["s01.d"], 0.4), 9)
        E.frase(c, t, C["s01.a"], ps("ímã num", "i", 76) + [("cano de cobre", "g", 76, COBRE)], XE, 260, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("desce", "i", 76) + [("devagar", "g", 76, COR)], XE, 420, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("quem segura:", "i", 60), XE, 620, passo=0.12)
        E.frase(c, t, C["s01.d"] + 0.6, [("a corrente", "g", 64, COR), ("no cano", "i", 64)], XE, 710, passo=0.12)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s, dt) in enumerate((("s02.a", "o sentido da corrente", 1.2), ("s02.b", "por que ela freia", 0))):
        y = 470 + i * 170
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def far(a, x, y):
        E.formula(c, "ε = f{ΔΦ}{Δt}", x + 20, y + 30, 56, "g", TINTA, a, "center")

    def esp(a, x, y):
        c.drawCircle(x - 60, y, 70, M.paint(TINTA, a, stroke=7))
        E._meio(c, "N", x - 60, y, 60, "g", E.COR, a)
        F.seta(c, x + 30, y, x + 150, y, E.COR, a, 8)
    lembrete2(c, t, C, "s03", (("s03.b", "Faraday:", "fluxo muda: corrente"), ("s03.c", "espira com corrente:", "vira um ímã")), (far, esp))


# ---------------- a lei ----------------
def b_lei(c, t, C, b):
    E.frase(c, t, C["s04"], [("lei de", "i", 100), ("Lenz", "g", 100, COR)], XE, 240)
    E.frase(c, t, C["s04.a"], ps("a corrente induzida luta contra", "i", 66) + [("a mudança", "g", 66, COR)], XE, 400, passo=0.1)
    for i, (k, l1, l2) in enumerate((("s04.b", "fluxo aumenta", "ela tenta diminuir"), ("s04.c", "fluxo diminui", "ela tenta manter"))):
        y = 580 + i * 140
        E.foco(c, t, C[k], 0.5, lambda a, y=y, l1=l1: E.pilula(c, l1, XE + 220, y - 20, 50, "g", fundo=TINTA, a=a))
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, y=y: F.seta(c, XE + 480, y - 20, XE + 600, y - 20, TINTA2, a, 8))
        E.frase(c, t, C[k] + 0.6, [(l2, "g", 60, COR)], XE + 640, y)
    E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "a espira é do contra", W / 2, 940, 70, "g", fundo=E.COR, a=a))


# ---------------- aproxima ----------------
def b_aproxima(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("o", "i", 76), ("norte", "g", 76, COR), ("chega", "i", 76)], XE, 200, passo=0.12)
    cena_lado(c, t, C["s05.a"], True, "N", "N", C["s05.c"])
    E.foco(c, t, C["s05.b"], 0.5, lambda a: E.pilula(c, "fluxo aumenta", 640, 900, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.d"], 0.5, lambda a: E.pilula(c, "N com N: empurra", 640, 380, 50, "g", fundo=E.COR, a=a))
    if t >= C["s06"]:
        vista_do_ima(c, t, C["s06.a"], 1550, 600, 190, "N")
        E.foco(c, t, C["s06.c"], 0.5, lambda a: E.pilula(c, "face norte = anti-horário", 1550, 960, 50, "g", fundo=E.COR, a=a))


# ---------------- afasta ----------------
def b_afasta(c, t, C, b):
    E.frase(c, t, C["s07.a"], [("o ímã", "i", 76), ("se afasta", "g", 76, COR)], XE, 200, passo=0.12)
    cena_lado(c, t, C["s07.a"], False, "N", "S", C["s07.c"])
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "fluxo diminui", 640, 900, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: E.pilula(c, "S com N: puxa", 640, 380, 50, "g", fundo=NEG, a=a))
    if t >= C["s08"]:
        vista_do_ima(c, t, C["s08.a"], 1550, 560, 170, "S")
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "chegando: empurra", 1550, 880, 46, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "saindo: puxa", 1550, 970, 46, "g", fundo=TINTA, a=a))


# ---------------- por quê ----------------
def b_porque(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("e se fosse a", "i", 76) + [("favor?", "g", 76, ERRADO)], XE, 220, passo=0.12)
        cy = 600
        q = min(1.0, max(0.0, t - C["s09.a"]) ** 2 / 9)
        xm = lerp(400, 820, q)
        barra(c, xm, cy, 380, 110, ep(t, C["s09.a"], 0.4))
        espira_lado(c, 1150, cy, 190, ep(t, C["s09.a"], 0.4))
        for k, (kk, s) in enumerate((("s09.b", "mais rápido"), ("s09.c", "mais corrente"), ("s09.d", "mais puxão"))):
            E.foco(c, t, C[kk], 0.4, lambda a, k=k, s=s: E.pilula(c, s, 1550, 380 + k * 120, 48, "g", fundo=ERRADO, a=a))
        if t >= C["s09.a"] + 0.6:
            F.seta(c, xm + 200, cy + 110, xm + 200 + 120 + 200 * q, cy + 110, ERRADO, ep(t, C["s09.a"] + 0.6, 0.3), 10)
        E.foco(c, t, C["s09.e"], 0.5, lambda a: (E.pilula(c, "movimento do nada: nunca", W / 2, 920, 60, "g", fundo=TINTA, a=a)))
        E.foco(c, t, C["s09.e"] + 0.4, 0.4, lambda a: E.selo(c, W / 2 + 470, 920, 50, False, a))
        return
    E.frase(c, t, C["s10.a"], ps("o sinal de", "i", 80) + [("menos", "g", 80, COR)], XE, 260, passo=0.12)
    E.formula_em(c, t, C["s10.b"], "ε = − f{ΔΦ}{Δt}", W / 2, 600, 180, "g", TINTA, "center")
    if t >= C["s10.c"]:
        w = E.formula(None, "ε = − f{ΔΦ}{Δt}", 0, 0, 180, a=0)
        xm = W / 2 - w / 2 + E.formula(None, "ε = ", 0, 0, 180, a=0) + 40
        c.drawCircle(xm, 540, 80 + 5 * math.sin(t * 5), M.paint(E.COR, ep(t, C["s10.c"], 0.4), stroke=7))
        E.foco(c, t, C["s10.c"] + 0.3, 0.4, lambda a: E.pilula(c, "o menos é a lei de Lenz", W / 2, 880, 60, "g", fundo=E.COR, a=a))


# ---------------- freio ----------------
def b_freio(c, t, C, b):
    if t < C["s12"]:
        cx = 1300
        M.rrect(c, cx - 150, 140, 300, 880, 30, E.mix(COBRE, BR, 0.55))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 150, 140, 300, 880), 30, 30), M.paint(COBRE, 1, stroke=10))
        y = 560
        E.foco(c, t, C["s11.a"], 0.5, lambda a: [c.drawOval(skia.Rect.MakeXYWH(cx - 150, yy - 26, 300, 52), M.paint(COBRE, a, stroke=7)) for yy in (300, 820)])
        barra(c, cx, y, 260, 100, 1, -90)
        E.foco(c, t, C["s11.b"], 0.4, lambda a: (E.pilula(c, "N", cx + 240, 820, 52, "g", fundo=E.COR, a=a), F.seta(c, cx - 200, 760, cx - 200, 640, E.COR, a, 10)))
        E.foco(c, t, C["s11.c"], 0.4, lambda a: (E.pilula(c, "N", cx + 240, 300, 52, "g", fundo=E.COR, a=a), F.seta(c, cx - 200, 440, cx - 200, 320, E.COR, a, 10)))
        E.frase(c, t, C["s11.a"], ps("cada pedaço:", "i", 62) + [("uma espira", "g", 62, COR)], XE, 240, passo=0.12)
        E.frase(c, t, C["s11.b"], [("abaixo:", "g", 56), ("empurra", "i", 60, COR)], XE, 760, passo=0.12)
        E.frase(c, t, C["s11.c"], [("acima:", "g", 56), ("puxa", "i", 60, COR)], XE, 400, passo=0.12)
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "as duas freiam a queda", XE + 300, 560, 54, "g", fundo=CERTO, a=a))
        return
    E.frase(c, t, C["s12.a"], [("freio", "g", 100, COR), ("magnético", "i", 100)], XE, 260)
    E.frase(c, t, C["s12.b"], ps("montanha-russa: ímãs e placas de metal", "i", 60), XE, 420, passo=0.1)
    q = ease_out(prog(t, C["s12.b"], 3.0))
    E.foco(c, t, C["s12.b"], 0.5, lambda a: (M.rrect(c, 1000, 760, 700, 40, 8, "#9AA0A8", a), F.chao(c, 300, 1800, 840, a)))
    F.carrinho(c, lerp(400, 1250, q), 840, 300, a=ep(t, C["s12.b"], 0.4))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "freia sem encostar", 1350, 600, 56, "g", fundo=CERTO, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("a espira", "i", 64) + [("sempre empurra?", "g", 64, ERRADO)], XE, 320, passo=0.12)
    E.frase(c, t, C["s13.b"], ps("luta contra a", "i", 64) + [("mudança,", "g", 64, COR)] + ps("não contra o ímã", "i", 64), XE, 440, passo=0.1)
    if t >= C["s13.c"]:
        cena_lado(c, t, C["s13.c"], False, "N", "S", C["s13.c"] + 0.4, cy=700)
    E.frase(c, t, C["s13.d"], ps("pergunte:", "i", 56) + [("o fluxo aumenta ou diminui?", "g", 56, COR)], XE, 980, passo=0.1)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 180, "center")
        E.frase(c, t, C["s14.a"], [("chegou,", "g", 110, BR), ("repele", "g", 110, E.CLARO)], W / 2, 400, "center", 0.2)
        E.frase(c, t, C["s14.b"], [("saiu,", "g", 110, BR), ("atrai", "g", 110, E.CLARO)], W / 2, 560, "center", 0.2)
        E.frase(c, t, C["s14.c"], ps("repelir: face", "i", 56, CLARO) + [("igual", "g", 56, BR)] + ps("ao polo", "i", 56, CLARO), W / 2, 760, "center", 0.1)
        E.frase(c, t, C["s14.d"], ps("atrair: face", "i", 56, CLARO) + [("oposta", "g", 56, BR)], W / 2, 860, "center", 0.1)
        return
    E.frase(c, t, C["s15.a"], ps("depois, a face vira", "i", 66, CLARO) + [("sentido", "g", 66, BR)], W / 2, 170, "center", 0.12)
    for i, (k, face) in enumerate((("s15.b", "N"), ("s15.c", "S"))):
        x = 620 + i * 680
        if t >= C[k]:
            q = ep(t, C[k], 0.4)
            c.drawCircle(x, 470, 160, M.paint(BR, q, stroke=8))
            n = 36
            sinal = -1 if face == "N" else 1
            pts = [(x + 160 * math.cos(sinal * 2 * math.pi * j / n), 470 + 160 * math.sin(sinal * 2 * math.pi * j / n)) for j in range(n)]
            F.corrente(c, t, C[k] + 0.2, pts, espaco=140)
            E._meio(c, face, x, 470, 120, "g", E.COR if face == "N" else "#6FA8FF", q)
            E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x=x, face=face: centro(c, "anti-horário" if face == "N" else "horário", x, 720, 58, "g", BR, a))
    E.frase(c, t, C["s15.b"] + 0.6, ps("olhando do lado do ímã", "i", 50, CLARO), W / 2, 800, "center", 0.1)
    E.frase(c, t, C["s15.d"], ps("visto do outro lado:", "i", 50, CLARO) + [("inverta", "g", 50, BR)], W / 2, 890, "center", 0.1)
    E.frase(c, t, C["s15.e"], ps("sem ímã: aumentou, campo contrário; diminuiu, a favor", "i", 46, CLARO), W / 2, 980, "center", 0.06)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s17"]:
        cena_lado(c, t, C["s16.a"], False, "S", None, None, x_esp=1300, cy=520)
        E.frase(c, t, C["s16.a"], [("o", "i", 66), ("sul", "g", 66, NEG), ("se", "i", 66), ("afasta", "g", 66)], XE, 760, passo=0.12)
        E.frase(c, t, C["s16.b"], ps("que", "i", 60) + [("face", "g", 60, COR)] + ps("a espira cria?", "i", 60), XE, 870, passo=0.12)
        E.frase(c, t, C["s16.c"], ps("e o", "i", 60) + [("sentido,", "g", 60, COR)] + ps("visto do ímã?", "i", 60), XE, 970, passo=0.12)
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=500, r=200)
        E.frase(c, t, C["s17"], [("sul", "g", 64, NEG), ("se afastando", "g", 64)], XE, 420, passo=0.12)
        E.frase(c, t, C["s17"] + 0.2, [("face?", "g", 64, COR), ("sentido?", "g", 64, COR)], XE, 540, passo=0.12)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s18.a"], [("saiu:", "g", 80), ("atrai", "g", 80, COR)], XE, 220, passo=0.15)
    cena_lado(c, t, C["s18"], False, "S", "N", C["s18.c"], x_esp=1050, cy=560)
    E.frase(c, t, C["s18.c"], ps("atrair um", "i", 60) + [("sul:", "g", 60, NEG)] + ps("face", "i", 60) + [("norte", "g", 60, COR)], XE, 900, passo=0.12)
    vista_do_ima(c, t, C["s18.d"], 1580, 540, 180, "N")
    E.foco(c, t, C["s18.e"], 0.5, lambda a: E.pilula(c, "anti-horário", 1580, 930, 64, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s19.a", [("a corrente", "i", 74), ("luta contra a mudança", "g", 70)]),
                 ("s19.b", [("chegou, repele;", "g", 70), ("saiu, atrai", "g", 70, COR)]),
                 ("s19.c", [("face norte:", "g", 70), ("anti-horário", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
        E.frase(c, t, C["s19.d"], ps("próxima aula: o", "i", 60, TINTA2) + [("transformador", "g", 60, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.foco(c, t, C["s20.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s20.a"] + 0.2, 0.4))
    E.frase(c, t, C["s20.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, lei=b_lei, aproxima=b_aproxima, afasta=b_afasta, porque=b_porque, freio=b_freio,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
