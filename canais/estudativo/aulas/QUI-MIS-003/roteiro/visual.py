"""Visual — Estudativo · QUI-MIS-003: estados físicos e mudanças de estado.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001/roteiro/visual.py) e as convenções da trilha Matéria e
Misturas (QUI-MIS-002). Nesta aula:
- ESTADOS = três caixas de vidro com Q.particulas (sólido em grade, líquido no fundo, gás voando). Agitação maior = o tempo
  das partículas corre mais rápido (relogio_part), sem salto de posição.
- TRIÂNGULO DAS MUDANÇAS: sólido, líquido e gás nos cantos; cada par tem duas setas. As que absorvem calor ficam por fora,
  em âmbar (QUENTE, o mesmo do ΔH > 0); as que liberam ficam por dentro, em azul (FRIO, o do ΔH < 0).
- ESCADA (atalho, no palco): subir = absorver (âmbar), descer = liberar (azul).
Peças candidatas ao kit: triangulo_estados, escada_estados, chaleira, chama.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-003_estados_fisicos_mudancas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("estados", "mudancas", "calor", "atalho", "questao", "fim"))
BR = "#FFFFFF"
QUENTE, FRIO = "#E07B12", "#1F6FEB"   # absorve calor (âmbar) · libera calor (azul)

MUDANCAS = {  # (de, para): nome; as três primeiras absorvem calor
    ("S", "L"): "fusão", ("L", "G"): "vaporização", ("S", "G"): "sublimação",
    ("L", "S"): "solidificação", ("G", "L"): "condensação", ("G", "S"): "ressublimação",
}
ABSORVE = {"fusão", "vaporização", "sublimação"}
NIVEL = {"S": 0, "L": 1, "G": 2}
assert all((NIVEL[b] > NIVEL[a]) == (n in ABSORVE) for (a, b), n in MUDANCAS.items())  # subir a escada = absorver
assert len(MUDANCAS) == 6


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


def relogio_part(t, t1, k):
    """tempo das partículas: igual a t até t1 e k vezes mais rápido depois (posição contínua)"""
    return t if t < t1 else t1 + (t - t1) * k


def caixa_estado(c, t, t0, x, y, w, h, estado, n, nome=None, tp=None, r=18, semente=2):
    if t < t0:
        return
    q = ep(t, t0, 0.5)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), M.paint(BR, 0.6 * q))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), M.paint(Q.VIDRO, q, stroke=5))
    Q.particulas(c, t if tp is None else tp, x + 12, y + 12, w - 24, h - 24, n, estado, tipos=[(E.COR, 1.0)], r=r, semente=semente, a=q)
    if nome:
        E.foco(c, t, t0 + 0.3, 0.4, lambda a: centro(c, nome, x + w / 2, y + h + 80, 64, "g", TINTA, a))


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


def floco(c, cx, cy, s, a=1.0):
    for k in range(3):
        ang = math.radians(90 + 60 * k)
        M.line(c, cx - s * math.cos(ang), cy - s * math.sin(ang), cx + s * math.cos(ang), cy + s * math.sin(ang), FRIO, a, 7)


def chaleira(c, cx, cy, s, a=1.0, t=0.0, nuvem=1.0, gap=True):
    """chaleira com bico para a direita; a nuvem branca começa longe do bico (perto dele, o vapor é invisível)"""
    if a <= 0:
        return
    corpo = skia.Path()
    corpo.moveTo(cx - s, cy + s * 0.7)
    corpo.cubicTo(cx - s * 1.1, cy - s * 0.3, cx - s * 0.5, cy - s * 0.75, cx, cy - s * 0.75)
    corpo.cubicTo(cx + s * 0.5, cy - s * 0.75, cx + s * 1.1, cy - s * 0.3, cx + s, cy + s * 0.7)
    corpo.close()
    bico = skia.Path()
    bico.moveTo(cx + s * 0.8, cy + s * 0.1); bico.lineTo(cx + s * 1.55, cy - s * 0.55); bico.lineTo(cx + s * 1.62, cy - s * 0.42)
    bico.lineTo(cx + s * 0.95, cy + s * 0.45); bico.close()
    c.drawPath(bico, M.paint("#9AA0A8", a))
    c.drawPath(corpo, M.paint("#B9BFC7", a))
    c.drawPath(corpo, M.paint("#6E747C", a, stroke=5))
    M.rrect(c, cx - s * 0.25, cy - s * 0.92, s * 0.5, s * 0.2, s * 0.08, "#2A2B31", a)
    M.rrect(c, cx - s * 1.05, cy + s * 0.62, s * 2.1, s * 0.16, s * 0.08, "#2A2B31", a)
    if nuvem > 0:
        bx, by = cx + s * 1.62, cy - s * 0.52
        for k in range(9):
            u = ((t * 0.35 + k / 9) % 1.0)
            d0 = s * (0.55 if gap else 0.05)
            px = bx + d0 + u * s * 1.6 + 18 * math.sin(k * 2.1 + t)
            py = by - d0 * 0.8 - u * s * 1.4
            r = s * (0.18 + 0.32 * u)
            c.drawCircle(px, py, r, M.paint("#DCE1E7", 0.95 * nuvem * a * (1 - u) * min(1, u * 4)))
            c.drawCircle(px, py, r, M.paint("#A4ABB4", 0.8 * nuvem * a * (1 - u) * min(1, u * 4), stroke=3))


NOS = {"S": (300, 860), "L": (960, 270), "G": (1620, 860)}
NOMES = {"S": "sólido", "L": "líquido", "G": "gás"}
CENTRO = (960, 660)


def _geo(a_, b_, d):
    (x0, y0), (x1, y1) = NOS[a_], NOS[b_]
    ux, uy = (x1 - x0), (y1 - y0)
    L = math.hypot(ux, uy); ux, uy = ux / L, uy / L
    nx, ny = -uy, ux
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    if nx * (mx - CENTRO[0]) + ny * (my - CENTRO[1]) < 0:
        nx, ny = -nx, -ny
    return (x0, y0), (x1, y1), (ux, uy), (nx, ny), (mx, my)


def triangulo_estados(c, t, t0, tl, cor_seta=None, rot=True, r=118, escuro=False):
    """os três estados nos cantos e as seis setas; tl = {nome: instante}. cor_seta(nome) → cor (padrão: tinta)"""
    tinta = BR if escuro else TINTA
    for k, n in enumerate(("S", "L", "G")):
        x, y = NOS[n]
        E.foco(c, t, t0 + 0.2 * k, 0.5, lambda a, x=x, y=y, n=n: (E.bola(c, x, y, r * ease_back(prog(t, t0 + 0.2 * k, 0.5)), a=a),
                                                                  centro(c, NOMES[n], x, y + 18, 50, "g", E.SOBRE, a)))
    for (a_, b_), nome in MUDANCAS.items():
        if nome not in tl or t < tl[nome]:
            continue
        P0, P1, (ux, uy), (nx, ny), (mx, my) = _geo(a_, b_, 0)
        sgn = 1 if nome in ABSORVE else -1
        d = 38
        x0, y0 = P0[0] + ux * (r + 18) + sgn * nx * d, P0[1] + uy * (r + 18) + sgn * ny * d
        x1, y1 = P1[0] - ux * (r + 18) + sgn * nx * d, P1[1] - uy * (r + 18) + sgn * ny * d
        cor = cor_seta(nome) if cor_seta else tinta
        p = ease_io(prog(t, tl[nome], 0.6))
        M.arrow(c, x0, y0, x1, y1, cor, 1, 7, 26, p)
        if rot:
            off = d + 24 + abs(nx) * E.larg(nome, "g", 48) / 2 + abs(ny) * 26
            lx, ly = mx + sgn * nx * off, my + sgn * ny * off
            E.foco(c, t, tl[nome] + 0.3, 0.4, lambda a, lx=lx, ly=ly, nome=nome, cor=cor: centro(c, nome, lx, ly + 16, 48, "g", cor if cor_seta else tinta, a))


def exemplo(c, t, itens, x, y, size=52):
    """um exemplo por vez, no canto: itens = [(instante, texto)]; o novo troca o anterior"""
    for k, (ti, s) in enumerate(itens):
        t1 = itens[k + 1][0] if k + 1 < len(itens) else 1e9
        if ti <= t < t1 + 0.4:
            E.saida(c, t, t1, lambda s=s, ti=ti: E.foco(c, t, ti, 0.4, lambda a: (M.rrect(c, x - 20, y - size * 1.1, E.larg(s, "i", size) + 40, size * 1.6, 20, BR, a, stroke=3, stroke_color=FIO),
                                                                                   E.escreve(c, s, x, y, size, "i", TINTA, a))))


# ---------------- gancho ----------------
def varal(c, cx, cy, a, t):
    M.line(c, cx - 200, cy - 120, cx + 200, cy - 120, TINTA2, a, 4)
    for dx in (-200, 200):
        M.line(c, cx + dx, cy - 140, cx + dx, cy + 180, "#6E747C", a, 8)
    camisa = skia.Path()
    camisa.moveTo(cx - 60, cy - 120); camisa.lineTo(cx - 140, cy - 70); camisa.lineTo(cx - 110, cy - 20); camisa.lineTo(cx - 75, cy - 45)
    camisa.lineTo(cx - 75, cy + 110); camisa.lineTo(cx + 75, cy + 110); camisa.lineTo(cx + 75, cy - 45); camisa.lineTo(cx + 110, cy - 20)
    camisa.lineTo(cx + 140, cy - 70); camisa.lineTo(cx + 60, cy - 120); camisa.quadTo(cx, cy - 80, cx - 60, cy - 120); camisa.close()
    c.drawPath(camisa, M.paint(E.COR, a))
    for k in range(3):
        u = (t * 0.4 + k / 3) % 1
        x = cx - 40 + 40 * k
        p = skia.Path(); p.moveTo(x, cy - 140 - u * 120)
        p.cubicTo(x + 18, cy - 160 - u * 120, x - 18, cy - 190 - u * 120, x, cy - 210 - u * 120)
        c.drawPath(p, M.paint(CINZA, a * (1 - u), stroke=4))


def b_gancho(c, t, C, b):
    def um():
        cols = ((C["s01.a"], 360, "a roupa seca", "sem ferver"), (C["s01.b"], 960, "a naftalina some", "sem virar líquido"),
                (C["s01.c"], 1560, "a fumacinha branca", "não é gás"))
        for k, (ti, x, l1, l2) in enumerate(cols):
            if k == 0:
                E.foco(c, t, ti, 0.5, lambda a, x=x: varal(c, x, 540, a, t))
            elif k == 1:
                rr = 90 * (1 - 0.45 * ep(t, ti + 0.8, 4.0))
                E.foco(c, t, ti, 0.5, lambda a, x=x, rr=rr: (E.bola(c, x, 600, rr, "#F4F4F2", a), c.drawCircle(x, 600, rr, M.paint(CINZA, a, stroke=3))))
            else:
                E.foco(c, t, ti, 0.5, lambda a, x=x: chaleira(c, x - 150, 660, 110, a, t))
            E.frase(c, t, ti + 0.3, [(l1, "g", 56)], x, 860, "center")
            E.frase(c, t, ti + 0.8, [(l2, "i", 56, COR)], x, 940, "center")
        E.frase(c, t, C["s01.d"], ps("o que está acontecendo?", "i", 76, TINTA2), W / 2, 200, "center", 0.12)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("sólido,", "g", 70), ("líquido", "g", 70), ("e", "i", 74), ("gás", "g", 70, COR)]),
                 (C["s02.c"], [("as", "i", 74), ("seis", "g", 70, COR), ("mudanças", "g", 70)]),
                 (C["s02.d"], [("quando", "i", 74), ("recebe", "g", 70), ("calor", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula passada", "i", 80, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], ps("tudo é feito de", "i", 90) + [("partículas", "g", 90, COR)], XE, 400, passo=0.14)
    Q.formula_em(c, t, C["s03.b"], "H2O", XE, 640, 170)
    E.frase(c, t, C["s03.b"] + 0.6, [("=", "g", 70, TINTA2)] + ps("uma molécula", "i", 70, TINTA2), XE + 380, 620, passo=0.12)
    E.frase(c, t, C["s03.c"], ps("e elas", "i", 76) + [("nunca", "g", 72, COR), ("param", "g", 72)], XE, 860, passo=0.14)
    for k, (dx, dy, g) in enumerate(((0, 0, 20), (180, 120, 200), (-150, 160, 90), (100, -140, 300))):
        mexe = 14 * ep(t, C["s03.c"], 0.5)
        E.foco(c, t, C["s03.b"] + 0.3 + 0.2 * k, 0.4, lambda a, dx=dx, dy=dy, g=g, k=k, mexe=mexe: Q.molecula_desenho(
            c, "H2O", 1450 + dx + mexe * math.sin(t * 6 + k), 540 + dy + mexe * math.cos(t * 5 + k), 100, a, giro=g + 3 * mexe * math.sin(t * 4 + k)))


# ---------------- estados ----------------
def b_estados(c, t, C, b):
    if t < C["s07"]:
        def tres():
            w, h, y = 440, 420, 300
            caixa_estado(c, t, C["s04.a"], 140, y, w, h, "solido", 30, "sólido")
            E.frase(c, t, C["s04.b"], ps("só tremem no lugar", "i", 48, TINTA2), 360, 220, "center", 0.08)
            pilula_em(c, t, C["s04.c"], "forma própria", 360, 940, 44, TINTA)
            caixa_estado(c, t, C["s05.a"], 740, y, w, h, "liquido", 22, "líquido")
            E.frase(c, t, C["s05.b"], ps("escorregam umas sobre as outras", "i", 44, TINTA2), 960, 220, "center", 0.08)
            pilula_em(c, t, C["s05.c"], "forma do copo, mesmo volume", 960, 940, 40, TINTA)
            caixa_estado(c, t, C["s06.a"], 1340, y, w, h, "gas", 10, "gás")
            E.frase(c, t, C["s06.b"], ps("voam, bem afastadas", "i", 48, TINTA2), 1560, 220, "center", 0.08)
            pilula_em(c, t, C["s06.c"], "ocupa todo o espaço", 1560, 940, 44, TINTA)
            if t >= C["s06.a"]:
                q = ep(t, C["s06.a"] + 1.0, 0.6)
                M.arrow(c, 380, 1030, 1540, 1030, E.COR, q, 6, 22, ease_io(prog(t, C["s06.a"] + 1.0, 1.0)))
                E.foco(c, t, C["s06.a"] + 1.6, 0.4, lambda a: E.escreve(c, "mais agitação", 1580, 1045, 44, "b", COR, a))
        E.saida(c, t, C["s07"] - 0.1, tres)
        return
    E.frase(c, t, C["s07.a"], ps("o que muda a agitação?", "i", 66, TINTA2), XE, 190, passo=0.1)
    E.frase(c, t, C["s07.a"] + 1.0, [("calor", "g", 120, COR)], XE, 340)
    E.frase(c, t, C["s07.a"] + 1.6, ps("energia que vai do mais quente para o mais frio", "i", 50, TINTA2), XE, 430, passo=0.06)
    w, h, y = 560, 320, 520
    t1 = C["s07.b"] + 0.4
    caixa_estado(c, t, C["s07.b"], 160, y, w, h, "liquido", 20, tp=relogio_part(t, t1, 3.0))
    E.foco(c, t, C["s07.b"] + 0.2, 0.4, lambda a: chama(c, 440, y + h + 100, 80, a, t))
    E.frase(c, t, C["s07.b"] + 0.4, [("recebe", "g", 56, QUENTE), ("calor:", "i", 60), ("agita", "i", 60), ("mais", "g", 56)], 440, 1020, "center", 0.12)
    t2 = C["s07.c"] + 0.4
    caixa_estado(c, t, C["s07.c"], 1200, y, w, h, "liquido", 20, tp=relogio_part(t, t2, 0.25), semente=5)
    E.foco(c, t, C["s07.c"] + 0.2, 0.4, lambda a: floco(c, 1480, y + h + 70, 40, a))
    E.frase(c, t, C["s07.c"] + 0.4, [("perde", "g", 56, FRIO), ("calor:", "i", 60), ("agita", "i", 60), ("menos", "g", 56)], 1480, 1020, "center", 0.12)


# ---------------- mudanças ----------------
def b_mudancas(c, t, C, b):
    tl = {"fusão": C["s08.a"], "solidificação": C["s08.b"], "vaporização": C["s09.a"], "condensação": C["s09.b"],
          "sublimação": C["s10.a"], "ressublimação": C["s10.c"]}
    if t < C["s11"]:
        def tri():
            triangulo_estados(c, t, C["s08"], tl)
            exemplo(c, t, [(C["s08.a"] + 0.8, "o gelo derretendo"), (C["s08.b"] + 0.8, "a água virando gelo"),
                           (C["s09.c"], "o espelho embaçado"), (C["s10.b"], "naftalina, gelo seco"),
                           (C["s10.d"], "o gelo na parede do congelador")], 90, 180)
        E.saida(c, t, C["s11"] - 0.1, tri)
        return
    # s11: os três jeitos da vaporização
    E.frase(c, t, C["s11"], [("vaporização:", "g", 72, COR)] + ps("três jeitos", "i", 76), W / 2, 180, "center", 0.12)
    cols = ((C["s11.a"], 360, "evaporação", "lenta, só na superfície"), (C["s11.b"], 960, "ebulição", "rápida, bolhas no líquido todo"),
            (C["s11.c"], 1560, "calefação", "a gota pula na chapa quente"))
    for k, (ti, x, nome, txt) in enumerate(cols):
        if t < ti:
            continue
        q = ep(t, ti, 0.5)
        if k == 0:
            Q.bequer(c, t, ti, x, 700, 280, 300, 0.55, Q.AGUA, graduacao=False)
            for j in range(3):
                u = (t * 0.3 + j / 3) % 1
                E.bola(c, x - 60 + 60 * j, 520 - u * 160, 12, E.COR, q * (1 - u))
        elif k == 1:
            Q.bequer(c, t, ti, x, 700, 280, 300, 0.7, Q.AGUA, graduacao=False)
            for j in range(7):
                u = (t * 0.8 + j / 7) % 1
                c.drawCircle(x - 100 + 33 * j, 690 - u * 190, 9 + 8 * u, M.paint(BR, q * 0.9, stroke=4))
            chama(c, x, 820, 80, q, t)
        else:
            M.rrect(c, x - 180, 640, 360, 50, 12, "#2A2B31", q)
            M.rrect(c, x - 170, 690, 340, 20, 8, "#E5322D", q * (0.6 + 0.2 * math.sin(t * 5)))
            yy = 600 - 40 * abs(math.sin(t * 3))
            E.bola(c, x, yy, 30, Q.AGUA, q)
            for j in (-1, 1):
                M.line(c, x + j * 50, 625, x + j * 80, 610, CINZA, q, 4)
        E.frase(c, t, ti + 0.2, [(nome, "g", 62)], x, 900, "center")
        E.frase(c, t, ti + 0.5, ps(txt, "i", 44, TINTA2), x, 970, "center", 0.06)


# ---------------- calor ----------------
def b_calor(c, t, C, b):
    def cor(nome):
        return QUENTE if nome in ABSORVE else FRIO
    tl = {"fusão": C["s12.c"], "vaporização": C["s12.c"] + 0.4, "sublimação": C["s12.c"] + 0.8,
          "solidificação": C["s13.a"], "condensação": C["s13.a"] + 0.4, "ressublimação": C["s13.a"] + 0.8}
    triangulo_estados(c, t, C["s12"], tl, cor_seta=cor)
    E.frase(c, t, C["s12.a"], ps("mais agitação pede", "i", 58, TINTA2), 80, 140, passo=0.1)
    E.frase(c, t, C["s12.b"], [("absorve", "g", 70, QUENTE), ("calor", "g", 70, QUENTE)], 80, 240, passo=0.12)
    E.frase(c, t, C["s13.a"] + 0.4, [("libera", "g", 70, FRIO), ("calor", "g", 70, FRIO)], 1840, 240, "right", 0.12)
    E.frase(c, t, C["s13.a"] + 0.2, ps("as outras três:", "i", 58, TINTA2), 1840, 140, "right", 0.1)
    exemplo(c, t, [(C["s12.d"], "o suor evapora e tira calor da pele"), (C["s13.b"], "a água condensa e aquece o espelho"),
                   (C["s13.c"], "a água vira gelo e perde calor")], 1120, 1050, 44)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.foco(c, t, C["s14"] + 0.3, 0.6, lambda a: chaleira(c, 560, 700, 190, a, t, nuvem=1.0))

    def errado():
        E.frase(c, t, C["s14.a"], ps("a fumaça branca é", "i", 64), 1100, 400, passo=0.1)
        E.frase(c, t, C["s14.a"] + 1.0, [("vapor?", "g", 90, ERRADO)], 1100, 530)
        if t >= C["s14.b"]:
            E.risco(c, 1090, 545, 1420, 450, t, C["s14.b"], largura=10)
            E.frase(c, t, C["s14.b"] + 0.3, ps("o vapor é invisível", "i", 60, TINTA2), 1100, 660, passo=0.1)
    E.saida(c, t, C["s15.a"] - 0.1, errado)
    if t < C["s15.a"]:
        return
    bx, by = 560 + 190 * 1.62, 700 - 190 * 0.52
    E.foco(c, t, C["s15.a"], 0.4, lambda a: (M.line(c, bx + 10, by - 10, bx + 60, by - 140, TINTA2, a, 3, dash=[8, 8]),
                                            E.escreve(c, "vapor: invisível", bx - 120, by - 160, 48, "b", TINTA2, a)))
    E.frase(c, t, C["s15.b"], ps("ele condensa em", "i", 64), 1150, 560, passo=0.1)
    E.frase(c, t, C["s15.b"] + 0.9, [("gotinhas", "g", 76, COR), ("de", "i", 70), ("líquido", "g", 76, COR)], 1150, 660, passo=0.12)
    pilula_em(c, t, C["s15.c"], "a nuvem branca já é líquido", 1450, 790, 48, E.COR)
    E.foco(c, t, C["s15.d"], 0.4, lambda a: E.escreve(c, "no bico, quente: quase não se vê nada", 1050, 920, 46, "i", TINTA2, a))


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s16.a"], ps("o atalho:", "i", 66, CLARO) + [("a escada", "g", 64, BR)], XE, 150, passo=0.12)
    degraus = (("sólido", 860), ("líquido", 640), ("gás", 420))
    for k, (nome, y) in enumerate(degraus):
        x0 = 220 + k * 300
        E.foco(c, t, C["s16.b"] + 0.3 * k, 0.5, lambda a, x0=x0, y=y, nome=nome: (
            M.rrect(c, x0, y, 300, 1000 - y, 16, "#1B1C26", a), c.drawRect(skia.Rect.MakeXYWH(x0, y, 300, 10), M.paint(E.CLARO, a)),
            centro(c, nome, x0 + 150, y + 90, 56, "g", BR, a)))
    E.foco(c, t, C["s16.c"], 0.5, lambda a: (M.arrow(c, 380, 800, 980, 370, QUENTE, a, 10, 34, ease_io(prog(t, C["s16.c"], 0.8))),
                                            E.escreve(c, "subir = absorve calor", 1180, 400, 56, "g", "#F5A04A", a)))
    E.foco(c, t, C["s16.d"], 0.5, lambda a: (M.arrow(c, 900, 270, 300, 700, FRIO, a, 10, 34, ease_io(prog(t, C["s16.d"], 0.8))),
                                            E.escreve(c, "descer = libera calor", 1180, 580, 56, "g", "#6FA8FF", a)))
    E.frase(c, t, C["s17.a"], ps("fusão, vaporização, sublimação", "i", 44, "#F5C08A"), 1180, 470, passo=0.08)
    E.frase(c, t, C["s17.b"], ps("solidificação, condensação,", "i", 44, "#A9C8FF"), 1180, 650, passo=0.08)
    E.frase(c, t, C["s17.b"] + 0.5, ps("ressublimação", "i", 44, "#A9C8FF"), 1180, 710, passo=0.08)
    E.frase(c, t, C["s17.c"], ps("cada degrau para cima", "i", 48, CLARO), 1180, 830, passo=0.08)
    E.frase(c, t, C["s17.c"] + 0.6, ps("pede mais agitação", "i", 48, CLARO), 1180, 890, passo=0.08)
    pilula_em(c, t, C["s18.a"], "não diz a temperatura: próxima aula", 1480, 1000, 44, E.COR)


# ---------------- questão ----------------
def poca(c, cx, cy, a):
    p = skia.Path(); p.addOval(skia.Rect.MakeXYWH(cx - 170, cy - 40, 340, 80))
    c.drawPath(p, M.paint(Q.AGUA, a)); c.drawPath(p, M.paint("#8FC3DA", a, stroke=4))


def forminha(c, cx, cy, a):
    M.rrect(c, cx - 170, cy - 50, 340, 100, 14, "#DDE3EA", a, stroke=4, stroke_color=Q.VIDRO)
    for k in range(4):
        M.rrect(c, cx - 155 + 80 * k, cy - 35, 66, 70, 10, Q.AGUA, a)


def b_questao(c, t, C, b):
    E.frase(c, t, C["s19"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s19"] + 1.0, ps("nome da mudança + absorve ou libera?", "i", 56, TINTA2), XE, 280, passo=0.08)
    itens = ((C["s19.a"], "a poça some do chão", poca), (C["s19.b"], "a naftalina diminui", None), (C["s19.c"], "a água vira gelo na forminha", forminha))
    for k, (ti, txt, fn) in enumerate(itens):
        y = 470 + 200 * k
        E.frase(c, t, ti, [(str(k + 1), "g", 60, COR)] + ps(txt, "i", 64), XE, y, passo=0.1)
        if t < C["s20"]:
            if fn:
                E.foco(c, t, ti + 0.3, 0.4, lambda a, fn=fn, y=y: fn(c, 1450, y - 20, a))
            else:
                E.foco(c, t, ti + 0.3, 0.4, lambda a, y=y: E.bola(c, 1450, y - 20, 50, "#F4F4F2", a))
    if t >= C["s20"]:
        E.relogio(c, t, C["s20.a"], cx=1500, cy=520, r=190)


# ---------------- resposta ----------------
def linha_resp(c, t, t0, t1, y, evento, nome, sobe):
    E.frase(c, t, t0, ps(evento, "b", 50, TINTA2), XE, y, passo=0.08)
    E.frase(c, t, t1, [(nome, "g", 66, COR)], 900, y)
    cor = QUENTE if sobe else FRIO
    E.foco(c, t, t1 + 0.5, 0.4, lambda a: (M.arrow(c, 1420, y + (10 if sobe else -50), 1420, y + (-50 if sobe else 10), cor, a, 9, 26),
                                          E.escreve(c, "absorve" if sobe else "libera", 1480, y, 60, "g", cor, a)))


def b_resposta(c, t, C, b):
    linha_resp(c, t, C["s21.a"], C["s21.b"], 330, "líquido → gás, sem ferver", "evaporação", True)
    linha_resp(c, t, C["s22.a"], C["s22.b"], 540, "sólido → gás direto", "sublimação", True)
    linha_resp(c, t, C["s22.c"], C["s22.d"], 750, "líquido → sólido", "solidificação", False)

    def erro():
        E.foco(c, t, C["s22.e"], 0.4, lambda a: E.escreve(c, "o congelador dá frio à água", XE, 950, 56, "i", ERRADO, a))
        if t >= C["s22.e"] + 0.8:
            E.risco(c, XE - 10, 965, XE + 720, 915, t, C["s22.e"] + 0.8, largura=8)
    erro()
    pilula_em(c, t, C["s22.f"], "a água perde calor para ele", 1380, 935, 50, FRIO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s23"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s23.a", [("agitação", "g", 66, COR), ("define", "i", 70), ("o", "i", 70), ("estado", "g", 66)]),
                 ("s23.b", [("seis", "g", 66, COR), ("mudanças,", "g", 66), ("em", "i", 70), ("pares", "i", 70)]),
                 ("s23.c", [("subir", "g", 66, QUENTE), ("absorve,", "i", 70), ("descer", "g", 66, FRIO), ("libera", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 190
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s24"] - 0.1, resumo)
    if t < C["s24"]:
        return
    E.frase(c, t, C["s24"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s24.a"], [("Curva", "g", 110, COR), ("de", "i", 110), ("aquecimento", "g", 110, COR)], XE, 400, passo=0.14)
    Q.aquecimento(c, t, C["s24.a"] + 0.6, XE + 120, 520, 760, 400, 0, 100, -20, 120, rotulos=False, d=1.6, size=36)
    E.foco(c, t, C["s24.b"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 560, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s24.b"] + 0.3, 0.8))
    E.cursor(c, lerp(1860, 1690, p), lerp(860, 585, p), ep(t, C["s24.b"] + 0.2, 0.4))
    E.frase(c, t, C["s24.c"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1560, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, estados=b_estados, mudancas=b_mudancas, calor=b_calor, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
