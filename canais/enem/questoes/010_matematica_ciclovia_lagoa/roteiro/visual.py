"""Visual — Estudativo · Questão de Matemática 010 (aula horizontal 1920x1080): ENEM 2025, questão 136, a ciclovia da lagoa.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = dado do problema (1 km, 200 m, π ≈ 3, ponto P), ciano = incógnita (quantos policiais) e o
trecho que um policial protege, menta = resultado conferido / trechos alternados, coral = a pegadinha e o trecho sem proteção.
A ciclovia é o anel em volta da lagoa; "desenrolar" vira a volta numa linha reta do mesmo comprimento (curva()).
Ângulos na lagoa: 0 = topo, sentido horário. 200 m de 6.000 m = 12°."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_010_matematica_ciclovia_lagoa.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.e": "shimmer", "02.c": "shimmer", "02.d": "confirm", "02.e": "confirm", "03.b": "confirm",
        "04.b": "impact", "05.c": "confirm", "05.d": "alert", "06.b": "impact", "06.d": "confirm", "07.c": "deny",
        "07.d": "confirm", "08.c": "confirm", "08.d": "lock", "10.a": "shimmer", "10.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.20, lufs=-14, bpm=100, sfx=_SFX)

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 010", "QUESTÃO DE MATEMÁTICA · 010"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_circ=("THE TOOL · CIRCUMFERENCE", "A FERRAMENTA · COMPRIMENTO DA CIRCUNFERÊNCIA"),
    s_unid=("STEP 1 · SAME UNIT", "PASSO 1 · A MESMA UNIDADE"), s_volta=("STEP 2 · THE LENGTH OF THE PATH", "PASSO 2 · O TAMANHO DA CICLOVIA"),
    s_cob=("THE KEY IDEA · HOW MUCH ONE OFFICER COVERS", "A IDEIA · QUANTO UM POLICIAL PROTEGE"),
    s_div=("STEP 3 · SPLIT THE LOOP", "PASSO 3 · DIVIDIR A VOLTA"), s_min=("WHY NOT FEWER?", "POR QUE NÃO MENOS?"),
    s_gen=("WHAT IF IT DOESN'T DIVIDE EXACTLY?", "E SE A DIVISÃO NÃO FOR EXATA?"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 136", "ENEM 2025 · questão 136"),
    lagoa=("circular lake: r = ", "lagoa circular: r = "), prot=("protected: officer ≤ 200 m away", "protegido: policial a ≤ 200 m"),
    minimo=("minimum number of officers = ", "mínimo de policiais = "),
    p_circ=("CIRCUMFERENCE", "COMPRIMENTO DA CIRCUNFERÊNCIA"), p_cob=("HOW MUCH EACH ONE COVERS", "QUANTO CADA UM PROTEGE"),
    volta=("C = the whole way around", "C = a volta inteira"), raio=("radius", "raio"), diam=("diameter", "diâmetro"),
    sempre=("in ANY circle:", "em QUALQUER círculo:"), mais3=("a bit more than 3", "um pouco mais que 3"),
    roda=("wheel: r = 30 cm,  π = 3", "roda: r = 30 cm,  π = 3"),
    raio_prot=("radius: 1 km  ·  protection: 200 m", "raio: 1 km  ·  proteção: 200 m"),
    ciclo=("bike path = the lake's circumference", "ciclovia = volta da lagoa"), largura=("(ignore the lane width)", "(sem a largura da pista)"),
    esticada=("stretched out: 6 km", "esticada: 6 km"),
    pergunta=("1 officer protects how much?", "1 policial protege quanto?"),
    p_prot=("P is protected if an officer is ≤ 200 m away", "P protegido: policial a ≤ 200 m de P"),
    inverte=("turn it around: 1 officer protects", "invertendo: 1 policial protege"),
    frente=("ahead", "à frente"), atras=("behind", "atrás"),
    errado=("forgot one side!", "esqueceu um lado!"), dobro=("each officer covers TWICE that", "cada policial protege o DOBRO"),
    trechos=("loop ÷ 400 m stretches", "volta ÷ trechos de 400 m"), corta=("drop two zeros", "corta dois zeros"),
    no_meio=("one officer in the middle of each stretch", "um policial no meio de cada trecho"),
    policiais=("officers", "policiais"),
    com14=("what about 14?", "e com 14?"), sem=("400 m UNPROTECTED", "400 m SEM PROTEÇÃO"),
    sem_curto=("unprotected", "sem proteção"),
    r11=("radius 1.1 km = 1,100 m", "raio 1,1 km = 1.100 m"), meio=("there's no half an officer", "não existe meio policial"),
    com16=("16 → a piece is left uncovered", "16 → sobra um pedaço sem proteção"),
    cima=("round UP: ", "arredonda para CIMA: "),
    desafio=("r = 2 km  ·  250 m each side?", "r = 2 km  ·  250 m para cada lado?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["1 km = 1,000 m", "C = 2 · 3 · 1,000 = 6,000 m", "1 officer: 200 + 200 = 400 m", "6,000 ÷ 400 = 15  (C)"],
            ["1 km = 1.000 m", "C = 2 · 3 · 1.000 = 6.000 m", "1 policial: 200 + 200 = 400 m", "6.000 ÷ 400 = 15  (C)"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("", "Circumference"), ("Units and", "conversions"), ("", "Divisibility")],
           [("Comprimento da", "circunferência"), ("Unidades e", "conversões"), ("", "Divisibilidade")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("um vírgula um quilômetro", "1,1 km"), ("um quilômetro", "1 km"),
    ("dois quilômetros", "2 km"), ("seis quilômetros", "6 km"), ("seis mil e seiscentos metros", "6.600 m"),
    ("cinco mil e seiscentos metros", "5.600 m"), ("seis mil metros", "6.000 m"), ("mil metros", "1.000 m"),
    ("seis mil", "6.000"), ("mil e cem", "1.100"), ("mil", "1.000"),
    ("duzentos e cinquenta metros", "250 m"), ("quatrocentos metros", "400 m"), ("duzentos metros", "200 m"),
    ("trinta centímetros", "30 cm"), ("cento e oitenta centímetros", "180 cm"), ("três vírgula um quatro", "3,14"),
    ("dezesseis vírgula cinco", "16,5"), ("dividido por", "÷"), ("dois vezes", "2 ×"), ("dois", "2"), ("pi", "π")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
n_ = lambda s: s.replace(".", "#").replace(",", ".").replace("#", ",") if EN else s   # noqa: E731  troca , e . no inglês


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- figuras
AGUA = ("#4CC9F0", "#1F6F99")
PISTA = "#D7E0EE"
GRAU = math.pi / 180


def pt(cx, cy, R, ang):
    """ponto na circunferência; ang em radianos, 0 = topo, sentido horário"""
    return cx + R * math.sin(ang), cy - R * math.cos(ang)


def lagoa(c, cx, cy, R, a, t, agua=1.0, pista=1.0):
    """lagoa (água em ciano) com a ciclovia (anel claro com faixa tracejada)"""
    if a <= 0:
        return
    if agua > 0:
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial((cx - R * 0.3, cy - R * 0.35), R * 1.4, [hexc(AGUA[0]), hexc(AGUA[1])]))
        p.setAlphaf(0.55 * a * agua)
        c.drawCircle(cx, cy, R * 0.955, p)
        for i in range(3):   # marolas
            yy = cy - R * 0.3 + i * R * 0.3
            w = R * (0.5 - 0.1 * abs(i - 1))
            ph = math.sin(t * 1.2 + i * 2)
            pth = skia.Path(); pth.moveTo(cx - w + ph * 10, yy)
            pth.quadTo(cx - w / 2 + ph * 10, yy - 10, cx + ph * 10, yy); pth.quadTo(cx + w / 2 + ph * 10, yy + 10, cx + w + ph * 10, yy)
            c.drawPath(pth, paint(WHITE, 0.16 * a * agua, stroke=3, cap_round=True))
    if pista > 0:
        sw = max(14, R * 0.075)
        c.drawCircle(cx, cy, R, blur_paint(PISTA, 0.18 * a * pista, 10, stroke=sw + 8))
        c.drawCircle(cx, cy, R, paint(PISTA, 0.9 * a * pista, stroke=sw))
        pd = paint(BG1, 0.55 * a * pista, stroke=2.5)
        pd.setPathEffect(skia.DashPathEffect.Make([14, 12], 0))
        c.drawCircle(cx, cy, R, pd)


def arco(c, cx, cy, R, a0, a1, col, a, w=22, glow=True):
    """trecho da ciclovia de a0 a a1 (rad, 0 = topo, horário)"""
    if a <= 0 or a1 <= a0:
        return
    rect = skia.Rect.MakeLTRB(cx - R, cy - R, cx + R, cy + R)
    pth = skia.Path(); pth.addArc(rect, a0 / GRAU - 90, (a1 - a0) / GRAU)
    if glow:
        c.drawPath(pth, blur_paint(col, 0.45 * a, 12, stroke=w + 10))
    p = paint(col, a, stroke=w)
    c.drawPath(pth, p)


def policial(c, x, y, s, a, col=CYA, k=1.0):
    """marcador do policial: alfinete com bonequinho"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    pth = skia.Path()   # alfinete: círculo com ponta para baixo
    pth.addCircle(0, -s * 1.25, s)
    tri_ = skia.Path(); tri_.moveTo(-s * 0.62, -s * 0.5); tri_.lineTo(0, 0); tri_.lineTo(s * 0.62, -s * 0.5); tri_.close()
    pth = skia.Op(pth, tri_, skia.kUnion_PathOp)
    c.drawPath(pth, blur_paint(col, 0.4 * a, 8))
    c.drawPath(pth, paint(col, a))
    c.drawPath(pth, paint(WHITE, a, stroke=max(2, s * 0.12)))
    c.drawCircle(0, -s * 1.5, s * 0.24, paint(BG0, a))                      # cabeça
    body = skia.Path(); body.addArc(skia.Rect.MakeXYWH(-s * 0.45, -s * 1.22, s * 0.9, s * 0.8), 180, 180)
    c.drawPath(body, paint(BG0, a))                                          # ombros
    c.restore()


