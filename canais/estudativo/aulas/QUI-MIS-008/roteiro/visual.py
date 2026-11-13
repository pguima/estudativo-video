"""Visual — Estudativo · QUI-MIS-008: destilação simples e fracionada.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e as convenções da separação de misturas
(QUI-MIS-006/007: aparelho desenhado e animado; o que sai se move). Nesta aula:
- APARELHO DE DESTILAÇÃO (aparelho): balão no fogo, termômetro no alto, condensador inclinado com a camisa de água fria
  (setas azuis: entra por baixo, sai por cima) e o frasco coletor. Vapor = bolinhas brancas com contorno que andam pelo
  caminho; destilado = gotas que pingam. A fracionada ganha a coluna com contas de vidro entre o balão e o condensador.
- TORRE DO PETRÓLEO (torre): mais quente embaixo (âmbar) e mais fria em cima (azul); cada fração sai por um cano à direita,
  no seu nível, com o nome; quanto mais alto, menor o ponto de ebulição.
- Temperatura lida no termômetro = pílula na cor da matéria ao lado do bulbo.
Peças candidatas ao kit: aparelho (destilação simples/fracionada), torre (refino do petróleo), salina.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-008_destilacao_simples_fracionada.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("evaporar", "simples", "fracionada", "petroleo", "alcool", "atalho", "questao", "fim"))
BR = "#FFFFFF"
QUENTE, FRIO = "#E07B12", "#1F6FEB"
PE = {"acetona": 56, "etanol": 78, "água": 100}
assert PE["acetona"] < PE["água"] and PE["etanol"] < PE["água"]  # sai primeiro o de menor PE
FRACOES = ["gás de cozinha", "gasolina", "querosene", "óleo diesel", "óleos lubrificantes", "asfalto"]  # de cima para baixo


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, r=44):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, r, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def riscado(c, t, t0, s, x, y, size=56):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, "i", ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, "i", size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def chama(c, cx, cy, s, a=1.0, t=0.0):
    if a <= 0:
        return
    for k, (cor, f) in enumerate((("#F28C28", 1.0), ("#FFC21A", 0.6))):
        hh = s * f * (1 + 0.08 * math.sin(t * 9 + k))
        p = skia.Path()
        p.moveTo(cx, cy - hh)
        p.cubicTo(cx + s * 0.5 * f, cy - hh * 0.4, cx + s * 0.45 * f, cy, cx, cy)
        p.cubicTo(cx - s * 0.45 * f, cy, cx - s * 0.5 * f, cy - hh * 0.4, cx, cy - hh)
        c.drawPath(p, M.paint(cor, a))


def caminho(pts, u):
    """ponto a uma fração u (0..1) do comprimento de uma linha poligonal"""
    L = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    s = u * sum(L)
    for i, l in enumerate(L):
        if s <= l or i == len(L) - 1:
            f = min(1.0, s / l) if l else 0
            return lerp(pts[i][0], pts[i + 1][0], f), lerp(pts[i][1], pts[i + 1][1], f)
        s -= l


def aparelho(c, t, t0, bx, by, fracionada=False, liquido=Q.AGUA, nivel=0.55, sal=False, tv=None, coleta=0.0, cor_dest=Q.AGUA,
             termo=None, a=1.0, agua_fria=True):
    """destilação: balão em (bx, by); tv = instante em que o vapor começa a andar; coleta 0..1 = líquido no frasco;
    termo = texto da leitura do termômetro (None = sem pílula). Devolve pontos úteis."""
    if t < t0 or a <= 0:
        return None
    q = ep(t, t0, 0.6) * a
    r = 130
    vid = M.paint(Q.VIDRO, q, stroke=5)
    # balão
    c.drawCircle(bx, by, r, M.paint(BR, 0.5 * q))
    c.save(); p = skia.Path(); p.addCircle(bx, by, r - 3); c.clipPath(p, skia.ClipOp.kIntersect, True)
    yl = by + r - 2 * r * nivel
    c.drawRect(skia.Rect.MakeLTRB(bx - r, yl, bx + r, by + r), M.paint(liquido, 0.9 * q))
    if sal:
        rnd = random.Random(4)
        for k in range(12):
            c.drawRect(skia.Rect.MakeXYWH(bx - 70 + rnd.random() * 140, by + r - 30 - rnd.random() * 30, 10, 10), M.paint(BR, q))
    if tv is not None and t >= tv:
        for k in range(8):
            u = (t * 0.9 + k / 8) % 1
            c.drawCircle(bx - 80 + 22 * k, yl + 60 - u * 60, 6 + 4 * u, M.paint(BR, 0.8 * q * (1 - u), stroke=3))
    c.restore()
    c.drawCircle(bx, by, r, vid)
    ytop = by - r - (380 if fracionada else 140)
    for dx in (-22, 22):
        M.line(c, bx + dx, by - r + 8, bx + dx, ytop, Q.VIDRO, q, 5)
    if fracionada:
        for k in range(9):
            yy = by - r - 30 - k * 36
            c.drawCircle(bx - 8 + 14 * (k % 2), yy, 12, M.paint("#C9D6DE", q))
            c.drawCircle(bx - 8 + 14 * (k % 2), yy, 12, M.paint(Q.VIDRO, 0.6 * q, stroke=2))
    # termômetro
    M.line(c, bx, ytop - 80, bx, ytop + 50, "#6E747C", q, 8)
    c.drawCircle(bx, ytop + 54, 11, M.paint("#E5322D", q))
    # braço e condensador
    c0 = (bx + 22, ytop + 20)
    c1 = (bx + 520, ytop + 260)
    M.line(c, c0[0], c0[1], c1[0], c1[1], Q.VIDRO, q, 5)
    ang = math.atan2(c1[1] - c0[1], c1[0] - c0[0])
    j0 = (lerp(c0[0], c1[0], 0.22), lerp(c0[1], c1[1], 0.22))
    j1 = (lerp(c0[0], c1[0], 0.88), lerp(c0[1], c1[1], 0.88))
    nx, ny = -math.sin(ang), math.cos(ang)
    cam = skia.Path()
    cam.moveTo(j0[0] + nx * 40, j0[1] + ny * 40); cam.lineTo(j1[0] + nx * 40, j1[1] + ny * 40)
    cam.lineTo(j1[0] - nx * 40, j1[1] - ny * 40); cam.lineTo(j0[0] - nx * 40, j0[1] - ny * 40); cam.close()
    c.drawPath(cam, M.paint("#CFE9F7", 0.85 * q))
    c.drawPath(cam, vid)
    if agua_fria:
        # entra por baixo (perto de j1, lado de baixo), sai por cima (perto de j0, lado de cima)
        ei = (j1[0] - 40 + nx * 40, j1[1] - 20 + ny * 40)
        so = (j0[0] + 40 - nx * 40, j0[1] + 20 - ny * 40)
        M.arrow(c, ei[0], ei[1] + 70, ei[0], ei[1] + 4, FRIO, q, 6, 20)
        M.arrow(c, so[0], so[1] - 4, so[0], so[1] - 70, FRIO, q, 6, 20)
    # frasco coletor
    fx, fy = c1[0] + 30, c1[1] + 270
    Q.erlenmeyer(c, t, t0, fx, fy, 200, 230, 0.6 * coleta, cor_dest, graduacao=False)
    # chama
    chama(c, bx, by + r + 110, 70, q, t)
    # vapor andando e gotas pingando
    if tv is not None and t >= tv:
        trilha = [(bx, by - r), (bx, ytop + 10), c0, c1]
        for k in range(7):
            u = ((t - tv) * 0.25 + k / 7) % 1
            if t - tv < 4 * (k / 7):
                continue
            x, y = caminho(trilha, u)
            cond = u > 0.62
            if cond:
                E.bola(c, x, y, 8, cor_dest, q)
            else:
                c.drawCircle(x, y, 10, M.paint(BR, 0.9 * q)); c.drawCircle(x, y, 10, M.paint(CINZA, q, stroke=2))
        for k in range(3):
            u = ((t - tv) * 1.2 + k / 3) % 1
            E.bola(c, c1[0], c1[1] + 20 + u * 120, 8, cor_dest, q)
    if termo:
        E.foco(c, t, termo[1], 0.4, lambda aa: E.pilula(c, termo[0], bx + 150, ytop - 70, 46, "g", fundo=E.COR, a=aa * q))
    return dict(ytop=ytop, c0=c0, c1=c1, j0=j0, j1=j1, frasco=(fx, fy))


def salina(c, t, x, y, w, a=1.0, seca=0.0):
    """tanque raso de água do mar ao sol; seca 0..1 baixa a água e mostra o sal"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, 120, 14, "#C9B79A", a)
    hh = 90 * (1 - seca)
    c.drawRect(skia.Rect.MakeXYWH(x + 14, y + 104 - hh, w - 28, hh), M.paint("#8FC9E0", a))
    rnd = random.Random(3)
    for k in range(int(40 * seca)):
        c.drawRect(skia.Rect.MakeXYWH(x + 20 + rnd.random() * (w - 50), y + 92 - rnd.random() * 12, 12, 10), M.paint(BR, a))
    for k in range(10):
        ang = k * math.tau / 10
        M.line(c, x + w - 80 + 70 * math.cos(ang), y - 250 + 70 * math.sin(ang), x + w - 80 + 100 * math.cos(ang), y - 250 + 100 * math.sin(ang), "#F5B400", a, 7)
    E.bola(c, x + w - 80, y - 250, 55, "#FFC21A", a)
    for k in range(4):
        u = (t * 0.35 + k / 4) % 1
        xx = x + 80 + 120 * k
        pth = skia.Path(); pth.moveTo(xx, y - u * 160); pth.cubicTo(xx + 18, y - 20 - u * 160, xx - 18, y - 50 - u * 160, xx, y - 70 - u * 160)
        c.drawPath(pth, M.paint(CINZA, a * (1 - u) * seca * 2 if seca < 0.5 else a * (1 - u), stroke=4))


