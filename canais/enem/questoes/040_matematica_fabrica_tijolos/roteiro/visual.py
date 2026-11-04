"""Visual — Estudativo · Questão de Matemática 040 (aula horizontal 1920x1080): ENEM 2025, questão 152, a fábrica de
tijolos (proporcionalidade e produção por hora de trabalho). Design system de matemática: _ferramentas/matematica.py.
Figura: a grade "funcionários × horas" (grade()): cada linha é um funcionário, cada coluna uma hora; cada quadradinho é
1 funcionário trabalhando 1 hora e vale 40 tijolos. A grade cresce (3 × 6 → 5 × 9) para mostrar o aumento.
Cores: âmbar = dado (720, 3 × 6), ciano = as horas de trabalho, menta = a resposta (1 800), coral = as alternativas
erradas."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_040_matematica_fabrica_tijolos.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.b": "data", "01.c": "data", "01.d": "alert", "01.e": "shimmer", "02.b": "data", "02.c": "confirm",
        "02.d": "confirm", "02.e": "lock", "03.b": "data", "03.c": "confirm", "04.b": "data", "04.c": "confirm",
        "04.d": "lock", "05.b": "data", "05.c": "confirm", "06.b": "data", "06.c": "impact", "07.b": "data",
        "07.c": "data", "07.d": "confirm", "07.e": "confirm", "08.b": "impact", "09.b": "deny", "09.c": "deny",
        "09.d": "deny", "09.e": "deny", "10.b": "alert", "11.a": "shimmer", "12.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 040", "QUESTÃO DE MATEMÁTICA · 040"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_prop=("TOOL 1 · PROPORTIONAL QUANTITIES", "FERRAMENTA 1 · GRANDEZAS PROPORCIONAIS"),
    s_horas=("TOOL 2 · THE WORK HOUR", "FERRAMENTA 2 · A HORA DE TRABALHO"),
    s_p1=("STEP 1 · BRICKS PER WORK HOUR", "PASSO 1 · TIJOLOS POR HORA DE TRABALHO"),
    s_p2=("STEP 2 · THE NEW WORK HOURS", "PASSO 2 · AS HORAS DE TRABALHO NOVAS"),
    s_p3=("STEP 3 · THE NEW PRODUCTION", "PASSO 3 · A PRODUÇÃO NOVA"), s_conf=("CHECKING ANOTHER WAY", "CONFERINDO DE OUTRO JEITO"),
    s_resp=("THE ANSWER", "A RESPOSTA"), s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"),
    s_des=("CHALLENGE", "DESAFIO"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 152", "ENEM 2025 · questão 152"), fab=("the brick factory", "a fábrica de tijolos"),
    g1=("3 workers · 6 h → 720 a day", "3 funcionários · 6 h → 720 por dia"),
    g2=("5 workers · 9 h → ?", "5 funcionários · 9 h → ?"), g3=("same output per hour", "mesma produção por hora"),
    pede=("how many bricks a day?", "quantos tijolos por dia?"),
    t_prop=("proportionality", "proporcionalidade"), t_hora=("per work hour", "por hora de trabalho"),
    pr1=("same output per hour", "mesma produção por hora"), pr2=("2× workers → 2× bricks", "2× funcionários → 2× tijolos"),
    pr3=("2× hours → 2× bricks", "2× horas → 2× tijolos"), pr4=("proportional to workers × hours", "proporcional a funcionários × horas"),
    h1=("□ = 1 worker · 1 hour", "□ = 1 funcionário · 1 hora"), h2=("3 × 6 = 18 work hours", "3 × 6 = 18 horas de trabalho"),
    q1=("720 bricks in 18 work hours", "720 tijolos em 18 horas de trabalho"), q2=("720 ÷ 18 = 40", "720 ÷ 18 = 40"),
    q3=("□ = 40 bricks", "□ = 40 tijolos"),
    n1=("5 workers · 9 hours", "5 funcionários · 9 horas"), n2=("5 × 9 = 45 work hours", "5 × 9 = 45 horas de trabalho"),
    m1=("45 squares × 40 bricks", "45 quadradinhos × 40 tijolos"), m2=("45 × 40 = 1 800", "45 × 40 = 1 800"),
    m3=("bricks a day!", "tijolos por dia!"),
    k1=("workers 3 → 5:  × 5/3", "funcionários 3 → 5:  × 5/3"), k2=("hours 6 → 9:  × 3/2", "horas 6 → 9:  × 3/2"),
    k3=("720 × 5/3 = 1 200", "720 × 5/3 = 1 200"), k4=("1 200 × 3/2 = 1 800 ✓", "1 200 × 3/2 = 1 800 ✓"),
    r1=("1 800 bricks a day", "1 800 tijolos por dia"), alt=("ANSWER", "ALTERNATIVA"),
    pA=("800 → no correct count gives it", "800 → não sai de conta certa"),
    pB=("1 080 → only the hours (3 × 9)", "1 080 → só as horas (3 × 9)"),
    pC=("1 200 → only the workers (5 × 6)", "1 200 → só os funcionários (5 × 6)"),
    pD=("1 800 → 5 × 9 × 40 ✓", "1 800 → 5 × 9 × 40 ✓"), pE=("2 520 → 720 + 1 800", "2 520 → 720 + 1 800"),
    des1=("what if the factory had", "e se a fábrica tivesse"), des2=("4 workers · 8 hours", "4 funcionários · 8 horas"),
    des3=("how many bricks a day?", "quantos tijolos por dia?"), comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["workers × hours", "output ÷ work hours = per hour", "per hour × new work hours"],
            ["funcionários × horas", "produção ÷ horas = por hora", "por hora × horas novas"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Ratio and", "proportion"), ("Proportional", "quantities"), ("Compound", "rule of three")],
           [("Razão e", "proporção"), ("Grandezas", "proporcionais"), ("Regra de três", "composta")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
    func=("workers", "funcionários"), horas=("hours", "horas"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("cento e cinquenta e dois", "152"), ("setecentos e vinte", "720"),
    ("mil e oitocentos", "1800"), ("mil e duzentos", "1200"), ("mil e oitenta", "1080"),
    ("dois mil quinhentos e vinte", "2520"), ("quarenta e cinco", "45"), ("cinco terços", "5/3"), ("três meios", "3/2")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))


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


def pessoa(c, x, y, s, cor, a):
    """ícone de funcionário: cabeça + tronco"""
    c.drawCircle(x, y - s * 0.28, s * 0.2, paint(cor, a))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - s * 0.3, y - s * 0.02, s * 0.6, s * 0.42), s * 0.18, s * 0.18),
                paint(cor, a))


def grade(c, cx, cy, lin, col, cel, a, k=1.0, cor=CYA, valor=None, kv=0.0, rotulos=True, cor_novo=None, base=None):
    """funcionários (linhas) × horas (colunas); lin/col podem ser fracionários (a grade crescendo);
    k = quanto da grade já foi pintado (em ordem de leitura); valor = texto em cada quadradinho (kv = alpha);
    base = (lin, col) da grade antiga: os quadradinhos fora dela ganham cor_novo"""
    if a <= 0:
        return
    nl, nc = math.ceil(lin - 1e-6), math.ceil(col - 1e-6)
    w, h = col * cel, lin * cel
    x0, y0 = cx - w / 2 + 30, cy - h / 2
    tot = max(1, nl * nc)
    for i in range(nl):
        fl = min(1.0, lin - i)
        for j in range(nc):
            fc = min(1.0, col - j)
            n = i * nc + j
            kc = a * ep(k * tot - n, 0, 1.0) * fl * fc
            if kc <= 0:
                continue
            novo = base is not None and (i >= base[0] or j >= base[1])
            cc = cor_novo if (novo and cor_novo) else cor
            r = skia.Rect.MakeXYWH(x0 + j * cel + 4, y0 + i * cel + 4, cel - 8, cel - 8)
            c.drawRRect(skia.RRect.MakeRectXY(r, 8, 8), paint(cc, 0.85 * kc))
            if valor and kv > 0:
                text_mid(c, valor, x0 + j * cel + cel / 2, y0 + i * cel + cel / 2, cel * 0.34, "black", BG0, kc * kv)
        if rotulos:
            pessoa(c, x0 - cel * 0.6, y0 + i * cel + cel / 2, cel * 0.8, WHITE, a * fl * 0.9)
    if rotulos:
        for j in range(nc):
            fc = min(1.0, col - j)
            text_mid(c, f"{j + 1}h", x0 + j * cel + cel / 2, y0 - cel * 0.4, cel * 0.3, "extrabold", INK2, a * fc)


def lista(c, itens, t, a, y0=260, dy=110, size=50, cx=RX):
    """linhas do quadro que aparecem no seu tempo: (texto, cor, t0, caixa)"""
    for j, (s, cor, t0, box) in enumerate(itens):
        k = a * ep(t, t0, 0.3)
        if k > 0:
            eq(c, [(s, cor)], y0 + j * dy, k, size, box=cor if box else None, maxw=820)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td, te = (C[f"01.{k}"] for k in "abcde")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao.png"), a, w=800, cx=LX, cy=520, hmax=640)
    popill(c, L["t_prop"], LX - 200, 900, 38, AMB, BG0, a * ep(t, te + 1.0, 0.3), t, te + 1.0)
    popill(c, L["t_hora"], LX + 200, 900, 38, CYA, BG0, a * ep(t, te + 2.4, 0.3), t, te + 2.4)
    board(c, a)
    label(c, L["enem"], RX, 240, a, 36, INK2, "extrabold")
    label(c, L["fab"], RX, 310, a, 46, WHITE, "black")
    eq(c, [(L["g1"], AMB)], 440, a * ep(t, ta + 10.4, 0.3), 42, maxw=820)
    eq(c, [(L["g2"], CYA)], 540, a * ep(t, tb + 0.6, 0.3), 42, maxw=820)
    eq(c, [(L["g3"], WHITE)], 640, a * ep(t, tc + 0.4, 0.3), 40, maxw=820)
    eq(c, [(L["pede"], MNT)], 790, a * ep(t, td + 0.6, 0.3), 52, box=MNT)


def b_proporcao(c, t, C, B):
    ta, tb, tc, td, te = (C[f"02.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_prop"], a)
    lin = 2 + 2 * ep(t, tc + 0.4, 0.8)        # dobra os funcionários
    col = 3 + 3 * ep(t, td + 0.4, 0.8)        # dobra as horas
    grade(c, LX, 580, lin, col, 90, a * ep(t, tb, 0.4), cor=AMB)
    board(c, a)
    lista(c, [(L["pr1"], WHITE, tb + 0.3, False), (L["pr2"], AMB, tc + 0.4, False), (L["pr3"], AMB, td + 0.4, False)],
          t, a, y0=290, dy=130, size=44)
    eq(c, [(L["pr4"], CYA)], 760, a * ep(t, te + 0.6, 0.3), 44, box=CYA, maxw=820)


def b_horas(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], d_out=0.01)
    header(c, L["s_horas"], a)
    k = ep(t, tb, 0.3) * (1 / 18) + ep(t, tc + 1.4, 3.0) * (17 / 18)   # um quadradinho; depois os 18
    grade(c, LX, 560, 3, 6, 110, a, k=k, cor=CYA)
    board(c, a)
    lista(c, [(L["h1"], WHITE, tb + 0.3, False)], t, a, y0=330, size=46)
    eq(c, [(L["h2"], CYA)], 560, a * ep(t, tc + 5.0, 0.3), 46, box=CYA, maxw=820)


def b_passo1(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"], d=0.01)
    header(c, L["s_p1"], a)
    grade(c, LX, 560, 3, 6, 110, a, cor=CYA, valor="40", kv=ep(t, td + 0.4, 0.5))
    board(c, a)
    lista(c, [(L["q1"], AMB, tb + 0.3, False), (L["q2"], WHITE, tc + 1.6, False)], t, a, y0=300, dy=160, size=46)
    eq(c, [(L["q3"], CYA)], 700, a * ep(t, td + 0.8, 0.3), 56, box=CYA)


def b_passo2(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], d=0.01, d_out=0.01)
    header(c, L["s_p2"], a)
    kg = ep(t, tb + 0.3, 2.4)
    grade(c, LX, 580, 3 + 2 * kg, 6 + 3 * kg, 82, a, cor=CYA, cor_novo=AMB, base=(3, 6))
    board(c, a)
    lista(c, [(L["n1"], WHITE, tb + 0.3, False)], t, a, y0=330, size=46)
    eq(c, [(L["n2"], CYA)], 560, a * ep(t, tc + 1.8, 0.3), 46, box=CYA, maxw=820)


def b_passo3(c, t, C, B):
    ta, tb, tc = (C[f"06.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"], d=0.01)
    header(c, L["s_p3"], a)
    kd = ep(t, tc + 2.0, 0.4)
    grade(c, LX, 580, 5, 9, 82, a, cor=MNT if kd > 0.5 else CYA, valor="40", kv=ep(t, tb + 0.6, 0.5))
    board(c, a)
    lista(c, [(L["m1"], WHITE, tb + 0.3, False)], t, a, y0=310, size=44)
    eq(c, [(L["m2"], MNT)], 500, a * ep(t, tc + 1.8, 0.3), 70, box=MNT)
    label(c, L["m3"], RX, 640, a * ep(t, tc + 2.6, 0.3), 46, WHITE, "black")


def b_confere(c, t, C, B):
    ta, tb, tc, td, te = (C[f"07.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_conf"], a)
    lin = 3 + 2 * ep(t, tb + 1.0, 1.0)
    col = 6 + 3 * ep(t, tc + 1.0, 1.0)
    grade(c, LX, 580, lin, col, 82, a, cor=CYA, cor_novo=AMB, base=(3, 6))
    board(c, a)
    lista(c, [(L["k1"], AMB, tb + 0.4, False), (L["k2"], AMB, tc + 0.4, False), (L["k3"], WHITE, td + 2.6, False)],
          t, a, y0=280, dy=130, size=44)
    eq(c, [(L["k4"], MNT)], 720, a * ep(t, te + 1.6, 0.3), 50, box=MNT, maxw=820)


def b_resposta(c, t, C, B):
    ta, tb = C["08.a"], C["08.b"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    grade(c, LX, 560, 5, 9, 82, a, cor=MNT, valor="40", kv=1.0)
    popill(c, "1 800", LX + 30, 880, 60, MNT, BG0, a * ep(t, ta + 1.4, 0.3), t, ta + 1.4)
    board(c, a)
    eq(c, [(L["r1"], MNT)], 300, a * ep(t, ta + 1.0, 0.3), 56)
    kc = a * ep(t, tb, 0.3)
    if kc > 0:
        for j, (le, v) in enumerate(zip("ABCDE", ("800", "1 080", "1 200", "1 800", "2 520"))):
            x = BX0 + 130 + j * 160
            ok = le == "D"
            c.drawCircle(x, 500, 34, paint(MNT if ok else INK2, kc))
            text_mid(c, le, x, 500, 36, "black", BG0, kc)
            text_mid(c, v, x, 575, 32, "black", MNT if ok else INK2, kc)
        check(c, BX0 + 130 + 3 * 160 + 38, 470, 18, kc)
        eq(c, [(L["alt"] + " ", WHITE), ("D", MNT)], 760, kc, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td, te = (C[f"09.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    # a grade de cada erro: C = 5 × 6, B = 3 × 9, E = 5 × 9 (mais a antiga)
    if t < tb:
        lin, col, cor = 5, 9, MNT
    elif t < tc:
        lin, col, cor = 5, 6, RED
    elif t < td:
        lin, col, cor = 3, 9, RED
    else:
        lin, col, cor = 5, 9, (RED if t < te else MNT)
    grade(c, LX, 580, lin, col, 82, a, cor=cor)
    if td <= t < te:
        popill(c, "+ 720", LX + 30, 880, 48, RED, BG0, a * ep(t, td + 3.2, 0.3), t, td + 3.2)
    board(c, a)
    linhas = (("A", L["pA"], RED, te + 0.2), ("B", L["pB"], RED, tc + 0.2), ("C", L["pC"], RED, tb + 0.2),
              ("D", L["pD"], MNT, ta), ("E", L["pE"], RED, td + 0.2))
    for j, (le, s, cor_, t0) in enumerate(linhas):
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        y = 270 + j * 140
        c.drawCircle(BX0 + 70, y, 32, paint(cor_, k))
        text_mid(c, le, BX0 + 70, y, 34, "black", BG0, k)
        sz = 36
        while text_w(s, "black", sz) > 720:
            sz -= 2
        text_mid(c, s, BX0 + 125, y, sz, "black", WHITE, k, align="left")


def b_desafio(c, t, C, B):
    ta, tb, tc, td = (C[f"10.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    grade(c, LX, 560, 4, 8, 90, a * ep(t, tb, 0.3), k=ep(t, tb + 0.3, 1.6), cor=AMB)
    popill(c, "?", LX + 30, 900, 60, AMB, BG0, a * ep(t, tc, 0.3), t, tc)
    board(c, a)
    label(c, L["des1"], RX, 300, a * ep(t, tb, 0.3), 46, WHITE, "black")
    eq(c, [(L["des2"], AMB)], 430, a * ep(t, tb + 1.2, 0.3), 54, box=AMB, maxw=820)
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
    """miniatura de cada aula: a : b · 2× → 2× · a grade"""
    if i == 2:
        grade(c, cx - 30, cy, 2, 3, 46, a, cor=MNT, rotulos=False)
        return
    s, cor = (("a : b", CYA), ("2× → 2×", AMB))[i]
    text_mid(c, s, cx, cy, 72, "black", cor, a)


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
            c.drawCircle(x, 790, 38, paint(MNT if v == "D" else INK2, kl, stroke=4))
            text_mid(c, v, x, 790, 38, "black", WHITE, kl)


BLOCKS = dict(gancho=b_gancho, proporcao=b_proporcao, horas=b_horas, passo1=b_passo1, passo2=b_passo2,
              passo3=b_passo3, confere=b_confere, resposta=b_resposta, pegadinhas=b_pegadinhas, desafio=b_desafio,
              resumo=b_resumo, aulas=b_aulas)
