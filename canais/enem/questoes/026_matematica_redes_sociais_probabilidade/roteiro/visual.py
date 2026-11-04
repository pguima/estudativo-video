"""Visual — Estudativo · Questão de Matemática 026 (aula horizontal 1920x1080): ENEM 2025, questão 145, redes sociais e
probabilidade (porcentagem de porcentagem). Design system de matemática: _ferramentas/matematica.py (paleta, quadro, legenda).
Cores com função: âmbar = as mulheres (o dado do infográfico, 60%), ciano = os homens que acessam (o que a questão pede),
menta = a resposta e a conferência, coral = as armadilhas, cinza vazado = quem não acessa redes sociais.
Figura principal: 100 internautas imaginários numa grade 10 × 10 (cem()): 90 acessam (54 mulheres + 36 homens), 10 não."""
import idioma
import matematica
from matematica import *  # noqa

IDIOMAS_NO_CODIGO = True
EN = idioma.LANG == "en"
ARQUIVO_FINAL = "estudativo_questao_026_matematica_redes_sociais_probabilidade.mp4"
MARCA = ""
ENTRADA_SECA = True   # render.py: o enunciado aparece no primeiro quadro, sem fade

_SFX = {"01.d": "shimmer", "02.b": "data", "02.c": "data", "02.d": "lock", "03.b": "data", "03.c": "data", "03.d": "confirm",
        "04.c": "data", "04.d": "alert", "05.c": "data", "06.b": "data", "06.c": "data", "07.b": "data", "07.c": "confirm",
        "07.d": "confirm", "08.b": "impact", "08.c": "confirm", "08.d": "confirm", "09.b": "deny", "09.c": "deny",
        "09.d": "deny", "10.b": "alert", "12.a": "shimmer", "12.f": "lock"}
SOM = dict(intro=False, ganho_trilha=0.0, lufs=-14, bpm=100, sfx=_SFX)   # aula horizontal: sem trilha de fundo

