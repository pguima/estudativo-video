"""Visual — Estudativo · FIS-EGF-011: princípio de Bernoulli.

Segue a linguagem visual da Física (visual.py da FIS-CIN-001) e a da trilha Equilíbrio, Gravitação e Fluidos (cabeçalho do
visual.py da FIS-EGF-001): eixo e braço em cota, giro horário laranja e anti-horário azul, astros (Sol âmbar, Terra azul),
fluidos em azul translúcido, pressão em setinhas laranja, empuxo azul. O kit da trilha vem copiado logo abaixo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Equilíbrio, Gravitação e Fluidos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-EGF-011_principio_de_bernoulli.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "asa", "tanque", "atalho", "questao", "fim"))

# todas as contas da aula
assert 1000 * (3 ** 2 - 1 ** 2) / 2 == 4000 and math.isqrt(2 * 10 * 5) == 10  # cano deitado; furo a 5 m
assert abs((20 * 0.8) ** 0.5 - 4) < 1e-9 and abs((20 * 1.8) ** 0.5 - 6) < 1e-9  # atalho 0,8 m; questão 1,8 m


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- kit da trilha (o mesmo em todas as aulas FIS-EGF) ----------------
BR = "#FFFFFF"
MADEIRA, MADEIRA2 = "#B07A4A", "#7E5432"
AGUA, AGUA2, OLEO = "#5AB4E6", "#2C86C2", "#E9B44C"
SOL, TERRA, LUA = "#FFB020", "#2F6FB0", "#A9A9B4"


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera: "20 m/s" com a unidade menor"""
    v, _, u = s.partition(" ")
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     F.medida(c, v, u, cx, cy + size * 0.36, size, E.SOBRE, a, "center", cor_u=E.SOBRE)))


def troca(c, t, itens, fn):
    """um de cada vez: itens = [(instante, arg)], cada um sai quando o próximo chega; fn(arg, a) desenha"""
    for i, (ti, s) in enumerate(itens):
        fim = itens[i + 1][0] - 0.1 if i + 1 < len(itens) else 1e9
        if t >= ti - 0.01:
            E.saida(c, t, fim, lambda s=s, ti=ti: E.foco(c, t, ti, 0.45, lambda a: fn(s, a)), d=0.25)


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def linhas(c, t, itens, x, y0, dy, size=72, align="left", est="g"):
    """passo a passo: itens = [(instante, "fórmula", cor)], uma linha por etapa, de cima para baixo"""
    for i, it in enumerate(itens):
        t0, s, cor = it[0], it[1], (it[2] if len(it) > 2 else TINTA)
        E.formula_em(c, t, t0, s, x, y0 + i * dy, size, est, cor, align)


def cota(c, t, t0, A, B, rot, cor=TINTA2, size=46, lado=-1, d=0.5, cor_txt=None):
    """linha de medida de A até B, com tracinhos nas pontas e o rótulo no meio, do lado `lado` (−1 = acima/esquerda)"""
    q = ep(t, t0, d)
    if q <= 0:
        return
    ux, uy = E._uni(*A, *B)
    nx, ny = -uy, ux
    M.line(c, *A, lerp(A[0], B[0], q), lerp(A[1], B[1], q), cor, 1.0, 4)
    for P_ in (A, B):
        M.line(c, P_[0] - nx * 16, P_[1] - ny * 16, P_[0] + nx * 16, P_[1] + ny * 16, cor, q, 4)
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    E.foco(c, t, t0 + d * 0.6, 0.4, lambda a: E._meio(c, rot, mx + nx * lado * (size * 0.8), my + ny * lado * (size * 0.8), size, "b", cor_txt or E.COR_TEXTO, a))


def seta_giro(c, cx, cy, r, ini, varre, cor, a=1.0, largura=9, p=1.0):
    """arco com ponta de seta: o sentido do giro. ini e varre em graus de tela (varre > 0 = horário)"""
    if a <= 0 or p <= 0:
        return
    v = varre * p
    E.arco(c, cx, cy, r, ini, v, cor, largura, a)
    g = math.radians(ini + v)
    x, y = cx + r * math.cos(g), cy + r * math.sin(g)
    s = 1 if v > 0 else -1
    ux, uy = -math.sin(g) * s, math.cos(g) * s
    F._cabeca(c, x + ux * largura * 1.6, y + uy * largura * 1.6, ux, uy, largura * 3.2, cor, a)


