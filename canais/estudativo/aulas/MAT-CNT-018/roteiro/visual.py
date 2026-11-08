"""Visual — Estudativo · MAT-CNT-018: árvore de probabilidades.
Mesma linguagem da trilha Contagem e Probabilidade (MAT-CNT-001 a 017): E.arvore da MAT-CNT-001 agora com a chance em fração em cada galho
(ramos="f{1}{3}"), caminhos em destaque na cor da matéria, igual_bola() com o resultado na esfera, linha() com contas e frações numa linha
(MAT-CNT-013), pessoa() da MAT-CNT-005/015.
Peças desta aula:
- conta_ponta(): a conta do caminho (1/3 × 1/2 = 1/6) escrita ao lado da ponta da árvore.
- gene(): a versão do gene numa pílula, A (dominante) na cor da matéria e a (recessiva) em âmbar.
- arvore_clara(): árvore desenhada à mão em branco, para o palco escuro (o E.arvore usa tinta escura), com galhos cortados tracejados.
- maquina(): máquina da fábrica, para a questão.
Sem voz ainda: todo instante vem de C[...] (cenas e marcadores), nunca de segundos fixos."""
import math
from fractions import Fraction as Fr
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Contagem e Probabilidade")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-CNT-018_arvore_probabilidades.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("chuva", "regra", "genetica", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
AMBAR = "#E8920C"
CHUVA = {("chove", "atrasa"): Fr(1, 3) * Fr(1, 2), ("não chove", "atrasa"): Fr(2, 3) * Fr(1, 4),
         ("chove", "não atrasa"): Fr(1, 3) * Fr(1, 2), ("não chove", "não atrasa"): Fr(2, 3) * Fr(3, 4)}
assert Fr(1) - Fr(1, 3) == Fr(2, 3) and CHUVA[("chove", "atrasa")] == Fr(1, 6) and Fr(2, 12) == Fr(1, 6) == CHUVA[("não chove", "atrasa")]
assert Fr(1, 6) + Fr(1, 6) == Fr(2, 6) == Fr(1, 3) and sum(CHUVA.values()) == 1
assert Fr(1, 2) * Fr(1, 2) == Fr(1, 4) and Fr(1, 4) * 100 == 25 and Fr(1, 4) + Fr(1, 4) == Fr(1, 2)
assert Fr(1) - Fr(3, 5) == Fr(2, 5) and Fr(3, 5) * Fr(1, 10) == Fr(3, 50) and Fr(2, 5) * Fr(1, 20) == Fr(2, 100) == Fr(1, 50)
assert Fr(3, 50) + Fr(1, 50) == Fr(4, 50) and Fr(4, 50) * 100 == 8


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trilha (MAT-CNT-002 a 017) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    """uma frase, palavra a palavra, no mesmo estilo"""
    return [(w, est, size, cor) for w in txt.split()]


def igual_bola(c, t, t0, x, y, txt, r=120, size=None, cor=None, escuro=False, t_igual=None):
    """'=' em x e o resultado numa esfera à direita; y = centro. Devolve o centro da esfera."""
    size = size or r * (0.72 if len(txt) <= 2 else 0.56 if len(txt) == 3 else 0.46 if len(txt) == 4 else 0.38)
    E.sinal(c, t, t0 - 0.2 if t_igual is None else t_igual, "=", x, y, r * 0.75, BR if escuro else TINTA)
    bx = x + r * 0.55 + r
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, bx, y, r, cor, a), centro(c, txt, bx, y + size * 0.36, size, "g", E.SOBRE, a)))
    return bx


def nota(c, t, t0, x, y, txt, size=46, cor=TINTA2, estilo="b"):
    E.foco(c, t, t0, 0.45, lambda a: centro(c, txt, x, y, size, estilo, cor, a))


def larg_parte(p, size):
    return E.larg(p, "g", size) if isinstance(p, str) else max(E.larg(str(p[0]), "g", size), E.larg(str(p[1]), "g", size)) + size * 0.2


def linha(c, t, x, y, size, partes, align="left", gap=None):
    """conta numa linha: partes = [(texto ou (n, d), instante[, cor])]; y = altura da barra das frações. Devolve o x de cada parte e o fim"""
    gap = size * 0.28 if gap is None else gap
    ws = [larg_parte(p[0], size) for p in partes]
    tot = sum(ws) + gap * (len(partes) - 1)
    xx = x - tot / 2 if align == "center" else x - tot if align == "right" else x
    xs = []
    for (p, t0, *cor), w in zip(partes, ws):
        cor = cor[0] if cor else TINTA
        xs.append(xx)
        if isinstance(p, str):
            E.foco(c, t, t0, 0.45, lambda a, p=p, xx=xx, cor=cor: E.escreve(c, p, xx, y + size * 0.34, size, "g", cor, a))
        else:
            E.fr(c, t, t0, p[0], p[1], xx + w / 2, y, size, cor)
        xx += w + gap
    return xs, xx - gap


