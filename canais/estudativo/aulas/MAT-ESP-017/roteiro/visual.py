"""Visual — Estudativo · MAT-ESP-017: sólidos compostos, somar e subtrair volumes.
Mesma linguagem da trilha (MAT-ESP-001 a 016): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
a 2ª família em cinza, resposta na esfera. π = 3 em toda a aula, como no roteiro.
- O SILO: E.cilindro com E.cone em cima, de mesmo raio; as duas peças se afastam (silo()), cada uma com a sua altura numa
  cota ao lado (6 e 3); a peça da vez pintada (cilindro em COR, cone em cinza). Juntar = as peças voltam a encostar.
- A PEÇA COM FURO: E.cubo (perspectiva cavaleira) com o furo de frente para quem olha: na face da frente ele é um círculo de
  verdade, e o fundo do furo aparece tracejado na face de trás (furo_cubo()). Tirar = o furo sai da peça como um cilindro.
- ERRO: a altura total 9 marcada em vermelho ao lado do cilindro esticado até a ponta (o cilindro errado, tracejado em vermelho).
- ATALHO (palco): o cone vira um cilindro baixinho de altura 1 sobre o de altura 6: 6 + 1 = 7.
- O TUBO (questão): E.cilindro em pé com o furo; a ponta é uma coroa pintada (coroa()).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-017_solidos_compostos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("metodo", "silo", "furo", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))
assert 3 * 2 ** 2 == 12 and 12 * 6 == 72 and 12 * 3 == 36 and 36 // 3 == 12 and 72 + 12 == 84 and 84 == 28 * 3
assert 6 + 3 // 3 == 7 and 12 * 7 == 84 and 12 * 9 == 108 and 108 + 12 == 120
assert 10 ** 3 == 1000 and 2 ** 2 == 4 and 3 * 4 * 10 == 120 and 1000 - 120 == 880
assert 3 * 25 * 10 == 750 and 3 * 16 * 10 == 480 and 750 - 480 == 270 and 3 * (25 - 16) == 27 and 27 * 10 == 270


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra (palavra com ², ³, √, π ou ° vai na grotesca)"""
    out = []
    for w in txt.split():
        g = any(ch in w for ch in "²³√π°")
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


def cota(c, t, t0, x, y0, y1, rot, cor=None, size=54, lado=1, a=1.0):
    """cota vertical de y0 a y1 em x, com tracinhos nas pontas e o rótulo ao lado"""
    q = ep(t, t0, 0.4) * a
    if q <= 0:
        return
    M.line(c, x, y0, x, y1, cor or TINTA, q, 4, progress=ease_io(prog(t, t0, 0.5)))
    for y in (y0, y1):
        M.line(c, x - 12, y, x + 12, y, cor or TINTA, q, 4)
    E.foco(c, t, t0 + 0.2, 0.4, lambda k: E._cola(c, rot, x, (y0 + y1) / 2, lado, 0, 14, size, "g", cor or COR, k * a))


# ================= peças desta aula =================
def tampa(c, cx, cy, r, a=1.0, cor=None, alfa_=0.55):
    if a <= 0:
        return
    ry = r * SEN
    c.drawOval(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), M.paint(cor or E.COR, alfa_ * a))


def lateral(c, cx, cy, r, h, a=1.0, cor=None, alfa_=0.5):
    """a lateral do E.cilindro pintada (de MAT-ESP-008)"""
    if a <= 0:
        return
    ry, ct = r * SEN, cy - h * COS
    p = skia.Path()
    p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.lineTo(cx + r, ct)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
    p.close()
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


def lateral_cone(c, cx, cy, r, h, a=1.0, cor=None, alfa_=0.5):
    """a lateral do E.cone pintada (de MAT-ESP-013)"""
    if a <= 0:
        return
    ry, hy = r * SEN, h * COS
    yt = -ry * ry / hy
    xt = r * math.sqrt(max(0.0, 1 - (yt / ry) ** 2))
    at = math.degrees(math.atan2(yt / ry, xt / r))
    p = skia.Path()
    p.moveTo(cx, cy - hy); p.lineTo(cx - xt, cy + yt)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180 - at, -(180 - 2 * at), False)
    p.close()
    c.drawPath(p, M.paint(cor or CINZA2, alfa_ * a))


