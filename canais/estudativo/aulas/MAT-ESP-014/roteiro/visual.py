"""Visual — Estudativo · MAT-ESP-014: esfera, área e volume.
Mesma linguagem da trilha (MAT-ESP-001 a 013): sólidos do kit (E.esfera, E.cilindro) com a metade de trás do equador tracejada,
o elemento da vez na cor da matéria, a 2ª família em cinza, resposta na esfera.
- A CASCA DE LARANJA (gancho e área): quatro círculos iguais ao do corte, desenhados em fila, que a casca vai cobrindo
  (casca(): o círculo se pinta girando, como um setor que cresce).
- O CÍRCULO DO MEIO: a elipse do equador pintada na cor da matéria (equador()), com o raio da esfera.
- A LATA DE ARQUIMEDES (volume): E.esfera dentro de um E.cilindro de mesmo raio e altura 2r, na mesma inclinação (22°);
  os dois terços aparecem numa barra de 3 partes (E.barra_fatias). A lateral da lata aberta é o retângulo 2πr × 2r.
- ERRO: a esfera do diâmetro usado como raio aparece em vermelho tracejado, com o dobro do raio, por fora da certa.
- π fica escrito (100π, 36π) até o atalho; no atalho e na questão, π = 3.
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-014_esfera_area_e_volume.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("esfera", "area", "volume", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)  # a 2ª família pintada numa face de papel
IN = 22                                  # inclinação da esfera e da lata (a mesma de E.cilindro)
SEN, COS = math.sin(math.radians(IN)), math.cos(math.radians(IN))
assert 5 ** 2 == 25 and 4 * 25 == 100 and 3 ** 3 == 27 and 27 // 3 == 9 and 9 * 4 == 36 and 4 * 27 == 108
assert 6 ** 3 == 216 and 4 * 216 // 3 == 288 and 288 == 8 * 36 and 6 // 2 == 3 and 108 * 1000 == 108000 and 108 == 36 * 3
assert 4 * 3 == 12 and 10 ** 2 == 100 and 12 * 100 == 1200 and 10 ** 3 == 1000 and 4 * 1000 == 4000 and 4 * 3 * 1000 == 12000
assert 12000 // 3 == 4000


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ², ³, √ ou π vai na grotesca: a serifada não tem esses sinais)"""
    out = []
    for w in txt.split():
        g = any(ch in w for ch in "²³√π")
        out.append((w, "g" if g else est, size * (0.92 if g and est != "g" else 1), cor))
    return out


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.5, tracejada=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def alfa(c, a, fn):
    if a <= 0:
        return
    if a >= 0.999:
        fn()
        return
    p = skia.Paint(); p.setAlphaf(a)
    c.saveLayer(None, p); fn(); c.restore()


def vertice(c, t, t0, P, r=15, cor=None, a=1.0):
    """o ponto da vez: bolinha que salta (de MAT-ESP-001)"""
    k = ease_back(prog(t, t0, 0.35))
    if k > 0 and a > 0:
        c.drawCircle(P[0], P[1], r * k, M.paint(cor or E.COR, a))


# ================= peças desta aula =================
def esfera(c, t, t0, cx, cy, r, raio=None, **kw):
    return E.esfera(c, t, t0, cx, cy, r, raio, inclina=IN, **kw)


def equador(c, cx, cy, r, a=1.0, cor=None, alfa_=0.45):
    """o círculo do meio pintado: a elipse do equador"""
    if a <= 0:
        return
    ry = r * SEN
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, alfa_ * a))
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, a, stroke=4))


def raio_esf(c, t, t0, cx, cy, r, ang, rot=None, cor=None, size=58, largura=8, tracejado=False, a=1.0):
    """um raio do centro até a superfície, no ângulo ang (graus da tela, horário a partir da direita)"""
    P = (cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang)))
    aresta(c, t, t0, (cx, cy), P, cor or E.COR, largura, 0.4, tracejado, a)
    if rot:
        n = (-math.sin(math.radians(ang)), math.cos(math.radians(ang)))
        E.foco(c, t, t0 + 0.3, 0.4, lambda q: E._cola(c, rot, (cx + P[0]) / 2, (cy + P[1]) / 2, -n[0], -n[1], 12, size, "g", cor or COR, q * a))
    return P


