"""Visual — Estudativo · Questão de Matemática 034 (aula horizontal 1920x1080): ENEM 2025, questão 149, matrículas na escola
de idiomas (gráfico de setores, gráfico de barras e porcentagem). Design system de matemática: _ferramentas/matematica.py.
Cores por idioma (as mesmas nos dois gráficos e na grade): ciano = inglês, âmbar = espanhol, menta = francês (o que a
questão pede), cinza-azulado = alemão; coral = as alternativas erradas.
Figuras: a pizza de 2023 (pizza()), as barras de 2024 (barras()) e a grade de 400 bolinhas, uma por matrícula (grade())."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_034_matematica_escola_idiomas_matriculas.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.b": "data", "01.c": "data", "01.e": "shimmer", "02.b": "data", "02.c": "data", "03.b": "data",
        "03.c": "lock", "04.b": "data", "04.c": "confirm", "05.b": "data", "05.c": "data", "05.d": "confirm",
        "06.b": "data", "06.c": "confirm", "07.b": "confirm", "07.c": "impact", "08.b": "deny", "08.c": "deny",
        "08.d": "deny", "08.e": "deny", "09.b": "alert", "10.a": "shimmer", "11.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 034", "QUESTÃO DE MATEMÁTICA · 034"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_graf=("TOOL 1 · THE TWO CHARTS", "FERRAMENTA 1 · OS DOIS GRÁFICOS"),
    s_pct=("TOOL 2 · PERCENT OF A TOTAL", "FERRAMENTA 2 · PORCENTAGEM DE UM TOTAL"),
    s_tot=("STEP 1 · THE 2024 TOTAL", "PASSO 1 · O TOTAL DE 2024"), s_fr=("STEP 2 · FRENCH", "PASSO 2 · O FRANCÊS"),
    s_conf=("CHECKING", "CONFERINDO"), s_resp=("THE ANSWER", "A RESPOSTA"),
    s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"), s_des=("CHALLENGE", "DESAFIO"),
    s_resumo=("SUMMARY", "RESUMO"),
    idiomas=(["English", "Spanish", "French", "German"], ["inglês", "espanhol", "francês", "alemão"]),
    enem=("ENEM 2025 · question 149", "ENEM 2025 · questão 149"), escola=("a language school", "escola de idiomas"),
    g1=("2025 total = 2024 total", "total de 2025 = total de 2024"), g2=("2025 % = 2023 %", "% de 2025 = % de 2023"),
    pede=("French in 2025?", "francês em 2025?"),
    t_graf=("reading charts", "leitura de gráficos"), t_pct=("percentage", "porcentagem"),
    pizza=("pie: 2023 → percent", "pizza: 2023 → porcentagem"), barras=("bars: 2024 → students", "barras: 2024 → alunos"),
    a2023=("2023", "2023"), a2024=("2024", "2024"),
    p1=("10% = 10 out of 100", "10% = 10 em cada 100"), p2=("10% of N = N ÷ 10", "10% de N = N ÷ 10"),
    p3=("10% of 100 = 10", "10% de 100 = 10"),
    soma=("280 + 80 + 20 + 20", "280 + 80 + 20 + 20"), t400=("= 400", "= 400"), t2025=("2025: 400 enrollments", "2025: 400 matrículas"),
    f1=("French: 10% (2023)", "francês: 10% (2023)"), f2=("10% of 400 = 400 ÷ 10", "10% de 400 = 400 ÷ 10"),
    f3=("40 enrollments", "40 matrículas"),
    c1=("60% of 400 = 240", "60% de 400 = 240"), c2=("25% of 400 = 100", "25% de 400 = 100"),
    c3=("10% of 400 = 40", "10% de 400 = 40"), c4=("5% of 400 = 20", "5% de 400 = 20"), c5=("240 + 100 + 40 + 20 = 400 ✓", "240 + 100 + 40 + 20 = 400 ✓"),
    r1=("French 2025 = 40", "francês 2025 = 40"), dobro=("× 2", "× 2"), alt=("ANSWER", "ALTERNATIVA"),
    pA=("2 → 10% of 20 (wrong total)", "2 → 10% de 20 (total errado)"), pB=("12 → doesn't come from the right math", "12 → não sai da conta certa"),
    pC=("20 → French in 2024 (wrong chart)", "20 → francês de 2024 (gráfico errado)"), pD=("22 → 20 + 2", "22 → 20 + 2"),
    pE=("40 → 10% of 400 ✓", "40 → 10% de 400 ✓"),
    des1=("what if 2025 had", "e se 2025 tivesse"), des2=("500 enrollments?", "500 matrículas?"),
    des3=("how many in Spanish?", "quantos no espanhol?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["what does each chart show: % or count?", "find the total", "apply the percent to the total"],
            ["o que cada gráfico mede: % ou quantidade?", "ache o total", "aplique a porcentagem sobre o total"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Percent-", "age"), ("Pie", "charts"), ("Bar", "charts")],
           [("Porcen-", "tagem"), ("Gráfico", "de setores"), ("Gráfico", "de barras")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("dois mil e vinte e quatro", "2024"), ("dois mil e vinte e três", "2023"),
    ("sessenta por cento", "60%"), ("vinte e cinco por cento", "25%"), ("dez por cento", "10%"), ("cinco por cento", "5%")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

PCT = (60, 25, 10, 5)            # 2023 (pizza)
QTD = (280, 80, 20, 20)          # 2024 (barras)
NOVO = (240, 100, 40, 20)        # 2025: % de 2023 sobre 400
CORES = (CYA, AMB, MNT, INK2)


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


def pizza(c, cx, cy, r, a, t=0, ks=(1, 1, 1, 1), foco=None, rot=None, rotk=(1, 1, 1, 1), title=None):
    """a pizza de 2023: fatias no sentido horário a partir do topo; ks = quanto cada fatia já apareceu; rot = textos"""
    if a <= 0:
        return
    ang = -90.0
    for i, p in enumerate(PCT):
        sw = 3.6 * p
        k = ks[i]
        al = a * (1 - 0.65 * (foco is not None and foco != i))
        if k > 0:
            path = skia.Path()
            path.moveTo(cx, cy)
            path.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ang, sw * k, False)
            path.close()
            c.drawPath(path, paint(CORES[i], 0.9 * al))
            c.drawPath(path, paint(BG0, al, stroke=3))
            m = math.radians(ang + sw / 2)
            rr = r * (0.62 if p >= 10 else 1.22)
            s = (rot or [f"{q}%" for q in PCT])[i]
            text_mid(c, s, cx + rr * math.cos(m), cy + rr * math.sin(m), 36 if p >= 10 else 30, "black",
                     BG0 if p >= 10 else CORES[i], al * ep(k, 0.7, 0.3) * rotk[i])
        ang += sw
    if title:
        label(c, title, cx, cy - r - 80, a, 34, WHITE, "black")


def barras(c, x0, yb, a, ks=(1, 1, 1, 1), foco=None, vals=QTD, kh=1.6, w=90, gap=170, title=None, cores=None, lab=26):
    """as barras de 2024 (quantidade de alunos)"""
    if a <= 0:
        return
    c.drawLine(x0 - 30, yb, x0 + gap * 3 + w + 30, yb, paint(WHITE, 0.8 * a, stroke=3))
    for i, v in enumerate(vals):
        k = ks[i]
        al = a * (1 - 0.65 * (foco is not None and foco != i))
        x = x0 + i * gap
        h = v * kh * ep(k, 0, 1)
        cor = (cores or CORES)[i]
        if h > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x, yb - h, x + w, yb), 8, 8), paint(cor, 0.9 * al))
            text_mid(c, str(v), x + w / 2, yb - h - 26, 34, "black", WHITE, al * ep(k, 0.6, 0.4))
        text_mid(c, L["idiomas"][i], x + w / 2, yb + 34, lab, "extrabold", WHITE if foco in (None, i) else INK2, al)
    if title:
        label(c, title, x0 + (gap * 3 + w) / 2, yb - 280 * kh - 70, a, 34, WHITE, "black")


GC0, GR0, GS = 190, 230, 34   # grade 20 × 20: canto, linha e espaçamento


def grade(c, a, t, grupos, t0=None, passo=0.0, destaque=None, rot=None):
    """400 bolinhas (uma por matrícula), coloridas por grupos [(quantidade, cor, t_aparece)]; destaque = índice do grupo"""
    if a <= 0:
        return
    i = 0
    for gi, (n, cor, tg) in enumerate(grupos):
        k = ep(t, tg, 0.5) if tg is not None else 1.0
        dim = destaque is not None and destaque != gi
        for j in range(n):
            x, y = GC0 + (i % 20) * GS, GR0 + (i // 20) * GS
            kk = clamp(k * 1.6 - j / max(n, 1) * 0.6)
            c.drawCircle(x, y, 11, paint(INK2, 0.15 * a))
            if kk > 0:
                c.drawCircle(x, y, 11 * ease_back(kk), paint(cor, a * (0.3 if dim else 0.95)))
            i += 1
    if rot:
        s, cor, kr = rot
        label(c, s, GC0 + 19 * GS / 2, GR0 + 20 * GS + 20, a * kr, 40, cor, "black")


def _grupos_2024(t0s):
    return [(q, cor, t0) for q, cor, t0 in zip(QTD, CORES, t0s)]


def _grupos_2025(t0s):
    return [(q, cor, t0) for q, cor, t0 in zip(NOVO, CORES, t0s)]


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao.png"), a, w=820, cx=LX, cy=440, hmax=600)
    popill(c, L["t_graf"], LX - 180, 850, 38, CYA, BG0, a * ep(t, te + 1.0, 0.3), t, te + 1.0)
    popill(c, L["t_pct"], LX + 220, 850, 38, AMB, BG0, a * ep(t, te + 2.2, 0.3), t, te + 2.2)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 36, INK2, "extrabold")
    label(c, L["escola"], RX, 310, a, 46, WHITE, "black")
    eq(c, [(L["g1"], AMB)], 440, a * ep(t, tb + 1.5, 0.3), 46)
    eq(c, [(L["g2"], CYA)], 560, a * ep(t, tc + 0.7, 0.3), 46)
    eq(c, [(L["pede"], MNT)], 740, a * ep(t, td + 1.7, 0.3), 56, box=MNT)


def b_graficos(c, t, C, B):
    ta, tb, tc = (C[f"02.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_graf"], a)
    ks = tuple(ep(t, tb + d, 0.6) for d in (3.1, 3.9, 5.1, 5.9))   # cada fatia quando é falada
    pizza(c, 260, 580, 150, a * ep(t, tb, 0.3), t, ks=ks, title=L["a2023"])
    kb = tuple(ep(t, tc + 0.5 + i * 0.3, 0.5) for i in range(4))
    barras(c, 515, 800, a * ep(t, tc, 0.3), ks=kb, kh=1.5, w=60, gap=108, title=L["a2024"], lab=21)
    board(c, a)
    eq(c, [(L["pizza"], WHITE)], 300, a * ep(t, tb + 0.2, 0.3), 44)
    eq(c, [("60% · ", CYA), ("25% · ", AMB), ("10% · ", MNT), ("5%", INK2)], 410, a * ep(t, tb + 3.1, 0.3), 54)
    eq(c, [(L["barras"], WHITE)], 600, a * ep(t, tc + 0.5, 0.3), 44)
    eq(c, [("280 · ", CYA), ("80 · ", AMB), ("20 · ", MNT), ("20", INK2)], 710, a * ep(t, tc + 1.5, 0.3), 54)


def b_porcentagem(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_pct"], a)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:   # 100 quadradinhos, 10 em menta
        for i in range(100):
            x, y = 260 + (i % 10) * 56, 250 + (i // 10) * 56
            k = ep(t, tb + i * 0.006, 0.3)
            on = i % 10 == 9 and t >= tb + 0.8 + (i // 10) * 0.08
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 48, 48), 8, 8), paint(MNT if on else BG2, kb * k * (1 if on else 0.9)))
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 48, 48), 8, 8), paint(INK2, 0.35 * kb * k, stroke=2))
        label(c, "10 / 100", LX, 860, kb * ep(t, tb + 1.8, 0.3), 44, MNT, "black")
    board(c, a)
    eq(c, [(L["p1"], WHITE)], 320, kb, 48)
    eq(c, [(L["p2"], MNT)], 500, a * ep(t, tc + 2.1, 0.3), 54, box=MNT)
    eq(c, [(L["p3"], WHITE)], 680, a * ep(t, td + 1.0, 0.3), 50)


def b_total(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_tot"], a)
    grade(c, a, t, _grupos_2024((tb + 1.2, tb + 2.3, tb + 3.2, tb + 3.8)), rot=("400", WHITE, ep(t, tc, 0.3)))
    board(c, a)
    eq(c, [("280", CYA), (" + ", WHITE), ("80", AMB), (" + ", WHITE), ("20", MNT), (" + ", WHITE), ("20", INK2)], 320,
       a * ep(t, tb + 1.2, 0.3), 58)
    eq(c, [(L["t400"], WHITE)], 460, a * ep(t, tc, 0.3), 72, box=CYA)
    eq(c, [(L["t2025"], AMB)], 640, a * ep(t, td + 1.0, 0.3), 48)


def b_frances(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_fr"], a)
    tr = tb + 1.6   # a grade passa para as porcentagens de 2023
    if t < tr:
        grade(c, a, t, _grupos_2024((None,) * 4))
    else:
        grade(c, a, t, _grupos_2025((tr, tr + 0.2, tr + 0.4, tr + 0.6)), destaque=2 if t >= tc else None,
              rot=("40", MNT, ep(t, td + 0.3, 0.3)))
    board(c, a)
    eq(c, [(L["f1"], MNT)], 320, a * ep(t, tb + 1.6, 0.3), 50)
    eq(c, [(L["f2"], WHITE)], 470, a * ep(t, tc + 0.7, 0.3), 50)
    eq(c, [(L["f3"], MNT)], 660, a * ep(t, td + 0.3, 0.3), 66, box=MNT)


def b_conferencia(c, t, C, B):
    ta, tb, tc = (C[f"06.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conf"], a)
    dts = (1.6, 2.7, 4.6, 6.5)
    pizza(c, LX, 540, 270, a, t, rot=[str(v) for v in NOVO], rotk=tuple(ep(t, tb + d, 0.3) for d in dts))
    board(c, a)
    for j, (k, d) in enumerate(zip(("c1", "c2", "c3", "c4"), dts)):
        eq(c, [(L[k], CORES[j] if j < 3 else WHITE)], 270 + j * 105, a * ep(t, tb + d, 0.3), 46)
    eq(c, [(L["c5"], MNT)], 760, a * ep(t, tc + 1.0, 0.3), 46, box=MNT)


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"07.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    yb, kh = 800, 9.0
    for j, (ano, v, t0) in enumerate((("2024", 20, ta), ("2025", 40, ta + 2.4))):
        k = a * ep(t, t0, 0.4)
        if k <= 0:
            continue
        x = 300 + j * 300
        h = v * kh * ep(t, t0, 0.8)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x - 70, yb - h, x + 70, yb), 10, 10), paint(MNT, (0.45 + 0.5 * j) * k))
        text_mid(c, str(v), x, yb - h - 34, 48, "black", WHITE, k)
        text_mid(c, ano, x, yb + 40, 34, "extrabold", WHITE, k)
    c.drawLine(180, yb, 780, yb, paint(WHITE, 0.8 * a, stroke=3))
    popill(c, L["dobro"], 450, 380, 44, AMB, BG0, a * ep(t, tb + 0.2, 0.3), t, tb + 0.2)
    label(c, L["idiomas"][2], 450, 900, a, 36, MNT, "black")
    board(c, a)
    eq(c, [(L["r1"], MNT)], 300, a * ep(t, ta + 2.4, 0.3), 56)
    kc = a * ep(t, tc, 0.3)
    if kc > 0:
        for j, le in enumerate("ABCDE"):
            x = BX0 + 130 + j * 160
            ok = le == "E"
            c.drawCircle(x, 500, 34, paint(MNT if ok else INK2, kc))
            text_mid(c, le, x, 500, 36, "black", BG0, kc)
        check(c, BX0 + 130 + 4 * 160 + 38, 470, 18, kc)
        eq(c, [(L["alt"] + " ", WHITE), ("E", MNT)], 700, kc, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td, te = (C[f"08.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    kb = ep(t, tb + 0.2, 0.3)
    barras(c, 160, 760, a, foco=2 if kb > 0 else None, kh=1.6, w=90, gap=170, title=L["a2024"],
           cores=(CYA, AMB, _mix_cor(MNT, RED, kb), INK2))
    board(c, a)
    linhas = (("A", L["pA"], RED, tc + 0.2), ("B", L["pB"], RED, te + 0.2), ("C", L["pC"], RED, tb + 0.2),
              ("D", L["pD"], RED, td + 0.2), ("E", L["pE"], MNT, ta))
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


def _mix_cor(h1, h2, u):
    u = clamp(u)
    p = [int(h1[i:i + 2], 16) for i in (1, 3, 5)]
    q = [int(h2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(x + (y - x) * u):02X}" for x, y in zip(p, q))


def b_desafio(c, t, C, B):
    ta, tb, tc = (C[f"09.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    pizza(c, LX, 600, 230, a, t, foco=1 if t >= tb + 4.2 else None,
          rot=["60%", "?", "10%", "5%"] if t >= tb + 4.2 else None)
    popill(c, "500", LX, 230, 44, WHITE, BG0, a * ep(t, tb + 2.4, 0.3), t, tb + 2.4)
    board(c, a)
    label(c, L["des1"], RX, 320, a * ep(t, tb, 0.3), 46, WHITE, "black")
    eq(c, [(L["des2"], AMB)], 440, a * ep(t, tb + 2.4, 0.3), 60, box=AMB)
    label(c, L["des3"], RX, 600, a * ep(t, tb + 4.2, 0.3), 50, CYA, "black")
    label(c, L["comenta"], RX, 740, a * ep(t, tc, 0.3), 40, AMB, "extrabold")


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
    """miniatura de cada aula: % · a pizza · as barras"""
    if i == 0:
        text_mid(c, "10%", cx, cy, 100, "black", CYA, a)
    elif i == 1:
        pizza(c, cx, cy, 90, a, t, rot=["", "", "", ""])
    else:
        barras(c, cx - 150, cy + 80, a, kh=0.5, w=50, gap=80, vals=QTD)


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
            c.drawCircle(x, 790, 38, paint(MNT if v == "E" else INK2, kl, stroke=4))
            text_mid(c, v, x, 790, 38, "black", WHITE, kl)


BLOCKS = dict(gancho=b_gancho, graficos=b_graficos, porcentagem=b_porcentagem, total=b_total, frances=b_frances,
              conferencia=b_conferencia, resposta=b_resposta, pegadinhas=b_pegadinhas, desafio=b_desafio,
              resumo=b_resumo, aulas=b_aulas)