def torre(c, t, t0, x, y, w, h, tl=None, a=1.0):
    """torre de fracionamento do petróleo; tl[k] = instante do nome de FRACOES[k] (de cima para baixo)"""
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.6) * a
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y), skia.Point(0, y + h)], [M.hexc("#BFD7F2", q), M.hexc("#F6C48E", q)]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), p)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint("#6E747C", q, stroke=6))
    n = len(FRACOES)
    for k in range(1, n):
        yy = y + h * k / n
        M.line(c, x + 10, yy, x + w - 10, yy, "#8A8D94", 0.8 * q, 4)
    for k, nome in enumerate(FRACOES):
        yy = y + h * (k + 0.5) / n
        if tl is not None and t < tl[k]:
            continue
        qq = ep(t, tl[k], 0.4) if tl else 1
        M.line(c, x + w, yy, x + w + 90, yy, "#6E747C", q * qq, 14)
        E.escreve(c, nome, x + w + 110, yy + 16, 46, "g" if k in (0, 1) else "b", TINTA if k else COR, q * qq)
    # entrada do petróleo aquecido
    M.line(c, x - 160, y + h - 60, x, y + h - 60, "#2A2B31", q, 18)
    chama(c, x - 120, y + h + 10, 55, q, t)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.5, lambda a: salina(c, t, 960, 700, 820, a, ep(t, C["s01.a"] + 0.5, 3.0)))
        E.frase(c, t, C["s01.a"], [("na", "i", 90), ("salina", "g", 90, COR)], XE, 330, passo=0.12)
        E.frase(c, t, C["s01.a"] + 0.8, ps("o sol tira a água, o sal fica", "i", 58, TINTA2), XE, 440, passo=0.08)
        E.frase(c, t, C["s01.b"], ps("e se você quisesse", "i", 66), XE, 620, passo=0.1)
        E.frase(c, t, C["s01.b"] + 1.0, [("a", "i", 80), ("água?", "g", 80, COR)], XE, 730, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("muitos navios fazem isso", "i", 58, TINTA2), XE, 900, passo=0.08)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("evaporação", "g", 64), ("ou", "i", 68), ("destilação", "g", 64, COR)]),
                 (C["s02.c"], [("petróleo", "g", 64), ("→", "g", 64, TINTA2), ("gasolina", "g", 64, COR)]),
                 (C["s02.d"], [("o", "i", 68), ("álcool", "g", 64), ("96%", "g", 64, COR)])], XE, 440, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("filtro", "g", 70, COR)] + ps("não separa mistura homogênea", "i", 68), XE, 380, passo=0.1)
    E.frase(c, t, C["s03.b"], [("vaporização", "g", 66), ("líquido → gás;", "b", 60, TINTA2), ("condensação", "g", 66), ("gás → líquido", "b", 60, TINTA2)], XE, 560, passo=0.1)
    E.frase(c, t, C["s03.c"], [("ponto", "g", 70, COR), ("de", "i", 70), ("ebulição", "g", 70, COR)] + [("=", "g", 66, TINTA2)] + ps("a temperatura em que ferve", "i", 66), XE, 740, passo=0.1)


