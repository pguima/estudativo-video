"""Visual — Estudativo · Questão de Matemática 008 (aula horizontal 1920x1080): ENEM 2025, questão 137, a solução de 99,95%.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = dado do problema (10 L, 99,95%, 99,90%, S2), ciano = incógnita (T, o que sai) e S1 no desenho,
menta = resultado conferido, coral = a pegadinha. S2 é 0,05% da solução (invisível no desenho): aparece numa lupa."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_008_matematica_solucao_9995.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.d": "deny", "01.e": "shimmer", "02.c": "confirm", "02.d": "confirm", "03.c": "confirm", "03.d": "confirm",
        "04.a": "alert", "04.c": "deny", "05.a": "shimmer", "05.c": "confirm", "06.e": "impact", "07.b": "impact",
        "07.c": "confirm", "08.a": "shimmer", "08.d": "confirm", "09.c": "confirm", "09.d": "lock", "11.a": "shimmer",
        "11.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.20, lufs=-14, bpm=100, sfx=_SFX)

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 008", "QUESTÃO DE MATEMÁTICA · 008"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_pct=("THE TOOL · PERCENTAGE", "A FERRAMENTA · PORCENTAGEM"),
    s_comp=("ONLY S1 AND S2", "SÓ S1 E S2"), s_peg=("THE TRAP", "A PEGADINHA"),
    s_nao=("STEP 1 · WHAT DOESN'T CHANGE", "PASSO 1 · O QUE NÃO MUDA"), s_novo=("STEP 2 · THE NEW TOTAL", "PASSO 2 · O NOVO TOTAL"),
    s_ret=("STEP 3 · HOW MUCH COMES OUT", "PASSO 3 · A RETIRADA"), s_porque=("WHY SO MUCH?", "POR QUE TANTO?"),
    s_batata=("THE POTATO PARADOX", "O PARADOXO DA BATATA"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 137", "ENEM 2025 · questão 137"),
    gotinha=("just a drop?", "só uma gotinha?"), p_pct=("PERCENTAGE", "PORCENTAGEM"), p_nao=("WHAT DOESN'T CHANGE", "O QUE NÃO MUDA"),
    de_cada=("percent = out of every 100", "por cento = de cada 100"),
    quadradinho=("1/20 of a little square", "1/20 de um quadradinho"),
    so=("the solution has ONLY S1 and S2", "a solução tem SÓ S1 e S2"),
    antes=("BEFORE · 10 L", "ANTES · 10 L"), depois=("AFTER · T L", "DEPOIS · T L"), lupa=("magnifier: S2 enlarged", "lupa: S2 ampliado"),
    depois_eq=("after: ", "depois: "),
    errado=("different totals!", "totais diferentes!"),
    nao_sub=("you can't subtract % of different totals", "não se subtrai % de totais diferentes"),
    de10=("99.95% of 10 L", "99,95% de 10 L"), deT=("99.90% of ? L", "99,90% de ? L"),
    so_s1=("only S1 comes out → S2 stays the same", "sai só S1 → o S2 fica igual"),
    colher=("5 mL ≈ a teaspoon", "5 mL ≈ uma colher de chá"), nao_muda=("doesn't change", "não muda"),
    sai_s1=("only S1 comes out", "sai só S1"),
    nova=("new solution: T liters", "nova solução: T litros"), div=("÷ 0.001 on both sides", "÷ 0,001 dos dois lados"),
    metade=("HALF!", "METADE!"), sairam=("5 L came out", "saíram 5 L"),
    dobrou=("S2: 0.05% → 0.10%  (×2)", "S2: 0,05% → 0,10%  (×2)"), mesma=("same amount → total ÷ 2", "mesma quantidade → total ÷ 2"),
    confere=("check:", "conferência:"),
    bat1=("100 kg · 99% water", "100 kg · 99% de água"), bat2=("dries to 98% water", "seca até 98% de água"),
    peso=("weight = ?", "peso = ?"), seca=("dry part: 1% = 1 kg → 2%", "parte seca: 1% = 1 kg → 2%"),
    bat3=("doubled → weight ÷ 2", "dobrou → peso ÷ 2"), agua=("water", "água"), seco=("dry", "seco"),
    desafio=("WHAT IF IT WERE 99.80%?", "E SE FOSSE 99,80%?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["S2 = 100% − S1: 0.05% → 0.10%", "S2 = 0.005 L (doesn't change)", "0.001 × T = 0.005 → T = 5 L", "10 − 5 = 5 L (E)"],
            ["S2 = 100% − S1: 0,05% → 0,10%", "S2 = 0,005 L (não muda)", "0,001 × T = 0,005 → T = 5 L", "10 − 5 = 5 L (E)"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("", "Percentage"), ("Ratio and", "proportion"), ("Linear", "equations")],
           [("", "Porcentagem"), ("Razão e", "proporção"), ("Equação do", "1º grau")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("noventa e nove vírgula noventa e cinco por cento", "99,95%"),
    ("noventa e nove vírgula noventa e cinco", "99,95"), ("noventa e nove vírgula noventa por cento", "99,90%"),
    ("noventa e nove vírgula noventa", "99,90"), ("noventa e nove vírgula oitenta por cento", "99,80%"),
    ("zero vírgula zero cinco por cento", "0,05%"), ("zero vírgula zero cinco sobre cem", "0,05/100"),
    ("zero vírgula zero cinco", "0,05"), ("zero vírgula dez por cento", "0,10%"), ("zero vírgula dez", "0,10"),
    ("zero vírgula zero zero zero cinco", "0,0005"), ("zero vírgula zero zero cinco litro", "0,005 L"),
    ("zero vírgula zero zero cinco", "0,005"), ("zero vírgula zero zero um", "0,001"),
    ("nove vírgula nove nove cinco litros", "9,995 L"), ("quatro vírgula nove nove cinco", "4,995"),
    ("zero vírgula nove nove nove", "0,999"), ("noventa e nove por cento", "99%"), ("noventa e oito por cento", "98%"),
    ("vinte por cento", "20%"), ("cem por cento", "100%"), ("dois por cento", "2%"), ("um por cento", "1%"),
    ("vinte sobre cem", "20/100"), ("s um", "S1"), ("s dois", "S2"), ("cinco mililitros", "5 mL"),
    ("dez litros", "10 L"), ("cinco litros", "5 L"), ("cinquenta quilos", "50 kg"), ("cem quilos", "100 kg"),
    ("um quilo", "1 kg"), ("primeiro grau", "1º grau")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
DEC = "." if EN else ","
n_ = lambda s: s.replace(",", ".") if EN else s   # noqa: E731  número com a vírgula do idioma


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- linha de contas com frações empilhadas (da questão 007)
P = lambda s, col=WHITE: (s, col)            # noqa: E731
F = lambda n, d, col=WHITE: ("/", n, d, col)  # noqa: E731


def _w(it, size):
    if it[0] == "/":
        return max(text_w(it[1], "black", size * 0.8), text_w(it[2], "black", size * 0.8)) + size * 0.3
    return text_w(it[0], "black", size)


def row(c, items, cy, a, size=60, cx=RX, box=None, maxw=840):
    """como eq(), mas aceita frações F(num, den, cor); devolve [(x0, x1)] de cada item"""
    if a <= 0:
        return []
    f = ease_out(clamp(a))
    tot = sum(_w(it, size) for it in items)
    while tot > maxw:
        size -= 2
        tot = sum(_w(it, size) for it in items)
    tem_frac = any(it[0] == "/" for it in items)
    x = cx - tot / 2
    yy = cy + (1 - f) * 18
    if box:
        hh = size * (2.3 if tem_frac else 1.34)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 26, yy - hh / 2, tot + 52, hh), 18, 18)
        c.drawRRect(r, blur_paint(box, 0.3 * f, 22))
        c.drawRRect(r, paint(BG1, 0.95 * f))
        c.drawRRect(r, paint(box, f, stroke=4))
    pos = []
    for it in items:
        w = _w(it, size)
        if it[0] == "/":
            _, n, d, col = it
            s2 = size * 0.8
            m = x + w / 2
            text_mid(c, n, m, yy - s2 * 0.62, s2, "black", col, f)
            text_mid(c, d, m, yy + s2 * 0.62, s2, "black", col, f)
            c.drawLine(x + size * 0.1, yy, x + w - size * 0.1, yy, paint(col, f, stroke=max(3, size * 0.06), cap_round=True))
        else:
            text(c, it[0], x, yy + size * 0.36, size, "black", it[1], f, align="left")
        pos.append((x, x + w))
        x += w
    return pos


# ---------------------------------------------------------------- figuras
def recipiente(c, cx, base, a, t, nivel=1.0, w=330, h=520, hl_s2=0.0, fantasma=0.0, rot="10 L", rot_col=AMB, marca5=0.0):
    """recipiente de vidro com a solução (S1 em ciano); nivel 1 = 10 L. S2 (0,05%) vira gotinhas âmbar no fundo.
    fantasma: contorno tracejado da parte que saiu; marca5: risco dos 5 L"""
    if a <= 0:
        return
    x0, x1, top = cx - w / 2, cx + w / 2, base - h
    cheio = h * 0.86
    lv = base - cheio * nivel
    # líquido
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([(cx, lv), (cx, base)], [hexc(CYA), hexc("#1F6F99")]))
    p.setAlphaf(0.55 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0 + 8, lv, x1 - 8, base - 8), 18, 18), p)
    c.drawLine(x0 + 10, lv, x1 - 10, lv + 2 * math.sin(t * 3), paint(WHITE, 0.6 * a, stroke=3))
    if fantasma > 0:
        pf = paint(CYA, 0.7 * a * fantasma, stroke=3)
        pf.setPathEffect(skia.DashPathEffect.Make([14, 10], t * 30 % 24))
        c.drawRect(skia.Rect.MakeLTRB(x0 + 14, base - cheio, x1 - 14, lv), pf)
    # S2: gotinhas no fundo
    pul = 0.5 + 0.5 * math.sin(t * 6)
    for i in range(5):
        gx, gy = cx - 60 + i * 30, base - 30 - 10 * (i % 2)
        if hl_s2 > 0:
            c.drawCircle(gx, gy, 16, blur_paint(AMB, (0.4 + 0.4 * pul) * a * hl_s2, 10))
        c.drawCircle(gx, gy, 6, paint(AMB, a))
    # vidro
    pth = skia.Path(); pth.moveTo(x0 - 16, top); pth.lineTo(x0, top + 14); pth.lineTo(x0, base - 24)
    pth.quadTo(x0, base, x0 + 24, base); pth.lineTo(x1 - 24, base); pth.quadTo(x1, base, x1, base - 24)
    pth.lineTo(x1, top + 14); pth.lineTo(x1 + 16, top)
    c.drawPath(pth, blur_paint(WHITE, 0.25 * a, 8, stroke=8))
    c.drawPath(pth, paint(WHITE, 0.85 * a, stroke=5))
    for k in range(1, 11):   # graduação
        yk = base - cheio * k / 10
        c.drawLine(x1 - (40 if k % 5 == 0 else 22), yk, x1 - 4, yk, paint(WHITE, 0.45 * a, stroke=3))
    if marca5 > 0:
        y5 = base - cheio * 0.5
        c.drawLine(x0 - 30, y5, x1 + 30, y5, paint(AMB, a * marca5, stroke=3))
        label(c, "5 L", x1 + 46, y5, a * marca5, 34, AMB, "black", "left")
    if rot:
        label(c, rot, cx, base + 50, a, 46, rot_col, "black")


def lupa(c, cx, cy, r, a, frac, t, col=AMB, rotulo="S2"):
    """lupa: um pedaço da barra ampliado; frac = largura de S2 dentro do círculo (0..1)"""
    if a <= 0:
        return
    c.save()
    pth = skia.Path(); pth.addCircle(cx, cy, r)
    c.clipPath(pth, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), paint(CYA, 0.45 * a))
    c.drawRect(skia.Rect.MakeXYWH(cx + r - 2 * r * frac, cy - r, 2 * r * frac, 2 * r), paint(AMB, a))
    c.restore()
    c.drawCircle(cx, cy, r, paint(WHITE, a, stroke=6))
    c.drawLine(cx + r * 0.72, cy + r * 0.72, cx + r * 1.15, cy + r * 1.15, paint(WHITE, a, stroke=14, cap_round=True))
    if rotulo and frac > 0.08:
        text_mid(c, rotulo, cx + r - r * frac, cy, 30, "black", BG0, a)


def barra(c, x, y, w, a, t, pct_s2, titulo, r=78, ux=None):
    """barra 100% (S1 ciano, S2 âmbar invisível de tão fino) + lupa ×z na ponta direita"""
    if a <= 0:
        return
    label(c, titulo, x, y - 52, a, 32, WHITE, "extrabold", "left")
    rrect(c, x, y - 26, w, 52, 12, CYA, 0.45 * a)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y - 26, w, 52), 12, 12), paint(CYA, a, stroke=3))
    lx = ux if ux is not None else x + w - 40
    c.drawCircle(x + w - 6, y, 22, paint(AMB, 0.9 * a, stroke=3))
    c.drawLine(x + w - 6, y + 22, lx, y + 80, paint(AMB, 0.7 * a, stroke=3))
    lupa(c, lx, y + 80 + r, r, a, min(1, pct_s2 * 3), t)   # S2 ampliado: 0,05% → 15% do círculo, 0,10% → 30%


def grade100(c, cx, cy, a, t, n_hl=0, hl_a=0.0, cell=46, gap=6, col=AMB):
    """100 quadradinhos (10 × 10); os n_hl primeiros acendem"""
    if a <= 0:
        return
    tot = 10 * cell + 9 * gap
    x0, y0 = cx - tot / 2, cy - tot / 2
    for i in range(100):
        r, k = divmod(i, 10)
        x, y = x0 + k * (cell + gap), y0 + r * (cell + gap)
        on = i < n_hl and hl_a > 0
        kk = ep(hl_a, i / max(1, n_hl) * 0.6, 0.4) if on else 0
        rrect(c, x, y, cell, cell, 8, col if on and kk > 0 else BG2, (0.9 if kk > 0 else 0.7) * a)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, cell, cell), 8, 8), paint(CYA, 0.25 * a, stroke=2))


def batata(c, cx, cy, s, a, seca=0.0):
    """batata (marrom) com manchas; seca 0 → 1 encolhe e fica enrugada"""
    if a <= 0:
        return
    k = 1 - 0.2 * seca
    c.save(); c.translate(cx, cy); c.scale(k, k * (1 - 0.06 * seca))
    c.drawOval(skia.Rect.MakeXYWH(-s * 0.62, -s * 0.42, s * 1.24, s * 0.84), blur_paint("#C08A4A", 0.3 * a, 20))
    c.drawOval(skia.Rect.MakeXYWH(-s * 0.62, -s * 0.42, s * 1.24, s * 0.84), paint("#B07A3F", a))
    c.drawOval(skia.Rect.MakeXYWH(-s * 0.62, -s * 0.42, s * 1.24, s * 0.84), paint("#5E3B17", a, stroke=4))
    for i, (px, py) in enumerate(((-0.3, -0.1), (0.1, 0.15), (0.35, -0.12), (-0.05, -0.25))):
        c.drawCircle(px * s, py * s, s * 0.035, paint("#5E3B17", 0.8 * a))
    for i in range(int(4 * seca)):
        yy = -s * 0.2 + i * s * 0.13
        c.drawLine(-s * 0.35, yy, s * 0.3, yy + s * 0.04, paint("#5E3B17", 0.6 * a * seca, stroke=3))
    c.restore()


def _card_enunciado(c, a):
    img = _img_enunciado()
    w = 800
    h = img.height() * w / img.width()
    x, y = LX - w / 2 + 10, 540 - h / 2
    rrect(c, x - 18, y - 18, w + 36, h + 36, 22, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


@lru_cache(None)
def _img_enunciado():
    from pathlib import Path
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / "questao.png"))


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    row(c, [P("10 L", AMB), P("  ·  S1 + S2")], 360, a, 64)
    row(c, [P("S1:  "), P(n_("99,95%"), AMB)], 490, a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.15)), 64)
    if t >= tc:
        row(c, [P("S1:  "), P(n_("99,95%"), AMB), P("  →  ", INK2), P(n_("99,90%"), AMB)], 490, a * ep(t, tc, 0.3), 64)
    row(c, [P("sai: " if not EN else "out: "), P("? L", CYA)], 630, a * ep(t, td, 0.3), 80, box=CYA)
    label(c, L["gotinha"], RX, 740, a * ep(t, td + 1.6, 0.3) * (1 - ep(t, te, 0.3)), 42, INK2, "bold")
    ke = a * ep(t, te, 0.3)
    w1, w2 = (text_w(s, "black", 32) + 38 for s in (L["p_pct"], L["p_nao"]))
    x1 = RX - (w1 + w2 + 80) / 2 + w1 / 2
    x2 = x1 + w1 / 2 + 80 + w2 / 2
    popill(c, L["p_pct"], x1, 790, 32, CYA, BG0, ke, t, te + 3.0)
    label(c, "+", x1 + w1 / 2 + 40, 790, ke * ep(t, te + 3.6, 0.2), 54, WHITE, "black")
    popill(c, L["p_nao"], x2, 790, 32, AMB, BG0, ke, t, te + 4.6)


def b_porcentagem(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_pct"], a)
    kg = a * (1 - ep(t, td, 0.3))
    grade100(c, LX, 520, kg, t, n_hl=20, hl_a=prog(t, tb, 1.0))
    label(c, "20 / 100", LX, 840, kg * ep(t, tb + 0.6, 0.3), 44, AMB, "black")
    kd = a * ep(t, td, 0.3)
    if kd > 0:   # 0,05% = 1/20 de um quadradinho
        s = 300
        rrect(c, LX - s / 2, 520 - s / 2, s, s, 22, BG2, kd)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(LX - s / 2, 520 - s / 2, s, s), 22, 22), paint(CYA, kd, stroke=4))
        c.drawRect(skia.Rect.MakeXYWH(LX + s / 2 - s / 20, 520 - s / 2 + 4, s / 20 - 4, s - 8), paint(AMB, kd * ep(t, td + 0.8, 0.3)))
        label(c, "= 1 / 100", LX, 520 + s / 2 + 50, kd, 38, INK2, "bold")
        label(c, n_("0,05%") + " = " + L["quadradinho"], LX, 520 + s / 2 + 110, kd * ep(t, td + 1.0, 0.3), 38, AMB, "black")
    board(c, a)
    label(c, L["de_cada"], RX, 270, a * ep(t, ta + 1.2, 0.3), 46, WHITE, "black")
    row(c, [P("20% = "), F("20", "100", AMB)], 410, a * ep(t, tb, 0.3), 64)
    row(c, [P("20% de 50 = " if not EN else "20% of 50 = "), F("20", "100", AMB), P(" × 50 = "), P("10", MNT)], 580,
        a * ep(t, tc + 0.8, 0.3), 60)
    row(c, [P(n_("0,05%") + " = "), F(n_("0,05"), "100", AMB), P(" = "), P(n_("0,0005"), CYA)], 760, a * ep(t, td, 0.3), 60, box=CYA)


def b_complemento(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_comp"], a)
    barra(c, 130, 300, 760, a * ep(t, tb, 0.3), t, 0.05, L["antes"] + "  ·  S2 = " + n_("0,05%"), ux=560)
    barra(c, 130, 640, 760, a * ep(t, td, 0.3), t, 0.10, L["depois"] + "  ·  S2 = " + n_("0,10%"), ux=560)
    label(c, L["lupa"], 170, 960 - 40, a * ep(t, tb + 1.0, 0.3), 26, INK2, "semibold", "left")
    board(c, a)
    label(c, L["so"], RX, 270, a * ep(t, ta + 0.6, 0.3), 40, WHITE, "black")
    eq(c, [("S1", CYA), (" + ", WHITE), ("S2", AMB), (" = 100%", WHITE)], 400, a * ep(t, tb, 0.3), 64)
    eq(c, [("S2 = 100% − ", WHITE), (n_("99,95%"), AMB), (" = ", WHITE), (n_("0,05%"), AMB)], 560, a * ep(t, tc, 0.3), 54, box=AMB)
    eq(c, [(L["depois_eq"] + "S2 = 100% − ", WHITE), (n_("99,90%"), AMB), (" = ", WHITE), (n_("0,10%"), AMB)], 730,
       a * ep(t, td, 0.3), 50, box=AMB)


def b_pegadinha(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    kc = a * ep(t, tc, 0.3)
    recipiente(c, 330, 800, a * (0.35 + 0.65 * kc), t, 1.0, w=250, h=430, rot=L["de10"])
    recipiente(c, 720, 800, kc, t, 0.5, w=250, h=430, rot=L["deT"], rot_col=CYA)
    label(c, "≠", 525, 600, kc, 90, RED, "black")
    board(c, a)
    pos = eq(c, [(n_("99,95%") + " − " + n_("99,90%"), AMB), (" = ", WHITE), (n_("0,05%"), RED)], 330, a * ep(t, ta + 1.4, 0.3), 58)
    eq(c, [(n_("0,05%") + " × 10 L = ", WHITE), (n_("0,005") + " L", RED)], 480, a * ep(t, tb, 0.3), 58)
    popill(c, "A ?", RX, 610, 40, RED, BG0, a * ep(t, tb, 0.3), t, tb + 3.0)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 330, a, ep(t, tc, 0.4))
    cross(c, RX + 120, 610, 30, a * ep(t, tc + 0.3, 0.2))
    label(c, L["errado"], RX, 730, kc * ep(t, tc + 1.4, 0.3), 54, RED, "black")
    label(c, L["nao_sub"], RX, 830, a * ep(t, td, 0.3), 36, WHITE, "bold")


def b_naomuda(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_nao"], a)
    hl = ep(t, ta + 1.0, 0.4)
    recipiente(c, LX, 830, a, t, 1.0, hl_s2=hl)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:   # S1 saindo (setas para cima) e S2 parado
        for i in range(3):
            u = ((t - tb) * 0.7 + i / 3) % 1
            yy = 420 - 120 * u
            c.drawLine(LX - 80 + i * 80, yy + 40, LX - 80 + i * 80, yy, paint(CYA, kb * (1 - u), stroke=6, cap_round=True))
        label(c, L["sai_s1"], LX, 230, kb, 40, CYA, "black")
        label(c, "S2: " + L["nao_muda"], LX - 190, 790, kb, 34, AMB, "black", "right")
    board(c, a)
    label(c, L["so_s1"], RX, 270, kb, 40, WHITE, "black")
    eq(c, [("S2 = ", AMB), (n_("0,05%"), AMB), (" de 10 L" if not EN else " of 10 L", WHITE)], 420, a * ep(t, tc + 0.8, 0.3), 58)
    eq(c, [("= ", WHITE), (n_("0,0005"), AMB), (" × 10", WHITE)], 540, a * ep(t, tc + 3.6, 0.3), 58)
    eq(c, [("S2 = ", AMB), (n_("0,005") + " L", AMB)], 680, a * ep(t, tc + 6.0, 0.3), 72, box=AMB)
    label(c, L["colher"], RX, 820, a * ep(t, td, 0.3), 42, INK2, "bold")


def b_novototal(c, t, C, B):
    ta, tb, tc, td, te = (C[f"06.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_novo"], a)
    nv = 1 - 0.5 * ease_io(prog(t, te + 0.5, 1.6))
    recipiente(c, LX, 830, a, t, nv, hl_s2=ep(t, tb, 0.3) * (1 - ep(t, tc, 0.3)), rot="T = ?" if t < te + 2.0 else "T = 5 L",
               rot_col=CYA, marca5=ep(t, te + 2.0, 0.3))
    board(c, a)
    label(c, L["nova"], RX, 260, a * ep(t, ta + 1.0, 0.3), 42, WHITE, "black")
    eq(c, [("S2 = ", AMB), (n_("0,10%"), AMB), (" de " if not EN else " of ", WHITE), ("T", CYA), (" = ", WHITE), (n_("0,005") + " L", AMB)],
       370, a * ep(t, tb, 0.3), 54)
    eq(c, [(n_("0,001"), AMB), (" × ", WHITE), ("T", CYA), (" = ", WHITE), (n_("0,005"), AMB)], 490, a * ep(t, tc + 2.2, 0.3), 64)
    label(c, L["div"], RX, 590, a * ep(t, td, 0.3), 36, INK2, "bold")
    row(c, [P("T", CYA), P(" = "), F(n_("0,005"), n_("0,001"), AMB), P(" = "), F("5", "1", AMB)], 710,
        a * ep(t, td + 1.8, 0.3) * (1 - ep(t, te + 2.4, 0.2)), 60)
    row(c, [P("T", CYA), P(" = "), P("5 L", CYA)], 710, a * ep(t, te + 2.4, 0.3), 80, box=CYA)


def b_retirada(c, t, C, B):
    ta, tb, tc = (C[f"07.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ret"], a)
    recipiente(c, LX, 830, a, t, 0.5, fantasma=ep(t, ta + 1.0, 0.3), marca5=1, rot="10 L → 5 L")
    label(c, L["sairam"], LX, 250, a * ep(t, tb, 0.3), 46, CYA, "black")
    board(c, a)
    eq(c, [("10 L − 5 L = ", WHITE), ("5 L", MNT)], 300, a * ep(t, ta + 1.4, 0.3), 70, box=MNT)
    popill(c, L["metade"], RX, 430, 44, AMB, BG0, a, t, tb + 1.2)
    ops = [("A", n_("0,0050")), ("B", n_("0,0100")), ("C", n_("0,5000")), ("D", n_("4,9775")), ("E", n_("5,0000"))]
    kc = a * ep(t, tc, 0.3)
    for i, (le, v) in enumerate(ops):
        y = 540 + i * 74
        ok = le == "E"
        col = MNT if ok else (RED if le == "A" else INK2)
        k = kc * ep(t, tc + i * 0.08, 0.2)
        text_mid(c, le, RX - 160, y, 44, "black", col, k)
        text_mid(c, v, RX - 100, y, 44, "black", WHITE if ok else INK2, k, align="left")
        if ok:
            check(c, RX + 170, y, 26, kc * ep(t, tc + 0.6, 0.2))
        elif le == "A":
            cross(c, RX + 170, y, 22, kc * 0.8)


def b_porque(c, t, C, B):
    ta, tb, tc, td = (C[f"08.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_porque"], a)
    barra(c, 130, 300, 760, a, t, 0.05, L["antes"] + "  ·  S2 = " + n_("0,05%"), ux=560)
    barra(c, 130, 640, 380 + 380 * (1 - ep(t, tb + 2.0, 1.0)), a * ep(t, ta + 2.0, 0.3), t, 0.10,
          (L["depois"].replace("T L", "5 L")) + "  ·  S2 = " + n_("0,10%"), ux=560)
    board(c, a)
    eq(c, [(L["dobrou"], AMB)], 280, a * ep(t, ta + 2.0, 0.3), 50)
    eq(c, [(L["mesma"], WHITE)], 390, a * ep(t, tb, 0.3), 48)
    eq(c, [("10 L  →  ", WHITE), ("5 L", CYA)], 490, a * ep(t, tb + 2.2, 0.3), 58)
    label(c, L["confere"], RX, 600, a * ep(t, tc, 0.3), 36, INK2, "bold")
    eq(c, [("S1: ", CYA), (n_("9,995") + " − 5 = ", WHITE), (n_("4,995") + " L", MNT)], 680, a * ep(t, tc + 1.0, 0.3), 52)
    row(c, [F(n_("4,995"), "5", MNT), P(" = " + n_("0,999") + " = "), P(n_("99,90%"), MNT)], 810, a * ep(t, td, 0.3), 54, box=MNT)
    check(c, BX1 - 50, 810, 26, a * ep(t, td + 3.2, 0.2))


def b_batata(c, t, C, B):
    ta, tb, tc, td = (C[f"09.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_batata"], a)
    seca = ep(t, tb, 1.2)
    ka = a * (1 - ep(t, td, 0.3))
    batata(c, LX, 470, 420, ka, seca)
    label(c, "100 kg" if t < tc + 3 else "50 kg", LX, 750, ka, 60, AMB if t < tc + 3 else MNT, "black")
    # composição: água × seco
    wtot = 600
    x0 = LX - wtot / 2
    pseco = 0.01 + 0.01 * seca
    rrect(c, x0, 820, wtot * (1 - pseco), 40, 10, CYA, 0.6 * ka)
    rrect(c, x0 + wtot * (1 - pseco), 820, wtot * pseco + 6, 40, 6, AMB, ka)
    label(c, L["agua"] + "  " + ("99%" if seca < 0.5 else "98%"), x0, 900, ka, 30, CYA, "bold", "left")
    label(c, L["seco"] + "  " + ("1%" if seca < 0.5 else "2%"), x0 + wtot, 900, ka, 30, AMB, "bold", "right")
    kd = a * ep(t, td, 0.3)
    if kd > 0:
        recipiente(c, LX, 860, kd, t, 1.0, w=260, h=440, rot="")
        popill(c, L["desafio"], LX, 300, 40, AMB, BG0, kd, t, td + 1.0)
    board(c, a)
    eq(c, [(L["bat1"], AMB)], 280, a * ep(t, ta + 1.5, 0.3), 48)
    eq(c, [(L["bat2"], AMB)], 390, a * ep(t, tb, 0.3), 48)
    eq(c, [(L["peso"], CYA)], 490, a * ep(t, tb + 2.2, 0.3), 52)
    eq(c, [(L["seca"], WHITE)], 610, a * ep(t, tc, 0.3), 44)
    eq(c, [(L["bat3"] + " = ", WHITE), ("50 kg", MNT)], 730, a * ep(t, tc + 3.4, 0.3), 50, box=MNT)
    label(c, L["comenta"], RX, 850, a * ep(t, td + 5.0, 0.3), 40, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"10.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 280 + i * 160
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 400
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 54, "black", WHITE, ki, align="left")
        check(c, 1560, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula: grade de porcentagem · proporção · equação"""
    if i == 0:
        c.save(); c.translate(cx, cy); c.scale(0.4, 0.4); c.translate(-cx, -cy)
        grade100(c, cx, cy, a, t, n_hl=20, hl_a=1.0)
        c.restore()
    elif i == 1:
        row(c, [F(n_("0,05%"), "10 L", AMB), P(" → "), F(n_("0,10%"), "5 L", CYA)], cy, a, 50, cx=cx, maxw=380)
    else:
        row(c, [P(n_("0,001") + "·"), P("T", CYA), P(" = " + n_("0,005"))], cy, a, 46, cx=cx, maxw=380)


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
        if l1:
            text_mid(c, l1, cx, 610, 50, "black", WHITE, kk)
        text_mid(c, l2, cx, 674 if l1 else 640, 50, "black", cores[i], kk)
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
        recipiente(c, 960, 900, kg * 0.9 * ep(t, tf + 1.2, 0.4), t, 0.5, w=200, h=230, rot="", fantasma=1)


BLOCKS = dict(gancho=b_gancho, porcentagem=b_porcentagem, complemento=b_complemento, pegadinha=b_pegadinha,
              naomuda=b_naomuda, novototal=b_novototal, retirada=b_retirada, porque=b_porque, batata=b_batata,
              resumo=b_resumo, aulas=b_aulas)
