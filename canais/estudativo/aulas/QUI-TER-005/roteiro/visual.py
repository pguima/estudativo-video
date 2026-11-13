"""Visual — Estudativo · QUI-TER-005: colisões e fatores da velocidade.

Segue a LINGUAGEM VISUAL DA QUÍMICA (QUI-MIS-001), da trilha (QUI-TER-001) e da Cinética (QUI-TER-004).
Nesta aula: COLISÃO = duas partículas que se aproximam (batida); a efetiva vira molécula com um clarão turquesa, a não efetiva
volta e leva um "×" cinza. Partículas agitadas = Q.particulas em estado "gas"; mais quente = o mesmo desenho com o relógio
acelerado (o tempo passado a Q.particulas corre mais rápido), mais concentrado = mais partículas na mesma caixa.
Cada fator ganha uma pílula-resumo "↑ colisões efetivas ↑ velocidade".
Peças candidatas ao kit: batida (colisão efetiva ou não), caixa_part (caixa com partículas e rótulo), comprimido (disco efervescente).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Termoquímica e Cinética")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-TER-005_colisoes_fatores_velocidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("colisoes", "superficie", "temperatura", "concentracao", "atalho", "questao", "fim"))
BR = "#FFFFFF"
QUENTE, FRIO = "#E8590C", "#4DABF7"

assert 6 * 4 == 24 and 8 * 6 == 48 and 48 == 2 * 24     # faces do cubo de 8 cubinhos
assert (40 - 20) // 10 == 2 and 2 ** 2 == 4             # dois saltos de 10 °C: 4 vezes


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def batida(c, t, t0, cx, cy, ok, d=1.4, r=44, escuro=False):
    """duas partículas que se encontram: ok=True vira molécula (clarão); ok=False bate e volta (×)"""
    if t < t0:
        return
    u = prog(t, t0, d)
    if u < 0.5:
        k = ease_io(u / 0.5)
        dx = lerp(260, r * 0.9, k)
    elif ok:
        dx = r * 0.9
    else:
        dx = lerp(r * 0.9, 260, ease_io((u - 0.5) / 0.5))
    ang = 0 if ok else 18
    if ok and u >= 0.5:
        q = ep(t, t0 + d * 0.5, 0.3) * (1 - ep(t, t0 + d * 0.5 + 0.3, 0.5))
        c.drawCircle(cx, cy, r * 2.6, M.paint(E.COR, 0.35 * q))
        M.line(c, cx - dx, cy, cx + dx, cy, Q.LIGA, 1, 12)
    Q.atomo(c, cx - dx, cy - math.sin(math.radians(ang)) * (dx - r), r, "O", escuro=escuro)
    Q.atomo(c, cx + dx, cy + math.sin(math.radians(ang)) * (dx - r), r * 0.8, "H", escuro=escuro)
    if not ok and u > 0.55:
        q = ep(t, t0 + d * 0.55, 0.3)
        M.line(c, cx - 22, cy - 22, cx + 22, cy + 22, CINZA, q, 7)
        M.line(c, cx + 22, cy - 22, cx - 22, cy + 22, CINZA, q, 7)


def caixa_part(c, t, t0, x, y, w, h, n, rel=1.0, rotulo=None, cor_r=None, semente=1):
    """caixa com partículas de gás; rel acelera o movimento (mais quente)"""
    q = ep(t, t0, 0.5)
    if q <= 0:
        return
    M.rrect(c, x, y, w, h, 24, "#FFFFFF", q, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 24, 24), M.paint(cor_r or TINTA2, q, stroke=5))
    Q.particulas(c, t0 + (t - t0) * rel, x + 14, y + 14, w - 28, h - 28, n, "gas", tipos=[("O", 0.5), ("H", 0.5)], r=15, semente=semente, a=q)
    if rotulo:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, rotulo, x + w / 2, y + h + 66, 52, "g", cor_r or TINTA, a))


def comprimido(c, cx, cy, r, a=1.0, po=0.0, semente=2):
    """comprimido inteiro (po=0) ou em pó (po=1)"""
    if a <= 0:
        return
    if po < 1:
        c.drawOval(skia.Rect.MakeLTRB(cx - r, cy - r * 0.35, cx + r, cy + r * 0.35), M.paint("#FFFFFF", a * (1 - po)))
        c.drawOval(skia.Rect.MakeLTRB(cx - r, cy - r * 0.35, cx + r, cy + r * 0.35), M.paint("#B9C2CC", a * (1 - po), stroke=4))
    if po > 0:
        import random
        rnd = random.Random(semente)
        for k in range(70):
            px, py = cx + rnd.uniform(-r * 1.1, r * 1.1), cy + rnd.uniform(-r * 0.25, r * 0.25)
            c.drawCircle(px, py, 6, M.paint("#FFFFFF", a * po))
            c.drawCircle(px, py, 6, M.paint("#B9C2CC", a * po, stroke=2))


def bolhas(c, t, t0, cx, yb, w, n, a=1.0):
    if t < t0:
        return
    for k in range(n):
        ph = ((t * 0.7 + k * 0.37) % 1.0)
        c.drawCircle(cx - w / 2 + (k * 53 % int(w)), yb - ph * 300, 9 + (k % 3) * 2, M.paint(TINTA2, 0.6 * a * (1 - ph), stroke=3))


def resumo_fator(c, t, t0, cx, cy, txt="mais colisões efetivas: mais rápido"):
    pilula_em(c, t, t0, txt, cx, cy, 46, E.COR)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, (cx, tt, po) in enumerate(((620, C["s01.b"], 0.0), (1300, C["s01.c"], 1.0))):
            Q.bequer(c, t, C["s01.a"], cx, 900, 380, 420, 0.72, Q.AGUA, graduacao=False)
            dissolve = ep(t, C["s01.d"], 3.0) * (1.0 if po else 0.3)
            E.foco(c, t, tt, 0.4, lambda a, cx=cx, po=po, dissolve=dissolve: comprimido(c, cx, 860, 120 if not po else 130, a * (1 - dissolve), po))
            bolhas(c, t, tt + 0.3, cx, 860, 300, 6 if not po else 18, 1 - 0.7 * ep(t, C["s01.d"] + 2.5, 1.0) if po else 1)
            E.foco(c, t, tt, 0.4, lambda a, cx=cx, po=po: centro(c, "em pó" if po else "inteiro", cx, 400, 64, "g", COR if po else TINTA, a))
        E.frase(c, t, C["s01.a"], ps("dois comprimidos iguais", "i", 70), W / 2, 200, "center", 0.12)
        pilula_em(c, t, C["s01.d"] + 0.4, "o pó some antes", 1680, 330, 46, E.COR)
        E.frase(c, t, C["s01.e"], ps("com a mesma quantidade de remédio", "i", 56, TINTA2), W / 2, 1010, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1640, 640, 220 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], [("teoria", "g", 100, COR), ("das", "i", 100), ("colisões", "g", 100, COR)], XE, 300, passo=0.14)
    lista(c, t, [(C["s02.b"], [("por", "i", 74), ("que", "i", 74), ("a", "i", 74), ("geladeira", "g", 70), ("conserva", "i", 74)]),
                 (C["s02.c"], [("o", "i", 74), ("que", "i", 74), ("muda", "i", 74), ("com", "i", 74), ("a", "i", 74), ("concentração", "g", 70)])], XE, 520, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 80, TINTA2), XE, 240, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.formula(c, "v = f{Δ[ ]}{Δt}", XE, 480, 120, "g", TINTA, a))
    E.foco(c, t, C["s03.a"] + 0.6, 0.4, lambda a: E.escreve(c, "mol/L por minuto", XE + 520, 470, 56, "i", TINTA2, a))
    E.frase(c, t, C["s03.b"], [("concentração", "g", 64, COR), ("=", "g", 64, TINTA2)] + ps("quanto há em cada litro", "i", 68), XE, 760, passo=0.12)


# ---------------- teoria das colisões ----------------
def b_colisoes(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], ps("para reagir, as partículas precisam se", "i", 66) + [("encontrar", "g", 62, COR)], XE, 200, passo=0.1)
            caixa_part(c, t, C["s04.b"] - 0.3, 360, 300, 1200, 520, 36, rel=1.0, semente=5)
            E.frase(c, t, C["s04.c"], ps("só reage quando há uma", "i", 66) + [("batida", "g", 62, COR)], W / 2, 960, "center", 0.12)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        E.frase(c, t, C["s05.a"], ps("nem toda batida dá certo", "i", 72), W / 2, 170, "center", 0.12)
        E.frase(c, t, C["s05.b"], [("1", "g", 60, COR), ("energia", "g", 60), ("mínima", "i", 64)], XE, 320, passo=0.12)
        E.frase(c, t, C["s05.c"], [("2", "g", 60, COR), ("posição", "g", 60), ("certa", "i", 64)], XE, 420, passo=0.12)
        batida(c, t, C["s05.b"] + 0.3, 1350, 340, False, d=1.6)
        batida(c, t, C["s05.d"], 1350, 640, True, d=1.6)
        E.foco(c, t, C["s05.d"] + 0.8, 0.4, lambda a: (E.escreve(c, "colisão", XE, 640, 84, "g", COR, a), E.escreve(c, "efetiva", XE, 740, 84, "g", COR, a)))
        E.foco(c, t, C["s05.d"] + 1.4, 0.4, lambda a: E.escreve(c, "forma produto", XE + 420, 690, 54, "i", TINTA2, a))
        E.foco(c, t, C["s05.e"], 0.4, lambda a: (E.escreve(c, "as outras: batem e voltam", 1100, 470, 46, "i", TINTA2, a)))
        return
    E.frase(c, t, C["s06.a"], ps("mais", "i", 84) + [("colisões efetivas", "g", 80, COR)] + ps("por segundo", "i", 84), W / 2, 400, "center", 0.12)
    E.frase(c, t, C["s06.b"], [("=", "g", 90, TINTA2), ("reação mais rápida", "g", 90)], W / 2, 560, "center", 0.12)
    for k, s in enumerate(("superfície", "temperatura", "concentração")):
        pilula_em(c, t, C["s06.c"] + 0.4 * k, s, 460 + k * 500, 800, 56, TINTA)


# ---------------- superfície de contato ----------------
def b_superficie(c, t, C, b):
    if t < C["s08"]:
        def s07():
            E.frase(c, t, C["s07.a"], [("1", "g", 70, COR), ("superfície", "g", 76), ("de", "i", 80), ("contato", "g", 76)], XE, 200, passo=0.12)
            for k, (cx, tt, po, rot) in enumerate(((620, C["s07.b"], 0.0, "só a parte de fora"), (1300, C["s07.d"], 1.0, "quase tudo exposto"))):
                Q.bequer(c, t, tt, cx, 880, 380, 400, 0.72, Q.AGUA, graduacao=False)
                E.foco(c, t, tt + 0.2, 0.4, lambda a, cx=cx, po=po: comprimido(c, cx, 840, 130, a, po))
                bolhas(c, t, tt + 0.4, cx, 840, 300, 5 if not po else 18)
                E.foco(c, t, tt + 0.4, 0.4, lambda a, cx=cx, rot=rot: centro(c, rot, cx, 980, 50, "i", TINTA2, a))
            E.foco(c, t, C["s07.c"], 0.4, lambda a: centro(c, "o miolo espera", 620, 400, 54, "g", TINTA, a))
            resumo_fator(c, t, C["s07.e"], 1300, 400)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    E.frase(c, t, C["s08"], ps("conte as faces", "i", 70, TINTA2), XE, 180, passo=0.12)
    E.cubo(c, t, C["s08.a"] - 0.3, 300, 760, 300, None)
    for k in (1,):
        pass
    if t >= C["s08.a"]:
        q = ep(t, C["s08.a"], 0.4)
        M.line(c, 300 + 150, 760, 300 + 150, 460, TINTA2, q, 3)
        M.line(c, 300, 610, 600, 610, TINTA2, q, 3)
    E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: (E.formula(c, "6 × 4 = 24 faces", 230, 900, 64, "g", TINTA, a)))
    for k in range(8):
        tk = C["s08.b"] + 0.15 * k
        x = 1000 + (k % 4) * 210
        y = 560 + (k // 4) * 230
        if t >= tk:
            E.cubo(c, t, tk, x, y, 120, None)
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.formula(c, "8 × 6 = 48 faces", 1000, 900, 64, "g", COR, a))
    pilula_em(c, t, C["s08.e"], "o dobro de superfície, a mesma massa", W / 2, 1010, 50, E.COR)


# ---------------- temperatura ----------------
def geladeira(c, x, y, w, h, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x, y, w, h, 30, "#E9EEF3", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30), M.paint("#9DB3C2", a, stroke=5))
    M.line(c, x, y + h * 0.36, x + w, y + h * 0.36, "#9DB3C2", a, 5)
    M.rrect(c, x + w - 50, y + 60, 18, 120, 9, "#9DB3C2", a)
    M.rrect(c, x + w - 50, y + h * 0.36 + 50, 18, 160, 9, "#9DB3C2", a)
    E.escreve(c, "4 °C", x + 40, y + h * 0.36 + 120, 70, "g", FRIO, a)


def b_temperatura(c, t, C, b):
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("2", "g", 70, COR), ("temperatura", "g", 76)], XE, 190, passo=0.12)
            E.frase(c, t, C["s09.b"], ps("mede o quanto as partículas", "i", 64) + [("se agitam", "g", 60, COR)], XE, 290, passo=0.1)
            caixa_part(c, t, C["s09.c"] - 0.4, 260, 360, 620, 400, 22, rel=0.35, rotulo="frio", cor_r=FRIO, semente=3)
            caixa_part(c, t, C["s09.c"], 1040, 360, 620, 400, 22, rel=2.4, rotulo="quente", cor_r=QUENTE, semente=3)
            E.frase(c, t, C["s09.d"], ps("batem", "i", 60) + [("mais vezes", "g", 56)], W / 2, 1010, "center", 0.1) if t < C["s09.e"] else \
                E.frase(c, t, C["s09.e"], ps("e, principalmente,", "i", 60) + [("com mais força", "g", 56, QUENTE)], W / 2, 1010, "center", 0.1)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    E.foco(c, t, C["s10.a"], 0.5, lambda a: geladeira(c, 1200, 200, 440, 760, a))
    E.frase(c, t, C["s10.a"], ps("na geladeira, o contrário", "i", 70), XE, 240, passo=0.12)
    E.frase(c, t, C["s10.b"], ps("as reações que estragam a comida", "i", 60), XE, 380, passo=0.1)
    E.frase(c, t, C["s10.b"] + 1.4, [("ficam", "i", 64), ("mais lentas", "g", 60, FRIO)], XE, 470, passo=0.1)
    E.frase(c, t, C["s10.c"], [("não", "g", 64, ERRADO)] + ps("para:", "i", 68), XE, 660, passo=0.1)
    E.frase(c, t, C["s10.d"], [("só", "i", 68), ("desacelera", "g", 64, COR)], XE + 300, 660, passo=0.1)
    pilula_em(c, t, C["s10.d"] + 1.2, "dura mais, não para sempre", 560, 820, 50, TINTA)


# ---------------- concentração ----------------
def b_concentracao(c, t, C, b):
    if t < C["s12"]:
        def s11():
            E.frase(c, t, C["s11.a"], [("3", "g", 70, COR), ("concentração", "g", 76)], XE, 190, passo=0.12)
            caixa_part(c, t, C["s11.b"], 260, 300, 560, 420, 10, rotulo="pouca", semente=7)
            caixa_part(c, t, C["s11.b"] + 0.5, 1100, 300, 560, 420, 40, rotulo="muita", cor_r=E.COR, semente=7)
            E.frase(c, t, C["s11.b"] + 1.0, ps("mais encontros por segundo", "b", 54), W / 2, 870, "center", 0.1)
            E.frase(c, t, C["s11.c"], ps("brasa em oxigênio puro volta a acender:", "i", 54, TINTA2), W / 2, 980, "center", 0.08)
            E.foco(c, t, C["s11.d"], 0.4, lambda a: centro(c, "há mais oxigênio por litro", W / 2, 1060, 46, "b", COR, a))
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    E.frase(c, t, C["s12.a"], ps("e explica a desaceleração da aula anterior", "i", 66), W / 2, 220, "center", 0.1)
    for k, (tt, s) in enumerate(((C["s12.b"], "reagente gasto, concentração cai"), (C["s12.c"], "colisões ficam raras"), (C["s12.d"], "a velocidade diminui"))):
        y = 420 + k * 180
        E.foco(c, t, tt, 0.4, lambda a, y=y, k=k: (E.bola(c, XE + 280, y - 26, 44, a=a), centro(c, str(k + 1), XE + 280, y - 4, 54, "g", E.SOBRE, a)))
        E.foco(c, t, tt + 0.1, 0.5, lambda a, y=y, s=s: E.escreve(c, s, XE + 360, y, 70, "g", TINTA, a))
        if k:
            E.foco(c, t, tt - 0.1, 0.3, lambda a, y=y: centro(c, "↓", XE + 280, y - 110, 50, "g", TINTA2, a))


# ---------------- erro comum ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s13.a"], ps("“esquentar só faz bater mais vezes”", "i", 64, ERRADO), XE, 320, passo=0.1)
    if t >= C["s13.b"] + 0.4:
        E.risco(c, XE - 10, 335, XE + 1040, 270, t, C["s13.b"] + 0.4, largura=9)
    E.frase(c, t, C["s13.b"], ps("isso conta, mas pouco", "i", 62, TINTA2), XE, 430, passo=0.1)
    # barras: colisões com energia suficiente, frio x quente
    for k, (tt, x, alt, cor, rot) in enumerate(((C["s13.c"], 520, 90, FRIO, "frio"), (C["s13.d"], 900, 420, QUENTE, "quente"))):
        p = ease_out(prog(t, tt, 0.8))
        if p > 0:
            M.rrect(c, x, 960 - alt * p, 200, alt * p, 14, cor, 1)
            E.foco(c, t, tt, 0.4, lambda a, x=x, rot=rot: centro(c, rot, x + 100, 1030, 50, "g", TINTA, a))
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.escreve(c, "batidas com a energia mínima", 300, 520, 52, "b", TINTA, a))
    E.frase(c, t, C["s13.e"], ps("poucos graus a mais", "i", 60), 1200, 720, passo=0.1)
    E.frase(c, t, C["s13.e"] + 0.6, [("aceleram muito", "g", 60, QUENTE)], 1200, 810, passo=0.1)


# ---------------- atalho (palco) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        def s14():
            E.frase(c, t, C["s14.a"], ps("pergunte:", "i", 70, CLARO) + [("mais ou menos colisões efetivas?", "g", 62, BR)], W / 2, 180, "center", 0.12)
            linhas = ((C["s14.b"], "picar, triturar, moer", "↑"), (C["s14.c"], "esquentar", "↑"), (C["s14.d"], "concentrar", "↑"),
                      (C["s14.e"], "esfriar, diluir, pedaço grande", "↓"))
            for k, (tt, s, sn) in enumerate(linhas):
                y = 380 + k * 150
                cor = E.CLARO if sn == "↑" else FRIO
                E.foco(c, t, tt, 0.4, lambda a, y=y, s=s: E.escreve(c, s, XE + 100, y, 66, "b", BR, a))
                E.foco(c, t, tt + 0.2, 0.4, lambda a, y=y, sn=sn, cor=cor: E.escreve(c, sn + " velocidade", 1260, y, 66, "g", cor, a))
        E.saida(c, t, C["s15"] - 0.1, s14)
        return
    E.frase(c, t, C["s15.a"], ps("regra aproximada, se a questão der:", "i", 64, CLARO), W / 2, 220, "center", 0.1)
    E.frase(c, t, C["s15.b"], [("+10 °C", "g", 80, BR), ("→", "g", 80, CLARO), ("velocidade × 2", "g", 80, E.CLARO)], W / 2, 380, "center", 0.12)
    E.foco(c, t, C["s15.c"], 0.5, lambda a: E.formula(c, "20 °C → 30 °C → 40 °C", W / 2, 560, 80, "g", BR, a, "center"))
    E.foco(c, t, C["s15.d"], 0.5, lambda a: E.formula(c, "2 × 2 = 4 vezes mais rápido", W / 2, 720, 80, "g", E.CLARO, a, "center"))
    pilula_em(c, t, C["s15.e"], "só se o enunciado der a regra", W / 2, 900, 52, TINTA2)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar: qual é o fator?", "i", 72, COR), XE, 170, passo=0.1)
    itens = ((C["s16.a"], "palha de aço enferruja antes do prego"), (C["s16.b"], "leite fora da geladeira azeda antes"),
             (C["s16.c"], "vinagre mais concentrado: mais bolhas na casca de ovo"))
    for k, (tt, s) in enumerate(itens):
        y = 360 + k * 170
        E.foco(c, t, tt, 0.4, lambda a, y=y, k=k: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(k + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.foco(c, t, tt + 0.1, 0.5, lambda a, y=y, s=s: E.escreve(c, s, XE + 110, y, 58, "i", TINTA, a))
    E.relogio(c, t, C["s17.a"], cx=W / 2, cy=850, r=80)


def b_resposta(c, t, C, b):
    linhas = ((C["s18.a"], "palha de aço", "superfície de contato", C["s18.b"]), (C["s18.c"], "leite fora da geladeira", "temperatura", C["s18.d"]),
              (C["s18.e"], "vinagre mais concentrado", "concentração", C["s18.f"]))
    for k, (tt, s, f, tf) in enumerate(linhas):
        y = 280 + k * 250
        E.foco(c, t, tt, 0.4, lambda a, y=y, k=k: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(k + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.foco(c, t, tt + 0.1, 0.4, lambda a, y=y, s=s: E.escreve(c, s, XE + 110, y, 66, "i", TINTA, a))
        pilula_em(c, t, tf, f, 1450, y - 22, 56, E.COR)
    E.foco(c, t, C["s18.b"] + 0.4, 0.4, lambda a: E.escreve(c, "fios finos: muito ferro exposto ao ar", XE + 110, 360, 44, "i", TINTA2, a))
    E.foco(c, t, C["s18.d"] + 0.4, 0.4, lambda a: E.escreve(c, "mais quente: mais colisões efetivas", XE + 110, 610, 44, "i", TINTA2, a))
    E.foco(c, t, C["s18.f"] + 0.4, 0.4, lambda a: E.escreve(c, "mais ácido por litro: mais encontros", XE + 110, 860, 44, "i", TINTA2, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        E.frase(c, t, C["s19.a"], ps("reação acontece por", "i", 74) + [("colisão efetiva", "g", 70, COR)], W / 2, 380, "center", 0.12)
        for k, s in enumerate(("superfície", "temperatura", "concentração")):
            pilula_em(c, t, C["s19.b"] + 0.4 * k, s, 460 + k * 500, 620, 60, TINTA)
        E.frase(c, t, C["s19.b"] + 1.4, ps("aumentam essas colisões", "i", 66), W / 2, 820, "center", 0.12)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s20.a"], [("energia", "g", 110, COR), ("de", "i", 110), ("ativação", "g", 110, COR)], XE, 420)
    E.frase(c, t, C["s20.b"], ps("e o catalisador, que acelera sem ser gasto", "i", 60, TINTA2), XE, 560, passo=0.1)
    E.frase(c, t, C["s20.c"], ps("como as enzimas", "i", 60, TINTA2), XE, 650, passo=0.1)
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 800, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(1000, 825, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, colisoes=b_colisoes, superficie=b_superficie, temperatura=b_temperatura,
              concentracao=b_concentracao, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
