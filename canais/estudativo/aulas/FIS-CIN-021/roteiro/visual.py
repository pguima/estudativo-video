"""Visual — Estudativo · FIS-CIN-021: praticando movimento circular (aula de prática, 5 situações). Última aula da trilha.

Segue a LINGUAGEM VISUAL DA FÍSICA do cabeçalho de FIS-CIN-001/roteiro/visual.py e a do MOVIMENTO CIRCULAR do cabeçalho de
FIS-CIN-018/roteiro/visual.py. Cada situação: enunciado à esquerda e desenho à direita; na cena "pause o vídeo", o relógio
toma o lugar do desenho. Frequência em violeta (F.ACEL), velocidade linear em petróleo (F.VEL), período em laranja.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Cinemática")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-CIN-021_praticando_movimento_circular.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
FREQ = F.ACEL

# todas as contas da aula (π = 3)
assert 600 / 60 == 10 and 1 / 10 == 0.1 and 60 / 600 == 0.1
assert 2 * 60 == 120 and abs(2 * 3 / 120 - 0.05) < 1e-12 and abs(0.05 * 20 - 1) < 1e-12 and 2 * 3 * 20 == 120 and 120 / 120 == 1
assert 3000 * 2 == 6000 and 6000 / 6 == 1000
assert 45 / 15 == 3 and abs(2 * 3 * 3 * 0.3 - 5.4) < 1e-9 and abs(5.4 * 3.6 - 19.44) < 1e-9


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def promessa(c, t, C, cena, itens, size=76):
    """“até o fim da aula” + itens numerados [(cue, texto)] + a órbita da Física à direita"""
    tb = C[cena + ".a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena + ".a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    passo_y = 150 if len(itens) <= 3 else 128
    for i, (k, s) in enumerate(itens):
        y = 430 + i * passo_y
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 28, 38, a=a), centro(c, str(i + 1), XE + 40, y - 6, 48, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", size, COR if i == 0 else TINTA)], XE + 110, y)


def lembrete(c, t, C, cena, itens, num="2", titulo=("coisas",)):
    """você precisa de N coisas: itens = [(cue, linha fina, linha forte, desenho(a, x, y) ou None)]"""
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de", "i", 80), XE, 380, passo=0.14)
    t1 = C[itens[0][0]] - 0.6 if num is None else C[cena + ".a"]
    if num:
        E.foco(c, t, t1, 0.5, lambda a: E.escreve(c, num, XE - 8, 700, 320, "g", COR, a))
        E.foco(c, t, t1 + 0.15, 0.5, lambda a: E.escreve(c, titulo[0], XE + 205, 680, 110, "i", TINTA, a))
    else:
        for j, s in enumerate(titulo):
            E.frase(c, t, t1 + 0.2 * j, [(s, "g", 110, COR)], XE, 540 + 130 * j)
    n = len(itens)
    x, w = 820, 1000
    h = 230 if n == 2 else 190
    gap = 290 if n == 2 else 225
    y0 = 230 if n == 2 else 150
    for i, (k, l1, l2, des) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 54)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 54, COR)], x + 44, y + h * 0.75)
        if des:
            E.foco(c, t, C[k] + 0.6, 0.5, lambda a, des=des, y=y: des(a, x + w - 170, y + h / 2))
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 52, COR) + ps("procure no canal", "i", 52),
            820, y0 + n * gap + 20, "left", 0.12)


def fim(c, t, C, cr, itens, cp, linhas, desenho, k_insc, k_bons):
    """resumo numerado (cena cr, itens = [(cue, partes)]) e a ponte (cena cp): linhas = [(cue, partes)], desenho(a) à esquerda embaixo"""
    def resumo():
        E.frase(c, t, C[cr], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C[cp] - 0.1, resumo)
    if t < C[cp]:
        return
    E.frase(c, t, C[cp], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    for i, (k, partes) in enumerate(linhas):
        E.frase(c, t, C[k], partes, XE, 400 + 140 * i, passo=0.12)
    desenho()
    E.foco(c, t, C[k_insc], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[k_insc] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[k_insc] + 0.2, 0.4))
    E.frase(c, t, C[k_bons], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


# ---------------- peças desta aula ----------------
def situacao(c, t, C, cq, cp, n, linhas, desenho):
    """tela de enunciado: "situação n" + linhas [(instante, partes, y)]; desenho() à direita até a cena da pausa cp"""
    E.frase(c, t, C[cq + ".a"], [("situação", "i", 70, COR), (str(n), "g", 76, COR)], XE, 200, passo=0.12)
    for ti, partes, y in linhas:
        E.frase(c, t, ti, partes, XE, y, passo=0.12)
    if t < C[cp]:
        desenho()
    else:
        E.relogio(c, t, C[cp + ".a"], cx=1460, cy=440, r=200)


def polia(c, cx, cy, r, ang, a=1.0, cor=None, raios=3, escuro=False, marca=True):
    """polia de frente: aro, raios girando (ang em graus) e uma marca laranja na borda (copiada de FIS-CIN-020)"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA
    c.drawCircle(cx, cy, r, M.paint("#FFF7EF" if not escuro else "#1A1A24", a))
    c.drawCircle(cx, cy, r, M.paint(cor or tinta, a, stroke=max(6, r * 0.08)))
    for k in range(raios):
        g = math.radians(ang + 360 * k / raios)
        M.line(c, cx, cy, cx + math.cos(g) * r * 0.9, cy - math.sin(g) * r * 0.9, tinta, a * 0.7, 4)
    c.drawCircle(cx, cy, max(8, r * 0.08), M.paint(tinta, a))
    if marca:
        g = math.radians(ang)
        E.bola(c, cx + math.cos(g) * r, cy - math.sin(g) * r, max(12, r * 0.09), None, a)


