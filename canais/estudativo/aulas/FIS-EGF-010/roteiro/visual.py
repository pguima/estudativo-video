"""Visual — Estudativo · FIS-EGF-010: vazão e equação da continuidade.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-010_vazao_e_equacao_da_continuidade.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("vazao", "continuidade", "atalho", "questao", "fim"))

# todas as contas da aula
assert 20 * 50 == 1000 and 20 * 0.5 == 5 * 2 and (4 / 2) ** 2 == 4 and 3 ** 2 == 9  # 1.000 cm³/s = 1 L/s; v2 = 2 m/s
assert 2 * (2 / 1) ** 2 == 8 and 3 * 1 ** 2 == 3 and 3 * 200 == 600 and abs(12 / 0.6 - 20) < 1e-9  # bico 8 m/s; 0,6 L/s; 20 s


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


# ---------------- peças desta aula ----------------
def cano(c, x0, x1, xm, y, h1, h2, a=1.0, cor=AGUA, trans=60):
    """cano horizontal com eixo em y: largura h1 até xm e h2 depois (com transição suave). Devolve a função meia-altura(x)"""
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
    """setinhas de velocidade andando no cano: velocidade v1 px/s no trecho largo e v1·h1/h2 no fino (a vazão é a mesma)"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    v2 = v1 * h1 / h2
    for j in range(n_lin):
        fy = (j + 0.5) / n_lin - 0.5
        for trecho, (xa, xb, v, hh) in enumerate(((x0, xm, v1, h1), (xm, x1, v2, h2))):
            passo = esp * (v / v1)
            off = ((t - t0) * v) % passo
            x = xa + off - passo
            while x < xb:
                if x >= xa + 10 and x + 40 <= xb:
                    yy = y + fy * hh * 0.8
                    F.seta(c, x, yy, x + 22 + 18 * (v / v1), yy, F.VEL, q, 5, cabeca=14)
                x += passo


def tracejado_ret(c, x, y, w, h, q, cor=E.COR):
    pt = M.paint(cor, q, stroke=4)
    pt.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), pt)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            ap = ease_io(prog(t, C["s01.a"] + 0.2, 0.6))
            hb = lerp(110, 40, ap)
            q = ep(t, C["s01.a"], 0.5)
            cano(c, 820, 1300, 1290, 420, 110, 110, q)
            # o jato: sai mais rápido e vai mais longe quando a saída é menor
            alc = lerp(260, 560, ap)
            if q > 0:
                pts = [(1300 + alc * s, 420 + 380 * s * s) for s in [i / 30 for i in range(31)]]
                F.poli(c, pts, ep(t, C["s01.b"] - 0.3, 0.6), AGUA2, q, hb * 0.5)
                M.rrect(c, 1290, 420 - 70, 26, 70 - hb / 2, 6, E.COR, q * ap)
            E.frase(c, t, C["s01.a"], ps("tampe parte da", "i", 64) + [("mangueira", "g", 64, COR)], XE, 220, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("a água sai", "i", 60) + [("mais rápida", "g", 60, F.VEL)], XE, 330, passo=0.12)
            E.frase(c, t, C["s01.c"], ps("a torneira não abriu mais", "i", 56, TINTA2), XE, 820, passo=0.1)
            E.frase(c, t, C["s01.d"], ps("mudou o", "i", 66) + [("tamanho da saída", "g", 66, COR)], XE, 940, passo=0.12)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "a vazão de um cano"), ("s02.b", "a velocidade no cano fino")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "vazão:", "volume ÷ tempo (L/s)"), ("s03.c", "velocidade constante:", "distância = v · t"),
                              ("s03.d", "área do círculo:", "π · r²")), 3)


