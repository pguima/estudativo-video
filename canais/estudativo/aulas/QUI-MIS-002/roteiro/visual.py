"""Visual — Estudativo · QUI-MIS-002: substância pura ou mistura.

Segue a LINGUAGEM VISUAL DA QUÍMICA do cabeçalho de QUI-MIS-001/roteiro/visual.py (fórmula com Q.formula, átomo na cor do
elemento, erro com risco ou selo, palco só no atalho). Nesta trilha (Matéria e Misturas), três convenções a mais:
- LENTE = olhar as partículas de um material: círculo com aro grosso e cabo (lente), conteúdo recortado dentro.
- COPO EM CAMADAS = sistema com fases (copo_camadas): cada fase é uma faixa; água incolor (Q.AGUA), óleo âmbar (OLEO),
  areia em grãos (AREIA). O número da fase vai numa bolinha escura à direita da faixa.
- Classificação: substância e simples/composta em TINTA; mistura e homogênea/heterogênea na cor da matéria.
Peças desta aula candidatas ao kit: copo_camadas, lente, garrafa, decisao (fluxo de duas perguntas).
Todo instante vem de C[...] (marcadores do roteiro)."""
import math
import random

import editorial as E
import quimica as Q
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Química", "Matéria e Misturas")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_QUI-MIS-002_substancia_pura_ou_mistura.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("pura", "simples", "fases", "alotropia", "atalho", "questao", "fim"))
BR = "#FFFFFF"
OLEO = "#E8B23A"
AREIA = "#C99A5B"

# as contagens da aula, conferidas pelo kit
assert len(Q.contar("O2")) == 1 and len(Q.contar("H2")) == 1 and len(Q.contar("O3")) == 1
assert len(Q.contar("H2O")) == 2 and len(Q.contar("CO2")) == 2
assert Q.contar("O2") == {"O": 2} and Q.contar("O3") == {"O": 3}
FASES_Q, COMPONENTES_Q = 3, 4  # água+sal / óleo / areia; água, sal, óleo, areia
assert len(["água com sal", "óleo", "areia"]) == FASES_Q and len(["água", "sal", "óleo", "areia"]) == COMPONENTES_Q


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", E.SOBRE, a, "center")))


def pilula_em(c, t, t0, s, cx, cy, size, fundo=None, est="g", cor=BR):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, cx, cy, size, est, fundo=fundo, a=a, cor=cor))


def lista(c, t, itens, x, y0, dy, r=44):
    for i, (ti, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, ti, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 40, y - 26, r, a=a), centro(c, str(i + 1), x + 40, y - 4, 54, "g", E.SOBRE, a)))
        E.frase(c, t, ti + 0.1, partes, x + 110, y, passo=0.12)


def num(c, t, t0, n, cx, cy, r=34, cor=TINTA):
    E.foco(c, t, t0, 0.3, lambda a: (E.bola(c, cx, cy, r, cor, a), centro(c, str(n), cx, cy + r * 0.45, r * 1.25, "g", BR, a)))


def caixa_em(c, t, t0, x, y, w, h, cor=None, t1=None):
    if t < t0 or (t1 is not None and t >= t1):
        return
    p = ep(t, t0, 0.4)
    E.caixa_pontilhada(c, x, y, w, h, p, cor, prog_=p)


def copo_camadas(c, t, t0, cx, yb, w, h, camadas, a=1.0):
    """copo com fases empilhadas de baixo para cima: camadas = [(tipo, fração da altura, instante)], tipo = cor ou
    "areia"; instante None = já no copo. Devolve [(y_topo, y_base)] de cada camada, para rótulos."""
    if t < t0 or a <= 0:
        return []
    q = ep(t, t0, 0.5) * a
    contorno, dentro, (yt, yb_) = Q._copo_path("bequer", cx, yb, w, h)
    c.drawPath(dentro, M.paint(BR, 0.45 * q))
    c.save()
    c.clipPath(dentro, skia.ClipOp.kIntersect, True)
    y, faixas = yb_, []
    for k, (tipo, f, ti) in enumerate(camadas):
        hh = (yb_ - yt) * f * (ease_io(prog(t, ti, 0.9)) if ti is not None else 1.0)
        if hh <= 0.5:
            faixas.append((y, y))
            continue
        r = skia.Rect.MakeLTRB(cx - w, y - hh, cx + w, y + 1)
        if tipo == "areia":
            c.drawRect(r, M.paint(AREIA, 0.95 * q))
            rnd = random.Random(7 + k)
            for _ in range(int(w * hh / 260)):
                gx, gy = cx - w / 2 + rnd.random() * w, y - rnd.random() * hh
                c.drawCircle(gx, gy, 2.5 + 2.5 * rnd.random(), M.paint("#8E6A38" if rnd.random() < 0.5 else "#E2C08A", 0.9 * q))
        else:
            pt = skia.Paint(AntiAlias=True)
            pt.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y - hh), skia.Point(0, y)],
                                                        [M.hexc(M.mix(tipo, BR, 0.15), 0.92 * q), M.hexc(M.mix(tipo, "#000000", 0.1), 0.95 * q)]))
            c.drawRect(r, pt)
            M.line(c, cx - w, y - hh, cx + w, y - hh, M.mix(tipo, BR, 0.5), q, 4)
        faixas.append((y - hh, y))
        y -= hh
    c.restore()
    pv = M.paint(Q.VIDRO, q, stroke=5)
    pv.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(contorno, pv)
    M.line(c, cx - w * 0.36, yt + h * 0.18, cx - w * 0.36, yt + h * 0.55, BR, 0.7 * q, max(4, w * 0.03))
    return faixas


