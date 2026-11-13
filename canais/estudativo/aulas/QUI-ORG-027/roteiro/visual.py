"""Visual — Estudativo · QUI-ORG-027: polímeros naturais, plásticos e reciclagem.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001) e a LINGUAGEM DOS POLÍMEROS de QUI-ORG-025. Nesta aula, os
polímeros aparecem como CORRENTES de contas: glicose = hexágono claro (amido e celulose), aminoácido = conta colorida
(proteína), isopreno = zigue-zague com dupla (borracha), ponte de enxofre = bolinha amarela ligando duas cadeias.
TERMOPLÁSTICO = fios soltos (espaguete) que deslizam no calor; TERMOFIXO = rede com nós (ligações fortes) que não se mexe.
Calor = brilho âmbar no fundo do quadro. Reciclagem = triângulo com o número da embalagem.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-027_polimeros_naturais_plasticos_reciclagem.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("natural", "termo", "recicla", "atalho", "questao", "fim"))

# a glicose entra na cadeia soltando água: n C6H12O6 → (C6H10O5)n + n H2O (para n = 3)
assert Q.lados("3 C6H12O6 -> C18H30O15 + 3 H2O")[0] == Q.lados("3 C6H12O6 -> C18H30O15 + 3 H2O")[1]
assert Q.contar("C5H8") == {"C": 5, "H": 8}  # isopreno, o monômero da borracha
CODIGOS = {1: "PET", 2: "PEAD", 3: "PVC", 4: "PEBD", 5: "PP", 6: "PS", 7: "outros"}


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da Orgânica (candidatas ao kit quimica.py; iguais em todas as aulas QUI-ORG-015 a 028) ----------------
BR = "#FFFFFF"


def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, escuro=False):
    """lista numerada: itens = [(instante, partes da frase)]"""
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, 44, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def rot(c, s, cx, cy, size, cor=None, a=1.0, escuro=False):
    """rótulo químico (CH3, OH, COOH) centrado em (cx, cy) nas duas direções"""
    if a > 0 and s:
        Q.formula(c, s, cx, cy + size * 0.36, size, cor, a, "center", escuro=escuro)


def _meia(s, size):
    """meia largura e meia altura da caixa de um rótulo"""
    if not s:
        return size * 0.05, size * 0.05
    return Q.formula(None, s, 0, 0, size) / 2, size * 0.42


def _corta(P, s, size, ux, uy, folga):
    """distância do centro do rótulo até a borda dele na direção (ux, uy)"""
    w, h = _meia(s, size)
    if not s:
        return 0
    k = min(w / abs(ux) if abs(ux) > 1e-6 else 1e9, h / abs(uy) if abs(uy) > 1e-6 else 1e9)
    return k + folga


def estr(c, t, t0, atomos, ligs, cx, cy, esc=150, size=80, tl=None, passo=0.12, cores=None, escuro=False, a=1.0, cor_lig=None, d=0.4):
    """fórmula estrutural plana com rótulos químicos: atomos = [(rótulo, x, y)] em unidades de ligação (rótulo "" = vértice
    sem letra); ligs = [(i, j, ordem[, cor])]. Cada átomo entra no seu instante (tl ou t0 + i·passo); a ligação cresce quando as
    duas pontas existem. cores = {i: cor} pinta o rótulo i. t0 = None desenha parado. Devolve os pontos na tela"""
    tinta = Q._tinta(escuro)
    pts = [(cx + x * esc, cy + y * esc) for _, x, y in atomos]
    ts = [(tl[i] if tl else (t0 if t0 is not None else -99) + i * passo) for i in range(len(atomos))]
    lw = max(5, size * 0.075)
    for lg in ligs:
        i, j, o = lg[0], lg[1], lg[2]
        cr = lg[3] if len(lg) > 3 and lg[3] else (cor_lig or tinta)
        p = 1.0 if t0 is None else ease_out(prog(t, max(ts[i], ts[j]) + 0.2, 0.4))
        if p <= 0 or o <= 0:
            continue
        A, B = pts[i], pts[j]
        ux, uy = E._uni(*A, *B)
        nx, ny = -uy, ux
        ra = _corta(A, atomos[i][0], size, ux, uy, size * 0.14)
        rb = _corta(B, atomos[j][0], size, ux, uy, size * 0.14)
        A2, B2 = (A[0] + ux * ra, A[1] + uy * ra), (B[0] - ux * rb, B[1] - uy * rb)
        g = size * 0.17
        for k in {1: (0,), 2: (-0.5, 0.5), 3: (-1, 0, 1)}[o]:
            M.line(c, A2[0] + nx * k * g, A2[1] + ny * k * g, B2[0] + nx * k * g, B2[1] + ny * k * g, cr, a, lw, progress=p)
    for i, (s, _, _) in enumerate(atomos):
        cr = (cores or {}).get(i, None)
        if t0 is None:
            rot(c, s, *pts[i], size, cr, a, escuro)
        else:
            E.foco(c, t, ts[i], d, lambda q, s=s, i=i, cr=cr: rot(c, s, *pts[i], size, cr, q * a, escuro))
    return pts


# alceno plano: os dois carbonos da dupla na horizontal e os quatro ligantes a 120°
ALC = [("C", -0.62, 0), ("C", 0.62, 0), (None, -1.25, -0.95), (None, -1.25, 0.95), (None, 1.25, -0.95), (None, 1.25, 0.95)]


def alceno(c, t, t0, cx, cy, subs, esc=150, size=80, tl=None, cores=None, escuro=False, a=1.0, ordem=2, carbonos=("C", "C"), cor_dupla=None):
    """subs = (em cima à esquerda, embaixo à esquerda, em cima à direita, embaixo à direita). Devolve os 6 pontos"""
    at = [(carbonos[0], -0.62, 0), (carbonos[1], 0.62, 0)] + [(s, x, y) for s, (_, x, y) in zip(subs, ALC[2:])]
    ligs = [(0, 1, ordem, cor_dupla), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, tl, 0.1, cores, escuro, a)


def colchetes(c, x0, x1, cy, h, a=1.0, cor=None, n="n", size=64, escuro=False):
    """[ ... ]n em volta da unidade que se repete"""
    if a <= 0:
        return
    cr = cor or Q._tinta(escuro)
    lw, k = 6, h * 0.12
    for x, s in ((x0, 1), (x1, -1)):
        pth = skia.Path(); pth.moveTo(x + s * k, cy - h / 2); pth.lineTo(x, cy - h / 2); pth.lineTo(x, cy + h / 2); pth.lineTo(x + s * k, cy + h / 2)
        c.drawPath(pth, M.paint(cr, a, stroke=lw))
    if n:
        E.escreve(c, n, x1 + 12, cy + h / 2 + size * 0.2, size, "g", cr, a)


def espelho(c, x, y0, y1, a=1.0, escuro=False):
    """espelho visto de lado: faixa azulada com fio tracejado"""
    if a <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(x - 22, 0), skia.Point(x + 22, 0)],
                                               [M.hexc("#9CC9E8", 0.0), M.hexc("#9CC9E8", 0.55 * a), M.hexc("#9CC9E8", 0.0)], [0, 0.5, 1]))
    c.drawRect(skia.Rect.MakeLTRB(x - 22, y0, x + 22, y1), p)
    M.line(c, x, y0, x, y1, "#5B8DB8", a, 4, dash=[18, 12])


def seta_em(c, t, t0, x0, x1, y, size=80, rotulo=None, escuro=False, eq=False, cor=None, d=0.6):
    """seta da reação que cresce a partir de t0; y = linha de base do texto ao lado"""
    p = ease_out(prog(t, t0, d))
    if p > 0:
        Q.seta_reacao(c, x0, x1, y, size, cor or (E.CLARO if escuro else E.COR), 1.0, p, eq, rotulo, escuro)


def x_em(c, t, t0, cx, cy, r=34, ok=False):
    """selo de certo ou errado que entra com salto"""
    q = ease_back(prog(t, t0, 0.45))
    if q > 0:
        E.selo(c, cx, cy, r * q, ok, min(1, q))


def anel(c, cx, cy, r, a=1.0, cor=None, lw=7, giro=90):
    """benzeno em bastão: hexágono com três duplas por dentro"""
    if a <= 0:
        return []
    cr = cor or TINTA
    v = [(cx + r * math.cos(math.radians(giro + 60 * k)), cy - r * math.sin(math.radians(giro + 60 * k))) for k in range(6)]
    for k in range(6):
        M.line(c, *v[k], *v[(k + 1) % 6], cr, a, lw)
        if k % 2 == 0:
            A, B = v[k], v[(k + 1) % 6]
            mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
            ux, uy = cx - mx, cy - my
            n = math.hypot(ux, uy)
            ux, uy = ux / n * r * 0.17, uy / n * r * 0.17
            M.line(c, lerp(A[0], B[0], 0.18) + ux, lerp(A[1], B[1], 0.18) + uy, lerp(A[0], B[0], 0.82) + ux, lerp(A[1], B[1], 0.82) + uy, cr, a, lw)
    return v


def circ(c, t, t0, cx, cy, r, cor=None, lw=7, t1=None):
    """círculo de destaque que se fecha em volta de algo"""
    if t < t0 or (t1 is not None and t >= t1 + 0.4):
        return
    p = ease_out(prog(t, t0, 0.45))
    a = 1 - ep(t, t1, 0.4) if t1 is not None else 1
    pth = skia.Path(); pth.addArc(skia.Rect.MakeLTRB(cx - r, cy - r, cx + r, cy + r), -90, 360 * p)
    c.drawPath(pth, M.paint(cor or E.COR, a, stroke=lw))


def caixa(c, t, t0, x, y, w, h, cor=None, t1=None):
    """caixa pontilhada que se desenha (x, y = canto de cima à esquerda)"""
    if t < t0 or (t1 is not None and t >= t1 + 0.4):
        return
    p = ep(t, t0, 0.4)
    a = 1 - ep(t, t1, 0.4) if t1 is not None else 1
    E.caixa_pontilhada(c, x, y, w, h, p * a, cor, prog_=p)


def caixa_rot(c, t, t0, P, s, size, cor=None, pad=14, t1=None):
    """caixa pontilhada em volta de um rótulo da estrutura (P = centro dele)"""
    w, h = _meia(s, size)
    caixa(c, t, t0, P[0] - w - pad, P[1] - h - pad, 2 * (w + pad), 2 * (h + pad), cor, t1)


# (peças copiadas de QUI-ORG-023)
def cauda(c, x0, y0, n=9, L=58, dobra=False, a=1.0, cor=None, p=1.0, escuro=False):
    """cadeia de ácido graxo em bastão, da cabeça (x0, y0) para a esquerda; dobra = óleo (dupla e cadeia entortada)"""
    cr = cor or Q._tinta(escuro)
    pts, bx, by, ang = [(x0, y0)], x0, y0, 180.0
    for k in range(1, n):
        if dobra and k == n // 2:
            ang = 200.0
        ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
        bx, by = bx + ux * L * 0.87, by + uy * L * 0.87
        off = L * 0.25 * (1 if k % 2 else -1)
        pts.append((bx - uy * off, by + ux * off))
    m = max(1, int(round(p * (len(pts) - 1))))
    for i in range(m):
        A, B = pts[i], pts[i + 1]
        dupla = dobra and i == n // 2 - 1
        M.line(c, *A, *B, E.COR if dupla else cr, a, 6)
        if dupla:
            ux, uy = E._uni(*A, *B)
            M.line(c, A[0] - uy * 12 + ux * 8, A[1] + ux * 12 + uy * 8, B[0] - uy * 12 - ux * 8, B[1] + ux * 12 - uy * 8, E.COR, a, 6)
    return pts


# ---------------- peças desta aula ----------------
AMBAR = "#F2994A"


def corrente(c, t, t0, x0, y, n, passo_x=150, tipo="glicose", a=1.0, cores=None, onda=0.0):
    """cadeia de contas: glicose (hexágono) ou aminoácido (bolinhas de cores variadas). Devolve os centros"""
    pts = []
    for i in range(n):
        x = x0 + i * passo_x
        yy = y + (24 * math.sin(i * 1.3 + onda) if tipo == "aminoacido" else 0)
        pts.append((x, yy))
    for i, (x, yy) in enumerate(pts):
        q = 1.0 if t0 is None else ease_back(prog(t, t0 + 0.12 * i, 0.4))
        if q <= 0:
            continue
        if i > 0:
            M.line(c, pts[i - 1][0], pts[i - 1][1], x, yy, TINTA2, a * min(1, q), 6)
        if tipo == "glicose":
            E.hexagono(c, x, yy, 44 * q, "#E8D9A8", a * min(1, q), sombra=False)
        else:
            cr = (cores or ["#E07A5F", "#3D85C6", "#81B29A", "#F2CC8F", "#9B5DE5"])[i % 5]
            E.bola(c, x, yy, 34 * q, cr, a * min(1, q))
    return pts


def calor(c, t, t0, a=1.0, t1=None):
    """brilho âmbar no pé do quadro: está quente"""
    q = ep(t, t0, 0.6) * a * (1 - (ep(t, t1, 0.5) if t1 is not None else 0))
    if q <= 0:
        return
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, H), skia.Point(0, H - 420)], [M.hexc(AMBAR, 0.45 * q), M.hexc(AMBAR, 0)], [0, 1]))
    c.drawRect(skia.Rect.MakeLTRB(0, H - 420, W, H), p)


def espaguete(c, t, cx, cy, w, h, mexe=0.0, a=1.0, n=7):
    """fios soltos; mexe > 0 faz os fios deslizarem uns sobre os outros"""
    for k in range(n):
        y0 = cy - h / 2 + k * h / (n - 1)
        dx = mexe * 60 * math.sin(t * 2 + k * 1.7)
        pth = skia.Path(); pth.moveTo(cx - w / 2 + dx, y0)
        for j in range(1, 9):
            x = cx - w / 2 + j * w / 8 + dx
            pth.lineTo(x, y0 + 26 * math.sin(j * 1.2 + k * 2.1))
        c.drawPath(pth, M.paint(["#D98E04", "#B46F00", "#E3A21A"][k % 3], a, stroke=9))


def rede(c, cx, cy, w, h, a=1.0, cor=None, nos=True):
    """cadeias amarradas: grade com nós fortes nos cruzamentos"""
    cr = cor or TINTA
    cols, lins = 6, 4
    for i in range(cols):
        x = cx - w / 2 + i * w / (cols - 1)
        M.line(c, x, cy - h / 2, x, cy + h / 2, cr, a, 6)
    for j in range(lins):
        y = cy - h / 2 + j * h / (lins - 1)
        M.line(c, cx - w / 2, y, cx + w / 2, y, cr, a, 6)
    if nos:
        for i in range(cols):
            for j in range(lins):
                E.bola(c, cx - w / 2 + i * w / (cols - 1), cy - h / 2 + j * h / (lins - 1), 12, E.COR, a)


def tri_recicla(c, cx, cy, s, n, a=1.0, cor=None):
    """triângulo de reciclagem com o número da embalagem"""
    if a <= 0:
        return
    cr = cor or TINTA
    pts = [(cx + s * math.cos(math.radians(90 + 120 * k)), cy - s * math.sin(math.radians(90 + 120 * k))) for k in range(3)]
    for k in range(3):
        A, B = pts[k], pts[(k + 1) % 3]
        M.arrow(c, lerp(A[0], B[0], 0.12), lerp(A[1], B[1], 0.12), lerp(A[0], B[0], 0.82), lerp(A[1], B[1], 0.82), cr, a, s * 0.1, s * 0.25, 1)
    centro(c, str(n), cx, cy + s * 0.3, s * 0.75, "g", cr, a)
    centro(c, CODIGOS[n], cx, cy + s * 1.0, s * 0.42, "g", cr, a)


def pneu(c, cx, cy, r, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#2B2D33", a))
    c.drawCircle(cx, cy, r * 0.5, M.paint("#9AA0A8", a))
    for k in range(16):
        ang = math.radians(k * 22.5)
        M.line(c, cx + r * 0.82 * math.cos(ang), cy + r * 0.82 * math.sin(ang), cx + r * 0.98 * math.cos(ang), cy + r * 0.98 * math.sin(ang), "#55585F", a, 6)


def borracha(c, t, t0, x0, y, s, vulc=0.0, a=1.0):
    """duas cadeias de poli-isopreno (com a dupla que sobra) e, com vulc, as pontes de enxofre"""
    for k, yy in enumerate((y, y + s * 2.2)):
        q = 1.0 if t0 is None else ease_out(prog(t, t0 + 0.3 * k, 0.8))
        if q > 0:
            cauda(c, x0, yy, n=12, L=s, dobra=False, a=a, p=q)
            for j in (2, 6, 10):
                xx = x0 - j * s * 0.87
                M.line(c, xx - s * 0.3, yy - 18, xx + s * 0.3, yy - 18, E.COR, a * q, 6)
    if vulc > 0:
        for j in (3, 8):
            xx = x0 - j * s * 0.87
            p = ease_out(min(1, vulc * 1.5))
            M.line(c, xx, y + 14, xx, y + 14 + (s * 2.2 - 28) * p, "#C9A400", a, 6)
            E.bola(c, xx, y + s * 1.1, 26 * ease_back(min(1, vulc)), "#F2C94C", a)
            centro(c, "S", xx, y + s * 1.1 + 14, 30, "g", TINTA, a * min(1, vulc))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        itens = ((380, "pão"), (800, "algodão"), (1220, "cabelo"), (1620, "pneu"))
        for k, (x, nome) in enumerate(itens):
            tk = a1 + 0.5 * k
            if nome == "pão":
                E.foco(c, t, tk, 0.4, lambda a, x=x: M.rrect(c, x - 130, 440, 260, 150, 70, "#C8873E", a, shadow=True))
            elif nome == "algodão":
                E.foco(c, t, tk, 0.4, lambda a, x=x: [E.bola(c, x + dx, 520 + dy, 60, "#FBFBFB", a) for dx, dy in ((-50, 10), (40, -20), (10, 30), (70, 30))])
            elif nome == "cabelo":
                def fios(a, x=x):
                    for j in range(6):
                        pth = skia.Path(); pth.moveTo(x - 80 + j * 30, 420)
                        pth.cubicTo(x - 120 + j * 30, 500, x - 40 + j * 30, 560, x - 80 + j * 30, 640)
                        c.drawPath(pth, M.paint("#5A3A22", a, stroke=7))
                E.foco(c, t, tk, 0.4, fios)
            else:
                E.foco(c, t, tk, 0.4, lambda a, x=x: pneu(c, x, 520, 120, a))
            E.foco(c, t, tk + 0.2, 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 720, 56, "g", TINTA, a))
        E.frase(c, t, b1, ps("todos são", "i", 76) + [("polímeros", "g", 72, COR)], W / 2, 220, "center", 0.12)
        E.frase(c, t, c1, ps("nenhum saiu de uma fábrica de plástico", "i", 62, TINTA2), W / 2, 880, "center", 0.1)
        E.foco(c, t, d1, 0.4, lambda a: E.pilula(c, "a natureza fabrica os dela", W / 2, 990, 52, "g", fundo=E.COR, a=a))
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("polímeros", "g", 66, COR), ("naturais", "i", 70)]),
                 (C["s02.c"], [("termoplástico", "g", 66), ("×", "g", 66, TINTA2), ("termofixo", "g", 66)]),
                 (C["s02.d"], [("qual", "i", 70), ("se", "i", 70), ("recicla", "g", 66, COR), ("derretendo", "i", 70)]),
                 (C["s02.e"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 420, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre das duas últimas aulas", "i", 70, TINTA2), XE, 200, passo=0.12)
    E.frase(c, t, C["s03.a"], [("adição:", "g", 80, COR)] + ps("a dupla abre, nada sai", "i", 70), XE, 400, passo=0.12)
    E.frase(c, t, C["s03.b"], [("condensação:", "g", 80, COR)] + ps("cada ligação solta água", "i", 70), XE, 580, passo=0.12)


# ---------------- naturais ----------------
def b_natural(c, t, C, b):
    if t < C["s06"]:
        E.frase(c, t, C["s04.a"], [("amido", "g", 80, COR)] + ps("pão, arroz, batata", "i", 60, TINTA2), XE, 220, passo=0.12)
        corrente(c, t, C["s04.b"], 1100, 210, 6, 125)
        E.foco(c, t, C["s04.b"] + 0.6, 0.4, lambda a: E.pilula(c, "glicose", 1650, 300, 44, "g", fundo=TINTA, a=a))
        E.frase(c, t, C["s04.c"], [("celulose", "g", 80, COR)] + ps("algodão, papel, madeira", "i", 60, TINTA2), XE, 480, passo=0.12)
        pts = corrente(c, t, C["s04.d"], 1100, 470, 6, 125)
        if t >= C["s04.d"] + 0.8:
            for i, P in enumerate(pts):
                if i % 2:
                    E.foco(c, t, C["s04.d"] + 0.8, 0.3, lambda a, P=P: c.drawCircle(P[0], P[1], 54, M.paint(E.COR, a, stroke=5)))
        E.foco(c, t, C["s04.d"] + 0.9, 0.4, lambda a: E.pilula(c, "ligada de outro jeito", 1650, 560, 42, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s04.e"], 0.4, lambda a: (E.escreve(c, "amido: o corpo digere", XE, 720, 56, "g", TINTA, a)))
        x_em(c, t, C["s04.e"] + 0.2, XE + 640, 700, 32, True)
        E.foco(c, t, C["s04.e"] + 0.8, 0.4, lambda a: E.escreve(c, "celulose: não digere", XE, 820, 56, "g", TINTA, a))
        x_em(c, t, C["s04.e"] + 1.0, XE + 640, 800, 32, False)
        E.foco(c, t, C["s05.a"], 0.4, lambda a: E.pilula(c, "cada glicose solta uma água", 1300, 760, 46, "g", fundo=TINTA2, a=a))
        E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "condensação", 1300, 870, 56, "g", fundo=E.COR, a=a))
        return
    if t < C["s07"]:
        E.frase(c, t, C["s06.a"], [("proteína", "g", 90, COR)] + ps("cabelo, carne", "i", 64, TINTA2), XE, 240, passo=0.12)
        corrente(c, t, C["s06.b"], 400, 520, 8, 160, "aminoacido", onda=t * 0.6)
        E.foco(c, t, C["s06.b"] + 0.8, 0.4, lambda a: E.pilula(c, "aminoácido: grupo ácido + grupo amina", W / 2, 680, 46, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s06.c"], 0.4, lambda a: Q.formula(c, "–CO–NH–", W / 2, 820, 80, COR, a, "center"))
        E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "poliamida natural", W / 2, 950, 56, "g", fundo=E.COR, a=a))
        return
    E.frase(c, t, C["s07.a"], [("borracha", "g", 90, COR)] + ps("do látex da seringueira", "i", 62, TINTA2), XE, 200, passo=0.12)
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "adição do isopreno: sobra uma dupla", 1300, 320, 44, "g", fundo=TINTA, a=a))
    borracha(c, t, C["s07.b"] + 0.3, 1500, 500, 80, ease_io(prog(t, C["s07.d"], 1.2)))
    calor(c, t, C["s07.c"], t1=C["s07.d"])
    E.foco(c, t, C["s07.c"], 0.4, lambda a: E.pilula(c, "crua: mole no calor", 560, 880, 48, "g", fundo=AMBAR, a=a))
    E.foco(c, t, C["s07.d"] + 1.0, 0.4, lambda a: E.pilula(c, "pontes de enxofre", 1100, 880, 48, "g", fundo="#C9A400", a=a))
    E.foco(c, t, C["s07.e"], 0.4, lambda a: E.pilula(c, "vulcanização: o pneu", 1600, 880, 48, "g", fundo=E.COR, a=a))


# ---------------- termoplástico e termofixo ----------------
def b_termo(c, t, C, b):
    calor(c, t, C["s08.b"], t1=C["s09"])
    calor(c, t, C["s09.c"])
    E.foco(c, t, C["s08.a"], 0.4, lambda a: centro(c, "termoplástico", 520, 240, 76, "g", COR, a))
    mexe = ep(t, C["s08.b"], 0.6)
    E.foco(c, t, C["s08.a"] + 0.3, 0.5, lambda a: espaguete(c, t, 520, 520, 600, 300, mexe, a))
    E.foco(c, t, C["s08.a"] + 0.6, 0.4, lambda a: centro(c, "fios soltos, como espaguete", 520, 740, 46, "i", TINTA2, a))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "no calor, amolece", 520, 830, 48, "g", fundo=AMBAR, a=a))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "e ganha outra forma", 520, 920, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s08.e"], 0.4, lambda a: E.escreve(c, "PE, PP, PVC, PET, PS", 300, 1020, 50, "g", TINTA, a))
    E.foco(c, t, C["s09.a"], 0.4, lambda a: centro(c, "termofixo", 1400, 240, 76, "g", COR, a))
    E.foco(c, t, C["s09.a"] + 0.3, 0.5, lambda a: rede(c, 1400, 520, 560, 300, a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: centro(c, "amarrada, como rede de pesca", 1400, 740, 46, "i", TINTA2, a))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "não amolece; se esquentar demais, queima", 1400, 830, 42, "g", fundo=ERRADO, a=a))
    E.foco(c, t, C["s09.e"], 0.4, lambda a: E.escreve(c, "baquelite: cabo de panela, tomada", 1130, 1020, 46, "g", TINTA, a))


# ---------------- reciclagem ----------------
def b_recicla(c, t, C, b):
    E.frase(c, t, C["s10"], [("reciclagem", "g", 80, COR)] + ps("por fusão", "i", 76), XE, 200, passo=0.12)
    E.foco(c, t, C["s10.a"], 0.4, lambda a: E.pilula(c, "termoplástico: derrete e molda de novo", 640, 340, 46, "g", fundo=E.COR, a=a))
    x_em(c, t, C["s10.a"] + 0.3, 1140, 340, 34, True)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "termofixo: não", 1400, 340, 46, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s10.c"], ps("nas embalagens: o", "i", 62, TINTA2) + [("triângulo com número", "g", 58)], XE, 500, passo=0.1)
    for k, (n, tk) in enumerate(((1, "s10.d"), (3, "s10.e"), (6, "s10.f"))):
        E.foco(c, t, C[tk], 0.4, lambda a, n=n, k=k: tri_recicla(c, 520 + k * 440, 740, 110, n, a, E.COR))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("todo plástico recicla derretendo?", "i", 70), XE + 450, 190, passo=0.1)
    calor(c, t, C["s11.b"])
    E.foco(c, t, C["s11.b"], 0.5, lambda a: rede(c, 640, 560, 560, 300, a))
    E.foco(c, t, C["s11.b"] + 0.4, 0.4, lambda a: E.pilula(c, "termofixo não derrete", 640, 800, 52, "g", fundo=ERRADO, a=a))
    E.frase(c, t, C["s11.c"], ps("só pode ser", "i", 62), 1100, 460, passo=0.1)
    E.foco(c, t, C["s11.c"] + 0.6, 0.4, lambda a: E.pilula(c, "moído, como enchimento", 1400, 580, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s11.c"] + 1.4, 0.4, lambda a: E.pilula(c, "queimado para gerar energia", 1400, 690, 48, "g", fundo=TINTA, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12.a"], ps("as cadeias estão", "i", 70, CLARO) + [("soltas", "g", 66, BR)] + ps("ou", "i", 70, CLARO) + [("amarradas?", "g", 66, BR)], W / 2, 170, "center", 0.12)
    E.foco(c, t, C["s12.b"], 0.5, lambda a: espaguete(c, t, 520, 450, 520, 240, 0.6, a))
    E.foco(c, t, C["s12.b"] + 0.4, 0.4, lambda a: (centro(c, "soltas: termoplástico", 520, 660, 52, "g", BR, a), centro(c, "amolece, recicla por fusão", 520, 730, 44, "i", CLARO, a)))
    E.foco(c, t, C["s12.c"], 0.5, lambda a: rede(c, 1400, 450, 480, 240, a, "#D8DCE0"))
    E.foco(c, t, C["s12.c"] + 0.4, 0.4, lambda a: (centro(c, "amarradas: termofixo", 1400, 660, 52, "g", BR, a), centro(c, "não amolece, não recicla por fusão", 1400, 730, 44, "i", CLARO, a)))
    E.foco(c, t, C["s12.d"], 0.4, lambda a: pneu(c, 300, 930, 90, a))
    E.frase(c, t, C["s12.d"] + 0.3, ps("borracha vulcanizada: amarrada pelo enxofre,", "i", 54, CLARO) + [("não derrete", "g", 50, BR)], 440, 945, "left", 0.08)


# ---------------- questão e resposta ----------------
def cabo(c, cx, cy, a=1.0):
    if a <= 0:
        return
    c.drawCircle(cx - 180, cy, 110, M.paint("#9AA0A8", a))
    c.drawCircle(cx - 180, cy, 85, M.paint("#C9CED3", a))
    M.rrect(c, cx - 80, cy - 26, 300, 52, 26, "#2B2D33", a, shadow=True)


# (peças copiadas de QUI-ORG-026)
def garrafa_pet(c, cx, yb, h, a=1.0):
    if a <= 0:
        return
    w = h * 0.36
    M.rrect(c, cx - w / 2, yb - h * 0.8, w, h * 0.8, w * 0.3, "#CFEDEA", a * 0.9, shadow=True)
    M.rrect(c, cx - w * 0.2, yb - h, w * 0.4, h * 0.25, 10, "#CFEDEA", a * 0.9)
    M.rrect(c, cx - w * 0.24, yb - h * 1.04, w * 0.48, h * 0.08, 8, E.COR, a)



def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.foco(c, t, C["s13.a"], 0.5, lambda a: garrafa_pet(c, 520, 720, 420, a))
    E.foco(c, t, C["s13.a"] + 0.3, 0.4, lambda a: centro(c, "garrafa PET", 520, 800, 54, "g", TINTA, a))
    E.saida(c, t, C["s14"], lambda: (E.foco(c, t, C["s13.b"], 0.5, lambda a: cabo(c, 1380, 560, a)),
                                     E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: centro(c, "cabo de baquelite", 1380, 800, 54, "g", TINTA, a))))
    E.frase(c, t, C["s13.c"], [("1", "g", 58, COR)] + ps("qual pode ser derretido e virar outro objeto?", "i", 60), XE, 920, passo=0.08)
    E.frase(c, t, C["s13.d"], [("2", "g", 58, COR)] + ps("por quê?", "i", 60), XE, 1010, passo=0.08)
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1380, cy=560, r=150)


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s15"], ps("resolvendo", "i", 72, COR), XE, 170)
    E.foco(c, t, C["s15"], 0.4, lambda a: garrafa_pet(c, 360, 640, 340, a))
    E.foco(c, t, C["s15.a"], 0.5, lambda a: espaguete(c, t, 760, 460, 360, 200, 0.5 * ep(t, C["s15.b"], 0.5), a))
    E.foco(c, t, C["s15.a"] + 0.3, 0.4, lambda a: E.pilula(c, "termoplástico", 640, 640, 50, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s15.b"], 0.4, lambda a: E.pilula(c, "vira fibra, tecido, outra garrafa", 640, 750, 44, "g", fundo=TINTA, a=a))
    x_em(c, t, C["s15.b"] + 0.4, 640, 860, 40, True)
    E.foco(c, t, C["s15.c"], 0.4, lambda a: cabo(c, 1500, 380, a))
    E.foco(c, t, C["s15.c"] + 0.3, 0.5, lambda a: rede(c, 1450, 560, 360, 160, a))
    E.foco(c, t, C["s15.c"] + 0.5, 0.4, lambda a: E.pilula(c, "termofixo", 1450, 700, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s15.d"], 0.4, lambda a: E.pilula(c, "não se recicla por fusão", 1450, 810, 44, "g", fundo=ERRADO, a=a))
    x_em(c, t, C["s15.d"] + 0.4, 1450, 910, 40, False)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s16"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s16.a", [("naturais:", "g", 62, COR)] + ps("amido, celulose, proteína, borracha", "i", 66)),
                 ("s16.b", [("termoplástico:", "g", 62, COR)] + ps("solto, recicla por fusão", "i", 66)),
                 ("s16.c", [("termofixo:", "g", 62, COR)] + ps("amarrado, não recicla por fusão", "i", 66)))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
    E.saida(c, t, C["s17"] - 0.1, resumo)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s17"] + 0.6, [("praticando", "g", 110, COR)], XE, 370)
    E.frase(c, t, C["s17.a"], ps("monômeros, tipos e destino dos plásticos", "i", 60, TINTA2), XE, 480, passo=0.1)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.pilula(c, "questões de prova", XE + 220, 600, 52, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s17.c"] + 0.2, 0.4))
    E.frase(c, t, C["s17.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, natural=b_natural, termo=b_termo, recicla=b_recicla, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