def policial_na_pista(c, cx, cy, R, ang, s, a, col=CYA, k=1.0):
    x, y = pt(cx, cy, R, ang)
    policial(c, x, y, s, a, col, k)


def ponto_p(c, cx, cy, R, ang, a, t):
    x, y = pt(cx, cy, R, ang)
    pul = 0.5 + 0.5 * math.sin(t * 5)
    c.drawCircle(x, y, 22, blur_paint(AMB, (0.35 + 0.3 * pul) * a, 10))
    c.drawCircle(x, y, 11, paint(AMB, a))
    c.drawCircle(x, y, 11, paint(BG0, a, stroke=3))
    lx, ly = pt(cx, cy, R - 60, ang)
    label(c, "P", lx, ly, a, 44, AMB, "black")


def cota_arco(c, cx, cy, R, a0, a1, s, a, col=AMB, off=58, size=32):
    """rótulo de um trecho, por fora do anel, no meio do arco"""
    if a <= 0:
        return
    m = (a0 + a1) / 2
    x, y = pt(cx, cy, R + off, m)
    label(c, s, x, y, a, size, col, "black")


def curva(cx, base, R, u):
    """'desenrola' a circunferência de raio R: devolve f(s) → (x, y), s ∈ [−L/2, L/2] medido a partir do ponto de baixo.
    u = 0: círculo com o ponto de baixo em (cx, base); u = 1: segmento horizontal de comprimento L = 2πR."""
    u = clamp(u)
    if u > 0.999:
        return lambda s: (cx + s, base)
    rho = R / (1 - u)

    def f(s):
        ph = s / rho
        return cx + rho * math.sin(ph), base - rho * (1 - math.cos(ph))
    return f