def tangentes(A, ra, B, rb):
    dx, dy = B[0] - A[0], B[1] - A[1]
    d = math.hypot(dx, dy)
    th = math.atan2(dy, dx)
    phi = math.acos(max(-1.0, min(1.0, (ra - rb) / d)))
    out = []
    for s in (1, -1):
        al = th + s * phi
        out.append(((A[0] + ra * math.cos(al), A[1] + ra * math.sin(al)), (B[0] + rb * math.cos(al), B[1] + rb * math.sin(al))))
    return out


def correia(c, A, ra, B, rb, fase, a=1.0, cor=None, largura=8):
    """correia aberta (copiada de FIS-CIN-020)"""
    if a <= 0:
        return
    cor = cor or TINTA
    for i, (P, Q) in enumerate(tangentes(A, ra, B, rb)):
        pt = M.paint(cor, a, stroke=largura)
        pt.setPathEffect(skia.DashPathEffect.Make([34, 16], (fase if i == 0 else -fase) % 50))
        path = skia.Path(); path.moveTo(*P); path.lineTo(*Q)
        c.drawPath(path, pt)
    for X, r in ((A, ra), (B, rb)):
        c.drawCircle(X[0], X[1], r + largura / 2, M.paint(cor, a * 0.85, stroke=largura * 0.5))


def engrenagem(c, cx, cy, r, n, ang, a=1.0, cor=None):
    """engrenagem de n dentes (copiada de FIS-CIN-020)"""
    if a <= 0:
        return
    cor = cor or TINTA2
    p = skia.Path()
    h = r * 0.14 if n > 14 else r * 0.2
    for k in range(n * 4 + 1):
        g = math.radians(ang + 360 * k / (n * 4))
        rr = r if (k % 4) in (1, 2) else r - h
        x, y = cx + math.cos(g) * rr, cy - math.sin(g) * rr
        p.moveTo(x, y) if k == 0 else p.lineTo(x, y)
    p.close()
    c.drawPath(p, M.paint(cor, a))
    c.drawCircle(cx, cy, r * 0.55, M.paint("#FFF7EF", a))
    c.drawCircle(cx, cy, r * 0.12, M.paint(cor, a))


