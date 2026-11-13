"""Visual — Estudativo · QUI-ATO-003: modelo de Bohr, saltos e cores.
Segue a linguagem visual da Química (QUI-MIS-001) e a da trilha (cabeçalho de QUI-ATO-001). Nesta aula:
- CAMADAS = círculos finos em volta do núcleo turquesa, com a letra (K, L, M...) no alto à direita; o elétron da vez é a
  bolinha azul com contorno claro. Escada = a mesma ideia de lado: degrau mais alto, mais energia.
- LUZ EMITIDA = onda que sai do átomo NA COR DA LUZ (vermelho do estrôncio, verde do bário, amarelo do sódio,
  verde-azulado do cobre). Energia recebida = raio âmbar que chega; energia devolvida = onda colorida que sai.
Todo instante vem de C[...] (marcadores do roteiro)."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Átomo e Tabela Periódica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ATO-003_bohr_saltos_e_cores.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("problema", "niveis", "salto", "cores", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#F2A33A"
LUZ = dict(Sr="#E8352E", Ba="#3DBE4C", Na="#F7C81E", Cu="#1FB5A5")


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def eletron(c, x, y, r=16, a=1.0, destaque=False):
    if destaque:
        c.drawCircle(x, y, r + 8, M.paint(AMBAR, 0.9 * a, stroke=4))
    E.bola(c, x, y, r, Q.ELETRON, a)
    if r >= 12:
        M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, a, max(3, r * 0.16))


def fogos(c, t, t0, cx, cy, r, cor, n=16, a=1.0):
    """explosão de fogos: raios que crescem e pontinhos que caem e apagam (repete a cada 2,6 s)"""
    if t < t0 or a <= 0:
        return
    u = ((t - t0) % 2.6) / 1.6
    if u > 1:
        return
    e = ease_out(u)
    fade = a * (1 - max(0, (u - 0.55) / 0.45))
    for k in range(n):
        g = math.tau * k / n + 0.2
        x1, y1 = cx + r * e * math.cos(g), cy + r * e * math.sin(g) + 40 * u * u
        x0, y0 = cx + r * e * 0.55 * math.cos(g), cy + r * e * 0.55 * math.sin(g) + 20 * u * u
        M.line(c, x0, y0, x1, y1, cor, fade, 6)
        c.drawCircle(x1, y1, 8, M.paint(cor, fade))
    c.drawCircle(cx, cy, r * 0.25 * (1 - u), M.paint(BR, 0.8 * fade))


def onda(c, x0, y0, ang, L, cor, a=1.0, p=1.0, amp=16, lam=46):
    """onda de luz saindo de (x0, y0) na direção ang (graus), comprimento L"""
    if a <= 0 or p <= 0:
        return
    g = math.radians(ang)
    ux, uy, nx, ny = math.cos(g), math.sin(g), -math.sin(g), math.cos(g)
    pth = skia.Path()
    for k in range(int(L * p / 4) + 1):
        s = k * 4
        w = amp * math.sin(s / lam * math.tau)
        x, y = x0 + ux * s + nx * w, y0 + uy * s + ny * w
        pth.moveTo(x, y) if k == 0 else pth.lineTo(x, y)
    c.drawPath(pth, M.paint(cor, a, stroke=6, cap_round=True))


def atomo_salto(c, t, cx, cy, ts, tv, R=(110, 190, 270), cor_luz=None, a=1.0, letras=True, energia=True, escuro=False):
    """núcleo + 3 camadas; um elétron sobe da camada 1 para a 3 em ts (recebe energia) e volta em tv (solta luz)"""
    if a <= 0:
        return
    tinta = BR if escuro else TINTA2
    for i, r in enumerate(R):
        c.drawCircle(cx, cy, r, M.paint(tinta, 0.6 * a, stroke=3))
        if letras:
            E.formula(c, "KLM"[i], cx + r * 0.71 + 12, cy - r * 0.71 - 6, 40, "b", tinta, a)
    E.bola(c, cx, cy, 44, E.COR, a)
    # outros elétrons parados
    for i, (r, n) in enumerate(zip(R[:2], (2, 3))):
        for j in range(n):
            g = math.tau * j / n + 1.2 + i
            if i == 0 and j == 0:
                continue
            eletron(c, cx + r * math.cos(g), cy + r * math.sin(g), 13, a)
    # o elétron da vez
    g0 = 1.2
    sobe = ease_io(prog(t, ts, 0.6)) if ts is not None else 0
    volta = ease_io(prog(t, tv, 0.6)) if tv is not None else 0
    r = lerp(R[0], R[2], sobe * (1 - volta))
    x, y = cx + r * math.cos(g0), cy + r * math.sin(g0)
    if energia and ts is not None and t >= ts - 0.7 and t < ts + 0.2:
        q = ep(t, ts - 0.7, 0.3)
        p = ease_io(prog(t, ts - 0.7, 0.6))
        M.arrow(c, x + 260, y + 160, lerp(x + 260, x + 30, p), lerp(y + 160, y + 20, p), AMBAR, q, 7, 24)
    eletron(c, x, y, 17, a, destaque=True)
    if tv is not None and t >= tv:
        p = ease_out(prog(t, tv + 0.2, 1.0))
        onda(c, x + 30, y - 10, -30, 420, cor_luz or LUZ["Na"], a * (1 - ep(t, tv + 2.6, 0.6)), p)
    return x, y


def chama(c, cx, yb, w, h, cor, a=1.0, t=0.0):
    """chama de bico de gás: gota que tremula, com miolo azulado"""
    if a <= 0:
        return
    k = 1 + 0.04 * math.sin(t * 9)
    pth = skia.Path()
    pth.moveTo(cx - w / 2, yb)
    pth.cubicTo(cx - w * 0.7, yb - h * 0.5 * k, cx - w * 0.1, yb - h * 0.7 * k, cx, yb - h * k)
    pth.cubicTo(cx + w * 0.1, yb - h * 0.7 * k, cx + w * 0.7, yb - h * 0.5 * k, cx + w / 2, yb)
    pth.close()
    pnt = skia.Paint(AntiAlias=True)
    pnt.setShader(skia.GradientShader.MakeLinear([skia.Point(0, yb), skia.Point(0, yb - h)], [M.hexc("#5B8DEF", a), M.hexc(cor, a), M.hexc(cor, 0.0)], [0, 0.35, 1]))
    c.drawPath(pth, pnt)
    M.rrect(c, cx - w * 0.22, yb, w * 0.44, 120, 8, "#8A8D96", a)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        for k, (el, x, y) in enumerate((("Sr", 1250, 380), ("Ba", 1600, 300), ("Na", 1470, 640))):
            fogos(c, t, C["s01.a"] + 0.4 * k, x, y, 170, LUZ[el])
        E.frase(c, t, C["s01.a"], [("vermelhos,", "g", 70, LUZ["Sr"]), ("verdes,", "g", 70, LUZ["Ba"]), ("amarelos", "g", 70, "#D9A400")], XE, 260, passo=0.25)
        E.frase(c, t, C["s01.b"], ps("as cores", "i", 76) + [("não", "g", 72, ERRADO)] + ps("vêm de tinta", "i", 76), XE, 420, passo=0.12)
        E.frase(c, t, C["s01.c"], ps("vêm dos", "i", 90) + [("elétrons", "g", 90, Q.ELETRON)], XE, 620, passo=0.12)
        E.frase(c, t, C["s01.d"], ps("pulando dentro do átomo", "i", 66, TINTA2), XE, 740, passo=0.1)
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02"] + 0.1, ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.a"], [("a cor dos", "i", 74), ("fogos", "g", 70)]),
                 (C["s02.b"], [("o", "i", 74), ("teste de chama", "g", 70)]),
                 (C["s02.c"], [("com o modelo de", "i", 74), ("Bohr", "g", 70, COR)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula anterior", "i", 70, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("núcleo", "g", 76, COR)] + ps("pequeno e positivo", "i", 76), XE, 400, passo=0.12)
    E.frase(c, t, C["s03.b"], [("eletrosfera", "g", 76, Q.ELETRON)] + ps("com os elétrons", "i", 76), XE, 540, passo=0.12)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.bola(c, 1500, 560, 30, E.COR, a))
    if t >= C["s03.b"]:
        q = ep(t, C["s03.b"], 0.5)
        c.drawCircle(1500, 560, 300, M.paint(Q.ELETRON, 0.08 * q))
        for k in range(5):
            g = t * 0.6 + k * 1.3
            eletron(c, 1500 + 230 * math.cos(g), 560 + 180 * math.sin(g * 1.1), 16, q)


# ---------------- o problema de Rutherford ----------------
def b_problema(c, t, C, b):
    E.frase(c, t, C["s04"], ps("no modelo de Rutherford, os elétrons", "i", 60, TINTA2), XE, 180, passo=0.08)
    E.frase(c, t, C["s04"] + 1.6, ps("giram como", "i", 60, TINTA2) + [("planetas", "g", 58)], XE, 260, passo=0.08)
    E.frase(c, t, C["s04.a"], [("um problema", "g", 80, ERRADO)], XE, 420)
    cx, cy = 1400, 600
    E.foco(c, t, C["s04"] + 0.3, 0.5, lambda a: E.bola(c, cx, cy, 40, E.COR, a))
    # o elétron gira e, a partir de s04.b, cai em espiral
    if t >= C["s04"] + 0.3:
        tq = C["s04.b"]
        cai = ease_io(prog(t, tq, 3.0))
        r = lerp(300, 50, cai)
        g = (t - C["s04"]) * (1.6 + 3 * cai)
        # rastro da espiral
        if t >= tq:
            pth = skia.Path()
            for k in range(80):
                u = cai * k / 79
                rr = lerp(300, 50, u)
                gg = (tq - C["s04"]) * 1.6 + u * 3.0 * (1.6 + 3 * u) * 2.2
                x, y = cx + rr * math.cos(gg), cy + rr * math.sin(gg)
                pth.moveTo(x, y) if k == 0 else pth.lineTo(x, y)
            c.drawPath(pth, M.paint(Q.ELETRON, 0.35, stroke=4))
        eletron(c, cx + r * math.cos(g), cy + r * math.sin(g), 20)
    E.frase(c, t, C["s04.b"], ps("perderia energia", "i", 64), XE, 560, passo=0.1)
    E.frase(c, t, C["s04.c"], ps("e cairia no núcleo, em", "i", 64) + [("espiral", "g", 60, Q.ELETRON)], XE, 660, passo=0.1)
    E.frase(c, t, C["s04.d"], ps("o átomo desmontaria", "i", 64), XE, 820, passo=0.1)
    E.frase(c, t, C["s04.d"] + 2.0, ps("mas os átomos", "i", 64) + [("não desmontam", "g", 60, COR)], XE, 920, passo=0.1)


# ---------------- os níveis ----------------
def escada(c, x, yb, n, dw, dh, a=1.0, letras="KLMNOPQ"):
    """escada de degraus: degrau i no alto em y = yb - i*dh; devolve o ponto em cima de cada degrau"""
    pts = []
    for i in range(n):
        y = yb - i * dh
        M.rrect(c, x + i * dw, y, dw + 8, yb - y + 30, 6, E.mix(E.COR, "#FFFFFF", 0.75 - 0.08 * i), a)
        E.formula(c, letras[i], x + i * dw + dw / 2, y + 60, 46, "g", COR, a, "center")
        pts.append((x + i * dw + dw / 2, y - 22))
    return pts


def b_niveis(c, t, C, b):
    if t < C["s06"]:
        E.foco(c, t, C["s05"] + 0.2, 0.4, lambda a: E.escreve(c, "1913", XE, 180, 54, "i", TINTA2, a))
        E.frase(c, t, C["s05.a"], [("Niels", "g", 80), ("Bohr", "g", 80, COR)], XE + 170, 180, passo=0.15)
        E.frase(c, t, C["s05.b"], ps("o elétron só fica em", "i", 64) + [("certos níveis", "g", 60)], XE, 320, passo=0.1)
        E.frase(c, t, C["s05.c"], [("camadas", "g", 110, COR)], XE, 480)
        Q.bohr(c, t, C["s05.c"], 1400, 600, (2, 8, 8, 2), r0=110, dr=80, te=[C["s05.d"] + 0.4 * k for k in range(4)], nomes=True)
        if t >= C["s05.d"]:
            for k, s in enumerate("KLMN"):
                E.foco(c, t, C["s05.d"] + 0.4 * k, 0.4, lambda a, k=k, s=s: E.pilula(c, s, XE + 50 + k * 120, 640, 64, "g", fundo=TINTA, a=a))
            E.frase(c, t, C["s05.d"] + 1.8, ps("... até a sétima", "i", 56, TINTA2), XE + 490, 660, passo=0.1)
        E.frase(c, t, C["s05.e"], ps("camada", "i", 58) + [("1", "g", 56, COR)] + ps("é a K,", "i", 58) + [("2", "g", 56, COR)] + ps("é a L", "i", 58), XE, 820, passo=0.1)
        return
    # s06: a escada
    E.frase(c, t, C["s06.a"], ps("pense numa", "i", 72) + [("escada", "g", 70, COR)], XE, 200, passo=0.12)
    E.foco(c, t, C["s06.a"] + 0.3, 0.5, lambda a: escada(c, 900, 900, 4, 200, 150, a))
    pts = escada(c, 900, 900, 4, 200, 150, 0)
    # o elétron pula de degrau em degrau, sem parar no meio
    q = ep(t, C["s06.a"] + 0.6, 0.4)
    if q > 0:
        u = max(0, t - C["s06.a"] - 1.0)
        i = min(3, int(u / 1.1)) if t < C["s06.d"] else 1
        f = (u / 1.1) % 1 if t < C["s06.d"] and i < 3 else 1
        j = min(3, i + 1)
        if f < 0.6 or i == j:
            x, y = pts[i]
        else:
            v = (f - 0.6) / 0.4
            x = lerp(pts[i][0], pts[j][0], v); y = lerp(pts[i][1], pts[j][1], v) - 90 * math.sin(math.pi * v)
        eletron(c, x, y, 20, q, destaque=True)
    E.frase(c, t, C["s06.b"], ps("um degrau ou outro,", "i", 60) + [("nunca no meio", "g", 58)], XE, 330, passo=0.1)
    E.foco(c, t, C["s06.c"], 0.5, lambda a: (M.arrow(c, 1770, 920, 1770, 380, AMBAR, a, 7, 26), E.escreve(c, "mais energia", 1440, 350, 48, "g", AMBAR, a)))
    E.frase(c, t, C["s06.c"] + 0.3, ps("mais alto: mais longe do núcleo", "i", 54, TINTA2), XE, 450, passo=0.08)
    E.frase(c, t, C["s06.d"], ps("no degrau, ele", "i", 60) + [("não perde energia", "g", 58, COR)], XE, 600, passo=0.1)
    E.frase(c, t, C["s06.e"], ps("o átomo", "i", 60) + [("não desmonta", "g", 58)], XE, 700, passo=0.1)


# ---------------- o salto ----------------
AX, AY = 1380, 560


def b_salto(c, t, C, b):
    if t < C["s08"]:
        atomo_salto(c, t, AX, AY, C["s07.a"] + 0.8, None)
        E.frase(c, t, C["s07.a"], ps("para subir, o elétron", "i", 62) + [("recebe energia", "g", 58, AMBAR)], XE, 220, passo=0.1)
        E.frase(c, t, C["s07.b"], ps("na medida exata do salto", "i", 60, TINTA2), XE, 320, passo=0.1)
        E.frase(c, t, C["s07.c"], ps("calor de uma chama", "i", 58), XE, 460, passo=0.1)
        E.frase(c, t, C["s07.c"] + 1.4, ps("ou eletricidade", "i", 58), XE, 540, passo=0.1)
        E.frase(c, t, C["s07.d"], ps("lá em cima:", "i", 66) + [("excitado", "g", 66, AMBAR)], XE, 720, passo=0.1)
        E.frase(c, t, C["s07.e"], ps("instável, não dura", "i", 58, TINTA2), XE, 820, passo=0.1)
        return
    atomo_salto(c, t, AX, AY, C["s08"] - 3, C["s08.a"] + 0.3, cor_luz=LUZ["Na"], energia=False)
    E.frase(c, t, C["s08.a"], ps("o elétron", "i", 62) + [("volta", "g", 60, COR)], XE, 220, passo=0.1)
    E.frase(c, t, C["s08.b"], ps("e devolve a energia como", "i", 62) + [("luz", "g", 60, "#D9A400")], XE, 320, passo=0.1)
    E.frase(c, t, C["s08.c"], ps("a cor depende do", "i", 60) + [("tamanho do salto", "g", 58)], XE, 480, passo=0.1)
    E.frase(c, t, C["s08.d"], ps("cada elemento tem", "i", 60) + [("seus degraus", "g", 58, COR)], XE, 640, passo=0.1)
    E.frase(c, t, C["s08.e"], ps("cada elemento,", "i", 64) + [("sua cor", "g", 62, COR)], XE, 800, passo=0.1)
    for k, el in enumerate(("Sr", "Ba", "Na", "Cu")):
        E.foco(c, t, C["s08.e"] + 0.3 + 0.2 * k, 0.4, lambda a, k=k, el=el: E.bola(c, XE + 60 + 110 * k, 900, 36, LUZ[el], a))


# ---------------- as cores ----------------
def b_cores(c, t, C, b):
    if t < C["s10"]:
        E.frase(c, t, C["s09"], ps("nos", "i", 70) + [("fogos de artifício", "g", 66)], XE, 190, passo=0.12)
        for k, (ck, el, nome, cor) in enumerate((("s09.a", "Sr", "estrôncio", "vermelho"), ("s09.b", "Ba", "bário", "verde"),
                                                 ("s09.c", "Na", "sódio", "amarelo"), ("s09.d", "Cu", "cobre", "verde-azulado"))):
            x = 330 + k * 420
            fogos(c, t, C[ck], x, 470, 160, LUZ[el])
            Q.formula_em(c, t, C[ck] + 0.2, el, x, 790, 110, align="center")
            E.foco(c, t, C[ck] + 0.4, 0.4, lambda a, x=x, nome=nome, cor=cor: (centro(c, nome, x, 870, 46, "i", TINTA2, a),
                                                                              E.pilula(c, cor, x, 950, 42, "g", fundo=E.mix(LUZ[el], "#000000", 0.15), a=a)))
        return
    if t < C["s11"]:
        E.frase(c, t, C["s10.a"], [("teste de chama", "g", 90, COR)], XE, 220)
        cor = Q.muda_cor(t, C["s10.c"], "#F29A3A", LUZ["Na"], 0.8)
        E.foco(c, t, C["s10.b"], 0.5, lambda a: chama(c, 1300, 820, 220, 460, cor, a, t))
        E.frase(c, t, C["s10.b"], ps("um pouco da amostra no fogo", "i", 60), XE, 360, passo=0.1)
        E.frase(c, t, C["s10.c"], ps("e olha a cor", "i", 60), XE, 450, passo=0.1)
        E.frase(c, t, C["s10.d"], ps("amarelo forte?", "i", 66) + [("sódio", "g", 64, COR)], XE, 600, passo=0.1)
        # o poste de rua
        def poste(a):
            M.line(c, 1700, 980, 1700, 380, "#5B6470", a, 14)
            M.line(c, 1700, 380, 1620, 380, "#5B6470", a, 12)
            p = skia.Paint(AntiAlias=True)
            p.setShader(skia.GradientShader.MakeRadial(skia.Point(1610, 420), 220, [M.hexc("#F7B733", 0.6 * a), M.hexc("#F7B733", 0.0)], [0, 1]))
            c.drawCircle(1610, 420, 220, p)
            E.bola(c, 1610, 405, 26, "#F7B733", a)
        E.foco(c, t, C["s10.e"], 0.6, poste)
        E.frase(c, t, C["s10.e"], ps("postes com lâmpada de sódio", "i", 54, TINTA2), XE, 780, passo=0.08)
        return
    E.frase(c, t, C["s11.a"], [("Bohr", "g", 80, COR)] + ps("não é o mais moderno", "i", 72), XE, 300, passo=0.12)
    pilula_em(c, t, C["s11.b"], "o modelo atual: outra aula", XE + 330, 440, 50, TINTA2, "b")
    E.frase(c, t, C["s11.c"], ps("mas é o que a prova usa para", "i", 66) + [("a luz", "g", 64, "#D9A400")], XE, 640, passo=0.1)
    atomo_salto(c, t, 1500, 620, C["s11"] - 4, C["s11"] - 0.5, R=(80, 140, 200), cor_luz=LUZ["Na"], letras=False, energia=False)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s12"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s12.a"], ps("a luz sai quando o elétron", "i", 64) + [("sobe?", "g", 62, ERRADO)], XE, 320, passo=0.1)
    if t >= C["s12.b"]:
        E.risco(c, XE, 340, XE + 960, 270, t, C["s12.b"], largura=12)
    atomo_salto(c, t, 1450, 640, C["s12.b"], C["s12.c"], R=(100, 170, 240), cor_luz=LUZ["Na"], letras=False)
    E.frase(c, t, C["s12.b"], ps("subir:", "i", 64) + [("recebe energia", "g", 60, AMBAR)], XE, 520, passo=0.1)
    E.frase(c, t, C["s12.c"], ps("voltar:", "i", 64) + [("solta luz", "g", 60, "#D9A400")], XE, 660, passo=0.1)
    E.foco(c, t, C["s12.c"] + 1.0, 0.4, lambda a: E.selo(c, XE + 620, 640, 40, True, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 160, "center", 0.12)
        for k, s in enumerate(("fogos", "teste de chama", "lâmpada de sódio", "letreiro de néon")):
            E.foco(c, t, C["s13.a"] + 0.45 * k, 0.4, lambda a, k=k, s=s: E.pilula(c, s, 380 + k * 390, 300, 46, "b", fundo="#22232B", a=a, cor=BR))
        E.frase(c, t, C["s13.b"] - 1.4, ps("luz com cor própria?", "i", 66, CLARO), W / 2, 450, "center", 0.1)
        E.foco(c, t, C["s13.b"], 0.5, lambda a: E.pilula(c, "a resposta é Bohr", W / 2, 560, 80, "g", fundo=E.COR, a=a))
        for k, s in enumerate(("recebe energia", "sobe", "volta", "solta luz")):
            x = 300 + k * 440
            E.foco(c, t, C["s13.c"] + 0.4 * k, 0.4, lambda a, x=x, s=s, k=k: (E.bola(c, x, 780, 40, a=a), centro(c, str(k + 1), x, 800, 50, "g", E.SOBRE, a),
                                                                             centro(c, s, x, 890, 50, "g", BR, a)))
            if k < 3:
                p = ep(t, C["s13.c"] + 0.4 * k + 0.3, 0.3)
                if p > 0:
                    M.arrow(c, x + 60, 780, x + 380, 780, E.CLARO, p, 4, 16)
        return
    E.frase(c, t, C["s14.a"], ps("luz de cor própria", "i", 70, CLARO) + [("= salto", "g", 66, BR)], W / 2, 280, "center", 0.12)
    atomo_salto(c, t, W / 2, 620, C["s14.a"], C["s14.a"] + 1.4, R=(80, 130, 180), cor_luz=LUZ["Ba"], letras=False, energia=False, escuro=True)
    E.frase(c, t, C["s14.b"], [("cuidado:", "g", 60, ERRADO)] + ps("alternativa do núcleo se partindo", "i", 62, CLARO), W / 2, 900, "center", 0.1)
    E.frase(c, t, C["s14.c"], ps("a cor da chama mexe só nos", "i", 60, CLARO) + [("elétrons", "g", 58, BR)], W / 2, 1000, "center", 0.1)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s15"] + 1.0, ps("o sal de cozinha tem", "i", 62) + [("sódio", "g", 60, COR)], XE, 300, passo=0.1)
    E.frase(c, t, C["s15.a"], ps("uma pitada cai na chama", "i", 62), XE, 420, passo=0.1)
    E.frase(c, t, C["s15.b"], ps("e a chama fica", "i", 62) + [("amarela", "g", 60, "#D9A400")], XE, 520, passo=0.1)
    E.frase(c, t, C["s15.c"], ps("explique pelo modelo de Bohr,", "i", 62), XE, 700, passo=0.1)
    E.frase(c, t, C["s15.d"], ps("em", "i", 62) + [("quatro passos", "g", 60, COR)], XE, 800, passo=0.1)
    if t < C["s16"]:
        cor = Q.muda_cor(t, C["s15.b"], "#F29A3A", LUZ["Na"], 0.6)
        E.foco(c, t, C["s15.a"], 0.5, lambda a: chama(c, 1480, 820, 220, 440, cor, a, t))
    else:
        E.relogio(c, t, C["s16.a"], cx=1500, cy=480, r=190)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    passos = (("s17.a", "calor dá energia aos elétrons"), ("s17.b", "sobem e ficam excitados"), ("s17.c", "voltam para a camada de antes"),
              ("s17.d", "devolvem a energia: luz amarela"))
    for i, (k, s) in enumerate(passos):
        y = 250 + i * 160
        E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, ps(s, "i", 58), XE + 110, y, passo=0.08)
    atomo_salto(c, t, 1500, 520, C["s17.b"], C["s17.c"] + 0.4, R=(90, 150, 210), cor_luz=LUZ["Na"], letras=False)
    if t >= C["s17.e"]:
        q = ep(t, C["s17.e"], 0.4)
        c.drawRoundRect(skia.Rect.MakeXYWH(XE - 20, 250 + 3 * 160 - 90, 1060, 130), 24, 24, M.paint(E.COR, q, stroke=5))
        E.frase(c, t, C["s17.e"] + 0.2, ps("a luz sai na", "i", 56, TINTA2) + [("volta", "g", 54, COR)] + ps("(passo 4), não na subida", "i", 56, TINTA2), XE, 1000, passo=0.08)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s18"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        for i, (k, partes) in enumerate((("s18.a", [("só", "i", 66), ("certas camadas", "g", 62)]), ("s18.b", [("recebe energia:", "i", 66), ("sobe", "g", 62, AMBAR)]),
                                         ("s18.c", [("volta:", "i", 66), ("solta luz", "g", 62, "#D9A400")]), ("s18.d", [("a", "i", 66), ("cor de cada elemento", "g", 62, COR)]))):
            y = 340 + i * 160
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 44, a=a), centro(c, str(i + 1), XE + 40, y - 4, 54, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 110, y, passo=0.12)
        atomo_salto(c, t, 1500, 600, C["s18.b"], C["s18.c"], R=(90, 150, 210), cor_luz=LUZ["Sr"], letras=False, energia=False)
    E.saida(c, t, C["s19"] - 0.1, resumo)
    if t < C["s19"]:
        return
    E.frase(c, t, C["s19"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    for k, (s, cor) in enumerate((("prótons", E.COR), ("nêutrons", "#8A8D96"), ("elétrons", Q.ELETRON))):
        E.foco(c, t, C["s19.a"] + 0.3 * k, 0.4, lambda a, k=k, s=s, cor=cor: (E.bola(c, XE + 50, 380 + k * 120, 36, cor, a), E.escreve(c, s, XE + 110, 402 + k * 120, 70, "g", TINTA, a)))
    E.frase(c, t, C["s19.b"], [("íons", "g", 70, COR), ("e", "i", 74), ("isótopos", "g", 70, COR)], XE, 800, passo=0.12)
    E.foco(c, t, C["s19.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s19.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s19.c"] + 0.2, 0.4))
    E.frase(c, t, C["s19.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, problema=b_problema, niveis=b_niveis, salto=b_salto, cores=b_cores, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
