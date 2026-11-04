"""Visual — Estudativo · Questão de Matemática 028 (aula horizontal 1920x1080): ENEM 2025, questão 146, o cilindro de GNV
(proporção e arredondar para cima). Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = os dados do enunciado (30 km por dia, 1 m³ a cada 13 km, a sobra), ciano = o gás (cada m³) e
a ferramenta, menta = o cilindro certo e a conferência, coral = os cilindros que não dão conta.
Figuras: os cinco cilindros com altura proporcional à capacidade (cilindros()), a semana como uma faixa de 7 dias de 30 km
(semana()), os cubos de gás de 13 km (cubos()) e as vans de 12 lugares (van())."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_028_matematica_gnv_cilindro.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.e": "shimmer", "02.b": "data", "02.c": "data", "02.e": "lock", "03.b": "data", "03.c": "data", "03.e": "confirm",
        "04.b": "data", "04.c": "deny", "04.d": "alert", "05.c": "confirm", "06.c": "data", "06.d": "alert",
        "07.b": "deny", "07.c": "confirm", "07.d": "confirm", "08.a": "data", "08.b": "confirm", "08.c": "impact",
        "09.b": "deny", "09.c": "deny", "09.d": "alert", "10.b": "alert", "12.a": "shimmer", "12.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 028", "QUESTÃO DE MATEMÁTICA · 028"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_leit=("READING THE QUESTION", "TRADUZINDO O ENUNCIADO"),
    s_prop=("TOOL 1 · PROPORTION", "FERRAMENTA 1 · PROPORÇÃO"), s_arr=("TOOL 2 · ROUNDING UP", "FERRAMENTA 2 · ARREDONDAR PARA CIMA"),
    s_sem=("STEP 1 · KM PER WEEK", "PASSO 1 · QUILÔMETROS POR SEMANA"), s_gas=("STEP 2 · HOW MUCH GAS", "PASSO 2 · QUANTO GÁS"),
    s_esc=("STEP 3 · WHICH TANK", "PASSO 3 · QUAL CILINDRO"), s_resp=("THE ANSWER", "A RESPOSTA"),
    s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"), s_des=("CHALLENGE", "DESAFIO"),
    s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 146", "ENEM 2025 · questão 146"), gnv=("natural gas in the car (CNG)", "gás natural no carro (GNV)"),
    caps=("tanks: 10 · 14 · 17 · 21 · 25 m³", "cilindros: 10 · 14 · 17 · 21 · 25 m³"),
    preco=("price proportional to capacity", "preço proporcional à capacidade"),
    dia=("30 km a day · 7 days a week", "30 km por dia · 7 dias por semana"), cons=("1 m³ every 13 km", "1 m³ a cada 13 km"),
    pede=("cheapest one that lasts the week", "o mais barato que aguenta a semana"),
    t_prop=("proportion", "proporção"), t_arr=("rounding up", "arredondar para cima"),
    vol=("m³ = volume: how much gas fits", "m³ = volume: quanto gás cabe"), l_vol=("volume of gas", "volume de gás"),
    km13=("1 m³ of gas → 13 km", "1 m³ de gás → 13 km"), caro=("bigger tank = more expensive", "cilindro maior = mais caro"),
    l_caro=("more expensive", "mais caro"),
    menor=("cheapest = the SMALLEST that is enough", "mais barato = o MENOR que dá conta"),
    razao=("same ratio: ×2, ×3", "mesma razão: ×2, ×3"), div13=("gas = distance ÷ 13", "gás = distância ÷ 13"),
    vans=("50 students · vans with 12 seats", "50 alunos · vans de 12 lugares"), r50=("50 ÷ 12 = 4, remainder 2", "50 ÷ 12 = 4, resto 2"),
    v4=("4 vans: 2 left behind", "4 vans: 2 ficam para trás"), v5=("5 vans ✓", "5 vans ✓"), atras=("left behind", "ficam para trás"),
    sobe=("anything left over? go UP", "sobrou? sobe para o próximo"),
    dia_n=("day", "dia"), c30x7=("30 km × 7 days", "30 km × 7 dias"), c210=("30 × 7 = 210", "30 × 7 = 210"),
    km210=("210 km a week", "210 km por semana"),
    d210=("210 ÷ 13 = ?", "210 ÷ 13 = ?"), c208=("13 × 16 = 208", "13 × 16 = 208"), sob2=("2 km left over", "sobram 2 km"),
    c162=("≈ 16.2 m³", "≈ 16,2 m³"), mais16=("MORE than 16 m³", "MAIS de 16 m³"), l208=("16 m³ = 208 km", "16 m³ = 208 km"),
    l2km=("+ 2 km", "+ 2 km"), precisa=("needed: 16.2 m³", "precisa: 16,2 m³"),
    nao=("10 and 14 < 16.2 ✗", "10 e 14 < 16,2 ✗"), sim=("17, 21, 25 > 16.2 ✓", "17, 21, 25 > 16,2 ✓"),
    preco_up=("price grows with capacity", "o preço cresce com a capacidade"), barato=("cheapest", "mais barato"),
    c221=("17 × 13 = 221 km", "17 × 13 = 221 km"), folga=("221 − 210 = 11 km to spare", "221 − 210 = 11 km de folga"),
    l221=("17 m³ → 221 km", "17 m³ → 221 km"), l210=("week: 210 km", "semana: 210 km"), alt=("ANSWER", "ALTERNATIVA"),
    acaba=("out of gas", "acabou o gás"),
    pA=("10 m³ → 130 km: out on day 5", "10 m³ → 130 km: acaba no 5º dia"),
    pB=("14 m³ → 182 km: out on day 7", "14 m³ → 182 km: acaba no 7º dia"), pC=("17 m³ → 221 km ✓", "17 m³ → 221 km ✓"),
    pD=("21 m³: enough, but pricier", "21 m³: serve, mas é mais caro"), pE=("25 m³: enough, but pricier", "25 m³: serve, mas é mais caro"),
    des1=("what if the car drove", "e se o carro rodasse"), des2=("40 km a day?", "40 km por dia?"),
    des3=("which tank?", "qual cilindro?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["week distance = daily distance × 7", "gas = distance ÷ 13", "tank = the SMALLEST above the result"],
            ["distância da semana = a do dia × 7", "gás = distância ÷ 13", "cilindro = o MENOR acima do resultado"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Ratio and", "proportion"), ("The rule", "of three"), ("Division with", "remainder")],
           [("Razão e", "proporção"), ("Regra", "de três"), ("Divisão", "com resto")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("dezesseis vírgula dois", "16,2"), ("metros cúbicos", "m³"),
    ("metro cúbico", "m³"), ("quilômetros", "km"), ("regra de três", "regra de três")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
# aqui "mais" é "mais barato", "mais de 16", "mais ou menos": a legenda não troca "mais"/"menos" por + e −
_lingua0 = matematica._lingua
matematica._lingua = lambda lang: (lambda r: ([p for p in r[0] if p[0] not in ("mais", "menos", "plus", "minus")],) + r[1:])(
    _lingua0(lang))
CAPS = (10, 14, 17, 21, 25)
LETRAS = "ABCDE"
PRECISA = 210 / 13   # 16,15... m³


def n_(s):
    return s


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


def cilindro(c, cx, yb, cap, a, cor=WHITE, kh=24, w=110, nivel=1.0, rot=True, letra=None, k=1.0):
    """cilindro de gás em pé: altura ∝ capacidade (kh px por m³), base em yb; nivel = fração cheia de gás (ciano)"""
    if a <= 0 or k <= 0:
        return
    h = cap * kh
    c.save(); c.translate(cx, yb); c.scale(k, k)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h, w, h), w * 0.42, w * 0.42)
    c.drawRRect(r, paint(BG1, 0.95 * a))
    if nivel > 0:
        c.save(); c.clipRRect(r, True)
        c.drawRect(skia.Rect.MakeXYWH(-w / 2, -h * nivel, w, h * nivel), paint(cor, 0.32 * a))
        c.restore()
    c.drawRRect(r, paint(cor, a, stroke=4))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-14, -h - 22, 28, 24), 5, 5), paint(cor, a))   # válvula
    if rot:
        text_mid(c, f"{cap}", 0, -h / 2, 44 if w >= 100 else 32, "black", WHITE, a)
        text_mid(c, "m³", 0, -h / 2 + 40, 26, "extrabold", INK2, a)
    if letra:
        c.drawCircle(0, 40, 24, paint(cor, a))
        text_mid(c, letra, 0, 40, 28, "black", BG0, a)
    c.restore()


XC = (200, 360, 520, 680, 840)


def cilindros(c, a, t, t0=None, yb=820, kh=24, cores=None, dim=None, letras=False, nivel=1.0):
    for i, (cap, x) in enumerate(zip(CAPS, XC)):
        k = pop(t, t0 + i * 0.15, 0.35) if t0 is not None else 1.0
        cor = (cores or {}).get(cap, WHITE)
        al = a * (1 - 0.7 * (dim or {}).get(cap, 0.0))
        cilindro(c, x, yb, cap, al, cor, kh, nivel=nivel, letra=LETRAS[i] if letras else None, k=k)


def nivel_linha(c, y, a, rot=None, x0=110, x1=910, col=CYA):
    if a <= 0:
        return
    c.drawLine(x0, y, x0 + (x1 - x0) * ep(a, 0, 1), y, _dash(col, a, 4))
    if rot:
        label(c, rot, x0, y - 30, a, 32, col, "black", align="left")


def semana(c, x0, y, w, a, t, t0=None, km=None, cor=CYA, dias=7, rot=True, h=86):
    """a semana como faixa de 7 dias de 30 km; km = até onde o gás leva (preenche e marca o fim)"""
    if a <= 0:
        return
    cw = w / dias
    for i in range(dias):
        k = pop(t, t0 + i * 0.12, 0.3) if t0 is not None else 1.0
        if k <= 0:
            continue
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + i * cw + 3, y, cw - 6, h), 12, 12)
        c.drawRRect(r, paint(BG1, 0.95 * a * k))
        c.drawRRect(r, paint(INK2, 0.6 * a * k, stroke=2))
        if rot:
            text_mid(c, f"{L['dia_n']} {i + 1}", x0 + (i + 0.5) * cw, y - 26, 26, "extrabold", INK2, a * k)
            text_mid(c, "30 km", x0 + (i + 0.5) * cw, y + h / 2, 26, "black", WHITE, a * k)
    if km is not None and km > 0:
        ww = w * min(km, 210) / 210
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + 3, y + h + 12, max(ww - 6, 1), 22), 11, 11), paint(cor, a))


def cubo(c, x, y, s, a, cor=CYA, u=1.0, k=1.0, rot="1 m³"):
    """cubo de gás (1 m³ = 13 km): quadrado com a face de cima; u = fração cheia"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    d = s * 0.22
    top = skia.Path(); top.moveTo(-s / 2, -s / 2); top.lineTo(-s / 2 + d, -s / 2 - d); top.lineTo(s / 2 + d, -s / 2 - d)
    top.lineTo(s / 2, -s / 2); top.close()
    lado = skia.Path(); lado.moveTo(s / 2, -s / 2); lado.lineTo(s / 2 + d, -s / 2 - d); lado.lineTo(s / 2 + d, s / 2 - d)
    lado.lineTo(s / 2, s / 2); lado.close()
    face = skia.Rect.MakeXYWH(-s / 2, -s / 2, s, s)
    c.drawRect(face, paint(BG1, 0.95 * a))
    if u > 0:
        c.drawRect(skia.Rect.MakeXYWH(-s / 2, s / 2 - s * u, s, s * u), paint(cor, 0.55 * a))
        c.drawPath(lado, paint(cor, 0.3 * a)); c.drawPath(top, paint(cor, 0.45 * a if u >= 1 else 0.1 * a))
    for p in (top, lado):
        c.drawPath(p, paint(cor, a, stroke=3))
    c.drawRect(face, paint(cor, a, stroke=3))
    if rot:
        text_mid(c, rot, 0, 2, s * 0.26, "black", WHITE, a)
    c.restore()