def roda_bike(c, cx, cy, R, ang, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, R, M.paint("#1B1B20", a, stroke=R * 0.07))
    for k in range(16):
        g = math.radians(ang + 22.5 * k)
        M.line(c, cx, cy, cx + math.cos(g) * R * 0.96, cy - math.sin(g) * R * 0.96, TINTA2, a * 0.6, 2)
    g = math.radians(ang)
    E.bola(c, cx + math.cos(g) * R, cy - math.sin(g) * R, 16, None, a)


def transmissao(c, t, x1, x2, y, r1, r2, n1, n2, R, giros_pedal, a=1.0):
    """bicicleta: coroa com pedal, corrente, catraca no eixo da roda (copiada de FIS-CIN-020)"""
    if a <= 0:
        return
    ang1 = 90 - 360 * giros_pedal
    ang2 = 90 - 360 * giros_pedal * n1 / n2
    roda_bike(c, x2, y, R, ang2, a * 0.9)
    correia(c, (x1, y), r1, (x2, y), r2, 360 * giros_pedal * r1 * math.pi / 180, a, TINTA, 7)
    engrenagem(c, x1, y, r1, n1 // 2, ang1, a, E.COR)
    engrenagem(c, x2, y, r2, max(8, n2 // 2), ang2, a, E.COR)
    g = math.radians(ang1 + 180)
    P = (x1 + math.cos(g) * r1 * 1.3, y - math.sin(g) * r1 * 1.3)
    M.line(c, x1, y, *P, TINTA, a, 12)
    M.rrect(c, P[0] - 34, P[1] - 10, 68, 20, 6, TINTA, a)


def maquina(c, cx, cy, s, giro, a=1.0):
    """máquina de lavar de frente, com o cesto girando"""
    if a <= 0:
        return
    M.rrect(c, cx - 200 * s, cy - 240 * s, 400 * s, 480 * s, 24 * s, "#E9E6E0", a)
    M.rrect(c, cx - 200 * s, cy - 240 * s, 400 * s, 80 * s, 24 * s, "#D2CEC6", a)
    c.drawCircle(cx + 130 * s, cy - 200 * s, 18 * s, M.paint(TINTA2, a))
    c.drawCircle(cx, cy + 40 * s, 150 * s, M.paint(TINTA, a, stroke=14 * s))
    c.drawCircle(cx, cy + 40 * s, 130 * s, M.paint("#BFD4E6", a))
    for k in range(3):
        g = math.radians(giro + 120 * k)
        c.drawCircle(cx + math.cos(g) * 80 * s, cy + 40 * s - math.sin(g) * 80 * s, 22 * s, M.paint(E.COR, a))


def roda_gigante(c, cx, cy, R, ang, a=1.0):
    if a <= 0:
        return
    M.line(c, cx, cy, cx - R * 0.55, cy + R * 1.25, TINTA2, a, 10)
    M.line(c, cx, cy, cx + R * 0.55, cy + R * 1.25, TINTA2, a, 10)
    c.drawCircle(cx, cy, R, M.paint(TINTA, a, stroke=7))
    for k in range(8):
        g = math.radians(ang + 45 * k)
        X, Y = cx + math.cos(g) * R, cy - math.sin(g) * R
        M.line(c, cx, cy, X, Y, TINTA2, a * 0.6, 3)
        M.rrect(c, X - 22, Y, 44, 40, 8, E.COR if k == 0 else E.mix(E.COR, BR, 0.6), a)
    c.drawCircle(cx, cy, 12, M.paint(TINTA, a))


def terra(c, cx, cy, R, a=1.0, giro=0.0):
    """a Terra com o eixo, o equador e um paralelo perto do polo"""
    if a <= 0:
        return
    E.bola(c, cx, cy, R, "#2F7FC1", a)
    for dx, dy, k in ((-0.3, -0.2, 0.3), (0.25, 0.25, 0.22), (0.35, -0.35, 0.15)):
        c.drawCircle(cx + dx * R + math.sin(giro) * 10, cy + dy * R, k * R, M.paint("#4FA35A", 0.7 * a))
    M.line(c, cx, cy - R * 1.25, cx, cy + R * 1.25, TINTA, a, 5, dash=E.TRACO)
    c.drawOval(skia.Rect.MakeXYWH(cx - R, cy - R * 0.12, 2 * R, R * 0.24), M.paint(BR, a, stroke=4))
    c.drawOval(skia.Rect.MakeXYWH(cx - R * 0.35, cy - R * 0.94 - R * 0.05, R * 0.7, R * 0.1), M.paint(BR, a, stroke=4))


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.foco(c, t, C["s01.a"], 0.6, lambda a: E.escreve(c, "5", XE - 10, 560, 400, "g", COR, a))
    E.frase(c, t, C["s01.a"] + 0.3, [("situações", "g", 110)], XE + 300, 470)
    E.frase(c, t, C["s01.a"] + 0.9, ps("rotação, polias, bicicleta e a Terra", "i", 60), XE + 300, 570, passo=0.1)
    E.foco(c, t, C["s01.b"], 0.5, lambda a: E.pilula(c, "pause e resolva antes", XE + 640, 780, 60, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s01.b"] + 0.4, 0.6, lambda a: E.simbolo(c, 1600, 300, 150 * a, giro=12 * math.sin(t * 0.4)), blur=0)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 84), XE, 200, passo=0.14)
    itens = (("s02.a", [("T = 1 ÷ f", "g", 60, COR), ("e", "i", 62), ("rpm ÷ 60 = Hz", "g", 60, FREQ)]),
             ("s02.b", [("ω = 2π ÷ T", "g", 60, FREQ), ("e", "i", 62), ("v = ω · R", "g", 60, F.VEL)]),
             ("s02.c", [("correia:", "g", 60), ("v", "g", 60, F.VEL), ("igual;", "i", 62), ("eixo:", "g", 60), ("ω", "g", 60, FREQ), ("igual", "i", 62)]))
    for i, (k, partes) in enumerate(itens):
        y = 380 + i * 170
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 30, y - 22, 30, a=a), centro(c, str(i + 1), XE + 30, y - 4, 38, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, XE + 90, y, passo=0.1)
    E.frase(c, t, lerp(C["s02.c"], C["s02.end"], 0.6), ps("travou?", "i", 52, COR) + ps("procure a aula no canal", "i", 52), XE + 90, 920, "left", 0.1)


# ---------------- situação 1: máquina de lavar ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C, "s03", "s04", 1, [
        (C["s03.a"] + 0.6, ps("centrifugação:", "i", 66), 330),
        (C["s03.b"], [("600", "g", 90), ("rpm", "b", 60, F.UNID)], 460),
        (C["s03.c"], [("frequência", "g", 70), ("em", "i", 70), ("Hz?", "g", 70, FREQ)], 640),
        (C["s03.d"], [("período?", "g", 70, COR)], 760)],
        lambda: E.foco(c, t, C["s03.a"], 0.5, lambda a: maquina(c, 1460, 560, 1.0, t * 720, a)))


def b_resposta1(c, t, C, b):
    E.formula_em(c, t, C["s05.a"], "f{600}{60} =", XE, 330, 90, "g", TINTA)
    bola_txt(c, t, C["s05.b"], "10 Hz", XE + 500, 305, 110, 56, FREQ)
    E.frase(c, t, C["s05.b"] + 0.8, ps("10 voltas por segundo", "i", 54, TINTA2), XE + 680, 320, passo=0.1)
    E.formula_em(c, t, C["s05.c"], "T = f{1}{10} =", XE, 600, 90, "g", TINTA)
    bola_txt(c, t, C["s05.d"], "0,1 s", XE + 600, 575, 110, 56)
    E.foco(c, t, lerp(C["s05.d"], C["s05.end"], 0.4), 0.5, lambda a: E.pilula(c, "atalho: 60 ÷ 600 = 0,1 s", XE + 450, 820, 54, "g", fundo=E.COR, a=a))


# ---------------- situação 2: roda-gigante ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C, "s06", "s07", 2, [
        (C["s06.a"] + 0.6, ps("roda-gigante", "i", 66), 330),
        (C["s06.b"], [("R = 20 m", "g", 66, COR)], 440),
        (C["s06.c"], [("1", "g", 66), ("volta", "i", 66), ("a", "i", 66), ("cada", "i", 66), ("2 min", "g", 66, COR)], 540),
        (C["s06.d"], [("velocidade", "g", 66), ("da", "i", 66), ("cabine?", "g", 66, F.VEL)], 700),
        (C["s06.d"] + 1.6, [("em", "i", 56, TINTA2), ("m/s,", "g", 52, TINTA2), ("π = 3", "b", 52, TINTA2)], 800)],
        lambda: E.foco(c, t, C["s06.a"], 0.5, lambda a: roda_gigante(c, 1460, 460, 280, 90 + (t - C["s06.a"]) * 8, a)))