T = dict(   # (inglês, português)
    selo=("MATH QUESTION · 026", "QUESTÃO DE MATEMÁTICA · 026"),
    canal=("ESTUDATIVO ENGLISH", "ESTUDATIVO"),
    s_gancho=("THE QUESTION", "A QUESTÃO"), s_prob=("TOOL 1 · PROBABILITY", "FERRAMENTA 1 · PROBABILIDADE"),
    s_pct=("TOOL 2 · A PERCENTAGE OF A PERCENTAGE", "FERRAMENTA 2 · PORCENTAGEM DE PORCENTAGEM"),
    s_sobra=("TOOL 3 · WHAT IS LEFT", "FERRAMENTA 3 · O QUE SOBRA"),
    s_univ=("STEP 1 · WHO IS IN THE DRAW?", "PASSO 1 · DE ONDE SE SORTEIA?"), s_ac=("STEP 2 · WHO USES IT", "PASSO 2 · QUEM ACESSA"),
    s_hom=("STEP 3 · HOW MANY MEN", "PASSO 3 · QUANTOS SÃO HOMENS"), s_resp=("THE ANSWER", "A RESPOSTA"),
    s_peg=("WHY THE OTHERS ARE WRONG", "POR QUE AS OUTRAS ESTÃO ERRADAS"), s_des=("CHALLENGE", "DESAFIO"),
    s_resumo=("SUMMARY", "RESUMO"),
    enem=("ENEM 2025 · question 145", "ENEM 2025 · questão 145"), rede=("social networks", "redes sociais"),
    d90=("90% use social networks", "90% acessam redes sociais"), d60=("60% of those: women", "60% de quem acessa: mulheres"),
    pede=("P(man who uses it) = ", "P(homem que acessa) = "), nao40=("why it isn't 40%", "por que não é 40%"),
    servem=("cases that work", "casos que servem"), todos=("all the cases", "todos os casos"),
    turma=("40 students · 10 wear glasses", "40 alunos · 10 usam óculos"), sorteio=("the group you draw from", "o grupo de onde se sorteia"),
    metade=("half of half = ¼", "metade da metade = ¼"), p50=("50% of 50% = 25%", "50% de 50% = 25%"),
    de_vezes=("“of” → ×", "“de” → ×"), conta05=("0.5 × 0.5 = 0.25", "0,5 × 0,5 = 0,25"),
    acessa=("who uses it", "quem acessa"), todo=("all internet users", "todos os internautas"),
    mulheres=("women", "mulheres"), homens=("men", "homens"), naoac=("don't use it", "não acessam"),
    divide=("users = women + men", "quem acessa = mulheres + homens"), sobra=("100% − 60% = 40%", "100% − 60% = 40%"),
    de_quem=("40% of the USERS", "40% de quem ACESSA"),
    qualquer=("draw ANY internet user", "sorteio: QUALQUER internauta"), imagine=("imagine 100", "imagine 100"),
    c90=("90% of 100 = 90", "90% de 100 = 90"), c10=("100 − 90 = 10", "100 − 90 = 10"),
    c54=("60% of 90 = 0.6 × 90 = 54", "60% de 90 = 0,6 × 90 = 54"), c36=("90 − 54 = 36", "90 − 54 = 36"),
    c36b=("40% of 90 = 0.4 × 90 = 36", "40% de 90 = 0,4 × 90 = 36"),
    h36=("36 men who use it", "36 homens que acessam"), confere=("54 + 36 + 10 = 100 ✓", "54 + 36 + 10 = 100 ✓"),
    alt=("ANSWER", "ALTERNATIVA"),
    pC=("C: 40% of EVERYONE", "C: 40% de TODO MUNDO"), pADE=("A, D, E: only the users below", "A, D, E: só quem acessa embaixo"),
    p3690=("and even so: 36/90", "e mesmo assim: 36/90"),
    des1=("draw any internet user", "sorteando um internauta"), des2=("P(woman who uses it) = ?", "P(mulher que acessa) = ?"),
    comenta=("answer in the comments!", "responda nos comentários!"),
    passos=(["what works ÷ the whole group you draw from", "a percentage of a percentage = ×",
             "imagine 100 people"],
            ["o que serve ÷ todo o grupo do sorteio", "porcentagem de porcentagem = ×",
             "imagine 100 pessoas"]),
    s_aulas=("FULL LESSONS ON THE CHANNEL", "AULAS COMPLETAS NO CANAL"), aula=("LESSON", "AULA"),
    aulas=([("Percentages", ""), ("Probability", ""), ("Fractions", "and decimals")],
           [("Porcentagem", ""), ("Probabilidade", ""), ("Frações", "e decimais")]),
    no_canal=("search the channel: Estudativo English", "procure no canal: Estudativo"),
    inscreva=("SUBSCRIBE FOR THE NEXT QUESTION", "INSCREVA-SE PARA A PRÓXIMA QUESTÃO"),
)

L = {k: (v[0] if EN else v[1]) for k, v in T.items()}
n_ = lambda s: s.replace(",", ".") if EN else s   # noqa: E731
_EXTRA = [] if EN else (
    [(f"{matematica._extenso_pt(n)} por cento", f"{n}%") for n in (25, 40, 50, 60, 90)] +
    [("dois mil e vinte e cinco", "2025"), ("um quarto", "¼"), ("zero vírgula vinte e cinco", "0,25"),
     ("zero vírgula cinco", "0,5"), ("passo um", "Passo 1"), ("passo dois", "Passo 2"), ("passo três", "Passo 3")])
matematica.NUMEROS_EXTRA[:] = sorted(_EXTRA, key=lambda p: -len(p[0].split()))
OPS = [("A", "30", "90"), ("B", "36", "100"), ("C", "40", "100"), ("D", "40", "90"), ("E", "46", "90")]


def OVERLAY(c, t):
    selo(c, L["selo"], t)