def tracar(c, f, s0, s1, col, a, w, n=None, glow=False):
    if a <= 0 or s1 <= s0:
        return
    n = n or max(8, int((s1 - s0) / 6))
    pth = skia.Path()
    pth.moveTo(*f(s0))
    for i in range(1, n + 1):
        pth.lineTo(*f(s0 + (s1 - s0) * i / n))
    if glow:
        c.drawPath(pth, blur_paint(col, 0.4 * a, 10, stroke=w + 10))
    p = paint(col, a, stroke=w)
    p.setStrokeCap(skia.Paint.kRound_Cap)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(pth, p)


def _card_enunciado(c, a):
    img = _img_enunciado()
    h = 830
    w = img.width() * h / img.height()
    x, y = LX - w / 2, 545 - h / 2
    rrect(c, x - 18, y - 18, w + 36, h + 36, 22, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


@lru_cache(None)
def _img_enunciado():
    from pathlib import Path
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / "questao.png"))


# ---------------------------------------------------------------- cenas
LC = (500, 525)    # centro da lagoa nas cenas com a figura grande
RL = 300           # raio da lagoa (px) nessas cenas
D12 = 12 * GRAU    # 200 m de 6.000 m


def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    eq(c, [(L["lagoa"], WHITE), ("1 km", AMB)], 360, a, 54)
    eq(c, [(L["prot"].split("200")[0], WHITE), ("200 m", AMB)], 470, a * ep(t, tc, 0.3), 46)
    eq(c, [("π ≈ ", WHITE), ("3", AMB)], 570, a * ep(t, td, 0.3), 54)
    eq(c, [(L["minimo"], WHITE), ("?", CYA)], 690, a * ep(t, te, 0.3), 56, box=CYA)
    ke = a * ep(t, te + 2.0, 0.3)
    popill(c, L["p_circ"], RX, 800, 28, CYA, BG0, ke, t, te + 4.2)
    popill(c, L["p_cob"], RX, 868, 28, AMB, BG0, ke, t, te + 6.8)