def b_resposta2(c, t, C, b):
    def s08():
        E.formula_em(c, t, C["s08.a"], "2 min = 120 s", XE, 260, 76, "g", COR)
        E.formula_em(c, t, C["s08.b"], "ω = f{2 · 3}{120} =", XE, 450, 84, "g", TINTA)
        bola_txt(c, t, C["s08.c"], "0,05 rad/s", XE + 850, 425, 120, 40, FREQ)
        E.formula_em(c, t, C["s08.d"], "v = 0,05 · 20 =", XE, 680, 84, "g", TINTA)
        bola_txt(c, t, C["s08.e"], "1 m/s", XE + 850, 655, 110, 56, F.VEL)
        E.frase(c, t, lerp(C["s08.e"], C["s08.end"], 0.4), ps("devagar, como um passeio", "i", 54, TINTA2), XE, 860, passo=0.1)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], ps("pelo caminho direto:", "i", 66), XE, 260, passo=0.12)
    E.formula_em(c, t, C["s09.a"], "v = f{2 · π · R}{T} = f{2 · 3 · 20}{120} = f{120}{120}", XE, 480, 76, "g", TINTA)
    bola_txt(c, t, C["s09.b"], "1 m/s", XE + 400, 720, 110, 56, F.VEL)
    E.frase(c, t, C["s09.b"] + 0.8, ps("os dois caminhos batem", "g", 56, CERTO), XE + 600, 740, passo=0.1)


