"""Visual — Estudativo · QUI-ORG-015: isomeria geométrica, cis e trans.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho de QUI-MIS-001 (turquesa, fórmulas só com Q.formula, palco só no atalho,
erro com risco ou selo). Complemento usado nas aulas QUI-ORG-015 a 028:
- ESTRUTURA PLANA: estr() / alceno() desta pasta, com rótulos químicos escritos por Q.formula (CH3, OH, COOH com índice de
  verdade), ligações em tinta e a dupla da vez na cor da matéria. Rótulo à esquerda de uma ligação sai invertido (H3C).
- O grupo que a fala explica fica em COR (cores={i: COR}); o par de ligantes que se compara ganha caixa pontilhada.
- ALCENO sempre na mesma pose: os dois carbonos da dupla na horizontal e os quatro ligantes a 120°, para que "mesmo lado"
  e "lados opostos" se leiam pela linha tracejada que passa pelo eixo da dupla.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Química Orgânica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-ORG-015_isomeria_cis_trans.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("giro", "cistrans", "regra", "atalho", "questao", "fim"))

# as fórmulas da aula, conferidas pela contagem do kit
assert Q.contar("CH3CHCHCH3") == Q.contar("C4H8") == {"C": 4, "H": 8}          # but-2-eno, cis e trans
assert Q.contar("CH2CHCH2CH3") == Q.contar("C4H8")                              # but-1-eno, o contraexemplo
assert Q.contar("CH3CHCHCH2CH3") == Q.contar("CH3C(CH3)CHCH3") == {"C": 5, "H": 10}  # pent-2-eno e 2-metilbut-2-eno


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
CIS = ("H3C", "H", "CH3", "H")
TRANS = ("H3C", "H", "H", "CH3")
MADEIRA = "#C9A26B"


def eixo(c, t, t0, cx, cy, w, escuro=False, rotulos=True, t1=None):
    """linha tracejada pelo eixo da dupla: separa os dois lados"""
    if t < t0 or (t1 is not None and t >= t1 + 0.4):
        return
    p = ease_out(prog(t, t0, 0.5)) * (1 - (ep(t, t1, 0.4) if t1 is not None else 0))
    vao = w * 0.17  # não passa por cima da dupla
    cr = CLARO if escuro else TINTA2
    M.line(c, cx - w / 2, cy, lerp(cx - w / 2, cx - vao, p), cy, cr, p, 3, dash=[14, 10])
    M.line(c, cx + vao, cy, lerp(cx + vao, cx + w / 2, p), cy, cr, p, 3, dash=[14, 10])


def tabua(c, cx, cy, L, ang, a=1.0):
    c.save(); c.rotate(ang, cx, cy)
    M.rrect(c, cx - L / 2, cy - 42, L, 84, 14, MADEIRA, a, shadow=True)
    for k in range(3):
        M.line(c, cx - L / 2 + 30, cy - 20 + 20 * k, cx + L / 2 - 30, cy - 18 + 20 * k, "#A97F48", 0.5 * a, 2)
    c.restore()


def prego(c, x, y, a=1.0):
    E.bola(c, x, y, 17, "#5A5F68", a)


def rotulo_nutri(c, x, y, a):
    """tabela nutricional de embalagem, com a linha da gordura trans"""
    if a <= 0:
        return
    M.rrect(c, x, y, 600, 400, 18, "#FFFFFF", a, shadow=True)
    E.escreve(c, "INFORMAÇÃO NUTRICIONAL", x + 36, y + 70, 36, "g", TINTA, a)
    M.line(c, x + 36, y + 96, x + 564, y + 96, TINTA, a, 5)
    for k, (s, v) in enumerate((("Gorduras totais", "8 g"), ("Gorduras saturadas", "3 g"), ("Gorduras trans", "0 g"))):
        yy = y + 170 + k * 82
        cr = COR if k == 2 else TINTA
        E.escreve(c, s, x + 36, yy, 40, "b", cr, a)
        E.escreve(c, v, x + 564 - E.larg(v, "b", 40), yy, 40, "b", cr, a)
        M.line(c, x + 36, yy + 26, x + 564, yy + 26, FIO, a, 2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1, c1, d1 = C["s01.a"], C["s01.b"], C["s01.c"], C["s01.d"]
    if t < C["s02"]:
        def um():
            E.frase(c, t, a1, [("gordura", "g", 150), ("trans", "g", 150, COR)], XE, 330, passo=0.3)
            E.frase(c, t, a1 + 1.4, ps("já viu no rótulo?", "i", 70, TINTA2), XE, 450, passo=0.12)
            E.saida(c, t, b1 + 0.6, lambda: E.foco(c, t, a1 + 0.8, 0.6, lambda a: rotulo_nutri(c, 1180, 230, a)))
            E.frase(c, t, b1, ps("o jeito de arrumar os átomos", "i", 66), XE, 640, passo=0.1)
            E.frase(c, t, b1 + 1.4, ps("em volta da", "i", 66) + [("dupla", "g", 62, COR)], XE, 740, passo=0.1)
            alceno(c, t, b1 + 0.8, 1480, 560, TRANS, 150, 80, cores={2: COR, 5: COR}, cor_dupla=E.COR)
        E.saida(c, t, c1 - 0.1, um)
        if t < c1:
            return
        E.frase(c, t, c1, ps("mesma fórmula, mesmas ligações", "i", 72), W / 2, 200, "center", 0.12)
        for k, (x, subs) in enumerate(((560, CIS), (1360, TRANS))):
            alceno(c, t, c1 + 0.4 + 0.6 * k, x, 540, subs, 140, 76, cores={2: COR, 4 + k: COR})
            Q.formula_em(c, t, c1 + 1.2 + 0.6 * k, "C4H8", x, 860, 90, align="center")
        E.foco(c, t, d1, 0.5, lambda a: centro(c, "≠", W / 2, 590, 160, "g", COR, a))
        pilula_em(c, t, d1 + 0.5, "2 substâncias diferentes", W / 2, 990, 54, E.COR)
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1550, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("quando", "i", 74), ("existe", "i", 74), ("cis", "g", 70, COR), ("e", "i", 74), ("trans", "g", 70, COR)]),
                 (C["s02.c"], [("o", "i", 74), ("cis", "g", 70), ("e", "i", 74), ("o", "i", 74), ("trans", "g", 70), ("do", "i", 74), ("but-2-eno", "g", 70)]),
                 (C["s02.d"], [("atalho", "g", 70, COR), ("de", "i", 74), ("prova", "i", 74)])], XE, 460, 170)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("lembre da isomeria plana", "i", 70, TINTA2), XE, 190, passo=0.12)
    E.frase(c, t, C["s03.a"], [("isômeros", "g", 130, COR)], XE, 350)
    E.frase(c, t, C["s03.a"] + 0.8, [("mesma", "i", 70), ("fórmula molecular,", "g", 62)], XE + 760, 300, passo=0.12)
    E.frase(c, t, C["s03.a"] + 1.8, [("estruturas", "g", 62), ("diferentes", "i", 70)], XE + 760, 390, passo=0.12)
    s = "CH3–CH=CH–CH3"
    fx, fy, fs = W / 2, 830, 120
    E.frase(c, t, C["s03.b"], [("but-2-eno", "g", 80, COR)], XE, 560)
    E.frase(c, t, C["s03.b"] + 0.6, ps("4 carbonos, dupla no carbono 2", "i", 60, TINTA2), XE + 480, 560, passo=0.1)
    Q.formula_em(c, t, C["s03.b"] + 0.8, s, fx, fy, fs, align="center", cores={"=": COR})
    cs = [g for g in Q.grupos(s, fx, fy, fs, "center") if g["s"] == "C"]
    for k, g in enumerate(cs):
        tk = C["s03.b"] + 1.4 + 0.25 * k
        E.foco(c, t, tk, 0.4, lambda a, g=g, k=k: (E.bola(c, g["x0"] + fs * 0.36, fy - fs - 40, 34, a=a),
                                                   centro(c, str(k + 1), g["x0"] + fs * 0.36, fy - fs - 25, 42, "g", E.SOBRE, a)))


# ---------------- giro: ligação simples gira, dupla não ----------------
def b_giro(c, t, C, b):
    px, py = 1380, 620
    if t < C["s05.b"]:
        def tabuas():
            E.frase(c, t, C["s04.a"], [("ligação", "i", 80), ("simples", "g", 80)], XE, 300, passo=0.15)
            E.frase(c, t, C["s04.a"] + 0.8, [("gira?", "g", 80, COR)], XE, 410)
            E.frase(c, t, C["s04.b"], ps("duas tábuas,", "i", 66, TINTA2), XE, 580, passo=0.12)
            E.frase(c, t, C["s04.b"] + 0.8, [("1", "g", 64, COR)] + ps("prego só", "i", 66, TINTA2), XE, 670, passo=0.12)
            gira = 38 * math.sin(max(0, t - C["s04.c"]) * 2.2) * ep(t, C["s04.c"], 0.4)
            dois = C["s05.a"]
            gira *= 1 - ep(t, dois, 0.6)
            E.foco(c, t, C["s04.b"], 0.5, lambda a: tabua(c, px, py, 620, 0, a))
            E.foco(c, t, C["s04.b"] + 0.4, 0.5, lambda a: tabua(c, px, py, 620, gira, a))
            E.foco(c, t, C["s04.b"] + 0.7, 0.3, lambda a: prego(c, px, py, a))
            if t >= dois:
                E.foco(c, t, dois, 0.3, lambda a: prego(c, px + 200, py, a))
                E.frase(c, t, dois, [("2", "g", 64, COR)] + ps("pregos: nada gira", "i", 66), XE, 800, passo=0.12)
                E.frase(c, t, dois + 1.4, [("ligação", "i", 70), ("dupla", "g", 70, COR)], XE, 920, passo=0.12)
        E.saida(c, t, C["s05.b"] - 0.1, tabuas)
        return
    E.frase(c, t, C["s05.b"], [("ligação", "i", 80), ("dupla", "g", 80, COR), ("não", "i", 80), ("gira", "g", 80)], XE, 250, passo=0.15)
    alceno(c, t, C["s05.b"] + 0.4, W / 2, 640, ("?", "?", "?", "?"), 170, 90, tl=[C["s05.b"] + 0.4, C["s05.b"] + 0.5] + [C["s05.c"] + 0.15 * k for k in range(4)],
           cor_dupla=E.COR)
    pilula_em(c, t, C["s05.b"] + 1.0, "travados", W / 2, 420, 48, E.COR)
    eixo(c, t, C["s05.c"] + 0.6, W / 2, 640, 1000)
    E.foco(c, t, C["s05.c"] + 1.0, 0.4, lambda a: (E.escreve(c, "um lado", W / 2 + 520, 470, 50, "i", TINTA2, a),
                                                     E.escreve(c, "o outro lado", W / 2 + 520, 840, 50, "i", TINTA2, a)))


# ---------------- cis e trans ----------------
def b_cistrans(c, t, C, b):
    if t < C["s07"]:
        def s06():
            Q.formula_em(c, t, C["s06.a"], "CH3–CH=CH–CH3", W / 2, 220, 100, align="center", cores={"=": COR})
            P = alceno(c, t, C["s06.a"] + 0.8, W / 2, 640, CIS, 170, 90, cores={2: COR, 3: COR} if t >= C["s06.c"] else None)
            caixa(c, t, C["s06.b"], P[2][0] - 110, P[2][1] - 70, 220, 520 - 140 + 140, E.COR)
            pilula_em(c, t, C["s06.b"] + 0.4, "2 ligantes", P[2][0] - 340, P[0][1], 50, E.COR)
            wf = E.frase(c, t, C["s06.c"], [("1", "g", 60, COR), ("H", "g", 60), ("e", "i", 64), ("1", "g", 60, COR)], XE, 1000, passo=0.12)
            Q.formula_em(c, t, C["s06.c"] + 0.6, "CH3", XE + wf + 16, 1000, 60)
            E.frase(c, t, C["s06.c"] + 0.6, ps("em cada carbono da dupla", "i", 60, TINTA2), XE + wf + 180, 1000, passo=0.1)
        E.saida(c, t, C["s07"] - 0.1, s06)
        return
    y0 = 520
    for k, (x, subs, nome, sig, tk, tn) in enumerate(((520, CIS, "cis", "deste lado", "s07.a", "s07.b"),
                                                       (1400, TRANS, "trans", "do outro lado", "s07.c", "s07.d"))):
        alceno(c, t, C[tk], x, y0, subs, 140, 76, cores={2: COR, 4 + k: COR})
        eixo(c, t, C[tk] + 0.8, x, y0, 640)
        E.foco(c, t, C[tn], 0.5, lambda a, x=x, nome=nome: centro(c, nome, x, 830, 130, "g", COR, a))
        E.foco(c, t, C[tn] + 0.5, 0.4, lambda a, x=x, sig=sig: centro(c, "= " + sig, x, 910, 60, "i", TINTA2, a))
    # s08: não gira sem quebrar; mesma fórmula; pontos de ebulição
    if t < C["s08"]:
        return

    def giro():
        p = ep(t, C["s08.a"], 0.6)
        if p > 0:
            pth = skia.Path(); pth.moveTo(780, 300); pth.quadTo(W / 2, 170, 1140, 300)
            m = skia.PathMeasure(pth, False)
            seg = skia.Path(); m.getSegment(0, m.getLength() * p, seg, True)
            c.drawPath(seg, M.paint(TINTA2, 1, stroke=6))
            if p >= 1:
                Q.seta_reacao(c, 1100, 1150, 320, 60, TINTA2)
        E.foco(c, t, C["s08.a"] + 0.4, 0.4, lambda a: centro(c, "girar?", W / 2, 165, 56, "g", TINTA2, a))
        if t >= C["s08.a"] + 1.4:
            E.risco(c, W / 2 - 110, 190, W / 2 + 110, 120, t, C["s08.a"] + 1.4, largura=9)
    E.saida(c, t, C["s08.b"] - 0.1, giro)
    pilula_em(c, t, C["s08.b"], "2 substâncias", W / 2, 240, 54, E.COR)
    if t >= C["s08.c"]:
        def formulas():
            for x in (520, 1400):
                Q.formula_em(c, t, C["s08.c"], "C4H8", x, 1030, 70, align="center")
        E.saida(c, t, C["s08.d"] - 0.1, formulas)
    for x, s, tk in ((520, "ferve a 4 °C", "s08.d"), (1400, "ferve a 1 °C", "s08.e")):
        E.foco(c, t, C[tk], 0.5, lambda a, x=x, s=s: E.pilula(c, s, x, 1005, 48, "g", fundo=TINTA, a=a))


# ---------------- regra ----------------
def b_regra(c, t, C, b):
    E.frase(c, t, C["s09"], ps("quando existe", "i", 76) + [("cis e trans?", "g", 72, COR)], XE, 180, passo=0.12)
    lista(c, t, [(C["s09.a"], [("dupla", "g", 64, COR)] + ps("entre carbonos", "i", 68)),
                 (C["s09.b"], ps("cada carbono da dupla com", "i", 68) + [("2 ligantes diferentes", "g", 62, COR)])], XE, 330, 120)
    cx, cy = 980, 780
    P = alceno(c, t, C["s10"], cx, cy, TRANS, 150, 80)
    for k, (i, j, tk) in enumerate(((2, 3, "s10.a"), (4, 5, "s10.b"))):
        A, B_ = P[i], P[j]
        caixa(c, t, C[tk], min(A[0], B_[0]) - 110, A[1] - 60, 220, B_[1] - A[1] + 120, E.COR)
        xs = A[0] - 330 if k == 0 else A[0] + 330
        E.foco(c, t, C[tk] + 0.4, 0.4, lambda a, xs=xs, k=k: (centro(c, f"C{k + 2}", xs, cy - 40, 60, "g", COR, a),
                                                               Q.formula(c, "H ≠ CH3", xs, cy + 50, 54, TINTA, a, "center")))
    x_em(c, t, C["s10.c"], 760, 1030, 40, True)
    E.frase(c, t, C["s10.c"] + 0.3, ps("tem cis e trans", "g", 52, COR), 820, 1048, passo=0.1)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s11"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s11.a"], ps("toda dupla tem", "i", 70) + [("cis e trans?", "g", 64)], XE + 450, 190, passo=0.12)
    if t < C["s12"]:
        E.frase(c, t, C["s11.b"], [("but-1-eno", "g", 80, COR)], W / 2, 420, "center")
        Q.formula_em(c, t, C["s11.b"] + 0.4, "CH2=CH–CH2–CH3", W / 2, 640, 120, align="center", cores={"=": COR})
        return
    # o carbono 1 tem dois H: trocar um pelo outro não muda nada
    cx, cy, es = W / 2 - 80, 640, 160
    u = ease_io(prog(t, C["s12.b"] + 0.3, 1.4))
    s_ = math.sin(math.pi * u)
    ha = (-1.25 - 0.8 * s_, -0.95 * math.cos(math.pi * u))
    hb = (-1.25 - 0.3 * s_, 0.95 * math.cos(math.pi * u))
    move = 0 < u < 1
    at = [("C", -0.62, 0), ("C", 0.62, 0), ("H", *ha), ("H", *hb), ("H", 1.25, -0.95), ("CH2–CH3", 1.55, 0.95)]
    ligs = [(0, 1, 2, E.COR), (0, 2, 0 if move else 1), (0, 3, 0 if move else 1), (1, 4, 1), (1, 5, 1)]
    E.foco(c, t, C["s12"], 0.4, lambda a: estr(c, t, None, at, ligs, cx, cy, es, 84, cores={2: COR}, a=a))
    E.foco(c, t, C["s12.a"], 0.4, lambda a: centro(c, "C1", cx - 0.62 * es, cy - 90, 50, "g", COR, a))
    caixa(c, t, C["s12.a"] + 0.2, cx - 1.25 * es - 70, cy - 0.95 * es - 70, 140, 1.9 * es + 140, E.COR, t1=C["s12.b"] + 0.2)
    E.foco(c, t, C["s12.a"] + 0.4, 0.4, lambda a: E.pilula(c, "2 H iguais", cx - 1.25 * es - 260, cy, 46, "g", fundo=E.COR, a=a))
    E.frase(c, t, C["s12.c"], ps("continua", "i", 72) + [("igual", "g", 70, COR)], 1380, 470, passo=0.12)
    x_em(c, t, C["s12.d"], 1420, 640, 46, False)
    E.frase(c, t, C["s12.d"] + 0.3, ps("sem cis e trans", "g", 50), 1480, 658, passo=0.1)
    E.frase(c, t, C["s12.d"] + 1.0, ps("um carbono da dupla com", "i", 60, TINTA2) + [("2 ligantes iguais", "g", 56, ERRADO)] + ps("basta", "i", 60, TINTA2),
            W / 2, 990, "center", 0.1)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s14"]:
        def s13():
            E.frase(c, t, C["s13"], ps("o atalho de prova", "i", 72, CLARO), W / 2, 150, "center", 0.12)
            E.frase(c, t, C["s13.a"], [("1", "g", 62, CLARO)] + ps("olhe", "i", 70, CLARO) + [("um carbono", "g", 64, BR)] + ps("da dupla por vez", "i", 70, CLARO), XE, 290, passo=0.1)
            E.frase(c, t, C["s13.b"], [("2", "g", 62, CLARO)] + ps("dois ligantes", "i", 70, CLARO) + [("iguais?", "g", 64, BR), ("pare", "g", 64, ERRADO)], XE, 400, passo=0.1)
            cx, cy = W / 2, 690
            P = alceno(c, t, C["s13.a"] + 0.6, cx, cy, ("H", "H", "H", "CH2–CH3"), 140, 76, escuro=True, cor_dupla=E.CLARO)
            circ(c, t, C["s13.b"] + 0.4, P[2][0] - 10, (P[2][1] + P[3][1]) / 2, 175, E.CLARO)
            x_em(c, t, C["s13.c"], 340, cy - 40, 50, False)
            E.foco(c, t, C["s13.c"] + 0.2, 0.4, lambda a: centro(c, "não tem cis e trans", 340, cy + 70, 44, "g", BR, a))
            E.frase(c, t, C["s13.d"], ps("trocar dois iguais", "i", 66, CLARO) + [("não muda nada", "g", 62, BR)], W / 2, 990, "center", 0.12)
        E.saida(c, t, C["s14"] - 0.1, s13)
        return
    E.frase(c, t, C["s14.a"], ps("compare o", "i", 72, CLARO) + [("grupo inteiro", "g", 68, BR)], W / 2, 280, "center", 0.12)
    E.frase(c, t, C["s14.a"] + 1.4, ps("não só o primeiro átomo", "i", 60, CLARO), W / 2, 380, "center", 0.1)
    Q.formula_em(c, t, C["s14.b"], "CH3", 560, 660, 160, align="center", cores={"C": E.CLARO}, escuro=True)
    Q.formula_em(c, t, C["s14.b"] + 0.6, "CH2–CH3", 1360, 660, 160, align="center", cores={0: E.CLARO}, escuro=True)
    E.foco(c, t, C["s14.c"], 0.5, lambda a: centro(c, "≠", 860, 640, 170, "g", E.CLARO, a))
    pilula_em(c, t, C["s14.c"] + 0.5, "grupos diferentes", W / 2, 880, 56, E.COR)


# ---------------- questão ----------------
PENT = ("H3C", "H", "H", "CH2–CH3")
METIL = ("H3C", "H3C", "H", "CH3")
QY = 560


def b_questao(c, t, C, b):
    E.frase(c, t, C["s15"], ps("hora de testar", "i", 72, COR), XE, 170)
    E.frase(c, t, C["s15.a"], ps("qual tem", "i", 70) + [("cis e trans?", "g", 66, COR)], XE + 520, 170, passo=0.12)
    alceno(c, t, C["s15.b"], 480, QY, PENT, 130, 70)
    E.frase(c, t, C["s15.b"] + 0.5, [("pent-2-eno", "g", 66)], 480, 820, "center")
    alceno(c, t, C["s15.c"], 1440, QY, METIL, 130, 70)
    E.frase(c, t, C["s15.c"] + 0.5, [("2-metilbut-2-eno", "g", 66)], 1440, 820, "center")
    E.frase(c, t, C["s15.d"], ps("no que tiver:", "i", 64, TINTA2) + [("como fica o cis?", "g", 60)], W / 2, 980, "center", 0.12)
    if t >= C["s16"]:
        E.relogio(c, t, C["s16.a"], cx=W / 2, cy=QY - 20, r=120)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    E.frase(c, t, C["s17"], ps("resolvendo", "i", 72, COR), XE, 170)
    # o 2-metilbut-2-eno: dois CH3 no carbono 2
    P = alceno(c, t, C["s17"], 1440, QY, METIL, 130, 70, cores={2: COR, 3: COR} if t >= C["s17.a"] else None)
    centro(c, "2-metilbut-2-eno", 1440, 820, 60, "g", TINTA, ep(t, C["s17"], 0.4))
    caixa(c, t, C["s17.a"], P[2][0] - 100, P[2][1] - 60, 200, P[3][1] - P[2][1] + 120, E.COR)
    E.foco(c, t, C["s17.b"], 0.4, lambda a: E.pilula(c, "iguais", P[2][0] - 210, QY, 44, "g", fundo=E.COR, a=a))
    x_em(c, t, C["s17.c"], 1440, 940, 46, False)
    E.foco(c, t, C["s17.c"] + 0.2, 0.4, lambda a: E.escreve(c, "não tem", 1500, 958, 50, "g", TINTA, a))
    # o pent-2-eno: ligantes diferentes nos dois carbonos; vira o cis
    cis = ep(t, C["s18.d"], 0.6)
    if cis < 1:
        def pent():
            Q_ = alceno(c, t, C["s17"], 480, QY, PENT, 130, 70, cores={2: COR} if t >= C["s18.a"] else None)
            caixa(c, t, C["s18.a"], Q_[2][0] - 100, Q_[2][1] - 60, 200, Q_[3][1] - Q_[2][1] + 120, E.COR)
            caixa(c, t, C["s18.b"], Q_[4][0] - 100, Q_[4][1] - 60, 260, Q_[5][1] - Q_[4][1] + 120, E.COR)
        E.saida(c, t, C["s18.d"], pent)
    if t >= C["s18.d"]:
        E.foco(c, t, C["s18.d"] + 0.2, 0.5, lambda a: (alceno(c, t, None, 480, QY, ("H3C", "H", "CH2–CH3", "H"), 130, 70, cores={2: COR, 4: COR}, a=a)))
        eixo(c, t, C["s18.d"] + 0.6, 480, QY, 620)
        E.foco(c, t, C["s18.d"] + 0.8, 0.4, lambda a: E.pilula(c, "mesmo lado", 480, QY - 230, 44, "g", fundo=E.COR, a=a))
    nome = "cis-pent-2-eno" if t >= C["s18.d"] else "pent-2-eno"
    centro(c, nome, 480, 820, 60, "g", COR if t >= C["s18.d"] else TINTA, ep(t, C["s17"], 0.4))
    x_em(c, t, C["s18.c"], 420, 940, 46, True)
    E.foco(c, t, C["s18.c"] + 0.2, 0.4, lambda a: E.escreve(c, "tem cis e trans", 480, 958, 50, "g", TINTA, a))


# ---------------- fechamento ----------------
def quiral(c, t, t0, cx, cy, esc, espelha=False, escuro=False):
    """CHFClBr: carbono com quatro ligantes diferentes, em bola-vareta"""
    s = -1 if espelha else 1
    mol = dict(atomos=[("C", 0, 0), ("H", 0, -1.05), ("F", s * -0.95, 0.4), ("Cl", s * 0.95, 0.4), ("Br", s * 0.32, 1.0)],
               ligacoes=[(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)])
    return Q.molecula(c, t, t0, mol, cx, cy, esc, passo=0.12, escuro=escuro)


def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s19"], [("resumindo", "i", 92, COR)], XE, 170)
        itens = (("s19.a", [("a", "i", 70), ("dupla", "g", 66), ("não", "i", 70), ("gira", "i", 70)]),
                 ("s19.b", [("cada", "i", 70), ("carbono", "i", 70), ("dela:", "i", 70), ("2 ligantes diferentes", "g", 62)]),
                 ("s19.c", [("cis", "g", 66, COR), ("=", "g", 66, TINTA2), ("mesmo", "i", 70), ("lado", "i", 70)]),
                 ("s19.d", [("trans", "g", 66, COR), ("=", "g", 66, TINTA2), ("lados", "i", 70), ("opostos", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 320 + i * 150
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, XE + 40, y - 26, 46, a=a), centro(c, str(i + 1), XE + 40, y - 4, 56, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, XE + 120, y, passo=0.12)
        alceno(c, t, C["s19.d"] + 0.4, 1600, 700, TRANS, 110, 60, cores={2: COR, 5: COR})
        E.foco(c, t, C["s19.e"], 0.5, lambda a: E.pilula(c, "gordura trans", 1600, 960, 56, "g", fundo=E.COR, a=a))
    E.saida(c, t, C["s20"] - 0.1, resumo)
    if t < C["s20"]:
        return
    E.frase(c, t, C["s20"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 220)
    E.frase(c, t, C["s20.a"], [("carbono", "g", 110, COR), ("quiral", "g", 110, COR)], XE, 360)
    quiral(c, t, C["s20.b"], 440, 700, 130)
    E.foco(c, t, C["s20.b"] + 0.3, 0.5, lambda a: espelho(c, 700, 520, 900, a))
    quiral(c, t, C["s20.b"] + 0.6, 960, 700, 130, espelha=True)
    E.foco(c, t, C["s20.b"] + 1.2, 0.4, lambda a: centro(c, "imagem no espelho", 700, 990, 50, "i", TINTA2, a))
    E.foco(c, t, C["s20.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 470, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s20.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(770, 495, p), ep(t, C["s20.c"] + 0.2, 0.4))
    E.frase(c, t, C["s20.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, giro=b_giro, cistrans=b_cistrans, regra=b_regra, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
