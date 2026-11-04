"""Visual — Estudativo · Questão de Matemática 016 (aula horizontal 1920x1080): ENEM 2025, questão 140, o sódio por pacote.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = dado do rótulo (porções, mg por porção) e o produto da vez, ciano = a ferramenta (total =
por porção × porções), menta = o total certo e a resposta, coral = as pegadinhas (as gramas, o menor por porção, o
pacote mais leve).
Figura principal: os cinco rótulos em cartões numa coluna (rotulo()), com a faixa na cor do rótulo da prova; à direita
de cada cartão aparece o total do pacote (ou o peso do pacote, na pegadinha 2). coluna(..., u) desliza da ordem das
alternativas (u = 0) para a ordem crescente do total (u = 1)."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_016_matematica_sodio_cantina.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.d": "shimmer", "02.c": "confirm", "02.d": "confirm", "03.c": "deny", "04.b": "data", "04.c": "data",
        "04.d": "data", "04.e": "data", "04.f": "data", "05.b": "whoosh", "05.c": "impact", "06.b": "alert", "06.c": "deny",
        "06.d": "alert", "07.a": "data", "07.b": "lock", "09.a": "shimmer", "09.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo (só os efeitos)

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 016", "QUESTÃO DE MATEMÁTICA · 016"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_ferr=("THE TOOL · PER SERVING × PER PACK", "A FERRAMENTA · POR PORÇÃO × POR PACOTE"),
    s_dados=("STEP 1 · WHAT MATTERS", "PASSO 1 · O QUE IMPORTA"), s_contas=("STEP 2 · TOTAL PER PACK", "PASSO 2 · O TOTAL DE CADA PACOTE"),
    s_comp=("STEP 3 · COMPARE", "PASSO 3 · COMPARAR"), s_peg=("THE TRAPS", "AS PEGADINHAS"),
    s_gen=("CURIOSITY · AND A CHALLENGE", "CURIOSIDADE · E UM DESAFIO"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 140", "ENEM 2025 · questão 140"),
    cinco=("5 snacks", "5 alimentos"), rotulo=("label: sodium PER SERVING", "rótulo: sódio POR PORÇÃO"),
    pede=("question: LEAST sodium", "pergunta: MENOR sódio"), pacote=("PER PACK", "POR PACOTE"),
    escolha=("choice = ", "escolha = "), p_ferr=("PER SERVING × PER PACK", "POR PORÇÃO × POR PACOTE"), p_peg=("2 TRAPS", "2 PEGADINHAS"),
    um=("label → 1 serving", "rótulo → 1 porção"), varias=("pack → several equal servings", "pacote → várias porções iguais"),
    total=("total = per serving × servings", "total = por porção × porções"), porcao=("serving", "porção"),
    usa1=("number of servings", "nº de porções"), usa2=("mg of sodium per serving", "mg de sódio por porção"),
    gramas=("grams per serving", "gramas da porção"), peso=("weight ≠ sodium", "peso ≠ sódio"), fora=("not in the math", "fora da conta"),
    ordem=("smallest → largest", "do menor para o maior"), menor=("least = ", "menor = "),
    peg1=("1 · looking only PER SERVING", "1 · olhar só POR PORÇÃO"), peg2=("2 · the LIGHTEST pack", "2 · o pacote mais LEVE"),
    menor_porcao=("least per serving: 166 → E ?", "menor por porção: 166 → E ?"),
    leve=("lightest: 4 × 20 g = 80 g", "mais leve: 4 × 20 g = 80 g"), leve2=("light ≠ little sodium", "leve ≠ pouco sódio"),
    oms=("WHO: adults < 2,000 mg / day", "OMS: adulto < 2.000 mg / dia"), oms_fonte=("World Health Organization", "Organização Mundial da Saúde"),
    desafio=("water crackers with 3 servings?", "água e sal com 3 porções?"), muda=("would her choice change?", "a escolha mudaria?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["keep: servings and mg per serving", "multiply: total of each pack", "least total: 510 mg → chips (A)",
             "not least per serving, not the lightest"],
            ["usar: porções e mg por porção", "multiplicar: o total de cada pacote", "menor total: 510 mg → chips (A)",
             "nem o menor por porção, nem o mais leve"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Ratio and", "proportion"), ("Proportional", "quantities"), ("Comparing", "offers")],
           [("Razão e", "proporção"), ("Grandezas", "proporcionais"), ("Comparação de", "propostas")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("dois mil cento e doze", "2.112"), ("dois mil e quatro", "2.004"),
    ("dois mil", "2.000"), ("mil e seiscentos", "1.600"), ("mil e cinquenta", "1.050"), ("miligramas", "mg"),
    ("vezes dois", "× 2"), ("passo dois", "Passo 2"), ("passo três", "Passo 3")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("pacote", "mais"), ("consuma", "menos")}
n_ = lambda s: s.replace(".", "#").replace(",", ".").replace("#", ",") if EN else s   # noqa: E731  troca , e . no inglês


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- figuras
# (nome, porções, gramas por porção, mg de sódio por porção, alternativa, cor do rótulo na prova)
PROD = [("Batata chips", 3, 50, 170, "A", "#8FD3F4"), ("Palitos salgados", 4, 20, 501, "B", "#9BD3AE"),
        ("Biscoito multigrãos", 8, 25, 264, "C", "#B8B3D8"), ("Biscoito de polvilho", 6, 15, 175, "D", "#F7BBA6"),
        ("Biscoito de água e sal", 5, 40, 166, "E", "#FFF59D")]
NOMES_EN = ["Potato chips", "Salted sticks", "Multigrain crackers", "Tapioca biscuits", "Water crackers"]
TOT = [p * s for _, p, _, s, _, _ in PROD]                       # 510, 2004, 2112, 1050, 830
ORDEM = sorted(range(5), key=lambda i: TOT[i])                     # chips, água e sal, polvilho, palitos, multigrãos
POS = {i: k for k, i in enumerate(ORDEM)}
CW, CH, PASSO_Y, Y0 = 790, 120, 142, 255                           # cartão: largura, altura; coluna: passo e topo
mg = lambda v: n_(f"{v:,}".replace(",", ".")) + " mg"              # noqa: E731  2004 → "2.004 mg"


def nome(i):
    return NOMES_EN[i] if EN else PROD[i][0]


def rotulo(c, i, x, y, a, borda=INK2, glow=0.0, total=0.0, cor_t=MNT, riscar=0.0, peso=0.0, cor_s=AMB, s=None):
    """cartão do rótulo i: faixa colorida + letra, nome, '3 porções de 50 g · 170 mg/porção'; à direita, o total do
    pacote (total = alfa) ou o peso do pacote (peso = alfa). riscar = 0..1 risca as gramas. (x, y) = centro"""
    if a <= 0:
        return
    nm, p, g, sd, le, cor = PROD[i]
    sd = s if s is not None else sd
    x0, y0 = x - CW / 2, y - CH / 2
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, y0, CW, CH), 18, 18)
    if glow > 0:
        c.drawRRect(r, blur_paint(borda, 0.5 * a * glow, 16))
    c.drawRRect(r, paint(BG1, 0.95 * a))
    c.save(); c.clipRRect(r, doAntiAlias=True)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, 16, CH), paint(cor, a))
    c.restore()
    c.drawRRect(r, paint(borda, a, stroke=3))
    c.drawCircle(x0 + 58, y, 26, paint(cor, a))
    text_mid(c, le, x0 + 58, y, 30, "black", BG0, a)
    text_mid(c, nome(i), x0 + 104, y - 25, 34, "black", WHITE, a, align="left")
    por = "servings of" if EN else "porções de"
    s1, s2, s3 = f"{p} ", f"{por} ", f"{g} g"
    xx = x0 + 104
    text_mid(c, s1, xx, y + 25, 29, "black", AMB, a, align="left"); xx += text_w(s1, "black", 29)
    text_mid(c, s2, xx, y + 25, 29, "semibold", INK2, a, align="left"); xx += text_w(s2, "semibold", 29)
    xg = xx
    text_mid(c, s3, xx, y + 25, 29, "semibold", INK2, a * (1 - 0.6 * riscar), align="left"); xx += text_w(s3, "semibold", 29)
    if riscar > 0:
        c.drawLine(xg - 4, y + 25, xg - 4 + (xx - xg + 8) * ease_io(riscar), y + 25, paint(RED, a, stroke=4, cap_round=True))
    s4 = f"  ·  {sd} mg"
    text_mid(c, s4, xx, y + 25, 29, "black", cor_s, a, align="left")
    if total > 0:
        text_mid(c, mg(p * sd), x0 + CW - 26, y - 22, 40, "black", cor_t, a * total, align="right")
        text_mid(c, "no pacote" if not EN else "per pack", x0 + CW - 26, y + 22, 24, "semibold", INK2, a * total, align="right")
    if peso > 0:
        text_mid(c, f"{p * g} g", x0 + CW - 26, y - 22, 40, "black", cor_t, a * peso, align="right")
        text_mid(c, "o pacote pesa" if not EN else "pack weight", x0 + CW - 26, y + 22, 24, "semibold", INK2, a * peso, align="right")


def coluna(c, a, u=0.0, estilo=None, x=LX - 12, y0=Y0, passo=PASSO_Y):
    """os cinco cartões; u = 0: ordem das alternativas (A..E), u = 1: ordem crescente do total.
    estilo(i) → kwargs de rotulo() para o cartão i"""
    for i in range(5):
        uu = ease_io(clamp(u * 1.3 - 0.3 * (i / 4)))
        y = y0 + passo * (i + (POS[i] - i) * uu)
        dx = 60 * math.sin(math.pi * uu) * (1 if POS[i] > i else -1) if POS[i] != i else 0
        rotulo(c, i, x + dx, y, a, **((estilo(i) if estilo else None) or {}))


def bolinha(c, x, y, v, a, col=INK2, fundo=BG1, glow=0.0, k=1.0, size=None):
    """texto curto numa bolinha"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    if glow:
        c.drawCircle(0, 0, 46, blur_paint(col, 0.5 * a * glow, 14))
    c.drawCircle(0, 0, 42, paint(fundo, 0.95 * a))
    c.drawCircle(0, 0, 42, paint(col, a, stroke=4))
    text_mid(c, str(v), 0, 0, size or (40 if len(str(v)) < 3 else 30), "black", WHITE, a)
    c.restore()


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


