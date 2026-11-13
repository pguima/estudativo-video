"""Visual — Estudativo · QUI-MIS-006: separar sólidos, da peneira ao ímã.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e as convenções da trilha (QUI-MIS-002).
Na separação de misturas (MIS-006 a MIS-009), cada método é um desenho pequeno e animado do aparelho do dia a dia
(bateia, peneira, ímã, béquer), com o componente que SAI em movimento e o que FICA parado. A DIFERENÇA que o método usa
vai numa pílula escura acima do desenho (tamanho, densidade, ímã, dissolve); o nome do método, embaixo, na cor da matéria.
Areia = grãos cor de areia (AREIA); ouro e ferro = cor do elemento (Q.cor_el); água = Q.AGUA.
Peças candidatas ao kit: bateia, peneira, ima, feijao, vento, copo_camadas (com areia).
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
ARQUIVO_FINAL = "estudativo_QUI-MIS-006_separar_solidos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "tamanho", "densidade", "outros", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AREIA = "#C99A5B"
OURO = "#E6B422"
DENS = {"água": 1.0, "ouro": 19.3, "areia": 2.6, "isopor": 0.03, "serragem": 0.5}
assert DENS["ouro"] / DENS["água"] > 19 and DENS["isopor"] < 1 < DENS["areia"] and DENS["serragem"] < 1
METODO = {"tamanho": ("catação", "peneiração"), "densidade": ("ventilação", "levigação", "flotação"), "ímã": ("separação magnética",),
          "dissolve": ("dissolução fracionada",)}
assert sum(len(v) for v in METODO.values()) == 7


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


def metodo(c, t, t0, cx, y, dif, nome, size=52):
    """pílula escura com a diferença (em cima) e o nome do método (embaixo)"""
    if dif:
        pilula_em(c, t, t0, dif, cx, y, 40, TINTA, "b")
    E.frase(c, t, t0 + 0.3, [(nome, "g", size, COR)], cx, y + 470, "center")


def grao(c, x, y, r, cor, a=1.0, giro=0.0, alongado=1.0):
    c.save(); c.translate(x, y); c.rotate(giro)
    c.drawOval(skia.Rect.MakeXYWH(-r * alongado, -r, 2 * r * alongado, 2 * r), M.paint(cor, a))
    c.drawOval(skia.Rect.MakeXYWH(-r * alongado * 0.5, -r * 0.6, r * alongado * 0.6, r * 0.5), M.paint(BR, 0.35 * a))
    c.restore()


def bateia(c, t, cx, cy, w, a=1.0, lava=0.0, gira=True):
    """bacia do garimpeiro, de lado: água girando; a areia sai pela borda (lava 0..1) e o ouro fica no fundo"""
    if a <= 0:
        return
    h = w * 0.32
    ang = 8 * math.sin(t * 2.2) if gira else 0
    c.save(); c.translate(cx, cy); c.rotate(ang)
    corpo = skia.Path()
    corpo.moveTo(-w / 2, -h / 2); corpo.quadTo(0, h * 1.1, w / 2, -h / 2); corpo.close()
    agua = skia.Path()
    agua.moveTo(-w * 0.42, -h * 0.32); agua.quadTo(0, h * 0.9, w * 0.42, -h * 0.32); agua.close()
    c.drawPath(corpo, M.paint("#6B4E2E", a))
    c.drawPath(agua, M.paint(Q.AGUA, 0.9 * a))
    rnd = random.Random(11)
    for k in range(40):
        u = rnd.random()
        sai = lava > u
        x = (rnd.random() - 0.5) * w * 0.6
        y = h * 0.1 + rnd.random() * h * 0.25
        if sai:
            f = min(1.0, (lava - u) * 3)
            x += f * w * 0.55 * (1 if rnd.random() > 0.5 else -1)
            y -= f * h * 0.9
            if f >= 1:
                continue
        c.drawCircle(x, y, 6 + 3 * rnd.random(), M.paint(AREIA, a))
    for k in range(6):
        grao(c, -40 + 16 * k, h * 0.38 - 4 * (k % 2), 9, OURO, a, 20 * k, 1.4)
    c.restore()


def feijao(c, t, cx, cy, a=1.0, t_cata=None):
    rnd = random.Random(4)
    for k in range(22):
        x, y = cx + (rnd.random() - 0.5) * 380, cy + (rnd.random() - 0.5) * 180
        grao(c, x, y, 18, "#7A3E1D", a, rnd.random() * 180, 1.5)
    for k, (dx, dy) in enumerate(((-90, -20), (70, 40), (130, -60))):
        x, y = cx + dx, cy + dy
        if t_cata is not None and t >= t_cata + 0.5 * k:
            u = ease_io(prog(t, t_cata + 0.5 * k, 0.6))
            x, y = lerp(x, cx + 300, u), lerp(y, cy - 220, u)
        p = skia.Path(); p.moveTo(x - 16, y); p.lineTo(x - 6, y - 14); p.lineTo(x + 14, y - 10); p.lineTo(x + 16, y + 8); p.lineTo(x - 4, y + 14); p.close()
        c.drawPath(p, M.paint("#8A8D94", a))


def peneira(c, t, cx, cy, w, a=1.0, cai=True):
    """peneira vista de lado: os grãos pequenos caem pelos furos, os grandes ficam"""
    if a <= 0:
        return
    h = w * 0.16
    rnd = random.Random(8)
    for k in range(10):
        x = cx + (rnd.random() - 0.5) * w * 0.8
        grao(c, x, cy - 10 - rnd.random() * 20, 20, "#B8875A", a, rnd.random() * 90)
    c.drawOval(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), M.paint("#8B6B42", a, stroke=10))
    for k in range(1, 9):
        x = cx - w / 2 + k * w / 9
        M.line(c, x, cy - h * 0.4, x, cy + h * 0.4, "#8B6B42", 0.6 * a, 2)
    if cai:
        for k in range(14):
            u = (t * 0.6 + k / 14) % 1
            x = cx + (rnd.random() - 0.5) * w * 0.7
            c.drawCircle(x, cy + h / 2 + u * 260, 5, M.paint("#D9B27A", a * (1 - u)))
        c.drawOval(skia.Rect.MakeXYWH(cx - w * 0.35, cy + 300, w * 0.7, 40), M.paint("#D9B27A", a))


def vento(c, t, x, y, a=1.0, n=4):
    for k in range(n):
        u = (t * 0.8 + k / n) % 1
        xx = x + u * 260
        yy = y + 50 * k
        p = skia.Path(); p.moveTo(xx, yy); p.cubicTo(xx + 40, yy - 20, xx + 80, yy + 20, xx + 120, yy)
        c.drawPath(p, M.paint("#9FB7C6", a * (1 - abs(2 * u - 1)), stroke=5))


def ventilacao(c, t, cx, cy, a=1.0):
    vento(c, t, cx - 260, cy - 120, a)
    rnd = random.Random(2)
    for k in range(12):
        u = (t * 0.5 + k / 12) % 1
        x = cx + (rnd.random() - 0.5) * 40
        grao(c, x, cy - 160 + u * 320, 13, "#C9A15E", a, 90, 1.4)
        xc = cx + u * 340 * (0.6 + rnd.random() * 0.4)
        yc = cy - 160 + u * 140 + 30 * math.sin(u * 6 + k)
        c.drawOval(skia.Rect.MakeXYWH(xc - 14, yc - 5, 28, 10), M.paint("#E8D9B5", a))
    c.drawOval(skia.Rect.MakeXYWH(cx - 90, cy + 170, 180, 40), M.paint("#C9A15E", a))


def copo_camadas(c, t, t0, cx, yb, w, h, camadas, a=1.0):
    if t < t0 or a <= 0:
        return []
    q = ep(t, t0, 0.5) * a
    contorno, dentro, (yt, yb_) = Q._copo_path("bequer", cx, yb, w, h)
    c.drawPath(dentro, M.paint(BR, 0.45 * q))
    c.save()
    c.clipPath(dentro, skia.ClipOp.kIntersect, True)
    y, faixas = yb_, []
    for k, (tipo, f, ti) in enumerate(camadas):
        hh = (yb_ - yt) * f * (ease_io(prog(t, ti, 0.9)) if ti is not None else 1.0)
        r = skia.Rect.MakeLTRB(cx - w, y - hh, cx + w, y + 1)
        if tipo == "areia":
            c.drawRect(r, M.paint(AREIA, 0.95 * q))
            rnd = random.Random(7 + k)
            for _ in range(int(w * hh / 260)):
                gx, gy = cx - w / 2 + rnd.random() * w, y - rnd.random() * hh
                c.drawCircle(gx, gy, 2.5 + 2.5 * rnd.random(), M.paint("#8E6A38" if rnd.random() < 0.5 else "#E2C08A", 0.9 * q))
        else:
            c.drawRect(r, M.paint(tipo, 0.92 * q))
            M.line(c, cx - w, y - hh, cx + w, y - hh, M.mix(tipo, BR, 0.5), q, 4)
        faixas.append((y - hh, y))
        y -= hh
    c.restore()
    c.drawPath(contorno, M.paint(Q.VIDRO, q, stroke=5))
    return faixas


def flotacao(c, t, t0, cx, yb, a=1.0, coisa="serragem"):
    fx = copo_camadas(c, t, t0, cx, yb, 300, 360, [("areia", 0.12, None), (Q.AGUA, 0.55, None)], a)
    if fx:
        ys = fx[1][0]
        rnd = random.Random(3)
        for k in range(9):
            x = cx - 110 + 27 * k
            if coisa == "isopor":
                E.bola(c, x, ys - 4 + 3 * math.sin(t * 2 + k), 13, "#F7F7F5", a)
            else:
                c.save(); c.translate(x, ys + 2 * math.sin(t * 2 + k)); c.rotate(rnd.random() * 40 - 20)
                c.drawRect(skia.Rect.MakeXYWH(-12, -5, 24, 10), M.paint("#B07A3E", a)); c.restore()
    return fx


def ima(c, cx, cy, s, a=1.0, giro=0.0):
    """ímã em U, vermelho com as pontas cinza, aberto para baixo"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(giro)
    p = skia.Path()
    p.moveTo(-s, s * 0.9); p.lineTo(-s, 0); p.arcTo(skia.Rect.MakeXYWH(-s, -s, 2 * s, 2 * s), 180, 180, False)
    p.lineTo(s, s * 0.9)
    pt = M.paint("#D93A32", a, stroke=s * 0.6)
    c.drawPath(p, pt)
    for dx in (-s, s):
        c.drawRect(skia.Rect.MakeXYWH(dx - s * 0.3, s * 0.75, s * 0.6, s * 0.35), M.paint("#B9BFC7", a))
    c.restore()


