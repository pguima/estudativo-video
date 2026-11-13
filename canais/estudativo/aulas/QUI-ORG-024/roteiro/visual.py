"""Visual — Estudativo · QUI-ORG-024: praticando reações orgânicas (prática, cinco situações).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001), o complemento da Orgânica de QUI-ORG-015 e a linguagem das
reações de QUI-ORG-018. Prática no modelo de QUI-ORG-017: pílula "situação n", enunciado à esquerda, cena à direita, relógio na
pausa; na resposta, o NOME DA REAÇÃO vai na pílula turquesa e a cena reaproveita as peças das aulas da trilha (adição/eliminação
de QUI-ORG-020, nitração de QUI-ORG-019, oxidação de QUI-ORG-021, triglicerídeo de QUI-ORG-023), copiadas abaixo.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-024_praticando_reacoes_organicas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))

for eq in ("C2H4 + H2 -> C2H6", "C2H6O -> C2H4O + H2", "C6H6 + HNO3 -> C6H5NO2 + H2O", "C2H6O -> C2H4 + H2O",
           "C57H110O6 + 3 H2O -> 3 C18H36O2 + C3H8O3"):
    assert Q.lados(eq)[0] == Q.lados(eq)[1], eq


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


# (peças copiadas de QUI-ORG-020)
ANTES = [(-1.25, -0.95), (-1.25, 0.95), (1.25, -0.95), (1.25, 0.95)]


DEPOIS = [(-1.8, 0.0), (-0.62, 1.15), (1.8, 0.0), (0.62, 1.15)]


REAG = [(-0.45, -2.0), (0.45, -2.0)]


NOVO = [(-0.62, -1.15), (0.62, -1.15)]


def reacao(c, t, t0, tu, cx, cy, esc, size, subs, pecas=("H", "OH"), volta=False, escuro=False, cores=None, d=1.4, a=1.0, dx=None, cor_p=None):
    """a adição de QUI-ORG-018 nos dois sentidos. volta=True = eliminação: começa no composto em cruz e, a partir de tu,
    as pecas sobem e saem juntas (H–OH) enquanto a dupla fecha. Devolve os pontos: C1, C2, 4 ligantes, 2 peças"""
    u = ease_io(prog(t, tu, d)) if tu is not None else 0.0
    if volta:
        u = 1 - u
    dx = dx or {}
    lig = [(lerp(x0, x1, u) + dx.get(k, 0) * (1 if x1 > 0 else -1) * u, lerp(y0, y1, u)) for k, ((x0, y0), (x1, y1)) in enumerate(zip(ANTES, DEPOIS))]
    nov = [(lerp(x0, x1, u), lerp(y0, y1, u)) for (x0, y0), (x1, y1) in zip(REAG, NOVO)]
    at = [("C", -0.62, 0), ("C", 0.62, 0)] + [(s, x, y) for s, (x, y) in zip(subs, lig)] + [(s, x, y) for s, (x, y) in zip(pecas, nov)]
    ordem = 2 if u < 0.45 else 1
    ligs = [(0, 1, ordem, E.COR if ordem == 2 else None), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]
    if u < 0.25:
        ligs.append((6, 7, 1))
    if u > 0.75:
        ligs += [(0, 6, 1), (1, 7, 1)]
    cr = dict(cores or {})
    cp = cor_p or (TINTA2 if volta else (CLARO if escuro else COR))
    cr.setdefault(6, cp); cr.setdefault(7, cp)
    return estr(c, t, t0, at, ligs, cx, cy, esc, size, passo=0.08, cores=cr, escuro=escuro, a=a)


ETANOL_SUBS = ("H", "H", "H", "H")

# (peças copiadas de QUI-ORG-019)
def benzeno_sub(c, t, t0, cx, cy, R, u, sai="H", entra="NO2", escuro=False):
    """anel do benzeno com um ligante na direita: sai o H (desliza para baixo) e entra o grupo novo"""
    q = 1.0 if t0 is None else ep(t, t0, 0.5)
    anel(c, cx, cy, R, q, Q._tinta(escuro), giro=0)
    x0 = cx + R
    M.line(c, x0, cy, x0 + 70, cy, Q._tinta(escuro), q, 7)
    if u < 1:
        rot(c, sai, lerp(x0 + 110, x0 + 220, u), lerp(cy, cy + 200, u), 80, TINTA2 if u > 0 else Q._tinta(escuro), q * (1 - 0.5 * u))
    if u > 0:
        w = _meia(entra, 80)[0]
        rot(c, entra, lerp(x0 + 380, x0 + 80 + w, u), lerp(cy - 200, cy, u), 80, CLARO if escuro else COR, q * min(1, u * 2))

# (peças copiadas de QUI-ORG-021)
ETANOL = ([("H3C", -1.2, 0), ("C", 0, 0), ("H", 0, -1), ("H", 0, 1), ("O", 1.05, 0), ("H", 1.85, 0)],
          [(0, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1), (4, 5, 1)])


ETANAL = ([("H3C", -1.2, 0), ("C", 0, 0), ("O", 0, -1.05), ("H", 0, 1)], [(0, 1, 1), (1, 2, 2, E.COR), (1, 3, 1)])


ACIDO = ([("H3C", -1.2, 0), ("C", 0, 0), ("O", 0, -1.05), ("OH", 0, 1.05)], [(0, 1, 1), (1, 2, 2), (1, 3, 1)])


def mol(c, t, t0, M_, cx, cy, esc=110, size=64, cores=None, a=1.0, escuro=False):
    return estr(c, t, t0, M_[0], M_[1], cx, cy, esc, size, passo=0.06, cores=cores, a=a, escuro=escuro)


def seta_o(c, t, t0, x0, x1, y, escuro=False):
    seta_em(c, t, t0, x0, x1, y + 24, 100, rotulo="[O]", escuro=escuro)

# (peças copiadas de QUI-ORG-023)
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

# (peças copiadas de QUI-ORG-020)
def cana(c, x, y, h, a=1.0):
    """um colmo de cana com nós e duas folhas"""
    if a <= 0:
        return
    for k in range(5):
        M.rrect(c, x - 18, y - h + k * h / 5, 36, h / 5 - 6, 10, "#7FB24A", a)
    for s in (-1, 1):
        pth = skia.Path(); pth.moveTo(x, y - h * 0.9); pth.quadTo(x + s * 120, y - h * 1.1, x + s * 170, y - h * 0.7)
        c.drawPath(pth, M.paint("#5E9A35", a, stroke=10))


# ---------------- peças desta aula ----------------
def situacao(c, t, t0, n):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"situação {n}", XE + 150, 150, 50, "g", fundo=E.COR, a=a))


def pausa(c, t, C, k, cx=1480, cy=600, r=180):
    if t >= C[k]:
        E.relogio(c, t, C[k + ".a"], cx=cx, cy=cy, r=r)


def tipo(c, t, t0, s, cx=W / 2, y=960, size=64):
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, s, cx, y, size, "g", fundo=E.COR, a=a))


def figado(c, cx, cy, s, a=1.0):
    """o fígado em silhueta"""
    if a <= 0:
        return
    pth = skia.Path()
    pth.moveTo(cx - 1.2 * s, cy - 0.3 * s)
    pth.cubicTo(cx - 0.9 * s, cy - 1.0 * s, cx + 0.8 * s, cy - 0.9 * s, cx + 1.2 * s, cy - 0.5 * s)
    pth.cubicTo(cx + 1.0 * s, cy + 0.1 * s, cx + 0.2 * s, cy + 0.8 * s, cx - 0.6 * s, cy + 0.6 * s)
    pth.cubicTo(cx - 1.1 * s, cy + 0.4 * s, cx - 1.3 * s, cy + 0.1 * s, cx - 1.2 * s, cy - 0.3 * s)
    c.drawPath(pth, M.paint("#9C3B32", a))


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR)], XE, 380)
    E.frase(c, t, C["s01.a"] + 0.4, ps("situações", "i", 110), XE + 170, 380)
    E.frase(c, t, C["s01.b"], ps("da fábrica e do corpo humano", "i", 66, TINTA2), XE, 500, passo=0.1)
    E.frase(c, t, C["s01.c"], ps("que reação? o que se forma?", "g", 60), XE, 650, passo=0.1)
    pilula_em(c, t, C["s01.d"], "pause e resolva", XE + 260, 800, 60, E.COR)
    E.foco(c, t, C["s01.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1600, 420, 220 * a, giro=8 * math.sin(t * 0.4)), blur=0)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 76, TINTA2), XE, 200, passo=0.12)
    itens = (("s02.a", "adição"), ("s02.b", "substituição"), ("s02.c", "eliminação"), ("s02.d", "oxidação"),
             ("s02.e", "esterificação, hidrólise e saponificação"))
    for i, (k, s) in enumerate(itens):
        y = 330 + i * 120
        E.foco(c, t, C[k], 0.4, lambda a, i=i, y=y: (E.bola(c, XE + 36, y - 22, 38, a=a), centro(c, str(i + 1), XE + 36, y - 3, 46, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 62)], XE + 100, y)
    E.foco(c, t, C["s02.e"] + 1.2, 0.4, lambda a: E.pilula(c, "travou? procure a aula no canal", 1450, 960, 44, "b", fundo=TINTA2, a=a))


# ---------------- 1: margarina ----------------
def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1)
    E.frase(c, t, C["s03.b"], [("óleo", "g", 64), ("+", "g", 64, TINTA2), ("H₂", "g", 64, COR)] + ps("com níquel, quente", "i", 62, TINTA2), XE, 360, passo=0.12)
    E.frase(c, t, C["s03.c"], ps("líquido vira", "i", 66) + [("gordura pastosa", "g", 62)], XE, 480, passo=0.12)
    E.frase(c, t, C["s03.d"], ps("que reação? e as duplas?", "i", 66, COR), XE, 640, passo=0.12)
    if t < C["s04"]:
        Q.bequer(c, t, C["s03.b"], 1450, 860, 340, 400, 0.7, OLEO, graduacao=False)
    pausa(c, t, C, "s04")


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05"], ps("resolvendo", "i", 64, COR), XE, 165)
    Q.equacao(c, t, C["s05.a"], "CH2=CH2 + H2 -> CH3–CH3", W / 2, 300, 70, cores={2: COR})
    E.foco(c, t, C["s05.a"] + 0.4, 0.4, lambda a: centro(c, "(em cada dupla do óleo)", W / 2, 380, 44, "i", TINTA2, a))
    reacao(c, t, C["s05.a"] + 0.3, C["s05.a"] + 0.8, W / 2, 690, 130, 70, ETANOL_SUBS, ("H", "H"))
    tipo(c, t, C["s05.b"], "adição: hidrogenação")
    E.foco(c, t, C["s05.c"], 0.4, lambda a: E.pilula(c, "dupla → simples", 380, 690, 48, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s05.d"], 0.4, lambda a: E.pilula(c, "margarina", 1540, 690, 56, "g", fundo=TINTA, a=a))


# ---------------- 2: fígado ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C["s06.a"], 2)
    E.frase(c, t, C["s06.b"], ps("no fígado:", "i", 64) + [("etanol", "g", 62), ("→", "g", 62, TINTA2), ("etanal", "g", 62, COR)], XE, 360, passo=0.12)
    E.frase(c, t, C["s06.c"], ps("ligado à ressaca", "i", 58, TINTA2), XE, 460, passo=0.1)
    E.frase(c, t, C["s06.d"], ps("etanol:", "i", 62) + [("álcool primário", "g", 58)], XE, 580, passo=0.1)
    E.frase(c, t, C["s06.e"], ps("que reação? e se continuar?", "i", 66, COR), XE, 720, passo=0.12)
    if t < C["s07"]:
        E.foco(c, t, C["s06.b"], 0.5, lambda a: figado(c, 1450, 560, 220, a))
    pausa(c, t, C, "s07")


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s08"], ps("resolvendo", "i", 64, COR), XE, 165)
    y = 520
    mol(c, t, C["s08"], ETANOL, 360, y, 110, 64, cores={1: COR})
    seta_o(c, t, C["s08.a"], 610, 780, y)
    mol(c, t, C["s08.a"] + 0.3, ETANAL, 1020, y, 110, 64)
    E.foco(c, t, C["s08.c"], 0.4, lambda a: centro(c, "etanal (aldeído)", 1020, 740, 50, "g", COR, a))
    seta_o(c, t, C["s08.d"], 1220, 1390, y)
    mol(c, t, C["s08.d"] + 0.3, ACIDO, 1620, y, 110, 64)
    E.foco(c, t, C["s08.d"] + 0.6, 0.4, lambda a: centro(c, "ácido acético", 1620, 740, 50, "g", COR, a))
    tipo(c, t, C["s08.b"], "oxidação")


# ---------------- 3: nitração ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C["s09.a"], 3)
    E.frase(c, t, C["s09.b"], ps("fábrica de corantes:", "i", 64), XE, 360, passo=0.12)
    Q.formula_em(c, t, C["s09.b"] + 0.6, "C6H6 + HNO3", XE, 480, 80)
    E.foco(c, t, C["s09.b"] + 1.0, 0.4, lambda a: E.escreve(c, "com um pouco de ácido sulfúrico", XE, 570, 50, "i", TINTA2, a))
    E.frase(c, t, C["s09.c"], ps("que reação? que produto?", "i", 66, COR), XE, 720, passo=0.12)
    if t < C["s10"]:
        benzeno_sub(c, t, C["s09.b"], 1450, 560, 150, 0.0)
    pausa(c, t, C, "s10")


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s11"], ps("resolvendo", "i", 64, COR), XE, 165)
    Q.equacao(c, t, C["s11"], "C6H6 + HNO3 -> C6H5NO2 + H2O", W / 2, 300, 70, tl=[C["s11"], C["s11"] + 0.2, C["s11"] + 0.4, C["s11.b"], C["s11.d"], C["s11.e"] - 0.2, C["s11.e"]])
    benzeno_sub(c, t, C["s11"], 760, 640, 140, ease_io(prog(t, C["s11.b"], 1.4)))
    E.foco(c, t, C["s11.a"], 0.4, lambda a: E.pilula(c, "o anel não abre", 760, 440, 46, "g", fundo=TINTA, a=a))
    tipo(c, t, C["s11.c"], "substituição: nitração")
    E.foco(c, t, C["s11.d"], 0.4, lambda a: centro(c, "nitrobenzeno", 1460, 660, 60, "g", COR, a))
    E.foco(c, t, C["s11.e"], 0.4, lambda a: E.pilula(c, "+ água", 1460, 760, 48, "g", fundo=TINTA2, a=a))


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s12.a"], ps("compare o", "i", 70, CLARO) + [("antes", "g", 66, BR)] + ps("e o", "i", 70, CLARO) + [("depois", "g", 66, BR)], W / 2, 140, "center", 0.12)
    linhas = (("s12.b", "sumiu dupla, nada saiu", "adição"), ("s12.c", "apareceu dupla, saiu molécula pequena", "eliminação"),
              ("s12.d", "átomo ou grupo no lugar de um H", "substituição"), ("s13.a", "C perdeu H, ganhou O", "oxidação"),
              ("s13.b", "apareceu éster, saiu água", "esterificação"), ("s13.c", "éster quebrou com água / com base", "hidrólise / saponificação"))
    for i, (k, s, n) in enumerate(linhas):
        y = 270 + i * 112
        E.foco(c, t, C[k], 0.4, lambda a, s=s, y=y: E.escreve(c, s, XE, y, 50, "g", BR, a))
        E.foco(c, t, C[k] + 0.4, 0.4, lambda a, n=n, y=y: E.pilula(c, n, 1500, y - 17, 44, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s13.d"], ps("cada tipo deixa uma marca na fórmula", "i", 58, CLARO), W / 2, 1000, "center", 0.1)


# ---------------- 4: plástico verde ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C["s14.a"], 4)
    E.frase(c, t, C["s14.b"], ps("usina:", "i", 64) + [("etanol", "g", 62)] + ps("a 170 °C, com ácido sulfúrico", "i", 60, TINTA2), XE, 360, passo=0.1)
    E.frase(c, t, C["s14.c"], ps("sai um", "i", 64) + [("gás que vira plástico", "g", 60)] + ps("e sai água", "i", 64), XE, 480, passo=0.1)
    E.frase(c, t, C["s14.d"], ps("que reação? que gás?", "i", 66, COR), XE, 640, passo=0.12)
    if t < C["s15"]:
        E.foco(c, t, C["s14.b"], 0.5, lambda a: (cana(c, 1400, 940, 420, a), cana(c, 1520, 960, 380, a)))
    pausa(c, t, C, "s15", 1480, 700, 150)


def b_resposta4(c, t, C, b):
    E.frase(c, t, C["s16"], ps("resolvendo", "i", 64, COR), XE, 165)
    Q.equacao(c, t, C["s16"], "CH3–CH2–OH -> CH2=CH2 + H2O", W / 2, 300, 70, tl=[C["s16"], C["s16.b"], C["s16.d"], C["s16.a"], C["s16.a"] + 0.2])
    reacao(c, t, C["s16"] + 0.3, C["s16.a"], W / 2, 690, 130, 70, ETANOL_SUBS, ("H", "OH"), volta=True)
    tipo(c, t, C["s16.c"], "eliminação: desidratação")
    E.foco(c, t, C["s16.d"] + 0.5, 0.4, lambda a: E.pilula(c, "eteno", 1540, 690, 56, "g", fundo=TINTA, a=a))


# ---------------- 5: digestão ----------------
def b_questao5(c, t, C, b):
    situacao(c, t, C["s17.a"], 5)
    E.frase(c, t, C["s17.b"], ps("no intestino: gordura +", "i", 64) + [("água", "g", 60, COR)] + ps("com enzima", "i", 64), XE, 340, passo=0.1)
    E.frase(c, t, C["s17.c"], ps("saem", "i", 64) + [("ácidos graxos", "g", 60)] + ps("e", "i", 64) + [("glicerol", "g", 60)], XE, 450, passo=0.1)
    E.frase(c, t, C["s17.d"], ps("gordura = triéster", "g", 56, TINTA2), XE, 560, passo=0.1)
    E.frase(c, t, C["s17.e"], ps("que reação?", "i", 66, COR), XE, 680, passo=0.12)
    if t < C["s18"]:
        c.save(); c.translate(1500 - 0.62 * 930, 640 - 0.62 * 640); c.scale(0.62, 0.62)
        trigli(c, t, C["s17.b"], 1380, 640)
        c.restore()
    pausa(c, t, C, "s18", 1480, 700, 150)


def b_resposta5(c, t, C, b):
    E.frase(c, t, C["s19"], ps("resolvendo", "i", 64, COR), XE, 165)
    c.save(); c.translate(W / 2 - 0.7 * 960, 560 - 0.7 * 640); c.scale(0.7, 0.7)
    trigli(c, t, C["s19"], 1380, 640, ease_io(prog(t, C["s19.a"], 1.6)), "acido")
    c.restore()
    E.foco(c, t, C["s19.b"], 0.4, lambda a: E.pilula(c, "ácidos graxos + glicerol", W / 2, 860, 50, "g", fundo=TINTA, a=a))
    tipo(c, t, C["s19.c"], "hidrólise")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.frase(c, t, C["s20.a"], [("3", "g", 110, COR)] + ps("ou mais? módulo firme", "i", 76), XE, 280, passo=0.12)
    E.frase(c, t, C["s20.a"] + 1.6, ps("travou? reveja a aula da reação", "i", 60, TINTA2), XE, 390, passo=0.1)
    E.frase(c, t, C["s20.b"] - 0.8, [("próxima", "i", 76), ("aula", "i", 76)], XE, 560)
    E.frase(c, t, C["s20.c"], [("polímeros", "g", 110, COR)], XE, 700)
    Q.formula_em(c, t, C["s20.c"] + 0.6, "[–CH2–CH2–]", XE, 840, 70)
    E.foco(c, t, C["s20.c"] + 0.6, 0.4, lambda a: E.escreve(c, "n", XE + Q.formula(None, "[–CH2–CH2–]", 0, 0, 70) + 6, 870, 50, "g", TINTA, a))
    E.foco(c, t, C["s20.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s20.d"] + 0.2, 0.4))
    E.frase(c, t, C["s20.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
