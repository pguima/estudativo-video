"""Visual — Estudativo · MAT-POT-013: contas em notação científica.
Peças locais: balança da compensação, Terra e Lua (desenho abstrato), grade de 81 luas, notas de dinheiro.
Todo instante vem de C[...]: entre dois cues, lerp(C[a], C[b], f), que acompanha qualquer voz."""
import math

import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Potências e Raízes")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-POT-013_contas_em_notacao_cientifica.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("multiplicar", "terra", "soma", "atalho", "questao", "fim"))
BR = "#FFFFFF"
assert 3 * 4 == 12 and 5 + 2 == 7 and 3 * 10 ** 5 * 4 * 10 ** 2 == 120000000 and 12 * 10 ** 7 == 120000000
assert 3 * 10 ** 5 + 8 * 10 ** 4 == 380000 and 11 * 10 ** 5 == 1100000 and 2 < 1100000 / 380000 < 3
assert round(60 / 74, 2) == 0.81 and 6 * 5 == 30 and 6 * 10 ** 4 * 5 * 10 ** 2 == 30000000


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


def pil_f(c, s, cx, cy, size, fundo=None, tinta=None, a=1.0):
    """pílula com fórmula dentro (E.pilula não entende expoente)"""
    w = E.formula(c, s, 0, 0, size, a=0)
    pw, ph = w + size * 1.1, size * 1.7
    M.rrect(c, cx - pw / 2, cy - ph / 2, pw, ph, ph / 2, fundo or E.COR, a)
    E.formula(c, s, cx, cy + size * 0.36, size, "g", tinta or E.SOBRE, a, "center")


def balanca(c, cx, cy, w, giro, rot_e, rot_d, a=1.0):
    """balança da compensação: giro em graus (> 0 sobe o lado esquerdo); no nível, o valor é o mesmo"""
    if a <= 0:
        return
    ang = math.radians(giro)
    dx, dy = w / 2 * math.cos(ang), w / 2 * math.sin(ang)
    M.line(c, cx, cy, cx, cy + 210, TINTA, a, 10)
    M.line(c, cx - 110, cy + 210, cx + 110, cy + 210, TINTA, a, 12)
    M.line(c, cx - dx, cy - dy, cx + dx, cy + dy, TINTA, a, 12)
    E.bola(c, cx, cy, 24, a=a)
    for lado, rot in ((-1, rot_e), (1, rot_d)):
        px, py = cx + lado * dx, cy + lado * dy
        M.line(c, px, py, px, py + 72, TINTA2, a, 5)
        rot(px, py + 130)


def compensa(c, t, t0, t1, cx, cy, w=860):
    """a balança pende quando a frente diminui (t0) e volta ao nível quando a potência cresce (t1)"""
    ang = 9 * ep(t, t0, 0.5) * (1 - ease_io(prog(t, t1, 0.8)))

    def rot(s_, k):
        def fn(px, py):
            E.foco(c, t, k, 0.4, lambda a: pil_f(c, s_, px, py, 76, a=a))
        return fn
    E.foco(c, t, t0, 0.5, lambda a: balanca(c, cx, cy, w, ang, rot("÷ 10", t0), rot("× 10", t1), a))


def conserta(c, t, dig, e0, e1, x, y, s, ta, tj, tc, terro=None):
    """a frente de dois algarismos salta para a forma em tj, e o expoente sobe em tc. Devolve o x do fim"""
    cl = E.casa(s)
    k = s / 170
    xf = x + 2 * cl + 44 * k
    wf = E.formula(c, "× 10", 0, 0, s, a=0)
    xe = xf + wf
    cor = ERRADO if terro is not None and terro <= t < tj + 0.7 else TINTA
    E.foco(c, t, ta, 0.5, lambda a: E.anda(c, t, dig, 2, [(tj, 1)], x, y, s, cor=cor, tv=tj - 0.3))
    E.foco(c, t, ta, 0.5, lambda a: (E.formula(c, "× 10", xf, y, s, a=a), E.formula(c, f"^{e0}", xe, y, s, a=a)))
    E.corta(c, t, tc, xe + 30 * k, y - 106 * k, 76 * k)
    E.foco(c, t, tc + 0.3, 0.4, lambda a: E.formula(c, f"^{e1}", xe + 66 * k, y, s, cor=COR, a=a))