# ---------------- evaporação ----------------
def b_evaporar(c, t, C, b):
    E.frase(c, t, C["s04.a"], [("evaporação", "g", 110, COR)], XE, 260)
    E.frase(c, t, C["s04.b"], ps("água salgada ao sol ou no fogo", "i", 58, TINTA2), XE, 380, passo=0.08)
    E.foco(c, t, C["s04.b"], 0.5, lambda a: salina(c, t, 900, 780, 880, a, ep(t, C["s04.c"], 3.0)))
    E.frase(c, t, C["s04.c"], [("a", "i", 62), ("água", "g", 62), ("vai", "i", 62), ("embora,", "i", 62), ("o", "i", 62), ("sal", "g", 62, COR), ("fica", "i", 62)], XE, 520, passo=0.1)
    pilula_em(c, t, C["s04.d"], "a salina", XE + 160, 650, 50, TINTA)
    E.frase(c, t, C["s04.e"], [("a", "i", 58), ("água", "g", 58), ("se", "i", 58), ("perde:", "g", 58, ERRADO)] + ps("só quando você quer o sólido", "i", 58), XE, 1010, passo=0.08)


# ---------------- destilação simples ----------------
def b_simples(c, t, C, b):
    E.frase(c, t, C["s05.a"], [("destilação", "g", 90, COR), ("simples", "g", 90)], XE, 190, passo=0.14)
    d = aparelho(c, t, C["s05.b"], 520, 650, liquido="#BFE3F2", sal=True, tv=C["s05.c"], coleta=ep(t, C["s06.c"], 6.0))
    if not d:
        return
    E.foco(c, t, C["s05.b"] + 0.3, 0.4, lambda a: E.escreve(c, "balão", 240, 800, 44, "b", TINTA2, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "condensador", d["j0"][0] + 200, d["j0"][1] - 40, 46, "b", TINTA, a))
    E.foco(c, t, C["s06.a"], 0.4, lambda a: (E.escreve(c, "água fria: entra embaixo,", 1300, 560, 42, "b", FRIO, a),
                                            E.escreve(c, "sai em cima", 1300, 610, 42, "b", FRIO, a)))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E.escreve(c, "água destilada", d["frasco"][0] + 140, d["frasco"][1] - 60, 46, "g", COR, a))
    E.foco(c, t, C["s06.e"], 0.4, lambda a: E.escreve(c, "o sal fica no balão", 140, 1000, 46, "b", TINTA2, a))
    pilula_em(c, t, C["s07.a"], "sólido dissolvido + líquido: fica com os dois", 1300, 300, 40, TINTA, "b")


