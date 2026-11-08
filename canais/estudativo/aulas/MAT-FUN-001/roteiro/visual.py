"""Visual — Estudativo · MAT-FUN-001: plano cartesiano, marcar e ler pontos. Primeira aula da trilha Funções.

Linguagem visual da trilha Funções (as próximas aulas copiam daqui):
- x, entrada e domínio = índigo da matéria (ENT); y, saída e imagem = tinta preta (SAI). O eixo x é índigo e o eixo y é preto.
- par ordenado "(x, y)" sempre com o x em índigo e o y em preto (par()); no erro, o par inteiro fica vermelho.
- andar no plano: seta índigo deitada (corredor = x) e depois seta preta em pé (elevador = y), com anda().
- plano sempre na metade direita (PLANO), texto na esquerda; quadrantes como "1º" a "4º", com a região pintada de leve.
Peças locais: eixos() desenha os eixos um de cada vez (o x antes do y), par(), anda(), quad(), pino() do mapa, predio()."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Funções")
COR, CLARO = E.COR_TEXTO, E.CLARO
ENT, SAI = COR, TINTA  # x / entrada / domínio · y / saída / imagem
ARQUIVO_FINAL = "estudativo_MAT-FUN-001_plano_cartesiano_marcar_e_ler_pontos.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("eixos", "marcar", "mapa", "atalho", "questao", "fim"))
BR = "#FFFFFF"
PLANO = (1060, 170, 740, 740)
P = E.Plano(*PLANO, -5, 5, -5, 5)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças desta aula (e da trilha) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))


def eixos(c, t, P, tx, ty=None, tg=None, size=38):
    """plano em etapas: grade em tg, eixo x (índigo) em tx, eixo y (preto) em ty"""
    ty = tx if ty is None else ty
    x, y, w, h = P.caixa
    if tg is not None and t >= tg:
        q = ep(t, tg, 0.8)
        for v in range(int(P.xmin), int(P.xmax) + 1):
            M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
        for v in range(int(P.ymin), int(P.ymax) + 1):
            M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    if t >= tx:
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, ep(t, tx, 0.7))
        E.foco(c, t, tx + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 20, P.oy + 66, 62, "i", ENT, a))
        for i, v in enumerate(range(int(P.xmin), int(P.xmax) + 1)):
            if v == 0:
                continue
            X = P.x(v)
            E.foco(c, t, tx + 0.2 + i * 0.03, 0.4, lambda a, X=X, v=v: (
                M.line(c, X, P.oy - 10, X, P.oy + 10, ENT, a, 4),
                centro(c, E._num(v), X, P.oy + 14 + size, size, "b", TINTA2, a)), sobe=6)
    if t >= ty:
        M.arrow(c, P.ox, y + h + 10, P.ox, y - 44, SAI, 1.0, 6, 24, ep(t, ty, 0.7))
        E.foco(c, t, ty + 0.5, 0.4, lambda a: E.escreve(c, "y", P.ox + 22, y - 18, 62, "i", SAI, a))
        for i, v in enumerate(range(int(P.ymin), int(P.ymax) + 1)):
            if v == 0:
                continue
            Y = P.y(v)
            E.foco(c, t, ty + 0.2 + i * 0.03, 0.4, lambda a, Y=Y, v=v: (
                M.line(c, P.ox - 10, Y, P.ox + 10, Y, SAI, a, 4),
                E.escreve(c, E._num(v), P.ox - 20 - E.larg(E._num(v), "b", size), Y + size * 0.36, size, "b", TINTA2, a)), sobe=6)


def plano(c, t, t0, grade=True):
    eixos(c, t, P, t0, t0, t0 if grade else None)


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto; cores=(cx, cy) troca as duas (ERRADO no erro)"""
    cx_, cy_ = cores or (ENT, SAI)
    partes = (("(", TINTA if not cores else cx_), (xv, cx_), (", ", TINTA if not cores else cx_), (yv, cy_), (")", TINTA if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left", cores=None):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align, cores))


def anda(c, t, t0, P, A, B, cor, d=0.8, largura=10):
    """seta que anda no plano de A até B (em valores)"""
    p = ease_io(prog(t, t0, d))
    if p > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, 0.22, largura * 3.2)  # halo: a seta aparece mesmo sobre o eixo
        M.arrow(c, x0, y0, x1, y1, cor, 1.0, largura, 30, p)


def quad(c, P, q, cor, alfa):
    if alfa <= 0:
        return
    x, y, w, h = P.caixa
    ox, oy = P.ox, P.oy
    r = {1: (ox, y, x + w, oy), 2: (x, y, ox, oy), 3: (x, oy, ox, y + h), 4: (ox, oy, x + w, y + h)}[q]
    c.drawRect(skia.Rect.MakeLTRB(*r), M.paint(cor, alfa))


QC = {1: (3.5, 3.7), 2: (-3.5, 3.7), 3: (-3.5, -3.7), 4: (3.5, -3.7)}


def numeral(c, t, t0, P, q, size=100, cor=None, a=1.0, em=None):
    X, Y = P(*(em or QC[q]))
    E.foco(c, t, t0, 0.5, lambda k: centro(c, f"{q}º", X, Y + size * 0.36, size, "g", cor or COR, k * a))


def anel(c, t, t0, X, Y, cor=None):
    """anel que se abre num ponto: chama a atenção para ele"""
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def pino(c, X, Y, cor, nome=None, a=1.0, lado=1, size=42):
    """alfinete de mapa com a ponta em (X, Y)"""
    if a <= 0:
        return
    r, cy = 26, Y - 58
    p = skia.Path()
    p.addCircle(X, cy, r)
    tri = skia.Path()
    tri.moveTo(X - r * 0.86, cy + r * 0.5); tri.lineTo(X, Y); tri.lineTo(X + r * 0.86, cy + r * 0.5); tri.close()
    p = skia.Op(p, tri, skia.PathOp.kUnion_PathOp)
    c.drawPath(p, M.paint(cor, a))
    c.drawCircle(X, cy, 10, M.paint(BR, a))
    if nome:
        if lado > 0:
            E.escreve(c, nome, X + r + 12, cy + size * 0.36, size, "b", cor, a)
        else:
            E.escreve(c, nome, X - r - 12 - E.larg(nome, "b", size), cy + size * 0.36, size, "b", cor, a)


def pino_em(c, t, t0, P, x, y, cor, nome, lado=1):
    X, Y = P(x, y)
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        c.save(); c.translate(X, Y); c.scale(k, k); c.translate(-X, -Y)
        pino(c, X, Y, cor, nome, 1.0, lado)
        c.restore()


def guia(c, t, t0, A, B, cor, d=0.7):
    """tracejado de leitura, de A até B (em valores)"""
    p = ease_io(prog(t, t0, d))
    if p > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, x1, y1, cor, 1.0, 6, dash=E.TRACO, progress=p)