# ---------------------------------------------------------------- peças
def _mix(h1, h2, u):
    u = clamp(u)
    a = [int(h1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(h2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{int(x + (y - x) * u):02X}" for x, y in zip(a, b))


def boneco(c, x, y, s, cor, a, vazado=0.0, oculos=0.0, k=1.0):
    """pictograma de pessoa (cabeça + tronco arredondado), centrado em (x, y), altura ≈ s; vazado = só o contorno"""
    if a <= 0 or k <= 0:
        return
    c.save(); c.translate(x, y); c.scale(k, k)
    hr = 0.19 * s
    corpo = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-0.3 * s, -0.12 * s, 0.6 * s, 0.6 * s), 0.26 * s, 0.26 * s)
    if vazado < 1:
        c.drawCircle(0, -0.36 * s, hr, paint(cor, a * (1 - vazado)))
        c.drawRRect(corpo, paint(cor, a * (1 - vazado)))
    if vazado > 0:
        c.drawCircle(0, -0.36 * s, hr, paint(cor, a * vazado, stroke=2.5))
        c.drawRRect(corpo, paint(cor, a * vazado, stroke=2.5))
    if oculos > 0:
        for dx in (-0.085, 0.085):
            c.drawCircle(dx * s, -0.37 * s, 0.065 * s, paint(BG0, a * oculos, stroke=2.4))
        c.drawLine(-0.02 * s, -0.37 * s, 0.02 * s, -0.37 * s, paint(BG0, a * oculos, stroke=2.4))
    c.restore()


NM, NH = 54, 36   # mulheres e homens entre os 100 imaginados (os 10 últimos não acessam)
CEL_X, CEL_Y, S_BON = 72, 70, 56


def pos_cem(i, cx=LX, cy=545):
    return cx + (i % 10 - 4.5) * CEL_X, cy + (i // 10 - 4.5) * CEL_Y


def cem(c, a, t, t_in=None, t_ac=None, t_gen=None, t_hom=None, foco=None, foco_a=0.0, cx=LX, cy=545, alvo=None):
    """os 100 internautas: t_in = entram (brancos); t_ac = os 10 que não acessam ficam cinza vazado; t_gen = as 54 mulheres
    ficam âmbar; t_hom = os 36 homens ficam ciano; foco = 'H' | 'M' | 'N' (apaga os outros); alvo = 'N' pisca em coral"""
    if a <= 0:
        return
    for i in range(100):
        x, y = pos_cem(i, cx, cy)
        k = pop(t, t_in + i * 0.012, 0.25) if t_in is not None else 1.0
        if k <= 0:
            continue
        grupo = "M" if i < NM else "H" if i < NM + NH else "N"
        cor, vaz = WHITE, 0.0
        if grupo == "N" and t_ac is not None:
            u = ep(t, t_ac + (i - 90) * 0.04, 0.3)
            cor, vaz = _mix(WHITE, INK2, u), u
        if grupo == "M" and t_gen is not None:
            cor = _mix(WHITE, AMB, ep(t, t_gen + i * 0.015, 0.3))
        if grupo == "H" and t_hom is not None:
            cor = _mix(WHITE, CYA, ep(t, t_hom + (i - NM) * 0.02, 0.3))
        al = a * (1 - 0.75 * foco_a * (foco is not None and grupo != foco))
        if alvo == grupo:
            cor = _mix(cor, RED, 0.5 + 0.5 * math.sin(t * 6))
        boneco(c, x, y, S_BON, cor, al, vazado=vaz, k=k)


def frac(c, num, den, cx, cy, size, a, cn=WHITE, cd=WHITE, linha=WHITE, peso="black"):
    """fração empilhada centrada em (cx, cy) = a altura do traço"""
    if a <= 0:
        return
    w = max(text_w(num, peso, size), text_w(den, peso, size)) + size * 0.3
    text_mid(c, num, cx, cy - size * 0.62, size, peso, cn, a)
    c.drawLine(cx - w / 2, cy, cx + w / 2, cy, paint(linha, a, stroke=max(3, size * 0.07), cap_round=True))
    text_mid(c, den, cx, cy + size * 0.66, size, peso, cd, a)
    return w


def opcoes(c, a, t, y, t0, marca=None, cores=None, k_op=None):
    """as cinco alternativas (frações) numa linha do quadro; marca = {letra: 'certo'|'errado'}"""
    for j, (le, nu, de) in enumerate(OPS):
        k = a * (k_op[j] if k_op else ep(t, t0 + j * 0.15, 0.3))
        if k <= 0:
            continue
        x = BX0 + 110 + j * 170
        col = (cores or {}).get(le, INK2)
        c.drawCircle(x, y - 90, 26, paint(col, k))
        text_mid(c, le, x, y - 90, 30, "black", BG0, k)
        frac(c, nu, de, x, y + 20, 52, k)
        m = (marca or {}).get(le)
        if m == "certo":
            check(c, x + 52, y - 92, 15, k)
        elif m == "errado":
            cross(c, x + 52, y - 92, 15, k)


def _card_img(c, img, a, w=760, cx=LX, cy=545, hmax=830):
    h = img.height() * w / img.width()
    if h > hmax:
        h = hmax
        w = img.width() * h / img.height()
    x, y = cx - w / 2, cy - h / 2
    rrect(c, x - 14, y - 14, w + 28, h + 28, 18, "#FFFFFF", a)
    c.drawImageRect(img, skia.Rect.MakeXYWH(x, y, w, h), skia.SamplingOptions(skia.FilterMode.kLinear), paint(WHITE, a))


@lru_cache(None)
def _img(nome):
    from pathlib import Path
    return skia.Image.open(str(Path(__file__).resolve().parent.parent / "enunciado" / nome))


def pizza(c, cx, cy, r, a, u_meia, u_quarto):
    """a pizza: metade marcada, depois a metade da metade (¼) em destaque"""
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(BG2, a))
    c.drawCircle(cx, cy, r, paint(WHITE, a, stroke=4))
    box = skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r)
    if u_meia > 0:
        p = skia.Path(); p.moveTo(cx, cy); p.arcTo(box, -90, 180 * u_meia, False); p.close()
        c.drawPath(p, paint(AMB, 0.45 * a))
        c.drawLine(cx, cy - r, cx, cy + r, paint(WHITE, a * ep(u_meia, 0.0, 1.0), stroke=4))
    if u_quarto > 0:
        p = skia.Path(); p.moveTo(cx, cy); p.arcTo(box, -90, 90 * u_quarto, False); p.close()
        c.drawPath(p, paint(CYA, a))
        c.drawLine(cx, cy, cx + r, cy, paint(WHITE, a * clamp(u_quarto * 2), stroke=4))