S = 62                              # px por metro no silo
SX, SY, SR, SHC, SHK = 470, 960, 2 * S, 6 * S, 3 * S


def silo(c, t, t0, sep=0.0, pc=0.0, pk=0.0, cotas=None, t1=None, cx=SX, cy=SY, esc=1.0):
    """o silo: cilindro (raio 2, altura 6) e cone (altura 3) em cima; sep = quanto o cone sobe; pc/pk pintam as peças.
    cotas = (instante do 6, instante do 3); t1 = instante do cone (senão, junto)"""
    r, hc, hk = SR * esc, SHC * esc, SHK * esc
    E.cilindro(c, t, t0, cx, cy, r, hc)
    lateral(c, cx, cy, r, hc, pc, E.COR, 0.4)
    yk = cy - hc * COS - sep
    E.cone(c, t, t0 + 0.4 if t1 is None else t1, cx, yk, r, hk)
    lateral_cone(c, cx, yk, r, hk, pk, TINTA2, 0.28)
    if cotas:
        x = cx + r + 40
        cota(c, t, cotas[0], x, cy, cy - hc * COS, "6", TINTA2 if pc == 0 else COR)
        cota(c, t, cotas[1], x, yk, yk - hk * COS, "3", TINTA2 if pk == 0 else COR)
    return yk


A10 = 380                          # aresta do cubo (38 px por cm)
FX, FY = 150, 880                  # canto de baixo à esquerda da frente