def b_circunferencia(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_circ"], a)
    R, cx, base = 120, LX, 690
    cy = base - R
    # desenrola duas vezes: na definição (ta) e na prova do π (tc); volta a ser círculo entre elas
    u = ease_io(prog(t, ta + 3.2, 1.6)) * (1 - ease_io(prog(t, tb - 0.2, 1.0))) + ease_io(prog(t, tc + 1.0, 1.6))
    Lc = 2 * math.pi * R
    f = curva(cx, base, R, u)
    c.drawCircle(cx, cy, R * 0.97, paint(BG2, 0.6 * a * (1 - u)))
    tracar(c, f, -Lc / 2, Lc / 2, CYA, a, 8, n=160, glow=True)
    # raio e diâmetro (somem enquanto desenrola)
    kr = a * ep(t, tb + 0.6, 0.3) * (1 - ep(t, tc + 0.8, 0.2))
    if kr > 0:
        c.drawCircle(cx, cy, 7, paint(WHITE, kr))
        c.drawLine(cx, cy, cx + R * 0.71, cy - R * 0.71, paint(AMB, kr, stroke=6, cap_round=True))
        label(c, "r", cx + R * 0.28, cy - R * 0.5, kr, 40, AMB, "black")
        kd = kr * ep(t, tb + 2.6, 0.3)
        c.drawLine(cx - R, cy, cx + R, cy, paint(MNT, kd, stroke=6, cap_round=True))
        label(c, "d", cx - R * 0.45, cy + 32, kd, 40, MNT, "black")
        label(c, L["raio"] + " · " + L["diam"], cx, cy - R - 60, kr, 32, INK2, "bold")
    # prova do π: 3 diâmetros cabem na volta e sobra um pedacinho
    kp = a * ep(t, tc + 2.8, 0.3)
    if kp > 0 and u > 0.99:
        x0 = cx - Lc / 2
        for i in range(3):
            k = ep(t, tc + 2.8 + i * 0.5, 0.3)
            rrect(c, x0 + i * 2 * R + 3, base + 26, 2 * R - 6, 22, 8, MNT, kp * k)
            label(c, "d", x0 + i * 2 * R + R, base + 80, kp * k, 36, MNT, "black")
        k4 = kp * ep(t, tc + 4.6, 0.3)
        rrect(c, x0 + 6 * R + 3, base + 26, Lc - 6 * R - 6, 22, 6, AMB, k4)
        label(c, n_("0,14…"), x0 + 6 * R + (Lc - 6 * R) / 2 + 14, base + 80, k4, 28, AMB, "black")
        label(c, "C", cx, base - 46, kp, 44, CYA, "black")
        label(c, L["mais3"], cx, base + 150, k4, 34, INK2, "bold")
    board(c, a)
    label(c, L["volta"], RX, 270, a * ep(t, ta + 0.8, 0.3), 46, WHITE, "black")
    eq(c, [("d", MNT), (" = 2 · ", WHITE), ("r", AMB)], 380, a * ep(t, tb + 3.6, 0.3), 58)
    label(c, L["sempre"], RX, 480, a * ep(t, tc, 0.3), 36, INK2, "bold")
    eq(c, [("C", CYA), (" ÷ ", WHITE), ("d", MNT), (" = π ≈ " + n_("3,14…"), WHITE)], 560, a * ep(t, tc + 4.0, 0.3), 56)
    eq(c, [("C", CYA), (" = 2 · π · ", WHITE), ("r", AMB)], 690, a * ep(t, td + 1.6, 0.3), 70, box=CYA)
    ke = a * ep(t, te, 0.3)
    label(c, L["roda"], RX, 800, ke, 34, AMB, "bold")
    eq(c, [("C = 2 · 3 · 30 = ", WHITE), ("180 cm", MNT)], 862, a * ep(t, te + 2.4, 0.3), 46)


def b_unidades(c, t, C, B):
    ta, tb = (C[f"03.{k}"] for k in "ab")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_unid"], a)
    cx, cy = LC
    lagoa(c, cx, cy, RL, a, t)
    c.drawCircle(cx, cy, 8, paint(WHITE, a))
    x1, y1 = pt(cx, cy, RL, 90 * GRAU)
    c.drawLine(cx, cy, x1 - 12, y1, paint(AMB, a, stroke=6, cap_round=True))
    k = ep(t, tb + 0.4, 0.4)
    label(c, "r = 1 km", cx + RL / 2, cy - 40, a * (1 - k), 44, AMB, "black")
    label(c, "r = " + n_("1.000") + " m", cx + RL / 2, cy - 40, a * k, 44, AMB, "black")
    board(c, a)
    label(c, L["raio_prot"], RX, 300, a * ep(t, ta + 1.2, 0.3), 40, WHITE, "black")
    eq(c, [("1 km", AMB), (" = ", WHITE), (n_("1.000") + " m", AMB)], 480, a * ep(t, tb, 0.3), 72, box=AMB)
    eq(c, [("r = ", WHITE), (n_("1.000") + " m", AMB)], 660, a * ep(t, tb + 1.6, 0.3), 64)


def b_volta(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_volta"], a)
    # lagoa grande → encolhe → desenrola numa reta de 6 km
    enc = ease_io(prog(t, tc - 1.4, 1.2))
    R = RL + (125 - RL) * enc
    cx, cy = LX, LC[1] + (690 - 125 - LC[1]) * enc
    u = ease_io(prog(t, tc, 1.8))
    lagoa(c, cx, cy, R, a * (1 - u), t, pista=0)
    Lc = 2 * math.pi * R
    f = curva(cx, cy + R, R, u)
    tracar(c, f, -Lc / 2, Lc / 2, PISTA, a, max(14, R * 0.075) * (1 - u) + 16 * u, n=160)
    kk = a * ep(t, tc + 1.9, 0.4)
    if kk > 0:   # régua em km
        x0 = cx - Lc / 2
        for i in range(7):
            x = x0 + Lc * i / 6
            c.drawLine(x, cy + R + 20, x, cy + R + 44, paint(WHITE, kk, stroke=3))
            label(c, str(i), x, cy + R + 72, kk, 30, INK2, "bold")
        label(c, "km", x0 + Lc + 40, cy + R + 72, kk, 30, INK2, "bold")
        label(c, n_("6.000") + " m", cx, cy + R - 60, kk, 54, CYA, "black")
    board(c, a)
    label(c, L["ciclo"], RX, 270, a * ep(t, ta + 0.8, 0.3), 42, WHITE, "black")
    label(c, L["largura"], RX, 330, a * ep(t, ta + 3.0, 0.3), 32, INK2, "bold")
    eq(c, [("C = 2 · π · ", WHITE), ("r", AMB)], 450, a * ep(t, tb, 0.3), 60)
    eq(c, [("C = 2 · ", WHITE), ("3", AMB), (" · ", WHITE), (n_("1.000"), AMB)], 570, a * ep(t, tb + 2.0, 0.3), 60)
    eq(c, [("C = ", WHITE), (n_("6.000") + " m", CYA)], 700, a * ep(t, tb + 4.0, 0.3), 76, box=CYA)
    label(c, L["esticada"], RX, 830, a * ep(t, tc + 1.2, 0.3), 40, INK2, "bold")


def b_cobertura(c, t, C, B):
    ta, tb, tc, td = (C[f"05.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_cob"], a)
    cx, cy = LC
    ang = 45 * GRAU   # como na figura do enunciado: P no alto, à direita
    D12 = 24 * GRAU   # fora de escala, como na figura do enunciado (na escala real, 200 m = 12°)
    lagoa(c, cx, cy, RL, a, t)
    kb = a * ep(t, tb, 0.4) * (1 - ep(t, tc, 0.3))
    arco(c, cx, cy, RL, ang - D12, ang + D12, "#7C8799", kb, 26, glow=False)
    cota_arco(c, cx, cy, RL, ang - D12, ang, "200 m", kb, AMB, 64, 28)
    cota_arco(c, cx, cy, RL, ang, ang + D12, "200 m", kb, AMB, 64, 28)
    if t < tc:
        ponto_p(c, cx, cy, RL, ang, a * ep(t, tb, 0.3), t)
    kc = a * ep(t, tc, 0.4)
    if kc > 0:
        arco(c, cx, cy, RL, ang - D12 * ep(t, tc + 0.3, 0.8), ang + D12 * ep(t, tc + 0.3, 0.8), CYA, kc, 26)
        policial_na_pista(c, cx, cy, RL, ang, 26, kc, CYA, pop(t, tc, 0.4))
        cota_arco(c, cx, cy, RL, ang - D12, ang, L["atras"], kc * ep(t, tc + 2.4, 0.3), CYA, 70, 28)
        cota_arco(c, cx, cy, RL, ang, ang + D12, L["frente"], kc * ep(t, tc + 1.4, 0.3), CYA, 70, 28)
        label(c, "400 m", cx, cy, kc * ep(t, tc + 4.0, 0.3), 70, CYA, "black")
    board(c, a)
    label(c, L["pergunta"], RX, 260, a * ep(t, ta + 0.6, 0.3), 44, WHITE, "black")
    label(c, L["p_prot"], RX, 360, a * ep(t, tb + 1.0, 0.3), 34, AMB, "bold")
    label(c, L["inverte"], RX, 450, a * ep(t, tc, 0.3), 34, INK2, "bold")
    eq(c, [("200 + 200 = ", WHITE), ("400 m", CYA)], 540, a * ep(t, tc + 3.4, 0.3), 66, box=CYA)
    kd = a * ep(t, td, 0.3)
    pos = eq(c, [(n_("6.000") + " ÷ 200 = ", WHITE), ("30", RED)], 680, a * ep(t, td + 1.6, 0.3), 54)
    popill(c, "D ?", BX1 - 80, 680, 34, RED, BG0, kd * ep(t, td + 4.6, 0.2), t, td + 4.6)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 680, a, ep(t, td + 6.0, 0.4))
    label(c, L["errado"], RX, 780, a * ep(t, td + 6.0, 0.3), 40, RED, "black")
    label(c, L["dobro"], RX, 850, a * ep(t, td + 7.0, 0.3), 34, WHITE, "bold")


def _anel_policiais(c, cx, cy, R, a, t, t0, n, passo=0.18, gap=None, s=20, ang0=0.0):
    """n policiais com trechos de 24° (400 m) em volta, aparecendo um a um a partir de t0; devolve quantos já apareceram"""
    vis = 0
    for i in range(n):
        ti = t0 + i * passo
        k = ep(t, ti, 0.3)
        if k <= 0:
            continue
        vis += 1
        a0 = ang0 + i * 2 * D12
        col = CYA if i % 2 == 0 else MNT
        arco(c, cx, cy, R, a0, a0 + 2 * D12 * k, col, a * 0.9, 24, glow=False)
    for i in range(n):
        ti = t0 + i * passo
        if t >= ti:
            policial_na_pista(c, cx, cy, R, ang0 + i * 2 * D12 + D12, s, a, CYA if i % 2 == 0 else MNT, pop(t, ti, 0.35))
    return vis


def b_divisao(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_div"], a)
    cx, cy = LC
    lagoa(c, cx, cy, RL, a, t)
    # marcas dos trechos de 400 m
    km = a * ep(t, ta + 1.0, 0.4)
    for i in range(15):
        x0, y0 = pt(cx, cy, RL - 22, i * 2 * D12)
        x1, y1 = pt(cx, cy, RL + 22, i * 2 * D12)
        c.drawLine(x0, y0, x1, y1, paint(WHITE, 0.8 * km * ep(t, ta + 1.0 + i * 0.05, 0.2), stroke=3))
    vis = _anel_policiais(c, cx, cy, RL, a, t, tc, 15, 0.2)
    if vis:
        label(c, str(vis), cx, cy - 16, a, 110, WHITE, "black")
        label(c, L["policiais"], cx, cy + 62, a, 36, INK2, "bold")
    board(c, a)
    label(c, L["trechos"], RX, 260, a * ep(t, ta + 0.6, 0.3), 42, WHITE, "black")
    eq(c, [(n_("6.000"), WHITE), (" ÷ ", WHITE), ("400", WHITE)], 370, a * ep(t, tb, 0.3), 64)
    kz = a * ep(t, tb + 2.2, 0.3)
    if kz > 0:   # corta dois zeros
        eq(c, [("60", WHITE), (" ÷ ", WHITE), ("4", WHITE)], 490, kz, 64)
        label(c, L["corta"], RX + 130, 490, kz, 28, INK2, "bold", "left")
    eq(c, [("= ", WHITE), ("15", CYA)], 610, a * ep(t, tb + 4.0, 0.3), 80, box=CYA)
    label(c, L["no_meio"], RX, 720, a * ep(t, tc, 0.3), 32, INK2, "bold")
    ops = [("A", "4"), ("B", "8"), ("C", "15"), ("D", "30"), ("E", "60")]
    kd = a * ep(t, td, 0.3)
    for i, (le, v) in enumerate(ops):
        x = BX0 + 110 + i * 170
        ok = le == "C"
        col = MNT if ok else (RED if le == "D" else INK2)
        k = kd * ep(t, td + i * 0.08, 0.2)
        text_mid(c, le, x - 26, 830, 40, "black", col, k)
        text_mid(c, v, x + 4, 830, 40, "black", WHITE if ok else INK2, k, align="left")
    kk = kd * ep(t, td + 0.6, 0.3)
    if kk > 0:   # moldura na alternativa certa
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 110 + 2 * 170 - 56, 830 - 36, 140, 72), 16, 16)
        c.drawRRect(r, paint(MNT, kk, stroke=4))


