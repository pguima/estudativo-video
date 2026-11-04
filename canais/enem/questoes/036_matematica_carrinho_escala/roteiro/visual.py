"""Visual — Estudativo · Questão de Matemática 036 (aula horizontal 1920x1080): ENEM 2025, questão 150, o carrinho de
controle remoto (escala e conversão de unidades). Design system de matemática: _ferramentas/matematica.py.
Figuras: as cinco telas do controle (tela()), redesenhadas com as posições medidas no enunciado; a régua da escala
(regua()) e as barras do tamanho real em metros (metros()). Cores: âmbar = dado (escala, medida do desenho),
ciano = o deslocamento, menta = a resposta (tela III), coral = as alternativas erradas."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_036_matematica_carrinho_escala.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.b": "data", "01.c": "data", "01.e": "shimmer", "02.b": "data", "02.c": "lock", "02.d": "confirm",
        "03.b": "data", "03.c": "data", "03.d": "deny", "03.e": "lock", "04.b": "confirm", "04.c": "confirm",
        "04.d": "confirm", "05.b": "confirm", "05.c": "confirm", "06.b": "data", "06.c": "data", "06.d": "confirm",
        "07.b": "confirm", "07.c": "impact", "08.b": "deny", "08.c": "deny", "08.d": "deny", "08.e": "deny",
        "09.b": "alert", "10.a": "shimmer", "11.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 036", "QUESTÃO DE MATEMÁTICA · 036"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_esc=("TOOL 1 · WHAT A SCALE IS", "FERRAMENTA 1 · O QUE É ESCALA"),
    s_eng=("TOOL 2 · THE DRAWING TRICKS YOU", "FERRAMENTA 2 · O DESENHO ENGANA"),
    s_p1=("STEP 1 · SCREENS I, II AND III", "PASSO 1 · TELAS I, II E III"),
    s_p2=("STEP 2 · SCREENS IV AND V", "PASSO 2 · TELAS IV E V"),
    s_cmp=("COMPARING IN METERS", "COMPARANDO EM METROS"), s_resp=("THE ANSWER", "A RESPOSTA"),
    s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"), s_des=("CHALLENGE", "DESAFIO"),
    s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 150", "ENEM 2025 · questão 150"), carrinho=("the remote-control car", "o carrinho de controle remoto"),
    g1=("5 trips, 5 screens", "5 deslocamentos, 5 telas"), g2=("each screen, its own scale", "cada tela, uma escala"),
    pede=("which was the longest?", "qual foi o maior de verdade?"),
    t_esc=("scale", "escala"), t_conv=("unit conversion", "conversão de unidades"),
    desenho=("drawing", "desenho"), real=("real", "realidade"),
    e1=("1 cm on the drawing", "1 cm no desenho"), e2=("= 100 cm for real", "= 100 cm de verdade"),
    e3=("real = drawing × 100", "real = desenho × 100"), e4=("9 cm × 100 = 900 cm", "9 cm × 100 = 900 cm"), e5=("= 9 m", "= 9 m"),
    n1=("biggest drawing: I (9 cm)", "maior desenho: I (9 cm)"), n2=("but each screen has its own scale", "mas cada tela tem sua escala"),
    n3=("comparing drawings ✗", "comparar desenhos ✗"), n4=("everything → real size", "tudo → tamanho real"),
    m1=("100 cm = 1 m", "100 cm = 1 m"), m2=("cm ÷ 100 = m", "cm ÷ 100 = m"),
    maior=("longest: screen III", "maior: tela III"),
    r1=("screen III = 30 m", "tela III = 30 m"), r2=("drawing: only 5 cm!", "desenho: só 5 cm!"), alt=("ANSWER", "ALTERNATIVA"),
    pA=("I → biggest drawing, only 9 m", "I → maior desenho, só 9 m"), pB=("II → only 15 m", "II → só 15 m"),
    pC=("III → 30 m ✓", "III → 30 m ✓"), pD=("IV → 21 m, second longest", "IV → 21 m, o segundo maior"),
    pE=("V → biggest scale, 20 m", "V → maior escala, só 20 m"),
    des1=("a sixth screen:", "uma sexta tela:"), des2=("4 cm at 1 : 800", "4 cm em 1 : 800"),
    des3=("longer than screen III?", "maior que a tela III?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["read each drawing's scale", "drawing × scale number", "compare in the same unit"],
            ["leia a escala de cada desenho", "desenho × número da escala", "compare na mesma unidade"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Scales", ""), ("Units and", "conversions"), ("Ratio and", "proportion")],
           [("Escalas", ""), ("Unidades e", "conversões"), ("Razão e", "proporção")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("um para cem", "1 : 100"), ("um para trezentos", "1 : 300"),
    ("um para seiscentos", "1 : 600"), ("um para setecentos", "1 : 700"), ("um para mil", "1 : 1000"),
    ("um para oitocentos", "1 : 800"), ("mil e quinhentos", "1500"), ("dois mil e cem", "2100"), ("três mil", "3000"),
    ("dois mil", "2000"), ("mil", "1000")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))

ROMANO = ("I", "II", "III", "IV", "V")
CM = (9, 5, 5, 3, 2)               # medida no desenho
ESC = (100, 300, 600, 700, 1000)   # 1 : ESC
REAL = tuple(a * b for a, b in zip(CM, ESC))   # 900, 1500, 3000, 2100, 2000 cm
# posições medidas no enunciado (fração da moldura): ponto inicial, ponto final, letras, rótulo da medida
GEO = (
    ((0.163, 0.844), (0.794, 0.146), ("A", "B"), (0.333, 0.396)),
    ((0.794, 0.146), (0.591, 0.731), ("B", "C"), (0.470, 0.377)),
    ((0.585, 0.731), (0.312, 0.193), ("C", "D"), (0.200, 0.490)),
    ((0.313, 0.193), (0.313, 0.566), ("D", "E"), (0.500, 0.358)),
    ((0.309, 0.566), (0.468, 0.434), ("E", "F"), (0.560, 0.640)),
)


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


def _seta(c, x0, y0, x1, y1, cor, a, s=14):
    """ponta de seta no meio do segmento, apontando de (x0, y0) para (x1, y1)"""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    ang = math.atan2(y1 - y0, x1 - x0)
    for d in (2.5, -2.5):
        c.drawLine(mx + s * 0.4 * math.cos(ang), my + s * 0.4 * math.sin(ang),
                   mx - s * math.cos(ang + d / 4.5), my - s * math.sin(ang + d / 4.5), paint(cor, a, stroke=4))


def tela(c, i, x, y, w, a, k=1.0, foco=None, cor_seg=CYA, cor_esc=AMB, esc_k=1.0, num=True, dado=None):
    """a tela i do controle remoto (moldura 4:3, canto superior esquerdo em x, y); k = quanto do deslocamento já foi
    desenhado; foco = tela em destaque (as outras ficam apagadas); dado = (cm, escala) de uma tela inventada"""
    if a <= 0:
        return
    h = w * 0.752
    al = a * (1 - 0.6 * (foco is not None and foco != i))
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 14, 14)
    c.drawRRect(r, paint("#5B6478", al))
    bw = w * 0.04
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x + bw, y + bw, w - 2 * bw, h - 2 * bw), 8, 8), paint(BG1, al))
    if foco == i:
        c.drawRRect(r, paint(MNT if foco == 2 else AMB, a, stroke=5))
    (u0, v0), (u1, v1), (n0, n1), (lu, lv) = GEO[i] if dado is None else GEO[4]
    if dado is not None:
        (u0, v0), (u1, v1), lu, lv = (0.18, 0.62), (0.70, 0.30), 0.30, 0.30
    X0, Y0, X1, Y1 = x + u0 * w, y + v0 * h, x + u1 * w, y + v1 * h
    kk = ep(k, 0, 1)
    if kk > 0:
        xe, ye = X0 + (X1 - X0) * kk, Y0 + (Y1 - Y0) * kk
        c.drawLine(X0, Y0, xe, ye, paint(cor_seg, al, stroke=max(3, w * 0.014)))
        if kk > 0.55:
            _seta(c, X0, Y0, X1, Y1, cor_seg, al, w * 0.04)
    sz = w * 0.075
    for (px, py), nome, kp in (((X0, Y0), n0, 1.0), ((X1, Y1), n1, kk)):
        if kp > 0.9 and dado is None:
            c.drawCircle(px, py, w * 0.018, paint(RED, al))
            dx = -1 if px < x + w * 0.5 else 1
            text_mid(c, nome, px + dx * w * 0.05, py - w * 0.03, sz * 0.85, "extrabold", RED, al)
    cm, esc = (CM[i], ESC[i]) if dado is None else dado
    text_mid(c, f"{cm} cm", x + lu * w, y + lv * h, sz, "extrabold", WHITE, al * ep(k, 0.6, 0.4))
    text_mid(c, f"1 : {esc:,}".replace(",", " "), x + w * 0.74, y + h * 0.84, sz, "black", cor_esc, al * esc_k)
    if num:
        text_mid(c, ROMANO[i] if dado is None else "VI", x + w / 2, y + h + sz * 1.0, sz * 1.15, "black", WHITE, al)


def linha_telas(c, a, t, y=190, w=330, x0=91, gap=22, ks=None, foco=None, esc_k=None):
    for i in range(5):
        tela(c, i, x0 + i * (w + gap), y, w, a, k=1.0 if ks is None else ks[i], foco=foco,
             esc_k=1.0 if esc_k is None else esc_k[i])


def metros(c, a, t, x0=330, y0=260, dy=130, kw=42, ks=(1,) * 5, foco=None, cores=None, lab=46, titulo=None):
    """barras horizontais com o tamanho real de cada deslocamento, em metros"""
    if a <= 0:
        return
    c.drawLine(x0, y0 - dy * 0.55, x0, y0 + dy * 4.45, paint(WHITE, 0.8 * a, stroke=3))
    for i, v in enumerate(REAL):
        m = v // 100
        k = ks[i]
        al = a * (1 - 0.65 * (foco is not None and foco != i))
        y = y0 + i * dy
        text_mid(c, ROMANO[i], x0 - 50, y, lab, "black", WHITE, al)
        wb = m * kw * ep(k, 0, 1)
        cor = (cores or (CYA,) * 5)[i]
        if wb > 0:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y - dy * 0.3, wb, dy * 0.6), 10, 10), paint(cor, 0.9 * al))
            text_mid(c, f"{m} m", x0 + wb + 20, y, lab, "black", WHITE, al * ep(k, 0.6, 0.4), align="left")
    if titulo:
        label(c, titulo, x0 + 30 * kw / 2, y0 - dy * 0.95, a, 34, INK2, "extrabold")


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao.png"), a, w=820, cx=LX, cy=450, hmax=620)
    popill(c, L["t_esc"], LX - 200, 860, 38, AMB, BG0, a * ep(t, te + 1.0, 0.3), t, te + 1.0)
    popill(c, L["t_conv"], LX + 170, 860, 38, CYA, BG0, a * ep(t, te + 1.8, 0.3), t, te + 1.8)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 36, INK2, "extrabold")
    label(c, L["carrinho"], RX, 310, a, 46, WHITE, "black")
    eq(c, [(L["g2"], AMB)], 450, a * ep(t, tb + 1.0, 0.3), 50)
    eq(c, [(L["g1"], WHITE)], 570, a * ep(t, tc, 0.3), 46)
    eq(c, [(L["pede"], MNT)], 740, a * ep(t, td + 0.6, 0.3), 52, box=MNT)


def regua(c, a, t, t0, t1):
    """1 cm no desenho (em cima) vira 100 cm na realidade (embaixo, 100 tracinhos de 1 cm)"""
    if a <= 0:
        return
    x0 = 150
    k0 = a * ep(t, t0, 0.3)
    label(c, L["desenho"], x0, 300, k0, 32, INK2, "extrabold", align="left")
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, 340, 7.4, 46), 3, 3), paint(AMB, k0))
    text_mid(c, "1 cm", x0 + 30, 363, 40, "black", AMB, k0, align="left")
    k1 = ep(t, t1, 1.2)
    label(c, L["real"], x0, 520, a * ep(t, t1, 0.3), 32, INK2, "extrabold", align="left")
    n = int(100 * k1)
    for j in range(n):
        xx = x0 + j * 7.4
        c.drawRect(skia.Rect.MakeXYWH(xx, 560, 6.2, 46), paint(CYA if j % 10 else WHITE, a * 0.9))
    if n > 0:
        text_mid(c, f"{n} cm", x0 + 370, 660, 44, "black", CYA, a)
        k2 = a * ep(t, t1 + 1.3, 0.3)
        text_mid(c, "= 1 m", x0 + 370, 730, 40, "black", WHITE, k2)


def b_escala(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_esc"], a)
    regua(c, a, t, tb + 2.0, tb + 3.6)
    board(c, a)
    eq(c, [("1 : 100", AMB)], 280, a * ep(t, tb, 0.3), 72)
    eq(c, [(L["e1"], AMB)], 400, a * ep(t, tb + 2.0, 0.3), 44)
    eq(c, [(L["e2"], CYA)], 480, a * ep(t, tb + 3.6, 0.3), 44)
    eq(c, [(L["e3"], CYA)], 620, a * ep(t, tc + 2.0, 0.3), 52, box=CYA)
    eq(c, [(L["e4"], WHITE)], 760, a * ep(t, td + 1.0, 0.3), 46)
    eq(c, [(L["e5"], MNT)], 850, a * ep(t, td + 4.2, 0.3), 46)


def b_engana(c, t, C, B):
    ta, tb, tc, td, te = (C[f"03.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_eng"], a)
    ks = tuple(ep(t, ta + 0.2 + 0.25 * i, 0.6) for i in range(5))
    foco = 0 if tb + 0.3 <= t < tc else None
    esc_k = tuple(1 if t < tc else 0.55 + 0.45 * math.cos((t - tc) * 6) ** 2 for _ in range(5))
    linha_telas(c, a, t, y=200, ks=ks, foco=foco, esc_k=esc_k)
    eq(c, [(L["n1"], AMB)], 640, a * ep(t, tb + 0.3, 0.3) * (1 - ep(t, tc, 0.25)), 46, cx=960, maxw=1500)
    eq(c, [(L["n2"], WHITE)], 640, a * ep(t, tc + 0.25, 0.3), 46, cx=960, maxw=1500)
    eq(c, [(L["n3"], RED)], 740, a * ep(t, td + 0.8, 0.3), 50, cx=960, maxw=1500)
    eq(c, [(L["n4"], MNT)], 860, a * ep(t, te + 1.0, 0.3), 54, cx=960, box=MNT, maxw=1500)


def _conta(c, i, a, t, t_mul, t_res, x0=91, w=330, gap=22):
    """a conta embaixo da tela i: '9 × 100' e '= 900 cm'"""
    cx = x0 + i * (w + gap) + w / 2
    k1 = a * ep(t, t_mul, 0.3)
    if k1 > 0:
        text_mid(c, f"{CM[i]} × {ESC[i]}", cx, 640, 46, "black", WHITE, k1)
    k2 = a * ep(t, t_res, 0.3)
    if k2 > 0:
        cor = CYA
        s = f"{REAL[i]} cm"
        tw = text_w(s, "black", 48)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - tw / 2 - 18, 712, tw + 36, 72), 14, 14), paint(cor, k2, stroke=3))
        text_mid(c, s, cx, 748, 48, "black", cor, k2)


def b_passo1(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], d_out=0.01)
    header(c, L["s_p1"], a)
    linha_telas(c, a, t, y=190, foco=None)
    for i, t0 in enumerate((tb, tc, td)):
        _conta(c, i, a, t, t0 + 1.4, t0 + 2.9)
    for i in (3, 4):
        text_mid(c, "?", 91 + i * 352 + 165, 680, 70, "black", INK2, a * 0.6)


def b_passo2(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], d=0.01)
    header(c, L["s_p2"], a)
    linha_telas(c, a, t, y=190)
    for i in range(3):
        _conta(c, i, a, t, 0, 0)
    for i, t0 in ((3, tb), (4, tc)):
        k = 1 - ep(t, t0 + 1.0, 0.3)
        text_mid(c, "?", 91 + i * 352 + 165, 680, 70, "black", INK2, a * 0.6 * k)
        _conta(c, i, a, t, t0 + 1.0, t0 + 2.6)


def b_comparar(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_cmp"], a)
    dts = (0.0, 0.9, 1.7, 2.5, 3.4)
    ks = tuple(ep(t, tc + d, 0.6) for d in dts)
    foco = 2 if t >= td else None
    cores = tuple(MNT if (i == 2 and foco == 2) else CYA for i in range(5))
    metros(c, a, t, x0=230, y0=290, dy=135, kw=17, ks=ks, foco=foco, cores=cores, lab=42)
    board(c, a)
    eq(c, [(L["m1"], WHITE)], 300, a * ep(t, tb, 0.3), 50)
    eq(c, [(L["m2"], CYA)], 430, a * ep(t, tb + 1.8, 0.3), 52, box=CYA)
    eq(c, [("9 · 15 · 30 · 21 · 20", WHITE)], 590, a * ep(t, tc, 0.3), 52)
    eq(c, [(L["maior"], MNT)], 760, a * ep(t, td + 0.5, 0.3), 58, box=MNT)


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"07.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    tela(c, 2, 170, 230, 700, a, foco=2, cor_seg=MNT, num=False)
    popill(c, "30 m", LX, 820, 60, MNT, BG0, a * ep(t, ta + 2.0, 0.3), t, ta + 2.0)
    board(c, a)
    eq(c, [(L["r1"], MNT)], 290, a * ep(t, ta + 2.0, 0.3), 56)
    eq(c, [(L["r2"], AMB)], 420, a * ep(t, tb + 0.8, 0.3), 50)
    kc = a * ep(t, tc, 0.3)
    if kc > 0:
        for j, le in enumerate("ABCDE"):
            x = BX0 + 130 + j * 160
            ok = le == "C"
            c.drawCircle(x, 580, 34, paint(MNT if ok else INK2, kc))
            text_mid(c, le, x, 580, 36, "black", BG0, kc)
        check(c, BX0 + 130 + 2 * 160 + 38, 550, 18, kc)
        eq(c, [(L["alt"] + " ", WHITE), ("C", MNT)], 760, kc, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td, te = (C[f"08.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    foco = None
    for f, t0 in ((0, tb), (4, tc), (3, td), (1, te)):
        if t >= t0:
            foco = f
    cores = tuple(MNT if i == 2 else (RED if i == foco else CYA) for i in range(5))
    metros(c, a, t, x0=200, y0=290, dy=135, kw=20, foco=foco, cores=cores, lab=42)
    board(c, a)
    linhas = (("A", L["pA"], RED, tb + 0.2), ("B", L["pB"], RED, te + 0.2), ("C", L["pC"], MNT, ta),
              ("D", L["pD"], RED, td + 0.2), ("E", L["pE"], RED, tc + 0.2))
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
    ta, tb, tc, td = (C[f"09.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    tela(c, 0, 170, 260, 700, a * ep(t, tb, 0.3), k=ep(t, tb + 0.2, 1.0), dado=(4, 800), num=False)
    popill(c, "?", LX, 860, 60, AMB, BG0, a * ep(t, tc, 0.3), t, tc)
    board(c, a)
    label(c, L["des1"], RX, 300, a * ep(t, tb, 0.3), 46, WHITE, "black")
    eq(c, [(L["des2"], AMB)], 430, a * ep(t, tb + 1.2, 0.3), 60, box=AMB)
    label(c, L["des3"], RX, 600, a * ep(t, tc, 0.3), 50, CYA, "black")
    label(c, L["comenta"], RX, 740, a * ep(t, td, 0.3), 40, AMB, "extrabold")


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
    """miniatura de cada aula: 1 : 100 · cm → m · a : b"""
    s, cor = (("1 : 100", CYA), ("cm → m", AMB), ("a : b", MNT))[i]
    text_mid(c, s, cx, cy, 80, "black", cor, a)


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
            c.drawCircle(x, 790, 38, paint(MNT if v == "C" else INK2, kl, stroke=4))
            text_mid(c, v, x, 790, 38, "black", WHITE, kl)


BLOCKS = dict(gancho=b_gancho, escala=b_escala, engana=b_engana, passo1=b_passo1, passo2=b_passo2,
              comparar=b_comparar, resposta=b_resposta, pegadinhas=b_pegadinhas, desafio=b_desafio,
              resumo=b_resumo, aulas=b_aulas)
