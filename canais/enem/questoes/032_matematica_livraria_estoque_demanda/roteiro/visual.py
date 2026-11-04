"""Visual — Estudativo · Questão de Matemática 032 (aula horizontal 1920x1080): ENEM 2025, questão 148, estoque e demanda
na livraria (leitura de gráfico de barras e linha). Design system de matemática: _ferramentas/matematica.py.
Cores: âmbar = autor brasileiro (a barra laranja do enunciado), menta = autor estrangeiro (a barra verde), ciano = a
demanda (a linha azul) e o estoque total; os vereditos usam check (menta) e cross (coral).
Figura: o gráfico do enunciado redesenhado à esquerda (grafico()), com as duas barras de cada gênero que se empilham no
estoque total (empilha) e a marca da demanda ao lado para comparar. Valores lidos na figura da prova (escala de 10 em 10)."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_032_matematica_livraria_estoque_demanda.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.b": "data", "01.c": "data", "01.e": "shimmer", "02.b": "data", "02.c": "data", "02.d": "lock",
        "03.b": "data", "03.c": "confirm", "03.d": "deny", "04.b": "data", "04.c": "confirm", "05.b": "data",
        "05.c": "data", "05.d": "alert", "06.b": "data", "06.c": "confirm", "07.b": "data", "07.c": "confirm",
        "08.b": "confirm", "08.c": "impact", "09.b": "deny", "09.c": "deny", "09.d": "deny", "10.b": "alert",
        "11.a": "shimmer", "12.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 032", "QUESTÃO DE MATEMÁTICA · 032"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_leit=("TOOL 1 · READING THE CHART", "FERRAMENTA 1 · LER O GRÁFICO"),
    s_comp=("TOOL 2 · COMPARING", "FERRAMENTA 2 · COMPARAR"), s_resp=("THE ANSWER", "A RESPOSTA"),
    s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"), s_des=("CHALLENGE", "DESAFIO"),
    s_resumo=("SUMMARY", "RESUMO"),
    passo=("STEP {} · {}", "PASSO {} · {}"),
    generos=(["sci-fi", "self-help", "romance", "biography"], ["ficção", "autoajuda", "romance", "biografia"]),
    generos_cab=(["SCI-FI", "SELF-HELP", "ROMANCE", "BIOGRAPHY"], ["FICÇÃO CIENTÍFICA", "AUTOAJUDA", "ROMANCE", "BIOGRAFIA"]),
    enem=("ENEM 2025 · question 148", "ENEM 2025 · questão 148"), livraria=("a bookstore, 4 genres", "livraria: 4 gêneros"),
    barras=("bars = stock", "barras = estoque"), linha=("line = demand", "linha = demanda"),
    regra=("order only if stock < demand", "encomenda só se estoque < demanda"), pede=("which genre?", "qual gênero?"),
    t_leit=("reading the chart", "leitura de gráfico"), t_comp=("comparing", "comparação"),
    bras=("orange = Brazilian author", "laranja = autor brasileiro"), estr=("green = foreign author", "verde = autor estrangeiro"),
    dem=("blue line = demand", "linha azul = demanda"), escala=("scale: steps of 10", "escala: de 10 em 10"),
    soma=("stock = Brazilian + foreign", "estoque = brasileiro + estrangeiro"),
    ok=("stock ≥ demand → enough ✓", "estoque ≥ demanda → dá conta ✓"),
    falta=("stock < demand → ORDER!", "estoque < demanda → ENCOMENDA!"),
    l_est=("stock", "estoque"), l_dem=("demand", "demanda"),
    v_bras=("Brazilian", "brasileiro"), v_estr=("+ foreign", "+ estrangeiro"), v_tot=("in stock", "em estoque"),
    v_dem=("demand", "demanda"), sobram=("{} to spare ✓", "sobram {} ✓"), faltam=("{} short ✗", "faltam {} ✗"),
    enc=("ORDER!", "ENCOMENDAR!"), da=("ENOUGH", "DÁ CONTA"),
    acima=("the dot is above 130", "o ponto fica acima de 130"),
    r1=("sci-fi, romance, biography ✓", "ficção, romance, biografia ✓"), r2=("self-help: 130 < 135", "autoajuda: 130 < 135"),
    alt=("ANSWER", "ALTERNATIVA"),
    pA=("sci-fi: 200 ≥ 160, there's extra", "ficção: 200 ≥ 160, sobra"), pB=("biography: least demand, but 95 ≥ 80", "biografia: menor demanda, mas 95 ≥ 80"),
    pC=("self-help: 130 < 135 ✓", "autoajuda: 130 < 135 ✓"), pD=("biography: least stock, but 95 ≥ 80", "biografia: menor estoque, mas 95 ≥ 80"),
    pE=("romance: forgot the foreign 105", "romance: esqueceu os 105 estrangeiros"),
    des1=("what if biography demand", "e se a demanda de biografia"), des2=("DOUBLED?", "DOBRASSE?"),
    des3=("order? at least how many?", "encomenda? no mínimo quantos?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["read each bar on the scale", "add the bars of the same genre", "stock < demand → order"],
            ["leia cada barra na escala", "some as barras do mesmo gênero", "estoque < demanda → encomenda"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Bar", "charts"), ("Line", "charts"), ("Charts and", "tables")],
           [("Gráfico", "de barras"), ("Gráfico", "de linhas"), ("Gráficos", "e tabelas")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [("dois mil e vinte e cinco", "2025")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

BRAS = (80, 50, 40, 45)     # autor brasileiro (lido no gráfico)
ESTR = (120, 80, 105, 50)   # autor estrangeiro
DEM = (160, 135, 140, 80)   # demanda (a linha)
TOT = tuple(b + e for b, e in zip(BRAS, ESTR))   # 200, 130, 145, 95


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


GX0, GX1, GY0, KY = 150, 900, 860, 2.9   # eixo x de GX0 a GX1, zero em GY0, px por livro
GC = (265, 440, 615, 790)                 # centro de cada gênero
BW = 58


def yv(v):
    return GY0 - v * KY


def grafico(c, a, t, foco=None, emp=None, kb=1.0, ke=1.0, kd=1.0, marca=None, dims=None, escala=0.0, demk=None,
            rotulos=True):
    """o gráfico da questão: emp[i] = 0..1 (as duas barras se empilham no estoque total); foco = gênero em destaque;
    marca[i] = True/False (check ou cross acima); demk[i] = demanda alternativa (desafio); escala = destaque da grade"""
    if a <= 0:
        return
    for v in range(0, 201, 10):   # grade de 10 em 10
        y = yv(v)
        c.drawLine(GX0, y, GX1, y, paint(CYA if escala > 0 and v % 10 == 0 else INK2, (0.1 + 0.15 * escala) * a, stroke=1))
        if v % 20 == 0:
            text_mid(c, str(v), GX0 - 34, y, 22, "extrabold", INK2, a)
    c.drawLine(GX0, GY0, GX1, GY0, paint(WHITE, 0.8 * a, stroke=3))
    pts = []
    for i, cx in enumerate(GC):
        al = a * (1 - 0.7 * ((dims or {}).get(i, 0.0) if dims else (0.0 if foco is None or foco == i else 1.0)))
        u = ep((emp or {}).get(i, 0.0), 0, 1)
        xb, xe = cx - 32 * (1 - u), cx + 32 * (1 - u)
        hb, he = BRAS[i] * KY * kb, ESTR[i] * KY * ke
        ye0 = GY0 - hb * u   # a barra estrangeira sobe para cima da brasileira
        w = BW + 12 * u
        if hb > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(xb - w / 2, GY0 - hb, xb + w / 2, GY0), 6, 6), paint(AMB, 0.9 * al))
        if he > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(xe - w / 2, ye0 - he, xe + w / 2, ye0), 6, 6), paint(MNT, 0.9 * al))
        if u > 0.98:
            text_mid(c, str(TOT[i]), cx, yv(TOT[i]) + 26, 30, "black", BG0, al)
        if rotulos:
            text_mid(c, L["generos"][i], cx, GY0 + 36, 28, "extrabold", WHITE if foco in (None, i) else INK2, al)
        d = (demk or {}).get(i, DEM[i])
        pts.append((cx, yv(d), al))
        if marca and i in marca:
            k = al * ep(marca[i][1], 0, 1)
            (check if marca[i][0] else cross)(c, cx + 62, yv(max(TOT[i], d)) - 70, 22, k)
    if kd > 0:   # a linha de demanda com os quadradinhos
        n = len(pts)
        for j in range(n - 1):
            (x0, y0, a0), (x1, y1, a1) = pts[j], pts[j + 1]
            u = clamp(kd * (n - 1) - j)
            if u > 0:
                c.drawLine(x0, y0, x0 + (x1 - x0) * u, y0 + (y1 - y0) * u, paint(CYA, 0.85 * a * min(a0, a1) / max(a, 1e-6), stroke=4))
        for j, (x, y, al) in enumerate(pts):
            if kd * (n - 1) >= j - 0.01:
                c.drawRect(skia.Rect.MakeXYWH(x - 9, y - 9, 18, 18), paint(CYA, al))


def comparar(c, i, a, k=1.0, cor=CYA):
    """traço da demanda atravessando a pilha do gênero i, para ver se o estoque passa ou não"""
    if a <= 0 or k <= 0:
        return
    cx, y = GC[i], yv(DEM[i])
    c.drawLine(cx - 70, y, cx - 70 + 140 * k, y, _dash(cor, a, 4, 8))


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao.png"), a, cx=300, cy=530, hmax=790)
    ke = ep(t, te, 0.4)
    for i, dt in enumerate((5.7, 6.9, 7.7, 8.4)):   # os quatro gêneros
        popill(c, L["generos"][i], 735, 300 + i * 120, 34, (AMB, MNT, CYA, WHITE)[i], BG0, a * (1 - ke), t, ta + dt)
    popill(c, L["t_leit"], 735, 420, 32, CYA, BG0, a * ke, t, te + 1.3)
    popill(c, L["t_comp"], 735, 580, 34, AMB, BG0, a * ke, t, te + 2.6)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 36, INK2, "extrabold")
    label(c, L["livraria"], RX, 310, a, 46, WHITE, "black")
    eq(c, [(L["barras"], AMB)], 430, a * ep(t, tb + 0.8, 0.3), 48)
    eq(c, [(L["linha"], CYA)], 540, a * ep(t, tb + 2.2, 0.3), 48)
    eq(c, [(L["regra"], WHITE)], 660, a * ep(t, tc + 2.3, 0.3), 42)
    eq(c, [(L["pede"], CYA)], 800, a * ep(t, td, 0.3), 54, box=CYA)


def b_leitura(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_leit"], a)
    grafico(c, a, t, kb=ep(t, tb + 2.1, 0.8), ke=ep(t, tb + 4.1, 0.8), kd=ep(t, tc + 0.2, 1.0), escala=ep(t, td, 0.4))
    kg = a * ep(t, td + 1.9, 0.4)   # do topo da barra até o eixo
    if kg > 0:
        x0 = GC[0] - 32
        c.drawLine(x0 - BW / 2, yv(80), x0 - BW / 2 - (x0 - BW / 2 - GX0) * ep(t, td + 1.9, 0.8), yv(80), _dash(AMB, kg, 4, 8))
        popill(c, "80", GX0 - 34, yv(80), 26, AMB, BG0, kg, t, td + 2.6)
    board(c, a)
    eq(c, [(L["bras"], AMB)], 300, a * ep(t, tb + 2.1, 0.3), 44)
    eq(c, [(L["estr"], MNT)], 420, a * ep(t, tb + 4.1, 0.3), 44)
    eq(c, [(L["dem"], CYA)], 540, a * ep(t, tc + 0.2, 0.3), 44)
    eq(c, [(L["escala"], WHITE)], 720, a * ep(t, td + 0.6, 0.3), 50, box=CYA)


def _exemplo(c, cx, est, dem, a, t, t0, ok):
    """barra de estoque × traço da demanda (exemplo genérico)"""
    k = a * ep(t, t0, 0.3)
    if k <= 0:
        return
    h = est * ep(t, t0, 0.6)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(cx - 50, 820 - h, cx + 50, 820), 8, 8), paint(CYA, 0.8 * k))
    c.drawLine(cx - 100, 820 - dem, cx + 100, 820 - dem, _dash(WHITE, k, 4, 8))
    label(c, L["l_dem"], cx + 100, 820 - dem - 28, k, 26, WHITE, "extrabold", align="right")
    label(c, L["l_est"], cx, 860, k, 30, CYA, "black")
    (check if ok else cross)(c, cx, 820 - max(est, dem) - 70, 30, k * ep(t, t0 + 0.6, 0.3))


def b_comparar(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_comp"], a)
    kb = a * ep(t, tb + 1.3, 0.3)   # duas barras viram uma pilha
    if kb > 0:
        u = ep(t, tb + 1.8, 0.8)
        x = 520
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x - 40 - 50 * (1 - u), 400 - 160, x + 40 - 50 * (1 - u), 400), 6, 6), paint(AMB, 0.9 * kb * (1 - ep(t, tc, 0.3))))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x - 40 + 50 * (1 - u), 400 - 120 - 160 * u, x + 40 + 50 * (1 - u), 400 - 160 * u), 6, 6), paint(MNT, 0.9 * kb * (1 - ep(t, tc, 0.3))))
    _exemplo(c, 330, 420, 300, a, t, tc + 0.5, True)
    _exemplo(c, 710, 220, 340, a, t, td + 0.3, False)
    board(c, a)
    eq(c, [(L["soma"], WHITE)], 300, a * ep(t, tb + 1.3, 0.3), 42, box=CYA)
    eq(c, [(L["ok"], MNT)], 480, a * ep(t, tc + 0.5, 0.3), 42)
    eq(c, [(L["falta"], RED)], 620, a * ep(t, td + 0.3, 0.3), 42)


# tempos de cada passo (a partir de b e de c): brasileiro, estrangeiro, total, demanda, veredito
PASSOS = {0: ("04", (0.0, 1.3, 2.9), (0.6, 2.5)), 1: ("05", (0.0, 0.7, 1.5), (3.6, None)),
          2: ("06", (0.0, 0.8, 1.8), (0.9, 2.9)), 3: ("07", (0.0, 0.8, 1.5), (0.5, 1.2))}


def _emp_ate(i, t, C):
    """estado da pilha e das marcas dos gêneros já resolvidos (antes do passo i) e do próprio i"""
    emp, marca = {}, {}
    for j in range(4):
        sid, (_, _, dtot), (_, dver) = PASSOS[j]
        tb = C[f"{sid}.b"]
        emp[j] = ep(t, tb + dtot - 0.3, 0.6)
        tv = C[f"{sid}.d"] + 1.9 if j == 1 else C[f"{sid}.c"] + dver
        marca[j] = (TOT[j] >= DEM[j], ep(t, tv, 0.3))
    return emp, marca


def b_genero(i):
    sid, (dbr, des, dtot), (ddem, dver) = PASSOS[i]

    def b(c, t, C, B):
        tb, tc = C[f"{sid}.b"], C[f"{sid}.c"]
        a = fade(t, B["start"], B["end"])
        header(c, L["passo"].format(i + 1, L["generos_cab"][i]), a)
        emp, marca = _emp_ate(i, t, C)
        grafico(c, a, t, emp=emp, marca=marca, dims={j: (0.0 if j == i else 0.6) for j in range(4)})
        comparar(c, i, a * ep(t, tc + ddem, 0.3), ep(t, tc + ddem, 0.6))
        board(c, a)
        eq(c, [(f"{BRAS[i]} ", AMB), (L["v_bras"], WHITE)], 270, a * ep(t, tb + dbr, 0.3), 48)
        eq(c, [(f"+ {ESTR[i]} ", MNT), (L["v_estr"][2:], WHITE)], 370, a * ep(t, tb + des, 0.3), 48)
        eq(c, [(f"= {TOT[i]} ", CYA), (L["v_tot"], WHITE)], 490, a * ep(t, tb + dtot, 0.3), 56, box=CYA)
        if i == 1:
            td = C[f"{sid}.d"]
            eq(c, [(L["acima"], INK2)], 610, a * ep(t, tc + 1.8, 0.3) * (1 - ep(t, tc + 3.6, 0.2)), 38)
            eq(c, [(L["v_dem"] + ": ", WHITE), ("≈ 135", CYA)], 610, a * ep(t, tc + 3.6, 0.3), 50)
            eq(c, [("130 < 135", RED)], 720, a * ep(t, td + 0.6, 0.3), 54)
            eq(c, [(L["enc"], RED)], 820, a * ep(t, td + 1.9, 0.3), 56, box=RED)
        else:
            eq(c, [(L["v_dem"] + ": ", WHITE), (str(DEM[i]), CYA)], 610, a * ep(t, tc + ddem, 0.3), 50)
            eq(c, [(L["sobram"].format(TOT[i] - DEM[i]), MNT)], 720, a * ep(t, tc + ddem + 0.6, 0.3), 50)
            eq(c, [(L["da"], MNT)], 820, a * ep(t, tc + dver, 0.3), 56, box=MNT)
    return b


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"08.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    emp, marca = _emp_ate(4, t, C)
    kb = ep(t, tb + 3.5, 0.4)
    grafico(c, a, t, emp=emp, marca=marca, dims={j: (0.0 if j == 1 else 0.6 * kb) for j in range(4)})
    comparar(c, 1, a * kb, 1.0, RED)
    board(c, a)
    eq(c, [(L["r1"], MNT)], 280, a * ep(t, ta + 1.2, 0.3), 44)
    eq(c, [(L["r2"], RED)], 400, a * ep(t, tb + 3.5, 0.3), 48)
    kc = a * ep(t, tc, 0.3)
    if kc > 0:
        for j, le in enumerate("ABCDE"):
            x = BX0 + 130 + j * 160
            ok = le == "C"
            c.drawCircle(x, 580, 34, paint(MNT if ok else INK2, kc))
            text_mid(c, le, x, 580, 36, "black", BG0, kc)
        check(c, BX0 + 130 + 2 * 160 + 38, 550, 18, kc)
        eq(c, [(L["alt"] + " ", WHITE), ("C", MNT)], 770, kc, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td = (C[f"09.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    emp, marca = _emp_ate(4, t, C)
    foco = 2 if t >= td else 3 if t >= tc else 0 if t >= tb else 1
    if t >= td:   # a E: só os brasileiros do romance (a pilha do romance volta a separar)
        emp[2] = 1 - ep(t, td + 0.4, 0.6)
    grafico(c, a, t, emp=emp, marca=marca, dims={j: (0.0 if j == foco else 0.65) for j in range(4)})
    if t >= td:
        cross(c, GC[2] - 32, yv(BRAS[2]) - 40, 22, a * ep(t, td + 1.6, 0.3))
    board(c, a)
    linhas = (("A", L["pA"], RED, tb + 0.4), ("B", L["pB"], RED, tc + 0.4), ("C", L["pC"], MNT, ta),
              ("D", L["pD"], RED, tc + 1.0), ("E", L["pE"], RED, td + 0.4))
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
    ta, tb, tc = (C[f"10.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    u = ep(t, tb + 1.4, 1.0)
    grafico(c, a, t, emp={j: 1.0 for j in range(4)}, dims={j: (0.0 if j == 3 else 0.65) for j in range(4)},
            demk={3: 80 + 80 * u})
    label(c, "?", GC[3] + 70, yv(130), a * ep(t, tb + 4.0, 0.3) * (0.6 + 0.4 * math.sin(t * 5) ** 2), 80, AMB, "black")
    board(c, a)
    label(c, L["des1"], RX, 320, a * ep(t, tb, 0.3), 44, WHITE, "black")
    eq(c, [(L["des2"], AMB)], 440, a * ep(t, tb + 1.4, 0.3), 64, box=AMB)
    label(c, L["des3"], RX, 600, a * ep(t, tb + 3.2, 0.3), 46, CYA, "black")
    label(c, L["comenta"], RX, 740, a * ep(t, tc, 0.3), 40, AMB, "extrabold")


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
    """miniatura de cada aula: barras · linha · tabela"""
    if i == 0:
        for j, h in enumerate((70, 120, 90, 150)):
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(cx - 130 + j * 70, cy + 70 - h, cx - 80 + j * 70, cy + 70), 6, 6), paint(CYA, a))
    elif i == 1:
        p = skia.Path()
        for j, v in enumerate((40, 110, 70, 140)):
            (p.moveTo if j == 0 else p.lineTo)(cx - 130 + j * 87, cy + 70 - v)
        c.drawPath(p, paint(AMB, a, stroke=6))
        for j, v in enumerate((40, 110, 70, 140)):
            c.drawRect(skia.Rect.MakeXYWH(cx - 139 + j * 87, cy + 61 - v, 18, 18), paint(AMB, a))
    else:
        for r in range(3):
            for col in range(3):
                c.drawRect(skia.Rect.MakeXYWH(cx - 120 + col * 80, cy - 60 + r * 46, 76, 42), paint(MNT, a * (0.9 if r == 0 else 0.35)))


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
            c.drawCircle(x, 790, 38, paint(MNT if v == "C" else INK2, kl, stroke=4))
            text_mid(c, v, x, 790, 38, "black", WHITE, kl)


BLOCKS = dict(gancho=b_gancho, leitura=b_leitura, comparar=b_comparar, ficcao=b_genero(0), autoajuda=b_genero(1),
              romance=b_genero(2), biografia=b_genero(3), resposta=b_resposta, pegadinhas=b_pegadinhas,
              desafio=b_desafio, resumo=b_resumo, aulas=b_aulas)