# ---------------- vazão ----------------
def b_vazao(c, t, C, b):
    if t < C["s05"]:
        def s04():
            E.frase(c, t, C["s04.a"], [("vazão", "g", 80, COR)] + ps("= volume que passa a cada segundo", "i", 60), XE, 220, passo=0.1)
            F.formula_legenda(c, t, C["s04.b"], "Q = f{V}{t}", [("V", "volume", "m^3 ou L"), ("t", "tempo", "s")], XE, 480, 130, size_l=50)
            E.frase(c, t, C["s04.c"], [("SI:", "g", 56), ("m³/s", "g", 56, COR)], XE, 800, passo=0.12)
            E.frase(c, t, C["s04.d"], [("dia a dia:", "g", 56), ("L/s", "g", 56, COR)], XE + 420, 800, passo=0.12)
            E.formula_em(c, t, C["s04.e"], "1 m^3 = 1.000 L", XE, 940, 64, "g", TINTA2)
            q = ep(t, C["s04.a"], 0.5)
            cano(c, 1100, 1800, 1800, 520, 160, 160, q)
            fluxo(c, t, C["s04.a"] + 0.3, 1100, 1800, 1799, 520, 160, 160, 160)
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            y, h = 600, 200
            q = ep(t, C["s05"], 0.5)
            cano(c, 300, 1700, 1700, y, h, h, q)
            fluxo(c, t, C["s05.a"], 300, 1700, 1699, y, h, h, 160, n_lin=2)
            x0 = 600
            comp = 520 * ease_io(prog(t, C["s05.b"], 1.2))
            if t >= C["s05.b"]:
                c.drawRect(skia.Rect.MakeXYWH(x0, y - h / 2, comp, h), M.paint(E.COR, 0.22))
                tracejado_ret(c, x0, y - h / 2, comp, h, ep(t, C["s05.c"], 0.4))
                cota(c, t, C["s05.b"] + 0.6, (x0, y + h / 2 + 50), (x0 + 520, y + h / 2 + 50), "v · t", lado=1, size=50)
            E.foco(c, t, C["s05.d"], 0.4, lambda a: (c.drawOval(skia.Rect.MakeXYWH(x0 - 40, y - h / 2, 80, h), M.paint(E.COR, a, stroke=5)),
                                                      E.escreve(c, "A", x0 - 120, y + 20, 60, "g", COR, a)))
            E.frase(c, t, C["s05.a"], ps("a água anda com velocidade", "i", 60) + [("v", "g", 60, F.VEL)], XE, 220, passo=0.1)
            E.formula_em(c, t, C["s05.d"], "V = A · v · t", XE, 950, 84, "g", TINTA)
            E.formula_em(c, t, C["s05.e"], "Q = f{A · v · t}{t}", XE + 680, 950, 84, "g", TINTA)
            if t >= C["s05.e"] + 0.6:
                xq = XE + 680 + E.formula(None, "Q = ", 0, 0, 84, a=0)
                wnum = E.formula(None, "A · v · t", 0, 0, 84 * 0.78, a=0)
                wt = E.formula(None, "t", 0, 0, 84 * 0.78, a=0)
                E.risco(c, xq + wnum + 4 - wt, 935, xq + wnum + 14, 885, t, C["s05.e"] + 0.6, cor=E.COR, largura=7)
                E.risco(c, xq + wnum / 2 - 8, 1010, xq + wnum / 2 + 26, 960, t, C["s05.e"] + 0.8, cor=E.COR, largura=7)
            bola_txt(c, t, C["s05.f"], "Q = A · v", 1600, 920, 140, 46)
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    if t < C["s07"]:
        def s06():
            F.formula_legenda(c, t, C["s06"], "Q = A · v", [("A", "área da seção do cano", "m^2"), ("v", "velocidade da água", "m/s"), ("Q", "vazão", "m^3/s")],
                              XE, 380, 140, tl=[C["s06.a"], C["s06.b"], C["s06.c"]], size_l=52)
            q = ep(t, C["s06.a"], 0.5)
            if q > 0:
                cx, cy = 1450, 560
                c.drawCircle(cx, cy, 170, M.paint(AGUA, 0.5 * q))
                c.drawCircle(cx, cy, 170, M.paint(TINTA, q, stroke=8))
                centro(c, "A", cx, cy + 30, 90, "g", COR, q)
                centro(c, "o cano cortado", cx, cy + 260, 46, "i", TINTA2, q)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    y, h = 520, 200
    q = ep(t, C["s07"], 0.5)
    cano(c, 900, 1800, 1800, y, h, h, q)
    fluxo(c, t, C["s07"], 900, 1800, 1799, y, h, h, 120, n_lin=2)
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "A = 20 cm²", 1350, y - h / 2 - 60, 44, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "v = 50 cm/s", 1350, y + h / 2 + 60, 44, "g", fundo=F.VEL, a=a))
    E.frase(c, t, C["s07.c"], ps("tudo em", "i", 62) + [("centímetro:", "g", 62, COR)], XE, 260, passo=0.12)
    E.formula_em(c, t, C["s07.d"], "Q = 20 · 50", XE, 420, 84, "g", TINTA)
    E.formula_em(c, t, C["s07.e"], "= 1.000 cm^3/s", XE, 560, 84, "g", TINTA)
    E.formula_em(c, t, C["s07.e"] + 1.2, "1.000 cm^3 = 1 L", XE, 720, 64, "g", TINTA2)
    bola_txt(c, t, C["s07.f"], "1 L/s", 600, 890, 120, 60, CERTO)


# ---------------- continuidade ----------------
CX0, CX1, CXM, CY, CH1, CH2 = 260, 1660, 960, 560, 240, 120