def barra(c, x, y, w, h, a, partes, rot=None):
    """barra dividida: partes = [(fração, cor, rótulo, vazado)]"""
    if a <= 0:
        return
    xx = x
    for fr, cor, rt, vaz in partes:
        ww = w * fr
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx + 2, y, ww - 4, h), 12, 12)
        c.drawRRect(r, paint(cor, a * (0.25 if vaz else 0.9)))
        if vaz:
            c.drawRRect(r, paint(cor, a, stroke=3))
        if rt:
            text_mid(c, rt, xx + ww / 2, y + h / 2, 34, "black", WHITE if vaz else BG0, a)
        xx += ww
    if rot:
        text_mid(c, rot, x, y - 34, 30, "extrabold", INK2, a, align="left")


def chave(c, x0, x1, y, a, cor, rot=None):
    """chave horizontal embaixo de um trecho (x0 → x1), com rótulo"""
    if a <= 0:
        return
    p = skia.Path(); m = (x0 + x1) / 2
    p.moveTo(x0, y); p.quadTo(x0, y + 18, x0 + 20, y + 18); p.lineTo(m - 16, y + 18); p.quadTo(m, y + 18, m, y + 34)
    p.quadTo(m, y + 18, m + 16, y + 18); p.lineTo(x1 - 20, y + 18); p.quadTo(x1, y + 18, x1, y)
    c.drawPath(p, paint(cor, a, stroke=4))
    if rot:
        text_mid(c, rot, m, y + 66, 32, "black", cor, a)


