"""Visual — Estudativo · FIS-EGF-005: lei de Stevin.

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
ARQUIVO_FINAL = "estudativo_FIS-EGF-005_lei_de_stevin.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("coluna", "vasos", "atalho", "questao", "fim"))

# todas as contas da aula
assert 1000 * 10 * 10 == 100_000 and 1 + 1 == 2 and abs(0.8 * 10 / 1 - 8) < 1e-9
assert 1000 * 10 * 15 == 150_000 and 150_000 / 100_000 == 1.5 and 1.5 + 1 == 2.5 and 3 + 1 == 4
assert 1 + 20 / 10 == 3 and 1 + 40 / 10 == 5 and abs(13600 * 10 * 0.75 - 102_000) < 1e-6  # 75 cm de mercúrio ≈ 1 atm


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
def tanque(c, x, y, w, h, nivel, a=1.0, cor=AGUA):
    """recipiente aberto: paredes em tinta, líquido até a altura `nivel` (px a partir do fundo)"""
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeXYWH(x, y + h - nivel, w, nivel), M.paint(cor, 0.45 * a))
    M.line(c, x, y + h - nivel, x + w, y + h - nivel, AGUA2 if cor == AGUA else "#B98A2A", a, 5)
    for X in (x, x + w):
        M.line(c, X, y, X, y + h, TINTA, a, 6)
    M.line(c, x - 3, y + h, x + w + 3, y + h, TINTA, a, 6)


def mergulhador(c, x, y, s=1.0, a=1.0):
    if a <= 0:
        return
    M.rrect(c, x - 34 * s, y - 14 * s, 68 * s, 28 * s, 12 * s, E.COR, a)
    E.bola(c, x - 44 * s, y - 4 * s, 16 * s, E.mix(E.COR, BR, 0.25), a)
    M.rrect(c, x - 20 * s, y - 32 * s, 40 * s, 16 * s, 6 * s, TINTA2, a)
    M.line(c, x + 34 * s, y, x + 60 * s, y - 10 * s, TINTA, a, 5 * s)


def regua(c, t, t0, x, y0, k, marcas, a=1.0):
    """régua de profundidade à esquerda do tanque: marcas = [(metros, texto)]"""
    q = ep(t, t0, 0.5) * a
    if q <= 0:
        return
    for m, s in marcas:
        y = y0 + m * k
        M.line(c, x, y, x + 30, y, TINTA, q, 4)
        E.escreve(c, s, x - 10 - E.larg(s, "b", 40), y + 14, 40, "b", TINTA2, q)


def tubo_u(c, t, t0, cx, yb, k, h_oleo, h_agua, a=1.0):
    """tubo em U: água embaixo e à esquerda; óleo à direita sobre a água. Alturas em cm, k = px por cm. Devolve (y_sep, y_agua, y_oleo, xL, xR)"""
    q = ep(t, t0, 0.6) * a
    w, gap = 120, 300
    xL, xR = cx - gap / 2 - w, cx + gap / 2
    y_sep = yb - 120
    y_ag = y_sep - h_agua * k
    y_ol = y_sep - h_oleo * k
    if q <= 0:
        return y_sep, y_ag, y_ol, xL, xR
    agua, oleo = M.paint(AGUA, 0.55 * q), M.paint(OLEO, 0.65 * q)
    c.drawRect(skia.Rect.MakeLTRB(xL, y_ag, xL + w, yb), agua)
    c.drawRect(skia.Rect.MakeLTRB(xL, yb - 120, xR + w, yb), agua)
    c.drawRect(skia.Rect.MakeLTRB(xR, y_sep, xR + w, yb), agua)
    c.drawRect(skia.Rect.MakeLTRB(xR, y_ol, xR + w, y_sep), oleo)
    top = min(y_ag, y_ol) - 140
    p = skia.Path()
    p.moveTo(xL, top); p.lineTo(xL, yb); p.lineTo(xR + w, yb); p.lineTo(xR + w, top)
    p.moveTo(xL + w, top); p.lineTo(xL + w, yb - 120); p.lineTo(xR, yb - 120); p.lineTo(xR, top)
    c.drawPath(p, M.paint(TINTA, q, stroke=6))
    return y_sep, y_ag, y_ol, xL, xR


TX, TY, TW, TH, TK = 1080, 160, 560, 860, 26  # tanque fundo: 30 m de água em 780 px (26 px por metro)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    if t < C["s02"]:
        def um():
            q = ep(t, C["s01.a"], 0.5)
            if q > 0:
                tanque(c, TX, TY, TW, TH, TH - 60, q)
            regua(c, t, C["s01.a"], TX - 20, TY + 60, TK, ((0, "0 m"), (10, "10 m"), (20, "20 m"), (30, "30 m")))
            prof = 10 * ease_io(prog(t, C["s01.a"] + 0.3, 1.6))
            E.foco(c, t, C["s01.a"] + 0.3, 0.4, lambda a: mergulhador(c, TX + TW / 2, TY + 60 + prof * TK, 1.2, a))
            E.frase(c, t, C["s01.a"], ps("a", "i", 70) + [("10 m", "g", 70, COR)] + ps("de profundidade", "i", 70), XE, 200, passo=0.12)
            E.frase(c, t, C["s01.b"], ps("a pressão", "i", 70) + [("dobrou", "g", 70, COR)], XE, 310, passo=0.12)
            pilula_em(c, t, C["s01.b"] + 0.4, "2 atm", TX + TW / 2 + 160, TY + 60 + 10 * TK, 44, E.COR)
            E.frase(c, t, C["s01.c"], [("10 m de água", "g", 58)], XE, 560)
            E.frase(c, t, C["s01.c"] + 0.8, [("=", "g", 58, TINTA2)] + ps("todo o ar em cima", "i", 60), XE, 650, passo=0.1)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "a pressão num líquido"), ("s02.b", "o atalho dos 10 metros"), ("s02.c", "os vasos comunicantes")))


def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "pressão = força ÷ área:", "1 atm ≈ 100.000 Pa"), ("s03.c", "densidade = massa ÷ volume:", "água: 1.000 kg/m³")), 2)


# ---------------- a coluna ----------------
def b_coluna(c, t, C, b):
    x, y, w, h = 1150, 200, 560, 760
    if t < C["s06"]:
        def s0405():
            q = ep(t, C["s04"], 0.5)
            if q > 0:
                tanque(c, x, y, w, h, h - 40, q)
            cx0, cw = x + 200, 160
            top, bot = y + 40, y + 560
            qq = ep(t, C["s04.c"], 0.6)
            if qq > 0:
                c.drawRect(skia.Rect.MakeLTRB(cx0, top, cx0 + cw, bot), M.paint(AGUA2, 0.35 * qq))
                c.drawRect(skia.Rect.MakeLTRB(cx0, top, cx0 + cw, bot), M.paint(E.COR, qq, stroke=4))
            cota(c, t, C["s04.c"] + 0.3, (cx0 - 50, top), (cx0 - 50, bot), "h", lado=-1, size=56)
            E.foco(c, t, C["s04.c"] + 0.6, 0.4, lambda a: (M.line(c, cx0, bot, cx0 + cw, bot, E.COR, a, 10), centro(c, "área A", cx0 + cw / 2, bot + 60, 44, "b", COR, a)))
            F.vetor(c, t, C["s04.d"], (cx0 + cw / 2, top + 150), (cx0 + cw / 2, bot - 30), "P", None, E.COR, 10, lado=-1)
            if t < C["s05"]:
                E.frase(c, t, C["s04.a"], ps("por que a pressão", "i", 64) + [("aumenta", "g", 64, COR)] + ps("com a profundidade?", "i", 64), XE, 190, passo=0.1)
                E.frase(c, t, C["s04.b"], ps("a água de cima", "i", 66) + [("pesa", "g", 66, COR)], XE, 330, passo=0.12)
                E.frase(c, t, C["s04.d"], [("p =", "g", 64), ("peso ÷ área", "g", 64, COR)], XE, 520, passo=0.12)
            else:
                linhas(c, t, [(C["s05.a"], "P = m · g", TINTA), (C["s05.b"], "m = d · V", TINTA), (C["s05.c"], "V = A · h", TINTA)], XE, 200, 120, 72)
                E.formula_em(c, t, C["s05.d"], "p = f{d · A · h · g}{A}", XE, 640, 92, "g", TINTA)
                if t >= C["s05.d"] + 0.6:
                    wa = E.formula(None, "p = ", 0, 0, 92, a=0)
                    num = E.formula(None, "d · A · h · g", 0, 0, 92 * 0.78, a=0) + 92 * 0.12
                    xa = XE + wa + (num - E.formula(None, "d · A · h · g", 0, 0, 92 * 0.78, a=0)) / 2 + E.formula(None, "d · ", 0, 0, 92 * 0.78, a=0)
                    E.risco(c, xa - 4, 612, xa + 50, 560, t, C["s05.d"] + 0.6, cor=E.COR, largura=8)
                    xb = XE + wa + num / 2 - 22
                    E.risco(c, xb, 700, xb + 50, 650, t, C["s05.d"] + 0.8, cor=E.COR, largura=8)
                E.formula_em(c, t, C["s05.e"], "= d · g · h", XE, 830, 100, "g", COR)
        E.saida(c, t, C["s06"] - 0.1, s0405)
        return
    if t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], ps("somando o ar da superfície,", "i", 62) + [("p₀", "g", 62, COR)], XE, 190, passo=0.1)
            F.formula_legenda(c, t, C["s06.b"], "p = p₀ + d · g · h", [("d", "densidade do líquido", "kg/m^3"), ("g", "gravidade, 10", "m/s^2"),
                                                                      ("h", "profundidade, da superfície para baixo", "m")],
                              XE, 420, 130, tl=[C["s06.c"], C["s06.d"], C["s06.e"]], size_l=48)
            pilula_em(c, t, C["s06.b"] + 0.6, "lei de Stevin", 1500, 330, 52, E.COR)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    if t < C["s08"]:
        def s07():
            q = ep(t, C["s07"], 0.5)
            if q > 0:
                tanque(c, TX + 200, TY, TW - 200, TH, TH - 60, q)
            regua(c, t, C["s07"], TX + 180, TY + 60, TK, ((0, "0 m"), (10, "10 m"), (20, "20 m")))
            E.foco(c, t, C["s07.a"], 0.4, lambda a: mergulhador(c, TX + 380, TY + 60 + 10 * TK, 1.1, a))
            E.formula_em(c, t, C["s07.b"], "1.000 · 10 · 10", XE, 330, 84, "g", TINTA)
            E.formula_em(c, t, C["s07.c"], "= 100.000 Pa", XE, 470, 84, "g", TINTA)
            pilula_em(c, t, C["s07.d"], "+1 atm", XE + 160, 600, 56, E.COR)
            E.formula_em(c, t, C["s07.e"], "total: 1 + 1 = 2 atm", XE, 800, 84, "g", COR)
        E.saida(c, t, C["s08"] - 0.1, s07)
        return
    # s08: a largura não importa
    E.frase(c, t, C["s08.a"], ps("não entrou na conta:", "i", 66) + [("a largura", "g", 66, COR)], XE, 200, passo=0.12)
    yb, nivel = 900, 420
    for i, (k_, x, w, nome) in enumerate((("s08.c", 260, 140, "copo"), ("s08.c", 620, 320, "balde"), ("s08.c", 1100, 640, "piscina"))):
        q = ep(t, C[k_] + 0.4 * i, 0.5)
        if q > 0:
            tanque(c, x, yb - 520, w, 520, nivel, q)
            centro(c, nome, x + w / 2, yb + 60, 44, "i", TINTA2, q)
        E.foco(c, t, C["s08.d"] + 0.2 * i, 0.4, lambda a, x=x, w=w: E.bola(c, x + w / 2, yb - 120, 16, E.COR, a))
    if t >= C["s08.d"]:
        M.line(c, 200, yb - 120, 1800, yb - 120, E.COR, ep(t, C["s08.d"], 0.6) * 0.6, 3, dash=E.TRACO)
    pilula_em(c, t, C["s08.d"] + 0.6, "mesma profundidade, mesma pressão", W / 2, 1010, 46, E.COR)


# ---------------- vasos comunicantes ----------------
def b_vasos(c, t, C, b):
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], [("vasos comunicantes:", "g", 64, COR)] + ps("ligados por baixo", "i", 66), XE, 190, passo=0.1)
            yb = 900
            iguala = ease_io(prog(t, C["s09.d"], 1.2))
            alto = lerp(260, 0, iguala) if t >= C["s09.b"] else 0
            nivel = 360
            q = ep(t, C["s09.a"], 0.5)
            if q > 0:
                c.drawRect(skia.Rect.MakeLTRB(300, yb - 90, 1600, yb), M.paint(AGUA, 0.45 * q))
                for x, w in ((300, 160), (800, 300), (1400, 200)):
                    hh = nivel + (alto if x == 300 else -alto * 0.25)
                    c.drawRect(skia.Rect.MakeLTRB(x, yb - hh, x + w, yb), M.paint(AGUA, 0.45 * q))
                    M.line(c, x, yb - hh, x + w, yb - hh, AGUA2, q, 5)
                    M.line(c, x, yb - 560, x, yb, TINTA, q, 5)
                    M.line(c, x + w, yb - 560, x + w, yb - 90 if x + w < 1600 else yb, TINTA, q, 5)
                M.line(c, 300, yb, 1600, yb, TINTA, q, 6)
                for x0, x1 in ((460, 800), (1100, 1400)):
                    M.line(c, x0, yb - 90, x1, yb - 90, TINTA, q, 5)
            if C["s09.c"] <= t < C["s09.d"]:
                F.vetor(c, t, C["s09.c"], (420, yb - 45), (700, yb - 45), None, None, E.COR, 10)
            if t >= C["s09.d"] + 1.0:
                M.line(c, 260, yb - nivel, 1660, yb - nivel, E.COR, ep(t, C["s09.d"] + 1.0, 0.5), 3, dash=E.TRACO)
            E.frase(c, t, C["s09.b"], ps("mais alta de um lado?", "i", 56), XE, 300, passo=0.1)
            E.frase(c, t, C["s09.c"], ps("pressão maior embaixo:", "i", 56) + [("a água corre", "g", 54, COR)], XE + 620, 300, passo=0.1)
            E.frase(c, t, C["s09.d"], [("níveis iguais,", "g", 62, COR)] + ps("qualquer formato", "i", 62), W / 2, 1010, "center", 0.12)
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    k = 26
    cx, yb = 1350, 940
    ys, ya, yo, xL, xR = tubo_u(c, t, C["s10"], cx, yb, k, 10, 8 if t >= C["s11"] else 8)
    E.foco(c, t, C["s10.a"], 0.4, lambda a: (centro(c, "água", xL + 60, yb + 60, 44, "b", AGUA2, a), centro(c, "óleo", xR + 60, yo - 30, 44, "b", "#B98A2A", a)))
    if t >= C["s10.c"]:
        M.line(c, xL - 80, ys, xR + 200, ys, E.COR, ep(t, C["s10.c"], 0.5), 4, dash=E.TRACO)
        E.foco(c, t, C["s10.c"] + 0.3, 0.4, lambda a: E.escreve(c, "mesma pressão", xL - 420, ys + 14, 40, "b", COR, a))
    cota(c, t, C["s10.d"], (xR + 160, ys), (xR + 160, yo), "h₂", lado=1, size=48)
    cota(c, t, C["s10.d"] + 0.3, (xL - 40, ys), (xL - 40, ya), "h₁", lado=-1, size=48)
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], ps("dois líquidos que", "i", 62) + [("não se misturam", "g", 60, COR)], XE, 190, passo=0.1)
        E.frase(c, t, C["s10.b"], [("níveis diferentes", "g", 62)], XE, 300)
        E.formula_em(c, t, C["s10.d"], "d₁ · h₁ = d₂ · h₂", XE, 560, 100, "g", COR)
        E.frase(c, t, C["s10.d"] + 1.0, ps("alturas a partir da separação", "i", 50, TINTA2), XE, 660, passo=0.08)
        return
    E.formula_em(c, t, C["s11.a"], "óleo: d₂ = 0,8 g/cm^3", XE, 220, 64, "g", "#B98A2A")
    E.formula_em(c, t, C["s11.b"], "h₂ = 10 cm", XE, 320, 64, "g", "#B98A2A")
    E.formula_em(c, t, C["s11.c"], "água: d₁ = 1 g/cm^3", XE, 420, 64, "g", AGUA2)
    E.formula_em(c, t, C["s11.d"], "0,8 · 10 = 1 · h₁", XE, 600, 84, "g", TINTA)
    bola_txt(c, t, C["s11.e"], "h₁ = 8 cm", 520, 790, 140, 52, CERTO)
    E.frase(c, t, C["s11.f"], ps("menos denso:", "i", 56) + [("mais alto", "g", 56, COR)], XE, 1010, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("esquecer o ar", "i", 70), XE + 480, 190, passo=0.12)
    q = ep(t, C["s12.a"], 0.5)
    if q > 0:
        tanque(c, TX + 200, TY, TW - 200, TH, TH - 60, q)
    regua(c, t, C["s12.a"], TX + 180, TY + 60, TK, ((0, "0 m"), (30, "30 m")))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: mergulhador(c, TX + 380, TY + 60 + 30 * TK - 30, 1.1, a))
    E.formula_em(c, t, C["s12.a"] + 0.6, "total = 3 atm?", XE, 360, 80, "g", ERRADO)
    if t >= C["s12.c"]:
        E.risco(c, XE - 10, 380, XE + 560, 300, t, C["s12.c"], largura=10)
    E.formula_em(c, t, C["s12.b"], "água sozinha: 3 atm", XE, 480, 72, "g", TINTA)
    E.formula_em(c, t, C["s12.c"], "total: 3 + 1 = 4 atm", XE, 600, 84, "g", CERTO)
    E.frase(c, t, C["s12.d"], ps("a atmosfera", "i", 60) + [("continua lá em cima", "g", 58, COR)], XE, 740, passo=0.1)
    E.frase(c, t, C["s12.e"], ps("a questão pede:", "i", 58), XE, 860, passo=0.1)
    E.frase(c, t, C["s12.f"], [("total", "g", 58, COR), ("ou", "i", 60), ("só a do líquido?", "g", 58)], XE, 950, passo=0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 170, "center")
            E.frase(c, t, C["s13.a"], ps("na água, cada", "i", 70, CLARO) + [("10 m", "g", 70, BR)] + [("= +1 atm", "g", 70, BR)], W / 2, 320, "center", 0.12)
            E.formula_em(c, t, C["s13.b"], "20 m  →  1 + 2 = 3 atm", W / 2, 500, 90, "g", CLARO, "center")
            E.formula_em(c, t, C["s13.c"], "40 m  →  1 + 4 = 5 atm", W / 2, 640, 90, "g", CLARO, "center")
            E.formula_em(c, t, C["s13.d"], "1.000 · 10 · 10 = 100.000 Pa = 1 atm", W / 2, 840, 76, "g", BR, "center")
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], [("só vale", "g", 72, BR)] + ps("para a água", "i", 72, CLARO), W / 2, 250, "center", 0.12)
    E.frase(c, t, C["s14.b"], [("mercúrio:", "g", 66, BR), ("13,6 ×", "g", 66, CLARO)] + ps("mais denso", "i", 68, CLARO), W / 2, 450, "center", 0.12)
    E.frase(c, t, C["s14.c"], [("≈ 75 cm", "g", 70, BR)] + ps("de mercúrio", "i", 70, CLARO) + [("= 1 atm", "g", 70, BR)], W / 2, 620, "center", 0.12)
    E.frase(c, t, C["s14.d"], ps("aí,", "i", 66, CLARO) + [("use a fórmula", "g", 66, BR)], W / 2, 820, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s15")
    E.frase(c, t, C["s15.a"], ps("mergulhador a", "i", 66) + [("15 m", "g", 66, COR)], XE, 330, passo=0.12)
    E.frase(c, t, C["s15.b"], [("d =", "g", 60), ("1.000 kg/m³", "g", 60, COR)], XE, 440, passo=0.12)
    E.frase(c, t, C["s15.c"], ps("pressão total em", "i", 70) + [("atm?", "g", 70, COR)], XE, 620, passo=0.12)
    E.frase(c, t, C["s15.d"], ps("quantas vezes a da", "i", 70) + [("superfície?", "g", 70)], XE, 760, passo=0.12)
    if t < C["s16"]:
        q = ep(t, C["s15.a"], 0.5)
        if q > 0:
            tanque(c, TX + 200, TY, TW - 200, TH, TH - 60, q)
            mergulhador(c, TX + 380, TY + 60 + 15 * TK, 1.1, q)
        regua(c, t, C["s15.a"], TX + 180, TY + 60, TK, ((0, "0 m"), (15, "15 m")))
    else:
        E.relogio(c, t, C["s16.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    linhas(c, t, [(C["s17.a"], "1.000 · 10 · 15", TINTA), (C["s17.b"], "= 150.000 Pa", TINTA), (C["s17.c"], "= 1,5 atm de água", COR)], XE, 220, 140, 80)
    E.formula_em(c, t, C["s17.d"], "atalho: 15 m = 10 + 5  →  1,5 atm", XE, 680, 64, "g", TINTA2)
    E.formula_em(c, t, C["s17.e"], "1,5 + 1 (ar) =", XE, 860, 84, "g", TINTA)
    bola_txt(c, t, C["s17.e"] + 0.6, "2,5 atm", 1450, 520, 160, 66, CERTO)
    pilula_em(c, t, C["s17.f"], "2,5 vezes a da superfície", 1450, 780, 46, TINTA)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s19"]:
        E.saida(c, t, C["s19"] - 0.1, lambda: resumo(c, t, C, "s18", (
            ("s18.a", [("p = p₀ + d · g · h", "g", 66, COR)]),
            ("s18.b", [("água:", "g", 66), ("+1 atm", "g", 66, COR), ("a cada 10 m", "i", 70)]),
            ("s18.c", [("mesma profundidade,", "i", 70), ("mesma pressão", "g", 64, COR)]))))
        return

    def desenho():
        q = ep(t, C["s19.a"], 0.6)
        if q <= 0:
            return
        yb = 1000
        c.drawRect(skia.Rect.MakeLTRB(300, 860, 1180, yb), M.paint(OLEO, 0.6 * q))
        c.drawRect(skia.Rect.MakeLTRB(300, 760, 420, 860), M.paint(OLEO, 0.6 * q))
        c.drawRect(skia.Rect.MakeLTRB(860, 800, 1180, 860), M.paint(OLEO, 0.6 * q))
        M.rrect(c, 290, 740, 140, 22, 6, TINTA, q)
        M.rrect(c, 850, 780, 340, 26, 6, TINTA, q)
        F.bloco(c, 1020, 720, 220, 100, "carro", a=q, size=36)
        F.seta(c, 360, 640, 360, 730, E.COR, q, 9)
    proxima(c, t, C, "s19", [("Princípio", "g", 120, COR), ("de", "i", 110), ("Pascal", "g", 120, COR)], None, desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, coluna=b_coluna, vasos=b_vasos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