def pil_esq(c, t, t0, x, y, txt, size=46, fundo=None, cor=BR):
    """pílula com a borda esquerda em x"""
    w = E.larg(txt, "g", size) + size * 1.1
    E.foco(c, t, t0, 0.45, lambda a: E.pilula(c, txt, x + w / 2, y, size, estilo="g", fundo=fundo or TINTA2, cor=cor, a=a))


def pessoa(c, cx, cy, h, cor, a=1.0, mulher=False):
    """boneco simples (MAT-CNT-005 / 015): a mulher tem o tronco em saia"""
    if a <= 0:
        return
    c.drawCircle(cx, cy - h * 0.36, h * 0.17, M.paint(cor, a))
    if mulher:
        pa = skia.Path()
        pa.moveTo(cx - h * 0.16, cy - h * 0.14); pa.lineTo(cx + h * 0.16, cy - h * 0.14)
        pa.lineTo(cx + h * 0.3, cy + h * 0.38); pa.lineTo(cx - h * 0.3, cy + h * 0.38); pa.close()
        c.drawPath(pa, M.paint(cor, a))
    else:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - h * 0.25, cy - h * 0.14, h * 0.5, h * 0.52), h * 0.2, h * 0.2), M.paint(cor, a))


# ---------------- peças desta aula ----------------
def conta_ponta(c, t, pos, cam, rotulo_size, partes, size=56, t_cor=None):
    """a conta do caminho ao lado da ponta: partes = [(texto ou (n, d), instante[, cor])]"""
    px, py = pos[cam]
    x = px + E.larg(cam[-1], "g", rotulo_size) / 2 + 40
    return linha(c, t, x, py, size, partes)


def gene(c, cx, cy, letra, size=60, a=1.0):
    """a versão do gene numa pílula: A dominante (cor da matéria), a recessiva (âmbar)"""
    E.pilula(c, letra, cx, cy, size, estilo="g", fundo=E.COR if letra == "A" else AMBAR, a=a)


def maquina(c, cx, cy, s, nome, a=1.0):
    """máquina da fábrica: caixa com engrenagem e o nome"""
    if a <= 0:
        return
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s * 0.4, s, s * 0.8), 24, 24)
    c.drawRRect(r, M.paint(BR, a))
    c.drawRRect(r, M.paint(TINTA, a, stroke=5))
    gx, gy, gr = cx - s * 0.18, cy + s * 0.05, s * 0.17
    for k in range(8):
        ang = k * math.pi / 4
        M.line(c, gx + math.cos(ang) * gr * 0.7, gy + math.sin(ang) * gr * 0.7, gx + math.cos(ang) * gr * 1.25, gy + math.sin(ang) * gr * 1.25, TINTA2, a, s * 0.06)
    c.drawCircle(gx, gy, gr, M.paint(TINTA2, a))
    c.drawCircle(gx, gy, gr * 0.4, M.paint(BR, a))
    centro(c, nome, cx + s * 0.26, cy + s * 0.18, s * 0.4, "g", COR, a)