# ---------------------------------------------------------------- cenas
def b_gancho(c, t, C, B):
    ta, tb, tc, td = (C[f"01.{k}"] for k in "abcd")
    a = 1 - prog(t, B["end"], 0.25)   # cheio desde o quadro 0
    header(c, L["s_gancho"], a)
    _card_img(c, _img("questao_topo.png"), a)
    board(c, a)
    label(c, L["enem"], RX, 250, a, 40, INK2, "extrabold")
    label(c, L["rede"], RX, 330, a, 44, WHITE, "black")
    eq(c, [(L["d90"], WHITE)], 450, a * ep(t, ta + 4.6, 0.3), 46)
    eq(c, [(L["d60"], AMB)], 540, a * ep(t, tb + 1.6, 0.3), 46)
    eq(c, [(L["pede"], WHITE), ("?", CYA)], 680, a * ep(t, tc + 2.0, 0.3), 54, box=CYA)
    popill(c, L["nao40"], RX, 820, 30, RED, BG0, a * ep(t, td, 0.3), t, td + 0.2)


def b_probabilidade(c, t, C, B):
    ta, tb, tc, td = (C[f"02.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_prob"], a)
    for i in range(40):   # a turma: 40 alunos, 10 de óculos
        x, y = LX + (i % 10 - 4.5) * 72, 420 + (i // 10) * 110
        k = pop(t, tc + i * 0.02, 0.25)
        oc = i in (1, 6, 12, 15, 19, 23, 28, 30, 34, 37)
        boneco(c, x, y, 70, CYA if (oc and t >= tc + 2.4) else WHITE, a * k, oculos=ep(t, tc + 2.4, 0.3) if oc else 0)
    label(c, L["turma"], LX, 900, a * ep(t, tc, 0.3), 40, WHITE, "black")
    board(c, a)
    kb = a * ep(t, tb, 0.3)
    frac(c, L["servem"], L["todos"], RX, 340, 52, kb, cn=CYA, cd=WHITE)
    label(c, "P =", BX0 + 80, 340, kb, 52, WHITE, "black")
    kc = a * ep(t, tc + 4.6, 0.3)
    frac(c, "10", "40", RX, 620, 80, kc, cn=CYA)
    label(c, "P =", RX - 150, 620, kc, 60, WHITE, "black")
    kd = a * ep(t, td, 0.3)
    if kd > 0:
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(RX - 70, 640, 140, 100), 16, 16)
        c.drawRRect(r, blur_paint(AMB, 0.4 * kd, 14))
        c.drawRRect(r, paint(AMB, kd, stroke=4))
        label(c, L["sorteio"], RX, 810, kd, 38, AMB, "black")


def b_porcentagem(c, t, C, B):
    ta, tb, tc, td = (C[f"03.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_pct"], a)
    pizza(c, LX, 520, 270, a * ep(t, ta + 0.4, 0.4), ep(t, tb + 0.4, 0.8), ep(t, tb + 1.8, 0.8))
    label(c, L["metade"], LX, 880, a * ep(t, tb + 1.8, 0.3), 44, CYA, "black")
    board(c, a)
    eq(c, [(L["p50"], WHITE)], 360, a * ep(t, tc, 0.3), 60)
    eq(c, [(L["de_vezes"], AMB)], 520, a * ep(t, td, 0.3), 60)
    eq(c, [(n_(L["conta05"]), WHITE)], 680, a * ep(t, td + 2.4, 0.3), 60, box=MNT)


def b_sobra(c, t, C, B):
    ta, tb, tc, td = (C[f"04.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_sobra"], a)
    kb = a * ep(t, tb, 0.3)
    u = ep(t, tc, 0.5)
    barra(c, 120, 330, 800, 110, kb, [(0.6, AMB, "60% " + L["mulheres"] if u > 0.5 else "", False),
                                      (0.4, _mix(WHITE, CYA, u), "40%" if u > 0.5 else "", False)], rot=L["acessa"])
    kd = a * ep(t, td, 0.4)   # a barra de todos os internautas: quem acessa é só 90% dela
    barra(c, 120, 640, 800, 110, kd, [(0.9, WHITE, L["acessa"] + " · 90%", False), (0.1, INK2, "", True)], rot=L["todo"])
    if kd > 0:
        c.drawLine(122, 445, 122, 588, _dash(INK2, kd))
        c.drawLine(918, 445, 120 + 720, 636, _dash(INK2, kd))
    board(c, a)
    eq(c, [(L["divide"], WHITE)], 340, kb, 44)
    eq(c, [(L["sobra"], CYA)], 500, a * ep(t, tc, 0.3), 60)
    eq(c, [(L["de_quem"], AMB)], 680, kd, 54, box=RED)


