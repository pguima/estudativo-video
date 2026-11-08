"""Visual — Estudativo · MAT-TRI-013: praticando ciclo e funções trigonométricas (495° → 135° = 3π/4; sen 495° = √2/2 e
cos 495° = −√2/2; sen x = −5/13 no 3º → cos −12/13 e tg 5/12; estufa 22 + 6 sen(πt/12): 28 °C, 16 °C, 24 h, 15 h e 3 h).
Linguagem de cada parte, como nas aulas de origem:
- ciclo (MAT-TRI-007): eixos com seta, o arco que anda na cor da matéria com a ponta de seta, mais de uma volta em espiral;
- seno e cosseno no ciclo (MAT-TRI-008 e 010): o seno é o traço em pé, em âmbar (OPO); o cosseno é o traço deitado, em
  petróleo (ADJ); o raio = hipotenusa em índigo; triângulo retângulo da MAT-TRI-001 para o 5-12-13;
- onda (MAT-TRI-011, 014 e 012): eixo do tempo em índigo, eixo da temperatura em preto; o nível médio (o número somado) em
  âmbar com a linha do meio tracejada, o número da frente em índigo, o de dentro do parêntese e o período em magenta.
Cada questão: título "questão n", a pergunta à direita e o relógio de pausa; a resposta passo a passo na pílula; erro em
vermelho, certo em verde. A figura não mente: 135°, 45° e 202,6° (sen −5/13, cos −12/13) são os ângulos de verdade, e a
onda é 22 + 6 sen(πt/12), com o máximo em t = 6 e o mínimo em t = 18.
Peças locais: ciclo(), arco(), espiral(), marca(), quadrante(), tri_ciclo(), tri(), cf(), resp(), lista(), titulo(), eixos().
Todo instante vem de C[...] (marcadores do roteiro), para acompanhar a voz real quando ela chegar."""
import math
import editorial as E
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, CERTO, ERRADO, XE, ep, prog, lerp, ease_io, ease_back, ease_out, palco, centro
import motor as M
import skia

E.usar("Matemática", "Trigonometria")
COR, CLARO = E.COR_TEXTO, E.CLARO
ARQUIVO_FINAL = "estudativo_MAT-TRI-013_praticando_ciclo_e_funcoes_trigonometricas.mp4"
MARCA = ""
BACKGROUND = E.fundo
CORTINAS = E.carregar_cortinas(__file__, ("questao1", "questao2", "questao3", "questao4", "fim"))
BR = "#FFFFFF"
AMBAR = "#D98A00"
HIP, OPO, ADJ = E.COR, AMBAR, "#0E9AA7"
LA, LB, LC = AMBAR, E.COR, "#C0187C"
ENT, SAI = E.COR, TINTA
PI = math.pi
X3 = 180 + math.degrees(math.asin(5 / 13))    # 202,62°: sen −5/13, cos −12/13
assert 495 - 360 == 135 and 90 < 135 < 180 and 180 / 45 == 4 and 135 == 3 * 45 and 3 * 180 / 4 == 135 and 180 - 135 == 45
assert 169 - 25 == 144 == 12 ** 2 and abs(math.cos(math.radians(X3)) + 12 / 13) < 1e-12 and abs((-5 / 13) / (-12 / 13) - 5 / 12) < 1e-12
T_est = lambda t: 22 + 6 * math.sin(PI * t / 12)
assert T_est(6) == 28 and abs(T_est(18) - 16) < 1e-12 and 9 + 6 == 15 and 9 + 18 - 24 == 3 and 2 * 12 == 24


def CAPTION(c, s, t):
    pass


def OVERLAY(c, t):
    E.acabamento(c, t)
    for t0 in CORTINAS:
        E.cortina(c, t, t0 + 0.1)


# ---------------- peças gerais ----------------
def ps(txt, est="i", size=84, cor=TINTA):
    return [(w, est, size, cor) for w in txt.split()]


def _w(s, size, est="g"):
    return E.formula(None, s, 0, 0, size, est, a=0)


def cf(c, partes, x, y, size, a=1.0, align="left", est="g"):
    ws = [_w(s, size, est) for s, _ in partes]
    xx = x - sum(ws) / 2 if align == "center" else x - sum(ws) if align == "right" else x
    if c is not None and a > 0:
        for (s, cor), wi in zip(partes, ws):
            E.formula(c, s, xx, y, size, est, cor, a)
            xx += wi
    return sum(ws)


def cf_em(c, t, t0, partes, x, y, size, align="left"):
    E.foco(c, t, t0, 0.5, lambda a: cf(c, partes, x, y, size, a, align))


