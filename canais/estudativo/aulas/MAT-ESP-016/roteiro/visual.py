"""Visual — Estudativo · MAT-ESP-016: praticando pirâmides, cones e esfera (5 situações inéditas).
Mesma linguagem da trilha (MAT-ESP-001 a 015): sólidos do kit com as escondidas tracejadas, o elemento da vez na cor da matéria,
a 2ª família em cinza, resposta na esfera. Estrutura das aulas de prática (MAT-ESP-010, MAT-ANG-019): a pílula "situação n de 5"
com os pontos de progresso (situacao()), o enunciado à direita (pergunta()), a figura à esquerda e o relógio de pausa.
- Situação 1: a tenda (E.piramide quadrangular, na escala certa: baixa e larga) com o triângulo altura 3, apótema da base 4
  e apótema 5; as quatro paredes pintadas.
- Situação 2: a casquinha (casquinha(): o cone de ponta para baixo, com a boca inteira à vista); o atalho com os dois 3 riscados.
- Situação 3: o cone e a pirâmide de mesma altura lado a lado, as contas em duas colunas e as duas respostas em esferas.
- Situação 4: a garrafa de 1 L (garrafa()) e as bolinhas (E.esfera pequena) que saem dela, 9 inteiras.
- Situação 5: o reservatório de meia esfera de boca para cima (metade(), de MAT-ESP-015), sem tampa, com a água e a casca
  pintada; os círculos contados (2, e o 3º riscado).
Sem voz ainda: todo instante vem de C[...] (marcadores do roteiro)."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Espacial")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ESP-016_praticando_piramides_cones_e_esfera.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "questao5", "fim"))
BR = "#FFFFFF"
CINZA2 = E.mix(TINTA2, "#FFFFFF", 0.5)
IN = 22
SEN, COS = math.sin(math.radians(IN)), math.cos(math.radians(IN))
assert 8 // 2 == 4 and 3 ** 2 + 4 ** 2 == 5 ** 2 and 4 * 8 == 32 and 32 * 5 == 160 and 160 // 2 == 80 and 32 * 3 // 2 == 48
assert 3 ** 2 == 9 and 9 * 10 == 90 and 3 * 9 * 10 == 270 and 270 == 3 * 90
assert 4 ** 2 == 16 and 16 * 12 == 192 and 7 ** 2 == 49 and 12 // 3 == 4 and 49 * 4 == 196 and 196 - 192 == 4 and 2 * 4 == 8
assert 3 ** 3 == 27 and 4 * 27 == 108 and 1000 // 108 == 9 and 1000 % 108 == 28 and 9 * 108 == 972
assert 4 * 2 ** 3 == 32 and 32 // 2 == 16 and 16 * 1000 == 16000 and 3 * 2 ** 2 == 12 and 2 * 12 == 24


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


def face(c, pts, idx, a=1.0, cor=None, alfa_=0.42):
    if a <= 0:
        return
    p = skia.Path(); p.addPoly([pts[i] for i in idx], True)
    c.drawPath(p, M.paint(cor or E.COR, alfa_ * a))


def aresta(c, t, t0, P, Q, cor=None, largura=13, d=0.5, tracejada=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P, *Q, cor or E.COR, a, largura, dash=E.TRACO if tracejada else None, progress=p)


def reto(c, P, A, B, k=28, a=1.0, cor=None):
    if a <= 0:
        return
    def un(Q):
        dx, dy = Q[0] - P[0], Q[1] - P[1]
        n = math.hypot(dx, dy) or 1
        return dx / n * k, dy / n * k
    u, v = un(A), un(B)
    path = skia.Path()
    path.moveTo(P[0] + u[0], P[1] + u[1]); path.lineTo(P[0] + u[0] + v[0], P[1] + u[1] + v[1]); path.lineTo(P[0] + v[0], P[1] + v[1])
    c.drawPath(path, M.paint(cor or TINTA, a, stroke=4))


def rot(c, t, t0, s, P, Q, n, size=56, cor=None, gap=14, a=1.0):
    E.foco(c, t, t0, 0.4, lambda q: E._cola(c, s, (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2, n[0], n[1], gap, size, "g", cor or COR, q * a))


def situacao(c, t, t0, n, total=5):
    """situação n de 5, com os pontos de progresso (de MAT-ESP-010)"""
    s = f"situação {n} de {total}"
    w = E.larg(s, "b", 46) + 46 * 1.1

    def fn(a):
        E.pilula(c, s, XE + w / 2, 110, 46, estilo="b", a=a)
        for i in range(total):
            x = XE + w + 44 + i * 46
            if i < n:
                E.bola(c, x, 110, 15, a=a)
            else:
                c.drawCircle(x, 110, 14, M.paint(CINZA, a, stroke=4))
    E.foco(c, t, t0, 0.4, fn, sobe=6)


def pergunta(c, t, linhas, X=1350, y0=230, dy=100):
    for i, (t0, partes) in enumerate(linhas):
        E.frase(c, t, t0, partes, X, y0 + i * dy, "center", 0.1)


def riscado(c, t, t0, tr, partes, riscar, cx, y, size, cor=TINTA, cor_r=ERRADO):
    """fórmula em partes, centrada em cx; as partes em riscar levam um risco no instante tr"""
    ws = [E.formula(None, s_, 0, 0, size, "g", a=0) for s_ in partes]
    x = cx - sum(ws) / 2
    xs = []
    for w_ in ws:
        xs.append(x); x += w_
    E.foco(c, t, t0, 0.5, lambda q: [E.formula(c, s_, xx, y, size, "g", cor, q) for s_, xx in zip(partes, xs)])
    if t >= tr:
        for n, k in enumerate(riscar):
            E.risco(c, xs[k] - 8, y + 10, xs[k] + ws[k] + 8, y - size * 0.8, t, tr + 0.3 * n, cor_r, 9)


# ================= peças desta aula =================
def esfera(c, t, t0, cx, cy, r, raio=None, **kw):
    return E.esfera(c, t, t0, cx, cy, r, raio, inclina=IN, **kw)


def casquinha(c, t, t0, cx, cy, r, h, a=1.0, sorvete=0.0):
    """o cone de ponta para baixo: (cx, cy) = centro da boca; r e h em px. sorvete = 0..1 pinta o cone cheio"""
    if a <= 0:
        return
    ry, vy = r * SEN, cy + h * COS
    yt = ry * ry / (h * COS)
    xt = r * math.sqrt(max(0.0, 1 - (yt / ry) ** 2))
    p = ease_io(prog(t, t0, 1.0))
    q = ep(t, t0 + 0.5, 0.6) * a
    corpo = skia.Path()
    corpo.moveTo(cx, vy); corpo.lineTo(cx - xt, cy + yt)
    corpo.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180 - math.degrees(math.asin(yt / ry)), -(180 - 2 * math.degrees(math.asin(yt / ry))), False)
    corpo.close()
    if q > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeLinear([skia.Point(cx - r, 0), skia.Point(cx + r, 0)],
                    [M.hexc(E.mix(E.COR, "#FFFFFF", 0.62), q * 0.8), M.hexc(E.mix(E.COR, "#FFFFFF", 0.82), q * 0.8), M.hexc(E.mix(E.COR, "#FFFFFF", 0.5), q * 0.8)],
                    [0.0, 0.38, 1.0]))
        c.drawPath(corpo, g)
        el = skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry)
        c.drawOval(el, M.paint(E.mix(E.COR, "#FFFFFF", 0.75), q))
        if sorvete > 0:
            c.drawPath(corpo, M.paint(E.COR, 0.45 * sorvete * a))
            c.drawOval(el, M.paint(E.COR, 0.45 * sorvete * a))
    if p > 0:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, 360 * p, False, M.paint(TINTA, a, stroke=6, cap_round=True))
        M.line(c, cx, vy, cx - xt, cy + yt, TINTA, a, 6, progress=p)
        M.line(c, cx, vy, cx + xt, cy + yt, TINTA, a, 6, progress=p)
    return (cx, vy)


def metade(c, t, t0, cx, cy, r, a=1.0, agua=0.0, casca=0.0):
    """o reservatório: meia esfera de boca para cima, sem tampa (a E.esfera recortada, de MAT-ESP-015).
    agua = 0..1 enche de água; casca = 0..1 pinta a chapa"""
    if a <= 0:
        return
    ry = r * SEN
    cr, el = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry)
    p = skia.Path()
    p.moveTo(cx - r, cy); p.arcTo(cr, 180, -180, False); p.arcTo(el, 0, -180, False); p.close()
    c.save(); c.clipPath(p, skia.ClipOp.kIntersect, True)
    esfera(c, t, t0, cx, cy, r)
    c.restore()
    if casca > 0:
        pc = skia.Path()
        pc.moveTo(cx - r, cy); pc.arcTo(cr, 180, -180, False); pc.arcTo(el, 0, 180, False); pc.close()
        c.drawPath(pc, M.paint(E.COR, 0.4 * casca * a))
    c.drawOval(el, M.paint(E.mix(E.COR, "#FFFFFF", 0.85), a * ep(t, t0, 0.5)))   # o lado de dentro, à vista pela boca
    if agua > 0:
        c.drawOval(el, M.paint(E.COR, 0.5 * agua * a))
    c.drawOval(el, M.paint(TINTA, ep(t, t0, 0.5) * a, stroke=6))


def garrafa(c, cx, base, w, h, a=1.0, nivel=1.0):
    """garrafa de 1 litro: corpo arredondado com gargalo; nivel = 0..1 de borracha dentro"""
    if a <= 0:
        return
    x0, y0 = cx - w / 2, base - h
    gw, gh = w * 0.34, h * 0.18
    p = skia.Path()
    p.moveTo(cx - gw / 2, y0); p.lineTo(cx + gw / 2, y0); p.lineTo(cx + gw / 2, y0 + gh)
    p.quadTo(cx + w / 2, y0 + gh, cx + w / 2, y0 + gh * 2.1); p.lineTo(cx + w / 2, base - 24)
    p.quadTo(cx + w / 2, base, cx + w / 2 - 24, base); p.lineTo(x0 + 24, base); p.quadTo(x0, base, x0, base - 24)
    p.lineTo(x0, y0 + gh * 2.1); p.quadTo(x0, y0 + gh, cx - gw / 2, y0 + gh); p.close()
    c.drawPath(p, M.paint(E.mix(E.COR, "#FFFFFF", 0.88), a))
    if nivel > 0:
        c.save(); c.clipPath(p, skia.ClipOp.kIntersect, True)
        yn = base - (h - gh * 2.1) * nivel
        c.drawRect(skia.Rect.MakeLTRB(x0 - 5, yn, x0 + w + 5, base + 5), M.paint(E.COR, 0.5 * a))
        c.restore()
    pt = M.paint(TINTA, a, stroke=6); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def bolinhas(c, t, ts, x0, y0, r, cols, gap, a=1.0):
    """bolinhas (E.esfera pequenas) em grade, cada uma no seu instante"""
    for k, tk in enumerate(ts):
        q = ease_back(prog(t, tk, 0.4))
        if q > 0:
            x = x0 + (k % cols) * (2 * r + gap)
            y = y0 + (k // cols) * (2 * r + gap)
            esfera(c, 1e9, 0, x, y, r * q, preenche=0.6, largura=4)


def circulos(c, t, ts, x0, y, r, gap, cor=None, borda=TINTA, a=1.0):
    for k, tk in enumerate(ts):
        q = ease_back(prog(t, tk, 0.4))
        if q > 0:
            cx = x0 + k * (2 * r + gap)
            c.drawCircle(cx, y, r * q, M.paint(cor or E.COR, 0.85 * a))
            c.drawCircle(cx, y, r * q, M.paint(borda, a, stroke=5))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1 = C["s01.a"], C["s01.b"], C["s01.c"]
    E.frase(c, t, a1, [("5 situações", "g", 96, COR)], W / 2, 220, "center", 0.1)
    E.frase(c, t, a1 + 0.8, ps("criadas para esta aula", "i", 60, TINTA2), W / 2, 310, "center", 0.1)
    xs = (240, 600, 960, 1320, 1680)
    nomes = ("tenda", "casquinha", "pipoca", "bolinhas", "reservatório")
    tk0 = lerp(a1, b1, 0.3)
    for k, x in enumerate(xs):
        tk = tk0 + 0.6 * k
        E.foco(c, t, tk, 0.4, lambda q, k=k, x=x: (E.bola(c, x, 430, 34, a=q), centro(c, str(k + 1), x, 450, 46, "g", E.SOBRE, q)))
        E.foco(c, t, tk + 0.3, 0.4, lambda q, x=x, k=k: centro(c, nomes[k], x, 830, 46, "i", TINTA2, q))
    E.piramide(c, t, tk0, 240, 720, 4, 150, 110)
    casquinha(c, t, tk0 + 0.6, 600, 560, 75, 200)
    E.cone(c, t, tk0 + 1.2, 905, 730, 50, 170)
    E.piramide(c, t, tk0 + 1.3, 1030, 730, 4, 60, 170)
    for j in range(3):
        esfera(c, t, tk0 + 1.8 + 0.1 * j, 1270 + 50 * j, 690 - 30 * (j % 2), 40)
    metade(c, t, tk0 + 2.4, 1680, 620, 120)
    E.frase(c, t, b1, ps("primeiro passo:", "i", 60) + [("reconheça o sólido", "g", 64, COR)], W / 2, 940, "center", 0.1)
    E.foco(c, t, c1, 0.5, lambda q: E.pilula(c, "pause e resolva antes da resposta", W / 2, 1030, 52, "g", a=q, cor=E.SOBRE))


# ---------------- ferramentas ----------------
def b_lembrete(c, t, C, b):
    a2, b2, c2, d2 = (C[f"s02.{k}"] for k in "abcd")
    E.frase(c, t, C["s02"] + 0.3, ps("você vai usar", "i", 84), XE, 410, passo=0.14)
    E.foco(c, t, a2, 0.5, lambda a: E.escreve(c, "3", XE - 8, 720, 340, "g", COR, a))
    E.foco(c, t, a2 + 0.15, 0.5, lambda a: E.escreve(c, "famílias", XE + 215, 700, 110, "i", TINTA, a))
    x, w = 940, 880
    itens = (("s02.b", "pirâmide e cone:", "V = f{área da base × h}{3}"), ("s02.c", "apótema e geratriz:", "Pitágoras, altura em pé"),
             ("s02.d", "esfera:", "A = 4πr^2     V = f{4πr³}{3}"))
    for i, (k, l1, l2) in enumerate(itens):
        y = 170 + i * 260
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 220, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, ps(l1, "i", 56), x + 44, y + 72, "left", 0.1)
        E.formula_em(c, t, C[k] + 0.4, l2, x + 44, y + 172, 54, "g", COR)
    alvo = [170 + i * 260 + 180 for i in range(3)]
    q1, q2 = ease_io(prog(t, c2 - 0.35, 0.5)), ease_io(prog(t, d2 - 0.35, 0.5))
    E.cursor(c, x + w - 30, lerp(lerp(alvo[0], alvo[1], q1), alvo[2], q2), ep(t, b2, 0.4))
    E.frase(c, t, lerp(d2, C["s02.end"], 0.75), ps("travou?", "i", 54, COR) + ps("procure a aula no canal", "i", 54), x, 1010, "left", 0.12)


# ---------------- situação 1: a tenda ----------------
TX, TY, TR, TH = 470, 800, 360, 190   # lado 8 e altura 3 (64 px por metro): a tenda é baixa e larga


def tenda(c, t, t0):
    pts = E.piramide(c, t, t0, TX, TY, 4, TR, TH)
    i = max(range(4), key=lambda i: pts[i][1] + pts[(i + 1) % 4][1])
    Mf = ((pts[i][0] + pts[(i + 1) % 4][0]) / 2, (pts[i][1] + pts[(i + 1) % 4][1]) / 2)
    return pts, i, Mf


def b_questao1(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s03.{k}"] for k in "abcde")
    situacao(c, t, a3, 1)
    pts, i, Mf = tenda(c, t, b3)
    V, O = pts[4], (TX, TY)
    if t >= c3:
        rot(c, t, c3, "8 m", pts[i], pts[(i + 1) % 4], (0, 1), 54, COR)
    if t >= d3:
        aresta(c, t, d3, V, O, TINTA2, 6, tracejada=True)
        xc = TX - TR - 30
        aresta(c, t, d3, (xc, O[1]), (xc, V[1]), TINTA, 4)
        for yy in (O[1], V[1]):
            M.line(c, xc - 12, yy, xc + 12, yy, TINTA, ep(t, d3, 0.3), 4)
        E.foco(c, t, d3 + 0.3, 0.4, lambda q: E._cola(c, "3 m", xc, (O[1] + V[1]) / 2, 1, 0, 14, 54, "g", COR, q))
    pergunta(c, t, [(b3, ps("tenda:", "i", 60) + [("pirâmide de base quadrada", "g", 56, COR)]),
                    (c3, ps("lado", "i", 60) + [("8 m", "g", 62, COR)]),
                    (d3, ps("altura", "i", 60) + [("3 m", "g", 62, COR)]),
                    (e3, ps("quantos", "i", 60) + [("m²", "g", 62, COR)] + ps("de lona", "i", 60)),
                    (e3 + 1.0, ps("nas 4 paredes, sem o chão?", "i", 58))], X=1380, y0=200, dy=90)
    E.relogio(c, t, C["s04.a"], 1380, 810, 100)


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6 = (C[f"s06.{k}"] for k in "abcde")
    situacao(c, t, C["s05"], 1)
    pts, i, Mf = tenda(c, t, -1e9)
    V, O = pts[4], (TX, TY)
    rot(c, t, -1e9, "8 m", pts[i], pts[(i + 1) % 4], (0, 1), 54, COR)
    q = ep(t, a5, 0.5) * (1 - 0.6 * ep(t, b5, 0.4))
    for k in range(4):
        face(c, pts, (k, (k + 1) % 4, 4), q if k == i else q * 0.4, alfa_=0.4)
    aresta(c, t, C["s05"], V, O, TINTA2, 6, tracejada=True)
    E.foco(c, t, C["s05"], 0.4, lambda q2: E._cola(c, "3", O[0], (O[1] + V[1]) / 2, -1, 0, 14, 56, "g", TINTA, q2))
    if t >= b5:
        aresta(c, t, b5, V, Mf, None, 11)
    if t >= c5:
        aresta(c, t, c5, O, Mf, TINTA, 7)
        reto(c, O, V, Mf, 22, ep(t, c5 + 0.4, 0.3))
        rot(c, t, c5 + 0.3, "4", O, Mf, (1, 0.3), 56, TINTA)
    if t >= d5:
        rot(c, t, d5 + 0.3, "5", V, Mf, (1, -0.4), 60, COR, gap=18)
    X = 1380

    def apotema():
        E.frase(c, t, a5, [("4 triângulos", "g", 64, COR)], X, 240, "center", 0.1)
        E.frase(c, t, b5, ps("altura de cada um:", "i", 56) + [("a apótema", "g", 60, COR)], X, 360, "center", 0.1)
        E.frase(c, t, b5 + 1.0, ps("não a altura da tenda", "i", 52, TINTA2), X, 440, "center", 0.1)
        fcen(c, t, c5, "8 ÷ 2 = 4", X, 590, 76)
        E.frase(c, t, c5 + 0.6, ps("a apótema da base", "i", 50, TINTA2), X, 670, "center", 0.1)
        E.foco(c, t, d5, 0.5, lambda q: E.pilula(c, "terno 3, 4 e 5", X - 170, 820, 56, "g", a=q, cor=E.SOBRE, fundo=TINTA))
        bola_txt(c, t, d5 + 0.5, "5 m", X + 220, 820, 90, 60)
    fase(c, t, C["s05"], C["s06"] - 0.1, apotema)
    if t < C["s06"] - 0.1:
        return
    fcen(c, t, C["s06"] + 0.1, "lateral = f{perímetro × apótema}{2}", X, 250, 54, TINTA2)
    fcen(c, t, a6, "4 × 8 = 32", X, 420, 76)
    fcen(c, t, b6, "32 × 5 = 160", X, 540, 76)
    fcen(c, t, c6, "160 ÷ 2", X - 190, 720, 80)
    bola_txt(c, t, c6 + 0.6, "80 m²", X + 200, 695, 110, 64)
    fcen(c, t, d6, "32 × 3 ÷ 2 = 48", X - 60, 930, 66, ERRADO)
    E.foco(c, t, d6 + 0.5, 0.5, lambda q: E.selo(c, X + 270, 905, 40, False, q))
    E.frase(c, t, e6, [("faltaria lona", "g", 54, ERRADO)], X, 1020, "center", 0.1)


# ---------------- situação 2: a casquinha ----------------
KX, KY, KR, KH = 470, 300, 150, 500   # raio 3 e altura 10 (50 px por cm)


def b_questao2(c, t, C, b):
    a7, b7, c7, d7, e7, f7 = (C[f"s07.{k}"] for k in "abcdef")
    situacao(c, t, a7, 2)
    Vp = casquinha(c, t, b7, KX, KY, KR, KH)
    if t >= c7:
        aresta(c, t, c7, (KX, KY), (KX + KR, KY), TINTA, 6)
        E.foco(c, t, c7 + 0.3, 0.4, lambda q: E._cola(c, "3 cm", KX + KR / 2, KY - KR * SEN, 0, -1, 8, 52, "g", COR, q))
    if t >= d7:
        aresta(c, t, d7, (KX, KY), Vp, TINTA2, 6, tracejada=True)
        xc = KX + KR + 50
        aresta(c, t, d7, (xc, KY), (xc, Vp[1]), TINTA, 4)
        for yy in (KY, Vp[1]):
            M.line(c, xc - 12, yy, xc + 12, yy, TINTA, ep(t, d7, 0.3), 4)
        E.foco(c, t, d7 + 0.3, 0.4, lambda q: E._cola(c, "10 cm", xc, (KY + Vp[1]) / 2, 1, 0, 14, 52, "g", COR, q))
    pergunta(c, t, [(b7, ps("casquinha:", "i", 60) + [("cone", "g", 64, COR)]),
                    (c7, ps("raio", "i", 60) + [("3 cm", "g", 62, COR)]),
                    (d7, ps("altura", "i", 60) + [("10 cm", "g", 62, COR)]),
                    (e7, [("π = 3", "g", 62, COR)]),
                    (f7, ps("quantos", "i", 60) + [("mL", "g", 62, COR)] + ps("cabem, até a borda?", "i", 60))], X=1380, y0=200, dy=90)
    E.relogio(c, t, C["s08.a"], 1380, 810, 100)


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9, e9, f9, g9 = (C[f"s09.{k}"] for k in "abcdefg")
    situacao(c, t, C["s09"], 2)
    Vp = casquinha(c, t, -1e9, KX, KY, KR, KH, sorvete=ep(t, f9, 0.8))
    M.line(c, KX, KY, KX + KR, KY, TINTA, 1, 6)
    E._cola(c, "3", KX + KR / 2, KY - KR * SEN, 0, -1, 8, 52, "g", TINTA, 1)
    M.line(c, KX, KY, Vp[0], Vp[1], TINTA2, 1, 6, dash=E.TRACO)
    xc = KX + KR + 50
    M.line(c, xc, KY, xc, Vp[1], TINTA, 1, 4)
    for yy in (KY, Vp[1]):
        M.line(c, xc - 12, yy, xc + 12, yy, TINTA, 1, 4)
    E._cola(c, "10", xc, (KY + Vp[1]) / 2, 1, 0, 14, 52, "g", TINTA, 1)
    X = 1380
    fcen(c, t, a9, "cone = f{1}{3} do cilindro", X, 250, 64)
    riscado(c, t, b9, b9 + 0.8, ("V = ", "3", " · r² · h ÷ ", "3"), (1, 3), X, 410, 84)
    fcen(c, t, c9, "V = r² · h", X, 540, 92, COR)
    fcen(c, t, d9, "3² = 9", X, 650, 74)
    fcen(c, t, e9, "9 × 10 = 90 cm³", X, 760, 74)
    bola_txt(c, t, f9, "90 mL", X - 260, 910, 95, 58)
    fcen(c, t, g9, "3 × 9 × 10 = 270", X + 170, 900, 56, ERRADO)
    E.foco(c, t, g9 + 0.6, 0.5, lambda q: E.pilula(c, "o triplo", X + 170, 990, 46, "g", a=q, cor=E.SOBRE, fundo=ERRADO))


# ---------------- situação 3: a pipoca ----------------
S3 = 26                          # px por cm
CX3, PX3, Y3 = 330, 800, 900     # o cone (raio 4) e a pirâmide (lado 7), altura 12
PR3 = 7 * S3 / math.sqrt(2)      # raio da base quadrada


def pacotes(c, t, t_cone, t_pir, t_h=None, tr=None, tl=None, a_cone=1.0, a_pir=1.0):
    E.cone(c, t, t_cone, CX3, Y3, 4 * S3, 12 * S3, "4", None, size=50, tm=tr if tr is not None else 1e9)
    E.piramide(c, t, t_pir, PX3, Y3, 4, PR3, 12 * S3, None, "7", size=50, tm=tl if tl is not None else 1e9)
    if t_h is not None and t >= t_h:
        for x in (CX3 + 4 * S3 + 30, PX3 + PR3 + 20):
            aresta(c, t, t_h, (x, Y3), (x, Y3 - 12 * S3 * COS), TINTA, 4)
            E.foco(c, t, t_h + 0.3, 0.4, lambda q, x=x: E._cola(c, "12", x, Y3 - 6 * S3 * COS, 1, 0, 12, 50, "g", COR, q))


def b_questao3(c, t, C, b):
    a0, b0, c0, d0, e0, f0 = (C[f"s10.{k}"] for k in "abcdef")
    situacao(c, t, a0, 3)
    pacotes(c, t, c0, d0, t_h=b0, tr=c0 + 0.6, tl=d0 + 0.6)
    E.foco(c, t, c0 + 0.5, 0.4, lambda q: centro(c, "cone", CX3, Y3 + 150, 50, "g", TINTA, q))
    E.foco(c, t, d0 + 0.5, 0.4, lambda q: centro(c, "pirâmide", PX3, Y3 + 150, 50, "g", TINTA, q))
    pergunta(c, t, [(b0, ps("mesma altura:", "i", 58) + [("12 cm", "g", 62, COR)]),
                    (c0, ps("cone de raio", "i", 58) + [("4 cm", "g", 62, COR)]),
                    (d0, ps("pirâmide de lado", "i", 58) + [("7 cm", "g", 62, COR)]),
                    (e0, [("π = 3", "g", 62, COR)]),
                    (f0, ps("qual cabe", "i", 60) + [("mais pipoca?", "g", 64, COR)])], X=1490, y0=200, dy=90)
    E.relogio(c, t, C["s11.a"], 1490, 810, 100)


def b_resposta3(c, t, C, b):
    a2, b2, c2, d2, e2, f2 = (C[f"s12.{k}"] for k in "abcdef")
    a3, b3, c3 = C["s13.a"], C["s13.b"], C["s13.c"]
    situacao(c, t, C["s12"], 3)
    pacotes(c, t, -1e9, -1e9, t_h=-1e9, tr=-1e9, tl=-1e9)
    if t >= b3:
        yt = Y3 - 12 * S3 * COS + 0
        aresta(c, t, b3, (CX3 - 4 * S3, Y3), (CX3 + 4 * S3, Y3), ERRADO, 7)
        E.foco(c, t, b3 + 0.3, 0.4, lambda q: centro(c, "boca: 8 cm", CX3, Y3 + 110, 50, "g", ERRADO, q))
    X1, X2 = 1240, 1650
    fcen(c, t, a2, "f{1}{3} da base × altura", (X1 + X2) / 2, 250, 60, TINTA2)
    E.foco(c, t, b2 - 0.3, 0.4, lambda q: (centro(c, "cone", X1, 360, 56, "g", COR, q)))
    E.foco(c, t, d2 - 0.3, 0.4, lambda q: (centro(c, "pirâmide", X2, 360, 56, "g", COR, q)))
    fcen(c, t, b2, "4² = 16", X1, 480, 70)
    fcen(c, t, c2, "16 × 12", X1, 600, 70)
    fcen(c, t, d2, "7² = 49", X2, 480, 70)
    fcen(c, t, e2, "12 ÷ 3 = 4", X2, 600, 70)
    fcen(c, t, f2, "49 × 4", X2, 720, 70)
    win = ep(t, a3, 0.5)
    bola_txt(c, t, c2 + 0.6, "192", X1, 790, 85 - 15 * win, 60 - 10 * win, E.mix(TINTA2, E.COR, 1 - win))
    bola_txt(c, t, f2 + 0.6, "196", X2, 870, 85 + 20 * win, 60 + 10 * win)
    E.frase(c, t, a3 + 0.3, [("+4 cm³", "g", 54, COR)] + ps("na pirâmide", "i", 50), X2, 1045, "center", 0.1)
    E.foco(c, t, c3, 0.5, lambda q: E.pilula(c, "a conta decide", X1 - 20, 1030, 46, "g", a=q, cor=E.SOBRE))


# ---------------- situação 4: as bolinhas ----------------
BX4, BY4 = 330, 900   # a garrafa


def b_questao4(c, t, C, b):
    a4, b4, c4, d4, e4 = (C[f"s14.{k}"] for k in "abcde")
    situacao(c, t, a4, 4)
    E.foco(c, t, b4, 0.5, lambda q: garrafa(c, BX4, BY4, 260, 520, q))
    E.foco(c, t, b4 + 0.4, 0.4, lambda q: centro(c, "1 L", BX4, BY4 - 160, 80, "g", BR, q))
    if t >= c4:
        esfera(c, t, c4, 800, 700, 120, "3 cm", size=50, tm=c4 + 0.5)
    pergunta(c, t, [(b4, [("1 litro", "g", 62, COR)] + ps("de borracha", "i", 60)),
                    (c4, ps("bolinhas maciças de", "i", 58) + [("raio 3 cm", "g", 62, COR)]),
                    (d4, [("π = 3", "g", 62, COR)]),
                    (e4, ps("quantas bolinhas", "i", 60) + [("inteiras?", "g", 64, COR)])], X=1420, y0=280, dy=110)
    E.relogio(c, t, C["s15.a"], 1420, 800, 100)


def b_resposta4(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    a7, b7, c7, d7 = (C[f"s17.{k}"] for k in "abcd")
    situacao(c, t, C["s16"], 4)
    garrafa(c, BX4, BY4, 260, 520, 1.0, 1 - 0.972 * ease_io(prog(t, b7, 1.4)))
    centro(c, "1 L", BX4, BY4 - 160, 80, "g", BR if t < b7 + 0.7 else TINTA)
    X = 1380

    def uma():
        esfera(c, t, C["s16"], 800, 700, 120, "3", size=52, tm=C["s16"] + 0.4)
        E.frase(c, t, a6, ps("bolinha =", "i", 60) + [("esfera", "g", 64, COR)], X, 250, "center", 0.1)
        fcen(c, t, b6, "V = 4r^3", X, 400, 90, COR)
        E.frase(c, t, b6 + 0.6, ps("com π = 3", "i", 50, TINTA2), X, 470, "center", 0.1)
        fcen(c, t, c6, "3³ = 27", X, 610, 76)
        fcen(c, t, d6, "4 × 27 = 108 cm³", X, 750, 76)
        E.frase(c, t, d6 + 0.8, ps("por bolinha", "i", 52, TINTA2), X, 830, "center", 0.1)
    fase(c, t, C["s16"], C["s17"] - 0.1, uma)
    if t < C["s17"] - 0.1:
        return
    fcen(c, t, C["s17"] + 0.1, "108 cm³ por bolinha", X, 230, 54, TINTA2)
    fcen(c, t, a7, "1 L = 1.000 cm³", X, 360, 76)
    fcen(c, t, b7, "1.000 ÷ 108 = 9", X, 490, 76)
    fcen(c, t, c7, "9 × 108 = 972: sobram 28", X, 610, 62, TINTA2)
    E.frase(c, t, c7 + 1.0, ps("28 não fazem outra bolinha", "i", 50, ERRADO), X, 700, "center", 0.1)
    bolinhas(c, t, [b7 + 0.15 * k for k in range(9)], 640, 520, 42, 3, 22)
    bola_txt(c, t, d7, "9", X - 150, 870, 90, 90)
    E.frase(c, t, d7 + 0.3, [("bolinhas", "g", 60, COR)], X - 30, 895, "left", 0.1)


# ---------------- situação 5: o reservatório ----------------
RX5, RY5, RR5 = 470, 560, 280   # raio 2 (140 px por metro)


def b_questao5(c, t, C, b):
    a8, b8, c8, d8, e8, f8 = (C[f"s18.{k}"] for k in "abcdef")
    situacao(c, t, a8, 5)
    metade(c, t, b8, RX5, RY5, RR5)
    if t >= c8:
        aresta(c, t, c8, (RX5, RY5), (RX5 + RR5, RY5), TINTA, 6)
        E.foco(c, t, c8 + 0.3, 0.4, lambda q: E._cola(c, "2 m", RX5 + RR5 / 2, RY5, 0, -1, 8, 54, "g", COR, q))
    pergunta(c, t, [(b8, [("meia esfera,", "g", 60, COR)] + ps("boca para cima", "i", 58)),
                    (b8 + 1.2, ps("e", "i", 58) + [("sem tampa", "g", 60, COR)]),
                    (c8, ps("raio", "i", 60) + [("2 m", "g", 62, COR)]),
                    (d8, [("π = 3", "g", 62, COR)]),
                    (e8, [("1)", "g", 58, COR)] + ps("quantos litros guarda?", "i", 58)),
                    (f8, [("2)", "g", 58, COR)] + ps("quantos", "i", 58) + [("m²", "g", 60)] + ps("de chapa?", "i", 58))],
             X=1380, y0=230, dy=95)
    E.relogio(c, t, C["s19.a"], 1380, 850, 90)


def b_resposta5(c, t, C, b):
    a0, b0, c0, d0, e0 = (C[f"s20.{k}"] for k in "abcde")
    a1, b1, c1, d1 = (C[f"s21.{k}"] for k in "abcd")
    situacao(c, t, C["s20"], 5)
    metade(c, t, -1e9, RX5, RY5, RR5, agua=ep(t, e0, 0.8) * (1 - ep(t, C["s21"], 0.4)), casca=ep(t, a1, 0.5))
    M.line(c, RX5, RY5, RX5 + RR5, RY5, TINTA, 1, 6)
    E._cola(c, "2", RX5 + RR5 / 2, RY5, 0, -1, 8, 54, "g", TINTA, 1)
    X = 1380

    def litros():
        E.frase(c, t, a0, ps("meia esfera =", "i", 60) + [("hemisfério", "g", 64, COR)], X, 240, "center", 0.1)
        fcen(c, t, b0, "esfera: 4 × 2³ = 32 m³", X, 390, 72)
        fcen(c, t, c0, "32 ÷ 2 = 16 m³", X, 530, 76, COR)
        fcen(c, t, d0, "1 m³ = 1.000 L", X, 670, 66, TINTA2)
        bola_txt(c, t, e0, "16.000 L", X, 860, 125, 52)
    fase(c, t, C["s20"], C["s21"] - 0.1, litros)
    if t < C["s21"] - 0.1:
        return
    E.frase(c, t, C["s21"] + 0.1, ps("a chapa:", "i", 60) + [("conte círculos", "g", 64, COR)], X, 220, "center", 0.1)
    E.frase(c, t, a1, ps("meia casca =", "i", 58) + [("2 círculos", "g", 62, COR)], X, 340, "center", 0.1)
    circulos(c, t, (a1 + 0.3, a1 + 0.5), X - 200, 470, 70, 60)
    q = ep(t, b1, 0.4)
    if q > 0:
        pt = M.paint(TINTA2, q, stroke=5); pt.setPathEffect(skia.DashPathEffect.Make(E.TRACO, 0))
        c.drawCircle(X + 200, 470, 70, pt)
        E.risco(c, X + 140, 530, X + 260, 410, t, b1 + 0.3, ERRADO, 9)
        E.frase(c, t, b1 + 0.3, ps("sem tampa: não entra", "i", 52, ERRADO), X + 200, 600, "center", 0.1)
    fcen(c, t, c1, "1 círculo: 3 × 2² = 12", X, 740, 70)
    fcen(c, t, d1, "2 × 12", X - 190, 920, 78)
    bola_txt(c, t, d1 + 0.6, "24 m²", X + 200, 895, 110, 60)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s22.a", [("reconheça o sólido", "g", 62, COR)]),
                 ("s22.b", ps("a pergunta quer o", "i", 60) + [("de dentro", "g", 62, COR)] + ps("ou a", "i", 60) + [("casca?", "g", 62, COR)]),
                 ("s22.c", ps("a altura é a", "i", 60) + [("de dentro", "g", 62, COR)] + ps("ou a", "i", 60) + [("inclinada?", "g", 62, COR)]))
        for i, (k, l1) in enumerate(itens):
            y = 400 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 25, 52, a=a), centro(c, str(i + 1), 260, y - 4, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, l1, 350, y, "left", 0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    a3, b3, c3, d3, e3 = (C[f"s23.{k}"] for k in "abcde")
    E.frase(c, t, C["s23"] + 0.2, ps("na próxima aula", "i", 80), XE, 260, passo=0.12)
    E.frase(c, t, C["s23"] + 0.8, [("juntar", "g", 120, COR)] + ps("sólidos", "i", 100), XE, 410)
    E.frase(c, t, a3, ps("um", "i", 58) + [("silo:", "g", 60, COR)] + ps("cilindro + cone", "i", 58), XE, 540, passo=0.1)
    E.frase(c, t, b3, ps("uma peça com", "i", 58) + [("furo", "g", 60, COR)], XE, 640, passo=0.1)
    E.frase(c, t, c3, ps("somar e", "i", 64) + [("subtrair", "g", 66, COR)] + ps("volumes", "i", 64), XE, 760, passo=0.1)
    E.cilindro(c, t, a3, 1300, 900, 100, 260)
    E.cone(c, t, a3 + 0.4, 1300, 900 - 260 * COS, 100, 150)
    E.cilindro(c, t, b3, 1640, 900, 130, 120)
    if t >= b3 + 0.6:
        pt = M.paint(TINTA, ep(t, b3 + 0.6, 0.4), stroke=5)
        c.drawOval(skia.Rect.MakeXYWH(1640 - 45, 900 - 120 * COS - 45 * SEN, 90, 90 * SEN), M.paint(E.COR, 0.5 * ep(t, b3 + 0.6, 0.4)))
        c.drawOval(skia.Rect.MakeXYWH(1640 - 45, 900 - 120 * COS - 45 * SEN, 90, 90 * SEN), pt)
    E.foco(c, t, d3, 0.5, lambda a: E.pilula(c, "Inscreva-se", 1500, 330, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, d3 + 0.3, 0.8))
    E.cursor(c, lerp(1830, 1630, p), lerp(560, 355, p), ep(t, d3 + 0.2, 0.4))
    E.frase(c, t, e3, [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 1040, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, questao5=b_questao5,
              resposta5=b_resposta5, fim=b_fim)