def _dash(col, a, w=3):
    p = paint(col, a, stroke=w)
    p.setPathEffect(skia.DashPathEffect.Make([8, 8], 0))
    return p


def b_universo(c, t, C, B):
    ta, tb, tc = (C[f"05.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_univ"], a)
    cem(c, a, t, t_in=tc + 3.2)
    board(c, a)
    eq(c, [(L["qualquer"], WHITE)], 340, a * ep(t, tb, 0.3), 46, box=CYA)
    kc = a * ep(t, tc, 0.3)
    frac(c, "?", L["todo"], RX, 600, 56, kc, cn=CYA, cd=WHITE)
    label(c, "P =", BX0 + 90, 600, kc, 56, WHITE, "black")
    popill(c, L["imagine"], RX, 820, 34, AMB, BG0, a * ep(t, tc + 3.2, 0.3), t, tc + 3.4)


def b_acessam(c, t, C, B):
    ta, tb, tc = (C[f"06.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_ac"], a)
    cem(c, a, t, t_ac=tc)
    kb = a * ep(t, tb + 1.0, 0.3)
    chave(c, LX - 310, LX + 310, 890, a * ep(t, tc, 0.3), INK2, "10 " + L["naoac"])
    board(c, a)
    eq(c, [(L["c90"], WHITE)], 380, kb, 60, box=MNT)
    eq(c, [(L["c10"], INK2)], 560, a * ep(t, tc, 0.3), 60)


def b_homens(c, t, C, B):
    ta, tb, tc, td = (C[f"07.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_hom"], a)
    cem(c, a, t, t_ac=-99, t_gen=tb + 1.0, t_hom=tc + 1.0)
    board(c, a)
    eq(c, [(n_(L["c54"]), AMB)], 330, a * ep(t, tb + 1.0, 0.3), 50)
    eq(c, [(L["c36"], CYA)], 500, a * ep(t, tc + 1.0, 0.3), 60)
    eq(c, [(n_(L["c36b"]), CYA)], 690, a * ep(t, td + 1.0, 0.3), 50, box=MNT)


def b_resposta(c, t, C, B):
    ta, tb, tc, td = (C[f"08.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_resp"], a)
    foco = ep(t, ta + 0.6, 0.4) * (1 - ep(t, tc, 0.4))
    cem(c, a, t, t_ac=-99, t_gen=-99, t_hom=-99, foco="H", foco_a=foco)
    board(c, a)
    eq(c, [(L["h36"], CYA)], 280, a * ep(t, ta + 0.6, 0.3) * (1 - ep(t, td, 0.3)), 46)
    kb = a * ep(t, tb, 0.3)
    k = pop(t, tb, 0.4)
    c.save(); c.translate(RX, 480); c.scale(k, k); c.translate(-RX, -480)
    frac(c, "36", "100", RX + 60, 480, 96, kb * (1 - ep(t, td, 0.3)), cn=CYA, cd=WHITE, linha=MNT)
    label(c, "P =", RX - 110, 480, kb * (1 - ep(t, td, 0.3)), 72, WHITE, "black")
    c.restore()
    eq(c, [(L["confere"], MNT)], 690, a * ep(t, tc + 1.0, 0.3) * (1 - ep(t, td, 0.3)), 50)
    kd = a * ep(t, td, 0.3)
    if kd > 0:
        opcoes(c, kd, t, 430, td + 0.35, marca={"B": "certo"}, cores={"B": MNT})   # entram depois que a fração sai
        eq(c, [(L["alt"] + " ", WHITE), ("B", MNT)], 720, kd, 64, box=MNT)