def van(c, x, y, a, n, cor=WHITE, k=1.0, t=0, t0=None, alunos_cor=WHITE):
    """van de 12 lugares (4 × 3) com n alunos sentados"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    w, h = 230, 150
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 28, 28)
    c.drawRRect(r, paint(BG1, 0.95 * a))
    c.drawRRect(r, paint(cor, a, stroke=4))
    for wx in (-w / 2 + 48, w / 2 - 48):
        c.drawCircle(wx, h / 2 + 4, 20, paint(BG0, a)); c.drawCircle(wx, h / 2 + 4, 20, paint(cor, a, stroke=4))
    for j in range(12):
        sx, sy = -78 + (j % 4) * 52, -36 + (j // 4) * 36
        kk = pop(t, t0 + j * 0.05, 0.25) if t0 is not None else 1.0
        if j < n and kk > 0:
            c.drawCircle(sx, sy, 13 * kk, paint(alunos_cor, a))
        else:
            c.drawCircle(sx, sy, 13, paint(INK2, 0.35 * a, stroke=2))
    c.restore()


def carro(c, x, y, s, a, cor=CYA):
    """carrinho de perfil (a silhueta, sem detalhes), centrado em (x, y), comprimento s"""
    if a <= 0:
        return
    p = skia.Path()
    p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s / 2, y - s * 0.16, s, s * 0.24), s * 0.08, s * 0.08))
    p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s * 0.26, y - s * 0.34, s * 0.5, s * 0.22), s * 0.09, s * 0.09))
    c.drawPath(p, paint(cor, a))
    for wx in (x - s * 0.3, x + s * 0.3):
        c.drawCircle(wx, y + s * 0.09, s * 0.1, paint(BG0, a)); c.drawCircle(wx, y + s * 0.09, s * 0.1, paint(cor, a, stroke=4))


def estrada(c, x0, x1, y, a, km_max, marcas=(), cor=INK2, t=0, marcas_t=None):
    """estrada reta de x0 a x1 (0 a km_max km), com marcos de km"""
    if a <= 0:
        return
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, y - 22, x1, y + 22), 10, 10), paint(BG2, 0.95 * a))
    c.drawLine(x0 + 10, y, x1 - 10, y, _dash(cor, 0.6 * a, 3, 14))
    for j, km in enumerate(marcas):
        k = ep(t, marcas_t[j], 0.3) if marcas_t else 1.0
        x = x0 + (x1 - x0) * km / km_max
        c.drawLine(x, y - 34, x, y + 34, paint(AMB, a * k, stroke=4, cap_round=True))
        text_mid(c, f"{km} km", x, y + 66, 30, "black", AMB, a * k)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao.png"), a, w=820, cy=340, hmax=420)
    ke = ep(t, te, 0.4)
    kb = a * ep(t, tb + 0.3, 0.3) * (1 - ke)
    cilindros(c, kb, t, tb + 0.3, yb=880, kh=13)
    popill(c, L["t_prop"], LX - 200, 760, 40, CYA, BG0, a * ke, t, te + 1.4)
    popill(c, L["t_arr"], LX + 150, 760, 40, AMB, BG0, a * ke, t, te + 3.6)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 36, INK2, "extrabold")
    label(c, L["gnv"], RX, 310, a, 44, WHITE, "black")
    eq(c, [(L["caps"], AMB)], 420, a * ep(t, tb + 1.2, 0.3), 42)
    eq(c, [(L["preco"], WHITE)], 500, a * ep(t, tb + 6.4, 0.3), 38)
    eq(c, [(L["dia"], AMB)], 600, a * ep(t, tc + 0.6, 0.3), 40)
    eq(c, [(L["cons"], AMB)], 680, a * ep(t, tc + 5.1, 0.3), 42)
    eq(c, [(L["pede"], CYA)], 810, a * ep(t, td + 0.5, 0.3), 42, box=CYA)


def b_leitura(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_leit"], a)
    k1 = a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.3))   # o volume: quanto gás cabe
    if k1 > 0:
        cilindro(c, LX, 860, 17, k1, CYA, kh=36, w=200, nivel=ep(t, tb + 2.6, 1.2), rot=False)
        label(c, L["l_vol"], 790, 560, k1 * ep(t, tb + 2.6, 0.3), 36, CYA, "black")
    k2 = a * ep(t, tc, 0.3) * (1 - ep(t, td, 0.3))   # 1 m³ leva o carro 13 km
    if k2 > 0:
        cubo(c, 200, 520, 130, k2, CYA)
        estrada(c, 120, 920, 760, k2, 13, marcas=(13,))
        u = ep(t, tc + 3.6, 2.4)
        carro(c, 170 + 700 * u, 700, 150, k2, CYA)
        c.drawLine(280, 520, 520, 520, paint(CYA, k2 * ep(t, tc + 1.2, 0.3), stroke=5, cap_round=True))
        label(c, "13 km", 640, 520, k2 * ep(t, tc + 1.2, 0.3), 64, AMB, "black")
    k3 = a * ep(t, td, 0.3)   # maior = mais caro
    if k3 > 0:
        cilindros(c, k3, t, td, yb=860, kh=22, cores={17: MNT} if t >= te else None,
                  dim={x: ep(t, te + 1.3, 0.4) for x in (21, 25)})
        p = skia.Path(); p.moveTo(170, 520); p.lineTo(820, 170)
        ka = k3 * ep(t, td + 2.4, 0.4)
        c.drawPath(p, paint(AMB, ka, stroke=6, cap_round=True))
        c.drawLine(820, 170, 780, 168, paint(AMB, ka, stroke=6, cap_round=True))
        c.drawLine(820, 170, 805, 207, paint(AMB, ka, stroke=6, cap_round=True))
        label(c, L["l_caro"], 380, 300, ka, 40, AMB, "black")
    board(c, a)
    eq(c, [(L["vol"], WHITE)], 300, a * ep(t, tb, 0.3), 42)
    eq(c, [(L["km13"], AMB)], 450, a * ep(t, tc + 0.4, 0.3), 50)
    eq(c, [(L["caro"], WHITE)], 600, a * ep(t, td + 2.4, 0.3), 44)
    eq(c, [(L["menor"], CYA)], 770, a * ep(t, te + 0.4, 0.3), 40, box=CYA)


def b_proporcao(c, t, C, B):
    ta, tb, tc, td, te = (C[f"03.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_prop"], a)
    t13, t26, t39 = tb + 1.9, tb + 4.4, tc + 1.1
    x0, x1 = 110, 920
    estrada(c, x0, x1, 760, a * ep(t, tb, 0.3), 39, marcas=(13, 26, 39), t=t, marcas_t=(t13, t26, t39))
    sw = (x1 - x0) / 3
    for j, t0 in enumerate((t13, t26, t39)):   # cada m³ cobre 13 km da estrada
        cubo(c, x0 + sw * (j + 0.5), 560, 150, a, CYA, k=pop(t, t0, 0.4))
    u = (ep(t, t13 - 1.0, 1.0) + ep(t, t26 - 1.0, 1.0) + ep(t, t39 - 0.6, 0.8)) / 3
    carro(c, x0 + 40 + (x1 - x0 - 80) * u, 700, 120, a * ep(t, tb, 0.3), WHITE)
    board(c, a)
    for j, (s, t0) in enumerate((("1 m³ → 13 km", t13), ("2 m³ → 26 km", t26), ("3 m³ → 39 km", t39))):
        eq(c, [(s.split("→")[0], CYA), ("→", INK2), (s.split("→")[1], AMB)], 280 + j * 110, a * ep(t, t0, 0.3), 56)
    eq(c, [(L["razao"], WHITE)], 620, a * ep(t, td + 0.5, 0.3), 44)
    eq(c, [(L["div13"], CYA)], 780, a * ep(t, te + 3.0, 0.3), 54, box=CYA)


def b_arredondar(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_arr"], a)
    pos = ((220, 330), (520, 330), (820, 330), (370, 620), (670, 620))
    for i in range(4):
        van(c, *pos[i], a, 12, WHITE, pop(t, tb + 1.5 + i * 0.25, 0.35), t, tb + 2.9 + i * 0.6)
    t5 = tc + 3.4
    k5 = ep(t, t5, 0.3)
    van(c, *pos[4], a * k5, 2, MNT, pop(t, t5, 0.35), alunos_cor=MNT)
    kr = a * ep(t, tb + 5.4, 0.3) * (1 - k5)   # os 2 que sobram, ainda de fora
    if kr > 0:
        for j in range(2):
            c.drawCircle(pos[4][0] - 30 + j * 60, pos[4][1], 22, paint(RED, kr))
        label(c, L["atras"], pos[4][0], pos[4][1] + 70, kr * ep(t, tc, 0.3), 36, RED, "black")
    label(c, L["vans"], LX, 860, a * ep(t, tb, 0.3), 40, WHITE, "black")
    board(c, a)
    eq(c, [(L["r50"], WHITE)], 300, a * ep(t, tb + 4.4, 0.3), 50)
    eq(c, [(L["v4"], RED)], 440, a * ep(t, tc, 0.3), 48)
    eq(c, [(L["v5"], MNT)], 570, a * ep(t, t5, 0.3), 56)
    eq(c, [(L["sobe"], AMB)], 760, a * ep(t, td + 1.4, 0.3), 46, box=AMB)


def b_semana(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_sem"], a)
    carro(c, LX, 300, 220, a * ep(t, ta + 0.4, 0.3), CYA)
    semana(c, 110, 520, 810, a, t, tb + 1.0)
    kc = a * ep(t, tc, 0.3)
    if kc > 0:   # chave embaixo dos 7 dias
        p = skia.Path(); y = 640; m = LX
        p.moveTo(113, y); p.quadTo(113, y + 20, 135, y + 20); p.lineTo(m - 18, y + 20); p.quadTo(m, y + 20, m, y + 40)
        p.quadTo(m, y + 20, m + 18, y + 20); p.lineTo(895, y + 20); p.quadTo(917, y + 20, 917, y)
        c.drawPath(p, paint(CYA, kc, stroke=5))
        label(c, "210 km", LX, 720, kc, 64, CYA, "black")
    board(c, a)
    eq(c, [(L["c30x7"], AMB)], 340, a * ep(t, tb + 1.4, 0.3), 54)
    eq(c, [(L["c210"], WHITE)], 500, a * ep(t, tb + 2.8, 0.3), 60)
    eq(c, [(L["km210"], CYA)], 680, kc, 56, box=CYA)


POS_CUBO = [(LX - 300 + (i % 6) * 120, 300 + (i // 6) * 150) for i in range(17)]


def b_gas(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gas"], a)
    for i in range(16):   # 16 m³ cheios = 208 km
        x, y = POS_CUBO[i]
        cubo(c, x, y, 92, a, CYA, k=pop(t, tc + 0.4 + i * 0.09, 0.3), rot=None)
    x, y = POS_CUBO[16]
    t17 = tc + 2.8
    u17 = 2 / 13
    k17 = ep(t, td + 2.8, 0.4)
    cubo(c, x, y, 92, a * ep(t, t17, 0.3), _mix_cor(AMB, CYA, k17), u=u17, k=pop(t, t17, 0.35), rot=None)
    if k17 > 0:
        c.drawRect(skia.Rect.MakeXYWH(x - 56, y - 66, 132, 122), _dash(CYA, a * k17, 3, 8))
    label(c, L["l208"], LX - 60, 760, a * ep(t, tc + 1.6, 0.3), 44, CYA, "black")
    label(c, L["l2km"], x, y + 90, a * ep(t, t17, 0.3), 36, AMB, "black")
    board(c, a)
    eq(c, [(L["d210"], WHITE)], 280, a * ep(t, tb, 0.3), 58)
    eq(c, [(L["c208"], CYA)], 400, a * ep(t, tc + 0.4, 0.3), 54)
    eq(c, [(L["sob2"], AMB)], 510, a * ep(t, t17, 0.3), 50)
    eq(c, [(L["c162"], WHITE)], 630, a * ep(t, td, 0.3), 58)
    eq(c, [(L["mais16"], CYA)], 790, a * ep(t, td + 5.2, 0.3), 56, box=CYA)


def _mix_cor(h1, h2, u):
    u = clamp(u)
    p = [int(h1[i:i + 2], 16) for i in (1, 3, 5)]
    q = [int(h2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(x + (y - x) * u):02X}" for x, y in zip(p, q))


YB, KH = 830, 24


def b_escolha(c, t, C, B):
    ta, tb, tc, td = (C[f"07.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_esc"], a)
    cores, dim = {}, {}
    if t >= tb + 0.2:
        cores[10] = cores[14] = RED
    for cap, t0 in ((17, tc + 0.3), (21, tc + 1.4), (25, tc + 2.4)):
        if t >= t0:
            cores[cap] = MNT
    kd = ep(t, td + 3.9, 0.4)
    for cap in (10, 14, 21, 25):
        dim[cap] = 0.6 * kd
    cilindros(c, a, t, ta + 0.2, yb=YB, kh=KH, cores=cores, dim=dim, letras=True)
    nivel_linha(c, YB - PRECISA * KH, a * ep(t, ta + 1.4, 0.6), n_(L["c162"][2:]), x0=100, x1=920)
    for cap, x in zip(CAPS, XC):
        top = YB - cap * KH - 75
        if cap in (10, 14):
            cross(c, x, top, 24, a * ep(t, tb + 0.4 + (cap == 14) * 0.5, 0.3) * (1 - 0.6 * kd))
        elif t >= tc:
            check(c, x, top, 24, a * ep(t, {17: tc + 0.3, 21: tc + 1.4, 25: tc + 2.4}[cap], 0.3) * (1 - 0.6 * dim.get(cap, 0)))
    popill(c, L["barato"], XC[2], YB - 17 * KH - 130, 30, MNT, BG0, a * kd, t, td + 3.9)
    board(c, a)
    eq(c, [(L["nao"], RED)], 320, a * ep(t, tb + 0.4, 0.3), 54)
    eq(c, [(L["sim"], MNT)], 470, a * ep(t, tc + 2.6, 0.3), 54)
    eq(c, [(L["preco_up"], WHITE)], 620, a * ep(t, td + 0.4, 0.3), 42)
    eq(c, [("17 m³", MNT)], 780, a * ep(t, td + 3.9, 0.3), 72, box=MNT)


def b_resposta(c, t, C, B):
    ta, tb, tc = (C[f"08.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    cilindro(c, 190, 820, 17, a, MNT, kh=26, w=130, letra=None)
    x0, pk = 330, 2.3   # px por km
    ka = a * ep(t, ta + 4.3, 0.4)
    kb = a * ep(t, tb, 0.4)
    for y, km, cor, rot, k in ((420, 221, MNT, L["l221"], ka), (620, 210, AMB, L["l210"], kb)):
        if k <= 0:
            continue
        w = km * pk * ep(t, ta + 4.3 if km == 221 else tb, 0.8)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y - 36, w, 72), 16, 16), paint(cor, 0.85 * k))
        label(c, rot, x0, y - 70, k, 36, cor, "black", align="left")
    kf = a * ep(t, tb + 1.6, 0.3)
    if kf > 0:
        xa, xb = x0 + 210 * pk, x0 + 221 * pk
        c.drawLine(xa, 360, xa, 680, _dash(WHITE, kf, 3, 8))
        label(c, "11 km", xa - 20, 760, kf, 40, MNT, "black", align="right")
        c.drawLine(xa, 720, xb, 720, paint(MNT, kf, stroke=5, cap_round=True))
    board(c, a)
    eq(c, [(L["c221"], MNT)], 300, a * ep(t, ta + 3.6, 0.3), 56)
    eq(c, [(L["folga"], WHITE)], 440, kb * ep(t, tb + 1.6, 0.3), 44)
    kc = a * ep(t, tc, 0.3)
    if kc > 0:
        for j, (le, cap) in enumerate(zip(LETRAS, CAPS)):
            x = BX0 + 130 + j * 160
            ok = le == "C"
            c.drawCircle(x, 600, 34, paint(MNT if ok else INK2, kc))
            text_mid(c, le, x, 600, 36, "black", BG0, kc)
            text_mid(c, f"{cap}", x, 670, 40, "black", MNT if ok else WHITE, kc)
        check(c, BX0 + 130 + 2 * 160 + 38, 570, 18, kc)
        eq(c, [(L["alt"] + " ", WHITE), ("C", MNT)], 800, kc, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td = (C[f"09.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    for y, cap, km, t0, tfim, le in ((330, 14, 182, tb, tb + 5.6, "B"), (640, 10, 130, tc, tc + 2.8, "A")):
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        semana(c, 190, y, 740, k, t, None, km=km * ep(t, t0 + 0.6, 1.4), cor=CYA, h=74)
        cilindro(c, 105, y + 80, cap, k, RED, kh=11, w=70, rot=False)
        c.drawCircle(105, y + 118, 22, paint(RED, k))
        text_mid(c, le, 105, y + 118, 26, "black", BG0, k)
        kf = k * ep(t, tfim, 0.3)
        if kf > 0:
            xf = 190 + 740 * km / 210
            c.drawLine(xf, y - 10, xf, y + 116, paint(RED, kf, stroke=6, cap_round=True))
            popill(c, L["acaba"], min(xf, 800), y + 160, 28, RED, BG0, kf, t, tfim)
    board(c, a)
    linhas = (("A", L["pA"], RED, tc + 2.8), ("B", L["pB"], RED, tb + 5.6), ("C", L["pC"], MNT, ta + 0.4),
              ("D", L["pD"], AMB, td + 1.0), ("E", L["pE"], AMB, td + 1.0))
    for j, (le, s, cor, t0) in enumerate(linhas):
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        y = 270 + j * 140
        c.drawCircle(BX0 + 70, y, 32, paint(cor, k))
        text_mid(c, le, BX0 + 70, y, 34, "black", BG0, k)
        sz = 38
        while text_w(s, "black", sz) > 700:
            sz -= 2
        text_mid(c, s, BX0 + 125, y, sz, "black", WHITE, k, align="left")


def b_desafio(c, t, C, B):
    ta, tb, tc = (C[f"10.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    cilindros(c, a, t, ta + 0.2, yb=820, kh=22, letras=True)
    board(c, a)
    label(c, L["des1"], RX, 320, a * ep(t, tb, 0.3), 44, WHITE, "black")
    eq(c, [(L["des2"], AMB)], 440, a * ep(t, tb + 0.9, 0.3), 64, box=AMB)
    label(c, L["des3"], RX, 600, a * ep(t, tb + 3.0, 0.3), 50, CYA, "black")
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
    """miniatura de cada aula: 1 : 13 · a tabela da regra de três · 50 ÷ 12"""
    if i == 0:
        text_mid(c, "1 : 13", cx, cy, 90, "black", CYA, a)
    elif i == 1:
        for j, (p, q) in enumerate((("1", "13"), ("x", "210"))):
            text_mid(c, p, cx - 70, cy - 36 + j * 72, 50, "black", AMB if j == 0 else CYA, a)
            text_mid(c, "→", cx, cy - 36 + j * 72, 44, "black", INK2, a)
            text_mid(c, q, cx + 80, cy - 36 + j * 72, 50, "black", WHITE, a)
    else:
        text_mid(c, "50 ÷ 12", cx, cy - 20, 64, "black", WHITE, a)
        text_mid(c, "4 r 2" if EN else "4 resto 2", cx, cy + 44, 36, "black", MNT, a)


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


BLOCKS = dict(gancho=b_gancho, leitura=b_leitura, proporcao=b_proporcao, arredondar=b_arredondar, semana=b_semana,
              gas=b_gas, escolha=b_escolha, resposta=b_resposta, pegadinhas=b_pegadinhas, desafio=b_desafio,
              resumo=b_resumo, aulas=b_aulas)
