"""Visual — Estudativo · Questão de Matemática 014 (aula horizontal 1920x1080): ENEM 2025, questão 139, a mediana das velocidades.
Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = dado do problema (as velocidades do quadro) e a moda, ciano = incógnita (a mediana) e o meio
da lista, menta = resultado conferido, coral = a pegadinha (o meio da tabela sem ordenar).
Figura principal: as dez velocidades em fichas numa coluna (ficha()), que deslizam da ordem do quadro para a ordem
crescente (coluna(..., u) com u de 0 a 1)."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_014_matematica_mediana_velocidade.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.d": "shimmer", "02.b": "confirm", "02.d": "confirm", "03.b": "whoosh", "04.c": "confirm", "05.b": "impact",
        "05.c": "confirm", "06.b": "alert", "06.c": "deny", "07.b": "data", "07.c": "data", "07.e": "confirm",
        "08.b": "confirm", "08.c": "lock", "10.a": "shimmer", "10.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo (só os efeitos)

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 014", "QUESTÃO DE MATEMÁTICA · 014"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_ferr=("THE TOOL · THE MEDIAN", "A FERRAMENTA · A MEDIANA"),
    s_ord=("STEP 1 · PUT THEM IN ORDER", "PASSO 1 · COLOCAR EM ORDEM"), s_meio=("STEP 2 · FIND THE MIDDLE", "PASSO 2 · ACHAR O MEIO"),
    s_med=("STEP 3 · THE MEDIAN", "PASSO 3 · A MEDIANA"), s_peg=("THE TRAP · FORGETTING TO SORT", "A PEGADINHA · ESQUECER DE ORDENAR"),
    s_outras=("THE OTHER OPTIONS · OTHER MEASURES", "AS OUTRAS ALTERNATIVAS · OUTRAS MEDIDAS"),
    s_gen=("WHAT IF THE COUNT IS ODD?", "E SE A QUANTIDADE FOR ÍMPAR?"), s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 139", "ENEM 2025 · questão 139"),
    dez=("10 cities", "10 cidades"), regra=("new standard = MEDIAN", "novo padrão = MEDIANA"), mbs=("values in MB/s", "valores em MB/s"),
    veloc=("speed = ", "velocidade = "),
    p_med=("MEDIAN", "MEDIANA"), p_outras=("MEAN · MODE", "MÉDIA · MODA"),
    meio_def=("median = the MIDDLE value", "mediana = o valor do MEIO"), ordem=("of the list IN ORDER", "da lista EM ORDEM"),
    impar=("odd count: 1 in the middle", "quantidade ímpar: 1 no meio"), par=("even count: mean of the 2 in the middle", "quantidade par: média dos 2 do meio"),
    crescente=("smallest → largest", "da menor para a maior"), repete=("repeated values count every time", "repetido entra todas as vezes"),
    dez_par=("10 values → EVEN", "10 valores → PAR"), meio56=("middle: 5th and 6th", "meio: 5º e 6º"),
    antes=("5 before", "5 antes"), depois=("5 after", "5 depois"),
    quinto=("5th = 380   ·   6th = 380", "5º = 380   ·   6º = 380"),
    mediana_eq=("median = ", "mediana = "),
    sem_ordem=("WITHOUT sorting:", "SEM ordenar:"), tabela=("5th and 6th of the TABLE", "5ª e 6ª cidade do QUADRO"),
    nao_meio=("middle of the table ≠ middle of the values", "meio da tabela ≠ meio dos valores"),
    media=("mean", "média"), moda=("mode", "moda"), maior=("largest", "maior"), mediana=("median", "mediana"),
    soma=("sum = 3,700", "soma = 3.700"), vezes3=("3 times", "3 vezes"),
    onze=("11 values → ODD", "11 valores → ÍMPAR"), meio6=("middle = 6th value", "meio = 6º valor"), nova=("new city", "nova cidade"),
    desafio=("C3: 320 → 420 ?", "C3: 320 → 420 ?"), qual=("what would the median be?", "qual seria a mediana?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["put the 10 speeds in order", "10 is even: middle = 5th and 6th", "(380 + 380) ÷ 2 = 380  (C)",
             "not the mean, the mode or the largest"],
            ["colocar as 10 velocidades em ordem", "10 é par: meio = 5º e 6º", "(380 + 380) ÷ 2 = 380  (C)",
             "não é a média, nem a moda, nem o maior"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("", "The mean"), ("Mode and", "median"), ("Reading", "tables")],
           [("", "Média aritmética"), ("Moda e", "mediana"), ("Leitura de", "tabelas")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
_EXTRA = [] if EN else [
    ("dois mil e vinte e cinco", "2025"), ("três mil e setecentos", "3.700"), ("megabytes por segundo", "MB/s"),
    ("dividido por", "÷"), ("cidade três", "C3"), ("quinto", "5º"), ("sexto", "6º")]
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
matematica.EXPRESSOES |= {("são", "dez"), ("a", "quinta"), ("a", "sexta"), ("as", "vezes"), ("três", "vezes")}
n_ = lambda s: s.replace(".", "#").replace(",", ".").replace("#", ",") if EN else s   # noqa: E731  troca , e . no inglês


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- figuras
VALS = [390, 380, 320, 390, 340, 380, 390, 400, 350, 360]          # C1..C10, como no quadro
ORDEM = sorted(range(10), key=lambda i: (VALS[i], i))               # índices em ordem crescente
POS = {i: k for k, i in enumerate(ORDEM)}                           # posição de cada cidade na lista ordenada
FW, FH, PASSO_Y, Y0 = 330, 54, 64, 228                              # ficha: largura, altura; coluna: passo e topo


def ficha(c, x, y, cidade, v, a, borda=INK2, fundo=BG1, cor_v=WHITE, glow=0.0, k=1.0):
    """ficha de uma cidade: 'C3' à esquerda, a velocidade à direita; (x, y) = centro"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-FW / 2, -FH / 2, FW, FH), 16, 16)
    if glow > 0:
        c.drawRRect(r, blur_paint(borda, 0.5 * a * glow, 14))
    c.drawRRect(r, paint(fundo, 0.95 * a))
    c.drawRRect(r, paint(borda, a, stroke=3))
    if cidade:
        text_mid(c, cidade, -FW / 2 + 26, 0, 28, "bold", INK2, a, align="left")
    text_mid(c, str(v), FW / 2 - 26, 0, 38, "black", cor_v, a, align="right")
    c.restore()