def apoio(c, x, y, s=70, a=1.0, escuro=False):
    """apoio triangular com o vértice (o eixo) em (x, y)"""
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x, y); p.lineTo(x - s * 0.7, y + s); p.lineTo(x + s * 0.7, y + s); p.close()
    c.drawPath(p, M.paint(BR if escuro else TINTA, a))
    c.drawCircle(x, y, s * 0.13, M.paint(E.COR, a))


def lembrete(c, t, C, cena, itens, numero, palavra="coisas"):
    """o que precisa saber: itens = [(cue, linha fina, linha forte)], uma caixa por item"""
    n = len(itens)
    E.frase(c, t, C[cena] + 0.2, ps("você precisa de" if palavra == "coisas" else "você vai usar", "i", 80), XE, 410, passo=0.14)
    t1 = C.get(cena + ".a", C[cena] + 0.6) if hasattr(C, "get") else C[cena] + 0.6
    E.foco(c, t, t1, 0.5, lambda a: E.escreve(c, str(numero), XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, t1 + 0.15, 0.5, lambda a: E.escreve(c, palavra, XE + 215, 700, 110 if palavra == "coisas" else 84, "i", TINTA, a))
    x, w = 820, 1000
    h = {2: 230, 3: 190, 4: 150}[n]
    gap = {2: 290, 3: 230, 4: 180}[n]
    y0 = {2: 230, 3: 150, 4: 140}[n]
    s1, s2 = {2: (58, 58), 3: (50, 52), 4: (44, 46)}[n]
    for i, (k, l1, l2) in enumerate(itens):
        y = y0 + i * gap
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, h, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(l1, "i", s1)], x + 44, y + h * 0.4)
        E.frase(c, t, C[k] + 0.3, [(l2, "g", s2, COR)], x + 44, y + h * 0.4 + s2 * 1.3)
    E.frase(c, t, lerp(C[itens[-1][0]], C[cena + ".end"], 0.6), ps("faltou alguma?", "i", 50, COR) + ps("procure no canal", "i", 50), 820, 1010, "left", 0.12)


def promessa(c, t, C, cena, itens):
    """até o fim da aula: itens = [(cue, texto)] numerados, com a órbita à direita"""
    tb = C[itens[0][0]] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1500, 560, 300 * ease_back(prog(t, tb, 0.8)), giro=12 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C[cena], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    for i, (k, s) in enumerate(itens):
        y = 450 + i * 160
        dt = 1.2 if i == 0 else 0
        E.foco(c, t, C[k] + dt, 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 30, 38, a=a), centro(c, str(i + 1), XE + 40, y - 8, 48, "g", BR, a)))
        E.frase(c, t, C[k] + dt + 0.1, [(s, "g", 80, COR if i == 0 else TINTA)], XE + 110, y)


def resumo(c, t, C, cena, itens):
    """itens = [(cue, partes de E.frase)]"""
    E.frase(c, t, C[cena], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
    for i, (k, partes) in enumerate(itens):
        y = 360 + i * 200
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 26, 52, a=a), centro(c, str(i + 1), 230, y - 4, 60, "g", BR, a)))
        E.frase(c, t, C[k] + 0.1, partes, 330, y, passo=0.1)