def marca_eixo(c, t, t0, v, eixo, cor):
    """valor lido num eixo, numa pílula"""
    if eixo == "x":
        X, Y = P.x(v), P.oy + 52
    else:
        X, Y = P.ox - 44, P.y(v)
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, E._num(v), X, Y, 44, "g", fundo=cor, a=a))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano(c, t, C["s01"])
        par_em(c, t, C["s01.a"], "3", "−2", XE, 380, 130)
        E.ponto(c, t, C["s01.a"] + 0.3, P, 3, -2, cor=COR, r=16)
        par_em(c, t, C["s01.b"], "−2", "3", XE, 580, 130)
        E.ponto(c, t, C["s01.b"] + 0.3, P, -2, 3, cor=TINTA, r=16)
        if t >= C["s01.c"]:
            (x0, y0), (x1, y1) = P(3, -2), P(-2, 3)
            M.line(c, x0, y0, x1, y1, TINTA2, 0.8, 4, dash=E.TRACO, progress=ease_io(prog(t, C["s01.c"], 0.8)))
        E.frase(c, t, C["s01.c"], [("mesmos", "i", 72), ("números,", "i", 72)], XE, 780)
        E.frase(c, t, C["s01.c"] + 0.6, [("lugares", "i", 72), ("diferentes", "g", 66, COR)], XE, 870)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.c"] - 0.2, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.c"] - 0.2, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 330)
        E.frase(c, t, C["s02.a"] + 1.0, [("marcar", "g", 130), ("e", "i", 120), ("ler", "g", 130)], XE, 480)
        E.frase(c, t, C["s02.a"] + 1.6, [("qualquer", "i", 96), ("ponto", "i", 96, COR)], XE, 600)
        E.frase(c, t, C["s02.b"], [("+", "g", 96, COR), ("o", "i", 96), ("quadrante", "g", 110)], XE, 760)
        E.foco(c, t, C["s02.c"] + 0.2, 0.5, lambda a: (E.escreve(c, "+ atalho", 1320, 525, 84, "g", BR, a),
                                                      E.escreve(c, "de prova", 1340, 610, 84, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("uma", "i", 84, TINTA, C["s03.a"]), ("coisa", "g", 80, COR, C["s03.a"] + 0.2), ("só", "i", 84, TINTA, C["s03.a"] + 0.4)],
           W / 2, 220, "center")
    E.frase(c, t, C["s03.b"], [("a", "i", 120), ("reta", "g", 120, COR), ("numérica", "g", 120, COR)], W / 2, 420, "center")
    vx = E.reta(c, t, C["s03.b"] + 0.3, 330, 1590, 800, -5, 5, list(range(-5, 6)), E._num, size=46)
    t1, t2 = C["s03.b"] + 1.4, C["s03.b"] + 2.9
    E.frase(c, t, t1, [("o", "i", 64), ("sinal", "g", 64, COR), ("diz", "i", 64), ("o", "i", 64), ("lado", "g", 64)], 330, 580)
    E.frase(c, t, t2, [("o", "i", 64), ("número", "g", 60, COR), ("diz", "i", 60), ("quantos", "i", 60), ("passos", "g", 60)], 1010, 580)
    if t >= t1:
        p = ep(t, t1, 0.6)
        M.arrow(c, vx(0), 700, vx(-3), 700, COR, p, 8, 26, p)
        M.arrow(c, vx(0), 700, vx(3), 700, COR, p, 8, 26, p)
        E.foco(c, t, t1 + 0.2, 0.4, lambda a: (centro(c, "−", vx(-4), 718, 80, "g", COR, a), centro(c, "+", vx(4), 718, 80, "g", COR, a)))
    for i in range(3):
        E.foco(c, t, t2 + 0.4 + 0.25 * i, 0.3, lambda a, i=i: E.bola(c, vx(-1 - i), 800, 22, a=a), blur=0)


# ---------------- eixos ----------------
def b_eixos(c, t, C, b):
    eixos(c, t, P, C["s04.b"], C["s04.c"], C["s05.d"])
    if t >= C["s04.c"]:
        anel(c, t, C["s04.c"] + 0.9, P.ox, P.oy)
    x, y, w, h = P.caixa
    for k, y0, y1, s, ty in (("s04.d", y, P.oy, "+", y + 60), ("s04.e", P.oy, y + h, "−", y + h - 40)):
        q = pulso(t, C[k], 2.4) if k == "s04.d" else ep(t, C[k], 0.3) * (1 - ep(t, C["s05"] - 0.3, 0.4))
        if q > 0:
            M.rrect(c, P.ox - 34, y0 + 6, 68, y1 - y0 - 12, 34, TINTA, 0.12 * q)
            centro(c, s, P.ox + 70, ty, 90, "g", TINTA, q)

    def s04():
        E.frase(c, t, C["s04.a"], [("duas", "i", 84), ("retas", "g", 76), ("numéricas", "g", 76)], XE, 300)
        E.frase(c, t, C["s04.b"], [("uma", "i", 80), ("deitada", "g", 80, ENT)], XE, 460)
        E.frase(c, t, C["s04.c"], [("outra", "i", 80), ("em", "g", 80), ("pé", "g", 80)], XE, 580)
        E.frase(c, t, C["s04.d"], [("+", "g", 80), ("para", "i", 72), ("cima", "g", 72)], XE, 740)
        E.frase(c, t, C["s04.e"], [("−", "g", 80), ("para", "i", 72), ("baixo", "g", 72)], XE, 850)
    E.saida(c, t, C["s05"] - 0.1, s04)
    if t < C["s05"]:
        return
    q = pulso(t, C["s05.a"])
    if q > 0:
        M.line(c, x - 10, P.oy, x + w + 20, P.oy, ENT, 0.25 * q, 26)
    q = pulso(t, C["s05.b"])
    if q > 0:
        M.line(c, P.ox, y + h + 10, P.ox, y - 20, SAI, 0.2 * q, 26)
    E.frase(c, t, C["s05.a"], [("eixo", "i", 90), ("x", "g", 110, ENT)], XE, 320)
    E.frase(c, t, C["s05.b"], [("eixo", "i", 90), ("y", "g", 110, SAI)], XE, 460)
    E.frase(c, t, C["s05.c"], [("a", "i", 90), ("origem", "g", 96, COR), ("(0,", "i", 70, TINTA2), ("0)", "i", 70, TINTA2)], XE, 600)
    if t >= C["s05.c"]:
        anel(c, t, C["s05.c"], P.ox, P.oy)
        k = ease_back(prog(t, C["s05.c"], 0.45))
        c.drawCircle(P.ox, P.oy, 16 * k, M.paint(COR))
    E.frase(c, t, C["s05.d"], [("plano", "g", 104, COR)], XE, 780)
    E.frase(c, t, C["s05.d"] + 0.3, [("cartesiano", "g", 104, COR)], XE, 900)


# ---------------- endereço ----------------
def b_endereco(c, t, C, b):
    def s06():
        cx, y = W / 2, 520
        E.frase(c, t, C["s06.a"], [("dois", "i", 76), ("números", "i", 76), ("entre", "i", 76), ("parênteses", "g", 70, COR)], cx, 220, "center")
        E.foco(c, t, C["s06.a"], 0.5, lambda a: (centro(c, "(", cx - 380, y, 280, "g", TINTA, a), centro(c, ",", cx, y, 280, "g", TINTA, a),
                                                 centro(c, ")", cx + 380, y, 280, "g", TINTA, a)))
        for k, sx, letra, cor, l1 in (("s06.b", cx - 190, "x", ENT, "direita ou esquerda"), ("s06.c", cx + 190, "y", SAI, "cima ou baixo")):
            if t < C[k]:
                E.foco(c, t, C["s06.a"] + 0.3, 0.5, lambda a, sx=sx: E.caixa_pontilhada(c, sx - 90, y - 190, 180, 220, a))
            E.foco(c, t, C[k], 0.5, lambda a, sx=sx, letra=letra, cor=cor: centro(c, letra, sx, y, 280, "i", cor, a))
            E.foco(c, t, C[k] + 0.2, 0.5, lambda a, sx=sx, cor=cor, k=k: E.pilula(c, "1º" if k == "s06.b" else "2º", sx, y + 130, 46, "g", fundo=cor, a=a))
            E.foco(c, t, C[k] + 0.5, 0.5, lambda a, sx=sx, cor=cor, l1=l1: centro(c, l1, sx, y + 260, 58, "i", cor, a))
            if t >= C[k] + 0.6:
                p = ep(t, C[k] + 0.6, 0.5)
                if k == "s06.b":
                    M.arrow(c, sx, y + 340, sx - 160, y + 340, cor, p, 7, 22, p)
                    M.arrow(c, sx, y + 340, sx + 160, y + 340, cor, p, 7, 22, p)
                else:
                    M.arrow(c, sx, y + 345, sx, y + 296, cor, p, 7, 22, p)
                    M.arrow(c, sx, y + 345, sx, y + 410, cor, p, 7, 22, p)
        E.frase(c, t, C["s06.d"], [("as", "i", 84), ("coordenadas", "g", 90, COR)], cx, 1010, "center")
    E.saida(c, t, C["s07"] - 0.1, s06)
    if t >= C["s07"]:
        predio(c, t, C)


def predio(c, t, C):
    x0, x1, y0, y1 = 1080, 1720, 230, 930
    a = ep(t, C["s07"], 0.5)
    M.rrect(c, x0, y0, x1 - x0, y1 - y0, 10, BR, a)
    c.drawRect(skia.Rect.MakeLTRB(x0, y0, x1, y1), M.paint(TINTA, a, stroke=6))
    andares = 4
    hh = (y1 - y0) / andares
    for i in range(1, andares):
        M.line(c, x0, y0 + hh * i, x1, y0 + hh * i, FIO, a, 4)
    for i in range(andares):
        for j in range(3):
            M.rrect(c, x0 + 50 + j * 140, y0 + hh * i + 40, 90, 70, 8, FIO, a)
    # poço do elevador à direita
    ex = x1 - 130
    c.drawRect(skia.Rect.MakeLTRB(ex, y0, x1, y1), M.paint(TINTA, 0.06 * a))
    M.line(c, ex, y0, ex, y1, TINTA, a, 4, dash=E.TRACO)
    yc = y1 - hh / 2 + 40
    pa = ep(t, C["s07.a"], 0.9)
    M.arrow(c, x0 + 40, yc, ex + 50, yc, ENT, pa, 14, 40, pa)
    pb = ep(t, C["s07.b"], 0.9)
    M.arrow(c, ex + 65, yc, ex + 65, y0 + 70, SAI, pb, 14, 40, pb)
    E.frase(c, t, C["s07.a"], [("1º", "g", 96, ENT), ("corredor", "g", 96)], XE, 380)
    E.frase(c, t, C["s07.a"] + 2.6, [("x", "g", 80, ENT), ("deitado", "i", 76, ENT)], XE + 110, 490)
    E.frase(c, t, C["s07.b"], [("2º", "g", 96), ("elevador", "g", 96)], XE, 680)
    E.frase(c, t, C["s07.b"] + 3.2, [("y", "g", 80), ("em", "i", 76), ("pé", "i", 76)], XE + 110, 790)


# ---------------- marcar ----------------
def passo_txt(c, t, t0, n, txt, cor, y):
    E.linha(c, t, [(n, "g", 80, cor, t0), (txt.split()[0], "i", 66, TINTA, t0 + 0.15)] +
            [(w, "g" if i == len(txt.split()) - 2 else "i", 66, cor if i == len(txt.split()) - 2 else TINTA, t0 + 0.3 + 0.12 * i)
             for i, w in enumerate(txt.split()[1:])], XE, y)


def b_marcar(c, t, C, b):
    plano(c, t, C["s08"] - 3)
    # ponto 1: (3, −2)
    def ida1():
        anda(c, t, C["s08.c"], P, (0, 0), (3, 0), ENT)
        anda(c, t, C["s08.d"], P, (3, 0), (3, -2), SAI)
    E.saida(c, t, C["s09"], ida1)
    if t >= C["s08.b"]:
        anel(c, t, C["s08.b"], P.ox, P.oy)
    E.ponto(c, t, C["s08.e"], P, 3, -2, cor=COR, r=17)
    E.foco(c, t, C["s08.e"] + 0.2, 0.4, lambda a: par(c, "3", "−2", *P(3.3, -2.9), 52, a, "center"))

    def txt1():
        par_em(c, t, C["s08.a"], "3", "−2", XE, 320, 120)
        E.frase(c, t, C["s08.b"], [("saia", "i", 66), ("da", "i", 66), ("origem", "g", 66, COR)], XE, 450)
        passo_txt(c, t, C["s08.c"], "3", "para a direita", ENT, 570)
        passo_txt(c, t, C["s08.d"], "2", "para baixo", SAI, 680)
    E.saida(c, t, C["s09"] - 0.1, txt1)
    if t < C["s09"]:
        return
    # ponto 2: (−1, 4)
    def ida2():
        anda(c, t, C["s09.b"], P, (0, 0), (-1, 0), ENT)
        anda(c, t, C["s09.c"], P, (-1, 0), (-1, 4), SAI)
    E.saida(c, t, C["s09.d"], ida2)
    E.ponto(c, t, C["s09.c"] + 0.8, P, -1, 4, cor=COR, r=17)
    E.foco(c, t, C["s09.c"] + 1.0, 0.4, lambda a: par(c, "−1", "4", *P(-2.6, 4.3), 52, a, "center"))

    def txt2():
        par_em(c, t, C["s09.a"], "−1", "4", XE, 320, 120)
        passo_txt(c, t, C["s09.b"], "1", "para a esquerda", ENT, 450)
        passo_txt(c, t, C["s09.c"], "4", "para cima", SAI, 560)
    E.saida(c, t, C["s09.d"] - 0.1, txt2)
    if t < C["s09.d"]:
        return
    anda(c, t, C["s09.d"] + 1.6, P, (0, 0), (0, 3), SAI)
    q = ep(t, C["s09.e"], 0.4)
    if q > 0:
        x, y, w, h = P.caixa
        M.line(c, P.ox, y + h, P.ox, y - 20, SAI, 0.18 * q, 26)
    E.ponto(c, t, C["s09.e"], P, 0, 3, cor=COR, r=17)
    E.foco(c, t, C["s09.e"] + 0.2, 0.4, lambda a: par(c, "0", "3", *P(1.4, 3.1), 52, a, "center"))
    par_em(c, t, C["s09.d"], "0", "3", XE, 320, 120)
    E.frase(c, t, C["s09.d"] + 1.0, [("x", "g", 66, ENT), ("=", "g", 66, ENT), ("0:", "g", 66, ENT), ("não", "i", 66), ("anda", "i", 66)], XE, 450)
    E.frase(c, t, C["s09.d"] + 1.8, [("só", "i", 66), ("sobe", "g", 66)], XE, 550)
    E.frase(c, t, C["s09.e"], [("em", "i", 66), ("cima", "i", 66), ("do", "i", 66), ("eixo", "i", 66), ("y", "g", 76)], XE, 700)


# ---------------- quadrantes ----------------
def seta_giro(c, t, t0, P, r=150, d=1.4):
    p = ease_io(prog(t, t0, d))
    if p <= 0:
        return
    ini, varre = -60, -240 * p
    E.arco(c, P.ox, P.oy, r, ini, varre, COR, 7)
    if p > 0.05:
        ang = math.radians(ini + varre)
        X, Y = P.ox + r * math.cos(ang), P.oy + r * math.sin(ang)
        tg = ang - math.pi / 2  # tangente no sentido anti-horário da tela
        pth = skia.Path()
        pth.moveTo(X + 30 * math.cos(tg), Y + 30 * math.sin(tg))
        pth.lineTo(X + 18 * math.cos(tg + 2.2), Y + 18 * math.sin(tg + 2.2))
        pth.lineTo(X + 18 * math.cos(tg - 2.2), Y + 18 * math.sin(tg - 2.2))
        pth.close()
        c.drawPath(pth, M.paint(COR))


def b_quadrantes(c, t, C, b):
    q0 = ep(t, C["s10.a"], 0.6)
    for q in (1, 2, 3, 4):
        quad(c, P, q, COR, 0.05 * q0)
    hl = {1: "s10.b", 2: "s10.d", 3: "s10.e", 4: "s10.f"}
    for q, k in hl.items():
        quad(c, P, q, COR, 0.12 * pulso(t, C[k], 1.2))
    quad(c, P, 4, COR, 0.16 * ep(t, C["s11.b"], 0.4))
    quad(c, P, 2, COR, 0.16 * ep(t, C["s11.d"], 0.4))
    plano(c, t, C["s10"] - 3)
    E.saida(c, t, C["s11"] - 0.1, lambda: seta_giro(c, t, C["s10.c"], P))
    apaga = 1 - 0.55 * ep(t, C["s11"], 0.5)
    for q, k in hl.items():
        numeral(c, t, C[k], P, q, 110, a=apaga)

    def s10():
        E.frase(c, t, C["s10.a"], [("4", "g", 180, COR), ("quadrantes", "i", 96)], XE, 380)
        E.frase(c, t, C["s10.b"], [("começa", "i", 72), ("em", "i", 72), ("cima,", "i", 72), ("à", "i", 72), ("direita", "g", 66)], XE, 540)
        E.frase(c, t, C["s10.c"], [("e", "i", 72), ("gira", "i", 72), ("ao", "i", 72), ("contrário", "g", 66, COR)], XE, 660)
        E.frase(c, t, C["s10.c"] + 0.9, [("do", "i", 72), ("relógio", "g", 66, COR)], XE, 760)
    E.saida(c, t, C["s11"] - 0.1, s10)
    if t < C["s11"]:
        return
    E.ponto(c, t, C["s11.a"], P, 3, -2, cor=COR, r=17)
    E.ponto(c, t, C["s11.c"], P, -1, 4, cor=COR, r=17)
    E.ponto(c, t, C["s11.e"], P, 0, 3, cor=TINTA, r=17)
    if t >= C["s11.e"]:
        anel(c, t, C["s11.e"] + 0.3, *P(0, 3), TINTA)
    par_em(c, t, C["s11.a"], "3", "−2", XE, 320, 96)
    E.frase(c, t, C["s11.b"], [("4º", "g", 80, COR), ("quadrante", "i", 72)], XE, 430)
    par_em(c, t, C["s11.c"], "−1", "4", XE, 590, 96)
    E.frase(c, t, C["s11.d"], [("2º", "g", 80, COR), ("quadrante", "i", 72)], XE, 700)
    par_em(c, t, C["s11.e"], "0", "3", XE, 860, 96)
    E.frase(c, t, C["s11.e"] + 0.6, [("na", "i", 72), ("divisa", "g", 72)], XE + 330, 860)
    E.frase(c, t, C["s11.e"] + 2.4, [("sem", "i", 60, TINTA2), ("quadrante", "i", 60, TINTA2)], XE, 950)


# ---------------- mapa ----------------
def praca(c, t, t0):
    """a praça é a origem: um quadradinho cheio no cruzamento, com o nome acima à direita (não cobre os números dos eixos)"""
    k = ease_back(prog(t, t0, 0.5))
    if k > 0:
        M.rrect(c, P.ox - 20 * k, P.oy - 20 * k, 40 * k, 40 * k, 8, TINTA)
        c.drawCircle(P.ox, P.oy, 8 * k, M.paint(BR))
    E.foco(c, t, t0 + 0.2, 0.4, lambda a: E.escreve(c, "praça", P.ox + 30, P.oy - 30, 44, "b", TINTA, a))


def mapa(c, t, t0, escola=True):
    plano(c, t, t0)
    praca(c, t, t0 + 0.4)
    if escola:
        pino_em(c, t, t0 + 0.6, P, -4, 2, COR, "escola", -1)


def b_mapa(c, t, C, b):
    plano(c, t, C["s12"])
    praca(c, t, C["s12.b"])
    q = ep(t, C["s12.c"], 0.4) * (1 - ep(t, C["s13"], 0.5))
    if q > 0:
        c.drawRect(skia.Rect.MakeLTRB(P.x(1), P.y(-1), P.x(2), P.y(-2)), M.paint(COR, 0.35 * q))
        E.chave(c, P.x(1), P.x(2), P.y(-2) + 4, TINTA, q, 20, 5)
        centro(c, "1 quadra", P.x(1.5), P.y(-2) + 74, 40, "b", TINTA, q)
    pino_em(c, t, C["s12.d"], P, -4, 2, COR, "escola", -1)

    def s12():
        E.frase(c, t, C["s12.a"], [("ler", "g", 110, COR), ("o", "i", 96), ("endereço", "i", 96)], XE, 340)
        E.frase(c, t, C["s12.b"], [("praça", "g", 76), ("=", "i", 76), ("origem", "i", 76)], XE, 500)
        E.frase(c, t, C["s12.c"], [("1", "g", 76, COR), ("quadradinho", "i", 72), ("=", "i", 72)], XE, 620)
        E.frase(c, t, C["s12.c"] + 0.6, [("1", "g", 76, COR), ("quadra", "g", 76)], XE, 720)
        E.frase(c, t, C["s12.d"], [("onde", "i", 84), ("está", "i", 84), ("a", "i", 84), ("escola?", "g", 84, COR)], XE, 880)
    E.saida(c, t, C["s13"] - 0.1, s12)
    if t < C["s13"]:
        return
    guia(c, t, C["s13.a"], (-4, 2), (-4, 0), ENT)
    marca_eixo(c, t, C["s13.b"], -4, "x", ENT)
    guia(c, t, C["s13.c"], (-4, 2), (0, 2), SAI)
    marca_eixo(c, t, C["s13.d"], 2, "y", SAI)
    E.frase(c, t, C["s13.a"], [("desça", "i", 68), ("até", "i", 68), ("o", "i", 68), ("eixo", "i", 68), ("x", "g", 80, ENT)], XE, 330)
    E.frase(c, t, C["s13.b"], [("x", "g", 90, ENT), ("=", "g", 90, ENT), ("−4", "g", 90, ENT)], XE + 60, 440)
    E.frase(c, t, C["s13.c"], [("de", "i", 68), ("lado", "i", 68), ("até", "i", 68), ("o", "i", 68), ("eixo", "i", 68), ("y", "g", 80)], XE, 590)
    E.frase(c, t, C["s13.d"], [("y", "g", 90), ("=", "g", 90), ("2", "g", 90)], XE + 60, 700)
    par_em(c, t, C["s13.e"], "−4", "2", XE, 870, 110)
    E.frase(c, t, C["s13.e"] + 1.5, [("2º", "g", 60, COR), ("quadrante", "i", 60)], XE, 960)


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano(c, t, C["s14"] - 3)
    quad(c, P, 2, ERRADO, 0.12 * ep(t, C["s14.d"], 0.5))
    if t >= C["s14.d"]:
        numeral(c, t, C["s14.d"], P, 2, 100, ERRADO, em=(-3.6, 1.3))
    anda(c, t, C["s14.b"], P, (0, 0), (0, 3), ERRADO)
    anda(c, t, C["s14.b"] + 1.4, P, (0, 3), (-2, 3), ERRADO)
    E.ponto(c, t, C["s14.c"], P, -2, 3, cor=ERRADO, r=17)
    E.foco(c, t, C["s14.c"] + 0.2, 0.4, lambda a: par(c, "−2", "3", *P(-2.6, 3.7), 52, a, "center", (ERRADO, ERRADO)))
    # o certo, lá longe
    anda(c, t, C["s14.e"], P, (0, 0), (3, 0), CERTO, 0.6)
    anda(c, t, C["s14.e"] + 0.6, P, (3, 0), (3, -2), CERTO, 0.6)
    E.ponto(c, t, C["s14.d"] + 1.2, P, 3, -2, cor=CERTO, r=17)
    E.foco(c, t, C["s14.d"] + 1.4, 0.4, lambda a: par(c, "3", "−2", *P(3.3, -2.9), 52, a, "center", (CERTO, CERTO)))

    E.frase(c, t, C["s14.a"], [("o", "i", 84), ("erro:", "i", 84), ("começar", "g", 76, ERRADO)], XE, 300)
    E.frase(c, t, C["s14.a"] + 0.6, [("pelo", "i", 84), ("elevador", "g", 76, ERRADO)], XE, 400)
    E.frase(c, t, C["s14.b"], [("sobe", "i", 64), ("3,", "g", 64, ERRADO)], XE, 520)
    E.frase(c, t, C["s14.b"] + 1.4, [("anda", "i", 64), ("2", "g", 64, ERRADO), ("para", "i", 64), ("a", "i", 64), ("esquerda", "i", 64)], XE, 600)
    par_em(c, t, C["s14.c"], "−2", "3", XE, 720, 96, cores=(ERRADO, ERRADO))
    E.frase(c, t, C["s14.e"], [("primeiro", "i", 72), ("o", "i", 72), ("x,", "g", 80, ENT)], XE, 860)
    E.frase(c, t, C["s14.e"] + 0.9, [("depois", "i", 72), ("o", "i", 72), ("y", "g", 80)], XE, 950)


# ---------------- atalho (palco escuro) ----------------
SINAIS = {1: ("+", "+"), 2: ("−", "+"), 3: ("−", "−"), 4: ("+", "−")}


def b_atalho(c, t, C, b):
    palco(c, t)

    def s15():
        E.frase(c, t, C["s15"], ps("agora, o atalho", "i", 80, CLARO), W / 2, 170, "center")
        E.frase(c, t, C["s15.a"], [("o", "i", 96, CLARO), ("quadrante", "g", 96, BR), ("pelos", "i", 96, CLARO), ("sinais", "g", 96, BR)],
                W / 2, 310, "center")
        cx, cy = W / 2, 720
        a = ep(t, C["s15.a"] + 0.6, 0.6)
        M.arrow(c, cx - 560, cy, cx + 580, cy, CLARO, a, 5, 20, a)
        M.arrow(c, cx, cy + 280, cx, cy - 300, BR, a, 5, 20, a)
        pos = {1: (cx + 300, cy - 140), 2: (cx - 300, cy - 140), 3: (cx - 300, cy + 170), 4: (cx + 300, cy + 170)}
        for q, k in ((1, "s15.b"), (2, "s15.c"), (3, "s15.d"), (4, "s15.e")):
            X, Y = pos[q]
            sx, sy = SINAIS[q]

            def d(a, X=X, Y=Y, q=q, sx=sx, sy=sy):
                centro(c, f"{q}º", X, Y - 92, 52, "i", CLARO, a)
                par(c, sx, sy, X, Y + 40, 110, a, "center", (CLARO, BR))
            E.foco(c, t, C[k], 0.5, d)
    E.saida(c, t, C["s16"] - 0.1, s15)
    if t < C["s16"]:
        return
    E.frase(c, t, C["s16.a"], [("sinal", "i", 80, CLARO), ("do", "i", 80, CLARO), ("x", "g", 96, CLARO)], XE, 280)
    E.frase(c, t, C["s16.a"] + 0.8, [("direita", "g", 72, BR), ("ou", "i", 72, CLARO), ("esquerda", "g", 72, BR)], 900, 280)
    E.frase(c, t, C["s16.b"], [("sinal", "i", 80, CLARO), ("do", "i", 80, CLARO), ("y", "g", 96, BR)], XE, 440)
    E.frase(c, t, C["s16.b"] + 0.8, [("cima", "g", 72, BR), ("ou", "i", 72, CLARO), ("baixo", "g", 72, BR)], 900, 440)
    for yy, k in ((256, "s16.a"), (416, "s16.b")):
        p = ep(t, C[k] + 0.5, 0.5)
        M.arrow(c, 640, yy, 820, yy, CLARO, p, 5, 18, p)
    E.frase(c, t, C["s16.c"], [("não", "g", 84, ERRADO), ("compensa", "i", 84, CLARO), ("com", "i", 84, CLARO), ("zero", "g", 84, BR)], W / 2, 680, "center")
    E.foco(c, t, C["s16.d"], 0.5, lambda a: par(c, "0", "3", 520, 860, 96, a, "center", (CLARO, BR)))
    E.frase(c, t, C["s16.d"] + 0.3, [("no", "i", 76, CLARO), ("eixo:", "i", 76, CLARO), ("sem", "g", 76, BR), ("quadrante", "g", 76, BR)], 740, 860)


# ---------------- questão ----------------
def b_questao(c, t, C, b):
    mapa(c, t, C["s17"])
    pino_em(c, t, C["s17.c"], P, 2, -4, TINTA, "posto")
    E.foco(c, t, C["s17.c"] + 0.3, 0.4, lambda a: E.pilula(c, "?", P.x(2), P.y(-4) - 150, 44, "g", a=a))
    E.frase(c, t, C["s17"], ps("hora de testar", "i", 72, COR), XE, 190)
    E.frase(c, t, C["s17.a"], [("farmácia", "g", 72)], XE, 310)
    par_em(c, t, C["s17.a"] + 0.4, "−3", "−1", XE + 330, 310, 80)
    E.frase(c, t, C["s17.b"], [("em", "i", 68), ("que", "i", 68), ("quadrante?", "g", 66, COR)], XE, 410)
    E.frase(c, t, C["s17.c"], [("posto:", "g", 72), ("o", "i", 68), ("ponto", "i", 68), ("na", "i", 68), ("tela", "i", 68)], XE, 540)
    E.frase(c, t, C["s17.d"], [("endereço", "g", 66, COR), ("e", "i", 68), ("quadrante?", "g", 66, COR)], XE, 640)
    if t >= C["s18"]:
        E.relogio(c, t, C["s18.a"], cx=560, cy=790, r=90)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    mapa(c, t, C["s19"] - 3)
    quad(c, P, 3, COR, 0.16 * ep(t, C["s19.b"], 0.5))
    quad(c, P, 4, COR, 0.16 * ep(t, C["s19.f"], 0.5))
    pino_em(c, t, C["s19"] - 3, P, 2, -4, TINTA, "posto")
    E.ponto(c, t, C["s19.b"], P, -3, -1, cor=COR, r=17)
    E.foco(c, t, C["s19.b"] + 0.2, 0.4, lambda a: centro(c, "farmácia", P.x(-3), P.y(-1) + 70, 42, "b", COR, a))
    guia(c, t, C["s19.c"], (2, -4), (2, 0), ENT)
    marca_eixo(c, t, C["s19.c"] + 0.6, 2, "x", ENT)
    guia(c, t, C["s19.d"], (2, -4), (0, -4), SAI)
    marca_eixo(c, t, C["s19.d"] + 0.6, -4, "y", SAI)

    par_em(c, t, C["s19"], "−3", "−1", XE, 260, 90)
    E.frase(c, t, C["s19.a"], [("menos", "i", 66), ("e", "i", 66), ("menos", "i", 66)], XE + 390, 260)
    E.frase(c, t, C["s19.b"], [("3º", "g", 84, COR), ("quadrante", "i", 76)], XE, 380)
    E.frase(c, t, C["s19.c"], [("x", "g", 84, ENT), ("=", "g", 84, ENT), ("2", "g", 84, ENT)], XE, 560)
    E.frase(c, t, C["s19.d"], [("y", "g", 84), ("=", "g", 84), ("−4", "g", 84)], XE, 670)
    par_em(c, t, C["s19.e"], "2", "−4", XE, 840, 110)
    E.foco(c, t, C["s19.f"], 0.5, lambda a: E.pilula(c, "4º quadrante", XE + 640, 805, 52, "g", fundo=CERTO, a=a))


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"], [("resumindo", "i", 92, COR)], W / 2, 210, "center")
        itens = (("s20.a", [("corredor,", "g", 90), ("depois", "i", 90), ("elevador", "g", 90)]),
                 ("s20.b", [("os", "i", 90), ("sinais", "g", 90, COR), ("dizem", "i", 90), ("o", "i", 90), ("quadrante", "g", 90)]))
        for i, (k, partes) in enumerate(itens):
            y = 450 + i * 220
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 300, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 300 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 400, y)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    E.frase(c, t, C["s21"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 300)
    E.frase(c, t, C["s21.a"], [("Função", "g", 170, COR)], XE, 480)
    E.frase(c, t, C["s21.b"], [("cada", "i", 76), ("entrada,", "i", 76), ("uma", "i", 76), ("saída", "g", 72, COR)], XE, 620)
    E.frase(c, t, C["s21.c"], [("como", "i", 64, TINTA2), ("o", "i", 64, TINTA2), ("preço", "i", 64, TINTA2), ("do", "i", 64, TINTA2),
                               ("táxi", "g", 60)], XE, 720)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 920, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, eixos=b_eixos, endereco=b_endereco, marcar=b_marcar, quadrantes=b_quadrantes,
              mapa=b_mapa, erro=b_erro, atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