# ---------------- destilação fracionada ----------------
def b_fracionada(c, t, C, b):
    E.frase(c, t, C["s08.a"], [("álcool", "g", 76), ("+", "g", 76, TINTA2), ("água", "g", 76)], 1180, 480, passo=0.12)
    E.frase(c, t, C["s08.b"], [("78 °C", "g", 60, COR), ("e", "i", 60), ("100 °C", "g", 60, COR)], 1180, 580, passo=0.12)
    termo = None
    if t >= C["s10.b"]:
        termo = ("78 °C" if t < C["s10.c"] else "~100 °C", C["s10.b"] if t < C["s10.c"] else C["s10.c"])
    d = aparelho(c, t, C["s09.a"] - 0.3, 520, 800, fracionada=True, liquido="#D7ECF5", tv=C["s09.b"], coleta=ep(t, C["s10.a"], 6.0), termo=termo)
    if d:
        E.foco(c, t, C["s09.a"], 0.4, lambda a: E.escreve(c, "coluna", 590, 520, 46, "g", COR, a))
        E.foco(c, t, C["s09.b"], 0.4, lambda a: E.escreve(c, "o vapor que ferve fácil sobe", 1180, 230, 42, "b", TINTA2, a))
        E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "o outro condensa e volta", 1180, 290, 42, "b", TINTA2, a))
    E.frase(c, t, C["s10.a"], ps("sai primeiro o de", "i", 56), 1180, 880, passo=0.08)
    E.frase(c, t, C["s10.a"] + 0.9, [("menor", "g", 54, COR), ("ponto", "g", 54), ("de", "i", 56), ("ebulição", "g", 54)], 1180, 960, passo=0.1)
    pilula_em(c, t, C["s10.d"], "troque o frasco", 1560, 1040, 42, TINTA)