# ---------------- situação 3: liquidificador ----------------
def b_questao3(c, t, C, b):
    A, ra, B, rb = (1260, 620), 70, (1660, 620), 210

    def desenho():
        s = max(0.0, t - C["s10.a"]) * 200.0
        E.foco(c, t, C["s10.b"], 0.5, lambda a: polia(c, *A, ra, 90 - math.degrees(s / ra), a))
        E.foco(c, t, C["s10.d"], 0.5, lambda a: (polia(c, *B, rb, 90 - math.degrees(s / rb), a), correia(c, A, ra, B, rb, s, a)))
        E.foco(c, t, C["s10.b"] + 0.4, 0.4, lambda a: centro(c, "2 cm", A[0], A[1] + ra + 80, 50, "g", TINTA, a))
        E.foco(c, t, C["s10.c"], 0.4, lambda a: centro(c, "3000 rpm", A[0], A[1] - ra - 50, 50, "g", FREQ, a))
        E.foco(c, t, C["s10.d"] + 0.4, 0.4, lambda a: (centro(c, "6 cm", B[0], B[1] + rb + 70, 50, "g", TINTA, a), centro(c, "? rpm", B[0], B[1] - rb - 40, 50, "g", FREQ, a)))
    situacao(c, t, C, "s10", "s11", 3, [
        (C["s10.a"] + 0.6, ps("motor de liquidificador", "i", 62), 330),
        (C["s10.b"], [("polia", "i", 62), ("de", "i", 62), ("2 cm,", "g", 62)], 430),
        (C["s10.c"], [("3000", "g", 62, FREQ), ("rpm", "b", 48, F.UNID)], 520),
        (C["s10.d"], [("correia", "i", 62), ("até", "i", 62), ("6 cm", "g", 62)], 620),
        (C["s10.e"], [("rpm", "g", 66), ("da", "i", 66), ("maior?", "g", 66, COR)], 780)], desenho)