def b_pegadinhas(c, t, C, B):
    ta, tb, tc, td = (C[f"09.{k}"] for k in "abcd")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_peg"], a)
    alvo = "N" if tb + 1.0 <= t < tc else None
    some = ep(t, tc + 1.0, 0.4) * (1 - ep(t, td + 2.0, 0.4))   # A, D, E: os 10 que não acessam saem do grupo do sorteio
    cem(c, a, t, t_ac=-99, t_gen=-99, t_hom=-99, alvo=alvo, foco="H" if some > 0 else None, foco_a=0.0)
    if some > 0:   # cobre a última fila (fora do sorteio dessas alternativas)
        x0, y0 = pos_cem(90)
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 - 34, y0 - 44, 10 * CEL_X + 6, 74), 14, 14)
        c.drawRRect(r, paint(BG0, 0.85 * a * some))
        c.drawRRect(r, _dash(RED, a * some))
    board(c, a)
    marca, cores = {}, {}
    if t >= tb:
        marca["C"], cores["C"] = "errado", RED
    if t >= tc:
        for le in "ADE":
            marca[le], cores[le] = "errado", RED
    if t >= td + 2.0:
        marca["B"], cores["B"] = "certo", MNT
    opcoes(c, a, t, 330, ta + 0.2, marca=marca, cores=cores)
    eq(c, [(L["pC"], RED)], 560, a * ep(t, tb, 0.3), 46)
    eq(c, [(L["pADE"], RED)], 660, a * ep(t, tc, 0.3), 42)
    eq(c, [(L["p3690"], INK2)], 770, a * ep(t, td + 4.4, 0.3), 42)


def b_desafio(c, t, C, B):
    ta, tb, tc = (C[f"10.{k}"] for k in "abc")
    a = fade(t, B["start"], B["end"])
    header(c, L["s_des"], a)
    cem(c, a, t, t_ac=-99, t_gen=-99, t_hom=-99, foco="M", foco_a=ep(t, tb + 2.0, 0.4))
    board(c, a)
    label(c, L["des1"], RX, 330, a * ep(t, tb, 0.3), 44, WHITE, "black")
    eq(c, [(L["des2"], AMB)], 480, a * ep(t, tb + 2.0, 0.3), 50, box=AMB)
    label(c, L["comenta"], RX, 660, a * ep(t, tc, 0.3), 40, AMB, "extrabold")


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
    """miniatura de cada aula: % · um sorteio (pessoas, uma em destaque) · ½ = 0,5"""
    if i == 0:
        text_mid(c, "%", cx, cy, 130, "black", CYA, a)
    elif i == 1:
        for j in range(5):
            boneco(c, cx - 120 + j * 60, cy + 20, 70, AMB if j == 2 else WHITE, a)
    else:
        frac(c, "1", "2", cx - 80, cy, 54, a, cn=MNT, cd=MNT)
        text_mid(c, n_("= 0,5"), cx + 50, cy, 54, "black", WHITE, a)


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
        if l2:
            text_mid(c, l1, cx, 610, sz, "black", WHITE, kk)
            text_mid(c, l2, cx, 610 + sz * 1.25, sz, "black", cores[i], kk)
        else:   # nome de uma palavra só: uma linha, na cor do cartão
            text_mid(c, l1, cx, 610 + sz * 0.62, sz, "black", cores[i], kk)
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
            c.drawCircle(x, 790, 38, paint(MNT if v == "B" else INK2, kl, stroke=4))
            text_mid(c, v, x, 790, 38, "black", WHITE, kl)


BLOCKS = dict(gancho=b_gancho, probabilidade=b_probabilidade, porcentagem=b_porcentagem, sobra=b_sobra,
              universo=b_universo, acessam=b_acessam, homens=b_homens, resposta=b_resposta, pegadinhas=b_pegadinhas,
              desafio=b_desafio, resumo=b_resumo, aulas=b_aulas)