def b_minimo(c, t, C, B):
    ta, tb, tc, td = (C[f"07.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_min"], a)
    cx, cy = LC
    lagoa(c, cx, cy, RL, a, t)
    a0 = -123 * GRAU   # o buraco fica embaixo, à esquerda (213°–237°)
    _anel_policiais(c, cx, cy, RL, a, t, ta + 1.0, 14, 0.12, ang0=a0)
    # o buraco: os 24° (400 m) depois do 14º policial
    g0, g1 = a0 + 14 * 2 * D12, a0 + 15 * 2 * D12
    kc = a * ep(t, tc, 0.3)
    fecha = ep(t, td + 0.6, 0.5)
    if kc > 0:
        pul = 0.6 + 0.4 * math.sin(t * 6)
        arco(c, cx, cy, RL, g0, g1, RED, kc * pul * (1 - fecha), 28)
        lx, ly = pt(cx, cy, RL + 100, (g0 + g1) / 2)
        label(c, "400 m", lx - 30, ly - 26, kc * (1 - fecha), 32, RED, "black")
        label(c, L["sem_curto"], lx - 30, ly + 12, kc * (1 - fecha), 26, RED, "bold")
    if t >= td + 0.6:
        arco(c, cx, cy, RL, g0, g0 + 2 * D12 * fecha, MNT, a * 0.9, 24, glow=False)
        policial_na_pista(c, cx, cy, RL, g0 + D12, 20, a, MNT, pop(t, td + 0.6, 0.4))
    n = 15 if t >= td + 0.6 else 14
    if t >= ta + 1.0:
        label(c, str(n), cx, cy - 16, a, 110, WHITE if n == 14 else MNT, "black")
        label(c, L["policiais"], cx, cy + 62, a, 36, INK2, "bold")
    board(c, a)
    label(c, L["com14"], RX, 260, a * ep(t, ta + 0.8, 0.3), 46, WHITE, "black")
    eq(c, [("14 × 400 = ", WHITE), (n_("5.600") + " m", AMB)], 380, a * ep(t, tb, 0.3), 58)
    eq(c, [(n_("6.000") + " − " + n_("5.600") + " = ", WHITE), ("400 m", RED)], 500, kc, 54)
    label(c, L["sem"], RX, 590, kc * ep(t, tc + 0.8, 0.3), 40, RED, "black")
    eq(c, [("15 × 400 = ", WHITE), (n_("6.000") + " m", MNT)], 730, a * ep(t, td + 1.0, 0.3), 64, box=MNT)
    check(c, BX1 - 60, 730, 26, a * ep(t, td + 4.0, 0.2))