def proxima(c, t, C, cena, l1, l2, desenho=None, k=("a", "c", "d")):
    """próxima aula + inscreva-se + bons estudos; desenho(a) ilustra a próxima aula na metade de baixo"""
    E.frase(c, t, C[cena], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C[f"{cena}.{k[0]}"], l1, XE, 400)
    if l2:
        E.frase(c, t, C[f"{cena}.{k[0]}"] + 0.5, l2, XE, 540)
    if desenho:
        desenho()
    E.foco(c, t, C[f"{cena}.{k[1]}"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C[f"{cena}.{k[1]}"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C[f"{cena}.{k[1]}"] + 0.2, 0.4))
    E.frase(c, t, C[f"{cena}.{k[2]}"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1570, 990, "center")


def hora_testar(c, t, C, cena):
    E.frase(c, t, C[cena], ps("hora de testar", "i", 72, COR), XE, 180)




def empurra(c, t, t0, P, ang, comp, rot=None, modulo=None, cor=None):
    """força que CHEGA ao ponto P vindo da direção oposta a ang (graus da Física): a ponta encosta no corpo"""
    dx, dy = F._dir(ang)
    F.vetor(c, t, t0, (P[0] - dx * comp, P[1] - dy * comp), P, rot, modulo, cor, 10, em=0.4)


# ---------------- peças desta aula (cano e fluxo copiados da FIS-EGF-010) ----------------
def cano(c, x0, x1, xm, y, h1, h2, a=1.0, cor=AGUA, trans=60):
    def meia(x):
        if x <= xm - trans / 2:
            return h1 / 2
        if x >= xm + trans / 2:
            return h2 / 2
        return lerp(h1 / 2, h2 / 2, ease_io((x - xm + trans / 2) / trans))
    if a <= 0:
        return meia
    n = 60
    xs = [lerp(x0, x1, i / n) for i in range(n + 1)]
    top = [(x, y - meia(x)) for x in xs]
    bot = [(x, y + meia(x)) for x in reversed(xs)]
    p = skia.Path(); p.addPoly(top + bot, True)
    c.drawPath(p, M.paint(cor, 0.5 * a))
    for pts in (top, bot):
        pp = skia.Path(); pp.addPoly(pts, False)
        c.drawPath(pp, M.paint(TINTA, a, stroke=6))
    return meia


def fluxo(c, t, t0, x0, x1, xm, y, h1, h2, v1, a=1.0, n_lin=3, esp=150):
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    v2 = v1 * h1 / h2
    for j in range(n_lin):
        fy = (j + 0.5) / n_lin - 0.5
        for xa, xb, v, hh in ((x0, xm, v1, h1), (xm, x1, v2, h2)):
            passo = esp * (v / v1)
            off = ((t - t0) * v) % passo
            x = xa + off - passo
            while x < xb:
                if x >= xa + 10 and x + 40 <= xb:
                    yy = y + fy * hh * 0.8
                    F.seta(c, x, yy, x + 22 + 18 * (v / v1), yy, F.VEL, q, 5, cabeca=14)
                x += passo


def manometro(c, x, y_cano, nivel, a=1.0):
    """tubinho vertical em cima do cano: a altura da água mostra a pressão ali"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x - 18, y_cano - nivel, x + 18, y_cano), M.paint(AGUA, 0.6 * a))
    M.line(c, x - 18, y_cano - 330, x - 18, y_cano, TINTA, a, 4)
    M.line(c, x + 18, y_cano - 330, x + 18, y_cano, TINTA, a, 4)
    M.line(c, x - 18, y_cano - nivel, x + 18, y_cano - nivel, AGUA2, a, 4)


def asa(c, cx, cy, s, a=1.0, ang=-6):
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    p = skia.Path()
    p.moveTo(-s, 0); p.cubicTo(-s * 0.7, -s * 0.32, s * 0.3, -s * 0.3, s, 0)
    p.cubicTo(s * 0.3, s * 0.06, -s * 0.7, s * 0.12, -s, 0); p.close()
    c.drawPath(p, M.paint("#B9BCC4", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=4))
    c.restore()


def linhas_ar(c, t, t0, cx, cy, s, a=1.0):
    """linhas de corrente: por cima, mais juntas e com setas mais rápidas; por baixo, mais espaçadas"""
    q = ep(t, t0, 0.6) * a
    if q <= 0:
        return
    for k, (dy, vel) in enumerate(((-0.55, 420), (-0.42, 400), (0.35, 220), (0.6, 210))):
        y0 = cy + dy * s
        pts = []
        for i in range(41):
            x = lerp(cx - 1.5 * s, cx + 1.5 * s, i / 40)
            u = (x - cx) / s
            bump = (-0.3 if dy < 0 else 0.08) * s * math.exp(-u * u * 1.6)
            pts.append((x, y0 + bump * (1.3 if abs(dy) < 0.5 else 0.7)))
        F.poli(c, pts, q, TINTA2, 0.5 * q, 3)
        off = ((t - t0) * vel) % (3 * s)
        idx = int(clampi(off / (3 * s) * 40, 0, 39))
        x1, y1 = pts[idx]
        x2, y2 = pts[min(idx + 1, 40)]
        F.seta(c, x1, y1, x1 + (x2 - x1) * 3, y1 + (y2 - y1) * 3, F.VEL, q, 5, cabeca=16)


def clampi(v, lo, hi):
    return max(lo, min(hi, v))


def tanque_furo(c, t, t0, x, y, w, h, nivel, furo_y, jato=0.0, a=1.0):
    """tanque aberto; furo na parede direita na altura furo_y; jato horizontal que cai em parábola"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    ys = y + h - nivel
    c.drawRect(skia.Rect.MakeLTRB(x, ys, x + w, y + h), M.paint(AGUA, 0.5 * q))
    M.line(c, x, ys, x + w, ys, AGUA2, q, 5)
    M.line(c, x, y, x, y + h, TINTA, q, 6)
    M.line(c, x, y + h, x + w, y + h, TINTA, q, 6)
    M.line(c, x + w, y, x + w, furo_y - 12, TINTA, q, 6)
    M.line(c, x + w, furo_y + 12, x + w, y + h, TINTA, q, 6)
    if jato > 0:
        pts = [(x + w + 340 * s, furo_y + 300 * s * s) for s in [i / 30 for i in range(31)]]
        F.poli(c, pts, jato, AGUA2, q, 16)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            q = ep(t, C["s01.a"], 0.5)
            sobe = 60 * ease_io(prog(t, C["s01.d"] + 0.5, 1.0))
            if q > 0:
                c.drawRect(skia.Rect.MakeLTRB(1100, 620, 1700, 960), M.paint("#EDE3D6", q))
                c.drawRect(skia.Rect.MakeLTRB(1100, 620, 1700, 960), M.paint(TINTA, q, stroke=5))
                p = skia.Path(); p.moveTo(1050, 630 - sobe); p.lineTo(1400, 430 - sobe); p.lineTo(1750, 630 - sobe); p.close()
                c.drawPath(p, M.paint("#B5533C", q))
                F.chao(c, 1000, 1800, 960, q)
            if t >= C["s01.b"]:
                for i in range(3):
                    y = 360 - i * 60
                    x = 900 + ((t - C["s01.b"]) * 500 + i * 220) % 900
                    F.seta(c, x, y, x + 160, y, F.VEL, ep(t, C["s01.b"], 0.4), 7, cabeca=20)
            F.forca(c, t, C["s01.d"], (1400, 800), 90, 230, None, lado=1)
            E.frase(c, t, C["s01.a"], ps("vendaval:", "i", 64) + [("o telhado voa", "g", 64, COR)], XE, 220, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("o vento sopra", "i", 60) + [("por cima", "g", 60, F.VEL)], XE, 330, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("quem empurra", "i", 64) + [("para cima?", "g", 64)], XE, 520, passo=0.12)
            E.frase(c, t, C["s01.d"], ps("o ar parado", "i", 64) + [("de dentro", "g", 64, COR)], XE, 640, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "velocidade e pressão"), ("s02.b", "a asa do avião"), ("s02.c", "o furo no tanque")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "continuidade:", "cano fino, água mais rápida"), ("s03.c", "Stevin:", "mais fundo, mais pressão"),
                              ("s03.d", "energia:", "cinética + potencial constante")), 3)