def graos_sal(c, t, t0, t_some, cx, y0, y1, n=14, w=120, semente=3):
    """grãos de sal caindo no copo e sumindo (dissolvendo) a partir de t_some"""
    rnd = random.Random(semente)
    for i in range(n):
        ti = t0 + i * 0.06
        if t < ti:
            continue
        u = ease_io(prog(t, ti, 0.8))
        x = cx + (rnd.random() - 0.5) * w
        y = lerp(y0, y1 + rnd.random() * 60, u)
        s = 11 * (1 - ep(t, t_some + rnd.random() * 0.8, 0.6))
        if s > 0.5:
            c.save(); c.translate(x, y); c.rotate(rnd.random() * 90)
            c.drawRect(skia.Rect.MakeXYWH(-s / 2, -s / 2, s, s), M.paint(BR, 1))
            c.drawRect(skia.Rect.MakeXYWH(-s / 2, -s / 2, s, s), M.paint(CINZA, 1, stroke=2))
            c.restore()


def lente(c, cx, cy, r, fn, a=1.0, cabo=True):
    """lente de aumento: o que fn() desenha aparece recortado dentro do círculo"""
    if a <= 0:
        return
    if cabo:
        ang = math.radians(42)
        x0, y0 = cx + r * math.cos(ang), cy + r * math.sin(ang)
        M.line(c, x0, y0, x0 + 150 * math.cos(ang), y0 + 150 * math.sin(ang), "#2A2B31", a, 34)
    c.drawCircle(cx, cy, r, M.paint(BR, 0.92 * a))
    c.save()
    pth = skia.Path(); pth.addCircle(cx, cy, r - 8)
    c.clipPath(pth, skia.ClipOp.kIntersect, True)
    fn()
    c.restore()
    c.drawCircle(cx, cy, r, M.paint("#2A2B31", a, stroke=16))
    c.drawCircle(cx, cy, r - 12, M.paint(BR, 0.5 * a, stroke=4))


def garrafa(c, cx, yb, w, h, a=1.0, nivel=0.8, rotulo=None):
    """garrafa de água: corpo arredondado, gargalo, tampa azul e rótulo"""
    if a <= 0:
        return
    corpo = skia.Path()
    x0, x1, yt = cx - w / 2, cx + w / 2, yb - h
    gw, gh = w * 0.34, h * 0.16
    corpo.moveTo(cx - gw / 2, yt + gh * 0.4)
    corpo.lineTo(cx - gw / 2, yt + gh)
    corpo.cubicTo(x0, yt + gh * 1.6, x0, yt + gh * 2.2, x0, yt + gh * 2.6)
    corpo.lineTo(x0, yb - 30); corpo.quadTo(x0, yb, x0 + 30, yb); corpo.lineTo(x1 - 30, yb); corpo.quadTo(x1, yb, x1, yb - 30)
    corpo.lineTo(x1, yt + gh * 2.6)
    corpo.cubicTo(x1, yt + gh * 2.2, x1, yt + gh * 1.6, cx + gw / 2, yt + gh)
    corpo.lineTo(cx + gw / 2, yt + gh * 0.4); corpo.close()
    c.drawPath(corpo, M.paint("#EAF4F8", 0.85 * a))
    c.save(); c.clipPath(corpo, skia.ClipOp.kIntersect, True)
    yl = yb - (h - gh) * nivel
    c.drawRect(skia.Rect.MakeLTRB(x0, yl, x1, yb), M.paint(Q.AGUA, 0.9 * a))
    c.restore()
    c.drawPath(corpo, M.paint(Q.VIDRO, a, stroke=5))
    M.rrect(c, cx - gw / 2 - 8, yt - 10, gw + 16, gh * 0.55, 10, "#1F6FEB", a)
    if rotulo:
        M.rrect(c, x0 - 2, yb - h * 0.55, w + 4, h * 0.26, 6, E.COR, a)
        for i, s in enumerate(rotulo):
            centro(c, s, cx, yb - h * 0.55 + h * 0.1 + i * h * 0.1, h * 0.075, "g" if i == 0 else "i", BR, a)
    M.line(c, x0 + w * 0.16, yt + gh * 2.8, x0 + w * 0.16, yb - h * 0.6, BR, 0.7 * a, 8)


def agua_mol(c, cx, cy, s, giro, a=1.0):
    Q.molecula_desenho(c, "H2O", cx, cy, s, a, giro=giro, rotulos=False)