def resp(c, t, t0, partes, cx, cy, size=64, alto=1.75, cor=None):
    if isinstance(partes, str):
        partes = [(partes, BR)]

    def f(a):
        w = cf(None, partes, 0, 0, size) + size * 1.1
        h = size * alto
        M.rrect(c, cx - w / 2, cy - h / 2, w, h, h / 2, cor or E.COR, a, shadow=True)
        cf(c, partes, cx, cy + size * 0.36, size, a, "center")
    E.foco(c, t, t0, 0.5, f)


def lista(c, t, itens, x, y0, dy=130, size=58):
    for i, (t0, partes) in enumerate(itens):
        y = y0 + i * dy
        E.foco(c, t, t0, 0.5, lambda a, i=i, y=y: (E.bola(c, x + 36, y - size * 0.36, 36, a=a),
                                                   centro(c, str(i + 1), x + 36, y - size * 0.36 + 16, 46, "g", BR, a)))
        E.frase(c, t, t0 + 0.1, partes, x + 100, y, "left", 0.1)


def titulo(c, t, t0, n, nome, x=XE, y=150):
    E.frase(c, t, t0, ps("questão", "i", 64, COR) + [(str(n), "g", 72, COR)] + ps(f"· {nome}", "i", 56, TINTA2), x, y, "left", 0.1)


def pergunta(c, t, linhas, rel, X=1420, y_rel=440):
    def txt():
        for t0, partes, y in linhas:
            E.frase(c, t, t0, partes, X, y, "center", 0.1)
    E.saida(c, t, rel - 0.2, txt)
    E.relogio(c, t, rel, X, y_rel, 160)


# ---------------- ciclo ----------------
def pt(cx, cy, r, ang):
    return cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))


def ciclo(c, t, t0, cx, cy, r, a=1.0):
    if t < t0 or a <= 0:
        return
    q = ep(t, t0, 0.6) * a
    M.arrow(c, cx - r - 70, cy, cx + r + 90, cy, TINTA, q, 4, 20, q)
    M.arrow(c, cx, cy + r + 70, cx, cy - r - 90, TINTA, q, 4, 20, q)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -360 * ease_io(prog(t, t0 + 0.2, 0.9)), False, M.paint(TINTA, a, stroke=5))
    for s, X, Y in (("1", cx + r + 12, cy + 50), ("−1", cx - r - 70, cy + 50), ("1", cx - 40, cy - r - 12), ("−1", cx - 70, cy + r + 50)):
        E.foco(c, t, t0 + 0.7, 0.4, lambda b, s=s, X=X, Y=Y: E.escreve(c, s, X, Y, 42, "b", TINTA, b * a))


def quadrante(c, t, t0, cx, cy, r, n, rot=True):
    """quadrante n (1 a 4) pintado de leve, com o nome"""
    if t < t0:
        return
    k = ep(t, t0, 0.5)
    path = skia.Path(); path.moveTo(cx, cy); path.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90 * (n - 1), -90, False); path.close()
    c.drawPath(path, M.paint(E.COR, 0.12 * k))
    if rot:
        X, Y = pt(cx, cy, r * 0.6, 45 + 90 * (n - 1))
        E.foco(c, t, t0, 0.4, lambda a: centro(c, f"{n}º", X, Y + 20, 60, "g", CINZA, a))


def ponta(c, x, y, dx, dy, cor, a, tam=26):
    n = math.hypot(dx, dy) or 1
    dx, dy = dx / n, dy / n
    p = skia.Path()
    p.moveTo(x + dx * tam * 0.6, y + dy * tam * 0.6)
    p.lineTo(x - dx * tam * 0.6 - dy * tam * 0.55, y - dy * tam * 0.6 + dx * tam * 0.55)
    p.lineTo(x - dx * tam * 0.6 + dy * tam * 0.55, y - dy * tam * 0.6 - dx * tam * 0.55)
    p.close()
    c.drawPath(p, M.paint(cor, a))


def espiral(c, cx, cy, r, total, cor=None, larg=10, p=1.0, a=1.0, passo=34):
    if p <= 0 or a <= 0:
        return
    cor = cor or E.COR
    fim = total * p
    path = skia.Path()
    n = max(2, int(fim / 2))
    for i in range(n + 1):
        ang = fim * i / n
        X, Y = pt(cx, cy, r + passo * ang / 360, ang)
        (path.moveTo if i == 0 else path.lineTo)(X, Y)
    pp = M.paint(cor, a, stroke=larg, cap_round=True); pp.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pp)
    X, Y = pt(cx, cy, r + passo * fim / 360, fim)
    th = math.radians(fim)
    ponta(c, X, Y, -math.sin(th), -math.cos(th), cor, a, larg * 2.6)