def _y(k, y0=Y0, passo=PASSO_Y):
    return y0 + passo * k


def opcoes(c, a, t, t0, certa="A", erradas=()):
    """linha A B C D E no pé do quadro, com a certa em caixa menta e as erradas riscadas"""
    for j, le in enumerate("ABCDE"):
        x = BX0 + 130 + j * 160
        k = a * ep(t, t0 + j * 0.08, 0.2)
        col = MNT if le == certa else (RED if le in erradas else INK2)
        text_mid(c, le, x, 800, 48, "black", col, k)
        if le in erradas:
            cross(c, x, 800, 30, k * ep(t, t0 + 0.6, 0.2))
    kk = a * ep(t, t0 + 0.6, 0.3)
    if kk > 0 and certa:
        j = "ABCDE".index(certa)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 130 + j * 160 - 46, 800 - 44, 92, 88), 18, 18)
        c.drawRRect(r, paint(MNT, kk, stroke=4))


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    label(c, L["cinco"], RX, 345, a, 50, AMB, "black")
    label(c, L["rotulo"], RX, 445, a * ep(t, tb, 0.3), 40, WHITE, "black")
    eq(c, [(L["pede"].split(":")[0] + ": ", INK2), (L["pede"].split(": ")[1], CYA)], 545, a * ep(t, tc, 0.3), 44)
    label(c, L["pacote"], RX, 615, a * ep(t, tc + 2.6, 0.3), 46, CYA, "black")
    eq(c, [(L["escolha"], WHITE), ("?", CYA)], 735, a * ep(t, td, 0.3), 60, box=CYA)
    kd = a * ep(t, td + 2.2, 0.3)
    popill(c, L["p_ferr"], RX - 170, 850, 26, CYA, BG0, kd, t, td + 2.4)
    popill(c, L["p_peg"], RX + 270, 850, 26, RED, BG0, kd, t, td + 4.6)