def arvore_clara(c, t, t0, x, y, w, h, tcorte):
    """a árvore da chuva no palco: galhos brancos; os 'não atrasa' ficam tracejados, apagados e com um X em tcorte"""
    S, SF = 54, 44
    raiz = (x, y + h / 2)
    n1 = [(x + w * 0.4, y + h * 0.25, "chove", "f{1}{3}"), (x + w * 0.4, y + h * 0.75, "não chove", "f{2}{3}")]
    n2 = {0: [(x + w * 0.88, y + h * 0.08, "atrasa", "f{1}{2}", True), (x + w * 0.88, y + h * 0.4, "não atrasa", "f{1}{2}", False)],
          1: [(x + w * 0.88, y + h * 0.6, "atrasa", "f{1}{4}", True), (x + w * 0.88, y + h * 0.92, "não atrasa", "f{3}{4}", False)]}
    meia = lambda s_: E.larg(s_, "g", S) / 2 + 22
    q0 = ease_io(prog(t, t0, 0.6))
    if q0 > 0:
        c.drawCircle(*raiz, 10, M.paint(BR))
    for i, (nx, ny, rot, fr) in enumerate(n1):
        if q0 > 0:
            M.line(c, raiz[0] + 14, raiz[1], lerp(raiz[0] + 14, nx - meia(rot), q0), lerp(raiz[1], ny, q0), BR, 1, 6)
        E.foco(c, t, t0 + 0.4, 0.4, lambda a, nx=nx, ny=ny, rot=rot: centro(c, rot, nx, ny + S * 0.36, S, "g", BR, a))
        mx0, my0 = (raiz[0] + nx - meia(rot)) / 2, (raiz[1] + ny) / 2
        E.foco(c, t, t0 + 0.5, 0.4, lambda a, mx0=mx0, my0=my0, fr=fr, i=i: E.formula(c, fr, mx0 - 70, my0 + (-24 if i == 0 else 70), SF, "b", CLARO, a))
        q1 = ease_io(prog(t, t0 + 0.8, 0.6))
        for j, (mx, my, rot2, fr2, fica) in enumerate(n2[i]):
            al = 1.0 if fica else 1 - 0.7 * ep(t, tcorte, 0.5)
            ax_, bx_ = nx + meia(rot), mx - meia(rot2)
            if q1 > 0:
                p = M.paint(BR, al, stroke=6)
                if not fica and t >= tcorte:
                    p.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
                pa = skia.Path(); pa.moveTo(ax_, ny); pa.lineTo(lerp(ax_, bx_, q1), lerp(ny, my, q1))
                c.drawPath(pa, p)
            E.foco(c, t, t0 + 1.2, 0.4, lambda a, mx=mx, my=my, rot2=rot2, al=al: centro(c, rot2, mx, my + S * 0.36, S, "g", BR, a * al))
            fx, fy = (ax_ + bx_) / 2, (ny + my) / 2
            E.foco(c, t, t0 + 1.3, 0.4, lambda a, fx=fx, fy=fy, fr2=fr2, al=al, j=j:
                   E.formula(c, fr2, fx - 30, fy + (-26 if j == 0 else 72), SF, "b", CLARO, a * al))
            if not fica and t >= tcorte:
                q = ep(t, tcorte, 0.4)
                M.line(c, fx - 28 * q, fy - 28 * q, fx + 28 * q, fy + 28 * q, ERRADO, 1, 9)
                M.line(c, fx - 28 * q, fy + 28 * q, fx + 28 * q, fy - 28 * q, ERRADO, 1, 9)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def pergunta():
        E.foco(c, t, C["s01.a"] - 0.6, 0.45, lambda a: pessoa(c, 360, 420, 230, TINTA, a))
        E.foco(c, t, C["s01.a"] - 0.4, 0.45, lambda a: pessoa(c, 640, 420, 230, TINTA, a, True))
        nota(c, t, C["s01.a"] - 0.3, 360, 600, "pai", 48, TINTA2)
        nota(c, t, C["s01.a"] - 0.1, 640, 600, "mãe", 48, TINTA2)
        E.frase(c, t, C["s01.a"], ps("não têm a característica", "i", 64), 900, 330, passo=0.1)
        E.frase(c, t, lerp(C["s01.a"], C["s01.b"], 0.4), ps("mas carregam o gene escondido", "i", 56, TINTA2), 900, 430, passo=0.08)
        E.frase(c, t, C["s01.b"], [("o", "i", 72), ("filho", "g", 80, COR), ("pode", "i", 72), ("ter?", "g", 80)], 900, 600, passo=0.12)
        E.foco(c, t, lerp(C["s01.b"], C["s01.c"], 0.25), 0.45, lambda a: E.escreve(c, "pode!", 1500, 600, 72, "g", CERTO, a))
        E.foco(c, t, C["s01.b"] + 0.3, 0.45, lambda a: pessoa(c, 500, 860, 170, COR, a))
        nota(c, t, C["s01.b"] + 0.5, 500, 1000, "filho", 44, COR)
        xs, xf = linha(c, t, 900, 860, 110, [("chance:", C["s01.c"] - 0.3)])
        E.resultado(c, t, C["s01.c"], 1, 4, xf + 160, 860, 100, 120)
    E.saida(c, t, C["s02"] - 0.1, pergunta)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 520, 300 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 96), XE, 300)
        E.frase(c, t, C["s02.a"] + 0.9, [("a", "i", 100), ("árvore", "g", 116, COR)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.3, [("de", "i", 100), ("probabilidades", "g", 104, COR)], XE, 600)
        pil_esq(c, t, C["s02.b"], XE, 760, "quando × e quando +", 50)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.centro(c, "+ atalho", 1480, 490, 88, "g", BR, a),
                                                      E.centro(c, "de prova", 1480, 600, 88, "g", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.frase(c, t, C["s03"] + 0.1, [("você", "i", 84), ("vai", "i", 84), ("usar", "i", 84), ("duas", "g", 88, COR), ("coisas", "i", 84)], W / 2, 190, "center")
    for k, x, titulo in (("s03.b", 200, "etapas em sequência"), ("s03.c", 1000, "somar frações")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 720, 620, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 60, COR)], x + 360, 400, "center")
    E.foco(c, t, C["s03.b"] + 0.5, 0.45, lambda a: E.centro(c, "multiplique as chances", 560, 560, 52, "i", TINTA2, a))
    linha(c, t, 560, 720, 90, [((3, 5), C["s03.b"] + 0.8), ("×", C["s03.b"] + 1.0), ((2, 4), C["s03.b"] + 1.2)], "center")
    linha(c, t, 1360, 640, 90, [((1, 2), C["s03.c"] + 0.5), ("+", C["s03.c"] + 0.7), ((1, 3), C["s03.c"] + 0.9), ("=", C["s03.c"] + 1.2),
                                 ((5, 6), C["s03.c"] + 1.4, COR)], "center")
    nota(c, t, C["s03.c"] + 1.8, 1360, 840, "denominadores diferentes", 44, TINTA2, "i")
    E.frase(c, t, lerp(C["s03.c"], C["s03.end"], 0.8), ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 1010, "center", passo=0.1)