# ---------------- a ideia ----------------
CX0, CX1, CXM, CY, CH1, CH2 = 260, 1660, 960, 720, 220, 110


def b_ideia(c, t, C, b):
    if t < C["s05"]:
        def s04():
            q = ep(t, C["s04.a"], 0.5)
            cano(c, CX0, CX1, CXM, CY, CH1, CH2, q)
            fluxo(c, t, C["s04.a"], CX0, CX1, CXM, CY, CH1, CH2, 110, n_lin=3, esp=170)
            ql = ep(t, C["s04.d"], 0.6)
            manometro(c, 600, CY - CH1 / 2, 300 * ql + 1, q)
            manometro(c, 1320, CY - CH2 / 2, 150 * ql + 1, q)
            if t >= C["s04.c"]:
                F.seta(c, 800, CY, 920, CY, E.COR, ep(t, C["s04.c"], 0.4), 12)
            E.foco(c, t, C["s04.d"] + 0.4, 0.4, lambda a: (E.pilula(c, "pressão maior", 600, CY + CH1 / 2 + 60, 42, "g", fundo=E.COR, a=a),
                                                           E.pilula(c, "pressão menor", 1320, CY + CH2 / 2 + 60, 42, "g", fundo=TINTA, a=a)))
            E.frase(c, t, C["s04.a"], ps("cano fino:", "i", 62) + [("a água acelera", "g", 62, F.VEL)], XE, 190, passo=0.12)
            E.frase(c, t, C["s04.b"], ps("quem empurra?", "i", 62) + [("a pressão", "g", 62, COR)], XE + 820, 190, passo=0.12)
            E.frase(c, t, C["s04.e"], [("mais rápido,", "g", 66, F.VEL), ("menos pressão", "g", 66, COR)], W / 2, 1020, "center", 0.15)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s07"]:
        def s0506():
            E.frase(c, t, C["s05.a"], [("Daniel Bernoulli:", "g", 62, COR)] + ps("conservação da energia", "i", 62), XE, 200, passo=0.1)
            E.frase(c, t, C["s05.b"], ps("num fluido sem atrito, ao longo do tubo:", "i", 54, TINTA2), XE, 300, passo=0.08)
            E.formula_em(c, t, C["s05.c"], "p + f{d · v^2}{2} + d · g · h = constante", XE, 480, 96, "g", TINTA)
            if t >= C["s06"]:
                for k_, txt, cor, y in (("s06.a", "p: pressão (Pa)", COR, 660), ("s06.b", "d · v^2 / 2: energia cinética por volume", F.VEL, 770),
                                        ("s06.c", "d · g · h: energia potencial por volume", F.ACEL, 930)):
                    E.foco(c, t, C[k_], 0.5, lambda a, txt=txt, cor=cor, y=y: E.formula(c, txt, XE, y, 54, "b", cor, a))
                E.foco(c, t, C["s06.b"] + 1.8, 0.4, lambda a: E.formula(c, "(como m · v^2 / 2, com d no lugar de m)", XE + 40, 840, 42, "b", TINTA2, a))
                E.frase(c, t, C["s06.d"], ps("v: velocidade · h: altura", "i", 50, TINTA2), XE, 1030, passo=0.08)
        E.saida(c, t, C["s07"] - 0.1, s0506)
        return
    q = ep(t, C["s07"], 0.5)
    cano(c, CX0, CX1, CXM, CY + 60, CH1, CH2, q)
    fluxo(c, t, C["s07"], CX0, CX1, CXM, CY + 60, CH1, CH2, 110, n_lin=3, esp=170)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: (E.pilula(c, "1 m/s", 600, CY + 60 - CH1 / 2 - 50, 44, "g", fundo=F.VEL, a=a),
                                              E.pilula(c, "3 m/s", 1320, CY + 60 - CH2 / 2 - 50, 44, "g", fundo=F.VEL, a=a)))
    E.frase(c, t, C["s07.a"], [("cano deitado:", "g", 58)] + ps("o termo da altura é igual dos dois lados", "i", 56), XE, 190, passo=0.08)
    E.formula_em(c, t, C["s07.c"], "queda de p = f{d}{2} · (v₂^2 − v₁^2)", XE, 340, 76, "g", TINTA)
    E.formula_em(c, t, C["s07.d"], "= f{1.000}{2} · (9 − 1)", XE, 480, 76, "g", TINTA)
    bola_txt(c, t, C["s07.e"], "4.000 Pa", 1500, 400, 145, 50)


