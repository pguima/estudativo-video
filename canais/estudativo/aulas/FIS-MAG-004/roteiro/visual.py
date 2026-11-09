"""Visual — Estudativo · FIS-MAG-004: força sobre um fio e motor elétrico. Linguagem visual do Magnetismo: veja o visual.py da
FIS-MAG-001. Corrente = setinhas laranja no fio (F.corrente) e a letra i; força = seta grossa laranja com F; campo B em tinta.
O motor é desenhado em corte: polos N (laranja) e S (azul) dos lados, a espira de lado como um segmento com o símbolo da corrente
saindo/entrando em cada ponta. Todo instante vem de C[...]."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Magnetismo")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-MAG-004_forca_sobre_um_fio_e_motor_eletrico.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("fio", "exemplo", "motor", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
NEG = F.NEG
VEL = F.VEL
PELE, PELE2 = "#F4D3B8", "#E2B48F"

# todas as contas da aula
assert math.isclose(0.5 * 4 * 0.2, 0.4) and math.isclose(0.5 * 4, 2) and math.isclose(0.5 * 4 * 0.2 * math.sin(math.radians(30)), 0.2)
assert math.isclose(0.3 * 2 * 0.5, 0.3) and math.isclose(0.3 * 2, 0.6)
assert 20 / 100 == 0.2 and 50 / 100 == 0.5 and 10 / 100 == 0.1
cruz = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
# questão: corrente +x, campo entrando (−z) → força +y (para cima)
assert cruz((1, 0, 0), (0, 0, -1)) == (0, 1, 0)
# motor em corte: campo +x (do N à esquerda para o S à direita); corrente saindo (+z) → força +y; entrando (−z) → −y
assert cruz((0, 0, 1), (1, 0, 0)) == (0, 1, 0) and cruz((0, 0, -1), (1, 0, 0)) == (0, -1, 0)


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
    """ponto no círculo = saindo da folha; xis no círculo = entrando"""
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


def mao(c, cx, cy, s, a=1.0):
    """mão direita aberta, palma para quem olha, dedos para cima e polegar para a direita"""
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
    c.save(); c.translate(cx, cy)
    c.drawPath(forma, M.paint(PELE, a))
    for dx in (-0.25, 0.0, 0.25):
        M.line(c, dx * s, -0.42 * s, dx * s, -0.3 * s, PELE2, a, 4)
    pt = M.paint(TINTA, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(forma, pt)
    c.restore()


def mao_regra(c, t, cx, cy, s, t_pol, t_ded, t_pal, rot=("i", "B", "F"), cor_pol=None):
    """a mão do tapa com as três pílulas, cada uma no seu instante"""
    cp = cor_pol or E.COR
    E.foco(c, t, t_pol - 0.6, 0.5, lambda a: mao(c, cx, cy, s, a))
    E.foco(c, t, t_pol, 0.4, lambda a: (F.seta(c, cx + 0.95 * s, cy - 0.12 * s, cx + 1.55 * s, cy - 0.12 * s, cp, a, 10),
                                        E.pilula(c, f"polegar: {rot[0]}", cx + 1.55 * s, cy + 0.15 * s, 40, "g", fundo=cp, a=a)))
    E.foco(c, t, t_ded, 0.4, lambda a: (F.seta(c, cx, cy - 1.1 * s, cx, cy - 1.55 * s, TINTA, a, 10),
                                        E.pilula(c, f"dedos: {rot[1]}", cx + 0.55 * s, cy - 1.45 * s, 40, "g", fundo=TINTA, a=a)))
    E.foco(c, t, t_pal, 0.4, lambda a: (simbolo_campo(c, cx, cy + 0.12 * s, 0.16 * s, True, a, E.COR),
                                        E.pilula(c, f"palma: {rot[2]} para você", cx, cy + 0.85 * s, 40, "g", fundo=E.COR, a=a)))


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
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "0,4 N" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def polos(c, cx, cy, gap, h, a=1.0, campo=True):
    """polo N à esquerda e S à direita, com o campo horizontal entre eles"""
    if a <= 0:
        return
    for lado, cor, s in ((-1, E.COR, "N"), (1, NEG, "S")):
        x0 = cx + lado * gap / 2 - (180 if lado < 0 else 0)
        M.rrect(c, x0, cy - h / 2, 180, h, 14, cor, a)
        E._meio(c, s, x0 + 90, cy, 80, "g", BR, a)
    if campo:
        for k in range(5):
            yy = cy - h * 0.4 + k * h * 0.2
            F.seta(c, cx - gap / 2 + 20, yy, cx + gap / 2 - 20, yy, TINTA2, a * 0.7, 4, 20)


def espira_corte(c, cx, cy, R, phi, a=1.0, comutador=True, forcas=1.0, inverte=False):
    """espira vista de lado: segmento girando (phi em graus); com comutador, a ponta da esquerda sempre tem corrente saindo"""
    if a <= 0:
        return
    g = math.radians(phi)
    P1 = (cx + R * math.cos(g), cy - R * math.sin(g))
    P2 = (cx - R * math.cos(g), cy + R * math.sin(g))
    M.line(c, *P1, *P2, TINTA, a, 8, dash=E.TRACO)
    c.drawCircle(cx, cy, 10, M.paint(TINTA, a))
    sai1 = (P1[0] <= cx + 1) if comutador else True
    if inverte:
        sai1 = not sai1
    for P, sai in ((P1, sai1), (P2, not sai1)):
        c.drawCircle(*P, 40, M.paint(BR, a))
        simbolo_campo(c, *P, 40, sai, a, E.COR)
        if forcas > 0:
            d = -1 if sai else 1
            F.seta(c, P[0], P[1] + d * 48, P[0], P[1] + d * 210, E.COR, a * forcas, 10)
    return P1, P2


# ---------------- gancho ----------------
def ventilador(c, cx, cy, r, ang, a=1.0):
    if a <= 0:
        return
    for k in range(3):
        g = ang + k * 120
        c.save(); c.translate(cx, cy); c.rotate(g)
        c.drawOval(skia.Rect.MakeXYWH(r * 0.1, -r * 0.22, r * 0.9, r * 0.44), M.paint(E.COR, a))
        c.restore()
    c.drawCircle(cx, cy, r * 0.16, M.paint(TINTA, a))
    c.drawCircle(cx, cy, r * 1.05, M.paint(TINTA2, a, stroke=4))
    M.line(c, cx, cy + r * 1.05, cx, cy + r * 1.8, TINTA, a, 10)
    M.rrect(c, cx - r * 0.6, cy + r * 1.8, r * 1.2, r * 0.18, 8, TINTA, a)


def liquidificador(c, cx, yb, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s * 0.5, yb - s * 0.45, s, s * 0.45, 14, TINTA, a)
    p = skia.Path()
    p.moveTo(cx - s * 0.42, yb - s * 0.45); p.lineTo(cx - s * 0.55, yb - s * 1.6); p.lineTo(cx + s * 0.55, yb - s * 1.6); p.lineTo(cx + s * 0.42, yb - s * 0.45); p.close()
    c.drawPath(p, M.paint("#BFE3F2", 0.7 * a))
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    M.rrect(c, cx - s * 0.62, yb - s * 1.72, s * 1.24, s * 0.14, 6, TINTA, a)
    c.drawCircle(cx, yb - s * 0.22, s * 0.1, M.paint(E.COR, a))


def b_gancho(c, t, C, b):
    if t < C["s02"]:
        if t < C["s01.d"]:
            E.foco(c, t, C["s01.a"], 0.5, lambda a: ventilador(c, 420, 480, 150, (t - C["s01.a"]) * 400, a))
            E.foco(c, t, C["s01.b"], 0.5, lambda a: liquidificador(c, 960, 800, 260, a))
            E.foco(c, t, C["s01.c"], 0.5, lambda a: F.carrinho(c, 1520, 800, 420, a=a))
            for x, s, k in ((420, "ventilador", "s01.a"), (960, "liquidificador", "s01.b"), (1520, "carro elétrico", "s01.c")):
                E.foco(c, t, C[k] + 0.3, 0.4, lambda a, x=x, s=s: centro(c, s, x, 930, 52, "i", TINTA2, a))
            E.frase(c, t, C["s01.c"] + 0.8, ps("o mesmo", "i", 84) + [("motivo", "g", 84, COR)], W / 2, 200, "center", 0.12)
            return
        cx, cy = 1350, 560
        E.foco(c, t, C["s01.d"], 0.5, lambda a: polos(c, cx, cy, 640, 500, a))
        y = cy - 50 * ease_out(prog(t, C["s01.d"] + 1.6, 1.0))

        E.foco(c, t, C["s01.d"] + 0.4, 0.4, lambda a: simbolo_campo(c, cx, y, 54, True, a, E.COR))
        E.foco(c, t, C["s01.d"] + 1.2, 0.4, lambda a: F.seta(c, cx, y - 64, cx, y - 260, E.COR, a, 12))
        E.foco(c, t, C["s01.d"] + 1.3, 0.4, lambda a: E.escreve(c, "F", cx + 30, y - 200, 70, "g", COR, a))
        E.frase(c, t, C["s01.d"], ps("fio com corrente", "i", 64), XE, 260, passo=0.12)
        E.frase(c, t, C["s01.d"] + 0.8, ps("no campo:", "i", 64) + [("empurrado", "g", 64, COR)], XE, 360, passo=0.12)
        E.foco(c, t, C["s01.d"] + 0.6, 0.4, lambda a: E.escreve(c, "corrente saindo da folha", XE, 940, 44, "i", TINTA2, a))
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1480, 540, 330 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate((("s02.a", "a força no fio"), ("s02.b", "como o motor gira"))):
        y = 470 + i * 170
        dt = 1.2 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    def carga(a, x, y):
        E.formula(c, "F = q · v · B · sen θ", x - 60, y + 20, 46, "g", TINTA, a, "center")

    def corr(a, x, y):
        E.formula(c, "i = f{Q}{Δt}", x - 30, y + 30, 70, "g", TINTA, a, "center")
    lembrete2(c, t, C, "s03", (("s03.b", "carga andando no campo:", "F e a mão"), ("s03.c", "corrente:", "carga andando (A)")), (carga, corr))


# ---------------- a força no fio ----------------
def b_fio(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("fio com corrente:", "i", 70) + [("cargas andando", "g", 70, COR)], XE, 220, passo=0.12)
        folha_campo(c, t, C["s04.b"] - 0.4, 360, 430, 9, 4, 160, False, 22, TINTA2)
        dy = -70 * ease_out(prog(t, C["s04.c"], 0.8))
        y = 670 + dy
        if t >= C["s04.a"]:
            M.line(c, 200, y, 1720, y, TINTA, ep(t, C["s04.a"], 0.4), 30)
            for k in range(7):
                x = 260 + ((t - C["s04.a"]) * 120 + k * 220) % 1460
                c.drawCircle(x, y, 16, M.paint(E.COR, ep(t, C["s04.a"], 0.4)))
                E._meio(c, "+", x, y, 26, "g", BR, ep(t, C["s04.a"], 0.4))
                if t >= C["s04.b"]:
                    F.seta(c, x, y - 22, x, y - 100, E.COR, ep(t, C["s04.b"], 0.4), 6, 18)
        E.foco(c, t, C["s04.b"] + 0.4, 0.4, lambda a: E.pilula(c, "campo entrando", 1580, 380, 44, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s04.c"], 0.5, lambda a: E.pilula(c, "o fio inteiro é empurrado", W / 2, 960, 56, "g", fundo=E.COR, a=a))
        return
    if t < C["s06"]:
        F.formula_legenda(c, t, C["s05.a"], "F = B · i · L · sen θ", [("B", "campo", "T"), ("i", "corrente", "A"), ("L", "fio dentro do campo", "m"),
                                                                      ("θ", "ângulo entre o fio e B", None)],
                          XE, 330, 140, tl=[C["s05.b"], C["s05.c"], C["s05.d"], C["s05.e"]])
        cx, cy = 1450, 780
        if t >= C["s05.d"]:
            E.foco(c, t, C["s05.d"], 0.4, lambda a: (M.rrect(c, cx - 170, cy - 160, 340, 320, 20, "#E9E3D6", a), centro(c, "campo", cx, cy + 210, 44, "i", TINTA2, a)))
            M.line(c, cx - 330, cy, cx + 330, cy, TINTA, ep(t, C["s05.d"] + 0.2, 0.4), 8)
            E.foco(c, t, C["s05.d"] + 0.5, 0.4, lambda a: (E.chave(c, cx - 170, cx + 170, cy - 40, E.COR, 1, -22), centro(c, "L", cx, cy - 90, 60, "g", COR, a)))
        return
    E.frase(c, t, C["s06.a"], ps("a mesma", "i", 80) + [("mão do tapa", "g", 80, COR)], XE, 220, passo=0.12)
    mao_regra(c, t, 1150, 640, 250, C["s06.b"], C["s06.c"], C["s06.d"])


# ---------------- exemplo ----------------
def b_exemplo(c, t, C, b):
    if t < C["s08"]:
        dados = ("B = 0,5 T", "i = 4 A", "L = 20 cm", "θ = 90°")
        for i, s in enumerate(dados):
            E.foco(c, t, C["s07.a"] + 0.9 * i, 0.4, lambda a, s=s, i=i: E.formula(c, s, XE + i * 420, 230, 66, "g", TINTA, a))
        E.foco(c, t, C["s07.b"], 0.5, lambda a: E.formula(c, "20 cm = 0,2 m", XE + 840, 340, 60, "g", COR, a))
        troca(c, t, [(C["s07.c"] - 0.4, "F = 0,5 · 4 · 0,2"), (lerp(C["s07.c"], C["s07.d"], 0.55), "F = 2 · 0,2")],
              lambda s, a: E.formula(c, s, XE, 600, 110, "g", TINTA, a))
        bola_txt(c, t, C["s07.d"], "0,4 N", 1450, 580, 170, 90)
        return
    E.frase(c, t, C["s08.a"], ps("fio inclinado:", "i", 70) + [("30°", "g", 70, COR)], XE, 220, passo=0.12)
    cx, cy = 1350, 560
    for k in range(4):
        F.seta(c, cx - 380, cy - 180 + k * 120, cx + 380, cy - 180 + k * 120, TINTA2, 0.6, 4, 20)
    E.foco(c, t, C["s08.a"] + 0.3, 0.4, lambda a: E.escreve(c, "B", cx + 400, cy - 190, 60, "g", TINTA, a))
    g = math.radians(30 * ease_io(prog(t, C["s08.a"], 0.8)) if t < C["s08.d"] else 30 * (1 - ease_io(prog(t, C["s08.d"], 0.8))))
    M.line(c, cx - 300 * math.cos(g), cy + 300 * math.sin(g), cx + 300 * math.cos(g), cy - 300 * math.sin(g), TINTA, 1, 9)
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.formula(c, "× sen 30° = × f{1}{2}", XE, 450, 80, "g", TINTA2, a))
    E.foco(c, t, C["s08.c"], 0.5, lambda a: E.formula(c, "F = 0,2 N", XE, 640, 110, "g", COR, a))
    E.foco(c, t, C["s08.d"] + 0.6, 0.5, lambda a: E.pilula(c, "fio na direção de B: F = 0", XE + 330, 860, 50, "g", fundo=TINTA, a=a))


# ---------------- motor ----------------
def b_motor(c, t, C, b):
    cx, cy, R = 1360, 600, 210
    if t < C["s12"]:
        E.foco(c, t, C["s09.a"], 0.5, lambda a: polos(c, cx, cy, 640, 560, a))
        if t < C["s10.d"]:
            phi = 180
        elif t < C["s11.a"]:
            phi = 180 - 70 * (t - C["s10.d"])  # gira no sentido horário
            phi = max(phi, 180 - 175)
        elif t < C["s11.b"]:
            phi = 0  # meia volta depois, sem comutador
        else:
            phi = 0 - 90 * max(0.0, t - C["s11.c"])
        sem_com = C["s11.a"] <= t < C["s11.c"]
        forcas = ep(t, C["s10.a"], 0.4)
        if t >= C["s09.a"] + 0.4:
            espira_corte(c, cx, cy, R, phi, ep(t, C["s09.a"] + 0.4, 0.4), comutador=not sem_com, forcas=forcas)
        E.frase(c, t, C["s09"], ps("o", "i", 90) + [("motor", "g", 90, COR)], XE, 200)
        if t < C["s11"]:
            E.frase(c, t, C["s09.b"], [("saindo", "g", 56, COR), ("num lado,", "i", 60)], XE, 340, passo=0.12)
            E.frase(c, t, C["s09.c"], [("entrando", "g", 56, COR), ("no outro", "i", 60)], XE, 430, passo=0.12)
            E.frase(c, t, C["s10.a"], [("correntes opostas,", "i", 60)], XE, 560, passo=0.12)
            E.frase(c, t, C["s10.a"] + 0.4, [("forças opostas", "g", 60, COR)], XE, 650, passo=0.12)
            E.foco(c, t, C["s10.d"], 0.5, lambda a: E.pilula(c, "a espira gira", XE + 180, 800, 56, "g", fundo=E.COR, a=a))
            return
        E.frase(c, t, C["s11"], ps("depois de meia volta...", "i", 60), XE, 340, passo=0.12)
        E.foco(c, t, C["s11.a"], 0.5, lambda a: E.pilula(c, "giraria para trás", XE + 200, 460, 50, "g", fundo=ERRADO, a=a))
        E.frase(c, t, C["s11.b"], [("comutador:", "g", 60, COR), ("anel partido", "i", 64)], XE, 600, passo=0.12)
        E.frase(c, t, C["s11.c"], ps("inverte a corrente", "i", 60), XE, 700, passo=0.12)
        E.foco(c, t, C["s11.d"], 0.5, lambda a: E.pilula(c, "sempre no mesmo sentido", XE + 270, 830, 50, "g", fundo=CERTO, a=a))
        # o anel partido: duas metades e as escovas
        def anel(a):
            ax, ay, r = 640, 990, 60
            for k in (0, 180):
                c.drawArc(skia.Rect.MakeXYWH(ax - r, ay - r, 2 * r, 2 * r), k + 10 + phi, 160, False, M.paint(E.COR if k else NEG, a, stroke=16))
            for d in (-1, 1):
                M.rrect(c, ax + d * (r + 14) - (24 if d < 0 else 0), ay - 14, 24, 28, 4, TINTA, a)
        E.foco(c, t, C["s11.b"] + 0.4, 0.5, anel)
        return
    # muitas voltas
    E.frase(c, t, C["s12.a"], ps("centenas de", "i", 80) + [("voltas de fio", "g", 80, COR)], XE, 220, passo=0.12)
    bx, by = 1400, 620
    E.foco(c, t, C["s12.a"] + 0.3, 0.5, lambda a: polos(c, bx, by, 640, 560, a, False))
    for k in range(9):
        E.foco(c, t, C["s12.a"] + 0.4 + 0.08 * k, 0.4, lambda a, k=k: c.drawOval(skia.Rect.MakeXYWH(bx - 230 + k * 6, by - 200 + k * 4, 460, 400), M.paint(E.COR if k % 2 else TINTA, a, stroke=5)))
    E.frase(c, t, C["s12.b"], ps("a força", "i", 64) + [("soma", "g", 64, COR)], XE, 400, passo=0.12)
    E.foco(c, t, C["s12.c"], 0.5, lambda a: (E.pilula(c, "elétrica", XE + 170, 580, 56, "g", fundo=TINTA, a=a),
                                             F.seta(c, XE + 170, 630, XE + 170, 730, TINTA2, a, 8),
                                             E.pilula(c, "movimento", XE + 170, 800, 56, "g", fundo=E.COR, a=a)))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s13"], [("cuidado", "g", 96, ERRADO)], XE, 200)
    E.frase(c, t, C["s13.a"], ps("usar o", "i", 64) + [("fio inteiro", "g", 64, ERRADO)], XE, 320, passo=0.12)
    y = 640
    if t >= C["s13.b"]:
        E.foco(c, t, C["s13.b"], 0.5, lambda a: (M.rrect(c, 1300, 420, 220, 440, 16, "#E9E3D6", a)))
        folha_campo(c, t, C["s13.b"] + 0.2, 1340, 480, 2, 3, 140, False, 20, TINTA2)
        M.line(c, 200, y, 1740, y, TINTA, ep(t, C["s13.b"], 0.5), 9)
        E.foco(c, t, C["s13.b"] + 0.6, 0.4, lambda a: (E.segmento(c, 99, 0, (200, y + 120), (1740, y + 120), "2 m", cor=TINTA2, largura=4)))
        E.foco(c, t, C["s13.b"] + 1.0, 0.4, lambda a: (E.chave(c, 1300, 1520, y - 230, E.COR, 1, -22), centro(c, "10 cm", 1410, y - 270, 54, "g", COR, a)))
    E.foco(c, t, C["s13.c"], 0.5, lambda a: E.pilula(c, "fora do campo: sem força", 480, 900, 46, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s13.d"], 0.5, lambda a: E.pilula(c, "L = 0,1 m", 1450, 900, 70, "g", fundo=CERTO, a=a))


# ---------------- atalho ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s15"]:
        E.frase(c, t, C["s14"], ps("agora, o atalho", "i", 76, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s14.a"], ps("não decore", "i", 64, CLARO) + [("duas fórmulas", "g", 64, BR)], W / 2, 290, "center", 0.12)
        E.formula_em(c, t, C["s14.b"], "i = f{q}{Δt}", 520, 520, 100, "g", BR, "center")
        E.formula_em(c, t, C["s14.c"], "L = v · Δt", 1400, 520, 100, "g", BR, "center")
        E.formula_em(c, t, C["s14.d"], "i · L = f{q}{Δt} · v · Δt", W / 2, 760, 100, "g", CLARO, "center")
        if t >= C["s14.d"] + 0.8:
            w = E.formula(None, "i · L = f{q}{Δt} · v · Δt", 0, 0, 100, a=0)
            x0 = W / 2 - w / 2
            xq = x0 + E.formula(None, "i · L = ", 0, 0, 100, a=0)
            E.risco(c, xq + 2, 820, xq + 80, 770, t, C["s14.d"] + 0.8, E.COR, 8)
            xt = x0 + w - E.formula(None, "Δt", 0, 0, 100, a=0)
            E.risco(c, xt, 790, xt + 100, 700, t, C["s14.d"] + 1.0, E.COR, 8)
        E.foco(c, t, C["s14.e"], 0.5, lambda a: E.pilula(c, "i · L = q · v", W / 2, 940, 70, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s15.a"], ps("troque", "i", 70, CLARO) + [("q · v", "g", 66, BR)] + ps("por", "i", 70, CLARO) + [("i · L", "g", 66, BR)], W / 2, 220, "center", 0.12)
    E.formula_em(c, t, C["s15.b"], "F = q · v · B", 560, 480, 110, "g", BR, "center")
    E.foco(c, t, C["s15.b"] + 0.6, 0.4, lambda a: F.seta(c, 860, 450, 1060, 450, E.CLARO, a, 9))
    E.formula_em(c, t, C["s15.b"] + 1.0, "F = B · i · L", 1360, 480, 110, "g", CLARO, "center")
    E.frase(c, t, C["s15.c"], ps("mesma mão:", "i", 60, CLARO) + [("polegar na corrente", "g", 58, BR)], W / 2, 700, "center", 0.12)
    E.frase(c, t, C["s15.d"], ps("cargas soltas, sem fio:", "i", 56, CLARO) + [("F = q · v · B", "g", 54, BR)], W / 2, 900, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s16"], ps("hora de testar", "i", 72, COR), XE, 180)
    if t < C["s17"]:
        folha_campo(c, t, C["s16.b"], 960, 340, 6, 4, 150, False, 22, TINTA2)
        y = 565
        if t >= C["s16.a"]:
            M.line(c, 900, y, 1820, y, TINTA, ep(t, C["s16.a"], 0.4), 9)
        if t >= C["s16.c"]:
            F.corrente(c, t, C["s16.c"], [(900, y), (1820, y)], fecha=False)
            E.foco(c, t, C["s16.c"] + 0.3, 0.4, lambda a: E.escreve(c, "i", 1840, y - 25, 64, "g", COR, a))
        E.frase(c, t, C["s16.a"], [("L = 50 cm,", "g", 64)], XE, 300)
        E.frase(c, t, C["s16.a"] + 0.8, [("B = 0,3 T", "g", 64)], XE + 400, 300)
        E.frase(c, t, C["s16.b"], ps("campo", "i", 64) + [("entrando", "g", 64)], XE, 480, passo=0.12)
        E.frase(c, t, C["s16.c"], [("2 A", "g", 64, COR), ("para a direita", "i", 66)], XE, 600, passo=0.12)
        E.frase(c, t, C["s16.d"], [("F = ?", "g", 70, COR), ("e o sentido?", "i", 70)], XE, 760, passo=0.12)
    else:
        E.relogio(c, t, C["s17.a"], cx=1460, cy=500, r=200)
        E.frase(c, t, C["s17"], [("L = 50 cm,", "g", 60), ("B = 0,3 T,", "g", 60)], XE, 420, passo=0.12)
        E.frase(c, t, C["s17"] + 0.2, [("i = 2 A", "g", 60, COR), ("→", "g", 60)], XE, 520, passo=0.12)
        E.frase(c, t, C["s17"] + 0.4, [("F = ?", "g", 60, COR), ("sentido?", "g", 60)], XE, 620, passo=0.12)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s19"]:
        E.foco(c, t, C["s18.a"], 0.5, lambda a: E.formula(c, "L = 50 cm = 0,5 m", XE, 250, 70, "g", TINTA, a))
        E.foco(c, t, C["s18.b"], 0.5, lambda a: E.formula(c, "θ = 90°,  sen θ = 1", XE, 380, 70, "g", TINTA, a))
        troca(c, t, [(C["s18.c"] - 0.3, "F = 0,3 · 2 · 0,5"), (lerp(C["s18.c"], C["s18.d"], 0.55), "F = 0,6 · 0,5")],
              lambda s, a: E.formula(c, s, XE, 620, 110, "g", TINTA, a))
        bola_txt(c, t, C["s18.d"], "0,3 N", 1450, 560, 170, 90)
        return
    folha_campo(c, t, C["s19"] - 0.4, 960, 380, 7, 4, 150, False, 22, TINTA2, d=0.0)
    y = 605
    M.line(c, 900, y, 1860, y, TINTA, 1, 9)
    F.corrente(c, t, C["s19"], [(900, y), (1860, y)], fecha=False)
    E.foco(c, t, C["s19.a"], 0.4, lambda a: E.pilula(c, "polegar: corrente", 1640, 755, 40, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.pilula(c, "dedos: B entrando", 1640, 300, 40, "g", fundo=TINTA, a=a))
    F.vetor(c, t, C["s19.c"], (1335, y - 20), (1335, y - 300), "F", "0,3 N", E.COR, 12, size=60)
    E.frase(c, t, C["s19.c"], ps("palma virada", "i", 64) + [("para cima", "g", 64, COR)], XE, 260, passo=0.12)
    E.foco(c, t, C["s19.d"], 0.5, lambda a: E.pilula(c, "a força aponta para cima", XE + 320, 900, 56, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", None), ("s20.b", [("só conta", "i", 74), ("o fio dentro do campo", "g", 70)]),
                 ("s20.c", [("forças opostas:", "g", 70), ("o motor gira", "i", 74)]))
        for i, (k, partes) in enumerate(itens):
            y = 360 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            if partes:
                E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
            else:
                E.formula_em(c, t, C[k] + 0.1, "F = B · i · L · sen θ", 400, y, 70, "g", TINTA)
        E.frase(c, t, C["s20.d"], ps("próxima aula: movimento e campo", "i", 60, TINTA2) + [("gerando corrente", "g", 60, COR)], W / 2, 920, "center", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.foco(c, t, C["s21.a"], 0.5, lambda a: E.pilula(c, "Inscreva-se", W / 2, 460, 90, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.a"] + 0.3, 0.8))
    E.cursor(c, lerp(1300, 1080, p), lerp(800, 490, p), ep(t, C["s21.a"] + 0.2, 0.4))
    E.frase(c, t, C["s21.b"], [("bons", "i", 110), ("estudos!", "i", 110, COR)], W / 2, 760, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, fio=b_fio, exemplo=b_exemplo, motor=b_motor, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