# ---------------- chuva ----------------
AX, AY, AW, AH = 120, 190, 1020, 660
RAMOS_CHUVA = [["f{1}{3}", "f{2}{3}"], lambda cam, rot: {("chove", "atrasa"): "f{1}{2}", ("chove", "não atrasa"): "f{1}{2}",
                                                       ("não chove", "atrasa"): "f{1}{4}", ("não chove", "não atrasa"): "f{3}{4}"}[(cam[0], rot)]]


def b_chuva(c, t, C, b):
    def dados():
        E.frase(c, t, C["s04"] + 0.1, ps("no dia a dia", "i", 72, TINTA2), W / 2, 180, "center")
        linha(c, t, 300, 360, 90, [("chover amanhã:", C["s04.a"]), ((1, 3), C["s04.a"] + 0.4, COR)])
        linha(c, t, 300, 560, 90, [("se chover, atrasar:", C["s04.b"]), ((1, 2), C["s04.b"] + 0.4, COR)])
        linha(c, t, 300, 760, 90, [("se não chover:", C["s04.c"]), ((1, 4), C["s04.c"] + 0.4, COR)])
        E.foco(c, t, C["s04.d"], 0.5, lambda a: E.pilula(c, "chance de se atrasar?", W / 2, 960, 58, estilo="g", a=a))
    E.saida(c, t, C["s05"] - 0.1, dados)
    if t < C["s05"]:
        return
    dest = []
    if t >= C["s06.b"]:
        dest.append(("chove", "atrasa"))
    if t >= C["s06.d"]:
        dest.append(("não chove", "atrasa"))
    pos = E.arvore(c, t, C["s05.a"] - 0.3, [("chove", "não chove"), ("atrasa", "não atrasa")], AX, AY, AW, AH, ramos=RAMOS_CHUVA,
                   tn=[C["s05.a"], C["s05.c"]], destaque=tuple(dest), size=44, size_ramo=44)
    nota(c, t, C["s05.b"] + 0.3, 330, AY + AH * 0.75 + 140, "o que falta para o inteiro", 40, TINTA2, "i")
    E.foco(c, t, C["s05.d"], 0.45, lambda a: E.pilula(c, "a chance em cima de cada galho", 1500, 140, 40, estilo="b", fundo=TINTA2, a=a) if t < C["s06"] else None)
    E.foco(c, t, C["s06.a"], 0.45, lambda a: E.pilula(c, "cada caminho: uma história completa", 1460, 140, 40, estilo="b", fundo=TINTA2, a=a) if t < C["s07.a"] else None)
    conta_ponta(c, t, pos, ("chove", "atrasa"), 44, [((1, 3), C["s06.b"] + 0.4), ("×", C["s06.b"] + 0.6), ((1, 2), C["s06.b"] + 0.8), ("=", C["s06.c"] - 0.2),
                                                     ((1, 6), C["s06.c"], COR)])
    conta_ponta(c, t, pos, ("não chove", "atrasa"), 44, [((2, 3), C["s06.d"] + 0.4), ("×", C["s06.d"] + 0.6), ((1, 4), C["s06.d"] + 0.8), ("=", C["s06.e"] - 0.2),
                                                         ((2, 12), C["s06.e"]), ("=", C["s06.e"] + 0.8), ((1, 6), C["s06.e"] + 1.0, COR)])
    # some os dois caminhos
    E.foco(c, t, C["s07.a"], 0.45, lambda a: E.pilula(c, "ou choveu, ou não choveu", 1460, 140, 40, estilo="b", fundo=TINTA2, a=a))
    E.foco(c, t, C["s07.b"], 0.5, lambda a: E.pilula(c, "some", 1000, 970, 52, estilo="g", a=a))
    xs, xf = linha(c, t, 1140, 970, 76, [((1, 6), C["s07.c"]), ("+", C["s07.c"] + 0.3), ((1, 6), C["s07.c"] + 0.5), ("=", C["s07.c"] + 0.9), ((2, 6), C["s07.c"] + 1.1)])
    E.sinal(c, t, C["s07.d"] - 0.2, "=", xf + 45, 970, 64)
    E.resultado(c, t, C["s07.d"], 1, 3, xf + 150, 970, 66, 75, CERTO)