def b_resposta3(c, t, C, b):
    E.foco(c, t, C["s12.a"], 0.5, lambda a: E.pilula(c, "correia: f · R igual", XE + 280, 260, 56, "g", fundo=F.VEL, a=a))
    E.formula_em(c, t, C["s12.b"], "3000 · 2 = f · 6", XE, 470, 90, "g", TINTA)
    E.formula_em(c, t, C["s12.c"], "f = f{6000}{6} =", XE, 670, 90, "g", TINTA)
    bola_txt(c, t, C["s12.c"] + 1.4, "1000 rpm", XE + 720, 645, 120, 46, FREQ)
    E.frase(c, t, C["s12.d"], [("raio", "i", 60), ("3×", "g", 60, COR), ("maior", "i", 60), ("→", "g", 60), ("3×", "g", 60, COR), ("mais", "i", 60), ("devagar", "i", 60)], XE, 880, passo=0.1)
    E.frase(c, t, C["s12.d"] + 1.6, ps("sem converter unidades", "i", 50, TINTA2), XE, 960, passo=0.1)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("aqui cabe o atalho:", "i", 70, CLARO), W / 2, 170, "center", 0.12)
    E.frase(c, t, C["s13.a"], ps("antes da conta:", "i", 64, CLARO) + [("como", "g", 64, BR), ("estão", "g", 64, BR), ("ligadas?", "g", 64, BR)], W / 2, 300, "center", 0.1)
    # correia
    if t >= C["s13.b"]:
        s = (t - C["s13.b"]) * 160
        q = ep(t, C["s13.b"], 0.4)
        A, B = (380, 640), (760, 640)
        polia(c, *A, 60, 90 - math.degrees(s / 60), q, escuro=True)
        polia(c, *B, 140, 90 - math.degrees(s / 140), q, escuro=True)
        correia(c, A, 60, B, 140, s, q, CLARO)
        E.foco(c, t, C["s13.b"] + 1.2, 0.4, lambda a: E.pilula(c, "pela borda: v igual", 570, 880, 54, "g", fundo=F.VEL, a=a))
    if t >= C["s13.c"]:
        q = ep(t, C["s13.c"], 0.4)
        ang = 90 - (t - C["s13.c"]) * 60
        polia(c, 1400, 640, 200, ang, q, escuro=True, marca=False)
        polia(c, 1400, 640, 80, ang, q, E.COR, escuro=True, marca=False)
        E.foco(c, t, C["s13.c"] + 1.0, 0.4, lambda a: E.pilula(c, "mesmo eixo: ω igual", 1400, 900, 54, "g", fundo=FREQ, a=a))
    E.frase(c, t, C["s13.end"] - 2.6, ps("isso resolve metade da questão", "i", 56, CLARO), W / 2, 1010, "center", 0.1)


# ---------------- situação 4: bicicleta ----------------
def b_questao4(c, t, C, b):
    def desenho():
        g = max(0.0, t - C["s14.e"]) if t >= C["s14.e"] else 0
        transmissao(c, t, 1220, 1640, 560, 140, 46, 45, 15, 250, g, ep(t, C["s14.a"], 0.5))
    situacao(c, t, C, "s14", "s15", 4, [
        (C["s14.b"], [("coroa", "i", 62), ("45", "g", 62, COR), ("dentes,", "i", 62)], 330),
        (C["s14.c"], [("catraca", "i", 62), ("15", "g", 62, COR)], 420),
        (C["s14.d"], [("roda:", "i", 62), ("R = 0,3 m", "g", 62, COR)], 510),
        (C["s14.e"], [("1", "g", 62), ("pedalada", "i", 62), ("por", "i", 62), ("segundo", "i", 62)], 600),
        (C["s14.f"], [("velocidade", "g", 66), ("em", "i", 66), ("m/s?", "g", 66, F.VEL)], 760),
        (C["s14.f"] + 1.8, [("π = 3", "b", 52, TINTA2)], 850)], desenho)


