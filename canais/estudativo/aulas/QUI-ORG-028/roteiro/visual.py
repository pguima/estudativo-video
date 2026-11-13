"""Visual — Estudativo · QUI-ORG-028: praticando polímeros (prática, quatro situações). Última aula da trilha.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001) e a LINGUAGEM DOS POLÍMEROS de QUI-ORG-025. Prática no modelo
de QUI-ORG-017; as peças vêm das aulas do módulo (unidade e formula_n de QUI-ORG-025, peças de condensação de QUI-ORG-026,
rede, espaguete, triângulo de reciclagem e cadeia de glicose de QUI-ORG-027), copiadas abaixo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-028_praticando_polimeros.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "atalho", "questao3", "questao4", "fim"))

assert Q.contar("CH2CHCl") == Q.contar("C2H3Cl")  # monômero do PVC = a unidade (adição)
assert Q.lados("C8H6O4 + C6H8N2 -> C14H10N2O2 + 2 H2O")[0] == Q.lados("C8H6O4 + C6H8N2 -> C14H10N2O2 + 2 H2O")[1]  # kevlar
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


# (peças copiadas de QUI-ORG-025)
def formula_n(c, t, t0, s, x, y, size, align="left", cores=None, escuro=False, cor=None):
    """fórmula da unidade com colchetes e o n pequeno embaixo, à direita"""
    w = Q.formula(None, s, 0, 0, size)
    x0 = x - w / 2 if align == "center" else x
    E.foco(c, t, t0, 0.5, lambda a: (Q.formula(c, s, x0, y, size, cor, a, cores=cores, escuro=escuro),
                                     E.escreve(c, "n", x0 + w + 6, y + size * 0.3, size * 0.6, "g", cor or Q._tinta(escuro), a)))
    return w


def unidade(c, t, t0, cx, cy, subs, esc=110, size=64, cores=None, escuro=False, a=1.0, simples=True):
    """a unidade que se repete, em estrutura plana, com traços abertos e colchetes"""
    at = [("C", -0.5, 0), ("C", 0.5, 0), (subs[0], -0.5, -1.05), (subs[1], -0.5, 1.05), (subs[2], 0.5, -1.05), (subs[3], 0.5, 1.05), ("", -1.35, 0), ("", 1.35, 0)]
    ligs = [(0, 1, 1 if simples else 2, None if simples else ERRADO), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1), (0, 6, 1), (1, 7, 1)]
    P = estr(c, t, t0, at, ligs, cx, cy, esc, size, cores=cores, escuro=escuro, a=a)
    q = 1.0 if t0 is None else ep(t, t0 + 0.5, 0.4)
    colchetes(c, cx - 1.25 * esc, cx + 1.25 * esc, cy, 2.6 * esc, q * a, n="n", size=size * 0.8, escuro=escuro)
    return P

# (peças copiadas de QUI-ORG-026)
def peca(c, cx, cy, w, meio, esq, dir_, cor_e=None, cor_d=None, a=1.0, h=110, size=46):
    """um monômero como peça de montar: o miolo e um grupo reativo em cada ponta (None = ponta sem grupo)"""
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#FFFFFF", a, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 22, 22), M.paint(FIO, a, stroke=3))
    Q.formula(c, meio, cx, cy + size * 0.36, size, TINTA, a, "center")
    for s, g, cr in ((-1, esq, cor_e), (1, dir_, cor_d)):
        if g:
            gw = Q.formula(None, g, 0, 0, size) + 30
            x = cx + s * (w / 2 + gw / 2 - 4)
            M.rrect(c, x - gw / 2, cy - h * 0.32, gw, h * 0.64, 14, cr or E.COR, a)
            Q.formula(c, g, x, cy + size * 0.36, size, BR, a, "center")


def fila_cond(c, t, t0, tu, pecas, cx, cy, gap0=420, gap1=330, w=220, d=1.6, rotulo="éster"):
    """fila de peças que se encaixam a partir de tu; cada encaixe solta uma bolha H₂O e ganha a caixa do grupo novo"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    gap1 = w + 190  # as pontas se encostam
    gap0 = gap1 + 110
    gap = lerp(gap0, gap1, u)
    k = len(pecas)
    xs = [cx + (i - (k - 1) / 2) * gap for i in range(k)]
    for i, (x, p) in enumerate(zip(xs, pecas)):
        q = 1.0 if t0 is None else ep(t, t0 + 0.25 * i, 0.4)
        peca(c, x, cy, w, *p, a=q)
    if u > 0.6:
        for i in range(k - 1):
            xm = (xs[i] + xs[i + 1]) / 2
            b = ep(t, tu + d * 0.6 + 0.1 * i, 0.9) if tu is not None else 1
            if b < 1:
                E.pilula(c, "H₂O", xm, cy - 90 - 120 * b, 40, "g", fundo=TINTA2, a=1 - b)
            qq = ep(t, tu + d * 0.8, 0.4) if tu is not None else 1
            jun = "CO–O" if rotulo == "éster" else "CO–NH"
            jw = Q.formula(None, jun, 0, 0, 46) + 40
            M.rrect(c, xm - jw / 2, cy - 40, jw, 80, 16, "#FFFFFF", qq)
            Q.formula(c, jun, xm, cy + 16, 46, COR, qq, "center")
            E.caixa_pontilhada(c, xm - jw / 2 - 14, cy - 60, jw + 28, 120, qq, E.COR, prog_=qq)
            E.foco(c, t, (tu or -9) + d * 0.9, 0.3, lambda a, xm=xm: centro(c, rotulo, xm, cy + 120, 40, "g", COR, a))
    return xs