def b_continuidade(c, t, C, b):
    q = ep(t, C["s08"] - 0.3, 0.5)
    h2 = lerp(CH1, CH2, ease_io(prog(t, C["s08.a"], 1.0)))
    cano(c, CX0, CX1, CXM, CY, CH1, h2, q)
    fluxo(c, t, C["s08"] - 0.3, CX0, CX1, CXM, CY, CH1, h2, 120, n_lin=3, esp=170)
    if t < C["s09"]:
        E.frase(c, t, C["s08.a"], ps("o cano", "i", 70) + [("afina", "g", 70, COR)], XE, 200, passo=0.12)
        E.frase(c, t, C["s08.b"], ps("a água não se comprime nem se acumula", "i", 54, TINTA2), XE, 290, passo=0.08)
        E.frase(c, t, C["s08.c"], ps("o que entra num trecho", "i", 58) + [("sai do outro", "g", 58)], XE, 860, passo=0.1)
        E.frase(c, t, C["s08.d"], [("mesma vazão", "g", 70, COR)] + ps("em todo o cano", "i", 70), XE, 980, passo=0.12)
        return
    E.foco(c, t, C["s09"], 0.4, lambda a: (E.pilula(c, "A₁, v₁", 600, CY - CH1 / 2 - 60, 44, "g", fundo=TINTA, a=a),
                                           E.pilula(c, "A₂, v₂", 1350, CY - CH2 / 2 - 60, 44, "g", fundo=TINTA, a=a)))
    if t < C["s10"]:
        E.formula_em(c, t, C["s09.a"], "A₁ · v₁ = A₂ · v₂", W / 2, 230, 110, "g", COR, "center")
        pilula_em(c, t, C["s09.b"], "equação da continuidade", W / 2, 320, 46, E.COR)
        E.frase(c, t, C["s09.c"], [("área menor", "g", 64), ("→", "g", 60, TINTA2), ("velocidade maior", "g", 64, F.VEL)], W / 2, 870, "center", 0.15)
        E.frase(c, t, C["s09.d"], ps("inversamente proporcionais", "i", 60, TINTA2), W / 2, 980, "center", 0.1)
        return
    E.foco(c, t, C["s10.a"], 0.4, lambda a: (E.pilula(c, "20 cm²", 600, CY + CH1 / 2 + 60, 44, "g", fundo=TINTA2, a=a),
                                              E.pilula(c, "5 cm²", 1350, CY + CH2 / 2 + 60, 44, "g", fundo=TINTA2, a=a)))
    E.formula_em(c, t, C["s10.b"], "20 · 0,5 = 5 · v₂", XE, 200, 80, "g", TINTA)
    E.formula_em(c, t, C["s10.c"], "10 = 5 · v₂", XE + 900, 200, 80, "g", TINTA)
    bola_txt(c, t, C["s10.d"], "v₂ = 2 m/s", 1640, 330, 120, 44, CERTO)
    E.frase(c, t, C["s10.e"], [("área ÷ 4", "g", 62), ("→", "g", 58, TINTA2), ("velocidade × 4", "g", 62, F.VEL)], W / 2, 920, "center", 0.15)
    E.frase(c, t, C["s10.f"], ps("é o seu dedo na mangueira", "i", 54, TINTA2), W / 2, 1020, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("diâmetro no lugar da área", "i", 66), XE + 480, 190, passo=0.1)
    q = ep(t, C["s11.b"], 0.5)
    for i, (cx, d, rot) in enumerate(((560, 240, "D = 4 cm"), (1060, 120, "D = 2 cm"))):
        if q > 0:
            c.drawCircle(cx, 520, d / 2 + 0, M.paint(AGUA, 0.5 * q))
            c.drawCircle(cx, 520, d / 2, M.paint(TINTA, q, stroke=6))
            centro(c, rot, cx, 720, 48, "b", TINTA, q)
    E.foco(c, t, C["s11.c"], 0.4, lambda a: E.formula(c, "velocidade × 2?", 1250, 450, 60, "g", ERRADO, a))
    if t >= C["s11.d"]:
        E.risco(c, 1240, 470, 1730, 400, t, C["s11.d"], largura=10)
    if t >= C["s11.e"]:
        qq = ep(t, C["s11.e"], 0.5)
        for k in range(4):
            dx, dy = (k % 2) * 120, (k // 2) * 120
            pt = M.paint(E.COR, qq, stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
            c.drawCircle(500 + dx, 460 + dy, 60, pt)
    E.formula_em(c, t, C["s11.d"], "A = π · r^2", 1250, 620, 68, "g", TINTA)
    E.formula_em(c, t, C["s11.e"], "D ÷ 2  →  A ÷ 4", 1250, 780, 68, "g", TINTA)
    E.formula_em(c, t, C["s11.f"], "velocidade × 4", 1250, 930, 72, "g", CERTO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.frase(c, t, C["s12.a"], ps("com diâmetros,", "i", 72, CLARO) + [("nem calcule a área", "g", 72, BR)], W / 2, 320, "center", 0.12)
            E.formula_em(c, t, C["s12.b"], "v₂ = v₁ · (f{D₁}{D₂})^2", W / 2, 540, 120, "g", BR, "center")
            E.formula_em(c, t, C["s12.d"], "D ÷ 3  →  v × 9", W / 2, 760, 96, "g", CLARO, "center")
            E.frase(c, t, C["s12.e"], ps("o", "i", 60, CLARO) + [("π", "g", 60, BR)] + ps("corta dos dois lados", "i", 60, CLARO), W / 2, 920, "center", 0.12)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    E.frase(c, t, C["s13.a"], ps("o atalho", "i", 72, CLARO) + [("não dá a vazão", "g", 72, BR)], W / 2, 400, "center", 0.12)
    E.frase(c, t, C["s13.b"], ps("para ela,", "i", 66, CLARO) + [("calcule a área", "g", 66, BR)], W / 2, 600, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s14")
    E.frase(c, t, C["s14.a"], [("mangueira:", "i", 60), ("D = 2 cm", "g", 60, COR)], XE, 310, passo=0.12)
    E.frase(c, t, C["s14.b"], [("bico:", "i", 60), ("D = 1 cm", "g", 60, COR)], XE, 410, passo=0.12)
    E.frase(c, t, C["s14.c"], [("na mangueira:", "i", 60), ("2 m/s", "g", 60, F.VEL)], XE, 510, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("velocidade no", "i", 64) + [("bico?", "g", 64, COR)], XE, 680, passo=0.12)
    E.frase(c, t, C["s14.e"], ps("tempo para", "i", 64) + [("12 L?", "g", 64, COR), ("(π = 3)", "b", 50, TINTA2)], XE, 800, passo=0.12)
    if t < C["s15"]:
        q = ep(t, C["s14.a"], 0.5)
        cano(c, 1050, 1780, 1600, 560, 160, 80, q)
        fluxo(c, t, C["s14.a"], 1050, 1780, 1600, 560, 160, 80, 100, n_lin=2)
    else:
        E.relogio(c, t, C["s15.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s16.e"]:
        def parte1():
            linhas(c, t, [(C["s16.a"], "D ÷ 2", TINTA), (C["s16.b"], "A ÷ 4", TINTA), (C["s16.c"], "v × 4 = 2 × 4", TINTA)], XE, 260, 170, 92)
            bola_txt(c, t, C["s16.d"], "8 m/s", 1400, 480, 150, 64, CERTO)
        E.saida(c, t, C["s16.e"] - 0.1, parte1)
        return
    linhas(c, t, [(C["s16.e"], "r = 1 cm:  A = 3 · 1^2 = 3 cm^2", TINTA), (C["s16.f"], "2 m/s = 200 cm/s", TINTA2),
                  (C["s16.f"] + 1.4, "Q = 3 · 200 = 600 cm^3/s = 0,6 L/s", TINTA), (C["s16.g"], "t = 12 ÷ 0,6", TINTA)], XE, 230, 150, 66)
    bola_txt(c, t, C["s16.h"], "20 s", 1500, 860, 120, 64, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s18"]:
        E.saida(c, t, C["s18"] - 0.1, lambda: resumo(c, t, C, "s17", (
            ("s17.a", [("Q = V / t", "g", 64, COR), ("=", "g", 64, TINTA2), ("A · v", "g", 64, COR)]),
            ("s17.b", [("mesma vazão", "g", 64), ("em todo o cano", "i", 70)]),
            ("s17.c", [("cano fino:", "i", 70), ("água mais rápida", "g", 64, F.VEL)]))))
        return

    def desenho():
        q = ep(t, C["s18.b"], 0.6)
        if q <= 0:
            return
        p = skia.Path()
        x0, y0 = 300, 840
        p.moveTo(x0, y0); p.cubicTo(x0 + 200, y0 - 120, x0 + 600, y0 - 110, x0 + 860, y0)
        p.cubicTo(x0 + 600, y0 + 20, x0 + 200, y0 + 30, x0, y0); p.close()
        c.drawPath(p, M.paint("#B9BCC4", q))
        c.drawPath(p, M.paint(TINTA, q, stroke=4))
        F.seta(c, x0 + 430, y0 - 40, x0 + 430, y0 - 220, E.COR, ep(t, C["s18.b"] + 0.5, 0.5), 10)
    proxima(c, t, C, "s18", [("Princípio", "g", 120, COR)], [("de Bernoulli", "g", 110, COR)], desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, vazao=b_vazao, continuidade=b_continuidade, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