AGUAS = [(-150, -130, 20), (40, -170, 200), (170, -40, 80), (-90, 60, 300), (80, 170, 150), (-200, 110, 250), (190, 120, 330), (-20, -40, 120)]


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def um():
        E.foco(c, t, C["s01"], 0.6, lambda a: garrafa(c, 560, 960, 330, 720, a, 0.78, ("água mineral", "natural")))
        E.frase(c, t, C["s01.a"] + 0.2, ps("no rótulo:", "i", 70, TINTA2), 960, 300, passo=0.12)
        E.frase(c, t, C["s01.a"] + 0.8, [("pura?", "g", 190)], 960, 500)
        if t >= C["s01.b"]:
            E.risco(c, 950, 470, 1520, 380, t, C["s01.b"], largura=12)
        E.frase(c, t, C["s01.b"] + 0.3, ps("para a Química, é", "i", 70), 960, 680, passo=0.12)
        E.frase(c, t, C["s01.b"] + 1.2, [("mistura", "g", 170, COR)], 960, 870)
        E.frase(c, t, C["s01.c"], [("por quê?", "i", 90, TINTA2)], 1560, 1010, "center")
    E.saida(c, t, C["s02"] - 0.1, um)
    if t < C["s02"]:
        return
    tb = C["s02.a"] + 0.4
    E.foco(c, t, tb, 0.8, lambda a: E.simbolo(c, 1540, 560, 280 * ease_back(prog(t, tb, 0.8)), giro=8 * math.sin(t * 0.4)), blur=0)
    E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 88), XE, 280, passo=0.14)
    lista(c, t, [(C["s02.b"], [("substância", "g", 70), ("ou", "i", 74), ("mistura", "g", 70, COR)]),
                 (C["s02.c"], [("contar", "g", 70), ("as", "i", 74), ("fases", "g", 70, COR)]),
                 (C["s02.d"], [("alótropos", "g", 70, COR)])], XE, 460, 170)
    Q.formula_em(c, t, C["s02.d"] + 0.5, "O2", XE + 560, 800, 84)
    Q.formula_em(c, t, C["s02.d"] + 0.7, "O3", XE + 760, 800, 84)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"], ps("da aula passada", "i", 80, TINTA2), XE, 220, passo=0.12)
    E.frase(c, t, C["s03.a"], [("elemento", "g", 96, COR), ("=", "g", 96, TINTA2)] + ps("tipo de átomo", "i", 96), XE, 420, passo=0.14)
    for k, el in enumerate(("H", "O", "C")):
        Q.atomo_em(c, t, C["s03.a"] + 1.0 + 0.2 * k, 1350 + 160 * k, 390, 62, el)
    E.frase(c, t, C["s03.b"], [("fórmula", "g", 96, COR), ("=", "g", 96, TINTA2)] + ps("quais e quantos", "i", 96), XE, 640, passo=0.14)
    Q.formula_em(c, t, C["s03.b"] + 1.2, "H2O", XE, 900, 200, cores={"indice": E.COR})
    E.foco(c, t, C["s03.b"] + 1.8, 0.4, lambda a: E.escreve(c, "2 hidrogênios, 1 oxigênio", XE + 470, 880, 60, "i", TINTA2, a))


# ---------------- substância pura × mistura ----------------
def b_pura(c, t, C, b):
    def s04_05():
        E.frase(c, t, C["s04"] + 0.2, ps("olhe com uma lupa", "i", 76, TINTA2), XE, 200, passo=0.12)
        E.frase(c, t, C["s04.a"], [("água", "g", 90), ("destilada", "g", 90, COR)], XE, 340, passo=0.14)
        E.frase(c, t, C["s04.a"] + 1.4, ps("toda molécula é igual", "i", 70), XE, 450, passo=0.12)
        rr = 330 * ease_back(prog(t, C["s04.a"], 0.7))
        if rr > 5:
            def dentro():
                for k, (dx, dy, g) in enumerate(AGUAS):
                    q = ep(t, C["s04.b"] + 0.18 * k, 0.4)
                    if q > 0:
                        agua_mol(c, 1400 + dx + 6 * math.sin(t * 1.3 + k), 560 + dy + 6 * math.cos(t * 1.1 + k), 90, g + 20 * math.sin(t * 0.6 + k), q)
            lente(c, 1400, 560, rr, dentro, 1.0)
        for k in range(3):
            Q.formula_em(c, t, C["s04.b"] + 0.5 * k, "H2O", XE + 330 * k, 640, 90)
        E.frase(c, t, C["s05.a"], ps("um tipo só de partícula:", "i", 66), XE, 820, passo=0.1)
        E.frase(c, t, C["s05.a"] + 1.0, [("substância", "g", 96), ("pura", "g", 96, COR)], XE, 950, passo=0.14)
        pilula_em(c, t, C["s05.b"], "uma fórmula só", 1400, 1000, 50, TINTA)
    E.saida(c, t, C["s06"] - 0.1, s04_05)
    if C["s06"] <= t < C["s07"]:
        def s06():
            E.frase(c, t, C["s06.a"], [("água", "g", 90), ("mineral", "g", 90, COR)], XE, 260, passo=0.14)
            E.frase(c, t, C["s06.b"], ps("+ sais dissolvidos", "i", 70), XE, 370, passo=0.12)
            ions = [("Na", -110, 170), ("Ca", 90, -90), ("Mg", 30, 100), ("Cl", 220, 30), ("Na", -210, -40)]

            def dentro():
                for k, (dx, dy, g) in enumerate(AGUAS):
                    agua_mol(c, 1400 + dx + 6 * math.sin(t * 1.3 + k), 560 + dy + 6 * math.cos(t * 1.1 + k), 90, g + 20 * math.sin(t * 0.6 + k))
                for k, (el, dx, dy) in enumerate(ions):
                    Q.atomo_em(c, t, C["s06.b"] + 0.2 * k, 1400 + dx + 5 * math.cos(t + k), 560 + dy, 40, el)
            E.foco(c, t, C["s06"], 0.4, lambda a: lente(c, 1400, 560, 330, dentro, a))
            E.frase(c, t, C["s06.c"], ps("dois ou mais tipos:", "i", 66), XE, 560, passo=0.1)
            E.frase(c, t, C["s06.c"] + 0.9, [("mistura", "g", 130, COR)], XE, 710)
            E.frase(c, t, C["s06.d"], [("componente", "g", 62), ("=", "g", 62, TINTA2)] + ps("cada substância dela", "i", 62), XE, 870, passo=0.1)
            pilula_em(c, t, C["s06.d"] + 1.2, "água", XE + 110, 960, 50, TINTA)
            pilula_em(c, t, C["s06.d"] + 1.4, "sais", XE + 330, 960, 50, TINTA)
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    E.frase(c, t, C["s07.a"], [("puro", "g", 96), ("no rótulo", "i", 90)], XE, 330, passo=0.14)
    E.foco(c, t, C["s07.a"] + 0.6, 0.4, lambda a: centro(c, "≠", XE + 320, 470, 120, "g", ERRADO, a))
    E.frase(c, t, C["s07.a"] + 0.9, [("puro", "g", 96, COR), ("na Química", "i", 90)], XE, 610, passo=0.14)
    E.frase(c, t, C["s07"] + 2.0, [("=", "g", 60, TINTA2)] + ps("nada foi acrescentado", "i", 60, TINTA2), XE, 730, passo=0.1)
    E.foco(c, t, C["s07.b"], 0.5, lambda a: Q.bequer(c, t, C["s07.b"], 1450, 900, 330, 420, 0.75, "#F59A23", graduacao=False))
    E.foco(c, t, C["s07.b"] + 0.5, 0.4, lambda a: E.pilula(c, "suco 100% natural", 1450, 360, 50, "b", fundo=TINTA, a=a))
    E.frase(c, t, C["s07.b"] + 1.0, [("também", "i", 70), ("mistura", "g", 70, COR)], XE, 920, passo=0.12)