def terra(c, cx, cy, r, a=1.0):
    """a Terra, abstrata: esfera da cor da matéria com manchas claras"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, E.COR, a)
    c.save()
    p = skia.Path(); p.addCircle(cx, cy, r * 0.985)
    c.clipPath(p, True)
    for dx, dy, w, h, g in ((-0.42, -0.34, 0.74, 0.42, -24), (0.34, 0.1, 0.58, 0.8, 18), (-0.3, 0.56, 0.56, 0.3, 10)):
        c.save(); c.translate(cx + dx * r, cy + dy * r); c.rotate(g)
        c.drawOval(skia.Rect.MakeXYWH(-w * r / 2, -h * r / 2, w * r, h * r), M.paint(E.CLARO, 0.55 * a))
        c.restore()
    c.restore()


def lua(c, cx, cy, r, a=1.0):
    """a Lua, abstrata: esfera cinza com crateras"""
    if a <= 0:
        return
    E.bola(c, cx, cy, r, "#A6A6AC", a)
    for dx, dy, q in ((-0.34, -0.26, 0.24), (0.3, 0.1, 0.16), (-0.08, 0.42, 0.13)):
        c.drawCircle(cx + dx * r, cy + dy * r, q * r, M.paint("#7D7D85", a))


def nota(c, x, y, w, h, s, cor, a=1.0):
    """nota de dinheiro (desenho simples): retângulo com moldura e o valor no meio"""
    if a <= 0:
        return
    sombra = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.2 * a))
    sombra.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 7))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 3, y + 6, w, h), 10, 10), sombra)
    M.rrect(c, x, y, w, h, 10, cor, a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 8, y + 8, w - 16, h - 16), 6, 6), M.paint(M.on(cor), 0.45 * a, stroke=2.5))
    size = h * 0.4
    centro(c, s, x + w / 2, y + h / 2 + size * 0.35, size, "g", M.on(cor), a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    ka, kb, kc = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        fcen(c, t, ka, "3 × 10^5", 620, 310, 150)
        fcen(c, t, kb, "+ 8 × 10^4", 1270, 310, 150)
        fcen(c, t, kc, "= 11 × 10^5", W / 2, 560, 150, ERRADO)
        E.foco(c, t, kc + 0.3, 0.5, lambda a: E.selo(c, 1460, 510, 66, False, a))
        E.frase(c, t, lerp(kc, C["s01.end"], 0.42), ps("sua resposta saiu", "i", 92) + [("quase o triplo", "g", 92, ERRADO)], W / 2, 770, "center", 0.14)
        E.frase(c, t, lerp(kc, C["s01.end"], 0.72), ps("do valor certo", "i", 92), W / 2, 890, "center", 0.14)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1490, 540, 250 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 280, passo=0.14)
        for i, (s, f) in enumerate((("multiplicar", 0.32), ("dividir", 0.42), ("somar", 0.5))):
            E.frase(c, t, lerp(ta, tb, f), [(s, "g", 112, COR)], XE, 420 + i * 120)
        E.frase(c, t, lerp(ta, tb, 0.62), ps("em notação científica", "i", 90), XE, 830, passo=0.14)
        E.foco(c, t, tb + 0.2, 0.5, lambda a: (centro(c, "+ atalho", 1490, 525, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1490, 610, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 240, 700, 120, "i", TINTA, a))
    x, w = 920, 830
    itens = (("s03.b", "escrever em", "notação científica"), ("s03.c", "multiplicar e dividir", "potências de mesma base"), ("s03.d", "fazer contas", "com decimais"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 130 + i * 230
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 62)], x + 44, y + 84)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 62, COR)], x + 44, y + 160)
    py = 300
    for i, (k, _, _) in enumerate(itens[1:], 1):
        py = lerp(py, 300 + i * 230, ease_io(prog(t, C[k] - 0.35, 0.5)))
    E.cursor(c, x + w - 30, py, ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.55), ps("faltou alguma?", "i", 62, COR) + ps("procure no canal", "i", 62), 920, 940, "left", 0.12)


# ---------------- multiplicar ----------------
def b_multiplicar(c, t, C, b):
    def caixas():
        ka, kb, kc, kd = C["s04.a"], C["s04.b"], C["s04.c"], C["s04.d"]
        E.frase(c, t, ka - 0.3, [("300 mil", "g", 130, COR), ("caixas", "i", 120)], W / 2, 280, "center", 0.2)
        E.frase(c, t, kb - 0.3, ps("cada uma com", "i", 96) + [("400 folhas", "g", 110, COR)], W / 2, 450, "center", 0.14)
        fcen(c, t, kc, "(3 × 10^5)", 540, 760, 130)
        fcen(c, t, kd - 0.1, "×", 960, 750, 120)
        fcen(c, t, kd, "(4 × 10^2)", 1380, 760, 130)
    E.saida(c, t, C["s05"] - 0.1, caixas)

    def juntar():
        ka, kb, kc, kd = C["s05.a"], C["s05.b"], C["s05.c"], C["s05.d"]
        E.frase(c, t, C["s05"] + 0.1, ps("a ordem não muda o resultado", "i", 76), W / 2, 150, "center", 0.11)
        p1, p2 = ep(t, ka, 0.5), ep(t, kb, 0.5)
        E.caixa_pontilhada(c, 240, 240, 620, 300, p1, COR, prog_=p1)
        E.caixa_pontilhada(c, 1000, 240, 700, 300, p2, COR, prog_=p2)
        cen(c, t, ka, "junte os da frente", 550, 325, 72, COR, "i")
        cen(c, t, kb, "junte as potências", 1350, 325, 72, COR, "i")
        fcen(c, t, ka + 0.1, "3 × 4", 550, 470, 120)
        fcen(c, t, kb + 0.1, "10^5 × 10^2", 1350, 470, 120)
        fcen(c, t, ka + 0.2, "×", 930, 410, 90)
        fcen(c, t, kc, "= 12", 550, 720, 150, COR)
        E.frase(c, t, lerp(kc, kd, 0.55), ps("mesma base,", "i", 72) + [("soma os expoentes", "g", 68, COR)], 1350, 660, "center", 0.11)
        fcen(c, t, kd, "= 10^7", 1350, 830, 150, COR)
    if C["s05"] - 0.1 <= t:
        E.saida(c, t, C["s06"] - 0.1, juntar)

    def forma():
        ka, kb, kc, kd = C["s06.a"], C["s06.b"], C["s06.c"], C["s06.d"]
        s, y = 170, 300
        tm, ts = lerp(kc, kd, 0.42), lerp(kd, C["s06.end"], 0.48)
        conserta(c, t, "12", 7, 8, 500, y, s, ka, kc, ts, terro=kb)
        E.saida(c, t, tm - 0.1, lambda: (E.frase(c, t, kb, ps("o valor está certo, mas", "i", 72) + [("12 passa de 10", "g", 76, ERRADO)], W / 2, 520, "center", 0.11),
                                         E.frase(c, t, kc, ps("uma casa para a", "i", 80) + [("esquerda:", "g", 76, COR), ("1,2", "g", 90, COR)], W / 2, 680, "center", 0.12)))
        if tm - 0.1 <= t:
            compensa(c, t, tm, kd, W / 2, 500, 760)
            E.frase(c, t, tm, ps("frente", "i", 66) + [("10 vezes menor", "g", 60, COR)], 480, 910, "center", 0.12)
            E.frase(c, t, kd, ps("potência", "i", 66) + [("10 vezes maior", "g", 60, COR)], 1440, 910, "center", 0.12)
    if C["s06"] - 0.1 <= t:
        E.saida(c, t, C["s07"] - 0.1, forma)

    if t >= C["s07"]:
        ka, kb = C["s07.a"], C["s07.b"]
        E.frase(c, t, C["s07"] + 0.1, ps("resposta", "i", 92), W / 2, 240, "center")
        E.cientifica(c, t, ka, "1,2", 8, W / 2, 510, 210, cor=COR, align="center")
        E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "120 milhões de folhas", W / 2, 760, 100, "g", a=a, cor=E.SOBRE))


# ---------------- dividir: Terra e Lua ----------------
def b_terra(c, t, C, b):
    def massas():
        ka, kb, kc, kd = C["s08.a"], C["s08.b"], C["s08.c"], C["s08.d"]
        tm = lerp(kb, kc, 0.45)
        E.frase(c, t, ka - 0.2, ps("dividir:", "i", 84, COR) + ps("divida os da frente", "i", 84), W / 2, 150, "center", 0.11)
        E.frase(c, t, kb, ps("e", "i", 84) + [("subtraia os expoentes", "g", 80, COR)], W / 2, 260, "center", 0.12)
        E.frase(c, t, tm, ps("massa: a quantidade de matéria", "i", 66), W / 2, 365, "center", 0.1)
        E.foco(c, t, kc, 0.6, lambda a: terra(c, 520, 610, 180, a))
        cen(c, t, kc, "Terra: cerca de", 520, 850, 66, TINTA, "i")
        wt = E.cientifica(c, t, kc + 0.2, "6", 24, 500, 960, 96, cor=COR, align="center")
        cen(c, t, kc + 0.8, "kg", 500 + wt / 2 + 60, 960, 76, TINTA, "i")
        E.foco(c, t, kd, 0.6, lambda a: lua(c, 1340, 660, 50, a))
        cen(c, t, kd, "Lua: cerca de", 1340, 850, 66, TINTA, "i")
        wl = E.cientifica(c, t, kd + 0.2, "7,4", 22, 1320, 960, 96, cor=COR, align="center")
        cen(c, t, kd + 0.8, "kg", 1320 + wl / 2 + 60, 960, 76, TINTA, "i")
    E.saida(c, t, C["s09"] - 0.1, massas)

    def conta():
        ka, kb, kc, kd = C["s09.a"], C["s09.b"], C["s09.c"], C["s09.d"]
        E.frase(c, t, ka, ps("quantas vezes a massa da", "i", 80) + [("Terra", "g", 80, COR)] + ps("é maior?", "i", 80), W / 2, 200, "center", 0.11)
        fcen(c, t, kb, "6 ÷ 7,4", 560, 500, 130)
        E.frase(c, t, lerp(kb, kc, 0.3), ps("tirando a vírgula do divisor", "i", 60), 1320, 350, "center", 0.09)
        if t >= kc - 0.3:
            q = ep(t, kc - 0.3, 0.5)
            M.arrow(c, 830, 455, 1010, 455, COR, q, 7, 22, q)
        fcen(c, t, kc, "60 ÷ 74", 1320, 500, 130, COR)
        fcen(c, t, kd, "≈ 0,81", W / 2, 790, 170, COR)
    if C["s09"] - 0.1 <= t:
        E.saida(c, t, C["s10"] - 0.1, conta)

    if t >= C["s10"]:
        ka, kb, kc = C["s10.a"], C["s10.b"], C["s10.c"]
        tr = lerp(kc, C["s10.end"], 0.32)

        def contas():
            fcen(c, t, ka - 0.1, "24 − 22 = 2", 480, 200, 90)
            fcen(c, t, lerp(ka, kb, 0.55), "10^2 = 100", 1320, 200, 100, COR)
            fcen(c, t, kb, "0,81 × 100", W / 2, 370, 100)
            s = 180
            y = 620
            cl = E.casa(s)
            xb = 400
            h1, h2 = lerp(kb, kc, 0.5), lerp(kb, kc, 0.75)
            E.foco(c, t, kb + 0.4, 0.5, lambda a: (E.anda(c, t, "81", 0, [(h1, 1), (h2, 2)], xb, y, s, some=True),
                                                   E.saida(c, t, h1 + 0.2, lambda: centro(c, "0", xb - cl * 0.5, y, s, "g", TINTA))))
            E.frase(c, t, lerp(kb, kc, 0.3), ps("a vírgula anda", "i", 66) + [("duas casas", "g", 62, COR)], 520, 800, "center", 0.1)
            E.foco(c, t, kc, 0.6, lambda a: (terra(c, 1040, 620, 140, a), centro(c, "=", 1240, 650, 100, "g", TINTA, a)))
            for i in range(81):
                E.foco(c, t, kc + 0.2 + i * 0.015, 0.25, lambda a, i=i: lua(c, 1340 + (i % 9) * 44, 444 + (i // 9) * 44, 19, a), blur=4, sobe=4)
            E.frase(c, t, kc, [("cerca de 81 vezes", "g", 92, COR)], W / 2, 950, "center")
        E.saida(c, t, tr, contas)
        E.frase(c, t, tr + 0.2, ps("a frente ficou abaixo de 1", "i", 84), W / 2, 380, "center", 0.11)
        E.frase(c, t, lerp(tr, C["s10.end"], 0.3), ps("mas a pergunta pede um", "i", 84) + [("número comum", "g", 84, COR)], W / 2, 520, "center", 0.11)
        E.frase(c, t, lerp(tr, C["s10.end"], 0.68), ps("aqui não precisa da forma", "i", 84), W / 2, 660, "center", 0.11)


# ---------------- somar ----------------
def b_soma(c, t, C, b):
    def notas():
        ka, kb, kc, kd = C["s11.a"], C["s11.b"], C["s11.c"], C["s11.d"]
        E.frase(c, t, C["s11"] + 0.1, [("somar é diferente", "g", 84, COR)], W / 2, 150, "center")
        fcen(c, t, ka, "3 × 10^5", 620, 340, 130)
        fcen(c, t, kb, "+ 8 × 10^4", 1270, 340, 130)
        E.frase(c, t, lerp(kb, kc, 0.55), ps("imagine notas", "i", 80), W / 2, 470, "center", 0.11)
        for i in range(3):
            E.foco(c, t, kc + i * 0.2, 0.4, lambda a, i=i: nota(c, 180 + i * 214, 600, 204, 124, "100 mil", E.COR, a))
        cen(c, t, kc + 0.3, "3 notas de cem mil", 490, 880, 58, COR, "i")
        for i in range(8):
            E.foco(c, t, kd + i * 0.1, 0.4, lambda a, i=i: nota(c, 900 + (i % 4) * 196, 540 + (i // 4) * 130, 182, 112, "10 mil", TINTA2, a))
        cen(c, t, kd + 0.3, "8 notas de dez mil", 1282, 880, 58, TINTA2, "i")
    E.saida(c, t, C["s12"] - 0.1, notas)

    def valores():
        ka, kb, kc, kd = C["s12.a"], C["s12.b"], C["s12.c"], C["s12.d"]
        E.frase(c, t, ka, ps("as notas têm", "i", 92) + [("valores diferentes", "g", 92, COR)], W / 2, 200, "center", 0.14)
        E.frase(c, t, lerp(ka, kb, 0.5), ps("não dá para juntar 3 com 8", "i", 76), W / 2, 330, "center", 0.11)
        E.foco(c, t, kb, 0.5, lambda a: E.pilula(c, "só funciona com o mesmo expoente", W / 2, 510, 80, "g", a=a, cor=E.SOBRE))
        fcen(c, t, kc, "300.000 + 80.000", W / 2, 760, 130)
        fcen(c, t, kd, "= 380.000", W / 2, 930, 130, CERTO)
    if C["s12"] - 0.1 <= t:
        E.saida(c, t, C["s13"] - 0.1, valores)

    def igualar():
        ka, kb, kc = C["s13.a"], C["s13.b"], C["s13.c"]
        tf, tp = lerp(kc, C["s13.end"], 0.42), lerp(kc, C["s13.end"], 0.62)
        E.frase(c, t, ka, [("iguale os expoentes,", "g", 84, COR)] + ps("passando para o maior", "i", 84), W / 2, 170, "center", 0.12)
        fcen(c, t, kb, "8 × 10^4", 560, 400, 140)
        if t >= kc - 0.3:
            q = ep(t, kc - 0.3, 0.5)
            M.arrow(c, 880, 350, 1010, 350, COR, q, 7, 22, q)
        fcen(c, t, kc, "0,8 × 10^5", 1370, 400, 140, COR)
        compensa(c, t, tf, tp, W / 2, 560, 760)
        E.frase(c, t, tf, ps("frente", "i", 62) + [("10 vezes menor", "g", 58, COR)], 460, 880, "center", 0.12)
        E.frase(c, t, tp, ps("potência", "i", 62) + [("10 vezes maior", "g", 58, COR)], 1460, 880, "center", 0.12)
        E.frase(c, t, lerp(kc, C["s13.end"], 0.86), [("o valor é o mesmo", "g", 72, CERTO)], W / 2, 980, "center")
    if C["s13"] - 0.1 <= t:
        E.saida(c, t, C["s14"] - 0.1, igualar)

    if t >= C["s14"]:
        ka, kb, kc = C["s14.a"], C["s14.b"], C["s14.c"]
        E.frase(c, t, C["s14"] + 0.1, ps("mesmo expoente: some os da frente", "i", 80), W / 2, 200, "center", 0.11)
        fcen(c, t, ka, "3 + 0,8 = 3,8", W / 2, 400, 130)
        E.cientifica(c, t, kb, "3,8", 5, W / 2, 660, 200, cor=COR, align="center")
        E.foco(c, t, kc, 0.5, lambda a: (centro(c, "380.000", W / 2 - 60, 880, 130, "g", TINTA, a), E.selo(c, W / 2 + 300, 835, 62, True, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    ka, kb, kc, kd, ke = C["s15.a"], C["s15.b"], C["s15.c"], C["s15.d"], C["s15.e"]

    def um():
        E.frase(c, t, C["s15"] + 0.1, ps("o erro do começo:", "i", 80), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("somar os da frente", "i", 84) + [("sem igualar", "g", 84, ERRADO)], W / 2, 280, "center", 0.11)
        fcen(c, t, lerp(ka, kb, 0.72), "11 × 10^5", W / 2, 460, 130, ERRADO)
        fcen(c, t, kb, "= 1.100.000", W / 2, 620, 130, ERRADO)
        fcen(c, t, kc - 0.9, "300.000 + 80.000", W / 2, 790, 100)
        E.frase(c, t, kc, ps("não chega nem a", "i", 84) + [("meio milhão", "g", 84, COR)], W / 2, 930, "center", 0.11)
    E.saida(c, t, kd - 0.1, um)
    if t >= kd:
        for k, y, op, s, cor, ok in ((kd, 340, "× ÷", "não pedem expoente igual", TINTA, True), (ke, 660, "+ −", "pedem expoente igual", COR, False)):
            E.foco(c, t, k, 0.5, lambda a, op=op, y=y: E.pilula(c, op, 400, y, 110, "g", a=a, cor=E.SOBRE))
            E.frase(c, t, k + 0.1, [(s, "g", 76, cor)], 620, y + 26)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def regra():
        ka, kb, kc, kd, ke = C["s16.a"], C["s16.b"], C["s16.c"], C["s16.d"], C["s16.e"]
        E.frase(c, t, C["s16"] + 0.1, ps("o atalho da multiplicação", "i", 76, CLARO), W / 2, 150, "center", 0.11)
        E.frase(c, t, ka, ps("ache o expoente", "g", 96, BR) + ps("antes da conta", "i", 96, CLARO), W / 2, 280, "center", 0.14)
        for k, n, s, y in ((kb, "1", "some os expoentes", 460), (kc, "2", "se a frente der 10 ou mais", 590), (kd, "3", "some mais um", 720)):
            E.foco(c, t, k, 0.5, lambda a, n=n, y=y: (E.bola(c, 400, y - 24, 46, a=a), centro(c, n, 400, y - 4, 56, "g", E.SOBRE, a)))
            E.frase(c, t, k + 0.1, [(s, "g", 76, BR)], 480, y)
        E.frase(c, t, lerp(kd, ke, 0.3), ps("3 vezes 4 passou de 10:", "i", 72, CLARO), 620, 910, "center", 0.11)
        fcen(c, t, ke, "7 + 1 = 8", 1330, 915, 120, CLARO)
    E.saida(c, t, C["s17"] - 0.1, regra)
    if t < C["s17"]:
        return
    ka, kb, kc, kd = C["s17.a"], C["s17.b"], C["s17.c"], C["s17.d"]
    E.frase(c, t, C["s17"] + 0.1, ps("cada número da frente é", "i", 76, CLARO) + [("menor que 10", "g", 72, BR)], W / 2, 190, "center", 0.11)
    E.frase(c, t, ka, ps("o produto fica", "i", 92, CLARO) + [("abaixo de 100", "g", 92, BR)], W / 2, 340, "center", 0.12)
    E.frase(c, t, kb, ps("basta", "i", 92, CLARO) + [("um ajuste", "g", 92, BR)], W / 2, 470, "center", 0.12)
    E.foco(c, t, kc, 0.5, lambda a: E.pilula(c, "serve para eliminar alternativas", W / 2, 620, 76, "g", a=a, cor=E.SOBRE))
    E.foco(c, t, kd, 0.5, lambda a: E.selo(c, 340, 820, 66, False, a))
    E.frase(c, t, kd + 0.1, ps("não compensa na soma:", "i", 76, CLARO), 440, 800, "left", 0.1)
    E.frase(c, t, lerp(kd, C["s17.end"], 0.6), [("aí, iguale os expoentes", "g", 76, BR)], 440, 900)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s18"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 170, passo=0.12)
    ka, kb, kc = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, ka - 0.5, ps("uma fábrica produz", "i", 76), XE, 310, passo=0.1)
    E.formula_em(c, t, ka, "6 × 10^4", XE, 430, 110, cor=COR)
    E.frase(c, t, ka + 1.0, ps("garrafas por dia", "i", 76), XE + 400, 430, passo=0.1)
    E.frase(c, t, kb - 0.6, ps("funcionou por", "i", 76), XE, 570, passo=0.1)
    E.formula_em(c, t, kb, "5 × 10^2", XE, 690, 110, cor=COR)
    E.frase(c, t, kb + 1.0, ps("dias", "i", 76), XE + 400, 690, passo=0.1)
    E.frase(c, t, kc, ps("quantas garrafas produziu,", "i", 84) + [("em notação científica?", "g", 76, COR)], W / 2, 880, "center", 0.1)
    E.relogio(c, t, C["s19.a"], 1520, 330, 170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ka, kb, kc = C["s20.a"], C["s20.b"], C["s20.c"]
    a1, b1, c1, d1 = C["s21.a"], C["s21.b"], C["s21.c"], C["s21.d"]
    s, y = 130, 610

    def contas():
        fcen(c, t, ka, "6 × 5 = 30", 500, 240, 110)
        fcen(c, t, kb, "4 + 2 = 6", 1320, 240, 110)
        fcen(c, t, lerp(kb, kc, 0.62), "10^6", 1320, 390, 110, COR)
    E.saida(c, t, c1 - 0.1, contas)
    E.saida(c, t, a1 - 0.2, lambda: E.frase(c, t, kc - 0.5, ps("ficou", "i", 80), 400, y, "left"))
    cl = E.casa(s)
    x = 640
    if t < a1 + 0.9:
        conserta(c, t, "30", 6, 7, x, y, s, kc, a1, 1e9, terro=lerp(kc, C["s21"], 0.9))
    else:
        conserta3(c, t, x, y, s, a1 + 0.9, lerp(b1, c1, 0.5))
    E.frase(c, t, lerp(C["s21"], a1, 0.1), ps("30 passa de 10", "i", 70, ERRADO), 1480, y - 20, "center", 0.11)
    E.cientifica(c, t, c1, "3", 7, W / 2, 880, 170, cor=COR, align="center")
    E.frase(c, t, c1 + 1.2, ps("garrafas", "i", 90), W / 2 + 340, 880, "left")
    E.foco(c, t, d1, 0.5, lambda a: E.pilula(c, "30 milhões", W / 2, 990, 66, "g", a=a, cor=E.SOBRE))


def conserta3(c, t, x, y, s, t0, tc):
    """depois de a vírgula andar, o 3,0 vira 3: o zero e a vírgula somem, e a conta fica no lugar"""
    k = s / 170
    cl = E.casa(s)
    xf = x + 2 * cl + 44 * k - cl * ease_io(prog(t, t0 + 0.2, 0.5))
    wf = E.formula(c, "× 10", 0, 0, s, a=0)
    xe = xf + wf
    E._digito(c, "3", x + 0.5 * cl, y, s, "g", TINTA, 1.0)
    E.saida(c, t, t0, lambda: (E._digito(c, "0", x + 1.5 * cl, y, s, "g", TINTA, 1.0), E._virgula(c, x + cl, y, s, COR, 1.0)))
    E.formula(c, "× 10", xf, y, s)
    E.formula(c, "^6", xe, y, s)
    E.corta(c, t, tc, xe + 30 * k, y - 106 * k, 76 * k)
    E.foco(c, t, tc + 0.3, 0.4, lambda a: E.formula(c, "^7", xe + 66 * k, y, s, cor=COR, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 170, "center")
        for i, (k, s) in enumerate((("s22.a", "multiplicar soma expoentes"), ("s22.b", "dividir subtrai"), ("s22.c", "mais ou menos pede expoente igual"), ("s22.d", "a frente fica de 1 até menos de 10"))):
            y = 330 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 260, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, [(s, "g", 76)], 350, y)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"] + 0.1, ps("na próxima aula", "i", 84), XE, 240, passo=0.14)
    E.frase(c, t, C["s23.a"], [("ordem de grandeza", "g", 130, COR)], XE, 390)
    E.frase(c, t, lerp(C["s23.a"], C["s23.b"], 0.3), ps("a potência de 10 mais próxima de um número", "i", 70), XE, 500, passo=0.08)
    E.frase(c, t, C["s23.b"] - 0.9, ps("e por que a referência é", "i", 76) + [("3,16", "g", 90, COR)], XE, 610, passo=0.09)
    E.foco(c, t, C["s23.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 750, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s23.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(990, 775, p), ep(t, C["s23.c"] + 0.2, 0.4))
    E.frase(c, t, C["s23.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 930, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, multiplicar=b_multiplicar, terra=b_terra, soma=b_soma, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
