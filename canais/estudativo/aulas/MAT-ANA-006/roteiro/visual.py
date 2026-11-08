"""Visual — Estudativo · MAT-ANA-006: ponto de encontro de duas retas (sistema) e os três casos (um ponto, paralelas, a mesma reta).

Segue a linguagem da Geometria Analítica definida em MAT-ANA-001 a 005 (leia os cabeçalhos de lá):
- plano à direita, texto à esquerda; x em índigo, y em preto; pontos dados em tinta;
- AS DUAS RETAS TÊM COR FIXA, e a mesma cor pinta a expressão de cada uma nas contas: a primeira reta é índigo (R1), a segunda
  é tinta preta (R2). Em "2x + 1 = −x + 4", o lado esquerdo é índigo e o direito é preto: dá para ver de que reta veio cada lado;
- o ponto de encontro é o ponto achado (achado(): índigo, maior, com anel), com as guias tracejadas até os eixos;
- degrau da inclinação: andada petróleo (DX), subida âmbar (DY); erro em vermelho, certo em verde; atalho no palco escuro.
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Geometria Analítica")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-ANA-006_ponto_de_encontro_de_duas_retas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("ideia", "geral", "casos", "erro", "atalho", "questao", "fim"))
BR = "#FFFFFF"
ENT, SAI = COR, TINTA
DX, DY, DIST = "#0E9AA7", "#D98A00", E.COR
DX_ESC, DY_ESC = "#3CC7D3", "#FFB833"
R1, R2 = COR, TINTA                               # a primeira reta e a segunda
assert 2 * 1 + 1 == -1 + 4 == 3                   # (1, 3)
assert 3 + 4 - 7 == 0 and 2 * 3 - 4 - 2 == 0 and 7 - 3 == 4   # (3, 4)
assert 2 * 3 + 1 == 7 and -3 + 4 == 1             # o erro: x = 3
assert 3 * 6 + 20 == 5 * 6 + 8 == 38 and 20 - 8 == 12 and 12 / 2 == 6

PA = E.Plano(1140, 150, 630, 720, -2, 5, -1, 7)       # y = 2x + 1 e y = −x + 4
PB = E.Plano(1200, 130, 525, 750, -1, 6, -2, 8)       # x + y − 7 = 0 e 2x − y − 2 = 0
PC = E.Plano(1230, 130, 450, 750, -3, 3, -3, 7)       # y = 2x + 1 e y = 2x + 5
PL = E.Plano(1170, 170, 600, 660, 0, 10, 0, 60)       # locadoras (dias × reais)


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da geometria analítica ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def plano(c, t, t0, P, marcas_x=None, marcas_y=None, size=38, grade=True):
    """E.plano na caixa de P, com o eixo x em índigo (como em Funções)"""
    E.plano(c, t, t0, *P.caixa, P.xmin, P.xmax, P.ymin, P.ymax, marcas_x=marcas_x, marcas_y=marcas_y, size=size,
            nomes=("", "y"), grade=grade)
    if t >= t0:
        x, y, w, h = P.caixa
        p = ep(t, t0, 0.6)
        M.arrow(c, x - 10, P.oy, x + w + 44, P.oy, ENT, 1.0, 6, 24, p)
        E.foco(c, t, t0 + 0.5, 0.4, lambda a: E.escreve(c, "x", x + w + 26, P.oy + 62, 58, "i", ENT, a))


def par(c, xv, yv, x, y, size, a=1.0, align="left", cores=None, est="g"):
    """par ordenado (x, y): x em índigo, y em preto; cores=(cx, cy) troca as duas"""
    cx_, cy_ = cores or (ENT, SAI)
    neutro = TINTA if not cores else cx_
    partes = (("(", neutro), (xv, cx_), (", ", neutro), (yv, cy_), (")", neutro if not cores else cy_))
    w = sum(E.larg(s, est, size) for s, _ in partes) + size * 0.04 * 4
    xx = x - w / 2 if align == "center" else x
    for s, cor in partes:
        E.escreve(c, s, xx, y, size, est, cor, a)
        xx += E.larg(s, est, size) + size * 0.04
    return w


def par_em(c, t, t0, xv, yv, x, y, size, align="left", cores=None):
    E.foco(c, t, t0, 0.5, lambda a: par(c, xv, yv, x, y, size, a, align, cores))


def anda(c, t, t0, P, A, B, cor, d=0.8, largura=10, a=1.0):
    """seta que anda no plano de A até B (em valores) e fica"""
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        (x0, y0), (x1, y1) = P(*A), P(*B)
        M.line(c, x0, y0, lerp(x0, x1, p), lerp(y0, y1, p), cor, 0.22 * a, largura * 3.2)
        M.arrow(c, x0, y0, x1, y1, cor, a, largura, 30, p)


def cateto(c, t, t0, P, A, B, cor, d=0.7, largura=11, a=1.0):
    """lado do triângulo que cresce de A até B (em valores), na cor fixa"""
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor, a, largura, progress=p)


def lado_txt(c, t, t0, P, A, B, s, G, cor, size=56, gap=22, em=0.5):
    """medida ao lado do segmento AB (valores), do lado de fora do triângulo de centro G (valores); em = onde, de A (0) a B (1)"""
    (ax, ay), (bx, by), (gx, gy) = P(*A), P(*B), P(*G)
    ux, uy = E._uni(ax, ay, bx, by)
    nx, ny = uy, -ux
    mx, my = lerp(ax, bx, em), lerp(ay, by, em)
    if (mx + nx - gx) ** 2 + (my + ny - gy) ** 2 < (mx - gx) ** 2 + (my - gy) ** 2:
        nx, ny = -nx, -ny
    E.foco(c, t, t0, 0.4, lambda a: E._cola(c, s, mx, my, nx, ny, gap, size, "g", cor, a))


def nome(c, t, t0, P, x, y, s, lado=(1, -1), size=46, r=15, cor=TINTA):
    """ponto em tinta com o nome ao lado, também em tinta (o índigo fica para o x e para a distância)"""
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=r)
    if s:
        E.foco(c, t, t0 + 0.2, 0.4, lambda a: E._cola(c, s, *P(x, y), lado[0], lado[1], r + 8, size, "b", TINTA, a))


def tiques(c, t, t0, P, xs=(), ys=()):
    """tracinhos sem número nos eixos (quando só alguns valores têm rótulo)"""
    for i, v in enumerate(xs):
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, v=v: M.line(c, P.x(v), P.oy - 10, P.x(v), P.oy + 10, TINTA, a, 4), sobe=6)
    for i, v in enumerate(ys):
        E.foco(c, t, t0 + 0.2 + i * 0.03, 0.4, lambda a, v=v: M.line(c, P.ox - 10, P.y(v), P.ox + 10, P.y(v), TINTA, a, 4), sobe=6)


def canto(c, t, t0, P, V, A, B, cor=TINTA):
    """quadradinho do ângulo reto em V (valores), entre os lados VA e VB"""
    E.angulo(c, t, t0, P(*V), P(*A), P(*B), r=58, cor=cor, preenche=0.12)


def sombra_tri(c, t, t0, P, A, R, B, a=1.0):
    q = ep(t, t0, 0.6) * a
    if q > 0:
        path = skia.Path()
        path.addPoly([P(*A), P(*R), P(*B)], True)
        c.drawPath(path, M.paint(COR, 0.08 * q))


def conta(c, partes, x, y, size, a=1.0, align="left", est="g"):
    """conta numa linha com partes coloridas: partes = [(texto em escrita de fórmula, cor)]. Devolve a largura"""
    ws = [E.formula(None, s, 0, 0, size, est, a=0) for s, _ in partes]
    w = sum(ws)
    xx = x - w / 2 if align == "center" else x - w if align == "right" else x
    if a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return w


def conta_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: conta(c, partes, x, y, size, a, align))


def bola_txt(c, t, t0, s, cx, cy, r, size, cor=None):
    """resposta na esfera"""
    E.foco(c, t, t0, 0.5, lambda a: (E.bola(c, cx, cy, r * ease_back(prog(t, t0, 0.5)), cor, a),
                                     E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")))


def anel(c, t, t0, X, Y, cor=None):
    p = prog(t, t0, 0.9)
    if 0 < p < 1:
        c.drawCircle(X, Y, 14 + 60 * ease_out(p), M.paint(cor or COR, 1 - p, stroke=6))


def pulso(t, t0, d=1.6):
    return ep(t, t0, 0.3) * (1 - ep(t, t0 + d, 0.5))



def seq(c, t, pecas, x, y, size, align="left"):
    """conta que cresce: pecas = [(texto em escrita de fórmula, cor, t0)], cada peça entra no seu instante, uma ao lado da outra"""
    ws = [E.formula(None, s, 0, 0, size, "g", a=0) for s, _, _ in pecas]
    xx = x - sum(ws) / 2 if align == "center" else x
    for (s, cor, ti), w in zip(pecas, ws):
        E.foco(c, t, ti, 0.5, lambda a, s=s, cor=cor, xx=xx: E.formula(c, s, xx, y, size, "g", cor, a))
        xx += w


def seg(c, t, t0, P, A, B, cor=None, d=0.8, largura=7, tracejado=False, a=1.0):
    p = ease_io(prog(t, t0, d))
    if p > 0 and a > 0:
        M.line(c, *P(*A), *P(*B), cor or DIST, a, largura, dash=E.TRACO if tracejado else None, progress=p)


def letra_par(c, t, t0, L, xv, yv, x, y, size, cor=TINTA):
    E.foco(c, t, t0, 0.5, lambda a: (E.escreve(c, L, x, y, size, "g", cor, a),
                                     par(c, xv, yv, x + E.larg(L, "g", size) + size * 0.3, y, size, a)))


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def fra(c, cima, baixo, x, y, size, a=1.0, cc=TINTA, cb=TINTA, barra=TINTA):
    """fração empilhada com cima e baixo em cores próprias; y = linha de base da conta. Devolve a largura"""
    s_ = size * 0.78
    wc, wb = _w(cima, s_), _w(baixo, s_)
    w = max(wc, wb) + size * 0.16
    if a > 0 and c is not None:
        E.formula(c, cima, x + (w - wc) / 2, y - size * 0.46, s_, "g", cc, a)
        E.formula(c, baixo, x + (w - wb) / 2, y + size * 0.46, s_, "g", cb, a)
        b = max(4, size * 0.07)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - size * 0.3 - b / 2, w, b), b / 2, b / 2), M.paint(barra, a))
    return w


def mfr(c, t, t0, cima, baixo, x, y, size, pre="m = ", pos="", cc=DY, cb=DX, cp=None, tpos=None, tinta=TINTA, cpre=None):
    """m = Δy/Δx com o de cima em âmbar e o de baixo em petróleo; pos (o resultado) entra em tpos. Devolve a largura"""
    wp = _w(pre, size) if pre else 0
    wf = fra(None, cima, baixo, 0, 0, size)
    gap = size * 0.12
    E.foco(c, t, t0, 0.5, lambda a: (pre and E.formula(c, pre, x, y, size, "g", cpre or tinta, a), fra(c, cima, baixo, x + wp, y, size, a, cc, cb, tinta)))
    if pos:
        E.foco(c, t, tpos if tpos is not None else t0 + 0.8, 0.5, lambda a: E.formula(c, pos, x + wp + wf + gap, y, size, "g", cp or tinta, a))
    return wp + wf + gap + (_w(pos, size) if pos else 0)




def eqn(c, t, t0, partes, x, y, size, align="left", caixa=None):
    """equação com partes coloridas que entra no cue; caixa = instante da caixa pontilhada em volta"""
    conta_em(c, t, t0, partes, x, y, size, align)
    if caixa is not None and t >= caixa:
        w = conta(None, partes, 0, 0, size, 0)
        x0 = x - w / 2 if align == "center" else x
        p = ep(t, caixa, 0.5)
        E.caixa_pontilhada(c, x0 - 30, y - size * 1.05, w + 60, size * 1.45, p, COR, prog_=p)


def pilula_em(c, t, t0, s, x, y, size=40, fundo=None):
    E.foco(c, t, t0, 0.4, lambda a: E.pilula(c, s, x, y, size, "g", fundo=fundo or COR, a=a))


def reta_eq(c, t, t0, P, A, B, cor=None, largura=7, d=0.8, tracejado=False, a=1.0):
    """reta por A e B (valores), de borda a borda da caixa do plano"""
    if t < t0 or a <= 0:
        return
    (ax, ay), (bx, by) = P(*A), P(*B)
    dx, dy = bx - ax, by - ay
    k = 1e4 / (math.hypot(dx, dy) or 1)
    x, y, w, h = P.caixa
    s = E._corta_caixa(ax - dx * k, ay - dy * k, ax + dx * k, ay + dy * k, x, y, w, h)
    if s:
        M.line(c, *s, cor or DIST, a, largura, dash=E.TRACO if tracejado else None, progress=ease_io(prog(t, t0, d)))




def plano_de(c, t, t0, P, mx, my):
    todos_x = [v for v in range(int(P.xmin), int(P.xmax) + 1) if v != 0 and v not in mx]
    todos_y = [v for v in range(int(P.ymin), int(P.ymax) + 1) if v != 0 and v not in my]
    plano(c, t, t0, P, marcas_x=mx, marcas_y=my, size=36)
    tiques(c, t, t0, P, todos_x, todos_y)


def reta_m(c, t, t0, P, m, n, cor=None, largura=7, tracejado=False, a=1.0, d=0.8):
    """reta y = mx + n"""
    reta_eq(c, t, t0, P, (0, n), (1, m + n), cor, largura, d, tracejado, a)


def achado(c, t, t0, P, x, y, cor=None):
    """o ponto achado: índigo, maior, com anel"""
    cor = cor or DIST
    if t >= t0:
        anel(c, t, t0, *P(x, y), cor)
        anel(c, t, t0 + 0.5, *P(x, y), cor)
    E.ponto(c, t, t0, P, x, y, None, cor=cor, r=19)


def guias(c, t, t0, P, x, y, cor=TINTA2):
    """tracejado do ponto até os dois eixos"""
    q = ease_io(prog(t, t0, 0.6))
    if q > 0:
        X, Y = P(x, y)
        M.line(c, X, Y, X, P.oy, cor, 0.8, 4, dash=E.TRACO, progress=q)
        M.line(c, X, Y, P.ox, Y, cor, 0.8, 4, dash=E.TRACO, progress=q)


def eq_lado(c, t, t0, esq, dir_, x, y, size, ce=R1, cd=R2, align="left"):
    """igualdade com o lado esquerdo de uma reta e o direito da outra"""
    conta_em(c, t, t0, [(esq, ce), (" = ", TINTA), (dir_, cd)], x, y, size, align)


def nota(c, t, t0, s, x, y, size=34, fundo=None):
    pilula_em(c, t, t0, s, x, y, size, fundo or TINTA2)


def sistema2(c, t, t0, l1, l2, x, y, size=70, c1=R1, c2=R2, t2=None):
    """sistema de duas equações, cada linha na cor da sua reta"""
    dy = size * 1.45
    alto, baixo = y - size * 0.95, y + dy + size * 0.35
    meio = (alto + baixo) / 2
    q = ep(t, t0, 0.5)
    if q > 0:
        p = skia.Path()
        k = size * 0.32
        p.moveTo(x, alto); p.cubicTo(x - k, alto, x - k * 0.2, meio - k, x - k, meio)
        p.cubicTo(x - k * 0.2, meio + k, x - k, baixo, x, baixo)
        c.drawPath(p, M.paint(TINTA, q, stroke=max(5, size * 0.07), cap_round=True))
    E.formula_em(c, t, t0, l1, x + size * 0.3, y, size, "g", c1)
    E.formula_em(c, t, t2 if t2 is not None else t0, l2, x + size * 0.3, y + dy, size, "g", c2)


def plano_a(c, t, t0, t1=None, t2=None):
    plano_de(c, t, t0, PA, [-2, 2, 4], [2, 4, 6])
    reta_m(c, t, t0 if t1 is None else t1, PA, 2, 1, R1)
    reta_m(c, t, t0 if t2 is None else t2, PA, -1, 4, R2)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    def cena1():
        plano_a(c, t, C["s01"] + 0.2, C["s01.a"] + 0.3, C["s01.b"] + 0.3)
        X, Y = PA(1, 3)
        if C["s01.c"] <= t < C["s01.e"]:
            E.foco(c, t, C["s01.c"] + 0.3, 0.4, lambda a: E.pilula(c, "?", X + 90, Y - 70, 44, "g", fundo=TINTA2, a=a))
        if C["s01.d"] <= t < C["s01.e"] + 0.3:
            q = ep(t, C["s01.d"], 0.4) * (1 - ep(t, C["s01.e"], 0.3))
            pt = M.paint(TINTA2, q, stroke=4)
            pt.setPathEffect(skia.DashPathEffect.Make([10, 8], 0))
            c.drawCircle(X, Y, 70, pt)
        achado(c, t, C["s01.e"], PA, 1, 3)
        E.foco(c, t, C["s01.e"] + 0.3, 0.4, lambda a: par(c, "1", "3", X + 120, Y + 15, 44, a, "center"))
        eqn(c, t, C["s01.a"], [("y = 2x + 1", R1)], XE, 280, 88)
        eqn(c, t, C["s01.b"], [("y = −x + 4", R2)], XE, 420, 88)
        E.frase(c, t, C["s01.c"], [("em", "i", 76), ("que", "i", 76), ("ponto", "i", 76), ("exato?", "g", 76, COR)], XE, 600)
        E.frase(c, t, C["s01.d"], [("o", "i", 66), ("desenho:", "i", 66), ("palpite", "g", 66, TINTA2)], XE, 760)
        E.frase(c, t, C["s01.e"], [("a", "i", 66), ("conta:", "i", 66), ("certeza", "g", 66, CERTO)], XE, 870)
    E.saida(c, t, C["s02"] - 0.1, cena1)

    if t >= C["s02"]:
        E.foco(c, t, C["s02.b"] - 0.4, 0.7, lambda a: E.bola(c, 1480, 540, 290 * ease_back(prog(t, C["s02.b"] - 0.4, 0.7))), blur=0)
        E.frase(c, t, C["s02.a"], ps("até o fim da aula", "i", 90), XE, 300)
        E.frase(c, t, C["s02.a"] + 1.0, [("o", "i", 110), ("ponto", "g", 120)], XE, 450)
        E.frase(c, t, C["s02.a"] + 1.4, [("de", "i", 110), ("encontro", "g", 120, COR)], XE, 590)
        E.frase(c, t, C["s02.a"] + 2.4, ps("de duas retas", "i", 80, TINTA2), XE, 710)
        E.foco(c, t, C["s02.b"], 0.5, lambda a: (E.escreve(c, "existe?", 1330, 520, 96, "g", BR, a),
                                                E.escreve(c, "antes da conta", 1290, 600, 56, "i", BR, a)))


# ---------------- o que precisa saber ----------------
def b_lembrete(c, t, C, b):
    E.linha(c, t, [("você", "i", 84, TINTA, C["s03"]), ("precisa", "i", 84, TINTA, C["s03"] + 0.2), ("de", "i", 84, TINTA, C["s03"] + 0.4),
                   ("duas", "g", 80, COR, C["s03.a"]), ("coisas", "i", 84, TINTA, C["s03.a"] + 0.2)], W / 2, 200, "center")
    x, w = 230, 1460
    for k, y in (("s03.b", 290), ("s03.c", 590)):
        p = ep(t, C[k], 0.5)
        E.caixa_pontilhada(c, x, y, w, 250, p, prog_=p)
    k = C["s03.b"]
    E.frase(c, t, k, [("a", "i", 66), ("equação", "g", 66, COR), ("reduzida", "g", 66, COR)], 320, 390)
    conta_em(c, t, k + 1.0, [("y = ", TINTA), ("m", COR), ("x + ", TINTA), ("n", TINTA)], 320, 490, 76)
    k = C["s03.c"]
    E.frase(c, t, k, [("sistema", "g", 66, COR), ("por", "i", 66), ("substituição", "g", 66, COR)], 320, 690)
    E.frase(c, t, k + 1.6, ps("uma letra sozinha, troca na outra", "i", 52, TINTA2), 320, 780, passo=0.1)
    sistema2(c, t, k + 0.8, "c + m = 30", "4c + 2m = 100", 1250, 700, 56, TINTA, TINTA)
    E.frase(c, t, C["s04"] - 2.6, ps("faltou alguma? procure no canal", "i", 52, TINTA2), W / 2, 960, "center", passo=0.1)


# ---------------- a ideia ----------------
def b_ideia(c, t, C, b):
    plano_a(c, t, C["s04"])
    X, Y = PA(1, 3)
    if t >= C["s04.a"]:
        k = ease_back(prog(t, C["s04.a"], 0.45))
        c.drawCircle(X, Y, 19 * k, M.paint(DIST))
        anel(c, t, C["s04.a"], X, Y)
        anel(c, t, C["s04.a"] + 0.6, X, Y)
    q = ep(t, C["s04.b"], 0.4)
    if q > 0:  # as duas retas acendem
        M.line(c, *PA(0, 1), *PA(2, 5), R1, 0.2 * q * (1 - ep(t, C["s04.b"] + 2.5, 0.5)), 30)
        M.line(c, *PA(-1, 5), *PA(3, 1), R2, 0.15 * q * (1 - ep(t, C["s04.b"] + 2.5, 0.5)), 30)
    E.frase(c, t, C["s04.a"], [("está", "i", 70), ("nas", "i", 70), ("duas", "g", 70, COR), ("retas", "i", 70)], XE, 270)
    E.frase(c, t, C["s04.a"] + 0.8, ps("ao mesmo tempo", "i", 60, TINTA2), XE, 360)
    E.frase(c, t, C["s04.b"], [("vale", "i", 66), ("nas", "i", 66), ("duas", "g", 66), ("equações", "g", 66)], XE, 500)
    sistema2(c, t, C["s04.c"], "y = 2x + 1", "y = −x + 4", XE + 30, 690, 76)
    E.frase(c, t, C["s04.c"] + 0.4, [("um", "i", 60), ("sistema", "g", 60, COR)], XE + 560, 760)


# ---------------- resolver ----------------
def b_resolver(c, t, C, b):
    plano_a(c, t, C["s05"] - 3)
    if t >= C["s06.c"]:
        q = ease_io(prog(t, C["s06.c"], 0.6))
        x, y, w, h = PA.caixa
        M.line(c, PA.x(1), y + h, PA.x(1), y, COR, 0.7, 4, dash=E.TRACO, progress=q)
        pilula_em(c, t, C["s06.c"] + 0.3, "x = 1", PA.x(1) + 70, PA.y(-0.5), 34, COR)
    if t >= C["s07.e"]:
        guias(c, t, C["s07.e"], PA, 1, 3)
    if t >= C["s07.b"]:
        E.ponto(c, t, C["s07.b"], PA, 1, 3, None, cor=R1, r=14)
    achado(c, t, C["s07.e"], PA, 1, 3)
    E.foco(c, t, C["s07.e"] + 0.3, 0.4, lambda a: par(c, "1", "3", PA.x(1) + 120, PA.y(3) + 15, 44, a, "center"))

    def s05():
        sistema2(c, t, C["s05"], "y = 2x + 1", "y = −x + 4", XE + 30, 270, 70)
        if t >= C["s05.a"]:
            for yy in (270, 270 + 70 * 1.45):
                p = ep(t, C["s05.a"], 0.4)
                E.caixa_pontilhada(c, XE + 40, yy - 62, 60, 80, p, COR, prog_=p)
            E.frase(c, t, C["s05.a"] + 0.4, ps("o y já está sozinho", "i", 50, TINTA2), XE + 520, 330, passo=0.1)
        eq_lado(c, t, C["s05.b"], "2x + 1", "−x + 4", XE, 610, 90)
        E.frase(c, t, C["s05.c"], [("iguale", "g", 66, COR), ("as", "i", 66), ("duas", "i", 66), ("expressões", "i", 66)], XE, 790)
    E.saida(c, t, C["s06"] - 0.1, s05)

    def s06():
        eq_lado(c, t, C["s06"], "2x + 1", "−x + 4", XE, 260, 80)
        E.frase(c, t, C["s06"] + 0.6, ps("a balança", "i", 50, TINTA2), XE + 620, 255)
        eqn(c, t, C["s06.a"], [("3x + 1 = 4", TINTA)], XE, 420, 80)
        nota(c, t, C["s06.a"] + 0.4, "+ x de cada lado", XE + 640, 395)
        eqn(c, t, C["s06.b"], [("3x = 3", TINTA)], XE, 580, 80)
        nota(c, t, C["s06.b"] + 0.4, "− 1 de cada lado", XE + 640, 555)
        eqn(c, t, C["s06.c"], [("x = 1", ENT)], XE, 760, 96, caixa=C["s06.c"] + 0.5)
        nota(c, t, C["s06.c"] + 0.4, "÷ 3", XE + 400, 730)
    if t >= C["s06"]:
        E.saida(c, t, C["s07"] - 0.1, s06)
    if t < C["s07"]:
        return
    eqn(c, t, C["s07"], [("x = 1", ENT)], XE, 250, 76)
    E.frase(c, t, C["s07.a"], ps("em qualquer uma das retas", "i", 54, TINTA2), XE, 360, passo=0.1)
    eqn(c, t, C["s07.b"], [("y = 2 · 1 + 1 = 3", R1)], XE, 470, 76)
    E.frase(c, t, C["s07.c"] - 0.6, ps("confira na outra", "i", 46, TINTA2), XE, 565)
    eqn(c, t, C["s07.c"], [("y = −1 + 4 = 3", R2)], XE, 660, 76)
    pilula_em(c, t, C["s07.d"], "bateu", XE + 680, 630, 44, CERTO)
    E.frase(c, t, C["s07.e"], [("se", "i", 66), ("cruzam", "i", 66), ("em", "i", 66)], XE, 820)
    par_em(c, t, C["s07.e"] + 0.4, "1", "3", XE + 440, 820, 96)


# ---------------- forma geral ----------------
def b_geral(c, t, C, b):
    plano_de(c, t, C["s08"], PB, [2, 4, 6], [-2, 2, 4, 6, 8])
    reta_m(c, t, C["s08.b"] + 0.3, PB, -1, 7, R1)
    reta_m(c, t, C["s08.c"] + 0.3, PB, 2, -2, R2)
    if t >= C["s10.b"]:
        q = ease_io(prog(t, C["s10.b"], 0.6))
        x, y, w, h = PB.caixa
        M.line(c, PB.x(3), y + h, PB.x(3), y, COR, 0.7, 4, dash=E.TRACO, progress=q)
    if t >= C["s10.d"]:
        guias(c, t, C["s10.d"], PB, 3, 4)
    achado(c, t, C["s10.d"], PB, 3, 4)
    E.foco(c, t, C["s10.d"] + 0.3, 0.4, lambda a: par(c, "3", "4", PB.x(3) - 150, PB.y(4) + 15, 42, a, "center"))

    def s08():
        E.frase(c, t, C["s08.a"], [("na", "i", 74), ("forma", "i", 74), ("geral?", "g", 74, COR)], XE, 250)
        eqn(c, t, C["s08.b"], [("x + y − 7 = 0", R1)], XE, 400, 80)
        eqn(c, t, C["s08.c"], [("2x − y − 2 = 0", R2)], XE, 540, 80)
        E.frase(c, t, C["s08.d"], [("isole", "g", 60, COR), ("o", "i", 60), ("y", "g", 60), ("na", "i", 60), ("1ª:", "g", 60)], XE, 700)
        eqn(c, t, C["s08.d"] + 0.8, [("y = 7 − x", R1)], XE, 830, 90, caixa=C["s08.d"] + 1.3)
    E.saida(c, t, C["s09"] - 0.1, s08)
    if t < C["s09"]:
        return
    eqn(c, t, C["s09"], [("y = 7 − x", R1)], XE, 240, 66)
    E.frase(c, t, C["s09"] + 0.4, [("na", "i", 56), ("2ª", "g", 56)], XE + 420, 240)
    eqn(c, t, C["s09.a"], [("2x − ", R2), ("(7 − x)", R1), (" − 2 = 0", R2)], XE, 400, 80)
    E.frase(c, t, C["s09.a"] + 3.0, ps("o menos antes do parêntese troca os sinais", "i", 46, TINTA2), XE, 480, passo=0.08)
    eqn(c, t, C["s09.b"], [("2x ", R2), ("− 7 + x", CERTO), (" − 2 = 0", R2)], XE, 600, 80)

    def s10():
        eqn(c, t, C["s10.a"], [("3x − 9 = 0", TINTA)], XE, 740, 76)
        seq(c, t, [("x = 3", ENT, C["s10.b"])], XE + 520, 740, 76)
        eqn(c, t, C["s10.c"], [("y = 7 − 3 = 4", R1)], XE, 880, 76)
    if t >= C["s10"]:
        s10()
    E.frase(c, t, C["s10.d"], [("se", "i", 60), ("cruzam", "i", 60), ("em", "i", 60)], XE, 1000)
    par_em(c, t, C["s10.d"] + 0.3, "3", "4", XE + 390, 1000, 72)


# ---------------- nem sempre existe ----------------
def b_casos(c, t, C, b):
    def s11_12():
        plano_de(c, t, C["s11"], PC, [-2, 2], [-2, 2, 4, 6])
        reta_m(c, t, C["s11.a"] + 0.3, PC, 2, 1, R1)
        reta_m(c, t, C["s11.b"] + 0.3, PC, 2, 5, R2)
        for i, (x0, n) in enumerate(((0, 1), (-2, 5))):
            y0 = 2 * x0 + n
            t0 = C["s12.a"] + 0.3 * i
            anda(c, t, t0, PC, (x0, y0), (x0 + 1, y0), DX, 0.5, 6)
            anda(c, t, t0 + 0.5, PC, (x0 + 1, y0), (x0 + 1, y0 + 2), DY, 0.5, 6)
        E.frase(c, t, C["s11"], [("toda", "i", 70), ("dupla", "i", 70), ("se", "i", 70), ("cruza?", "g", 70, COR)], XE, 240)
        eqn(c, t, C["s11.a"], [("y = 2x + 1", R1)], XE, 370, 70)
        eqn(c, t, C["s11.b"], [("y = 2x + 5", R2)], XE + 480, 370, 70)

        def s11():
            sz, y = 84, 540
            eq_lado(c, t, C["s11.c"] - 0.8, "2x + 1", "2x + 5", XE, y, sz)
            if t >= C["s11.c"]:
                xa = XE
                xb = XE + _w("2x + 1 = ", sz)
                for xx in (xa, xb):
                    E.risco(c, xx - 6, y + 12, xx + _w("2x", sz) + 6, y - 70, t, C["s11.c"], largura=9)
            eqn(c, t, C["s11.d"], [("1 = 5", ERRADO)], XE, 700, 96)
            E.frase(c, t, C["s11.d"] + 0.8, [("impossível", "g", 66, ERRADO)], XE + 320, 700)
        s11()
        E.frase(c, t, C["s12.a"], [("mesma", "g", 60), ("inclinação:", "i", 60), ("sobe", "i", 60), ("2", "g", 60, DY)], XE, 820)
        E.frase(c, t, C["s12.b"], [("paralelas,", "g", 66, COR), ("nunca", "i", 66), ("se", "i", 66), ("encontram", "i", 66)], XE, 930, passo=0.12)
        E.foco(c, t, C["s12.d"], 0.4, lambda a: E.pilula(c, "sem solução", 1460, PC.caixa[1] - 30, 40, "g", fundo=ERRADO, a=a))
    E.saida(c, t, C["s13"] - 0.1, s11_12)
    if t < C["s13"]:
        return
    E.frase(c, t, C["s13.a"], [("três", "g", 84, COR), ("casos", "i", 84)], W / 2, 210, "center")
    casos = (("s13.b", [("m", COR), (" diferente", TINTA)], "1 ponto", (2, -1), (-0.5, 0)),
             ("s13.c", [("m", COR), (" igual, ", TINTA), ("n", TINTA), (" diferente", TINTA)], "nenhum ponto", (1, 0), (1, -1.6)),
             ("s13.d", [("m", COR), (" igual, ", TINTA), ("n", TINTA), (" igual", TINTA)], "todos os pontos", (1, 0), (1, 0)))
    for i, (k, rot, res, r1, r2) in enumerate(casos):
        cx, cy, L = 360 + i * 600, 560, 190
        q = ep(t, C[k], 0.5)
        if q <= 0:
            continue
        E.caixa_pontilhada(c, cx - 250, cy - 220, 500, 440, q, prog_=q)
        for (m, dn), cor, larg in ((r1, R1, 12), (r2, R2, 6)):
            n = math.hypot(1, m)
            ux, uy = 1 / n, -m / n
            off = dn * 60
            M.line(c, cx - ux * L, cy - uy * L + off, cx + ux * L, cy + uy * L + off, cor, q, larg if i != 2 else (14 if cor == R1 else 5),
                   progress=ease_io(prog(t, C[k] + (0 if cor == R1 else 0.3), 0.6)))
        if i == 0:
            E.foco(c, t, C[k] + 0.6, 0.3, lambda a: (c.drawCircle(cx, cy, 18, M.paint(DIST, a)),), blur=0)
        E.foco(c, t, C[k] + 0.3, 0.4, lambda a, rot=rot, cx=cx: conta(c, rot, cx, 860, 46, a, "center"))
        E.foco(c, t, C[k] + 0.8, 0.4, lambda a, res=res, cx=cx, i=i: E.pilula(c, res, cx, 950, 42, "g", fundo=[COR, ERRADO, TINTA][i], a=a))


# ---------------- erro ----------------
def b_erro(c, t, C, b):
    plano_a(c, t, C["s14"])
    if t >= C["s15.a"]:
        q = ease_io(prog(t, C["s15.a"], 0.6))
        x, y, w, h = PA.caixa
        M.line(c, PA.x(3), y + h, PA.x(3), y, ERRADO, 0.7, 4, dash=E.TRACO, progress=q)
    E.ponto(c, t, C["s15.a"] + 0.3, PA, 3, 7, None, cor=R1, r=15)
    pilula_em(c, t, C["s15.a"] + 0.5, "y = 7", PA.x(3) + 90, PA.y(6.6), 34, R1)
    E.ponto(c, t, C["s15.b"] + 0.3, PA, 3, 1, None, cor=R2, r=15)
    pilula_em(c, t, C["s15.b"] + 0.5, "y = 1", PA.x(3) + 90, PA.y(1.6), 34, R2)
    achado(c, t, C["s15.d"] + 1.0, PA, 1, 3, CERTO)

    def s14():
        E.frase(c, t, C["s14"], [("cuidado", "g", 90, ERRADO)], XE, 240)
        E.frase(c, t, C["s14"] + 1.2, ps("ao juntar os x", "i", 62), XE + 420, 240)
        eq_lado(c, t, C["s14.a"], "2x + 1", "−x + 4", XE, 400, 80)
        E.frase(c, t, C["s14.b"], [("leva", "i", 60), ("o", "i", 60), ("−x", "g", 60, ERRADO), ("com", "i", 60), ("o", "i", 60), ("mesmo", "g", 60, ERRADO),
                                   ("sinal", "i", 60)], XE, 540, passo=0.12)
        eqn(c, t, C["s14.c"], [("2x − x = 3", ERRADO)], XE, 700, 84)
        eqn(c, t, C["s14.d"], [("x = 3", ERRADO)], XE, 860, 96)
    E.saida(c, t, C["s15"] - 0.1, s14)
    if t < C["s15"]:
        return
    E.frase(c, t, C["s15"], [("a", "i", 70), ("conferência", "g", 70, COR), ("denuncia", "i", 70)], XE, 240)
    eqn(c, t, C["s15.a"], [("y = 2 · 3 + 1 = 7", R1)], XE, 400, 76)
    eqn(c, t, C["s15.b"], [("y = −3 + 4 = 1", R2)], XE, 540, 76)
    E.frase(c, t, C["s15.c"], [("7", "g", 66, ERRADO), ("≠", "g", 66, ERRADO), ("1:", "g", 66, ERRADO), ("não", "i", 66), ("é", "i", 66), ("encontro", "g", 66)], XE, 690)
    E.frase(c, t, C["s15.d"], [("some", "g", 66, CERTO), ("x", "g", 66, CERTO), ("de", "i", 66), ("cada", "i", 66), ("lado", "i", 66)], XE, 830)
    eqn(c, t, C["s15.d"] + 0.8, [("3x + 1 = 4", CERTO), ("  →  x = 1", CERTO)], XE, 960, 64)


# ---------------- atalho (palco escuro) ----------------
def b_atalho(c, t, C, b):
    palco(c, t)

    def s16():
        E.frase(c, t, C["s16"], ps("agora, o atalho", "i", 70, CLARO), W / 2, 160, "center")
        E.frase(c, t, C["s16.a"], [("compare", "g", 84, BR), ("os", "i", 84, CLARO), ("m", "g", 84, BR), ("antes", "i", 84, CLARO), ("da", "i", 84, CLARO),
                                   ("conta", "i", 84, CLARO)], W / 2, 300, "center")
        linhas = (("s16.b", [("m", BR), (" diferente", CLARO)], "tem ponto: resolva", CERTO, 480),
                  ("s16.c", [("m", BR), (" igual", CLARO)], "olhe o n", COR, 660),
                  ("s16.d", [("m", BR), (" igual, ", CLARO), ("n", BR), (" diferente", CLARO)], "nenhum ponto, sem conta", ERRADO, 840))
        for k, rot, res, cor, y in linhas:
            E.foco(c, t, C[k], 0.5, lambda a, rot=rot, y=y: conta(c, rot, 900, y, 70, a, "right"))
            p = ep(t, C[k] + 0.4, 0.5)
            if p > 0:
                M.arrow(c, 930, y - 24, 1060, y - 24, CLARO, p, 5, 18, p)
            E.foco(c, t, C[k] + 0.6, 0.4, lambda a, res=res, cor=cor, y=y: E.pilula(c, res, 1100 + (E.larg(res, "g", 44) + 48) / 2, y - 24, 44, "g", fundo=cor, a=a))
    E.saida(c, t, C["s17"] - 0.1, s16)
    if t < C["s17"]:
        return
    E.frase(c, t, C["s17"], [("por", "i", 70, CLARO), ("que", "i", 70, CLARO), ("funciona", "g", 70, BR)], W / 2, 170, "center")
    cx, cy, L = W / 2, 470, 360
    for m, cor, t0 in ((0.25, BR, C["s17.a"]), (1.2, DY_ESC, C["s17.a"] + 0.4)):
        n = math.hypot(1, m)
        ux, uy = 1 / n, -m / n
        p = ease_io(prog(t, t0, 0.8))
        if p > 0:
            M.line(c, cx - ux * L, cy - uy * L, cx + ux * L, cy + uy * L, cor, 1, 8, progress=p)
    if t >= C["s17.b"]:
        k = ease_back(prog(t, C["s17.b"], 0.45))
        c.drawCircle(cx, cy, 20 * k, M.paint(BR))
        anel(c, t, C["s17.b"], cx, cy, BR)
    E.frase(c, t, C["s17.a"], ps("inclinações diferentes", "i", 56, CLARO), 420, 300, "center", passo=0.1)
    E.frase(c, t, C["s17.b"], ps("acabam se cruzando", "i", 56, CLARO), 1500, 640, "center", passo=0.1)
    E.frase(c, t, C["s17.c"], [("não", "g", 66, ERRADO), ("compensa", "i", 70, CLARO), ("quando", "i", 70, CLARO), ("pedem", "i", 70, CLARO), ("o", "i", 70, CLARO),
                               ("ponto", "g", 66, BR)], W / 2, 850, "center")
    E.frase(c, t, C["s17.d"], [("diz", "i", 64, CLARO), ("se", "i", 64, CLARO), ("existe,", "g", 60, BR), ("não", "i", 64, CLARO), ("diz", "i", 64, CLARO),
                               ("onde", "g", 60, BR)], W / 2, 970, "center")


# ---------------- questão ----------------
def plano_l(c, t, t0):
    x, y, w, h = PL.caixa
    E.plano(c, t, t0, x, y, w, h, 0, 10, 0, 60, passo=2, passo_y=10, size=34, nomes=("", ""))
    if t >= t0:
        M.arrow(c, x - 10, PL.oy, x + w + 44, PL.oy, ENT, 1.0, 6, 24, ep(t, t0, 0.6))
    E.foco(c, t, t0 + 0.5, 0.4, lambda a: (E.escreve(c, "dias", x + w - 40, PL.oy + 96, 46, "i", ENT, a),
                                          E.escreve(c, "reais", PL.ox + 24, y - 20, 46, "i", SAI, a)))


def b_questao(c, t, C, b):
    plano_l(c, t, C["s18"])
    reta_m(c, t, C["s18.a"] + 0.4, PL, 3, 20, R1)
    reta_m(c, t, C["s18.b"] + 0.4, PL, 5, 8, R2)
    E.foco(c, t, C["s18.c"] + 0.3, 0.4, lambda a: E.pilula(c, "?", PL.x(6) - 70, PL.y(38) - 50, 44, "g", fundo=TINTA2, a=a))
    E.frase(c, t, C["s18"], ps("hora de testar", "i", 72, COR), XE, 200)
    E.frase(c, t, C["s18.a"], [("locadora", "i", 60), ("1:", "g", 60)], XE, 330)
    eqn(c, t, C["s18.a"] + 0.3, [("y = 3x + 20", R1)], XE + 330, 330, 70)
    E.frase(c, t, C["s18.b"], [("locadora", "i", 60), ("2:", "g", 60)], XE, 450)
    eqn(c, t, C["s18.b"] + 0.3, [("y = 5x + 8", R2)], XE + 330, 450, 70)
    E.frase(c, t, C["s18.b"] + 1.6, [("x", "g", 52, ENT), ("=", "i", 52), ("dias,", "i", 52), ("y", "g", 52), ("=", "i", 52), ("reais", "i", 52)], XE, 540)
    E.frase(c, t, C["s18.c"], [("onde", "i", 66), ("se", "i", 66), ("cruzam?", "g", 66, COR)], XE, 680)
    E.frase(c, t, C["s18.d"], [("o", "i", 66), ("que", "i", 66), ("isso", "i", 66), ("quer", "i", 66), ("dizer?", "g", 66, COR)], XE, 790)
    if t >= C["s19"]:
        E.relogio(c, t, C["s19.a"], cx=930, cy=560, r=60)


# ---------------- resposta ----------------
def b_resposta(c, t, C, b):
    t0 = C["s20"] - 3
    plano_l(c, t, t0)
    reta_m(c, t, t0, PL, 3, 20, R1)
    reta_m(c, t, t0, PL, 5, 8, R2)
    if t >= C["s20.e"]:
        q = ease_io(prog(t, C["s20.e"], 0.6))
        M.line(c, PL.x(6), PL.y(38), PL.x(6), PL.oy, TINTA2, 0.8, 4, dash=E.TRACO, progress=q)
        pilula_em(c, t, C["s20.e"] + 0.3, "6", PL.x(6), PL.oy + 50, 36, ENT)
    if t >= C["s21.c"]:
        q = ease_io(prog(t, C["s21.c"], 0.6))
        M.line(c, PL.x(6), PL.y(38), PL.ox, PL.y(38), TINTA2, 0.8, 4, dash=E.TRACO, progress=q)
        pilula_em(c, t, C["s21.c"] + 0.3, "38", PL.x(4.6), PL.y(38) - 40, 36, SAI)
    achado(c, t, C["s21.c"], PL, 6, 38)

    def s20():
        E.frase(c, t, C["s20"], [("m", "g", 60, COR), ("=", "g", 60), ("3", "g", 60, R1), ("e", "i", 60), ("5:", "g", 60, R2), ("diferentes", "i", 60)], XE, 220)
        pilula_em(c, t, C["s20.a"], "existe o ponto", XE + 690, 290, 34, CERTO)
        eq_lado(c, t, C["s20.b"], "3x + 20", "5x + 8", XE, 400, 80)
        eqn(c, t, C["s20.c"], [("20 = 2x + 8", TINTA)], XE, 530, 80)
        nota(c, t, C["s20.c"] + 0.4, "− 3x de cada lado", XE + 680, 505)
        eqn(c, t, C["s20.d"], [("12 = 2x", TINTA)], XE, 680, 80)
        nota(c, t, C["s20.d"] + 0.4, "− 8 de cada lado", XE + 680, 655)
        eqn(c, t, C["s20.e"], [("x = 6", ENT)], XE, 850, 96, caixa=C["s20.e"] + 0.5)
    E.saida(c, t, C["s21"] - 0.1, s20)
    if t < C["s21"]:
        return
    eqn(c, t, C["s21"], [("x = 6", ENT)], XE, 230, 70)
    eqn(c, t, C["s21.a"], [("y = 3 · 6 + 20 = 18 + 20 = 38", R1)], XE, 370, 60)
    eqn(c, t, C["s21.b"], [("y = 5 · 6 + 8 = 30 + 8 = 38", R2)], XE, 490, 60)
    pilula_em(c, t, C["s21.b"] + 2.0, "bateu", XE + 100, 570, 36, CERTO)
    par_em(c, t, C["s21.c"], "6", "38", XE, 700, 100)
    E.frase(c, t, C["s21.d"], [("6", "g", 64, ENT), ("dias:", "i", 64), ("mesmo", "g", 64), ("preço,", "i", 64)], XE, 830)
    E.frase(c, t, C["s21.d"] + 1.0, [("R$", "g", 72, CERTO), ("38", "g", 72, CERTO)], XE, 940)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s22"], [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s22.a", [("o", "i", 70), ("ponto", "g", 70, COR), ("resolve", "i", 70), ("as", "i", 70), ("duas", "g", 70), ("equações", "i", 70)]),
                 ("s22.b", [("iguale", "g", 70, COR), ("e", "i", 70), ("confira", "g", 70, COR)]),
                 ("s22.c", [("m", "g", 70, COR), ("igual,", "i", 70), ("n", "g", 70), ("diferente:", "i", 70), ("paralelas", "g", 70)]))
        for i, (k, partes) in enumerate(itens):
            y = 400 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 260, y - 30, 56, a=a),
                                                         E.escreve(c, str(i + 1), 260 - E.larg(str(i + 1), "g", 64) / 2, y - 7, 64, "g", BR, a)))
            E.frase(c, t, C[k] + 0.1, partes, 360, y, passo=0.12)
    E.saida(c, t, C["s23"] - 0.1, resumo)
    if t < C["s23"]:
        return
    E.frase(c, t, C["s23"], [("próxima", "i", 84), ("aula", "i", 84)], XE, 290)
    E.frase(c, t, C["s23.a"], [("Praticando:", "g", 120, COR)], XE, 450)
    E.frase(c, t, C["s23.a"] + 0.6, [("pontos", "g", 120, COR), ("e", "i", 110), ("retas", "g", 120, COR)], XE, 590)
    E.frase(c, t, C["s23.b"], ps("distância, equação da reta", "i", 58, TINTA2), XE, 700, passo=0.1)
    E.frase(c, t, C["s23.c"], ps("e retas que se cruzam, em questões", "i", 58, TINTA2), XE, 780, passo=0.1)
    E.foco(c, t, C["s23.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1450, 400, 76, estilo="g", a=a))
    p = ease_io(prog(t, C["s23.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1780, 1580, p), lerp(720, 425, p), ep(t, C["s23.d"] + 0.2, 0.4))
    E.frase(c, t, C["s23.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 940, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, ideia=b_ideia, resolver=b_resolver, geral=b_geral, casos=b_casos, erro=b_erro,
              atalho=b_atalho, questao=b_questao, resposta=b_resposta, fim=b_fim)
