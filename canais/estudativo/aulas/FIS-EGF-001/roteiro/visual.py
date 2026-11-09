"""Visual — Estudativo · FIS-EGF-001: torque e alavancas. Primeira aula da trilha Equilíbrio, Gravitação e Fluidos.

A linguagem visual da Física (cores de vetores, medida com unidade, fórmula com legenda, conversão) está no visual.py da
FIS-CIN-001 e vale aqui. LINGUAGEM VISUAL DA TRILHA EQUILÍBRIO, GRAVITAÇÃO E FLUIDOS (as aulas FIS-EGF-* copiam daqui):
- EIXO E APOIO: triângulo em tinta (apoio) com o ponto do eixo em laranja; dobradiça = bolinha em tinta. Barras, tábuas e
  portas em madeira (MADEIRA) vistas de lado ou de cima; corpos apoiados = F.bloco laranja com a massa escrita.
- BRAÇO: cota fina em cinza-tinta (cota), SEMPRE começando no eixo, com a medida e a unidade ("2 m"). Braço errado = cota
  vermelha riscada.
- TORQUE E GIRO: seta curva em volta do eixo (seta_giro). Horário = laranja (COR); anti-horário = azul (F.NEG). Os dois
  lados de uma igualdade de torques usam essas mesmas cores ("horário = anti-horário").
- FORÇAS: laranja, como em toda a Física (peso para baixo, apoio para cima); só na hidrostática o empuxo é azul (vem da
  água) para não se confundir com o peso, que segue laranja.
- ASTROS: Sol = esfera âmbar (SOL); Terra = esfera azul (TERRA); outros planetas e luas = cinza (LUA). Órbita = elipse
  tracejada em tinta; área varrida = setor laranja translúcido; distância centro a centro = cota.
- FLUIDOS: água = azul translúcido (AGUA) com a superfície mais forte; óleo = âmbar (OLEO); mercúrio = cinza. Pressão =
  setinhas laranja perpendiculares à parede, maiores onde a pressão é maior; profundidade h = cota da superfície para baixo.
  Velocidade do fluido = setinhas em petróleo (F.VEL) andando no cano, mais juntas e rápidas no trecho fino.
- Conta passo a passo: uma linha por etapa (linhas), a última na esfera laranja (bola_txt) ou verde, se for a resposta certa.
- Atalho no palco escuro; questão com E.relogio; resumo numerado; próxima aula com o desenho dela. Mínimo 40 px.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import fisica as F
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Física", "Equilíbrio, Gravitação e Fluidos")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_FIS-EGF-001_torque_e_alavancas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("torque", "gangorra", "equilibrio", "atalho", "questao", "fim"))

# todas as contas da aula
assert abs(20 * 0.8 - 16) < 1e-9 and abs(20 * 0.1 - 2) < 1e-9 and 16 / 2 == 8
assert 30 * 10 == 300 and 60 * 10 == 600 and 300 * 2 == 600 * 1 and 300 + 600 == 900 and 5 - 1.5 == 3.5
assert abs(600 * 0.3 - 180) < 1e-9 and abs(180 / 1.5 - 120) < 1e-9 and abs(1.5 / 0.3 - 5) < 1e-9 and 600 / 5 == 120


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


# ---------------- peças desta aula ----------------
def tabua(c, cx, cy, L, ang=0.0, a=1.0, esp=26):
    """tábua de comprimento L centrada em (cx, cy), girada ang graus (positivo = horário na tela)"""
    if a <= 0:
        return
    c.save(); c.translate(cx, cy); c.rotate(ang)
    M.rrect(c, -L / 2, -esp / 2, L, esp, 8, MADEIRA, a)
    M.line(c, -L / 2 + 10, -esp / 2 + 6, L / 2 - 10, -esp / 2 + 6, "#D19A66", a * 0.7, 3)
    c.restore()


def ponto_tabua(cx, cy, u, ang):
    """ponto a u pixels do centro da tábua girada"""
    g = math.radians(ang)
    return cx + u * math.cos(g), cy + u * math.sin(g)


def porta(c, hx, hy, L, ang, a=1.0, paredes=True):
    """porta vista de cima: dobradiça em (hx, hy), folha de comprimento L aberta ang graus (para baixo na tela)"""
    if a <= 0:
        return
    if paredes:
        M.line(c, hx - 200, hy - 30, hx - 10, hy - 30, TINTA, a, 8)
        M.line(c, hx + L + 30, hy - 30, hx + L + 160, hy - 30, TINTA, a, 8)
        pt = M.paint(TINTA2, 0.5 * a, stroke=3)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawArc(skia.Rect.MakeXYWH(hx - L, hy - L, 2 * L, 2 * L), 0, 40, False, pt)
    c.save(); c.translate(hx, hy); c.rotate(ang)
    M.rrect(c, 0, -14, L, 28, 6, MADEIRA, a)
    c.drawCircle(L - 50, 22, 12, M.paint(TINTA, a))
    c.restore()
    c.drawCircle(hx, hy, 18, M.paint(TINTA, a))
    c.drawCircle(hx, hy, 7, M.paint(E.COR, a))


def ponto_porta(hx, hy, u, ang):
    g = math.radians(ang)
    return hx + u * math.cos(g), hy + u * math.sin(g)


def gangorra(c, t, t0, cx, cy, L, ang=0.0, d=0.6):
    """apoio com o vértice em (cx, cy) e a tábua por cima; devolve se já apareceu"""
    q = ep(t, t0, d)
    if q <= 0:
        return False
    apoio(c, cx, cy + 13, 80, q)
    tabua(c, cx, cy, L * ease_io(q), ang, q)
    F.chao(c, cx - L / 2 - 60, cx + L / 2 + 60, cy + 93, q * 0.8)
    return True


def sobre(cx, cy, u, ang, h):
    """centro de um bloco de altura h sentado na tábua a u pixels do eixo"""
    x, y = ponto_tabua(cx, cy, u, ang)
    g = math.radians(ang)
    return x + math.sin(g) * (13 + h / 2), y - math.cos(g) * (13 + h / 2)


# ---------------- gancho ----------------
def empurra(c, t, t0, P, ang, comp, rot=None, modulo=None, cor=None):
    """força que CHEGA ao ponto P vindo da direção oposta a ang (graus da Física): a ponta encosta no corpo"""
    dx, dy = F._dir(ang)
    F.vetor(c, t, t0, (P[0] - dx * comp, P[1] - dy * comp), P, rot, modulo, cor, 10, em=0.4)


def b_gancho(c, t, C, b):
    hx, hy, L = 980, 260, 760
    if t < C["s02"]:
        def um():
            # a porta: perto da dobradiça quase não gira; perto da maçaneta, gira fácil
            q1 = math.sin(math.pi * prog(t, C["s01.b"] + 0.3, 1.2)) * 3
            q2 = 34 * ease_io(prog(t, C["s01.d"], 1.4))
            ang = q1 + q2
            E.foco(c, t, C["s01.a"], 0.6, lambda a: porta(c, hx, hy, L, ang, a))
            if C["s01.b"] <= t < C["s01.c"] - 0.1:
                empurra(c, t, C["s01.b"], ponto_porta(hx, hy, 90, ang), -90 - ang, 150)
            if t >= C["s01.c"]:
                empurra(c, t, C["s01.c"], ponto_porta(hx, hy, L - 30, ang), -90 - ang, 150)
            E.frase(c, t, C["s01.b"], ps("perto da dobradiça:", "i", 64), XE, 520, passo=0.1)
            E.frase(c, t, C["s01.b"] + 1.4, [("quase não gira", "g", 64, ERRADO)], XE, 610)
            E.frase(c, t, C["s01.c"], ps("perto da maçaneta:", "i", 64), XE, 750, passo=0.1)
            E.frase(c, t, C["s01.d"], [("gira fácil", "g", 64, CERTO)], XE, 840)
            E.frase(c, t, lerp(C["s01.d"], C["s01.e"], 0.4), ps("mesma força. o que muda é", "i", 66), XE, 1000, "left", 0.1)
            E.frase(c, t, C["s01.e"], [("a distância", "g", 80, COR)], XE + 760, 1000)
        E.saida(c, t, C["s02"] - 0.1, um)
        return
    promessa(c, t, C, "s02", (("s02.a", "o torque"), ("s02.b", "equilibrar a gangorra"), ("s02.c", "as 2 condições")))


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    lembrete(c, t, C, "s03", (("s03.b", "força resultante zero:", "parado continua parado"),
                              ("s03.c", "o peso:", "P = m · g, com g = 10 m/s²")), 2)


# ---------------- torque ----------------
def barra_presa(c, t, t0, px, py, L, ang, a=1.0):
    """barra presa num pino em (px, py)"""
    tabua(c, px + L / 2 * math.cos(math.radians(ang)), py + L / 2 * math.sin(math.radians(ang)), L, ang, a)
    c.drawCircle(px, py, 20, M.paint(TINTA, a))
    c.drawCircle(px, py, 8, M.paint(E.COR, a))


def b_torque(c, t, C, b):
    if t < C["s05"]:
        def s04():
            # empurrar: o bloco desliza
            E.frase(c, t, C["s04.a"], [("empurrar", "g", 76, TINTA)], XE, 260)
            dx = 240 * ease_io(prog(t, C["s04.a"] + 0.8, 1.2))
            E.foco(c, t, C["s04.a"], 0.5, lambda a: F.bloco(c, 400 + dx, 520, 180, 150, None, a=a))
            if t >= C["s04.a"]:
                F.chao(c, 180, 900, 595, ep(t, C["s04.a"], 0.4))
            F.forca(c, t, C["s04.a"] + 0.4, (160 + dx, 520), 0, 140, "F")
            # girar: a barra presa no pino
            E.frase(c, t, C["s04.b"], [("girar", "g", 76, COR)], 1100, 260)
            ang = -35 * ease_io(prog(t, C["s04.b"] + 0.8, 1.4))
            E.foco(c, t, C["s04.b"], 0.5, lambda a: barra_presa(c, t, 0, 1160, 560, 600, ang, a))
            if t >= C["s04.b"] + 0.3:
                P = ponto_tabua(1160, 560, 520, ang)
                empurra(c, t, C["s04.b"] + 0.3, (P[0] - 14 * math.sin(math.radians(ang)), P[1] + 14 * math.cos(math.radians(ang))), 90 - ang, 150, "F")
            pilula_em(c, t, C["s04.c"], "eixo de rotação", 1160, 700, 50, TINTA)
            E.foco(c, t, C["s04.c"], 0.4, lambda a: M.line(c, 1160, 660, 1160, 590, TINTA, a, 4))
        E.saida(c, t, C["s05"] - 0.1, s04)
        return
    if t < C["s06"]:
        def s05():
            E.frase(c, t, C["s05.a"], [("torque", "g", 110, COR)], XE, 230)
            E.frase(c, t, C["s05.a"] + 0.5, ps("ou momento da força", "i", 66, TINTA2), XE + 420, 230, passo=0.1)
            E.frase(c, t, C["s05.b"], ps("força", "i", 70) + [("×", "g", 64, TINTA2)] + ps("braço", "i", 70), XE, 350, passo=0.12)
            F.formula_legenda(c, t, C["s05.c"], "M = F · d", [("F", "força", "N"), ("d", "braço", "m"), ("M", "torque", "N·m")],
                              XE, 540, 140, tl=[C["s05.d"], C["s05.e"], C["s05.f"]], size_l=54)
            # o braço no desenho: do eixo até a linha da força
            px, py, Lb = 1150, 520, 600
            q = ep(t, C["s05.b"], 0.5)
            if q > 0:
                barra_presa(c, t, 0, px, py, Lb, 0, q)
            F.forca(c, t, C["s05.d"], (px + 520, py - 190), -90, 170, "F")
            if t >= C["s05.e"]:
                M.line(c, px + 520, py - 260, px + 520, py + 230, TINTA2, 0.7 * ep(t, C["s05.e"], 0.4), 4, dash=E.TRACO)
            cota(c, t, C["s05.e"] + 0.3, (px, py + 110), (px + 520, py + 110), "d", lado=1, size=56)
            E.foco(c, t, C["s05.e"] + 0.8, 0.4, lambda a: centro(c, "linha da força", px + 520, py + 290, 42, "i", TINTA2, a))
        E.saida(c, t, C["s06"] - 0.1, s05)
        return
    # s06 e s07: a porta vista de cima, com as contas
    hx, hy, L = 700, 360, 900
    k = L / 1.0  # 900 px = 1 m
    if t < C["s07"]:
        def s06():
            E.foco(c, t, C["s06"], 0.5, lambda a: porta(c, hx, hy, L, 0, a, paredes=False))
            E.frase(c, t, C["s06"] + 0.3, ps("em ângulo reto: braço = até onde você empurra", "i", 52, TINTA2), XE, 140, passo=0.06)
            x1 = hx + 0.8 * k
            empurra(c, t, C["s06.a"], (x1, hy + 14), 90, 170, None, "20 N")
            cota(c, t, C["s06.b"], (hx, hy - 80), (x1, hy - 80), "0,8 m", size=50)
            E.formula_em(c, t, C["s06.c"], "M = 20 · 0,8", XE, 700, 84, "g", TINTA)
            E.foco(c, t, C["s06.d"], 0.4, lambda a: E.formula(c, "= 16 N·m", XE + E.formula(None, "M = 20 · 0,8 ", 0, 0, 84, a=0), 700, 84, "g", COR, a))
            x2 = hx + 0.1 * k
            empurra(c, t, C["s06.e"], (x2, hy + 14), 90, 170, None, "20 N")
            E.formula_em(c, t, C["s06.f"], "a 0,1 m:  M = 20 · 0,1 = 2 N·m", XE, 840, 84, "g", TINTA)
            E.frase(c, t, C["s06.f"] + 1.2, [("8 vezes", "g", 76, ERRADO)] + ps("menos giro", "i", 80), XE, 990, passo=0.12)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    # s07: empurrar na direção da dobradiça: braço zero
    E.foco(c, t, C["s07"], 0.5, lambda a: porta(c, hx, hy, L, 0, a, paredes=False))
    F.vetor(c, t, C["s07.a"], (hx + L + 220, hy), (hx + L + 10, hy), None, None, E.COR, 10)
    E.foco(c, t, C["s07.a"] + 0.4, 0.4, lambda a: E.escreve(c, "F", hx + L + 90, hy - 40, 60, "g", COR, a))
    if t >= C["s07.b"]:
        M.line(c, hx - 120, hy, hx + L + 240, hy, TINTA2, 0.8 * ep(t, C["s07.b"], 0.5), 4, dash=E.TRACO)
        q = ep(t, C["s07.b"] + 0.4, 0.4) * (0.6 + 0.4 * math.sin(t * 5))
        c.drawCircle(hx, hy, 46, M.paint(E.COR, q, stroke=6))
    E.frase(c, t, C["s07.a"], ps("na direção da dobradiça", "i", 70), XE, 620, passo=0.1)
    E.frase(c, t, C["s07.b"], [("braço", "i", 76), ("=", "g", 76, TINTA2), ("0", "g", 90, COR)], XE, 760, passo=0.12)
    E.frase(c, t, C["s07.b"] + 1.4, [("torque", "i", 76), ("=", "g", 76, TINTA2), ("0", "g", 90, COR)], XE + 560, 760, passo=0.12)
    E.frase(c, t, C["s07.c"], ps("a porta", "i", 80) + [("não gira", "g", 80, ERRADO)], XE, 900, passo=0.12)


# ---------------- gangorra ----------------
GX, GY, GL, GK = 960, 700, 1300, 250  # eixo da gangorra, comprimento e pixels por metro


def b_gangorra(c, t, C, b):
    if t < C["s09"]:
        def s08():
            E.frase(c, t, C["s08.a"], ps("todo torque tem um", "i", 76) + [("sentido de giro", "g", 76, COR)], XE, 200, passo=0.12)
            E.foco(c, t, C["s08.b"], 0.5, lambda a: (seta_giro(c, 1460, 430, 90, -150, 300, E.COR, a, p=ep(t, C["s08.b"], 0.8)),
                                                      centro(c, "horário", 1460, 590, 52, "g", COR, a)))
            E.foco(c, t, C["s08.c"], 0.5, lambda a: (seta_giro(c, 460, 430, 90, -30, -300, F.NEG, a, p=ep(t, C["s08.c"], 0.8)),
                                                      centro(c, "anti-horário", 460, 590, 52, "g", F.NEG, a)))
            if t >= C["s08.d"] - 1.5:
                gangorra(c, t, C["s08.d"] - 1.5, GX, GY + 60, GL)
            for k_, u, m in (("s08.d", -2 * GK, "30 kg"), ("s08.e", 2 * GK, "60 kg")):
                cx, cy = sobre(GX, GY + 60, u, 0, 110)
                E.foco(c, t, C[k_], 0.5, lambda a, cx=cx, cy=cy, m=m: F.bloco(c, cx, cy, 130, 110, m, a=a))
                F.forca(c, t, C[k_] + 0.4, (cx, cy - 30), -90, 130, "P", lado=-1)
        E.saida(c, t, C["s09"] - 0.1, s08)
        return
    if t < C["s10"]:
        def s09():
            E.frase(c, t, C["s09.a"], ps("em equilíbrio, os giros", "i", 76) + [("empatam", "g", 76, COR)], W / 2, 260, "center", 0.12)
            tb_ = C["s09.b"]
            E.linha(c, t, [("torque anti-horário", "g", 72, F.NEG, tb_ + 1.0), ("=", "g", 72, TINTA2, tb_ + 0.7), ("torque horário", "g", 72, COR, tb_)], W / 2, 480, "center")
            E.formula_em(c, t, C["s09.c"] + 1.2, "P · d", W / 2 - 300, 720, 120, "g", F.NEG, "center")
            E.formula_em(c, t, C["s09.c"] + 0.8, "=", W / 2, 720, 120, "g", TINTA2, "center")
            E.formula_em(c, t, C["s09.c"], "P · d", W / 2 + 300, 720, 120, "g", COR, "center")
            E.foco(c, t, C["s09.c"] + 1.6, 0.4, lambda a: centro(c, "lado esquerdo", W / 2 - 300, 830, 50, "i", TINTA2, a))
            E.foco(c, t, C["s09.c"] + 0.4, 0.4, lambda a: centro(c, "lado direito", W / 2 + 300, 830, 50, "i", TINTA2, a))
        E.saida(c, t, C["s10"] - 0.1, s09)
        return
    # s10: 30 kg a 2 m; 60 kg a 1 m
    gangorra(c, t, C["s10"], GX, GY, GL)
    cx1, cy1 = sobre(GX, GY, -2 * GK, 0, 110)
    E.foco(c, t, C["s10.a"], 0.5, lambda a: F.bloco(c, cx1, cy1, 130, 110, "30 kg", a=a))
    cota(c, t, C["s10.a"] + 0.4, (GX - 2 * GK, GY + 150), (GX, GY + 150), "2 m", lado=1)
    cx2, cy2 = sobre(GX, GY, 1 * GK, 0, 110)
    E.foco(c, t, C["s10.b"], 0.5, lambda a: F.bloco(c, cx2, cy2, 130, 110, "60 kg", a=a, cor=E.mix(E.COR, BR, 0.35) if t < C["s10.f"] else None))
    if C["s10.b"] <= t < C["s10.f"]:
        E.foco(c, t, C["s10.b"] + 0.3, 0.4, lambda a: centro(c, "?", cx2, cy2 - 100, 70, "g", COR, a))
    cota(c, t, C["s10.f"], (GX, GY + 150), (GX + GK, GY + 150), "d = 1 m", lado=1)
    E.formula_em(c, t, C["s10.c"], "P = 300 N  e  600 N", XE, 230, 66, "b", TINTA2)
    E.formula_em(c, t, C["s10.d"], "300 · 2", XE, 360, 96, "g", F.NEG)
    E.formula_em(c, t, C["s10.e"] - 0.3, "=", XE + 380, 360, 96, "g", TINTA2)
    E.formula_em(c, t, C["s10.e"], "600 · d", XE + 480, 360, 96, "g", COR)
    bola_txt(c, t, C["s10.f"], "d = 1 m", 1500, 330, 120, 56)
    E.frase(c, t, C["s10.g"], ps("o dobro da massa,", "i", 60) + [("metade da distância", "g", 56, COR)], XE, 470, passo=0.1)


# ---------------- equilíbrio ----------------
def b_equilibrio(c, t, C, b):
    if t < C["s12"]:
        def s11():
            gangorra(c, t, C["s11"] - 0.2, GX, GY, GL)
            for u, m in ((-2 * GK, "30 kg"), (GK, "60 kg")):
                cx, cy = sobre(GX, GY, u, 0, 110)
                F.bloco(c, cx, cy, 130, 110, m, a=ep(t, C["s11"] - 0.2, 0.4))
                F.forca(c, t, C["s11"] + 0.2, (cx, cy), -90, 80 if m == "30 kg" else 160, None, modulo="300 N" if m == "30 kg" else "600 N", size=46, lado=-1)
            F.forca(c, t, C["s11.a"], (GX, GY - 13), 90, 300, "N", lado=-1)
            E.frase(c, t, C["s11"], ps("parar de girar", "i", 70) + [("não basta", "g", 70, ERRADO)], XE, 200, passo=0.12)
            E.frase(c, t, C["s11.b"], ps("apoio = soma dos pesos", "i", 64), XE, 320, passo=0.1)
            E.formula_em(c, t, C["s11.c"], "N = 300 + 600 = 900 N", 1050, 320, 70, "g", COR)
        E.saida(c, t, C["s12"] - 0.1, s11)
        return
    if t < C["s13"]:
        def s12():
            E.frase(c, t, C["s12.a"], ps("equilíbrio:", "i", 84) + [("duas condições", "g", 84, COR)], W / 2, 200, "center", 0.12)
            for i, (k_, l1, l2, l3) in enumerate((("s12.b", "1", "força resultante = 0", "não sai do lugar"),
                                                  ("s12.c", "2", "torque total = 0", "não gira"))):
                x = 190 + i * 800
                p = ep(t, C[k_], 0.5)
                E.caixa_pontilhada(c, x, 320, 740, 420, p, prog_=p)
                E.foco(c, t, C[k_], 0.5, lambda a, x=x, l1=l1: (E.bola(c, x + 90, 420, 54, a=a), centro(c, l1, x + 90, 444, 64, "g", BR, a)))
                E.frase(c, t, C[k_] + 0.2, [(l2, "g", 60)], x + 60, 580)
                E.frase(c, t, C[k_] + 0.6, ps(l3, "i", 60, COR), x + 60, 680, passo=0.1)
            E.frase(c, t, C["s12.d"], ps("faltou uma:", "i", 76) + [("o corpo se mexe", "g", 72, ERRADO)], W / 2, 900, "center", 0.12)
        E.saida(c, t, C["s13"] - 0.1, s12)
        return
    # s13: alavancas
    E.frase(c, t, C["s13.a"], ps("a gangorra é uma", "i", 80) + [("alavanca", "g", 84, COR)], XE, 220, passo=0.12)
    E.frase(c, t, C["s13.a"] + 1.0, ps("barra que gira num apoio", "i", 60, TINTA2), XE, 320, passo=0.1)
    for i, (k_, s) in enumerate((("s13.b", "pé de cabra"), ("s13.c", "carrinho de mão"), ("s13.d", "abridor de garrafa"))):
        x = XE + [0, 420, 960][i]
        E.foco(c, t, C[k_], 0.4, lambda a, s=s, x=x: E.pilula(c, s, x + (E.larg(s, "g", 44) + 48) / 2, 430, 44, "g", fundo=TINTA, a=a))
    # braço curto para a carga, braço comprido para a sua força
    ax, ay = 760, 840
    q = ep(t, C["s13.e"] - 0.6, 0.5)
    if q > 0:
        apoio(c, ax, ay + 13, 70, q)
        tabua(c, ax + 250, ay, 1260, 0, q)
        F.chao(c, ax - 520, ax + 1000, ay + 83, q * 0.8)
        cx, cy = sobre(ax, ay, -260, 0, 150)
        F.bloco(c, cx, cy, 170, 150, "carga", a=q, size=40)
    cx, cy = sobre(ax, ay, -260, 0, 150)
    F.forca(c, t, C["s13.e"] + 0.8, (cx, cy - 330), -90, 245, None)
    E.foco(c, t, C["s13.e"] + 1.0, 0.4, lambda a: E.escreve(c, "força grande", cx + 30, cy - 200, 46, "b", COR, a))
    F.forca(c, t, C["s13.e"], (ax + 820, ay - 170), -90, 155, None)
    E.foco(c, t, C["s13.e"] + 0.2, 0.4, lambda a: E.escreve(c, "força pequena", ax + 800 - E.larg("força pequena", "b", 46), ay - 110, 46, "b", COR, a))
    cota(c, t, C["s13.e"] + 0.3, (ax, ay + 140), (ax + 820, ay + 140), "braço comprido", lado=1, size=42)
    cota(c, t, C["s13.e"] + 1.0, (ax - 260, ay + 140), (ax, ay + 140), "curto", lado=1, size=42)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("medir da ponta da barra", "i", 70), XE + 480, 190, passo=0.12)
    k = 250
    x0, y = 335, 640
    xa = x0 + 1.5 * k
    q = ep(t, C["s14.b"], 0.6)
    if q > 0:
        tabua(c, x0 + 2.5 * k, y, 5 * k * ease_io(q), 0, q)
    cota(c, t, C["s14.b"] + 0.3, (x0, y - 300), (x0 + 5 * k, y - 300), "5 m", size=50)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: (apoio(c, xa, y + 13, 80, a), F.chao(c, x0 - 40, x0 + 5 * k + 40, y + 93, a * 0.8)))
    cota(c, t, C["s14.c"] + 0.3, (x0, y + 160), (xa, y + 160), "1,5 m", lado=1, size=46)
    cx, cy = sobre(x0 + 5 * k - 70, y, 0, 0, 100)
    E.foco(c, t, C["s14.d"], 0.5, lambda a: F.bloco(c, cx, cy, 120, 100, None, a=a))
    if C["s14.d"] + 0.5 <= t:
        E.foco(c, t, C["s14.d"] + 0.5, 0.4, lambda a: centro(c, "5 m?", cx, cy - 110, 64, "g", ERRADO, a))
        E.risco(c, cx - 80, cy - 100, cx + 80, cy - 160, t, C["s14.d"] + 1.6, largura=10)
    cota(c, t, C["s14.e"], (xa, y + 250), (x0 + 5 * k, y + 250), "3,5 m", lado=-1, size=56, cor=CERTO, cor_txt=CERTO)
    E.frase(c, t, C["s14.f"], ps("o braço começa", "i", 66) + [("no eixo", "g", 66, COR)], 1300, 1020, "center", 0.12)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s16"]:
        def s15():
            E.frase(c, t, C["s15"], ps("o atalho de prova", "i", 76, CLARO), W / 2, 180, "center")
            E.frase(c, t, C["s15.a"], ps("na gangorra,", "i", 76, CLARO) + [("nem calcule o peso", "g", 76, BR)], W / 2, 330, "center", 0.12)
            E.formula_em(c, t, C["s15.a"] + 1.2, "30 · 10 · 2 = 60 · 10 · d", W / 2, 540, 110, "g", BR, "center")
            if t >= C["s15.b"]:
                w = E.formula(None, "30 · 10 · 2 = 60 · 10 · d", 0, 0, 110, a=0)
                x0 = W / 2 - w / 2
                for pre in ("30 · ", "30 · 10 · 2 = 60 · "):
                    xa = x0 + E.formula(None, pre, 0, 0, 110, a=0)
                    wb = E.formula(None, "10", 0, 0, 110, a=0)
                    E.risco(c, xa - 8, 560, xa + wb + 8, 460, t, C["s15.b"] + (0 if pre == "30 · " else 0.25), cor=CLARO, largura=10)
            E.formula_em(c, t, C["s15.c"], "30 · 2 = 60 · d", W / 2, 740, 110, "g", CLARO, "center")
            bola_txt(c, t, lerp(C["s15.c"], C["s15.end"], 0.7), "d = 1 m", W / 2, 910, 105, 50)
        E.saida(c, t, C["s16"] - 0.1, s15)
        return
    E.frase(c, t, C["s16"], ps("repare na proporção", "i", 76, CLARO), W / 2, 180, "center")
    for i, (k_, a1, a2) in enumerate((("s16.a", "2 × a massa", "½ da distância"), ("s16.b", "3 × a massa", "⅓ da distância"))):
        y = 360 + i * 150
        E.frase(c, t, C[k_], [(a1, "g", 76, BR), ("→", "g", 76, CLARO), (a2, "g", 76, CLARO)], W / 2, y, "center", 0.2)
    E.frase(c, t, C["s16.c"], [("cortar o 10:", "g", 58, BR)] + ps("só quando todas as forças são pesos", "i", 60, CLARO), W / 2, 780, "center", 0.08)
    E.frase(c, t, C["s16.c"] + 2.6, [("proporção:", "g", 58, BR)] + ps("só com duas forças; com mais, some", "i", 60, CLARO), W / 2, 900, "center", 0.08)


# ---------------- questão ----------------
QX, QY = 1230, 700


def cena_barra(c, t, ta, tb, tc, mostra_f=True):
    """a barra da questão: caixa de 600 N a 0,3 m do apoio, força F a 1,5 m"""
    k = 250
    q = ep(t, ta, 0.5)
    if q > 0:
        apoio(c, QX, QY + 13, 70, q)
        tabua(c, QX + 0.6 * k, QY, 2.1 * k + 120, 0, q)
        F.chao(c, QX - 0.3 * k - 160, QX + 1.5 * k + 160, QY + 83, q * 0.8)
    cx, cy = sobre(QX, QY, -0.3 * k, 0, 120)
    E.foco(c, t, tb, 0.5, lambda a: F.bloco(c, cx - 20, cy, 150, 120, "600 N", a=a, size=40))
    cota(c, t, tb + 0.3, (QX - 0.3 * k, QY + 140), (QX, QY + 140), "0,3 m", lado=1, size=40)
    if mostra_f:
        F.forca(c, t, tc, (QX + 1.5 * k, QY - 200), -90, 185, "F")
    cota(c, t, tc + 0.3, (QX, QY + 230), (QX + 1.5 * k, QY + 230), "1,5 m", lado=1, size=44)


def b_questao(c, t, C, b):
    hora_testar(c, t, C, "s17")
    E.frase(c, t, C["s17.a"], ps("barra leve num apoio", "i", 66), XE, 300, passo=0.1)
    E.frase(c, t, C["s17.b"], [("caixa", "i", 66), ("600 N", "g", 66, COR), ("a", "i", 66), ("30 cm", "g", 66)], XE, 410, passo=0.12)
    E.frase(c, t, C["s17.c"], [("você empurra a", "i", 66), ("1,5 m", "g", 66)], XE, 520, passo=0.12)
    E.frase(c, t, C["s17.d"], ps("que força", "i", 76) + [("F?", "g", 76, COR)], XE, 680, passo=0.12)
    E.frase(c, t, C["s17.e"], ps("torque da caixa?", "i", 76), XE, 800, passo=0.12)
    if t < C["s18"]:
        cena_barra(c, t, C["s17.a"], C["s17.b"], C["s17.c"])
    else:
        E.relogio(c, t, C["s18.a"], cx=1480, cy=440, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    if t < C["s20"]:
        def s19():
            linhas(c, t, [(C["s19.a"], "30 cm = 0,3 m", TINTA2),
                          (C["s19.b"], "M = 600 · 0,3", TINTA),
                          (C["s19.d"], "F · 1,5 = 180", TINTA),
                          (C["s19.e"], "F = 180 ÷ 1,5", TINTA)], XE, 230, 150, 84)
            E.foco(c, t, C["s19.c"], 0.4, lambda a: E.formula(c, "= 180 N·m", XE + E.formula(None, "M = 600 · 0,3 ", 0, 0, 84, a=0), 380, 84, "g", COR, a))
            bola_txt(c, t, C["s19.f"], "120 N", 1450, 560, 170, 90, CERTO)
        E.saida(c, t, C["s20"] - 0.1, s19)
        return
    E.frase(c, t, C["s20"], ps("confira pela proporção", "i", 76, COR), XE, 220)
    cena_barra(c, t, C["s20"], C["s20"], C["s20"] + 0.2)
    E.frase(c, t, C["s20.a"], [("braço", "i", 72), ("5 ×", "g", 72, COR), ("maior", "i", 72)], XE, 400, passo=0.12)
    E.frase(c, t, C["s20.b"], [("força", "i", 72), ("5 ×", "g", 72, COR), ("menor", "i", 72)], XE, 520, passo=0.12)
    E.formula_em(c, t, C["s20.c"] - 0.6, "600 ÷ 5 =", XE, 690, 84, "g", TINTA)
    bola_txt(c, t, C["s20.c"], "120 N", XE + 590, 660, 105, 54, CERTO)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    if t < C["s22"]:
        E.saida(c, t, C["s22"] - 0.1, lambda: resumo(c, t, C, "s21", (
            ("s21.a", [("torque", "g", 66), ("=", "g", 66, TINTA2), ("força × braço,", "i", 70), ("do eixo", "g", 66, COR)]),
            ("s21.b", [("horário", "g", 66, COR), ("=", "g", 66, TINTA2), ("anti-horário", "g", 66, F.NEG)]),
            ("s21.c", [("resultante = 0", "g", 62), ("e", "i", 66), ("torque total = 0", "g", 62, COR)]))))
        return

    def desenho():
        cx, cy = 820, 830
        q = ep(t, C["s22.b"], 0.6)
        if q <= 0:
            return
        pt = M.paint(TINTA, 0.8 * q, stroke=4)
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawOval(skia.Rect.MakeXYWH(cx - 420 * q, cy - 170 * q, 840 * q, 340 * q), pt)
        E.bola(c, cx - 150, cy, 70 * q, SOL, q)
        g = t * 0.9
        E.bola(c, cx + 420 * math.cos(g), cy + 170 * math.sin(g), 30 * q, TERRA, q)
    proxima(c, t, C, "s22", [("Leis", "g", 120, COR), ("de", "i", 110), ("Kepler", "g", 120, COR)], None, desenho)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, torque=b_torque, gangorra=b_gangorra, equilibrio=b_equilibrio, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