def garrafa_pet(c, cx, yb, h, a=1.0):
    if a <= 0:
        return
    w = h * 0.36
    M.rrect(c, cx - w / 2, yb - h * 0.8, w, h * 0.8, w * 0.3, "#CFEDEA", a * 0.9, shadow=True)
    M.rrect(c, cx - w * 0.2, yb - h, w * 0.4, h * 0.25, 10, "#CFEDEA", a * 0.9)
    M.rrect(c, cx - w * 0.24, yb - h * 1.04, w * 0.48, h * 0.08, 8, E.COR, a)

# (peças copiadas de QUI-ORG-027)
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


# ---------------- peças desta aula ----------------
PVC = ("H", "H", "H", "Cl")
KEVLAR = "[–CO–C6H4–CO–NH–C6H4–NH–]"


def situacao(c, t, t0, n):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"situação {n}", XE + 150, 150, 50, "g", fundo=E.COR, a=a))


def pausa(c, t, C, k, cx=1480, cy=600, r=170):
    if t >= C[k]:
        E.relogio(c, t, C[k + ".a"], cx=cx, cy=cy, r=r)


def tomada(c, cx, cy, s, a=1.0):
    if a <= 0:
        return
    M.rrect(c, cx - s, cy - s, 2 * s, 2 * s, s * 0.3, "#3A3B42", a, shadow=True)
    for dx in (-0.35, 0.35):
        c.drawCircle(cx + dx * s, cy, s * 0.14, M.paint("#111111", a))