def limalha(c, t, t0, cx, cy, xi, yi, a=1.0, n=26):
    """limalha de ferro: tracinhos escuros na areia que pulam até o ímã a partir de t0"""
    rnd = random.Random(9)
    for k in range(n):
        x, y = cx + (rnd.random() - 0.5) * 300, cy + (rnd.random() - 0.5) * 60
        u = ease_io(prog(t, t0 + rnd.random() * 0.8, 0.6)) if t0 is not None else 0
        tx, ty = xi + (rnd.random() - 0.5) * 120, yi + rnd.random() * 30
        x, y = lerp(x, tx, u), lerp(y, ty, u)
        ang = rnd.random() * math.pi
        M.line(c, x - 9 * math.cos(ang), y - 9 * math.sin(ang), x + 9 * math.cos(ang), y + 9 * math.sin(ang), "#3A3B40", a, 4)


def monte_areia(c, cx, cy, w, a=1.0):
    p = skia.Path(); p.moveTo(cx - w / 2, cy); p.quadTo(cx, cy - w * 0.3, cx + w / 2, cy); p.close()
    c.drawPath(p, M.paint(AREIA, a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01.a"], 0.6, lambda a: bateia(c, t, 1350, 560, 720, a, ep(t, C["s01.a"] + 1.0, 6.0)))
        E.frase(c, t, C["s01.a"], [("ouro", "g", 110, "#B8860B"), ("e", "i", 100), ("areia", "g", 110)], XE, 330, passo=0.14)
        E.frase(c, t, C["s01.a"] + 1.2, ps("uma bacia e um pouco de água", "i", 60, TINTA2), XE, 450, passo=0.1)
        E.frase(c, t, C["s01.b"], ps("sem máquina, sem produto", "i", 60), XE, 600, passo=0.1)
        E.frase(c, t, C["s01.c"], ps("como funciona?", "i", 80, COR), XE, 820, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("sete", "g", 70, COR), ("jeitos", "g", 70), ("de", "i", 74), ("separar", "i", 74)]),
                 (C["s02.c"], [("a", "i", 74), ("pergunta", "g", 70, COR), ("que", "i", 74), ("escolhe", "i", 74)])], XE, 470, 180)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("dois lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("heterogênea:", "g", 70, COR)] + ps("dá para ver as partes", "i", 70), XE, 360, passo=0.1)
    E.frase(c, t, C["s03.b"], [("densidade", "g", 70, COR), ("=", "g", 70, TINTA2)] + ps("massa dividida por volume", "i", 70), XE, 520, passo=0.1)
    fx = copo_camadas(c, t, C["s03.c"] - 0.3, 1450, 1000, 380, 380, [(Q.AGUA, 0.7, None)])
    if fx:
        ys = fx[0][0]
        E.foco(c, t, C["s03.c"], 0.4, lambda a: (M.rrect(c, 1340, ys - 40, 90, 60, 10, "#B07A3E", a)))
        E.foco(c, t, C["s03.d"], 0.4, lambda a: M.rrect(c, 1480, lerp(ys, 940, ease_io(prog(t, C["s03.d"], 1.0))), 80, 60, 10, "#5B6470", a))
    E.frase(c, t, C["s03.c"], [("menor", "g", 62), ("que", "i", 64), ("a", "i", 64), ("da", "i", 64), ("água:", "i", 64), ("boia", "g", 62, COR)], XE, 700, passo=0.1)
    E.frase(c, t, C["s03.d"], [("maior:", "g", 62), ("afunda", "g", 62, COR)], XE, 820, passo=0.1)


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    E.frase(c, t, C["s04"], ps("toda separação usa", "i", 76, TINTA2), W / 2, 260, "center", 0.12)
    E.frase(c, t, C["s04.a"], [("uma", "i", 120), ("diferença", "g", 120, COR)], W / 2, 420, "center", 0.14)
    E.frase(c, t, C["s04.b"], ps("em que esses sólidos são diferentes?", "i", 70), W / 2, 580, "center", 0.1)
    for k, (key, s) in enumerate((("s05.a", "tamanho"), ("s05.b", "densidade"), ("s05.c", "ímã"), ("s05.d", "dissolver"))):
        pilula_em(c, t, C[key], s, 360 + 400 * k, 820, 66, TINTA)


# ---------------- tamanho ----------------
def b_tamanho(c, t, C, b):
    pilula_em(c, t, C["s06.a"], "tamanho ou aparência", W / 2, 150, 50, TINTA, "b")
    E.foco(c, t, C["s06.b"], 0.5, lambda a: feijao(c, t, 520, 560, a, C["s06.c"] + 0.4))
    E.foco(c, t, C["s06.b"] + 0.6, 0.4, lambda a: (M.line(c, 860, 320, 760, 420, "#6E747C", a, 8), M.line(c, 880, 330, 770, 430, "#6E747C", a, 8)))
    E.frase(c, t, C["s06.b"] + 0.4, ps("partes grandes e poucas: mão ou pinça", "i", 46, TINTA2), 520, 790, "center", 0.08)
    E.frase(c, t, C["s06.c"], [("catação", "g", 80, COR)], 520, 920, "center")
    if t >= C["s07"]:
        E.foco(c, t, C["s07.a"], 0.5, lambda a: peneira(c, t, 1350, 420, 460, a))
        E.frase(c, t, C["s07.b"], [("peneiração", "g", 80, COR)], 1350, 920, "center")
        E.foco(c, t, C["s07.b"] + 0.8, 0.4, lambda a: E.escreve(c, "ou tamisação", 1220, 990, 46, "i", TINTA2, a))
        E.foco(c, t, C["s07.c"], 0.4, lambda a: centro(c, "os pequenos passam", 1350, 800, 42, "b", TINTA2, a))
        E.foco(c, t, C["s07.d"], 0.4, lambda a: centro(c, "os grandes ficam", 1350, 320, 42, "b", TINTA2, a))


# ---------------- densidade ----------------
def b_densidade(c, t, C, b):
    pilula_em(c, t, C["s08.a"], "densidade: o que muda é o que empurra", W / 2, 150, 46, TINTA, "b")
    if t >= C["s08.b"]:
        E.foco(c, t, C["s08.b"], 0.5, lambda a: ventilacao(c, t, 330, 520, a))
        E.frase(c, t, C["s08.b"] + 0.3, [("ar", "g", 56, TINTA2)], 330, 300, "center")
        E.frase(c, t, C["s08.b"] + 0.5, [("ventilação", "g", 64, COR)], 360, 860, "center")
        E.foco(c, t, C["s08.c"], 0.4, lambda a: E.escreve(c, "casca vai com o vento", 400, 650, 40, "i", TINTA2, a))
        E.foco(c, t, C["s08.d"], 0.4, lambda a: E.escreve(c, "grão cai", 110, 760, 40, "i", TINTA2, a))
    if t >= C["s09"]:
        E.foco(c, t, C["s09.a"], 0.5, lambda a: bateia(c, t, 1000, 560, 440, a, ep(t, C["s09.c"], 3.0)))
        E.frase(c, t, C["s09.a"] + 0.3, [("água", "g", 56, TINTA2)], 1000, 300, "center")
        E.frase(c, t, C["s09.a"] + 0.5, [("levigação", "g", 64, COR)], 1000, 860, "center")
        E.foco(c, t, C["s09.c"], 0.4, lambda a: centro(c, "a água leva a areia", 1000, 400, 40, "i", TINTA2, a))
        E.foco(c, t, C["s09.d"], 0.4, lambda a: centro(c, "ouro: ~19 vezes a água", 1000, 760, 40, "b", "#9A7208", a))
    if t >= C["s10"]:
        E.frase(c, t, C["s10.a"], [("líquido", "g", 56, TINTA2), ("parado", "g", 56, TINTA2)], 1560, 300, "center")
        flotacao(c, t, C["s10.a"], 1560, 760)
        E.foco(c, t, C["s10.b"], 0.4, lambda a: centro(c, "serragem boia", 1560, 380, 40, "i", TINTA2, a))
        E.foco(c, t, C["s10.c"], 0.4, lambda a: centro(c, "areia afunda", 1560, 690, 40, "b", TINTA2, a))
        E.frase(c, t, C["s10.d"], [("flotação", "g", 64, COR)], 1560, 860, "center")
        pilula_em(c, t, C["s10.e"], "reciclagem de plásticos", 1560, 960, 40, TINTA2, "b")


# ---------------- ímã e dissolução ----------------
def b_outros(c, t, C, b):
    xi, yi = 520, 380
    if t >= C["s11"]:
        pilula_em(c, t, C["s11.a"], "atraído por ímã?", 520, 170, 46, TINTA, "b")
        yy = lerp(260, 380, ease_io(prog(t, C["s11.c"], 0.8)))
        E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: ima(c, xi, yy, 70, a))
        E.foco(c, t, C["s11.a"] + 0.3, 0.4, lambda a: monte_areia(c, 520, 700, 460, a))
        limalha(c, t, C["s11.c"] + 0.6, 520, 640, xi, yy + 110)
        E.frase(c, t, C["s11.b"], [("separação", "g", 64, COR), ("magnética", "g", 64, COR)], 520, 860, "center", 0.12)
        E.foco(c, t, C["s11.c"] + 0.2, 0.4, lambda a: E.escreve(c, "limalha = ferro em pó", 300, 790, 44, "b", TINTA2, a))
        pilula_em(c, t, C["s11.d"], "latas de aço no lixo", 520, 960, 42, TINTA2, "b")
    if t >= C["s12"]:
        pilula_em(c, t, C["s12.a"], "um dissolve na água?", 1400, 170, 46, TINTA, "b")
        sal = 1 - ep(t, C["s12.d"], 1.5)
        fx = copo_camadas(c, t, C["s12.c"], 1400, 760, 340, 400, [("areia", 0.12 * ease_io(prog(t, C["s12.d"], 1.2)), None), (Q.AGUA, 0.6, C["s12.c"])])
        rnd = random.Random(2)
        if fx and sal > 0:
            for k in range(16):
                s_ = 12 * sal
                x, y = 1400 + (rnd.random() - 0.5) * 240, 700 - rnd.random() * 160
                c.drawRect(skia.Rect.MakeXYWH(x - s_ / 2, y - s_ / 2, s_, s_), M.paint(BR, 1))
                c.drawRect(skia.Rect.MakeXYWH(x - s_ / 2, y - s_ / 2, s_, s_), M.paint(CINZA, 1, stroke=2))
        E.frase(c, t, C["s12.b"], [("dissolução", "g", 64, COR), ("fracionada", "g", 64, COR)], 1400, 860, "center", 0.12)
        E.foco(c, t, C["s12.d"] + 0.4, 0.4, lambda a: (E.escreve(c, "sal dissolve", 1590, 470, 42, "i", TINTA2, a), E.escreve(c, "areia não", 1590, 720, 42, "i", TINTA2, a)))
        pilula_em(c, t, C["s12.e"], "e depois? próximas aulas", 1400, 960, 42, TINTA2, "b")


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def tabela():
            E.frase(c, t, C["s13.a"], ps("o atalho:", "i", 66, CLARO) + [("qual", "g", 62, BR), ("é", "i", 66, CLARO), ("a", "i", 66, CLARO), ("diferença?", "g", 62, E.CLARO)], XE, 160, passo=0.12)
            linhas = (("s13.b", "tamanho", "catação ou peneira"), ("s13.c", "densidade", "ar, água correndo ou líquido parado"),
                      ("s13.d", "ímã", "separação magnética"), ("s13.e", "dissolve", "dissolução fracionada"))
            for k, (key, d, m) in enumerate(linhas):
                y = 330 + 170 * k
                E.foco(c, t, C[key], 0.4, lambda a, d=d, y=y: E.pilula(c, d, XE + 180, y - 20, 54, "g", fundo="#1F2030", a=a))
                E.frase(c, t, C[key] + 0.3, [("→", "g", 60, CLARO)], XE + 420, y)
                E.frase(c, t, C[key] + 0.4, [(m, "g", 58, BR)], XE + 520, y)
        E.saida(c, t, C["s14"] - 0.1, tabela)
        return
    E.frase(c, t, C["s14.a"], ps("a prova descreve a situação;", "i", 64, CLARO), W / 2, 300, "center", 0.1)
    E.frase(c, t, C["s14.a"] + 1.2, ps("ela quase nunca pede o nome solto", "i", 64, CLARO), W / 2, 400, "center", 0.1)
    E.frase(c, t, C["s14.b"], [("achada", "i", 66, CLARO), ("a", "i", 66, CLARO), ("diferença,", "g", 62, BR), ("sobram", "i", 66, CLARO), ("1", "g", 62, E.CLARO), ("ou", "i", 66, CLARO), ("2", "g", 62, E.CLARO)], W / 2, 580, "center", 0.12)
    E.frase(c, t, C["s14.c"], [("não", "g", 58, ERRADO), ("basta:", "i", 62, CLARO)] + ps("3 componentes pedem passos em ordem", "i", 62, CLARO), W / 2, 800, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s15"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.foco(c, t, C["s15"] + 0.3, 0.6, lambda a: bateia(c, t, 1350, 560, 660, a, ep(t, C["s15.b"], 3.0)))
    riscado(c, t, C["s15.a"], "na levigação, fica o mais leve", XE, 360, 58)
    E.frase(c, t, C["s15.b"], [("a", "i", 66), ("água", "g", 66), ("leva", "i", 66), ("o", "i", 66), ("menos", "g", 66, COR), ("denso", "g", 66, COR)], XE, 520, passo=0.12)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: (M.arrow(c, 1520, 820, 1380, 680, "#9A7208", a, 6, 22), E.escreve(c, "fica: o ouro", 1530, 860, 52, "g", "#9A7208", a)))
    E.frase(c, t, C["s15.d"], ps("o mais denso de todos", "i", 60), XE, 640, passo=0.1)
    if t >= C["s16"]:
        E.frase(c, t, C["s16.a"], ps("e não troque", "i", 64, TINTA2), XE, 820, passo=0.12)
        pilula_em(c, t, C["s16.b"], "ventilação = ar", XE + 260, 940, 52, TINTA)
        pilula_em(c, t, C["s16.c"], "levigação = água", XE + 760, 940, 52, E.COR)