# ---------------- petróleo ----------------
def b_petroleo(c, t, C, b):
    E.frase(c, t, C["s11.a"], [("petróleo", "g", 90, COR)], XE, 220)
    E.frase(c, t, C["s11.a"] + 0.8, ps("milhares de substâncias", "i", 58, TINTA2), XE, 320, passo=0.08)
    E.frase(c, t, C["s11.a"] + 1.8, ps("de carbono e hidrogênio", "i", 58, TINTA2), XE, 400, passo=0.08)
    E.frase(c, t, C["s11.b"], ps("uma fracionada gigante:", "i", 58), XE, 560, passo=0.08)
    E.frase(c, t, C["s11.b"] + 1.2, [("a", "i", 70), ("torre", "g", 70, COR)], XE, 660, passo=0.12)
    tl = [C["s13.a"], C["s13.b"], C["s13.c"], C["s13.d"], C["s13.e"], C["s13.f"]]
    torre(c, t, C["s11.b"], 900, 120, 260, 860, tl)
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.escreve(c, "entra aquecido", 620, 1050, 44, "b", TINTA2, a))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: (E.escreve(c, "quente", 730, 890, 40, "b", QUENTE, a), E.escreve(c, "fria", 820, 170, 40, "b", FRIO, a)))
    E.frase(c, t, C["s12.c"], ps("cada parte condensa", "i", 50), XE, 820, passo=0.08)
    E.frase(c, t, C["s12.c"] + 1.0, ps("na sua altura", "i", 50), XE, 890, passo=0.08)
    if t >= C["s13.g"]:
        q = ep(t, C["s13.g"], 0.5)
        M.arrow(c, 1820, 950, 1820, 200, E.COR, q, 8, 26, ease_io(prog(t, C["s13.g"], 0.8)))
        E.foco(c, t, C["s13.g"] + 0.6, 0.4, lambda a: (E.escreve(c, "menor PE", 1650, 170, 40, "g", COR, a)))


