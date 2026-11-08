"""Visual — Estudativo · MAT-ESP-003: vistas e projeções.
Mesma linguagem da MAT-ESP-001 (sólidos do kit, elemento da vez na cor da matéria, resposta na esfera).

LINGUAGEM DAS VISTAS (as próximas aulas copiam daqui):
- Vista = figura plana num PAINEL (cartão branco com o nome em cima: "de frente", "de cima"), contorno em tinta preta
  e miolo claro da cor da matéria. O sólido fica do lado, em perspectiva; o painel mostra o que sobra dele achatado.
- Sombra = a mesma figura, mas cheia de cinza escuro (sombra()), no painel "sombra no chão" ou "sombra na parede".
- Luz: sol() com raios tracejados retos na cor da matéria (de cima ou de frente). Olhar: olho() com a seta tracejada.
- Pilha de cubinhos: cubinho() da trilha Medidas (MAT-MED-005), na mesma perspectiva cavaleira do kit.
  Posição (i, j, k) = coluna da esquerda para a direita, fileira da frente para o fundo, andar de baixo para cima.
  Nas vistas, cada cubinho vira um quadradinho; o que a fala aponta ganha a cor da matéria, o escondido fica tracejado.
Peças locais: painel(), olho(), sol(), sombra(), lata_deitada(), cubinho(), pilha(), quadradinhos().
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-003_vistas_e_projecoes.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("vista", "pilha", "sombra", "atalho", "questao", "fim"))
BR = "#FFFFFF"
MIOLO = E.mix(E.COR, "#FFFFFF", 0.78)   # miolo claro das vistas
ESCURO = "#3A3946"                       # sombra


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças comuns ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def fase(c, t, t0, t1, fn):
    if t0 - 0.01 <= t < t1 + 0.4:
        E.saida(c, t, t1, fn)


# ---------------- peças das vistas ----------------
def painel(c, t, t0, x, y, w, h, titulo, escuro=False):
    """cartão onde a vista é desenhada, com o nome em cima à esquerda. Devolve a opacidade"""
    a = ep(t, t0, 0.5)
    if a <= 0:
        return 0
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.12 * a))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 14))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + 6, y + 10, w, h), 22, 22), s)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), M.paint("#1A1838" if escuro else "#FFFFFF", a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 22, 22), M.paint(CINZA, a, stroke=2))
    E.escreve(c, titulo, x + 30, y + 62, 46, "i", CLARO if escuro else TINTA2, a)
    return a


def figura(c, path, a=1.0, cor=None, fundo=None, tracejada=False):
    """figura plana: miolo claro e contorno preto (vista) ou cheia de cinza escuro (sombra, com fundo=ESCURO)"""
    if a <= 0:
        return
    c.drawPath(path, M.paint(fundo or MIOLO, a))
    pt = M.paint(cor or TINTA, a, stroke=6)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    if tracejada:
        pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawPath(path, pt)


def p_ret(x, y, w, h):
    p = skia.Path(); p.addRect(skia.Rect.MakeXYWH(x, y, w, h)); return p


def p_circ(cx, cy, r):
    p = skia.Path(); p.addCircle(cx, cy, r); return p


def p_poli(pts):
    p = skia.Path(); p.addPoly(pts, True); return p


def sombra(c, path, a=1.0):
    figura(c, path, a, ESCURO, E.mix(ESCURO, "#000000", 0.0))


def olho(c, cx, cy, s, ang=0.0, a=1.0, alvo=None, t=0, t0=0):
    """olho que olha na direção ang (graus da tela); alvo = ponto até onde vai a seta tracejada"""
    if a <= 0:
        return
    if alvo:
        p = ease_io(prog(t, t0 + 0.3, 0.6))
        M.line(c, cx, cy, *alvo, E.COR, a * 0.8, 5, dash=[14, 12], progress=p)
        if p > 0.95:
            ux, uy = alvo[0] - cx, alvo[1] - cy
            n = math.hypot(ux, uy) or 1
            M.arrow(c, alvo[0] - ux / n * 30, alvo[1] - uy / n * 30, *alvo, E.COR, a, 5, 18)
    c.save(); c.translate(cx, cy); c.rotate(ang)
    p = skia.Path(); p.moveTo(-s, 0); p.quadTo(0, -0.8 * s, s, 0); p.quadTo(0, 0.8 * s, -s, 0); p.close()
    c.drawPath(p, M.paint("#FFFFFF", a))
    c.drawPath(p, M.paint(TINTA, a, stroke=5))
    c.drawCircle(0.12 * s, 0, 0.36 * s, M.paint(E.COR, a))
    c.drawCircle(0.12 * s, 0, 0.15 * s, M.paint(TINTA, a))
    c.restore()


def sol(c, t, t0, cx, cy, r=46, raios=(), escuro=False):
    """sol (ou lâmpada) com raios retos tracejados: raios = [(x0, y0, x1, y1), ...]"""
    k = ease_back(prog(t, t0, 0.5))
    if k <= 0:
        return
    for i in range(10):
        ang = math.radians(i * 36 + 10 * t)
        M.line(c, cx + math.cos(ang) * r * 1.25 * k, cy + math.sin(ang) * r * 1.25 * k,
               cx + math.cos(ang) * r * 1.7 * k, cy + math.sin(ang) * r * 1.7 * k, E.COR, 1, 6)
    c.drawCircle(cx, cy, r * k, M.paint(E.mix(E.COR, "#FFFFFF", 0.45)))
    c.drawCircle(cx, cy, r * k, M.paint(E.COR, 1, stroke=6))
    for i, (x0, y0, x1, y1) in enumerate(raios):
        p = ease_io(prog(t, t0 + 0.3 + 0.1 * i, 0.6))
        M.line(c, x0, y0, x1, y1, E.COR, 0.7, 5, dash=[14, 12], progress=p)
        if p > 0.97:
            M.arrow(c, lerp(x0, x1, 0.9), lerp(y0, y1, 0.9), x1, y1, E.COR, 0.9, 5, 16)


def lata_deitada(c, x, y, L, r, a=1.0, cor=None):
    """lata deitada, vista de lado e um pouco de cima: o eixo vai de x a x + L na altura y; a tampa da direita aparece inteira"""
    if a <= 0:
        return
    cor = cor or E.COR
    rx = r * 0.36
    corpo = skia.Path()
    corpo.moveTo(x, y - r); corpo.lineTo(x + L, y - r)
    corpo.arcTo(skia.Rect.MakeXYWH(x + L - rx, y - r, 2 * rx, 2 * r), 270, 180, False)
    corpo.lineTo(x, y + r)
    corpo.arcTo(skia.Rect.MakeXYWH(x - rx, y - r, 2 * rx, 2 * r), 90, 180, False)
    corpo.close()
    g = skia.Paint(AntiAlias=True)
    g.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y - r), skia.Point(0, y + r)],
                                               [M.hexc(E.mix(cor, "#FFFFFF", 0.82), a), M.hexc(E.mix(cor, "#FFFFFF", 0.62), a),
                                                M.hexc(E.mix(cor, "#FFFFFF", 0.45), a)], [0, 0.4, 1]))
    c.drawPath(corpo, g)
    c.drawOval(skia.Rect.MakeXYWH(x + L - rx, y - r, 2 * rx, 2 * r), M.paint(E.mix(cor, "#FFFFFF", 0.72), a))
    pt = M.paint(TINTA, a, stroke=6)
    c.drawLine(x, y - r, x + L, y - r, pt); c.drawLine(x, y + r, x + L, y + r, pt)
    c.drawArc(skia.Rect.MakeXYWH(x - rx, y - r, 2 * rx, 2 * r), 90, 180, False, pt)
    tr = M.paint(TINTA, 0.55 * a, stroke=4)
    tr.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
    c.drawArc(skia.Rect.MakeXYWH(x - rx, y - r, 2 * rx, 2 * r), -90, 180, False, tr)
    c.drawOval(skia.Rect.MakeXYWH(x + L - rx, y - r, 2 * rx, 2 * r), pt)


# ---------------- cubinhos ----------------
KX, KY = 0.394, -0.308  # a profundidade na perspectiva cavaleira (a mesma de E.paralelepipedo)


def cubinho(c, x, y, s, a=1.0, cor=None, borda="#FFFFFF"):
    """cubinho cheio de aresta s: (x, y) = canto de baixo à esquerda da face da frente"""
    if a <= 0:
        return
    cor = cor or E.COR
    dx, dy = KX * s, KY * s
    br = M.paint(borda, 0.9 * a, stroke=3)

    def poli(pts, tinta):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(tinta, a)); c.drawPath(p, br)
    poli([(x, y - s), (x + s, y - s), (x + s + dx, y - s + dy), (x + dx, y - s + dy)], E.mix(cor, "#FFFFFF", 0.35))
    poli([(x + s, y), (x + s + dx, y + dy), (x + s + dx, y - s + dy), (x + s, y - s)], E.mix(cor, "#000000", 0.25))
    poli([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], cor)


PILHA = ((0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 2))   # (coluna, fileira, andar)
FRENTE = (3, 1, 1)                                                          # altura de cada coluna, vista de frente
CIMA = ((0, 0), (1, 0), (2, 0), (0, 1))                                     # (coluna, fileira) com cubo
assert all(FRENTE[i] == max(k + 1 for ii, j, k in PILHA if ii == i) for i in range(3))
assert sorted(CIMA) == sorted({(i, j) for i, j, k in PILHA})


def pilha(c, t, ts, x0, y0, s, cores=None, achata=1.0, a=1.0, escondidos=(3,), cor_esc=None):
    """a pilha da aula: ts = instante de cada cubinho de PILHA; cores = {índice: cor}; achata = 1 (normal) a 0 (achatada no chão)"""
    ordem = sorted(range(len(PILHA)), key=lambda n: (-PILHA[n][1], PILHA[n][2], PILHA[n][0]))
    for n in ordem:
        i, j, k = PILHA[n]
        q = ep(t, ts[n], 0.4) * a
        if q <= 0:
            continue
        cair = (1 - ease_io(prog(t, ts[n], 0.4))) * 60
        ss = s * max(achata, 0.04)
        x = x0 + i * s + KX * s * j
        y = y0 - k * ss + KY * s * j - cair
        if achata < 0.999:
            # cubinho achatado: só a altura encolhe
            dx, dy = KX * s, KY * s
            cor = (cores or {}).get(n) or E.COR
            for pts, tinta in (([(x, y - ss), (x + s, y - ss), (x + s + dx, y - ss + dy), (x + dx, y - ss + dy)], E.mix(cor, "#FFFFFF", 0.35)),
                               ([(x + s, y), (x + s + dx, y + dy), (x + s + dx, y - ss + dy), (x + s, y - ss)], E.mix(cor, "#000000", 0.25)),
                               ([(x, y), (x + s, y), (x + s, y - ss), (x, y - ss)], cor)):
                p = skia.Path(); p.addPoly(pts, True)
                c.drawPath(p, M.paint(tinta, q)); c.drawPath(p, M.paint("#FFFFFF", 0.9 * q, stroke=3))
        else:
            cubinho(c, x, y, s, q, (cores or {}).get(n))
    # o cubinho de trás fica quase todo escondido: o contorno dele aparece tracejado, como aresta oculta
    for n in escondidos:
        i, j, k = PILHA[n]
        q = ep(t, ts[n] + 0.3, 0.4) * a * (achata >= 0.999)
        if q <= 0:
            continue
        x, y, dx, dy = x0 + i * s + KX * s * j, y0 - k * s + KY * s * j, KX * s, KY * s
        pt = M.paint(cor_esc or TINTA, q, stroke=5)
        pt.setPathEffect(skia.DashPathEffect.Make([12, 9], 0))
        for P, Q in (((x, y), (x + s, y)), ((x + s, y), (x + s, y - s)), ((x + s, y - s), (x, y - s)), ((x, y - s), (x, y)),
                     ((x + s, y - s), (x + s + dx, y - s + dy)), ((x + s, y), (x + s + dx, y + dy)), ((x + s + dx, y + dy), (x + s + dx, y - s + dy))):
            c.drawLine(*P, *Q, pt)


def quadradinhos(c, t, cel, x, y, q, ts, cores=None, a=1.0, sombra_=False, tracejados=()):
    """vista em quadradinhos: cel = [(coluna, linha de baixo para cima)], (x, y) = canto de baixo à esquerda; ts = instante de cada um"""
    for n, (i, j) in enumerate(cel):
        k = ep(t, ts[n], 0.4) * a
        if k <= 0:
            continue
        r = p_ret(x + i * q, y - (j + 1) * q, q, q)
        if sombra_:
            figura(c, r, k, "#FFFFFF", ESCURO)
        else:
            figura(c, r, k, TINTA, (cores or {}).get(n) or MIOLO)
    for (i, j, t0) in tracejados:
        k = ep(t, t0, 0.4) * a
        if k > 0:
            figura(c, p_ret(x + i * q + 10, y - (j + 1) * q + 10, q - 20, q - 20), k, TINTA2, E.mix(TINTA2, "#FFFFFF", 0.9), tracejada=True)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s01.{k}"] for k in "abcd")

    def um():
        sol(c, t, a1, 560, 170, 50, raios=[(x, 280, x, 470) for x in (380, 500, 620, 740)])
        E.frase(c, t, a1 + 0.3, ps("meio-dia:", "i", 66) + [("sol em cima", "g", 66, COR)], 1100, 200, "left", 0.1)
        E.foco(c, t, b1, 0.6, lambda q: (M.line(c, 200, 712, 920, 712, TINTA2, q, 4), lata_deitada(c, 340, 600, 420, 110, q)))
        E.frase(c, t, b1 + 0.3, ps("lata deitada:", "i", 66) + [("que sombra?", "g", 66, COR)], 1100, 320, "left", 0.1)
        pa = painel(c, t, b1 + 0.8, 1100, 420, 720, 470, "sombra no chão")
        E.foco(c, t, c1, 0.5, lambda q: figura(c, p_circ(1290, 680, 110), q, ERRADO if t >= d1 else TINTA2, E.mix(TINTA2, "#FFFFFF", 0.85),
                                               tracejada=True))
        E.foco(c, t, c1 + 0.2, 0.4, lambda q: centro(c, "círculo?", 1290, 860, 52, "i", ERRADO if t >= d1 else TINTA2, q))
        if t >= d1:
            E.risco(c, 1190, 790, 1390, 570, t, d1, largura=10)
        E.foco(c, t, d1, 0.5, lambda q: sombra(c, p_ret(1460, 610, 300, 140), q))
        E.foco(c, t, d1 + 0.2, 0.4, lambda q: centro(c, "retângulo", 1610, 860, 56, "g", CERTO, q))
    E.saida(c, t, C["s02"] - 0.1, um)

    if t >= C["s02"]:
        ta, tb = C["s02.a"], C["s02.b"]
        E.foco(c, t, tb - 0.2, 0.7, lambda a: E.bola(c, 1560, 580, 240 * ease_back(prog(t, tb - 0.2, 0.7))), blur=0)
        E.frase(c, t, ta, ps("até o fim desta aula", "i", 90), XE, 300, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.25), [("desenhar", "g", 104, COR)] + ps("o objeto", "i", 96), XE, 460, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.45), ps("de cima e de frente", "i", 90), XE, 590, passo=0.14)
        E.frase(c, t, lerp(ta, tb, 0.7), [("acertar", "g", 104, COR)] + ps("a sombra", "i", 96), XE, 750, passo=0.14)
        E.foco(c, t, tb + 0.1, 0.5, lambda a: (centro(c, "+ atalho", 1560, 555, 80, "g", E.SOBRE, a),
                                               centro(c, "de prova", 1560, 640, 80, "i", E.SOBRE, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.3, ps("você só precisa de", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, C["s03.a"], 0.5, lambda a: E.escreve(c, "1", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, C["s03.a"] + 0.15, 0.5, lambda a: E.escreve(c, "coisa", XE + 200, 700, 120, "i", TINTA, a))
    x, y, w = 940, 230, 880
    p = ep(t, C["s03.b"], 0.5)
    E.caixa_pontilhada(c, x, y, w, 196, p, prog_=p)
    E.frase(c, t, C["s03.b"] + 0.1, [("reconhecer", "i", 60)], x + 44, y + 84)
    E.frase(c, t, C["s03.b"] + 0.3, [("os sólidos", "g", 60, COR)], x + 44, y + 160)
    E.cursor(c, x + w - 30, y + 170, ep(t, C["s03.b"], 0.4))
    tb = C["s03.b"]
    E.cubo(c, t, tb + 0.6, 960, 780, 150)
    E.cilindro(c, t, tb + 0.9, 1290, 790, 80, 190)
    E.cone(c, t, tb + 1.2, 1500, 790, 85, 200)
    E.piramide(c, t, tb + 1.5, 1720, 790, 4, 100, 200)
    E.frase(c, t, lerp(tb, C["s03.end"], 0.8), ps("faltou?", "i", 58, COR) + ps("procure no canal", "i", 58), x, 960, "left", 0.12)


# ---------------- o que é vista ----------------
PF = (960, 300, 400, 520)    # painel "de frente": x, y, w, h
PC = (1420, 300, 400, 520)   # painel "de cima"


def b_vista(c, t, C, b):
    a4, b4, c4, d4 = (C[f"s04.{k}"] for k in "abcd")
    a5, b5, c5 = C["s05.a"], C["s05.b"], C["s05.c"]
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")

    def ideia():
        E.cubo(c, t, C["s04"], 330, 820, 320)
        olho(c, 150, 660, 46, 0, ep(t, a4, 0.4), alvo=(300, 660), t=t, t0=a4)
        E.frase(c, t, a4, [("vista:", "g", 84, COR)] + ps("o que você vê", "i", 76), 1000, 300, "left", 0.1)
        E.frase(c, t, a4 + 0.8, ps("olhando bem reto", "i", 76), 1000, 400, "left", 0.1)
        E.frase(c, t, b4, [("figura plana,", "g", 70)], 1000, 560, "left", 0.1)
        E.frase(c, t, b4 + 0.6, ps("sem perspectiva", "i", 70), 1000, 650, "left", 0.1)
        E.foco(c, t, b4 + 0.4, 0.5, lambda q: figura(c, p_ret(1560, 520, 180, 180), q))
        E.frase(c, t, c4, ps("as mais cobradas:", "i", 60, TINTA2), 1000, 820, "left", 0.1)
        E.frase(c, t, c4 + 0.5, [("de frente", "g", 66, COR)], 1000, 910, "left", 0.1)
        E.frase(c, t, d4, ps("e", "i", 66) + [("de cima", "g", 66, COR)], 1300, 910, "left", 0.1)
        olho(c, 545, 260, 46, 90, ep(t, d4, 0.4), alvo=(545, 420), t=t, t0=d4)
    fase(c, t, C["s04"], C["s05"] - 0.1, ideia)

    def lata():
        E.cilindro(c, t, a5, 400, 820, 130, 340)
        E.frase(c, t, a5, ps("uma lata", "i", 70) + [("em pé", "g", 70, COR)], 400, 230, "center", 0.1)
        x, y, w, h = PF
        painel(c, t, b5 - 0.3, x, y, w, h, "de frente")
        E.foco(c, t, b5, 0.5, lambda q: figura(c, p_ret(x + w / 2 - 104, y + 130, 208, 272), q))
        E.foco(c, t, b5 + 0.5, 0.4, lambda q: centro(c, "retângulo", x + w / 2, y + h - 50, 52, "g", COR, q))
        x, y, w, h = PC
        painel(c, t, c5 - 0.3, x, y, w, h, "de cima")
        E.foco(c, t, c5, 0.5, lambda q: figura(c, p_circ(x + w / 2, y + 270, 104), q))
        E.foco(c, t, c5 + 0.5, 0.4, lambda q: centro(c, "círculo", x + w / 2, y + h - 50, 52, "g", COR, q))
    fase(c, t, C["s05"], C["s06"] - 0.1, lata)
    if t < C["s06"] - 0.1:
        return
    E.cone(c, t, a6, 400, 840, 140, 380)
    E.frase(c, t, a6, ps("um cone", "i", 70) + [("em pé", "g", 70, COR)], 400, 230, "center", 0.1)
    x, y, w, h = PF
    painel(c, t, b6 - 0.3, x, y, w, h, "de frente")
    E.foco(c, t, b6, 0.5, lambda q: figura(c, p_poli([(x + w / 2 - 112, y + 420), (x + w / 2 + 112, y + 420), (x + w / 2, y + 120)]), q))
    E.foco(c, t, b6 + 0.5, 0.4, lambda q: centro(c, "triângulo", x + w / 2, y + h - 50, 52, "g", COR, q))
    x, y, w, h = PC
    painel(c, t, c6 - 0.3, x, y, w, h, "de cima")
    E.foco(c, t, c6, 0.5, lambda q: figura(c, p_circ(x + w / 2, y + 270, 112), q))
    if t >= c6:
        pulsa = 1 + 0.6 * math.sin(min(1, prog(t, d6, 0.9)) * math.pi) if t >= d6 else 1
        k = ease_back(prog(t, c6 + 0.3, 0.4))
        c.drawCircle(x + w / 2, y + 270, 12 * k * pulsa, M.paint(E.COR if t >= d6 else TINTA))
    E.foco(c, t, d6, 0.4, lambda q: centro(c, "a ponta", x + w / 2, y + h - 50, 52, "g", COR, q))


# ---------------- pilha de cubinhos ----------------
SX, SY, SS = 200, 860, 125
QF = (900, 280, 440, 560)
QC = (1400, 280, 440, 560)


def b_pilha(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    a8, b8, c8 = C["s08.a"], C["s08.b"], C["s08.c"]
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    ts = (b7, b7 + 0.25, b7 + 0.5, c7, d7, d7 + 0.35)
    cores = {}
    if c8 <= t < C["s09"]:
        cores[3] = E.mix(TINTA2, "#FFFFFF", 0.3)
    if t >= c9:
        cores[3] = E.COR
    if b9 <= t:
        cores.update({4: E.mix(E.COR, "#FFFFFF", 0.35), 5: E.mix(E.COR, "#FFFFFF", 0.35)})
    pilha(c, t, ts, SX, SY, SS, cores, cor_esc=E.COR if (C["s07.c"] <= t < C["s07.d"] or t >= C["s09.c"]) else None)
    E.frase(c, t, C["s07"] + 0.2, ps("uma pilha de", "i", 70) + [("cubinhos iguais", "g", 70, COR)], XE, 180, "left", 0.1)
    if t < C["s08"]:
        E.frase(c, t, b7 + 0.2, [("3", "g", 66, COR)] + ps("na frente", "i", 62), 1000, 420, "left", 0.1)
        E.frase(c, t, c7 + 0.2, [("1", "g", 66, COR)] + ps("atrás do da esquerda", "i", 62), 1000, 540, "left", 0.1)
        E.frase(c, t, d7 + 0.2, [("2", "g", 66, COR)] + ps("em cima: torre de 3", "i", 62), 1000, 660, "left", 0.1)
        return
    # vista de frente: alturas 3, 1, 1
    x, y, w, h = QF
    q = 100
    bx, by = x + w / 2 - 1.5 * q, y + h - 70
    painel(c, t, C["s08"], x, y, w, h, "de frente")
    cel_f = [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
    ts_f = [a8, a8 + 0.2, a8 + 0.4, b8, b8 + 0.2]
    cores_f = {0: E.mix(E.COR, "#FFFFFF", 0.35), 1: E.mix(E.COR, "#FFFFFF", 0.35), 2: E.mix(E.COR, "#FFFFFF", 0.35)} if t < b8 + 0.6 else None
    quadradinhos(c, t, cel_f, bx, by, q, ts_f, cores_f, tracejados=() if t >= C["s09"] else ((0, 0, c8 + 0.5),))
    if C["s08"] <= t < C["s09"] + 0.4:
        E.saida(c, t, C["s09"] - 0.1, lambda: (E.frase(c, t, c8, ps("o de trás", "i", 56, TINTA2) + [("some", "g", 56)], x + w / 2, y + 140, "center", 0.1)))
    if t < C["s09"] - 0.1:
        return
    # vista de cima: 4 quadradinhos em L
    x, y, w, h = QC
    bx, by = x + w / 2 - 1.5 * q, y + h - 120
    painel(c, t, C["s09"], x, y, w, h, "de cima")
    ts_c = [a9 + 0.3, a9 + 0.5, a9 + 0.7, c9]
    cores_c = {}
    if t >= b9:
        cores_c[0] = E.mix(E.COR, "#FFFFFF", 0.35)
    if t >= c9:
        cores_c[3] = E.COR
    quadradinhos(c, t, CIMA, bx, by, q, ts_c, cores_c)
    E.foco(c, t, d9, 0.5, lambda q_: E.pilula(c, "4 em L", x + w / 2, y + 150, 56, "g", a=q_, cor=E.SOBRE))
    E.frase(c, t, a9, ps("de cima,", "i", 56, TINTA2) + [("a altura some", "g", 56)], 1150, 1000, "center", 0.1)


# ---------------- sombra ----------------
def b_sombra(c, t, C, b):
    a0, b0, c0, d0 = (C[f"s10.{k}"] for k in "abcd")
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    q = 90

    def luzes():
        pilha(c, t, [C["s10"]] * 6, 260, 880, 110)
        sol(c, t, a0, 420, 330, 42, raios=[(x, 410, x, 530) for x in (310, 420, 530)])
        x, y, w, h = QF
        painel(c, t, b0 - 0.2, x, y, w, h, "sombra no chão")
        quadradinhos(c, t, CIMA, x + w / 2 - 1.5 * q, y + h - 120, q, [b0] * 4, sombra_=True)
        sol(c, t, c0, 110, 960, 40, raios=[(170, 900, 330, 780), (150, 840, 310, 720)])
        x, y, w, h = QC
        painel(c, t, d0 - 0.2, x, y, w, h, "sombra na parede")
        quadradinhos(c, t, [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)], x + w / 2 - 1.5 * q, y + h - 70, q, [d0] * 5, sombra_=True)
        E.frase(c, t, b0 + 0.3, ps("= vista", "i", 56, TINTA2) + [("de cima", "g", 56, COR)], QF[0] + QF[2] / 2, QF[1] + QF[3] + 90, "center", 0.1)
        E.frase(c, t, d0 + 0.3, ps("= vista", "i", 56, TINTA2) + [("de frente", "g", 56, COR)], QC[0] + QC[2] / 2, QC[1] + QC[3] + 90, "center", 0.1)
        E.frase(c, t, C["s10"] + 0.2, ps("e a", "i", 70) + [("sombra?", "g", 74, COR)], XE, 180, "left", 0.1)
    fase(c, t, C["s10"], C["s11"] - 0.1, luzes)
    if t < C["s11"] - 0.1:
        return
    E.frase(c, t, a1, ps("sombra de luz reta =", "i", 70) + [("projeção", "g", 76, COR)], W / 2, 180, "center", 0.1)
    sol(c, t, C["s11"], 500, 290, 44, raios=[(x, 370, x, 470) for x in (340, 500, 660)])
    E.foco(c, t, C["s11"] + 0.2, 0.5, lambda q_: lata_deitada(c, 280, 600, 440, 110, q_))
    if t >= b1:
        E.foco(c, t, b1, 0.4, lambda q_: (M.line(c, 280, 750, 720, 750, COR, q_, 5), centro(c, "comprimento", 500, 810, 50, "g", COR, q_)))
        E.foco(c, t, b1 + 0.6, 0.4, lambda q_: (M.line(c, 720, 490, 720, 710, COR, q_, 5), E.escreve(c, "largura", 700, 465, 46, "g", COR, q_)))
    x, y, w, h = QC
    painel(c, t, b1 + 0.3, x - 60, y, w + 60, h, "de cima")
    E.foco(c, t, c1, 0.5, lambda q_: sombra(c, p_ret(x + 20, y + 200, 340, 160), q_))
    E.foco(c, t, c1 + 0.4, 0.4, lambda q_: centro(c, "retângulo", x + w / 2 - 10, y + 460, 56, "g", CERTO, q_))
    olho(c, 1000, 600, 40, 180, ep(t, d1, 0.4), alvo=(800, 600), t=t, t0=d1)
    E.foco(c, t, d1 + 0.3, 0.5, lambda q_: figura(c, p_circ(1000, 820, 70), q_))
    E.frase(c, t, d1 + 0.5, ps("olhando a tampa:", "i", 52, TINTA2), 1000, 960, "center", 0.1)
    E.frase(c, t, d1 + 0.9, [("círculo", "g", 52, COR)], 1000, 1020, "center", 0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    a2, b2, c2, d2, e2 = (C[f"s12.{k}"] for k in "abcde")
    E.frase(c, t, C["s12"] + 0.2, [("o erro", "g", 80, ERRADO)] + ps("comum", "i", 80), W / 2, 170, "center", 0.12)

    def famosa():
        E.frase(c, t, a2, ps("responder pela", "i", 70) + [("forma famosa", "g", 70, ERRADO)], W / 2, 290, "center", 0.1)
        E.foco(c, t, a2 + 0.3, 0.5, lambda q: lata_deitada(c, 360, 620, 440, 110, q))
        E.frase(c, t, b2, ps("lata é redonda →", "i", 66), 1360, 560, "center", 0.1)
        E.foco(c, t, b2 + 0.6, 0.5, lambda q: figura(c, p_circ(1360, 760, 100), q, ERRADO, E.mix(ERRADO, "#FFFFFF", 0.85)))
        E.foco(c, t, b2 + 0.8, 0.4, lambda q: centro(c, "círculo?", 1360, 930, 56, "g", ERRADO, q))
    fase(c, t, C["s12"], c2 - 0.1, famosa)
    if t < c2 - 0.1:
        return
    E.frase(c, t, c2, ps("depende de", "i", 64) + [("onde vem a luz", "g", 64, COR)] + ps("e de", "i", 64) + [("como ele está", "g", 64, COR)],
            W / 2, 280, "center", 0.1)
    sol(c, t, d2 - 0.5, 480, 390, 40, raios=[(x, 460, x, 530) for x in (400, 480, 560)])
    E.cilindro(c, t, d2 - 0.3, 480, 800, 100, 240)
    E.foco(c, t, d2, 0.5, lambda q: sombra(c, p_circ(480, 960, 70), q))
    E.foco(c, t, d2 + 0.3, 0.4, lambda q: E.escreve(c, "círculo", 580, 975, 56, "g", CERTO, q))
    sol(c, t, e2 - 0.5, 1340, 390, 40, raios=[(x, 460, x, 560) for x in (1220, 1340, 1460)])
    E.foco(c, t, e2 - 0.3, 0.5, lambda q: lata_deitada(c, 1150, 700, 380, 95, q))
    E.foco(c, t, e2, 0.5, lambda q: sombra(c, p_ret(1150, 905, 380, 110), q))
    E.foco(c, t, e2 + 0.3, 0.4, lambda q: E.escreve(c, "retângulo", 1560, 980, 56, "g", CERTO, q))
    M.line(c, 960, 380, 960, 1020, TINTA2, ep(t, d2 - 0.5, 0.4) * 0.5, 3, dash=E.TRACO)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    a4, b4 = C["s14.a"], C["s14.b"]
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")

    def eixos():
        E.frase(c, t, a3, ps("cada vista", "i", 80, CLARO) + [("apaga uma direção", "g", 80, BR)], W / 2, 200, "center", 0.12)
        O = (520, 760)
        some_p = ep(t, b3, 0.5) * (1 - ep(t, c3, 0.5))
        some_a = ep(t, c3, 0.5)
        for (dx, dy), nome, apaga in (((420, 0), "largura", 0), ((0, -380), "altura", some_a), ((330 * 0.79, -330 * 0.62), "profundidade", some_p)):
            q = ep(t, a3 + 0.3, 0.6)
            al = q * (1 - 0.75 * apaga)
            M.arrow(c, *O, O[0] + dx, O[1] + dy, CLARO, al, 9, 26, q)
            E.foco(c, t, a3 + 0.6, 0.4, lambda k, dx=dx, dy=dy, nome=nome, al=al: centro(c, nome, O[0] + dx * 1.12, O[1] + dy * 1.12 + (60 if dy == 0 else 0), 52, "g", BR, k * max(al, 0.25)))
            if apaga > 0:
                mx, my = O[0] + dx * 0.55, O[1] + dy * 0.55
                M.line(c, mx - 40, my + 40, mx + 40, my - 40, ERRADO, apaga, 10)
        E.frase(c, t, b3, [("de frente:", "g", 60, BR)] + ps("largura e altura", "i", 58, CLARO), 1060, 500, "left", 0.1)
        E.frase(c, t, c3, [("de cima:", "g", 60, BR)] + ps("largura e profundidade", "i", 58, CLARO), 1060, 650, "left", 0.1)
    fase(c, t, C["s13"], C["s14"] - 0.1, eixos)

    def regras():
        E.frase(c, t, C["s14"] + 0.2, ps("na pilha de cubinhos", "i", 76, CLARO), W / 2, 200, "center", 0.12)
        E.frase(c, t, a4, [("de cima:", "g", 76, BR)], 260, 400)
        E.frase(c, t, a4 + 0.6, ps("1 quadradinho em cada", "i", 66, CLARO), 260, 490, "left", 0.1)
        E.frase(c, t, a4 + 1.2, ps("lugar do chão com cubo", "i", 66, CLARO), 260, 570, "left", 0.1)
        E.frase(c, t, b4, [("de frente:", "g", 76, BR)], 260, 740)
        E.frase(c, t, b4 + 0.6, ps("em cada coluna, a", "i", 66, CLARO) + [("torre mais alta", "g", 66, BR)], 260, 830, "left", 0.1)
        E.frase(c, t, b4 + 1.6, ps("na frente ou no fundo", "i", 66, CLARO), 260, 910, "left", 0.1)
        q = 80
        quadradinhos(c, t, CIMA, 1450, 560, q, [a4 + 0.4] * 4)
        quadradinhos(c, t, [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)], 1450, 960, q, [b4 + 0.4] * 5)
    fase(c, t, C["s14"], C["s15"] - 0.1, regras)
    if t < C["s15"] - 0.1:
        return

    def achata():
        E.frase(c, t, a5, ps("a luz reta", "i", 76, CLARO) + [("achata", "g", 84, BR)] + ps("o objeto", "i", 76, CLARO), W / 2, 200, "center", 0.12)
        k = 1 - ease_io(prog(t, a5 + 0.5, 1.6))
        sol(c, t, a5, 960, 330, 40, raios=[(x, 400, x, 520) for x in (840, 960, 1080)])
        pilha(c, t, [C["s15"]] * 6, 790, 880, 120, achata=k)
        E.frase(c, t, b5, ps("o de trás", "i", 66, CLARO) + [("cai em cima", "g", 66, BR)] + ps("do da frente", "i", 66, CLARO), W / 2, 1000, "center", 0.1)
    fase(c, t, C["s15"], c5 - 0.1, achata)
    if t < c5 - 0.1:
        return
    E.frase(c, t, c5, [("luz inclinada:", "g", 76, BR)] + ps("não compensa", "i", 76, CLARO), W / 2, 220, "center", 0.12)
    E.foco(c, t, c5, 0.5, lambda q: M.line(c, 300, 820, 1700, 820, CLARO, q * 0.6, 4))
    E.foco(c, t, c5 + 0.2, 0.5, lambda q: M.line(c, 760, 820, 760, 560, BR, q, 14))
    # o sol desce e a sombra estica: o raio passa pela ponta do poste e cai na ponta da sombra
    L = lerp(240, 620, ease_io(prog(t, d5, 1.4)))
    ys = 560 - 430 * 260 / L
    sol(c, t, c5 + 0.3, 330, ys, 40)
    q = ep(t, c5 + 0.8, 0.5)
    if q > 0:
        M.line(c, 330, ys, 760 + L, 820, E.COR, 0.7 * q, 5, dash=[14, 12])
        c.drawRect(skia.Rect.MakeXYWH(760, 808, L, 24), M.paint(CLARO, 0.55 * q))
    E.frase(c, t, d5, ps("a sombra", "i", 70, CLARO) + [("estica", "g", 76, BR)], W / 2, 960, "center", 0.12)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    a6, b6, c6 = C["s16.a"], C["s16.b"], C["s16.c"]
    E.frase(c, t, C["s16"] + 0.1, ps("hora de testar", "i", 72, COR), XE, 200, passo=0.12)
    E.frase(c, t, a6, ps("uma", "i", 72) + [("pirâmide quadrangular", "g", 72, COR)], XE, 340, passo=0.1)
    E.frase(c, t, a6 + 1.0, ps("em pé, ponta sobre o centro", "i", 64, TINTA2), XE, 430, passo=0.1)
    E.frase(c, t, b6, ps("a vista", "i", 80) + [("de cima?", "g", 86, COR)], XE, 620, passo=0.12)
    E.frase(c, t, c6, ps("luz de frente: a sombra", "i", 72), XE, 770, passo=0.1)
    E.frase(c, t, c6 + 1.0, ps("na parede", "i", 72) + [("atrás?", "g", 80, COR)], XE, 860, passo=0.1)
    E.saida(c, t, C["s17.a"] - 0.1, lambda: E.piramide(c, t, a6, 1480, 820, 4, 240, 440))
    E.relogio(c, t, C["s17.a"])


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    a9, b9, c9 = C["s19.a"], C["s19.b"], C["s19.c"]
    E.piramide(c, t, C["s18"], 400, 820, 4, 200, 400)
    x, y, w, h = PF
    painel(c, t, C["s18"] + 0.2, x, y, w, h, "de cima")
    cx, cy, l = x + w / 2, y + 270, 260
    E.foco(c, t, a8, 0.5, lambda q: figura(c, p_ret(cx - l / 2, cy - l / 2, l, l), q))
    for k, (dx, dy) in enumerate(((-1, -1), (1, -1), (1, 1), (-1, 1))):
        p = ease_io(prog(t, b8 + 0.15 * k, 0.5))
        if p > 0:
            M.line(c, cx + dx * l / 2, cy + dy * l / 2, cx, cy, TINTA, 1, 6, progress=p)
    if t >= c8:
        pulsa = 1 + 0.6 * math.sin(min(1, prog(t, c8, 0.9)) * math.pi)
        c.drawCircle(cx, cy, 14 * pulsa * ease_back(prog(t, c8, 0.4)), M.paint(E.COR))
    E.foco(c, t, a8 + 0.4, 0.4, lambda q: centro(c, "quadrado", cx, y + h - 50, 52, "g", COR, q))
    E.frase(c, t, b8, ps("arestas = diagonais", "i", 50, TINTA2), cx, y + h + 70, "center", 0.08)
    E.frase(c, t, c8, ps("ponta no centro", "i", 50, TINTA2), cx, y + h + 140, "center", 0.08)
    x, y, w, h = PC
    painel(c, t, a9, x, y, w, h, "sombra na parede")
    E.frase(c, t, a9 + 0.3, ps("some a", "i", 50, TINTA2) + [("profundidade", "g", 50)], x + w / 2, y + h + 70, "center", 0.08)
    E.foco(c, t, b9, 0.5, lambda q: sombra(c, p_poli([(x + w / 2 - 130, y + 400), (x + w / 2 + 130, y + 400), (x + w / 2, y + 130)]), q))
    E.foco(c, t, b9 + 0.4, 0.4, lambda q: centro(c, "triângulo", x + w / 2, y + h - 50, 56, "g", CERTO, q))
    E.frase(c, t, c9, ps("mesmo sólido,", "i", 66) + [("duas formas", "g", 66, COR)], 1380, 210, "center", 0.1)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", ps("vista: o objeto", "i", 70) + [("achatado,", "g", 70, COR)], ps("visto bem reto", "i", 70)),
                 ("s20.b", ps("sombra de luz reta =", "i", 70) + [("a vista", "g", 70, COR)], ps("daquela direção", "i", 70)))
        for i, (k, l1, l2) in enumerate(itens):
            y = 400 + i * 300
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 60, a=a), centro(c, str(i + 1), 300, y - 7, 68, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 400, y, "left", 0.12)
            E.frase(c, t, C[k] + 1.0, l2, 400, y + 95, "left", 0.12)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, a1, [("Retas", "g", 130, COR)] + ps("no espaço", "i", 110), XE, 420)
    E.frase(c, t, a1 + 0.6, ps("paralelas ou que se cruzam", "i", 70), XE, 530, passo=0.1)
    E.frase(c, t, b1, ps("e uma reta que só existe no espaço", "i", 64, TINTA2), XE, 650, passo=0.1)
    E.paralelepipedo(c, t, a1 + 0.3, 1330, 860, 330, 180, 200)
    E.foco(c, t, c1, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 380, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, c1 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(700, 405, p), ep(t, c1 + 0.2, 0.4))
    E.frase(c, t, d1, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, vista=b_vista, pilha=b_pilha, sombra=b_sombra, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
