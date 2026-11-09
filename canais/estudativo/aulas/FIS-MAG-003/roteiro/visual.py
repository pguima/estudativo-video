"""Visual — Estudativo · FIS-MAG-003: força magnética sobre uma carga. Linguagem visual do Magnetismo: veja o visual.py da FIS-MAG-001.
Força = laranja (F), velocidade = petróleo (F.VEL), campo B em tinta (símbolos saindo/entrando, setas finas). Carga + laranja,
− azul. A mão do tapa: mão direita aberta, palma para você, dedos para cima, polegar para a direita (mao()).
Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-003_forca_magnetica_sobre_uma_carga.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("quando", "formula", "sentido", "curva", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
VEL = F.VEL
PELE, PELE2 = "#F4D3B8", "#E2B48F"

# todas as contas da aula
assert math.isclose(math.sin(math.radians(30)), 0.5) and math.isclose(math.sin(math.radians(90)), 1)
assert 2 * 4 == 8 and math.isclose(1e-6 * 1e3, 1e-3)
assert math.isclose(2e-6 * 4e3 * 0.5 * 0.5, 2e-3)
assert math.isclose(5e-10 * 4e3, 2e-6) and math.isclose(2e-6 * 0.5, 1e-6) and math.isclose(2e-6 / 1e-6, 2)
assert math.isclose(5e-10 * 4e3 / (2e-6 * 0.5), 2.0)
# sentido: v = +x, B = −z (entra) → v × B = +y (palma para cima); elétron: −y, para baixo
cruz = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
assert cruz((1, 0, 0), (0, 0, -1)) == (0, 1, 0)
# a mão: polegar +x (v), dedos +y (B) → palma +z (F saindo da folha)
assert cruz((1, 0, 0), (0, 1, 0)) == (0, 0, 1)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças do magnetismo ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def simbolo_campo(c, cx, cy, r, sai=True, a=1.0, cor=None, escuro=False):
    """campo furando a folha: ponto no círculo = saindo; xis no círculo = entrando"""
    if a <= 0:
        return
    cor = cor or (BR if escuro else TINTA)
    c.drawCircle(cx, cy, r, M.paint(cor, a, stroke=max(3, r * 0.14)))
    if sai:
        c.drawCircle(cx, cy, r * 0.28, M.paint(cor, a))
    else:
        k = r * 0.62
        M.line(c, cx - k, cy - k, cx + k, cy + k, cor, a, max(3, r * 0.14))
        M.line(c, cx - k, cy + k, cx + k, cy - k, cor, a, max(3, r * 0.14))


def folha_campo(c, t, t0, x0, y0, cols, lins, passo, sai=True, r=20, cor=None, escuro=False, d=0.04, a=1.0):
    for i in range(lins):
        for j in range(cols):
            k = i * cols + j
            E.foco(c, t, t0 + d * k, 0.35, lambda a_, i=i, j=j: simbolo_campo(c, x0 + j * passo, y0 + i * passo, r, sai, a_ * a, cor, escuro), sobe=0)


def mao(c, cx, cy, s, a=1.0, giro=0.0):
    """mão direita aberta, palma para quem olha, dedos para cima e polegar para a direita; (cx, cy) = centro da palma"""
    if a <= 0:
        return
    rr = lambda x, y, w, h, r: skia.Path().addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r))
    forma = rr(-0.5 * s, -0.3 * s, s, 0.85 * s, 0.22 * s)
    fw = 0.23 * s
    for dx, L in ((-0.375, 0.5), (-0.125, 0.66), (0.125, 0.72), (0.375, 0.64)):
        forma = skia.Op(forma, rr(dx * s - fw / 2, -0.3 * s - L * s, fw, L * s + 0.2 * s, fw / 2), skia.PathOp.kUnion_PathOp)
    pol = rr(0, -0.13 * s, 0.62 * s, 0.26 * s, 0.13 * s)
    m = skia.Matrix(); m.setRotate(-28); m.postTranslate(0.36 * s, 0.22 * s)
    pol.transform(m)
    forma = skia.Op(forma, pol, skia.PathOp.kUnion_PathOp)
    c.save(); c.translate(cx, cy); c.rotate(giro)
    c.drawPath(forma, M.paint(PELE, a))
    for dx in (-0.25, 0.0, 0.25):  # vãos entre os dedos
        M.line(c, dx * s, -0.42 * s, dx * s, -0.3 * s, PELE2, a, 4)
    pt = M.paint(TINTA, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(forma, pt)
    c.restore()


def mao_regra(c, t, C, cx, cy, s, t_pol, t_ded, t_pal, rot=("v", "B", "F"), cores=(None, TINTA, None)):
    """a mão com as três pílulas: polegar, dedos e palma, cada uma no seu instante"""
    E.foco(c, t, t_pol - 0.6, 0.5, lambda a: mao(c, cx, cy, s, a))
    cv = cores[0] or VEL
    cf = cores[2] or E.COR
    E.foco(c, t, t_pol, 0.4, lambda a: (F.seta(c, cx + 0.95 * s, cy - 0.12 * s, cx + 1.55 * s, cy - 0.12 * s, cv, a, 10),
                                        E.pilula(c, f"polegar: {rot[0]}", cx + 1.55 * s, cy + 0.15 * s, 40, "g", fundo=cv, a=a)))
    E.foco(c, t, t_ded, 0.4, lambda a: (F.seta(c, cx, cy - 1.1 * s, cx, cy - 1.55 * s, cores[1], a, 10),
                                        E.pilula(c, f"dedos: {rot[1]}", cx + 0.55 * s, cy - 1.45 * s, 40, "g", fundo=cores[1], a=a)))
    E.foco(c, t, t_pal, 0.4, lambda a: (simbolo_campo(c, cx, cy + 0.12 * s, 0.16 * s, True, a, cf),
                                        E.pilula(c, f"palma: {rot[2]} para você", cx, cy + 0.85 * s, 40, "g", fundo=cf, a=a)))


def carga_em(c, cx, cy, r, sinal, a=1.0):
    """F.carga já crescida, com transparência"""
    if a <= 0:
        return
    pt = skia.Paint(); pt.setAlphaf(a)
    c.saveLayer(None, pt)
    F.carga(c, 99, 0, cx, cy, r, sinal)
    c.restore()


def campo_seta(c, x0, x1, ys, a=1.0, cor=None):
    """campo uniforme desenhado como setas finas para a direita"""
    for y in ys:
        F.seta(c, x0, y, x1, y, cor or TINTA2, a, 4, 20)


def lembrete2(c, t, C, cena, itens, desenhos):
    """lembrete de duas coisas (o mesmo da FIS-CIN-001)"""
    E.frase(c, t, C[cena] + 0.2, ps("lembre", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C[cena + ".a"], 0.5, lambda a: E.escreve(c, "2", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C[cena + ".a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisas", XE + 215, 700, 120, "i", TINTA, a))
    x, w = 820, 1000
    for i, (k, l1, l2) in enumerate(itens):
        y = 230 + i * 290
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 230, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", 58)], x + 44, y + 90)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", 58, COR)], x + 44, y + 170)
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, i=i, y=y: desenhos[i](a, x + w - 170, y + 115))
    q1 = ease_io(prog(t, C[itens[1][0]] - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(430, 720, q1), ep(t, C[itens[0][0]], 0.4))
    E.frase(c, t, lerp(C[itens[1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 56, COR) + ps("procure no canal", "i", 56), 820, 920, "left", 0.12)


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def roda(c, t, t0, cx, cy, R, w, a=1.0, sinal="+", setas=True, sentido=1):
    """carga girando no círculo (sentido=1: anti-horário na tela), com v tangente e F para o centro"""
    g = sentido * w * max(0.0, t - t0) + math.pi / 2
    x, y = cx + R * math.cos(g), cy - R * math.sin(g)
    pt = M.paint(TINTA2, 0.6 * a, stroke=4)
    pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawCircle(cx, cy, R, pt)
    if setas:
        tx, ty = -math.sin(g) * sentido, -math.cos(g) * sentido
        F.seta(c, x, y, x + tx * 170, y + ty * 170, VEL, a, 9)
        F.seta(c, x, y, x + (cx - x) / R * 150, y + (cy - y) / R * 150, E.COR, a, 9)
    carga_em(c, x, y, 34, sinal, a)
    return x, y


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        sx, sy = 260, 560
        tx, ty, r = 1350, 560, 190
        E.foco(c, t, C["s01.a"], 0.6, lambda a: (E.bola(c, sx, sy, 230, "#FFB020", a), centro(c, "Sol", sx, sy + 20, 60, "g", TINTA, a)))
        # partículas saindo do Sol
        if t >= C["s01.a"] + 0.4:
            for k in range(9):
                f = ((t - C["s01.a"]) * 0.35 + k / 9) % 1
                yk = sy - 220 + 55 * k
                if t < C["s01.c"]:
                    x, y = lerp(sx + 240, tx - 380, f), yk
                else:  # guiadas pelas linhas até os polos
                    lado = -1 if yk < sy else 1
                    x = lerp(sx + 240, tx, f)
                    y = lerp(yk, ty + lado * (r + 10), ease_io(clamp01((x - (tx - 520)) / 520)))
                c.drawCircle(x, y, 7, M.paint(E.COR, ep(t, C["s01.a"] + 0.4, 0.4)))
        if t >= C["s01.b"]:
            c.save(); c.translate(tx, ty); c.rotate(90)  # norte do "ímã" da Terra para baixo
            F.linhas_campo(c, t, C["s01.b"], 0, 0, 2 * r, 2, TINTA2, d=1.2, h=2 * r * 0.55)
            c.restore()
        E.foco(c, t, C["s01.b"], 0.6, lambda a: (E.bola(c, tx, ty, r, "#2F7FC2", a),
                                                 c.drawCircle(tx - 50, ty - 30, 70, M.paint("#3FA45B", 0.8 * a)),
                                                 c.drawCircle(tx + 60, ty + 60, 50, M.paint("#3FA45B", 0.8 * a))))
        q = ep(t, C["s01.d"], 0.6)
        if q > 0:
            for lado in (-1, 1):
                p = skia.Paint(AntiAlias=True)
                p.setShader(skia.GradientShader.MakeRadial(skia.Point(tx, ty + lado * r * 0.95), 150, [M.hexc("#3CF08A", 0.85 * q), M.hexc("#3CF08A", 0)], [0, 1]))
                c.drawCircle(tx, ty + lado * r * 0.95, 150, p)
            E.foco(c, t, C["s01.d"] + 0.3, 0.4, lambda a: E.pilula(c, "aurora", tx + 330, ty - r - 40, 52, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s01.a"], ps("partículas com", "i", 64) + [("carga", "g", 64, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("o campo da Terra", "i", 64) + [("desvia", "g", 64, COR)], XE, 960, passo=0.12)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    itens = (("s02.a", "calcular a força", 1.4), ("s02.b", "o sentido, com a mão", 0), ("s02.c", "o raio da curva", 0))
    for i, (k, s, dt) in enumerate(itens):
        y = 450 + i * 160
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def clamp01(x):
    return max(0.0, min(1.0, x))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def fcp(a, x, y):
        E.formula(c, "F = f{m · v^2}{R}", x - 40, y + 30, 70, "g", TINTA, a, "center")

    def sen(a, x, y):
        E.formula(c, "sen 90° = 1", x - 40, y - 10, 46, "g", TINTA, a, "center")
        E.formula(c, "sen 30° = f{1}{2}", x - 40, y + 70, 46, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "movimento em círculo:", "força para o centro"), ("s03.c", "seno:", "90° dá 1; 30° dá meio")), (fcp, sen))


# ---------------- quando existe ----------------
def b_quando(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04"], [("força", "g", 90, COR), ("magnética", "i", 96)], XE, 220)
        ys = (440, 560, 680, 800)
        if t >= C["s04"]:
            campo_seta(c, 760, 1760, ys, ep(t, C["s04"], 0.5))
            E.foco(c, t, C["s04"] + 0.3, 0.4, lambda a: E.escreve(c, "B", 1780, 400, 64, "g", TINTA, a))
        E.foco(c, t, C["s04.a"], 0.5, lambda a: carga_em(c, 1000, 620, 50, "+", a))
        E.foco(c, t, C["s04.a"] + 0.4, 0.4, lambda a: E.pilula(c, "parada: F = 0", 1000, 740, 44, "g", fundo=TINTA, a=a))
        if t >= C["s04.b"]:
            q = min(1.0, (t - C["s04.b"]) / 2.5)
            px, py = lerp(1300, 1500, q), lerp(820, 470, q)
            carga_em(c, px, py, 50, "+")
            F.seta(c, px, py, px + 0.5 * 200, py - 0.87 * 200, VEL, 1, 9)
            E.foco(c, t, C["s04.b"] + 0.3, 0.4, lambda a: E.escreve(c, "v", 1520, 380, 60, "g", VEL, a))
        E.frase(c, t, C["s04.b"], ps("só com carga em", "i", 60) + [("movimento", "g", 60, COR)], XE, 360, passo=0.12)
        E.frase(c, t, C["s04.c"], ps("depende do", "i", 60) + [("ângulo", "g", 60, COR)] + ps("entre v e B", "i", 60), XE, 960, passo=0.12)
        return
    E.frase(c, t, C["s05"], [("o ângulo", "g", 84, COR), ("decide", "i", 90)], XE, 200)
    for i, (k, ang, txt, cor) in enumerate((("s05.a", 0, "mesma direção: F = 0", TINTA), ("s05.b", 90, "90 graus: F máxima", E.COR))):
        x0 = 230 + i * 820
        y0 = 360
        E.foco(c, t, C[k], 0.5, lambda a, x0=x0: campo_seta(c, x0, x0 + 640, (y0 + 40, y0 + 160, y0 + 280, y0 + 400), a))
        cx, cy = x0 + 320, y0 + 220
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, cx=cx, cy=cy: carga_em(c, cx, cy, 46, "+", a))
        dx, dy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
        E.foco(c, t, C[k] + 0.5, 0.4, lambda a, cx=cx, cy=cy, dx=dx, dy=dy: F.seta(c, cx, cy, cx + dx * 220, cy + dy * 220, VEL, a, 10))
        E.foco(c, t, C[k] + 0.8, 0.4, lambda a, x0=x0, txt=txt, cor=cor: E.pilula(c, txt, x0 + 320, 900, 50, "g", fundo=cor, a=a))


# ---------------- fórmula ----------------
def b_formula(c, t, C, b):
    if t < C["s07"]:
        F.formula_legenda(c, t, C["s06.a"], "F = q · v · B · sen θ", [("q", "carga", "C"), ("v", "velocidade", "m/s"), ("B", "campo", "T"),
                                                                      ("θ", "ângulo entre v e B", None)],
                          XE, 330, 140, tl=[C["s06.b"], C["s06.c"], C["s06.d"], C["s06.e"]])
        # o ângulo
        cx, cy = 1450, 760
        if t >= C["s06.e"]:
            F.seta(c, cx, cy, cx + 300, cy, TINTA, ep(t, C["s06.e"], 0.4), 8)
            F.seta(c, cx, cy, cx + 260 * math.cos(math.radians(30)), cy - 260 * math.sin(math.radians(30)), VEL, ep(t, C["s06.e"] + 0.2, 0.4), 8)
            E.foco(c, t, C["s06.e"] + 0.5, 0.4, lambda a: (E.arco(c, cx, cy, 110, -30, 30, E.COR, 6, a), E.escreve(c, "θ", cx + 130, cy - 20, 56, "g", COR, a),
                                                          E.escreve(c, "B", cx + 320, cy + 20, 56, "g", TINTA, a), E.escreve(c, "v", cx + 240, cy - 150, 56, "g", VEL, a)))
        return
    dados = (("q = 2 · 10^{−6} C", 0), ("v = 4 · 10^{3} m/s", 0.5), ("B = 0,5 T", 1.0), ("θ = 30°", 1.5))
    for i, (s, dt) in enumerate(dados):
        E.foco(c, t, C["s07.a"] + dt * 2, 0.4, lambda a, s=s, i=i: E.formula(c, s, XE + (i % 2) * 760, 230 + (i // 2) * 120, 70, "g", TINTA, a))
    y = 620
    troca(c, t, [(C["s07.b"] - 0.6, "F = 2 · 10^{−6} · 4 · 10^{3} · 0,5 · 0,5"), (C["s07.b"] + 1.6, "F = 8 · 10^{−3} · 0,5 · 0,5")],
          lambda s, a: E.formula(c, s, XE, y, 90, "g", TINTA, a))
    E.foco(c, t, C["s07.c"], 0.5, lambda a: E.formula(c, "× sen 30° = × f{1}{2}", XE, 820, 70, "g", TINTA2, a))
    E.foco(c, t, C["s07.d"], 0.5, lambda a: (E.bola(c, 1500, 820, 170, a=a), E.formula(c, "2 · 10^{−3} N", 1500, 845, 64, "g", E.SOBRE, a, "center")))


# ---------------- sentido ----------------
def b_sentido(c, t, C, b):
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], [("F", "g", 90, COR), ("perpendicular a", "i", 90), ("v", "g", 90, VEL), ("e a", "i", 90), ("B", "g", 90)], XE, 260, passo=0.14)
        # três eixos: v para a direita, B para cima, F saindo da folha
        ox, oy = 1300, 700
        F.vetor(c, t, C["s08.a"] + 0.6, (ox, oy), (ox + 330, oy), "v", None, VEL, 10, size=64, lado=-1)
        F.vetor(c, t, C["s08.a"] + 1.0, (ox, oy), (ox, oy - 330), "B", None, TINTA, 10, size=64, lado=1)
        E.foco(c, t, C["s08.a"] + 1.4, 0.4, lambda a: (simbolo_campo(c, ox, oy, 44, True, a, E.COR), E.escreve(c, "F", ox - 120, oy + 90, 64, "g", COR, a)))
        E.frase(c, t, C["s08.b"], ps("a mão direita aberta:", "i", 66) + [("o tapa", "g", 66, COR)], XE, 420, passo=0.12)
        return
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("a mão do", "i", 80) + [("tapa", "g", 80, COR)], XE, 220, passo=0.12)
        mao_regra(c, t, C, 1150, 640, 250, C["s09.a"], C["s09.b"], C["s09.c"])
        E.foco(c, t, C["s09.c"] + 0.6, 0.4, lambda a: E.pilula(c, "carga +", XE + 140, 480, 50, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s09.d"], 0.5, lambda a: E.pilula(c, "carga −: costas da mão", XE + 290, 600, 50, "g", fundo=NEG, a=a))
        return
    E.frase(c, t, C["s10.a"], ps("na prova, o campo", "i", 80) + [("fura a folha", "g", 80, COR)], XE, 220, passo=0.12)
    for i, (k, sai, nome) in enumerate((("s10.b", True, "saindo, para você"), ("s10.c", False, "entrando na folha"))):
        x = 560 + i * 800
        E.foco(c, t, C[k], 0.5, lambda a, x=x, sai=sai: simbolo_campo(c, x, 560, 130, sai, a))
        E.frase(c, t, C[k] + 0.3, [(nome, "g", 64, COR)], x, 800, "center")


# ---------------- curva ----------------
def b_curva(c, t, C, b):
    if t < C["s12"]:
        E.frase(c, t, C["s11.a"], ps("não acelera nem freia:", "i", 64), XE, 220, passo=0.12)
        E.frase(c, t, C["s11.b"], ps("só muda a", "i", 64) + [("direção", "g", 64, COR)], XE, 320, passo=0.12)
        folha_campo(c, t, C["s11"], 900, 260, 7, 5, 150, False, 22, TINTA2)
        if t >= C["s11.a"]:
            roda(c, t, C["s11.a"], 1350, 560, 230, 0.9)
        E.foco(c, t, C["s11.c"], 0.4, lambda a: E.pilula(c, "F magnética = força para o centro", XE + 330, 900, 44, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s11.a"] + 0.4, 0.4, lambda a: (E.escreve(c, "v", XE, 520, 60, "g", VEL, a), E.escreve(c, "velocidade", XE + 60, 520, 50, "i", TINTA2, a),
                                                       E.escreve(c, "F", XE, 620, 60, "g", COR, a), E.escreve(c, "força", XE + 60, 620, 50, "i", TINTA2, a)))
        return
    if t < C["s13"]:
        E.frase(c, t, C["s12.a"], ps("iguale as duas", "i", 80), XE, 220, passo=0.12)
        E.formula_em(c, t, C["s12.a"] + 0.4, "q · v · B = f{m · v^2}{R}", W / 2, 470, 130, "g", TINTA, "center")
        if t >= C["s12.b"]:
            w = E.formula(None, "q · v · B = f{m · v^2}{R}", 0, 0, 130, a=0)
            x0 = W / 2 - w / 2
            wq = E.formula(None, "q · ", 0, 0, 130, a=0)
            E.risco(c, x0 + wq - 6, 490, x0 + wq + 70, 400, t, C["s12.b"], E.COR, 9)
            xe = x0 + E.formula(None, "q · v · B = ", 0, 0, 130, a=0) + E.formula(None, "m · v", 0, 0, 130 * 0.78, a=0) + 10
            E.foco(c, t, C["s12.b"] + 0.3, 0.3, lambda a: M.line(c, xe - 4, 395, xe + 30, 360, E.COR, a, 8))
        E.foco(c, t, C["s12.c"], 0.5, lambda a: (E.bola(c, W / 2, 790, 190, a=a), E.formula(c, "R = f{m · v}{q · B}", W / 2, 810, 84, "g", E.SOBRE, a, "center")))
        return

    E.foco(c, t, C["s13"], 0.5, lambda a: E.formula(c, "m = 5 · 10^{−10} kg,   θ = 90°", XE, 220, 70, "g", TINTA, a))
    E.foco(c, t, C["s13.a"], 0.5, lambda a: E.formula(c, "em cima:  5 · 10^{−10} · 4 · 10^{3} = 2 · 10^{−6}", XE, 420, 70, "g", TINTA, a))
    E.foco(c, t, C["s13.b"], 0.5, lambda a: E.formula(c, "embaixo:  2 · 10^{−6} · 0,5 = 10^{−6}", XE, 560, 70, "g", TINTA, a))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.formula(c, "R = f{2 · 10^{−6}}{10^{−6}}", XE, 800, 100, "g", TINTA, a))
    E.foco(c, t, C["s13.c"] + 0.5, 0.5, lambda a: (E.bola(c, 1450, 770, 150, a=a), centro(c, "2 m", 1450, 800, 80, "g", E.SOBRE, a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s14.a"], ps("a força magnética", "i", 64) + [("não acelera", "g", 64, ERRADO)], XE, 320, passo=0.12)
    cx, cy, R = 1350, 640, 230
    if t >= C["s14.b"]:
        x, y = roda(c, t, C["s14.b"], cx, cy, R, 1.1, ep(t, C["s14.b"], 0.4))
        M.line(c, cx, cy, x, y, TINTA, ep(t, C["s14.b"], 0.4), 4)
        c.drawCircle(cx, cy, 14, M.paint(TINTA, ep(t, C["s14.b"], 0.4)))
    E.frase(c, t, C["s14.b"], ps("empurra de lado,", "i", 60) + [("como a corda", "g", 60)], XE, 480, passo=0.12)
    E.frase(c, t, C["s14.c"], [("direção", "g", 60, COR), ("muda;", "i", 64)], XE, 640, passo=0.12)
    E.frase(c, t, C["s14.c"] + 0.8, [("valor de v", "g", 60), ("igual", "i", 64, CERTO)], XE, 740, passo=0.12)


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s15.a"], ps("não decore:", "i", 64, CLARO) + [("iguale e corte um v", "g", 64, BR)], W / 2, 290, "center", 0.12)
        E.formula_em(c, t, C["s15.b"], "q · v · B = f{m · v^2}{R}   →   R = f{m · v}{q · B}", W / 2, 460, 90, "g", BR, "center")
        for i, (k, txt, r) in enumerate((("s15.d", "m ou v maior: curva aberta", 170), ("s15.e", "q ou B maior: curva fechada", 80))):
            x = 560 + i * 800
            E.foco(c, t, C[k], 0.5, lambda a, x=x, r=r: c.drawCircle(x, 740, r, M.paint(E.CLARO, a, stroke=7)))
            E.foco(c, t, C[k] + 0.2, 0.4, lambda a, x=x, txt=txt: centro(c, txt, x, 980, 48, "g", BR, a))
        return
    E.frase(c, t, C["s16.a"], ps("antes da conta,", "i", 70, CLARO) + [("olhe o ângulo", "g", 70, BR)], W / 2, 200, "center", 0.12)
    y = 520
    if t >= C["s16.b"]:
        for yy in (y - 120, y, y + 120):
            F.seta(c, 300, yy, 1620, yy, E.CLARO, ep(t, C["s16.b"], 0.4) * 0.6, 4, 20)
        q = min(1.0, (t - C["s16.b"]) / 3)
        carga_em(c, lerp(400, 1500, q), y, 40, "+")
        E.foco(c, t, C["s16.b"] + 0.5, 0.4, lambda a: E.pilula(c, "v na direção de B: F = 0, segue reta", W / 2, 760, 50, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s16.c"], [("R = mv/qB:", "g", 56, BR), ("só com", "i", 60, CLARO), ("90°", "g", 56, BR)], W / 2, 930, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s18"]:
        folha_campo(c, t, C["s17.a"], 1050, 320, 5, 4, 160, False, 26, TINTA2)
        E.foco(c, t, C["s17.b"], 0.5, lambda a: (carga_em(c, 1000, 560, 46, "−", a), F.seta(c, 1050, 560, 1260, 560, VEL, a, 10),
                                                 E.escreve(c, "v", 1270, 530, 60, "g", VEL, a)))
        E.frase(c, t, C["s17.a"], [("elétron;", "g", 64, NEG), ("campo", "i", 66), ("entrando", "g", 64)], XE, 360, passo=0.12)
        E.frase(c, t, C["s17.c"], ps("para que lado vai a", "i", 60) + [("força?", "g", 60, COR)], XE, 520, passo=0.12)
        E.frase(c, t, C["s17.d"], [("v × 2:", "g", 64, VEL), ("e o raio?", "i", 66)], XE, 680, passo=0.12)
    else:
        E.relogio(c, t, C["s18.a"], cx=1460, cy=500, r=200)
        E.frase(c, t, C["s18"], [("elétron,", "g", 64, NEG), ("v", "g", 64, VEL), ("→,", "g", 64), ("B entrando", "g", 64)], XE, 420, passo=0.12)
        E.frase(c, t, C["s18"] + 0.2, [("força?", "g", 64, COR), ("e", "i", 66), ("v × 2?", "g", 64, VEL)], XE, 540, passo=0.12)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s20"]:
        ox, oy = 1150, 600
        folha_campo(c, t, C["s19"], 900, 300, 6, 4, 150, False, 22, TINTA2)
        carga_em(c, ox, oy, 46, "−")
        F.seta(c, ox + 50, oy, ox + 300, oy, VEL, ep(t, C["s19.a"], 0.4), 10, p=ep(t, C["s19.a"], 0.5))
        E.foco(c, t, C["s19.a"], 0.4, lambda a: E.pilula(c, "polegar: v", ox + 300, oy + 60, 40, "g", fundo=VEL, a=a))
        E.foco(c, t, C["s19.b"], 0.4, lambda a: E.pilula(c, "dedos: B entrando", 1560, 840, 40, "g", fundo=TINTA, a=a))
        if t >= C["s19.c"]:  # a palma (carga +) para cima, tracejada
            M.line(c, ox, oy - 50, ox, oy - 240, E.COR, ep(t, C["s19.c"], 0.4), 7, dash=E.TRACO)
            E.foco(c, t, C["s19.c"] + 0.2, 0.4, lambda a: E.pilula(c, "palma: para cima (se fosse +)", ox, oy - 290, 40, "g", fundo=TINTA2, a=a))
        F.vetor(c, t, C["s19.e"], (ox, oy + 50), (ox, oy + 280), "F", None, E.COR, 11, size=64, lado=-1)
        E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "elétron: costas da mão", XE + 300, 760, 50, "g", fundo=NEG, a=a))
        E.foco(c, t, C["s19.e"] + 0.3, 0.5, lambda a: E.pilula(c, "para baixo", XE + 200, 880, 60, "g", fundo=CERTO, a=a))
        E.frase(c, t, C["s19"], ps("polegar, dedos, palma", "i", 60), XE, 260, passo=0.12)
        return
    E.formula_em(c, t, C["s20.a"], "R = f{m · v}{q · B}", XE, 360, 130, "g", TINTA)
    E.foco(c, t, C["s20.b"], 0.4, lambda a: E.pilula(c, "v em cima", XE + 200, 520, 50, "g", fundo=VEL, a=a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.formula(c, "v × 2  →  R × 2", XE, 720, 100, "g", COR, a))
    E.foco(c, t, C["s20.d"], 0.5, lambda a: c.drawCircle(1450, 560, 140, M.paint(TINTA2, a, stroke=6)))
    E.foco(c, t, C["s20.d"] + 0.4, 0.5, lambda a: c.drawCircle(1450, 560, 280, M.paint(E.COR, a, stroke=8)))
    E.foco(c, t, C["s20.d"] + 0.6, 0.4, lambda a: E.pilula(c, "curva 2 vezes mais aberta", 1450, 920, 46, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s21.a", None), ("s21.b", [("sentido:", "g", 70), ("a mão do tapa", "i", 74)]), ("s21.c", [("força para o centro", "g", 70), ("dá o raio", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            if partes:
                E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
            else:
                E.formula_em(c, t, C[k] + 0.1, "F = q · v · B · sen θ", 400, y, 70, "g", TINTA)
        E.frase(c, t, C["s21.d"], ps("próxima aula: a força num", "i", 60, TINTA2) + [("fio", "g", 60, COR)], W / 2, 900, "center", 0.1)
        E.frase(c, t, C["s21.e"], ps("e o", "i", 60, TINTA2) + [("motor elétrico", "g", 60, COR)], W / 2, 990, "center", 0.1)
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.foco(c, t, C["s22.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s22.a"] + 0.2, 0.4))
    E.frase(c, t, C["s22.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, quando=b_quando, formula=b_formula, sentido=b_sentido, curva=b_curva,
              erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