# ---------------- regra ----------------
def mini(c, x, y, a, cor_caminhos):
    """árvore pequena de 2 níveis; cor_caminhos = 'ao longo' (um caminho inteiro) ou 'entre' (duas pontas)"""
    if a <= 0:
        return
    raiz = (x, y)
    ns = [(x + 140, y - 70), (x + 140, y + 70)]
    fs = [(x + 280, y - 105), (x + 280, y - 35), (x + 280, y + 35), (x + 280, y + 105)]
    forte = {"ao longo": {(0,), (0, 0)}, "entre": {(0,), (0, 0), (1,), (1, 0)}}[cor_caminhos]
    for i, (nx, ny) in enumerate(ns):
        M.line(c, *raiz, nx, ny, E.COR if (i,) in forte else TINTA2, a, 8 if (i,) in forte else 4)
        for j in range(2):
            fx, fy = fs[i * 2 + j]
            M.line(c, nx, ny, fx, fy, E.COR if (i, j) in forte else TINTA2, a, 8 if (i, j) in forte else 4)
    c.drawCircle(*raiz, 9, M.paint(TINTA, a))


def b_regra(c, t, C, b):
    E.frase(c, t, C["s08"] + 0.1, [("a", "i", 80), ("regra", "g", 86, COR), ("da", "i", 80), ("árvore", "g", 86, COR)], W / 2, 180, "center")
    for k, x, modo, simb, titulo, kp, palavra in (("s08.a", 200, "ao longo", "×", "ao longo do caminho", "s08.c", "e"),
                                                  ("s08.b", 1000, "entre", "+", "entre caminhos", "s08.d", "ou")):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, 290, 720, 680, p, prog_=p)
        E.frase(c, t, C[k] + 0.1, [(titulo, "g", 54, COR)], x + 360, 380, "center")
        E.foco(c, t, C[k] + 0.3, 0.5, lambda a, x=x, modo=modo: mini(c, x + 90, 560, a, modo))
        E.foco(c, t, C[k] + 0.6, 0.5, lambda a, x=x, simb=simb: (E.bola(c, x + 560, 560, 90, a=a), centro(c, simb, x + 560, 560 + 40, 110, "g", E.SOBRE, a)))
        E.foco(c, t, C[kp], 0.5, lambda a, x=x, palavra=palavra: (E.centro(c, "a palavra", x + 300, 830, 54, "i", TINTA2, a),
                                                                   E.centro(c, f"“{palavra}”", x + 520, 836, 84, "g", COR, a)))
    nota(c, t, C["s08.c"] + 0.4, 560, 920, "uma etapa depois da outra", 42, TINTA2, "i")
    nota(c, t, C["s08.d"] + 0.4, 1360, 920, "histórias diferentes", 42, TINTA2, "i")


# ---------------- genética ----------------
GX, GY, GW, GH = 160, 260, 860, 620
RAMOS_GENE = [["f{1}{2}", "f{1}{2}"], lambda cam, rot: "f{1}{2}"]


def arvore_gene(c, t, t0, tn, tf, destaque=(), cor_dest=None):
    pos = E.arvore(c, t, t0, [("A", "a"), ("A", "a")], GX, GY, GW, GH, ramos=RAMOS_GENE, folha=lambda cam: "".join(cam),
                   tn=tn, tf=tf, destaque=destaque, size=56, size_ramo=44)
    return pos


