"""Visual — Estudativo · MAT-ARE-012: praticando círculo, figuras compostas e razão entre áreas (quatro situações). Fecha a trilha.
Aula de prática no molde da MAT-ARE-007 (e da MAT-ANG-019): selo "situação n de 4", figura à esquerda, pergunta embaixo à direita e
relógio de pausa; na resposta, a mesma figura ganha as medidas e a conta vai para a coluna da direita.
Linguagem da trilha (MAT-ARE-001 a 011): figuras em tinta, região da área pintada clara; pedaços de círculo que se JUNTAM num círculo
inteiro (a peça da aula: os quartos deslizam até o círculo); o furo da coroa em branco tracejado; pizza com a massa em âmbar claro
(MAT-POL-005, MAT-ARE-008); no triângulo, os dois pedaços em COR e âmbar e a altura única tracejada (MAT-ARE-011).
Medidas na grotesca; erro em vermelho, certo em verde; resposta na esfera; atalho no palco; k aparece como "k".
Peças locais: marca(), pergunta(), quarto() (quarto de círculo num canto), azulejo(), coroa_setor() (o limpador), pizza(), tri4().
Todo instante vem de C[...] (marcadores do roteiro); entre() reparte o tempo entre dois marcadores."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Áreas e Perímetros")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ARE-012_praticando_circulo_compostas_e_razao_entre_areas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "atalho", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
AZUL = "#3A7BFF"
MASSA = "#F3D9A4"
VIDRO = "#D7ECF7"
assert 8 * 8 == 64 and 4 ** 2 == 16 and 16 * 3 == 48 and 64 - 48 == 16 and 2 * 3 * 4 == 24 and 4 * 90 == 360 and 2 * 180 == 360
assert 50 ** 2 == 2500 and 10 ** 2 == 100 and 2500 - 100 == 2400 and 360 // 120 == 3 and 2400 // 3 == 800 and 800 * 3 == 2400
assert 45 / 30 == 1.5 and 15 * 15 == 225 and abs(1.5 ** 2 - 2.25) < 1e-9 and 2.25 > 2 and 80 == 2 * 40
assert 20 / 10 == 2 and 30 / 10 == 3 and 15 / 5 == 3 and 2 * 3 == 6 and 3 * 3 == 9 and 6 + 9 == 15


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def num_bola(c, s, cx, cy, r, size, a=1.0, cor=None):
    E.bola(c, cx, cy + 3, r, cor, a)
    centro(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a)


def entre(C, k1, k2, f):
    return lerp(C[k1], C[k2], f)


def pt(O, r, g):
    return O[0] + r * math.cos(math.radians(g)), O[1] - r * math.sin(math.radians(g))


def marca(c, t, t0, n, total=4):
    s = f"situação {n} de {total}"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(total):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, linhas, rel, X=1500, y0=780, dy=85):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * dy, "center", 0.12)
    E.relogio(c, t, rel, X, 370, 150)


def setor_path(O, r, g1, g2, r_in=0.0):
    """setor (ou pedaço de coroa, com r_in) de g1 a g2 graus, anti-horário"""
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    path = skia.Path()
    if r_in <= 0:
        path.moveTo(*O); path.arcTo(ret, -g1, -(g2 - g1), False); path.close()
    else:
        ri = skia.Rect.MakeXYWH(O[0] - r_in, O[1] - r_in, 2 * r_in, 2 * r_in)
        path.moveTo(*pt(O, r_in, g1)); path.arcTo(ret, -g1, -(g2 - g1), False)
        path.arcTo(ri, -g2, (g2 - g1), False); path.close()
    return path


def pinta(c, path, cor, alfa, a=1.0, borda=TINTA, larg=5):
    if a <= 0:
        return
    if alfa > 0:
        c.drawPath(path, M.paint(cor, alfa * a))
    if borda:
        p = M.paint(borda, a, stroke=larg); p.setStrokeJoin(skia.Paint.kRound_Join)
        c.drawPath(path, p)


# ---------------- S1: azulejo 8 × 8 com quartos de círculo de raio 4 (50 px por cm) ----------------
AU = 50
AX, AY, AL = 200, 330, 8 * AU
AR = 4 * AU
CANTOS = (((AX, AY + AL), 0), ((AX + AL, AY + AL), 90), ((AX + AL, AY), 180), ((AX, AY), 270))  # (canto, ângulo inicial)
CIRC = (900, AY + AL / 2)   # onde os quartos se juntam


def azulejo(c, t, t0, tq=None, junta=None, branco=None, arcos=None, lados=None, tl=None):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    c.drawRect(skia.Rect.MakeXYWH(AX, AY, AL, AL), M.paint(BR, q))
    if branco is not None:
        c.drawRect(skia.Rect.MakeXYWH(AX, AY, AL, AL), M.paint(CERTO, 0.25 * ep(t, branco, 0.5)))
    if tq is not None:
        for i, (V, g0) in enumerate(CANTOS):
            k = ep(t, tq + 0.2 * i, 0.4)
            if k > 0:
                pinta(c, setor_path(V, AR, g0, g0 + 90), AZUL, 0.75, k, None)
                if branco is None or t < branco:
                    pass
            if junta is not None and t >= junta:  # a cópia desliza até o círculo
                g = ease_io(prog(t, junta + 0.15 * i, 1.0))
                O = (lerp(V[0], CIRC[0], g), lerp(V[1], CIRC[1], g))
                pinta(c, setor_path(O, AR, g0, g0 + 90), AZUL, 0.75, 1.0, TINTA, 4)
    c.drawRect(skia.Rect.MakeXYWH(AX, AY, AL, AL), M.paint(TINTA, q, stroke=6))
    if lados is not None and t >= lados:
        k = ep(t, lados, 0.4)
        c.drawRect(skia.Rect.MakeXYWH(AX, AY, AL, AL), M.paint(ERRADO, k, stroke=12))
    if arcos is not None and t >= arcos:  # o contorno do branco: quatro arcos
        p = ease_io(prog(t, arcos, 1.0))
        for V, g0 in CANTOS:
            ret = skia.Rect.MakeXYWH(V[0] - AR, V[1] - AR, 2 * AR, 2 * AR)
            c.drawArc(ret, -g0, -90 * p, False, M.paint(E.COR, 1.0, stroke=12, cap_round=True))
    if tl is not None:
        E.foco(c, t, tl, 0.4, lambda f: (centro(c, "8 cm", AX + AL / 2, AY + AL + 70, 56, "b", TINTA, f),
                                         M.line(c, AX, AY + AL, AX + AR * 0.7, AY + AL - AR * 0.7, TINTA, f, 4),
                                         E.formula(c, "4", AX + AR * 0.42, AY + AL - AR * 0.25, 52, "g", TINTA, f, "left")))


# ---------------- S2: limpador, raios 10 e 50, 120° (9 px por cm) ----------------
LO = (560, 920)
LR, Lr = 50 * 9, 10 * 9


def limpador(c, t, t0, tr=None, ta=None, reg=None, setor_err=None, cor_reg=None):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.6))
    path = skia.Path(); path.addPoly([(80, 940), (1040, 940), (960, 360), (160, 360)], True)
    c.drawPath(path, M.paint(VIDRO, 0.95 * q))
    c.drawPath(path, M.paint(TINTA2, q, stroke=4))
    if reg is not None and t >= reg:
        p = ease_io(prog(t, reg, 0.9))
        pinta(c, setor_path(LO, LR, 30, 30 + 120 * p, Lr), cor_reg or AZUL, 0.45, 1.0, TINTA, 4)
    if setor_err is not None and t >= setor_err:
        k = ep(t, setor_err, 0.4)
        pinta(c, setor_path(LO, Lr, 30, 150), ERRADO, 0.6, k, ERRADO, 4)
    # a haste e a borracha (no meio da varredura)
    g = 90 if reg is None else 30 + 120 * ease_io(prog(t, reg, 0.9))
    M.line(c, *LO, *pt(LO, LR + 10, g), TINTA, q, 6)
    M.line(c, *pt(LO, Lr, g), *pt(LO, LR, g), TINTA, q, 14)
    c.drawCircle(*LO, 14 * q, M.paint(TINTA))
    if tr is not None:
        E.foco(c, t, tr, 0.4, lambda f: (E.pilula(c, "10 cm", LO[0] - 230, LO[1] - 20, 40, "g", fundo=TINTA, a=f),
                                         E.pilula(c, "50 cm", *pt(LO, LR * 0.75, 20), 44, "g", fundo=TINTA, a=f)))
    if ta is not None and t >= ta:
        k = ep(t, ta, 0.4)
        for gg in (30, 150):
            M.line(c, *LO, *pt(LO, LR, gg), TINTA2, k, 3, dash=[12, 10])
        c.drawArc(skia.Rect.MakeXYWH(LO[0] - 60, LO[1] - 60, 120, 120), -30, -120, False, M.paint(E.COR, k, stroke=5))
        E.foco(c, t, ta, 0.4, lambda f: centro(c, "120°", LO[0], LO[1] - 130, 50, "g", TINTA, f))


# ---------------- S3: pizzas de 30 e 45 cm (9 px por cm) ----------------
PM, PG = (290, 600), (760, 600)
RM, RG = 15 * 9, 22.5 * 9


def pizza(c, O, r, a=1.0):
    if a <= 0:
        return
    c.drawCircle(*O, r, M.paint(MASSA, a))
    for dx, dy in ((0.35, 0.2), (-0.4, 0.3), (0.1, -0.45), (-0.2, -0.1), (0.5, -0.3), (-0.1, 0.55)):
        c.drawCircle(O[0] + dx * r, O[1] + dy * r, r * 0.09, M.paint("#C8553D", 0.75 * a))
    c.drawCircle(*O, r, M.paint(AMBAR, a, stroke=max(8, r * 0.06)))


def pizzas(c, t, t0, tm=None, tg=None, tp=None):
    E.foco(c, t, tm if tm is not None else t0, 0.5, lambda f: (pizza(c, PM, RM, f), M.line(c, PM[0] - RM, PM[1], PM[0] + RM, PM[1], TINTA, f, 5),
                                                               E.pilula(c, "30 cm", PM[0], PM[1] - 40, 40, "g", fundo=TINTA, a=f)))
    E.foco(c, t, tg if tg is not None else t0, 0.5, lambda f: (pizza(c, PG, RG, f), M.line(c, PG[0] - RG, PG[1], PG[0] + RG, PG[1], TINTA, f, 5),
                                                               E.pilula(c, "45 cm", PG[0], PG[1] - 40, 44, "g", fundo=TINTA, a=f)))
    E.foco(c, t, tm if tm is not None else t0, 0.5, lambda f: E.pilula(c, "R$ 40", PM[0], PM[1] + RM + 70, 50, "g", fundo=E.COR, a=f))
    E.foco(c, t, tg if tg is not None else t0, 0.5, lambda f: E.pilula(c, "R$ 80", PG[0], PG[1] + RG + 70, 50, "g", fundo=E.COR, a=f))


# ---------------- S4: triângulo de base 15 (50 px por cm), linha do vértice até a base ----------------
TB, TC, TA = (170, 860), (170 + 15 * 50, 860), (420, 400)
TD = (170 + 6 * 50, 860)


def tri4(c, t, t0, tl=None, tareas=None, altura=None, tbases=None):
    if t < t0:
        return
    q = ease_io(prog(t, t0, 0.7))
    for pts, cor in (([TA, TB, TD], E.COR), ([TA, TD, TC], AMBAR)):
        path = skia.Path(); path.addPoly(pts, True)
        c.drawPath(path, M.paint(cor, 0.3 * ep(t, t0 + 0.4, 0.5)))
    E._contorno(c, [TB, TC, TA], q, TINTA, 6)
    M.line(c, *TA, *TD, TINTA, 1.0, 6, progress=ease_io(prog(t, t0 + 0.6, 0.5)))
    if tl is not None:
        E.foco(c, t, tl, 0.4, lambda f: (M.line(c, TB[0], TB[1] + 100, TC[0], TC[1] + 100, TINTA, f * (1 - ep(t, tbases or 1e9, 0.3)), 4),
                                         centro(c, "15 cm", (TB[0] + TC[0]) / 2, TB[1] + 165, 54, "g", TINTA, f * (1 - ep(t, tbases or 1e9, 0.3)))))
    if tareas is not None:
        E.foco(c, t, tareas, 0.4, lambda f: (E.pilula(c, "20", (TA[0] + TB[0] + TD[0]) / 3, (TA[1] + TB[1] + TD[1]) / 3 + 40, 52, "g", fundo=E.COR, a=f),
                                             E.pilula(c, "30", (TA[0] + TD[0] + TC[0]) / 3 + 20, (TA[1] + TD[1] + TC[1]) / 3 + 40, 52, "g", fundo=AMBAR, a=f)))
    if altura is not None and t >= altura:
        pe = (TA[0], TB[1])
        M.line(c, *TA, *pe, TINTA2, 1.0, 5, dash=E.TRACO, progress=ease_io(prog(t, altura, 0.5)))
        k = ep(t, altura + 0.4, 0.3)
        c.drawRect(skia.Rect.MakeXYWH(pe[0], pe[1] - 24, 24, 24), M.paint(TINTA2, k, stroke=3))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a_, b_, c_, d_ = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    E.frase(c, t, a_ + 0.1, ps("4", "g", 220, COR) + ps("situações", "g", 160, COR), XE, 330, passo=0.25)
    E.frase(c, t, a_ + 0.9, ps("criadas para esta aula", "i", 64, TINTA2), XE, 440, passo=0.1)
    for i, (s, cx) in enumerate((("círculos", 420), ("figuras recortadas", 960), ("ampliações", 1500))):
        E.foco(c, t, b_ + 0.5 * i, 0.4, lambda a, i=i, s=s, cx=cx: E.pilula(c, s, cx, 580, 58, "g", fundo=TINTA if i % 2 else E.COR, a=a))
    for i, (s, cx, ti) in enumerate((("pause", 560, c_), ("resolva", 1240, c_ + 0.9))):
        E.foco(c, t, ti, 0.5, lambda p, i=i, s=s, cx=cx: (num_bola(c, str(i + 1), cx - 190, 770, 56, 64, p),
                                                           E.escreve(c, s, cx - 110, 795, 92, "g", TINTA, p)))
    E.frase(c, t, d_, ps("o segredo:", "i", 66) + [("não fazer conta à toa", "g", 72, COR)], W / 2, 970, "center", 0.12)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"] + 0.1, ps("você vai usar", "i", 84, COR), XE, 190, passo=0.12)
    itens = (("a", "círculo:", "A = πr^2   e   C = 2πr"), ("b", "setor:", "fração do círculo"), ("c", "compostas:", "somar e tirar pedaços"),
             ("d", "ampliação:", "área × k^2"), ("e", "mesma altura:", "razão das bases"))
    for i, (k, tit, sub) in enumerate(itens):
        y = 330 + i * 135
        ti = C[f"s02.{k}"]
        E.foco(c, t, ti, 0.5, lambda p, i=i, y=y: num_bola(c, str(i + 1), XE + 46, y - 24, 42, 50, p))
        E.frase(c, t, ti + 0.1, [(tit, "g", 60)], XE + 120, y)
        E.formula_em(c, t, ti + 0.5, sub, XE + 150 + E.larg(tit, "g", 60), y, 58, "g", COR)
    E.frase(c, t, C["s02.end"] - 2.6, ps("travou? procure a aula no canal", "i", 58), XE, 1030, passo=0.1)


# ---------------- situação 1: azulejo ----------------
def b_questao1(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s03.{k}"] for k in "abcde")
    marca(c, t, a3, 1)
    azulejo(c, t, b3 - 0.3, tq=c3, tl=b3)
    E.saida(c, t, C["s04.a"] - 0.1, lambda: E.frase(c, t, b3, ps("azulejo de", "i", 62) + [("8 cm", "g", 70)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(c3, ps("4 quartos de círculo,", "i", 56) + [("raio 4", "g", 62, AZUL)]),
                    (d3, ps("área branca", "i", 58) + [("= ?", "g", 66, COR)]),
                    (e3, ps("contorno do branco", "i", 58) + [("= ?", "g", 66, COR)]),
                    (e3 + 1.2, ps("use", "i", 56) + [("π = 3", "g", 62)])], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s05.{k}"] for k in "abcde")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    X = 1540
    t0 = C["s05"] - 1.2
    azulejo(c, t, t0, tq=t0, tl=t0, junta=a5, branco=e5, arcos=a6, lados=d6)
    if t >= b6:  # a volta inteira, no círculo montado
        c.drawCircle(*CIRC, AR, M.paint(E.COR, ep(t, b6, 0.4), stroke=12))
    E.foco(c, t, b5 + 0.4, 0.4, lambda f: centro(c, "16π", CIRC[0], CIRC[1] + 26, 72, "g", BR, f))

    def um():
        E.frase(c, t, a5, ps("4 quartos =", "i", 60) + [("1 círculo", "g", 66, AZUL)], X, 220, "center", 0.12)
        fcen(c, t, b5, "π · 4^2 = 16π", X, 360, 76)
        fcen(c, t, c5, "16 · 3 = 48", X, 490, 76, AZUL)
        fcen(c, t, d5, "azulejo: 8 · 8 = 64", X, 630, 70)
        fcen(c, t, e5, "64 − 48", X, 760, 76)
        bola_txt(c, t, e5 + 0.6, "16 cm²", X, 920, 105, 56, CERTO)
    E.saida(c, t, C["s06"] - 0.1, um)
    if t >= C["s06"] - 0.1:
        E.frase(c, t, a6, ps("contorno:", "i", 62) + [("só arcos", "g", 68, COR)], X, 230, "center", 0.12)
        E.frase(c, t, b6, ps("4 quartos =", "i", 60) + [("1 volta", "g", 66, COR)], X, 360, "center", 0.12)
        fcen(c, t, c6, "2 · 3 · 4", X, 500, 80)
        bola_txt(c, t, c6 + 0.6, "24 cm", X, 680, 105, 60, CERTO)
        E.foco(c, t, d6, 0.5, lambda a: E.pilula(c, "os lados não entram", X, 880, 56, "g", fundo=ERRADO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a7, b7, c7, d7, e7, f7 = (C[f"s07.{k}"] for k in "abcdef")
    X = W / 2
    E.frase(c, t, C["s07"] + 0.2, [("atalho", "g", 90, CLARO)] + ps("do dia", "i", 76, BR), X, 160, "center", 0.12)
    E.frase(c, t, a7, ps("junte os pedaços de círculo em", "i", 62, CLARO) + [("círculos inteiros", "g", 68, BR)], X, 290, "center", 0.12)
    # quatro quartos → um círculo
    O1, r = (560, 500), 120
    if t >= b7:
        g = ease_io(prog(t, b7 + 0.3, 0.8))
        for i, g0 in enumerate((0, 90, 180, 270)):
            m = g0 + 45
            off = (1 - g) * 60
            O = pt(O1, off, m)
            pinta(c, setor_path(O, r, g0, g0 + 90), CLARO, 0.7, ep(t, b7, 0.4), BR, 3)
        E.foco(c, t, b7 + 0.2, 0.4, lambda f: centro(c, "4 × 90°", O1[0], O1[1] + r + 90, 56, "g", BR, f))
    O2 = (1360, 500)
    if t >= c7:
        g = ease_io(prog(t, c7 + 0.3, 0.8))
        for g0 in (90, 270):
            O = pt(O2, (1 - g) * 70, g0 + 90)
            pinta(c, setor_path(O, r, g0, g0 + 180), AMBAR, 0.7, ep(t, c7, 0.4), BR, 3)
        E.foco(c, t, c7 + 0.2, 0.4, lambda f: centro(c, "2 × 180°", O2[0], O2[1] + r + 90, 56, "g", BR, f))
    fcen(c, t, d7, "os ângulos somam 360°", X, 820, 70, AMBAR)
    E.foco(c, t, e7, 0.5, lambda a: E.pilula(c, "raios diferentes? não compensa", X, 920, 52, "g", fundo=ERRADO, a=a))
    E.frase(c, t, f7, ps("aí,", "i", 56, CLARO) + [("calcule cada pedaço", "g", 60, BR)], X, 1030, "center", 0.12)


# ---------------- situação 2: limpador ----------------
def b_questao2(c, t, C, b):
    a8, b8, c8, d8 = (C[f"s08.{k}"] for k in "abcd")
    marca(c, t, a8, 2)
    limpador(c, t, a8 + 0.3, tr=b8, ta=c8, reg=c8 + 0.4)
    E.saida(c, t, C["s09.a"] - 0.1, lambda: E.frase(c, t, a8 + 0.6, ps("limpador de", "i", 60) + [("para-brisa", "g", 66)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b8, ps("borracha de", "i", 56) + [("10 cm a 50 cm", "g", 62)]),
                    (c8, ps("gira", "i", 58) + [("120°", "g", 64)]),
                    (d8, ps("área limpa", "i", 58) + [("= ?", "g", 66, COR)]),
                    (d8 + 1.2, ps("use", "i", 56) + [("π = 3", "g", 62)])], C["s09.a"])


def b_resposta2(c, t, C, b):
    a10, b10, c10, d10 = (C[f"s10.{k}"] for k in "abcd")
    a11, b11, c11, d11, e11 = (C[f"s11.{k}"] for k in "abcde")
    X = 1500
    t0 = C["s10"] - 1.2
    limpador(c, t, t0, tr=t0, ta=t0, reg=t0, setor_err=d11, cor_reg=E.COR if t >= a10 else AZUL)
    if b10 <= t < a11:  # o círculo de fora e o furo, fantasmas
        k = ep(t, b10, 0.4) * (1 - ep(t, a11 - 0.4, 0.4))
        p = M.paint(TINTA2, k, stroke=3); p.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
        c.save(); c.clipRect(skia.Rect.MakeXYWH(0, 0, 1100, LO[1] + 5)); c.drawCircle(*LO, LR, p); c.restore()
        if t >= c10:
            c.drawCircle(*LO, Lr, M.paint(BR, 0.7 * ep(t, c10, 0.4)))
            c.drawCircle(*LO, Lr, M.paint(ERRADO, ep(t, c10, 0.4), stroke=4))

    def dez():
        E.frase(c, t, a10, [("pedaço de coroa", "g", 64, COR)] + ps("entre 10 e 50", "i", 58), X, 220, "center", 0.12)
        fcen(c, t, b10, "fora: π · 50^2 = 2.500π", X, 380, 64)
        fcen(c, t, c10, "dentro: π · 10^2 = 100π", X, 520, 64, ERRADO)
        fcen(c, t, d10, "coroa: 2.400π", X, 680, 76, COR)
    E.saida(c, t, C["s11"] - 0.1, dez)
    if t >= C["s11"] - 0.1:
        fcen(c, t, a11, "120° = f{1}{3} da volta", X, 220, 70, COR)
        fcen(c, t, b11, "f{1}{3} · 2.400π = 800π", X, 400, 70)
        fcen(c, t, c11, "800 · 3", X, 550, 72)
        E.foco(c, t, c11 + 0.6, 0.5, lambda a: E.pilula(c, "2.400 cm²", X, 700, 72, "g", fundo=CERTO, a=a))
        E.frase(c, t, d11, ps("erro: o", "i", 52, ERRADO) + [("setor inteiro de 50", "g", 54, ERRADO)], X, 890, "center", 0.12)
        E.frase(c, t, e11, ps("conta vidro que a borracha", "i", 48) + [("nem toca", "g", 52, ERRADO)], X, 980, "center", 0.12)


# ---------------- situação 3: pizza ----------------
def b_questao3(c, t, C, b):
    a12, b12, c12, d12 = (C[f"s12.{k}"] for k in "abcd")
    marca(c, t, a12, 3)
    pizzas(c, t, a12, tm=b12, tg=c12)
    E.saida(c, t, C["s13.a"] - 0.1, lambda: E.frase(c, t, entre(C, "s12.c", "s12.d", 0.7), ps("custa", "i", 62) + [("o dobro", "g", 70)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b12, ps("média:", "i", 58) + [("30 cm, R$ 40", "g", 62)]),
                    (c12, ps("grande:", "i", 58) + [("45 cm, R$ 80", "g", 62)]),
                    (d12, ps("mais ou menos que", "i", 58) + [("o dobro?", "g", 64, COR)])], C["s13.a"])


def b_resposta3(c, t, C, b):
    a14, b14, c14, d14, e14 = (C[f"s14.{k}"] for k in "abcde")
    a15, b15, c15, d15 = (C[f"s15.{k}"] for k in "abcd")
    X = 1500
    t0 = C["s14"] - 1.2
    pizzas(c, t, t0)
    E.foco(c, t, b14 + 0.5, 0.4, lambda f: E.pilula(c, "× 1,5", (PM[0] + PG[0]) / 2 + 30, 330, 52, "g", fundo=AMBAR, a=f * (1 - ep(t, a15, 0.3))))
    E.foco(c, t, a15, 0.4, lambda f: E.pilula(c, "área × 2,25", (PM[0] + PG[0]) / 2 + 30, 330, 52, "g", fundo=CERTO, a=f))

    def um():
        E.frase(c, t, a14, ps("círculos:", "i", 54) + [("sempre semelhantes", "g", 58, COR)], X, 220, "center", 0.12)
        fcen(c, t, b14, "k = 45 ÷ 30 = 1,5", X, 370, 76, AMBAR)
        fcen(c, t, c14, "área × 1,5^2", X, 520, 80)
        fcen(c, t, d14, "15 · 15 = 225", X, 670, 80)
        fcen(c, t, e14, "1,5^2 = 2,25", X, 820, 88, COR)
    E.saida(c, t, C["s15"] - 0.1, um)
    if t >= C["s15"] - 0.1:
        fcen(c, t, a15, "área: × 2,25", X, 240, 84, COR)
        E.frase(c, t, b15, [("2,25 > 2:", "g", 66)] + ps("mais que o dobro", "i", 60), X, 400, "center", 0.12)
        E.frase(c, t, b15 + 1.2, ps("pelo dobro do preço", "i", 58), X, 490, "center", 0.12)
        E.foco(c, t, c15, 0.5, lambda a: E.pilula(c, "a grande compensa", X, 660, 66, "g", fundo=CERTO, a=a))
        E.frase(c, t, d15, ps("sem calcular", "i", 58) + [("área nenhuma", "g", 62)], X, 840, "center", 0.12)


# ---------------- situação 4: razão das bases ----------------
def b_questao4(c, t, C, b):
    a16, b16, c16, d16 = (C[f"s16.{k}"] for k in "abcd")
    marca(c, t, a16, 4)
    tri4(c, t, a16 + 0.3, tl=b16, tareas=c16)
    E.foco(c, t, d16 + 0.3, 0.4, lambda f: (centro(c, "?", (TB[0] + TD[0]) / 2, TB[1] + 60, 60, "g", COR, f),
                                            centro(c, "?", (TD[0] + TC[0]) / 2, TB[1] + 60, 60, "g", AMBAR, f)))
    E.saida(c, t, C["s17.a"] - 0.1, lambda: E.frase(c, t, a16 + 0.5, ps("uma linha do", "i", 60) + [("vértice", "g", 66)], 1500, 380, "center", 0.12))
    pergunta(c, t, [(b16, ps("lado da frente:", "i", 58) + [("15 cm", "g", 64)]),
                    (c16, ps("pedaços de", "i", 58) + [("20 e 30 cm²", "g", 64)]),
                    (d16, ps("o lado fica", "i", 58) + [("? + ?", "g", 66, COR)])], C["s17.a"])


def b_resposta4(c, t, C, b):
    a18, b18, c18, d18 = (C[f"s18.{k}"] for k in "abcd")
    a19, b19, c19, d19, e19 = (C[f"s19.{k}"] for k in "abcde")
    X = 1500
    t0 = C["s18"] - 1.2
    tri4(c, t, t0, tl=t0, tareas=t0, altura=a18, tbases=c19)
    if t >= c19:
        k = ep(t, c19, 0.4)
        y = TB[1] + 50
        for (x0, x1, s, cor, ti) in ((TB[0], TD[0], "6 cm", COR, c19), (TD[0], TC[0], "9 cm", AMBAR, d19)):
            kk = ep(t, ti, 0.4)
            if kk > 0:
                M.line(c, x0 + 4, y, x1 - 4, y, cor, kk, 5)
                for x in (x0 + 4, x1 - 4):
                    M.line(c, x, y - 12, x, y + 12, cor, kk, 5)
                centro(c, s, (x0 + x1) / 2, y + 66, 56, "g", cor, kk)

    def um():
        E.frase(c, t, a18, ps("mesmo vértice:", "i", 60) + [("mesma altura", "g", 66, CERTO)], X, 230, "center", 0.12)
        E.frase(c, t, b18, ps("bases seguem as", "i", 60) + [("áreas", "g", 66)], X, 360, "center", 0.12)
        fcen(c, t, c18, "20 : 30 = 2 : 3", X, 510, 84, COR)
        E.foco(c, t, d18, 0.5, lambda a: E.pilula(c, "não são semelhantes", X, 680, 54, "g", fundo=TINTA, a=a))
        E.frase(c, t, d18 + 0.8, ps("nada vai", "i", 58) + [("ao quadrado", "g", 62)], X, 800, "center", 0.12)
    E.saida(c, t, C["s19"] - 0.1, um)
    if t >= C["s19"] - 0.1:
        fcen(c, t, a19, "2 + 3 = 5 partes", X, 220, 74)
        fcen(c, t, b19, "15 ÷ 5 = 3", X, 360, 80)
        fcen(c, t, c19, "2 · 3 = 6 cm", X, 500, 80, COR)
        fcen(c, t, d19, "3 · 3 = 9 cm", X, 640, 80, AMBAR)
        fcen(c, t, e19, "6 + 9 = 15", X - 40, 810, 80, CERTO)
        E.foco(c, t, e19 + 0.8, 0.4, lambda a: E.selo(c, X + 250, 785, 44 * ease_back(prog(t, e19 + 0.8, 0.4)), True, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", "junte os", "pedaços de círculo"), ("s20.b", "tire o que", "não faz parte"),
                 ("s20.c", "ampliação:", "área × k^2"), ("s20.d", "mesma altura:", "razão das bases"))
        for i, (k, it, g) in enumerate(itens):
            y = 380 + i * 165
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 28, 52, a=a), centro(c, str(i + 1), 300, y - 6, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, [(it, "i", 72)], 400, y)
            E.formula_em(c, t, C[k] + 0.4, g, 400 + E.larg(it, "i", 72) + 26, y, 70, "g", COR)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a21, b21, c21, d21, e21, f21 = (C[f"s21.{k}"] for k in "abcdef")
    E.foco(c, t, a21, 0.5, lambda a: E.pilula(c, "trilha concluída: áreas e perímetros", XE + 470, 180, 48, "g", fundo=CERTO, a=a))
    E.frase(c, t, b21 - 0.6, ps("próxima aula", "i", 76), XE, 330)
    E.frase(c, t, b21, [("função", "g", 96, COR), ("exponencial", "g", 96, COR)], XE, 460, passo=0.2)
    E.foco(c, t, c21, 0.5, lambda a: E.formula(c, "y = 2^x", XE, 620, 110, "g", TINTA, a))
    if t >= d21:
        P = E.plano(c, t, d21, 1100, 530, 600, 340, -3, 3, 0, 8, passo=1, marcas_x=[-2, 2], marcas_y=[4], grade=True)
        E.curva(c, t, d21 + 0.3, P, lambda x: 2 ** x, -3, 3, d=1.0)
        E.curva(c, t, d21 + 0.9, P, lambda x: 0.5 ** x, -3, 3, d=1.0, cor=AMBAR)
    E.foco(c, t, e21, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1460, 330, 72, estilo="g", a=a))
    p = ease_io(prog(t, e21 + 0.3, 0.8))
    E.cursor(c, lerp(1720, 1600, p), lerp(560, 355, p), ep(t, e21 + 0.2, 0.4))
    E.frase(c, t, f21, [("bons", "i", 120), ("estudos!", "i", 120, COR)], W / 2, 1020, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, atalho=b_atalho,
              questao2=b_questao2, resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3,
              questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