def coluna(c, a, u, estilo=None, x=LX, y0=Y0, passo=PASSO_Y, extra=None, vals=None):
    """as dez fichas; u = 0: ordem do quadro, u = 1: ordem crescente (cada ficha desliza da linha i para POS[i]).
    estilo(i, k) → dict(borda, fundo, cor_v, glow) para a ficha da cidade i que está na posição k da lista ordenada.
    extra = (rótulo, valor) de uma 11ª ficha no fim da lista."""
    vals = vals or VALS
    ordem = sorted(range(len(vals)), key=lambda i: (vals[i], i))
    pos = {i: k for k, i in enumerate(ordem)}
    for i, v in enumerate(vals):
        uu = ease_io(clamp(u * 1.4 - 0.4 * (i / 9)))    # deslizam um pouco escalonadas
        y = y0 + passo * (i + (pos[i] - i) * uu)
        dx = 70 * math.sin(math.pi * uu) * (1 if (pos[i] - i) > 0 else -1) if pos[i] != i else 0
        st = dict(borda=INK2, fundo=BG1, cor_v=WHITE, glow=0.0)
        if estilo:
            st.update(estilo(i, pos[i]) or {})
        ficha(c, x + dx, y, f"C{i + 1}", v, a, **st)
    if extra:
        ficha(c, x, y0 + passo * len(vals), extra[0], extra[1], a, borda=MNT, cor_v=MNT)


def chave(c, x, y0, y1, s, a, col=INK2, lado=1):
    """chave vertical de y0 a y1 ao lado de x, com rótulo"""
    if a <= 0:
        return
    pth = skia.Path(); m = (y0 + y1) / 2; d = 18 * lado
    pth.moveTo(x, y0); pth.quadTo(x + d, y0, x + d, y0 + 20); pth.lineTo(x + d, m - 14); pth.quadTo(x + d, m, x + 2 * d, m)
    pth.quadTo(x + d, m, x + d, m + 14); pth.lineTo(x + d, y1 - 20); pth.quadTo(x + d, y1, x, y1)
    c.drawPath(pth, paint(col, a, stroke=3.5, cap_round=True))
    label(c, s, x + 2 * d + 14 * lado, m, a, 30, col, "black", "left" if lado > 0 else "right")