def b_genetica(c, t, C, b):
    def versoes():
        E.frase(c, t, C["s09"] + 0.1, [("genética", "g", 84, COR)], W / 2, 170, "center")
        E.frase(c, t, C["s09.a"], ps("cada pessoa tem 2 versões de um gene", "i", 60), W / 2, 300, "center", passo=0.08)
        E.foco(c, t, C["s09.a"] + 0.8, 0.45, lambda a: (gene(c, 840, 420, "A", 64, a), gene(c, 1080, 420, "a", 64, a)))
        E.frase(c, t, C["s09.b"], ps("e passa uma delas ao filho: meio a meio", "i", 60), W / 2, 560, "center", passo=0.08)
        E.frase(c, t, C["s09.c"], [("a", "i", 60), ("característica", "i", 60), ("só", "i", 60), ("aparece", "i", 60), ("com", "i", 60)],
                W / 2, 700, "center", passo=0.08)
        E.foco(c, t, C["s09.c"] + 1.2, 0.45, lambda a: (gene(c, 790, 800, "a", 60, a), E.centro(c, "do pai e", 960, 820, 54, "i", TINTA, a),
                                                        gene(c, 1150, 800, "a", 60, a), E.centro(c, "da mãe", 1320, 820, 54, "i", TINTA, a)))
        E.foco(c, t, lerp(C["s09.c"], C["s09.end"], 0.3), 0.45, lambda a: (gene(c, 600, 950, "a", 48, a),
                                                                           E.escreve(c, "recessiva: fica escondida quando a dominante está junto", 660, 966, 44, "b", TINTA2, a)))
    E.saida(c, t, C["s10"] - 0.1, versoes)
    if C["s10"] <= t < C["s11"]:
        def pais():
            for x, nome, mulher, tt in ((620, "pai", False, C["s10.a"]), (1300, "mãe", True, lerp(C["s10.a"], C["s10.b"], 0.55))):
                E.foco(c, t, tt - 0.3, 0.45, lambda a, x=x, mulher=mulher: pessoa(c, x, 430, 260, TINTA, a, mulher))
                nota(c, t, tt - 0.2, x, 620, nome, 52, TINTA2)
                E.foco(c, t, tt, 0.45, lambda a, x=x: (gene(c, x - 70, 730, "A", 60, a), gene(c, x + 70, 730, "a", 60, a)))
            E.foco(c, t, lerp(C["s10.a"], C["s10.b"], 0.3), 0.45, lambda a: (gene(c, 860, 220, "A", 44, a),
                                                                             E.escreve(c, "= dominante", 920, 236, 48, "b", TINTA2, a)))
            E.foco(c, t, C["s10.b"], 0.5, lambda a: E.pilula(c, "nem o pai nem a mãe mostram a característica", W / 2, 900, 46, estilo="g", fundo=TINTA2, a=a))
        E.saida(c, t, C["s11"] - 0.1, pais)
    if t < C["s11"]:
        return
    dest = []
    if C["s12.a"] <= t < C["s13"]:
        dest = [("a", "a")]
    elif t >= C["s13.b"]:
        dest = [("A", "a"), ("a", "A")]
    pos = arvore_gene(c, t, C["s11.a"] - 0.3, [C["s11.a"], C["s11.b"]], C["s11.c"], tuple(dest))
    nota(c, t, C["s11.a"], GX + 40 + (GW - 160) / 4, GY - 20, "pai passa", 44, TINTA2, "i")
    nota(c, t, C["s11.b"], GX + 40 + (GW - 160) * 3 / 4, GY - 20, "mãe passa", 44, TINTA2, "i")
    nota(c, t, C["s11.c"] + 0.5, GX + GW + 20, GY + GH + 70, "4 pontas", 48, TINTA2)
    XP = 1150
    if C["s12"] <= t < C["s13"]:
        def caracteristica():
            E.foco(c, t, C["s12.a"], 0.45, lambda a: E.escreve(c, "tem a característica:", XP, 330, 54, "i", TINTA, a))
            E.foco(c, t, C["s12.a"] + 0.4, 0.45, lambda a: (gene(c, XP + 60, 440, "a", 60, a), gene(c, XP + 200, 440, "a", 60, a)))
            linha(c, t, XP, 640, 96, [((1, 2), C["s12.b"]), ("×", C["s12.b"] + 0.3), ((1, 2), C["s12.b"] + 0.5), ("=", C["s12.b"] + 0.9),
                                      ((1, 4), C["s12.b"] + 1.1, COR)])
            E.foco(c, t, C["s12.c"], 0.5, lambda a: E.pilula(c, "25%", XP + 250, 850, 72, estilo="g", a=a))
        E.saida(c, t, C["s13"] - 0.1, caracteristica)
    if t < C["s13"]:
        return
    E.foco(c, t, C["s13.a"], 0.45, lambda a: E.escreve(c, "uma recessiva só?", XP, 330, 60, "g", TINTA, a))
    E.foco(c, t, C["s13.b"], 0.45, lambda a: E.escreve(c, "2 caminhos: do pai ou da mãe", XP, 430, 46, "b", TINTA2, a))
    for cam in (("A", "a"), ("a", "A")):
        px, py = pos[cam]
        E.foco(c, t, C["s13.c"], 0.45, lambda a, px=px, py=py: E.fracao(c, 1, 4, px + 175, py, 50, COR, a))
    linha(c, t, XP + 40, 880, 96, [((1, 4), C["s13.d"]), ("+", C["s13.d"] + 0.3), ((1, 4), C["s13.d"] + 0.5), ("=", C["s13.d"] + 0.9), ((1, 2), C["s13.d"] + 1.1, COR)])


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    E.frase(c, t, C["s14"] + 0.1, [("cuidado", "g", 90, ERRADO), ("com", "i", 84), ("isto", "i", 84)], W / 2, 150, "center")
    dest = [("a", "A")] if t < C["s14.c"] else [("A", "a"), ("a", "A")]
    pos = arvore_gene(c, t, C["s14"] + 0.2, [C["s14"] + 0.3, C["s14"] + 0.6], C["s14"] + 0.9, tuple(dest) if t >= C["s14.a"] else ())
    XP = 1150
    E.foco(c, t, C["s14.a"], 0.45, lambda a: E.pilula(c, "vê só um caminho", XP + 300, 330, 50, estilo="g", fundo=ERRADO, a=a))
    E.fr(c, t, C["s14.b"], 1, 4, XP + 120, 520, 110, ERRADO)
    if t >= C["s14.c"]:
        E.risco(c, XP + 50, 610, XP + 190, 430, t, C["s14.c"], largura=11)
    E.frase(c, t, C["s14.c"], ps("do pai e da mãe: histórias diferentes", "i", 50, TINTA2), XP, 720, passo=0.08)
    nota(c, t, lerp(C["s14.c"], C["s14.d"], 0.6), XP + 300, 800, "cada ponta conta", 48, COR)
    linha(c, t, XP, 920, 90, [((1, 4), C["s14.d"] - 0.3), ("+", C["s14.d"] - 0.2), ((1, 4), C["s14.d"] - 0.1), ("=", C["s14.d"]), ((1, 2), C["s14.d"] + 0.1, CERTO)])


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def corte():
        E.frase(c, t, C["s15.a"], [("corte", "g", 80, BR), ("os", "i", 74, CLARO), ("galhos", "i", 74, CLARO), ("que", "i", 74, CLARO), ("não", "i", 74, CLARO),
                                   ("interessam", "g", 80, BR)], W / 2, 190, "center", passo=0.1)
        E.frase(c, t, C["s15.b"], ps("desenhe só o que chega ao que a questão pede", "i", 54, CLARO), W / 2, 290, "center", passo=0.08)
        arvore_clara(c, t, C["s15.b"] + 0.4, 200, 390, 1200, 600, C["s15.c"])
        nota(c, t, C["s15.c"] + 0.6, 1620, 700, "não entram na soma", 50, CLARO, "i")
    E.saida(c, t, C["s16"] - 0.1, corte)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], ps("cada galho cortado: uma ponta que você não somaria", "i", 58, CLARO), W / 2, 230, "center", passo=0.08)
    E.foco(c, t, C["s16.b"], 0.5, lambda a: E.pilula(c, "não compensa: várias perguntas na mesma árvore", W / 2, 450, 52, estilo="g", fundo=ERRADO, a=a))
    E.frase(c, t, lerp(C["s16.b"], C["s16.c"], 0.6), ps("desenhe a árvore inteira", "i", 62, CLARO), W / 2, 640, "center", passo=0.1)
    E.foco(c, t, C["s16.c"], 0.5, lambda a: E.pilula(c, "confira: as pontas somam 1 inteiro", W / 2, 820, 60, estilo="g", fundo=E.COR, a=a))


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    E.frase(c, t, C["s17"] + 0.1, [("hora", "i", 72, COR), ("de", "i", 72, COR), ("testar", "i", 72, COR)], XE, 170)
    E.foco(c, t, C["s17.a"], 0.45, lambda a: maquina(c, XE + 140, 400, 250, "A", a))
    E.foco(c, t, C["s17.a"] + 0.3, 0.45, lambda a: maquina(c, XE + 140, 690, 250, "B", a))
    linha(c, t, XE + 310, 400, 72, [("faz", C["s17.b"]), ((3, 5), C["s17.b"] + 0.3, COR), ("· defeito", lerp(C["s17.b"], C["s17.c"], 0.5)),
                                    ((1, 10), lerp(C["s17.b"], C["s17.c"], 0.5) + 0.3, ERRADO)])
    linha(c, t, XE + 310, 690, 72, [("faz o resto", C["s17.c"]), ("· defeito", lerp(C["s17.c"], C["s17.d"], 0.5)),
                                    ((1, 20), lerp(C["s17.c"], C["s17.d"], 0.5) + 0.3, ERRADO)])
    E.frase(c, t, C["s17.d"], [("peça", "i", 66), ("ao", "i", 66), ("acaso:", "i", 66), ("chance", "i", 66), ("de", "i", 66), ("defeito?", "g", 74, ERRADO)],
            XE, 930, passo=0.1)
    E.relogio(c, t, C["s18.a"], 1560, 560, 180)


