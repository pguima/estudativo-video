"""Visual — Estudativo · Questão de Matemática 038 (aula horizontal 1920x1080): ENEM 2025, questão 151, a cúpula pentagonal
giralongada (contagem de faces e arestas e relação de Euler). Design system de matemática: _ferramentas/matematica.py.
Figuras: o sólido em 3D girando (poliedro.py, geometria exata com aresta 1), o cubo dos exemplos e o icosaedro do
desafio. Cores das faces como na prova: triângulos azuis, quadrados âmbar, pentágono menta, decágono coral; vértices em
branco; arestas em ciano quando são o assunto. Menta = a resposta (25)."""
import sys
from pathlib import Path

import idioma
import matematica
from matematica import *  # noqa

sys.path.insert(0, str(Path(__file__).resolve().parent))
import poliedro as PL  # noqa: E402

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_038_matematica_poliedro_vertices.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.b": "data", "01.c": "data", "01.d": "alert", "01.e": "shimmer", "02.b": "data", "02.c": "data",
        "02.d": "data", "02.e": "confirm", "03.b": "lock", "03.c": "confirm", "03.d": "data", "04.b": "data",
        "04.c": "data", "04.d": "data", "04.e": "data", "04.f": "confirm", "05.c": "data", "05.d": "confirm",
        "05.e": "lock", "05.f": "confirm", "06.b": "data", "06.c": "data", "06.d": "impact", "07.b": "pop",
        "07.c": "pop", "07.d": "pop", "07.e": "confirm", "08.b": "impact", "09.b": "deny", "09.c": "deny",
        "09.d": "deny", "10.b": "alert", "11.a": "shimmer", "12.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 038", "QUESTÃO DE MATEMÁTICA · 038"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_pecas=("TOOL 1 · THE PARTS OF A POLYHEDRON", "FERRAMENTA 1 · AS PEÇAS DE UM POLIEDRO"),
    s_euler=("TOOL 2 · EULER'S FORMULA", "FERRAMENTA 2 · A RELAÇÃO DE EULER"),
    s_faces=("STEP 1 · THE FACES", "PASSO 1 · AS FACES"), s_ar=("STEP 2 · THE EDGES", "PASSO 2 · AS ARESTAS"),
    s_conta=("STEP 3 · EULER", "PASSO 3 · EULER"), s_conf=("CHECKING ON THE SOLID", "CONFERINDO NO SÓLIDO"),
    s_resp=("THE ANSWER", "A RESPOSTA"), s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"),
    s_des=("CHALLENGE", "DESAFIO"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 151", "ENEM 2025 · questão 151"),
    nome1=("the gyroelongated", "a cúpula pentagonal"), nome2=("pentagonal cupola", "giralongada"),
    g1=("all faces are regular polygons", "todas as faces são regulares"),
    g2=("the solid + a net", "o sólido + uma planificação"),
    pede=("how many vertices?", "quantos vértices?"),
    t_cont=("faces and edges", "faces e arestas"), t_euler=("Euler's formula", "relação de Euler"),
    p1=("faces = the polygons", "faces = os polígonos"), p2=("edges = where 2 faces meet", "arestas = onde 2 faces se encontram"),
    p3=("vertices = the corners", "vértices = os cantos"), cubo=("cube:", "cubo:"),
    eu1=("V − E + F = 2", "V − A + F = 2"), eu2=("8 − 12 + 6 = 2", "8 − 12 + 6 = 2"),
    eu3=("know F and E → find V", "sabendo F e A → acha V"),
    f_dec=("1 decagon", "1 decágono"), f_pen=("1 pentagon", "1 pentágono"), f_sq=("5 squares", "5 quadrados"),
    f_tri=("25 triangles", "25 triângulos"), f_tot=("1 + 1 + 5 + 25 = 32 faces", "1 + 1 + 5 + 25 = 32 faces"),
    a_tri=("25 × 3 = 75", "25 × 3 = 75"), a_sq=("5 × 4 = 20", "5 × 4 = 20"), a_pd=("+ 5 + 10", "+ 5 + 10"),
    a_tot=("110 sides", "110 lados"), a_par=("each edge joins 2 sides", "cada aresta junta 2 lados"),
    a_res=("110 ÷ 2 = 55 edges", "110 ÷ 2 = 55 arestas"),
    c1=("V − E + F = 2", "V − A + F = 2"), c2=("V − 55 + 32 = 2", "V − 55 + 32 = 2"), c3=("V − 23 = 2", "V − 23 = 2"),
    c4=("V = 2 + 23 = 25", "V = 2 + 23 = 25"),
    v_top=("top: 5", "em cima: 5"), v_mid=("middle: 10", "no meio: 10"), v_bot=("bottom: 10", "embaixo: 10"),
    v_tot=("5 + 10 + 10 = 25 ✓", "5 + 10 + 10 = 25 ✓"),
    r1=("V = 25 vertices", "V = 25 vértices"), alt=("ANSWER", "ALTERNATIVA"),
    pA=("21 → no correct count gives it", "21 → não sai de conta certa"), pB=("25 → the vertices ✓", "25 → os vértices ✓"),
    pC=("55 → the edges", "55 → as arestas"), pD=("80 → no correct count gives it", "80 → não sai de conta certa"),
    pE=("110 → all the sides added up", "110 → a soma dos lados"),
    des1=("a polyhedron with", "um poliedro com"), des2=("F = 20 · E = 30", "F = 20 · A = 30"),
    des3=("how many vertices?", "quantos vértices?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["count the faces of each type", "sides ÷ 2 = edges", "V − E + F = 2"],
            ["conte as faces de cada tipo", "lados ÷ 2 = arestas", "V − A + F = 2"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Polyhedra", ""), ("Euler's", "formula"), ("Nets of", "solids")],
           [("Poliedros", ""), ("Relação de", "Euler"), ("Planificação", "de sólidos")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025"), ("cento e cinquenta e um", "151"),
                        ("cento e dez", "110"), ("cinquenta e cinco", "55"), ("vinte e cinco", "25"),
                        ("trinta e duas", "32"), ("trinta e dois", "32"), ("vinte e três", "23"),
                        ("setenta e cinco", "75")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

TRI = "#3D7BE0"
COR = dict(tri_a=TRI, tri_c=TRI, sq=AMB, pent=MNT, dec=RED)
TRIS = {"tri_a", "tri_c"}
SOLIDO_CY = 560


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- peças
@lru_cache(None)
def _img(nome):
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / nome))


def _card_img(c, img, a, w=820, cx=LX, cy=545, hmax=830):
    h = img.height() * w / img.width()
    if h > hmax:
        h = hmax
        w = img.width() * h / img.height()
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x - 14, y - 14, w + 28, h + 28, 18, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


def giro(t, v=0.32, fase=0.4):
    return fase + v * t


def j24(c, t, a, cx=LX, cy=SOLIDO_CY, escala=178, tilt=0.42, **kw):
    """a cúpula pentagonal giralongada girando devagar"""
    return PL.desenha(c, PL.j24(), cx, cy, escala, giro(t), tilt, a, COR, **kw)


def lista(c, itens, t, a, y0=260, dy=110, size=50, cx=RX):
    """linhas do quadro que aparecem no seu tempo: (texto, cor, t0, caixa)"""
    for j, (s, cor, t0, box) in enumerate(itens):
        k = a * ep(t, t0, 0.3)
        if k > 0:
            eq(c, [(s, cor)], y0 + j * dy, k, size, box=cor if box else None)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    ki = a * (1 - ep(t, tb, 0.4))     # o enunciado primeiro; depois o sólido girando
    _card_img(c, _img("questao.png"), ki, w=820, cx=LX, cy=540, hmax=800)
    j24(c, t, a * ep(t, tb, 0.5), escala=150)
    popill(c, L["t_cont"], LX - 190, 900, 38, CYA, BG0, a * ep(t, te + 1.4, 0.3), t, te + 1.4)
    popill(c, L["t_euler"], LX + 190, 900, 38, AMB, BG0, a * ep(t, te + 2.6, 0.3), t, te + 2.6)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 36, INK2, "extrabold")
    label(c, L["nome1"], RX, 310, a, 46, WHITE, "black")
    label(c, L["nome2"], RX, 370, a, 46, WHITE, "black")
    eq(c, [(L["g1"], AMB)], 500, a * ep(t, tb + 0.6, 0.3), 44)
    eq(c, [(L["g2"], WHITE)], 600, a * ep(t, tc + 0.6, 0.3), 44)
    eq(c, [(L["pede"], MNT)], 760, a * ep(t, td + 0.6, 0.3), 56, box=MNT)


def cubo(c, t, a, k_faces=1.0, k_ar=0.0, k_v=0.0, cx=LX, cy=SOLIDO_CY):
    cor = dict(sq=CYA)
    PL.desenha(c, PL.cubo(), cx, cy, 175, giro(t, 0.4, 0.6), 0.5, a, cor, modo="vidro",
               k_tipo={"sq": k_faces}, k_ar=k_ar, cor_ar=AMB, vert={0: k_v})


def b_pecas(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_pecas"], a)
    kf = 0.35 + 0.65 * ep(t, tb, 0.4) * (1 - 0.6 * ep(t, tc, 0.3)) + 0.25 * ep(t, te, 0.3)
    cubo(c, t, a, k_faces=min(1, kf), k_ar=ep(t, tc, 0.4) * (1 - 0.5 * ep(t, td, 0.3)), k_v=ep(t, td, 0.3))
    board(c, a)
    lista(c, [(L["p1"], CYA, tb + 0.3, False), (L["p2"], AMB, tc + 0.3, False), (L["p3"], WHITE, td + 0.3, False)],
          t, a, y0=280, dy=120, size=44)
    ke = a * ep(t, te, 0.3)
    if ke > 0:
        label(c, L["cubo"], RX, 650, ke, 40, INK2, "extrabold")
        for j, (s, cor, d) in enumerate((("F = 6", CYA, 0.6), ("A = 12" if not EN else "E = 12", AMB, 1.6),
                                         ("V = 8", WHITE, 2.6))):
            k = a * ep(t, te + d, 0.3)
            if k > 0:
                pill(c, s, RX - 280 + j * 280, 760, 46, cor, BG0, k)


def b_euler(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_euler"], a)
    cubo(c, t, a, k_faces=1, k_ar=0.6, k_v=1)
    board(c, a)
    eq(c, [(L["eu1"], AMB)], 330, a * ep(t, tb + 0.4, 0.3), 76, box=AMB)
    eq(c, [(L["eu2"], WHITE)], 520, a * ep(t, tc + 0.4, 0.3), 64)
    check(c, RX + 260, 520, 24, a * ep(t, tc + 3.4, 0.2))
    eq(c, [(L["eu3"], CYA)], 720, a * ep(t, td + 0.8, 0.3), 46)


def b_faces(c, t, C, B):
    ta, tb, tc, td, te, tf = (C[f"04.{k}"] for k in "abcdef")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_faces"], a)
    foco = None
    for f, t0 in (({"dec"}, tb), ({"pent"}, tc), ({"sq"}, td), (TRIS, te), (None, tf)):
        if t >= t0:
            foco = f
    # de baixo para ver o decágono; de cima para o pentágono
    kb = ep(t, tb, 0.6) * (1 - ep(t, tc, 0.6))
    tilt = 0.42 - 1.0 * kb
    j24(c, t, a, tilt=tilt, modo="vidro", foco=foco)
    board(c, a)
    lista(c, [(L["f_dec"], RED, tb + 0.3, False), (L["f_pen"], MNT, tc + 0.3, False), (L["f_sq"], AMB, td + 0.2, False),
              (L["f_tri"], CYA, te + 0.2, False)], t, a, y0=250, dy=105, size=48)
    eq(c, [(L["f_tot"], WHITE)], 760, a * ep(t, tf + 4.0, 0.3), 46, box=WHITE)


def b_arestas(c, t, C, B):
    ta, tb, tc, td, te, tf = (C[f"05.{k}"] for k in "abcdef")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ar"], a)
    j24(c, t, a, modo="vidro", k_ar=ep(t, te, 0.4), cor_ar=CYA)
    board(c, a)
    k1 = 1 - 0.5 * ep(t, te, 0.3)
    lista(c, [(L["a_tri"], CYA, tc + 2.4, False), (L["a_sq"], AMB, tc + 5.3, False), (L["a_pd"], WHITE, tc + 7.6, False)],
          t, a * k1, y0=250, dy=95, size=46)
    eq(c, [(L["a_tot"], WHITE)], 545, a * ep(t, td + 1.1, 0.3), 52, box=WHITE)
    eq(c, [(L["a_par"], INK2)], 670, a * ep(t, te + 0.8, 0.3), 40)
    eq(c, [(L["a_res"], CYA)], 790, a * ep(t, tf + 2.5, 0.3), 54, box=CYA)


def b_conta(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conta"], a)
    j24(c, t, a)
    board(c, a)
    lista(c, [(L["c1"], AMB, ta + 0.6, False), (L["c2"], WHITE, tb + 0.4, False), (L["c3"], WHITE, tc + 2.0, False)],
          t, a, y0=270, dy=140, size=60)
    eq(c, [(L["c4"], MNT)], 760, a * ep(t, td + 2.5, 0.3), 66, box=MNT)


def _aneis(t, tb, tc, td):
    return {0: ep(t, tb + 1.3, 0.3), 1: ep(t, tc + 1.9, 0.3), 2: ep(t, td + 1.8, 0.3)}


def b_confere(c, t, C, B):
    ta, tb, tc, td, te = (C[f"07.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conf"], a)
    j24(c, t, a, modo="vidro", vert=_aneis(t, tb, tc, td), cor_vert=WHITE)
    board(c, a)
    lista(c, [(L["v_top"], MNT, tb + 1.3, False), (L["v_mid"], AMB, tc + 1.9, False), (L["v_bot"], RED, td + 1.8, False)],
          t, a, y0=270, dy=130, size=56)
    eq(c, [(L["v_tot"], MNT)], 740, a * ep(t, te + 1.6, 0.3), 60, box=MNT)


def b_resposta(c, t, C, B):
    ta, tb = C["08.a"], C["08.b"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    j24(c, t, a, modo="vidro", vert={0: 1, 1: 1, 2: 1}, cor_vert=MNT)
    popill(c, "25", LX, 850, 60, MNT, BG0, a * ep(t, ta + 2.0, 0.3), t, ta + 2.0)
    board(c, a)
    eq(c, [(L["r1"], MNT)], 300, a * ep(t, ta + 1.0, 0.3), 58)
    kc = a * ep(t, tb, 0.3)
    if kc > 0:
        for j, (le, v) in enumerate(zip("ABCDE", ("21", "25", "55", "80", "110"))):
            x = BX0 + 130 + j * 160
            ok = le == "B"
            c.drawCircle(x, 500, 34, paint(MNT if ok else INK2, kc))
            text_mid(c, le, x, 500, 36, "black", BG0, kc)
            text_mid(c, v, x, 575, 36, "black", MNT if ok else INK2, kc)
        check(c, BX0 + 130 + 160 + 38, 470, 18, kc)
        eq(c, [(L["alt"] + " ", WHITE), ("B", MNT)], 760, kc, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td = (C[f"09.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    j24(c, t, a, modo="vidro", k_ar=ep(t, tc, 0.4) * (1 - ep(t, td, 0.4)), cor_ar=RED,
        vert={0: 1, 1: 1, 2: 1} if t < tc or t >= td else None, cor_vert=WHITE)
    board(c, a)
    linhas = (("A", L["pA"], RED, td + 0.2), ("B", L["pB"], MNT, ta), ("C", L["pC"], RED, tc + 0.2),
              ("D", L["pD"], RED, td + 0.8), ("E", L["pE"], RED, tb + 0.2))
    for j, (le, s, cor, t0) in enumerate(linhas):
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        y = 270 + j * 140
        c.drawCircle(BX0 + 70, y, 32, paint(cor, k))
        text_mid(c, le, BX0 + 70, y, 34, "black", BG0, k)
        sz = 36
        while text_w(s, "black", sz) > 720:
            sz -= 2
        text_mid(c, s, BX0 + 125, y, sz, "black", WHITE, k, align="left")


def b_desafio(c, t, C, B):
    ta, tb, tc, td = (C[f"10.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    k = a * ep(t, tb, 0.4)
    PL.desenha(c, PL.icosaedro(), LX, 510, 150, giro(t, 0.35), 0.5, k, dict(tri_a=TRI))
    popill(c, "?", LX, 870, 60, AMB, BG0, a * ep(t, tc, 0.3), t, tc)
    board(c, a)
    label(c, L["des1"], RX, 300, a * ep(t, tb, 0.3), 46, WHITE, "black")
    eq(c, [(L["des2"], AMB)], 430, a * ep(t, tb + 1.2, 0.3), 60, box=AMB)
    label(c, L["des3"], RX, 600, a * ep(t, tc, 0.3), 50, CYA, "black")
    label(c, L["comenta"], RX, 740, a * ep(t, td, 0.3), 40, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"11.{k}"] for k in "bcd"]
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
    """miniatura de cada aula: o sólido · a fórmula · a planificação"""
    if i == 0:
        PL.desenha(c, PL.j24(), cx, cy, 52, giro(t, 0.5), 0.45, a, COR)
    elif i == 1:
        text_mid(c, L["eu1"], cx, cy, 52, "black", AMB, a)
    else:
        PL.desenha(c, PL.cubo(), cx, cy, 52, giro(t, 0.5, 0.6), 0.5, a, dict(sq=MNT))


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"12.{k}"] for k in "abcdef")
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
        _icone(c, i, cx, 430, kk, t)
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
            c.drawCircle(x, 790, 38, paint(MNT if v == "B" else INK2, kl, stroke=4))
            text_mid(c, v, x, 790, 38, "black", WHITE, kl)


BLOCKS = dict(gancho=b_gancho, pecas=b_pecas, euler=b_euler, faces=b_faces, arestas=b_arestas, conta=b_conta,
              confere=b_confere, resposta=b_resposta, pegadinhas=b_pegadinhas, desafio=b_desafio, resumo=b_resumo,
              aulas=b_aulas)