def b_resposta4(c, t, C, b):
    transmissao(c, t, 1300, 1660, 560, 120, 40, 45, 15, 210, max(0.0, t - C["s16"]) * 0.5, ep(t, C["s16"], 0.5))

    def s16():
        E.frase(c, t, C["s16.a"], [("corrente:", "g", 60, F.VEL), ("45 ÷ 15 = 3", "g", 60)], XE, 260, passo=0.1)
        E.frase(c, t, C["s16.b"], [("eixo:", "g", 60, FREQ), ("roda", "i", 62)], XE, 380, passo=0.1)
        bola_txt(c, t, C["s16.b"] + 1.2, "3 Hz", XE + 460, 360, 80, 50, FREQ)
        E.formula_em(c, t, C["s16.c"], "v = 2 · π · f · R", XE, 560, 72, "g", TINTA)
        E.formula_em(c, t, C["s16.d"], "= 2 · 3 · 3 · 0,3", XE, 690, 72, "g", TINTA)
        bola_txt(c, t, C["s16.e"], "5,4 m/s", XE + 760, 660, 110, 48, F.VEL)
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.formula_em(c, t, C["s17.a"], "5,4 · 3,6 ≈ 19,4 km/h", XE, 330, 80, "g", TINTA)
    E.frase(c, t, C["s17.a"] + 1.6, ps("quase 20 km/h", "g", 60, COR), XE, 450, passo=0.1)
    E.frase(c, t, C["s17.b"] - 1.4, ps("mais rápido sem pedalar mais:", "i", 56), XE, 640, passo=0.1)
    E.foco(c, t, C["s17.b"], 0.5, lambda a: (E.pilula(c, "catraca menor", XE + 210, 760, 50, "g", fundo=E.COR, a=a),
                                             E.pilula(c, "ou coroa maior", XE + 640, 760, 50, "g", fundo=E.COR, a=a)))


# ---------------- situação 5: a Terra ----------------
def b_questao5(c, t, C, b):
    def desenho():
        E.foco(c, t, C["s18.b"], 0.6, lambda a: terra(c, 1460, 560, 260, a, t * 0.5))
        E.foco(c, t, C["s18.c"], 0.4, lambda a: (E.bola(c, 1460 + 255, 560, 20, E.COR, a), E.pilula(c, "equador", 1640, 880, 40, "g", fundo=E.COR, a=a)))
        E.foco(c, t, C["s18.d"], 0.4, lambda a: (E.bola(c, 1460 + 90, 560 - 248, 18, TINTA, a), E.pilula(c, "perto do polo", 1460 + 240, 250, 40, "g", fundo=TINTA, a=a)))
    situacao(c, t, C, "s18", "s19", 5, [
        (C["s18.a"] + 0.8, ps("sem conta:", "i", 62, TINTA2), 300),
        (C["s18.b"], ps("a Terra: 1 volta por dia", "i", 64), 410),
        (C["s18.e"], [("maior", "i", 64), ("velocidade", "i", 64), ("angular?", "g", 64, FREQ)], 640),
        (C["s18.f"], [("maior", "i", 64), ("velocidade", "i", 64), ("linear?", "g", 64, F.VEL)], 760)], desenho)


