"""Visual — Estudativo · MAT-TRI-006: prática de razões trigonométricas (sombra de 12 m a 37°: 9 m; escada 6 m a 3 m da parede: 60°;
farol de 20 m visto a 30°: 20√3 ≈ 34 m; antena de 15 m com cabo a 30°: 30 m).
Linguagem da trigonometria (MAT-TRI-001): lados em tinta; cada lado ganha a cor fixa do seu nome — OPO âmbar (cateto oposto),
ADJ petróleo (cateto adjacente; ADJ_ESC no palco escuro), HIP índigo da matéria (hipotenusa); ângulo da vez = arco com cunha;
ângulo reto = quadradinho; sen, cos e tg abreviados; resposta na esfera ou na pílula; erro em vermelho, certo em verde.
A figura não mente: cada cena respeita as medidas (12 e 9; 6 e 3; 20 e 20√3; 15 e 30).
Peças locais: tri() e rot() (de MAT-TRI-001: triângulo retângulo com os lados nomeados no tempo), tabela_trig() (a tabela de 30°,
45° e 60° com casa acesa), poste(), sol(), escada(), farol(), barco(), antena(), titulo(), pergunta(), resp(), lista().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-006_praticando_razoes_trigonometricas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"      # cor fixa de cada lado da trigonometria
ADJ_ESC = "#3CC7D3"
AZUL = "#3D7FD9"
R3 = math.sqrt(3)
assert 0.75 * 12 == 9 and 12 // 4 * 3 == 9 and abs(math.degrees(math.atan(0.75)) - 37) < 0.2
assert 3 / 6 == 0.5 and abs(math.degrees(math.acos(0.5)) - 60) < 1e-9 and abs(math.sin(math.radians(30)) - 0.5) < 1e-12
assert round(20 * 1.7) == 34 and 20 * R3 > 34 and 3 * 20 == 60 and abs(60 / R3 - 20 * R3) < 1e-9
assert 15 / 0.5 == 30 and 2 * 15 == 30 and 15 * 0.5 == 7.5 < 15


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças da trigonometria (de MAT-TRI-001) ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def fcen(c, t, t0, s, cx, y, size, cor=None):
    E.formula_em(c, t, t0, s, cx, y, size, "g", cor, "center")


def grosso(c, P, Q, cor, a, larg=12, p=1.0, dash=None):
    if a > 0 and p > 0:
        M.line(c, *P, *Q, cor, a, larg, progress=p, dash=dash)


def rot(c, P, Q, s, G, size=60, cor=None, a=1.0, gap=20, est="b"):
    """rótulo ao lado do segmento PQ, do lado de fora do triângulo de centro G"""
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    E._cola(c, s, mx, my, nx, ny, gap, size, est, cor or TINTA, a)


def tri(c, t, A, R, T, med, tm=None, cores=None, nomes=None, tn=None, size=60, contorno=None, gm=20):
    """triângulo retângulo sobre a figura: A = ângulo da vez, R = reto, T = o outro. Lados "adj" A–R, "opo" R–T, "hip" A–T.
    med = (adj, opo, hip); tm = {lado: instante da medida}; cores = {lado: (instante, cor)}; nomes/tn = nome do lado e instante"""
    G = ((A[0] + R[0] + T[0]) / 3, (A[1] + R[1] + T[1]) / 3)
    if contorno is not None and t >= contorno:
        q = ep(t, contorno, 0.6)
        path = skia.Path(); path.addPoly([A, R, T], True)
        c.drawPath(path, M.paint(E.COR, 0.07 * q))
    seg = {"adj": (A, R), "opo": (R, T), "hip": (A, T)}
    idx = {"adj": 0, "opo": 1, "hip": 2}
    cores, tm, tn = cores or {}, tm or {}, tn or {}
    for k, (P, Q) in seg.items():
        cor_k = None
        if k in cores and t >= cores[k][0]:
            cor_k = cores[k][1]
            grosso(c, P, Q, cor_k, 1.0, 12, ease_io(prog(t, cores[k][0], 0.5)))
        if k in tm and med[idx[k]]:
            E.foco(c, t, tm[k], 0.4, lambda a, P=P, Q=Q, s=med[idx[k]], cor_t=cor_k or TINTA: rot(c, P, Q, s, G, size, cor_t, a, gm))
        if nomes and k in nomes and k in tn:
            wnum = E.formula(None, med[idx[k]] or "", 0, 0, size, "b", a=0)
            dx, dy = abs(Q[0] - P[0]), abs(Q[1] - P[1])
            gap = gm + 10 + (wnum if dy > 2 * dx else size * 0.8 if dx > 2 * dy else max(wnum * 0.7, size * 0.8))
            E.foco(c, t, tn[k], 0.4, lambda a, P=P, Q=Q, s=nomes[k], cor_n=cor_k or TINTA, gap=gap: rot(c, P, Q, s, G, size * 0.8, cor_n, a, gap, "i"))
    return G


def resp(c, t, t0, s, cx, cy, size=76, alto=1.75, cor=None):
    """resposta numa pílula com volume, na cor da matéria"""
    def f(a):
        w = E.formula(c, s, 0, 0, size, a=0) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        E.formula(c, s, cx, cy + size * 0.36, size, "g", BR, a, "center")
    E.foco(c, t, t0, 0.5, f)


def pilula(c, t, t0, s, cx, cy, size=64):
    E.foco(c, t, t0, 0.5, lambda a: E.pilula(c, s, cx, cy, size, "g", a=a, cor=E.SOBRE))


def lista(c, t, itens, x, y0, dy=130, size=58):
    """linhas numeradas [(t0, partes)] com o número na esfera"""
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 36, y - size * 0.36, 36, a=a),
                                                   centro(c, str(i + 1), x + 36, y - size * 0.36 + 16, 46, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 100, y, "left", 0.1)


def titulo(c, t, t0, n, nome, x=170, y=150):
    E.frase(c, t, t0, ps("situação", "i", 64, COR) + [(str(n), "g", 72, COR)] + ps(f"· {nome}", "i", 56, TINTA2), x, y, "left", 0.1)


def chao(c, x0, x1, y, a=1.0):
    if a > 0:
        M.line(c, x0, y, x1, y, TINTA2, a, 5)
        for k in range(int((x1 - x0) / 40) + 1):
            x = x0 + 20 + k * 40
            M.line(c, x, y + 6, x - 16, y + 26, TINTA2, 0.35 * a, 3)


def angulo_rot(c, t, t0, V, A, B, s, dx, dy, r=110, cor=None, size=54):
    E.angulo(c, t, t0, V, A, B, None, r=r, cor=cor)
    E.foco(c, t, t0 + 0.3, 0.4, lambda a: E._meio(c, s, V[0] + dx, V[1] + dy, size, "b", cor or COR, a))


def tabela_trig(c, t, t0, x, y, cw=200, rh=120, size=54, acesas=()):
    """tabela de 30°, 45° e 60° (linhas sen, cos, tg); acesas = [(linha, coluna, t0, cor)] acende uma casa"""
    cab = ("30°", "45°", "60°")
    lin = (("sen", ("f{1}{2}", "f{r{2}}{2}", "f{r{3}}{2}")), ("cos", ("f{r{3}}{2}", "f{r{2}}{2}", "f{1}{2}")), ("tg", ("f{r{3}}{3}", "1", "r{3}")))
    q = ep(t, t0, 0.6)
    if q <= 0:
        return
    w0 = 150
    for i, (l_, c_, t1, cor) in enumerate(acesas):
        k = ep(t, t1, 0.4)
        if k > 0:
            M.rrect(c, x + w0 + c_ * cw + 6, y + rh * (l_ + 1) - rh + 6 + 40, cw - 12, rh - 12, 18, cor, 0.22 * k)
            M.rrect(c, x + w0 + c_ * cw + 6, y + rh * (l_ + 1) - rh + 6 + 40, cw - 12, rh - 12, 18, None, k, stroke=5, stroke_color=cor)
    for j, s in enumerate(cab):
        centro(c, s, x + w0 + j * cw + cw / 2, y + 20, size, "g", COR, q)
    M.line(c, x, y + 40, x + w0 + 3 * cw, y + 40, TINTA2, q, 3)
    for i, (nome, vals) in enumerate(lin):
        yy = y + 40 + rh * i + rh / 2
        E.escreve(c, nome, x + 10, yy + size * 0.36, size, "g", TINTA, q)
        for j, v in enumerate(vals):
            E.formula(c, v, x + w0 + j * cw + cw / 2, yy + size * 0.3, size, "g", TINTA, q * ep(t, t0 + 0.2 + 0.08 * (3 * i + j), 0.4), "center")


# ---------------- objetos das quatro situações ----------------
GY = 860


def poste(c, base, topo, a=1.0):
    if a <= 0:
        return
    M.line(c, *base, *topo, TINTA, a, 14)
    M.line(c, topo[0], topo[1] + 6, topo[0] + 60, topo[1] + 6, TINTA, a, 8)
    c.drawCircle(topo[0] + 62, topo[1] + 18, 14, M.paint("#FFC400", a))


def sol(c, cx, cy, a=1.0, r=46):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, M.paint("#FFC400", a))
    for k in range(10):
        an = k * math.pi / 5
        M.line(c, cx + (r + 12) * math.cos(an), cy + (r + 12) * math.sin(an), cx + (r + 34) * math.cos(an), cy + (r + 34) * math.sin(an), "#F2A900", a, 5)


def parede(c, x, y0, y1, a=1.0):
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x, y0, x + 70, y1), M.paint(CINZA, 0.3 * a))
    for yy in range(int(y0) + 30, int(y1), 46):
        M.line(c, x, yy, x + 70, yy, TINTA2, 0.4 * a, 3)
    M.line(c, x, y0, x, y1, TINTA, a, 6)


def escada(c, pe, topo, a=1.0, p=1.0):
    """escada de dois trilhos com degraus, de pe até topo"""
    if a <= 0 or p <= 0:
        return
    ux, uy = E._uni(*pe, *topo)
    nx, ny = -uy * 16, ux * 16
    fim = (lerp(pe[0], topo[0], p), lerp(pe[1], topo[1], p))
    for s in (1, -1):
        M.line(c, pe[0] + s * nx, pe[1] + s * ny, fim[0] + s * nx, fim[1] + s * ny, "#8C5A2B", a, 7)
    L = math.dist(pe, topo) * p
    for k in range(1, int(L / 46)):
        px, py = pe[0] + ux * 46 * k, pe[1] + uy * 46 * k
        M.line(c, px - nx, py - ny, px + nx, py + ny, "#8C5A2B", a, 5)


def farol(c, base, topo, a=1.0):
    if a <= 0:
        return
    h = base[1] - topo[1]
    wb, wt = 80, 50
    p = skia.Path()
    p.moveTo(base[0] - wb / 2 + 40, base[1]); p.lineTo(base[0] + wb / 2 + 40, base[1])
    p.lineTo(base[0] + wt / 2 + 40, topo[1]); p.lineTo(base[0] - wt / 2 + 40, topo[1]); p.close()
    c.save(); c.clipPath(p, skia.ClipOp.kIntersect, True)
    c.drawRect(skia.Rect.MakeLTRB(base[0] - 60, topo[1], base[0] + 140, base[1]), M.paint(BR, a))
    for k in range(4):
        y0 = topo[1] + h * (0.12 + 0.22 * k)
        c.drawRect(skia.Rect.MakeLTRB(base[0] - 60, y0, base[0] + 140, y0 + h * 0.1), M.paint(ERRADO, a))
    c.restore()
    pt = M.paint(TINTA, a, stroke=5); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    c.drawRect(skia.Rect.MakeLTRB(base[0] + 40 - 34, topo[1] - 44, base[0] + 40 + 34, topo[1]), M.paint("#FFC400", a))
    c.drawRect(skia.Rect.MakeLTRB(base[0] + 40 - 34, topo[1] - 44, base[0] + 40 + 34, topo[1]), M.paint(TINTA, a, stroke=4))


def barco(c, x, y, a=1.0):
    if a <= 0:
        return
    p = skia.Path()
    p.moveTo(x - 70, y - 30); p.lineTo(x + 70, y - 30); p.lineTo(x + 40, y + 6); p.lineTo(x - 46, y + 6); p.close()
    c.drawPath(p, M.paint("#8C5A2B", a))
    M.line(c, x - 10, y - 30, x - 10, y - 110, TINTA, a, 5)
    s = skia.Path(); s.moveTo(x - 4, y - 106); s.lineTo(x + 50, y - 40); s.lineTo(x - 4, y - 40); s.close()
    c.drawPath(s, M.paint(BR, a)); c.drawPath(s, M.paint(TINTA, a, stroke=3))


def mar(c, x0, x1, y, a=1.0):
    if a <= 0:
        return
    c.drawRect(skia.Rect.MakeLTRB(x0, y, x1, y + 140), M.paint(AZUL, 0.16 * a))
    M.line(c, x0, y, x1, y, AZUL, a, 5)


def antena(c, base, topo, a=1.0):
    if a <= 0:
        return
    M.line(c, *base, *topo, TINTA, a, 10)
    for k in range(1, 6):
        y = lerp(base[1], topo[1], k / 6)
        M.line(c, base[0] - 22, y, base[0] + 22, y, TINTA, a, 4)
    c.drawCircle(topo[0], topo[1] - 10, 12, M.paint(ERRADO, a))


def pergunta(c, t, linhas, rel, X=1420, y_rel=420):
    """linhas [(t0, partes, y)] somem quando o relógio entra"""
    def txt():
        for t0, partes, y in linhas:
            E.frase(c, t, t0, partes, X, y, "center", 0.1)
    E.saida(c, t, rel - 0.2, txt)
    E.relogio(c, t, rel, X, y_rel, 160)


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "4", XE - 8, 520, 340, "g", COR, a))
    E.foco(c, t, a1 + 0.15, 0.5, lambda a: E.escreve(c, "situações", XE + 215, 500, 110, "i", TINTA, a))
    nomes = ("sombra", "escada", "farol", "antena")
    for i, s in enumerate(nomes):
        x, y = 1180 + (i % 2) * 400, 260 + (i // 2) * 170
        pilula(c, t, lerp(a1 + 1.0, b1, 0.2 + 0.2 * i), s, x, y, 64)
    E.frase(c, t, b1, ps("em cada uma,", "i", 62) + [("pause e resolva", "g", 66, COR)], XE, 760, "left", 0.1)
    E.frase(c, t, b1 + 1.4, ps("antes de ver a resposta", "i", 62), XE, 860, "left", 0.1)
    E.frase(c, t, lerp(b1, C["s01.end"], 0.6), ps("errar aqui", "i", 56, TINTA2) + [("não custa nada", "g", 58, CERTO)], XE, 990, "left", 0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    a2, b2, c2 = C["s02.a"], C["s02.b"], C["s02.c"]
    E.frase(c, t, C["s02"] + 0.2, ps("você vai usar", "i", 72, COR), XE, 190, "left", 0.1)
    lista(c, t, [(a2, [("as 3 perguntas", "g", 62)]), (b2, [("sen, cos ou tg", "g", 62)]), (c2, [("a tabela", "g", 62)])], XE, 380, 200, 62)
    E.frase(c, t, a2 + 1.0, ps("ângulo · tenho · quero", "i", 50, TINTA2), XE + 100, 450, "left", 0.08)
    tabela_trig(c, t, c2 + 0.3, 1000, 330, 230, 130, 58)
    E.frase(c, t, C["s02.end"] - 2.4, ps("travou?", "i", 58, COR) + ps("procure a aula no canal", "i", 58), XE, 1000, "left", 0.12)


# ---------------- situação 1: a sombra (45 px por metro) ----------------
U1 = 45
P1B, P1T = (240, GY), (240, GY - 9 * U1)       # o poste
S1 = (240 + 12 * U1, GY)                         # a ponta da sombra


def fig1(c, t, ent, tsombra, traio, tx=None):
    q = ep(t, ent, 0.5)
    chao(c, 100, 1000, GY, q)
    poste(c, P1B, P1T, q)
    if t >= tsombra:
        c.drawRect(skia.Rect.MakeLTRB(P1B[0], GY - 8, lerp(P1B[0], S1[0], ease_io(prog(t, tsombra, 0.6))), GY + 8), M.paint(TINTA2, 0.55))
    if t >= traio:
        k = ep(t, traio, 0.5)
        sol(c, P1T[0] - 150, P1T[1] - 112, k)
        grosso(c, (P1T[0] - 110, P1T[1] - 82), S1, "#F2A900", k, 4, ease_io(prog(t, traio, 0.8)), dash=E.TRACO)
        angulo_rot(c, t, traio + 0.6, S1, P1B, P1T, "37°", -170, -40, r=110)
    if tx is not None:
        E.foco(c, t, tx, 0.4, lambda a: E._cola(c, "x = ?", P1B[0], (P1B[1] + P1T[1]) / 2, -1, 0, 30, 64, "g", OPO, a))


def b_questao1(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s03.{k}"] for k in "abcde")
    titulo(c, t, a3, 1, "a sombra")
    fig1(c, t, a3, b3, c3, e3)
    E.foco(c, t, b3 + 0.5, 0.4, lambda a: centro(c, "12 m", (P1B[0] + S1[0]) / 2, GY + 70, 60, "b", TINTA, a))
    pergunta(c, t, [(b3, ps("sombra de", "i", 62) + [("12 m", "g", 66, COR)], 300),
                    (c3, ps("sol a", "i", 62) + [("37°", "g", 66, COR)] + ps("do chão", "i", 62), 420),
                    (d3, [("tg 37° ≈ 0,75", "g", 66)], 560),
                    (e3, ps("a", "i", 70) + [("altura do poste?", "g", 72, OPO)], 720)], C["s04.a"])
    E.foco(c, t, C["s04.a"] + 0.4, 0.5, lambda a: E.formula(c, "tg 37° ≈ 0,75", 1420, 820, 60, "g", TINTA2, a, "center"))


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s05.{k}"] for k in "abcd")
    a6, b6, c6, d6 = (C[f"s06.{k}"] for k in "abcd")
    ent = C["s05"] - 0.4
    titulo(c, t, ent, 1, "a sombra")
    fig1(c, t, ent, ent, ent)
    tri(c, t, S1, P1B, P1T, ("12", "x", None), tm={"adj": ent, "opo": c5 + 0.3}, cores={"adj": (b5, ADJ), "opo": (c5, OPO)},
        nomes={"adj": "adjacente", "opo": "oposto"}, tn={"adj": b5 + 0.3, "opo": c5 + 0.5}, contorno=a5)
    X = 1420

    def cinco():
        lista(c, t, [(a5, ps("ângulo:", "i", 56) + [("37°, na sombra", "g", 58, COR)]),
                     (b5, ps("tenho:", "i", 56) + [("12", "g", 58, ADJ), ("→ adjacente", "b", 54, ADJ)]),
                     (c5, ps("quero:", "i", 56) + [("poste", "g", 58, OPO), ("→ oposto", "b", 54, OPO)])], 1030, 300, 140, 56)
        pilula(c, t, d5, "tangente", X, 760, 70)
    E.saida(c, t, C["s06"] - 0.1, cinco)
    if t < C["s06"] - 0.1:
        return
    fcen(c, t, a6, "0,75 = f{x}{12}", X, 300, 90)
    fcen(c, t, b6, "x = 0,75 × 12", X, 460, 80)
    resp(c, t, b6 + 1.6, "x = 9 m", X, 590, 66)
    E.frase(c, t, c6 - 0.6, ps("mais rápido:", "i", 56, COR), X, 730, "center", 0.1)
    fcen(c, t, c6, "0,75 = f{3}{4}", X, 850, 72)
    fcen(c, t, d6, "f{3}{4} de 12 = 9", X, 1000, 72, CERTO)


# ---------------- situação 2: a escada (80 px por metro) ----------------
U2 = 80
E2P = (760 - 3 * U2, GY)                     # o pé da escada
E2R = (760, GY)                              # o pé da parede
E2T = (760, GY - 3 * R3 * U2)                # o topo


def fig2(c, t, ent, tesc, tchao, tq=None):
    q = ep(t, ent, 0.5)
    chao(c, 120, 1000, GY, q)
    parede(c, E2R[0], 260, GY, q)
    if t >= tesc:
        escada(c, E2P, E2T, 1.0, ease_io(prog(t, tesc, 0.7)))
    if t >= tchao:
        q2 = ep(t, tchao, 0.5)
        M.line(c, E2P[0], GY + 50, E2R[0], GY + 50, TINTA, q2, 4)
        for X in (E2P[0], E2R[0]):
            M.line(c, X, GY + 36, X, GY + 64, TINTA, q2, 4)
        E.foco(c, t, tchao + 0.2, 0.4, lambda a: centro(c, "3 m", (E2P[0] + E2R[0]) / 2, GY + 115, 56, "b", TINTA, a))
    if tq is not None:
        angulo_rot(c, t, tq, E2P, E2R, E2T, "θ = ?", 170, -40, r=90)


def b_questao2(c, t, C, b):
    a7, b7, c7, d7 = (C[f"s07.{k}"] for k in "abcd")
    titulo(c, t, a7, 2, "a escada")
    fig2(c, t, a7, b7, c7, d7)
    E.foco(c, t, b7 + 0.6, 0.4, lambda a: E._cola(c, "6 m", (E2P[0] + E2T[0]) / 2, (E2P[1] + E2T[1]) / 2, -0.87, -0.5, 30, 60, "b", TINTA, a))
    pergunta(c, t, [(b7, ps("escada de", "i", 62) + [("6 m", "g", 66, COR)], 320),
                    (c7, ps("pé a", "i", 62) + [("3 m", "g", 66, COR)] + ps("da parede", "i", 62), 450),
                    (d7, ps("que", "i", 70) + [("ângulo", "g", 72, COR)] + ps("com o chão?", "i", 70), 640)], C["s08.a"])


def b_resposta2(c, t, C, b):
    a9, b9, c9, d9, e9 = (C[f"s09.{k}"] for k in "abcde")
    a0, b0, c0, d0, e0 = (C[f"s10.{k}"] for k in "abcde")
    ent = C["s09"] - 0.4
    titulo(c, t, ent, 2, "a escada")
    fig2(c, t, ent, ent, 1e9)
    tri(c, t, E2P, E2R, E2T, ("3", None, "6"), tm={"adj": c9 + 0.3, "hip": ent}, cores={"hip": (b9, HIP), "adj": (c9, ADJ)},
        nomes={"hip": "hipotenusa", "adj": "adjacente"}, tn={"hip": b9 + 0.3, "adj": c9 + 0.5}, contorno=a9)
    E.angulo(c, t, a9, E2P, E2R, E2T, None, r=90)
    E.foco(c, t, a9 + 0.3, 0.4, lambda a: E._meio(c, "θ = 60°" if t >= a0 else "θ", E2P[0] - 150 if t >= a0 else E2P[0] + 150, E2P[1] - 36, 52, "b", COR, a))
    X = 1420

    def nove():
        lista(c, t, [(a9, ps("ângulo:", "i", 56) + [("no pé da escada", "g", 58, COR)]),
                     (b9, ps("escada:", "i", 56) + [("hipotenusa, 6", "g", 58, HIP)]),
                     (c9, ps("chão:", "i", 56) + [("adjacente, 3", "g", 58, ADJ)])], 1010, 280, 140, 56)
        E.frase(c, t, d9, [("adjacente", "g", 60, ADJ)] + ps("e", "i", 58) + [("hipotenusa:", "g", 60, HIP), ("cos", "g", 66, COR)], X, 740, "center", 0.1)
        fcen(c, t, e9, "cos θ = f{3}{6} = f{1}{2}", X, 920, 84)
    E.saida(c, t, C["s10"] - 0.1, nove)
    if t < C["s10"] - 0.1:
        return
    fcen(c, t, C["s10"] + 0.1, "cos θ = f{1}{2}", 1130, 220, 72, TINTA2)
    resp(c, t, a0, "θ = 60°", 1600, 200, 62)
    tabela_trig(c, t, C["s10"] + 0.3, 1000, 340, 210, 120, 52,
                acesas=[(0, 0, c0, ERRADO), (1, 2, d0, CERTO)])
    E.foco(c, t, b0, 0.5, lambda a: (E.selo(c, 1080, 860, 40, False, a), E.escreve(c, "30°?", 1140, 880, 60, "g", ERRADO, a)))
    E.frase(c, t, c0 + 0.3, ps("1/2 é o", "i", 50, ERRADO) + [("sen 30°", "g", 54, ERRADO)], 1330, 880, "left", 0.08)
    E.frase(c, t, e0, ps("veja", "i", 58) + [("qual razão", "g", 62, COR)] + ps("você montou", "i", 58), 1420, 1010, "center", 0.1)


# ---------------- situação 3: o farol (18 px por metro) ----------------
U3 = 18
F3B = (170, GY)                                  # o barco
F3R = (170 + 20 * R3 * U3, GY)                   # o pé do farol
F3T = (F3R[0], GY - 20 * U3)                     # o topo


def fig3(c, t, ent, tang, tfar, tx=None):
    q = ep(t, ent, 0.5)
    mar(c, 60, F3R[0] - 20, GY, q)
    M.line(c, F3R[0] - 20, GY, 1010, GY, TINTA2, q, 5)
    c.drawRect(skia.Rect.MakeLTRB(F3R[0] - 20, GY, 1010, GY + 140), M.paint(TINTA2, 0.15 * q))
    if t >= tfar:
        farol(c, (F3R[0] - 40, GY), (F3T[0] - 40, F3T[1]), ep(t, tfar, 0.5))
    barco(c, F3B[0], GY, q)
    if t >= tang:
        grosso(c, F3B, F3T, TINTA2, 1.0, 4, ease_io(prog(t, tang, 0.7)), dash=E.TRACO)
        angulo_rot(c, t, tang + 0.5, F3B, F3R, F3T, "30°", 200, -36, r=140)
    if tx is not None:
        E.foco(c, t, tx, 0.4, lambda a: centro(c, "x = ?", (F3B[0] + F3R[0]) / 2, GY + 80, 60, "g", ADJ, a))


def b_questao3(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    titulo(c, t, a1, 3, "o farol")
    fig3(c, t, a1, b1, c1, d1)
    E.foco(c, t, c1 + 0.4, 0.4, lambda a: E._cola(c, "20 m", F3R[0] + 40, (F3R[1] + F3T[1]) / 2, 1, 0, 40, 60, "b", TINTA, a))
    pergunta(c, t, [(b1, ps("do barco:", "i", 62) + [("30°", "g", 66, COR)], 300),
                    (c1, ps("farol de", "i", 62) + [("20 m", "g", 66, COR)], 420),
                    (d1, ps("a que", "i", 66) + [("distância?", "g", 72, ADJ)], 600),
                    (d1 + 1.6, [("√3 ≈ 1,7", "g", 56, TINTA2)], 720)], C["s12.a"])
    E.foco(c, t, C["s12.a"] + 0.4, 0.5, lambda a: E.formula(c, "r{3} ≈ 1,7", 1420, 820, 60, "g", TINTA2, a, "center"))


def b_resposta3(c, t, C, b):
    a3, b3, c3, d3 = (C[f"s13.{k}"] for k in "abcd")
    a4, b4, c4, d4 = (C[f"s14.{k}"] for k in "abcd")
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    ent = C["s13"] - 0.4
    titulo(c, t, ent, 3, "o farol")
    fig3(c, t, ent, ent, ent)
    tri(c, t, F3B, F3R, F3T, ("x", "20", None), tm={"opo": ent, "adj": c3 + 0.3}, cores={"opo": (b3, OPO), "adj": (c3, ADJ)},
        nomes={"opo": "oposto", "adj": "adjacente"}, tn={"opo": b3 + 0.3, "adj": c3 + 0.5}, contorno=a3, gm=56)
    E.angulo(c, t, b4, F3T, F3B, F3R, None, r=90, cor=TINTA2)
    E.foco(c, t, b4 + 0.3, 0.4, lambda a: E._meio(c, "60°", F3T[0] - 120, F3T[1] + 130, 46, "b", TINTA2, a))
    X = 1420

    def treze():
        lista(c, t, [(a3, ps("ângulo:", "i", 56) + [("30°, no barco", "g", 58, COR)]),
                     (b3, ps("farol:", "i", 56) + [("oposto, 20", "g", 58, OPO)]),
                     (c3, ps("distância:", "i", 56) + [("adjacente", "g", 58, ADJ)])], 1010, 280, 140, 56)
        E.frase(c, t, c3 + 1.2, [("oposto", "g", 58, OPO)] + ps("e", "i", 56) + [("adjacente:", "g", 58, ADJ), ("tg", "g", 64, COR)], X, 720, "center", 0.1)
        pilula(c, t, d3, "o atalho é mais rápido", X, 870, 56)
    E.saida(c, t, C["s14"] - 0.1, treze)

    def quatorze():
        E.frase(c, t, a4, ps("frente ao 30°:", "i", 58) + [("menor = 20", "g", 62, OPO)], X, 260, "center", 0.1)
        E.frase(c, t, b4, ps("frente ao 60°:", "i", 58) + [("menor × √3", "g", 62, ADJ)], X, 400, "center", 0.1)
        fcen(c, t, c4, "x = 20r{3}", X, 580, 100, ADJ)
        fcen(c, t, d4, "20 × 1,7 = 34", X, 750, 80)
        resp(c, t, d4 + 1.6, "x ≈ 34 m", X, 900, 66)
    E.saida(c, t, C["s15"] - 0.1, quatorze)
    if t < C["s15"] - 0.1:
        return
    E.frase(c, t, C["s15"] + 0.1, ps("pela tangente, o mesmo", "i", 56, COR), X, 190, "center", 0.1)
    fcen(c, t, a5, "f{r{3}}{3} = f{20}{x}", X, 360, 84)
    fcen(c, t, b5, "r{3} · x = 60", X, 540, 84)
    fcen(c, t, c5, "x = f{60}{r{3}}", X, 720, 84)
    fcen(c, t, d5, "= f{60r{3}}{3} = 20r{3}", X, 920, 80, CERTO)


# ---------------- situação 4: a antena (24 px por metro) ----------------
U4 = 24
A4C = (820 - 15 * R3 * U4, GY)                   # onde o cabo chega no chão
A4B = (820, GY)                                  # o pé da antena
A4T = (820, GY - 15 * U4)                        # o topo


def fig4(c, t, ent, tant, tcabo, tq=None):
    q = ep(t, ent, 0.5)
    chao(c, 100, 1000, GY, q)
    if t >= tant:
        antena(c, A4B, (A4T[0], lerp(A4B[1], A4T[1], ease_io(prog(t, tant, 0.7)))), 1.0)
    if t >= tcabo:
        grosso(c, A4T, A4C, TINTA, 1.0, 5, ease_io(prog(t, tcabo, 0.8)))
        angulo_rot(c, t, tcabo + 0.6, A4C, A4B, A4T, "30°", 200, -36, r=140)
    if tq is not None:
        E.foco(c, t, tq, 0.4, lambda a: E._cola(c, "cabo = ?", (A4C[0] + A4T[0]) / 2, (A4C[1] + A4T[1]) / 2, -0.5, -0.87, 30, 60, "g", HIP, a))


def b_questao4(c, t, C, b):
    a6, b6, c6, d6 = (C[f"s16.{k}"] for k in "abcd")
    titulo(c, t, a6, 4, "a antena")
    fig4(c, t, a6, b6, lerp(b6, c6, 0.6), d6)
    E.foco(c, t, b6 + 0.6, 0.4, lambda a: E._cola(c, "15 m", A4B[0] + 30, (A4B[1] + A4T[1]) / 2, 1, 0, 30, 60, "b", TINTA, a))
    pergunta(c, t, [(b6, ps("antena de", "i", 62) + [("15 m", "g", 66, COR)], 300),
                    (lerp(b6, c6, 0.6), ps("cabo do topo", "i", 62) + [("ao chão", "g", 66, COR)], 420),
                    (c6, ps("cabo a", "i", 62) + [("30°", "g", 66, COR)] + ps("do chão", "i", 62), 540),
                    (d6, ps("quanto mede o", "i", 66) + [("cabo?", "g", 72, HIP)], 720)], C["s17.a"])


def b_resposta4(c, t, C, b):
    a8, b8, c8, d8, e8 = (C[f"s18.{k}"] for k in "abcde")
    a9, b9, c9, d9, e9 = (C[f"s19.{k}"] for k in "abcde")
    ent = C["s18"] - 0.4
    titulo(c, t, ent, 4, "a antena")
    fig4(c, t, ent, ent, ent)
    tri(c, t, A4C, A4B, A4T, (None, "15", "x"), tm={"opo": ent, "hip": a8 + 0.3}, cores={"hip": (a8, HIP), "opo": (b8, OPO)},
        nomes={"hip": "hipotenusa", "opo": "oposto"}, tn={"hip": a8 + 0.5, "opo": b8 + 0.3})
    X = 1420

    def dezoito():
        lista(c, t, [(a8, ps("cabo:", "i", 56) + [("hipotenusa, falta", "g", 58, HIP)]),
                     (b8, ps("antena:", "i", 56) + [("oposto, 15", "g", 58, OPO)])], 1010, 280, 140, 56)
        E.frase(c, t, c8, [("oposto", "g", 58, OPO)] + ps("e", "i", 56) + [("hipotenusa:", "g", 58, HIP), ("sen", "g", 64, COR)], X, 590, "center", 0.1)
        fcen(c, t, d8, "f{1}{2} = f{15}{x}", X, 770, 90)
        resp(c, t, e8, "x = 30 m", X, 940, 66)
    E.saida(c, t, C["s19"] - 0.1, dezoito)
    if t < C["s19"] - 0.1:
        return
    E.frase(c, t, a9, ps("pelo atalho:", "i", 58, COR), X, 220, "center", 0.1)
    E.frase(c, t, a9 + 0.8, [("hipotenusa", "g", 58, HIP)] + ps("= dobro do", "i", 56), X, 310, "center", 0.1)
    E.frase(c, t, a9 + 1.6, [("oposto ao 30°", "g", 58, OPO)], X, 385, "center", 0.1)
    fcen(c, t, b9, "2 × 15 = 30", X, 510, 84, CERTO)
    fcen(c, t, c9, "15 × f{1}{2} = 7,5", X - 60, 650, 80, ERRADO)
    E.foco(c, t, d9, 0.5, lambda a: E.selo(c, X + 270, 625, 40, False, a))
    E.frase(c, t, d9, ps("cabo", "i", 56, ERRADO) + [("mais curto", "g", 58, ERRADO)] + ps("que a antena?", "i", 56, ERRADO), X, 780, "center", 0.1)
    pilula(c, t, e9, "hipotenusa procurada: divida", X, 920, 54)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s20"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 180, "center")
        itens = (("s20.a", "dê nome aos lados", "a partir do ângulo"), ("s20.b", "na tabela:", "tabela ou atalho"),
                 ("s20.c", "fora da tabela:", "o valor da prova"), ("s20.d", "confira se", "faz sentido"))
        for i, (k, l1, l2) in enumerate(itens):
            y = 340 + i * 170
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 52, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 8, 60, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, ps(l1, "i", 66) + [(l2, "g", 68, COR)], 320, y, "left", 0.1)
    E.saida(c, t, C["s21"] - 0.1, resumo)
    if t < C["s21"]:
        return
    a1, b1, c1 = C["s21.a"], C["s21.b"], C["s21.c"]
    E.frase(c, t, C["s21"] + 0.2, ps("na próxima aula, a trigonometria", "i", 70), XE, 200, passo=0.1)
    E.frase(c, t, C["s21"] + 1.2, [("sai do triângulo", "g", 76, COR)], XE, 300, passo=0.1)
    E.frase(c, t, a1, ps("o", "i", 70) + [("radiano", "g", 76, COR)], XE, 440, passo=0.1)
    E.foco(c, t, b1, 0.5, lambda a: E.formula(c, "60° = f{π}{3}", XE + 420, 450, 76, "g", TINTA, a))
    E.frase(c, t, c1, ps("o", "i", 70) + [("ciclo:", "g", 76, COR), ("390°", "g", 66), ("cai no ponto do", "i", 62), ("30°", "g", 66)], XE, 600, passo=0.1)
    E.foco(c, t, C["s21.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s21.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s21.d"] + 0.2, 0.4))
    E.frase(c, t, C["s21.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2,
              resposta2=b_resposta2, questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
