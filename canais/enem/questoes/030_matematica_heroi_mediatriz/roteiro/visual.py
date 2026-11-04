"""Visual — Estudativo · Questão de Matemática 030 (aula horizontal 1920x1080): ENEM 2025, questão 147, o herói e os dois
vilões (mediatriz, coeficiente angular e equação da reta). Design system de matemática: _ferramentas/matematica.py.
Cores com função: âmbar = os dados do enunciado (S, V) e o Δx, ciano = a ferramenta (a reta, o Δy, o ponto médio),
menta = o herói e o caminho certo, coral = os vilões e as alternativas erradas.
Figura: o plano cartesiano à esquerda (plano(), P()), com o quadrado STUV, os personagens (heroi(), vilao()), a mediatriz
(reta()) e os degraus Δx/Δy (degrau())."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_030_matematica_heroi_mediatriz.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.b": "data", "01.c": "data", "01.e": "shimmer", "02.b": "data", "02.c": "confirm", "02.d": "lock",
        "03.b": "data", "03.c": "data", "03.d": "confirm", "04.b": "data", "04.c": "lock", "05.c": "data",
        "05.d": "data", "05.e": "confirm", "06.b": "data", "06.c": "data", "06.d": "confirm", "07.b": "data",
        "07.c": "confirm", "08.b": "data", "08.c": "data", "08.d": "impact", "09.b": "confirm", "09.c": "impact",
        "10.b": "deny", "10.c": "deny", "11.b": "alert", "12.a": "shimmer", "13.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 030", "QUESTÃO DE MATEMÁTICA · 030"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_med=("TOOL 1 · PERPENDICULAR BISECTOR", "FERRAMENTA 1 · MEDIATRIZ"),
    s_coef=("TOOL 2 · SLOPE", "FERRAMENTA 2 · COEFICIENTE ANGULAR"),
    s_eq=("TOOL 3 · EQUATION OF A LINE", "FERRAMENTA 3 · EQUAÇÃO DA RETA"),
    s_t=("STEP 1 · WHERE IS T?", "PASSO 1 · ONDE ESTÁ T?"), s_pm=("STEP 2 · MIDPOINT", "PASSO 2 · PONTO MÉDIO"),
    s_inc=("STEP 3 · THE SLOPE", "PASSO 3 · A INCLINAÇÃO"), s_eqf=("STEP 4 · THE EQUATION", "PASSO 4 · A EQUAÇÃO"),
    s_resp=("THE ANSWER", "A RESPOSTA"), s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"),
    s_des=("CHALLENGE", "DESAFIO"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 147", "ENEM 2025 · questão 147"), jogo=("a game: 1 hero × 2 villains", "jogo: 1 herói × 2 vilões"),
    viloes=("villains: V(8; 6) and T", "vilões: V(8; 6) e T"), heroi=("hero starts at S(6; 2)", "herói começa em S(6; 2)"),
    mesma=("same distance from both", "mesma distância dos dois"), pede=("equation of the path?", "equação do caminho?"),
    t_med=("bisector", "mediatriz"), t_coef=("slope", "coeficiente angular"), t_eq=("equation of a line", "equação da reta"),
    l_heroi=("hero", "herói"), l_viloes=("villains", "vilões"),
    m1=("equidistant from A and B", "mesma distância de A e de B"), m2=("= the bisector of AB", "= a mediatriz de AB"),
    m3=("goes through the midpoint", "passa pelo ponto médio"), m4=("meets AB at a right angle", "corta AB em ângulo reto"),
    c1=("slope m = how steep", "coeficiente m = inclinação"), c2=("y per step of x", "quanto y sobe por passo de x"),
    c3=("m = Δy ÷ Δx", "m = Δy ÷ Δx"), c4=("perpendicular: m₁ · m₂ = −1", "perpendiculares: m₁ · m₂ = −1"),
    c5=("1/3 · (−3) = −1", "1/3 · (−3) = −1"),
    e1=("1 point (x₀; y₀)", "1 ponto (x₀; y₀)"), e2=("+ the slope m", "+ o coeficiente m"),
    e3=("y − y₀ = m(x − x₀)", "y − y₀ = m(x − x₀)"),
    q1=("STUV is a square", "STUV é um quadrado"), q2=("S → V: (+2; +4)", "S → V: (+2; +4)"),
    q3=("turn 90°: swap, flip a sign", "girar 90°: troca e muda um sinal"), q4=("S → T: (−4; +2)", "S → T: (−4; +2)"),
    q5=("T = (6 − 4; 2 + 2)", "T = (6 − 4; 2 + 2)"), q6=("T(2; 4)", "T(2; 4)"),
    p1=("midpoint of TV", "ponto médio de TV"), p2=("x: (2 + 8) ÷ 2 = 5", "x: (2 + 8) ÷ 2 = 5"),
    p3=("y: (4 + 6) ÷ 2 = 5", "y: (4 + 6) ÷ 2 = 5"), p4=("M(5; 5)", "M(5; 5)"),
    i1=("T → V: Δy = 2 · Δx = 6", "T → V: Δy = 2 · Δx = 6"), i2=("m(TV) = 2/6 = 1/3", "m(TV) = 2/6 = 1/3"),
    i3=("bisector: m = −3", "mediatriz: m = −3"), i4=("1/3 · (−3) = −1 ✓", "1/3 · (−3) = −1 ✓"),
    f1=("M(5; 5) · m = −3", "M(5; 5) · m = −3"), f2=("y − 5 = −3(x − 5)", "y − 5 = −3(x − 5)"),
    f3=("y − 5 = −3x + 15", "y − 5 = −3x + 15"), f4=("y = −3x + 20", "y = −3x + 20"),
    r1=("S(6; 2): −3 · 6 + 20 = 2 ✓", "S(6; 2): −3 · 6 + 20 = 2 ✓"),
    r2=("U(4; 8): −3 · 4 + 20 = 8 ✓", "U(4; 8): −3 · 4 + 20 = 8 ✓"),
    r3=("the other diagonal!", "a outra diagonal!"), alt=("ANSWER", "ALTERNATIVA"),
    pA=("y = −3x + 20 ✓", "y = −3x + 20 ✓"), pB=("y = −3x + 16 → at x = 5, y = 1", "y = −3x + 16 → x = 5 dá y = 1"),
    pC=("y = −3x − 20 → at x = 5, y = −35", "y = −3x − 20 → x = 5 dá y = −35"),
    pD=("y = 3x + 16 → sign not flipped", "y = 3x + 16 → sinal não trocou"),
    pE=("y = 3x − 16 → sign not flipped", "y = 3x − 16 → sinal não trocou"),
    l_mais3=("m = +3 ✗", "m = +3 ✗"), l_b=("(5; 1) ≠ M", "(5; 1) ≠ M"),
    des1=("the line through", "a reta que passa"), des2=("both villains, T and V", "pelos dois vilões, T e V"),
    des3=("what's its equation?", "qual é a equação?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["same distance from 2 points → bisector", "it goes through the midpoint", "its slope: flip it, change the sign"],
            ["mesma distância de 2 pontos → mediatriz", "ela passa pelo ponto médio", "coeficiente: inverte e troca o sinal"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Equation", "of a line"), ("Midpoint", "and distance"), ("Perpendicular", "lines")],
           [("Equação", "da reta"), ("Ponto médio", "e distância"), ("Retas", "perpendiculares")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("mais perto", "mais perto"), ("noventa graus", "90°"),
    ("oito e seis", "(8; 6)"), ("seis e dois", "(6; 2)"), ("dois e quatro", "(2; 4)"), ("cinco e cinco", "(5; 5)"),
    ("ípsilon zero", "y₀"), ("xis zero", "x₀"), ("ípsilons", "y"), ("ípsilon", "y"), ("três xis", "3x"), ("xis", "x"),
    ("eme", "m"), ("um terço", "1/3"), ("dois sobre seis", "2/6")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

S_, V_, T_, U_, M_ = (6, 2), (8, 6), (2, 4), (4, 8), (5, 5)


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- peças
@lru_cache(None)
def _img(nome):
    from pathlib import Path
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / nome))


def _card_img(c, img, a, w=820, cx=LX, cy=545, hmax=830):
    h = img.height() * w / img.width()
    if h > hmax:
        h = hmax
        w = img.width() * h / img.height()
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x - 14, y - 14, w + 28, h + 28, 18, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


def _dash(col, a, w=3, on=10):
    p = paint(col, a, stroke=w)
    p.setPathEffect(skia.DashPathEffect.Make([on, on], 0))
    return p


OX, OY, UN = 190, 870, 68   # origem do plano e pixels por unidade
XMAX, YMAX = 10, 9


def P(x, y):
    return OX + x * UN, OY - y * UN


def plano(c, a):
    """plano cartesiano 0..10 × 0..9 com a grade fraca e os números de 2 em 2"""
    if a <= 0:
        return
    for i in range(1, XMAX + 1):
        c.drawLine(*P(i, 0), *P(i, YMAX), paint(INK2, 0.12 * a, stroke=1))
    for j in range(1, YMAX + 1):
        c.drawLine(*P(0, j), *P(XMAX, j), paint(INK2, 0.12 * a, stroke=1))
    seta(c, *P(0, 0), P(XMAX, 0)[0] + 26, OY, WHITE, 0.8 * a, 3, 14)
    seta(c, *P(0, 0), OX, P(0, YMAX)[1] - 26, WHITE, 0.8 * a, 3, 14)
    for i in range(2, XMAX + 1, 2):
        text_mid(c, str(i), *P(i, -0.45), 22, "extrabold", INK2, a)
    for j in range(2, YMAX + 1, 2):
        text_mid(c, str(j), P(-0.4, j)[0], P(0, j)[1], 22, "extrabold", INK2, a)
    text_mid(c, "x", P(XMAX, 0)[0] + 30, OY - 30, 28, "black", INK2, a)
    text_mid(c, "y", OX + 30, P(0, YMAX)[1] - 26, 28, "black", INK2, a)


def seta(c, x0, y0, x1, y1, cor, a, w=5, cab=18):
    if a <= 0:
        return
    c.drawLine(x0, y0, x1, y1, paint(cor, a, stroke=w, cap_round=True))
    ang = math.atan2(y1 - y0, x1 - x0)
    for s in (2.6, -2.6):
        c.drawLine(x1, y1, x1 + cab * math.cos(ang + s), y1 + cab * math.sin(ang + s), paint(cor, a, stroke=w, cap_round=True))


def _clip(px, py, dx, dy):
    """trecho da reta (px, py) + s(dx, dy) dentro do plano: (s0, s1)"""
    s0, s1 = -1e9, 1e9
    for p, d, lo, hi in ((px, dx, 0, XMAX), (py, dy, 0, YMAX)):
        if abs(d) < 1e-9:
            if not lo <= p <= hi:
                return None
            continue
        a_, b_ = (lo - p) / d, (hi - p) / d
        s0, s1 = max(s0, min(a_, b_)), min(s1, max(a_, b_))
    return (s0, s1) if s0 < s1 else None


def reta(c, px, py, dx, dy, a, cor=CYA, u=1.0, w=6, tracej=False, inv=False):
    """reta pelo ponto (px, py) com direção (dx, dy), cortada no plano; u = quanto já foi desenhado (do centro para fora)"""
    if a <= 0 or u <= 0:
        return
    r = _clip(px, py, dx, dy)
    if not r:
        return
    s0, s1 = r
    m = (s0 + s1) / 2
    s0, s1 = m + (s0 - m) * u, m + (s1 - m) * u
    p = _dash(cor, a, w, 14) if tracej else paint(cor, a, stroke=w, cap_round=True)
    c.drawLine(*P(px + s0 * dx, py + s0 * dy), *P(px + s1 * dx, py + s1 * dy), p)


def segmento(c, p0, p1, a, cor=WHITE, w=5, u=1.0, tracej=False):
    if a <= 0 or u <= 0:
        return
    x1, y1 = p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u
    p = _dash(cor, a, w, 10) if tracej else paint(cor, a, stroke=w, cap_round=True)
    c.drawLine(*P(*p0), *P(x1, y1), p)


def ponto(c, x, y, a, cor=WHITE, rot=None, dx=0, dy=-40, k=1.0, r=11, size=30):
    if a <= 0 or k <= 0:
        return
    sx, sy = P(x, y)
    c.drawCircle(sx, sy, r * k, paint(cor, a))
    if rot:
        text_mid(c, rot, sx + dx, sy + dy, size, "black", cor, a)


def vilao(c, x, y, a, k=1.0, rot=None, dx=0, dy=-56):
    """vilão: bola coral com dois chifres"""
    if a <= 0 or k <= 0:
        return
    sx, sy = P(x, y)
    c.save(); c.translate(sx, sy); c.scale(k, k)
    for s in (-1, 1):
        p = skia.Path(); p.moveTo(s * 8, -20); p.lineTo(s * 22, -34); p.lineTo(s * 18, -12); p.close()
        c.drawPath(p, paint(RED, a))
    c.drawCircle(0, 0, 22, paint(RED, a))
    for s in (-1, 1):
        c.drawLine(s * 12, -8, s * 4, -3, paint(BG0, a, stroke=4, cap_round=True))
    c.restore()
    if rot:
        text_mid(c, rot, sx + dx, sy + dy, 32, "black", RED, a)


def heroi(c, x, y, a, k=1.0, rot=None, dx=0, dy=-56):
    """herói: bola menta com uma estrela"""
    if a <= 0 or k <= 0:
        return
    sx, sy = P(x, y)
    c.save(); c.translate(sx, sy); c.scale(k, k)
    c.drawCircle(0, 0, 22, paint(MNT, a))
    p = skia.Path()
    for i in range(10):
        r = 13 if i % 2 == 0 else 5.5
        an = -math.pi / 2 + i * math.pi / 5
        (p.moveTo if i == 0 else p.lineTo)(r * math.cos(an), r * math.sin(an))
    p.close()
    c.drawPath(p, paint(BG0, a))
    c.restore()
    if rot:
        text_mid(c, rot, sx + dx, sy + dy, 32, "black", MNT, a)


def degrau(c, p0, p1, a, t, tx, ty, rx=None, ry=None, cx=AMB, cy=CYA, fx=0.5):
    """Δx (horizontal, âmbar) e depois Δy (vertical, ciano) de p0 até p1"""
    kx, ky = ep(t, tx, 0.6), ep(t, ty, 0.6)
    canto = (p1[0], p0[1])
    if kx > 0:
        segmento(c, p0, canto, a, cx, 6, kx)
        if rx:
            sx, sy = P(p0[0] + (p1[0] - p0[0]) * fx, p0[1])
            label(c, rx, sx, sy + 34 if p1[1] > p0[1] else sy - 34, a * kx, 30, cx, "black")
    if ky > 0:
        segmento(c, canto, p1, a, cy, 6, ky)
        if ry:
            sx, sy = P(p1[0], (p0[1] + p1[1]) / 2)
            label(c, ry, sx + (54 if p1[0] >= p0[0] else -54), sy, a * ky, 30, cy, "black")


def angulo_reto(c, p, d1, d2, a, s=22, cor=WHITE):
    """marquinha de ângulo reto no ponto p (coordenadas) entre as direções d1 e d2"""
    if a <= 0:
        return
    sx, sy = P(*p)
    u = [(d[0] / math.hypot(*d), -d[1] / math.hypot(*d)) for d in (d1, d2)]
    q = skia.Path()
    q.moveTo(sx + u[0][0] * s, sy + u[0][1] * s)
    q.lineTo(sx + (u[0][0] + u[1][0]) * s, sy + (u[0][1] + u[1][1]) * s)
    q.lineTo(sx + u[1][0] * s, sy + u[1][1] * s)
    c.drawPath(q, paint(cor, a, stroke=3))


def quadrado(c, a, fill=0.12, cor=CYA):
    if a <= 0:
        return
    p = skia.Path()
    for i, q in enumerate((S_, V_, U_, T_)):
        (p.moveTo if i == 0 else p.lineTo)(*P(*q))
    p.close()
    c.drawPath(p, paint(cor, fill * a))
    c.drawPath(p, paint(cor, 0.7 * a, stroke=3))


def _cena_base(c, a, t, t_t=None, quad=0.0, s_dx=-36):
    """plano + S (herói) + V (vilão) + T (vilão, a partir de t_t)"""
    plano(c, a)
    quadrado(c, a * quad)
    heroi(c, *S_, a, rot="S", dx=s_dx, dy=36)
    vilao(c, *V_, a, rot="V", dx=40, dy=-30)
    if t_t is not None:
        vilao(c, *T_, a * ep(t, t_t, 0.2), k=pop(t, t_t, 0.35), rot="T", dx=-40, dy=-30)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao.png"), a, cx=310, cy=530, hmax=790)
    ke = ep(t, te, 0.4)
    kb = a * ep(t, tb, 0.3) * (1 - ke)   # o herói no meio dos dois vilões
    if kb > 0:
        cx = 735
        vilao_tela(c, cx, 300, kb, pop(t, tb + 2.4, 0.35), "V")
        vilao_tela(c, cx, 700, kb, pop(t, tb + 4.6, 0.35), "T")
        heroi_tela(c, cx, 500, kb, pop(t, tb + 6.2, 0.35), "S")
        kc = kb * ep(t, tc + 2.1, 0.4)
        if kc > 0:
            for y0, y1 in ((470, 330), (530, 670)):
                c.drawLine(cx + 40, y0, cx + 40, y0 + (y1 - y0) * kc, _dash(AMB, kc, 4, 8))
            label(c, "=", cx + 90, 500, kc, 56, AMB, "black")
    popill(c, L["t_med"], 735, 330, 34, CYA, BG0, a * ke, t, te + 1.3)
    popill(c, L["t_coef"], 735, 500, 30, AMB, BG0, a * ke, t, te + 2.3)
    popill(c, L["t_eq"], 735, 670, 32, MNT, BG0, a * ke, t, te + 3.6)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 36, INK2, "extrabold")
    label(c, L["jogo"], RX, 310, a, 46, WHITE, "black")
    eq(c, [(L["viloes"], RED)], 430, a * ep(t, tb + 2.4, 0.3), 46)
    eq(c, [(L["heroi"], MNT)], 540, a * ep(t, tb + 6.2, 0.3), 46)
    eq(c, [(L["mesma"], AMB)], 660, a * ep(t, tc + 2.1, 0.3), 46)
    eq(c, [(L["pede"], CYA)], 800, a * ep(t, td, 0.3), 50, box=CYA)


def vilao_tela(c, x, y, a, k, rot):
    vilao(c, (x - OX) / UN, (OY - y) / UN, a, k=k * 1.5)
    label(c, rot, x - 80, y, a * k, 44, RED, "black")


def heroi_tela(c, x, y, a, k, rot):
    heroi(c, (x - OX) / UN, (OY - y) / UN, a, k=k * 1.5)
    label(c, rot, x - 80, y, a * k, 44, MNT, "black")


A2, B2 = (2, 2), (7, 6)   # pontos genéricos da ferramenta 1
M2 = (4.5, 4)
D2 = (-4, 5)


def b_mediatriz(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_med"], a)
    plano(c, a)
    kb = a * ep(t, tb + 0.6, 0.3)
    segmento(c, A2, B2, kb, INK2, 3, tracej=True)
    ponto(c, *A2, kb, AMB, "A", dx=-30, dy=26, k=pop(t, tb + 0.6))
    ponto(c, *B2, kb, AMB, "B", dx=30, dy=-26, k=pop(t, tb + 0.7))
    n = math.hypot(*D2)
    for j, d in enumerate((-3.4, -1.8, 1.8, 3.4)):   # pontos à mesma distância de A e de B
        q = (M2[0] + d * D2[0] / n, M2[1] + d * D2[1] / n)
        k = a * ep(t, tb + 1.8 + j * 0.6, 0.3) * (1 - 0.6 * ep(t, td, 0.3))
        if k <= 0:
            continue
        segmento(c, q, A2, k * 0.8, AMB, 3, tracej=True)
        segmento(c, q, B2, k * 0.8, AMB, 3, tracej=True)
        ponto(c, *q, k, CYA, k=pop(t, tb + 1.8 + j * 0.6))
    reta(c, *M2, *D2, a, CYA, u=ep(t, tc, 1.0), w=6)
    kd = a * ep(t, td + 0.8, 0.3)
    ponto(c, *M2, kd, CYA, "M", dx=46, dy=10, k=pop(t, td + 0.8), r=13)
    angulo_reto(c, M2, (B2[0] - A2[0], B2[1] - A2[1]), D2, a * ep(t, td + 3.2, 0.3), 26)
    board(c, a)
    eq(c, [(L["m1"], AMB)], 300, a * ep(t, tb + 1.8, 0.3), 44)
    eq(c, [(L["m2"], CYA)], 420, a * ep(t, tc + 0.8, 0.3), 50, box=CYA)
    eq(c, [(L["m3"], WHITE)], 580, a * ep(t, td + 0.8, 0.3), 42)
    eq(c, [(L["m4"], WHITE)], 700, a * ep(t, td + 3.2, 0.3), 42)


def b_coeficiente(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_coef"], a)
    plano(c, a)
    p0, p1 = (2, 2), (5, 3)
    reta(c, *p0, 3, 1, a, CYA, u=ep(t, tb, 0.8))
    degrau(c, p0, p1, a, t, tb + 2.0, tb + 2.6, "Δx = 3", "Δy = 1")
    ponto(c, *p0, a * ep(t, tb + 2.0, 0.3), WHITE)
    ponto(c, *p1, a * ep(t, tb + 2.0, 0.3), WHITE)
    kd = ep(t, td + 0.6, 0.3)
    reta(c, *p1, -1, 3, a, MNT, u=ep(t, td + 0.6, 0.8))
    angulo_reto(c, p1, (3, 1), (-1, 3), a * ep(t, td + 1.6, 0.3), 24)
    label(c, "1/3", *P(8.4, 5.3), a * ep(t, td + 5.2, 0.3), 34, CYA, "black")
    label(c, "−3", *P(4.1, 7.4), a * kd * ep(t, td + 6.1, 0.3), 34, MNT, "black")
    board(c, a)
    eq(c, [(L["c1"], WHITE)], 290, a * ep(t, tb, 0.3), 44)
    eq(c, [(L["c2"], INK2)], 380, a * ep(t, tb + 2.0, 0.3), 36)
    eq(c, [("m = ", WHITE), ("Δy", CYA), (" ÷ ", WHITE), ("Δx", AMB)], 520, a * ep(t, tc + 1.3, 0.3), 64, box=CYA)
    eq(c, [(L["c4"], MNT)], 680, a * ep(t, td + 0.6, 0.3), 42)
    eq(c, [(L["c5"], WHITE)], 790, a * ep(t, td + 5.2, 0.3), 50)


def b_equacao(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_eq"], a)
    plano(c, a)
    p0 = (4, 4)
    kp = a * ep(t, tb + 0.6, 0.3)
    ang = math.radians(75 - 48.4 * ep(t, tb + 1.8, 1.4))   # a reta gira até m = 1/2
    reta(c, *p0, math.cos(ang), math.sin(ang), a * ep(t, tb + 1.8, 0.3), CYA)
    ponto(c, *p0, kp, AMB, "(x₀; y₀)", dx=0, dy=44, k=pop(t, tb + 0.6), r=13, size=30)
    if t >= tb + 3.2:
        degrau(c, (6, 5), (8, 6), a, t, tb + 3.2, tb + 3.6, None, "m")
    board(c, a)
    eq(c, [(L["e1"], AMB)], 320, kp, 50)
    eq(c, [(L["e2"], CYA)], 440, a * ep(t, tb + 1.8, 0.3), 50)
    eq(c, [("y − ", WHITE), ("y₀", AMB), (" = ", WHITE), ("m", CYA), ("(x − ", WHITE), ("x₀", AMB), (")", WHITE)],
       640, a * ep(t, tc, 0.3), 66, box=CYA)


def b_ponto_t(c, t, C, B):
    ta, tb, tc, td, te = (C[f"05.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_t"], a)
    ke = ep(t, te + 0.4, 0.3)
    _cena_base(c, a, t, te + 0.4, quad=ep(t, te + 2.0, 0.6))
    kq = a * ep(t, tb, 0.3) * (1 - ke)   # o "?" onde deveria estar T
    if kq > 0:
        label(c, "T = ?", *P(T_[0] - 0.2, T_[1] + 0.9), kq * (0.6 + 0.4 * math.sin(t * 5) ** 2), 40, RED, "black")
    kc = a * (1 - 0.65 * ep(t, td + 6.4, 0.4))
    degrau(c, S_, V_, kc, t, tc + 2.4, tc + 3.9, "+2", "+4")
    kg = a * ep(t, td + 2.8, 0.3)   # o lado S→V gira 90° em torno de S
    if kg > 0 and t < td + 7.0:
        g = math.pi / 2 * ep(t, td + 2.8, 1.4)
        vx, vy = 2 * math.cos(g) - 4 * math.sin(g), 2 * math.sin(g) + 4 * math.cos(g)
        seta(c, *P(*S_), *P(S_[0] + vx, S_[1] + vy), AMB, kg * (1 - ep(t, td + 6.6, 0.4)), 6, 20)
    degrau(c, S_, T_, a, t, td + 6.8, td + 8.4, "−4", "+2")
    board(c, a)
    eq(c, [(L["q1"], WHITE)], 280, a * ep(t, tb + 1.3, 0.3), 44)
    eq(c, [(L["q2"], AMB)], 390, a * ep(t, tc + 2.4, 0.3), 48)
    eq(c, [(L["q3"], INK2)], 500, a * ep(t, td + 2.8, 0.3), 38)
    eq(c, [(L["q4"], AMB)], 610, a * ep(t, td + 6.8, 0.3), 48)
    eq(c, [(L["q6"], RED)], 780, a * ke, 64, box=RED)


def b_ponto_medio(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_pm"], a)
    _cena_base(c, a, t, -1, quad=0.4)
    segmento(c, T_, V_, a * ep(t, ta + 2.0, 0.3), WHITE, 4, u=ep(t, ta + 2.0, 0.6))
    kx = a * ep(t, tb + 3.6, 0.3)   # 5 no eixo x
    if kx > 0:
        segmento(c, (5, 0), (5, 5), kx, CYA, 3, tracej=True)
        ponto(c, 5, 0, kx, CYA, "5", dy=36, k=pop(t, tb + 3.6))
    ky = a * ep(t, tc + 4.7, 0.3)   # 5 no eixo y
    if ky > 0:
        segmento(c, (0, 5), (5, 5), ky, CYA, 3, tracej=True)
        ponto(c, 0, 5, ky, CYA, "5", dx=-40, dy=0, k=pop(t, tc + 4.7))
    ponto(c, *M_, a * ep(t, td + 1.0, 0.3), CYA, "M", dx=-6, dy=-40, k=pop(t, td + 1.0), r=14, size=34)
    board(c, a)
    eq(c, [(L["p1"], WHITE)], 290, a, 44)
    eq(c, [("x: (", WHITE), ("2", AMB), (" + ", WHITE), ("8", AMB), (") ÷ 2 = ", WHITE), ("5", CYA)], 430,
       a * ep(t, tb + 1.3, 0.3), 54)
    eq(c, [("y: (", WHITE), ("4", AMB), (" + ", WHITE), ("6", AMB), (") ÷ 2 = ", WHITE), ("5", CYA)], 560,
       a * ep(t, tc + 2.0, 0.3), 54)
    eq(c, [(L["p4"], CYA)], 740, a * ep(t, td + 1.0, 0.3), 70, box=CYA)


def b_inclinacao(c, t, C, B):
    ta, tb, tc = (C[f"07.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_inc"], a)
    _cena_base(c, a, t, -1, quad=0.4)
    segmento(c, T_, V_, a, WHITE, 4)
    degrau(c, T_, V_, a * (1 - 0.6 * ep(t, tc, 0.4)), t, tb + 2.9, tb + 1.6, "Δx = 6", "Δy = 2", fx=0.27)
    reta(c, *M_, -1, 3, a, MNT, u=ep(t, tc + 1.0, 0.9))
    angulo_reto(c, M_, (3, 1), (-1, 3), a * ep(t, tc + 1.8, 0.3), 24)
    ponto(c, *M_, a, CYA, "M", dx=-40, dy=-10, r=12)
    board(c, a)
    eq(c, [("T → V: ", WHITE), ("Δy = 2", CYA), (" · ", INK2), ("Δx = 6", AMB)], 300, a * ep(t, tb + 1.6, 0.3), 48)
    eq(c, [("m(TV) = ", WHITE), ("2/6", WHITE), (" = ", WHITE), ("1/3", CYA)], 430, a * ep(t, tb + 5.2, 0.3), 56)
    eq(c, [(L["i3"], MNT)], 600, a * ep(t, tc + 4.5, 0.3), 58, box=MNT)
    eq(c, [(L["i4"], WHITE)], 760, a * ep(t, tc + 5.6, 0.3), 46)


def b_equacao_final(c, t, C, B):
    ta, tb, tc, td = (C[f"08.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_eqf"], a)
    _cena_base(c, a, t, -1, quad=0.4)
    segmento(c, T_, V_, a * 0.5, WHITE, 3, tracej=True)
    reta(c, *M_, -1, 3, a, MNT)
    ponto(c, *M_, a, CYA, "M", dx=-40, dy=-10, r=12)
    kd = a * ep(t, td + 1.9, 0.3)
    if kd > 0:   # a etiqueta da reta
        label(c, "y = −3x + 20", *P(7.6, 8.2), kd, 38, MNT, "black")
    board(c, a)
    eq(c, [("M(5; 5)", CYA), (" · ", INK2), ("m = −3", MNT)], 280, a * ep(t, tb + 0.5, 0.3), 50)
    eq(c, [("y − 5 = ", WHITE), ("−3", MNT), ("(x − 5)", WHITE)], 410, a * ep(t, tb + 3.7, 0.3), 58)
    eq(c, [("y − 5 = ", WHITE), ("−3x + 15", MNT)], 540, a * ep(t, tc + 1.5, 0.3), 58)
    eq(c, [(L["f4"], MNT)], 730, kd, 76, box=MNT)


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"09.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    plano(c, a)
    quadrado(c, a, 0.12 + 0.1 * ep(t, tb + 2.5, 0.4))
    reta(c, *M_, -1, 3, a, MNT)
    vilao(c, *V_, a, rot="V", dx=40, dy=-30)
    vilao(c, *T_, a, rot="T", dx=-40, dy=-30)
    ponto(c, *U_, a * ep(t, tb + 1.1, 0.3), CYA, "U", dx=36, dy=-24, k=pop(t, tb + 1.1))
    u = ep(t, tb + 0.4, 2.2)   # o herói anda de S até U pela mediatriz
    x, y = S_[0] + (U_[0] - S_[0]) * u, S_[1] + (U_[1] - S_[1]) * u
    if u > 0:
        for q, cor in ((T_, RED), (V_, RED)):
            segmento(c, (x, y), q, a * 0.7 * (1 - ep(t, tc, 0.3)), AMB, 3, tracej=True)
    heroi(c, x, y, a, rot="S" if u < 0.05 else None, dx=36, dy=36)
    board(c, a)
    eq(c, [(L["r1"], WHITE)], 280, a * ep(t, ta + 4.5, 0.3), 44)
    eq(c, [(L["r2"], WHITE)], 380, a * ep(t, tb + 1.1, 0.3), 44)
    eq(c, [(L["r3"], CYA)], 480, a * ep(t, tb + 2.5, 0.3), 46)
    kc = a * ep(t, tc, 0.3)
    if kc > 0:
        for j, le in enumerate("ABCDE"):
            xx = BX0 + 130 + j * 160
            ok = le == "A"
            c.drawCircle(xx, 620, 34, paint(MNT if ok else INK2, kc))
            text_mid(c, le, xx, 620, 36, "black", BG0, kc)
        check(c, BX0 + 130 + 38, 590, 18, kc)
        eq(c, [(L["alt"] + " ", WHITE), ("A", MNT)], 790, kc, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td = (C[f"10.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    _cena_base(c, a, t, -1, quad=0.25, s_dx=36)
    reta(c, *M_, -1, 3, a, MNT)
    ponto(c, *M_, a, CYA, "M", dx=-40, dy=-10, r=12)
    kb = a * ep(t, tb + 1.0, 0.3) * (1 - 0.7 * ep(t, tc, 0.3))   # D e E: inclinação +3
    reta(c, *M_, 1, 3, kb, RED, u=ep(t, tb + 1.0, 0.8), w=5, tracej=True)
    label(c, L["l_mais3"], *P(7.4, 8.6), kb, 34, RED, "black")
    kc = a * ep(t, tc + 0.6, 0.3)   # B: coeficiente certo, mas paralela (passa por (5; 1))
    reta(c, 5, 1, -1, 3, kc, RED, u=ep(t, tc + 0.6, 0.8), w=5, tracej=True)
    kd = a * ep(t, td + 2.4, 0.3)
    ponto(c, 5, 1, kd, RED, L["l_b"], dx=200, dy=0, k=pop(t, td + 2.4))
    board(c, a)
    linhas = (("A", L["pA"], MNT, ta), ("B", L["pB"], RED, td + 2.4), ("C", L["pC"], RED, td + 3.2),
              ("D", L["pD"], RED, tb + 0.4), ("E", L["pE"], RED, tb + 0.8))
    for j, (le, s, cor, t0) in enumerate(linhas):
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        y = 270 + j * 140
        c.drawCircle(BX0 + 70, y, 32, paint(cor, k))
        text_mid(c, le, BX0 + 70, y, 34, "black", BG0, k)
        sz = 38
        while text_w(s, "black", sz) > 720:
            sz -= 2
        text_mid(c, s, BX0 + 125, y, sz, "black", WHITE, k, align="left")


def b_desafio(c, t, C, B):
    ta, tb, tc = (C[f"11.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    plano(c, a)
    reta(c, *T_, 3, 1, a * ep(t, tb + 2.4, 0.3), AMB, u=ep(t, tb + 2.4, 0.8), w=5, tracej=True)
    vilao(c, *T_, a, k=pop(t, tb + 2.6), rot="T(2; 4)", dx=0, dy=-56)
    vilao(c, *V_, a, k=pop(t, tb + 2.9), rot="V(8; 6)", dx=0, dy=-56)
    label(c, "?", *P(5, 6.4), a * ep(t, tb + 3.0, 0.3) * (0.6 + 0.4 * math.sin(t * 5) ** 2), 80, AMB, "black")
    board(c, a)
    label(c, L["des1"], RX, 320, a * ep(t, tb, 0.3), 46, WHITE, "black")
    eq(c, [(L["des2"], RED)], 440, a * ep(t, tb + 2.4, 0.3), 54, box=RED)
    label(c, L["des3"], RX, 600, a * ep(t, tb + 0.6, 0.3), 50, CYA, "black")
    label(c, L["comenta"], RX, 740, a * ep(t, tc, 0.3), 40, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"12.{k}"] for k in "bcd"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 330 + i * 180
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 260
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 50, "black", WHITE, ki, align="left")
        check(c, 1700, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula: y = mx + n · o ponto médio · m₁ · m₂ = −1"""
    if i == 0:
        text_mid(c, "y = mx + n", cx, cy, 60, "black", CYA, a)
    elif i == 1:
        text_mid(c, "M = (x₁ + x₂) ÷ 2", cx, cy - 20, 38, "black", AMB, a)
        c.drawLine(cx - 140, cy + 50, cx + 140, cy + 50, paint(WHITE, a, stroke=4, cap_round=True))
        c.drawCircle(cx, cy + 50, 12, paint(AMB, a))
    else:
        text_mid(c, "m₁ · m₂ = −1", cx, cy, 52, "black", MNT, a)


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"13.{k}"] for k in "abcdef")
    a = fade(t, B["start"], B["end"], d_out=0.01)
    ka = a * (1 - ep(t, tf, 0.4))
    header(c, L["s_aulas"], ka)
    cores = (CYA, AMB, MNT)
    for i, (t0, (l1, l2)) in enumerate(zip((tb, tc, td), L["aulas"])):
        k = ka * pop(t, t0, 0.4)
        if k <= 0:
            continue
        x, w = 180 + i * 560, 480
        cx = x + w / 2
        c.save(); c.translate(cx, 520); c.scale(k, k); c.translate(-cx, -520)
        kk = min(1, ka)
        cartao(c, x, 260, w, 520, kk, cores[i], L["aula"])
        _icone(c, i, cx, 420, kk, t)
        sz = min(50, *(50 * (w - 50) / max(1, text_w(s_, "black", 50)) for s_ in (l1, l2) if s_))
        text_mid(c, l1, cx, 610, sz, "black", WHITE, kk)
        text_mid(c, l2, cx, 610 + sz * 1.25, sz, "black", cores[i], kk)
        c.restore()
    label(c, L["no_canal"], 960, 870, ka * ep(t, te, 0.3), 40, AMB, "extrabold")
    kg = a * ep(t, tf, 0.4)
    if kg > 0:
        glow_text(c, L["canal"], 960, 400, 120, "black", WHITE, kg, glow=0.12)
        w = text_w(L["canal"], "black", 120)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(960 - w / 2, 430, w * ep(t, tf + 0.3, 0.6), 14), 7, 7), paint(AMB, kg))
        pulse = 1 + 0.03 * math.sin(t * 5)
        c.save(); c.translate(960, 560); c.scale(pulse, pulse)
        pill(c, L["inscreva"], 0, 0, 38, CYA, BG0, kg * ep(t, tf + 0.8, 0.3))
        c.restore()
        kl = kg * ep(t, tf + 1.2, 0.4)
        for j, v in enumerate("ABCDE"):
            x = 960 - 280 + j * 140
            c.drawCircle(x, 790, 38, paint(BG1, 0.95 * kl))
            c.drawCircle(x, 790, 38, paint(MNT if v == "A" else INK2, kl, stroke=4))
            text_mid(c, v, x, 790, 38, "black", WHITE, kl)


BLOCKS = dict(gancho=b_gancho, mediatriz=b_mediatriz, coeficiente=b_coeficiente, equacao=b_equacao, ponto_t=b_ponto_t,
              ponto_medio=b_ponto_medio, inclinacao=b_inclinacao, equacao_final=b_equacao_final, resposta=b_resposta,
              pegadinhas=b_pegadinhas, desafio=b_desafio, resumo=b_resumo, aulas=b_aulas)