# ---------------- resposta ----------------
RX, RY, RW, RH = 140, 230, 760, 560


def b_resposta(c, t, C, b):
    dest = []
    if t >= C["s19.b"]:
        dest.append(("A", "defeito"))
    if t >= C["s19.d"]:
        dest.append(("B", "defeito"))
    ramos = [["f{3}{5}", "f{2}{5}"], lambda cam, rot: "f{1}{10}" if cam[0] == "A" else "f{1}{20}"]
    pos = E.arvore(c, t, C["s19"] + 0.2, [("A", "B"), ("defeito",)], RX, RY, RW, RH, ramos=ramos, tn=[C["s19"] + 0.3, C["s19.b"] - 0.6],
                   destaque=tuple(dest), size=50, size_ramo=44)
    nota(c, t, C["s19.a"] + 0.3, RX + 230, RY + RH * 0.75 + 130, "o que falta para o inteiro", 40, TINTA2, "i")
    nota(c, t, C["s19"] + 0.8, RX + RW / 2, RY - 70, "só os galhos de defeito", 42, TINTA2, "i")
    conta_ponta(c, t, pos, ("A", "defeito"), 50, [((3, 5), C["s19.b"] + 0.4), ("×", C["s19.b"] + 0.6), ((1, 10), C["s19.b"] + 0.8), ("=", C["s19.c"] - 0.2),
                                                  ((3, 50), C["s19.c"], COR)], size=64)
    conta_ponta(c, t, pos, ("B", "defeito"), 50, [((2, 5), C["s19.d"] + 0.4), ("×", C["s19.d"] + 0.6), ((1, 20), C["s19.d"] + 0.8), ("=", C["s19.e"] - 0.2),
                                                  ((2, 100), C["s19.e"]), ("=", C["s19.e"] + 1.0), ((1, 50), C["s19.e"] + 1.2, COR)], size=64)
    y = 950
    xs, xf = linha(c, t, 380, y, 80, [((3, 50), C["s20.a"]), ("+", C["s20.a"] + 0.3), ((1, 50), C["s20.a"] + 0.5), ("=", C["s20.a"] + 0.9), ((4, 50), C["s20.a"] + 1.1)])
    igual_bola(c, t, C["s20.b"], xf + 40, y, "8%", r=85, cor=CERTO)
    nota(c, t, C["s20.c"], xf + 430, y + 18, "8 em cada 100 peças", 46, TINTA2, "i")


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s21"], [("resumindo", "i", 92, COR)], W / 2, 190, "center")
        for k, x, modo, simb, titulo in (("s21.a", 200, "ao longo", "×", "ao longo do caminho"), ("s21.b", 1000, "entre", "+", "entre caminhos")):
            E.frase(c, t, C[k], [(titulo, "g", 56, COR)], x + 360, 400, "center")
            E.foco(c, t, C[k] + 0.2, 0.5, lambda a, x=x, modo=modo: mini(c, x + 90, 600, a, modo))
            E.foco(c, t, C[k] + 0.4, 0.5, lambda a, x=x, simb=simb: (E.bola(c, x + 560, 600, 90, a=a), centro(c, simb, x + 560, 640, 110, "g", E.SOBRE, a)))
    E.saida(c, t, C["s22"] - 0.1, resumo)
    if t < C["s22"]:
        return
    E.frase(c, t, C["s22"] + 0.1, ps("próxima aula", "i", 84), XE, 300)
    E.frase(c, t, C["s22.a"], [("praticando:", "i", 76), ("probabilidade", "g", 84, COR)], XE, 440, passo=0.12)
    E.frase(c, t, C["s22.a"] + 0.8, ps("contar, complementar, somar ou multiplicar", "i", 54, TINTA2), XE, 540, passo=0.08)
    E.frase(c, t, C["s22.b"], [("sorteio", "g", 70, COR), ("e", "i", 66), ("genética", "g", 70, COR)], XE, 680, passo=0.12)
    E.foco(c, t, C["s22.c"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1560, 330, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s22.c"] + 0.3, 0.8))
    E.cursor(c, lerp(1850, 1690, p), lerp(560, 355, p), ep(t, C["s22.c"] + 0.2, 0.4))
    E.frase(c, t, C["s22.d"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, chuva=b_chuva, regra=b_regra, genetica=b_genetica, erro=b_erro, atalho=b_atalho,
              questao=b_questao, resposta=b_resposta, fim=b_fim)
