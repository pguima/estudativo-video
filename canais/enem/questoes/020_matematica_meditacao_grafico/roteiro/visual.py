"""Visual — Estudativo · Questão de Matemática 020 (aula horizontal 1920x1080): ENEM 2025, questão 142, o gráfico da
frequência respiratória na meditação. Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = dado do gráfico (f1, f2, t1, t2, o trecho antes de t1), ciano = o trecho que desce (diminui),
menta = o trecho deitado (constante) e a resposta, coral = as alternativas erradas e as formas que o gráfico não tem.
Figura principal: o gráfico da questão redesenhado (grafico()), com cada trecho pintado na cor do que ele faz e um ponto
que anda pela linha mostrando o instante e o valor."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_020_matematica_meditacao_grafico.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.d": "shimmer", "02.d": "data", "02.e": "confirm", "03.b": "data", "03.c": "data", "04.c": "deny",
        "05.c": "confirm", "06.b": "confirm", "06.d": "impact", "07.b": "deny", "07.c": "deny", "07.d": "deny",
        "07.e": "deny", "08.b": "whoosh", "08.c": "alert", "10.a": "shimmer", "10.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 020", "QUESTÃO DE MATEMÁTICA · 020"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_leitura=("TOOL 1 · READING A GRAPH", "FERRAMENTA 1 · LER UM GRÁFICO"),
    s_prop=("TOOL 2 · PROPORTIONAL", "FERRAMENTA 2 · PROPORCIONAL"),
    s_t1=("STEP 1 · ONLY WHAT IS ASKED", "PASSO 1 · SÓ O QUE A PERGUNTA PEDE"),
    s_t2=("STEP 2 · FROM t₁ TO t₂", "PASSO 2 · DE t₁ ATÉ t₂"), s_t3=("STEP 3 · AFTER t₂", "PASSO 3 · DEPOIS DE t₂"),
    s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"),
    s_gen=("THE SAME SHAPE · AND A CHALLENGE", "O MESMO DESENHO · E UM DESAFIO"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 142", "ENEM 2025 · questão 142"),
    freq=("breathing rate", "frequência respiratória"), rpm=("breaths per minute", "respirações por minuto"),
    t1=("t₁ = meditation starts", "t₁ = começa a meditação"), t2=("t₂ = breathing settles", "t₂ = a respiração estabiliza"),
    pede=("from t₁ on: ?", "a partir de t₁: ?"),
    p_ler=("READ THE GRAPH", "LER O GRÁFICO"), p_pal=("THE HARD WORDS", "AS PALAVRAS DIFÍCEIS"),
    eixo_t=("time (min)", "tempo (min)"), eixo_f=("rate (bpm)", "frequência (rpm)"),
    ponto=("point = (instant, value)", "ponto = (instante, valor)"),
    sobe=("goes up → increases", "sobe → aumenta"), desce=("goes down → decreases", "desce → diminui"),
    deitada=("flat → constant", "deitada → constante"),
    direta=("DIRECTLY PROPORTIONAL", "DIRETAMENTE PROPORCIONAL"), inversa=("INVERSELY PROPORTIONAL", "INVERSAMENTE PROPORCIONAL"),
    dobra=("doubles → doubles", "dobra → dobra"), metade=("doubles → halves", "dobra → metade"),
    reta=("rising line through 0", "reta que sobe e passa pelo 0"), nunca=("never goes flat", "nunca fica deitada"),
    antes=("before t₁: flat at f₁", "antes de t₁: deitada em f₁"), pergunta=("question: FROM t₁ ON", "pergunta: A PARTIR DE t₁"),
    fora=("left out", "fica de fora"), medita=("not meditating yet", "ainda não medita"),
    de_t1=("from t₁ to t₂", "de t₁ até t₂"), f1f2=("f₁ → f₂ (lower)", "f₁ → f₂ (mais baixo)"), diminui=("DECREASES", "DIMINUI"),
    depois=("after t₂", "depois de t₂"), sempre_f2=("always f₂", "sempre f₂"), constante=("CONSTANT", "CONSTANTE"),
    junta=("decreases until t₂, then constant", "diminui até t₂, depois constante"),
    alt=(["A · stays constant", "B · directly proportional", "C · inversely proportional", "E · decreases the whole time"],
         ["A · mantém-se constante", "B · diretamente proporcional", "C · inversamente proporcional",
          "E · diminui o tempo todo"]),
    pq=(["it goes down between t₁ and t₂", "time goes up, the rate goes down", "after t₂ the line goes flat",
         "after t₂ it stops decreasing"],
        ["entre t₁ e t₂ a linha desce", "o tempo sobe e a frequência desce", "depois de t₂ a linha deita",
         "depois de t₂ ela para de diminuir"]),
    cafe=("hot coffee on the table", "café quente na mesa"), sala=("room", "sala"), temp=("temperature", "temperatura"),
    rapido=("fast, then slower", "rápido, depois devagar"),
    desafio=("iced juice on the same table?", "suco gelado na mesma mesa?"), como=("what does the graph look like?", "como fica o gráfico?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["what does each axis show?", "only the part that is asked", "up, down or flat?",
             "proportional: only with the right shape"],
            ["o que cada eixo mostra?", "só o trecho que a pergunta pede", "sobe, desce ou deitada?",
             "proporcional: só com a forma certa"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Reading", "graphs"), ("Increasing, decreasing", "and constant"), ("Direct and inverse", "proportion")],
           [("Leitura de", "gráficos"), ("Funções crescentes,", "decrescentes e constantes"),
            ("Grandezas diretamente e", "inversamente proporcionais")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("tê um", "t₁"), ("tê dois", "t₂"), ("efe um", "f₁"), ("efe dois", "f₂"),
    ("passo um", "Passo 1"), ("passo dois", "Passo 2"), ("passo três", "Passo 3"), ("letra a", "letra A"),
    ("letra b", "letra B"), ("letra c", "letra C"), ("letra e", "letra E")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("diminui", "mais"), ("vez", "mais"), ("muda", "mais")}   # "mais" que não é "+"


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- o gráfico da questão
T1, T2 = 0.36, 0.66          # posições de t1 e t2 no eixo do tempo (0..1)
F1, F2 = 0.74, 0.36          # alturas de f1 e f2 (0..1)
GX, GY, GW, GH = 200, 820, 690, 560     # origem (canto de baixo à esquerda), largura e altura da área do gráfico


def f(u):
    """altura (0..1) da linha no tempo u (0..1): deitada em F1, desce suave de T1 a T2, deitada em F2"""
    if u <= T1:
        return F1
    if u >= T2:
        return F2
    k = (u - T1) / (T2 - T1)
    k = k * k * k * (k * (6 * k - 15) + 10)
    return F1 + (F2 - F1) * k


def _xy(u, v, g):
    gx, gy, gw, gh = g
    return gx + u * gw, gy - v * gh


def _tracejado(col, a, w=3):
    p = paint(col, a, stroke=w)
    p.setPathEffect(skia.DashPathEffect.Make([12, 10], 0))
    return p


def _curva(c, u0, u1, g, col, a, w=9, glow=0.0, fn=f):
    if a <= 0 or u1 <= u0:
        return
    p = skia.Path()
    n = max(2, int((u1 - u0) * 160))
    for i in range(n + 1):
        u = u0 + (u1 - u0) * i / n
        x, y = _xy(u, fn(u), g)
        (p.moveTo if i == 0 else p.lineTo)(x, y)
    if glow > 0:
        c.drawPath(p, blur_paint(col, 0.6 * a * glow, 18, stroke=w * 2.4))
    st = paint(col, a, stroke=w, cap_round=True)
    st.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, st)


def eixos(c, a, g=(GX, GY, GW, GH), rot=True, size=1.0):
    gx, gy, gw, gh = g
    if a <= 0:
        return
    w = 4 * size
    c.drawLine(gx, gy, gx + gw + 30 * size, gy, paint(WHITE, a, stroke=w, cap_round=True))
    c.drawLine(gx, gy, gx, gy - gh - 30 * size, paint(WHITE, a, stroke=w, cap_round=True))
    for (x0, y0, dx, dy) in ((gx + gw + 30 * size, gy, 1, 0), (gx, gy - gh - 30 * size, 0, -1)):
        s = 16 * size
        p = skia.Path()
        p.moveTo(x0 + dx * s, y0 + dy * s)
        p.lineTo(x0 - dy * s * 0.6 - dx * 0.0, y0 + dx * s * 0.6)
        p.lineTo(x0 + dy * s * 0.6, y0 - dx * s * 0.6)
        p.close()
        c.drawPath(p, paint(WHITE, a))
    if rot:
        text_mid(c, L["eixo_t"], gx + gw, gy + 46 * size, 30 * size, "bold", INK2, a, align="right")
        c.save(); c.translate(gx - 100 * size, gy - gh / 2); c.rotate(-90)
        text_mid(c, L["eixo_f"], 0, 0, 30 * size, "bold", INK2, a)
        c.restore()


def grafico(c, a, t, draw=1.0, cores=None, ponto=None, guias=1.0, g=(GX, GY, GW, GH), marcas=1.0):
    """o gráfico da questão. cores = {"antes": (cor, alfa, glow), "desce": ..., "deitada": ...} pinta cada trecho;
    draw 0..1 desenha a linha da esquerda para a direita; ponto = u (0..1) mostra um ponto com as projeções"""
    if a <= 0:
        return
    gx, gy, gw, gh = g
    eixos(c, a, g)
    km = a * marcas
    # marcas f1, f2, t1, t2 e as guias tracejadas
    for v, s in ((F1, "f₁"), (F2, "f₂")):
        text_mid(c, s, gx - 24, gy - v * gh, 40, "black", AMB, km, align="right")
    for u, s in ((T1, "t₁"), (T2, "t₂")):
        text_mid(c, s, gx + u * gw, gy + 40, 40, "black", AMB, km)
    if guias > 0:
        x1, y1 = _xy(T1, F1, g)
        x2, y2 = _xy(T2, F2, g)
        c.drawLine(x1, y1, x1, gy, _tracejado(INK2, 0.7 * a * guias))
        c.drawLine(x2, y2, x2, gy, _tracejado(INK2, 0.7 * a * guias))
        c.drawLine(gx, y2, x2, y2, _tracejado(INK2, 0.5 * a * guias))
    cores = cores or {}
    padrao = (WHITE, 1.0, 0.0)
    for nome, u0, u1 in (("antes", 0.0, T1), ("desce", T1, T2), ("deitada", T2, 1.0)):
        col, al, gl = cores.get(nome, padrao)
        _curva(c, u0, min(u1, draw), g, col, a * al, glow=gl)
    if ponto is not None and 0 <= ponto <= 1:
        x, y = _xy(ponto, f(ponto), g)
        c.drawLine(x, y, x, gy, _tracejado(CYA, 0.9 * a))
        c.drawLine(gx, y, x, y, _tracejado(CYA, 0.9 * a))
        c.drawCircle(x, y, 22, blur_paint(CYA, 0.6 * a, 14))
        c.drawCircle(x, y, 13, paint(WHITE, a))
        c.drawCircle(x, y, 13, paint(CYA, a, stroke=5))


def mini(c, a, cx, cy, tipo, col, draw=1.0, w=150, h=110):
    """grafiquinho: 'sobe', 'desce', 'deitada', 'direta', 'inversa' (eixos + a forma)"""
    if a <= 0:
        return
    g = (cx - w / 2, cy + h / 2, w, h)
    eixos(c, a, g, rot=False, size=0.5)
    fn = {"sobe": lambda u: 0.15 + 0.7 * u, "desce": lambda u: 0.85 - 0.7 * u, "deitada": lambda u: 0.5,
          "direta": lambda u: 0.9 * u, "inversa": lambda u: min(1.0, 0.12 / max(u, 0.01))}[tipo]
    _curva(c, 0.0 if tipo != "inversa" else 0.12, draw, g, col, a, w=7, fn=fn)


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


def opcoes(c, a, t, t0, certa="D", erradas=(), y=800):
    """linha A B C D E no pé do quadro, com a certa em caixa menta e as erradas riscadas"""
    for j, le in enumerate("ABCDE"):
        x = BX0 + 130 + j * 160
        k = a * ep(t, t0 + j * 0.08, 0.2)
        col = MNT if le == certa else (RED if le in erradas else INK2)
        text_mid(c, le, x, y, 48, "black", col, k)
        if le in erradas:
            cross(c, x, y, 30, k * ep(t, t0 + 0.6, 0.2))
    kk = a * ep(t, t0 + 0.6, 0.3)
    if kk > 0 and certa:
        j = "ABCDE".index(certa)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 130 + j * 160 - 46, y - 44, 92, 88), 18, 18)
        c.drawRRect(r, paint(MNT, kk, stroke=4))


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    label(c, L["freq"], RX, 340, a, 50, AMB, "black")
    label(c, L["rpm"], RX, 405, a * ep(t, ta + 3.0, 0.3), 34, INK2, "bold")
    label(c, L["t1"], RX, 490, a * ep(t, tb, 0.3), 40, WHITE, "black")
    label(c, L["t2"], RX, 560, a * ep(t, tb + 2.4, 0.3), 40, WHITE, "black")
    eq(c, [(L["pede"].split(":")[0] + ": ", WHITE), ("?", CYA)], 680, a * ep(t, tc, 0.3), 54, box=CYA)
    kd = a * ep(t, td, 0.3)
    popill(c, L["p_ler"], RX - 190, 830, 26, CYA, BG0, kd, t, td + 0.4)
    popill(c, L["p_pal"], RX + 210, 830, 26, RED, BG0, kd, t, td + 2.2)


def b_leitura(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_leitura"], a)
    draw = ep(t, ta + 0.3, 1.6)
    # o ponto anda pela linha a partir de c
    pu = None
    if t >= tc:
        pu = 0.08 + 0.84 * (0.5 - 0.5 * math.cos((t - tc) * 0.55))
    cores = {}
    if t >= td:
        kd = ep(t, td + 1.0, 0.3)
        cores = {"desce": (CYA, 1.0, kd), "deitada": (MNT, 1.0, ep(t, te, 0.3)), "antes": (MNT, 1.0, ep(t, te, 0.3))}
    grafico(c, a, t, draw, cores=cores, ponto=pu, guias=0.0, marcas=0.0)
    # eixos em destaque na fala
    kb = ep(t, tb, 0.3) * (1 - ep(t, tc, 0.3))
    if kb > 0:
        c.drawLine(GX, GY, GX + GW + 30, GY, blur_paint(AMB, 0.8 * a * kb * ep(t, tb, 0.3), 14, stroke=14))
        c.drawLine(GX, GY, GX, GY - GH - 30, blur_paint(AMB, 0.8 * a * kb * ep(t, tb + 2.4, 0.3), 14, stroke=14))
    board(c, a)
    label(c, L["eixo_t"].split(" (")[0].upper() + " → " + L["eixo_t"].split("(")[1].rstrip(")"), RX, 260,
          a * ep(t, tb + 0.4, 0.3), 40, WHITE, "black")
    label(c, L["eixo_f"].split(" (")[0].upper() + " → " + L["eixo_f"].split("(")[1].rstrip(")"), RX, 330,
          a * ep(t, tb + 2.6, 0.3), 40, WHITE, "black")
    eq(c, [(L["ponto"], CYA)], 450, a * ep(t, tc + 0.6, 0.3), 42, box=CYA)
    for q, (key, tipo, col, t0) in enumerate((("sobe", "sobe", AMB, td + 0.6), ("desce", "desce", CYA, td + 2.6),
                                               ("deitada", "deitada", MNT, te))):
        k = a * ep(t, t0, 0.3)
        y = 590 + q * 110
        mini(c, k, BX0 + 150, y, tipo, col, draw=ep(t, t0, 0.8), w=120, h=80)
        text_mid(c, L[key], BX0 + 260, y, 42, "black", col, k, align="left")


def b_proporcao(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_prop"], a)
    kd = a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.4))      # diretamente
    ki = a * ep(t, tc, 0.4)                              # inversamente
    g = (GX + 30, GY - 20, GW - 60, GH - 80)
    gx, gy, gw, gh = g
    if kd > 0:
        eixos(c, kd, g, rot=False)
        _curva(c, 0.0, ep(t, tb + 0.4, 1.2), g, AMB, kd, fn=lambda u: 0.9 * u, glow=0.5)
        for j, (xv, yv, t0) in enumerate(((2, 10, tb + 3.6), (4, 20, tb + 4.6))):
            u = xv / 5.0
            x, y = _xy(u, 0.9 * u, g)
            k = kd * ep(t, t0, 0.3)
            c.drawLine(x, y, x, gy, _tracejado(INK2, 0.7 * k))
            c.drawLine(gx, y, x, y, _tracejado(INK2, 0.7 * k))
            bolinha(c, x, y, "", k, AMB, k=0.4)
            text_mid(c, str(xv), x, gy + 40, 38, "black", AMB, k)
            text_mid(c, str(yv), gx - 22, y, 38, "black", WHITE, k, align="right")
        bolinha(c, gx, gy, "0", kd * ep(t, tb + 6.4, 0.3), AMB, glow=1.0, k=0.7, size=38)
    if ki > 0:
        eixos(c, ki, g, rot=False)
        fi = lambda u: min(1.05, 0.12 / max(u, 0.01))   # noqa: E731
        _curva(c, 0.115, 0.115 + 0.885 * ep(t, tc + 0.4, 1.4), g, CYA, ki, fn=fi, glow=0.5)
        for j, (xv, yv, t0) in enumerate(((2, 6, tc + 3.0), (4, 3, tc + 4.0))):
            u = xv / 10.0
            x, y = _xy(u, fi(u), g)
            k = ki * ep(t, t0, 0.3)
            c.drawLine(x, y, x, gy, _tracejado(INK2, 0.7 * k))
            c.drawLine(gx, y, x, y, _tracejado(INK2, 0.7 * k))
            bolinha(c, x, y, "", k, CYA, k=0.4)
            text_mid(c, str(xv), x, gy + 40, 38, "black", CYA, k)
            text_mid(c, str(yv), gx - 22, y, 38, "black", WHITE, k, align="right")
    board(c, a)
    if kd > 0:
        label(c, L["direta"], RX, 260, kd, 40, AMB, "black")
        eq(c, [(L["dobra"], WHITE)], 370, kd * ep(t, tb + 1.0, 0.3), 52)
        eq(c, [("2 → 10   ·   4 → 20", WHITE)], 490, kd * ep(t, tb + 3.6, 0.3), 46)
        eq(c, [("y = k · x", AMB)], 620, kd * ep(t, tb + 5.0, 0.3), 56, box=AMB)
        popill(c, L["reta"], RX, 770, 32, AMB, BG0, kd * ep(t, tb + 6.0, 0.3), t, tb + 6.0)
    if ki > 0:
        label(c, L["inversa"], RX, 260, ki, 40, CYA, "black")
        eq(c, [(L["metade"], WHITE)], 370, ki * ep(t, tc + 1.0, 0.3), 52)
        eq(c, [("2 → 6   ·   4 → 3", WHITE)], 490, ki * ep(t, tc + 3.0, 0.3), 46)
        eq(c, [("x · y = k", CYA)], 620, ki * ep(t, tc + 4.6, 0.3), 56, box=CYA)
        popill(c, L["nunca"], RX, 770, 34, RED, BG0, ki * ep(t, td + 1.6, 0.3), t, td + 1.6)


def b_trecho1(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_t1"], a)
    kb = ep(t, tb, 0.3)
    kc = ep(t, tc + 1.6, 0.4)
    cores = {"antes": (AMB if kc == 0 else INK2, 1.0 - 0.6 * kc, kb * (1 - kc)), "desce": (WHITE, 0.35 + 0.65 * kc, 0),
             "deitada": (WHITE, 0.35 + 0.65 * kc, 0)}
    grafico(c, a, t, 1.0, cores=cores)
    # a faixa que fica de fora
    if kc > 0:
        x1 = GX + T1 * GW
        rrect(c, GX + 6, GY - GH - 10, x1 - GX - 12, GH + 4, 16, RED, 0.12 * a * kc)
        cross(c, GX + T1 * GW / 2, GY - GH * 0.4, 34, a * kc)
        label(c, L["medita"], GX + T1 * GW / 2, GY - GH * 0.4 + 70, a * kc, 28, RED, "black")
    board(c, a)
    label(c, L["antes"], RX, 300, a * ep(t, tb + 0.6, 0.3), 46, AMB, "black")
    eq(c, [(L["pergunta"], CYA)], 470, a * ep(t, tc, 0.3), 46, box=CYA)
    popill(c, L["fora"], RX, 640, 36, RED, BG0, a * ep(t, tc + 1.8, 0.3), t, tc + 1.8)


def b_trecho2(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_t2"], a)
    kb = ep(t, tb, 0.3)
    cores = {"antes": (INK2, 0.4, 0), "desce": (CYA, 1.0, kb), "deitada": (WHITE, 0.35, 0)}
    pu = T1 + (T2 - T1) * ease_io(prog(t, tb + 0.3, 2.4)) if t >= tb else None
    grafico(c, a, t, 1.0, cores=cores, ponto=pu)
    board(c, a)
    label(c, L["de_t1"], RX, 280, a * ep(t, ta + 0.8, 0.3), 46, WHITE, "black")
    eq(c, [(L["f1f2"], AMB)], 420, a * ep(t, tb + 1.0, 0.3), 50)
    eq(c, [("↓  " + L["diminui"], CYA)], 600, a * ep(t, tc + 0.6, 0.3), 70, box=CYA)


def b_trecho3(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_t3"], a)
    kb = ep(t, tb, 0.3)
    kc = ep(t, tc, 0.3)
    cores = {"antes": (INK2, 0.4, 0), "desce": (CYA, 0.5 + 0.5 * kc, kc), "deitada": (MNT, 1.0, kb)}
    pu = T2 + (1 - T2) * (0.5 - 0.5 * math.cos((t - tb) * 1.2)) if tb <= t < tc else None
    grafico(c, a, t, 1.0, cores=cores, ponto=pu)
    board(c, a)
    k1 = a * (1 - kc)
    label(c, L["depois"], RX, 280, k1 * ep(t, ta + 0.8, 0.3), 46, WHITE, "black")
    eq(c, [(L["sempre_f2"], AMB)], 420, k1 * ep(t, tb + 1.0, 0.3), 50)
    eq(c, [("→  " + L["constante"], MNT)], 600, k1 * ep(t, tb + 2.6, 0.3), 70, box=MNT)
    if kc > 0:
        eq(c, [("↓ " + L["diminui"], CYA), ("  +  ", WHITE), ("→ " + L["constante"], MNT)], 330, a * kc, 50)
        label(c, L["junta"], RX, 450, a * ep(t, tc + 1.4, 0.3), 36, INK2, "bold")
        opcoes(c, a, t, td, "D", y=640)


PEG_FN = [None,                                                    # A: (a própria linha, trecho que desce em coral)
          lambda u: 0.08 + 0.8 * u,                                # B: reta que sobe e passa pelo 0
          lambda u: min(1.05, 0.2 / max(u, 0.01)),                 # C: curva inversa (nunca deita)
          lambda u: F1 - (F1 - 0.0) * (u - T1) / (1 - T1)]          # E: diminuindo sempre (até o fim)


def b_pegadinhas(c, t, C, B):
    ts = [C[f"07.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    atual = max([j for j, t0 in enumerate(ts) if t >= t0], default=-1)
    cores = {"antes": (INK2, 0.4, 0), "desce": (MNT, 1.0, 0), "deitada": (MNT, 1.0, 0)}
    if atual == 0:
        cores["desce"] = (RED, 1.0, ep(t, ts[0] + 1.6, 0.3))
    grafico(c, a, t, 1.0, cores=cores)
    if atual >= 1:
        k = a * ep(t, ts[atual], 0.3)
        fn = PEG_FN[atual]
        u0 = {1: 0.0, 2: 0.17, 3: T1}[atual]
        g = (GX, GY, GW, GH)
        x0 = _curva(c, u0, u0 + (1 - u0) * ep(t, ts[atual] + 0.6, 1.2), g, RED, k, w=6, fn=fn)
        if atual >= 2:   # o trecho deitado da questão, que a forma errada não tem
            _curva(c, T2, 1.0, g, MNT, k, w=9, glow=ep(t, ts[atual] + 2.4, 0.3))
    board(c, a)
    for j, t0 in enumerate(ts):
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        y = 270 + j * 150
        cross(c, BX0 + 70, y, 24, k * ep(t, t0 + 1.2, 0.2))
        text_mid(c, L["alt"][j], BX0 + 116, y - 22, 38, "black", RED if j <= atual else INK2, k, align="left")
        text_mid(c, L["pq"][j], BX0 + 116, y + 26, 32, "semibold", WHITE, k * ep(t, t0 + 1.0, 0.3), align="left")


def xicara(c, cx, cy, a, col, t, vapor=1.0, copo=False):
    """xícara de café (ou copo de suco, copo=True) simples, no estilo do design system"""
    if a <= 0:
        return
    if copo:
        p = skia.Path(); p.moveTo(cx - 60, cy - 80); p.lineTo(cx + 60, cy - 80); p.lineTo(cx + 46, cy + 80); p.lineTo(cx - 46, cy + 80); p.close()
        c.drawPath(p, paint(BG1, 0.95 * a))
        c.save(); c.clipPath(p, doAntiAlias=True)
        c.drawRect(skia.Rect.MakeLTRB(cx - 70, cy - 40, cx + 70, cy + 90), paint(AMB, 0.85 * a))
        for j in range(3):
            rrect(c, cx - 40 + j * 26, cy - 20 + (j % 2) * 30, 24, 24, 5, "#DDF6FF", 0.9 * a)
        c.restore()
        c.drawPath(p, paint(WHITE, a, stroke=5))
        return
    rrect(c, cx - 70, cy - 60, 140, 130, 30, BG1, 0.95 * a)
    c.save(); c.clipRect(skia.Rect.MakeLTRB(cx - 70, cy - 60, cx + 70, cy - 40))
    c.drawRect(skia.Rect.MakeLTRB(cx - 70, cy - 60, cx + 70, cy - 40), paint("#7A4A2A", a))
    c.restore()
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 70, cy - 60, 140, 130), 30, 30), paint(col, a, stroke=6))
    c.drawArc(skia.Rect.MakeXYWH(cx + 50, cy - 30, 60, 60), -90, 180, False, paint(col, a, stroke=6))
    for j in range(3):
        k = ((t * 0.6 + j / 3) % 1)
        x = cx - 30 + j * 30 + 8 * math.sin(t * 3 + j)
        c.drawLine(x, cy - 80 - k * 70, x + 6 * math.sin(t * 4 + j), cy - 100 - k * 70, paint(WHITE, a * vapor * (1 - k) * 0.7, stroke=5, cap_round=True))


def b_generaliza(c, t, C, B):
    ta, tb, tc = (C[f"08.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    kb = a * ep(t, tb, 0.3) * (1 - ep(t, tc, 0.4))
    kc = a * ep(t, tc, 0.4)
    g = (GX + 60, GY, GW - 80, GH - 140)
    sala = 0.3
    k0 = a * (1 - ep(t, tb, 0.3))          # abertura: o desenho da questão (desce e depois deita)
    if k0 > 0:
        grafico(c, k0, t, 1.0, cores={"antes": (INK2, 0.4, 0), "desce": (CYA, 1.0, 1.0), "deitada": (MNT, 1.0, 1.0)})
    if kb > 0:
        eixos(c, kb, g, rot=False)
        c.drawLine(g[0], g[1] - sala * g[3], g[0] + g[2], g[1] - sala * g[3], _tracejado(AMB, kb))
        text_mid(c, L["sala"], g[0] + g[2] + 10, g[1] - sala * g[3] - 26, 30, "black", AMB, kb, align="right")
        fc = lambda u: sala + (0.95 - sala) * math.exp(-5.5 * u)   # noqa: E731
        _curva(c, 0.0, ep(t, tb + 0.6, 3.0), g, CYA, kb, fn=fc, glow=0.4)
        text_mid(c, L["temp"], g[0], g[1] - g[3] - 46, 30, "bold", INK2, kb, align="left")
        xicara(c, LX + 230, 300, kb, CYA, t, vapor=1 - ep(t, tb + 3.0, 2.0))
    if kc > 0:
        eixos(c, kc, g, rot=False)
        c.drawLine(g[0], g[1] - 0.55 * g[3], g[0] + g[2], g[1] - 0.55 * g[3], _tracejado(AMB, kc))
        text_mid(c, L["sala"], g[0] + g[2] + 10, g[1] - 0.55 * g[3] - 26, 30, "black", AMB, kc, align="right")
        text_mid(c, "?", g[0] + g[2] * 0.45, g[1] - g[3] * 0.25, 120, "black", AMB, kc * ep(t, tc + 1.4, 0.3))
        xicara(c, LX + 230, 300, kc, AMB, t, copo=True)
    board(c, a)
    if kb > 0:
        label(c, L["cafe"], RX, 300, kb, 46, CYA, "black")
        eq(c, [(L["rapido"], WHITE)], 430, kb * ep(t, tb + 1.6, 0.3), 44)
        eq(c, [("→  " + L["constante"], MNT)], 590, kb * ep(t, tb + 5.6, 0.3), 56, box=MNT)
    if kc > 0:
        label(c, L["desafio"], RX, 330, kc * ep(t, tc + 0.8, 0.3), 44, AMB, "black")
        label(c, L["como"], RX, 470, kc * ep(t, tc + 3.0, 0.3), 48, WHITE, "black")
        label(c, L["comenta"], RX, 640, kc * ep(t, tc + 4.6, 0.3), 40, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"09.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 280 + i * 160
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 300
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 50, "black", WHITE, ki, align="left")
        check(c, 1660, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula: um gráfico com eixos · sobe/desce/deitada · reta e curva inversa"""
    if i == 0:
        mini(c, a, cx, cy, "desce", CYA, w=200, h=130)
    elif i == 1:
        for j, (tipo, col) in enumerate((("sobe", AMB), ("desce", CYA), ("deitada", MNT))):
            mini(c, a, cx - 140 + j * 140, cy, tipo, col, w=100, h=80)
    else:
        mini(c, a, cx - 80, cy, "direta", AMB, w=120, h=100)
        mini(c, a, cx + 90, cy, "inversa", CYA, w=120, h=100)


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
            bolinha(c, 960 - 280 + j * 140, 790, v, kl, MNT if v == "D" else INK2, glow=1.0 if v == "D" else 0, k=0.9)


BLOCKS = dict(gancho=b_gancho, leitura=b_leitura, proporcao=b_proporcao, trecho1=b_trecho1, trecho2=b_trecho2,
              trecho3=b_trecho3, pegadinhas=b_pegadinhas, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