def casca(c, cx, cy, r, borda=1.0, cobre=0.0, a=1.0):
    """um círculo riscado no papel (borda = 0..1 desenha o contorno) que a casca cobre (cobre = 0..1, girando)"""
    if a <= 0:
        return
    rc = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    if cobre >= 0.999:
        c.drawCircle(cx, cy, r, M.paint(E.COR, 0.55 * a))
    elif cobre > 0:
        p = skia.Path()
        p.moveTo(cx, cy); p.arcTo(rc, -90, 360 * ease_io(cobre), False); p.close()
        c.drawPath(p, M.paint(E.COR, 0.55 * a))
    if borda > 0:
        c.drawArc(rc, -90, 360 * ease_io(borda), False, M.paint(TINTA, a, stroke=5, cap_round=True))


def quatro(c, t, tb, t_cobre, t_fim, x0, y, r, gap, a=1.0, rotulos=False):
    """os 4 círculos: contornos a partir de tb; a casca cobre um por vez de t_cobre até t_fim"""
    T = max(0.6, (t_fim - t_cobre) / 4)
    for k in range(4):
        cx = x0 + k * (2 * r + gap)
        casca(c, cx, y, r, prog(t, tb + 0.3 * k, 0.5), prog(t, t_cobre + k * T, T * 0.9), a)
        if rotulos:
            E.foco(c, t, t_cobre + (k + 0.6) * T, 0.3, lambda q, cx=cx, k=k: centro(c, str(k + 1), cx, y + 22, 60, "g", BR, q * a))


def lata(c, t, t0, cx, cy, r, **kw):
    """a lata em volta da esfera: (cx, cy) = centro da esfera; raio r e altura 2r"""
    return E.cilindro(c, t, t0, cx, cy + r * COS, r, 2 * r, inclina=IN, preenche=0.18, **kw)


def lateral_lata(c, cx, cy, r, a=1.0, cor=None, alfa_=0.45):
    """a lateral da lata pintada (cx, cy = centro da esfera)"""
    if a <= 0:
        return
    ry, yb, yt = r * SEN, cy + r * COS, cy - r * COS
    p = skia.Path()
    p.moveTo(cx - r, yt); p.lineTo(cx - r, yb)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, yb - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, yt)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, yt - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


def fuso(c, cx, cy, r, a=1.0, cor=None):
    """o gomo (fuso) na frente da esfera: entre dois meridianos"""
    if a <= 0:
        return
    r1, r2 = r * 0.12, r * 0.62
    p = skia.Path()
    p.moveTo(cx, cy - r)
    p.arcTo(skia.Rect.MakeXYWH(cx - r2, cy - r, 2 * r2, 2 * r), -90, 180, False)
    p.arcTo(skia.Rect.MakeXYWH(cx - r1, cy - r, 2 * r1, 2 * r), 90, -180, False)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, 0.5 * a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))


def hemisferio(c, cx, cy, r, a=1.0, cor=None):
    """a metade de baixo pintada"""
    if a <= 0:
        return
    ry = r * SEN
    p = skia.Path()
    p.moveTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 180, -180, False)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 0, -180, False)
    p.close()
    c.drawPath(p, M.paint(cor or TINTA2, 0.35 * a))


