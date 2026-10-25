"""Visual — Estudativo · Questão de Matemática 001 (aula horizontal 1920x1080): triângulo retângulo, cateto c = 5, lados inteiros.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, figuras, legenda).
Versão em inglês (Estudativo English): o mesmo arquivo com --lang en (roteiro/cenas_en.py; textos da tela em T, abaixo).
Cores com função: âmbar = dado do problema, ciano = a (hipotenusa), menta = b / certo, vermelho = erro / descartado."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True   # textos da tela em pares (inglês, português) no T: não usa textos_en.py
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_001_matematica_triangulo_cateto_5.mp4"   # --lang en: ..._en.mp4
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.a": "impact", "01.c": "deny", "01.d": "shimmer", "06.c": "confirm", "07.c": "shimmer", "07.g": "confirm",
        "08.b": "confirm", "09.b": "impact", "10.e": "deny", "11.c": "impact", "11.d": "impact", "12.b": "confirm",
        "12.c": "shimmer", "13.c": "confirm", "13.d": "lock", "15.a": "shimmer", "15.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.20, lufs=-14, bpm=100, sfx=_SFX)

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 001", "QUESTÃO DE MATEMÁTICA · 001"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_nomes=("THE NAMES", "OS NOMES"),
    s_pit=("PYTHAGOREAN THEOREM", "TEOREMA DE PITÁGORAS"), s_inf=("INFINITELY MANY ANSWERS?", "INFINITAS RESPOSTAS?"),
    s_chute=("JUST TEST NUMBERS?", "TESTAR NÚMEROS?"), s_isolar=("STEP 1 · ISOLATE", "PASSO 1 · ISOLAR"),
    s_prod=("SPECIAL PRODUCT", "PRODUTO NOTÁVEL"), s_ex=("A NUMBER EXAMPLE", "EXEMPLO COM NÚMEROS"),
    s_aplica=("STEP 2 · FACTOR", "PASSO 2 · FATORAR"), s_div=("STEP 3 · DIVISORS", "PASSO 3 · DIVISORES"),
    s_sist=("STEP 4 · SYSTEM", "PASSO 4 · SISTEMA"), s_conf=("CHECK", "CONFERÊNCIA"),
    s_gen=("OTHER LEGS", "OUTROS CATETOS"), s_res=("SUMMARY", "RESUMO"),
    pit=("PYTHAGORAS", "PITÁGORAS"),
    inteiros=("WHOLE-NUMBER SIDES", "LADOS INTEIROS"), abc_int=("a, b, c whole numbers", "a, b, c inteiros"),
    falta=("Missing information?", "Falta informação?"), nao_falta=("NOT AT ALL!", "NÃO FALTA!"),
    hip=("hypotenuse", "hipotenusa"), cateto=("leg", "cateto"), maior=("always the longest side", "sempre o maior lado"),
    ang=("right angle = 90°", "ângulo reto = 90°"), d_hip=("a → hypotenuse", "a → hipotenusa"),
    d_hip2=("(opposite the right angle)", "(oposta ao ângulo reto)"), d_cat=("legs", "catetos"),
    aqui_hip=("there, 5 is the hypotenuse", "lá, o 5 é a hipotenusa"), nosso=("in our triangle, 5 is a leg", "no nosso, o 5 é cateto"),
    duas=("2 UNKNOWNS", "2 INCÓGNITAS"), lento=("SLOW", "LENTO"), outra=("ANOTHER ANSWER?", "E SE TIVER OUTRA?"),
    melhor=("A BETTER WAY →", "CAMINHO MELHOR →"), dif2=("difference of two squares", "diferença de dois quadrados"),
    pn=("SPECIAL PRODUCTS", "PRODUTOS NOTÁVEIS"), soma_dif=("product of a sum and a difference", "produto da soma pela diferença"),
    distrib=("distributive property", "distributiva"), cancelam=("cancel out", "se cancelam"),
    x_a=("x → a   ·   y → b", "x → a   ·   y → b"), inteiro=("whole", "inteiro"),
    q25=("25 = ? × ?", "25 = ? × ?"), maior_menor=("smaller × larger", "menor × maior"),
    b0=("b = 0 → not a triangle", "b = 0 → não é triângulo"), unica=("the only whole-number answer", "a única resposta inteira"),
    c9=("AND WITH c = 9?", "E COM c = 9?"), mais_uma=("hint: more than one answer!", "dica: pode ter mais de uma!"),
    passos=(["Pythagoras", "Isolate a² − b²", "Special product", "Divisors of 25", "Solve the system"],
            ["Pitágoras", "Isolar a² − b²", "Produto notável", "Divisores de 25", "Resolver o sistema"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Pythagorean", "theorem"), ("Special", "products"), ("Systems of", "equations")],
           [("Teorema de", "Pitágoras"), ("Produtos", "notáveis"), ("Sistemas de", "equações")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
DEC = "." if EN else ","
matematica.NUMEROS_EXTRA[:] = [("ninety degrees", "90°")] if EN else [("noventa graus", "90°")]


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- blocos
P = lambda s, col=WHITE: (s, col)   # noqa: E731
TRI = (200, 760, 600, 400)          # triângulo do problema no painel da esquerda: x0, y0, wb, hc


def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    tri(c, *TRI, a, t, "a = ?", "b = ?", "c = 5", size=52, hl=("c",) if t < tb else ("a", "b"))
    popill(c, L["inteiros"], LX, 885, 30, MNT, BG0, a, t, ta + 1.6)
    board(c, a)
    eq(c, [P("c = 5", AMB)], 300, a, 92)
    label(c, L["abc_int"], RX, 400, a * ep(t, ta + 1.6, 0.3), 40, MNT, "bold")
    eq(c, [P("a = ?", CYA), P("     "), P("b = ?", MNT)], 540, a * ep(t, tb, 0.3), 96)
    kc = a * ep(t, tc, 0.25) * (1 - ep(t, td, 0.3))
    label(c, L["falta"], RX, 680, kc, 46, INK2, "bold")
    popill(c, L["nao_falta"], RX, 770, 40, AMB, BG0, kc, t, tc + 1.2)
    kd = a * ep(t, td, 0.3)
    w1, w2 = (text_w(s, "black", 34) + 41 for s in (L["pit"], L["s_prod"]))   # duas pílulas lado a lado com um "+" no meio
    x1 = RX - (w1 + w2 + 90) / 2 + w1 / 2
    x2 = x1 + w1 / 2 + 90 + w2 / 2
    popill(c, L["pit"], x1, 730, 34, CYA, BG0, kd, t, td + 1.6)
    label(c, "+", x1 + w1 / 2 + 45, 730, kd * ep(t, td + 2.2, 0.2), 54, WHITE, "black")
    popill(c, L["s_prod"], x2, 730, 34, AMB, BG0, kd, t, td + 2.4)


def b_nomes(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_nomes"], a)
    hl = ("ang",) if t < tb else ("a",) if t < tc else ("b", "c") if t < td else ("c",)
    sub = {}
    if t >= tb:
        sub["a"] = L["hip"]
    if t >= tc:
        sub["b"] = sub["c"] = L["cateto"]
    tri(c, *TRI, a, t, "a" if t >= tb else "", "b" if t >= tc else "", ("c = 5" if t >= td else "c") if t >= tc else "",
        size=52, hl=hl, sub=sub, ang="90°" if t >= ta + 1.2 else None)
    board(c, a)
    label(c, L["ang"], RX, 290, a * ep(t, ta + 1.0, 0.3), 50, AMB, "black")
    label(c, L["d_hip"], RX, 420, a * ep(t, tb, 0.3), 54, CYA, "black")
    label(c, L["d_hip2"], RX, 480, a * ep(t, tb + 0.4, 0.3), 32, INK2)
    label(c, L["maior"], RX, 528, a * ep(t, tb + 1.4, 0.3), 32, INK2)
    eq(c, [P("b", MNT), P(", "), P("c", AMB), P(" → " + L["d_cat"])], 650, a * ep(t, tc, 0.3), 54)
    eq(c, [P("c = 5", AMB)], 800, a * ep(t, td, 0.3), 80, box=AMB)


def b_pitagoras(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_pit"], a)
    # figura: o nosso triângulo → o 3-4-5 (exemplo) → volta ao nosso
    ex = a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.3))
    nosso = a * (1 - ep(t, tb, 0.3) + ep(t, tc, 0.3))
    tri(c, *TRI, nosso, t, "a", "b", "c = 5" if t >= tc else "c", size=52, hl=("c",) if t >= tc else ())
    tri(c, 220, 760, 560, 420, ex, t, "5", "4", "3", size=56, hl=("a",) if t >= tb + 6 else ())
    board(c, a)
    eq(c, [P("a²", CYA), P(" = "), P("b²", MNT), P(" + "), P("c²", AMB)], 285, a * ep(t, ta + 0.3, 0.3), 82, box=CYA)
    dim = 1 - 0.6 * ep(t, tc, 0.3)
    eq(c, [P("3² + 4² = 5²")], 420, a * ep(t, tb + 0.6, 0.3) * dim, 54)
    eq(c, [P("9 + 16 = 25")], 500, a * ep(t, tb + 3.4, 0.3) * dim, 54)
    label(c, L["aqui_hip"], RX, 575, a * ep(t, tb + 6.0, 0.3) * dim, 32, INK2)
    label(c, L["nosso"], RX, 665, a * ep(t, tc, 0.3), 34, AMB, "bold")
    k5 = a * ep(t, tc + 0.6, 0.3) * (1 - ep(t, td, 0.25))
    eq(c, [P("a²", CYA), P(" = "), P("b²", MNT), P(" + "), P("5²", AMB)], 790, k5, 76)
    eq(c, [P("a²", CYA), P(" = "), P("b²", MNT), P(" + "), P("25", AMB)], 790, a * ep(t, td + 0.4, 0.3), 76, box=AMB)


def b_infinitas(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_inf"], a)
    # triângulo real com c = 5 e b variando de 1 a 3 (proporção verdadeira)
    u = clamp((t - tc) / max(1.0, td - tc - 0.5))
    bv = 1 + 2 * ease_io(u) if t >= tc else 2.4
    inteiro = t >= tc and abs(bv - round(bv)) < 0.08
    lab_b = f"b = {round(bv)}" if inteiro else ("b" if t < tc else "")
    av = math.sqrt(bv * bv + 25)
    lab_a = f"a ≈ {av:.2f}".replace(".", DEC) if t >= tc else "a"
    if t >= td:
        bv, lab_b, lab_a = 2.4, "b", "a"
    tri(c, 330, 790, bv * 80, 400, a, t, lab_a, lab_b, "5", size=46)
    popill(c, L["inteiros"], LX, 900, 32, MNT, BG0, a, t, td + 0.8)
    board(c, a)
    eq(c, [P("a²", CYA), P(" = "), P("b²", MNT), P(" + "), P("25", AMB)], 260, a, 60)
    popill(c, L["duas"], RX, 360, 30, AMB, BG0, a, t, ta + 0.4)
    rows = [("1", "26", "5.10"), ("2", "29", "5.39"), ("3", "34", "5.83")]
    for i, (b, sq, ap) in enumerate(rows):
        ki = a * ep(t, tc + (0, 3.0, 5.0)[i], 0.3) * (1 - 0.5 * ep(t, td, 0.3))
        eq(c, [P(f"b = {b}", MNT), P("  →  "), P(f"a = √{sq} ≈ {ap.replace('.', DEC)}", CYA)], 470 + i * 85, ki, 46)
    label(c, "...  ∞", RX, 725, a * ep(t, tc + 6.0, 0.3) * (1 - 0.5 * ep(t, td, 0.3)), 50, INK2, "black")
    if t >= td:
        eq(c, [P(L["inteiros"] + "!", MNT)], 830, a * ep(t, td + 0.6, 0.3), 60, box=MNT)


def b_chute(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_chute"], a)
    n = int(clamp((t - ta) / 0.55, 0, 5.99)) + 1 if t >= ta else 1
    tri(c, *TRI, a, t, "a", f"b = {n}?", "5", size=50)
    board(c, a)
    for i in range(6):
        b = i + 1
        ki = a * ep(t, ta + 0.4 + i * 0.5, 0.25) * (1 - 0.55 * ep(t, tb, 0.3))
        x = RX - 210 + (i // 3) * 420
        y = 300 + (i % 3) * 100
        pos = eq(c, [P(f"b = {b}", MNT), P(f" → a² = {b * b + 25}")], y, ki, 44, cx=x, maxw=330)
        if pos:
            cross(c, pos[-1][1] + 30, y, 18, ki * ep(t, ta + 0.7 + i * 0.5, 0.2))
    popill(c, L["lento"], RX - 200, 640, 34, RED, WHITE, a, t, tb + 1.0)
    popill(c, L["outra"], RX + 150, 640, 34, RED, WHITE, a, t, tb + 2.2)
    eq(c, [P(L["melhor"], AMB)], 790, a * ep(t, tc, 0.3), 60, box=AMB)


def b_isolar(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_isolar"], a)
    # esquerda: triângulo → a forma "a² sem b²" (diferença de quadrados)
    kq = ep(t, td, 0.4)
    tri(c, *TRI, a * (1 - kq), t, "a", "b", "5", size=50)
    quadrados(c, a * kq, t)
    label(c, L["dif2"], LX, 875, a * kq, 36, AMB, "bold")
    board(c, a)
    pos = eq(c, [P("a²", CYA), P(" = "), P("b²", MNT), P(" + "), P("25", AMB)], 330, a, 84)
    u = ease_io(prog(t, tb + 0.2, 0.9))
    if t >= ta and u < 1 and pos:
        bx0 = (pos[2][0] + pos[2][1]) / 2
        bx1 = RX - 90
        if t < tb:   # o b² que vai mudar de lado pulsa
            c.drawCircle(bx0, 330, 62, blur_paint(MNT, (0.2 + 0.25 * math.sin(t * 8)) * a, 20))
        else:
            text_mid(c, "+b²" if u < 0.5 else "−b²", bx0 + (bx1 - bx0) * u, 330 + 170 * u, 84, "black",
                     MNT if u < 0.5 else RED, a)
    eq(c, [P("a²", CYA), P(" − "), P("b²", MNT), P(" = "), P("25", AMB)], 500, a * ep(t, tb + 1.0, 0.3), 84,
       box=AMB if t >= tc else None)
    if t >= td:   # chave sob a diferença
        kd = a * ep(t, td, 0.4)
        x0, x1 = RX - 250, RX + 20
        m = (x0 + x1) / 2
        p = skia.Path(); p.moveTo(x0, 570); p.quadTo(x0, 600, x0 + 30, 600); p.lineTo(m - 20, 600)
        p.quadTo(m, 600, m, 625); p.quadTo(m, 600, m + 20, 600); p.lineTo(x1 - 30, 600); p.quadTo(x1, 600, x1, 570)
        c.drawPath(p, paint(AMB, kd, stroke=5, cap_round=True))
        label(c, L["dif2"], m + 60, 680, kd, 38, AMB, "bold")
        label(c, "→ " + L["s_prod"].lower(), RX, 780, a * ep(t, td + 2.0, 0.3), 40, WHITE, "black")


def b_produto(c, t, C, B):
    ta, tb, tc, td, te, tf, tg = (C[f"07.{k}"] for k in "abcdefg")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_prod"], a)
    # esquerda: a lista de produtos notáveis; o da soma pela diferença em destaque
    label(c, L["pn"], LX, 260, a * ep(t, ta, 0.3), 44, AMB, "black")
    linhas = ["(x + y)² = x² + 2xy + y²", "(x − y)² = x² − 2xy + y²", "(x + y)(x − y) = x² − y²"]
    for i, s in enumerate(linhas):
        ki = a * ep(t, ta + 0.6 + i * 0.5, 0.3)
        y = 380 + i * 110
        if i == 2:
            kb = ki * ep(t, tb, 0.3)
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(LX - 380, y - 46, 760, 92), 18, 18)
            c.drawRRect(r, paint(CYA, 0.12 * kb)); c.drawRRect(r, paint(CYA, kb, stroke=4))
            text_mid(c, s, LX, y, 44, "black", CYA if t >= tb else WHITE, ki)
        else:
            text_mid(c, s, LX, y, 44, "black", WHITE, ki * (1 - 0.6 * ep(t, tb, 0.3)))
    label(c, L["soma_dif"], LX, 680, a * ep(t, tb + 0.5, 0.3), 32, CYA, "bold")
    board(c, a)
    eq(c, [P("(x + y)", CYA), P("(x − y)", MNT), P(" = "), P("x² − y²", AMB)], 270, a * ep(t, tc, 0.3), 70, box=AMB)
    label(c, L["distrib"], RX, 365, a * ep(t, td, 0.3), 34, INK2, "bold")
    termos = [("x · x = x²", te), ("x · (−y) = −xy", te + 2.0), ("y · x = +xy", tf), ("y · (−y) = −y²", tf + 2.0)]
    for i, (s, t0) in enumerate(termos):
        eq(c, [P(s)], 450 + (i // 2) * 90, a * ep(t, t0, 0.3), 44, cx=RX - 210 + (i % 2) * 420, maxw=400)
    kg = a * ep(t, tg, 0.3)
    pos = eq(c, [P("x²"), P(" − xy + xy", RED if t >= tg + 0.6 else WHITE), P(" − y²")], 680, kg, 60)
    if pos:
        strike(c, pos[1][0] + 10, pos[1][1], 680, kg, ep(t, tg + 0.6, 0.4))
        label(c, L["cancelam"], (pos[1][0] + pos[1][1]) / 2, 740, kg * ep(t, tg + 0.6, 0.3), 30, RED, "bold")
    eq(c, [P("= x² − y²", AMB)], 830, a * ep(t, tg + 1.6, 0.3), 64, box=AMB)


def b_exemplo(c, t, C, B):
    ta, tb = C["08.a"], C["08.b"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ex"], a)
    quadrados(c, a, t, A=420, Bq=126, lab=("10", "3"), cy=500)
    label(c, "100 − 9 = 91", LX, 890, a * ep(t, tb + 1.6, 0.3), 44, AMB, "black")
    board(c, a)
    eq(c, [P("(10 + 3)", CYA), P("(10 − 3)", MNT)], 300, a * ep(t, ta + 0.3, 0.3), 70)
    eq(c, [P("= 13 · 7 = "), P("91", AMB)], 400, a * ep(t, ta + 2.6, 0.3), 70)
    eq(c, [P("10² − 3²")], 580, a * ep(t, tb, 0.3), 70)
    pos = eq(c, [P("= 100 − 9 = "), P("91", AMB)], 680, a * ep(t, tb + 1.6, 0.3), 70)
    if pos:
        check(c, pos[-1][1] + 50, 680, 28, a * ep(t, tb + 2.6, 0.25))


def b_aplica(c, t, C, B):
    ta, tb, tc = (C[f"09.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_aplica"], a)
    quadrados(c, a, t, u=ep(t, ta + 2.0, 2.2), cx=LX + 60, cy=480)
    board(c, a)
    eq(c, [P("a² − b²"), P(" = "), P("(a + b)", CYA), P("(a − b)", MNT)], 290, a * ep(t, ta + 0.3, 0.3), 70)
    label(c, L["x_a"], RX, 380, a * ep(t, ta + 0.3, 0.3), 32, INK2, "bold")
    pos = eq(c, [P("(a + b)", CYA), P(" · "), P("(a − b)", MNT), P(" = "), P("25", AMB)], 540, a * ep(t, tb, 0.3), 84, box=AMB)
    if pos and t >= tc:
        kc = a * ep(t, tc, 0.3)
        for i in (0, 2):
            label(c, L["inteiro"], (pos[i][0] + pos[i][1]) / 2, 640, kc, 32, CYA if i == 0 else MNT, "bold")
        label(c, "× → 25", (pos[0][0] + pos[2][1]) / 2, 720, kc * ep(t, tc + 1.5, 0.3), 40, AMB, "black")


def b_divisores(c, t, C, B):
    ta, tb, tc, td, te = (C[f"10.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_div"], a)
    # esquerda: se b → 0, o triângulo "achata" e deixa de existir
    kz = ep(t, te + 1.0, 1.2)
    tri(c, 200, 760, 600 * (1 - kz) + 2, 400, a, t, "a", "b = 0" if kz > 0.95 else "b", "5", size=50)
    board(c, a)
    eq(c, [P("(a + b)", CYA), P(" · "), P("(a − b)", MNT), P(" = "), P("25", AMB)], 260, a, 58)
    eq(c, [P(L["q25"])], 350, a * ep(t, ta + 0.3, 0.3), 54)
    for i, (s, y, t0) in enumerate((("1 × 25", 470, tb + 0.4), ("5 × 5", 570, tb + 1.8))):
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        ruim = i == 1 and t >= te
        col = RED if ruim else (MNT if i == 0 and t >= td else INK2)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(RX - 200, y - 42, 400, 84), 18, 18)
        c.drawRRect(r, paint(BG1, 0.9 * ki)); c.drawRRect(r, paint(col, ki, stroke=4))
        text_mid(c, s, RX - 20, y, 56, "black", WHITE, ki * (0.55 if ruim else 1))
        if ruim:
            strike(c, RX - 120, RX + 80, y, ki, ep(t, te + 0.3, 0.3))
            cross(c, RX + 150, y, 24, ki * ep(t, te + 0.3, 0.2))
    if t >= td:   # menor × maior sobre o 1 × 25
        kd = a * ep(t, td, 0.3)
        label(c, "a − b", RX - 112, 404, kd, 30, MNT, "black")
        label(c, "a + b", RX + 62, 404, kd, 30, CYA, "black")
    eq(c, [P("a + b", CYA), P("  >  "), P("a − b", MNT)], 690, a * ep(t, tc + 1.2, 0.3), 58)
    label(c, L["maior_menor"], RX, 760, a * ep(t, td, 0.3), 32, INK2, "bold")
    label(c, L["b0"], RX, 845, a * ep(t, te + 2.2, 0.3), 38, RED, "black")


def b_sistema(c, t, C, B):
    ta, tb, tc, td = (C[f"11.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_sist"], a)
    tri(c, *TRI, a, t, "a = 13" if t >= tc + 2 else "a", "b = 12" if t >= td + 2 else "b", "5", size=52,
        hl=("a",) if tc + 2 <= t < td else ("b",) if t >= td + 2 else ())
    board(c, a)
    x0 = RX - 220
    k1, k2 = a * ep(t, ta + 0.4, 0.3), a * ep(t, ta + 2.2, 0.3)
    p1 = eq(c, [P("a "), P("+ b", MNT), P(" = 25")], 290, k1, 70, cx=RX - 60)
    p2 = eq(c, [P("a "), P("− b", MNT), P(" = 1")], 390, k2, 70, cx=RX - 60)
    if k1 > 0:   # chave do sistema
        p = skia.Path(); p.moveTo(x0, 245); p.quadTo(x0 - 30, 248, x0 - 30, 290); p.quadTo(x0 - 30, 325, x0 - 52, 340)
        p.quadTo(x0 - 30, 355, x0 - 30, 390); p.quadTo(x0 - 30, 432, x0, 435)
        c.drawPath(p, paint(WHITE, k1 * 0.8, stroke=5, cap_round=True))
    kb = a * ep(t, tb, 0.3)
    if kb > 0:
        text_mid(c, "+", x0 - 80, 390, 60, "black", AMB, kb)
        c.drawLine(x0 - 20, 450, x0 - 20 + 470 * ep(t, tb, 0.4), 450, paint(WHITE, kb * 0.7, stroke=4, cap_round=True))
        u = ep(t, tb + 1.6, 0.4)
        for p, y in ((p1, 290), (p2, 390)):
            if p:
                strike(c, p[1][0] + 4, p[1][1], y, kb, u, MNT)
    eq(c, [P("2a = 26")], 540, a * ep(t, tc, 0.3), 70, cx=RX - 210)
    label(c, "→", RX + 30, 540, a * ep(t, tc + 1.4, 0.3), 56, WHITE, "black")
    eq(c, [P("a = 13", CYA)], 540, a * ep(t, tc + 1.4, 0.3), 70, cx=RX + 230, box=CYA)
    eq(c, [P("13 + b = 25")], 700, a * ep(t, td + 0.4, 0.3), 64, cx=RX - 210)
    label(c, "→", RX + 30, 700, a * ep(t, td + 2.0, 0.3), 56, WHITE, "black")
    eq(c, [P("b = 12", MNT)], 700, a * ep(t, td + 2.0, 0.3), 70, cx=RX + 230, box=MNT)


def b_confere(c, t, C, B):
    ta, tb, tc = (C[f"12.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conf"], a)
    u = ease_io(prog(t, ta + 0.3, 1.2))   # vira o 5-12-13 de verdade
    tri(c, 160 + 20 * (1 - u), 760, 600 + 120 * u, 400 - 100 * u, a, t, "13", "12", "5", size=54)
    board(c, a)
    eq(c, [P("12²", MNT), P(" + "), P("5²", AMB), P(" = 144 + 25")], 300, a * ep(t, ta + 0.6, 0.3), 64)
    eq(c, [P("= 169")], 400, a * ep(t, ta + 4.4, 0.3), 64)
    pos = eq(c, [P("13²", CYA), P(" = 169")], 540, a * ep(t, tb, 0.3), 70, box=CYA)
    if pos:
        check(c, pos[-1][1] + 60, 540, 30, a * ep(t, tb + 1.4, 0.25))
    popill(c, "5 · 12 · 13", RX, 700, 52, AMB, BG0, a, t, tc)
    label(c, L["unica"], RX, 805, a * ep(t, tc + 2.0, 0.3), 36, MNT, "bold")


def b_generaliza(c, t, C, B):
    ta, tb, tc, td = (C[f"13.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    k7 = ep(t, tc + 2.0, 0.6)     # vira o 7-24-25 de verdade
    nove = ep(t, td, 0.4)
    tri(c, 160, 760, 600 + 48 * k7, 400 - 211 * k7, a * (1 - nove), t,
        "25" if k7 > 0.5 else "a", "24" if k7 > 0.5 else "b", "7", size=50)
    tri(c, *TRI, a * nove, t, "a = ?", "b = ?", "c = 9", size=52, hl=("c",))
    board(c, a)
    eq(c, [P("c = 7", AMB)], 280, a * ep(t, tb, 0.3), 64)
    eq(c, [P("(a + b)", CYA), P("(a − b)", MNT), P(" = 49", AMB)], 380, a * ep(t, tb + 1.2, 0.3), 58)
    eq(c, [P("1 × 49  →  "), P("a = 25", CYA), P(",  "), P("b = 24", MNT)], 490, a * ep(t, tc, 0.3), 52)
    popill(c, "7 · 24 · 25", RX, 590, 44, AMB, BG0, a, t, tc + 4.0)
    eq(c, [P(L["c9"], AMB)], 730, a * ep(t, td, 0.3), 72, box=AMB)
    label(c, L["mais_uma"], RX, 835, a * ep(t, td + 4.5, 0.3), 36, MNT, "bold")


def b_resumo(c, t, C, B):
    ks = [C[f"14.{k}"] for k in "bcdef"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_res"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 260 + i * 130
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 620
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 56, "black", WHITE, ki, align="left")
        check(c, 1380, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula indicada: triângulo · (a + b)(a − b) · sistema"""
    if i == 0:
        tri(c, cx - 90, cy + 62, 180, 124, a, t, "", "", "", size=24)
    elif i == 1:
        eq(c, [P("(a+b)", CYA), P("(a−b)", MNT)], cy, a, 50, cx=cx, maxw=300)
    else:
        text_mid(c, "{", cx - 150, cy - 6, 130, "regular", INK2, a)
        label(c, "a + b = 25", cx - 110, cy - 32, a, 44, CYA, "black", align="left")
        label(c, "a − b = 1", cx - 110, cy + 34, a, 44, MNT, "black", align="left")


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"15.{k}"] for k in "abcdef")
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
        text_mid(c, l1, cx, 610, 50, "black", WHITE, kk)
        text_mid(c, l2, cx, 674, 50, "black", cores[i], kk)
        c.restore()
    label(c, L["no_canal"], 960, 870, ka * ep(t, te, 0.3), 40, AMB, "extrabold")
    kg = a * ep(t, tf, 0.4)
    if kg > 0:
        glow_text(c, L["canal"], 960, 450, 120, "black", WHITE, kg, glow=0.12)
        w = text_w(L["canal"], "black", 120)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(960 - w / 2, 480, w * ep(t, tf + 0.3, 0.6), 14), 7, 7), paint(AMB, kg))
        pulse = 1 + 0.03 * math.sin(t * 5)
        c.save(); c.translate(960, 620); c.scale(pulse, pulse)
        pill(c, L["inscreva"], 0, 0, 38, CYA, BG0, kg * ep(t, tf + 0.8, 0.3))
        c.restore()
        tri(c, 760, 900, 400, 167, kg * 0.9 * ep(t, tf + 1.2, 0.4), t, "13", "12", "5", size=34)


BLOCKS = dict(gancho=b_gancho, nomes=b_nomes, pitagoras=b_pitagoras, infinitas=b_infinitas, chute=b_chute,
              isolar=b_isolar, produto=b_produto, exemplo=b_exemplo, aplica=b_aplica, divisores=b_divisores,
              sistema=b_sistema, confere=b_confere, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