def bolinha(c, x, y, v, a, col=INK2, fundo=BG1, glow=0.0, k=1.0):
    """número numa bolinha (exemplos da ferramenta)"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    if glow:
        c.drawCircle(0, 0, 46, blur_paint(col, 0.5 * a * glow, 14))
    c.drawCircle(0, 0, 42, paint(fundo, 0.95 * a))
    c.drawCircle(0, 0, 42, paint(col, a, stroke=4))
    text_mid(c, str(v), 0, 0, 40 if v < 100 else 30, "black", WHITE, a)
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


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_enunciado(c, a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    label(c, L["dez"], RX, 350, a, 50, AMB, "black")
    eq(c, [(L["regra"].split("=")[0] + "= ", WHITE), (L["regra"].split("= ")[1], CYA)], 460, a * ep(t, tb, 0.3), 52)
    label(c, L["mbs"], RX, 560, a * ep(t, tc, 0.3), 40, INK2, "bold")
    eq(c, [(L["veloc"], WHITE), ("?", CYA)], 680, a * ep(t, td, 0.3), 60, box=CYA)
    kd = a * ep(t, td + 2.0, 0.3)
    popill(c, L["p_med"], RX, 800, 30, CYA, BG0, kd, t, td + 2.4)
    popill(c, L["p_outras"], RX, 868, 28, AMB, BG0, kd, t, td + 5.0)


def b_ferramenta(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ferr"], a)
    # exemplo ímpar: 3, 8, 5 → 3, 5, 8
    kb = a * ep(t, tb, 0.3)
    u = ease_io(prog(t, tb + 2.2, 0.8))
    xs = [250, 520, 790]
    orig, pos = [3, 8, 5], {0: 0, 1: 2, 2: 1}
    for i, v in enumerate(orig):
        x = xs[i] + (xs[pos[i]] - xs[i]) * u
        y = 330 - 60 * math.sin(math.pi * u) * (1 if i == 1 else 0)
        meio = pos[i] == 1 and t >= tb + 4.0
        bolinha(c, x, y, v, kb, CYA if meio else INK2, glow=1.0 if meio else 0, k=pop(t, tb + i * 0.4, 0.3))
    # exemplo par: 2, 4, 6, 10 → os do meio 4 e 6
    kc = a * ep(t, tc + 1.2, 0.3)
    xs2 = [200, 420, 640, 860]
    for i, v in enumerate([2, 4, 6, 10]):
        meio = i in (1, 2) and t >= tc + 3.0
        bolinha(c, xs2[i], 640, v, kc, MNT if meio else INK2, glow=1.0 if meio else 0, k=pop(t, tc + 1.2 + i * 0.3, 0.3))
    kd = a * ep(t, td + 1.0, 0.3)
    if kd > 0:
        c.drawLine(xs2[1], 700, xs2[1], 730, paint(MNT, kd, stroke=3)); c.drawLine(xs2[2], 700, xs2[2], 730, paint(MNT, kd, stroke=3))
        c.drawLine(xs2[1], 730, xs2[2], 730, paint(MNT, kd, stroke=3))
        label(c, "5", (xs2[1] + xs2[2]) / 2, 780, kd * ep(t, td + 3.4, 0.3), 54, MNT, "black")
    board(c, a)
    label(c, L["meio_def"], RX, 270, a * ep(t, ta + 0.6, 0.3), 46, CYA, "black")
    label(c, L["ordem"], RX, 345, a * ep(t, ta + 2.6, 0.3), 42, WHITE, "black")
    label(c, L["impar"], RX, 470, a * ep(t, tb + 4.0, 0.3), 36, INK2, "bold")
    eq(c, [("3, ", WHITE), ("5", CYA), (", 8  →  5", WHITE)], 540, a * ep(t, tb + 4.0, 0.3), 46)
    label(c, L["par"], RX, 660, a * ep(t, tc, 0.3), 36, INK2, "bold")
    eq(c, [("(4 + 6) ÷ 2 = ", WHITE), ("5", MNT)], 770, a * ep(t, td + 1.0, 0.3), 64, box=MNT)


@lru_cache(None)
def _leitura():
    """instantes (absolutos) em que a voz lê cada um dos 10 valores da lista ordenada (cena 03): tirados das palavras do
    Whisper (analise/voz.json, parte 1), deslocados para o vídeo pelo "Passo um" que abre a cena"""
    import json
    from pathlib import Path
    raiz = Path(__file__).resolve().parent.parent
    tp = json.loads((raiz / "audio" / "tempos.json").read_text(encoding="utf-8"))
    sc = next(x for x in tp["scenes"] if x["id"] == "03")
    ws = json.loads((raiz / "analise" / "voz.json").read_text(encoding="utf-8"))[0]["words"]
    i0 = [j for j, w in enumerate(ws) if w["w"].startswith("Passo")][0]          # 1º "Passo" = início da cena 03
    desl = sc["start"] + sc["cues"]["a"] - ws[i0]["s"]
    seq = ["320", "340", "350", "360", "380", "380", "390", "390", "390", "400"]
    out, j = [], i0
    for v in seq:
        while j < len(ws) and ws[j]["w"].strip(",.") != v:
            j += 1
        if j == len(ws):
            return []
        out.append(ws[j]["s"] + desl); j += 1
    return out


def _ordenada(i, k, t):
    """realce da ficha na posição k enquanto a lista ordenada é lida"""
    ts = _leitura()
    if len(ts) < 10 or t < ts[0]:
        return None
    t0 = ts[k]
    t1 = ts[k + 1] if k < 9 else t0 + 0.9
    falando = t0 <= t < t1
    return dict(borda=AMB if falando else (CYA if t >= t0 else INK2), glow=1.0 if falando else 0.0)


def b_ordenar(c, t, C, B):
    ta, tb, tc = (C[f"03.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ord"], a)
    u = prog(t, ta + 2.0, 2.2)
    passo = (tc - tb) / 10.4
    coluna(c, a, u, lambda i, k: _ordenada(i, k, t))
    chave(c, LX + FW / 2 + 16, _y(0) - 20, _y(9) + 20, "", a * ep(t, ta + 4.2, 0.3) * (1 - ep(t, tc, 0.3)), INK2)
    if t >= tc:   # os repetidos
        kc = a * ep(t, tc + 1.0, 0.3)
        for k0, k1, s in ((4, 5, "× 2"), (6, 8, "× 3")):
            chave(c, LX + FW / 2 + 16, _y(k0) - 22, _y(k1) + 22, s, kc, AMB)
    board(c, a)
    label(c, L["crescente"], RX, 270, a * ep(t, ta + 1.2, 0.3), 42, WHITE, "black")
    l1 = "320 · 340 · 350 · 360 · 380"
    l2 = "380 · 390 · 390 · 390 · 400"
    label(c, l1, RX, 420, a * ep(t, tb, 0.3), 50, WHITE, "black")
    label(c, l2, RX, 510, a * ep(t, _leitura()[5] if len(_leitura()) == 10 else tb + 5 * passo, 0.3), 50, WHITE, "black")
    label(c, L["repete"], RX, 660, a * ep(t, tc + 0.6, 0.3), 38, AMB, "black")


def b_meio(c, t, C, B):
    ta, tb, tc = (C[f"04.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_meio"], a)
    km = ep(t, tc, 0.3)
    coluna(c, a, 1, lambda i, k: dict(borda=CYA, glow=km, cor_v=CYA) if k in (4, 5) and km > 0 else None)
    kb = a * ep(t, tb, 0.3)
    chave(c, LX + FW / 2 + 16, _y(0) - 22, _y(4) - 34, L["antes"], kb * ep(t, tb + 2.6, 0.3), INK2)
    chave(c, LX + FW / 2 + 16, _y(5) + 34, _y(9) + 22, L["depois"], kb * ep(t, tb + 3.6, 0.3), INK2)
    if kb > 0:   # a linha do meio, entre o 5º e o 6º
        ym = (_y(4) + _y(5)) / 2
        pd = paint(CYA, kb, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([14, 10], 0))
        c.drawLine(LX - FW / 2 - 60, ym, LX + FW / 2 + 10, ym, pd)
        label(c, "5º", LX - FW / 2 - 40, _y(4), kb * km, 32, CYA, "black")
        label(c, "6º", LX - FW / 2 - 40, _y(5), kb * km, 32, CYA, "black")
    board(c, a)
    eq(c, [(L["dez_par"], WHITE)], 290, a * ep(t, ta + 1.4, 0.3), 54)
    eq(c, [(L["meio56"], CYA)], 420, kb, 54, box=CYA)
    label(c, L["quinto"], RX, 560, a * km, 46, WHITE, "black")


def b_mediana(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_med"], a)
    kb = ep(t, tb + 3.0, 0.3)
    coluna(c, a, 1, lambda i, k: dict(borda=MNT if kb > 0 else CYA, glow=1.0, cor_v=MNT if kb > 0 else CYA) if k in (4, 5) else None)
    ym = (_y(4) + _y(5)) / 2
    if kb > 0:
        label(c, "380", LX - FW / 2 - 90, ym, a * kb, 50, MNT, "black")
    board(c, a)
    label(c, L["mediana"], RX, 270, a * ep(t, ta + 0.8, 0.3), 40, INK2, "bold")
    eq(c, [("(380 + 380) ÷ 2", WHITE)], 390, a * ep(t, tb, 0.3), 66)
    eq(c, [("= ", WHITE), ("380", MNT), (" MB/s", INK2)], 520, a * kb, 80, box=MNT)
    ops = [("A", "360"), ("B", "370"), ("C", "380"), ("D", "390"), ("E", "400")]
    kc = a * ep(t, tc + 2.0, 0.3)
    for i, (le, v) in enumerate(ops):
        x = BX0 + 110 + i * 170
        ok = le == "C"
        k = kc * ep(t, tc + 2.0 + i * 0.08, 0.2)
        text_mid(c, le, x - 26, 760, 40, "black", MNT if ok else INK2, k)
        text_mid(c, v, x + 4, 760, 40, "black", WHITE if ok else INK2, k, align="left")
    kk = kc * ep(t, tc + 2.6, 0.3)
    if kk > 0:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 110 + 2 * 170 - 56, 760 - 36, 150, 72), 16, 16)
        c.drawRRect(r, paint(MNT, kk, stroke=4))


def b_pegadinha(c, t, C, B):
    ta, tb, tc = (C[f"06.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    u = 1 - prog(t, ta + 1.0, 1.8)   # volta para a ordem do quadro
    kb = ep(t, tb, 0.3)
    coluna(c, a, u, lambda i, k: dict(borda=RED, glow=kb, cor_v=RED) if i in (4, 5) and kb > 0 else None)
    if kb > 0:
        chave(c, LX + FW / 2 + 16, _y(4) - 24, _y(5) + 24, "5ª e 6ª" if not EN else "5th, 6th", a * kb, RED)
    board(c, a)
    label(c, L["sem_ordem"], RX, 270, a * ep(t, ta + 1.0, 0.3), 46, RED, "black")
    label(c, L["tabela"], RX, 345, a * ep(t, ta + 3.0, 0.3), 36, INK2, "bold")
    pos = eq(c, [("(340 + 380) ÷ 2 = ", WHITE), ("360", RED)], 480, a * ep(t, tb + 2.6, 0.3), 58)
    popill(c, "A ?", RX, 560, 34, RED, BG0, a * ep(t, tb + 5.0, 0.2), t, tb + 5.0)
    if pos:
        strike(c, pos[0][0], pos[-1][1], 480, a, ep(t, tc, 0.4))
    label(c, L["nao_meio"], RX, 680, a * ep(t, tc + 1.0, 0.3), 34, WHITE, "black")


def b_medidas(c, t, C, B):
    ta, tb, tc, td, te = (C[f"07.{k}"] for k in "abcde")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_outras"], a)

    def est(i, k):
        if te <= t:
            return dict(borda=MNT, glow=1.0, cor_v=MNT) if k in (4, 5) else None
        if td <= t:
            return dict(borda=RED, glow=1.0, cor_v=RED) if k == 9 else None
        if tc <= t:
            return dict(borda=AMB, glow=1.0, cor_v=AMB) if VALS[i] == 390 else None
        if tb <= t:
            return dict(borda=CYA, glow=0.5)
        return None
    coluna(c, a, 1, est)
    if tb <= t < tc:
        label(c, L["soma"], LX, _y(9) + 70, a * ep(t, tb + 1.0, 0.3), 36, CYA, "black")
    if tc <= t < td:
        chave(c, LX + FW / 2 + 16, _y(6) - 22, _y(8) + 22, L["vezes3"], a * ep(t, tc + 1.0, 0.3), AMB)
    board(c, a)
    rows = [("B", L["media"], n_("3.700") + " ÷ 10 = 370", tb + 1.0, CYA),
            ("D", L["moda"], "390", tc + 1.0, AMB),
            ("E", L["maior"], "400", td + 0.3, RED),
            ("C", L["mediana"], "380", te, MNT)]
    for j, (le, nome, s, t0, col) in enumerate(rows):
        y = 290 + j * 140
        k = a * ep(t, t0, 0.3)
        if k <= 0:
            continue
        c.drawCircle(BX0 + 80, y, 32, paint(col, k))
        text_mid(c, le, BX0 + 80, y, 36, "black", BG0, k)
        text_mid(c, nome + ":", BX0 + 135, y, 44, "black", col, k, align="left")
        text_mid(c, s, BX1 - 60, y, 46, "black", WHITE, k, align="right")
        if le == "C":
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(BX0 + 35, y - 50, BX1 - BX0 - 70, 100), 18, 18)
            c.drawRRect(r, paint(MNT, k, stroke=4))


def b_generaliza(c, t, C, B):
    ta, tb, tc = (C[f"08.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_gen"], a)
    ka = a * (1 - ep(t, tc, 0.3))
    if ka > 0:   # 11 valores (a 11ª ficha entra no fim) e o 6º no meio
        kb = ep(t, tb + 2.0, 0.3)
        passo = 60
        coluna(c, ka, 1, lambda i, k: dict(borda=CYA, glow=kb, cor_v=CYA) if k == 5 and kb > 0 else None,
               y0=210, passo=passo, extra=("C11", 410) if t >= ta + 1.5 else None)
        if kb > 0:
            chave(c, LX + FW / 2 + 16, 210 - 20, 210 + passo * 4 + 20, L["antes"], ka * kb, INK2)
            chave(c, LX + FW / 2 + 16, 210 + passo * 6 - 20, 210 + passo * 10 + 20, L["depois"], ka * kb, INK2)
            label(c, "6º", LX - FW / 2 - 40, 210 + passo * 5, ka * kb, 32, CYA, "black")
    kc = a * ep(t, tc, 0.3)
    if kc > 0:   # o desafio: C3 vira 420
        coluna(c, kc, 0, lambda i, k: dict(borda=AMB, glow=1.0, cor_v=AMB) if i == 2 else None,
               vals=VALS[:2] + [420] + VALS[3:])
        popill(c, L["desafio"], LX, 160, 30, AMB, BG0, kc, t, tc + 0.8)
    board(c, a)
    eq(c, [(L["onze"], WHITE)], 280, a * ep(t, tb, 0.3), 52)
    eq(c, [(L["meio6"], CYA)], 400, a * ep(t, tb + 2.0, 0.3), 50, box=CYA)
    eq(c, [(L["mediana_eq"], WHITE), ("380", MNT)], 520, a * ep(t, tb + 6.0, 0.3), 52)
    label(c, L["qual"], RX, 690, kc * ep(t, tc + 4.0, 0.3), 44, AMB, "black")
    label(c, L["comenta"], RX, 820, kc * ep(t, tc + 6.0, 0.3), 38, AMB, "extrabold")


def b_resumo(c, t, C, B):
    ks = [C[f"09.{k}"] for k in "bcde"]
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resumo"], a)
    for i, (s, t0) in enumerate(zip(L["passos"], ks)):
        y = 280 + i * 160
        ki = a * ep(t, t0, 0.3)
        if ki <= 0:
            continue
        x = 330
        c.drawCircle(x, y, 34, paint(AMB, ki))
        text_mid(c, str(i + 1), x, y, 38, "black", BG0, ki)
        text_mid(c, s, x + 70, y, 52, "black", WHITE, ki, align="left")
        check(c, 1640, y, 24, ki * ep(t, t0 + 0.5, 0.2))


def _icone(c, i, cx, cy, a, t):
    """miniatura de cada aula: barras com a linha da média · lista com o meio · tabela"""
    if i == 0:
        for j, h in enumerate((60, 110, 80, 130)):
            rrect(c, cx - 110 + j * 58, cy + 60 - h, 44, h, 8, CYA, a)
        pd = paint(AMB, a, stroke=4); pd.setPathEffect(skia.DashPathEffect.Make([12, 8], 0))
        c.drawLine(cx - 125, cy - 35, cx + 125, cy - 35, pd)
    elif i == 1:
        for j, v in enumerate((3, 5, 8)):
            bolinha(c, cx - 100 + j * 100, cy, v, a, CYA if j == 1 else INK2, glow=1.0 if j == 1 else 0)
    else:
        for r in range(4):
            for q in range(2):
                rrect(c, cx - 120 + q * 125, cy - 80 + r * 42, 115, 36, 6, MNT if r == 0 else BG2, a)


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
        for j, v in enumerate((320, 360, 380, 390, 400)):
            bolinha(c, 960 - 280 + j * 140, 790, v, kl, MNT if j == 2 else INK2, glow=1.0 if j == 2 else 0, k=0.9)


BLOCKS = dict(gancho=b_gancho, ferramenta=b_ferramenta, ordenar=b_ordenar, meio=b_meio, mediana=b_mediana,
              pegadinha=b_pegadinha, medidas=b_medidas, generaliza=b_generaliza, resumo=b_resumo, aulas=b_aulas)