def secao(c, cx, cy, r, k=0.55, a=1.0):
    """o círculo de um corte fora do centro, à altura k·r acima do centro"""
    if a <= 0:
        return
    rr = r * math.sqrt(1 - k * k)
    ry, y = rr * SEN, cy - k * r * COS
    c.drawOval(skia.Rect.MakeXYWH(cx - rr, y - ry, 2 * rr, 2 * ry), M.paint(E.COR, 0.5 * a))
    c.drawOval(skia.Rect.MakeXYWH(cx - rr, y - ry, 2 * rr, 2 * ry), M.paint(E.COR, a, stroke=4))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        ox, oy, orr = 330, 560, 190
        esfera(c, t, a1, ox, oy, orr)
        equador(c, ox, oy, orr, ep(t, a1 + 0.8, 0.5))
        E.frase(c, t, a1 + 0.2, ps("uma", "i", 64) + [("laranja", "g", 68, COR)] + ps("cortada ao meio", "i", 64), 120, 200, "left", 0.1)
        E.foco(c, t, a1 + 1.2, 0.4, lambda q: centro(c, "o corte: um círculo", ox, oy + orr + 90, 48, "i", TINTA2, q))
        quatro(c, t, b1, lerp(b1, c1, 0.45), c1 + 0.2, 760, 560, 130, 40, rotulos=True)
        E.frase(c, t, b1 + 0.3, ps("o contorno do corte,", "i", 58) + [("4 vezes", "g", 62, COR)], 1290, 330, "center", 0.1)
        E.frase(c, t, lerp(b1, c1, 0.45), ps("a casca", "i", 58) + [("cobre", "g", 62, COR)], 1290, 820, "center", 0.1)
        E.frase(c, t, c1, [("os 4, certinho", "g", 72, COR)], 1290, 950, "center", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.3), ps("a", "i", 90) + [("área", "g", 104, COR)] + ps("e o", "i", 90) + [("volume", "g", 104, COR)], XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.6), ps("de qualquer", "i", 90) + [("esfera", "g", 104, COR)], XE, 610, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "área do círculo:", "A = πr^2"), ("s03.c", "volume do cilindro:", "V = πr² · h"),
             ("s03.d", "érre ao cubo:", "r³ = r · r · r"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 190 + i * 240
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 58), x + 44, y + 80, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 166, 60, "g", COR)
    alvo = [190 + i * 240 + 170 for i in range(3)]
    q1, q2 = ease_io(prog(t, C["s03.c"] - 0.35, 0.5)), ease_io(prog(t, C["s03.d"] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, C["s03.b"], 0.4))
    E.frase(c, t, lerp(C["s03.d"], C["s03.end"], 0.72), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 1000, "left", 0.12)


# ---------------- o que é esfera ----------------
SX, SY, SR = 520, 580, 300