# ---------------- questão ----------------
def icone_cafe(c, t, cx, cy, a):
    rnd = random.Random(5)
    for k in range(10):
        grao(c, cx + (rnd.random() - 0.5) * 220, cy + (rnd.random() - 0.5) * 80, 16, "#5A3A22", a, rnd.random() * 180, 1.3)
    for k in range(8):
        c.drawOval(skia.Rect.MakeXYWH(cx + (rnd.random() - 0.5) * 240 - 14, cy + (rnd.random() - 0.5) * 90 - 5, 28, 10), M.paint("#E8D9B5", a))


def icone_isopor(c, t, cx, cy, a):
    monte_areia(c, cx, cy + 40, 260, a)
    for k in range(7):
        E.bola(c, cx - 90 + 30 * k, cy + 10 - 8 * (k % 2), 13, "#F7F7F5", a)


def icone_acucar(c, t, cx, cy, a):
    monte_areia(c, cx, cy + 40, 260, a)
    rnd = random.Random(1)
    for k in range(14):
        x, y = cx + (rnd.random() - 0.5) * 160, cy + 10 - rnd.random() * 30
        c.drawRect(skia.Rect.MakeXYWH(x - 6, y - 6, 12, 12), M.paint(BR, a)); c.drawRect(skia.Rect.MakeXYWH(x - 6, y - 6, 12, 12), M.paint(CINZA, a, stroke=2))


