"""Visual — Estudativo · Questão de Matemática 024 (aula horizontal 1920x1080): ENEM 2025, questão 144, o cubo que se move
no espaço e as suas projeções ortogonais. Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = o cubo na posição do enunciado (dado), ciano = a ferramenta (o plano em destaque, as distâncias
e as sombras), menta = o cubo e as sombras no fim (a resposta), coral = as sombras das alternativas erradas.
Figura principal: a cena da prova redesenhada em perspectiva cavaleira (cena3d()): chão xy, parede do fundo yz, parede da
esquerda xz, grade 8 × 8, eixos, o cubo de aresta 1 e as três sombras (projeções) ligadas por linhas pontilhadas."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_024_matematica_cubo_projecoes.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.d": "shimmer", "02.b": "data", "02.c": "data", "02.d": "data", "03.b": "data", "03.c": "data", "03.d": "data",
        "03.e": "lock", "04.c": "confirm", "04.d": "confirm", "05.b": "data", "05.c": "data", "05.d": "data",
        "06.b": "whoosh", "06.c": "whoosh", "06.d": "whoosh", "07.b": "confirm", "07.c": "confirm", "07.d": "confirm",
        "07.e": "impact", "08.b": "deny", "08.c": "deny", "08.d": "deny", "08.e": "confirm", "09.c": "alert",
        "11.a": "shimmer", "11.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 024", "QUESTÃO DE MATEMÁTICA · 024"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_planos=("TOOL 1 · THE THREE PLANES", "FERRAMENTA 1 · OS TRÊS PLANOS"),
    s_dist=("TOOL 2 · DISTANCE TO A PLANE", "FERRAMENTA 2 · DISTÂNCIA ATÉ UM PLANO"),
    s_proj=("TOOL 3 · ORTHOGONAL PROJECTION", "FERRAMENTA 3 · PROJEÇÃO ORTOGONAL"),
    s_ini=("STEP 1 · WHERE IT STARTS", "PASSO 1 · ONDE O CUBO COMEÇA"), s_mov=("STEP 2 · THE MOVES", "PASSO 2 · OS MOVIMENTOS"),
    s_fim=("STEP 3 · THE SHADOWS AT THE END", "PASSO 3 · AS SOMBRAS NO FIM"),
    s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"), s_des=("CHALLENGE", "DESAFIO"),
    s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 144", "ENEM 2025 · questão 144"), cubo=("a cube moving in space", "um cubo se movendo no espaço"),
    m1=("closer to yz: 3", "aproxima do yz: 3"), m2=("away from xz: 5", "afasta do xz: 5"), m3=("closer to xy: 4", "aproxima do xy: 4"),
    pede=("the projections = ?", "as projeções = ?"), p_pal=("WHAT EACH WORD MEANS", "O QUE CADA PALAVRA QUER DIZER"),
    chao=("floor → plane xy", "chão → plano xy"), fundo=("back wall → plane yz", "fundo → plano yz"),
    esq=("left wall → plane xz", "esquerda → plano xz"), nome=("name = the 2 axes in the plane", "nome = os 2 eixos do plano"),
    d_yz=("to plane yz → x", "até o plano yz → x"), d_xz=("to plane xz → y", "até o plano xz → y"),
    d_xy=("to plane xy → z (height)", "até o plano xy → z (altura)"),
    regra=("closer = smaller · away = bigger", "aproximar = diminuir · afastar = aumentar"),
    falta=("the axis MISSING from the name", "o eixo que FALTA no nome"),
    sombra=("shadow, light perpendicular", "sombra, com a luz perpendicular"),
    g_yz=("on yz: keeps y, z", "no yz: guarda y, z"), g_xz=("on xz: keeps x, z", "no xz: guarda x, z"),
    g_xy=("on xy: keeps x, y", "no xy: guarda x, y"),
    ini_x=("x: 5 to 6", "x: de 5 a 6"), ini_y=("y: 1 to 2", "y: de 1 a 2"), ini_z=("z: 6 to 7", "z: de 6 a 7"),
    mv_x=("x: 5–6 → 2–3", "x: 5–6 → 2–3"), mv_y=("y: 1–2 → 6–7", "y: 1–2 → 6–7"), mv_z=("z: 6–7 → 2–3", "z: 6–7 → 2–3"),
    f_yz=("yz: y 6–7 · z 2–3", "yz: y 6–7 · z 2–3"), f_xz=("xz: x 2–3 · z 2–3", "xz: x 2–3 · z 2–3"),
    f_xy=("xy: x 2–3 · y 6–7", "xy: x 2–3 · y 6–7"), alt=("ANSWER", "ALTERNATIVA"),
    so_fundo=("look only at the back-wall shadow", "olhe só a sombra da parede do fundo"),
    pegs=(["A · z 3–4 (swapped 3 and 4)", "B · y 4–5", "C and D · y 5–6", "E · y 6–7 · z 2–3 ✓"],
          ["A · z 3–4 (trocou 3 e 4)", "B · y 4–5", "C e D · y 5–6", "E · y 6–7 · z 2–3 ✓"]),
    des1=("then: 2 away from plane xy", "depois: afasta 2 do plano xy"), des2=("back-wall shadow: what height?", "sombra no fundo: em que altura?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["distance to a plane = the missing axis", "closer: smaller · away: bigger",
             "projection keeps the 2 axes of the name"],
            ["distância até o plano = o eixo que falta", "aproximar diminui · afastar aumenta",
             "projeção guarda os 2 eixos do nome"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Coordinates", "in space"), ("Orthogonal", "projection"), ("Views of", "solids")],
           [("Coordenadas", "no espaço"), ("Projeção", "ortogonal"), ("Vistas de", "sólidos")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("xis ípsilon", "xy"), ("ípsilon zê", "yz"), ("xis zê", "xz"),
    ("xis", "x"), ("ípsilon", "y"), ("zê", "z"), ("dois", "2"), ("passo um", "Passo 1"), ("passo dois", "Passo 2"), ("passo três", "Passo 3")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
_lingua0 = matematica._lingua
# aqui "dois a três" é um intervalo (de 2 a 3), não "2a": desliga essa regra da legenda só neste vídeo
matematica._lingua = lambda lang: (lambda r: (r[0], r[1], r[2], set(), r[4]))(_lingua0(lang))


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- a cena em 3D (perspectiva cavaleira, como na prova)
U = 54.0
O = (420.0, 722.0)
VX, VY, VZ = (-0.72 * U, 0.42 * U), (U, 0.0), (0.0, -U)   # tela por unidade de x (para frente), y, z
N = 8
INI = (5, 1, 6)   # canto do cubo de menor coordenada: posição do enunciado
FIM = (2, 6, 2)   # depois dos três movimentos


def P(x, y, z, o=O):
    return (o[0] + x * VX[0] + y * VY[0] + z * VZ[0], o[1] + x * VX[1] + y * VY[1] + z * VZ[1])


def _poly(pts):
    p = skia.Path()
    p.addPoly([skia.Point(*q) for q in pts], True)
    return p


def _tracejado(col, a, w=2.0, on=8, off=8):
    p = paint(col, a, stroke=w)
    p.setPathEffect(skia.DashPathEffect.Make([on, off], 0))
    return p


def plano(c, nome, a, tint=None, tint_a=0.0, rot=None):
    """um dos planos com a grade tracejada; tint pinta o plano (destaque); rot = rótulo no meio do plano"""
    if a <= 0:
        return
    if nome == "xy":
        f = lambda i, j: P(i, j, 0)   # noqa: E731
    elif nome == "yz":
        f = lambda i, j: P(0, i, j)   # noqa: E731
    else:
        f = lambda i, j: P(i, 0, j)   # noqa: E731
    canto = _poly([f(0, 0), f(N, 0), f(N, N), f(0, N)])
    if tint and tint_a > 0:
        c.drawPath(canto, paint(tint, 0.16 * a * tint_a))
        c.drawPath(canto, paint(tint, 0.9 * a * tint_a, stroke=3))
    for k in range(N + 1):
        c.drawLine(*f(k, 0), *f(k, N), _tracejado(INK2, 0.38 * a))
        c.drawLine(*f(0, k), *f(N, k), _tracejado(INK2, 0.38 * a))
    if rot and tint_a > 0:
        x, y = f(N / 2, N / 2)
        pill(c, rot, x, y, 26, tint, BG0, a * tint_a)


def eixos3d(c, a, numeros=0.0):
    if a <= 0:
        return
    for (dx, dy, dz), nome in (((N + 1.2, 0, 0), "x"), ((0, N + 1.2, 0), "y"), ((0, 0, N + 1.2), "z")):
        p1 = P(dx, dy, dz)
        c.drawLine(*O, *p1, paint(WHITE, a, stroke=4, cap_round=True))
        ang = math.atan2(p1[1] - O[1], p1[0] - O[0])
        s = 16
        tri = _poly([(p1[0] + math.cos(ang) * s, p1[1] + math.sin(ang) * s),
                     (p1[0] + math.cos(ang + 2.5) * s, p1[1] + math.sin(ang + 2.5) * s),
                     (p1[0] + math.cos(ang - 2.5) * s, p1[1] + math.sin(ang - 2.5) * s)])
        c.drawPath(tri, paint(WHITE, a))
        lx, ly = P(dx * 1.06 + (0.4 if nome == "z" else 0), dy * 1.06, dz * 1.04)
        text_mid(c, nome, lx + (-14 if nome == "x" else 0), ly + (14 if nome == "y" else 0), 40, "black", WHITE, a)
    if numeros > 0:   # números nas linhas da grade (o cubo vai "de 2 a 3" = entre as linhas 2 e 3)
        for k in range(1, N + 1):
            x, y = P(0, k, 0)
            text_mid(c, str(k), x, y + 26, 20, "bold", INK2, a * numeros)
            x, y = P(0, 0, k)
            text_mid(c, str(k), x - 14, y, 20, "bold", INK2, a * numeros, align="right")
            x, y = P(k, 0, 0)
            text_mid(c, str(k), x - 14, y + 8, 20, "bold", INK2, a * numeros, align="right")


def cubo(c, pos, a, cor=AMB, contorno=WHITE, glow=0.0):
    """cubo de aresta 1 com o canto (x, y, z) na menor coordenada: faces visíveis = frente (+x), lado (+y), topo (+z)"""
    if a <= 0:
        return
    x, y, z = pos
    frente = [P(x + 1, y, z), P(x + 1, y + 1, z), P(x + 1, y + 1, z + 1), P(x + 1, y, z + 1)]
    lado = [P(x + 1, y + 1, z), P(x, y + 1, z), P(x, y + 1, z + 1), P(x + 1, y + 1, z + 1)]
    topo = [P(x, y, z + 1), P(x + 1, y, z + 1), P(x + 1, y + 1, z + 1), P(x, y + 1, z + 1)]
    if glow > 0:
        cx, cy = P(x + 0.5, y + 0.5, z + 0.5)
        c.drawCircle(cx, cy, U * 1.1, blur_paint(cor, 0.45 * a * glow, 24))
    for pts, k in ((lado, 0.72), (frente, 0.88), (topo, 1.0)):
        pth = _poly(pts)
        c.drawPath(pth, paint(_escurece(cor, k), a))
        c.drawPath(pth, paint(contorno, 0.6 * a, stroke=2))


def _escurece(cor, k):
    v = [int(cor[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(x * k):02X}" for x in v)


def sombras(c, pos, a, cor=CYA, quais="yz xz xy", linhas=1.0, ks=None):
    """as três projeções ortogonais do cubo (sombra em cada plano), com as linhas pontilhadas até o cubo.
    ks = {plano: alfa} para fazer cada uma aparecer na sua hora"""
    if a <= 0:
        return
    x, y, z = pos
    ks = ks or {}
    for q in quais.split():
        k = a * ks.get(q, 1.0)
        if k <= 0:
            continue
        if q == "yz":
            sq = [P(0, y, z), P(0, y + 1, z), P(0, y + 1, z + 1), P(0, y, z + 1)]
            pares = [((x, y, z + 1), (0, y, z + 1)), ((x, y + 1, z + 1), (0, y + 1, z + 1)), ((x, y + 1, z), (0, y + 1, z))]
        elif q == "xz":
            sq = [P(x, 0, z), P(x + 1, 0, z), P(x + 1, 0, z + 1), P(x, 0, z + 1)]
            pares = [((x, y, z + 1), (x, 0, z + 1)), ((x + 1, y, z + 1), (x + 1, 0, z + 1)), ((x + 1, y, z), (x + 1, 0, z))]
        else:
            sq = [P(x, y, 0), P(x + 1, y, 0), P(x + 1, y + 1, 0), P(x, y + 1, 0)]
            pares = [((x + 1, y, z), (x + 1, y, 0)), ((x + 1, y + 1, z), (x + 1, y + 1, 0)), ((x, y + 1, z), (x, y + 1, 0))]
        if linhas > 0:
            for p0, p1 in pares:
                c.drawLine(*P(*p0), *P(*p1), _tracejado(WHITE, 0.55 * k * linhas, 2, 4, 5))
        pth = _poly(sq)
        c.drawPath(pth, blur_paint(cor, 0.35 * k, 10))
        c.drawPath(pth, paint(cor, k))


def faixa_eixo(c, eixo, v0, v1, a, cor=AMB, rot=None):
    """marca no eixo o intervalo [v0, v1] (ex.: o cubo vai de 5 a 6 no x)"""
    if a <= 0:
        return
    f = {"x": lambda v: P(v, 0, 0), "y": lambda v: P(0, v, 0), "z": lambda v: P(0, 0, v)}[eixo]
    p0, p1 = f(v0), f(v1)
    c.drawLine(*p0, *p1, blur_paint(cor, 0.6 * a, 10, stroke=16))
    c.drawLine(*p0, *p1, paint(cor, a, stroke=10, cap_round=True))
    if rot:
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        off = {"x": (-40, 24), "y": (0, 44), "z": (-44, 0)}[eixo]
        text_mid(c, rot, mx + off[0], my + off[1], 30, "black", cor, a)


def seta3d(c, p0, p1, a, cor=CYA, rot=None, w=6):
    if a <= 0:
        return
    (x0, y0), (x1, y1) = P(*p0), P(*p1)
    c.drawLine(x0, y0, x1, y1, paint(cor, a, stroke=w, cap_round=True))
    ang = math.atan2(y1 - y0, x1 - x0)
    s = 18
    c.drawPath(_poly([(x1, y1), (x1 - math.cos(ang - 0.45) * s, y1 - math.sin(ang - 0.45) * s),
                      (x1 - math.cos(ang + 0.45) * s, y1 - math.sin(ang + 0.45) * s)]), paint(cor, a))
    if rot:
        pill(c, rot, (x0 + x1) / 2, (y0 + y1) / 2, 26, cor, BG0, a)


def cena3d(c, a, numeros=0.0, tints=None):
    """os três planos + os eixos (tints = {plano: (cor, alfa, rótulo)})"""
    tints = tints or {}
    for nome in ("xy", "xz", "yz"):
        cor, ta, rot = tints.get(nome, (None, 0.0, None))
        plano(c, nome, a, cor, ta, rot)
    eixos3d(c, a, numeros)


def _lerp3(p, q, u):
    return tuple(p[i] + (q[i] - p[i]) * u for i in range(3))


def pos_mov(t, tb, tc, td, dur=1.6):
    """posição do cubo durante os movimentos: x (em tb), depois y (em tc), depois z (em td)"""
    x = lerp(INI[0], FIM[0], ease_io(prog(t, tb + 1.4, dur)))
    y = lerp(INI[1], FIM[1], ease_io(prog(t, tc + 1.4, dur)))
    z = lerp(INI[2], FIM[2], ease_io(prog(t, td + 1.4, dur)))
    return (x, y, z)


# ---------------------------------------------------------------- imagens da prova
def _card_img(c, img, a, w=760, cx=LX, cy=545, hmax=830):
    h = img.height() * w / img.width()
    if h > hmax:
        h = hmax
        w = img.width() * h / img.height()
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x - 14, y - 14, w + 28, h + 28, 18, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


@lru_cache(None)
def _img(nome):
    from pathlib import Path
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / nome))


def bolinha(c, x, y, v, a, col=INK2, fundo=BG1, glow=0.0, k=1.0, size=None):
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    if glow:
        c.drawCircle(0, 0, 46, blur_paint(col, 0.5 * a * glow, 14))
    c.drawCircle(0, 0, 42, paint(fundo, 0.95 * a))
    c.drawCircle(0, 0, 42, paint(col, a, stroke=4))
    text_mid(c, str(v), 0, 0, size or 40, "black", WHITE, a)
    c.restore()


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao_topo.png"), a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    label(c, L["cubo"], RX, 330, a, 44, WHITE, "black")
    for j, key in enumerate(("m1", "m2", "m3")):
        eq(c, [(L[key], AMB)], 440 + j * 80, a * ep(t, tb + j * 1.8, 0.3), 44)
    eq(c, [(L["pede"].split("=")[0] + "= ", WHITE), ("?", CYA)], 720, a * ep(t, tc, 0.3), 54, box=CYA)
    popill(c, L["p_pal"], RX, 840, 28, CYA, BG0, a * ep(t, td, 0.3), t, td + 0.2)


def b_planos(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_planos"], a)
    tints = {"xy": (AMB, ep(t, tb, 0.3) * (1 - 0.6 * ep(t, tc, 0.3)), "xy"),
             "yz": (CYA, ep(t, tc, 0.3) * (1 - 0.6 * ep(t, td, 0.3)), "yz"),
             "xz": (MNT, ep(t, td, 0.3), "xz")}
    if t >= te:
        tints = {k: (v[0], 1.0, v[2]) for k, v in tints.items()}
    cena3d(c, a * ep(t, ta, 0.4), tints=tints)
    board(c, a)
    for j, (key, col, t0) in enumerate((("chao", AMB, tb), ("fundo", CYA, tc), ("esq", MNT, td))):
        label(c, L[key], RX, 300 + j * 110, a * ep(t, t0, 0.3), 46, col, "black")
    eq(c, [(L["nome"], WHITE)], 680, a * ep(t, te, 0.3), 40, box=AMB)


def b_distancia(c, t, C, B):
    ta, tb, tc, td, te = (C[f"03.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_dist"], a)
    tints = {"yz": (CYA, ep(t, tb, 0.3) * (1 - ep(t, tc, 0.3)), None), "xz": (CYA, ep(t, tc, 0.3) * (1 - ep(t, td, 0.3)), None),
             "xy": (CYA, ep(t, td, 0.3) * (1 - ep(t, te, 0.3)), None)}
    cena3d(c, a, tints=tints)
    x, y, z = INI
    cubo(c, INI, a, AMB)
    seta3d(c, (x, y + 0.5, z + 0.5), (0.05, y + 0.5, z + 0.5), a * ep(t, tb + 1.0, 0.3), CYA, "x")
    seta3d(c, (x + 0.5, y, z + 0.5), (x + 0.5, 0.05, z + 0.5), a * ep(t, tc + 0.6, 0.3), CYA, "y")
    seta3d(c, (x + 0.5, y + 0.5, z), (x + 0.5, y + 0.5, 0.05), a * ep(t, td + 0.8, 0.3), CYA, "z")
    board(c, a)
    label(c, L["falta"], RX, 260, a * ep(t, tb + 0.6, 0.3), 36, CYA, "black")
    for j, (key, t0) in enumerate((("d_yz", tb + 1.0), ("d_xz", tc + 0.6), ("d_xy", td + 0.8))):
        label(c, L[key], RX, 380 + j * 100, a * ep(t, t0, 0.3), 46, WHITE, "black")
    eq(c, [(L["regra"], AMB)], 760, a * ep(t, te, 0.3), 40, box=AMB)


def b_projecao(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_proj"], a)
    cena3d(c, a)
    ks = {"yz": ep(t, tc, 0.4), "xz": ep(t, tc + 2.6, 0.4), "xy": ep(t, td, 0.4)}
    sombras(c, INI, a, CYA, ks=ks)
    if t >= tb and t < tc:   # a luz perpendicular chegando na parede do fundo
        k = ep(t, tb, 0.3)
        for j in range(4):
            yy, zz = INI[1] + 0.2 + j * 0.2, INI[2] + 0.5
            seta3d(c, (INI[0] + 2.4, yy, zz), (INI[0] + 1.2, yy, zz), a * k * 0.8, AMB, w=3)
    cubo(c, INI, a, AMB)
    board(c, a)
    label(c, L["sombra"], RX, 280, a * ep(t, tb, 0.3), 40, AMB, "black")
    for j, (key, t0) in enumerate((("g_yz", tc), ("g_xz", tc + 2.6), ("g_xy", td))):
        label(c, L[key], RX, 420 + j * 100, a * ep(t, t0, 0.3), 46, CYA, "black")


def b_inicial(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ini"], a)
    cena3d(c, a, numeros=ep(t, ta + 0.6, 0.4))
    sombras(c, INI, a * 0.9, CYA)
    cubo(c, INI, a, AMB)
    faixa_eixo(c, "x", 5, 6, a * ep(t, tb, 0.3), AMB)
    faixa_eixo(c, "y", 1, 2, a * ep(t, tc, 0.3), AMB)
    faixa_eixo(c, "z", 6, 7, a * ep(t, td, 0.3), AMB)
    board(c, a)
    for j, (key, t0) in enumerate((("ini_x", tb), ("ini_y", tc), ("ini_z", td))):
        eq(c, [(L[key], AMB)], 330 + j * 130, a * ep(t, t0, 0.3), 60)


def b_movimentos(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_mov"], a)
    cena3d(c, a, numeros=1.0)
    pos = pos_mov(t, tb, tc, td)
    cubo(c, INI, a * 0.25, AMB, contorno=INK2)            # onde ele estava
    sombras(c, pos, a * 0.85, CYA, linhas=0.6)
    cubo(c, pos, a, AMB if t < td + 3.2 else MNT, glow=0.6)
    faixa_eixo(c, "x", pos[0], pos[0] + 1, a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.3)), CYA)
    faixa_eixo(c, "y", pos[1], pos[1] + 1, a * ep(t, tc, 0.3) * (1 - ep(t, td, 0.3)), CYA)
    faixa_eixo(c, "z", pos[2], pos[2] + 1, a * ep(t, td, 0.3), CYA)
    board(c, a)
    for j, (key, op, t0) in enumerate((("mv_x", "−3", tb), ("mv_y", "+5", tc), ("mv_z", "−4", td))):
        k = a * ep(t, t0, 0.3)
        y = 320 + j * 150
        eq(c, [(L[key], WHITE)], y, k, 54)
        popill(c, op, BX1 - 90, y - 50, 30, CYA if op[0] == "+" else AMB, BG0, k, t, t0 + 0.8)


def b_final(c, t, C, B):
    ta, tb, tc, td, te = (C[f"07.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_fim"], a)
    cena3d(c, a, numeros=1.0)
    ks = {"yz": ep(t, tb, 0.4), "xz": ep(t, tc, 0.4), "xy": ep(t, td, 0.4)}
    sombras(c, FIM, a, MNT, ks=ks)
    cubo(c, FIM, a, MNT)
    board(c, a)
    k1 = a * (1 - ep(t, te, 0.3))
    for j, (key, t0) in enumerate((("f_yz", tb), ("f_xz", tc), ("f_xy", td))):
        eq(c, [(L[key], MNT)], 320 + j * 120, k1 * ep(t, t0, 0.3), 50)
    ke = a * ep(t, te, 0.3)
    if ke > 0:
        _card_img(c, _img("opcao_E.png"), ke, w=560, cx=RX, cy=470)
        eq(c, [(L["alt"] + " ", WHITE), ("E", MNT)], 790, ke, 60, box=MNT)


# sombras na parede yz de cada alternativa (medidas nas figuras da prova): (y, z) do canto
YZ_ALT = dict(A=(6, 3), B=(4, 2), C=(5, 2), D=(5, 2), E=(6, 2))


def b_pegadinhas(c, t, C, B):
    tb, tc, td, te = (C[f"08.{k}"] for k in "bcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    cena3d(c, a, numeros=1.0, tints={"yz": (CYA, ep(t, B["start"] + 0.6, 0.4), None)})
    atual = max([j for j, t0 in enumerate((tb, tc, td, te)) if t >= t0], default=-1)
    letras = (["A"], ["B"], ["C", "D"], ["E"])
    if atual >= 0:
        y, z = YZ_ALT[letras[atual][0]]
        cor = MNT if atual == 3 else RED
        k = a * ep(t, (tb, tc, td, te)[atual], 0.3)
        pth = _poly([P(0, y, z), P(0, y + 1, z), P(0, y + 1, z + 1), P(0, y, z + 1)])
        c.drawPath(pth, blur_paint(cor, 0.4 * k, 10))
        c.drawPath(pth, paint(cor, k))
        if atual < 3:   # onde deveria estar
            ok = _poly([P(0, 6, 2), P(0, 7, 2), P(0, 7, 3), P(0, 6, 3)])
            c.drawPath(ok, _tracejado(MNT, k, 4, 10, 6))
    board(c, a)
    label(c, L["so_fundo"], RX, 230, a * ep(t, B["start"] + 0.6, 0.3), 32, CYA, "black")
    if atual >= 0:
        k = a * ep(t, (tb, tc, td, te)[atual], 0.3)
        nomes = letras[atual]
        if len(nomes) == 1:
            _card_img(c, _img(f"opcao_{nomes[0]}.png"), k, w=440, cx=RX, cy=460)
        else:
            for j, nm in enumerate(nomes):
                _card_img(c, _img(f"opcao_{nm}.png"), k, w=380, cx=RX - 210 + 420 * j, cy=460)
        label(c, L["pegs"][atual], RX, 720, k, 44, MNT if atual == 3 else RED, "black")
    for j in range(4):   # placar das letras
        kj = a * ep(t, (tb, tc, td, te)[j], 0.3)
        for nm in letras[j]:
            x = BX0 + 160 + "ABCDE".index(nm) * 145
            text_mid(c, nm, x, 830, 44, "black", MNT if nm == "E" else RED, kj)
            if nm != "E":
                cross(c, x + 34, 800, 16, kj)


def b_desafio(c, t, C, B):
    ta, tb, tc = (C[f"09.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    cena3d(c, a, numeros=1.0)
    sombras(c, FIM, a, MNT, quais="yz")
    cubo(c, FIM, a, MNT)
    kb = a * ep(t, tb, 0.3)
    x, y, z = FIM
    seta3d(c, (x + 0.5, y + 0.5, z + 1.1), (x + 0.5, y + 0.5, z + 3.1), kb, AMB, "+2")
    kq = a * ep(t, tc, 0.3)
    if kq > 0:
        qx, qy = P(0, 6.5, 5.5)
        text_mid(c, "?", qx, qy, 110, "black", AMB, kq)
    board(c, a)
    label(c, L["des1"], RX, 320, kb, 46, AMB, "black")
    label(c, L["des2"], RX, 470, kq, 46, WHITE, "black")
    label(c, L["comenta"], RX, 640, a * ep(t, tc + 2.6, 0.3), 40, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"10.{k}"] for k in "bcd"]
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
    """miniatura de cada aula: eixos x, y, z · um cubo e a sua sombra · as vistas de um sólido"""
    if i == 0:
        o = (cx - 20, cy + 50)
        for (dx, dy), nm in (((-70, 40), "x"), ((110, 0), "y"), ((0, -110), "z")):
            c.drawLine(*o, o[0] + dx, o[1] + dy, paint(WHITE, a, stroke=5, cap_round=True))
            text_mid(c, nm, o[0] + dx * 1.2, o[1] + dy * 1.2, 34, "black", CYA, a)
    elif i == 1:
        rrect(c, cx - 30, cy - 70, 60, 60, 6, AMB, a)
        for j in range(3):
            c.drawLine(cx - 20 + j * 20, cy - 10, cx - 20 + j * 20, cy + 50, _tracejado(WHITE, a * 0.6, 2, 4, 4))
        c.drawPath(_poly([(cx - 30, cy + 50), (cx + 30, cy + 50), (cx + 10, cy + 70), (cx - 50, cy + 70)]), paint(CYA, a))
    else:
        for j, (w_, h_) in enumerate(((60, 60), (90, 60), (60, 90))):
            rrect(c, cx - 140 + j * 100, cy - h_ / 2, w_, h_, 6, MNT, a * (0.6 + 0.2 * j))


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"11.{k}"] for k in "abcdef")
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
        sz = min(50, *(50 * (w - 50) / max(1, text_w(s_, "black", 50)) for s_ in (l1, l2)))
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
            bolinha(c, 960 - 280 + j * 140, 790, v, kl, MNT if v == "E" else INK2, glow=1.0 if v == "E" else 0, k=0.9)


BLOCKS = dict(gancho=b_gancho, planos=b_planos, distancia=b_distancia, projecao=b_projecao, inicial=b_inicial,
              movimentos=b_movimentos, final=b_final, pegadinhas=b_pegadinhas, desafio=b_desafio, resumo=b_resumo,
              aulas=b_aulas)
