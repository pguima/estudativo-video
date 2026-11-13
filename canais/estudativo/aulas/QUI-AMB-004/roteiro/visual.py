"""Visual — Estudativo · QUI-AMB-004: tratamento de água.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e a LINGUAGEM VISUAL DA QUÍMICA AMBIENTAL
(cabeçalho de QUI-AMB-001/roteiro/visual.py). Nesta aula:
- ESTEIRA DAS ETAPAS (esteira) no alto da tela: seis ícones em fila; a etapa da vez acende. As etapas têm três cores de
  grupo, a dos três verbos do atalho: JUNTAR (cor da matéria), TIRAR (tinta), PROTEGER (azul do flúor e do cloro, PROT).
- TANQUE (tanque): as partículas finas de barro mexem sem descer; com o Al(OH)₃ (geleia branca) elas se juntam em flocos
  (junta 0..1) e, na decantação, descem (desce 0..1).
- Filtro em camadas: carvão (escuro), areia (cor de areia), cascalho (cinza), de cima para baixo.
Peças candidatas ao kit: esteira (etapas em fila), tanque (flocos que se juntam e descem), filtro_camadas, microbio, dente.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Química e Ambiente")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-AMB-004_tratamento_de_agua.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("problema", "coagula", "separa", "protege", "atalho", "questao", "fim"))
BR = "#FFFFFF"
BARRO = "#8B5E34"
PROT = "#1F6FEB"
ETAPAS = ["coagulação", "floculação", "decantação", "filtração", "cloração", "fluoretação"]
GRUPO = {"coagulação": "juntar", "floculação": "juntar", "decantação": "tirar", "filtração": "tirar", "cloração": "proteger", "fluoretação": "proteger"}
COR_G = {"juntar": E.COR, "tirar": TINTA, "proteger": PROT}
assert [GRUPO[e] for e in ETAPAS] == ["juntar"] * 2 + ["tirar"] * 2 + ["proteger"] * 2
for eq in ("Al2(SO4)3 + 3 Ca(OH)2 -> 2 Al(OH)3 + 3 CaSO4", "Cl2 + H2O -> HCl + HClO"):
    r, p = Q.lados(eq)
    assert r == p, eq
EMBARALHADA = ["filtração", "cloração", "floculação", "coagulação", "fluoretação", "decantação"]
assert sorted(EMBARALHADA, key=ETAPAS.index) == ETAPAS


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


def riscado(c, t, t0, s, x, y, size=56, est="i"):
    E.foco(c, t, t0, 0.4, lambda a: E.escreve(c, s, x, y, size, est, ERRADO, a))
    if t >= t0 + 0.8:
        E.risco(c, x - 10, y + 14, x + E.larg(s, est, size) + 10, y - size * 0.6, t, t0 + 0.8, largura=8)


def esteira(c, t, t0, ativa=None, y=110, a=1.0, ts=None):
    """as seis etapas em fila; ativa = índice aceso; ts = instante de entrada de cada uma (None = todas em t0)"""
    for k, nome in enumerate(ETAPAS):
        ti = ts[k] if ts else t0
        if ti is None or t < ti:
            continue
        q = ep(t, ti, 0.4) * a
        x = 210 + 300 * k
        cor = COR_G[GRUPO[nome]]
        on = ativa == k
        r = 34 if not on else 40
        E.bola(c, x, y, r, cor if on or ativa is None else M.mix(cor, BR, 0.55), q)
        centro(c, str(k + 1), x, y + r * 0.45, r * 1.2, "g", BR, q)
        centro(c, nome, x, y + 80, 40 if not on else 44, "g" if on else "b", cor if on or ativa is None else CINZA, q)
        if k:
            M.line(c, x - 260, y, x - 50, y, FIO, q, 4)


def tanque(c, t, x, y, w, h, junta=0.0, desce=0.0, a=1.0, turvo=1.0, n=70, geleia=0.0, pas=None, semente=4):
    """tanque com água barrenta: partículas finas que tremem; junta 0..1 forma flocos; desce 0..1 leva ao fundo"""
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 20, M.mix(Q.AGUA, BARRO, 0.35 * turvo * (1 - desce * 0.9)), a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 20, 20), M.paint(Q.VIDRO, a, stroke=5))
    rnd = random.Random(semente)
    K = 7
    centros = [(x + w * (0.12 + 0.76 * rnd.random()), y + h * (0.2 + 0.5 * rnd.random())) for _ in range(K)]
    c.save(); c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 20, 20), skia.ClipOp.kIntersect, True)
    if geleia > 0:
        for k, (cx, cy) in enumerate(centros):
            c.drawCircle(cx, cy, 34 * geleia, M.paint("#F4F7FA", 0.7 * a * (1 - desce)))
    for i in range(n):
        px, py = x + w * rnd.random(), y + h * rnd.random()
        kx, ky = centros[i % K]
        ox, oy = (rnd.random() - 0.5) * 50, (rnd.random() - 0.5) * 40
        jx, jy = lerp(px, kx + ox, junta), lerp(py, ky + oy, junta)
        jx += 3 * math.sin(t * 7 + i) * (1 - junta)
        jy += 3 * math.cos(t * 6 + i * 1.3) * (1 - junta)
        fundo = y + h - 14 - rnd.random() * 26
        jy = lerp(jy, fundo, desce)
        c.drawCircle(jx, jy, 4 + 3 * junta, M.paint(BARRO, a))
    if pas is not None:
        for k in range(3):
            xx = x + w * (0.2 + 0.3 * k)
            ang = pas + k
            M.line(c, xx - 60 * math.cos(ang), y + h / 2 - 20 * math.sin(ang), xx + 60 * math.cos(ang), y + h / 2 + 20 * math.sin(ang), "#6E747C", a, 10)
            M.line(c, xx, y - 40, xx, y + h / 2, "#6E747C", a, 6)
    c.restore()


def filtro_camadas(c, t, x, y, w, h, a=1.0, passa=True):
    camadas = (("carvão", "#3A3B40", 0.25), ("areia", "#D9B27A", 0.4), ("cascalho", "#9AA0A8", 0.35))
    yy = y
    for k, (nome, cor, f) in enumerate(camadas):
        hh = h * f
        c.drawRect(skia.Rect.MakeXYWH(x, yy, w, hh), M.paint(cor, a))
        rnd = random.Random(k + 2)
        for _ in range(int(w * hh / 900)):
            c.drawCircle(x + rnd.random() * w, yy + rnd.random() * hh, 3 + 5 * rnd.random() * (k + 1) / 2, M.paint(M.mix(cor, "#000000" if k != 0 else "#FFFFFF", 0.25), a))
        E.escreve(c, nome, x + w + 30, yy + hh / 2 + 16, 44, "b", TINTA, a)
        yy += hh
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(Q.VIDRO, a, stroke=5))
    if passa:
        for k in range(6):
            u = (t * 0.5 + k / 6) % 1
            E.bola(c, x + w * (0.15 + 0.14 * k), y - 60 + u * (h + 160), 9, Q.AGUA, a)


def microbio(c, cx, cy, s, a=1.0, giro=0.0):
    c.save(); c.translate(cx, cy); c.rotate(giro)
    M.rrect(c, -s, -s * 0.4, 2 * s, s * 0.8, s * 0.4, "#9C5FD0", a)
    for k in range(3):
        M.line(c, -s * 0.5 + k * s * 0.5, -s * 0.4, -s * 0.6 + k * s * 0.5, -s * 0.8, "#9C5FD0", a, 3)
    c.restore()


def dente(c, cx, cy, s, a=1.0):
    p = skia.Path()
    p.moveTo(cx - s, cy - s * 0.6)
    p.cubicTo(cx - s, cy - s * 1.3, cx - s * 0.2, cy - s * 1.2, cx, cy - s * 0.9)
    p.cubicTo(cx + s * 0.2, cy - s * 1.2, cx + s, cy - s * 1.3, cx + s, cy - s * 0.6)
    p.cubicTo(cx + s, cy + s * 0.2, cx + s * 0.6, cy + s * 1.3, cx + s * 0.3, cy + s * 1.2)
    p.lineTo(cx, cy + s * 0.2); p.lineTo(cx - s * 0.3, cy + s * 1.2)
    p.cubicTo(cx - s * 0.6, cy + s * 1.3, cx - s, cy + s * 0.2, cx - s, cy - s * 0.6)
    c.drawPath(p, M.paint(BR, a)); c.drawPath(p, M.paint("#9AA0A8", a, stroke=5))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        tanque(c, t, 140, 380, 560, 420, a=ep(t, C["s01.a"], 0.5))
        E.frase(c, t, C["s01.a"], ps("do rio: barro, folhas e micróbios", "i", 50, TINTA2), 140, 330, passo=0.08)
        E.foco(c, t, C["s01.b"], 0.5, lambda a: (M.arrow(c, 760, 590, 1100, 590, E.COR, a, 8, 30), Q.bequer(c, t, C["s01.b"], 1400, 820, 360, 420, 0.7, Q.AGUA, graduacao=False)))
        E.frase(c, t, C["s01.b"] + 0.4, ps("limpa na torneira", "i", 50, TINTA2), 1250, 330, passo=0.08)
        for k, (key, s, cor) in enumerate((("s01.c", "um produto que junta a sujeira", E.COR), ("s01.d", "cloro contra os germes", PROT), ("s01.e", "flúor para os dentes", PROT))):
            E.foco(c, t, C[key], 0.4, lambda a, k=k, s=s, cor=cor: E.pilula(c, s, 360 + 600 * k, 960, 40, "b", fundo=cor, a=a))
        E.frase(c, t, C["s01.a"], [("do", "i", 70), ("rio", "g", 70), ("à", "i", 70), ("torneira", "g", 70, COR)], XE, 200, passo=0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1560, 600, 240 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 300, passo=0.14)
    lista(c, t, [(C["s02.b"], [("as", "i", 66), ("seis", "g", 62, COR), ("etapas", "g", 62), ("em", "i", 66), ("ordem", "i", 66)]),
                 (C["s02.c"], [("a", "i", 66), ("química", "g", 62, COR), ("de", "i", 66), ("cada", "i", 66), ("uma", "i", 66)])], XE, 500, 180)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("três lembretes", "i", 80, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("decantação:", "g", 66, COR)] + ps("o sólido mais denso desce sozinho", "i", 64), XE, 400, passo=0.1)
    E.frase(c, t, C["s03.b"], [("dupla", "g", 66, COR), ("troca:", "g", 66, COR)] + ps("forma precipitado: sólido que não dissolve", "i", 56), XE, 580, passo=0.08)
    E.frase(c, t, C["s03.c"], [("pH", "g", 70, COR), ("<", "g", 70, TINTA2), ("7", "g", 70), ("=", "g", 70, TINTA2), ("ácido", "g", 70)], XE, 760, passo=0.12)


# ---------------- o problema ----------------
def b_problema(c, t, C, b):
    E.frase(c, t, C["s04.a"], ps("boa parte do barro é", "i", 70), XE, 240, passo=0.12)
    E.frase(c, t, C["s04.a"] + 1.2, [("fina", "g", 110, COR), ("demais", "g", 110)], XE, 380, passo=0.14)
    tanque(c, t, 1000, 220, 760, 560, a=ep(t, C["s04"], 0.5), n=90)
    E.foco(c, t, C["s04.b"], 0.4, lambda a: E.escreve(c, "boiando por dias, sem descer", 1000, 860, 50, "b", TINTA2, a))
    E.frase(c, t, C["s04.b"], ps("pequenas e leves", "i", 60, TINTA2), XE, 540, passo=0.1)
    pilula_em(c, t, C["s04.c"], "é preciso juntar antes", 560, 760, 56, E.COR)


# ---------------- coagulação ----------------
def b_coagula(c, t, C, b):
    esteira(c, t, C["s05"], 0)
    gel = ep(t, C["s06.a"], 1.2)
    tanque(c, t, 1180, 300, 620, 460, junta=0.25 * gel, geleia=gel, a=ep(t, C["s05"], 0.5))
    E.frase(c, t, C["s05.a"], [("coagulação", "g", 90, COR)], XE, 340)
    E.frase(c, t, C["s05.b"], ps("sulfato de alumínio", "i", 56), XE, 450, passo=0.08)
    Q.formula_em(c, t, C["s05.b"] + 0.6, "Al2(SO4)3", XE + 520, 455, 70)
    E.frase(c, t, C["s05.c"], ps("+ cal: hidróxido de cálcio", "i", 56), XE, 550, passo=0.08)
    Q.formula_em(c, t, C["s05.c"] + 0.8, "Ca(OH)2", XE + 690, 555, 70)
    if C["s05.d"] <= t:
        Q.equacao(c, t, C["s05.d"], "Al2(SO4)3 + 3 Ca(OH)2 -> 2 Al(OH)3 + 3 CaSO4", W / 2, 880, 66,
                  tl=[C["s05.d"] + 0.2 * k for k in range(4)] + [C["s06.a"], C["s06.a"] + 0.3, C["s06.a"] + 0.6], cores={"Al(OH)3": E.COR})
        E.foco(c, t, C["s05.d"], 0.4, lambda a: E.escreve(c, "dupla troca", XE, 770, 46, "b", TINTA2, a))
    E.foco(c, t, C["s06.b"], 0.4, lambda a: E.escreve(c, "geleia que não dissolve", 1200, 280, 46, "b", COR, a))
    pilula_em(c, t, C["s06.c"], "a cal também corrige o pH", 1490, 1010, 44, TINTA, "b")


# ---------------- floculação ----------------
def b_flocula(c, t, C, b):
    esteira(c, t, C["s07"], 1)
    junta = ease_io(prog(t, C["s07.c"], 3.5))
    tanque(c, t, 820, 280, 960, 560, junta=0.25 + 0.75 * junta, geleia=1.0 - 0.6 * junta, pas=t * 1.2 if t >= C["s07.b"] else None, a=ep(t, C["s07"], 0.5))
    E.frase(c, t, C["s07.a"], [("floculação", "g", 80, COR)], XE, 340)
    E.frase(c, t, C["s07.b"], ps("mexida devagar,", "i", 56), XE, 470, passo=0.1)
    E.frase(c, t, C["s07.b"] + 0.8, ps("por um bom tempo", "i", 56), XE, 550, passo=0.1)
    E.frase(c, t, C["s07.c"], ps("a geleia gruda no barro", "i", 56), XE, 700, passo=0.08)
    pilula_em(c, t, C["s07.d"], "flocos maiores e mais pesados", 1300, 950, 46, E.COR)


# ---------------- decantação e filtração ----------------
def b_separa(c, t, C, b):
    if t < C["s09"]:
        esteira(c, t, C["s08"], 2)
        tanque(c, t, 820, 280, 960, 560, junta=1.0, geleia=0.4, desce=ease_io(prog(t, C["s08.c"], 2.5)), a=ep(t, C["s08"], 0.5))
        E.frase(c, t, C["s08.a"], [("decantação", "g", 80, TINTA)], XE, 340)
        E.frase(c, t, C["s08.b"], ps("tanques enormes, água quase parada", "i", 50), XE, 470, passo=0.08)
        E.frase(c, t, C["s08.c"], ps("os flocos descem: o lodo", "i", 56), XE, 600, passo=0.08)
        return
    esteira(c, t, C["s09"], 3)
    E.frase(c, t, C["s09.a"], [("filtração", "g", 80, TINTA)], XE, 340)
    E.frase(c, t, C["s09.b"], ps("camadas de areia, cascalho e carvão", "i", 50), XE, 470, passo=0.08)
    E.foco(c, t, C["s09.b"], 0.5, lambda a: filtro_camadas(c, t, 1000, 330, 520, 560, a))
    E.frase(c, t, C["s09.c"], ps("seguram os flocos pequenos", "i", 56), XE, 600, passo=0.08)
    pilula_em(c, t, C["s09.d"], "o carvão tira cheiro e gosto", 560, 760, 46, TINTA)


# ---------------- cloração e fluoretação ----------------
def b_protege(c, t, C, b):
    if t < C["s11.c"]:
        esteira(c, t, C["s10"], 4)
        E.frase(c, t, C["s10.a"], [("cloração", "g", 80, PROT)], XE, 340)
        E.frase(c, t, C["s10.a"] + 0.8, ps("limpa, mas ainda com micróbios", "i", 50, TINTA2), XE, 430, passo=0.08)
        Q.molecula(c, t, C["s10.b"], "Cl2", 1500, 400, 110)
        Q.equacao(c, t, C["s10.b"] + 0.4, "Cl2 + H2O -> HCl + HClO", W / 2, 640, 100, tl=[C["s10.b"] + 0.4, C["s10.b"] + 0.7, C["s10.b"] + 1.0, C["s10.c"], C["s10.c"] + 0.3, C["s10.c"] + 0.6], cores={"HClO": PROT})
        E.foco(c, t, C["s10.c"] + 1.0, 0.4, lambda a: E.escreve(c, "ácido hipocloroso", 1250, 730, 46, "b", PROT, a))
        mata = ep(t, C["s10.d"], 1.2)
        rnd = random.Random(6)
        for k in range(7):
            E.foco(c, t, C["s10.a"], 0.4, lambda a, k=k: microbio(c, 300 + 200 * k + 10 * math.sin(t * 2 + k), 900 + 20 * math.cos(t * 1.7 + k), 30, a * (1 - mata), 30 * k))
        if t >= C["s11"]:
            E.foco(c, t, C["s11.a"], 0.4, lambda a: E.pilula(c, "um pouco de cloro fica na água", 700, 1010, 42, "b", fundo=PROT, a=a))
            E.foco(c, t, C["s11.b"], 0.4, lambda a: E.escreve(c, "protege nos canos até a sua casa", 1120, 1020, 42, "b", TINTA2, a))
        return
    esteira(c, t, C["s11.c"], 5)
    E.frase(c, t, C["s11.c"], [("fluoretação", "g", 80, PROT)], XE, 340)
    E.frase(c, t, C["s11.d"], ps("uma dose pequena de um composto de flúor", "i", 52), XE, 480, passo=0.08)
    E.foco(c, t, C["s11.d"], 0.5, lambda a: dente(c, 1450, 600, 160, a))
    for k in range(5):
        E.foco(c, t, C["s11.d"] + 0.3 + 0.15 * k, 0.4, lambda a, k=k: Q.atomo(c, 1250 + 90 * k, 860 + 20 * math.sin(k), 28, "F", a))
    E.frase(c, t, C["s11.e"], ps("fortalece o esmalte e diminui as cáries", "i", 52), XE, 620, passo=0.08)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("o atalho: três verbos", "i", 66, CLARO), XE, 170, passo=0.12)
        for k, (key, verbo, e1, e2, cor) in enumerate((("s12.b", "juntar", "coagulação", "floculação", E.CLARO), ("s12.c", "tirar", "decantação", "filtração", BR),
                                                       ("s12.d", "proteger", "cloração", "fluoretação", "#6FA8FF"))):
            x = 200 + 560 * k
            E.foco(c, t, C[key], 0.4, lambda a, x=x, verbo=verbo, e1=e1, e2=e2, cor=cor, k=k: (
                M.rrect(c, x, 300, 500, 560, 30, "#14141E", a), E.escreve(c, f"{k + 1}. {verbo}", x + 40, 420, 72, "g", cor, a),
                E.escreve(c, e1, x + 40, 560, 52, "b", BR, a), E.escreve(c, e2, x + 40, 650, 52, "b", BR, a)))
            if k:
                M.arrow(c, x - 50, 580, x - 10, 580, CLARO, ep(t, C[key], 0.4), 6, 20)
        return
    E.frase(c, t, C["s13.a"], ps("cada etapa prepara a próxima", "i", 64, CLARO), W / 2, 260, "center", 0.1)
    E.frase(c, t, C["s13.b"], [("sem", "i", 66, CLARO), ("flocos,", "g", 62, BR), ("nada", "i", 66, CLARO), ("decanta", "g", 62, E.CLARO)], W / 2, 420, "center", 0.12)
    E.frase(c, t, C["s13.c"], ps("o cloro vem depois: a sujeira gastaria o cloro", "i", 60, BR), W / 2, 600, "center", 0.08)
    pilula_em(c, t, C["s13.d"], "a prova cobra a ordem padrão", W / 2, 820, 48, E.COR)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    riscado(c, t, C["s14.a"], "água tratada é água pura", XE, 340, 64)
    E.frase(c, t, C["s14.b"], [("ela", "i", 70), ("é", "i", 70), ("potável:", "g", 70, COR)] + ps("boa para beber", "i", 70), XE, 500, passo=0.12)
    E.frase(c, t, C["s14.c"], [("mas", "i", 64), ("é", "i", 64), ("mistura", "g", 64, COR)], XE, 650, passo=0.12)
    for k, (el, nome) in enumerate((("Cl", "cloro"), ("F", "flúor"), ("Na", "sais"))):
        E.foco(c, t, C["s14.c"] + 0.6 + 0.3 * k, 0.4, lambda a, k=k, el=el, nome=nome: (Q.atomo(c, 1100 + 230 * k, 620, 44, el, a), centro(c, nome, 1100 + 230 * k, 720, 44, "b", TINTA2, a)))
    E.frase(c, t, C["s14.d"], [("pura,", "g", 60), ("para", "i", 60), ("a", "i", 60), ("Química:", "i", 60), ("só", "i", 60)], XE, 880, passo=0.1)
    Q.formula_em(c, t, C["s14.d"] + 0.8, "H2O", XE + 700, 885, 80)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15.a"], ps("ponha em ordem:", "i", 60, TINTA2), XE, 300, passo=0.1)
    for k, nome in enumerate(EMBARALHADA):
        pilula_em(c, t, C["s15.a"] + 0.4 + 0.3 * k, nome, 320 + 420 * (k % 3), 440 + 130 * (k // 3), 50, TINTA)
    E.frase(c, t, C["s15.b"], ps("e em qual etapa se forma o", "i", 60), XE, 800, passo=0.1)
    Q.formula_em(c, t, C["s15.b"] + 1.0, "Al(OH)3", XE + 790, 805, 70)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=1600, cy=600, r=170)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    ts = [C["s17.a"], C["s17.a"] + 0.8, C["s17.b"], C["s17.b"] + 0.8, C["s17.c"], C["s17.c"] + 0.8]
    esteira(c, t, C["s17"], None, 300, ts=ts)
    for k, (key, verbo, cor) in enumerate((("s17.a", "juntar", E.COR), ("s17.b", "tirar", TINTA), ("s17.c", "proteger", PROT))):
        x = 210 + 600 * k + 150
        E.foco(c, t, C[key], 0.4, lambda a, x=x, verbo=verbo, cor=cor: centro(c, verbo, x, 200, 56, "g", cor, a))
    E.foco(c, t, C["s18.a"], 0.4, lambda a: c.drawCircle(210, 300, 60, M.paint(E.COR, a, stroke=6)))
    E.frase(c, t, C["s18.a"], ps("o", "i", 60), XE, 620)
    Q.formula_em(c, t, C["s18.a"] + 0.2, "Al(OH)3", XE + 60, 625, 76, cores={"Al(OH)3": E.COR})
    E.foco(c, t, C["s18.a"] + 0.6, 0.4, lambda a: E.escreve(c, "se forma na coagulação", XE + 400, 620, 60, "g", TINTA, a))
    riscado(c, t, C["s18.b"], "floculação primeiro: sem a geleia, nada gruda", XE, 820, 52)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for k, (key, verbo, e, cor) in enumerate((("s19.a", "juntar", "coagular e flocular", E.COR), ("s19.b", "tirar", "decantar e filtrar", TINTA),
                                                   ("s19.c", "proteger", "clorar e fluoretar", PROT))):
            y = 380 + 170 * k
            E.foco(c, t, C[key], 0.5, lambda a, k=k, y=y, cor=cor: (E.bola(c, 300, y - 26, 52, cor, a), centro(c, str(k + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[key] + 0.1, [(verbo + ":", "g", 66, cor), (e, "i", 70)], 400, y, passo=0.12)
        E.frase(c, t, C["s19.d"], [("juntar,", "g", 70, E.COR), ("tirar,", "g", 70), ("proteger", "g", 70, PROT)], W / 2, 960, "center", 0.14)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("Esgoto", "g", 100, COR), ("e", "i", 100), ("DBO", "g", 100, COR)], XE, 400, passo=0.14)
    E.frase(c, t, C["s20.a"] + 0.6, ps("a falta de oxigênio nos rios", "i", 70), XE, 520, passo=0.12)
    E.foco(c, t, C["s20.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(720, 445, p), ep(t, C["s20.b"] + 0.2, 0.4))
    E.frase(c, t, C["s20.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, problema=b_problema, coagula=b_coagula, flocula=b_flocula, separa=b_separa,
              protege=b_protege, atalho=b_atalho, erro=b_erro, questao=b_questao, resposta=b_resposta, fim=b_fim)