def b_esfera(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    esfera(c, t, a4, SX, SY, SR)
    equador(c, SX, SY, SR, ep(t, d4, 0.5))
    if t >= b4:
        vertice(c, t, b4, (SX, SY), 12, TINTA)
        for k, ang in enumerate((-150, -100, -40, 20, 150)):
            raio_esf(c, t, b4 + 0.3 + 0.2 * k, SX, SY, SR, ang, None, TINTA2, largura=5, tracejado=True, a=1 - 0.6 * ep(t, c4, 0.4))
    if t >= c4:
        raio_esf(c, t, c4, SX, SY, SR, -40, "r", largura=9)
    if t >= d4:
        aresta(c, t, d4 + 0.4, (SX, SY), (SX - SR, SY), TINTA, 6)
        E.foco(c, t, d4 + 0.7, 0.4, lambda q: E._cola(c, "r", SX - SR / 2, SY, 0, 1, 8, 54, "g", TINTA, q))
    X = 1080
    E.frase(c, t, a4, [("esfera", "g", 96, COR)] + ps("= a bola", "i", 80), X, 240, "left", 0.1)
    E.frase(c, t, b4, ps("cada ponto da superfície", "i", 56), X, 390, "left", 0.1)
    E.frase(c, t, b4 + 0.8, ps("à", "i", 54) + [("mesma distância", "g", 58, COR)] + ps("do centro", "i", 54), X, 470, "left", 0.1)
    E.frase(c, t, c4, ps("essa distância é o", "i", 56) + [("raio r", "g", 62, COR)], X, 590, "left", 0.1)
    E.frase(c, t, d4, ps("corte no meio:", "i", 56), X, 740, "left", 0.1)
    E.frase(c, t, d4 + 0.6, ps("o", "i", 60) + [("maior círculo", "g", 64, COR)], X, 830, "left", 0.1)
    E.frase(c, t, d4 + 1.2, ps("com o mesmo raio", "i", 52, TINTA2), X, 910, "left", 0.1)


# ---------------- área ----------------
def b_area(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    ox, oy, orr = 330, 560, 210
    esfera(c, t, C["s05"] - 0.6, ox, oy, orr)
    equador(c, ox, oy, orr, 1.0 if t < C["s06"] else 1 - ep(t, C["s06"], 0.4))

    def quatro_circ():
        E.frase(c, t, C["s05"] + 0.2, ps("o círculo que você riscou", "i", 56, TINTA2), 1200, 200, "center", 0.1)
        quatro(c, t, C["s05"] + 0.2, a5, a5 + 1.6, 790, 400, 100, 40, rotulos=True)
        E.frase(c, t, a5, ps("a casca vale", "i", 60) + [("4 círculos", "g", 64, COR)], 1200, 600, "center", 0.1)
        fcen(c, t, b5, "A = 4πr^2", 1200, 800, 140, COR)
        if t >= c5:
            wa = E.formula(None, "A = 4", 0, 0, 140, "g", a=0)
            wt = E.formula(None, "A = 4πr^2", 0, 0, 140, "g", a=0)
            x0 = 1200 - wt / 2 + wa
            p = ep(t, c5, 0.5)
            E.caixa_pontilhada(c, x0 - 12, 680, wt - wa + 24, 150, p, prog_=p)
        E.frase(c, t, c5 + 0.3, [("πr²", "g", 56, COR)] + ps("= área do círculo", "i", 54), 1200, 950, "center", 0.1)
    fase(c, t, C["s05"], C["s06"] - 0.1, quatro_circ)
    if t < C["s06"] - 0.1:
        return
    if t >= a6:
        raio_esf(c, t, a6, ox, oy, orr, -35, "5 cm", size=52)
    X = 1260
    E.frase(c, t, C["s06"] + 0.1, ps("uma bola de", "i", 60) + [("raio 5 cm", "g", 64, COR)], X, 220, "center", 0.1)
    fcen(c, t, b6, "5² = 25", X, 400, 84)
    fcen(c, t, c6, "4 × 25 = 100", X, 560, 84)
    bola_txt(c, t, d6, "100π cm²", X, 790, 150, 58)
    E.frase(c, t, d6 + 0.6, ps("de couro", "i", 54, TINTA2), X, 1010, "center", 0.1)


# ---------------- volume: a lata de Arquimedes ----------------
LX_, LY_, LR_ = 470, 600, 230   # a esfera dentro da lata


def b_volume(c, t, C, b):
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    a8, b8, c8, d8, e8 = (C[f"s08.{k}"] for k in "abcde")
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    X = 1300

    def arquimedes():
        esfera(c, t, C["s07"] - 0.6, LX_, LY_, LR_)
        lata(c, t, a7, LX_, LY_, LR_)
        yt, yb = LY_ - LR_ * COS, LY_ + LR_ * COS
        if t >= b7:
            aresta(c, t, b7, (LX_, yt), (LX_ + LR_, yt), TINTA, 6)
            E.foco(c, t, b7 + 0.3, 0.4, lambda q: E._cola(c, "r", LX_ + LR_ / 2, yt, 0, -1, 8, 56, "g", TINTA, q))
            xc = LX_ + LR_ + 50
            aresta(c, t, b7 + 0.5, (xc, yb), (xc, yt), TINTA, 4)
            E.foco(c, t, b7 + 0.8, 0.4, lambda q: E._cola(c, "2r", xc, LY_, 1, 0, 14, 60, "g", COR, q))
    fase(c, t, C["s07"], C["s10"] - 0.1, arquimedes)

    def texto07():
        E.frase(c, t, a7, ps("a", "i", 62) + [("lata", "g", 66, COR)] + ps("em que a bola cabe", "i", 62), X, 230, "center", 0.1)
        E.frase(c, t, b7, ps("mesmo raio, altura", "i", 58) + [("2 raios", "g", 62, COR)], X, 340, "center", 0.1)
        E.frase(c, t, lerp(b7, c7, 0.45), ps("Arquimedes, há mais de 2.000 anos:", "i", 50, TINTA2), X, 520, "center", 0.08)
        E.frase(c, t, c7, [("esfera", "g", 70, COR)] + ps("=", "i", 66), X - 150, 680, "center", 0.1)
        fcen(c, t, c7 + 0.3, "f{2}{3}", X + 30, 690, 90, COR)
        E.frase(c, t, c7 + 0.5, ps("da lata", "i", 66), X + 200, 680, "center", 0.1)
        E.foco(c, t, c7 + 0.6, 0.5, lambda q: E.barra_fatias(c, X - 300, 790, 600, 100, 3, 2, E.COR, q))
    fase(c, t, C["s07"], C["s08"] - 0.1, texto07)

    def formula():
        E.frase(c, t, a8, ps("lata: base", "i", 58), X - 160, 230, "center", 0.1)
        fcen(c, t, a8 + 0.4, "πr^2", X + 60, 230, 70, COR)
        E.frase(c, t, b8, ps("altura", "i", 58), X - 160, 330, "center", 0.1)
        fcen(c, t, b8 + 0.4, "2r", X + 60, 330, 70, COR)
        fcen(c, t, c8, "πr² · 2r = 2πr^3", X, 470, 80)
        fcen(c, t, d8, "f{2}{3} · 2πr³ =", X - 160, 690, 80)
        fcen(c, t, d8 + 0.6, "V = f{4πr³}{3}", X + 250, 690, 96, COR)
        if t >= d8 + 0.6:
            p = ep(t, d8 + 0.6, 0.5)
            E.caixa_pontilhada(c, X + 60, 570, 390, 190, p, prog_=p)
        E.foco(c, t, e8, 0.5, lambda q: E.pilula(c, "volume: 3 medidas → r³", X, 900, 58, "g", a=q, cor=E.SOBRE))
    fase(c, t, C["s08"], C["s09"] - 0.1, formula)
    if C["s09"] - 0.1 <= t < C["s10"] + 0.3:
        E.saida(c, t, C["s10"] - 0.1, lambda: casca_lata(c, t, C))
    if t < C["s10"] - 0.1:
        return
    # o reservatório
    esfera(c, t, C["s10"] - 0.3, LX_, LY_, LR_)
    if t >= a0:
        raio_esf(c, t, a0, LX_, LY_, LR_, -35, "3 m", size=58)
    fcen(c, t, C["s10"] + 0.2, "V = f{4πr³}{3}", X, 230, 80, TINTA2)
    E.frase(c, t, a0, ps("reservatório de", "i", 56) + [("raio 3 m", "g", 60, COR)], X, 360, "center", 0.1)
    fcen(c, t, b0, "3 · 3 · 3 = 27", X, 490, 78)
    fcen(c, t, c0, "27 ÷ 3 = 9", X, 610, 78)
    fcen(c, t, d0, "9 × 4 = 36", X, 730, 78)
    bola_txt(c, t, e0, "36π m³", X, 900, 115, 56)


def casca_lata(c, t, C):
    """s09: a lateral da lata aberta (2πr × 2r) tem a mesma área da casca"""
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    X = 1300
    lateral_lata(c, LX_, LY_, LR_, ep(t, C["s09"] + 0.2, 0.5) * (1 - 0.5 * ep(t, d9, 0.4)))
    rx, ry, rw, rh = 1010, 300, 600, 230
    p = ease_io(prog(t, a9 - 0.3, 0.8))
    if p > 0:
        c.drawRect(skia.Rect.MakeXYWH(rx, ry, rw * p, rh), M.paint(E.mix(E.COR, "#FFFFFF", 0.6)))
        c.drawRect(skia.Rect.MakeXYWH(rx, ry, rw * p, rh), M.paint(TINTA, 1, stroke=5))
    E.frase(c, t, C["s09"] + 0.2, ps("a lateral da lata, aberta", "i", 56), rx + rw / 2, 220, "center", 0.1)
    if t >= a9:
        E.chave(c, rx, rx + rw, ry + rh + 26, COR, ep(t, a9, 0.5), 24)
        E.foco(c, t, a9 + 0.3, 0.4, lambda q: E.formula(c, "2πr", rx + rw / 2, ry + rh + 120, 64, "g", COR, q, "center"))
    if t >= b9:
        aresta(c, t, b9, (rx + rw + 30, ry + rh), (rx + rw + 30, ry), TINTA, 6)
        E.foco(c, t, b9 + 0.3, 0.4, lambda q: E.escreve(c, "2r", rx + rw + 56, ry + rh / 2 + 22, 64, "g", COR, q))
    fcen(c, t, c9, "2πr · 2r = 4πr^2", X + 10, 780, 92)
    E.foco(c, t, d9, 0.5, lambda q: E.selo(c, X - 250, 935, 46, True, q))
    E.frase(c, t, d9 + 0.1, ps("a mesma área da", "i", 58) + [("casca", "g", 64, COR)], X - 180, 960, "left", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a1, b1, c1, d1, e1, f1 = (C[f"s11.{k}"] for k in "abcdef")
    cx, cy, r = 430, 640, 150
    E.frase(c, t, C["s11"] + 0.2, [("erro comum:", "g", 66, ERRADO)], W / 2, 180, "center", 0.1)
    E.frase(c, t, a1, ps("usar o", "i", 62) + [("diâmetro", "g", 66, ERRADO)] + ps("no lugar do", "i", 62) + [("raio", "g", 66, COR)],
            W / 2, 280, "center", 0.1)
    esfera(c, t, b1, cx, cy, r)
    if t >= b1:
        aresta(c, t, b1 + 0.5, (cx - r, cy), (cx + r, cy), ERRADO, 7, a=1 - ep(t, f1, 0.4))
        E.foco(c, t, b1 + 0.8, 0.4, lambda q: centro(c, "6 m de diâmetro", cx, cy + r + 80, 50, "g", ERRADO, q * (1 - ep(t, f1, 0.4))))
    # a esfera errada: raio 6, por fora
    q = ease_back(prog(t, e1 - 0.2, 0.7))
    if q > 0:
        pt = M.paint(ERRADO, 1, stroke=6)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawCircle(cx, cy, 2 * r * q, pt)
        c.drawCircle(cx, cy, 2 * r * q, M.paint(ERRADO, 0.07))
    if t >= f1:
        raio_esf(c, t, f1 + 0.3, cx, cy, r, 0, "3", size=56, largura=9)
    X = 1330
    fcen(c, t, c1, "6³ = 216", X, 440, 84, ERRADO)
    fcen(c, t, d1, "f{4π · 216}{3} = 288π", X - 40, 600, 76, ERRADO)
    E.foco(c, t, d1 + 0.8, 0.5, lambda q: E.selo(c, X + 360, 580, 44, False, q))
    E.frase(c, t, e1, [("8 vezes", "g", 70, ERRADO)] + ps("o certo: o raio entra", "i", 58) + [("ao cubo", "g", 62)], X, 770, "center", 0.1)
    fcen(c, t, f1, "6 ÷ 2 = 3", X - 180, 930, 84, COR)
    E.foco(c, t, f1 + 0.7, 0.5, lambda q: E.pilula(c, "raio 3", X + 200, 905, 66, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def riscado(c, t, t0, tr, partes, riscar, y, size, cor_r=ERRADO):
    """fórmula em partes, centrada; as partes de índice em riscar levam um risco no instante tr"""
    ws = [E.formula(None, s_, 0, 0, size, "g", a=0) for s_ in partes]
    x = W / 2 - sum(ws) / 2
    xs = []
    for w_ in ws:
        xs.append(x); x += w_
    E.foco(c, t, t0, 0.5, lambda q: [E.formula(c, s_, xx, y, size, "g", CLARO if k in riscar else BR, q) for k, (s_, xx) in enumerate(zip(partes, xs))])
    if t >= tr:
        for n, k in enumerate(riscar):
            E.risco(c, xs[k] - 8, y + 10, xs[k] + ws[k] + 8, y - size * 0.8, t, tr + 0.3 * n, cor_r, 10)


def b_atalho(c, t, C, b):
    palco(c, t)
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")

    def um():
        E.frase(c, t, C["s12"] + 0.2, ps("atalho do", "i", 70, CLARO) + [("volume", "g", 74, BR)], W / 2, 190, "center", 0.1)
        fcen(c, t, a2, "π = 3", W / 2, 330, 90, CLARO)
        riscado(c, t, a2 + 0.4, b2, ("V = 4 · ", "3", " · r³ ÷ ", "3"), (1, 3), 530, 120)
        fcen(c, t, c2, "V = 4r^3", W / 2, 720, 130, BR)
        fcen(c, t, d2, "4 × 27 = 108 m³", 720, 920, 80, CLARO)
        bola_txt(c, t, e2, "108.000 L", 1380, 895, 140, 50)
    fase(c, t, C["s12"], C["s13"] - 0.1, um)
    if t < C["s13"] - 0.1:
        return

    def dois():
        E.frase(c, t, C["s13"] + 0.2, ps("na", "i", 70, CLARO) + [("área", "g", 74, BR)] + ps("não tem divisão", "i", 70, CLARO), W / 2, 190, "center", 0.1)
        fcen(c, t, a3, "4 × 3 = 12", 640, 380, 90, CLARO)
        fcen(c, t, b3, "A = 12r^2", 1300, 380, 120, BR)
    fase(c, t, C["s13"], C["s13.end"] + 5, dois)
    fcen(c, t, c3, "× 3  e  ÷ 3  se desfazem", W / 2, 600, 86, BR)
    E.foco(c, t, d3, 0.5, lambda a: E.selo(c, 470, 772, 44, False, a))
    E.frase(c, t, d3 + 0.1, ps("não compensa: resposta com o", "i", 56, CLARO) + [("π", "g", 62, BR)] + ps("escrito", "i", 56, CLARO), 540, 795, "left", 0.1)
    E.foco(c, t, e3, 0.5, lambda a: E.pilula(c, "aí, use a fórmula inteira", W / 2, 960, 60, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
QX, QY, QR = 1460, 620, 250


def b_questao(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    E.frase(c, t, C["s14"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a4, ps("luminária:", "i", 62) + [("esfera", "g", 66, COR)], XE, 340, passo=0.1)
    E.frase(c, t, a4 + 0.8, ps("raio", "i", 62) + [("10 cm", "g", 66, COR)], XE, 450, passo=0.1)
    E.frase(c, t, b4, [("π = 3", "g", 66, COR)], XE, 560, passo=0.1)
    E.frase(c, t, c4, [("1)", "g", 62, COR)] + ps("quanto plástico na superfície?", "i", 60), XE, 720, passo=0.1)
    E.frase(c, t, d4, [("2)", "g", 62, COR)] + ps("quantos litros de ar cabem?", "i", 60), XE, 830, passo=0.1)

    def luminaria():
        esfera(c, t, a4, QX, QY, QR)
        if t >= a4 + 0.8:
            raio_esf(c, t, a4 + 0.8, QX, QY, QR, -35, "10 cm", size=54)
    E.saida(c, t, C["s15.a"] - 0.1, luminaria)
    E.relogio(c, t, C["s15.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a6, b6 = C["s16.a"], C["s16.b"]
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    a8, b8 = C["s18.a"], C["s18.b"]
    cx, cy, r = 380, 600, 230
    esfera(c, t, C["s16"], cx, cy, r)
    raio_esf(c, t, C["s16"] + 0.6, cx, cy, r, -35, "10", size=56)
    X = 1240

    def area():
        E.frase(c, t, C["s16"] + 0.2, [("1)", "g", 64, COR)] + ps("área, pelo atalho", "i", 62), X, 200, "center", 0.1)
        fcen(c, t, C["s16"] + 0.8, "A = 12r^2", X, 360, 90, TINTA2)
        fcen(c, t, a6, "10² = 100", X, 520, 84)
        fcen(c, t, b6, "12 × 100", X - 200, 750, 84)
        bola_txt(c, t, b6 + 0.6, "1.200 cm²", X + 210, 725, 145, 50)
    fase(c, t, C["s16"], C["s17"] - 0.1, area)

    def volume():
        E.frase(c, t, C["s17"] + 0.1, [("2)", "g", 64, COR)] + ps("volume, pelo atalho", "i", 62), X, 200, "center", 0.1)
        fcen(c, t, C["s17"] + 0.4, "V = 4r^3", X, 340, 84, TINTA2)
        fcen(c, t, a7, "10³ = 1.000", X, 480, 80)
        fcen(c, t, b7, "4 × 1.000 = 4.000 cm³", X, 620, 80)
        fcen(c, t, c7, "1.000 cm³ = 1 L", X - 160, 850, 70, COR)
        bola_txt(c, t, d7, "4 L", X + 290, 825, 110, 76)
    fase(c, t, C["s17"], C["s18"] - 0.1, volume)
    if t < C["s18"] - 0.1:
        return
    E.frase(c, t, C["s18"] + 0.2, ps("pela fórmula inteira", "i", 66), X, 200, "center", 0.1)
    fcen(c, t, C["s18"] + 0.6, "V = f{4πr³}{3}", X, 380, 84, TINTA2)
    fcen(c, t, a8, "4 × 3 × 1.000 = 12.000", X, 580, 80)
    fcen(c, t, b8, "12.000 ÷ 3 = 4.000", X, 730, 84, COR)
    E.foco(c, t, b8 + 0.9, 0.5, lambda a: E.selo(c, X - 120, 900, 60, True, a))
    E.frase(c, t, b8 + 1.1, [("bateu", "g", 72, CERTO)], X - 30, 925, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s19.a", ps("área:", "i", 66), "4πr^2", "a casca de 4 círculos"), ("s19.b", ps("volume:", "i", 66), "f{4πr³}{3}", "2/3 da lata"))
        for i, (k, l1, f_, nota) in enumerate(itens):
            y = 480 + i * 260
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 420, y - 25, 52, a=a), centro(c, str(i + 1), 420, y - 4, 60, "g", E.SOBRE, a)))
            wl = E.frase(c, t, C[k] + 0.1, l1, 510, y, "left", 0.12)
            E.formula_em(c, t, C[k] + 0.5, f_, 510 + wl + 24, y, 80, "g", COR)
            E.frase(c, t, C[k] + 1.2, ps(nota, "i", 52, TINTA2), 1000, y, "left", 0.1)
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    a2, b2, c2, d2, e2 = (C[f"s20.{k}"] for k in "abcde")
    E.frase(c, t, C["s20"] + 0.2, ps("na próxima aula", "i", 80), XE, 230, passo=0.12)
    E.frase(c, t, C["s20"] + 0.8, [("partes", "g", 110, COR)] + ps("da esfera", "i", 92), XE, 380)
    E.frase(c, t, a2, ps("meia esfera:", "i", 58) + [("hemisfério", "g", 62, COR)], XE, 510, passo=0.1)
    E.frase(c, t, b2, ps("o gomo:", "i", 58) + [("fuso", "g", 62, COR)], XE, 610, passo=0.1)
    E.frase(c, t, c2, ps("o corte fora do centro:", "i", 58) + [("Pitágoras", "g", 62, COR)], XE, 710, passo=0.1)
    ex, ey, er = 1560, 640, 200
    esfera(c, t, C["s20"] + 0.8, ex, ey, er)
    hemisferio(c, ex, ey, er, ep(t, a2, 0.5) * (1 - ep(t, b2, 0.4)))
    fuso(c, ex, ey, er, ep(t, b2, 0.5) * (1 - ep(t, c2, 0.4)))
    secao(c, ex, ey, er, 0.55, ep(t, c2, 0.5))
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d2 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(620, 355, p), ep(t, d2 + 0.2, 0.4))
    E.frase(c, t, e2, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1000, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, esfera=b_esfera, area=b_area, volume=b_volume, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