def marca(c, t, t0, cx, cy, r, ang, rot=None, cor=None, size=50, fora=64):
    k = ease_back(prog(t, t0, 0.4))
    if k <= 0:
        return
    cor = cor or E.COR
    X, Y = pt(cx, cy, r, ang)
    c.drawCircle(X, Y, 15 * k, M.paint(cor))
    c.drawCircle(X, Y, 15 * k, M.paint(BR, 1.0, stroke=3))
    if rot:
        Xr, Yr = pt(cx, cy, r + fora, ang)
        E.foco(c, t, t0 + 0.1, 0.4, lambda a: E.formula(c, rot, Xr, Yr + size * 0.36, size, "g", cor, a, "center"))


def rotulo_lado(c, P, Q, s, G, size, cor, a, gap=26):
    if a <= 0 or not s:
        return
    ux, uy = E._uni(*P, *Q)
    nx, ny = uy, -ux
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    if (mx + nx - G[0]) ** 2 + (my + ny - G[1]) ** 2 < (mx - G[0]) ** 2 + (my - G[1]) ** 2:
        nx, ny = -nx, -ny
    w = _w(s, size)
    hh = size * (0.95 if "f{" in s else 0.5)
    d = gap + abs(nx) * w / 2 + abs(ny) * hh
    X, Y = mx + nx * d, my + ny * d
    M.rrect(c, X - w / 2 - 10, Y - hh - 8, w + 20, 2 * hh + 16, 14, E.PAPEL, 0.92 * a)
    E.formula(c, s, X, Y + size * 0.36, size, "g", cor, a, "center")


def tri_ciclo(c, t, cx, cy, r, ang, td=None, tf=None, tc=None, ts=None, rc=None, rs=None, size=62, a=1.0):
    """o triângulo no ciclo: o seno em pé (âmbar) e o cosseno deitado (petróleo), com rótulos"""
    if a <= 0:
        return
    co, se = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    O, P, F = (cx, cy), (cx + r * co, cy - r * se), (cx + r * co, cy)
    G = ((O[0] + P[0] + F[0]) / 3, (O[1] + P[1] + F[1]) / 3)
    if tf is not None and t >= tf:
        q = ep(t, tf, 0.6) * a
        path = skia.Path(); path.moveTo(*O); path.lineTo(*F); path.lineTo(*P); path.close()
        c.drawPath(path, M.paint(E.COR, 0.13 * q))
        M.line(c, *O, *P, HIP, q, 6)
    if td is not None and t >= td:
        M.line(c, *P, *F, TINTA, 0.8 * a, 5, dash=E.TRACO, progress=ep(t, td, 0.6))
    for t_, P1, Q1, cor, rot_ in ((tc, O, F, ADJ, rc), (ts, F, P, OPO, rs)):
        if t_ is None or t < t_:
            continue
        M.line(c, *P1, *Q1, cor, a, 12, progress=ease_io(prog(t, t_, 0.5)))
        if rot_:
            E.foco(c, t, t_ + 0.3, 0.4, lambda b, P1=P1, Q1=Q1, s=rot_, cor=cor: rotulo_lado(c, P1, Q1, s, G, size, cor, b * a))


def tri(c, t, t0, A, R, T, med, tm, cores, size=64):
    """triângulo retângulo da MAT-TRI-001: lados "adj" A–R, "opo" R–T, "hip" A–T; med = {lado: texto ou função t → texto}"""
    G = ((A[0] + R[0] + T[0]) / 3, (A[1] + R[1] + T[1]) / 3)
    E.triangulo(c, t, t0, A, R, T, vertices=None, retos=(1,), preenche=0.07, d=0.9)
    seg = {"adj": (A, R), "opo": (R, T), "hip": (A, T)}
    for k, (P, Q) in seg.items():
        cor_k = None
        if k in cores and t >= cores[k][0]:
            cor_k = cores[k][1]
            M.line(c, *P, *Q, cor_k, 1.0, 12, progress=ease_io(prog(t, cores[k][0], 0.5)))
        if k in tm and k in med:
            s = med[k](t) if callable(med[k]) else med[k]
            E.foco(c, t, tm[k], 0.4, lambda a, P=P, Q=Q, s=s, cor_t=cor_k or TINTA: rotulo_lado(c, P, Q, s, G, size, cor_t, a, 18))