# ---------------- álcool 96 ----------------
def b_alcool(c, t, C, b):
    E.frase(c, t, C["s14.a"], ps("destilando álcool com água:", "i", 62, TINTA2), XE, 220, passo=0.1)
    E.frase(c, t, C["s14.a"] + 1.4, [("96%", "g", 220, COR)], XE, 470)
    E.frase(c, t, C["s14.b"], ps("e não passa disso", "i", 70), XE, 600, passo=0.12)
    pilula_em(c, t, C["s14.d"], "mistura azeotrópica: ferve como se fosse pura", 700, 760, 44, E.COR)
    if t >= C["s15"]:
        for k, (x, nome) in enumerate(((1250, "no balão"), (1600, "no vapor"))):
            tk = C["s15.b"] + 0.5 * k
            E.foco(c, t, tk, 0.5, lambda a, x=x: (c.drawCircle(x, 520, 130, M.paint("#D7ECF5", a)), c.drawCircle(x, 520, 130, M.paint(Q.VIDRO, a, stroke=5))))
            E.foco(c, t, tk + 0.2, 0.4, lambda a, x=x, nome=nome: (centro(c, "96%", x, 545, 76, "g", COR, a), centro(c, nome, x, 720, 46, "i", TINTA2, a)))
        E.foco(c, t, C["s15.b"] + 0.8, 0.4, lambda a: centro(c, "=", 1425, 545, 90, "g", TINTA2, a))
        E.frase(c, t, C["s15.a"], ps("o vapor tem a mesma composição do líquido", "i", 52), XE, 920, passo=0.06)
        E.frase(c, t, C["s15.c"], ps("destilar de novo não muda nada", "i", 56, TINTA2), XE, 1010, passo=0.08)
        pilula_em(c, t, C["s15.d"], "o resto da água: outro processo", 1430, 860, 42, TINTA, "b")


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s16.a"], ps("o atalho:", "i", 66, CLARO) + [("o", "i", 66, CLARO), ("que", "i", 66, CLARO), ("você", "i", 66, CLARO), ("quer", "g", 62, BR), ("guardar?", "g", 62, E.CLARO)], XE, 160, passo=0.1)
    linhas = (("s16.b", "só o sólido dissolvido", "evaporação"), ("s16.c", "o líquido, ou os dois", "destilação simples"),
              ("s16.d", "líquidos que se misturam", "fracionada"))
    for k, (key, cond, met) in enumerate(linhas):
        y = 330 + 150 * k
        E.frase(c, t, C[key], [(cond, "i", 60, CLARO)], XE, y)
        E.frase(c, t, C[key] + 0.4, [("→", "g", 60, CLARO), (met, "g", 60, E.CLARO)], XE + 820, y, passo=0.12)
    E.frase(c, t, C["s16.e"], ps("sai primeiro o de menor ponto de ebulição", "i", 56, BR), XE + 80, 760, passo=0.08)
    E.frase(c, t, C["s17.a"], ps("todos usam: um ferve antes do outro", "i", 52, CLARO), XE, 880, passo=0.08)
    E.frase(c, t, C["s17.c"], [("não", "g", 52, ERRADO), ("funciona", "i", 54, CLARO), ("na", "i", 54, CLARO), ("azeotrópica", "g", 52, BR)], XE, 980, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s18"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s18.a"], "na fracionada, sai primeiro o mais pesado", XE, 340, 54)
    E.frase(c, t, C["s18.b"], [("quem", "i", 66), ("manda:", "i", 66), ("o", "i", 66), ("ponto", "g", 66, COR), ("de", "i", 66), ("ebulição", "g", 66, COR)], XE, 500, passo=0.12)
    E.frase(c, t, C["s18.c"], ps("sai primeiro quem ferve mais fácil", "i", 58), XE, 610, passo=0.08)
    torre(c, t, C["s18.d"] - 0.4, 1130, 140, 200, 800, None)
    E.frase(c, t, C["s18.d"], ps("na torre, as moléculas maiores", "i", 50, TINTA2), XE, 780, passo=0.08)
    E.frase(c, t, C["s18.d"] + 1.2, ps("também fervem mais tarde", "i", 50, TINTA2), XE, 850, passo=0.08)
    pilula_em(c, t, C["s18.e"], "mas quem decide é o ponto de ebulição", 620, 980, 44, E.COR)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s19.a"], ps("acetona e água se misturam", "i", 60, TINTA2), XE, 290, passo=0.08)
    E.frase(c, t, C["s19.b"], [("acetona:", "g", 60), ("56 °C", "g", 60, COR), ("água:", "g", 60), ("100 °C", "g", 60, COR)], XE, 400, passo=0.12)
    E.frase(c, t, C["s19.c"], [("1", "g", 60, COR)] + ps("que método?", "i", 64), XE, 560, passo=0.1)
    E.frase(c, t, C["s19.d"], [("2", "g", 60, COR)] + ps("qual sai primeiro?", "i", 64), XE, 680, passo=0.1)
    E.frase(c, t, C["s19.e"], [("3", "g", 60, COR)] + ps("o que marca o termômetro?", "i", 64), XE, 800, passo=0.1)
    if t < C["s20"]:
        aparelho(c, t, C["s19.a"], 1180, 800, fracionada=True, liquido="#E3F1F7", coleta=0, a=0.9, agua_fria=False)
    else:
        E.relogio(c, t, C["s20.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    termo = ("56 °C", C["s21.d"]) if t >= C["s21.d"] else None
    aparelho(c, t, C["s21"], 1150, 800, fracionada=True, liquido="#E3F1F7", tv=C["s21.c"], coleta=ep(t, C["s21.c"], 5.0), termo=termo)
    E.frase(c, t, C["s21.a"], ps("dois líquidos que se misturam:", "i", 56, TINTA2), XE, 220, passo=0.08)
    pilula_em(c, t, C["s21.b"], "destilação fracionada", 450, 330, 56, E.COR)
    E.frase(c, t, C["s21.c"], [("sai", "i", 62), ("primeiro", "i", 62), ("a", "i", 62), ("acetona", "g", 62, COR)], XE, 500, passo=0.1)
    E.foco(c, t, C["s21.d"], 0.4, lambda a: E.escreve(c, "termômetro: 56 °C", XE, 620, 60, "g", TINTA, a))
    riscado(c, t, C["s21.e"], "simples: vapores misturados", XE, 760, 52)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s22.a", [("evaporação", "g", 62), ("guarda", "i", 66), ("o", "i", 66), ("sólido", "g", 62, COR)]),
                 ("s22.b", [("simples", "g", 62), ("guarda", "i", 66), ("o", "i", 66), ("líquido", "g", 62, COR)]),
                 ("s22.c", [("fracionada:", "g", 62), ("do", "i", 66), ("menor", "g", 62, COR), ("PE", "g", 62), ("para", "i", 66), ("o", "i", 66), ("maior", "i", 66)]),
                 ("s22.d", [("azeotrópica", "g", 62), ("não", "g", 62, ERRADO), ("se", "i", 66), ("separa", "i", 66), ("só", "i", 66), ("destilando", "i", 66)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s23.a"], [("Praticando:", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s23.a"] + 0.6, ps("a ordem dos métodos", "i", 80), XE, 520, passo=0.12)
    for k, s in enumerate(("1 ímã", "2 água", "3 filtro", "4 fogo")):
        pilula_em(c, t, C["s23.a"] + 1.0 + 0.3 * k, s, XE + 110 + 230 * k, 680, 50, TINTA)
    E.foco(c, t, C["s23.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s23.b"] + 0.2, 0.4))
    E.frase(c, t, C["s23.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, evaporar=b_evaporar, simples=b_simples, fracionada=b_fracionada,
              petroleo=b_petroleo, alcool=b_alcool, atalho=b_atalho, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
