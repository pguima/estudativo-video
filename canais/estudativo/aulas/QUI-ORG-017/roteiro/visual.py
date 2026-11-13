"""Visual — Estudativo · QUI-ORG-017: praticando propriedades e isomeria (prática, cinco situações).

Segue a LINGUAGEM VISUAL DA QUÍMICA (cabeçalho de QUI-MIS-001) e o complemento da Orgânica de QUI-ORG-015 (estr, alceno).
Prática: cada situação abre com a pílula "situação n", o enunciado à esquerda e o desenho à direita; a pausa usa E.relogio
no lugar do desenho; a resposta mantém o desenho e acende, na cor da matéria, o pedaço que decide.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-017_praticando_propriedades_isomeria.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "atalho", "questao4", "questao5", "fim"))

# fórmulas e massas da aula (C = 12, H = 1, O = 16)
MASSA = dict(C=12, H=1, O=16)
massa = lambda f: sum(MASSA[e] * n for e, n in Q.contar(f).items())
assert massa("CH3CH2CH2CH2CH3") == 72 and massa("CH3CH2CH2CH2OH") == 74 and massa("CH3CH2COOH") == 74
assert Q.contar("CH3CH2OH") == Q.contar("CH3OCH3") == Q.contar("C2H6O")
assert Q.contar("C6H8O6") == {"C": 6, "H": 8, "O": 6} and Q.contar("C20H30O") == {"C": 20, "H": 30, "O": 1}
PE = [("pentano", "CH3–CH2–CH2–CH2–CH3", 36), ("butan-1-ol", "CH3–CH2–CH2–CH2–OH", 118), ("ácido propanoico", "CH3–CH2–COOH", 141)]
assert [p[2] for p in PE] == sorted(p[2] for p in PE)  # a ordem da resposta


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


def situacao(c, t, t0, n):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, f"situação {n}", XE + 150, 150, 50, "g", fundo=E.COR, a=a))


def pausa(c, t, C, k, cx=1480, cy=560, r=190):
    if t >= C[k]:
        E.relogio(c, t, C[k + ".a"], cx=cx, cy=cy, r=r)


def cadeia(x0, y0, ang, n, L, lado=1):
    """n pontos em zigue-zague a partir de (x0, y0), na direção ang (graus); L = comprimento de cada ligação em px"""
    ux, uy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))
    px, py = -uy * lado, ux * lado
    return [(x0 + ux * L * 0.87 * k + px * L * 0.5 * (k % 2), y0 + uy * L * 0.87 * k + py * L * 0.5 * (k % 2)) for k in range(n)]


def graxo(c, t, t0, cx, cy, esc, cis=True, a=1.0, n=6, escuro=False, cor_dupla=None):
    """ácido graxo com uma dupla no meio: cis dobra a cadeia, trans deixa reta. A ponta esquerda é o COOH"""
    tinta = Q._tinta(escuro)
    cd = cor_dupla or E.COR
    A, B = (cx - 0.5 * esc, cy), (cx + 0.5 * esc, cy)
    p = 1.0 if t0 is None else ease_out(prog(t, t0, 0.5))
    if p <= 0:
        return
    k = esc * 0.09
    M.line(c, A[0], A[1] - k, B[0], B[1] - k, cd, a * p, 7)
    M.line(c, A[0], A[1] + k, B[0], B[1] + k, cd, a * p, 7)
    esq = cadeia(A[0], A[1], 150, n, esc)
    dir_ = cadeia(B[0], B[1], 30 if cis else -30, n, esc)
    for pts, tk in ((esq, 0.2), (dir_, 0.4)):
        q = 1.0 if t0 is None else ease_out(prog(t, t0 + tk, 0.6))
        m = max(1, int(round(q * (len(pts) - 1))))
        for i in range(m):
            M.line(c, *pts[i], *pts[i + 1], tinta, a, 7)
    q = 1.0 if t0 is None else ep(t, t0 + 0.8, 0.4)
    rot(c, "COOH", esq[-1][0] - 70, esq[-1][1] - 10, 46, tinta, a * q)
    for P, dy in ((A, 1), (B, 1 if cis else -1)):
        rot(c, "H", P[0] + (0.2 if P is B else -0.2) * esc, P[1] + dy * esc * 0.8, 44, tinta, a * q)


def ibuprofeno(c, t, t0, cx, cy, s=1.0, cores=None, a=1.0):
    """ibuprofeno: anel de benzeno no meio; à direita o CH quiral com CH3 e COOH; à esquerda CH2 e CH(CH3)2. Devolve os pontos"""
    R = 105 * s
    q = 1.0 if t0 is None else ep(t, t0, 0.5)
    anel(c, cx, cy, R, a * q, giro=0)
    sz = 62 * s
    at = [("", R, 0), ("CH", R + 140 * s, 0), ("CH3", R + 140 * s, 135 * s), ("COOH", R + 330 * s, 0),
          ("", -R, 0), ("CH2", -R - 140 * s, 0), ("CH", -R - 290 * s, 0), ("H3C", -R - 390 * s, -110 * s), ("H3C", -R - 390 * s, 110 * s)]
    at = [(r_, x / 150, y / 150) for r_, x, y in at]
    ligs = [(0, 1, 1), (1, 2, 1), (1, 3, 1), (4, 5, 1), (5, 6, 1), (6, 7, 1), (6, 8, 1)]
    return estr(c, t, t0 + 0.4 if t0 is not None else None, at, ligs, cx, cy, 150, sz, passo=0.08, cores=cores, a=a)


def vitamina_c(c, x, y, a=1.0):
    """esquema da vitamina C: um anel pequeno com quatro OH em volta"""
    if a <= 0:
        return
    pts = [(x + 90 * math.cos(math.radians(90 + 72 * k)), y - 90 * math.sin(math.radians(90 + 72 * k))) for k in range(5)]
    for k in range(5):
        M.line(c, *pts[k], *pts[(k + 1) % 5], TINTA, a, 7)
    for k, (dx, dy) in enumerate(((-190, -40), (-150, 150), (190, -40), (200, 150))):
        P = pts[[1, 2, 4, 3][k]]
        M.line(c, *P, x + dx * 0.72, y + dy * 0.72, TINTA, a, 6)
        rot(c, "OH", x + dx, y + dy, 58, COR, a)


def vitamina_a(c, t, t0, x, y, a=1.0):
    """esquema da vitamina A: cadeia longa de carbono com um OH na ponta"""
    pts = cadeia(x, y, 0, 12, 74)
    q = 1.0 if t0 is None else ease_out(prog(t, t0, 1.0))
    m = max(1, int(round(q * (len(pts) - 1))))
    for i in range(m):
        M.line(c, *pts[i], *pts[i + 1], TINTA, a, 7)
    if q >= 1:
        rot(c, "OH", pts[-1][0] + 70, pts[-1][1], 58, COR, a)
    return pts


# ---------------- gancho e lembrete ----------------
def b_gancho(c, t, C, b):
    E.frase(c, t, C["s01.a"], [("5", "g", 200, COR)], XE, 380)
    E.frase(c, t, C["s01.a"] + 0.4, ps("situações", "i", 110), XE + 170, 380)
    E.frase(c, t, C["s01.b"], ps("remédios, alimentos e o dia a dia", "i", 66, TINTA2), XE, 500, passo=0.1)
    E.frase(c, t, C["s01.c"], ps("em cada uma:", "i", 70), XE, 720, passo=0.1)
    pilula_em(c, t, C["s01.c"] + 0.6, "pause e resolva", XE + 650, 700, 60, E.COR)
    E.foco(c, t, C["s01.a"] + 0.4, 0.8, lambda a: E.simbolo(c, 1600, 420, 220 * a, giro=8 * math.sin(t * 0.4)), blur=0)


def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s02"], ps("você vai usar", "i", 76, TINTA2), XE, 200, passo=0.12)
    itens = (("s02.a", "ponto de ebulição"), ("s02.b", "semelhante dissolve semelhante"), ("s02.c", "isomeria plana"),
             ("s02.d", "cis e trans"), ("s02.e", "carbono quiral"))
    for i, (k, s) in enumerate(itens):
        y = 330 + i * 120
        E.foco(c, t, C[k], 0.4, lambda a, i=i, y=y: (E.bola(c, XE + 36, y - 22, 38, a=a), centro(c, str(i + 1), XE + 36, y - 3, 46, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, [(s, "g", 62)], XE + 100, y)
    E.foco(c, t, C["s02.e"] + 0.8, 0.4, lambda a: E.pilula(c, "travou? procure a aula no canal", 1450, 960, 44, "b", fundo=TINTA2, a=a))


# ---------------- 1: ponto de ebulição ----------------
def linhas_pe(c, t, t0s, cores=None):
    for i, ((nome, f, _), tk) in enumerate(zip(PE, t0s)):
        y = 380 + i * 200
        E.foco(c, t, tk, 0.4, lambda a, nome=nome, y=y: E.escreve(c, nome, XE, y - 70, 50, "i", TINTA2, a))
        Q.formula_em(c, t, tk + 0.2, f, XE, y, 70, cores=(cores or {}).get(i))


def b_questao1(c, t, C, b):
    situacao(c, t, C["s03.a"], 1)
    linhas_pe(c, t, [C["s03.b"], C["s03.c"], C["s03.d"]])
    E.frase(c, t, C["s03.e"], ps("ordem do menor para o maior", "i", 60) + [("ponto de ebulição", "g", 56, COR)], XE, 1000, passo=0.1)
    E.foco(c, t, C["s03.a"] + 0.4, 0.4, lambda a: E.escreve(c, "massas parecidas: 72, 74 e 74", 1100, 165, 46, "i", TINTA2, a))
    pausa(c, t, C, "s04", 1540, 560, 180)


def b_resposta1(c, t, C, b):
    E.frase(c, t, C["s05"], ps("resolvendo", "i", 64, COR), XE + 360, 165)
    linhas_pe(c, t, [-9] * 3, {1: {"O": COR}, 2: {"O": COR}} if t >= C["s05.c"] else None)
    for i, (tk, tv) in enumerate((("s05.a", "s05.b"), ("s05.c", "s05.d"), ("s05.e", "s05.f"))):
        y = 380 + i * 200
        v = PE[i][2]
        p = ease_out(prog(t, C[tv], 0.8))
        if p > 0:
            x0, w = 1150, 3.6 * v * p
            M.rrect(c, x0, y - 55, w, 56, 12, E.COR if i == 2 else TINTA2, 1)
            E.escreve(c, f"{v} °C", x0 + w + 20, y - 8, 54, "g", TINTA, ep(t, C[tv] + 0.6, 0.3))
        rotulo = ("atração fraca", "ligação de hidrogênio", "mais ligações de H, aos pares")[i]
        E.foco(c, t, C[tk] + 0.3, 0.4, lambda a, y=y, rotulo=rotulo: E.escreve(c, rotulo, 1150, y + 50, 44, "i", TINTA2, a))
    E.frase(c, t, C["s06.a"], [("pentano", "g", 56), ("<", "g", 56, COR), ("álcool", "g", 56), ("<", "g", 56, COR), ("ácido", "g", 56)], XE, 1000, passo=0.15)
    E.frase(c, t, C["s06.b"], ps("massa parecida:", "i", 54, TINTA2) + [("manda a atração", "g", 50, COR)], 1180, 1000, passo=0.1)


# ---------------- 2: solubilidade ----------------
def b_questao2(c, t, C, b):
    situacao(c, t, C["s07.a"], 2)
    E.frase(c, t, C["s07.b"], [("vitamina C", "g", 64)], XE, 330)
    E.frase(c, t, C["s07.b"] + 0.5, [("4", "g", 58, COR), ("OH,", "g", 58)] + ps("molécula pequena", "i", 60, TINTA2), XE, 420, passo=0.1)
    E.frase(c, t, C["s07.c"], [("vitamina A", "g", 64)], XE, 620)
    E.frase(c, t, C["s07.c"] + 0.5, [("1", "g", 58, COR), ("OH", "g", 58)] + ps("na ponta de uma cadeia longa", "i", 60, TINTA2), XE, 710, passo=0.1)
    E.frase(c, t, C["s07.d"], ps("qual vai na", "i", 62) + [("água?", "g", 58, COR)] + ps("qual precisa de", "i", 62) + [("gordura?", "g", 58, COR)], XE, 960, passo=0.1)
    if t < C["s08"]:
        E.foco(c, t, C["s07.b"] + 0.4, 0.5, lambda a: vitamina_c(c, 1450, 360, a))
        vitamina_a(c, t, C["s07.c"] + 0.4, 1000, 740)
    pausa(c, t, C, "s08", 1480, 560, 190)


def b_resposta2(c, t, C, b):
    E.frase(c, t, C["s09.a"], ps("semelhante dissolve", "i", 76) + [("semelhante", "g", 70, COR)], W / 2, 170, "center", 0.12)
    Q.bequer(c, t, C["s09.b"], 560, 900, 400, 420, 0.7, Q.AGUA, graduacao=False, rotulo=None,
             particulas=dict(n=22, estado="gas", tipos=[(E.COR, 1.0)], r=12, semente=3))
    E.foco(c, t, C["s09.b"] + 0.3, 0.4, lambda a: centro(c, "água", 560, 990, 54, "g", TINTA, a))
    E.foco(c, t, C["s09.b"] + 0.5, 0.4, lambda a: E.pilula(c, "vitamina C: polar", 560, 390, 50, "g", fundo=E.COR, a=a))
    x_em(c, t, C["s09.c"], 820, 420, 40, True)
    Q.bequer(c, t, C["s09.d"], 1360, 900, 400, 420, 0.7, OLEO, graduacao=False)
    E.foco(c, t, C["s09.d"] + 0.3, 0.4, lambda a: centro(c, "gordura", 1360, 990, 54, "g", TINTA, a))
    E.foco(c, t, C["s09.d"] + 0.8, 0.4, lambda a: E.pilula(c, "vitamina A: quase apolar", 1360, 390, 46, "g", fundo=TINTA, a=a))
    x_em(c, t, C["s09.e"], 1700, 420, 40, True)
    if t >= C["s09.d"] + 0.4:
        c.save(); c.translate(1220, 730); c.scale(0.5, 0.5)
        vitamina_a(c, t, C["s09.d"] + 0.6, 0, 0)
        c.restore()


# ---------------- 3: isomeria de função ----------------
def b_questao3(c, t, C, b):
    situacao(c, t, C["s10.a"], 3)
    E.frase(c, t, C["s10.b"], [("etanol", "g", 64)], XE, 330)
    Q.formula_em(c, t, C["s10.b"] + 0.4, "CH3–CH2–OH", XE + 300, 330, 70)
    E.frase(c, t, C["s10.c"], [("metoximetano", "g", 64)], XE, 480)
    Q.formula_em(c, t, C["s10.c"] + 0.4, "CH3–O–CH3", XE + 470, 480, 70)
    E.foco(c, t, C["s10.d"], 0.4, lambda a: E.escreve(c, "os dois:", XE, 630, 56, "i", TINTA2, a))
    Q.formula_em(c, t, C["s10.d"] + 0.2, "C2H6O", XE + 230, 630, 70, cores={"indice": COR})
    E.frase(c, t, C["s10.e"], [("1", "g", 56, COR)] + ps("que tipo de isomeria?", "i", 62), XE, 820, passo=0.1)
    E.frase(c, t, C["s10.f"], [("2", "g", 56, COR)] + ps("qual ferve mais alto?", "i", 62), XE, 920, passo=0.1)
    pausa(c, t, C, "s11", 1480, 600, 190)


def b_resposta3(c, t, C, b):
    E.frase(c, t, C["s12"], ps("resolvendo", "i", 64, COR), XE, 170)
    Q.formula(c, "CH3–CH2–OH", 520, 400, 90, TINTA, 1, "center", cores={"O": COR, 3: COR} if t >= C["s12.a"] else None)
    Q.formula(c, "CH3–O–CH3", 1400, 400, 90, TINTA, 1, "center", cores={"O": COR} if t >= C["s12.b"] else None)
    E.foco(c, t, C["s12.a"], 0.4, lambda a: E.pilula(c, "álcool: OH", 520, 520, 54, "g", fundo=E.COR, a=a))
    E.foco(c, t, C["s12.b"], 0.4, lambda a: E.pilula(c, "éter: O entre carbonos", 1400, 520, 54, "g", fundo=TINTA, a=a))
    E.frase(c, t, C["s12.c"], [("isomeria", "i", 84), ("de função", "g", 80, COR)], W / 2, 720, "center", 0.12)
    E.foco(c, t, C["s12.e"], 0.4, lambda a: E.pilula(c, "78 °C", 520, 900, 64, "g", fundo=CERTO, a=a))
    E.foco(c, t, C["s12.f"], 0.4, lambda a: E.pilula(c, "−24 °C", 1400, 900, 64, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s12.d"], ps("ligação de hidrogênio", "i", 52, TINTA2), 520, 1010, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    E.frase(c, t, C["s13"], ps("isomeria em", "i", 72, CLARO) + [("3 perguntas", "g", 68, BR)], W / 2, 150, "center", 0.12)
    perg = (("s13.a", "mesma fórmula molecular?", "não: nem são isômeros"),
            ("s13.b", "ligados em ordem diferente?", "sim: isomeria plana"),
            ("s13.c", "só muda no espaço?", "sim: cis e trans, ou óptica"))
    for i, (k, p_, r_) in enumerate(perg):
        y = 330 + i * 200
        E.foco(c, t, C[k], 0.4, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 22, 44, a=a), centro(c, str(i + 1), XE + 40, y - 2, 54, "g", E.SOBRE, a)))
        E.frase(c, t, C[k] + 0.1, [(p_, "g", 58, BR)], XE + 110, y, passo=0.1)
        tr = C["s13.d"] if i == 2 else C[k] + 1.6
        E.foco(c, t, tr, 0.4, lambda a, y=y, r_=r_, i=i: E.pilula(c, r_, 1460, y - 20, 46, "g", fundo=ERRADO if i == 0 else E.COR, a=a))
        if i < 2:
            p = ease_out(prog(t, C[perg[i + 1][0]] - 0.3, 0.4))
            if p > 0:
                M.arrow(c, XE + 40, y + 30, XE + 40, y + 30 + 100 * p, E.CLARO, 1, 5, 16, 1)
    E.frase(c, t, C["s14.a"], ps("a questão já diz o tipo?", "i", 56, CLARO) + [("vá direto à regra", "g", 52, BR)], W / 2, 1000, "center", 0.1)


# ---------------- 4: cis e trans nas gorduras ----------------
def b_questao4(c, t, C, b):
    situacao(c, t, C["s15.a"], 4)
    E.frase(c, t, C["s15.b"], [("ácido oleico", "g", 60)] + ps("do azeite", "i", 60, TINTA2), XE, 290, passo=0.1)
    E.frase(c, t, C["s15.c"], [("ácido elaídico", "g", 60)] + ps("gorduras industrializadas", "i", 60, TINTA2), XE, 380, passo=0.1)
    E.foco(c, t, C["s15.c"] + 1.0, 0.4, lambda a: E.escreve(c, "mesma fórmula, mesmas ligações", XE, 470, 52, "i", TINTA2, a))
    if t < C["s16"]:
        graxo(c, t, C["s15.d"], 500, 760, 80, True, n=5)
        E.foco(c, t, C["s15.d"] + 0.6, 0.4, lambda a: centro(c, "oleico", 500, 1010, 56, "g", TINTA, a))
        graxo(c, t, C["s15.e"], 1420, 760, 80, False, n=5)
        E.foco(c, t, C["s15.e"] + 0.6, 0.4, lambda a: centro(c, "elaídico", 1420, 1010, 56, "g", TINTA, a))
    E.frase(c, t, C["s15.f"], ps("que isomeria?", "i", 60) + [("qual é a trans?", "g", 56, COR)], 1180, 290, passo=0.1)
    pausa(c, t, C, "s16", 1080, 760, 180)


def b_resposta4(c, t, C, b):
    E.frase(c, t, C["s17.a"], [("isomeria", "i", 80), ("cis e trans", "g", 76, COR)], W / 2, 200, "center", 0.12)
    graxo(c, t, -9, 480, 640, 80, True, n=5)
    graxo(c, t, -9, 1400, 640, 80, False, n=5)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: (centro(c, "cis: oleico", 480, 960, 60, "g", TINTA, a), centro(c, "do azeite", 480, 1030, 46, "i", TINTA2, a)))
    E.foco(c, t, C["s17.c"], 0.4, lambda a: centro(c, "trans: elaídico", 1400, 960, 60, "g", COR, a))
    E.foco(c, t, C["s17.d"], 0.4, lambda a: E.pilula(c, "gordura trans", 1400, 1035, 46, "g", fundo=E.COR, a=a))


# ---------------- 5: carbono quiral no ibuprofeno ----------------
IX, IY = 1000, 640


def b_questao5(c, t, C, b):
    situacao(c, t, C["s18.a"], 5)
    E.frase(c, t, C["s18.b"], [("ibuprofeno", "g", 70)] + ps("remédio para dor", "i", 60, TINTA2), XE + 360, 165, passo=0.1)
    if t < C["s19"]:
        ibuprofeno(c, t, C["s18.b"], IX, IY)
    E.frase(c, t, C["s18.c"], [("1", "g", 56, COR)] + ps("quantos carbonos quirais?", "i", 60), XE, 920, passo=0.1)
    E.frase(c, t, C["s18.d"], [("2", "g", 56, COR)] + ps("quantos isômeros ópticos?", "i", 60), XE, 1010, passo=0.1)
    pausa(c, t, C, "s19", W / 2, 500, 170)


def b_resposta5(c, t, C, b):
    P = ibuprofeno(c, t, None, IX, IY, cores={1: COR} if t >= C["s21.a"] else None)
    tR = C["s20.a"]
    if t >= tR:  # o anel e o carbono do COOH: ligação dupla
        for k in range(2):
            E.risco(c, IX - 90 + 0 * k, IY + 90 - 180 * k, IX + 90, IY - 90 + 180 * k, t, tR + 0.2 * k, largura=9)
        P3 = P[3]
        E.risco(c, P3[0] - 70, P3[1] + 30, P3[0] - 20, P3[1] - 30, t, tR + 0.6, largura=8)
    for k, i in enumerate((2, 5, 7, 8)):
        if t >= C["s20.b"] + 0.2 * k:
            w = _meia(("CH3", "CH2", "H3C", "H3C")[k], 62)[0]
            E.risco(c, P[i][0] - w, P[i][1] + 30, P[i][0] + w, P[i][1] - 30, t, C["s20.b"] + 0.2 * k, largura=8)
    if t >= C["s20.c"]:
        E.risco(c, P[6][0] - 40, P[6][1] + 30, P[6][0] + 40, P[6][1] - 30, t, C["s20.c"], largura=8)
    E.foco(c, t, C["s20.c"] + 0.4, 0.4, lambda a: E.pilula(c, "2 CH3 iguais", P[6][0], P[6][1] + 200, 44, "g", fundo=ERRADO, a=a))
    circ(c, t, C["s21.a"], P[1][0], P[1][1], 70, E.COR)
    E.foco(c, t, C["s21.a"] + 0.3, 0.4, lambda a: E.escreve(c, "*", P[1][0] + 40, P[1][1] - 40, 80, "g", COR, a))
    Q.formula_em(c, t, C["s21.b"], "H, CH3, COOH e o anel", XE, 200, 54)
    E.frase(c, t, C["s21.c"], [("1", "g", 60, COR), ("carbono quiral", "g", 58)], XE, 310, passo=0.12)
    E.formula_em(c, t, C["s21.d"] - 0.4, "2^1 =", 1500, 300, 90, "g", TINTA, "right")
    bola_txt(c, t, C["s21.d"], "2", 1600, 272, 62, 80, CERTO)
    E.foco(c, t, C["s21.d"] + 0.3, 0.4, lambda a: E.escreve(c, "isômeros", 1680, 300, 54, "i", TINTA, a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    E.frase(c, t, C["s22.a"], [("3", "g", 110, COR)] + ps("ou mais? módulo firme", "i", 76), XE, 280, passo=0.12)
    E.frase(c, t, C["s22.a"] + 1.6, ps("travou? reveja a aula da questão", "i", 60, TINTA2), XE, 390, passo=0.1)
    E.frase(c, t, C["s22.b"] - 0.8, [("próxima", "i", 76), ("aula", "i", 76)], XE, 560)
    E.frase(c, t, C["s22.b"], [("reação", "g", 100, COR), ("de", "i", 100), ("adição", "g", 100, COR)], XE, 690, passo=0.15)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "óleo → margarina", XE + 330, 820, 56, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s22.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s22.d"] + 0.2, 0.4))
    E.frase(c, t, C["s22.e"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, atalho=b_atalho, questao4=b_questao4,
              resposta4=b_resposta4, questao5=b_questao5, resposta5=b_resposta5, fim=b_fim)