# ---------------- simples × composta ----------------
def b_simples(c, t, C, b):
    xa, xb = 520, 1400
    E.foco(c, t, C["s08.b"], 0.5, lambda a: E.pilula(c, "SIMPLES", xa, 200, 56, "g", fundo=TINTA, a=a))
    E.foco(c, t, C["s09.b"], 0.5, lambda a: E.pilula(c, "COMPOSTA", xb, 200, 56, "g", fundo=TINTA, a=a))
    M.line(c, W / 2, 260, W / 2, 1000, FIO, ep(t, C["s08.b"], 0.6), 3)
    # coluna da esquerda: O₂ (e H₂ no s10)
    cores_a = {"O": E.COR} if t >= C["s10.b"] else None
    Q.molecula(c, t, C["s08.a"], "O2", xa, 420, 120, passo=0.2)
    Q.formula_em(c, t, C["s08.a"] + 0.4, "O2", xa, 640, 150, align="center", cores=cores_a)
    E.frase(c, t, C["s08.b"] + 0.4, [("1", "g", 60, COR), ("elemento", "i", 64)], xa, 750, "center", 0.12)
    if t >= C["s10.b"]:
        Q.molecula(c, t, C["s10.b"] + 0.2, "H2", xa - 120, 860, 100, passo=0.2)
        Q.formula_em(c, t, C["s10.b"] + 0.3, "H2", xa + 20, 900, 110, cores={"H": E.COR})
    # coluna da direita: H₂O e CO₂
    cores_b = {"H": E.COR, "O": E.COR} if t >= C["s10.c"] else None
    Q.molecula(c, t, C["s09.a"], "H2O", xb - 200, 420, 120, passo=0.2)
    Q.formula_em(c, t, C["s09.a"] + 0.4, "H2O", xb - 200, 640, 150, align="center", cores=cores_b)
    E.frase(c, t, C["s09.b"] + 0.4, [("2", "g", 60, COR), ("ou", "i", 64), ("mais", "i", 64), ("elementos", "i", 64)], xb, 750, "center", 0.12)
    Q.molecula(c, t, C["s09.c"], "CO2", xb + 220, 420, 105, passo=0.2)
    Q.formula_em(c, t, C["s09.c"] + 0.4, "CO2", xb + 220, 640, 150, align="center", cores={"C": E.COR, "O": E.COR} if t >= C["s10.c"] else None)
    # s10: as maiúsculas
    if t >= C["s10.a"]:
        E.frase(c, t, C["s10.a"], ps("conte as", "i", 64, TINTA2) + [("maiúsculas", "g", 60, COR)], W / 2, 1040, "center", 0.12)
    if t >= C["s10.b"]:
        pilula_em(c, t, C["s10.b"] + 0.6, "1 maiúscula", xa, 980, 44, TINTA)
    if t >= C["s10.c"]:
        pilula_em(c, t, C["s10.c"] + 0.6, "2 ou mais", xb, 860, 44, TINTA)