def b_resposta5(c, t, C, b):
    # vista de cima do polo norte: o equador é o círculo grande; perto do polo, o pequeno. Os dois giram juntos.
    cx, cy, R, r = 1460, 560, 300, 80
    ang = 90 + max(0.0, t - C["s20"]) * 25
    q0 = ep(t, C["s20"], 0.5)
    if q0 > 0:
        E.bola(c, cx, cy, R, "#2F7FC1", q0)
        c.drawCircle(cx, cy, r, M.paint(BR, q0, stroke=4))
        c.drawCircle(cx, cy, 10, M.paint(TINTA, q0))
        E.foco(c, t, C["s20"] + 0.3, 0.4, lambda a: centro(c, "vista de cima do polo", cx, cy - R - 40, 44, "i", TINTA2, a))
    g = math.radians(ang)
    Pe, Pp = (cx + math.cos(g) * R, cy - math.sin(g) * R), (cx + math.cos(g) * r, cy - math.sin(g) * r)
    if t >= C["s20.b"]:
        E.arco(c, cx, cy, R * 0.55, -ang, 40, FREQ, 26, 0.5 * ep(t, C["s20.b"], 0.4))
    if t >= C["s20.c"]:
        q = ep(t, C["s20.c"], 0.4)
        M.line(c, cx, cy, *Pe, E.COR, q, 6)
    E.bola(c, *Pe, 22, E.COR, q0)
    E.bola(c, *Pp, 16, TINTA, q0)
    if t >= C["s20.d"]:
        q = ep(t, C["s20.d"], 0.4)
        tx, ty = -math.sin(g), -math.cos(g)
        F.seta(c, Pe[0], Pe[1], Pe[0] + tx * 230, Pe[1] + ty * 230, F.VEL, q, 10)
        F.seta(c, Pp[0], Pp[1], Pp[0] + tx * 62, Pp[1] + ty * 62, F.VEL, q, 7)
    E.frase(c, t, C["s20.a"], ps("pontos do mesmo corpo:", "i", 62), XE, 280, passo=0.1)
    E.frase(c, t, C["s20.b"], [("mesmo", "g", 70, FREQ), ("ω", "g", 76, FREQ)], XE, 410, passo=0.12)
    E.frase(c, t, C["s20.c"], ps("equador: muito mais", "i", 62) + [("longe", "g", 62, COR)] + ps("do eixo", "i", 62), XE, 570, passo=0.1)
    E.frase(c, t, C["s20.d"], [("v", "g", 76, F.VEL), ("maior", "g", 76), ("no", "i", 70), ("equador", "g", 70, COR)], XE, 720, passo=0.12)
    E.frase(c, t, lerp(C["s20.d"], C["s20.end"], 0.5), ps("o carrossel, em tamanho de planeta", "i", 52, TINTA2), XE, 880, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    itens = (("s21.a", [("rpm", "g", 64), ("÷ 60", "g", 64, COR), ("=", "g", 64), ("Hz", "g", 64, FREQ)]),
             ("s21.b", [("v = ω · R", "g", 64, F.VEL)]),
             ("s21.c", [("a", "i", 66), ("ligação", "g", 64), ("diz", "i", 66), ("o", "i", 66), ("que", "i", 66), ("é", "i", 66), ("igual", "g", 64, COR)]))

    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 175
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 26, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22.a"], [("Cinemática:", "g", 96, COR), ("completa", "i", 96)], XE, 280, passo=0.14)
    E.frase(c, t, C["s22.b"], ps("do movimento uniforme ao circular", "i", 60), XE, 400, passo=0.1)
    E.foco(c, t, C["s22.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1500, 350, 180 * ease_back(prog(t, C["s22.a"] + 0.4, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s22.c"], ps("o que", "i", 70) + [("muda", "g", 70)] + ps("o movimento:", "i", 70), XE, 600, passo=0.12)
    E.frase(c, t, C["s22.c"] + 1.6, [("as", "i", 100), ("forças", "g", 110, COR)], XE, 740, passo=0.14)
    E.foco(c, t, C["s22.c"] + 2.0, 0.5, lambda a: E.pilula(c, "outra trilha do curso", XE + 280, 850, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 600, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(900, 625, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4, resposta4=b_resposta4,
              questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