def b_generaliza(c, t, C, B):
    ta, tb, tc, td = (C[f"08.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    # a volta de 6.600 m esticada: 16 trechos inteiros + meio trecho
    kb = a * ep(t, tb, 0.4) * (1 - ep(t, td, 0.3))
    x0, x1, y = 110, 900, 520
    seg = (x1 - x0) / 16.5
    if kb > 0:
        label(c, n_("6.600") + " m", (x0 + x1) / 2, y - 130, kb, 48, CYA, "black")
        c.drawLine(x0, y, x1, y, paint(PISTA, kb, stroke=16, cap_round=True))
        for i in range(17):
            k = ep(t, tb + 2.0 + i * 0.1, 0.25)
            if i < 16:
                rrect(c, x0 + i * seg + 2, y - 8, seg - 4, 16, 6, CYA if i % 2 == 0 else MNT, kb * k)
                policial(c, x0 + i * seg + seg / 2, y - 12, 12, kb, CYA if i % 2 == 0 else MNT, pop(t, tb + 2.0 + i * 0.1, 0.3))
        kc = kb * ep(t, tc, 0.3)
        sobra = ep(t, tc + 5.0, 0.4)
        if kc > 0:
            pul = 0.6 + 0.4 * math.sin(t * 6)
            rrect(c, x0 + 16 * seg + 2, y - 8, seg / 2 - 2, 16, 6, RED, kc * pul * (1 - sobra))
            label(c, "?", x0 + 16 * seg + seg / 4, y - 70, kc * (1 - sobra), 54, RED, "black")
        if sobra > 0:   # o 17º policial cobre o pedaço que sobrou
            rrect(c, x0 + 16 * seg + 2, y - 8, seg / 2 - 2, 16, 6, MNT, kb * sobra)
            policial(c, x0 + 16 * seg + seg / 4, y - 12, 12, kb, MNT, pop(t, tc + 5.0, 0.4))
            label(c, "17", x0 + 16 * seg + seg / 4, y + 64, kb * sobra, 44, MNT, "black")
        label(c, "16,5" if not EN else "16.5", (x0 + x1) / 2, y + 130, kb * ep(t, tb + 4.4, 0.3), 44, WHITE, "black")
    kd = a * ep(t, td, 0.3)
    if kd > 0:   # o desafio
        lagoa(c, LX, 560, 230, kd, t)
        popill(c, L["desafio"], LX, 230, 34, AMB, BG0, kd, t, td + 1.0)
        label(c, "?", LX, 560, kd * ep(t, td + 3.0, 0.3), 120, CYA, "black")
    board(c, a)
    eq(c, [(L["r11"], AMB)], 260, a * ep(t, ta + 1.2, 0.3), 44)
    eq(c, [("C = 2 · 3 · " + n_("1.100") + " = ", WHITE), (n_("6.600") + " m", CYA)], 370, a * ep(t, tb, 0.3), 50)
    eq(c, [(n_("6.600") + " ÷ 400 = ", WHITE), ("16,5" if not EN else "16.5", AMB)], 480, a * ep(t, tb + 4.0, 0.3), 56)
    label(c, L["meio"], RX, 580, a * ep(t, tc, 0.3), 36, WHITE, "bold")
    label(c, L["com16"], RX, 640, a * ep(t, tc + 1.8, 0.3), 34, RED, "bold")
    eq(c, [(L["cima"], WHITE), ("17", MNT)], 750, a * ep(t, tc + 4.0, 0.3), 58, box=MNT)
    label(c, L["comenta"], RX, 860, a * ep(t, td + 6.0, 0.3), 38, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"09.{k}"] for k in "bcde"]
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
    """miniatura de cada aula: circunferência com raio · conversão · divisão"""
    if i == 0:
        c.drawCircle(cx, cy, 70, paint(CYA, a, stroke=6))
        c.drawCircle(cx, cy, 6, paint(WHITE, a))
        c.drawLine(cx, cy, cx + 70, cy, paint(AMB, a, stroke=5, cap_round=True))
        label(c, "r", cx + 35, cy - 24, a, 32, AMB, "black")
    elif i == 1:
        eq(c, [("1 km = ", WHITE), (n_("1.000") + " m", AMB)], cy, a, 44, cx=cx, maxw=380)
    else:
        eq(c, [(n_("6.000") + " ÷ 400 = ", WHITE), ("15", CYA)], cy, a, 40, cx=cx, maxw=380)


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"10.{k}"] for k in "abcdef")
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
        kl = kg * ep(t, tf + 1.2, 0.4)
        lagoa(c, 960, 800, 110, kl, t)
        for i in range(15):
            policial_na_pista(c, 960, 800, 110, i * 2 * D12 + D12, 9, kl, CYA if i % 2 == 0 else MNT)


BLOCKS = dict(gancho=b_gancho, circunferencia=b_circunferencia, unidades=b_unidades, volta=b_volta, cobertura=b_cobertura,
              divisao=b_divisao, minimo=b_minimo, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
