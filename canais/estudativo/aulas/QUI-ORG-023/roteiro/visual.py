"""Visual — Estudativo · QUI-ORG-023: saponificação e biodiesel.

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001), o complemento da Orgânica de QUI-ORG-015 e a linguagem das
reações de QUI-ORG-018. TRIGLICERÍDEO em esquema (trigli): o glicerol é uma barra vertical à direita, com três linhas; em
cada linha, a cadeia do ácido graxo em bastão (zigue-zague) termina no grupo do éster, CO–O, encostado no glicerol. Óleo =
cadeia com dobra e dupla na cor da matéria; gordura = cadeia reta. Na reação, as três cadeias saem juntas para a esquerda
com a cabeça nova (COO⁻ Na⁺ = sabão; COO–CH3 = biodiesel) e o glicerol fica com três OH.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-023_saponificacao_e_biodiesel.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("trigli", "sabao", "biodiesel", "atalho", "questao", "fim"))

# tristearina (gordura) com NaOH e com metanol: a conta 1 : 3 : 3 : 1 fecha
for eq in ("C57H110O6 + 3 NaOH -> 3 C18H35O2Na + C3H8O3", "C57H110O6 + 3 CH4O -> 3 C19H38O2 + C3H8O3",
           "C57H110O6 + 3 C2H6O -> 3 C20H40O2 + C3H8O3", "C57H110O6 + 3 KOH -> 3 C18H35O2K + C3H8O3"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq
assert Q.contar("CH2(OH)CH(OH)CH2(OH)") == Q.contar("C3H8O3")  # glicerol


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


# ---------------- peças desta aula ----------------
OLEO = "#F2C94C"


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


def trigli(c, t, t0, x, y, u=0.0, modo="ester", dobras=(True, False, True), a=1.0, dy=170, size=56, escuro=False):
    """triglicerídeo com o glicerol em x (barra) e três cadeias à esquerda. u = 0..1 separa (modo "sabao" ou "biodiesel")"""
    q = 1.0 if t0 is None else ep(t, t0, 0.5)
    if q <= 0:
        return
    tinta = Q._tinta(escuro)
    M.rrect(c, x - 60, y - dy - 70, 120, 2 * dy + 140, 30, "#D8EFEA" if not escuro else "#1E3B37", q * a)
    centro(c, "glicerol", x, y + dy + 130, 44, "i", TINTA2 if not escuro else CLARO, q * a)
    for i in range(3):
        yy = y + (i - 1) * dy
        pi = 1.0 if t0 is None else ease_out(prog(t, t0 + 0.3 + 0.2 * i, 0.8))
        if u < 0.5:
            hx = x - 70
            w = Q.formula(None, "CO–O", 0, 0, size)
            Q.formula(c, "CO–O", hx, yy + size * 0.36, size, tinta, q * a * (1 - 2 * u), "right", cores={1: E.COR})
            cauda(c, hx - w - 6, yy, dobra=dobras[i], a=q * a * (1 - 2 * u), p=pi, escuro=escuro)
        else:
            k = (u - 0.5) * 2
            sh = 280 * k
            cab = {"sabao": "COO^- Na^+", "sabaoK": "COO^- K^+", "biodiesel": "COO–CH3", "bioetanol": "COO–C2H5"}.get(modo, "COOH")
            hx = x - 170 - sh
            w = Q.formula(None, cab, 0, 0, size)
            Q.formula(c, cab, hx, yy + size * 0.36, size, tinta, q * a * k, "right", cores={k_: (CLARO if escuro else COR) for k_ in range(2, 8)})
            cauda(c, hx - w - 6, yy, dobra=dobras[i], a=q * a * max(0.3, k), escuro=escuro)
            Q.formula(c, "HO", x - 70, yy + size * 0.36, size, CLARO if escuro else COR, q * a * k, "right")


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        Q.bequer(c, t, a1 - 0.3, W / 2, 700, 320, 340, 0.7, OLEO, graduacao=False)
        E.foco(c, t, a1, 0.4, lambda a: centro(c, "óleo", W / 2, 790, 60, "g", TINTA, a))
        E.foco(c, t, a1 + 0.4, 0.5, lambda a: (M.rrect(c, 260, 520, 300, 190, 26, "#F6F1E7", a, shadow=True), centro(c, "sabão", 410, 635, 60, "g", TINTA, a)))
        seta_em(c, t, a1 + 0.4, 790, 600, 640, 90, cor=TINTA2)
        E.foco(c, t, b1, 0.5, lambda a: (M.rrect(c, 1360, 460, 260, 300, 30, "#E9C24A", a, shadow=True), centro(c, "biodiesel", 1490, 640, 50, "g", TINTA, a)))
        seta_em(c, t, b1, 1130, 1330, 640, 90, cor=TINTA2)
        E.frase(c, t, c1, ps("mesmo óleo, dois produtos", "i", 76), W / 2, 220, "center", 0.12)
        E.frase(c, t, d1, ps("só muda o que", "i", 70) + [("entra", "g", 66, COR)], W / 2, 960, "center", 0.12)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1600, 560, 260 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 260, passo=0.14)
    lista(c, t, [(C["s02.b"], [("óleo", "g", 66, COR), ("×", "g", 66, TINTA2), ("gordura", "g", 66, COR)]),
                 (C["s02.c"], [("como", "i", 70), ("vira", "i", 70), ("sabão", "g", 66)]),
                 (C["s02.d"], [("o", "i", 70), ("biodiesel", "g", 66)]),
                 (C["s02.e"], [("atalho", "g", 66, COR), ("de", "i", 70), ("prova", "i", 70)])], XE, 420, 150)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre de duas aulas", "i", 70, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("hidrólise:", "g", 70, COR), ("éster", "g", 66), ("+", "g", 66, TINTA2), ("água", "g", 66), ("→", "g", 66, TINTA2), ("ácido", "g", 66), ("+", "g", 66, TINTA2), ("álcool", "g", 66)], XE, 340, passo=0.1)
    E.frase(c, t, C["s03.b"], [("sabão:", "g", 70, COR)] + ps("ponta que gosta de água", "i", 66), XE, 540, passo=0.1)
    E.frase(c, t, C["s03.c"], ps("e cauda que gosta de gordura", "i", 66), XE + 255, 640, passo=0.1)
    if t >= C["s03.b"]:
        E.foco(c, t, C["s03.b"] + 0.4, 0.5, lambda a: (cauda(c, 1450, 860, a=a), E.bola(c, 1490, 860, 40, E.COR, a)))
        E.foco(c, t, C["s03.b"] + 0.8, 0.4, lambda a: centro(c, "ponta", 1540, 950, 44, "i", COR, a))
        E.foco(c, t, C["s03.c"], 0.4, lambda a: centro(c, "cauda", 1200, 950, 44, "i", TINTA2, a))


# ---------------- óleo e gordura ----------------
def b_trigli(c, t, C, b):
    if t < C["s05"]:
        E.frase(c, t, C["s04.a"], ps("óleo e gordura: a mesma família", "i", 66, TINTA2), XE, 180, passo=0.1)
        trigli(c, t, C["s04.a"] + 0.3, 1300, 560)
        E.foco(c, t, C["s04.b"], 0.4, lambda a: E.pilula(c, "glicerol: 3 OH", 1300, 290, 46, "g", fundo=E.COR, a=a))
        E.foco(c, t, C["s04.c"], 0.4, lambda a: E.pilula(c, "ácido graxo", 560, 290, 46, "g", fundo=TINTA, a=a))
        E.foco(c, t, C["s04.c"] + 0.6, 0.4, lambda a: E.pilula(c, "ligação de éster", 1050, 900, 44, "g", fundo=E.COR, a=a))
        E.frase(c, t, C["s04.d"], [("3", "g", 66, COR)] + ps("ésteres:", "i", 70) + [("triglicerídeo", "g", 66, COR)], XE, 1010, passo=0.12)
        return
    E.frase(c, t, C["s05"], ps("a diferença está nas cadeias", "i", 66, TINTA2), XE, 180, passo=0.1)
    for k in range(3):
        E.foco(c, t, C["s05.a"] + 0.2 * k, 0.4, lambda a, k=k: cauda(c, 820, 420 + k * 120, n=9, dobra=True, a=a))
        E.foco(c, t, C["s05.c"] + 0.2 * k, 0.4, lambda a, k=k: cauda(c, 1700, 420 + k * 70, n=12, a=a))
    E.foco(c, t, C["s05.a"] + 0.4, 0.4, lambda a: centro(c, "óleo: mais duplas", 560, 800, 60, "g", COR, a))
    E.foco(c, t, C["s05.b"], 0.4, lambda a: E.pilula(c, "encaixam mal: líquido", 560, 900, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.c"] + 0.4, 0.4, lambda a: centro(c, "gordura: retas", 1380, 800, 60, "g", TINTA, a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "empilham bem: sólida", 1380, 900, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.b"] + 0.4, 0.4, lambda a: centro(c, "à temperatura ambiente", W / 2, 1010, 44, "i", TINTA2, a))


# ---------------- saponificação ----------------
def b_sabao(c, t, C, b):
    E.frase(c, t, C["s06"], [("saponificação", "g", 80, COR)], XE, 170)
    tl = [C["s06.a"], C["s06.a"] + 0.2, C["s06.a"] + 0.4, C["s07.c"], C["s07.d"], C["s07.e"] - 0.2, C["s07.e"]]
    Q.equacao(c, t, C["s06.a"], "triglicerídeo + 3 NaOH -> 3 sabão + glicerol", W / 2, 300, 60, tl=tl, cores={})
    u = ease_io(prog(t, C["s06.b"], 2.0))
    trigli(c, t, C["s06"], 1380, 640, u, "sabao", dy=150, size=54)
    E.foco(c, t, C["s06.a"] + 0.6, 0.4, lambda a: E.pilula(c, "soda cáustica, quente", 1600, 380, 42, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s06.d"], 0.4, lambda a: E.pilula(c, "sal de sódio", 560, 900, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.a"], 0.4, lambda a: E.pilula(c, "o sabão", 560, 980, 52, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s07.b"], 0.4, lambda a: E.pilula(c, "glicerol livre", 1380, 980, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s07.f"], 0.4, lambda a: E.pilula(c, "de sabão: saponificação", 1500, 170, 46, "g", fundo=E.COR, a=a))


# ---------------- biodiesel ----------------
def b_biodiesel(c, t, C, b):
    E.frase(c, t, C["s08"], [("biodiesel", "g", 80, COR)], XE, 170)
    tl = [C["s08.a"], C["s08.a"] + 0.2, C["s08.a"] + 0.4, C["s09.c"], C["s09.c"] + 0.3, C["s09.c"] + 0.5, C["s09.c"] + 0.7]
    Q.equacao(c, t, C["s08.a"], "óleo + 3 CH3OH -> 3 éster + glicerol", W / 2, 300, 60, tl=tl)
    E.saida(c, t, C["s09.d"] - 0.1, lambda: E.foco(c, t, C["s08.a"] + 0.6, 0.4, lambda a: E.pilula(c, "catalisador: acelera e não é gasto", W / 2, 400, 40, "g", fundo=TINTA, a=a)))
    u = ease_io(prog(t, C["s08.b"] + 0.3, 2.0))
    trigli(c, t, C["s08"], 1380, 680, u, "biodiesel", dy=150, size=54)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: E.pilula(c, "sai o glicerol", 1380, 1010, 46, "g", fundo=TINTA2, a=a))
    E.foco(c, t, C["s08.d"], 0.4, lambda a: E.pilula(c, "entra o metanol", 560, 1010, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.b"], 0.4, lambda a: E.pilula(c, "ésteres = biodiesel", 1500, 170, 46, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s09.d"], 0.4, lambda a: E.pilula(c, "éster → éster: transesterificação", W / 2, 400, 46, "g", fundo=TINTA, a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s10"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s10.a"], ps("confundir as duas", "i", 74), XE + 450, 190, passo=0.12)
    E.foco(c, t, C["s10.b"], 0.4, lambda a: E.pilula(c, "as duas soltam glicerol", W / 2, 330, 50, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s10.c"], ps("olhe o", "i", 66) + [("produto principal", "g", 62, COR)], W / 2, 460, "center", 0.12)
    for k, (nome, cab, tipo, vem, tk) in enumerate((("sabão", "COO^- Na^+", "é sal", "veio de uma base", "s10.d"),
                                                   ("biodiesel", "COO–CH3", "é éster", "veio de um álcool", "s10.e"))):
        x = 560 + k * 820
        E.foco(c, t, C[tk], 0.4, lambda a, x=x, nome=nome: centro(c, nome, x, 620, 70, "g", COR, a))
        E.foco(c, t, C[tk] + 0.2, 0.4, lambda a, x=x, cab=cab: (cauda(c, x - 20, 760, n=7, a=a), Q.formula(c, cab, x, 780, 56, TINTA, a, cores={k_: COR for k_ in range(2, 8)})))
        E.foco(c, t, C[tk] + 0.5, 0.4, lambda a, x=x, tipo=tipo, vem=vem: (centro(c, tipo, x, 900, 58, "g", TINTA, a), centro(c, vem, x, 970, 48, "i", TINTA2, a)))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s11.a"], ps("o que", "i", 72, CLARO) + [("entra", "g", 68, BR)] + ps("decide o que", "i", 72, CLARO) + [("sai", "g", 68, BR)], W / 2, 170, "center", 0.12)
    linhas = (("s11.b", "água", "ácido", "hidrólise"), ("s11.c", "base", "sal (sabão)", "saponificação"), ("s11.d", "álcool", "éster", "transesterificação"))
    for i, (k, e, s, n) in enumerate(linhas):
        y = 360 + i * 170
        E.foco(c, t, C[k], 0.4, lambda a, e=e, y=y: E.pilula(c, "entra " + e, 400, y - 20, 50, "g", fundo=E.COR, a=a))
        seta_em(c, t, C[k] + 0.2, 640, 780, y, 70, escuro=True)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, s=s, n=n, y=y: (E.escreve(c, "sai " + s, 830, y, 62, "g", BR, a), E.escreve(c, n, 1390, y, 54, "i", CLARO, a)))
    E.frase(c, t, C["s11.e"], ps("e o glicerol sai", "i", 64, CLARO) + [("sempre", "g", 60, BR)], W / 2, 880, "center", 0.12)
    E.frase(c, t, C["s12.a"], ps("o ácido graxo é o mesmo; muda o parceiro dele", "i", 56, CLARO), W / 2, 990, "center", 0.08)


# ---------------- questão e resposta ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s13"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s13.a"], [("óleo de soja", "g", 64)] + ps("+", "g", 64, TINTA2) + [("etanol", "g", 64, COR)] + ps("+ catalisador", "i", 64), XE, 360, passo=0.12)
    E.frase(c, t, C["s13.b"], [("1", "g", 58, COR)] + ps("que reação? o que se forma?", "i", 62), XE, 500, passo=0.1)
    w = E.frase(c, t, C["s13.c"], [("2", "g", 58, COR)] + ps("e com", "i", 62), XE, 640, passo=0.1)
    Q.formula_em(c, t, C["s13.c"] + 0.5, "KOH", XE + w + 20, 640, 62, cores={"K": COR, "O": COR, "H": COR})
    E.frase(c, t, C["s13.c"] + 0.8, ps("no lugar do etanol?", "i", 62), XE + w + 200, 640, passo=0.1)
    if t >= C["s14"]:
        E.relogio(c, t, C["s14.a"], cx=1480, cy=800, r=150)


def b_resposta(c, t, C, b):
    E.frase(c, t, C["s15"], ps("resolvendo", "i", 72, COR), XE, 170)
    for k, (tk, rot_, prod, x) in enumerate((("s15.a", "entrou álcool: transesterificação", "ésteres de etanol = biodiesel", 520),
                                              ("s16.a", "entrou base: saponificação", "sais de potássio = sabão", 1400))):
        E.foco(c, t, C[tk], 0.4, lambda a, rot_=rot_, x=x, k=k: E.pilula(c, rot_, x, 330, 42, "g", fundo=E.COR if k == 0 else TINTA, a=a))
        if t >= C[tk]:
            u = ease_io(prog(t, C[tk] + 0.3, 1.4))
            c.save(); c.translate(x - 0.55 * 960, 620 - 0.55 * 640); c.scale(0.55, 0.55)
            trigli(c, t, C[tk], 1380, 640, u, "bioetanol" if k == 0 else "sabaoK", dy=170, size=70)
            c.restore()
        tp = C["s15.b"] if k == 0 else C["s16.b"]
        E.foco(c, t, tp, 0.4, lambda a, prod=prod, x=x: centro(c, prod, x, 860, 50, "g", TINTA, a))
        tg = C["s15.c"] if k == 0 else C["s16.c"]
        E.foco(c, t, tg, 0.4, lambda a, x=x: E.pilula(c, "+ glicerol", x, 960, 46, "g", fundo=TINTA2, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s17.a", [("óleo:", "g", 62, COR)] + ps("mais duplas, líquido;", "i", 64) + [("gordura:", "g", 62, COR)] + ps("sólida", "i", 64)),
                 ("s17.b", [("com", "i", 66), ("base:", "g", 62), ("sabão", "g", 62, COR), ("+", "g", 62, TINTA2), ("glicerol", "g", 62)]),
                 ("s17.c", [("com", "i", 66), ("álcool:", "g", 62), ("biodiesel", "g", 62, COR), ("+", "g", 62, TINTA2), ("glicerol", "g", 62)]))
        for i, (k, partes) in enumerate(itens):
            y = 340 + i * 180
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    E.frase(c, t, C["s18"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 230)
    E.frase(c, t, C["s18"] + 0.6, [("praticando", "g", 110, COR)], XE, 370)
    E.frase(c, t, C["s18.a"], ps("todas as reações do módulo", "i", 62, TINTA2), XE, 480, passo=0.1)
    E.foco(c, t, C["s18.b"], 0.4, lambda a: E.pilula(c, "indústria e corpo humano", XE + 280, 600, 50, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s18.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s18.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s18.c"] + 0.2, 0.4))
    E.frase(c, t, C["s18.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, trigli=b_trigli, sabao=b_sabao, biodiesel=b_biodiesel, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