ICONES = (icone_cafe, icone_isopor, icone_acucar)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s17"] + 1.0, ps("que método separa cada mistura?", "i", 56, TINTA2), XE, 280, passo=0.08)
    itens = ((C["s17.a"], "café seco + cascas soltas"), (C["s17.b"], "isopor + areia, com um balde de água"), (C["s17.c"], "açúcar + areia"))
    for k, (ti, txt) in enumerate(itens):
        y = 470 + 200 * k
        E.frase(c, t, ti, [(str(k + 1), "g", 60, COR)] + ps(txt, "i", 60), XE, y, passo=0.1)
        if t < C["s18"]:
            E.foco(c, t, ti + 0.3, 0.4, lambda a, k=k, y=y: ICONES[k](c, t, 1550, y - 30, a))
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=1500, cy=520, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    linhas = ((C["s19.a"], C["s19.b"], "densidade: casca leve", "ventilação"), (C["s20.a"], C["s20.b"], "densidade: o isopor boia", "flotação"),
              (C["s20.c"], C["s20.d"], "o açúcar dissolve", "dissolução fracionada"))
    for k, (t0, t1, dif, nome) in enumerate(linhas):
        y = 300 + 210 * k
        E.foco(c, t, t0, 0.4, lambda a, k=k, y=y: ICONES[k](c, t, 330, y - 20, a))
        E.frase(c, t, t0 + 0.3, ps(dif, "i", 56, TINTA2), 560, y - 20, passo=0.08)
        E.frase(c, t, t1, [(nome, "g", 66, COR)], 560, y + 60)
        E.foco(c, t, t1 + 0.5, 0.4, lambda a, y=y: E.selo(c, 1780, y + 20, 40, True, a))
    riscado(c, t, C["s20.e"], "peneira para o açúcar: grãos do mesmo tamanho", XE, 1000, 50)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 220, "center")
        E.frase(c, t, C["s21.a"], [("separar", "i", 100), ("=", "g", 100, TINTA2), ("usar", "i", 100), ("uma", "i", 100), ("diferença", "g", 100, COR)], W / 2, 480, "center", 0.12)
        E.frase(c, t, C["s21.b"], ps("ache a diferença,", "i", 80, TINTA2), W / 2, 680, "center", 0.12)
        E.frase(c, t, C["s21.c"], ps("e o método aparece", "i", 80), W / 2, 800, "center", 0.12)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s22.a"], [("Decantar,", "g", 100, COR)], XE, 400)
    E.frase(c, t, C["s22.a"] + 0.5, [("filtrar", "g", 100, COR), ("e", "i", 100), ("centrifugar", "g", 100, COR)], XE, 520, passo=0.14)
    copo_camadas(c, t, C["s22.a"] + 0.8, 560, 960, 300, 300, [("areia", 0.2, None), (Q.AGUA, 0.6, None)])
    E.foco(c, t, C["s22.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s22.b"] + 0.2, 0.4))
    E.frase(c, t, C["s22.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, tamanho=b_tamanho, densidade=b_densidade, outros=b_outros,
              atalho=b_atalho, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