# ---------------- a asa e o telhado ----------------
def b_asa(c, t, C, b):
    if t < C["s09"]:
        def s08():
            cx, cy, s = 1250, 600, 380
            E.foco(c, t, C["s08.a"], 0.5, lambda a: asa(c, cx, cy, s, a))
            linhas_ar(c, t, C["s08.b"], cx, cy, s)
            E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "rápido: pressão menor", cx, cy - 300, 42, "g", fundo=F.VEL, a=a))
            E.foco(c, t, C["s08.c"] + 0.6, 0.4, lambda a: E.pilula(c, "devagar: pressão maior", cx, cy + 300, 42, "g", fundo=E.COR, a=a))
            F.forca(c, t, C["s08.d"], (cx, cy + 20), 90, 230, None, lado=1)
            E.frase(c, t, C["s08.a"], [("asa:", "g", 62)] + ps("curva e um pouco inclinada", "i", 60), XE, 190, passo=0.1)
            E.frase(c, t, C["s08.e"], [("sustentação", "g", 76, COR)], XE, 1000)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    q = ep(t, C["s09.a"], 0.5)
    if q > 0:
        c.drawRect(skia.Rect.MakeLTRB(1100, 640, 1700, 960), M.paint("#EDE3D6", q))
        c.drawRect(skia.Rect.MakeLTRB(1100, 640, 1700, 960), M.paint(TINTA, q, stroke=5))
        p = skia.Path(); p.moveTo(1050, 650); p.lineTo(1400, 450); p.lineTo(1750, 650); p.close()
        c.drawPath(p, M.paint("#B5533C", q))
        F.chao(c, 1000, 1800, 960, q)
    if t >= C["s09.b"]:
        for i in range(3):
            y = 380 - i * 60
            x = 900 + ((t - C["s09.b"]) * 500 + i * 220) % 900
            F.seta(c, x, y, x + 160, y, F.VEL, ep(t, C["s09.b"], 0.4), 7, cabeca=20)
    E.foco(c, t, C["s09.b"] + 0.4, 0.4, lambda a: E.pilula(c, "fora: pressão menor", 1400, 200, 42, "g", fundo=F.VEL, a=a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.pilula(c, "dentro: pressão normal", 1400, 820, 40, "g", fundo=E.COR, a=a))
    F.forca(c, t, C["s09.d"], (1400, 700), 90, 200, None, lado=1)
    E.frase(c, t, C["s09.a"], ps("o telhado é a", "i", 64) + [("mesma coisa", "g", 64, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s09.d"], ps("a diferença", "i", 60) + [("empurra para cima", "g", 60, COR)], XE, 900, passo=0.12)


# ---------------- o tanque ----------------
TX, TY, TW, TH = 1050, 260, 420, 640


def b_tanque(c, t, C, b):
    furo_y = TY + TH - 80
    nivel = TH - 60
    ys = TY + TH - nivel
    jato = ep(t, C["s10.a"] + 0.6, 1.0)
    tanque_furo(c, t, C["s10.a"], TX, TY, TW, TH, nivel, furo_y, jato)
    cota(c, t, C["s10.b"], (TX - 40, ys), (TX - 40, furo_y), "h", lado=1, size=60)
    if t >= C["s10.b"]:
        M.line(c, TX - 60, furo_y, TX + TW, furo_y, TINTA2, 0.6 * ep(t, C["s10.b"], 0.4), 3, dash=E.TRACO)
    if t < C["s11"]:
        E.foco(c, t, C["s10.c"], 0.4, lambda a: (E.pilula(c, "p do ar", TX + TW / 2, ys - 50, 40, "g", fundo=TINTA2, a=a),
                                                  E.pilula(c, "p do ar", TX + TW + 160, furo_y - 70, 40, "g", fundo=TINTA2, a=a)))
        E.frase(c, t, C["s10.a"], ps("tanque aberto com um", "i", 62) + [("furo", "g", 62, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s10.c"], ps("em cima e no furo:", "i", 56) + [("a mesma pressão", "g", 54)], XE, 320, passo=0.1)
        E.frase(c, t, C["s10.d"], ps("em cima:", "i", 56) + [("quase parada", "g", 54)], XE, 420, passo=0.1)
        E.frase(c, t, C["s10.e"], [("potencial", "g", 58, F.ACEL), ("→", "g", 56, TINTA2), ("cinética", "g", 58, F.VEL)], XE, 560, passo=0.12)
        return
    F.formula_legenda(c, t, C["s11.a"], "v = r{2 · g · h}", [("h", "da superfície até o furo", "m"), ("v", "velocidade de saída", "m/s")],
                      XE, 330, 120, size_l=46)
    pilula_em(c, t, C["s11.a"] + 1.2, "teorema de Torricelli", XE + 330, 180, 44, E.COR)
    E.frase(c, t, C["s11.b"], ps("= a pedra que cai de h", "i", 54, TINTA2), XE, 640, passo=0.1)
    E.formula_em(c, t, C["s11.c"], "h = 5 m:", XE, 790, 70, "g", TINTA)
    E.formula_em(c, t, C["s11.d"], "r{2 · 10 · 5} = r{100}", XE + 270, 790, 58, "g", TINTA)
    bola_txt(c, t, C["s11.e"], "10 m/s", 560, 960, 95, 44, CERTO)


# ---------------- erro ----------------
def folha(c, x, y, ang, a=1.0):
    c.save(); c.translate(x, y); c.rotate(ang)
    M.rrect(c, -10, 0, 20, 380, 4, "#FFFFFF", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-10, 0, 20, 380), 4, 4), M.paint(TINTA2, a, stroke=3))
    c.restore()


def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("ar rápido empurra mais?", "i", 64), XE + 480, 190, passo=0.1)
    if t >= C["s12.d"]:
        E.risco(c, XE + 470, 205, XE + 1180, 150, t, C["s12.d"], largura=10)
    junta = ease_io(prog(t, C["s12.d"], 0.8))
    q = ep(t, C["s12.b"], 0.5)
    cx, y0 = 1300, 360
    if q > 0:
        M.line(c, cx - 250, y0, cx + 250, y0, TINTA, q, 6)
        folha(c, cx - 110 + 70 * junta, y0, -6 * junta, q)
        folha(c, cx + 110 - 70 * junta, y0, 6 * junta, q)
    if t >= C["s12.b"] + 0.6:
        for i in range(3):
            yy = y0 + 520 - ((t * 400 + i * 120) % 400)
            F.seta(c, cx, yy, cx, yy - 90, F.VEL, ep(t, C["s12.b"] + 0.6, 0.4), 6, cabeca=16)
    if t >= C["s12.e"]:
        for d in (-1, 1):
            F.seta(c, cx + d * 330, y0 + 190, cx + d * 150, y0 + 190, E.COR, ep(t, C["s12.e"], 0.4), 8, cabeca=22)
    E.frase(c, t, C["s12.b"], ps("sopre entre", "i", 58) + [("duas folhas", "g", 58)], XE, 380, passo=0.12)
    E.frase(c, t, C["s12.c"], ps("elas se afastam?", "i", 58, TINTA2), XE, 490, passo=0.12)
    E.frase(c, t, C["s12.d"], [("elas se juntam!", "g", 64, COR)], XE, 620)
    E.frase(c, t, C["s12.e"], ps("no meio, pressão menor;", "i", 54) + [("o ar de fora empurra", "g", 52)], XE, 760, passo=0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
    E.frase(c, t, C["s13.a"], ps("tanque furado:", "i", 66, CLARO) + [("nem monte Bernoulli", "g", 66, BR)], W / 2, 310, "center", 0.12)
    E.formula_em(c, t, C["s13.b"], "v = r{2 · g · h}", W / 2, 470, 110, "g", BR, "center")
    E.frase(c, t, C["s13.c"], [("h:", "g", 56, BR)] + ps("da superfície até o furo, não do chão", "i", 56, CLARO), W / 2, 590, "center", 0.08)
    E.formula_em(c, t, C["s13.d"], "g = 10  →  v^2 = 20 · h", W / 2, 720, 84, "g", CLARO, "center")
    E.formula_em(c, t, C["s13.e"], "h = 0,8  →  v = r{16} = 4 m/s", W / 2, 850, 76, "g", BR, "center")
    E.frase(c, t, C["s14.a"], [("tanque fechado, ar apertado:", "g", 54, BR)] + ps("não vale", "i", 56, CLARO), W / 2, 990, "center", 0.08)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s15")
    E.frase(c, t, C["s15.a"], ps("caixa d'água aberta,", "i", 60) + [("furo", "g", 60, COR)], XE, 310, passo=0.12)
    E.frase(c, t, C["s15.b"], [("1,8 m", "g", 60, COR)] + ps("abaixo do nível", "i", 60), XE, 410, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("velocidade de", "i", 64) + [("saída?", "g", 64, COR)], XE, 570, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("cano que afina: no fino, a pressão é", "i", 56) + [("maior ou menor?", "g", 56, COR)], XE, 700, passo=0.08)
    if t < C["s16"]:
        furo_y = 300 + 520 - 80
        tanque_furo(c, t, C["s15.a"], 1480, 300, 260, 520, 460, furo_y, ep(t, C["s15.a"] + 0.5, 0.8))
        cota(c, t, C["s15.b"], (1440, 300 + 60), (1440, furo_y), "", lado=1, size=44)
        E.foco(c, t, C["s15.b"] + 0.3, 0.4, lambda a: E.escreve(c, "1,8 m", 1410 - E.larg("1,8 m", "b", 46), (360 + furo_y) / 2 + 16, 46, "b", COR, a))
    else:
        E.relogio(c, t, C["s16.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    linhas(c, t, [(C["s17.a"], "v^2 = 20 · 1,8", TINTA), (C["s17.b"], "v^2 = 36", TINTA), (C["s17.c"], "v = r{36}", TINTA)], XE, 260, 170, 92)
    bola_txt(c, t, C["s17.d"], "6 m/s", 1450, 340, 130, 60, CERTO)
    q = ep(t, C["s17.e"], 0.5)
    cano(c, 1000, 1800, 1400, 800, 160, 80, q)
    fluxo(c, t, C["s17.e"], 1000, 1800, 1400, 800, 160, 80, 110, n_lin=2)
    E.frase(c, t, C["s17.e"], ps("no fino, a água é", "i", 58) + [("mais rápida", "g", 58, F.VEL)], XE, 800, passo=0.1)
    E.frase(c, t, C["s17.f"], ps("então a pressão é", "i", 58) + [("menor", "g", 64, CERTO)], XE, 920, passo=0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s19"]:
        E.saida(c, t, C["s19"] - 0.1, lambda: resumo(c, t, C, "s18", (
            ("s18.a", [("mais rápido,", "g", 64, F.VEL), ("pressão menor", "g", 64, COR)]),
            ("s18.b", [("p + d·v²/2 + d·g·h", "g", 62, COR), ("constante", "i", 66)]),
            ("s18.c", [("furo:", "i", 70), ("v = √(2 · g · h)", "g", 64, COR)]))))
        return

    def desenho():
        q = ep(t, C["s19.b"], 0.6)
        if q <= 0:
            return
        for i, (rot, cor) in enumerate((("Q = A · v", E.COR), ("A₁v₁ = A₂v₂", F.VEL), ("Bernoulli", TINTA))):
            E.foco(c, t, C["s19.b"] + 0.3 * i, 0.4, lambda a, i=i, rot=rot, cor=cor: E.pilula(c, rot, 400 + i * 360, 800, 48, "g", fundo=cor, a=a))
    proxima(c, t, C, "s19", [("Praticando:", "g", 110, COR)], [("vazão e Bernoulli", "i", 96)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, asa=b_asa, tanque=b_tanque, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