def pacote(c, cx, cy, n, a, t, t_in, col=AMB, val=100, kt=0.0):
    """um pacote (caixa) com n porções iguais (bolinhas 'val mg'), entrando uma a uma a partir de t_in"""
    if a <= 0:
        return
    w, h = 140 + 150 * n, 230
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 30, 30)
    c.drawRRect(r, paint(BG1, 0.9 * a))
    c.drawRRect(r, paint(col, a, stroke=4))
    label(c, ("PACK" if EN else "PACOTE"), cx, cy - h / 2 - 34, a, 30, col, "black")
    for j in range(n):
        x = cx - (n - 1) * 75 + j * 150
        bolinha(c, x, cy, val, a, MNT if kt > 0 else CYA, glow=kt, k=pop(t, t_in + j * 0.5, 0.3), size=34)
        label(c, "mg", x, cy + 70, a * ep(t, t_in + j * 0.5, 0.3), 26, INK2, "bold")


def b_ferramenta(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ferr"], a)
    kb = a * ep(t, tb, 0.3)
    k0 = a * (1 - ep(t, tb, 0.3))   # abertura: os dois conceitos lado a lado
    popill(c, L["p_ferr"].split(" × ")[0], LX, 420, 44, AMB, BG0, k0, t, ta + 1.2)
    label(c, "≠", LX, 540, k0 * ep(t, ta + 1.8, 0.3), 60, WHITE, "black")
    popill(c, L["p_ferr"].split(" × ")[1], LX, 660, 44, CYA, BG0, k0, t, ta + 2.4)
    # 1 porção (o rótulo) → pacote com várias
    if t < tc + 0.5:
        k1 = kb * (1 - ep(t, tc, 0.4))
        bolinha(c, LX, 400, 100, k1, CYA, glow=1.0, size=34)
        label(c, L["porcao"], LX, 480, k1, 32, CYA, "black")
        label(c, "mg", LX, 400 + 70, 0, 26, INK2, "bold")
    kp = a * ep(t, tc, 0.4)
    if kp > 0:
        pacote(c, LX, 470, 2, kp, t, tc + 0.2, kt=ep(t, td + 3.0, 0.3))
        kr = kp * ep(t, td + 3.0, 0.3)
        label(c, "= " + mg(200), LX, 700, kr, 64, MNT, "black")
    board(c, a)
    label(c, L["um"], RX, 280, a * ep(t, tb, 0.3), 42, WHITE, "black")
    label(c, L["varias"], RX, 370, a * ep(t, tb + 2.0, 0.3), 38, INK2, "bold")
    eq(c, [(L["total"], CYA)], 500, a * ep(t, tc + 1.0, 0.3), 46, box=CYA)
    eq(c, [("100 × 2 = ", WHITE), ("200 mg", MNT)], 680, a * ep(t, td + 1.5, 0.3), 64, box=MNT)


def b_dados(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_dados"], a)
    kr = ep(t, tc + 2.6, 0.8)
    kb = ep(t, tb + 0.4, 0.3)
    coluna(c, a, 0, lambda i: dict(borda=AMB if kb > 0 and kr == 0 else INK2, glow=0.4 * kb * (1 - kr), riscar=kr))
    board(c, a)
    kb1 = a * ep(t, tb + 1.6, 0.3)
    kb2 = a * ep(t, tb + 3.4, 0.3)
    for y, s, k in ((300, L["usa1"], kb1), (400, L["usa2"], kb2)):
        if k > 0:
            check(c, BX0 + 90, y, 22, k)
            text_mid(c, s, BX0 + 140, y, 44, "black", AMB, k, align="left")
    kc = a * ep(t, tc, 0.3)
    if kc > 0:
        cross(c, BX0 + 90, 560, 22, kc, RED)
        text_mid(c, L["gramas"], BX0 + 140, 560, 44, "black", RED, kc, align="left")
        label(c, L["peso"], RX, 680, a * ep(t, tc + 3.6, 0.3), 46, WHITE, "black")
        popill(c, L["fora"], RX, 790, 32, RED, BG0, a * ep(t, tc + 6.0, 0.3), t, tc + 6.0)


# contas da cena 04, por produto: (linhas parciais, total); cada linha = texto da conta
CONTAS = [([("3 × 170", "")], 510),
          ([("4 × 500 = ", "2.000"), ("4 × 1 = ", "4")], 2004),
          ([("8 × 200 = ", "1.600"), ("8 × 64 = ", "512")], 2112),
          ([("6 × 100 = ", "600"), ("6 × 75 = ", "450")], 1050),
          ([("5 × 100 = ", "500"), ("5 × 66 = ", "330")], 830)]


def b_contas(c, t, C, B):
    ts = [C[f"04.{k}"] for k in "bcdef"]
    ta = C["04.a"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_contas"], a)
    fins = ts[1:] + [B["end"]]
    atual = max([j for j, t0 in enumerate(ts) if t >= t0], default=-1)

    def est(i):
        if i == atual:
            return dict(borda=AMB, glow=1.0, total=ep(t, ts[i] + 0.8 * (fins[i] - ts[i]), 0.3))
        if i < atual:
            return dict(borda=MNT, total=1.0)
        return None
    coluna(c, a, 0, est)
    board(c, a)
    label(c, L["total"], RX, 260, a * ep(t, ta + 0.6, 0.3), 36, CYA, "black")
    for j, t0 in enumerate(ts):
        t1 = fins[j]
        kj = a * ep(t, t0, 0.3) * (1 - ep(t, t1 - 0.2, 0.3) if j < 4 else 1)
        if kj <= 0:
            continue
        sp = t1 - t0
        _, p, _, s, le, cor = PROD[j]
        label(c, nome(j), RX, 370, kj, 44, AMB, "black")
        eq(c, [(f"{p} × {s}", WHITE)], 470, kj * ep(t, t0 + 0.2 * sp, 0.3), 56)
        linhas, tot = CONTAS[j]
        if len(linhas) > 1:
            for q, (s1, s2) in enumerate(linhas):
                eq(c, [(s1, INK2), (n_(s2), WHITE)], 570 + q * 80, kj * ep(t, t0 + (0.38 + 0.2 * q) * sp, 0.3), 44)
        eq(c, [("= ", WHITE), (mg(tot), MNT)], 790, kj * ep(t, t0 + 0.8 * sp, 0.3), 68, box=MNT)


@lru_cache(None)
def _leitura():
    """instantes (absolutos) em que a voz lê os cinco totais em ordem (cena 05): tirados das palavras do Whisper
    (analise/voz.json, parte 2, que começa na cena 05), deslocados para o vídeo pelo "Passo" que abre a cena"""
    import json
    from pathlib import Path
    raiz = Path(__file__).resolve().parent.parent
    tp = json.loads((raiz / "audio" / "tempos.json").read_text(encoding="utf-8"))
    sc = next(x for x in tp["scenes"] if x["id"] == "05")
    ws = json.loads((raiz / "analise" / "voz.json").read_text(encoding="utf-8"))[1]["words"]
    desl = sc["start"] + sc["cues"]["a"] - ws[0]["s"]
    out, j = [], 0
    for v in ("510", "830", "1050", "2004", "2112"):
        while j < len(ws) and ws[j]["w"].strip(",.").replace(" ", "") != v:
            j += 1
        if j == len(ws):
            return []
        out.append(ws[j]["s"] + desl); j += 1
    return out


def b_comparar(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_comp"], a)
    u = prog(t, ta + 1.2, 1.8)
    kc = ep(t, tc, 0.3)
    coluna(c, a, u, lambda i: dict(borda=MNT if (i == 0 and kc > 0) else INK2, glow=kc if i == 0 else 0, total=1.0,
                                     cor_t=MNT if i == 0 else WHITE))
    board(c, a)
    label(c, L["ordem"], RX, 260, a * ep(t, ta + 0.8, 0.3), 40, INK2, "bold")
    for q, i in enumerate(ORDEM):
        lt = _leitura()
        tq = lt[q] if len(lt) == 5 else tb + 0.9 + q * 1.15
        k = a * ep(t, tq, 0.3)
        y = 340 + q * 64
        col = MNT if i == 0 and kc > 0 else WHITE
        text_mid(c, mg(TOT[i]), RX - 40, y, 40, "black", col, k, align="right")
        text_mid(c, PROD[i][4], RX + 10, y, 36, "black", AMB, k, align="left")
    opcoes(c, a, t, tc + 2.2)


def b_pegadinha(c, t, C, B):
    ta, tb, tc, td = (C[f"06.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    kb = ep(t, tb, 0.3)
    kc = ep(t, tc, 0.3)
    kd = ep(t, td, 0.3)

    def est(i):
        if kd > 0:
            return dict(borda=RED if i == 1 else INK2, glow=kd if i == 1 else 0, peso=ep(t, td + 2.0, 0.3),
                        cor_t=RED if i == 1 else WHITE)
        if kc > 0:
            if i in (0, 4):
                return dict(borda=MNT if i == 0 else RED, glow=1.0, total=kc, cor_t=MNT if i == 0 else RED)
            return None
        if kb > 0 and i == 4:
            return dict(borda=RED, glow=kb, cor_s=RED)
        return None
    coluna(c, a, 0, est)
    board(c, a)
    k1 = a * ep(t, ta + 1.2, 0.3) * (1 - kd)
    if k1 > 0:
        label(c, L["peg1"], RX, 270, k1, 42, RED, "black")
        pos = eq(c, [(L["menor_porcao"], WHITE)], 400, k1 * kb, 44)
        if pos:
            strike(c, pos[0][0], pos[-1][1], 400, k1, ep(t, tc + 0.5, 0.4))
        eq(c, [("5 × 166 = ", INK2), ("830 mg", RED)], 540, k1 * ep(t, tc + 0.6, 0.3), 50)
        eq(c, [("3 × 170 = ", INK2), ("510 mg", MNT)], 650, k1 * ep(t, tc + 3.8, 0.3), 50, box=MNT)
        opcoes(c, k1, t, tc + 4.5, "A", ("E",))
    k2 = a * kd
    if k2 > 0:
        label(c, L["peg2"], RX, 270, k2, 42, RED, "black")
        eq(c, [(L["leve"], WHITE)], 400, k2 * ep(t, td + 2.0, 0.3), 44)
        eq(c, [("4 × 501 = ", INK2), ("2.004 mg" if not EN else "2,004 mg", RED)], 530, k2 * ep(t, td + 4.2, 0.3), 54)
        label(c, L["leve2"], RX, 680, k2 * ep(t, td + 6.4, 0.3), 50, WHITE, "black")
        opcoes(c, k2, t, td + 4.6, "A", ("B",))


def barras(c, a, t, t0, lim=2000):
    """os cinco totais em barras horizontais, com a linha da recomendação da OMS (2.000 mg)"""
    x0, esc = 330, 470 / 2200
    curto = ["Chips", "Palitos", "Multigrãos", "Polvilho", "Água e sal"] if not EN else ["Chips", "Sticks", "Multigrain", "Tapioca", "Water"]
    for q, i in enumerate(range(5)):
        y = 300 + q * 120
        k = a * ep(t, t0 + q * 0.15, 0.3)
        if k <= 0:
            continue
        acima = TOT[i] > lim
        text_mid(c, PROD[i][4], x0 - 230, y, 36, "black", AMB, k)
        text_mid(c, curto[i], x0 - 190, y, 30, "bold", WHITE, k, align="left")
        w = TOT[i] * esc * ease_io(prog(t, t0 + q * 0.15, 0.8))
        rrect(c, x0, y - 26, max(w, 1), 52, 12, RED if acima else MNT, k)
        text_mid(c, mg(TOT[i]), x0 + w + 16, y, 30, "black", WHITE, k * ep(t, t0 + 0.8 + q * 0.15, 0.3), align="left")
    kl = a * ep(t, t0 + 1.4, 0.3)
    if kl > 0:
        xl = x0 + lim * esc
        pd = paint(AMB, kl, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
        c.drawLine(xl, 230, xl, 840, pd)
        label(c, "2.000 mg" if not EN else "2,000 mg", xl, 205, kl, 30, AMB, "black")


def b_generaliza(c, t, C, B):
    ta, tb = (C[f"07.{k}"] for k in "ab")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    ka = a * (1 - ep(t, tb, 0.3))
    if ka > 0:
        barras(c, ka, t, ta + 0.3)
    kb = a * ep(t, tb, 0.3)
    if kb > 0:   # o desafio: água e sal com 3 porções
        k3 = ep(t, tb + 2.0, 0.4)
        rotulo(c, 4, LX - 12, 420, kb, borda=AMB, glow=1.0)
        if k3 > 0:
            popill(c, "5 → 3 ?", LX, 560, 40, AMB, BG0, kb * k3, t, tb + 2.0)
        rotulo(c, 0, LX - 12, 700, kb * ep(t, tb + 4.0, 0.3), borda=MNT, total=1.0)
    board(c, a)
    if ka > 0:
        label(c, L["oms_fonte"], RX, 300, ka * ep(t, ta + 0.6, 0.3), 36, INK2, "bold")
        eq(c, [(L["oms"], AMB)], 400, ka * ep(t, ta + 2.0, 0.3), 46, box=AMB)
        eq(c, [("B: ", INK2), ("2.004 mg" if not EN else "2,004 mg", RED)], 540, ka * ep(t, ta + 5.6, 0.3), 46)
        eq(c, [("C: ", INK2), ("2.112 mg" if not EN else "2,112 mg", RED)], 630, ka * ep(t, ta + 6.4, 0.3), 46)
    if kb > 0:
        label(c, L["desafio"], RX, 330, kb * ep(t, tb + 1.0, 0.3), 44, AMB, "black")
        label(c, L["muda"], RX, 470, kb * ep(t, tb + 4.4, 0.3), 50, WHITE, "black")
        label(c, L["comenta"], RX, 640, kb * ep(t, tb + 6.0, 0.3), 40, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"08.{k}"] for k in "bcde"]
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
    """miniatura de cada aula: fração a/b · reta de grandezas proporcionais · duas ofertas com a melhor marcada"""
    if i == 0:
        text_mid(c, "a", cx, cy - 50, 64, "black", CYA, a)
        c.drawLine(cx - 50, cy, cx + 50, cy, paint(WHITE, a, stroke=6, cap_round=True))
        text_mid(c, "b", cx, cy + 52, 64, "black", CYA, a)
    elif i == 1:
        c.drawLine(cx - 110, cy + 70, cx + 110, cy + 70, paint(INK2, a, stroke=4))
        c.drawLine(cx - 110, cy + 70, cx - 110, cy - 80, paint(INK2, a, stroke=4))
        c.drawLine(cx - 110, cy + 70, cx + 90, cy - 70, paint(AMB, a, stroke=6, cap_round=True))
        for j in range(1, 4):
            c.drawCircle(cx - 110 + j * 50, cy + 70 - j * 35, 9, paint(WHITE, a))
    else:
        for j, col in enumerate((INK2, MNT)):
            rrect(c, cx - 120 + j * 125, cy - 70, 115, 140, 12, BG2, a)
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 120 + j * 125, cy - 70, 115, 140), 12, 12), paint(col, a, stroke=3))
        check(c, cx + 67, cy, 26, a)


def b_aulas(c, t, C, B):
    """convite para as aulas do assunto no canal (toda questão termina assim) + CTA"""
    ta, tb, tc, td, te, tf = (C[f"09.{k}"] for k in "abcdef")
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
        for j, v in enumerate("ABCDE"):
            bolinha(c, 960 - 280 + j * 140, 790, v, kl, MNT if j == 0 else INK2, glow=1.0 if j == 0 else 0, k=0.9)


BLOCKS = dict(gancho=b_gancho, ferramenta=b_ferramenta, dados=b_dados, contas=b_contas, comparar=b_comparar,
              pegadinha=b_pegadinha, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