# ---------------- homogênea × heterogênea ----------------
def b_fases(c, t, C, b):
    ca, cb, yb, w, h = 560, 1360, 900, 380, 460
    # copo da esquerda: água + sal que some
    copo_camadas(c, t, C["s11"], ca, yb, w, h, [(Q.AGUA, 0.72, None)])
    if t < C["s11.b"] + 2:
        graos_sal(c, t, C["s11.a"], C["s11.a"] + 1.4, ca, yb - h - 80, yb - 120)
    E.frase(c, t, C["s11.a"], ps("água + sal", "i", 64, TINTA2), ca, 330, "center", 0.12)
    E.frase(c, t, C["s11.b"], ps("o mesmo aspecto em tudo", "i", 52, TINTA2), ca, 1000, "center", 0.08)
    pilula_em(c, t, C["s11.c"], "homogênea", ca, 220, 60, E.COR)
    E.foco(c, t, C["s11.d"], 0.4, lambda a: E.escreve(c, "ar, água mineral", ca - 200, 1060, 46, "i", TINTA2, a))
    # copo da direita: água + óleo
    if t >= C["s12"]:
        copo_camadas(c, t, C["s12"], cb, yb, w, h, [(Q.AGUA, 0.45, None), (OLEO, 0.25, C["s12.a"])])
        E.frase(c, t, C["s12.a"], ps("água + óleo", "i", 64, TINTA2), cb, 330, "center", 0.12)
        if t >= C["s12.b"]:
            yd = yb - (h - 0) * 0.45 + 4
            q = ep(t, C["s12.b"], 0.5)
            M.line(c, cb - w / 2 - 60, yd, cb - w / 2 - 6, yd, E.COR, q, 6)
            E.foco(c, t, C["s12.b"], 0.4, lambda a: E.escreve(c, "divisa", cb - w / 2 - 230, yd + 16, 46, "b", COR, a))
        pilula_em(c, t, C["s12.c"], "heterogênea", cb, 220, 60, E.COR)
    # s13: fases numeradas
    if t >= C["s13.a"]:
        E.frase(c, t, C["s13.a"], [("fase", "g", 60, COR), ("=", "g", 60, TINTA2)] + ps("parte com o mesmo aspecto", "i", 60), W / 2, 130, "center", 0.1)
    if t >= C["s13.b"]:
        num(c, t, C["s13.b"], 1, ca - w / 2 - 60, yb - h * 0.36)
        E.foco(c, t, C["s13.b"] + 0.3, 0.4, lambda a: E.escreve(c, "1 fase", ca - w / 2 - 110 - E.larg("1 fase", "g", 50), yb - h * 0.36 + 16, 50, "g", TINTA, a))
    if t >= C["s13.c"]:
        num(c, t, C["s13.c"], 1, cb + w / 2 + 60, yb - h * 0.22)
        num(c, t, C["s13.c"] + 0.3, 2, cb + w / 2 + 60, yb - h * 0.58)
        E.foco(c, t, C["s13.c"] + 0.6, 0.4, lambda a: E.escreve(c, "2 fases", cb + w / 2 + 110, yb - h * 0.4 + 16, 50, "g", TINTA, a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    cx, yb, w, h = 600, 960, 420, 560
    E.frase(c, t, C["s14"], [("cuidado", "g", 96, ERRADO)], XE, 190)
    E.frase(c, t, C["s14.a"], ps("componentes no lugar das fases", "i", 64), XE + 420, 190, passo=0.1)
    copo_camadas(c, t, C["s14.b"], cx, yb, w, h, [(Q.AGUA, 0.5, None), (OLEO, 0.22, None)])
    if t < C["s15.a"] + 1.5:
        graos_sal(c, t, C["s14.b"] + 0.4, C["s15.a"], cx, yb - h, yb - 160, semente=5)
    for k, s in enumerate(("água", "sal", "óleo")):
        pilula_em(c, t, C["s14.b"] + 0.4 * k, s, 1150 + 210 * k, 340, 48, TINTA)

    def errado():
        E.frase(c, t, C["s14.c"], [("3", "g", 110, ERRADO), ("fases?", "i", 100, ERRADO)], 1150, 560, passo=0.15)
        if t >= C["s14.c"] + 1.0:
            E.risco(c, 1130, 590, 1560, 460, t, C["s14.c"] + 1.0, largura=12)
    E.saida(c, t, C["s15.a"] - 0.1, errado)
    if t < C["s15.a"]:
        return
    E.frase(c, t, C["s15.a"], ps("o sal está espalhado na água", "i", 56, TINTA2), 1080, 470, passo=0.08)
    if t >= C["s15.b"]:
        num(c, t, C["s15.b"], 1, cx + w / 2 + 60, yb - h * 0.25)
        E.foco(c, t, C["s15.b"] + 0.2, 0.4, lambda a: E.escreve(c, "água com sal", cx + w / 2 + 110, yb - h * 0.25 + 16, 46, "b", TINTA, a))
    if t >= C["s15.c"]:
        num(c, t, C["s15.c"], 2, cx + w / 2 + 60, yb - h * 0.61)
        E.foco(c, t, C["s15.c"] + 0.2, 0.4, lambda a: E.escreve(c, "óleo", cx + w / 2 + 110, yb - h * 0.61 + 16, 46, "b", TINTA, a))
    E.frase(c, t, C["s15.d"], [("3", "g", 90, COR), ("componentes", "i", 80)], 1300, 700, passo=0.14)
    E.frase(c, t, C["s15.d"] + 0.8, [("2", "g", 90, COR), ("fases", "i", 80)], 1300, 820, passo=0.14)
    E.foco(c, t, C["s15.d"] + 1.2, 0.4, lambda a: E.selo(c, 1800, 760, 56, True, a))
    pilula_em(c, t, C["s15.e"], "sal sobrando no fundo = mais uma fase", 1380, 980, 40, TINTA2, "b")


# ---------------- alótropos ----------------
def sol(c, cx, cy, r, a=1.0):
    for k in range(12):
        ang = k * math.tau / 12 + 0.2 * math.sin(0)
        M.line(c, cx + (r + 14) * math.cos(ang), cy + (r + 14) * math.sin(ang), cx + (r + 44) * math.cos(ang), cy + (r + 44) * math.sin(ang), "#F5B400", a, 8)
    E.bola(c, cx, cy, r, "#FFC21A", a)


def grafite(c, cx, cy, a=1.0):
    """duas folhas de anéis de carbono, uma sobre a outra"""
    r = 46
    for camada, dy in enumerate((-80, 80)):
        pts, arestas = [], []
        for i in range(3):
            hx, hy = cx - 1.732 * r + i * 1.732 * r + camada * 40, cy + dy
            v = [(hx + r * math.cos(math.radians(30 + 60 * k)), hy + 0.55 * r * math.sin(math.radians(30 + 60 * k))) for k in range(6)]
            arestas += [(v[k], v[(k + 1) % 6]) for k in range(6)]
            pts += v
        for P, Q_ in arestas:
            M.line(c, P[0], P[1], Q_[0], Q_[1], Q.LIGA, a, 5)
        for (x, y) in pts:
            Q.atomo(c, x, y, 15, "C", a, rotulo=False)
    for k in range(3):
        x = cx - 1.732 * r + k * 1.732 * r + 20
        M.line(c, x, cy - 50, x, cy + 50, CINZA, 0.6 * a, 3, dash=[8, 8])


def diamante(c, cx, cy, s, a=1.0):
    """o diamante lapidado"""
    top, mid, bot = cy - s * 0.55, cy - s * 0.2, cy + s * 0.75
    pts = [(cx - s * 0.5, top), (cx + s * 0.5, top), (cx + s * 0.85, mid), (cx, bot), (cx - s * 0.85, mid)]
    p = skia.Path(); p.moveTo(*pts[0])
    for P in pts[1:]:
        p.lineTo(*P)
    p.close()
    pt = skia.Paint(AntiAlias=True)
    pt.setShader(skia.GradientShader.MakeLinear([skia.Point(cx - s, top), skia.Point(cx + s, bot)], [M.hexc("#E8FBFF", a), M.hexc("#9FD8E8", a)]))
    c.drawPath(p, pt)
    for P, Q_ in ((pts[4], pts[2]), (pts[0], (cx - s * 0.2, mid)), (pts[1], (cx + s * 0.2, mid)), ((cx - s * 0.2, mid), pts[3]), ((cx + s * 0.2, mid), pts[3]),
                  ((cx - s * 0.2, mid), (cx, top)), ((cx + s * 0.2, mid), (cx, top))):
        M.line(c, P[0], P[1], Q_[0], Q_[1], "#5AA8C0", a, 3)
    c.drawPath(p, M.paint("#3D8CA6", a, stroke=4))


def b_alotropia(c, t, C, b):
    if t < C["s18"]:
        def ozonio():
            Q.molecula(c, t, C["s16.a"] - 0.6, "O2", 560, 470, 130, passo=0.25)
            Q.molecula(c, t, C["s16.a"], "O3", 1360, 470, 130, passo=0.25)
            Q.formula_em(c, t, C["s16.a"] - 0.4, "O2", 560, 720, 150, align="center")
            Q.formula_em(c, t, C["s16.a"] + 0.3, "O3", 1360, 720, 150, align="center", cores={"indice": E.COR} if t >= C["s16.d"] else None)
            E.frase(c, t, C["s16.a"] + 0.6, ps("ozônio", "i", 64, TINTA2), 1360, 820, "center")
            E.frase(c, t, C["s16"], ps("os dois: só oxigênio", "i", 60, TINTA2), W / 2, 200, "center", 0.1)
            E.foco(c, t, C["s16.b"], 0.4, lambda a: centro(c, "=", W / 2, 500, 140, "g", TINTA2, a) if t < C["s16.c"] else None)
            if t >= C["s16.c"]:
                E.foco(c, t, C["s16.c"], 0.4, lambda a: centro(c, "≠", W / 2, 500, 140, "g", ERRADO, a))
            E.frase(c, t, C["s16.c"] + 0.5, [("2", "g", 60, COR), ("átomos", "i", 60)], 560, 940, "center", 0.1)
            E.frase(c, t, C["s16.d"], [("3", "g", 60, COR), ("átomos", "i", 60)], 1360, 940, "center", 0.1)
        if t < C["s17"]:
            E.saida(c, t, C["s17"] - 0.1, ozonio)
            return
        # s17: propriedades
        Q.molecula_desenho(c, "O2", 420, 360, 100)
        Q.formula(c, "O2", 420, 520, 110, align="center")
        E.frase(c, t, C["s17.a"], ps("sem cheiro", "i", 60), 420, 640, "center", 0.1)
        E.frase(c, t, C["s17.a"] + 0.8, [("você", "i", 60), ("respira", "g", 56, COR)], 420, 730, "center", 0.1)
        Q.molecula_desenho(c, "O3", 1050, 360, 100)
        Q.formula(c, "O3", 1050, 520, 110, align="center")
        E.frase(c, t, C["s17.b"], ps("cheiro forte", "i", 60), 1050, 640, "center", 0.1)
        E.frase(c, t, C["s17.b"] + 0.8, [("irrita", "g", 56, ERRADO), ("o pulmão", "i", 60)], 1050, 730, "center", 0.1)
        if t >= C["s17.c"]:
            E.foco(c, t, C["s17.c"], 0.5, lambda a: sol(c, 1660, 230, 70, a))
            q = ep(t, C["s17.c"] + 0.4, 0.6)
            M.rrect(c, 1380, 440, 520, 70, 35, E.COR, 0.85 * q)
            E.foco(c, t, C["s17.c"] + 0.5, 0.4, lambda a: centro(c, "camada de ozônio", 1640, 488, 40, "b", BR, a))
            for k in range(3):
                x = 1560 + 70 * k
                M.arrow(c, x, 320, x - 20, 430, "#F5B400", q, 6, 20, ease_io(prog(t, C["s17.c"] + 0.6 + 0.15 * k, 0.5)))
                M.line(c, x - 40, 600, x - 50, 640, "#F5B400", 0.35 * q, 6)
            E.frase(c, t, C["s17.c"] + 1.4, ps("barra parte da luz", "i", 52, TINTA2), 1640, 720, "center", 0.08)
            E.frase(c, t, C["s17.c"] + 2.0, ps("que queima a pele", "i", 52, TINTA2), 1640, 790, "center", 0.08)
        return
    # s18: alótropos
    E.frase(c, t, C["s18.a"], ps("mesmo elemento, substâncias simples diferentes:", "i", 56, TINTA2), W / 2, 160, "center", 0.08)
    E.frase(c, t, C["s18.a"] + 1.6, [("alótropos", "g", 120, COR)], W / 2, 310, "center")
    E.foco(c, t, C["s18.b"], 0.4, lambda a: (Q.atomo(c, W / 2, 450, 46, "C", a), E.escreve(c, "carbono", W / 2 + 70, 466, 52, "i", TINTA2, a)))
    E.foco(c, t, C["s18.c"], 0.6, lambda a: grafite(c, 520, 700, a))
    E.frase(c, t, C["s18.c"] + 0.3, [("grafite", "g", 66)], 520, 940, "center")
    E.foco(c, t, C["s18.c"] + 0.5, 0.4, lambda a: E.escreve(c, "do lápis", 430, 1010, 46, "i", TINTA2, a))
    E.foco(c, t, C["s18.d"], 0.6, lambda a: diamante(c, 1400, 680, 190, a))
    E.frase(c, t, C["s18.d"] + 0.3, [("diamante", "g", 66)], 1400, 940, "center")
    pilula_em(c, t, C["s18.e"], "muda o arranjo dos átomos", W / 2, 1020, 44, E.COR)


# ---------------- atalho (palco) ----------------
def caixa_dec(c, s, cx, cy, w, h, a, borda, cor_txt=BR, size=52, est="g"):
    if a <= 0:
        return
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#14141E", a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26), M.paint(borda, a, stroke=4))
    centro(c, s, cx, cy + size * 0.36, size, est, cor_txt, a)


def seta(c, t, t0, x0, y0, x1, y1, cor=None, rot=None):
    p = ep(t, t0, 0.4)
    if p <= 0:
        return
    M.arrow(c, x0, y0, x1, y1, cor or E.CLARO, p, 5, 20, ease_io(prog(t, t0, 0.5)))
    if rot:
        E.foco(c, t, t0 + 0.2, 0.3, lambda a: centro(c, rot, (x0 + x1) / 2 + (-50 if x1 < x0 else 50), (y0 + y1) / 2 + 10, 40, "b", E.CLARO, a))


def b_atalho(c, t, C, b):
    palco(c, t)
    if t < C["s21"]:
        def arvore():
            E.frase(c, t, C["s19"], ps("o atalho:", "i", 66, CLARO) + [("duas perguntas", "g", 62, BR)], W / 2, 120, "center", 0.12)
            E.foco(c, t, C["s19.b"], 0.4, lambda a: caixa_dec(c, "uma fórmula só?", W / 2, 250, 640, 110, a, E.CLARO))
            seta(c, t, C["s19.c"], W / 2 - 220, 310, 560, 410, rot="sim")
            E.foco(c, t, C["s19.c"] + 0.3, 0.4, lambda a: caixa_dec(c, "substância", 480, 470, 440, 100, a, BR))
            seta(c, t, C["s19.d"], 400, 525, 320, 640)
            seta(c, t, C["s19.d"] + 0.6, 560, 525, 640, 780)
            E.foco(c, t, C["s19.d"], 0.4, lambda a: caixa_dec(c, "1 maiúscula: simples", 300, 700, 470, 100, a, "#8A8D99", size=44, est="b"))
            E.foco(c, t, C["s19.d"] + 0.6, 0.4, lambda a: caixa_dec(c, "2 ou mais: composta", 700, 840, 470, 100, a, "#8A8D99", size=44, est="b"))
            seta(c, t, C["s20.a"], W / 2 + 220, 310, 1360, 410, rot="não")
            E.foco(c, t, C["s20.a"] + 0.3, 0.4, lambda a: caixa_dec(c, "mistura", 1440, 470, 440, 100, a, E.CLARO, E.CLARO))
            seta(c, t, C["s20.b"], 1440, 522, 1440, 578)
            E.foco(c, t, C["s20.b"], 0.4, lambda a: caixa_dec(c, "vê partes diferentes?", 1440, 640, 600, 100, a, BR, size=46))
            seta(c, t, C["s20.c"], 1350, 695, 1250, 790, rot="não")
            seta(c, t, C["s20.d"], 1530, 695, 1630, 790, rot="sim")
            E.foco(c, t, C["s20.c"] + 0.2, 0.4, lambda a: caixa_dec(c, "homogênea", 1220, 850, 380, 100, a, E.CLARO, E.CLARO, 46))
            E.foco(c, t, C["s20.d"] + 0.2, 0.4, lambda a: caixa_dec(c, "heterogênea", 1660, 850, 400, 100, a, E.CLARO, E.CLARO, 46))
            E.foco(c, t, C["s20.b"] + 1.2, 0.4, lambda a: centro(c, "a olho nu ou no microscópio", 1440, 970, 44, "i", CLARO, a))
        E.saida(c, t, C["s21"] - 0.1, arvore)
        return
    E.frase(c, t, C["s21.a"], ps("as perguntas são as", "i", 66, CLARO) + [("definições", "g", 62, BR)], W / 2, 220, "center", 0.12)
    E.frase(c, t, C["s21.b"], [("não", "g", 60, ERRADO), ("compensa:", "i", 64, CLARO)] + ps("desenho de bolinhas", "i", 64, CLARO), W / 2, 360, "center", 0.12)

    def caixa():
        bx, by, bw, bh = 560, 460, 800, 440
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, by, bw, bh), 24, 24), M.paint("#8A8D99", 1, stroke=4))
        mols = [("O2", 680, 560, 10), ("O3", 900, 600, 60), ("O2", 1150, 540, 120), ("O3", 1250, 780, 200), ("O2", 760, 800, 280), ("O3", 1000, 820, 330)]
        for k, (m, x, y, g) in enumerate(mols):
            Q.molecula_desenho(c, m, x + 5 * math.sin(t + k), y + 5 * math.cos(t * 1.2 + k), 60, 1, giro=g + 10 * math.sin(t * 0.5 + k), escuro=True)
    E.foco(c, t, C["s21.b"] + 0.8, 0.6, lambda a: caixa())
    E.frase(c, t, C["s21.c"], ps("conte os tipos de molécula:", "i", 60, CLARO) + [("2 tipos", "g", 56, BR)], W / 2, 990, "center", 0.1)