def furo_cubo(c, t, t0, pts, r, a=1.0, cor=None, alfa_=0.0):
    """o furo de lado a lado: círculo na face da frente e o fundo tracejado na face de trás; alfa_ pinta o furo"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    cf = (sum(pts[i][0] for i in range(4)) / 4, sum(pts[i][1] for i in range(4)) / 4)
    cb = (sum(pts[i][0] for i in range(4, 8)) / 4, sum(pts[i][1] for i in range(4, 8)) / 4)
    dx, dy = cb[0] - cf[0], cb[1] - cf[1]
    n = math.hypot(dx, dy) or 1
    ux, uy = -dy / n * r, dx / n * r      # as duas geratrizes do furo, tangentes aos círculos
    if alfa_ > 0:
        p = skia.Path()
        p.addCircle(cf[0], cf[1], r)
        c.drawPath(p, M.paint(cor or E.COR, alfa_ * q))
        pp = skia.Path(); pp.addPoly([(cf[0] + ux, cf[1] + uy), (cb[0] + ux, cb[1] + uy), (cb[0] - ux, cb[1] - uy), (cf[0] - ux, cf[1] - uy)], True)
        c.drawPath(pp, M.paint(cor or E.COR, alfa_ * 0.6 * q))
    pt = M.paint(TINTA, 0.55 * q, stroke=4); pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawCircle(cb[0], cb[1], r, pt)
    for s_ in (1, -1):
        c.drawLine(cf[0] + s_ * ux, cf[1] + s_ * uy, cb[0] + s_ * ux, cb[1] + s_ * uy, pt)
    c.drawCircle(cf[0], cf[1], r, M.paint(E.mix(E.COR, "#FFFFFF", 0.9), q * (1 - min(1, alfa_ * 2))))
    c.drawCircle(cf[0], cf[1], r, M.paint(TINTA, q, stroke=6))
    return cf, cb


def cilindro_deitado(c, cf, cb, r, a=1.0, cor=None):
    """o furo fora da peça: um cilindro deitado da frente (cf) até o fundo (cb), pintado"""
    if a <= 0:
        return
    dx, dy = cb[0] - cf[0], cb[1] - cf[1]
    n = math.hypot(dx, dy) or 1
    ux, uy = -dy / n * r, dx / n * r
    p = skia.Path(); p.addPoly([(cf[0] + ux, cf[1] + uy), (cb[0] + ux, cb[1] + uy), (cb[0] - ux, cb[1] - uy), (cf[0] - ux, cf[1] - uy)], True)
    c.drawPath(p, M.paint(cor or E.COR, 0.35 * a))
    c.drawCircle(cb[0], cb[1], r, M.paint(cor or E.COR, 0.35 * a))
    for s_ in (1, -1):
        M.line(c, cf[0] + s_ * ux, cf[1] + s_ * uy, cb[0] + s_ * ux, cb[1] + s_ * uy, TINTA, a, 5)
    c.drawCircle(cf[0], cf[1], r, M.paint(E.mix(cor or E.COR, "#FFFFFF", 0.5), a))
    c.drawCircle(cf[0], cf[1], r, M.paint(TINTA, a, stroke=5))


def coroa(c, cx, cy, R, r, a=1.0, cor=None, alfa_=0.55, furo=True):
    """a ponta do tubo: o anel entre a elipse de fora (R) e a do furo (r)"""
    if a <= 0:
        return
    p = skia.Path()
    p.addOval(skia.Rect.MakeXYWH(cx - R, cy - R * SEN, 2 * R, 2 * R * SEN))
    if furo:
        p.addOval(skia.Rect.MakeXYWH(cx - r, cy - r * SEN, 2 * r, 2 * r * SEN))
        p.setFillType(skia.PathFillType.kEvenOdd)
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


TX, TY, TS = 470, 900, 34           # o tubo: 34 px por decímetro (raio 5, furo 4, comprimento 10)


def tubo(c, t, t0, tf=None, a=1.0, ponta=0.0, cheio=0.0, furo_p=0.0):
    """o tubo em pé: E.cilindro de raio 5 e o furo de raio 4 (a boca de cima e o tracejado das paredes de dentro).
    ponta pinta a coroa; cheio pinta o cilindro cheio; furo_p pinta o furo"""
    R, r, h = 5 * TS, 4 * TS, 10 * TS
    E.cilindro(c, t, t0, TX, TY, R, h)
    ct = TY - h * COS
    lateral(c, TX, TY, R, h, cheio, E.COR, 0.35)
    tampa(c, TX, ct, R, cheio, E.COR, 0.35)
    q = ep(t, t0 + 0.5 if tf is None else tf, 0.5) * a
    if q > 0:
        lateral(c, TX, TY, r, h, furo_p, E.COR, 0.45)
        c.drawOval(skia.Rect.MakeXYWH(TX - r, ct - r * SEN, 2 * r, 2 * r * SEN), M.paint(E.mix(E.COR, "#FFFFFF", 0.92), q * (1 - furo_p)))
        if furo_p > 0:
            tampa(c, TX, ct, r, furo_p, E.COR, 0.5)
        c.drawOval(skia.Rect.MakeXYWH(TX - r, ct - r * SEN, 2 * r, 2 * r * SEN), M.paint(TINTA, q, stroke=5))
        pt = M.paint(TINTA, 0.5 * q, stroke=4); pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        for x in (TX - r, TX + r):
            c.drawLine(x, ct, x, TY, pt)
        c.drawArc(skia.Rect.MakeXYWH(TX - r, TY - r * SEN, 2 * r, 2 * r * SEN), 0, 180, False, pt)
    coroa(c, TX, ct, R, r, ponta)
    return ct


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]

    def um():
        sep = 70 * ease_io(prog(t, c1, 0.9))
        silo(c, t, a1, sep, ep(t, c1 + 0.6, 0.5), ep(t, c1 + 0.9, 0.5))
        E.frase(c, t, a1, ps("um", "i", 64) + [("silo", "g", 72, COR)] + ps("de fazenda", "i", 64), 1000, 260, "left", 0.1)
        E.frase(c, t, b1, ps("um", "i", 60) + [("cilindro", "g", 64, COR)] + ps("com um telhado", "i", 60), 1000, 380, "left", 0.1)
        E.frase(c, t, b1 + 0.8, ps("em forma de", "i", 60) + [("cone", "g", 64, TINTA2)], 1000, 470, "left", 0.1)
        E.frase(c, t, lerp(b1, c1, 0.5), ps("fórmula de silo?", "i", 60), 1000, 620, "left", 0.1)
        E.foco(c, t, lerp(b1, c1, 0.5) + 0.8, 0.4, lambda q: E.selo(c, 1490, 600, 40, False, q))
        E.frase(c, t, c1, ps("corte em", "i", 60) + [("sólidos", "g", 64, COR)], 1000, 780, "left", 0.1)
        E.frase(c, t, c1 + 0.5, [("que você já conhece", "g", 64, COR)], 1000, 870, "left", 0.1)
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), ps("o", "i", 90) + [("volume", "g", 104, COR)], XE, 450, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("de sólidos", "i", 90) + [("montados", "g", 104, COR)], XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.75), ps("com e sem furo", "i", 80), XE, 720, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "volumes", XE + 215, 700, 110, "i", TINTA, a))
    x, w = 940, 860
    itens = (("s03.b", "cilindro:", "V = πr² · h"), ("s03.c", "cone:", "f{1}{3} do cilindro"), ("s03.d", "cubo:", "V = a · a · a"))
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


# ---------------- o método ----------------
def b_metodo(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    E.frase(c, t, a4, ps("o método:", "i", 72) + [("3 passos", "g", 80, COR)], XE, 220, passo=0.12)
    E.passo(c, t, b4, 1, "separe", "em peças conhecidas", 400)
    E.passo(c, t, c4, 2, "calcule cada peça", "cada uma com a sua altura", 600)
    E.passo(c, t, d4, 3, "some e subtraia", "some o que juntou, subtraia o que tirou", 800)
    sep = 60 * ease_io(prog(t, b4 + 0.5, 0.8))
    silo(c, t, a4, sep, 0, 0, cotas=(c4 + 0.3, c4 + 0.6), cx=1560, cy=940, esc=0.8)
    E.foco(c, t, d4 + 0.5, 0.4, lambda q: (centro(c, "+", 1760, 640, 90, "g", COR, q)))


# ---------------- o silo ----------------
def b_silo(c, t, C, b):
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6 = C["s06.a"], C["s06.b"], C["s06.c"]
    a7, b7, c7 = C["s07.a"], C["s07.b"], C["s07.c"]
    sep = 70 * (1 - ease_io(prog(t, a7, 0.8)))
    pc = ep(t, b6, 0.5) * (1 - ep(t, c6, 0.4)) + ep(t, b7, 0.5)
    pk = ep(t, c6, 0.5)
    silo(c, t, C["s05"] - 0.6, sep, min(1.0, pc), min(1.0, pk), cotas=(a5 + 0.4, b5 + 0.4), t1=b5)
    tampa(c, SX, SY, SR, ep(t, a6, 0.5) * (1 - ep(t, b6, 0.4)), E.COR, 0.6)
    if t >= a5:
        aresta(c, t, a5, (SX, SY), (SX + SR, SY), TINTA, 6)
        E.foco(c, t, a5 + 0.3, 0.4, lambda q: E._cola(c, "2", SX + SR / 2, SY, 0, -1, 8, 52, "g", TINTA, q))
    X = 1330

    def dados():
        E.frase(c, t, a5, [("cilindro:", "g", 62, COR)] + ps("raio 2 m, altura 6 m", "i", 58), X, 300, "center", 0.1)
        E.frase(c, t, b5, [("cone:", "g", 62, TINTA2)] + ps("mesmo raio, altura 3 m", "i", 58), X, 430, "center", 0.1)
        E.frase(c, t, c5, [("π = 3", "g", 64, COR)], X, 580, "center", 0.1)
    fase(c, t, C["s05"], C["s06"] - 0.1, dados)

    def contas():
        fcen(c, t, a6, "base: 3 × 2² = 12 m²", X, 240, 70)
        E.frase(c, t, a6 + 1.2, ps("a mesma nas duas peças", "i", 50, TINTA2), X, 320, "center", 0.1)
        fcen(c, t, b6, "cilindro: 12 × 6 = 72", X, 480, 74, COR)
        fcen(c, t, c6, "cone: 12 × 3 = 36", X, 630, 74, TINTA2)
        fcen(c, t, c6 + 1.4, "36 ÷ 3 = 12", X, 750, 74, TINTA2)
    fase(c, t, C["s06"], C["s07"] - 0.1, contas)
    if t < C["s07"] - 0.1:
        return
    E.frase(c, t, C["s07"] + 0.1, ps("as peças foram juntadas:", "i", 60), X, 260, "center", 0.1)
    E.frase(c, t, a7, [("some", "g", 90, COR)], X, 400, "center", 0.1)
    fcen(c, t, b7, "72 + 12", X - 200, 620, 90)
    bola_txt(c, t, b7 + 0.6, "84 m³", X + 220, 595, 115, 62)
    E.frase(c, t, c7, ps("de grãos", "i", 58, TINTA2), X + 220, 790, "center", 0.1)


# ---------------- o furo ----------------
def b_furo(c, t, C, b):
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    pts = E.cubo(c, t, b8, FX, FY, A10, "10 cm")
    sai = ease_io(prog(t, d9, 1.0))
    fu = furo_cubo(c, t, c8, pts, 2 * A10 / 10, alfa_=0.5 * ep(t, c9, 0.5) * (1 - sai))
    if t >= a9:
        face = skia.Path(); face.addPoly([pts[i] for i in (0, 1, 2, 3)], True)
        c.drawPath(face, M.paint(E.COR, 0.18 * ep(t, a9, 0.5) * (1 - ep(t, b9, 0.4))))
    if fu and t >= b9:
        cf, cb = fu
        aresta(c, t, b9, cf, cb, E.COR, 7)
        E.foco(c, t, b9 + 0.3, 0.4, lambda q: E._cola(c, "10", (cf[0] + cb[0]) / 2, (cf[1] + cb[1]) / 2, -0.6, -1, 12, 54, "g", COR, q * (1 - sai)))
    if fu and t >= c8:
        cf, cb = fu
        r = 2 * A10 / 10
        aresta(c, t, c8 + 0.3, cf, (cf[0] + r, cf[1]), TINTA, 6, a=1 - sai)
        E.foco(c, t, c8 + 0.5, 0.4, lambda q: E._cola(c, "2", cf[0] + r / 2, cf[1], 0, 1, 8, 50, "g", TINTA, q * (1 - sai)))
    if fu and sai > 0:
        cf, cb = fu
        dx = 470 * sai
        cilindro_deitado(c, (cf[0] + dx, cf[1] + 40 * sai), (cb[0] + dx, cb[1] + 40 * sai), 2 * A10 / 10, ep(t, d9, 0.4))
    X = 1420

    def peca():
        E.frase(c, t, a8, ps("agora o contrário:", "i", 62) + [("tirar", "g", 70, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b8, [("cubo", "g", 64, COR)] + ps("de aresta 10 cm", "i", 60), X, 380, "center", 0.1)
        E.frase(c, t, c8, ps("furo cilíndrico de", "i", 58) + [("raio 2 cm", "g", 62, COR)], X, 500, "center", 0.1)
        E.frase(c, t, c8 + 1.2, ps("de lado a lado", "i", 54, TINTA2), X, 590, "center", 0.1)
    fase(c, t, C["s08"], C["s09"] - 0.1, peca)
    if t < C["s09"] - 0.1:
        return
    fcen(c, t, a9, "cubo: 10 × 10 × 10 = 1.000", X, 220, 62)
    E.frase(c, t, b9, ps("altura do furo =", "i", 56) + [("10", "g", 62, COR)], X, 340, "center", 0.1)
    fcen(c, t, c9, "2² = 4", X, 460, 70)
    fcen(c, t, c9 + 1.2, "furo: 3 × 4 × 10 = 120", X, 570, 66, COR)
    E.frase(c, t, d9, ps("o furo foi tirado:", "i", 58) + [("subtraia", "g", 64, COR)], X, 690, "center", 0.1)
    fcen(c, t, e9, "1.000 − 120", X - 170, 880, 80)
    bola_txt(c, t, e9 + 0.6, "880 cm³", X + 250, 855, 120, 50)
    E.frase(c, t, e9 + 1.2, ps("de metal", "i", 52, TINTA2), X + 250, 1030, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    silo(c, t, C["s10"] - 0.4, 0.0, 0, 0)
    xc = SX - SR - 50
    ytop = SY - (SHC + SHK) * COS
    cota(c, t, b0, xc, SY, ytop, "9", ERRADO, 58, -1)
    # o cilindro errado: até a ponta
    q = ep(t, c0, 0.5) * (1 - ep(t, e0, 0.5))
    if q > 0:
        pt = M.paint(ERRADO, q, stroke=6); pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        ry = SR * SEN
        c.drawOval(skia.Rect.MakeXYWH(SX - SR, ytop - ry, 2 * SR, 2 * ry), pt)
        for x in (SX - SR, SX + SR):
            c.drawLine(x, SY - SHC * COS, x, ytop, pt)
        lateral(c, SX, SY, SR, SHC + SHK, q, ERRADO, 0.12)
    if t >= e0:
        x = SX + SR + 40
        cota(c, t, e0, x, SY, SY - SHC * COS, "6", COR)
        cota(c, t, e0 + 0.4, x, SY - SHC * COS, ytop, "3", TINTA2)
    X = 1330
    E.frase(c, t, C["s10"] + 0.2, [("erro comum:", "g", 66, ERRADO)], X, 200, "center", 0.1)
    E.frase(c, t, a0, ps("usar a", "i", 60) + [("altura total", "g", 64, ERRADO)] + ps("numa peça só", "i", 60), X, 310, "center", 0.1)
    E.frase(c, t, b0, ps("do chão até a ponta:", "i", 56) + [("9 m", "g", 62, ERRADO)], X, 430, "center", 0.1)
    fcen(c, t, c0, "12 × 9 = 108", X, 580, 80, ERRADO)
    fcen(c, t, d0, "108 + 12 = 120", X - 40, 720, 80, ERRADO)
    E.foco(c, t, d0 + 0.8, 0.5, lambda q: E.selo(c, X + 300, 695, 44, False, q))
    E.frase(c, t, lerp(d0, e0, 0.5), ps("o cilindro de 9 m já ocupa o lugar do cone", "i", 48, TINTA2), X, 840, "center", 0.08)
    E.foco(c, t, e0, 0.5, lambda q: E.pilula(c, "cada peça, a sua altura", X, 960, 58, "g", a=q, cor=E.SOBRE))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a1, b1, c1, d1, e1 = (C[f"s11.{k}"] for k in "abcde")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    cx, cy, r = 430, 900, 110
    hc, h1 = 6 * 55, 1 * 55

    def pecas():
        E.cilindro(c, t, a1, cx, cy, r, hc, cor=BR, preenche=0.3)
        topo = cy - hc * COS
        vira = ease_io(prog(t, b1, 0.9))
        if vira < 1:
            alfa_ = 1 - vira
            pa = skia.Paint(); pa.setAlphaf(alfa_)
            c.saveLayer(None, pa); E.cone(c, t, a1 + 0.3, cx, topo, r, 3 * 55, cor=BR, preenche=0.3); c.restore()
        if vira > 0:
            pa = skia.Paint(); pa.setAlphaf(vira)
            c.saveLayer(None, pa); E.cilindro(c, t, b1, cx, topo, r, h1, cor=BR, preenche=0.9); c.restore()
        x = cx + r + 40
        for y0, y1, s_ in ((cy, topo, "6"), (topo, topo - h1 * COS, "1")):
            q = ep(t, c1 if s_ == "1" else a1 + 0.6, 0.4)
            if q > 0:
                M.line(c, x, y0, x, y1, CLARO, q, 4)
                for y in (y0, y1):
                    M.line(c, x - 12, y, x + 12, y, CLARO, q, 4)
                E._cola(c, s_, x, (y0 + y1) / 2, 1, 0, 14, 56, "g", BR, q)
    fase(c, t, C["s11"], C["s12.end"] + 5, pecas)
    X = 1260

    def um():
        E.frase(c, t, C["s11"] + 0.2, ps("atalho:", "i", 66, CLARO) + [("mesmo raio", "g", 70, BR)], X, 200, "center", 0.1)
        E.frase(c, t, b1, ps("cone = cilindro com", "i", 58, CLARO) + [("um terço", "g", 62, BR)] + ps("da altura", "i", 58, CLARO), X, 330, "center", 0.1)
        fcen(c, t, c1, "f{1}{3} de 3 = 1", X, 490, 80, CLARO)
        fcen(c, t, d1, "6 + 1 = 7", X, 640, 90, BR)
        fcen(c, t, e1, "12 × 7", X - 200, 840, 90, BR)
        bola_txt(c, t, e1 + 0.6, "84", X + 200, 815, 100, 80)
        E.frase(c, t, e1 + 1.2, ps("uma conta só", "i", 54, CLARO), X, 1000, "center", 0.1)
    fase(c, t, C["s11"], C["s12"] - 0.1, um)
    if t < C["s12"] - 0.1:
        return
    E.frase(c, t, C["s12"] + 0.1, ps("funciona porque a", "i", 62, CLARO) + [("base é a mesma", "g", 66, BR)], X, 220, "center", 0.1)
    fcen(c, t, a2 + 0.6, "12 × 6 + 12 × 1", X, 380, 84, CLARO)
    fcen(c, t, b2, "= 12 × 7", X, 510, 90, BR)
    E.foco(c, t, c2, 0.5, lambda a: E.selo(c, 900, 680, 44, False, a))
    E.frase(c, t, c2 + 0.1, ps("raios diferentes:", "i", 56, CLARO) + [("não compensa", "g", 60, BR)], 970, 702, "left", 0.1)
    E.frase(c, t, lerp(c2, d2, 0.4), ps("telhado mais largo que a parede", "i", 52, CLARO), 970, 790, "left", 0.1)
    E.foco(c, t, d2, 0.5, lambda a: E.pilula(c, "calcule peça por peça", X, 960, 60, "g", a=a, cor=E.SOBRE))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    E.frase(c, t, C["s13"] + 0.1, ps("hora de testar", "i", 72, COR), XE + 640, 200, passo=0.12)
    E.frase(c, t, a3, ps("tubo de concreto:", "i", 60) + [("cilindro", "g", 64, COR)], XE + 640, 320, passo=0.1)
    E.frase(c, t, b3, ps("raio", "i", 58) + [("50 cm,", "g", 62, COR)] + ps("comprimento", "i", 58) + [("1 m", "g", 62, COR)], XE + 640, 420, passo=0.1)
    E.frase(c, t, c3, ps("furo de", "i", 58) + [("raio 40 cm,", "g", 62, COR)] + ps("de ponta a ponta", "i", 58), XE + 640, 520, passo=0.1)
    E.frase(c, t, d3, [("π = 3", "g", 62, COR)], XE + 640, 620, passo=0.1)
    E.frase(c, t, e3, ps("quantos", "i", 62) + [("litros", "g", 66, COR)] + ps("de concreto?", "i", 62), XE + 640, 740, passo=0.1)

    def fig():
        ct = tubo(c, t, a3, tf=c3)
        if t >= b3:
            R, h = 5 * TS, 10 * TS
            aresta(c, t, b3, (TX, ct), (TX + R, ct), TINTA, 5)
            E.foco(c, t, b3 + 0.3, 0.4, lambda q: E._cola(c, "50 cm", TX + R / 2 + 40, ct - R * SEN, 0, -1, 8, 48, "g", COR, q))
            cota(c, t, b3 + 0.5, TX + R + 40, TY, ct, "1 m", COR, 50)
        if t >= c3:
            aresta(c, t, c3 + 0.4, (TX, ct), (TX - 4 * TS, ct), TINTA2, 5)
            E.foco(c, t, c3 + 0.7, 0.4, lambda q: E._cola(c, "40 cm", TX - 2 * TS - 40, ct - 5 * TS * SEN, 0, -1, 8, 48, "g", TINTA2, q))
    E.saida(c, t, C["s14.a"] - 0.1, fig)
    E.relogio(c, t, C["s14.a"], 470, 560, 200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a5, b5, c5, d5, e5 = (C[f"s15.{k}"] for k in "abcde")
    a6, b6, c6, d6, e6, f6 = (C[f"s16.{k}"] for k in "abcdef")
    cheio = ep(t, e5, 0.5) * (1 - ep(t, a6, 0.4))
    ct = tubo(c, t, C["s15"] - 0.6, ponta=ep(t, d6, 0.5), cheio=cheio, furo_p=ep(t, a6, 0.5) * (1 - ep(t, b6, 0.4)))
    R, r, h = 5 * TS, 4 * TS, 10 * TS
    if t >= b5:
        aresta(c, t, b5, (TX, ct), (TX + R, ct), TINTA, 5)
        E.foco(c, t, b5 + 0.3, 0.4, lambda q: E._cola(c, "5", TX + R * 0.75, ct - R * SEN, 0, -1, 8, 54, "g", COR, q))
    if t >= c5:
        aresta(c, t, c5, (TX, ct), (TX - r, ct), TINTA2, 5)
        E.foco(c, t, c5 + 0.3, 0.4, lambda q: E._cola(c, "4", TX - r / 2, ct - R * SEN, 0, -1, 8, 54, "g", TINTA2, q))
    cota(c, t, d5, TX + R + 40, TY, ct, "10", COR, 54)
    X = 1330

    def dm():
        E.frase(c, t, a5, ps("trabalhe em", "i", 60) + [("decímetros", "g", 64, COR)], X, 220, "center", 0.1)
        fcen(c, t, a5 + 1.0, "1 L = 1 dm³", X, 330, 64, TINTA2)
        E.frase(c, t, lerp(a5, b5, 0.6), ps("10 cm = 1 dm", "i", 52, TINTA2), X, 420, "center", 0.1)
        fcen(c, t, b5, "raio de fora: 50 cm = 5 dm", X, 540, 58)
        fcen(c, t, c5, "raio do furo: 40 cm = 4 dm", X, 640, 58, TINTA2)
        fcen(c, t, d5, "comprimento: 1 m = 10 dm", X, 740, 58)
        fcen(c, t, e5, "cheio: 3 × 25 × 10 = 750", X, 900, 66, COR)
    fase(c, t, C["s15"], C["s16"] - 0.1, dm)

    def conta():
        fcen(c, t, C["s16"] + 0.1, "cheio: 750", X, 220, 60, TINTA2)
        fcen(c, t, a6, "furo: 3 × 16 × 10 = 480", X, 350, 66)
        fcen(c, t, b6, "750 − 480", X - 200, 540, 84)
        bola_txt(c, t, c6, "270 L", X + 210, 515, 110, 62)
    fase(c, t, C["s16"], d6 - 0.1, conta)
    if t < d6 - 0.1:
        return
    E.frase(c, t, d6, ps("confira pela ponta: a", "i", 58) + [("coroa", "g", 64, COR)], X, 240, "center", 0.1)
    fcen(c, t, e6, "25 − 16 = 9", X, 400, 76)
    fcen(c, t, e6 + 1.6, "3 × 9 = 27 dm²", X, 530, 76)
    fcen(c, t, f6, "27 × 10 = 270", X, 690, 84, COR)
    E.foco(c, t, f6 + 0.8, 0.5, lambda a: E.selo(c, X - 120, 860, 60, True, a))
    E.frase(c, t, f6 + 1.0, [("bateu", "g", 72, CERTO)], X - 30, 885, "left", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], W / 2, 230, "center")
        itens = (("s17.a", ps("corte em", "i", 64) + [("peças conhecidas", "g", 64, COR)]),
                 ("s17.b", ps("cada peça com a", "i", 64) + [("sua altura", "g", 64, COR)]),
                 ("s17.c", [("some", "g", 64, COR)] + ps("o que junta,", "i", 64) + [("subtraia", "g", 64, COR)] + ps("o que tira", "i", 64)))
        for i, (k, l1) in enumerate(itens):
            y = 430 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 380, y - 25, 52, a=a), centro(c, str(i + 1), 380, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 470, y, "left", 0.12)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a8, b8, c8, d8 = (C[f"s18.{k}"] for k in "abcd")
    E.frase(c, t, C["s18"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, C["s18"] + 0.8, ps("a", "i", 96) + [("água", "g", 120, COR)] + ps("mede o volume", "i", 96), XE, 420)
    E.frase(c, t, a8, ps("a", "i", 60) + [("pedra", "g", 64, COR)] + ps("no aquário:", "i", 60) + [("quanto a água sobe", "g", 60)], XE, 560, passo=0.1)
    E.frase(c, t, b8, ps("e se o líquido", "i", 60) + [("transborda", "g", 64, COR)], XE, 660, passo=0.1)
    # o aquário com a água subindo (a ideia de MAT-ESP-005)
    x, y, w, hh = 1380, 880, 320, 240
    nivel = lerp(0.45, 0.62, ease_io(prog(t, a8 + 0.8, 1.2)))
    E.paralelepipedo(c, t, C["s18"] + 0.8, x, y, w, 120, hh, preenche=0.05)
    c.drawRect(skia.Rect.MakeXYWH(x, y - hh * nivel, w, hh * nivel), M.paint(E.COR, 0.3))
    q = ep(t, a8 + 0.6, 0.5)
    if q > 0:
        yp = lerp(y - hh - 60, y - 50, ease_io(prog(t, a8 + 0.6, 0.6)))
        p = skia.Path(); p.addOval(skia.Rect.MakeXYWH(x + w / 2 - 60, yp - 40, 120, 80))
        c.drawPath(p, M.paint(TINTA2, 0.85 * q)); c.drawPath(p, M.paint(TINTA, q, stroke=4))
    E.foco(c, t, c8, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c8 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(560, 355, p), ep(t, c8 + 0.2, 0.4))
    E.frase(c, t, d8, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1040, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, metodo=b_metodo, silo=b_silo, furo=b_furo, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