def copo(c, cx, yb, h, a=1.0):
    if a <= 0:
        return
    pth = skia.Path(); pth.moveTo(cx - h * 0.4, yb - h); pth.lineTo(cx + h * 0.4, yb - h); pth.lineTo(cx + h * 0.28, yb); pth.lineTo(cx - h * 0.28, yb); pth.close()
    c.drawPath(pth, M.paint("#F7F7F2", a)); c.drawPath(pth, M.paint(FIO, a, stroke=4))


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("4", "g", 200, COR)], XE, 380)
    E.frase(c, t, C["s01.a"] + 0.4, ps("situações", "i", 110), XE + 170, 380)
    E.frase(c, t, C["s01.b"], ps("plásticos, fibras e comida", "i", 66, TINTA2), XE, 500, passo=0.1)
    pilula_em(c, t, C["s01.c"], "pause e resolva", XE + 260, 700, 60, E.COR)
    E.foco(c, t, C["s01.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1600, 420, 220 * a, giro=8 * math.sin(t * 0.4)), blur=0)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 76, TINTA2), XE, 200, passo=0.12)
    for i, (k, s) in enumerate((("s02.a", "polímero de adição"), ("s02.b", "polímero de condensação"), ("s02.c", "termoplástico e termofixo"))):
        y = 360 + i * 140
        E.foco(c, t, C[k], 0.4, lambda a, i=i, y=y: (E.bola(c, XE + 36, y - 22, 38, a=a), centro(c, str(i + 1), XE + 36, y - 3, 46, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 64)], XE + 100, y)
    E.foco(c, t, C["s02.c"] + 1.0, 0.4, lambda a: E.pilula(c, "travou? procure a aula no canal", 1450, 960, 44, "b", fundo=TINTA2, a=a))


# ---------------- 1: PVC ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1)
    E.foco(c, t, C["s03.a"] + 0.3, 0.4, lambda a: E.escreve(c, "o cano de PVC", XE + 360, 168, 54, "g", TINTA, a))
    formula_n(c, t, C["s03.b"], "[–CH2–CHCl–]", XE, 400, 100, cores={"Cl": COR})
    if t < C["s04"]:
        unidade(c, t, C["s03.b"] + 0.4, 1450, 560, PVC, 120, 66, cores={5: COR})
    E.frase(c, t, C["s03.c"], [("1", "g", 58, COR)] + ps("qual é o monômero?", "i", 62), XE, 640, passo=0.1)
    E.frase(c, t, C["s03.d"], [("2", "g", 58, COR)] + ps("que tipo de polímero?", "i", 62), XE, 750, passo=0.1)
    pausa(c, t, C, "s04")


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05"], ps("resolvendo", "i", 64, COR), XE, 165)
    if t < C["s05.c"]:
        unidade(c, t, None, 560, 560, PVC, 130, 70, cores={5: COR})
    else:
        alceno(c, t, C["s05.c"], 560, 560, PVC, 130, 70, cores={5: COR}, cor_dupla=E.COR)
    E.foco(c, t, C["s05.a"], 0.4, lambda a: E.pilula(c, "sem éster nem amida", 1300, 400, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "adição", 1300, 500, 60, "g", fundo=E.COR, a=a))
    Q.formula_em(c, t, C["s05.d"], "CH2=CHCl", 1100, 720, 96, cores={"Cl": COR})
    E.foco(c, t, C["s05.e"], 0.4, lambda a: E.pilula(c, "cloreto de vinila", 1300, 830, 52, "g", fundo=CERTO, a=a))


# ---------------- 2: kevlar ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.b"], [("kevlar", "g", 66)] + ps("a fibra do colete à prova de bala", "i", 60, TINTA2), XE, 300, passo=0.1)
    formula_n(c, t, C["s06.b"] + 0.6, KEVLAR, XE, 440, 76)
    E.frase(c, t, C["s06.c"], [("1", "g", 56, COR)] + ps("que tipo de polímero?", "i", 60), XE, 600, passo=0.1)
    E.frase(c, t, C["s06.d"], [("2", "g", 56, COR)] + ps("que grupo é esse?", "i", 60), XE, 690, passo=0.1)
    E.frase(c, t, C["s06.e"], [("3", "g", 56, COR)] + ps("o que sai? de que monômeros vem?", "i", 60), XE, 780, passo=0.1)
    pausa(c, t, C, "s07", 1480, 760, 160)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s08"], ps("resolvendo", "i", 64, COR), XE, 165)
    formula_n(c, t, -9, KEVLAR, W / 2, 330, 76, "center", cores={k: COR for k in (4, 5, 6, 7)} if t >= C["s08.a"] else None)
    E.foco(c, t, C["s08.a"], 0.4, lambda a: E.pilula(c, "CO–NH: amida", W / 2 - 320, 440, 48, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s08.b"], 0.4, lambda a: E.pilula(c, "poliamida, como o náilon", W / 2 + 280, 440, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "condensação: sai água", W / 2, 560, 54, "g", fundo=E.COR, a=a))
    if t >= C["s08.e"]:
        fila_cond(c, t, C["s08.e"], C["s08.e"] + 2.0, [("C6H4", "HOOC", "COOH", E.COR, E.COR), ("C6H4", "H2N", "NH2", TINTA, TINTA)], W / 2, 800, w=200, rotulo="amida")
        E.foco(c, t, C["s08.e"] + 0.4, 0.4, lambda a: centro(c, "ácido tereftálico + diamina com anel", W / 2, 990, 46, "i", TINTA2, a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s09.a"], ps("olhe a", "i", 70, CLARO) + [("unidade que se repete", "g", 66, BR)], W / 2, 160, "center", 0.12)
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.escreve(c, "cadeia principal só de carbonos?", XE, 320, 56, "g", BR, a))
    E.foco(c, t, C["s09.b"] + 0.5, 0.4, lambda a: E.pilula(c, "adição: devolva a dupla", 1500, 300, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.c"], 0.4, lambda a: E.escreve(c, "O ou N ligando as unidades?", XE, 460, 56, "g", BR, a))
    E.foco(c, t, C["s09.c"] + 0.5, 0.4, lambda a: E.escreve(c, "éster, amida, entre as glicoses", XE, 530, 44, "i", CLARO, a))
    E.foco(c, t, C["s09.c"] + 0.8, 0.4, lambda a: E.pilula(c, "condensação: corte e devolva a água", 1420, 445, 40, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s10.a"], 0.4, lambda a: E.escreve(c, "destino do plástico:", XE, 720, 56, "g", BR, a))
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.escreve(c, "amolece no calor?", XE + 600, 720, 56, "g", E.CLARO, a))
    E.foco(c, t, C["s10.c"], 0.4, lambda a: E.pilula(c, "termoplástico: recicla por fusão", W / 2, 880, 54, "g", fundo=E.COR, a=a))


# ---------------- 3: esteira ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C["s11.a"], 3)
    xs = (420, 960, 1500)
    E.foco(c, t, C["s11.b"], 0.5, lambda a: copo(c, xs[0], 640, 300, a))
    E.foco(c, t, C["s11.b"] + 0.3, 0.4, lambda a: centro(c, "copo de isopor", xs[0], 720, 50, "g", TINTA, a))
    E.foco(c, t, C["s11.c"], 0.5, lambda a: garrafa_pet(c, xs[1], 640, 380, a))
    E.foco(c, t, C["s11.c"] + 0.3, 0.4, lambda a: centro(c, "garrafa PET", xs[1], 720, 50, "g", TINTA, a))
    E.foco(c, t, C["s11.d"], 0.5, lambda a: tomada(c, xs[2], 500, 120, a))
    E.foco(c, t, C["s11.d"] + 0.3, 0.4, lambda a: centro(c, "tomada de baquelite", xs[2], 720, 50, "g", TINTA, a))
    M.line(c, 150, 660, 1770, 660, TINTA2, ep(t, C["s11.a"], 0.5), 10)
    E.saida(c, t, C["s12"], lambda: E.frase(c, t, C["s11.e"], ps("quais podem ser derretidos e moldados de novo?", "i", 62, COR), W / 2, 900, "center", 0.08))
    if t >= C["s12"]:
        E.relogio(c, t, C["s12.a"], cx=W / 2, cy=830, r=65)


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s13"], ps("resolvendo", "i", 64, COR), XE, 165)
    xs = (420, 960, 1500)
    copo(c, xs[0], 640, 300); garrafa_pet(c, xs[1], 640, 380); tomada(c, xs[2], 500, 120)
    E.foco(c, t, C["s13.a"], 0.4, lambda a: tri_recicla(c, xs[0], 850, 70, 6, a, E.COR))
    E.foco(c, t, C["s13.b"], 0.4, lambda a: tri_recicla(c, xs[1], 850, 70, 1, a, E.COR))
    for k, x in enumerate(xs[:2]):
        x_em(c, t, C["s13.c"] + 0.2 * k, x + 150, 760, 40, True)
    E.foco(c, t, C["s13.c"], 0.4, lambda a: E.pilula(c, "termoplásticos: reciclam por fusão", 690, 1010, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s13.d"], 0.4, lambda a: E.pilula(c, "termofixo", xs[2], 820, 52, "g", fundo=TINTA, a=a))
    x_em(c, t, C["s13.e"], xs[2], 930, 44, False)


# ---------------- 4: amido e celulose ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C["s14.a"], 4)
    E.frase(c, t, C["s14.b"], [("arroz:", "g", 64), ("amido", "g", 64, COR)], XE, 330, passo=0.12)
    E.frase(c, t, C["s14.c"], [("alface:", "g", 64), ("celulose", "g", 64, COR)], XE, 450, passo=0.12)
    E.frase(c, t, C["s14.d"], ps("o mesmo monômero", "i", 62, TINTA2), XE, 570, passo=0.1)
    E.frase(c, t, C["s14.e"], [("1", "g", 56, COR)] + ps("qual é o monômero?", "i", 60), XE, 720, passo=0.1)
    E.frase(c, t, C["s14.f"], [("2", "g", 56, COR)] + ps("qual o corpo digere?", "i", 60), XE, 830, passo=0.1)
    if t < C["s15"]:
        corrente(c, t, C["s14.b"], 1080, 330, 6, 130)
        corrente(c, t, C["s14.c"], 1080, 450, 6, 130)
    pausa(c, t, C, "s15", 1480, 700, 160)


def b_resposta4(c, t, C, b):
    E.frase(c, t, C["s16"], ps("resolvendo", "i", 64, COR), XE, 165)
    corrente(c, t, None, 560, 380, 6, 110)
    corrente(c, t, None, 560, 640, 6, 110)
    E.foco(c, t, C["s16.a"], 0.4, lambda a: E.pilula(c, "glicose", 300, 510, 56, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s16.b"], 0.4, lambda a: E.escreve(c, "amido: digerido, vira energia", 1220, 395, 48, "g", TINTA, a))
    x_em(c, t, C["s16.b"] + 0.3, 1180, 380, 28, True)
    E.foco(c, t, C["s16.c"], 0.4, lambda a: E.escreve(c, "celulose: passa sem digerir", 1220, 655, 48, "g", TINTA, a))
    E.foco(c, t, C["s16.d"], 0.4, lambda a: E.pilula(c, "é a fibra da alimentação", 1480, 780, 48, "g", fundo=TINTA, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.frase(c, t, C["s17.a"], [("3", "g", 110, COR)] + ps("ou mais? módulo firme", "i", 76), XE, 270, passo=0.12)
    E.frase(c, t, C["s17.a"] + 1.6, ps("travou? reveja a aula da questão", "i", 60, TINTA2), XE, 380, passo=0.1)
    E.frase(c, t, C["s17.b"], ps("você fechou a trilha de", "i", 72) + [("Química Orgânica", "g", 68, COR)], XE, 560, passo=0.12)
    E.foco(c, t, C["s17.c"], 0.5, lambda a: E.pilula(c, "das fórmulas do carbono aos plásticos", XE + 470, 680, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s17.b"] + 0.5, 0.8, lambda a: E.simbolo(c, 1600, 880, 150 * a, giro=8 * math.sin(t * 0.4)), blur=0)
    E.foco(c, t, C["s17.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 300, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s17.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(600, 325, p), ep(t, C["s17.d"] + 0.2, 0.4))
    E.frase(c, t, C["s17.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], XE, 900)


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, atalho=b_atalho, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4,
              resposta4=b_resposta4, fim=b_fim)
