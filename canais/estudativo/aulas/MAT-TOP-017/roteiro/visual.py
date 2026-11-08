"""Visual — Estudativo · MAT-TOP-017: homotetia, ampliar a partir de um centro.

Linguagem: o centro O é um ponto em tinta com um halo âmbar (a "lanterna"); os raios saem dele tracejados. A figura original
fica em tinta clara (contorno preto, preenchimento leve); a imagem, na cor da matéria. O caminho do centro até o ponto anda
como na MAT-POL-011: primeiro o corredor (petróleo, deitado), depois o elevador (âmbar, em pé). Áreas contadas em
quadradinhos. Erro em vermelho, certo em verde, atalho no palco escuro.
Peças locais: tri() (triângulo por três pontos, em pixels, que se desenha), raio(), centro_pt(), quadradinhos()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Tópicos Avançados")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TOP-017_homotetia.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("definicao", "plano", "centro", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
LUZ = "#D98A00"
DX, DY = "#0E9AA7", "#D98A00"
C_ESC = "#3CC7D3"
T1 = ((1, 1), (3, 1), (1, 2))
T1k = tuple((2 * x, 2 * y) for x, y in T1)
TQ = ((2, 1), (4, 1), (2, 3))
TQk = tuple((3 * x, 3 * y) for x, y in TQ)
assert T1k == ((2, 2), (6, 2), (2, 4)) and TQk == ((6, 3), (12, 3), (6, 9))
assert 2 * 1 / 2 == 1 and 4 * 2 / 2 == 4 and (1 + 2 * 2, 1 + 2 * 1) == (5, 3) and 2 * 2 / 2 == 2 and 2 * 9 == 18 == 6 * 6 / 2


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return w


def conta_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: conta(c, partes, x, y, size, a, align))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def plano(c, t, t0, P, mx=None, my=None, size=32, escuro=False):
    return E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, marcas_x=mx, marcas_y=my, size=size, escuro=escuro)


def tri(c, pts, p=1.0, cor=TINTA, fundo=None, largura=6, a=1.0):
    """triângulo que se desenha em volta (p de 0 a 1), com preenchimento leve"""
    if p <= 0 or a <= 0:
        return
    if fundo is not None:
        path = skia.Path(); path.addPoly(list(pts), True)
        c.drawPath(path, M.paint(fundo, 0.16 * a * min(1, p * 1.5)))
    seq = list(pts) + [pts[0]]
    tot = 3 * p
    for i in range(3):
        f = max(0.0, min(1.0, tot - i))
        if f > 0:
            M.line(c, *seq[i], *seq[i + 1], cor, a, largura, progress=f)


def tri_em(c, t, t0, pts, cor=TINTA, fundo=None, d=0.8, largura=6, a=1.0):
    tri(c, pts, ease_io(prog(t, t0, d)), cor, fundo, largura, a)


def raio(c, t, t0, O, Q, cor=LUZ, d=0.6, a=1.0, largura=4):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *O, *Q, cor, 0.85 * a, largura, dash=E.TRACO, progress=p)


def centro_pt(c, t, t0, X, nome="O", escuro=False, lado=(-1, 1)):
    k = ease_back(prog(t, t0, 0.45))
    if k > 0:
        c.drawCircle(*X, 34 * k, M.paint(LUZ, 0.25))
        c.drawCircle(*X, 14 * k, M.paint(BR if escuro else TINTA))
    if nome:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, nome, *X, lado[0], lado[1], 26, 46, "g", BR if escuro else TINTA, a))


def quadradinhos(c, x, y, l, n, cor, a=1.0, cheio=None):
    """quadrado de lado n·l dividido em n×n quadradinhos; cheio = quantos ficam pintados"""
    if a <= 0:
        return
    for i in range(n):
        for j in range(n):
            k = i * n + j
            if cheio is None or k < cheio:
                c.drawRect(skia.Rect.MakeXYWH(x + j * l + 4, y + i * l + 4, l - 8, l - 8), M.paint(cor, 0.3 * a))
    c.drawRect(skia.Rect.MakeXYWH(x, y, n * l, n * l), M.paint(TINTA, a, stroke=6))
    for i in range(1, n):
        M.line(c, x + i * l, y, x + i * l, y + n * l, TINTA, a, 3)
        M.line(c, x, y + i * l, x + n * l, y + i * l, TINTA, a, 3)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    O = (300, 560)
    obj = ((800, 470), (800, 650), (920, 560))
    img = tuple((O[0] + 2 * (x - O[0]), O[1] + 2 * (y - O[1])) for x, y in obj)

    def cena():
        # a lanterna
        a = ep(t, C["s01.a"], 0.5)
        if a > 0:
            M.rrect(c, O[0] - 150, O[1] - 40, 150, 80, 18, TINTA, a)
            c.drawCircle(*O, 46, M.paint(LUZ, 0.9 * a))
        tri_em(c, t, C["s01.a"] + 0.4, obj, TINTA, TINTA)
        for i, Q in enumerate(img):
            raio(c, t, C["s01.b"] + 0.1 * i, O, Q)
        tri_em(c, t, C["s01.b"] + 0.5, img, COR, COR, 0.6, 8)
        E.foco(c, t, C["s01.b"] + 1.2, 0.4, lambda a: E.pilula(c, "sombra: lados × 2", 1380, 300, 48, "g", a=a))
        E.frase(c, t, C["s01.b"] + 2.6, [("área", "i", 74), ("×", "g", 70), ("2?", "g", 74, ERRADO)], 560, 900)
        if t >= C["s01.c"]:
            E.risco(c, 550, 920, 880, 840, t, C["s01.c"], largura=10)
        E.foco(c, t, C["s01.c"] + 0.3, 0.4, lambda a: E.pilula(c, "área × 4", 1150, 878, 64, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s01.a"], [("a", "i", 64), ("lanterna", "i", 64), ("e", "i", 64), ("a", "i", 64), ("sombra", "i", 64)], XE, 190)
    E.saida(c, t, C["s02"] - 0.1, cena)
    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("ampliar", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.4, [("de", "i", 100), ("um", "i", 100), ("ponto", "g", 120, COR)], XE, 590)
        E.frase(c, t, C["s02.a"] + 3.0, ps("comprimentos e área", "i", 70, TINTA2), XE, 710, passo=0.1)
        E.foco(c, t, C["s02.b"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 190, "center")
    x, w = 200, 1520
    for k, y in (("s03.b", 280), ("s03.c", 610)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 290, p, prog_=p)
    k = C["s03.b"]
    E.frase(c, t, k, [("refletir,", "g", 60), ("girar,", "g", 60), ("deslizar", "g", 60)], 260, 380)
    E.frase(c, t, k + 1.6, [("mudam", "i", 60), ("o", "i", 60), ("lugar,", "g", 58, COR), ("não", "i", 60), ("o", "i", 60), ("tamanho", "g", 58, ERRADO)], 260, 480)
    a = ep(t, k + 0.6, 0.5)
    tri(c, ((1250, 500), (1400, 500), (1250, 400)), a, TINTA, TINTA)
    s = ease_io(prog(t, k + 1.4, 1.0))
    tri(c, ((1250 + 260 * s, 500), (1400 + 260 * s, 500), (1250 + 260 * s, 400)), a, COR, COR)
    k = C["s03.c"]
    E.frase(c, t, k, [("semelhantes:", "g", 60, COR)], 260, 710)
    conta_em(c, t, k + 1.0, [("lados × k  →  área × k^2", TINTA)], 260, 820, 68)
    E.frase(c, t, C["s04"] - 2.4, ps("faltou alguma? procure no canal", "i", 50, TINTA2), W / 2, 980, "center", passo=0.1)


# ---------------- definição ----------------
def b_definicao(c, t, C, b):
    O, P_ = (1000, 760), (1300, 560)
    P2 = (O[0] + 2 * (P_[0] - O[0]), O[1] + 2 * (P_[1] - O[1]))
    E.frase(c, t, C["s04.a"], [("homotetia", "g", 90, COR)], XE, 260)
    E.frase(c, t, C["s04.a"] + 0.8, ps("muda o tamanho", "i", 66), XE, 360)
    E.frase(c, t, C["s04.b"], [("centro", "g", 64, LUZ), ("=", "i", 66), ("a", "i", 66), ("lanterna", "i", 66)], XE, 520)
    E.frase(c, t, C["s04.c"], [("razão", "g", 64, COR), ("k", "g", 64, COR), ("=", "i", 66), ("quantas", "i", 66), ("vezes", "i", 66)], XE, 620)
    centro_pt(c, t, C["s04.b"], O)
    k_ = ease_back(prog(t, C["s05.a"] - 0.3, 0.45))
    if k_ > 0:
        c.drawCircle(*P_, 14 * k_, M.paint(TINTA))
        E.foco(c, t, C["s05.a"] - 0.1, 0.4, lambda a: E._cola(c, "P", *P_, -1, -1, 24, 46, "g", TINTA, a))
    seg_a = ease_io(prog(t, C["s05.a"], 0.6))
    if seg_a > 0:
        M.line(c, *O, *P_, TINTA, 1, 7, progress=seg_a)
    if t >= C["s05.b"]:
        p = ease_io(prog(t, C["s05.b"], 0.8))
        M.line(c, *P_, lerp(P_[0], P2[0], p), lerp(P_[1], P2[1], p), COR, 1, 7, dash=E.TRACO)
    k2 = ease_back(prog(t, C["s05.c"], 0.45))
    if k2 > 0:
        c.drawCircle(*P2, 16 * k2, M.paint(COR))
        E.foco(c, t, C["s05.c"] + 0.2, 0.4, lambda a: E._cola(c, "P'", *P2, 1, 0, 24, 48, "g", COR, a))
    if t >= C["s05.d"]:
        q = ep(t, C["s05.d"], 0.4)
        nx, ny = 0.55, 0.83
        for (A_, B_, s, cor) in ((O, P_, "d", TINTA), (O, P2, "2d", COR)):
            off = 40 if s == "d" else 100
            a0 = (A_[0] + nx * off, A_[1] + ny * off)
            b0 = (B_[0] + nx * off, B_[1] + ny * off)
            M.line(c, *a0, *b0, cor, q, 4)
            E.foco(c, t, C["s05.d"], 0.4, lambda a, a0=a0, b0=b0, s=s, cor=cor: E._meio(c, s, (a0[0] + b0[0]) / 2 + nx * 34, (a0[1] + b0[1]) / 2 + ny * 34, 46, "g", cor, a))
    conta_em(c, t, C["s05.d"] + 0.4, [("k = 2:  OP' = 2 · OP", COR)], XE, 820, 66)


# ---------------- no plano ----------------
PP = E.Plano(1060, 170, 760, 660, -0.5, 7.5, -0.5, 6.45)   # 95 px por unidade


def b_plano(c, t, C, b):
    plano(c, t, C["s06"], PP, [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6])
    O = PP(0, 0)
    centro_pt(c, t, C["s06.a"], O, "O", lado=(-1, 1))
    tri_em(c, t, C["s06.b"], [PP(*p) for p in T1], TINTA, TINTA)
    for i, Q in enumerate(T1k):
        raio(c, t, C["s07.a"] + 1.4 * i - 0.2, O, PP(*Q), LUZ, 0.5)
        k_ = ease_back(prog(t, C["s07.a"] + 1.4 * i + 0.2, 0.4))
        if k_ > 0:
            c.drawCircle(*PP(*Q), 13 * k_, M.paint(COR))
    tri_em(c, t, C["s07.c"] + 0.8, [PP(*p) for p in T1k], COR, COR, 0.8, 7)
    # medidas (s08)
    if t >= C["s08.a"]:
        q = ep(t, C["s08.a"], 0.4)
        E._meio(c, "2", *PP(2, 0.7), 40, "g", TINTA, q)
        E._meio(c, "4", *PP(4, 1.55), 44, "g", COR, q)
    if t >= C["s08.b"]:
        q = ep(t, C["s08.b"], 0.4)
        E._meio(c, "1", *PP(0.65, 1.5), 40, "g", TINTA, q)
        E._meio(c, "2", *PP(1.6, 3), 44, "g", COR, q)
    if t >= C["s08.e"]:
        q = ep(t, C["s08.e"], 0.4) * (1 - ep(t, C["s09"], 0.4))
        for (A_, B_) in ((T1[1], T1[2]), (T1k[1], T1k[2])):
            M.line(c, *PP(*A_), *PP(*B_), CERTO, q, 10)

    def s06_07():
        E.frase(c, t, C["s06.a"], ps("centro na origem", "i", 62), XE, 250)
        conta_em(c, t, C["s06.c"], [("k = 2: cada coordenada × 2", COR)], XE, 360, 54)
        for i, (k, A_, B_) in enumerate(zip(("s07.a", "s07.b", "s07.c"), T1, T1k)):
            conta_em(c, t, C[k], [(f"({A_[0]}, {A_[1]})  →  ", TINTA), (f"({B_[0]}, {B_[1]})", COR)], XE, 520 + i * 130, 70)
    E.saida(c, t, C["s08"] - 0.1, s06_07)
    if t < C["s08"]:
        return

    def s08():
        conta_em(c, t, C["s08.a"], [("base: 2 → ", TINTA), ("4", COR)], XE, 300, 66)
        conta_em(c, t, C["s08.b"], [("altura: 1 → ", TINTA), ("2", COR)], XE, 410, 66)
        E.frase(c, t, C["s08.c"], [("comprimentos", "i", 66), ("×", "g", 66, COR), ("2", "g", 66, COR)], XE, 540)
        E.frase(c, t, C["s08.d"], [("ângulos:", "i", 62), ("iguais", "g", 60)], XE, 680)
        E.frase(c, t, C["s08.e"], [("lados:", "i", 62), ("paralelos", "g", 60, CERTO)], XE, 790)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    E.frase(c, t, C["s09"], [("e", "i", 80), ("a", "i", 80), ("área?", "g", 80, COR)], XE, 270)
    conta_em(c, t, C["s09.a"], [("antes: f{2 · 1}{2} = 1", TINTA)], XE, 430, 64)
    conta_em(c, t, C["s09.b"], [("depois: f{4 · 2}{2} = ", TINTA), ("4", COR)], XE, 600, 64)
    conta_em(c, t, C["s09.c"], [("k^2 = 2^2 = 4", COR)], XE, 780, 76)


# ---------------- centro fora da origem ----------------
PCc = E.Plano(1060, 170, 760, 660, -0.5, 7.5, -0.5, 6.45)


def b_centro(c, t, C, b):
    def s10_11():
        plano(c, t, C["s10"], PCc, [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6])
        O, Pt, R = (1, 1), (3, 2), (5, 3)
        centro_pt(c, t, C["s11.a"], PCc(*O), "O", lado=(-1, 1))
        k_ = ease_back(prog(t, C["s11.b"], 0.4))
        if k_ > 0:
            c.drawCircle(*PCc(*Pt), 13 * k_, M.paint(TINTA))
            E.foco(c, t, C["s11.b"] + 0.2, 0.4, lambda a: E._cola(c, "P", *PCc(*Pt), -0.4, -1, 18, 44, "g", TINTA, a))
        # caminho do centro até P: corredor e elevador
        for t0, A_, B_, cor in ((C["s11.c"], O, (3, 1), DX), (C["s11.c"] + 0.7, (3, 1), Pt, DY)):
            p = ease_io(prog(t, t0, 0.6))
            if p > 0:
                M.arrow(c, *PCc(*A_), *PCc(*B_), cor, 1, 7, 22, p)
        for t0, A_, B_, cor in ((C["s11.d"], O, (5, 1), DX), (C["s11.d"] + 0.8, (5, 1), R, DY)):
            p = ease_io(prog(t, t0, 0.7))
            if p > 0:
                M.arrow(c, *PCc(*A_), *PCc(*B_), cor, 0.55, 5, 20, p)
        raio(c, t, C["s11.e"] - 0.4, PCc(*O), PCc(*R), LUZ, 0.6)
        k2 = ease_back(prog(t, C["s11.e"], 0.4))
        if k2 > 0:
            c.drawCircle(*PCc(*R), 15 * k2, M.paint(COR))
            E.foco(c, t, C["s11.e"] + 0.2, 0.4, lambda a: E._cola(c, "P' (5, 3)", *PCc(*R), 1, -1, 18, 44, "g", COR, a))
        E.frase(c, t, C["s10"], ps("centro fora da origem?", "i", 62), XE, 230, passo=0.1)
        E.frase(c, t, C["s10.a"], [("1", "g", 56, COR), ("caminho", "i", 60), ("do", "i", 60), ("centro", "i", 60), ("ao", "i", 60), ("ponto", "i", 60)], XE, 340)
        E.frase(c, t, C["s10.b"], [("2", "g", 56, COR), ("caminho", "i", 60), ("×", "g", 58, COR), ("k", "g", 58, COR)], XE, 430)
        E.frase(c, t, C["s10.c"], [("3", "g", 56, COR), ("ande", "i", 60), ("a", "i", 60), ("partir", "i", 60), ("do", "i", 60), ("centro", "i", 60)], XE, 520)
        conta_em(c, t, C["s11.c"], [("→ 2", DX), ("  ↑ 1", DY)], XE, 680, 70)
        conta_em(c, t, C["s11.d"], [("× 2:  ", TINTA), ("→ 4", DX), ("  ↑ 2", DY)], XE, 790, 70)
        conta_em(c, t, C["s11.e"], [("(1 + 4, 1 + 2) = ", TINTA), ("(5, 3)", COR)], XE, 920, 66)
    E.saida(c, t, C["s12"] - 0.1, s10_11)
    if t < C["s12"]:
        return
    E.frase(c, t, C["s12.a"], [("k", "g", 76, COR), ("entre", "i", 76), ("0", "g", 76), ("e", "i", 76), ("1:", "g", 76), ("encolhe", "g", 76, COR)], XE, 280)
    O = (1150, 820)
    big = ((1250, 820), (1650, 820), (1250, 520))
    small = tuple((O[0] + (x - O[0]) / 2, O[1] + (y - O[1]) / 2) for x, y in big)
    centro_pt(c, t, C["s12.a"], O, "O", lado=(-1, 1))
    tri_em(c, t, C["s12.a"] + 0.3, big, TINTA, TINTA)
    for i, Q in enumerate(big):
        raio(c, t, C["s12.b"] + 0.1 * i, O, Q)
    tri_em(c, t, C["s12.b"] + 0.5, small, COR, COR, 0.6, 7)
    conta_em(c, t, C["s12.b"], [("k = f{1}{2}", COR)], XE, 470, 80)
    conta_em(c, t, C["s12.b"] + 1.2, [("lados: metade", TINTA)], XE, 620, 64)
    conta_em(c, t, C["s12.c"], [("área: ", TINTA), ("(f{1}{2})^2 = f{1}{4}", COR)], XE, 790, 68)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 230)
    E.frase(c, t, C["s13.a"], [("área", "i", 70), ("×", "g", 66), ("2?", "g", 70, ERRADO)], XE, 380)
    if t >= C["s13.c"]:
        E.risco(c, XE + 120, 400, XE + 300, 320, t, C["s13.c"], largura=10)
    l = 150
    E.foco(c, t, C["s13.b"] - 0.6, 0.5, lambda a: quadradinhos(c, 760, 560, l, 1, TINTA, a))
    E.foco(c, t, C["s13.b"] - 0.4, 0.4, lambda a: E.centro(c, "lado 1", 760 + l / 2, 780, 44, "b", TINTA, a))
    E.foco(c, t, C["s13.b"] + 0.4, 0.5, lambda a: E.escreve(c, "→", 960, 660, 90, "g", COR, a))
    nq = int(min(4, max(0, (t - C["s13.c"]) / 0.35 + 1))) if t >= C["s13.c"] else 0
    E.foco(c, t, C["s13.b"] + 0.6, 0.5, lambda a: quadradinhos(c, 1100, 410, l, 2, COR, a, nq))
    E.foco(c, t, C["s13.b"] + 0.8, 0.4, lambda a: E.centro(c, "lado 2", 1100 + l, 780, 44, "b", COR, a))
    E.foco(c, t, C["s13.c"] + 1.4, 0.4, lambda a: E.pilula(c, "4 quadradinhos", 1250, 880, 56, "g", fundo=CERTO, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    O = (1240, 720)
    obj = ((1380, 660), (1520, 660), (1380, 550))
    img = tuple((O[0] + 2.1 * (x - O[0]), O[1] + 2.1 * (y - O[1])) for x, y in obj)
    tri_em(c, t, C["s14"], obj, CLARO, CLARO)
    tri_em(c, t, C["s14"] + 0.3, img, BR, BR)
    for i, (A_, B_) in enumerate(zip(obj, img)):
        p = ease_io(prog(t, C["s14.b"] + 0.3 * i, 0.7))
        if p > 0:
            ext = (B_[0] + (O[0] - B_[0]) * 1.12, B_[1] + (O[1] - B_[1]) * 1.12)
            M.line(c, *B_, lerp(B_[0], ext[0], p), lerp(B_[1], ext[1], p), C_ESC, 0.9, 4, dash=E.TRACO)
    if t >= C["s14.c"]:
        centro_pt(c, t, C["s14.c"], O, "centro", escuro=True, lado=(-1, 0.4))
    E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 70, CLARO), XE, 200)
    E.frase(c, t, C["s14.a"], [("onde", "i", 70, CLARO), ("está", "i", 70, CLARO), ("o", "i", 70, CLARO), ("centro?", "g", 70, BR)], XE, 310)
    E.frase(c, t, C["s14.b"], ps("ligue cada ponto à imagem", "i", 58, CLARO), XE, 450, passo=0.1)
    E.frase(c, t, C["s14.c"], [("as", "i", 58, CLARO), ("retas", "i", 58, CLARO), ("se", "i", 58, CLARO), ("cruzam", "g", 58, C_ESC)], XE, 540)
    conta_em(c, t, C["s14.d"], [("k = f{lado novo}{lado antigo}", BR)], XE, 700, 64)
    E.frase(c, t, C["s15.a"], ps("ponto e imagem: mesma reta pelo centro", "i", 50, CLARO), XE, 860, passo=0.08)
    E.frase(c, t, C["s15.b"], [("não", "g", 52, ERRADO), ("compensa:", "i", 54, CLARO), ("centro", "i", 54, CLARO), ("na", "i", 54, CLARO), ("origem", "g", 52, BR)],
            XE, 960)


# ---------------- questão ----------------
PQ = E.Plano(1000, 150, 820, 750, -0.6, 12.9, -0.6, 11.75)  # 60,7 px por unidade


def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 200)
    for i, p in enumerate(TQ):
        conta_em(c, t, C["s16.a"] + 0.9 * i, [(f"({p[0]}, {p[1]})", TINTA)], XE + i * 230, 330, 60)
    E.frase(c, t, C["s16.b"], [("centro:", "i", 62), ("origem", "g", 60, LUZ)], XE, 480)
    E.frase(c, t, C["s16.b"] + 1.0, [("razão:", "i", 62), ("k = 3", "g", 60, COR)], XE, 570)
    E.frase(c, t, C["s16.c"], [("novos", "i", 66), ("vértices?", "g", 66, COR)], XE, 720)
    E.frase(c, t, C["s16.d"], [("nova", "i", 66), ("área?", "g", 66, COR)], XE, 820)
    plano(c, t, C["s16.a"], PQ, [2, 4, 6, 8, 10, 12], [2, 4, 6, 8, 10])
    tri_em(c, t, C["s16.a"] + 2.6, [PQ(*p) for p in TQ], TINTA, TINTA)
    centro_pt(c, t, C["s16.b"], PQ(0, 0), "O", lado=(-1, 1))
    if t >= C["s17"]:
        E.relogio(c, t, C["s17.a"], cx=1640, cy=330, r=110)


def b_resposta(c, t, C, b):
    plano(c, t, C["s18"] - 3, PQ, [2, 4, 6, 8, 10, 12], [2, 4, 6, 8, 10])
    centro_pt(c, t, C["s18"] - 3, PQ(0, 0), "O", lado=(-1, 1))
    tri_em(c, t, C["s18"] - 3, [PQ(*p) for p in TQ], TINTA, TINTA)
    for i, (k, Q) in enumerate(zip(("s18.b", "s18.c", "s18.d"), TQk)):
        raio(c, t, C[k] - 0.3, PQ(0, 0), PQ(*Q), LUZ, 0.5)
        kk = ease_back(prog(t, C[k], 0.4))
        if kk > 0:
            c.drawCircle(*PQ(*Q), 13 * kk, M.paint(COR))
    tri_em(c, t, C["s18.d"] + 0.6, [PQ(*p) for p in TQk], COR, COR, 0.8, 7)
    conta_em(c, t, C["s18.a"], [("cada coordenada × 3", COR)], XE, 230, 56)
    for i, (k, A_, B_) in enumerate(zip(("s18.b", "s18.c", "s18.d"), TQ, TQk)):
        conta_em(c, t, C[k], [(f"({A_[0]}, {A_[1]})  →  ", TINTA), (f"({B_[0]}, {B_[1]})", COR)], XE, 340 + i * 100, 58)
    conta_em(c, t, C["s19.a"], [("antes: f{2 · 2}{2} = 2", TINTA)], XE, 690, 56)
    conta_em(c, t, C["s19.b"], [("k^2 = 9", COR)], XE + 530, 690, 56)
    conta_em(c, t, C["s19.c"], [("2 · 9 = ", TINTA)], XE, 850, 70)
    bola_txt(c, t, C["s19.c"] + 0.3, "18", XE + 320, 828, 70, 70, CERTO)
    conta_em(c, t, C["s19.d"], [("confira: f{6 · 6}{2} = 18", TINTA2)], XE, 990, 52)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s20.a", [("homotetia:", "g", 70, COR), ("amplia", "i", 72), ("de", "i", 72), ("um", "i", 72), ("centro", "g", 70, LUZ)]),
                 ("s20.b", [("comprimentos", "i", 72), ("×", "g", 70), ("k", "g", 70, COR)]),
                 ("s20.c", [("área", "i", 72), ("×", "g", 70), ("k²", "g", 70, COR)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 240, y - 26, 56, a=a),
                                                         E.escreve(c, str(i + 1), 240 - E.larg(str(i + 1), "g", 64) / 2, y - 3, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 340, y, passo=0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s21"] + 0.8, [("Praticando", "g", 150, COR)], XE, 460)
    E.frase(c, t, C["s21.a"], ps("bases e algarismos significativos", "i", 58, TINTA2), XE, 580, passo=0.08)
    E.frase(c, t, C["s21.b"], ps("troncos e homotetia", "i", 58, TINTA2), XE, 670, passo=0.08)
    E.foco(c, t, C["s21.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(620, 325, p), ep(t, C["s21.c"] + 0.2, 0.4))
    E.frase(c, t, C["s21.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, definicao=b_definicao, plano=b_plano, centro=b_centro, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