# ---------------- questão ----------------
QX, QYB, QW, QH = 1450, 960, 400, 560
CAMADAS_Q = [("areia", 0.16, None), (Q.AGUA, 0.42, None), (OLEO, 0.18, None)]


def b_questao(c, t, C, b):
    E.frase(c, t, C["s22"], ps("hora de testar", "i", 72, COR), XE, 180)
    E.frase(c, t, C["s22.a"], ps("água, sal dissolvido, óleo e areia", "i", 58, TINTA2), XE, 300, passo=0.08)
    E.frase(c, t, C["s22.b"], [("1", "g", 60, COR)] + ps("quantas fases?", "i", 66), XE, 500, passo=0.1)
    E.frase(c, t, C["s22.c"], [("2", "g", 60, COR)] + ps("quantos componentes?", "i", 66), XE, 640, passo=0.1)
    E.frase(c, t, C["s22.d"], [("3", "g", 60, COR)] + ps("homogênea ou heterogênea?", "i", 66), XE, 780, passo=0.1)
    if t < C["s23"]:
        copo_camadas(c, t, C["s22.a"], QX, QYB, QW, QH, CAMADAS_Q)
    else:
        E.relogio(c, t, C["s23.a"], cx=1470, cy=470, r=200)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    fx = copo_camadas(c, t, C["s24"], 560, 980, 400, 560, CAMADAS_Q)
    if fx:
        for k, key in enumerate(("s24.a", "s24.b", "s24.c")):
            i = (1, 2, 0)[k]
            yc = (fx[i][0] + fx[i][1]) / 2
            num(c, t, C[key], k + 1, 560 + 200 + 60, yc)
            nome = ("água com sal", "óleo", "areia")[k]
            E.foco(c, t, C[key] + 0.2, 0.4, lambda a, yc=yc, nome=nome: E.escreve(c, nome, 560 + 200 + 110, yc + 16, 44, "b", TINTA, a))
    bola_txt(c, t, C["s24.d"], "3", 1300, 260, 70, 90, CERTO)
    E.frase(c, t, C["s24.d"] + 0.3, [("fases", "i", 80)], 1400, 290)
    for k, s in enumerate(("água", "sal", "óleo", "areia")):
        pilula_em(c, t, C["s25.a"] + 0.3 * k, s, 1240 + 170 * k, 470, 44, TINTA)
    bola_txt(c, t, C["s25.b"], "4", 1300, 620, 70, 90, CERTO)
    E.frase(c, t, C["s25.b"] + 0.3, [("componentes", "i", 80)], 1400, 650)
    pilula_em(c, t, C["s25.c"], "heterogênea", 1520, 800, 60, E.COR)

    def erro():
        E.foco(c, t, C["s25.d"], 0.5, lambda a: E.escreve(c, "4 fases: contou o sal", 1230, 960, 52, "i", ERRADO, a))
        if t >= C["s25.d"] + 0.8:
            E.risco(c, 1220, 975, 1740, 920, t, C["s25.d"] + 0.8, largura=8)
    erro()


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s26"], [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s26.a", [("substância", "g", 66), ("=", "g", 66, TINTA2), ("um", "i", 70), ("tipo", "i", 70), ("de", "i", 70), ("partícula", "i", 70)]),
                 ("s26.b", [("mistura", "g", 66, COR), ("=", "g", 66, TINTA2), ("dois", "i", 70), ("ou", "i", 70), ("mais", "i", 70)]),
                 ("s26.c", [("simples", "g", 66), ("1", "g", 66, COR), ("elemento;", "i", 70), ("composta,", "g", 66), ("mais", "i", 70)]),
                 ("s26.d", [("fase", "g", 66, COR), ("=", "g", 66, TINTA2), ("cada", "i", 70), ("parte", "i", 70), ("que", "i", 70), ("você", "i", 70), ("distingue", "i", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 350 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 26, 52, a=a), centro(c, str(i + 1), 300, y - 4, 60, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y, passo=0.12)
    E.saida(c, t, C["s27"] - 0.1, resumo)
    if t < C["s27"]:
        return
    E.frase(c, t, C["s27"], [("próxima", "i", 80), ("aula", "i", 80)], XE, 250)
    E.frase(c, t, C["s27.b"], [("Estados", "g", 110, COR), ("físicos", "g", 110, COR)], XE, 400)
    for k, (est, n) in enumerate((("solido", 16), ("liquido", 14), ("gas", 8))):
        x = XE + 20 + k * 300
        tk = C["s27.a"] + 0.3 * k
        E.foco(c, t, tk, 0.5, lambda a, x=x: c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 560, 240, 240), 20, 20), M.paint(Q.VIDRO, a, stroke=4)))
        if t >= tk:
            Q.particulas(c, t, x + 10, 570, 220, 220, n, est, tipos=[(E.COR, 1.0)], r=16, semente=3 + k, a=ep(t, tk, 0.5))
        E.foco(c, t, tk + 0.3, 0.4, lambda a, x=x, k=k: centro(c, ("sólido", "líquido", "gás")[k], x + 120, 870, 48, "i", TINTA2, a))
    E.foco(c, t, C["s27.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1520, 420, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s27.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1820, 1650, p), lerp(720, 445, p), ep(t, C["s27.c"] + 0.2, 0.4))
    E.frase(c, t, C["s27.d"], [("bons", "i", 104), ("estudos!", "i", 104, COR)], 1520, 990, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, pura=b_pura, simples=b_simples, fases=b_fases, erro=b_erro,
              alotropia=b_alotropia, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