# ---------------- gancho ----------------
def b_gancho(c, t, C, b):
    a1, b1 = C["s01.a"], C["s01.b"]
    E.foco(c, t, a1, 0.5, lambda a: E.escreve(c, "4", XE - 8, 520, 340, "g", COR, a))
    E.foco(c, t, a1 + 0.15, 0.5, lambda a: E.escreve(c, "questões", XE + 215, 500, 110, "i", TINTA, a))
    nomes = (("ciclo", COR), ("sinais", COR), ("relação fundamental", COR), ("onda", ADJ))
    for i, (s, cor) in enumerate(nomes):
        x, y = 1160 + (i % 2) * 440, 260 + (i // 2) * 170
        E.foco(c, t, lerp(a1 + 1.0, b1, 0.15 + 0.2 * i), 0.5, lambda a, s=s, x=x, y=y, cor=cor: E.pilula(c, s, x, y, 58, "g", fundo=cor, a=a, cor=E.SOBRE))
    E.frase(c, t, b1, ps("em cada uma,", "i", 62) + [("pause e resolva", "g", 66, COR)], XE, 760, "left", 0.1)
    E.frase(c, t, b1 + 1.4, ps("antes de ver a resposta", "i", 62), XE, 860, "left", 0.1)
    E.frase(c, t, lerp(b1, C["s01.end"], 0.55), ps("errar aqui", "i", 56, TINTA2) + [("não custa nada", "g", 58, CERTO)], XE, 990, "left", 0.1)


# ---------------- lembrete ----------------
def b_lembrete(c, t, C, b):
    a2, b2, c2, d2, e2, f2 = (C[f"s02.{k}"] for k in "abcdef")
    E.frase(c, t, C["s02"] + 0.2, ps("você vai usar", "i", 70, COR), XE, 170, "left", 0.1)
    E.frase(c, t, a2, [("5 ferramentas", "g", 76)], XE + 470, 170, "left", 0.1)
    lista(c, t, [(b2, [("radianos e voltas", "g", 60)] + ps("no ciclo", "i", 56)),
                 (c2, ps("o", "i", 56) + [("sinal", "g", 60, COR)] + ps("de sen e cos por quadrante", "i", 56)),
                 (d2, ps("a", "i", 56) + [("redução", "g", 60, COR)] + ps("ao 1º quadrante", "i", 56)),
                 (e2, ps("a", "i", 56) + [("relação fundamental", "g", 60, COR)]),
                 (f2, [("máximo, mínimo e período", "g", 60, LC)] + ps("de uma onda", "i", 56))], XE, 340, 135, 58)
    E.frase(c, t, C["s02.end"] - 2.4, ps("travou?", "i", 58, COR) + ps("procure a aula no canal", "i", 58), XE, 1010, "left", 0.12)


# ---------------- questão 1 ----------------
CX, CY, CR = 560, 590, 300


def b_questao1(c, t, C, b):
    a3, b3, c3 = C["s03.a"], C["s03.b"], C["s03.c"]
    titulo(c, t, a3, 1, "ciclo e radianos")
    ciclo(c, t, a3 + 0.2, CX, CY, CR)
    E.foco(c, t, b3, 0.5, lambda a: E.formula(c, "495°", CX + 60, CY - 60, 76, "g", COR, a))
    pergunta(c, t, [(b3, ps("um arco de", "i", 62) + [("495°", "g", 70, COR)], 300),
                    (c3, ps("em que", "i", 62) + [("quadrante", "g", 68, COR)] + ps("termina?", "i", 62), 440),
                    (c3 + 2.2, ps("o da 1ª volta,", "i", 58) + [("em radianos?", "g", 64, COR)], 570)], C["s04.a"])


def b_resposta1(c, t, C, b):
    a5, b5, c5, d5, e5, f5 = (C[f"s05.{k}"] for k in "abcdef")
    X = 1380
    ciclo(c, t, C["s05"] - 0.2, CX, CY, CR)
    quadrante(c, t, b5, CX, CY, CR, 2)
    espiral(c, CX, CY, CR - 70, 495, E.COR, 10, ease_io(prog(t, a5, 2.4)), 1.0, passo=48)
    marca(c, t, a5 + 2.4, CX, CY, CR, 135, "135°", fora=74)
    E.foco(c, t, e5 + 0.4, 0.4, lambda a: E.formula(c, "f{3π}{4}", *(lambda P: (P[0] - 60, P[1] - 50))(pt(CX, CY, CR + 70, 135)), 54, "g", AMBAR, a, "center"))
    E.frase(c, t, C["s05"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 150, "left", 0.1)
    cf_em(c, t, a5, [("495 − 360 = 135", TINTA)], X, 210, 76, "center")
    E.frase(c, t, b5, ps("entre 90° e 180°:", "i", 54) + [("2º quadrante", "g", 60, COR)], X, 330, "center", 0.08)
    cf_em(c, t, c5, [("180 ÷ 45 = 4  →  ", TINTA), ("f{π}{4}", AMBAR)], X, 470, 66, "center")
    cf_em(c, t, d5, [("135 = 3 · 45", TINTA)], X, 610, 66, "center")
    resp(c, t, e5, [("135° = f{3π}{4} rad", BR)], X, 760, 64, 2.3)
    E.frase(c, t, f5, ps("confere: troque", "i", 50, TINTA2) + [("π por 180", "g", 54)], X, 900, "center", 0.08)
    cf_em(c, t, f5 + 1.6, [("f{3 · 180}{4} = f{540}{4} = 135", CERTO)], X, 1010, 56, "center")


# ---------------- questão 2 ----------------
def b_questao2(c, t, C, b):
    a6, b6 = C["s06.a"], C["s06.b"]
    titulo(c, t, a6, 2, "redução e sinais")
    ciclo(c, t, a6 + 0.2, CX, CY, CR)
    marca(c, t, a6 + 0.6, CX, CY, CR, 135, "495°", fora=74)
    pergunta(c, t, [(a6 + 0.6, ps("com o", "i", 62) + [("mesmo arco", "g", 68, COR)], 300),
                    (b6, [("sen 495° = ?", "g", 72, OPO)], 450),
                    (b6 + 0.8, [("cos 495° = ?", "g", 72, ADJ)], 580)], C["s07.a"])


def b_resposta2(c, t, C, b):
    a8, b8, c8, d8, e8, f8, g8 = (C[f"s08.{k}"] for k in "abcdefg")
    X = 1380
    ciclo(c, t, C["s08"] - 0.2, CX, CY, CR)
    quadrante(c, t, C["s08"], CX, CY, CR, 2)
    marca(c, t, C["s08"] + 0.2, CX, CY, CR, 135, "135°", fora=74)
    # o parceiro 45° no 1º quadrante, ligado pela horizontal (mesma altura)
    if t >= b8:
        P1, P2 = pt(CX, CY, CR, 135), pt(CX, CY, CR, 45)
        M.line(c, *P1, *P2, TINTA2, 0.8, 4, dash=E.TRACO, progress=ep(t, b8, 0.7))
    marca(c, t, b8 + 0.6, CX, CY, CR, 45, "45°", cor=CINZA, fora=70)
    tri_ciclo(c, t, CX, CY, CR, 135, td=c8 - 0.2, tf=c8 - 0.2, ts=c8, rs="f{r{2}}{2}", tc=e8, rc="−f{r{2}}{2}" if t >= f8 else "f{r{2}}{2}", size=56)
    E.frase(c, t, C["s08"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 150, "left", 0.1)
    E.frase(c, t, a8, ps("mesmo ponto:", "i", 54) + [("vale o de 135°", "g", 60, COR)], X, 200, "center", 0.08)
    cf_em(c, t, b8, [("180 − 135 = 45", TINTA)], X, 320, 66, "center")
    cf_em(c, t, c8, [("sen 45° = f{r{2}}{2}", OPO)], X, 470, 66, "center")
    E.frase(c, t, d8, ps("no 2º, o seno é", "i", 52) + [("positivo", "g", 58, CERTO)], X, 580, "center", 0.08)
    cf_em(c, t, e8, [("cos 45° = f{r{2}}{2}", ADJ)], X, 710, 66, "center")
    E.frase(c, t, f8, ps("no 2º, o cosseno é", "i", 52) + [("negativo", "g", 58, ERRADO)], X, 820, "center", 0.08)
    resp(c, t, g8, [("sen 495° = f{r{2}}{2}", BR), ("    ", BR), ("cos 495° = −f{r{2}}{2}", BR)], 1180, 970, 52, 2.4)


# ---------------- questão 3 ----------------
def b_questao3(c, t, C, b):
    a9, b9, c9, d9 = (C[f"s09.{k}"] for k in "abcd")
    titulo(c, t, a9, 3, "relação fundamental")
    ciclo(c, t, a9 + 0.2, CX, CY, CR)
    quadrante(c, t, c9, CX, CY, CR, 3)
    pergunta(c, t, [(b9, ps("seno", "i", 62) + [("−5/13", "g", 70, OPO)], 300),
                    (c9, ps("no", "i", 62) + [("3º quadrante", "g", 68, COR)], 440),
                    (d9, ps("calcule", "i", 62) + [("cos x", "g", 68, ADJ)] + ps("e", "i", 62) + [("tg x", "g", 68)], 580)], C["s10.a"])


K3 = 38
TA3, TR3, TT3 = (170, 800), (170 + 12 * K3, 800), (170 + 12 * K3, 800 - 5 * K3)


def b_resposta3(c, t, C, b):
    a1, b1, c1, d1 = (C[f"s11.{k}"] for k in "abcd")
    a2, b2, c2, d2 = (C[f"s12.{k}"] for k in "abcd")
    X = 1300

    def tri3():
        tri(c, t, C["s11"] + 0.2, TA3, TR3, TT3, med={"opo": "5", "hip": "13", "adj": lambda tt: "12" if tt >= c1 else "?"},
            tm={"opo": a1, "hip": a1 + 0.5, "adj": a1 + 1.0}, cores={"opo": (a1, OPO), "hip": (a1 + 0.5, HIP), "adj": (c1, ADJ)})
    E.saida(c, t, d1 - 0.3, tri3)
    if t >= d1 - 0.3:
        ciclo(c, t, d1 - 0.3, CX, CY, CR)
        quadrante(c, t, d1 - 0.1, CX, CY, CR, 3, rot=False)
        marca(c, t, d1, CX, CY, CR, X3, None)
        tri_ciclo(c, t, CX, CY, CR, X3, td=d1 + 0.2, tf=d1 + 0.2, ts=d1 + 0.3, rs="−f{5}{13}", tc=d1 + 0.5, rc="−f{12}{13}", size=54)

    def onze():
        E.frase(c, t, C["s11"] + 0.1, ps("vamos lá, pelo triângulo", "i", 60, COR), X, 170, "center", 0.1)
        E.frase(c, t, a1, [("oposto 5,", "g", 60, OPO), ("hipotenusa 13", "g", 60, HIP)], X, 300, "center", 0.1)
        cf_em(c, t, b1, [("169 − 25 = 144", TINTA)], X, 450, 76, "center")
        cf_em(c, t, c1, [("r{144} = 12", ADJ)], X, 610, 76, "center")
        E.frase(c, t, d1, ps("no 3º: à esquerda e embaixo", "i", 52, TINTA2), X, 760, "center", 0.07)
        resp(c, t, d1 + 1.0, [("cos x = −f{12}{13}", BR)], X, 900, 64, 2.3, ADJ)
    E.saida(c, t, C["s12"] - 0.1, onze)
    if t < C["s12"] - 0.1:
        return
    cf_em(c, t, a2, [("tg x = ", TINTA), ("(−f{5}{13})", OPO), (" ÷ ", TINTA), ("(−f{12}{13})", ADJ)], X, 230, 66, "center")
    E.frase(c, t, a2 + 2.0, ps("os treze avos se cancelam", "i", 48, TINTA2), X, 350, "center", 0.07)
    E.frase(c, t, b2, ps("por hábito:", "i", 54, ERRADO) + [("−5/12", "g", 60, ERRADO)], X, 470, "center", 0.08)
    if t >= b2 + 1.0:
        xw = E._arranjo(ps("por hábito:", "i", 54, ERRADO) + [("−5/12", "g", 60, ERRADO)], X, "center")
        x1 = xw[1][-1]
        E.risco(c, x1 - 10, 488, x1 + E.larg("−5/12", "g", 60) + 10, 430, t, b2 + 1.0, ERRADO, 8)
    cf_em(c, t, c2, [("(−) ÷ (−) = +", CERTO)], X, 620, 72, "center")
    E.frase(c, t, c2 + 1.6, ps("to, se, ta, co: no 3º, só a", "i", 50, TINTA2) + [("tangente", "g", 54)] + ps("é positiva", "i", 50, TINTA2), X, 730, "center", 0.06)
    resp(c, t, d2, [("tg x = f{5}{12}", BR)], X, 890, 66, 2.3, CERTO)


# ---------------- questão 4 ----------------
def estufa(tinta=TINTA, tam=None):
    return [("T(t) = ", tinta), ("22", LA), (" + ", tinta), ("6", LB), (" · sen(", tinta), ("f{πt}{12}", LC), (")", tinta)]


def b_questao4(c, t, C, b):
    a3, b3, c3, d3, e3 = (C[f"s13.{k}"] for k in "abcde")
    titulo(c, t, a3, 4, "a estufa (imaginada)")
    cf_em(c, t, b3, estufa(), XE, 360, 90)
    E.frase(c, t, b3 + 1.2, ps("temperatura em", "i", 52, TINTA2) + [("°C", "g", 56)], XE, 470, "left", 0.08)
    E.frase(c, t, c3, [("t:", "g", 60, ENT)] + ps("horas a partir das", "i", 56) + [("9 h", "g", 62, ENT)], XE, 590, "left", 0.1)
    E.frase(c, t, d3, [("máxima,", "g", 62, LB), ("mínima", "g", 62, LB)] + ps("e", "i", 58) + [("período?", "g", 62, LC)], XE, 740, "left", 0.1)
    E.frase(c, t, e3, ps("a que horas fica", "i", 58) + [("mais quente?", "g", 62, ERRADO)], XE, 870, "left", 0.1)
    E.relogio(c, t, C["s14.a"], 1560, 440, 160)


PE = E.Plano(1060, 300, 720, 500, 0, 25.5, 12, 30.5)


def eixos_estufa(c, t, t0):
    P = PE
    x, y, w, h = P.caixa
    if t < t0:
        return
    q = ep(t, t0, 0.8)
    for v in (6, 12, 18, 24):
        M.line(c, P.x(v), y, P.x(v), y + h, FIO, q, 2)
    for v in (16, 22, 28):
        M.line(c, x, P.y(v), x + w, P.y(v), FIO, q, 2)
    M.arrow(c, x - 10, y + h, x + w + 40, y + h, ENT, 1.0, 6, 22, ep(t, t0, 0.7))
    M.arrow(c, x, y + h + 10, x, y - 40, SAI, 1.0, 6, 22, ep(t, t0, 0.7))
    E.foco(c, t, t0 + 0.4, 0.4, lambda a: (E.escreve(c, "t (h)", x + w - 60, y + h - 22, 42, "i", ENT, a),
                                           E.escreve(c, "°C", x - 70, y - 10, 44, "i", SAI, a)))
    for v, hr in ((0, "9 h"), (6, "15 h"), (12, "21 h"), (18, "3 h"), (24, "9 h")):
        X = P.x(v)
        E.foco(c, t, t0 + 0.3, 0.4, lambda a, X=X, v=v, hr=hr: (centro(c, str(v), X, y + h + 54, 42, "b", ENT, a),
                                                                centro(c, hr, X, y + h + 100, 36, "b", CINZA, a)))
    for v in (16, 22, 28):
        Y = P.y(v)
        E.foco(c, t, t0 + 0.3, 0.4, lambda a, Y=Y, v=v: E.escreve(c, str(v), x - 22 - E.larg(str(v), "b", 42), Y + 15, 42, "b", SAI, a))


def b_resposta4(c, t, C, b):
    a5, b5, c5, d5 = (C[f"s15.{k}"] for k in "abcd")
    a6, b6, c6, d6, e6, f6, g6 = (C[f"s16.{k}"] for k in "abcdefg")
    eixos_estufa(c, t, C["s15"])
    if t >= C["s15"] + 0.2:
        M.line(c, PE.x(0), PE.y(22), PE.x(25.5), PE.y(22), LA, 1.0, 5, dash=E.TRACO, progress=ep(t, C["s15"] + 0.2, 0.8))
    E.curva(c, t, C["s15"] + 0.4, PE, T_est, 0, 24, d=1.6, cor=OPO, largura=8)
    E.ponto(c, t, a5, PE, 6, 28, None, cor=LB, r=14)
    E.ponto(c, t, b5, PE, 18, 16, None, cor=LB, r=14)
    if t >= c5:
        E.chave(c, PE.x(0), PE.x(24), PE.y(30.2), LC, ease_out(prog(t, c5, 0.6)), -24, 6)
        E.foco(c, t, c5 + 0.3, 0.4, lambda a: E.formula(c, "24 h", PE.x(12), PE.y(30.2) - 44, 50, "g", LC, a, "center"))
    E.foco(c, t, e6, 0.4, lambda a: E.formula(c, "15 h", PE.x(6) + 28, PE.y(28) - 18, 46, "g", ERRADO, a))
    E.foco(c, t, g6, 0.4, lambda a: E.formula(c, "3 h", PE.x(18) + 28, PE.y(16) + 56, 46, "g", ADJ, a))

    def quinze():
        E.frase(c, t, C["s15"] + 0.1, ps("vamos lá", "i", 62, COR), XE, 150, "left", 0.1)
        cf_em(c, t, a5, [("máx = ", TINTA), ("22", LA), (" + ", TINTA), ("6", LB), (" = 28 °C", TINTA)], XE, 320, 72)
        cf_em(c, t, b5, [("mín = ", TINTA), ("22", LA), (" − ", TINTA), ("6", LB), (" = 16 °C", TINTA)], XE, 480, 72)
        cf_em(c, t, c5, [("f{πt}{12}", LC), ("  →  período = 2 · 12 = 24 h", TINTA)], XE, 650, 60)
        resp(c, t, d5, [("repete todo dia", BR)], XE + 260, 820, 60, cor=LC)
    E.saida(c, t, C["s16"] - 0.1, quinze)
    if t < C["s16"] - 0.1:
        return
    cf_em(c, t, a6, [("sen = 1 em 90° = ", TINTA), ("f{π}{2}", LC)], XE, 170, 56)
    cf_em(c, t, b6, [("f{πt}{12} = f{π}{2}", LC)], XE, 300, 60)
    cf_em(c, t, c6, [("f{t}{12} = f{1}{2}", TINTA)], XE + 310, 300, 60)
    cf_em(c, t, d6, [("t = 6", TINTA)], XE + 580, 300, 60)
    resp(c, t, e6, [("9 h + 6 h = 15 h", BR)], XE + 300, 450, 58, cor=ERRADO)
    E.frase(c, t, e6 + 1.6, ps("perto da hora mais quente do dia", "i", 46, TINTA2), XE, 560, "left", 0.06)
    cf_em(c, t, f6, [("sen = −1 em ", TINTA), ("f{3π}{2}", LC), ("  →  t = 18", TINTA)], XE, 700, 58)
    cf_em(c, t, f6 + 6.0, [("9 + 18 = 27  →  27 − 24 = 3", TINTA)], XE, 840, 56)
    resp(c, t, g6, [("3 h da madrugada", BR)], XE + 300, 970, 58, cor=ADJ)


# ---------------- fechamento ----------------
def b_fim(c, t, C, b):
    def resumo():
        E.frase(c, t, C["s17"] + 0.2, [("resumindo", "i", 92, COR)], W / 2, 200, "center")
        itens = (("s17.a", ps("no ciclo:", "i", 58) + [("tire as voltas, ache o quadrante, reduza", "g", 58, COR)]),
                 ("s17.b", ps("o tamanho vem da", "i", 58) + [("conta,", "g", 62)] + ps("o sinal, do", "i", 58) + [("quadrante", "g", 62, COR)]),
                 ("s17.c", ps("na onda:", "i", 58) + [("máx, mín e período", "g", 62, LC)] + ps("em três contas", "i", 58)))
        for i, (k, partes) in enumerate(itens):
            y = 380 + i * 200
            E.foco(c, t, C[k], 0.5, lambda a, i=i, y=y: (E.bola(c, 230, y - 30, 56, a=a),
                                                         E.centro(c, str(i + 1), 230, y - 7, 64, "g", E.SOBRE, a)))
            E.frase(c, t, C[k] + 0.1, partes, 320, y, "left", 0.1)
    E.saida(c, t, C["s18"] - 0.1, resumo)
    if t < C["s18"]:
        return
    a8, b8, c8 = C["s18.a"], C["s18.b"], C["s18.c"]
    E.frase(c, t, C["s18"] + 0.2, ps("você fecha a trilha de", "i", 64) + [("trigonometria", "g", 70, COR)], XE, 190, passo=0.1)
    E.frase(c, t, a8, ps("na próxima aula, a matemática", "i", 62) + [("ganha volume", "g", 70, COR)], XE, 320, passo=0.1)
    E.frase(c, t, b8, ps("sólidos:", "i", 58) + [("faces, arestas e vértices", "g", 62)], XE, 450, passo=0.1)
    E.frase(c, t, c8, ps("e a", "i", 58) + [("relação de Euler", "g", 64, COR)], XE, 570, passo=0.1)
    E.cubo(c, t, a8 + 0.3, 1230, 700, 170)
    E.foco(c, t, C["s18.d"], 0.5, lambda a: E.pilula(c, "Inscreva-se", 1440, 790, 76, estilo="g", a=a, cor=E.SOBRE))
    p = ease_io(prog(t, C["s18.d"] + 0.3, 0.8))
    E.cursor(c, lerp(1770, 1570, p), lerp(1030, 815, p), ep(t, C["s18.d"] + 0.2, 0.4))
    E.frase(c, t, C["s18.e"], [("bons", "i", 130), ("estudos!", "i", 130, COR)], W / 2, 980, "center")


BLOCKS = dict(gancho=b_gancho, lembrete=b_lembrete, questao1=b_questao1, resposta1=b_resposta1, questao2=b_questao2, resposta2=b_resposta2,
              questao3=b_questao3, resposta3=b_resposta3, questao4=b_questao4, resposta4=b_resposta4, fim=b_fim)
